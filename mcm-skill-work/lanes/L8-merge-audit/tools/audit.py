#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Recount the six coding lanes and write reports/recount.json.

Read-only against every lane. Writes only reports/recount.json inside this lane.

Run:  python -I -X utf8 tools/audit.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L8-merge-audit"
REPORTS = LANE / "reports"

JOBS = [
    "route", "define", "source", "select", "derive", "compute", "read-figure",
    "compare", "check", "limit", "mechanism", "interpret", "handoff",
]
EXT = ["context", "claim"]

CHAPTERS_14 = [
    "abstract", "introduction", "assumptions", "notation", "data-preprocessing",
    "model-establishment", "model-improvement", "algorithm", "results",
    "sensitivity-analysis", "robustness-verification", "strengths-limitations",
    "memo", "conclusion",
]

LANES = {
    "A": {
        "dir": "lanes/L6-a-evidence",
        "records": "records-a",
        "jobs": None,
        "quotes": ["lanes/L6-a-evidence/quotes-a.jsonl"],
        "layout": None,
        "shape": "block",
    },
    "B": {
        "dir": "lanes/L4-b-ledger",
        "records": "records",
        "jobs": "jobs-b.jsonl",
        "quotes": ["lanes/L7-quote-backfill/quotes-b.jsonl"],
        "layout": "layout",
        "shape": "chapter",
    },
    "C": {
        "dir": "lanes/L3-c-ledger",
        "records": "records",
        "jobs": "jobs-c.jsonl",
        "quotes": ["lanes/L7-quote-backfill/quotes-c.jsonl"],
        "layout": "layout",
        "shape": "chapter",
    },
    "D": {
        "dir": "lanes/L2-d-ledger",
        "records": "records",
        "jobs": "jobs-d.jsonl",
        "quotes": ["lanes/L7-quote-backfill/quotes-d.jsonl"],
        "layout": "layout",
        "shape": "chapter",
    },
    "E": {
        "dir": "lanes/L5-e-ledger",
        "records": "records",
        "jobs": "jobs-e.jsonl",
        "quotes": [],
        "layout": "layout",
        "shape": "chapter",
    },
    "F": {
        "dir": "lanes/L1-f-structure",
        "records": "records",
        "jobs": "jobs-f.jsonl",
        "quotes": [],
        "layout": "layout",
        "shape": "chapter",
    },
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path):
    rows = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def base_job(job: str) -> str:
    return job.split("+close:")[0].replace("ext:", "")


def load_records(lane: str, cfg: dict):
    """Return (records, skipped) where records maps pid -> chapter rows."""
    rdir = ROOT / cfg["dir"] / cfg["records"]
    records = {}
    skipped = []
    for path in sorted(rdir.glob("*.json")):
        if path.name.endswith(".skipped.json"):
            skipped.append(path.name)
            continue
        rows = read_json(path)
        if not isinstance(rows, list):
            raise SystemExit("%s: %s is not a list" % (lane, path))
        records[path.stem] = rows
    return records, skipped


def chapter_rows(lane: str, rows):
    """Normalise one paper's rows to [{chapter, groups, jobs, pages}]."""
    out = []
    if lane == "A":
        for row in rows:
            blocks = row.get("blocks", [])
            out.append(
                {
                    "chapter": row["chapter"],
                    "groups": [[b["block_index"]] for b in blocks],
                    "jobs": [b["job"] for b in blocks],
                    "pages": sorted(
                        {p for b in blocks for p in [b.get("page")] if isinstance(p, int)}
                    ),
                    "heading": None,
                }
            )
        return out
    for row in rows:
        groups = row.get("groups") or []
        pages = row.get("pages") or []
        out.append(
            {
                "chapter": row["chapter"],
                "groups": groups,
                "jobs": row.get("jobs") or [],
                "pages": pages,
                "heading": row.get("heading"),
            }
        )
    return out


def layout_index(cfg: dict):
    """pid -> {block n: page}, plus per-pid max page."""
    if not cfg["layout"]:
        return None
    ldir = ROOT / cfg["dir"] / cfg["layout"]
    idx = {}
    for path in sorted(ldir.glob("*.json")):
        doc = read_json(path)
        pages = {}
        max_page = 0
        for para in doc.get("paragraphs", []):
            pages[para["n"]] = para.get("pages") or []
            for p in para.get("pages") or []:
                if isinstance(p, int) and p > max_page:
                    max_page = p
        idx[path.stem] = {"pages": pages, "max_page": max_page}
    return idx


def audit_lane(lane: str, cfg: dict, manifest: dict, pdf_pages: dict):
    records, skipped = load_records(lane, cfg)
    layout = layout_index(cfg)

    papers = sorted(records)
    chapters = 0
    groups = 0
    blocks = 0
    pages_seen = []
    job_census = Counter()
    job_bad = Counter()
    chapter_census = Counter()
    chapter_off = Counter()
    per_chapter_groups = {}  # (pid, chapter) -> group count
    per_chapter_jobs = {}  # (pid, chapter) -> job per group, in group order
    empty_chapters = []
    dup_block_refs = []
    missing_layout_blocks = []
    page_out_of_range = []
    block_page_out_of_chapter = []
    dup_chapter_labels = []

    for pid in papers:
        rows = chapter_rows(lane, records[pid])
        seen_labels = Counter(r["chapter"] for r in rows)
        if len(seen_labels) != len(rows):
            dup_chapter_labels.append(
                {
                    "paper": pid,
                    "labels": [
                        {"label": k, "rows": v}
                        for k, v in sorted(seen_labels.items())
                        if v > 1
                    ],
                    "extra_rows": len(rows) - len(seen_labels),
                }
            )
        block_seen = Counter()
        chapter_block_seen = defaultdict(Counter)
        for row in rows:
            chapters += 1
            groups += len(row["groups"])
            for g in row["groups"]:
                blocks += len(g)
                for n in g:
                    block_seen[n] += 1
                    chapter_block_seen[row["chapter"]][n] += 1
            per_chapter_groups[(pid, row["chapter"])] = (
                per_chapter_groups.get((pid, row["chapter"]), 0) + len(row["groups"])
            )
            per_chapter_jobs.setdefault((pid, row["chapter"]), []).extend(row["jobs"])
            for job in row["jobs"]:
                job_census[job] += 1
                b = base_job(job)
                if b not in JOBS and b not in EXT:
                    job_bad[job] += 1
            chapter_census[row["chapter"]] += 1
            if not row["groups"]:
                empty_chapters.append({"paper": pid, "chapter": row["chapter"]})
            if row["chapter"] not in CHAPTERS_14:
                chapter_off[row["chapter"]] += 1
            pages = row["pages"]
            if pages:
                pages_seen.extend(p for p in pages if isinstance(p, int))
                if isinstance(pages, list) and len(pages) == 2 and pages[0] > pages[1]:
                    page_out_of_range.append(
                        {"paper": pid, "chapter": row["chapter"], "pages": pages}
                    )
        scope = chapter_block_seen if lane == "A" else {None: block_seen}
        for chapter, counts in scope.items():
            for n, c in counts.items():
                if c > 1:
                    item = {"paper": pid, "block": n, "uses": c}
                    if chapter is not None:
                        item["chapter"] = chapter
                    dup_block_refs.append(item)
        if layout is not None:
            lay = layout.get(pid)
            if lay is None:
                missing_layout_blocks.append({"paper": pid, "reason": "no layout file"})
                continue
            for row in rows:
                for g in row["groups"]:
                    for n in g:
                        if n not in lay["pages"]:
                            missing_layout_blocks.append(
                                {"paper": pid, "chapter": row["chapter"], "block": n}
                            )
                        elif row["pages"] and len(row["pages"]) == 2:
                            lo, hi = row["pages"]
                            block_pages = [
                                p for p in lay["pages"][n] if isinstance(p, int)
                            ]
                            if block_pages and not any(lo <= p <= hi for p in block_pages):
                                block_page_out_of_chapter.append(
                                    {
                                        "paper": pid,
                                        "chapter": row["chapter"],
                                        "block": n,
                                        "block_pages": block_pages,
                                        "chapter_pages": row["pages"],
                                    }
                                )
            for row in rows:
                pdf_page_count = pdf_pages.get(pid) or lay["max_page"]
                for p in row["pages"] or []:
                    if isinstance(p, int) and p > pdf_page_count:
                        page_out_of_range.append(
                            {
                                "paper": pid,
                                "chapter": row["chapter"],
                                "page": p,
                                "pdf_pages": pdf_page_count,
                            }
                        )

    # jobs file
    jobs_info = None
    if cfg["jobs"]:
        jpath = ROOT / cfg["dir"] / cfg["jobs"]
        rows = read_jsonl(jpath)
        jobs_info = {
            "file": cfg["jobs"],
            "rows": len(rows),
            "papers": len({r["paper"] for r in rows}),
            "group_count_sum": sum(int(r.get("group_count", 0)) for r in rows),
            "literal_blocks_sum": sum(int(r.get("literal_blocks", 0)) for r in rows),
            "papers_not_in_records": sorted(
                {r["paper"] for r in rows} - set(papers)
            ),
            "papers_not_in_jobs": sorted(
                set(papers) - {r["paper"] for r in rows}
            ),
        }

    # quotes
    quote_info = None
    quote_chapter_mismatch = []
    dup_quote_keys = []
    quote_unknown_chapter = []
    quote_index_out_of_range = []
    quote_job_mismatch = []
    quote_rows_without_page = 0
    missing_quotes = []
    if cfg["quotes"]:
        qrows = []
        files = []
        for rel in cfg["quotes"]:
            qpath = ROOT / rel
            files.append(rel)
            qrows.extend(read_jsonl(qpath))
        keys = Counter()
        per_chapter = Counter()
        for r in qrows:
            keys[(r["paper"], r["chapter"], r["block_index"])] += 1
            per_chapter[(r["paper"], r["chapter"])] += 1
            if r.get("page") is None:
                quote_rows_without_page += 1
            jobs = per_chapter_jobs.get((r["paper"], r["chapter"]))
            if jobs is not None:
                idx = r["block_index"]
                if not isinstance(idx, int) or idx < 0 or idx >= len(jobs):
                    quote_index_out_of_range.append(
                        {
                            "paper": r["paper"],
                            "chapter": r["chapter"],
                            "block_index": idx,
                            "groups": len(jobs),
                        }
                    )
                elif jobs[idx] != r.get("job"):
                    quote_job_mismatch.append(
                        {
                            "paper": r["paper"],
                            "chapter": r["chapter"],
                            "block_index": idx,
                            "quote_job": r.get("job"),
                            "record_job": jobs[idx],
                        }
                    )
        dup_quote_keys = [
            {"paper": k[0], "chapter": k[1], "block_index": k[2], "count": v}
            for k, v in sorted(keys.items())
            if v > 1
        ]
        for key, count in sorted(per_chapter.items()):
            rec = per_chapter_groups.get(key)
            if rec is None:
                quote_unknown_chapter.append(
                    {"paper": key[0], "chapter": key[1], "rows": count}
                )
            elif rec != count:
                quote_chapter_mismatch.append(
                    {"paper": key[0], "chapter": key[1], "quote_rows": count, "groups": rec}
                )
        for key, rec in sorted(per_chapter_groups.items()):
            if rec and key not in per_chapter:
                missing_quotes.append(
                    {"paper": key[0], "chapter": key[1], "groups": rec, "quote_rows": 0}
                )
        quote_info = {
            "files": files,
            "rows": len(qrows),
            "papers": len({r["paper"] for r in qrows}),
            "duplicate_keys": dup_quote_keys,
            "chapter_mismatch": quote_chapter_mismatch,
            "chapters_without_quotes": missing_quotes,
            "chapters_not_in_records": quote_unknown_chapter,
            "index_out_of_range": quote_index_out_of_range,
            "job_mismatch": quote_job_mismatch,
            "rows_without_page": quote_rows_without_page,
        }

    eligible = sorted(manifest.get(lane, []))
    queue = None
    qpath = ROOT / cfg["dir"] / "queue.txt"
    if qpath.exists():
        queue = [
            line.strip()
            for line in qpath.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    return {
        "lane": lane,
        "record_shape": cfg["shape"],
        "records_dir": "%s/%s" % (cfg["dir"], cfg["records"]),
        "record_files": len(papers),
        "skipped_files": skipped,
        "papers": len(papers),
        "chapters": chapters,
        "groups": groups,
        "blocks": blocks,
        "pages_min": min(pages_seen) if pages_seen else None,
        "pages_max": max(pages_seen) if pages_seen else None,
        "job_census": dict(sorted(job_census.items())),
        "jobs_outside_vocabulary": dict(sorted(job_bad.items())),
        "chapter_census": dict(sorted(chapter_census.items())),
        "chapters_outside_fourteen": dict(sorted(chapter_off.items())),
        "duplicate_chapter_labels": dup_chapter_labels,
        "empty_chapters": empty_chapters,
        "duplicate_block_refs": dup_block_refs,
        "blocks_missing_in_layout": missing_layout_blocks,
        "pages_out_of_range": page_out_of_range,
        "block_pages_outside_chapter": block_page_out_of_chapter,
        "jobs_file": jobs_info,
        "quotes": quote_info,
        "first_paper_pdf_pages": pdf_pages.get(papers[0]) if papers else None,
        "manifest_eligible": len(eligible),
        "papers_missing_vs_manifest": sorted(set(eligible) - set(papers)),
        "papers_not_in_manifest": sorted(set(papers) - set(eligible)),
        "queue_rows": len(queue) if queue is not None else None,
        "queue_minus_records": (
            sorted(set(queue) - set(papers)) if queue is not None else None
        ),
        "_records": records,
        "_per_chapter_groups": per_chapter_groups,
    }


def merge_rows(info: dict):
    if info["quotes"] is not None:
        return info["quotes"]["rows"]
    return info["groups"]


def gap_by_paper(info: dict):
    per = defaultdict(int)
    for (pid, _chapter), count in info["_per_chapter_groups"].items():
        per[pid] += count
    return dict(sorted(per.items()))


def audit_ledger(merge_totals, merge_chapter_keys):
    path = ROOT / "artifacts" / "paragraph-ledger.jsonl"
    rows = read_jsonl(path)
    by_type = Counter(r.get("type") for r in rows)
    keys = Counter((r.get("paper"), r.get("chapter")) for r in rows)
    dup = [
        {"paper": k[0], "chapter": k[1], "count": v}
        for k, v in sorted(keys.items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1])))
        if v > 1
    ]
    off = Counter(r.get("chapter") for r in rows if r.get("chapter") not in CHAPTERS_14)
    ledger_keys = set(keys)
    missing = sorted(ledger_keys - merge_chapter_keys)
    absent = sorted(merge_chapter_keys - ledger_keys)
    return {
        "file": "artifacts/paragraph-ledger.jsonl",
        "rows": len(rows),
        "by_type": dict(sorted(by_type.items(), key=lambda kv: str(kv[0]))),
        "distinct_papers": len({r.get("paper") for r in rows}),
        "chapters": len(ledger_keys),
        "chapters_outside_fourteen": dict(sorted(off.items())),
        "duplicate_keys": dup,
        "keys_not_in_lane_records": missing[:20],
        "keys_not_in_lane_records_count": len(missing),
        "lane_chapters_absent_from_ledger_count": len(absent),
        "merge_group_rows": merge_totals["total"],
        "merge_chapter_rows": merge_totals["chapters"],
        "merge_chapter_keys": len(merge_chapter_keys),
    }


def l7_coverage():
    path = ROOT / "lanes" / "L7-quote-backfill" / "reports" / "coverage.json"
    if not path.exists():
        return None
    out = {}
    for lane in read_json(path):
        out[lane["lane"]] = {
            "rows": lane.get("rows"),
            "papers": lane.get("papers"),
            "chapter_records": lane.get("chapter_records"),
            "coded_groups": lane.get("coded_groups"),
            "blocks_in_groups": lane.get("blocks_in_groups"),
            "row_shortfall": lane.get("row_shortfall"),
            "empty_quotes": lane.get("empty_quotes"),
            "duplicate_keys": lane.get("duplicate_keys"),
            "match_levels": lane.get("match_levels"),
            "labels_outside_vocabulary": lane.get("labels_outside_vocabulary"),
        }
    return out


def build():
    manifest_rows = read_jsonl(ROOT / "artifacts" / "corpus" / "manifest.jsonl")
    manifest = defaultdict(list)
    pdf_pages = {}
    for row in manifest_rows:
        if row.get("eligible_paper"):
            manifest[row["problem_type"]].append(row["paper_id"])
            pdf_pages[row["paper_id"]] = row.get("page_count")

    lanes = {}
    for lane, cfg in LANES.items():
        lanes[lane] = audit_lane(lane, cfg, manifest, pdf_pages)

    rows = {lane: merge_rows(info) for lane, info in lanes.items()}
    total = sum(rows.values())
    merge_chapter_keys = set()
    for info in lanes.values():
        merge_chapter_keys.update(
            (pid, chapter) for (pid, chapter) in info["_per_chapter_groups"]
        )
    gaps = {}
    for lane in ("E", "F"):
        gaps[lane] = gap_by_paper(lanes[lane])

    merge = {
        "chapters": sum(info["chapters"] for info in lanes.values()),
        "rows_by_lane": dict(sorted(rows.items())),
        "total": total,
        "rows_from_quote_layer": dict(
            sorted((k, v) for k, v in rows.items() if lanes[k]["quotes"] is not None)
        ),
        "rows_without_quote_layer": dict(
            sorted((k, v) for k, v in rows.items() if lanes[k]["quotes"] is None)
        ),
        "gap_by_paper": gaps,
    }

    checks = []

    def check(cid, lane, status, detail):
        checks.append({"id": cid, "lane": lane, "status": status, "detail": detail})

    for lane, info in lanes.items():
        check(
            "records_vs_jobs.groups",
            lane,
            "n/a" if info["jobs_file"] is None else
            ("pass" if info["jobs_file"]["group_count_sum"] == info["groups"] else "delta"),
            "records %d groups, jobs %s"
            % (info["groups"], None if info["jobs_file"] is None else info["jobs_file"]["group_count_sum"]),
        )
        check(
            "records_vs_jobs.blocks",
            lane,
            "n/a" if info["jobs_file"] is None else
            ("pass" if info["jobs_file"]["literal_blocks_sum"] == info["blocks"] else "delta"),
            "records %d blocks, jobs %s"
            % (info["blocks"], None if info["jobs_file"] is None else info["jobs_file"]["literal_blocks_sum"]),
        )
        check(
            "groups_vs_quotes.rows",
            lane,
            "n/a" if info["quotes"] is None else
            ("pass" if info["quotes"]["rows"] == info["groups"] else "delta"),
            "records %d groups, quotes %s"
            % (info["groups"], None if info["quotes"] is None else info["quotes"]["rows"]),
        )
        check(
            "quotes.duplicate_keys",
            lane,
            "n/a" if info["quotes"] is None else
            ("pass" if not info["quotes"]["duplicate_keys"] else "delta"),
            None if info["quotes"] is None else len(info["quotes"]["duplicate_keys"]),
        )
        check(
            "quotes.chapter_mismatch",
            lane,
            "n/a" if info["quotes"] is None else
            ("pass" if not info["quotes"]["chapter_mismatch"] else "delta"),
            None if info["quotes"] is None else len(info["quotes"]["chapter_mismatch"]),
        )
        check(
            "quotes.chapters_without_quotes",
            lane,
            "n/a" if info["quotes"] is None else
            ("pass" if not info["quotes"]["chapters_without_quotes"] else "delta"),
            None if info["quotes"] is None else len(info["quotes"]["chapters_without_quotes"]),
        )
        check(
            "records.jobs_outside_vocabulary",
            lane,
            "pass" if not info["jobs_outside_vocabulary"] else "delta",
            info["jobs_outside_vocabulary"],
        )
        check(
            "records.chapters_outside_fourteen",
            lane,
            "pass" if not info["chapters_outside_fourteen"] else "delta",
            info["chapters_outside_fourteen"],
        )
        check(
            "quotes.index_out_of_range",
            lane,
            "n/a" if info["quotes"] is None else
            ("pass" if not info["quotes"]["index_out_of_range"] else "delta"),
            None if info["quotes"] is None else len(info["quotes"]["index_out_of_range"]),
        )
        check(
            "quotes.job_mismatch",
            lane,
            "n/a" if info["quotes"] is None else
            ("pass" if not info["quotes"]["job_mismatch"] else "delta"),
            None if info["quotes"] is None else len(info["quotes"]["job_mismatch"]),
        )
        check(
            "quotes.rows_without_page",
            lane,
            "n/a" if info["quotes"] is None else
            ("pass" if not info["quotes"]["rows_without_page"] else "delta"),
            None if info["quotes"] is None else info["quotes"]["rows_without_page"],
        )
        check(
            "records.empty_chapters",
            lane,
            "pass" if not info["empty_chapters"] else "delta",
            len(info["empty_chapters"]),
        )
        check(
            "records.duplicate_block_refs",
            lane,
            "pass" if not info["duplicate_block_refs"] else "delta",
            len(info["duplicate_block_refs"]),
        )
        check(
            "records.duplicate_chapter_labels",
            lane,
            "pass" if not info["duplicate_chapter_labels"] else "delta",
            info["duplicate_chapter_labels"],
        )
        check(
            "records.blocks_missing_in_layout",
            lane,
            "n/a" if info["jobs_file"] is None and info["lane"] == "A" else
            ("pass" if not info["blocks_missing_in_layout"] else "delta"),
            len(info["blocks_missing_in_layout"]),
        )
        check(
            "records.pages_out_of_range",
            lane,
            "pass" if not info["pages_out_of_range"] else "delta",
            len(info["pages_out_of_range"]),
        )
        check(
            "records.block_pages_outside_chapter",
            lane,
            "pass" if not info["block_pages_outside_chapter"] else "delta",
            len(info["block_pages_outside_chapter"]),
        )
        check(
            "manifest.papers_missing",
            lane,
            "pass" if not info["papers_missing_vs_manifest"] else "delta",
            len(info["papers_missing_vs_manifest"]),
        )

    ledger = audit_ledger(merge, merge_chapter_keys)

    for info in lanes.values():
        info.pop("_records", None)
        info.pop("_per_chapter_groups", None)

    return {
        "lane": "L8-merge-audit",
        "tool": "tools/audit.py",
        "vocabularies": {
            "jobs": JOBS,
            "ext": EXT,
            "chapters_canonical_fourteen": CHAPTERS_14,
        },
        "manifest_eligible": {
            k: len(v) for k, v in sorted(manifest.items())
        },
        "lanes": lanes,
        "checks": sorted(checks, key=lambda c: (c["lane"], c["id"])),
        "l7_coverage_snapshot": l7_coverage(),
        "merge": merge,
        "ledger": ledger,
    }


def main():
    result = build()
    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / "recount.json"
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    out.write_text(text, encoding="utf-8")

    for lane, info in sorted(result["lanes"].items()):
        jf = info["jobs_file"]
        q = info["quotes"]
        print(
            "%s papers=%d chapters=%d groups=%d blocks=%d jobs=%s quotes=%s"
            % (
                lane,
                info["papers"],
                info["chapters"],
                info["groups"],
                info["blocks"],
                "n/a" if jf is None else jf["rows"],
                "n/a" if q is None else q["rows"],
            )
        )
    print("merge total rows:", result["merge"]["total"])
    print("ledger rows:", result["ledger"]["rows"])
    bad = [c for c in result["checks"] if c["status"] == "delta"]
    print("delta checks:", len(bad))
    for c in bad:
        print("  %s %s -> %s" % (c["lane"], c["id"], c["detail"]))


if __name__ == "__main__":
    sys.exit(main())
