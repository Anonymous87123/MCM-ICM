"""Assemble the hand-written parts for paper 186 into one runnable census script."""

from __future__ import annotations

from pathlib import Path

PARTS = ["a", "b", "c", "d", "e"]
PROXY = Path(__file__).resolve().parents[1] / ".proxy"


def main() -> None:
    chunks = [(PROXY / f"_t186{p}.py").read_text(encoding="utf-8") for p in PARTS]
    out = PROXY / "_t186_all.py"
    out.write_text("\n\n".join(chunks), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} B)")


if __name__ == "__main__":
    main()
