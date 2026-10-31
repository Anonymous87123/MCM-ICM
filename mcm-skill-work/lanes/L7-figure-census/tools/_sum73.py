"""Summary dumps for paper 73: regions, headings, captions, mentions, and the text measure."""

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2015-35532-1a9fa997"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))
CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}


def rn(page: int) -> str:
    return schema.page_text(PID, page)


lines: list[str] = []

lines.append(f"== layout  pages={LAYOUT['page_count']} regions={LAYOUT['region_total']}")
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        b = r["bbox"]
        c = CTXREG.get((pg["page"], i), {})
        lines.append(
            f"p{pg['page']:02d} r{i} {r.get('kind','?'):6s} "
            f"[{b[0]:6.1f},{b[1]:6.1f},{b[2]:6.1f},{b[3]:6.1f}] "
            f"w={b[2]-b[0]:6.1f} h={b[3]-b[1]:6.1f} "
            f"zone={c.get('page_zone','?'):8s} area={c.get('area_frac',0):.3f} "
            f"solo={c.get('solo_page','?')} :: {' / '.join(c.get('section_path', []))}"
        )

lines.append("")
lines.append("== headings")
for h in CTX["headings"]:
    lines.append(f"p{h.get('page')} num={h.get('number')!r} title={h.get('title')!r}")

lines.append("")
lines.append("== ctx captions")
for c in CTX["captions"]:
    lines.append(f"p{c.get('page')} r{c.get('region')} above={c.get('caption_above')!r} "
                 f"below={c.get('caption_below')!r} inside={c.get('text_inside')!r}")

lines.append("")
lines.append("== printed captions out of page_text")
for page in range(1, LAYOUT["page_count"] + 1):
    text = rn(page)
    for m in re.finditer(r"(Figure|FIGURE|Table|TABLE)\s*\d+\s*[:.]", text):
        start = m.start()
        chunk = text[start:start + 400]
        cut = chunk.find("\n")
        lines.append(f"p{page:02d} {chunk[:380]!r}")

lines.append("")
lines.append("== exhibit mentions")
for page in range(1, LAYOUT["page_count"] + 1):
    text = rn(page)
    for m in re.finditer(r"(?:Fig\.|Figure|Table|FIGURE|TABLE)\s*\d+", text):
        a = max(0, m.start() - 80)
        b = min(len(text), m.end() + 80)
        lines.append(f"p{page:02d} {text[a:b]!r}")

dest = PROXY / "p73-sum.txt"
dest.write_text("\n".join(lines), encoding="utf-8")
print(dest, len(lines))
