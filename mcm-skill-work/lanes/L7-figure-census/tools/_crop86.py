"""Crop proxies for P-D-2015-35780-97fea85b, one per measured region, at 150 dpi."""

import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

LANE = Path(__file__).resolve().parents[1]
PID = "P-D-2015-35780-97fea85b"
TOOL = LANE.parents[1] / "scripts" / "make_review_proxy.py"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

want = {(int(p.split("r")[0]), int(p.split("r")[1])) for p in sys.argv[1:]}
for pg in LAYOUT["pages"]:
    regs = sorted(pg["regions"], key=lambda r: (r["bbox"][1], r["bbox"][0]))
    if not regs:
        continue
    src = LANE / ".proxy" / f"pd86p{pg['page']:02d}.png"
    s = Image.open(src).size[0] / float(pg.get("width") or 612.0)
    for i, reg in enumerate(regs, 1):
        if want and (pg["page"], i) not in want:
            continue
        x0, y0, x1, y1 = reg["bbox"]
        box = [max(0, int((x0 - 8) * s)), max(0, int((y0 - 16) * s)),
               int((x1 + 8) * s), int((y1 + 16) * s)]
        dest = LANE / ".proxy" / f"qd86p{pg['page']:02d}r{i}.jpg"
        cmd = [sys.executable, "-I", str(TOOL), "--input", str(src), "--output", str(dest),
               "--crop", ",".join(str(v) for v in box), "--max-bytes", "450000"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(dest.name, box, res.returncode, (res.stdout or res.stderr).strip().splitlines()[-1:])
