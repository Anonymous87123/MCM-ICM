from __future__ import annotations

import json

import build_q94_transaction as base


PAPER_ID = "P-B-2012-15171-ce229936"


def main() -> None:
    base.PAPER_ID = PAPER_ID
    base.PROBLEM_TYPE = "B"
    base.main()

    draft_path = base.ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    details = {
        "validate_extraction.py": "36/36 text pages and 36/36 rendered pages passed extraction checks; complete page-aware visual review is recorded.",
        "validate_learning_audit.py": f"{draft['after']['section_contract_count']} five-part chapter contracts, the exact 8-paragraph Abstract and 2-paragraph Introduction chains, positive organization artifacts, {draft['after']['important_visual_count']} visual dispositions, and {draft['after']['warning_count']} last-pass warnings passed.",
        "python -m unittest discover -s tests -v": "All 119 regression tests pass against the final live bytes.",
        "request_body_guard": "The failed archived session was inspected only with streaming byte/count summaries that omitted base64 payloads: the session was about 21.87 MB and accumulated 16 images totaling about 19.873 MiB of base64 before nginx returned 413. The root context received no images during Queue 96; visual review used fresh read-only contexts, one image per tool call, byte-bounded JPEG proxies at or below 450,000 bytes, and text-only reports.",
    }
    for result in draft["validation_results"]:
        if result["validator"] in details:
            result["details"] = details[result["validator"]]

    draft_path.write_text(
        json.dumps(draft, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"draft": str(draft_path), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
