#!/usr/bin/env python3
"""Correct prose attribution and modality in a new create-only candidate pack.

No live artifacts, history, progress, formula or visual statuses are modified.
The full existing language validator remains authoritative and may still fail
for missing quantitative layouts. Semantic attribution is root-reviewed, not
proved by automated consistency checks or by passing tests.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

import stage_d38727_language_links as links
import stage_integrity_repair as storage
import validate_language_anticopy as anticopy
import validate_language_units as language

ROOT = storage.ROOT
PID = links.PID
V5 = Path("artifacts/staging/integrity-repair-20261025-v5") / PID
V8 = Path("artifacts/staging/integrity-repair-20261025-v8") / PID
V10 = Path("artifacts/staging/integrity-repair-20261025-v10") / PID
V11 = Path("artifacts/staging/integrity-repair-20261029-v11") / PID

SLOT_TYPES = dict(links.SLOT_TYPES)
SLOT_TYPES.update({
    3: "object=assessment-object; dimensions=assessment-dimensions; method section=documentation-location; component construction=dimension-specific-construction-rule",
    30: "scenario=conditional-input-setting; overall result=qualified-projected-direction; component=non-improving-exception; driver=reported-explanation",
    36: "tool=analytical-artifact; unmet need=diagnosed-planning-need; candidate action=proposed-response; analytical consequence=prospective-computed-or-justified-output",
    37: "inputs=selected-indicators; relation=author-stated-influence-or-association; target=target-construct",
    39: "programme component=scoped-proposed-service; institutional partner=coordinating-organisation; front-line partners=operational-delivery-actors",
})

REVISIONS = {
    3: {
        "reason": "Aggregation can imply a single total; the retained source describes dimensions and their construction.",
        "observed_action": "Name the dimensions and direct the reader to their construction.",
        "editorial_boundary": "Do not invent a single aggregate scalar. This is a reuse guardrail, not a claim that the authors explicitly warned against one.",
        "edits": {"reusable_pattern": "We assess [object] across [dimensions]; [method section] explains [component construction]."},
    },
    15: {
        "reason": "The old function attributed a distinction from universal validation to authors who instead overclaimed universal applicability.",
        "observed_action": "State the diversity-based case-selection rationale and the intended comparison purpose.",
        "editorial_boundary": "Purposive variation is not universal validation. The source does not itself enforce this boundary: p6 continues into p7's robust-and-universally-applicable assertion.",
        "edits": {"function": "State why deliberately varied cases were selected and what comparison they are intended to illustrate."},
    },
    24: {
        "reason": "The shared order imposed a retention effect on matching funds; the education purpose paragraph also has an ambiguous antecedent.",
        "observed_action": "Describe proposed support conditional on a service commitment or local matching contribution.",
        "editorial_boundary": "The source names retention intentions but does not unambiguously assign all of them to the service clause. The matching-fund variant has neither a stated service duration nor a stated matching rate.",
        "edits": {
            "reusable_pattern": "The proposed [support] for [recipient] is conditional on [commitment] under [duration or condition].",
            "information_order": ["support instrument", "eligible recipient", "stated commitment or contribution", "stated duration or participation condition"],
        },
        "semantic_slots": ["recipient", "support", "commitment or contribution", "stated eligibility condition"],
    },
    30: {
        "reason": "The frame and both standalone invented examples did not explicitly mark the scenario/projection status required by this candidate's function.",
        "observed_action": "Report the result after assumed updates and preserve the named non-improving component.",
        "editorial_boundary": "Explicit scenario wording in the reusable frame and illustrations is a safe adaptation, not proof that the paper established policy efficacy.",
        "edits": {"reusable_pattern": "Under [scenario], [overall result] is projected to improve, except for [component], which remains affected by [driver]."},
        "examples": [
            "Under the extra-session scenario, most conflicts are projected to decline, but ownership fields remain unresolved where the source register is missing.",
            "Under the revised-route scenario, most detours are projected to shorten; the courtyard entrance still requires the long path because its connecting stairway remains closed.",
        ],
    },
    36: {
        "reason": "Measured consequence can falsely suggest an observed policy effect in an Introduction that states an intended analytical use.",
        "observed_action": "Connect unmet needs and policy measures to the consequence the analytical tool is intended to represent.",
        "editorial_boundary": "Analytical consequence may be prospective, computed or justified; the Introduction does not certify an observed treatment effect.",
        "edits": {
            "reusable_pattern": "The [tool] connects [unmet need] and [candidate action] through [analytical consequence].",
            "information_order": ["operational meaning", "unmet need", "candidate action", "analytical consequence", "construction handoff"],
        },
        "semantic_slots": ["tool", "unmet need", "candidate action", "analytical consequence", "construction section"],
    },
    37: {
        "reason": "The source qualifies a believed relation and says influence or correlate; it does not explicitly articulate the candidate's additional causal disclaimer.",
        "observed_action": "Qualify the claimed relevance of inputs with belief and influence-or-association language.",
        "editorial_boundary": "Do not upgrade a believed relation into established causation. The negative causal disclaimer in the invented examples is editorial scaffolding, not an additional source utterance.",
        "edits": {
            "function": "Qualify the claimed relevance of selected inputs using belief and influence-or-association language.",
            "reusable_pattern": "The [inputs] are included for their reported [relation] to [target].",
        },
    },
    39: {
        "reason": "This program refers to the public-health education campaign, not every infrastructure proposal in the section.",
        "observed_action": "Name institutional and front-line delivery partners for the health-education campaign.",
        "editorial_boundary": "The source does not assign those partners ownership of every infrastructure action, or establish consent, capacity or funding.",
        "edits": {
            "function": "Name coordinating and front-line partners for a specific proposed programme component.",
            "reusable_pattern": "[programme component] will be delivered with [institutional partner] and [front-line partners].",
        },
    },
}


def revise(record):
    result = copy.deepcopy(record)
    notes = []
    for unit in result["units"]:
        number = int(unit["language_unit_id"].rsplit("-", 1)[1])
        if number not in REVISIONS:
            continue
        revision = REVISIONS[number]
        before = copy.deepcopy(unit)
        unit.update(copy.deepcopy(revision["edits"]))
        if "examples" in revision:
            unit["features"]["original_instantiations"] = revision["examples"][:]
        unit["g3"]["stable_function"] = unit["function"]
        unit["g3"]["order"] = unit["information_order"][:]
        if "semantic_slots" in revision:
            unit["g3"]["slots"] = revision["semantic_slots"][:]
        unit["g3"]["boundary"].append(revision["editorial_boundary"])
        unit["prohibited_generalizations"].append(revision["editorial_boundary"])
        replacements = {
            "stable function: ": unit["function"],
            "order: ": " > ".join(unit["information_order"]),
            "slots: ": "; ".join(unit["g3"]["slots"]),
        }
        unit["reusable_elements"] = [
            next((prefix + text for prefix, text in replacements.items() if old.startswith(prefix)), old)
            for old in unit["reusable_elements"]]
        notes.append({"language_unit_id": unit["language_unit_id"],
                      **{k: revision[k] for k in ("reason", "observed_action", "editorial_boundary")},
                      "before": before, "after": copy.deepcopy(unit)})
    return result, notes


def verify_preservation(before, after, notes):
    if len(before["units"]) != len(after["units"]):
        raise ValueError("unit count changed")
    changed = set()
    for old, new in zip(before["units"], after["units"]):
        number = int(old["language_unit_id"].rsplit("-", 1)[1])
        for field in ("language_unit_id", "page", "printed_page", "section", "chapter",
                      "source_excerpt", "occurrences", "candidate_pattern_ids", "disposition"):
            if old[field] != new[field]:
                raise ValueError("source/identity/support field changed: " + field)
        if old != new:
            changed.add(number)
        if number not in REVISIONS and old != new:
            raise ValueError("unreviewed unit changed")
        expected = REVISIONS.get(number, {}).get("examples", old["features"]["original_instantiations"])
        if new["features"]["original_instantiations"] != expected:
            raise ValueError("unreviewed example changed")
    if changed != set(REVISIONS) or len(notes) != len(REVISIONS):
        raise ValueError("revision coverage mismatch")
    if any(new["g3"]["cross_paper_support_count"] != old["g3"]["cross_paper_support_count"]
           for old, new in zip(before["units"], after["units"])):
        raise ValueError("support count changed")


def build(output):
    output.mkdir(parents=True, exist_ok=False)
    storage.put_new(output / "recipe.py", Path(__file__).read_bytes())
    bound = {}

    def read(path):
        path = ROOT / path
        raw = path.read_bytes()
        bound[str(path)] = storage.digest(raw)
        return raw

    previous = json.loads(read(V11 / "content-handoffs.draft.json"))
    for path, expected in previous["input_sha256"].items():
        if storage.digest(Path(path).read_bytes()) != expected:
            raise ValueError("frozen content input changed")
        bound[path] = expected
    original = json.loads(read(V5 / "language-units.draft.json"))
    record, notes = revise(original)
    verify_preservation(original, record, notes)
    package = links.assemble(record, SLOT_TYPES)
    errors = links.validate_links(record, package, SLOT_TYPES)
    if errors:
        raise ValueError(str(errors))
    # Integrity and byte matching only; do not inspect or certify mathematical notation.
    fresh = read(V10 / "fresh-native-full.bin").decode("utf-8")
    decoded = read(V10 / "decoded-full.txt").decode("utf-8")
    scans = {}
    for name, source in [("fresh-native", fresh), ("decoded-historical", decoded)]:
        scans[name] = links.scan_examples(record, anticopy.build_source_profile(source, 8))
        if any(item["result"] != "pass" for item in scans[name]):
            raise ValueError("anti-copy failed: " + name)
    manifest = language.find_manifest_record(ROOT / "artifacts/corpus/manifest.jsonl", PID)
    full_errors = language.validate_record(record, manifest_record=manifest)
    original_errors = language.validate_record(original, manifest_record=manifest)
    if full_errors != original_errors:
        raise ValueError("unexpected full-record gate drift: " + str(full_errors))
    outputs = {
        "language-units.draft.json": storage.encoded(record),
        "pattern-registry.draft.json": storage.encoded({"schema": "single-paper-g3-proposal-registry-v1",
            "paper_id": PID, "review_status": "draft-not-published-catalog", "patterns": package["patterns"],
            "published_catalog_acceptance_claimed": False}),
        "unit-pattern-rule-map.draft.json": storage.encoded(package["mapping"]),
        "language-observations.draft.jsonl": storage.encoded(package["observations"], jsonl=True),
        "language-rules.draft.jsonl": storage.encoded(package["rules"], jsonl=True),
        "attribution-review.json": storage.encoded({"reviewer": "root; no subagent",
            "scope": "All41 candidate functions, frames, boundaries and82 invented examples read; no formula/visual verification.",
            "reviewed_units": [{"language_unit_id": u["language_unit_id"],
                "disposition": "corrected-with-explicit-attribution" if int(u["language_unit_id"].rsplit("-", 1)[1]) in REVISIONS else "no-corrective-edit-identified"}
                for u in record["units"]], "revisions": notes,
            "limits": "A root editorial review, not independent corroboration or formal G2/G4 acceptance."}),
    }
    read(Path("scripts/stage_d38727_language_links.py"))
    read(Path("scripts/validate_language_anticopy.py"))
    read(Path("scripts/validate_language_units.py"))
    for path, expected in bound.items():
        if storage.digest(Path(path).read_bytes()) != expected:
            raise ValueError("input changed during attribution correction")
    for name, raw in outputs.items():
        storage.put_new(output / name, raw)
    report = {
        "paper_id": PID, "status": "attribution-corrected-proposal-not-paper-closure",
        "corrected_units": len(notes), "unchanged_units": len(record["units"]) - len(notes),
        "language_units": len(record["units"]), "patterns": len(package["patterns"]),
        "source_occurrences": sum(len(u["occurrences"]) for u in record["units"]),
        "original_examples": sum(len(u["features"]["original_instantiations"]) for u in record["units"]),
        "revised_example_texts": 2, "unchanged_example_texts": 80,
        "source_support": "one paper only; no new source occurrences or independent support",
        "link_errors": errors, "typed_slot_definitions": SLOT_TYPES,
        "full_language_gate_status": "pass" if not full_errors else "fail",
        "full_language_gate_errors": full_errors,
        "gate_failures_unchanged_from_v5": full_errors == original_errors,
        "anticopy_results": scans,
        "maximum_shared_content_run": max(s["maximum_shared_content_run"] for seq in scans.values() for s in seq),
        "input_sha256": bound,
        "output_sha256": {name: storage.digest(raw) for name, raw in outputs.items()},
        "frozen_recipe_sha256": storage.digest((output / "recipe.py").read_bytes()),
        "not_claimed": ["published catalog acceptance", "full-scope saturation", "quantitative layouts",
                        "formula or visual verification", "live branch installation", "paper closure"],
    }
    storage.put_new(output / "verification.json", storage.encoded(report))
    print(json.dumps({k: v for k, v in report.items() if k not in {
        "typed_slot_definitions", "anticopy_results", "input_sha256", "output_sha256"}}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()
