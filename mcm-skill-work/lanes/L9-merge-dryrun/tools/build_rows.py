"""Build the merge staging rows for the six coding lanes.

Two modes. `snapshot` freezes a projection of every input into `inputs/`;
`build` reads only that projection, so the row file is reproducible after the
live lanes move on.

  python -I -X utf8 lanes/L9-merge-dryrun/tools/build_rows.py snapshot
  python -I -X utf8 lanes/L9-merge-dryrun/tools/build_rows.py build

`snapshot` writes:
  inputs/records.jsonl   one line per chapter row, fields the merge needs
  inputs/quotes.jsonl    one line per quote row: hash and length, not the text
  inputs/pages.json      paper -> {layout block n: pages}, for pages_coded
  inputs/levels.json     per-lane match-level census (L7 emits it per lane only)
  reports/snapshot.json  sha256 of every original input and of the projections

`build` writes one row per coded group: reports/rows.jsonl and
reports/stats.json. A group is the merge unit: one printed unit, one job, one
quote slot. Quote text is not copied; the row carries quote_sha256, quote_len,
page and source_quote_row, so a merge session reads the source file back.

Writes only lanes/L9-merge-dryrun/**.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L9-merge-dryrun"
INPUTS = LANE / "inputs"
REPORTS = LANE / "reports"
SNAPSHOT = REPORTS / "snapshot.json"

RECORDS = INPUTS / "records.jsonl"
QUOTES = INPUTS / "quotes.jsonl"
PAGES = INPUTS / "pages.json"
LEVELS = INPUTS / "levels.json"

CHAPTERS_14 = (
    "abstract",
    "introduction",
    "assumptions",
    "notation",
    "data-preprocessing",
    "model-establishment",
    "model-improvement",
    "algorithm",
    "results",
    "sensitivity-analysis",
    "robustness-verification",
    "strengths-limitations",
    "memo",
    "conclusion",
)

JOBS_13 = (
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
)

# Chapter labels outside the fourteen whose normalisation L8 already ruled on
# (reports/deltas.md section 3). Aliases only aggregate; `chapter` stays verbatim.
ALIASES = {
    "problem-analysis": "introduction",
    "problem-restatement": "introduction",
    "sensitivity-robustness": "sensitivity-analysis",
    "future-improvements": "strengths-limitations",
    "strengths": "strengths-limitations",
    "limitations": "strengths-limitations",
    "error-analysis": "results",
}

STRUCTURAL = {"references": "references", "appendix": "structural"}
FRONT_MATTER = {"title"}

# No ruling exists anywhere. chapter_normalized stays null and the row is
# blocked: the merge session decides, this lane does not.
UNRULED = {
    "cultural-analysis",
    "technology-impact",
    "illustration",
    "heavy-trucks",
    "our-work",
    "recommendations",
    "advice",
    "future-considerations",
    "gcn-evidence",
    "recommendation",
    "model-testing",
}

LANES = {
    "A": {
        "records": "lanes/L6-a-evidence/records-a",
        "quotes": "lanes/L6-a-evidence/quotes-a.jsonl",
        "layout": None,
        "shape": "block",
        "levels": None,
    },
    "B": {
        "records": "lanes/L4-b-ledger/records",
        "quotes": "lanes/L7-quote-backfill/quotes-b.jsonl",
        "layout": "lanes/L4-b-ledger/layout",
        "shape": "chapter",
        "levels": "lanes/L7-quote-backfill/reports/levels-b.json",
    },
    "C": {
        "records": "lanes/L3-c-ledger/records",
        "quotes": "lanes/L7-quote-backfill/quotes-c.jsonl",
        "layout": "lanes/L3-c-ledger/layout",
        "shape": "chapter",
        "levels": "lanes/L7-quote-backfill/reports/levels-c.json",
    },
    "D": {
        "records": "lanes/L2-d-ledger/records",
        "quotes": "lanes/L7-quote-backfill/quotes-d.jsonl",
        "layout": "lanes/L2-d-ledger/layout",
        "shape": "chapter",
        "levels": "lanes/L7-quote-backfill/reports/levels-d.json",
    },
    "E": {
        "records": "lanes/L5-e-ledger/records",
        "quotes": "lanes/L7-quote-backfill/quotes-e.jsonl",
        "layout": "lanes/L5-e-ledger/layout",
        "shape": "chapter",
        "levels": "lanes/L7-quote-backfill/reports/levels-e.json",
    },
    "F": {
        "records": "lanes/L1-f-structure/records",
        "quotes": "lanes/L7-quote-backfill/quotes-f.jsonl",
        "layout": "lanes/L1-f-structure/layout",
        "shape": "chapter",
        "levels": "lanes/L7-quote-backfill/reports/levels-f.json",
    },
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def dump_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8")


def record_files(dir_path: Path) -> list[Path]:
    return sorted(p for p in dir_path.glob("*.json") if not p.name.endswith(".skipped.json"))


# --------------------------------------------------------------------------- #
# snapshot
# --------------------------------------------------------------------------- #


def project_records() -> list[dict]:
    """One line per chapter row, reduced to what a merge row needs.

    A is flattened to one single-block group per block, so the build is uniform
    across the two record shapes. A's block ordinal is kept and marked as its
    own basis; B-F keep the layout paragraph numbers.
    """
    out: list[dict] = []
    for lane, cfg in LANES.items():
        rec_dir = ROOT / cfg["records"]
        for path in record_files(rec_dir):
            data = json.loads(path.read_text(encoding="utf-8"))
            source = rel(path)
            if cfg["shape"] == "block":
                for ch_pos, chapter_row in enumerate(data):
                    blocks = chapter_row["blocks"]
                    out.append(
                        {
                            "lane": lane,
                            "paper": chapter_row["paper"],
                            "chapter": chapter_row["chapter"],
                            "chapter_index": ch_pos + 1,
                            "heading": None,
                            "pages": None,
                            "groups": [[int(b["block_index"])] for b in blocks],
                            "jobs": [b["job"] for b in blocks],
                            "block_pages": [
                                [b["page"], b["page"]] if b.get("page") is not None else None
                                for b in blocks
                            ],
                            "source_record": source,
                        }
                    )
                continue
            for ch_pos, chapter_row in enumerate(data):
                out.append(
                    {
                        "lane": lane,
                        "paper": path.stem,
                        "chapter": chapter_row["chapter"],
                        "chapter_index": ch_pos + 1,
                        "heading": chapter_row.get("heading"),
                        "pages": chapter_row.get("pages"),
                        "groups": [[int(b) for b in group] for group in chapter_row.get("groups") or []],
                        "jobs": list(chapter_row.get("jobs") or []),
                        "block_pages": None,
                        "source_record": source,
                    }
                )
    return out


def project_quotes() -> list[dict]:
    out: list[dict] = []
    for lane, cfg in LANES.items():
        path = ROOT / cfg["quotes"]
        with path.open(encoding="utf-8") as fh:
            for line_no, line in enumerate(fh, start=1):
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                text = row.get("quote")
                out.append(
                    {
                        "lane": lane,
                        "paper": row["paper"],
                        "chapter": row["chapter"],
                        "chapter_index": row.get("chapter_index"),
                        "block_index": int(row["block_index"]),
                        "job": row["job"],
                        "page": row.get("page"),
                        "quote_sha256": sha256_text(text) if text is not None else None,
                        "quote_len": len(text) if text is not None else None,
                        "source_quote_row": line_no,
                    }
                )
    return out


def project_pages() -> dict[str, dict[str, list[int]]]:
    pages: dict[str, dict[str, list[int]]] = {}
    for lane, cfg in LANES.items():
        if not cfg["layout"]:
            continue
        for path in sorted((ROOT / cfg["layout"]).glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            pages[data["paper"]] = {
                str(int(par["n"])): list(par.get("pages") or []) for par in data["paragraphs"]
            }
    return pages


def project_levels() -> dict:
    out = {}
    for lane, cfg in LANES.items():
        path = cfg["levels"]
        if path and (ROOT / path).exists():
            data = json.loads((ROOT / path).read_text(encoding="utf-8"))
            out[lane] = {
                "rows": data.get("rows"),
                "match_levels": data.get("match_levels"),
                "heading_rows": data.get("heading_rows"),
                "papers": data.get("papers"),
            }
        else:
            out[lane] = None
    return out


def original_inventory() -> list[dict]:
    entries: list[dict] = []
    for lane, cfg in LANES.items():
        rec_dir = ROOT / cfg["records"]
        recs = record_files(rec_dir)
        entries.append(
            {
                "kind": "records-dir",
                "lane": lane,
                "path": rel(rec_dir),
                "files": len(recs),
                "sha256": sha256_text("".join(f"{p.name}:{sha256_file(p)}\n" for p in recs)),
            }
        )
        quotes = ROOT / cfg["quotes"]
        entries.append(
            {
                "kind": "quotes",
                "lane": lane,
                "path": rel(quotes),
                "rows": len(load_jsonl(quotes)),
                "sha256": sha256_file(quotes),
            }
        )
        if cfg["layout"]:
            lay = sorted((ROOT / cfg["layout"]).glob("*.json"))
            entries.append(
                {
                    "kind": "layout-dir",
                    "lane": lane,
                    "path": cfg["layout"],
                    "files": len(lay),
                    "sha256": sha256_text("".join(f"{p.name}:{sha256_file(p)}\n" for p in lay)),
                }
            )
        if cfg["levels"] and (ROOT / cfg["levels"]).exists():
            entries.append(
                {"kind": "levels", "lane": lane, "path": cfg["levels"], "sha256": sha256_file(ROOT / cfg["levels"])}
            )
    return entries


def cmd_snapshot() -> int:
    if INPUTS.exists():
        shutil.rmtree(INPUTS)
    records = project_records()
    quotes = project_quotes()
    pages = project_pages()
    levels = project_levels()

    dump_jsonl(RECORDS, records)
    dump_jsonl(QUOTES, quotes)
    write_json(PAGES, pages)
    write_json(LEVELS, levels)

    per_lane = {}
    for lane in "ABCDEF":
        recs = [r for r in records if r["lane"] == lane]
        qs = [q for q in quotes if q["lane"] == lane]
        per_lane[lane] = {
            "papers": len({r["paper"] for r in recs}),
            "chapters": len(recs),
            "groups": sum(len(r["groups"]) for r in recs),
            "quote_rows": len(qs),
        }

    payload = {
        "tool": "lanes/L9-merge-dryrun/tools/build_rows.py",
        "mode": "snapshot",
        "originals": original_inventory(),
        "projections": {
            "inputs/records.jsonl": {"lines": len(records), "sha256": sha256_file(RECORDS)},
            "inputs/quotes.jsonl": {"lines": len(quotes), "sha256": sha256_file(QUOTES)},
            "inputs/pages.json": {"papers": len(pages), "sha256": sha256_file(PAGES)},
            "inputs/levels.json": {"sha256": sha256_file(LEVELS)},
        },
        "state": per_lane,
    }
    write_json(SNAPSHOT, payload)

    print(f"snapshot -> {rel(SNAPSHOT)}  ({len(payload['originals'])} original inputs)")
    for lane in "ABCDEF":
        s = per_lane[lane]
        print(
            f"  {lane}: papers {s['papers']:>3}  chapters {s['chapters']:>5}  "
            f"groups {s['groups']:>6}  quote rows {s['quote_rows']:>6}"
        )
    return 0


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #


def split_job(job: str) -> tuple[str, str | None]:
    head, sep, close = job.partition("+close:")
    base = head[4:] if head.startswith("ext:") else head
    return base, (close if sep else None)


def is_job_ok(job: str) -> bool:
    base, close = split_job(job)
    if base not in JOBS_13 and base not in ("context", "claim"):
        return False
    if close is not None and close not in JOBS_13:
        return False
    return True


def classify_chapter(label: str) -> tuple[str | None, str, list[str]]:
    """(chapter_normalized, evidence_class, blocked_reasons)."""
    if label in CHAPTERS_14:
        return label, "prose", []
    if label in ALIASES:
        return ALIASES[label], "prose", []
    if label in STRUCTURAL:
        return None, STRUCTURAL[label], []
    if label in FRONT_MATTER:
        return None, "front-matter", []
    if label in UNRULED:
        return None, "prose", ["chapter-label-unruled"]
    return None, "prose", ["chapter-label-unknown"]


def count_by(rows: list[dict], field: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        key = row[field]
        out[key] = out.get(key, 0) + 1
    return dict(sorted(out.items()))


def count_reasons(rows: list[dict]) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        for reason in row["blocked"]:
            out[reason] = out.get(reason, 0) + 1
    return dict(sorted(out.items()))


def key_of(row: dict) -> tuple:
    return (row["type"], row["paper"], row["chapter_index"], row["group_index"])


def build_rows() -> tuple[list[dict], dict]:
    records = load_jsonl(RECORDS)
    quotes = load_jsonl(QUOTES)
    pages = json.loads(PAGES.read_text(encoding="utf-8"))
    levels = json.loads(LEVELS.read_text(encoding="utf-8"))

    manifest_pages = {}
    for row in load_jsonl(ROOT / "artifacts" / "corpus" / "manifest.jsonl"):
        manifest_pages[row["paper_id"]] = row.get("page_count")

    # Quote index. A-D quote rows key groups by (paper, chapter, 0-based group
    # ordinal); E/F add the 0-based chapter ordinal because their chapter labels
    # repeat inside a paper.
    qindex: dict[tuple, dict] = {}
    qdupes: list[dict] = []
    for q in quotes:
        if q["lane"] in ("E", "F"):
            key = (q["lane"], q["paper"], int(q["chapter_index"]), q["block_index"])
        else:
            key = (q["lane"], q["paper"], q["chapter"], q["block_index"])
        if key in qindex:
            qdupes.append({"key": list(key), "lines": [qindex[key]["source_quote_row"], q["source_quote_row"]]})
        else:
            qindex[key] = q

    # Duplicate block references: one layout block coded into two groups of one
    # paper. The paper is refused rather than double-counted.
    seen: dict[tuple, set[int]] = {}
    dup_blocks: dict[str, set[int]] = {}
    for rec in records:
        if rec["lane"] == "A":
            continue
        bucket = seen.setdefault((rec["lane"], rec["paper"]), set())
        for group in rec["groups"]:
            for block in group:
                if block in bucket:
                    dup_blocks.setdefault(f"{rec['lane']}-{rec['paper']}", set()).add(block)
                else:
                    bucket.add(block)

    rows: list[dict] = []
    for rec in records:
        lane = rec["lane"]
        norm, evclass, ch_blocked = classify_chapter(rec["chapter"])
        paper_pages = pages.get(rec["paper"], {})
        for i, group in enumerate(rec["groups"]):
            job = rec["jobs"][i] if i < len(rec["jobs"]) else ""
            if lane in ("E", "F"):
                key = (lane, rec["paper"], rec["chapter_index"] - 1, i)
            else:
                key = (lane, rec["paper"], rec["chapter"], i)
            quote = qindex.get(key)

            blocked = list(ch_blocked)
            if not is_job_ok(job):
                blocked.append("job-outside-vocabulary")
            if quote is None:
                blocked.append("no-quote")
            if f"{lane}-{rec['paper']}" in dup_blocks and any(
                b in dup_blocks[f"{lane}-{rec['paper']}"] for b in group
            ):
                blocked.append("duplicate-block-ref")

            if rec["block_pages"] is not None:
                span = rec["block_pages"][i]
                pages_coded = span
                missing = [b for b in group if span is None]
                basis = "record-ordinal-0"
            else:
                found = [p for b in group for p in paper_pages.get(str(b), [])]
                pages_coded = [min(found), max(found)] if found else None
                missing = [b for b in group if str(b) not in paper_pages] if paper_pages else []
                basis = "layout-paragraph-n"
            if missing:
                blocked.append("block-missing-in-layout")

            page = quote.get("page") if quote else None
            if (
                page is not None
                and manifest_pages.get(rec["paper"]) is not None
                and not (1 <= page <= manifest_pages[rec["paper"]])
            ):
                blocked.append("page-outside-pdf")

            base_job, close_job = split_job(job)
            rows.append(
                {
                    "paper": rec["paper"],
                    "type": lane,
                    "chapter": rec["chapter"],
                    "chapter_normalized": norm,
                    "chapter_index": rec["chapter_index"],
                    "group_index": i + 1,
                    "block_index": group[0] if group else 0,
                    "block_index_basis": basis,
                    "blocks": group,
                    "job": job,
                    "base_job": base_job,
                    "close_job": close_job,
                    "quote_sha256": quote["quote_sha256"] if quote else None,
                    "quote_len": quote["quote_len"] if quote else None,
                    "quote_level": "in-record" if lane == "A" else None,
                    "page": page,
                    "pages_declared": rec["pages"],
                    "pages_coded": pages_coded,
                    "heading": rec["heading"],
                    "evidence_class": evclass,
                    "status": None,
                    "blocked": blocked,
                    "source_record": rec["source_record"],
                    "source_quote_row": quote["source_quote_row"] if quote else None,
                    "source_quote_file": quotes_source_file(lane) if quote else None,
                }
            )

    for row in rows:
        if row["evidence_class"] == "front-matter":
            row["status"] = "excluded"
        elif row["blocked"]:
            row["status"] = "blocked"
        else:
            row["status"] = "merge"

    rows.sort(key=key_of)

    lanes_stats = {}
    for lane in "ABCDEF":
        lane_rows = [r for r in rows if r["type"] == lane]
        lane_recs = [r for r in records if r["lane"] == lane]
        lane_quotes = [q for q in quotes if q["lane"] == lane]
        joined = sum(1 for r in lane_rows if r["source_quote_row"] is not None)
        lanes_stats[lane] = {
            "papers": len({r["paper"] for r in lane_recs}),
            "chapters": len(lane_recs),
            "groups": len(lane_rows),
            "quote_rows": len(lane_quotes),
            "quote_joined": joined,
            "quote_shortfall": len(lane_rows) - joined,
            "quote_rows_unused": len(lane_quotes) - joined,
            "status": count_by(lane_rows, "status"),
            "blocked_reasons": count_reasons(lane_rows),
            "evidence_class": count_by(lane_rows, "evidence_class"),
            "chapter_normalized_null": sum(1 for r in lane_rows if r["chapter_normalized"] is None),
            "dup_block_papers": {
                pid.split("-", 1)[1]: sorted(v)
                for pid, v in sorted(dup_blocks.items())
                if pid.startswith(lane + "-")
            },
            "levels_aggregate": (levels.get(lane) or {}).get("match_levels"),
            "levels_rows": (levels.get(lane) or {}).get("rows"),
            "level_per_row_available": False,
        }

    keys = [key_of(r) for r in rows]
    stats = {
        "tool": "lanes/L9-merge-dryrun/tools/build_rows.py",
        "mode": "build",
        "snapshot_sha256": sha256_file(SNAPSHOT),
        "ordering": ["type", "paper", "chapter_index", "group_index"],
        "dedupe_key": ["paper", "chapter_index", "group_index"],
        "quote_duplicate_keys": qdupes,
        "lanes": lanes_stats,
        "totals": {
            "papers": sum(s["papers"] for s in lanes_stats.values()),
            "chapters": sum(s["chapters"] for s in lanes_stats.values()),
            "groups": len(rows),
            "quote_rows": sum(s["quote_rows"] for s in lanes_stats.values()),
            "quote_joined": sum(s["quote_joined"] for s in lanes_stats.values()),
            "quote_shortfall": sum(s["quote_shortfall"] for s in lanes_stats.values()),
            "status": count_by(rows, "status"),
            "blocked_reasons": count_reasons(rows),
            "evidence_class": count_by(rows, "evidence_class"),
            "dedupe_keys": len(set(keys)),
            "duplicate_keys": len(keys) - len(set(keys)),
        },
    }
    return rows, stats


def quotes_source_file(lane: str) -> str:
    return LANES[lane]["quotes"]


def cmd_build() -> int:
    if not SNAPSHOT.exists() or not INPUTS.exists():
        print("no snapshot: run `build_rows.py snapshot` first")
        return 2
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    for name, meta in snap["projections"].items():
        path = LANE / name
        if sha256_file(path) != meta["sha256"]:
            print(f"projection changed: {name} — re-run snapshot")
            return 2

    rows, stats = build_rows()
    REPORTS.mkdir(parents=True, exist_ok=True)
    dump_jsonl(REPORTS / "rows.jsonl", rows)
    stats["rows_sha256"] = sha256_file(REPORTS / "rows.jsonl")
    write_json(REPORTS / "stats.json", stats)

    for lane in "ABCDEF":
        s = stats["lanes"][lane]
        print(
            f"{lane}: groups {s['groups']:>6}  joined {s['quote_joined']:>6}  "
            f"short {s['quote_shortfall']:>4}  merge {s['status'].get('merge', 0):>6}  "
            f"blocked {s['status'].get('blocked', 0):>5}  excluded {s['status'].get('excluded', 0):>3}"
        )
    t = stats["totals"]
    print(
        f"TOTAL rows {t['groups']}  keys {t['dedupe_keys']}  dupes {t['duplicate_keys']}  "
        f"shortfall {t['quote_shortfall']}"
    )
    print(f"rows.jsonl sha256 {stats['rows_sha256']}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in ("snapshot", "build"):
        print(__doc__)
        return 64
    return cmd_snapshot() if argv[1] == "snapshot" else cmd_build()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
