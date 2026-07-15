#!/usr/bin/env python3
"""Derive current-protocol compliance for every lifecycle-closed paper.

The report is a read-only view over progress and artifact directories. It never
updates lifecycle progress or treats a historical migration baseline as scope.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


PROTOCOL_STATUSES = (
    "current-validated",
    "partial",
    "absent",
    "correction-required",
)
ARTIFACT_KINDS = (
    "paper_cards",
    "language_units",
    "model_units",
    "learning_audits",
)


@dataclass
class ArtifactIndex:
    records: dict[str, dict[str, Any]] = field(default_factory=dict)
    paths: dict[str, Path] = field(default_factory=dict)
    duplicate_paper_ids: set[str] = field(default_factory=set)
    invalid_files: list[str] = field(default_factory=list)
    filename_id_mismatches: list[dict[str, str]] = field(default_factory=list)
    errors_by_paper_id: dict[str, list[str]] = field(default_factory=dict)

    @property
    def paper_ids(self) -> set[str]:
        return set(self.records)

    def add_error(self, paper_id: str, reason: str) -> None:
        self.errors_by_paper_id.setdefault(paper_id, []).append(reason)


def load_progress(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"invalid progress JSON at line {line_number}: {error.msg}"
            ) from error
        if not isinstance(value, dict):
            raise ValueError(f"progress line {line_number} must be an object")
        if not isinstance(value.get("paper_id"), str):
            raise ValueError(f"progress line {line_number} requires paper_id")
        rows.append(value)
    return rows


def load_artifact_index(directory: Path, kind: str) -> ArtifactIndex:
    index = ArtifactIndex()
    for path in sorted(directory.glob("*.json")):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            index.invalid_files.append(str(path))
            index.add_error(path.stem, f"{kind}:invalid-json-or-unreadable")
            continue
        if not isinstance(value, dict):
            index.invalid_files.append(str(path))
            index.add_error(path.stem, f"{kind}:record-not-object")
            continue
        paper_id = value.get("paper_id")
        if not isinstance(paper_id, str) or not paper_id:
            index.invalid_files.append(str(path))
            index.add_error(path.stem, f"{kind}:missing-paper-id")
            continue
        if path.stem != paper_id:
            index.filename_id_mismatches.append(
                {"file": str(path), "filename_id": path.stem, "record_id": paper_id}
            )
            index.add_error(paper_id, f"{kind}:filename-paper-id-mismatch")
            index.add_error(path.stem, f"{kind}:filename-paper-id-mismatch")
        if paper_id in index.records:
            index.duplicate_paper_ids.add(paper_id)
            index.add_error(paper_id, f"{kind}:duplicate-paper-id")
            continue
        index.records[paper_id] = value
        index.paths[paper_id] = path
    return index


def _is_string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and item for item in value)
    )


def _equation_count(model_record: dict[str, Any]) -> int | None:
    models = model_record.get("models")
    if not isinstance(models, list):
        return None
    total = 0
    for model in models:
        if not isinstance(model, dict):
            return None
        equations = model.get("governing_equations")
        if not isinstance(equations, list):
            return None
        total += len(equations)
    return total


def _linked_basename(link: Any) -> str | None:
    if not isinstance(link, dict) or not isinstance(link.get("path"), str):
        return None
    return Path(link["path"]).name


def _check_card_consistency(
    card: dict[str, Any],
    language: dict[str, Any] | None,
    language_path: Path | None,
    model: dict[str, Any] | None,
    model_path: Path | None,
) -> tuple[list[str], list[str]]:
    partial: list[str] = []
    correction: list[str] = []
    if card.get("review_status") != "validated":
        partial.append("paper-card:review-status-not-validated")
    links = card.get("protocol_v2_records")
    if not isinstance(links, dict):
        partial.append("card:protocol-links-missing")
        return partial, correction

    language_link = links.get("language")
    if not isinstance(language_link, dict):
        partial.append("card:language-link-missing")
    elif language is not None and language_path is not None:
        if _linked_basename(language_link) != language_path.name:
            correction.append("card:language-path-mismatch")
        if language_link.get("schema_version") != language.get("schema_version"):
            correction.append("card:language-schema-mismatch")
        units = language.get("units")
        if isinstance(units, list):
            if language_link.get("unit_count") != len(units):
                correction.append("card:language-unit-count-mismatch")
        else:
            correction.append("language:units-not-array")
        chapters = language.get("available_chapters")
        declared_chapters = language_link.get("chapters")
        if _is_string_list(chapters) and _is_string_list(declared_chapters):
            if set(chapters) != set(declared_chapters) or len(chapters) != len(
                declared_chapters
            ):
                correction.append("card:language-chapter-set-mismatch")
        else:
            correction.append("card:language-chapters-invalid")
        if language_link.get("review_status") != language.get("review_status"):
            correction.append("card:language-review-status-mismatch")

    model_link = links.get("models")
    if not isinstance(model_link, dict):
        partial.append("card:model-link-missing")
    elif model is not None and model_path is not None:
        if _linked_basename(model_link) != model_path.name:
            correction.append("card:model-path-mismatch")
        models = model.get("models")
        if isinstance(models, list):
            if model_link.get("model_count") != len(models):
                correction.append("card:model-count-mismatch")
        else:
            correction.append("model:models-not-array")
        equation_count = _equation_count(model)
        if equation_count is None:
            correction.append("model:equations-invalid")
        elif model_link.get("equation_count") != equation_count:
            correction.append("card:equation-count-mismatch")
        if model_link.get("review_status") != model.get("review_status"):
            correction.append("card:model-review-status-mismatch")
    return partial, correction


def _evaluate_closed_paper(
    paper_id: str,
    indexes: dict[str, ArtifactIndex],
    duplicate_progress_ids: set[str],
    semantic_errors_by_paper: dict[str, list[str]],
) -> dict[str, Any]:
    card = indexes["paper_cards"].records.get(paper_id)
    language = indexes["language_units"].records.get(paper_id)
    model = indexes["model_units"].records.get(paper_id)
    audit = indexes["learning_audits"].records.get(paper_id)
    present = {
        "paper_card": card is not None,
        "language": language is not None,
        "model": model is not None,
        "learning_audit": audit is not None,
    }
    partial: list[str] = []
    correction: list[str] = []

    if paper_id in duplicate_progress_ids:
        correction.append("progress:duplicate-paper-id")
    for kind, index in indexes.items():
        correction.extend(index.errors_by_paper_id.get(paper_id, []))

    if card is None:
        partial.append("paper-card:missing")
    if language is None:
        partial.append("language:missing")
    else:
        schema_version = language.get("schema_version")
        if schema_version != 3:
            partial.append(f"language:schema-version-{schema_version}")
        if language.get("review_status") != "validated":
            partial.append("language:review-status-not-validated")
        chapters = language.get("available_chapters")
        if schema_version == 3:
            if not _is_string_list(chapters) or len(chapters) != len(set(chapters)):
                correction.append("language:available-chapters-invalid")
            layouts = language.get("chapter_layouts")
            if not isinstance(layouts, list):
                correction.append("language:chapter-layouts-missing")
            elif _is_string_list(chapters):
                layout_chapters = [
                    layout.get("chapter")
                    for layout in layouts
                    if isinstance(layout, dict)
                    and isinstance(layout.get("chapter"), str)
                ]
                if len(layout_chapters) != len(layouts):
                    correction.append("language:chapter-layout-entry-invalid")
                elif len(layout_chapters) != len(set(layout_chapters)):
                    correction.append("language:duplicate-chapter-layout")
                elif set(layout_chapters) != set(chapters):
                    correction.append("language:chapter-layout-set-mismatch")
            units = language.get("units")
            if not isinstance(units, list):
                correction.append("language:units-not-array")

    if model is None:
        partial.append("model:missing")
    else:
        if model.get("schema_version") != 2:
            partial.append(f"model:schema-version-{model.get('schema_version')}")
        if model.get("review_status") != "validated":
            partial.append("model:review-status-not-validated")
        if model.get("schema_version") == 2 and not isinstance(
            model.get("models"), list
        ):
            correction.append("model:models-not-array")

    if audit is None:
        partial.append("learning-audit:missing")
    else:
        if audit.get("schema_version") != 1:
            partial.append(
                f"learning-audit:schema-version-{audit.get('schema_version')}"
            )
        if audit.get("review_status") != "validated":
            partial.append("learning-audit:review-status-not-validated")
        semantic_errors = semantic_errors_by_paper.get(paper_id, [])
        if semantic_errors:
            correction.append("learning-audit:semantic-validation-failed")

    if card is not None:
        card_partial, card_correction = _check_card_consistency(
            card,
            language,
            indexes["language_units"].paths.get(paper_id),
            model,
            indexes["model_units"].paths.get(paper_id),
        )
        partial.extend(card_partial)
        correction.extend(card_correction)

    if correction:
        protocol_status = "correction-required"
    elif not any(present.values()):
        protocol_status = "absent"
    elif partial:
        protocol_status = "partial"
    else:
        protocol_status = "current-validated"
    reasons = sorted(set(correction + partial))
    return {
        "paper_id": paper_id,
        "lifecycle_status": "closed",
        "protocol_status": protocol_status,
        "artifact_presence": present,
        "reasons": reasons,
        "semantic_validation_errors": semantic_errors_by_paper.get(paper_id, []),
    }


def derive_report(
    *,
    progress_path: Path,
    paper_cards_dir: Path,
    language_units_dir: Path,
    model_units_dir: Path,
    learning_audits_dir: Path,
    semantic_errors_by_paper: dict[str, list[str]] | None = None,
) -> dict[str, Any]:
    progress_rows = load_progress(progress_path)
    closed_rows = [row for row in progress_rows if row.get("status") == "closed"]
    closed_id_rows = [row["paper_id"] for row in closed_rows]
    closed_ids = set(closed_id_rows)
    progress_counts = Counter(row["paper_id"] for row in progress_rows)
    duplicate_progress_ids = {
        paper_id for paper_id, count in progress_counts.items() if count > 1
    }
    indexes = {
        "paper_cards": load_artifact_index(paper_cards_dir, "paper-card"),
        "language_units": load_artifact_index(language_units_dir, "language"),
        "model_units": load_artifact_index(model_units_dir, "model"),
        "learning_audits": load_artifact_index(
            learning_audits_dir, "learning-audit"
        ),
    }
    records = [
        _evaluate_closed_paper(
            paper_id,
            indexes,
            duplicate_progress_ids,
            semantic_errors_by_paper or {},
        )
        for paper_id in sorted(closed_ids)
    ]
    status_counts = {
        status: sum(record["protocol_status"] == status for record in records)
        for status in PROTOCOL_STATUSES
    }
    current_ids = [
        record["paper_id"]
        for record in records
        if record["protocol_status"] == "current-validated"
    ]
    migration_ids = [
        record["paper_id"]
        for record in records
        if record["protocol_status"] != "current-validated"
    ]
    artifact_only = {
        kind: sorted(index.paper_ids - closed_ids) for kind, index in indexes.items()
    }
    closed_without = {
        kind: sorted(closed_ids - index.paper_ids) for kind, index in indexes.items()
    }
    integrity = {
        "duplicate_progress_paper_ids": sorted(duplicate_progress_ids),
        "duplicate_artifact_paper_ids": {
            kind: sorted(index.duplicate_paper_ids)
            for kind, index in indexes.items()
        },
        "invalid_artifact_files": {
            kind: sorted(index.invalid_files) for kind, index in indexes.items()
        },
        "filename_id_mismatches": {
            kind: sorted(
                index.filename_id_mismatches,
                key=lambda item: (item["file"], item["record_id"]),
            )
            for kind, index in indexes.items()
        },
        "artifact_only_paper_ids": artifact_only,
        "closed_without_artifact_paper_ids": closed_without,
    }
    has_integrity_error = bool(duplicate_progress_ids) or any(
        index.duplicate_paper_ids
        or index.invalid_files
        or index.filename_id_mismatches
        for index in indexes.values()
    ) or any(artifact_only.values())
    if has_integrity_error or status_counts["correction-required"]:
        report_status = "correction-required"
    elif migration_ids:
        report_status = "partial"
    else:
        report_status = "current-validated"
    return {
        "schema_version": 1,
        "scope": "all unique papers whose progress status is closed",
        "report_status": report_status,
        "progress_closed_rows": len(closed_rows),
        "lifecycle_closed": len(closed_ids),
        "current_protocol_complete": len(current_ids),
        "status_counts": status_counts,
        "closed_paper_ids": sorted(closed_ids),
        "current_protocol_complete_paper_ids": current_ids,
        "migration_paper_ids": migration_ids,
        "records": records,
        "integrity": integrity,
    }


def load_manifest_index(path: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError(f"manifest line {line_number} must be an object")
        paper_id = row.get("paper_id")
        if not isinstance(paper_id, str):
            continue
        if paper_id in index:
            raise ValueError(f"duplicate manifest paper_id {paper_id}")
        index[paper_id] = row
    return index


def load_learning_validator() -> Any:
    path = Path(__file__).with_name("validate_learning_audit.py")
    spec = importlib.util.spec_from_file_location("protocol_learning_validator", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load learning validator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_audit


def semantic_audit_errors(
    *,
    closed_ids: set[str],
    paper_cards_dir: Path,
    language_units_dir: Path,
    model_units_dir: Path,
    learning_audits_dir: Path,
    observations_dir: Path,
    manifest_path: Path,
) -> dict[str, list[str]]:
    validate_audit = load_learning_validator()
    manifest = load_manifest_index(manifest_path)
    errors_by_paper: dict[str, list[str]] = {}
    for paper_id in sorted(closed_ids):
        paths = {
            "card": paper_cards_dir / f"{paper_id}.json",
            "language": language_units_dir / f"{paper_id}.json",
            "model": model_units_dir / f"{paper_id}.json",
            "audit": learning_audits_dir / f"{paper_id}.json",
            "observations": observations_dir / f"{paper_id}.jsonl",
        }
        if not all(path.is_file() for path in paths.values()) or paper_id not in manifest:
            continue
        try:
            errors = validate_audit(
                json.loads(paths["audit"].read_text(encoding="utf-8")),
                json.loads(paths["language"].read_text(encoding="utf-8")),
                json.loads(paths["model"].read_text(encoding="utf-8")),
                json.loads(paths["card"].read_text(encoding="utf-8")),
                [
                    json.loads(line)
                    for line in paths["observations"].read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ],
                manifest[paper_id],
            )
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors = [str(error)]
        if errors:
            errors_by_paper[paper_id] = errors
    return errors_by_paper


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--progress", type=Path, required=True)
    parser.add_argument("--paper-cards", type=Path, required=True)
    parser.add_argument("--language-units", type=Path, required=True)
    parser.add_argument("--model-units", type=Path, required=True)
    parser.add_argument("--learning-audits", type=Path, required=True)
    parser.add_argument("--observations", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        progress_rows = load_progress(args.progress)
        closed_ids = {
            row["paper_id"] for row in progress_rows if row.get("status") == "closed"
        }
        audit_errors = semantic_audit_errors(
            closed_ids=closed_ids,
            paper_cards_dir=args.paper_cards,
            language_units_dir=args.language_units,
            model_units_dir=args.model_units,
            learning_audits_dir=args.learning_audits,
            observations_dir=args.observations,
            manifest_path=args.manifest,
        )
        report = derive_report(
            progress_path=args.progress,
            paper_cards_dir=args.paper_cards,
            language_units_dir=args.language_units,
            model_units_dir=args.model_units,
            learning_audits_dir=args.learning_audits,
            semantic_errors_by_paper=audit_errors,
        )
        encoded = json.dumps(
            report, ensure_ascii=False, indent=2, sort_keys=True
        ) + "\n"
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
