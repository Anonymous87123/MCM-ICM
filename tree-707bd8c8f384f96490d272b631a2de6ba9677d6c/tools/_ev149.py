"""Evidence pass for P-B-2018-74316-1198d12d: captions, mentions, headings, region inventory."""

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PID = "P-B-2018-74316-1198d12d"

CTX = json.loads((LANE / ".proxy" / f"{PID}-ctx.json").read_text(encoding="utf-8"))
LAY = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
RAW = (LANE / ".proxy" / f"{PID}-pages.txt").read_text(encoding="utf-8")
PAGES: dict[int, str] = {}
for block in RAW.split("=== page ")[1:]:
    num, _, body = block.partition("\n")
    PAGES[int(num)] = body

out: list[str] = []
out.append("== captions")
for c in CTX["captions"]:
    out.append(f"p{c['page']:>2} [{c['kind']}] {c['text']!r}")

out.append("")
out.append("== mentions")
for m in CTX["mentions"]:
    out.append(f"{m}")

out.append("")
out.append("== headings")
for h in CTX["headings"]:
    out.append(f"p{h['page']:>2} {h['title']!r} [{h['kind']}] level={h.get('level')}")

out.append("")
out.append("== regions")
for pg in LAY["pages"]:
    if not pg["regions"]:
        continue
    out.append(f"-- page {pg['page']} ({pg['width']}x{pg['height']})")
    for i, r in enumerate(pg["regions"], 1):
        b = r["bbox"]
        w = b[2] - b[0]
        h = b[3] - b[1]
        frac = w * h / (pg["width"] * pg["height"])
        out.append(f"   r{i} bbox={[round(v, 1) for v in b]} {round(w)}x{round(h)} "
                   f"area={frac:.3f} kinds={sorted({e.get('kind') for e in r.get('elements', [])})}")

dest = LANE / ".proxy" / f"{PID}-evidence.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print(f"{dest} regions={sum(len(p['regions']) for p in LAY['pages'])}")
