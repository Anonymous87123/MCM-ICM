#!/usr/bin/env python3
"""Initialize a deterministic paper progress ledger from the eligible queue."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
from pathlib import Path


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv or sys.argv[1:])

    with args.queue.open("r", encoding="utf-8-sig", newline="") as handle:
        queue = list(csv.DictReader(handle))
    records = []
    paper_ids: set[str] = set()
    for expected_position, row in enumerate(queue, start=1):
        if row["paper_id"] in paper_ids:
            raise SystemExit(f"duplicate paper_id: {row['paper_id']}")
        if row["queue_position"] != str(expected_position):
            raise SystemExit(f"invalid queue position at row {expected_position}")
        paper_ids.add(row["paper_id"])
        records.append(
            {
                "branch_update_status": "pending",
                "extraction_status": "pending",
                "paper_card_status": "pending",
                "paper_id": row["paper_id"],
                "problem_type": row["problem_type"],
                "progress_version": 1,
                "queue_position": expected_position,
                "source_relative_path": row["relative_path"],
                "status": "discovered",
                "validation_status": "pending",
                "year": row["year"],
            }
        )
    lines = "\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n"
    atomic_write(args.output, lines)
    summary = {
        "paper_count": len(records),
        "progress_sha256": hashlib.sha256(lines.encode("utf-8")).hexdigest(),
        "status_counts": {"discovered": len(records)},
    }
    atomic_write(
        args.output.with_name("progress-summary.json"),
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
