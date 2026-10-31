"""Per-region rule and text-line report for P-A-2015-40764-20552f34.

Rule lists are restricted to the region's own y band so a plot on the same page cannot leak
into a table's rules, and filled rects are reported separately because a grey body row is a
fill, not a rule.
"""

import json
from pathlib import Path

import pdfplumber

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2015-40764-20552f34"
head = (LANE / ".proxy" / f"{PID}-read.txt").read_text(encoding="utf-8").splitlines()
SRC = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

TABLE_REGIONS = {(3, 2), (5, 1), (6, 1), (7, 1), (7, 2), (8, 1), (9, 1), (10, 1), (11, 1),
                 (13, 1), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (15, 1), (15, 2),
                 (15, 3), (19, 1)}

out: list[str] = []
with pdfplumber.open(SRC) as pdf:
    for pg in LAYOUT["pages"]:
        page = pdf.pages[pg["page"] - 1]
        regs = sorted(pg["regions"], key=lambda r: (r["bbox"][1], r["bbox"][0]))
        for i, reg in enumerate(regs, 1):
            x0, y0, x1, y1 = reg["bbox"]
            detail = (pg["page"], i) in TABLE_REGIONS
            out.append(f"== p{pg['page']} r{i}  bbox {x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f} "
                       f"kind {reg.get('kind')} paths {reg.get('paths')}")

            hs, vs, fills = [], [], []
            for ln in page.lines:
                w = abs(ln["x1"] - ln["x0"])
                h = abs(ln["bottom"] - ln["top"])
                mid_y = (ln["top"] + ln["bottom"]) / 2
                if h <= 1.6 and w >= 20 and y0 - 2 <= mid_y <= y1 + 2:
                    hs.append((ln["top"], min(ln["x0"], ln["x1"]), max(ln["x0"], ln["x1"]), h))
                elif w <= 1.6 and h >= 8 and ln["top"] < y1 and ln["bottom"] > y0:
                    vs.append((min(ln["x0"], ln["x1"]), ln["top"], ln["bottom"], w))
            for rc in page.rects:
                w = rc["x1"] - rc["x0"]
                h = rc["bottom"] - rc["top"]
                mid_y = (rc["top"] + rc["bottom"]) / 2
                if h <= 2.0 and w >= 20 and y0 - 2 <= mid_y <= y1 + 2:
                    hs.append((rc["top"], rc["x0"], rc["x1"], h))
                elif w <= 2.0 and h >= 8 and rc["top"] < y1 and rc["bottom"] > y0:
                    vs.append((rc["x0"], rc["top"], rc["bottom"], w))
                elif w >= 20 and h >= 5 and y0 - 2 <= mid_y <= y1 + 2:
                    fills.append((rc["top"], rc["x0"], rc["x1"], h, rc.get("non_stroking_color")))
            hs.sort()
            vs.sort()
            if detail:
                out.append(f"   H rules {len(hs)}")
                for y, a, b, th in hs:
                    out.append(f"     y={y:7.1f} x={a:6.1f}..{b:6.1f} w={b - a:6.1f}")
                xs = sorted({round(v[0], 1) for v in vs})
                out.append(f"   V rules {len(vs)} at x={xs}")
            else:
                out.append(f"   H rules {len(hs)}  V rules {len(vs)}")
            out.append(f"   filled rects {len(fills)}")
            for f in fills[:12]:
                out.append(f"     y={f[0]:7.1f} x={f[1]:6.1f}..{f[2]:6.1f} h={f[3]:5.1f} "
                           f"fill={f[4]}")

            lines = [ln for ln in page.extract_text_lines()
                     if y0 - 2 <= ln["top"] <= y1 + 2 and ln["x1"] > x0 - 2 and ln["x0"] < x1 + 2]
            lines.sort(key=lambda ln: (round(ln["top"], 1), ln["x0"]))
            row: list[dict] = []
            for ln in lines:
                if row and ln["top"] - row[-1]["top"] > 4.0:
                    out.append("   row y=%6.1f | %s" % (
                        row[0]["top"], " || ".join(f"[{c['x0']:.0f}]{c['text']}" for c in row)))
                    row = []
                row.append(ln)
            if row:
                out.append("   row y=%6.1f | %s" % (
                    row[0]["top"], " || ".join(f"[{c['x0']:.0f}]{c['text']}" for c in row)))
        out.append("")

dest = LANE / ".proxy" / "p74-tables.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print(dest, len(out), "lines")
