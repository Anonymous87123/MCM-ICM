"""Print text blocks with bbox for the given pages of one paper.

  python -I tools/_lines.py <pid> <page> [page ...]
"""

import sys

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

import fitz  # noqa: E402

from pathlib import Path  # noqa: E402

LANE = Path(__file__).resolve().parents[1]
PID = sys.argv[1]
read = (LANE / ".proxy" / f"{PID}-read.txt").read_text(encoding="utf-8").splitlines()
src = next(line for line in read if line.startswith("source ")).split(" ", 1)[1].strip()

doc = fitz.open(src)
for arg in sys.argv[2:]:
    page = doc[int(arg) - 1]
    print(f"=== page {arg}")
    for block in page.get_text("blocks"):
        x0, y0, x1, y1, text = block[0], block[1], block[2], block[3], block[4]
        text = " ".join(text.split())
        if text:
            print(f"  [{x0:6.1f} {y0:6.1f} {x1:6.1f} {y1:6.1f}] {text[:150]}")
