from __future__ import annotations

"""Build a create-only observation corpus for Queue 107 rule staging."""

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-30680-9f0c0d05"
EXISTING = ROOT / "artifacts/observations"
STAGED = ROOT / "tmp/q107-stage-v3/observations.jsonl"


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
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                row = json.loads(line)
                observation_id = row.get("observation_id")
                if not isinstance(observation_id, str) or not observation_id:
                    raise SystemExit(f"missing observation_id: {path}:{line_number}")
                if observation_id in seen:
                    raise SystemExit(f"duplicate observation_id: {observation_id}")
                seen.add(observation_id)
                encoded = (json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
                handle.write(encoded)
                digest.update(encoded)
                count += 1
    print(json.dumps({"paper_id": PAPER_ID, "input_files": len(paths), "observation_count": count, "output": str(output), "sha256": digest.hexdigest(), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
