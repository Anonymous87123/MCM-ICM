"""Refreeze merge/snapshot/paragraph-ledger.jsonl from the live artifacts ledger.

`tools/audit_merge.py` never reads `artifacts/paragraph-ledger.jsonl` directly: it
works on a frozen copy so its numbers stay reproducible while the encoding session
appends to the live file. Nothing refreshed that copy, so every number in
`merge/` silently drifted from the ledger. This is the refresh step.

Usage:
  python -I -X utf8 lanes/L1-f-structure/tools/freeze_ledger.py
  python -I -X utf8 lanes/L1-f-structure/tools/audit_merge.py
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
LIVE = ROOT / "artifacts" / "paragraph-ledger.jsonl"
SNAPSHOT = ROOT / "lanes" / "L1-f-structure" / "merge" / "snapshot" / "paragraph-ledger.jsonl"


def main() -> None:
    rows = []
    skipped = 0
    for line in LIVE.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if not text:
            continue
        try:
            json.loads(text)
        except json.JSONDecodeError:
            skipped += 1
            continue
        rows.append(text)

    payload = ("\n".join(rows) + "\n").encode("utf-8")
    staging = SNAPSHOT.with_suffix(".tmp")
    staging.write_bytes(payload)
    os.replace(staging, SNAPSHOT)

    digest = hashlib.sha256(SNAPSHOT.read_bytes()).hexdigest()
    print(f"rows {len(rows)} skipped_partial_or_invalid {skipped}")
    print(f"sha256 {digest}")
    print(f"wrote {SNAPSHOT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
