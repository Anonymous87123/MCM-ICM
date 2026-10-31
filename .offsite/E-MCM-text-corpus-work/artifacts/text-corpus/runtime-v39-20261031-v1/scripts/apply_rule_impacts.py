#!/usr/bin/env python3
"""Apply one paper card's declared rule impacts without changing rule maturity."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path} line {line_number}: expected object")
            records.append(value)
    return records


def observation_paths(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(candidate for candidate in path.glob("*.jsonl") if candidate.is_file())
    raise ValueError(f"observation corpus does not exist: {path}")


def build_observation_index(path: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for observation_path in observation_paths(path):
        for record in load_jsonl(observation_path):
            observation_id = record.get("observation_id")
            if not isinstance(observation_id, str) or not observation_id:
                continue
            if observation_id in index:
                raise ValueError(f"duplicate observation_id {observation_id}")
            index[observation_id] = record
    return index


def apply_impacts(
    rules: list[dict[str, Any]],
    paper_card: dict[str, Any],
    observation_index: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    updated = copy.deepcopy(rules)
    rule_index = {rule.get("rule_id"): rule for rule in updated}
    paper_id = paper_card.get("paper_id")
    problem_type = paper_card.get("problem_type")
    impacts = paper_card.get("candidate_rule_impacts")
    if not isinstance(impacts, list):
        raise ValueError("paper card candidate_rule_impacts must be an array")

    changes: list[dict[str, Any]] = []
    changed_rule_ids: list[str] = []
    for impact in impacts:
        if not isinstance(impact, dict):
            raise ValueError("paper card impact must be an object")
        rule_id = impact.get("rule_id")
        rule = rule_index.get(rule_id)
        if rule is None:
            raise ValueError(f"unknown rule {rule_id}")
        if rule.get("problem_type") != problem_type:
            raise ValueError(f"{rule_id} type mismatch with paper card")
        evidence_ids = impact.get("evidence_ids")
        if not isinstance(evidence_ids, list) or not all(
            isinstance(evidence_id, str) and evidence_id for evidence_id in evidence_ids
        ):
            raise ValueError(f"{rule_id} impact evidence_ids must be a string array")

        added: list[str] = []
        rule_evidence = rule.get("evidence_ids")
        if not isinstance(rule_evidence, list):
            raise ValueError(f"{rule_id} evidence_ids must be an array")
        for evidence_id in evidence_ids:
            observation = observation_index.get(evidence_id)
            if observation is None:
                raise ValueError(f"{rule_id} references unknown evidence {evidence_id}")
            if observation.get("paper_id") != paper_id:
                raise ValueError(f"{evidence_id} paper mismatch with paper card")
            if observation.get("problem_type") != problem_type:
                raise ValueError(f"{evidence_id} type mismatch with paper card")
            if rule_id not in observation.get("candidate_rule_ids", []):
                raise ValueError(f"{evidence_id} does not nominate rule {rule_id}")
            if evidence_id not in rule_evidence:
                rule_evidence.append(evidence_id)
                added.append(evidence_id)
        if rule_id not in changed_rule_ids:
            changed_rule_ids.append(rule_id)
        changes.append(
            {
                "rule_id": rule_id,
                "declared_action": impact.get("action"),
                "added_evidence_ids": added,
                "lifecycle_unchanged": rule.get("lifecycle"),
            }
        )

    for rule_id in changed_rule_ids:
        rule = rule_index[rule_id]
        source_papers: list[str] = []
        for evidence_id in rule["evidence_ids"]:
            observation = observation_index.get(evidence_id)
            if observation is None:
                raise ValueError(f"{rule_id} has unresolved evidence {evidence_id}")
            evidence_paper = observation.get("paper_id")
            if isinstance(evidence_paper, str) and evidence_paper not in source_papers:
                source_papers.append(evidence_paper)
        rule["source_papers"] = source_papers
        rule["source_count"] = len(source_papers)
    return updated, changes


def encoded_jsonl(records: list[dict[str, Any]]) -> str:
    return "".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        for record in records
    )


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except OSError:
            pass
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rules", type=Path, required=True)
    parser.add_argument("--paper-card", type=Path, required=True)
    parser.add_argument("--observation-corpus", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--change-report", type=Path, required=True)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        rules = load_jsonl(args.rules)
        paper_card = load_json(args.paper_card)
        observations = build_observation_index(args.observation_corpus)
        updated, changes = apply_impacts(rules, paper_card, observations)
        output_text = encoded_jsonl(updated)
        report = {
            "paper_id": paper_card.get("paper_id"),
            "problem_type": paper_card.get("problem_type"),
            "rule_change_count": len(changes),
            "changes": changes,
            "output_sha256": hashlib.sha256(output_text.encode("utf-8")).hexdigest(),
            "status": "pass",
        }
        atomic_write(args.output, output_text)
        atomic_write(
            args.change_report,
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "fail", "errors": [str(error)]}, indent=2))
        return 1
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
