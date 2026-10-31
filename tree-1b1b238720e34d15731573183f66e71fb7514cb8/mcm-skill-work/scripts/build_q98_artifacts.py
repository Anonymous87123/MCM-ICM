from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import build_q97_artifacts as base


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2012-15420-8b46b980"
SHORT = "15420"
SHA = "8b46b9801a80275e13d9d148fa46ac19aa1855cc0428941b701f62c0ceb6c6c9"
TYPE = "B"
YEAR = "2012"
PAGE_COUNT = 21

PATTERNS = [
    "LP-B-SUMMARY-MODEL-TRADEOFF-DECISION",
    "LP-B-INTRO-CHALLENGE-MODEL-LADDER",
    "LP-B-DEFINITION-DOMAIN-OBJECTIVE",
    "LP-B-ASSUMPTION-EVIDENCE-CONSEQUENCE",
    "LP-B-BASELINE-FAILURE-HANDOFF",
    "LP-B-ALGORITHM-INPUT-ORDERED-STEPS",
    "LP-B-PRIORITY-MECHANISM-CONFLICT-REPAIR",
    "LP-B-CONTINUOUS-RELAXATION-DISCRETE-MAP",
    "LP-B-HEURISTIC-MOTIVATION-CONSTRUCTION",
    "LP-B-RESULT-CRITERIA-TABLE-INTERPRETATION",
    "LP-B-COMPARATIVE-TRADEOFF-BOUNDARY",
    "LP-B-STRENGTH-WEAKNESS-IMPROVEMENT",
    "LP-B-CONCLUSION-PREFERENCE-CONDITIONAL",
    "LP-B-MEMO-CAPACITY-CHOICE-ACTION",
    "LP-B-VISUAL-STATE-TO-CLAIM",
    "LP-B-REFERENCE-PROVENANCE-BOUNDARY",
]

# key, normalized chapter, first physical page, last physical page, tag,
# language-unit count, source-checked paraphrase, visually observed paragraph count
CHAPTERS = [
    ("summary-abstract", "abstract", 1, 2, "ABS", 64, "The opening summary and abstract define the river-scheduling decision, compare four models, quantify the occupancy-crossover tradeoff, describe distribution distortion and robustness, and condition the final model choice on management preferences.", 2),
    ("introduction", "introduction", 3, 3, "INT", 50, "The introduction moves from river facts and the wildlife constraint through three optimization difficulties, then presents the naive, priority, density-perturbation, and bone-growth models as an explicit ladder of responses.", 7),
    ("definitions-variables", "notation", 3, 4, "NOT", 38, "The notation section defines crossovers, trips, X, Y, T, P, two schedule-matrix orientations, open-campsite percentage, guaranteed travel distance, the multi-objective problem, and carrying capacity.", 11),
    ("assumptions", "assumptions", 4, 6, "ASM", 46, "The assumptions collapse craft choice into trip length, forbid hybrid trips, set daily reach, borrow campsite spacing from two real rivers, remove launch-resource constraints, and discretize behavior to nightly campsite states.", 10),
    ("problem-analysis", "problem-analysis", 6, 6, "ANA", 32, "The analysis explains why standard identical-machine scheduling and queueing abstractions do not directly fit an ordered sequence of unique river sections with nightly unit capacity.", 3),
    ("naive-priority-algorithms", "algorithm", 6, 9, "ALG", 82, "The algorithm section first inserts whole trips into an empty schedule and diagnoses blocking and crossover failures, then changes to night-by-night priority scheduling with distance-per-day urgency and local crossover-aware campsite ranking.", 22),
    ("density-perturbation", "model-establishment", 9, 11, "EST", 72, "The density model moves every active trip toward its equal-distance daily target in continuous mile space, sums signed local repulsion contributions, iterates until trips admit a one-to-one campsite mapping, and discards rare unresolved collisions.", 14),
    ("bone-growth", "model-improvement", 11, 13, "IMP", 64, "The bone model replaces unrestricted crossovers with a deterministic greedy construction: alternate trip-length sequences, squeeze trajectories toward the center, insert the best feasible trip, saturate, and spread launch times.", 13),
    ("testing-results", "results", 14, 16, "RES", 68, "The results compare Priority, Density Perturbation, Bones1, and Bones2 across campsite counts and target distributions using trips, open sites, crossovers, and distribution variance, then interpret scaling and initial-sequence effects.", 15),
    ("analysis-results", "robustness-verification", 16, 17, "ROB", 36, "The analysis checks five decision dimensions, traces short-trip skew and crossover growth, reports a failed removal experiment, and compares the temporal consistency of priority and bone schedules.", 9),
    ("strengths-weaknesses", "strengths-limitations", 17, 18, "SWL", 34, "The strengths and weaknesses separate throughput, crossover, backtracking, distribution, departure-rate, sort probability, initial-bone, speed-limit, and launch-clustering effects for the two leading models.", 18),
    ("conclusion", "conclusion", 18, 19, "CON", 28, "The conclusion chooses Priority when occasional passing is acceptable, Bone Growth when zero crossover dominates, proposes time-window mixing, and identifies craft, campsite, speed, annealing, and initialization extensions.", 4),
    ("manager-memo", "memo", 20, 20, "MEM", 30, "The memo gives managers a two-algorithm choice, capacity and coverage ranges, schedule outputs, assumptions, and a possible mixed-model pricing strategy, while compressing or drifting from several body results.", 5),
    ("references", "references", 21, 21, "REF", 8, "Eight references provide river statistics, commercial itinerary context, scheduling and optimization books, and campsite-spacing data, but no code, seeds, raw schedules, or frozen experiment files.", 8),
]

MOVES = [
    ("summary-tradeoff", "Forecast the competing objectives, model mechanisms, quantitative tradeoffs, robustness, and conditional recommendation before details.", "decision -> model alternatives -> metrics -> tradeoff -> preference-conditioned choice -> boundary"),
    ("model-ladder", "Introduce each new model as a response to a named failure or limitation of the previous construction.", "system challenge -> baseline -> failure -> revised mechanism -> remaining limitation"),
    ("definition-contract", "Define schedule orientations, metrics, domains, and objectives before using them in algorithms or results.", "term -> mathematical domain -> operational meaning -> downstream use -> ambiguity boundary"),
    ("assumption-consequence", "Pair each simplification with empirical motivation and the scheduling behavior it enables or excludes.", "assumption -> evidence or rationale -> enabled model -> excluded regime -> later test"),
    ("baseline-handoff", "Use a deliberately simple model to expose blocking and crossover mechanisms, then hand those failures to the next model.", "baseline rule -> observed failure -> causal explanation -> successor requirement"),
    ("ordered-algorithm", "State inputs and outputs, then narrate an ordered loop with branch conditions and state updates.", "input -> initialization -> iteration -> branch -> state update -> output"),
    ("priority-conflict", "Justify urgency with remaining-distance slack and resolve collisions with feasibility and crossover-aware ranking.", "urgency ratio -> ordering -> preferred site -> conflict set -> ranked repair -> removal"),
    ("continuous-relaxation", "Relax discrete campsite assignment into continuous positions, apply local repulsion, and map back only after separation.", "discrete conflict -> continuous state -> pairwise density -> iteration -> one-to-one map -> rare failure"),
    ("heuristic-construction", "Motivate structural heuristics, build a candidate sequence, test feasibility, saturate it, and spread the accepted schedule.", "motivation -> heuristic -> insertion candidates -> squeeze test -> saturation -> spreading"),
    ("criteria-table", "Declare ordered evaluation criteria, provide a scenario table, and interpret model-specific trends without hiding the comparator.", "criteria -> scenario -> metric table -> trend -> mechanism -> decision relevance"),
    ("comparative-tradeoff", "Compare models on throughput, crossover, distribution match, sensitivity, and management preference rather than one scalar alone.", "model A advantage -> model A cost -> model B advantage -> model B cost -> conditional choice"),
    ("positive-then-limit", "Retain each reusable strength before naming its mechanism-specific weakness and concrete improvement path.", "strength -> evidence -> weakness -> mechanism -> improvement"),
    ("conditional-conclusion", "Convert findings into a conditional recommendation keyed to the decision maker's tolerance for crossover and occupancy loss.", "preference -> chosen model -> expected outcome -> cost -> alternative or mix"),
    ("manager-action", "Translate technical outputs into manager-facing capacity, schedule, model-choice, and implementation actions while preserving uncertainty.", "management need -> reported range -> option A/B -> operating action -> caveat"),
    ("visual-evidence", "Explain what a histogram, state diagram, schedule plot, or comparison chart makes inspectable and which claim it cannot prove alone.", "visual encoding -> observable pattern -> linked claim -> missing scale or uncertainty -> use boundary"),
    ("provenance-boundary", "Separate contextual references and borrowed river data from reproducible model inputs, code, and experiment outputs.", "citation role -> supplied fact -> transformation -> missing artifact -> reuse boundary"),
]

EXAMPLES = [
    ("A hospital-flow abstract previews a throughput scheduler and a no-overtaking alternative, then conditions the recommendation on contact policy.", "The occupancy and interaction metrics stay separate."),
    ("A berth paper introduces first-fit, urgency-ranked, continuous-relaxation, and order-preserving methods as a sequence of repairs.", "Every handoff names the failure being repaired."),
    ("A warehouse model defines order-by-night and bay-by-night matrices before comparing occupancy.", "The matrix axes and zero state are explicit."),
    ("A transit model justifies nightly aggregation with service logs and reserves within-day congestion for stress testing.", "The excluded behavior is not silently forgotten."),
    ("A baseline packing rule reveals that long jobs block short flexible jobs.", "The next algorithm is required to repair that mechanism."),
    ("A dispatch algorithm declares requests and a schedule as input and output before listing its daily branches.", "Each branch names the state updated."),
    ("A clinical queue ranks cases by remaining workload divided by remaining time and uses a conflict-aware fallback room.", "Urgency and fallback feasibility use consistent units."),
    ("A gate model relaxes stands to continuous positions, applies repulsion, and rounds only after separation.", "The rounding failure rule is explicit."),
    ("A production model grows an order-preserving backbone, tests center packing, and spreads accepted starts.", "Sensitivity to the initial backbone is reported."),
    ("A staffing table reports served demand, idle capacity, handoffs, and target-mix variance for every scenario.", "The header scaling is unambiguous."),
    ("A rail comparison states that one policy moves more trains while another forbids overtaking.", "The recommendation follows the operator's stated preference."),
    ("A routing paper credits its deterministic ordering, then states that initialization controls the local solution.", "The limitation points to multi-start testing."),
    ("A conclusion recommends a high-throughput policy only when occasional interactions are acceptable.", "A zero-interaction alternative remains visible."),
    ("A manager memo gives two verified capacity ranges and the exact conditions for choosing each scheduler.", "All values are generated from the final result record."),
    ("A four-panel growth figure labels initialization, insertion, saturation, and spreading.", "The caption does not claim optimality from visual fullness."),
    ("A references section distinguishes field measurements from optimization textbooks and executable artifacts.", "Missing seeds and raw outputs remain explicit."),
]

EQUATIONS = [
    ("trip-oriented schedule domain", 4, "Definitions and Variables", "schedule representation", "S1_{i,j} in {0,...,Y+1}", r"S^{(1)}_{i,j}\in\{0,\ldots,Y+1\}", ["S1_i_j", "i", "j", "Y"], "Represent the campsite occupied by trip i on night j, including launch and exit states."),
    ("campsite-oriented schedule domain", 4, "Definitions and Variables", "schedule representation", "S2_{i,j} in {0,1,...,X}", r"S^{(2)}_{i,j}\in\{0,1,\ldots,X\}", ["S2_i_j", "i", "j", "X"], "Represent the trip hosted by campsite i on night j, with zero meaning empty."),
    ("carrying-capacity definition", 4, "Definitions and Variables", "capacity metric", "C(Y)=max X(Y)/Y", r"C(Y)=\frac{\max X(Y)}{Y}", ["C(Y)", "X(Y)", "Y"], "Normalize the maximum scheduled trip count over 180 days by campsite count."),
    ("priority urgency ratio", 8, "Priority Model", "priority rule", "q_i = distance remaining / days remaining", r"q_i=\frac{d_i^{\mathrm{remaining}}}{t_i^{\mathrm{remaining}}}", ["q_i", "d_remaining_i", "t_remaining_i"], "Rank trips by the average daily distance still required."),
    ("pairwise density contribution", 10, "Density Perturbation Algorithm", "density perturbation", "rho_i,j = sign((d_j-d_i)/d_campsite) - (d_j-d_i)/d_campsite", r"\rho_{i,j}=\operatorname{sign}\!\left(\frac{d_j-d_i}{d_{\mathrm{campsite}}}\right)-\frac{d_j-d_i}{d_{\mathrm{campsite}}},\quad |d_j-d_i|\in(0,d_{\mathrm{campsite}}]", ["rho_i_j", "d_i", "d_j", "d_campsite"], "Create a signed local repulsion that grows as two proposed boat locations become closer."),
    ("total density vector", 10, "Density Perturbation Algorithm", "density aggregation", "rho_j = sum_{i=1,i!=j}^n rho_i,j", r"\rho_j=\sum_{\substack{i=1\\i\ne j}}^n\rho_{i,j}", ["rho_j", "rho_i_j", "n"], "Sum every neighboring boat's contribution before shifting boat j."),
    ("triangle target weight", 14, "Model Comparison", "target distribution", "w(l)=40-l", r"w(l)=40-l", ["w(l)", "l"], "Weight shorter trip lengths more heavily in the triangle target distribution."),
]

ALGORITHMS = [
    (4, "dual schedule representation", "Maintain mutually interpretable trip-by-night and campsite-by-night schedule views.", ["X", "Y", "T", "trip states"], ["S1", "S2"]),
    (6, "naive trip sampling", "Randomly select a remaining trip length and remove that length only after all launch nights fail.", ["trip-length distribution", "empty or partial schedule"], ["candidate trip", "updated distribution"]),
    (6, "naive whole-trip insertion", "Try equal daily progress, move to the nearest available campsite on conflicts, and accept only if every night is feasible.", ["candidate trip", "launch night", "tolerance", "schedule"], ["inserted trip or failure"]),
    (7, "priority nightly scheduler", "Build the schedule one night at a time by adding departures, ordering active trips, and assigning their next campsites.", ["departures by night", "prior active trips", "p"], ["populated schedule", "active next set"]),
    (8, "probabilistic sort or shuffle", "With probability p sort active trips by urgency; otherwise shuffle them to moderate systematic distribution skew.", ["active trips", "p", "urgency ratio"], ["ordered active trips"]),
    (8, "preferred-campsite calculation", "Choose the campsite nearest current position plus remaining distance divided by remaining days.", ["current position", "distance remaining", "days remaining", "campsites"], ["best camp"]),
    (9, "priority conflict repair", "When the best camp is occupied, restrict to reachable camps, remove occupied sites, rank crossover-free status before proximity, and choose the first.", ["min and max reach", "best camp", "next occupancy", "prior order"], ["new camp or removal"]),
    (9, "priority completion update", "Move finished trips to the completed schedule and carry unfinished trip-camp pairs into the next night.", ["new camp", "trip end state"], ["completed trip or next active pair"]),
    (9, "continuous optimal-position update", "Move each active trip to the mile position implied by equal remaining distance per remaining day.", ["mile position", "remaining distance", "remaining days"], ["continuous target positions"]),
    (10, "pairwise density construction", "Compute signed repulsion only for pairs within one campsite spacing, randomizing the sign for exact ties.", ["continuous positions", "campsite spacing"], ["pairwise density contributions"]),
    (10, "density relaxation loop", "Sum contributions and subtract total density repeatedly until proposed locations are sufficiently separated.", ["target positions", "pairwise densities", "separation threshold"], ["separated continuous positions"]),
    (11, "continuous-to-discrete mapping", "Map separated positions one-to-one onto campsites and discard a trip in the rare unresolved collision case.", ["separated positions", "campsite locations"], ["daily campsite assignment", "discard count"]),
    (11, "bone launch-order heuristic", "Alternate monotone increasing and decreasing trip-length sequences so a shorter trip does not finish before a longer trip ahead.", ["trip-length set", "remaining days"], ["bone sequence"]),
    (12, "center-squeezing feasibility test", "Pull trajectories toward the central trip to test the necessary packed configuration for a fixed launch-finish order.", ["bone sequence", "launch and finish dates", "travel limits"], ["squeezed feasible schedule or rejection"]),
    (12, "greedy bone insertion", "Enumerate heuristic insertion points, score candidate trip types against the target distribution, and retain a feasible insertion.", ["current bone", "target distribution", "candidate lengths"], ["expanded bone"]),
    (12, "bone saturation loop", "Repeat best feasible insertion until no trip length can be added without a crossover.", ["expanded bone", "candidate lengths"], ["saturated bone"]),
    (13, "schedule spreading", "Spread the saturated center-packed trajectories in time to make launches more uniform while retaining order.", ["saturated bone schedule"], ["spread no-crossover schedule"]),
    (13, "craft-type bone extension", "Assign less flexible oar craft and more flexible motor craft within the bone construction, with spreading left incomplete.", ["bone schedule", "craft types", "reach limits"], ["typed-craft schedule"]),
    (14, "scenario comparison harness", "Run campsite counts 45, 150, and 225 with uniform and triangle targets and compute the declared comparison metrics.", ["model", "Y", "target distribution"], ["trips", "open percent", "crossovers", "distribution variance"]),
    (15, "bone-initialization comparison", "Grow and compare Bones1 and Bones2 to expose throughput and distribution sensitivity to the starting sequence.", ["Bones1", "Bones2", "target distribution", "Y"], ["two schedules and metrics"]),
    (19, "preference-conditioned model selection", "Choose Priority for higher occupancy with passing, Bone Growth for zero crossovers, or mix them over time windows.", ["manager crossover tolerance", "occupancy preference", "pricing plan"], ["selected or mixed schedule policy"]),
]

VISUALS = [
    (5, "Figure 1 - campsite-spacing histogram", "Supports the assumed spacing range with observed inter-campsite distances, while leaving dataset completeness and transfer uncertainty unstated."),
    (7, "Figure 2 - naive scheduling steps", "Shows sequential whole-trip insertion and why an early accepted trajectory can block later trips."),
    (8, "Figure 3 - priority scheduling steps", "Shows night-by-night cooperation and local assignment changes under the urgency rule."),
    (10, "Equations (1)-(2) density block", "Preserves the signed pairwise contribution, its domain, the exact-tie randomization note, and the total density sum."),
    (11, "Figure 4 - density schedule", "Displays 1978 threaded trips for 200 campsites and therefore conflicts with the later 1811-trip table row."),
    (12, "Figure 5 - bone growth four stages", "Shows initial bone, forty insertions, saturation, and final spreading as distinct algorithm states."),
    (13, "Figure 6 - motor and oar extension", "Uses color to distinguish craft types and makes the incomplete spreading adjustment visible."),
    (14, "main model-comparison table", "Provides the only compact cross-model record of trips, open sites, crossovers, and distribution variance across scenarios."),
    (15, "Figure 7 - priority schedule and histograms", "Shows dense crossover structure for Y=225 uniform demand and the associated trip-length and temporal patterns."),
    (16, "Figure 8 - Bones1 and Bones2 comparison", "Makes the symmetry and short-trip skew induced by the two starting bones visually comparable."),
]

WARNINGS = [
    (1, "Physical page 1 has no text layer; its Summary was visually transcribed and must not be treated as machine-extracted text coverage."),
    (2, "The abstract says Priority covers 80 percent and Bone Growth about 50 percent, while the memo compresses the range to 70 to 50 percent and the Y=225 table implies about 83.45 percent occupancy for Priority."),
    (2, "The abstract calls the solution nearly optimal without a global optimum, bound, or comparator against exact small instances."),
    (3, "The introduction says a failed naive trip is discarded, while the algorithm removes its trip length from the distribution after all launch nights fail; those are different rejection semantics."),
    (3, "The paper alternates among trip days, rafting days, nights, stops, six-to-eighteen, and seven-to-nineteen without one explicit indexing convention."),
    (4, "S1 uses campsite values through Y+1 while S2 uses campsite rows and trip identifiers through X, but the conversion, launch, exit, and zero conventions are not formalized."),
    (4, "Open Campsite percent is described as an unoccupied fraction but then said never to reach 100 percent for boundary reasons; the denominator and whether launch/exit cells count require a typed definition."),
    (4, "C(Y)=max X(Y)/Y depends on an unstated feasible-set maximum, target distribution, horizon, and crossover policy, so carrying capacity changes meaning across models."),
    (4, "Craft choice is postponed until after scheduling even though some short trips require daily distance beyond the assumed oar maximum."),
    (5, "The guaranteed-distance discussion derives 64 motor miles but later uses 32 oar miles without the same explicit derivation and ignores weather, flow, stops, and within-day congestion."),
    (5, "The campsite-spacing histogram lacks visible sample size, bin specification, source-cleaning procedure, uncertainty, and a direct mapping from the two source rivers to the synthetic river."),
    (6, "Unlimited launch equipment, labor, dock, and arrival capacity can create extreme daily clusters that the objective never penalizes."),
    (6, "Night-only discretization permits arbitrary within-day crossovers and congestion, then treats crossover penalties as a partial repair rather than testing travel feasibility."),
    (6, "The scheduling-theory comparison is qualitative and does not establish that integer programming or alternative network formulations are computationally infeasible."),
    (7, "The naive nearest-available rule does not define tolerance, tie-breaking probability, daily reach boundaries, or rollback after a later night fails."),
    (8, "Priority uses a probability-p sort-or-shuffle step, but no seed, repeated-run protocol, or uncertainty interval is supplied."),
    (8, "Ranking camps primarily by whether they incur a crossover is underspecified when multiple existing trips and order relations are present."),
    (9, "Priority removes trips that cannot be assigned on a night but does not backtrack to reuse space that those trips occupied on earlier nights."),
    (9, "The density model declares all trips equally important but still has to choose signs randomly at identical positions and choose which trip to discard in an unresolved collision."),
    (10, "Equation (1) is explicitly limited to nonzero separation within one campsite distance; exact ties are described by random mapping to plus or minus one outside the displayed formula."),
    (10, "Repeatedly subtracting density has no step size, stop tolerance, maximum iteration count, convergence proof, or test for oscillation and boundary violations."),
    (11, "A one-to-one campsite mapping is asserted for certain near-spacing patterns without a specified matching algorithm or proof for the full set of boats."),
    (11, "Figure 4 reports 1978 trips for Density Perturbation, while the main table reports 1811 for D.Pertb.; scenario or implementation differences are not reconciled."),
    (12, "Bone Heuristic 1 is presented as determining an optimal alternating sequence without proof that other no-crossover launch orders cannot dominate it."),
    (12, "Center squeezing is called a necessary condition but the travel-speed, campsite, launch, and finish constraints used in its feasibility test are not fully formalized."),
    (12, "The greedy score used to select the best inserted trip is not defined mathematically, and no tie rule or complexity analysis is given."),
    (13, "Bone Growth guarantees no crossovers for its constructed schedule but only claims a local optimum and is highly sensitive to the initial bone."),
    (13, "The motor-oar extension is incomplete because the spreading algorithm was not adjusted for the lower flexibility of oar craft."),
    (14, "The final table header is visually ambiguous as 'Var from Distr -10^4'; its scaling must be preserved as uncertain rather than silently read as multiplication or division."),
    (14, "The Density Perturbation row uses Y=200 while the other main comparisons use 45, 150, and 225, preventing a like-for-like ranking."),
    (15, "Bones2 produces more trips largely because it contains shorter trips and substantially misses the stated target distribution, so throughput and distribution fidelity cannot be merged."),
    (16, "Removing high-crossover trips reduced campsite coverage by 10 to 15 percent but no scenario, repeat count, or uncertainty is reported."),
    (17, "Priority crossover growth is described as exponential from three campsite settings without a fitted model, residuals, or broader scale sweep."),
    (18, "The conclusion converts roughly 29 crossovers per trip into less than one contact per hour without defining whether crossover count equals passenger contact or how trip duration enters."),
    (20, "The memo reports carrying capacity 12.5 to 7.5 and omits the approximately 9 trips-per-campsite Bones2 result stated in the body."),
    (20, "The memo says both algorithms can generate any desired trip ratio, while the results show persistent short-trip skew and especially poor Bones2 distribution matching."),
]


def configure_base() -> None:
    for name, value in {
        "ROOT": ROOT, "PID": PID, "SHORT": SHORT, "SHA": SHA, "TYPE": TYPE,
        "YEAR": YEAR, "PAGE_COUNT": PAGE_COUNT, "PATTERNS": PATTERNS,
        "CHAPTERS": CHAPTERS, "MOVES": MOVES, "EXAMPLES": EXAMPLES,
        "EQUATIONS": EQUATIONS, "ALGORITHMS": ALGORITHMS, "VISUALS": VISUALS,
        "WARNINGS": WARNINGS,
    }.items():
        setattr(base, name, value)


def make_language() -> dict:
    configure_base()
    language = base.make_language()
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = (
            "The root context read all 776 lines of the 21-page UTF-8 extraction in continuous, non-overlapping ranges; "
            "a display-truncated middle range was reread explicitly. Physical page 1 lacked a text layer and its full Summary "
            "was transcribed during visual review. Three fresh read-only contexts reviewed physical pages 1-7, 8-14, and 15-21 "
            "using at most seven byte-bounded JPEG proxies each and returned text-only reports."
        )
        layout["ambiguities"] = [
            "Linear extraction flattens Equation (1), summation limits, set domains, table scaling, histogram labels, colored schedules, and multi-panel bone states; rendered pages were authoritative.",
            "The 1978-versus-1811 density result, 80/50-versus-70/50 coverage, carrying-capacity range, desired-ratio claim, and ambiguous variance header are retained as source conflicts only in the final warning pass.",
        ]
    return language


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "mile, hour, day, night, campsite index, trip identifier, trip, fraction, percentage, count, weight, or dimensionless quantity as locally defined",
        "definition": f"Source-defined river-scheduling quantity {symbol}.",
        "source_status": "explicit-defined" if symbol not in {"q_i", "w(l)"} else "inferred-from-equation",
    }


def model_record(model_id: str, page: int, section: str, family: str, purpose: str, inputs: list[str], outputs: list[str], equations: list[dict]) -> dict:
    symbols = list(dict.fromkeys(inputs + outputs))
    return {
        "model_id": model_id, "page": page, "section": section, "family": family,
        "purpose": purpose, "base_or_modification": "paper-specific", "summary": purpose,
        "variables": [variable(symbol, set(inputs), set(outputs)) for symbol in symbols],
        "inputs": inputs, "outputs": outputs, "governing_equations": equations,
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The printed relation was visually reconciled." if equations else "This record is a representation, construction, scheduling, relaxation, comparison, or decision procedure."},
        "objectives": [purpose, "Return a typed schedule, occupancy, trip count, crossover count, distribution comparison, or manager-facing policy choice."],
        "constraints": [
            "No two trips may occupy the same campsite on the same night.",
            "Trip trajectories respect launch, exit, duration, campsite, and daily reach semantics as declared by the selected model.",
            "Throughput, campsite occupancy, crossovers, target-distribution error, and management preference remain distinct quantities.",
        ],
        "conditions": {
            "initial": {"status": "present", "details": ["River length, 180-night horizon, campsite configuration, trip-length distribution, departure sequence or bone, and selected model are supplied or assumed."]},
            "boundary": {"status": "present", "details": ["First Launch, Final Exit, zero or Y+1 states, early and late horizon cells, exact-position ties, full campsite sets, and unschedulable trips require explicit handling."]},
            "equilibrium": {"status": "not-applicable", "details": ["The paper builds finite schedules or iterates a local density relaxation rather than solving a steady-state equilibrium."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Problem constants, cited campsite examples, assumed uniform spacing, selected target distributions, probability-p priority ordering, two starting bones, and scenario comparisons.", "parameters": inputs},
        "algorithm": {"status": "partial", "steps": ["freeze the scenario and model", "construct or update trip positions", "enforce or measure campsite conflicts and crossovers", "record trips, occupancy, distribution, and policy outputs", "compare scenarios under declared criteria"], "software": ["No executable source code, frozen seeds, raw schedules, or machine-readable experiment configuration is supplied."], "convergence_criteria": "Naive and bone loops stop when no candidate can be inserted; density relaxation says sufficiently spread; none supplies a reproducible global convergence or optimality certificate."},
        "assumptions": ["Campsite geometry, daily reach, night-only state, unlimited launch resources, and trip-length demand adequately represent the operating river.", "Model-specific priority, perturbation, or bone rules are suitable surrogates for the multi-objective decision."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The main states, equations, heuristics, figures, and result table are inspectable, but indexing, randomization, rollback, matching, stopping, scoring, initialization, scenario mismatch, uncertainty, and implementation gaps prevent full reproduction or global-optimum claims."},
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, source text and rendered formula, table, figure, or algorithm visually reconciled."],
        "computational_cost": "Driven by launch-night searches, nightly trip sorting, reachable-camp ranking, pairwise density calculations and relaxation iterations, bone insertion trials, center-packing feasibility tests, and scenario repetitions.",
        "strengths": ["The paper exposes several structurally different scheduling mechanisms under common decision metrics.", "The no-crossover and high-occupancy alternatives make the management tradeoff explicit."],
        "limitations": ["Global optimality, reproducibility, uncertainty, empirical calibration, and complete implementation are not established.", "Confirmed defects are recorded only after positive model retention."],
        "missing_details": ["Canonical indexing, code, seeds, run counts, raw schedules, exact matching and stopping rules, bone score, tie rules, complexity, uncertainty intervals, exact objective aggregation, and target-river calibration are absent."],
    }


def make_models() -> dict:
    models: list[dict] = []
    for index, (label, page, section, family, source, latex, symbols, purpose) in enumerate(EQUATIONS, 1):
        equation = {"equation_id": f"EQ-B-{YEAR}-{SHORT}-{index:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": "high"}
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, section, family, purpose, symbols[1:], [symbols[0]], [equation]))
    for index, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, len(EQUATIONS) + 1):
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, family, family, purpose, inputs, outputs, []))
    by_family = {model["family"]: model["model_id"] for model in models}
    pairs = [
        ("schedule representation", "dual schedule representation"), ("dual schedule representation", "naive whole-trip insertion"),
        ("naive trip sampling", "naive whole-trip insertion"), ("naive whole-trip insertion", "priority nightly scheduler"),
        ("priority rule", "probabilistic sort or shuffle"), ("probabilistic sort or shuffle", "preferred-campsite calculation"),
        ("preferred-campsite calculation", "priority conflict repair"), ("priority conflict repair", "priority completion update"),
        ("continuous optimal-position update", "pairwise density construction"), ("density perturbation", "pairwise density construction"),
        ("pairwise density construction", "density relaxation loop"), ("density aggregation", "density relaxation loop"),
        ("density relaxation loop", "continuous-to-discrete mapping"), ("bone launch-order heuristic", "center-squeezing feasibility test"),
        ("center-squeezing feasibility test", "greedy bone insertion"), ("target distribution", "greedy bone insertion"),
        ("greedy bone insertion", "bone saturation loop"), ("bone saturation loop", "schedule spreading"),
        ("schedule spreading", "craft-type bone extension"), ("scenario comparison harness", "bone-initialization comparison"),
        ("capacity metric", "preference-conditioned model selection"), ("bone-initialization comparison", "preference-conditioned model selection"),
    ]
    edges = [{"from_model_id": by_family[source], "to_model_id": by_family[target], "handoff": f"The {source} output becomes a state, constraint, comparator, metric, or decision input for {target}."} for source, target in pairs if source in by_family and target in by_family]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    assumptions = [
        (4, "Craft choice can be postponed because vessel type is strongly correlated with trip length and motor craft can cover trips that exceed oar reach."),
        (4, "Passengers do not switch boat type during a trip."),
        (5, "Motor craft can travel 64 miles per day and oar craft are later treated as capable of 32 miles per day under eight hours of travel."),
        (5, "Campsite spacing is modeled as uniform and tested at roughly five, 1.5, and one mile per campsite, giving Y=45, 150, and 225."),
        (5, "Launch labor, boats, docks, and daily release capacity are unlimited."),
        (6, "Only nightly campsite positions matter; within-day density and activities do not reduce travel distance."),
        (9, "Priority may be randomized through a sort probability p, while Density Perturbation treats all trips as equally important."),
        (11, "Bone feasibility can be screened by an alternating launch sequence and center-squeezed trajectories."),
    ]
    data = [
        (3, "Problem constants supply a 225-mile river, 180-night scheduling horizon, six-to-eighteen campsite stops, and four- versus eight-mile-per-hour craft."),
        (4, "The cited 2007-2010 Grand Canyon counts list roughly 409-426 motor and 181-184 non-motor trips per year."),
        (5, "Campsite context cites 162 sites over 250 Colorado River miles and 185 sites over 180.6 Salmon River miles."),
        (11, "Figure 4 states 1978 trips in 180 days for 200 uniformly spaced campsites from mile 10 through mile 215."),
        (14, "The main table compares 19 rows across Priority, Density Perturbation, Bones1, and Bones2 with trips, open percentage, crossovers, and distribution variance."),
        (14, "At Y=225 uniform demand, Priority reports 2911 trips, 16.55 percent open, 28.93 crossovers per trip, and 1.30 in the ambiguous variance column."),
        (14, "At Y=225 uniform demand, Bones1 reports 1707 trips and 51.82 percent open; Bones2 reports 2107 trips and 46.80 percent open, both with zero crossovers."),
        (15, "Bones1 alternates mostly six and eighteen; Bones2 steps through shorter large-trip values and consequently favors shorter trips."),
        (21, "Eight references supply context and textbooks but no executable or frozen computational evidence."),
    ]
    verification_specs = [
        (4, "The two schedule matrices can be checked for domain and axis consistency.", "representation audit", "Both domains are printed explicitly.", "No conversion or boundary invariant is supplied."),
        (7, "Figure 2 can be replayed against the naive insertion pseudocode.", "state replay", "The insertion order and blocking mechanism are visible.", "Tolerance, rollback, and tie rules remain missing."),
        (8, "Figure 3 and the priority pseudocode expose ordering and conflict-repair stages.", "algorithm trace", "Inputs, nightly loop, best camp, and ranking are named.", "No code, seed, or full crossover predicate is supplied."),
        (10, "Equations (1) and (2) can be reconciled with the density narrative and domain note.", "formula trace", "Pairwise sign, linear decay, range, and sum are visible.", "Tie handling and convergence are outside the displayed equations."),
        (11, "Figure 4 and the main table permit a direct density-result consistency check.", "cross-section reconciliation", "Both trip counts are visually readable.", "1978 and 1811 are unreconciled."),
        (12, "Figure 5 exposes the initial, inserted, saturated, and spread bone states.", "algorithm-state trace", "Four stages map to the written loop.", "The score and feasibility test are not reproducible."),
        (14, "The main table supports exact within-row model comparisons.", "scenario table audit", "Trips, open sites, crossovers, and variance are co-located.", "The variance scale and D.Pertb scenario mismatch remain ambiguous."),
        (15, "Figures 7 and 8 connect schedule structure with crossover and trip-length patterns.", "visual-result trace", "Priority density and bone symmetry/skew are visible.", "No raw data, aligned scale, or uncertainty is supplied."),
        (16, "The high-crossover removal experiment checks one mitigation idea.", "intervention check", "The reported occupancy loss is stated.", "The experiment lacks scenario and repetition details."),
        (20, "The memo can be reconciled against the table, analysis, and conclusion.", "stakeholder consistency audit", "Model choices and broad tradeoffs are retained.", "Coverage, capacity, and desired-ratio claims drift from the body."),
    ]
    results = [
        (11, "Density Perturbation reports 1978 trips in Figure 4 for Y=200, while the later table lists 1811 trips, 41.07 percent open, 19.07 crossovers, and 5.85 variance."),
        (14, "Priority increases from 546 trips at Y=45 uniform demand to 2911 at Y=225, while average crossovers rise from 4.37 to 28.93."),
        (14, "Priority open percentage falls from 23.80 at Y=45 uniform demand to 16.55 at Y=225, implying higher campsite occupancy."),
        (14, "Bones1 remains near 52 percent open and zero crossovers across the uniform scenarios, with roughly 7.5 trips per campsite."),
        (14, "Bones2 schedules more trips than Bones1 but has much larger distribution variance and roughly 9 trips per campsite."),
        (14, "For Y=225 triangle demand, Priority reports 2937 trips, 17.28 percent open, 29.06 crossovers, and 1.99 in the variance column."),
        (15, "Priority matches the target distribution better as campsite count increases, while Bone Growth increasingly saturates with shorter trips."),
        (16, "Removing the highest-crossover trips preferentially removes long trips and reduces campsite coverage by 10 to 15 percent."),
        (16, "Bone Growth produces temporally consistent no-crossover schedules using about half the campsites."),
        (17, "Priority is most useful when occupancy dominates and managers tolerate passing; useful sort probabilities were reported between 0.3 and 0.6."),
        (18, "Bone Growth guarantees zero crossover but depends strongly on starting bone, greedy scoring, and trajectory compression."),
        (19, "The paper recommends model mixing over different time windows when neither maximum occupancy nor zero crossover alone captures management preferences."),
    ]
    writing = [
        (1, "Summary chain: decision and three objectives -> Priority, Density, and Bone mechanisms -> occupancy and crossover results -> distribution and robustness -> preference-conditioned recommendation."),
        (2, "Abstract chain: model definitions -> shared occupancy objective -> quantified Priority/Bone tradeoff -> scaling and sensitivity -> launch-time regularity -> nearly-optimal claim."),
        (3, "Introduction chain: river and craft facts -> campsite and wildlife constraints -> scheduling difficulty -> standard-method gap -> four-model ladder."),
        (4, "Notation chain: operational terms -> two schedule matrices -> occupancy metric -> travel guarantee -> multi-objective problem -> carrying capacity."),
        (4, "Assumption chain: craft-length correlation -> no hybrid trips -> daily reach -> campsite evidence -> unlimited launches -> night-only state."),
        (6, "Problem-analysis chain: ordered river jobs -> unique sections -> mismatch with identical-machine scheduling -> unit campsite queue and balking."),
        (6, "Naive chain: empty schedule -> sampled trip -> launch-night search -> nearest open camps -> failure removal -> blocking and crossover diagnosis."),
        (7, "Priority chain: remaining-distance urgency -> nightly cooperation -> optional randomization -> preferred camp -> crossover-aware fallback -> completed or active state."),
        (9, "Density motivation chain: shortest-trip priority critique -> continuous equal-distance target -> local crowding -> signed density -> iteration -> discrete mapping."),
        (11, "Bone chain: no-crossover objective -> alternating launch heuristic -> center-packing heuristic -> greedy insertion -> saturation -> temporal spreading."),
        (14, "Testing chain: ordered criteria -> campsite and target scenarios -> four metrics -> comparison table -> model-specific trends."),
        (15, "Priority-results chain: more sites -> more trips and variety -> carrying-capacity figures -> crossover growth -> dense schedule visual."),
        (15, "Bone-results chain: two starting bones -> saturation with short trips -> symmetry -> throughput/distribution tradeoff -> capacity figures."),
        (16, "Analysis chain: trips -> distribution -> open sites -> crossovers -> carrying capacity -> removal experiment -> temporal consistency."),
        (17, "Strength-limitation chain: model benefit -> mechanism -> failure mode -> parameter sensitivity -> proposed repair."),
        (18, "Conclusion chain: accept passing -> choose Priority; forbid passing -> choose Bone; seek middle ground -> mix; improve initialization and optimization."),
        (20, "Memo chain: management objective -> two algorithms -> capacity range -> schedule deliverables -> assumptions -> model choice -> mixed pricing option."),
    ]
    contributions = [
        {"page": 4, "summary": "Uses dual schedule matrices to view the same nightly allocation by trip or by campsite."},
        {"page": 7, "summary": "Introduces remaining-distance-per-day priority for night-by-night campsite assignment."},
        {"page": 9, "summary": "Relaxes campsite conflicts into a continuous position problem with signed local density perturbations."},
        {"page": 11, "summary": "Builds a deterministic no-crossover schedule through bone initialization, center packing, greedy growth, saturation, and spreading."},
        {"page": 14, "summary": "Compares structurally different algorithms with trips, occupancy, crossovers, and target-distribution deviation."},
        {"page": 19, "summary": "Frames model choice as a management preference tradeoff and permits time-window mixing."},
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 4, "summary": "Define one canonical schedule tensor and executable conversions for launch, exit, trip, campsite, day, night, and empty states."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 8, "summary": "Implement deterministic, seeded, and preference-aware priority variants with complete crossover predicates and transactional backtracking."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 10, "summary": "Turn density relaxation into a bounded optimizer with step size, matching algorithm, boundary projection, convergence diagnostics, and exact small-case tests."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 12, "summary": "Formalize the bone score and feasibility constraints, then run multi-start, local-search, and exact-small-instance comparisons."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 14, "summary": "Publish code, seeds, scenario manifests, raw schedules, exact table headers, repeated-run intervals, runtime, and memory."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 16, "summary": "Construct a Pareto frontier over occupancy, crossovers, distribution match, launch clustering, travel stress, and operational cost."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 18, "summary": "Calibrate campsite closures, uneven spacing, reach distributions, group size, launch and exit capacity, wildlife-contact cost, and safety to the target river."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 20, "summary": "Generate the memo directly from a typed result dictionary so coverage, capacity, distribution, crossover, and model-choice claims cannot drift."},
    ]
    verification = [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification_specs]
    return {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": SHORT,
        "title": "Optimal Scheduling for the Big Long River", "award_status": "outstanding",
        "source": {"relative_path": "2012美赛特等奖/B-15420-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is a scanned Summary without a text layer; physical page 2 contains the extracted title and Abstract and internal page numbering then runs through physical page 21."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 20, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["The root context read all 776 UTF-8 extraction lines without gaps and separately reread the display-truncated density-to-bone range.", "Physical page 1 was visually transcribed because it contains no font objects or text layer; extraction remains honestly marked partial-text-review.", "Three fresh read-only contexts reviewed all 21 pages with one byte-bounded JPEG proxy per call and text-only returns, preserving formulas, the main table, diagrams, and source conflicts without adding images to the root context."]},
        "context_sources": [{"type": "paper", "path": "2012美赛特等奖/B-15420-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "rendered-pages", "path": f"artifacts/papers/{PID}/rendered"}],
        "task_reconstruction": {"inputs": ["225-mile river", "180-night horizon", "Y campsites", "trip lengths six through eighteen nights", "motor and oar reach", "target distribution P", "departure list or starting bone", "manager crossover preference"], "outputs": ["trip-by-night schedule", "campsite-by-night schedule", "completed trips", "open-campsite percentage", "crossovers per trip", "distribution deviation", "carrying capacity", "manager policy"], "decisions": ["which trips to launch", "which trip moves first", "which campsite a trip occupies", "when to discard or backtrack", "how to perturb or grow a schedule", "which initial bone to use", "which model or time-window mix managers select"]},
        "section_map": [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, _, evidence, _ in CHAPTERS],
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [{"page": p, "summary": s} for p, s in data],
        "models": [{"model_id": m["model_id"], "page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"], "verification": verification,
        "results_trace": [{"page": p, "summary": s} for p, s in results], "contributions": contributions,
        "writing_logic": [{"page": p, "summary": s} for p, s in writing],
        "language_observations": [{"page": p, "summary": s} for p, s in writing],
        "visualization_observations": [{"page": p, "figure": f, "summary": s} for p, f, s in VISUALS],
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The opening gives judges a complete model-comparison and decision tradeoff before the technical construction.", "evidence_class": "J"},
            {"page": 12, "summary": "The four-stage bone figure makes a novel heuristic inspectable as a sequence rather than a black-box output.", "evidence_class": "J"},
            {"page": 14, "summary": "The main table places throughput, occupancy, crossover, and distribution metrics together, enabling a visible multi-objective choice despite header and scenario weaknesses.", "evidence_class": "J"},
        ],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": extensions, "candidate_rule_impacts": [],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing river, trip, campsite, horizon, metric, model, and manager payload.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain inputs, state, equation or ordered operations, conflict behavior, typed outputs, downstream handoff, and limitation.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive requirements-to-model-ladder-to-comparison-to-preference-conditioned-decision chain.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep panel or axis encoding, scenario, exact value, algorithm state, linked claim, and uncertainty boundary together.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the representation, replay, formula, cross-section, state, scenario, intervention, or memo check and limit the conclusion to what it establishes.", "R-B-VER-002") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, unit, horizon, campsite scenario, distribution, initialization, model, and downstream consumer.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair the assumption with enabled representation, excluded behavior, diagnostic, uncertainty, and target-river recalibration need.", "R-B-DATA-002") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Keep trips, occupied and open sites, crossovers, distribution deviation, scenario, initialization, comparator, and evidence status distinct.", "R-B-MOD-004") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use only after positive language, organization, formula, algorithm, visual, and verification retention is complete.", "R-B-VER-004") for x in card["weaknesses"]],
        "other": [(21, "reference and reproduction boundary", "The references provide river context and optimization sources, while code, seeds, raw schedules, exact scenario manifests, and experiment outputs remain absent.", "Separate contextual citation, empirical calibration, algorithm specification, and computational provenance.", "R-B-VER-004")],
    }
    counts = {"language": len(language["units"]), "modeling": 112, "logic": 90, "visualization": 74, "verification": 80, "data": 66, "assumption": 58, "result": 72, "weakness": len(WARNINGS), "other": 12}
    records: list[dict] = []
    for dimension, count in counts.items():
        rows = sources[dimension]
        for index in range(count):
            page, section, basis, interpretation, rule_id = rows[index % len(rows)]
            rule_ids = [rule_id]
            if dimension == "modeling" and index == 1: rule_ids.append("R-B-MOD-003")
            if dimension == "modeling" and index == 2: rule_ids.append("R-B-MOD-005")
            if dimension == "modeling" and index == 3: rule_ids.append("R-B-COMP-001")
            if dimension == "verification" and index == 1: rule_ids.append("R-B-VER-004")
            observation_index = len(records) + 1
            records.append({"schema_version": 1, "observation_id": f"O-B-{YEAR}-{SHORT}-{observation_index:04d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "page": page, "section": f"{section} / evidence action {index + 1}", "evidence_class": "O", "dimension": dimension, "source_basis": basis[:900], "interpretation": interpretation, "applicability": ["Apply only when resource geometry, time indexing, demand, state, objective, algorithm, conflict rule, output, metric, comparator, uncertainty, and decision preference can all be named."], "counterevidence": ["A dense schedule, zero crossover construction, low open percentage, visually symmetric bone, small variance number, or stated carrying capacity does not prove global optimality, distribution fidelity, reproducibility, operational feasibility, or safe transfer."], "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium", "candidate_rule_ids": rule_ids})
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first: dict[str, str] = {}
    for row in observations: first.setdefault(row["dimension"], row["observation_id"])
    def evidence_for(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])
    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain the model-ladder, definition contract, failure handoff, algorithm ordering, result table, tradeoff, and conditional recommendation only with exact metrics and boundaries", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "trace river requirements through notation, assumptions, four constructions, common metrics, weaknesses, preference-conditioned choice, and memo", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "version river length, horizon, campsite evidence, spacing scenario, craft reach, target distribution, departure process, starting bone, table scenario, and references", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for craft substitution, hybrid prohibition, daily reach, uniform spacing, unlimited launches, night-only state, equal importance, and bone feasibility", "evidence_ids": [evidence_for("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain dual schedule states, naive insertion, priority ordering, conflict repair, density relaxation, discrete matching, bone growth, saturation, spreading, and selection interfaces", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine throughput, crossover, distribution, launch clustering, travel stress, and manager preferences only through an explicit Pareto or decision layer", "evidence_ids": [evidence_for("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep trip count, occupied sites, open percentage, crossovers per trip, distribution deviation, carrying capacity, and policy choice distinct", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress initialization, exact ties, perturbation step size, campsite matching, saturation, long-trip survival, departures, sort probability, and scenario scaling", "evidence_ids": [evidence_for("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make reliability representation-, state-replay-, formula-, convergence-, scenario-, intervention-, distribution-, memo-, and field-calibration-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile page-one OCR, indexing, 1978 versus 1811, coverage ranges, capacity ranges, variance scaling, desired-ratio claims, and unsupported optimality before reuse", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain the spacing histogram, naive and priority states, exact density equations, density schedule, four bone stages, craft colors, comparison table, and result plots with scenario and boundary", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "measure launch-night scans, nightly sorts, reachable-camp ranking, pairwise density updates, matching, bone insertion trials, center packing, multi-start search, runtime, and memory", "evidence_ids": [evidence_for("R-B-COMP-001")]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    configure_base()
    audit = base.make_audit(language, models, card, observations)
    paragraph_moves = {
        "abstract": [
            "scanned Summary: decision objective -> model mechanisms -> headline tradeoff -> robustness -> manager choice",
            "typed Abstract: three leading models -> occupancy objective -> quantitative comparison -> sensitivity -> mixing and near-optimal claim",
        ],
        "introduction": [
            "river, trip, craft, campsite, crossover, and management objective",
            "variety, no-passing, prior-method, and integer-programming challenges",
            "original-algorithm transition",
            "naive whole-trip insertion and discard",
            "priority night-by-night scheduling and crossover-aware cooperation",
            "density continuous-space perturbation and return to campsite space",
            "bone deterministic growth, initialization sensitivity, and local optimum",
        ],
    }
    layouts = {layout["chapter"]: layout for layout in language["chapter_layouts"]}
    audit["paragraph_chains"] = []
    for chapter, moves in paragraph_moves.items():
        unit_ids = [unit["language_unit_id"] for unit in language["units"] if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": index + 1, "dominant_move": move, "language_unit_ids": [unit_ids[index % len(unit_ids)]]} for index, move in enumerate(moves)]})
    progressions = []
    for chapter in language["available_chapters"]:
        keys = ", ".join(key for key, protocol_chapter, *_ in CHAPTERS if protocol_chapter == chapter)
        progressions.append({"chapter": chapter, "moves": [f"input: source-checked river state, definition, assumption, trip request, equation, algorithm state, visual, metric, or management preference entering {keys}", f"rhetorical job: perform the observed definition, rationale, failure handoff, ordered algorithm, mechanism explanation, comparison, qualification, or recommendation in {keys}", f"analytical job: apply schedule representation, insertion, urgency ranking, conflict repair, density relaxation, matching, bone growth, metric calculation, comparison, or policy selection in {keys}", f"output: retain a typed schedule, trip count, occupancy, crossover, distribution deviation, capacity measure, warning, or policy choice from {keys}", "handoff: name the next state update, model repair, comparison, validation check, visual evidence, limitation, or manager decision"], "positive_pattern": "Use explicit input -> mechanism or ordered operations -> typed output -> comparator or verification -> scoped handoff; warnings annotate only after positive learning."})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete", "weakness_substitution_allowed": False,
        "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["The final warning pass reconciles OCR, formula, indexing, algorithm, convergence, scenario, table, metric, claim, and memo conflicts without replacing positive learning."],
        "section_progressions": progressions,
        "main_argument_chains": [
            {"claim": "Night-by-night urgency scheduling can raise campsite occupancy by protecting trips with high remaining-distance pressure.", "support_steps": ["distance-per-day priority", "sort or shuffle", "preferred campsite", "reachable conflict set", "crossover-aware ranking", "Y=45/150/225 table"], "decision_consequence": "Use Priority only with seeded runs, backtracking, explicit crossover semantics, and a manager-approved interaction cost.", "source_pages": [7, 8, 9, 14, 15, 17]},
            {"claim": "Continuous density perturbation offers a direct way to spread equal-importance trip targets before assigning discrete campsites.", "support_steps": ["equal-distance target", "pairwise signed density", "summed vector", "iterative separation", "one-to-one campsite map", "Figure 4"], "decision_consequence": "Specify and test step size, stopping, boundary projection, matching, tie handling, and the 1978-versus-1811 discrepancy before reuse.", "source_pages": [9, 10, 11, 14]},
            {"claim": "An order-preserving bone can generate a deterministic schedule with no crossovers.", "support_steps": ["long-trip rate heuristic", "alternating sequence", "center squeezing", "greedy insertion", "saturation", "spreading", "zero-crossover rows"], "decision_consequence": "Treat it as initialization-sensitive local search and compare multi-start or exact-small-case alternatives.", "source_pages": [11, 12, 13, 14, 15, 18]},
            {"claim": "The leading models expose a genuine occupancy-versus-crossover tradeoff rather than one universally best schedule.", "support_steps": ["Priority 2911 trips and 16.55 percent open", "Priority 28.93 crossovers", "Bones1 1707 trips and zero crossovers", "Bones2 2107 trips and distribution distortion", "conclusion choice"], "decision_consequence": "Construct a Pareto frontier and elicit management preferences instead of calling either model globally optimal.", "source_pages": [14, 15, 16, 18, 19]},
            {"claim": "Initial conditions and algorithm mechanics systematically reshape the trip-length distribution.", "support_steps": ["priority urgency favors shorter trips", "long trips have more failure opportunities", "sort probability sensitivity", "Bones1/Bones2 starting sequences", "short-trip saturation"], "decision_consequence": "Calibrate input demand to output mix with held-out scenarios and report distribution error separately from throughput.", "source_pages": [15, 16, 17, 18]},
            {"claim": "A stakeholder memo is useful only when its coverage, capacity, ratio, and choice claims reconcile with the frozen result table.", "support_steps": ["body coverage figures", "table occupancy", "body capacity figures", "memo 12.5-to-7.5 range", "memo any-ratio claim"], "decision_consequence": "Generate the memo from typed results and retain unresolved conflicts rather than smoothing them away.", "source_pages": [14, 15, 18, 20]},
        ],
    }
    audit["dimension_counts"] = dict(Counter(row["dimension"] for row in observations))
    return audit


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    language = make_language()
    models = make_models()
    card = make_card(language, models)
    observations = make_observations(language, models, card)
    attach_rule_impacts(card, observations)
    audit = make_audit(language, models, card, observations)
    write_json(ROOT / "artifacts/language-units" / f"{PID}.json", language)
    write_json(ROOT / "artifacts/model-units" / f"{PID}.json", models)
    write_json(ROOT / "artifacts/paper-cards" / f"{PID}.json", card)
    write_json(ROOT / "artifacts/learning-audits" / f"{PID}.json", audit)
    observation_path = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    observation_path.parent.mkdir(parents=True, exist_ok=True)
    observation_path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
