#!/usr/bin/env python3
"""Create-only first body-prose continuation; no live installation or closure."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

import stage_d38996_text_first as opening
import validate_language_anticopy as anticopy
import validate_language_units as language

ROOT, PID, SHA = opening.ROOT, opening.PID, opening.SHA
S = opening.spec

# These augment existing mechanisms; repeated witnesses do not become new rules.
AUGMENTS = {
    1: [(6, 3, 11, "3.1. Analysis of Sustainable Development", "explanatory division is explicitly not absolute"),
        (7, 35, 38, "3.3.1. Index System", "dimensions hand off to construction")],
    2: [(8, 43, 45, "3.3.1. Index System", "combined operations named for the next construction level")],
    4: [(13, 14, 26, "3.3.4. Further Discussion", "reference/intervention tasks assigned separate procedures")],
    5: [(11, 52, 54, "3.3.3. An Implementation of Our model", "missing data prompts imputation"),
        (17, 32, 38, "5.1. System Dynamics and Structure Equations", "incomplete system and stated estimation repair")],
    6: [(14, 14, 16, "4. Sustainability Development Plan", "case analysis and forecast precede plan")],
    7: [(20, 21, 25, "5.3. Conclusion", "reported joint-measure comparison becomes recommendation")],
    9: [(7, 22, 29, "3.2.2. Discussion on EF Model", "scope omissions motivate next model"),
        (20, 31, 33, "6.1. Strengths", "retrospective claim of expanded scope")],
    10: [(20, 37, 40, "6.1. Strengths", "claimed audience benefit of representation")],
    11: [(18, 66, 67, "5.1. System Dynamics and Structure Equations", "expected no-action agreement"),
         (19, 3, 5, "5.1. System Dynamics and Structure Equations", "authors' interpretation of displayed agreement")]
}

BODY = [
    S("assumptions", [(4, 26, 29, "2. Assumption", "stability translated to excluded shocks"),
                      (4, 40, 47, "2. Assumption", "independence restated as noninterference"),
                      (21, 7, 11, "6.2. Weaknesses", "scope exclusion returns as a limitation")],
      "Translate a broad operating assumption into the classes of situations the analysis will not cover.",
      "We assume [operating condition]; [excluded situations] therefore fall outside this analysis.",
      "broad condition > operational restatement > excluded examples > later limitation",
      "operating condition; restatement; excluded situations; applicability boundary",
      "that-is-to-say restatement; excluded examples; retrospective scope reminder",
      "An assumption defines scope; it does not establish actual stability, independence or predictability. National sovereignty is not proof that cross-border effects are absent.",
      ["The access review assumes normal opening hours, so emergency evacuations and exceptional security closures lie outside its remit.",
       "The catalogue comparison treats each accession as a separate record; disputed ownership transfers require a different review."]),
    S("assumptions", [(4, 20, 24, "2. Assumption", "task purpose bounds measurement detail"),
                      (4, 31, 35, "2. Assumption", "available records stand in for direct investigation")],
      "Explain the resolution of an analysis through its intended task and a stated measurement constraint.",
      "Because [detail] is difficult to observe, we use [available representation] for [bounded task].",
      "measurement difficulty > task purpose > chosen representation > bounded use",
      "measurement difficulty; available representation; intended task; omitted detail",
      "purpose contrasted with exhaustive measurement; available-data scope rationale",
      "A task-level purpose does not excuse inaccurate inputs or prove the chosen abstraction is adequate. The paper's data-availability assumptions remain unverified.",
      ["The inventory records box-level locations because individual sheets cannot yet be inspected; it is intended to guide retrieval, not establish document condition.",
       "Weekly entry totals support a broad staffing review, but they cannot resolve the queue during a particular hour."]),
    S("model-establishment", [(5, 17, 30, "3.1. Analysis of Sustainable Development", "ideal example gives way to an observable-factor task")],
      "Use an explanatory ideal to expose an operational difficulty, then redirect the analysis toward observable factors.",
      "[example] illustrates [ideal relation], but [observability difficulty] requires us to identify [measurable factors].",
      "illustrative ideal > practical identification difficulty > operational factor search",
      "illustrative example; ideal relation; observability difficulty; measurable factors",
      "analogy followed by however-and-therefore operationalization",
      "The fishing discussion is explanatory, not a verified optimum or proof that the later proxy set identifies the ideal. Do not invent a failed numerical search.",
      ["A perfectly indexed drawer illustrates effortless retrieval, but actual search difficulty must be described through missing labels and misplaced folders.",
       "An uninterrupted route gives a useful reference, yet the building survey must record the closures and entrance restrictions that make it unavailable."], short_span=(5, 28, 30)),
    S("model-establishment", [(7, 40, 44, "3.3.1. Index System", "ranked candidates retain a meaning and coverage guard")],
      "Place a substantive interpretation condition beside a quantitative candidate-screening rule.",
      "We rank [candidates] by [screen], retaining them only when [meaning condition] and [coverage condition] hold.",
      "quantitative ordering > candidate retention > substantive meaning guard > coverage constraint",
      "candidates; ranking screen; meaning condition; coverage condition",
      "rank-then-retain with on-condition-that qualifier",
      "This captures the announced selection rule, not acceptance of its calculation or proof that the retained candidates are balanced or valid.",
      ["The review queue is sorted by duplicate flags, but a record is retained for manual work only when the identifier conflict has a clear ownership consequence.",
       "Candidate entrances are ordered by reported use, with the shortlist also retaining a route for each occupied wing."]),
    S("results", [(11, 45, 54, "3.3.3. An Implementation of Our model", "omitted indices and remaining missing data receive distinct treatment")],
      "Disclose different missing-data responses by the object affected instead of implying one universal repair.",
      "We omit [unavailable components], while [remaining gaps] are handled using [stated procedure].",
      "demonstration scope > omitted components > residual missing data > stated repair",
      "unavailable components; remaining gaps; repair procedure; consequence for interpretation",
      "component omission followed by missing-record repair",
      "The prose reports omitted indices and imputation for other gaps. It does not prove successful recovery, preserve an unchanged measure, or supply an imputation protocol.",
      ["The first comparison excludes boxes without accession numbers; missing room labels in the retained register are listed separately for reconciliation.",
       "Unmapped entrances are left out of the route exercise, while uncertain opening times are carried as unresolved intervals."], short_span=(11, 45, 48)),
    S("results", [(13, 3, 6, "3.3.3. An Implementation of Our model", "same verdict, different reported explanations")],
      "Disaggregate a shared classification by giving each case its own reported explanation.",
      "Although [cases] share [verdict], [case A] is associated with [reason A], whereas [case B] has [reason B].",
      "shared verdict > difference in explanation > case-specific accounts",
      "shared verdict; cases; reason A; reason B",
      "same-outcome but-different-reasons contrast",
      "These are the authors' interpretations of their outputs, not independently established causes or verified country classifications.",
      ["Both boxes need review, but one has conflicting accession dates while the other has no ownership entry.",
       "The two entrances remain unavailable for different reasons: the east door is locked and the courtyard path is obstructed."]),
    S("model-establishment", [(5, 47, 48, "3.1. Analysis of Sustainable Development", "factor family routed to a named section"),
                             (13, 7, 8, "3.3.3. An Implementation of Our model", "selected case reserved for later detailed analysis")],
      "Close a local discussion by naming the later section responsible for the deferred detail.",
      "We leave [subtopic] here and develop it in [named section] for [specific purpose].",
      "current boundary > deferred object > named destination > promised detail",
      "current discussion; deferred subtopic; destination; later purpose",
      "forward reference for a factor family; selected-case handoff",
      "A forward reference allocates exposition; it is not evidence that the promised section fulfils its task. It must resolve to an actual destination.",
      ["The ownership exceptions are set aside here and examined with the transfer records in the next section.",
       "We leave the basement routes for the access audit, where temporary closures can be considered explicitly."]),
    S("model-improvement", [(13, 30, 32, "3.3.4. Further Discussion", "policy evaluation reuses intervention forecasting")],
      "Recast a new decision object as an instance of an already defined analytical task and reuse its interface.",
      "We treat [new object] as [existing task type], so [established procedure] provides the analysis route.",
      "new decision object > task reinterpretation > existing procedure > avoided repetition",
      "new object; existing task type; reused procedure; interface assumptions",
      "regard-as followed by hence-and-reuse",
      "Task reuse requires compatible assumptions and inputs. This prose mapping does not identify a causal policy effect or validate the intervention model.",
      ["We treat a proposed evening opening as a timetable change and pass it to the existing access review rather than create another route inventory.",
       "A new deposit is handled as an accession batch, using the identifier checks already defined for incoming records."]),
    S("model-establishment", [(13, 41, 48, "3.3.4. Further Discussion", "comparison organized around interpretability and domain context"),
                             (14, 3, 10, "3.3.4. Further Discussion", "authors contrast certainty and implementation claims")],
      "Organize a comparison around named task requirements rather than an unqualified list of method names.",
      "For [task requirement], [approach A] offers [claimed property], while [approach B] requires [different condition].",
      "comparison class > task criterion > reported limitation > claimed relative advantage",
      "task requirement; compared approaches; claimed property; evidence basis; scope",
      "criterion-led contrast between method families",
      "The source's broad technical criticisms and superiority claims are not accepted benchmarks. Reuse requires actual support for each contrast; never generalize that stochastic or heuristic methods are inherently unsuitable.",
      ["A flat register is easier to print, whereas linked ownership records can preserve competing claims; the choice depends on the review task.",
       "A fixed opening notice is simple to distribute, while a live closure list can represent short interruptions; neither property establishes overall superiority."], short_span=(13, 41, 45)),
    S("model-improvement", [(15, 9, 25, "4.2. Details of the Plan", "effectiveness and feasibility are separate screens")],
      "Keep an analytically promising direction separate from a feasible recommendation by applying two explicit screens.",
      "We first assess [potential effect], then retain only options compatible with [practical conditions].",
      "effect criterion > promising candidates > suitability qualification > practical screen > retained plan",
      "effect criterion; candidate set; practical conditions; acceptance rule",
      "named effectiveness/reasonableness criteria; not-necessarily-suitable qualification",
      "A sensitivity result does not by itself establish intervention effectiveness. The prose announces separate screens; their calculations and table decisions remain unaccepted.",
      ["A route change may shorten the detour yet still be rejected if it blocks deliveries; both checks precede the access recommendation.",
       "A relabelling option is considered only after its expected review benefit and the handling risk to fragile folders have been assessed."], short_span=(15, 21, 23)),
    S("model-improvement", [(15, 29, 31, "4.2.1. Effectiveness Judgment by Sensitivity Analysis", "usual method role is distinguished from current use")],
      "Distinguish a familiar analytical use from the specific role assigned to the same tool in the current task.",
      "Although [tool] is often used for [usual role], here we use it to examine [current question].",
      "usual analytical role > current purpose > intended influence comparison",
      "tool; usual role; current role; interpretation boundary",
      "usual-use statement followed by and-we-invoke role reassignment",
      "A change in analytical purpose does not prove that the tool answers the new causal or decision question. No sensitivity formula or perturbation result is verified.",
      ["The duplicate detector normally flags repeated identifiers; here its output is used only to select folders for a manual reconciliation trial.",
       "The closure log usually supports incident reporting, but this review uses its dates to identify periods that need a separate access survey."]),
    S("model-improvement", [(16, 19, 26, "4.2.2. Reasonability Judgment by Actual Conditions", "rough model directions are refined using case conditions")],
      "Place a contextual refinement step between a model's rough directions and an actionable proposal.",
      "[analysis] supplies broad directions; [case conditions] constrain how they become [specific actions].",
      "rough analytical output > need for refinement > case-specific conditions > proposal decision",
      "rough directions; case conditions; refinement decision; proposed action",
      "it-remains-to-refine handoff from model to contextual judgement",
      "The listed historical and country descriptions remain paper claims; neither their truth nor the table's accept/reject decisions are independently checked.",
      ["The review flags crowded storage areas, but the move schedule must still account for fragile holdings and available shelving.",
       "The access map suggests a side entrance, yet staffing and delivery windows determine whether that entrance can be opened."], short_span=(16, 19, 20)),
    S("model-improvement", [(16, 49, 53, "4.2.3. Ultimate Plan for Sustainable development", "aggregate progress coexists with unequal access")],
      "Use a concession about overall progress to identify who remains underserved and target the proposal accordingly.",
      "Although [aggregate progress], [subgroup] still faces [barrier]; [proposal] targets that remaining gap.",
      "overall progress > remaining distributional gap > named recipients > proposed response",
      "aggregate progress; subgroup; access barrier; proposed response",
      "although-progress followed by unresolved access and targeted action",
      "The paper's baseline figures, subgroup descriptions and promised effects are not verified. A targeted proposal is not evidence that equal access was achieved.",
      ["Although most boxes now have labels, fragile loose sheets remain difficult to retrieve; the next repair round therefore covers those sheets explicitly.",
       "The main entrance has reopened, but visitors arriving after reception closes still lack access; the proposed trial addresses that period."]),
    S("model-improvement", [(16, 49, 53, "4.2.3. Ultimate Plan for Sustainable development", "education proposal has an annual input target"),
                           (17, 3, 6, "4.2.3. Ultimate Plan for Sustainable development", "infrastructure alternatives have stated rates"),
                           (17, 9, 12, "4.2.3. Ultimate Plan for Sustainable development", "aid has a stated investment target")],
      "Give a proposal an operational input or activity target and time basis before using it as a scenario setting.",
      "[programme] aims to change [input or activity] by [target] over [period].",
      "named programme > intended mechanism > operational target > time basis",
      "programme; proposed input; target; unit; period; scenario role",
      "annual expenditure target; alternative infrastructure rates; investment share",
      "These are proposed targets, not calibrated response functions, realized benefits or independently justified rates. No source number is transferred into the illustrations.",
      ["The pilot schedules one additional review session each week; the number of resolved records will be measured separately.",
       "The access trial adds a staffed evening opening on selected days, with attendance recorded rather than presumed."]),
    S("model-establishment", [(17, 23, 30, "5.1. System Dynamics and Structure Equations", "reciprocal and time-varying case relationships motivate the method role")],
      "Connect the role of a proposed dynamic approach to stated reciprocal relationships and temporal change in the case.",
      "Because [components] influence one another and change over [time], [approach] is used to examine their joint evolution.",
      "case components > reciprocal influence > change over time > announced approach > intended decision use",
      "components; reciprocal relationships; time variation; approach; intended output",
      "case relationship description leading to therefore-method role",
      "This is the authors' appropriateness argument, not verification of feedback equations, temporal calibration or superiority. The preceding attributed general definition is not positive author-language evidence.",
      ["Delivery windows and visitor access affect one another across the day, so the planning exercise follows both schedules together.",
       "New deposits and review capacity change the backlog in opposite directions over a term; the proposed record tracks both flows."], short_span=(17, 23, 28)),
    S("results", [(19, 27, 34, "5.2. Simulation Run and Results", "alternatives, measure, reporting times and horizon are announced")],
      "Declare the comparison objects and reporting frame before presenting the preferred option.",
      "We compare [alternatives] using [measure] at [checkpoints] over [horizon].",
      "alternatives > evaluation measure > reporting checkpoints > horizon > comparative presentation",
      "alternatives; measure; checkpoints; horizon; comparison conditions",
      "one-by-one scenario runs with shared reporting times and presentation",
      "A common display or horizon is not proof of matched inputs, equal resources or valid causal comparison. Planned achievement levels are scenario inputs, not observed outcomes.",
      ["Each trial roster is reviewed at the end of the same opening period, using unresolved requests as the reported outcome.",
       "The label layouts are compared on the same folder set, with reading time recorded at each scheduled review point."], short_span=(19, 27, 29)),
    S("results", [(20, 11, 25, "5.2. Simulation Run and Results / 5.3. Conclusion", "reported performance on two criteria feeds joint measure and recommendation")],
      "Carry criterion-level result statements into a joint-measure claim and then a scoped recommendation.",
      "[option] is reported to lead on [criteria]; the stated [joint measure] then supports [bounded recommendation].",
      "criterion-specific findings > joint-measure comparison > preferred option > decision audience",
      "option; criteria; joint measure; evaluation conditions; recommendation audience",
      "on-the-one-hand/on-the-other-hand results followed by to-sum-up decision",
      "Only the prose's argument chain is traced. Plot readings, table values, aggregation and the winning-programme claim remain unverified; improvement on two narrated dimensions is not independently established dominance.",
      ["The large-print label was read faster and confused fewer trial readers; within that exercise, the combined review favoured it for the next pilot.",
       "The staggered roster left fewer requests unresolved and required fewer handovers in the trial, supporting its use for a further limited test."], short_span=(20, 21, 25)),
    S("strengths-limitations", [(20, 46, 48, "6.1. Strengths", "representational extensibility is proposed as future capability")],
      "Distinguish a possible extension from the functionality actually demonstrated in the current analysis.",
      "[representation] could be extended to [additional scope], which may support [intended use].",
      "present representational property > possible extension > intended explanatory benefit",
      "representation; additional scope; implementation requirement; intended benefit",
      "can-be-extended capability claim",
      "Extensibility is the author's proposed capability, not an implemented higher-dimensional model or a verified explanatory gain.",
      ["The room register could add temporary storage locations, but the extra fields have not yet been tested during a move.",
       "The access record could include delivery entrances once their opening restrictions have been surveyed."]),
    S("strengths-limitations", [(21, 21, 27, "6.2. Weaknesses", "represented relationship class and incompleteness bound interpretation")],
      "State the relationship class retained by an implementation and keep incomplete coverage visible in the conclusion.",
      "This implementation represents [relationship class]; [unrepresented structure] remains outside its current coverage.",
      "represented relationship class > stated estimation route > coverage consequence > remaining data limitation",
      "implementation; represented relationships; unrepresented structure; data limitation",
      "can-only-explain coverage statement followed by incompleteness reminder",
      "The paper's statement about its linear representation is recorded, not generalized into a limitation of every use of the named estimator. Formula and model correctness remain paused.",
      ["The present register links only confirmed transfers; disputed chains remain outside the ownership summary.",
       "This access review covers scheduled closures, while unlogged interruptions remain an unresolved source of error."])
]

REGISTERS = [
    ("present condition", "assumed scope with explicit exclusions", "condition, restatement and excluded examples"),
    ("present rationale", "purpose-bounded abstraction, not demonstrated adequacy", "measurement difficulty contrasted with intended task"),
    ("present exposition", "illustrative ideal followed by operational limitation", "example then however/therefore redirection"),
    ("present procedure", "announced screening with substantive guard", "rank then retain on stated conditions"),
    ("present work report", "disclosed data treatments, not accepted recovery", "omission contrasted with residual-gap repair"),
    ("present reported result", "author-interpreted same verdict with distinct explanations", "shared category followed by case-specific reasons"),
    ("present work preview", "deferred exposition with named destination", "local closure and forward reference"),
    ("present task mapping", "policy interpreted as an intervention task", "regard-as then hence-and-reuse"),
    ("present comparison claim", "author-claimed method properties, not accepted benchmarks", "criterion-led contrast"),
    ("present planning rule", "separate analytic promise and practical acceptance", "effective does not necessarily mean suitable"),
    ("present method-role report", "analytical reuse, not validated causal relevance", "usual use followed by current purpose"),
    ("present planning rationale", "rough output requires contextual refinement", "it remains to refine then case evidence"),
    ("present proposal", "remaining access gap despite reported progress", "although-progress followed by targeted need"),
    ("prospective target", "intended input/activity settings, not realized effects", "programme, target and time basis"),
    ("present appropriateness claim", "case interactions motivate an announced dynamic method", "reciprocal and temporal conditions then therefore"),
    ("present simulation protocol", "stated comparison frame, not proven comparability", "one-by-one alternatives and shared reporting frame"),
    ("present reported result", "author-reported joint comparison and recommendation", "two criterion accounts then joint decision"),
    ("prospective capability", "possible extension, not implemented gain", "can-extend property and intended benefit"),
    ("present limitation", "implementation-specific coverage restriction", "can-only coverage followed by residual gap")
]

# Ranges reviewed as readable prose. Other regions are explicitly not certified.
CLEAN_RANGES = {4: [(18, 47)], 5: [(3, 48)], 6: [(3, 11), (15, 22)],
                7: [(3, 46)], 8: [(43, 45), (63, 64)], 9: [(56, 58)],
                10: [(24, 35)], 11: [(7, 10), (43, 54)], 12: [(50, 54)],
                13: [(3, 52)], 14: [(3, 22), (25, 26), (28, 36), (59, 60)],
                15: [(3, 31)], 16: [(17, 26), (44, 57)], 17: [(3, 38)],
                18: [(66, 67)], 19: [(3, 5), (25, 34)], 20: [(11, 50)], 21: [(3, 27)]}


def build_units(pages):
    if len(BODY) != len(REGISTERS):
        raise ValueError("body register/spec mismatch")
    units = []
    for i, original in enumerate(opening.MECHANISMS, 1):
        item = copy.deepcopy(original)
        item["spans"] += AUGMENTS.get(i, [])
        if i == 1:
            item["boundary"] += " The body explicitly calls the division explanatory and not absolute."
            item["variants"] += ["qualified explanatory split in body", "construction handoff"]
        if i in AUGMENTS:
            item["variants"] += ["body or appraisal witness of the same stable function"]
        units.append(opening.construct_unit(item, i, pages))
    for i, (item, register) in enumerate(zip(BODY, REGISTERS), 13):
        units.append(opening.construct_unit(item, i, pages, register=register))
    for u in units:
        u["disposition"] = f"opens candidate: {u['candidate_pattern_ids'][0]}; one paper, first bounded prose pass, not promoted or saturated"
    units[25]["features"]["quantitative_role"] = "proposed operational input/target with time basis, not an accepted forecast"
    units[27]["features"]["quantitative_role"] = "declared reporting checkpoints and horizon, not verified comparison values"
    return units


def contracts():
    # Five fields are explicit; the contracts reconstruct exposition, not equations.
    rows = [
        ("2. Assumption", "Task and available records", "Bound intended operating conditions", "State measurement, stability, availability and independence assumptions", "Declared applicability limits", "Concept analysis proceeds under those limits"),
        ("3.1. Analysis of Sustainable Development", "Attributed meaning and intertemporal needs", "Turn a broad ideal into a tractable exposition", "Use an example, admit identification difficulty, identify factor families and qualify their partition", "Named explanatory dimensions and factor roles", "Environmental/resource factors are handed to3.2; construction continues in3.3"),
        ("3.2. Ecological Footprint / 3.2.2. Discussion", "Existing attributed environmental/resource baseline", "Explain why the starting approach is retained but extended", "State several author-perceived limitations; no formula-level critique is verified", "Motivation for a broader representation and altered construction", "3.3 introduces the proposed system"),
        ("3.3. The Model / construction and implementation", "Proposed dimensions, candidate indices and data", "Move from construction to an illustrative use", "Announce screened indices, combined operations, intended measurement and data treatments; formal stages remain deferred", "Author-reported case verdicts and differentiated explanations", "Selected-case and forecast roles move to3.3.4 and4"),
        ("3.3.4. Further Discussion", "A proposed measure and illustrative case outputs", "Map forecasting and policy tasks to their next analytical route", "Separate reference/intervention tasks, reinterpret a policy as intervention, state comparison claims", "Forward interfaces to4.1 and5 plus unverified method-property contrasts", "4 develops the case proposal;5 develops intervention analysis"),
        ("4. Sustainability Development Plan", "Selected case, reference forecast and rough influence directions", "Make a proposed plan inspectable rather than list disconnected actions", "Separate effect and feasibility screens, contextualize rough directions, specify recipients and operational targets", "Three proposed programme/aid settings", "5 uses expected achievements as simulation inputs, not observed effects"),
        ("5. Dynamic Improvement", "Proposed settings and stated interacting subsystems", "Connect an extension and comparison exercise to a decision", "Announce dynamic relationships, estimation repair, reference consistency, comparison frame and reported multi-criterion interpretation", "Author-reported preferred programme under the stated exercise", "6 returns to scope, claimed strengths and unresolved data/representation limits"),
        ("6. Analysis of the Model", "Construction, intended uses and implementation experience reported by authors", "Appraise contribution and limit interpretation", "Relate claimed scope/presentation advantages to prior work and retain excluded shocks, missing inputs and representation restrictions", "Bounded text account of claimed capability and limitations", "References provide attribution, not additional author-style evidence")
    ]
    return [{"section": s, "input": a, "rhetorical_job": b, "analytical_job": c, "output": d, "handoff": e,
             "status": "prose-contract-draft-not-formal-G4-acceptance"} for s, a, b, c, d, e in rows]


def build(output, root=ROOT):
    if output.exists():
        raise FileExistsError("create-only body stage already exists")
    prior = root / f"artifacts/staging/text-first-20261029-v3/{PID}"
    old_report = json.loads((prior / "validation.json").read_text(encoding="utf-8"))
    if any(opening.digest(Path(p)) != h for p, h in old_report["input_sha256"].items()):
        raise ValueError("opening-stage input changed")
    manifest = language.find_manifest_record(root / "artifacts/corpus/manifest.jsonl", PID)
    source = root.parent / "MCM-ICM-master" / manifest["relative_path"]
    if opening.digest(source) != SHA or manifest["page_count"] != 21:
        raise ValueError("source identity mismatch")
    input_paths = [Path(p) for p in old_report["input_sha256"]]
    input_paths += [prior / name for name in ("language-units.draft.json", "opening-review.draft.json", "validation.json")]
    input_paths += [Path(__file__), Path(opening.__file__), Path(anticopy.__file__), Path(language.__file__)]
    frozen = {str(p): opening.digest(p) for p in input_paths}
    pages = {i: (root / f"artifacts/papers/{PID}/text/pages/page-{i:04d}.txt").read_text(encoding="utf-8") for i in range(1, 22)}
    units = build_units(pages)
    record = {"schema_version": 3, "paper_id": PID, "problem_type": "D", "year": "2015", "source_sha256": SHA,
              "review_status": "draft", "available_chapters": list(dict.fromkeys(u["chapter"] for u in units)),
              "units": units, "source_specific_terms": opening.SOURCE_TERMS, "layout_review_status": "pending",
              "draft_scope": "First bounded author-prose pass across body and appraisal. Not complete saturation; mixed notation/visual passages and quantitative layouts remain deferred."}
    profile = anticopy.build_source_profile("\n\f\n".join(pages.values()), 8)
    scans = [anticopy.scan_unit_with_profile(u, profile, 8, set(opening.SOURCE_TERMS)) for u in units]
    unit_errors = [e for i, u in enumerate(units, 1) for e in language.validate_unit(u, "D", 21, None, i)]
    record_errors = language.validate_record(record, None, manifest)
    # Source eligibility is a text check, not a mathematical validation.
    span_errors = []
    for u in units:
        for o in u["occurrences"]:
            if "\ufffd" in o["source_excerpt"]:
                span_errors.append(u["language_unit_id"])
    review = {"paper_id": PID, "status": "first-bounded-body-prose-pass-not-G2-saturation",
              "opening_review_ref": str(prior / "opening-review.draft.json"),
              "clean_prose_ranges": CLEAN_RANGES,
              "range_policy": "Ranges are text-layer reading windows, not page-layout or paragraph measurements. Context ranges may contain headings or blank lines. Unlisted regions are not certified.",
              "exclusions": ["physical2 Contents", "physical21 line29 onward bibliography", "office fields and running headers", "all figures/captions/tables", "notation, symbol dictionaries and U+FFFD/mixed lines"],
              "mixed_or_deferred_examples": ["physical8 construction equations and9 weighting table", "physical9-11 measurement/threshold passages", "physical10 line37 has graphic text mixed with author prose", "physical14 line37 has overlaid plot text", "physical15 sensitivity notation/table", "physical17 equations and18 diagram/estimated-equation table", "physical19 line35 contains corrupted notation"],
              "eight_body_contracts": contracts(),
              "positive_full_text_route": "assumptions -> ideal/example and measurable factors -> baseline limitations -> proposed construction and case illustration -> reference/intervention task map -> case forecast -> effect and feasibility screens -> operational programmes -> dynamic extension and stated data repair -> announced reference check -> option comparisons -> joint-measure recommendation -> scope and data limits",
              "claim_boundaries": ["No broad algorithm-family criticism or source superiority claim is adopted as established technical fact.", "The expected no-intervention agreement is an author claim; no plot equality or equation identity is verified.", "Proposed programme rates are scenario inputs, not calibrated effects or observed achievements.", "The final choice has a prose support path, but plots/tables and the claimed winning effect remain unaccepted.", "The data-remedy assurance in the limitations section is not treated as actual data recovery."],
              "scan_log": [{"phase": "body first read", "new_mechanisms": len(BODY), "existing_mechanisms_augmented": sorted(AUGMENTS), "final_zero_new_moves": False}],
              "remaining": ["second and further prose scans until the final bounded scan adds zero moves", "subsection-level five-part contracts and paragraph/argument handoffs", "source-wording and original-example review", "G3 nominations/link replay without promotion", "mixed prose/notation boundaries remain deferred with paused work"],
              "acceptance_not_claimed": ["complete prose saturation", "quantitative layouts", "formal full G4", "formula/model/visual acceptance", "live debt clearance", "paper closure", "skill installation"]}
    if any(opening.digest(Path(p)) != h for p, h in frozen.items()):
        raise ValueError("input changed before staging")
    output.mkdir(parents=True, exist_ok=False)
    opening.put_new(output / "recipe.py", Path(__file__).read_bytes())
    opening.put_new(output / "dependencies" / "stage_d38996_text_first.py", Path(opening.__file__).read_bytes())
    for p in (prior / "before").iterdir():
        opening.put_new(output / "before" / p.name, p.read_bytes())
    opening.put_new(output / "language-units.draft.json", opening.encoded(record))
    opening.put_new(output / "prose-review.draft.json", opening.encoded(review))
    changed = [p for p, h in frozen.items() if opening.digest(Path(p)) != h]
    report = {"paper_id": PID, "status": "prose-stage-not-committable", "input_sha256": frozen,
              "candidate_sha256": opening.digest(output / "language-units.draft.json"),
              "prose_review_sha256": opening.digest(output / "prose-review.draft.json"),
              "recipe_sha256": opening.digest(output / "recipe.py"), "language_units": len(units),
              "new_mechanisms": len(BODY), "source_witnesses": sum(len(u["occurrences"]) for u in units),
              "original_examples": sum(x["example_count"] for x in scans), "support_papers": 1,
              "unit_structure_errors": unit_errors, "source_span_errors": span_errors,
              "anticopy_failures": [x for x in scans if x["result"] != "pass"], "anticopy_results": scans,
              "maximum_shared_content_run": max(x["maximum_shared_content_run"] for x in scans),
              "full_record_errors_retained": record_errors, "input_changes_during_build": changed,
              "new_history_events": 0, "new_paper_closures": 0}
    opening.put_new(output / "validation.json", opening.encoded(report))
    if unit_errors or span_errors or report["anticopy_failures"] or changed:
        raise ValueError("body candidate failed; diagnostic generation preserved")
    print(json.dumps({k: v for k, v in report.items() if k not in {"input_sha256", "anticopy_results"}}, ensure_ascii=False))
    return report


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    build(p.parse_args().output)
