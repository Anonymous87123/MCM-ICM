"""Reading list for one paper: measured regions plus the text around them.

Usage: python -I lanes/L7-figure-census/tools/dump_paper.py <pid> [--pad-px 90]

Writes .proxy/<pid>-read.txt. The paper is read from that file; the crop is made only
when a region's identity or boundary is still doubtful after reading the dump.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
ROOT = LANE.parents[1]
LAYOUT = LANE / "layout"
PAPERS = ROOT / "artifacts" / "papers"
PROXY = LANE / ".proxy"
PNG_SCALE_HINT = 2.0  # rendered pages are ~2x the PDF point box; confirmed per paper below


def main(argv: list[str]) -> int:
    pid = argv[0]
    pad = int(argv[argv.index("--pad-px") + 1]) if "--pad-px" in argv else 90
    lay = json.loads((LAYOUT / f"{pid}.json").read_text(encoding="utf-8"))
    text_dir = PAPERS / pid / "text" / "pages"
    lines = [f"paper {pid}", f"source {lay['source_pdf']}", f"pages {lay['page_count']} "
             f"regions {lay['region_total']} sha {lay['layout_sha256']}", ""]
    for pg in lay["pages"]:
        page_no, w, h = pg["page"], pg["width"], pg["height"]
        scale = PNG_SCALE_HINT
        png = PAPERS / pid / "rendered" / f"page-{page_no:04d}.png"
        if png.exists():
            from PIL import Image
            with Image.open(png) as im:
                scale = im.size[0] / w
        lines.append(f"=== page {page_no}  (points {w}x{h}, png scale {scale:.3f})")
        tf = text_dir / f"page-{page_no:04d}.txt"
        if tf.exists():
            txt = re.sub(r"\s+", " ", tf.read_text(encoding="utf-8", errors="replace"))
            m = re.search(r"(Figure|Table)\s*\d+", txt)
            lines.append(f"  text {len(txt)}ch  first caption token at {m.group(0) if m else 'none'}")
        for k, r in enumerate(pg["regions"], 1):
            x0, y0, x1, y1 = r["bbox"]
            crop = (max(0, int(x0 * scale) - pad), max(0, int(y0 * scale) - pad),
                    int(x1 * scale) + pad, int(y1 * scale) + pad)
            flags = []
            if r["fragment_suspected"]:
                flags.append("fragment?")
            if r["touches_top"]:
                flags.append("touches-top")
            if r["touches_bottom"]:
                flags.append("touches-bottom")
            lines.append(
                f"  r{k} y={y0:.0f}-{y1:.0f} {r['kind']} paths={r['path_count']} "
                f"area={r['area_frac']:.3f} aspect={r['aspect']} {' '.join(flags)}".rstrip())
            if r["text_inside"]:
                lines.append(f"      inside: {' '.join(r['text_inside'])[:160]}")
            if r["caption_below"]:
                lines.append(f"      cap↓: {r['caption_below'][:160]}")
            if r["caption_above"]:
                lines.append(f"      cap↑: {r['caption_above'][:160]}")
            lines.append(f"      crop: {crop[0]},{crop[1]},{crop[2]},{crop[3]}")
        lines.append("")
    out = PROXY / f"{pid}-read.txt"
    PROXY.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
