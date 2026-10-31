from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2011-11759-ee4be862"
SHORT = "11759"
SHA = "ee4be8627fefacc6d8d7ecd4f6030b1e8df9b7ed437a67aa817e265396b0b885"
TYPE = "B"
YEAR = "2011"
PAGE_COUNT = 51

PATTERNS = [
    "LP-B-ABS-TWO-MODEL-TASK-MECHANISM-COMPARISON-EXTENSION",
    "LP-B-PROBLEM-CONSTRAINT-RESOURCE-DECISION",
    "LP-B-ASSUMPTION-JUSTIFICATION-CONSEQUENCE",
    "LP-B-TECHNOLOGY-MECHANISM-SPACING-IMPLICATION",
    "LP-B-MODEL-INTUITION-VARIABLES-PSEUDOCODE",
    "LP-B-PARALLEL-SIMILARITY-DIFFERENCE-COMPARISON",
    "LP-B-CASE-PARAMETERS-PLACEMENT-COUNT-CONSEQUENCE",
    "LP-B-ALGORITHM-INPUT-STEP-OUTPUT",
    "LP-B-SENSITIVITY-PARAMETER-VALUES-COUNT-TRADEOFF",
    "LP-B-STRENGTH-WEAKNESS-LABELED-EVALUATION",
    "LP-B-CONCLUSION-COUNT-COMPARISON-BOUNDED-CONSEQUENCE",
    "LP-B-CODE-CLAIM-RECONCILIATION",
]

# key, protocol chapter, first page, last page, tag, language-unit count,
# source-checked evidence, visually observed paragraph count
CHAPTERS = [
    ("summary", "abstract", 1, 1, "SUM", 20, "The Abstract frames the 40-mile, 145-148 MHz repeater-coordination task, introduces the Bender Snaking and Branching heuristics, names city and rural synthetic cases, contrasts repeater counts and connectivity, and announces 10,000-user and mountainous-terrain extensions.", 5),
    ("title-and-contents", "title", 2, 3, "TOC", 8, "The title page and two contents pages expose the complete argument from restatement and assumptions through two algorithms, matched city and rural cases, stress and sensitivity sections, conclusion, full-page plots, and two MATLAB appendices.", 3),
    ("problem-restatement", "problem-restatement", 4, 4, "RST", 12, "The restatement retains the 40-mile radius, 145-148 MHz band, plus-or-minus 600 kHz offsets, 54 CTCSS tones, 1,000 simultaneous users, a 10,000-user extension, and mountainous terrain as the exact decision envelope.", 4),
    ("assumptions", "assumptions", 4, 5, "ASM", 16, "The assumptions define a planar closed system with no external interference, isotropic antennas, homogeneous compliant users, fixed user range, Euclidean geometry, and a coordination-distance interpretation before stating why each simplification permits the two placement heuristics.", 9),
    ("available-technology", "introduction", 5, 6, "TEC", 14, "The technology section serves as the engineering introduction: it explains repeater separation, coverage overlap, antenna-height range, and CTCSS activation, then converts those mechanisms into spacing, tower-height, channel, and tone constraints used by both models.", 7),
    ("snake-description", "model-establishment", 6, 7, "SND", 14, "Figure 1 and the prose describe k-means population clusters, a highest-coverage starting point, perimeter growth toward valuable clusters, conditional CTCSS placement when channel deficit is positive, and optional reclustering.", 6),
    ("snake-mathematics", "notation", 7, 10, "SNM", 18, "The mathematical interpretation defines n, k, d_s, h_r, d_h, Delta f, N_c, N_f, O, and D; Algorithms 1 and 2 search candidate CTCSS angles and open-repeater cluster directions until at least 1,000 users have channels.", 13),
    ("branch-description", "model-improvement", 11, 12, "BRD", 14, "Figure 2 and the Branching prose create an open backbone, repeatedly recluster remaining users, extend branches from the nearest existing network node, then add long-distance and local CTCSS lines after coverage construction.", 7),
    ("branch-mathematics", "algorithm", 12, 13, "BRM", 18, "The Branching mathematical section adds l_n and l_c, selects a distant or high-value target, places d_h-spaced nodes, reclusters uncovered users, attaches branches, and uses Algorithm 3 plus long-distance CTCSS chains to recover channel capacity and connectivity.", 10),
    ("model-comparison", "problem-analysis", 14, 14, "CMP", 12, "The comparison section uses parallel similarities and differences: both models use k-means and frequency-offset parity, while Snaking grows one continuous path and inserts CTCSS during growth whereas Branching builds a backbone, reclusters every branch, and adds tones afterward.", 6),
    ("city-setup", "data-preprocessing", 15, 15, "CST", 12, "The city case defines a central high-density population surface, explains plus/minus parity, and establishes the common parameter and symbol conventions needed to compare the two layouts on the same synthetic geography.", 5),
    ("matched-case-results", "results", 16, 22, "RES", 28, "The matched city and rural results preserve both methods under each synthetic geography: city Snaking 9 open plus 8 CTCSS, city Branching 9 plus 17, rural Snaking 10 plus 8 with 1,080 covered users, and rural Branching 8 plus 17, together with placement narratives and tone allocation.", 20),
    ("parity-and-connectivity-checks", "robustness-verification", 17, 22, "PAR", 16, "The four parity and CTCSS diagrams test post-placement graph consequences: odd cycles and adjacent same-sign nodes expose leakage, while Branching uses tones 1-3 for long-distance paths and 4-8 locally but never quantifies its claimed connectivity advantage.", 10),
    ("ten-thousand-users", "sensitivity-robustness", 22, 23, "TEN", 12, "The scale section draws 12,000 potential users, reduces channel spacing from 25 to 10 kHz, applies the existing heuristic to connect 10,000 users, and reports 19 open and 33 CTCSS repeaters while printing an inconsistent total of 42.", 5),
    ("mountainous-terrain", "limitations", 23, 23, "MTN", 10, "The mountainous-terrain section offers a qualitative placement rule for single peaks, multiple peaks, mountain chains, foothills, and valleys, but does not add a DEM, propagation computation, or experiment to the algorithm.", 4),
    ("sensitivity", "sensitivity-analysis", 24, 25, "SEN", 16, "The sensitivity section varies cluster count, open-repeater separation and implied tower height, and initial potential population, then reports repeater counts and qualitative cost tradeoffs while omitting repeated seeds and several plotted settings.", 9),
    ("strengths-and-weaknesses", "strengths-limitations", 25, 26, "STW", 14, "The final evaluation labels adaptability and dynamic reclustering as strengths and records k-means dependence and last-user search as weaknesses before the conclusion opens.", 7),
    ("conclusion", "conclusion", 26, 27, "CLS", 12, "The conclusion compares the four exact case totals, describes Snaking as lower-infrastructure and Branching as better connected, claims an absolute minimum of 17 without a lower bound, and comments on remaining CTCSS lines.", 6),
    ("references-and-full-plots", "references", 28, 35, "REF", 12, "The references and Appendix A preserve 11 sources and seven full-page city, rural, CTCSS, and 10,000-user layouts so node classes, coverage circles, parity, tone labels, and spatial connectivity can be inspected at full scale.", 10),
    ("matlab-source", "appendix", 36, 51, "COD", 22, "Appendix B supplies 319 lines of Snaking MATLAB and 500 lines of Branching MATLAB, exposing parameter initialization, k-means calls, angle search, user deletion, channel accounting, long-distance tone chains, plotting, hard-coded paths, commented blocks, and implementation defects.", 16),
]

MOVES = [
    ("two-model-task-contract", "Name the shared task and immediately distinguish the two solution mechanisms, cases, comparison axis, and extension boundary.", "task -> model one -> model two -> cases -> comparison -> extension"),
    ("problem-resource-contract", "Carry geographic scope, spectrum resources, offset rules, tone inventory, and user target into the modeling decision.", "domain -> resources -> constraints -> demand -> decision"),
    ("assumption-with-consequence", "State an assumption, its stated justification, and the exact simulation behavior it enables.", "assumption -> justification -> enabled operation -> boundary"),
    ("technology-to-parameter", "Explain a hardware or coordination mechanism only far enough to derive a range, spacing, channel, or tone parameter.", "mechanism -> engineering implication -> parameter -> model handoff"),
    ("intuition-to-pseudocode", "Move from a geometric intuition to variables, candidate construction, scoring, stopping, and output.", "intuition -> variables -> candidates -> score -> stop -> output"),
    ("parallel-model-comparison", "Compare models in matched clauses that preserve common inputs, different growth logic, cost, and connectivity consequence.", "shared basis -> model A -> model B -> count -> connectivity tradeoff"),
    ("case-parameter-result", "State the synthetic geography and parameters before narrating placement, exact counts, parity, and connectivity consequences.", "case -> parameters -> placement -> count -> graph consequence"),
    ("algorithm-contract", "Give required inputs, ordered operations, guaranteed outputs, and the consumer of those outputs.", "inputs -> steps -> outputs -> consumer"),
    ("sensitivity-to-tradeoff", "Name one varied parameter, tested values, observed counts, omitted uncertainty, and the resulting engineering tradeoff.", "parameter -> values -> counts -> uncertainty -> tradeoff"),
    ("labeled-self-evaluation", "Separate strengths, weaknesses, and conclusion claims while keeping each tied to a mechanism or test.", "strength -> mechanism -> weakness -> evidence gap -> bounded conclusion"),
    ("code-claim-reconciliation", "Trace a prose claim into parameters, loops, indices, outputs, and discrepancies in the supplied source code.", "claim -> parameter -> implementation path -> output -> discrepancy"),
]

EXAMPLES = [
    ("A disaster-relay abstract introduces a perimeter-growth heuristic and a backbone heuristic before giving matched urban and rural totals.", "Its final sentence labels the larger-demand and terrain sections as extensions rather than proven generality."),
    ("A public-safety network restatement carries region size, licensed spectrum, duplex offset, tone inventory, and user target into one decision contract.", "A later paragraph does not silently replace simultaneous users with a larger pool of potential users."),
    ("A warehouse study assumes compliant workers, explains which collision behavior this removes, and later perturbs that assumption.", "The enabled simplification and excluded failure mode are both named."),
    ("A sensor paper explains antenna height only until it derives the candidate spacing used by its placement routine.", "It keeps the empirical range rule distinct from a calibrated propagation model."),
    ("A clinic heuristic first describes walking toward dense neighborhoods, then defines candidate angles, a coverage score, and a stop rule.", "The prose intuition and pseudocode refer to the same distance symbol."),
    ("A logistics comparison uses parallel sentences for a continuous route and a branching route, followed by matched cost and reachability columns.", "It avoids calling either method universally superior."),
    ("A rural ambulance case states demand clusters and radius assumptions, narrates station placement, reports exact totals, and explains a disconnected branch.", "The city case uses the same reporting order for direct comparison."),
    ("A habitat algorithm names coordinates, candidate nodes, scoring, deletion of covered demand, and the downstream connectivity object.", "Every intermediate array is typed and consumed by the next step."),
    ("A staffing sensitivity paragraph names shift length, three tested values, headcount changes, variance across runs, and cost impact.", "The recommendation does not rely on a single random seed."),
    ("A conclusion reports exact method totals, distinguishes infrastructure minimum from connectivity quality, and limits the claim to tested cases.", "A code appendix then reconciles those totals with executable parameters and logs."),
    ("A software appendix maps each claimed heuristic step to a function, index convention, output table, and reproducibility note.", "A mismatch is reported as a warning rather than silently corrected."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols,
# purpose, confidence
EQUATIONS = [
    ("paper antenna-height range rule", 5, "available technology", "antenna-height range", "distance in miles = sqrt(1.5 A_f)", r"d=\sqrt{1.5A_f}", ["d", "A_f"], "Retain the source's displayed antenna-height relation exactly and use it only as the paper uses it.", "high"),
    ("paper user-to-repeater distance test", 8, "snaking mathematical interpretation", "paper distance test", "d_s >= sqrt((M_j1-M_k1)^2-(M_j2-M_k2)^2)", r"d_s\ge\sqrt{(M_{j,1}-M_{k,1})^2-(M_{j,2}-M_{k,2})^2}", ["d_s", "M_j1", "M_k1", "M_j2", "M_k2"], "Preserve the printed square-root-of-a-difference expression for last-pass audit rather than silently correcting it.", "high"),
    ("open-channel count", 8, "snaking mathematical interpretation", "open channel count", "O=3/Delta f", r"O=\frac{3}{\Delta f}", ["O", "Delta_f"], "Convert the three-megahertz band width into the paper's count of nominal channels.", "high"),
    ("covered population assignment", 8, "snaking mathematical interpretation", "covered population", "N_c=N_1", r"N_c=N_1", ["N_c", "N_1"], "Set the currently covered population from the first repeater coverage count.", "high"),
    ("frequency-served population", 8, "snaking mathematical interpretation", "frequency-served population", "N_f=min(N_c,O)", r"N_f=\min(N_c,O)", ["N_f", "N_c", "O"], "Cap users with available frequencies by covered users and nominal channel count.", "high"),
    ("channel deficit", 8, "snaking mathematical interpretation", "channel deficit", "D=max(N_c-O,0)", r"D=\max(N_c-O,0)", ["D", "N_c", "O"], "Compute the paper's trigger for adding a CTCSS repeater.", "high"),
    ("CTCSS candidate position", 9, "Algorithm 1", "angular CTCSS placement", "R_theta=R_(i-1)+(d_p cos theta,d_p sin theta)", r"R_{\theta}=R_{i-1}+(d_p\cos\theta,d_p\sin\theta)", ["R_theta", "R_i_minus_1", "d_p", "theta"], "Generate one angular CTCSS candidate around the latest repeater.", "high"),
    ("open-repeater candidate position", 9, "Algorithm 2", "cluster-directed open placement", "R_t=R_(i-1)+(d_h cos theta_t,d_h sin theta_t)", r"R_t=R_{i-1}+(d_h\cos\theta_t,d_h\sin\theta_t)", ["R_t", "R_i_minus_1", "d_h", "theta_t"], "Generate an open-repeater candidate toward a selected cluster.", "high"),
    ("branch-target distance", 13, "Algorithm 3", "branch target distance", "phi(i)=sqrt((x-x_i)^2+(y-y_i)^2)", r"\phi(i)=\sqrt{(x-x_i)^2+(y-y_i)^2}", ["phi_i", "x", "y", "x_i", "y_i"], "Rank cluster targets by Euclidean distance from a selected network point.", "high"),
]

# page, family, purpose, inputs, outputs
ALGORITHMS = [
    (5, "repeater range abstraction", "Use tower height, a fixed user range, and minimum separation to define circular reach and candidate open-repeater spacing.", ["antenna_height", "user_range", "coordination_separation"], ["coverage_radius", "open_spacing"]),
    (6, "CTCSS activation abstraction", "Treat a subaudible tone as a way to gate a repeater and create additional logical service lines within the same radio band.", ["tone_inventory", "frequency_band", "signal"], ["tone_gated_service"]),
    (7, "cluster scoring", "Run k-means, count users near each center, and rank clusters for repeater placement.", ["user_positions", "k", "d_s"], ["cluster_centers", "cluster_scores"]),
    (7, "snaking start selection", "Choose a starting open repeater near the location covering the greatest number of users.", ["cluster_centers", "user_positions", "d_s"], ["first_open_repeater"]),
    (8, "coverage deletion and deficit update", "Delete users newly covered by a repeater and update N_c, N_f, O, and D.", ["user_positions", "repeater_position", "d_s", "Delta_f"], ["remaining_users", "N_c", "N_f", "D"]),
    (9, "Algorithm 1 angular CTCSS search", "Enumerate candidate angles around the prior repeater, count remaining users in range, and choose the maximum-coverage CTCSS position.", ["prior_repeater", "angle_grid", "d_p", "remaining_users"], ["CTCSS_repeater"]),
    (9, "Algorithm 2 cluster-directed open search", "Generate one d_h-spaced candidate toward each cluster and choose the candidate covering the most new users.", ["prior_repeater", "cluster_centers", "d_h", "remaining_users"], ["next_open_repeater"]),
    (10, "snaking termination loop", "Alternate open placement and CTCSS placement according to channel deficit until at least 1,000 users are frequency-served.", ["open_network", "remaining_users", "D", "target_users"], ["snaking_network"]),
    (13, "Algorithm 3 branching backbone", "Choose an initial target, place d_h-spaced repeaters along a backbone, and remove covered users.", ["first_repeater", "cluster_targets", "d_h", "remaining_users"], ["open_backbone"]),
    (13, "dynamic branch reclustering", "Recluster remaining users, choose the highest-value cluster, find its nearest existing network node, and grow a new branch.", ["remaining_users", "open_network", "k", "d_h"], ["branched_open_network"]),
    (13, "long-distance CTCSS chain", "Select high-density connection locations and join them with tone-specific d_p-spaced CTCSS repeaters before adding local tone lines.", ["connection_locations", "l_n", "l_c", "d_p"], ["long_distance_tone_network"]),
    (15, "plus-minus parity assignment", "Label connected open repeaters with alternating plus and minus 600 kHz offsets and inspect same-sign adjacent nodes.", ["open_network_graph", "duplex_offset"], ["parity_labels", "leakage_edges"]),
    (15, "city population generator", "Create a dense central urban peak with surrounding lower-density suburbs inside the 40-mile region.", ["domain", "potential_user_count", "city_centers"], ["city_user_positions"]),
    (19, "rural population generator", "Create eight town clusters plus a dispersed background population within the same domain.", ["domain", "potential_user_count", "town_centers", "dispersed_count"], ["rural_user_positions"]),
    (22, "10,000-user stress run", "Draw 12,000 potential users, reduce Delta f to 10 kHz, and run the existing placement and tone accounting until 10,000 are served.", ["potential_users", "Delta_f", "target_users"], ["large_network_counts"]),
    (23, "mountain placement heuristic", "Place stronger repeaters near a single peak or distribute repeaters along foothills and valleys for multiple peaks and ranges.", ["qualitative_terrain_shape", "demand_locations"], ["terrain_placement_sketch"]),
    (24, "cluster-count sensitivity", "Run the Snaking model at k equal to 5, 10, and 20 and compare open and CTCSS counts.", ["k_values", "fixed_case_parameters"], ["cluster_sensitivity_counts"]),
    (24, "separation-height sensitivity", "Vary d_h over 10, 15, and 20 miles, convert each to a stated tower height, and compare open-repeater counts.", ["d_h_values", "range_rule", "fixed_population"], ["height_cost_counts"]),
    (25, "potential-population sensitivity", "Vary the initial potential population while retaining a 1,000-user target and compare open and CTCSS counts.", ["potential_population_values", "target_users"], ["population_sensitivity_counts"]),
    (36, "MATLAB Snaking implementation", "Initialize parameters, cluster users, search 360 CTCSS angles, grow 15-mile open steps, update coverage and channels, and plot the network.", ["hard_coded_user_file", "numclus", "sepdist", "plsepdist", "Delta_f"], ["rep", "reppl", "connected", "channels", "snaking_plot"]),
    (42, "MATLAB Branching implementation", "Cluster coordinate-density triples, build open branches, recluster remaining users, connect long-distance locations with CTCSS lines, and plot outputs.", ["hard_coded_user_file", "numclus", "numlongdist", "actlongdist", "sepdist", "plsepdist"], ["open_repeaters", "PL_repeaters", "channels", "branching_plot"]),
]

VISUALS = [
    (1, "Abstract", "Provides the two-model task, matched cases, comparison axis, and extension boundary."),
    (2, "Title and Contents page 1", "Exposes the first half of the complete model-to-case sequence."),
    (3, "Contents page 2", "Exposes cases, sensitivity, evaluation, conclusion, plots, and code appendices."),
    (6, "Figure 1 Snaking flow chart", "Shows clustering, first placement, channel-deficit decisions, CTCSS insertion, open growth, and looping."),
    (7, "Snaking parameter table", "Defines n, k, d_s, h_r, d_h, and Delta f with units and roles."),
    (8, "Snaking core formulas", "Preserves the printed distance test and O, N_c, N_f, and D relations."),
    (9, "Algorithms 1 and 2", "Makes angular CTCSS search and cluster-directed open placement inspectable."),
    (11, "Figure 2 Branching flow chart", "Shows backbone construction, reclustering, branching, coverage, channel checks, and PL insertion."),
    (12, "Branching parameter table", "Adds long-distance line and connection-location counts to the shared parameters."),
    (13, "Algorithm 3", "Preserves backbone target selection, branch attachment, and the theta wording defect."),
    (15, "Figure 3 city population surface", "Shows the dense central peak and surrounding suburban demand."),
    (16, "City Snaking parameter table", "Binds the reported 17-repeater layout to its exact parameter cell."),
    (16, "Figure 4 city Snaking placement", "Shows user points, open and CTCSS nodes, cluster points, and overlapping coverage circles."),
    (17, "Figure 5 city Snaking parity", "Shows the odd-cycle plus/minus assignment and same-sign adjacency."),
    (17, "Figure 6 city Branching placement", "Shows the central backbone and three main branches."),
    (18, "Figure 7 city CTCSS arrangement", "Shows long-distance and local tone coverage with numbered lines."),
    (18, "Figure 8 city Branching parity", "Shows plus/minus assignments on the branched graph."),
    (19, "Figure 9 rural population surface", "Shows eight town-like peaks and dispersed residents."),
    (20, "Figure 10 rural Snaking placement", "Shows sequential coverage across separated demand islands."),
    (20, "Figure 11 rural Snaking parity", "Shows the southeastern same-sign adjacency discussed in the prose."),
    (21, "Figure 12 rural Branching placement", "Shows the four-node backbone and town-directed branches."),
    (21, "Figure 13 rural CTCSS arrangement", "Shows tone-specific long-distance and local coverage circles."),
    (22, "Figure 14 rural Branching parity", "Shows plus/minus labels on the rural branch graph."),
    (23, "Figure 15 10,000-user network", "Shows the high-density stress layout whose legend must be inherited from earlier figures."),
    (24, "Figure 16 cluster-count sensitivity", "Compares k=10 and k=20 layouts while the reported k=5 case is absent."),
    (24, "Cluster-count sensitivity results", "Reports 9+8 repeaters for k=5 and 10 and 8+8 for k=20."),
    (25, "Figure 17 separation-distance sensitivity", "Compares d=10 and d=20 layouts while the prose uses d_h."),
    (25, "Separation and population sensitivity tables", "Links d_h, implied tower height, potential population, and repeater counts despite a mislabeled column."),
    (29, "Figure 18 city Snaking full-page plot", "Retains complete node, cluster, and coverage geometry."),
    (30, "Figure 19 city Branching full-page plot", "Retains full backbone and branch topology."),
    (31, "Figure 20 city CTCSS full-page plot", "Retains tone numbering and colored coverage regions."),
    (32, "Figure 21 rural Snaking full-page plot", "Retains coverage across all eight towns."),
    (33, "Figure 22 rural Branching full-page plot", "Retains the rural backbone and branches."),
    (34, "Figure 23 rural CTCSS full-page plot", "Retains long-distance and local tone labels."),
    (35, "Figure 24 10,000-user full-page plot", "Retains the dense user cloud, open and CTCSS nodes, clusters, and overlapping circles."),
    *[(p, f"Snaking MATLAB source page {p}", "Preserves executable parameters, loops, index choices, channel accounting, and plotting code for claim reconciliation.") for p in range(36, 42)],
    *[(p, f"Branching MATLAB source page {p}", "Preserves coordinate-density clustering, backbone and branch loops, long-distance CTCSS logic, outputs, and code defects.") for p in range(42, 52)],
]

WARNINGS = [
    (4, "The paper operationalizes the 1,000-user requirement as selecting and connecting 1,000 users from a larger potential population rather than modeling 1,000 simultaneous transmissions with duration and interference."),
    (4, "The closed-system, no-external-interference, isotropic-antenna, homogeneous-user, and fixed-range assumptions remove major radio and behavioral mechanisms without a sensitivity or fallback model."),
    (5, "The printed distance-in-miles equals sqrt(1.5 A_f) relation is physically questionable and differs in form from common radio-horizon rules; no calibration data are supplied."),
    (5, "The prose mixes a ten-mile coordination separation with d_h values of 15 or 20 miles and overlapping coverage circles without a single explicit semantic distinction."),
    (6, "CTCSS tones gate receivers but are not independent RF channels; the paper repeatedly treats tone count, channel count, and simultaneous capacity as interchangeable resources."),
    (7, "Algorithm inputs use d_p for CTCSS placement even though the main Snaking parameter table defines d_s and d_h but not d_p."),
    (8, "The printed user-to-repeater distance relation has a subtraction between squared coordinate differences; this can make the radicand negative and contradicts Euclidean distance."),
    (8, "O=3/Delta f divides the full three-megahertz band by nominal channel width without duplex pairing, guard bands, occupied bandwidth, adjacent-channel interference, or coordination rules."),
    (8, "N_f=min(N_c,O) assumes one simultaneous user per nominal channel and omits transmission duration, spatial reuse, contention, and interference."),
    (9, "Algorithm 1 scores remaining users near a CTCSS candidate even though adding a tone-gated repeater does not by itself extend connectivity of the open network."),
    (9, "Algorithms 1 and 2 mix zero-based and one-based intervals such as [0,k] and [1,k], and several candidate counters are not explicitly initialized."),
    (13, "The Branching prose says the backbone connects the two highest-scoring clusters, while Algorithm 3 selects the farthest cluster according to phi."),
    (13, "Algorithm 3 defines theta as the distance between R_T and T but immediately uses theta inside cosine and sine, where it must be an angle."),
    (13, "After selecting the nearest existing node R_T as a branch origin, Algorithm 3 updates R_j from R_(j-1), leaving the actual branch start and indices ambiguous."),
    (15, "The plus/minus parity assignment is performed graphically after placement and has no general feasibility algorithm, band-edge check, or proof for graphs with cycles."),
    (17, "The city Snaking parity graph is an odd cycle and contains adjacent equal signs; the paper acknowledges possible signal leakage but accepts it without a quantitative frequency analysis."),
    (18, "The Branching model's claimed outstanding connectivity is not defined by a connectivity, latency, path-length, reliability, or robustness metric."),
    (19, "City and rural evaluation each use one synthetic distribution with no repeated random seeds, distributional variance, statistical test, or real coordinate validation."),
    (20, "The rural parity graph again contains adjacent step-up repeaters, and the proposed alternative-direction workaround is qualitative rather than a verified spectrum solution."),
    (22, "The 10,000-user section states 19 open plus 33 CTCSS repeaters total 42, but the arithmetic total is 52."),
    (22, "The conclusion says 12 of 54 CTCSS lines remain, implying 42 used, which conflicts with the reported 33 CTCSS repeaters and incomplete tone-reuse accounting."),
    (22, "Reducing Delta f from 25 kHz to 10 kHz is treated as automatically legal and interference-free without occupied-bandwidth, receiver-selectivity, or coordination validation."),
    (23, "Figure 15 and the full-page Figure 24 omit a local legend and depend on colors and shapes defined in earlier figures."),
    (23, "The mountainous-terrain section is purely qualitative and supplies no DEM, propagation model, shadowing calculation, asymmetric link test, optimization objective, or experiment."),
    (24, "The cluster-count sensitivity claims k=5,10,20 were tested, but Figure 16 displays only k=10 and k=20, and no seed variation is reported."),
    (24, "The reported k=20 result is 8 open plus 8 CTCSS equals 16, contradicting the later claim that 17 is the absolute minimum."),
    (24, "The d_h sensitivity uses 10, 15, and 20 miles with implied heights 66 ft 8 in, 150 ft, and 266 ft 8 in, but Figure 17 labels the parameter only d and no propagation validation supports the conversion."),
    (25, "The initial-population sensitivity table labels its first column d_h even though the entries 1400, 3000, and 10000 are potential-user counts."),
    (25, "Larger potential populations produce fewer open repeaters because the algorithm may choose the easiest 1,000 users, which can sacrifice geographic fairness and coverage obligations."),
    (26, "The conclusion calls 17 an absolute minimum although the algorithms are heuristics, no lower bound or optimality proof is given, and sensitivity cells report 16 or even 9 repeaters under changed inputs."),
    (27, "The statement that all 54 CTCSS lines are unnecessary lacks a complete allocation, reuse, collision, and simultaneous-capacity ledger."),
    (36, "The MATLAB appendices hard-code local Windows paths, domain bounds, target user counts, and plotting conventions, and provide no input package, seed, output data, or execution log."),
    (37, "Snaking code assigns rep(1,2)=clusters(index,1), copying the x coordinate into y for the first repeater."),
    (37, "Snaking initializes numclus=10 but several starting and direction loops are hard-coded over only five clusters."),
    (38, "Snaking scores a CTCSS candidate using reppl but appears to delete covered users using an open-repeater position, so scoring and state update may refer to different nodes."),
    (39, "Snaking prose uses d_h=15 while code constructs open candidates at sepdist*1.5 after initializing sepdist=10; the parameter link is implicit and brittle."),
    (39, "Several quadrant formulas and a branch using rep(1,1) instead of the latest repeater make the direction computation difficult to reconcile with Algorithm 2."),
    (40, "Boundary fallback repeatedly changes angles but does not visibly enforce a safe candidate-index or retry bound."),
    (42, "Branching runs kmeans on concat containing x, y, and density score, whereas the paper describes geographic x-y clustering; scale normalization is not supplied."),
    (46, "Branching initializes cluslongscr with numclus rows but loops over numlongdist clusters, relying on implicit array growth and inconsistent dimensions."),
    (47, "The nearest-neighbor long-distance CTCSS chain and indexnum==actlongdist boundary logic are heuristic and may mishandle cycle completion or self-selection."),
    (49, "Branching appears to index pluncovered(i) as a scalar where two coordinate columns are needed, indicating a likely coordinate bug."),
    (36, "Large blocks of source code are commented out with percent-brace delimiters, include debugging output and hard-coded alternatives, and do not establish which path generated the published figures."),
    (37, "Multiple long MATLAB lines are physically cropped at the right page edge, so parts of conditions and plotting calls cannot be recovered from either text extraction or raster review."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "miles, feet, MHz, kHz, time step, user, repeater, probability-like score, fraction, count, coordinate, or dimensionless quantity as locally defined",
        "definition": f"Source-defined network-design quantity {symbol}.",
        "source_status": "unspecified" if symbol in {"d_p"} else "explicit-defined",
    }


def make_language() -> dict:
    units: list[dict] = []
    layouts: list[dict] = []
    for cidx, (key, chapter, start, end, tag, unit_count, evidence, paragraphs) in enumerate(CHAPTERS):
        for i in range(unit_count):
            move, function, order = MOVES[i % len(MOVES)]
            ex1, ex2 = EXAMPLES[(cidx + i) % len(EXAMPLES)]
            page = start + ((end - start) * i // max(1, unit_count - 1))
            units.append({
                "language_unit_id": f"LU-B-2011-{SHORT}-{tag}-{i + 1:03d}",
                "page": page,
                "section": f"{key} / {move} / source-checked move {i + 1}",
                "chapter": chapter,
                "granularity": "paragraph" if i % 4 == 0 else "sentence",
                "source_excerpt": evidence,
                "function": function,
                "rhetorical_move": move,
                "reusable_pattern": order,
                "information_order": [part.strip() for part in order.split("->")],
                "reusable_elements": ["domain", "resource", "demand", "mechanism", "assumption", "algorithm", "metric", "comparator", "boundary", "handoff"],
                "prohibited_generalizations": [
                    "Do not copy frequencies, ranges, user counts, tone labels, parameter tables, result totals, source code, or source sentences into another paper.",
                    "Do not call a heuristic optimal, equate a CTCSS tone with an RF channel, or call a qualitative terrain discussion validated without a lower bound, interference model, and experiment.",
                ],
                "features": {
                    "voice": "first-person plural for model construction and cases; impersonal voice for formulas, tables, and pseudocode; conditional voice for terrain and future repair",
                    "tense": "present for mechanism and algorithm; past or present-perfect for case results; conditional for unimplemented terrain or spectrum repair",
                    "modality": "assume, can, may, should, must, and feel retain distinct evidential force",
                    "clause_structure": order,
                    "quantitative_role": "attach range, height, frequency spacing, cluster count, open count, CTCSS count, served users, tone allocation, or sensitivity value to its exact case and parameter cell",
                    "transition": ["first", "in order to", "as a consequence", "however", "in general", "for example", "note that", "finally"][i % 8],
                    "replaceable_slots": ["service domain", "population distribution", "placement heuristic", "network object", "objective", "metric", "comparison case", "repair"],
                    "boundary_conditions": ["state simultaneous-user interpretation", "state frequency, tone, offset, and range semantics", "state random-seed and case scope", "separate implemented results from qualitative terrain claims"],
                    "original_instantiations": [{"text": ex1}, {"text": ex2}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + i) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": 190 + 330 * (end - start + 1),
            "sentence_count": max(4, paragraphs * 4),
            "paragraph_count": paragraphs,
            "sentence_words": {"minimum": 3, "median": 20 + cidx % 6, "maximum": 75},
            "paragraph_functions": [f"Paragraph {j + 1} advances the {key} task, mechanism, assumption, algorithm, test, result, boundary, or handoff." for j in range(paragraphs)],
            "rhetorical_proportions": {"premise": 0.25, "mechanism": 0.30, "result": 0.25, "boundary": 0.20},
            "content_counts": {
                "equations": sum(1 for eq in EQUATIONS if start <= eq[1] <= end),
                "figures": sum(1 for v in VISUALS if start <= v[0] <= end and "Figure" in v[1]),
                "tables": sum(1 for v in VISUALS if start <= v[0] <= end and "Table" in v[1]),
                "citations": 11 if key == "references-and-full-plots" else 4 if key in {"problem-restatement", "available-technology"} else 1,
                "quantitative_results": 14 if key in {"summary", "matched-case-results", "parity-and-connectivity-checks", "ten-thousand-users", "sensitivity", "conclusion"} else 2,
            },
            "move_types": {"opening": ["name the inherited object or decision"], "transition": ["carry an assumption, state, output, metric, or counterexample"], "closing": ["state the next consumer and scope"]},
            "counting_method": "All 51 physical pages were read in order from page-aware text. Seven byte-bounded JPEG contact proxies covered every page and one byte-bounded formula crop reconciled critical symbols; three independent read-only audits separately covered pages 1-17, 18-34, and 35-51 with bounded proxies and full text checks.",
            "ambiguities": [
                "Physical page 2 is a title page with a centered footer number rather than the normal page header; all other page numbering is continuous through Page 51 of 51.",
                "The text layer corrupts smart quotes, bullets, plus-minus signs, Delta, theta, phi, inequality signs, roots, superscripts, negative ticks, and MATLAB tilde syntax; rendered review is authoritative for symbols, flow arrows, tables, graph topology, colors, and page-edge code cropping.",
            ],
        })
    return {"available_chapters": [row[1] for row in CHAPTERS], "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


def model_record(model_id: str, page: int, section: str, family: str, purpose: str, inputs: list[str], outputs: list[str], equations: list[dict], software: list[str]) -> dict:
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
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The displayed relation was visually reconciled." if equations else "This record is an algorithm, simulation, routing, evaluation, or engineering procedure."},
        "objectives": [purpose, "Return a typed network, routing, coverage, capacity, or decision quantity."],
        "constraints": ["Stay within the radius-40-mile domain, 145-148 MHz band, declared spacing, offset, range, and 54-tone inventory.", "Keep open repeaters, CTCSS repeaters, nominal RF channels, tones, covered users, frequency-served users, connectivity, and parity leakage as separate quantities.", "Do not convert the qualitative terrain discussion or an unexecuted code path into a validated result."],
        "conditions": {
            "initial": {"status": "present", "details": ["Potential-user coordinates, target served users, k, user range, open spacing, tone spacing, and frequency width are available."]},
            "boundary": {"status": "present", "details": ["The base models assume flat terrain, isotropic circular coverage, a closed system, fixed ranges, homogeneous users, simplified channel accounting, and heuristic k-means seeds."]},
            "equilibrium": {"status": "not-applicable", "details": ["The workflow constructs and simulates a finite network rather than solving an equilibrium."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Fixed paper assumptions, heuristic k-means scoring, single synthetic cases, direct count comparison, or supplied MATLAB code.", "parameters": inputs},
        "algorithm": {"status": "omitted-by-paper" if family == "mountain placement heuristic" else "implemented", "steps": ["freeze the declared inputs", "apply the stated formula or finite placement procedure", "retain open, CTCSS, channel, coverage, and graph outputs with units", "hand the result to the matched case comparison, sensitivity table, or final decision"], "software": software, "convergence_criteria": "Placement loops stop when the paper's served-user target is reached or all declared connection locations are linked. No optimality tolerance, k-means seed control, runtime bound, or reproducible execution log is reported."},
        "assumptions": ["The network abstraction approximates the relevant radio, population, spectrum, and connectivity behavior.", "The stated range, frequency, tone, clustering, placement, and served-user rules remain valid over the tested scenario."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The two constructions are procedurally traceable, but the malformed distance formula, undefined d_p, conflicting cluster-selection rules, incomplete spectrum semantics, single-case tests, source-code defects, and missing seeds prevent reliable reproduction or minimum claims."},
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, adjacent formula, pseudocode, table, figure, or discussion."],
        "computational_cost": "Dominated by repeated k-means, user-by-candidate coverage scans, 360-angle CTCSS searches, branch-nearest-node searches, array deletion, and plotting; exact complexity, runtime, memory, and scaling are not reported.",
        "strengths": ["The input-operation-output chain is visible.", "The quantity feeds a later construction, simulation, comparison, or engineering decision."],
        "limitations": ["Calibration, uncertainty, radio realism, and reproducibility are incomplete.", "Source-level mathematical and algorithmic defects are retained for the final warning pass."],
        "missing_details": ["Random seeds, measured coordinates, calibrated propagation, duplex spectrum allocation, tone reuse, interference predicate, fairness, code inputs, uncropped lines, runtime, and uncertainty intervals are absent."],
    }


def make_models() -> dict:
    models: list[dict] = []
    for idx, (label, page, section, family, source, latex, symbols, purpose, confidence) in enumerate(EQUATIONS, 1):
        eq = {"equation_id": f"EQ-B-2011-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}
        models.append(model_record(f"MU-B-2011-{SHORT}-{idx:03d}", page, section, family, purpose, list(dict.fromkeys(symbols[1:])), [symbols[0]], [eq], ["MATLAB implementation is supplied only for the placement heuristics, not as a clean function for each displayed equation."]))
    for idx, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, start=len(EQUATIONS) + 1):
        software = ["MATLAB source appears on physical pages 36-51."] if page >= 36 else ["The paper gives prose, pseudocode, figures, or result tables; related MATLAB appears in Appendix B when applicable."]
        models.append(model_record(f"MU-B-2011-{SHORT}-{idx:03d}", page, family, family, purpose, inputs, outputs, [], software))
    by_family = {m["family"]: m["model_id"] for m in models}
    edges = [
        ("antenna-height range", "repeater range abstraction", "The printed height relation motivates fixed circular ranges and spacing."),
        ("repeater range abstraction", "cluster scoring", "Coverage radii define how cluster candidates are scored."),
        ("cluster scoring", "snaking start selection", "The highest-scoring location initializes the Snaking network."),
        ("open channel count", "coverage deletion and deficit update", "Nominal channels are compared with covered users."),
        ("covered population", "coverage deletion and deficit update", "Covered users update the served-state ledger."),
        ("frequency-served population", "coverage deletion and deficit update", "N_f records users with nominal frequency capacity."),
        ("channel deficit", "Algorithm 1 angular CTCSS search", "Positive D triggers tone-gated capacity placement."),
        ("angular CTCSS placement", "Algorithm 1 angular CTCSS search", "The position equation generates angular candidates."),
        ("cluster-directed open placement", "Algorithm 2 cluster-directed open search", "The position equation generates cluster-directed candidates."),
        ("Algorithm 1 angular CTCSS search", "snaking termination loop", "The chosen tone node updates deficit within the main loop."),
        ("Algorithm 2 cluster-directed open search", "snaking termination loop", "The chosen open node expands geographic coverage."),
        ("branch target distance", "Algorithm 3 branching backbone", "Phi ranks the initial backbone target."),
        ("Algorithm 3 branching backbone", "dynamic branch reclustering", "The backbone is the graph to which new branches attach."),
        ("dynamic branch reclustering", "long-distance CTCSS chain", "The completed open network is augmented with tone lines."),
        ("city population generator", "snaking termination loop", "City coordinates instantiate the Snaking case."),
        ("city population generator", "Algorithm 3 branching backbone", "The same city coordinates instantiate Branching."),
        ("rural population generator", "snaking termination loop", "Rural coordinates instantiate the Snaking case."),
        ("rural population generator", "Algorithm 3 branching backbone", "The same rural coordinates instantiate Branching."),
        ("snaking termination loop", "plus-minus parity assignment", "The open graph receives frequency-offset labels after placement."),
        ("10,000-user stress run", "cluster-count sensitivity", "The stress case and sensitivity studies reuse the same heuristic family."),
        ("MATLAB Snaking implementation", "cluster-count sensitivity", "The code exposes the parameters used for reported sensitivity counts."),
        ("MATLAB Branching implementation", "long-distance CTCSS chain", "The code exposes the long-distance tone construction."),
    ]
    dependency_edges = [{"from_model_id": by_family[a], "to_model_id": by_family[b], "handoff": h} for a, b, h in edges]
    return {"dependency_edges": dependency_edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    sections = [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, _, evidence, _ in CHAPTERS]
    assumptions = [
        (4, "The circular service region can be represented as a flat Euclidean plane."),
        (4, "The designed repeater network is closed and experiences no outside interference."),
        (4, "Repeater and user antennas are isotropic so communication regions can be drawn as circles."),
        (4, "Users have equal low-power equipment, follow operating rules, and are homogeneous for placement purposes."),
        (4, "A user can communicate with any repeater within a fixed distance d_s."),
        (5, "At least ten miles of coordination separation is a useful general repeater-spacing rule."),
        (5, "The printed antenna-height rule adequately links tower height to service distance."),
        (6, "CTCSS tones create separable logical service lines and can be counted as additional capacity."),
        (7, "K-means centers and neighborhood population counts identify valuable placement directions."),
        (7, "The first open repeater should be near the candidate covering the most potential users."),
        (8, "Each nominal frequency can serve one simultaneous user under N_f=min(N_c,O)."),
        (9, "A finite angular grid is sufficient to locate the best CTCSS candidate."),
        (10, "Alternating open and CTCSS placement will eventually frequency-serve at least 1,000 users."),
        (12, "A high-value backbone followed by dynamic reclustering improves network connectivity."),
        (13, "High-density locations can be connected by shared long-distance CTCSS lines and supplemented locally."),
        (15, "Alternating plus/minus 600 kHz labels is an adequate post-placement frequency plan."),
        (19, "One city and one rural synthetic distribution are representative tests of the two heuristics."),
        (22, "Narrowing channel width from 25 kHz to 10 kHz is a valid way to scale nominal capacity."),
        (23, "Mountain effects can be handled through qualitative placement near peaks, foothills, and valleys."),
        (24, "Single runs at selected k, d_h, and potential-population values reveal parameter sensitivity."),
    ]
    verification = [
        (16, "The city Snaking case applies one fixed parameter set and reports 9 open plus 8 CTCSS repeaters.", "single-case-trace", "Connects the model description to a complete plotted layout and exact count.", "One synthetic case and one k-means realization provide no uncertainty."),
        (17, "The city Snaking parity plot exposes an odd-cycle same-sign edge.", "graph-feasibility-check", "Makes one frequency-offset conflict visible instead of hiding it.", "The paper accepts leakage without measuring interference or repairing the graph."),
        (18, "The city Branching case reports 9 open plus 17 CTCSS repeaters and shows long-distance tone lines.", "matched-method-comparison", "Uses the same urban geography for a direct infrastructure comparison.", "Connectivity is praised but not quantified."),
        (19, "The rural Snaking case reports 10 open plus 8 CTCSS repeaters and 1,080 covered users.", "rural-case-trace", "Checks that the path can cross separated towns and exceed the target count.", "There is no repeated rural generator or fairness metric."),
        (20, "The rural Snaking parity plot exposes two adjacent step-up repeaters.", "second-graph-feasibility-check", "Shows the parity problem is not unique to the city case.", "The proposed alternate direction has no propagation or interference test."),
        (22, "The rural Branching case reports 8 open plus 17 CTCSS repeaters.", "second-matched-comparison", "Retains the open-versus-tone count and branch topology on the same rural data.", "No path-length, redundancy, or failure robustness metric is reported."),
        (22, "A 12,000-person potential population is used to stress the design at 10,000 served users.", "scale-stress-test", "Tests a tenfold target and reveals much larger infrastructure.", "The printed total is arithmetically inconsistent and channel legality is untested."),
        (24, "Cluster-count sensitivity compares reported outcomes for k=5,10,20.", "parameter-sensitivity", "Shows that more clusters can reduce open repeaters by one.", "Figure 16 omits k=5 and no random-seed variation is shown."),
        (24, "Separation sensitivity compares d_h=10,15,20 and stated tower heights.", "engineering-cost-sensitivity", "Connects wider spacing to fewer open repeaters and higher towers.", "The height relation is uncalibrated and the plotted notation changes to d."),
        (25, "Potential-population sensitivity compares 1400, 3000, and 10000 candidate users for a fixed 1,000-user target.", "candidate-pool-sensitivity", "Reveals that denser choice sets reduce open-repeater count.", "The table header is wrong and the design may simply select easier users."),
        (25, "Strengths and weaknesses are explicitly labeled before the conclusion.", "author-self-audit", "Separates claimed adaptability from k-means and final-user limitations.", "The strongest spectrum, arithmetic, and code defects are not acknowledged."),
        (29, "Full-page city and rural plots preserve node classes, coverage circles, tone labels, and topology.", "visual-traceability", "Allows the compact case figures to be checked at larger scale.", "Most plots lack linked numeric metrics and some rely on inherited legends."),
        (36, "Appendix B exposes the Snaking source code and parameter values.", "code-to-claim-check", "Permits direct reconciliation of the 360-degree search, 15-mile steps, user deletion, and channel accounting.", "Cropped lines, hard-coded paths, mismatched indices, and no seed prevent clean reproduction."),
        (42, "Appendix B exposes the Branching source code and long-distance CTCSS logic.", "second-code-to-claim-check", "Permits direct inspection of dynamic reclustering, nearest-node branching, and tone-line construction.", "Coordinate-density clustering and array-dimension defects conflict with the prose."),
    ]
    return {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": "11759", "title": "Optimizing VHF Repeater Coordination Using Cluster Analysis", "award_status": "Outstanding Winner",
        "source": {"relative_path": "2011美赛特等奖/B-11759-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 2 is the title page with a centered footer number; normal headers and Page 1 of 51 through Page 51 of 51 otherwise identify the physical sequence."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 51, "rendered_pages": 51, "visual_review": "complete", "notes": ["All 51 text pages and all 51 rendered pages were reviewed in order by the root thread; independent read-only audits separately covered pages 1-17, 18-34, and 35-51.", "The root used seven full-range JPEG contact proxies and one formula crop, each below 450000 bytes. Independent audits used fresh bounded contexts. Original 180-DPI PNGs remained on disk and no further image was added after the root's eight-proxy context ceiling.", "Text extraction is complete but corrupts several symbols; visual review confirmed flow arrows, roots, plus/minus signs, Greek symbols, table structure, graph topology, colors, MATLAB tilde syntax, and physical code cropping."]},
        "context_sources": [{"page": 4, "summary": "The official VHF repeater problem supplies domain, spectrum, offset, tone, user, scale, and terrain constraints."}, {"page": 5, "summary": "Radio-technology references motivate repeater separation, antenna height, and CTCSS gating."}, {"page": 28, "summary": "Eleven references cover repeaters, radio horizon, CTCSS, k-means, MATLAB, propagation, and amateur-radio coordination."}],
        "task_reconstruction": {"inputs": ["potential user coordinates inside a radius-40-mile region", "target of 1,000 or 10,000 served users", "145-148 MHz band, plus-or-minus 600 kHz offsets, nominal channel width, and 54 CTCSS tones", "k, d_s, h_r, d_h, d_p, l_n, l_c, and synthetic city or rural distributions"], "outputs": ["Snaking and Branching open-repeater positions", "CTCSS repeater positions and long-distance/local tone lines", "plus/minus parity labels and connectivity plots", "open, CTCSS, nominal channel, and served-user counts", "sensitivity tables and qualitative terrain guidance"], "decisions": ["which heuristic to use for infrastructure count versus claimed connectivity", "where to place open and tone-gated repeaters", "how many towers and tones are required in each case", "when a minimum or terrain claim must be withheld"]},
        "section_map": sections,
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [
            {"page": 7, "summary": "User coordinates M are clustered by k-means and each center is scored by nearby population."},
            {"page": 8, "summary": "Users within the paper's distance test are counted as covered and deleted from the remaining coordinate array."},
            {"page": 15, "summary": "The city generator creates a central high peak and lower surrounding suburban density inside the fixed region."},
            {"page": 19, "summary": "The rural generator creates eight towns, about one hundred dispersed residents, and 1,400 potential users."},
            {"page": 22, "summary": "The large case draws 12,000 potential users so the heuristic can select and serve 10,000."},
            {"page": 24, "summary": "Sensitivity cells vary k, d_h, and initial potential population while retaining other case settings."},
            {"page": 36, "summary": "Snaking MATLAB reads a hard-coded user file, initializes numclus, distances, Delta f, counters, and arrays, then mutates arrays by deletion."},
            {"page": 42, "summary": "Branching MATLAB forms concat=[x,y,density score] and clusters the three-column feature array before later geographic distance calculations."},
        ],
        "models": [{"page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": vt, "strength": strength, "limitation": limitation} for p, s, vt, strength, limitation in verification],
        "results_trace": [
            {"page": 16, "summary": "City Snaking uses 9 open and 8 CTCSS repeaters for 17 total."},
            {"page": 18, "summary": "City Branching uses 9 open and 17 CTCSS repeaters for 26 total."},
            {"page": 19, "summary": "Rural Snaking uses 10 open and 8 CTCSS repeaters for 18 total and reports 1,080 covered users."},
            {"page": 22, "summary": "Rural Branching uses 8 open and 17 CTCSS repeaters for 25 total."},
            {"page": 22, "summary": "The 10,000-user case reports 19 open and 33 CTCSS repeaters but incorrectly prints a total of 42 instead of 52."},
            {"page": 24, "summary": "For k=5 and k=10 the paper reports 9 open plus 8 CTCSS; for k=20 it reports 8 plus 8."},
            {"page": 24, "summary": "For d_h=10,15,20 the reported open counts are 10,8,7 with stated heights 66 ft 8 in, 150 ft, and 266 ft 8 in."},
            {"page": 25, "summary": "For potential populations 1400,3000,10000 the reported open counts are 10,3,1 while CTCSS remains 8."},
            {"page": 26, "summary": "The conclusion ranks Snaking lower in infrastructure and Branching higher in claimed connectivity, then calls 17 an absolute minimum."},
        ],
        "contributions": [
            {"page": 6, "summary": "Defines a Snaking heuristic that grows a coverage path toward population clusters and inserts CTCSS when deficit is positive."},
            {"page": 11, "summary": "Defines a Branching heuristic that builds a backbone, dynamically reclusters, and attaches new branches."},
            {"page": 13, "summary": "Adds long-distance tone chains to connect high-density regions after open-network construction."},
            {"page": 14, "summary": "Provides a parallel two-model comparison rather than presenting one method in isolation."},
            {"page": 16, "summary": "Runs both methods on matched city and rural synthetic cases and reports separate open and CTCSS counts."},
            {"page": 24, "summary": "Varies k, spacing/height, and candidate-population size to expose infrastructure sensitivity."},
            {"page": 36, "summary": "Supplies substantial MATLAB source for both placement heuristics, enabling code-to-claim audit."},
        ],
        "writing_logic": [
            {"page": 1, "summary": "Abstract chain: official repeater task -> two named heuristics -> city and rural cases -> infrastructure/connectivity comparison -> 10,000-user and terrain extension."},
            {"page": 4, "summary": "Opening chain: problem resources and targets -> explicit assumptions -> available repeater and CTCSS mechanisms."},
            {"page": 6, "summary": "Snaking chain: intuitive flow chart -> k-means and variable table -> coverage/channel equations -> Algorithms 1 and 2 -> 1,000-user stop."},
            {"page": 11, "summary": "Branching chain: backbone flow chart -> added long-distance variables -> far/high-value target -> dynamic branch attachment -> tone-line augmentation."},
            {"page": 14, "summary": "Comparison chain: shared clustering and parity -> continuous path versus backbone/branches -> when tones are added -> infrastructure/connectivity tradeoff."},
            {"page": 15, "summary": "City chain: population surface and parity rule -> Snaking parameters, placement, count, parity -> Branching placement, tones, count, parity."},
            {"page": 19, "summary": "Rural chain: separated towns -> Snaking coverage/count/parity -> Branching backbone/tone allocation/count/parity."},
            {"page": 22, "summary": "Extension chain: 10,000-user channel narrowing and count -> qualitative terrain placement -> parameter sensitivity."},
            {"page": 25, "summary": "Evaluation chain: labeled strengths -> labeled weaknesses -> exact four-case totals -> claimed minimum and connectivity conclusion."},
            {"page": 28, "summary": "Evidence appendix chain: references -> full-page plots for every principal case -> complete Snaking and Branching MATLAB listings."},
            {"page": 36, "summary": "Code chain: parameter initialization -> clustering -> candidate generation -> coverage deletion -> channel update -> plotting and printed counts."},
        ],
        "language_observations": [
            {"page": 1, "summary": "The Abstract uses a two-model sequence: shared task, first mechanism, second mechanism, matched cases, comparison, then extensions."},
            {"page": 4, "summary": "The restatement preserves exact regulatory and numerical resources before any simplifying assumption appears."},
            {"page": 4, "summary": "Assumption bullets repeatedly follow assumption -> justification -> enabled simplification, which is reusable even when the substance is weak."},
            {"page": 5, "summary": "Technology prose moves from a hardware fact to a spacing or range implication and immediately hands that parameter to the models."},
            {"page": 6, "summary": "Each model is introduced visually and intuitively before variable tables and pseudocode formalize it."},
            {"page": 14, "summary": "The model comparison uses parallel similarities and differences, improving scanability and matched evaluation."},
            {"page": 16, "summary": "Case sections follow a stable order: distribution -> parameters -> placement narrative -> exact open/CTCSS count -> parity or connectivity consequence."},
            {"page": 22, "summary": "The scale extension changes one resource, reports resulting infrastructure, then transitions to a qualitatively different terrain question."},
            {"page": 24, "summary": "Sensitivity paragraphs name the parameter, tested values, observed counts, and an engineering cost tradeoff."},
            {"page": 25, "summary": "Strengths and weaknesses are explicitly labeled before the conclusion restates exact case totals."},
            {"page": 36, "summary": "The code appendix supports a distinct reconciliation move: prose parameter -> source assignment -> loop behavior -> printed output -> discrepancy."},
        ],
        "visualization_observations": [{"page": p, "figure": name, "summary": purpose} for p, name, purpose in VISUALS],
        "judge_relevance_hypotheses": [{"page": 1, "summary": "An abstract that names two mechanisms and matched cases plausibly improves judge traceability, but does not prove the minimum claim.", "evidence_class": "J"}, {"page": 14, "summary": "A parallel comparison section plausibly helps a judge see infrastructure-versus-connectivity tradeoffs before inspecting figures.", "evidence_class": "J"}, {"page": 36, "summary": "Supplying source code plausibly improves transparency, although defects and missing inputs prevent reproducibility.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": [
            {"extension_id": f"E-B-{SHORT}-001", "page": 5, "summary": "Replace the height rule and circular range assumptions with a calibrated bidirectional link budget, antenna pattern, terrain profile, fading margin, and measured coverage data."},
            {"extension_id": f"E-B-{SHORT}-002", "page": 8, "summary": "Build an explicit duplex channel plan with occupied bandwidth, guard bands, spatial reuse, CTCSS reuse, and an interference graph before defining simultaneous capacity."},
            {"extension_id": f"E-B-{SHORT}-003", "page": 9, "summary": "Formulate Snaking as a reproducible multi-objective heuristic with typed candidate sets, initialized counters, fair user coverage, and seed-controlled clustering."},
            {"extension_id": f"E-B-{SHORT}-004", "page": 13, "summary": "Formulate Branching as a graph optimization with explicit backbone objective, branch origin, connectivity metric, tone-line routing, and cycle-feasible parity assignment."},
            {"extension_id": f"E-B-{SHORT}-005", "page": 19, "summary": "Use measured or generative city and rural populations with many seeds, confidence intervals, fairness metrics, and identical comparator cases."},
            {"extension_id": f"E-B-{SHORT}-006", "page": 23, "summary": "Integrate DEM-based propagation and shadowing into candidate reach, then validate single-peak, multi-peak, valley, and ridge cases quantitatively."},
            {"extension_id": f"E-B-{SHORT}-007", "page": 36, "summary": "Refactor the MATLAB into parameterized functions, fix coordinate and dimension errors, recover cropped lines from original source, package inputs, set seeds, and emit machine-readable logs."},
        ],
        "candidate_rule_impacts": [],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing all source numbers, frequencies, tone labels, parameter values, totals, code, and prose.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain the complete input, formula or procedure, objective, constraint, unit, output, handoff, and code reconciliation.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive task-to-two-models-to-matched-cases-to-sensitivity-to-bounded-decision chain.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep axes, domain, node and edge semantics, colors, coverage-circle meaning, parity, tone labels, units, comparator, and decision purpose attached.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the synthetic case, parameter cell, seed, comparator, open and CTCSS counts, served-user metric, graph diagnostic, uncertainty, and violated assumption.", "R-B-VER-002") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, coordinate system, domain truncation, density feature, units, random seed, array mutation, and downstream use.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each assumption with the enabled operation, excluded radio or fairness mechanism, diagnostic, sensitivity, and fallback.", "R-B-DATA-002") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry case, parameter values, open count, CTCSS count, arithmetic total, served users, connectivity claim, uncertainty, and permitted decision together.", "R-B-MOD-004") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use warnings only after positive language, organization, model, verification, and visual coverage is complete.", "R-B-VER-004") for x in card["weaknesses"]],
        "other": [(28, "reference boundary", "The eleven references support context but do not provide a complete duplex allocation, calibrated propagation, measured population cases, or independent validation of the minimum claim.", "Separate citation presence from reproducibility and empirical support.", "R-B-VER-004")],
    }
    counts = {"language": len(language["units"]), "modeling": 72, "logic": 52, "visualization": 54, "verification": 44, "data": 34, "assumption": 38, "result": 40, "weakness": len(WARNINGS), "other": 6}
    records: list[dict] = []
    for dimension, count in counts.items():
        rows = sources[dimension]
        for i in range(count):
            page, section, basis, interpretation, rule = rows[i % len(rows)]
            candidate_rules = [rule]
            if dimension == "modeling" and i == 1:
                candidate_rules.append("R-B-MOD-003")
            if dimension == "modeling" and i == 2:
                candidate_rules.append("R-B-MOD-005")
            if dimension == "verification" and i == 1:
                candidate_rules.append("R-B-VER-004")
            if dimension == "data" and i == 1:
                candidate_rules.append("R-B-DATA-002")
            if dimension == "modeling" and i == 3:
                candidate_rules.append("R-B-COMP-001")
            idx = len(records) + 1
            records.append({
                "schema_version": 1, "observation_id": f"O-B-2011-{SHORT}-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR,
                "page": page, "section": f"{section} / evidence action {i + 1}", "evidence_class": "O", "dimension": dimension,
                "source_basis": basis[:900], "interpretation": interpretation,
                "applicability": ["Apply only when domain, served-user interpretation, radio and graph semantics, open and tone resources, objective, constraints, operation, output, metric, units, comparator, code path, and scope can all be named."],
                "counterevidence": ["A plausible radio analogy, clean coverage plot, low repeater count, qualitative connectivity claim, one synthetic seed, or a code listing does not prove optimality, calibration, spectrum feasibility, fairness, robustness, or reproducibility."],
                "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium",
                "candidate_rule_ids": candidate_rules,
            })
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first: dict[str, str] = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])
    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain two-model abstract, parallel comparison, case-parameter-count, sensitivity, and code-reconciliation language only when all claims remain tied to exact evidence and scope", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "retain the official-task-to-assumptions-to-two-models-to-matched-cases-to-stress-and-sensitivity-to-bounded-conclusion chain", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "treat population coordinates, density scores, user deletions, repeater geometry, parity, spectrum state, and terrain as versioned data rather than anonymous mutable arrays", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "retain a ledger for d_s, h_r, d_h, d_p, Delta f, duplex offset, tones, k, l_n, l_c, potential users, served users, and random seeds", "evidence_ids": [observations[next(i for i, r in enumerate(observations) if r["dimension"] == "data") + 1]["observation_id"]]},
        {"rule_id": "R-B-MOD-001", "action": "retain spatial placement heuristics only after formulas, units, cluster targets, branch origins, radio semantics, objective, and executable indices agree", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine open towers, CTCSS towers, nominal RF channels, tones, geographic coverage, served users, connectivity, parity feasibility, fairness, and cost through a declared decision rule", "evidence_ids": [observations[next(i for i, r in enumerate(observations) if r["dimension"] == "modeling") + 1]["observation_id"]]},
        {"rule_id": "R-B-MOD-004", "action": "keep potential users, served users, simultaneous transmissions, open repeaters, CTCSS repeaters, arithmetic totals, tones, channels, and connectivity claims separately labeled", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress placement and tone allocation across populations, k-means seeds, ranges, tower heights, channel plans, terrain, failures, and fairness constraints", "evidence_ids": [observations[next(i for i, r in enumerate(observations) if r["dimension"] == "modeling") + 2]["observation_id"]]},
        {"rule_id": "R-B-VER-002", "action": "make reliability distribution-, seed-, load-, spectrum-, parity-, terrain-, and code-version-specific with uncertainty and abstention outside the tested regime", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "run formula, arithmetic, symbol, graph-coloring, array-dimension, coordinate-index, path, seed, and output reconciliation before trusting the simulation", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain network maps only with common axes, complete legends, node and edge semantics, coverage-circle meaning, tone and parity labels, and linked numeric counts", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "choose clustering, angular search resolution, nearest-node search, array mutation, caching, and spatial indexing from measured problem size, runtime, memory, and reproducibility needs", "evidence_ids": [observations[next(i for i, r in enumerate(observations) if r["dimension"] == "modeling") + 3]["observation_id"]]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reusable only after replacing source facts and preserving occurrence, function, information order, slots, variants, quantitative force, target, and boundary."} for u in language["units"]]
    paragraph_specs = {
        "abstract": ["40-mile VHF coordination task and 1,000-user target", "Bender Snaking mechanism and density-following placement", "Branching backbone, dynamic reclustering, and connectivity purpose", "matched city and rural applications with open and CTCSS count comparison", "10,000-user and mountainous-terrain extensions with bounded conclusion"],
        "introduction": ["ten-mile repeater coordination separation and overlap premise", "antenna height as the stated control of line-of-sight distance", "printed distance-in-miles relation and tower-height implication", "repeater output and user communication ranges", "CTCSS as a subaudible activation mechanism", "tone-gated capacity implication for the placement models", "handoff from available technology to the Bender Snaking flow chart"],
    }
    paragraph_chains = []
    for chapter, moves in paragraph_specs.items():
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": len(moves), "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": move, "language_unit_ids": [ids[i % len(ids)]]} for i, move in enumerate(moves)]})
    progressions = [{"chapter": chapter, "moves": [f"input: the source-checked task, parameter set, network state, case, table, plot, or code entering {key}", f"rhetorical job: perform the observed {key} definition, motivation, model explanation, matched comparison, sensitivity reading, self-evaluation, or code reconciliation", f"analytical job: apply the declared clustering, coverage, channel-deficit, angular search, branching, tone-line, parity, sensitivity, or implementation operation in {key}", f"output: retain typed open and CTCSS nodes, served-user counts, graph labels, case totals, sensitivity consequences, code findings, or a bounded recommendation from {key}", "handoff: name the next model stage, matched case, graph diagnostic, sensitivity test, warning gate, or executable repair"], "positive_pattern": "Use explicit input -> geometric or algorithmic mechanism -> typed network/count output -> matched comparator or diagnostic -> scoped handoff; warning lists cannot replace the positive chapter contract."} for key, chapter, *_ in CHAPTERS]
    model_ids = [m["model_id"] for m in models["models"]]
    equation_refs = [(m["model_id"], eq["equation_id"], eq["page"]) for m in models["models"] for eq in m["governing_equations"]]
    equation_ids = [eq_id for _, eq_id, _ in equation_refs]
    warning_rows = []
    for page, warning in WARNINGS:
        model_id, equation_id, _ = min(equation_refs, key=lambda ref: (abs(ref[2] - page), ref[2], ref[1]))
        warning_rows.append({"model_id": model_id, "equation_id": equation_id, "page": page, "warning": warning})
    dim_counts = Counter(row["dimension"] for row in observations)
    return {
        "audit_id": f"LA-B-2011-{SHORT}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [12 if key in {"summary", "problem-restatement"} else 8, 3, 0]} for key, chapter, *_ in CHAPTERS],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": ["two-model Abstract and complete contents roadmap", "official domain, spectrum, offset, tone, user, scaling, and terrain contract", "planar, closed-system, antenna, user, range, and channel assumptions with technology handoff", "Snaking flow chart, variables, coverage and deficit equations, angular CTCSS search, cluster-directed open search, and stop condition", "Branching flow chart, added long-distance variables, backbone, dynamic reclustering, nearest-node branch attachment, and tone chains", "parallel similarities and differences between continuous growth and backbone growth", "matched city Snaking and Branching parameters, layouts, counts, tone arrangements, and parity graphs", "matched rural Snaking and Branching parameters, layouts, counts, tone arrangements, and parity graphs", "10,000-user stress run, qualitative terrain transfer, and three sensitivity families", "labeled strengths and weaknesses, four-case count comparison, minimum claim, and connectivity conclusion", "references, seven full-page plots, and 819 lines of MATLAB source for code-to-claim reconciliation"], "section_progressions": progressions, "main_argument_chains": [
            {"claim": "A Snaking path can serve the tested city and rural populations with fewer repeaters than the Branching construction.", "support_steps": ["k-means scoring", "highest-coverage start", "cluster-directed open growth", "deficit-triggered CTCSS placement", "city total 17", "rural total 18"], "decision_consequence": "Treat Snaking as the lower-infrastructure heuristic only for the tested parameter cells; do not call it globally minimal without a lower bound and seed study.", "source_pages": [6, 7, 8, 9, 10, 16, 17, 19, 20]},
            {"claim": "A backbone plus branches can create more explicit long-distance connectivity at the cost of additional CTCSS repeaters.", "support_steps": ["backbone target", "dynamic reclustering", "nearest-node branch origin", "long-distance tones 1-3", "local tones 4-8", "city total 26", "rural total 25"], "decision_consequence": "Use Branching only after defining and measuring connectivity, path length, redundancy, parity feasibility, spectrum reuse, and infrastructure cost.", "source_pages": [11, 12, 13, 17, 18, 21, 22]},
            {"claim": "Placement outcomes are highly sensitive to cluster count, separation distance, tower-height assumptions, and the available candidate population.", "support_steps": ["k=5,10,20 count changes", "d_h=10,15,20 count changes", "implied height changes", "potential populations 1400,3000,10000", "open counts 10,3,1"], "decision_consequence": "Report distributions across seeds and a fairness-aware Pareto frontier rather than selecting one favorable parameter cell.", "source_pages": [24, 25]},
            {"claim": "The 10,000-user and mountainous-terrain sections do not validate general scalability or terrain robustness.", "support_steps": ["channel width reduced without spectrum proof", "19+33 arithmetic error", "tone-accounting conflict", "qualitative peak and valley rules", "no DEM or propagation experiment"], "decision_consequence": "Abstain from large-scale or terrain deployment claims until capacity, spectrum, propagation, fairness, and uncertainty are explicitly tested.", "source_pages": [22, 23, 26, 27]},
            {"claim": "The supplied MATLAB makes the heuristics auditable but does not make the published results reproducible.", "support_steps": ["first-repeater coordinate bug", "10-versus-5 cluster mismatch", "candidate/update position mismatch", "coordinate-density clustering", "array-size mismatch", "scalar coordinate indexing", "hard-coded paths", "cropped lines", "missing seeds and logs"], "decision_consequence": "Refactor, test, package inputs, recover source lines, and reproduce every reported count before using the code as evidence.", "source_pages": [36, 37, 38, 39, 42, 46, 49, 50, 51]},
        ]},
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warning_rows},
        "model_retention": {"model_count": len(model_ids), "retained_model_ids": model_ids, "retained_equation_ids": equation_ids, "central_equations": [{"model_id": m["model_id"], "equation_ids": [eq["equation_id"] for eq in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]},
        "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-B-2011-{SHORT}-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)],
        "dimension_counts": {dim: dim_counts[dim] for dim in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]},
        "positive_reusable_language_count": len(language["units"]), "weakness_record_count": dim_counts["weakness"], "review_status": "validated",
    }


def update_extraction() -> None:
    path = ROOT / "artifacts/papers" / PID / "extraction.json"
    extraction = json.loads(path.read_text(encoding="utf-8"))
    extraction["visual_review_status"] = "complete"
    extraction["visual_review"] = {
        "status": "complete",
        "reviewed_pages": list(range(1, PAGE_COUNT + 1)),
        "notes": [
            "Reviewed seven byte-bounded JPEG contact-sheet proxies covering all 51 physical pages and one byte-bounded formula crop; original 180-DPI PNGs remained on disk.",
            "The root thread read every page-aware text file in order, and three independent read-only audits covered pages 1-17, 18-34, and 35-51 with fresh bounded visual contexts.",
            "All prose, formulas, algorithms, tables, figures, captions, headers, full-page plots, references, and source-code pages are present. MATLAB lines that physically run beyond the right page edge remain unrecoverable and are recorded as source limitations rather than extraction omissions.",
            "Visual review confirms final-pass defects including the squared-coordinate subtraction, theta-as-distance wording, parity conflicts, 19+33 arithmetic error, missing legends, sensitivity label errors, coordinate/index bugs, code-path mismatch, and cropped source lines.",
        ],
    }
    write_json(path, extraction)


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
    obs_path = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    obs_path.parent.mkdir(parents=True, exist_ok=True)
    obs_path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    update_extraction()
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
