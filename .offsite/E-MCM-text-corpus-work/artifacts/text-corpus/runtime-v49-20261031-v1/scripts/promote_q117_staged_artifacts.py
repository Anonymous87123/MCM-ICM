#!/usr/bin/env python3
"""Promote Queue 117 bytes with create-only outputs and hash preconditions."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2017-68303-6c8a9ede"
STAGE = ROOT / "tmp" / "q117-stage-v1"
SOURCE_PAPER = ROOT / "tmp" / "q117-extraction" / PAPER_ID
TARGET_PAPER = ROOT / "artifacts" / "papers" / PAPER_ID
STAGED_RULES = STAGE / "B-rules.jsonl"
STAGED_IMPACT = STAGE / "rule-impact-report.json"
LIVE_RULES = ROOT / "artifacts" / "type-branches" / "B" / "rules.jsonl"
RULES_PREIMAGE = ROOT / "tmp" / f"{PAPER_ID}-B-rules-preimage.jsonl"
NEW = (
    (STAGE / "language.json", ROOT / "artifacts" / "language-units" / f"{PAPER_ID}.json"),
    (STAGE / "models.json", ROOT / "artifacts" / "model-units" / f"{PAPER_ID}.json"),
    (STAGE / "card.json", ROOT / "artifacts" / "paper-cards" / f"{PAPER_ID}.json"),
    (STAGE / "audit.json", ROOT / "artifacts" / "learning-audits" / f"{PAPER_ID}.json"),
    (STAGE / "observations.jsonl", ROOT / "artifacts" / "observations" / f"{PAPER_ID}.jsonl"),
    (STAGED_IMPACT, ROOT / "artifacts" / "type-branches" / "B" / f"{PAPER_ID}-rule-impact-report.json"),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_digest(root: Path) -> str:
    value = hashlib.sha256()
    for path in sorted(candidate for candidate in root.rglob("*") if candidate.is_file()):
        relative = path.relative_to(root).as_posix().encode("utf-8")
        value.update(relative)
        value.update(b"\0")
        value.update(hashlib.sha256(path.read_bytes()).digest())
    return value.hexdigest()


def create(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-live-rules-sha256", required=True)
    parser.add_argument("--expected-staged-rules-sha256", required=True)
    parser.add_argument("--expected-source-tree-sha256", required=True)
    args = parser.parse_args()

    paper_sources = sorted(candidate for candidate in SOURCE_PAPER.rglob("*") if candidate.is_file())
    sources = [source for source, _target in NEW] + [STAGED_RULES, LIVE_RULES] + paper_sources
    missing = [str(path) for path in sources if not path.is_file()]
    existing = [str(target) for _source, target in NEW if target.exists()]
    existing += [str(path) for path in (TARGET_PAPER, RULES_PREIMAGE) if path.exists()]
    if missing:
        raise SystemExit(f"missing staged source(s): {missing}")
    if existing:
        raise SystemExit(f"refusing to overwrite formal or preimage artifact(s): {existing}")
    if not paper_sources:
        raise SystemExit(f"source paper tree is empty: {SOURCE_PAPER}")

    live_rules = LIVE_RULES.read_bytes()
    staged_rules = STAGED_RULES.read_bytes()
    if hashlib.sha256(live_rules).hexdigest() != args.expected_live_rules_sha256.lower():
        raise SystemExit("live B rules changed since prospective verification")
    if hashlib.sha256(staged_rules).hexdigest() != args.expected_staged_rules_sha256.lower():
        raise SystemExit("staged B rules changed since prospective verification")
    if tree_digest(SOURCE_PAPER) != args.expected_source_tree_sha256.lower():
        raise SystemExit("source extraction tree changed since prospective verification")

    create(RULES_PREIMAGE, live_rules)
    for source, target in NEW:
        create(target, source.read_bytes())
    for source in paper_sources:
        create(TARGET_PAPER / source.relative_to(SOURCE_PAPER), source.read_bytes())
    LIVE_RULES.write_bytes(staged_rules)

    artifact_hashes = {
        str(target.relative_to(ROOT)).replace("\\", "/"): digest(target)
        for _source, target in NEW
    }
    artifact_hashes[f"artifacts/papers/{PAPER_ID}/extraction.json"] = digest(TARGET_PAPER / "extraction.json")
    print(json.dumps({
        "paper_id": PAPER_ID, "new_artifact_hashes": artifact_hashes,
        "paper_file_count": len(paper_sources), "paper_tree_sha256": tree_digest(TARGET_PAPER),
        "rules_before_sha256": hashlib.sha256(live_rules).hexdigest(),
        "rules_after_sha256": digest(LIVE_RULES), "status": "pass",
    }, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
