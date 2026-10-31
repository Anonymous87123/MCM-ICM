#!/usr/bin/env python3
"""Build a deterministic manifest and A-F paper queues for the MCM corpus."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


RECORD_VERSION = 1
TYPE_SET = frozenset("ABCDEF")
YEAR_RE = re.compile(r"(?:19|20)\d{2}")
PRIMARY_TYPE_FOLDER_RE = re.compile(
    r"^(?:([A-F])|([A-F])\u9898\d+\u7bc7|(?:MCM|ICM)\d{4}([A-F]))$",
    re.IGNORECASE,
)
LEADING_TYPE_RE = re.compile(
    r"^([A-F])(?:[-_\s]|\d{4,}|\u7c7b)", re.IGNORECASE
)
NAMED_TYPE_RE = re.compile(
    r"(?:MCM|ICM)[-_\s]?\d{4}[-_\s]?([A-F])|Problem[-_\s]?([A-F])",
    re.IGNORECASE,
)
TEAM_TOKEN_RE = re.compile(r"\d{4,}")

OTHER_AWARD_FOLDER = "\u5176\u4ed6\u5956\u9879"
TRIAGE_FOLDER_FRAGMENT = "\u521d\u8bc4\u6807\u51c6"

DATA_EXTENSIONS = {".csv", ".xlsx", ".xls", ".txt", ".mat", ".zip"}
CODE_EXTENSIONS = {".m", ".py", ".r", ".jl", ".ipynb", ".tex"}
DOCUMENT_EXTENSIONS = {".doc", ".docx", ".png", ".jpg", ".jpeg"}

QUEUE_FIELDS = (
    "queue_position",
    "paper_id",
    "problem_type",
    "year",
    "award_status",
    "relative_path",
    "sha256",
    "page_count",
    "text_probe_class",
    "text_probe_chars",
    "file_size_bytes",
)


def nfc(value: str) -> str:
    return unicodedata.normalize("NFC", value)


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def extract_year(parts: tuple[str, ...]) -> str | None:
    for part in parts:
        match = YEAR_RE.search(part)
        if match:
            return match.group(0)
    return None


def primary_folder_type(folder: str) -> str | None:
    match = PRIMARY_TYPE_FOLDER_RE.fullmatch(nfc(folder))
    if not match:
        return None
    for value in match.groups():
        if value:
            return value.upper()
    return None


def type_signals(relative_path: Path) -> list[dict[str, str]]:
    signals: list[dict[str, str]] = []
    parts = tuple(nfc(part) for part in relative_path.parts)
    for index, folder in enumerate(parts[:-1]):
        problem_type = primary_folder_type(folder)
        if problem_type:
            signals.append(
                {
                    "type": problem_type,
                    "source": "parent-folder",
                    "value": folder,
                    "part_index": str(index),
                }
            )

    stem = nfc(relative_path.stem)
    leading = LEADING_TYPE_RE.search(stem)
    if leading:
        signals.append(
            {
                "type": leading.group(1).upper(),
                "source": "filename-prefix",
                "value": leading.group(0),
                "part_index": str(len(parts) - 1),
            }
        )

    for match in NAMED_TYPE_RE.finditer(stem):
        value = next(group for group in match.groups() if group)
        signals.append(
            {
                "type": value.upper(),
                "source": "filename-pattern",
                "value": match.group(0),
                "part_index": str(len(parts) - 1),
            }
        )

    unique: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for signal in signals:
        key = (signal["type"], signal["source"], signal["value"])
        if key not in seen:
            unique.append(signal)
            seen.add(key)
    return unique


def award_status(relative_path: Path, primary_folder: bool) -> tuple[str | None, str | None]:
    name = nfc(relative_path.name).casefold()
    if "finalist" in name:
        return "finalist", "filename-finalist"
    if "outstanding" in name or "o\u5956" in name:
        return "outstanding", "filename-outstanding"
    if "meritorious" in name:
        return "meritorious", "filename-meritorious"
    if "honorable" in name:
        return "honorable", "filename-honorable"
    if "successful" in name:
        return "successful", "filename-successful"
    if primary_folder:
        return "outstanding", "primary-type-folder"
    return None, None


def has_any_fragment(values: Iterable[str], fragments: Iterable[str]) -> bool:
    folded = tuple(nfc(value).casefold() for value in values)
    return any(fragment.casefold() in value for value in folded for fragment in fragments)


def classify(relative_path: Path) -> dict[str, Any]:
    parts = tuple(nfc(part) for part in relative_path.parts)
    parents = parts[:-1]
    suffix = relative_path.suffix.casefold()
    signals = type_signals(relative_path)
    distinct_types = sorted({signal["type"] for signal in signals})
    conflict = len(distinct_types) > 1
    problem_type = distinct_types[0] if len(distinct_types) == 1 else None
    primary_types = [primary_folder_type(folder) for folder in parents]
    primary_types = [value for value in primary_types if value]
    primary_folder = bool(primary_types)
    award, award_evidence = award_status(relative_path, primary_folder)
    year = extract_year(parts)

    parent_folded = {parent.casefold() for parent in parents}
    name_folded = nfc(relative_path.name).casefold()
    out_of_scope_type = any(parent.upper() in {"Y", "Z"} for parent in parents)
    in_results_folder = "results" in parent_folded
    in_problems_folder = "problems" in parent_folded or any(
        "mcm-icm_problems" in parent.casefold() for parent in parents
    )
    in_other_award_folder = OTHER_AWARD_FOLDER.casefold() in parent_folded
    in_triage_folder = any(TRIAGE_FOLDER_FRAGMENT in parent for parent in parents)

    is_results = in_results_folder or "results" in name_folded
    is_triage = in_triage_folder or "triage_guide" in name_folded
    is_problem_statement = in_problems_folder or (
        "problem" in name_folded
        and award not in {"outstanding", "finalist"}
        and "solution" not in name_folded
    )

    eligibility_reason: str | None = None
    exclusion_reason: str | None = None

    if suffix != ".pdf":
        if suffix in DATA_EXTENSIONS:
            role = "problem-dataset"
        elif suffix in CODE_EXTENSIONS:
            role = "supplemental-code"
        elif suffix in DOCUMENT_EXTENSIONS:
            role = "supplemental-document"
        else:
            role = "unknown-quarantine"
            exclusion_reason = "unsupported-extension"
    elif out_of_scope_type:
        role = "out-of-scope-problem-type"
        exclusion_reason = "problem-type-outside-A-F"
    elif is_results:
        role = "results-document"
    elif is_triage:
        role = "judging-or-triage-guide"
    elif is_problem_statement:
        role = "problem-statement"
    elif conflict:
        role = "unknown-quarantine"
        exclusion_reason = "conflicting-A-F-path-or-filename-signals"
    elif award in {"outstanding", "finalist"} and problem_type in TYPE_SET:
        role = "award-paper-primary" if award == "outstanding" else "award-paper-finalist"
        eligibility_reason = award_evidence
    elif in_other_award_folder or award in {"meritorious", "honorable", "successful"}:
        role = "other-award-paper"
        exclusion_reason = "award-status-outside-Outstanding-or-Finalist"
    else:
        role = "unknown-quarantine"
        exclusion_reason = "no-eligible-paper-or-context-role-rule-matched"

    if conflict:
        classification_status = "conflict"
    elif problem_type:
        classification_status = "classified"
    else:
        classification_status = "not-classified"

    return {
        "award_evidence": award_evidence,
        "award_status": award,
        "classification_status": classification_status,
        "document_role": role,
        "eligibility_reason": eligibility_reason,
        "eligible_paper": role in {"award-paper-primary", "award-paper-finalist"},
        "exclusion_reason": exclusion_reason,
        "problem_type": problem_type,
        "type_signals": signals,
        "year": year,
    }


def pdf_info(path: Path, executable: str) -> dict[str, Any]:
    try:
        result = subprocess.run(
            [executable, str(path)],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return {"pdfinfo_status": "error", "pdfinfo_error": str(error), "page_count": None}

    if result.returncode != 0:
        message = (result.stderr or result.stdout).strip()[:500]
        return {"pdfinfo_status": "error", "pdfinfo_error": message, "page_count": None}

    values: dict[str, str] = {}
    for line in result.stdout.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip().casefold()] = value.strip()

    pages = values.get("pages")
    return {
        "page_count": int(pages) if pages and pages.isdigit() else None,
        "pdf_encrypted": values.get("encrypted"),
        "pdf_page_size": values.get("page size"),
        "pdf_version": values.get("pdf version"),
        "pdfinfo_error": None,
        "pdfinfo_status": "ok",
    }


def probe_pdf_text(path: Path, executable: str, pages: int) -> dict[str, Any]:
    try:
        result = subprocess.run(
            [executable, "-f", "1", "-l", str(pages), "-layout", str(path), "-"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=90,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return {
            "text_probe_chars": 0,
            "text_probe_class": "probe-error",
            "text_probe_error": str(error),
            "text_probe_pages": pages,
            "text_probe_words": 0,
        }

    if result.returncode != 0:
        message = (result.stderr or result.stdout).strip()[:500]
        return {
            "text_probe_chars": 0,
            "text_probe_class": "probe-error",
            "text_probe_error": message,
            "text_probe_pages": pages,
            "text_probe_words": 0,
        }

    text = result.stdout
    char_count = len(re.sub(r"\s+", "", text))
    word_count = len(re.findall(r"[A-Za-z0-9]+", text))
    if char_count >= 200:
        probe_class = "text-rich"
    elif char_count >= 20:
        probe_class = "text-sparse"
    else:
        probe_class = "no-text"
    return {
        "text_probe_chars": char_count,
        "text_probe_class": probe_class,
        "text_probe_error": None,
        "text_probe_pages": pages,
        "text_probe_words": word_count,
    }


def slug_token(path: Path) -> str:
    match = TEAM_TOKEN_RE.search(path.stem)
    if match:
        return match.group(0)
    ascii_stem = unicodedata.normalize("NFKD", path.stem).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-z0-9]+", "-", ascii_stem.casefold()).strip("-")
    return value[:24] or "unknown"


def make_record(
    source_root: Path,
    path: Path,
    pdfinfo_executable: str | None,
    pdftotext_executable: str | None,
    probe_pages: int,
) -> dict[str, Any]:
    relative_path = path.relative_to(source_root)
    normalized_relative = nfc(relative_path.as_posix())
    stat = path.stat()
    digest = sha256_file(path)
    path_digest = hashlib.sha256(normalized_relative.encode("utf-8")).hexdigest()
    classification = classify(relative_path)
    record: dict[str, Any] = {
        "content_id": f"C-{digest[:12]}",
        "document_id": f"D-{path_digest[:12]}",
        "file_extension": path.suffix.casefold(),
        "file_name": nfc(path.name),
        "file_size_bytes": stat.st_size,
        "modified_time_ns": stat.st_mtime_ns,
        "record_version": RECORD_VERSION,
        "relative_path": normalized_relative,
        "sha256": digest,
        **classification,
    }

    if record["eligible_paper"]:
        record["paper_id"] = (
            f"P-{record['problem_type']}-{record['year'] or 'unknown'}-"
            f"{slug_token(relative_path)}-{digest[:8]}"
        )
    else:
        record["paper_id"] = None

    if path.suffix.casefold() == ".pdf":
        if pdfinfo_executable:
            record.update(pdf_info(path, pdfinfo_executable))
        else:
            record.update(
                {"page_count": None, "pdfinfo_error": None, "pdfinfo_status": "not-run"}
            )
        if pdftotext_executable:
            record.update(probe_pdf_text(path, pdftotext_executable, probe_pages))
        else:
            record.update(
                {
                    "text_probe_chars": None,
                    "text_probe_class": "not-run",
                    "text_probe_error": None,
                    "text_probe_pages": probe_pages,
                    "text_probe_words": None,
                }
            )
    else:
        record.update(
            {
                "page_count": None,
                "pdfinfo_error": None,
                "pdfinfo_status": "not-applicable",
                "text_probe_chars": None,
                "text_probe_class": "not-applicable",
                "text_probe_error": None,
                "text_probe_pages": None,
                "text_probe_words": None,
            }
        )
    return record


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    lines = [json.dumps(record, ensure_ascii=False, sort_keys=True) for record in records]
    atomic_write_text(path, "\n".join(lines) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fields), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def count_nested(records: list[dict[str, Any]], key: str) -> dict[str, int]:
    counts = Counter(str(record.get(key) or "null") for record in records)
    return dict(sorted(counts.items()))


def build_summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    eligible = [record for record in records if record["eligible_paper"]]
    type_counts = Counter(record["problem_type"] for record in eligible)
    year_type: dict[str, Counter[str]] = defaultdict(Counter)
    for record in eligible:
        year_type[str(record["year"] or "unknown")][str(record["problem_type"])] += 1

    inventory_rows = "\n".join(
        f"{record['relative_path']}\t{record['file_size_bytes']}\t{record['sha256']}"
        for record in records
    )
    inventory_signature = hashlib.sha256(inventory_rows.encode("utf-8")).hexdigest()
    exact_duplicate_groups = Counter(record["sha256"] for record in records)
    duplicate_groups = sum(1 for count in exact_duplicate_groups.values() if count > 1)
    duplicate_extra_files = sum(count - 1 for count in exact_duplicate_groups.values() if count > 1)

    return {
        "candidate_counts_by_type": {key: type_counts.get(key, 0) for key in sorted(TYPE_SET)},
        "candidate_counts_by_year_and_type": {
            year: {key: counts.get(key, 0) for key in sorted(TYPE_SET)}
            for year, counts in sorted(year_type.items())
        },
        "eligible_paper_count": len(eligible),
        "exact_duplicate_extra_file_count": duplicate_extra_files,
        "exact_duplicate_group_count": duplicate_groups,
        "extension_counts": count_nested(records, "file_extension"),
        "inventory_signature_sha256": inventory_signature,
        "pdfinfo_status_counts": count_nested(records, "pdfinfo_status"),
        "record_count": len(records),
        "role_counts": count_nested(records, "document_role"),
        "text_probe_class_counts": count_nested(records, "text_probe_class"),
        "total_bytes": sum(record["file_size_bytes"] for record in records),
        "type_conflict_count": sum(
            record["classification_status"] == "conflict" for record in records
        ),
        "unknown_quarantine_count": sum(
            record["document_role"] == "unknown-quarantine" for record in records
        ),
    }


def summary_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Corpus Manifest Summary",
        "",
        f"- Inventory signature: `{summary['inventory_signature_sha256']}`",
        f"- Files: {summary['record_count']}",
        f"- Bytes: {summary['total_bytes']}",
        f"- Eligible papers: {summary['eligible_paper_count']}",
        f"- Type conflicts: {summary['type_conflict_count']}",
        f"- Unknown quarantine: {summary['unknown_quarantine_count']}",
        f"- Exact duplicate groups: {summary['exact_duplicate_group_count']}",
        f"- Exact duplicate extra files: {summary['exact_duplicate_extra_file_count']}",
        "",
        "## Eligible Papers by Type",
        "",
        "| Type | Count |",
        "|---|---:|",
    ]
    for problem_type, count in summary["candidate_counts_by_type"].items():
        lines.append(f"| {problem_type} | {count} |")

    lines.extend(["", "## Roles", "", "| Role | Count |", "|---|---:|"])
    for role, count in summary["role_counts"].items():
        lines.append(f"| {role} | {count} |")

    lines.extend(
        ["", "## PDF Text Probe", "", "| Class | Count |", "|---|---:|"]
    )
    for probe_class, count in summary["text_probe_class_counts"].items():
        lines.append(f"| {probe_class} | {count} |")

    lines.extend(
        ["", "## Eligible Papers by Year and Type", "", "| Year | A | B | C | D | E | F | Total |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    )
    for year, counts in summary["candidate_counts_by_year_and_type"].items():
        values = [counts[key] for key in sorted(TYPE_SET)]
        lines.append(
            f"| {year} | " + " | ".join(str(value) for value in values) + f" | {sum(values)} |"
        )
    return "\n".join(lines) + "\n"


def duplicate_rows(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[record["sha256"]].append(record)
    rows: list[dict[str, Any]] = []
    for digest, group in sorted(groups.items()):
        if len(group) < 2:
            continue
        canonical = min(record["relative_path"] for record in group)
        for record in sorted(group, key=lambda item: item["relative_path"]):
            rows.append(
                {
                    "sha256": digest,
                    "canonical_relative_path": canonical,
                    "relative_path": record["relative_path"],
                    "is_canonical": record["relative_path"] == canonical,
                }
            )
    return rows


def write_outputs(output_root: Path, records: list[dict[str, Any]]) -> dict[str, Any]:
    eligible = sorted(
        (record for record in records if record["eligible_paper"]),
        key=lambda record: (
            record["problem_type"],
            record["year"] or "9999",
            record["relative_path"].casefold(),
            record["sha256"],
        ),
    )
    queue_rows: list[dict[str, Any]] = []
    for position, record in enumerate(eligible, start=1):
        row = dict(record)
        row["queue_position"] = position
        queue_rows.append(row)

    context_or_excluded = sorted(
        (record for record in records if not record["eligible_paper"]),
        key=lambda record: record["relative_path"].casefold(),
    )
    conflicts = [
        record for record in records if record["classification_status"] == "conflict"
    ]
    unknown = [record for record in records if record["document_role"] == "unknown-quarantine"]
    summary = build_summary(records)

    write_jsonl(output_root / "manifest.jsonl", records)
    write_csv(output_root / "eligible_papers.csv", queue_rows, QUEUE_FIELDS)
    write_csv(
        output_root / "context_and_excluded.csv",
        context_or_excluded,
        (
            "document_id",
            "document_role",
            "problem_type",
            "year",
            "award_status",
            "relative_path",
            "exclusion_reason",
            "sha256",
            "file_size_bytes",
        ),
    )
    write_csv(
        output_root / "classification_conflicts.csv",
        conflicts,
        ("document_id", "relative_path", "problem_type", "classification_status", "exclusion_reason"),
    )
    write_csv(
        output_root / "unknown_quarantine.csv",
        unknown,
        ("document_id", "relative_path", "file_extension", "exclusion_reason"),
    )
    write_csv(
        output_root / "exact_duplicates.csv",
        duplicate_rows(records),
        ("sha256", "canonical_relative_path", "relative_path", "is_canonical"),
    )
    atomic_write_text(
        output_root / "summary.json",
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    atomic_write_text(output_root / "summary.md", summary_markdown(summary))
    return summary


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Extracted corpus root")
    parser.add_argument("--output", type=Path, required=True, help="Generated artifact directory")
    parser.add_argument("--skip-pdf-metadata", action="store_true")
    parser.add_argument("--skip-text-probe", action="store_true")
    parser.add_argument("--probe-pages", type=int, default=2)
    parser.add_argument("--progress-every", type=int, default=25)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    source_root = args.source.resolve()
    output_root = args.output.resolve()
    if not source_root.is_dir():
        raise SystemExit(f"Source directory does not exist: {source_root}")
    if args.probe_pages < 1:
        raise SystemExit("--probe-pages must be at least 1")
    if args.progress_every < 1:
        raise SystemExit("--progress-every must be at least 1")
    try:
        output_root.relative_to(source_root)
    except ValueError:
        pass
    else:
        raise SystemExit("Output must be outside the source corpus")

    pdfinfo_executable = None if args.skip_pdf_metadata else shutil.which("pdfinfo")
    pdftotext_executable = None if args.skip_text_probe else shutil.which("pdftotext")
    if not args.skip_pdf_metadata and not pdfinfo_executable:
        raise SystemExit("pdfinfo is required unless --skip-pdf-metadata is used")
    if not args.skip_text_probe and not pdftotext_executable:
        raise SystemExit("pdftotext is required unless --skip-text-probe is used")

    paths = sorted(
        (path for path in source_root.rglob("*") if path.is_file()),
        key=lambda path: nfc(path.relative_to(source_root).as_posix()).casefold(),
    )
    records: list[dict[str, Any]] = []
    for index, path in enumerate(paths, start=1):
        if index == 1 or index == len(paths) or index % args.progress_every == 0:
            print(f"[{index}/{len(paths)}] {path.relative_to(source_root)}", file=sys.stderr)
        records.append(
            make_record(
                source_root,
                path,
                pdfinfo_executable,
                pdftotext_executable,
                args.probe_pages,
            )
        )

    summary = write_outputs(output_root, records)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
