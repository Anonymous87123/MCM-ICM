"""Coverage report: how much of the 435-paper queue is measured and recorded.

Usage: python -I lanes/L7-figure-census/tools/coverage.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
QUEUE = LANE / "queue.txt"
LAYOUT = LANE / "layout"
RECORDS = LANE / "records"


def main() -> int:
    queue = [line.split()[1] for line in QUEUE.read_text(encoding="utf-8").splitlines()
             if line.strip()]
    measured = {p.stem for p in LAYOUT.glob("*.json")}
    recorded = list(RECORDS.glob("*.json"))

    families: Counter[str] = Counter()
    figures = tables = 0
    for path in recorded:
        rec = json.loads(path.read_text(encoding="utf-8"))
        families.update(rec.get("family_counts", {}))
        figures += rec.get("figure_items", 0)
        tables += rec.get("table_items", 0)

    print(f"queue {len(queue)}  measured {len(measured)}  recorded {len(recorded)}")
    print(f"figures {figures}  tables {tables}")
    total = sum(families.values())
    if total:
        for fam, n in families.most_common():
            print(f"  {fam:24s} {n:4d}  {100 * n / total:5.1f}%")
    todo = [p for p in queue if p not in {q.stem for q in RECORDS.glob('*.json')}]
    print(f"next {todo[0] if todo else 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
