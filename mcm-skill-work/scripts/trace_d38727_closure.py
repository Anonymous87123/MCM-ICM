#!/usr/bin/env python3
"""Extract bounded, payload-free closure provenance; never replay old commands."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import append_transaction as tx
import stage_integrity_repair as storage

ROOT = storage.ROOT
PID = "P-D-2015-38727-eeb1090f"
CALLS = {
    "call-54fb9a07-9d0b-4515-81c0-2d1a5fc2a2f1-305": "initial-paper-validation",
    "call-af2af327-c305-48d1-b790-a948f6585c21-308": "revised-paper-validation",
    "call-7bc10adf-9515-4c1e-a1d2-f7b132d355d3-309": "bookkeeping-close",
}


def text_only(value):
    if isinstance(value, str):
        return "[image payload omitted]" if "data:image" in value else value
    if isinstance(value, list):
        return "\n".join(text_only(item.get("text", "")) for item in value
                         if isinstance(item, dict) and item.get("type") == "text")
    return ""


def inspect_session(path, start=23000, end=23815):
    evidence = []
    image_requests = []
    with path.open(encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, 1):
            if line_number < start:
                continue
            if line_number > end:
                break
            record = json.loads(raw)
            if record.get("type") not in {"assistant", "user"}:
                continue  # no API-request blobs, copied contexts, or reasoning payloads
            message = record.get("message", {})
            blocks = message.get("content", []) if isinstance(message, dict) else []
            if not isinstance(blocks, list):
                continue
            for block in blocks:
                if not isinstance(block, dict):
                    continue
                kind = block.get("type")
                call_id = block.get("id") if kind == "tool_use" else block.get("tool_use_id")
                if call_id in CALLS and kind in {"tool_use", "tool_result"}:
                    item = {"line": line_number, "timestamp_utc": record.get("timestamp"),
                            "line_sha256": storage.digest(raw.encode("utf-8")),
                            "call_id": call_id, "purpose": CALLS[call_id], "kind": kind}
                    if kind == "tool_use":
                        command = block.get("input", {}).get("command", "")
                        if not isinstance(command, str) or len(command) > 5000 or "data:image" in command:
                            raise ValueError("refusing an oversized or image-bearing command")
                        item.update(tool=block.get("name"), command=command,
                                    command_sha256=storage.digest(command.encode("utf-8")),
                                    complete_visual_flag_present="--require-complete-visual-review" in command)
                    else:
                        text = text_only(block.get("content", ""))
                        if len(text) > 2500:
                            raise ValueError("unexpectedly large selected result; inspect metadata first")
                        item.update(is_error=block.get("is_error", False), text=text)
                    evidence.append(item)
                if kind == "tool_use" and block.get("name") == "Read":
                    target = block.get("input", {}).get("file_path", "")
                    if Path(target).suffix.lower() in {".png", ".jpg", ".jpeg", ".pdf"}:
                        image_requests.append({"line": line_number, "file_path": target})
    return evidence, image_requests


def build(session, output):
    if output.exists():
        raise FileExistsError(f"create-only output exists: {output}")
    evidence, image_requests = inspect_session(session)
    pairs = Counter((item["call_id"], item["kind"]) for item in evidence)
    expected = Counter({(call_id, kind): 1 for call_id in CALLS for kind in ("tool_use", "tool_result")})
    if pairs != expected:
        raise ValueError("expected three original calls and their three results")
    history_path = ROOT / "artifacts/transactions/history.jsonl"
    history = tx.load_history(history_path)
    history_errors = tx.validate_history(history)
    if history_errors:
        raise ValueError(str(history_errors))
    history_matches = [event["event_id"] for event in history if event.get("paper_id") == PID]
    script_path = ROOT / "tmp/q275-close.py"
    script = script_path.read_text(encoding="utf-8")
    if PID not in script or "append_event" in script or "append_transaction" in script:
        raise ValueError("bookkeeping script identity/behaviour changed; no conclusion certified")
    report = {
        "paper_id": PID, "timestamp_utc": tx.utc_now(), "status": "provenance-gap-confirmed-not-repaired",
        "recipe_sha256": storage.digest(Path(__file__).read_bytes()),
        "session_path": str(session), "line_window": [23000, 23815], "selected_operations": evidence,
        "live_history_sha256": storage.digest(history_path.read_bytes()), "live_history_events": len(history),
        "live_history_events_for_paper": history_matches,
        "bookkeeping_script": {"path": "tmp/q275-close.py", "sha256": storage.digest(script_path.read_bytes()),
                               "scope": "sets progress and progress-summary; no history append in this script"},
        "recognized_image_read_requests_in_window": image_requests,
        "findings": [
            "At 2026-10-18T02:55:24Z the recorded card/audit validation command omitted --require-complete-visual-review.",
            "Its recorded output reports CARD:0 and AUDIT:0, but does not attest complete visual review.",
            "At 2026-10-18T02:55:29Z a copied bookkeeping-only script ran and reported closed:416, discovered:19, next:276.",
            "The current bookkeeping script contains the target paper ID but no transaction append; current live history has no target event.",
            "No original closure transaction was recovered from these selected operations; no event is reconstructed or backdated.",
        ],
        "limitations": [
            "This is a bounded execution trace, not a claim that every historical session has been exhaustively reviewed.",
            "Zero recognized Read requests does not prove that no other human or tool ever viewed an image.",
            "The exact old validation scripts/bytes are not all frozen here; old green output is not current gate acceptance.",
            "Commands are stored only as provenance. This script never executes them or modifies session history, progress, or paper artifacts.",
        ],
    }
    storage.put_new(output, storage.encoded(report))
    print(json.dumps({"report": str(output), "selected_operations": len(evidence),
                      "native_history_matches": len(history_matches), "image_payloads_exported": 0}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", type=Path, default=Path(r"C:\Users\Lenovo\.claude\projects\f--MCM\4fa73313-72f5-4f36-abe2-16e943826fad.jsonl"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.session, args.output.resolve())


if __name__ == "__main__":
    main()
