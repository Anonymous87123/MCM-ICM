from __future__ import annotations

"""Create Queue 110 G4 organization evidence from the validated language stage."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-38720-26d38781"
LANGUAGE = ROOT / "tmp/q110-language-stage-v1/language.json"
STAGE = ROOT / "tmp/q110-organization-stage-v1"

CONTRACTS = [
    {
        "source_headings": ["Hidden in Plane Sight summary"], "chapter": "abstract", "pages": [1, 1],
        "input": "An aircraft missing over remote water, rescue urgency, uncertain crash location, and finite search resources.",
        "rhetorical_job": "Make the whole paper legible as an escalation from location prediction and ideal route screening to imperfect discovery and a final decision.",
        "analytical_job": "Preview a bounded Gaussian location field, random and systematic route simulations, Bayesian updating, completion proportions, and transfer to different targets/resources.",
        "output": "A conditional promise that posterior-guided searching can find most modeled crashes quickly enough to matter for rescue.",
        "handoff": "The contents and introduction unpack the research, assumptions, candidate routes, realism upgrade, evidence, and recommendation.",
        "transition_cue": "The summary repeatedly moves from where to look to how to search, then from ideal to imperfect accuracy.",
    },
    {
        "source_headings": ["Table of Contents"], "chapter": "title", "pages": [2, 3],
        "input": "The summary's location-to-route-to-recommendation promise.",
        "rhetorical_job": "Expose the unusually long evidence route before the reader enters historical research or simulation detail.",
        "analytical_job": "Order research, variable/scenario foundation, assumptions, two model regimes, stability tests, comparative results, recommendation, public communication, and provenance.",
        "output": "A complete source-heading map in which ideal and uncertainty-aware solutions remain visibly distinct.",
        "handoff": "Introduction supplies the ranked human criteria that give this architecture its decision purpose.",
        "transition_cue": "The first body heading changes from document navigation to the missing-aircraft dilemma and planned response.",
    },
    {
        "source_headings": ["1 Introduction", "The Dilemma", "The Approach"], "chapter": "introduction", "pages": [4, 5],
        "input": "Modern aircraft can still disappear over open ocean while families and possible survivors wait.",
        "rhetorical_job": "Rank success criteria and show that the proposed recommendation will be earned through a declared sequence rather than asserted immediately.",
        "analytical_job": "Prioritize discovery, then rescue time; include aircraft/sensor variation; route case research, variables, geometry, simulation, imperfect detection, stability, and analysis.",
        "output": "A two-level objective and an auditable research-to-decision work plan.",
        "handoff": "Historical and technical research select the incident class, lost-plane trigger, probability objective, and sensor regime.",
        "transition_cue": "The prose shifts from the approach checklist to evidence about past crashes and search practice.",
    },
    {
        "source_headings": ["2 Research", "2.1-2.6"], "chapter": "problem-analysis", "pages": [6, 12],
        "input": "A broad class of ocean disappearances with heterogeneous aircraft, causes, communication systems, and search technologies.",
        "rhetorical_job": "Narrow the modeling case through explicit historical, geographic, causal, regulatory, and sensing choices.",
        "analytical_job": "Use Earhart/MH370 as context; screen 89 cases; choose Atlantic passenger aircraft and three representatives; exclude ATC/hijacking cases; set a 30-minute uncertainty interval; define containment times detection; choose P-8 radar.",
        "output": "A modelable Atlantic mid-flight crash case with a representative target set, lost-contact window, probability objective, and initial ideal sensor.",
        "handoff": "Variables and scenario calculations translate those research choices into geometry and simulation parameters.",
        "transition_cue": "After selecting the sensor regime, the next major heading changes from external evidence to internal model definitions.",
    },
    {
        "source_headings": ["3 Foundation of Analysis", "3.1-3.3"], "chapter": "notation", "pages": [13, 19],
        "input": "The selected incident class, representative aircraft, 30-minute alert rule, search-theory probabilities, and P-8 radar.",
        "rhetorical_job": "Bind every later equation and path rule to named physical or operational quantities before simulation begins.",
        "analytical_job": "Define lost/search states; derive glide range and 30-minute path length; create a swept-capsule rectangle; select Boeing 777 values; simplify containment to uniform x and normal y; choose P-8 speed and sight.",
        "output": "A 520-by-200-mile coordinate search field, probability representation, selected target/search aircraft, and symbol interface.",
        "handoff": "General assumptions freeze the regime in which these inputs may be used.",
        "transition_cue": "The question about the shortest route closes the foundation and leads directly to grouped operating assumptions.",
    },
    {
        "source_headings": ["4 Compilation of General Assumptions", "4.1-4.3"], "chapter": "assumptions", "pages": [20, 21],
        "input": "The rectangle, containment model, representative aircraft, sensor, and search-time objective.",
        "rhetorical_job": "Make the first experiment's idealizations inspectable and organize them by environment, crash, and search operation.",
        "analytical_job": "Fix flat geometry, no wind/current, on-route instantaneous failure, bounded glide, stationary debris, ideal mobilization/endurance/weather/cost, and uniform radar sight.",
        "output": "A controlled ideal regime whose known gaps can later motivate discovery uncertainty and final limitations.",
        "handoff": "The normal-distribution model instantiates the common crash generator, completion rule, and statistical protocol.",
        "transition_cue": "The next heading changes from constraints on the experiment to the experiment itself.",
    },
    {
        "source_headings": ["5 Models", "5.1 Normal Distribution", "Completed Simulation", "Statistical Analysis"], "chapter": "model-establishment", "pages": [22, 23],
        "input": "A rectangular normal-containment field, ideal radar, search-plane motion variables, and candidate route requirement.",
        "rhetorical_job": "Give every route a shared test bed and reporting template so comparisons do not change the target or stopping rule.",
        "analytical_job": "Sample crashes from the normal field; stop when distance is below sight range; summarize time by mean, median, spread, standard error, and 95-percent confidence interval.",
        "output": "A reusable simulation harness and comparison metric for ideal-discovery paths.",
        "handoff": "Random paths establish failure, confinement, and weighting baselines within that harness.",
        "transition_cue": "The first named solution begins with the least structured path to create a baseline.",
    },
    {
        "source_headings": ["Solution 5.1.1", "Solution 5.1.2", "Solution 5.1.3"], "chapter": "algorithm", "pages": [24, 31],
        "input": "The shared crash field, ideal completion rule, P-8 speed/sight, and a need for a comparison baseline.",
        "rhetorical_job": "Reveal why unconstrained randomness, boundary confinement, and weak containment weighting remain inadequate.",
        "analytical_job": "Update a random unit vector; redirect excursions orthogonally; add endpoint weighting; run 100 trials where feasible; compare skewed time distributions and overlapping intervals.",
        "output": "An unviable unbounded route and two slow, redundant bounded baselines with no proven difference between them.",
        "handoff": "Systematic routes directly repair overlap and probability-ordering failures.",
        "transition_cue": "The next solution replaces stochastic wandering with predictable, nonoverlapping strips.",
    },
    {
        "source_headings": ["Solution 5.1.4", "Solution 5.1.5", "Solution 5.1.6", "Normal Distribution Overall Conclusion"], "chapter": "model-improvement", "pages": [32, 40],
        "input": "Random-route redundancy, a normal containment field, 10-mile sight, and the common ideal-detection harness.",
        "rhetorical_job": "Make each new geometry a traceable repair and compare it on the same outcome distribution.",
        "analytical_job": "Test edge-to-edge descending stripes, center-out alternating stripes, and sight-scaled sinusoidal passes; measure 100-trial time distributions and interval overlap.",
        "output": "Systematic routes dominate random baselines; center-out spiral stripes give the lowest one-plane ideal-model times.",
        "handoff": "Discovery uncertainty tests whether the ideal-model winner remains preferable when passes can miss debris.",
        "transition_cue": "A direct question challenges the 100-percent detection assumption and opens the second model regime.",
    },
    {
        "source_headings": ["5.2 Normal Distribution with Discovery Uncertainty", "Solution 5.2.1", "Solution 5.2.2"], "chapter": "robustness-verification", "pages": [41, 48],
        "input": "The same containment field and route family, now with separate radar and operator failure probabilities.",
        "rhetorical_job": "Increase realism without losing comparability by changing the observation model and explicitly showing its effect on the next action.",
        "analytical_job": "Set detection from radar and operator terms; update searched/unsearched containment after nondetection; choose posterior maxima for each pass; cap at 24 hours; compare 500 adaptive and fixed-route trials.",
        "output": "Bayesian search has a higher conditional mean but finds 95 percent by 24 hours versus 80 percent for fixed spiral stripes, with equal medians.",
        "handoff": "Stability scenarios alter target detectability and search resources before aggregate results choose a recommendation.",
        "transition_cue": "The paper moves from comparing two uncertain-discovery routes to changing the target and number of search planes.",
    },
    {
        "source_headings": ["6 Solution Stability", "6.1", "6.2"], "chapter": "sensitivity-robustness", "pages": [49, 52],
        "input": "The Bayesian winner, the ideal spiral/stripe geometry, Boeing target properties, and one P-8 search plane.",
        "rhetorical_job": "Test flexibility by changing recognizable scenario dimensions instead of repeating the baseline with cosmetic inputs.",
        "analytical_job": "Shrink the area and detection rate for a Cessna; then add a second plane with opposite, nonoverlapping striped motion; compare distributions and intervals.",
        "output": "Target size materially changes Bayesian search time, while a second idealized plane lowers stripe-search mean to about 2.4 hours.",
        "handoff": "Results synthesize all route and stability evidence by model regime.",
        "transition_cue": "The next section stops presenting individual solutions and compares their intervals and operational criteria together.",
    },
    {
        "source_headings": ["7 Results", "7.1", "7.2"], "chapter": "results", "pages": [53, 55],
        "input": "Seven ideal-route trials, three uncertain-discovery trials, confidence intervals, skew diagnostics, medians, and 24-hour failure counts.",
        "rhetorical_job": "Prevent a single fast conditional mean from dominating by separating regimes and matching statistics to skew/censoring.",
        "analytical_job": "Establish systematic-versus-random differences; identify two-plane and one-plane ideal winners; compare uncertain routes by median and completion proportion; compare target sizes.",
        "output": "Spiral stripes win the one-plane ideal model, but the Bayesian route wins the realistic decision because its equal median accompanies much higher completion.",
        "handoff": "Recommendation ties that statistical tradeoff back to the rescue-time criterion.",
        "transition_cue": "After model-level synthesis, the conclusion restates the human success threshold and selects one operational route.",
    },
    {
        "source_headings": ["8 Conclusion", "8.1 Recommendation"], "chapter": "conclusion", "pages": [56, 56],
        "input": "Rescue-before-hypothermia criterion, ideal-route times, uncertain-route medians, and 24-hour completion proportions.",
        "rhetorical_job": "Choose the most defensible route by the ranked objective rather than merely the smallest reported mean.",
        "analytical_job": "Reject idealized solutions despite sub-eight-hour means; compare equal 4.05-hour medians; prefer 95-percent Bayesian completion over 80-percent spiral completion.",
        "output": "Recommend the normal distribution with discovery uncertainty paired with a Bayesian-adjusted flight path.",
        "handoff": "Strengths and weaknesses delimit what that recommendation actually supports.",
        "transition_cue": "The following subsection changes from route selection to explicit capability and scope assessment.",
    },
    {
        "source_headings": ["8.2 Strengths and Weaknesses of Recommendation"], "chapter": "strengths-limitations", "pages": [57, 57],
        "input": "The chosen Bayesian mechanism, Boeing/Cessna completion evidence, confidence interval, and all earlier idealizations.",
        "rhetorical_job": "Preserve the recommendation's adaptive value while preventing its modeled rescue performance from being mistaken for field validation.",
        "analytical_job": "Attribute flexibility to adjustable detection/area/sight inputs; report completion and rescue-window evidence; identify exponential computation, overlap, distribution uncertainty, omitted drift/weather/debris stages, mobilization, fuel, and cost.",
        "output": "A bounded recommendation with explicit computational, geometric, physical, temporal, and resource failure modes.",
        "handoff": "The press document translates the intended procedure for a public audience while some technical caveats become less explicit.",
        "transition_cue": "A new audience and document style mark the move from technical self-assessment to stakeholder communication.",
    },
    {
        "source_headings": ["9 Press Conference Document"], "chapter": "memo", "pages": [58, 58],
        "input": "Public concern after MH370 and the paper's posterior-guided search loop.",
        "rhetorical_job": "Translate technical work into accountable immediate actions without introducing a new mathematical claim.",
        "analytical_job": "Predict from last signal/path; bound and deploy; fly parallel paths; update location from search data; adjust for equipment imperfections; continue and refine.",
        "output": "A stakeholder-facing commitment to rapid, thorough, adaptive searching.",
        "handoff": "References document the external evidence and software behind the technical paper.",
        "transition_cue": "The prose ends its promise before switching to bibliographic entries and image/software provenance.",
    },
    {
        "source_headings": ["10 References", "8.2 Image References"], "chapter": "references", "pages": [59, 61],
        "input": "Historical cases, aircraft specifications, communication rules, search theory, radar tests, Bayesian formulas, visual-search evidence, survival data, images, and software.",
        "rhetorical_job": "Expose the external basis of major choices while revealing what cannot be reconstructed from the paper alone.",
        "analytical_job": "Map citations to incidents, specifications, detection assumptions, probability updating, and rescue timing; identify Mathematica/Excel and image dependencies.",
        "output": "A provenance boundary lacking frozen code, simulation datasets, random seeds, posterior grids, and executable configurations.",
        "handoff": "This closes the source; no later section repairs the missing reproducibility artifacts.",
        "transition_cue": "The document terminates after software credits; the repeated 8.2 label is a source numbering defect.",
    },
]


def chain(paragraph: int, move: str, claim: str, support: str, qualifier: str, consequence: str, next_link: str, unit_ids: list[str]) -> dict:
    return {"paragraph": paragraph, "dominant_move": move, "claim": claim, "support": support, "qualifier": qualifier, "consequence": consequence, "next_link": next_link, "language_unit_ids": unit_ids}


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    language = json.loads(LANGUAGE.read_text(encoding="utf-8"))
    units_by_chapter: dict[str, list[str]] = {}
    for unit in language["units"]:
        units_by_chapter.setdefault(unit["chapter"], []).append(unit["language_unit_id"])
    contracts = []
    for item in CONTRACTS:
        contract = dict(item)
        contract["linked_language_unit_ids"] = units_by_chapter[item["chapter"]]
        contract["coverage_decision"] = "positive-contract-complete"
        contracts.append(contract)
    au = units_by_chapter["abstract"]
    iu = units_by_chapter["introduction"]
    result = {
        "paper_id": PAPER_ID,
        "source_task_context": {
            "official_problem_statement_status": "not-available-in-manifest",
            "paper_explicit_task": "Develop a model and usable procedure for locating an aircraft lost over open ocean quickly enough to improve rescue chances, accounting for crash-location uncertainty, flight-path choice, sensor discovery uncertainty, and different targets/resources.",
            "stakeholders": ["search coordinators", "search-plane crews and radar operators", "survivors and families", "airlines", "press and travelers"],
            "required_outputs_observed": ["bounded search area", "containment distribution", "search path", "discovery update", "time distribution", "completion proportion", "stability comparison", "recommendation", "public procedure"],
        },
        "source_heading_map": [{"source_headings": item["source_headings"], "normalized_chapter": item["chapter"], "pages": item["pages"]} for item in CONTRACTS],
        "global_progression": [
            "human urgency and ranked success criteria", "historical and technical screening", "state variables and representative scenario", "explicit ideal assumptions", "common crash and detection harness", "random-route failure baselines", "systematic probability-aware path repairs", "imperfect discovery and Bayesian updating", "target/resource stability checks", "distribution-aware comparison", "conditional recommendation and scope", "stakeholder translation and provenance boundary",
        ],
        "section_contracts": contracts,
        "paragraph_chains": {
            "abstract": [
                chain(1, "urgency", "Faster recovery can support rescue and closure.", "contrasts the need with the failed MH370 search", "urgency does not itself establish a method", "sets the ranked human objective", "moves to location and route inputs", [au[0]]),
                chain(2, "model-route", "Crash-state and search-plane inputs can support route simulation.", "names speed, glide ratio, altitude, search speed, and sight", "the distributions and sensors remain simplified", "defines the modeling route", "moves to the search field", [au[1]]),
                chain(3, "location-field", "A bounded Gaussian field represents where to look.", "projects the commercial path and rectangular area", "the field is estimated rather than incident-calibrated", "creates a common target distribution", "supports ideal route comparison", [au[1]]),
                chain(4, "ideal-comparison", "Systematic routes reduce redundancy under perfect discovery.", "contrasts random performance with 3.6-hour mean", "the sensor is assumed certain", "identifies a geometric candidate", "introduces imperfect detection", [au[2]]),
                chain(5, "uncertainty-update", "Bayesian updating retains fast median search with missed detections.", "reports 4.7-hour comparative mean and 95-percent one-day completion in the summary", "wording compresses different uncertain-route results", "promotes an adaptive route", "tests flexibility", [au[3]]),
                chain(6, "transfer", "The framework can change aircraft count and target size.", "names both dimensions explicitly", "only two stability scenarios are later tested", "claims bounded flexibility", "moves to recommendation", [au[3]]),
                chain(7, "recommendation", "Bayes is the preferred realistic procedure.", "selects the majority-found criterion", "field realism remains limited by stated omissions", "states the decision", "the body must justify it", au),
            ],
            "introduction": [
                chain(1, "context-and-stake", "Modern tracking does not eliminate open-ocean disappearance.", "links MH370, searchers, families, and possible survivors", "the incident is used as motivation and representative context", "establishes need", "ranks objectives", [iu[0]]),
                chain(2, "ranked-objectives", "Discovery comes first and rescue time second.", "the Dilemma bullet order states the priority", "cost and field logistics are not yet part of the objective", "creates the decision rule", "adds entity variation", [iu[1]]),
                chain(3, "research-route", "Cases, communication, search theory, sensors, variables, and geometry must be established before paths.", "the first Approach bullets enumerate these dependencies", "selection quality depends on cited and estimated inputs", "defines the evidence foundation", "moves to simulation", [iu[2]]),
                chain(4, "validation-to-decision", "Ideal routes should be tested, made less ideal, transferred, analyzed, and then recommended.", "the closing bullets state this order", "simulation is within-model evidence rather than field validation", "commits to an auditable decision route", "research begins the route", iu),
            ],
        },
        "main_argument_chains": [
            {"name": "search-field construction", "chain": ["30-minute last-contact interval", "cruising distance plus maximum glide", "swept capsule", "520-by-200 rectangle", "uniform x and normal y containment", "sampled crash coordinate"], "decision": "candidate routes are compared on a bounded probability field rather than an unweighted ocean"},
            {"name": "path-learning ladder", "chain": ["unbounded random failure", "boundary confinement", "weak probability weighting", "nonoverlapping descending stripes", "center-out spiral stripes", "sinusoidal wider passes", "common confidence-interval comparison"], "decision": "systematic center-first geometry is the best one-plane route under ideal detection"},
            {"name": "realism-to-recommendation", "chain": ["reject perfect detection", "radar/operator discovery probability", "Bayesian nondetection update", "posterior-maximum next pass", "24-hour capped trials", "median plus completion proportion", "95-percent versus 80-percent discovery"], "decision": "Bayesian adaptive search is preferred despite a higher conditional mean"},
            {"name": "rescue-and-scope loop", "chain": ["18-hour hypothermia threshold", "modeled time distributions", "rank discovery above conditional speed", "select uncertainty-aware Bayes", "state computational and physical omissions", "translate prediction-deployment-update to stakeholders"], "decision": "the route is an adaptable modeled procedure, not a field guarantee"},
        ],
        "organization_skeleton_test": {
            "status": "pass",
            "result": "With aircraft names, values, and equations removed, the route remains urgency -> evidence screening -> state/interface definition -> controlled baseline -> failure-led route repair -> observation uncertainty -> posterior action -> stability -> distribution-aware choice -> bounded communication.",
            "weakness_substitution": False,
        },
    }
    STAGE.mkdir(parents=True)
    output = STAGE / "organization.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "section_contracts": len(contracts), "main_argument_chains": len(result["main_argument_chains"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
