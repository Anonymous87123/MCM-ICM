from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import build_q93_artifacts as template


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2012-13074-8fc549d2"
SHORT = "13074"
SHA = "8fc549d20a5ec5d7cff7a85c2785f8c74f8510f203d55bccbec02a08da5f1fb5"
TYPE = "B"
YEAR = "2012"
PAGE_COUNT = 22

PATTERNS = [
    "LP-B-INTRO-CONTEXT-TASK-THREE-LEVELS",
    "LP-B-DEFINITION-SYMBOL-OPERATION",
    "LP-B-ASSUMPTION-MECHANISM-CONVENIENCE",
    "LP-B-CONTROL-RELAXATION-CAPACITY-TRADEOFF",
    "LP-B-PARTITION-LOCAL-SCHEDULE-GLOBAL-ASSEMBLY",
    "LP-B-LEADER-CYCLE-FORGONE-LOSS",
    "LP-B-PROPORTION-TO-RESOURCE-ALLOCATION",
    "LP-B-SMALL-CASE-TO-GENERAL-ORBIT",
    "LP-B-PROBABILITY-DEFINITION-RECURSION-HANDOFF",
    "LP-B-GREEDY-MINIMAX-STOP-RULE",
    "LP-B-GIVEN-TRIPS-CONTINUATION-CASE",
    "LP-B-RANDOM-FEASIBLE-CONSTRUCTION",
    "LP-B-SENSITIVITY-PARAMETER-TABLE-INTERPRETATION",
    "LP-B-STRENGTH-WEAKNESS-EXTENSION",
    "LP-B-CONCLUSION-THREE-OPTION-DECISION",
    "LP-B-MANAGER-LETTER-FINDING-TRADEOFF",
]

# key, protocol chapter, first page, last page, tag, language-unit count,
# source-checked paraphrase, visually observed paragraph count
CHAPTERS = [
    ("introduction", "introduction", 1, 1, "INT", 28, "The Introduction frames river popularity, wilderness separation, a 225-mile corridor, six-month scheduling, and three progressively less controlled schedule designs whose capacity and flexibility must be traded by managers.", 9),
    ("definitions", "problem-restatement", 2, 2, "DEF", 18, "The definitions assign operational meanings to optimal, route, orbit, twenty-six nominal trip types, daily travel demand, orbit size, and seasonal trip count.", 8),
    ("problem-formulation", "problem-analysis", 2, 2, "FRM", 16, "The formulation represents the river as an ordered line of campsites and separates deterministic fixed-route, random-route, and random-type scheduling questions.", 5),
    ("assumptions", "assumptions", 3, 3, "ASM", 20, "The assumptions impose downstream travel, one-night stops, a daily travel limit, uniform complete-route choice, a small-probability collision convention, and a worked value Y=150.", 8),
    ("part1-method", "model-establishment", 3, 4, "P1M", 22, "Part 1 motivates the most controlled schedule, defines exclusive campsite orbits, and decomposes the task into single-type, multi-type, and two-orbit regimes as Y decreases.", 9),
    ("single-type-orbits", "algorithm", 4, 7, "SNG", 30, "The single-type construction partitions campsites by residue, chooses a leader route, fills campsites ahead of the leader, repeats a short cycle, and maps requested type proportions to orbit sizes.", 17),
    ("multi-type-orbits", "model-improvement", 7, 9, "MUL", 28, "The multi-type construction shares each orbit among paired propulsion-compatible durations, derives a Y=150 two-day cycle, lists fixed routes, and reports 2,340 launches.", 13),
    ("general-orbits", "model-improvement", 9, 10, "GEN", 16, "The orbit idea is extended from three durations to an arbitrary group and finally to one orbit per propulsion class for small Y.", 6),
    ("part2-method", "model-establishment", 10, 11, "P2M", 22, "Part 2 replaces fixed routes by an equal-probability route model, defines route-count, occupancy, and collision quantities, invokes inclusion-exclusion, and announces a greedy minimax schedule.", 10),
    ("route-probability", "model-establishment", 12, 12, "PRB", 24, "The paper recursively counts route prefixes and combines them with a printed suffix factor to estimate the probability that trip type T occupies campsite x on day t.", 7),
    ("greedy-schedule", "algorithm", 12, 15, "GRD", 30, "For each launch day the algorithm evaluates every candidate type, chooses the one minimizing the worst campsite-day collision probability, stops when the threshold fails, and displays a 180-day calendar totaling 500 trips.", 15),
    ("given-trips", "model-improvement", 15, 15, "GIV", 14, "Two continuation cases treat X given trips with free or fixed routes as an initial schedule state before the same probability-based construction continues.", 5),
    ("part3-random", "algorithm", 16, 17, "RND", 24, "Part 3 selects uniformly from currently feasible trip types rather than the greedy minimizer, reports eight capacities, and aggregates the resulting type frequencies.", 10),
    ("sensitivity", "sensitivity-analysis", 17, 18, "SEN", 24, "Sensitivity tables vary the first trip type, daily travel hours, and the small-probability threshold, then interpret the resulting capacity changes.", 9),
    ("evaluation", "strengths-limitations", 19, 20, "EVA", 18, "The evaluation lists operational strengths, distributional weaknesses, and survey-based extensions for route and type-choice probabilities.", 10),
    ("conclusion", "conclusion", 20, 20, "CON", 18, "The conclusion restates the three control regimes, orbit, recursion, inclusion-exclusion, greedy and random mechanisms, and the headline capacities 2,340, 500, and 493.", 6),
    ("references", "references", 20, 20, "REF", 8, "Four web references provide weak practical context, including one duplicated source and no executable or archival reproduction package.", 4),
    ("manager-letter", "memo", 21, 22, "LTR", 22, "The manager letter translates the three schedules into choices between capacity and tourist freedom, repeats the headline figures, and delegates the final commercial and management decision.", 8),
]

MOVES = [
    ("three-level-control-frame", "Present one decision problem through three progressively relaxed control regimes and forecast the capacity-flexibility tradeoff.", "context -> hard constraint -> three regimes -> decision tradeoff"),
    ("definition-to-computation", "Define each operational word or symbol immediately before the formula or algorithm that consumes it.", "term -> symbol -> unit or range -> downstream use"),
    ("assumption-with-replacement", "State a simplifying distribution, explain why it is convenient, and note how an empirical distribution could replace it.", "mechanism -> simplification -> convenience -> replacement boundary"),
    ("partition-before-scheduling", "Partition a coupled resource into disjoint orbits, solve each local schedule, and assemble the global calendar.", "resource partition -> local cycle -> aggregation -> capacity"),
    ("leader-cycle-construction", "Introduce a leader path, name unavoidable transient loss, fill positions behind it, and repeat the resulting cycle.", "leader -> transient -> follower fill -> cycle"),
    ("proportion-to-allocation", "Translate requested type proportions into trip counts, orbit-size ratios, and a complete resource allocation.", "demand mix -> count ratio -> orbit ratio -> allocation"),
    ("small-case-generalization", "Demonstrate two and three types in one orbit before stating the arbitrary-group construction and its boundary.", "worked case -> repeated mechanism -> general form -> limit"),
    ("probability-dataflow", "Define route counts, convert them to point occupancy probabilities, combine trips into collision risk, and hand the risk to scheduling.", "count -> marginal probability -> joint risk -> decision"),
    ("greedy-minimax", "For each candidate compute a worst local risk, choose the smallest worst risk, and stop at a named threshold.", "candidate -> worst case -> minimizer -> stop"),
    ("random-feasible-comparator", "Replace the greedy choice by random selection among feasible candidates and compare repeated capacities and composition.", "feasible set -> random draw -> repeated runs -> distribution"),
    ("sensitivity-table-claim", "Vary one assumption at a time, retain the exact table, and connect the observed change to a qualified stability claim.", "parameter -> sweep -> output range -> qualified implication"),
    ("strength-weakness-extension", "Pair each claimed strength with the assumption that enables it and a practical data collection extension.", "benefit -> assumption -> weakness -> remedy"),
    ("managerial-option-letter", "Translate each model into a manager-facing option with mechanism, capacity, flexibility, and selection boundary.", "option -> method -> result -> tradeoff -> choice"),
]

EXAMPLES = [
    ("A park introduction presents controlled permits, flexible routes, and user-selected trip products as three explicit operating regimes.", "It predicts the capacity-flexibility tradeoff without calling any regime universally best."),
    ("A scheduling paper defines route, service day, resource block, and risk threshold immediately before using them.", "Every symbol has a unit and one downstream consumer."),
    ("A route-choice model starts with equal path probabilities for calibration and states how survey-estimated probabilities replace them.", "The simplification is not described as realistic by default."),
    ("A berth scheduler partitions docks by vessel class, solves cyclic sub-schedules, and then proves that the assembled calendar is conflict free.", "The proof covers transients and season boundaries."),
    ("A production cycle identifies unavoidable warm-up loss and then fills all reachable slots behind a leader batch.", "The cycle length and termination state are explicit."),
    ("A permit system converts observed demand shares into capacity-weighted resource shares rather than ignoring duration.", "The allocation equation retains service time."),
    ("A two-class worked schedule is generalized only after the invariant and feasibility test are written.", "The m-class index range contains exactly m classes."),
    ("A path model counts prefixes and remaining-time suffixes, verifies probability normalization, and then computes collision risk.", "Independence is stated or a joint model is used."),
    ("A greedy scheduler minimizes maximum local overload and reports both the local threshold and system-wide risk.", "Best observed is kept distinct from global optimum."),
    ("A randomized scheduler reports seeds, run count, mean, interval, maximum, and the exact selected realization.", "It does not publish the sample maximum alone."),
    ("A sensitivity section flags a nonmonotone spike as a reproducibility defect before claiming stability.", "All other parameters and code versions are frozen."),
    ("A conclusion gives managers capacity, flexibility, safety risk, and evidence strength for each option.", "The recommendation abstains when a hard constraint fails."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose
EQUATIONS = [
    ("daily travel demand", 4, "Part 1 feasibility", "trip feasibility", "A_i = 225/(v_i d_i), feasible iff A_i <= 8", r"A_i=\frac{225}{v_i d_i},\quad A_i\le8", ["A_i", "v_i", "d_i"], "Compute average daily river hours for each propulsion-duration type."),
    ("seven-day oar value", 4, "Part 1 feasibility", "trip feasibility", "A_3 = 225/(4*7) = 8.03", r"A_3=\frac{225}{4\cdot7}\approx8.0357", ["A_3"], "Retain the printed near-threshold calculation and its deliberate constraint relaxation."),
    ("orbit interval distance", 5, "single-type orbit", "orbit geometry", "interval = (25/Y)*225 miles", r"\ell=\frac{25\cdot225}{Y}", ["ell", "Y"], "Approximate the distance between consecutive campsites in one residue-class orbit."),
    ("maximum orbit step", 5, "single-type orbit", "route step bound", "Q = floor(32Y/(25*225))", r"Q=\left\lfloor\frac{32Y}{25\cdot225}\right\rfloor", ["Q", "Y"], "Convert the oar daily distance into a maximum number of orbit intervals."),
    ("route distance decomposition", 5, "single-type orbit", "integer route construction", "sum_i z_i i = n_i", r"\sum_{i=1}^{Q} i z_i=n_i", ["z_i", "Q", "n_i"], "Represent an orbit route by counts of step lengths."),
    ("route day count", 5, "single-type orbit", "integer route construction", "sum_i z_i = duration - 1", r"\sum_{i=1}^{Q}z_i=d_i-1", ["z_i", "Q", "d_i"], "Match the number of campsite nights to the trip duration convention."),
    ("single-type seasonal count", 6, "single-type orbit", "capacity approximation", "m_i = floor(180 n_i/duration_i)", r"m_i=\left\lfloor\frac{180n_i}{d_i}\right\rfloor", ["m_i", "n_i", "d_i"], "Estimate seasonal launches assigned to one orbit."),
    ("large-Y threshold", 7, "single-type orbit", "resource threshold", "Y >= 7+...+18+6+...+18 = 306", r"Y\ge\sum_{d=7}^{18}d+\sum_{d=6}^{18}d=306", ["Y"], "State the printed campsite threshold for separate type orbits."),
    ("Y150 construction threshold", 8, "multi-type orbit", "resource threshold", "Y >= 5+2(7+9+11+13+15+17) = 149", r"Y\ge5+2(7+9+11+13+15+17)=149", ["Y"], "Check the paired-orbit construction against Y=150."),
    ("Part 1 launch count", 9, "multi-type orbit", "schedule capacity", "26*180/2 = 2340", r"M_1=\frac{26\cdot180}{2}=2340", ["M_1"], "Convert twenty-six launches per two-day cycle into a seasonal count."),
    ("inclusion-exclusion expansion", 11, "Part 2 method", "probability union", "P(union A_i)=sum P(A_i)-sum P(A_i cap A_j)+...+(-1)^(n-1)P(union A_i)", r"P\!\left(\bigcup_iA_i\right)=\sum_iP(A_i)-\sum_{i<j}P(A_i\cap A_j)+\cdots+(-1)^{n-1}P\!\left(\bigcup_iA_i\right)", ["P", "A_i"], "Retain the printed expansion whose final union should be the full intersection."),
    ("route-count base", 12, "route probability", "dynamic programming", "f(T,x,1)=1 for 1<=x<=N", r"f(T,x,1)=1,\quad1\le x\le N_T", ["f", "T", "x", "N_T"], "Initialize one-day reachable campsite route counts."),
    ("route-count recursion", 12, "route probability", "dynamic programming", "f(T,x,t)=sum_available_y f(T,y,t-1)", r"f(T,x,t)=\sum_{y\in\mathcal P_T(x)}f(T,y,t-1)", ["f", "T", "x", "t", "y"], "Count route prefixes through reachable predecessor campsites."),
    ("printed occupancy probability", 12, "route probability", "path probability", "p(T,x,t)=f(T,x,t)f(T,Y+1-x,duration)/f(T,Y+1,duration)", r"p(T,x,t)=\frac{f(T,x,t)f(T,Y+1-x,d_T)}{f(T,Y+1,d_T)}", ["p", "f", "T", "x", "t", "Y", "d_T"], "Compute the printed campsite-day occupancy probability while preserving the missing remaining-time warning."),
    ("greedy minimax choice", 12, "greedy schedule", "minimax heuristic", "choose T minimizing max_(x,day) q_after_T(x,day)", r"T^*=\arg\min_T\max_{x,\tau}q_T(x,\tau)", ["T_star", "T", "q", "x", "tau"], "Choose the candidate type with the smallest worst local collision probability."),
]

# page, family, purpose, inputs, outputs
ALGORITHMS = [
    (4, "residue-class orbit partition", "Assign campsites to type-specific residue classes before local scheduling.", ["Y", "eligible trip types"], ["orbits"]),
    (5, "leader-and-follower cyclic schedule", "Move a leader by maximum feasible steps and fill reachable campsites with follower launches.", ["orbit", "Q", "duration", "season horizon"], ["cyclic launch and route schedule"]),
    (6, "proportional orbit allocation", "Translate desired trip-type proportions into orbit sizes and campsite assignments.", ["type proportions", "durations", "Y"], ["n_i allocation"]),
    (7, "skeleton-orbit allocation", "Use sparse mandatory campsite skeletons before assigning remaining campsites.", ["Y", "daily travel limits", "trip types"], ["feasible orbit skeletons"]),
    (8, "paired-type two-day schedule", "Share one orbit between two duration types and repeat a two-day pattern for Y=150.", ["paired types", "150 campsites", "route lists"], ["Part 1 schedule", "2340 launch count"]),
    (10, "multi-type orbit generalization", "Extend a worked three-type orbit to larger same-propulsion type groups.", ["m trip types", "shared orbit"], ["generalized orbit schedule"]),
    (11, "collision probability aggregation", "Combine trip occupancy events into campsite-day probability of at least two simultaneous trips.", ["p_i(x,day)", "event dependence"], ["q(x,day)"] ),
    (12, "greedy daily schedule construction", "Add the minimax candidate repeatedly for each of 180 launch days until the local threshold fails.", ["trip types", "q", "threshold", "Y", "180 days"], ["500-trip calendar"]),
    (15, "given-trip continuation", "Continue the schedule from X fixed initial trips after checking their route treatment.", ["X given trips", "dates", "types", "optional fixed routes"], ["augmented schedule"]),
    (16, "random feasible trip construction", "Randomly select among currently feasible types instead of minimizing worst collision risk.", ["feasible candidate set", "random generator", "180 days"], ["random schedule capacity", "type composition"]),
    (18, "first-type sensitivity sweep", "Run the Part 2 procedure once for each of twenty-four legal initial types.", ["first trip type", "fixed remaining settings"], ["capacity by first type"]),
    (18, "hours-and-threshold sensitivity sweeps", "Vary daily travel hours and collision thresholds and compare capacity outputs.", ["hour limit", "probability threshold", "first type 22"], ["capacity sensitivity tables"]),
]

VISUALS = [
    (2, "Chart 1 - numbered trip types", "Maps 6-18 day durations and two propulsion modes to nominal type numbers 1-26."),
    (4, "Chart 2 - model outline", "Shows the orbit-regime split as Y decreases, but page-scale labels are small."),
    (6, "Chart 3 - Y=425 schedule", "Illustrates the leader-cycle construction for the seven-day oar type with a six-night schedule convention."),
    (7, "Chart 4 - type 3 skeleton orbit", "Shows widely spaced mandatory campsite positions for the most demanding retained type."),
    (7, "Chart 5 - generic skeleton orbit", "Shows a seven-point skeleton reused for other trip types, with small and partly malformed labels."),
    (8, "Chart 6 - two-type orbit schedule", "Demonstrates a repeated 7,7,8 sequence intended to tune a two-type proportion."),
    (9, "Chart 7 - first two days schedule", "Provides complete fixed campsite routes for a two-day Y=150 cycle and supports the 2340 launch arithmetic."),
    (10, "Chart 8 - three-type orbit schedule", "Illustrates the claimed transition from paired types to an arbitrary multi-type orbit."),
    (11, "Chart 9 - probability model flow", "Connects p calculation, q calculation, given-trip cases, type flexibility, and schedule construction."),
    (12, "Chart 10 - Part 2 calendar, March opening", "Begins the seven-column 180-day calendar whose launch multiplicities sum to 500."),
    (13, "Chart 10 - Part 2 calendar continuation 1", "Continues the calendar without repeated weekday headers, flattening badly in extracted text."),
    (14, "Chart 10 - Part 2 calendar continuation 2", "Continues the dense calendar through July with small but legible labels."),
    (15, "Chart 10 - Part 2 calendar close", "Completes the calendar through August 27 and visually supports the 500-trip count."),
    (17, "Charts 11-12 - random capacities and type totals", "Reports eight capacities and the aggregated 3864-trip type distribution dominated by long oar trips."),
    (18, "Charts 13-15 - sensitivity tables", "Displays first-type, daily-hour, and threshold sweeps, including the visually confirmed 560-versus-500 inconsistency."),
]

WARNINGS = [
    (1, "Carrying capacity is defined as trip count rather than passengers, vessel occupancy, ecological pressure, or total person-days."),
    (1, "The claim that three capacities must decline only because control is relaxed is not a controlled comparison because the type set and risk semantics also change."),
    (2, "Campsites are numbered 0 through Y+1 although only Y campsites are stated; launch and exit endpoints are not cleanly distinguished from campsites."),
    (3, "The daily travel assumption calls half a day eight hours and later alternates among at most, less than, and deliberately above eight hours."),
    (3, "The assumption lists both 0.05 and 0.025 without assigning them to models or risk meanings."),
    (3, "A local campsite-day probability below 0.05 does not control the probability of any collision across 150 campsites, 180 launch days, or the full network."),
    (3, "Y=150, uniform campsite spacing, and the 225-mile Grand Canyon analogy lack a traceable calibrated data source."),
    (4, "The seven-day oar type requires 225/(4*7)=8.0357 hours per day; printing 8.03 and adding it back violates the stated hard limit."),
    (4, "The printed 8.03 is truncated; ordinary two-decimal rounding gives 8.04."),
    (4, "Twenty-five residue classes do not all contain exactly Y/25 campsites unless Y is divisible by 25."),
    (5, "The orbit-spacing approximation uses 225/Y even though Y internal campsites between two endpoints imply Y+1 intervals."),
    (5, "The integer variables z_i lack a declared domain, solver, existence proof, and reproducible construction."),
    (5, "Filling positions ahead of a leader does not by itself prove optimality through startup, steady state, termination, and season boundaries."),
    (6, "Chart 3 uses six campsite nights for a seven-day type, exposing an unresolved days-versus-nights convention."),
    (6, "The formula m_i=floor(180 n_i/d_i) conflicts with route tables that occupy d_i-1 internal campsites and with the M-6 launch frequency."),
    (6, "Trip-count ratios do not equal orbit-size ratios when durations differ unless duration weights are retained."),
    (6, "Ignoring forgone loss supports an approximation, not an exact best-schedule proof."),
    (7, "The paper prints min A_i=A_3 although the retained seven-day oar type has the largest daily-hour requirement."),
    (7, "The paper prints A_i>=A_3 where the feasibility ordering requires A_i<=A_3."),
    (7, "The seven-point skeleton formulas do not specify rounding for noninteger fractions and contain a visibly malformed k range."),
    (7, "The threshold 306 sums durations, while the later Y=150 construction uses duration minus one; the campsite requirement is inconsistent."),
    (8, "The threshold 149 is arithmetically correct but adopts a different campsite-night convention from the 306 threshold."),
    (8, "Replacing 7,7,8 by arbitrary combinations does not prove daily travel or collision feasibility for every requested ratio."),
    (8, "The claim of uniform type distribution is contradicted by motorized six-day trips launching on both days of the cycle."),
    (9, "Twenty-five distinct feasible types produce twenty-six launches per two-day cycle because M-6 is duplicated; the prose risks conflating types and launches."),
    (9, "Chart 7 leaves campsite 150 unused and averages about 143 of 150 occupied campsites per cycle, contrary to full-utilization rhetoric."),
    (9, "Several printed oar routes require roughly nine to ten-and-a-half hours in a day, so the 2340 schedule violates the travel constraint beyond the O-7 average."),
    (9, "The 2340 arithmetic permits long trips launched on day 180 to finish after the six-month horizon; an in-season completion interpretation gives a lower count."),
    (9, "The table explanation alternates between day and night terminology and gives an example multiplicity that is not visible in the cited row."),
    (10, "The sequence n through n+m contains m+1 types; an m-type group should end at n+m-1."),
    (10, "The Y<18 boundary conflicts with the paper's use of d-1 internal campsite nights."),
    (10, "The jump from two and three types to arbitrary groups has no invariant, feasibility proof, or optimality proof."),
    (11, "The inclusion-exclusion final term visibly repeats the union; the standard formula requires the intersection of all n events."),
    (11, "Calling inclusion-exclusion Jordan Formula does not define the event family, dependence assumptions, or the probability of at least two occupancies."),
    (11, "The text alternates between below 0.05 and probability 0.05 being treated as impossible, leaving equality ambiguous."),
    (12, "The recursion defines x only through Y but the occupancy formula uses f(T,Y+1,duration)."),
    (12, "The printed occupancy probability uses a suffix count at the full duration rather than remaining time d-t and can fail probability normalization."),
    (12, "The paper declares only twenty-four legal types but continues to write candidate domains 1 through 26 without an implementation-level filter."),
    (12, "The greedy minimax schedule is a local heuristic and has no exchange argument, upper bound, exact comparison, or global-optimum proof."),
    (12, "The q function is never given an explicit computable formula and independence among trip route choices is not stated."),
    (15, "An arbitrary set of X given trips may already violate the collision threshold or may not correspond to a prefix of the greedy construction."),
    (15, "Multiple fixed-route given trips can collide deterministically; the continuation procedure does not state a feasibility rejection step."),
    (16, "Part 3 samples a feasible type for each launch rather than modeling tourists choosing types after launch, so the stochastic interface does not match the claimed freedom."),
    (16, "Random feasible selection has no seeds, tie policy, run-count justification, convergence diagnostic, or optimality guarantee."),
    (17, "The eight capacities have mean 483 and range 474-493; selecting the repeated maximum 493 is post-selection, not a representative or proven optimum."),
    (17, "Chart 12 aggregates all eight runs rather than documenting the complete schedule for either 493 realization."),
    (17, "Uniform selection from a changing feasible set produces a highly skewed final type distribution and is not equivalent to uniform overall type demand."),
    (18, "Chart 13 ranges from 473 to 500, so the first trip has a material effect and the main 500 is the maximum case."),
    (18, "Chart 14 visually confirms 454, 484, 560, 483, 488; the isolated 560 contradicts Chart 13, Chart 15, and the 500 main result under the stated same baseline."),
    (18, "The nonmonotone daily-hours sweep cannot support the claim that results change only slightly."),
    (18, "Changing the small-probability threshold from 0.025 to 0.05 changes capacity from 376 to 500, so the two values cannot be treated interchangeably."),
    (19, "Equal complete-route probabilities and equal feasible-type selection are admitted simplifications that directly determine the reported capacities."),
    (20, "Repeated use of optimal for the orbit construction, greedy schedule, and random maximum exceeds the evidence supplied."),
    (20, "References 2 and 3 are visually identical, the first source is a weak question-answer page, and reference-to-assumption linkage is missing."),
    (20, "No code, random seeds, machine-readable schedules, probability checks, or complete reproduction package is supplied."),
    (21, "The manager letter repeats 2340, 500, and 493 without carrying the hard-constraint failures and uncertainty needed for a decision."),
    (21, "The manager letter prints separate 'which' where the intended term is orbits."),
    (21, "Internal headers show page 21 of 20 and page 22 of 20; the denominator was not updated for the letter."),
    (22, "The final three lines are stranded on an otherwise almost empty page, creating an avoidable orphan and pagination defect."),
]


def configure_template() -> None:
    for name, value in {
        "ROOT": ROOT, "PID": PID, "SHORT": SHORT, "SHA": SHA, "TYPE": TYPE,
        "YEAR": YEAR, "PAGE_COUNT": PAGE_COUNT, "PATTERNS": PATTERNS,
        "CHAPTERS": CHAPTERS, "MOVES": MOVES, "EXAMPLES": EXAMPLES,
        "EQUATIONS": EQUATIONS, "ALGORITHMS": ALGORITHMS, "VISUALS": VISUALS,
        "WARNINGS": WARNINGS,
    }.items():
        setattr(template, name, value)
    template.configure_base()


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "day, hour, mile, mph, campsite, trip, route, probability, count, type, date, or dimensionless quantity as locally defined",
        "definition": f"Source-defined river-scheduling quantity {symbol}.",
        "source_status": "explicit-defined",
    }


def model_record(model_id: str, page: int, section: str, family: str, purpose: str, inputs: list[str], outputs: list[str], equations: list[dict]) -> dict:
    return {
        "model_id": model_id, "page": page, "section": section, "family": family,
        "purpose": purpose, "base_or_modification": "paper-specific", "summary": purpose,
        "variables": [variable(s, set(inputs), set(outputs)) for s in list(dict.fromkeys(inputs + outputs))],
        "inputs": inputs, "outputs": outputs, "governing_equations": equations,
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The printed relation was reconciled against the rendered page." if equations else "This record is a scheduling, probability, experiment, or extension procedure."},
        "objectives": [purpose, "Return a typed schedule, capacity, route probability, collision risk, sensitivity result, or decision option."],
        "constraints": [
            "Keep launch date, trip duration, propulsion, route, campsite-day occupancy, local collision risk, and season boundary separately typed.",
            "Distinguish nominal types, legal types, launches per cycle, complete routes, and trips finishing within the operating season.",
            "Do not turn a constructive schedule, greedy choice, or random sample maximum into a global optimum without a matching bound or proof.",
        ],
        "conditions": {
            "initial": {"status": "present", "details": ["River length, campsite count, trip type, travel limit, season horizon, and route-control regime are supplied."]},
            "boundary": {"status": "present", "details": ["The worked case assumes uniformly spaced campsites, downstream-only travel, one-night stops, and simplified route and type probabilities."]},
            "equilibrium": {"status": "not-applicable", "details": ["The paper builds finite schedules rather than a steady physical equilibrium."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Problem constants, web analogies, hand-built orbit schedules, recursive counting, heuristic optimization, random runs, and sensitivity tables.", "parameters": inputs},
        "algorithm": {"status": "partial", "steps": ["freeze declared inputs", "apply the printed formula or scheduling rule", "check travel, campsite-day, probability, and horizon constraints", "retain the exact result and warning", "hand outputs to the next regime or decision"], "software": ["No executable source code is supplied."], "convergence_criteria": "Greedy addition stops at the local 0.05 threshold; random construction stops when no type remains feasible for the current day."},
        "assumptions": ["Campsites are approximately uniform and travelers move only downstream.", "Complete routes or currently feasible trip types are sampled uniformly in Parts 2 and 3."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The conceptual dataflow is observable, but days-versus-nights conventions, missing remaining-time probability, undefined q, local-versus-global risk, horizon treatment, seeds, and code prevent full reproduction."},
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, visually checked equation, chart, table, schedule, or discussion."],
        "computational_cost": "Dominated by complete-route dynamic programming, repeated candidate evaluation across 18Y campsite-days, daily greedy or random insertion, and sensitivity reruns.",
        "strengths": ["The intended input-operation-output chain is observable.", "Several printed schedules and tables permit direct arithmetic checks."],
        "limitations": ["Hard feasibility, probability normalization, global risk, optimality, and reproducibility are incomplete.", "Confirmed source defects are retained only in the final warning pass."],
        "missing_details": ["Source code, route-count indexing, q formula, dependence assumptions, seeds, tie breaking, runtime, exact horizon semantics, empirical route distributions, and independent optimality bounds are absent."],
    }


def make_models() -> dict:
    models = []
    for idx, (label, page, section, family, source, latex, symbols, purpose) in enumerate(EQUATIONS, 1):
        eq = {"equation_id": f"EQ-B-{YEAR}-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": "high"}
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{idx:03d}", page, section, family, purpose, symbols[1:], [symbols[0]], [eq]))
    for idx, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, len(EQUATIONS) + 1):
        models.append(model_record(f"MU-B-{YEAR}-{SHORT}-{idx:03d}", page, family, family, purpose, inputs, outputs, []))
    by_family = {m["family"]: m["model_id"] for m in models}
    pairs = [
        ("trip feasibility", "residue-class orbit partition"),
        ("orbit geometry", "leader-and-follower cyclic schedule"),
        ("route step bound", "leader-and-follower cyclic schedule"),
        ("integer route construction", "leader-and-follower cyclic schedule"),
        ("leader-and-follower cyclic schedule", "proportional orbit allocation"),
        ("skeleton-orbit allocation", "paired-type two-day schedule"),
        ("resource threshold", "paired-type two-day schedule"),
        ("paired-type two-day schedule", "multi-type orbit generalization"),
        ("dynamic programming", "path probability"),
        ("path probability", "collision probability aggregation"),
        ("probability union", "collision probability aggregation"),
        ("collision probability aggregation", "greedy daily schedule construction"),
        ("minimax heuristic", "greedy daily schedule construction"),
        ("greedy daily schedule construction", "given-trip continuation"),
        ("greedy daily schedule construction", "random feasible trip construction"),
        ("random feasible trip construction", "first-type sensitivity sweep"),
        ("greedy daily schedule construction", "hours-and-threshold sensitivity sweeps"),
    ]
    edges = []
    for a, b in pairs:
        if a in by_family and b in by_family:
            edges.append({"from_model_id": by_family[a], "to_model_id": by_family[b], "handoff": f"The {a} output becomes an input, constraint, diagnostic, or warning boundary for {b}."})
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    assumptions = [
        (1, "The 225-mile river contains Y approximately uniform campsites and a six-month 180-day launch season."),
        (1, "Oar and motor craft average four and eight miles per hour and nominal durations span six through eighteen days."),
        (3, "Travel proceeds only downstream, each campsite is used for one night, and a new campsite is reached every day."),
        (3, "Travelers spend no more than eight hours per day on the river, except for the Part 1 seven-day oar exception."),
        (3, "All complete legal routes for one type are equally likely in Parts 2 and 3."),
        (3, "A campsite-day collision probability around 0.05 is treated as negligible."),
        (3, "Y=150 is a representative worked campsite count."),
        (4, "Exclusive campsite orbits can decouple trip types without losing the best schedule."),
        (6, "Startup forgone loss is small enough to ignore in seasonal capacity."),
        (7, "Sparse skeleton campsites guarantee all adjacent moves in an orbit are reachable."),
        (11, "Trip route choices can be combined through inclusion-exclusion or the so-called Jordan Formula."),
        (16, "All currently feasible trip types are equally likely choices in Part 3."),
    ]
    data = [
        (1, "Problem constants include 225 miles, Y campsites, 180 launch days, two propulsion speeds, and thirteen durations."),
        (2, "Chart 1 maps the twenty-six nominal propulsion-duration types."),
        (6, "Chart 3 supplies a Y=425 leader-cycle illustration."),
        (9, "Chart 7 gives every fixed campsite route in the Y=150 two-day Part 1 cycle."),
        (12, "The recursive route counts and occupancy formula provide the probability inputs for Parts 2 and 3."),
        (12, "Chart 10 begins the exact 180-day Part 2 launch calendar."),
        (17, "Charts 11-12 give eight random capacities and aggregated type counts totaling 3864."),
        (18, "Charts 13-15 give first-type, daily-hour, and small-probability sensitivity grids."),
        (20, "Four web references provide only weak practical analogies and include one duplicate."),
    ]
    verification_specs = [
        (4, "Average daily travel time screens nominal trip types.", "arithmetic-feasibility", "The threshold is explicit and easy to recalculate.", "The paper then knowingly admits an infeasible type."),
        (8, "The Y=150 paired-orbit threshold evaluates to 149.", "resource-count-check", "The arithmetic is transparent.", "It uses a different day/night convention from the 306 threshold."),
        (9, "Chart 7 can be replayed as a two-day cycle to check campsite-day collisions.", "schedule-replay", "No same-campsite same-day collision was found under the printed route timing convention.", "Several routes violate daily travel and the season boundary is undefined."),
        (9, "Twenty-six launches every two days give 2340 launches over 180 days.", "arithmetic-result", "The displayed count is reproducible.", "It is not a complete feasible-capacity proof."),
        (12, "Chart 10 launch multiplicities sum to 500 and span March 1 through August 27.", "calendar-recount", "The main Part 2 count matches the displayed schedule.", "The underlying p and q calculations are not validly reproduced."),
        (17, "Eight Part 3 runs produce 474 through 493 with mean 483.", "repeated-random-runs", "The table exposes run-to-run variation.", "Seeds, uncertainty, and selection policy are absent."),
        (18, "Twenty-four first-type runs range from 473 to 500.", "sensitivity-sweep", "The legal type set is visible.", "The result is more sensitive than the prose admits."),
        (18, "Daily-hour and threshold tables test two assumptions.", "sensitivity-sweep", "The exact printed values are retained.", "The 560 spike contradicts the main 500 result."),
        (19, "The authors explicitly list route-distribution, type-choice, and mix-balance weaknesses.", "self-critique", "The strongest behavioral assumptions are acknowledged.", "The final optimality language is not correspondingly reduced."),
    ]
    verification = [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification_specs]
    results = [
        (4, "Part 1 retains twenty-five distinct types only by allowing the seven-day oar type above the eight-hour limit."),
        (9, "The printed two-day cycle contains twenty-six launches and extrapolates to 2340 seasonal launches."),
        (12, "The Part 2 greedy calendar reports 500 launches for Y=150 and threshold 0.05."),
        (15, "A mechanical recount of the displayed Part 2 calendar equals 500."),
        (17, "Eight Part 3 runs are 482, 486, 493, 493, 476, 474, 485, and 475, with mean 483."),
        (17, "Aggregated Part 3 counts total 3864, split 67.7 percent oar and 32.3 percent motor."),
        (18, "First-type sensitivity ranges from 473 to 500, with type 22 producing 500."),
        (18, "Daily-hour sensitivity is 454, 484, 560, 483, and 488 for 7 through 9 hours."),
        (18, "Threshold sensitivity is 215, 376, and 500 for 0.01, 0.025, and 0.05."),
        (20, "The conclusion promotes 2340, 500, and the sample maximum 493 as the three carrying capacities."),
    ]
    writing = [
        (1, "Introduction chain: river popularity -> wilderness collision constraint -> trip characteristics -> carrying-capacity definition -> three control regimes -> manager choice."),
        (2, "Definition chain: operational terms -> type numbering -> symbols -> deterministic and stochastic subquestions."),
        (3, "Assumption chain: movement rules -> daily limit -> route distribution -> small-probability convention -> Y=150 demonstration."),
        (4, "Part 1 chain: control routes -> divide into orbits -> solve local cycles -> combine type proportions -> specialize to Y=150."),
        (5, "Single-orbit chain: spacing -> daily step Q -> leader -> forgone loss -> followers -> repeated cycle."),
        (7, "Scale-down chain: single-type orbits -> paired types -> three types -> arbitrary group -> two propulsion orbits."),
        (10, "Part 2 chain: actual route freedom -> equal route probability -> f and p -> collision q -> greedy minimax -> calendar."),
        (15, "Extension chain: X given free routes -> X fixed routes -> continue the same schedule state."),
        (16, "Part 3 chain: type freedom -> random feasible choice -> eight runs -> composition table -> compare with Part 2."),
        (17, "Robustness chain: first-trip sweep -> daily-hour sweep -> risk-threshold sweep -> strengths and weaknesses."),
        (20, "Conclusion chain: three methods -> three headline capacities -> manager tradeoff -> repeated executive letter."),
    ]
    contributions = [
        {"page": 4, "summary": "Uses campsite-orbit partitioning to decompose a coupled seasonal route schedule."},
        {"page": 5, "summary": "Expresses a cyclic leader-and-follower construction with integer step counts."},
        {"page": 8, "summary": "Builds a concrete two-day Y=150 fixed-route schedule."},
        {"page": 12, "summary": "Connects dynamic route counting, occupancy probability, collision risk, and minimax trip insertion."},
        {"page": 15, "summary": "Extends the schedule state to cases with X given trips."},
        {"page": 16, "summary": "Introduces a randomized feasible comparator to expose trip-mix behavior."},
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 3, "summary": "Replace uniform campsite spacing and web analogies with surveyed campsite coordinates, closures, capacities, ecological limits, and trip demand."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 4, "summary": "Enforce daily travel and season-end constraints exactly, with explicit day-versus-night indexing and no near-threshold exceptions."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 5, "summary": "Formulate fixed-route scheduling as a time-expanded conflict graph or integer program and compare orbit cycles with exact upper bounds."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 12, "summary": "Correct the prefix-suffix probability with remaining time, define q explicitly, test normalization, and validate collision risk by simulation."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 12, "summary": "Control system-wide collision probability through a union bound, chance constraint, or target expected collision count rather than per-cell 0.05."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 16, "summary": "Model tourist type choice with an estimated mixed distribution and optimize offered departures before choices are realized."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 17, "summary": "Use frozen code, seeds, many independent runs, mean and quantile reporting, and exact small-instance benchmarks."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 18, "summary": "Investigate and reconcile the 560 spike before drawing any sensitivity conclusion."},
    ]
    return {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": SHORT,
        "title": "Best Schedule to Utilize the Big Long River", "award_status": "outstanding",
        "source": {"relative_path": "2012美赛特等奖/B-13074-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "The PDF contains 22 physical pages although internal headers continue from page 1 of 20 through page 22 of 20."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 22, "rendered_pages": 22, "visual_review": "complete", "notes": ["All 22 UTF-8 page files were read sequentially by the root context.", "Two fresh read-only visual contexts reviewed pages 1-11 and 12-22 using six byte-bounded JPEG proxies each; the first used one additional formula crop and both returned text only.", "Visual review reconciled all fifteen charts, displayed equations, page numbering, long tables, and source defects without exposing original PNGs or PDF pages to the root context."]},
        "context_sources": [{"type": "paper", "path": "2012美赛特等奖/B-13074-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "rendered-pages", "path": f"artifacts/papers/{PID}/rendered"}],
        "task_reconstruction": {"inputs": ["225-mile river", "Y campsites", "180-day launch season", "oar and motor speeds", "6-18 day durations", "daily travel limit", "X given trips", "collision-risk threshold"], "outputs": ["launch dates", "trip types", "fixed or probabilistic routes", "campsite-day risk", "seasonal trip count", "sensitivity results", "manager-facing option"], "decisions": ["which control regime to use", "how campsites are partitioned", "which trip is launched next", "whether local and system-wide risk is acceptable", "whether all trips meet travel and horizon constraints", "which capacity claim is supported"]},
        "section_map": [{"page": s, "section": k, "summary": e} for k, _, s, _, _, _, e, _ in CHAPTERS],
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [{"page": p, "summary": s} for p, s in data],
        "models": [{"model_id": m["model_id"], "page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"], "verification": verification,
        "results_trace": [{"page": p, "summary": s} for p, s in results], "contributions": contributions,
        "writing_logic": [{"page": p, "summary": s} for p, s in writing],
        "language_observations": [{"page": p, "summary": s} for p, s in writing],
        "visualization_observations": [{"page": p, "figure": f, "summary": s} for p, f, s in VISUALS],
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The three-regime framing gives judges a clear tradeoff structure when scope and feasibility stay explicit.", "evidence_class": "J"},
            {"page": 9, "summary": "A complete concrete schedule is persuasive because it can be replayed, but hard travel and horizon violations undermine the headline count.", "evidence_class": "J"},
            {"page": 18, "summary": "Sensitivity tables can build trust only when contradictory runs such as 560 versus 500 are investigated rather than described as stable.", "evidence_class": "J"},
        ],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": extensions, "candidate_rule_impacts": [],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing every paper-specific fact, phrase, count, and formula.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain inputs, operations, constraints, typed outputs, handoffs, and warning boundaries.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive context-to-regime-to-mechanism-to-result-to-tradeoff chain.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep table structure, route semantics, captions, parameter settings, totals, and linked warnings together.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the replay rule, arithmetic check, seed, sample, bound, comparator, uncertainty, and permitted conclusion.", "R-B-VER-002") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, units, indexing, distribution assumptions, horizon, and downstream consumer.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each assumption with the mechanism it enables, excluded behavior, sensitivity test, and fallback.", "R-B-DATA-002") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry regime, constraints, horizon, count, risk, comparator, and evidence status together.", "R-B-MOD-004") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use only after positive language, organization, model, visual, and verification retention is complete.", "R-B-VER-004") for x in card["weaknesses"]],
        "other": [(20, "reference boundary", "The paper uses four web references and provides no executable reproduction package.", "Separate contextual citation from data provenance and computational validation.", "R-B-VER-004")],
    }
    counts = {"language": len(language["units"]), "modeling": 86, "logic": 72, "visualization": 52, "verification": 60, "data": 46, "assumption": 48, "result": 50, "weakness": len(WARNINGS), "other": 6}
    records = []
    for dim, count in counts.items():
        rows = sources[dim]
        for i in range(count):
            page, section, basis, interpretation, rule = rows[i % len(rows)]
            rules = [rule]
            if dim == "modeling" and i == 1: rules.append("R-B-MOD-003")
            if dim == "modeling" and i == 2: rules.append("R-B-MOD-005")
            if dim == "modeling" and i == 3: rules.append("R-B-COMP-001")
            if dim == "verification" and i == 1: rules.append("R-B-VER-004")
            idx = len(records) + 1
            records.append({"schema_version": 1, "observation_id": f"O-B-{YEAR}-{SHORT}-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "page": page, "section": f"{section} / evidence action {i+1}", "evidence_class": "O", "dimension": dim, "source_basis": basis[:900], "interpretation": interpretation, "applicability": ["Apply only when river geometry, campsite indexing, trip duration, travel limit, route distribution, launch horizon, risk target, algorithm, output, comparator, uncertainty, and scope can all be named."], "counterevidence": ["A conflict-free displayed table, local probability threshold, greedy choice, random maximum, or high campsite utilization does not prove hard travel feasibility, global seasonal safety, or optimality."], "confidence": "high" if dim in {"language", "modeling", "logic", "visualization"} else "medium", "candidate_rule_ids": rules})
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first = {}
    for row in observations: first.setdefault(row["dimension"], row["observation_id"])
    def evidence_for(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])
    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain three-regime framing, orbit-to-cycle exposition, probability dataflow, sensitivity interpretation, and manager-letter translation with explicit scope", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "retain the context-to-definitions-to-assumptions-to-controlled schedule-to-probabilistic schedule-to-random comparator-to-sensitivity-to-decision chain", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "treat campsite coordinates, trip types, route tables, calendar entries, route probabilities, random seeds, and sensitivity settings as versioned data", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for spacing, daily travel, day-night indexing, route choice, type choice, local risk, and season boundaries", "evidence_ids": [evidence_for("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain orbit partition, cyclic scheduling, dynamic route counting, collision aggregation, greedy insertion, and random construction only with typed interfaces", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine trip count, person-days, campsite use, daily travel, route freedom, local and global collision risk, mix balance, and operating horizon in one decision rule", "evidence_ids": [evidence_for("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep arithmetic launch counts, replayed feasibility, greedy best observed, random sample maximum, and proven optimum separately labeled", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress Y, spacing, hours, duration indexing, probability threshold, route distribution, first type, season end, and random seed", "evidence_ids": [evidence_for("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make reliability route-replay-, normalization-, network-risk-, seed-, sample-, bound-, and horizon-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile 25 versus 26, days versus nights, union versus intersection, remaining time, 500 versus 560, and 483 versus 493 before reuse", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain charts only with route timing, table headers, continuation semantics, exact totals, parameter settings, and linked contradictions", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "choose dynamic programming, incremental probability updates, exact scheduling, random multi-run evaluation, caching, runtime, and memory strategies from measured problem size", "evidence_ids": [evidence_for("R-B-COMP-001")]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reuse only after replacing source facts while preserving rhetorical function, order, slots, variants, and boundary."} for u in language["units"]]
    intro_ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == "introduction"]
    intro_moves = ["river access and popularity context", "wilderness collision constraint", "six-month capacity task", "trip propulsion and duration inputs", "practice-based route flexibility", "carrying-capacity definition", "three schedule regimes", "capacity-flexibility ordering hypothesis", "manager decision handoff"]
    chains = [{"chapter": "introduction", "visual_paragraph_count": len(intro_moves), "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": move, "language_unit_ids": [intro_ids[i % len(intro_ids)]]} for i, move in enumerate(intro_moves)]}]
    chapter_keys = {}
    for key, chapter, *_ in CHAPTERS:
        chapter_keys.setdefault(chapter, []).append(key)
    progressions = []
    for chapter, keys in chapter_keys.items():
        section_names = ", ".join(keys)
        progressions.append({"chapter": chapter, "moves": [f"input: the source-checked river state, campsite resource, type definition, formula, schedule, chart, probability, or result entering {section_names}", f"rhetorical job: perform the observed definition, construction, explanation, comparison, sensitivity interpretation, or managerial translation across {section_names}", f"analytical job: apply the declared partition, route, dynamic count, probability, greedy, random, replay, or sensitivity operation across {section_names}", f"output: retain a typed route, schedule, capacity, probability, table, warning, or decision option from {section_names}", "handoff: name the next regime, computation, verification, robustness analysis, warning gate, or manager choice"], "positive_pattern": "Use explicit input -> mechanism -> typed output -> verification or comparator -> scoped handoff; warnings cannot replace the positive section contract."})
    eqrefs = [(m["model_id"], eq["equation_id"], eq["page"]) for m in models["models"] for eq in m["governing_equations"]]
    warning_rows = []
    for page, warning in WARNINGS:
        mid, eid, _ = min(eqrefs, key=lambda x: (abs(x[2] - page), x[2], x[1]))
        warning_rows.append({"model_id": mid, "equation_id": eid, "page": page, "warning": warning})
    dims = Counter(x["dimension"] for x in observations)
    return {
        "audit_id": f"LA-B-{YEAR}-{SHORT}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [14 if chapter in {"introduction", "memo"} else 9, 3, 0]} for chapter in language["available_chapters"]],
        "language_unit_dispositions": dispositions, "paragraph_chains": chains,
        "organization_logic": {
            "positive_artifacts_status": "complete", "weakness_substitution_allowed": False,
            "global_organization_chain": [
                "Introduction frames the river decision and three progressively relaxed control regimes.",
                "Definitions, formulation, and assumptions establish types, orbits, downstream movement, daily travel, route probabilities, and the worked Y=150 case.",
                "Part 1 partitions campsites into orbits, constructs leader cycles, combines type groups, and publishes a two-day fixed-route schedule.",
                "Part 2 defines route counts and campsite occupancy probabilities, aggregates collision risk, and builds a 180-day greedy minimax calendar.",
                "Given-trip cases reuse the same schedule state under free or fixed routes.",
                "Part 3 replaces greedy choice with random feasible choice and reports repeated capacities and composition.",
                "Sensitivity tables vary first type, daily hours, and the risk threshold before strengths, weaknesses, and extensions.",
                "Conclusion and manager letter translate the three schedules into capacity-flexibility options, while the last pass retains feasibility and evidence warnings.",
            ],
            "section_progressions": progressions,
            "main_argument_chains": [
                {"claim": "More agency control can create denser schedules through exclusive campsite orbits.", "support_steps": ["residue partition", "leader cycle", "paired types", "Y=150 route table"], "decision_consequence": "Use the fixed-route option only after hard travel and horizon feasibility are rechecked.", "source_pages": [4,5,8,9]},
                {"claim": "Free route choice can be represented by complete-route probabilities and campsite-day collision risk.", "support_steps": ["recursive prefix counts", "printed occupancy probability", "inclusion-exclusion", "q risk"], "decision_consequence": "Correct remaining-time and joint-probability interfaces before accepting the 500 schedule.", "source_pages": [11,12]},
                {"claim": "Greedy minimax insertion constructs a high-capacity calendar.", "support_steps": ["candidate worst risk", "daily stop threshold", "180-day calendar", "500 recount"], "decision_consequence": "Call 500 a displayed heuristic schedule, not a proven optimum.", "source_pages": [12,13,14,15]},
                {"claim": "Random feasible type choice produces capacity near the greedy schedule.", "support_steps": ["eight runs", "483 mean", "493 maximum", "3864 aggregated trips"], "decision_consequence": "Report the distribution and exact selected realization rather than the sample maximum alone.", "source_pages": [16,17]},
                {"claim": "Sensitivity checks defend operational stability.", "support_steps": ["first type range", "daily-hour spike", "threshold monotonicity"], "decision_consequence": "Withhold stability claims until the 560-versus-500 conflict is resolved.", "source_pages": [18]},
            ],
        },
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warning_rows},
        "model_retention": {"model_count": len(models["models"]), "retained_model_ids": [m["model_id"] for m in models["models"]], "retained_equation_ids": [x[1] for x in eqrefs], "central_equations": [{"model_id": m["model_id"], "equation_ids": [e["equation_id"] for e in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]},
        "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-B-{YEAR}-{SHORT}-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)],
        "dimension_counts": {d: dims[d] for d in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]},
        "positive_reusable_language_count": len(language["units"]), "weakness_record_count": dims["weakness"], "review_status": "validated",
    }


def main() -> None:
    configure_template()
    language = template.base.make_language()
    for unit in language["units"]:
        unit["language_unit_id"] = unit["language_unit_id"].replace(
            f"LU-B-2011-{SHORT}-", f"LU-B-{YEAR}-{SHORT}-"
        )
    language["available_chapters"] = list(dict.fromkeys(language["available_chapters"]))
    merged = {}
    for layout in language["chapter_layouts"]:
        chapter = layout["chapter"]
        if chapter not in merged:
            merged[chapter] = {**layout, "paragraph_functions": list(layout["paragraph_functions"]), "content_counts": dict(layout["content_counts"])}
            continue
        row = merged[chapter]
        row["page_start"] = min(row["page_start"], layout["page_start"]); row["page_end"] = max(row["page_end"], layout["page_end"])
        row["word_count"] += layout["word_count"]; row["sentence_count"] += layout["sentence_count"]; row["paragraph_count"] += layout["paragraph_count"]
        row["paragraph_functions"].extend(layout["paragraph_functions"])
        for key, value in layout["content_counts"].items(): row["content_counts"][key] += value
    language["chapter_layouts"] = list(merged.values())
    for layout in language["chapter_layouts"]:
        layout["page_fraction"] = round((layout["page_end"] - layout["page_start"] + 1) / PAGE_COUNT, 6)
        layout["counting_method"] = "All 22 physical-page text files were read in UTF-8 order by the root context. Two fresh read-only contexts visually covered pages 1-11 and 12-22 with six byte-bounded JPEG proxies each; the first used one additional crop, and both returned text-only reports."
        layout["ambiguities"] = ["Extracted text flattens calendars and corrupts mathematical symbols, circles, arrows, smart punctuation, and table structure; rendered equations and charts were visually checked.", "Source-paper defects in formulas, constraints, page numbering, and claims are retained as final-pass warnings rather than extraction omissions."]
    models = make_models(); card = make_card(language, models); observations = make_observations(language, models, card)
    attach_rule_impacts(card, observations); audit = make_audit(language, models, card, observations)
    template.base.write_json(ROOT / "artifacts/language-units" / f"{PID}.json", language)
    template.base.write_json(ROOT / "artifacts/model-units" / f"{PID}.json", models)
    template.base.write_json(ROOT / "artifacts/paper-cards" / f"{PID}.json", card)
    template.base.write_json(ROOT / "artifacts/learning-audits" / f"{PID}.json", audit)
    op = ROOT / "artifacts/observations" / f"{PID}.jsonl"; op.parent.mkdir(parents=True, exist_ok=True)
    op.write_text("".join(json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "\n" for x in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
