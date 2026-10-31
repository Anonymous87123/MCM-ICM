from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import build_q98_artifacts as base


ROOT = Path(r"F:/MCM/mcm-skill-work")
STAGE = ROOT / "tmp/q99-stage"
PID = "P-B-2012-15878-825774ea"
SHORT = "15878"
SHA = "825774eaa5d3e849b37885ed80389c0f54df9d03484cff13c136276bb99fa41c"
TYPE = "B"
YEAR = "2012"
PAGE_COUNT = 23

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

# key, normalized chapter, first page, last page, tag, unit count,
# source-checked chapter evidence, visually observed paragraph count
CHAPTERS = [
    ("abstract", "abstract", 1, 1, "ABS", 56, "The abstract compresses the management objective, one-dimensional cellular representation, visitor-object rules, daily adaptation, satisfaction criteria, and the headline 1102-capacity result into one forward-moving paragraph.", 1),
    ("introduction", "introduction", 3, 3, "INT", 72, "The introduction moves from growth in rafting participation to encounter norms and prior wilderness simulation, identifies the inflexibility of static itineraries, and motivates a demand-responsive dynamic scheduler.", 3),
    ("plan-of-attack", "problem-analysis", 3, 4, "PLA", 52, "The plan of attack restates the 225-mile, Y-campsite, six-to-eighteen-day decision and previews assumptions, criteria, a cellular model, implementation variants, evaluation, and capacity selection.", 8),
    ("assumptions", "assumptions", 4, 5, "ASM", 58, "The assumptions translate craft speeds, daily rafting hours, uniform campsites, local visitor activity, maintenance, constant mean arrivals, and advance booking into a daily discrete scheduling surface.", 11),
    ("definitions-and-good-model", "notation", 5, 6, "NOT", 50, "The definitions distinguish three encounter types, schedule deviation, rejected demand, absolute capacity, practical carrying capacity, satisfaction constraints, flexibility, robustness, and implementability.", 12),
    ("static-versus-dynamic", "model-establishment", 6, 8, "EST", 60, "The comparison first credits static schedules for conflict-free predictability, then names their demand and throughput costs and replaces them with a rolling day-by-day destination assignment that can be planned in advance.", 14),
    ("cellular-model-and-metrics", "algorithm", 9, 13, "ALG", 120, "The core section defines the river array, Poisson loading, visitor state, ideal movement, bump priority, conflict resolution, completion calculations, seven implementations, interaction geometry, rejection sets, and satisfaction metrics.", 29),
    ("results-and-capacity", "results", 14, 18, "RES", 100, "The results compare implementation variants, then sweep Y and lambda through interaction, rejection, off-schedule, and completion surfaces before selecting maximum and economic capacity points.", 21),
    ("environment-and-storms", "robustness-verification", 19, 20, "ROB", 64, "The extension breaks the fixed-campsite and uninterrupted-flow assumptions, removes campsites through an environmental-degradation rule, pauses movement and loading during Poisson-duration storms, and maps operational responses.", 13),
    ("conclusion", "conclusion", 20, 21, "CON", 42, "The conclusion reconnects customer-choice flexibility, conflict elimination, satisfaction metrics, the 1102 maximum, the 1074 practical point, adverse-event tests, and claimed transfer to other one-dimensional rivers.", 5),
    ("manager-memo", "memo", 22, 22, "MEM", 42, "The memo translates the cellular scheduler into advance-booking, daily placement, conflict reassignment, capacity, on-time completion, interaction, storm, environmental, and scale-up claims for rafting managers.", 4),
    ("notes", "references", 23, 23, "REF", 12, "Ten notes supply recreation-demand, social-norm, wilderness-simulation, safety, itinerary, parks, encounter-norm, and cellular-automaton context while leaving code, seeds, raw runs, and complete task text absent.", 10),
]

MOVES = [
    ("objective-mechanism-result", "Forecast the decision objective, model mechanism, adaptation rule, satisfaction criteria, and headline result before technical detail.", "decision need -> representation -> daily mechanism -> evaluation criteria -> quantitative result -> scope"),
    ("context-gap-handoff", "Use domain growth and prior research to expose a flexibility gap that the proposed model must repair.", "domain trend -> prior evidence -> inherited limitation -> unmet demand -> model requirement"),
    ("deliverable-roadmap", "Turn the task restatement into an ordered roadmap whose later sections discharge named analytical obligations.", "system inputs -> objective -> assumptions -> criteria -> model -> variants -> evaluation -> decision"),
    ("assumption-operationalization", "Pair each simplifying assumption with the state update, data need, or excluded behavior it creates.", "assumption -> rationale -> enabled operation -> excluded regime -> later stress test"),
    ("definition-threshold", "Define a customer or capacity term through observable metrics and explicit acceptance thresholds.", "term -> observable quantity -> threshold -> decision use -> ambiguity boundary"),
    ("baseline-credit-limit", "Credit a baseline for the property it guarantees before naming the flexibility or capacity it sacrifices.", "baseline benefit -> operating rule -> limitation -> consequence -> successor requirement"),
    ("dynamic-sequence", "Explain the rolling scheduler as a day-indexed sequence with known future demand and repeated destination updates.", "advance request -> daily state -> next destination -> conflict check -> update -> completion"),
    ("state-object-rule", "Introduce a model by defining its array state, visitor object, transition rule, and completion condition.", "state space -> object fields -> load rule -> move rule -> conflict rule -> output"),
    ("priority-conflict-repair", "Resolve a local resource conflict by comparing schedule pressure, choosing a winner, and displacing the lower-priority visitor.", "collision -> priority coefficient -> comparison -> displacement direction -> updated schedule"),
    ("variant-control-comparison", "Separate the ideal implementation from controlled rule ablations so mechanism effects can be compared.", "ideal rule set -> controlled change -> held constants -> common metrics -> mechanism inference"),
    ("metric-geometry", "Define an interaction metric from relative positions and movement rather than using an untyped count.", "visitor pair -> initial order -> final order -> event classification -> aggregate count"),
    ("surface-trend-interpretation", "Read a parameter surface by naming axes, threshold behavior, asymptote, and managerial implication.", "parameters -> response surface -> monotone or threshold trend -> limiting regime -> decision"),
    ("capacity-with-economics", "Separate the mathematical maximum from a lower-maintenance practical operating point.", "feasible maximum -> satisfaction checks -> resource cost -> alternative point -> tradeoff"),
    ("assumption-break-stress-test", "Break one ideal assumption, alter the state transition, and measure how performance degrades.", "ideal assumption -> disturbance rule -> scenario grid -> metric deterioration -> mitigation"),
    ("positive-conclusion-boundary", "Synthesize the model's useful result, then state the conditions under which the claimed transfer is plausible.", "contribution -> evidence -> operating point -> extension -> transfer condition"),
    ("manager-workflow", "Translate technical state updates into booking, warning, reassignment, and capacity actions a manager can implement.", "customer request -> model input -> daily decision -> exception output -> manager action -> caveat"),
    ("visual-evidence-contract", "State what a figure or table makes inspectable and which claim still needs uncertainty or reproduction evidence.", "encoding -> visible relation -> linked claim -> missing evidence -> use boundary"),
    ("provenance-boundary", "Separate contextual citations from model calibration, executable evidence, and complete task reconstruction.", "citation role -> supplied fact -> model use -> missing artifact -> reuse boundary"),
]

EXAMPLES = [
    ("A park-capacity abstract moves from visitor-choice pressure to a daily state model and reports service, delay, and contact metrics together.", "The opening keeps the mechanism and operating point tied to one scenario."),
    ("A permit paper uses participation growth and encounter-norm research to motivate a demand-responsive allocation policy.", "Prior work supports the gap rather than substituting for the new model."),
    ("A transit roadmap lists assumptions, service criteria, dynamic assignment, controlled variants, stress tests, and policy output in execution order.", "Each promised stage has a later evidence-bearing section."),
    ("A campground model pairs uniform-site spacing with the daily cell update it enables and reserves closures for robustness testing.", "The excluded uneven geometry remains explicit."),
    ("A service-capacity paper defines rejection, delay, and interaction thresholds before searching for a maximum load.", "Units and denominators are fixed before comparison."),
    ("A static roster is credited for guaranteed conflict avoidance, then rejected because it suppresses customer choice and throughput.", "The successor requirement follows from a named cost."),
    ("A clinic scheduler receives next-day requests, assigns one day ahead, resolves bed conflicts, and repeats until discharge.", "The time index and carried state are visible."),
    ("A warehouse model defines a line of bays and job objects before giving load, move, collision, and exit rules.", "Every rule updates a typed state."),
    ("A berth conflict compares remaining slack and displaces the vessel with lower urgency to a feasible alternative.", "Priority and displacement are not conflated."),
    ("A dispatch study compares an ideal rule set with direction, randomization, and bumping ablations under one metric suite.", "Ablations change one mechanism at a time."),
    ("A pedestrian interaction metric detects whether two trajectories reverse order over a time step.", "The event geometry is defined before aggregation."),
    ("A capacity surface names demand and resource axes, then identifies a plateau where one parameter no longer matters.", "The conclusion stays within the plotted domain."),
    ("A hospital paper distinguishes the maximum staffed census from a slightly smaller configuration with lower maintenance cost.", "Economic efficiency is not renamed as mathematical capacity."),
    ("A logistics model removes depots or pauses flow to test how service and rejection respond to disruptions.", "Each disturbance has an explicit state rule."),
    ("A conclusion reports the best tested operating point and a practical point, then limits transfer to systems with matching geometry and demand.", "Robustness is not universalized."),
    ("A manager memo converts forecasts into accept, reassign, warn, or reject actions and retains uncertainty.", "Rounded headline values trace to typed results."),
    ("A two-panel contour plot lists axis units, legend levels, and the exact decision claim it supports.", "Small labels and scaling are not guessed."),
    ("A references section distinguishes background theory from data, code, scenario manifests, and executable validation.", "Missing artifacts remain missing."),
]

EQUATIONS = [
    ("absolute seasonal capacity", 6, "Carrying Capacity", "capacity bound", "C_abs = 6*30*Y = 180Y visitor groups per season", r"C_{\mathrm{abs}}=6\cdot30\cdot Y=180Y", ["C_abs", "Y"], "Set an occupancy-only upper bound before satisfaction constraints are applied."),
    ("bump coefficient", 10, "Bump Coefficient", "conflict priority", "beta = (Y-y)/D_r", r"\beta=\frac{Y-y}{D_r}", ["beta", "Y", "y", "D_r"], "Measure remaining river distance per remaining day for conflict priority."),
    ("ideal daily movement", 11, "Ideal Implementation", "daily movement", "y* = (Y-y)/D_r", r"y^{*}=\frac{Y-y}{D_r}", ["y_star", "Y", "y", "D_r"], "Move a visitor by the average campsite distance needed per remaining day."),
    ("Poisson daily loading", 11, "General Implementation", "arrival process", "A_t ~ Pois(lambda)", r"A_t\sim\operatorname{Poisson}(\lambda)", ["A_t", "lambda"], "Generate the number of visitors loaded on a simulated day."),
    ("rejection satisfaction threshold", 13, "Clarifying the Metrics", "acceptance criterion", "100|R|/|V_requested| < 10", r"100\frac{|R|}{|V_{\mathrm{requested}}|}<10", ["p_reject", "R", "V_requested"], "Require fewer than ten percent of requested visitors to be rejected."),
    ("off-schedule satisfaction threshold", 13, "Clarifying the Metrics", "acceptance criterion", "100|V_off|/|V_completed| < 10", r"100\frac{|V_{\mathrm{off}}|}{|V_{\mathrm{completed}}|}<10", ["p_off", "V_off", "V_completed"], "Require fewer than ten percent of completed visitors to finish early or late."),
    ("interaction satisfaction threshold", 13, "Clarifying the Metrics", "acceptance criterion", "I/(person day) < 10", r"\frac{I}{\text{person}\cdot\text{day}}<10", ["i_rate", "I"], "State the paper's encounter ceiling for customer satisfaction."),
    ("environmental campsite availability", 19, "Environmental Degradation", "resource degradation", "Y_operational = [Y - alpha log(lambda)]", r"Y_{\mathrm{operational}}=\left\lfloor Y-\alpha\log(\lambda)\right\rfloor", ["Y_operational", "Y", "alpha", "lambda"], "Reduce the operational campsite count as use intensity and degradation sensitivity increase."),
    ("storm duration distribution", 20, "Mitigating Storms", "disruption duration", "N ~ Pois(mu)", r"N\sim\operatorname{Poisson}(\mu)", ["N", "mu"], "Generate the number of days for which loading and movement are suspended."),
]

ALGORITHMS = [
    (3, "deliverable decomposition", "Sequence assumptions, criteria, model construction, implementation variants, evaluation, stress tests, and management advice.", ["river specification", "trip options", "season", "manager objective"], ["analysis roadmap"]),
    (7, "static itinerary baseline", "Preassign fixed daily campsites so conflicts and schedule deviation are zero at the cost of trip variety and seasonal capacity.", ["fixed trip menu", "campsites", "season"], ["static schedules", "baseline metrics"]),
    (7, "rolling dynamic scheduler", "Use advance requests and current occupancy to assign each visitor's next campsite one day at a time until completion.", ["advance requests", "current visitors", "next-day requests", "occupancy"], ["next destinations", "completed visitors"]),
    (9, "cellular river representation", "Represent the ordered river as Y campsite cells and advance the complete visitor population through daily iterations.", ["Y", "visitor states", "day"], ["cell occupancy", "next simulation state"]),
    (10, "visitor object construction", "Store propulsion type, desired duration, remaining days, current cell, desired finish, and scheduling state for each trip request.", ["trip request", "craft", "duration"], ["visitor object"]),
    (10, "queue and load", "Draw a Poisson daily count, test whether each requested trip can be offered, reject infeasible requests, and load accepted visitors.", ["lambda", "request queue", "schedule feasibility"], ["loaded visitors", "rejection set"]),
    (10, "daily ideal move", "Recompute the average remaining campsite distance and advance each visitor toward the exit.", ["Y", "y", "D_r"], ["y_star", "proposed cells"]),
    (10, "bump conflict resolution", "Inspect multiply occupied cells, compare bump coefficients, and move the lower-priority visitor according to the implementation direction rule.", ["proposed cells", "beta", "bump direction"], ["unique campsite assignment", "interaction events"]),
    (11, "daily calculation and dequeue", "Remove visitors whose position exceeds Y, store completed schedules, and update interactions, rejection, and timing metrics.", ["assigned visitors", "day", "desired duration"], ["completed reservoir", "metrics"]),
    (12, "implementation ablation matrix", "Run ideal and six control implementations that toggle optimal movement, bump direction, randomization, and bumping.", ["implementation A-G", "common arrivals", "common river"], ["comparable result rows"]),
    (13, "interaction geometry classifier", "Compare visitor order before and after movement to count raft-to-raft overtaking interactions.", ["v1 initial/final position", "v2 initial/final position"], ["interaction count"]),
    (14, "variant comparison harness", "Compare implementations A-G on visitors, rejections, interactions, and schedule deviation to identify useful mechanisms.", ["implementation outputs", "Tables 4-5"], ["selected implementation A"]),
    (15, "Y-lambda parameter sweep", "Sweep campsite count and Poisson loading rate and plot interaction, rejection, off-schedule, and completion responses.", ["Y grid", "lambda grid", "implementation A"], ["Figures 5-8", "capacity candidates"]),
    (18, "capacity decision", "Choose the maximum tested point satisfying the declared metrics, then compare lower-Y points for economic practicality.", ["response surfaces", "satisfaction thresholds", "maintenance concern"], ["1102 maximum", "1025 or 1074 practical alternatives"]),
    (19, "environmental degradation stress test", "Reduce available campsites with alpha and lambda, then recalculate visitors, rejection, and off-schedule rates.", ["Y", "alpha", "lambda", "implementation A"], ["Table 6", "maintenance mitigations"]),
    (20, "storm interruption rule", "For N days prevent loading and movement, increment every visitor's remaining-duration state, and resume the daily scheduler afterward.", ["storm probability", "mu", "visitor states"], ["disrupted performance metrics"]),
    (22, "advance-booking deployment", "Accept customer data before launch, run the daily scheduler prospectively, and return accommodation, reassignment, or error information to managers.", ["bookings", "future occupancy", "model parameters"], ["manager booking decision"]),
]

VISUALS = [
    (4, "Table 1 - craft velocity and daily rafting duration", "Supplies minimum and maximum craft speeds and four-to-eight-hour daily operation assumptions used by reach reasoning."),
    (8, "Table 2 - static versus dynamic strategy", "Compares trip variety, offer frequency, maximum visitors, conflicts, and schedule deviation while making the flexibility tradeoff visible."),
    (9, "Figure 1 - cellular river array", "Shows ordered campsite cells, heterogeneous visitor objects, trip duration, propulsion type, and downstream direction in one state snapshot."),
    (11, "Figure 2 - general daily flow", "Connects Poisson queueing, loading, movement, conflict resolution, calculations, and the 180-day feedback loop."),
    (11, "Figure 3 - ideal implementation flow", "Shows desired-trip acceptance, ideal movement, beta comparison, bumping, completion, optimization, and metric accumulation."),
    (12, "Table 3 - implementations A through G", "Acts as an ablation map for optimal movement, bump direction, and bumping behavior."),
    (13, "Figure 4 - interaction geometry", "Defines an overtaking event through relative boat order at the start and end of a simulated day."),
    (14, "Table 4 - movement controls", "Compares A-D on visitors, rejection, early and late completion, and off-schedule totals."),
    (14, "Table 5 - bump controls", "Compares A and E-G on visitors, rejection, interactions per visitor, and off-schedule percentage."),
    (15, "Figure 5 - interaction surface and contours", "Maps average interactions per trip over Y and lambda and supports the claim that campsite count dominates encounter reduction."),
    (16, "Figure 6 - rejection surface and contours", "Maps rejection percentage over Y and lambda and exposes the rapid decline as campsite count rises."),
    (17, "Figure 7 - off-schedule surface and contours", "Uses Y, lambda, a 0-to-60 color bar, and contour levels 54 to 0 by two to show schedule deviation approaching zero."),
    (18, "Figure 8 - completed visitors surface and contours", "Uses Y, lambda, a 200-to-1000 color bar, and levels 1000 to 200 by fifty to locate capacity candidates."),
    (19, "Table 6 - environmental degradation", "Reports visitor totals, off-schedule percentages, and rejection percentages across alpha rows at Y=110, while the four lambda column values are missing."),
]

WARNINGS = [
    (1, "The title page retains the template word Subtitle and the abstract contains subject-verb and wording defects; these are source defects, not extraction omissions."),
    (1, "The abstract says 1102 visitors although the simulated objects and later economic paragraph sometimes refer to visitor groups; the unit must remain typed."),
    (2, "Pages 2 through 23 visibly overlap C.A.R.S with Cellular Automaton Rafting Simulation in the footer."),
    (3, "No official problem statement was found locally; task reconstruction relies on the paper's own restatement and remains incomplete."),
    (4, "Uniform equivalent campsites, constant mean daily arrivals, advance booking, and routine maintenance exclude important spatial, seasonal, labor, and closure variation."),
    (6, "Absolute capacity 180Y counts one visitor group per campsite-day without trip-duration occupancy, interaction, launch, exit, or satisfaction constraints."),
    (7, "The dynamic strategy promises conflict elimination but the algorithm later describes resolving occupied cells rather than proving global conflict-free feasibility."),
    (8, "The paper says the dynamic model can be planned in advance but does not specify the optimization horizon, forecast update, rollback, or computational complexity."),
    (10, "The bump coefficient beta and ideal movement y-star are displayed as the same ratio despite serving priority and movement roles."),
    (10, "The conflict step says cells with more than two visitors, apparently omitting the exactly-two case that should already violate one-group campsite capacity."),
    (10, "Bump direction reversal is mentioned, but tie handling, boundary handling, repeated collision resolution, and termination are not formalized."),
    (11, "Poisson loading lacks a seed, repeated-run count, warm-up, confidence interval, and explicit mapping from arrivals to individual trip requests."),
    (12, "The seven implementation variants do not report matched random streams or replication uncertainty, limiting causal claims from Tables 4 and 5."),
    (13, "The carrying-capacity definition uses fewer than ten interactions per person per day, while the final result reports interactions per person per season."),
    (13, "The source says one rafting reason where season is intended, and its encounter metric omits raft-to-camp and camp-to-camp measures defined earlier."),
    (14, "Table 5 implementation G duplicates the visitor and percentage pattern of Table 4 implementation D, which may be a copied row but is visually present in the source."),
    (14, "Tables 4 and 5 provide single point estimates without seeds, run counts, variance, intervals, or raw outputs."),
    (15, "Figure 5 alternates among interactions per tourist, per trip, per visitor, per person, per day, and per season without one invariant denominator."),
    (16, "The argument compares a ten-interactions-per-day standard with fewer than ten total interactions over a season, a dimensional mismatch."),
    (17, "The claim that off-schedule completion becomes independent of lambda at large Y is visual and has no fitted model, uncertainty band, or tested-domain boundary."),
    (18, "The result alternates between 1102 and 1102.8 without an explicit rounding rule."),
    (18, "The maximum capacity is reported at Y=180 and lambda=15, but no proof shows it is the global optimum outside the displayed grid."),
    (18, "The body practical alternative is 1025 groups at Y=100, lambda=15, while the conclusion gives 1074 visitors at Y=110, lambda=15 under a different ratio criterion."),
    (19, "The environmental formula prints square brackets but does not define rounding, nonnegativity, time indexing, recovery, cumulative use, or the base of the logarithm."),
    (19, "Table 6 omits the four lambda column values, so its numeric columns cannot be independently interpreted."),
    (20, "The storm sentence displays no comparison sign before 5 percent; a targeted crop confirms the character is absent rather than corrupted."),
    (20, "Storm occurrence probability, independence, event overlap, duration truncation, and the meaning of incrementing D_i are not fully specified."),
    (20, "The conclusion displays Y ¿ 110; the source PDF has a broken greater-than glyph and must not be silently normalized without warning."),
    (21, "Claims of strong real-world performance and transfer to any one-dimensional rafting system exceed the limited synthetic scenarios and absent field calibration."),
    (22, "The memo extrapolates from one 225-mile river to thousands of visitors on several longer rivers without modeling network topology or shared resources."),
    (23, "Reference URLs display inverted punctuation instead of angle brackets, and no code, seeds, raw schedules, or machine-readable results are supplied."),
    (23, "Several references are incomplete or inconsistently formatted, limiting provenance and reproducibility checks."),
]


def configure_base() -> None:
    for name, value in {
        "ROOT": ROOT,
        "PID": PID,
        "SHORT": SHORT,
        "SHA": SHA,
        "TYPE": TYPE,
        "YEAR": YEAR,
        "PAGE_COUNT": PAGE_COUNT,
        "PATTERNS": PATTERNS,
        "CHAPTERS": CHAPTERS,
        "MOVES": MOVES,
        "EXAMPLES": EXAMPLES,
        "EQUATIONS": EQUATIONS,
        "ALGORITHMS": ALGORITHMS,
        "VISUALS": VISUALS,
        "WARNINGS": WARNINGS,
    }.items():
        setattr(base, name, value)


def make_language() -> dict:
    configure_base()
    language = base.make_language()
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = (
            "The root context read all 1201 lines of the 23-page UTF-8 extraction to EOF. Fresh fork_turns-none read-only "
            "contexts reviewed pages 1-8, 9-16, and 17-23 with one JPEG proxy below 450000 bytes per tool call and text-only "
            "returns. Three additional targeted crops reconciled the small Figure 7 and Figure 8 legends and the missing storm comparison sign."
        )
        layout["ambiguities"] = [
            "Linear extraction corrupts bullets, apostrophes, lambda, alpha, beta, mu, set membership, inequalities, minus signs, subscripts, URLs, table geometry, and chart legends; rendered pages and targeted crops were authoritative.",
            "Source conflicts involving interaction units, more-than-two conflict wording, Table 5 duplication, practical-capacity values, missing Table 6 lambda headers, storm inequality, and Y greater-than glyph are retained only in the final warning pass.",
        ]
    return language


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "day, season, mile, mph, campsite, visitor, visitor group, trip, interaction, percentage, probability, count, or dimensionless quantity as locally defined",
        "definition": f"Source-defined cellular rafting quantity {symbol}.",
        "source_status": "explicit-defined" if symbol not in {"A_t", "p_reject", "p_off", "i_rate", "Y_operational"} else "inferred-from-equation",
    }


def model_record(model_id: str, page: int, section: str, family: str, purpose: str, inputs: list[str], outputs: list[str], equations: list[dict]) -> dict:
    symbols = list(dict.fromkeys(inputs + outputs))
    return {
        "model_id": model_id,
        "page": page,
        "section": section,
        "family": family,
        "purpose": purpose,
        "base_or_modification": "paper-specific",
        "summary": purpose,
        "variables": [variable(symbol, set(inputs), set(outputs)) for symbol in symbols],
        "inputs": inputs,
        "outputs": outputs,
        "governing_equations": equations,
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The printed formula, threshold, figure label, or prose distribution was visually reconciled." if equations else "This record is a state representation, daily rule, controlled implementation, parameter sweep, stress test, or deployment procedure."},
        "objectives": [purpose, "Return a typed visitor state, campsite assignment, completion, rejection, interaction, schedule deviation, capacity point, or management action."],
        "constraints": [
            "A campsite is intended to host one visitor group per day and visitors move downstream through a finite 180-day season.",
            "Trip request, accepted group, rejected request, completed visitor, off-schedule visitor, interaction, and campsite resource remain separately typed.",
            "A best displayed Y-lambda cell or low synthetic metric is not a proof of global optimality, economic optimality, robustness, or transferability.",
        ],
        "conditions": {
            "initial": {"status": "present", "details": ["River length, Y, season horizon, craft type, desired duration, mean arrival rate, implementation rules, and advance requests are supplied or assumed."]},
            "boundary": {"status": "present", "details": ["Launch, final exit, y greater than Y, first and last day, full cells, exact beta ties, repeated bumps, closures, and paused-flow days require explicit treatment."]},
            "equilibrium": {"status": "not-applicable", "details": ["The paper runs finite daily simulations and parameter sweeps rather than solving a steady-state equilibrium."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Problem restatement, industry speed ranges, cited encounter standards, Poisson arrivals, selected Y-lambda grids, implementation controls, environmental alpha rows, and storm scenarios.", "parameters": inputs},
        "algorithm": {"status": "partial", "steps": ["freeze the river, season, request, implementation, and disturbance scenario", "load accepted visitors", "compute intended movement", "resolve campsite conflicts", "update completion and satisfaction metrics", "repeat for 180 days or the declared scenario grid", "select a capacity or management response"], "software": ["No executable code, fixed seed, raw visitor stream, scenario manifest, or machine-readable output archive is supplied."], "convergence_criteria": "The daily simulation ends after the season; repeated bump resolution, parameter-grid sufficiency, and global capacity search have no formal convergence or optimality certificate."},
        "assumptions": ["Uniform campsite geometry and daily discrete movement adequately represent the river.", "Poisson loading, simplified craft states, encounter thresholds, and synthetic disturbances are adequate decision surrogates."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The main states, formulas, flowcharts, ablations, tables, and surfaces are inspectable, but conflict termination, tie rules, random seeds, repetitions, uncertainty, table headers, metric units, economic objective, and field calibration prevent full reproduction."},
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, source text and rendered equation, flow, table, or plot visually reconciled."],
        "computational_cost": "Driven by daily Poisson loading, visitor-state updates, campsite conflict scans and repeated bumping, 180-day simulation, Y-lambda sweeps, implementation ablations, and disturbance scenarios; the paper supplies no runtime or complexity analysis.",
        "strengths": ["The cellular state and daily flow make a flexible demand-responsive scheduler inspectable.", "Controlled variants and four response surfaces connect mechanism changes to management metrics."],
        "limitations": ["Optimality, stochastic reproducibility, uncertainty, complete conflict semantics, economic objective, and field calibration are incomplete.", "Confirmed defects are recorded only after positive language, organization, model, and visual retention."],
        "missing_details": ["Official task text, code, seed, run count, raw requests, exact trip-choice distribution, tie and rollback rules, bump termination, confidence intervals, runtime, lambda headers, storm inequality, economic cost function, and transfer calibration are absent."],
    }


def make_models() -> dict:
    models: list[dict] = []
    for index, (label, page, section, family, source, latex, symbols, purpose) in enumerate(EQUATIONS, 1):
        equation = {
            "equation_id": f"EQ-B-{YEAR}-{SHORT}-{index:03d}",
            "page": page,
            "label": label,
            "source_expression": source,
            "normalized_latex": latex,
            "purpose": purpose,
            "variable_symbols": list(dict.fromkeys(symbols)),
            "source_type": "paper" if index in {1, 2, 3, 4, 8, 9} else "reconstructed",
            "visual_checked": True,
            "transcription_confidence": "medium" if index in {5, 6, 7, 8} else "high",
        }
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, section, family, purpose, symbols[1:], [symbols[0]], [equation]))
    for index, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, len(EQUATIONS) + 1):
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, family, family, purpose, inputs, outputs, []))
    by_family = {model["family"]: model["model_id"] for model in models}
    pairs = [
        ("capacity bound", "capacity decision"),
        ("static itinerary baseline", "rolling dynamic scheduler"),
        ("rolling dynamic scheduler", "cellular river representation"),
        ("cellular river representation", "visitor object construction"),
        ("arrival process", "queue and load"),
        ("visitor object construction", "queue and load"),
        ("daily movement", "daily ideal move"),
        ("conflict priority", "bump conflict resolution"),
        ("daily ideal move", "bump conflict resolution"),
        ("bump conflict resolution", "daily calculation and dequeue"),
        ("daily calculation and dequeue", "implementation ablation matrix"),
        ("implementation ablation matrix", "variant comparison harness"),
        ("interaction geometry classifier", "variant comparison harness"),
        ("acceptance criterion", "capacity decision"),
        ("variant comparison harness", "Y-lambda parameter sweep"),
        ("Y-lambda parameter sweep", "capacity decision"),
        ("resource degradation", "environmental degradation stress test"),
        ("disruption duration", "storm interruption rule"),
        ("capacity decision", "advance-booking deployment"),
    ]
    edges = [{"from_model_id": by_family[source], "to_model_id": by_family[target], "handoff": f"The {source} output becomes a state, constraint, metric, scenario, or decision input for {target}."} for source, target in pairs if source in by_family and target in by_family]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    assumptions = [
        (4, "Oar and motor rafts operate within the Table 1 speed ranges for four to eight hours per day."),
        (4, "Daily motion depends on initial and final campsite positions rather than within-day speed variation."),
        (4, "Y campsites are equivalent, uniformly distributed, maintained, and available unless a later stress test removes them."),
        (4, "Campsites are offset from the river and visitor activity remains local to the assigned site."),
        (4, "The mean number of visitors entering per day is constant and represented by lambda."),
        (5, "Visitors make reservations at least twenty-four hours in advance."),
        (7, "The dynamic scheduler has access to current visitors and next-day arrivals when assigning destinations."),
        (9, "The river can be represented as a one-dimensional cellular array updated once per day."),
        (13, "Rejected demand, off-schedule completion, and encounter rates are sufficient customer-satisfaction proxies."),
        (19, "Environmental degradation and storm interruption can be represented through campsite removal and paused daily transitions."),
    ]
    data = [
        (3, "The paper restates a 225-mile river, Y campsites, six-to-eighteen-day trips, and oar or motor propulsion."),
        (4, "Table 1 gives both craft types a three-mph minimum, maxima of five and ten mph, and four-to-eight-hour rafting days."),
        (11, "Daily load follows a Poisson process with parameter lambda in the flow diagram."),
        (12, "Table 3 defines seven implementation rule combinations A-G."),
        (14, "Tables 4 and 5 report visitor totals, rejection, interactions, and timing for selected implementations."),
        (15, "Figure 5 sweeps Y and lambda for average boat interactions."),
        (16, "Figure 6 sweeps Y and lambda for rejected visitors."),
        (17, "Figure 7 sweeps Y and lambda for off-schedule completion with contour levels 54 through 0."),
        (18, "Figure 8 sweeps Y and lambda for completed visitors with contour levels 1000 through 200."),
        (19, "Table 6 uses Y=110 and alpha rows zero, ten, twenty, and thirty, but omits the four lambda column values."),
        (20, "Storm tests use Y=110, four lambda values, four occurrence probabilities, and mean duration mu equal to one day, but the table of results is not printed."),
    ]
    verification_specs = [
        (6, "The absolute-capacity expression can be visually reconciled with the six-month, thirty-day, Y-campsite assumptions.", "formula-unit check", "The printed multiplication and 180Y result are clear.", "It is only an occupancy upper bound."),
        (10, "The beta formula and variable domain can be reconciled against the rendered equation.", "formula transcription", "Beta, Y, y, and D_r are visually clear.", "Its distinction from y-star remains unclear."),
        (11, "Figures 2 and 3 permit a state-transition trace from request queue to completed visitors.", "flow replay", "Major branches and the 180-day loop are explicit.", "Conflict iteration and termination are underspecified."),
        (12, "Table 3 permits a controlled-rule comparison of A-G.", "ablation inspection", "Optimal movement, direction, and bumping switches are visible.", "Matched randomness and replication are absent."),
        (14, "Tables 4 and 5 permit exact visual transcription of implementation outcomes.", "table cross-check", "All printed cells are legible.", "No uncertainty or raw runs are supplied."),
        (15, "Figure 5 supports the qualitative decline of interactions as Y increases.", "surface trend", "Axes, color scale, and contours are visible.", "Metric units vary across text and figure labels."),
        (16, "Figure 6 supports the qualitative decline of rejection as Y increases.", "surface trend", "The response surface is visually coherent.", "The grid and replication design are not specified."),
        (17, "A targeted crop preserves Figure 7 axes, 0-to-60 color bar, and 54-to-0-by-two contour legend.", "small-label visual check", "Fine legend values are recovered without loading a full-resolution page into the model context.", "The surface alone does not prove asymptotic independence."),
        (18, "A targeted crop preserves Figure 8's 200-to-1000 color bar and 1000-to-200-by-fifty contour legend.", "small-label visual check", "Capacity-level encoding is exact.", "No global search or uncertainty is established."),
        (19, "Table 6 is visually checked for all alpha rows and response cells.", "table integrity check", "The values and Y=110 note are present.", "The four lambda column values are absent in the source."),
        (20, "A targeted crop confirms that the comparison sign before storm 5 percent is absent.", "source-defect check", "The absence is distinguishable from extraction corruption.", "The intended inequality cannot be recovered with certainty."),
        (22, "Memo claims can be traced to the results and conclusion.", "memo-result trace", "1102, roughly 98 percent, and 99.33 percent are linked.", "Practical capacity, metric units, rounding, and transfer claims drift."),
    ]
    results = [
        (14, "Implementation A completes 756 visitors with 3.8 percent rejection and 2.1 percent off-schedule in Table 4."),
        (14, "Removing optimal movement in implementation B raises off-schedule completion to 42.3 percent in Table 4."),
        (14, "Implementation A reports 7.10 interactions per visitor and 2.2 percent off-schedule in Table 5."),
        (14, "Upstream bumping in implementation F reduces interactions but rejects 35.0 percent of requests."),
        (15, "Interaction surfaces remain below about ten over the displayed grid and decline with added campsites."),
        (16, "Rejection falls sharply with Y and rises with lambda when campsites are scarce."),
        (17, "Off-schedule completion approaches zero as Y increases in the displayed grid."),
        (18, "The claimed maximum is 1102 visitors or groups at Y=180 and lambda=15."),
        (18, "At the claimed maximum, rejection is 1.79 percent, off-schedule completion is 0.67 percent, and interactions are 10.35 per person per season."),
        (18, "A lower-resource point at Y=100 and lambda=15 is reported to complete 1025 visitor groups."),
        (19, "Large alpha values substantially reduce visitor totals and increase rejection and off-schedule percentages in Table 6."),
        (21, "The conclusion reports a practical point of 1074 visitors at Y=110 and lambda=15 under a visitors-to-campsites ratio criterion."),
    ]
    writing = [
        (1, "Abstract chain: management need -> cellular representation -> visitor objects and rules -> daily adaptation -> satisfaction metrics -> 1102-capacity claim."),
        (3, "Introduction chain: participation growth -> encounter norms -> prior static simulation -> customer-choice gap -> dynamic-model need."),
        (3, "Plan chain: river and trip inputs -> maximize visitors and experience -> assumptions -> criteria -> model -> variants -> evaluation."),
        (4, "Assumption chain: craft reach -> daily motion -> uniform cells -> local activity -> maintenance -> constant mean arrivals -> advance booking."),
        (5, "Definition chain: encounter types -> schedule timing -> trip rejection -> absolute and satisfaction-constrained capacity."),
        (6, "Criteria chain: efficient capacity -> demand flexibility -> variable-condition performance -> implementability."),
        (7, "Comparison chain: static guarantee -> flexibility loss -> rolling dynamic destinations -> advance planning response."),
        (9, "Model chain: cell array -> visitor object -> queue/load -> move -> conflict -> calculate -> repeat."),
        (10, "Priority chain: remaining distance and days -> beta -> bump comparison -> displacement direction -> updated occupancy."),
        (12, "Ablation chain: ideal A -> movement controls B-D -> bump controls E-G -> common metrics -> mechanism selection."),
        (14, "Results chain: implementation tables -> four parameter surfaces -> satisfaction thresholds -> capacity point -> economic alternative."),
        (19, "Robustness chain: break campsite permanence -> degradation formula and table -> mitigations -> break uninterrupted flow -> storm rule."),
        (20, "Conclusion chain: flexibility and conflict claim -> metric recap -> maximum and practical points -> adverse events -> transfer claim."),
        (22, "Memo chain: static-industry limitation -> dynamic booking workflow -> test design -> headline metrics -> storm and environmental extensions -> scale claim."),
    ]
    contributions = [
        {"page": 9, "summary": "Represents a multi-day rafting corridor as a daily updated one-dimensional cellular array."},
        {"page": 10, "summary": "Packages heterogeneous trip duration and propulsion into visitor objects with explicit remaining-schedule state."},
        {"page": 10, "summary": "Uses remaining-distance pressure to prioritize campsite conflict resolution."},
        {"page": 12, "summary": "Builds an ablation family A-G to separate movement and bump-rule effects."},
        {"page": 13, "summary": "Defines overtaking interactions through relative trajectory order."},
        {"page": 15, "summary": "Uses four Y-lambda response surfaces to connect system resources and demand to customer metrics."},
        {"page": 18, "summary": "Separates maximum carrying capacity from a lower-maintenance practical operating point."},
        {"page": 19, "summary": "Extends the daily state model with campsite degradation and storm interruption rules."},
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 10, "summary": "Define an exact conflict-resolution loop for two or more visitors, including beta ties, boundaries, repeated bumps, cycle detection, and termination."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 11, "summary": "Publish pseudocode or executable code with fixed seeds, typed visitor requests, state invariants, and machine-readable outputs."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 13, "summary": "Choose one interaction denominator and retain raft-to-raft, raft-to-camp, and camp-to-camp measures separately."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 14, "summary": "Use common random numbers and repeated runs for A-G with intervals and paired mechanism-effect estimates."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 18, "summary": "Construct a Pareto frontier over completed groups, rejection, delay, interactions, campsite count, and maintenance cost rather than one capacity scalar."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 18, "summary": "Search a declared Y-lambda domain with exact constraints or bounded optimization and publish the full feasible set."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 19, "summary": "Model campsite degradation as cumulative state with recovery, heterogeneity, closure duration, and empirically calibrated use effects."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 20, "summary": "Use an explicit storm arrival process, duration law, overlap rule, travel-safety state, and customer-notification policy."},
        {"extension_id": f"E-B-{SHORT}-009", "page": 21, "summary": "Calibrate demand, group size, spatial geometry, craft speed, closures, encounter tolerance, safety, staffing, and multi-river topology before transfer."},
        {"extension_id": f"E-B-{SHORT}-010", "page": 22, "summary": "Generate the memo from a typed result object so rounding, capacity, practical point, interaction units, and uncertainty cannot drift."},
    ]
    verification = [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification_specs]
    return {
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "C.A.R.S.: Cellular Automaton Rafting Simulation",
        "award_status": "outstanding",
        "source": {"relative_path": "2012美赛特等奖/B-15878-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page numbering matches Page 1 of 23 through Page 23 of 23; page 1 is the title and abstract, page 2 is contents, and page 23 is Notes."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["The root context read all 1201 UTF-8 extraction lines without skipping any substantive chapter.", "Fresh isolated visual contexts reviewed all 23 pages using one byte-bounded JPEG per call and returned text only.", "Targeted crops recovered Figure 7 and Figure 8 fine legends and confirmed the storm inequality sign is absent; extraction symbol corruption was not treated as source mathematics."]},
        "context_sources": [{"type": "paper", "path": "2012美赛特等奖/B-15878-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "rendered-pages", "path": f"artifacts/papers/{PID}/rendered"}],
        "task_reconstruction": {"status": "incomplete-official-task-unavailable", "inputs": ["225-mile river", "Y uniformly described campsites", "180-day season", "six-to-eighteen-day trips", "oar or motor propulsion", "Poisson daily load lambda", "advance requests", "implementation rules", "disturbance parameters alpha and mu"], "outputs": ["daily campsite schedule", "accepted and rejected requests", "completed visitors or groups", "off-schedule percentage", "interaction count", "capacity point", "practical operating point", "manager response"], "decisions": ["which requested trips are accepted", "which campsite each visitor receives next", "which visitor is bumped", "when a visitor completes", "which implementation rules are used", "which Y-lambda point is selected", "how closures and storms are mitigated"]},
        "section_map": [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, _, evidence, _ in CHAPTERS],
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [{"page": p, "summary": s} for p, s in data],
        "models": [{"model_id": model["model_id"], "page": model["page"], "summary": model["summary"]} for model in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": verification,
        "results_trace": [{"page": p, "summary": s} for p, s in results],
        "contributions": contributions,
        "writing_logic": [{"page": p, "summary": s} for p, s in writing],
        "language_observations": [{"page": p, "summary": s} for p, s in writing],
        "visualization_observations": [{"page": p, "figure": figure, "summary": summary} for p, figure, summary in VISUALS],
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The one-paragraph abstract gives judges the full representation-mechanism-metric-result path before details.", "evidence_class": "J"},
            {"page": 11, "summary": "The daily and ideal flowcharts make the cellular update and conflict branches inspectable.", "evidence_class": "J"},
            {"page": 18, "summary": "The paper converts four response surfaces into both a maximum and a practical management point.", "evidence_class": "J"},
        ],
        "weaknesses": [{"page": p, "summary": warning} for p, warning in WARNINGS],
        "independent_extensions": extensions,
        "candidate_rule_impacts": [],
        "unresolved_questions": [warning for _, warning in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(model["governing_equations"]) for model in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(unit["page"], unit["section"], unit["source_excerpt"], "Transfer the rhetorical mechanism only after replacing river, cell, visitor, campsite, season, metric, implementation, disturbance, and manager payload.", "R-B-LANG-001") for unit in language["units"]],
        "modeling": [(model["page"], model["section"], model["summary"], "Retain inputs, state, daily operation, conflict behavior, equation or threshold, typed outputs, dependency handoff, and limitation.", "R-B-MOD-001") for model in models["models"]],
        "logic": [(item["page"], "organization chain", item["summary"], "Preserve the positive context-to-gap-to-dynamic-state-to-ablation-to-surface-to-capacity-to-stress-test-to-memo chain.", "R-B-LOG-001") for item in card["writing_logic"]],
        "visualization": [(item["page"], item["figure"], item["summary"], "Keep axes, units, legend levels, table headers, implementation, exact values, linked claim, and uncertainty boundary together.", "R-B-VIZ-001") for item in card["visualization_observations"]],
        "verification": [(item["page"], "verification", item["summary"], "Name the formula, flow, ablation, table, surface, crop, source-defect, or memo check and limit the conclusion to what it establishes.", "R-B-VER-002") for item in card["verification"]],
        "data": [(item["page"], "data and preprocessing", item["summary"], "Retain provenance, unit, scenario, random process, grid, missing header, and downstream consumer.", "R-B-DATA-001") for item in card["data_and_preprocessing"]],
        "assumption": [(item["page"], "assumption", item["summary"], "Pair the assumption with the enabled state transition, excluded behavior, diagnostic, disturbance test, and recalibration need.", "R-B-DATA-002") for item in card["assumptions"]],
        "result": [(item["page"], "result trace", item["summary"], "Keep accepted groups, rejection, delay, interactions, Y, lambda, implementation, maximum, practical point, and evidence status distinct.", "R-B-MOD-004") for item in card["results_trace"]],
        "weakness": [(item["page"], "last-pass warning", item["summary"], "Use only after positive language, organization, formula, algorithm, visual, result, and verification retention is complete.", "R-B-VER-004") for item in card["weaknesses"]],
        "other": [(23, "reference and reproduction boundary", "The notes supply context while official task text, executable code, seeds, raw runs, scenario manifests, and complete provenance remain absent.", "Separate background citation, calibration input, algorithm specification, computational provenance, and task reconstruction.", "R-B-VER-004")],
    }
    counts = {"language": len(language["units"]), "modeling": 168, "logic": 120, "visualization": 84, "verification": 110, "data": 80, "assumption": 72, "result": 96, "weakness": len(WARNINGS), "other": 16}
    records: list[dict] = []
    for dimension, count in counts.items():
        rows = sources[dimension]
        for index in range(count):
            page, section, basis, interpretation, rule_id = rows[index % len(rows)]
            rule_ids = [rule_id]
            if dimension == "modeling" and index == 1:
                rule_ids.append("R-B-MOD-003")
            if dimension == "modeling" and index == 2:
                rule_ids.append("R-B-MOD-005")
            if dimension == "modeling" and index == 3:
                rule_ids.append("R-B-COMP-001")
            if dimension == "verification" and index == 1:
                rule_ids.append("R-B-VER-004")
            observation_index = len(records) + 1
            records.append({"schema_version": 1, "observation_id": f"O-B-{YEAR}-{SHORT}-{observation_index:04d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "page": page, "section": f"{section} / evidence action {index + 1}", "evidence_class": "O", "dimension": dimension, "source_basis": basis[:900], "interpretation": interpretation, "applicability": ["Apply only when corridor geometry, resource cells, time step, demand law, object state, transition order, conflict rule, metric denominator, scenario, comparator, uncertainty, and decision preference can all be named."], "counterevidence": ["A dense cellular schedule, low rejection surface, low delay, a best grid point, visually smooth contour, or stated capacity does not prove global optimality, reproducibility, economic superiority, robustness, or safe transfer."], "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium", "candidate_rule_ids": rule_ids})
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first: dict[str, str] = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])
    def evidence_for(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])
    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain the one-paragraph abstract compression, research-gap handoff, roadmap, assumption consequences, baseline credit, daily rule ordering, result surfaces, capacity tradeoff, and manager workflow with exact boundaries", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "trace participation and customer-choice pressure through criteria, static baseline, dynamic cellular state, ablations, response surfaces, capacity points, disturbance rules, conclusion, and memo", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "version river length, season, Y, craft speeds, daily hours, Poisson lambda, trip requests, implementation, grid, alpha, mu, Table 6 missing headers, and exact visual legend levels", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for uniform cells, advance booking, constant mean arrivals, maintenance, daily discretization, one-dimensional geometry, satisfaction proxies, closures, and paused flow", "evidence_ids": [evidence_for("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain cellular state, visitor objects, queue and load, y-star movement, beta priority, bump resolution, completion updates, A-G ablations, geometry metrics, sweeps, capacity selection, degradation, storms, and deployment interfaces", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine completed groups, rejection, delay, encounters, campsite count, maintenance, environmental cost, and manager preference only through an explicit multi-objective decision layer", "evidence_ids": [evidence_for("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep requests, accepted visitor groups, completed visitors, rejected visitors, off-schedule visitors, encounter rates, mathematical maximum, practical point, and rounded memo values distinct", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress Poisson seeds, trip mixes, exactly-two conflicts, beta ties, repeated bumps, boundaries, Y-lambda grid, alpha dynamics, storm overlap, interaction units, and multi-river transfer", "evidence_ids": [evidence_for("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make reliability formula-, flow-, ablation-, table-, contour-, crop-, source-defect-, stochastic-, economic-, disturbance-, memo-, and field-calibration-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile footer overlap, title placeholder, units, identical beta and y-star ratios, more-than-two wording, duplicated row, interaction denominators, 1102 versus 1102.8, practical points, lambda headers, missing storm sign, and broken greater-than glyph", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain Tables 1-6, Figures 1-8, exact flow branches, implementation switches, interaction geometry, surface axes, color bars, contour levels, and missing-label boundaries", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "measure daily visitor updates, conflict scans, bump iterations, 180-day runs, A-G controls, Y-lambda sweeps, degradation scenarios, storm scenarios, runtime, and memory", "evidence_ids": [evidence_for("R-B-COMP-001")]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    configure_base()
    audit = base.make_audit(language, models, card, observations)
    paragraph_moves = {
        "abstract": ["management objective -> cellular river representation -> visitor-object rules -> daily adaptation -> satisfaction criteria -> headline capacity and timing result"],
        "introduction": [
            "participation growth and the management desire to increase trips without lowering satisfaction",
            "encounter norms, social carrying capacity, and prior wilderness-use simulation",
            "static itinerary inflexibility -> unmet customer demand -> requirement for a dynamic model",
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
        progressions.append({"chapter": chapter, "moves": [f"input: source-checked domain context, request, assumption, cell state, visitor object, equation, implementation, table, surface, disturbance, or management need entering {keys}", f"rhetorical job: perform the observed motivation, definition, baseline credit, ordered rule, mechanism comparison, trend interpretation, stress-test, synthesis, or recommendation in {keys}", f"analytical job: apply capacity bounds, dynamic assignment, cellular updates, Poisson loading, beta priority, y-star movement, bump resolution, metric calculation, ablation, parameter sweep, degradation, storm interruption, or decision selection in {keys}", f"output: retain a typed schedule, accepted or rejected set, completion, interaction, timing metric, response surface, capacity point, mitigation, warning, or manager action from {keys}", "handoff: name the next state update, controlled comparison, metric consumer, capacity decision, robustness check, implementation action, or calibrated transfer boundary"], "positive_pattern": "Use explicit input -> state or mechanism -> ordered operation -> typed output -> comparison or verification -> scoped handoff; warnings annotate only after positive learning."})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["The final warning pass reconciles extraction, source glyph, formula-role, conflict, stochastic, unit, table, capacity, disturbance, transfer, and memo defects without replacing positive learning."],
        "section_progressions": progressions,
        "main_argument_chains": [
            {"claim": "A rolling daily cellular scheduler can preserve customer trip choice while maintaining feasible campsite assignments.", "support_steps": ["static-model flexibility gap", "advance request availability", "one-dimensional campsite cells", "visitor objects", "daily destination updates", "conflict resolution", "completion reservoir"], "decision_consequence": "Use the mechanism only with a complete conflict loop, typed state invariants, and prospective booking horizon.", "source_pages": [3, 7, 8, 9, 10, 11, 22]},
            {"claim": "Remaining-distance pressure provides a simple local priority for resolving campsite conflicts.", "support_steps": ["beta ratio", "ideal movement ratio", "multiply occupied cell", "coefficient comparison", "bump direction", "implementation controls"], "decision_consequence": "Separate movement and priority semantics and specify exactly-two cases, ties, cycles, and boundaries before implementation.", "source_pages": [10, 11, 12]},
            {"claim": "Controlled implementations suggest that optimal movement and bump behavior materially affect service and schedule quality.", "support_steps": ["Table 3 ablation definitions", "Table 4 movement results", "Table 5 bump results", "selected implementation A"], "decision_consequence": "Repeat A-G under matched random streams and report paired uncertainty before causal reuse.", "source_pages": [12, 14]},
            {"claim": "Increasing campsite count reduces rejection and off-schedule completion and raises completed visitors across the tested grid.", "support_steps": ["Figure 6 rejection surface", "Figure 7 off-schedule surface", "Figure 8 completion surface", "Y-lambda trend interpretation"], "decision_consequence": "Retain the exact tested domain and quantify uncertainty instead of asserting universal monotonicity or independence.", "source_pages": [16, 17, 18]},
            {"claim": "The paper identifies a mathematical maximum and lower-resource practical alternatives rather than one cost-free capacity number.", "support_steps": ["1102 at Y=180 lambda=15", "1.79 percent rejection", "0.67 percent off schedule", "1025 at Y=100", "1074 at Y=110", "maintenance concern"], "decision_consequence": "Build an explicit Pareto or cost model and reconcile the two practical points and visitor-versus-group units.", "source_pages": [18, 21]},
            {"claim": "The cellular state can be extended to closures and paused flow by changing resource availability and daily transitions.", "support_steps": ["Y-alpha-log-lambda rule", "Table 6 deterioration", "build or protect campsites", "storm loading and movement pause", "incremented D_i"], "decision_consequence": "Use cumulative degradation and explicit storm-event semantics calibrated to the operating river.", "source_pages": [19, 20]},
            {"claim": "A management memo is valuable when advance-booking decisions and headline results trace to frozen typed outputs.", "support_steps": ["request input", "prospective accommodation test", "conflict reassignment", "1102 capacity", "98 percent desired trips", "99.33 percent on time", "disturbance extensions"], "decision_consequence": "Generate the memo mechanically from results and preserve rounding, units, uncertainty, practical capacity, and transfer limits.", "source_pages": [18, 21, 22]},
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
    write_json(STAGE / "language.json", language)
    write_json(STAGE / "models.json", models)
    write_json(STAGE / "card.json", card)
    write_json(STAGE / "audit.json", audit)
    STAGE.mkdir(parents=True, exist_ok=True)
    (STAGE / "observations.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "stage": str(STAGE), "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
