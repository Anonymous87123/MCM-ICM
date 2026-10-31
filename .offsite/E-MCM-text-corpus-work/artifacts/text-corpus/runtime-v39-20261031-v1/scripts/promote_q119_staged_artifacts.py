#!/usr/bin/env python3
"""Promote Queue 119 bytes with create-only outputs and hash preconditions."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2017-70174-8bf62421"
STAGE = ROOT / "tmp" / "q119-stage-v2"
STAGED_RULES = STAGE / "rules-replay-1.jsonl"
REPLAY_RULES = STAGE / "rules-replay-2.jsonl"
STAGED_IMPACT = STAGE / "rule-impact-replay-1.json"
REPLAY_IMPACT = STAGE / "rule-impact-replay-2.json"
LIVE_RULES = ROOT / "artifacts" / "type-branches" / "B" / "rules.jsonl"
RULES_PREIMAGE = ROOT / "tmp" / f"{PAPER_ID}-B-rules-preimage.jsonl"
LIVE_EXTRACTION = ROOT / "artifacts" / "papers" / PAPER_ID / "extraction.json"
STAGED_EXTRACTION = STAGE / "extraction.json"
EXTRACTION_PREIMAGE = ROOT / "tmp" / f"{PAPER_ID}-extraction-preimage.json"
NEW = (
    (STAGE / "language.json", ROOT / "artifacts" / "language-units" / f"{PAPER_ID}.json"),
    (STAGE / "models.json", ROOT / "artifacts" / "model-units" / f"{PAPER_ID}.json"),
    (STAGE / "card.json", ROOT / "artifacts" / "paper-cards" / f"{PAPER_ID}.json"),
    (STAGE / "audit.json", ROOT / "artifacts" / "learning-audits" / f"{PAPER_ID}.json"),
    (STAGE / "observations.jsonl", ROOT / "artifacts" / "observations" / f"{PAPER_ID}.jsonl"),
    (
        STAGED_IMPACT,
        ROOT / "artifacts" / "type-branches" / "B" / f"{PAPER_ID}-rule-impact-report.json",
    ),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def lexists(path: Path) -> bool:
    return os.path.lexists(path)


def require_within_root(path: Path) -> None:
    try:
        path.relative_to(ROOT)
    except ValueError as exc:
        raise SystemExit(f"refusing path outside promotion root: {path}") from exc

    current = path.parent
    while True:
        if lexists(current):
            metadata = os.lstat(current)
            reparse = bool(
                getattr(metadata, "st_file_attributes", 0)
                & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
            )
            if stat.S_ISLNK(metadata.st_mode) or reparse:
                raise SystemExit(f"refusing path below symlink or reparse point: {current}")
            if not stat.S_ISDIR(metadata.st_mode):
                raise SystemExit(f"promotion ancestor is not a directory: {current}")
        if current == ROOT:
            return
        if current == current.parent:
            raise SystemExit(f"promotion path does not descend from root: {path}")
        current = current.parent


def read_regular(path: Path, label: str) -> bytes:
    require_within_root(path)
    if not lexists(path):
        raise SystemExit(f"missing {label}: {path}")
    metadata = os.lstat(path)
    reparse = bool(
        getattr(metadata, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    )
    if stat.S_ISLNK(metadata.st_mode) or reparse or not stat.S_ISREG(metadata.st_mode):
        raise SystemExit(f"{label} is not a regular non-link file: {path}")
    return path.read_bytes()


def create_fsynced_sibling(path: Path, data: bytes) -> Path:
    require_within_root(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    require_within_root(path)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.{PAPER_ID}.",
        suffix=".tmp",
        dir=path.parent,
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        if lexists(temporary_path):
            temporary_path.unlink()
        raise
    return temporary_path


def remove_owned_temporary(path: Path) -> None:
    # This exact random sibling was created by this process; no pre-existing path is removed.
    if lexists(path):
        path.unlink()


def normalized_expected(value: str, label: str) -> str:
    normalized = value.lower()
    if len(normalized) != 64 or any(character not in "0123456789abcdef" for character in normalized):
        raise SystemExit(f"{label} must be a lowercase or uppercase SHA-256 digest")
    return normalized


def ensure_exact(path: Path, data: bytes, label: str) -> str:
    require_within_root(path)
    if lexists(path):
        if read_regular(path, label) != data:
            raise SystemExit(f"refusing to overwrite mismatched {label}: {path}")
        return "already-present"

    temporary_path = create_fsynced_sibling(path, data)
    linked = False
    try:
        try:
            os.link(temporary_path, path)
            linked = True
        except FileExistsError:
            if read_regular(path, label) != data:
                raise SystemExit(f"refusing concurrently created mismatched {label}: {path}")
        if read_regular(path, label) != data:
            raise SystemExit(f"create-only verification failed for {label}: {path}")
    finally:
        remove_owned_temporary(temporary_path)
    return "created" if linked else "already-present"


def preflight_exact_or_absent(path: Path, data: bytes, label: str) -> None:
    require_within_root(path)
    if lexists(path) and read_regular(path, label) != data:
        raise SystemExit(f"refusing mismatched existing {label}: {path}")


def inspect_preimage(
    live_path: Path,
    preimage_path: Path,
    expected_before: str,
    desired_data: bytes,
    label: str,
) -> bytes:
    live_data = read_regular(live_path, label)
    live_hash = digest_bytes(live_data)
    desired_hash = digest_bytes(desired_data)
    if live_hash not in {expected_before, desired_hash}:
        raise SystemExit(f"{label} is neither the verified preimage nor staged version")

    if lexists(preimage_path):
        preimage_data = read_regular(preimage_path, f"{label} preimage")
        if digest_bytes(preimage_data) != expected_before:
            raise SystemExit(f"{label} preimage does not match the verified before hash")
        if live_data not in {preimage_data, desired_data}:
            raise SystemExit(f"{label} does not match its preimage or staged bytes")
        return preimage_data

    if live_hash != expected_before:
        raise SystemExit(f"{label} is already promoted but its create-only preimage is missing")
    return live_data


def atomically_promote(
    live_path: Path,
    desired_data: bytes,
    before_data: bytes,
    label: str,
) -> str:
    current_data = read_regular(live_path, label)
    if current_data == desired_data:
        return "already-promoted"
    if current_data != before_data:
        raise SystemExit(f"{label} changed after preimage verification")

    temporary_path = create_fsynced_sibling(live_path, desired_data)
    try:
        rechecked_data = read_regular(live_path, label)
        if rechecked_data == desired_data:
            return "already-promoted"
        if rechecked_data != before_data:
            raise SystemExit(f"{label} changed immediately before atomic replacement")
        os.replace(temporary_path, live_path)
        if read_regular(live_path, label) != desired_data:
            raise SystemExit(f"{label} verification failed after atomic replacement")
    finally:
        remove_owned_temporary(temporary_path)
    return "promoted"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-live-rules-sha256", required=True)
    parser.add_argument("--expected-staged-rules-sha256", required=True)
    parser.add_argument("--expected-live-extraction-sha256", required=True)
    parser.add_argument("--expected-staged-extraction-sha256", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    expected_live_rules = normalized_expected(
        args.expected_live_rules_sha256, "expected live rules hash"
    )
    expected_staged_rules = normalized_expected(
        args.expected_staged_rules_sha256, "expected staged rules hash"
    )
    expected_live_extraction = normalized_expected(
        args.expected_live_extraction_sha256, "expected live extraction hash"
    )
    expected_staged_extraction = normalized_expected(
        args.expected_staged_extraction_sha256, "expected staged extraction hash"
    )

    sources = list(
        dict.fromkeys(
            [source for source, _target in NEW]
            + [
                STAGED_RULES,
                REPLAY_RULES,
                STAGED_IMPACT,
                REPLAY_IMPACT,
                LIVE_RULES,
                LIVE_EXTRACTION,
                STAGED_EXTRACTION,
            ]
        )
    )
    frozen = {path: read_regular(path, "promotion source") for path in sources}

    staged_rules = frozen[STAGED_RULES]
    staged_extraction = frozen[STAGED_EXTRACTION]
    if digest_bytes(staged_rules) != expected_staged_rules:
        raise SystemExit("staged B rules changed since prospective verification")
    if digest_bytes(staged_extraction) != expected_staged_extraction:
        raise SystemExit("staged extraction changed since validation")
    if frozen[REPLAY_RULES] != staged_rules:
        raise SystemExit("independent B-rule replay differs from staged rules")
    if frozen[REPLAY_IMPACT] != frozen[STAGED_IMPACT]:
        raise SystemExit("independent rule-impact replay differs from staged report")

    live_rules = inspect_preimage(
        LIVE_RULES,
        RULES_PREIMAGE,
        expected_live_rules,
        staged_rules,
        "live B rules",
    )
    live_extraction = inspect_preimage(
        LIVE_EXTRACTION,
        EXTRACTION_PREIMAGE,
        expected_live_extraction,
        staged_extraction,
        "live extraction",
    )

    preflight_exact_or_absent(
        RULES_PREIMAGE, live_rules, "live B rules preimage"
    )
    preflight_exact_or_absent(
        EXTRACTION_PREIMAGE, live_extraction, "live extraction preimage"
    )
    for source, target in NEW:
        relative = str(target.relative_to(ROOT)).replace("\\", "/")
        preflight_exact_or_absent(target, frozen[source], relative)

    if args.dry_run:
        create_only_plan = {
            str(path.relative_to(ROOT)).replace("\\", "/"): (
                "verify-existing" if lexists(path) else "create"
            )
            for path in [
                RULES_PREIMAGE,
                EXTRACTION_PREIMAGE,
                *[target for _source, target in NEW],
            ]
        }
        print(
            json.dumps(
                {
                    "paper_id": PAPER_ID,
                    "create_only_plan": create_only_plan,
                    "live_update_plan": {
                        "rules": (
                            "already-promoted"
                            if read_regular(LIVE_RULES, "live B rules") == staged_rules
                            else "atomic-replace"
                        ),
                        "extraction": (
                            "already-promoted"
                            if read_regular(LIVE_EXTRACTION, "live extraction")
                            == staged_extraction
                            else "atomic-replace"
                        ),
                    },
                    "status": "dry-run-pass",
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return

    rules_preimage_status = ensure_exact(
        RULES_PREIMAGE, live_rules, "live B rules preimage"
    )
    extraction_preimage_status = ensure_exact(
        EXTRACTION_PREIMAGE, live_extraction, "live extraction preimage"
    )

    write_statuses = {}
    for source, target in NEW:
        source_data = frozen[source]
        relative = str(target.relative_to(ROOT)).replace("\\", "/")
        write_statuses[relative] = ensure_exact(target, source_data, relative)

    write_statuses[str(LIVE_RULES.relative_to(ROOT)).replace("\\", "/")] = (
        atomically_promote(
            LIVE_RULES,
            staged_rules,
            live_rules,
            "live B rules",
        )
    )
    write_statuses[str(LIVE_EXTRACTION.relative_to(ROOT)).replace("\\", "/")] = (
        atomically_promote(
            LIVE_EXTRACTION,
            staged_extraction,
            live_extraction,
            "live extraction",
        )
    )

    if digest_bytes(read_regular(RULES_PREIMAGE, "rules preimage")) != expected_live_rules:
        raise SystemExit("rules preimage changed during promotion")
    if digest_bytes(read_regular(EXTRACTION_PREIMAGE, "extraction preimage")) != expected_live_extraction:
        raise SystemExit("extraction preimage changed during promotion")
    for source, target in NEW:
        relative = str(target.relative_to(ROOT)).replace("\\", "/")
        if read_regular(target, relative) != frozen[source]:
            raise SystemExit(f"final artifact changed during promotion: {relative}")
    if read_regular(LIVE_RULES, "live B rules") != staged_rules:
        raise SystemExit("live B rules differ from staged bytes after promotion")
    if read_regular(LIVE_EXTRACTION, "live extraction") != staged_extraction:
        raise SystemExit("live extraction differs from staged bytes after promotion")

    hashes = {
        str(target.relative_to(ROOT)).replace("\\", "/"): digest(target)
        for _source, target in NEW
    }
    hashes[str(LIVE_EXTRACTION.relative_to(ROOT)).replace("\\", "/")] = digest(
        LIVE_EXTRACTION
    )
    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "new_artifact_hashes": hashes,
                "rules_before_sha256": hashlib.sha256(live_rules).hexdigest(),
                "rules_after_sha256": digest(LIVE_RULES),
                "extraction_before_sha256": hashlib.sha256(live_extraction).hexdigest(),
                "extraction_after_sha256": digest(LIVE_EXTRACTION),
                "preimage_statuses": {
                    "rules": rules_preimage_status,
                    "extraction": extraction_preimage_status,
                },
                "write_statuses": write_statuses,
                "status": "pass",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
