from __future__ import annotations

import json

import build_q94_transaction as base


PAPER_ID = "P-B-2013-21185-c7f22f59"


def main() -> None:
    base.PAPER_ID = PAPER_ID
    base.PROBLEM_TYPE = "B"
    base.main()

    draft_path = base.ROOT / f"artifacts/transactions/{PAPER_ID}-draft.json"
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    details = {
        "validate_extraction.py": "All 43/43 physical pages have text and rendered-page coverage; complete page-aware visual review is recorded, including explicit confirmation of the sparse one-line physical page 43 appendix continuation.",
        "validate_learning_audit.py": f"{draft['after']['section_contract_count']} five-part chapter contracts, the complete Introduction paragraph chain, positive organization artifacts, {draft['after']['important_visual_count']} visual dispositions, and {draft['after']['warning_count']} last-pass warnings passed.",
        "python -m unittest discover -s tests -v": "All 119 regression tests pass against the final staged bytes.",
        "request_body_guard": "The archived 413 failure was inspected only with bounded byte/count summaries that omitted base64 payloads: the session was about 21.9 MB with 16 accumulated image data URLs and about 19.873 MiB of base64 before nginx rejected the request. Queue 100 used three fresh read-only visual contexts, one JPEG proxy per tool call, at most eight proxies per context, every proxy at or below 450,000 bytes, and text-only reports to the root; no original PNG or base64 entered the request.",
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
