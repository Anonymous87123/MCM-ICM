"""Compact per-region worksheet for P-A-2015-40764-20552f34.

One line per measured region plus the captions printed on the same page, and the y position of
every p7 text line so the 3.1.x sub-heading order can be read off.
"""

import json
from pathlib import Path

import pdfplumber

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2015-40764-20552f34"
CTX = json.loads((LANE / ".proxy" / f"{PID}-ctx.json").read_text(encoding="utf-8"))
head = (LANE / ".proxy" / f"{PID}-read.txt").read_text(encoding="utf-8").splitlines()
SRC = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))

for page_no in CTX["pages"]:
    caps = [c["text"] for c in CTX["captions"] if c["page"] == page_no]
    regs = sorted((r for r in CTX["regions"] if r["page"] == page_no),
                  key=lambda r: (r["bbox"][1], r["bbox"][0]))
    for i, reg in enumerate(regs, 1):
        x0, y0, x1, y1 = reg["bbox"]
        print(f"p{page_no} r{i} y={y0:.0f}..{y1:.0f} x={x0:.0f}..{x1:.0f} "
              f"area={reg['area_frac']} paths={reg.get('paths')} "
              f"path={' / '.join(reg['section_path'])}")
    for c in caps:
        print(f"     cap {c[:70]}")

print("\n-- p7 text lines --")
with pdfplumber.open(SRC) as pdf:
    for ln in sorted(pdf.pages[6].extract_text_lines(), key=lambda l: l["top"]):
        print(f"  y={ln['top']:6.1f} {ln['text'][:70]!r}")
