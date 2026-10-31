"""Rebuild paragraph boundaries from PDF text geometry, one paper at a time.

Not a batch classifier: this only measures line positions and groups lines that
belong to one paragraph. Job coding stays manual.

Two-column pages are handled as two independent reading streams (left column top
to bottom, then right column), because otherwise the two columns interleave line
by line and every paragraph boundary is wrong.

Usage:
  python -I lanes/L5-e-ledger/tools/para_extract.py layout <paper_id>
  python -I lanes/L5-e-ledger/tools/para_extract.py dump <paper_id> <chapter>
"""
import json
import pathlib
import re
import sys

import pymupdf

ROOT = pathlib.Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "artifacts" / "corpus" / "manifest.jsonl"
PDF_ROOT = pathlib.Path(r"F:\MCM\MCM-ICM-master")
OUT = ROOT / "lanes" / "L5-e-ledger" / "layout"

HEADER = re.compile(r"(Team\s*#?\s*\d+|Page\s+\d+\s*of\s*\d+|^\s*\d+\s*$)", re.I)


def page_lines(page):
    rows = []
    for block in page.get_text("dict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            text = "".join(s["text"] for s in line["spans"]).strip()
            if not text:
                continue
            size = max(round(s["size"], 1) for s in line["spans"] if s["text"].strip())
            bold = any("Bold" in s["font"] for s in line["spans"])
            x0, y0, x1, y1 = line["bbox"]
            rows.append({"text": text, "x0": x0, "x1": x1, "y0": y0, "y1": y1,
                         "size": size, "bold": bold})
    rows.sort(key=lambda r: (round(r["y0"], 1), r["x0"]))
    return rows


def modal_size(doc):
    votes = {}
    for pno in range(len(doc)):
        for row in page_lines(doc[pno]):
            votes[row["size"]] = votes.get(row["size"], 0) + len(row["text"])
    return max(votes, key=votes.get) if votes else 10.0


def is_two_column(page, rows, size):
    """A page is two-column when long body lines start in both halves."""
    width = page.rect.width
    mid = width / 2
    long_rows = [r for r in rows if abs(r["size"] - size) < 0.7 and len(r["text"]) >= 25]
    if len(long_rows) < 8:
        return False, mid
    left = sum(1 for r in long_rows if r["x0"] < mid)
    right = len(long_rows) - left
    return (left >= 0.2 * len(long_rows) and right >= 0.2 * len(long_rows)), mid


def margins(doc, size):
    """Left margin per column side: 0 for the left column, 1 for the right one."""
    votes = {0: {}, 1: {}}
    for pno in range(len(doc)):
        page = doc[pno]
        rows = page_lines(page)
        two, mid = is_two_column(page, rows, size)
        for r in rows:
            if abs(r["size"] - size) >= 0.7 or len(r["text"]) < 25:
                continue
            side = 1 if (two and r["x0"] >= mid) else 0
            key = int(round(r["x0"] / 3) * 3)
            votes[side][key] = votes[side].get(key, 0) + len(r["text"])
    left = float(max(votes[0], key=votes[0].get)) if votes[0] else 0.0
    right = float(max(votes[1], key=votes[1].get)) if votes[1] else left
    return {0: left, 1: right}


def build(paper_id):
    row = None
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("paper_id") == paper_id:
            row = rec
            break
    if row is None:
        raise SystemExit("not in manifest: " + paper_id)
    doc = pymupdf.open(PDF_ROOT / row["relative_path"])
    body_size = modal_size(doc)
    body_left = margins(doc, body_size)

    paras = []
    cur = None
    prev = None  # last kept line of the open paragraph
    for pno in range(len(doc)):
        page = doc[pno]
        rows = page_lines(page)
        if not rows:
            continue
        two, mid = is_two_column(page, rows, body_size)
        buckets = [[r for r in rows if r["x0"] < mid], [r for r in rows if r["x0"] >= mid]] if two else [rows]

        for side, chunk in enumerate(buckets):
            if not chunk:
                continue
            # body line spacing inside this column: median gap between full lines
            gaps = []
            for a, b in zip(chunk, chunk[1:]):
                d = b["y0"] - a["y0"]
                if 0.8 * body_size < d < 40 and abs(b["size"] - body_size) < 0.6:
                    gaps.append(d)
            gaps.sort()
            spacing = gaps[len(gaps) // 2] if gaps else 12.0
            left = body_left[side]

            for ln in chunk:
                if HEADER.search(ln["text"]) and (ln["y0"] < 60 or ln["y0"] > 700):
                    continue
                is_body = abs(ln["size"] - body_size) < 0.7
                indented = is_body and (ln["x0"] - left) > 6
                new_stream = prev is not None and cur is not None and (
                    cur["page_end"] != pno + 1 or cur["side"] != side)
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
                    cur = {"page_start": pno + 1, "page_end": pno + 1, "lines": [],
                           "x0": round(ln["x0"], 1), "size": ln["size"],
                           "is_body": is_body, "bold": ln["bold"], "side": side}
                cur["lines"].append(ln)
                cur["page_end"] = pno + 1
                prev = ln
    if cur:
        paras.append(cur)

    out = []
    for p in paras:
        text = " ".join(x["text"] for x in p["lines"])
        text = re.sub(r"\s+", " ", text).strip()
        rec = {"pages": [p["page_start"], p["page_end"]],
               "kind": "body" if p["is_body"] else ("heading" if p["size"] > body_size + 0.7 else "display"),
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
        {"paper": paper_id, "body_size": body_size, "body_left": body_left, "paragraphs": out},
        ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def chapters(paper_id):
    path = ROOT / "artifacts" / "language-units" / (paper_id + ".json")
    rec = json.loads(path.read_text(encoding="utf-8"))
    return rec.get("chapter_layouts", [])


def main():
    mode = sys.argv[1]
    paper = sys.argv[2]
    if mode == "layout":
        out = build(paper)
        body = [p for p in out if p["kind"] == "body"]
        print(paper, "paragraphs", len(out), "body", len(body))
        for p in out[:8]:
            print(" ", p["n"], p["kind"], p["pages"], p["words"],
                  p["first"][:80].encode("ascii", "replace").decode())
        return
    if mode == "dump":
        chapter = sys.argv[3]
        lay = json.loads((OUT / (paper + ".json")).read_text(encoding="utf-8"))
        spans = [(c["page_start"], c["page_end"]) for c in chapters(paper) if c["chapter"] == chapter]
        if not spans:
            raise SystemExit("chapter not in layout: " + chapter)
        lo, hi = spans[0]
        rows = [p for p in lay["paragraphs"] if lo <= p["pages"][0] <= hi]
        print("# %s %s pages %s-%s paragraphs %d" % (paper, chapter, lo, hi, len(rows)))
        for p in rows:
            print("\n[%d] %s p%s-%s w=%d" % (p["n"], p["kind"], p["pages"][0], p["pages"][1], p["words"]))
            print(p["text"])
        return
    raise SystemExit("mode: layout | dump")


if __name__ == "__main__":
    main()
