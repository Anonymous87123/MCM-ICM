from __future__ import annotations

"""Create Queue 109 G4 organization evidence from the validated language stage."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-36178-d0225ad0"
LANGUAGE = ROOT / "tmp/q109-language-stage-v4/language.json"
STAGE = ROOT / "tmp/q109-organization-stage-v1"

CONTRACTS = [
    {
        "source_headings": ["2015 Mathematical Contest in Modeling summary"],
        "chapter": "abstract", "pages": [1, 1],
        "input": "A lost-aircraft incident, last known flight state, ocean setting, available search resources, and uncertain recovery time.",
        "rhetorical_job": "Compress the practical need into a complete route that makes the later paper legible before technical detail appears.",
        "analytical_job": "Name the initial bound, day-by-day current displacement, reverse debris tracing, three search algorithms, and scenario comparison without deriving them yet.",
        "output": "A bounded promise: conditional estimates of where to search, which route to use, and how long debris recovery may take.",
        "handoff": "The contents and introduction unpack the route into assumptions, components, and calculations.",
        "transition_cue": "Once the initial area is determined, the text moves from location estimation to current drift and then search algorithms.",
    },
    {
        "source_headings": ["Contents"], "chapter": "title", "pages": [2, 3],
        "input": "The summary's promised location-to-search route.",
        "rhetorical_job": "Expose the architecture before the body begins, including sensitivity, limitations, conclusion, and a separate public communication artifact.",
        "analytical_job": "Order assumptions, parameters, geometry, algorithms, results, error analysis, and operational reflection as dependencies rather than a topic pile.",
        "output": "A navigable source-heading map covering every printed technical and stakeholder section.",
        "handoff": "Introduction supplies the decision problem that gives this route its purpose.",
        "transition_cue": "The first body heading changes from a navigation list to the search problem itself.",
    },
    {
        "source_headings": ["1 Introduction to Problem"], "chapter": "introduction", "pages": [4, 4],
        "input": "A plane likely lost over water and a desire to minimize the elapsed search time.",
        "rhetorical_job": "Frame urgency while specifying the linked tasks a reader must accept as one response system.",
        "analytical_job": "Separate initial-location estimation, adaptable search, and current-informed reconstruction into a three-part technical route.",
        "output": "A stated purpose and a preview of the model interfaces needed to fulfill it.",
        "handoff": "Assumptions constrain what each later interface may claim.",
        "transition_cue": "The next heading changes from what the response should achieve to what it may safely assume.",
    },
    {
        "source_headings": ["2.1 Assumptions and Justifications"], "chapter": "assumptions", "pages": [4, 4],
        "input": "The three-task route and numerous unknown physical, sensing, personnel, and time conditions.",
        "rhetorical_job": "Make simplifying commitments inspectable by attaching reasons rather than silently hiding them in equations.",
        "analytical_job": "Fix worst-case crash behavior, omitted drag, visual-only debris search, flat water, daylight, fatigue, debris persistence, and airport distance assumptions.",
        "output": "A bounded problem regime in which the geometric and search calculations have defined meaning.",
        "handoff": "Parameters operationalize the assumptions as inputs to aircraft, drift, and search calculations.",
        "transition_cue": "After assumptions, the prose switches from why the simplifications are allowed to which quantities carry them forward.",
    },
    {
        "source_headings": ["2.2 Parameters"], "chapter": "notation", "pages": [4, 5],
        "input": "The accepted assumptions and the need to implement aircraft and search behavior.",
        "rhetorical_job": "Bind operational facts to the later decision roles they play instead of presenting a detached symbol list.",
        "analytical_job": "Connect altitude, velocity, mass, crash wind, aircraft range/count, available daylight, weather, visibility, current direction, and time since crash to later model outputs.",
        "output": "A parameter interface for location bounds, drift, sweep width, and route capacity.",
        "handoff": "Problem analysis uses the interface to split the response into location and search mechanisms.",
        "transition_cue": "The next section moves from input declaration to a hypothesis about the problem's separable structure.",
    },
    {
        "source_headings": ["3 Analysis of the Problem", "3.1 Hypotheses"], "chapter": "problem-analysis", "pages": [5, 5],
        "input": "Aircraft/search parameters and the stated need to find a plane quickly.",
        "rhetorical_job": "Show why the proposed route is a deliberate decomposition, not a collection of convenient formulas.",
        "analytical_job": "Divide the task into splash-down prediction and area search; reject spiral-like paths under an efficiency criterion; retain adaptable parallel-route candidates.",
        "output": "A justified six-component model architecture and a path-family screening rule.",
        "handoff": "Statement of Model turns the decomposition into linked components.",
        "transition_cue": "The heading changes from hypotheses about a useful route to an explicit statement of what the model will calculate.",
    },
    {
        "source_headings": ["4 Statement of Model", "4.1 Components of the Model", "4.1.1-4.1.5"], "chapter": "model-establishment", "pages": [5, 9],
        "input": "Problem decomposition, aircraft/current/search parameters, and the admissible assumptions.",
        "rhetorical_job": "Make a multi-stage system readable by enumerating its interfaces before deriving the individual calculations.",
        "analytical_job": "Parameterize a downed plane, search plane, and debris drift; generate a crash region; determine how a path searches it; reverse-trace debris evidence.",
        "output": "An ordered interface chain from last contact to a changing search area and evidence feedback.",
        "handoff": "Grid and geometric construction make those interfaces computationally actionable.",
        "transition_cue": "The subheadings move from component naming to the concrete geometry of the search area.",
    },
    {
        "source_headings": ["4.2 Generating the Search Area", "4.3 Adjusting the search area over time"], "chapter": "data-preprocessing", "pages": [9, 10],
        "input": "Aircraft state, glide and turn limits, wind uncertainty, and a local ocean-current field.",
        "rhetorical_job": "Turn heterogeneous physical uncertainty into a represented computational object that later search algorithms can consume.",
        "analytical_job": "Construct reachable edge points, expand the perimeter by wind, form a convex hull, place it over a grid, drift markers using discrete Euler updates, and rebuild the containing polygon.",
        "output": "A time-indexed, bounded n-gon/search grid with an explicit approximation rule.",
        "handoff": "Detection theory interprets coverage of this changing area as a probability objective.",
        "transition_cue": "After the geometric object exists, the prose introduces the metric used to decide whether it has been searched effectively.",
    },
    {
        "source_headings": ["4.4 Search Theory", "4.5.1 Parallel search"], "chapter": "algorithm", "pages": [10, 11],
        "input": "A bounded search area, aircraft capability inputs, time window, and a need to compare coverage fairly.",
        "rhetorical_job": "Establish a baseline route and metric so later alternatives have a common decision standard.",
        "analytical_job": "Define POD from time, aircraft count, rate, sweep width, and area; describe searchleg/crossleg structure; allocate legs by range; compute swept area.",
        "output": "A parallel-search baseline that returns day-level area coverage and a detection-relevant metric.",
        "handoff": "Alternative geometries modify the baseline's path and resource-use constraints.",
        "transition_cue": "The next subheading retains the same search goal but rotates the path geometry and changes turn/corner behavior.",
    },
    {
        "source_headings": ["4.5.2 Diagonal search", "4.5.3 Optimized parallel search"], "chapter": "model-improvement", "pages": [12, 13],
        "input": "The parallel baseline, the shared POD/coverage objective, and limits on one-pass coverage.",
        "rhetorical_job": "Make alternative designs comparable by explaining both the intended gain and the structural cost of each modification.",
        "analytical_job": "Derive diagonal-area cases; allow surplus aircraft to re-sweep search blocks; account for delayed starts and decreasing legs within a block.",
        "output": "Two variants with explicit coverage logic, capacity use, and conditions that can later be tested against the baseline.",
        "handoff": "The main equation turns their swept area into days/POD and reverse drift closes the evidence loop.",
        "transition_cue": "After defining variants, the paper shifts from path mechanics to the common measure used for operational comparison.",
    },
    {
        "source_headings": ["4.6 Full Statement of the Model’s Main Equation", "4.7 Tracing the Findings to the Crash", "5 Results"], "chapter": "robustness-verification", "pages": [13, 15],
        "input": "Swept-area outputs from each route, a changing search polygon, and found-debris positions.",
        "rhetorical_job": "Translate local computations into an outcome metric and test whether the intended operational choice behaves plausibly across evidence sources and scenarios.",
        "analytical_job": "Map swept area to POD/days, reverse Euler current displacement, compare a conservative bound with AF447 context, and simulate route performance under varied resources and weather.",
        "output": "A conditional decision rule with observed best/worst cases rather than an unconditional route claim.",
        "handoff": "Sensitivity analysis isolates the parameters behind the decision behavior.",
        "transition_cue": "The narrative moves from aggregate route results to one-at-a-time parameter variation around a stated baseline.",
    },
    {
        "source_headings": ["6 Error/Sensitivity Analysis", "6.1-6.6"], "chapter": "sensitivity-analysis", "pages": [15, 16],
        "input": "A 45,000-foot/459-knot/10-knot/21-aircraft/20-knot/14.6-nautical-mile baseline and modeled time-to-search output.",
        "rhetorical_job": "Bound interpretation by showing which operational inputs matter locally and how the claim changes when one input is perturbed.",
        "analytical_job": "Vary height, aircraft speed, crash wind, aircraft count, search wind, and visibility independently; compare days against the 11-day baseline.",
        "output": "A set of local response descriptions that distinguish marginal, linear-like, inverse-exponential-like, and threshold behavior.",
        "handoff": "Model analysis turns those response limits into explicit strengths, weaknesses, and repair priorities.",
        "transition_cue": "The following section stops varying inputs and assesses what the completed system can and cannot claim.",
    },
    {
        "source_headings": ["7.1 Strengths", "7.2 Weaknesses"], "chapter": "strengths-limitations", "pages": [16, 17],
        "input": "The simulation route, sensitivity results, and documented assumptions.",
        "rhetorical_job": "Preserve useful mechanisms while preventing their operational scope from being mistaken for field validity.",
        "analytical_job": "Attribute adaptability to low-input location geometry and moving current fields; bound it by rectangular over-search, MH370-local currents, ignored survivors, and omitted glide-speed detail.",
        "output": "A balanced scope statement with concrete failure mechanisms rather than generic self-criticism.",
        "handoff": "Future work maps each named limitation to a proposed interface or calculation improvement.",
        "transition_cue": "The future-work section converts limitations into additions rather than repeating them as conclusions.",
    },
    {
        "source_headings": ["7.3 Future improvements"], "chapter": "future-improvements", "pages": [17, 17],
        "input": "The data, geometry, search-method, visualization, and deployment limitations named immediately before it.",
        "rhetorical_job": "Turn each scope boundary into a concrete extension route with a clear operational use.",
        "analytical_job": "Propose local current data, more loss-of-contact modes, broader method comparison, coordinate-bearing maps, additional incident inputs, and time-since-crash information.",
        "output": "A prioritized expansion list tied to specific missing assumptions, data, or decision interfaces.",
        "handoff": "Conclusion restates what is usable now while retaining the uncertainty that motivates the extensions.",
        "transition_cue": "The closing heading returns from proposed changes to the present paper's bounded operating contribution.",
    },
    {
        "source_headings": ["8 Conclusion"], "chapter": "conclusion", "pages": [17, 17],
        "input": "Location bound, daily coverage, current drift, algorithm comparison, and stated limits.",
        "rhetorical_job": "Close the paper by restitching the operational loop without erasing the conditional nature of the recommendation.",
        "analytical_job": "Recap bounding-area construction, daily POD reporting, current-informed movement/backtracking, conditional route choice, and remaining unknowns.",
        "output": "A defensible final claim: the framework assists searchers under its declared inputs and uncertainties.",
        "handoff": "References identify external dependencies; the memo translates the same loop for a nontechnical audience.",
        "transition_cue": "The technical paper closes before an explicit source list and separately formatted public communication appear.",
    },
    {
        "source_headings": ["References"], "chapter": "references", "pages": [18, 18],
        "input": "Aircraft specifications, search theory, convex-hull method, current data, and incident sources used by earlier sections.",
        "rhetorical_job": "Expose provenance and reproducibility dependencies without treating citation text as model evidence itself.",
        "analytical_job": "List the external sources for physical assumptions, detection concepts, geometry, aircraft parameters, and ocean-current data.",
        "output": "A dependency boundary that reveals missing frozen data, code, run configuration, and calibration artifacts.",
        "handoff": "The following memo is stakeholder communication, not a further technical derivation.",
        "transition_cue": "A new display style and audience-oriented heading mark the transition from references to public communication.",
    },
    {
        "source_headings": ["Addressing the Press Regarding the Plan for Future Searches"], "chapter": "memo", "pages": [19, 20],
        "input": "The paper's technical decision loop and a public audience needing actionable next steps.",
        "rhetorical_job": "Translate technical uncertainty into a three-stage response that specifies required incident facts, field actions, and evidence feedback.",
        "analytical_job": "Describe bounded-area generation, rectangular/diagonal deployment choice, visual debris observation, current-based reverse tracing, and repeated re-planning.",
        "output": "A stakeholder-facing operational narrative consistent with, but simpler than, the technical route.",
        "handoff": "The iterative loop itself is the final communication endpoint; no new technical claim is introduced.",
        "transition_cue": "The document ends after the repeated search-and-update cycle is stated.",
    },
]


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    language = json.loads(LANGUAGE.read_text(encoding="utf-8"))
    units_by_chapter: dict[str, list[str]] = {}
    for unit in language["units"]:
        units_by_chapter.setdefault(unit["chapter"], []).append(unit["language_unit_id"])
    contracts = []
    for item in CONTRACTS:
        chapter = item["chapter"]
        contract = dict(item)
        contract["linked_language_unit_ids"] = units_by_chapter[chapter]
        contract["coverage_decision"] = "positive-contract-complete"
        contracts.append(contract)
    abstract_units = units_by_chapter["abstract"]
    introduction_units = units_by_chapter["introduction"]
    result = {
        "paper_id": PAPER_ID,
        "source_task_context": {
            "official_problem_statement_status": "not-available-in-manifest",
            "paper_explicit_task": "Develop an adaptive maritime lost-aircraft search response that bounds likely crash location, updates the region with currents and debris evidence, compares search routes, and estimates time to a high detection probability.",
            "stakeholders": ["search coordinators", "search-plane crews", "families and public audiences", "press communication recipients"],
            "required_outputs_observed": ["initial search region", "daily drifting region", "search route", "probability/time estimate", "reverse debris trace", "conditional operational recommendation", "public explanation"],
        },
        "source_heading_map": [{"source_headings": item["source_headings"], "normalized_chapter": item["chapter"], "pages": item["pages"]} for item in CONTRACTS],
        "global_progression": [
            "incident and time-critical objective",
            "assumptions and operational parameters",
            "two-part location/search decomposition",
            "aircraft and current interfaces",
            "bounded moving search polygon",
            "coverage and detection objective",
            "baseline and alternative paths",
            "scenario comparison and conditional method choice",
            "sensitivity and scope limits",
            "future repair, conclusion, and stakeholder iteration",
        ],
        "section_contracts": contracts,
        "paragraph_chains": {
            "abstract": [
                {"paragraph": 1, "dominant_move": "incident-and-purpose", "claim": "A robust model can support a waterborne lost-plane search.", "support": "states the model's use throughout the search process", "qualifier": "robust is asserted before detailed validation", "consequence": "introduces the response objective", "next_link": "moves to initial location inputs", "language_unit_ids": [abstract_units[0]]},
                {"paragraph": 2, "dominant_move": "location-bound", "claim": "Last contact and heading can yield a constrained crash area.", "support": "turn radius and post-contact travel limit a simple circle", "qualifier": "the area is a possible range, not a point prediction", "consequence": "produces an initial search area", "next_link": "current movement changes that area", "language_unit_ids": [abstract_units[1]]},
                {"paragraph": 3, "dominant_move": "dynamic-update", "claim": "Currents move and reshape the region, while debris permits reverse tracing.", "support": "same current calculations are used forward and in reverse", "qualifier": "depends on current information", "consequence": "supports repeated location refinement", "next_link": "search algorithms act on the updated region", "language_unit_ids": [abstract_units[2]]},
                {"paragraph": 4, "dominant_move": "comparison-and-decision", "claim": "Scenario analysis makes an algorithm and time estimate conditional on operating factors.", "support": "three algorithms are compared over more than 900 scenarios", "qualifier": "recommendation varies with weather, aircraft count, and area", "consequence": "offers a conditional route selection", "next_link": "the body explains the underlying components", "language_unit_ids": [abstract_units[3]]},
            ],
            "introduction": [
                {"paragraph": 1, "dominant_move": "task-routing", "claim": "Effective response requires linked location, adaptable route, and current-based recovery tasks.", "support": "the sentence enumerates all three tasks", "qualifier": "the paper treats the incident as a generic open-water case", "consequence": "establishes the model's three-stage logic", "next_link": "assumptions define the usable regime", "language_unit_ids": introduction_units},
            ],
        },
        "main_argument_chains": [
            {"name": "initial-search-area argument", "chain": ["last contact plus aircraft state", "glide and turn constraints", "wind-expanded reachable edge points", "convex-hull n-gon", "initial area for a search route"], "decision": "search begins from a conservative geometric bound rather than a circular point estimate"},
            {"name": "daily-route-selection argument", "chain": ["drifting n-gon and search-plane inputs", "sweep width and route geometry", "swept area", "probability of detection and days", "scenario comparison", "conditional parallel/diagonal/optimized choice"], "decision": "route choice depends on area, weather, visibility, and aircraft availability"},
            {"name": "evidence-feedback argument", "chain": ["debris location and observation time", "local current vector", "reverse Euler drift", "revised crash-origin estimate", "new daily search region", "repeat search cycle"], "decision": "each finding should update the next operational search rather than only confirm a fixed initial map"},
        ],
        "organization_skeleton_test": {
            "status": "pass",
            "result": "With aircraft names, values, and equations removed, the route remains incident -> assumptions -> inputs -> bounded state -> coverage metric -> path alternatives -> scenario decision -> limits -> iterative stakeholder action.",
            "weakness_substitution": False,
        },
    }
    STAGE.mkdir(parents=True)
    output = STAGE / "organization.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "section_contracts": len(contracts), "main_argument_chains": len(result["main_argument_chains"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
