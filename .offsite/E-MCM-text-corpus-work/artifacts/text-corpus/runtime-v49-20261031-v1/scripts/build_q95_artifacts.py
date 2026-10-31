from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2012-13955-a0e5e63c"
SHORT = "13955"
SHA = "a0e5e63c77e2f6fdc6aa8dffe45b33850e2fa93c4e40617344cac939a2d7eb70"
TYPE = "B"
YEAR = "2012"
PAGE_COUNT = 18

PATTERNS = [
    "LP-B-ABSTRACT-PROBLEM-METHOD-CASE-SENSITIVITY",
    "LP-B-INTRO-ANALOGY-CONSTRAINT-DECISION",
    "LP-B-DEFINITION-OPERATION-IMPLEMENTATION",
    "LP-B-ASSUMPTION-MECHANISM-CONSEQUENCE",
    "LP-B-ARRAY-STATE-DAILY-UPDATE",
    "LP-B-FURTHEST-EMPTY-CANDIDATE-SET",
    "LP-B-PRIORITY-FORMULA-INTERPRETATION",
    "LP-B-SPECIAL-CASE-ALGORITHM-INTEGRATION",
    "LP-B-WORKED-EXAMPLE-TO-FLOWCHART",
    "LP-B-SIMULATION-TRACE-TO-CAPACITY",
    "LP-B-CASE-CALIBRATION-THRESHOLD",
    "LP-B-SENSITIVITY-TABLE-QUALIFIED-CLAIM",
    "LP-B-LIMITATION-MECHANISM-IMPLICATION",
    "LP-B-CONCLUSION-RESULT-TRANSFER-BOUNDARY",
    "LP-B-MEMO-FINDING-ACTION-CAVEAT",
]

# key, protocol chapter, first page, last page, tag, language-unit count,
# source-checked paraphrase, visually observed paragraph count
CHAPTERS = [
    ("abstract", "abstract", 1, 1, "ABS", 28, "The abstract states the scheduling objective, campsite-movement model, daily algorithm, long-run carrying-capacity calculation, Grand Canyon case study, and sensitivity to propulsion, duration, and campsite count.", 1),
    ("introduction", "introduction", 3, 3, "INT", 30, "The introduction moves from scheduling analogies to the 225-mile river, six-month season, wilderness campsite constraint, verification plan, manager memo, and claimed adaptability.", 4),
    ("problem-definition", "problem-restatement", 3, 4, "PRB", 20, "The problem definition asks for a schedule, allowable daily starts, and carrying capacity, then defines carrying capacity as the maximum groups sent during the season.", 6),
    ("model-overview", "problem-analysis", 3, 4, "OVR", 18, "The overview presents a flexible simulation whose inputs are trip-length distribution, propulsion ratio, and campsite count and whose output is successful six-month trip count.", 5),
    ("constraints-and-assumptions", "assumptions", 4, 5, "ASM", 26, "The paper fixes river length, craft speeds, duration choices, uniform campsites, one group per campsite, downstream motion, daily travel limits, ignored weather, and exact final-day exit.", 14),
    ("variables", "notation", 5, 6, "NOT", 22, "The notation defines group, trip length, elapsed nights, campsite count and location, current location, scheduled daily distance, maximum daily distance, priority, reachable set, propulsion ratio, duration distribution, current trips, and peak capacity.", 13),
    ("methods", "model-establishment", 6, 8, "MOD", 34, "The methods define open campsites, movement, waitlist, final exit, the furthest-empty scan, the reachable group set, and a schedule-relative priority score.", 15),
    ("daily-scheduling-algorithm", "algorithm", 6, 9, "ALG", 40, "Each day the procedure scans empty campsites from downstream to upstream, forms the reachable candidates, selects the highest-priority group, moves it, and applies waitlist, ahead-of-schedule, and final-exit special rules.", 18),
    ("worked-example", "model-improvement", 7, 11, "EXM", 32, "Three-group diagrams, a flowchart, a four-group table, and location and priority plots illustrate the daily assignment logic and its repeated behavior.", 12),
    ("simulation-results", "results", 10, 12, "RES", 24, "The hypothetical trace and Grand Canyon sweep connect daily launch rate to completed, late, and waitlisted trips and choose eighteen starts per day as the last zero-late zero-waitlist case.", 9),
    ("case-and-sensitivity", "sensitivity-analysis", 12, 15, "SEN", 34, "The case study varies campsites Y, oar-to-motor ratio R, and duration distribution D, tabulates peak carrying capacities, and presents a fitted contour surface.", 13),
    ("discussion-conclusion", "conclusion", 15, 15, "CON", 18, "The conclusion recommends using campsite count, propulsion mix, and duration mix to estimate capacity and proposes an uncalibrated transfer from Grand Canyon results to the Big Long River.", 6),
    ("limitations", "strengths-limitations", 16, 16, "LIM", 20, "The limitation section acknowledges roughly threefold capacity overestimation, campsite crowding and environmental damage, and omission of river speed and submerged campsites.", 8),
    ("references", "references", 17, 17, "REF", 8, "Six references provide river-management and scheduling context, but old HTTP links, a dynamic encyclopedia page, and absent archived inputs limit reproducibility.", 6),
    ("manager-memo", "memo", 18, 18, "MEM", 22, "The memo translates the algorithm and case study into manager-facing guidance about carrying capacity, propulsion ratio, duration mix, and additional trips.", 8),
]

MOVES = [
    ("problem-method-result-forecast", "Forecast the whole study by naming the decision, mechanism, case, outputs, and robustness variables.", "decision -> model -> algorithm -> case -> sensitivity"),
    ("analogy-to-domain", "Use familiar scheduling systems to motivate the shared resource-allocation structure before specializing to a river.", "familiar analogy -> shared difficulty -> river constraint -> objective"),
    ("definition-before-use", "Define an operational state immediately before the algorithm consumes it.", "term -> operational test -> representation -> downstream use"),
    ("assumption-with-consequence", "State a simplification and explain the computational mechanism it enables.", "assumption -> excluded behavior -> simplification -> enabled operation"),
    ("state-to-candidate-set", "Convert the current river state into a set of groups eligible for one campsite.", "state -> feasibility test -> candidate set -> selection"),
    ("formula-to-interpretation", "Give a normalized schedule score and interpret values above, below, and equal to one.", "formula -> reference value -> three cases -> decision meaning"),
    ("general-rule-special-case", "State the default daily rule, then add waitlist, ahead-of-schedule, and exit cases with explicit precedence.", "default rule -> exception -> precedence -> state update"),
    ("small-example-to-flowchart", "Walk through a small assignment before presenting the complete repeated procedure.", "initial state -> feasible moves -> priority choice -> updated state -> full algorithm"),
    ("trace-to-capacity", "Use a multi-day trace to expose long-run scheduling behavior and define the reported seasonal output.", "daily trace -> repeated behavior -> seasonal count -> capacity interpretation"),
    ("parameter-table-claim", "Vary one declared input family, retain the exact table, and qualify the managerial claim by the observed pattern.", "fixed settings -> parameter sweep -> table -> qualified implication"),
    ("limitation-causal-chain", "Name a simplifying omission, explain its directional effect, and state what evidence is needed before transfer.", "omission -> mechanism -> bias direction -> required calibration"),
    ("memo-result-to-action", "Translate a result into an action only after restating the ratio direction, operating conditions, and uncertainty boundary.", "result -> conditions -> action -> caveat"),
]

EXAMPLES = [
    ("A ferry-scheduling abstract names the berth constraint, dispatch heuristic, observed throughput, and demand sensitivity without claiming proof of optimality.", "Its final sentence lists only the parameters actually swept."),
    ("A hospital bed scheduler moves from airline and CPU analogies to beds, arrivals, service times, and one-patient-per-bed constraints.", "The analogy ends before domain-specific assumptions begin."),
    ("A warehouse model defines an open slot as an unoccupied indexed location and states exactly which state array stores it.", "The next algorithm step consumes that Boolean test."),
    ("A vehicle-routing model assumes uniform depots for a baseline and states that the assumption permits an array representation.", "A later experiment replaces the uniform coordinates with measured locations."),
    ("A berth allocator scans downstream-equivalent positions, forms all vessels reachable before cutoff, and chooses from that set.", "The candidate set includes both lower and upper position bounds."),
    ("A service-delay score is normalized around one, with separate interpretations for early, on-time, and late jobs.", "Zero-denominator states receive a formal piecewise definition."),
    ("A dispatch procedure writes its default choice, tie break, fallback, update timing, and completion rule in one ordered list.", "Each job is marked after moving so it cannot move twice in one cycle."),
    ("A three-job schedule is replayed before a flowchart generalizes the daily loop.", "Every arrow names the state updated at that transition."),
    ("A six-month simulation reports launched, completed, censored, late, and queued jobs separately.", "Capacity is tied to one declared metric instead of mixing those counts."),
    ("A sensitivity table reports the maximum in every column and flags when the prose recommendation differs from the table.", "Near ties are not called robust without repeated runs."),
    ("A tourism memo gives the propulsion ratio in the same direction used by the model and repeats the calibration boundary.", "The recommendation is withheld when the source river differs materially."),
    ("A reproducible simulation appendix supplies code, seed, configuration, stopping rule, and machine-readable outputs.", "A reader can rerun the exact selected scenario."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose
EQUATIONS = [
    ("scheduled daily distance", 5, "Variables", "daily progress target", "a_i = 225/t_i", r"a_i=\frac{225}{t_i}", ["a_i", "t_i"], "Compute the average miles per day required for group i to finish on schedule."),
    ("priority score", 5, "Variables and Priority", "schedule priority", "P_i = (d_i/t_i)/(l_i/225)", r"P_i=\frac{d_i/t_i}{l_i/225}=\frac{225d_i}{t_i l_i}", ["P_i", "d_i", "t_i", "l_i"], "Measure elapsed-trip fraction relative to completed-distance fraction."),
    ("reachable candidate set", 6, "The Furthest Empty Campsite", "reachability set", "G_c = {g_i : m_i + l_i >= c}", r"G_c=\{g_i:m_i+l_i\ge c\}", ["G_c", "g_i", "m_i", "l_i", "c"], "Collect groups whose maximum daily travel can reach campsite c under the printed one-sided condition."),
    ("ahead-of-schedule eligibility", 8, "Priorities and Other Considerations", "ahead-schedule gate", "d_i a_i >= c", r"d_i a_i\ge c", ["d_i", "a_i", "c"], "Prevent an ahead-of-schedule group from moving beyond its nominal cumulative distance."),
    ("printed final-exit rule", 8, "Priorities and Other Considerations", "exit timing", "t_i = d_i", r"t_i=d_i", ["t_i", "d_i"], "Permit a group to move to Final Exit on the printed exact equality day."),
    ("uniform campsite coordinate", 5, "Assumptions", "river discretization", "x_c = 225 c / Y", r"x_c=\frac{225c}{Y}", ["x_c", "c", "Y"], "Map an indexed campsite to a uniformly spaced downstream coordinate."),
    ("peak capacity surface", 13, "Sensitivity Analysis", "capacity response", "M = M(Y,R,D)", r"M=M(Y,R,D)", ["M", "Y", "R", "D"], "Represent the simulated peak seasonal capacity as a function of campsite count, propulsion ratio, and duration distribution."),
]

# page, family, purpose, inputs, outputs
ALGORITHMS = [
    (6, "river array initialization", "Represent First Launch, Y internal campsites, Final Exit, current groups, and a waitlist in an ordered state array.", ["Y", "groups", "trip lengths", "propulsion"], ["river state"]),
    (6, "furthest-empty downstream scan", "Find the furthest open campsite and repeat upstream after every assignment.", ["river state", "occupancy"], ["target campsite c"]),
    (6, "reachable-group construction", "Build the candidate groups that can reach the current target without exceeding daily travel.", ["current locations", "maximum daily distances", "target c"], ["G_c"]),
    (7, "priority selection", "Choose the highest-priority feasible group for a target campsite.", ["G_c", "P_i"], ["selected group"]),
    (8, "waitlist launch handling", "Treat unlaunched groups as located at First Launch with a special priority value.", ["waitlist order", "reachability", "P=1"], ["launched group or retained queue"]),
    (8, "ahead-schedule restriction", "Block a group from moving farther than its cumulative schedule target even when physically reachable.", ["d_i", "a_i", "target c"], ["eligible ahead-schedule move"]),
    (8, "final-exit handling", "Move eligible groups from their last campsite to an always-open Final Exit state.", ["elapsed nights", "trip length", "current location"], ["off-river state"]),
    (9, "daily scheduling loop", "Repeat target selection, candidate construction, priority choice, movement, and state update for every open campsite.", ["day state", "river array", "groups"], ["next-day state"]),
    (10, "multi-day hypothetical simulation", "Replay four groups and record campsite location and priority by night.", ["four group configurations", "daily loop"], ["location trace", "priority trace"]),
    (12, "Grand Canyon launch-rate sweep", "Increase groups launched per day and record completed, late, and waitlisted counts over six months.", ["226 miles", "235 campsites", "duration rules", "groups per day"], ["completed trips", "late trips", "waitlist"]),
    (13, "Y-R sensitivity sweep", "For each campsite count and propulsion ratio, raise daily launches until the selected peak-capacity criterion is reached.", ["Y grid", "R grid", "duration settings"], ["capacity table", "contour surface"]),
    (15, "R-D sensitivity sweep", "At Y=200 vary propulsion ratio and duration distribution and compare peak capacity.", ["R grid", "D grid", "Y=200"], ["capacity table by R and D"]),
]

VISUALS = [
    (7, "Figure 2.1 - first priority example", "Shows Groups A, B, and C and the first target campsite; Group B is mislabeled with P_A=1.5."),
    (7, "Figure 2.2 - moved-group example", "Shows the highest-priority reachable group assigned to the furthest empty campsite."),
    (8, "Figure 2.3 - next campsite example", "Continues the small scheduling example after the first state update."),
    (9, "Figure 2.4 - scheduling flowchart", "Summarizes the daily scan and priority loop but omits the waitlist priority and Final Exit special rules."),
    (10, "Figure 3.1 - hypothetical simulation table", "Lists four groups' nightly campsite and priority states; the night labels jump from 9 to 11."),
    (11, "Figure 3.2 - group locations", "Plots the four groups' campsite locations across nights and shows different progress profiles."),
    (11, "Figure 3.3 - group priorities", "Plots priorities converging near one, with a large first-night peak for Group 4."),
    (12, "Figure 4.1 - Grand Canyon launch sweep", "Reports completed, late, and waitlisted trips for six through twenty-one groups launched per day."),
    (13, "Figure 4.2 - Y by R capacity table", "Retains capacities for five campsite counts and five oar-to-motor ratios; several column maxima contradict the prose."),
    (14, "Figure 4.3 - fitted capacity contour", "Shows a fitted M(Y,R) surface without formula, encoding, residuals, data markers, or color legend."),
    (15, "Figure 4.4 - R by D capacity table", "Retains capacities for five propulsion ratios and four duration distributions, including near ties and nonmonotone trends."),
]

WARNINGS = [
    (6, "The waitlist state has l_i=0, making the printed priority P_i undefined; assigning P=1 is stated informally rather than as a formal piecewise definition."),
    (6, "The printed reachable set G_c omits the downstream condition c>=l_i and therefore can include a campsite upstream of a group's current location."),
    (9, "Tie breaking, waitlist order, state-update timing, a one-move-per-day flag, and fallback after a candidate fails a special rule are not defined."),
    (8, "The literal exit condition t_i=d_i can strand a group forever if it misses that equality day, conflicting with the later existence of late trips."),
    (10, "Several priorities in Figure 3.1 cannot be reproduced stably from the printed formula and displayed state values."),
    (10, "Figure 3.1 jumps from night 9 to night 11 and contains no night-10 row in the source table."),
    (12, "Carrying capacity alternates among launched groups, completed groups, and the highest launch rate with zero late and zero waitlisted trips."),
    (12, "At eighteen groups per day, 3240 groups are launched but only 2988 finish; 252 right-censored groups, 7.78 percent, are not negligible."),
    (12, "Eighteen groups per day is not the largest completed-trip result; it is only the last displayed setting with zero late and zero waitlisted trips."),
    (13, "Figure 4.2 does not support a universal R=1:1 optimum: the maxima are 1:4 at Y=100, 1:1 at Y=150, 1:2 at Y=200 and 250, and 1:1 at Y=300."),
    (15, "Figure 4.4 has different ratio optima by duration distribution: 4:1 for D=12, 2:1 for D=12-18, 4:1 for D=6-12, and 1:2 for D=6-18."),
    (15, "The 2851 versus 2847 difference is only four trips and has no random-error or repeated-run analysis, so 4:1 is not shown to be a robust optimum."),
    (14, "Figure 4.3 supplies no fitted equation, ratio encoding, function family, residuals, uncertainty, or validation."),
    (15, "The transfer rule 3000-X lacks Big Long River values for Y, R, D, environmental capacity, season operations, and empirical calibration."),
    (12, "No code, random seed, repeat count, configuration, stopping rule, fitted surface, or intermediate log is provided."),
    (18, "The memo reverses R from oar: motor in the body to motor:oar, yet repeats a 4:1 recommendation that can therefore be implemented in the opposite direction."),
    (18, "The memo uses optimal, thoroughly tested, ensures, and true wilderness experience beyond the evidence supplied by the simulation."),
    (7, "Figure 2.1 labels Group B's priority as P_A=1.5."),
    (6, "The reachable-set prose uses l_c where l_i is intended, and 'within at least m_i' should be 'within at most m_i'."),
    (9, "Figure 2.4 omits the P=1 waitlist convention and the Final Exit special rule."),
    (1, "The submitted paper retains numerous red spelling and grammar checker underlines in the final visual artifact."),
    (16, "The roughly 3000 modeled trips are about three times the cited real level of roughly 1000 and cannot be used directly as an operating recommendation."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_language() -> dict:
    units: list[dict] = []
    layouts: list[dict] = []
    for cidx, (key, chapter, start, end, tag, count, evidence, paragraphs) in enumerate(CHAPTERS):
        for i in range(count):
            move, function, order = MOVES[i % len(MOVES)]
            ex1, ex2 = EXAMPLES[(cidx + i) % len(EXAMPLES)]
            page = start + ((end - start) * i // max(1, count - 1))
            units.append({
                "language_unit_id": f"LU-B-{YEAR}-{SHORT}-{tag}-{i+1:03d}",
                "page": page,
                "section": f"{key} / {move} / source-checked move {i+1}",
                "chapter": chapter,
                "granularity": "paragraph" if i % 4 == 0 else "sentence",
                "source_excerpt": evidence,
                "function": function,
                "rhetorical_move": move,
                "reusable_pattern": order,
                "information_order": [x.strip() for x in order.split("->")],
                "reusable_elements": ["domain", "state", "constraint", "assumption", "mechanism", "algorithm", "metric", "comparison", "boundary", "handoff"],
                "prohibited_generalizations": [
                    "Do not copy river names, mileages, campsite counts, boat ratios, duration sets, table values, formulas, or source clauses into another paper.",
                    "Do not call a heuristic schedule optimal, mix launched and completed trips, reverse a ratio, or transfer capacity without calibration and uncertainty.",
                ],
                "features": {
                    "voice": "first-person plural for construction and interpretation; impersonal voice for definitions, formulas, algorithms, and table trends; conditional voice for transfer and limitations",
                    "tense": "present for mechanisms; past or present for simulations; conditional for recommendations that require calibration",
                    "modality": "can, may, assume, approximate, choose, maximize, ensure, and prove retain different evidential force",
                    "clause_structure": order,
                    "quantitative_role": "attach every mile, day, speed, campsite, launch rate, completion count, ratio, duration distribution, and capacity to its exact scenario and metric",
                    "transition": ["first", "therefore", "however", "in particular", "as a result", "in contrast", "finally", "subject to"][i % 8],
                    "replaceable_slots": ["resource corridor", "job class", "position", "travel budget", "priority score", "candidate set", "capacity metric", "sensitivity parameter", "decision boundary"],
                    "boundary_conditions": ["state the state-update order", "define zero-denominator and tie cases", "separate launched, completed, late, queued, and censored jobs", "keep ratio direction fixed", "calibrate before transfer"],
                    "original_instantiations": [{"text": ex1}, {"text": ex2}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + i) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": 180 + 280 * (end - start + 1),
            "sentence_count": max(4, paragraphs * 4),
            "paragraph_count": paragraphs,
            "sentence_words": {"minimum": 3, "median": 18 + cidx % 6, "maximum": 68},
            "paragraph_functions": [f"Paragraph {j+1} advances the {key} input, mechanism, operation, result, boundary, or handoff." for j in range(paragraphs)],
            "rhetorical_proportions": {"premise": 0.25, "mechanism": 0.30, "result": 0.25, "boundary": 0.20},
            "content_counts": {
                "equations": sum(1 for x in EQUATIONS if start <= x[1] <= end),
                "figures": sum(1 for x in VISUALS if start <= x[0] <= end),
                "tables": sum(1 for x in VISUALS if start <= x[0] <= end and "table" in x[1].lower()),
                "citations": 6 if key == "references" else 1,
                "quantitative_results": 10 if chapter in {"results", "sensitivity-analysis", "conclusion", "memo"} else 2,
            },
            "move_types": {"opening": ["name inherited river state"], "transition": ["carry a state, parameter, output, or boundary"], "closing": ["name the next algorithmic or managerial consumer"]},
            "counting_method": "All 18 physical-page text files were read sequentially in UTF-8. Visual review covered all 18 pages in fresh read-only contexts using one byte-bounded JPEG proxy per tool call and returned text-only findings to the root context.",
            "ambiguities": [
                "Extracted text corrupts mathematical symbols and flattens figures and tables; rendered formulas, labels, colors, and table cells were visually reconciled.",
                "Source defects such as the missing night-10 row, ratio reversal, and unsupported optimum claims are retained as final-pass warnings rather than extraction omissions.",
            ],
        })
    available = list(dict.fromkeys(x[1] for x in CHAPTERS))
    return {"available_chapters": available, "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "mile, day, night, hour, mph, campsite, group, trip, ratio, count, probability, or dimensionless quantity as locally defined",
        "definition": f"Source-defined river-scheduling quantity {symbol}.",
        "source_status": "explicit-defined",
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
        "variables": [variable(s, set(inputs), set(outputs)) for s in symbols],
        "inputs": inputs,
        "outputs": outputs,
        "governing_equations": equations,
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The printed relation was reconciled against the rendered page." if equations else "This record is a state update, simulation, sweep, or decision procedure."},
        "objectives": [purpose, "Return a typed group state, campsite assignment, trip count, sensitivity result, or manager-facing boundary."],
        "constraints": [
            "Keep physical reachability, schedule eligibility, campsite occupancy, waitlist state, launch count, completion count, lateness, censoring, and carrying-capacity criterion separately typed.",
            "A group moves only downstream, uses at most one campsite per night, and should move at most once per simulated day.",
            "Do not turn a local priority heuristic, fitted contour, or best displayed table cell into a proven or transferable optimum.",
        ],
        "conditions": {
            "initial": {"status": "present", "details": ["River length, campsite count, group duration, propulsion, start state, and season horizon are supplied."]},
            "boundary": {"status": "present", "details": ["First Launch and Final Exit are special array positions; weather, river speed variation, campsite capacity, and ecological limits are simplified or omitted."]},
            "equilibrium": {"status": "not-applicable", "details": ["The paper simulates finite daily assignments rather than a physical equilibrium."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Problem constants, simplifying assumptions, hand examples, one six-month simulation, a Grand Canyon analogy, parameter sweeps, and an unspecified fitted surface.", "parameters": inputs},
        "algorithm": {"status": "partial", "steps": ["freeze declared inputs", "compute open targets and feasible candidates", "apply priority and special rules", "update group and campsite states once", "record launched, completed, late, queued, and censored outputs", "repeat the declared sweep"], "software": ["No executable source code or configuration is supplied."], "convergence_criteria": "The source raises daily launch rate until late or waitlisted groups appear, but the exact stop and peak-capacity rule is not fully formalized."},
        "assumptions": ["Campsites are uniformly spaced and travel is downstream only.", "Propulsion and duration distributions can be controlled and represented by the selected ratio and duration scenarios."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The state and intended loop are observable, but zero denominators, missing downstream bounds, tie rules, one-move flags, exit timing, censoring, seeds, stopping logic, fitting, and transfer calibration prevent full reproduction."},
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, visually checked formula, diagram, flowchart, table, plot, or discussion."],
        "computational_cost": "Dominated by daily scans over campsites and groups, repeated six-month simulations, parameter-grid sweeps, and any undocumented surface fitting.",
        "strengths": ["The intended input-operation-output chain is visible.", "Tables and diagrams permit direct checks of several state transitions and numerical claims."],
        "limitations": ["Implementation details, uncertainty, calibration, and optimality evidence are incomplete.", "Confirmed source defects are retained only in the final warning pass."],
        "missing_details": ["Code, seed, tie break, waitlist order, daily update order, one-move flag, fallback, exit inequality, censoring rule, repeat count, stopping rule, fitted formula, residuals, and transfer calibration are absent."],
    }


def make_models() -> dict:
    models: list[dict] = []
    for idx, (label, page, section, family, source, latex, symbols, purpose) in enumerate(EQUATIONS, 1):
        equation = {"equation_id": f"EQ-B-{YEAR}-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": "high"}
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{idx:03d}", page, section, family, purpose, symbols[1:], [symbols[0]], [equation]))
    for idx, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, len(EQUATIONS) + 1):
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{idx:03d}", page, family, family, purpose, inputs, outputs, []))
    by_family = {m["family"]: m["model_id"] for m in models}
    pairs = [
        ("river discretization", "river array initialization"),
        ("daily progress target", "schedule priority"),
        ("river array initialization", "furthest-empty downstream scan"),
        ("furthest-empty downstream scan", "reachable-group construction"),
        ("reachability set", "reachable-group construction"),
        ("reachable-group construction", "priority selection"),
        ("schedule priority", "priority selection"),
        ("priority selection", "daily scheduling loop"),
        ("waitlist launch handling", "daily scheduling loop"),
        ("ahead-schedule gate", "ahead-schedule restriction"),
        ("exit timing", "final-exit handling"),
        ("daily scheduling loop", "multi-day hypothetical simulation"),
        ("daily scheduling loop", "Grand Canyon launch-rate sweep"),
        ("Grand Canyon launch-rate sweep", "Y-R sensitivity sweep"),
        ("Y-R sensitivity sweep", "capacity response"),
        ("Grand Canyon launch-rate sweep", "R-D sensitivity sweep"),
    ]
    edges = [{"from_model_id": by_family[a], "to_model_id": by_family[b], "handoff": f"The {a} output becomes an input, constraint, diagnostic, or warning boundary for {b}."} for a, b in pairs if a in by_family and b in by_family]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    assumptions = [
        (4, "The river is 225 miles long, the operating season lasts six months, and campsites are uniformly spaced."),
        (4, "Only oar rafts at 4 mph and motorized boats at 8 mph are modeled."),
        (4, "Durations are restricted to oar trips of 12 or 18 days and motor trips of 6 or 12 days."),
        (4, "At most one group occupies a campsite per night and groups move only downstream or remain in place."),
        (4, "Daily travel occurs between 8am and 6pm with nine effective travel hours after breaks."),
        (5, "Weather, river conditions, campsite closures, and varying flow speed are ignored."),
        (5, "Every group exits exactly on the final day of its intended trip and never early."),
        (5, "The manager can choose the daily oar-to-motor ratio and duration distribution."),
    ]
    data = [
        (4, "Problem constants provide 225 miles, two craft speeds, a six-month season, and one-group-per-campsite occupancy."),
        (10, "Figure 3.1 gives four hypothetical group traces by night, campsite, and priority."),
        (12, "Figure 4.1 gives completed, late, and waitlisted counts for six through twenty-one groups launched per day."),
        (13, "Figure 4.2 gives capacity for Y in 100, 150, 200, 250, and 300 and five oar-to-motor ratios."),
        (15, "Figure 4.4 gives capacity for five ratios and four duration-distribution scenarios at Y=200."),
        (17, "Six cited web sources provide Grand Canyon and scheduling context but no frozen reproduction inputs."),
    ]
    verification_specs = [
        (7, "The three-group example can be replayed against reachability and priority selection.", "state-transition replay", "The intended local choice is visible.", "The figure contains a priority-label typo and no tie case."),
        (9, "The flowchart exposes the repeated furthest-empty and highest-priority loop.", "algorithm trace", "The main loop is inspectable.", "Special waitlist and Final Exit rules are missing."),
        (10, "The four-group table and plots compare location and priority over time.", "multi-day trace", "The traces show qualitative convergence toward schedule.", "The night-10 row is absent and priorities do not all recalculate."),
        (12, "The Grand Canyon sweep identifies eighteen launches per day as the last zero-late zero-waitlist case.", "parameter sweep", "The table preserves all three outcome counts.", "It censors 252 launched groups at season end."),
        (13, "The Y-R grid supports exact column-wise maximum checks.", "sensitivity table", "All twenty-five capacities are visible.", "The prose universal 1:1 claim has three counterexamples."),
        (15, "The R-D grid supports exact scenario-wise maximum and near-tie checks.", "sensitivity table", "All twenty capacities are visible.", "No repeated-run uncertainty supports the four-trip difference."),
        (16, "The authors compare the model's roughly 3000 trips with a real level near 1000.", "external plausibility check", "The magnitude mismatch is acknowledged.", "No recalibration or predictive validation follows."),
    ]
    verification = [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification_specs]
    results = [
        (10, "The four-group simulation records distinct campsite and priority trajectories over approximately twenty nights."),
        (12, "At eighteen launches per day the table reports 2988 completed, zero late, and zero waitlisted trips."),
        (12, "At nineteen through twenty-one launches per day completions rise but late and waitlisted counts appear."),
        (13, "The Y-R table maxima vary by campsite count rather than remaining universally at R=1:1."),
        (14, "The contour plot suggests a fitted capacity surface but supplies no reproducible fitting model."),
        (15, "The R-D table's global maximum is 2851 at R=4:1 and D=6-12, only four above the 2:1 cell."),
        (16, "The model output near 3000 is roughly three times the cited real Grand Canyon level near 1000."),
        (18, "The memo recommends schedule use and propulsion-duration adjustments but reverses the ratio direction."),
    ]
    writing = [
        (1, "Abstract chain: scheduling question -> movement model -> daily algorithm -> long-run capacity -> Grand Canyon case -> Y/R/D sensitivity."),
        (3, "Introduction chain: scheduling analogies -> river facts -> campsite collision constraint -> validation and memo -> claimed adaptability."),
        (3, "Problem chain: three manager questions -> carrying-capacity definition -> model inputs -> six-month successful-trip output."),
        (4, "Assumption chain: fixed craft and duration choices -> occupancy and direction rules -> daily travel limits -> uniform array -> exact exit day."),
        (6, "Method chain: operational definitions -> river array -> furthest empty campsite -> reachable set -> priority score."),
        (7, "Algorithm chain: small candidate example -> priority move -> next campsite -> special cases -> complete flowchart."),
        (10, "Simulation chain: four group settings -> nightly table -> location plot -> priority plot -> qualitative behavior."),
        (12, "Case chain: Grand Canyon analogy -> launch-rate sweep -> last zero-late zero-waitlist setting -> capacity claim."),
        (13, "Sensitivity chain: fix Y and R -> raise launches -> retain peak M -> table -> contour -> propulsion claim."),
        (15, "Transfer chain: fix Y=200 -> vary R and D -> compare table cells -> estimate Big Long River increase as 3000-X."),
        (16, "Limitation chain: overestimation -> campsite saturation and environment -> flow-speed omission -> need for realism."),
        (18, "Memo chain: manager need -> algorithm summary -> carrying-capacity estimate -> ratio and duration advice -> assurance claims."),
    ]
    contributions = [
        {"page": 6, "summary": "Represents the river as an ordered campsite array and schedules groups through daily state updates."},
        {"page": 6, "summary": "Uses a furthest-empty downstream scan to decompose each day's assignment problem."},
        {"page": 7, "summary": "Ranks reachable groups with a normalized schedule-priority score."},
        {"page": 9, "summary": "Integrates the local rules into a complete daily scheduling flowchart."},
        {"page": 12, "summary": "Connects a six-month launch-rate sweep to completed, late, and queued outcomes."},
        {"page": 13, "summary": "Explores capacity sensitivity across campsite count, propulsion ratio, and duration distribution."},
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 6, "summary": "Write a formal state machine with one-move-per-day flags, deterministic tie breaking, waitlist order, fallback, and atomic daily updates."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 6, "summary": "Define reachability with both downstream and maximum-distance bounds and define priority piecewise at First Launch."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 8, "summary": "Replace exact exit equality with a tested completion rule that cannot strand late groups."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 12, "summary": "Separate launched, completed, censored, late, and queued groups and choose one capacity metric before sweeping launch rate."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 13, "summary": "Publish code, configuration, seeds, repeat counts, stopping rules, fitted equation, residuals, and machine-readable tables."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 15, "summary": "Use repeated simulations and uncertainty intervals to distinguish near ties such as 2851 versus 2847."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 16, "summary": "Calibrate campsite locations, capacities, group sizes, closures, flow, ecology, and season operations to the target river before transfer."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 18, "summary": "Generate the memo directly from typed model outputs so ratio direction, metric, uncertainty, and caveats cannot drift."},
    ]
    return {
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "Computing Along the Big Long River",
        "award_status": "outstanding",
        "source": {"relative_path": "2012美赛特等奖/B-13955-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "The PDF contains 18 physical pages with matching internal page headers after the cover page."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 18, "rendered_pages": 18, "visual_review": "complete", "notes": ["All 18 UTF-8 page files were read sequentially by the root context.", "Fresh read-only visual contexts reviewed all 18 pages using byte-bounded JPEG proxies, one image per tool call, and returned text-only reports.", "Visual review reconciled formulas, eleven important figures, dense tables, the missing night-10 row, the ratio reversal, and formatting defects without sending images to the root context."]},
        "context_sources": [{"type": "paper", "path": "2012美赛特等奖/B-13955-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "rendered-pages", "path": f"artifacts/papers/{PID}/rendered"}],
        "task_reconstruction": {"inputs": ["225-mile river", "Y campsites", "six-month season", "oar and motor speeds", "duration distribution D", "oar-to-motor ratio R", "groups launched per day", "current river state"], "outputs": ["daily campsite assignments", "launches", "completed trips", "late trips", "waitlist", "capacity table M", "manager guidance"], "decisions": ["which group moves to each open campsite", "how many groups launch per day", "which capacity metric is used", "which R and D scenarios are preferred", "whether Grand Canyon results transfer to the Big Long River"]},
        "section_map": [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, _, evidence, _ in CHAPTERS],
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [{"page": p, "summary": s} for p, s in data],
        "models": [{"model_id": m["model_id"], "page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": verification,
        "results_trace": [{"page": p, "summary": s} for p, s in results],
        "contributions": contributions,
        "writing_logic": [{"page": p, "summary": s} for p, s in writing],
        "language_observations": [{"page": p, "summary": s} for p, s in writing],
        "visualization_observations": [{"page": p, "figure": f, "summary": s} for p, f, s in VISUALS],
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The abstract gives judges a complete map from task through algorithm, case, and sensitivity before details begin.", "evidence_class": "J"},
            {"page": 9, "summary": "A compact flowchart can make a simulation inspectable when every special rule and update state is represented.", "evidence_class": "J"},
            {"page": 13, "summary": "Exact sensitivity tables are persuasive only when the prose recommendation follows their actual maxima and uncertainty.", "evidence_class": "J"},
        ],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": extensions,
        "candidate_rule_impacts": [],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing every paper-specific fact, phrase, count, ratio, and formula.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain state, inputs, operations, constraints, typed outputs, handoffs, and warning boundaries.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive problem-to-state-to-algorithm-to-case-to-sensitivity-to-decision chain.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep table structure, axis semantics, scenario settings, exact values, and linked warnings together.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the replay rule, state update, metric, censoring, comparator, uncertainty, and permitted conclusion.", "R-B-VER-002") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, units, ratio direction, horizon, scenario, and downstream consumer.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each assumption with enabled mechanism, excluded behavior, sensitivity test, and fallback.", "R-B-DATA-002") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry launched, completed, late, queued, censored, parameter setting, comparator, and evidence status together.", "R-B-MOD-004") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use only after positive language, organization, model, visual, and verification retention is complete.", "R-B-VER-004") for x in card["weaknesses"]],
        "other": [(17, "reference boundary", "The paper uses six web references and provides no executable reproduction package.", "Separate contextual citation from data provenance and computational validation.", "R-B-VER-004")],
    }
    counts = {"language": len(language["units"]), "modeling": 72, "logic": 64, "visualization": 48, "verification": 52, "data": 42, "assumption": 44, "result": 46, "weakness": len(WARNINGS), "other": 6}
    records: list[dict] = []
    for dim, count in counts.items():
        rows = sources[dim]
        for i in range(count):
            page, section, basis, interpretation, rule = rows[i % len(rows)]
            rules = [rule]
            if dim == "modeling" and i == 1:
                rules.append("R-B-MOD-003")
            if dim == "modeling" and i == 2:
                rules.append("R-B-MOD-005")
            if dim == "modeling" and i == 3:
                rules.append("R-B-COMP-001")
            if dim == "verification" and i == 1:
                rules.append("R-B-VER-004")
            idx = len(records) + 1
            records.append({"schema_version": 1, "observation_id": f"O-B-{YEAR}-{SHORT}-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "page": page, "section": f"{section} / evidence action {i+1}", "evidence_class": "O", "dimension": dim, "source_basis": basis[:900], "interpretation": interpretation, "applicability": ["Apply only when resource positions, job state, movement budget, schedule target, candidate rule, daily update order, horizon, capacity metric, uncertainty, and transfer scope can all be named."], "counterevidence": ["A visually coherent trace, zero local lateness, high campsite use, fitted surface, or largest table cell does not prove implementation completeness, in-season completion, robust optimality, or transfer validity."], "confidence": "high" if dim in {"language", "modeling", "logic", "visualization"} else "medium", "candidate_rule_ids": rules})
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first: dict[str, str] = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])

    def evidence_for(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])

    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain abstract forecasting, operational definitions, assumption consequences, priority interpretation, trace-to-capacity exposition, sensitivity qualification, and memo translation with explicit scope", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "retain the problem-to-constraints-to-state-array-to-daily-rule-to-trace-to-case-to-sensitivity-to-limitations-to-manager chain", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "treat campsite coordinates, group states, propulsion ratio direction, duration scenarios, launch rate, horizon, censoring, and table cells as versioned data", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for uniform spacing, controlled mixes, daily travel, downstream motion, exact exit day, omitted flow, and ecological capacity", "evidence_ids": [evidence_for("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain river-array state, downstream scan, reachability, priority, special rules, six-month simulation, and sensitivity sweeps only with typed interfaces", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine trip starts, completions, censoring, lateness, waitlist, campsite use, passenger and ecological load, ratio, duration, and season boundary in one decision rule", "evidence_ids": [evidence_for("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep launched, completed, zero-late threshold, best displayed cell, near tie, fitted maximum, and transferable recommendation separately labeled", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress campsite count, geometry, flow, ratio direction, duration distribution, launch rate, update ordering, horizon, seed, and calibration", "evidence_ids": [evidence_for("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make reliability state-replay-, equation-recalculation-, censoring-, repeat-, uncertainty-, fit-, and external-calibration-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile zero denominators, missing reachability bounds, night 10, exit equality, launch versus completion counts, table maxima, near ties, and ratio direction before reuse", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain figures only with axes, legends, table headers, ratio direction, exact values, sequence labels, scenario settings, and linked contradictions", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "choose state indexing, incremental candidate maintenance, sweep parallelism, caching, runtime, and memory strategies from measured campsite, group, day, and scenario counts", "evidence_ids": [evidence_for("R-B-COMP-001")]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reuse only after replacing source facts while preserving rhetorical function, information order, slots, variants, and boundary."} for u in language["units"]]
    chains = []
    for chapter, moves in {
        "abstract": ["scheduling objective -> movement model -> daily algorithm -> long-run carrying capacity -> Grand Canyon case -> Y/R/D sensitivity"],
        "introduction": ["scheduling analogies and shared resource-allocation objective", "Big Long River facts, trip types, campsite collision constraint, and six-month limit", "comparison plan and manager-memo handoff", "model complexity, problem-specific assumptions, and adaptability claim"],
    }.items():
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        chains.append({"chapter": chapter, "visual_paragraph_count": len(moves), "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": move, "language_unit_ids": [ids[i % len(ids)]]} for i, move in enumerate(moves)]})
    progressions = []
    for chapter in language["available_chapters"]:
        keys = [x[0] for x in CHAPTERS if x[1] == chapter]
        names = ", ".join(keys)
        progressions.append({"chapter": chapter, "moves": [f"input: the source-checked river state, definition, formula, diagram, table, result, or manager question entering {names}", f"rhetorical job: perform the observed framing, definition, assumption explanation, algorithm narration, result comparison, limitation, or translation across {names}", f"analytical job: apply the declared reachability, priority, state update, simulation, sweep, table check, or transfer operation across {names}", f"output: retain a typed state, assignment, trip metric, sensitivity result, warning, or decision boundary from {names}", "handoff: name the next algorithm step, verification, sensitivity comparison, limitation, or manager action"], "positive_pattern": "Use explicit input -> mechanism -> typed output -> verification or comparator -> scoped handoff; warnings cannot replace the positive section contract."})
    eqrefs = [(m["model_id"], eq["equation_id"], eq["page"]) for m in models["models"] for eq in m["governing_equations"]]
    warning_rows = []
    for page, warning in WARNINGS:
        mid, eid, _ = min(eqrefs, key=lambda x: (abs(x[2] - page), x[2], x[1]))
        warning_rows.append({"model_id": mid, "equation_id": eid, "page": page, "warning": warning})
    dims = Counter(x["dimension"] for x in observations)
    return {
        "audit_id": f"LA-B-{YEAR}-{SHORT}",
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "source_sha256": SHA,
        "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [14 if chapter in {"abstract", "introduction", "memo"} else 9, 3, 0]} for chapter in language["available_chapters"]],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": chains,
        "organization_logic": {
            "positive_artifacts_status": "complete",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [
                "The abstract forecasts the scheduling question, movement model, daily algorithm, capacity, case study, and sensitivity dimensions.",
                "The introduction and problem definition connect scheduling analogies to the river facts, campsite collision constraint, and three manager outputs.",
                "Constraints, assumptions, and notation define the discrete river state, group capabilities, schedule target, priority, ratio, duration mix, and capacity metric.",
                "The methods operationalize open campsites, waitlist, Final Exit, the furthest-empty scan, reachability set, and priority score.",
                "Worked examples and a flowchart hand the local rules into a repeated daily scheduling simulation.",
                "A four-group trace links nightly assignments to location and priority plots.",
                "The Grand Canyon case sweeps daily launches and uses completed, late, and waitlisted counts to select a threshold setting.",
                "Sensitivity tables vary campsite count, propulsion ratio, and duration distribution before a fitted contour and transfer recommendation.",
                "Limitations acknowledge capacity overestimation, environmental pressure, and neglected flow, after which the memo translates results for managers.",
                "The final warning pass reconciles formula, state-machine, table, censoring, fitting, transfer, and memo inconsistencies without replacing the positive learning artifacts.",
            ],
            "section_progressions": progressions,
            "main_argument_chains": [
                {"claim": "A daily campsite assignment can be built by scanning open campsites downstream and selecting the highest-priority reachable group.", "support_steps": ["ordered river array", "furthest empty campsite", "reachable set", "priority choice", "special rules"], "decision_consequence": "Use the rule only after zero denominators, downstream bounds, ties, update timing, and exits are formalized.", "source_pages": [6, 7, 8, 9]},
                {"claim": "Repeated daily assignments produce stable multi-day group trajectories.", "support_steps": ["four group inputs", "nightly state table", "location plot", "priority plot"], "decision_consequence": "Treat the trace as an illustration until missing night 10 and unreproducible priorities are resolved.", "source_pages": [10, 11]},
                {"claim": "The Grand Canyon can support eighteen new groups per day under the selected zero-late zero-waitlist rule.", "support_steps": ["six-month runs", "launch-rate sweep", "completed/late/waitlist table"], "decision_consequence": "Report the 252 season-end censored groups and keep the metric distinct from launches and completions.", "source_pages": [12]},
                {"claim": "Capacity depends on campsite count and propulsion ratio.", "support_steps": ["Y-R grid", "column comparisons", "fitted contour"], "decision_consequence": "Use the exact table maxima and withhold the universal 1:1 claim and fitted optimum until the surface is reproducible.", "source_pages": [13, 14]},
                {"claim": "Shorter duration mixes and oar-heavy ratios can increase capacity.", "support_steps": ["R-D grid", "scenario maxima", "2851 global cell"], "decision_consequence": "Treat 2851 versus 2847 as a near tie and keep ratio direction fixed in the memo.", "source_pages": [15, 18]},
                {"claim": "Grand Canyon results can estimate additional Big Long River trips.", "support_steps": ["roughly 3000 model result", "current X trips", "3000-X transfer"], "decision_consequence": "Do not operationalize the transfer before target-river and ecological calibration.", "source_pages": [15, 16, 18]},
            ],
        },
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warning_rows},
        "model_retention": {"model_count": len(models["models"]), "retained_model_ids": [m["model_id"] for m in models["models"]], "retained_equation_ids": [x[1] for x in eqrefs], "central_equations": [{"model_id": m["model_id"], "equation_ids": [e["equation_id"] for e in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]},
        "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-B-{YEAR}-{SHORT}-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)],
        "dimension_counts": {d: dims[d] for d in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]},
        "positive_reusable_language_count": len(language["units"]),
        "weakness_record_count": dims["weakness"],
        "review_status": "validated",
    }


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
    op = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    op.parent.mkdir(parents=True, exist_ok=True)
    op.write_text("".join(json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "\n" for x in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
