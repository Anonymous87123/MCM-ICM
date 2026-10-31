#!/usr/bin/env python3
"""Prepare a create-only, source-preserving integrity repair; never install it.

The output is a candidate view, not a completion claim. Existing validators run
unchanged, including the complete cumulative rule/evidence check. Historical
observations are recovered only by exact ID from recorded local snapshots.
"""
from __future__ import annotations

import argparse
import contextlib
import copy
import functools
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

import append_transaction as tx
import derive_protocol_compliance as compliance
import validate_language_units as language_validator
import validate_learning_audit as audit_validator
import validate_model_units as model_validator
import validate_paper_artifacts as paper_validator


ROOT = Path(__file__).resolve().parents[1]
RECOVERY_SOURCES = {
    "P-B-2012-15420-8b46b980": "tmp/q172-prior-observations-v1/P-B-2012-15420-8b46b980.jsonl",
    "P-C-2025-2505964-9dbe18d6": "tmp/q172-prior-observations-v1/P-C-2025-2505964-9dbe18d6.jsonl",
    "P-C-2023-2301192-c71d36ff": "tmp/q233-g8-stage-v1/observations.jsonl",
    "P-C-2023-2307166-ec54f9ce": "tmp/q234-g8-stage-v1/observations.jsonl",
    "P-C-2023-2307946-61b646ed": "tmp/q235-g8-stage-v1/observations.jsonl",
}


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def encoded(value, jsonl=False) -> bytes:
    if jsonl:
        text = "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in value)
    else:
        text = json.dumps(value, ensure_ascii=False, indent=2)
    return (text + "\n").encode("utf-8")


def put_new(path: Path, raw: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(raw)


def canonical_links(card, paper_id, language, models):
    """Only add canonical path/schema metadata; do not rewrite any evidence."""
    result = copy.deepcopy(card)
    declarations = result["protocol_v2_records"]
    declarations["language"]["path"] = f"artifacts/language-units/{paper_id}.json"
    declarations["models"]["path"] = f"artifacts/model-units/{paper_id}.json"
    declarations["models"]["schema_version"] = models["schema_version"]
    return result


def prepare(output: Path):
    output.mkdir(parents=True, exist_ok=False)
    artifact = ROOT / "artifacts"
    manifest = compliance.load_manifest_index(artifact / "corpus/manifest.jsonl")
    progress = compliance.load_progress(artifact / "progress.jsonl")
    history = tx.load_history(artifact / "transactions/history.jsonl")
    chain_errors = tx.validate_history(history)
    if chain_errors:
        raise ValueError(f"invalid history: {chain_errors[:3]}")
    report = compliance.derive_report(
        progress_path=artifact / "progress.jsonl", paper_cards_dir=artifact / "paper-cards",
        language_units_dir=artifact / "language-units", model_units_dir=artifact / "model-units",
        learning_audits_dir=artifact / "learning-audits",
    )
    debt = {row["paper_id"] for row in report["records"] if row["protocol_status"] != "current-validated"}
    recorded = {row["paper_id"] for row in history}
    missing_history = {row["paper_id"] for row in progress if row["status"] == "closed"} - recorded
    queue = [row["paper_id"] for row in progress if row["paper_id"] in debt | missing_history]
    changes = {}
    source_provenance = {}
    observations = {p.stem: read_jsonl(p) for p in (artifact / "observations").glob("*.jsonl")}
    evidence_ids = {row["observation_id"] for rows in observations.values() for row in rows}
    rules_by_type = {t: read_jsonl(artifact / f"type-branches/{t}/rules.jsonl") for t in "ABCDEF"}
    needed = {eid for rows in rules_by_type.values() for row in rows for eid in row.get("evidence_ids", []) if eid not in evidence_ids}
    restored = []
    for paper_id, source_relative in RECOVERY_SOURCES.items():
        source = ROOT / source_relative
        original_raw = source.read_bytes()
        original_rows = read_jsonl(source)
        selected = [row for row in original_rows if row.get("observation_id") in needed]
        if not selected:
            continue
        if any(row.get("paper_id") != paper_id for row in selected):
            raise ValueError(f"recovery source identity mismatch: {source}")
        source_provenance[source_relative] = {
            "sha256": digest(original_raw), "restored_ids": [row["observation_id"] for row in selected],
        }
        put_new(output / "sources" / source_relative, original_raw)
        for original in selected:
            row = copy.deepcopy(original)
            legacy = {}
            if row.get("year") != manifest[paper_id]["year"]:
                legacy["year"] = row["year"]
                row["year"] = manifest[paper_id]["year"]
            if row.get("confidence") not in paper_validator.CONFIDENCE:
                legacy["confidence"] = row["confidence"]
                row["confidence"] = "low"
            row["recovery_provenance"] = {
                "source_path": source_relative, "source_sha256": digest(original_raw),
                "original_observation_id": original["observation_id"], "legacy_schema_values": legacy,
                "scope": "Restore an existing historical citation, not new learning or promotion; source claims remain subject to review.",
            }
            observations[paper_id].append(row)
            restored.append(row["observation_id"])
        relative = f"artifacts/observations/{paper_id}.jsonl"
        changes[relative] = encoded(observations[paper_id], jsonl=True)
        audit_path = f"artifacts/learning-audits/{paper_id}.json"
        audit = read_json(ROOT / audit_path)
        counts = Counter(row["dimension"] for row in observations[paper_id])
        audit["dimension_counts"] = {key: counts[key] for key in audit_validator.DIMENSIONS}
        audit["weakness_record_count"] = counts["weakness"]
        changes[audit_path] = encoded(audit)

    unknown = needed - set(restored)
    if unknown:
        raise ValueError(f"Missing exact recovery sources for {len(unknown)} IDs: {sorted(unknown)[:5]}")
    normalized_rules = []
    for typ, rules in rules_by_type.items():
        touched = False
        for row in rules:
            legacy = {}
            if row.get("lifecycle") not in paper_validator.LIFECYCLES:
                if row.get("lifecycle") != "proposed":
                    raise ValueError(f"unsupported lifecycle conversion: {row['rule_id']}")
                legacy["lifecycle"] = row["lifecycle"]
                row["lifecycle"] = "seed"
            if row.get("confidence") not in paper_validator.CONFIDENCE:
                legacy["confidence"] = row["confidence"]
                row["confidence"] = "low"
            if legacy:
                row["legacy_schema_values"] = legacy
                row["normalization_basis"] = "Legacy proposal retained as an unpromoted seed; numeric confidence is not treated as calibrated evidence."
                normalized_rules.append(row["rule_id"])
                touched = True
        if touched:
            changes[f"artifacts/type-branches/{typ}/rules.jsonl"] = encoded(rules, jsonl=True)

    affected = set(queue) | {pid for pid in RECOVERY_SOURCES if f"artifacts/observations/{pid}.jsonl" in changes}
    for paper_id in queue:
        card_path = f"artifacts/paper-cards/{paper_id}.json"
        card = read_json(ROOT / card_path)
        language = read_json(artifact / f"language-units/{paper_id}.json")
        models = read_json(artifact / f"model-units/{paper_id}.json")
        candidate = canonical_links(card, paper_id, language, models)
        if candidate != card:
            changes[card_path] = encoded(candidate)

    for relative, raw in changes.items():
        before = (ROOT / relative).read_bytes()
        put_new(output / "before" / relative, before)
        put_new(output / "after" / relative, raw)
    for paper_id, rows in observations.items():
        put_new(output / "observation-corpus" / f"{paper_id}.jsonl", encoded(rows, jsonl=True))

    def candidate_path(relative):
        proposed = output / "after" / relative
        return proposed if proposed.exists() else ROOT / relative

    # Cache only immutable reads in this isolated candidate view. Validation
    # functions, error handling and gate requirements remain unchanged.
    original_load_jsonl = paper_validator.load_jsonl
    paper_validator.load_jsonl = functools.lru_cache(maxsize=None)(original_load_jsonl)
    results = []
    try:
        for index, paper_id in enumerate(pid for pid in [row["paper_id"] for row in progress] if pid in affected):
            typ = manifest[paper_id]["problem_type"]
            language_path = artifact / f"language-units/{paper_id}.json"
            model_path = artifact / f"model-units/{paper_id}.json"
            card_path = candidate_path(f"artifacts/paper-cards/{paper_id}.json")
            audit_path = candidate_path(f"artifacts/learning-audits/{paper_id}.json")
            observations_path = output / "observation-corpus" / f"{paper_id}.jsonl"
            language, models, card, audit = map(read_json, [language_path, model_path, card_path, audit_path])
            gates = {
                "language": language_validator.validate_record(language, None, manifest[paper_id]),
                "models": model_validator.validate_record(models, manifest[paper_id]),
                "audit": audit_validator.validate_audit(audit, language, models, card, observations[paper_id], manifest[paper_id]),
            }
            stream = io.StringIO()
            args = ["--paper-card", str(card_path), "--observations", str(observations_path),
                    "--rules", str(candidate_path(f"artifacts/type-branches/{typ}/rules.jsonl")),
                    "--manifest", str(artifact / "corpus/manifest.jsonl"),
                    "--extraction", str(artifact / f"papers/{paper_id}/extraction.json"),
                    "--observation-corpus", str(output / "observation-corpus"),
                    "--require-complete-visual-review", "--language-record", str(language_path),
                    "--model-record", str(model_path)]
            with contextlib.redirect_stdout(stream):
                paper_validator.main(args)
            gates["paper_artifacts"] = json.loads(stream.getvalue())["errors"]
            item = {"paper_id": paper_id, "pass": not any(gates.values()), "gates": gates}
            results.append(item)
            print(json.dumps({"validated": index + 1, "paper_id": paper_id, "errors": {k: len(v) for k,v in gates.items()}}), flush=True)
    finally:
        paper_validator.load_jsonl = original_load_jsonl

    summary = {
        "status": "candidate-only", "history_event_count": len(history),
        "history_sha256": digest((artifact / "transactions/history.jsonl").read_bytes()),
        "protocol_debt": sorted(debt), "unrecorded_closed_papers": sorted(missing_history),
        "queue": queue, "recovery_sources": source_provenance,
        "restored_observation_count": len(restored), "normalized_rule_ids": normalized_rules,
        "changes": {rel: {"before_sha256": digest((output / "before" / rel).read_bytes()), "after_sha256": digest(raw)} for rel,raw in changes.items()},
        "validation_results": results,
    }
    put_new(output / "report.json", encoded(summary))
    print(json.dumps({"stage": str(output), "changed_files": len(changes), "recovered_evidence": len(restored),
                      "normalized_rules": len(normalized_rules), "passed_papers": sum(r["pass"] for r in results),
                      "failed_papers": [r["paper_id"] for r in results if not r["pass"]]}, ensure_ascii=False), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    prepare(args.output.resolve())


if __name__ == "__main__":
    main()
