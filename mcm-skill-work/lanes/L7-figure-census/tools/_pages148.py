"""Per-page text dump for the hand pass (GBK stdout cannot print the paper's unicode)."""


import sys
from pathlib import Path

import pdfplumber

LANE = Path(__file__).resolve().parents[1]
head = (LANE / ".proxy" / f"{sys.argv[1]}-read.txt").read_text(encoding="utf-8").splitlines()
src = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))

out = []
with pdfplumber.open(src) as pdf:
    for i, page in enumerate(pdf.pages, 1):
        text = page.extract_text() or ""
        out.append(f"=== page {i}\n{text}\n")

dest = LANE / ".proxy" / f"{sys.argv[1]}-pages.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print(dest)
