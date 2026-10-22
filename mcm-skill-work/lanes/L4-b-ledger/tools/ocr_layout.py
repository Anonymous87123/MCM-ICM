"""Rebuild paragraph boundaries from OCR line boxes for papers with no text layer.

Same measurement rules as `para_extract.py`, but the geometry comes from
`artifacts/papers/<pid>/ocr-lines.jsonl` (RapidOCR at 200 dpi) instead of the PDF
text layer, which a scanned paper does not have. Line boxes are converted from
pixels to points before the indent and spacing thresholds are applied, so both
extractors measure in the same unit.

The layout record it writes carries `"extractor": "ocr_layout"` so that
`check.py` re-runs this tool for the reproducibility hash instead of the PDF one.

Usage:
  python -I lanes/L4-b-ledger/tools/ocr_layout.py layout <paper_id>
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
PAPERS = ROOT / "artifacts" / "papers"
OUT = ROOT / "lanes" / "L4-b-ledger" / "layout"

PX_TO_PT = 72.0 / 200.0
BODY_LOW = 0.75   # box heights carry the ascender and descender of the line, so the
BODY_HIGH = 1.12  # OCR size band is wider than a PDF font size band
HEADING = 1.15
HEADER = re.compile(r"(Team\s*#?\s*\d+|Page\s+\d+\s+of\s+\d+|^\s*\d+\s*$)", re.I)


def load_pages(paper_id):
    path = PAPERS / paper_id / "ocr-lines.jsonl"
    pages = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        rows = []
        for ln in rec.get("lines") or []:
            text = (ln.get("text") or "").strip()
            if not text:
                continue
            xs = [p[0] for p in ln["box"]]
            ys = [p[1] for p in ln["box"]]
            rows.append({"text": text,
                         "x0": min(xs) * PX_TO_PT, "x1": max(xs) * PX_TO_PT,
                         "y0": min(ys) * PX_TO_PT, "y1": max(ys) * PX_TO_PT,
                         "size": round((max(ys) - min(ys)) * PX_TO_PT, 1),
                         "bold": False})
        rows.sort(key=lambda r: (round(r["y0"], 1), r["x0"]))
        pages.append({"rows": rows,
                      "width": (max((r["x1"] for r in rows), default=0.0)),
                      "height": (max((r["y1"] for r in rows), default=0.0))})
    return pages


def is_body_size(size, body_size):
    return BODY_LOW * body_size <= size <= BODY_HIGH * body_size


def modal_size(pages):
    votes = {}
    for page in pages:
        for row in page["rows"]:
            votes[row["size"]] = votes.get(row["size"], 0) + len(row["text"])
    return max(votes, key=votes.get) if votes else 10.0


def is_two_column(page, rows, size):
    """A page is two-column when long body lines start in both halves."""
    mid = page["width"] / 2
    long_rows = [r for r in rows if is_body_size(r["size"], size) and len(r["text"]) >= 25]
    if len(long_rows) < 8:
        return False, mid
    left = sum(1 for r in long_rows if r["x0"] < mid)
    right = len(long_rows) - left
    return (left >= 0.2 * len(long_rows) and right >= 0.2 * len(long_rows)), mid


def margins(pages, size):
    """Left margin per column side: 0 for the left column, 1 for the right one."""
    votes = {0: {}, 1: {}}
    for page in pages:
        rows = page["rows"]
        two, mid = is_two_column(page, rows, size)
        for r in rows:
            if not is_body_size(r["size"], size) or len(r["text"]) < 25:
                continue
            side = 1 if (two and r["x0"] >= mid) else 0
            key = int(round(r["x0"] / 3) * 3)
            votes[side][key] = votes[side].get(key, 0) + len(r["text"])
    left = float(max(votes[0], key=votes[0].get)) if votes[0] else 0.0
    right = float(max(votes[1], key=votes[1].get)) if votes[1] else left
    return {0: left, 1: right}


def build(paper_id):
    pages = load_pages(paper_id)
    body_size = modal_size(pages)
    body_left = margins(pages, body_size)

    paras = []
    cur = None
    prev = None  # last kept line of the open paragraph
    for pno, page in enumerate(pages, 1):
        rows = page["rows"]
        if not rows:
            continue
        two, mid = is_two_column(page, rows, body_size)
        buckets = [[r for r in rows if r["x0"] < mid], [r for r in rows if r["x0"] >= mid]] if two else [rows]

        for side, chunk in enumerate(buckets):
            if not chunk:
                continue
            gaps = []
            for a, b in zip(chunk, chunk[1:]):
                d = b["y0"] - a["y0"]
                if 0.8 * body_size < d < 40 and is_body_size(b["size"], body_size):
                    gaps.append(d)
            gaps.sort()
            spacing = gaps[len(gaps) // 2] if gaps else 12.0
            left = body_left[side]

            for ln in chunk:
                if HEADER.search(ln["text"]) and (
                        ln["y0"] < 0.06 * page["height"] or ln["y0"] > 0.94 * page["height"]):
                    continue
                is_body = is_body_size(ln["size"], body_size)
                # a first line is indented relative to the line above it, not relative
                # to the page margin: an indented block with a hanging indent (bullets,
                # inset strategies) starts every line past the margin and would split
                # into one block per line under a margin rule
                indented = is_body and prev is not None and (ln["x0"] - prev["x0"]) > 6
                new_stream = prev is not None and cur is not None and (
                    cur["page_end"] != pno or cur["side"] != side)
                new_para = False
                if is_body:
                    if cur is None:
                        new_para = True
                    elif not cur["is_body"]:
                        new_para = True
                    elif new_stream:
                        # a paragraph continues over a page or column break unless
                        # the previous line closed a sentence and this one starts fresh
                        closed = prev["text"].rstrip().endswith((".", "!", "?", ":"))
                        new_para = closed and not ln["text"][:1].islower()
                    else:
                        gap = ln["y0"] - prev["y0"]
                        if gap > 1.25 * spacing:
                            new_para = True
                        elif indented:
                            new_para = True
                        elif ln["y0"] < prev["y0"] - 1:  # column wrap
                            new_para = True
                else:
                    if cur is None or (cur["is_body"] is False and ln["y0"] - prev["y0"] > 1.6 * spacing):
                        new_para = True
                    elif cur["is_body"] and ln["y0"] - prev["y0"] > 1.9 * spacing:
                        new_para = True

                if new_para:
                    if cur:
                        paras.append(cur)
                    cur = {"page_start": pno, "page_end": pno, "lines": [],
                           "x0": round(ln["x0"], 1), "size": ln["size"],
                           "is_body": is_body, "bold": ln["bold"], "side": side}
                cur["lines"].append(ln)
                cur["page_end"] = pno
                prev = ln
    if cur:
        paras.append(cur)

    out = []
    for p in paras:
        text = " ".join(x["text"] for x in p["lines"])
        text = re.sub(r"\s+", " ", text).strip()
        rec = {"pages": [p["page_start"], p["page_end"]],
               "kind": "body" if p["is_body"] else ("heading" if p["size"] >= HEADING * body_size else "display"),
               "x0": p["x0"], "words": len(re.findall(r"[A-Za-z']+", text)),
               "first": text[:110], "text": text}
        # display equations and page-break fragments are not paragraphs of their own
        if rec["words"] < 5 and out and out[-1]["kind"] == "body":
            out[-1]["text"] += " " + text
            out[-1]["pages"][1] = max(out[-1]["pages"][1], rec["pages"][1])
            out[-1]["words"] += rec["words"]
            continue
        out.append(rec)
    for i, rec in enumerate(out, 1):
        rec["n"] = i
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / (paper_id + ".json")).write_text(json.dumps(
        {"paper": paper_id, "extractor": "ocr_layout", "body_size": body_size,
         "body_left": body_left, "paragraphs": out},
        ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def main():
    mode = sys.argv[1]
    paper = sys.argv[2]
    if mode != "layout":
        raise SystemExit("mode: layout")
    out = build(paper)
    body = [p for p in out if p["kind"] == "body"]
    print(paper, "paragraphs", len(out), "body", len(body))
    for p in out[:8]:
        print(" ", p["n"], p["kind"], p["pages"], p["words"],
              p["first"][:80].encode("ascii", "replace").decode())


if __name__ == "__main__":
    main()
