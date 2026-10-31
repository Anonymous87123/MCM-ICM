#!/usr/bin/env python3
"""Promote Queue 118 bytes with create-only outputs and hash preconditions."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2017-69427-b04ae242"
STAGE = ROOT / "tmp" / "q118-stage-v2"
STAGED_EXTRACTION = STAGE / "extraction.json"
CANONICAL_EXTRACTION = (
    ROOT / "artifacts" / "papers" / PAPER_ID / "extraction.json"
)
STAGED_RULES = STAGE / "B-rules.jsonl"
REPLAY_RULES = STAGE / "B-rules-replay.jsonl"
STAGED_IMPACT = STAGE / "rule-impact-report.json"
REPLAY_IMPACT = STAGE / "rule-impact-report-replay.json"
LIVE_RULES = ROOT / "artifacts" / "type-branches" / "B" / "rules.jsonl"
RULES_PREIMAGE = ROOT / "tmp" / f"{PAPER_ID}-B-rules-preimage.jsonl"
NEW = (
    (STAGE / "language.json", ROOT / "artifacts" / "language-units" / f"{PAPER_ID}.json"),
    (STAGE / "models.json", ROOT / "artifacts" / "model-units" / f"{PAPER_ID}.json"),
    (STAGE / "card.json", ROOT / "artifacts" / "paper-cards" / f"{PAPER_ID}.json"),
    (STAGE / "audit.json", ROOT / "artifacts" / "learning-audits" / f"{PAPER_ID}.json"),
    (STAGE / "observations.jsonl", ROOT / "artifacts" / "observations" / f"{PAPER_ID}.jsonl"),
    (
        STAGED_IMPACT,
        ROOT
        / "artifacts"
        / "type-branches"
        / "B"
        / f"{PAPER_ID}-rule-impact-report.json",
    ),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def create(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-live-rules-sha256", required=True)
    parser.add_argument("--expected-staged-rules-sha256", required=True)
    parser.add_argument("--expected-canonical-extraction-sha256", required=True)
    args = parser.parse_args()

    sources = [source for source, _target in NEW] + [
        STAGED_EXTRACTION,
        CANONICAL_EXTRACTION,
        STAGED_RULES,
        REPLAY_RULES,
        REPLAY_IMPACT,
        LIVE_RULES,
    ]
    missing = [str(path) for path in sources if not path.is_file()]
    existing = [str(target) for _source, target in NEW if target.exists()]
    if RULES_PREIMAGE.exists():
        existing.append(str(RULES_PREIMAGE))
    if missing:
        raise SystemExit(f"missing staged or canonical source(s): {missing}")
    if existing:
        raise SystemExit(f"refusing to overwrite formal or preimage artifact(s): {existing}")

    live_rules = LIVE_RULES.read_bytes()
    staged_rules = STAGED_RULES.read_bytes()
    if hashlib.sha256(live_rules).hexdigest() != args.expected_live_rules_sha256.lower():
        raise SystemExit("live B rules changed since prospective verification")
    if hashlib.sha256(staged_rules).hexdigest() != args.expected_staged_rules_sha256.lower():
        raise SystemExit("staged B rules changed since prospective verification")
    if digest(REPLAY_RULES) != digest(STAGED_RULES):
        raise SystemExit("independent B-rule replay differs from staged rules")
    if digest(REPLAY_IMPACT) != digest(STAGED_IMPACT):
        raise SystemExit("independent rule-impact replay differs from staged report")
    if digest(CANONICAL_EXTRACTION) != args.expected_canonical_extraction_sha256.lower():
        raise SystemExit("canonical extraction changed since visual verification")
    staged_extraction = json.loads(STAGED_EXTRACTION.read_text(encoding="utf-8"))
    canonical_extraction = json.loads(
        CANONICAL_EXTRACTION.read_text(encoding="utf-8")
    )
    if staged_extraction != canonical_extraction:
        raise SystemExit("staged and canonical extraction records differ semantically")

    create(RULES_PREIMAGE, live_rules)
    for source, target in NEW:
        create(target, source.read_bytes())
    LIVE_RULES.write_bytes(staged_rules)

    artifact_hashes = {
        str(target.relative_to(ROOT)).replace("\\", "/"): digest(target)
        for _source, target in NEW
    }
    artifact_hashes[
        f"artifacts/papers/{PAPER_ID}/extraction.json"
    ] = digest(CANONICAL_EXTRACTION)
    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "new_artifact_hashes": artifact_hashes,
                "rules_before_sha256": hashlib.sha256(live_rules).hexdigest(),
                "rules_after_sha256": digest(LIVE_RULES),
                "status": "pass",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
