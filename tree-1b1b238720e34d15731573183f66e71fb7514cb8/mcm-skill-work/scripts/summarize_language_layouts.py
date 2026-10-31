#!/usr/bin/env python3
"""Aggregate validated language schema v3 chapter-layout distributions."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


METRICS = {
    "word_count": "word",
    "sentence_count": "sentence",
    "paragraph_count": "paragraph",
    "page_fraction": "page-fraction",
}


def summarize_records(
    records: list[dict[str, Any]],
    problem_type: str,
) -> list[dict[str, Any]]:
    eligible = [
        record
        for record in records
        if record.get("schema_version") == 3
        and record.get("problem_type") == problem_type
    ]
    paper_ids = [record.get("paper_id") for record in eligible]
    if len(paper_ids) != len(set(paper_ids)):
        raise ValueError("duplicate paper_id in schema v3 language records")

    groups: dict[tuple[str, str], list[tuple[str, str, float]]] = defaultdict(list)
    for record in eligible:
        paper_id = record.get("paper_id")
        year = record.get("year")
        if not isinstance(paper_id, str) or not isinstance(year, str):
            raise ValueError("schema v3 language record requires paper_id and year")
        for layout in record.get("chapter_layouts", []):
            if not isinstance(layout, dict) or not isinstance(layout.get("chapter"), str):
                continue
            chapter = layout["chapter"]
            for field, unit in METRICS.items():
                value = layout.get(field)
                if isinstance(value, (int, float)):
                    groups[(chapter, unit)].append((paper_id, year, value))

    summaries = []
    for (chapter, unit), samples in sorted(groups.items()):
        if len(samples) < 2:
            continue
        values = [sample[2] for sample in samples]
        q1, _, q3 = statistics.quantiles(values, n=4, method="inclusive")
        years = [sample[1] for sample in samples]
        summaries.append(
            {
                "chapter": chapter,
                "unit": unit,
                "measurement_status": "provisional",
                "sample_papers": [sample[0] for sample in samples],
                "sample_size": len(samples),
                "observed_range": {
                    "minimum": min(values),
                    "maximum": max(values),
                },
                "median": statistics.median(values),
                "quartiles": {"q1": q1, "q3": q3, "iqr": q3 - q1},
                "era": {"start_year": min(years), "end_year": max(years)},
                "recommended_use": (
                    "Treat as an observed schema-v3 distribution, not a quota; "
                    "preserve rhetorical completeness and report the sample boundary."
                ),
            }
        )
    return summaries


def load_records(path: Path) -> list[dict[str, Any]]:
    records = []
    for candidate in sorted(path.glob("*.json")):
        value = json.loads(candidate.read_text(encoding="utf-8"))
        if isinstance(value, dict):
            records.append(value)
    return records


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language-units", type=Path, required=True)
    parser.add_argument("--problem-type", choices=list("ABCDEF"), required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        result = {
            "problem_type": args.problem_type,
            "layout_profiles": summarize_records(
                load_records(args.language_units), args.problem_type
            ),
        }
        encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(encoded, encoding="utf-8")
        else:
            print(encoded, end="")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
