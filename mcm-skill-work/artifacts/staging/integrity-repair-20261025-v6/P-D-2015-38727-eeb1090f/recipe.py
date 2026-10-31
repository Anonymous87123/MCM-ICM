#!/usr/bin/env python3
"""Create-only G3 proposal links; never publish a catalog or close a paper.

Inputs are the frozen v5 text repair. Human-authored slot types and applicability
tests below make each mechanism usable without copying the source. Single-paper
proposals are not schema-v2 published language templates, which require separate
independent-paper evidence. No existing validator is relaxed.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import stage_integrity_repair as storage
import validate_language_anticopy as anticopy
import validate_paper_artifacts as paper

ROOT = storage.ROOT
PID = "P-D-2015-38727-eeb1090f"
BASE = Path("artifacts/staging/integrity-repair-20261025-v5") / PID
EXPECTED_CANDIDATE = "2886b64b9a86d9f5d7803904e7c9831ec3399a658dd5ec46b35606ee5e3d9f57"

# Each bracket label is explicitly typed. Broader semantic fields in the source
# units are retained separately; they are not silently equated with placeholders.
SLOT_TYPES = {
    1: "tool=analytical-artifact; condition=diagnosed-state; audience=decision-owner; action=proposed-response",
    2: "comparability=assumed-comparison-condition; representation=assumed-construct-relation; data condition=assumed-input-quality",
    3: "object=assessment-object; dimensions=assessment-dimensions; method section=documentation-location; aggregation=construction-rule",
    4: "data choice=input-selection; intended comparison=planned-use; missing case=uncovered-input-case; fallback=absent-alternative",
    5: "case=selected-demonstration; relevant property=substantive-eligibility; data eligibility=practical-data-condition; analysis=intended-demonstration-task",
    6: "scenario=conditional-input-setting; output=forecast-metric; direction=projected-change; horizon=future-interval",
    7: "resources=allocation-constraint; audience=decision-owner; prioritisation rule=required-decision-procedure",
    8: "concept=term-being-defined; core property=operational-meaning; scale=application-level; capacity=observable-capability",
    9: "change=proposed-or-observed-change; benefit=desired-objective; other objective=potentially-competing-objective",
    10: "representation=analytical-output; objects=cross-case-comparison-set; changes=longitudinal-difference; reference=comparison-baseline",
    11: "measures=comparable-indicators; common scale=measurement-scale; direction=score-interpretation; data convention=input-comparability-rule",
    12: "threshold=screening-trigger; warning=limited-positive-classification; stronger property=excluded-negative-certification",
    13: "indicator=defined-component; condition=represented-construct; decision need=planning-use",
    14: "classification=borrowed-categories; source basis=external-provenance; original purpose=source-context",
    15: "contrasts=purposive-case-variation; comparative use=limited-demonstration-purpose",
    16: "complication=excluded-confounder; intended comparison=analysis-protected-by-restriction",
    17: "goals=proposed-priorities; diagnosis=prior-analytical-finding; stated priorities=declared-policy-objectives",
    18: "case=target-case; reference A=first-comparator; role A=first-comparator-purpose; reference B=second-comparator; role B=second-comparator-purpose",
    19: "case=assessment-object; score=reported-result; components=reported-contributors",
    20: "present condition=current-planning-context; change=anticipated-driver; future challenge=conditional-planning-need",
    21: "external driver=outside-cause-or-constraint; outcome=affected-result; local component=locally-actionable-remainder",
    22: "favourable overall assessment=qualified-aggregate-result; specific exposure=residual-problem; targeted response=scoped-proposed-action",
    23: "diagnosed problems=prior-findings; programme=proposed-intervention; horizon=implementation-interval",
    24: "recipient=eligible-participant; support=proposed-resource; commitment=recipient-obligation; duration or condition=eligibility-term",
    25: "initiative=proposed-programme; components=specified-actions; implementation need=delivery-purpose",
    26: "outcome A=first-intended-benefit; outcome B=second-intended-benefit; outcome C=third-intended-benefit",
    27: "targeted action=bottleneck-repair; specific bottleneck=diagnosed-operational-obstacle",
    28: "resource=allocated-support; recipients=eligible-recipient-class; criteria=priority-rule",
    29: "listed inputs=scenario-changes; scenario=assumed-intervention-setting; remainder=held-fixed-inputs; horizon=scenario-interval",
    30: "overall result=qualified-projected-direction; component=non-improving-exception; driver=reported-explanation",
    31: "data condition=input-quality-limit; perturbation condition=asserted-robustness-scope",
    32: "multi-cause factor=multi-mechanism-phenomenon; category=representation-choice; other mechanism=potentially-hidden-aspect",
    33: "observed score pattern=reported-pattern; naive inference=overstrong-interpretation; contextual driver=alternative-explanation",
    34: "external driver=cross-boundary-influence; local agency=actor-control-limit; wider coordination=proposed-response-scale",
    35: "missing inputs=information-gap; weighting choice=combination-rule-to-evaluate; decision threshold=screening-rule-to-evaluate",
    36: "tool=analytical-artifact; unmet need=diagnosed-planning-need; candidate action=proposed-response; measured consequence=analytical-output-to-compute",
    37: "inputs=selected-indicators; target=target-construct",
    38: "response to persistent problem=absent-intervention; outcome=conditional-forecast-target",
    39: "programme=proposed-service; institutional partner=coordinating-organisation; front-line partners=operational-delivery-actors",
    40: "action=proposed-intervention; locations=implementation-sites; beneficiary group or coverage share=expected-reach-with-a-basis",
    41: "combined measure=aggregate-representation; critical component condition=proposed-exception-trigger; overall result=bounded-aggregate-interpretation",
}

# Positive/negative contexts test applicability, not a classifier's performance.
# They contain no additional empirical evidence or purported source experiments.
APPLICATIONS = {
    1: ("A named diagnostic output is introduced to a known user making a specific choice.", "The text promises a useful tool but names no user or decision, or treats intended utility as validated."),
    2: ("The analysis depends on explicit input and representation assumptions that can be revisited.", "Unverified assumptions are presented as measured facts or a guarantee of validity."),
    3: ("Several dimensions are reported separately and construction documentation is available.", "A dimension list is described as a single validated total without a stated aggregation rule."),
    4: ("A selected data source supports a comparison but has a named uncovered case.", "The advertised data advantage is used to claim robustness even for cases with missing inputs."),
    5: ("A demonstration case has stated substantive and practical selection reasons.", "A tractable selected case is described as representative of every possible deployment."),
    6: ("A result is conditional on a scenario and future horizon.", "A forecast is described as an observed intervention benefit or a proved causal effect."),
    7: ("Competing tasks must share a limited resource and need an explicit order.", "Scarcity alone is offered as proof that the chosen ranking is optimal."),
    8: ("A contested term needs a local operational meaning at a stated scale.", "The local operational definition is presented as the sole universally correct meaning."),
    9: ("A proposal has two explicit objectives with a possible trade-off.", "Every improvement is presumed to impose an inevitable cost without evidence."),
    10: ("One output is used for distinct between-case and over-time comparisons.", "An uncontrolled before/after difference is said to identify a causal treatment effect."),
    11: ("Scale, direction and data conventions need disclosure for comparison.", "A common numeric range is said to prove construct equivalence or equal importance."),
    12: ("A screening threshold flags a concern but a negative screen cannot certify adequacy.", "Falling below the trigger is described as proof that no relevant problem exists."),
    13: ("An indicator's represented condition and intended planning use are delimited.", "An indicator association is described as a complete causal explanation or construct validation."),
    14: ("A classification is borrowed from a documented external source.", "External provenance is treated as validation for an unrelated new use or population."),
    15: ("Deliberately varied cases illustrate how a procedure behaves.", "Purposive case variation is said to establish statistical representativeness or universal validity."),
    16: ("A selection restriction removes a named complication to clarify a limited demonstration.", "The procedure is claimed to be tested under the very complication excluded from the sample."),
    17: ("Proposed priorities can be traced to both diagnosis and declared local objectives.", "Policy alignment is substituted for evidence that the proposed action achieves its outcome."),
    18: ("Two comparators are assigned distinct interpretive roles.", "Reference cases are treated as calibrated uncertainty bounds or proof for all intermediate cases."),
    19: ("A reported result has an inspectable component decomposition.", "Component association is reported as a verified causal contribution without identification."),
    20: ("An anticipated change creates a conditional future planning need.", "A growth assumption or future distributional concern is reported as an already observed demand."),
    21: ("Part of an outcome is outside local control but another part is locally actionable.", "The existence of a local action is said to establish its size or effectiveness."),
    22: ("A favourable overall result coexists with a named remaining exposure.", "The aggregate assessment is used to erase the specific exposure or certify universal safety."),
    23: ("A programme directly addresses earlier diagnosed problems within a stated horizon.", "A recommendation list is called a costed or causally validated intervention model."),
    24: ("Support is proposed in exchange for a stated service or matching contribution.", "Recipient compliance, an unstated matching rate or achieved retention is presumed."),
    25: ("A proposal needs concrete components rather than an unexplained programme label.", "A component list alone is used as proof of feasibility, budget sufficiency or achieved impact."),
    26: ("Planned activities and intended outcomes need separate presentation.", "Intended benefits are written as measured outcomes before any evaluation."),
    27: ("A feasible local repair targets a diagnosed operational bottleneck.", "The feasibility qualifier is omitted or the proposed repair is described as completed."),
    28: ("A support allocation has an explicit recipient class and priority criteria.", "A named criterion is said to establish the optimal or equitable allocation without testing."),
    29: ("A scenario changes listed inputs and declares its fixed remainder.", "Held-fixed inputs are described as predictions that those real-world quantities will not change."),
    30: ("An overall favourable scenario has a named non-improving component.", "The favourable aggregate direction is rewritten as improvement in every component."),
    31: ("A robustness assertion must be read alongside data quality and perturbation conditions.", "A conditional prose assertion is presented as an executed sensitivity experiment."),
    32: ("A representation choice may hide one mechanism of a multi-cause phenomenon.", "The direction or magnitude of the distortion is asserted without checking it."),
    33: ("A score pattern admits a plausible contextual explanation besides the intuitive one.", "A qualifier is used to deny an inconvenient finding without any relevant alternative explanation."),
    34: ("Cross-boundary influences limit local agency and motivate a wider response scale.", "Mentioning coordination is treated as evidence that a particular governance arrangement works."),
    35: ("Stated limitations can be turned into finite future evaluation tasks.", "An unimplemented extension is claimed to improve accuracy solely because it adds complexity."),
    37: ("Input selection is justified by a stated relation whose evidence strength is limited.", "A believed or observed association is silently upgraded into an established causal driver."),
    38: ("A persistent problem motivates an explicit no-action expectation.", "A prose no-action expectation is presented as a simulated counterfactual or measured treatment effect."),
    39: ("A proposed service needs named coordinating and front-line delivery partners.", "Naming partners is treated as evidence of consent, capacity or committed funding."),
    40: ("Implementation sites have an inspectable link to expected beneficiary reach.", "Small site size or a small number of sites is said to prove high coverage or low cost by itself."),
    41: ("An aggregate can hide a critical component and an additional check is proposed.", "The proposed trigger is described as a calibrated implemented algorithm with validated improvement."),
}


def slot_records(unit):
    number = int(unit["language_unit_id"].rsplit("-", 1)[1])
    definitions = dict(item.split("=", 1) for item in SLOT_TYPES[number].split("; "))
    placeholders = list(dict.fromkeys(re.findall(r"\[([^\[\]]+)\]", unit["reusable_pattern"])))
    if set(placeholders) != set(definitions):
        raise ValueError(f"typed slot mismatch for {unit['language_unit_id']}")
    return [{"name": re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_"),
             "placeholder": name, "semantic_type": definitions[name], "required": True}
            for name in placeholders]


def identity(pattern_id):
    suffix = pattern_id.removeprefix("CP-D-2015-38727-REPAIR-")
    if not re.fullmatch(r"\d{2}", suffix):
        raise ValueError("unexpected proposal identity")
    return f"R-D-LANG-38727-REPAIR-{suffix}"


def assemble(record):
    groups = defaultdict(list)
    for unit in record["units"]:
        targets = unit.get("candidate_pattern_ids", [])
        if len(targets) != 1:
            raise ValueError("each unit needs exactly one candidate disposition")
        groups[targets[0]].append(unit)
    patterns, observations, mapping, rules = [], [], [], []
    for candidate_id, units in groups.items():
        first = units[0]
        number = int(candidate_id.rsplit("-", 1)[1])
        appropriate, forbidden = APPLICATIONS[number]
        rule_id = identity(candidate_id)
        function = first["function"]
        order = first["information_order"]
        if number == 1:
            function = "Connect a named analytical deliverable to a downstream decision, retaining distinct Summary-opening and Introduction-closing variants."
            order = ["analytical deliverable", "intended operational use", "audience decision"]
        variants, occurrences, examples, evidence_ids = [], [], [], []
        for unit in units:
            uid = unit["language_unit_id"]
            obs_id = "O-D-2015-38727-REPAIR-" + uid.rsplit("-", 1)[1]
            evidence_ids.append(obs_id)
            variants.append({"language_unit_id": uid, "chapter": unit["chapter"],
                             "function": unit["function"], "frame": unit["reusable_pattern"],
                             "information_order": unit["information_order"], "slots": slot_records(unit),
                             "semantic_fields": unit["g3"]["slots"], "source_variants": unit["g3"]["variants"],
                             "boundary": unit["g3"]["boundary"],
                             "voice": unit["features"]["voice"], "tense": unit["features"]["tense"],
                             "modality": unit["features"]["modality"]})
            for occurrence in unit["occurrences"]:
                occurrences.append({"language_unit_id": uid, **copy.deepcopy(occurrence)})
            for example in unit["features"]["original_instantiations"]:
                examples.append({"language_unit_id": uid, "text": example,
                                 "status": "invented-illustration-not-source-evidence"})
            observations.append({"schema_version": 1, "observation_id": obs_id,
                "paper_id": PID, "problem_type": "D", "year": "2015", "page": unit["page"],
                "section": unit["section"], "evidence_class": "O", "dimension": "language",
                "source_basis": {"short_excerpt": unit["source_excerpt"], "occurrences": unit["occurrences"],
                                 "language_unit_id": uid, "source_sha256": record["source_sha256"]},
                "interpretation": unit["function"], "applicability": appropriate,
                "counterevidence": unit["g3"]["boundary"], "confidence": "low",
                "candidate_rule_ids": [rule_id], "candidate_pattern_id": candidate_id,
                "review_status": "draft-not-live-evidence"})
            mapping.append({"language_unit_id": uid, "candidate_pattern_id": candidate_id,
                            "candidate_rule_id": rule_id, "observation_id": obs_id,
                            "physical_page": unit["page"], "printed_page": unit["printed_page"],
                            "disposition": "opens-candidate" if unit is first else "supports-same-paper-candidate-variant"})
        pattern = {"candidate_pattern_id": candidate_id, "function": function,
                   "information_order": order, "variants": variants,
                   "source_occurrences": occurrences, "occurrence_count": len(occurrences),
                   "source_papers": [PID], "independent_paper_count": 1,
                   "source_unit_count": len(units), "original_instantiations": examples,
                   "boundary": list(dict.fromkeys(b for u in units for b in u["g3"]["boundary"])),
                   "applicability_test": {"appropriate": appropriate, "forbidden": forbidden,
                                          "review": "root-authored semantic applicability cases, not classifier test data"},
                   "disposition": "opens-single-paper-candidate; not a published template or promoted skill rule",
                   "judge_relevance": {"status": "unknown", "basis": "No judging evidence is inferred from an award-paper writing routine."}}
        patterns.append(pattern)
        rules.append({"schema_version": 1, "rule_id": rule_id, "problem_type": "D", "dimension": "language",
            "lifecycle": "seed", "statement": function, "applicability": [appropriate],
            "inapplicable": [forbidden], "procedure": ["Check applicability and evidence strength before writing."] +
                ["Preserve semantic move: " + move for move in order] +
                ["Choose a documented variant and replace every typed slot.",
                 "Carry the scope and modality boundary into the new context.",
                 "Use new content; never reuse source clauses or case facts."],
            "positive_pattern": variants[0]["frame"], "forbidden": [forbidden] + pattern["boundary"],
            "evidence_ids": evidence_ids, "source_papers": [PID], "source_count": 1,
            "confidence": "low", "required_tests": ["source occurrence binding", "function/order preservation",
                "typed slot coverage", "appropriate and forbidden context review", "original example retention",
                "eight-content-word anti-copy", "independent-paper-count audit"],
            "candidate_pattern_id": candidate_id, "information_order": order,
            "variant_records": variants, "original_instantiations": examples,
            "review_status": "proposal-not-installed", "cross_paper_support_claimed": False})
    return {"patterns": patterns, "observations": observations, "mapping": mapping, "rules": rules}


def validate_links(record, package):
    errors = []
    def unique(items, field):
        index = {item[field]: item for item in items}
        if len(index) != len(items): errors.append("duplicate " + field)
        return index
    units = unique(record["units"], "language_unit_id")
    patterns = unique(package["patterns"], "candidate_pattern_id")
    observations = unique(package["observations"], "observation_id")
    rules = unique(package["rules"], "rule_id")
    mapping = unique(package["mapping"], "language_unit_id")
    if set(mapping) != set(units): errors.append("unit mapping not bijective")
    for uid, link in mapping.items():
        if uid not in units: continue
        u = units[uid]
        p = patterns.get(link["candidate_pattern_id"])
        o = observations.get(link["observation_id"])
        r = rules.get(link["candidate_rule_id"])
        if not p or not o or not r:
            errors.append("dangling mapping " + uid); continue
        if link["candidate_pattern_id"] != u["candidate_pattern_ids"][0]: errors.append("pattern remap " + uid)
        if o.get("candidate_rule_ids") != [r["rule_id"]] or o["observation_id"] not in r["evidence_ids"]:
            errors.append("observation/rule backlink " + uid)
        if o.get("page") != u["page"] or link["physical_page"] != u["page"]:
            errors.append("page drift " + uid)
        if o.get("source_basis", {}).get("occurrences") != u["occurrences"]:
            errors.append("observation witness drift " + uid)
        expected_occurrences = [{"language_unit_id": uid, **copy.deepcopy(x)} for x in u["occurrences"]]
        if [x for x in p["source_occurrences"] if x["language_unit_id"] == uid] != expected_occurrences:
            errors.append("pattern occurrence loss " + uid)
        variants = [x for x in p["variants"] if x["language_unit_id"] == uid]
        if len(variants) != 1:
            errors.append("variant coverage " + uid); continue
        variant = variants[0]
        for target, source in [("frame", "reusable_pattern"), ("function", "function"), ("information_order", "information_order")]:
            if variant[target] != u[source]: errors.append("variant lost " + target + " " + uid)
        if variant["slots"] != slot_records(u): errors.append("slot loss " + uid)
        actual_examples = [x["text"] for x in p["original_instantiations"] if x["language_unit_id"] == uid]
        if actual_examples != u["features"]["original_instantiations"]: errors.append("example loss " + uid)
        if variant["boundary"] != u["g3"]["boundary"]: errors.append("boundary loss " + uid)
    for p in patterns.values():
        if p["source_papers"] != [PID] or p["independent_paper_count"] != 1:
            errors.append("inflated pattern support " + p["candidate_pattern_id"])
        if p["occurrence_count"] != len(p["source_occurrences"]): errors.append("occurrence count drift")
        members = [uid for uid, link in mapping.items() if link["candidate_pattern_id"] == p["candidate_pattern_id"]]
        if p["source_unit_count"] != len(members) or sorted(x["language_unit_id"] for x in p["variants"]) != sorted(members):
            errors.append("pattern member drift " + p["candidate_pattern_id"])
        if not p["applicability_test"]["appropriate"] or not p["applicability_test"]["forbidden"]:
            errors.append("missing boundary test")
    for r in rules.values():
        if paper.missing_fields(r, paper.REQUIRED_RULE_FIELDS): errors.append("missing rule schema fields")
        if r["lifecycle"] != "seed" or r["confidence"] != "low" or r["source_papers"] != [PID] or r["source_count"] != 1:
            errors.append("unjustified rule promotion " + r["rule_id"])
        if r.get("cross_paper_support_claimed") is not False: errors.append("unjustified cross-paper claim")
        p = patterns.get(r["candidate_pattern_id"])
        if not p: errors.append("unknown rule pattern"); continue
        for field, expected in [("statement", p["function"]), ("information_order", p["information_order"]),
                                ("variant_records", p["variants"]), ("original_instantiations", p["original_instantiations"])]:
            if r[field] != expected: errors.append("rule lost " + field)
        expected_evidence = {o["observation_id"] for o in observations.values() if o["candidate_pattern_id"] == p["candidate_pattern_id"]}
        if set(r["evidence_ids"]) != expected_evidence: errors.append("evidence link loss")
    for o in observations.values():
        if paper.missing_fields(o, paper.REQUIRED_OBSERVATION_FIELDS): errors.append("missing observation schema fields")
        if (o["paper_id"], o["problem_type"], o["year"], o["dimension"], o["evidence_class"], o["confidence"]) != (PID, "D", "2015", "language", "O", "low"):
            errors.append("observation identity drift")
    if len(patterns) != len(rules) or len(units) != len(observations): errors.append("compressed or orphaned proposal")
    return errors


def build(output):
    output.mkdir(parents=True, exist_ok=False)
    storage.put_new(output / "recipe.py", Path(__file__).read_bytes())
    source = ROOT / BASE
    verification = storage.read_json(source / "verification-summary.json")
    for name, expected in verification["candidate_files"].items():
        if storage.digest((source / name).read_bytes()) != expected:
            raise ValueError("frozen v5 file changed: " + name)
    record_path = source / "language-units.draft.json"
    if storage.digest(record_path.read_bytes()) != EXPECTED_CANDIDATE:
        raise ValueError("unexpected source generation")
    validation = storage.read_json(source / "validation.json")
    frozen = validation["input_sha256"].copy()
    branch_path = ROOT / "artifacts/type-branches/D/rules.jsonl"
    frozen[str(branch_path)] = storage.digest(branch_path.read_bytes())
    for path in [source / name for name in verification["candidate_files"]] + [source / "verification-summary.json"]:
        frozen[str(path)] = storage.digest(path.read_bytes())
    if any(storage.digest(Path(path).read_bytes()) != expected for path, expected in frozen.items()):
        raise ValueError("input generation has changed")
    record = storage.read_json(record_path)
    if record["paper_id"] != PID or record["review_status"] != "draft": raise ValueError("not the expected draft")
    package = assemble(record)
    errors = validate_links(record, package)
    if errors: raise ValueError(str(errors))
    live_rules = storage.read_jsonl(branch_path)
    if {r["rule_id"] for r in live_rules} & {r["rule_id"] for r in package["rules"]}:
        raise ValueError("candidate rule id collides with live branch")
    live_ids = {o["observation_id"] for o in storage.read_jsonl(ROOT / f"artifacts/observations/{PID}.jsonl")}
    if live_ids & {o["observation_id"] for o in package["observations"]}:
        raise ValueError("candidate observation id collides with live evidence")
    pages = [ROOT / f"artifacts/papers/{PID}/text/pages/page-{n:04d}.txt" for n in range(1, 20)]
    profile = anticopy.build_source_profile("\n\f\n".join(p.read_text(encoding="utf-8") for p in pages), 8)
    scans = [anticopy.scan_unit_with_profile({"language_unit_id": p["candidate_pattern_id"],
              "features": {"original_instantiations": [e["text"] for e in p["original_instantiations"]]}},
              profile, 8, set(record["source_specific_terms"])) for p in package["patterns"]]
    if any(s["result"] != "pass" for s in scans): raise ValueError("candidate anti-copy failed")
    registry = {"schema": "single-paper-g3-proposal-registry-v1", "paper_id": PID,
        "source_sha256": record["source_sha256"], "review_status": "draft-not-published-catalog",
        "patterns": package["patterns"], "published_catalog_acceptance_claimed": False,
        "independent_support_requirement": "A published schema-v2 template needs evidence from at least two independent content entities; this pack has one."}
    generated = {"pattern-registry.draft.json": storage.encoded(registry),
                 "unit-pattern-rule-map.draft.json": storage.encoded(package["mapping"]),
                 "language-observations.draft.jsonl": storage.encoded(package["observations"], jsonl=True),
                 "language-rules.draft.jsonl": storage.encoded(package["rules"], jsonl=True)}
    for name, raw in generated.items(): storage.put_new(output / name, raw)
    if any(storage.digest(Path(path).read_bytes()) != expected for path, expected in frozen.items()):
        raise ValueError("live/input bytes changed during build; output is not certified")
    language_rules = [r for r in live_rules if r.get("dimension") == "language"]
    report = {"paper_id": PID, "status": "linked-proposals-not-paper-closure", "input_sha256": frozen,
        "source_candidate_sha256": EXPECTED_CANDIDATE, "language_units": len(record["units"]),
        "patterns": len(package["patterns"]), "observations": len(package["observations"]),
        "seed_rules": len(package["rules"]), "mappings": len(package["mapping"]),
        "source_occurrences": sum(p["occurrence_count"] for p in package["patterns"]),
        "original_examples": sum(s["example_count"] for s in scans),
        "maximum_shared_content_run": max(s["maximum_shared_content_run"] for s in scans),
        "link_errors": errors, "anticopy_results": scans,
        "output_sha256": {name: storage.digest(raw) for name, raw in generated.items()},
        "frozen_recipe_sha256": storage.digest((output / "recipe.py").read_bytes()),
        "existing_D_branch_review": {"language_rule_count": len(language_rules),
            "write_prefixed_statements": sum(r.get("statement", "").startswith("Write ") for r in language_rules),
            "lifecycle_counts": dict(Counter(r["lifecycle"] for r in language_rules)),
            "broad_related_rules": ["R-D-WRITE-001", "R-D-CLAIM-001"],
            "decision": "No broad-rule support count borrowed. Precise mechanisms remain separate single-paper proposals. Existing seed source clauses are not approved by this metadata review."},
        "remaining": ["Full paper integrity/layout/model/visual gates remain open.",
            "No cross-paper corroboration, live branch installation, rule promotion or transaction append.",
            "Do not replace published catalog acceptance with proposal-link validation."]}
    storage.put_new(output / "link-verification.json", storage.encoded(report))
    print(json.dumps({k: v for k, v in report.items() if k not in {"input_sha256", "anticopy_results", "output_sha256", "existing_D_branch_review"}}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()
