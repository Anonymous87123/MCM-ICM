"""Rebuild one crop per measured region from the rendered page PNG.

The raster is the authoritative source for anything the text layer cannot settle
(three-d, rule style, zebra, merged cells), so every region gets its own bounded
JPEG proxy before the hand pass looks at it. Nothing is decided here.

Crop rectangle = region bbox in points, scaled to the rendered PNG, plus a small
margin so a caption or axis label just outside the bbox stays visible.

Usage: python -I lanes/L7-figure-census/tools/crop_regions.py <pid> [page ...]
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PROXY = LANE / ".proxy"
PAPERS = LANE.parents[1] / "artifacts" / "papers"
SCRIPT = LANE.parents[1] / "scripts" / "make_review_proxy.py"
MARGIN_PT = 8.0
MAX_BYTES = "450000"


def main(argv: list[str]) -> int:
    if not argv:
        raise SystemExit("usage: crop_regions.py <pid> [page ...]")
    pid = argv[0]
    wanted = {int(a) for a in argv[1:]}
    layout = json.loads((LANE / "layout" / f"{pid}.json").read_text(encoding="utf-8"))
    made = []
    for pg in layout["pages"]:
        page = pg["page"]
        if wanted and page not in wanted:
            continue
        png = PAPERS / pid / "rendered" / f"page-{page:04d}.png"
        if not png.exists():
            print(f"  no render for page {page}")
            continue
        scale = png_height(png) / pg["height"]
        for idx, region in enumerate(
                sorted(pg["regions"], key=lambda r: r["bbox"][1]), 1):
            x0, y0, x1, y1 = region["bbox"]
            px_w, px_h = png_size(png)
            box = [max(0, int((x0 - MARGIN_PT) * scale)),
                   max(0, int((y0 - MARGIN_PT) * scale)),
                   min(px_w, int((x1 + MARGIN_PT) * scale)),
                   min(px_h, int((y1 + MARGIN_PT) * scale))]
            out = PROXY / f"{pid}-p{page}-r{idx}.jpg"
            subprocess.run([sys.executable, "-I", str(SCRIPT), "--input", str(png),
                            "--output", str(out), "--crop",
                            ",".join(str(v) for v in box),
                            "--max-bytes", MAX_BYTES], check=True,
                           stdout=subprocess.DEVNULL)
            made.append({"page": page, "region": idx, "bbox": region["bbox"],
                         "crop_px": box, "file": out.name})
        print(f"  p{page}: {len(pg['regions'])} crops")
    path = PROXY / f"{pid}-crops.json"
    path.write_text(json.dumps(made, indent=1), encoding="utf-8")
    print(f"{len(made)} crops -> {path}")
    return 0


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as fh:
        head = fh.read(24)
    return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")


def png_height(path: Path) -> int:
    return png_size(path)[1]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
