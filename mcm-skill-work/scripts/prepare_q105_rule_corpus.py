from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-28875-728f6f07"


def main() -> None:
    path = ROOT / "scripts/prepare_q104_rule_corpus.py"
    spec = importlib.util.spec_from_file_location("q104_rule_corpus_template", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = ROOT
    module.PAPER_ID = PAPER_ID
    module.EXISTING = ROOT / "artifacts/observations"
    module.STAGED = ROOT / "tmp/q105-stage-v2/observations.jsonl"
    module.main()


if __name__ == "__main__":
    main()
