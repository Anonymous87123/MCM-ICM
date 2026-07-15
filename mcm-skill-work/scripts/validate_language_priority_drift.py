#!/usr/bin/env python3
"""Validate rolling language priority without weakening model or visual retention."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


DIMENSIONS = (
    "language", "modeling", "logic", "visualization", "verification",
    "data", "assumption", "result", "weakness", "other",
)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"expected object at {path}:{line_number}")
        records.append(value)
    return records


def is_substantive_learning_event(event: dict[str, Any]) -> bool:
    if event.get("history_completeness") != "native":
        return False
    if not isinstance(event.get("paper_id"), str):
        return False
    if event.get("event_type") == "paper-closed":
        return True
    if event.get("event_type") != "paper-corrected":
        return False
    after = event.get("after")
    return (
        isinstance(after, dict)
        and isinstance(after.get("language_unit_count"), int)
        and after["language_unit_count"] > 0
        and isinstance(after.get("model_count"), int)
        and isinstance(after.get("important_visual_count"), int)
    )


def rolling_paper_events(
    history: list[dict[str, Any]], window: int
) -> list[dict[str, Any]]:
    """Return latest distinct native learning events, skipping metadata corrections."""
    selected: list[dict[str, Any]] = []
    for event in history:
        if not is_substantive_learning_event(event):
            continue
        paper_id = event["paper_id"]
        selected = [item for item in selected if item.get("paper_id") != paper_id]
        selected.append(event)
    return selected[-window:]


def rolling_paper_ids(history: list[dict[str, Any]], window: int) -> list[str]:
    """Compatibility helper for callers that only need selected paper IDs."""
    return [str(event["paper_id"]) for event in rolling_paper_events(history, window)]


def validate_window(
    history: list[dict[str, Any]], observations_dir: Path, window: int = 5
) -> dict[str, Any]:
    selected_events = rolling_paper_events(history, window)
    paper_ids = [str(event["paper_id"]) for event in selected_events]
    errors: list[str] = []
    if len(paper_ids) < window:
        errors.append(f"requires {window} distinct native substantive learning events; found {len(paper_ids)}")
    counts: Counter[str] = Counter()
    per_paper: dict[str, dict[str, int]] = {}
    count_basis: dict[str, str] = {}
    for event in selected_events:
        paper_id = str(event["paper_id"])
        path = observations_dir / f"{paper_id}.jsonl"
        if not path.is_file():
            errors.append(f"missing observations for {paper_id}")
            continue
        paper_counts = Counter(
            item.get("dimension") for item in load_jsonl(path)
        )
        unknown = sorted(set(paper_counts) - set(DIMENSIONS))
        if unknown:
            errors.append(f"{paper_id} has unknown dimensions: {', '.join(unknown)}")
        after = event.get("after")
        if isinstance(after, dict) and isinstance(after.get("language_unit_count"), int):
            paper_counts["language"] = after["language_unit_count"]
            paper_counts["modeling"] = max(
                int(after.get("model_count", 0)),
                int(after.get("equation_count", 0)),
            )
            paper_counts["visualization"] = int(after.get("important_visual_count", 0))
            count_basis[paper_id] = (
                "mixed:frozen-language-model-visual+live-observations"
            )
        else:
            count_basis[paper_id] = "legacy-observation-counts"
        counts.update(paper_counts)
        per_paper[paper_id] = {dimension: paper_counts[dimension] for dimension in DIMENSIONS}

    normalized = {dimension: counts[dimension] for dimension in DIMENSIONS}
    nonlanguage_max = max(
        (count for dimension, count in normalized.items() if dimension != "language"),
        default=0,
    )
    if normalized["language"] <= nonlanguage_max:
        errors.append("rolling language observations are not the strictly largest evidence dimension")
    if normalized["weakness"] >= normalized["language"]:
        errors.append("rolling weakness observations are not a strict minority of language observations")
    if normalized["modeling"] == 0:
        errors.append("rolling window lost formula-level modeling evidence")
    if normalized["visualization"] == 0:
        errors.append("rolling window lost visualization evidence")
    return {
        "schema_version": 1,
        "window_size": window,
        "paper_ids": paper_ids,
        "event_ids": [event.get("event_id") for event in selected_events],
        "count_basis": count_basis,
        "dimension_counts": normalized,
        "per_paper_counts": per_paper,
        "assertions": {
            "language_is_strictly_largest": normalized["language"] > nonlanguage_max,
            "weakness_is_strict_minority_of_language": normalized["weakness"] < normalized["language"],
            "modeling_retained": normalized["modeling"] > 0,
            "visualization_retained": normalized["visualization"] > 0,
        },
        "error_count": len(errors),
        "errors": errors,
        "status": "pass" if not errors else "fail",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", type=Path, required=True)
    parser.add_argument("--observations", type=Path, required=True)
    parser.add_argument("--window", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv or None)
    try:
        if args.window < 1:
            raise ValueError("window must be positive")
        report = validate_window(load_jsonl(args.history), args.observations, args.window)
        encoded = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(encoded, encoding="utf-8")
        else:
            print(encoded, end="")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
