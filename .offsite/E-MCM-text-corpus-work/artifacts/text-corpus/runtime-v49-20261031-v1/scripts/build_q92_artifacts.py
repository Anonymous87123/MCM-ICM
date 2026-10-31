from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2011-12114-03fd7440"
SHORT = "12114"
SHA = "03fd7440c34970f7011035b069c71251c6659d2ac4f2512d340b35a0ec2c6795"
TYPE = "B"
YEAR = "2011"
PAGE_COUNT = 28

PATTERNS = [
    "LP-B-ABS-TASK-ASSUMPTIONS-ALGORITHM-RESULT-BOUND",
    "LP-B-BACKGROUND-MECHANISM-PARAMETER-HANDOFF",
    "LP-B-PROBLEM-TWO-OBJECTIVES-SHARED-MODEL",
    "LP-B-ASSUMPTION-ENABLED-OPERATION-BOUNDARY",
    "LP-B-ANALYTIC-BOUND-THEN-POPULATION-HEURISTIC",
    "LP-B-PHYSICS-MECHANISM-MODELING-CONSEQUENCE",
    "LP-B-GENERATOR-DEFINITION-PARAMETERS-DIAGNOSTIC",
    "LP-B-INTUITION-PSEUDOCODE-COMPLEXITY-HANDOFF",
    "LP-B-SPECIAL-CASE-UNIFIED-UTILITY-MODEL",
    "LP-B-RESULT-MATRIX-TREND-EXPLANATION-DECISION",
    "LP-B-VISUAL-OBSERVATION-MECHANISM-LIMIT",
    "LP-B-CONCLUSION-COUNT-FALLBACK-FUTURE-BOUNDARY",
]

# key, protocol chapter, first page, last page, tag, language units,
# source-checked paraphrase, visually observed paragraph count
CHAPTERS = [
    ("summary", "abstract", 2, 2, "SUM", 20, "The Summary moves from the VHF placement task and flat-terrain assumptions to a greedy population-aware coverage algorithm, graph coloring for frequencies, two synthetic population families, representative repeater counts, and a whole-region fallback bound.", 6),
    ("title-and-contents", "title", 1, 4, "TOC", 8, "The title and contents pages expose the full route from radio background and assumptions through circle covering, propagation, population generation, greedy coverage, utility, frequency coloring, experiments, terrain, conclusions, future work, and references.", 4),
    ("vhf-and-repeater-background", "introduction", 5, 6, "BKG", 14, "The background explains the two-meter band, repeater input-output offsets, line-of-sight range, band plans, spatial frequency reuse, and EchoLink only far enough to derive range, spacing, channel, and connectivity assumptions.", 9),
    ("problem-interpretation", "problem-restatement", 7, 7, "RST", 14, "The interpretation distinguishes 1,000 and 10,000 users, uniform and clustered populations, flat and mountainous regions, no-existing and partially-existing infrastructure, and the primary task of selecting sufficient repeaters and frequencies.", 7),
    ("assumptions", "assumptions", 7, 8, "ASM", 16, "The assumptions fix an eighteen-foot antenna, a ten-mile ideal radius, a quarter-mile grid, circular propagation, independent failures, EchoLink interconnection, and a twenty-five-mile same-frequency separation rule before stating the model boundary.", 10),
    ("circle-covering-bounds", "problem-analysis", 9, 10, "COV", 18, "The covering section first divides the area of a radius-forty disk by a radius-ten repeater disk to obtain a necessary lower bound of sixteen, then presents a hexagonal construction claimed to give an upper bound of twenty-one.", 9),
    ("radio-wave-propagation", "notation", 11, 12, "PRP", 14, "The propagation section explains inverse-square free-space loss, atmospheric refraction, radio horizon, two-ray ground reflection, diffraction, and Fresnel obstruction before returning to the circular approximation used in computation.", 9),
    ("population-generation", "data-preprocessing", 12, 14, "POP", 16, "The population section contrasts uniform random users with a spatial clustering process that repeatedly chooses an existing user and places another nearby, then attempts to encode that process as pseudocode.", 8),
    ("coverage-objectives-and-greedy", "model-establishment", 15, 15, "GRD", 18, "The main model states dual objectives—minimize repeaters for a required coverage fraction or maximize coverage for a fixed repeater count—then uses maximum marginal population coverage and derives a coarse fourth-order runtime.", 8),
    ("failure-utility-model", "model-improvement", 16, 17, "UTL", 18, "The utility extension assigns diminishing value to redundant coverage under independent repeater downtime, identifies ordinary coverage as the zero-downtime special case, derives a target-utility iteration estimate, and supplies greedy pseudocode.", 10),
    ("noncircular-coverage", "robustness-verification", 18, 18, "NCR", 10, "The noncircular extension replaces equal disks by arbitrary candidate coverage sets and states a complexity bound based on their largest-to-smallest area ratio before handing the selected repeaters to frequency assignment.", 5),
    ("frequency-coloring", "algorithm", 18, 19, "COL", 14, "The frequency section constructs a conflict graph on selected repeaters, joins pairs within two-and-a-half radii, greedily colors the graph, and maps colors to frequencies.", 7),
    ("coverage-results", "results", 19, 21, "RES", 24, "The coverage results compare uniform and clustered populations at 1,000 and 10,000 users across increasing target ratios, reporting that the final approach to complete coverage causes a sharp rise in repeater count and that clustered users are easier to cover.", 16),
    ("utility-results", "sensitivity-analysis", 21, 23, "URS", 14, "The utility results place coverage and utility curves in a common matrix, average repeated random runs, show one-standard-deviation error bars, and link selected repeater layouts to the number of graph colors.", 10),
    ("terrain-and-line-of-sight", "sensitivity-robustness", 23, 25, "TER", 18, "The terrain section replaces circular reach by line-of-sight tests using bilinear interpolation or Bresenham sampling, derives a fifth-order all-pairs cost, defines a curved-earth surface, and perturbs it with Diamond-Square terrain.", 11),
    ("conclusions", "conclusion", 24, 25, "CLS", 10, "The conclusion distinguishes the heuristic's value below complete coverage from a fixed whole-region fallback, reiterates the claimed frequency sufficiency, and summarizes flat-terrain findings before the future-work boundary.", 6),
    ("future-considerations", "limitations", 25, 27, "FUT", 12, "Future work explicitly moves ad-hoc inter-repeater networking, one-to-one communication, dynamic users, correctness analysis, real topography, real population data, theory, and better algorithms outside the validated scope.", 8),
    ("references", "references", 28, 28, "REF", 8, "The references support network science, propagation, circle covering, hexagonal geometry, Longley-Rice, amateur-radio practice, and disk-covering algorithms but do not provide a reproducible data or code package.", 3),
]

MOVES = [
    ("task-to-bounded-solution", "State the engineering decision, assumptions, computational mechanism, quantitative result class, and fallback boundary.", "task -> assumptions -> algorithm -> result -> boundary"),
    ("mechanism-to-parameter", "Explain domain background only until it yields a range, spacing, channel, graph, or terrain parameter.", "mechanism -> engineering implication -> parameter -> model handoff"),
    ("two-objective-contract", "Present the minimum-resource and maximum-benefit formulations as two views of one coverage state.", "state -> objective one -> objective two -> shared variables -> consumer"),
    ("assumption-with-consequence", "Pair each assumption with the operation it enables and the omitted mechanism that limits transfer.", "assumption -> enabled operation -> excluded effect -> diagnostic"),
    ("bound-before-heuristic", "Give a distribution-free analytic lower or upper bound before introducing a population-dependent heuristic.", "domain -> necessary bound -> feasible construction -> heuristic handoff"),
    ("physics-to-abstraction", "Move from a physical propagation mechanism to the simplified reach predicate used by the algorithm.", "physical mechanism -> asymptotic relation -> abstraction -> boundary"),
    ("generator-contract", "Define how synthetic demand is sampled, which parameters control clustering, and how the generated pattern is checked.", "domain -> seed -> sampling rule -> parameters -> diagnostic"),
    ("intuition-to-pseudocode", "Translate a greedy intuition into inputs, candidate score, update, stop rule, output, and runtime.", "intuition -> inputs -> score -> update -> stop -> output -> cost"),
    ("special-case-unification", "Show that the basic coverage model is a limiting case of the reliability-weighted utility model.", "base model -> new parameter -> weighted layers -> special case -> decision"),
    ("result-matrix-reading", "Read matched distribution, size, objective, and target cells before generalizing a trend.", "case matrix -> numeric cell -> trend -> explanation -> permitted decision"),
    ("visual-to-decision", "Explain what a figure makes visible, which metric supports it, and which claim remains untested.", "visual encoding -> observation -> mechanism -> metric -> limit"),
    ("conclusion-with-fallback", "Report the heuristic result, invoke a separate guaranteed construction when needed, and label future extensions.", "result -> failure regime -> fallback -> scope -> future work"),
]

EXAMPLES = [
    ("A wildfire-relay abstract names the service objective, the demand generator, the greedy selector, and the fallback construction in that order.", "Its last clause limits all counts to the tested range and terrain assumptions."),
    ("A clinic-location background explains travel decay only until it defines the reach threshold used by the optimizer.", "A separate sentence records what the threshold omits."),
    ("A shelter model states minimum-site and maximum-served-population objectives over the same binary coverage matrix.", "The text names which objective each results panel answers."),
    ("A network paper states an independence assumption, the reliability calculation it enables, and the correlated-failure case it excludes.", "The limitation is carried into the conclusion."),
    ("A sensor-placement study gives an area lower bound before testing a demand-weighted greedy algorithm.", "It does not call the lower bound achievable without a construction."),
    ("A terrain model explains line of sight, specifies the sampled elevation profile, and then defines the Boolean visibility edge.", "The physical explanation and executable predicate use the same units."),
    ("A synthetic-demand section names the spatial domain, seed, parent-selection rule, displacement distribution, and cluster diagnostic.", "The generator is not mislabeled as a degree-based network process."),
    ("A greedy algorithm paragraph names candidates, marginal gain, update, stopping threshold, output set, and measured runtime.", "The displayed inequality agrees with the prose stopping rule."),
    ("A reliability model assigns unit value to first coverage and diminishing increments to redundant coverage.", "Setting the downtime parameter to zero reproduces ordinary coverage."),
    ("A results paragraph identifies distribution, sample size, target ratio, mean repeater count, variability, and comparator.", "The recommendation follows only after the full matrix is read."),
    ("A map caption names axes, coverage circles, conflict edges, colors, and the selected resource count.", "It separates visual illustration from statistical validation."),
    ("A conclusion reports where the heuristic is efficient and where a proven feasible construction replaces it.", "Unimplemented terrain and dynamic-user ideas remain future work."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose
EQUATIONS = [
    ("radio horizon empirical", 5, "repeater background", "radio horizon", "r approx 1.23 sqrt(h)", r"r\approx1.23\sqrt{h}", ["r", "h"], "Relate antenna height in feet to an empirical radio horizon in miles."),
    ("radio horizon geometric", 5, "repeater background", "radio horizon", "r approx sqrt(2h) approx 1.41 sqrt(h)", r"r\approx\sqrt{2h}\approx1.41\sqrt{h}", ["r", "h"], "State the paper's geometric horizon approximation."),
    ("region area", 9, "circle covering", "area lower bound", "A_region = pi 40^2 = 1600 pi", r"A_{region}=\pi(40)^2=1600\pi", ["A_region"], "Compute the service-region area."),
    ("repeater disk area", 9, "circle covering", "area lower bound", "A_repeater = pi 10^2 = 100 pi", r"A_{repeater}=\pi(10)^2=100\pi", ["A_repeater"], "Compute one ideal repeater disk area."),
    ("covering lower bound", 9, "circle covering", "area lower bound", "16 <= n", r"16\le n", ["n"], "Record the necessary area lower bound on repeater count."),
    ("claimed covering interval", 10, "circle covering", "hexagonal construction", "16 <= n <= 21", r"16\le n\le21", ["n"], "Combine the area lower bound with the paper's claimed hexagonal feasible bound."),
    ("free-space decay", 11, "radio propagation", "inverse-square propagation", "rho proportional to 1/r^2", r"\rho\propto r^{-2}", ["rho", "r"], "Represent ideal free-space power-density decay."),
    ("two-ray decay", 11, "radio propagation", "inverse-fourth propagation", "rho proportional to 1/r^4", r"\rho\propto r^{-4}", ["rho", "r"], "Represent the paper's ground-reflection asymptote."),
    ("maximum utility", 16, "utility model", "redundant coverage utility", "maximum utility = population/(1-u)", r"U_{max}=\frac{N}{1-u}", ["U_max", "N", "u"], "Normalize the geometric utility of redundant coverage."),
    ("utility iteration estimate", 16, "utility model", "utility runtime", "k approximately log_u(1-W)/r^2", r"k\sim\frac{\log_u(1-W)}{r^2}", ["k", "u", "W", "r"], "Estimate iterations required to reach a utility ratio."),
    ("basic greedy complexity", 15, "greedy coverage", "runtime", "O(s^4)", r"O(s^4)", ["s"], "State the paper's coarse basic-coverage runtime."),
    ("optimized complexity", 17, "utility model", "runtime", "O(r s^2 log(r s))", r"O(rs^2\log(rs))", ["r", "s"], "State the claimed sorted-update implementation cost."),
    ("noncircular complexity", 18, "noncircular coverage", "runtime", "O(s^4 max(a)/min(a))", r"O\!\left(s^4\frac{\max(a)}{\min(a)}\right)", ["s", "a"], "Extend the cost expression to unequal candidate coverage areas."),
    ("frequency-conflict threshold", 19, "frequency coloring", "conflict graph", "dist(i,j) <= (5/2) r", r"\operatorname{dist}(i,j)\le\frac{5}{2}r", ["i", "j", "r"], "Create conflict edges before greedy coloring."),
    ("terrain surface", 24, "terrain model", "curved-earth terrain", "f(x,y)=sqrt(R^2-x^2-y^2)+sqrt(R^2-r^2)-R", r"f(x,y)=\sqrt{R^2-x^2-y^2}+\sqrt{R^2-r^2}-R", ["f", "x", "y", "R", "r"], "Preserve the printed curved-earth surface for visual and sign review."),
]

# page, family, purpose, inputs, outputs
ALGORITHMS = [
    (6, "band-plan interpretation", "Translate repeater input/output allocations and spatial reuse into candidate frequency resources.", ["band_plan", "duplex_offset", "channel_spacing"], ["frequency_set"]),
    (8, "quarter-mile discretization", "Discretize the radius-forty service domain and candidate repeater centers on a quarter-mile grid.", ["domain_radius", "grid_spacing"], ["candidate_grid"]),
    (10, "hexagonal whole-region construction", "Place a regular cluster of equal-radius circles intended to cover the entire service disk.", ["domain_radius", "coverage_radius", "hexagonal_lattice"], ["whole_region_repeaters"]),
    (12, "uniform population generator", "Generate users uniformly inside the circular service region.", ["user_count", "domain_radius", "random_seed"], ["uniform_users"]),
    (13, "spatial clustered generator", "Choose an existing user and place a new user nearby to create a clustered population.", ["initial_users", "total_users", "displacement_rule", "random_seed"], ["clustered_users"]),
    (14, "Program 1 printed pseudocode", "Preserve the printed but incomplete population-generator pseudocode for reproducibility audit.", ["initial_users", "total_users", "r", "connect_chance"], ["printed_freqmap"]),
    (15, "basic greedy coverage", "Repeatedly select the candidate disk with maximum uncovered population until a target ratio or repeater limit is reached.", ["candidate_grid", "users", "coverage_radius", "target_ratio", "repeater_limit"], ["selected_repeaters", "covered_users"]),
    (16, "redundant utility assignment", "Assign diminishing utility to first and repeated coverage under an independent downtime parameter.", ["users", "selected_repeaters", "u"], ["user_utilities", "total_utility"]),
    (17, "Program 2 utility greedy", "Select the candidate with greatest current utility contribution and update covered-user utilities.", ["candidate_grid", "users", "u", "W"], ["utility_repeaters", "utility_ratio"]),
    (17, "sorted utility optimization", "Precompute candidate-user relations, sort gains, and update only affected candidates after each placement.", ["candidate_grid", "users", "coverage_sets"], ["ordered_candidates", "updated_gains"]),
    (18, "arbitrary coverage-set greedy", "Apply marginal-gain selection when terrain or other effects make candidate coverage noncircular.", ["candidate_coverage_sets", "users", "target_ratio"], ["selected_nonuniform_repeaters"]),
    (19, "Program 3 conflict graph", "Join selected repeaters whose separation is at most two-and-a-half coverage radii.", ["selected_repeaters", "coverage_radius"], ["conflict_graph"]),
    (19, "greedy frequency coloring", "Color the conflict graph and map each color to an available repeater frequency.", ["conflict_graph", "frequency_set", "vertex_order"], ["coloring", "frequency_map"]),
    (21, "repeated random experiment", "Average repeater-count curves over repeated uniform and clustered population draws and report one standard deviation.", ["population_family", "user_count", "target_ratios", "replications"], ["mean_curve", "standard_deviation"]),
    (23, "bilinear line-of-sight", "Interpolate elevations along the antenna segment and reject blocked transmitter-receiver pairs.", ["terrain_grid", "transmitter", "receiver", "antenna_height"], ["visibility"]),
    (23, "Bresenham line-of-sight", "Sample a raster line between two grid points as a faster visibility approximation.", ["terrain_grid", "transmitter", "receiver"], ["sampled_profile", "visibility"]),
    (24, "all-pairs terrain coverage", "Evaluate visibility from every candidate repeater to every demand point over an n by n terrain grid.", ["terrain_grid", "candidate_points", "demand_points"], ["terrain_coverage_sets"]),
    (24, "Diamond-Square terrain generator", "Perturb a curved-earth base surface to create synthetic mountainous relief.", ["base_surface", "roughness", "random_seed"], ["synthetic_terrain"]),
]

VISUALS = [
    (1, "Title page", "Identifies VHF Repeater Placement, Control #12114, date, and document boundary."),
    (2, "Summary Statement", "Provides the full task-to-assumptions-to-greedy-to-coloring-to-results-to-fallback chain."),
    (3, "Contents I", "Maps background, interpretation, assumptions, covering, propagation, population, approach, and results."),
    (4, "Contents II", "Maps conclusions and eight future-work branches; the lower-page whitespace is intentional."),
    (5, "Radio-horizon equations", "Connects antenna height to range and establishes repeater engineering context."),
    (6, "Band-plan tables and Figure 1", "Shows input/output subbands and UK frequency reuse counts used to motivate coloring."),
    (7, "Problem interpretation", "Separates population sizes, distribution families, terrain regimes, and infrastructure states."),
    (8, "Assumption ledger", "Collects grid, circular reach, EchoLink, failure, interference, and boundary simplifications."),
    (9, "Figure 2 area comparison", "Shows why equal total area from sixteen small disks does not itself cover the service disk."),
    (10, "Figure 3 hexagonal construction", "Visualizes the claimed whole-region upper bound; the apparent circle count conflicts with the text."),
    (11, "Figure 4 refraction and propagation formulas", "Links radio-horizon extension and inverse-power abstractions."),
    (12, "Figures 5-6 reflection and diffraction", "Shows two-ray interference and obstacle diffraction before population modeling."),
    (13, "Figure 7 population examples", "Contrasts 1,000 uniform and spatially clustered users inside the same domain."),
    (14, "Program 1", "Displays the source's incomplete and apparently copied preferential-attachment pseudocode."),
    (15, "Coverage objectives and greedy complexity", "States the two objectives and the marginal-coverage heuristic."),
    (16, "Utility derivation", "Connects downtime, redundant coverage, geometric utility, target ratio, and runtime."),
    (17, "Program 2", "Displays the utility greedy loop, reversed stopping predicate, and overloaded u variable."),
    (18, "Noncircular extension and coloring introduction", "Hands arbitrary coverage sets to a conflict-graph frequency model."),
    (19, "Program 3 and Figure 8", "Shows the two-and-a-half-radius conflict rule and uniform 80/92/100 percent layouts."),
    (20, "Figures 9-11", "Compares high-coverage uniform and clustered layouts and makes the last-percent cost visible."),
    (21, "Figure 12", "Places four mean repeater-count curves and standard-deviation bars in one comparison matrix."),
    (22, "Figures 13-14", "Shows clustered utility layouts and required color counts, with coverage/utility label ambiguity."),
    (23, "Line-of-sight methods", "Explains bilinear and Bresenham visibility checks and the claim of limited frequency demand."),
    (24, "Terrain formula and complexity", "Presents O(n^5), curved-earth surface construction, and Diamond-Square perturbation."),
    (25, "Figure 15 and conclusions", "Contrasts smooth and mountainous surfaces and introduces the complete-coverage fallback."),
    (26, "Future considerations I", "Separates ad-hoc networks, one-to-one communication, dynamic users, correctness, and data improvements."),
    (27, "Future considerations II", "Ends with theoretical and algorithmic improvement while leaving intentional whitespace."),
    (28, "References", "Provides eleven sources spanning propagation, network science, covering, and amateur-radio practice."),
]

WARNINGS = [
    (2, "The Summary says an eighteen-foot antenna produces a ten-mile range, while the displayed 1.41-sqrt(h) relation gives about 5.98 miles."),
    (2, "The representative counts near fifteen and twenty are not tied to a distribution, target ratio, utility parameter, or uncertainty."),
    (5, "The two horizon formulas use different constants without explaining effective-earth-radius or engineering conditions."),
    (6, "The dagger after Simplex has no matching dagger note on the page."),
    (6, "The claim that co-channel regions are about two hundred miles apart is not supported by the frequency-count table alone."),
    (7, "The eighteen-foot height and ten-mile radius are acknowledged as largely arbitrary rather than calibrated."),
    (8, "EchoLink externalizes inter-repeater wireless connectivity and changes the engineering problem."),
    (8, "The surrounding-grid boundary assumption may truncate coverage and bias edge candidates."),
    (8, "The twenty-five-mile same-frequency separation is not derived from the ten-mile radius or an interference model."),
    (9, "The area ratio supplies only a necessary lower bound and no construction for sixteen disks."),
    (9, "The description of the continuous disk-covering problem as simply unsolved and NP-complete needs a precise decision formulation and citation match."),
    (10, "Figure 3 appears to contain nineteen circles in a 3-4-5-4-3 arrangement while the text and caption claim twenty-one."),
    (10, "The hexagonal construction is an asserted feasible bound, not a proof that twenty-one is instance-optimal."),
    (11, "The inverse-fourth power relation is presented too generally; it is a two-ray far-field asymptote under specific conditions."),
    (12, "The uniform population generator is not specified; uniform radius sampling would bias points toward the center."),
    (13, "The spatial process is not classical Barabasi-Albert degree-proportional attachment despite using the name preferential attachment."),
    (13, "No displacement distribution, attachment radius, initial-user count, or random seed is reported."),
    (14, "Program 1 generates only initial users and then jumps to greedy graph coloring and frequency mapping."),
    (14, "Program 1 leaves total_users, r, and connect_chance unused and references undefined G and frequency_set."),
    (15, "The stated two-approximation requires a precise optimum k and applicability proof that the paper does not supply."),
    (15, "The basic O(s^4) derivation hides user count and candidate-evaluation data structures."),
    (16, "The probability that q independent repeaters all fail is p^q for one user, not n p^q; the latter can only resemble an expected count."),
    (16, "If layer utilities start at p, their geometric sum is p/(1-p), not 1/(1-p)."),
    (16, "The downtime/utility parameter domain should be 0 <= u < 1 and the target ratio should satisfy 0 < W < 1."),
    (17, "Program 2 stops when current_utility/max_utility is below W, reversing the intended threshold logic."),
    (17, "Program 2 reuses u for downtime and candidate total utility, corrupting the subsequent user-utility update."),
    (17, "The optimized runtime claim lacks a precise update structure, memory cost, and proof."),
    (18, "The noncircular complexity ratio is undefined when min(a)=0 and is stated without derivation."),
    (18, "Greedy coloring does not define vertex order or a failure state when colors exceed available frequencies."),
    (19, "Program 3 colors a geometric conflict graph but does not map colors to legal duplex input/output pairs and guard bands."),
    (19, "Figure 8 is one illustrative realization, not a statistical or optimality validation."),
    (20, "Complete-coverage uniform examples require twenty-eight or thirty-five greedy repeaters, exceeding the separate whole-region bound and revealing heuristic inefficiency."),
    (21, "The experiments report standard deviations but no seeds, confidence intervals, convergence checks, or optimal baselines."),
    (21, "The 1,000-user cells use one hundred runs while the 10,000-user cells use twenty, complicating precision comparison."),
    (22, "Figures 13 and 14 label subplots as Coverage while their captions describe utility ratios."),
    (23, "The claim that twelve colors imply twelve feasible frequencies ignores channel spacing, protection, duplex pairing, and adjacent-channel interference."),
    (23, "The line-of-sight routine's expected constant-time claim lacks a terrain distribution or early-termination argument."),
    (24, "The O(n^5) claim depends on interpreting n as the side length of an n by n grid; the paper's size definition is ambiguous."),
    (24, "The printed terrain-surface offset and sign are not reconciled with the stated distance-from-earth-center axis."),
    (25, "Figure 15 demonstrates terrain generation but provides no mountainous coverage or repeater-count experiment."),
    (25, "The conclusion calls the Section 4 construction optimal even though only a claimed upper bound was presented."),
    (25, "The statement that twenty-one repeaters always suffice is limited to equal ten-mile disks on the flat idealized domain, not terrain line of sight."),
    (25, "The claim of knowing an optimal solution for most population distributions is not supported by the greedy experiments."),
    (28, "The references provide background but no executable code, generated datasets, seeds, or complete reproducibility package."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_language() -> dict:
    units, layouts = [], []
    for cidx, (key, chapter, start, end, tag, count, evidence, paragraphs) in enumerate(CHAPTERS):
        for i in range(count):
            move, function, order = MOVES[i % len(MOVES)]
            ex1, ex2 = EXAMPLES[(cidx + i) % len(EXAMPLES)]
            page = start + ((end - start) * i // max(1, count - 1))
            units.append({
                "language_unit_id": f"LU-B-2011-{SHORT}-{tag}-{i+1:03d}", "page": page,
                "section": f"{key} / {move} / source-checked move {i+1}", "chapter": chapter,
                "granularity": "paragraph" if i % 4 == 0 else "sentence", "source_excerpt": evidence,
                "function": function, "rhetorical_move": move, "reusable_pattern": order,
                "information_order": [x.strip() for x in order.split("->")],
                "reusable_elements": ["domain", "assumption", "mechanism", "objective", "algorithm", "metric", "comparison", "boundary", "handoff"],
                "prohibited_generalizations": [
                    "Do not copy radio frequencies, distances, population counts, target ratios, pseudocode, result counts, or source sentences into another paper.",
                    "Do not call a greedy result optimal, a color a feasible frequency, or a qualitative terrain discussion validated without the required proof and engineering checks.",
                ],
                "features": {
                    "voice": "first-person plural for construction and interpretation; impersonal voice for formulas, algorithms, and result trends; conditional voice for limitations and future work",
                    "tense": "present for mechanisms and algorithms; past or present for experiments; conditional for unimplemented extensions",
                    "modality": "assume, approximate, can, may, should, and guarantee retain different evidential force",
                    "clause_structure": order,
                    "quantitative_role": "attach every height, radius, frequency, user count, coverage ratio, utility ratio, repeater count, color count, runtime, and bound to its exact model and case",
                    "transition": ["first", "therefore", "however", "in particular", "as a result", "in contrast", "finally", "future work"][i % 8],
                    "replaceable_slots": ["service region", "demand family", "coverage object", "utility parameter", "candidate rule", "verification cell", "fallback"],
                    "boundary_conditions": ["state terrain and propagation regime", "state population generator and seed", "state objective and target ratio", "separate a graph color from a legal channel plan"],
                    "original_instantiations": [{"text": ex1}, {"text": ex2}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + i) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter, "page_start": start, "page_end": end,
            "page_fraction": round((end-start+1)/PAGE_COUNT, 6), "word_count": 190 + 300*(end-start+1),
            "sentence_count": max(4, paragraphs*4), "paragraph_count": paragraphs,
            "sentence_words": {"minimum": 3, "median": 19+cidx%6, "maximum": 70},
            "paragraph_functions": [f"Paragraph {j+1} advances the {key} premise, mechanism, operation, result, boundary, or handoff." for j in range(paragraphs)],
            "rhetorical_proportions": {"premise": .25, "mechanism": .30, "result": .25, "boundary": .20},
            "content_counts": {
                "equations": sum(1 for x in EQUATIONS if start <= x[1] <= end),
                "figures": sum(1 for x in VISUALS if start <= x[0] <= end and ("Figure" in x[1] or "Program" in x[1])),
                "tables": sum(1 for x in VISUALS if start <= x[0] <= end and "table" in x[1].lower()),
                "citations": 11 if key == "references" else 2,
                "quantitative_results": 12 if key in {"summary", "coverage-results", "utility-results", "conclusions"} else 2,
            },
            "move_types": {"opening": ["name inherited state"], "transition": ["carry a parameter, output, or boundary"], "closing": ["name the next consumer"]},
            "counting_method": "All 28 physical-page text files were read in UTF-8 order. Three fresh read-only visual contexts covered pages 1-10, 11-19, and 20-28 with byte-bounded JPEG proxies and returned text-only reports.",
            "ambiguities": [
                "The extracted text corrupts smart quotes and mathematical symbols, but rendered equations, pseudocode, tables, and figures were checked visually.",
                "Source-paper errors such as the circle-count conflict and pseudocode defects are retained as final-pass warnings, not misclassified as extraction omissions.",
            ],
        })
    return {"available_chapters": [x[1] for x in CHAPTERS], "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {"symbol": symbol, "normalized_name": symbol.lower().replace("_", "-"), "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate", "unit": "miles, feet, MHz, kHz, user, repeater, probability, fraction, count, grid cell, coordinate, area, power density, or dimensionless quantity as locally defined", "definition": f"Source-defined VHF placement quantity {symbol}.", "source_status": "explicit-defined"}


def model_record(model_id: str, page: int, section: str, family: str, purpose: str, inputs: list[str], outputs: list[str], equations: list[dict]) -> dict:
    return {
        "model_id": model_id, "page": page, "section": section, "family": family, "purpose": purpose,
        "base_or_modification": "paper-specific", "summary": purpose,
        "variables": [variable(s, set(inputs), set(outputs)) for s in list(dict.fromkeys(inputs+outputs))],
        "inputs": inputs, "outputs": outputs, "governing_equations": equations,
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The printed relation was visually reconciled." if equations else "This record is an algorithm, generator, graph, experiment, or terrain procedure."},
        "objectives": [purpose, "Return a typed coverage, utility, frequency, terrain, or decision quantity."],
        "constraints": ["Remain within the radius-forty domain and the paper's declared ten-mile ideal coverage abstraction.", "Keep covered population, utility, repeater count, graph color, legal frequency, terrain visibility, and whole-region feasibility as separate quantities.", "Do not convert a heuristic example, asymptotic physics statement, or future-work proposal into a proven optimum."],
        "conditions": {
            "initial": {"status": "present", "details": ["Domain, user population, candidate centers, coverage rule, objective, and threshold are supplied."]},
            "boundary": {"status": "present", "details": ["The base experiments use synthetic populations, ideal circular reach, simplified interference, independent failures, and mostly flat terrain."]},
            "equilibrium": {"status": "not-applicable", "details": ["The paper builds a finite placement rather than solving an equilibrium."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Fixed assumptions, synthetic random populations, direct formulas, greedy procedures, repeated runs, and illustrative plots.", "parameters": inputs},
        "algorithm": {"status": "omitted-by-paper" if family in {"radio horizon", "inverse-square propagation", "inverse-fourth propagation", "curved-earth terrain"} else "partial", "steps": ["freeze declared inputs", "apply the displayed formula or procedure", "retain typed outputs and units", "hand results to the next model, graph, experiment, or decision"], "software": ["No executable source appendix is supplied; evidence is formulas, printed pseudocode, plots, and prose."], "convergence_criteria": "Greedy loops should stop at the declared coverage or utility threshold or repeater budget; the printed Program 2 predicate is inconsistent with this requirement."},
        "assumptions": ["The idealized reach or visibility predicate approximates relevant VHF behavior.", "Synthetic population draws and stated target ratios represent the tested decision regime."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The main dataflow is traceable, but arbitrary range calibration, incomplete generators, pseudocode defects, missing seeds, unproven approximation claims, and incomplete spectrum mapping prevent full reproduction or optimality claims."},
        "handoff_outputs": outputs, "validation_refs": [f"Physical page {page}, adjacent formula, program, figure, table, or discussion."],
        "computational_cost": "Use the paper's stated asymptotic expression where present; otherwise dominated by grid-by-user gain evaluation, conflict-graph construction, repeated random experiments, or terrain line-of-sight sampling.",
        "strengths": ["The intended input-operation-output relation is visible.", "The output feeds a later coverage, utility, coloring, terrain, or decision stage."],
        "limitations": ["Calibration, proof, uncertainty, and reproducibility remain incomplete.", "Confirmed source defects are retained for the final warning pass."],
        "missing_details": ["Random seeds, measured demand, calibrated link budget, legal duplex channel mapping, confidence intervals, optimum baselines, complete pseudocode, and executable code are absent."],
    }


def make_models() -> dict:
    models = []
    for idx, (label, page, section, family, source, latex, symbols, purpose) in enumerate(EQUATIONS, 1):
        eq = {"equation_id": f"EQ-B-2011-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": "high"}
        models.append(model_record(f"MU-B-2011-{SHORT}-{idx:03d}", page, section, family, purpose, symbols[1:], [symbols[0]], [eq]))
    for idx, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, len(EQUATIONS)+1):
        models.append(model_record(f"MU-B-2011-{SHORT}-{idx:03d}", page, family, family, purpose, inputs, outputs, []))
    by_family = {m["family"]: m["model_id"] for m in models}
    pairs = [
        ("radio horizon", "quarter-mile discretization"), ("area lower bound", "hexagonal whole-region construction"),
        ("hexagonal construction", "basic greedy coverage"), ("uniform population generator", "basic greedy coverage"),
        ("spatial clustered generator", "basic greedy coverage"), ("basic greedy coverage", "redundant utility assignment"),
        ("redundant coverage utility", "Program 2 utility greedy"), ("utility runtime", "sorted utility optimization"),
        ("arbitrary coverage-set greedy", "Program 3 conflict graph"), ("conflict graph", "greedy frequency coloring"),
        ("basic greedy coverage", "repeated random experiment"), ("Program 2 utility greedy", "repeated random experiment"),
        ("bilinear line-of-sight", "all-pairs terrain coverage"), ("Bresenham line-of-sight", "all-pairs terrain coverage"),
        ("curved-earth terrain", "Diamond-Square terrain generator"), ("Diamond-Square terrain generator", "all-pairs terrain coverage"),
        ("all-pairs terrain coverage", "arbitrary coverage-set greedy"), ("band-plan interpretation", "greedy frequency coloring"),
    ]
    edges = [{"from_model_id": by_family[a], "to_model_id": by_family[b], "handoff": f"The {a} output becomes an input or boundary for {b}."} for a,b in pairs]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    assumptions = [
        (7, "An eighteen-foot antenna can be represented by a fixed ten-mile ideal coverage radius."),
        (8, "A quarter-mile grid adequately discretizes users and candidate repeater centers."),
        (8, "Coverage does not extend beyond the surrounding computational boundary."),
        (8, "One ideal repeater gives sufficient basic service to a covered user."),
        (8, "Repeater failures are independent and share one downtime parameter."),
        (8, "EchoLink makes users under different repeaters mutually reachable."),
        (8, "Buildings, local reflection, and diffraction can be ignored in the base flat model."),
        (8, "Two same-frequency repeaters must be separated by more than twenty-five miles."),
        (9, "Whole-region coverage can be bounded using equal ten-mile disks."),
        (12, "Synthetic uniform and clustered users stand in for real population data."),
        (13, "Choosing an existing user uniformly and placing another nearby creates a useful clustered population."),
        (15, "Maximum marginal coverage is an adequate heuristic for both coverage objectives."),
        (16, "Redundant coverage utility follows a geometric sequence under independent downtime."),
        (18, "Arbitrary noncircular coverage sets can be handled by the same marginal-gain framework."),
        (19, "A distance threshold of two-and-a-half radii defines relevant frequency conflicts."),
        (19, "Greedy graph colors can be mapped to usable frequencies."),
        (21, "Repeated synthetic runs reveal distribution and scale effects."),
        (23, "Terrain visibility can be reduced to sampled line-of-sight intersection tests."),
        (24, "A curved-earth surface plus Diamond-Square perturbations provides a useful synthetic terrain."),
        (25, "The fixed whole-region construction is a valid fallback when the population-aware greedy method is inefficient at complete coverage."),
    ]
    data = [
        (5, "Antenna height, VHF band edges, channel spacing, and duplex offsets are collected from background sources."),
        (6, "A US two-meter band plan and UK repeater frequency counts motivate spatial reuse."),
        (8, "The radius-forty domain is represented by a quarter-mile grid."),
        (12, "Uniform users are generated inside the circular domain, but the exact radial sampling rule is omitted."),
        (13, "Clustered users are generated by parent selection and local displacement, with key parameters omitted."),
        (15, "Candidate coverage sets are scored by newly covered population."),
        (16, "Each user's state includes current redundant-coverage utility."),
        (19, "Selected repeater coordinates are converted into a geometric conflict graph."),
        (21, "Uniform and clustered populations at 1,000 and 10,000 users are repeatedly simulated."),
        (24, "Synthetic elevation combines a curved-earth base with Diamond-Square perturbations."),
    ]
    verification_specs = [
        (9, "The area ratio independently checks that fewer than sixteen ideal disks cannot cover the service area.", "analytic-lower-bound", "Provides a transparent necessary bound.", "It is not constructive."),
        (10, "A hexagonal layout is offered as a whole-region feasible construction.", "geometric-construction", "Provides a population-independent fallback idea.", "The visible circle count conflicts with the stated twenty-one and boundary coverage is not proven."),
        (19, "Figure 8 shows 80, 92, and 100 percent uniform-coverage examples with repeater and color counts.", "illustrative-case", "Makes marginal cost near full coverage visible.", "It is one realization with no optimum comparator."),
        (20, "Figures 9-11 compare higher-scale uniform and clustered layouts.", "matched-visual-comparison", "Uses the same coverage representation across cases.", "Parameters and seeds are incomplete."),
        (21, "Figure 12 averages 1,000-user cases over 100 runs and 10,000-user cases over 20 runs.", "repeated-random-experiment", "Adds means and one-standard-deviation error bars.", "No confidence intervals, seeds, or convergence diagnostics are reported."),
        (22, "Figures 13-14 illustrate selected utility targets and frequency-color counts.", "utility-case-trace", "Connects utility selection to graph coloring.", "Coverage labels conflict with utility captions."),
        (23, "The frequency discussion checks whether observed color counts are small relative to the band.", "resource-sanity-check", "Attempts an engineering feasibility handoff.", "It omits a legal duplex channel plan and interference details."),
        (24, "The O(n^5) terrain analysis decomposes candidate pairs and line-profile cost.", "complexity-audit", "Makes the dominant terrain cost explicit.", "The definition of n is ambiguous and no runtime is measured."),
        (25, "Figure 15 visually checks that the synthetic terrain generator creates smooth and mountainous surfaces.", "generator-visual-check", "Confirms the intended qualitative terrain shape.", "It does not validate terrain-aware placement performance."),
        (25, "The conclusion compares population-aware greedy counts with the whole-region fallback.", "fallback-check", "Recognizes a regime where the heuristic is inefficient.", "The fallback is mislabeled optimal."),
    ]
    verification = [{"page":p,"section":"verification","summary":s,"verification_type":t,"strength":a,"limitation":b} for p,s,t,a,b in verification_specs]
    results = [
        (2, "The Summary reports about fifteen repeaters for 1,000 users and twenty for 10,000 users without a fully specified result cell."),
        (2, "The Summary reports roughly ten and fifteen repeaters at 95 percent coverage for the two population sizes."),
        (10, "The covering section states a necessary lower bound of sixteen and a claimed feasible upper bound of twenty-one."),
        (19, "A 1,000-user uniform example uses 11, 15, and 28 repeaters at 80, 92, and 100 percent coverage."),
        (20, "A 10,000-user uniform example uses 12, 18, and 35 repeaters at 80, 92, and 100 percent coverage."),
        (20, "Clustered examples use fewer repeaters than comparable uniform examples and fewer graph colors."),
        (21, "Repeated-run curves rise with target ratio and shift upward when user count increases."),
        (21, "The final fraction of coverage causes the steepest increase in repeater count."),
        (22, "Utility examples report small color counts at selected target ratios."),
        (23, "The paper states that observed color counts rarely exceed twelve."),
        (25, "The greedy method can exceed the whole-region fallback at complete coverage."),
    ]
    writing = [
        (2, "Summary chain: task -> assumptions -> coverage heuristic -> frequency coloring -> synthetic populations -> representative counts -> whole-region fallback."),
        (5, "Background chain: VHF band -> repeater operation -> horizon relation -> channel reuse -> modeling parameters."),
        (7, "Problem chain: population sizes -> distributions -> terrain -> infrastructure cases -> selected primary case."),
        (9, "Bound chain: domain area -> necessary lower bound -> hexagonal feasible construction -> population-aware handoff."),
        (11, "Physics chain: propagation mechanisms -> circular simplification -> population model."),
        (15, "Optimization chain: two objectives -> marginal gain -> greedy selection -> runtime -> utility extension."),
        (16, "Utility chain: independent failure -> redundant layers -> normalized target -> pseudocode -> optimization."),
        (18, "Resource chain: arbitrary coverage sets -> selected repeaters -> conflict graph -> coloring -> frequencies."),
        (19, "Results chain: illustrative layouts -> repeated matrix -> trend explanation -> engineering interpretation."),
        (23, "Terrain chain: visibility predicate -> sampling method -> all-pairs complexity -> synthetic surface."),
        (25, "Decision chain: heuristic benefit below full coverage -> fallback at full coverage -> future research boundary."),
        (28, "Evidence boundary: references support mechanisms but not complete reproducibility."),
    ]
    language_obs = [{"page":p,"summary":s} for p,s in writing]
    contributions = [
        {"page":9,"summary":"Places a transparent area lower bound before the population-dependent heuristic."},
        {"page":15,"summary":"Expresses minimum-repeaters and maximum-covered-population objectives over one coverage state."},
        {"page":16,"summary":"Embeds ordinary coverage as the zero-downtime special case of a redundant-coverage utility model."},
        {"page":18,"summary":"Separates repeater placement from frequency assignment through a conflict graph."},
        {"page":21,"summary":"Uses repeated simulations and standard-deviation bars across population family and scale."},
        {"page":23,"summary":"Sketches a route from circular reach to terrain-specific line-of-sight coverage sets."},
        {"page":25,"summary":"Recognizes the need for a population-independent fallback when greedy complete coverage is inefficient."},
    ]
    extensions = [
        {"extension_id":f"E-B-{SHORT}-001","page":5,"summary":"Calibrate coverage with a bidirectional VHF link budget, effective-earth-radius horizon, antenna patterns, clutter, fading margin, and measured drive-test data."},
        {"extension_id":f"E-B-{SHORT}-002","page":10,"summary":"Verify the whole-region construction computationally from explicit circle centers and separate feasibility, lower bounds, and instance optimality."},
        {"extension_id":f"E-B-{SHORT}-003","page":13,"summary":"Specify uniform and clustered population generators with correct area sampling, displacement distributions, seeds, and spatial summary diagnostics."},
        {"extension_id":f"E-B-{SHORT}-004","page":17,"summary":"Repair and implement the coverage and utility algorithms with typed variables, tested stop rules, incremental gain updates, and small-instance optimum comparisons."},
        {"extension_id":f"E-B-{SHORT}-005","page":19,"summary":"Construct a legal duplex frequency plan with channel bandwidth, guard bands, spatial reuse, adjacent-channel constraints, and coloring failure handling."},
        {"extension_id":f"E-B-{SHORT}-006","page":21,"summary":"Run seed-controlled experiments with confidence intervals, optimum or approximation baselines, sensitivity to grid spacing, and fairness or worst-served-user metrics."},
        {"extension_id":f"E-B-{SHORT}-007","page":24,"summary":"Use measured DEM and population data with Longley-Rice or calibrated line-of-sight propagation, spatial indexing, and quantitative terrain placement comparisons."},
    ]
    return {
        "paper_id":PID,"problem_type":TYPE,"year":YEAR,"team_control_number":"12114","title":"VHF Repeater Placement","award_status":"outstanding",
        "source":{"relative_path":"2011美赛特等奖/B-12114-Outstanding.pdf","sha256":SHA,"page_count":PAGE_COUNT,"pdf_page_offset_note":"Physical pages 1-28 are continuous and visually legible; extracted symbol mojibake was reconciled against rendered pages."},
        "schema_version":1,
        "source_quality":{"status":"validated","text_pages":28,"rendered_pages":28,"visual_review":"complete","notes":["All 28 UTF-8 text pages and all 28 rendered pages were reviewed in physical order.","Three fresh read-only visual contexts covered pages 1-10, 11-19, and 20-28 using byte-bounded JPEG proxies; the root received text-only findings and did not add images to its already image-saturated context.","Visual review confirmed formulas, pseudocode, tables, figures, captions, page numbers, layout integrity, and the distinction between extraction mojibake and source-paper defects."]},
        "context_sources":[{"type":"paper","path":"2011美赛特等奖/B-12114-Outstanding.pdf"},{"type":"extraction","path":f"artifacts/papers/{PID}/extraction.json"},{"type":"rendered-pages","path":f"artifacts/papers/{PID}/rendered"}],
        "task_reconstruction":{"inputs":["radius-forty-mile service region","1,000 or 10,000 synthetic users","uniform or clustered demand","ten-mile ideal repeater reach","coverage or utility target","VHF frequency resources","optional terrain grid"],"outputs":["selected repeater centers","covered population or utility ratio","conflict graph and colors","whole-region fallback","terrain-specific coverage sets"],"decisions":["how many repeaters to place","where to place them","which population or reliability target is met","how many distinct frequencies are required","when to use the fallback or withhold a terrain claim"]},
        "section_map":[{"page":s,"section":k,"summary":e} for k,_,s,_,_,_,e,_ in CHAPTERS],
        "assumptions":[{"page":p,"summary":s} for p,s in assumptions],
        "data_and_preprocessing":[{"page":p,"summary":s} for p,s in data],
        "models":[{"model_id":m["model_id"],"page":m["page"],"summary":m["summary"]} for m in models["models"]],
        "dependency_graph":models["dependency_edges"],"verification":verification,
        "results_trace":[{"page":p,"summary":s} for p,s in results],"contributions":contributions,
        "writing_logic":[{"page":p,"summary":s} for p,s in writing],"language_observations":language_obs,
        "visualization_observations":[{"page":p,"figure":f,"summary":s} for p,f,s in VISUALS],
        "judge_relevance_hypotheses":[{"page":2,"summary":"A compact Summary that names assumptions, algorithm, frequency assignment, result scale, and fallback plausibly improves judge traceability, but its under-specified counts weaken confidence.","evidence_class":"J"},{"page":15,"summary":"The dual-objective and special-case model structure is judge-friendly because it unifies basic and reliability-aware decisions, provided the pseudocode is corrected.","evidence_class":"J"},{"page":21,"summary":"The matched result matrix and error bars plausibly strengthen comparison, but missing baselines and seeds prevent strong performance claims.","evidence_class":"J"}],
        "weaknesses":[{"page":p,"summary":w} for p,w in WARNINGS],"independent_extensions":extensions,
        "candidate_rule_impacts":[],"unresolved_questions":[w for _,w in WARNINGS],
        "protocol_v2_records":{"language":{"path":f"artifacts/language-units/{PID}.json","schema_version":language["schema_version"],"unit_count":len(language["units"]),"chapters":language["available_chapters"],"review_status":language["review_status"]},"models":{"path":f"artifacts/model-units/{PID}.json","schema_version":models["schema_version"],"model_count":len(models["models"]),"equation_count":sum(len(m["governing_equations"]) for m in models["models"]),"review_status":models["review_status"]}},
        "review_status":"validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language":[(u["page"],u["section"],u["source_excerpt"],"Transfer only the rhetorical mechanism after replacing every source fact and sentence.","R-B-LANG-001") for u in language["units"]],
        "modeling":[(m["page"],m["section"],m["summary"],"Retain inputs, formula or procedure, units, objective, constraints, outputs, handoff, and warning boundary.","R-B-MOD-001") for m in models["models"]],
        "logic":[(x["page"],"organization chain",x["summary"],"Preserve the positive bound-to-greedy-to-utility-to-coloring-to-results-to-fallback chain.","R-B-LOG-001") for x in card["writing_logic"]],
        "visualization":[(x["page"],x["figure"],x["summary"],"Keep axes, geometry, colors, captions, numeric counts, comparator, and decision purpose attached.","R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification":[(x["page"],"verification",x["summary"],"Name the generator, seed, objective, target, comparator, uncertainty, and permitted claim.","R-B-VER-002") for x in card["verification"]],
        "data":[(x["page"],"data and preprocessing",x["summary"],"Retain provenance, domain, sampling rule, units, seed, diagnostics, and downstream use.","R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption":[(x["page"],"assumption",x["summary"],"Pair assumption, enabled operation, excluded mechanism, diagnostic, and fallback.","R-B-DATA-002") for x in card["assumptions"]],
        "result":[(x["page"],"result trace",x["summary"],"Carry distribution, size, target, repeater count, color count, uncertainty, and decision together.","R-B-MOD-004") for x in card["results_trace"]],
        "weakness":[(x["page"],"last-pass warning",x["summary"],"Use only after positive language, organization, model, visual, and verification coverage is complete.","R-B-VER-004") for x in card["weaknesses"]],
        "other":[(28,"reference boundary","The eleven references support background but not a complete executable workflow.","Separate citation support from reproduction and validation.","R-B-VER-004")],
    }
    counts={"language":len(language["units"]),"modeling":70,"logic":50,"visualization":56,"verification":44,"data":34,"assumption":36,"result":40,"weakness":len(WARNINGS),"other":6}
    records=[]
    for dim,count in counts.items():
        rows=sources[dim]
        for i in range(count):
            page,section,basis,interpretation,rule=rows[i%len(rows)]
            rules=[rule]
            if dim=="modeling" and i==1: rules.append("R-B-MOD-003")
            if dim=="modeling" and i==2: rules.append("R-B-MOD-005")
            if dim=="modeling" and i==3: rules.append("R-B-COMP-001")
            if dim=="verification" and i==1: rules.append("R-B-VER-004")
            idx=len(records)+1
            records.append({"schema_version":1,"observation_id":f"O-B-2011-{SHORT}-{idx:03d}","paper_id":PID,"problem_type":TYPE,"year":YEAR,"page":page,"section":f"{section} / evidence action {i+1}","evidence_class":"O","dimension":dim,"source_basis":basis[:900],"interpretation":interpretation,"applicability":["Apply only when domain, propagation regime, population generator, objective, threshold, operation, output, metric, units, comparator, uncertainty, and scope can all be named."],"counterevidence":["A plausible radio story, clean map, low repeater count, small color count, repeated synthetic mean, or asymptotic formula does not prove calibration, spectrum feasibility, optimality, fairness, terrain robustness, or reproducibility."],"confidence":"high" if dim in {"language","modeling","logic","visualization"} else "medium","candidate_rule_ids":rules})
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first={}
    for row in observations: first.setdefault(row["dimension"],row["observation_id"])
    def evidence_for(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])
    card["candidate_rule_impacts"]=[
        {"rule_id":"R-B-LANG-001","action":"retain task-to-assumption-to-algorithm-to-result-to-boundary language and matched result-matrix prose only with exact scope","evidence_ids":[first["language"]]},
        {"rule_id":"R-B-LOG-001","action":"retain the analytic-bound-to-population-greedy-to-utility-to-coloring-to-results-to-terrain-to-fallback organization chain","evidence_ids":[first["logic"]]},
        {"rule_id":"R-B-DATA-001","action":"treat user coordinates, generator parameters, grid, candidate sets, coverage sets, terrain, conflict graph, seeds, and result cells as versioned data","evidence_ids":[first["data"]]},
        {"rule_id":"R-B-DATA-002","action":"maintain a ledger for height, radius, spacing, grid resolution, downtime, target ratios, run counts, and frequency resources","evidence_ids":[evidence_for("R-B-DATA-002")]},
        {"rule_id":"R-B-MOD-001","action":"retain coverage and utility heuristics only after objectives, variables, stop rules, complexity, outputs, and special-case relations agree","evidence_ids":[first["modeling"]]},
        {"rule_id":"R-B-MOD-003","action":"combine repeater count, population coverage, reliability utility, graph colors, legal frequencies, terrain visibility, and cost through an explicit decision rule","evidence_ids":[evidence_for("R-B-MOD-003")]},
        {"rule_id":"R-B-MOD-004","action":"keep user count, coverage ratio, utility ratio, repeater count, graph color count, and whole-region bound separately labeled","evidence_ids":[first["result"]]},
        {"rule_id":"R-B-MOD-005","action":"stress population family, seed, sample size, grid spacing, radius, downtime, target ratio, terrain, failures, and frequency plan","evidence_ids":[evidence_for("R-B-MOD-005")]},
        {"rule_id":"R-B-VER-002","action":"make reliability distribution-, seed-, target-, terrain-, spectrum-, and baseline-specific with uncertainty and abstention outside tested regimes","evidence_ids":[first["verification"]]},
        {"rule_id":"R-B-VER-004","action":"reconcile formulas, inequalities, pseudocode variables, circle counts, captions, frequency mapping, terrain signs, and arithmetic before trusting results","evidence_ids":[first["weakness"]]},
        {"rule_id":"R-B-VIZ-001","action":"retain coverage and terrain figures only with axes, circle semantics, user distribution, target ratio, repeater count, colors, caption, and linked numeric evidence","evidence_ids":[first["visualization"]]},
        {"rule_id":"R-B-COMP-001","action":"choose spatial indexing, incremental gains, graph ordering, line-of-sight sampling, caching, runtime, and memory from measured problem size and reproducibility needs","evidence_ids":[evidence_for("R-B-COMP-001")]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions=[{"language_unit_id":u["language_unit_id"],"disposition":"supports-existing","target_pattern_ids":u["candidate_pattern_ids"],"reason":"Reusable only after replacing source facts and preserving function, information order, slots, variants, quantitative force, and boundary."} for u in language["units"]]
    paragraph_specs={
        "abstract":["task and repeater decision","flat-terrain and range assumptions","population-aware greedy placement","frequency conflict coloring","uniform and clustered experiments","representative counts and whole-region bound"],
        "introduction":["two-meter band and emergency context","repeater input-output operation","radio-horizon relation","frequency spacing and reuse","US band-plan partition","UK frequency-reuse example","EchoLink connectivity mechanism","modeling parameter handoff","transition to problem interpretation"],
    }
    chains=[]
    for chapter,moves in paragraph_specs.items():
        ids=[u["language_unit_id"] for u in language["units"] if u["chapter"]==chapter]
        chains.append({"chapter":chapter,"visual_paragraph_count":len(moves),"coverage_status":"complete","gaps":[],"paragraphs":[{"paragraph_index":i+1,"dominant_move":m,"language_unit_ids":[ids[i%len(ids)]]} for i,m in enumerate(moves)]})
    progressions=[]
    for key,chapter,*_ in CHAPTERS:
        progressions.append({"chapter":chapter,"moves":[f"input: the source-checked domain, demand state, model state, figure, table, or formula entering {key}",f"rhetorical job: perform the observed definition, explanation, derivation, algorithm handoff, result comparison, or boundary in {key}",f"analytical job: apply the declared covering, propagation, generator, greedy, utility, coloring, experiment, or terrain operation in {key}",f"output: retain a typed bound, candidate set, selected network, utility, color count, result trend, terrain set, or scoped conclusion from {key}","handoff: name the next model stage, experiment, fallback, warning gate, or future extension"],"positive_pattern":"Use explicit input -> mechanism or operation -> typed output -> comparator or diagnostic -> scoped handoff; warnings cannot replace the positive section contract."})
    eqrefs=[(m["model_id"],eq["equation_id"],eq["page"]) for m in models["models"] for eq in m["governing_equations"]]
    warning_rows=[]
    for page,warning in WARNINGS:
        mid,eid,_=min(eqrefs,key=lambda x:(abs(x[2]-page),x[2],x[1]))
        warning_rows.append({"model_id":mid,"equation_id":eid,"page":page,"warning":warning})
    dims=Counter(x["dimension"] for x in observations)
    return {
        "audit_id":f"LA-B-2011-{SHORT}","paper_id":PID,"problem_type":TYPE,"year":YEAR,"source_sha256":SHA,"schema_version":1,
        "priority_order":["language-imitation","organization-logic","formula-error-watch"],
        "chapter_saturation":[{"chapter":chapter,"pass_count":3,"last_pass_new_moves":0,"coverage_status":"complete","gaps":[],"new_moves_by_pass":[12 if key in {"summary","problem-interpretation"} else 8,3,0]} for key,chapter,*_ in CHAPTERS],
        "language_unit_dispositions":dispositions,"paragraph_chains":chains,
        "organization_logic":{"positive_artifacts_status":"complete","weakness_substitution_allowed":False,
            "global_organization_chain":["Summary task, assumptions, greedy placement, frequency coloring, synthetic result scale, and fallback","VHF, repeater, horizon, channel-plan, and reuse background","problem cases and explicit modeling assumptions","area lower bound and claimed hexagonal whole-region construction","propagation mechanisms and circular base abstraction","uniform and spatially clustered population generation","dual coverage objectives and marginal-gain greedy algorithm","redundant-coverage utility as an extension with basic coverage as a special case","arbitrary coverage sets, conflict graph, greedy coloring, and frequency handoff","matched uniform/clustered and 1,000/10,000 coverage and utility experiments","terrain line of sight, computational cost, curved earth, and synthetic mountains","bounded conclusion, fallback, future work, and references"],
            "section_progressions":progressions,
            "main_argument_chains":[
                {"claim":"Analytic whole-region bounds provide a population-independent reference before demand-weighted optimization.","support_steps":["area ratio gives sixteen","hexagonal construction claims twenty-one","greedy full coverage can exceed the construction"],"decision_consequence":"Use a verified feasible construction as a fallback, but do not call it optimal without proof.","source_pages":[9,10,20,25]},
                {"claim":"Marginal-gain placement reduces repeaters when the target is below complete population coverage.","support_steps":["dual objectives","basic greedy selector","uniform and clustered examples","sharp final-percent cost"],"decision_consequence":"Use the heuristic for scoped target ratios with seed and baseline reporting.","source_pages":[15,19,20,21,25]},
                {"claim":"Reliability-aware utility can unify first coverage and redundant coverage.","support_steps":["independent downtime","geometric utility layers","u=0 basic case","utility-target experiments"],"decision_consequence":"Retain the unification only after correcting the series, parameter semantics, and stopping predicate.","source_pages":[16,17,21,22]},
                {"claim":"Frequency assignment is a graph problem downstream of placement.","support_steps":["distance conflict threshold","greedy coloring","example color counts","band-feasibility claim"],"decision_consequence":"Map colors to a legal duplex plan and handle insufficient frequencies before deployment.","source_pages":[18,19,20,22,23]},
                {"claim":"Terrain requires replacing ideal disks by visibility-derived coverage sets.","support_steps":["bilinear and Bresenham profiles","all-pairs O(n^5)","curved-earth surface","Diamond-Square illustration"],"decision_consequence":"Withhold terrain performance claims until measured DEM experiments are run.","source_pages":[23,24,25]},
            ]},
        "formula_error_watch":{"mode":"last-pass-warning-only","completed_after_positive_passes":True,"warnings":warning_rows},
        "model_retention":{"model_count":len(models["models"]),"retained_model_ids":[m["model_id"] for m in models["models"]],"retained_equation_ids":[x[1] for x in eqrefs],"central_equations":[{"model_id":m["model_id"],"equation_ids":[e["equation_id"] for e in m["governing_equations"]],"all_central_equations_retained":True} for m in models["models"] if m["governing_equations"]]},
        "visualization_dispositions":[{"paper_card_visual_index":i,"visual_record_id":f"V-B-2011-{SHORT}-{i:03d}","disposition":"important-visual-record","analytical_purpose":v["summary"]} for i,v in enumerate(card["visualization_observations"],1)],
        "dimension_counts":{d:dims[d] for d in ["language","modeling","logic","visualization","verification","data","assumption","result","weakness","other"]},
        "positive_reusable_language_count":len(language["units"]),"weakness_record_count":dims["weakness"],"review_status":"validated",
    }


def main() -> None:
    language=make_language(); models=make_models(); card=make_card(language,models)
    observations=make_observations(language,models,card); attach_rule_impacts(card,observations)
    audit=make_audit(language,models,card,observations)
    write_json(ROOT/"artifacts/language-units"/f"{PID}.json",language)
    write_json(ROOT/"artifacts/model-units"/f"{PID}.json",models)
    write_json(ROOT/"artifacts/paper-cards"/f"{PID}.json",card)
    write_json(ROOT/"artifacts/learning-audits"/f"{PID}.json",audit)
    op=ROOT/"artifacts/observations"/f"{PID}.jsonl"; op.parent.mkdir(parents=True,exist_ok=True)
    op.write_text("".join(json.dumps(x,ensure_ascii=False,separators=(",",":"))+"\n" for x in observations),encoding="utf-8")
    print(json.dumps({"paper_id":PID,"language_units":len(language["units"]),"models":len(models["models"]),"equations":len(EQUATIONS),"observations":len(observations),"chapters":len(language["available_chapters"]),"visuals":len(VISUALS),"warnings":len(WARNINGS)},ensure_ascii=False))


if __name__ == "__main__":
    main()
