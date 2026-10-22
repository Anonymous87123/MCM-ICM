#!/usr/bin/env python3
"""Create a frozen observation corpus for Queue 132 prospective B-rule validation."""

from __future__ import annotations

from pathlib import Path

import prepare_q119_rule_corpus as _q119


PAPER_ID = "P-B-2020-2010821-2af4f390"
ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    _q119.PAPER_ID = PAPER_ID
    _q119.ROOT = ROOT
    _q119.EXISTING = ROOT / "artifacts" / "observations"
    _q119.STAGED = (
        ROOT
        / "tmp"
        / "q132-stage-v2"
        / f"observations-{PAPER_ID}.jsonl"
    )
    _q119.main()


if __name__ == "__main__":
    main()
