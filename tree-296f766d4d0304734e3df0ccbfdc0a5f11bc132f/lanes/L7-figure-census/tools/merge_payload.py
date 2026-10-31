"""Merge coder row files into one payload for record.py.

Rows are visual judgments returned by the crop readers; this script only joins them,
resolves (page, region) to the measured bbox, and splits figures from tables. It never
changes a family.

Usage:
  python -I lanes/L7-figure-census/tools/merge_payload.py <pid> .proxy/<pid>-rows-*.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
LAYOUT = LANE / "layout"
PROXY = LANE / ".proxy"

ITEM_KEYS = {"page", "region", "family", "confidence", "panel_count", "table",
             "caption_verbatim", "caption_source", "excluded", "other_note", "note"}


def norm_caption_source(row: dict) -> str:
    """Readers describe provenance in prose; record.py wants three values."""
    raw = str(row.get("caption_source") or "").lower()
    if "typed" in raw:
        return "typed-from-crop"
    if "text-layer" in raw or "text layer" in raw or "page text" in raw:
        return "text-layer"
    return "text-layer" if (row.get("caption_verbatim") or "").strip() else "none"


def main(argv: list[str]) -> int:
    pid, files = argv[0], [a for a in argv[1:] if not a.startswith("--")]
    remap: dict[tuple[int, int], int] = {}
    for arg in argv:
        if arg.startswith("--remap"):
            spec = arg.split("=", 1)[1] if "=" in arg else ""
            for part in spec.split(","):
                if not part.strip():
                    continue
                page, rest = part.split(":")
                old, new = rest.split("=")
                remap[(int(page), int(old))] = int(new)
    lay = json.loads((LAYOUT / f"{pid}.json").read_text(encoding="utf-8"))
    index = {(pg["page"], n): r
             for pg in lay["pages"] for n, r in enumerate(pg["regions"], 1)}

    rows: list[dict] = []
    for f in files:
        raw = json.loads(Path(f).read_text(encoding="utf-8"))
        if isinstance(raw, dict):
            raw = raw.get("rows", [])
        rows.extend(raw)

    items, tables, excluded, used = [], [], [], set()
    problems = []
    for row in rows:
        raw_key = (int(row["page"]), int(row["region"]))
        key = (raw_key[0], remap.get(raw_key, raw_key[1]))
        if key not in index:
            problems.append(f"no measured region at page {key[0]} r{key[1]}")
            continue
        if key in used:
            problems.append(f"page {key[0]} r{key[1]} returned twice")
            continue
        used.add(key)
        reg = index[key]
        base = {"page": key[0], "bbox": reg["bbox"], "kind": reg["kind"],
                "region": f"r{key[1]}"}
        if row.get("excluded"):
            excluded.append({**base, "reason": row["excluded"],
                             "note": row.get("note", "")})
            continue
        if row.get("table"):
            tables.append({**base, "caption_verbatim": row.get("caption_verbatim", ""),
                           "note": row.get("note", "")})
            continue
        items.append({**base,
                      "family": row["family"],
                      "confidence": row["confidence"],
                      "panel_count": int(row.get("panel_count", 1)),
                      "is_panel_of": row.get("is_panel_of"),
                      "caption_verbatim": row.get("caption_verbatim", ""),
                      "caption_source": norm_caption_source(row),
                      "other_note": row.get("other_note"),
                      "note": row.get("note", "")})

    missing = sorted(set(index) - used)
    unknown = sorted({k for k in rows[0].keys() if k not in ITEM_KEYS}) if rows else []
    payload = {"paper": pid, "layout_sha256": lay["layout_sha256"],
               "items": items, "tables": tables, "excluded_regions": excluded,
               "note": ""}
    out = PROXY / f"{pid}-payload.json"
    out.write_text(json.dumps(payload, indent=1, sort_keys=True), encoding="utf-8")
    print(f"{pid}: rows={len(rows)} figures={len(items)} tables={len(tables)} "
          f"excluded={len(excluded)} missing_regions={len(missing)} extra_keys={unknown}")
    for p in problems:
        print(f"  PROBLEM {p}")
    if missing:
        print("  missing: " + ", ".join(f"p{p}r{r}" for p, r in missing))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
