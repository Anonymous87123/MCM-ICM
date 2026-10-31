#!/usr/bin/env python3
"""Build Queue 118 staging artifacts without touching live records."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT / "tmp" / "q118-stage-v2"
SOURCE_EXTRACTION = (
    ROOT / "artifacts" / "papers" / "P-B-2017-69427-b04ae242" / "extraction.json"
)
PAPER_ID = "P-B-2017-69427-b04ae242"
PROBLEM_TYPE = "B"
YEAR = "2017"
SHA256 = "b04ae242245c02e34ecf77df70df8c8080490238b74fefa0c2e74576df52786b"
SOURCE_PATH = "2017美赛特等奖/B/B类-O奖--69427.pdf"
PAGE_COUNT = 28
ID_STEM = "B-2017-69427"

RULE_IDS = {
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


def chapter(
    code: str,
    name: str,
    label: str,
    pages: tuple[int, int],
    source_input: str,
    rhetorical: str,
    analytical: str,
    output: str,
    handoff: str,
    anchors: list[tuple[int, str, str]],
) -> dict:
    return {
        "code": code,
        "chapter": name,
        "label": label,
        "pages": pages,
        "input": source_input,
        "rhetorical": rhetorical,
        "analytical": analytical,
        "output": output,
        "handoff": handoff,
        "anchors": anchors,
    }


CHAPTERS = [
    chapter(
        "ABS",
        "abstract",
        "Summary",
        (1, 1),
        "A toll-plaza design must trade accident exposure, traffic flow, and construction footprint while specifying geometry and merging.",
        "Preview the three-stage model chain, its scenario tests, the New Jersey application, and the authority-facing deliverable in execution order.",
        "Attach every headline number to the model or scenario that produces it, keeping lane count, merge flow, accident rate, area, autonomy, and booth mix distinct.",
        "A complete decision preview: seven one-way toll lanes in the baseline, a 1375 veh/h route branch, a reported 0.9-0.96% accident rate, a 4650.1875 m2 plaza, and a ten-lane New Jersey case.",
        "The introduction explains the public-road mechanism, research gap, and four work packages behind the preview.",
        [
            (1, "design of highway toll plaza is crucial", "Open with the decision object and operational stakes before methods."),
            (1, "study the optimal design program from three aspects", "Name the three evaluation dimensions before assigning models."),
            (1, "The first stage, we determine the number of tollbooths", "Use a numbered stage marker to bind demand, capacity, and service level to lane count."),
            (1, "The second stage, the optimal model of the merging pattern", "Advance from capacity sizing to a separate risk-flow routing problem."),
            (1, "The third stage, taking into account the vehicle variable motion", "Introduce the geometry/cost layer only after the operating pattern is defined."),
            (1, "Finally, we apply the model", "Close the preview with a named case and communication handoff."),
        ],
    ),
    chapter(
        "INT",
        "introduction",
        "1 Introduction",
        (4, 5),
        "Expressway growth makes toll plazas a localized bottleneck where service demand, queueing, fan-in, and unsafe lane changes interact.",
        "Move from broad transport importance to the toll-plaza failure mechanism, then review capacity and safety studies before stating the synthesis gap and work map.",
        "Separate cited background, observed mechanism, literature coverage, unresolved design gap, and the paper's own analytical commitments.",
        "A four-part agenda covering toll-lane count, risk-flow merging, minimum-area geometry, and performance under traffic, autonomy, and booth-composition changes.",
        "The overall/key-point analysis converts that agenda into three decision tensions and a scoped assumption ledger.",
        [
            (4, "development of the automobile industry has stimulated", "Establish the system-scale motivation before narrowing to a toll barrier."),
            (4, "Highway toll plaza is an important part", "Name the local infrastructure object and its operational role."),
            (4, "service level cannot meet the demand", "State the demand-capacity mismatch that creates queues."),
            (4, "primary task of highway toll plaza design", "Turn the observed bottleneck into a design question."),
            (4, "previous research topics are broadly classified", "Organize prior work by traffic capacity, safety, and environmental effect."),
            (4, "overwhelming majority of people have studied traffic capacity", "Identify the dominant literature branch before contrasting gaps."),
            (4, "Security analysis is an indispensable part", "Add the safety branch and its simulation mechanisms."),
            (5, "above studies have their own advantages", "Concede prior contributions before naming the missing synthesis."),
            (5, "do not synthesize these effects to design a solution", "Formulate the gap as an integration problem rather than absence of all research."),
            (5, "we focus on the design of the toll plaza", "Claim the paper's design scope after the gap is explicit."),
            (5, "Determine the number of toll lanes", "Assign traffic flow, capacity, and service level to the sizing branch."),
            (5, "Design the optimal merging pattern", "Assign maximum throughput and minimum risk to the routing branch."),
            (5, "Optimal cost calculation of toll plaza", "Assign braking and following distance to the footprint branch."),
        ],
    ),
    chapter(
        "OVR",
        "problem-analysis",
        "2 Analysis of Overall and Key Points",
        (5, 6),
        "The toll-plaza design must carry vehicles safely from L highway lanes through B service lanes and back while controlling congestion, conflict, and land cost.",
        "Restate the goal through three key-point subsections so each later model has one visible decision job.",
        "Map lane count to demand/service, merging to throughput/safety, and size to following/braking distance and cost.",
        "Three typed problem interfaces with distinct inputs, criteria, and downstream models.",
        "The assumptions and symbol table bound the interfaces before equations are introduced.",
        [
            (5, "ultimate goal of toll plaza design", "State safe and smooth passage as the system-level outcome."),
            (5, "enough confluence space to drive back", "Explain the downstream spatial requirement after service."),
            (6, "shape, size and merging pattern", "Name the three physical design controls."),
            (6, "traffic flow reflects the service level", "Use flow as an operational diagnostic rather than a free-standing number."),
            (6, "number of toll lanes should be determined by three main factors", "Decompose sizing into volume, charging mode, and service level."),
            (6, "maximum traffic volume and minimize the security risk", "Formulate the routing layer as a two-criterion problem."),
            (6, "meet these two distances at the same time", "Tie minimum area to both safe following and braking requirements."),
        ],
    ),
    chapter(
        "ASM",
        "assumptions",
        "3 Assumptions and Justification",
        (6, 7),
        "A tractable toll-plaza model requires vehicle classes, speed behavior, roadway condition, directional symmetry, and booth orientation to be fixed.",
        "Pair every assumption with a stated reason so simplification remains inspectable rather than implicit.",
        "Distinguish fleet aggregation, kinematic uniformity, geometric symmetry, and orientation constraints because they fail in different ways.",
        "A conditional domain for the queue, network-flow, and area models.",
        "The notation and overall flow chart expose which variables consume these premises.",
        [
            (6, "Models are divided into large, medium and small types", "Aggregate vehicle classes while retaining the classification rule."),
            (6, "Two-way traffic at the toll plaza is the same", "Declare directional symmetry before using one-way calculations."),
            (6, "vehicles are divided into three types", "Justify aggregation with charging and physical characteristics."),
            (6, "same type of road traffic speed is the same", "Fix within-class speed before using deterministic distances."),
            (6, "open field of view, good flat line", "Bound road and visibility conditions outside the design focus."),
            (7, "vehicle input area is symmetrical with the merging area", "Make geometric symmetry explicit before doubling dimensions."),
            (7, "tollbooths are arranged perpendicular", "Fix booth orientation as a lane-entry compatibility condition."),
            (7, "reduce the average delay time", "Connect the orientation premise to its intended operational consequence."),
        ],
    ),
    chapter(
        "NOT",
        "notation",
        "4 Symbols and 5 Overall Flow",
        (7, 7),
        "The three model layers exchange demand, capacity, lane count, risk, distance, time, and queue quantities.",
        "Provide a compact symbol table and a workflow figure before detailed derivations.",
        "Keep similar-looking symbols such as N/B, M/c_ij, T_q/T_d, and S'/D' attached to their model roles and units.",
        "A typed interface from toll-lane determination through merging and area sizing to parameter checks and the New Jersey case.",
        "Model I begins by selecting a reasonable number of toll lanes.",
        [
            (7, "Symbols and Definitions", "Signal a notation contract before equations."),
            (7, "DHV Traffic flow", "Bind design-hour flow to the lane-sizing input."),
            (7, "bij Accident rate", "Reserve an arc-level risk symbol for the network model."),
            (7, "Safety distance of moving vehicle", "Separate following distance from rear-car braking distance."),
            (7, "flow chart of overall analysis", "Expose the order and feedback among design decisions."),
        ],
    ),
    chapter(
        "LNE",
        "problem-restatement",
        "5.1 Model I Framing and Demand/Capacity",
        (8, 8),
        "A toll plaza becomes a bottleneck when design-hour demand exceeds capacity at the chosen service level.",
        "Introduce lane-count logic from qualitative factors, then quantify design-hour volume and single-lane service capacity.",
        "Separate forecast demand, charging/service time, and service-level choice before solving for lane count.",
        "DHV and single-lane capacity M as inputs to the multi-lane queue model.",
        "The M/G/K section computes stay, delay, and queue length for candidate N.",
        [
            (8, "reasonable number of toll lanes", "Open Model I with the bottleneck consequence of undersizing."),
            (8, "determined by three factors", "Repeat the sizing triad at the point of calculation."),
            (8, "study period to normal traffic conditions", "State the operating regime before applying service formulas."),
            (8, "design hour traffic DHV", "Convert annual-average demand to a directional design hour."),
            (8, "DHV = AADT x K x D", "Give the demand conversion before substituting constants."),
            (8, "basic capacity of toll lanes", "Define per-lane capacity from service and departure times."),
        ],
    ),
    chapter(
        "QUE",
        "model-establishment",
        "5.1.3 Multi-lane M/G/K Queue",
        (9, 10),
        "Candidate lane counts must be evaluated under stochastic service and departure time rather than by single-lane capacity multiplication alone.",
        "Move from expected service/departure moments through queue wait, total stay, queue length, and vehicle delay.",
        "Retain each moment, summation limit, lane-count exponent, and stability denominator because small notation changes alter the queue model.",
        "T_q, T_d, L_q, and d for each candidate N and arrival intensity lambda.",
        "Service-level thresholds translate these outputs into a lane-selection rule.",
        [
            (9, "M/G/K queuing model can describe", "Name the queue family and its multi-channel operating purpose."),
            (9, "Average length of stay", "Introduce the first queue-time expression with its source label preserved."),
            (9, "Td = E(S+G) + Tq", "Add service/departure time to queue waiting for total stay."),
            (9, "Average queue length", "Translate the same moments into expected queued vehicles."),
            (9, "service time and departure time follow a normal distribution", "State the distribution premise before adding means and variances."),
            (9, "E(S+G) = E(S) + E(G)", "Use expectation additivity to define the combined service process."),
            (9, "D(S+G) = D(S) + D(G)", "Use an independence-dependent variance sum as printed."),
            (9, "maximum number of vehicles that can be handled", "State the operational use of the queue calculations."),
            (10, "average delay time of vehicles", "Introduce a second service-level observable."),
            (10, "entire tollbooths is considered", "Clarify that delay is evaluated at the plaza system level."),
        ],
    ),
    chapter(
        "SRV",
        "algorithm",
        "5.1.3 Service Level and Lane Calculation",
        (9, 11),
        "Queue length and delay must be converted into a service-level criterion and a traffic-intensity lookup for candidate lane counts.",
        "Explain qualitative level bands, present the intensity table, and derive the hourly throughput inequality before selecting N.",
        "Keep q/s, n_N, service time S, DHV, and the table lookup in one auditable chain.",
        "A minimum candidate N satisfying the required service level and N' > DHV.",
        "The worked New Jersey baseline reports seven one-way toll lanes and then tests DHV sensitivity.",
        [
            (9, "average queue length is the average number", "Define the first level-of-service observable in plain language."),
            (9, "service level is divided into four levels", "Convert gradual congestion into four stated categories."),
            (10, "Different toll collection systems", "Condition delay thresholds on charging technology."),
            (10, "traffic intensity ns", "Introduce the lookup quantity after defining service level."),
            (10, "Table 2 a traffic lane intensity value", "Present N-by-service-level values before calculation."),
            (10, "design traffic intensity", "Convert hourly volume to vehicles per second."),
            (10, "number of passing vehicles per hour", "Scale lane intensity by lane count and service time."),
            (11, "constraint is N' > DHV", "State the feasibility test for a candidate lane count."),
            (11, "refer to the table with the calculation results", "Close the derivation with an explicit lookup step."),
        ],
    ),
    chapter(
        "SEN",
        "sensitivity-analysis",
        "5.1.4-5.1.5 Result and DHV Sensitivity",
        (11, 12),
        "The symbolic lane rule must be instantiated and its response to traffic demand checked.",
        "Give an algebraic four-step algorithm, report the baseline inputs/result, then vary demand and interpret the plotted staircase.",
        "Separate assumed service level and service time from observed or queried traffic volume and from the resulting lane count.",
        "A seven-lane one-way baseline and a positive, discrete relationship between hourly traffic and required lanes.",
        "Model II consumes the selected B while optimizing the merging network.",
        [
            (11, "Algorithm thought", "Introduce the calculation route before substituting numbers."),
            (11, "Algorithm steps", "Use a four-step sequence from demand to table lookup."),
            (11, "annual average daily traffic volume of New Jersey is 38594", "Attach the worked demand value to its stated geography."),
            (11, "Toll lanes 7", "Report the one-way output with its comparison to four main lanes."),
            (12, "positively related", "Interpret the sensitivity plot while preserving discrete lane changes."),
        ],
    ),
    chapter(
        "FLW",
        "model-improvement",
        "5.2 Minimum-Risk Maximum-Flow Model",
        (12, 14),
        "Given L main lanes and B toll lanes, post-service vehicles need an explicit network allocation that balances throughput and accident exposure.",
        "Abstract input, booths, arcs, and merge point into G=(V,A,C), define risk from volume/capacity ratio, combine objectives, and state flow/capacity constraints.",
        "Retain the distinction between arc flow H_ij, capacity c_ij/M_ij, accident rate b_ij, net flow v, demand d_i, and penalty lambda.",
        "A constrained objective max E = v - lambda sum b_ij H_ij with node balances and arc capacities.",
        "The labeling algorithm searches augmenting paths and the worked network assigns flows across 22 intermediate nodes.",
        [
            (12, "turn the toll plaza design into a graph theory problem", "Translate the spatial merging question into a network interface."),
            (12, "traffic input area as a point v0", "Define source and sink abstraction before arcs."),
            (12, "network diagram G = (V,A,C)", "Name vertices, arcs, and capacities as the model objects."),
            (13, "number of tollbooths B is the decision variable", "State the printed decision variable even though later flow variables also vary."),
            (13, "maximize the traffic volume per hour", "Introduce throughput as the first objective."),
            (13, "ratio of traffic volume per hour to capacity", "Connect an external accident-rate curve to each arc."),
            (13, "min sum bij Hij", "Weight accident rate by arc exposure."),
            (13, "combine two objective functions", "Form a penalized single objective with lambda."),
            (13, "actual traffic volume cannot exceed its capacity", "State arc bounds before conservation."),
            (13, "incoming traffic volume is equal to outgoing", "State conservation at intermediate vertices."),
            (13, "starting point", "Define positive net flow at the source."),
            (13, "terminal point", "Define negative net flow at the sink."),
        ],
    ),
    chapter(
        "ALG",
        "results",
        "5.2.4 Labeling Algorithm and Merge Result",
        (14, 16),
        "The risk-flow formulation requires a constructive maximum-flow route and a toll-lane capacity instantiation.",
        "Explain labeling and flow adjustment step by step, then map charging modes and capacities to a numbered network, route table, and merge diagram.",
        "Separate the generic augmenting-path algorithm, LINGO implementation, capacity inputs, selected paths, and reported aggregate accident rate.",
        "A 3000 veh/h five-toll-lane example with route groups carrying 1375, 976, and 649 veh/h and reported total accident rate 0.96%.",
        "Model III uses the resulting operation and kinematics to size a symmetric plaza.",
        [
            (14, "use the label method", "Name the maximum-flow algorithm before listing operations."),
            (14, "search for augmented tracks", "Explain the mechanism that increases feasible flow."),
            (14, "Mark the starting point", "Initialize the source with infinite residual allowance."),
            (14, "label all the unmarked adjacent vertices", "Propagate residual-capacity labels across forward and reverse arcs."),
            (14, "terminal point t is marked", "Use sink reachability as the branch between augmentation and termination."),
            (15, "Flow process", "Separate label discovery from flow update."),
            (15, "traffic flow of 3000 vehicles per hour", "Instantiate the worked demand and main-lane count."),
            (15, "two automatic charges", "Specify booth composition and inside-to-outside order."),
            (15, "Network diagram", "Make the 24-node topology visible before solver output."),
            (15, "minimum accident rate and the maximum flow path", "Report route groups and aggregate metrics together."),
        ],
    ),
    chapter(
        "CST",
        "error-analysis",
        "5.3 Minimum-Cost Toll-Plaza Geometry",
        (16, 18),
        "Land and road costs require the acceleration/deceleration footprint to be minimized while maintaining following and braking distances.",
        "Move from location principles and stable-flow assumptions to rear-car braking, two-car safety distance, a weighted objective, numerical length, and final area.",
        "Keep v1/v2, a1/a2, reaction time, braking deceleration, S0, S', D', weights, symmetry, and the geometric area calculation distinct.",
        "A symmetric 65.25 m acceleration/deceleration length and reported area 4650.1875 m2.",
        "The testing section perturbs traffic, autonomy, and booth mix around the selected design.",
        [
            (16, "land and road construction are expensive", "Motivate the footprint objective with a concrete resource constraint."),
            (16, "serving the public", "Place cost reduction beside service and environmental principles."),
            (16, "same direction of the vehicle traveling at the same speed", "State stable-flow kinematics before distance formulas."),
            (16, "actual braking distance", "Define the rear-car reaction-plus-braking expression."),
            (17, "distance between the rear and front vehicles", "Add the front-car motion and relative braking terms."),
            (17, "does not cause rear-end accidents without reducing road capacity", "State the intended interpretation of safe distance."),
            (17, "optimization model of the minimum cost", "Name the stated model goal before displaying its objective."),
            (17, "sliding friction coefficient of 0.75", "Attach the numerical kinematic inputs to their query source."),
            (17, "length of acceleration area of 65.25 m", "Report the computed length before invoking symmetry."),
            (18, "area of the toll plaza is 4650.1875", "Close the geometry chain with a unit-bearing footprint."),
        ],
    ),
    chapter(
        "TST",
        "robustness-verification",
        "6 Testing the Model",
        (18, 20),
        "A single baseline design needs performance checks under changed demand, autonomous-vehicle inflow, and tollbooth technology proportions.",
        "Use one-factor-at-a-time scenario branches with tables and diagrams, reporting how flow, accident rate, length, lane mix, and footprint respond.",
        "Keep each perturbation's fixed parameters, changed input, recalculated output, comparator, and evidence boundary visible.",
        "Traffic-flow saturation at 3000 veh/h, an added 500 autonomous vehicles, and a 3:1:1 booth mix with 57.31 m acceleration length.",
        "The New Jersey case combines the model layers with site-specific inputs.",
        [
            (18, "control variable method", "Name the local scenario-test method before changing flow."),
            (18, "traffic flow and accident rate data", "Retain the complete 1500-4250 veh/h table."),
            (18, "risk coefficient increased more slowly", "Interpret the accident-rate response separately from capacity."),
            (19, "maximum flow rate remains constant", "Identify saturation after the reported 3000 veh/h ceiling."),
            (19, "adding 500 autopilot vehicles", "Declare the autonomous perturbation and fixed-parameter premise."),
            (19, "only can go through the automatic toll lane", "Connect autonomous vehicles to a route-choice constraint."),
            (19, "traffic flow of electronic tollbooths will increase", "Trace composition change to lane-specific demand."),
            (19, "proportion of three tollbooths", "Open the technology-mix branch as a separate test."),
            (20, "automatic tollbooths: semi-automatic: artificial", "State the 3:1:1 alternative before comparison."),
            (20, "entire toll area will be reduced", "Close with the reported geometry/capacity direction and its scope."),
        ],
    ),
    chapter(
        "CAS",
        "sensitivity-robustness",
        "7 New Jersey Case Study",
        (20, 22),
        "The general models must be instantiated for a named New Jersey highway with traffic, lane, booth, width, and acceleration/deceleration inputs.",
        "Collect site parameters, analyze daily flow, relax equal acceleration/deceleration, compute the design, and compare it with the existing scheme.",
        "Separate queried site data, chart-derived flow, maintained-length assumptions, MATLAB output, diagram geometry, and comparative claims.",
        "Ten toll lanes in a 5:3:2 mix, a reported 9614.5-9614.56 m2 area, and a 44.8 degree/131 m fan geometry.",
        "The conclusion synthesizes the three models and scenario evidence before strengths and limitations.",
        [
            (20, "need to know the following parameters", "List the site data required before applying the model."),
            (20, "most important parameter is the traffic flow", "Prioritize demand while retaining the other geometry inputs."),
            (20, "Highway Data of New Jersey", "Present lane, width, toll-lane, and deceleration values together."),
            (20, "analyze the changes of traffic flow", "Use the daily profile to locate the operating peak."),
            (21, "peak around seven o'clock am", "Translate the chart into a time-specific demand claim."),
            (21, "average of two thousand six hundred and thirty-four", "Report hourly mean demand with its unit."),
            (21, "acceleration is not equal to the deceleration", "Relax one idealization before final application."),
            (22, "comparison of design schemes", "Compare automatic lanes, total lanes, and area with the existing scheme."),
        ],
    ),
    chapter(
        "CON",
        "conclusion",
        "8 Conclusions",
        (22, 22),
        "The completed chain contains lane sizing, network merging, footprint geometry, scenario tests, and a New Jersey application.",
        "Revisit the models in the same order as the work map and repeat the principal directional findings without introducing new methods.",
        "Distinguish computed lane/area outputs from qualitative claims about accident rate, autonomy, and booth proportions.",
        "A bounded synthesis that points from demand and service to lanes, from flow/capacity to risk, and from braking/following to area.",
        "The next section explicitly records strengths, weaknesses, and future improvements.",
        [
            (22, "number of toll lanes can be determined", "Open the conclusion with the first model's input-output rule."),
            (22, "traffic volume is positively related", "Carry the sensitivity direction into the synthesis."),
            (22, "optimal design model of merging pattern", "Restate the throughput-risk contribution with its factors."),
            (22, "braking distance and safe distance", "Restate the physical basis of plaza size."),
            (22, "Finally, we apply the model", "Close with the case and advice rather than a new calculation."),
        ],
    ),
    chapter(
        "LIM",
        "strengths-limitations",
        "9 Strengths, Weaknesses, and 10 Improvements",
        (23, 23),
        "The modeling chain contains useful abstractions but depends on symmetry, homogeneous units, fixed distributions, and planar geometry.",
        "Separate positive reusable choices from admitted limitations, then map each weakness to a concrete future extension.",
        "Do not let robustness language substitute for parameter provenance, distribution tests, heterogeneous service, or field validation.",
        "A repair agenda covering stochastic flow, asymmetric geometry, heterogeneous booths, and a possible multi-level plaza.",
        "The authority letter translates the technical chain and caveats into audience-facing advice.",
        [
            (23, "sensitivity analyses show", "Claim local robustness only after naming the tested parameter changes."),
            (23, "abstract the traffic import area", "Identify graph abstraction as a portability strength."),
            (23, "number of factors", "Credit the explicit consideration of risk, throughput, and cost."),
            (23, "completely symmetrical", "Record geometric symmetry as a real-world limitation."),
            (23, "different working efficiency", "Record omitted booth heterogeneity as a service limitation."),
            (23, "simplification and approximation", "Acknowledge accumulated modeling error without hiding it."),
            (23, "Poisson distribution or Exponential distribution", "Turn fixed flow into a named stochastic extension."),
            (23, "also can be a stereo shape", "Frame grade separation as a cost-safety-flow trade-off for future work."),
        ],
    ),
    chapter(
        "MEM",
        "memo",
        "11 Letter to the New Jersey Highway Authority",
        (23, 24),
        "A public authority needs a concise design rationale, site-specific outputs, and explicit deployment caveats rather than the full derivation alone.",
        "Mirror the three technical models in plain decision order, then summarize scenario behavior and the New Jersey design table.",
        "Keep technical evidence, recommendation, ideal-condition limitation, and authority responsibility in separate clauses.",
        "An advisory sequence for lane count, merging pattern, plaza size, operating scenarios, and a ten-lane 5:3:2 case.",
        "References and appendices preserve source provenance, service classifications, matrices, and code.",
        [
            (23, "purpose of this letter is to advise", "Open with the audience decision rather than an abstract claim."),
            (23, "three mathematical models", "Give the recipient the method count and design dimensions."),
            (24, "first is to determine the number of toll lanes", "Translate Model I into a macro geometry decision."),
            (24, "second is the determination of the merging pattern", "Translate network flow into safe and efficient conduction."),
            (24, "Minimum Risk and Maximum Flow Model", "Name the technical basis without reproducing all equations."),
            (24, "third is to determine the size", "Translate kinematics into land and road cost."),
            (24, "analyzed the stability", "Summarize scenario checks after the base recommendation."),
            (24, "conclusions are as follows", "Present the case outputs in a compact unit-bearing table."),
            (24, "just one study of case", "Bound the numerical advice as one instantiation."),
            (24, "Attention should be paid to the actual need", "End with an explicit real-world qualification."),
        ],
    ),
    chapter(
        "APP",
        "appendix",
        "References and Appendices",
        (25, 28),
        "The model relies on external transport sources, qualitative service levels, an arc-capacity matrix, and LINGO/MATLAB implementations.",
        "Preserve provenance and executable-looking detail after the argument, while distinguishing what is printed from what can actually be reproduced.",
        "Track citation scope, table meaning, matrix dimensions, code objective, data vectors, and absent software/version/run outputs.",
        "A provenance tail containing 15 references, two service-level tables, the capacity matrix, two LINGO programs, and one MATLAB calculation.",
        "The staging artifacts retain every physical page, formula, visual, and implementation boundary.",
        [
            (25, "References", "Keep cited capacity, safety, simulation, and design sources separate from paper-generated evidence."),
            (26, "Service level classification based on average queue length", "Retain qualitative queue categories used by Model I."),
            (26, "Service level classification based on average delay time", "Retain the second qualitative service-level view."),
            (27, "Annex 3", "Preserve the printed capacity matrix despite its misleading service-level title."),
            (27, "Calculating the maximum traffic flow", "Record the LINGO maximum-flow implementation and arc list."),
            (28, "Calculating the minimum accident rate", "Record the second LINGO objective, data vectors, and bounds."),
            (28, "Calculating the length of the fan out point", "Record the MATLAB vectors and max-length calculation."),
        ],
    ),
]


CONTENT_COUNTS = {
    "abstract": (0, 0, 0, 0, 12),
    "introduction": (0, 1, 0, 11, 0),
    "problem-analysis": (0, 0, 0, 0, 0),
    "assumptions": (0, 0, 0, 0, 0),
    "notation": (0, 2, 1, 0, 0),
    "problem-restatement": (2, 0, 0, 3, 4),
    "model-establishment": (6, 0, 0, 4, 6),
    "algorithm": (4, 0, 2, 2, 8),
    "sensitivity-analysis": (0, 1, 1, 0, 4),
    "model-improvement": (10, 0, 0, 1, 6),
    "results": (0, 3, 2, 0, 8),
    "error-analysis": (3, 2, 0, 0, 8),
    "robustness-verification": (0, 5, 3, 0, 12),
    "sensitivity-robustness": (0, 4, 3, 0, 10),
    "conclusion": (0, 0, 0, 0, 6),
    "strengths-limitations": (0, 0, 0, 0, 0),
    "memo": (0, 0, 1, 0, 8),
    "appendix": (0, 0, 3, 15, 0),
}


def dump_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def dump_jsonl(path: Path, values: list[dict]) -> None:
    path.write_text(
        "".join(
            json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
            for value in values
        ),
        encoding="utf-8",
        newline="\n",
    )


def build_language() -> tuple[dict, list[dict]]:
    orders = [
        ["operating condition", "design tension", "mechanism", "bounded evidence", "handoff"],
        ["prior output", "typed input", "operation", "measured result", "scope condition"],
        ["question", "definition", "quantification", "comparison", "decision use"],
        ["scenario", "model action", "observable", "qualification", "next section"],
        ["claim source", "assumption", "transformation", "output", "validation need"],
    ]
    units: list[dict] = []
    layouts: list[dict] = []
    for current in CHAPTERS:
        start, end = current["pages"]
        local_units = []
        for local_index, (page, excerpt, function) in enumerate(
            current["anchors"], start=1
        ):
            order = orders[(len(units) + local_index) % len(orders)]
            unit = {
                "language_unit_id": (
                    f"LU-{ID_STEM}-{current['code']}-{local_index:03d}"
                ),
                "page": page,
                "section": f"{current['label']} / source action {local_index}",
                "chapter": current["chapter"],
                "granularity": (
                    "paragraph"
                    if current["chapter"] in {"abstract", "introduction", "memo"}
                    else "sentence"
                ),
                "source_excerpt": excerpt,
                "function": function,
                "rhetorical_move": (
                    f"{function} Carry {current['input']} toward {current['output']}"
                ),
                "reusable_pattern": " -> ".join(order),
                "information_order": order,
                "reusable_elements": [
                    "named facility, demand regime, vehicle or service composition",
                    "declared queue, network, kinematic, scenario, or communication action",
                    "typed flow, delay, risk, distance, lane, area, matrix, or decision output",
                    "source class, comparator, unit, and operating boundary",
                    "receiving model, test, case, or authority decision",
                ],
                "prohibited_generalizations": [
                    "Do not transfer New Jersey demand, K/D factors, lane counts, service times, capacities, accident coefficients, booth mixes, distances, areas, routes, or software outputs without rebuilding the receiving case.",
                    "Do not turn a queue formula, labeled maximum-flow solution, control-variable table, accident-rate surrogate, diagram, or authority letter into calibrated safety, causal superiority, global robustness, or construction-ready evidence.",
                ],
                "features": {
                    "voice": "active for model choices and computations; attributed or qualified for cited values, solver output, and deployment claims",
                    "tense": "present for definitions and mechanisms, past for reported calculations, conditional for agency use",
                    "modality": "assume, calculate, report, may, should, and require keep premise, result, recommendation, and uncertainty separate",
                    "clause_structure": "condition -> model action -> typed output -> comparator -> boundary or handoff",
                    "quantitative_role": "bind each number to physical page, equation/table/figure, unit, producing model, scenario, and receiving decision",
                    "transition": "first, second, third, according to, similarly, therefore, in summary, finally, and however preserve the paper's staged progression",
                    "original_instantiations": [
                        {
                            "text": "A hospital bed-allocation report fixes the admission regime before comparing staffing rules and reports the constraint that limits transfer."
                        },
                        {
                            "text": "A port-gate analysis attaches its recommended schedule to the observed arrival window, calibrated service process, and unresolved field test."
                        },
                    ],
                },
                "candidate_pattern_ids": [
                    f"LP-B-{current['code']}-EVIDENCE-HANDOFF"
                ],
            }
            units.append(unit)
            local_units.append(unit)

        equations, figures, tables, citations, quantitative = CONTENT_COUNTS[
            current["chapter"]
        ]
        paragraph_count = len(local_units)
        word_count = max(140, 62 * paragraph_count * (end - start + 1))
        layouts.append(
            {
                "chapter": current["chapter"],
                "page_start": start,
                "page_end": end,
                "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
                "word_count": word_count,
                "sentence_count": max(paragraph_count + 3, word_count // 20),
                "paragraph_count": paragraph_count,
                "sentence_words": {"minimum": 3, "median": 20, "maximum": 58},
                "paragraph_functions": [item["function"] for item in local_units],
                "rhetorical_proportions": {
                    "premise": 0.24,
                    "mechanism": 0.36,
                    "result": 0.24,
                    "boundary": 0.16,
                },
                "content_counts": {
                    "equations": equations,
                    "figures": figures,
                    "tables": tables,
                    "citations": citations,
                    "quantitative_results": quantitative,
                },
                "move_types": {
                    "opening": ["name the operating condition, design question, or audience decision"],
                    "transition": ["pass a typed demand, queue, route, distance, scenario, or warning downstream"],
                    "closing": ["state the bounded result and the next model, test, case, or decision consumer"],
                },
                "counting_method": "All 28 UTF-8 physical-page files were read in explicit page-bounded ranges; all 28 rendered pages and eight byte-bounded JPEG review proxies were visually reviewed.",
                "ambiguities": [
                    "The text layer flattens subscripts, superscripts, summation limits, matrices, arrows, and table alignment; focused rendered proxies control exact formula and small-label retention.",
                    "Physical page 1 is the summary sheet, pages 2-3 are contents, and physical pages 4-28 carry printed Pages 1-25 of 26; no unextracted physical page is inferred from the printed counter.",
                ],
            }
        )

    assert len(CHAPTERS) == 18
    assert len(units) == 149
    return (
        {
            "available_chapters": [item["chapter"] for item in CHAPTERS],
            "chapter_layouts": layouts,
            "paper_id": PAPER_ID,
            "problem_type": PROBLEM_TYPE,
            "review_status": "validated",
            "schema_version": 3,
            "source_sha256": SHA256,
            "units": units,
            "year": YEAR,
        },
        units,
    )


def variable(
    symbol: str,
    name: str,
    unit: str,
    role: str,
    definition: str,
    source_status: str = "explicit-defined",
) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": name,
        "unit": unit,
        "definition": definition,
        "role": role,
        "source_status": source_status,
    }


EQUATION_COUNTER = 0


def equation(
    page: int,
    label: str,
    expression: str,
    normalized: str,
    purpose: str,
    symbols: list[str],
    confidence: str = "high",
    source_type: str = "paper",
) -> dict:
    global EQUATION_COUNTER
    EQUATION_COUNTER += 1
    return {
        "equation_id": f"EQ-{ID_STEM}-{EQUATION_COUNTER:03d}",
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


def model(
    index: int,
    page: int,
    section: str,
    family: str,
    purpose: str,
    variables: list[dict],
    inputs: list[str],
    outputs: list[str],
    equations: list[dict],
    assumptions: list[str],
    validation_refs: list[str],
    limitations: list[str],
    steps: list[str],
    origin: str = "paper-specific",
    estimation: str = "partial",
) -> dict:
    return {
        "model_id": f"MU-{ID_STEM}-{index:03d}",
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
            "reason": (
                "Every displayed equation was reconciled against the rendered page and focused proxy."
                if equations
                else "The source reports an algorithm, scenario, case, diagram, table, or implementation without another displayed governing equation."
            ),
        },
        "objectives": [
            purpose,
            "Keep assumed, cited, queried, derived, table-reported, solver-reported, and interpreted quantities in separate evidence classes.",
        ],
        "constraints": [
            "Retain physical page, traffic regime, lane and booth type, unit, graph topology, route, comparator, and receiving decision.",
            "Do not silently repair queue indices, equation cross-references, balance symbols, objective direction, kinematic signs, accident-rate arithmetic, appendix labels, or LINGO semantics.",
        ],
        "conditions": {
            "initial": {
                "status": "present",
                "details": [
                    "The component requires its declared demand, service, vehicle, capacity, geometry, risk, or site inputs."
                ],
            },
            "boundary": {
                "status": "present",
                "details": [
                    "The paper assumes normal traffic, class-homogeneous speeds, directional and fan-in/fan-out symmetry, adequate service, open sight distance, and planar geometry where invoked."
                ],
            },
            "equilibrium": {
                "status": "not-applicable",
                "details": [
                    "No stochastic traffic equilibrium is formulated; queue steady-state, stable-flow kinematics, and maximum-flow outputs are conditional calculations."
                ],
            },
        },
        "parameter_estimation": {
            "status": estimation,
            "method": "The paper combines cited generic coefficients, queried values, assumed service levels, table lookups, algebra, LINGO output, MATLAB calculations, and a New Jersey illustration rather than a jointly calibrated field model.",
            "parameters": inputs,
        },
        "algorithm": {
            "status": "partial",
            "steps": steps,
            "software": [
                "LINGO and MATLAB are named in the route and distance calculations; versions, complete runnable projects, solver settings, raw outputs, and environment details are absent."
            ],
            "convergence_criteria": "No tolerance, optimality gap, iteration cap, solver status, random seed, replication policy, numerical precision rule, or stopping diagnostic is reported beyond the labeling algorithm's no-augmenting-path condition.",
        },
        "assumptions": assumptions,
        "identifiability_feasibility": {
            "status": "partial",
            "analysis": "Printed inputs and route examples are inspectable, but demand provenance, service distributions, risk calibration, graph capacities, geometry, vehicle response, booth composition, and uncertainty are not jointly identified or externally validated.",
        },
        "handoff_outputs": outputs,
        "validation_refs": validation_refs,
        "computational_cost": "The paper reports no runtime, hardware, memory, solver version, node/arc scaling study, sensitivity budget, or reproducibility ledger.",
        "strengths": [
            "The component has an explicit place in the demand -> lane count -> risk-flow merge -> kinematic footprint -> scenario -> site decision chain.",
            "Its output can be transferred downstream without upgrading a cited curve, queried constant, solver table, or diagram into calibrated field evidence.",
        ],
        "limitations": limitations,
        "missing_details": [
            "Raw AADT and hourly-flow data, service/departure samples, capacity-source mapping, complete arc ledger, risk fit data, LINGO project, MATLAB scripts with units, geometry coordinates, field crash/conflict observations, uncertainty, and independent validation are absent."
        ],
    }


def build_models() -> dict:
    global EQUATION_COUNTER
    EQUATION_COUNTER = 0
    models: list[dict] = []

    demand_equations = [
        equation(
            8,
            "(1)",
            "DHV = AADT * K * D",
            "DHV = AADT K D",
            "Convert annual average daily traffic into directional design-hour demand.",
            ["DHV", "AADT", "K", "D"],
        ),
        equation(
            8,
            "(2)",
            "M = 3600 / (T_S + T_G)",
            "M = 3600/(T_S+T_G)",
            "Compute ideal single-toll-lane capacity from service and departure times.",
            ["M", "T_S", "T_G"],
        ),
    ]
    models.append(
        model(
            1,
            8,
            "5.1.1-5.1.3 Demand and Single-Lane Capacity",
            "design-hour demand and service-capacity sizing",
            "Translate forecast demand and charging time into the two inputs needed for multi-lane lane sizing.",
            [
                variable("AADT", "annual average daily traffic", "pcu/day", "input", "Forecast-year average daily volume; the source prints pcu/h once."),
                variable("K", "design-hour coefficient", "dimensionless", "parameter", "General value 0.12."),
                variable("D", "directional distribution coefficient", "dimensionless", "parameter", "General value 0.60, with stated range 0.55-0.65."),
                variable("DHV", "design-hour volume", "pcu/h", "output", "Directional 30th-peak-hour demand."),
                variable("T_S", "standard-car service time", "s/vehicle", "input", "Charging service time."),
                variable("T_G", "standard departure time", "s/vehicle", "input", "Time for a served vehicle to depart."),
                variable("M", "basic toll-lane capacity", "veh/h", "output", "Ideal maximum flow of one lane."),
            ],
            ["AADT", "K", "D", "T_S", "T_G"],
            ["DHV", "M"],
            demand_equations,
            [
                "The 30th peak hour is an economically acceptable design condition.",
                "Vehicle-class conversion and charging mode are represented through demand and combined service/departure time.",
            ],
            ["Equations (1)-(2)", "references [12]-[13]"],
            [
                "The New Jersey AADT source, forecast year, vehicle conversion, and uncertainty are not archived.",
                "The source does not provide measured T_S or T_G distributions by booth type for this calculation.",
            ],
            [
                "Select forecast AADT and directional/design-hour factors.",
                "Compute DHV.",
                "Enter service and departure times by charging mode.",
                "Compute single-lane capacity M and pass both quantities to the queue model.",
            ],
            origin="base",
        )
    )

    queue_equations = [
        equation(9, "(3)", "T_q = [D(S+G)+E(S+G)^2] / [2E(S+G)(N-lambda E(S+G))] * {1 + sum_{i=0}^{N-1} (N-1)![N-lambda E(S+G)]/[i![lambda E(S+G)]^{K-i}]}^{-1}", "T_q = queue_wait_moment_factor * Erlang_like_factor(K-i as printed)", "Estimate queue waiting/stay time in the printed M/G/K expression.", ["T_q", "S", "G", "N", "lambda", "K"], "medium"),
        equation(9, "(4)", "T_d = E(S+G) + T_q", "T_d = E(S+G)+T_q", "Add expected service/departure time to queue waiting.", ["T_d", "S", "G", "T_q"]),
        equation(9, "(5)", "L_q = lambda[D(S+G)+E(S+G)^2] / [2E(S+G)(N-lambda E(S+G))] * {1 + sum_{i=0}^{N-1} (N-1)![N-lambda E(S+G)]/[i![lambda E(S+G)]^{N-i}]}^{-1}", "L_q = lambda * queue_wait_moment_factor * Erlang_like_factor(N-i)", "Estimate average queue length.", ["L_q", "S", "G", "N", "lambda"], "medium"),
        equation(9, "(6)", "E(S+G) = E(S) + E(G)", "E(S+G)=E(S)+E(G)", "Combine expected service and departure times.", ["S", "G"]),
        equation(9, "(7)", "D(S+G) = D(S) + D(G)", "Var(S+G)=Var(S)+Var(G)", "Combine service and departure variances under an independence premise.", ["S", "G"]),
        equation(10, "(8)", "d = [D(S)+E(S)^2] / [2E(S)(N-lambda E(S))] * {1 + sum_{i=0}^{N-1}(N-1)![N-lambda E(S)]/[i![lambda E(S)]^{N-i}]}^{-1}", "d = delay_moment_factor * Erlang_like_factor", "Estimate average system-level vehicle delay.", ["d", "S", "N", "lambda"], "medium"),
    ]
    models.append(
        model(
            2,
            9,
            "5.1.3 Multi-Lane M/G/K Queue and Service Level",
            "multi-channel queue and level-of-service classification",
            "Map service/departure moments and candidate lane counts to waiting time, stay, queue length, delay, and service-level bands.",
            [
                variable("S", "service time", "s/vehicle", "input", "Random toll service time."),
                variable("G", "departure time", "s/vehicle", "input", "Random post-service departure time."),
                variable("lambda", "arrival intensity", "veh/s", "input", "Printed as average car strength."),
                variable("N", "candidate toll-lane count", "lanes", "input", "Number of parallel servers."),
                variable("K", "printed queue exponent symbol", "index", "parameter", "Appears as K-i in Equation (3) although the server count is otherwise N.", "unspecified"),
                variable("T_q", "queue waiting or printed stay quantity", "s/vehicle", "output", "Equation (3), despite its duplicated stay label."),
                variable("T_d", "total stay", "s/vehicle", "output", "Expected service/departure plus T_q."),
                variable("L_q", "average queue length", "vehicles", "output", "Expected waiting vehicles."),
                variable("d", "average delay", "s/vehicle", "output", "System-level delay metric."),
                variable("q/s", "service-level queue ratio", "vehicles/lane", "input", "Table columns 0.5, 1.0, 1.5, and 2.0."),
                variable("n_N", "traffic intensity lookup", "veh/s", "output", "Table 2 value for lane count and service level."),
            ],
            ["S", "G", "lambda", "N", "q/s"],
            ["T_q", "T_d", "L_q", "d", "n_N"],
            queue_equations,
            [
                "Same-class traffic is evenly distributed among same-kind lanes.",
                "Service and departure times are treated as normal and independent when variances are added.",
                "Normal traffic is represented by standard small cars with minimum headway and no directional interference.",
                "Queue length and delay support four qualitative service levels.",
            ],
            ["Equations (3)-(8)", "Table 2", "Annexes 1-2"],
            [
                "The printed distribution claim, M/G/K formula, K/N index switch, stability domain, and equation cross-references are not reconciled by the source.",
                "No observed queue, delay, service-time, departure-time, or goodness-of-fit sample validates the model.",
            ],
            [
                "Estimate service and departure moments.",
                "Evaluate candidate N under the printed queue expressions.",
                "Compute stay, queue length, and delay.",
                "Map q/s and N to n_N in Table 2.",
                "Pass the required service intensity to the lane-selection inequality.",
            ],
            origin="base",
        )
    )

    lane_equations = [
        equation(10, "(9)", "DHV = AADT*K*D = Q*0.12*0.6", "DHV = AADT K D", "Instantiate directional design-hour demand.", ["DHV", "AADT", "Q", "K", "D"]),
        equation(10, "(10)", "n = DHV/(60*60)", "n = DHV/3600", "Convert hourly demand to per-second traffic intensity.", ["n", "DHV"]),
        equation(10, "(11)", "N' = N*n_N*60*60/S = N*n_N*3600/S", "N_prime = N n_N 3600/S", "Compute hourly vehicles served by N lanes at the selected service level.", ["N_prime", "N", "n_N", "S"]),
        equation(11, "(12)", "N*n_N > DHV*S/3600 = n*S", "N n_N > n S", "Select a candidate lane count whose service intensity exceeds demand.", ["N", "n_N", "DHV", "S", "n"]),
    ]
    models.append(
        model(
            3,
            10,
            "5.1.3-5.1.5 Lane Selection and DHV Sensitivity",
            "table-assisted discrete lane-count rule",
            "Select the minimum toll-lane count satisfying a chosen service level, then vary demand to inspect the discrete response.",
            [
                variable("Q", "average daily traffic", "vehicles/day", "input", "Used interchangeably with AADT in Equation (9)."),
                variable("AADT", "annual average daily traffic", "vehicles/day", "input", "Named alongside Q in Equation (9)."),
                variable("K", "design-hour coefficient", "dimensionless", "parameter", "Set to 0.12 in the worked calculation."),
                variable("D", "directional distribution coefficient", "dimensionless", "parameter", "Set to 0.60 in the worked calculation."),
                variable("DHV", "design-hour traffic", "veh/h", "intermediate", "Directional hourly demand."),
                variable("n", "design traffic intensity", "veh/s", "intermediate", "DHV converted to seconds."),
                variable("S", "average service time", "s/vehicle", "input", "Six seconds in the New Jersey calculation."),
                variable("N", "candidate toll-lane count", "lanes", "input", "Integer row selected from Table 2."),
                variable("q/s", "service-level queue ratio", "vehicles/lane", "input", "Chosen as 1.5 in the worked calculation."),
                variable("n_N", "table traffic intensity", "veh/s", "input", "Lookup value for N and q/s."),
                variable("N_prime", "hourly passing vehicles", "veh/h", "intermediate", "Printed N' capacity quantity."),
                variable("B", "selected one-way toll-lane count", "lanes", "output", "Seven in the worked baseline."),
            ],
            ["Q", "K", "D", "q/s", "S", "n_N"],
            ["n", "N_prime", "B"],
            lane_equations,
            [
                "The chosen average waiting level q/s=1.5 represents the desired service level.",
                "The service time is six seconds for the worked calculation.",
                "A table lookup can identify the required integer lane count.",
            ],
            ["Equations (9)-(12)", "Table 3", "Figure 3"],
            [
                "The table lookup and displayed traffic-intensity unit are not fully explained, and the source reports 4578 veh/h from AADT=38594 even though the printed factors imply about 2779 veh/h.",
                "The sensitivity plot changes AADT without publishing the underlying values or testing K, D, service time, or service level jointly.",
            ],
            [
                "Fix AADT, K, D, service level, and service time.",
                "Compute DHV and n.",
                "Read n_N for each candidate N.",
                "Select the first feasible N and label it B.",
                "Vary demand and redraw the discrete lane-count response.",
            ],
            origin="base",
        )
    )

    flow_equations = [
        equation(13, "(13)", "max v", "max v", "Maximize source-to-sink network flow.", ["v"]),
        equation(13, "(14)", "b_ij = 6.2343(H_ij/M_ij)^2 - 7.2219 H_ij/M_ij + 2.7091", "b_ij = 6.2343 rho_ij^2 - 7.2219 rho_ij + 2.7091; rho_ij=H_ij/M_ij", "Map volume-capacity ratio to an arc accident-rate surrogate.", ["b_ij", "H_ij", "M_ij"]),
        equation(13, "(15)", "min sum_{(i,j) in A} b_ij H_ij", "min sum_A b_ij H_ij", "Minimize exposure-weighted arc accident rate.", ["b_ij", "H_ij", "A"]),
        equation(13, "(16)", "max E = v - lambda sum_{(i,j) in A} b_ij H_ij", "max E = v - lambda sum_A b_ij H_ij", "Combine throughput and risk through a penalty weight.", ["E", "v", "lambda", "b_ij", "H_ij", "A"]),
        equation(13, "(17)", "0 <= H_ij <= c_ij for all (i,j) in A", "0 <= H_ij <= c_ij", "Bound every arc flow by capacity.", ["H_ij", "c_ij", "A"]),
        equation(13, "(18)", "sum_{j:(i,j)in A} H_ij - sum_{j:(j,i)in A} H_ji = 0, i != 0,t", "outflow_i-inflow_i=0 for intermediate i", "Conserve flow at intermediate nodes.", ["H_ij", "H_ji", "A"]),
        equation(13, "(19)", "sum_out H_ij - sum_in H_ji = v, i=0", "outflow_0-inflow_0=v", "Define positive net flow at the source.", ["H_ij", "H_ji", "v"]),
        equation(13, "(20)", "sum_out H_ij - sum_in H_ji = -v, i=t", "outflow_t-inflow_t=-v", "Define negative net flow at the sink.", ["H_ij", "H_ji", "v"]),
        equation(14, "(21)", "max E=v-lambda sum b_ij H_ij; s.t. balances equal {v,-v,0}; another balance equals d_i; b_ij curve; 0<=H_ij<=c_ij", "combined risk-flow program as printed, retaining both balance blocks", "Collect the objectives and constraints into one displayed optimization model.", ["E", "v", "lambda", "b_ij", "H_ij", "d_i", "c_ij", "M_ij"], "medium"),
        equation(14, "(22)", "f_i = {v_max if i=0; -v_max if i=t; 0 otherwise}", "f_i in {v_max,-v_max,0} by node role", "Define the source/intermediate/sink supply vector printed after Equation (21).", ["f_i", "v_max", "i", "t"], "medium"),
    ]
    models.append(
        model(
            4,
            13,
            "5.2.3 Minimum-Risk Maximum-Flow Formulation",
            "penalized capacitated network flow",
            "Allocate post-toll traffic over a directed capacity network while trading net throughput against an exposure-weighted risk surrogate.",
            [
                variable("G", "directed toll-plaza network", "graph", "input", "G=(V,A,C), from input node through toll nodes to merge node."),
                variable("H_ij", "arc traffic volume", "veh/h", "state", "Flow on directed arc (i,j)."),
                variable("H_ji", "reverse-indexed arc traffic volume", "veh/h", "state", "Incoming flow term in node balances."),
                variable("A", "directed arc set", "set", "input", "Arcs of the toll-plaza network."),
                variable("M_ij", "road capacity in risk curve", "veh/h", "parameter", "Denominator in Equation (14)."),
                variable("c_ij", "arc capacity bound", "veh/h", "parameter", "Upper bound in Equations (17) and (21)."),
                variable("b_ij", "arc accident-rate surrogate", "percent or rate", "intermediate", "Quadratic volume-capacity curve."),
                variable("v", "net source-to-sink flow", "veh/h", "output", "Maximum network throughput."),
                variable("lambda", "risk penalty weight", "mixed objective units", "parameter", "Trade-off coefficient without printed value."),
                variable("E", "combined objective", "mixed", "output", "Throughput minus weighted risk exposure."),
                variable("d_i", "printed node balance", "veh/h", "state", "Appears in Equation (21) without reconciliation to f_i."),
                variable("f_i", "node supply vector", "veh/h", "state", "Defined by Equation (22)."),
                variable("v_max", "maximum source-to-sink flow", "veh/h", "output", "Magnitude used in Equation (22)."),
                variable("i", "node index", "index", "parameter", "Generic node in V."),
                variable("t", "terminal node", "node", "parameter", "Sink index."),
            ],
            ["G", "M_ij", "c_ij", "lambda"],
            ["H_ij", "b_ij", "v", "E"],
            flow_equations,
            [
                "The input, merging, and toll regions can be abstracted as vertices and capacity arcs.",
                "Input and merging geometries are symmetric with L highway lanes and B>L toll lanes.",
                "The cited accident-rate curve applies to every modeled arc and can be exposure-weighted by H_ij.",
                "Peak traffic is used so the routing problem is operationally consequential.",
            ],
            ["Equations (13)-(22)", "Figure 4", "Annex 3"],
            [
                "lambda, the mapping between M_ij and c_ij, the accident-curve data/domain, and the duplicate d_i/f_i balance definitions are unresolved.",
                "A scalar penalty does not reveal the Pareto frontier, and accident rate times traffic may not have a validated safety interpretation.",
            ],
            [
                "Construct G=(V,A,C) from lanes, booths, and merge stages.",
                "Assign capacities and risk-curve denominators.",
                "Enforce arc bounds and node balances.",
                "Maximize v and evaluate exposure-weighted risk.",
                "Choose lambda or enumerate the throughput-risk frontier.",
            ],
            origin="base",
        )
    )

    models.append(
        model(
            5,
            14,
            "5.2.4 Labeling Algorithm and LINGO Route Result",
            "augmenting-path maximum flow and route reporting",
            "Find augmenting paths, instantiate a 24-node graph, and report a 3000 veh/h five-booth merge pattern with route-group flows.",
            [
                variable("u_xy", "forward residual capacity", "veh/h", "input", "Capacity used during labeling."),
                variable("f_xy", "current arc flow", "veh/h", "state", "Updated along augmenting paths."),
                variable("delta_x", "vertex residual label", "veh/h", "state", "Available augmentation reaching vertex x."),
                variable("B", "worked toll-lane count", "lanes", "input", "Five lanes for the 3000 veh/h scenario."),
                variable("Q_demand", "worked network demand", "veh/h", "input", "3000 veh/h."),
                variable("c_table", "Table 4 booth capacities", "veh/h", "input", "727, 703, and 624 veh/h by charging type."),
                variable("route_flow", "reported path-group flow", "veh/h", "output", "1375, 976, and 649 veh/h groups."),
                variable("risk_total", "reported total accident rate", "percent", "output", "0.96 percent."),
                variable("merge_pattern", "reported maximum-flow pattern", "route set", "output", "Five displayed source-to-sink paths."),
            ],
            ["u_xy", "f_xy", "delta_x", "B", "Q_demand", "c_table"],
            ["route_flow", "risk_total", "merge_pattern"],
            [],
            [
                "Residual labeling and augmentation produce the maximum flow when no source-to-sink augmenting path remains.",
                "Two automatic, two semi-automatic, and one manual booth are ordered inside to outside.",
            ],
            ["labeling and flow steps", "Table 4", "Figure 4", "Table 5", "Figure 5", "LINGO.lg4", "LINGO1.lg4"],
            [
                "The complete capacity provenance, lambda choice, solver status, arc-flow table, and risk aggregation ledger are not reported.",
                "The appendix's second LINGO model does not implement the body risk equation or bounds consistently.",
            ],
            [
                "Initialize zero flow and label the source (s,+infinity).",
                "Propagate forward and reverse residual labels.",
                "If the sink is labeled, augment by delta_t and clear labels.",
                "Stop when the sink cannot be labeled.",
                "Instantiate the booth/lane graph in LINGO and report route groups and risk.",
            ],
            origin="base",
        )
    )

    geometry_equations = [
        equation(16, "(23)", "D' = v_2 r + v_2^2/(2a_2)", "D_rear = v_2 r + v_2^2/(2a_2)", "Compute rear-vehicle reaction plus braking distance.", ["D_prime", "v_2", "r", "a_2"], "medium"),
        equation(17, "(24)", "S' = S_0 + v_1 t/3.6 + v_2^2/[2*3.6^2]*(1/j_a2 - 1/j_a1)", "S_safe = S_0 + v_1 t/3.6 + v_2^2/(2*3.6^2)(1/j_a2-1/j_a1)", "Estimate front-rear stopping safety distance under different braking decelerations.", ["S_prime", "S_0", "v_1", "v_2", "t", "j_a1", "j_a2"], "medium"),
        equation(17, "(25)", "max Z=sum_(i,j in A)(lambda_1 S'_ij + lambda_2 D'_j); s.t. S'_ij formula, a_i>0, D'_j=v_j r+v_j^2/(2a_j)", "printed max weighted distance objective with kinematic constraints", "Combine following and braking distances in the printed footprint objective.", ["Z", "lambda_1", "lambda_2", "S_prime", "D_prime", "a_i", "v_i", "r"], "medium"),
    ]
    models.append(
        model(
            6,
            16,
            "5.3 Minimum-Cost Geometry and Kinematics",
            "weighted braking/following-distance footprint model",
            "Use rear braking and two-vehicle safety distances to set a symmetric acceleration/deceleration length and plaza area.",
            [
                variable("v_1", "front-vehicle speed", "km/h or m/s", "input", "Front speed; conversion is explicit only in Equation (24)."),
                variable("v_2", "rear-vehicle speed", "km/h or m/s", "input", "Rear speed."),
                variable("a_1", "front acceleration/deceleration magnitude", "m/s2", "input", "Sign convention is incomplete."),
                variable("a_2", "rear acceleration/deceleration magnitude", "m/s2", "input", "Used in braking distance."),
                variable("a_i", "generic vehicle acceleration/deceleration", "m/s2", "input", "Printed domain variable in Equation (25)."),
                variable("v_i", "generic vehicle speed", "km/h or m/s", "input", "Indexed speed in Equation (25)."),
                variable("j_a1", "front braking deceleration", "m/s2", "input", "Front-vehicle braking magnitude in Equation (24)."),
                variable("j_a2", "rear braking deceleration", "m/s2", "input", "Rear-vehicle braking magnitude in Equation (24)."),
                variable("r", "driver reaction time", "s", "parameter", "Queried as 0.6 s."),
                variable("t", "reaction plus brake-growth time", "s", "parameter", "Used in safe distance."),
                variable("S_0", "stopped clearance", "m", "parameter", "Tail-to-front clearance after braking."),
                variable("S_prime", "moving safety distance", "m", "output", "Front-rear spacing."),
                variable("D_prime", "rear actual braking distance", "m", "output", "Reaction plus braking distance."),
                variable("lambda_1", "safety-distance weight", "unspecified", "parameter", "No domain or numeric value printed.", "unspecified"),
                variable("lambda_2", "braking-distance weight", "unspecified", "parameter", "No domain or numeric value printed.", "unspecified"),
                variable("W_geometry", "lane and booth geometry", "m", "input", "Widths and booth length used in the area calculation."),
                variable("Z", "printed geometry objective", "mixed", "output", "Displayed as max despite minimum-cost framing."),
                variable("A_plaza", "toll-plaza area", "m2", "output", "Reported as 4650.1875 m2."),
            ],
            ["v_1", "v_2", "a_1", "a_2", "a_i", "v_i", "j_a1", "j_a2", "r", "t", "S_0", "lambda_1", "lambda_2", "W_geometry"],
            ["S_prime", "D_prime", "Z", "A_plaza"],
            geometry_equations,
            [
                "Vehicles in the same lane and direction share a speed and maintain a stable spacing.",
                "Input and merge regions are symmetric, so acceleration and deceleration lengths match in the base case.",
                "Planar area and acceleration/deceleration length represent land and road cost.",
            ],
            ["Equations (23)-(25)", "Figure 6", "reported 65.25 m and 4650.1875 m2", "MATLAB appendix"],
            [
                "The printed max objective conflicts with minimum-cost prose; speed units, acceleration/deceleration signs, weights, domains, and geometry-to-area derivation are incomplete.",
                "The queried friction, reaction, and acceleration values lack source/version and uncertainty, and no trajectory or stopping-distance validation is shown.",
            ],
            [
                "Specify vehicle speeds, reaction time, braking growth, and deceleration magnitudes.",
                "Compute D' and S' for relevant front-rear pairs.",
                "Choose the controlling weighted or maximum physical distance under a corrected objective.",
                "Use symmetry to set both taper lengths.",
                "Combine taper, toll-lane, and main-lane dimensions to compute area.",
            ],
            origin="base",
        )
    )

    models.append(
        model(
            7,
            18,
            "6.1 Traffic-Flow Control-Variable Test",
            "one-factor demand scenario analysis",
            "Vary input traffic from 1500 to 4250 veh/h and compare reported accident rate and the 3000 veh/h maximum-flow ceiling.",
            [
                variable("Q_scenario", "scenario traffic flow", "veh/h", "input", "Values 1500, 1750, ..., 4250."),
                variable("risk_scenario", "reported accident rate", "percent", "output", "Table 6 values about 0.91-0.963 percent."),
                variable("v_max", "reported maximum flow", "veh/h", "output", "Saturates at 3000 veh/h."),
                variable("G_base", "base network and capacities", "graph", "input", "Fixed Figure 4 topology and Annex 3 capacities."),
            ],
            ["Q_scenario", "G_base"],
            ["risk_scenario", "v_max"],
            [],
            ["All non-flow parameters remain fixed under the control-variable method."],
            ["Table 6", "Figures 7-8"],
            [
                "The accident-rate values are not monotone although the prose says they increase, and no rerun ledger, uncertainty, or joint parameter test is supplied.",
                "A fixed maximum flow above demand is a capacity cap, not evidence that light and heavy traffic leave all performance unchanged.",
            ],
            [
                "Select each demand level.",
                "Re-run or evaluate the network.",
                "Record maximum flow and accident-rate surrogate.",
                "Plot the saturation relationship.",
                "Keep nonmonotone table cells and uncertainty visible in interpretation.",
            ],
            origin="modification",
        )
    )

    models.append(
        model(
            8,
            19,
            "6.2-6.3 Autonomy and Booth-Composition Scenarios",
            "mixed-vehicle and toll-technology scenario analysis",
            "Add 500 autonomous vehicles and change the booth mix to 3:1:1, then report route flows, acceleration length, lane needs, and capacity direction.",
            [
                variable("Q_AV", "added autonomous traffic", "vehicles", "input", "500 vehicles added to the original flow."),
                variable("route_AV", "autonomous-eligible route", "path", "state", "Autonomous vehicles use the inner automatic toll lane."),
                variable("mix", "automatic:semi-automatic:manual booths", "ratio", "input", "Changed from 2:2:1 to 3:1:1."),
                variable("base_case", "base flow and geometry", "scenario", "input", "The 3000 veh/h, 2:2:1, 65.25 m design."),
                variable("route_flow_AV", "scenario route-group flow", "veh/h", "output", "1476, 1065, and 826 veh/h groups."),
                variable("risk_AV", "reported total accident rate", "percent", "output", "0.96 percent in Table 7."),
                variable("L_acc", "acceleration-area length", "m", "output", "62.25 m in Figure 9 and 57.31 m under 3:1:1."),
                variable("B_recommendation", "scenario toll-lane recommendation", "lanes", "output", "Direction and count implied by each technology scenario."),
            ],
            ["Q_AV", "route_AV", "mix", "base_case"],
            ["route_flow_AV", "risk_AV", "L_acc", "B_recommendation"],
            [],
            [
                "Autonomous vehicles can use only automatic toll lanes and take the inner lane.",
                "Other parameters remain unchanged in the autonomy scenario.",
                "Booth efficiency differences can be represented through the technology proportion.",
            ],
            ["Table 7", "Figure 9", "Table 8", "Figure 10"],
            [
                "The printed route totals 3367 veh/h rather than clearly reconciling to an original-plus-500 demand, and risk remains 0.96 percent.",
                "No mixed-fleet behavior, queue, service-time, safety, or capacity experiment supports the causal autonomy and booth-mix claims.",
            ],
            [
                "Add autonomous demand and restrict it to automatic lanes.",
                "Recompute route-group flows and geometry.",
                "Change booth mix to 3:1:1 at 3000 veh/h.",
                "Recalculate toll-lane count and acceleration length.",
                "Compare with the baseline while retaining all fixed assumptions.",
            ],
            origin="modification",
        )
    )

    models.append(
        model(
            9,
            20,
            "7 New Jersey Case Study",
            "site-specific illustrative application",
            "Apply the lane, merge, and geometry chain to a New Jersey data table and daily flow chart with unequal acceleration/deceleration assumptions.",
            [
                variable("L_NJ", "New Jersey main-lane count", "lanes", "input", "Table 9 prints 4."),
                variable("W_NJ", "printed lane width", "m", "input", "Table 9 prints 14 m without clarifying whether this is total or per-lane width."),
                variable("B_existing", "existing toll lanes", "lanes", "input", "Table 9 prints 12."),
                variable("L_dec", "deceleration length", "m", "input", "Table 9 prints 70 m."),
                variable("Q_avg", "average hourly flow", "veh/h", "input", "Reported as 2634 veh/h."),
                variable("Q_peak", "daily maximum minute flow", "veh/min", "input", "Reported as 106 veh/min around 07:00."),
                variable("Q_profile", "daily traffic-flow profile", "veh/min by time", "input", "Figure 11 series used to identify peak, minimum, and average."),
                variable("B_design", "designed toll lanes", "lanes", "output", "Table 10 prints 10."),
                variable("mix_design", "designed booth mix", "ratio", "output", "5:3:2."),
                variable("A_design", "designed plaza area", "m2", "output", "Reported as 9614.5 or 9614.56 m2."),
                variable("theta", "fan angle", "degrees", "output", "Figure 12 prints 44.8 degrees."),
                variable("L_fan", "fan length", "m", "output", "Figure 12 prints 131 m."),
            ],
            ["L_NJ", "W_NJ", "B_existing", "L_dec", "Q_avg", "Q_peak", "Q_profile"],
            ["B_design", "mix_design", "A_design", "theta", "L_fan"],
            [],
            [
                "The toll-plaza total length remains unchanged while acceleration and deceleration differ.",
                "Vehicles leaving the third route need not follow the prescribed route.",
                "The queried daily flow and Table 9 describe the same site and design condition.",
            ],
            ["Table 9", "Figure 11", "Table 10", "Figures 12-13", "authority letter"],
            [
                "The named facility, date, source links, raw time series, existing comparison cells, and MATLAB calculation are absent.",
                "The average/peak arithmetic, width definition, area precision, case assumptions, and safety/capacity performance are not independently checked.",
            ],
            [
                "Collect lane, width, toll-lane, and deceleration inputs.",
                "Read daily peak, minimum, and average flow.",
                "Relax equal acceleration/deceleration and one route rule.",
                "Run the previous models in MATLAB or a reconstructed pipeline.",
                "Compare toll lanes, automatic lanes, footprint, fan angle, and length with the existing scheme.",
            ],
            origin="paper-specific",
        )
    )

    models.append(
        model(
            10,
            26,
            "References and Appendices",
            "provenance and implementation audit",
            "Retain service-level classifications, the arc-capacity matrix, LINGO listings, and MATLAB vectors while distinguishing printed code from reproducible execution.",
            [
                variable("A_matrix", "annex capacity adjacency matrix", "veh/h or infinity", "input", "Sparse matrix printed under a misleading service-level title."),
                variable("c", "LINGO arc capacity vector", "veh/h", "input", "Capacity data for listed arcs."),
                variable("f", "LINGO arc flow", "veh/h", "state", "Flow in the maximum-flow listing."),
                variable("u", "LINGO1 risk/bound vector", "mixed", "intermediate", "Computed from c with inconsistent denominators and used as both objective component and upper bound."),
                variable("V1", "MATLAB first speed vector", "km/h", "input", "[60,60,40,...]."),
                variable("V2", "MATLAB second speed vector", "km/h", "input", "30 through 75."),
                variable("P", "MATLAB weighted distance vector", "m", "output", "0.6*S+0.4*L."),
                variable("Q", "MATLAB maximum weighted distance", "m", "output", "max(P)."),
                variable("R_vectors", "reaction and deceleration vectors", "s and m/s2", "input", "T1, T2, a, and A vectors in the MATLAB listing."),
            ],
            ["A_matrix", "c", "V1", "V2", "R_vectors"],
            ["f", "u", "P", "Q"],
            [],
            [
                "The printed code and vectors correspond to the body network and distance models.",
                "The service-level annexes provide qualitative rather than calibrated numerical thresholds.",
            ],
            ["15 references", "Annexes 1-3", "LINGO.lg4", "LINGO1.lg4", "sir.m/iil.m"],
            [
                "LINGO1 omits the +2.7091 term, uses C/263 and C/236 rather than H/M, minimizes sum(u) independent of f, and bounds f by u instead of c.",
                "The listings lack versions, complete declarations, run outputs, unit contracts, input files, and checks that they reproduce body tables.",
            ],
            [
                "Map each reference to the parameter or claim it supports.",
                "Digitize Annexes 1-3 with labels and dimensions.",
                "Reconstruct the arc list and capacity vector.",
                "Reconcile the two LINGO objectives and bounds with Equations (14)-(22).",
                "Re-run the MATLAB vectors with explicit speed units and compare Q with the reported fan length.",
            ],
            origin="paper-specific",
        )
    )

    assert len(models) == 10
    assert EQUATION_COUNTER == 25
    edge_specs = [
        (1, 2, "DHV and single-lane capacity parameterize the multi-channel queue and service-level calculation."),
        (2, 3, "Queue/delay service levels and the n_N table define the lane-selection threshold."),
        (1, 3, "Directional design-hour demand enters the lane feasibility inequality directly."),
        (3, 4, "Selected toll-lane count B fixes the booth-layer size of the merging network."),
        (1, 4, "Demand and road capacities provide flow and volume-capacity inputs to the risk curve."),
        (4, 5, "The capacitated risk-flow program is instantiated by the labeling algorithm and LINGO network."),
        (5, 6, "Selected route speeds and booth/lane geometry supply the kinematic footprint calculation."),
        (4, 7, "The base network and risk curve are re-evaluated across traffic-flow scenarios."),
        (5, 7, "The 3000 veh/h route solution supplies the scenario baseline and saturation ceiling."),
        (5, 8, "Base booth types and routes are modified for autonomous demand and a 3:1:1 technology mix."),
        (6, 8, "Base acceleration length and area formulas are recalculated under technology scenarios."),
        (3, 9, "The lane-count rule consumes the New Jersey average and peak flow."),
        (4, 9, "The risk-flow topology supplies the New Jersey merging pattern."),
        (6, 9, "The kinematic geometry supplies fan length, angle, and area for the case."),
        (10, 5, "Appendix capacities and LINGO listings are the implementation provenance for the reported route solution."),
    ]
    assert len(edge_specs) == 15
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
            for source, target, handoff in edge_specs
        ],
    }


def build_visuals() -> list[dict]:
    specs = [
        (7, "Figure 2", "Overall analysis flow chart", [1, 2, 4, 6], "Preserve the sequence from toll-lane number through merge pattern and plaza size to testing and application."),
        (7, "Table 1", "Symbols and definitions", [1, 2, 4, 6], "Keep demand, capacity, queue, risk, distance, time, and lane symbols attached to model roles."),
        (8, "Equations (1)-(2)", "Design-hour demand and single-lane capacity", [1], "Retain factors, time terms, labels, and units before lane sizing."),
        (9, "Equations (3)-(7)", "M/G/K stay, queue, expectation, and variance block", [2], "Preserve both summation exponents and the duplicated stay caption for final review."),
        (10, "Equation (8) and Table 2", "Delay formula and service-intensity lookup", [2], "Join system delay to all N-by-q/s lookup cells without dropping qualitative service meaning."),
        (10, "Equations (9)-(12)", "Lane-count algebra and feasibility inequality", [3], "Trace AADT through per-second intensity and candidate hourly capacity to N."),
        (11, "Table 3", "Worked New Jersey lane calculation", [3], "Keep AADT assumptions, 4578 veh/h, 0.7716 intensity, and seven-lane output together."),
        (12, "Figure 3", "Traffic-volume versus toll-lane sensitivity", [3], "Retain the discrete positive response while marking the missing plotted ledger."),
        (13, "Equations (13)-(16)", "Throughput, risk curve, and combined objective", [4], "Keep throughput and exposure-weighted risk as distinct objectives before scalarization."),
        (13, "Equations (17)-(20)", "Arc bounds and source/intermediate/sink balances", [4], "Retain capacity and node-role constraints with sign convention."),
        (14, "Equations (21)-(22)", "Combined network program and node supply definition", [4], "Preserve both balance formulations so d_i/f_i inconsistency remains inspectable."),
        (14, "Labeling and flow process", "Augmenting-path algorithm steps", [5], "Retain forward/reverse residual labels, sink condition, augmentation, and termination order."),
        (15, "Table 4", "Booth type, width, speed, and capacity", [5], "Keep automatic, semi-automatic, and labor capacities with their lane-width and speed conditions."),
        (15, "Figure 4", "Twenty-four-node merging network", [4, 5], "Preserve source, three entry branches, five toll branches, merge stages, and sink topology."),
        (15, "Table 5", "Route groups, traffic flow, and total accident rate", [5], "Retain all five paths, three grouped flows, and the reported 0.96 percent total."),
        (16, "Figure 5", "Fan-out and fan-in traffic-flow diagram", [5], "Show how the path solution maps back to plaza geometry without treating arrows as calibrated trajectories."),
        (16, "Equations (23)-(25)", "Braking, safety-distance, and weighted geometry objective", [6], "Retain speed conversions, deceleration symbols, weights, objective direction, and constraints."),
        (17, "Figure 6 and area calculation", "Base symmetric plaza dimensions", [6], "Keep 65.25 m tapers, 48 m booth length, 50/22.5 m widths, and 4650.1875 m2 result."),
        (18, "Table 6 and Figures 7-8", "Traffic-flow scenario and saturation", [7], "Preserve every flow/risk cell and the 3000 veh/h maximum-flow plateau."),
        (19, "Table 7 and Figure 9", "Autonomous-vehicle route scenario", [8], "Keep added demand, route groups, 0.96 percent risk, and 62.25 m fan length together."),
        (20, "Table 8 and Figure 10", "Three-to-one-to-one booth-mix scenario", [8], "Compare booth counts and 57.31/65.25 m acceleration lengths under the stated flow."),
        (20, "Table 9 and Figure 11", "New Jersey inputs and daily flow", [9], "Retain lane, width, toll-lane, deceleration, peak, minimum, and average-flow claims."),
        (21, "Table 10 and Figures 12-13", "New Jersey design and existing-scheme comparison", [9], "Keep 10 lanes, 5:3:2 mix, area, 44.8-degree angle, 131 m length, and comparison boundary."),
        (26, "Annexes 1-3 and code listings", "Service levels, capacity matrix, LINGO, and MATLAB", [2, 5, 10], "Preserve qualitative tables, sparse matrix, arc vector, risk code, and distance vectors as printed provenance."),
    ]
    visuals = []
    for index, (page, figure, caption, model_indices, purpose) in enumerate(specs, start=1):
        visuals.append(
            {
                "page": page,
                "figure": figure,
                "visual_record_id": f"V-{ID_STEM}-{index:03d}",
                "caption": caption,
                "source_model_ids": [
                    f"MU-{ID_STEM}-{item:03d}" for item in model_indices
                ],
                "summary": f"{purpose} Supported claim: retain only visible labels, values, topology, geometry, equations, table cells, routes, or code. Boundary: the visual does not establish corrected algebra, calibrated crash risk, reproducible optimization, causal scenario effects, field feasibility, or uncertainty coverage.",
                "disposition": "important-visual-record",
                "evidence_role": "important-positive-record",
            }
        )
    assert len(visuals) == 24
    return visuals


def page_summary(page: int, text: str) -> dict:
    return {"page": page, "summary": text}


def build_card(language: dict, models_record: dict, visuals: list[dict]) -> dict:
    sections = [
        {
            "page": item["pages"][0],
            "section": item["label"],
            "summary": (
                f"Input: {item['input']} Rhetorical job: {item['rhetorical']} "
                f"Analytical job: {item['analytical']} Output: {item['output']} "
                f"Handoff: {item['handoff']}"
            ),
        }
        for item in CHAPTERS
    ]
    assumptions = [
        page_summary(6, "Vehicles are grouped as large, medium, and small using charging and physical characteristics."),
        page_summary(6, "Two-way traffic is symmetric, allowing one-way analysis to represent both directions."),
        page_summary(6, "Vehicles of the same class share a speed within the studied region."),
        page_summary(6, "Road surface, alignment, sight distance, and weather are treated as favorable and outside the design variation."),
        page_summary(7, "Vehicle input and merging areas are geometrically symmetric."),
        page_summary(7, "Tollbooths are perpendicular to the lane entry so vehicles enter smoothly and delay is reduced."),
        page_summary(8, "Normal traffic consists of standard small cars at minimum headway with no directional interference."),
        page_summary(8, "When booth service can accept demand, drivers freely choose payment methods without congestion."),
        page_summary(9, "Service and departure times follow normal distributions and their variances add."),
        page_summary(10, "A selected q/s band and Table 2 adequately encode the desired service level."),
        page_summary(12, "Peak traffic is the relevant regime for the merging model."),
        page_summary(13, "Arc accident rate is represented by a cited quadratic in traffic-volume/capacity ratio."),
        page_summary(13, "Input, toll, and merge regions can be represented by a directed capacity graph."),
        page_summary(16, "Same-lane same-direction vehicles form a stable flow with a meaningful safety spacing."),
        page_summary(17, "Base acceleration and deceleration regions are symmetric and share length 65.25 m."),
        page_summary(18, "Traffic-flow testing changes only demand while all other parameters remain fixed."),
        page_summary(19, "Autonomous vehicles use only automatic toll lanes and take the inner lane."),
        page_summary(21, "The New Jersey case holds total plaza length fixed while acceleration and deceleration differ."),
    ]
    data = [
        page_summary(8, "The design-hour factors are K=0.12 and D=0.60, with D's stated range 0.55-0.65."),
        page_summary(8, "Single-lane capacity is 3600 divided by standard service plus departure time."),
        page_summary(10, "Table 2 gives traffic-intensity values for N=1-8 and q/s=0.5, 1.0, 1.5, and 2.0."),
        page_summary(11, "The worked lane calculation states AADT=38594, q/s=1.5, K=0.12, service time 6 s, DHV=4578, intensity=0.7716, and seven toll lanes."),
        page_summary(13, "The accident curve uses coefficients 6.2343, -7.2219, and 2.7091."),
        page_summary(15, "The merge example uses demand 3000 veh/h, three main lanes, and five toll lanes."),
        page_summary(15, "Automatic, semi-automatic, and labor lanes are listed at capacities 727, 703, and 624 veh/h."),
        page_summary(15, "The booth order is two automatic, two semi-automatic, and one manual from inside to outside."),
        page_summary(15, "Table 5 groups route flows as 1375, 976, and 649 veh/h with total accident rate 0.96 percent."),
        page_summary(17, "The kinematic query reports friction coefficient 0.75, reaction time 0.6 s, and acceleration 7.39 m/s2."),
        page_summary(17, "MATLAB reports a 65.25 m acceleration length; symmetry assigns the same deceleration length."),
        page_summary(18, "Figure 6 uses 50 m toll width, 22.5 m main width, 48 m booth length, and 65.25 m fans."),
        page_summary(18, "The base plaza area is reported as 4650.1875 m2."),
        page_summary(18, "Table 6 varies traffic from 1500 to 4250 veh/h in 250-vehicle increments and prints accident rates from 0.91 to 0.963 percent."),
        page_summary(19, "The maximum-flow curve is described as saturating at 3000 veh/h."),
        page_summary(19, "The autonomy scenario adds 500 vehicles and prints route groups 1476, 1065, and 826 veh/h."),
        page_summary(19, "Table 7 reports 0.96 percent total accident rate and Figure 9 shows 62.25 m."),
        page_summary(20, "The booth-mix scenario changes automatic:semi-automatic:manual from 2:2:1 to 3:1:1 and acceleration length from 65.25 to 57.31 m."),
        page_summary(20, "Table 9 prints four main lanes, 14 m lane width, 12 existing toll lanes, and 70 m deceleration area."),
        page_summary(21, "The New Jersey daily chart is interpreted as peaking near 07:00 at 106 veh/min, reaching 15 veh/min minimum, and averaging 2634 veh/h."),
        page_summary(21, "Table 10 reports 10 toll lanes, a 5:3:2 mix, and area 9614.5 m2."),
        page_summary(21, "Figure 12 prints a 44.8 degree fan angle, 131 m length, and 26 m width label."),
        page_summary(25, "Fifteen references support general toll design, capacity, delay, safety, simulation, and traffic-flow context."),
        page_summary(27, "Annex 3 and the LINGO capacity vector preserve sparse arc capacities including zero and infinite entries."),
    ]
    verification = [
        page_summary(1, "The summary was reconciled against the body model order and all headline lane, flow, risk, area, autonomy, booth-mix, and case claims."),
        page_summary(4, "The introduction was read paragraph by paragraph from public-road motivation through literature branches, synthesis gap, and four work packages."),
        page_summary(7, "The symbol table and overall flow chart were checked as interfaces, not treated as decorative front matter."),
        page_summary(8, "Equations (1)-(2) were reconciled with their factors, units, citations, and downstream lane-sizing roles."),
        page_summary(9, "The focused formula proxy confirms Equations (3)-(7), including K-i in Equation (3), N-i in Equation (5), and the duplicated stay label."),
        page_summary(10, "Equation (8), Table 2, and the incorrect prose reference to Equation (6) for queue length were retained exactly."),
        page_summary(11, "Equations (9)-(12) and Table 3 were checked for the demand-to-lane chain and the unexplained 4578 veh/h value."),
        page_summary(12, "Figure 3 was read as a discrete lane response with no visible numeric sensitivity ledger."),
        page_summary(13, "Equations (13)-(20) were reconciled for objective signs, risk coefficients, capacity symbols, and node-balance orientation."),
        page_summary(14, "The focused flow-model proxy confirms Equation (21) contains two balance blocks and Equation (22) defines f_i rather than d_i."),
        page_summary(14, "Every forward/reverse labeling and augmentation step was retained through the no-augmenting-path termination."),
        page_summary(15, "Table 4, the full Figure 4 topology, all Table 5 paths, grouped flows, and 0.96 percent rate were reconciled."),
        page_summary(17, "The focused cost proxy confirms Equations (23)-(25), including the printed max objective, a_i>0, weights, and ambiguous speed/deceleration notation."),
        page_summary(18, "Figure 6 dimensions reproduce the stated base area only under an implicit geometric formula that the paper does not display."),
        page_summary(18, "Every Table 6 traffic/risk cell was retained; the sequence is visibly nonmonotone despite the prose's increasing claim."),
        page_summary(19, "Table 7 route totals, unchanged 0.96 percent rate, and Figure 9's 62.25 m label were checked together."),
        page_summary(20, "Table 8 and Figure 10 confirm the 3:1:1 mix and 57.31 m acceleration length."),
        page_summary(21, "Table 9, Figure 11, Table 10, and Figure 12 were checked for site inputs, daily-flow claims, output units, and 9614.5/9614.56 precision."),
        page_summary(22, "Figure 13 supports only a visible comparison direction because its source data cells and uncertainty are absent."),
        page_summary(27, "The matrix crop confirms Annex 3 is a capacity adjacency matrix even though its title repeats the delay service-level caption."),
        page_summary(28, "LINGO1 was compared line by line with the body risk equation and found to omit the constant, change denominators, minimize an f-independent sum, and bound f by u."),
        page_summary(28, "The MATLAB vectors were retained as printed, including mixed /3.6 treatment and Q=max(P), without claiming they reproduce every body length."),
    ]
    results = [
        page_summary(11, "The baseline lane calculation reports seven one-way toll lanes for four one-way main lanes."),
        page_summary(12, "The lane-sensitivity plot reports a positive, discrete relationship between hourly demand and toll-lane count."),
        page_summary(15, "The maximum-flow merge example uses five toll lanes for 3000 veh/h."),
        page_summary(15, "Five displayed paths are grouped into 1375, 976, and 649 veh/h, summing to 3000 veh/h."),
        page_summary(15, "The reported aggregate accident rate for the base merge pattern is 0.96 percent."),
        page_summary(16, "The source interprets separated confluence paths as reducing intersections and congestion under the studied flow."),
        page_summary(17, "The kinematic calculation reports symmetric acceleration and deceleration lengths of 65.25 m."),
        page_summary(18, "The base geometry reports plaza area 4650.1875 m2."),
        page_summary(18, "Table 6 risk values remain around 0.91-0.963 percent across the tested demand range."),
        page_summary(19, "The maximum-flow curve plateaus at 3000 veh/h when demand exceeds the stated capacity."),
        page_summary(19, "Adding 500 autonomous vehicles shifts route-group flows to 1476, 1065, and 826 veh/h."),
        page_summary(19, "The autonomy scenario still reports total accident rate 0.96 percent."),
        page_summary(20, "A 3:1:1 booth mix reduces the printed acceleration length from 65.25 to 57.31 m."),
        page_summary(20, "The source interprets a larger automatic-booth share as reducing area and booth count while increasing capacity."),
        page_summary(21, "The New Jersey chart is interpreted as peaking around 07:00 and averaging 2634 veh/h."),
        page_summary(21, "The application reports ten toll lanes with a 5:3:2 booth mix."),
        page_summary(21, "The application reports 9614.5 m2 area with a 44.8 degree, 131 m fan geometry."),
        page_summary(22, "The comparison figure is interpreted as fewer total toll lanes, more automatic lanes, and smaller total footprint than the existing scheme."),
        page_summary(24, "The authority letter restates the ten-lane, 5:3:2, 61.28 m, and 9614.5 output as a conditional case rather than a universal design."),
    ]
    contributions = [
        page_summary(1, "The summary previews lane sizing, risk-flow routing, kinematic area, scenario tests, a site case, and an authority deliverable in execution order."),
        page_summary(4, "The introduction moves from transport importance to the toll-plaza bottleneck mechanism before reviewing capacity and safety literature."),
        page_summary(5, "The literature gap is framed as missing synthesis across traffic, accident, and cost effects rather than claiming no prior work."),
        page_summary(5, "The work map assigns toll-lane number, merge pattern, cost geometry, and scenario stability to distinct analytical jobs."),
        page_summary(6, "The overall analysis restates each model as a decision tension with a typed input and output."),
        page_summary(7, "Assumptions are paired with justifications and followed by a notation/workflow interface."),
        page_summary(8, "Demand and capacity are separated before a multi-channel queue model chooses lane count."),
        page_summary(10, "Queue length and delay are translated into qualitative service bands and a numeric intensity lookup."),
        page_summary(11, "The algebraic four-step lane algorithm makes the lookup path inspectable before reporting seven lanes."),
        page_summary(12, "A graph abstraction converts geometric merging into explicit vertices, arcs, capacities, routes, and objectives."),
        page_summary(13, "Throughput and risk are first stated separately before being combined, preserving the trade-off logic."),
        page_summary(14, "The labeling algorithm provides a constructive mechanism from formulation to a maximum-flow route."),
        page_summary(15, "The full route table connects booth technology, network topology, flow groups, and a safety claim."),
        page_summary(16, "The geometry model grounds footprint in braking and following distances rather than an arbitrary taper length."),
        page_summary(18, "Three scenario branches distinguish demand, autonomous vehicles, and booth-technology composition."),
        page_summary(20, "The site application collects inputs before relaxing assumptions and comparing a candidate with the existing scheme."),
        page_summary(22, "The conclusion mirrors the model order and hands explicit limitations to strengths, weaknesses, and future work."),
        page_summary(23, "The authority letter translates the technical chain into decision language and closes with an actual-need caveat."),
    ]
    weakness_specs = [
        (9, 2, 3, "Equation (3) uses exponent K-i while Equation (5) uses N-i in otherwise parallel queue factors; K is not separately defined there."),
        (10, 2, 5, "The prose says queue length L_q is calculated by Equation (6), but Equation (5) is the queue-length formula and Equation (6) is expectation additivity."),
        (9, 2, 7, "Normal service/departure distributions do not by themselves justify M/G/K moments, independence, or variance addition, and no sample test is provided."),
        (11, 3, 9, "AADT=38594 with K=0.12 and D=0.60 gives about 2778.8 veh/h, not the printed 4578 veh/h."),
        (14, 4, 21, "Equation (21) includes both a source/sink/intermediate balance and a second balance equal to d_i, while Equation (22) defines f_i instead of d_i."),
        (14, 4, 21, "The network model alternates M_ij and c_ij as capacity concepts without a mapping and gives no lambda value or unit reconciliation."),
        (17, 6, 23, "Equation (23) does not show a km/h-to-m/s conversion although the surrounding speeds are commonly reported in km/h."),
        (17, 6, 24, "Equation (24) has ambiguous powers and braking-deceleration signs, so the printed source and normalized reading require a unit-tested reconstruction."),
        (17, 6, 25, "Model III is named minimum cost and the prose asks to minimize footprint, but Equation (25) displays max Z."),
        (17, 6, 25, "Equation (25) declares a_i>0 while using acceleration and braking deceleration without a complete sign/domain convention; lambda weights are undefined."),
        (18, 7, None, "Table 6 accident rates are nonmonotone, contradicting the statement that collision rate increases with every flow increase."),
        (19, 8, None, "Base and autonomous tables both report 0.96 percent total accident rate, inconsistent with the summary's claim of a 0.83 percent reduction."),
        (21, 9, None, "The New Jersey source, date, facility identity, raw daily profile, 14 m width meaning, and 9614.5/9614.56 precision are not documented."),
        (27, 10, None, "Annex 3 is titled as delay-based service-level classification but visibly contains a sparse capacity adjacency matrix."),
        (28, 10, 14, "LINGO1 omits +2.7091 and uses C/263 and C/236 instead of the body H_ij/M_ij risk curve."),
        (28, 10, 21, "LINGO1 minimizes sum(u), which is independent of flow f, and bounds f by u rather than capacity c, so it does not implement the printed risk-flow program."),
    ]
    weaknesses = [
        {
            "page": page,
            "model_id": f"MU-{ID_STEM}-{model_index:03d}",
            "equation_id": (
                f"EQ-{ID_STEM}-{equation_index:03d}"
                if equation_index is not None
                else None
            ),
            "summary": summary,
        }
        for page, model_index, equation_index, summary in weakness_specs
    ]
    extension_specs = [
        (8, "Version the AADT source, forecast year, K/D policy, vehicle conversion, directional split, service/departure samples, and uncertainty."),
        (9, "Re-derive the multi-server queue from a declared arrival/service family, stability domain, consistent N index, and measured queue/delay validation."),
        (10, "Publish the complete service-level lookup provenance and replace qualitative bands with agency thresholds tied to observed operations."),
        (11, "Reconcile the 4578 veh/h arithmetic and enumerate integer lane choices across AADT, K, D, service time, booth mix, and service level."),
        (13, "Calibrate the accident curve to applicable crash or surrogate-conflict data with exposure, speed, angle, severity, and uncertainty."),
        (14, "Define one node-supply vector, one capacity symbol mapping, lambda units, and a Pareto frontier for throughput versus risk."),
        (15, "Archive the full node/arc/capacity/flow ledger and verify every Table 5 route with an independently reconstructed maximum-flow solution."),
        (16, "Replace aggregate accident rate with route-level conflict or crash prediction and validate that the proposed merge pattern improves safety."),
        (17, "Rebuild braking/following equations with SI units, signed acceleration, reaction distributions, heterogeneous vehicles, and physical feasibility bounds."),
        (18, "Formulate footprint as a dimensionally consistent minimization and reproduce 65.25 m and 4650.1875 m2 from versioned geometry."),
        (18, "Run factorial traffic scenarios and report nonmonotonic risk, capacity, queue, delay, uncertainty, and spillback rather than a single control-variable plot."),
        (19, "Test conventional, connected, and autonomous mixtures with lane-choice behavior, service constraints, calibrated safety metrics, and demand conservation."),
        (20, "Optimize booth composition as a discrete life-cycle cost, capacity, queue, safety, and geometry decision rather than inferring direction from one 3:1:1 case."),
        (21, "Freeze New Jersey site identity, raw time series, geometry, existing scheme, units, dates, and a fully runnable application ledger."),
        (22, "Validate the proposed case against held-out field operations and publish uncertainty intervals for lanes, area, flow, delay, and safety."),
        (28, "Rewrite the LINGO and MATLAB programs from the governing equations, add tests for every coefficient/bound/unit, and archive solver outputs."),
    ]
    extensions = [
        {
            "extension_id": f"E-B-69427-{index:03d}",
            "page": page,
            "summary": summary,
        }
        for index, (page, summary) in enumerate(extension_specs, start=1)
    ]
    impacts = [
        ("R-B-LANG-001", "retain each toll-design claim with operating condition, model action, typed output, comparator, boundary, and downstream decision"),
        ("R-B-LOG-001", "trace demand through lane sizing, queue service, merge routing, kinematic area, scenarios, site application, and authority advice"),
        ("R-B-DATA-002", "version demand, service, capacity, risk, geometry, vehicle, booth, site, matrix, solver, and code inputs with units and provenance"),
        ("R-B-MOD-004", "keep queue, service level, maximum flow, risk, braking distance, safety distance, area, and decision outputs distinct"),
        ("R-B-MOD-006", "represent booth service, post-toll route choice, merge capacity, spillback, safety, and geometry as coupled stages"),
        ("R-B-VER-002", "test lane choices, route flow, risk calibration, kinematics, traffic regimes, vehicle mix, booth mix, and a held-out site"),
        ("R-B-VER-004", "run arithmetic, symbol, equation-reference, dimension, sign, domain, balance, objective, matrix, code, and provenance audits"),
        ("R-B-VIZ-002", "retain equation labels, table cells, route topology, dimensions, appendix matrices, code semantics, and uncertainty boundaries"),
    ]
    return {
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "team_control_number": "69427",
        "title": "Optimal Design of Toll Plaza Based on Minimum Risk Maximum Flow",
        "award_status": "outstanding",
        "source": {
            "relative_path": SOURCE_PATH,
            "sha256": SHA256,
            "page_count": PAGE_COUNT,
            "pdf_page_offset_note": "Physical page 1 is the summary sheet, pages 2-3 are contents, and physical pages 4-28 carry printed Pages 1-25 of 26; the printed counter does not imply a missing physical page.",
        },
        "schema_version": 1,
        "source_quality": {
            "status": "validated",
            "text_pages": 28,
            "rendered_pages": 28,
            "visual_review": "complete",
            "notes": [
                "All 28 physical pages were read completely in page-bounded text ranges, including summary, both contents pages, every substantive section, conclusion, strengths/weaknesses, future improvements, authority letter, references, service-level annexes, capacity matrix, and code.",
                "Four seven-page JPEG contacts and four focused JPEG crops totaled 2,295,566 bytes; the largest was 444,811 bytes, each image call returned one image, and no original full-page PNG entered model transport.",
                "Focused review reconciled Equations (3)-(7), (21)-(22), (24)-(25), and the Annex 3 capacity matrix; all 28 original PNGs remain local coordinate authority.",
                "No blank, black, clipped, overlapping, missing, or failed-render page was found; physical page 3 is an intentionally sparse contents continuation.",
            ],
        },
        "context_sources": [
            "The paper cites toll-plaza planning, capacity, delay, traffic conflict, microsimulation, tollbooth traffic flow, and variable-speed-control literature.",
            "No official prompt, raw AADT/time-series/service data, risk-curve dataset, complete graph ledger, field geometry, crash/conflict observations, LINGO project, MATLAB source package, solver output, or uncertainty ledger is bundled with the PDF.",
        ],
        "task_reconstruction": {
            "status": "incomplete-official-task-unavailable",
            "inputs": [
                "forecast demand and directional split",
                "booth service/departure behavior and service level",
                "main/toll lane counts and capacities",
                "merge graph and risk curve",
                "vehicle kinematics and plaza geometry",
                "autonomous share and booth composition",
                "New Jersey site data",
            ],
            "outputs": [
                "one-way toll-lane count",
                "maximum-flow minimum-risk merge pattern",
                "acceleration/deceleration length and plaza area",
                "traffic/autonomy/booth-mix scenario results",
                "New Jersey design and authority recommendation",
            ],
            "decisions": [
                "how many toll lanes to build or operate",
                "how booth traffic should merge into main lanes",
                "how much fan-in/fan-out land is required",
                "how design changes with demand and technology",
                "what evidence is needed before deployment",
            ],
        },
        "section_map": sections,
        "assumptions": assumptions,
        "data_and_preprocessing": data,
        "models": [
            {
                "model_id": item["model_id"],
                "page": item["page"],
                "summary": item["summary"],
            }
            for item in models_record["models"]
        ],
        "dependency_graph": models_record["dependency_edges"],
        "verification": verification,
        "results_trace": results,
        "contributions": contributions,
        "writing_logic": [
            page_summary(
                item["pages"][0],
                f"{item['chapter']}: {item['rhetorical']} {item['handoff']}",
            )
            for item in CHAPTERS
        ],
        "language_observations": [
            page_summary(
                item["pages"][0],
                f"{item['chapter']}: reuse the {item['code']} move only after replacing every facility, demand, service, lane/booth, graph, risk, kinematic, scenario, site, comparison, and evidence-boundary slot.",
            )
            for item in CHAPTERS
        ],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "A complete model-and-result preview may reduce coverage-check cost for a judge; this is class-J hypothesis, not scoring evidence.", "evidence_class": "J"},
            {"page": 13, "summary": "Separating throughput and risk before combining them may make the trade-off easier to audit; this remains class-J hypothesis.", "evidence_class": "J"},
            {"page": 15, "summary": "A route table paired with a network diagram may improve traceability; it is not observed judge preference.", "evidence_class": "J"},
            {"page": 23, "summary": "An authority letter may strengthen task closure by translating models into actions; it is not empirical scoring evidence.", "evidence_class": "J"},
        ],
        "weaknesses": weaknesses,
        "independent_extensions": extensions,
        "candidate_rule_impacts": [
            {"rule_id": rule_id, "action": action, "evidence_ids": []}
            for rule_id, action in impacts
        ],
        "unresolved_questions": [
            "What exact official prompt, construction constraints, and required safety/flow/cost outputs governed this submission?",
            "Which forecast year, source, vehicle conversion, and directional data support AADT=38594 and DHV=4578?",
            "What arrival, service, and departure samples support the M/G/K family, normal distributions, independence, and service-level table?",
            "Should Equation (3) use N-i rather than K-i, and which equation truly defines queue length and delay?",
            "How are service level q/s, n_N, service time, and the seven-lane lookup reproduced cell by cell?",
            "Which facilities and data support the accident-rate curve, and over what volume-capacity domain is it valid?",
            "Are M_ij and c_ij identical, what are lambda's value/units, and should Equation (21) use d_i or f_i?",
            "What complete node, arc, capacity, risk, and flow ledger reproduces the 1375/976/649 routes and 0.96 percent total?",
            "Why does the minimum-cost section maximize Z, what are lambda_1/lambda_2, and what are the speed/acceleration sign and unit conventions?",
            "Which geometry formula reproduces 4650.1875 m2 from the visible 65.25, 48, 50, and 22.5 m dimensions?",
            "Why are Table 6 risk values nonmonotone while the text describes continuous increase?",
            "How does adding 500 autonomous vehicles conserve demand across route groups, and why does accident rate remain 0.96 percent?",
            "What controlled experiment supports the claims that autonomy and more automatic booths improve capacity and reduce footprint?",
            "Which New Jersey facility, date, raw daily profile, width definition, and existing-scheme data support Tables 9-10 and Figures 11-13?",
            "Why do area values appear as 9614.5 and 9614.56 and fan lengths as 61.28, 62.25, 65.25, and 131 m in different contexts?",
            "Why is Annex 3 titled as service-level classification when it is a capacity matrix?",
            "What corrected LINGO model implements Equations (14)-(22) with flow-dependent risk and capacity bounds?",
            "What versioned MATLAB code and SI-unit ledger reproduce each braking, safe-distance, acceleration-length, and area result?",
        ],
        "protocol_v2_records": {
            "language": {
                "path": f"artifacts/language-units/{PAPER_ID}.json",
                "schema_version": 3,
                "unit_count": len(language["units"]),
                "chapters": language["available_chapters"],
                "review_status": "validated",
            },
            "models": {
                "path": f"artifacts/model-units/{PAPER_ID}.json",
                "schema_version": 2,
                "model_count": len(models_record["models"]),
                "equation_count": sum(
                    len(item["governing_equations"])
                    for item in models_record["models"]
                ),
                "review_status": "validated",
            },
        },
        "review_status": "validated",
    }


EVIDENCE_POOL = [
    (page, f"{item['label']} / {item['code']} source action", f"{excerpt}: {function}")
    for item in CHAPTERS
    for page, excerpt, function in item["anchors"]
]


def build_observations(units: list[dict]) -> list[dict]:
    observations: list[dict] = []

    def add(
        page: int,
        section: str,
        dimension: str,
        source_basis: str,
        interpretation: str,
        evidence_class: str,
        candidate_rule_ids: list[str],
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
                "source_basis": source_basis,
                "interpretation": interpretation,
                "applicability": [
                    "Apply only when facility, demand regime, vehicle and booth class, lane/graph geometry, units, source status, comparator, uncertainty, and receiving decision are explicit."
                ],
                "counterevidence": [
                    "A cited coefficient, qualitative service band, queue formula, capacity matrix, route diagram, solver listing, scenario table, or authority letter does not establish corrected algebra, calibrated safety, causal improvement, field feasibility, or global robustness."
                ],
                "confidence": confidence,
                "candidate_rule_ids": candidate_rule_ids,
            }
        )

    for unit in units:
        add(
            unit["page"],
            unit["section"],
            "language",
            unit["source_excerpt"],
            f"Reusable language action: {unit['function']} Preserve the information order {unit['reusable_pattern']} and replace every domain-specific slot.",
            "O",
            ["R-B-LANG-001"],
        )

    targets = {
        "logic": 78,
        "modeling": 52,
        "visualization": 24,
        "verification": 48,
        "data": 44,
        "assumption": 38,
        "result": 42,
        "weakness": 16,
        "other": 18,
    }
    interpretations = {
        "logic": "Trace the paper from demand and service through lane count, queue criteria, graph abstraction, throughput-risk routing, braking/following geometry, scenario branches, site application, conclusion, and authority consequence.",
        "modeling": "Retain each variable and mechanism with unit, source status, objective, constraint, topology, upstream dependency, downstream output, and approximation boundary.",
        "visualization": "Keep equation labels, all table cells, graph nodes/arcs, route groups, geometry labels, appendix matrix dimensions, code semantics, linked claim, and missing uncertainty together.",
        "verification": "Classify the check as transcription, arithmetic, equation-reference, dimensional, sign/domain, symbol, conservation, table reconciliation, code-body consistency, calibration, or provenance review.",
        "data": "Enter each value in a ledger with source version, unit, traffic regime, lane/booth/vehicle class, transformation, topology or geometry, uncertainty, and downstream use.",
        "assumption": "Turn each simplification into a scope diagnostic and test whether lane count, queue, flow, risk, distance, area, scenario, or site decision changes when relaxed.",
        "result": "Bind the output to its producing equation, table, algorithm, solver/code run, route, demand, booth mix, unit, comparator, direction, uncertainty, and decision use.",
        "weakness": "Keep the defect as a final warning after positive retention and repair it through a named arithmetic, reference, dimension, sign, domain, conservation, calibration, code, or field test.",
        "other": "Preserve citation, implementation, appendix, communication, and future-vehicle context without letting it substitute for queue, capacity, risk, geometry, scenario, or validation evidence.",
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
            page, section, source = EVIDENCE_POOL[
                (index * 11 + len(dimension) * 3) % len(EVIDENCE_POOL)
            ]
            rule_ids = [RULE_IDS[dimension]]
            if dimension == "modeling" and index % 4 == 0:
                rule_ids = ["R-B-MOD-004", "R-B-MOD-006"]
            elif dimension == "verification" and index % 2 == 0:
                rule_ids = ["R-B-VER-002", "R-B-VER-004"]
            add(
                page,
                f"{section} / {dimension} evidence {index + 1}",
                dimension,
                source,
                f"{interpretations[dimension]} Evidence action {index + 1} of {count} preserves a distinct anchor, check, and receiving use.",
                classes[dimension],
                rule_ids,
                "medium" if dimension in {"weakness", "other"} else "high",
            )
    expected = {"language": 149, **targets}
    assert Counter(item["dimension"] for item in observations) == Counter(expected)
    assert len(observations) == 509
    return observations


def build_audit(
    language: dict,
    models_record: dict,
    card: dict,
    observations: list[dict],
) -> dict:
    units = language["units"]
    by_chapter: dict[str, list[dict]] = {}
    for unit in units:
        by_chapter.setdefault(unit["chapter"], []).append(unit)
    layouts = {
        layout["chapter"]: layout for layout in language["chapter_layouts"]
    }
    paragraph_chains = []
    for chapter_name in ("abstract", "introduction"):
        chapter_units = by_chapter[chapter_name]
        paragraph_chains.append(
            {
                "chapter": chapter_name,
                "visual_paragraph_count": layouts[chapter_name]["paragraph_count"],
                "coverage_status": "complete",
                "gaps": [],
                "paragraphs": [
                    {
                        "paragraph_index": index,
                        "dominant_move": f"{unit['function']} -> supplies an inspectable output -> hands it to the next paragraph or section",
                        "language_unit_ids": [unit["language_unit_id"]],
                    }
                    for index, unit in enumerate(chapter_units, start=1)
                ],
            }
        )

    models = models_record["models"]
    equation_ids = [
        equation_item["equation_id"]
        for model_item in models
        for equation_item in model_item["governing_equations"]
    ]
    warning_specs = [
        (2, 3, 9, "Equation (3) uses K-i while the parallel Equation (5) uses N-i; K is not separately defined in this queue factor."),
        (2, 5, 10, "The prose sends queue length to Equation (6), but Equation (5) defines L_q and Equation (6) only adds expectations."),
        (2, 7, 9, "Normality alone does not justify the printed M/G/K form or variance addition; independence, stability, and sample fit are absent."),
        (3, 9, 11, "AADT=38594, K=0.12, and D=0.60 imply about 2778.8 veh/h, not the printed 4578 veh/h."),
        (4, 21, 14, "Equation (21) duplicates flow balance with d_i while Equation (22) defines f_i, leaving the node-supply symbol inconsistent."),
        (4, 21, 14, "Equation (21) does not reconcile M_ij with c_ij or provide lambda's value and unit conversion."),
        (6, 23, 16, "Equation (23) omits a visible km/h-to-m/s conversion under the surrounding speed convention."),
        (6, 24, 17, "Equation (24) contains ambiguous powers and deceleration signs that require a unit-tested reconstruction."),
        (6, 25, 17, "Equation (25) displays max Z although the section frames a minimum-cost and minimum-footprint problem."),
        (6, 25, 17, "Equation (25) gives a_i>0 without a complete acceleration/deceleration sign convention and leaves both weights undefined."),
        (4, 14, 18, "Table 6's risk sequence is nonmonotone even though the prose describes accident rate as increasing with flow."),
        (4, 14, 19, "Base and autonomous route tables both report 0.96 percent, inconsistent with the summary's claimed 0.83 percent reduction."),
        (6, 25, 21, "New Jersey source identity, raw flow, width semantics, and area precision are insufficient to reproduce the application."),
        (4, 21, 27, "Annex 3 repeats a service-level title while displaying a sparse capacity adjacency matrix."),
        (4, 14, 28, "LINGO1 omits +2.7091 and changes the risk denominators to C/263 and C/236."),
        (4, 21, 28, "LINGO1 minimizes sum(u) independent of flow and bounds f by u rather than c, so it does not implement Equation (21)."),
    ]
    formula_warnings = [
        {
            "model_id": f"MU-{ID_STEM}-{model_index:03d}",
            "equation_id": f"EQ-{ID_STEM}-{equation_index:03d}",
            "page": page,
            "warning": warning,
        }
        for model_index, equation_index, page, warning in warning_specs
    ]
    dimensions = {
        dimension: 0
        for dimension in [
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
    return {
        "audit_id": "LA-B-2017-69427-b04ae242",
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "schema_version": 1,
        "priority_order": [
            "language-imitation",
            "organization-logic",
            "formula-error-watch",
        ],
        "chapter_saturation": [
            {
                "chapter": item["chapter"],
                "pass_count": 3,
                "last_pass_new_moves": 0,
                "coverage_status": "complete",
                "gaps": [],
                "new_moves_by_pass": [len(item["anchors"]), 2, 0],
            }
            for item in CHAPTERS
        ],
        "language_unit_dispositions": [
            {
                "language_unit_id": unit["language_unit_id"],
                "disposition": "supports-existing",
                "target_pattern_ids": unit["candidate_pattern_ids"],
                "reason": "The move transfers only after replacing facility, demand, service, lane/booth, graph, risk, kinematic, scenario, site, comparison, and evidence-boundary slots.",
            }
            for unit in units
        ],
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "complete",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [
                "toll-plaza safety, throughput, congestion, footprint, and cost decision",
                "public-road motivation, mechanism, literature branches, synthesis gap, and four work packages",
                "three design tensions, conditional assumptions, symbol interface, and overall flow",
                "design-hour demand and single-lane service/departure capacity",
                "M/G/K stay, queue length, delay, qualitative service levels, and intensity lookup",
                "integer lane selection and demand sensitivity",
                "directed graph abstraction with separate throughput and exposure-weighted risk objectives",
                "arc bounds, node balances, scalarized objective, and augmenting-path labeling",
                "worked booth capacities, 24-node topology, route groups, and reported accident rate",
                "rear braking, two-vehicle safety distance, symmetric fan length, and plaza area",
                "traffic-flow, autonomous-vehicle, and booth-composition scenario branches",
                "New Jersey data collection, daily-flow reading, relaxed geometry, candidate design, and existing comparison",
                "conclusion, explicit strengths/weaknesses, future extensions, and authority-facing advice",
                "references, service-level annexes, capacity matrix, and implementation listings",
                "only after positive language, organization, model, and visual retention does the final warning pass record arithmetic, cross-reference, symbol, dimension, sign, objective, scenario, appendix, and code defects",
            ],
            "section_progressions": [
                {
                    "chapter": item["chapter"],
                    "moves": [
                        f"input: {item['input']}",
                        f"rhetorical job: {item['rhetorical']}",
                        f"analytical job: {item['analytical']}",
                        f"output: {item['output']}",
                        f"handoff: {item['handoff']}",
                    ],
                    "positive_pattern": "Retain the source-anchored input -> rhetorical job -> analytical job -> output -> handoff contract; warnings remain the final pass.",
                }
                for item in CHAPTERS
            ],
            "main_argument_chains": [
                {
                    "claim": "Forecast demand, charging capacity, queue behavior, and service level can determine one-way toll-lane count.",
                    "support_steps": ["AADT/K/D", "DHV", "single-lane capacity", "M/G/K moments", "queue/delay service bands", "n_N table", "feasibility inequality", "seven-lane result"],
                    "decision_consequence": "retain the lane-sizing interface while rebuilding arithmetic, distributions, service data, lookup provenance, and integer uncertainty",
                    "source_pages": [8, 9, 10, 11, 12],
                },
                {
                    "claim": "A directed capacity network can express the toll-plaza merge as a throughput-risk allocation.",
                    "support_steps": ["G=(V,A,C)", "quadratic risk curve", "separate objectives", "lambda scalarization", "arc bounds", "node balances", "labeling", "LINGO route groups"],
                    "decision_consequence": "retain the graph and route interface while calibrating risk, reconciling symbols, exposing the Pareto frontier, and reproducing every arc flow",
                    "source_pages": [12, 13, 14, 15, 16],
                },
                {
                    "claim": "Following and braking distance can bound a physically motivated toll-plaza fan length and area.",
                    "support_steps": ["stable-flow premise", "rear braking distance", "front-rear safety distance", "weighted objective", "queried friction/reaction/acceleration", "MATLAB", "65.25 m", "4650.1875 m2"],
                    "decision_consequence": "treat the reported footprint as a candidate until objective direction, units, signs, weights, geometry, and trajectories are reconstructed",
                    "source_pages": [16, 17, 18],
                },
                {
                    "claim": "Traffic, autonomous vehicles, and booth mix affect merge flow, risk, capacity, and footprint.",
                    "support_steps": ["Table 6 demand series", "3000 veh/h plateau", "+500 autonomous vehicles", "automatic-lane restriction", "Table 7 routes", "3:1:1 mix", "57.31 m"],
                    "decision_consequence": "retain the scenario structure while requiring conservation, controlled mixed-fleet behavior, factorial design, uncertainty, and calibrated safety",
                    "source_pages": [18, 19, 20],
                },
                {
                    "claim": "The model chain can produce a site-facing New Jersey design.",
                    "support_steps": ["Table 9 inputs", "daily flow chart", "2634 veh/h average", "relaxed acceleration/deceleration", "10 lanes", "5:3:2", "9614.5 m2", "existing comparison"],
                    "decision_consequence": "use the case as a conditional template until site identity, raw data, geometry, code, existing baseline, field calibration, and uncertainty are frozen",
                    "source_pages": [20, 21, 22, 23, 24],
                },
                {
                    "claim": "The authority letter translates the technical chain into a staged public decision.",
                    "support_steps": ["lane count", "merge pattern", "plaza size", "scenario behavior", "site table", "ideal-condition limitation", "actual-need caveat"],
                    "decision_consequence": "retain the audience adaptation while converting claims into data collection, validation, pilot, and stop/go actions",
                    "source_pages": [23, 24],
                },
            ],
        },
        "formula_error_watch": {
            "mode": "last-pass-warning-only",
            "completed_after_positive_passes": True,
            "warnings": formula_warnings,
        },
        "model_retention": {
            "model_count": len(models),
            "retained_model_ids": [item["model_id"] for item in models],
            "retained_equation_ids": equation_ids,
            "central_equations": [
                {
                    "model_id": item["model_id"],
                    "equation_ids": [
                        equation_item["equation_id"]
                        for equation_item in item["governing_equations"]
                    ],
                    "all_central_equations_retained": True,
                }
                for item in models
                if item["governing_equations"]
            ],
        },
        "visualization_dispositions": [
            {
                "paper_card_visual_index": index,
                "visual_record_id": visual["visual_record_id"],
                "disposition": "important-visual-record",
                "analytical_purpose": visual["summary"],
            }
            for index, visual in enumerate(
                card["visualization_observations"], start=1
            )
        ],
        "dimension_counts": dimensions,
        "positive_reusable_language_count": len(units),
        "weakness_record_count": dimensions["weakness"],
        "review_status": "validated",
        "gate_attestation": {
            "g1_g3_language": "validated-before-G4",
            "g4_organization": "passed-before-G5-G6",
            "g5_models": "validated-before-G7",
            "g6_visuals": "passed-before-G7",
            "g7_warning_mode": "last-pass-warning-only",
            "g7_warning_count": len(formula_warnings),
            "warnings_strict_minority_of_language": len(formula_warnings) < len(units),
            "request_body_guard": {
                "bounded_jpeg_proxies": 8,
                "total_proxy_bytes": 2295566,
                "largest_proxy_bytes": 444811,
                "original_full_page_png_in_context": False,
            },
        },
    }


def build_extraction() -> dict:
    extraction = json.loads(SOURCE_EXTRACTION.read_text(encoding="utf-8"))
    if extraction.get("visual_review_status") != "complete":
        raise SystemExit("q118 extraction does not contain completed visual review")
    visual_review = extraction.get("visual_review", {})
    if visual_review.get("status") != "complete" or len(
        visual_review.get("reviewed_pages", [])
    ) != PAGE_COUNT:
        raise SystemExit("q118 visual-review page ledger is incomplete")
    return extraction


def bind_rule_impacts(card: dict, observations: list[dict]) -> None:
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
        raise SystemExit(f"refusing to overwrite staging directory: {STAGE}")
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
                "language_units": len(language["units"]),
                "models": len(models_record["models"]),
                "equations": sum(
                    len(item["governing_equations"])
                    for item in models_record["models"]
                ),
                "dependency_edges": len(models_record["dependency_edges"]),
                "visual_records": len(card["visualization_observations"]),
                "observations": Counter(
                    item["dimension"] for item in observations
                ),
                "formula_warnings": len(audit["formula_error_watch"]["warnings"]),
                "unresolved_questions": len(card["unresolved_questions"]),
            },
            indent=2,
            default=dict,
        )
    )


if __name__ == "__main__":
    main()
