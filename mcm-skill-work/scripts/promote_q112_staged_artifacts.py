from __future__ import annotations

"""Promote Queue 112 bytes with create-only outputs and hash preconditions."""

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-40612-8bcdc1a7"
STAGE = ROOT / "tmp/q112-stage-v1"
STAGED_RULES = ROOT / f"tmp/{PAPER_ID}-B-rules-staged.jsonl"
STAGED_IMPACT = ROOT / f"tmp/{PAPER_ID}-rule-impact-report-staged.json"
LIVE_RULES = ROOT / "artifacts/type-branches/B/rules.jsonl"
RULES_PREIMAGE = ROOT / f"tmp/{PAPER_ID}-B-rules-preimage.jsonl"
LIVE_EXTRACTION = ROOT / f"artifacts/papers/{PAPER_ID}/extraction.json"
STAGED_EXTRACTION = STAGE / "extraction.json"
EXTRACTION_PREIMAGE = ROOT / f"tmp/{PAPER_ID}-extraction-preimage.json"
NEW = (
    (STAGE / "language.json", ROOT / f"artifacts/language-units/{PAPER_ID}.json"),
    (STAGE / "models.json", ROOT / f"artifacts/model-units/{PAPER_ID}.json"),
    (STAGE / "card.json", ROOT / f"artifacts/paper-cards/{PAPER_ID}.json"),
    (STAGE / "audit.json", ROOT / f"artifacts/learning-audits/{PAPER_ID}.json"),
    (STAGE / "observations.jsonl", ROOT / f"artifacts/observations/{PAPER_ID}.jsonl"),
    (STAGED_IMPACT, ROOT / f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json"),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def create(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-live-rules-sha256", required=True)
    parser.add_argument("--expected-staged-rules-sha256", required=True)
    parser.add_argument("--expected-live-extraction-sha256", required=True)
    parser.add_argument("--expected-staged-extraction-sha256", required=True)
    args = parser.parse_args()

    sources = [source for source, _target in NEW] + [STAGED_RULES, STAGED_EXTRACTION, LIVE_RULES, LIVE_EXTRACTION]
    missing = [str(path) for path in sources if not path.is_file()]
    existing = [str(target) for _source, target in NEW if target.exists()]
    existing += [str(path) for path in (RULES_PREIMAGE, EXTRACTION_PREIMAGE) if path.exists()]
    if missing:
        raise SystemExit(f"missing staged source(s): {missing}")
    if existing:
        raise SystemExit(f"refusing to overwrite formal or preimage artifact(s): {existing}")

    live_rules = LIVE_RULES.read_bytes()
    staged_rules = STAGED_RULES.read_bytes()
    live_extraction = LIVE_EXTRACTION.read_bytes()
    staged_extraction = STAGED_EXTRACTION.read_bytes()
    checks = (
        (live_rules, args.expected_live_rules_sha256, "live B rules changed since prospective verification"),
        (staged_rules, args.expected_staged_rules_sha256, "staged B rules changed since prospective verification"),
        (live_extraction, args.expected_live_extraction_sha256, "live extraction changed since prospective verification"),
        (staged_extraction, args.expected_staged_extraction_sha256, "staged extraction changed since prospective verification"),
    )
    for data, expected, message in checks:
        if hashlib.sha256(data).hexdigest() != expected.lower():
            raise SystemExit(message)

    create(RULES_PREIMAGE, live_rules)
    create(EXTRACTION_PREIMAGE, live_extraction)
    for source, target in NEW:
        create(target, source.read_bytes())
    LIVE_RULES.write_bytes(staged_rules)
    LIVE_EXTRACTION.write_bytes(staged_extraction)

    hashes = {str(target.relative_to(ROOT)).replace("\\", "/"): digest(target) for _source, target in NEW}
    hashes[str(LIVE_EXTRACTION.relative_to(ROOT)).replace("\\", "/")] = digest(LIVE_EXTRACTION)
    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "new_artifact_hashes": hashes,
                "rules_before_sha256": hashlib.sha256(live_rules).hexdigest(),
                "rules_after_sha256": digest(LIVE_RULES),
                "extraction_before_sha256": hashlib.sha256(live_extraction).hexdigest(),
                "extraction_after_sha256": digest(LIVE_EXTRACTION),
                "status": "pass",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
