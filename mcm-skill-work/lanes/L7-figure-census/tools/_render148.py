"""Render selected pages to PNG at the scale the layout crops assume (2.084 px/pt)."""

import sys
from pathlib import Path

import pdfplumber

LANE = Path(__file__).resolve().parents[1]
head = (LANE / ".proxy" / f"{sys.argv[1]}-read.txt").read_text(encoding="utf-8").splitlines()
src = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))
tag = sys.argv[2]
pages = [int(p) for p in sys.argv[3].split(",")]

with pdfplumber.open(src) as pdf:
    for n in pages:
        img = pdf.pages[n - 1].to_image(resolution=150)
        dest = LANE / ".proxy" / f"{tag}p{n:02d}.png"
        img.save(dest)
        print(dest)
