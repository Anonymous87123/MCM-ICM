"""Find printed rule grids the region measurer did not return, by counting long rules per page.

A variable-definition table on this paper is drawn as a closed box with one rule per row, so a
page carrying eight or more full-measure horizontal rules holds a grid the layout pass skipped.
"""

import sys
from pathlib import Path

import pdfplumber

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
head = (LANE / ".proxy" / "P-B-2015-38720-26d38781-read.txt").read_text(
    encoding="utf-8").splitlines()
SRC = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))

with pdfplumber.open(SRC) as pdf:
    for page_no, page in enumerate(pdf.pages, 1):
        hs = []
        for ln in page.lines:
            w = abs(ln["x1"] - ln["x0"])
            h = abs(ln["bottom"] - ln["top"])
            if h <= 1.6 and w >= 200:
                hs.append((round(ln["top"], 1), round(min(ln["x0"], ln["x1"]), 1),
                           round(max(ln["x0"], ln["x1"]), 1)))
        for rc in page.rects:
            w = rc["x1"] - rc["x0"]
            h = rc["bottom"] - rc["top"]
            if h <= 2.0 and w >= 200:
                hs.append((round(rc["top"], 1), round(rc["x0"], 1), round(rc["x1"], 1)))
        if len(hs) >= 5:
            hs.sort()
            print(f"p{page_no}: {len(hs)} long rules, y {hs[0][0]}..{hs[-1][0]}, "
                  f"x {hs[0][1]}..{hs[0][2]}")
