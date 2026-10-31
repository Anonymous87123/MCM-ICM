"""Assemble the hand-written parts for P-C-2018-80560-ad2eea75 into one payload.

The parts live in .proxy as _t156<part>.py and are concatenated in build order:
  a   helpers, section constants, empty containers
  cap captions and citation blocks for every row
  b   rows on pp5-11
  c   rows on pp12-21 and p27
  e   rules and the paper note
  d   exclusion ledger appended to the note
  f   ordering, coverage asserts, payload write

Usage: python -I tools/_dist_paper156.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PARTS = ["a", "cap", "b", "c", "e", "d", "f"]


def main() -> None:
    body = "\n".join(
        (LANE / ".proxy" / f"_t156{p}.py").read_text(encoding="utf-8")
        for p in PARTS
    )
    scratch = LANE / ".proxy" / "_t156_all.py"
    scratch.write_text(body, encoding="utf-8")
    done = subprocess.run([sys.executable, "-I", "-X", "utf8", str(scratch)], cwd=LANE)
    raise SystemExit(done.returncode)


if __name__ == "__main__":
    main()
