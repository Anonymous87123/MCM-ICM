from __future__ import annotations

"""Create Queue 112 G4 organization evidence from validated language units."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-40612-8bcdc1a7"
LANGUAGE = ROOT / "tmp/q112-language-stage-v1/language.json"
STAGE = ROOT / "tmp/q112-organization-stage-v1"


CONTRACTS = [
    {
        "source_headings": ["1 Summary"], "chapter": "abstract", "pages": [1, 2],
        "input": "A lost aircraft in open water, sparse incident evidence, heterogeneous search aircraft, and a two-stage maritime search problem.",
        "rhetorical_job": "Preview the positive physical-to-probabilistic-to-allocation workflow before naming sensitivity and limitations.",
        "analytical_job": "Name drifter-count estimation, current-driven simulation, surface and underwater Bayesian updates, branch-and-bound allocation, AF447/MH370 applications, and sensitivity.",
        "output": "A conditional promise that the system can prioritize search regions and resources for a declared incident scenario.",
        "handoff": "The contents and introduction unpack the model stages, case evidence, evaluation, public explanation, and source record.",
        "transition_cue": "The summary moves context -> model chain -> applications -> sensitivity and boundary.",
    },
    {
        "source_headings": ["Contents"], "chapter": "title", "pages": [3, 5],
        "input": "The summary's collision, search, allocation, application, and evaluation promise.",
        "rhetorical_job": "Expose all source sections and keep surface search, underwater recursion, allocation, cases, sensitivity, public communication, and references distinct.",
        "analytical_job": "Order base analysis; five assumption groups; notation; collision, simulation, Bayesian, surface, underwater, and allocation models; two applications; six sensitivity subsections; evaluation; press paper; references.",
        "output": "A complete source-heading map for the 34-page argument.",
        "handoff": "The introduction supplies the delayed-recovery context and seven explicit tasks.",
        "transition_cue": "The body begins after the contents with MH370 and AF447 evidence history.",
    },
    {
        "source_headings": ["2 Introduction"], "chapter": "introduction", "pages": [6, 6],
        "input": "The unresolved MH370 search, AF447's nearly two-year underwater recovery, sparse data, and poorly charted ocean geography.",
        "rhetorical_job": "Turn public incidents into a bounded modeling and decision agenda rather than a general call for rescue technology.",
        "analytical_job": "Require drifter count, drift simulation, sequential Bayesian search, aircraft allocation, AF447 retrospective use, MH370 prediction, and strengths/weaknesses analysis.",
        "output": "Seven observable deliverables for an open-water missing-aircraft search system.",
        "handoff": "Base analysis identifies which target and platform attributes enter those deliverables.",
        "transition_cue": "The last bullet moves from model construction to evaluation before Section 3 classifies aircraft roles.",
    },
    {
        "source_headings": ["3 Base Analysis", "3.1 Type of Plane Crashed", "3.2 Type of Search Plane"], "chapter": "problem-analysis", "pages": [7, 8],
        "input": "Candidate crashed-aircraft types and helicopter/fixed-wing search platforms with different physical and sensing properties.",
        "rhetorical_job": "Separate target-generation factors from search-capability factors before they are combined in one plan.",
        "analytical_job": "Connect aircraft size, passenger capacity, and material to drifter count; connect search speed, range, and sensors to cell coverage and detection.",
        "output": "Two typed parameter families for the collision and allocation layers.",
        "handoff": "The assumptions state which real differences are retained, collapsed, or omitted.",
        "transition_cue": "Table 1's platform comparison leads directly to the feasibility assumptions.",
    },
    {
        "source_headings": ["4 Assumption and Hypothesis", "4.1-4.5"], "chapter": "assumptions", "pages": [8, 9],
        "input": "The target and platform heterogeneity identified in the base analysis.",
        "rhetorical_job": "Expose the operating regime of every downstream physical, simulation, probabilistic, and allocation result.",
        "analytical_job": "Fix full load, two disintegration regimes, equal fragments, simplified impulse, common initial target state, current-plus-random surface motion, static seabed parts, stationary targets during search, no false positives, aircraft-only assets, weather-invariant capability, and area limits replacing range.",
        "output": "A component-indexed assumption contract.",
        "handoff": "The notation table defines the quantities consumed under this contract.",
        "transition_cue": "The final search-plan assumption closes the qualitative setup before Table 2 formalizes symbols.",
    },
    {
        "source_headings": ["5 Variable and Definition"], "chapter": "notation", "pages": [10, 10],
        "input": "Collision, drift, search-state, and platform-detection concepts from Sections 3-4.",
        "rhetorical_job": "Keep maximum and actual target counts, crash mechanics, spatial probabilities, and surface/underwater likelihoods distinguishable.",
        "analytical_job": "Define N0, N, V, m, alpha, beta, v, theta, I, S_i,j, D, F(D), P_C, P_D, P_W, P_AkD, and P_AkW.",
        "output": "A notation interface for the physical and Bayesian models.",
        "handoff": "The collision model first uses N0, N, V, alpha, beta, v, theta, and I.",
        "transition_cue": "Section 6 begins immediately after Table 2 with the drifter-count question.",
    },
    {
        "source_headings": ["6.1 Collision Model", "6.1.1 Air Disintegration", "6.1.2 Water Disintegration"], "chapter": "model-establishment", "pages": [10, 12],
        "input": "Aircraft volume, total mass, impact velocity and angle, disintegration regime, and unobserved calibration constants.",
        "rhetorical_job": "Separate maximum searchable material from the fraction released by a particular collision.",
        "analytical_job": "Set N0=alpha V; use N=beta N0; derive I=mv sin(theta); map impulse through a zero-linear-saturation beta function with I0 and gamma.",
        "output": "An actual drifter-count N for later surface-target reasoning.",
        "handoff": "The simulation module places those targets at the impact point and evolves synthetic trajectories.",
        "transition_cue": "After the piecewise beta response returns to N=beta N0, Section 6.2 changes from count to motion.",
    },
    {
        "source_headings": ["6.2 System Module"], "chapter": "data-preprocessing", "pages": [12, 12],
        "input": "An impact location, generated drifters, current data, and an unspecified computer-random motion process.",
        "rhetorical_job": "Introduce a synthetic environment for comparing search outputs with hidden target trajectories.",
        "analytical_job": "Initialize targets together, apply current-based motion plus random motion, and generate debris distributions and trajectories.",
        "output": "A simulated target-location history intended for model measurement and correction.",
        "handoff": "The Bayesian overview defines how actual search reports, rather than hidden simulator state, update location beliefs.",
        "transition_cue": "The source calls the simulator an exact answer, then Section 6.3 returns to inference from incomplete observations.",
    },
    {
        "source_headings": ["6.3 Overview on Search Model", "6.3.1 Review on Bayesian Filtering Algorithm", "6.3.2 Steps of Search Plan"], "chapter": "problem-restatement", "pages": [13, 14],
        "input": "Unknown target cell S_i,j, accessible information, binary search reports B, and separate surface/underwater phases.",
        "rhetorical_job": "Give the reader a prediction-update contract and phase flow before any incident-specific prior is mixed.",
        "analytical_job": "Define a location prior, observation likelihood, posterior, recursive update, and the surface-to-underwater handoff shown in Figure 2.",
        "output": "A two-phase Bayesian state-estimation and control loop.",
        "handoff": "Section 6.4 constructs the surface prior from flight dynamics and reverse drift.",
        "transition_cue": "The flowchart terminates in phase posteriors before the next heading opens surface-prior construction.",
    },
    {
        "source_headings": ["6.4 Water Surface Search Model", "6.4.1 Surface Search Prior PDF", "6.4.2 Surface Search Posterior PDF"], "chapter": "model-improvement", "pages": [14, 18],
        "input": "Last-known-position reachability, a nine-accident distance curve, reverse-drift evidence from spotted targets, OSCAR currents, search cells, and binary reports.",
        "rhetorical_job": "Keep each evidence source and weight visible while converting them into an updateable surface-search distribution.",
        "analytical_job": "Mix equal-probability LKP reachability with F(D)=1-22/(D^2+22) at 50/50; reverse-interpolate currents with a 0.25 speed factor; mix flight and drift priors at 70/30; apply normalized Bayes updating over the current search area.",
        "output": "A surface-search prior and posterior PDF over cells.",
        "handoff": "The underwater model reuses the surface posterior with the flight-dynamics prior.",
        "transition_cue": "Figure 7 closes the surface phase before Section 6.5 changes target class from drifters to wreckage.",
    },
    {
        "source_headings": ["6.5 Underwater Search Model", "6.5.1-6.5.4"], "chapter": "robustness-verification", "pages": [19, 20],
        "input": "The surface posterior, flight-dynamics prior, underwater platform likelihood, and phase-specific detection reports.",
        "rhetorical_job": "Turn the surface result into a recursive underwater plan without treating one failed phase as elimination.",
        "analytical_job": "Mix 30% surface posterior with 70% flight prior; suspend surface search; replace drifter states and likelihoods with wreckage states and likelihoods in Bayes' rule; recurse after misses.",
        "output": "Phase-indexed underwater priors and posteriors until detection or intentional suspension.",
        "handoff": "The allocation model assigns available aircraft to high-probability cells in either phase.",
        "transition_cue": "The recursion statement supplies the probability state consumed by Section 7's resource allocation.",
    },
    {
        "source_headings": ["7 Allocation Model", "7.1 Review on Algorithms", "7.2 Allocation of Search Planes"], "chapter": "algorithm", "pages": [21, 22],
        "input": "An updated cell PDF and search aircraft with heterogeneous area limits and detection rates.",
        "rhetorical_job": "Connect spatial priority to resource selection through a named, inspectable optimization objective.",
        "analytical_job": "Sort cells and aircraft in descending order, match stronger aircraft to larger cell probabilities, and state cumulative detection probability as the branch-and-bound maximization objective.",
        "output": "A ranked aircraft-to-cell allocation plan.",
        "handoff": "The application section uses the probability pipeline on AF447 and MH370, though it does not expose a complete allocation trace.",
        "transition_cue": "Figure 10 illustrates an assignment before Section 8 switches to case evidence.",
    },
    {
        "source_headings": ["8 Applying of Model", "8.1 Application on AF447", "8.2 Prediction on MH370"], "chapter": "results", "pages": [22, 27],
        "input": "AF447 recovery data and initial-search drifter distribution; MH370 satellite/radar path analyses, accessible probability regions, and assumed nondetections.",
        "rhetorical_job": "Demonstrate two distinct uses: retrospective region comparison and conditional prospective search distribution.",
        "analytical_job": "For AF447, mix flight prior and initial surface evidence and compare the highest-probability region with the known wreckage point; for MH370, adopt an external path distribution and propagate no-detection updates through the search phases.",
        "output": "An AF447 underwater-prior map and four MH370 phase PDFs.",
        "handoff": "Sensitivity analysis varies selected target, resource, and mixture inputs around the paper's unspecified baseline case.",
        "transition_cue": "Figure 14 ends the case section and is followed immediately by the sensitivity metric.",
    },
    {
        "source_headings": ["9 Sensitivity Analysis", "9.1-9.6"], "chapter": "sensitivity-robustness", "pages": [27, 30],
        "input": "A cumulative wreckage-detection metric, selected drifter counts, fleet sizes, nine platform profiles, and three pairs of mixture weights.",
        "rhetorical_job": "Show local output response to named physical, resource, platform, and weight choices.",
        "analytical_job": "Evaluate N in {50,100,200}; fleet count in {2,3,4}; selected two-plane combinations; and 30/70, 50/50, 70/30 weight pairs for three prior mixtures.",
        "output": "Six small deterministic sensitivity tables and directional interpretations.",
        "handoff": "Strengths and weaknesses convert these local responses and applications into broader claims and admitted limits.",
        "transition_cue": "The weight section calls the model flexible and reliable before Section 10 audits strengths and weaknesses.",
    },
    {
        "source_headings": ["10 Strengths and Weaknesses", "10.1 Strengths", "10.2 Weaknesses"], "chapter": "strengths-limitations", "pages": [31, 31],
        "input": "The AF447 region comparison, qualitative computation claims, local weight sweeps, and the assumption and parameter record.",
        "rhetorical_job": "Summarize claimed utility while exposing the evidence and implementation boundaries that control transfer.",
        "analytical_job": "Claim accuracy, efficiency, application value, and robustness; admit scaling limits, unrealistic target simplifications, difficult detection parameters, and unrealistic fleet counts.",
        "output": "A paired capability-and-risk record requiring claim downgrades where evidence is absent.",
        "handoff": "The press paper translates the intended system for a public audience.",
        "transition_cue": "The last limitation on fleet assumptions is followed by a new nontechnical register.",
    },
    {
        "source_headings": ["11 Non-technical Paper for Press Conference"], "chapter": "memo", "pages": [32, 33],
        "input": "Public concern about MH370, ocean uncertainty, the surface/underwater Bayesian plan, aircraft allocation, and AF447 comparison.",
        "rhetorical_job": "Translate mathematical states and updates into a chronological search commitment without equations.",
        "analytical_job": "Explain current and leeway evidence, rapid response, surface target observations, underwater posterior updates, stronger-plane-to-higher-probability allocation, and continued search.",
        "output": "A public narrative of evidence, action, feedback, redeployment, and termination.",
        "handoff": "References identify the external reports, data, search theory, and algorithm sources behind the narrative.",
        "transition_cue": "The public commitment ends before the bibliography switches from persuasion to provenance.",
    },
    {
        "source_headings": ["References"], "chapter": "references", "pages": [33, 34],
        "input": "Claims about AF447, MH370, ocean currents, Bayesian search, quicksort, branch-and-bound, and flight-path regions.",
        "rhetorical_job": "Expose the external basis and the archival limits of contextual, data, model, and algorithm claims.",
        "analytical_job": "Map nineteen citations to incident reports, OSCAR data, drift studies, Bayesian search theory, algorithms, and MH370 search geometry.",
        "output": "A provenance map with books and reports alongside incomplete web and data citations.",
        "handoff": "The paper terminates without frozen datasets, source code, simulation logs, or optimization traces.",
        "transition_cue": "Reference 19 is the final source artifact.",
    },
]


def chain(paragraph: int, move: str, claim: str, support: str, qualifier: str, consequence: str, next_link: str, unit_ids: list[str]) -> dict:
    return {"paragraph": paragraph, "dominant_move": move, "claim": claim, "support": support, "qualifier": qualifier, "consequence": consequence, "next_link": next_link, "language_unit_ids": unit_ids}


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    language = json.loads(LANGUAGE.read_text(encoding="utf-8"))
    if language.get("review_status") != "validated":
        raise ValueError("G1-G3 language stage must be validated before G4")
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
            "official_problem_statement_status": "reconstructed-from-paper",
            "paper_explicit_task": "Build an open-water missing-aircraft search system that estimates surface targets, simulates drift, updates surface and underwater location probabilities, allocates heterogeneous aircraft, traces AF447, predicts a conditional MH370 search region, and explains limitations.",
            "stakeholders": ["search-and-rescue authorities", "aircraft dispatchers", "surface and underwater search teams", "airlines", "victims' families", "press and public"],
            "required_outputs_observed": ["drifter count", "synthetic trajectories", "surface prior and posterior", "underwater recursive posterior", "aircraft-cell allocation", "AF447 comparison", "MH370 conditional PDFs", "sensitivity tables", "strengths and weaknesses", "press paper"],
        },
        "source_heading_map": [{"source_headings": item["source_headings"], "normalized_chapter": item["chapter"], "pages": item["pages"]} for item in CONTRACTS],
        "global_progression": [
            "incident delay and observation gap", "target and platform heterogeneity", "component-specific assumption contract", "collision-derived drifter count", "synthetic current-driven trajectories", "Bayesian phase overview", "flight and reverse-drift surface prior", "surface posterior from search reports", "underwater prior and recursion", "ranked aircraft-cell allocation", "AF447 retrospective trace", "MH370 conditional prediction", "local target/resource/weight sensitivity", "claim and limitation review", "public translation", "external-source boundary",
        ],
        "section_contracts": contracts,
        "paragraph_chains": {
            "abstract": [
                chain(1, "context-and-physical-input", "Open-water aircraft loss requires estimating searchable targets before location inference.", "the paragraph moves from 2014 incidents to a collision model and drifter count", "the count parameters are not identified from crash data", "creates a target-state input", "moves to search and allocation", [au[0]]),
                chain(2, "search-allocation-and-cases", "Sequential surface and underwater evidence can update location priorities and resource assignments.", "Bayes, drift behavior, search outcomes, branch-and-bound, simulation, AF447, and MH370 are named in order", "no executable simulation or optimization trace is supplied", "creates an end-to-end workflow promise", "moves to sensitivity and limitations", [au[1], au[2]]),
                chain(3, "scope-and-limit", "The system is claimed adaptable but retains computation, assumption, and parameter barriers.", "the paragraph names accuracy, efficiency, application, robustness, complexity, unrealistic assumptions, and hard parameters", "these are source claims rather than passed release gates", "states the intended evaluation boundary", "the introduction must justify the task", [au[3]]),
            ],
            "introduction": [
                chain(1, "incident-history", "Delayed recovery makes maritime search planning consequential.", "MH370 remains missing while AF447 required nearly two years and four sea-search phases", "the cases are contextual and not an experiment", "establishes the operational stakes", "identifies the observation gap", [iu[0]]),
                chain(2, "evidence-gap", "Sparse data and poorly known ocean geography limit localization.", "the paragraph names flight dynamics, ocean models, search consequences, and uncharted bathymetry", "the paper does not archive the cited data products", "defines the information bottleneck", "states concrete model outputs", [iu[1]]),
                chain(3, "task-contract", "A useful generic plan must connect physical target generation, motion, probabilistic search, allocation, cases, and evaluation.", "seven bullets enumerate collision, simulation, Bayes, allocation, AF447, MH370, and strengths/weaknesses", "generic reliability remains a goal rather than established evidence", "commits the paper to inspectable deliverables", "base analysis types the inputs", [iu[2], iu[3]]),
            ],
        },
        "main_argument_chains": [
            {"name": "physical-and-evidence-to-search-state", "chain": ["aircraft size and load", "maximum drifters", "impact impulse", "piecewise disintegration", "actual drifters", "synthetic current trajectories", "unknown target cells"], "decision": "represent what may be detectable and where it may move before search reports arrive"},
            {"name": "surface-prior-to-posterior", "chain": ["last-known-position reachability", "nine-accident distance distribution", "50/50 flight prior", "reverse drift with interpolated currents", "70/30 surface prior", "aircraft search report", "normalized Bayes posterior"], "decision": "prioritize the next surface-search cells under explicit evidence and weight assumptions"},
            {"name": "surface-to-underwater-recursion", "chain": ["surface posterior", "flight-dynamics prior", "30/70 underwater prior", "underwater likelihood", "phase-I report", "posterior-as-next-prior", "detection or intentional suspension"], "decision": "continue underwater localization without treating a missed phase as proof of absence"},
            {"name": "ranked-assets-to-case-decisions", "chain": ["updated cell PDF", "aircraft capability scores", "parallel rankings", "cumulative-detection objective", "aircraft-cell allocation", "AF447 region comparison", "MH370 conditional phase maps"], "decision": "assign stronger resources to higher-priority regions and retain each case's evidence boundary"},
            {"name": "sensitivity-to-public-and-provenance", "chain": ["drifter-count grid", "fleet-count grid", "platform combinations", "three weight sweeps", "local response claims", "admitted limitations", "press chronology", "nineteen-source provenance map"], "decision": "communicate only the local stability, application trace, and operational sequence supported by the declared artifacts"},
        ],
        "organization_skeleton_test": {
            "status": "pass",
            "result": "With incident names, numeric values, and equations removed, the positive route remains context -> typed target/platform inputs -> assumptions -> physical target generation -> movement scenario -> surface prior/update -> underwater recursion -> resource allocation -> case trace -> sensitivity -> bounded evaluation -> public explanation -> provenance boundary.",
            "weakness_substitution": False,
        },
    }
    STAGE.mkdir(parents=True)
    output = STAGE / "organization.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "section_contracts": len(contracts), "main_argument_chains": len(result["main_argument_chains"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
