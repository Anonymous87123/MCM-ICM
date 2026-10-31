#!/usr/bin/env python3
"""Append and validate hash-chained paper transaction events."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EVENT_FIELDS = {
    "event_id",
    "sequence",
    "timestamp_utc",
    "event_type",
    "paper_id",
    "before",
    "after",
    "changed_fields",
    "artifact_diffs",
    "type_branch_diff",
    "validation_results",
    "unresolved_added",
    "unresolved_resolved",
    "history_completeness",
    "previous_event_hash",
    "event_hash",
}
DRAFT_FIELDS = EVENT_FIELDS - {
    "event_id",
    "sequence",
    "timestamp_utc",
    "history_completeness",
    "previous_event_hash",
    "event_hash",
}
EVENT_TYPES = {
    "migration-baseline",
    "paper-closed",
    "paper-corrected",
    "schema-migrated",
}
ARTIFACT_DIFF_RE = re.compile(
    r"^artifact:(?P<path>[^|]+)\|sha256:(?P<sha256>[0-9a-f]{64})$"
)


def canonical_bytes(event: dict[str, Any]) -> bytes:
    payload = {key: value for key, value in event.items() if key != "event_hash"}
    return json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def event_hash(event: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(event)).hexdigest()


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def string_list(value: Any) -> bool:
    return isinstance(value, list) and all(nonempty_string(item) for item in value)


def nonempty_string_list(value: Any) -> bool:
    return string_list(value) and bool(value)


def validate_declared_artifacts(
    event_or_draft: dict[str, Any], artifact_root: Path
) -> list[str]:
    """Verify machine-readable artifact hashes and declared frozen counts."""
    errors: list[str] = []
    declarations: dict[str, str] = {}
    for item in event_or_draft.get("artifact_diffs", []):
        if not isinstance(item, str) or not item.startswith("artifact:"):
            continue
        match = ARTIFACT_DIFF_RE.fullmatch(item)
        if match is None:
            errors.append(f"invalid artifact declaration: {item}")
            continue
        relative = match.group("path").replace("\\", "/")
        relative_path = Path(relative)
        if relative_path.is_absolute() or ".." in relative_path.parts:
            errors.append(f"artifact path must be canonical and relative: {relative}")
            continue
        if relative in declarations:
            errors.append(f"duplicate artifact declaration: {relative}")
            continue
        declarations[relative] = match.group("sha256")

    paper_id = event_or_draft.get("paper_id")
    after = event_or_draft.get("after")
    if not isinstance(after, dict):
        after = {}
    requires_binding = (
        event_or_draft.get("event_type") == "paper-closed"
        or after.get("protocol_status") == "current-validated"
    )
    if requires_binding and isinstance(paper_id, str):
        required = {
            f"artifacts/paper-cards/{paper_id}.json",
            f"artifacts/language-units/{paper_id}.json",
            f"artifacts/model-units/{paper_id}.json",
            f"artifacts/learning-audits/{paper_id}.json",
            f"artifacts/observations/{paper_id}.jsonl",
        }
        missing = sorted(required - set(declarations))
        if missing:
            errors.append(
                "current-validated event lacks artifact declarations: "
                + ", ".join(missing)
            )

    root = artifact_root.resolve()
    loaded: dict[str, Any] = {}
    for relative, expected_hash in declarations.items():
        path = (root / Path(relative)).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            errors.append(f"artifact path escapes artifact root: {relative}")
            continue
        if not path.is_file():
            errors.append(f"declared artifact does not exist: {relative}")
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            errors.append(f"artifact hash mismatch: {relative}")
            continue
        if path.suffix == ".json":
            try:
                loaded[relative] = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                errors.append(f"declared JSON artifact is invalid: {relative}: {error.msg}")

    if not isinstance(paper_id, str):
        return errors
    language_path = f"artifacts/language-units/{paper_id}.json"
    model_path = f"artifacts/model-units/{paper_id}.json"
    card_path = f"artifacts/paper-cards/{paper_id}.json"
    language = loaded.get(language_path)
    model_record = loaded.get(model_path)
    card = loaded.get(card_path)
    count_checks: dict[str, int] = {}
    if isinstance(language, dict) and isinstance(language.get("units"), list):
        count_checks["language_unit_count"] = len(language["units"])
    if isinstance(model_record, dict) and isinstance(model_record.get("models"), list):
        models = [item for item in model_record["models"] if isinstance(item, dict)]
        count_checks["model_count"] = len(models)
        count_checks["equation_count"] = sum(
            len(item.get("governing_equations", []))
            for item in models
            if isinstance(item.get("governing_equations"), list)
        )
    if isinstance(card, dict) and isinstance(card.get("visualization_observations"), list):
        count_checks["important_visual_count"] = len(card["visualization_observations"])
    for field, actual in count_checks.items():
        if field in after and after[field] != actual:
            errors.append(f"declared {field} differs from frozen artifact ({after[field]} != {actual})")
    if event_or_draft.get("event_type") == "paper-closed":
        for field in (
            "language_unit_count",
            "model_count",
            "equation_count",
            "important_visual_count",
        ):
            if field not in after:
                errors.append(f"paper-closed event requires declared {field}")
    return errors


def validate_history(events: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    event_ids: set[str] = set()
    closed_papers: set[str] = set()
    previous_hash: str | None = None
    for index, event in enumerate(events, start=1):
        label = f"events[{index}]"
        if not isinstance(event, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = sorted(EVENT_FIELDS - set(event))
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")
            continue
        if event.get("sequence") != index:
            errors.append(f"{label} sequence mismatch")
        event_id = event.get("event_id")
        if not nonempty_string(event_id):
            errors.append(f"{label} has invalid event_id")
        elif event_id in event_ids:
            errors.append(f"{label} duplicate event_id {event_id}")
        else:
            event_ids.add(event_id)
        if event.get("previous_event_hash") != previous_hash:
            errors.append(f"{label} previous_event_hash mismatch")
        stored_hash = event.get("event_hash")
        computed_hash = event_hash(event)
        if stored_hash != computed_hash:
            errors.append(f"{label} event_hash mismatch")
        if event.get("history_completeness") not in {"native", "baseline-only"}:
            errors.append(f"{label} has invalid history_completeness")
        elif event.get("event_type") == "migration-baseline" and event.get("history_completeness") != "baseline-only":
            errors.append(f"{label} migration baseline must be baseline-only")
        elif event.get("event_type") != "migration-baseline" and event.get("history_completeness") != "native":
            errors.append(f"{label} non-migration event must be native")
        if event.get("event_type") == "migration-baseline" and index != 1:
            errors.append(f"{label} migration baseline must be the genesis event")
        if not nonempty_string(event.get("timestamp_utc")):
            errors.append(f"{label} has invalid timestamp_utc")
        if event.get("event_type") not in EVENT_TYPES:
            errors.append(f"{label} has invalid event_type")
        if not nonempty_string(event.get("paper_id")) or not re.fullmatch(
            r"P-[A-F]-\d{4}-.+", str(event.get("paper_id", ""))
        ):
            errors.append(f"{label} has invalid paper_id")
        for field in ("before", "after", "type_branch_diff"):
            if not isinstance(event.get(field), dict):
                errors.append(f"{label} {field} must be an object")
        for field in (
            "unresolved_added",
            "unresolved_resolved",
        ):
            if not string_list(event.get(field)):
                errors.append(f"{label} {field} must be a string array")
        for field in ("changed_fields", "artifact_diffs"):
            if not nonempty_string_list(event.get(field)):
                errors.append(f"{label} {field} must be a nonempty string array")
        results = event.get("validation_results")
        if not isinstance(results, list) or not results or not all(
            isinstance(result, dict)
            and nonempty_string(result.get("validator"))
            and result.get("status") == "pass"
            for result in results
        ):
            errors.append(f"{label} validation_results are invalid")
        paper_id = event.get("paper_id")
        if event.get("event_type") == "paper-closed" and isinstance(paper_id, str):
            if paper_id in closed_papers:
                errors.append(f"{label} duplicate paper-closed event for {paper_id}")
            closed_papers.add(paper_id)
        previous_hash = stored_hash if isinstance(stored_hash, str) else None
    return errors


def build_event(
    draft: dict[str, Any],
    history: list[dict[str, Any]],
    timestamp_utc: str,
) -> dict[str, Any]:
    history_errors = validate_history(history)
    if history_errors:
        raise ValueError(f"invalid existing history: {'; '.join(history_errors)}")
    missing = sorted(DRAFT_FIELDS - set(draft))
    if missing:
        raise ValueError(f"event draft missing fields: {', '.join(missing)}")
    paper_id = draft.get("paper_id")
    event_type = draft.get("event_type")
    completeness = draft.get("history_completeness", "native")
    if event_type not in EVENT_TYPES:
        raise ValueError(f"invalid event_type {event_type}")
    if event_type == "migration-baseline" and history:
        raise ValueError("migration-baseline must be the genesis event")
    if event_type == "paper-corrected" and paper_id not in {
        event.get("paper_id") for event in history
    }:
        raise ValueError(f"paper-corrected event targets unknown paper {paper_id}")
    for field in ("before", "after", "type_branch_diff"):
        if not isinstance(draft.get(field), dict) or not draft[field]:
            raise ValueError(f"event draft {field} must be a nonempty object")
    for field in ("changed_fields", "artifact_diffs"):
        if not nonempty_string_list(draft.get(field)):
            raise ValueError(f"event draft {field} must be a nonempty string array")
    results = draft.get("validation_results")
    if not isinstance(results, list) or not results or not all(
        isinstance(result, dict)
        and nonempty_string(result.get("validator"))
        and result.get("status") == "pass"
        for result in results
    ):
        raise ValueError("event draft requires nonempty passing validation_results")
    if event_type == "paper-closed" and any(
        event.get("event_type") == "paper-closed" and event.get("paper_id") == paper_id
        for event in history
    ):
        raise ValueError(f"duplicate paper-closed event for {paper_id}")
    sequence = len(history) + 1
    identity = hashlib.sha256(
        f"{sequence}|{timestamp_utc}|{event_type}|{paper_id}".encode("utf-8")
    ).hexdigest()[:12]
    event: dict[str, Any] = {
        "event_id": f"TX-{sequence:06d}-{identity}",
        "sequence": sequence,
        "timestamp_utc": timestamp_utc,
        **{field: draft[field] for field in DRAFT_FIELDS},
        "history_completeness": completeness,
        "previous_event_hash": history[-1]["event_hash"] if history else None,
    }
    event["event_hash"] = event_hash(event)
    errors = validate_history([*history, event])
    if errors:
        raise ValueError(f"invalid event: {'; '.join(errors)}")
    return event


def load_history(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path} line {line_number}: {error}") from error
            if not isinstance(event, dict):
                raise ValueError(f"{path} line {line_number}: expected object")
            events.append(event)
    return events


@contextmanager
def exclusive_history_lock(path: Path):
    """Prevent two cooperating processes from appending the same sequence."""
    lock_path = path.with_name(f"{path.name}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+b")
    if handle.tell() == 0:
        handle.write(b"\0")
        handle.flush()
    handle.seek(0)
    try:
        if os.name == "nt":
            import msvcrt

            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as error:
        handle.close()
        raise ValueError(f"history is locked by another writer: {path}") from error
    try:
        yield
    finally:
        handle.seek(0)
        if os.name == "nt":
            import msvcrt

            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def append_event(
    path: Path,
    draft: dict[str, Any],
    timestamp_utc: str,
) -> dict[str, Any]:
    with exclusive_history_lock(path):
        history = load_history(path)
        event = build_event(draft, history, timestamp_utc)
        path.parent.mkdir(parents=True, exist_ok=True)
        encoded = json.dumps(event, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        persisted = load_history(path)
        errors = validate_history(persisted)
        if errors:
            raise ValueError(f"persisted history failed validation: {'; '.join(errors)}")
    return event


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", type=Path, required=True)
    parser.add_argument("--draft", type=Path, required=True)
    parser.add_argument("--artifact-root", type=Path, default=Path("."))
    parser.add_argument("--timestamp-utc")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        if args.validate_only:
            events = load_history(args.history)
            errors = validate_history(events)
            draft = json.loads(args.draft.read_text(encoding="utf-8"))
            if not isinstance(draft, dict):
                raise ValueError("event draft must be an object")
            artifact_errors = validate_declared_artifacts(draft, args.artifact_root)
            if artifact_errors:
                raise ValueError("invalid draft artifacts: " + "; ".join(artifact_errors))
            timestamp = args.timestamp_utc or utc_now()
            prospective = build_event(draft, events, timestamp) if not errors else None
            report: dict[str, Any] = {
                "event_count": len(events),
                "errors": errors,
                "prospective_event_id": prospective.get("event_id") if prospective else None,
                "status": "pass" if not errors else "fail",
            }
            print(json.dumps(report, indent=2, sort_keys=True))
            return 0 if not errors else 1
        draft = json.loads(args.draft.read_text(encoding="utf-8"))
        if not isinstance(draft, dict):
            raise ValueError("event draft must be an object")
        artifact_errors = validate_declared_artifacts(draft, args.artifact_root)
        if artifact_errors:
            raise ValueError("invalid draft artifacts: " + "; ".join(artifact_errors))
        timestamp = args.timestamp_utc or utc_now()
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp):
            raise ValueError("timestamp must use UTC YYYY-MM-DDTHH:MM:SSZ")
        event = append_event(args.history, draft, timestamp)
        report = {
            "event_hash": event["event_hash"],
            "event_id": event["event_id"],
            "history": str(args.history),
            "sequence": event["sequence"],
            "status": "pass",
        }
    except (OSError, ValueError, json.JSONDecodeError) as error:
        report = {"errors": [str(error)], "status": "fail"}
        print(json.dumps(report, indent=2, sort_keys=True))
        return 1
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
