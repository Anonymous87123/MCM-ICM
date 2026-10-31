"""Guard the merge audit's reproducibility contract.

`audit_merge.py` measured a frozen snapshot but recorded the hash of the live
ledger, so two runs never produced identical output and every number in
`merge/` drifted silently. The fix is one line (`sha(SNAP)`); these tests fail
if it is reverted or if `metrics.json` stops describing the snapshot on disk.
"""

from __future__ import annotations

import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
LANE = ROOT / "lanes" / "L1-f-structure"
SNAP = LANE / "merge" / "snapshot" / "paragraph-ledger.jsonl"
AUDIT = LANE / "tools" / "audit_merge.py"


def test_metrics_describes_snapshot_on_disk() -> None:
    metrics = json.loads((LANE / "merge" / "metrics.json").read_text(encoding="utf-8"))
    recorded = metrics["inputs_sha256"]["paragraph-ledger.jsonl"]
    actual = hashlib.sha256(SNAP.read_bytes()).hexdigest()
    assert recorded == actual


def test_audit_hashes_the_snapshot_not_the_live_ledger() -> None:
    row = [l for l in AUDIT.read_text(encoding="utf-8").splitlines()
           if l.strip().startswith('"paragraph-ledger.jsonl"')]
    assert len(row) == 1, row
    assert "sha(SNAP)" in row[0], row[0]
