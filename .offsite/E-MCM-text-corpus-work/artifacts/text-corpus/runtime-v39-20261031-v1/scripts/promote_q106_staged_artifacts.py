from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-29696-84be6e3a"


def main() -> None:
    path = ROOT / "scripts/promote_q104_staged_artifacts.py"
    spec = importlib.util.spec_from_file_location("q104_promote_template_for_q106", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    stage = ROOT / "tmp/q106-stage-v2"
    staged_rules = ROOT / f"tmp/{PAPER_ID}-B-rules-staged.jsonl"
    staged_impact = ROOT / f"tmp/{PAPER_ID}-rule-impact-report-staged.json"
    module.ROOT = ROOT
    module.PAPER_ID = PAPER_ID
    module.STAGE = stage
    module.STAGED_RULES = staged_rules
    module.STAGED_IMPACT = staged_impact
    module.LIVE_RULES = ROOT / "artifacts/type-branches/B/rules.jsonl"
    module.PREIMAGE = ROOT / f"tmp/{PAPER_ID}-B-rules-preimage.jsonl"
    module.NEW_ARTIFACTS = (
        (stage / "language.json", ROOT / f"artifacts/language-units/{PAPER_ID}.json"),
        (stage / "models.json", ROOT / f"artifacts/model-units/{PAPER_ID}.json"),
        (stage / "card.json", ROOT / f"artifacts/paper-cards/{PAPER_ID}.json"),
        (stage / "audit.json", ROOT / f"artifacts/learning-audits/{PAPER_ID}.json"),
        (stage / "observations.jsonl", ROOT / f"artifacts/observations/{PAPER_ID}.jsonl"),
        (staged_impact, ROOT / f"artifacts/type-branches/B/{PAPER_ID}-rule-impact-report.json"),
    )
    module.main()


if __name__ == "__main__":
    main()
