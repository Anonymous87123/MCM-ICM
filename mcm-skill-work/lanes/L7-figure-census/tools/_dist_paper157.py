"""Assemble the hand-written parts for P-C-2018-82150-43b69981 into one payload.

The parts live in .proxy as _t157<part>.py and are concatenated in build order:
  a   helpers, section constants, empty containers
  cap captions and citation blocks for every row
  b   rows on pp5-13
  c   rows on pp14-21
  d   appendix rows and the exclusion ledger
  e   rules and the paper note
  f   ordering, coverage asserts, payload write

Usage: python -I tools/_dist_paper157.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PARTS = ["a", "cap", "b", "c", "d", "e", "f"]


def main() -> None:
    body = "\n".join(
        (LANE / ".proxy" / f"_t157{p}.py").read_text(encoding="utf-8")
        for p in PARTS
    )
    scratch = LANE / ".proxy" / "_t157_all.py"
    scratch.write_text(body, encoding="utf-8")
    done = subprocess.run([sys.executable, "-I", "-X", "utf8", str(scratch)], cwd=LANE)
    raise SystemExit(done.returncode)


if __name__ == "__main__":
    main()
