from __future__ import annotations

"""Promote Queue 108 bytes with create-only files and B-rule hash preconditions."""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-32879-2c587e51"
STAGE = ROOT / "tmp/q108-stage-v2"
STAGED_RULES = ROOT / f"tmp/{PAPER_ID}-B-rules-staged.jsonl"
STAGED_IMPACT = ROOT / f"tmp/{PAPER_ID}-rule-impact-report-staged.json"
LIVE_RULES = ROOT / "artifacts/type-branches/B/rules.jsonl"
PREIMAGE = ROOT / f"tmp/{PAPER_ID}-B-rules-preimage.jsonl"
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
    args = parser.parse_args()
    sources = [source for source, _target in NEW] + [STAGED_RULES]
    missing = [str(path) for path in sources if not path.is_file()]
    existing = [str(target) for _source, target in NEW if target.exists()]
    if PREIMAGE.exists():
        existing.append(str(PREIMAGE))
    if missing:
        raise SystemExit(f"missing staged source(s): {missing}")
    if existing:
        raise SystemExit(f"refusing to overwrite formal artifact(s): {existing}")
    before, staged = LIVE_RULES.read_bytes(), STAGED_RULES.read_bytes()
    if hashlib.sha256(before).hexdigest() != args.expected_live_rules_sha256.lower():
        raise SystemExit("live B rules changed since prospective verification")
    if hashlib.sha256(staged).hexdigest() != args.expected_staged_rules_sha256.lower():
        raise SystemExit("staged B rules changed since prospective verification")
    create(PREIMAGE, before)
    for source, target in NEW:
        create(target, source.read_bytes())
    LIVE_RULES.write_bytes(staged)
    hashes = {str(target.relative_to(ROOT)).replace("\\", "/"): digest(target) for _source, target in NEW}
    print(json.dumps({"paper_id": PAPER_ID, "new_artifact_hashes": hashes, "rules_before_sha256": hashlib.sha256(before).hexdigest(), "rules_after_sha256": digest(LIVE_RULES), "rules_preimage": str(PREIMAGE), "status": "pass"}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
