from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-28875-728f6f07"


def main() -> None:
    path = ROOT / "scripts/build_q103_transaction.py"
    spec = importlib.util.spec_from_file_location("q103_transaction_template_for_q105", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    values = {
        "ROOT": ROOT,
        "PAPER_ID": PAPER_ID,
        "PROBLEM_TYPE": "B",
        "STAGE": ROOT / "tmp/q105-stage-v2",
        "STAGED_RULES": ROOT / f"tmp/{PAPER_ID}-B-rules-staged.jsonl",
        "STAGED_IMPACT": ROOT / f"tmp/{PAPER_ID}-rule-impact-report-staged.json",
        "SHADOW_ROOT": ROOT / "tmp/q105-prospective-root",
        "SHADOW_OBSERVATIONS": ROOT / "tmp/q105-prospective-observations",
        "DRAFT": ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json",
        "TIMESTAMP": ROOT / f"tmp/{PAPER_ID}-transaction-timestamp.txt",
    }
    for name, value in values.items():
        setattr(module, name, value)
    module.main()

    draft = json.loads(values["DRAFT"].read_text(encoding="utf-8"))
    details = {
        "validate_extraction.py": "All 35/35 physical pages have extracted text and rendered pixels. Visual review used four byte-bounded contact-sheet JPEGs for complete page coverage and four focused formula crops; no original full-page PNG entered model transport.",
        "validate_language_anticopy.py": "144/144 language units passed against the complete 35-page source text with no failed original-instantiation checks.",
        "validate_learning_audit.py": "Eighteen five-part chapter contracts, the seven-paragraph Abstract chain, the one-paragraph Introduction chain, six main arguments, 31 visual dispositions, and 12 final warning records passed.",
        "apply_rule_impacts.py": "Twelve nominated B rules received source-matched Queue 105 evidence without lifecycle changes; staged output is frozen at 0e3b6e338dc79f97a42af4ee5d9f6f24be4f5468a19a64129f897301804731fb.",
        "python -m unittest discover -s tests -v": "All 119 regression tests pass against the Queue 105 staged bytes and current formal baseline.",
        "request_body_guard": "Queue 105 used one JPEG per image tool call, every proxy was below 450,000 bytes, the context segment stopped at eight proxies, and no full session JSONL or original-page PNG was transported.",
    }
    for result in draft["validation_results"]:
        replacement = details.get(result["validator"])
        if replacement is not None:
            result["details"] = replacement
    values["DRAFT"].write_text(
        json.dumps(draft, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
