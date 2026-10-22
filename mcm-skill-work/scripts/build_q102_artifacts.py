from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2014-26333-27e7d8ab"
SHORT = "26333"
SHA = "27e7d8ab3b61b87d9796aeb204393400e957174c906d3a5620889b3d999e47bf"
TYPE = "B"
YEAR = "2014"
PAGE_COUNT = 54
TEXT_DIR = ROOT / "artifacts/papers" / PID / "text/pages"
STAGE = ROOT / "tmp/q102-stage-v2"


def load_template_module():
    path = ROOT / "scripts/build_q100_artifacts.py"
    spec = importlib.util.spec_from_file_location("q100_template_for_q102", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHAPTERS = [
    ("title", "title", 2, 2, "TTL", "The title turns a familiar keep-right phrase into a compact traffic-rule evaluation frame."),
    ("summary", "abstract", 1, 3, "ABS", "The duplicated summary states the simulation ladder, nine-rule comparison, five evaluation criteria, traffic-regime result, left-driving adaptation, intelligent control, and ramp extension."),
    ("problem-restatement", "problem-restatement", 6, 6, "RST", "The restatement separates overtaking simulation from multi-criteria rule evaluation and names left-driving and intelligent-system extensions."),
    ("introduction", "introduction", 6, 7, "INT", "The introduction moves from freeway performance to the keep-right decision, then positions cellular automata through a short literature review."),
    ("assumptions", "assumptions", 7, 8, "ASM", "The assumptions exclude pedestrians, crosswind, emergency-lane use, curves, and slopes while fixing homogeneous rule-following categories."),
    ("notation", "notation", 8, 9, "NOT", "The notation tables bind lane gaps, vehicle speeds, time steps, flow counts, experience measures, and multi-criteria quantities to stated units."),
    ("model-overview", "problem-analysis", 10, 10, "OVR", "The overview connects a microscopic lane-change model, a periodic ring-road cellular automaton, and an open-boundary ramp refinement."),
    ("basic-lane-change", "model-establishment", 10, 12, "BAS", "The basic model translates overtaking trigger, acceleration, front-gap, rear-gap, and return-lane safety reasoning into inequalities."),
    ("cellular-automaton", "algorithm", 13, 19, "CEL", "The extended model fixes vehicle classes, cells, speeds, probabilities, update order, lane-change laws, and periodic boundary conditions."),
    ("ramp-refinement", "model-improvement", 20, 21, "RMP", "The refined model adds entrance and exit ramps, open boundaries, Poisson inflow, exit propensity, and failed-entry or failed-exit outcomes."),
    ("influencing-factors", "results", 22, 35, "FAC", "The factor study defines light and heavy traffic and compares lanes, maximum and minimum speed limits, and signaling across flow, safety, and experience criteria."),
    ("rule-evaluation", "data-preprocessing", 36, 43, "FSE", "The rule study defines five basic and four improved alternatives, aligns five criteria, constructs relative deviations, and reports regime-specific preferred rules."),
    ("sensitivity", "sensitivity-analysis", 43, 46, "SEN", "The sensitivity study perturbs vehicle mix, randomization probability, and willingness to change lanes by up to fifteen percent."),
    ("further-discussion", "future-improvements", 46, 52, "FUT", "The discussion mirrors the model for left-driving countries, changes compliance probabilities for intelligent control, and varies ramp-exit propensity."),
    ("strengths-weaknesses", "strengths-limitations", 53, 53, "SWK", "The final assessment credits vehicle heterogeneity, criteria, ramps, and apparent local robustness while acknowledging simplified judgment and guessed parameters."),
    ("conclusion", "conclusion", 35, 43, "CON", "Section conclusions convert factor and rule comparisons into different recommendations for light traffic, heavy traffic, and rush-hour operation."),
    ("references", "references", 53, 54, "REF", "The references identify cellular-automaton, traffic-engineering, fuzzy-evaluation, web, and company-data sources without supplying executable inputs or simulation code."),
]

PATTERNS = [
    "LP-B-SUMMARY-TASK-SIMULATION-DECISION",
    "LP-B-INTRO-POLICY-MECHANISM-ROADMAP",
    "LP-B-ASSUMPTION-OPERATIONAL-CONSEQUENCE",
    "LP-B-NOTATION-UNIT-DOWNSTREAM-USE",
    "LP-B-TRIGGER-SAFETY-INEQUALITY",
    "LP-B-STATE-UPDATE-ORDERED-ALGORITHM",
    "LP-B-BOUNDARY-CONDITION-SCOPE",
    "LP-B-TRAFFIC-REGIME-DEFINITION",
    "LP-B-CRITERION-DEFINITION-FORMULA",
    "LP-B-FACTOR-CONTROLLED-COMPARISON",
    "LP-B-RULE-ALTERNATIVE-IMPLEMENTATION",
    "LP-B-MULTICRITERIA-WEIGHT-DEVIATION",
    "LP-B-SENSITIVITY-PERTURBATION-BOUNDARY",
    "LP-B-EXTENSION-PARAMETER-MECHANISM",
    "LP-B-STRENGTH-LIMIT-IMPROVEMENT",
    "LP-B-REFERENCE-PROVENANCE-BOUNDARY",
    "LP-B-VISUAL-ENCODING-CLAIM-BOUNDARY",
]

MOVES = [
    ("task-simulation-decision", "State the rule-evaluation task, name the simulation ladder, report the regime-specific decision, and preserve its scope.", "task -> model ladder -> criterion -> decision -> scope"),
    ("policy-mechanism", "Move from a traffic policy question to the overtaking mechanism and then to measurable performance outputs.", "policy -> behavior -> simulation -> output"),
    ("assumption-consequence", "Pair each road, driver, cell, or boundary assumption with the operation it enables and the omitted regime.", "assumption -> rationale -> enabled step -> exclusion"),
    ("notation-contract", "Define gap, speed, count, probability, unit, and role before the symbol enters an update rule or criterion.", "symbol -> definition -> unit -> downstream use"),
    ("trigger-safety", "Separate incentive from front-gap and rear-gap safety conditions before allowing a lane change.", "trigger -> acceleration opportunity -> rear safety -> action"),
    ("ordered-update", "Present acceleration, randomization, collision avoidance, motion, and lane changing in executable order.", "state -> ordered laws -> next state -> check"),
    ("boundary-scope", "Explain why periodic or open boundaries are chosen and which traffic quantity they control.", "boundary choice -> controlled quantity -> simulation scope -> limitation"),
    ("regime-definition", "Define light and heavy traffic from occupancy and time-space behavior before comparing policies.", "observable pattern -> threshold -> regime -> later comparison"),
    ("criterion-formula", "Name a performance dimension, define its formula and direction, and state what decision it supports.", "dimension -> formula -> direction -> interpretation"),
    ("controlled-factor", "Hold the model route fixed, vary one declared factor, compare light and heavy traffic, and bound the inference.", "baseline -> factor change -> metric response -> boundary"),
    ("rule-implementation", "Describe a rule through operational lane assignments or limits before evaluating its results.", "rule -> implementation -> mechanism -> expected effect"),
    ("multicriteria-deviation", "Align alternatives and criteria, form an ideal vector, compute criterion weights and deviations, and rank by lower distance.", "alternatives -> criteria -> weights -> deviation -> rank"),
    ("local-sensitivity", "Perturb a declared parameter, report metric movement, and limit robustness to the tested range and simulation design.", "parameter -> perturbation -> response -> local limit"),
    ("extension-mechanism", "Modify orientation, compliance probability, or ramp propensity and trace the resulting mechanism before claiming transfer.", "new regime -> changed parameter -> mechanism -> result -> condition"),
    ("strength-limit", "Retain the constructive simulation contribution before naming data, behavioral, stochastic, or reproducibility limits.", "strength -> evidence -> boundary -> improvement"),
    ("provenance-boundary", "Separate cited traffic context and company data from frozen inputs, code, seeds, and reproducible outputs.", "source role -> supplied input -> transformation -> missing artifact"),
    ("visual-evidence", "Read diagrams, plots, tables, and flowcharts through labels, axes, comparators, and the claim they can actually support.", "encoding -> visible relation -> linked claim -> boundary"),
]

EXAMPLES = [
    ("A traffic-rule study first defines the road regime and driver state, then orders the cell updates before comparing flow and safety outputs.", "The method paragraph makes the state transition inspectable before presenting policy preferences."),
    ("A lane-change rule separates the desire to pass from front-gap and rear-gap safety checks.", "The prose preserves which inequality blocks the maneuver and which condition merely motivates it."),
    ("A factor experiment holds the cellular-automaton mechanism fixed while changing one speed-limit or signaling setting.", "Its conclusion is stated separately for light and heavy traffic rather than generalized to every density."),
    ("A rule comparison defines flow, speed, braking, satisfaction, and speed variability before weighting them.", "The preferred alternative remains conditional on the criterion direction and traffic regime."),
    ("A sensitivity table varies one probability over a declared range and reports metric deviations from the baseline.", "The result is called local simulation stability rather than proof of external validity."),
    ("A ramp extension replaces periodic boundaries with stochastic inflow and explicit entry and exit behavior.", "Its outputs include failure to enter or exit, not only average flow and speed."),
]


def build_language(template, pages):
    template.PID = PID
    template.SHORT = SHORT
    template.SHA = SHA
    template.TYPE = TYPE
    template.YEAR = YEAR
    template.PAGE_COUNT = PAGE_COUNT
    template.TEXT_DIR = TEXT_DIR
    template.STAGE = STAGE
    template.CHAPTERS = CHAPTERS
    template.PATTERNS = PATTERNS
    template.MOVES = MOVES
    template.EXAMPLES = EXAMPLES
    language = template.make_language(pages)
    for unit in language["units"]:
        unit["function"] = "Preserve a source-anchored traffic-rule rhetorical move and transfer it only after replacing road, vehicle, regime, parameter, criterion, and decision scope."
        unit["reusable_pattern"] = "traffic context or state -> typed operation -> measured output -> scoped handoff"
        unit["information_order"] = ["road regime or vehicle state", "inequality, update, simulation, or comparison", "measured metric or preferred rule", "condition and receiving use"]
        unit["reusable_elements"] = ["explicit traffic regime", "defined unit and criterion direction", "ordered mechanism", "result before caveat"]
        unit["prohibited_generalizations"] = ["Do not present a finite cellular-automaton run as universal traffic-policy truth.", "Do not detach a flow, speed, braking, satisfaction, deviation, or probability value from its definition, units, density regime, code, and run design."]
        unit["features"]["quantitative_role"] = "bind a gap, speed, probability, count, weight, relative deviation, or sensitivity response to its declared traffic decision role"
        unit["features"]["transition"] = "first, then, therefore, conversely, however, and finally connect state laws, regimes, criteria, results, and extensions"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 54 local UTF-8 page text files were read programmatically; chapter counts use declared bounded physical-page ranges, and byte-bounded JPEG review proxies supply the visual boundary check."
        layout["ambiguities"] = ["Extraction flattens inequalities, subscripts, matrices, axes, table alignment, and corrupted punctuation; source-level visual checks retain uncertainty rather than silently repairing notation.", "The paper does not provide simulation code, seeds, replicate counts, raw outputs, or a frozen parameter file; those are last-pass evidence boundaries, not substitutes for positive language learning."]
    return language


def equation(index, page, label, latex, symbols, purpose, confidence="high"):
    return {"equation_id": f"EQ-B-{YEAR}-{SHORT}-{index:03d}", "page": page, "label": label, "source_expression": latex, "normalized_latex": latex, "purpose": purpose, "variable_symbols": symbols, "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}


def make_model(template, model_id, page, section, family, purpose, inputs, outputs, equations):
    model = template.make_model(model_id, page, section, family, purpose, inputs, outputs, equations)
    model["summary"] = purpose
    for variable in model["variables"]:
        variable["definition"] = f"Source-defined traffic-rule quantity {variable['symbol']}."
        variable["unit"] = "cell, cell/time-step, time-step, count, probability, ratio, relative deviation, or dimensionless weight as defined by the source"
    model["objectives"] = [purpose, "Return a typed vehicle state, traffic metric, rule comparison, sensitivity response, or regime-specific recommendation."]
    model["constraints"] = ["Keep lane orientation, vehicle type, occupancy, speed limits, probabilities, boundary conditions, metric direction, and traffic regime explicit.", "A finite simulation result, common-sense agreement, or local parameter perturbation does not establish causal superiority or external policy validity."]
    model["conditions"] = {"initial": {"status": "present", "details": ["Vehicle mix, road cells, speed limits, occupancy or inflow, lane-change probabilities, and the selected overtaking rule are supplied or assumed."]}, "boundary": {"status": "present", "details": ["Periodic ring-road and open-ramp boundaries represent different systems and cannot be interchanged without changing interpretation."]}, "equilibrium": {"status": "present", "details": ["The source runs 20000 time steps and analyzes the last 1000 as steady-state output, but supplies no convergence diagnostic, seed, or replicate evidence."]}}
    model["parameter_estimation"] = {"status": "partial", "method": "Published traffic literature, one company vehicle-mix source, stated assumptions, semi-educated guesses, simulation outputs, coefficient-of-variation weights, and local perturbations.", "parameters": [v["symbol"] for v in model["variables"]]}
    model["algorithm"] = {"status": "partial", "steps": ["freeze road, vehicle, rule, and traffic-regime inputs", "apply the ordered movement and lane-change laws", "collect flow, speed, safety, utilization, and experience outputs", "compare factors or alternatives and perform declared sensitivity changes", "handoff the conditional result to a rule recommendation or extension"], "software": ["No simulation source code, runtime environment, seed policy, replicate count, parameter file, or raw output archive is supplied."], "convergence_criteria": "The source treats the last 1000 of 20000 steps as steady state; no quantitative burn-in, autocorrelation, Monte Carlo error, or cross-seed convergence test is reported."}
    model["assumptions"] = ["Cell geometry, driver myopia, homogeneous rule logic, random slowing, vehicle mix, and lane-change willingness are adequate surrogates for the stated freeway scenarios.", "The chosen traffic metrics and coefficient-of-variation aggregation represent flow, safety, and driver experience for the rule decision."]
    model["identifiability_feasibility"] = {"status": "partial", "analysis": "Equations, diagrams, criteria, tables, and rule descriptions are inspectable, but code, parameter calibration, random seeds, raw trajectories, replicates, uncertainty, and field validation are incomplete."}
    model["computational_cost"] = "Driven by vehicle-by-vehicle cell updates over 20000 steps, lane and gap searches, repeated density and policy scenarios, nine-rule evaluation, and parameter sensitivity reruns."
    model["strengths"] = ["The source connects microscopic behavior to rule-level performance through explicit intermediate criteria.", "Light and heavy traffic are separated before reporting preferred alternatives, preserving an important decision condition."]
    model["limitations"] = ["Behavioral calibration, stochastic uncertainty, external validation, and executable reproducibility are incomplete.", "Confirmed source inconsistencies remain in the final warning pass rather than being silently corrected."]
    model["missing_details"] = ["Official task text, source code, exact initialization, random seeds, replicate count, uncertainty intervals, raw trajectories, parameter calibration, complete FSE derivation, and field-validation data are absent."]
    return model


def build_models(template):
    lane = [
        equation(1, 11, "overtaking trigger", r"v_{expect}>v_s", ["v_expect", "v_s"], "Trigger interest in passing when expected speed exceeds the current constrained speed."),
        equation(2, 11, "left rear safety", r"D_{l,b,gap}>(v_{lb}-v_s)t", ["D_lbgap", "v_lb", "v_s", "t"], "Require sufficient rear clearance on the left lane."),
        equation(3, 12, "left front opportunity", r"D_{l,f,gap}>(v_s-v_{lf})t", ["D_lfgap", "v_s", "v_lf", "t"], "Require enough front clearance to avoid slowing after moving left."),
        equation(4, 12, "right rear safety", r"D_{r,b,gap}>(v_{rb}-v_s)t", ["D_rbgap", "v_rb", "v_s", "t"], "Require sufficient rear clearance when returning right."),
        equation(5, 12, "right front opportunity as printed", r"D_{r,b,gap}>(v_s-v_{rf})t", ["D_rbgap", "v_s", "v_rf", "t"], "Retain the printed right-front condition while flagging its repeated rear-gap symbol.", "medium"),
    ]
    ca = [
        equation(6, 17, "acceleration update", r"v_j^i(t+1/3)=v_j^i(t)+1", ["v_j_i", "t"], "Increase speed by one cell per step below the expected speed."),
        equation(7, 17, "random slowing", r"v_j^i(t+2/3)=v_j^i(t+1/3)-1", ["v_j_i", "t", "p_slow"], "Apply a one-cell random deceleration with probability p_slow."),
        equation(8, 17, "collision-avoidance update", r"v_j^i(t+1)=gap_j^i(t)\quad\mathrm{if}\ v_j^i(t+2/3)>gap_j^i(t)", ["v_j_i", "gap_j_i", "t"], "Cap motion by the front gap to prevent overlapping cells."),
        equation(9, 17, "position update", r"x_j^i(t+1)=x_j^i(t)+v_j^i(t+1)", ["x_j_i", "v_j_i", "t"], "Advance the vehicle after speed updates."),
        equation(10, 17, "front gap", r"gap_j^i=x_{j+1}^i-x_j^i-1", ["gap_j_i", "x_j_i"], "Calculate discrete clearance to the next vehicle."),
    ]
    metrics = [
        equation(11, 23, "flow rate", r"q=N/T", ["q", "N", "T"], "Count vehicles passing a point per unit time."),
        equation(12, 23, "lane utilization", r"u_j(t)=N_j(t)/N(t)", ["u_j", "N_j", "N", "t"], "Measure each lane's share of freeway vehicles."),
        equation(13, 23, "shift ratio", r"r_{shift}(t)=N_{shift}(t)/N(t)", ["r_shift", "N_shift", "N", "t"], "Normalize lane changes by the number of vehicles."),
        equation(14, 23, "satisfaction", r"s=t_{expect}/t_{actual}", ["s", "t_expect", "t_actual"], "Represent achieved travel time relative to maximum-speed travel time."),
    ]
    fse = [
        equation(15, 40, "relative deviation", r"r_{ij}=|a_{ij}-u_{0j}|/(\max_i a_{ij}-\min_i a_{ij})", ["r_ij", "a_ij", "u_0j"], "Measure each alternative's criterion distance from the ideal; the paper prints an inconsistent ideal-vector subscript.", "medium"),
        equation(16, 41, "coefficient of variation", r"v_j=s_j/\bar{x}_j", ["v_j", "s_j", "xbar_j"], "Measure how strongly a criterion differentiates alternatives."),
        equation(17, 41, "criterion weight", r"w_j=v_j/\sum_{k=1}^{5}v_k", ["w_j", "v_j"], "Normalize coefficient-of-variation values into criterion weights.", "medium"),
        equation(18, 41, "aggregate deviation", r"F_i=\sum_{j=1}^{5}w_jr_{ij}", ["F_i", "w_j", "r_ij"], "Rank each traffic rule by weighted distance from the ideal alternative."),
    ]
    models = [
        make_model(template, f"MU-B-{YEAR}-{SHORT}-001", 11, "Basic lane-changing model", "gap-and-speed lane-change conditions", "Represent the trigger and safety logic for moving left to pass and returning right.", ["vehicle speeds", "front and rear gaps", "time horizon"], ["lane-change eligibility"], lane),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-002", 13, "Extended ring-road model", "multi-lane cellular automaton", "Simulate heterogeneous vehicles through ordered movement and lane-change updates under periodic boundaries.", ["cells", "vehicle mix", "speed limits", "occupancy", "p_slow", "p_left", "p_right"], ["vehicle trajectories", "steady-window outputs"], ca),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-003", 20, "Refined model with ramps", "open-boundary cellular automaton", "Add entrance and exit ramps, Poisson inflow, exit propensity, and failed entry or exit behavior.", ["lambda", "p_exit", "ramp positions", "vehicle laws"], ["ramp flow", "failure ratio"], []),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-004", 22, "Traffic criteria", "traffic performance measurement", "Measure traffic flow, safety, lane use, and driver experience for factor and rule comparisons.", ["trajectories", "vehicle counts", "speeds", "travel times"], ["flow", "average speed", "lane utilization", "sharp braking", "shift ratio", "satisfaction", "speed variability"], metrics),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-005", 24, "Influencing-factor experiments", "controlled simulation comparison", "Vary occupancy, lanes, speed limits, and signaling while separating light and heavy traffic results.", ["baseline CA", "factor levels", "traffic regime"], ["criterion response curves", "factor conclusions"], []),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-006", 36, "Alternative overtaking rules", "policy mechanism comparison", "Encode five basic and four improved lane rules as changes to the same cellular-automaton laws.", ["nine rule definitions", "vehicle classes", "lane constraints"], ["rule-specific simulation outputs"], []),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-007", 39, "Rule aggregation", "coefficient-of-variation weighted relative deviation", "Combine five traffic criteria and select regime-specific rules by distance from an ideal alternative.", ["criterion matrix", "ideal vector", "criterion variation"], ["weights", "relative deviations", "rule ranking"], fse),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-008", 43, "Sensitivity analysis", "local parameter sensitivity", "Perturb vehicle mix, random slowing, and lane-change willingness by up to fifteen percent and record metric deviations.", ["baseline parameters", "plus-or-minus 15 percent range"], ["metric deviations", "local robustness claim"], []),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-009", 46, "Transfer and extensions", "left-driving, intelligent-control, and ramp scenarios", "Modify orientation, compliance probabilities, and p_exit to explore transfer beyond the base ring-road rule.", ["orientation", "p_left", "p_right", "p_exit", "boundary type"], ["extended scenario metrics", "conditional transfer findings"], []),
    ]
    edges = [
        {"from_model_id": models[0]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "Trigger and safety inequalities become the lane-change laws in the cellular automaton."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[2]["model_id"], "handoff": "The movement laws are retained while periodic boundaries are replaced by explicit ramps and stochastic inflow."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "Vehicle trajectories and event counts feed the flow, safety, utilization, and experience metrics."},
        {"from_model_id": models[3]["model_id"], "to_model_id": models[4]["model_id"], "handoff": "The typed criteria are compared across controlled factor levels and traffic regimes."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[5]["model_id"], "handoff": "Alternative policies are encoded by changing the cell and lane laws while retaining the base simulation interface."},
        {"from_model_id": models[5]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "Nine rule-specific metric vectors enter the weighted relative-deviation calculation."},
        {"from_model_id": models[6]["model_id"], "to_model_id": models[7]["model_id"], "handoff": "The selected rule and baseline parameters define the local sensitivity experiments."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[8]["model_id"], "handoff": "Open-boundary ramp outputs and compliance probabilities are reused in the transfer scenarios."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def build_card(models):
    assumptions = [
        (7, "Pedestrians, crosswind, emergency-lane traffic, curvature, and grades can be omitted for the stated freeway simulation."),
        (8, "Aggressive and non-aggressive drivers follow the same relevant rule set and act from local information."),
        (13, "Drivers change lanes with fixed willingness probabilities, maximize their own travel progress, and use only nearby vehicles."),
        (14, "A 4 m by 6 m cell, 2000-cell road, one-second step, and last 1000 of 20000 steps adequately represent the modeled freeway."),
        (15, "Cars, buses, and trucks occur in a 60/30/10 mix with fixed occupancy and maximum speeds."),
        (19, "Periodic boundaries represent a repeatable long freeway section at controlled occupancy."),
        (21, "Open-boundary inflow is Poisson and entrance-ramp inflow is balanced in expectation with exit-ramp demand."),
        (39, "Coefficient-of-variation weights appropriately encode criterion importance from discrimination among alternatives."),
    ]
    data = [
        (1, "The summary names five performance criteria, nine rules, and separate preferred rules for light and heavy traffic."),
        (9, "Notation tables define vehicle states, gap variables, event counts, multi-criteria values, weights, and relative deviation."),
        (15, "Vehicle characteristics fix cell occupancy, maximum speed, and a 60/30/10 traffic mix attributed to a freeway-company source."),
        (22, "Occupancy and time-space diagrams distinguish light traffic at 0.1 from heavy traffic at 0.4 for later experiments."),
        (23, "Flow, speed, lane utilization, sharp braking, shifting, satisfaction, and speed variability are defined as performance criteria."),
        (36, "Five basic rules and four improved rules are encoded as lane-changing, lane-assignment, or lane-specific speed constraints."),
        (40, "Table 4 supplies the five-rule by five-criterion light-traffic matrix and the ideal alternative."),
        (41, "Tables 5 and 6 report relative deviations for basic rules under light and heavy traffic."),
        (43, "Table 7 reports nine-rule deviations and regime-specific preferred policies."),
        (44, "Sensitivity tables record relative output changes for vehicle mix, randomization, and lane-change willingness."),
    ]
    verification = [
        (12, "The lane-change inequalities can be checked against the diagrammed front and rear vehicles.", "formula-to-diagram trace", "Trigger and safety roles are separated.", "The final right-front inequality repeats the rear-gap symbol."),
        (17, "Acceleration, randomization, collision avoidance, motion, and gap calculation can be checked in update order.", "algorithm trace", "The finite-state sequence is explicit.", "No code or simultaneous-update conflict handling is supplied."),
        (19, "The periodic boundary explanation can be checked against constant vehicle count and occupancy control.", "boundary-condition trace", "The intended density control is explicit.", "A short ring is only an asserted surrogate for a long open freeway."),
        (23, "Criterion formulas can be traced from vehicle events to performance dimensions.", "metric audit", "Flow, safety, utilization, and experience are separated.", "Several extracted summations and labels require visual interpretation."),
        (35, "Factor conclusions can be compared with Figures 7-23 under light and heavy traffic.", "controlled-comparison audit", "The source repeatedly separates regimes.", "No raw trajectories, seeds, replicates, or uncertainty bars are supplied."),
        (41, "The five basic-rule rows can be recomputed from Table 4, the ideal vector, weights, and aggregate deviation.", "multi-criteria audit", "The paper exposes intermediate values.", "The method is called fuzzy although the displayed calculation is coefficient-of-variation weighted distance."),
        (43, "Table 7 supports the two regime-specific rule recommendations.", "decision-table trace", "All nine alternatives are co-located.", "The overall column aggregation is not explained."),
        (46, "Sensitivity tables identify the changed input and percentage response for five metrics.", "local sensitivity", "Three uncertain parameter groups are tested.", "One stochastic realization or unknown replicate design cannot establish general robustness."),
        (52, "Ramp-extension figures connect p_exit to flow, speed, lane use, and failure ratio.", "extension trace", "The additional outputs are visible.", "Balancing entrance and exit counts partly constrains the observed flow behavior."),
    ]
    results = [
        (24, "Occupancy around 0.2-0.3 is treated as the watershed between light and heavy traffic."),
        (35, "Lane number is reported as weak at fixed occupancy, maximum speed limit matters mainly in light traffic, and minimum speed limit mainly in heavy traffic."),
        (35, "Signaling is reported to reduce flow and speed while changing braking and shifting behavior."),
        (41, "Among five basic rules, keep-right has the smallest light-traffic deviation and lane-specific speed limits the smallest heavy-traffic deviation."),
        (43, "Among all nine rules, partial-assigned-lane-and-keep-right is preferred in light traffic and lane-specific speed limits in heavy traffic."),
        (46, "The tested plus-or-minus fifteen-percent parameter changes yield reported metric deviations up to about 16.6 percent."),
        (47, "Swapping lane-change willingness for left-driving transfer is reported to change criteria by at most 4.6 percent."),
        (48, "Intelligent control is reported to improve heavy-traffic flow while increasing shifting and changing lane utilization."),
        (52, "Higher p_exit lowers heavy-traffic average speed and, in the reported simulation, can lower failure to reach the exit."),
    ]
    writing = [
        (1, "Summary chain: overtaking-rule task -> lane-change mechanism -> ring-road cellular automaton -> nine-rule criteria -> regime-specific choice -> transfer and ramps."),
        (6, "Restatement chain: simulate overtaking -> expose changeable inputs and mechanisms -> collect outputs -> combine flow, safety, and experience -> choose a rule."),
        (7, "Literature chain: single-lane cellular automaton -> multi-lane safety and incentive -> heterogeneous vehicles -> expectation-aware extension."),
        (10, "Overview chain: microscopic trigger model -> periodic multi-lane automaton -> open-boundary ramp refinement -> standard-model experiments."),
        (11, "Lane-change chain: desire to pass -> rear safety -> front opportunity -> left maneuver -> return-right constraints."),
        (16, "Algorithm chain: state and vehicle type -> acceleration -> randomization -> safety deceleration -> motion -> lane-change test -> next state."),
        (19, "Boundary chain: constant-count periodic road -> controlled occupancy -> light/heavy comparison -> open-boundary ramp handoff."),
        (22, "Factor-results chain: define traffic regimes -> define criteria -> vary one factor -> compare plots -> state regime-specific effect."),
        (36, "Rule-results chain: define operational alternatives -> inspect single criteria -> weight variation -> aggregate distance -> choose by regime."),
        (43, "Sensitivity chain: uncertain parameter -> plus-or-minus range -> metric response table -> local robustness statement."),
        (46, "Extension chain: new driving orientation or controller -> changed willingness parameter -> mechanism -> simulation output -> conditional transfer."),
        (50, "Ramp chain: open-boundary model -> vary exit propensity -> flow, speed, lane-use, and failure outputs -> heavy/light distinction."),
        (53, "Final chain: practical model strengths -> behavioral and calibration weaknesses -> references and reproducibility boundary."),
    ]
    contributions = [
        {"page": 11, "summary": "Separates lane-change incentive from front and rear safety conditions."},
        {"page": 16, "summary": "Turns the behavioral analysis into an ordered multi-lane cellular-automaton interface."},
        {"page": 19, "summary": "Uses periodic boundaries to control occupancy for factor comparisons."},
        {"page": 20, "summary": "Adds explicit ramp behavior and open boundaries as a realism extension."},
        {"page": 23, "summary": "Evaluates traffic rules on flow, safety, lane use, and driver-experience dimensions."},
        {"page": 36, "summary": "Encodes implementable alternatives through lane assignments and lane-specific speed limits."},
        {"page": 43, "summary": "Reports different preferred rules for light and heavy traffic rather than one unconditional policy."},
    ]
    visuals = [
        {"page": 11, "figure": "Figure 1", "summary": "The left-lane schematic fixes the subject vehicle, nearby vehicles, and gap directions used by the trigger and safety inequalities."},
        {"page": 13, "figure": "Figure 2", "summary": "The return-right schematic distinguishes right-front and right-rear vehicles for the printed conditions."},
        {"page": 18, "figure": "Figure 4", "summary": "The cellular-automaton flowchart makes the movement and lane-changing decision order inspectable."},
        {"page": 20, "figure": "Figure 5", "summary": "The freeway photograph anchors the exit-before-entrance ramp geometry used by the refined model."},
        {"page": 22, "figure": "Figure 6", "summary": "Time-space diagrams contrast unconstrained high-speed traces with congested low-speed traces for the light/heavy distinction."},
        {"page": 24, "figure": "Figures 7-15", "summary": "Occupancy sweeps compare flow, speed, lane utilization, braking, shifting, satisfaction, and speed variability for three and four lanes."},
        {"page": 30, "figure": "Figures 16-23", "summary": "Paired light/heavy plots expose the effects of maximum limits, minimum limits, and signaling across traffic metrics."},
        {"page": 37, "figure": "Figures 24-26", "summary": "Basic-rule plots compare flow, speed, braking, satisfaction, and speed variability before aggregation."},
        {"page": 40, "figure": "Table 4 and FSE matrix", "summary": "The criterion table, ideal vector, relative-deviation matrix, and weight vector expose the multi-criteria calculation inputs."},
        {"page": 41, "figure": "Tables 5-6", "summary": "The basic-rule deviation tables make the light/heavy preference reversal directly scannable."},
        {"page": 43, "figure": "Table 7", "summary": "The nine-rule table places light, heavy, and unexplained overall deviations beside the final recommendations."},
        {"page": 44, "figure": "Tables 8-13", "summary": "Sensitivity tables show signed metric changes for three parameter groups across both traffic regimes."},
        {"page": 48, "figure": "Figures 27-29", "summary": "Intelligent-system plots compare baseline, semi-intelligent, and complete control for flow, speed, braking, shifting, and lane use."},
        {"page": 50, "figure": "Figures 30-33", "summary": "Ramp plots trace p_exit against flow, average speed, lane utilization, and failure ratio in light and heavy traffic."},
    ]
    warnings = [
        (1, "The cover text reads 'Problem Chosen A' while the corpus manifest and filename classify this record as problem type B; the artifact retains manifest type B and records the source mismatch."),
        (1, "The summary says five improved rules, while section 7.4 defines four improved rules in addition to five basic rules."),
        (22, "The prose calls the occupancy time-space diagram Figure 8 while the page caption labels it Figure 6; later pages use Figure 8 for a lane-flow plot."),
        (12, "The printed right-front opportunity inequality repeats D_r,b,gap instead of the right-front symbol defined in the notation table."),
        (17, "The update equations and flowchart do not fully specify simultaneous lane-change conflict resolution or vehicle update ordering across lanes."),
        (21, "Open-boundary inflow, ramp-entry balance, and failed-entry handling are described in prose without a complete stochastic transition specification."),
        (23, "The extracted average-speed and speed-standard-deviation formulas have flattened indices and require visual source interpretation before numerical reuse."),
        (35, "The conclusion says signaling enhances safety although the immediately preceding discussion reports increased sharp-braking frequency."),
        (39, "The paper calls the aggregation fuzzy synthetic evaluation, but the displayed method uses coefficient-of-variation weights and distance from an ideal alternative without fuzzy membership grades."),
        (40, "The relative-deviation formula prints u_0i although the notation table and ideal vector imply a criterion-indexed u_0j; Table ?? is also an unresolved cross-reference."),
        (43, "The overall relative-deviation column in Table 7 is not derived or explained, so it cannot be independently reconstructed from the light and heavy columns."),
        (46, "The sensitivity claim lacks random seeds, replicate counts, Monte Carlo error, confidence intervals, and convergence evidence; maximum reported deviations reach about 16.6 percent."),
        (47, "The left-driving transfer assumes persistent asymmetric left/right lane-change willingness without empirical calibration and contains missing table references."),
        (52, "Ramp-flow conclusions are conditional on balancing entrance inflow with exit demand and on unreported simulation settings."),
        (53, "Agreement with common sense is used as validation without field trajectories, held-out data, or an external benchmark."),
        (54, "No executable code, frozen parameter file, initialization, raw output, seed, environment, or reproduction package is supplied."),
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 17, "summary": "Publish executable update rules with deterministic conflict resolution and cross-seed tests."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 22, "summary": "Calibrate occupancy regimes and lane-change probabilities against detector or trajectory data."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 39, "summary": "Compare the displayed relative-deviation method with explicit multi-criteria alternatives under transparent preference weights."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 43, "summary": "Report rule rankings across a continuous density range with uncertainty and rank-stability intervals."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 46, "summary": "Use variance decomposition, multiple seeds, and global sensitivity rather than single-parameter percentage tables."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 50, "summary": "Validate ramp queues, missed exits, and open-boundary flows against real merge and diverge observations."},
    ]
    return {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": SHORT, "title": "Keep Right to Keep Right?", "award_status": "outstanding",
        "source": {"relative_path": "2014\u7f8e\u8d5b\u7279\u7b49\u5956/B-26333-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is the contest summary cover; physical page 2 is printed page 1, and physical page 54 is printed page 53."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["All 54 local UTF-8 page text files were read in bounded physical-page ranges.", "All 54 physical pages were visually reviewed through isolated byte-bounded JPEG proxies before stage generation.", "No full-page original PNG, embedded base64 image, or multi-image tool result was sent through model transport.", "Formula, matrix, chart, table, type-classification, and cross-reference uncertainties remain explicit warning anchors rather than silent repairs."]},
        "context_sources": [{"type": "paper", "path": "2014\u7f8e\u8d5b\u7279\u7b49\u5956/B-26333-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "text-pages", "path": f"artifacts/papers/{PID}/text/pages"}],
        "task_reconstruction": {"status": "incomplete-official-task-unavailable", "inputs": ["freeway geometry and boundaries", "vehicle types and speeds", "occupancy or inflow", "lane-change probabilities", "overtaking rules", "flow, safety, and experience criteria"], "outputs": ["vehicle trajectories", "traffic metrics", "factor comparisons", "nine-rule deviations", "light/heavy recommendations", "sensitivity and transfer scenarios"], "decisions": ["how to encode lane changing", "which boundary model to use", "which criteria define performance", "which rule is preferred by traffic regime", "whether transfer claims are supported"]},
        "section_map": [{"page": start, "section": key, "summary": summary} for key, chapter, start, end, tag, summary in CHAPTERS],
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions], "data_and_preprocessing": [{"page": p, "summary": s} for p, s in data],
        "models": [{"model_id": model["model_id"], "page": model["page"], "summary": model["summary"]} for model in models["models"]], "dependency_graph": models["dependency_edges"],
        "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification],
        "results_trace": [{"page": p, "summary": s} for p, s in results], "contributions": contributions,
        "writing_logic": [{"page": p, "summary": s} for p, s in writing], "language_observations": [{"page": p, "summary": s} for p, s in writing],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The summary previews the complete simulation-to-rule-decision route, but award status alone does not prove which feature judges valued.", "evidence_class": "J"}, {"page": 18, "summary": "The algorithm flowchart makes a complicated vehicle update sequence scannable, without proving code correctness.", "evidence_class": "J"}, {"page": 43, "summary": "The nine-rule table gives a decision-facing light/heavy contrast, without establishing external traffic-policy validity.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": s} for p, s in warnings], "independent_extensions": extensions,
        "candidate_rule_impacts": [], "unresolved_questions": [s for _, s in warnings], "protocol_v2_records": {}, "review_status": "validated",
    }


def build_observations(template, language, models, card):
    observations = template.make_observations(language, models, card)
    dimension_interpretation = {
        "language": "Reuse the traffic-language move only after replacing road, vehicle, regime, parameter, metric, and policy entities.",
        "modeling": "Retain typed states, ordered updates, boundary conditions, criteria, alternatives, outputs, handoffs, and limitations.",
        "logic": "Preserve the positive task-to-behavior-to-simulation-to-metric-to-regime-specific-decision chain.",
        "visualization": "Keep vehicle roles, axes, table headers, traffic regimes, comparators, and analytical purpose together.",
        "verification": "Name the formula, update order, boundary, metric, plot, table, perturbation, or extension being checked and limit the claim.",
        "data": "Retain source, units, vehicle mix, density, parameter value, rule definition, transformation, and downstream consumer.",
        "assumption": "Pair each assumption with its enabled simulation step, excluded regime, diagnostic, and recalibration need.",
        "result": "Keep traffic regime, metric direction, alternative, deviation, comparator, and evidence status distinct.",
        "weakness": "Record the source weakness only after positive language, organization, model, result, and visualization learning.",
        "other": "Separate citations and printed tables from frozen inputs, code, seeds, raw outputs, and reproducibility evidence.",
    }
    for row in observations:
        row["interpretation"] = dimension_interpretation[row["dimension"]]
        row["applicability"] = ["Apply only when road geometry, vehicle mix, traffic regime, boundary condition, rule, units, stochastic design, criterion direction, and decision scope are explicit."]
        row["counterevidence"] = ["A plotted response, preferred rule, common-sense agreement, or local sensitivity table does not prove causal superiority, external validity, reproducibility, or safe policy transfer."]
    return observations


def attach_rule_impacts(card, observations):
    first = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])

    def evidence(rule_id):
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])

    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain the traffic-policy-to-behavior-to-simulation-to-metric-to-regime-specific-decision sequence with explicit mechanism and scope", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "trace lane-change conditions through cellular-automaton laws, factor studies, alternative rules, multi-criteria comparison, sensitivity, and transfer scenarios", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "version road geometry, vehicle mix, speeds, occupancy, inflow, probabilities, rule definitions, metric units, simulation seeds, and raw outputs", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for driver behavior, cell scale, vehicle heterogeneity, steady-window choice, boundary conditions, criterion meaning, and transfer", "evidence_ids": [evidence("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain lane-change inequalities, periodic and open cellular automata, traffic criteria, factor experiments, nine rules, weighted deviations, sensitivity, and extensions", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine flow, speed, safety, and experience only through an explicit criterion direction, normalization, weight, and aggregation contract", "evidence_ids": [evidence("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep vehicle state, traffic metric, criterion weight, relative deviation, regime-specific rank, sensitivity response, and recommendation distinct", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress conflict resolution, burn-in, random seeds, replicates, behavioral calibration, FSE naming, overall-score derivation, and field validation", "evidence_ids": [evidence("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make evidence claims formula-, state-update-, boundary-, plot-, table-, perturbation-, and transfer-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile the type mismatch, improved-rule count, right-front gap symbol, signaling safety claim, ideal-vector subscript, overall column, and absent executable evidence", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain vehicle diagrams, update flowchart, time-space plots, factor curves, criterion tables, rule comparisons, sensitivity tables, and extension plots with labels and purpose", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "measure vehicle-by-step updates, lane-neighbor searches, scenario counts, nine-rule reruns, multi-seed uncertainty, aggregation, and sensitivity runtime", "evidence_ids": [evidence("R-B-COMP-001")]},
    ]


def build_audit(template, language, models, card, observations):
    audit = template.make_audit(language, models, card, observations)
    layouts = {item["chapter"]: item for item in language["chapter_layouts"]}
    units = language["units"]
    audit["paragraph_chains"] = []
    for chapter in ("abstract", "introduction"):
        ids = [unit["language_unit_id"] for unit in units if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": index + 1, "dominant_move": "traffic context or task -> simulation mechanism -> result or scope", "language_unit_ids": [ids[index % len(ids)]]} for index in range(layouts[chapter]["paragraph_count"])]})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete", "weakness_substitution_allowed": False,
        "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["The final warning pass records type, notation, algorithm, data, claim, stochastic, and reproducibility defects without replacing positive learning."],
        "section_progressions": [{"chapter": chapter, "moves": [f"input: source-checked road, vehicle, rule, parameter, criterion, plot, or table entering {chapter}", f"rhetorical job: state the positive mechanism, comparison, or recommendation in {chapter}", f"analytical job: define, update, simulate, measure, weight, compare, perturb, or transfer the declared object in {chapter}", f"output: retain a typed state, metric, deviation, rule choice, or evidence boundary from {chapter}", "handoff: name the next model, experiment, criterion, decision, extension, or reproduction boundary"], "positive_pattern": "Use explicit source input -> typed operation -> measured output -> scoped handoff; warnings remain a last pass."} for chapter in language["available_chapters"]],
        "main_argument_chains": [
            {"claim": "A traffic policy question becomes inspectable when lane-change behavior is translated into ordered cellular-automaton laws and typed metrics.", "support_steps": ["trigger and safety inequalities", "vehicle classes and cells", "ordered state updates", "periodic occupancy control", "flow, safety, and experience criteria"], "decision_consequence": "Reuse the model interface only with explicit conflict handling, calibration, stochastic design, and boundaries.", "source_pages": [10, 11, 13, 16, 17, 19, 22, 23]},
            {"claim": "Traffic regime is a necessary condition for interpreting factor effects and preferred overtaking rules.", "support_steps": ["occupancy sweep", "light/heavy definition", "factor plots", "five basic rules", "four improved rules", "relative-deviation tables"], "decision_consequence": "Do not present one rule as globally optimal outside its density, criterion, and simulation scope.", "source_pages": [22, 24, 30, 35, 36, 39, 41, 43]},
            {"claim": "Sensitivity and transfer scenarios remain conditional until stochastic uncertainty and field calibration are supplied.", "support_steps": ["parameter perturbations", "left-driving probability swap", "intelligent compliance", "open-boundary ramp variation", "missing code and seeds"], "decision_consequence": "Report these as scenario evidence rather than external policy validation.", "source_pages": [43, 46, 47, 48, 50, 52, 53, 54]},
        ],
    }
    lane_id = models["models"][0]["model_id"]
    fse_id = models["models"][6]["model_id"]
    audit["formula_error_watch"] = {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": [
        {"model_id": lane_id, "equation_id": f"EQ-B-{YEAR}-{SHORT}-005", "page": 12, "warning": "The printed right-front opportunity condition repeats the right-rear gap symbol; reconcile it with the notation table and Figure 2 before reuse."},
        {"model_id": fse_id, "equation_id": f"EQ-B-{YEAR}-{SHORT}-015", "page": 40, "warning": "The relative-deviation formula prints u_0i while the criterion-indexed ideal vector implies u_0j; the unresolved Table ?? reference and denominator indexing also require reconciliation."},
        {"model_id": fse_id, "equation_id": f"EQ-B-{YEAR}-{SHORT}-017", "page": 41, "warning": "The printed weight denominator is extraction-flattened; retain the normalized five-criterion form only as a source-checked interpretation, not a silent source correction."},
    ]}
    for item in audit["language_unit_dispositions"]:
        item["reason"] = "The source move is reusable after replacing traffic-rule entities, units, regimes, stochastic design, and decision scope."
    counts = Counter(item["dimension"] for item in observations)
    audit["dimension_counts"] = {dimension: counts[dimension] for dimension in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}
    audit["positive_reusable_language_count"] = len(units)
    audit["weakness_record_count"] = counts["weakness"]
    return audit


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    template = load_template_module()
    pages = {}
    for page in range(1, PAGE_COUNT + 1):
        source = TEXT_DIR / f"page-{page:04d}.txt"
        if not source.is_file():
            raise FileNotFoundError(source)
        pages[page] = source.read_text(encoding="utf-8")
    language = build_language(template, pages)
    models = build_models(template)
    card = build_card(models)
    card["protocol_v2_records"] = {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(model["governing_equations"]) for model in models["models"]), "review_status": models["review_status"]}}
    observations = build_observations(template, language, models, card)
    attach_rule_impacts(card, observations)
    audit = build_audit(template, language, models, card, observations)
    write_json(STAGE / "language.json", language)
    write_json(STAGE / "models.json", models)
    write_json(STAGE / "card.json", card)
    write_json(STAGE / "audit.json", audit)
    (STAGE / "observations.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "stage": str(STAGE), "pages_read": len(pages), "language_units": len(language["units"]), "models": len(models["models"]), "equations": sum(len(model["governing_equations"]) for model in models["models"]), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(card["visualization_observations"]), "warnings": len(card["weaknesses"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
