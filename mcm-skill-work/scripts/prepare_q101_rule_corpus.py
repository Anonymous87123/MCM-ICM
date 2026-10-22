from __future__ import annotations

"""Build a non-destructive complete observation corpus for Queue 101 rule staging."""

import hashlib
import json
import argparse
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-26160-510e6a16"
EXISTING = ROOT / "artifacts/observations"
STAGED = ROOT / "tmp/q101-stage-v3/observations.jsonl"
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--include-staged", action="store_true")
    args = parser.parse_args()
    output = args.output
    if not output.is_absolute():
        output = ROOT / output
    if output.exists():
        raise SystemExit(f"refusing to overwrite existing staged corpus: {output}")
    paths = sorted(
        path for path in EXISTING.glob("*.jsonl") if path.name != f"{PAPER_ID}.jsonl"
    )
    if args.include_staged:
        paths.append(STAGED)
    records: list[str] = []
    identifiers: set[str] = set()
    for path in paths:
        if not path.is_file():
            raise SystemExit(f"missing corpus input: {path}")
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            observation_id = record.get("observation_id")
            if not isinstance(observation_id, str) or not observation_id:
                raise SystemExit(f"missing observation_id: {path}:{number}")
            if observation_id in identifiers:
                raise SystemExit(f"duplicate observation_id: {observation_id}")
            identifiers.add(observation_id)
            records.append(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
    text = "\n".join(records) + "\n"
    output.write_text(text, encoding="utf-8")
    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "input_files": len(paths),
                "observation_count": len(records),
                "output": str(output),
                "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                "status": "pass",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
