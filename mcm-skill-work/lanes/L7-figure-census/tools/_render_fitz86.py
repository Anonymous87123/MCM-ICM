"""Render selected pages of paper 86 with PyMuPDF at the 150 dpi the crop boxes assume."""

import sys
from pathlib import Path

import pymupdf

LANE = Path(__file__).resolve().parents[1]
head = (LANE / ".proxy" / f"{sys.argv[1]}-read.txt").read_text(encoding="utf-8").splitlines()
src = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))
tag = sys.argv[2]
pages = [int(p) for p in sys.argv[3].split(",")]

doc = pymupdf.open(src)
for n in pages:
    pix = doc[n - 1].get_pixmap(dpi=150)
    dest = LANE / ".proxy" / f"{tag}p{n:02d}.png"
    pix.save(dest)
    print(dest)
