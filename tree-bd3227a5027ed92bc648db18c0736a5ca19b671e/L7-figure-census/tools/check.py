"""Recount one recorded paper and confirm the geometry still reproduces.

Usage: python -I lanes/L7-figure-census/tools/check.py <pid> [<pid> ...]
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import fig_extract  # noqa: E402


def main(argv: list[str]) -> int:
    if not argv:
        raise SystemExit("usage: check.py <pid> ...")
    bad = 0
    for pid in argv:
        rec_path = LANE / "records" / f"{pid}.json"
        lay_path = LANE / "layout" / f"{pid}.json"
        if not rec_path.exists():
            print(f"{pid}: NO RECORD")
            bad += 1
            continue
        rec = json.loads(rec_path.read_text(encoding="utf-8"))
        lay = json.loads(lay_path.read_text(encoding="utf-8"))
        fresh = fig_extract.build(pid, lay["params"]["tol"])
        same = fresh["layout_sha256"] == lay["layout_sha256"]
        keys = {(p["page"], tuple(round(v, 1) for v in r["bbox"]))
                for p in lay["pages"] for r in p["regions"]}
        used = set()
        problems = []
        for it in rec["items"]:
            k = (it["page"], tuple(round(float(v), 1) for v in it["bbox"]))
            if k not in keys:
                problems.append(f"item p{it['page']} bbox not measured")
            if k in used:
                problems.append(f"item p{it['page']} duplicate")
            used.add(k)
        for t in rec.get("tables", []):
            k = (t["page"], tuple(round(float(v), 1) for v in t["bbox"]))
            if k not in keys:
                problems.append(f"table p{t['page']} bbox not measured")
            used.add(k)
        for ex in rec.get("excluded_regions", []):
            k = (ex["page"], tuple(round(float(v), 1) for v in ex["bbox"]))
            if k not in keys:
                problems.append(f"excluded p{ex['page']} bbox not measured")
            used.add(k)
        unaccounted = len(keys - used)
        print(f"{pid}: measured {len(keys)} figures {rec['figure_items']} "
              f"tables {rec['table_items']} excluded {rec['excluded_regions']} "
              f"unaccounted {unaccounted} layout {'identical' if same else 'CHANGED'}")
        for p in problems:
            print(f"  PROBLEM {p}")
        if problems or not same or unaccounted:
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
