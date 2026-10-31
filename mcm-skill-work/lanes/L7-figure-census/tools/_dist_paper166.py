"""Assemble the hand-written parts of paper 166 into one runnable module."""

from __future__ import annotations

from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PARTS = ["a", "b", "c", "d", "e", "f", "g"]


def main() -> None:
    chunks = [(LANE / ".proxy" / f"_t166{p}.py").read_text(encoding="utf-8")
              for p in PARTS]
    out = LANE / ".proxy" / "_t166_all.py"
    out.write_text("\n\n".join(chunks), encoding="utf-8")
    print(f"{len(chunks)} parts -> {out.name}")


if __name__ == "__main__":
    main()
