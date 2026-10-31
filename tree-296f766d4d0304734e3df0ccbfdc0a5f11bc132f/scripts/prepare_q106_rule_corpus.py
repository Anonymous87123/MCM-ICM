from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-29696-84be6e3a"


def main() -> None:
    path = ROOT / "scripts/prepare_q104_rule_corpus.py"
    spec = importlib.util.spec_from_file_location("q104_rule_corpus_template_for_q106", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = ROOT
    module.PAPER_ID = PAPER_ID
    module.EXISTING = ROOT / "artifacts/observations"
    module.STAGED = ROOT / "tmp/q106-stage-v2/observations.jsonl"
    module.main()


if __name__ == "__main__":
    main()
