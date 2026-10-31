#!/usr/bin/env python3
"""Replay all four unchanged paper gates and expose closure-provenance gaps.

Read-only over live artifacts. Writes one create-only audit report, never changes
paper status, gate requirements, visual records, compliance policy, or history.
Rejects a moving input snapshot rather than certifying mixed generations.
"""
from __future__ import annotations

import argparse
import contextlib
import functools
import io
import json
from collections import Counter
from pathlib import Path

import append_transaction as tx
import derive_protocol_compliance as compliance
import stage_integrity_repair as stage
import validate_language_priority_drift as rolling
import validate_language_units as language_validator
import validate_learning_audit as audit_validator
import validate_model_units as model_validator
import validate_paper_artifacts as paper_validator

ROOT = stage.ROOT
ART = ROOT / "artifacts"


def source_paths(paper_ids):
    paths = {ART / "corpus/manifest.jsonl", ART / "progress.jsonl", ART / "transactions/history.jsonl"}
    paths.update((ART / "observations").glob("*.jsonl"))
    paths.update(ART / f"type-branches/{typ}/rules.jsonl" for typ in "ABCDEF")
    for paper_id in paper_ids:
        paths.update(ART / f"{kind}/{paper_id}.json" for kind in (
            "paper-cards", "language-units", "model-units", "learning-audits"))
        paths.add(ART / f"papers/{paper_id}/extraction.json")
    return sorted(paths)


def fingerprints(paths):
    return {path.relative_to(ROOT).as_posix(): stage.digest(path.read_bytes()) for path in paths}


def audit(output):
    if output.exists():
        raise FileExistsError(f"Audit output is create-only: {output}")
    progress = compliance.load_progress(ART / "progress.jsonl")
    ids = [row["paper_id"] for row in progress]
    paths = source_paths(ids)
    frozen = fingerprints(paths)
    manifest = compliance.load_manifest_index(ART / "corpus/manifest.jsonl")
    history = tx.load_history(ART / "transactions/history.jsonl")
    chain_errors = tx.validate_history(history)
    binding_errors = tx.validate_declared_artifacts(history[-1], ROOT) if history else ["empty history"]
    recorded = {event["paper_id"] for event in history}
    native_closed = {event["paper_id"] for event in history
                     if event.get("event_type") == "paper-closed" and event.get("history_completeness") == "native"}
    results, semantic = [], {}
    original_loader = paper_validator.load_jsonl
    paper_validator.load_jsonl = functools.lru_cache(maxsize=None)(original_loader)
    try:
        for index, paper_id in enumerate(ids, 1):
            typ = manifest[paper_id]["problem_type"]
            card_path = ART / f"paper-cards/{paper_id}.json"
            language_path = ART / f"language-units/{paper_id}.json"
            models_path = ART / f"model-units/{paper_id}.json"
            audit_path = ART / f"learning-audits/{paper_id}.json"
            obs_path = ART / f"observations/{paper_id}.jsonl"
            language, models, card, learning_audit = map(stage.read_json, (language_path, models_path, card_path, audit_path))
            observations = stage.read_jsonl(obs_path)
            gates = {
                "language": language_validator.validate_record(language, None, manifest[paper_id]),
                "models": model_validator.validate_record(models, manifest[paper_id]),
                "audit": audit_validator.validate_audit(learning_audit, language, models, card, observations, manifest[paper_id]),
            }
            semantic[paper_id] = gates["audit"]
            stream = io.StringIO()
            args = ["--paper-card", str(card_path), "--observations", str(obs_path),
                    "--rules", str(ART / f"type-branches/{typ}/rules.jsonl"),
                    "--manifest", str(ART / "corpus/manifest.jsonl"),
                    "--extraction", str(ART / f"papers/{paper_id}/extraction.json"),
                    "--observation-corpus", str(ART / "observations"),
                    "--require-complete-visual-review", "--language-record", str(language_path),
                    "--model-record", str(models_path)]
            with contextlib.redirect_stdout(stream):
                paper_validator.main(args)
            gates["paper_artifacts"] = json.loads(stream.getvalue())["errors"]
            results.append({"paper_id": paper_id, "problem_type": typ, "four_gates_pass": not any(gates.values()),
                            "has_history_event": paper_id in recorded, "has_native_closure": paper_id in native_closed,
                            "gates": gates})
            if index % 25 == 0:
                print(json.dumps({"papers_checked": index, "gate_failures_so_far": sum(not row["four_gates_pass"] for row in results)}), flush=True)
    finally:
        paper_validator.load_jsonl = original_loader
    derived = compliance.derive_report(
        progress_path=ART / "progress.jsonl", paper_cards_dir=ART / "paper-cards",
        language_units_dir=ART / "language-units", model_units_dir=ART / "model-units",
        learning_audits_dir=ART / "learning-audits", semantic_errors_by_paper=semantic)
    if fingerprints(paths) != frozen or source_paths(ids) != paths:
        raise ValueError("Live inputs changed during the audit; no report was certified")
    statuses = {row["paper_id"]: row["protocol_status"] for row in derived["records"]}
    failures = [row["paper_id"] for row in results if not row["four_gates_pass"]]
    missing_history = [paper_id for paper_id in ids if paper_id not in recorded]
    missing_closures = [paper_id for paper_id in ids if paper_id not in native_closed]
    qualified = [row["paper_id"] for row in results if row["four_gates_pass"] and row["has_native_closure"]
                 and statuses.get(row["paper_id"]) == "current-validated"]
    drift = rolling.validate_window(history, ART / "observations")
    summary = {
        "papers": len(ids), "lifecycle_status_counts": dict(Counter(row["status"] for row in progress)),
        "current_protocol_complete": derived["current_protocol_complete"],
        "protocol_debt": len(derived["migration_paper_ids"]),
        "four_gates_pass": len(ids) - len(failures), "four_gates_fail": len(failures),
        "papers_without_any_history": len(missing_history), "papers_without_native_closure": len(missing_closures),
        "gates_protocol_and_native_closure": len(qualified),
        "history_events": len(history), "latest_event": history[-1]["event_id"],
        "chain_errors": len(chain_errors), "latest_binding_errors": len(binding_errors), "rolling": drift["status"],
    }
    report = {
        "schema_version": 1, "timestamp_utc": tx.utc_now(), "scope": "all435-live-integrity-snapshot",
        "status": "pass" if len(qualified) == len(ids) and not chain_errors + binding_errors and drift["status"] == "pass" else "correction-required",
        "limitations": ["Structural validators do not prove that earlier manual reading or visual review genuinely occurred.",
                        "No new visual distillation or image inspection was performed; existing visual gate requirements were retained.",
                        "A metadata correction is not new learning and does not repair a missing original closure transaction."],
        "summary": summary, "failed_paper_ids": failures, "unrecorded_paper_ids": missing_history,
        "missing_native_closure_paper_ids": missing_closures, "qualified_paper_ids": qualified,
        "chain_errors": chain_errors, "latest_binding_errors": binding_errors,
        "rolling": drift, "derived_protocol": derived, "records": results, "source_sha256": frozen,
    }
    stage.put_new(output, stage.encoded(report))
    print(json.dumps({"report": str(output), **summary}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    audit(args.output.resolve())


if __name__ == "__main__":
    main()
