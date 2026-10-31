"""Probe the paper-77 context index: mentions, region roster, and heading roster."""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-B-2015-39173-b8260835"
C = json.loads((LANE / ".proxy" / f"{PID}-ctx.json").read_text(encoding="utf-8"))

print("== mentions")
for m in C["mentions"]:
    print(json.dumps(m, ensure_ascii=False))
print("== regions")
for r in C["regions"]:
    print(f"p{r['page']:>2} r{r['region']} area={r['area_frac']:.3f} kind={r.get('kind')} "
          f"zone={r.get('page_zone')} solo={r.get('solo_page')} paths={r.get('paths')} "
          f"path={' / '.join(r['section_path'])} bbox={[round(v, 1) for v in r['bbox']]}")
print("== headings")
for h in C["headings"]:
    print(f"p{h['page']:>2} {h.get('number')!s:>6} {h['label']}")
