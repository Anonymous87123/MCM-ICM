"""Assemble the hand-written parts for P-D-2018-73156-1a30e830 into one payload.

The parts live in .proxy as _t158<part>.py and are concatenated in build order:
  a   helpers, section constants, empty containers
  cap captions and citation blocks for every row
  b   rows on pp5-13
  c   rows on pp14-21
  d   appendix rows and the exclusion ledger
  e   rules and the paper note
  f   ordering, coverage asserts, payload write

Usage: python -I tools/_dist_paper158.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PARTS = ["a", "cap", "b", "c", "d", "e", "f"]


def main() -> None:
    body = "\n".join(
        (LANE / ".proxy" / f"_t158{p}.py").read_text(encoding="utf-8")
        for p in PARTS
    )
    scratch = LANE / ".proxy" / "_t158_all.py"
    scratch.write_text(body, encoding="utf-8")
    done = subprocess.run([sys.executable, "-I", "-X", "utf8", str(scratch)], cwd=LANE)
    raise SystemExit(done.returncode)


if __name__ == "__main__":
    main()
