from __future__ import annotations

"""Build a non-destructive complete observation corpus for Queue 104 rule staging."""

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-28414-5bd5b982"
EXISTING = ROOT / "artifacts/observations"
STAGED = ROOT / "tmp/q104-stage-v2/observations.jsonl"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--include-staged", action="store_true")
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    if output.exists():
        raise SystemExit(f"refusing to overwrite existing staged corpus: {output}")

    paths = sorted(
        path for path in EXISTING.glob("*.jsonl") if path.name != f"{PAPER_ID}.jsonl"
    )
    if args.include_staged:
        paths.append(STAGED)

    identifiers: set[str] = set()
    count = 0
    digest = hashlib.sha256()
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as handle:
        for path in paths:
            if not path.is_file():
                raise SystemExit(f"missing corpus input: {path}")
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                record = json.loads(line)
                observation_id = record.get("observation_id")
                if not isinstance(observation_id, str) or not observation_id:
                    raise SystemExit(f"missing observation_id: {path}:{number}")
                if observation_id in identifiers:
                    raise SystemExit(f"duplicate observation_id: {observation_id}")
                identifiers.add(observation_id)
                encoded = (
                    json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
                ).encode("utf-8")
                handle.write(encoded)
                digest.update(encoded)
                count += 1

    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "input_files": len(paths),
                "observation_count": count,
                "output": str(output),
                "sha256": digest.hexdigest(),
                "status": "pass",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
