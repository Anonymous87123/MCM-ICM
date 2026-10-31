#!/usr/bin/env python3
"""Create a frozen observation corpus for Queue 117 prospective B-rule validation."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2017-68303-6c8a9ede"
EXISTING = ROOT / "artifacts" / "observations"
STAGED = ROOT / "tmp" / "q117-stage-v1" / "observations.jsonl"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    if output.exists():
        raise SystemExit(f"refusing to overwrite staged corpus: {output}")

    paths = sorted(EXISTING.glob("*.jsonl")) + [STAGED]
    seen: set[str] = set()
    count = 0
    digest = hashlib.sha256()
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as handle:
        for path in paths:
            if not path.is_file():
                raise SystemExit(f"missing corpus input: {path}")
            with path.open("r", encoding="utf-8") as source:
                for number, line in enumerate(source, 1):
                    if not line.strip():
                        continue
                    row = json.loads(line)
                    key = row.get("observation_id")
                    if not isinstance(key, str) or not key:
                        raise SystemExit(f"missing observation_id: {path}:{number}")
                    if key in seen:
                        raise SystemExit(f"duplicate observation_id: {key}")
                    seen.add(key)
                    data = (json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
                    handle.write(data)
                    digest.update(data)
                    count += 1

    print(json.dumps({
        "paper_id": PAPER_ID, "input_files": len(paths), "observation_count": count,
        "output": str(output), "sha256": digest.hexdigest(), "status": "pass",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
