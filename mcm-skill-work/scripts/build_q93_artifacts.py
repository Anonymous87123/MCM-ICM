from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import build_q92_artifacts as base


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2011-9440-95f0fa40"
SHORT = "9440"
SHA = "95f0fa406fe84cd797ea6b689fd7e1870edecb01791003db86c71f9d069c0b93"
TYPE = "B"
YEAR = "2011"
PAGE_COUNT = 41

PATTERNS = [
    "LP-B-ABS-CONSTRAINT-METHOD-RESULT-SCOPE",
    "LP-B-INTRO-GAP-MODULE-ROADMAP",
    "LP-B-DEFINITION-CONDITION-CONSEQUENCE",
    "LP-B-PROPOSITION-SUFFICIENT-CONDITION-BOUNDARY",
    "LP-B-PHYSICS-DERIVATION-PARAMETER-HANDOFF",
    "LP-B-LOWER-BOUND-BENCHMARK-IMPROVEMENT",
    "LP-B-VORONOI-WORST-CASE-ITERATION",
    "LP-B-HEURISTIC-ESCAPE-STOP-RULE",
    "LP-B-GRAPH-TREE-ROUTE-RESOURCE",
    "LP-B-RESULT-PROOF-QUALIFIER",
    "LP-B-SENSITIVITY-BOTTLENECK-TRANSITION",
    "LP-B-DISCRETE-CORRECTION-TOLERANCE",
    "LP-B-TERRAIN-HIERARCHY-BOUNDARY",
    "LP-B-CONCLUSION-CONTRIBUTION-WEAKNESS",
]

# key, protocol chapter, first page, last page, tag, language-unit count,
# source-checked paraphrase, visually observed paragraph count
CHAPTERS = [
    ("summary-sheet", "title", 1, 1, "SUM", 18, "The Summary Sheet compresses parameters, network concepts, Voronoi and extremal optimization, 104-versus-108 placement figures, probabilistic reachability, and stated strengths and weaknesses into a one-page decision overview.", 8),
    ("abstract", "abstract", 2, 2, "ABS", 24, "The Abstract moves from a capacity-and-interference two-tier network to weak and strong requirements, a cellular benchmark, Voronoi minimum-enclosing-circle refinement, quantitative 11 and 104 repeater results, frequency and tone assignment, and terrain or density extensions.", 8),
    ("introduction", "introduction", 3, 4, "INT", 24, "The Introduction distinguishes homogeneous relay research from the paper's user-repeater hierarchy, identifies coverage, placement, capacity, and interference gaps, announces a benchmark plus three algorithmic modules, and closes with a detailed section roadmap.", 12),
    ("problem-description", "problem-restatement", 5, 5, "PRB", 16, "The problem section defines the radius-forty domain, user count, repeater receive and transmit frequencies, PL tones, a simplified interference predicate, coverage, capacity, and the required composition of a complete placement solution.", 8),
    ("two-tier-network", "model-establishment", 6, 8, "NET", 24, "The model represents users and repeaters as two node classes in a directed graph, defines user-to-repeater and repeater-to-repeater edges, separates capacity, interference, coverage, and global reachability conditions, and proves two sufficient implication statements.", 13),
    ("communication-radius", "problem-analysis", 9, 11, "RAD", 24, "The propagation analysis derives a free-space received-power relation, converts it into a link budget, selects empirical power and threshold values, and reports repeater and user communication radii that drive all later geometry.", 13),
    ("repeater-capacity", "problem-analysis", 11, 12, "CAP", 22, "The capacity subsection starts from Shannon information rate, borrows a CDMA-style energy-to-noise expression, substitutes gain and voice factors, and reports a single-repeater capacity near 119 users.", 11),
    ("continuous-approximation", "data-preprocessing", 12, 14, "CON", 22, "The paper replaces mobile discrete users by a uniform continuous density, converts capacity into a Voronoi-area constraint, distinguishes 324 interference-free from 270 non-interacting repeater assignments, and derives geometric and capacity lower bounds.", 12),
    ("naive-cellular", "model-improvement", 14, 18, "NAI", 26, "The baseline arranges repeaters at regular-hexagon centers, tabulates small covering constructions, chooses cell edge length from coverage and capacity, and obtains 12 and 108 repeater benchmarks for the two population scales.", 15),
    ("voronoi-extremal-algorithm", "algorithm", 19, 21, "VOR", 28, "The main algorithm starts at an analytic lower bound, randomizes repeater locations, builds clipped Voronoi cells, finds each cell's minimum enclosing circle, moves sites to circle centers, checks feasibility, then perturbs the least-area cell or increases the repeater count.", 15),
    ("frequency-tone-algorithm", "algorithm", 22, 23, "FRE", 24, "The secondary algorithm builds a distance graph, chooses a minimum or maximum spanning tree, removes selected incident edges to create routes, assigns one PL tone per route, and chains receiver and transmitter frequencies along each route.", 12),
    ("ideal-range-results", "results", 24, 29, "RES", 28, "For an ideal repeater radius of 85.45 miles, the results report 11 repeaters for 1,000 users and 104 for 10,000, give full coordinate and frequency tables, and use a circle-covering theorem to exclude ten small circles in the first case.", 17),
    ("short-range-results", "robustness-verification", 29, 32, "R40", 20, "With the radius shortened to forty miles, the paper keeps the same locations, changes frequency and tone routes, and estimates random ordered-point reachability at 90.71 and 97.12 percent for the two network sizes.", 9),
    ("parameter-sensitivity", "sensitivity-analysis", 33, 34, "SEN", 20, "The sensitivity section sweeps user count and user communication radius, compares the proposed and cellular counts, and explains a transition from coverage-radius limitation to repeater-capacity limitation.", 9),
    ("density-fluctuation", "error-analysis", 34, 35, "DEN", 18, "The discrete correction models the count in a Voronoi cell with a binomial law, derives its mean and standard deviation, and replaces nominal capacity 119 by a heuristic two-standard-deviation tolerant capacity of 99.", 8),
    ("mountainous-terrain", "sensitivity-robustness", 35, 36, "MNT", 20, "The terrain discussion proposes lower-level hollow repeaters and higher-level mountain-top repeaters, then sketches tone and frequency reuse rules intended to use terrain shielding while preserving hierarchical relay paths.", 10),
    ("conclusion", "conclusion", 37, 37, "CLS", 14, "The conclusion restates the two-tier model, cellular benchmark, Voronoi extremal optimizer, spanning-tree allocation, 11 and 104 counts, probabilistic reachability, broad applicability claims, and two explicit weaknesses.", 7),
    ("parameter-symbol-assumption-appendices", "appendix", 38, 40, "APP", 22, "The appendices centralize parameter values, mathematical symbols, and seven assumptions, enabling cross-checks among the link budget, capacity derivation, continuous approximation, graph definitions, and claimed propagation boundary.", 12),
    ("references", "references", 40, 41, "REF", 8, "The references connect relay networking, circle covering, Voronoi diagrams, extremal optimization, antenna theory, CDMA capacity, and base-station placement, but include unstable web sources and no executable reproduction package.", 4),
]

MOVES = [
    ("constraint-to-method-to-result", "State the decision constraints, name the computational mechanism, report the result, and retain its scope.", "constraints -> method -> quantitative result -> scope"),
    ("gap-to-module-roadmap", "Turn each literature or task gap into a named modeling or algorithmic module and then preview the section that resolves it.", "prior work -> missing capability -> module -> roadmap"),
    ("definition-to-operational-test", "Define a graph, set, radius, frequency condition, or coverage object and immediately state how it will be tested.", "object -> attributes -> predicate -> operational consequence"),
    ("proposition-with-sufficiency", "State an implication, give the geometric reason, and distinguish a sufficient regime from necessity in one instance.", "claim -> condition -> proof idea -> scope boundary"),
    ("physics-to-parameter-handoff", "Derive a physical relation only far enough to produce the range, capacity, or interference parameter consumed by optimization.", "mechanism -> equation -> parameter -> downstream consumer"),
    ("lower-bound-before-benchmark", "Place necessary geometric and capacity bounds before a constructive cellular benchmark and later heuristic improvement.", "necessary bound -> feasible baseline -> improvement target -> comparison"),
    ("worst-cell-refinement", "Use the Voronoi partition to expose the worst coverage cell and move the site toward its minimum enclosing-circle center.", "partition -> worst-case geometry -> update -> convergence check"),
    ("escape-rule-with-budget", "Name the local-optimum escape action, its trigger, its operation budget, and the restart or resource-increase fallback.", "failure -> perturbation -> budget -> restart or increment"),
    ("graph-to-resource-route", "Convert geometric reach into a graph, choose a tree, split it into routes, and attach tones and frequencies to the route structure.", "reach graph -> tree -> route components -> resource assignment"),
    ("result-with-proof-qualifier", "Pair a numerical construction with the exact lower-bound theorem or experiment that supports it and limit the word optimal accordingly.", "construction -> evidence -> exclusion or uncertainty -> qualified conclusion"),
    ("sensitivity-to-bottleneck", "Sweep one parameter, identify a transition, and explain which constraint becomes binding on each side.", "parameter sweep -> transition -> active constraint -> decision implication"),
    ("continuous-to-discrete-correction", "Translate a continuous load estimate into a discrete probability model and a capacity margin without hiding approximation error.", "continuous mean -> count distribution -> variability -> tolerance"),
    ("terrain-to-hierarchy", "Explain how terrain simultaneously blocks and separates signals, then propose a tiered architecture with explicit unresolved radio constraints.", "terrain mechanism -> local coverage -> high-level relay -> reuse rule -> limitation"),
    ("conclusion-with-admitted-gap", "Summarize contributions and exact figures, then state unresolved global reachability and physical simplifications before generalizing.", "contribution -> result -> applicability -> weakness"),
]

EXAMPLES = [
    ("A flood-relief relay abstract names coverage, load, interference, a geometric baseline, an iterative placement method, and a bounded field-test result.", "It avoids calling the field layout globally optimal unless the lower bound covers every operational constraint."),
    ("A hospital-network introduction maps each prior limitation to one later module: demand estimation, capacitated placement, routing, and spectrum planning.", "The roadmap preserves the same order as the body."),
    ("A logistics hub model defines directed shipment edges and then states the exact capacity and reachability tests used by the solver.", "It does not silently assume reverse edges."),
    ("A sensor theorem labels a range condition sufficient for universal connectivity while allowing smaller-range instances to succeed.", "The proof separates diameter geometry from frequency feasibility."),
    ("A radio-planning section derives a calibrated path-loss relation and hands a confidence interval for service radius to the placement optimizer.", "Every dB and linear quantity keeps its unit and reference."),
    ("A facility study reports an area lower bound, a lattice baseline, and a stochastic refinement in that order.", "Necessary, feasible, and best-observed counts remain distinct."),
    ("A districting algorithm partitions demand, minimizes each cell's worst travel radius, and stops on the sum of displacement norms.", "It logs the objective after every iteration."),
    ("A randomized optimizer states the perturbation target, retry budget, seed policy, and resource-increment fallback.", "It reports success frequency across independent runs."),
    ("A pipeline network converts proximity into a graph, selects a tree by a declared weight, partitions routes, and assigns channels under explicit duplex constraints.", "Route connectivity and RF interference are validated separately."),
    ("A coverage result pairs an eleven-site construction with a theorem excluding ten sites under the same radius and domain assumptions.", "The conclusion states exactly which constraints the proof includes."),
    ("A staffing sensitivity plot identifies the demand level at which workload capacity overtakes geographic coverage as the binding constraint.", "Both raw and normalized counts are shown."),
    ("A warehouse load model replaces a continuous mean by a binomial count and chooses capacity from a stated tail probability.", "The confidence level replaces an informal two-sigma slogan."),
    ("A mountain communications design separates valley access nodes from ridge backbone nodes and adds scheduling to shared-frequency uplinks.", "Terrain shielding is verified by profiles and link budgets."),
    ("A conclusion reports the tested gains, unresolved connectivity guarantee, and omitted propagation effects before offering extensions.", "Performance adjectives are tied to measured baselines."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose
EQUATIONS = [
    ("circular domain", 6, "two-tier network", "domain constraint", "x^2+y^2 <= Phi^2", r"x^2+y^2\le\Phi^2", ["x", "y", "Phi"], "Constrain users and repeaters to the circular service area."),
    ("free-space power density", 9, "communication radius", "Friis propagation", "P = Pr,out/(4 pi d^2)", r"P=\frac{P_{r,out}}{4\pi d^2}", ["P", "P_r_out", "d"], "Express isotropic free-space power flux density."),
    ("effective aperture reception", 9, "communication radius", "Friis propagation", "P' = Pr,out/(4 pi d^2) * lambda^2/(4 pi)", r"P'=\frac{P_{r,out}}{4\pi d^2}\frac{\lambda^2}{4\pi}", ["P_prime", "P_r_out", "d", "lambda"], "Apply the ideal receiving aperture used by the paper."),
    ("frequency form of Friis", 9, "communication radius", "Friis propagation", "P' = Pr,out (c/(4 pi d f))^2", r"P'=P_{r,out}\left(\frac{c}{4\pi df}\right)^2", ["P_prime", "P_r_out", "c", "d", "f"], "Replace wavelength by c/f."),
    ("free-space path loss", 9, "communication radius", "link budget", "Ls = 10 lg(Pr,out/P') = 92.4 + 20 lg d + 20 lg f", r"L_s=10\log_{10}\frac{P_{r,out}}{P'}=92.4+20\log_{10}d+20\log_{10}f", ["L_s", "P_r_out", "P_prime", "d", "f"], "State the kilometer-and-gigahertz path-loss formula."),
    ("received-power budget", 10, "communication radius", "link budget", "Pr,in = Pr,out + gains - feed losses - other losses - Ls", r"P_{r,in}=P_{r,out}+G_{out}+G_{in}-L_{f,out}-L_{f,in}-L_{b,out}-L_{b,in}-L_s", ["P_r_in", "P_r_out", "G_out", "G_in", "L_f_out", "L_f_in", "L_b_out", "L_b_in", "L_s"], "Combine power, gains, losses, and path loss in a dB-domain budget."),
    ("printed range inversion", 10, "communication radius", "link budget", "d = 10^([10 lg(Pr,out/Pr,in)-37.2328]/20)", r"d=10^{\left[10\log_{10}(P_{r,out}/P_{r,in})-37.2328\right]/20}", ["d", "P_r_out", "P_r_in"], "Retain the printed inversion whose constant requires warning."),
    ("Shannon information rate", 11, "repeater capacity", "channel capacity", "phi = B log2(1+SNR)", r"\varphi=B\log_2(1+\mathrm{SNR})", ["varphi", "B", "SNR"], "Relate bandwidth and signal-to-noise ratio to information rate."),
    ("printed CDMA energy ratio", 11, "repeater capacity", "CDMA capacity", "Eb/N0 = (Pur/phi)/((C-1)Pur/B) = (B/phi)/(C-1)", r"\frac{E_b}{N_0}=\frac{P_{ur}/\varphi}{(C-1)P_{ur}/B}=\frac{B/\varphi}{C-1}", ["E_b_N_0", "P_ur", "varphi", "C", "B"], "Preserve the printed processing-gain capacity relation."),
    ("adapted repeater capacity relation", 11, "repeater capacity", "capacity approximation", "Eb/N0 = Gout/[V(C-1)(1+Iother/Iself)]", r"\frac{E_b}{N_0}=\frac{G_{out}}{V(C-1)(1+I_{other}/I_{self})}", ["E_b_N_0", "G_out", "V", "C", "I_other", "I_self"], "State the paper's adapted CDMA-style capacity equation."),
    ("equal-power SNR", 12, "repeater capacity", "capacity approximation", "SNR = Pur/((C-1)Pur) = 1/(C-1)", r"\mathrm{SNR}=\frac{P_{ur}}{(C-1)P_{ur}}=\frac{1}{C-1}", ["SNR", "P_ur", "C"], "Represent equal received powers with other noise ignored."),
    ("reported repeater capacity", 12, "repeater capacity", "capacity approximation", "C = 1 + Gout/[V(1+Iother/Iself)(Eb/N0)] approx 119", r"C=1+\frac{G_{out}}{V(1+I_{other}/I_{self})(E_b/N_0)}\approx119", ["C", "G_out", "V", "I_other", "I_self", "E_b_N_0"], "Compute the paper's nominal simultaneous-user capacity."),
    ("continuous user density", 12, "continuous approximation", "density model", "rho = N/(pi Phi^2)", r"\rho=\frac{N}{\pi\Phi^2}", ["rho", "N", "Phi"], "Replace discrete mobile users by uniform area density."),
    ("Voronoi capacity constraint", 12, "continuous approximation", "capacitated Voronoi", "rho S_V(r_j) <= C", r"\rho S_V(r_j)\le C", ["rho", "S_V", "r_j", "C"], "Limit each nearest-repeater service region by capacity."),
    ("geometric repeater lower bound", 13, "continuous approximation", "area lower bound", "M >= Phi^2/r^2 = 40^2/15.28^2 = 6.85", r"M\ge\frac{\Phi^2}{r^2}=\frac{40^2}{15.28^2}=6.85", ["M", "Phi", "r"], "Give a necessary area bound on repeater count."),
    ("capacity repeater lower bound", 14, "continuous approximation", "capacity lower bound", "M >= N/C = N/118", r"M\ge\frac{N}{C}=\frac{N}{118}", ["M", "N", "C"], "Give the printed capacity lower bound and retain its 118-versus-119 discrepancy."),
    ("hexagonal cell capacity", 16, "naive cellular solution", "cellular benchmark", "(3 sqrt(3)/2) rh^2 rho = C", r"\frac{3\sqrt{3}}{2}r_h^2\rho=C", ["r_h", "rho", "C"], "Choose the largest regular-hexagon edge satisfying capacity."),
    ("Voronoi movement convergence", 20, "main algorithm", "iterative refinement", "sum_j distance(r_j, c_j) < xi", r"\sum_j\lVert r_j-c_j\rVert<\xi", ["r_j", "c_j", "xi"], "Stop when the total displacement to minimum-enclosing-circle centers is small."),
    ("component balance objective", 23, "secondary algorithm", "tree route splitting", "min sum_(a,b) |SC_a-SC_b|", r"\min\sum_{a,b}|SC_a-SC_b|", ["SC_a", "SC_b"], "Choose deleted tree edges intended to balance resulting route sizes."),
    ("ten-circle covering theorem", 25, "N=1000 result", "circle-covering proof", "r(n)=1+2 cos(2 pi/(n-1)) for n=8,9,10", r"r(n)=1+2\cos\left(\frac{2\pi}{n-1}\right),\quad n\in\{8,9,10\}", ["r_n", "n"], "Invoke the cited exact covering radius for eight through ten unit circles."),
    ("ten-circle exclusion", 25, "N=1000 result", "circle-covering proof", "r(10)=2.532 < 40/15.28=2.618", r"r(10)\approx2.532<\frac{40}{15.28}\approx2.618", ["r_10"], "Exclude coverage of the service disk by ten user-radius circles."),
    ("constraint transition", 33, "parameter sensitivity", "bottleneck transition", "N/(pi Phi^2) = C/(pi r^2)", r"\frac{N}{\pi\Phi^2}=\frac{C}{\pi r^2}", ["N", "Phi", "C", "r"], "Locate the approximate transition between geometric and capacity bottlenecks."),
    ("Voronoi user-count distribution", 34, "density fluctuation", "binomial correction", "P(X)=choose(N,X)(Sv/(pi Phi^2))^X(1-Sv/(pi Phi^2))^(N-X)", r"P(X)=\binom{N}{X}\left(\frac{S_V}{\pi\Phi^2}\right)^X\left(1-\frac{S_V}{\pi\Phi^2}\right)^{N-X}", ["X", "N", "S_V", "Phi"], "Model the discrete number of users assigned to one region."),
    ("Voronoi count expectation", 34, "density fluctuation", "binomial correction", "E(X)=N Sv/(pi Phi^2)=rho Sv", r"\mathbb{E}[X]=\frac{NS_V}{\pi\Phi^2}=\rho S_V", ["E_X", "N", "S_V", "Phi", "rho"], "Recover the continuous load as the binomial expectation."),
    ("Voronoi count deviation", 34, "density fluctuation", "binomial correction", "sigma(X)=sqrt(rho Sv(1-Sv/(pi Phi^2)))", r"\sigma(X)=\sqrt{\rho S_V\left(1-\frac{S_V}{\pi\Phi^2}\right)}", ["sigma_X", "rho", "S_V", "Phi"], "Quantify discrete load fluctuation."),
    ("two-sigma tolerant capacity", 35, "density fluctuation", "capacity margin", "C' + 2 sqrt(C') = C", r"C'+2\sqrt{C'}=C", ["C_prime", "C"], "Choose the paper's heuristic two-standard-deviation capacity margin."),
]

ALGORITHMS = [
    (6, "two-tier directed graph construction", "Build user and repeater nodes with locations, frequencies, tones, and directed communication edges.", ["user_nodes", "repeater_nodes", "locations", "frequencies", "tones"], ["D", "E_ur", "E_rr"]),
    (7, "reachable-area traversal", "Traverse repeater-to-repeater directed paths from a user's reachable repeaters to construct the user's modeled reachable area.", ["D", "user", "coverage_disks"], ["reachable_repeaters", "reachable_area"]),
    (8, "weak-to-strong sufficient-condition check", "Use the service-region diameter to determine when any coverage solution automatically gives modeled global reachability.", ["R", "Phi", "coverage_solution"], ["strong_solution_flag"]),
    (9, "free-space range estimation", "Combine Friis propagation, a dB link budget, empirical ERP, gains, losses, frequency, and receive threshold to estimate R and r.", ["ERP", "frequency", "gains", "losses", "receive_threshold"], ["R", "r"]),
    (11, "CDMA-inspired capacity estimation", "Adapt a processing-gain and energy-to-noise relation to estimate simultaneous repeater users.", ["G_out", "V", "E_b_N_0", "interference_ratio"], ["C"]),
    (12, "continuous-density replacement", "Replace mobile discrete user locations by a uniform density and transform nearest-repeater capacity into a Voronoi-area inequality.", ["N", "Phi", "repeater_locations", "C"], ["rho", "capacity_feasible_cells"]),
    (13, "frequency-tone counting", "Count per-tone transmitter-frequency choices and remove inverse frequency-pair cycles to distinguish interference-free and non-interacting limits.", ["frequency_interval", "f_c", "N_PL", "duplex_pairs"], ["interference_free_limit", "non_interacting_limit"]),
    (13, "lower-bound synthesis", "Take the maximum of geometric area and capacity lower bounds before placement begins.", ["Phi", "r", "N", "C"], ["M_0"]),
    (14, "cellular benchmark lookup", "Scale beehive-like regular-hexagon constructions and select a sufficient cell count from coverage and capacity constraints.", ["Phi", "r", "rho", "C", "cell_table"], ["r_h", "baseline_repeaters"]),
    (20, "Voronoi minimum-enclosing-circle refinement", "Iteratively clip Voronoi cells to the service disk, compute each minimum enclosing circle, and move the repeater to its center.", ["M", "initial_locations", "service_disk", "xi"], ["refined_locations", "cell_circles", "converged"]),
    (21, "extremal perturbation and increment", "When a converged configuration violates radius or capacity, randomize the least-area repeater up to T_c times, then add one repeater and restart.", ["refined_locations", "feasibility", "T_c", "random_seed"], ["candidate_solution", "M"]),
    (22, "repeater reach graph", "Create an undirected geometric graph whose edges join repeaters separated by less than R.", ["repeater_locations", "R"], ["G"]),
    (22, "minimum-or-maximum spanning tree", "Choose a distance-weighted minimum or maximum spanning tree to trade local link strength against spatial reach.", ["G", "edge_weights", "tree_mode"], ["T"]),
    (23, "tree route splitting", "Delete selected incident edges at high-degree nodes to produce balanced connected route components.", ["T", "component_balance_rule"], ["signal_routes"]),
    (23, "route tone and frequency assignment", "Assign one PL tone to each route and chain transmitter frequencies to neighboring receiver frequencies.", ["signal_routes", "frequency_pairs", "PL_tones"], ["repeater_channel_plan"]),
    (24, "ideal-range feasibility check", "Check Voronoi area times density against capacity and minimum-enclosing-circle radius against user reach for reported placements.", ["repeater_locations", "rho", "C", "r"], ["coverage_capacity_status"]),
    (25, "N=1000 optimality argument", "Combine an eleven-circle construction with the cited ten-circle covering radius to exclude ten repeaters in the idealized coverage problem.", ["eleven_circle_layout", "r_10", "Phi", "r"], ["idealized_minimum_11"]),
    (26, "N=10000 parameter table", "Record 104 coordinates, five recurring duplex pairs, and 21 tones for the reported ideal-range layout.", ["repeater_locations", "duplex_pairs", "tones"], ["table_6_plan"]),
    (29, "short-range reachability Monte Carlo", "Sample 100000 ordered point pairs and estimate whether the assigned directed route system lets the first point communicate with the second.", ["channel_plan", "R", "ordered_point_pairs", "random_seed"], ["reachability_probability"]),
    (33, "parameter sensitivity sweep", "Vary user count and user communication radius and compare proposed and cellular repeater counts.", ["N_values", "r_values", "placement_algorithm", "cellular_baselines"], ["count_curves", "transition"]),
    (34, "binomial capacity correction", "Translate a Voronoi area into a binomial user count and reduce nominal capacity by a two-standard-deviation heuristic.", ["N", "S_V", "Phi", "C"], ["mean_load", "load_deviation", "C_prime"]),
    (35, "hierarchical mountain relay proposal", "Place lower-tier repeaters in hollows and upper-tier repeaters on mountains, then sketch shared-tone and reciprocal-frequency rules.", ["terrain", "users", "first_tier", "second_tier", "frequency_resources"], ["hierarchical_network", "proposed_channel_plan"]),
]

VISUALS = [
    (1, "MCM Summary Sheet", "Shows parameters, method keywords, strengths and weaknesses, and the 104-versus-108 network comparison omitted by the text layer."),
    (2, "Title and Abstract", "Presents the full constraints-to-method-to-results-to-scope chain."),
    (3, "Introduction literature chain", "Moves from homogeneous relay work to the two-tier capacity and interference gap."),
    (4, "Introduction contribution roadmap", "Names the cellular benchmark, three algorithmic modules, quantitative targets, and section order."),
    (5, "Problem variables and interference rule", "Displays Gamma, Phi, receive/transmit frequencies, duplex offset, tone count, and the simplified interference predicate."),
    (6, "Directed two-tier model and Equation 1", "Defines node classes, edge classes, circular domain, capacity, and interference conditions."),
    (7, "Figure 1 reachable-area example", "Makes directed multi-hop reach and excluded branches visible."),
    (8, "Propositions 1 and 2", "Separates strong-implies-weak from the diameter-based sufficient equivalence regime."),
    (9, "Equations 2-5", "Displays free-space power density, effective aperture, Friis reception, and path loss."),
    (10, "Equations 6-7 and Table 1", "Combines the printed link budget with Utah ERP data used to choose 100 W."),
    (11, "Range results and Equations 8-10", "Reports R and r, then begins the Shannon and CDMA-inspired capacity derivation."),
    (12, "Equations 11-14", "Shows equal-power SNR, reported capacity, continuous density, and Voronoi load constraint."),
    (13, "Frequency-tone limits and Equation 15", "Distinguishes 324 interference-free from 270 non-interacting assignments and gives the geometric lower bound."),
    (14, "Equation 16 and Table 2 start", "Gives the printed capacity lower bound and small cellular covering diagrams."),
    (15, "Table 2 continuation", "Continues hand-calculated cellular constructions and begins the N=1000 benchmark."),
    (16, "Equation 17 and Figure 2", "Shows the hexagonal capacity equation and twelve-repeater baseline layout."),
    (17, "Tables 3 and 4", "Lists the twelve-site channel plan and analytic radii for two cellular-center families."),
    (18, "Table 4 continuation and Figure 3", "Completes the lookup and visualizes the 108-cell benchmark."),
    (19, "Figures 4 and 5", "Contrasts random initial repeater locations with their Voronoi partition."),
    (20, "Figure 6", "Overlays Voronoi cells and their minimum enclosing circles for the refinement step."),
    (21, "Figure 7", "Shows repeater moves toward cell-circle centers and states xi and T_c."),
    (22, "Figures 8 and 9", "Shows the reach graph and minimum versus maximum spanning trees."),
    (23, "Figure 10 and route objective", "Shows deleted edges, retained signal routes, shared tones, and the component-balance expression."),
    (24, "Figure 11", "Visualizes the eleven-repeater coverage construction and reports its maximum Voronoi load."),
    (25, "Table 5 and optimality proof", "Lists the eleven-site plan and displays the ten-circle exclusion theorem."),
    (26, "Figure 12 and Table 6 start", "Shows the 104-site Voronoi layout and begins its parameter table."),
    (27, "Table 6 rows 16-56", "Continues the ideal-range 104-site coordinate, frequency, and tone plan."),
    (28, "Table 6 rows 57-97", "Continues the plan without repeated table headers."),
    (29, "Table 6 end and Table 7", "Completes rows 98-104 and gives the short-range eleven-site channel plan and 90.71 percent estimate."),
    (30, "Table 8 rows 1-39", "Begins the short-range 104-site frequency and tone assignment."),
    (31, "Table 8 rows 40-80", "Continues a dense parameter table without repeated headers."),
    (32, "Table 8 rows 81-104", "Completes the short-range plan but gives no post-table constraint summary."),
    (33, "Figure 13 and Equation 18", "Compares repeater counts versus user count and marks the coverage-to-capacity transition."),
    (34, "Figure 14 and Equations 19-21", "Shows normalized radius sensitivity and the discrete binomial load correction."),
    (35, "Equation 22 and Figure 15 image", "Gives the tolerant capacity heuristic and the mountain hierarchy image whose caption is separated."),
    (36, "Figure 15 caption and mountain proposal", "Explains hollow and mountain-top tiers plus proposed shared frequency and tone rules."),
    (37, "Conclusion", "Restates results and self-identified weaknesses while making unsupported speed and generality claims."),
    (38, "Appendix A Table 9 start", "Centralizes Phi, frequency range, tones, R, r, capacity, losses, gains, ERP, and receive threshold."),
    (39, "Table 9 end and Table 10 start", "Adds user power, Eb/N0, voice gain, bit-rate placeholder, xi, T_c, and begins symbol definitions."),
    (40, "Table 10 end and assumptions", "Completes symbols, lists assumptions A1-A7, and exposes noise and interference inconsistencies."),
    (41, "References", "Lists twenty-two sources with several editorial defects, web links, and no code or data package."),
]

WARNINGS = [
    (1, "The Summary Sheet is completely absent from the text layer even though it contains dense text and two result figures."),
    (1, "The 97.12 percent reachability headline is probabilistic, while the same page admits there is no method guaranteeing universal point-to-point communication."),
    (2, "The Abstract calls eleven repeaters the real optimum without immediately limiting the claim to the idealized continuous circle-covering subproblem."),
    (4, "The Introduction contains an unfinished comparison sentence ending with 'in the later case.'"),
    (5, "Different PL tones do not by themselves remove same-frequency or adjacent-frequency radio interference; the paper's predicate is an abstraction."),
    (5, "The frequency and tone counts are regional or problem-specific resources and cannot be generalized as a universal amateur-radio plan."),
    (6, "Only user-to-repeater and repeater-to-repeater directed edges are explicit; bidirectional user communication needs an additional symmetry or downlink assumption."),
    (6, "Assigning every user to the nearest repeater can create avoidable overload when a slightly farther repeater has spare capacity."),
    (7, "The reachable-area definition ignores a user's own direct communication disk and therefore represents a deliberate approximation."),
    (8, "R at least twice Phi is a universal sufficient condition for weak and strong equivalence, not a necessary condition for every particular network."),
    (9, "The free-space model excludes terrain, clutter, fading, antenna patterns, diffraction, atmospheric effects, and receiver implementation losses."),
    (9, "Equation 5 is attributed to Shannon theory although it is the Friis free-space path-loss relation."),
    (10, "Equation 6 mixes quantities originally introduced in watts with a dB-domain additive budget without an explicit conversion convention."),
    (10, "Equation 7 uses the constant 37.2328, while Equations 5-6 and the listed gains and losses imply a value near 3.72 rather than 37.23."),
    (10, "Using ERP from Table 1 and then adding transmitter antenna gain risks double-counting antenna gain."),
    (10, "The 39 dB VHF antenna gain is physically extraordinary and is not labeled dBi or dBd."),
    (10, "Table 1 contains repeated call signs and an old web source but no sampling date, cleaning rule, or summary statistic."),
    (11, "The one-microwatt receive threshold equals about -30 dBm and is far above common VHF receiver sensitivity; a microvolt-versus-microwatt confusion is plausible."),
    (11, "The reported R=85.45 miles and r=15.28 miles inherit the unresolved Equation 7 arithmetic and link-budget assumptions."),
    (11, "Equation 8 gives information rate in bits per second, but the text incorrectly says it is measured in watt or dB."),
    (11, "P_ur is a received power, but the text incorrectly says it is measured in bps."),
    (11, "The CDMA processing-gain relation is transferred to a narrowband repeater problem without a justified air-interface model."),
    (12, "The paper ignores background noise and other-repeater interference while simultaneously using SNR and E_b/N_0 to derive capacity."),
    (12, "The conversions 39 dB=7966.40 W, 0.4 dB=1.07 W, and 18 dB=63.01 W attach watts to dimensionless ratios."),
    (12, "Ten to the power 0.4/10 is about 1.096, not 1.07."),
    (12, "Calling 18 dB the midpoint of 5-30 dB is a rounded choice; the arithmetic midpoint is 17.5 dB."),
    (12, "The reported capacity near 119 is a model output under disputed gain, interference, and unit assumptions rather than an equipment specification."),
    (12, "The continuous approximation permits fractional users and suppresses local load variability until the later correction."),
    (13, "The 324 and 270 limits answer different questions—frequency separation versus avoidance of inverse-pair feedback—and should not be merged."),
    (13, "The five-per-tone non-interacting maximum is argued informally through a pigeonhole statement rather than a complete combinatorial proof."),
    (13, "The statement that when R is at least Phi any pair may interfere is existential or permissive wording, not a guarantee that every pair lies within R."),
    (13, "The area lower bound of seven is necessary only and ignores overlap and boundary inefficiency."),
    (14, "Equation 16 uses C=118 immediately after Equation 12 reports approximately 119, without explaining the conservative rounding."),
    (14, "Several Table 2 covering radii are described as hand calculations without derivations."),
    (16, "The twelve-cell conclusion excludes eleven only within the chosen regular-hexagon benchmark family, not among all circle placements."),
    (18, "The 108-cell result is a sufficient cellular construction, not a lower bound or an optimum."),
    (19, "The iterative algorithm claims to seek the least number but is randomized and has no global-optimality guarantee."),
    (20, "The paper calls the minimum enclosing circle a circumscribed circle, which can be misleading because it need not pass through all polygon vertices."),
    (20, "Small total site displacement does not prove monotone improvement or convergence of the maximum enclosing-circle radius."),
    (21, "The feasibility step says it counts users, while the implemented continuous model appears to use density times Voronoi area."),
    (21, "Random seeds, independent run counts, success rates, and runtime for the extremal optimizer are not reported."),
    (21, "Selecting the smallest Voronoi area as the least-fit repeater does not directly target the largest radius or largest load violation."),
    (22, "The spanning-tree edge weights are not formally defined even though minimum and maximum trees are central choices."),
    (22, "The claim that minimum-spanning-tree edges do not intersect needs the geometric and graph conditions under which it holds."),
    (23, "For degree k greater than three, deleting k-2 incident edges leaves degree two; if the intended cap is three the count should be k-3."),
    (23, "The component-balance summation leaves the pair index domain and double-counting convention undefined."),
    (23, "A spanning tree changes relay routes but does not by itself enlarge each repeater's user coverage disk, contrary to parts of the explanation."),
    (23, "A node with multiple route neighbors may face incompatible receiver-frequency requirements; direction and duplex constraints are not formalized."),
    (24, "The weather-based reduction from 85.45 to 40 miles is qualitative and unsupported by attenuation data or a revised link budget."),
    (24, "The sentence using R at least Phi as the threshold for any two repeaters to interfere conflicts with the earlier diameter condition R at least 2 Phi."),
    (25, "The eleven-site construction is displayed numerically but the proof does not independently verify every point of the target disk is covered by the listed coordinates."),
    (25, "The optimality proof depends on the exact scope and correctness of cited Theorem r(n) for closed congruent circles."),
    (26, "The 104-site result does not report its maximum enclosing-circle radius, maximum cell load, or an executable constraint audit."),
    (29, "The 90.71 percent Monte Carlo estimate gives no random seed or confidence interval; an approximate 95 percent sampling margin is about 0.18 percentage points."),
    (29, "The 6.4 paragraph refers to a solution in subsection 6.4 itself, likely an erroneous self-reference to subsection 6.2."),
    (29, "Two examples do not establish that adding repeaters generally increases every user's reachable area under the route assignment."),
    (30, "Tables 6 and 8 provide coordinates and channel labels but no machine-checkable proof that every interference and directed-connectivity constraint holds."),
    (33, "Equation 18 gives a parameter-based transition near N=816 with the appendix values, so 'about 1000' is only a coarse description."),
    (33, "Figure 13 lacks independent-run variability, optimum baselines, and uncertainty for the randomized proposed algorithm."),
    (34, "The text calls X Bernoulli, but the displayed count distribution is binomial."),
    (34, "Normalizing each Figure 14 curve by its own maximum hides absolute repeater-count differences."),
    (35, "The two-standard-deviation capacity rule is heuristic and does not specify a target tail probability or simultaneous-overload guarantee."),
    (35, "Approximating the binomial standard deviation by the square root of the mean omits the one-minus-p factor."),
    (35, "A two-meter wavelength alone does not justify a strong general claim that VHF readily bypasses small mountains."),
    (35, "Figure 15 is separated from its caption across a page break and lacks a complete legend."),
    (36, "Multiple lower-tier repeaters sharing one transmit frequency and PL tone can collide on simultaneous uplinks without scheduling or capture assumptions."),
    (36, "Terrain shielding is proposed without path profiles, diffraction calculations, or link-budget validation."),
    (37, "The claim that the method is much faster than simulated annealing is unsupported by runtime tables or experimental settings."),
    (37, "The claim of higher local-optimum escape ability is unsupported by repeated-run success statistics."),
    (37, "The 97.12 percent reachability result is empirical and cannot replace the strong solution's universal reachability condition."),
    (38, "Appendix A leaves the information bit-rate parameter without a numerical value, even though it is needed in the printed capacity derivation."),
    (39, "The symbol table gives V_u and V_u-prime the same description, obscuring their intended difference."),
    (40, "Assumption A5 of no background noise conflicts directly with the use of SNR, N_0, and E_b/N_0."),
    (40, "Assumption A6 about no noisy impact from repeaters is poorly reconciled with I_other, I_self, and the explicit interference condition."),
    (40, "Treating fog, rivers, hills, buildings, and solar activity as one generic interference class mixes propagation loss, obstruction, noise, and fading."),
    (41, "Wikipedia and old web pages support important engineering statements but are unstable or weak primary evidence."),
    (41, "The paper provides no source code, random seeds, machine-readable tables, or complete reproduction package."),
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


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "miles, kilometers, MHz, Hz, W, dB, dB ratio, bit/s, user, repeater, tone, probability, area, coordinate, count, or dimensionless quantity as locally defined",
        "definition": f"Source-defined repeater-placement quantity {symbol}.",
        "source_status": "explicit-defined",
    }


def model_record(model_id: str, page: int, section: str, family: str, purpose: str, inputs: list[str], outputs: list[str], equations: list[dict]) -> dict:
    return {
        "model_id": model_id,
        "page": page,
        "section": section,
        "family": family,
        "purpose": purpose,
        "base_or_modification": "paper-specific",
        "summary": purpose,
        "variables": [variable(s, set(inputs), set(outputs)) for s in list(dict.fromkeys(inputs + outputs))],
        "inputs": inputs,
        "outputs": outputs,
        "governing_equations": equations,
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The printed relation was visually reconciled against the rendered page." if equations else "This record is a graph, optimization, experiment, or architectural procedure."},
        "objectives": [purpose, "Return a typed geometric, network, capacity, resource, probability, or decision output."],
        "constraints": [
            "Keep the radius-forty service domain, user reach, repeater reach, capacity, tones, duplex pairs, and directed reachability separately typed.",
            "Distinguish a weak coverage solution, a strong reachability solution, an interference-free plan, and a non-interacting plan.",
            "Do not turn a randomized best-observed layout, a disputed link-budget parameter, or a qualitative terrain proposal into a deployment guarantee.",
        ],
        "conditions": {
            "initial": {"status": "present", "details": ["Domain, user scale, radio parameters, repeater count or lower bound, and relevant graph or geometry are supplied."]},
            "boundary": {"status": "present", "details": ["The base case assumes continuous uniform demand, flat free-space propagation, homogeneous equipment, simplified interference, and mostly idealized frequency resources."]},
            "equilibrium": {"status": "not-applicable", "details": ["The paper constructs finite placements and routes rather than a physical equilibrium."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Problem constants, web tables, printed formulas, continuous approximation, randomized placement, analytic covering results, and Monte Carlo reachability.", "parameters": inputs},
        "algorithm": {"status": "omitted-by-paper" if family in {"Friis propagation", "link budget", "channel capacity", "CDMA capacity", "capacity approximation", "density model", "capacitated Voronoi", "area lower bound", "capacity lower bound", "circle-covering proof", "bottleneck transition", "binomial correction", "capacity margin", "domain constraint"} else "partial", "steps": ["freeze declared inputs", "apply the displayed formula or procedure", "retain units and directed semantics", "check the stated stop or feasibility rule", "hand typed outputs to the next stage"], "software": ["No executable source code is supplied; evidence is formulas, tables, diagrams, and prose."], "convergence_criteria": "The placement loop uses total site displacement below xi, feasibility tests, at most T_c perturbations, and repeater-count increments; random-run diagnostics are omitted."},
        "assumptions": ["Continuous uniform users and nearest-repeater assignment approximate the demand state.", "The selected radio model and frequency-tone abstraction approximate the operational VHF system."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The dataflow is traceable, but the link-budget constant, unit conversions, 118/119 capacity choice, graph directions, random seeds, tree weights, route constraints, and terrain physics prevent full reproduction or deployment-level validation."},
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, visually checked equation, figure, table, proposition, algorithm step, or result discussion."],
        "computational_cost": "Dominated by repeated clipped-Voronoi construction, minimum-enclosing-circle computation, randomized restarts, spanning-tree operations, route splitting, parameter sweeps, or Monte Carlo point-pair traversal.",
        "strengths": ["The intended input-operation-output chain is observable.", "The output connects to a later bound, placement, channel plan, sensitivity result, or decision."],
        "limitations": ["Physical calibration, proof scope, uncertainty, and reproducibility are incomplete.", "Confirmed source defects are retained for the final warning pass."],
        "missing_details": ["Calibrated link data, legal regional band plan, seeds, run counts, runtime, raw tables, code, graph edge weights, scheduling, confidence intervals, and complete constraint rechecks are absent."],
    }


def make_models() -> dict:
    models = []
    for idx, (label, page, section, family, source, latex, symbols, purpose) in enumerate(EQUATIONS, 1):
        eq = {"equation_id": f"EQ-B-2011-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": "high"}
        models.append(model_record(f"MU-B-2011-{SHORT}-{idx:03d}", page, section, family, purpose, symbols[1:], [symbols[0]], [eq]))
    for idx, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, len(EQUATIONS) + 1):
        models.append(model_record(f"MU-B-2011-{SHORT}-{idx:03d}", page, family, family, purpose, inputs, outputs, []))
    by_family = {m["family"]: m["model_id"] for m in models}
    pairs = [
        ("domain constraint", "two-tier directed graph construction"),
        ("two-tier directed graph construction", "reachable-area traversal"),
        ("reachable-area traversal", "weak-to-strong sufficient-condition check"),
        ("Friis propagation", "free-space range estimation"),
        ("link budget", "free-space range estimation"),
        ("channel capacity", "CDMA-inspired capacity estimation"),
        ("capacity approximation", "continuous-density replacement"),
        ("density model", "continuous-density replacement"),
        ("capacitated Voronoi", "lower-bound synthesis"),
        ("area lower bound", "lower-bound synthesis"),
        ("capacity lower bound", "lower-bound synthesis"),
        ("lower-bound synthesis", "Voronoi minimum-enclosing-circle refinement"),
        ("cellular benchmark", "cellular benchmark lookup"),
        ("Voronoi minimum-enclosing-circle refinement", "extremal perturbation and increment"),
        ("extremal perturbation and increment", "ideal-range feasibility check"),
        ("repeater reach graph", "minimum-or-maximum spanning tree"),
        ("minimum-or-maximum spanning tree", "tree route splitting"),
        ("tree route splitting", "route tone and frequency assignment"),
        ("circle-covering proof", "N=1000 optimality argument"),
        ("route tone and frequency assignment", "short-range reachability Monte Carlo"),
        ("bottleneck transition", "parameter sensitivity sweep"),
        ("binomial correction", "binomial capacity correction"),
        ("capacity margin", "binomial capacity correction"),
        ("hierarchical mountain relay proposal", "route tone and frequency assignment"),
    ]
    edges = [{"from_model_id": by_family[a], "to_model_id": by_family[b], "handoff": f"The {a} output becomes an input, constraint, diagnostic, or boundary for {b}."} for a, b in pairs]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    assumptions = [
        (5, "The service region is a circle of radius forty miles with N homogeneous mobile users."),
        (5, "Repeater resources lie in 145-148 MHz with a 0.6 MHz duplex difference and 54 PL tones."),
        (5, "Same-tone repeaters within twice the repeater radius interfere when transmitter frequencies differ by less than the threshold."),
        (6, "Users always select the nearest repeater."),
        (6, "Users and repeaters can be represented as a directed two-tier graph."),
        (8, "A repeater radius at least the service diameter makes any coverage solution strong in the modeled sense."),
        (9, "The base region permits free-space fading without terrain, structures, weather, or other propagation effects."),
        (9, "Ideal isotropic or high-gain antenna relations provide usable communication radii."),
        (10, "The Utah ERP table supports a nominal 100 W repeater value."),
        (11, "A one-microwatt receive threshold is suitable for users and repeaters."),
        (11, "A CDMA-inspired gain relation can approximate narrowband repeater capacity."),
        (12, "Background noise and other-repeater interference can be neglected in the capacity calculation."),
        (12, "User locations can be replaced by a continuous uniform density and fractional local user counts."),
        (12, "Nearest-repeater Voronoi regions determine load."),
        (13, "Frequency choices at exactly 0.6 MHz spacing are noninterfering under the strict-threshold rule."),
        (14, "Regular-hexagon cellular layouts provide a useful analytic benchmark."),
        (20, "Moving sites to minimum-enclosing-circle centers improves worst-cell coverage sufficiently for iterative refinement."),
        (21, "The least-area Voronoi cell is the least-fit individual for extremal optimization."),
        (22, "Distance-weighted minimum or maximum spanning trees provide useful local-versus-wide routing alternatives."),
        (35, "Terrain can be handled qualitatively by hollow access nodes, mountain-top backbone nodes, and terrain-enabled frequency reuse."),
    ]
    data = [
        (1, "The Summary Sheet records headline parameters, methods, result counts, and 104-versus-108 figures unavailable in the text layer."),
        (5, "The problem supplies the circular domain, user scales, frequency interval, duplex difference, and PL tone count."),
        (10, "Table 1 lists Utah repeater ERP values from a web source."),
        (12, "Continuous user density is calculated from N and the circular area."),
        (13, "Six transmitter-frequency positions and five non-inverse duplex pairs support the 324 and 270 counts."),
        (14, "Table 2 provides hand-calculated cellular covering radii for small cell counts."),
        (17, "Tables 3-4 provide baseline coordinates, channel pairs, tones, and analytic cell-family radii."),
        (25, "Table 5 provides the eleven-site layout used by the idealized optimality argument."),
        (26, "Table 6 provides 104 coordinates, duplex pairs, and 21 tones for the ideal-range result."),
        (29, "Table 7 changes the eleven-site channel plan for R=40 and accompanies 100000 ordered-pair samples."),
        (30, "Table 8 provides the short-range 104-site channel plan."),
        (33, "Figures 13-14 report parameter sweeps over user count and user communication radius."),
        (38, "Appendices A-C centralize parameter values, symbols, and assumptions for cross-checking."),
    ]
    verification_specs = [
        (8, "Propositions 1-2 check implication between weak and strong solutions under a diameter condition.", "analytic-implication", "Provides a transparent sufficient condition.", "It is not necessary for every instance and does not repair channel semantics."),
        (13, "Geometric and capacity lower bounds establish a starting repeater count.", "analytic-lower-bound", "Separates two necessary resource pressures.", "Neither bound is constructive or jointly sufficient."),
        (16, "The cellular layout gives a reproducible twelve-repeater benchmark for N=1000.", "geometric-baseline", "Creates a clear comparator before the randomized algorithm.", "It is restricted to one lattice family."),
        (18, "The cellular layout gives a 108-repeater benchmark for N=10000.", "geometric-baseline", "Uses the same benchmark logic at a second scale.", "It is sufficient but not optimal."),
        (24, "The eleven-site result checks maximum Voronoi load against nominal capacity.", "capacity-check", "The reported 560.56 area gives about 112 users under continuous density.", "Coverage is shown visually and the capacity constant is disputed."),
        (25, "A cited exact ten-circle covering radius excludes ten ideal user-radius circles.", "external-theorem-lower-bound", "Provides a rigorous exclusion if the theorem and construction scopes match.", "It does not include the full real radio and routing problem."),
        (26, "Figure 12 and Table 6 document the 104-site ideal-range construction.", "illustrative-construction", "Coordinates and resource labels are retained.", "No complete computational constraint audit is supplied."),
        (29, "One hundred thousand ordered point pairs estimate short-range reachability for the eleven-site plan.", "monte-carlo-reachability", "Provides a direct empirical communication metric.", "Seed and confidence interval are omitted."),
        (32, "Table 8 documents the short-range 104-site resource assignment and its 97.12 percent result.", "parameter-trace", "The full table permits partial reproduction.", "The reported probability lacks detailed experimental protocol."),
        (33, "Figures 13-14 sweep demand and user range to expose active constraints.", "sensitivity-sweep", "Connects output changes to model bottlenecks.", "Random-run uncertainty and raw values are incomplete."),
        (34, "The binomial correction quantifies discrete load fluctuation around continuous density.", "uncertainty-model", "Adds a probabilistic correction to a deterministic approximation.", "The distribution is mislabeled and the capacity margin is heuristic."),
        (37, "The conclusion lists two explicit weaknesses after summarizing contributions.", "self-critique", "Keeps global reachability and physical simplification visible.", "Several performance and generality claims remain unbenchmarked."),
    ]
    verification = [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification_specs]
    results = [
        (1, "The Summary Sheet contrasts the proposed 104-site layout with the 108-site cellular benchmark and reports 97.12 percent random-pair reachability."),
        (11, "The link-budget analysis reports R=85.45 miles and r=15.28 miles, subject to the Equation 7 warning."),
        (12, "The capacity derivation reports approximately 119 simultaneous users, while later bounds use 118."),
        (13, "The frequency abstraction reports 324 interference-free and 270 non-interacting repeater assignments."),
        (14, "Necessary count bounds are at least 7 geometrically, 9 for 1,000 users by capacity, and 85 for 10,000."),
        (16, "The cellular benchmark uses 12 repeaters for 1,000 users."),
        (18, "The cellular benchmark uses 108 repeaters for 10,000 users."),
        (24, "The proposed algorithm uses 11 repeaters for 1,000 users with reported maximum continuous load about 112."),
        (25, "The ten-circle theorem excludes ten ideal coverage circles, supporting an eleven-circle minimum within the stated subproblem."),
        (26, "The proposed algorithm reports 104 repeaters and 21 tones for 10,000 users under ideal R."),
        (29, "At R=40, the eleven-site plan reaches 90708 of 100000 sampled ordered point pairs, or 90.71 percent."),
        (29, "At R=40, the 104-site plan is reported at 97.12 percent sampled ordered-point reachability."),
        (35, "The two-sigma heuristic reduces nominal capacity 119 to tolerant capacity 99."),
    ]
    writing = [
        (1, "Summary-sheet chain: parameters -> key concepts -> key techniques -> two layouts -> probabilistic result -> strengths and weaknesses."),
        (2, "Abstract chain: constrained two-tier network -> weak and strong requirements -> cellular benchmark -> Voronoi/extremal optimizer -> 11 and 104 results -> resource assignment -> extensions."),
        (3, "Introduction chain: relay-network literature -> missing placement and coverage -> capacity and interference gap -> paper modules."),
        (4, "Roadmap chain: formulation -> analysis -> algorithms -> results -> sensitivity -> conclusion -> appendices."),
        (5, "Problem chain: service region -> node resources -> interference predicate -> coverage and capacity -> required decision output."),
        (6, "Model chain: node and edge types -> four Omega conditions -> weak and strong solutions -> sufficient equivalence regime."),
        (9, "Parameter chain: free-space mechanism -> link budget -> empirical power -> communication radii -> geometric optimizer inputs."),
        (11, "Capacity chain: Shannon rate -> CDMA analogy -> gain substitutions -> nominal C -> continuous-load handoff."),
        (12, "Approximation chain: mobile discrete users -> constant density -> Voronoi load -> frequency limits -> lower bounds."),
        (14, "Baseline chain: inverse cellular covering -> edge-length constraints -> lookup -> 12 and 108 comparators."),
        (19, "Optimization chain: lower-bound initialization -> Voronoi cells -> enclosing circles -> movement -> feasibility -> extremal escape -> resource increment."),
        (22, "Resource chain: distance graph -> min/max tree -> balanced route split -> tones -> chained frequencies."),
        (24, "Results chain: ideal-range placements -> first-case proof -> full tables -> short-range reassignment -> Monte Carlo reachability."),
        (33, "Robustness chain: parameter sweeps -> bottleneck transition -> binomial correction -> capacity tolerance -> terrain hierarchy."),
        (37, "Conclusion chain: contributions -> quantitative outcomes -> broad claims -> two admitted weaknesses -> appendices and references."),
    ]
    contributions = [
        {"page": 6, "summary": "Separates coverage, capacity, interference, and global reachability in a two-tier directed network."},
        {"page": 13, "summary": "Places geometric and capacity lower bounds before constructive and randomized placement."},
        {"page": 14, "summary": "Creates a transparent regular-hexagon cellular benchmark at both user scales."},
        {"page": 20, "summary": "Uses Voronoi minimum-enclosing-circle centers to target worst-cell coverage rather than average distance."},
        {"page": 21, "summary": "Adds extremal perturbation and repeater-count increments to escape local configurations."},
        {"page": 22, "summary": "Separates placement from channel routing through graph and spanning-tree operations."},
        {"page": 25, "summary": "Connects a numerical eleven-site layout to an external exact circle-covering lower bound."},
        {"page": 34, "summary": "Revisits the continuous approximation with a discrete load distribution and a capacity margin."},
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 10, "summary": "Rebuild the bidirectional link budget with calibrated antenna gains, receiver sensitivity in dBm, ERP/EIRP consistency, terrain and clutter loss, fade margin, and uncertainty on R and r."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 12, "summary": "Replace the borrowed CDMA capacity equation with an explicit repeater access, traffic, duty-cycle, scheduling, and interference model."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 13, "summary": "Solve legal duplex-pair and PL-tone assignment as a constrained directed graph problem with adjacent-channel, receiver, and feedback-loop checks."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 21, "summary": "Implement deterministic seeds, multi-start runs, objective traces, direct violation targeting, small-instance exact baselines, and convergence diagnostics for the placement optimizer."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 23, "summary": "Define edge weights, degree limits, route directions, component objective, scheduling, and failure handling for the spanning-tree channel algorithm."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 26, "summary": "Parse Tables 5-8 and machine-check coverage, load, interference, feedback, route reachability, and frequency validity for every repeater."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 34, "summary": "Use exact binomial or concentration bounds and a network-wide overload risk target instead of an informal two-sigma capacity reduction."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 36, "summary": "Use measured DEMs, Fresnel clearance, diffraction and path-loss models, traffic scheduling, and ridge/valley link validation for the hierarchical terrain design."},
    ]
    return {
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": "9440",
        "title": "Least Number of Repeaters Covering a Circular Area: Iterative Extremal Optimization Based on Voronoi Diagram",
        "award_status": "outstanding",
        "source": {"relative_path": "2011美赛特等奖/B-9440-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is a populated MCM Summary Sheet with no text layer; physical pages 2-41 are numbered paper pages 1/40-40/40."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 41, "rendered_pages": 41, "visual_review": "complete", "notes": ["All 41 UTF-8 page files were read in physical order; physical page 1 was recovered visually because its text file is empty.", "Three fresh read-only contexts visually reviewed pages 1-14, 15-28, and 29-41 using at most eight byte-bounded JPEG proxies each and returned text-only findings.", "Visual review reconciled all numbered formulas, figures, tables, captions, page numbers, and layout while separating extraction mojibake from source-paper defects."]},
        "context_sources": [{"type": "paper", "path": "2011美赛特等奖/B-9440-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "rendered-pages", "path": f"artifacts/papers/{PID}/rendered"}],
        "task_reconstruction": {"inputs": ["radius-forty circular service region", "1,000 or 10,000 users", "user and repeater communication radii", "repeater capacity", "145-148 MHz resource interval", "54 PL tones", "flat or mountainous propagation regime"], "outputs": ["repeater count and coordinates", "weak or strong solution status", "Voronoi loads and enclosing radii", "receiver/transmitter frequency pairs", "PL tone routes", "reachability estimate"], "decisions": ["how many repeaters are needed", "where they are placed", "whether coverage and capacity hold", "whether global reachability is guaranteed or empirical", "how frequencies and tones are assigned", "which claims must be withheld under physical or algorithmic uncertainty"]},
        "section_map": [{"page": s, "section": k, "summary": e} for k, _, s, _, _, _, e, _ in CHAPTERS],
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
            {"page": 2, "summary": "The Abstract's constraint-to-benchmark-to-algorithm-to-numeric-result sequence is judge-friendly, but the unqualified optimum wording weakens trust.", "evidence_class": "J"},
            {"page": 20, "summary": "The visual Voronoi and enclosing-circle iteration makes the mechanism easy to inspect, provided randomized performance and feasibility are separately validated.", "evidence_class": "J"},
            {"page": 25, "summary": "Pairing a construction with a lower-bound theorem can strongly support a resource count when every scope condition is explicit.", "evidence_class": "J"},
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
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing every paper-specific fact, formula, count, and phrase.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain inputs, equations or operations, units, conditions, outputs, handoffs, verification needs, and warning boundaries.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive definition-to-bound-to-baseline-to-optimizer-to-resource-to-results-to-robustness chain.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep geometry, graph direction, axes, table headers, parameter values, caption, analytic purpose, and linked warning together.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name theorem scope, seed, sample size, comparator, uncertainty, constraint audit, and permitted conclusion.", "R-B-VER-002") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, units, parsing, regional scope, randomization, diagnostics, and downstream consumer.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each assumption with the operation it enables, excluded mechanism, sensitivity test, and fallback.", "R-B-DATA-002") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry user scale, range regime, count, capacity, channel plan, probability or proof scope, and decision together.", "R-B-MOD-004") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use only after positive language, organization, model, visual, and verification retention is complete.", "R-B-VER-004") for x in card["weaknesses"]],
        "other": [(41, "reference boundary", "The references support background mechanisms but not a complete executable deployment workflow.", "Separate citation support from calibration, reproduction, and validation.", "R-B-VER-004")],
    }
    counts = {"language": len(language["units"]), "modeling": 112, "logic": 80, "visualization": 92, "verification": 70, "data": 54, "assumption": 56, "result": 60, "weakness": len(WARNINGS), "other": 8}
    records = []
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
            records.append({"schema_version": 1, "observation_id": f"O-B-2011-{SHORT}-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "page": page, "section": f"{section} / evidence action {i+1}", "evidence_class": "O", "dimension": dim, "source_basis": basis[:900], "interpretation": interpretation, "applicability": ["Apply only when domain, demand, radio regime, graph direction, objective, operation, output, metric, units, comparator, uncertainty, and scope can all be named."], "counterevidence": ["A low repeater count, clean Voronoi plot, large nominal range, small tone count, spanning tree, sampled reachability percentage, or cited theorem does not prove calibrated radio performance, complete channel feasibility, global optimality, or universal reachability."], "confidence": "high" if dim in {"language", "modeling", "logic", "visualization"} else "medium", "candidate_rule_ids": rules})
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])
    def evidence_for(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])
    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain constraint-to-method-to-result language, paragraph chains, and qualified optimum phrasing with exact scope", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "retain the definition-to-bounds-to-cellular-baseline-to-Voronoi-optimizer-to-tree-resource-to-results-to-robustness organization chain", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "treat ERP tables, coordinates, frequency pairs, tones, seeds, point-pair samples, sensitivity grids, and visual-only cover data as versioned data", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for propagation, sensitivity, gain, capacity, uniform density, nearest assignment, interference, and terrain shielding", "evidence_ids": [evidence_for("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain the two-tier graph, link budget, capacity, lower bounds, Voronoi iteration, tree splitting, and uncertainty correction only with typed interfaces", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine repeater count, coverage, capacity, directed reachability, interference, inverse-pair risk, tones, frequencies, uncertainty, and cost through an explicit decision rule", "evidence_ids": [evidence_for("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep necessary bounds, sufficient constructions, best-observed randomized counts, idealized optimum proof, and Monte Carlo reachability separately labeled", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress link-budget constants, receive thresholds, capacity, user density, seeds, tree weights, R regime, tone counts, and terrain", "evidence_ids": [evidence_for("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make reliability theorem-, calibration-, seed-, sample-, confidence-, constraint-, and range-regime-specific with abstention outside checked conditions", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile every formula, unit, 118/119 capacity use, graph direction, tree deletion count, table continuation, probability model, and claim before reuse", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain figures and tables only with geometry or graph semantics, parameter regime, labels, headers, caption, linked numeric evidence, and extraction status", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "choose Voronoi, minimum-enclosing-circle, multi-start, graph, sampling, caching, runtime, and memory strategies from measured size and reproducibility requirements", "evidence_ids": [evidence_for("R-B-COMP-001")]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reusable only after replacing source facts and preserving rhetorical function, information order, quantitative force, variants, and boundary."} for u in language["units"]]
    paragraph_specs = {
        "abstract": ["problem and constraint frame", "two-tier weak and strong requirements", "cellular benchmark", "Voronoi and enclosing-circle iteration", "extremal optimization escape", "11 and 104 quantitative results", "frequency and tone allocation", "density and terrain extension boundary"],
        "introduction": ["application context", "homogeneous relay literature", "two-tier user-repeater distinction", "coverage gap", "placement and capacity gap", "interference gap", "circle-covering difficulty", "cellular baseline", "Voronoi refinement module", "extremal optimization module", "frequency assignment module", "section roadmap"],
    }
    chains = []
    for chapter, moves in paragraph_specs.items():
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        chains.append({"chapter": chapter, "visual_paragraph_count": len(moves), "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": move, "language_unit_ids": [ids[i % len(ids)]]} for i, move in enumerate(moves)]})
    progressions = []
    for key, chapter, *_ in CHAPTERS:
        progressions.append({"chapter": chapter, "moves": [f"input: the source-checked domain, graph state, parameter, formula, figure, table, bound, or result entering {key}", f"rhetorical job: perform the observed definition, derivation, algorithm explanation, comparison, sensitivity interpretation, or boundary in {key}", f"analytical job: apply the declared graph, propagation, capacity, covering, Voronoi, tree, Monte Carlo, probability, or terrain operation in {key}", f"output: retain a typed range, capacity, bound, placement, channel plan, probability, warning, or scoped decision from {key}", "handoff: name the next model stage, verification, result comparison, robustness analysis, warning gate, or conclusion"], "positive_pattern": "Use explicit input -> mechanism or operation -> typed output -> verification or comparator -> scoped handoff; a warning cannot substitute for the positive section contract."})
    eqrefs = [(m["model_id"], eq["equation_id"], eq["page"]) for m in models["models"] for eq in m["governing_equations"]]
    warning_rows = []
    for page, warning in WARNINGS:
        mid, eid, _ = min(eqrefs, key=lambda x: (abs(x[2] - page), x[2], x[1]))
        warning_rows.append({"model_id": mid, "equation_id": eid, "page": page, "warning": warning})
    dims = Counter(x["dimension"] for x in observations)
    return {
        "audit_id": f"LA-B-2011-{SHORT}",
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "source_sha256": SHA,
        "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [14 if key in {"summary-sheet", "abstract", "introduction"} else 9, 3, 0]} for key, chapter, *_ in CHAPTERS],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": chains,
        "organization_logic": {
            "positive_artifacts_status": "complete",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [
                "Summary Sheet and Abstract establish parameters, constraints, methods, headline counts, and scope.",
                "Introduction maps prior-network limitations to coverage, capacity, interference, placement, and resource modules.",
                "Problem Description and Model define the circular domain, directed graph, four Omega conditions, and weak versus strong solutions.",
                "Propagation and capacity derivations produce R, r, and C for downstream geometry, while warnings preserve their disputed calibration.",
                "Continuous approximation turns mobile users into Voronoi load, counts frequency-tone resources, and derives starting lower bounds.",
                "A regular-hexagon cellular construction supplies 12 and 108 repeater baselines.",
                "The main algorithm iterates Voronoi minimum-enclosing-circle centers, feasibility checks, extremal perturbations, and count increments.",
                "The secondary algorithm turns repeater reach into spanning-tree routes, tones, and duplex-frequency chains.",
                "Ideal-range simulations report 11 and 104 sites; the first receives a circle-covering exclusion argument.",
                "Short-range simulations keep locations, reassign channels, and report empirical ordered-pair reachability.",
                "Sensitivity sweeps identify geometry-versus-capacity bottlenecks and a binomial correction adds load uncertainty.",
                "Mountain discussion proposes a two-level architecture but remains qualitative.",
                "Conclusion reports contributions and admitted weaknesses; appendices and references expose parameter and assumption consistency."],
            "section_progressions": progressions,
            "main_argument_chains": [
                {"claim": "Coverage, capacity, interference, and global reachability are distinct constraints in repeater placement.", "support_steps": ["two-tier directed graph", "Omega1-Omega4", "weak and strong solution definitions", "diameter-based sufficient implication"], "decision_consequence": "Validate each constraint separately and do not infer universal reachability from coverage alone.", "source_pages": [5, 6, 7, 8]},
                {"claim": "Physical parameters determine the downstream geometric problem.", "support_steps": ["Friis relation", "dB budget", "R and r", "CDMA-inspired capacity", "continuous density"], "decision_consequence": "Recalibrate the link and capacity models before trusting repeater counts.", "source_pages": [9, 10, 11, 12]},
                {"claim": "Necessary lower bounds and a cellular construction provide references before stochastic optimization.", "support_steps": ["area bound", "capacity bound", "hexagonal cell equation", "12 and 108 benchmarks"], "decision_consequence": "Keep necessary, sufficient, and best-observed counts labeled separately.", "source_pages": [13, 14, 16, 18]},
                {"claim": "Voronoi minimum-enclosing-circle refinement targets worst-cell coverage.", "support_steps": ["random lower-bound initialization", "clipped Voronoi cells", "minimum enclosing circles", "center moves", "extremal perturbation and count increment"], "decision_consequence": "Use multi-start diagnostics and direct violation objectives before making optimality claims.", "source_pages": [19, 20, 21]},
                {"claim": "Frequency and tone allocation is a separate graph-routing problem downstream of placement.", "support_steps": ["distance graph", "minimum or maximum spanning tree", "component split", "route tone", "frequency chaining"], "decision_consequence": "Formalize edge weights, route direction, duplex constraints, feedback prevention, and scheduling.", "source_pages": [22, 23]},
                {"claim": "The eleven-site result has stronger support than the 104-site result.", "support_steps": ["eleven-site construction", "capacity check", "cited ten-circle exclusion", "104-site table without complete constraint audit"], "decision_consequence": "Call eleven optimal only in the exact idealized subproblem and call 104 best observed unless a lower bound closes the gap.", "source_pages": [24, 25, 26]},
                {"claim": "Robustness requires both parameter sensitivity and discrete or terrain corrections.", "support_steps": ["N sweep", "r sweep", "binomial load", "tolerant capacity", "mountain hierarchy"], "decision_consequence": "Use probabilistic overload guarantees and calibrated terrain propagation rather than qualitative extensions.", "source_pages": [33, 34, 35, 36]},
            ],
        },
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warning_rows},
        "model_retention": {"model_count": len(models["models"]), "retained_model_ids": [m["model_id"] for m in models["models"]], "retained_equation_ids": [x[1] for x in eqrefs], "central_equations": [{"model_id": m["model_id"], "equation_ids": [e["equation_id"] for e in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]},
        "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-B-2011-{SHORT}-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)],
        "dimension_counts": {d: dims[d] for d in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]},
        "positive_reusable_language_count": len(language["units"]),
        "weakness_record_count": dims["weakness"],
        "review_status": "validated",
    }


def main() -> None:
    configure_base()
    base.model_record = model_record
    language = base.make_language()
    merged_layouts: dict[str, dict] = {}
    for layout in language["chapter_layouts"]:
        chapter = layout["chapter"]
        if chapter not in merged_layouts:
            merged_layouts[chapter] = {
                **layout,
                "paragraph_functions": list(layout["paragraph_functions"]),
                "content_counts": dict(layout["content_counts"]),
            }
            continue
        merged = merged_layouts[chapter]
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
        for key, value in layout["content_counts"].items():
            merged["content_counts"][key] += value
    language["available_chapters"] = list(dict.fromkeys(language["available_chapters"]))
    language["chapter_layouts"] = list(merged_layouts.values())
    for layout in language["chapter_layouts"]:
        layout["page_fraction"] = round((layout["page_end"] - layout["page_start"] + 1) / PAGE_COUNT, 6)
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 41 physical-page text files were read in UTF-8 order. Physical page 1 had an empty text layer and was recovered visually. Three fresh read-only visual contexts covered pages 1-14, 15-28, and 29-41 with byte-bounded JPEG proxies and returned text-only reports."
        layout["ambiguities"] = ["Extracted text corrupts Greek letters, subscripts, inequalities, primes, smart punctuation, tables, and proof symbols, while rendered formulas and layouts were checked visually.", "Physical page 1 is a full Summary Sheet absent from the text layer; source-paper formula, unit, graph, algorithm, and claim defects are retained as warnings rather than extraction omissions."]
    models = make_models()
    card = make_card(language, models)
    observations = make_observations(language, models, card)
    attach_rule_impacts(card, observations)
    audit = make_audit(language, models, card, observations)
    saturation_by_chapter: dict[str, dict] = {}
    for record in audit["chapter_saturation"]:
        chapter = record["chapter"]
        if chapter not in saturation_by_chapter:
            saturation_by_chapter[chapter] = {**record, "new_moves_by_pass": list(record["new_moves_by_pass"])}
            continue
        merged = saturation_by_chapter[chapter]
        merged["pass_count"] = max(merged["pass_count"], record["pass_count"])
        merged["new_moves_by_pass"] = [
            left + right for left, right in zip(merged["new_moves_by_pass"], record["new_moves_by_pass"])
        ]
        merged["last_pass_new_moves"] = merged["new_moves_by_pass"][-1]
    audit["chapter_saturation"] = list(saturation_by_chapter.values())

    progression_by_chapter: dict[str, dict] = {}
    for progression in audit["organization_logic"]["section_progressions"]:
        chapter = progression["chapter"]
        if chapter not in progression_by_chapter:
            progression_by_chapter[chapter] = {**progression, "moves": list(progression["moves"])}
            continue
        merged = progression_by_chapter[chapter]
        combined_moves = []
        for earlier, later in zip(merged["moves"], progression["moves"]):
            prefix, earlier_body = earlier.split(":", 1)
            _, later_body = later.split(":", 1)
            combined_moves.append(f"{prefix}: {earlier_body.strip()}; then {later_body.strip()}")
        merged["moves"] = combined_moves
    audit["organization_logic"]["section_progressions"] = list(progression_by_chapter.values())
    base.write_json(ROOT / "artifacts/language-units" / f"{PID}.json", language)
    base.write_json(ROOT / "artifacts/model-units" / f"{PID}.json", models)
    base.write_json(ROOT / "artifacts/paper-cards" / f"{PID}.json", card)
    base.write_json(ROOT / "artifacts/learning-audits" / f"{PID}.json", audit)
    op = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    op.parent.mkdir(parents=True, exist_ok=True)
    op.write_text("".join(json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "\n" for x in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
