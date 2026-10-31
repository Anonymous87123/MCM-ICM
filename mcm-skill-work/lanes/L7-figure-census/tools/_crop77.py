"""Crop proxies for P-B-2015-38720-26d38781, one per measured region, at 150 dpi.

Crop boxes come from the measured bbox in points times 2.0833 px/pt, with a small margin, so
they do not depend on the artifact render's 2.001 scale hint.
"""

import json
import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PID = "P-B-2015-38720-26d38781"
SCALE = 2.0833
TOOL = LANE.parents[1] / "scripts" / "make_review_proxy.py"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

want = {(int(p.split("r")[0]), int(p.split("r")[1])) for p in sys.argv[1:]}
for pg in LAYOUT["pages"]:
    regs = sorted(pg["regions"], key=lambda r: (r["bbox"][1], r["bbox"][0]))
    for i, reg in enumerate(regs, 1):
        if want and (pg["page"], i) not in want:
            continue
        x0, y0, x1, y1 = reg["bbox"]
        box = [int((x0 - 8) * SCALE), int((y0 - 16) * SCALE),
               int((x1 + 8) * SCALE), int((y1 + 16) * SCALE)]
        src = LANE / ".proxy" / f"pa77p{pg['page']:02d}.png"
        dest = LANE / ".proxy" / f"q77p{pg['page']:02d}r{i}.jpg"
        cmd = [sys.executable, "-I", str(TOOL), "--input", str(src), "--output", str(dest),
               "--crop", ",".join(str(v) for v in box), "--max-bytes", "450000"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(dest.name, box, res.returncode, (res.stdout or res.stderr).strip().splitlines()[-1:])
