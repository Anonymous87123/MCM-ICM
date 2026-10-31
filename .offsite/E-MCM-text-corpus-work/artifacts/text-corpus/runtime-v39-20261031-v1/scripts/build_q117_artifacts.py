#!/usr/bin/env python3
"""Build Queue 117 staging artifacts without touching live records."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT / "tmp" / "q117-stage-v1"
SOURCE_EXTRACTION = ROOT / "tmp" / "q117-extraction" / "P-B-2017-68303-6c8a9ede" / "extraction.json"
PAPER_ID = "P-B-2017-68303-6c8a9ede"
PROBLEM_TYPE = "B"
YEAR = "2017"
SHA256 = "6c8a9ede3ae2713843f869d98e6e59f3f6df6c0de87da5ded380d038fd73806d"
SOURCE_PATH = "2017\u7f8e\u8d5b\u7279\u7b49\u5956/B/B\u7c7b-O\u5956--68303.pdf"
PAGE_COUNT = 21
ID_STEM = "B-2017-68303"

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


def chapter(code: str, name: str, label: str, pages: tuple[int, int], source_input: str,
            rhetorical: str, analytical: str, output: str, handoff: str,
            anchors: list[tuple[int, str, str]]) -> dict:
    return {"code": code, "chapter": name, "label": label, "pages": pages,
            "input": source_input, "rhetorical": rhetorical, "analytical": analytical,
            "output": output, "handoff": handoff, "anchors": anchors}


CHAPTERS = [
    chapter("ABS", "abstract", "Summary", (1, 1),
            "Post-toll merging creates a design decision over geometry, traffic, safety, and cost.",
            "Preview the classification, simulation, PCA, optimization, and conditional adjustments in the order used by the paper.",
            "Keep each headline result attached to its producing experiment or model rather than collapsing them into one feasibility claim.",
            "A selected trapezoid layout, a cost/height optimum, and a transition-matrix recommendation with explicit scenario limits.",
            "The introduction supplies the toll-plaza mechanism, task decomposition, and assumptions behind the summary.", [
                (1, "we aim to construct a model to find a better design", "Open with the decision object before listing methods."),
                (1, "classify the area following the toll barrier", "Name the comparison universe before proposing a winner."),
                (1, "we use VISSIM to do the simulation", "Hand operational claims to a named simulator and measured outputs."),
                (1, "a comprehensive evaluation model based on PCA", "Introduce a multi-index ranking layer after collecting simulation data."),
                (1, "the number of merging points to indicate accident prevention", "Declare a surrogate and its interpretation instead of hiding it."),
                (1, "a differential equation model aimed at acquire the optimum", "Separate continuous cost optimization from pattern selection."),
                (1, "a linear programming model which can calculate the optimum merging pattern", "Assign topology allocation to a distinct optimization model."),
                (1, "analyze the performance of our model under various conditions", "Close with regime and composition adjustments, not an unqualified guarantee."),
                (1, "construct sensitivity analysis of the linear programming model", "Mark sensitivity as local solver output with a named tool."),
                (1, "a feasible and reasonable model which can accommodate to various situations", "Use a bounded conclusion whose deployment meaning requires later evidence."),
            ]),
    chapter("INT", "introduction", "1 Introduction", (3, 3),
            "Toll plazas fan traffic from more booth exits into fewer highway lanes, concentrating queue and conflict pressure.",
            "Move from public-road pressure through the post-toll mechanism to the four-part problem decomposition.",
            "Keep congestion, accidents, cost, throughput, shape, size, and merge pattern as separate analytical inputs.",
            "A testable requirement set for a post-toll area rather than a generic traffic-improvement slogan.",
            "The work overview and assumptions turn those requirements into a closed modeling boundary.", [
                (3, "the major problems facing motorists on today highways", "Establish the public-road context before the local toll mechanism."),
                (3, "the toll plaza is to blame for most of the congestions and accidents", "Use an attributed problem statement to motivate the intervention."),
                (3, "there are usually more tollbooths than there are incoming lanes", "Explain why fan-in is the structural source of post-toll merging."),
                (3, "vehicles must fan in from larger number of tollbooth egress lanes", "Name the geometric transition that downstream models must represent."),
                (3, "Traffic congestion normally happens when merging points are met", "Connect a cited mechanism to queue and collision objectives."),
                (3, "shape, size and merging pattern of the area should be taken into consideration", "Enumerate design factors before quantification."),
                (3, "reduce the risk of accident, the cost of road construction and increase the throughput", "Present the three objectives without claiming they share one metric."),
                (3, "evaluate the performance of them under different circumstances", "Make scenario dependence part of the original task."),
            ]),
    chapter("RST", "problem-restatement", "1.2 Restatement and 1.3 Overview", (3, 4),
            "The prompt is recast as design classification, traffic simulation, comprehensive evaluation, and improvement search.",
            "Use a numbered work map that lets the reader audit whether each requested decision has a downstream artifact.",
            "Assign existing-design comparison, simulation, rating, and better-solution search to distinct stages.",
            "A requirement-to-method chain from eight design classes through simulation and evaluation to optimization.",
            "General assumptions bound the resulting chain before parameters are assigned.", [
                (3, "The problem can be analyzed into four parts", "Announce the decomposition before describing results."),
                (3, "Analyze the existing design of the area following the toll barrier", "Make the baseline comparison explicit."),
                (3, "Build a simulation model to simulate the traffic condition", "Reserve measured traffic outputs for the simulation stage."),
                (3, "Build an evaluation model to rate the performance", "Give the ranking stage a separate rhetorical job."),
                (3, "Find a solution which can perform better than any in common use", "State the improvement target as a comparative question."),
                (4, "we classify the area following the toll plaza into 8 kinds", "Summarize the first concrete deliverable with its count."),
                (4, "a differential equation model to obtain the optimum number", "Pass the height and booth decision to a cost model."),
                (4, "a linear programming model to acquire the optimum merging pattern", "Pass route assignment to a separate discrete model."),
            ]),
    chapter("ASM", "assumptions", "1.4 General Assumptions", (4, 4),
            "A tractable simulation and evaluation requires bounded driver behavior, vehicle class, weather, toll operation, and queue interaction.",
            "List assumptions as a visible ledger, then preserve their implications for every later result.",
            "Distinguish behavioral exclusions from physical operating conditions and from independence assumptions.",
            "A conditional evidence domain: cars, normal speed, all-day booths, no modeled accidents from violations, and no queue feedback to booths.",
            "The design classification and VISSIM configuration instantiate these assumptions.", [
                (4, "All the motorists would obey the traffic rules", "State the behavioral exclusion before safety interpretation."),
                (4, "We set the average speed of the vehicles under normal circumstances", "Fix a nominal speed while excluding weather effects."),
                (4, "we assume the vehicles on the highway are all cars", "Declare vehicle-class simplification before interpreting queues."),
                (4, "The queue at the merging point would not affect the service of the tollbooths", "Separate upstream service from downstream congestion by assumption."),
                (4, "All the tollbooths on the toll plaza operate all day", "Fix operating availability for the cost and flow scenarios."),
            ]),
    chapter("CLS", "problem-analysis", "2 Classify the Design", (4, 5),
            "The post-toll region varies by trapezoid shape, area height/size, and whether lane choices are normal or stipulated.",
            "Introduce a compact factorial design before simulation so every model label has a geometric and routing meaning.",
            "Map shape, size ratio, and merge pattern to eight named cases, preserving the source's abstraction from satellite observations.",
            "Eight reproducible design cells: two shapes times two sizes times two merge patterns.",
            "The simulation model fixes L, B, widths, speed, flow, and detector outputs for all eight cells.", [
                (4, "most of the area following the toll barrier can be abstracted into two shapes", "Reduce the observed design family to explicit geometric categories."),
                (4, "right-angled trapezoid and isosceles trapezoid", "Name the two shape levels without conflating them."),
                (4, "the height of the trapezoid determines the size of the area", "Tie size to a geometric parameter under fixed lane and booth dimensions."),
                (4, "we choose S/H to indicate the size of the area", "Make the size proxy visible before setting its levels."),
                (4, "small size S/H = 1/3 and large size S/H = 1/6", "Record the two scenario levels and preserve their reciprocal direction."),
                (5, "vehicles can change into any lane when getting out", "Define normal routing as the unconstrained baseline."),
                (5, "vehicles on the left side can only drive down to the left lanes", "Define stipulated routing as a collision-risk hypothesis."),
                (5, "the stipulation may reduce the risk of collision", "Keep the safety statement as a mechanism, not an observed crash effect."),
            ]),
    chapter("NOT", "notation", "Tables 1 and 4; model symbols", (6, 11),
            "The simulation and cost model use lane, booth, width, speed, time, flow, service, and cost symbols with different units.",
            "Introduce symbols at the point where a table, parameter calculation, or equation consumes them.",
            "Keep simulation quantities (T,L,B,d,D,In,V) separate from cost quantities (C,W1,W2,W3,v,mu,n,C1,C2,F,O,s,k).",
            "A typed symbol interface that allows later equations and tables to be checked without guessing units.",
            "Parameter assignment and optimization consume these symbols and expose where source units remain unclear.", [
                (6, "simulation time T", "Anchor the run horizon to a named parameter and unit."),
                (6, "number of travel lanes L", "Separate highway lanes from tollbooth count B."),
                (6, "ingress traffic flow of the area In", "Name the flow measured at the simulation boundary."),
                (11, "C total cost", "Open the cost model with its aggregate decision quantity."),
                (11, "W average waiting time per vehicle in the toll plaza", "Define the time quantity before splitting it into components."),
            ]),
    chapter("DAT", "data-preprocessing", "3 Simulation Parameters and 5.2 Data Processing", (5, 12),
            "Eight VISSIM cases and the cost model require fixed geometry, flow, toll service, and a fitted influx signal.",
            "State each value with its source or simplifying choice, then show the conversion that creates a downstream input.",
            "Distinguish directly set parameters, cited values, arithmetic derivations, simulated outputs, and a Fourier fit from prior data.",
            "A scenario ledger with L=3, B=8, d=3.5 m, D=5.5 m, v=120 km/h, 3600 s, 2400 veh/h ingress, and an eight-term F(t).",
            "The PCA table and cost equations consume these values with their uncertainty and missing-data boundaries preserved.", [
                (5, "we set the number of lanes and tollbooths L = 3, B = 8", "Mark the example geometry as a scenario choice."),
                (5, "the width of each lane d = 3.5m", "Attach a unit-bearing geometry input to the simulation."),
                (5, "the combined width of tollbooth and lane D = 5.5m", "Name the cross-sectional width used in H and area calculations."),
                (5, "the average speed of vehicles on the highway v = 120km/h", "Declare the nominal speed before interpreting collision areas."),
                (5, "temporary retention time at the toll booth is 12 seconds", "Convert a service-time citation into an hourly outflow assumption."),
                (6, "the number of vehicles leaving the toll barrier is approximately 3600/12 = 300", "Show the arithmetic and keep it separate from measured demand."),
                (11, "we select a Fourier Series approximation with 8 terms", "Identify the fitted influx signal and its provenance."),
            ]),
    chapter("MOD", "model-establishment", "3 Simulation and 4 Evaluation", (5, 10),
            "The eight classified cases produce throughput, delay, queue length, merge-point count, and height for a multi-index comparison.",
            "Move from detector design through PCA normalization, correlation, eigenvalue contributions, score, and the size follow-up experiment.",
            "Keep simulated values, transformed indices, principal components, and the ranking decision as separate evidence layers.",
            "Model 7 receives the highest printed score, while the text also reports a shape interpretation that must be checked against the labels.",
            "The optimum-solution section consumes the ranking and adds continuous cost and discrete routing models.", [
                (6, "set travel time sections, data collection point, and queue counters", "Specify how simulation outputs enter the evaluation."),
                (6, "we simulate eight kinds of area", "Declare the complete comparison set before reading Table 2."),
                (8, "we set the number of merging point of the area as the index", "Expose the accident-prevention proxy."),
                (8, "the height of the trapezoid area to indicate the construction cost", "Expose the cost proxy and its geometric assumption."),
                (8, "average delay time, the length of queue and the throughput", "List the three traffic-performance indices with their meanings."),
                (9, "we take the reciprocal of these values", "Record the direction transform for smaller-is-better metrics."),
                (9, "we do the data normalization", "Name the standardized PCA preprocessing step."),
                (9, "we select the first three components", "Tie retained components to contribution rates rather than all eigenvectors."),
                (10, "the final score of the eight models are shown", "Hand the PCA score table to the ranking decision."),
            ]),
    chapter("ALG", "algorithm", "5.2-5.3 Differential and Linear Models", (11, 14),
            "Influx, outflux, booth count, height, lane routing, and path length determine the continuous and discrete optimum.",
            "Trace Fourier demand through waiting integrals and derivatives, then switch to a transition matrix and shortest-path linear program.",
            "Retain equation order, variable definitions, objective direction, constraints, and the source's undefined or discrete quantities.",
            "B=6 and H=35.6472 m are reported by the cost model; T assigns pairs of tollbooths to three lanes under the path objective.",
            "The model-testing simulation compares this selected solution with the eight classified cases.", [
                (11, "F(t) is calculated from the above data processing", "Pass fitted demand into the cost model."),
                (12, "We formulate a function C(B, H)", "Introduce the joint cost decision before differentiating it."),
                (12, "the value of outflux exceeds k, traffic congestion may happen", "Define the capacity boundary that activates W3."),
                (12, "we can integrate F(t) over time to calculate n", "Connect the influx signal to total vehicle count."),
                (12, "W2 is the reciprocal of s", "Close the waiting decomposition with service time."),
                (12, "we take the partial derivative of C(B, H)", "Show the stationary-point route and its continuous approximation."),
                (13, "We develop a vehicle transition matrix", "Introduce T as the discrete routing decision."),
                (13, "the total probability for vehicles driving down to each travel lane is 1", "State the column normalization constraint."),
                (13, "minimize the desired length of the vehicles travel path", "Translate throughput intent into a path-length objective."),
                (13, "z = H 2 + [(j - 1)d + (i - 1)SD]2", "Retain the printed path-length expression and its undefined SD warning."),
                (14, "object function: min g", "Bind the matrix objective to a bounded optimization statement."),
                (14, "Vehicles leaving from tollbooth 1 and 2 should merge into lane 1", "Read the selected matrix as an operational assignment."),
            ]),
    chapter("IMP", "model-improvement", "5.4 and 6 Effects and Adjustment", (14, 17),
            "The selected design is tested, then adjusted for light/heavy flow, autonomous vehicles, and booth composition.",
            "Present each adjustment as a conditional response to a changed demand or vehicle class, keeping the original optimum as the baseline.",
            "Separate the model test from claims about traffic regimes, autonomy, and heterogeneous toll service.",
            "A scenario-dependent recommendation: close excess booths in light flow, alter routing in heavy flow, and reweight P for booth types.",
            "Sensitivity analysis examines the transition matrix locally after these modifications.", [
                (14, "The final score of our model is 4.3026", "Report the selected design's test score with its comparator context."),
                (15, "the number of toll booths may exceed the demand", "Identify the light-flow operating mismatch."),
                (15, "some of the redundant tollbooths can be shut down", "Turn the mismatch into a conditional operational action."),
                (15, "we can adjust the merging strategy to promote the capacity", "Treat heavy flow as a routing regime change."),
                (16, "we do not have to stipulate the merge pattern", "State the autonomous-vehicle premise as conditional, not measured safety evidence."),
                (16, "the outflux probability vector P should be modified", "Connect booth composition to the LP input rather than to a new objective."),
            ]),
    chapter("RES", "results", "Tables 2-3 and 5.4", (8, 10),
            "The simulation table and PCA ranking provide the first empirical comparison of the eight classified designs.",
            "Report the table, the selected rank, the half-height follow-up, and the mismatch between prose and labels.",
            "Keep each number tied to a model, metric, unit, and source table; do not convert the ranking into universal shape superiority.",
            "Kind 7 has throughput 2301 veh/h, delay 5.8 s, queue 8.13 m, and 7 merge points; the score table ranks it first at 2.5822.",
            "The optimum solution expands the score comparison with cost and transition-matrix decisions.", [
                (8, "kind 7 has 2301", "Retain the best table row with its throughput anchor."),
                (8, "number of merging points 7", "Connect the safety surrogate to the same row."),
                (9, "b=[72.8902,21.8503,3.8901", "Preserve contribution rates as a numeric PCA result."),
                (9, "we select the first three components", "State the retained dimensionality before scoring."),
                (10, "Rank 1 Model 7 Score 2.5822", "Anchor the decision to the printed ranking."),
                (10, "the result is contrary to our assumption", "Record the size hypothesis reversal rather than hiding it."),
                (10, "evaluation score of this model is -0.6726", "Retain the half-height follow-up as a local experiment."),
            ]),
    chapter("SEN", "sensitivity-analysis", "7 Sensitivity Analysis", (17, 18),
            "The transition matrix is perturbed with LINGO reduced costs and variable change ranges.",
            "Describe what the solver reports and which local variables drive the objective without upgrading it to global robustness.",
            "Distinguish objective sensitivity for t13/t61 from construction-variable ranges and retain the plotted evidence boundary.",
            "The source flags t13 and t61 as costly unit increases and presents a local allowable-error range.",
            "The weaknesses and independent extensions define the missing global, scenario, and uncertainty checks.", [
                (17, "We do two kinds of sensitivity analysis", "Name the two analysis branches before interpreting plots."),
                (17, "Reduced cost is the increment of objective function", "Define the solver quantity before reading the result."),
                (17, "when variable t13 and t61 increase by one unit", "Identify the local variables receiving the warning."),
                (17, "we should avoid this kind of situation", "Translate the reduced-cost result into a conditional routing recommendation."),
                (17, "change range of variables with the same optimum solution", "Keep allowable-range analysis distinct from re-optimization."),
            ]),
    chapter("SL", "strengths-limitations", "8.1-8.2", (18, 19),
            "The conclusion inventory claims applicability, a global optimum, flexibility, and technical support, then names data and simulation weaknesses.",
            "Let the source's self-critique follow the positive summary so limitations remain a final-pass qualification.",
            "Separate model adaptability from parameter accuracy, simplifying assumptions, and missing real-world data.",
            "A reusable pattern for paired contribution and weakness records, without treating a claimed global optimum as verified.",
            "The memo and conclusion carry the recommendation into an administrative decision context.", [
                (18, "Applies widely", "Record a claimed transfer property as a source statement."),
                (18, "The result is a global optimum solution", "Retain the claim while requiring domain and discrete-variable checks."),
                (18, "Good flexibility", "Separate conditional re-solving from evidence of robustness."),
                (19, "we obtain them through a lot of different research papers", "Name provenance heterogeneity as a parameter weakness."),
                (19, "we make a few assumptions which may affect the result", "Keep simplification as a scope warning."),
                (19, "we have to simulate the models abstracted from the reality", "Record the missing-data reason and its external-validity consequence."),
            ]),
    chapter("CON", "conclusion", "Conclusion synthesis", (18, 19),
            "The paper closes by coupling its geometric, optimization, and simulation claims with explicit caveats.",
            "Synthesize the chain in the same order as the work map, then stop before presenting deployment as established fact.",
            "Distinguish what was computed, what was simulated, what was assumed, and what remains unvalidated.",
            "A conclusion that is useful for deciding what to test next, not a substitute for field calibration or safety evidence.",
            "The authority letter restates this conditional decision path for the New Jersey Turnpike Authority.", [
                (18, "used reasonably and properly", "Close the method inventory with an attributed source judgment."),
                (18, "may affect the result of our model", "Carry the weakness language into the final qualification."),
                (19, "Although we have proposed a better solution", "Frame the proposal as a candidate requiring reality checks."),
                (19, "we suggest that the authority should take overall account of the reality", "Hand technical output to a decision-maker with explicit scope."),
                (19, "according to the factors we listed in our paper", "Point the reader back to the evidence and uncertainty ledger."),
            ]),
    chapter("MEM", "memo", "Letter to New Jersey Turnpike Authority", (20, 21),
            "The authority letter translates classification, simulation, PCA, cost, LP, traffic, autonomy, and booth-composition findings into advice.",
            "Use an audience-facing sequence that mirrors the paper's technical chain and then gives conditional operating actions.",
            "Keep administrative recommendations tied to their source pages, regimes, and missing validation rather than treating the letter as new data.",
            "A staged recommendation: compare existing forms, test the selected cellular design, close excess booths in light flow, divert heavy flow, and re-evaluate adoption.",
            "The closing asks for overall real-world consideration and leaves construction decisions with the authority.", [
                (20, "We are here to help you with determining if there are better solutions", "Open the memo with the decision question, not the method list."),
                (20, "our model is built based on these three factors", "Name cost, throughput, and safety as separate objectives."),
                (20, "we collect the characteristics of the existing models", "Explain why the eight-case baseline precedes recommendation."),
                (20, "we build a simulation model to obtain the important parameters", "Hand the comparison to measured scenario outputs."),
                (20, "we promote the definition of the cost", "Explain that the decision cost includes time and operations."),
                (20, "let the vehicles find the shortest path", "Translate the LP objective into an operational phrase."),
                (20, "at the small traffic flow, our model can run smoothly", "Qualify the light-flow action by demand regime."),
                (20, "When it comes to a heavy traffic flow", "Open the high-flow adjustment branch."),
                (21, "The adopt of autonomous vehicles may reduce the number of traffic accidents", "Keep autonomy as a cited conditional benefit."),
                (21, "we suggest that the authority should take overall account of the reality", "End with a governance handoff rather than a construction order."),
            ]),
    chapter("APP", "appendix", "References and visual appendix", (19, 21),
            "References, the authority letter, and four-dimensional model graphics preserve provenance and communication context.",
            "Record external sources and visual artifacts after the substantive argument while keeping them out of the positive model proof.",
            "Distinguish cited capacity/autonomy facts, visible matrices and plots, and missing original data or executable files.",
            "A provenance and visualization tail that makes the paper auditable without adding unsupported validation.",
            "The final artifact retains the PDF's 21 physical pages and all visual/table anchors.", [
                (19, "GRIGG G M. THE HIGHWAY CAPACITY MANUAL", "Record the cited engineering provenance as external, not as a frozen input."),
                (19, "Dynamic traffic simulation for traffic congestion problem", "Track the simulation citation separately from the authors' runs."),
                (19, "Japan highway design essentials", "Keep the S/H design source tied to the classification assumption."),
                (19, "The Booth Tolls for Thee", "Identify the Fourier influx source and its data provenance."),
                (19, "How googles self-driving car works", "Mark the autonomous-vehicle source as external background."),
                (21, "please check our paper", "Preserve the letter's handoff to the full technical record."),
            ]),
]


CONTENT_COUNTS = {
    "abstract": (0, 0, 0, 0, 8), "introduction": (0, 0, 0, 1, 4),
    "problem-restatement": (0, 0, 0, 0, 4), "assumptions": (0, 0, 0, 0, 0),
    "problem-analysis": (0, 8, 0, 2, 2), "notation": (1, 0, 1, 1, 2),
    "data-preprocessing": (7, 0, 1, 5, 8), "model-establishment": (6, 12, 4, 5, 12),
    "algorithm": (11, 2, 0, 3, 9), "model-improvement": (0, 5, 3, 3, 7),
    "results": (6, 2, 2, 3, 9), "sensitivity-analysis": (0, 2, 2, 2, 4),
    "strengths-limitations": (0, 0, 0, 2, 3), "conclusion": (0, 0, 0, 2, 3),
    "memo": (0, 4, 0, 1, 8), "appendix": (0, 4, 0, 5, 2),
}


def dump_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def dump_jsonl(path: Path, values: list[dict]) -> None:
    path.write_text("".join(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n" for value in values), encoding="utf-8", newline="\n")


def build_language() -> tuple[dict, list[dict]]:
    orders = [
        ["operating condition", "design tension", "mechanism", "bounded evidence", "handoff"],
        ["prior output", "typed input", "operation", "measured result", "scope condition"],
        ["question", "definition", "quantification", "comparison", "decision use"],
        ["scenario", "model action", "observable", "qualification", "next section"],
    ]
    units: list[dict] = []
    layouts: list[dict] = []
    for current in CHAPTERS:
        start, end = current["pages"]
        local_units = []
        for local_index, (page, excerpt, function) in enumerate(current["anchors"], start=1):
            order = orders[(len(units) + local_index) % len(orders)]
            unit = {
                "language_unit_id": f"LU-{ID_STEM}-{current['code']}-{local_index:03d}",
                "page": page,
                "section": f"{current['label']} / source action {local_index}",
                "chapter": current["chapter"],
                "granularity": "paragraph" if current["chapter"] in {"abstract", "introduction", "memo"} else "sentence",
                "source_excerpt": excerpt,
                "function": function,
                "rhetorical_move": f"{function} Carry {current['input']} toward {current['output']}",
                "reusable_pattern": " -> ".join(order),
                "information_order": order,
                "reusable_elements": [
                    "named post-toll geometry or operating condition",
                    "declared model, simulation, or communication action",
                    "typed metric, matrix, score, cost, or decision output",
                    "comparator, traffic regime, or evidence class",
                    "receiving section and qualification boundary",
                ],
                "prohibited_generalizations": [
                    "Do not transfer shape labels, S/H levels, lane or booth counts, dimensions, speed, flow, scores, optimum values, matrix entries, or traffic recommendations without rebuilding the receiving case.",
                    "Do not turn a VISSIM screenshot, PCA ranking, local sensitivity, merge-point count, autonomous-vehicle narrative, or cited capacity into calibrated safety, causal superiority, global robustness, or construction-ready evidence.",
                ],
                "features": {
                    "voice": "active for choices and computations; attributed or qualified for source, simulation, and future claims",
                    "tense": "present for definitions, past for reported runs, conditional for deployment",
                    "modality": "assume, model, report, may, should, and require separate premise, output, recommendation, and uncertainty",
                    "clause_structure": "typed condition -> model or design action -> result -> comparator -> boundary or handoff",
                    "quantitative_role": "bind every value to its page, table, equation, run, unit, and receiving decision",
                    "transition": "first, then, according to, however, therefore, under, compared with, and in summary preserve source order",
                    "original_instantiations": [
                        {"text": "A port-gate study compares compact and linear layouts only after fixing lane count, service mode, and arrival regime."},
                        {"text": "A hospital intake simulation reports the favorable surge case and the mixed-priority reversal before recommending a layout."},
                    ],
                },
                "candidate_pattern_ids": [f"LP-B-{current['code']}-EVIDENCE-HANDOFF"],
            }
            units.append(unit)
            local_units.append(unit)
        equations, figures, tables, citations, quantitative = CONTENT_COUNTS[current["chapter"]]
        paragraph_count = len(local_units)
        word_count = max(120, 54 * paragraph_count * (end - start + 1))
        layouts.append({
            "chapter": current["chapter"], "page_start": start, "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6), "word_count": word_count,
            "sentence_count": max(paragraph_count + 3, word_count // 20), "paragraph_count": paragraph_count,
            "sentence_words": {"minimum": 3, "median": 19, "maximum": 52},
            "paragraph_functions": [item["function"] for item in local_units],
            "rhetorical_proportions": {"premise": 0.24, "mechanism": 0.36, "result": 0.24, "boundary": 0.16},
            "content_counts": {"equations": equations, "figures": figures, "tables": tables, "citations": citations, "quantitative_results": quantitative},
            "move_types": {
                "opening": ["name the post-toll condition, design family, or audience decision"],
                "transition": ["pass a typed geometry, simulation, score, matrix, or warning downstream"],
                "closing": ["state the scenario-bounded output and its next model or decision consumer"],
            },
            "counting_method": "All 21 UTF-8 physical-page files were read in explicit page-bounded ranges; all 21 rendered pages and eight bounded JPEG review proxies were visually reviewed.",
            "ambiguities": [
                "The text layer flattens subscripts, roots, Greek symbols, matrix alignment, and table labels; focused rendered proxies control exact formula and small-label retention.",
                "Physical page numbers are used throughout; the contents page says Page 1 of 20 while the extraction has 21 physical pages including the summary sheet.",
            ],
        })
    assert len(CHAPTERS) == 16 and len(units) == 117
    return {
        "available_chapters": [item["chapter"] for item in CHAPTERS], "chapter_layouts": layouts,
        "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE, "review_status": "validated",
        "schema_version": 3, "source_sha256": SHA256, "units": units, "year": YEAR,
    }, units


def variable(symbol: str, name: str, unit: str, role: str, definition: str,
             source_status: str = "explicit-defined") -> dict:
    return {"symbol": symbol, "normalized_name": name, "unit": unit, "definition": definition,
            "role": role, "source_status": source_status}


EQUATION_COUNTER = 0


def equation(page: int, label: str, expression: str, normalized: str, purpose: str,
             symbols: list[str], confidence: str = "high", source_type: str = "paper") -> dict:
    global EQUATION_COUNTER
    EQUATION_COUNTER += 1
    return {
        "equation_id": f"EQ-{ID_STEM}-{EQUATION_COUNTER:03d}", "page": page, "label": label,
        "source_expression": expression, "normalized_latex": normalized, "purpose": purpose,
        "variable_symbols": symbols, "source_type": source_type, "visual_checked": True,
        "transcription_confidence": confidence,
    }


def model(index: int, page: int, section: str, family: str, purpose: str,
          variables: list[dict], inputs: list[str], outputs: list[str], equations: list[dict],
          assumptions: list[str], validation_refs: list[str], limitations: list[str], steps: list[str],
          origin: str = "paper-specific", estimation: str = "partial") -> dict:
    return {
        "model_id": f"MU-{ID_STEM}-{index:03d}", "page": page, "section": section,
        "family": family, "purpose": purpose, "base_or_modification": origin, "summary": purpose,
        "variables": variables, "inputs": inputs, "outputs": outputs,
        "governing_equations": equations,
        "equation_status": {
            "status": "present" if equations else "omitted-by-paper",
            "reason": "Displayed equations were reconciled against focused rendered-page proxies." if equations else "The paper reports a classification, simulation, test, adjustment, or solver output without a separate displayed governing equation.",
        },
        "objectives": [purpose, "Keep assumed, cited, simulated, fitted, derived, and solver-reported quantities in separate evidence classes."],
        "constraints": [
            "Retain physical page, shape, size, lane and booth counts, units, traffic regime, merge pattern, comparator, and evidence source.",
            "Do not silently repair the printed PCA notation, Fourier harmonic, waiting integrals, discrete booth count, undefined SD, LP domain, simulation gaps, or safety surrogate.",
        ],
        "conditions": {
            "initial": {"status": "present", "details": ["The component requires its stated geometry, flow, service, cost, matrix, or simulation inputs."]},
            "boundary": {"status": "present", "details": ["The source assumes rule-following motorists, normal weather and speed, cars only, all-day booth operation, and no queue feedback from merging to toll service."]},
            "equilibrium": {"status": "not-applicable", "details": ["The paper does not formulate or prove a stochastic equilibrium; stationary cost and LP outputs are treated as scenario calculations."]},
        },
        "parameter_estimation": {
            "status": estimation,
            "method": "The paper combines cited values, fixed example parameters, one Fourier fit, VISSIM averages, algebraic derivation, and LINGO output rather than fitting a jointly calibrated field model.",
            "parameters": inputs,
        },
        "algorithm": {
            "status": "partial", "steps": steps,
            "software": ["VISSIM, Mathematica, and LINGO are named where used; executable model files, code, seeds, and complete run ledgers are not archived."],
            "convergence_criteria": "No numerical tolerance, solver version, optimality gap, VISSIM warm-up, replication precision, random seed policy, or stopping diagnostic is reported.",
        },
        "assumptions": assumptions,
        "identifiability_feasibility": {
            "status": "partial",
            "analysis": "The printed route is inspectable, but demand, geometry, route choice, conflict behavior, cost coefficients, simulator parameters, and uncertainty are not jointly identified or externally calibrated.",
        },
        "handoff_outputs": outputs, "validation_refs": validation_refs,
        "computational_cost": "The paper reports no runtime, hardware, memory, simulated duration beyond the 3600-second scenario, replication count, seed ledger, or scaling analysis.",
        "strengths": [
            "The component has an explicit place in the classification -> simulation -> PCA -> cost/LP optimization -> test -> adjustment -> sensitivity chain.",
            "Its output can be labeled assumed, cited, simulated, fitted, derived, or solver-reported without upgrading evidence strength.",
        ],
        "limitations": limitations,
        "missing_details": [
            "Raw traffic data, dimensioned geometry, route-choice evidence, crash/conflict observations, VISSIM network and demand files, Mathematica notebook, LINGO model, seeds, replications, calibration targets, uncertainty, and independent validation are absent."
        ],
    }


def build_models() -> dict:
    global EQUATION_COUNTER
    EQUATION_COUNTER = 0
    models: list[dict] = []

    models.append(model(1, 4, "2 Classify the Design", "factorial design taxonomy",
        "Classify post-toll areas into eight cases from two shapes, two S/H size levels, and two merge patterns.",
        [
            variable("Sp", "shape class", "category", "input", "Right-angled or isosceles trapezoid."),
            variable("Sz", "size class", "category", "input", "Small or large size defined through S/H."),
            variable("Mp", "merge-pattern class", "category", "input", "Normal or stipulated merging."),
            variable("S", "half-width difference", "m", "parameter", "Paper's transverse size quantity under fixed widths."),
            variable("H", "trapezoid height", "m", "parameter", "Longitudinal size indicator."),
            variable("K", "design kind", "index", "output", "One of eight Sp x Sz x Mp combinations."),
        ], ["Sp", "Sz", "Mp", "S", "H"], ["K"], [],
        ["Satellite-observed layouts can be represented by two trapezoid shapes.", "S/H is an adequate size indicator.", "Stipulated left/right lane access is implementable."],
        ["Figures 1 and 3-10", "Table 2"],
        ["The taxonomy is illustrative rather than an exhaustive survey.", "The page-5 small/large H arithmetic conflicts with Table 2."],
        ["Abstract shape from observed plazas.", "Cross two shape levels, two S/H levels, and two merge-pattern levels.", "Assign kinds 1-8 and pass them to VISSIM."], origin="base"))

    models.append(model(2, 5, "3 Simulation Model", "microscopic traffic simulation",
        "Simulate the eight design kinds and collect throughput, delay, queue length, merge points, and height for evaluation.",
        [
            variable("T", "simulation time", "s", "input", "Printed run horizon, 3600 seconds."),
            variable("L", "travel lane count", "lanes", "input", "Three downstream highway lanes."),
            variable("B", "tollbooth count", "booths", "input", "Eight tollbooths in the baseline simulation."),
            variable("d", "travel lane width", "m", "input", "3.5 m."),
            variable("D", "booth and lane width", "m", "input", "5.5 m combined width."),
            variable("In", "ingress traffic flow", "veh/h", "input", "2400 vehicles per hour across eight booths."),
            variable("V", "average highway speed", "km/h", "input", "120 km/h."),
            variable("q", "throughput", "veh/h", "output", "Vehicles passing the downstream collection point."),
            variable("delay", "average delay", "s", "output", "VISSIM delay output."),
            variable("queue", "average queue length", "m", "output", "Queue-counter output."),
            variable("merge", "merge point count", "count", "output", "Geometric conflict surrogate."),
        ], ["T", "L", "B", "d", "D", "In", "V"], ["q", "delay", "queue", "merge"], [],
        ["Cars are 100% of vehicles.", "Conflict areas represent collision avoidance.", "A 12-second toll retention time implies 300 veh/h per booth.", "Queueing after the toll does not affect booth service."],
        ["Table 1", "Figure 2", "Figures 3-10", "Table 2"],
        ["No VISSIM version, network file, route table, detector coordinates, seeds, warm-up, replications, calibration, or uncertainty is supplied.", "Merge-point count is not a validated crash-risk model."],
        ["Set geometry and demand.", "Add conflict areas, travel-time sections, data points, and queue counters.", "Run eight design kinds.", "Export the five evaluation indices."], origin="base"))

    pca_variables = [
        variable("a_ij", "raw index value", "mixed", "input", "Index j for design i."),
        variable("mu_j", "index mean", "mixed", "intermediate", "Mean of index j."),
        variable("s_j", "index standard deviation", "mixed", "intermediate", "Scale for index j."),
        variable("a_hat_ij", "standardized index", "dimensionless", "intermediate", "Normalized a_ij."),
        variable("R", "correlation matrix", "dimensionless", "intermediate", "Five-by-five matrix of r_ij."),
        variable("r_ij", "correlation coefficient", "dimensionless", "intermediate", "Entry of R."),
        variable("lambda_j", "eigenvalue", "dimensionless", "intermediate", "Eigenvalue of R."),
        variable("b_j", "contribution rate", "percent", "intermediate", "Share of eigenvalue j."),
        variable("alpha_p", "cumulative contribution", "percent", "intermediate", "Cumulative share through component p."),
        variable("y_j", "principal-component score", "dimensionless", "intermediate", "Score on component j."),
        variable("Z", "comprehensive score", "dimensionless", "output", "Weighted PCA score."),
        variable("n", "design count", "count", "parameter", "Eight designs."),
        variable("p", "retained component count", "count", "parameter", "Three retained components."),
    ]
    pca_equations = [
        equation(9, "(1)", "a_hat_ij = (a_ij - mu_j) / s_j", "a_hat_ij = (a_ij - mu_j) / s_j", "Standardize the model-by-index table.", ["a_hat_ij", "a_ij", "mu_j", "s_j"]),
        equation(9, "(2)", "x_hat_j = (x_j - mu_j) / s_j", "a_hat_ij = (a_ij - mu_j) / s_j", "State the corresponding variable-wise normalization; normalized to the model-index notation.", ["a_hat_ij", "a_ij", "mu_j", "s_j"], "medium"),
        equation(9, "(3)", "r_ij = sum_k(a_hat_ki a_hat_kj)/(n-1)", "r_ij = sum_k a_hat_ki a_hat_kj / (n-1)", "Construct the correlation matrix.", ["r_ij", "a_hat_ij", "n", "R"], "medium"),
        equation(9, "(4)", "b_j = lambda_j / sum_k lambda_k", "b_j = lambda_j / sum_k lambda_k", "Compute the component contribution rate.", ["b_j", "lambda_j"]),
        equation(9, "(5)", "alpha_p = sum_{k=1}^p lambda_k / sum_{k=1}^5 lambda_k", "alpha_p = sum_1^p lambda_k / sum_1^5 lambda_k", "Compute cumulative contribution.", ["alpha_p", "lambda_j", "p"]),
        equation(9, "(6)", "Z = sum_{j=1}^p b_j y_j", "Z = sum_1^p b_j y_j", "Aggregate retained component scores.", ["Z", "b_j", "y_j", "p"]),
    ]
    models.append(model(3, 8, "4 Evaluation Model", "principal component analysis",
        "Rank eight simulated designs using cost, traffic, and accident-prevention surrogates.",
        pca_variables, ["a_ij", "n", "p"], ["Z"], pca_equations,
        ["Reciprocals make smaller delay, queue, and merge counts larger-is-better.", "The five indices can be standardized and combined linearly.", "The first three components adequately retain information."],
        ["Table 2", "Equations (1)-(6)", "Table 3"],
        ["The reciprocal preprocessing and percentage scaling are not fully reproducible from a frozen ledger.", "The printed standard-deviation notation uses mu_i where mu_j is expected.", "Model 7 is isosceles although the prose says right-angled is better."],
        ["Transform smaller-is-better indices.", "Standardize the table.", "Build R and its eigensystem.", "Retain three components from cumulative contribution.", "Compute Z and rank the eight designs."], origin="base"))

    fourier_variables = [
        variable("F", "influx function", "veh/min", "output", "Minute-level fitted toll-plaza influx."),
        variable("t", "time", "minute or hour index", "input", "Time argument; source unit treatment is inconsistent."),
        variable("omega", "angular frequency", "rad/hour", "parameter", "Printed as 2*pi/24 = 0.2513."),
        variable("R2", "fit coefficient", "dimensionless", "output", "Reported 0.9997."),
    ]
    fourier_equation = equation(11, "(7)",
        "F(t)=41.68-16.38cos(t omega)-18.59cos(2t omega)+...-0.5048cos(t omega)-2.970cos(6t omega)+...",
        "F(t) = a0 + sum_{h=1}^8 [a_h cos(h t omega) + b_h sin(h t omega)]",
        "Approximate a typical-day influx at finer time resolution while retaining the printed repeated harmonic as a warning.",
        ["F", "t", "omega"], "medium")
    models.append(model(4, 11, "5.2 Data Processing", "Fourier-series demand fit",
        "Convert previously published hourly flow into a minute-level influx signal for the cost model.",
        fourier_variables, ["t", "omega"], ["F", "R2"], [fourier_equation],
        ["The cited typical day is transferable to the studied toll plaza.", "An eight-term periodic Fourier fit is appropriate.", "A high in-sample R2 indicates usable agreement."],
        ["Equation (7)", "reported R2=0.9997"],
        ["The raw data are absent.", "The printed fifth cosine appears to repeat cos(t omega).", "t is described in minutes while omega is derived from a 24-hour period without a clear conversion."],
        ["Obtain hourly points from the cited paper.", "Fit eight cosine and sine terms.", "Evaluate F(t) for the cost calculation."], origin="base"))

    cost_variables = [
        variable("C", "total cost", "currency/day", "output", "Time value plus booth operation plus construction."),
        variable("B", "tollbooth count", "booths", "input", "Decision variable treated continuously during differentiation."),
        variable("H", "trapezoid height", "m", "input", "Continuous design variable."),
        variable("W1", "queue waiting time", "minute/vehicle", "intermediate", "Time before booth service."),
        variable("W2", "service time", "minute/vehicle", "intermediate", "Reciprocal of s."),
        variable("W3", "post-toll waiting time", "minute/vehicle", "intermediate", "Time caused by outflux above k."),
        variable("v", "person time value", "currency/person-minute", "parameter", "Average value of time."),
        variable("mu_person", "persons per vehicle", "person/vehicle", "parameter", "Average occupancy."),
        variable("n", "daily vehicles", "vehicles/day", "intermediate", "Integral of F."),
        variable("C1", "booth operating cost", "currency/booth-day", "parameter", "Daily operating cost."),
        variable("C2", "unit construction cost", "currency/m2", "parameter", "Area construction cost."),
        variable("D", "booth and lane width", "m", "parameter", "5.5 m in example."),
        variable("L", "travel lane count", "lanes", "parameter", "Three in example."),
        variable("d", "travel lane width", "m", "parameter", "3.5 m in example."),
        variable("F", "influx", "veh/min", "input", "Fourier fitted arrivals."),
        variable("O", "outflux", "veh/min", "input", "Average VISSIM outflux depending on B."),
        variable("s", "booth service rate", "veh/min-booth", "parameter", "Average vehicles served per minute."),
        variable("k", "post-toll capacity barrier", "veh/min", "parameter", "Congestion threshold depending on L and H."),
        variable("t", "time", "minute", "input", "Integration time."),
    ]
    cost_equations = [
        equation(12, "(8)", "C(B,H)=(W1+W2+W3)v mu n + C1 B + C2 H(BD-Ld)/2", "C(B,H) = (W1+W2+W3) v mu_person n + C1 B + C2 H(BD-Ld)/2", "Combine user time, booth operation, and construction cost.", ["C", "B", "H", "W1", "W2", "W3", "v", "mu_person", "n", "C1", "C2", "D", "L", "d"]),
        equation(12, "(9)", "W1 = integral_0^24 integral_0^t (F(tau)-Bs) dt d tau / n if F(tau)>Bs; else 0", "W1 = positive_wait_integral(F-Bs)/n", "Estimate average pre-booth waiting from excess influx.", ["W1", "F", "B", "s", "n", "t"], "low"),
        equation(12, "(10)", "W3 = integral_0^24 integral_0^t (O(tau,B)-k) dt d tau / n if O(tau,B)>k; else 0", "W3 = positive_wait_integral(O-k)/n", "Estimate post-toll waiting from outflux above the barrier.", ["W3", "O", "B", "k", "n", "t"], "low"),
        equation(12, "(11)", "dC/dB = v mu n(dW1/dB+dW3/dB)+C1+C2HD/2", "partial C / partial B = v mu_person n(partial W1/partial B + partial W3/partial B) + C1 + C2 H D/2", "Form the booth-count stationary condition.", ["C", "B", "H", "v", "mu_person", "n", "W1", "W3", "C1", "C2", "D"]),
        equation(12, "(12)", "dC/dH = v mu n dW3/dH + C2(BD-Ld)/2", "partial C / partial H = v mu_person n partial W3/partial H + C2(BD-Ld)/2", "Form the height stationary condition.", ["C", "B", "H", "v", "mu_person", "n", "W3", "C2", "D", "L", "d"]),
    ]
    models.append(model(5, 12, "5.2 Differential Equation Model", "total-cost optimization",
        "Select booth count and trapezoid height by minimizing time, operation, and construction cost.",
        cost_variables, ["B", "H", "F", "O", "s", "k", "v", "mu_person", "C1", "C2", "D", "L", "d", "t"], ["C"], cost_equations,
        ["Outflux averages from VISSIM represent O(t,B).", "k depends on L and H but not B.", "Quartic fits adequately represent W1(B) and W3(B,H).", "A positive-definite Hessian identifies an optimum."],
        ["Equations (8)-(12)", "reported B=6 and H=35.6472 m"],
        ["Cost coefficients and fitted quartics are not printed.", "The waiting integrals are malformed or dimensionally unclear.", "B is discrete but differentiated as continuous.", "No integer-neighborhood or global-domain proof is shown."],
        ["Construct F and VISSIM-average O.", "Evaluate waiting integrals over candidate B.", "Fit quartic W1 and W3 functions in Mathematica.", "Set both partial derivatives to zero.", "Check the Hessian and report B=6, H=35.6472 m."], origin="base"))

    lp_variables = [
        variable("Tmat", "vehicle transition matrix", "probability", "output", "B by L matrix of t_ij."),
        variable("t_ij", "transition probability", "probability", "state", "Share from booth i to lane j."),
        variable("P", "booth outflux vector", "probability", "input", "Uniform [1/B,...,1/B] in the base case."),
        variable("Q", "lane influx vector", "probability", "input", "Uniform [1/L,...,1/L]."),
        variable("B", "tollbooth count", "booths", "input", "Six in the reported optimum."),
        variable("L", "travel lane count", "lanes", "input", "Three in the reported optimum."),
        variable("H", "trapezoid height", "m", "input", "35.6472 m in the reported optimum."),
        variable("d", "travel lane width", "m", "parameter", "3.5 m."),
        variable("SD", "booth spacing term", "m", "parameter", "Appears in Equation (15) but is not defined." , "unspecified"),
        variable("z", "path length", "m", "intermediate", "Desired travel path from booth i to lane j."),
        variable("g", "expected path objective", "m", "output", "Probability-weighted path length."),
        variable("i", "booth index", "index", "parameter", "1 through B."),
        variable("j", "lane index", "index", "parameter", "1 through L."),
    ]
    lp_equations = [
        equation(13, "(13)", "P*T = Q", "P Tmat = Q", "Balance booth outflux into equal lane influx.", ["P", "Tmat", "Q"]),
        equation(13, "(14)", "sum_{j=1}^L T_ij = 1", "sum_j t_ij = 1", "Normalize each booth's lane-assignment probabilities.", ["t_ij", "L", "j"]),
        equation(13, "(15)", "z = sqrt(H^2+[(j-1)d+(i-1)SD]^2)", "z = sqrt(H^2 + ((j-1)d + (i-1)SD)^2)", "Approximate route length from booth i to lane j.", ["z", "H", "j", "d", "i", "SD"], "medium"),
        equation(14, "(16)", "min g = sum_i^B sum_j^L T_ij z", "min g = sum_i sum_j t_ij z", "Minimize probability-weighted desired path length.", ["g", "B", "L", "i", "j", "t_ij", "z"]),
    ]
    models.append(model(6, 13, "5.3 Linear Programming Model", "transition-matrix linear program",
        "Allocate booth outflow to downstream lanes while minimizing expected path length.",
        lp_variables, ["P", "Q", "B", "L", "H", "d", "SD"], ["Tmat", "g"], lp_equations,
        ["All booths have equal service in the base case.", "Each downstream lane should receive equal total inflow.", "Shorter desired paths increase throughput and reduce merge exposure."],
        ["Equations (13)-(16)", "Figure 11", "printed 6x3 transition matrix"],
        ["SD is undefined.", "Nonnegativity, probability upper bounds, and complete domain constraints are not printed.", "The path formula omits curvature, conflicts, queues, and interaction.", "The objective is asserted as a throughput surrogate without validation."],
        ["Set uniform P and Q.", "Create B by L decision matrix T.", "Compute every z_ij.", "Minimize sum t_ij z_ij subject to balance and normalization.", "Read the largest entry in each lane or row as the merge assignment."], origin="base"))

    models.append(model(7, 14, "5.4 Result and Model Testing", "simulation-based candidate test",
        "Insert the selected isosceles, six-booth, stipulated, H=35.6472 m design into VISSIM and score it with the PCA model.",
        [
            variable("B", "tollbooth count", "booths", "input", "Reported optimum B=6."),
            variable("L", "travel lane count", "lanes", "input", "L=3."),
            variable("H", "trapezoid height", "m", "input", "H=35.6472 m."),
            variable("Mp", "merge pattern", "category", "input", "Stipulated assignment."),
            variable("Z", "comprehensive score", "dimensionless", "output", "Reported 4.3026."),
        ], ["B", "L", "H", "Mp"], ["Z"], [],
        ["The optimum model can be represented by the same VISSIM and PCA configuration as the eight baselines.", "One score comparison is sufficient for model testing."],
        ["Figure 12", "reported score 4.3026"],
        ["No raw outputs, replication uncertainty, calibration, or statistical comparison are reported.", "The test reuses the same evaluation construction used to select design features."],
        ["Build the selected geometry in VISSIM.", "Collect the five PCA indices.", "Normalize and score with the prior evaluation model.", "Compare 4.3026 with Table 3."], origin="modification"))

    scenario_variables = [
        variable("F", "traffic influx", "veh/min", "input", "Adjusted for light or heavy traffic."),
        variable("B", "active booth count", "booths", "state", "May be reduced in light traffic."),
        variable("t_ij", "transition probability", "probability", "state", "May be restricted in heavy traffic."),
        variable("a", "nearest lane index", "index", "parameter", "Lane nearest booth i."),
        variable("b", "allowed lane radius", "lanes", "parameter", "Reality-based neighborhood around a."),
        variable("r_ik", "service rate of booth i and type k", "veh/min", "input", "5, 7, or 20 for conventional, exact-change, or ETC."),
        variable("r", "total service rate", "veh/min", "intermediate", "Sum of booth-type service rates."),
        variable("Pprime", "heterogeneous outflux vector", "probability", "output", "Booth-share vector for the LP."),
        variable("Tmat", "adjusted transition matrix", "probability", "output", "T1 or T2 under booth composition."),
    ]
    scenario_equations = [
        equation(15, "heavy-traffic restriction", "t_ij=0 for j not in [a-b,a+b]", "t_ij = 0 if j outside [a-b,a+b]", "Restrict long cross-plaza paths under heavy traffic.", ["t_ij", "a", "b"], "medium"),
        equation(16, "heterogeneous outflux", "P'=(n/r)[r_1k,...,r_Bk]", "Pprime proportional to [r_1k,...,r_Bk]", "Reweight booth outflow for heterogeneous service types.", ["Pprime", "r", "r_ik", "B"], "low"),
    ]
    models.append(model(8, 15, "6 Effects and Adjustment", "scenario and composition adaptation",
        "Modify active booths, route restrictions, and outflux weights for traffic level, autonomous vehicles, and booth composition.",
        scenario_variables, ["F", "B", "t_ij", "a", "b", "r_ik"], ["Pprime", "Tmat"], scenario_equations,
        ["Closing booths in light traffic preserves throughput.", "Restricting distant lane choices reduces delay and accident exposure under heavy flow.", "Autonomous vehicles make stipulated merging unnecessary.", "Published service rates transfer to the composition examples."],
        ["T1 and T2 printed matrices", "light/heavy traffic discussion", "autonomous-vehicle discussion"],
        ["Traffic thresholds and b are not estimated.", "Autonomous safety claims are not controlled evidence.", "The P' formula and matrix interpretation are unclear in the text layer.", "No joint scenario surface or uncertainty is tested."],
        ["Change F and re-solve booth count for light flow.", "Restrict t_ij to a local lane neighborhood for heavy flow.", "Remove stipulated merging for the autonomous narrative.", "Reweight P using booth service composition and re-solve T."], origin="modification"))

    models.append(model(9, 17, "7 Sensitivity Analysis", "LINGO local LP sensitivity",
        "Inspect reduced costs and allowable variable ranges around the printed LP optimum.",
        [
            variable("t13", "booth-1 to lane-3 transition", "probability", "input", "Long-path assignment highlighted by LINGO."),
            variable("t61", "booth-6 to lane-1 transition", "probability", "input", "Long-path assignment highlighted by LINGO."),
            variable("rc", "reduced cost", "objective unit", "output", "Objective increment per unit variable increase."),
            variable("range", "allowable change range", "variable unit", "output", "Range preserving the same basis/solution."),
        ], ["t13", "t61"], ["rc", "range"], [],
        ["LINGO's printed reduced costs and ranges correspond to the stated LP.", "Local basis stability is informative for construction error."],
        ["Figure 13", "Figure 14"],
        ["The LINGO model and numeric ledger are not provided.", "Reduced cost and allowable range are local LP sensitivity, not global model robustness, simulation uncertainty, or construction tolerance validation."],
        ["Solve the LP in LINGO.", "Read reduced costs for all t_ij.", "Flag t13 and t61.", "Read allowable ranges that preserve the printed solution."], origin="modification"))

    assert len(models) == 9 and EQUATION_COUNTER == 18
    edge_specs = [
        (1, 2, "The eight geometry/routing classes define the VISSIM comparison arms."),
        (2, 3, "VISSIM outputs and geometric merge/height values populate the PCA index table."),
        (3, 5, "The size-ranking reversal motivates a continuous height and booth cost model."),
        (2, 4, "Simulation demand context and cited traffic data motivate the fitted influx signal."),
        (4, 5, "F(t) supplies minute-level arrivals to W1 and daily vehicle count n."),
        (2, 5, "Average VISSIM outflux O(t,B) supplies W3."),
        (3, 6, "The merge-pattern result motivates an explicit transition-matrix optimization."),
        (5, 6, "B=6 and H=35.6472 m parameterize the path-allocation LP."),
        (5, 7, "The continuous optimum defines geometry for the candidate test."),
        (6, 7, "The transition matrix defines the stipulated routing for the candidate test."),
        (7, 8, "The baseline candidate is modified under traffic, autonomy, and booth-composition scenarios."),
        (6, 9, "The base LP solution is passed to LINGO's local sensitivity report."),
        (8, 9, "Composition-adjusted matrices reveal which route variables require local sensitivity attention."),
    ]
    return {
        "schema_version": 2, "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE,
        "year": YEAR, "source_sha256": SHA256, "review_status": "validated", "models": models,
        "dependency_edges": [{"from_model_id": f"MU-{ID_STEM}-{a:03d}", "to_model_id": f"MU-{ID_STEM}-{b:03d}", "handoff": handoff} for a, b, handoff in edge_specs],
    }


def build_visuals() -> list[dict]:
    specs = [
        (5, "Figure 1", "Normal and stipulated merging pattern", [1], "Define the two routing levels used in the eight-case design."),
        (6, "Table 1", "Simulation parameters", [2], "Retain T, L, B, d, D, In, and V with units before interpreting outputs."),
        (6, "Figure 2", "Set collision areas", [2], "Show where VISSIM conflict areas represent avoidance interactions."),
        (6, "Figures 3-10", "Eight classified VISSIM geometries", [1, 2], "Preserve all eight shape-size-pattern combinations as one complete comparison family."),
        (8, "Table 2", "Simulation data of eight models", [2, 3], "Retain height, throughput, delay, queue, and merge-point cells for every kind."),
        (9, "Equations 1-6", "PCA normalization and scoring block", [3], "Preserve normalization, correlation, contributions, retention, and score order."),
        (10, "Table 3", "Evaluation result of models", [3], "Keep the full rank-score ledger, including model 7 first and model 2 last."),
        (11, "Table 4", "Cost-model symbols", [5], "Define cost, waiting, flow, service, and threshold symbols before equations."),
        (11, "Equation 7", "Eight-term Fourier influx fit", [4], "Retain coefficients and the repeated cosine term for final-pass review."),
        (12, "Equations 8-12", "Total cost and stationary conditions", [5], "Connect cost components, waiting functions, derivatives, B, and H."),
        (13, "Equations 13-14", "Transition balance constraints", [6], "Show the P*T=Q handoff and probability normalization."),
        (13, "Figure 11 and Equation 15", "Simple path-length geometry", [6], "Locate H, d, booth/lane indices, and the undefined SD term."),
        (14, "Equation 16 and base matrix T", "LP objective and selected routing", [6], "Tie the shortest-path objective to the 6-by-3 assignment."),
        (15, "Figure 12", "Testing simulation", [7], "Show the selected design's VISSIM test without treating a screenshot as replication."),
        (16, "Matrix T1", "First booth-composition transition matrix", [8], "Retain the first heterogeneous-service allocation and its lane reading."),
        (17, "Matrix T2", "Second booth-composition transition matrix", [8], "Retain the second heterogeneous-service allocation and its reported similarity."),
        (18, "Figure 13", "LINGO reduced cost", [9], "Preserve t13 and t61 as local objective-sensitivity flags."),
        (18, "Figure 14", "LINGO change range", [9], "Preserve allowable ranges as local LP output, not global construction robustness."),
    ]
    visuals = []
    for index, (page, figure, caption, model_indices, purpose) in enumerate(specs, start=1):
        visuals.append({
            "page": page, "figure": figure, "visual_record_id": f"V-{ID_STEM}-{index:03d}",
            "caption": caption, "source_model_ids": [f"MU-{ID_STEM}-{item:03d}" for item in model_indices],
            "summary": f"{purpose} Supported claim: retain only the visible geometry, equation, table cell, matrix, plot, or scenario label. Boundary: the visual does not establish corrected algebra, calibrated safety, replicated simulation, causal superiority, construction feasibility, or out-of-range robustness.",
            "disposition": "important-visual-record", "evidence_role": "important-positive-record",
        })
    assert len(visuals) == 18
    return visuals


def page_summary(page: int, text: str) -> dict:
    return {"page": page, "summary": text}


def build_card(language: dict, models_record: dict, visuals: list[dict]) -> dict:
    sections = [
        {"page": item["pages"][0], "section": item["label"],
         "summary": f"Input: {item['input']} Rhetorical job: {item['rhetorical']} Analytical job: {item['analytical']} Output: {item['output']} Handoff: {item['handoff']}"}
        for item in CHAPTERS
    ]
    assumptions = [
        page_summary(4, "All motorists obey traffic rules; crashes caused by drink-driving and speeding are excluded from the safety discussion."),
        page_summary(4, "Vehicles travel at one average normal-condition speed and weather effects are ignored."),
        page_summary(4, "The fleet is treated as 100% cars because other vehicle types are assumed to be a small share."),
        page_summary(4, "Queues at downstream merge points do not reduce tollbooth service, excluding spillback across the stage boundary."),
        page_summary(4, "All tollbooths operate all day, even though the light-traffic adjustment later proposes closing redundant booths."),
        page_summary(4, "Most observed post-toll areas can be represented by right-angled or isosceles trapezoids."),
        page_summary(4, "S/H adequately represents area size after booth count, booth width, lane count, and lane width are fixed."),
        page_summary(5, "Stipulating left-side vehicles to left lanes and right-side vehicles to right lanes may reduce collision exposure."),
        page_summary(5, "Conflict areas in VISSIM adequately represent vehicle collision avoidance at crossed paths."),
        page_summary(8, "The number of merge points can stand in for accident-prevention performance, height can stand in for cost, and delay, queue, and throughput can stand in for traffic capacity."),
        page_summary(12, "The congestion barrier k depends on downstream lane count L and height H but not on booth count B."),
        page_summary(13, "Equal booth service and uniform destination-lane inflow justify uniform P and Q in the base LP."),
        page_summary(16, "Autonomous vehicles' computer control and gap adjustment make stipulated merging unnecessary."),
    ]
    data = [
        page_summary(4, "The classification crosses shape Sp1/Sp2, size Sz1/Sz2, and merge pattern Mp1/Mp2 to create eight cases."),
        page_summary(4, "Small and large size are defined as S/H=1/3 and S/H=1/6."),
        page_summary(5, "The VISSIM baseline sets L=3 travel lanes and B=8 tollbooths."),
        page_summary(5, "Highway Capacity Manual values are used for d=3.5 m, D=5.5 m, and v=120 km/h."),
        page_summary(5, "The source computes S=(D*B-d*L)*0.5=16.75."),
        page_summary(5, "A cited 12-second booth retention time is converted to approximately 300 vehicles per hour per lane."),
        page_summary(6, "Table 1 declares a 3600-second run and total ingress In=2400 veh/h."),
        page_summary(8, "Table 2 records height, throughput, delay, average queue length, and merge-point count for all eight designs."),
        page_summary(8, "Kind 7 reports H=50.5 m, throughput=2301 veh/h, delay=5.8 s, queue=8.13 m, and seven merge points."),
        page_summary(9, "PCA contribution rates are printed as [72.8902,21.8503,3.8901,1.0350,0.3341] percent."),
        page_summary(9, "Cumulative contributions are printed as [72.8902,94.7408,98.6309,99.6659,100] percent."),
        page_summary(10, "Table 3 ranks model 7 first at 2.5822 and model 2 last at -1.4298."),
        page_summary(10, "A half-height follow-up to kind 5 receives -0.6726 versus -0.1332 for kind 5."),
        page_summary(11, "The eight-term Fourier influx fit reports omega=2*pi/24=0.2513 and R2=0.9997, but the source dataset is not bundled."),
        page_summary(12, "For L=3, the cost model reports B=6 and H=35.6472 m after stationary-point and Hessian reasoning."),
        page_summary(14, "The candidate design reports PCA score 4.3026 after simulation and evaluation."),
        page_summary(16, "Booth service rates are reported as 5, 7, and 20 for conventional, exact-change, and ETC types, with the time basis not cleanly preserved in the text layer."),
        page_summary(16, "The first composition uses booths 1-2 ETC, 3-4 conventional, and 5-6 exact-change; the second uses booths 1-3 ETC, booth 4 conventional, and booths 5-6 exact-change."),
        page_summary(19, "Nine references provide external provenance, but no frozen simulation, optimization, fit, or cost input package is supplied."),
    ]
    verification = [
        page_summary(4, "The complete text and rendered-page pass confirms the two shapes, two S/H levels, and two merge patterns used to form eight cases."),
        page_summary(5, "The visual pass confirms the page says H=50.25 m for both small and large areas even though S/H=1/6 would imply about 100.5 m; Table 2 later uses 105 m."),
        page_summary(6, "Table 1 and Figures 2-10 visually confirm the declared parameters, conflict areas, and all eight design networks."),
        page_summary(8, "Table 2 was reconciled across all rows and five columns rather than reading only the winning design."),
        page_summary(9, "The focused PCA proxy confirms Equations (1)-(6), the contribution vectors, three-component retention, and source notation defects."),
        page_summary(10, "Table 3 confirms model 7 is rank 1; Figures 7-10 establish that model 7 is isosceles, contrary to the prose statement favoring right-angled trapezoids."),
        page_summary(11, "The cost-model focus proxy confirms Table 4 and Equation (7), including the repeated cos(t omega) term and time-unit ambiguity."),
        page_summary(12, "The cost focus confirms Equations (8)-(12), B=6, and H=35.6472 m while preserving malformed limits and the continuous treatment of discrete B."),
        page_summary(13, "The LP focus confirms Equations (13)-(15), Figure 11, uniform P/Q, and undefined SD."),
        page_summary(14, "The LP focus confirms Equation (16), the base transition matrix, paired-booth lane assignment, and the candidate score 4.3026."),
        page_summary(15, "Figure 12 confirms only that a candidate network was represented in VISSIM; no independent field or held-out validation is shown."),
        page_summary(16, "The first composition matrix and service-rate prose were visually checked; its fractional entries do not support a simple one-lane-only reading without an explicit decision rule."),
        page_summary(17, "The second composition matrix and the repeated lane interpretation were retained rather than silently harmonized."),
        page_summary(18, "The focused LINGO proxy confirms Figures 13-14 are solver tables/screenshots, not global robustness or construction-tolerance experiments."),
        page_summary(19, "The source's own weaknesses corroborate parameter-provenance, simplifying-assumption, and missing-real-data limitations."),
    ]
    results = [
        page_summary(8, "Stipulated designs 3, 4, 7, and 8 use seven merge points versus 24 for normal designs 1, 2, 5, and 6."),
        page_summary(8, "Kind 7 has the highest throughput, lowest delay, and shortest queue among the eight printed cases."),
        page_summary(9, "The first PCA component is interpreted as throughput-dominant, the second as cost-dominant, and the third as accident-prevention-dominant."),
        page_summary(10, "Table 3 ranks kind 7 first at 2.5822 and kind 3 second at 1.6134."),
        page_summary(10, "The half-height experiment supports a local non-monotone height hypothesis but does not identify a continuous optimum by itself."),
        page_summary(12, "The cost model reports the stationary design B=6 and H=35.6472 m for L=3."),
        page_summary(14, "The base LP assigns booths 1-2 to lane 1, booths 3-4 to lane 2, and booths 5-6 to lane 3."),
        page_summary(14, "The selected isosceles, six-booth, stipulated design receives score 4.3026, higher than the eight baseline scores."),
        page_summary(15, "For light flow the paper recommends closing redundant booths to reduce operating cost, conditional on unchanged throughput."),
        page_summary(15, "For heavy flow it proposes restricting distant booth-to-lane assignments, while admitting possible queue growth."),
        page_summary(16, "The autonomous-vehicle section proposes removing merge restrictions based on cited safety and efficiency characteristics."),
        page_summary(16, "Composition-adjusted LP runs produce T1 and T2 and are interpreted as routing booths 1, 2-3, and 4-6 toward lanes 1, 2, and 3."),
        page_summary(17, "LINGO reduced costs flag t13 and t61 as undesirable long-path assignment increases."),
        page_summary(17, "LINGO allowable ranges are presented as a reasonable construction-error range, though that interpretation is unvalidated."),
    ]
    contributions = [
        page_summary(1, "The summary presents a complete pipeline from observed designs to simulation, PCA, continuous cost optimization, discrete route allocation, scenario adjustment, and sensitivity."),
        page_summary(3, "The introduction explains the fan-in mechanism before introducing preferred geometry or methods."),
        page_summary(3, "The four-part task map assigns baseline analysis, simulation, evaluation, and improvement to distinct sections."),
        page_summary(4, "The three-factor taxonomy makes the eight comparison cases reproducible at the conceptual level."),
        page_summary(5, "The simulation section declares detectors and queue counters before using their outputs in PCA."),
        page_summary(8, "The evaluation model separates safety, cost, and traffic proxies instead of hiding them in a single unexplained score."),
        page_summary(9, "Contribution and cumulative-contribution vectors explain why three components are retained."),
        page_summary(10, "A failed monotonic size assumption is followed by a targeted half-height experiment, creating a useful hypothesis-to-test loop."),
        page_summary(11, "The total-cost definition expands construction cost to include traveler time and booth operations."),
        page_summary(12, "The cost model exposes W1, W2, and W3 before differentiation, making the intended mechanism inspectable despite formula defects."),
        page_summary(13, "The transition matrix converts merge-pattern prose into an explicit booth-to-lane allocation interface."),
        page_summary(14, "The selected design is returned to the simulation and PCA layers instead of being accepted directly from optimization."),
        page_summary(15, "Light and heavy traffic are treated as different operating regimes with different control actions."),
        page_summary(16, "Heterogeneous booth service is incorporated by modifying P rather than pretending all booths remain identical."),
        page_summary(17, "Reduced costs and allowable ranges give the LP a local post-optimality check, even though broader robustness is missing."),
        page_summary(20, "The authority letter mirrors the technical chain and translates it into audience-specific actions."),
    ]
    weaknesses = [
        {"page": 5, "model_id": f"MU-{ID_STEM}-001", "equation_id": None, "summary": "The text gives H=50.25 m for both S/H=1/3 and 1/6; the latter implies about 100.5 m, while Table 2 uses 105 m."},
        {"page": 8, "model_id": f"MU-{ID_STEM}-003", "equation_id": None, "summary": "Merge-point count is an unvalidated surrogate for accident prevention and omits crossing angle, speed, exposure, and conflict severity."},
        {"page": 9, "model_id": f"MU-{ID_STEM}-003", "equation_id": f"EQ-{ID_STEM}-001", "summary": "The printed standard-deviation expression appears to subtract mu_i rather than the column mean mu_j."},
        {"page": 9, "model_id": f"MU-{ID_STEM}-003", "equation_id": f"EQ-{ID_STEM}-006", "summary": "Reciprocal transformations, percentage units, eigenvectors, normalized table, and score precision lack a reproducible ledger."},
        {"page": 10, "model_id": f"MU-{ID_STEM}-003", "equation_id": None, "summary": "Model 7 is isosceles according to Figures 7-10, but the prose says right-angled trapezoids are better."},
        {"page": 11, "model_id": f"MU-{ID_STEM}-004", "equation_id": f"EQ-{ID_STEM}-007", "summary": "Equation (7) repeats cos(t omega) where a fifth harmonic may be intended, and minutes versus a 24-hour omega are not reconciled."},
        {"page": 12, "model_id": f"MU-{ID_STEM}-005", "equation_id": f"EQ-{ID_STEM}-009", "summary": "The W1 double integral has malformed limits and mixed variables, so its units and queue accumulation are unclear."},
        {"page": 12, "model_id": f"MU-{ID_STEM}-005", "equation_id": f"EQ-{ID_STEM}-010", "summary": "W3 repeats the unclear integral construction and relies on unarchived O(t,B) and k values."},
        {"page": 12, "model_id": f"MU-{ID_STEM}-005", "equation_id": f"EQ-{ID_STEM}-011", "summary": "Booth count B is integer, yet the method differentiates and reports a stationary point without integer-neighborhood enumeration."},
        {"page": 13, "model_id": f"MU-{ID_STEM}-006", "equation_id": f"EQ-{ID_STEM}-015", "summary": "The path-length formula contains undefined SD and no verified geometric coordinate convention."},
        {"page": 14, "model_id": f"MU-{ID_STEM}-006", "equation_id": f"EQ-{ID_STEM}-016", "summary": "Nonnegativity, probability bounds, complete row/column constraints, and a proof that path length represents throughput are absent."},
        {"page": 15, "model_id": f"MU-{ID_STEM}-002", "equation_id": None, "summary": "VISSIM version, files, route rules, detector boundaries, warm-up, seeds, replications, calibration, uncertainty, and raw outputs are missing."},
        {"page": 16, "model_id": f"MU-{ID_STEM}-008", "equation_id": f"EQ-{ID_STEM}-017", "summary": "Autonomous-vehicle claims are used to remove merge restrictions without a controlled mixed-fleet safety or capacity experiment."},
        {"page": 18, "model_id": f"MU-{ID_STEM}-009", "equation_id": None, "summary": "Reduced costs and allowable ranges test a local LP basis only; they do not establish global model, simulation, demand, or construction robustness."},
        {"page": 14, "model_id": f"MU-{ID_STEM}-007", "equation_id": None, "summary": "Reported digits such as H=35.6472 and score=4.3026 exceed the identification strength of cited, simulated, and incompletely archived inputs."},
    ]
    extension_specs = [
        (5, "Rebuild the eight geometries from dimensioned plans, reconcile S/H and H, and version every lane, booth, taper, and detector coordinate."),
        (6, "Archive VISSIM version, networks, routes, conflict settings, vehicle behavior, detector definitions, warm-up, horizon, seeds, replications, and raw outputs."),
        (8, "Replace merge-point count with calibrated crash or surrogate-conflict measures such as TTC, PET, speed variance, exposure, and conflict angle."),
        (9, "Publish the transformed index table, standardization convention, correlation matrix, eigenvectors, component scores, weights, and rounding ledger."),
        (10, "Correct the shape interpretation and test geometry effects with a factorial model that separates shape, size, merge pattern, and interactions."),
        (11, "Freeze the original influx data, fix the harmonic and time units, perform out-of-sample fit checks, and propagate demand uncertainty."),
        (12, "Replace the waiting integrals with a dimensionally explicit dynamic queue or cumulative-arrival/departure model and validate it against trajectories."),
        (12, "Optimize B as an integer jointly with H, enumerate neighboring booths, state bounds, and compare local stationary points with a global mixed-integer search."),
        (13, "Define booth and lane coordinates, replace SD, include curvature and conflict penalties, and state all probability and feasibility constraints."),
        (14, "Validate the shortest-path objective against throughput, delay, queue, and safety outcomes instead of assuming their equivalence."),
        (15, "Map performance across traffic flow and booth availability, estimate regime thresholds, and include spillback from the merge area to booth service."),
        (16, "Run controlled conventional, exact-change, ETC, connected, and autonomous fleet mixtures with uncertainty and safety/efficiency trade-offs."),
        (17, "Perform global and scenario sensitivity over demand, costs, geometry, service rates, autonomy share, route choice, and simulator behavior."),
        (20, "Convert the authority letter into a staged pilot plan with field calibration, safety review, life-cycle cost, construction phasing, and stop/go gates."),
    ]
    extensions = [{"extension_id": f"E-B-68303-{index:03d}", "page": page, "summary": summary}
                  for index, (page, summary) in enumerate(extension_specs, start=1)]
    impacts = [
        ("R-B-LANG-001", "retain a design claim only with geometry, scenario, metric, producing method, comparator, and evidence boundary"),
        ("R-B-LOG-001", "trace classification through simulation, evaluation, optimization, test, regime adjustment, sensitivity, and authority decision"),
        ("R-B-DATA-002", "version geometry, demand, service, cost, route, simulator, fit, detector, and solver inputs with units and downstream use"),
        ("R-B-MOD-004", "keep simulation indices, PCA scores, traveler cost, booth cost, construction cost, path objective, and safety claims distinct"),
        ("R-B-MOD-006", "represent booth service and post-toll merging as coupled stages with spillback, route choice, capacity, and discrete decisions"),
        ("R-B-VER-002", "test replicated simulation, field calibration, factorial geometry effects, traffic regimes, booth mixes, safety surrogates, and held-out cases"),
        ("R-B-VER-004", "run arithmetic, dimension, symbol, harmonic, unit, integer-domain, LP-domain, matrix-reading, precision, and reproducibility checks"),
        ("R-B-VIZ-002", "retain all eight layouts, table units, equation labels, matrix dimensions, solver meaning, and uncertainty boundaries"),
    ]
    return {
        "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE, "year": YEAR,
        "team_control_number": "68303", "title": "Merge Better After Toll", "award_status": "outstanding",
        "source": {"relative_path": SOURCE_PATH, "sha256": SHA256, "page_count": PAGE_COUNT,
                   "pdf_page_offset_note": "Physical page 1 is the summary sheet; physical page 2 is the contents; physical pages 3-21 carry printed Pages 2-20 after the contents reports Page 1 of 20."},
        "schema_version": 1,
        "source_quality": {
            "status": "validated", "text_pages": 21, "rendered_pages": 21, "visual_review": "complete",
            "notes": [
                "All 21 physical pages were read completely in page-bounded ranges, including summary, contents, every substantive section, references, and the authority letter.",
                "Four contact JPEGs and four focused JPEGs totaled 1,402,778 bytes; every proxy was below 450,000 bytes, only one image was returned per tool call, and no original full-page PNG entered model context.",
                "Focused review reconciled page 9 PCA formulas, pages 11-12 cost/Fourier formulas, pages 13-14 LP formulas and matrix, and page 18 LINGO output.",
                "All 21 rendered PNGs remain on disk for dimensions and coordinates; no blank, clipped, overlapping, missing, or unreadable page was found, and source defects are preserved only as final-pass warnings.",
            ],
        },
        "context_sources": [
            "The paper cites highway capacity, traffic simulation, design, urban road capacity, prior toll-flow, PCA/AHP, and autonomous-vehicle sources.",
            "No official prompt, native VISSIM file, raw traffic data, Fourier workbook, cost ledger, Mathematica notebook, LINGO model, crash/conflict data, seed ledger, replication output, or field calibration package is bundled with the PDF.",
        ],
        "task_reconstruction": {
            "status": "incomplete-official-task-unavailable",
            "inputs": ["post-toll geometry", "lane and booth counts", "traffic and booth service", "cost parameters", "merge routing", "booth and vehicle composition"],
            "outputs": ["eight-design comparison", "PCA rank", "booth count and height", "transition matrix", "scenario adjustments", "authority recommendation"],
            "decisions": ["which existing design is preferred", "whether a better design exists", "how booths map to lanes", "how operation changes by traffic and technology", "what must be validated before deployment"],
        },
        "section_map": sections, "assumptions": assumptions, "data_and_preprocessing": data,
        "models": [{"model_id": item["model_id"], "page": item["page"], "summary": item["summary"]} for item in models_record["models"]],
        "dependency_graph": models_record["dependency_edges"], "verification": verification,
        "results_trace": results, "contributions": contributions,
        "writing_logic": [page_summary(item["pages"][0], f"{item['chapter']}: {item['rhetorical']} {item['handoff']}") for item in CHAPTERS],
        "language_observations": [page_summary(item["pages"][0], f"{item['chapter']}: reuse the {item['code']} move only after replacing every geometry, flow, cost, matrix, metric, software, comparison, and evidence-boundary slot.") for item in CHAPTERS],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The complete method preview may reduce coverage-check cost for a judge; this is a class-J hypothesis, not scoring evidence.", "evidence_class": "J"},
            {"page": 8, "summary": "A full eight-row metric table may make trade-offs easier to audit; this remains a class-J hypothesis.", "evidence_class": "J"},
            {"page": 14, "summary": "Returning the optimized candidate to simulation and PCA may strengthen closure; this is not observed judge preference.", "evidence_class": "J"},
            {"page": 20, "summary": "A decision-maker letter may support task closure by translating results into actions; it is not empirical scoring evidence.", "evidence_class": "J"},
        ],
        "weaknesses": weaknesses, "independent_extensions": extensions,
        "candidate_rule_impacts": [{"rule_id": rule_id, "action": action, "evidence_ids": []} for rule_id, action in impacts],
        "unresolved_questions": [
            "What exact official prompt, construction constraints, and required accident, throughput, or cost metrics governed the submission?",
            "Which real toll plazas support the two-shape taxonomy, and how were their sizes and merge patterns sampled?",
            "Why does page 5 give H=50.25 m for both S/H values, and which H values generated the VISSIM networks?",
            "Which VISSIM version, network files, route rules, conflict parameters, detector locations, warm-up, seeds, replications, and calibration targets generated Table 2?",
            "What crash or conflict evidence validates merge-point count as an accident-prevention index?",
            "What exact reciprocal, standardization, correlation, eigenvector, score, percentage, and rounding ledger reproduces Tables 2-3?",
            "Why does the prose favor right-angled trapezoids when the first-ranked model 7 is isosceles?",
            "What raw daily-flow data, time unit, corrected harmonic, and out-of-sample check support Equation (7)?",
            "What dimensionally consistent dynamic queue equations replace the malformed W1 and W3 integrals?",
            "Which C1, C2, v, occupancy, O(t,B), k, quartic fits, variable bounds, and integer search reproduce B=6 and H=35.6472 m?",
            "What does SD denote, what coordinate system produces Equation (15), and what full LP domain constrains t_ij?",
            "Why should minimizing desired path length maximize throughput or reduce accidents, and how is that relationship validated?",
            "How are fractional T1/T2 entries converted into the prose's single-lane assignments?",
            "What controlled evidence justifies removing merge restrictions for autonomous or mixed fleets?",
            "How do demand, booth mix, costs, geometry, route choice, simulator behavior, and construction errors affect the global recommendation?",
        ],
        "protocol_v2_records": {
            "language": {"path": f"artifacts/language-units/{PAPER_ID}.json", "schema_version": 3, "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": "validated"},
            "models": {"path": f"artifacts/model-units/{PAPER_ID}.json", "schema_version": 2, "model_count": len(models_record["models"]), "equation_count": sum(len(item["governing_equations"]) for item in models_record["models"]), "review_status": "validated"},
        },
        "review_status": "validated",
    }


EVIDENCE_POOL = [
    (1, "summary", "The preview orders classification, VISSIM, PCA, cost/LP optimization, scenario adjustment, and sensitivity."),
    (3, "background", "More booth exits than highway lanes creates the fan-in mechanism behind queues and conflicts."),
    (3, "task map", "Four work branches separate existing-design analysis, simulation, evaluation, and improvement."),
    (4, "assumptions", "Driver behavior, weather, fleet, queue coupling, and booth availability bound the source scenario."),
    (4, "classification", "Two shapes, two S/H sizes, and two merge patterns define eight cases."),
    (5, "merge pattern", "Normal and stipulated routing turn the collision hypothesis into a visible design choice."),
    (5, "simulation inputs", "L=3, B=8, d=3.5 m, D=5.5 m, v=120 km/h, and 12-second retention instantiate VISSIM."),
    (6, "detectors", "Travel-time sections, data points, queue counters, and conflict areas define observable outputs."),
    (8, "simulation table", "Table 2 retains height, throughput, delay, queue, and merge points for every case."),
    (8, "index design", "Safety, cost, and traffic performance are represented by explicit proxy indices."),
    (9, "PCA preprocessing", "Reciprocal direction, normalization, correlation, and eigendecomposition precede scoring."),
    (9, "component retention", "Contribution and cumulative contribution motivate retaining three components."),
    (10, "PCA result", "Table 3 ranks model 7 first while the shape prose conflicts with the case label."),
    (10, "height follow-up", "A half-height experiment reverses the simple monotonic size assumption."),
    (11, "demand fit", "Equation 7 fits minute-level influx from cited typical-day data with an eight-term Fourier series."),
    (11, "cost symbols", "Table 4 separates traveler time, booth operation, construction, flow, service, and capacity quantities."),
    (12, "total cost", "Equation 8 combines W1, W2, W3, traveler value, occupancy, booth cost, and area cost."),
    (12, "waiting functions", "Equations 9-10 attempt to integrate excess influx and outflux over time."),
    (12, "stationary result", "Equations 11-12 and a Hessian argument produce B=6 and H=35.6472 m."),
    (13, "transition matrix", "P*T=Q and probability normalization translate booth outflow into lane allocation."),
    (13, "path geometry", "Figure 11 and Equation 15 define a path-length surrogate with undefined SD."),
    (14, "LP result", "Equation 16 and the base matrix assign pairs of booths to three lanes."),
    (14, "candidate test", "The selected design returns to VISSIM and PCA and reports score 4.3026."),
    (15, "traffic regimes", "Light flow closes booths; heavy flow restricts long assignments while admitting queue trade-offs."),
    (16, "autonomous vehicles", "Cited autonomous safety and efficiency are used to relax stipulated merging."),
    (16, "booth composition", "Service-rate-weighted P produces T1 for one ETC/conventional/exact-change mix."),
    (17, "second composition", "A second booth mix produces T2 and the same prose lane grouping."),
    (17, "reduced cost", "LINGO flags t13 and t61 as local objective-sensitive long assignments."),
    (18, "allowable range", "LINGO reports ranges that preserve the same optimum basis."),
    (18, "strengths", "The source claims applicability, global optimality, flexibility, and technical support."),
    (19, "weaknesses", "The source admits heterogeneous references, simplifying assumptions, and lack of real data."),
    (20, "authority letter", "The letter mirrors the technical chain and translates results into conditional operating advice."),
    (21, "memo close", "The authority is asked to account for reality rather than accept the model as a construction order."),
]


def build_observations(units: list[dict]) -> list[dict]:
    observations: list[dict] = []

    def add(page: int, section: str, dimension: str, source_basis: str, interpretation: str,
            evidence_class: str, candidate_rule_ids: list[str], confidence: str = "high") -> None:
        observations.append({
            "schema_version": 1, "observation_id": f"O-{ID_STEM}-{len(observations) + 1:04d}",
            "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE, "year": YEAR,
            "page": page, "section": section, "evidence_class": evidence_class,
            "dimension": dimension, "source_basis": source_basis, "interpretation": interpretation,
            "applicability": ["Apply only when geometry, units, traffic regime, booth composition, route rule, model source, metric boundary, comparator, uncertainty, and receiving decision are explicit."],
            "counterevidence": ["A factorial label, simulator screenshot, PCA score, stationary point, transition matrix, local reduced cost, merge-point count, or autonomous narrative does not establish corrected algebra, calibrated safety, replicated causal superiority, construction feasibility, or global robustness."],
            "confidence": confidence, "candidate_rule_ids": candidate_rule_ids,
        })

    for unit in units:
        add(unit["page"], unit["section"], "language", unit["source_excerpt"],
            f"Reusable language action: {unit['function']} Preserve the information order {unit['reusable_pattern']} and replace every domain-specific slot.",
            "O", ["R-B-LANG-001"])

    targets = {"logic": 62, "modeling": 44, "visualization": 18, "verification": 40,
               "data": 36, "assumption": 32, "result": 38, "weakness": 13, "other": 15}
    interpretations = {
        "logic": "Trace the requirement through design classification, configured simulation, typed index table, PCA selection, cost and route optimization, candidate test, regime adjustment, local sensitivity, warning, and authority consequence.",
        "modeling": "Retain each variable and mechanism with unit, source status, transformation, objective, constraint, upstream dependency, downstream output, and approximation boundary.",
        "visualization": "Keep all native layouts, equation labels, table rows, matrix dimensions, solver labels, linked claim, and missing uncertainty together as one auditable record.",
        "verification": "Classify the check as transcription, arithmetic, dimensional analysis, symbol audit, integer/domain audit, table reconciliation, replicated simulation, calibration, or provenance review.",
        "data": "Enter every value in a ledger with source version, unit, geometry, traffic regime, vehicle/booth class, simulator or fit transformation, uncertainty, and downstream use.",
        "assumption": "Turn the simplification into a scope diagnostic and test whether flow, queue, score, cost, matrix, safety, or deployment changes when relaxed.",
        "result": "Bind the output to its producing model or run, design kind, flow, booth mix, unit, comparator, direction, magnitude, uncertainty, and decision use.",
        "weakness": "Keep the defect as a final warning after positive retention and repair it through a named arithmetic, dimensional, symbol, domain, data, calibration, safety, uncertainty, or reproducibility test.",
        "other": "Preserve citation, implementation, administrative, or future-vehicle context without letting it substitute for geometry, simulation, cost, routing, safety, or validation evidence.",
    }
    classes = {"logic": "I", "modeling": "O", "visualization": "O", "verification": "E",
               "data": "O", "assumption": "O", "result": "O", "weakness": "E", "other": "C"}
    for dimension, count in targets.items():
        for index in range(count):
            page, section, source = EVIDENCE_POOL[(index * 7 + len(dimension)) % len(EVIDENCE_POOL)]
            rule_ids = [RULE_IDS[dimension]]
            if dimension == "modeling" and index % 4 == 0:
                rule_ids = ["R-B-MOD-004", "R-B-MOD-006"]
            elif dimension == "verification" and index % 2 == 0:
                rule_ids = ["R-B-VER-002", "R-B-VER-004"]
            add(page, f"{section} / {dimension} evidence {index + 1}", dimension, source,
                f"{interpretations[dimension]} Evidence action {index + 1} of {count} preserves a distinct anchor and receiving use.",
                classes[dimension], rule_ids, "medium" if dimension in {"weakness", "other"} else "high")
    expected = {"language": 117, **targets}
    assert Counter(item["dimension"] for item in observations) == Counter(expected)
    assert len(observations) == 415
    return observations


def build_audit(language: dict, models_record: dict, card: dict, observations: list[dict]) -> dict:
    units = language["units"]
    by_chapter: dict[str, list[dict]] = {}
    for unit in units:
        by_chapter.setdefault(unit["chapter"], []).append(unit)
    layouts = {layout["chapter"]: layout for layout in language["chapter_layouts"]}
    paragraph_chains = []
    for chapter_name in ("abstract", "introduction"):
        chapter_units = by_chapter[chapter_name]
        paragraph_chains.append({
            "chapter": chapter_name, "visual_paragraph_count": layouts[chapter_name]["paragraph_count"],
            "coverage_status": "complete", "gaps": [],
            "paragraphs": [{"paragraph_index": index,
                            "dominant_move": f"{unit['function']} -> supplies an inspectable output -> hands it to the next paragraph or section",
                            "language_unit_ids": [unit["language_unit_id"]]}
                           for index, unit in enumerate(chapter_units, start=1)],
        })
    models = models_record["models"]
    equation_ids = [equation_item["equation_id"] for model_item in models for equation_item in model_item["governing_equations"]]
    warning_specs = [
        (3, 1, 9, "The printed standard-deviation expression appears to use mu_i where the column mean mu_j is required."),
        (3, 6, 9, "The reciprocal transformation, normalized table, eigenvectors, percentage convention, and score rounding are not archived for exact reproduction."),
        (4, 7, 11, "Equation (7) repeats cos(t omega) where a fifth harmonic may be intended and mixes minute language with a 24-hour omega."),
        (5, 9, 12, "The W1 integral has malformed limits and mixed variables, leaving its dimensional and queue interpretation unclear."),
        (5, 10, 12, "The W3 integral repeats the malformed construction and depends on unarchived O(t,B) and k."),
        (5, 11, 12, "The model differentiates discrete booth count B and does not enumerate neighboring integers or prove a global mixed-domain optimum."),
        (6, 15, 13, "Equation (15) uses undefined SD, so the path geometry cannot be independently reconstructed."),
        (6, 16, 14, "The LP omits explicit nonnegativity and probability bounds and does not validate path length as a throughput or safety surrogate."),
    ]
    formula_warnings = [{
        "model_id": f"MU-{ID_STEM}-{model_index:03d}",
        "equation_id": f"EQ-{ID_STEM}-{equation_index:03d}",
        "page": page, "warning": warning,
    } for model_index, equation_index, page, warning in warning_specs]
    dimensions = {dimension: 0 for dimension in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}
    dimensions.update(Counter(item["dimension"] for item in observations))
    return {
        "audit_id": "LA-B-2017-68303-6c8a9ede", "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE, "year": YEAR, "source_sha256": SHA256,
        "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{
            "chapter": item["chapter"], "pass_count": 3, "last_pass_new_moves": 0,
            "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [len(item["anchors"]), 2, 0],
        } for item in CHAPTERS],
        "language_unit_dispositions": [{
            "language_unit_id": unit["language_unit_id"], "disposition": "supports-existing",
            "target_pattern_ids": unit["candidate_pattern_ids"],
            "reason": "The move transfers only after replacing geometry, demand, lane/booth mix, model, simulator, metric, comparator, decision, and evidence-boundary slots.",
        } for unit in units],
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "complete", "weakness_substitution_allowed": False,
            "global_organization_chain": [
                "post-toll fan-in congestion, accident, throughput, and cost problem",
                "four-part requirement map and conditional assumptions",
                "two-shape by two-size by two-pattern taxonomy",
                "VISSIM geometry, demand, conflict, detector, and queue configuration",
                "complete five-index table for eight cases",
                "PCA direction transform, normalization, correlation, contribution, retention, and ranking",
                "half-height experiment that rejects a simple monotonic size assumption",
                "Fourier influx, traveler/booth/construction cost, waiting components, stationary B and H",
                "transition-matrix balance, path geometry, LP objective, and paired-booth lane assignment",
                "return of the selected design to VISSIM and PCA",
                "light/heavy traffic, autonomous vehicle, and booth-composition adjustments",
                "LINGO local reduced-cost and allowable-range sensitivity",
                "source strengths and weaknesses followed by an authority-facing recommendation",
                "only after positive language, organization, model, and visual retention does the final warning pass record arithmetic, notation, dimensional, integer, domain, simulator, safety, and robustness defects",
            ],
            "section_progressions": [{
                "chapter": item["chapter"],
                "moves": [f"input: {item['input']}", f"rhetorical job: {item['rhetorical']}", f"analytical job: {item['analytical']}", f"output: {item['output']}", f"handoff: {item['handoff']}"],
                "positive_pattern": "Retain the source-anchored input -> rhetorical job -> analytical job -> output -> handoff contract; warnings remain the final pass.",
            } for item in CHAPTERS],
            "main_argument_chains": [
                {"claim": "Observed post-toll areas can be organized into eight inspectable design cases.",
                 "support_steps": ["fan-in mechanism", "two trapezoid shapes", "two S/H levels", "normal/stipulated routing", "kind labels", "Figures 1 and 3-10"],
                 "decision_consequence": "use the taxonomy as a comparison frame while requiring a representative plaza inventory and corrected size geometry",
                 "source_pages": [3, 4, 5, 6, 7]},
                {"claim": "VISSIM outputs and PCA can rank the eight designs on cost, traffic, and accident-prevention surrogates.",
                 "support_steps": ["Table 1 inputs", "conflict areas and detectors", "Table 2", "reciprocal transform", "normalization", "correlation/eigenvalues", "three components", "Table 3"],
                 "decision_consequence": "retain model 7's printed rank while requiring a reproducible PCA ledger, calibrated simulation, and validated safety measure",
                 "source_pages": [5, 6, 7, 8, 9, 10]},
                {"claim": "Traveler time, booth operation, and construction cost can jointly select B and H.",
                 "support_steps": ["Fourier F(t)", "W1/W2/W3", "C(B,H)", "VISSIM O(t,B)", "quartic fits", "partial derivatives", "Hessian", "B=6 and H=35.6472"],
                 "decision_consequence": "treat the reported optimum as a candidate until integrals, costs, units, integer B, bounds, and global search are rebuilt",
                 "source_pages": [11, 12]},
                {"claim": "A transition matrix can turn a desired merge pattern into booth-to-lane assignments.",
                 "support_steps": ["uniform P", "uniform Q", "P*T=Q", "normalization", "path length z", "expected path objective g", "base matrix T"],
                 "decision_consequence": "retain the allocation interface while defining SD, all constraints, geometry, and validated operational objectives",
                 "source_pages": [13, 14]},
                {"claim": "The selected candidate improves the paper's comprehensive score.",
                 "support_steps": ["isosceles shape", "B=6", "H=35.6472 m", "stipulated matrix", "VISSIM test", "PCA score 4.3026", "comparison with Table 3"],
                 "decision_consequence": "preserve the reported score as an unreplicated same-pipeline test rather than independent validation",
                 "source_pages": [14, 15]},
                {"claim": "The design and routing can be adjusted across traffic, autonomy, and booth-composition scenarios.",
                 "support_steps": ["close booths in light flow", "restrict routes in heavy flow", "autonomous narrative", "service-rate P'", "T1", "T2", "reduced costs", "allowable ranges"],
                 "decision_consequence": "build a controlled joint scenario surface and global uncertainty analysis before operational or construction use",
                 "source_pages": [15, 16, 17, 18]},
                {"claim": "The authority letter converts the modeling chain into conditional public-agency advice.",
                 "support_steps": ["three objectives", "eight-case baseline", "simulation/PCA", "expanded cost", "shortest path", "traffic regimes", "autonomy", "booth mix", "reality caveat"],
                 "decision_consequence": "use the letter as a staged validation agenda rather than evidence that the design is feasible",
                 "source_pages": [20, 21]},
            ],
        },
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": formula_warnings},
        "model_retention": {
            "model_count": len(models), "retained_model_ids": [item["model_id"] for item in models],
            "retained_equation_ids": equation_ids,
            "central_equations": [{
                "model_id": item["model_id"],
                "equation_ids": [equation_item["equation_id"] for equation_item in item["governing_equations"]],
                "all_central_equations_retained": True,
            } for item in models if item["governing_equations"]],
        },
        "visualization_dispositions": [{
            "paper_card_visual_index": index, "visual_record_id": visual["visual_record_id"],
            "disposition": "important-visual-record", "analytical_purpose": visual["summary"],
        } for index, visual in enumerate(card["visualization_observations"], start=1)],
        "dimension_counts": dimensions, "positive_reusable_language_count": len(units),
        "weakness_record_count": dimensions["weakness"], "review_status": "validated",
        "gate_attestation": {
            "g1_g3_language": "validated-before-G4", "g4_organization": "passed-before-G5-G6",
            "g5_models": "validated-before-G7", "g6_visuals": "passed-before-G7",
            "g7_warning_mode": "last-pass-warning-only", "g7_warning_count": len(formula_warnings),
            "warnings_strict_minority_of_language": len(formula_warnings) < len(units),
            "request_body_guard": {"bounded_jpeg_proxies": 8, "total_proxy_bytes": 1402778,
                                   "largest_proxy_bytes": 253479, "original_full_page_png_in_context": False},
        },
    }


def build_extraction() -> dict:
    extraction = json.loads(SOURCE_EXTRACTION.read_text(encoding="utf-8"))
    if extraction.get("visual_review_status") != "complete":
        raise SystemExit("q117 extraction does not contain completed visual review")
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
    print(json.dumps({
        "stage": str(STAGE), "chapters": len(language["available_chapters"]),
        "language_units": len(language["units"]), "models": len(models_record["models"]),
        "equations": sum(len(item["governing_equations"]) for item in models_record["models"]),
        "dependency_edges": len(models_record["dependency_edges"]),
        "visual_records": len(card["visualization_observations"]),
        "observations": Counter(item["dimension"] for item in observations),
        "formula_warnings": len(audit["formula_error_watch"]["warnings"]),
        "unresolved_questions": len(card["unresolved_questions"]),
    }, indent=2, default=dict))


if __name__ == "__main__":
    main()
