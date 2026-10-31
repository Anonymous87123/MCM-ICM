"""Geometry dump for P-A-2015-40764-20552f34: rules, rects, images, text lines per page."""

import sys
from pathlib import Path

import pdfplumber

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2015-40764-20552f34"
head = (LANE / ".proxy" / f"{PID}-read.txt").read_text(encoding="utf-8").splitlines()
SRC = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))

PAGES = [int(p) for p in sys.argv[1].split(",")] if len(sys.argv) > 1 else list(range(1, 26))
out: list[str] = []

with pdfplumber.open(SRC) as pdf:
    for n in PAGES:
        page = pdf.pages[n - 1]
        out.append(f"== page {n}  {page.width:.2f}x{page.height:.2f}")

        hs = []
        vs = []
        other = 0
        for ln in page.lines:
            w = abs(ln["x1"] - ln["x0"])
            h = abs(ln["bottom"] - ln["top"])
            if h <= 1.6 and w >= 30:
                hs.append((ln["top"], min(ln["x0"], ln["x1"]), max(ln["x0"], ln["x1"]), h))
            elif w <= 1.6 and h >= 12:
                vs.append((min(ln["x0"], ln["x1"]), ln["top"], ln["bottom"], w))
            else:
                other += 1
        for rc in page.rects:
            w = rc["x1"] - rc["x0"]
            h = rc["bottom"] - rc["top"]
            if h <= 2.0:
                hs.append((rc["top"], rc["x0"], rc["x1"], h))
            elif w <= 2.0:
                vs.append((rc["x0"], rc["top"], rc["bottom"], w))
            else:
                other += 1

        hs.sort()
        vs.sort()
        out.append(f"  H rules n={len(hs)}")
        for y, x0, x1, th in hs:
            out.append(f"    y={y:7.1f} x={x0:6.1f}..{x1:6.1f} w={x1 - x0:6.1f} th={th:.2f}")
        out.append(f"  V rules n={len(vs)}")
        for x, y0, y1, tw in vs:
            out.append(f"    x={x:7.1f} y={y0:6.1f}..{y1:6.1f} h={y1 - y0:6.1f} tw={tw:.2f}")
        if other:
            out.append(f"  non-rule drawings n={other} (curves={len(page.curves)})")

        out.append(f"  images n={len(page.images)}")
        for im in page.images:
            out.append(
                f"    bbox={im['x0']:.1f},{im['top']:.1f},{im['x1']:.1f},{im['bottom']:.1f} "
                f"px={im['srcsize'][0]}x{im['srcsize'][1]}"
            )

        groups: dict[int, list] = {}
        for ch in page.chars:
            groups.setdefault(round(ch["top"] / 2.2), []).append(ch)
        out.append("  lines")
        for key in sorted(groups):
            chs = sorted(groups[key], key=lambda c: c["x0"])
            text = "".join(c["text"] for c in chs)
            out.append(
                f"    y={min(c['top'] for c in chs):6.1f} x={chs[0]['x0']:6.1f}..{chs[-1]['x1']:6.1f} "
                f"sz={chs[0]['size']:.1f} | {text[:120]}"
            )

suffix = sys.argv[2] if len(sys.argv) > 2 else ""
dest = LANE / ".proxy" / f"{PID}-geo{suffix}.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print(dest)
