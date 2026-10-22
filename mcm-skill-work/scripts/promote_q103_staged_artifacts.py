from __future__ import annotations

"""Promote Queue 103 staged bytes with create-only artifact safeguards."""

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-26636-060c74b1"
STAGE = ROOT / "tmp/q103-stage-v2"
STAGED_RULES = ROOT / f"tmp/{PAPER_ID}-B-rules-staged.jsonl"
STAGED_IMPACT = ROOT / f"tmp/{PAPER_ID}-rule-impact-report-staged.json"
LIVE_RULES = ROOT / "artifacts/type-branches/B/rules.jsonl"
PREIMAGE = ROOT / f"tmp/{PAPER_ID}-B-rules-preimage.jsonl"

NEW_ARTIFACTS = (
    (STAGE / "language.json", ROOT / f"artifacts/language-units/{PAPER_ID}.json"),
    (STAGE / "models.json", ROOT / f"artifacts/model-units/{PAPER_ID}.json"),
    (STAGE / "card.json", ROOT / f"artifacts/paper-cards/{PAPER_ID}.json"),
    (STAGE / "audit.json", ROOT / f"artifacts/learning-audits/{PAPER_ID}.json"),
    (STAGE / "observations.jsonl", ROOT / f"artifacts/observations/{PAPER_ID}.jsonl"),
    (
        STAGED_IMPACT,
        ROOT / f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json",
    ),
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def create_only(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-live-rules-sha256", required=True)
    parser.add_argument("--expected-staged-rules-sha256", required=True)
    args = parser.parse_args()

    sources = [source for source, _ in NEW_ARTIFACTS] + [STAGED_RULES]
    missing = [str(source) for source in sources if not source.is_file()]
    if missing:
        raise SystemExit(f"missing staged source(s): {missing}")
    if not LIVE_RULES.is_file():
        raise SystemExit(f"missing live B rules: {LIVE_RULES}")
    existing = [str(target) for _, target in NEW_ARTIFACTS if target.exists()]
    if PREIMAGE.exists():
        existing.append(str(PREIMAGE))
    if existing:
        raise SystemExit(f"refusing to overwrite formal artifact(s): {existing}")

    live_before = LIVE_RULES.read_bytes()
    staged_rules = STAGED_RULES.read_bytes()
    if digest(live_before) != args.expected_live_rules_sha256.lower():
        raise SystemExit("live B rules changed since prospective verification")
    if digest(staged_rules) != args.expected_staged_rules_sha256.lower():
        raise SystemExit("staged B rules changed since prospective verification")

    # All existence and hash checks happen before the first write. The preimage
    # makes the one intentional shared rules update auditable without cleanup.
    create_only(PREIMAGE, live_before)
    for source, target in NEW_ARTIFACTS:
        create_only(target, source.read_bytes())
    LIVE_RULES.write_bytes(staged_rules)

    artifacts = {
        str(target.relative_to(ROOT)).replace("\\", "/"): digest(target.read_bytes())
        for _, target in NEW_ARTIFACTS
    }
    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "new_artifact_hashes": artifacts,
                "rules_before_sha256": digest(live_before),
                "rules_after_sha256": digest(LIVE_RULES.read_bytes()),
                "rules_preimage": str(PREIMAGE),
                "status": "pass",
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
