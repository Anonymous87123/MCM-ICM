#!/usr/bin/env python3
"""Promote Queue 123 bytes with create-only outputs and hash preconditions."""

from __future__ import annotations

from pathlib import Path

import promote_q119_staged_artifacts as _q119


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2018-77238-4380ec81"
STAGE = ROOT / "tmp" / "q123-stage-v2"
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
    (
        STAGE / "language.json",
        ROOT / "artifacts" / "language-units" / f"{PAPER_ID}.json",
    ),
    (
        STAGE / "models.json",
        ROOT / "artifacts" / "model-units" / f"{PAPER_ID}.json",
    ),
    (
        STAGE / "card.json",
        ROOT / "artifacts" / "paper-cards" / f"{PAPER_ID}.json",
    ),
    (
        STAGE / "audit.json",
        ROOT / "artifacts" / "learning-audits" / f"{PAPER_ID}.json",
    ),
    (
        STAGE / "observations.jsonl",
        ROOT / "artifacts" / "observations" / f"{PAPER_ID}.jsonl",
    ),
    (
        STAGED_IMPACT,
        ROOT
        / "artifacts"
        / "type-branches"
        / "B"
        / f"{PAPER_ID}-rule-impact-report.json",
    ),
)


def main() -> None:
    for name, value in {
        "ROOT": ROOT,
        "PAPER_ID": PAPER_ID,
        "STAGE": STAGE,
        "STAGED_RULES": STAGED_RULES,
        "REPLAY_RULES": REPLAY_RULES,
        "STAGED_IMPACT": STAGED_IMPACT,
        "REPLAY_IMPACT": REPLAY_IMPACT,
        "LIVE_RULES": LIVE_RULES,
        "RULES_PREIMAGE": RULES_PREIMAGE,
        "LIVE_EXTRACTION": LIVE_EXTRACTION,
        "STAGED_EXTRACTION": STAGED_EXTRACTION,
        "EXTRACTION_PREIMAGE": EXTRACTION_PREIMAGE,
        "NEW": NEW,
    }.items():
        setattr(_q119, name, value)
    _q119.main()


if __name__ == "__main__":
    main()
