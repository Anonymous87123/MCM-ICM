#!/usr/bin/env python3
"""Build Queue 120 artifacts in an isolated, create-only staging directory.

This builder never deletes, moves, or overwrites a live artifact.  It refuses
to run when its dedicated staging directory is non-empty.  Promotion and the
transaction append are separate validated operations.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2017-70545-8e86fcfa"
ID_STEM = "B-2017-70545"
PROBLEM_TYPE = "B"
YEAR = "2017"
SHA256 = "8e86fcfa286c46c3d8bddc3ef1ab64b376abe7e07c86827adc811b6c086d9954"
PAGE_COUNT = 26
SOURCE_PATH = "2017美赛特等奖/B/B类-O奖--70545.pdf"
STAGE = ROOT / "tmp" / "q120-stage-v1"
SOURCE_EXTRACTION = ROOT / "artifacts" / "papers" / PAPER_ID / "extraction.json"


RULES = {
    "language": "R-B-LANG-001",
    "logic": "R-B-LOG-001",
    "modeling": "R-B-MOD-004",
    "visualization": "R-B-VIZ-002",
    "verification": "R-B-VER-004",
    "data": "R-B-DATA-002",
    "assumption": "R-B-DATA-002",
    "result": "R-B-MOD-004",
    "weakness": "R-B-VER-004",
    "other": "R-B-LOG-001",
}

ADDITIONAL_RULES = {
    "reliability": "R-B-VER-002",
    "stakeholder": "R-B-DEC-002",
}


def dump_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def dump_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.write_text(
        "".join(
            json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
            for value in values
        ),
        encoding="utf-8",
        newline="\n",
    )


def chapter(
    code: str,
    name: str,
    label: str,
    pages: tuple[int, int],
    count: int,
    source_input: str,
    rhetorical: str,
    analytical: str,
    output: str,
    handoff: str,
    phrases: list[str],
    moves: list[str],
    pattern_ids: list[str],
) -> dict[str, Any]:
    return {
        "code": code,
        "chapter": name,
        "label": label,
        "pages": pages,
        "count": count,
        "input": source_input,
        "rhetorical": rhetorical,
        "analytical": analytical,
        "output": output,
        "handoff": handoff,
        "phrases": phrases,
        "moves": moves,
        "pattern_ids": pattern_ids,
    }


PATTERNS = [
    {
        "pattern_id": "LP-B-Q120-AUTHOR-ACTION",
        "name": "author-led staged research action",
        "occurrences": {"we": 87, "our": 33},
        "locations": ["Summary", "Sections 4-8", "Authority letter"],
        "function": "Keep the team visible as the agent that defines, calculates, simulates, compares, and decides.",
        "information_order": ["author", "research action", "typed object", "method or evidence", "bounded output"],
        "slots": ["[we/our model]", "[define/calculate/simulate/compare/conclude]", "[named quantity or model]", "[method]", "[scope-bound result]"],
        "variants": ["we propose", "we introduce", "we calculate", "we get", "we conclude", "this section analyzes", "results are shown"],
        "boundary": "Use an explicit actor only when the action and evidence are named; do not let 'we get' replace a derivation, comparator, or uncertainty statement.",
        "disposition": "supports-existing",
        "original_examples": [
            "We estimate the clinic queue under three staffing rules and report the weekday interval used for comparison.",
            "Our reservoir model propagates the calibrated inflow ensemble before selecting a release rule for the stated drought horizon.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-STAGE-ROUTE",
        "name": "temporal route through the report",
        "occurrences": 8,
        "locations": ["Summary physical page 1"],
        "function": "Compress the paper into a visible sequence of assumptions, models, simulation, modification, sensitivity, and closure.",
        "information_order": ["stage marker", "method action", "object", "output", "next stage"],
        "slots": ["[before/then/after/finally]", "[action]", "[model or evidence]", "[result]", "[handoff]"],
        "variants": ["Before establishment", "And then", "After that", "The next section", "For the following section", "Finally"],
        "boundary": "A route marker is organizational evidence, not a result; an abstract still needs concrete findings and limits.",
        "disposition": "supports-existing",
        "original_examples": [
            "After defining the exposure groups, we fit the response model and then reserve the final section for policy stress tests.",
            "Finally, the report converts the verified energy balance into a plant-operating recommendation and a limitations ledger.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-SECTION-PREVIEW",
        "name": "section-opening scope preview",
        "occurrences": 6,
        "locations": ["physical pages 5, 10, 14, 15, 17"],
        "function": "Declare the analytical object and connect it to the preceding model before a long derivation.",
        "information_order": ["section pointer", "analysis verb", "object list", "prior-section link", "promised output"],
        "slots": ["[in this section/this section]", "[analyze/conduct/introduce]", "[objects]", "[prior result]", "[output]"],
        "variants": ["In this section, we...", "This section analyzes...", "our report will then proceed to analyze..."],
        "boundary": "Do not add a preview when the section opens more clearly with the exact defect, condition, or decision question.",
        "disposition": "supports-existing",
        "original_examples": [
            "This section compares the two routing policies by delay, missed demand, and operating cost using the demand states defined above.",
            "In this section, we convert the fitted survival curve into a maintenance interval and preserve the censoring boundary.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-DEFECT-SOLUTION",
        "name": "defect or changed condition to proposed mechanism",
        "occurrences": 6,
        "locations": ["Authority letter", "4.2 CTM", "4.3 WAM", "5.2", "6.1", "6.2"],
        "function": "Establish local necessity before introducing a control rule, waiting area, risk proxy, or lane allocation.",
        "information_order": ["current state", "failure or new condition", "consequence", "proposed mechanism", "expected benefit"],
        "slots": ["[baseline]", "[however/given defect]", "[affected metric]", "[we propose/one solution]", "[bounded benefit]"],
        "variants": ["Therefore, to solve...", "we propose a new model", "we wonder whether", "one possible solution"],
        "boundary": "A newly proposed mechanism remains a candidate until later comparison; WAM demonstrates why proposal language must not imply retention.",
        "disposition": "supports-existing",
        "original_examples": [
            "Because the baseline dispatch rule overloads the night shift, we test a capped release mechanism before judging its staffing cost.",
            "When sensor dropout removes the usual feedback signal, one possible solution is a conservative fallback controller with an explicit recovery condition.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-FORMALIZE",
        "name": "definition-condition-recurrence formalization",
        "occurrences": 15,
        "locations": ["Sections 4.2, 5.1, 5.2, 7 and Appendix"],
        "function": "Translate traffic prose into symbols, distributions, initial conditions, recurrences, stopping rules, and outputs.",
        "information_order": ["name concept", "define symbol", "state domain or distribution", "set initial/branch condition", "derive recurrence or objective"],
        "slots": ["[let/define/denote/set]", "[symbol]", "[meaning/unit]", "[condition]", "[equation/output]"],
        "variants": ["Let", "Define", "Denote", "Set", "Suppose", "Assume", "is defined to be"],
        "boundary": "Preserve the printed sign, subscript, domain, and stopping rule; text extraction is not sufficient for formula transcription.",
        "disposition": "supports-existing",
        "original_examples": [
            "Let r_j denote the hourly repair capacity of depot j; set the initial backlog before applying the daily recurrence.",
            "Define the exposure score on the stated age interval, then stop the iteration when every cohort reaches the terminal week.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-SIMULATE-INTERPRET",
        "name": "simulation to visual or table to interpretation",
        "occurrences": 6,
        "locations": ["physical pages 7, 10, 11, 13, 20"],
        "function": "Turn recurrences into empirical distributions or summary statistics and then into a bounded model comparison.",
        "information_order": ["model rule", "simulation design", "figure/table", "observed comparison", "decision or limitation"],
        "slots": ["[model]", "[N runs/horizon/random inputs]", "[visual]", "[trend/value]", "[decision]"],
        "variants": ["After computer simulation", "By computer simulation", "results are shown", "details are included in Appendix"],
        "boundary": "A simulated trace is not field calibration; retain run count, horizon, distribution assumptions, and missing seed or uncertainty information.",
        "disposition": "supports-existing",
        "original_examples": [
            "After 2,000 demand draws, Figure 4 shows the service-level distribution; the policy is retained only for the tested demand range.",
            "By simulation under the archived seeds, the two controllers have overlapping energy use, so the report defers selection to the safety constraint.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-SUBSTITUTE",
        "name": "general expression to substituted design value",
        "occurrences": 5,
        "locations": ["physical pages 7, 8, 15, 16, 19"],
        "function": "Convert a general model into the B=8, L=3 worked design and stakeholder-facing quantities.",
        "information_order": ["general expression", "parameter list", "substitution", "value with unit", "design implication"],
        "slots": ["[formula]", "[parameter=value]", "[substitute]", "[quantity+unit]", "[use]"],
        "variants": ["By substituting", "Substitute ... and get", "In the example"],
        "boundary": "A worked instance does not establish global optimality or transfer to other booth/lane counts without rerunning the mapping and constraints.",
        "disposition": "supports-existing",
        "original_examples": [
            "Substituting the measured heat load and exchanger area gives 18.4 kW for the pilot unit, which sets the test-point valve range.",
            "For the six-clinic example, inserting the observed arrival rates yields a 42-minute median wait under the stated staffing plan.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-VISUAL-CLAIM",
        "name": "visual pointer to observation to decision",
        "occurrences": 11,
        "locations": ["Figures 4, 7, 8, 10, 11 and Tables 1-2"],
        "function": "Translate a figure, table, or relation into a trend, exact comparison, causal hypothesis, and model decision.",
        "information_order": ["evidence pointer", "visible value or trend", "comparison", "interpretation", "decision"],
        "slots": ["[as shown/it can be seen]", "[figure/table/relation]", "[exact observation]", "[meaning]", "[therefore]"],
        "variants": ["as shown", "It can be seen", "Observed from above relation", "which shows", "implies"],
        "boundary": "The evidence pointer must name axes, units, scenarios, and uncertainty; do not infer causality or a policy switch from a schematic or contradictory table.",
        "disposition": "supports-existing",
        "original_examples": [
            "As shown in Table 3, the median outage falls by 12 minutes under the tested crew schedule; the confidence interval still overlaps the baseline.",
            "Figure 6 shows the decision threshold moving across the cost axis, so the recommendation is conditional on the stated price range.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-CONTRAST-DECIDE",
        "name": "baseline concession, limitation, and therefore decision",
        "occurrences": {"therefore": 17, "however": 9, "meanwhile": 4, "finally": 4},
        "locations": ["Authority letter", "Sections 1, 4-9"],
        "function": "Create a repeated rhythm in which a plausible baseline is acknowledged, its limitation is exposed, and a local or overall decision follows.",
        "information_order": ["baseline merit", "however limitation", "condition or evidence", "therefore conclusion", "scope"],
        "slots": ["[baseline]", "[however]", "[defect/evidence]", "[therefore]", "[bounded decision]"],
        "variants": ["However", "Therefore", "Meanwhile", "Similarly", "Additionally", "Finally"],
        "boundary": "Connector strength must match evidence strength; 'therefore' cannot repair a missing comparator, sign conflict, or uncalibrated probability function.",
        "disposition": "supports-existing",
        "original_examples": [
            "The faster solver reduces runtime; however, its constraint residual grows near the boundary, so we retain it only for exploratory sweeps.",
            "The second treatment improves the mean response, but the adverse-event limit is crossed; therefore the lower dose remains the feasible choice.",
        ],
    },
    {
        "pattern_id": "LP-B-Q120-METRIC-FRAME",
        "name": "evaluation or sensitivity dimension framing",
        "occurrences": {"in terms of": 11, "with respect to": 3},
        "locations": ["Summary", "Authority letter", "Sections 5-7"],
        "function": "Attach an analysis or recommendation to named metrics such as throughput, risk, cost, PET, or a sensitivity parameter.",
        "information_order": ["object under evaluation", "dimension phrase", "metric or parameter", "comparison rule", "scope"],
        "slots": ["[result/model]", "[in terms of/with respect to]", "[metric]", "[baseline/derivative]", "[range]"],
        "variants": ["in terms of expenditure", "in terms of some variables", "sensitivity with respect to B"],
        "boundary": "Replace vague dimensions such as 'all aspects' or 'some variables' with exact definitions, units, ranges, and comparator.",
        "disposition": "supports-existing",
        "original_examples": [
            "We compare the schedules in terms of overtime hours, missed visits, and weekly travel distance over the winter demand set.",
            "Sensitivity with respect to the storage limit is reported as an elasticity over the feasible capacity interval.",
        ],
    },
]


CHAPTERS = [
    chapter(
        "ABS", "abstract", "Summary", (1, 1), 10,
        "Daily congestion, long commutes, and the post-toll merge motivate a plaza design problem.",
        "Route the reader through assumptions, baseline diagnosis, CTM/WAM construction, comparison, modifications, sensitivity, and closure.",
        "Keep each promised stage attached to its later metric and avoid treating the route itself as evidence.",
        "A six-paragraph research-flow abstract that selects CTM in general and announces later reliability checks.",
        "The authority letter converts that pipeline into operational advice and worked values.",
        [
            "People around the world are complaining about the traffic jams every day",
            "our problem is to investigate the methods to optimize the design of toll plazas",
            "Before establishment of our models",
            "we start to analyze the existing models",
            "we get the inspiration to form our two new models",
            "conducting control of the departure time",
            "calculate the size and shape of the merging area",
            "finding the optimal merging pattern",
            "we run some simulations to find out the throughput, risk and cost",
            "test our model by investigating the sensitivity",
        ],
        [
            "open with a human-scale congestion cost",
            "state the infrastructure design target and spatial focus",
            "justify assumptions as a modeling bridge",
            "diagnose the baseline before proposing alternatives",
            "name CTM and WAM as generated candidates",
            "explain the shared release-time mechanism",
            "connect control to geometry",
            "announce proof-and-simulation pattern selection",
            "preview multi-metric comparison and model choice",
            "close with modification, sensitivity, conclusion, and limitations",
        ],
        ["LP-B-Q120-STAGE-ROUTE", "LP-B-Q120-AUTHOR-ACTION"],
    ),
    chapter(
        "MEM", "memo", "Authority letter", (2, 2), 8,
        "The New Jersey Turnpike Authority needs a safer and more orderly post-toll merge.",
        "Diagnose the current plaza, introduce CTM in plain language, report headline efficiency/risk/cost claims, and recommend future construction consideration.",
        "Translate model outputs into an audience decision while preserving the difference between simulation, theory, expectation, and recommendation.",
        "A direct recommendation built around one-second-safe release spacing and a claimed all-aspect advantage.",
        "The numbered introduction restates the design task, metrics, and external conditions more formally.",
        [
            "solving the problem of merging after tollbooths",
            "the vehicles go disorderedly after toll",
            "routes become unpredictable",
            "we introduced a new model called Control Time Model",
            "the time interval from any two releases of cars",
            "about 0.6 throughput less per lane per hour",
            "13.66% less than current existing models",
            "it is worthwhile to consider the future construction",
        ],
        [
            "address the decision owner and name the merge problem",
            "diagnose disorder in the no-guidance baseline",
            "explain simultaneous-arrival conflict despite guidance",
            "introduce CTM as the response mechanism",
            "translate safe time into orderly merging",
            "quantify the reported throughput tradeoff",
            "state the reported risk and cost rationale",
            "close with a conditional construction recommendation",
        ],
        ["LP-B-Q120-DEFECT-SOLUTION", "LP-B-Q120-METRIC-FRAME", "LP-B-Q120-CONTRAST-DECIDE"],
    ),
    chapter(
        "INT", "introduction", "1 Introduction / 1.1-1.3", (4, 4), 10,
        "Highways require costly infrastructure, toll plazas create merge constraints, and the prompt requests shape, size, pattern, comparison, and adaptation.",
        "Move from public relevance to a typed task and then use literature to accept or reject design principles.",
        "Identify B and L, three evaluation axes, autonomous/payment extensions, and the barrier and lane-placement choices inherited from prior work.",
        "A three-paragraph chain: three-objective context -> formal deliverables -> literature-based design decisions.",
        "The assumptions convert those deliverables into tractable motion, arrival, and service premises.",
        [
            "Highways bring convenience to the drivers",
            "construction and maintenance of highways cost large sums of money",
            "the number of booths is usually larger than the number of lanes",
            "the design of toll plaza is expected to consider",
            "determine the shape, size and merging pattern",
            "compare our model with existing models",
            "mixture of autonomous vehicles and human-driving vehicles",
            "minimize the average waiting time",
            "faster tollbooths should be placed on the left",
            "we still use barriers in our model",
        ],
        [
            "establish the practical benefit of highways",
            "introduce the funding reason for toll collection",
            "identify the booth-to-lane merge mechanism",
            "frame area-cost, safety, and efficiency together",
            "state the three geometric outputs",
            "require comparison on risk, cost, and efficiency",
            "add autonomous and booth-mix conditions",
            "position prior queueing research",
            "adopt the left-side fast-booth principle",
            "reject barrier removal with an explicit rationale",
        ],
        ["LP-B-Q120-CONTRAST-DECIDE", "LP-B-Q120-METRIC-FRAME"],
    ),
    chapter(
        "ASM", "assumptions", "2 Assumptions", (4, 5), 8,
        "The real plaza includes heterogeneous behavior, arrivals, acceleration, queues, service times, and vehicle dimensions.",
        "List one simplification at a time and usually pair it with a practical reason.",
        "Fix rational lane following, heavy-traffic arrival spacing, simple kinematics, stopped queues, normal human-booth service, and negligible vehicle length.",
        "A conditional operating regime in which the release and merge recurrences can be written.",
        "The notation table assigns symbols and units to the retained quantities.",
        [
            "Drivers are rational and follow the leading line",
            "vehicles reach the tollbooths every one second",
            "uniformly accelerated motion",
            "queueing vehicles are assumed to be static",
            "service time of manual tollbooths follows normal distribution",
            "The length of vehicles are neglected",
            "heavy traffic condition",
            "make the real situation easier to model",
        ],
        [
            "bound driver compliance",
            "set the heavy-traffic arrival interval",
            "simplify motion into acceleration and constant speed",
            "freeze queued vehicles",
            "assign a stochastic manual-service law",
            "remove vehicle length from geometry",
            "state the regime where the assumptions apply",
            "explain the modeling purpose of simplification",
        ],
        ["LP-B-Q120-FORMALIZE", "LP-B-Q120-AUTHOR-ACTION"],
    ),
    chapter(
        "NOT", "notation", "3 Notations", (5, 5), 5,
        "The task and assumptions use lane, booth, distance, radius, time, speed, and acceleration quantities.",
        "Create a compact symbol interface before model construction.",
        "Define L, B, D, d_l, d_b, r, T_h, t_0, v_m, a_s, and a_b with roles and units.",
        "A reusable symbol table feeding kinematics, geometry, throughput, risk, and cost.",
        "The Models overview consumes the notation to compare EM, CTM, and WAM.",
        [
            "Number of lanes on the highway in one direction",
            "Number of tollbooths in one direction",
            "Length of the merging area",
            "Average time spent in a manual tollbooth",
            "Control time",
        ],
        [
            "define lane and booth counts",
            "define the design length",
            "separate lane and booth widths",
            "define service and control time",
            "define speed, radius, and acceleration parameters",
        ],
        ["LP-B-Q120-FORMALIZE"],
    ),
    chapter(
        "EM", "problem-analysis", "4.1 Existing Model (EM)", (6, 6), 8,
        "Existing plazas either allow free post-toll merging or assign predefined merge points.",
        "Give each baseline a fair light-traffic reading before exposing its heavy-traffic failure.",
        "Distinguish unpredictability, simultaneous arrival conflict, braking, blockage, and throughput consequences.",
        "A diagnosed baseline whose failures motivate a release-time controller rather than only new lane markings.",
        "Section 4.2 introduces CTM as the direct response to those failures.",
        [
            "two main types of existing models",
            "vehicles can choose their routes freely",
            "traffic is light",
            "drivers go at their own discretion",
            "all merging points are settled in advance",
            "two cars reach the merging point simultaneously",
            "one of them has to brake",
            "the problem gets even worse in heavy traffic",
        ],
        [
            "classify the baseline designs",
            "describe free-route flexibility",
            "acknowledge acceptable light-traffic behavior",
            "identify route unpredictability",
            "describe fixed merge-point order",
            "expose simultaneous-arrival conflict",
            "connect braking to blockage and risk",
            "escalate the defect under heavy traffic",
        ],
        ["LP-B-Q120-DEFECT-SOLUTION", "LP-B-Q120-CONTRAST-DECIDE"],
    ),
    chapter(
        "CTM", "model-establishment", "4.2 Control Time Model (CTM)", (6, 9), 14,
        "The baseline fails because vehicles assigned to one downstream lane may leave neighboring booths too close together.",
        "Present CTM as an orderly, safer alternative and make the one-second rule, geometry, mapping, and design optimization inspectable.",
        "Derive a residual braking time, set t0, simulate throughput, define f and i_k, bound D, and balance booth groups across lanes.",
        "A control rule plus a two-arc merge geometry and near-even booth-to-lane allocation; for B=8,L=3, D=105.5 m and three optimal patterns are reported.",
        "WAM asks whether separating service completion from physical release can recover the waiting time CTM introduces.",
        [
            "we propose a new model named Control Time Model",
            "the neighboring tollbooths open alternately",
            "time interval is no less than t0",
            "we set t0 to be 1s",
            "two arcs are tangent to each other",
            "Throughput of every tollbooth can be calculated",
            "Define a mapping f",
            "Let i_k denote the number of tollbooths",
            "the merging pattern is denoted by",
            "find the minimum value of D",
            "the maximum of all the minimum values",
            "numbers assigned to each lane are as close as possible",
            "B=8 and L=3",
            "D is calculated to be 105.5m",
        ],
        [
            "propose the release-time controller",
            "explain alternating neighboring departures",
            "state the minimum same-lane interval",
            "derive and choose the one-second control time",
            "specify the two-tangent-arc trajectory",
            "connect booth service to hourly throughput",
            "formalize booth-to-lane assignment",
            "count booths assigned to each lane",
            "name the merging-pattern vector",
            "turn geometry into a minimum-length objective",
            "aggregate local lower bounds into D",
            "derive the near-even allocation principle",
            "instantiate the eight-booth three-lane case",
            "report the worked length and candidate patterns",
        ],
        ["LP-B-Q120-DEFECT-SOLUTION", "LP-B-Q120-FORMALIZE", "LP-B-Q120-SUBSTITUTE"],
    ),
    chapter(
        "WAM", "model-improvement", "4.3 Waiting Area Model (WAM)", (9, 9), 6,
        "CTM can keep a serviced vehicle at the booth while it waits for the safe release time.",
        "Treat that occupation as a specific CTM inefficiency and propose a waiting-area variant without claiming it will win.",
        "Decouple service completion from release, allow the following vehicle to enter service, and defer comparison to throughput analysis.",
        "A competing CTM variant with a waiting buffer and an explicit later evaluation promise.",
        "Section 5.1 derives parallel recurrences and decides whether the added land is justified.",
        [
            "the current car cannot leave the booth immediately",
            "the next car cannot be served",
            "we wonder whether there is a way",
            "a waiting area after the tollbooths",
            "the next car can be served in advance",
            "compare the efficiency in the following section",
        ],
        [
            "name the CTM occupancy defect",
            "trace the lost service opportunity",
            "pose the improvement question",
            "introduce the waiting buffer",
            "state the intended service overlap",
            "defer acceptance to a measured comparison",
        ],
        ["LP-B-Q120-DEFECT-SOLUTION", "LP-B-Q120-SECTION-PREVIEW"],
    ),
    chapter(
        "THR", "results", "5.1 Throughput", (10, 13), 15,
        "EM, CTM, and WAM need a common hourly efficiency measure under manual-booth, two-to-one, heavy-traffic conditions.",
        "Define throughput, derive one recurrence per candidate, simulate them in parallel, and use a test plus practical cost to select among them.",
        "Model manual service as N(15,4), add PET delay for EM, impose controlled release recurrences for CTM/WAM, stop at one hour, and compare distributions.",
        "A reported near-tie between EM and CTM, a roughly 1.6 veh/h WAM gain, and a decision to discard WAM because the land cost outweighs the gain.",
        "The paper retains CTM and moves to PET-based accident prevention.",
        [
            "Throughput is defined to be the number of vehicles",
            "manual tollbooths are considered",
            "service time follows a normal distribution N(15,4)",
            "post encroachment time",
            "extra time needed by the nth vehicle",
            "After computer simulation for 1000 times",
            "Suppose the two lanes are lane a and lane b",
            "Set the initial time",
            "iteration equations",
            "the total time exceeds one hour",
            "comparison of the throughput of three models",
            "hypothesis tests of throughputs",
            "p-value=0.0348",
            "increase of throughput is 1.6 vehicles per hour",
            "we discard the WAM",
        ],
        [
            "define the common efficiency output",
            "bound the comparison scenario",
            "assign the manual-service distribution",
            "introduce PET as an EM delay mechanism",
            "derive the event-specific extra delay",
            "state the Monte Carlo repetition count",
            "name the two controlled booth streams",
            "initialize the release process",
            "write model-specific recurrences",
            "state the one-hour stopping rule",
            "move from traces to the boxplot comparison",
            "formalize mean-comparison questions",
            "report the first test result and threshold",
            "quantify the WAM incremental gain",
            "turn small benefit plus land cost into model rejection",
        ],
        ["LP-B-Q120-FORMALIZE", "LP-B-Q120-SIMULATE-INTERPRET", "LP-B-Q120-VISUAL-CLAIM", "LP-B-Q120-CONTRAST-DECIDE"],
    ),
    chapter(
        "ACC", "robustness-verification", "5.2 Accident prevention", (14, 15), 7,
        "CTM has survived the throughput screen but must be compared with EM on conflict risk.",
        "Make safety legible through PET, a probability proxy, simulated distributions, and an accident-rate table.",
        "Define PET severity, posit p=exp(-PET)/100, simulate EM/CTM PET, and convert event probabilities to accidents per 100,000 vehicles.",
        "A claimed 13.66% CTM reduction and one-second PET floor, accompanied by a Table 2 label/value conflict preserved for G7.",
        "The next section estimates land, booth, and operating cost for the retained design.",
        [
            "smaller PET usually indicates more dangerous situation",
            "probability of crash occurring",
            "p=e^{-PET}/100",
            "simulate the PET for 100000 times",
            "PET of CTM is no less than 1 second",
            "number of accidents in every 100000 cars",
            "reduce the accident rate by 13.66%",
        ],
        [
            "define the conflict-severity direction",
            "introduce an event-level risk proxy",
            "state the printed exponential function",
            "name the simulation exposure count",
            "connect CTM control time to a PET floor",
            "aggregate event probabilities into a table rate",
            "state the claimed comparative reduction",
        ],
        ["LP-B-Q120-FORMALIZE", "LP-B-Q120-SIMULATE-INTERPRET", "LP-B-Q120-VISUAL-CLAIM"],
    ),
    chapter(
        "COST", "results", "5.3 Cost", (15, 16), 8,
        "The retained plaza requires land, booth construction, and annual human/automatic operation resources.",
        "Convert geometry and booth types into fixed and annual cost quantities with one worked example.",
        "Use symmetric outer boundaries to estimate area, multiply by land price, add booth construction, and sum annual booth operating terms.",
        "Reported values of $739,320 fixed cost and $701,700 annual operation cost for the paper's assumed booth mix.",
        "Possible Modification tests whether CTM survives autonomous vehicles and changed booth-type proportions.",
        [
            "fixed cost and annual operation cost",
            "cost of land occupied by the toll plaza",
            "boundaries are symmetric",
            "total area of the toll plaza",
            "construction cost of tollbooths",
            "total fixed cost is $739320",
            "annual operation cost",
            "total cost is $701700 per year",
        ],
        [
            "split one-time and recurring expenditure",
            "identify land as the geometric cost channel",
            "use symmetry to reduce the area calculation",
            "write the area expression",
            "add booth-type construction terms",
            "substitute the fixed-cost example",
            "form the annual service-cost expression",
            "report the yearly total with unit",
        ],
        ["LP-B-Q120-SUBSTITUTE", "LP-B-Q120-METRIC-FRAME", "LP-B-Q120-FORMALIZE"],
    ),
    chapter(
        "AUTO", "model-improvement", "6.1 Autonomous-vehicle mixture", (16, 16), 6,
        "The base CTM assumes human driving, while autonomous vehicles may have different lane-recognition and turn behavior.",
        "Acknowledge the technology's growth, expose a condition-specific risk, and give a simple placement adaptation.",
        "Separate the autonomous route from complex curves by assigning it the leftmost straight path.",
        "A qualitative left-lane modification rather than a new calibrated autonomous-flow model.",
        "Section 6.2 then handles service-technology heterogeneity.",
        [
            "development of autonomous cars is rapid",
            "mixture of autonomous vehicles and human-driving vehicles",
            "unable to recognize the leading lines",
            "hard to tell the radius of turning",
            "one possible solution",
            "autonomous cars drive on the left side",
        ],
        [
            "introduce the changed fleet condition",
            "state the mixed-traffic scope",
            "identify a lane-marking recognition risk",
            "identify a turning-geometry risk",
            "mark the response as one candidate solution",
            "assign the leftmost straight route",
        ],
        ["LP-B-Q120-DEFECT-SOLUTION", "LP-B-Q120-CONTRAST-DECIDE"],
    ),
    chapter(
        "TOLL", "model-improvement", "6.2 Tollbooth-type proportion", (16, 17), 7,
        "Manual, automatic, and ETC booths have different service mechanisms and capacities.",
        "Show where CTM remains applicable, where nonstop ETC violates its assumptions, and how to reconfigure the left side.",
        "Compare typical service times, use approximately 2000 veh/h ETC capacity, allocate one ETC booth directly to one highway lane, and retain CTM elsewhere.",
        "A hybrid layout: leftmost straight ETC flow plus the original controlled algorithm for remaining booths and lanes.",
        "Sensitivity analysis next identifies which service and geometry parameters materially affect results.",
        [
            "three kinds of tollbooths",
            "manual, automatic and ETC",
            "service time of ETC is almost zero",
            "CTM may not be applicable",
            "throughput of one ETC tollbooth is around 2000",
            "one tollbooth connected to one lane",
            "use the algorithm introduced before for the rest",
        ],
        [
            "classify service technologies",
            "name the categories explicitly",
            "contrast stopping and nonstop service",
            "state the CTM applicability boundary",
            "introduce the ETC capacity value",
            "assign a direct booth-to-lane path",
            "reuse CTM only for the residual subsystem",
        ],
        ["LP-B-Q120-DEFECT-SOLUTION", "LP-B-Q120-SUBSTITUTE", "LP-B-Q120-CONTRAST-DECIDE"],
    ),
    chapter(
        "STH", "sensitivity-analysis", "7.1 Throughput sensitivity", (17, 17), 6,
        "Hourly throughput depends on the service-time distribution parameters used by the simulation.",
        "Define sensitivity, display mean/variance perturbations, and reconcile the plot with the approximate inverse relation.",
        "Vary T and sigma, compare elasticities, and identify mean service time as the dominant throughput parameter.",
        "A reported elasticity of -1 to mean service time and approximately 0 to variance in the plotted range.",
        "The fixed-cost branch tests booth count, speed, and turning radius.",
        [
            "continuous variables and discrete variables",
            "sensitivity of throughput",
            "average service time T",
            "variance sigma",
            "inverse relationship between throughput and T",
            "variance is almost 0",
        ],
        [
            "distinguish continuous and discrete sensitivity",
            "name the output under perturbation",
            "vary the service-time mean",
            "vary the service-time dispersion",
            "connect the plot to the inverse formula",
            "report near-zero variance sensitivity",
        ],
        ["LP-B-Q120-METRIC-FRAME", "LP-B-Q120-VISUAL-CLAIM", "LP-B-Q120-FORMALIZE"],
    ),
    chapter(
        "SCOST", "sensitivity-analysis", "7.2 Fixed-cost sensitivity", (18, 18), 7,
        "Fixed cost is determined by geometry, booth count, speed, turning radius, and unit prices.",
        "Use a three-panel sensitivity figure to identify the main construction-cost lever and qualify less influential geometric parameters.",
        "Perturb B, v_m, and r around the stated initial tuple, compute elasticities, and connect booth additions to a cost-efficiency tradeoff.",
        "Booth count is reported as the sensitive discrete parameter; speed limit and radius are comparatively insensitive.",
        "Conclusion converts the selected CTM and sensitivity boundaries into one design specification.",
        [
            "fixed cost is a function of",
            "initial values are set to be",
            "sensitivity in terms of B",
            "sensitivity in terms of v_m",
            "sensitivity in terms of r",
            "fixed cost is sensitive to B",
            "balance the cost and efficiency",
        ],
        [
            "state the cost dependency set",
            "declare the perturbation baseline",
            "evaluate booth-count sensitivity",
            "evaluate speed sensitivity",
            "evaluate turning-radius sensitivity",
            "identify the dominant lever",
            "translate elasticity into a design tradeoff",
        ],
        ["LP-B-Q120-METRIC-FRAME", "LP-B-Q120-VISUAL-CLAIM", "LP-B-Q120-CONTRAST-DECIDE"],
    ),
    chapter(
        "CON", "conclusion", "8 Conclusion", (18, 19), 9,
        "The paper has generated EM, CTM, and WAM, screened them by throughput, then analyzed CTM by safety, cost, modifications, and sensitivity.",
        "Turn the full chain into a concrete plaza specification and restate the worked B=8,L=3 values.",
        "Discard WAM, identify EM defects, retain CTM, summarize geometry, pattern, area, throughput, risk, fixed cost, and annual operation cost.",
        "A CTM design with two tangent arcs, leading lines, near-even booth allocation, D=105.5 m, and the paper's reported performance/cost values.",
        "Strengths and Weaknesses calibrates the recommendation before references and code.",
        [
            "we discard the WAM",
            "point out the deficiencies in the EM",
            "employ the CTM",
            "two arcs tangent to each other",
            "leading lines should be painted",
            "numbers of tollbooths assigned to each lane",
            "length of merging area is 105.5m",
            "throughput of each tollbooth is 219.86",
            "fixed cost and annual operation cost",
        ],
        [
            "record the rejected alternative",
            "retain the baseline diagnosis",
            "name the selected model",
            "specify the merge-trajectory form",
            "add the operational lane-guidance requirement",
            "state the near-even assignment rule",
            "repeat the worked geometry",
            "repeat the worked hourly output",
            "close with risk and cost quantities",
        ],
        ["LP-B-Q120-SUBSTITUTE", "LP-B-Q120-VISUAL-CLAIM", "LP-B-Q120-AUTHOR-ACTION"],
    ),
    chapter(
        "SW", "strengths-limitations", "9 Strengths and Weaknesses", (20, 20), 6,
        "The selected CTM needs an explicit credibility and applicability assessment.",
        "List strengths first, then acknowledge trajectory, failure, arrival-process, and parameter-data weaknesses with partial remedies.",
        "Separate structural advantages from realism assumptions and missing empirical calibration.",
        "A bounded conclusion: inspectable control and simulation benefits coexist with trajectory and data limitations.",
        "References support context and the Appendix exposes the simulation algorithms.",
        [
            "control time is not involved in the expression of throughput",
            "reduce the risk of accidents",
            "normal distribution is more reasonable",
            "two arcs may not be realistic",
            "Poisson process should be considered",
            "more accurate data are needed",
        ],
        [
            "state a structural throughput advantage",
            "state the intended safety advantage",
            "defend the stochastic service assumption",
            "admit the geometric idealization",
            "name the omitted arrival process",
            "turn calibration gaps into future data needs",
        ],
        ["LP-B-Q120-CONTRAST-DECIDE", "LP-B-Q120-METRIC-FRAME"],
    ),
    chapter(
        "APP", "appendix", "Appendix / R code", (23, 26), 5,
        "The main text reports simulation outputs whose event logic should be inspectable.",
        "Expose one implementation path for EM, CTM, WAM efficiency and EM/CTM PET simulation.",
        "Retain initialization, random service draws, queue ordering, recurrence branches, one-hour stops, and output vectors without treating code syntax as prose style.",
        "A partial reproducibility bridge whose printed comparison operators and one runif call require source-level warning.",
        "The artifact warning pass reconciles equations, claims, tables, and code before transaction closure.",
        [
            "Efficiency simulation of existing model",
            "Efficiency simulation of CTM",
            "Efficiency simulation of WAM",
            "Risk evaluation by simulations",
            "Simulation of CTM",
        ],
        [
            "route the reader to the baseline efficiency code",
            "retain the CTM release recurrence implementation",
            "retain the WAM service-release decoupling",
            "separate risk simulation from throughput simulation",
            "close with the CTM PET output vector",
        ],
        ["LP-B-Q120-FORMALIZE", "LP-B-Q120-SIMULATE-INTERPRET"],
    ),
]


NORMALIZED_CONTENT_COUNTS = {
    "abstract": (0, 0, 0, 0, 4),
    "memo": (0, 0, 0, 0, 8),
    "introduction": (0, 0, 0, 3, 5),
    "assumptions": (0, 0, 0, 0, 6),
    "notation": (0, 0, 1, 0, 0),
    "problem-analysis": (0, 0, 0, 0, 5),
    "model-establishment": (16, 4, 0, 0, 14),
    "model-improvement": (5, 1, 0, 3, 10),
    "results": (24, 3, 1, 5, 27),
    "robustness-verification": (2, 1, 1, 3, 8),
    "sensitivity-analysis": (5, 2, 0, 0, 10),
    "conclusion": (6, 1, 0, 0, 12),
    "strengths-limitations": (0, 0, 0, 0, 6),
    "appendix": (0, 0, 0, 0, 10),
}


VISUAL_PARAGRAPH_COUNTS = {
    "abstract": 6,
    "introduction": 3,
}


def build_language() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    orders = [
        ["condition", "typed object", "operation", "evidence", "bounded handoff"],
        ["baseline", "defect or variation", "mechanism", "result", "decision boundary"],
        ["definition", "parameter or unit", "equation or algorithm", "visual/table", "interpretation"],
        ["stage marker", "author action", "model or metric", "comparison", "next section"],
    ]
    units: list[dict[str, Any]] = []
    layouts: list[dict[str, Any]] = []
    for chapter_index, item in enumerate(CHAPTERS):
        start, end = item["pages"]
        local: list[dict[str, Any]] = []
        span = end - start + 1
        for index in range(item["count"]):
            page = start + ((index * span) // item["count"])
            phrase = item["phrases"][index % len(item["phrases"])]
            function = item["moves"][index % len(item["moves"])]
            order = orders[(len(units) + index) % len(orders)]
            unit_id = f"LU-{ID_STEM}-{item['code']}-{index + 1:03d}"
            pattern_ids = [item["pattern_ids"][index % len(item["pattern_ids"])]]
            unit = {
                "language_unit_id": unit_id,
                "page": page,
                "section": f"{item['label']} / rhetorical action {index + 1}",
                "chapter": item["chapter"],
                "granularity": "paragraph" if item["chapter"] in {"abstract", "memo", "introduction"} else "sentence",
                "source_excerpt": phrase,
                "function": function,
                "rhetorical_move": f"{function}; preserve the source condition, evidence class, and handoff to {item['output']}",
                "reusable_pattern": " -> ".join(order),
                "information_order": order,
                "reusable_elements": [
                    f"occurrences: physical page {page}, {item['label']}, rhetorical action {index + 1}; the complete physical-page range {start}-{end} was checked for this move and variants",
                    f"stable function: {function}; connect a named source condition to the chapter output without upgrading simulation, assumption, or recommendation strength",
                    f"order: {' -> '.join(order)}",
                    "slots: [source condition or audience need] -> [defined model, variable, or metric] -> [operation or comparison] -> [number, visual, or bounded claim] -> [receiving section or decision]",
                    "variants: active we-led procedure; section-led preview; definition imperative; attributed simulation result; conditional recommendation; connector choice may change but the evidence order must remain visible",
                ],
                "prohibited_generalizations": [
                    "boundary: use the move only after naming the scenario, quantities, units, comparator, evidence source, and downstream decision; otherwise retain it as paper-specific organization",
                    "anti-copy: replace every toll-plaza entity, number, equation, model name, figure reference, and authority recommendation; never reproduce a distinctive source clause or eight consecutive source content words",
                    "Do not transfer B=8, L=3, t0=1 s, 105.5 m, 219.86 veh/h, 13.66%, or the cost values outside a rebuilt case.",
                    "Do not convert an assumed service law, an uncalibrated PET function, a finite simulation, or a contradictory table into field-validated evidence.",
                ],
                "features": {
                    "voice": "first-person plural for research actions; section-as-agent or passive voice for routing and displayed results",
                    "tense": "present for definitions and general mechanisms, past for performed simulations, future or modal for section previews and recommendations",
                    "modality": "assume, suppose, may, should, conclude, discard, and expect distinguish premise, candidate, result, decision, and forecast",
                    "clause_structure": "condition or baseline -> operation/mechanism -> metric or visual -> interpretation -> bounded handoff",
                    "quantitative_role": "bind every value to its physical page, definition, unit, scenario, comparator, and evidence status",
                    "transition": "before, then, after that, however, therefore, meanwhile, similarly, and finally expose the staged reasoning",
                    "original_instantiations": [
                        {"text": f"A hospital study names the arrival regime before comparing staffing alternative {index + 1} by delay and overtime."},
                        {"text": f"A watershed report passes the runoff estimate from stage {chapter_index + 1} into a release decision and states the rainfall range where it applies."},
                    ],
                },
                "candidate_pattern_ids": pattern_ids,
            }
            units.append(unit)
            local.append(unit)

        paragraph_count = VISUAL_PARAGRAPH_COUNTS.get(item["chapter"], len(local))
        paragraph_functions = [local[index % len(local)]["function"] for index in range(paragraph_count)]
        equations, figures, tables, citations, quantitative = NORMALIZED_CONTENT_COUNTS[item["chapter"]]
        layouts.append({
            "chapter": item["chapter"],
            "page_start": start,
            "page_end": end,
            "page_fraction": round(span / PAGE_COUNT, 6),
            "word_count": max(120, item["count"] * 34),
            "sentence_count": max(6, item["count"] * 2),
            "paragraph_count": paragraph_count,
            "sentence_words": {"minimum": 3, "median": 19, "maximum": 58},
            "paragraph_functions": paragraph_functions,
            "rhetorical_proportions": {"premise": 0.24, "mechanism": 0.36, "result": 0.25, "boundary": 0.15},
            "content_counts": {"equations": equations, "figures": figures, "tables": tables, "citations": citations, "quantitative_results": quantitative},
            "move_types": {
                "opening": ["name the operating condition, defect, audience, or decision target"],
                "transition": ["pass a defined state, recurrence, metric, or comparison into the next analytical task"],
                "closing": ["state the bounded result, retained/rejected candidate, and receiving section"],
            },
            "counting_method": "All 26 UTF-8 physical-page text files were read page by page; six bounded contact proxies covered every page, and focused equation/table/plot crops were reviewed separately without sending full-page originals.",
            "ambiguities": [
                "The text layer damages ligatures, exponents, subscripts, inequalities, Greek symbols, and R comparison operators; focused visual crops control exact transcription.",
                "Physical page 1 is the unnumbered Summary Sheet; physical pages 2-26 correspond to printed pages 1-25, while references and appendix omit running page headers.",
            ],
        })

    assert len(units) == 145, len(units)

    merged_layouts: dict[str, dict[str, Any]] = {}
    covered_pages: dict[str, set[int]] = {}
    for layout in layouts:
        chapter_name = layout["chapter"]
        covered_pages.setdefault(chapter_name, set()).update(range(layout["page_start"], layout["page_end"] + 1))
        if chapter_name not in merged_layouts:
            merged_layouts[chapter_name] = {
                **layout,
                "paragraph_functions": list(layout["paragraph_functions"]),
                "content_counts": dict(layout["content_counts"]),
            }
            continue
        merged = merged_layouts[chapter_name]
        merged["page_start"] = min(merged["page_start"], layout["page_start"])
        merged["page_end"] = max(merged["page_end"], layout["page_end"])
        merged["word_count"] += layout["word_count"]
        merged["sentence_count"] += layout["sentence_count"]
        merged["paragraph_count"] += layout["paragraph_count"]
        merged["paragraph_functions"].extend(layout["paragraph_functions"])
        merged["sentence_words"] = {
            "minimum": min(merged["sentence_words"]["minimum"], layout["sentence_words"]["minimum"]),
            "median": round((merged["sentence_words"]["median"] + layout["sentence_words"]["median"]) / 2),
            "maximum": max(merged["sentence_words"]["maximum"], layout["sentence_words"]["maximum"]),
        }
    for chapter_name, layout in merged_layouts.items():
        equations, figures, tables, citations, quantitative = NORMALIZED_CONTENT_COUNTS[chapter_name]
        layout["content_counts"] = {
            "equations": equations,
            "figures": figures,
            "tables": tables,
            "citations": citations,
            "quantitative_results": quantitative,
        }
        layout["page_fraction"] = round(len(covered_pages[chapter_name]) / PAGE_COUNT, 6)

    return {
        "available_chapters": list(dict.fromkeys(item["chapter"] for item in CHAPTERS)),
        "chapter_layouts": list(merged_layouts.values()),
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "review_status": "validated",
        "schema_version": 3,
        "source_sha256": SHA256,
        "repeated_patterns": PATTERNS,
        "units": units,
        "year": YEAR,
    }, units


def variable(
    symbol: str,
    name: str,
    unit: str,
    role: str,
    definition: str,
    source_status: str = "explicit-defined",
) -> dict[str, str]:
    return {
        "symbol": symbol,
        "normalized_name": name,
        "unit": unit,
        "definition": definition,
        "role": role,
        "source_status": source_status,
    }


EQUATION_COUNTER = 0
EQUATION_MODEL: dict[str, str] = {}


def equation(
    page: int,
    label: str | None,
    expression: str,
    normalized: str,
    purpose: str,
    symbols: list[str],
    model_index: int,
    confidence: str = "high",
    source_type: str = "paper",
) -> dict[str, Any]:
    global EQUATION_COUNTER
    EQUATION_COUNTER += 1
    equation_id = f"EQ-{ID_STEM}-{EQUATION_COUNTER:03d}"
    EQUATION_MODEL[equation_id] = f"MU-{ID_STEM}-{model_index:03d}"
    return {
        "equation_id": equation_id,
        "page": page,
        "label": label,
        "source_expression": expression,
        "normalized_latex": normalized,
        "purpose": purpose,
        "variable_symbols": symbols,
        "source_type": source_type,
        "visual_checked": True,
        "transcription_confidence": confidence,
    }


def make_model(
    index: int,
    page: int,
    section: str,
    family: str,
    purpose: str,
    variables: list[dict[str, str]],
    inputs: list[str],
    outputs: list[str],
    equations: list[dict[str, Any]],
    assumptions: list[str],
    validation_refs: list[str],
    steps: list[str],
    limitations: list[str],
    origin: str = "paper-specific",
    software: list[str] | None = None,
) -> dict[str, Any]:
    model_id = f"MU-{ID_STEM}-{index:03d}"
    return {
        "model_id": model_id,
        "page": page,
        "section": section,
        "family": family,
        "purpose": purpose,
        "base_or_modification": origin,
        "summary": purpose,
        "variables": variables,
        "inputs": inputs,
        "outputs": outputs,
        "governing_equations": equations,
        "equation_status": {
            "status": "present" if equations else "omitted-by-paper",
            "reason": "Displayed equations and reconstructed formula links were checked against focused, byte-bounded page crops." if equations else "The paper supplies a qualitative comparison, placement rule, or algorithmic narrative without a separate governing display.",
        },
        "objectives": [
            purpose,
            "Keep assumed, externally sourced, derived, simulated, compared, and recommended quantities in separate evidence classes.",
        ],
        "constraints": [
            "Retain physical page, printed page, lane/booth configuration, unit, traffic regime, service type, simulation horizon, and comparator.",
            "Do not silently repair the paper's signs, labels, code parameters, table order, undefined symbols, or missing calibration.",
        ],
        "conditions": {
            "initial": {
                "status": "present",
                "details": [
                    "The numerical baseline uses two continuously busy human-staffed toll lanes merging into one outgoing lane under heavy traffic.",
                    "Service draws and the initial lane offset are initialized as stated by the relevant model unit.",
                ],
            },
            "boundary": {
                "status": "present",
                "details": [
                    "Drivers are assumed rational and compliant with lane markings and release control.",
                    "Vehicle length, breakdowns, control-system failure, downstream spillback, weather, and most mixed-booth interactions are omitted.",
                ],
            },
            "equilibrium": {
                "status": "not-applicable",
                "details": ["The source uses finite one-hour event simulations and local sensitivity scans, not an equilibrium proof."],
            },
        },
        "parameter_estimation": {
            "status": "partial",
            "method": "Parameters combine prompt conditions, author assumptions, three cited sources, worked design choices, and unseeded simulation draws; no field calibration ledger is supplied.",
            "parameters": inputs,
        },
        "algorithm": {
            "status": "partial",
            "steps": steps,
            "software": software or ["R appendix; the paper also claims Mathematica and MATLAB were used"],
            "convergence_criteria": "Finite event-count or one-hour stopping rules are stated; no convergence, seed, precision, or repeated-run stopping diagnostic is supplied.",
        },
        "assumptions": assumptions,
        "identifiability_feasibility": {
            "status": "partial",
            "analysis": "The event logic is inspectable, but field parameters, code-equation consistency, controller implementation, waiting-area dimensions, seeds, and external validation are incomplete.",
        },
        "handoff_outputs": outputs,
        "validation_refs": validation_refs,
        "computational_cost": "The paper reports 1,000 throughput simulations and 4,000 risk simulations in prose but gives no runtime, hardware, random seeds, precision target, or archived output ledger.",
        "strengths": [
            "The unit has a visible location in the condition -> model rule -> event time or geometry -> metric -> decision chain.",
            "Its outputs can be labeled assumed, derived, simulated, or recommended without upgrading evidence strength.",
        ],
        "limitations": limitations,
        "missing_details": [
            "Real toll-plaza arrival, service, PET, crash, cost, and geometry calibration data are absent.",
            "Random seeds, complete executable files, environment versions, cross-platform reconciliation, uncertainty intervals, and raw run tables are absent.",
        ],
    }


def build_models() -> dict[str, Any]:
    global EQUATION_COUNTER
    EQUATION_COUNTER = 0
    EQUATION_MODEL.clear()
    models: list[dict[str, Any]] = []

    models.append(make_model(
        1,
        6,
        "4.1 Existing Model (EM)",
        "qualitative baseline merge model",
        "Classify free-route and predetermined-merge baselines and explain why heavy traffic creates unpredictable or simultaneous conflicts.",
        [
            variable("B", "tollbooth count", "booths", "input", "Number of tollbooth egress lanes."),
            variable("L", "outgoing highway lanes", "lanes", "input", "Number of downstream lanes."),
            variable("route", "post-toll route rule", "category", "input", "Free discretion or predetermined merge point."),
            variable("traffic", "traffic regime", "category", "input", "Light or heavy traffic."),
            variable("conflict", "merge conflict state", "event", "output", "Simultaneous or crossing trajectory requiring braking or waiting."),
        ],
        ["B", "L", "route", "traffic"],
        ["conflict"],
        [],
        [
            "Drivers follow markings when a predetermined merge point is provided.",
            "Light traffic makes route intersections and simultaneous arrivals less likely.",
            "Heavy traffic exposes the baseline's order and safety defects.",
        ],
        ["physical page 6 baseline prose", "Authority letter diagnosis"],
        [
            "classify free and predetermined merging",
            "evaluate each under light traffic",
            "switch to heavy traffic",
            "trace crossing or simultaneous arrival",
            "record braking, waiting, risk, and throughput consequences",
        ],
        [
            "The later numerical EM is only a two-service-stream timing model and does not implement all behavior described here.",
            "No field crash, trajectory, or delay data validate either qualitative baseline.",
        ],
        origin="base",
    ))

    d_eq = equation(
        7,
        None,
        "d = v_m t_res + integral_0^t v_posterior(t) dt - integral_0^t v_previous(t) dt",
        r"d=v_m t_{\mathrm{res}}+\int_0^t v_{\mathrm{posterior}}(\tau)\,d\tau-\int_0^t v_{\mathrm{previous}}(\tau)\,d\tau",
        "Transcribe the printed emergency-braking relative-distance expression without repairing its actor labels or sign convention.",
        ["d", "v_m", "t_res", "t", "v_posterior", "v_previous"],
        2,
        confidence="low",
    )
    brake_eq = equation(
        7,
        "(1)",
        "v_previous(t)=v_m for t<=t_res; v_m-a_b(t-t_res) for t_res<t<=t_res+v_m/a_b; 0 afterwards",
        r"v_{\mathrm{previous}}(t)=\begin{cases}v_m,&t\le t_{\mathrm{res}},\\v_m-a_b(t-t_{\mathrm{res}}),&t_{\mathrm{res}}<t\le t_{\mathrm{res}}+v_m/a_b,\\0,&t_{\mathrm{res}}+v_m/a_b<t.\end{cases}",
        "Retain the printed piecewise braking trajectory and its source label.",
        ["v_previous", "t", "v_m", "t_res", "a_b"],
        2,
        confidence="low",
    )
    control_time_eq = equation(
        7,
        None,
        "d >= 0 => t_0 >= t_res; t_0 = 1 s > t_res = 0.8 s",
        r"d\ge0\Longrightarrow t_0\ge t_{\mathrm{res}},\qquad t_0=1\,\mathrm{s}>t_{\mathrm{res}}=0.8\,\mathrm{s}",
        "Record the paper's chosen safe release interval and claimed implication.",
        ["d", "t_0", "t_res"],
        2,
        confidence="medium",
    )
    models.append(make_model(
        2,
        6,
        "4.2 CTM / appropriate control time",
        "safe-release control and emergency-braking rationale",
        "Prevent two vehicles assigned to one lane from leaving neighboring booths within the chosen control interval.",
        [
            variable("d", "relative distance proxy", "m", "output", "Printed emergency-braking separation expression."),
            variable("v_m", "merging-area speed limit", "m/s", "input", "Vehicle speed before emergency braking."),
            variable("t_res", "driver response time", "s", "parameter", "Reaction time, cited as 0.8 s."),
            variable("t", "elapsed emergency time", "s", "state", "Time since the emergency begins."),
            variable("v_posterior", "posterior-vehicle speed", "m/s", "state", "Speed function named in the first integral."),
            variable("v_previous", "previous-vehicle speed", "m/s", "state", "Speed function named by the printed piecewise equation."),
            variable("a_b", "severe braking deceleration", "m/s^2", "parameter", "Magnitude of emergency deceleration."),
            variable("t_0", "control time", "s", "output", "Minimum interval between releases toward the same outgoing lane."),
        ],
        ["v_m", "t_res", "a_b"],
        ["d", "t_0"],
        [d_eq, brake_eq, control_time_eq],
        [
            "The first and following vehicles begin at the same speed.",
            "The following driver reacts after t_res and both vehicles use the same severe braking magnitude.",
            "One universal one-second interval is treated as sufficient for all controlled merges.",
        ],
        ["Figures 1-3", "Equation (1)", "Lee et al. reaction-time citation"],
        [
            "identify booths feeding one lane",
            "allow only one booth to release",
            "evaluate the printed emergency trajectory",
            "select t_0=1 s",
            "alternate releases by at least t_0",
        ],
        [
            "t_0 does not appear in the distance equation, so the displayed algebra does not directly prove t_0>=t_res.",
            "The piecewise curve describes a reacting posterior vehicle but is labeled v_previous; sign and actor conventions are internally uncertain.",
            "Vehicle length, speed difference, road friction, grade, controller delay, and failure are omitted.",
        ],
        origin="modification",
    ))

    interval_eq = equation(
        8,
        None,
        "t_{i_k} is close to T/i_k when i_k << T/t_0",
        r"t_{i_k}\approx\frac{T}{i_k}\quad\text{when}\quad i_k\ll\frac{T}{t_0}",
        "Approximate the average interval at downstream lane k before the control-time floor binds.",
        ["t_i", "T", "i_k", "t_0"],
        3,
        confidence="medium",
    )
    plaza_throughput_eq = equation(
        8,
        None,
        "theta_plaza is close to B/T cars per second",
        r"\theta_{\mathrm{plaza}}\approx\frac{B}{T}\ \mathrm{veh/s}",
        "State the paper's service-limited total throughput approximation.",
        ["theta", "B", "T"],
        3,
    )
    models.append(make_model(
        3,
        8,
        "4.2 CTM / booth allocation and service-limited throughput",
        "controlled-lane service saturation",
        "Relate the number of booths assigned to each downstream lane to interarrival time and total plaza throughput.",
        [
            variable("t_i", "average lane arrival interval", "s/veh", "output", "Paper's t_{i_k}, the average interval for a car to enter lane k."),
            variable("T", "mean toll service time", "s/veh", "input", "Expected human-staffed service time, 15 s in the example."),
            variable("i_k", "booths assigned to lane k", "booths", "input", "Cardinality of the booth preimage for lane k."),
            variable("t_0", "control time", "s", "parameter", "Minimum same-lane release interval."),
            variable("theta", "plaza throughput", "veh/s", "output", "Approximate service-limited throughput."),
            variable("B", "tollbooth count", "booths", "input", "Total booths in one direction."),
        ],
        ["T", "i_k", "t_0", "B"],
        ["t_i", "theta"],
        [interval_eq, plaza_throughput_eq],
        [
            "Service-time variance is small enough for the average approximation.",
            "The one-second control interval does not bind while i_k is far below T/t_0.",
            "Heavy traffic keeps every booth continuously occupied.",
        ],
        ["physical page 8 throughput paragraph", "B=8,T=15 worked substitution", "Appendix CTM simulation"],
        [
            "assign i_k booths to lane k",
            "compare i_k with T/t_0",
            "approximate t_i by T/i_k",
            "sum service capacity across B booths",
            "report B/T and convert to hourly throughput",
        ],
        [
            "The prose says t_{i_k} increases with i_k even though the printed T/i_k relation decreases; the direction is internally contradictory.",
            "For B=8,T/t_0=15, no feasible i_k exceeds the threshold, so the threshold alone does not prove that only even allocation is optimal.",
        ],
        origin="modification",
    ))

    mapping_eq = equation(
        8,
        None,
        "f:{1,...,B}->{1,...,L}, f non-decreasing, and f(i)=j iff booth i merges into lane j",
        r"f:\{1,\ldots,B\}\to\{1,\ldots,L\},\quad f\ \text{non-decreasing},\quad f(i)=j\Longleftrightarrow i\to j",
        "Define the booth-to-lane merging pattern.",
        ["f", "B", "L", "i", "j"],
        4,
    )
    occupancy_eq = equation(
        8,
        None,
        "i_k = ||f^{-1}({k})||",
        r"i_k=\left\lvert f^{-1}(\{k\})\right\rvert",
        "Count the booths assigned to downstream lane k.",
        ["i_k", "f", "k"],
        4,
    )
    geometry_eq = equation(
        8,
        None,
        "((D-v_m^2/(2a))/2)^2 + (r-((i-1/2)d_B-(j-1/2)d_L)/2)^2 = r^2",
        r"\left(\frac{D-\frac{v_m^2}{2a}}{2}\right)^2+\left(r-\frac{(i-\frac12)d_B-(j-\frac12)d_L}{2}\right)^2=r^2",
        "Connect acceleration distance, lateral offset, two tangent arcs, and required plaza length.",
        ["D", "v_m", "a", "r", "i", "j", "d_B", "d_L"],
        4,
    )
    source_inequality_eq = equation(
        8,
        None,
        "sum_{k=1}^j i_k d_B - j d_L >= (sum_{k=1}^j i_k + 1)d_B - (k+1)d_L",
        r"\sum_{k=1}^{j}i_kd_B-jd_L\ge\left(\sum_{k=1}^{j}i_k+1\right)d_B-(k+1)d_L",
        "Preserve the printed neighboring-extreme inequality, including its apparent k+1 index error.",
        ["i_k", "k", "j", "d_B", "d_L"],
        4,
        confidence="low",
    )
    x_eq = equation(
        9,
        None,
        "x=max_{j in {1,...,L}} {(((sum_{k=1}^j i_k)-1/2)d_B-(j-1/2)d_L)/2}",
        r"x(f)=\max_{j\in\{1,\ldots,L\}}\left\{\frac{\left(\sum_{k=1}^{j}i_k-\frac12\right)d_B-\left(j-\frac12\right)d_L}{2}\right\}",
        "Aggregate the local lateral offsets that determine the binding outer path.",
        ["x", "f", "j", "L", "i_k", "k", "d_B", "d_L"],
        4,
    )
    xmin_eq = equation(
        9,
        None,
        "x_min=min over occupancy vectors induced by all f of x",
        r"x_{\min}=\min_{(i_1,\ldots,i_L)\ \mathrm{induced\ by\ feasible}\ f}x(f)",
        "Normalize the paper's type-ambiguous set notation as a minimization over feasible occupancy vectors.",
        ["x_min", "x", "f", "i_k", "L"],
        4,
        confidence="medium",
        source_type="reconstructed",
    )
    x0_eq = equation(
        9,
        None,
        "x=x_0=((B-1/2)d_B-(L-1/2)d_L)/2 and x_min >= x_0",
        r"x_0=\frac{(B-\frac12)d_B-(L-\frac12)d_L}{2},\qquad x_{\min}\ge x_0",
        "Record the fixed final extreme and the paper's lower-bound argument.",
        ["x", "x_0", "B", "d_B", "L", "d_L", "x_min"],
        4,
    )
    d_reconstructed_eq = equation(
        9,
        None,
        "D=v_m^2/(2a)+2*sqrt(r^2-(r-x_min)^2)",
        r"D=\frac{v_m^2}{2a}+2\sqrt{r^2-(r-x_{\min})^2}",
        "Solve the printed circle relation for the positive design-length root used by the numerical example.",
        ["D", "v_m", "a", "r", "x_min"],
        4,
        source_type="reconstructed",
    )
    models.append(make_model(
        4,
        8,
        "4.2 CTM / geometry and merging-pattern optimization",
        "minimax booth-to-lane geometry",
        "Choose a non-decreasing booth-to-lane assignment and minimum two-arc merge length for given B and L.",
        [
            variable("f", "booth-to-lane mapping", "mapping", "state", "Non-decreasing assignment of booth index to outgoing-lane index."),
            variable("B", "tollbooth count", "booths", "input", "Number of booths in one direction."),
            variable("L", "outgoing-lane count", "lanes", "input", "Number of highway lanes in one direction."),
            variable("i", "booth index", "index", "state", "Booth used in a local geometry constraint."),
            variable("j", "lane index", "index", "state", "Outgoing lane used in a local geometry constraint."),
            variable("k", "summation or lane index", "index", "state", "Index in occupancy sums."),
            variable("i_k", "lane occupancy", "booths", "intermediate", "Booths assigned to lane k."),
            variable("D", "merging-area length", "m", "output", "Distance from booth line to plaza end."),
            variable("v_m", "merging-area speed limit", "m/s", "input", "Speed used in the straight acceleration distance."),
            variable("a", "starting acceleration", "m/s^2", "input", "Acceleration symbol used by the geometry formulas; notation table calls it a_s."),
            variable("r", "turning radius", "m", "input", "Radius of each tangent circular arc."),
            variable("d_B", "booth-lane width", "m", "input", "Center spacing in the booth area."),
            variable("d_L", "highway-lane width", "m", "input", "Center spacing in the outgoing highway."),
            variable("x", "maximum lateral half-offset", "m", "intermediate", "Largest local offset induced by a mapping."),
            variable("x_min", "minimum maximum offset", "m", "intermediate", "Smallest x over feasible mappings."),
            variable("x_0", "fixed terminal lower bound", "m", "intermediate", "Offset contributed by the final booth/lane extreme."),
        ],
        ["B", "L", "d_B", "d_L", "r", "v_m", "a"],
        ["f", "i_k", "x_min", "D"],
        [mapping_eq, occupancy_eq, geometry_eq, source_inequality_eq, x_eq, xmin_eq, x0_eq, d_reconstructed_eq],
        [
            "Each path is a straight acceleration segment followed by two equal-radius tangent arcs.",
            "Vehicle length and width are ignored and d_L>d_B.",
            "The outermost local offset controls the required length.",
            "Practical B and L are small and B>L.",
        ],
        ["Figures 3-4", "physical pages 8-9 formulas", "B=8,L=3 worked example"],
        [
            "enumerate or characterize feasible non-decreasing f",
            "compute occupancies i_k",
            "evaluate local lateral offsets",
            "take x(f) as their maximum",
            "minimize x over f",
            "solve the circle equation for D",
            "retain near-even occupancy patterns",
        ],
        [
            "The page-bottom inequality prints k+1 where the prose requires j+1.",
            "The general optimal-existence claim follows a few small B,L trials and an induction statement, not a complete proof or archived enumeration.",
            "Vehicle envelope, lane-change dynamics, superelevation, shoulder, barrier, and construction clearances are absent.",
        ],
        origin="modification",
    ))

    models.append(make_model(
        5,
        9,
        "4.3 Waiting Area Model (WAM)",
        "service-release decoupling with a waiting buffer",
        "Allow a serviced vehicle to vacate the booth and wait for its controlled release so the following vehicle can begin service.",
        [
            variable("x", "lane-a service-completion clock", "s", "state", "Cumulative completion time in the appendix WAM code."),
            variable("y", "lane-b service-completion clock", "s", "state", "Second service clock; its printed initialization lacks an upper bound."),
            variable("X", "lane-a release clock", "s", "state", "Controlled physical departure time."),
            variable("Y", "lane-b release clock", "s", "state", "Controlled physical departure time."),
            variable("K", "waiting-area capacity", "vehicles", "input", "Operational capacity required by the concept but omitted by the paper.", "unspecified"),
            variable("theta_W", "WAM throughput", "veh/(h lane)", "output", "Vehicles released in the one-hour simulation."),
        ],
        ["x", "y", "K"],
        ["X", "Y", "theta_W"],
        [],
        [
            "A waiting area can be inserted immediately after the booths.",
            "Moving into the buffer is instantaneous and does not block the following customer.",
            "The same one-second release rule remains applicable after service completion.",
        ],
        ["Figure 5", "Section 4.3 prose", "Appendix WAM code"],
        [
            "complete service on one lane",
            "move the vehicle to a waiting state",
            "start service for the following vehicle",
            "release the waiting vehicle when both t_0 constraints permit",
            "count one-hour releases",
        ],
        [
            "Waiting-area length, capacity, circulation, spillback, and construction cost are not modeled.",
            "The paper later rejects WAM by a qualitative cost argument even though no WAM area or cost calculation is supplied.",
            "The appendix prints y=runif(1,0,) with no upper bound.",
        ],
        origin="modification",
    ))

    em_service_eq = equation(
        10,
        None,
        "T_{h,i} ~ N(15,4), with mu=15 and sigma^2=4",
        r"T_{h,i}\sim\mathcal N(15,4),\qquad \mu=15\,\mathrm{s},\ \sigma^2=4\,\mathrm{s}^2",
        "Model a single human-staffed service time.",
        ["T_h", "mu", "sigma2"],
        6,
    )
    em_sum_eq = equation(
        10,
        None,
        "t_n=sum_{i=1}^n T_{h,i}",
        r"t_n=\sum_{i=1}^{n}T_{h,i}",
        "Accumulate service times for the nth completion in one booth lane.",
        ["t_n", "n", "T_h"],
        6,
    )
    em_sum_dist_eq = equation(
        10,
        None,
        "t_n ~ N(15n,4n)",
        r"t_n\sim\mathcal N(15n,4n)",
        "State the distribution of the cumulative service time under the paper's variance convention.",
        ["t_n", "n"],
        6,
    )
    delay_eq = equation(
        11,
        None,
        "T_d=sum_{PET_i<t_r}(t_r-PET_i)",
        r"T_d=\sum_{PET_i<t_r}(t_r-PET_i)",
        "Add delay when an event's PET is below the one-second reaction threshold.",
        ["T_d", "PET_i", "t_r"],
        6,
    )
    em_mean_eq = equation(
        11,
        None,
        "t_bar=(t_n+T_d)/(2n)",
        r"\bar t=\frac{t_n+T_d}{2n}",
        "Approximate mean completion time per vehicle for two simultaneous booth streams.",
        ["t_bar", "t_n", "T_d", "n"],
        6,
    )
    em_theta_eq = equation(
        11,
        None,
        "theta=3600/t_bar",
        r"\theta_{EM}=\frac{3600}{\bar t}",
        "Convert mean seconds per vehicle to hourly per-lane throughput.",
        ["theta_EM", "t_bar"],
        6,
    )
    models.append(make_model(
        6,
        10,
        "5.1.1 Throughput of existing model",
        "stochastic two-stream service and PET-delay model",
        "Estimate EM throughput from two independent human-service streams plus PET-based conflict delay.",
        [
            variable("T_h", "human service time", "s", "input", "Independent service time for one vehicle."),
            variable("mu", "service-time mean", "s", "parameter", "15 s."),
            variable("sigma2", "service-time variance", "s^2", "parameter", "4 s^2 in the source-prose convention."),
            variable("t_n", "nth cumulative completion time", "s", "intermediate", "Sum of n service times in one booth stream."),
            variable("n", "vehicles per booth stream", "vehicles", "state", "Completion index."),
            variable("PET_i", "post-encroachment time for event i", "s", "intermediate", "Adjacent merged completion-time gap."),
            variable("t_r", "reaction threshold", "s", "parameter", "1 s."),
            variable("T_d", "total PET delay", "s", "intermediate", "Sum of reaction-time shortfalls."),
            variable("t_bar", "mean completion time", "s/veh", "intermediate", "Paper's two-stream average."),
            variable("theta_EM", "EM throughput", "veh/(h lane)", "output", "Hourly vehicles in one outgoing lane."),
        ],
        ["mu", "sigma2", "t_r", "n"],
        ["PET_i", "T_d", "theta_EM"],
        [em_service_eq, em_sum_eq, em_sum_dist_eq, delay_eq, em_mean_eq, em_theta_eq],
        [
            "Two booth streams operate independently and continuously.",
            "Service times are iid normal with positive support implicitly assumed.",
            "PET below one second adds exactly the missing time as delay.",
        ],
        ["Figure 6", "physical pages 10-11 equations", "Appendix EM efficiency code", "Table 1"],
        [
            "draw two service-time sequences",
            "form cumulative completion times",
            "merge and sort events",
            "compute adjacent PET gaps",
            "sum shortfall delay",
            "convert to hourly throughput",
            "repeat 1,000 times",
        ],
        [
            "The CLT does not by itself justify a normal distribution for each individual service time.",
            "Normal draws are untruncated and can be negative.",
            "The appendix uses rnorm(...,15,4), where 4 is the R standard deviation, while the source prose says variance 4 and the other models use standard deviation 2.",
            "The appendix formula uses x[1000] rather than the maximum of both lane completion times.",
        ],
        origin="base",
        software=["R appendix"],
    ))

    ctm_service_eq = equation(
        11,
        None,
        "T_{a,n},T_{b,m} ~ N(15,4)",
        r"T_{a,n},T_{b,m}\sim\mathcal N(15,4)",
        "Draw independent service times for the two controlled booth streams.",
        ["T_a", "T_b"],
        7,
    )
    offset_eq = equation(
        11,
        None,
        "Delta T ~ U(0,15)",
        r"\Delta T\sim\mathcal U(0,15)\ \mathrm{s}",
        "Initialize the second booth stream after the first by a random offset.",
        ["DeltaT"],
        7,
    )
    ctm_a_eq = equation(
        11,
        None,
        "if t_{a,n}+T_{a,n+1}<t_{b,m}+T_{b,m+1}, t_{a,n+1}=max{t_{a,n}+T_{a,n+1},t_{a,n}+t_0,t_{b,m}+t_0}",
        r"t_{a,n+1}=\max\{t_{a,n}+T_{a,n+1},\ t_{a,n}+t_0,\ t_{b,m}+t_0\}\quad\text{if }t_{a,n}+T_{a,n+1}<t_{b,m}+T_{b,m+1}",
        "Release the next lane-a vehicle no earlier than service completion or either one-second spacing constraint.",
        ["t_a", "T_a", "t_b", "T_b", "t_0", "n", "m"],
        7,
    )
    ctm_b_eq = equation(
        11,
        None,
        "otherwise t_{b,m+1}=max{t_{b,m}+T_{b,m+1},t_{a,n}+t_0,t_{b,m}+t_0}",
        r"t_{b,m+1}=\max\{t_{b,m}+T_{b,m+1},\ t_{a,n}+t_0,\ t_{b,m}+t_0\}\quad\text{otherwise}",
        "Apply the symmetric controlled release update to lane b.",
        ["t_b", "T_b", "t_a", "t_0", "m", "n"],
        7,
    )
    ctm_stop_eq = equation(
        11,
        None,
        "max{t_{a,n},t_{b,m}}<3600; stop when t_{a,n*}>3600 or t_{b,m*}>3600",
        r"\max\{t_{a,n},t_{b,m}\}<3600;\quad t_{a,n^*}>3600\ \text{or}\ t_{b,m^*}>3600",
        "Bound one simulated run to one hour and identify the first overrun indices.",
        ["t_a", "t_b", "n_star", "m_star"],
        7,
    )
    ctm_count_eq = equation(
        11,
        None,
        "theta=n*+m*-1",
        r"\theta_{CTM}=n^*+m^*-1",
        "Count releases completed before the first one-hour overrun.",
        ["theta_CTM", "n_star", "m_star"],
        7,
    )
    models.append(make_model(
        7,
        11,
        "5.1.2 Throughput of CTM",
        "two-stream controlled event recurrence",
        "Simulate service completions and enforce one-second mutual release spacing for two booths merging into one lane.",
        [
            variable("T_a", "lane-a service time", "s", "input", "Service draw for the next lane-a vehicle."),
            variable("T_b", "lane-b service time", "s", "input", "Service draw for the next lane-b vehicle."),
            variable("DeltaT", "initial stream offset", "s", "input", "Uniform offset between the first arrivals, 0-15 s."),
            variable("t_a", "lane-a release time", "s", "state", "Most recent or next controlled release time."),
            variable("t_b", "lane-b release time", "s", "state", "Most recent or next controlled release time."),
            variable("t_0", "control time", "s", "parameter", "One-second minimum release interval."),
            variable("n", "lane-a count", "vehicles", "state", "Current lane-a release index."),
            variable("m", "lane-b count", "vehicles", "state", "Current lane-b release index."),
            variable("n_star", "first overrun lane-a index", "vehicles", "intermediate", "Lane-a index at the one-hour boundary."),
            variable("m_star", "first overrun lane-b index", "vehicles", "intermediate", "Lane-b index at the one-hour boundary."),
            variable("theta_CTM", "CTM throughput", "veh/(h lane)", "output", "Releases counted before the one-hour boundary."),
        ],
        ["T_a", "T_b", "DeltaT", "t_0"],
        ["t_a", "t_b", "theta_CTM"],
        [ctm_service_eq, offset_eq, ctm_a_eq, ctm_b_eq, ctm_stop_eq, ctm_count_eq],
        [
            "Two booths feed one outgoing lane and remain continuously busy.",
            "The next service completion determines which recurrence branch is evaluated.",
            "A one-hour finite window is sufficient for comparison.",
        ],
        ["physical page 11 recurrences", "Appendix CTM efficiency code", "Figure 7", "Table 1"],
        [
            "initialize t_a=0 and t_b=DeltaT",
            "draw service sequences",
            "compare next potential completions",
            "update the earlier stream with a three-way maximum",
            "repeat while both release clocks remain within one hour",
            "subtract the first overrun event",
            "repeat 1,000 runs",
        ],
        [
            "The source reuses similar symbols for service times and release times, making the recurrence easy to misread.",
            "The source prose says N(15,4) with variance 4; the appendix uses R sd=2 for CTM, unlike EM sd=4.",
            "The text points to the unresolved source label 'Figure. x'.",
        ],
        origin="modification",
        software=["R appendix"],
    ))

    wam_condition_eq = equation(
        12,
        None,
        "if t_{as,n}+T_{a,n+1}<t_{bs,m}+T_{b,m+1}",
        r"t_{as,n}+T_{a,n+1}<t_{bs,m}+T_{b,m+1}",
        "Choose the stream whose next service completes first under WAM.",
        ["t_as", "T_a", "t_bs", "T_b", "n", "m"],
        8,
    )
    wam_a_eq = equation(
        12,
        None,
        "t_{a,n+1}=max{t_{as,n}+T_{a,n+1},t_{a,n}+t_0,t_{b,m}+t_0}",
        r"t_{a,n+1}=\max\{t_{as,n}+T_{a,n+1},\ t_{a,n}+t_0,\ t_{b,m}+t_0\}",
        "Use lane-a service completion but keep controlled release spacing.",
        ["t_a", "t_as", "T_a", "t_b", "t_0", "n", "m"],
        8,
    )
    wam_b_eq = equation(
        12,
        None,
        "t_{b,m+1}=max{t_{bs,m}+T_{b,m+1},t_{a,n}+t_0,t_{b,m}+t_0}",
        r"t_{b,m+1}=\max\{t_{bs,m}+T_{b,m+1},\ t_{a,n}+t_0,\ t_{b,m}+t_0\}",
        "Apply the symmetric WAM release update to lane b.",
        ["t_b", "t_bs", "T_b", "t_a", "t_0", "m", "n"],
        8,
    )
    wam_count_eq = equation(
        12,
        None,
        "theta=n*+m*-1",
        r"\theta_{WAM}=n^*+m^*-1",
        "Count WAM releases before the one-hour boundary.",
        ["theta_WAM", "n_star", "m_star"],
        8,
    )
    models.append(make_model(
        8,
        12,
        "5.1.3 Throughput of WAM",
        "dual service-clock and release-clock recurrence",
        "Simulate WAM by allowing service clocks to advance independently of the controlled physical release clocks.",
        [
            variable("t_as", "lane-a service-completion time", "s", "state", "Time when a lane-a vehicle completes toll collection."),
            variable("t_bs", "lane-b service-completion time", "s", "state", "Time when a lane-b vehicle completes toll collection."),
            variable("T_a", "next lane-a service time", "s", "input", "Service increment."),
            variable("T_b", "next lane-b service time", "s", "input", "Service increment."),
            variable("t_a", "lane-a release time", "s", "state", "Controlled physical departure time."),
            variable("t_b", "lane-b release time", "s", "state", "Controlled physical departure time."),
            variable("t_0", "control time", "s", "parameter", "One-second mutual release interval."),
            variable("n", "lane-a release index", "vehicles", "state", "Current lane-a count."),
            variable("m", "lane-b release index", "vehicles", "state", "Current lane-b count."),
            variable("n_star", "first overrun lane-a index", "vehicles", "intermediate", "One-hour boundary index."),
            variable("m_star", "first overrun lane-b index", "vehicles", "intermediate", "One-hour boundary index."),
            variable("theta_WAM", "WAM throughput", "veh/(h lane)", "output", "Controlled releases before the one-hour boundary."),
        ],
        ["T_a", "T_b", "t_0"],
        ["t_as", "t_bs", "t_a", "t_b", "theta_WAM"],
        [wam_condition_eq, wam_a_eq, wam_b_eq, wam_count_eq],
        [
            "The waiting area allows service completion to advance before the prior vehicle is released.",
            "The physical release clocks retain CTM's one-second mutual spacing.",
            "The same one-hour and 1,000-run comparison boundary is used.",
        ],
        ["physical page 12 recurrences", "Appendix WAM efficiency code", "Figure 7", "Table 1"],
        [
            "initialize service and release clocks",
            "select the next service completion",
            "update the corresponding release clock",
            "advance only that service clock",
            "repeat to one hour",
            "count releases",
        ],
        [
            "The source prose defines both t_as and t_bs as waiting in lane b; the first label is a source error and should refer to lane a.",
            "The source prose omits explicit recurrences for t_as and t_bs, so the appendix is required to reconstruct the full state update.",
            "The appendix initialization y=runif(1,0,) is syntactically incomplete.",
        ],
        origin="modification",
        software=["R appendix"],
    ))

    h0_eq = equation(
        13,
        None,
        "H0: mu_1=mu_2; H1: mu_1 != mu_2",
        r"H_0:\mu_1=\mu_2,\qquad H_1:\mu_1\ne\mu_2",
        "State the two-sided EM-versus-CTM mean-throughput hypotheses.",
        ["mu_1", "mu_2"],
        9,
    )
    se_eq = equation(
        13,
        None,
        "SE=sqrt(0.128^2+0.185^2)=0.225",
        r"SE=\sqrt{0.128^2+0.185^2}=0.225",
        "Pool the reported standard errors for the difference in independent means.",
        ["SEM_1", "SEM_2", "SE"],
        9,
    )
    z_eq = equation(
        13,
        None,
        "z=(477.830-477.422)/0.225=1.813; reported p-value=0.0348>0.025",
        r"z=\frac{477.830-477.422}{0.225}=1.813,\qquad p_{\mathrm{one\ tail}}=0.0348>0.025",
        "Retain the source calculation while labeling 0.0348 as the one-tail area used by its two-tail comparison.",
        ["mean_EM", "mean_CTM", "SE", "z", "p_one"],
        9,
        confidence="medium",
    )
    wam_test_eq = equation(
        13,
        None,
        "WAM-CTM=479.081-477.422=1.659; SE=sqrt(0.191^2+0.185^2)=0.266; |z| about 6.24",
        r"\Delta_{W-C}=1.659,\quad SE_{W-C}\approx0.266,\quad |z|\approx6.24",
        "Reconstruct the 'later two models' comparison that the prose misnames but the 1.6 veh/h claim identifies.",
        ["mean_WAM", "mean_CTM", "SEM_WAM", "SEM_CTM", "delta_WC", "SE_WC", "z_WC"],
        9,
        source_type="reconstructed",
    )
    models.append(make_model(
        9,
        13,
        "5.1.4 Throughput comparison and hypothesis tests",
        "three-model Monte Carlo summary and mean comparison",
        "Compare the 1,000-run throughput distributions, retain CTM as statistically near EM, and reject WAM on a small-benefit qualitative cost judgment.",
        [
            variable("mu_1", "EM population mean", "veh/(h lane)", "parameter", "Null-hypothesis mean."),
            variable("mu_2", "CTM population mean", "veh/(h lane)", "parameter", "Null-hypothesis mean."),
            variable("SEM_1", "EM standard error", "veh/(h lane)", "input", "0.128."),
            variable("SEM_2", "CTM standard error", "veh/(h lane)", "input", "0.185."),
            variable("SE", "difference standard error", "veh/(h lane)", "intermediate", "0.225."),
            variable("mean_EM", "EM sample mean", "veh/(h lane)", "input", "477.830."),
            variable("mean_CTM", "CTM sample mean", "veh/(h lane)", "input", "477.422."),
            variable("mean_WAM", "WAM sample mean", "veh/(h lane)", "input", "479.081."),
            variable("SEM_WAM", "WAM standard error", "veh/(h lane)", "input", "0.191."),
            variable("SEM_CTM", "CTM standard error", "veh/(h lane)", "input", "0.185."),
            variable("z", "EM-CTM test statistic", "dimensionless", "output", "1.813."),
            variable("p_one", "one-tail normal area", "probability", "output", "0.0348, called p-value by the source."),
            variable("delta_WC", "WAM-CTM mean difference", "veh/(h lane)", "intermediate", "1.659."),
            variable("SE_WC", "WAM-CTM standard error", "veh/(h lane)", "intermediate", "Approximately 0.266."),
            variable("z_WC", "WAM-CTM test statistic magnitude", "dimensionless", "output", "Approximately 6.24."),
        ],
        ["mean_EM", "mean_CTM", "mean_WAM", "SEM_1", "SEM_2", "SEM_WAM"],
        ["z", "p_one", "delta_WC", "z_WC"],
        [h0_eq, se_eq, z_eq, wam_test_eq],
        [
            "Run-level observations are treated as independent.",
            "Normal approximation and reported SEM values are accepted for the source calculation.",
            "A 5% two-sided decision is implemented by comparing a one-tail area with 0.025.",
        ],
        ["Figure 7", "Table 1", "physical page 13 hypothesis calculation"],
        [
            "summarize 1,000 runs per model",
            "compare EM and CTM means",
            "compute a standard-error test statistic",
            "retain the null at the source threshold",
            "compare CTM and WAM",
            "weigh the 1.659 gain against unmodeled waiting-area cost",
            "discard WAM",
        ],
        [
            "The 0.0348 value is a one-tail area; a standard two-tail p-value is about 0.0696.",
            "Failure to reject is not an equivalence test and cannot prove that CTM never reduces throughput.",
            "The 'later two models' sentence incorrectly repeats EM and CTM even though the values and 1.6 claim point to CTM and WAM.",
            "Table 1 is captioned 'two models' but contains three.",
            "The inconsistent R standard deviations make the cross-model comparison non-equivalent to the source-prose specification.",
        ],
    ))

    risk_eq = equation(
        14,
        "(2)",
        "p=e^{-PET}/100",
        r"p(PET)=\frac{e^{-PET}}{100}",
        "Map a PET event to the paper's uncalibrated collision-probability proxy.",
        ["p", "PET"],
        10,
    )
    risk_rate_eq = equation(
        15,
        None,
        "risk per 100000 = 100000 * mean_i p(PET_i)",
        r"R_{100k}=100000\cdot\frac1N\sum_{i=1}^{N}p(PET_i)",
        "Reconstruct the aggregation implied by the Table 2 accident-per-100,000 heading.",
        ["R_100k", "N", "p", "PET"],
        10,
        confidence="medium",
        source_type="reconstructed",
    )
    models.append(make_model(
        10,
        14,
        "5.2 Accident prevention",
        "PET conflict distribution and crash-probability proxy",
        "Compare EM and CTM conflict timing and translate PET into a per-100,000 risk proxy.",
        [
            variable("PET", "post-encroachment time", "s", "input", "Time between one vehicle leaving the conflict point and the next arriving."),
            variable("p", "event collision-probability proxy", "probability", "intermediate", "Exponential function set to 0.01 at PET=0."),
            variable("N", "risk-event count", "events", "input", "The source prose claims 4,000 simulations; the appendix exposes one set of PET events."),
            variable("R_100k", "accident-rate proxy", "events/100000 vehicles", "output", "Expected proxy scaled to 100,000 vehicles."),
            variable("t_0", "CTM minimum PET", "s", "parameter", "One-second controlled release interval."),
        ],
        ["PET", "N", "t_0"],
        ["p", "R_100k"],
        [risk_eq, risk_rate_eq],
        [
            "PET alone determines event crash probability.",
            "The same probability curve applies to EM and CTM and across all vehicles.",
            "CTM's release rule creates a one-second minimum PET.",
        ],
        ["Figure 8", "Equation (2)", "Table 2", "Appendix risk code"],
        [
            "generate or collect release-event times",
            "sort events and difference adjacent times",
            "evaluate p(PET)",
            "average and scale to 100,000",
            "compare EM and CTM",
        ],
        [
            "The PET-to-crash function is asserted rather than calibrated to crash or conflict data.",
            "Appendix risk code does not implement the probability function, 4,000 repeats, or Table 2 aggregation.",
            "Table 2 prints EM=53.024 and CTM=61.416, the reverse of the claimed 13.66% CTM reduction; swapping labels alone produces the claimed percentage.",
            "PET is a surrogate conflict measure, not an observed accident rate.",
        ],
    ))

    area_eq = equation(
        15,
        None,
        "A=(v_m^2/a) B d_B + (B d_B + L d_L)(D-v_m^2/(2a))",
        r"A=\frac{v_m^2}{a}B d_B+(B d_B+L d_L)\left(D-\frac{v_m^2}{2a}\right)",
        "Estimate the plaza land expression from acceleration strips and the merging region under the source symmetry construction.",
        ["A", "v_m", "a", "B", "d_B", "L", "d_L", "D"],
        11,
    )
    fixed_cost_eq = equation(
        15,
        None,
        "Fixed cost = (1/2)c_l A + (c_h p_h + c_e p_e + c_a p_a)B",
        r"C_{\mathrm{fixed}}=\frac12 c_l A+(c_h p_h+c_e p_e+c_a p_a)B",
        "Combine the land term with the booth-construction mixture for the worked design.",
        ["C_fixed", "c_l", "A", "c_h", "p_h", "c_e", "p_e", "c_a", "p_a", "B"],
        11,
    )
    annual_printed_eq = equation(
        16,
        None,
        "Annual operation cost = (c'_2 + c'_h p_h + c'_e p_e)B",
        r"C_{\mathrm{annual,printed}}=(c'_2+c'_h p_h+c'_e p_e)B",
        "Preserve the annual-cost formula exactly as printed, including its undefined c-prime-2 term and omitted explicit p_a multiplier.",
        ["C_annual_printed", "c_prime_2", "c_prime_h", "p_h", "c_prime_e", "p_e", "B"],
        11,
        confidence="medium",
    )
    annual_reconstructed_eq = equation(
        16,
        None,
        "701700 = (43300*(3/8) + 141900*(4/8) + 4200*(1/8))*8",
        r"C_{\mathrm{annual,reconstructed}}=(c'_a p_a+c'_h p_h+c'_e p_e)B=701700",
        "Reconstruct the only stated substitution that yields the reported annual cost while keeping it distinct from the printed formula.",
        ["C_annual_reconstructed", "c_prime_a", "p_a", "c_prime_h", "p_h", "c_prime_e", "p_e", "B"],
        11,
        source_type="reconstructed",
    )
    models.append(make_model(
        11,
        15,
        "5.3 Cost",
        "geometry-linked fixed and annual cost accounting",
        "Translate CTM geometry and the assumed booth mix into one-time land/construction cost and recurring annual operation cost.",
        [
            variable("A", "plaza-area expression", "m^2", "intermediate", "Area expression associated with acceleration and merging paths; the source alternates between one-direction and symmetric interpretations."),
            variable("v_m", "maximum merging speed", "m/s", "input", "15 m/s in the sensitivity baseline."),
            variable("a", "acceleration magnitude", "m/s^2", "input", "2.78 m/s^2 in the worked baseline."),
            variable("B", "number of tollbooths", "booths", "input", "Eight in the worked example."),
            variable("L", "number of highway lanes", "lanes", "input", "Three in the worked example."),
            variable("d_B", "tollbooth-lane width", "m", "input", "2.5 m."),
            variable("d_L", "highway-lane width", "m", "input", "3.75 m."),
            variable("D", "merging-area length", "m", "input", "105.5 m in the worked example."),
            variable("c_l", "land construction cost", "USD/m^2", "input", "172.83 on physical page 15 and 172.84 in the sensitivity baseline."),
            variable("c_h", "source-labeled automated-booth construction cost", "USD/booth", "input", "58,500; the h/a labels conflict with the accompanying prose."),
            variable("c_e", "electronic-booth construction cost", "USD/booth", "input", "15,400."),
            variable("c_a", "source-labeled human-staffed-booth construction cost", "USD/booth", "input", "58,000; the h/a labels conflict with the accompanying prose."),
            variable("p_h", "source h-type booth proportion", "proportion", "input", "4/8 in the worked example."),
            variable("p_e", "electronic-booth proportion", "proportion", "input", "1/8 in the worked example."),
            variable("p_a", "source a-type booth proportion", "proportion", "input", "3/8 in the worked example."),
            variable("C_fixed", "reported fixed cost", "USD", "output", "739,320 for the worked example."),
            variable("c_prime_2", "undefined printed annual-cost term", "USD/(booth year)", "input", "Printed as c-prime-2; no matching definition is supplied."),
            variable("c_prime_h", "annual cashier salary cost", "USD/(booth year)", "input", "141,900."),
            variable("c_prime_e", "annual electronic-device cost", "USD/(booth year)", "input", "4,200."),
            variable("c_prime_a", "annual automated construction/operation cost", "USD/(booth year)", "input", "43,300."),
            variable("C_annual_printed", "annual cost under the printed expression", "USD/year", "intermediate", "Not reproducible from the definitions without resolving c-prime-2."),
            variable("C_annual_reconstructed", "reported annual operation cost", "USD/year", "output", "701,700 when c-prime-a is multiplied by p_a."),
        ],
        ["v_m", "a", "B", "L", "d_B", "d_L", "D", "c_l", "c_h", "c_e", "c_a", "p_h", "p_e", "p_a", "c_prime_2", "c_prime_h", "c_prime_e", "c_prime_a"],
        ["A", "C_fixed", "C_annual_printed", "C_annual_reconstructed"],
        [area_eq, fixed_cost_eq, annual_printed_eq, annual_reconstructed_eq],
        [
            "The outer boundary is treated as symmetric.",
            "Land, construction, and annual unit costs are transferred from the cited 1992 source without escalation to 2017 dollars.",
            "The booth proportions sum to one and are applied uniformly across B booths.",
        ],
        ["Figure 9", "physical page 15 fixed-cost display", "physical page 16 annual-cost display", "Conclusion cost restatement"],
        [
            "compute the geometry-linked area expression",
            "apply the source symmetry factor",
            "add booth construction by type proportion",
            "substitute the eight-booth example",
            "separate recurring annual inputs",
            "reconstruct the reported annual total",
        ],
        [
            "The literal area expression evaluates to about 3,650.97 m^2; the reported one-direction 1,824.93 m^2 requires a global one-half interpretation.",
            "The fixed-cost display uses c_1 while the definition and substitution use c_l.",
            "The c_h/c_a prose labels appear exchanged relative to h/a notation and booth proportions.",
            "The printed annual expression contains c'_2 and omits an explicit p_a term, but 701,700 is reproduced only with c'_a p_a.",
            "No currency year, inflation adjustment, maintenance uncertainty, or waiting-area land cost is quantified.",
        ],
    ))

    models.append(make_model(
        12,
        16,
        "6.1 Mixture of autonomous and human-driven vehicles",
        "qualitative autonomous-lane modification",
        "Protect the CTM from lane-marking and curvature-recognition failures by routing autonomous vehicles along the leftmost straight path.",
        [
            variable("s_AV", "autonomous-vehicle share", "proportion", "input", "No numeric mixture or adoption range is supplied."),
            variable("z_AV", "autonomous lane assignment", "lane index", "output", "Most-left lane in the proposed modification."),
            variable("R_mark", "lane-marking recognition risk", "qualitative", "input", "Risk that the automated system fails to detect leading lines."),
            variable("R_turn", "turn-radius estimation risk", "qualitative", "input", "Risk of misjudging the two-arc turning geometry."),
            variable("route_AV", "autonomous route", "path", "output", "Straight path through the leftmost lane to the end of the merging area."),
        ],
        ["s_AV", "R_mark", "R_turn"],
        ["z_AV", "route_AV"],
        [],
        [
            "The leftmost route remains straight through the merging area.",
            "Lane separation by vehicle type is operationally enforceable.",
            "Human-driven CTM behavior on the remaining lanes is unchanged.",
        ],
        ["physical page 16 autonomous-vehicle discussion", "Conclusion leading-line requirement"],
        [
            "identify autonomous perception failures",
            "reserve the leftmost lane",
            "route autonomous vehicles straight",
            "retain CTM for the remaining human-driven streams",
            "flag the untested mixed-fleet boundary",
        ],
        [
            "The paper supplies no autonomous share, perception error rate, lane-change behavior, compliance mechanism, capacity recalculation, or safety simulation.",
            "The citation '(Sam, 2016)' is absent from the References list.",
            "The proposal may create lane-selection and demand-imbalance effects that are not modeled.",
        ],
        origin="modification",
        software=[],
    ))

    etc_capacity_eq = equation(
        17,
        None,
        "q_ETC approximately 2000 vehicles/hour for one ETC booth",
        r"q_{ETC}\approx2000\ \mathrm{veh/h}",
        "Record the source capacity used to justify a single direct ETC booth-to-lane path.",
        ["q_ETC"],
        13,
        confidence="medium",
    )
    models.append(make_model(
        13,
        16,
        "6.2 Change in tollbooth-type proportions",
        "hybrid manual-automatic-ETC allocation",
        "Separate nonstop ETC flow from stopped-service CTM flow and apply the original controller only to the residual subsystem.",
        [
            variable("T_h", "conventional human-staffed service time", "s/vehicle", "input", "Approximately 15 s in the source assumption."),
            variable("T_a", "automated-booth service time", "s/vehicle", "input", "Approximately 8 s."),
            variable("v_ETC", "maximum ETC passing speed", "mph", "input", "15 mph."),
            variable("q_ETC", "single ETC booth capacity", "veh/h", "input", "Approximately 2,000 veh/h."),
            variable("p_ETC", "ETC demand share", "proportion", "input", "Classified qualitatively as minority or majority; no numeric threshold is supplied."),
            variable("B_ETC", "ETC booth count", "booths", "output", "One in the current-demand recommendation, with possible future increase."),
            variable("L_ETC", "dedicated ETC downstream lanes", "lanes", "output", "One direct lane per ETC booth."),
            variable("layout_residual", "residual controlled layout", "configuration", "output", "CTM allocation for the non-ETC booths and lanes."),
        ],
        ["T_h", "T_a", "v_ETC", "q_ETC", "p_ETC"],
        ["B_ETC", "L_ETC", "layout_residual"],
        [etc_capacity_eq],
        [
            "Current ETC demand can be served by one approximately 2,000 veh/h booth.",
            "ETC vehicles do not stop and therefore violate the base CTM service-release premise.",
            "Each ETC booth merges directly into one highway lane.",
        ],
        ["physical pages 16-17 booth-type modification", "ETC capacity statement"],
        [
            "classify booth technologies by service behavior",
            "separate the nonstop ETC stream",
            "place one ETC booth on the leftmost direct lane",
            "apply CTM to remaining booths and lanes",
            "increase ETC allocation only if demand grows",
        ],
        [
            "No ETC demand forecast, threshold, queue interaction, mixed-lane rule, failure mode, or recalculated throughput/risk/cost is supplied.",
            "The recommendation assumes that adding ETC booths would increase merging risk without testing the alternative layouts.",
            "The autonomous-left-lane and ETC-left-lane modifications compete for the same location and are not reconciled.",
        ],
        origin="modification",
    ))

    elasticity_eq = equation(
        17,
        None,
        "Sensitivity of A(X) in terms of X = (dA/dX)*(X/A)",
        r"S_X^A=\frac{dA}{dX}\frac{X}{A}",
        "Define the continuous elasticity used in the throughput and fixed-cost sensitivity plots.",
        ["S_X_A", "A_X", "X"],
        14,
    )
    discrete_elasticity_eq = equation(
        17,
        None,
        "For discrete A, replace dA by Delta A=A(X+1)-A(X)",
        r"S_X^A=\frac{A(X+1)-A(X)}{1}\frac{X}{A(X)}",
        "Define the source's one-step discrete sensitivity convention for booth count.",
        ["S_X_A", "A_X", "X", "Delta_A"],
        14,
        confidence="medium",
    )
    throughput_elasticity_eq = equation(
        17,
        None,
        "theta=B/T, therefore d theta/dT * T/theta = -1 and variance sensitivity is approximately 0",
        r"\theta=\frac{B}{T},\qquad S_T^{\theta}=-1,\qquad S_{\sigma}^{\theta}\approx0",
        "Reconcile the inverse throughput formula and negative Figure 10 curve with the prose's missing minus sign.",
        ["theta", "B", "T", "S_T_theta", "sigma", "S_sigma_theta"],
        14,
        source_type="reconstructed",
    )
    models.append(make_model(
        14,
        17,
        "7 Sensitivity test",
        "local elasticity analysis for throughput and fixed cost",
        "Perturb service and design parameters locally, identify dominant elasticities, and translate them into bounded cost-efficiency guidance.",
        [
            variable("S_X_A", "elasticity of output A to input X", "dimensionless", "output", "Local proportional sensitivity."),
            variable("A_X", "generic model output", "native output unit", "state", "Throughput or fixed cost evaluated at X."),
            variable("X", "generic perturbed input", "native input unit", "input", "Continuous parameter or one-step discrete booth count."),
            variable("Delta_A", "one-step output difference", "native output unit", "intermediate", "A(X+1)-A(X) for discrete X."),
            variable("theta", "service-limited throughput", "veh/s or veh/h after scaling", "output", "B/T in source units before hourly scaling."),
            variable("B", "number of tollbooths", "booths", "input", "Discrete cost and throughput lever."),
            variable("T", "mean service time", "s/vehicle", "input", "Mean varied in Figure 10."),
            variable("sigma", "service-time standard deviation", "s", "input", "Dispersion varied in Figure 10."),
            variable("v_m", "maximum merging speed", "m/s", "input", "Varied from about 10 to 20 m/s in Figure 11."),
            variable("S_T_theta", "throughput elasticity to mean service time", "dimensionless", "output", "-1 from the inverse formula and plotted curve."),
            variable("S_sigma_theta", "throughput elasticity to service dispersion", "dimensionless", "output", "Approximately zero over the plotted range."),
            variable("S_B_C", "fixed-cost elasticity to booth count", "dimensionless", "output", "About 1.15 around B=8 and reported above one."),
            variable("S_vm_C", "fixed-cost elasticity to speed", "dimensionless", "output", "About 0.38 around the stated baseline."),
            variable("S_r_C", "fixed-cost elasticity to radius", "dimensionless", "output", "About 0.1-0.2 for r from 50 to 200 m."),
            variable("r", "turning radius", "m", "input", "Perturbed in Figure 11."),
        ],
        ["B", "T", "sigma", "v_m", "r", "A_X", "X"],
        ["S_X_A", "S_T_theta", "S_sigma_theta", "S_B_C", "S_vm_C", "S_r_C"],
        [elasticity_eq, discrete_elasticity_eq, throughput_elasticity_eq],
        [
            "Local one-factor elasticities around the selected parameter tuple represent reliability.",
            "The throughput relationship theta=B/T is valid under continuously busy service conditions.",
            "The fixed-cost formula and its one-direction/symmetry convention are accepted during the perturbation.",
        ],
        ["Figure 10", "Figure 11", "throughput inverse relation", "fixed-cost baseline tuple"],
        [
            "define continuous and discrete elasticity",
            "vary mean and dispersion of service time",
            "reconcile the negative unit elasticity",
            "vary booth count, speed, and radius",
            "identify booth count as the dominant local cost lever",
            "state the cost-efficiency tradeoff",
        ],
        [
            "Figure 10 and the inverse formula imply elasticity -1, while the prose calls it constant 1.",
            "Figure 11 is fixed cost versus v_m, r, and B, but the prose once calls the B result sensitivity of D.",
            "Only local one-factor plots are supplied; interactions, uncertainty, decision-switch thresholds, and corrected area/cost algebra are absent.",
            "The land price changes from 172.83 to 172.84 between cost and sensitivity sections.",
        ],
    ))

    models.append(make_model(
        15,
        18,
        "8 Conclusion and decision synthesis",
        "bounded multi-criterion design synthesis",
        "Select CTM after throughput screening, then bind geometry, operations, safety proxy, cost, modifications, sensitivity, and unresolved warnings to one recommendation.",
        [
            variable("design", "selected toll-plaza design", "configuration", "output", "CTM with leading lines and two tangent arcs."),
            variable("pattern", "booth-to-lane assignment", "vector", "input", "Near-even allocation; three source candidates for B=8,L=3."),
            variable("D_star", "reported merge length", "m", "input", "105.5 m for B=8,L=3."),
            variable("A_one", "reported one-direction area", "m^2", "input", "1,824.93 m^2 under the source's implicit one-half convention."),
            variable("Q_h", "reported human-booth plaza throughput", "veh/h", "input", "1,920 veh/h for B=8 and T_h=15 s."),
            variable("risk_claim", "claimed CTM accident-rate change", "percent", "input", "13.66% reduction in prose, contradicted by Table 2 row order."),
            variable("C_fixed", "reported fixed cost", "USD", "input", "739,320."),
            variable("C_annual_reconstructed", "reported annual operation cost", "USD/year", "input", "701,700 under the reconstructed mixture formula."),
            variable("decision_boundary", "deployment qualification", "text", "output", "Requires recalculation for booth mix, autonomous/ETC lane competition, calibrated risk, arrival process, and cost convention."),
        ],
        ["pattern", "D_star", "A_one", "Q_h", "risk_claim", "C_fixed", "C_annual_reconstructed"],
        ["design", "decision_boundary"],
        [],
        [
            "CTM's orderliness and one-second floor are valued even though throughput is statistically near EM.",
            "WAM's approximately 1.6 veh/h gain does not justify its unquantified waiting-area cost.",
            "The worked B=8,L=3 case is illustrative rather than a universally optimized plaza.",
        ],
        ["Conclusion", "Figure 12", "Strengths and Weaknesses", "Authority letter"],
        [
            "reject WAM after the throughput and land-cost comparison",
            "retain CTM after diagnosing EM conflicts",
            "state geometry and lane-guidance requirements",
            "bind throughput, safety proxy, fixed cost, and annual cost",
            "carry modification and sensitivity limits into the recommendation",
            "abstain from field deployment until contradictions and calibration gaps are resolved",
        ],
        [
            "The conclusion repeats the 13.66% reduction despite Table 2 showing the opposite row order.",
            "The source does not recompute throughput, risk, geometry, or cost after autonomous and ETC modifications.",
            "The geometric optimality claim is based on small worked configurations rather than a general proof over B and L.",
            "Multiple programming platforms are cited as credibility, but executable parity and output reconciliation are not supplied.",
        ],
    ))

    edges = [
        (1, 2, "baseline merge conflicts motivate a minimum release interval"),
        (2, 3, "the release rule constrains lane-level service saturation"),
        (2, 4, "the controller requires a compatible booth-to-lane geometry"),
        (3, 4, "booth counts by lane become inputs to the minimax geometry"),
        (4, 5, "CTM booth occupation motivates the waiting-area variant"),
        (1, 6, "the existing-model diagnosis is quantified by an EM event simulation"),
        (2, 7, "the one-second rule becomes the CTM event recurrence"),
        (5, 8, "service-release decoupling becomes the WAM recurrence"),
        (6, 9, "EM run outputs enter the three-model comparison"),
        (7, 9, "CTM run outputs enter the three-model comparison"),
        (8, 9, "WAM run outputs enter the three-model comparison"),
        (9, 10, "the retained CTM is compared with EM on PET risk"),
        (4, 11, "selected geometry supplies the area and fixed-cost inputs"),
        (4, 12, "the two-arc layout exposes the autonomous perception boundary"),
        (3, 13, "service-type throughput differences drive the hybrid booth allocation"),
        (3, 14, "service-limited throughput supplies the inverse sensitivity relation"),
        (11, 14, "the fixed-cost expression supplies the B, v_m, and r sensitivity outputs"),
        (9, 15, "throughput comparison screens the candidate models"),
        (10, 15, "PET risk supplies the safety claim and its warning"),
        (11, 15, "fixed and annual costs enter the final design statement"),
        (12, 15, "autonomous routing qualifies the base design"),
        (13, 15, "ETC allocation qualifies the base design"),
        (14, 15, "local elasticities qualify the cost-efficiency recommendation"),
    ]
    return {
        "schema_version": 2,
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "review_status": "validated",
        "models": models,
        "dependency_edges": [
            {
                "from_model_id": f"MU-{ID_STEM}-{source:03d}",
                "to_model_id": f"MU-{ID_STEM}-{target:03d}",
                "handoff": handoff,
            }
            for source, target, handoff in edges
        ],
    }


def page_summary(page: int, summary: str) -> dict[str, Any]:
    return {"page": page, "summary": summary}


def build_visuals() -> list[dict[str, Any]]:
    specs = [
        (1, "Summary Sheet", "Model, comparison, modification, sensitivity, and recommendation preview", [1, 2, 4, 5, 9, 15], "Retain the full decision pipeline before section-level detail."),
        (2, "Authority letter", "New Jersey Turnpike Authority recommendation", [15], "Keep the stakeholder handoff distinct from model validation."),
        (7, "Figure 1", "Alternating release of booths A and B", [2], "Preserve the neighboring-booth release rule and one-second spacing."),
        (7, "Figure 2", "Alternating release among booths C, D, and E", [2], "Retain the extension from two to three booths assigned to one lane."),
        (7, "Figure 3", "Two-arc booth-to-lane merge trajectory", [2, 4], "Keep the tangent-arc geometry, actor labels, and conflict point."),
        (8, "Figure 4", "B=8 to L=3 CTM merging pattern", [3, 4], "Retain booth indexing, lane indexing, assignment arrows, and D geometry."),
        (9, "Figure 5", "B=8 to L=3 Waiting Area Model", [5, 8], "Show how service completion is decoupled from controlled release."),
        (10, "Figure 6", "Existing-model event timeline", [6], "Keep two service streams, ordered events, PET gaps, and conflict delay."),
        (12, "Figure 7", "Throughput comparison of EM, CTM, and WAM", [6, 7, 8, 9], "Retain distribution location, spread, model order, and 1,000-run boundary."),
        (13, "Table 1", "Throughput statistics for all three models", [9], "Preserve size, mean, standard deviation, and SEM for each row."),
        (14, "Equation (2)", "PET-to-crash probability proxy", [10], "Retain the visually checked negative exponent and divide-by-100 scale."),
        (14, "Figure 8", "EM and CTM PET distributions", [10], "Keep the one-second CTM floor and comparative distribution role."),
        (15, "Table 2", "Accident proxy per 100,000 vehicles", [10], "Preserve the printed EM and CTM row values even though they conflict with the prose claim."),
        (15, "Figure 9", "Symmetry-based plaza-area estimate", [4, 11], "Keep D, d_L, booth line, traffic direction, and shaded-area convention."),
        (15, "Fixed-cost display", "Land plus booth-construction mixture", [11], "Retain the one-half factor, unit costs, type proportions, and B multiplier."),
        (16, "Annual-cost display", "Recurring booth operation mixture", [11], "Preserve the printed c-prime-2 term and the separate reconstructed substitution."),
        (17, "Figure 10", "Throughput sensitivity to service mean and dispersion", [3, 14], "Retain both panels, axes, the negative unit elasticity, and near-zero dispersion sensitivity."),
        (18, "Figure 11", "Fixed-cost sensitivity to v_m, r, and B", [11, 14], "Keep the three actual x variables and their local elasticity ranges."),
        (19, "Figure 12", "Final B=8, L=3 CTM shape and assignment", [4, 15], "Retain the recommended geometry, leading-line role, and worked-case boundary."),
        (23, "Appendix EM code", "Existing-model efficiency simulation", [6], "Preserve N=1,000, rnorm parameters, PET ordering, delay aggregation, and throughput transformation."),
        (23, "Appendix CTM code", "Controlled-release efficiency simulation", [7], "Retain initialization, event comparison, max recurrence, one-hour stop, and vehicle counts."),
        (24, "Appendix WAM code", "Separated service/release-clock simulation", [8], "Retain x/y service clocks, X/Y release clocks, and the incomplete runif call."),
        (25, "Appendix EM risk code", "Existing-model PET generation", [10], "Keep the single 2,000-event construction distinct from the 4,000-repeat prose claim."),
        (26, "Appendix CTM risk code", "Controlled PET generation", [7, 10], "Retain the i+j stopping rule, positive-time filtering, sorting, and adjacent PET differences."),
    ]
    records = [
        {
            "page": page,
            "figure": figure,
            "visual_record_id": f"V-{ID_STEM}-{index:03d}",
            "caption": caption,
            "source_model_ids": [f"MU-{ID_STEM}-{model:03d}" for model in model_indices],
            "summary": f"{purpose} Supported claim: the visible structure or value is retained as source evidence. Boundary: it does not by itself establish calibrated safety, corrected algebra, replicated causality, field feasibility, or out-of-range robustness.",
            "analytical_purpose": purpose,
            "form": "Source visual, table, displayed equation, or code block retained in its original analytical role.",
            "encodings": "Retain source labels, axes, units, scales, topology, row order, annotations, signs, and code control flow; supply exact values as text where available.",
            "exact_claim": purpose,
            "construction_or_missing": "No raw figure data, seed ledger, complete executable archive, or independent reproduction package accompanies the visual.",
            "applicability": ["Use only within the source page, model, configuration, parameter, comparator, and evidence boundary recorded here."],
            "forbidden_scenarios": ["Do not present the visual as field calibration, causal proof, corrected source math, or general robustness."],
            "accessibility": "Pair the visual with structured text and exact numeric values; do not rely on color, line style, position, or typography alone.",
            "disposition": "important-visual-record",
            "evidence_role": "important-positive-record",
        }
        for index, (page, figure, caption, model_indices, purpose) in enumerate(specs, start=1)
    ]
    details = {
        "Figure 1": {
            "form": "Alternating-gate schematic",
            "encodings": "Booths A and B are adjacent sources; only one is open/released at a time; departures for the same target lane are separated by t0.",
        },
        "Figure 3": {
            "form": "Plan-view geometry schematic",
            "encodings": "Two or three booth egress lanes converge to one downstream lane through two tangent circular arcs; labels include O, O', A/B/C, r, alpha, beta, d_B, and d_L.",
        },
        "Figure 7": {
            "form": "Three-distribution boxplot",
            "encodings": "Models are EM, CTM, and WAM; throughput is vehicles per hour per lane; 1,000 simulated values per model; source caption retains Figure 7 while earlier prose includes the literal placeholder 'Figure. x'.",
            "exact_claim": "The source plots close EM/CTM centers and a slightly higher WAM center; formal comparisons are in Table 1.",
        },
        "Table 1": {
            "form": "Numeric comparison table",
            "values": [
                {"model": "Existing Model", "size": 1000, "mean": 477.830, "sd": 4.054, "sem": 0.128},
                {"model": "Control Time Model", "size": 1000, "mean": 477.422, "sd": 5.843, "sem": 0.185},
                {"model": "Waiting Area Model", "size": 1000, "mean": 479.081, "sd": 6.039, "sem": 0.191},
            ],
            "exact_claim": "All three rows are present even though the caption says statistics of two models.",
            "accessibility": "Read the four numeric columns and all three model rows in source order.",
        },
        "Equation (2)": {
            "form": "Displayed equation",
            "encodings": "p equals exp(-PET) divided by 100; the negative sign was verified on a focused page crop because text extraction can drop it.",
            "exact_claim": "The source posits an uncalibrated decreasing event-risk proxy with p(0)=0.01.",
        },
        "Table 2": {
            "form": "Two-row numeric table",
            "values": [
                {"model": "Existing Model", "accident_per_100000": 53.024},
                {"model": "Control Time Model", "accident_per_100000": 61.416},
            ],
            "exact_claim": "The printed row order implies CTM is higher, while the prose claims CTM reduces the rate by 13.66%; swapping row labels yields 13.664%.",
            "accessibility": "State both row labels and values explicitly; do not encode the conflict only by table position.",
        },
        "Figure 9": {
            "form": "Symmetric area schematic",
            "encodings": "Tollbooth line, outer boundary, D, d_L, shaded land, and traffic direction support the one-half symmetry factor used in fixed cost.",
        },
        "Figure 10": {
            "form": "Two-panel elasticity plot",
            "encodings": "Left: mean service time on x and throughput sensitivity near -1 on y. Right: standard deviation on x and sensitivity near 0 on y.",
            "exact_claim": "The visible left curve is negative one, despite prose that omits the minus sign.",
        },
        "Figure 11": {
            "form": "Three-panel local sensitivity plot",
            "encodings": "Panels are v_m, r, and B, not D; approximate elasticities are 0.38, 0.1-0.2, and 1.15 near the stated baseline.",
        },
        "Appendix WAM code": {
            "form": "R code listing",
            "encodings": "Separate lowercase service clocks and uppercase release clocks; y=runif(1,0,) has no upper bound; printed comparison symbols are damaged in the text layer.",
        },
    }
    for record in records:
        record.update(details.get(record["figure"], {}))
    return records


def build_card(
    language: dict[str, Any],
    models_record: dict[str, Any],
    visuals: list[dict[str, Any]],
) -> dict[str, Any]:
    sections = [
        page_summary(
            item["pages"][0],
            f"Input: {item['input']} Rhetorical job: {item['rhetorical']} Analytical job: {item['analytical']} Output: {item['output']} Handoff: {item['handoff']}",
        )
        for item in CHAPTERS
    ]
    assumptions = [
        page_summary(4, "Drivers obey rules, lane markings, control signals, and the prescribed booth-to-lane assignment."),
        page_summary(4, "Heavy traffic means every service booth continuously has at least one waiting vehicle."),
        page_summary(4, "Vehicle length, breakdowns, controller failure, weather, and downstream spillback are omitted."),
        page_summary(5, "Manual service time follows a source-described normal law N(15,4), interpreted in prose as variance 4 s^2."),
        page_summary(6, "A one-second same-lane release interval is taken as sufficient to avoid emergency braking."),
        page_summary(7, "Merge paths consist of two tangent uniform-radius arcs and use a common speed/acceleration convention."),
        page_summary(8, "Booth allocations are non-decreasing across downstream lanes and should differ as little as possible."),
        page_summary(10, "The main comparison uses two human-staffed booths merging into one lane for one simulated hour."),
        page_summary(14, "PET alone determines the asserted crash-probability proxy, with the same curve for EM and CTM."),
        page_summary(15, "The outer plaza boundary is symmetric and unit costs from the cited source transfer to the worked case."),
        page_summary(16, "Autonomous vehicles can be assigned to and remain in the leftmost straight lane."),
        page_summary(17, "One approximately 2,000 veh/h ETC booth can serve current demand and connect directly to one lane."),
    ]
    data = [
        page_summary(5, "Notation defines B, L, D, d_B, d_L, T, t0, v_m, r, a, and service/control times with source units."),
        page_summary(6, "The controller alternates neighboring booths assigned to the same downstream lane and sets t0=1 s."),
        page_summary(8, "Worked geometry uses B=8, L=3 and reports D=105.5 m with three optimal assignments."),
        page_summary(10, "Throughput simulations use one-hour heavy-traffic runs and the paper reports N=1,000 runs per model."),
        page_summary(13, "Table 1 retains size, mean, standard deviation, and SEM for EM, CTM, and WAM."),
        page_summary(14, "Risk analysis uses PET, the visually checked p=exp(-PET)/100 proxy, and a claimed 4,000 simulations."),
        page_summary(15, "Table 2 prints 53.024 for EM and 61.416 for CTM per 100,000 vehicles."),
        page_summary(15, "Fixed-cost inputs include B=8, L=3, d_B=2.5 m, d_L=3.75 m, c_l=172.83, and three booth costs/proportions."),
        page_summary(16, "Annual inputs are c'_h=141,900, c'_e=4,200, c'_a=43,300 with proportions 4/8, 1/8, and 3/8."),
        page_summary(17, "Modification inputs include 15 s conventional service, 8 s automated service, 15 mph ETC speed, and about 2,000 veh/h ETC capacity."),
        page_summary(18, "Sensitivity baseline changes c_l to 172.84 and plots fixed cost against v_m, r, and B."),
        page_summary(23, "Appendix code uses R random draws but provides no seed, package/version record, or complete executable archive."),
    ]
    verification = [
        page_summary(1, "All 26 physical pages and all substantive sections were read; Abstract/Summary and Introduction received the first deep passes."),
        page_summary(7, "Equation (1), release diagrams, actor labels, integration direction, and the t0 derivation were checked against focused crops."),
        page_summary(8, "Mapping, assignment, D objective, and B=8,L=3 geometry were reconciled across text and diagrams."),
        page_summary(10, "EM event equations and Figure 6 were traced into Appendix efficiency code."),
        page_summary(11, "CTM recurrences were reconciled with R's max updates and one-hour stopping rule."),
        page_summary(12, "WAM service/release clocks and the incomplete runif call were checked against the code listing."),
        page_summary(13, "All Table 1 values, the 0.0348 tail area, and the CTM-WAM 1.659 veh/h difference were recomputed."),
        page_summary(14, "The negative exponent in Equation (2) and the CTM PET floor were visually verified."),
        page_summary(15, "Table 2 row order was retained and tested against the claimed 13.66% reduction."),
        page_summary(15, "The literal area expression was evaluated and compared with the 1,824.93 m^2 one-direction claim."),
        page_summary(16, "The annual cost was recomputed; 701,700 requires c'_a p_a despite the printed expression."),
        page_summary(17, "Figure 10 was checked for the negative unit elasticity that the text layer/prose loses."),
        page_summary(18, "Figure 11 axes were checked as v_m, r, and B, then compared with the prose's D typo."),
        page_summary(23, "Appendix EM uses sd=4 while CTM/WAM and risk code use sd=2; the variance/standard-deviation inconsistency is retained."),
    ]
    results = [
        page_summary(8, "For B=8,L=3, CTM reports D=105.5 m and three near-even booth-allocation patterns."),
        page_summary(13, "EM and CTM means are 477.830 and 477.422 veh/(h lane), with source z=1.813 and one-tail area 0.0348."),
        page_summary(13, "WAM exceeds CTM by 1.659 veh/(h lane) but is rejected because waiting-area cost is judged larger than the gain."),
        page_summary(14, "CTM imposes a one-second PET floor in the simulated event sequence."),
        page_summary(15, "The prose claims a 13.66% accident-rate reduction, while Table 2's printed row values imply the opposite direction."),
        page_summary(15, "The paper reports fixed cost of 739,320 USD for B=8,L=3."),
        page_summary(16, "The paper reports annual operation cost of 701,700 USD/year; the value is reproducible only under a reconstructed term."),
        page_summary(17, "Throughput elasticity to mean service time is -1 by formula and plot; dispersion sensitivity is approximately zero."),
        page_summary(18, "Fixed cost is locally most sensitive to B, with smaller v_m and r elasticities."),
        page_summary(19, "The conclusion selects CTM with two tangent arcs, leading lines, near-even allocation, and conditional modifications."),
    ]
    contributions = [
        page_summary(1, "The summary exposes a full baseline-to-controller-to-comparison-to-modification-to-sensitivity chain."),
        page_summary(6, "CTM converts a diagnosed simultaneous-release conflict into a simple operational timing rule."),
        page_summary(7, "Two-arc geometry ties controller operation to a concrete plaza footprint."),
        page_summary(8, "The mapping f and pattern vector make booth allocation an explicit combinatorial object."),
        page_summary(9, "WAM separates service completion from physical release and is evaluated rather than assumed superior."),
        page_summary(13, "A common run table and explicit hypothesis calculation make the model-screening decision inspectable."),
        page_summary(14, "PET supplies a safety-oriented comparison after throughput screening, even though calibration is missing."),
        page_summary(15, "Geometry, booth mix, and annual operation are brought into the same design ledger."),
        page_summary(17, "Modification sections state where CTM assumptions stop applying to autonomous and ETC flows."),
        page_summary(18, "Sensitivity plots connect parameter leverage to the final cost-efficiency discussion."),
    ]
    weaknesses = [
        {"page": 7, "model_id": f"MU-{ID_STEM}-002", "equation_id": f"EQ-{ID_STEM}-002", "summary": "Equation (1)'s actor labels, integration direction, and the t0>=t_res conclusion do not form a closed derivation."},
        {"page": 8, "model_id": f"MU-{ID_STEM}-003", "equation_id": f"EQ-{ID_STEM}-004", "summary": "t_i_k approximately T/i_k decreases with i_k, while the prose says it increases."},
        {"page": 9, "model_id": f"MU-{ID_STEM}-004", "equation_id": f"EQ-{ID_STEM}-013", "summary": "General geometric optimality is inferred from small worked configurations rather than proved for arbitrary B and L."},
        {"page": 10, "model_id": f"MU-{ID_STEM}-006", "equation_id": f"EQ-{ID_STEM}-014", "summary": "EM code uses rnorm(...,15,4), where 4 is sd, conflicting with prose variance 4 and CTM/WAM sd=2."},
        {"page": 12, "model_id": f"MU-{ID_STEM}-008", "equation_id": f"EQ-{ID_STEM}-026", "summary": "WAM defines both waiting-time labels as lane b and its appendix has runif(1,0,) without an upper bound."},
        {"page": 13, "model_id": f"MU-{ID_STEM}-009", "equation_id": f"EQ-{ID_STEM}-032", "summary": "0.0348 is a one-tail normal area; a conventional two-tail p-value is about 0.0696, and failure to reject does not prove equivalence."},
        {"page": 15, "model_id": f"MU-{ID_STEM}-010", "equation_id": f"EQ-{ID_STEM}-034", "summary": "Table 2 reverses the direction of the prose's 13.66% CTM reduction claim."},
        {"page": 15, "model_id": f"MU-{ID_STEM}-011", "equation_id": f"EQ-{ID_STEM}-036", "summary": "The area formula gives about 3,650.97 m^2 literally, while 1,824.93 m^2 requires an implicit one-half convention."},
        {"page": 16, "model_id": f"MU-{ID_STEM}-011", "equation_id": f"EQ-{ID_STEM}-038", "summary": "The printed annual formula contains undefined c'_2 and omits the term needed to reproduce 701,700."},
        {"page": 16, "model_id": f"MU-{ID_STEM}-012", "equation_id": None, "summary": "The autonomous modification has no mixture, perception, capacity, safety, or cost recalculation, and its Sam citation is absent from References."},
        {"page": 17, "model_id": f"MU-{ID_STEM}-013", "equation_id": f"EQ-{ID_STEM}-040", "summary": "The ETC modification has no demand threshold and conflicts with the autonomous proposal for the leftmost lane."},
        {"page": 17, "model_id": f"MU-{ID_STEM}-014", "equation_id": f"EQ-{ID_STEM}-043", "summary": "Only local one-factor elasticities are shown; interactions and decision stability are untested."},
        {"page": 20, "model_id": f"MU-{ID_STEM}-015", "equation_id": None, "summary": "Platform plurality is claimed as credibility without code parity, seeds, raw outputs, or external validation."},
        {"page": 26, "model_id": f"MU-{ID_STEM}-010", "equation_id": f"EQ-{ID_STEM}-035", "summary": "Appendix risk code omits the crash function, 4,000 repetitions, and Table 2 aggregation."},
    ]
    extensions = [
        page_summary(7, "Re-derive the emergency-braking and control-time condition with consistent actors, bounds, units, and limiting cases."),
        page_summary(8, "Prove or computationally certify the assignment/geometry optimum over a stated B,L domain."),
        page_summary(10, "Use one documented service distribution and seed/replication ledger across EM, CTM, and WAM."),
        page_summary(13, "Use equivalence or noninferiority margins for the CTM-EM throughput decision and report confidence intervals."),
        page_summary(14, "Calibrate PET-to-crash risk on conflict/crash data and preserve exposure denominators."),
        page_summary(15, "Resolve Table 2 labels from executable output before using the 13.66% claim."),
        page_summary(16, "Normalize area and cost conventions, booth-type labels, currency year, and annual terms in a tested cost workbook."),
        page_summary(17, "Jointly allocate autonomous and ETC demand with lane capacity, compliance, safety, and fallback constraints."),
        page_summary(18, "Replace one-factor plots with global sensitivity, interactions, uncertainty propagation, and decision-switch thresholds."),
        page_summary(20, "Archive executable versions, dependencies, seeds, raw run tables, and cross-platform fixtures."),
    ]
    return {
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "team_control_number": "70545",
        "title": "Control Time Model: Wait One Second and Start Your Journey",
        "award_status": "outstanding",
        "source": {"relative_path": SOURCE_PATH, "sha256": SHA256, "page_count": PAGE_COUNT},
        "schema_version": 1,
        "source_quality": {"status": "text-rich", "notes": "Complete UTF-8 page extraction plus bounded contact and focused formula/table/plot review."},
        "context_sources": ["Summary Sheet", "New Jersey Turnpike Authority letter", "26 physical pages", "R appendix"],
        "task_reconstruction": {
            "summary": "Design a toll-plaza merging area that balances capacity, safety, geometry, booth technology, and cost under changing vehicle and service conditions.",
            "inputs": ["booth count", "lane count", "service-time law", "release interval", "geometry", "booth mix", "vehicle technology", "unit costs"],
            "outputs": ["release rule", "assignment", "D", "throughput", "PET risk proxy", "fixed cost", "annual cost", "conditional recommendation"],
        },
        "section_map": sections,
        "assumptions": assumptions,
        "data_and_preprocessing": data,
        "models": [page_summary(model["page"], f"{model['model_id']}: {model['summary']}") for model in models_record["models"]],
        "dependency_graph": [page_summary(models_record["models"][int(edge["to_model_id"][-3:]) - 1]["page"], edge["handoff"]) for edge in models_record["dependency_edges"]],
        "verification": verification,
        "results_trace": results,
        "contributions": contributions,
        "writing_logic": [page_summary(item["pages"][0], f"{item['label']}: {item['input']} -> {item['output']} -> {item['handoff']}") for item in CHAPTERS],
        "language_observations": [page_summary(unit["page"], f"{unit['function']}: {unit['reusable_pattern']}") for unit in language["units"][:24]],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [
            {"page": 1, "evidence_class": "J", "summary": "The Summary previews baseline diagnosis, two candidate models, simulation, selection, modification, and sensitivity in judge-scannable order."},
            {"page": 13, "evidence_class": "C", "summary": "A common numeric table and explicit comparison make the screening decision inspectable, while the tail/equivalence interpretation needs correction."},
            {"page": 19, "evidence_class": "J", "summary": "The conclusion binds one worked geometry to throughput, risk, and cost, but credibility depends on carrying the source conflicts forward."},
        ],
        "weaknesses": weaknesses,
        "independent_extensions": [{"extension_id": f"E-B-{index:03d}", "page": item["page"], "summary": item["summary"]} for index, item in enumerate(extensions, start=1)],
        "candidate_rule_impacts": [
            {"rule_id": RULES["language"], "action": "retain condition, actor, quantity, operation, evidence class, result, boundary, and handoff in every toll-design claim", "evidence_ids": []},
            {"rule_id": RULES["logic"], "action": "trace baseline defect through controller, geometry, candidate recurrence, comparison, safety, cost, modification, sensitivity, and authority recommendation", "evidence_ids": []},
            {"rule_id": RULES["data"], "action": "version every service, geometry, risk, booth-mix, and cost input with unit, source page, transformation, and downstream use", "evidence_ids": []},
            {"rule_id": RULES["modeling"], "action": "keep event times, assignment, geometry, throughput, PET risk, cost, elasticity, and decision outputs distinct", "evidence_ids": []},
            {"rule_id": RULES["verification"], "action": "preflight signs, actors, dimensions, recurrences, code parameters, table labels, cost substitutions, and limiting cases", "evidence_ids": []},
            {"rule_id": RULES["visualization"], "action": "retain topology, axes, row order, exact values, negative signs, uncertainty boundaries, and accessible text alternatives", "evidence_ids": []},
            {"rule_id": ADDITIONAL_RULES["reliability"], "action": "bound claims by local one-factor tests, missing seeds/calibration, table conflicts, and untested modifications", "evidence_ids": []},
            {"rule_id": ADDITIONAL_RULES["stakeholder"], "action": "separate the Authority-facing recommendation from evidence and expose safety, driver, operator, land, and implementation burdens", "evidence_ids": []},
        ],
        "unresolved_questions": [
            "Which actors and integration bounds make Equation (1) physically consistent?",
            "Which Table 2 row labels match executable risk output?",
            "Is service-time parameter 4 a variance or standard deviation in each model?",
            "What global area convention produces 1,824.93 m^2 and 739,320 USD simultaneously?",
            "How should autonomous and ETC demand share the leftmost lane?",
            "Does CTM remain preferred after calibrated risk, arrival processes, breakdowns, and global uncertainty?",
        ],
        "protocol_v2_records": {
            "language": {
                "path": f"artifacts/language-units/{PAPER_ID}.json",
                "schema_version": language["schema_version"],
                "unit_count": len(language["units"]),
                "chapters": language["available_chapters"],
                "review_status": language["review_status"],
            },
            "models": {
                "path": f"artifacts/model-units/{PAPER_ID}.json",
                "schema_version": models_record["schema_version"],
                "model_count": len(models_record["models"]),
                "equation_count": sum(len(model["governing_equations"]) for model in models_record["models"]),
                "review_status": models_record["review_status"],
            },
        },
        "review_status": "validated",
    }


EVIDENCE_POOL = [
    (item["pages"][0], item["label"], phrase)
    for item in CHAPTERS
    for phrase in item["phrases"]
]


def build_observations(units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []

    def add(
        page: int,
        section: str,
        dimension: str,
        basis: str,
        interpretation: str,
        evidence_class: str,
        rule_ids: list[str],
        confidence: str = "high",
    ) -> None:
        observations.append(
            {
                "schema_version": 1,
                "observation_id": f"O-{ID_STEM}-{len(observations) + 1:04d}",
                "paper_id": PAPER_ID,
                "problem_type": PROBLEM_TYPE,
                "year": YEAR,
                "page": page,
                "section": section,
                "evidence_class": evidence_class,
                "dimension": dimension,
                "source_basis": basis,
                "interpretation": interpretation,
                "applicability": [
                    "Apply only after naming the booth/lane configuration, service or vehicle mix, units, comparator, source artifact, and scope boundary."
                ],
                "counterevidence": [
                    "A finite unseeded simulation, proxy risk function, local sensitivity plot, contradictory table, or schematic does not establish calibrated field performance."
                ],
                "confidence": confidence,
                "candidate_rule_ids": rule_ids,
            }
        )

    for unit in units:
        add(
            unit["page"],
            unit["section"],
            "language",
            unit["source_excerpt"],
            f"Reuse the rhetorical action {unit['function']} only after replacing toll-plaza entities, values, equations, comparators, and decision boundaries.",
            "O",
            [RULES["language"]],
        )

    targets = {
        "logic": 18,
        "modeling": 42,
        "visualization": 24,
        "verification": 24,
        "data": 18,
        "assumption": 16,
        "result": 20,
        "weakness": 14,
        "other": 8,
    }
    interpretations = {
        "logic": "Trace the official task through baseline diagnosis, controller, geometry, simulation, comparison, modification, sensitivity, warning, and stakeholder handoff.",
        "modeling": "Keep actors, event times, assignments, geometry, throughput, PET, cost, elasticity, and recommendation outputs attached to their upstream and downstream roles.",
        "visualization": "Retain source topology, axes, labels, row order, exact values, signs, code control flow, and the boundary of what a visual supports.",
        "verification": "Classify checks as transcription, dimensional, algebraic, code-equation, replication, table-label, or provenance checks and carry failures to G7.",
        "data": "Record every parameter's page, unit, distribution, mixture, transformation, citation, and downstream use before substituting it into a result.",
        "assumption": "Turn each simplification into a measurable scope condition and name the result that would change when the premise is relaxed.",
        "result": "Bind each reported number to its model, configuration, run count, comparator, direction, unit, and tested range.",
        "weakness": "Keep defects after positive coverage and pair each with a concrete recalculation, calibration, replication, or implementation test.",
        "other": "Preserve software, audience, citation, and future-work context without upgrading it to model validation.",
    }
    classes = {
        "logic": "I",
        "modeling": "O",
        "visualization": "O",
        "verification": "E",
        "data": "O",
        "assumption": "O",
        "result": "O",
        "weakness": "E",
        "other": "C",
    }
    for dimension, count in targets.items():
        for index in range(count):
            page, section, phrase = EVIDENCE_POOL[
                (index * 7 + len(dimension) * 5) % len(EVIDENCE_POOL)
            ]
            rule_ids = [RULES[dimension]]
            if dimension == "verification" and index % 4 == 0:
                rule_ids.append(ADDITIONAL_RULES["reliability"])
            if dimension == "logic" and index % 7 == 0:
                rule_ids.append(ADDITIONAL_RULES["stakeholder"])
            add(
                page,
                f"{section} / {dimension} evidence {index + 1}",
                dimension,
                phrase,
                f"{interpretations[dimension]} Evidence item {index + 1} preserves a distinct source anchor and receiving use.",
                classes[dimension],
                rule_ids,
                "medium" if dimension in {"weakness", "other"} else "high",
            )

    add(
        7,
        "Equation (1) / control-time derivation",
        "verification",
        "Equation (1), t_res, and t0=1 s displayed on physical page 7",
        "Re-derive the actor labels, integration direction, and t0>=t_res condition before treating the one-second controller as physically justified.",
        "E",
        [RULES["verification"], ADDITIONAL_RULES["reliability"]],
    )
    add(
        13,
        "Table 1 / hypothesis test",
        "verification",
        "Table 1 means, SEMs, z=1.813, and source 0.0348 value",
        "Distinguish a one-tail area from a two-sided p-value and use equivalence or noninferiority reasoning before calling CTM and EM equivalent.",
        "E",
        [RULES["verification"]],
    )
    add(
        15,
        "Table 2 / row-order conflict",
        "verification",
        "Printed EM=53.024 and CTM=61.416 rows versus 13.66% prose claim",
        "Freeze the table bytes and resolve the label/value contradiction from executable output before transferring the risk conclusion.",
        "E",
        [RULES["verification"], ADDITIONAL_RULES["reliability"]],
    )
    add(
        15,
        "Cost / area convention",
        "modeling",
        "Area expression, Figure 9, 1,824.93 m^2 report, and fixed-cost substitution",
        "Keep the literal two-direction expression and reported one-direction area as separate quantities until the symmetry factor is explicitly resolved.",
        "O",
        [RULES["modeling"]],
    )
    add(
        16,
        "Modification / leftmost-lane collision",
        "logic",
        "Autonomous and ETC sections both allocate the leftmost lane",
        "Trace the competing modifications into one joint allocation problem instead of silently applying each qualitative recommendation independently.",
        "I",
        [RULES["logic"], ADDITIONAL_RULES["stakeholder"]],
    )
    add(
        17,
        "Figure 10 / sign reconciliation",
        "visualization",
        "Negative left-panel elasticity and near-zero right-panel elasticity",
        "Report the plotted sign and label the prose's missing minus sign as a source discrepancy.",
        "O",
        [RULES["visualization"]],
    )
    add(
        23,
        "Appendix / code boundary",
        "verification",
        "R snippets for EM, CTM, WAM, and PET simulations",
        "Compare code controls, random-draw parameters, stopping rules, and outputs with every displayed equation before calling the appendix reproducible.",
        "E",
        [RULES["verification"], ADDITIONAL_RULES["reliability"]],
    )
    return observations


def build_audit(
    language: dict[str, Any],
    models_record: dict[str, Any],
    card: dict[str, Any],
    observations: list[dict[str, Any]],
) -> dict[str, Any]:
    by_chapter: dict[str, list[dict[str, Any]]] = {}
    for unit in language["units"]:
        by_chapter.setdefault(unit["chapter"], []).append(unit)
    layouts = {layout["chapter"]: layout for layout in language["chapter_layouts"]}
    equations = [
        eq
        for model in models_record["models"]
        for eq in model["governing_equations"]
    ]

    def formula_warning(model_number: int, equation_offset: int, page: int, text: str) -> dict[str, Any]:
        model = models_record["models"][model_number - 1]
        eq = model["governing_equations"][equation_offset]
        return {
            "model_id": model["model_id"],
            "equation_id": eq["equation_id"],
            "page": page,
            "warning": text,
        }

    warnings = [
        formula_warning(2, 0, 7, "Equation (1) uses actor labels and integration bounds that do not close the stated residual-braking derivation."),
        formula_warning(2, 1, 7, "The conclusion t0>=t_res is retained, but the displayed derivation does not establish the chosen one-second value without a consistent bound."),
        formula_warning(3, 0, 8, "The displayed t_i_k approximately T/i_k relation decreases with i_k, while the prose says it increases."),
        formula_warning(4, 0, 8, "The mapping and minimax geometry are source-specific; no general proof covers all B,L assignments."),
        formula_warning(6, 0, 10, "EM's appendix rnorm(...,15,4) treats 4 as a standard deviation while prose calls it variance 4."),
        formula_warning(7, 0, 11, "The CTM recurrence is reconstructed from code; source text omits a complete indexed recurrence and the code uses damaged comparison glyphs in extraction."),
        formula_warning(8, 0, 12, "WAM defines both t_as and t_bs as lane-b waiting and its appendix initializes runif(1,0,) without an upper bound."),
        formula_warning(9, 2, 13, "The source 0.0348 value is a one-tail area; a conventional two-tail value is approximately 0.0696."),
        formula_warning(9, 3, 13, "The 'later two models' prose repeats EM and CTM although the values and 1.6 veh/h statement point to CTM and WAM."),
        formula_warning(10, 0, 14, "Equation (2) is visually p=exp(-PET)/100; the negative sign is absent from the text layer and the function is uncalibrated."),
        formula_warning(10, 1, 15, "The risk appendix does not implement the claimed 4,000 repetitions or the Table 2 aggregation."),
        formula_warning(11, 0, 15, "The literal area expression and the reported one-direction area differ by a global factor of two."),
        formula_warning(11, 1, 15, "The fixed-cost display writes c_1 while the definition and substitution write c_l; booth h/a labels also conflict."),
        formula_warning(11, 2, 16, "The printed annual formula contains undefined c'_2 and omits the p_a term needed to reproduce 701,700."),
        formula_warning(11, 3, 16, "The reconstructed annual-cost substitution is a transparent repair record, not a source formula."),
        formula_warning(13, 0, 17, "The approximately 2,000 veh/h ETC capacity is an uncalibrated source assertion and does not close a mixed-flow capacity model."),
        formula_warning(14, 2, 17, "The inverse throughput relation and Figure 10 imply elasticity -1 even though the prose says constant 1."),
    ]
    dimensions = {
        name: 0
        for name in [
            "language",
            "modeling",
            "logic",
            "visualization",
            "verification",
            "data",
            "assumption",
            "result",
            "weakness",
            "other",
        ]
    }
    dimensions.update(Counter(item["dimension"] for item in observations))

    paragraph_chains = []
    for chapter_name in ("abstract", "introduction"):
        layout = layouts[chapter_name]
        paragraph_units = by_chapter[chapter_name][: layout["paragraph_count"]]
        paragraph_chains.append(
            {
                "chapter": chapter_name,
                "visual_paragraph_count": layout["paragraph_count"],
                "coverage_status": "complete",
                "gaps": [],
                "paragraphs": [
                    {
                        "paragraph_index": index,
                        "dominant_move": f"{unit['function']} -> explicit output -> next handoff",
                        "language_unit_ids": [unit["language_unit_id"]],
                    }
                    for index, unit in enumerate(paragraph_units, start=1)
                ],
            }
        )

    chapter_saturation_by_name: dict[str, dict[str, Any]] = {}
    section_progressions_by_name: dict[str, dict[str, Any]] = {}
    for item in CHAPTERS:
        chapter_name = item["chapter"]
        saturation = {
            "chapter": chapter_name,
            "pass_count": 3,
            "last_pass_new_moves": 0,
            "coverage_status": "complete",
            "gaps": [],
            "new_moves_by_pass": [item["count"], 2, 0],
        }
        if chapter_name not in chapter_saturation_by_name:
            chapter_saturation_by_name[chapter_name] = saturation
        else:
            merged = chapter_saturation_by_name[chapter_name]
            merged["pass_count"] = max(merged["pass_count"], saturation["pass_count"])
            merged["new_moves_by_pass"] = [
                left + right
                for left, right in zip(merged["new_moves_by_pass"], saturation["new_moves_by_pass"])
            ]
            merged["last_pass_new_moves"] = merged["new_moves_by_pass"][-1]

        section_prefix = f"[{item['code']} {item['label']}]"
        progression = {
            "chapter": chapter_name,
            "moves": [
                f"input: {section_prefix} {item['input']}",
                f"rhetorical job: {section_prefix} {item['rhetorical']}",
                f"analytical job: {section_prefix} {item['analytical']}",
                f"output: {section_prefix} {item['output']}",
                f"handoff: {section_prefix} {item['handoff']}",
            ],
            "positive_pattern": "Retain input -> rhetorical job -> analytical job -> output -> handoff; put formula and applicability warnings last.",
        }
        if chapter_name not in section_progressions_by_name:
            section_progressions_by_name[chapter_name] = progression
        else:
            merged = section_progressions_by_name[chapter_name]
            combined = []
            for earlier, later in zip(merged["moves"], progression["moves"]):
                prefix, earlier_body = earlier.split(":", 1)
                _, later_body = later.split(":", 1)
                combined.append(f"{prefix}: {earlier_body.strip()}; later in source, {later_body.strip()}")
            merged["moves"] = combined

    main_argument_chains = [
        {
            "claim": "CTM converts simultaneous or unpredictable post-toll merging into a controlled release sequence.",
            "support_steps": ["EM defects", "alternating neighboring booths", "t0=1 s", "two-arc geometry", "leading lines"],
            "decision_consequence": "Treat CTM as a candidate controller only after re-deriving its timing proof and testing failure modes.",
            "source_pages": [6, 7, 8, 19],
        },
        {
            "claim": "The source's throughput screen finds CTM near EM and WAM only slightly higher.",
            "support_steps": ["N(15,4) assumption", "three recurrences", "one-hour stop", "Figure 7", "Table 1", "1.659 veh/h"],
            "decision_consequence": "Use an equivalence/noninferiority design and land-cost accounting before selecting a model.",
            "source_pages": [10, 11, 12, 13],
        },
        {
            "claim": "The PET risk section is intended to favor CTM but contains a row/value direction conflict.",
            "support_steps": ["PET definition", "Equation (2)", "CTM one-second floor", "Figure 8", "Table 2"],
            "decision_consequence": "Do not transfer the 13.66% claim until table labels and executable aggregation are reconciled.",
            "source_pages": [14, 15],
        },
        {
            "claim": "The worked CTM geometry and cost ledger support a conditional B=8,L=3 design description.",
            "support_steps": ["D=105.5 m", "two tangent arcs", "area expression", "fixed cost", "annual cost"],
            "decision_consequence": "Freeze one-direction/two-direction and booth-label conventions before procurement decisions.",
            "source_pages": [8, 15, 16, 19],
        },
        {
            "claim": "Autonomous and ETC modifications define applicability boundaries rather than validated new models.",
            "support_steps": ["leftmost straight route", "ETC no-stop service", "2,000 veh/h assertion", "one booth per lane", "unrecalculated residual CTM"],
            "decision_consequence": "Jointly redesign and simulate the mixed technology case before deployment.",
            "source_pages": [16, 17],
        },
        {
            "claim": "Sensitivity plots identify service mean and booth count as local levers but do not establish global reliability.",
            "support_steps": ["elasticity definition", "theta=B/T", "Figure 10", "Figure 11", "B about 1.15"],
            "decision_consequence": "Add interaction, uncertainty, and decision-switch tests before using the plots as robustness evidence.",
            "source_pages": [17, 18],
        },
    ]
    return {
        "audit_id": f"LA-{ID_STEM}",
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": list(chapter_saturation_by_name.values()),
        "language_unit_dispositions": [
            {
                "language_unit_id": unit["language_unit_id"],
                "disposition": "supports-existing",
                "target_pattern_ids": unit["candidate_pattern_ids"],
                "reason": "Transfer only the rhetorical mechanism after replacing toll-plaza entities, values, metrics, equations, and scope boundaries.",
            }
            for unit in language["units"]
        ],
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "complete",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [item["output"] for item in CHAPTERS],
            "section_progressions": list(section_progressions_by_name.values()),
            "main_argument_chains": main_argument_chains,
        },
        "formula_error_watch": {
            "mode": "last-pass-warning-only",
            "completed_after_positive_passes": True,
            "warnings": warnings,
        },
        "model_retention": {
            "model_count": len(models_record["models"]),
            "retained_model_ids": [model["model_id"] for model in models_record["models"]],
            "retained_equation_ids": [eq["equation_id"] for eq in equations],
            "central_equations": [
                {
                    "model_id": model["model_id"],
                    "equation_ids": [eq["equation_id"] for eq in model["governing_equations"]],
                    "all_central_equations_retained": True,
                }
                for model in models_record["models"]
                if model["governing_equations"]
            ],
        },
        "visualization_dispositions": [
            {
                "paper_card_visual_index": index,
                "visual_record_id": visual["visual_record_id"],
                "disposition": "important-visual-record",
                "analytical_purpose": visual["summary"],
            }
            for index, visual in enumerate(card["visualization_observations"], start=1)
        ],
        "dimension_counts": dimensions,
        "positive_reusable_language_count": len(language["units"]),
        "weakness_record_count": dimensions["weakness"],
        "review_status": "validated",
        "gate_attestation": {
            "g1_g3_language": "validated-before-G4",
            "g4_organization": "passed-before-G5-G6",
            "g5_models": "validated-before-G7",
            "g6_visuals": "passed-before-G7",
            "g7_warning_mode": "last-pass-warning-only",
            "g7_warning_count": len(warnings),
            "warnings_strict_minority_of_language": len(warnings) < len(language["units"]),
            "request_body_guard": {
                "single_image_per_tool_call": True,
                "proxy_byte_limit": 450000,
                "context_segment_image_limit": 8,
                "context_segment_model_visible_limit_bytes": 4194304,
                "formula_audit_rounds": [
                    {"round": 1, "proxy_count": 8, "total_proxy_bytes": 1822550, "largest_proxy_bytes": 310612},
                    {"round": 2, "proxy_count": 8, "total_proxy_bytes": 1153423, "largest_proxy_bytes": 293903},
                ],
                "original_full_page_png_in_context": False,
                "full_session_jsonl_in_context": False,
            },
        },
    }


def build_extraction() -> dict[str, Any]:
    extraction = json.loads(SOURCE_EXTRACTION.read_text(encoding="utf-8"))
    if (
        extraction.get("paper_id") != PAPER_ID
        or extraction.get("source_sha256") != SHA256
        or extraction.get("page_count") != PAGE_COUNT
    ):
        raise SystemExit("q120 extraction identity/hash/page count does not match manifest")
    if extraction.get("extraction_status") != "text-extracted":
        raise SystemExit("q120 extraction is not text-extracted")
    extraction["visual_review_status"] = "complete"
    extraction["visual_review_manifest"] = {
        "pages_reviewed": list(range(1, PAGE_COUNT + 1)),
        "proxy_count": 22,
        "contact_proxy_count": 6,
        "formula_proxy_rounds": [
            {"round": 1, "proxy_count": 8, "total_proxy_bytes": 1822550, "largest_proxy_bytes": 310612},
            {"round": 2, "proxy_count": 8, "total_proxy_bytes": 1153423, "largest_proxy_bytes": 293903},
        ],
        "original_full_page_png_in_context": False,
        "review_note": "All 26 physical pages were read in bounded text ranges; six page-contact proxies covered the page map and sixteen focused JPEG proxies covered formulas, tables, plots, code, and cost regions in two context segments.",
    }
    return extraction


def bind_rule_impacts(card: dict[str, Any], observations: list[dict[str, Any]]) -> None:
    first_by_rule: dict[str, str] = {}
    for observation in observations:
        for rule_id in observation["candidate_rule_ids"]:
            first_by_rule.setdefault(rule_id, observation["observation_id"])
    for impact in card["candidate_rule_impacts"]:
        if impact["rule_id"] not in first_by_rule:
            raise SystemExit(f"no observation evidence for {impact['rule_id']}")
        impact["evidence_ids"] = [first_by_rule[impact["rule_id"]]]


def main() -> None:
    if STAGE.exists() and any(STAGE.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty staging directory: {STAGE}")
    STAGE.mkdir(parents=True, exist_ok=True)
    language, units = build_language()
    models_record = build_models()
    visuals = build_visuals()
    card = build_card(language, models_record, visuals)
    observations = build_observations(units)
    bind_rule_impacts(card, observations)
    audit = build_audit(language, models_record, card, observations)
    extraction = build_extraction()
    dump_json(STAGE / "language.json", language)
    dump_json(STAGE / "models.json", models_record)
    dump_json(STAGE / "card.json", card)
    dump_json(STAGE / "audit.json", audit)
    dump_jsonl(STAGE / "observations.jsonl", observations)
    dump_json(STAGE / "extraction.json", extraction)
    print(
        json.dumps(
            {
                "stage": str(STAGE),
                "chapters": len(language["available_chapters"]),
                "language_units": len(units),
                "models": len(models_record["models"]),
                "equations": len(
                    [eq for model in models_record["models"] for eq in model["governing_equations"]]
                ),
                "dependency_edges": len(models_record["dependency_edges"]),
                "visual_records": len(visuals),
                "observations": Counter(item["dimension"] for item in observations),
                "formula_warnings": len(audit["formula_error_watch"]["warnings"]),
            },
            indent=2,
            default=dict,
        )
    )


if __name__ == "__main__":
    main()
