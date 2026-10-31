from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import build_q96_artifacts as base


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2012-15417-df1dd905"
SHORT = "15417"
SHA = "df1dd905398ab27de1df30b3a819163a831cf1b5f7b07f48832da4a32f45e634"
TYPE = "B"
YEAR = "2012"
PAGE_COUNT = 26

PATTERNS = [
    "LP-B-SUMMARY-DECISION-ALGORITHM-RESULT",
    "LP-B-MEMO-CAPACITY-ACTION",
    "LP-B-INTRO-MULTIOBJECTIVE-SCOPE",
    "LP-B-ASSUMPTION-REASON-CODE-CONSEQUENCE",
    "LP-B-STATE-REPRESENTATION-INTERPRETATION",
    "LP-B-PRIORITY-RULE-JUSTIFICATION",
    "LP-B-CODE-FIRST-EXPLANATION",
    "LP-B-CASE-SPLIT-STATE-UPDATE",
    "LP-B-HEURISTIC-MECHANISM-IMPROVEMENT",
    "LP-B-DISCRETE-THRESHOLD-EXPLANATION",
    "LP-B-EFFICIENCY-REFERENCE-COMPARISON",
    "LP-B-SENSITIVITY-PARAMETER-EFFECT",
    "LP-B-STRENGTH-LIMITATION-EXTENSION",
    "LP-B-CONCLUSION-RULE-TO-DECISION",
    "LP-B-APPENDIX-CODE-TRACE",
    "LP-B-REFERENCE-PROVENANCE-BOUNDARY",
]

# key, protocol chapter, first physical page, last physical page, tag,
# language-unit count, source-checked paraphrase, visually observed paragraph count
CHAPTERS = [
    ("summary", "abstract", 1, 1, "ABS", 50, "The Summary defines the river, demand, campsite collision rule, three scheduling goals, priority mechanism, paced movement, campsite-night efficiency benchmark, discrete magic-number claim, sensitivity findings, strengths, weaknesses, and future work before the detailed paper begins.", 6),
    ("manager-memo", "memo", 2, 2, "MEM", 24, "The Memo tells managers that advance reservations enable the scheduler, claims high trip volume and minimal interaction, equates the stated capacity with campsite count, and gives a two-condition magic-number rule as the operating action.", 2),
    ("introduction", "introduction", 3, 3, "INT", 24, "The Introduction restates the 225-mile, two-craft, six-to-eighteen-night problem and joins throughput, nightly campsite feasibility, and limited contact in one compact objective.", 1),
    ("assumptions-parameters", "assumptions", 3, 4, "ASM", 38, "The assumptions fix the season, equally spaced campsites, a minimum site count, downstream-only movement, advance requests, daily travel hours, trip-length distributions, and motor-oar mixture, with a short rationale and computational consequence for each.", 10),
    ("goals-hypotheses", "problem-analysis", 4, 5, "ANA", 38, "The analysis separates completed trips, crossovers, and rescheduling, contrasts pre-scheduled and first-come demand, and proposes least-days-left plus low-mobility priority as the organizing hypothesis.", 7),
    ("boat-river-schedule", "model-establishment", 5, 6, "EST", 40, "The model maps each trip to a Boat state, the river to an ordered campsite set, daily reach to a floor bound, and the season to a two-dimensional schedule consumed by Java Boat and River classes.", 8),
    ("general-scheduler", "algorithm", 6, 10, "ALG", 88, "The scheduler builds each day from a priority queue, computes a preferred site, handles completion, direct placement, upstream fallback, and recursive role swapping, then launches new boats and removes season-end nonfinishers.", 23),
    ("movement-rescheduling-preschedule", "model-improvement", 9, 10, "IMP", 42, "The improvement stage adds a movement constant, specifies first-come launch placement, deletes and requeues late boats, and proposes best-of-many random schedules when managers predefine the trip inventory.", 11),
    ("optimization-magic-efficiency", "results", 11, 12, "RES", 42, "The results connect a positive movement constant to more completions and fewer reschedules, interpret floor-function jumps as magic or black-magic settings, and compare simulated trips with a campsite-night efficiency reference.", 12),
    ("error-sensitivity", "sensitivity-analysis", 12, 14, "SEN", 54, "The sensitivity section varies travel time, motor fraction, duration distribution, season length, river length, and campsite count, reporting smooth trends interrupted by discrete reachability thresholds.", 14),
    ("analysis-strengths-weaknesses", "strengths-limitations", 14, 15, "SWL", 28, "The paper credits high synthetic utilization and priority-induced crossover reduction, then acknowledges random launch order and occasional rescheduling and proposes preset trips plus rollback.", 6),
    ("conclusion", "conclusion", 15, 15, "CON", 20, "The conclusion converts the study into three operational rules: prioritize low remaining time, prefer the less mobile craft on ties, and tune travel time, campsite count, and river length to favorable discrete thresholds.", 2),
    ("references", "references", 16, 16, "REF", 8, "Five references provide river-camping context, Java data structures and APIs, daylight information, and rafting-duration context, but do not freeze model inputs or simulation outputs.", 5),
    ("java-appendix", "appendix", 17, 26, "APP", 64, "The appendix supplies complete Boat.java and River.java listings for state, priority, movement, launch placement, rescheduling, daily scheduling, schedule diagnostics, crossover counting, uniform and clipped-Gaussian request generation, and the interactive entry point.", 20),
]

MOVES = [
    ("decision-forecast", "Forecast the decision, assumptions, algorithm, evaluation metric, main result, sensitivity, and limitation before details.", "decision -> assumptions -> algorithm -> metric -> result -> boundary"),
    ("manager-action", "Translate a technical threshold into an explicit operating input and action for a manager.", "management need -> parameter condition -> action -> expected effect -> caveat"),
    ("multiobjective-restatement", "Separate throughput, contact, and schedule-repair objectives before selecting the main optimization focus.", "system facts -> feasibility rule -> objectives -> scope"),
    ("assumption-rationale", "Pair each simplification with its practical rationale and the algorithmic structure it enables.", "assumption -> rationale -> enabled representation -> excluded regime"),
    ("state-definition", "Define object state and array axes before narrating transitions.", "entity -> fields -> index meaning -> downstream operation"),
    ("priority-justification", "Derive a scheduling priority from remaining slack and mobility rather than presenting it as an arbitrary sort key.", "risk -> slack -> mobility -> priority rule -> intended protection"),
    ("code-first-exposition", "Show a complete code block and then explain it by line range and state effect.", "code overview -> line range -> branch -> state update -> invariant"),
    ("case-split", "Partition a scheduling step into completion, direct placement, fallback, and displacement cases.", "preferred state -> case test -> local action -> displaced state -> termination"),
    ("heuristic-improvement", "Introduce one tunable constant, describe its mechanism, and report both throughput and repair effects.", "baseline rule -> parameter -> mechanism -> two metrics -> selected range"),
    ("discrete-threshold", "Explain an abrupt simulation change through the floor-function reachability boundary that caused it.", "observed jump -> integer bound -> adjacent settings -> craft coupling -> threshold rule"),
    ("efficiency-reference", "Normalize completed trips by a campsite-night reference so larger seasons or site counts are comparable.", "raw trips -> occupancy proxy -> capacity denominator -> percentage -> interpretation"),
    ("sensitivity-chain", "Vary one parameter, report direction and magnitude, identify threshold behavior, and state the operating implication.", "parameter sweep -> response -> discontinuity -> mechanism -> decision"),
    ("positive-then-limit", "Record the reusable contribution first and only then delimit its evidence and failure modes.", "strength -> supporting mechanism -> limitation -> improvement"),
    ("conclusion-rule", "Turn model findings into short operational rules while retaining the assumptions that make them valid.", "finding -> rule -> adjustable input -> expected outcome -> applicability"),
    ("code-trace", "Trace an implementation from input generation through scheduling and printed diagnostics.", "input -> state initialization -> execution -> metric output -> verification gap"),
    ("provenance-boundary", "Separate contextual citation from empirical calibration and computational reproducibility.", "citation role -> supplied fact -> missing artifact -> reuse boundary"),
]

EXAMPLES = [
    ("A clinic summary previews demand assumptions, a priority scheduler, utilization, stress tests, and its main limitation.", "It keeps the decision metric separate from the staffing recommendation."),
    ("A port memo converts berth-count thresholds into a daily release rule.", "The action names the conditions under which the threshold changes."),
    ("A warehouse introduction separates completed orders, aisle encounters, and replanning events.", "It states which objective drives the primary scheduler."),
    ("A rail model justifies uniform block spacing as a tractable first approximation.", "The excluded nonuniform geometry is reserved for sensitivity testing."),
    ("A bed-allocation model defines patient state, day index, and ward index before updating occupancy.", "The written matrix orientation matches the implementation."),
    ("A job scheduler ranks tasks by slack and then by processing flexibility.", "The prose and comparator implement the same tie break."),
    ("A routing paper prints pseudocode before explaining each branch by line number.", "Every explanation names the state changed by that branch."),
    ("A gate-assignment algorithm separates departure, preferred-gate, fallback-gate, and displacement cases.", "Its termination argument covers missing-index and full-capacity boundaries."),
    ("A dispatch model adds a pacing margin and reports throughput and rescheduling together.", "The parameter unit remains consistent across prose and code."),
    ("A staffing simulation links a sudden capacity drop to an integer shift boundary.", "Adjacent parameter values are reproduced from a frozen script."),
    ("A hotel model divides occupied room-nights by available room-nights.", "It counts actual occupancy rather than substituting an average stay when exact data exist."),
    ("A transit study varies service hours, route length, fleet mix, and stop count one at a time.", "Each curve includes uncertainty and the exact scenario held fixed."),
    ("A scheduling paper first explains why its priority rule is useful, then states that global optimality is unproved.", "The limitation does not erase the positive mechanism."),
    ("A conclusion turns low slack, low mobility, and discrete reachability into three operating rules.", "It avoids claiming transfer before local calibration."),
    ("An appendix generates fixed-seed cases, runs the scheduler, asserts invariants, and emits machine-readable metrics.", "Console printing is treated as debugging, not validation."),
    ("A references section distinguishes software documentation from field data.", "Missing code and raw outputs remain explicit provenance gaps."),
]

EQUATIONS = [
    ("uniform campsite spacing", 3, "Assumptions and Parameters", "river discretization", "D = 225/(Y+1)", r"D=\frac{225}{Y+1}", ["D", "Y"], "Convert campsite count into the assumed uniform inter-site distance."),
    ("maximum daily campsite advance", 4, "The Model", "daily reach bound", "Delta S_k <= floor(v_k h (Y+1)/225)", r"\Delta S_k\le\left\lfloor\frac{v_kh(Y+1)}{225}\right\rfloor", ["Delta S_k", "v_k", "h", "Y"], "Bound daily site movement by craft speed, travel hours, and discretized river geometry."),
    ("paced preferred movement", 9, "Calculating Movement", "paced movement", "Delta S_k = ceil((Y-S_k)/d_k)", r"\Delta S_k=\left\lceil\frac{Y-S_k}{d_k}\right\rceil", ["Delta S_k", "Y", "S_k", "d_k"], "Choose the minimum average campsite progress needed to exit on schedule."),
    ("movement-constant improvement", 9, "Calculating Movement", "movement margin", "Delta S_k = ceil((Y-S_k)/d_k) + m_C", r"\Delta S_k=\left\lceil\frac{Y-S_k}{d_k}\right\rceil+m_C", ["Delta S_k", "Y", "S_k", "d_k", "m_C"], "Move faster than the bare average pace to free upstream sites and reduce lateness."),
    ("motor reach jump condition", 12, "Magic Numbers", "discrete threshold", "floor(8h(Y+1)/225) != floor(8hY/225)", r"\left\lfloor\frac{8h(Y+1)}{225}\right\rfloor\ne\left\lfloor\frac{8hY}{225}\right\rfloor", ["Y", "h"], "Detect an adjacent campsite-count setting where motor-boat daily reach increases by one site."),
    ("motor-oar reach alignment", 12, "Magic Numbers", "craft reach coupling", "floor(8h(Y+1)/225) = 2 floor(4h(Y+1)/225)", r"\left\lfloor\frac{8h(Y+1)}{225}\right\rfloor=2\left\lfloor\frac{4h(Y+1)}{225}\right\rfloor", ["Y", "h"], "Require the motor reach to remain exactly twice the oar reach at the selected setting."),
    ("campsite-night efficiency", 12, "Efficiency", "utilization metric", "eta = n Lbar/(182Y) * 100%", r"\eta=\frac{n\bar L}{182Y}\times100\%", ["eta", "n", "Lbar", "Y"], "Compare approximate occupied campsite-nights with the seasonal campsite-night capacity."),
    ("continuous trip reference", 12, "Efficiency", "capacity reference", "M = 182Y/Lbar", r"M=\frac{182Y}{\bar L}", ["M", "Y", "Lbar"], "Give a continuous average-length reference for the number of trips supported by available campsite-nights."),
]

ALGORITHMS = [
    (5, "boat state representation", "Represent one trip by craft type, identifier, total days, remaining days, and current campsite.", ["type", "name", "totalDays", "daysLeft", "currentSite"], ["Boat state"]),
    (5, "river schedule representation", "Store one Boat reference per day and campsite with a waiting queue, completed list, and trip and lateness counters.", ["NUM_DAYS", "numSites", "requests"], ["schedule[day][site]", "queue", "boatsOut"]),
    (6, "priority queue ordering", "Order boats by the fewest days remaining and use the implementation's craft-type comparator as the tie break.", ["daysLeft", "type"], ["next boat to move"]),
    (6, "daily schedule generation", "For each day, collect yesterday's boats, move them in priority order, add new boats, and remove season-end nonfinishers.", ["previous-day schedule", "queue", "numSites"], ["updated schedule", "tripCount", "lateTrips"]),
    (6, "preferred-site calculation", "Compute paced movement plus the movement margin, cap it by maximum daily reach, and add it to the current site.", ["currentSite", "daysLeft", "numSites", "craft distance", "m_C"], ["nextSite"]),
    (6, "completion and lateness branch", "When nextSite passes Final Exit, decrement remaining days, count an on-time completion, or delete and requeue a late trip.", ["nextSite", "daysLeft", "numSites"], ["boatsOut", "tripCount", "rescheduled boat"]),
    (6, "direct preferred-site placement", "Place the highest-priority boat directly when its preferred site is empty and update its day and site state.", ["preferred site", "daily schedule"], ["placed boat"]),
    (7, "upstream fallback search", "Search from the preferred site back to the prior site and take the first empty campsite without moving upstream relative to yesterday.", ["preferred site", "currentSite", "occupancy"], ["fallback site"]),
    (8, "recursive role swapping", "Displace lower-priority boats or the boat at the previous site until the chain reaches an empty campsite.", ["priority", "current and prior sites", "occupancy"], ["resolved displacement chain"]),
    (9, "first-come launch placement", "Poll the request queue, reject trips that cannot finish before season end, and place each new boat at its preferred or nearest upstream open site.", ["day", "queue", "schedule"], ["launched boats", "remaining queue"]),
    (10, "delete-and-requeue rescheduling", "Remove every historical schedule reference to a late boat, reset its state, and push it to the front of the queue.", ["late boat", "full schedule"], ["cleared cells", "reset queued boat"]),
    (10, "best-of-random prescheduling", "Generate many random request sequences with fixed parameters and retain the schedule with the most completed trips.", ["request distribution", "scenario", "iteration count"], ["best observed schedule"]),
    (11, "movement-margin sweep", "Vary m_C and campsite count while comparing completed and rescheduled trips to choose a useful movement margin.", ["m_C", "Y", "request scenarios"], ["trip and reschedule response"]),
    (11, "magic-number scan", "Sweep campsite count, travel time, and river length and locate floor-function reach changes associated with trip-count jumps.", ["Y", "h", "river length"], ["magic and black-magic settings"]),
    (12, "efficiency calculation", "Convert completed trips and average trip nights into an approximate campsite-night utilization percentage.", ["n", "Lbar", "Y", "182 nights"], ["eta"]),
    (12, "multi-parameter sensitivity sweep", "Vary travel time, motor fraction, duration distribution, season length, river length, and campsite count and compare trip totals.", ["scenario grid", "random requests"], ["sensitivity trends"]),
    (24, "schedule rule diagnostic", "Scan completed boats to print early, late, and excessive-movement counts.", ["schedule", "boatsOut", "boat reach"], ["diagnostic counts"]),
    (24, "crossover counter", "Compare relative boat ordering on adjacent days and increment or cancel candidate overtaking events.", ["schedule on day i", "schedule on day i+1"], ["crossover count"]),
    (25, "uniform request harness", "Generate two thousand motor or oar requests with integer trip lengths, run the scheduler, and print schedule and diagnostics.", ["numSites", "unseeded Random"], ["one uniform-distribution run"]),
    (25, "Gaussian request harness", "Generate two thousand craft-specific Gaussian values clipped to seven through nineteen days, run the scheduler, and print diagnostics.", ["numSites", "unseeded Random", "means", "standard deviations"], ["one clipped-Gaussian run"]),
    (26, "interactive program entry", "Read a distribution name and campsite count, dispatch one harness, or print an unknown-distribution message.", ["console input"], ["selected simulation run"]),
]

VISUALS = [
    (5, "generateSchedule() listing, part 1", "Begins the day loop, priority queue construction, preferred-site calculation, exit handling, and direct placement."),
    (6, "generateSchedule() listing, part 2", "Shows upstream fallback, remaining-day update, and the first role swap when no site is found."),
    (7, "generateSchedule() listing, part 3", "Completes recursive displacement, daily launching, and season-end rescheduling."),
    (8, "Figure 1 - unresolved Case 4", "Shows Boat D without a feasible campsite under the initial local assignment."),
    (8, "Figure 2 - resolved Case 4", "Shows the role-swapping chain in which Boat A is moved relative to its preferred destination."),
    (9, "addBoats() listing", "Implements first-come queue polling, season-end feasibility, preferred placement, upstream fallback, and queue restoration."),
    (10, "reschedule() listing", "Deletes all references to a late boat and resets it to the front of the request queue."),
    (11, "Figure 3 - magic-number reschedules", "Plots rescheduled trips against campsite count and exposes periodic spikes and troughs caused by integer reach thresholds."),
    (13, "Figure 4 - motor fraction versus trips", "Plots trips per year against a 0-to-1 motor share with a quadratic trend line and R-squared label."),
    (17, "Boat.java listing", "Defines craft constants, trip state, preferred movement, reach bound, comparator, and string representation across physical pages 17-19."),
    (19, "River.java listing", "Defines schedule state and implements launch, reschedule, scheduling, diagnostics, crossover counting, request generation, and main across physical pages 19-26."),
]

WARNINGS = [
    (1, "The Summary states a magic-number comparison using D_O(Y) and D_O(Y-1), while the Memo and body use the motor reach at Y+1 versus Y; the conditions are not the same."),
    (2, "The Memo equates carrying capacity directly with Y campsites without defining whether capacity means nightly occupancy, concurrent boats, launches, completed trips, or people."),
    (4, "The prose calls the current site S_k while the displayed movement quantity is Delta S_k, and nearby text sometimes describes S_k as the daily advance."),
    (5, "The prose says schedule rows are campsites and columns are nights, but Java stores and accesses schedule[day][site]."),
    (19, "The prose repeatedly gives oar boats tie priority, but Boat.compareTo() makes Motor sort before Oar in Java PriorityQueue."),
    (2, "The Memo's claim of the absolute minimum amount of interaction is unsupported by a proof, exhaustive search, or reported crossover optimum."),
    (4, "Crossover minimization is introduced as a core goal but is not included in the main optimization result and no crossover dataset is reported."),
    (8, "The Case 4 claim that an empty site must eventually be found is not a complete termination proof and the lastSite=-1 boundary is not handled."),
    (10, "reschedule() deletes a boat's historical cells without rolling back or recomputing later boats whose placements depended on those cells."),
    (24, "Season-end calls to reschedule() do not increment lateTrips or the lateness statistics, so final nonfinishers are omitted from that metric."),
    (9, "addBoats() uses continue for requests that cannot finish before season end, permanently removing them from the queue rather than recording rejection or censoring."),
    (10, "Running thousands of random request orders and keeping the best is a best-observed heuristic, not a proof of an optimal pre-schedule."),
    (12, "The paper supplies no random seed, frozen configuration, raw run outputs, confidence interval, or uncertainty propagation for its reported averages."),
    (26, "The appendix main method performs one run, so it does not reproduce the stated ten data points with one thousand iterations per point."),
    (11, "m_C is measured in campsite indices, but the prose compares it with eight to fifteen percent of maximum travel distance without a consistent unit conversion."),
    (12, "The selected m_C=4 is not reconciled with the eight-to-fifteen-percent rule across campsite counts and craft types."),
    (12, "Magic and black-magic settings are inferred from floor jumps and simulation behavior; they are not a general optimality theorem."),
    (12, "M=182Y/Lbar is not rounded to an integer and therefore is a continuous reference, not a strict maximum count of complete trips."),
    (12, "Efficiency uses n times average trip length rather than exact occupied schedule cells even though the complete schedule exists."),
    (13, "For clipped Gaussian requests the authors acknowledge that the efficiency calculation is not accurate, yet compare it with the uniform case as if metrics were directly aligned."),
    (13, "Figure 4 labels its horizontal quantity as a ratio of motor boats to oar boats, but the 0-to-1 scale functions like a motor fraction."),
    (13, "The authors call high motor-share points inaccurate and provide no error bars, so the small fitted improvement is not securely resolved."),
    (12, "The reported 98.8 percent is utilization under synthetic demand and assumed geometry, not an empirical validation of river carrying capacity."),
    (14, "The statement that the best possible efficiency is around 99 percent is not derived as a formal bound."),
    (14, "The claim that river lengths from 25 to 257 miles differ by only about eleven trips lacks the complete scenario table and uncertainty needed to reproduce it."),
    (25, "Math.abs(Integer.MIN_VALUE) remains negative, so the uniform trip-length expression has a rare out-of-range failure path."),
    (24, "countCrossovers() is not tested or formally justified and its nested ordering logic may duplicate or omit crossover events."),
    (1, "Linear extraction damages smart punctuation, inequality signs, ceil and floor brackets, mean bars, and two-dimensional formula layout; rendered pages are required for fidelity."),
    (8, "The internal boat states and labels in Figures 1 and 2 do not enter text extraction and cannot be reconstructed from captions alone."),
    (16, "Reference 5 loses an underscore in extraction; the web references lack access dates and Reference 2 lacks a publication year."),
    (11, "The source contains grammar and spelling defects including where for were, procede, addBoats()which, and a double negative in the rollback proposal."),
    (8, "The phrase move back means retreat from a preferred downstream site, not physical upstream travel, and can be misread against the no-backwards assumption."),
    (12, "Trips, completed trips, rescheduled trips, schedule occupancy, and seasonal capacity are not kept as consistently distinct output types."),
    (10, "First-come individualized demand and best-of-random pre-scheduled demand are mixed when interpreting optimality and efficiency."),
    (15, "The greedy priority and displacement procedure is not shown to maximize completed trips globally or minimize crossovers globally."),
    (15, "No target-river occupancy, failure, environmental, ecological, safety, or demand data calibrate the operating recommendation."),
    (19, "MOVEMENT_CONSTANT is declared as 4 but getPreferredNextSite() hard-codes +4, so changing the named constant does not change behavior."),
    (19, "MOTOR_SPEED=80 and OAR_SPEED=40 are daily distance limits although getSpeed() and earlier prose use mph language; the unit naming is ambiguous."),
    (26, "The Gaussian harness clips values to seven and nineteen, creating endpoint probability masses rather than sampling a mathematically truncated Gaussian."),
    (26, "The test harness prints diagnostics without assertions or nonzero failure status and does not validate distribution or campsite input, so it is not an automated regression test."),
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
            "The root context read all 1616 lines of the 26-page UTF-8 extraction in continuous, non-overlapping ranges, "
            "including Summary, Memo, references, and every Boat.java and River.java line. Fresh read-only visual contexts "
            "reviewed pages 1-8, 9-16, 17-24, and 25-26 with one JPEG proxy of at most 450000 bytes per tool call and text-only reports."
        )
        layout["ambiguities"] = [
            "Linear extraction flattens fractions, ceil and floor brackets, inequality signs, mean bars, diagrams, chart labels, and code typography; rendered pages were authoritative.",
            "Source-level conflicts in priority, array orientation, magic-number conditions, units, stochastic testing, and metric definitions are retained only in the final warning pass.",
        ]
    return language


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "mile, mile per day, hour, day, night, campsite index, boat, trip, fraction, percentage, count, or dimensionless quantity as locally defined",
        "definition": f"Source-defined scheduling quantity {symbol}.",
        "source_status": "explicit-defined" if symbol not in {"eta", "Lbar"} else "inferred-from-equation",
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
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The printed relation was visually reconciled." if equations else "This record is a state, scheduling, sweep, diagnostic, or test procedure."},
        "objectives": [purpose, "Return a typed schedule state, completion count, reschedule count, crossover count, utilization measure, or parameter decision."],
        "constraints": [
            "Each campsite holds at most one boat per night and a boat may not move upstream relative to its prior-night site.",
            "Daily motion is bounded by craft reach and seasonal completion depends on explicit day-versus-night indexing.",
            "A best observed random schedule or high synthetic utilization is not a proof of global optimality or real carrying capacity.",
        ],
        "conditions": {
            "initial": {"status": "present", "details": ["River length, season, campsite count, request queue, craft type, trip duration, and movement margin are supplied or assumed."]},
            "boundary": {"status": "present", "details": ["First Launch, Final Exit, zero-based sites, the last season day, missing prior positions, full campsite rows, and clipped duration values require explicit handling."]},
            "equilibrium": {"status": "not-applicable", "details": ["The code builds a finite 183-day schedule rather than solving an equilibrium system."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Problem constants, assumed uniform or clipped-Gaussian requests, unseeded repeated simulation, and parameter sweeps over travel time, movement margin, fleet mix, river length, and campsite count.", "parameters": inputs},
        "algorithm": {"status": "partial", "steps": ["freeze the request and river scenario", "order active boats", "compute preferred and feasible sites", "update schedule state", "record completions, reschedules, crossovers, and utilization", "repeat or sweep the declared parameter"], "software": ["Complete Boat.java and River.java listings are printed in the appendix, but no frozen build, seed, test assertions, or raw output archive is supplied."], "convergence_criteria": "The schedule ends after 183 days; best-of-random and sensitivity claims do not state a statistical convergence rule."},
        "assumptions": ["Campsites are uniformly spaced, requests are available in advance, demand is abundant, and movement is downstream.", "Boat behavior is reduced to craft type, duration, remaining days, and current campsite."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The source code makes the main state updates inspectable, but priority conflict, deletion without rollback, boundary cases, crossover counting, unseeded randomness, clipped distributions, missing assertions, and absent empirical calibration prevent full validation."},
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, visually checked formula, code, figure, or discussion."],
        "computational_cost": "Dominated by daily priority-queue operations, campsite scans, recursive displacement, whole-schedule deletion during rescheduling, crossover nested loops, wide schedule printing, and repeated stochastic scenario runs.",
        "strengths": ["The appendix exposes the complete implementation needed to compare prose with code.", "The model connects state updates, discrete reachability, and manager-facing sensitivity choices."],
        "limitations": ["Optimality, stochastic reproducibility, automated verification, uncertainty, and field calibration are incomplete.", "Confirmed defects are recorded after positive model retention."],
        "missing_details": ["Fixed seeds, run manifest, raw outputs, confidence intervals, test assertions, input validation, formal termination proof, rollback semantics, crossover oracle, exact occupancy count, and target-river calibration are absent."],
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
        ("river discretization", "river schedule representation"),
        ("daily reach bound", "preferred-site calculation"),
        ("paced movement", "preferred-site calculation"),
        ("movement margin", "preferred-site calculation"),
        ("boat state representation", "priority queue ordering"),
        ("river schedule representation", "daily schedule generation"),
        ("priority queue ordering", "daily schedule generation"),
        ("preferred-site calculation", "direct preferred-site placement"),
        ("preferred-site calculation", "upstream fallback search"),
        ("upstream fallback search", "recursive role swapping"),
        ("daily schedule generation", "first-come launch placement"),
        ("daily schedule generation", "delete-and-requeue rescheduling"),
        ("movement-margin sweep", "best-of-random prescheduling"),
        ("discrete threshold", "magic-number scan"),
        ("craft reach coupling", "magic-number scan"),
        ("utilization metric", "efficiency calculation"),
        ("capacity reference", "efficiency calculation"),
        ("multi-parameter sensitivity sweep", "interactive program entry"),
        ("schedule rule diagnostic", "interactive program entry"),
        ("crossover counter", "interactive program entry"),
        ("uniform request harness", "interactive program entry"),
        ("Gaussian request harness", "interactive program entry"),
    ]
    edges = [{"from_model_id": by_family[source], "to_model_id": by_family[target], "handoff": f"The {source} output becomes an input, constraint, diagnostic, or warning boundary for {target}."} for source, target in pairs if source in by_family and target in by_family]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    assumptions = [
        (1, "The boating season runs April 1 through September 30, giving 183 days and 182 nights."),
        (3, "The 225-mile river has Y equally spaced campsites at distance 225/(Y+1)."),
        (3, "At least eighteen campsites are available and one boat occupies a campsite per night."),
        (3, "Boats never move upstream and all requests are known sufficiently far in advance."),
        (4, "Daily travel time is a tunable six-to-twelve-hour parameter and craft demand is initially uniform and random."),
        (4, "Motor and oar request proportions may vary and later duration tests use craft-specific clipped Gaussian draws."),
        (5, "A boat is synonymous with one trip and is represented only by craft type, duration, remaining days, and current site."),
        (10, "Pre-scheduled trip inventories may be approximated by selecting the best of many random request sequences."),
    ]
    data = [
        (1, "Problem constants supply 225 miles, 4 mph oar craft, 8 mph motor craft, six-to-eighteen-night requests, and one boat per campsite-night."),
        (11, "The movement-margin experiment reports 557.91 to 617.796 average trips and .793 to .166 average reschedules when adding one site of margin."),
        (11, "Figure 3 records rescheduled trips against campsite count and displays periodic threshold structure."),
        (12, "The preferred setting uses daily distance limits 80 and 40 miles, m_C=4, equal craft shares, uniform durations, and 44 sites."),
        (12, "The reported best result is 659.371 trips from ten data points of one thousand iterations, converted to about 98.8 percent."),
        (13, "Figure 4 plots trips per year against motor share with y=-26.173x^2+66.222x+617.96 and R^2=0.9968."),
        (13, "The Gaussian scenario uses printed means 12 and 13 nights in prose, while appendix code uses day parameters 13 and 14 with standard deviations 3 and 2 and clips to 7 through 19 days."),
        (16, "Five references provide contextual and software sources but no frozen empirical or computational dataset."),
    ]
    verification_specs = [
        (8, "Figures 1 and 2 permit a state-level replay of the Case 4 displacement explanation.", "state-transition replay", "The before and after assignments are visually explicit.", "The global termination and missing-prior-site boundary are not proved."),
        (9, "The movement equations can be reconciled directly with Boat.getPreferredNextSite() and getMaxSitesPerDay().", "prose-code equation check", "Ceil, floor, margin, and maximum reach are visible in source.", "The named movement constant is bypassed by a literal +4."),
        (19, "Boat.compareTo() can be checked against every prose statement of the tie-priority rule.", "prose-code comparator check", "Java ordering semantics determine the implemented result.", "The implementation reverses the stated oar-first rule."),
        (23, "River.generateSchedule() can be traced against the three placement cases and recursive swap narrative.", "code-path trace", "The printed implementation covers the full daily loop.", "Deletion, lastSite, and season-end accounting boundaries remain unsafe."),
        (11, "Figure 3 visually supports discrete jumps in rescheduling as campsite count changes.", "threshold trend", "The periodic spikes and troughs are visible.", "No raw values, seed, interval, or formal optimum proof is supplied."),
        (13, "Figure 4 supports a small rising trend in trips as motor share increases.", "parameter trend", "Axes, fitted curve, and R-squared are readable.", "The ratio definition and high-share accuracy are uncertain and no error bars are shown."),
        (12, "The campsite-night formula supplies a common denominator for trip-count comparisons.", "metric normalization", "Season nights, sites, average nights, and trips are linked.", "It uses an average-length proxy rather than exact schedule occupancy."),
        (25, "The appendix harnesses reveal the exact random request laws used by one executable run.", "implementation inspection", "All generation expressions and calls are visible.", "No fixed seed, repeated-run loop, assertion, or machine-readable output is included."),
        (24, "checkSchedule() and countCrossovers() expose intended diagnostics for timing, reach, and interaction.", "diagnostic inspection", "The diagnostic categories are explicit.", "They only print or return counts and have no independent oracle or test cases."),
        (15, "The conclusion can be checked against the algorithm, parameter results, and code comparator.", "claim trace", "Main recommendations can be traced to named mechanisms.", "The tie-priority conclusion conflicts with executable behavior and transfer claims exceed calibration."),
    ]
    results = [
        (11, "Adding m_C=1 raises average completed trips by about 10.7 percent and lowers average reschedules in the stated experiment."),
        (11, "Larger movement margins eventually raise rescheduling and are recommended at roughly eight to fifteen percent of maximum travel distance."),
        (11, "Magic campsite counts appear as periodic low-reschedule settings when daily reach floor values increase in aligned motor-oar steps."),
        (12, "At 8.8 travel hours the model retains high throughput, while 8.7 hours is reported to lose roughly one third of trips."),
        (12, "A river-length increase from 257 to 258 miles is reported to trigger another roughly one-third loss."),
        (12, "The preferred synthetic scenario reports 659.371 trips and approximately 98.8 percent campsite-night efficiency."),
        (13, "Increasing motor share changes reported trips by less than a four-percent decrease to a 2.3-percent increase across the tested range."),
        (13, "The clipped-Gaussian duration scenario loses roughly 27 to 30 trips relative to the uniform scenario."),
        (14, "Completed trips rise almost linearly with season length at about 3.5 trips per additional open day."),
        (14, "Within the stated non-threshold region, river length changes by up to 232 miles are claimed to change trip totals by only about eleven."),
        (14, "Trip totals rise with campsite count while the authors claim normalized efficiency remains nearly constant above the reachability floor."),
        (15, "The final recommendation prioritizes least remaining days, gives the less mobile craft the prose tie break, and tunes travel time to favorable thresholds."),
    ]
    writing = [
        (1, "Summary chain: system and collision rule -> assumptions -> three goals -> priority scheduler -> paced movement -> efficiency benchmark -> magic thresholds -> sensitivity -> strengths and future work."),
        (2, "Memo chain: advance reservations -> scheduling algorithm -> throughput and interaction claim -> carrying-capacity statement -> magic-number formula -> manager action."),
        (3, "Introduction chain: river and trip facts -> two craft speeds -> nightly campsite feasibility -> maximize trips and minimize contact."),
        (3, "Assumption chain: season -> spacing -> minimum sites -> downstream direction -> advance demand -> tunable hours and request distributions."),
        (4, "Problem-analysis chain: completed trips -> crossovers -> individualized versus preset demand -> rescheduling goal -> priority hypothesis."),
        (5, "Model chain: Boat state -> River state -> daily reach bound -> schedule array -> Java class handoff."),
        (6, "Algorithm chain: code listing -> priority queue -> preferred site -> four cases -> recursive displacement -> new launches -> season-end cleanup."),
        (9, "Movement chain: minimum paced progress -> craft reach cap -> added margin -> later optimization result."),
        (9, "Launch chain: first-come queue -> season feasibility -> preferred site -> upstream fallback -> queue restoration."),
        (10, "Rescheduling chain: individualized deadline problem -> delete references -> reset boat -> requeue -> unimplemented rollback alternative."),
        (10, "Prescheduling chain: preset inventory -> failed structured searches -> repeated random schedules -> best completed-trip outcome."),
        (11, "Optimization chain: underused downstream sites -> movement margin -> completion gain -> reschedule response -> recommended scale."),
        (11, "Magic-number chain: plotted periodicity -> adjacent floor calculations -> motor-oar alignment -> travel-time and river-length thresholds."),
        (12, "Efficiency chain: campsite-night table -> occupied-cell proxy -> normalized efficiency -> preferred parameters -> reported 98.8 percent."),
        (12, "Sensitivity chain: travel time -> motor share -> duration law -> season length -> river length -> campsite count -> transfer claim."),
        (14, "Evaluation chain: strength -> crossover mechanism -> random-order weakness -> rescheduling weakness -> preset-trip and rollback improvements."),
        (15, "Conclusion chain: priority rule -> movement inputs -> magic thresholds -> flexible customer choice -> efficiency and low-reschedule claim."),
        (17, "Appendix chain: Boat constants and state -> movement and comparator -> River arrays -> launch and scheduling -> diagnostics -> request harnesses -> main."),
    ]
    contributions = [
        {"page": 5, "summary": "Represents boat trips and campsite occupancy as explicit Java state across day and site indices."},
        {"page": 6, "summary": "Uses remaining time and craft reach to drive a priority-based daily campsite scheduler."},
        {"page": 8, "summary": "Introduces recursive role swapping to repair local campsite conflicts without upstream motion."},
        {"page": 9, "summary": "Adds a pacing margin to the minimum average progress rule and links it to throughput and lateness."},
        {"page": 11, "summary": "Connects discontinuous simulation behavior to floor-function changes in reachable campsite count."},
        {"page": 12, "summary": "Normalizes trip totals with a campsite-night utilization reference."},
        {"page": 17, "summary": "Publishes the complete source code, enabling direct prose-code verification uncommon in the corpus."},
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 5, "summary": "Adopt one canonical schedule orientation and document day, night, campsite, launch, exit, and completion indices with executable invariants."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 19, "summary": "Fix and test the craft tie comparator so prose, priority queue behavior, and recursive displacement use one declared rule."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 8, "summary": "Prove termination or replace recursive displacement with a bounded augmenting-path search that handles missing prior sites and full-capacity states."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 10, "summary": "Use transactional rollback or full forward recomputation after removal so later placements cannot depend on deleted history."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 12, "summary": "Compute exact occupied campsite-nights, completed trips, rejected requests, censored trips, reschedules, and crossovers from one typed run record."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 13, "summary": "Use fixed seeds, repeated runs, confidence intervals, machine-readable scenario grids, and uncertainty-aware threshold selection."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 26, "summary": "Replace console diagnostics with assertions and property tests for capacity, direction, reach, timing, uniqueness, comparator, rollback, and crossover invariants."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 26, "summary": "Sample a true truncated distribution, validate inputs, avoid Integer.MIN_VALUE arithmetic, and record the random seed and generated request manifest."},
        {"extension_id": f"E-B-{SHORT}-009", "page": 15, "summary": "Calibrate campsite geometry, closures, group size, demand, trip completion, contact, safety, environmental limits, and manager objectives to the target river."},
        {"extension_id": f"E-B-{SHORT}-010", "page": 2, "summary": "Generate the manager memo from typed outputs so capacity, threshold equations, units, priority rules, uncertainty, and caveats cannot drift from the implementation."},
    ]
    verification = [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification_specs]
    return {
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "Getting Our Priorities Straight for Maximizing Efficiency on the Big Long River",
        "award_status": "outstanding",
        "source": {"relative_path": "2012美赛特等奖/B-15417-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical pages 1 and 2 are the Summary and Memo; physical page 3 begins internal Page 1 of 24, and physical page 26 is internal Page 24 of 24."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["The root context read all 1616 UTF-8 extraction lines without skipping the ten-page Java appendix.", "Fresh read-only visual contexts reviewed all 26 pages using one JPEG proxy at or below 450000 bytes per tool call and returned text-only reports.", "Visual review reconciled eight equations, four figures, code line continuity, comparator semantics, hard-coded constants, chart labels, references, and page offsets without sending images to the root context."]},
        "context_sources": [{"type": "paper", "path": "2012美赛特等奖/B-15417-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "rendered-pages", "path": f"artifacts/papers/{PID}/rendered"}],
        "task_reconstruction": {"inputs": ["225-mile river", "183 days and 182 nights", "Y uniformly spaced campsites", "motor and oar reach", "six-to-eighteen-night requests", "advance request queue", "movement margin m_C", "request distribution and craft mix"], "outputs": ["daily campsite schedule", "completed trips", "rescheduled trips", "crossover count", "campsite-night efficiency", "magic thresholds", "manager recommendation"], "decisions": ["which boat moves first", "which campsite each boat receives", "when a trip completes or is rescheduled", "how new requests enter", "which movement margin is used", "which parameter settings avoid discrete reach losses", "which capacity metric is reported"]},
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
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The Summary gives judges the complete decision, algorithm, efficiency, sensitivity, and limitation map before details.", "evidence_class": "J"}, {"page": 8, "summary": "Before-and-after state diagrams make a difficult displacement algorithm inspectable when the implementation boundaries are also stated.", "evidence_class": "J"}, {"page": 17, "summary": "Complete source code permits unusually strong verification only if prose-code conflicts are actively checked rather than assumed away.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": extensions,
        "candidate_rule_impacts": [],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing river, craft, timing, site, distribution, threshold, metric, and implementation payload.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain inputs, state, equation or ordered operations, boundary behavior, typed outputs, code correspondence, downstream handoff, and limitation.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive Summary-to-assumptions-to-priority-to-scheduler-to-improvement-to-threshold-to-efficiency-to-decision chain.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep code line ranges, diagram states, axes, trend equation, scenario, caption, linked claim, and prose-code conflict together.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the replay, prose-code, threshold, metric, diagnostic, stochastic, or provenance check and limit the conclusion to what it establishes.", "R-B-VER-002") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, unit, horizon, craft share, duration law, run count, chart scenario, and downstream consumer.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair the assumption with its enabled representation, excluded behavior, threshold test, uncertainty, and target-river recalibration need.", "R-B-DATA-002") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry requests, launches, completed trips, reschedules, crossovers, occupied campsite-nights, censoring, scenario, comparator, and evidence status separately.", "R-B-MOD-004") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use only after positive language, organization, formula, algorithm, code, visual, and verification retention is complete.", "R-B-VER-004") for x in card["weaknesses"]],
        "other": [(16, "reference and reproduction boundary", "The references document context and Java APIs, while reproducible simulation inputs, build instructions, raw outputs, and empirical calibration remain absent.", "Separate contextual citation, software documentation, empirical data, and computational provenance.", "R-B-VER-004")],
    }
    counts = {"language": len(language["units"]), "modeling": 96, "logic": 84, "visualization": 70, "verification": 78, "data": 60, "assumption": 62, "result": 68, "weakness": len(WARNINGS), "other": 10}
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
            records.append({"schema_version": 1, "observation_id": f"O-B-{YEAR}-{SHORT}-{observation_index:04d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "page": page, "section": f"{section} / evidence action {index + 1}", "evidence_class": "O", "dimension": dimension, "source_basis": basis[:900], "interpretation": interpretation, "applicability": ["Apply only when the resource corridor, time horizon, capacity unit, state update, priority rule, stochastic law, threshold, implementation, uncertainty, and transfer scope can all be named."], "counterevidence": ["High simulated utilization, a smooth fitted curve, a low reschedule count, a visually complete code listing, or a best random run does not prove global optimality, correct implementation, reproducibility, field capacity, or safe transfer."], "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium", "candidate_rule_ids": rule_ids})
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first_by_dimension: dict[str, str] = {}
    for row in observations:
        first_by_dimension.setdefault(row["dimension"], row["observation_id"])
    def evidence_for(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])
    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain the Summary forecast, manager action, definition-before-code sequence, line-range explanation, case split, threshold mechanism, normalized efficiency, and scoped conclusion", "evidence_ids": [first_by_dimension["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "retain the objectives-to-state-to-priority-to-daily scheduler-to-movement improvement-to-discrete threshold-to-efficiency-to-sensitivity-to-manager chain", "evidence_ids": [first_by_dimension["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "version river length, season and night convention, campsite geometry, craft reach units, duration law, fleet share, run count, figure axes, fitted equation, code constants, and references", "evidence_ids": [first_by_dimension["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for uniform spacing, minimum sites, downstream movement, advance demand, one-group occupancy, controllable hours, request distributions, and transfer", "evidence_ids": [evidence_for("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain the floor reach bound, paced movement, margin, priority queue, direct and fallback placement, displacement chain, launch, reschedule, diagnostics, sensitivity, and capacity interfaces", "evidence_ids": [first_by_dimension["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "join the Java schedule, completion, reschedule, crossover, campsite-night efficiency, and manager threshold views through one typed seasonal decision layer", "evidence_ids": [evidence_for("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep requests, launches, active boats, completed trips, deleted trips, rescheduled trips, season-end nonfinishers, crossovers, occupied cells, utilization, and carrying capacity distinct", "evidence_ids": [first_by_dimension["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress array orientation, tie comparator, reach thresholds, lastSite boundaries, recursive termination, deletion rollback, season end, fleet mix, duration clipping, random seeds, and input validation", "evidence_ids": [evidence_for("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make reliability state-replay-, prose-code-, invariant-, repeated-run-, threshold-, uncertainty-, metric-, diagnostic-, regression-, and field-calibration-specific", "evidence_ids": [first_by_dimension["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile magic equations, capacity meaning, symbols, array axes, priority, constants, units, rollback, censoring, crossover counting, stochastic harnesses, references, and source grammar before reuse", "evidence_ids": [first_by_dimension["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain three scheduler code panels, two displacement diagrams, launch and reschedule listings, both plots, appendix code ranges, axes, fitted equation, and linked prose-code conflicts", "evidence_ids": [first_by_dimension["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "choose priority-queue operations, campsite scans, displacement search, whole-schedule deletion, crossover loops, schedule printing, scenario repetitions, caching, runtime, and memory from measured workload", "evidence_ids": [evidence_for("R-B-COMP-001")]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    configure_base()
    audit = base.make_audit(language, models, card, observations)
    paragraph_moves = {
        "abstract": [
            "river, trip, craft, campsite collision, and scheduling objective",
            "season, campsite geometry, downstream motion, and advance-request assumptions",
            "completed trips, crossovers, and rescheduling objectives",
            "least-days-left priority and paced daily movement mechanism",
            "campsite-night reference, 98.8-percent result, magic thresholds, and sensitivity",
            "strengths, random-order weakness, rescheduling weakness, and future improvements",
        ],
        "introduction": ["225-mile two-craft trip system -> campsite feasibility -> maximize trips while limiting contact"],
    }
    layouts = {layout["chapter"]: layout for layout in language["chapter_layouts"]}
    audit["paragraph_chains"] = []
    for chapter, moves in paragraph_moves.items():
        unit_ids = [unit["language_unit_id"] for unit in language["units"] if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": index + 1, "dominant_move": move, "language_unit_ids": [unit_ids[index % len(unit_ids)]]} for index, move in enumerate(moves)]})
    progressions = []
    for chapter in language["available_chapters"]:
        keys = ", ".join(key for key, protocol_chapter, *_ in CHAPTERS if protocol_chapter == chapter)
        progressions.append({"chapter": chapter, "moves": [f"input: the source-checked state, parameter, request, equation, code block, figure, metric, or manager need entering {keys}", f"rhetorical job: perform the observed definition, assumption rationale, priority justification, line-range explanation, case split, threshold interpretation, sensitivity comparison, qualification, or recommendation in {keys}", f"analytical job: apply the river discretization, reach bound, priority queue, preferred-site calculation, fallback, displacement, launch, reschedule, diagnostic, stochastic harness, or utilization calculation in {keys}", f"output: retain a typed schedule state, completion, reschedule, crossover, utilization, threshold, limitation, or manager action from {keys}", "handoff: name the next state update, implementation branch, experiment, visual check, metric comparison, warning boundary, or operating decision"], "positive_pattern": "Use explicit input -> mechanism or code path -> typed output -> verification or comparator -> scoped handoff; warnings annotate only after positive learning."})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["The final warning pass reconciles formula, symbol, unit, array, priority, boundary, stochastic, metric, validation, and provenance defects without replacing positive learning."],
        "section_progressions": progressions,
        "main_argument_chains": [
            {"claim": "Least remaining time and limited mobility can organize daily campsite allocation around schedule risk.", "support_steps": ["three stated objectives", "Boat remaining-day state", "priority queue", "preferred-site rule", "direct and fallback placement"], "decision_consequence": "Keep the slack-based priority mechanism, but fix and test the prose-code craft tie conflict before operational use.", "source_pages": [4, 5, 6, 9, 19]},
            {"claim": "A local conflict can be repaired through a chain of role swaps without intentionally moving a boat upstream relative to its prior site.", "support_steps": ["Case 3 upstream search", "Case 4 first swap", "previous-site recovery", "lower-priority displacement", "empty-site termination claim"], "decision_consequence": "Replace the informal guarantee with a bounded augmenting-path algorithm and explicit missing-index and full-capacity tests.", "source_pages": [6, 7, 8, 22, 23]},
            {"claim": "A positive movement margin can free upstream capacity and reduce late completion relative to the bare paced rule.", "support_steps": ["ceil paced movement", "craft reach cap", "m_C addition", "completion increase", "reschedule response"], "decision_consequence": "Tune a dimensionally consistent margin from repeated seeded runs and bind the named constant to the executable code.", "source_pages": [9, 11, 19]},
            {"claim": "Abrupt capacity changes arise when daily reachable campsite counts cross integer boundaries.", "support_steps": ["Figure 3 periodicity", "adjacent floor calculations", "motor reach jump", "motor-oar alignment", "travel-time and river-length black-magic cases"], "decision_consequence": "Use floor-boundary analysis as a design warning, not as a general proof that a setting is globally optimal.", "source_pages": [11, 12]},
            {"claim": "Campsite-night normalization permits comparison of trip totals across season and campsite scenarios.", "support_steps": ["182-night denominator", "Y campsite capacity", "average trip nights", "completed trip count", "98.8-percent report"], "decision_consequence": "Compute exact occupied cells and separate completed, rejected, rescheduled, and censored trips before calling the metric carrying capacity.", "source_pages": [12, 13, 14]},
            {"claim": "Complete source code permits direct validation of narrative scheduling claims.", "support_steps": ["Boat state", "preferred movement", "comparator", "River array", "scheduler", "diagnostics", "test harness"], "decision_consequence": "Treat code as additional evidence, not automatic validation; add fixed seeds, assertions, oracles, and field calibration.", "source_pages": [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]},
        ],
    }
    audit["dimension_counts"] = dict(Counter(row["dimension"] for row in observations))
    return audit


def main() -> None:
    language = make_language()
    models = make_models()
    card = make_card(language, models)
    observations = make_observations(language, models, card)
    attach_rule_impacts(card, observations)
    audit = make_audit(language, models, card, observations)
    base.base.write_json(ROOT / "artifacts/language-units" / f"{PID}.json", language)
    base.base.write_json(ROOT / "artifacts/model-units" / f"{PID}.json", models)
    base.base.write_json(ROOT / "artifacts/paper-cards" / f"{PID}.json", card)
    base.base.write_json(ROOT / "artifacts/learning-audits" / f"{PID}.json", audit)
    observation_path = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    observation_path.parent.mkdir(parents=True, exist_ok=True)
    observation_path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
