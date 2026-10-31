#!/usr/bin/env python3
"""Create-only opening-prose stage for the user-authorized text-first queue.

Human-reviewed prose mechanisms are serialized below. No formula/image review,
installation, progress update, rule promotion or transaction append is performed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import validate_language_anticopy as anticopy
import validate_language_units as language

ROOT = Path(__file__).resolve().parents[1]
PID = "P-D-2015-38996-1efe10af"
SHA = "1efe10af33686734c9dc12c9b8c9ac65446a5e759d61a48ccfffed2365117ac2"
SOURCE_TERMS = ["nepal", "nepalese", "france", "china", "arima", "critic", "ecological", "footprint", "sustainability"]


def spec(chapter, spans, function, frame, order, slots, variants, boundary, examples,
         modality="author-stated purpose or method, not verified efficacy", short_span=None):
    return dict(chapter=chapter, spans=spans, function=function, frame=frame,
                order=order.split(" > "), slots=slots.split("; "),
                variants=variants.split("; "), boundary=boundary,
                examples=examples, modality=modality, short_span=short_span)


# Physical page, one-based inclusive text lines, printed section, local role.
MECHANISMS = [
    spec("abstract", [(1, 20, 23, "Summary", "concept decomposition")],
         "Turn a broad evaluation concept into explicitly named dimensions before describing construction.",
         "We distinguish [dimension A] from [dimension B] when assessing [object].",
         "evaluation purpose > concept interpretation > named dimensions",
         "object; dimension A; dimension B",
         "purpose-first dimensional split",
         "A named split is a representation choice, not proof of exhaustive coverage or independent dimensions.",
         ["The collection review separates missing records from conflicting descriptions before assigning a repair category.",
          "For each entrance, we distinguish whether a route exists from how long the route takes."]),
    spec("abstract", [(1, 23, 25, "Summary", "methods hand their output to indices")],
         "Name operations together with their intended output rather than present an isolated method inventory.",
         "[operations] produce [intermediate output] for [next stage].",
         "representation choice > named operations > intermediate output",
         "operations; intermediate output; next stage",
         "construction overview linking operations to output",
         "The Summary names two weighting approaches and two overall indices, but does not establish a separate one-to-one method-to-index assignment. No calculation is verified here.",
         ["The duplicate check supplies a set of conflicting identifiers to the manual reconciliation stage.",
          "Route enumeration yields candidate paths that the access review can inspect individually."]),
    spec("abstract", [(1, 31, 35, "Summary", "case verdicts and comparison claim")],
         "Make a demonstration concrete by partitioning the named example set into contrasting reported verdicts.",
         "Within [examined set], [group A] receives [verdict A], whereas [group B] receives [verdict B].",
         "demonstration set > contrasting verdict groups > stated comparison",
         "examined set; group A; group B; verdict A; verdict B",
         "compressed contrast within a named demonstration",
         "The verdicts and superiority claim remain author reports. A demonstration set is not every possible case, and its reported outcome is not independently accepted by this text review.",
         ["Among the inspected cabinets, the eastern pair had complete labels, while the remaining cabinets required a second check.",
          "In the trial routes, the courtyard entrance remained reachable; the two basement entrances did not."]),
    spec("abstract", [(1, 37, 40, "Summary", "without versus with intervention"),
                      (4, 3, 13, "1.2. Our Work", "reference forecast then intervention simulation")],
         "Separate a reference forecast from the analysis of proposed interventions and state their different roles.",
         "We first examine [reference case]; [intervention procedure] then explores [changed case].",
         "selected case > reference projection > intervention projection > decision use",
         "reference case; reference procedure; intervention procedure; changed case; decision use",
         "without/with contrast in Summary; sequential reference-to-intervention roadmap",
         "Different procedures are named for the two cases. This alone does not show a matched counterfactual, comparable error, or that only intervention status changes.",
         ["The timetable audit first describes access under the current opening hours; a separate scheduling exercise explores extended evening access.",
          "We use the existing catalogue to estimate the review backlog, then examine how an extra verification desk could change its trajectory."]),
    spec("abstract", [(1, 38, 40, "Summary", "data limitation motivates estimation")],
         "Put a concrete data limitation immediately before the chosen estimation response.",
         "Because [data limitation], we estimate [unknowns] using [procedure].",
         "data limitation > affected unknowns > chosen estimation response > documentation",
         "data limitation; unknowns; estimation procedure; documentation location",
         "because-limitation to method response",
         "This is the authors' stated response, not proof that the named procedure remedies scarcity or meets its own conditions. Do not invent a failed trial or rejected alternatives.",
         ["Several registers omit the transfer date, so the draft chronology uses bounded intervals rather than a single reconstructed day.",
          "With only weekly headcounts available, the preliminary access review uses weekly blocks and leaves hourly demand unresolved."]),
    spec("abstract", [(1, 41, 44, "Summary", "context and forecast inform proposed plan"),
                      (4, 3, 7, "1.2. Our Work", "analysis hands off to programme")],
         "Hand a stated case diagnosis and forecast into a proposed action plan instead of appending an unrelated recommendation list.",
         "Using [case findings] and [forecast], we propose [plan] for [decision context].",
         "case context > analytical findings > proposed plan > implementation audience",
         "case findings; forecast; proposed plan; decision context",
         "context-and-results handoff in Summary; baseline-results handoff in Introduction",
         "A prose handoff does not certify feasibility, causal response, or that every recommendation has a traceable supporting result.",
         ["The missing-label survey and the expected intake guide a staged catalogue repair programme for the storage team.",
          "The access review combines the reported closures with next term's room schedule to propose where temporary entrances are needed."]),
    spec("abstract", [(1, 41, 44, "Summary", "best option scoped to simulation"),
                      (4, 9, 13, "1.2. Our Work", "option simulations inform effectiveness selection")],
         "Attach an option-selection claim to the evaluation procedure from which the claim is reported.",
         "Among [examined options], [option] performs best on [criterion] under [evaluation setting].",
         "evaluated options > stated evaluation > comparative selection > implementation use",
         "examined options; option; criterion; evaluation setting",
         "best-performing option qualified by simulation in Summary; simulation-to-selection roadmap",
         "The Summary explicitly confines its best-programme claim to simulation results. The Introduction announces selection but does not independently demonstrate a ranking. This review accepts neither the numerical comparison nor a universal winner.",
         ["Within the trial roster, the staggered desk arrangement left the fewest unresolved requests during the recorded afternoon session.",
          "Of the tested label layouts, the large-print version was read fastest in this small display exercise; other viewing distances were not examined."]),
    spec("introduction", [(3, 24, 30, "1.1. Background", "practical tension becomes an evaluation gap")],
         "Move from conflicting real-world demands to the specific decision that an inadequate evaluation method cannot yet support.",
         "[competing demands] create [practical difficulty]; without [evaluation capability], [audience] cannot reliably [decision].",
         "competing demands > operational difficulty > evaluation gap > blocked allocation decision",
         "competing demands; practical difficulty; evaluation gap; audience; allocation decision",
         "real-world tension followed by a decision-capability gap",
         "The causal and institutional descriptions remain source claims. Do not treat a topical opener or the word 'Unfortunately' as the mechanism, or invent empirical proof of the gap.",
         ["The archive must accept new deposits while clearing older boxes, yet its register does not distinguish urgent repairs from routine relabelling.",
          "Visitors need evening access, but the building team must also reserve maintenance periods; the current log cannot show which closures cause the largest detours."],
         short_span=(3, 26, 30)),
    spec("introduction", [(3, 39, 43, "1.2. Our Work", "retained concept with expanded evaluation scope")],
         "Introduce an extension as a response to a stated limitation while retaining the identifiable starting approach.",
         "We retain [starting approach] but extend [scope] to address [stated omission].",
         "evaluation purpose > identifiable starting approach > stated limitation > expanded scope",
         "starting approach; stated omission; expanded scope",
         "drawback-led extension in the work roadmap",
         "The paragraph says drawbacks were identified but does not report a failed experiment or a controlled superiority test. Later evidence must establish the actual omission and the claimed benefit.",
         ["We keep the shelf register as the inventory backbone but add unresolved ownership links that its current fields cannot represent.",
          "The route list remains the starting record, with temporary closures added because a permanently open map misses them."]),
    spec("introduction", [(3, 43, 47, "1.2. Our Work", "representation chosen for readers")],
         "Explain a presentation choice through the audience's interpretive needs.",
         "We present [output] as [representation] so [audience] can interpret [decision-relevant meaning].",
         "reported output > representation choice > audience constraint > intended interpretation",
         "output; representation; audience; intended interpretation",
         "so-that audience rationale beside a representation choice",
         "This captures a prose rationale, not acceptance of the actual graphic or evidence of comprehension. Do not infer that all readers understood it or that the visual review is complete.",
         ["The review sheet groups unresolved records by room so the move coordinator can locate the next batch without reading the full catalogue.",
          "We pair each access alert with an entrance name, allowing reception staff to give directions without consulting route identifiers."]),
    spec("introduction", [(4, 9, 13, "1.2. Our Work", "no-intervention baseline return contract")],
         "State the condition under which an extended procedure is intended to recover its earlier reference case.",
         "When [added action] is absent, [extended procedure] is intended to recover [reference behaviour].",
         "extended purpose > no-action condition > reference-case relationship > later option use",
         "added action; extended procedure; reference behaviour",
         "conditional return to the earlier procedure",
         "This is an explicit author-stated consistency contract, not a verified mathematical identity or a completed regression test. No formula or zero-action simulation is checked here.",
         ["If no temporary closures are supplied, the revised route register is intended to return the original list of available entrances.",
          "With no extra review shift scheduled, the planning extension should reproduce the reference backlog trajectory; that agreement still needs a separate check."]),
    spec("abstract", [(1, 46, 46, "Summary", "closing evaluation roadmap"),
                      (4, 15, 16, "1.2. Our Work", "closing checks roadmap")],
         "Close a work preview by naming the forthcoming checks and limitations discussion without reporting them as completed proof.",
         "We finish by examining [checks] and discussing [limits].",
         "preceding work preview > named check or appraisal > limitations handoff",
         "checks; appraisal scope; limitations",
         "compact Summary closure; sensitivity-and-appraisal Introduction closure",
         "This common roadmap move is retained as a single-paper candidate, not a distinctive high-frequency finding. A promised check is not evidence that its results pass.",
         ["The final review examines unresolved duplicates and records the cases that still require an owner decision.",
          "We close with a timetable replay and a discussion of entrances that the present survey could not cover."])
]

GROUPS = [
    ("SUM-01", 1, 17, 18, "Broad topic and definition-breadth opener", [], "Context only; no positive mechanism nomination."),
    ("SUM-02", 1, 20, 35, "Purpose, representation, construction, demonstration and reported verdicts", [1, 2, 3], "Construction labels and reported verdicts are not model acceptance."),
    ("SUM-03", 1, 37, 44, "Case, reference/intervention procedures, data constraint, plan and simulated selection", [4, 5, 6, 7], "Forecast procedures differ; the best-option claim is scoped to simulation."),
    ("SUM-04", 1, 46, 46, "Review roadmap", [12], "Promise of appraisal, not its result."),
    ("INTRO-01", 3, 7, 12, "Attributed historical definition and its contextual unpacking", [], "Borrowed definition excluded from positive author-language evidence."),
    ("INTRO-02", 3, 14, 22, "Attributed principles and parallel explanations", [], "Context retained; borrowed principle wording is not a new author-language unit."),
    ("INTRO-03", 3, 24, 30, "Competing needs, evaluation gap and aid-allocation decision", [8], "Institutional descriptions remain source claims."),
    ("INTRO-04", 3, 32, 35, "Commissioning audience and declared investment objective", [], "Task-derived audience context, not independent proof or imitation wording."),
    ("INTRO-05", 3, 39, 47, "Starting approach, limitation-led extension, representation and intended capability", [9, 10], "No failed trial, superiority proof or actual visual usability accepted."),
    ("INTRO-06", 4, 3, 7, "Earlier measure hands off to case forecast and proposed plan", [4, 6], "Case eligibility and programme feasibility are not independently checked."),
    ("INTRO-07", 4, 9, 13, "Dynamic extension, no-action reference relation and simulated option choice", [7, 11], "Relationship and effect comparisons are announced, not verified."),
    ("INTRO-08", 4, 15, 16, "Sensitivity and appraisal roadmap", [12], "No check result accepted from a roadmap.")
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def put_new(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(raw)


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def source_span(pages, page, first, last):
    lines = pages[page].splitlines()
    if not 1 <= first <= last <= len(lines):
        raise ValueError("source line range outside page")
    excerpt = "\n".join(lines[first - 1:last])
    if "\ufffd" in excerpt or any(0xD800 <= ord(c) <= 0xDFFF for c in excerpt):
        raise ValueError("corrupt text cannot witness an opening prose unit")
    return excerpt


def construct_unit(item, index, pages):
    occurrences = []
    for page, first, last, section, role in item["spans"]:
        occurrences.append({"page": page, "printed_page": None if page == 1 else page - 1,
                            "section": section, "first_line": first, "last_line": last,
                            "locator": f"physical p{page} lines{first}-{last}: {role}",
                            "source_excerpt": source_span(pages, page, first, last)})
    locations = [o["locator"] for o in occurrences]
    first = occurrences[0]
    short = item.get("short_span") or (first["page"], first["first_line"], first["last_line"])
    excerpt = source_span(pages, *short)
    if short[0] != first["page"] or excerpt not in first["source_excerpt"]:
        raise ValueError("representative excerpt must be inside its full occurrence")
    pattern = f"CP-D-2015-38996-TEXT-{index:02d}"
    return {
        "language_unit_id": f"LU-D-2015-38996-TEXT-{index:03d}",
        "paper_id": PID, "problem_type": "D", "chapter": item["chapter"], "paper_chapter": item["chapter"],
        "page": first["page"], "printed_page": first["printed_page"],
        "section": first["section"], "printed_section": first["section"],
        "granularity": "paragraph", "source_excerpt": excerpt,
        "source_excerpt_anchor": {"page": short[0], "first_line": short[1], "last_line": short[2]},
        "function": item["function"], "rhetorical_move": item["function"],
        "reusable_pattern": item["frame"], "information_order": item["order"],
        "candidate_pattern_ids": [pattern], "occurrences": occurrences,
        "reusable_elements": ["occurrences: " + "; ".join(locations), "stable function: " + item["function"],
                              "order: " + " > ".join(item["order"]), "slots: " + "; ".join(item["slots"]),
                              "variants: " + "; ".join(item["variants"]), "cross-paper support: none established"],
        "prohibited_generalizations": ["boundary: " + item["boundary"],
                                      "Do not copy source clauses, distinctive wording or source-specific facts into original illustrations."],
        "features": {"voice": "active", "tense": "present or prospective work preview",
                     "modality": item["modality"], "clause_structure": "source-linked local rhetorical move",
                     "quantitative_role": "none", "transition": " > ".join(item["order"]),
                     "original_instantiations": item["examples"]},
        "g3": {"occurrences": locations, "stable_function": item["function"], "order": item["order"],
               "slots": item["slots"], "variants": item["variants"], "boundary": [item["boundary"]],
               "cross_paper_support": [], "cross_paper_support_count": 0, "disposition": pattern},
        "disposition": f"opens candidate: {pattern}; one paper, partial opening scan, not promoted or saturated"
    }


def build(output, root=ROOT):
    if output.exists():
        raise FileExistsError("create-only stage already exists")
    manifest_path = root / "artifacts/corpus/manifest.jsonl"
    manifest = language.find_manifest_record(manifest_path, PID)
    source = root.parent / "MCM-ICM-master" / manifest["relative_path"]
    if manifest["sha256"] != SHA or digest(source) != SHA or manifest["page_count"] != 21:
        raise ValueError("source identity mismatch")
    page_paths = [root / f"artifacts/papers/{PID}/text/pages/page-{i:04d}.txt" for i in range(1, 22)]
    live = [(root / f"artifacts/{kind}/{PID}.{ext}") for kind, ext in
            [("paper-cards", "json"), ("language-units", "json"), ("model-units", "json"),
             ("learning-audits", "json"), ("observations", "jsonl")]]
    inputs = [manifest_path, source, *page_paths, *live,
              root / f"artifacts/papers/{PID}/extraction.json",
              root / "artifacts/progress.jsonl", root / "artifacts/transactions/history.jsonl",
              root / "artifacts/transactions/text-first-authorization-20261029.md"]
    frozen = {str(p): digest(p) for p in inputs}
    pages = {i: p.read_text(encoding="utf-8") for i, p in enumerate(page_paths, 1)}
    units = [construct_unit(item, i, pages) for i, item in enumerate(MECHANISMS, 1)]
    record = {"schema_version": 3, "paper_id": PID, "problem_type": "D", "year": "2015",
              "source_sha256": SHA, "review_status": "draft", "available_chapters": ["abstract", "introduction"],
              "units": units, "source_specific_terms": SOURCE_TERMS, "layout_review_status": "pending",
              "draft_scope": "Opening prose only; remaining substantive chapters and saturation pending. No full-paper or layout acceptance."}
    groups = []
    for gid, page, first, last, role, links, boundary in GROUPS:
        groups.append({"group_id": gid, "page": page, "printed_page": None if page == 1 else page - 1,
                       "first_line": first, "last_line": last, "role": role, "boundary": boundary,
                       "language_unit_ids": [f"LU-D-2015-38996-TEXT-{i:03d}" for i in links],
                       "source_excerpt": source_span(pages, page, first, last)})
    profile = anticopy.build_source_profile("\n\f\n".join(pages.values()), 8)
    scans = [anticopy.scan_unit_with_profile(u, profile, 8, set(SOURCE_TERMS)) for u in units]
    unit_errors = [e for i, u in enumerate(units, 1) for e in language.validate_unit(u, "D", 21, None, i)]
    record_errors = language.validate_record(record, None, manifest)
    if any(digest(Path(p)) != h for p, h in frozen.items()):
        raise ValueError("input changed during construction")
    output.mkdir(parents=True, exist_ok=False)
    recipe = Path(__file__).read_bytes()
    put_new(output / "recipe.py", recipe)
    for p in live:
        put_new(output / "before" / (p.parent.name + p.suffix), p.read_bytes())
    put_new(output / "language-units.draft.json", encoded(record))
    review = {
        "paper_id": PID, "status": "opening-prose-only-not-formal-G2-G4-acceptance", "groups": groups,
        "counting_policy": "Four Summary and eight Introduction editorial text groups, not visually certified paragraph counts.",
        "positive_routes": {"summary": "broad concept -> dimensions/construction -> example verdicts -> reference/intervention case work -> constraint/plan/scoped simulated selection -> appraisal preview",
                            "introduction": "attributed meaning/principles -> competing needs and evaluation gap -> commissioning audience -> limitation-led extension and presentation rationale -> case/reference forecast -> plan -> intervention extension/reference contract -> selection/checks"},
        "section_contracts": [
            {"section": "Summary", "input": "Task purpose and concept of sustainable development",
             "rhetorical_job": "Preview a measure and its intended decision use",
             "analytical_job": "Name representation/construction, reported case verdicts and the proposed intervention-analysis route without proving their correctness",
             "output": "Author-reported diagnostic and simulated programme-selection claims",
             "handoff": "Introduction supplies definition, audience problem and work roadmap"},
            {"section": "1. Introduction", "input": "Attributed meaning, case context and commissioning objective",
             "rhetorical_job": "Explain why evaluation and intervention comparison are needed",
             "analytical_job": "Connect the stated gap to an extension, reference forecast, proposal and intervention analysis",
             "output": "Observable work roadmap and an explicit intended reference-case consistency contract",
             "handoff": "Assumptions and substantive construction sections; their review is still pending"}
        ],
        "legacy_findings": [
            "Legacy Introduction units005/006 use printed page2 as if it were physical page2; actual text is physical3.",
            "The attributed definition and principle wording are retained as context, not positive author-language units.",
            "Some legacy source_excerpt fields paraphrase or truncate source language; the new witnesses are extracted from exact frozen page-line spans.",
            "Legacy unit002's one-method-per-index instruction is stronger than the Summary's stated mapping.",
            "Legacy unit004 omits the explicit simulation qualifier from its programme-winner framing.",
            "No legacy unit, mathematical record, table evidence or reference record is deleted or silently replaced."
        ],
        "scan_status": "One complete opening read and targeted abstraction check only; no final-zero-new-moves or whole-paper saturation claim.",
        "remaining": "Read Assumptions and every subsequent author-prose section in order, excluding paused notation/symbol dictionaries/tables/figures and bibliography. Contents headings provide only a provisional navigation map.",
        "acceptance_not_claimed": ["actual paragraph geometry", "all substantive prose coverage", "G2 saturation", "full G4 organization", "formula/model validation", "visual validation", "programme-effect correctness", "live debt clearance", "paper closure"]
    }
    put_new(output / "opening-review.draft.json", encoded(review))
    report = {"paper_id": PID, "status": "partial-text-stage-not-committable", "input_sha256": frozen,
              "recipe_sha256": hashlib.sha256(recipe).hexdigest(), "language_units": len(units),
              "candidate_mechanisms": len(units), "source_witnesses": sum(len(u["occurrences"]) for u in units),
              "original_examples": sum(s["example_count"] for s in scans), "support_papers": 1,
              "unit_structure_errors": unit_errors, "anticopy_results": scans,
              "anticopy_failures": [s for s in scans if s["result"] != "pass"],
              "maximum_shared_content_run": max(s["maximum_shared_content_run"] for s in scans),
              "full_record_errors_retained": record_errors,
              "candidate_sha256": digest(output / "language-units.draft.json"),
              "opening_review_sha256": digest(output / "opening-review.draft.json"),
              "new_paper_closures": 0, "new_history_events": 0,
              "scope": "Text-only generation; existing full extraction text is tokenized for anti-copy, not accepted as mathematical or visual evidence."}
    put_new(output / "validation.json", encoded(report))
    if unit_errors or report["anticopy_failures"]:
        raise ValueError("unit or anti-copy check failed; diagnostic stage preserved")
    print(json.dumps({k: v for k, v in report.items() if k not in {"input_sha256", "anticopy_results"}}, ensure_ascii=False))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.output)


if __name__ == "__main__":
    main()
