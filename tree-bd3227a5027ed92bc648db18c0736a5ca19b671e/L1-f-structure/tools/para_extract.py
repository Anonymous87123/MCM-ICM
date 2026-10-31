"""Rebuild paragraph boundaries from PDF text geometry, one paper at a time.

Not a batch classifier: this only measures line positions and groups lines that
belong to one paragraph. Job coding stays manual.

Usage:
  python -I lanes/L1-f-structure/tools/para_extract.py layout <paper_id>
  python -I lanes/L1-f-structure/tools/para_extract.py dump <paper_id> <chapter>
"""
import json
import pathlib
import re
import sys

import pymupdf

ROOT = pathlib.Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "artifacts" / "corpus" / "manifest.jsonl"
PDF_ROOT = pathlib.Path(r"F:\MCM\MCM-ICM-master")
OUT = ROOT / "lanes" / "L1-f-structure" / "layout"

HEADER = re.compile(r"(Team\s*#?\s*\d+|Page\s+\d+\s*of\s*\d+|^\s*\d+\s*$)", re.I)


def body_style(doc, page_numbers):
    """Modal body font size, then the left margin used by those body lines.

    Header and footer lines often share the body font size but sit on a different
    margin, so the margin vote only counts long lines at the modal size.
    """
    size_votes: dict[float, int] = {}
    lines = []
    for pno in page_numbers:
        for block in doc[pno].get_text("dict")["blocks"]:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                text = "".join(s["text"] for s in line["spans"]).strip()
                if len(text) < 3:
                    continue
                size = max(round(s["size"], 1) for s in line["spans"] if s["text"].strip())
                size_votes[size] = size_votes.get(size, 0) + len(text)
                lines.append((size, line["bbox"][0], len(text)))
    size = max(size_votes, key=size_votes.get) if size_votes else 10.0
    left_votes: dict[int, int] = {}
    for lsize, x0, n in lines:
        if abs(lsize - size) < 0.7 and n >= 25:
            key = int(round(x0 / 3) * 3)
            left_votes[key] = left_votes.get(key, 0) + n
    left = max(left_votes, key=left_votes.get) if left_votes else 0.0
    return size, float(left)


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
    pdf_path = PDF_ROOT / row["relative_path"]
    doc = pymupdf.open(pdf_path)
    body_size, body_left = body_style(doc, range(len(doc)))

    paras = []
    cur = None
    prev_y0 = None
    prev_x1 = None
    for pno in range(len(doc)):
        lines = page_lines(doc[pno])
        if not lines:
            continue
        # body line spacing on this page: median gap between consecutive full lines
        gaps = []
        for a, b in zip(lines, lines[1:]):
            d = b["y0"] - a["y0"]
            # inline math raises superscripts into their own short line; those
            # gaps are half a text line and must not vote for the spacing
            if 0.8 * body_size < d < 40 and abs(b["size"] - body_size) < 0.6:
                gaps.append(d)
        gaps.sort()
        spacing = gaps[len(gaps) // 2] if gaps else 12.0

        for idx, ln in enumerate(lines):
            if HEADER.search(ln["text"]) and (ln["y0"] < 60 or ln["y0"] > 700):
                continue
            is_body = abs(ln["size"] - body_size) < 0.7
            indented = is_body and (ln["x0"] - body_left) > 6
            new_page = cur is not None and cur["page_end"] != pno + 1
            new_para = False
            if is_body:
                if cur is None:
                    new_para = True
                elif not cur["is_body"]:
                    new_para = True
                elif new_page:
                    # a paragraph running over a page break continues unless the
                    # previous line closed a sentence and this line starts fresh
                    prev_text = cur["lines"][-1]["text"].rstrip()
                    closed = prev_text.endswith((".", "!", "?", ":"))
                    starts_lower = ln["text"][:1].islower()
                    new_para = closed and not starts_lower
                else:
                    gap = ln["y0"] - prev_y0
                    if gap > 1.25 * spacing:
                        new_para = True
                    elif indented:
                        new_para = True
                    elif ln["y0"] < prev_y0 - 1:  # column wrap
                        new_para = True
            else:
                if cur is None or cur["is_body"] is False and ln["y0"] - prev_y0 > 1.6 * spacing:
                    new_para = True
                elif cur["is_body"] and ln["y0"] - prev_y0 > 1.9 * spacing:
                    new_para = True

            if new_para:
                if cur:
                    paras.append(cur)
                cur = {"page_start": pno + 1, "page_end": pno + 1, "lines": [],
                       "x0": round(ln["x0"], 1), "size": ln["size"],
                       "is_body": is_body, "bold": ln["bold"]}
            cur["lines"].append(ln)
            cur["page_end"] = pno + 1
            prev_y0, prev_x1 = ln["y0"], ln["x1"]
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
            print(" ", p["n"], p["kind"], p["pages"], p["words"], p["first"][:80])
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
