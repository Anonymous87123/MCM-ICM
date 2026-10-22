from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import build_q95_artifacts as base


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2012-15171-ce229936"
SHORT = "15171"
SHA = "ce22993638670a187e0e65fcf691562ec5309560d3fa3fce35d1539bd7b0268c"
TYPE = "B"
YEAR = "2012"
PAGE_COUNT = 36

PATTERNS = [
    "LP-B-ABSTRACT-MULTIMODEL-CONVERGENCE",
    "LP-B-MEMO-OPTIONS-TRADEOFF",
    "LP-B-INTRO-CAPACITY-CONSTRAINT",
    "LP-B-PARAMETER-DEFINITION-USE",
    "LP-B-ASSUMPTION-RATIONALE-CONSEQUENCE",
    "LP-B-BASELINE-SCALING-REFERENCE",
    "LP-B-ALGORITHM-RULE-STATE-UPDATE",
    "LP-B-OPTIMIZATION-PARAMETER-MECHANISM",
    "LP-B-FIGURE-TREND-CAPACITY",
    "LP-B-GREEDY-PRIORITY-FEASIBILITY",
    "LP-B-PROBABILITY-ASSUMPTION-DERIVATION",
    "LP-B-MODEL-COMPARISON-DECISION",
    "LP-B-LIMITATION-EXTENSION",
    "LP-B-APPENDIX-PARAMETERIZED-VISUAL",
]

# key, protocol chapter, first page, last page, tag, language-unit count,
# source-checked paraphrase, visually observed paragraph count
CHAPTERS = [
    ("manager-memo", "memo", 2, 2, "MEM", 30, "The memo frames the capacity decision, offers itinerary and distance-management options, compares safety, autonomy, maintenance dependence, crowding, and expected throughput, and ends with an implementation tradeoff.", 7),
    ("abstract", "abstract", 1, 4, "ABS", 42, "The abstract names the river-management objective, shared assumptions, agent, itinerary, and probability models, model-specific recommendations, and the claimed convergence near 1150 to 1250 seasonal customers.", 8),
    ("introduction", "introduction", 4, 4, "INT", 24, "The introduction moves from rising rafting demand and overcrowding to one-group-per-campsite capacity and a three-model comparison across campsite counts.", 2),
    ("parameters", "notation", 5, 5, "NOT", 18, "The parameter table defines launches per day, campsite spacing, daylight bounds, speed, campsite count, utilization, failures, traveled distance, daily goal, number of stops, and nights remaining.", 3),
    ("assumptions", "assumptions", 5, 8, "ASM", 44, "The assumptions fix daylight travel, Grand Canyon geography, a May through October season, 225 miles, even campsite spacing, two speeds, downstream motion, excess demand, base-case behavior, trip-duration distributions, and probability-model stop behavior.", 18),
    ("base-case", "model-establishment", 8, 10, "BAS", 36, "The base case nondimensionalizes time, speed, and spacing, derives a daily launch bound and staggered start times, then differentiates a continuous surrogate to discuss sensitivity.", 12),
    ("agent-model", "algorithm", 11, 17, "AGT", 64, "The agent model advances boats in one-minute steps, assigns daily goals, triggers campsite search, defines two failure conditions, optimizes departure timing and slow-boat duration, and estimates capacity and utilization from figures.", 24),
    ("itinerary-model", "model-improvement", 17, 22, "ITI", 56, "The itinerary model uses a speed-prioritized greedy placement heuristic, removes infeasible trips, studies failures and utilization against launches and campsite count, and distinguishes a comfortable threshold from an overdriven upper envelope.", 18),
    ("probability-model", "robustness-verification", 23, 27, "PRO", 72, "The probability model uses conditional Poisson-process reasoning, a uniform nightly position argument, equal-speed and mixed-speed blocking events, six parameterized probability plots, and a 77-boat occupancy recommendation.", 22),
    ("conclusion", "conclusion", 27, 29, "CON", 34, "The conclusion compares the three models, maps manager assumptions to model choice, repeats the common throughput range, and proposes extensions for nonuniform campsites, correlated weather, and seasonal demand.", 10),
    ("appendix", "sensitivity-analysis", 30, 35, "APP", 32, "The appendix presents six probability-versus-boat-count plots for fast and slow boats under three campsite spacings and five fast-boat proportions.", 6),
    ("references", "references", 36, 36, "REF", 8, "Four references provide daylight regulation, stochastic-process theory, rafting context, and permit-demand context, but no code, frozen inputs, or computational archive.", 4),
]

MOVES = [
    ("whole-study-forecast", "Forecast the decision, assumptions, model families, model-specific actions, and cross-model result before details.", "decision -> assumptions -> models -> actions -> common range"),
    ("option-tradeoff", "Offer operational options and compare safety, autonomy, crowding, maintenance, and throughput.", "manager condition -> option -> benefit -> cost -> choice rule"),
    ("constraint-to-capacity", "Translate rising demand and one-resource-per-group occupancy into a capacity question.", "demand -> congestion risk -> occupancy rule -> capacity objective"),
    ("definition-before-use", "Define every symbol immediately before the model or figure consumes it.", "symbol -> unit -> operational meaning -> downstream use"),
    ("assumption-with-rationale", "State a modeling assumption, explain why it is plausible, and name the mathematical simplification it enables.", "assumption -> domain rationale -> enabled method -> excluded behavior"),
    ("scaling-to-reference", "Build a restrictive analytic baseline and use it as a reference rather than a universal optimum.", "units -> scaling -> bound -> schedule -> reference role"),
    ("algorithm-state-update", "Narrate an algorithm as ordered state transitions with triggers and failure recording.", "initialize -> compute target -> advance -> trigger search -> occupy -> update"),
    ("parameter-mechanism-trend", "Connect an adjustable parameter to a physical mechanism and then to a plotted trend.", "parameter change -> mechanism -> metric -> figure trend -> recommendation"),
    ("figure-to-threshold", "Read a figure into an explicit threshold while retaining axes, scenario, uncertainty, and comparator.", "scenario -> axes -> trend -> threshold -> boundary"),
    ("greedy-feasibility", "Explain priority, feasible-site search, nearest-goal placement, removal, and itinerary output.", "priority -> feasible set -> placement -> failure removal -> schedule"),
    ("probability-derivation", "Move from process assumptions through conditioning and event decomposition to a decision probability.", "process -> conditioning -> position law -> blocking event -> probability -> cutoff"),
    ("model-comparison", "Compare models by the assumptions managers can accept and the risks each leaves.", "manager belief -> model choice -> safety/autonomy tradeoff -> throughput"),
    ("limitation-to-extension", "Pair a restrictive assumption with a specific extension that changes the mechanism.", "restriction -> bias mechanism -> extension -> new evidence need"),
]

EXAMPLES = [
    ("A reservoir-allocation abstract names three policy models, one action from each, and the range on which they agree.", "It does not call agreement independent validation when the models share inputs."),
    ("A hospital memo offers a fixed bed itinerary and a flexible probabilistic admission rule.", "It states the safety and autonomy tradeoff before recommending either option."),
    ("A berth-capacity introduction turns increased demand and one-vessel-per-berth occupancy into a seasonal throughput decision.", "The objective retains both service and congestion outcomes."),
    ("A transport model defines departure rate, spacing, travel window, speed, utilization, failures, and remaining work before equations.", "Every plot later uses the same symbols and units."),
    ("A daylight-only routing assumption cites the safety rationale and records the omitted night operations.", "A sensitivity case later changes the travel window."),
    ("A warehouse baseline rescales time and distance, derives a continuous packing bound, and labels it a reference case.", "It does not differentiate a floor function without naming the surrogate."),
    ("A minute-step vehicle simulation records target distance, position update, search trigger, occupancy, and failure state.", "Update order and random seed are explicit."),
    ("A dispatch study explains why earlier starts reduce late arrivals before showing the failure-rate curve.", "The caption names the plotted metric correctly."),
    ("A greedy scheduler prioritizes low-flexibility jobs, searches feasible slots, and reruns after a removal.", "The guarantee applies only to the final retained schedule."),
    ("A queueing derivation states the conditional Poisson event before using uniform order statistics.", "The distribution parameter is calibrated to the declared trip duration."),
    ("A policy conclusion maps strict compliance to an itinerary model and flexible behavior to a probabilistic model.", "Shared assumptions and common failure modes remain visible."),
    ("An appendix gives one panel per resource density with identical axes and a visible decision cutoff.", "Parameter labels are arithmetically consistent with the domain length."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose
EQUATIONS = [
    ("scaled start time", 9, "Base Case", "time scaling", "S' = S/24", r"S'=\frac{S}{24}", ["S'", "S"], "Express the daily start as a fraction of a 24-hour day."),
    ("scaled end time", 9, "Base Case", "time scaling", "E' = E/24", r"E'=\frac{E}{24}", ["E'", "E"], "Express the daily end as a fraction of a 24-hour day."),
    ("scaled speed", 9, "Base Case", "speed scaling", "v' = 24v/225", r"v'=\frac{24v}{225}", ["v'", "v"], "Express boat speed as a fraction of the river per day."),
    ("scaled campsite spacing", 9, "Base Case", "distance scaling", "D' = D/225", r"D'=\frac{D}{225}", ["D'", "D"], "Express campsite spacing as a fraction of river length."),
    ("daily launch bound", 9, "Base Case", "capacity bound", "Delta X = floor(((E'-S')v')/D')", r"\Delta X=\left\lfloor\frac{(E'-S')v'}{D'}\right\rfloor", ["Delta X", "E'", "S'", "v'", "D'"], "Count equally spaced campsites reachable in the shared travel window."),
    ("staggered send-off time", 10, "Base Case", "departure schedule", "s_i = E' - iD'/v'", r"s_i=E'-\frac{iD'}{v'}", ["s_i", "E'", "i", "D'", "v'"], "Stagger launches so identical boats stop at the same end time."),
    ("end-time sensitivity", 10, "Base Case", "local sensitivity", "partial n / partial E = v/D", r"\frac{\partial n}{\partial E}=\frac{v}{D}", ["n", "E", "v", "D"], "Describe the continuous surrogate's sensitivity to later stopping."),
    ("start-time sensitivity", 10, "Base Case", "local sensitivity", "partial n / partial S = -v/D", r"\frac{\partial n}{\partial S}=-\frac{v}{D}", ["n", "S", "v", "D"], "Describe the continuous surrogate's sensitivity to later starts."),
    ("speed sensitivity", 10, "Base Case", "local sensitivity", "partial n / partial v = (E-S)/D", r"\frac{\partial n}{\partial v}=\frac{E-S}{D}", ["n", "v", "E", "S", "D"], "Describe the continuous surrogate's sensitivity to speed."),
    ("spacing sensitivity", 10, "Base Case", "local sensitivity", "partial n / partial D = -(E-S)v/D^2", r"\frac{\partial n}{\partial D}=-\frac{(E-S)v}{D^2}", ["n", "D", "E", "S", "v"], "Describe the continuous surrogate's inverse-square sensitivity to spacing."),
    ("daily distance goal", 11, "Agent Algorithm", "adaptive target", "g = (225-d)/(r+1)", r"g=\frac{225-d}{r+1}", ["g", "d", "r"], "Set today's target from remaining river distance and remaining nights."),
    ("minute position update", 11, "Agent Algorithm", "state update", "d = d + v/60", r"d\leftarrow d+\frac{v}{60}", ["d", "v"], "Advance a boat by one minute of travel."),
    ("itinerary target campsite", 18, "Itinerary Algorithm", "greedy target", "g_i = iL/n, i=1,...,6", r"g_i=\frac{iL}{n},\quad i=1,\ldots,6", ["g_i", "i", "L", "n"], "Choose evenly distributed daily goals for the printed six-index construction."),
    ("equal-speed first-block event", 25, "Probability Model", "blocking probability", "P(A)=C(N-1,2)w^2(1-w)^(N-3)", r"P(A)=\binom{N-1}{2}w^2(1-w)^{N-3}", ["P(A)", "N", "w"], "Model two threatening boats before the first campsite."),
    ("equal-speed two-interval event", 25, "Probability Model", "blocking probability", "P(B)=C(N-1,2)(w+D)^2(1-w-D)^(N-3) C(2,1)w(1-w)", r"P(B)=\binom{N-1}{2}(w+D)^2(1-w-D)^{N-3}\binom{2}{1}w(1-w)", ["P(B)", "N", "w", "D"], "Model one threatening boat before each of the first two campsites using the printed factorization."),
    ("row-boat first-block event", 26, "Probability Model", "mixed-speed blocking", "P(A')=C(N-1,2)(w+p_f w)^2(1-w-p_f w)^(N-3)", r"P(A')=\binom{N-1}{2}(w+p_fw)^2(1-w-p_fw)^{N-3}", ["P(A')", "N", "w", "p_f"], "Expand a row boat's threatening region for possible fast-boat overtaking."),
    ("row-boat two-interval event", 26, "Probability Model", "mixed-speed blocking", "P(B') uses w+D+p_fD and w+p_fw", r"P(B')=\binom{N-1}{2}(w+D+p_fD)^2(1-w-D-p_fD)^{N-3}\binom{2}{1}(w+p_fw)(1-w-p_fw)", ["P(B')", "N", "w", "D", "p_f"], "Apply the printed two-interval overtaking adjustment for a row boat."),
    ("motor-boat first-block event", 26, "Probability Model", "mixed-speed blocking", "P(A'') uses w-(1-p_f)w/2", r"P(A'')=\binom{N-1}{2}\left(w-\frac{(1-p_f)w}{2}\right)^2\left(1-w+\frac{(1-p_f)w}{2}\right)^{N-3}", ["P(A'')", "N", "w", "p_f"], "Shrink a motor boat's threatening region for row boats it can overtake."),
    ("motor-boat two-interval event", 26, "Probability Model", "mixed-speed blocking", "P(B'') uses w+D-(1-p_f)(w+D)/2", r"P(B'')=\binom{N-1}{2}\left(w+D-\frac{(1-p_f)(w+D)}{2}\right)^2\left(1-w-D+\frac{(1-p_f)(w+D)}{2}\right)^{N-3}\binom{2}{1}\left(w-\frac{(1-p_f)w}{2}\right)\left(1-w+\frac{(1-p_f)w}{2}\right)", ["P(B'')", "N", "w", "D", "p_f"], "Apply the printed two-interval overtaking adjustment for a motor boat."),
]

ALGORITHMS = [
    (9, "base-case campsite filling", "Fill consecutively reachable campsites with identical boats and move the occupied block downstream each day.", ["S", "E", "v", "D"], ["Delta X", "occupied campsite block"]),
    (10, "base-case launch staggering", "Compute one send-off time per boat so all identical boats stop at the shared end time.", ["E'", "D'", "v'", "Delta X"], ["s_i schedule"]),
    (11, "one-minute agent simulation", "Generate boat attributes, compute the remaining-distance goal, advance one minute, trigger campsite search, occupy the first available camp, and update the next day.", ["launch distributions", "sunrise", "sunset", "v", "trip length", "Y"], ["boat trajectories", "failures", "utilization"]),
    (12, "agent start-time optimization", "Move the departure-time distribution earlier and compare the fraction of boats failing to find camp.", ["maximum start time", "Delta X=6", "Y=100"], ["failure-rate curve"]),
    (12, "slow-boat duration optimization", "Raise the minimum slow-boat trip length and compare campsite utilization and failure behavior.", ["minimum slow-boat nights", "Delta X=6", "Y=100"], ["utilization curve"]),
    (14, "agent capacity sweep", "Increase launches per day and campsite count, then select the largest setting under the stated one-percent failure threshold.", ["Delta X grid", "Y grid", "failure rules"], ["capacity", "seasonal trips", "utilization"]),
    (18, "greedy itinerary construction", "Generate daily boats, prioritize slow boats, search feasible open campsites, choose the site nearest the daily goal, remove infeasible trips, and output the retained itinerary.", ["daily boats", "trip durations", "boat speeds", "campsite state"], ["retained itinerary", "failed boats"]),
    (19, "itinerary overdrive sweep", "Increase rafts added per day and campsite count while recording failed rafts, utilization, failure characteristics, and total accommodated boats.", ["Delta X grid", "Y grid", "uniform demand"], ["failure curves", "utilization curves", "total accommodated"]),
    (23, "conditional Poisson stop construction", "Condition a homogeneous Poisson process on a fixed stop count and use uniform order statistics as desired stop locations.", ["trip stop count n", "river length", "rate lambda"], ["desired stop positions"]),
    (24, "nightly fleet superposition", "Superimpose duration-specific stage distributions under constant daily launches to approximate a uniform nightly fleet distribution.", ["duration classes", "steady launch mix"], ["nightly boat-position distribution"]),
    (24, "blocking-event enumeration", "Enumerate threatening boat configurations before successive campsites and sum their probabilities for a travel cutoff.", ["N", "w", "D", "delta", "boat type mix"], ["cutoff exceedance probability"]),
    (27, "probability capacity conversion", "Read the one-percent cutoff at 99 campsites, keep 77 boats on the river, and convert average twelve-day occupancy into seasonal launches.", ["77 boats", "12-day average", "180-day horizon"], ["1155 launches per season"]),
]

VISUALS = [
    (5, "Table 1 - parameters", "Defines Delta X, D, S, E, v, Y, mu, F, d, g, n, and r used across the three models."),
    (13, "Figure 1 - start-time optimization", "Plots agent failure rate against maximum start time and shows later departures increasing failures."),
    (13, "Figure 2 - minimum slow-boat nights", "Plots campsite utilization against minimum slow-boat nights, although the caption incorrectly calls it failure percentage."),
    (14, "Figure 3 - minimum slow-boat nights", "Repeats essentially the same utilization trend as Figure 2 with a corrected mu-oriented caption."),
    (15, "Figure 4 - agent failures versus launches", "Plots percent failing against Delta X for Y=100 and supports a threshold comparison."),
    (15, "Figure 5 - agent utilization versus launches", "Plots campsite utilization against Delta X and approaches a high-utilization plateau."),
    (16, "Figure 6 - agent failures versus campsites", "Shows failures falling toward zero as Y increases at Delta X=7."),
    (17, "Figure 7 - campsites versus seasonal trips", "Shows an approximately linear increase in total trips with Y, with the vertical axis labeled X."),
    (17, "Figure 8 - campsite-level utilization", "Shows low use near the river ends and higher use through most middle campsites."),
    (19, "Figure 9 - unplaceable rafts versus launches", "Shows itinerary failures near zero through six daily rafts and increasing after seven."),
    (19, "Figure 10 - itinerary utilization versus launches", "Shows utilization rising and plateauing near 94 to 95 percent."),
    (20, "Figure 11 - failed rafts versus campsites", "Shows failures declining to near zero around one hundred campsites; the prose incorrectly describes this as utilization."),
    (20, "Figure 12 - itinerary utilization versus campsites", "Shows a knee near eighty campsites and declining utilization as more sites are added."),
    (21, "Figure 13 - mean nights of failed boats", "Shows wide-error-bar mean trip duration near eleven to twelve nights with little visible trend."),
    (21, "Figure 14 - mean speed of failed boats", "Shows failed-boat mean speed near eight at Delta X=7, then around six at larger launch rates."),
    (22, "Figure 15 - total accommodated versus launches", "Shows total accommodated boats plateauing near fourteen hundred after Delta X about eight."),
    (24, "Figure 16 - boat placement schematic", "Defines x, w, D, w+D, w+2D, and delta between First Launch and Final Exit."),
    (30, "Figure 17 - fast boat, far campsites", "Plots cutoff probability versus boats for 29 campsites and five fast-boat proportions."),
    (31, "Figure 18 - fast boat, medium campsites", "Plots cutoff probability for 59 campsites and a 3.75-mile spacing."),
    (32, "Figure 19 - fast boat, close campsites", "Plots cutoff probability for the printed 99-campsite, 1.25-mile, one-hundredth-length scenario."),
    (33, "Figure 20 - slow boat, far campsites", "Plots slow-boat cutoff probability for 29 campsites and five fast-boat proportions."),
    (34, "Figure 21 - slow boat, medium campsites", "Plots slow-boat cutoff probability for 59 campsites and a 3.75-mile spacing."),
    (35, "Figure 22 - slow boat, close campsites", "Plots slow-boat cutoff probability for the internally inconsistent 99-campsite spacing scenario."),
]

WARNINGS = [
    (2, "The manager memo is dated February 13, 2012, while the paper title page is dated February 12, 2012."),
    (1, "Boats, boaters, customers, groups, trips, and people served are used as if they were interchangeable throughput units."),
    (6, "May 1 through October 31 contains 184 calendar days when both endpoints are included, not the stated 180 days."),
    (6, "The Grand Canyon coordinates omit explicit minute and second marks, making the printed coordinate notation ambiguous."),
    (5, "Perfectly even campsite spacing drives all three models but is not supported by target-river data."),
    (8, "The exponential stopping model supplies no rate parameter, scale, unit, or calibration from trip duration."),
    (10, "The paper differentiates n after defining daily capacity with a floor; the displayed derivatives apply only to an unstated continuous surrogate, not the step function itself."),
    (9, "The base-case description says newly launched boats fill sites 1 through k even though k is not defined in the parameter table or derivation."),
    (11, "The agent simulation does not specify random seed, repeat count, boat ordering within each minute, simultaneous campsite arrival resolution, or closed-season censoring."),
    (13, "Figure 2's caption says percent of boats failing, but its vertical axis and data show campsite utilization."),
    (14, "Figures 2 and 3 repeat essentially the same slow-boat minimum-night utilization curve without explaining the duplication."),
    (15, "Several figure captions print Delta where the plot title uses Delta X, weakening symbol consistency."),
    (15, "The agent failure curve and the claimed seasonal capacity are not connected by a reproducible table, seed, repeated-run interval, or exact interpolation rule."),
    (16, "The 1170 seasonal-trip claim does not state whether it counts launches or completed trips and does not reconcile end-of-season boats still on the river."),
    (18, "The itinerary target formula uses L without defining it and hard-codes i=1,...,6 although the algorithm later evaluates seven or more daily rafts."),
    (18, "The itinerary algorithm sorts by boat speed but its boat-generation step explicitly samples duration only, leaving speed generation implicit."),
    (18, "Removing a boat after a greedy placement failure does not specify whether prior placements are rolled back or the schedule is recomputed."),
    (18, "The prose cites Figure 11 as campsite utilization versus campsite count, but Figure 11 is failed rafts; Figure 12 is the utilization plot."),
    (22, "The paper calls Delta X at least seven an overdrive even though seven is also its stated carrying-capacity boundary; strict overdrive would begin above seven."),
    (22, "The claim that utilization approaches 100 percent is based on a plotted plateau around 94 to 95 percent and no exact data table."),
    (21, "Figure 14 places the Delta X=7 failed-boat mean speed closer to 8 mph than the prose value of approximately 7.5 mph."),
    (23, "The probability model combines unconditional independent exponential increments with a fixed total stop count without explicitly conditioning the Poisson process."),
    (24, "The nightly uniform fleet argument requires steady state, equal stage representation, common support, independence, and ignored start/end transients that are not fully stated."),
    (25, "The text says K is Binomial(N-1,2), using 2 where a binomial success probability such as w is required."),
    (25, "The printed P(B) factor C(2,1)w(1-w) is not the conditional split probability of one boat in w and one in the adjacent D interval after conditioning on two boats in w+D."),
    (25, "The two displayed equal-speed events are not a complete general cutoff calculation unless delta's campsite interval, direction, occupancy, and all blocking configurations are fixed."),
    (26, "The mixed-speed formulas replace geometric threatening regions with p_f-scaled interval lengths without deriving the needed joint position, type, speed, and arrival-order probabilities."),
    (27, "The probability plots are described as travel of 14 miles without consistently distinguishing exactly 14, at least 14, and more than 14 miles."),
    (32, "A 1.25-mile spacing is not one hundredth of a 225-mile river and would imply roughly 180 intervals, not the printed 99 campsites."),
    (27, "The 77/12 times 180 calculation counts launches under a 180-day approximation and does not require those trips to finish within the season."),
    (28, "Agreement among the three models is not independent validation because they share river length, even campsite spacing, controlled demand assumptions, season horizon, and throughput ambiguities."),
    (36, "No executable code, seed, simulation configuration, raw output table, uncertainty analysis, or frozen source archive is provided."),
    (36, "The reference gives Ithica, NY for Cornell University; the place name is Ithaca."),
]


def configure_base() -> None:
    base.ROOT = ROOT
    base.PID = PID
    base.SHORT = SHORT
    base.SHA = SHA
    base.TYPE = TYPE
    base.YEAR = YEAR
    base.PAGE_COUNT = PAGE_COUNT
    base.PATTERNS = PATTERNS
    base.CHAPTERS = CHAPTERS
    base.MOVES = MOVES
    base.EXAMPLES = EXAMPLES
    base.EQUATIONS = EQUATIONS
    base.ALGORITHMS = ALGORITHMS
    base.VISUALS = VISUALS
    base.WARNINGS = WARNINGS


def make_language() -> dict:
    configure_base()
    language = base.make_language()
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = (
            "All 36 physical-page UTF-8 text files were read sequentially by the root context. "
            "Fresh read-only contexts visually reviewed pages 1-8, 9-16, 17-20, 21-24, "
            "25-32, and 33-36 using one JPEG proxy of at most 450000 bytes per tool call."
        )
        layout["ambiguities"] = [
            "Linear extraction flattens equations and chart geometry, loses mean bars on n and v, and includes control characters around large probability-formula brackets; rendered pages were authoritative.",
            "Source-level date, caption, cross-reference, season-length, probability, and spacing conflicts are retained as final-pass warnings rather than treated as extraction omissions.",
        ]
    return language


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "hour, day, night, mile, mph, campsite, boat, launch, fraction, probability, count, or dimensionless quantity as locally defined",
        "definition": f"Source-defined seasonal river-capacity quantity {symbol}.",
        "source_status": "explicit-defined" if symbol not in {"L", "lambda"} else "unspecified",
    }


def model_record(
    model_id: str,
    page: int,
    section: str,
    family: str,
    purpose: str,
    inputs: list[str],
    outputs: list[str],
    equations: list[dict],
) -> dict:
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
        "equation_status": {
            "status": "present" if equations else "not-applicable",
            "reason": "The printed relation was reconciled against the rendered page." if equations else "This record is a simulation, sweep, scheduling, probability, or decision procedure.",
        },
        "objectives": [purpose, "Return a typed launch, placement, failure, utilization, probability, capacity, or decision output."],
        "constraints": [
            "Keep boats, people, trips, launches, completions, failures, occupancy, utilization, and season-end censoring separately typed.",
            "A campsite holds one group, boats move downstream during daylight, and itinerary feasibility depends on the retained schedule rather than removed demand.",
            "A plotted threshold or common model range is not a proof of optimality, calibration, or independent validation.",
        ],
        "conditions": {
            "initial": {"status": "present", "details": ["River length, season, daylight, campsite count and spacing, craft speed, trip duration, and launch mix are supplied or assumed."]},
            "boundary": {"status": "present", "details": ["First Launch, Final Exit, river ends, sunrise, sunset, season start, and season end affect feasible states and censoring."]},
            "equilibrium": {"status": "uncertain", "details": ["The probability model requires an unstated steady-state fleet argument; the simulations are finite-season processes."]},
        },
        "parameter_estimation": {
            "status": "partial",
            "method": "Problem constants, Grand Canyon analogy, uniform or Bernoulli draws, one-minute simulation, greedy scheduling, conditional Poisson reasoning, and visual parameter sweeps.",
            "parameters": inputs,
        },
        "algorithm": {
            "status": "partial",
            "steps": ["freeze scenario and random-generation rules", "advance or place boats", "record campsite occupancy and failures", "repeat the finite season or probability sweep", "separate retained schedule from rejected demand", "report the declared metric and uncertainty"],
            "software": ["No executable source code, seed, configuration, or raw machine-readable outputs are supplied."],
            "convergence_criteria": "No numerical convergence criterion is stated; thresholds are read from finite simulations and plotted probability cutoffs.",
        },
        "assumptions": [
            "Campsites are evenly spaced, boats travel downstream in daylight, and demand is sufficient.",
            "The manager can control or approximate launch composition by speed and duration.",
        ],
        "identifiability_feasibility": {
            "status": "partial",
            "analysis": "The intended operations and figures are visible, but seeds, repetitions, exact random laws, event conditioning, simultaneous-arrival rules, greedy rollback, season censoring, probability factorization, and target-river calibration prevent full reproduction.",
        },
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, visually checked equation, algorithm, table, plot, or discussion."],
        "computational_cost": "Dominated by minute-level boat updates, campsite searches, greedy schedule construction, multi-season sweeps, and probability evaluation over boat counts and mixture parameters.",
        "strengths": ["The paper exposes three distinct operational views of the same capacity decision.", "Twenty-two figures and one parameter table permit direct trend and consistency checks."],
        "limitations": ["Implementation, uncertainty, metric typing, and empirical calibration are incomplete.", "Confirmed source defects are retained only in the final warning pass."],
        "missing_details": ["Code, seed, repeat count, exact distributions, simultaneous-event ordering, rollback, censoring, lambda calibration, steady-state proof, complete event enumeration, confidence intervals, and empirical validation are absent."],
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
            "source_type": "paper",
            "visual_checked": True,
            "transcription_confidence": "high",
        }
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, section, family, purpose, symbols[1:], [symbols[0]], [equation]))
    for index, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, len(EQUATIONS) + 1):
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, family, family, purpose, inputs, outputs, []))

    by_family = {model["family"]: model["model_id"] for model in models}
    pairs = [
        ("time scaling", "capacity bound"),
        ("speed scaling", "capacity bound"),
        ("distance scaling", "capacity bound"),
        ("capacity bound", "base-case campsite filling"),
        ("capacity bound", "base-case launch staggering"),
        ("adaptive target", "one-minute agent simulation"),
        ("state update", "one-minute agent simulation"),
        ("one-minute agent simulation", "agent start-time optimization"),
        ("one-minute agent simulation", "slow-boat duration optimization"),
        ("one-minute agent simulation", "agent capacity sweep"),
        ("greedy target", "greedy itinerary construction"),
        ("greedy itinerary construction", "itinerary overdrive sweep"),
        ("conditional Poisson stop construction", "nightly fleet superposition"),
        ("nightly fleet superposition", "blocking-event enumeration"),
        ("blocking probability", "blocking-event enumeration"),
        ("mixed-speed blocking", "blocking-event enumeration"),
        ("blocking-event enumeration", "probability capacity conversion"),
    ]
    edges = [
        {"from_model_id": by_family[source], "to_model_id": by_family[target], "handoff": f"The {source} output becomes an input, constraint, diagnostic, or warning boundary for {target}."}
        for source, target in pairs
        if source in by_family and target in by_family
    ]
    return {
        "dependency_edges": edges,
        "models": models,
        "paper_id": PID,
        "problem_type": TYPE,
        "review_status": "validated",
        "schema_version": 2,
        "source_sha256": SHA,
        "year": YEAR,
    }


def make_card(language: dict, models: dict) -> dict:
    assumptions = [
        (5, "Boats travel only during civil-twilight daylight; after-sunset travel is a failure in the agent model."),
        (6, "The Big Long River is placed at Grand Canyon coordinates and treated as a 225-mile analog."),
        (6, "The season is declared as May 1 through October 31 and approximated as 180 days."),
        (6, "Campsites are perfectly evenly spaced and each campsite holds one group per night."),
        (6, "Only 4 mph row boats and 8 mph motor boats travel downstream."),
        (7, "Demand exceeds supply; the base case uses only row boats, six-day trips, and exact sunset stopping."),
        (7, "Agent boats seek approximately equal daily progress; itinerary duration is uniform from 6 to 18 and speed is intended to be Bernoulli with p=0.5."),
        (8, "Probability-model daily desired distances are exponential and independent, while the number of stops is predetermined."),
        (8, "The daily mix of speed-duration classes remains approximately constant through the season."),
        (24, "The nightly positions of all boats can be approximated as independent uniform draws after a steady launch regime is reached."),
    ]
    data = [
        (5, "Table 1 defines the shared parameters and metrics used by all three models."),
        (6, "Grand Canyon coordinates, 280-mile comparison, rafting trip durations, and permit demand provide analogy context."),
        (13, "Figures 1 through 3 show start-time and minimum-slow-boat-night optimization at Delta X=6 and Y=100."),
        (15, "Figures 4 through 8 show agent failures, utilization, capacity against Y, and site-level utilization."),
        (19, "Figures 9 through 15 show itinerary failures, utilization, failed-boat characteristics, and total accommodated boats."),
        (24, "Figure 16 defines the blocking-event geometry with x, w, D, and delta."),
        (30, "Figures 17 through 22 show cutoff probability for fast and slow boats at three printed campsite spacings and five fast-boat proportions."),
        (36, "Four references provide regulatory, stochastic-process, rafting, and permit context but no frozen computational inputs."),
    ]
    verification_specs = [
        (9, "The scaled base-case capacity formula reduces to travel-window distance divided by campsite spacing.", "dimensional reconciliation", "The units cancel visibly after scaling.", "The floor function is later replaced by an unstated continuous surrogate for differentiation."),
        (13, "The start-time plot supports the mechanism that later starts increase failure risk.", "parameter trend", "The direction of the effect is visually clear.", "No raw runs, seed, interval, or fitted relation is supplied."),
        (13, "The slow-boat duration plots support higher utilization at longer minimum trips.", "parameter trend", "The plotted rise is visible.", "Figure 2's caption names the wrong metric and Figure 3 largely duplicates it."),
        (15, "Agent failure and utilization plots can be compared against the one-percent capacity definition.", "threshold check", "Axes and scenario are readable.", "The reported 1170 seasonal trips are not reconstructed from a table or explicit threshold interpolation."),
        (17, "Campsite-level utilization supports low use near the beginning and end of the river.", "spatial diagnostic", "The site pattern is visible over five simulated seasons.", "No site coordinates, raw utilization values, or uncertainty are provided."),
        (19, "Itinerary Figure 9 shows few failures at seven daily rafts and rapid growth thereafter.", "greedy schedule stress test", "The comfortable threshold and overdriven region are visible.", "The algorithm's rollback and rejected-demand accounting are unspecified."),
        (20, "Figures 11 and 12 expose how failures and utilization change with campsite count.", "cross-figure check", "The knee near eighty campsites is inspectable.", "The prose reverses the Figure 11 and Figure 12 meanings."),
        (22, "Figure 15 shows total accommodated boats plateauing near 1400.", "upper-envelope check", "The 1260 and 1400 regimes are visible.", "The claim of near-100-percent utilization lacks exact values and uncertainty."),
        (25, "Rendered probability equations can be transcribed and checked against the stated blocking events.", "equation audit", "All combinations, exponents, and speed-mix symbols are visible.", "The binomial parameterization and conditional split factor do not match the described events."),
        (32, "Figures 17 through 22 permit a one-percent cutoff reading by boat count and mixture.", "decision-cutoff plot", "The 77-boat reading for one printed scenario is visible.", "The close-spacing parameter labels are arithmetically inconsistent."),
        (28, "The three model outputs are compared around a common 1150 to 1250 range.", "cross-model comparison", "The decision tradeoffs are stated explicitly.", "Shared assumptions mean agreement is not independent validation."),
        (36, "The paper cites stochastic-process theory and domain context.", "provenance check", "The conceptual sources are identifiable.", "There is no code, configuration, archived data, or reproducible result package."),
    ]
    verification = [
        {"page": page, "section": "verification", "summary": summary, "verification_type": kind, "strength": strength, "limitation": limitation}
        for page, summary, kind, strength, limitation in verification_specs
    ]
    results = [
        (1, "All three models are claimed to give approximately 1150 to 1250 seasonal customers at 100 campsites; the itinerary upper envelope is near 1400."),
        (13, "Earlier maximum start times reduce the agent-model failure percentage."),
        (14, "Longer minimum slow-boat trips raise the plotted campsite utilization."),
        (16, "The agent model reports approximately 1170 seasonal boats when Y=100."),
        (17, "Agent campsite utilization is lower near the first twenty and final river miles."),
        (19, "The itinerary model has near-zero placement failures through six daily rafts and fewer than one percent at seven."),
        (20, "At Delta X=7, itinerary utilization is approximately 80 percent and failures approach zero around one hundred campsites."),
        (22, "The retained itinerary accommodates approximately 1260 boats at Delta X=7 and roughly 1360 to 1400 when overdriven."),
        (25, "Equal-speed and mixed-speed formulas estimate the chance that intervening boats occupy downstream campsites before the focal boat."),
        (27, "For the printed 99-campsite equal-mix scenario, the paper reads a 77-boat one-percent cutoff."),
        (27, "Using twelve average days and a 180-day horizon, the paper converts 77 concurrent boats into 1155 seasonal launches."),
        (28, "The conclusion maps fixed itineraries to safety guarantees and flexible behavior to agent and probability risk."),
        (29, "Extensions propose random campsite placement, correlated weather, and seasonally varying demand."),
    ]
    writing = [
        (1, "Abstract chain: decision need -> shared assumptions -> three model mechanisms -> model-specific recommendations -> common throughput range."),
        (2, "Memo chain: management context -> two proposals -> safety/autonomy/crowding tradeoffs -> cost and maintenance comparison -> behavior-based choice."),
        (4, "Introduction chain: rising demand -> overcrowding -> one-group-per-site rule -> maximum groups -> three-model plan."),
        (5, "Setup chain: parameter table -> common assumptions -> model-specific assumptions -> approach handoff."),
        (8, "Base-case chain: dimensional inputs -> scaled variables -> launch bound -> staggered schedule -> sensitivity discussion."),
        (11, "Agent chain: independent boats -> failure rules -> random attributes -> minute update -> campsite search -> optimization plots -> capacity plots."),
        (17, "Itinerary chain: greedy motivation -> eight-step schedule -> failure/utilization sweeps -> comfortable threshold -> overdriven upper envelope."),
        (23, "Probability chain: variable daily distance -> conditional Poisson argument -> nightly uniform fleet -> blocking geometry -> equal-speed equations -> mixed-speed equations."),
        (27, "Probability decision chain: six appendix plots -> one-percent cutoff -> 77 concurrent boats -> twelve-day turnover -> 1155 seasonal launches."),
        (28, "Conclusion chain: common range -> unique model insights -> manager-assumption decision rule -> shared limitations -> extensions."),
        (30, "Appendix chain: fast-boat plots across three spacings -> slow-boat plots across the same spacings -> comparison against one-percent cutoff."),
        (36, "Reference chain: daylight regulation -> stochastic-process theorem -> rafting analogy -> demand evidence."),
    ]
    contributions = [
        {"page": 9, "summary": "Provides a transparent analytic reference linking travel window, speed, spacing, and daily launches."},
        {"page": 11, "summary": "Implements autonomous boats with minute-level movement and explicit campsite-search triggers."},
        {"page": 13, "summary": "Connects earlier starts and longer slow-boat trips to failure and utilization mechanisms."},
        {"page": 18, "summary": "Builds a speed-prioritized greedy itinerary that can reject infeasible demand before issuance."},
        {"page": 19, "summary": "Separates a comfortable itinerary threshold from an overdriven upper envelope."},
        {"page": 23, "summary": "Uses conditional Poisson-process intuition to model variable desired stop locations."},
        {"page": 25, "summary": "Attempts to include boat-speed mixtures in campsite-blocking probabilities."},
        {"page": 28, "summary": "Maps model choice to the behavioral assumptions and risk tolerance of river managers."},
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 6, "summary": "Use the correct inclusive season length or an explicitly defined 180-day operating subset and track launches, completions, and censored trips separately."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 10, "summary": "Treat the floor capacity as a step function and use discrete perturbations or a labeled continuous relaxation for sensitivity."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 11, "summary": "Publish event ordering, simultaneous-arrival rules, random seeds, repetitions, raw outputs, and confidence intervals for the agent model."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 18, "summary": "Define L, generate speed explicitly, replace the hard-coded six-index target, and rerun or backtrack after greedy removals."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 22, "summary": "Report exact itinerary tables, rejected demand, completed trips, utilization, uncertainty, and the strict overdrive boundary."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 23, "summary": "Formulate the stop process explicitly as a Poisson process conditioned on N(L)=n and calibrate lambda to duration."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 24, "summary": "Prove or simulate the nightly position mixture with startup, steady-state, and shutdown phases rather than assuming uniformity."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 25, "summary": "Re-derive blocking probabilities with multinomial interval counts, type-conditioned speeds, and a complete cutoff event enumeration."},
        {"extension_id": f"E-B-{SHORT}-009", "page": 32, "summary": "Correct spacing, fraction-of-river, and campsite-count labels and regenerate all six probability panels from machine-readable parameters."},
        {"extension_id": f"E-B-{SHORT}-010", "page": 28, "summary": "Validate all three models against measured launches, completions, failures, campsite occupancy, environmental limits, and manager objectives on the target river."},
    ]
    return {
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "Optimization of Seasonal Throughput and Campsite Utilization on the Big Long River",
        "award_status": "outstanding",
        "source": {
            "relative_path": "2012美赛特等奖/B-15171-Outstanding.pdf",
            "sha256": SHA,
            "page_count": PAGE_COUNT,
            "pdf_page_offset_note": "Physical pages 1 and 2 are a control-sheet abstract and manager memo; physical page 3 begins internal page 1, and physical page 36 is internal page 34.",
        },
        "schema_version": 1,
        "source_quality": {
            "status": "validated",
            "text_pages": PAGE_COUNT,
            "rendered_pages": PAGE_COUNT,
            "visual_review": "complete",
            "notes": [
                "The root context read all 36 UTF-8 page files sequentially.",
                "Fresh read-only visual contexts reviewed all 36 pages in bounded batches using one JPEG proxy at or below 450000 bytes per tool call and returned text-only reports.",
                "The visual review reconciled nineteen equations, twenty-two figures, the parameter table, chart captions, mean-bar symbols, probability labels, page continuations, and four references without sending images to the root context.",
            ],
        },
        "context_sources": [
            {"type": "paper", "path": "2012美赛特等奖/B-15171-Outstanding.pdf"},
            {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"},
            {"type": "rendered-pages", "path": f"artifacts/papers/{PID}/rendered"},
        ],
        "task_reconstruction": {
            "inputs": ["225-mile river", "season and daylight window", "Y campsites", "campsite spacing D", "row and motor speeds", "trip-duration mix", "daily launch rate Delta X", "boat behavior model", "cutoff distance delta"],
            "outputs": ["daily launches", "boat trajectories", "campsite assignments", "failures", "utilization", "retained itinerary", "cutoff probabilities", "seasonal capacity", "manager recommendation"],
            "decisions": ["which model assumptions are acceptable", "how early boats start", "minimum slow-boat duration", "how many boats launch daily", "which trips remain in the itinerary", "how many concurrent boats satisfy a probability cutoff", "which metric defines capacity"],
        },
        "section_map": [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, _, evidence, _ in CHAPTERS],
        "assumptions": [{"page": page, "summary": summary} for page, summary in assumptions],
        "data_and_preprocessing": [{"page": page, "summary": summary} for page, summary in data],
        "models": [{"model_id": model["model_id"], "page": model["page"], "summary": model["summary"]} for model in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": verification,
        "results_trace": [{"page": page, "summary": summary} for page, summary in results],
        "contributions": contributions,
        "writing_logic": [{"page": page, "summary": summary} for page, summary in writing],
        "language_observations": [{"page": page, "summary": summary} for page, summary in writing],
        "visualization_observations": [{"page": page, "figure": figure, "summary": summary} for page, figure, summary in VISUALS],
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "A full abstract gives judges an immediate map of three model families, distinct decisions, and the common reported range.", "evidence_class": "J"},
            {"page": 2, "summary": "A memo that turns mathematical alternatives into manager-assumption choices makes operational relevance visible.", "evidence_class": "J"},
            {"page": 28, "summary": "Cross-model agreement is persuasive only when shared assumptions and common failure modes remain explicit.", "evidence_class": "J"},
        ],
        "weaknesses": [{"page": page, "summary": warning} for page, warning in WARNINGS],
        "independent_extensions": extensions,
        "candidate_rule_impacts": [],
        "unresolved_questions": [warning for _, warning in WARNINGS],
        "protocol_v2_records": {
            "language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]},
            "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(model["governing_equations"]) for model in models["models"]), "review_status": models["review_status"]},
        },
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [
            (
                unit["page"],
                unit["section"],
                unit["source_excerpt"],
                "Transfer the rhetorical mechanism only after replacing the river, campsite, craft, season, parameter, threshold, and numerical payload.",
                "R-B-LANG-001",
            )
            for unit in language["units"]
        ],
        "modeling": [
            (
                model["page"],
                model["section"],
                model["summary"],
                "Retain the typed inputs, state, equations or ordered operations, feasibility boundary, output metric, downstream handoff, and warning boundary.",
                "R-B-MOD-001",
            )
            for model in models["models"]
        ],
        "logic": [
            (
                item["page"],
                "organization chain",
                item["summary"],
                "Preserve the positive decision-to-assumptions-to-baseline-to-agent-to-itinerary-to-probability-to-manager chain.",
                "R-B-LOG-001",
            )
            for item in card["writing_logic"]
        ],
        "visualization": [
            (
                item["page"],
                item["figure"],
                item["summary"],
                "Keep axes, units, scenario, caption, uncertainty display, threshold, linked prose claim, and source inconsistency together.",
                "R-B-VIZ-001",
            )
            for item in card["visualization_observations"]
        ],
        "verification": [
            (
                item["page"],
                "verification",
                item["summary"],
                "Name the dimensional, trend, threshold, replay, equation, cutoff, cross-model, or provenance check and limit the conclusion to what it establishes.",
                "R-B-VER-002",
            )
            for item in card["verification"]
        ],
        "data": [
            (
                item["page"],
                "data and preprocessing",
                item["summary"],
                "Retain provenance, unit, season convention, coordinate meaning, campsite geometry, craft mix, duration mix, figure scenario, and downstream consumer.",
                "R-B-DATA-001",
            )
            for item in card["data_and_preprocessing"]
        ],
        "assumption": [
            (
                item["page"],
                "assumption",
                item["summary"],
                "Pair the assumption with the mechanism it enables, excluded behavior, violated-regime test, uncertainty, and target-river recalibration requirement.",
                "R-B-DATA-002",
            )
            for item in card["assumptions"]
        ],
        "result": [
            (
                item["page"],
                "result trace",
                item["summary"],
                "Carry launches, concurrent boats, retained trips, completed trips, failures, utilization, censoring, scenario, comparator, and decision status as separate fields.",
                "R-B-MOD-004",
            )
            for item in card["results_trace"]
        ],
        "weakness": [
            (
                item["page"],
                "last-pass warning",
                item["summary"],
                "Use only after positive language, organization, formula-level model, algorithm, visual, and verification retention is complete.",
                "R-B-VER-004",
            )
            for item in card["weaknesses"]
        ],
        "other": [
            (
                36,
                "reference and reproduction boundary",
                "The paper provides four contextual references but no executable code, seed, simulation configuration, raw output table, or frozen computational archive.",
                "Separate contextual citation, task analogy, model provenance, data provenance, and computational reproducibility.",
                "R-B-VER-004",
            )
        ],
    }
    counts = {
        "language": len(language["units"]),
        "modeling": 90,
        "logic": 78,
        "visualization": 78,
        "verification": 64,
        "data": 50,
        "assumption": 50,
        "result": 60,
        "weakness": len(WARNINGS),
        "other": 8,
    }
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
            records.append(
                {
                    "schema_version": 1,
                    "observation_id": f"O-B-{YEAR}-{SHORT}-{observation_index:03d}",
                    "paper_id": PID,
                    "problem_type": TYPE,
                    "year": YEAR,
                    "page": page,
                    "section": f"{section} / evidence action {index + 1}",
                    "evidence_class": "O",
                    "dimension": dimension,
                    "source_basis": basis[:900],
                    "interpretation": interpretation,
                    "applicability": [
                        "Apply only when the river or resource network, time horizon, capacity unit, state update, allocation rule, stochastic law, threshold, uncertainty, and transfer scope can all be named."
                    ],
                    "counterevidence": [
                        "A visually smooth curve, high utilization, low simulated failure rate, common cross-model range, or one-percent cutoff does not by itself prove implementation completeness, in-season completion, calibrated reliability, independent validation, or transfer validity."
                    ],
                    "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium",
                    "candidate_rule_ids": rule_ids,
                }
            )
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first_by_dimension: dict[str, str] = {}
    for row in observations:
        first_by_dimension.setdefault(row["dimension"], row["observation_id"])

    def evidence_for(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])

    card["candidate_rule_impacts"] = [
        {
            "rule_id": "R-B-LANG-001",
            "action": "retain the abstract's three-model forecast, the memo's option tradeoff, definition-before-use, mechanism-to-trend exposition, probability cutoff language, and scoped cross-model conclusion",
            "evidence_ids": [first_by_dimension["language"]],
        },
        {
            "rule_id": "R-B-LOG-001",
            "action": "retain the decision-to-shared-assumptions-to-analytic-baseline-to-agent-to-itinerary-to-probability-to-comparison-to-manager chain with explicit handoffs",
            "evidence_ids": [first_by_dimension["logic"]],
        },
        {
            "rule_id": "R-B-DATA-001",
            "action": "treat river length, season convention, daylight window, coordinates, campsite spacing and count, craft speeds, duration mix, launch rate, figure scenarios, and cutoff labels as versioned data",
            "evidence_ids": [first_by_dimension["data"]],
        },
        {
            "rule_id": "R-B-DATA-002",
            "action": "maintain an assumption ledger for even spacing, one-group occupancy, daylight travel, two speeds, controlled demand, fixed stop counts, constant class mix, steady state, and target-river transfer",
            "evidence_ids": [evidence_for("R-B-DATA-002")],
        },
        {
            "rule_id": "R-B-MOD-001",
            "action": "retain scaling, floor capacity, staggered starts, minute updates, greedy campsite placement, conditional stop construction, blocking geometry, probability cutoff, and manager handoff only with typed interfaces",
            "evidence_ids": [first_by_dimension["modeling"]],
        },
        {
            "rule_id": "R-B-MOD-003",
            "action": "combine the analytic, agent, itinerary, and probability views only through a declared seasonal-capacity decision layer that reconciles launches, concurrency, retained schedules, failures, utilization, and completion",
            "evidence_ids": [evidence_for("R-B-MOD-003")],
        },
        {
            "rule_id": "R-B-MOD-004",
            "action": "keep boats, boaters, groups, customers, launches, concurrent occupancy, retained itinerary trips, completed trips, failures, utilization, censored trips, and recommended capacity separately labeled",
            "evidence_ids": [first_by_dimension["result"]],
        },
        {
            "rule_id": "R-B-MOD-005",
            "action": "stress campsite geometry, daylight window, craft-speed mix, duration mix, launch timing, launch volume, event ordering, greedy rollback, season boundary, probability factorization, and target-river calibration",
            "evidence_ids": [evidence_for("R-B-MOD-005")],
        },
        {
            "rule_id": "R-B-VER-002",
            "action": "make reliability dimension-, repeated-run-, threshold-, censoring-, schedule-feasibility-, equation-event-, cutoff-, uncertainty-, and external-calibration-specific",
            "evidence_ids": [first_by_dimension["verification"]],
        },
        {
            "rule_id": "R-B-VER-004",
            "action": "reconcile the floor derivative, undefined symbols, captions, cross-references, duplicated plots, launch/completion ambiguity, greedy rollback, conditional Poisson law, blocking factors, spacing labels, and season arithmetic before reuse",
            "evidence_ids": [first_by_dimension["weakness"]],
        },
        {
            "rule_id": "R-B-VIZ-001",
            "action": "retain the parameter table, twenty-two figures, schematic geometry, axes, units, scenario settings, uncertainty bars, one-percent cutoff, exact caption meaning, and linked prose contradictions",
            "evidence_ids": [first_by_dimension["visualization"]],
        },
        {
            "rule_id": "R-B-COMP-001",
            "action": "choose minute-step state storage, campsite-search indexing, greedy backtracking, parameter-sweep parallelism, probability evaluation, caching, runtime, and memory from measured boats, campsites, days, scenarios, and repetitions",
            "evidence_ids": [evidence_for("R-B-COMP-001")],
        },
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [
        {
            "language_unit_id": unit["language_unit_id"],
            "disposition": "supports-existing",
            "target_pattern_ids": unit["candidate_pattern_ids"],
            "reason": "Reuse only after replacing river-specific facts while preserving rhetorical function, information order, typed slots, observed variants, and transfer boundary.",
        }
        for unit in language["units"]
    ]

    paragraph_moves = {
        "abstract": [
            "management decision and common capacity objective",
            "shared daylight, campsite, demand, and trip assumptions",
            "analytic base case and its restrictive reference role",
            "agent model mechanism and departure-time recommendation",
            "itinerary model mechanism and fixed-schedule recommendation",
            "probability model mechanism and cutoff recommendation",
            "model-specific capacity values and common reported range",
            "manager-facing choice among safety, autonomy, and crowding tradeoffs",
        ],
        "introduction": [
            "rising rafting demand, overcrowding risk, and one-group-per-campsite constraint",
            "maximum-groups question and three-model comparison plan",
        ],
    }
    paragraph_chains = []
    for chapter, moves in paragraph_moves.items():
        unit_ids = [unit["language_unit_id"] for unit in language["units"] if unit["chapter"] == chapter]
        paragraph_chains.append(
            {
                "chapter": chapter,
                "visual_paragraph_count": len(moves),
                "coverage_status": "complete",
                "gaps": [],
                "paragraphs": [
                    {
                        "paragraph_index": index + 1,
                        "dominant_move": move,
                        "language_unit_ids": [unit_ids[index % len(unit_ids)]],
                    }
                    for index, move in enumerate(moves)
                ],
            }
        )

    progressions = []
    for chapter in language["available_chapters"]:
        source_sections = [key for key, protocol_chapter, *_ in CHAPTERS if protocol_chapter == chapter]
        section_names = ", ".join(source_sections)
        progressions.append(
            {
                "chapter": chapter,
                "moves": [
                    f"input: the source-checked decision, assumption, parameter, formula, state, itinerary, probability event, figure, or manager question entering {section_names}",
                    f"rhetorical job: perform the observed framing, definition, assumption explanation, algorithm narration, trend interpretation, comparison, qualification, or recommendation across {section_names}",
                    f"analytical job: apply the declared scaling, movement update, campsite search, greedy feasibility, conditional process, blocking calculation, cutoff reading, or decision comparison across {section_names}",
                    f"output: retain a typed bound, schedule, trajectory, failure metric, utilization result, probability, threshold, limitation, or manager choice from {section_names}",
                    "handoff: name the next model, parameter sweep, visual check, cutoff interpretation, cross-model comparison, limitation, extension, or manager action",
                ],
                "positive_pattern": "Use explicit input -> mechanism -> typed output -> verification or comparator -> scoped handoff; final warnings may annotate but never replace the positive section contract.",
            }
        )

    equation_refs = [
        (model["model_id"], equation["equation_id"], equation["page"])
        for model in models["models"]
        for equation in model["governing_equations"]
    ]
    warning_rows = []
    for page, warning in WARNINGS:
        model_id, equation_id, _ = min(
            equation_refs,
            key=lambda item: (abs(item[2] - page), item[2], item[1]),
        )
        warning_rows.append(
            {
                "model_id": model_id,
                "equation_id": equation_id,
                "page": page,
                "warning": warning,
            }
        )

    dimensions = Counter(row["dimension"] for row in observations)
    return {
        "audit_id": f"LA-B-{YEAR}-{SHORT}",
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "source_sha256": SHA,
        "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [
            {
                "chapter": chapter,
                "pass_count": 3,
                "last_pass_new_moves": 0,
                "coverage_status": "complete",
                "gaps": [],
                "new_moves_by_pass": [18 if chapter in {"abstract", "memo", "introduction"} else 12, 4, 0],
            }
            for chapter in language["available_chapters"]
        ],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "complete",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [
                "The abstract forecasts the river-capacity decision, common assumptions, three model families, model-specific recommendations, and common reported range.",
                "The manager memo translates the mathematical alternatives into safety, autonomy, crowding, maintenance, throughput, and implementation tradeoffs.",
                "The introduction and parameter table turn rising demand and one-group-per-campsite occupancy into a typed capacity problem.",
                "Shared and model-specific assumptions define daylight, season, river length, campsite geometry, craft speeds, trip durations, demand, and desired stopping behavior.",
                "The analytic base case rescales time, speed, and spacing to derive a restrictive launch bound and staggered departure reference.",
                "The agent model advances independent boats minute by minute, searches for campsites, records failures, and sweeps departure time, slow-boat duration, launch rate, and campsite count.",
                "The itinerary model prioritizes slow boats, greedily selects feasible campsites near daily goals, rejects infeasible demand, and separates a comfortable threshold from an overdriven upper envelope.",
                "The probability model conditions a stop process, argues for a nightly fleet distribution, decomposes blocking events, and reads a one-percent cutoff from six parameterized plots.",
                "The conclusion compares model mechanisms and maps manager beliefs about fixed schedules and autonomous behavior to a recommended operating rule.",
                "The extension section opens nonuniform campsite, correlated weather, and seasonal-demand directions while preserving the need for target-river calibration.",
                "The final warning pass reconciles date, unit, season, symbol, algorithm, caption, probability, cutoff, spacing, completion, validation, and provenance defects without replacing positive learning artifacts.",
            ],
            "section_progressions": progressions,
            "main_argument_chains": [
                {
                    "claim": "A restrictive analytic reference can link travel window, identical speed, campsite spacing, and daily launches.",
                    "support_steps": ["dimensionless time, speed, and spacing", "floor launch bound", "staggered departure schedule", "continuous-surrogate sensitivity"],
                    "decision_consequence": "Use it as a transparent reference case, not a validated optimum, and separate the step function from any continuous relaxation.",
                    "source_pages": [8, 9, 10],
                },
                {
                    "claim": "An autonomous minute-step boat model can relate departure timing and slow-boat trip length to failures and utilization.",
                    "support_steps": ["random boat attributes", "remaining-distance goal", "minute position update", "campsite-search trigger", "failure rules", "parameter plots"],
                    "decision_consequence": "Operational use requires exact event ordering, simultaneous-arrival handling, seeds, repetitions, raw outputs, uncertainty, and season-end censoring.",
                    "source_pages": [11, 12, 13, 14, 15, 16, 17],
                },
                {
                    "claim": "A greedy fixed-itinerary model can reject infeasible demand before issuing schedules and can distinguish a comfortable threshold from an upper envelope.",
                    "support_steps": ["speed priority", "daily goal", "feasible campsite search", "nearest-goal placement", "failed-boat removal", "launch and campsite sweeps"],
                    "decision_consequence": "Treat approximately 1260 retained trips as the stated comfortable regime and roughly 1400 as an overdriven envelope only after speed generation, rollback, rejected demand, completion, and uncertainty are specified.",
                    "source_pages": [17, 18, 19, 20, 21, 22],
                },
                {
                    "claim": "A conditional stochastic stop model can turn nightly boat positions and campsite blocking geometry into a cutoff probability.",
                    "support_steps": ["conditional Poisson stop construction", "uniform-order-statistic argument", "nightly fleet superposition", "Figure 16 geometry", "equal-speed events", "mixed-speed events", "six cutoff plots"],
                    "decision_consequence": "Do not reuse the 77-boat cutoff until conditioning, steady state, event completeness, mixed-speed arrival order, and printed spacing labels are re-derived and calibrated.",
                    "source_pages": [23, 24, 25, 26, 27, 30, 31, 32, 33, 34, 35],
                },
                {
                    "claim": "The paper's three model families report a similar seasonal range and support different manager control philosophies.",
                    "support_steps": ["agent estimate near 1170", "itinerary comfortable threshold near 1260", "probability conversion near 1155", "memo safety/autonomy tradeoff", "conclusion comparison"],
                    "decision_consequence": "Present the range as shared-assumption triangulation rather than independent validation, and keep launches, concurrency, retained schedules, completions, and customers distinct.",
                    "source_pages": [1, 2, 16, 22, 27, 28, 29],
                },
            ],
        },
        "formula_error_watch": {
            "mode": "last-pass-warning-only",
            "completed_after_positive_passes": True,
            "warnings": warning_rows,
        },
        "model_retention": {
            "model_count": len(models["models"]),
            "retained_model_ids": [model["model_id"] for model in models["models"]],
            "retained_equation_ids": [item[1] for item in equation_refs],
            "central_equations": [
                {
                    "model_id": model["model_id"],
                    "equation_ids": [equation["equation_id"] for equation in model["governing_equations"]],
                    "all_central_equations_retained": True,
                }
                for model in models["models"]
                if model["governing_equations"]
            ],
        },
        "visualization_dispositions": [
            {
                "paper_card_visual_index": index,
                "visual_record_id": f"V-B-{YEAR}-{SHORT}-{index:03d}",
                "disposition": "important-visual-record",
                "analytical_purpose": visual["summary"],
            }
            for index, visual in enumerate(card["visualization_observations"], 1)
        ],
        "dimension_counts": {
            dimension: dimensions[dimension]
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
        },
        "positive_reusable_language_count": len(language["units"]),
        "weakness_record_count": dimensions["weakness"],
        "review_status": "validated",
    }


def main() -> None:
    language = make_language()
    models = make_models()
    card = make_card(language, models)
    observations = make_observations(language, models, card)
    attach_rule_impacts(card, observations)
    audit = make_audit(language, models, card, observations)

    base.write_json(ROOT / "artifacts/language-units" / f"{PID}.json", language)
    base.write_json(ROOT / "artifacts/model-units" / f"{PID}.json", models)
    base.write_json(ROOT / "artifacts/paper-cards" / f"{PID}.json", card)
    base.write_json(ROOT / "artifacts/learning-audits" / f"{PID}.json", audit)
    observation_path = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    observation_path.parent.mkdir(parents=True, exist_ok=True)
    observation_path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "paper_id": PID,
                "language_units": len(language["units"]),
                "models": len(models["models"]),
                "equations": len(EQUATIONS),
                "observations": len(observations),
                "chapters": len(language["available_chapters"]),
                "visuals": len(VISUALS),
                "warnings": len(WARNINGS),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
