#!/usr/bin/env python3
"""Promote Queue 140 artifacts with frozen hashes and create-only writes."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2021-2127300-7985ddca"
STAGE = ROOT / "tmp" / "q140-stage-v1"
TREE_SOURCE = ROOT / "tmp" / "q140-extraction-v2" / PAPER_ID
TREE_MANIFEST = STAGE / "paper-tree-manifest.json"
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID
LIVE_RULES = ROOT / "artifacts" / "type-branches" / "B" / "rules.jsonl"
STAGED_RULES = STAGE / "B-rules-staged.jsonl"
BACKUP_ROOT = ROOT / "tmp" / "q140-promotion-backup-v1"
BACKUP_RULES = BACKUP_ROOT / "B-rules-preimage.jsonl"
BACKUP_MANIFEST = BACKUP_ROOT / "manifest.json"
REPORT = ROOT / "tmp" / "q140-promotion-report-v1.json"
SOURCE_PDF = (
    ROOT.parent
    / "MCM-ICM-master"
    / "2021\u7f8e\u8d5b\u7279\u7b49\u5956"
    / "B"
    / "2127300.pdf"
)

EXPECTED_SOURCE_SHA256 = (
    "7985ddca762ed1235a76518fbdd88e77870a227dba6d45160646fa3ce62481d3"
)
EXPECTED_TREE_MANIFEST_SHA256 = (
    "1e8fe244c63633e57c16ae6bc5cd95dbb5d0acfc8fb8e40adfd5f4b5c22a6d8f"
)
EXPECTED_LIVE_RULES_SHA256 = (
    "d230e8ae99081f2f1bc12959f2232d5a031453efc87fce617014c858ffb2e28a"
)
EXPECTED_STAGED_RULES_SHA256 = (
    "2dd29f8f6f84edd39a4afb8d208d33253ff26c44e949950493880995a7a373ec"
)
EXPECTED_TREE_FILE_COUNT = 63
EXPECTED_TREE_TOTAL_BYTES = 21_833_389

STAGE_HASHES = {
    STAGE / "B-rules-staged.jsonl": EXPECTED_STAGED_RULES_SHA256,
    STAGE / "extraction.json": (
        "016f383cc41390d3625695a54eeb3fa244c137a1b0bf2fe6262bd0e514abec92"
    ),
    STAGE / f"language-units-{PAPER_ID}.json": (
        "d8a423384fc6155d678984128dec0831f14e3e2f298347c370e96f1cbf205a36"
    ),
    STAGE / f"learning-audit-{PAPER_ID}.json": (
        "17e73facf9afff74baf3867824c3e43d72899aa56cd46f66252ef274f3a6e2dc"
    ),
    STAGE / f"model-units-{PAPER_ID}.json": (
        "bbff71e747643580b843199c2811dea25aa8e533dd26a3c3ee0bcb8c0a35c8ae"
    ),
    STAGE / f"observations-{PAPER_ID}.jsonl": (
        "e76a7a1563acf0b53d521e56c76e144f7fabb1ffdc3de73ce4f924cf2d4fd4db"
    ),
    STAGE / f"paper-card-{PAPER_ID}.json": (
        "4ece8dbd41013a4638d94d5cbaae2dc4f42a153c5f149c90ba2fc859efa1a491"
    ),
    TREE_MANIFEST: EXPECTED_TREE_MANIFEST_SHA256,
    STAGE / f"{PAPER_ID}-rule-impact-report.json": (
        "f20540a52d7e83bab99834704e6cb0844ce2560df93fe14f9272794f2ae8e657"
    ),
}

NEW_ARTIFACTS = (
    (
        STAGE / f"paper-card-{PAPER_ID}.json",
        ROOT / "artifacts" / "paper-cards" / f"{PAPER_ID}.json",
    ),
    (
        STAGE / f"language-units-{PAPER_ID}.json",
        ROOT / "artifacts" / "language-units" / f"{PAPER_ID}.json",
    ),
    (
        STAGE / f"model-units-{PAPER_ID}.json",
        ROOT / "artifacts" / "model-units" / f"{PAPER_ID}.json",
    ),
    (
        STAGE / f"learning-audit-{PAPER_ID}.json",
        ROOT / "artifacts" / "learning-audits" / f"{PAPER_ID}.json",
    ),
    (
        STAGE / f"observations-{PAPER_ID}.jsonl",
        ROOT / "artifacts" / "observations" / f"{PAPER_ID}.jsonl",
    ),
    (
        STAGE / f"{PAPER_ID}-rule-impact-report.json",
        ROOT
        / "artifacts"
        / "type-branches"
        / "B"
        / f"{PAPER_ID}-rule-impact-report.json",
    ),
)


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def lexists(path: Path) -> bool:
    return os.path.lexists(path)


def is_reparse(metadata: os.stat_result) -> bool:
    return bool(
        getattr(metadata, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    )


def require_within(path: Path, root: Path) -> None:
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise SystemExit(f"refusing path outside allowed root: {path}") from exc

    current = path.parent
    while True:
        if lexists(current):
            metadata = os.lstat(current)
            if (
                stat.S_ISLNK(metadata.st_mode)
                or is_reparse(metadata)
                or not stat.S_ISDIR(metadata.st_mode)
            ):
                raise SystemExit(f"unsafe promotion ancestor: {current}")
        if current == root:
            return
        if current == current.parent:
            raise SystemExit(f"path does not descend from allowed root: {path}")
        current = current.parent


def read_regular(path: Path, label: str, root: Path = ROOT) -> bytes:
    require_within(path, root)
    if not lexists(path):
        raise SystemExit(f"missing {label}: {path}")
    metadata = os.lstat(path)
    if (
        stat.S_ISLNK(metadata.st_mode)
        or is_reparse(metadata)
        or not stat.S_ISREG(metadata.st_mode)
    ):
        raise SystemExit(f"{label} is not a regular non-link file: {path}")
    return path.read_bytes()


def json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def create_fsynced_sibling(path: Path, data: bytes) -> Path:
    require_within(path, ROOT)
    path.parent.mkdir(parents=True, exist_ok=True)
    require_within(path, ROOT)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.{PAPER_ID}.", suffix=".tmp", dir=path.parent
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
    if lexists(path):
        path.unlink()


def create_exclusive(path: Path, data: bytes, label: str) -> None:
    require_within(path, ROOT)
    if lexists(path):
        raise SystemExit(f"refusing to overwrite existing {label}: {path}")
    temporary_path = create_fsynced_sibling(path, data)
    try:
        try:
            os.link(temporary_path, path)
        except FileExistsError as exc:
            raise SystemExit(f"refusing concurrently created {label}: {path}") from exc
        if read_regular(path, label) != data:
            raise SystemExit(f"create-only verification failed for {label}: {path}")
    finally:
        remove_owned_temporary(temporary_path)


def atomic_replace_rules(before: bytes, desired: bytes) -> None:
    if read_regular(LIVE_RULES, "live B rules") != before:
        raise SystemExit("live B rules changed after preflight")
    temporary_path = create_fsynced_sibling(LIVE_RULES, desired)
    try:
        if read_regular(LIVE_RULES, "live B rules") != before:
            raise SystemExit("live B rules changed immediately before replacement")
        os.replace(temporary_path, LIVE_RULES)
        if read_regular(LIVE_RULES, "live B rules") != desired:
            raise SystemExit("live B rules verification failed after replacement")
    finally:
        remove_owned_temporary(temporary_path)


def validate_relative_path(value: Any) -> PurePosixPath:
    if not isinstance(value, str) or not value:
        raise SystemExit("tree manifest contains an invalid relative path")
    relative = PurePosixPath(value)
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
        raise SystemExit(f"unsafe tree-manifest relative path: {value!r}")
    return relative


def verify_stage() -> None:
    actual_files = {path for path in STAGE.iterdir() if path.is_file()}
    if actual_files != set(STAGE_HASHES):
        raise SystemExit("Q140 stage inventory changed after validation")
    for path, expected_hash in STAGE_HASHES.items():
        data = read_regular(path, f"staged file {path.name}")
        if digest_bytes(data) != expected_hash:
            raise SystemExit(f"staged file changed after validation: {path}")


def freeze_tree(
    manifest_data: bytes,
) -> tuple[list[tuple[Path, Path, bytes]], dict[str, Any]]:
    if digest_bytes(manifest_data) != EXPECTED_TREE_MANIFEST_SHA256:
        raise SystemExit("paper-tree manifest changed since validation")
    try:
        manifest = json.loads(manifest_data)
    except json.JSONDecodeError as exc:
        raise SystemExit("paper-tree manifest is not valid JSON") from exc

    if (
        manifest.get("paper_id") != PAPER_ID
        or manifest.get("status") != "frozen"
        or manifest.get("files_deleted") != 0
        or manifest.get("source_sha256") != EXPECTED_SOURCE_SHA256
        or manifest.get("file_count") != EXPECTED_TREE_FILE_COUNT
        or manifest.get("total_bytes") != EXPECTED_TREE_TOTAL_BYTES
        or not isinstance(manifest.get("files"), list)
        or len(manifest["files"]) != EXPECTED_TREE_FILE_COUNT
        or Path(manifest.get("source_root", "")) != TREE_SOURCE
    ):
        raise SystemExit("paper-tree manifest identity, count, or size is invalid")

    actual_files = {
        path.relative_to(TREE_SOURCE).as_posix()
        for path in TREE_SOURCE.rglob("*")
        if path.is_file()
    }
    mappings: list[tuple[Path, Path, bytes]] = []
    declared_files: set[str] = set()
    total_bytes = 0
    for item in manifest["files"]:
        if not isinstance(item, dict):
            raise SystemExit("paper-tree manifest contains a non-object entry")
        relative = validate_relative_path(item.get("relative_path"))
        relative_text = relative.as_posix()
        if relative_text in declared_files:
            raise SystemExit(f"duplicate paper-tree path: {relative_text}")
        declared_files.add(relative_text)
        expected_size = item.get("bytes")
        expected_hash = item.get("sha256")
        if (
            not isinstance(expected_size, int)
            or expected_size < 0
            or not isinstance(expected_hash, str)
            or len(expected_hash) != 64
            or any(character not in "0123456789abcdef" for character in expected_hash)
        ):
            raise SystemExit(f"invalid manifest metadata for {relative_text}")
        source = TREE_SOURCE.joinpath(*relative.parts)
        destination = PAPER_ROOT.joinpath(*relative.parts)
        data = read_regular(source, f"paper-tree source {relative_text}")
        if len(data) != expected_size or digest_bytes(data) != expected_hash:
            raise SystemExit(f"paper-tree source changed: {relative_text}")
        mappings.append((source, destination, data))
        total_bytes += len(data)

    if actual_files != declared_files or total_bytes != EXPECTED_TREE_TOTAL_BYTES:
        raise SystemExit("paper-tree inventory or byte total changed")
    return mappings, manifest


def relative_to_root(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    verify_stage()
    manifest_data = read_regular(TREE_MANIFEST, "paper-tree manifest")
    tree_mappings, tree_manifest = freeze_tree(manifest_data)
    source_data = read_regular(SOURCE_PDF, "source PDF", ROOT.parent)
    if digest_bytes(source_data) != EXPECTED_SOURCE_SHA256:
        raise SystemExit("source PDF identity changed")

    tree_extraction = next(
        data
        for source, _destination, data in tree_mappings
        if source.relative_to(TREE_SOURCE).as_posix() == "extraction.json"
    )
    staged_extraction = read_regular(STAGE / "extraction.json", "staged extraction")
    if staged_extraction != tree_extraction:
        raise SystemExit("staged extraction differs from frozen paper tree")

    staged_rules = read_regular(STAGED_RULES, "staged B rules")
    live_rules = read_regular(LIVE_RULES, "live B rules")
    if digest_bytes(staged_rules) != EXPECTED_STAGED_RULES_SHA256:
        raise SystemExit("staged B rules changed since validation")
    if digest_bytes(live_rules) != EXPECTED_LIVE_RULES_SHA256:
        raise SystemExit("live B rules do not match the verified Q139 preimage")

    artifact_mappings = [
        (source, destination, read_regular(source, "staged canonical artifact"))
        for source, destination in NEW_ARTIFACTS
    ]
    all_mappings = tree_mappings + artifact_mappings
    destinations = [destination for _source, destination, _data in all_mappings]
    if len(destinations) != len(set(destinations)):
        raise SystemExit("promotion contains duplicate destinations")
    if lexists(PAPER_ROOT):
        raise SystemExit(f"refusing existing Q140 paper root: {PAPER_ROOT}")
    for destination in destinations:
        require_within(destination, ROOT)
        if lexists(destination):
            raise SystemExit(f"refusing existing Q140 target: {destination}")
    for path, label in ((BACKUP_ROOT, "backup"), (REPORT, "promotion report")):
        require_within(path, ROOT)
        if lexists(path):
            raise SystemExit(f"refusing to overwrite existing {label}: {path}")

    summary = {
        "paper_id": PAPER_ID,
        "source_pdf": str(SOURCE_PDF),
        "source_sha256": EXPECTED_SOURCE_SHA256,
        "tree_file_count": len(tree_mappings),
        "tree_total_bytes": tree_manifest["total_bytes"],
        "new_top_level_artifact_count": len(artifact_mappings),
        "created_file_count": len(all_mappings),
        "rules_before_sha256": EXPECTED_LIVE_RULES_SHA256,
        "rules_after_sha256": EXPECTED_STAGED_RULES_SHA256,
        "files_deleted": 0,
    }
    if args.dry_run:
        print(json.dumps({**summary, "status": "dry-run-pass"}, indent=2, sort_keys=True))
        return

    BACKUP_ROOT.mkdir(parents=False, exist_ok=False)
    create_exclusive(BACKUP_RULES, live_rules, "B-rules preimage backup")
    backup_value = {
        "files_deleted": 0,
        "paper_id": PAPER_ID,
        "preimages": [
            {
                "backup_path": relative_to_root(BACKUP_RULES),
                "bytes": len(live_rules),
                "canonical_path": relative_to_root(LIVE_RULES),
                "sha256": digest_bytes(live_rules),
            }
        ],
        "status": "frozen",
    }
    backup_manifest_data = json_bytes(backup_value)
    create_exclusive(BACKUP_MANIFEST, backup_manifest_data, "backup manifest")
    if read_regular(BACKUP_RULES, "B-rules preimage backup") != live_rules:
        raise SystemExit("B-rules preimage backup verification failed")

    promoted: list[dict[str, Any]] = []
    for source, destination, data in all_mappings:
        create_exclusive(destination, data, relative_to_root(destination))
        promoted.append(
            {
                "bytes": len(data),
                "destination": relative_to_root(destination),
                "operation": "created",
                "sha256": digest_bytes(data),
                "source": relative_to_root(source),
            }
        )

    atomic_replace_rules(live_rules, staged_rules)
    promoted.append(
        {
            "bytes": len(staged_rules),
            "destination": relative_to_root(LIVE_RULES),
            "operation": "overwritten-after-backup",
            "sha256": digest_bytes(staged_rules),
            "source": relative_to_root(STAGED_RULES),
        }
    )

    for _source, destination, expected_data in all_mappings:
        if read_regular(destination, relative_to_root(destination)) != expected_data:
            raise SystemExit(f"final promoted artifact changed: {destination}")
    if read_regular(LIVE_RULES, "live B rules") != staged_rules:
        raise SystemExit("live B rules differ from staged bytes after promotion")

    report_value = {
        "backup_manifest_sha256": digest(BACKUP_MANIFEST),
        "created_files": len(all_mappings),
        "files_deleted": 0,
        "overwritten_after_backup": 1,
        "paper_id": PAPER_ID,
        "promoted": promoted,
        "promoted_file_count": len(promoted),
        "source_tree_file_count": len(tree_mappings),
        "source_tree_manifest_sha256": digest_bytes(manifest_data),
        "source_tree_total_bytes": tree_manifest["total_bytes"],
        "status": "pass",
    }
    report_data = json_bytes(report_value)
    create_exclusive(REPORT, report_data, "promotion report")
    if read_regular(REPORT, "promotion report") != report_data:
        raise SystemExit("promotion report verification failed")

    print(
        json.dumps(
            {**summary, "promoted_file_count": len(promoted), "status": "pass"},
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
