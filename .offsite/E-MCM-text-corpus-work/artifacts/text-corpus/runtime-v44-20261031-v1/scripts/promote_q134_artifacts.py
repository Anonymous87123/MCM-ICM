#!/usr/bin/env python3
"""Back up the Queue 134 placeholder and promote validated staged bytes."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2020-2013836-4c773f05"
EXPECTED_SOURCE_SHA256 = (
    "4c773f053b00da659fae50121f4d8d6a0d6bb29d3af57d0eb1951d45e2d13c14"
)
STAGE = ROOT / "tmp" / "q134-stage-v2"
OCR = ROOT / "tmp" / "q134-ocr-stage-v2" / PAPER_ID
PAPER_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID
BACKUP_ROOT = ROOT / "tmp" / "q134-promotion-backup-v1"
REPORT = ROOT / "tmp" / "q134-promotion-report-v1.json"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def inventory(root: Path) -> list[dict[str, Any]]:
    return [
        {
            "relative_path": path.relative_to(root).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": digest(path),
        }
        for path in sorted(candidate for candidate in root.rglob("*") if candidate.is_file())
    ]


def write_json_exclusive(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")


def add_tree(
    mappings: list[tuple[Path, Path]], source_root: Path, destination_root: Path
) -> None:
    mappings.extend(
        (source, destination_root / source.relative_to(source_root))
        for source in sorted(
            candidate for candidate in source_root.rglob("*") if candidate.is_file()
        )
    )


def main() -> None:
    if BACKUP_ROOT.exists():
        raise SystemExit(f"refusing to overwrite backup: {BACKUP_ROOT}")
    if REPORT.exists():
        raise SystemExit(f"refusing to overwrite report: {REPORT}")
    if not PAPER_ROOT.is_dir():
        raise SystemExit(f"missing canonical placeholder: {PAPER_ROOT}")

    extraction = json.loads((STAGE / "extraction.json").read_text(encoding="utf-8"))
    source_path = ROOT.parent / "MCM-ICM-master" / extraction["source_relative_path"]
    if not source_path.is_file() or digest(source_path) != EXPECTED_SOURCE_SHA256:
        raise SystemExit("source PDF identity changed")

    stage_files = {
        STAGE / f"paper-card-{PAPER_ID}.json": ROOT
        / "artifacts"
        / "paper-cards"
        / f"{PAPER_ID}.json",
        STAGE / f"language-units-{PAPER_ID}.json": ROOT
        / "artifacts"
        / "language-units"
        / f"{PAPER_ID}.json",
        STAGE / f"model-units-{PAPER_ID}.json": ROOT
        / "artifacts"
        / "model-units"
        / f"{PAPER_ID}.json",
        STAGE / f"learning-audit-{PAPER_ID}.json": ROOT
        / "artifacts"
        / "learning-audits"
        / f"{PAPER_ID}.json",
        STAGE / f"observations-{PAPER_ID}.jsonl": ROOT
        / "artifacts"
        / "observations"
        / f"{PAPER_ID}.jsonl",
        STAGE / "B-rules-staged.jsonl": ROOT
        / "artifacts"
        / "type-branches"
        / "B"
        / "rules.jsonl",
        STAGE / f"{PAPER_ID}-rule-impact-report.json": ROOT
        / "artifacts"
        / "type-branches"
        / "B"
        / f"{PAPER_ID}-rule-impact-report.json",
    }
    for source in stage_files:
        if not source.is_file():
            raise SystemExit(f"missing staged artifact: {source}")
    for destination in stage_files.values():
        if destination.name != "rules.jsonl" and destination.exists():
            raise SystemExit(f"refusing to overwrite canonical artifact: {destination}")

    rendered = sorted((OCR / "rendered").glob("page-*.png"))
    text_pages = sorted((OCR / "text" / "pages").glob("page-*.txt"))
    proxies = sorted(
        candidate
        for candidate in (STAGE / "review-proxies").rglob("*")
        if candidate.is_file()
    )
    if len(rendered) != 25 or len(text_pages) != 25 or len(proxies) != 9:
        raise SystemExit("staged paper tree has unexpected page or proxy counts")
    if inventory(PAPER_ROOT).__len__() != 31:
        raise SystemExit("canonical placeholder no longer has the expected 31-file preimage")

    preimage = inventory(PAPER_ROOT)
    live_rules = ROOT / "artifacts" / "type-branches" / "B" / "rules.jsonl"
    BACKUP_ROOT.mkdir(parents=True, exist_ok=False)
    backup_paper = BACKUP_ROOT / "paper-canonical-preimage"
    shutil.copytree(PAPER_ROOT, backup_paper)
    shutil.copy2(live_rules, BACKUP_ROOT / "B-rules-preimage.jsonl")
    backup_manifest = {
        "paper_id": PAPER_ID,
        "paper_preimage": preimage,
        "paper_preimage_file_count": len(preimage),
        "rules_preimage": {
            "bytes": live_rules.stat().st_size,
            "sha256": digest(live_rules),
        },
        "status": "complete-preimage-backup",
    }
    write_json_exclusive(BACKUP_ROOT / "manifest.json", backup_manifest)
    if inventory(backup_paper) != preimage:
        raise SystemExit("paper preimage backup verification failed")
    if digest(BACKUP_ROOT / "B-rules-preimage.jsonl") != digest(live_rules):
        raise SystemExit("B-rules preimage backup verification failed")

    mappings: list[tuple[Path, Path]] = [
        (OCR / "pages.jsonl", PAPER_ROOT / "pages.jsonl"),
        (OCR / "ocr-lines.jsonl", PAPER_ROOT / "ocr-lines.jsonl"),
        (STAGE / "extraction.json", PAPER_ROOT / "extraction.json"),
    ]
    add_tree(mappings, OCR / "rendered", PAPER_ROOT / "rendered")
    add_tree(mappings, OCR / "text", PAPER_ROOT / "text")
    add_tree(
        mappings,
        STAGE / "review-proxies",
        PAPER_ROOT / "review-proxies",
    )
    mappings.extend(stage_files.items())

    destinations = [destination.resolve() for _, destination in mappings]
    if len(destinations) != len(set(destinations)):
        raise SystemExit("promotion contains duplicate destinations")
    existed_before = {destination: destination.exists() for destination in destinations}
    promoted: list[dict[str, Any]] = []
    for source, destination in mappings:
        if not source.is_file():
            raise SystemExit(f"missing promotion source: {source}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        source_hash = digest(source)
        if digest(destination) != source_hash:
            raise SystemExit(f"promotion hash mismatch: {destination}")
        promoted.append(
            {
                "destination": destination.relative_to(ROOT).as_posix(),
                "source": source.relative_to(ROOT).as_posix(),
                "bytes": destination.stat().st_size,
                "sha256": source_hash,
                "operation": "overwritten-after-backup"
                if existed_before[destination.resolve()]
                else "created",
            }
        )

    report = {
        "backup_manifest_sha256": digest(BACKUP_ROOT / "manifest.json"),
        "created_files": sum(item["operation"] == "created" for item in promoted),
        "files_deleted": 0,
        "overwritten_after_backup": sum(
            item["operation"] == "overwritten-after-backup" for item in promoted
        ),
        "paper_id": PAPER_ID,
        "preimage_file_count": len(preimage),
        "promoted": promoted,
        "promoted_file_count": len(promoted),
        "status": "pass",
    }
    write_json_exclusive(REPORT, report)
    print(json.dumps({key: report[key] for key in (
        "paper_id",
        "preimage_file_count",
        "promoted_file_count",
        "created_files",
        "overwritten_after_backup",
        "files_deleted",
        "status",
    )}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
