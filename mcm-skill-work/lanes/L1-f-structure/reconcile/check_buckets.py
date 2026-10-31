"""Check the bucket reconciliation and the per-paper block coverage.

Inputs (read-only): lanes/L1-f-structure/jobs-f.jsonl, layout/<pid>.json,
reconcile/worklist.json, reconcile/bucket-decisions.jsonl,
artifacts/language-units/P-F-*.json.

For every stored F bucket that has no coded chapter under the normalised label
(the 26 rows of worklist.json) it recomputes:

  * how many measured blocks the bucket's page span holds,
  * which coded record covers each of them,
  * how many are left uncovered (0 is expected for every bucket),

and for every F paper it recomputes block coverage:

  * dup   - a block appearing in two coded groups,
  * miss  - a measured body/heading block inside the coded page range that no
            record holds, classified as reference / contents / front-matter /
            appendix / unexplained,
  * extra - a coded block number the layout does not contain.

The unexplained class must be empty; a bucket decision must name a class and a
piece of evidence. Exit code 1 if any of those fail.

Usage: python -I -X utf8 lanes/L1-f-structure/reconcile/check_buckets.py
"""
from __future__ import annotations

import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L1-f-structure"
RECON = LANE / "reconcile"

CLASSES = {"a": "covered by another chapter record",
           "b": "printed and uncoded (record added)",
           "c": "no such printed section / figure page / TOC"}

TOC = re.compile(r"(?:\.\s*){4,}|…{3,}")
REF_HEAD = re.compile(r"(References?|REFERENCES?|Bibliography|Work [Cc]ited)\b")
REF_ITEM = re.compile(r"\[[0-9]{1,3}\]|\bpp?\.\s*\d|\bdoi:|\bhttps?://|\b(?:19|20)\d\d\b\s*[,.]")
APPENDIX = re.compile(r"^\s*(Appendix|APPENDIX|Report on Use of AI|Use of AI)\b")
AI_LOG = re.compile(r"^\s*(Query\s*\d|Output\s*\d?)\s*:", re.I)
WM_ONLY = re.compile(r"^[\sm·.\-_|]*$")


def load_records() -> tuple[list[dict], dict[str, list[dict]]]:
    rows = [json.loads(line) for line in
            (LANE / "jobs-f.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    by_paper = collections.defaultdict(list)
    for row in rows:
        by_paper[row["paper"]].append(row)
    return rows, by_paper


def record_ids(by_paper: dict[str, list[dict]]) -> dict[tuple[str, int], str]:
    """paper + chapter-record index -> stable id 'paper#NN'."""
    ids = {}
    for paper, recs in by_paper.items():
        for i, rec in enumerate(recs, 1):
            ids[(paper, id(rec))] = "%s#%02d" % (paper, i)
    return ids


WM = ("微信公众号：数学模型", "微信号：MATHmodels", "关注数学模型",
      "MATHmodels", "获取更多资讯", "数学模型")


def clean(text: str) -> str:
    for w in WM:
        text = text.replace(w, " ")
    return re.sub(r"\s+", " ", text).strip()


def classify_miss(blocks: dict[int, dict], used: set[int], first_coded: int) -> dict[int, str]:
    """Assign one exclusion class to every uncoded block, stateful in print order.

    The classes are the lane's documented scope exclusions (README "Scope
    exclusions"): front matter (title sheet, contents, abstract), contents lines,
    references, an AI-use appendix, and watermark / running-head furniture. A
    reference or appendix run continues to the end of the paper once it starts,
    so a continuation line such as "Bank of England, Staff Working Paper No. 605."
    counts as part of the list it belongs to.
    """
    titles = collections.Counter(
        clean(p["text"]) for p in blocks.values() if clean(p["text"]))
    repeated = {t for t, c in titles.items() if c >= 3 and len(t.split()) <= 14}
    toc_blocks = {n for n, b in blocks.items() if TOC.search(b["text"])}
    toc_pages = collections.Counter(blocks[n]["pages"][0] for n in toc_blocks)
    contents_pages = {page for page, c in toc_pages.items() if c >= 2}

    def refish(n: int) -> bool:
        text = clean(blocks[n]["text"])
        return bool(REF_HEAD.search(text) or REF_ITEM.search(text))

    order = sorted(blocks)
    ref_start = None
    appendix_start = None
    for i, n in enumerate(order):
        if n < first_coded:
            continue
        if ref_start is None and refish(n):
            window = [m for m in order[i:i + 4] if m >= first_coded]
            if sum(1 for m in window if refish(m)) >= 2:
                ref_start = n
        if appendix_start is None:
            text = clean(blocks[n]["text"])
            if APPENDIX.match(text) or AI_LOG.match(text):
                appendix_start = n
    out = {}
    for n, block in blocks.items():
        if n in used:
            continue
        text = clean(block["text"])
        tokens = re.findall(r"[A-Za-z']+", text)
        m_share = sum(1 for t in tokens if t.lower() == "m") / max(1, len(tokens))
        if n < first_coded:
            out[n] = "front-matter"
        elif appendix_start is not None and n >= appendix_start:
            out[n] = "appendix"
        elif ref_start is not None and n >= ref_start:
            out[n] = "reference"
        elif TOC.search(block["text"]) or block["pages"][0] in contents_pages:
            out[n] = "contents"
        elif (not text or WM_ONLY.match(text) or text in repeated
              or (len(tokens) >= 20 and m_share >= 0.8)):
            out[n] = "banner"
        else:
            out[n] = "unexplained"
    return out


def paper_coverage(paper: str, recs: list[dict], layout: dict) -> dict:
    blocks = {p["n"]: p for p in layout["paragraphs"]}
    used = collections.Counter()
    for rec in recs:
        for group in rec["blocks"]:
            for n in group:
                used[n] += 1
    dup = sorted(n for n, c in used.items() if c > 1)
    extra = sorted(n for n in used if n not in blocks)
    first_page = min(r["pages"][0] for r in recs)
    last_page = max(r["pages"][1] for r in recs)
    first_coded = min(used) if used else 0
    classes = classify_miss(blocks, set(used), first_coded)
    miss = []
    for n in sorted(classes):
        block = blocks[n]
        if not (first_page <= block["pages"][0] <= last_page):
            continue
        if block["kind"] not in ("body", "heading", "display"):
            continue
        miss.append({"block": n, "pages": block["pages"], "kind": block["kind"],
                     "class": classes[n],
                     "text": re.sub(r"\s+", " ", block["text"])[:90]})
    counts = collections.Counter(m["class"] for m in miss)
    return {"paper": paper, "records": len(recs), "blocks_coded": sum(used.values()),
            "distinct_blocks": len(used), "dup": dup, "extra": extra,
            "miss_by_class": dict(counts), "miss": miss,
            "units": sum(len(r["units"]) for r in recs),
            "groups": sum(r["group_count"] for r in recs)}


def main() -> None:
    rows, by_paper = load_records()
    ids = record_ids(by_paper)
    worklist = json.loads((RECON / "worklist.json").read_text(encoding="utf-8"))
    decisions = {}
    path = RECON / "bucket-decisions.jsonl"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                d = json.loads(line)
                decisions[(d["paper"], d["stored_label"], d["stored_pages"][0], d["stored_pages"][1])] = d

    failures = []
    bucket_rows = []
    for item in worklist:
        paper, label, p0, p1 = item["paper"], item["label"], item["p0"], item["p1"]
        layout = json.loads((LANE / "layout" / (paper + ".json")).read_text(encoding="utf-8"))
        pages = {p["n"]: p["pages"] for p in layout["paragraphs"]}
        span = [p for p in layout["paragraphs"] if not (p["pages"][1] < p0 or p["pages"][0] > p1)]
        covering = collections.defaultdict(list)
        for rec in by_paper.get(paper, []):
            for group in rec["blocks"]:
                if any(n in pages and not (pages[n][1] < p0 or pages[n][0] > p1) for n in group):
                    covering[ids[(paper, id(rec))]].append(group)
        uncovered = [p["n"] for p in span
                     if not any(p["n"] in g for rec in by_paper[paper] for g in rec["blocks"])]
        d = decisions.get((paper, label, p0, p1))
        bucket_rows.append({
            "paper": paper, "stored_label": label, "stored_pages": [p0, p1],
            "blocks_in_span": len(span), "covered": len(span) - len(uncovered),
            "uncovered": uncovered, "record_ids": sorted(covering),
            "class": d["class"] if d else None,
        })
        if d is None:
            failures.append("no decision for %s %s pp.%d-%d" % (paper, label, p0, p1))
            continue
        if d["class"] not in CLASSES:
            failures.append("%s %s: class %r" % (paper, label, d["class"]))
        if d["class"] == "a" and sorted(d.get("record_ids", [])) != sorted(covering):
            failures.append("%s %s: decision record_ids %s != computed %s"
                            % (paper, label, d.get("record_ids"), sorted(covering)))
        if uncovered:
            failures.append("%s %s: %d uncovered blocks %s" % (paper, label, len(uncovered), uncovered))
        if d["class"] == "c" and not d.get("render"):
            failures.append("%s %s: class c without a render page evidence" % (paper, label))

    # per-paper coverage, every F paper
    cov_rows = []
    for paper in sorted(by_paper):
        layout = json.loads((LANE / "layout" / (paper + ".json")).read_text(encoding="utf-8"))
        cov = paper_coverage(paper, by_paper[paper], layout)
        cov_rows.append(cov)
        if cov["dup"] or cov["extra"]:
            failures.append("%s: dup=%s extra=%s" % (paper, cov["dup"], cov["extra"]))
        if cov["miss_by_class"].get("unexplained"):
            failures.append("%s: unexplained miss %s" % (paper, cov["miss_by_class"]["unexplained"]))
        if cov["units"] != cov["groups"]:
            failures.append("%s: units %d != groups %d" % (paper, cov["units"], cov["groups"]))

    tally = collections.Counter(r["class"] for r in bucket_rows)
    (RECON / "bucket-coverage.json").write_text(
        json.dumps({"buckets": bucket_rows, "tally": dict(tally),
                    "papers": cov_rows,
                    "duplicate_blocks": sum(len(c["dup"]) for c in cov_rows),
                    "extra_blocks": sum(len(c["extra"]) for c in cov_rows),
                    "miss_by_class": dict(collections.Counter(
                        k for c in cov_rows for k, v in c["miss_by_class"].items() for _ in range(v)))},
                   indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    print("buckets %d  tally %s" % (len(bucket_rows), dict(tally)))
    print("papers %d  dup %d  extra %d  miss %s" % (
        len(cov_rows), sum(len(c["dup"]) for c in cov_rows), sum(len(c["extra"]) for c in cov_rows),
        dict(collections.Counter(k for c in cov_rows for k, v in c["miss_by_class"].items() for _ in range(v)))))
    for f in failures:
        print("FAIL", f)
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
