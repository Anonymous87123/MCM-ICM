"""Per-region geometry and text-line report for P-B-2015-38720-26d38781.

For every measured region: the region line, the captions printed on that page, the rule and fill
counts restricted to the region's own y band, and the region's text lines grouped into rows. Writes
`.proxy/<pid>-geo.txt` and prints its path so the file can be read in slices.
"""

import json
from pathlib import Path

import pdfplumber

LANE = Path(__file__).resolve().parents[1]
PID = "P-B-2015-38720-26d38781"
CTX = json.loads((LANE / ".proxy" / f"{PID}-ctx.json").read_text(encoding="utf-8"))
head = (LANE / ".proxy" / f"{PID}-read.txt").read_text(encoding="utf-8").splitlines()
SRC = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

out: list[str] = []
with pdfplumber.open(SRC) as pdf:
    for page_no in CTX["pages"]:
        page = pdf.pages[page_no - 1]
        regs = sorted((r for r in CTX["regions"] if r["page"] == page_no),
                      key=lambda r: (r["bbox"][1], r["bbox"][0]))
        caps = [c["text"] for c in CTX["captions"] if c["page"] == page_no]
        for i, reg in enumerate(regs, 1):
            x0, y0, x1, y1 = reg["bbox"]
            out.append(f"== p{page_no} r{i} bbox {x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f} "
                       f"area={reg['area_frac']} kind={reg.get('kind')} paths={reg.get('paths')} "
                       f"path={' / '.join(reg['section_path'])}")
            for c in caps:
                out.append(f"   cap {c[:100]}")
            hs, vs, fills = [], [], []
            for ln in page.lines:
                w = abs(ln["x1"] - ln["x0"])
                h = abs(ln["bottom"] - ln["top"])
                mid_y = (ln["top"] + ln["bottom"]) / 2
                if h <= 1.6 and w >= 20 and y0 - 2 <= mid_y <= y1 + 2:
                    hs.append((ln["top"], min(ln["x0"], ln["x1"]), max(ln["x0"], ln["x1"])))
                elif w <= 1.6 and h >= 8 and ln["top"] < y1 and ln["bottom"] > y0:
                    vs.append(round(min(ln["x0"], ln["x1"]), 1))
            for rc in page.rects:
                w = rc["x1"] - rc["x0"]
                h = rc["bottom"] - rc["top"]
                mid_y = (rc["top"] + rc["bottom"]) / 2
                if h <= 2.0 and w >= 20 and y0 - 2 <= mid_y <= y1 + 2:
                    hs.append((rc["top"], rc["x0"], rc["x1"]))
                elif w <= 2.0 and h >= 8 and rc["top"] < y1 and rc["bottom"] > y0:
                    vs.append(round(rc["x0"], 1))
                elif w >= 20 and h >= 5 and y0 - 2 <= mid_y <= y1 + 2:
                    fills.append((rc["top"], rc["x0"], rc["x1"], h,
                                  rc.get("non_stroking_color")))
            hs.sort()
            out.append(f"   H {len(hs)} V {len(vs)} fills {len(fills)}")
            for y, a, b in hs:
                out.append(f"     H y={y:7.1f} x={a:6.1f}..{b:6.1f} w={b - a:6.1f}")
            if vs:
                out.append(f"     V at x={sorted(set(vs))}")
            for f in fills[:10]:
                out.append(f"     fill y={f[0]:7.1f} x={f[1]:6.1f}..{f[2]:6.1f} h={f[3]:5.1f} "
                           f"colour={f[4]}")

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

dest = LANE / ".proxy" / "p77-geo.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print(dest, len(out), "lines")
