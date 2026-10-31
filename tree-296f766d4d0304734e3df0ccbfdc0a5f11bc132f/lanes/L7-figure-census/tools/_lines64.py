"""Coordinate-stamped line dump for one paper's selected pages (GBK stdout cannot print the text)."""


import sys
from collections import defaultdict
from pathlib import Path

import pdfplumber

LANE = Path(__file__).resolve().parents[1]
pid = sys.argv[1]
pages = [int(x) for x in sys.argv[2].split(",")]
head = (LANE / ".proxy" / f"{pid}-read.txt").read_text(encoding="utf-8").splitlines()
src = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))

out = []
with pdfplumber.open(src) as pdf:
    for n in pages:
        page = pdf.pages[n - 1]
        buckets = defaultdict(list)
        for w in page.extract_words(keep_blank_chars=False, use_text_flow=False):
            buckets[round(w["top"], 1)].append(w)
        out.append(f"=== page {n}  height={page.height:.1f}")
        for top in sorted(buckets):
            row = sorted(buckets[top], key=lambda w: w["x0"])
            x0 = min(w["x0"] for w in row)
            x1 = max(w["x1"] for w in row)
            txt = " ".join(w["text"] for w in row)
            size = max(w.get("height", 0) for w in row)
            out.append(f"{top:7.1f} {x0:6.1f} {x1:6.1f} sz{size:4.1f} | {txt}")

dest = LANE / ".proxy" / f"{pid}-lines2.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print(dest)
