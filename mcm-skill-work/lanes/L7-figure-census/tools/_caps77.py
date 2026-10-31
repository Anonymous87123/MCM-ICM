"""Scan paper 77 for printed caption lines (Figure/Table) with their page and y position.

The ctx caption detector returned a single caption on this paper while the prose cites figures
up to 28, so the captions are located here from the page text lines themselves.
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
        hits = []
        for ln in page.extract_text_lines():
            t = ln["text"].strip()
            if t[:7].lower().startswith(("figure ", "table ")) or t[:5].lower() == "fig. ":
                hits.append((round(ln["top"], 1), round(ln["x0"], 1), t))
        if hits:
            print(f"--- p{page_no}")
            for top, x0, t in hits:
                print(f"  y={top:6.1f} x={x0:6.1f} {t[:150]}")
