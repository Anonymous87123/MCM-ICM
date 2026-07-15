#!/usr/bin/env python3
"""Select two deterministic calibration papers per A-F problem type."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path
from typing import Any


PROBE_PRIORITY = {
    "no-text": 0,
    "text-sparse": 1,
    "probe-error": 2,
    "text-rich": 3,
    "not-run": 4,
}
TYPES = "ABCDEF"
FIELDS = (
    "pilot_position",
    "selection_role",
    "paper_id",
    "problem_type",
    "year",
    "page_count",
    "text_probe_class",
    "relative_path",
    "selection_reason",
)


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def load_eligible(manifest: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with manifest.open("r", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            if record.get("eligible_paper"):
                records.append(record)
    return records


def select(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    for problem_type in TYPES:
        branch = [record for record in records if record["problem_type"] == problem_type]
        if not branch:
            raise RuntimeError(f"no eligible papers for type {problem_type}")
        years = sorted({record["year"] for record in branch})
        oldest_year, newest_year = years[0], years[-1]
        oldest = min(
            (record for record in branch if record["year"] == oldest_year),
            key=lambda record: (record["relative_path"].casefold(), record["sha256"]),
        )
        newest = min(
            (record for record in branch if record["year"] == newest_year),
            key=lambda record: (
                PROBE_PRIORITY.get(record["text_probe_class"], 99),
                record["relative_path"].casefold(),
                record["sha256"],
            ),
        )
        selected.append(
            {
                **oldest,
                "selection_reason": "earliest-year-first-path",
                "selection_role": "historical-anchor",
            }
        )
        selected.append(
            {
                **newest,
                "selection_reason": "newest-year-lowest-text-probe-then-first-path",
                "selection_role": "recent-risk-anchor",
            }
        )
    for index, record in enumerate(selected, start=1):
        record["pilot_position"] = index
    return selected


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv or sys.argv[1:])

    selected = select(load_eligible(args.manifest))
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with temporary.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(selected)
    os.replace(temporary, args.output)

    summary = {
        "paper_count": len(selected),
        "paper_ids": [record["paper_id"] for record in selected],
        "types": {problem_type: 2 for problem_type in TYPES},
    }
    atomic_write(
        args.output.with_name("pilot-summary.json"),
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
