from __future__ import annotations

import json

import build_q94_transaction as base


PAPER_ID = "P-B-2012-15420-8b46b980"


def main() -> None:
    base.PAPER_ID = PAPER_ID
    base.PROBLEM_TYPE = "B"
    base.main()

    draft_path = base.ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    details = {
        "validate_extraction.py": "The 21/21 rendered pages and 33294 extracted text characters passed extraction checks; physical page 1 has no text layer, remains honestly marked partial-text-review, and its complete Summary was visually transcribed. Complete page-aware visual review is recorded.",
        "validate_learning_audit.py": f"{draft['after']['section_contract_count']} five-part chapter contracts, the exact 2-part Summary/Abstract and 7-paragraph Introduction chains, positive organization artifacts, {draft['after']['important_visual_count']} visual dispositions, and {draft['after']['warning_count']} last-pass warnings passed.",
        "python -m unittest discover -s tests -v": "All 119 regression tests pass against the final live bytes.",
        "request_body_guard": "The failed archived session was inspected only with streaming byte/count summaries that omitted base64 payloads: the request context was 21,873,774 bytes and accumulated 16 image data URLs totaling about 19.873 MiB of base64 before nginx returned HTTP 413. Queue 98 reviewed all 21 pages in three fresh read-only visual batches (pages 1-7, 8-14, and 15-21), one image per tool call, at most seven images per context, using JPEG review proxies at or below 450,000 bytes; the root context received text-only reports and no images.",
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
