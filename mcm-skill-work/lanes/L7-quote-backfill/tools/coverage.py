"""Recount the L7 quote backfill against the lane records and write reports/.

Usage:
    python -I -X utf8 lanes/L7-quote-backfill/tools/coverage.py

The counts here are computed from the lane records and the emitted quote files, never
typed by hand: the denominator is the number of coded groups in the records, the emitted
count is the number of lines in quotes-<lane>.jsonl, and every gap is printed.
"""

from __future__ import annotations

import collections
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LANES = os.path.join(ROOT, "lanes")
OUT_DIR = os.path.join(ROOT, "lanes", "L7-quote-backfill")
REPORTS = os.path.join(OUT_DIR, "reports")

LANE_DIRS = {
    "B": "L4-b-ledger",
    "C": "L3-c-ledger",
    "D": "L2-d-ledger",
    "E": "L5-e-ledger",
    "F": "L1-f-structure",
}

JOBS = {
    "route",
    "define",
    "source",
    "select",
    "derive",
    "compute",
    "read-figure",
    "compare",
    "check",
    "limit",
    "mechanism",
    "interpret",
    "handoff",
}


def base_label(label: str) -> str:
    """Normalise a compound or namespaced label to its leading job."""
    head = label.split("+", 1)[0]
    return head.split(":", 1)[-1]


def record_papers(lane: str) -> list[str]:
    records = os.path.join(LANES, LANE_DIRS[lane], "records")
    return [
        name[:-5]
        for name in sorted(os.listdir(records))
        if name.endswith(".json") and not name.endswith(".skipped.json")
    ]


def denominator(lane: str) -> dict:
    papers = record_papers(lane)
    chapters = 0
    groups = 0
    blocks = 0
    labels: collections.Counter[str] = collections.Counter()
    for paper in papers:
        path = os.path.join(LANES, LANE_DIRS[lane], "records", paper + ".json")
        with open(path, encoding="utf-8") as handle:
            chapters_of_paper = json.load(handle)
        if not isinstance(chapters_of_paper, list):
            continue
        for chapter in chapters_of_paper:
            if not isinstance(chapter, dict):
                continue
            chapters += 1
            chapter_groups = chapter.get("groups") or []
            groups += len(chapter_groups)
            blocks += sum(len(group) for group in chapter_groups)
            labels.update(chapter.get("jobs") or [])
    return {
        "papers": len(papers),
        "chapter_records": chapters,
        "coded_groups": groups,
        "blocks_in_groups": blocks,
        "labels": labels,
    }


def emitted(lane: str) -> tuple[dict, list[dict]]:
    path = os.path.join(OUT_DIR, f"quotes-{lane.lower()}.jsonl")
    rows: list[dict] = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    # F repeats a chapter label inside one paper, so the chapter label alone is not a key.
    keys = collections.Counter(
        (row["paper"], row.get("chapter_index"), row["chapter"], row["block_index"]) for row in rows
    )
    return {
        "rows": len(rows),
        "papers": len({row["paper"] for row in rows}),
        "empty_quotes": sum(1 for row in rows if not (row.get("quote") or "").strip()),
        "missing_page": sum(1 for row in rows if row.get("page") is None),
        "short_quotes": sum(1 for row in rows if len(row.get("quote") or "") < 20),
        "duplicate_keys": sum(1 for count in keys.values() if count > 1),
        "labels": collections.Counter(row["job"] for row in rows),
    }, rows


def levels(lane: str) -> dict:
    path = os.path.join(REPORTS, f"levels-{lane.lower()}.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def lane_report(lane: str) -> dict:
    expected = denominator(lane)
    actual, _ = emitted(lane)
    run = levels(lane)
    outside = sorted(set(actual["labels"]) - JOBS)
    base = collections.Counter()
    for label, count in actual["labels"].items():
        base[base_label(label)] += count
    snapshot_groups = run.get("coded_groups")
    # The owning lane keeps coding while the quote files stand, so the shortfall that matters
    # is measured against the denominator the generator actually saw. Drift since then is
    # reported separately instead of being billed to the quote layer.
    basis = snapshot_groups if snapshot_groups is not None else expected["coded_groups"]
    return {
        "lane": lane,
        "records_dir": LANE_DIRS[lane],
        "papers": expected["papers"],
        "chapter_records": expected["chapter_records"],
        "coded_groups": basis,
        "coded_groups_live": expected["coded_groups"],
        "groups_added_since_emit": expected["coded_groups"] - basis,
        "blocks_in_groups": expected["blocks_in_groups"],
        "rows": actual["rows"],
        "row_shortfall": basis - actual["rows"],
        "papers_with_rows": actual["papers"],
        "empty_quotes": actual["empty_quotes"],
        "missing_page": actual["missing_page"],
        "short_quotes": actual["short_quotes"],
        "duplicate_keys": actual["duplicate_keys"],
        "labels_outside_vocabulary": {label: actual["labels"][label] for label in outside},
        "label_base_census": dict(sorted(base.items())),
        "match_levels": run.get("match_levels", {}),
        "verification_source": run.get("provenance", {}),
        "heading_or_display_rows": run.get("heading_rows"),
    }


def markdown(reports: list[dict]) -> str:
    lines = [
        "# L7 quote backfill coverage",
        "",
        "Recounted from the lane records and the emitted quote files by "
        "`tools/coverage.py`. No count on this page is typed by hand.",
        "",
        "| lane | papers | chapter records | coded groups at emit | rows | shortfall | added since emit | empty | dup keys | short quotes |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for report in reports:
        lines.append(
            f"| {report['lane']} | {report['papers']} | {report['chapter_records']} | "
            f"{report['coded_groups']} | {report['rows']} | {report['row_shortfall']} | "
            f"{report['groups_added_since_emit']} | "
            f"{report['empty_quotes']} | {report['duplicate_keys']} | {report['short_quotes']} |"
        )
    totals = {
        key: sum(report[key] for report in reports)
        for key in ("papers", "chapter_records", "coded_groups", "rows", "row_shortfall", "groups_added_since_emit")
    }
    lines.append(
        f"| total | {totals['papers']} | {totals['chapter_records']} | {totals['coded_groups']} | "
        f"{totals['rows']} | {totals['row_shortfall']} | {totals['groups_added_since_emit']} | "
        f"{sum(report['empty_quotes'] for report in reports)} | "
        f"{sum(report['duplicate_keys'] for report in reports)} | "
        f"{sum(report['short_quotes'] for report in reports)} |"
    )
    lines += ["", "## How each quote verifies", ""]
    levels_all: collections.Counter[str] = collections.Counter()
    for report in reports:
        levels_all.update(report["match_levels"])
    lines.append("| level | rows | meaning |")
    lines.append("|---|---|---|")
    meaning = {
        "exact": "opening sentence found verbatim after whitespace folding",
        "nfkc": "found after NFKC, which collapses fi/fl ligatures",
        "squeezed": "found after removing all whitespace, so line and column breaks vanish",
        "span": "longest contiguous run of at least 8 block words that verifies",
        "gapped": "in-order run of at least 8 block words, gaps of at most 8 foreign words",
        "unverified": "formula or table block with no prose sentence; first words quoted as-is",
        "layout-only": "paper lost its extracted text; quote copied from the layout unverified",
        "ocr-only": "layout read from page images; the extracted text never covered this block",
        "text-gap": "paper's text layer drops whole paragraphs; this block quoted from the layout",
    }
    for level, count in sorted(levels_all.items(), key=lambda item: -item[1]):
        lines.append(f"| {level} | {count} | {meaning.get(level, '')} |")
    lines += ["", "## Verification text per lane", ""]
    sources: collections.Counter[str] = collections.Counter()
    for report in reports:
        for name, count in report["verification_source"].items():
            sources[name.split(":", 1)[0]] += count
    lines.append("| source | rows |")
    lines.append("|---|---|")
    for name, count in sorted(sources.items(), key=lambda item: -item[1]):
        lines.append(f"| {name} | {count} |")
    lines += ["", "## Labels outside the 13-job vocabulary", ""]
    for report in reports:
        outside = report["labels_outside_vocabulary"]
        text = ", ".join(f"`{label}` {count}" for label, count in sorted(outside.items())) or "none"
        lines.append(f"- **{report['lane']}**: {text}")
    return "\n".join(lines) + "\n"


def main() -> int:
    reports = [lane_report(lane) for lane in sorted(LANE_DIRS)]
    os.makedirs(REPORTS, exist_ok=True)
    with open(os.path.join(REPORTS, "coverage.json"), "w", encoding="utf-8", newline="\n") as handle:
        json.dump(reports, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
    with open(os.path.join(REPORTS, "coverage.md"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(markdown(reports))

    for report in reports:
        drift = report["groups_added_since_emit"]
        print(
            f"{report['lane']}: {report['rows']} rows / {report['coded_groups']} groups at emit "
            f"({report['row_shortfall']} short), empty {report['empty_quotes']}, "
            f"dup {report['duplicate_keys']}, papers {report['papers_with_rows']}"
            + (f", lane added {drift} groups since (live {report['coded_groups_live']})" if drift else "")
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
