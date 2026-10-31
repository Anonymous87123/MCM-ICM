from __future__ import annotations

"""Create Queue 111 G4 organization evidence from the validated language stage."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-39173-b8260835"
LANGUAGE = ROOT / "tmp/q111-language-stage-v2/language.json"
STAGE = ROOT / "tmp/q111-organization-stage-v1"

CONTRACTS = [
    {
        "source_headings": ["Searching for a Lost Plane abstract"], "chapter": "abstract", "pages": [1, 1],
        "input": "A transoceanic flight beyond coastal radar, a last communication on the intended path, sparse prior evidence, and finite search resources.",
        "rhetorical_job": "Preview the complete model as a positive construction from containment through detection and updating before assumptions and transfer limits.",
        "analytical_job": "Name the casualty-distance density, glide/deviation field, POC cells, Koopman POD, nondetection update, neighborhood search, Flight ABCD example, sensitivity, and strengths.",
        "output": "A conditional promise that a source-parameterized, continuously updated neighborhood plan can prioritize a bounded search region.",
        "handoff": "The contents and introduction unpack the observation gap, model stages, evaluation, worked example, communication artifact, and code.",
        "transition_cue": "The abstract's three paragraphs move containment -> detection/search -> assumptions/transfer.",
    },
    {
        "source_headings": ["Contents"], "chapter": "title", "pages": [2, 2],
        "input": "The abstract's containment-detection-search promise.",
        "rhetorical_job": "Make the entire analytical route visible, including sensitivity, limitations, public communication, and computational appendices.",
        "analytical_job": "Order Introduction; containment, discretization, coordinates, POD, updating, assumptions, sensitivity, evaluation; Flight ABCD; conclusion; press summary; Appendices A-D.",
        "output": "A source-heading map that keeps each model interface and evidence artifact distinct.",
        "handoff": "The Introduction supplies the offshore observation problem and sparse-prior motivation.",
        "transition_cue": "The body begins on the same physical page with the radar-coverage gap.",
    },
    {
        "source_headings": ["1 Introduction"], "chapter": "introduction", "pages": [2, 3],
        "input": "Eighty-three vanished aircraft, limited offshore radar, scheduled pilot communication, and contrasting Air France/MH370 evidence histories.",
        "rhetorical_job": "Establish why a new search model is needed when familiar Bayesian elimination lacks strong incident-specific priors.",
        "analytical_job": "Connect radar loss to communication triggers; contrast informative versus sparse priors; require indefinite casualty timing, deviation from the IFP, no signal, and time efficiency.",
        "output": "A sparse-prior missing-flight search objective with explicit trajectory and time priorities.",
        "handoff": "The model overview decomposes that objective into containment, detection, and iterative priority updates.",
        "transition_cue": "The final Introduction sentence promises a search strategy before Section 2 names its three analytical components.",
    },
    {
        "source_headings": ["2 Model"], "chapter": "problem-analysis", "pages": [3, 3],
        "input": "A flight traveling linearly from A to B whose location and detectability are unknown after last contact.",
        "rhetorical_job": "Give the reader a three-part interface before any probability density or algorithm is introduced.",
        "analytical_job": "Separate containment, conditional detection under resource conservation, and continuously updated most-likely location.",
        "output": "A containment -> detection -> updating decomposition for an optimized search plan.",
        "handoff": "Section 2.1 first constructs the spatial probability field.",
        "transition_cue": "The next heading expands the first named component, probabilities of containment.",
    },
    {
        "source_headings": ["2.1 Constructing Probabilities of Containment for a Missing Airplane and its Debris"], "chapter": "model-establishment", "pages": [3, 6],
        "input": "Last-contact distance and coordinates, remaining route to coastal radar, aircraft altitude and glide ratio, and possible lateral deviation.",
        "rhetorical_job": "Turn physical narrative into a traceable joint impact-location distribution rather than asserting a search region.",
        "analytical_job": "Define a decreasing quadratic casualty-distance density; compute radar horizon; translate by Gh; model cross-track position normally with sigma_x=Gh sin(pi/8); multiply independent marginals.",
        "output": "A bounded along-track and normal cross-track joint density f(x,Y_I).",
        "handoff": "Discretization integrates this continuous density into region-level probabilities of containment.",
        "transition_cue": "The prose explicitly shifts from a joint density to dividing the search field into distinct regions.",
    },
    {
        "source_headings": ["2.1.1 Partitioning Search Region Through Model Discretization"], "chapter": "algorithm", "pages": [6, 8],
        "input": "The joint density, three-sigma cross-track support, search-plane speed, and a half-hour cell traversal target.",
        "rhetorical_job": "Make a continuous location prior actionable as a finite matrix with a time interpretation.",
        "analytical_job": "Bound x at three standard deviations; choose N by along-track span divided by 0.5 v_s; divide into N by 6 cells; exploit symmetry; integrate each cell in Mathematica.",
        "output": "A source-ordered list of POC values assigned to an N by 6 search-region matrix.",
        "handoff": "Coordinate transformation converts each selected cell from IFP-relative miles to latitude and longitude.",
        "transition_cue": "The last paragraph says the probability cells now need operational coordinate boundaries.",
    },
    {
        "source_headings": ["2.1.2 Finding Latitude and Longitude Coordinates for Search Regions"], "chapter": "data-preprocessing", "pages": [8, 9],
        "input": "Integer cell indices, sigma_x, the along-track partition, y0 and yB in local and geographic systems, and the flight-vector components.",
        "rhetorical_job": "Close the gap between a mathematical grid and coordinates a search-and-rescue team can receive.",
        "analytical_job": "Assemble corner matrix C; infer orientation phi; choose the sign-specific rotation R; check det(R)=1; scale and translate to C_L.",
        "output": "Latitude-longitude coordinates for every bounding corner of a selected region.",
        "handoff": "POD next quantifies whether search assets can detect the target while traversing such a region.",
        "transition_cue": "The coordinate summary ends Section 2.1 before Section 2.2 changes from where to search to whether a search detects.",
    },
    {
        "source_headings": ["2.2 Probability of Detection"], "chapter": "model-improvement", "pages": [10, 10],
        "input": "One cell's area, effective detection distance, search altitude, condition factor, swept distance, synchronized aircraft count, and parallel-swath geometry.",
        "rhetorical_job": "Retain containment and detection as separate probabilities and make resource/scenario changes enter through named parameters.",
        "analytical_job": "Adapt Koopman's exponential; compute A_S, projected detection reach, sweep width S, distance per swath d_s, effort d_s n, and final POD.",
        "output": "A region-level POD that can be uniform when search effort does not vary by region.",
        "handoff": "Nondetection uses POD to update the searched region's POC.",
        "transition_cue": "The final sentence fixes the uniform-POD regime before Section 2.3 asks what a missed search changes.",
    },
    {
        "source_headings": ["2.3 The POC-Updating Algorithm", "2.3.1 Using the POC-Updating Algorithm to Determine Search Pattern"], "chapter": "robustness-verification", "pages": [11, 11],
        "input": "An N by 6 POC matrix, region-specific POD, the just-searched cell, and its adjacent neighbors.",
        "rhetorical_job": "Connect imperfect sensing to the next operational action rather than treating one unsuccessful pass as elimination.",
        "analytical_job": "Retain POC_q(1-POD_q) in the searched cell; spread removed mass across other cells; compare updated adjacent POCs; choose the highest neighbor to reduce nonadjacent travel.",
        "output": "An iterative POC map and local next-region sequence that permits later revisits.",
        "handoff": "The assumption list defines when the distribution, detector, and path sequence are intended to apply.",
        "transition_cue": "After defining the search loop, the paper pauses to disclose its operating assumptions.",
    },
    {
        "source_headings": ["2.4 Assumptions in the Methodology"], "chapter": "assumptions", "pages": [12, 12],
        "input": "The complete containment, detection, and search-pattern chain.",
        "rhetorical_job": "Expose physical and resource idealizations before sensitivity or claims of transfer.",
        "analytical_job": "Fix a linear route, glide-before-impact, water-impact breakup, three-sigma deviation, stationary debris, constant speeds, near-contact prior, persistent detectability, and homogeneous search aircraft.",
        "output": "A nine-item operating contract for the model and worked example.",
        "handoff": "Sensitivity analysis varies selected parameters inside this contract.",
        "transition_cue": "The next heading explicitly changes from fixed assumptions to parameter effects.",
    },
    {
        "source_headings": ["2.5 Sensitivity Analysis"], "chapter": "sensitivity-robustness", "pages": [12, 15],
        "input": "The joint density and POD equations plus G, deviation angle theta, search altitude h_s, effective range, condition factor, and search-plane count n.",
        "rhetorical_job": "Show which inputs control probability concentration, detectability, feasibility, and resource response.",
        "analytical_job": "Plot density response to G/theta; plot POD(theta), POD(G), POD(h_s), and POD(n); state the h_s < kappa epsilon feasibility condition; interpret accommodation versus robustness.",
        "output": "A directional parameter-to-response map and an explicit sensor-reach feasibility boundary.",
        "handoff": "Strengths and weaknesses evaluate the mechanisms revealed by the construction and sensitivity pass.",
        "transition_cue": "The final paragraph distinguishes sensitivity needed for accommodation from robust behavior before formal evaluation begins.",
    },
    {
        "source_headings": ["2.6 Strengths and Weaknesses of Our Model", "2.6.1 Strengths", "2.6.2 Weaknesses"], "chapter": "strengths-limitations", "pages": [15, 16],
        "input": "The nonuniform prior, trajectory mapping, coordinate transform, condition-adjusted POD, updating rule, neighborhood restriction, and assumption set.",
        "rhetorical_job": "Attribute reuse value to concrete mechanisms and name omissions without allowing criticism to replace the positive chain.",
        "analytical_job": "Contrast the quadratic prior with uniform time; credit trajectory and coordinate conversion; explain kappa and updating; identify cross-track allocation distortion and omitted currents.",
        "output": "A mechanism-specific capability and boundary record plus two repair targets.",
        "handoff": "Flight ABCD demonstrates how the retained mechanisms connect numerically.",
        "transition_cue": "The evaluation closes with currents, then a new major heading opens the worked example.",
    },
    {
        "source_headings": ["3 Working Example: Flight ABCD to Lisbon, Portugal Reported Missing"], "chapter": "results", "pages": [16, 23],
        "input": "Boston-Lisbon endpoints, last-contact coordinates, B777 speed/altitude/glide ratio, search-plane speed/altitude/instrument, kappa=0.98, and eight aircraft.",
        "rhetorical_job": "Demonstrate that the model is an end-to-end procedure rather than disconnected formulas.",
        "analytical_job": "Instantiate f_YC, f_YI, f(x), and f(x,Y_I); integrate 36 POCs; calculate POD=0.677831; generate adjacent and unrestricted paths; transform one cell to latitude-longitude corners.",
        "output": "A complete scenario record with probability surfaces, cell matrix/map, search path, comparator, and operational coordinates.",
        "handoff": "The conclusion generalizes the resource and neighborhood lessons while retaining the currents gap.",
        "transition_cue": "After the coordinate table and Appendix B pointer, Section 4 switches from demonstration to recommendation.",
    },
    {
        "source_headings": ["4 Conclusion"], "chapter": "conclusion", "pages": [23, 23],
        "input": "Flight ABCD results, sensitivity relationships, fleet-size effect, neighborhood path comparison, and the omitted-current limitation.",
        "rhetorical_job": "Return the technical chain to time efficiency, resource choice, and a bounded search recommendation.",
        "analytical_job": "Emphasize parameterized aircraft/search assets, increased detection with more planes, local travel reduction, and future current/debris modeling.",
        "output": "A neighborhood-search recommendation conditioned on careful resource selection and an explicit drift extension.",
        "handoff": "The press-conference summary translates the same route for a nontechnical audience.",
        "transition_cue": "The conclusion's future-work sentence is followed immediately by a new audience and register.",
    },
    {
        "source_headings": ["5 Summary for an Airline's Press Conference"], "chapter": "memo", "pages": [23, 24],
        "input": "Public concern about MH370 and the paper's last-contact-to-neighborhood-search method.",
        "rhetorical_job": "Translate the full technical workflow into chronological operations and a small set of understandable restrictions.",
        "analytical_job": "Explain search-region narrowing, glide-based impact prediction, POC, POD and added parties, miss-driven next-neighbor selection, revisits, straight-path difficulty, and assumptions.",
        "output": "A public-facing explanation of prediction, detection, iterative search, resource adjustment, and restricted applicability.",
        "handoff": "References and appendices expose the external evidence and computational artifacts behind the explanation.",
        "transition_cue": "The public prose ends before the document switches to bibliography and implementation material.",
    },
    {
        "source_headings": ["References"], "chapter": "references", "pages": [25, 25],
        "input": "Claims about glide, search theory, radar coverage, missing-aircraft prevalence, and Air France/MH370 evidence.",
        "rhetorical_job": "Expose the external basis of major model choices and contextual claims.",
        "analytical_job": "Map six citations to flight physics, Koopman/search theory, radar range, missing-aircraft context, and incident comparison.",
        "output": "A concise provenance map whose external bytes and calibration datasets are not frozen with the paper.",
        "handoff": "Appendices expose the authors' own integration, transform, update, and path-generation artifacts.",
        "transition_cue": "Appendix A begins on the same page immediately after the final reference.",
    },
    {
        "source_headings": ["6 Appendix A", "7 Appendix B", "8 Appendix C", "9 Appendix D"], "chapter": "appendix", "pages": [25, 32],
        "input": "The declared formulas, Flight ABCD parameters, region POCs, coordinate conversion, and two search-pattern variants.",
        "rhetorical_job": "Expose enough computational structure to audit interfaces and outputs even though a fully executable archive is absent.",
        "analytical_job": "Show regional integration loops, Excel coordinate tables, parameter/POC initialization, POD code, miss updates, local/global minimum selection, tie handling, and printed region sequences.",
        "output": "Partial reproduction artifacts for the POC grid, coordinate handoff, adjacent path, and nonadjacent comparator.",
        "handoff": "The document terminates after program output; no later section resolves code, notation, or reproducibility gaps.",
        "transition_cue": "Appendix D's printed sequence is the final source artifact.",
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
            "official_problem_statement_status": "not-available-in-manifest",
            "paper_explicit_task": "Create a time-efficient mathematical model and operational search plan for a signal-less transoceanic flight with sparse prior information, including containment, detection, iterative search order, a worked example, and public explanation.",
            "stakeholders": ["air traffic control", "search-and-rescue coordinators", "search-plane crews", "airlines", "passengers' families", "press and public"],
            "required_outputs_observed": ["impact-location density", "POC grid", "latitude-longitude cell bounds", "POD", "nondetection update", "neighborhood path", "sensitivity analysis", "Flight ABCD example", "recommendation", "press summary", "code appendices"],
        },
        "source_heading_map": [{"source_headings": item["source_headings"], "normalized_chapter": item["chapter"], "pages": item["pages"]} for item in CONTRACTS],
        "global_progression": [
            "offshore observation gap and sparse-prior motivation", "containment-detection-updating decomposition", "casualty and impact probability construction", "timed POC-grid discretization", "coordinate handoff to search teams", "resource- and condition-aware detection", "miss-driven probability update", "adjacent next-cell selection", "assumption contract", "parameter and feasibility response", "mechanism-specific evaluation", "end-to-end Flight ABCD demonstration", "resource-aware recommendation", "public translation", "provenance and computational boundary",
        ],
        "section_contracts": contracts,
        "paragraph_chains": {
            "abstract": [
                chain(1, "containment-construction", "Last contact and aircraft trajectories can define a bounded probability field.", "the paragraph sequences casualty distance, glide, deviation, discretization, and POC", "the priors and trajectory assumptions are source-selected rather than incident-calibrated", "creates the spatial search input", "moves from where the plane may be to whether a search detects it", [au[0], au[1]]),
                chain(2, "detection-to-action", "Imperfect detection should alter both retained probability and the next searched neighbor.", "Koopman POD, redistribution, adjacency, time/resource efficiency, and Flight ABCD are named in operational order", "the neighborhood rule is a heuristic rather than a proven global optimum", "creates an iterative search loop", "moves to the assumptions and transfer properties", [au[2]]),
                chain(3, "scope-and-transfer", "The procedure is parameterized across plane types but only inside explicit physical assumptions.", "the paragraph names linear IFP, water-impact breakup, sensitivity, nonuniform distributions, and continuous updating", "parameter accommodation does not establish robustness or field validation", "states strengths and the operating boundary", "the Introduction must justify the sparse-prior need", [au[3]]),
            ],
            "introduction": [
                chain(1, "observation-gap", "Transoceanic flights become hard to locate beyond coastal radar.", "83 vanished aircraft, a 200-mile radar radius, and scheduled communication checks establish the gap", "the historical count and radius are contextual citations", "defines the missing-observation trigger", "contrasts prior-information cases", [iu[0]]),
                chain(2, "case-contrast", "Bayesian search is most useful when incident evidence can eliminate zones, while sparse priors leave a harder problem.", "Air France 447 has weather, bodies, and beacon evidence; MH370 has delayed search and little prior information", "the comparison is illustrative rather than a controlled study", "isolates the unmet sparse-prior case", "states a new model objective", [iu[1], iu[2]]),
                chain(3, "objective", "A signal-less flight with indefinite casualty time and possible IFP deviation needs a time-efficient mathematical search plan.", "the paragraph names casualty timing, deviation, sparse information, and time priority", "the source does not yet define a field-validation target", "commits the paper to an end-to-end procedure", "Section 2 decomposes the procedure", [iu[3]]),
            ],
        },
        "main_argument_chains": [
            {"name": "sparse-evidence-to-location-field", "chain": ["last reliable communication", "quadratic casualty-distance prior", "coastal radar horizon", "glide translation", "cross-track normal deviation", "joint impact density"], "decision": "represent the unknown aircraft location as a bounded, source-parameterized probability field"},
            {"name": "location-field-to-operational-cells", "chain": ["three-sigma cross-track bound", "half-hour along-track partitions", "N by 6 regional integrals", "POC matrix", "corner matrix", "rotation determinant check", "latitude-longitude coordinates"], "decision": "hand search teams finite probability cells with operational bounds"},
            {"name": "sensor-and-miss-to-next-action", "chain": ["cell area", "effective sensor reach", "sweep width and effort", "POD", "searched-cell residual POC", "mass redistribution", "adjacent updated POC comparison", "next region"], "decision": "let imperfect detection change a travel-aware local search sequence"},
            {"name": "parameter-and-example-to-recommendation", "chain": ["G/theta/altitude/fleet sensitivity", "sensor feasibility", "Flight ABCD parameters", "36-cell POC", "POD 0.677831", "adjacent versus unrestricted paths", "coordinate output", "resource-aware conclusion"], "decision": "recommend the neighborhood method only with incident-specific parameters and sufficient search resources"},
            {"name": "technical-to-public-and-reproducibility", "chain": ["model restrictions", "plain-language POC and POD", "miss feedback and revisits", "public commitment", "six external references", "Mathematica/Excel appendices", "unresolved execution boundary"], "decision": "communicate the method from typed evidence while preserving restrictions and provenance gaps"},
        ],
        "organization_skeleton_test": {
            "status": "pass",
            "result": "With aircraft names, values, and equations removed, the positive route remains observation gap -> sparse-prior objective -> state distribution -> operational discretization -> coordinate handoff -> detection -> miss update -> local action -> assumptions -> sensitivity -> worked demonstration -> bounded decision -> audience translation -> reproducibility boundary.",
            "weakness_substitution": False,
        },
    }
    STAGE.mkdir(parents=True)
    output = STAGE / "organization.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "section_contracts": len(contracts), "main_argument_chains": len(result["main_argument_chains"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
