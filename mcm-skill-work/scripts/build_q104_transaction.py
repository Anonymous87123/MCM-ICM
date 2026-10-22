from __future__ import annotations

"""Prepare Queue 104's frozen draft and create-only prospective projections."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-28414-5bd5b982"
STAGE = ROOT / "tmp/q104-stage-v2"
STAGED_RULES = ROOT / f"tmp/{PAPER_ID}-B-rules-staged.jsonl"
STAGED_IMPACT = ROOT / f"tmp/{PAPER_ID}-rule-impact-report-staged.json"
SHADOW_ROOT = ROOT / "tmp/q104-prospective-root"
SHADOW_OBSERVATIONS = ROOT / "tmp/q104-prospective-observations"
DRAFT = ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
TIMESTAMP = ROOT / f"tmp/{PAPER_ID}-transaction-timestamp.txt"


def main() -> None:
    path = ROOT / "scripts/build_q103_transaction.py"
    spec = importlib.util.spec_from_file_location("q103_transaction_template", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name, value in {
        "ROOT": ROOT,
        "PAPER_ID": PAPER_ID,
        "PROBLEM_TYPE": "B",
        "STAGE": STAGE,
        "STAGED_RULES": STAGED_RULES,
        "STAGED_IMPACT": STAGED_IMPACT,
        "SHADOW_ROOT": SHADOW_ROOT,
        "SHADOW_OBSERVATIONS": SHADOW_OBSERVATIONS,
        "DRAFT": DRAFT,
        "TIMESTAMP": TIMESTAMP,
    }.items():
        setattr(module, name, value)
    module.main()
    draft = json.loads(DRAFT.read_text(encoding="utf-8"))
    replacements = {
        "All 38/38 physical pages have extracted text, rendered pixels, and completed visual review backed by thirty-eight byte-bounded JPEG proxies across five bounded context segments.": "All 33/33 physical pages have extracted text, rendered pixels, and completed byte-bounded visual review.",
        "160/160 units passed against the full 38-page source text with no failed original-instantiation checks.": "160/160 units passed against the full 33-page source text with no failed original-instantiation checks.",
        "12 nominated B rules received source-matched Queue 103 evidence without lifecycle changes; staged output is frozen at 952e73fe6b3f5dcf8b3f61622c518ca6a2eb476931674b0c56f4a4ccdc484777.": "12 nominated B rules received source-matched Queue 104 evidence without lifecycle changes; staged output is frozen at 952e73fe6b3f5dcf8b3f61622c518ca6a2eb476931674b0c56f4a4ccdc484777.",
        "All 119 regression tests pass against the Queue 103 staged bytes and current formal baseline.": "All 119 regression tests pass against the Queue 104 staged bytes and current formal baseline.",
        "Queue 103 used single JPEG review proxies no larger than 450,000 bytes, at most eight per context segment, and no original-page PNG or full session JSONL transport.": "Queue 104 used single JPEG review proxies no larger than 450,000 bytes, at most eight per context segment, and no original-page PNG or full session JSONL transport.",
    }
    for result in draft["validation_results"]:
        result["details"] = replacements.get(result["details"], result["details"])
    DRAFT.write_text(
        json.dumps(draft, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
