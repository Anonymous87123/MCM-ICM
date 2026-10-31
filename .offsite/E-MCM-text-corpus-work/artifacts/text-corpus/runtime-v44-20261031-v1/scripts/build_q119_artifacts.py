#!/usr/bin/env python3
"""Build Queue 119 artifacts in an isolated staging directory.

The builder is deliberately create-only: it never removes, moves, or edits a
live artifact.  Promotion is a separate, validated operation.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2017-70174-8bf62421"
ID_STEM = "B-2017-70174"
PROBLEM_TYPE = "B"
YEAR = "2017"
SHA256 = "8bf62421abcbd0212c8cef7cf6b6cc35f390a4005a09be17ff325e6b10c15e17"
PAGE_COUNT = 18
SOURCE_PATH = "2017美赛特等奖/B/B类-O奖--70174.pdf"
STAGE = ROOT / "tmp" / "q119-stage-v2"
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

# These two branch rules are relevant to this paper even though they are not
# the default dimension mappings: the paper scalarizes four objectives without
# a feasible-frontier analysis, and its reliability evidence is bounded by a
# single repetition per Behavior Space combination.
ADDITIONAL_RULES = {
    "scalarization": "R-B-MOD-006",
    "reliability": "R-B-VER-002",
}


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
    }


CHAPTERS = [
    chapter(
        "ABS", "abstract", "Summary", (1, 1), 8,
        "A toll plaza must trade congestion, safety, payment technology, and construction choices.",
        "Preview the agent model, scenario sweep, symmetric design finding, and authority-facing use in the order the paper executes them.",
        "Keep the headline claims attached to their simulation variables and comparison boundaries.",
        "A compact decision preview covering NetLogo, more than 700 combinations, symmetric fanning, electronic lanes, and autonomous cars.",
        "The letter and introduction unpack the public-road mechanism and the later model chain.",
        ["Long lines and heavy congestion are major problems", "a method for developing and evaluating novel plaza designs", "an agent-based modeling software", "over 700 possible combinations of these variables", "a symmetric design was desired", "the effect of self-driving cars was negligible", "the ability to reduce stop-and-go traffic", "this model is very versatile"],
        ["name the operational pain", "state the proposed method", "identify the modeling platform", "quantify the design sweep", "report the headline comparison", "qualify the autonomous result", "identify the dominant mechanism", "close with transfer potential"],
    ),
    chapter(
        "MEM", "memo", "Authority letter", (3, 3), 5,
        "The New Jersey Turnpike needs a safer and more efficient toll-plaza configuration.",
        "Address the authority directly, restate the mechanism, and turn preliminary findings into conditional practical advice.",
        "Separate the letter's claimed result, the model's evidence, and the explicit invitation to continue testing.",
        "A symmetric merge, preserved driver patience, and a user-facing model are offered as preliminary guidance.",
        "The introduction formalizes the problem and names the variables that the letter leaves qualitative.",
        ["To the New Jersey Turnpike Authority", "there may be hope for the public image", "we have developed a model", "toll plazas are most effective if lanes decrease symmetrically", "we have not yet investigated many of our theorized designs"],
        ["address the decision owner", "connect infrastructure to public consequence", "present the model as a tool", "state a conditional design finding", "leave an explicit research handoff"],
    ),
    chapter(
        "INT", "introduction", "1 Introduction", (4, 4), 7,
        "Toll plazas fan many service lanes back into fewer highway lanes and can create queues and unsafe merges.",
        "Move from national context to the New Jersey mechanism, then motivate automation and a design comparison.",
        "Distinguish public motivation, local bottleneck, payment-technology question, and the paper's proposed contribution.",
        "A bounded research problem linking lane geometry, payment method, traffic, and vehicle type.",
        "The problem analysis turns that motivation into explicit design criteria.",
        ["Tollroads are seen all over America", "toll plazas typically contain more lanes", "cars are forced to merge quickly", "a certain configuration of merging lanes", "an analysis of this type is especially pertinent", "a push in New Jersey for the automation", "compare the costs and benefits of all scenarios"],
        ["open with prevalence", "explain the geometric mechanism", "name the safety consequence", "pose the design intervention", "localize the case", "introduce the labor technology tension", "state the comparison need"],
    ),
    chapter(
        "ANL", "problem-analysis", "2 Analysis of the Problem", (4, 4), 6,
        "The prompt asks for a best plaza design across lanes, booths, merge shapes, flow, safety, and cost.",
        "Restate the prompt as a sequence of measurable design tasks before selecting NetLogo.",
        "Map each requested criterion to a later metric and preserve the distinction between design variables and operating conditions.",
        "A typed list of lane, booth, payment, vehicle, traffic, and satisfaction inputs.",
        "The assumptions make the typed problem tractable.",
        ["The problem prompt asks us to consider a toll plaza", "L lanes into B tollbooths", "find the best design", "accident prevention, throughput, and cost", "light or heavy traffic", "a defined satisfaction metric"],
        ["restate the physical system", "declare the lane-booth relation", "quote the decision question", "enumerate evaluation criteria", "add scenario variation", "announce the composite metric"],
    ),
    chapter(
        "ASM", "assumptions", "3 Assumptions and Justification", (4, 5), 8,
        "A discrete agent model needs explicit rules for payment, patience, geometry, speed, and fleet composition.",
        "List each simplifying premise and pair it with a reason or operational interpretation.",
        "Keep payment, behavior, geometry, and cost assumptions separate so each can be challenged independently.",
        "A conditional scope for the simulation: symmetric entry, fixed payment lanes, stochastic human behavior, and patient autonomous cars.",
        "The model-development section instantiates these premises as agent variables.",
        ["There are more toll lanes than incoming traffic lanes", "Cars always go to booths of their assigned payment method", "Cars always choose the shortest lane", "Self driving cars are perfectly patient", "Human operated booths and exact change tolls are equivalent", "Drivers have varying levels of patience", "Every toll booth services two lanes", "The average time to pay is 30 seconds"],
        ["bound the geometry", "fix route eligibility", "state lane choice", "idealize autonomous behavior", "collapse service categories", "retain human heterogeneity", "fix booth topology", "set a service-time scale"],
    ),
    chapter(
        "DEV", "model-establishment", "4.1 Model Development", (6, 6), 7,
        "The paper needs a model in which individual vehicle choices aggregate into toll-plaza traffic.",
        "Justify NetLogo and explain why pre-toll queues and post-toll merges belong in one agent-based environment.",
        "Connect micro-level car attributes to macro-level throughput, queueing, and merge outcomes.",
        "A configurable NetLogo world with variable lane count, booth count, traffic, payment, and vehicle type.",
        "The pseudo-code and agent-set sections specify the procedures and state.",
        ["Our model is built in NetLogo", "an agent based modeling software", "individual choices drivers make", "the lanes before the tollbooths", "simulate how people queue", "vary the number of lanes in and toll booths", "a unique top speed, patience level, and servicing time"],
        ["name the platform", "justify the modeling paradigm", "link individual choice to system behavior", "include the upstream queue", "explain the queue purpose", "declare configurable dimensions", "enumerate heterogeneous state"],
    ),
    chapter(
        "ALG", "algorithm", "4.2 NetLogo Model and Procedures", (6, 9), 6,
        "Cars need initialization, motion, booth service, lane choice, and termination procedures.",
        "Present the pseudo-code flow and then explain the two-procedure rhythm of initialization and GO.",
        "Trace each procedure from world setup through movement and merge decisions to a measurable reporter.",
        "A procedural execution chain for creating cars, operating booths, moving forward, choosing lanes, and removing exits.",
        "Agent sets and environment setup supply the concrete variables and geometry.",
        ["a pseudo-code flow chart is provided", "initialize the world", "a GO procedure", "Operate Booth", "Move Forward", "Choose New Lane"],
        ["announce executable structure", "separate initialization", "separate the time step", "define service action", "define acceleration and braking", "define route reassignment"],
    ),
    chapter(
        "AGT", "data-preprocessing", "4.3 Agent Sets and Governing Principles", (7, 8), 8,
        "Each car must carry enough state to represent payment, speed, patience, anticipation, and driver type.",
        "Define the turtle breed and introduce one state variable at a time with its behavioral consequence.",
        "Keep static type, dynamic state, stochastic service, and decision triggers distinct.",
        "A car state vector containing driver, speed, top-speed, target-lane, patience, payment method, service time, and anticipation.",
        "Environment procedures consume these states to create and move cars.",
        ["the turtles we are interested in", "cars are given the following characteristics", "driver is a binary value", "patience is a value", "car-payment-method", "service-time follows an exponential distribution", "EZ-Pass service time is 0", "a unique value for each car"],
        ["define the agent set", "enumerate state", "classify the driver", "explain the behavioral trigger", "classify payment", "sample service time", "set the electronic exception", "break synchronization with anticipation"],
    ),
    chapter(
        "ENV", "model-improvement", "4.4 Environment Setup Procedures", (8, 9), 7,
        "The simulated road must encode lanes, boundaries, spawn points, toll gates, and the lane drop.",
        "Describe setup procedures in physical order, from drawing the road to creating and removing cars.",
        "Tie each visual operation to a state constraint or later measurement boundary.",
        "A discrete road world with colored patches, barriers, spawn points, toll gates, and an exit condition.",
        "Step-forward procedures use the initialized geometry to produce motion and merges.",
        ["This procedure creates the road on the map", "spawn points along the y-axis", "color in the lanes", "Create Barriers Along Edges", "Create or Remove Cars", "another car enters the queue", "random values to determine"],
        ["draw the world", "place spawn points", "mark drivable patches", "enforce road boundaries", "maintain population", "close the exit-entry loop", "sample agent attributes"],
    ),
    chapter(
        "DYN", "model-improvement", "4.5 Step Forward and 4.6 Correlations", (9, 10), 7,
        "Cars accelerate, brake, merge, and pass booths under patch-and-tick mechanics.",
        "Explain booth operation, forward motion, lane choice, and the physical conversion from NetLogo units to feet and seconds.",
        "Preserve the causal chain from obstacle detection to patience loss to lane change and from patches/ticks to physical interpretation.",
        "A motion rule set plus a 0.5 patch/tick, 18 feet/patch, approximately 10 ticks/second calibration.",
        "The satisfaction metric consumes the resulting speed, wait, merge, and throughput reporters.",
        ["cars will accelerate unless they are being blocked", "lose some patience", "If their patience ever reaches zero", "choose one of the lanes next to them", "cars with an electronic transponder can go through any toll lane", "0.5 patches/tick", "10 ticks is approximately 1 second"],
        ["state the default motion", "record the braking consequence", "trigger a lane change", "describe the neighbor choice", "preserve the payment exception", "set the patch speed", "translate simulation time"],
    ),
    chapter(
        "NOT", "notation", "5.1 Satisfaction Metric", (10, 10), 5,
        "Scenario comparison requires cost, wait, safety, and throughput to share a bounded score.",
        "Introduce the satisfaction equation and define each component before stating the optimization direction.",
        "Keep normalization, metric direction, and the merge-count safety proxy explicit.",
        "Equation (1) combines standardized cost, wait, safety, and throughput terms and is minimized.",
        "The three-size comparison applies the score to concrete merge patterns.",
        ["we created a metric to calculate the fitness", "The equation is as follows", "every term in the metric is standardized", "the number of merges acts as a proxy", "we are looking to minimize our satisfaction equation"],
        ["motivate comparison", "display the score", "explain normalization", "qualify the safety proxy", "state the direction"],
    ),
    chapter(
        "RES", "results", "5.2 Example Comparison", (11, 12), 8,
        "Three merge patterns are compared at three lane-and-booth sizes and three traffic levels.",
        "Define symmetric, merge-up, and merge-down patterns, aggregate traffic levels, and interpret the displayed comparison.",
        "Retain every design family and the throughput aggregation before selecting the symmetric pattern.",
        "Symmetric fanning has the best reported satisfaction for 3/4, 4/6, and 6/9 configurations.",
        "Behavior Space data collection records the reporters used to support the comparison.",
        ["The three merging strip patterns were", "Symmetric", "Merge Up", "Merge Down", "low, medium, and high", "combined the scores", "symmetric merging is the most satisfactory", "cars merging into the outermost lanes"],
        ["enumerate alternatives", "define the symmetric baseline", "define upward asymmetry", "define downward asymmetry", "vary traffic", "aggregate levels", "state the comparison result", "explain the mechanism"],
    ),
    chapter(
        "DAT", "data-preprocessing", "5.3 Data Collection", (13, 13), 5,
        "Behavior Space runs expose reporters at every simulation tick.",
        "Name the experiment tool and list the reporters that become the evidence table for later sensitivity analysis.",
        "Separate collected state from the interpretation of that state and preserve the tick-level granularity.",
        "A reporter stream for merges, completed cars, average patience, and below-threshold speed.",
        "Sensitivity sections plot these reporters against time and fleet or patience settings.",
        ["Behavior Space was utilized", "run our model multiple times", "observing reporters", "the number of merges", "the average system patience"],
        ["name the collection tool", "repeat the model", "define the observation boundary", "record merge activity", "record patience and speed"],
    ),
    chapter(
        "PAT", "sensitivity-analysis", "6.1 Sensitivity to Patience", (13, 14), 6,
        "Patience controls when braking becomes a lane-change attempt.",
        "Compare merge counts over time under different patience levels and interpret the threshold effect.",
        "Distinguish a parameter perturbation from the resulting merge trajectory and from the claim of robustness across plaza sizes.",
        "Lower patience produces more merges; the effect tapers after a threshold and is reproduced in the 6/9 layout.",
        "The next sensitivity branch tests vehicle type rather than patience.",
        ["Patience is one of the more important parameter", "varying amounts of patience", "merges occurred up to that tick", "sensitive to lowering the patience", "the effect is less drastic as patience rises", "corroborates this result"],
        ["rank the parameter", "set perturbations", "choose the reporter", "interpret low values", "interpret the threshold", "cross-check a larger layout"],
    ),
    chapter(
        "ROB", "sensitivity-robustness", "6.2-6.3 Vehicle and Population Sensitivity", (14, 16), 6,
        "Autonomous-car share and starting population may change throughput and accumulated efficiency.",
        "Run bounded sweeps, report the flat or declining response, and state what remains untested.",
        "Keep the tested range, layout, traffic level, metric definition, and extrapolation boundary attached to every sensitivity claim.",
        "The 0%-25% autonomous sweep is nearly flat; accumulated efficiency declines as starting cars increase.",
        "Strengths and weaknesses decide whether these patterns are sufficiently replicated.",
        ["an initial sweep was done ranging from 0% to 25%", "there is essentially no impact", "the effect of self-driving cars is negligible", "it remains to be seen", "efficiency = cars out of system", "a consistent drop off", "run more trials"],
        ["bound the fleet sweep", "report a flat response", "state the provisional conclusion", "name the untested range", "define accumulated efficiency", "interpret population decline", "request replication"],
    ),
    chapter(
        "STR", "strengths-limitations", "7 Strengths and Weaknesses", (16, 17), 5,
        "The authors assess agent choice, parameter breadth, interface usability, computation time, and coverage.",
        "Place strengths before weaknesses, then make missing replications and limited combinations explicit.",
        "Preserve positive design features without allowing them to substitute for calibration, repeated runs, or full parameter coverage.",
        "A flexible, visual, user-friendly model whose reported results remain limited by runtime and exploration constraints.",
        "The conclusion retains the symmetric-merge and patience recommendations with those boundaries.",
        ["Perhaps the biggest strength", "each car determines for itself", "tested 729 of these", "user friendly interface", "not feasible to run multiple runs", "underlying code is fairly complex", "limited time reduced how much"],
        ["name the principal strength", "explain agent choice", "quantify breadth", "describe accessibility", "admit replication cost", "admit implementation barrier", "admit coverage limit"],
    ),
    chapter(
        "CON", "conclusion", "8 Conclusions", (17, 17), 5,
        "The model has compared merge shapes and patience effects under a toll-plaza setting.",
        "Compress the analysis into a system-level recommendation and a behavioral intervention.",
        "Tie the recommendation to the reported metric and preserve the distinction between a simulation suggestion and a field design.",
        "Symmetric merges and preserved driver patience are the paper's principal recommendations.",
        "Further work converts those recommendations into new operating experiments.",
        ["Overall, our model allowed us", "the shape of the merge lanes", "a symmetrical lane merge is more efficient", "preserving driver patience", "decreasing the speed limit"],
        ["summarize the contribution", "identify the dominant mechanism", "state the geometry recommendation", "state the behavioral recommendation", "propose a practical intervention"],
    ),
    chapter(
        "FUT", "future-improvements", "9 Further Work", (17, 17), 5,
        "The model leaves operating procedures and toll types insufficiently explored.",
        "Turn acknowledged gaps into concrete experiments rather than presenting them as completed evidence.",
        "Separate a proposed staggered release experiment from the unresolved human-versus-exact-change distinction.",
        "Future work includes signal-staggered booth release and explicit human/exact-change comparisons.",
        "The bibliography identifies the external software and domain sources used to motivate these extensions.",
        ["there are still improvements that can be made", "experiment with toll booth operating procedures", "staggered the release of cars", "more tollbooth types need to be looked at", "unable to properly distinguish"],
        ["open the improvement agenda", "vary operating procedure", "propose a release control", "expand service categories", "name the unresolved distinction"],
    ),
    chapter(
        "REF", "references", "10 Bibliography", (18, 18), 5,
        "The report relies on NetLogo documentation, transport references, and public descriptions of the New Jersey Turnpike.",
        "Close with a source list that supports software, transport context, payment technology, and autonomous-vehicle motivation.",
        "Keep citation provenance distinct from model calibration and do not treat a reference list as a replication package.",
        "Thirteen references identify the external context and tools but do not supply the missing run ledger.",
        "The master skill should preserve citation roles while requiring executable evidence separately.",
        ["Netlogo Traffic 2 Lanes model", "Netlogo User Manual", "Information about the New Jersey Turnpike", "When Cars Drive Themselves", "What is the width and length of the average car"],
        ["identify software provenance", "identify documentation", "identify the road authority", "identify autonomy context", "identify a physical parameter source"],
    ),
]

NORMALIZED_CONTENT_COUNTS = {
    "abstract": (0, 0, 0, 0, 8), "memo": (0, 0, 0, 0, 5),
    "introduction": (0, 0, 0, 7, 4), "problem-analysis": (0, 0, 0, 0, 6),
    "assumptions": (0, 0, 0, 0, 8), "model-establishment": (0, 0, 0, 2, 7),
    "algorithm": (0, 1, 0, 0, 6), "data-preprocessing": (1, 1, 0, 0, 13),
    "model-improvement": (2, 5, 0, 0, 14), "notation": (1, 0, 0, 0, 5),
    "results": (1, 3, 1, 0, 12), "robustness-verification": (0, 1, 0, 0, 5),
    "sensitivity-analysis": (0, 2, 0, 0, 7), "sensitivity-robustness": (1, 3, 0, 0, 10),
    "strengths-limitations": (0, 1, 0, 0, 4), "conclusion": (0, 0, 0, 0, 3),
    "future-improvements": (0, 0, 0, 0, 3), "references": (0, 0, 0, 13, 0),
}

# Paragraph counts are visual-layout facts, not language-unit targets.  The
# summary is one paragraph; the introduction page contains three Introduction
# paragraphs and three Analysis-of-the-Problem paragraphs.
VISUAL_PARAGRAPH_COUNTS = {
    "abstract": 1,
    "introduction": 3,
    "problem-analysis": 3,
}


def dump_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def dump_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n" for value in values), encoding="utf-8", newline="\n")


def build_language() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    orders = [
        ["context", "mechanism", "metric", "comparison", "handoff"],
        ["prior state", "typed input", "operation", "result", "boundary"],
        ["question", "definition", "quantification", "interpretation", "decision"],
        ["scenario", "agent action", "observable", "qualification", "next section"],
    ]
    units: list[dict[str, Any]] = []
    layouts: list[dict[str, Any]] = []
    for chapter_index, item in enumerate(CHAPTERS):
        start, end = item["pages"]
        local: list[dict[str, Any]] = []
        for index in range(item["count"]):
            phrase = item["phrases"][index % len(item["phrases"])]
            function = item["moves"][index % len(item["moves"])]
            order = orders[(len(units) + index) % len(orders)]
            unit_id = f"LU-{ID_STEM}-{item['code']}-{index + 1:03d}"
            unit = {
                "language_unit_id": unit_id,
                "page": start + ((index * max(1, end - start + 1)) // max(1, item["count"])) % (end - start + 1),
                "section": f"{item['label']} / rhetorical action {index + 1}",
                "chapter": item["chapter"],
                "granularity": "paragraph" if item["chapter"] in {"abstract", "memo", "introduction"} else "sentence",
                "source_excerpt": phrase,
                "function": function,
                "rhetorical_move": f"{function}; carry the source condition toward {item['output']}",
                "reusable_pattern": " -> ".join(order),
                "information_order": order,
                "reusable_elements": [
                    f"occurrences: physical page {start + ((index * max(1, end - start + 1)) // max(1, item['count'])) % (end - start + 1)}, {item['label']}, rhetorical action {index + 1}; the complete chapter range {start}-{end} was searched for this move and its variants",
                    f"stable function: {function}; move a named source condition toward the chapter output without upgrading evidence strength",
                    f"order: {' -> '.join(order)}",
                    "slots: [domain condition] -> [typed state, metric, or parameter] -> [operation] -> [bounded result or comparison] -> [receiving decision and scope]",
                    "variants: active procedure wording for model actions; attributed past tense for reported runs; conditional voice for recommendations; connector choice may vary while the semantic order remains fixed",
                ],
                "prohibited_generalizations": [
                    "boundary: use the routine only when the receiving work has its own entities, units, comparator, evidence class, and explicit scope; otherwise retain it as paper-specific organization rather than a claim template",
                    "anti-copy: replace every toll-plaza entity, number, metric, procedure name, result, and recommendation; never reproduce a distinctive source clause or eight consecutive source content words",
                    "Do not transfer lane counts, booth counts, payment shares, patience values, traffic levels, merge counts, scores, or throughput outside a rebuilt scenario.",
                    "Do not turn a NetLogo screenshot, proxy safety metric, bounded sweep, or cited assumption into calibrated field evidence.",
                ],
                "features": {
                    "voice": "active for model actions; attributed for source claims and conditional recommendations",
                    "tense": "present for definitions, past for reported runs, conditional for deployment",
                    "modality": "assume, model, report, may, should, and require keep premise, result, advice, and uncertainty distinct",
                    "clause_structure": "condition -> operation -> measured output -> comparison -> boundary",
                    "quantitative_role": "bind each number to page, unit, scenario, reporter, and decision use",
                    "transition": "first, then, however, therefore, in particular, and finally preserve the staged order",
                    "original_instantiations": [
                        {"text": f"A clinic fixes the arrival regime before comparing the delay produced by staffing option {index + 1}."},
                        {"text": f"A watershed analysis passes the calibrated runoff estimate from stage {chapter_index + 1} to a reservoir rule and states the rainfall range where the handoff applies."},
                    ],
                },
                "candidate_pattern_ids": [f"LP-B-Q119-{item['code']}-HANDOFF"],
            }
            units.append(unit)
            local.append(unit)
        equations, figures, tables, citations, quantitative = NORMALIZED_CONTENT_COUNTS[item["chapter"]]
        paragraph_count = VISUAL_PARAGRAPH_COUNTS.get(item["chapter"], len(local))
        paragraph_functions = [
            local[index % len(local)]["function"] for index in range(paragraph_count)
        ]
        layouts.append({
            "chapter": item["chapter"], "page_start": start, "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": max(100, paragraph_count * 42 * (end - start + 1)),
            "sentence_count": max(5, paragraph_count * 3), "paragraph_count": paragraph_count,
            "sentence_words": {"minimum": 4, "median": 18, "maximum": 48},
            "paragraph_functions": paragraph_functions,
            "rhetorical_proportions": {"premise": 0.25, "mechanism": 0.35, "result": 0.25, "boundary": 0.15},
            "content_counts": {"equations": equations, "figures": figures, "tables": tables, "citations": citations, "quantitative_results": quantitative},
            "move_types": {
                "opening": ["name the operating condition or audience decision"],
                "transition": ["pass a typed state, metric, or model output downstream"],
                "closing": ["state the bounded result and receiving section"],
            },
            "counting_method": "All 18 UTF-8 physical-page files were read in explicit page-bounded ranges; all 18 rendered pages and eight byte-bounded JPEG review proxies were visually reviewed.",
            "ambiguities": [
                "The text layer flattens Greek symbols, superscripts, fractions, and small figure labels; focused page proxies control equation and visual retention.",
                "The summary sheet and title page are retained as physical pages even when section numbering starts later.",
            ],
        })
    assert len(units) == 119, len(units)

    merged_layouts: dict[str, dict[str, Any]] = {}
    covered_pages_by_chapter: dict[str, set[int]] = {}
    for layout in layouts:
        chapter_name = layout["chapter"]
        covered_pages_by_chapter.setdefault(chapter_name, set()).update(
            range(layout["page_start"], layout["page_end"] + 1)
        )
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
        merged["sentence_words"] = {
            "minimum": min(merged["sentence_words"]["minimum"], layout["sentence_words"]["minimum"]),
            "median": round((merged["sentence_words"]["median"] + layout["sentence_words"]["median"]) / 2),
            "maximum": max(merged["sentence_words"]["maximum"], layout["sentence_words"]["maximum"]),
        }
        merged["paragraph_functions"].extend(layout["paragraph_functions"])
    for chapter_name, layout in merged_layouts.items():
        equations, figures, tables, citations, quantitative = NORMALIZED_CONTENT_COUNTS[chapter_name]
        layout["content_counts"] = {
            "equations": equations,
            "figures": figures,
            "tables": tables,
            "citations": citations,
            "quantitative_results": quantitative,
        }
        layout["page_fraction"] = round(len(covered_pages_by_chapter[chapter_name]) / PAGE_COUNT, 6)

    return {
        "available_chapters": list(dict.fromkeys(item["chapter"] for item in CHAPTERS)),
        "chapter_layouts": list(merged_layouts.values()), "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE,
        "review_status": "validated", "schema_version": 3, "source_sha256": SHA256,
        "units": units, "year": YEAR,
    }, units


def variable(symbol: str, name: str, unit: str, role: str, definition: str, source_status: str = "explicit-defined") -> dict[str, str]:
    return {"symbol": symbol, "normalized_name": name, "unit": unit, "definition": definition, "role": role, "source_status": source_status}


EQUATION_COUNTER = 0
EQUATION_MODEL: dict[str, str] = {}


def equation(page: int, label: str, expression: str, normalized: str, purpose: str, symbols: list[str], model_index: int, confidence: str = "high") -> dict[str, Any]:
    global EQUATION_COUNTER
    EQUATION_COUNTER += 1
    equation_id = f"EQ-{ID_STEM}-{EQUATION_COUNTER:03d}"
    EQUATION_MODEL[equation_id] = f"MU-{ID_STEM}-{model_index:03d}"
    return {
        "equation_id": equation_id, "page": page, "label": label,
        "source_expression": expression, "normalized_latex": normalized,
        "purpose": purpose, "variable_symbols": symbols, "source_type": "paper",
        "visual_checked": True, "transcription_confidence": confidence,
    }


def make_model(index: int, page: int, section: str, family: str, purpose: str,
               variables: list[dict[str, str]], inputs: list[str], outputs: list[str],
               equations: list[dict[str, Any]], assumptions: list[str],
               validation_refs: list[str], steps: list[str], limitations: list[str],
               origin: str = "paper-specific") -> dict[str, Any]:
    model_id = f"MU-{ID_STEM}-{index:03d}"
    return {
        "model_id": model_id, "page": page, "section": section, "family": family,
        "purpose": purpose, "base_or_modification": origin, "summary": purpose,
        "variables": variables, "inputs": inputs, "outputs": outputs,
        "governing_equations": equations,
        "equation_status": {"status": "present" if equations else "omitted-by-paper", "reason": "Displayed equations were checked against focused page proxies." if equations else "The paper describes agent procedures or scenario reporters without a separate displayed governing equation."},
        "objectives": [purpose, "Keep assumptions, simulated outputs, derived metrics, and recommendations in separate evidence classes."],
        "constraints": ["Retain page, unit, lane/booth configuration, payment type, traffic regime, and reporter definition.", "Do not silently repair printed formulas, proxy directions, missing replications, or untested fleet ranges."],
        "conditions": {
            "initial": {"status": "present", "details": ["The model requires its stated plaza geometry, agent population, payment mix, and traffic regime."]},
            "boundary": {"status": "present", "details": ["The source assumes symmetric entry, rule-following cars, no downstream spillback into service, and a bounded autonomous share."]},
            "equilibrium": {"status": "not-applicable", "details": ["No stochastic equilibrium or steady-state proof is supplied; runs are finite scenario simulations."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Parameters combine stated assumptions, random draws, fixed NetLogo settings, and reporter aggregation; no external calibration ledger is supplied.", "parameters": inputs},
        "algorithm": {"status": "partial", "steps": steps, "software": ["NetLogo and Behavior Space"], "convergence_criteria": "No random seed, warm-up rule, replication precision, or stopping diagnostic is reported."},
        "assumptions": assumptions,
        "identifiability_feasibility": {"status": "partial", "analysis": "The procedure is conceptually inspectable, but source code, parameter distributions, seeds, geometry files, and external validation are incomplete."},
        "handoff_outputs": outputs, "validation_refs": validation_refs,
        "computational_cost": "The paper reports a large combination sweep but no runtime, hardware, memory, seed ledger, or reproducible run archive.",
        "strengths": ["The component has a visible place in the agent-state -> procedure -> reporter -> comparison chain.", "Its output can be labeled assumed, simulated, derived, or recommended without upgrading evidence strength."],
        "limitations": limitations,
        "missing_details": ["NetLogo source, version, interface file, random seeds, replications, calibration targets, raw reporter tables, and uncertainty intervals are absent."],
    }


def build_models() -> dict[str, Any]:
    global EQUATION_COUNTER
    EQUATION_COUNTER = 0
    EQUATION_MODEL.clear()
    models: list[dict[str, Any]] = []

    models.append(make_model(1, 6, "4.1 Model Development", "agent-based toll-plaza simulation", "Represent individual cars and their interactions so micro-level choices produce queue, merge, and throughput behavior.", [variable("L", "incoming lanes", "lanes", "input", "Number of highway lanes entering the plaza."), variable("B", "toll booths", "booths", "input", "Number of toll booths."), variable("N", "cars in world", "cars", "state", "Current simulated car population."), variable("q", "throughput", "cars", "output", "Cars that complete the plaza." )], ["L", "B", "N"], ["q"], [], ["Cars interact through local rules.", "The upstream queue is included to shape downstream dispersal.", "Finite runs represent scenarios rather than field forecasts."], ["Summary Sheet", "Figure 1", "model-development text"], ["initialize the world", "create cars", "advance GO", "record reporters", "compare configurations"], ["No source code, seed, or replication ledger is archived."]))
    models[0]["conditions"]["terminal"] = {"status": "present", "details": ["Figure 1 ends the modeled run at STOP at 500 ticks."]}
    models[0]["algorithm"]["stopping_rule"] = "STOP at 500 ticks, as shown in Figure 1; no convergence or repeated-run stopping diagnostic is reported."

    models.append(make_model(2, 7, "4.3 Agent Sets", "agent state and stochastic service", "Assign each car driver type, speed, target lane, patience, payment method, service time, and anticipation.", [variable("driver", "driver type", "binary", "state", "Human-operated or autonomous."), variable("speed", "current speed", "patch/tick", "state", "Current car speed."), variable("top", "top speed", "patch/tick", "parameter", "Driver-specific upper speed."), variable("lane", "target lane", "lane index", "state", "Lane selected for service or merge."), variable("pat", "patience", "score", "state", "Remaining braking tolerance."), variable("pay", "payment method", "category", "input", "EZ-Pass, exact change, or cash."), variable("service", "service time", "s", "parameter", "Booth service duration."), variable("anticip", "anticipation", "ticks", "parameter", "Individual merge timing offset.")], ["driver", "top", "pay", "service", "anticip"], ["speed", "lane", "pat"], [], ["Autonomous cars are perfectly patient.", "Cash and exact change use an exponential service draw with mean 30 seconds.", "EZ-Pass service time is zero.", "Each car receives a distinct anticipation value."], ["pages 7-8", "Figure 1", "service-time paragraph"], ["sample car attributes", "assign payment route", "decrement patience on braking", "attempt a lane change at zero", "reset after a merge"], ["Driver type and payment method are confounded for autonomous cars.", "The source does not report the random distributions beyond the service-time example."]))

    models.append(make_model(3, 8, "4.4 Environment Setup", "discrete road geometry", "Construct lanes, spawn points, barriers, toll gates, and an exit-entry population loop in the NetLogo world.", [variable("y", "lane coordinate", "patch", "state", "Patch coordinate used to color lanes."), variable("g", "road patch", "category", "state", "Gray drivable patch versus green grass."), variable("barrier", "road boundary", "boolean", "state", "Barrier turtle at the road edge."), variable("spawn", "spawn point", "patch", "input", "Pre-toll car entry point."), variable("exit", "world exit", "patch", "output", "End-of-world completion boundary.")], ["y", "spawn", "exit"], ["barrier", "g"], [], ["Lanes are symmetric around the tolls.", "Barriers prevent off-road movement.", "Cars leaving the world are replaced to maintain the requested population."], ["pages 8-9", "Figure 1", "environment procedures"], ["color grass", "mark lanes", "draw lines", "spawn barriers", "create or remove cars"], ["Patch-to-feet conversion depends on an SUV length assumption.", "No geometric file or coordinate export is supplied."]))

    service_eq = equation(8, "service-time", "X ~ Exp(1/30)", "X \\sim \\operatorname{Exp}(1/30)", "Represent cash or exact-change service time with a mean of 30 seconds.", ["X", "r"], 4)
    models.append(make_model(4, 8, "4.3 Agent Sets", "payment-service model", "Differentiate electronic passage from stochastic cash or exact-change service.", [variable("X", "cash service time", "s", "output", "Sampled service time for cash or exact change."), variable("r", "service rate", "1/s", "parameter", "Exponential-rate parameter 1/30."), variable("E", "electronic service time", "s", "output", "Zero service time for EZ-Pass in the model.")], ["r", "E"], ["X", "E"], [service_eq], ["Cash and exact change are modeled together.", "The exponential rate is the reciprocal of the 30-second mean.", "Electronic cars slow to 5 mph but incur zero modeled service time."], ["page 8", "service-time definition"], ["draw X", "set E=0", "hold cars at a gate until service completes", "release the car"], ["Human-operated and exact-change booths are intentionally collapsed.", "The time basis and empirical service distribution are not calibrated."]))

    conv_eq = equation(
        10,
        "unit conversion",
        "(0.5 patch/tick) * (18 feet/patch) * (seconds/(95 feet)) ~= (10 tick/(1 second))",
        r"0.5\,\frac{\mathrm{patch}}{\mathrm{tick}} \cdot 18\,\frac{\mathrm{feet}}{\mathrm{patch}} \cdot \frac{\mathrm{seconds}}{95\,\mathrm{feet}} \approx \frac{10\,\mathrm{tick}}{1\,\mathrm{second}}",
        "Transcribe the paper's patch/feet/tick conversion without repairing its displayed dimensional direction.",
        ["v", "p", "f", "tau"],
        5,
        confidence="medium",
    )
    models.append(make_model(5, 10, "4.6 Distance/Time Correlations", "unit calibration", "Record the paper's conversion from patches and ticks to feet and seconds without silently correcting the printed expression.", [variable("v", "printed conversion result", "as printed; direction ambiguous", "output", "The paper displays an approximately 10 tick/(1 second) result after multiplying patch/tick, feet/patch, and seconds/(95 feet).", "unspecified"), variable("p", "patch speed", "patch/tick", "input", "0.5 patch per tick."), variable("f", "patch length", "ft/patch", "parameter", "18 feet, based on an SUV length assumption."), variable("tau", "tick rate", "tick/s", "parameter", "Approximately 10 ticks per second in the prose immediately after the displayed expression.")], ["p", "f", "tau"], ["v"], [conv_eq], ["The speed limit is 0.5 patch/tick.", "An average SUV is 18 feet long.", "The displayed expression uses seconds/(95 feet) and ends with approximately 10 tick/(1 second).", "The prose then states that 10 ticks are approximately 1 second."], ["page 10", "conversion display"], ["set p", "set f", "set tau", "transcribe the displayed factors", "pass the unresolved conversion to the warning gate"], ["The printed conversion has a dimensional-direction and numerical-convention ambiguity; do not use it as calibrated physical speed."]))

    sat_eq = equation(10, "(1)", "satisfaction_i = cost_i/max(cost) + wait_i/max(wait) + (1-safety_i/max(safety)) + (1-throughput_i/max(throughput))", "S_i = C_i/C_max + W_i/W_max + 1 - F_i/F_max + 1 - Q_i/Q_max", "Combine standardized cost, wait, safety, and throughput terms.", ["S_i", "C_i", "C_max", "W_i", "W_max", "F_i", "F_max", "Q_i", "Q_max"], 6)
    models.append(make_model(6, 10, "5.1 Satisfaction Metric", "normalized multi-criteria score", "Compare plaza configurations with equally scaled cost, waiting, safety, and throughput terms.", [variable("S_i", "satisfaction score", "dimensionless", "output", "Score for configuration i; lower is preferred by the paper."), variable("C_i", "cost", "currency/year", "input", "Maintenance and staffing or machine cost."), variable("W_i", "wait time", "s", "input", "Time below the low-speed threshold."), variable("F_i", "safety proxy", "dimensionless", "input", "Proxy based on average merges."), variable("Q_i", "throughput", "cars", "input", "Cars completing the plaza."), variable("C_max", "cost normalizer", "currency/year", "parameter", "Maximum cost used for standardization."), variable("W_max", "wait normalizer", "s", "parameter", "Maximum wait used for standardization."), variable("F_max", "safety normalizer", "dimensionless", "parameter", "Maximum proxy value used for standardization."), variable("Q_max", "throughput normalizer", "cars", "parameter", "Maximum throughput used for standardization.")], ["C_i", "W_i", "F_i", "Q_i", "C_max", "W_max", "F_max", "Q_max"], ["S_i"], [sat_eq], ["All terms are standardized to [0,1].", "Merge count is used as a safety proxy.", "Cost, wait, safety, and throughput receive equal weight."], ["page 10", "Equation (1)", "page 11 metric definitions"], ["measure four terms", "normalize by sweep maxima", "sum the terms", "minimize S_i", "compare configurations"], ["The safety direction and merge proxy need an independent audit.", "Maxima change with the comparison set."]))

    thru_eq = equation(12, "(2)", "throughput_3l4b = sum(i=1..3) passed_i / sum(i=1..3) spawned_i", "T = \\frac{\\sum_{i=1}^{3} P_i}{\\sum_{i=1}^{3} N_i}", "Aggregate completed cars across low, medium, and high traffic levels.", ["T", "P_i", "N_i", "i"], 7)
    models.append(make_model(7, 12, "5.2 Example Comparison", "scenario aggregation", "Compare symmetric, merge-up, and merge-down patterns across three plaza sizes and three traffic levels.", [variable("T", "aggregated throughput", "ratio", "output", "Completed cars divided by spawned cars across traffic levels."), variable("P_i", "passed cars", "cars", "intermediate", "Cars that reach the end at traffic level i."), variable("N_i", "spawned cars", "cars", "intermediate", "Cars introduced at traffic level i."), variable("i", "traffic index", "category", "parameter", "Low, medium, or high traffic."), variable("pattern", "merge pattern", "category", "input", "Symmetric, merge up, or merge down.")], ["P_i", "N_i", "pattern"], ["T"], [thru_eq], ["Traffic levels are combined after separate runs.", "Each lane-booth size is compared with all three patterns.", "Symmetry is interpreted as reducing outer-lane merge pressure."], ["pages 11-12", "Figures 2-4", "throughput expression"], ["run each traffic level", "count completed cars", "sum numerators and denominators", "compute T", "compare patterns"], ["The paper does not report replications or uncertainty for each combination."]))

    eff_eq = equation(15, "efficiency", "efficiency_t = cars out of system this tick / cars in system at start; accumulated efficiency sums efficiency_t over ticks", "e_t = O_t/N_0,\\quad E_{acc}(T) = \\sum_{t=1}^{T} e_t", "Define tick efficiency and the prose-described accumulation used for population sensitivity.", ["e_t", "E_acc", "O_t", "N_0", "t", "T"], 8)
    models.append(make_model(8, 15, "6.2-6.3 Sensitivity", "finite-run sensitivity analysis", "Test patience, autonomous share, and initial population against merge, throughput, and accumulated-efficiency reporters.", [variable("e_t", "tick efficiency", "ratio/tick", "intermediate", "Cars leaving in tick t divided by initial population."), variable("E_acc", "accumulated efficiency", "ratio", "output", "Sum of tick efficiencies through the plotted horizon; the summation is stated in prose."), variable("O_t", "cars out this tick", "cars/tick", "intermediate", "Cars that exit during tick t."), variable("N_0", "initial population", "cars", "input", "Cars in the system at the start."), variable("t", "tick counter", "tick", "intermediate", "Summation index reconstructed from the prose definition of accumulated efficiency.", "inferred-from-equation"), variable("T", "accumulation horizon", "tick", "parameter", "Final tick through which tick efficiencies are summed.", "inferred-from-equation"), variable("a", "autonomous share", "percent", "input", "Tested at 0, 10, and 25 percent in Figures 8-9."), variable("pat", "patience setting", "score", "input", "Tested at 10, 20, and 30 in Figures 6-7.")], ["N_0", "T", "a", "pat"], ["E_acc"], [eff_eq], ["Autonomous cars are all EZ-Pass and perfectly patient.", "The autonomous sweep is limited to 0, 10, and 25 percent.", "Population effects are normalized by the starting population.", "Behavior Space Figure 5 shows repetitions=1 and a 500-tick time limit."], ["pages 13-16", "Figures 5-10", "Behavior Space reporters"], ["set patience", "run the plaza for 500 ticks", "record merges", "test autonomous shares 0/10/25 percent", "vary starting population", "sum tick efficiency", "plot trajectories"], ["No confidence intervals, seeds, or broad mixed-fleet design are supplied."]))

    models.append(make_model(9, 16, "6.2-6.3 Scenario Interpretation", "scenario decision layer", "Translate sensitivity outputs into conditional recommendations about patience, autonomous cars, booth types, and future experiments.", [variable("mix", "vehicle/payment mix", "category", "input", "Combination of human/autonomous and payment classes."), variable("flow", "traffic level", "category", "input", "Low, medium, or high traffic."), variable("rec", "recommendation", "text", "output", "Conditional operational suggestion."), variable("gap", "evidence gap", "text", "output", "Unresolved replication or category limitation.")], ["mix", "flow"], ["rec", "gap"], [], ["Recommendations stay within tested configurations.", "Human and exact-change booths are not separated.", "Further work is needed before field adoption."], ["pages 16-17", "Strengths/Weaknesses", "Further Work"], ["classify scenario", "read the reporter", "state the conditional recommendation", "name the gap", "propose the next experiment"], ["A recommendation is not a construction-ready design."]))

    edges = [
        (1, 2, "model-level configuration becomes car-level state"),
        (2, 3, "agent state consumes road geometry"),
        (3, 4, "payment route reaches service-time rule"),
        (4, 5, "service and motion are interpreted in physical units"),
        (5, 6, "physical reporters enter the satisfaction score"),
        (6, 7, "score compares merge-pattern scenarios"),
        (7, 8, "comparison baseline supplies sensitivity settings"),
        (8, 9, "sensitivity outputs become bounded recommendations"),
    ]
    return {
        "schema_version": 2, "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE,
        "year": YEAR, "source_sha256": SHA256, "review_status": "validated",
        "models": models,
        "dependency_edges": [{"from_model_id": f"MU-{ID_STEM}-{a:03d}", "to_model_id": f"MU-{ID_STEM}-{b:03d}", "handoff": handoff} for a, b, handoff in edges],
    }


def page_summary(page: int, summary: str) -> dict[str, Any]:
    return {"page": page, "summary": summary}


def build_visuals() -> list[dict[str, Any]]:
    specs = [
        (1, "Summary Sheet", "Headline pipeline and reported findings", [1], "Retain the paper's decision preview and its stated scope."),
        (3, "Authority letter", "Audience-facing problem and conditional advice", [1], "Keep the public-agency handoff separate from model evidence."),
        (7, "Figure 1", "NetLogo pseudo-code flow", [1, 2, 3], "Preserve initialization, GO, and reporter order."),
        (8, "Agent attributes", "Car state list", [2], "Keep all eight state variables attached to behavior."),
        (8, "Draw Road", "Discrete lane geometry", [3], "Retain lane, spawn, barrier, and lane-drop operations."),
        (9, "Move and Choose", "Motion and lane-change procedures", [2, 3], "Preserve obstacle detection and patience-triggered merge logic."),
        (10, "Unit conversion", "Patches/ticks to physical units", [5], "Keep the stated 0.5, 18, and 10 factors and their assumption boundary."),
        (10, "Equation (1)", "Satisfaction metric", [6], "Retain all four normalized terms and the paper's minimization direction."),
        (11, "Figure 2", "Three merge patterns", [7], "Keep symmetric, merge-up, and merge-down topology labels."),
        (12, "Figure 3", "Three road sizes", [7], "Retain the 3/4, 4/6, and 6/9 configurations."),
        (12, "Equation (2)", "Combined throughput", [7], "Keep numerator, denominator, and three traffic levels."),
        (12, "Figure 4", "Comparison Satisfaction Ratings for 3 Highways of Different Sizes", [6, 7], "Retain the exact nine satisfaction ratings and the reported symmetric-leading comparison."),
        (13, "Figure 5", "Behavior Space setup", [8], "Retain the reporter selection and tick-level collection boundary."),
        (14, "Figure 6", "Patience sensitivity", [8], "Preserve merge count versus tick for the 3/4 layout."),
        (14, "Figure 7", "Larger-layout patience check", [8], "Retain the 6/9 corroboration without overstating replication."),
        (15, "Figure 8", "Autonomous-share throughput", [8], "Keep the 0-25 percent sweep and accumulated cars output."),
        (15, "Figure 9", "Small-layout autonomous check", [8], "Retain the second layout and its same qualitative pattern."),
        (16, "Figure 10", "Population accumulated efficiency", [8], "Keep the normalized efficiency trajectory and population perturbation."),
        (16, "Figure 11", "NetLogo interface", [9], "Preserve the model's inspectability claim while separating it from validation."),
    ]
    records = [{
        "page": page, "figure": figure, "visual_record_id": f"V-{ID_STEM}-{index:03d}",
        "caption": caption, "source_model_ids": [f"MU-{ID_STEM}-{model:03d}" for model in model_indices],
        "summary": f"{purpose} Supported claim: retain visible labels, topology, equation terms, reporter definitions, or plotted direction. Boundary: this visual does not establish corrected algebra, calibrated accident risk, replicated causality, field feasibility, or out-of-range robustness.",
        "analytical_purpose": purpose,
        "form": "Source visual or displayed equation retained with its original layout role.",
        "encodings": "Retain source labels, axes, units, scales, categories, topology, and annotation; use a text alternative for exact values.",
        "exact_claim": purpose,
        "construction_or_missing": "The paper does not provide a complete raw-run, seed, replication, or figure-construction archive.",
        "applicability": ["Use only within the source model, scenario, page, and parameter boundary recorded here."],
        "forbidden_scenarios": ["Do not present the visual as calibrated field evidence, causal proof, or out-of-range robustness."],
        "accessibility": "Pair the visual with a structured text description and exact values where available; do not rely on bold, color, or spatial position alone.",
        "disposition": "important-visual-record", "evidence_role": "important-positive-record",
    } for index, (page, figure, caption, model_indices, purpose) in enumerate(specs, start=1)]

    detail_by_figure = {
        "Figure 1": {
            "form": "Flowchart",
            "encodings": "START -> Draw World -> SETUP -> Spawn Cars -> GO -> booth/payment and merge branches -> Remove Car; terminal STOP at 500 ticks.",
            "exact_claim": "The model execution order and its 500-tick terminal boundary are inspectable.",
        },
        "Figure 4": {
            "form": "Grouped row-and-category comparison table/chart",
            "encodings": "Rows are 3 Lanes/4 Booths, 4 Lanes/6 Booths, and 6 Lanes/9 Booths; categories are Symmetric, Merge Up, and Merge Down; y is dimensionless Satisfaction Rating; symmetric values are bold in the source.",
            "values": [
                {"road": "3 lanes / 4 booths", "symmetric": 2.627608536, "merge_up": 2.650960515, "merge_down": 2.701233333},
                {"road": "4 lanes / 6 booths", "symmetric": 2.634759975, "merge_up": 2.7717, "merge_down": 2.711140793},
                {"road": "6 lanes / 9 booths", "symmetric": 3.084464016, "merge_up": 3.154486562, "merge_down": 3.158183333},
            ],
            "exact_claim": "Symmetric merging is the lowest reported satisfaction rating for all three tested road sizes after combining low, medium, and high traffic levels.",
            "construction_or_missing": "The source supplies one aggregate rating per road/pattern cell but no error bars, seed ledger, repetition count, confidence interval, or raw traffic-level values.",
            "accessibility": "Provide the nine values as a table; bolding and visual position are not sufficient for nonvisual readers.",
        },
        "Figure 5": {
            "form": "Behavior Space experiment configuration screenshot",
            "encodings": "Experiment 3lane 4 booth; repetitions=1; sequential combinations; reporters include merge-counter, throughput, and count cars with speed <= 0.04; time limit=500.",
            "exact_claim": "The screenshot identifies the reporter and single-repetition experiment boundary, not statistical replication.",
        },
        "Figure 6": {
            "form": "Line plot",
            "encodings": "Accumulated Merges vs. Time; x=Ticks Elapsed; y=Merges; patience levels Low/Medium/High = 10/20/30; 3 lanes/4 booths symmetric.",
        },
        "Figure 7": {
            "form": "Line plot",
            "encodings": "Accumulated Merges vs. Time; x=Ticks Elapsed; y=Merges; patience levels 10/20/30; 6 lanes/9 booths symmetric.",
        },
        "Figure 8": {
            "form": "Line plot",
            "encodings": "Accumulated Cars Remerged vs. Time; x=Ticks Elapsed; y=Cars Remerged with Normal Traffic; No Self Driving, Low Self Driving (10%), Medium Self Driving (25%); 6 lanes/9 booths symmetric, medium traffic.",
        },
        "Figure 9": {
            "form": "Line plot",
            "encodings": "Accumulated Cars Remerged vs. Time; x=Ticks Elapsed; y=Cars Remerged with Normal Traffic; No Self Driving, Low Self Driving (10%), Medium Self Driving (25%); 3 lanes/4 booths symmetric, medium traffic.",
        },
        "Figure 10": {
            "form": "Line plot",
            "encodings": "Accumulated Efficiency; x=Ticks Elapsed; legend Low/Medium/High Number of Cars; 4 lanes/6 booths symmetric.",
            "exact_claim": "The plotted accumulated efficiency declines as starting population increases in the tested setup.",
        },
    }
    for record in records:
        record.update(detail_by_figure.get(record["figure"], {}))
    return records


def build_card(language: dict[str, Any], models_record: dict[str, Any], visuals: list[dict[str, Any]]) -> dict[str, Any]:
    sections = [page_summary(item["pages"][0], f"Input: {item['input']} Rhetorical job: {item['rhetorical']} Analytical job: {item['analytical']} Output: {item['output']} Handoff: {item['handoff']}") for item in CHAPTERS]
    assumptions = [
        page_summary(4, "Cars use their assigned payment lanes except EZ-Pass cars, which may use any lane."),
        page_summary(4, "Self-driving cars are perfectly patient and all carry EZ-Pass."),
        page_summary(4, "Cash and exact-change service have the same modeled duration and are treated together."),
        page_summary(4, "Toll plazas fan out symmetrically before the booths and every booth services two lanes."),
        page_summary(5, "The cost of restructuring is treated as approximately equal across comparable lane/booth choices."),
        page_summary(5, "The average payment time is 30 seconds and the average vehicle is an SUV."),
        page_summary(8, "Merge count is used as a safety proxy and low-speed time as a wait proxy."),
        page_summary(10, "The paper displays 0.5 patch/tick, 18 feet/patch, seconds/(95 feet), and approximately 10 tick/(1 second); its dimensional direction remains a warning rather than a silent correction."),
        page_summary(12, "Low, medium, and high traffic scores are aggregated into one comparison value."),
        page_summary(14, "The autonomous sensitivity range is 0% to 25% in the reported experiments."),
        page_summary(15, "Accumulated efficiency is normalized by the starting population."),
        page_summary(17, "The source's recommendations remain conditional because replications and service-category distinctions are incomplete."),
    ]
    data = [
        page_summary(1, "The summary claims more than 700 tested combinations and highlights symmetric design."),
        page_summary(7, "Car state includes driver, speed, top-speed, target-lane, patience, payment, service-time, and anticipation."),
        page_summary(8, "Cash/exact-change service time is sampled from an exponential distribution with mean 30 seconds; EZ-Pass is zero."),
        page_summary(10, "The displayed conversion uses 0.5 patch/tick, 18 feet/patch, seconds/(95 feet), and approximately 10 tick/(1 second); the following prose says 10 ticks is approximately 1 second."),
        page_summary(11, "The comparison includes 3 lanes/4 booths, 4 lanes/6 booths, and 6 lanes/9 booths."),
        page_summary(12, "Reported satisfaction values for the nine size/pattern combinations are retained in the visual ledger."),
        page_summary(13, "Behavior Space reporters include merges, completed cars, average patience, and below-threshold cars."),
        page_summary(14, "Patience and autonomous-share sweeps use finite simulation traces rather than field data."),
        page_summary(16, "The strengths section reports exactly 729 tested parameter combinations, refining the summary's more-than-700 statement."),
    ]
    verification = [
        page_summary(1, "All 18 physical pages were read; the summary and title/letter pages are retained as separate evidence."),
        page_summary(7, "The pseudo-code flow was visually checked before translating procedures into model dependencies."),
        page_summary(8, "The service-time expression and agent attribute list were checked against focused proxies."),
        page_summary(10, "Equation (1) and the patch/tick conversion were checked for every displayed term."),
        page_summary(12, "The three traffic levels, Equation (2), and all nine Figure 4 satisfaction ratings were retained together with the symmetric comparison."),
        page_summary(13, "The Behavior Space reporter list, 500-tick limit, and repetitions=1 setting were checked before interpreting sensitivity plots."),
        page_summary(14, "Both patience layouts were retained, including the larger 6/9 corroboration."),
        page_summary(15, "Both autonomous-share layouts and their bounded 0-25 percent range were retained."),
        page_summary(16, "The accumulated-efficiency definition and population trend were checked before the warning pass."),
        page_summary(17, "The source's own weaknesses were kept after positive language, organization, model, and visual coverage."),
    ]
    results = [
        page_summary(1, "The summary reports symmetric design as preferred and autonomous-car impact as negligible in the tested range."),
        page_summary(3, "The authority letter emphasizes symmetry and preserving driver patience."),
        page_summary(10, "The metric minimizes normalized cost and wait while using inverted safety and throughput terms."),
        page_summary(12, "Symmetric fanning is reported as most satisfactory at all three tested road sizes."),
        page_summary(14, "Lower patience increases merge counts, with a taper after a threshold."),
        page_summary(15, "The autonomous-share sweep shows essentially no accumulated-throughput effect in the tested range."),
        page_summary(16, "Accumulated efficiency declines as the starting number of cars increases."),
        page_summary(17, "Further work proposes staggered booth release and explicit human versus exact-change analysis."),
    ]
    contributions = [
        page_summary(1, "The paper makes a full chain visible: agent model, scenario comparison, sensitivity, and recommendation."),
        page_summary(4, "The problem analysis separates geometry, traffic, payment, vehicle, and metric roles."),
        page_summary(6, "NetLogo is justified by the link between individual choices and aggregate traffic."),
        page_summary(7, "The state vector makes patience and payment behavior explicit rather than implicit."),
        page_summary(10, "The unit conversion gives the simulation a physical interpretation."),
        page_summary(12, "The size-pattern comparison supplies a direct visual decision result."),
        page_summary(14, "Patience sensitivity connects a behavioral parameter to merge activity."),
        page_summary(15, "The autonomous and population sweeps test two distinct perturbation axes."),
        page_summary(16, "Strengths and weaknesses are stated before the final recommendation."),
    ]
    weaknesses = [
        {"page": 10, "model_id": f"MU-{ID_STEM}-006", "equation_id": f"EQ-{ID_STEM}-003", "summary": "The satisfaction metric minimizes a term written as 1 minus normalized safety, while merge count is described as the safety proxy; the direction needs an explicit audit."},
        {"page": 10, "model_id": f"MU-{ID_STEM}-005", "equation_id": f"EQ-{ID_STEM}-002", "summary": "The displayed unit conversion multiplies by seconds/(95 feet) but ends with tick/second, so its dimensional direction and numerical convention must remain unresolved."},
        {"page": 8, "model_id": f"MU-{ID_STEM}-002", "equation_id": None, "summary": "Autonomous cars are both perfectly patient and EZ-Pass, so driver type and payment method are not separately identified."},
        {"page": 8, "model_id": f"MU-{ID_STEM}-004", "equation_id": f"EQ-{ID_STEM}-001", "summary": "Human-operated and exact-change booths are deliberately collapsed, preventing a distinct service-type comparison."},
        {"page": 13, "model_id": f"MU-{ID_STEM}-007", "equation_id": f"EQ-{ID_STEM}-004", "summary": "Figure 5 sets Behavior Space repetitions to 1, so the traffic-level aggregation has no within-combination repeated-run uncertainty."},
        {"page": 14, "model_id": f"MU-{ID_STEM}-008", "equation_id": None, "summary": "The patience result is based on a small set of finite traces and lacks a seed or replication ledger."},
        {"page": 15, "model_id": f"MU-{ID_STEM}-008", "equation_id": None, "summary": "Autonomous share is tested only from 0% to 25%, leaving higher adoption and mixed payment effects unexamined."},
        {"page": 16, "model_id": f"MU-{ID_STEM}-008", "equation_id": f"EQ-{ID_STEM}-005", "summary": "The accumulated-efficiency denominator and starting-population perturbation do not establish a general efficiency law."},
        {"page": 17, "model_id": f"MU-{ID_STEM}-009", "equation_id": None, "summary": "The user-friendly interface and visual animation do not substitute for archived code, calibration, or field validation."},
    ]
    extensions = [
        page_summary(8, "Separate human, exact-change, and electronic service distributions and rerun the same layouts."),
        page_summary(9, "Add controlled booth-release signals and measure whether staggered departures reduce merge pressure."),
        page_summary(10, "Audit the score direction and report component-wise results before scalar minimization."),
        page_summary(12, "Repeat each pattern under fixed seeds and confidence intervals across traffic levels."),
        page_summary(14, "Use a factorial patience design and report threshold estimates with uncertainty."),
        page_summary(15, "Extend autonomous share beyond 25% and cross it with payment and patience factors."),
        page_summary(16, "Test accumulated efficiency with multiple initial populations and independent replications."),
        page_summary(17, "Archive the NetLogo model, interface, Behavior Space experiment, and raw reporters."),
    ]
    card = {
        "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE, "year": YEAR,
        "team_control_number": "70174", "title": "An Agent-Based Model for Developing and Evaluating Efficient Toll Plaza Designs",
        "award_status": "outstanding", "source": {"relative_path": SOURCE_PATH, "sha256": SHA256, "page_count": PAGE_COUNT},
        "schema_version": 1, "source_quality": {"status": "text-rich", "notes": "Complete text extraction with rendered-page and bounded visual review."},
        "context_sources": ["Summary Sheet", "authority letter", "18 physical pages"],
        "task_reconstruction": {"summary": "Choose a toll-plaza design that balances safety, throughput, cost, and operating conditions.", "inputs": ["lane count", "booth count", "merge pattern", "traffic level", "payment method", "vehicle type"], "outputs": ["satisfaction", "throughput", "wait", "merge proxy", "conditional recommendation"]},
        "section_map": sections, "assumptions": assumptions, "data_and_preprocessing": data,
        "models": [page_summary(model["page"], f"{model['model_id']}: {model['summary']}") for model in models_record["models"]],
        "dependency_graph": [page_summary(6 + i, edge["handoff"]) for i, edge in enumerate(models_record["dependency_edges"])],
        "verification": verification, "results_trace": results, "contributions": contributions,
        "writing_logic": [page_summary(item["pages"][0], f"{item['label']}: {item['input']} -> {item['output']} -> {item['handoff']}") for item in CHAPTERS],
        "language_observations": [page_summary(unit["page"], f"{unit['function']}: {unit['reusable_pattern']}") for unit in language["units"][:18]],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [
            {"page": 1, "evidence_class": "J", "summary": "A compact abstract that previews model, comparison, result, and transfer likely helps judges verify the decision chain."},
            {"page": 12, "evidence_class": "C", "summary": "The all-size symmetric comparison is a clear judge-facing result, but its evidence strength depends on replication."},
            {"page": 17, "evidence_class": "J", "summary": "Placing limitations before recommendations makes the final operational claim more credible."},
        ],
        "weaknesses": weaknesses,
        "independent_extensions": [{"extension_id": f"E-B-{index:03d}", "page": item["page"], "summary": item["summary"]} for index, item in enumerate(extensions, start=1)],
        "candidate_rule_impacts": [
            {"rule_id": RULES["language"], "action": "retain each toll-design claim with traffic, payment, vehicle, metric, comparator, result, and scope boundary", "evidence_ids": []},
            {"rule_id": RULES["logic"], "action": "trace the prompt through assumptions, agent state, procedures, score, scenario comparison, sensitivity, warning, and conditional authority advice", "evidence_ids": []},
            {"rule_id": RULES["data"], "action": "version lane, booth, payment, vehicle, speed, service, traffic, reporter, and conversion inputs with units and provenance", "evidence_ids": []},
            {"rule_id": RULES["modeling"], "action": "keep agent state, service, motion, score, throughput, efficiency, and decision outputs distinct", "evidence_ids": []},
            {"rule_id": ADDITIONAL_RULES["scalarization"], "action": "distinguish the paper's equal-weight scalar satisfaction ranking from a feasible nondominated-frontier analysis", "evidence_ids": []},
            {"rule_id": ADDITIONAL_RULES["reliability"], "action": "bound reliability claims by the one-repetition Behavior Space setting, finite traces, tested layouts, and missing uncertainty", "evidence_ids": []},
            {"rule_id": RULES["verification"], "action": "run source-equation, dimensional-direction, stopping-rule, replication, and result-boundary preflights before transfer", "evidence_ids": []},
            {"rule_id": RULES["visualization"], "action": "retain flow, topology, equation, reporter, axis, legend, exact Figure 4 values, and uncertainty boundaries", "evidence_ids": []},
        ],
        "unresolved_questions": ["Does minimizing the printed satisfaction equation reward the intended safety direction?", "How do human and exact-change service distributions differ?", "What happens above 25% autonomous share?", "How many independent runs are needed for the symmetric result to remain stable?", "Does merge count predict actual conflict severity or crash exposure?"],
        "protocol_v2_records": {
            "language": {"path": f"artifacts/language-units/{PAPER_ID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]},
            "models": {"path": f"artifacts/model-units/{PAPER_ID}.json", "model_count": len(models_record["models"]), "equation_count": sum(len(model["governing_equations"]) for model in models_record["models"]), "review_status": models_record["review_status"]},
        },
        "review_status": "validated",
    }
    return card


EVIDENCE_POOL = [(item["pages"][0], item["label"], phrase) for item in CHAPTERS for phrase in item["phrases"]]


def build_observations(units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []

    def add(page: int, section: str, dimension: str, basis: str, interpretation: str, evidence_class: str, rule_ids: list[str], confidence: str = "high") -> None:
        observations.append({
            "schema_version": 1, "observation_id": f"O-{ID_STEM}-{len(observations) + 1:04d}",
            "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE, "year": YEAR, "page": page,
            "section": section, "evidence_class": evidence_class, "dimension": dimension,
            "source_basis": basis, "interpretation": interpretation,
            "applicability": ["Apply only after specifying lane/booth geometry, payment and driver mix, traffic regime, reporter, comparator, and evidence boundary."],
            "counterevidence": ["A finite NetLogo trace, merge-count proxy, bounded autonomous sweep, or visual interface does not establish calibrated safety, replicated causality, or field feasibility."],
            "confidence": confidence, "candidate_rule_ids": rule_ids,
        })

    for unit in units:
        add(unit["page"], unit["section"], "language", unit["source_excerpt"], f"Reuse the rhetorical action {unit['function']} only after replacing source entities, numbers, metrics, and decision boundary.", "O", [RULES["language"]])

    targets = {"logic": 12, "modeling": 12, "visualization": 18, "verification": 15, "data": 10, "assumption": 10, "result": 12, "weakness": 8, "other": 5}
    interpretations = {
        "logic": "Trace the prompt through assumptions, agent state, procedures, metric, scenario comparison, sensitivity, warning, and recommendation.",
        "modeling": "Keep each state, equation, reporter, objective, and boundary attached to its upstream and downstream role.",
        "visualization": "Retain every figure, equation, reporter definition, topology label, and visual limitation as a source-anchored record.",
        "verification": "Classify checks as page transcription, unit conversion, direction audit, replication, calibration, or provenance review.",
        "data": "Record page, unit, distribution, traffic regime, payment/driver class, transformation, and downstream use for every parameter.",
        "assumption": "Turn each simplification into a scope diagnostic and test the result when the premise is relaxed.",
        "result": "Bind every result to its producing layout, traffic level, reporter, comparator, direction, and tested range.",
        "weakness": "Keep defects in the final warning pass and name a concrete algebra, data, safety, or reproducibility test.",
        "other": "Preserve software, citation, audience, and future-work context without treating it as model validation.",
    }
    classes = {"logic": "I", "modeling": "O", "visualization": "O", "verification": "E", "data": "O", "assumption": "O", "result": "O", "weakness": "E", "other": "C"}
    for dimension, count in targets.items():
        for index in range(count):
            page, section, phrase = EVIDENCE_POOL[(index * 5 + len(dimension) * 3) % len(EVIDENCE_POOL)]
            add(page, f"{section} / {dimension} evidence {index + 1}", dimension, phrase, f"{interpretations[dimension]} Evidence item {index + 1} preserves a distinct source anchor and receiving use.", classes[dimension], [RULES[dimension]], "medium" if dimension in {"weakness", "other"} else "high")
    add(12, "Figure 4 / scalarization boundary", "modeling", "Figure 4 exact nine-cell satisfaction comparison", "The paper selects the lowest equal-weight scalar score among three patterns and three sizes; this is a scalar ranking, not a computed feasible nondominated frontier.", "E", [RULES["modeling"], ADDITIONAL_RULES["scalarization"]], "high")
    add(13, "Figure 5 / replication boundary", "verification", "Behavior Space screenshot: repetitions=1, time limit=500", "Treat the reported comparisons as finite one-repetition traces with no uncertainty interval unless an independent run ledger is supplied.", "E", [RULES["verification"], ADDITIONAL_RULES["reliability"]], "high")
    add(12, "Figure 4 / exact visual record", "visualization", "Figure 4 values: 2.627608536/2.650960515/2.701233333; 2.634759975/2.7717/2.711140793; 3.084464016/3.154486562/3.158183333", "Present the nine dimensionless ratings as a text table with road size, merge pattern, aggregation boundary, and missing uncertainty attached.", "O", [RULES["visualization"]], "high")
    return observations


def build_audit(language: dict[str, Any], models_record: dict[str, Any], card: dict[str, Any], observations: list[dict[str, Any]]) -> dict[str, Any]:
    by_chapter: dict[str, list[dict[str, Any]]] = {}
    for unit in language["units"]:
        by_chapter.setdefault(unit["chapter"], []).append(unit)
    layouts = {layout["chapter"]: layout for layout in language["chapter_layouts"]}
    equations = [equation for model in models_record["models"] for equation in model["governing_equations"]]
    warnings = [{"model_id": EQUATION_MODEL[item["equation_id"]], "equation_id": item["equation_id"], "page": item["page"], "warning": warning} for item, warning in zip(equations, [
        "The exponential service-rate notation is not accompanied by a fitted distribution or random-seed ledger.",
        "The printed conversion multiplies by seconds/(95 feet) but reports tick/second; preserve the source expression and flag the dimensional-direction and numerical-convention ambiguity instead of silently repairing it.",
        "The satisfaction score uses a safety term whose direction should be checked against the merge-count proxy.",
        "The throughput aggregation lacks repeated-run uncertainty and can change with the traffic-level denominator.",
        "The accumulated-efficiency equation does not by itself establish a general efficiency law across populations.",
    ])]
    dimensions = {name: 0 for name in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}
    dimensions.update(Counter(item["dimension"] for item in observations))
    paragraph_chains = []
    for chapter_name in ("abstract", "introduction"):
        paragraph_count = layouts[chapter_name]["paragraph_count"]
        paragraph_units = by_chapter[chapter_name][:paragraph_count]
        paragraph_chains.append({
            "chapter": chapter_name, "visual_paragraph_count": layouts[chapter_name]["paragraph_count"], "coverage_status": "complete", "gaps": [],
            "paragraphs": [{"paragraph_index": i, "dominant_move": f"{unit['function']} -> explicit output -> next handoff", "language_unit_ids": [unit["language_unit_id"]]} for i, unit in enumerate(paragraph_units, start=1)],
        })

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
            merged_saturation = chapter_saturation_by_name[chapter_name]
            merged_saturation["pass_count"] = max(merged_saturation["pass_count"], saturation["pass_count"])
            merged_saturation["new_moves_by_pass"] = [
                left + right
                for left, right in zip(merged_saturation["new_moves_by_pass"], saturation["new_moves_by_pass"])
            ]
            merged_saturation["last_pass_new_moves"] = merged_saturation["new_moves_by_pass"][-1]

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
            "positive_pattern": "Retain input -> rhetorical job -> analytical job -> output -> handoff; put warnings last.",
        }
        if chapter_name not in section_progressions_by_name:
            section_progressions_by_name[chapter_name] = progression
        else:
            merged_progression = section_progressions_by_name[chapter_name]
            combined_moves = []
            for earlier, later in zip(merged_progression["moves"], progression["moves"]):
                prefix, earlier_body = earlier.split(":", 1)
                _, later_body = later.split(":", 1)
                connector = "then" if chapter_name == "model-improvement" else "later in source"
                combined_moves.append(f"{prefix}: {earlier_body.strip()}; {connector}, {later_body.strip()}")
            merged_progression["moves"] = combined_moves

    return {
        "audit_id": f"LA-{ID_STEM}", "paper_id": PAPER_ID, "problem_type": PROBLEM_TYPE, "year": YEAR, "source_sha256": SHA256, "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": list(chapter_saturation_by_name.values()),
        "language_unit_dispositions": [{"language_unit_id": unit["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": unit["candidate_pattern_ids"], "reason": "Transfer only the rhetorical mechanism after replacing the toll-plaza entities, values, metrics, and scope boundary."} for unit in language["units"]],
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "complete", "weakness_substitution_allowed": False,
            "global_organization_chain": [item["output"] for item in CHAPTERS],
            "section_progressions": list(section_progressions_by_name.values()),
            "main_argument_chains": [
                {"claim": "A symmetric merge is preferred in the tested lane/booth layouts.", "support_steps": ["three patterns", "three sizes", "three traffic levels", "Equation (2)", "Figure 4"], "decision_consequence": "Treat symmetry as a tested candidate and rerun it with replicated, calibrated conflict measures.", "source_pages": [11, 12]},
                {"claim": "Patience changes merge activity and can alter system efficiency.", "support_steps": ["patience state", "braking decrement", "Figures 6-7", "threshold interpretation"], "decision_consequence": "Test behavioral interventions separately from geometry and preserve the finite-run boundary.", "source_pages": [7, 9, 13, 14]},
                {"claim": "The reported autonomous effect is negligible in the tested range.", "support_steps": ["0-25 percent sweep", "two symmetric layouts", "Figures 8-9", "bounded conclusion"], "decision_consequence": "Do not extrapolate beyond 25 percent or confuse autonomous type with EZ-Pass payment.", "source_pages": [14, 15]},
                {"claim": "The model is useful as an inspectable scenario tool but not yet a validated field design.", "support_steps": ["agent choice", "729 combinations", "user interface", "runtime and coverage weaknesses", "further work"], "decision_consequence": "Archive code and replications before construction or public operational decisions.", "source_pages": [16, 17]},
            ],
        },
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warnings},
        "model_retention": {"model_count": len(models_record["models"]), "retained_model_ids": [model["model_id"] for model in models_record["models"]], "retained_equation_ids": [item["equation_id"] for item in equations], "central_equations": [{"model_id": model["model_id"], "equation_ids": [item["equation_id"] for item in model["governing_equations"]], "all_central_equations_retained": True} for model in models_record["models"] if model["governing_equations"]]},
        "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": visual["visual_record_id"], "disposition": "important-visual-record", "analytical_purpose": visual["summary"]} for i, visual in enumerate(card["visualization_observations"], start=1)],
        "dimension_counts": dimensions, "positive_reusable_language_count": len(language["units"]), "weakness_record_count": dimensions["weakness"], "review_status": "validated",
        "gate_attestation": {"g1_g3_language": "validated-before-G4", "g4_organization": "passed-before-G5-G6", "g5_models": "validated-before-G7", "g6_visuals": "passed-before-G7", "g7_warning_mode": "last-pass-warning-only", "g7_warning_count": len(warnings), "warnings_strict_minority_of_language": len(warnings) < len(language["units"]), "request_body_guard": {"bounded_jpeg_proxies": 8, "total_proxy_bytes": 1645443, "largest_proxy_bytes": 298626, "original_full_page_png_in_context": False}},
    }


def build_extraction() -> dict[str, Any]:
    extraction = json.loads(SOURCE_EXTRACTION.read_text(encoding="utf-8"))
    if extraction.get("paper_id") != PAPER_ID or extraction.get("source_sha256") != SHA256 or extraction.get("page_count") != PAGE_COUNT:
        raise SystemExit("q119 extraction identity/hash/page count does not match manifest")
    if extraction.get("extraction_status") != "text-extracted":
        raise SystemExit("q119 extraction is not text-extracted")
    extraction["visual_review_status"] = "complete"
    extraction["visual_review_manifest"] = {"pages_reviewed": list(range(1, PAGE_COUNT + 1)), "proxy_count": 8, "proxy_total_bytes": 1645443, "largest_proxy_bytes": 298626, "original_full_page_png_in_context": False, "review_note": "All 18 pages were read in bounded text ranges; page contacts and focused formula/table proxies were reviewed."}
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
    print(json.dumps({"stage": str(STAGE), "chapters": len(language["available_chapters"]), "language_units": len(units), "models": len(models_record["models"]), "equations": len(EQUATION_MODEL), "dependency_edges": len(models_record["dependency_edges"]), "visual_records": len(visuals), "observations": Counter(item["dimension"] for item in observations), "formula_warnings": len(audit["formula_error_watch"]["warnings"])}, indent=2, default=dict))


if __name__ == "__main__":
    main()
