#!/usr/bin/env python3
"""Atomically update one paper in the study progress ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ALLOWED = {
    "status": {
        "discovered", "scope-verified", "integrity-checked", "text-extracted",
        "layout-inspected", "section-mapped", "deep-read", "paper-card-complete",
        "type-branch-updated", "post-update-validated", "closed", "needs-ocr",
        "corrupt", "classification-conflict", "duplicate-candidate",
        "missing-pages-suspected", "manual-equation-review", "manual-figure-review",
    },
    "extraction_status": {
        "pending", "text-extracted", "partial-text-review", "needs-ocr", "validated"
    },
    "paper_card_status": {"pending", "draft", "source-checked", "validated"},
    "branch_update_status": {"pending", "updated", "validated"},
    "validation_status": {"pending", "pass", "fail"},
}


def atomic_write(path: Path, content: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def load_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            value = json.loads(line)
            if not isinstance(value, dict):
                raise RuntimeError(f"line {line_number} is not an object")
            records.append(value)
    return records


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--progress", type=Path, required=True)
    parser.add_argument("--paper-id", required=True)
    for field in ALLOWED:
        parser.add_argument(f"--{field.replace('_', '-')}", choices=sorted(ALLOWED[field]))
    args = parser.parse_args(argv or sys.argv[1:])

    updates = {
        field: getattr(args, field)
        for field in ALLOWED
        if getattr(args, field) is not None
    }
    if not updates:
        raise SystemExit("at least one status update is required")

    records = load_records(args.progress)
    matched = [record for record in records if record.get("paper_id") == args.paper_id]
    if len(matched) != 1:
        raise SystemExit(f"expected one progress record for {args.paper_id}; found {len(matched)}")
    matched[0].update(updates)

    lines = "\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n"
    atomic_write(args.progress, lines)
    status_counts = dict(sorted(Counter(record["status"] for record in records).items()))
    summary = {
        "paper_count": len(records),
        "progress_sha256": hashlib.sha256(lines.encode("utf-8")).hexdigest(),
        "status_counts": status_counts,
        "updated_paper_id": args.paper_id,
        "updates": updates,
    }
    atomic_write(
        args.progress.with_name("progress-summary.json"),
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
