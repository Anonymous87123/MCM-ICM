from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from append_transaction import (
    load_history,
    validate_declared_artifacts,
    validate_history,
)


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2012-15171-ce229936"


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def history_line_count(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timestamp-utc", required=True)
    args = parser.parse_args()

    history = ROOT / "artifacts/transactions/history.jsonl"
    draft = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    compliance = ROOT / "artifacts/transactions/current-protocol-compliance.json"
    manifest = ROOT / "artifacts/corpus/manifest.jsonl"

    live_events = load_history(history)
    if any(event.get("paper_id") == PAPER_ID for event in live_events):
        raise SystemExit("Queue 96 already exists in live history; refusing duplicate append")
    before_count = history_line_count(history)

    common = (
        "scripts/append_transaction.py",
        "--draft",
        str(draft),
        "--artifact-root",
        ".",
        "--timestamp-utc",
        args.timestamp_utc,
    )
    run(*common, "--history", str(history), "--validate-only")

    with tempfile.NamedTemporaryFile(
        prefix=f"{PAPER_ID}-prospective-",
        suffix=".jsonl",
        delete=False,
    ) as handle:
        prospective = Path(handle.name)
    lock = Path(f"{prospective}.lock")
    try:
        shutil.copyfile(history, prospective)
        run(*common, "--history", str(prospective))
        run(
            "scripts/validate_language_priority_drift.py",
            "--history",
            str(prospective),
            "--observations",
            "artifacts/observations",
            "--window",
            "5",
        )
    finally:
        prospective.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)

    if history_line_count(history) != before_count:
        raise SystemExit("Live history changed during prospective validation")

    run(*common, "--history", str(history))
    after_append_count = history_line_count(history)
    if after_append_count != before_count + 1:
        raise SystemExit(
            f"Expected {before_count + 1} live events after append, got {after_append_count}"
        )

    run(
        "scripts/update_progress.py",
        "--progress",
        "artifacts/progress.jsonl",
        "--paper-id",
        PAPER_ID,
        "--status",
        "closed",
        "--extraction-status",
        "validated",
        "--paper-card-status",
        "validated",
        "--branch-update-status",
        "validated",
        "--validation-status",
        "pass",
    )
    run(
        "scripts/derive_protocol_compliance.py",
        "--progress",
        "artifacts/progress.jsonl",
        "--paper-cards",
        "artifacts/paper-cards",
        "--language-units",
        "artifacts/language-units",
        "--model-units",
        "artifacts/model-units",
        "--learning-audits",
        "artifacts/learning-audits",
        "--observations",
        "artifacts/observations",
        "--manifest",
        str(manifest),
        "--output",
        str(compliance),
    )
    run(
        "scripts/validate_language_priority_drift.py",
        "--history",
        str(history),
        "--observations",
        "artifacts/observations",
        "--window",
        "5",
    )

    final_events = load_history(history)
    history_errors = validate_history(final_events)
    artifact_errors = validate_declared_artifacts(final_events[-1], ROOT)
    if history_errors:
        raise SystemExit(f"History-chain validation failed: {history_errors}")
    if artifact_errors:
        raise SystemExit(f"Final artifact binding failed: {artifact_errors}")

    report = json.loads(compliance.read_text(encoding="utf-8"))
    records = [record for record in report["records"] if record["paper_id"] == PAPER_ID]
    if len(records) != 1 or records[0]["protocol_status"] != "current-validated":
        raise SystemExit("Queue 96 is not protocol-current-validated")
    if report["migration_paper_ids"]:
        raise SystemExit("Migration debt remains after Queue 96 closeout")

    event = final_events[-1]
    print(
        json.dumps(
            {
                "after_history_count": after_append_count,
                "before_history_count": before_count,
                "correction_required": report["status_counts"]["correction-required"],
                "current_validated": report["status_counts"]["current-validated"],
                "event_hash": event["event_hash"],
                "event_id": event["event_id"],
                "migration_debt": len(report["migration_paper_ids"]),
                "paper_id": event["paper_id"],
                "previous_event_hash": event["previous_event_hash"],
                "report_status": report["report_status"],
                "timestamp_utc": event["timestamp_utc"],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
