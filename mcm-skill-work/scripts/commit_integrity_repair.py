#!/usr/bin/env python3
"""Commit validated, frozen metadata repairs, with append-only transactions.

Does not review images, change language/model content, or invent historical
closure events. Papers missing their native transaction remain explicitly
unresolved, even when a canonical-path repair can be committed.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import uuid
from pathlib import Path

import append_transaction as tx
import derive_protocol_compliance as compliance
import stage_integrity_repair as stage
import update_progress
import validate_language_priority_drift as rolling

ROOT = stage.ROOT
ART = ROOT / "artifacts"
HISTORY = ART / "transactions/history.jsonl"


def store(path, value):
    stage.put_new(path, stage.encoded(value))


def replace_checked(path, raw, expected_hash):
    if stage.digest(path.read_bytes()) != expected_hash:
        raise ValueError(f"live file changed outside this repair: {path}")
    temporary = path.with_name(path.name + ".repair-" + uuid.uuid4().hex + ".tmp")
    stage.put_new(temporary, raw)
    os.replace(temporary, path)


def validate_paper(paper_id, log):
    typ = paper_id.split("-")[1]
    card = ART / f"paper-cards/{paper_id}.json"
    language = ART / f"language-units/{paper_id}.json"
    models = ART / f"model-units/{paper_id}.json"
    audit = ART / f"learning-audits/{paper_id}.json"
    obs = ART / f"observations/{paper_id}.jsonl"
    manifest = ART / "corpus/manifest.jsonl"
    commands = [
        ["validate_language_units.py", "--record", str(language), "--manifest", str(manifest)],
        ["validate_model_units.py", "--record", str(models), "--manifest", str(manifest)],
        ["validate_learning_audit.py", "--audit", str(audit), "--language-record", str(language),
         "--model-record", str(models), "--paper-card", str(card), "--observations", str(obs), "--manifest", str(manifest)],
        ["validate_paper_artifacts.py", "--paper-card", str(card), "--observations", str(obs),
         "--rules", str(ART / f"type-branches/{typ}/rules.jsonl"), "--manifest", str(manifest),
         "--extraction", str(ART / f"papers/{paper_id}/extraction.json"), "--observation-corpus", str(ART / "observations"),
         "--require-complete-visual-review", "--language-record", str(language), "--model-record", str(models)],
    ]
    attestations = []
    for command in commands:
        result = subprocess.run([sys.executable, "-B", "-X", "utf8", str(ROOT / "scripts" / command[0]), *command[1:]],
                                cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        parsed = json.loads(result.stdout)
        store(log / (command[0] + ".json"), parsed)
        if result.returncode or parsed.get("status") != "pass":
            raise ValueError(f"{paper_id}: {command[0]} failed: {parsed.get('errors', [])[:3]}")
        attestations.append({"validator": command[0], "status": "pass", "details": f"Fresh live validation, 0 errors; full report: {log.relative_to(ROOT).as_posix()}/{command[0]}.json"})
    tests = subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-q"],
                           cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    stage.put_new(log / "unittest.txt", (tests.stdout + tests.stderr).encode("utf-8"))
    if tests.returncode:
        raise ValueError("regression tests failed")
    attestations.append({"validator": "python -m unittest discover -s tests -q", "status": "pass", "details": "Fresh complete regression suite; output retained beside the four validator reports."})
    return attestations


def rebuild(semantic_errors):
    report = compliance.derive_report(
        progress_path=ART / "progress.jsonl", paper_cards_dir=ART / "paper-cards",
        language_units_dir=ART / "language-units", model_units_dir=ART / "model-units",
        learning_audits_dir=ART / "learning-audits", semantic_errors_by_paper=semantic_errors,
    )
    update_progress.atomic_write(ART / "transactions/current-protocol-compliance.json", stage.encoded(report).decode("utf-8"))
    return report


def verify_live_tail():
    """Finish the protocol in its prescribed post-compliance order."""
    history = tx.load_history(HISTORY)
    drift = rolling.validate_window(history, ART / "observations")
    if drift["status"] != "pass":
        raise ValueError("live rolling validation failed")
    update_progress.atomic_write(ART / "transactions/current-language-priority-drift.json", stage.encoded(drift).decode("utf-8"))
    errors = tx.validate_history(history)
    if history:
        errors += tx.validate_declared_artifacts(history[-1], ROOT)
    if errors:
        raise ValueError(str(errors))
    return {"history_events": len(history), "latest_event": history[-1]["event_id"],
            "chain_errors": 0, "latest_binding_errors": 0, "rolling": drift["status"]}


def committed_correction(history, paper_id, run_name):
    return any(event.get("paper_id") == paper_id
               and event.get("after", {}).get("repair_run") == run_name
               for event in history)


def semantic_snapshot():
    ids = {r["paper_id"] for r in compliance.load_progress(ART / "progress.jsonl") if r.get("status") == "closed"}
    return compliance.semantic_audit_errors(
        closed_ids=ids, paper_cards_dir=ART / "paper-cards", language_units_dir=ART / "language-units",
        model_units_dir=ART / "model-units", learning_audits_dir=ART / "learning-audits",
        observations_dir=ART / "observations", manifest_path=ART / "corpus/manifest.jsonl",
    )


def commit_event(directory, paper_id, changed, stage_report, dependency=False):
    log = directory / "commits" / f"{paper_id}-{uuid.uuid4().hex[:8]}"
    log.mkdir(parents=True, exist_ok=False)
    history = tx.load_history(HISTORY)
    history_sha256 = stage.digest(HISTORY.read_bytes())
    if tx.validate_history(history):
        raise ValueError("invalid existing transaction chain")
    if paper_id not in {e["paper_id"] for e in history}:
        raise ValueError("A metadata correction cannot invent a missing native paper transaction")
    for relative in changed:
        actual = stage.digest((ROOT / relative).read_bytes())
        if actual != stage_report["changes"][relative]["before_sha256"]:
            raise ValueError(f"preimage mismatch for {relative}")
    for relative in changed:
        replace_checked(ROOT / relative, (directory / "after" / relative).read_bytes(), stage_report["changes"][relative]["before_sha256"])
    validations = validate_paper(paper_id, log)
    core = [f"artifacts/{kind}/{paper_id}.{extension}" for kind,extension in [
        ("paper-cards", "json"), ("language-units", "json"), ("model-units", "json"),
        ("learning-audits", "json"), ("observations", "jsonl")]]
    bound = sorted(set(core + changed))
    hashes = {path: stage.digest((ROOT / path).read_bytes()) for path in bound}
    draft = {
        "event_type": "schema-migrated" if dependency else "paper-corrected", "paper_id": paper_id,
        "before": {"repair_run": directory.name, "protocol_status": "correction-required", "file_sha256": {
            path: stage_report["changes"][path]["before_sha256"] for path in changed}},
        "after": {"repair_run": directory.name, "protocol_status": "current-validated", "metadata_only": True,
                  "scope": "Canonical link/schema repair and historical citation recovery; no new paper learning, no new visual review."},
        "changed_fields": ["protocol metadata and historical citation integrity", *changed],
        "artifact_diffs": [f"artifact:{path}|sha256:{hashes[path]}" for path in bound],
        "type_branch_diff": {"problem_type": paper_id.split("-")[1], "metadata_only": True,
                             "shared_catalog_changes": [path for path in changed if "/type-branches/" in path]},
        "validation_results": validations, "unresolved_added": [],
        "unresolved_resolved": ["Missing canonical artifact paths and/or exact historical evidence IDs restored without deleting newer evidence."],
    }
    if dependency:
        draft["after"]["historical_observations_restored"] = stage_report["restored_observation_count"]
        draft["after"]["legacy_rules_conservatively_normalized"] = len(stage_report["normalized_rule_ids"])
        draft["unresolved_added"] = ["Pre-existing pending/legacy visual-review states on supporting papers are not cleared by this metadata migration.",
                                     "Closed progress rows without native transactions remain unresolved; no historical event is fabricated."]
    store(log / "draft.json", draft)
    errors = tx.validate_declared_artifacts(draft, ROOT)
    if errors:
        raise ValueError(str(errors))
    timestamp = tx.utc_now()
    prospective = log / "prospective-history.jsonl"
    stage.put_new(prospective, HISTORY.read_bytes())
    try:
        expected = tx.append_event(prospective, draft, timestamp)
        drift = rolling.validate_window(tx.load_history(prospective), ART / "observations")
        store(log / "prospective-rolling.json", drift)
        if drift["status"] != "pass":
            raise ValueError(f"prospective rolling failure: {drift['errors']}")
    finally:
        # Only these two disposable paths were created by this exact operation.
        prospective.unlink(missing_ok=True)
        prospective.with_name(prospective.name + ".lock").unlink(missing_ok=True)
    if any(stage.digest((ROOT / path).read_bytes()) != value for path,value in hashes.items()):
        raise ValueError("frozen bytes changed after validation")
    if stage.digest(HISTORY.read_bytes()) != history_sha256:
        raise ValueError("history advanced during prospective validation")
    event = tx.append_event(HISTORY, draft, timestamp)
    if event != expected:
        raise ValueError("live event differs from prospective event")
    errors = tx.validate_history(tx.load_history(HISTORY)) + tx.validate_declared_artifacts(event, ROOT)
    if errors:
        raise ValueError(str(errors))
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        update_progress.main(["--progress", str(ART / "progress.jsonl"), "--paper-id", paper_id,
                              "--status", "closed", "--paper-card-status", "validated", "--validation-status", "pass"])
    store(log / "progress-update.json", json.loads(stream.getvalue()))
    store(log / "committed-event.json", event)
    return event


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=Path, required=True)
    parser.add_argument("--mode", choices=["dependencies", "links"], required=True)
    parser.add_argument("--limit", type=int, default=1)
    args = parser.parse_args()
    directory = args.stage.resolve()
    source = stage.read_json(directory / "report.json")
    current_history = tx.load_history(HISTORY)
    history_papers = {e["paper_id"] for e in current_history}
    if args.mode == "dependencies":
        anchor = source["queue"][0]
        paths = [p for p in source["changes"] if "/observations/" in p or "/learning-audits/" in p or "/type-branches/" in p]
        paths.append(f"artifacts/paper-cards/{anchor}.json")
        event = commit_event(directory, anchor, paths, source, dependency=True)
        semantic = semantic_snapshot()
        report = rebuild(semantic)
        verified = verify_live_tail()
        print(json.dumps({"event": event["event_id"], "restored_observations": source["restored_observation_count"],
                          "current_protocol_complete": report["current_protocol_complete"], "remaining": len(report["migration_paper_ids"]),
                          "live_verification": verified}), flush=True)
    else:
        semantic = semantic_snapshot()
        count = 0
        candidates = {r["paper_id"]: r for r in source["validation_results"]}
        for paper_id in source["queue"]:
            relative = f"artifacts/paper-cards/{paper_id}.json"
            if relative not in source["changes"]:
                continue
            if stage.digest((ROOT / relative).read_bytes()) == source["changes"][relative]["after_sha256"]:
                if not committed_correction(tx.load_history(HISTORY), paper_id, directory.name):
                    raise ValueError(f"Installed but uncommitted correction needs journal recovery: {paper_id}")
                continue
            if not candidates[paper_id]["pass"] or paper_id not in history_papers:
                print(json.dumps({"kept_open": paper_id, "reason": "failed existing gate or missing native transaction; not fabricated or waived"}), flush=True)
                continue
            event = commit_event(directory, paper_id, [relative], source)
            semantic.pop(paper_id, None)  # This exact live audit was revalidated above.
            report = rebuild(semantic)
            if next(r for r in report["records"] if r["paper_id"] == paper_id)["protocol_status"] != "current-validated":
                raise ValueError("committed target is not current-validated")
            verified = verify_live_tail()
            print(json.dumps({"event": event["event_id"], "paper_id": paper_id, "current_protocol_complete": report["current_protocol_complete"],
                              "remaining": len(report["migration_paper_ids"]), "live_verification": verified}), flush=True)
            count += 1
            if count >= args.limit:
                break


if __name__ == "__main__":
    main()
