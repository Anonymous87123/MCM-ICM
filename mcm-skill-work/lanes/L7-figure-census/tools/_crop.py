"""Crop proxies for one paper, one per measured region, at 150 dpi.

  python -I tools/_crop.py <pid> <page-tag> "[4:1 10:1 ...]"   optional region filter, page:region
"""

import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

LANE = Path(__file__).resolve().parents[1]
TOOL = LANE.parents[1] / "scripts" / "make_review_proxy.py"

PID = sys.argv[1]
TAG = sys.argv[2]
want = set()
for tok in sys.argv[3:]:
    page, _, reg = tok.partition(":")
    want.add((int(page), int(reg)))

LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
for pg in LAYOUT["pages"]:
    regs = sorted(pg["regions"], key=lambda r: (r["bbox"][1], r["bbox"][0]))
    if not regs:
        continue
    if want and not any((pg["page"], i) in want for i in range(1, len(regs) + 1)):
        continue
    src = LANE / ".proxy" / f"{TAG}p{pg['page']:02d}.png"
    im = Image.open(src)
    s = im.size[0] / float(pg.get("width") or 595.32)
    for i, reg in enumerate(regs, 1):
        if want and (pg["page"], i) not in want:
            continue
        x0, y0, x1, y1 = reg["bbox"]
        box = [max(0, int((x0 - 8) * s)), max(0, int((y0 - 16) * s)),
               min(im.size[0], int((x1 + 8) * s)), min(im.size[1], int((y1 + 16) * s))]
        dest = LANE / ".proxy" / f"q{TAG}p{pg['page']:02d}r{i}.jpg"
        cmd = [sys.executable, "-I", str(TOOL), "--input", str(src), "--output", str(dest),
               "--crop", ",".join(str(v) for v in box), "--max-bytes", "450000"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(dest.name, box, res.returncode, (res.stdout or res.stderr).strip().splitlines()[-1:])
