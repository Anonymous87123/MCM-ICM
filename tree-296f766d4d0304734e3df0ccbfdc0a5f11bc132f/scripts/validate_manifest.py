#!/usr/bin/env python3
"""Validate manifest structure, queue consistency, and optional source hashes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


DOCUMENT_ID_RE = re.compile(r"^D-[a-f0-9]{12}$")
CONTENT_ID_RE = re.compile(r"^C-[a-f0-9]{12}$")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
PAPER_ID_RE = re.compile(r"^P-[A-F]-(?:19|20)\d{2}-[a-z0-9-]+-[a-f0-9]{8}$")
TYPE_SET = frozenset("ABCDEF")
ELIGIBLE_ROLES = frozenset({"award-paper-primary", "award-paper-finalist"})


def load_builder(script_path: Path):
    spec = importlib.util.spec_from_file_location("manifest_builder", script_path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import builder: {script_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def load_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                value = json.loads(line)
            except json.JSONDecodeError as error:
                errors.append(f"line {line_number}: invalid JSON: {error}")
                continue
            if not isinstance(value, dict):
                errors.append(f"line {line_number}: record is not an object")
                continue
            records.append(value)
    return records, errors


def add_duplicate_errors(
    errors: list[str], records: list[dict[str, Any]], key: str, label: str
) -> None:
    counts = Counter(record.get(key) for record in records)
    duplicates = sorted(str(value) for value, count in counts.items() if count > 1)
    if duplicates:
        errors.append(f"duplicate {label}: {', '.join(duplicates[:20])}")


def validate_record(record: dict[str, Any], line_number: int) -> list[str]:
    prefix = f"line {line_number}"
    errors: list[str] = []
    required = (
        "record_version",
        "document_id",
        "content_id",
        "relative_path",
        "file_size_bytes",
        "sha256",
        "problem_type",
        "classification_status",
        "document_role",
        "eligible_paper",
        "paper_id",
        "pdfinfo_status",
        "text_probe_class",
    )
    missing = [key for key in required if key not in record]
    if missing:
        errors.append(f"{prefix}: missing fields: {', '.join(missing)}")
        return errors

    if record["record_version"] != 1:
        errors.append(f"{prefix}: unsupported record_version")
    if not isinstance(record["document_id"], str) or not DOCUMENT_ID_RE.fullmatch(record["document_id"]):
        errors.append(f"{prefix}: invalid document_id")
    if not isinstance(record["content_id"], str) or not CONTENT_ID_RE.fullmatch(record["content_id"]):
        errors.append(f"{prefix}: invalid content_id")
    if not isinstance(record["sha256"], str) or not SHA256_RE.fullmatch(record["sha256"]):
        errors.append(f"{prefix}: invalid sha256")
    elif record["content_id"] != f"C-{record['sha256'][:12]}":
        errors.append(f"{prefix}: content_id does not match sha256")
    if not isinstance(record["relative_path"], str) or not record["relative_path"]:
        errors.append(f"{prefix}: invalid relative_path")
    if not isinstance(record["file_size_bytes"], int) or record["file_size_bytes"] < 0:
        errors.append(f"{prefix}: invalid file_size_bytes")

    if record["eligible_paper"]:
        if record["problem_type"] not in TYPE_SET:
            errors.append(f"{prefix}: eligible paper has invalid type")
        if record["document_role"] not in ELIGIBLE_ROLES:
            errors.append(f"{prefix}: eligible paper has invalid role")
        if record.get("award_status") not in {"outstanding", "finalist"}:
            errors.append(f"{prefix}: eligible paper has invalid award status")
        if not isinstance(record["paper_id"], str) or not PAPER_ID_RE.fullmatch(record["paper_id"]):
            errors.append(f"{prefix}: eligible paper has invalid paper_id")
        elif not record["paper_id"].startswith(f"P-{record['problem_type']}-{record['year']}-"):
            errors.append(f"{prefix}: paper_id type/year mismatch")
    elif record["paper_id"] is not None:
        errors.append(f"{prefix}: ineligible record has paper_id")
    return errors


def expected_queue(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        (record for record in records if record["eligible_paper"]),
        key=lambda record: (
            record["problem_type"],
            record["year"] or "9999",
            record["relative_path"].casefold(),
            record["sha256"],
        ),
    )


def validate_queue(queue_path: Path, expected: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    with queue_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != len(expected):
        errors.append(f"queue row count {len(rows)} != expected {len(expected)}")
        return errors
    for index, (row, record) in enumerate(zip(rows, expected), start=1):
        if row.get("queue_position") != str(index):
            errors.append(f"queue row {index}: invalid position")
        if row.get("paper_id") != record["paper_id"]:
            errors.append(f"queue row {index}: paper_id/order mismatch")
        if row.get("relative_path") != record["relative_path"]:
            errors.append(f"queue row {index}: relative_path mismatch")
    return errors


def validate_source(
    source_root: Path, records: list[dict[str, Any]], verify_hashes: bool
) -> list[str]:
    errors: list[str] = []
    for record in records:
        path = source_root.joinpath(*record["relative_path"].split("/"))
        if not path.is_file():
            errors.append(f"missing source file: {record['relative_path']}")
            continue
        if path.stat().st_size != record["file_size_bytes"]:
            errors.append(f"source size changed: {record['relative_path']}")
        if verify_hashes and sha256_file(path) != record["sha256"]:
            errors.append(f"source hash changed: {record['relative_path']}")
    return errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--verify-source-hashes", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    records, errors = load_jsonl(args.manifest)
    for index, record in enumerate(records, start=1):
        errors.extend(validate_record(record, index))

    add_duplicate_errors(errors, records, "document_id", "document_id")
    add_duplicate_errors(errors, records, "relative_path", "relative_path")
    eligible = [record for record in records if record.get("eligible_paper")]
    add_duplicate_errors(errors, eligible, "paper_id", "paper_id")
    add_duplicate_errors(errors, eligible, "sha256", "eligible paper content hash")

    expected = expected_queue(records)
    errors.extend(validate_queue(args.queue, expected))

    builder = load_builder(Path(__file__).with_name("build_manifest.py"))
    calculated_summary = builder.build_summary(records)
    with args.summary.open("r", encoding="utf-8") as handle:
        stored_summary = json.load(handle)
    if calculated_summary != stored_summary:
        errors.append("stored summary does not match manifest")

    if args.source:
        errors.extend(
            validate_source(args.source.resolve(), records, args.verify_source_hashes)
        )
    elif args.verify_source_hashes:
        errors.append("--verify-source-hashes requires --source")

    report = {
        "eligible_paper_count": len(eligible),
        "error_count": len(errors),
        "errors": errors,
        "record_count": len(records),
        "source_hashes_verified": bool(args.source and args.verify_source_hashes),
        "status": "pass" if not errors else "fail",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
