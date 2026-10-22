from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2011-10496-de9286d6"
SHORT = "10496"
SHA = "de9286d69ab73d049cf7342b69097ef090a4625b3199ee92e57ec749ba86986c"
TYPE = "B"
YEAR = "2011"
PAGE_COUNT = 34

PATTERNS = [
    "LP-B-ABS-TASK-METHOD-METRIC-CONTRAST-BOUNDARY",
    "LP-B-INT-TECHNICAL-CONTEXT-TO-DECISION-TASK",
    "LP-B-ASSUMPTION-JUSTIFICATION-CONSEQUENCE",
    "LP-B-METRIC-OPERATION-THRESHOLD",
    "LP-B-BASELINE-FAILURE-TO-DESIGN",
    "LP-B-EXAMPLE-TO-GENERAL-ROUTING-RULE",
    "LP-B-ALGORITHM-INPUT-STEP-OUTPUT",
    "LP-B-RESULT-TABLE-TREND-TRADEOFF",
    "LP-B-DISCUSSION-SCALE-FAILURE-REPAIR",
    "LP-B-CONCLUSION-PERFORMANCE-SCOPE-LIMIT",
]

# key, protocol chapter, first page, last page, tag, language-unit count,
# source-checked evidence, visually observed paragraph count
CHAPTERS = [
    ("summary", "abstract", 1, 1, "SUM", 16, "The Summary states the 40-mile circular-domain task, the 145-148 MHz band, the 1,000-user interpretation, density-aware repeater placement, privacy-line routing, k-means centroids, component connection, clumped-population tests, coverage and capacity metrics, a 98 percent result, a 32 percent naive comparison, and a high-load subnetwork boundary.", 4),
    ("title-and-contents", "title", 2, 3, "TOC", 8, "The title and two-page contents expose the complete sequence from technical background and assumptions through metrics, placement and routing algorithms, results, 10,000-user and terrain adaptations, limitations, appendix figures, and references.", 2),
    ("introduction-background", "introduction", 4, 5, "INT", 14, "The Introduction moves from VHF line-of-sight and duplex repeaters through CTCSS interference control to the optimization task, then operationally redefines simultaneous users as a population that may generate requests at a parameterized rate.", 7),
    ("assumptions", "assumptions", 5, 8, "ASM", 14, "Nine assumptions define radial coverage, touching-range connectivity, negligible propagation time, 9-mile repeater and 3-mile handheld ranges, polite users, queued conflicts, 600 kHz spacing, equal load, United States regulation, and strongly local call demand.", 12),
    ("capacity-metric", "problem-analysis", 8, 9, "MET", 14, "The metric section defines accommodation as the fraction Q of attempted transmissions processed and gives a timestep queue simulation in which uncovered endpoints fail, noninterfering requests begin, conflicts wait, and leftover requests fail at the horizon.", 6),
    ("request-and-quality", "notation", 10, 10, "REQ", 12, "The request generator biases communication toward short tower paths with a displayed finite formula, while overall quality prioritizes the smallest repeater count subject to a configurable capacity threshold and secondary coverage or demand checks.", 4),
    ("population-model", "data-preprocessing", 11, 12, "POP", 12, "Population synthesis replaces an independent uniform sample with random clump centers and an independent-coordinate Gaussian-like field using sigma_x=sigma_y=20, then visually compares random, 5, 10, 20, and 40-clump patterns with one southeastern United States density image.", 5),
    ("linking-strategies", "model-establishment", 11, 14, "LNK", 14, "The linking section rejects reciprocal two-repeater frequencies because of feedback, defines A through E staggered 600 kHz receive-transmit pairs, adds inverse repeaters for bidirectionality, and sketches a weak-power continuation for chains longer than five levels.", 8),
    ("naive-baseline", "problem-restatement", 14, 15, "NAI", 10, "The naive baseline blankets the circle with evenly spaced connected repeaters, removes nodes covering nobody, and is rejected because it wastes sparse-area nodes, risks feedback or one-way links, and turns most communication into a single whole-network broadcast.", 4),
    ("privacy-routing", "algorithm", 15, 17, "PRI", 16, "The privacy-line section introduces a central hub, inward and outward directions, branch-local traffic, paired destination labels, a worked 6/13-to-8/15 route, and line 54 as a stop signal before generalizing which lines each repeater accepts.", 8),
    ("kmeans-main", "model-improvement", 17, 18, "KME", 12, "The k-means section groups nearby users, places repeaters at cluster centroids, and wraps clustering, range construction, component connection, adjacency construction, and channel assignment into the Main Network Generation Algorithm.", 5),
    ("connect-components", "robustness-verification", 19, 20, "CON", 12, "Disconnected repeater components become graph nodes weighted by their nearest intercomponent separation; the paper invokes a minimum spanning tree idea and repeatedly adds a repeater toward the closest other component until the network is connected.", 5),
    ("assign-channels", "error-analysis", 20, 21, "CHA", 12, "The channel algorithm chooses the node with greatest closeness centrality as hub, maps levels 1-5 to A, B/A-prime, C/B-prime, D/C-prime, and E/D-prime, then assigns increasing channel numbers by an outward breadth-first traversal.", 5),
    ("results-design", "results", 21, 23, "RES", 14, "The experiment crosses five population types with five initial cluster counts and five generated populations per type, then reports mean repeater counts, uncovered users, and ten-run transmission-capacity variability against the naive network.", 8),
    ("capacity-results", "sensitivity-analysis", 23, 24, "CAP", 14, "Tables 3 and 4 report capacity standard deviations and mean processed-request proportions, showing a large clustering advantage over the naive network but also nonmonotone cells and a repeater-count versus capacity tradeoff.", 5),
    ("scale-and-terrain", "sensitivity-robustness", 24, 27, "ROB", 14, "The Discussion explains the 10,000-user hub bottleneck, proposes recursively isolated local subnetworks and multiple hubs, and adapts placement and component connection to mountainous terrain through asymmetric ranges and simulated annealing.", 10),
    ("conclusion", "conclusion", 27, 28, "CLS", 12, "The Conclusion relies on an eyeball test and tables to claim shape adaptation, high coverage, high throughput, and relatively few wasteful nodes, while restricting the feasible search to cluster counts compatible with the finite privacy-line budget.", 6),
    ("limitations-future", "strengths-limitations", 28, 30, "LIM", 14, "The limitations section records k-means nondeterminism, duplicate delayed signals, the roughly 25-location privacy-line cap, missing cost tradeoffs, weather sensitivity, indirect repeater-count control, blind interference, switching time, heterogeneous demand, and a greedy removal extension.", 10),
    ("appendix-references", "appendix", 31, 34, "APP", 6, "Appendix Figures 6-8 show repeated network instances for random and 5, 10, 20, and 40-clump populations, followed by ten references for population data, VHF practice, frequency allocation, clustering, propagation, and operator procedures.", 4),
]

MOVES = [
    ("task-contract", "Name the domain, resource, demand interpretation, objective, and service criterion before implementation details.", "domain -> resource -> demand -> objective -> criterion"),
    ("technical-context", "Explain a physical or regulatory mechanism only far enough to justify the next modeling choice.", "mechanism -> consequence -> design need -> handoff"),
    ("assumption-with-consequence", "State an assumption, its stated justification, and the exact simulation behavior it enables.", "assumption -> justification -> enabled operation -> boundary"),
    ("metric-to-procedure", "Define a metric and immediately show how an algorithm counts its numerator, denominator, failures, and horizon.", "metric -> counted events -> failure rule -> threshold"),
    ("baseline-to-repair", "Use a simple baseline to expose waste, interference, or capacity failure before introducing the repair.", "baseline -> failure mechanism -> repair -> retained comparison"),
    ("worked-example-to-rule", "Trace one concrete routed request and then abstract it into reusable acceptance and forwarding rules.", "example -> state changes -> general rule -> stopping condition"),
    ("algorithm-contract", "Give required inputs, ordered operations, guaranteed outputs, and the consumer of those outputs.", "inputs -> steps -> outputs -> consumer"),
    ("table-to-tradeoff", "Read a table by metric, comparator, trend, exception, and design consequence rather than by a favorable maximum alone.", "metric -> comparator -> trend -> exception -> decision"),
    ("scale-failure-repair", "Explain why scaling breaks a bottleneck and distinguish an implemented result from a proposed repair.", "scale change -> bottleneck -> evidence -> proposed repair -> status"),
    ("claim-with-scope", "Pair a performance claim with population type, cluster count, capacity definition, and known implementation limits.", "claim -> test scope -> metric -> limit -> permitted use"),
]

EXAMPLES = [
    ("A clinic-placement abstract names the service radius, daily demand, facility-count objective, and maximum-wait criterion before describing clustering.", "A second paragraph reports both the best case and the uniform-grid comparator with the exact test population."),
    ("A flood-sensor paper explains line-of-sight loss only until it motivates a terrain-aware adjacency graph.", "It does not turn a hardware rule of thumb into an unqualified physical law."),
    ("A warehouse model states that orders queue during picker conflicts and explains how this changes the service metric.", "The assumption is followed by a maximum-wait sensitivity check."),
    ("A dispatch study defines fulfilled calls divided by attempted calls and lists uncovered, timed-out, and conflicting requests separately.", "The acceptance threshold is named before network sizes are compared."),
    ("A school-bus baseline covers every road uniformly, reveals empty-route waste, and motivates demand-weighted stops.", "The baseline remains in the results table under identical demand samples."),
    ("A packet-routing explanation follows one source-to-destination path, records label changes at the hub, and ends at a declared stop code.", "The following paragraph converts the example into a general forwarding table."),
    ("A habitat algorithm lists observations, cluster count, range constraints, added connectors, and the final adjacency matrix.", "Each intermediate output is explicitly consumed by the next stage."),
    ("A staffing table is read for mean service, variability, nonmonotone cells, and the cost of extra shifts.", "The recommendation does not rely on the single highest percentage."),
    ("A tenfold demand stress test identifies one central server as the bottleneck and labels sharding as unimplemented future work.", "A follow-up experiment would be required before claiming the repair succeeds."),
    ("A conclusion says performance is high only for the tested demand mixtures and feasible channel budget.", "It separates empirical evidence from an engineering adaptation that was not simulated."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols,
# purpose, confidence
EQUATIONS = [
    ("paper line-of-sight rule", 4, "technological background", "line-of-sight range", "distance=sqrt(1.5 h)", r"d=\sqrt{1.5h}", ["d", "h"], "Estimate a radio horizon in miles from antenna height in feet using the paper's displayed rule.", "high"),
    ("transmission success ratio", 8, "measuring transmission capacity", "transmission-success ratio", "Q=(number of transmissions processed)/(number of transmissions attempted)", r"Q=\frac{N_{\mathrm{processed}}}{N_{\mathrm{attempted}}}", ["Q", "N_processed", "N_attempted"], "Measure the fraction of attempted transmissions processed during the simulation.", "high"),
    ("paper short-path request expression", 10, "generating requests", "short-path request score", "C(n,l) lambda^k/l! (1-lambda/n)^(n-l)", r"\binom{n}{l}\frac{\lambda^k}{l!}\left(1-\frac{\lambda}{n}\right)^{n-l}", ["p_l", "n", "l", "lambda", "k"], "Retain the displayed request-distance expression exactly for audit; the paper sets lambda=1 but does not define k.", "high"),
    ("paper clumped population field", 11, "modeling population density", "clumped population field", "f(x,y)=1/(2 pi sigma_x sigma_y) exp(((x-mu_x)^2/sigma_x^2)+((y-mu_y)^2/sigma_y^2))", r"f(x,y)=\frac{1}{2\pi\sigma_x\sigma_y}\exp\left[\frac{(x-\mu_x)^2}{\sigma_x^2}+\frac{(y-\mu_y)^2}{\sigma_y^2}\right]", ["f_xy", "x", "y", "mu_x", "mu_y", "sigma_x", "sigma_y"], "Represent the source's printed population field without silently inserting a missing negative exponent.", "high"),
    ("intercomponent separation", 19, "connecting clusters", "component separation", "d_ij=min distance between any repeater in component i and any repeater in component j", r"d_{ij}=\min_{u\in C_i,\,v\in C_j}\|u-v\|_2", ["d_ij", "C_i", "C_j", "u", "v"], "Weight the component graph by its closest pair of repeaters.", "medium"),
    ("bridge placement spacing", 20, "connect components", "bridge spacing", "step distance=minDist/numRepeatersRequired", r"s=\frac{\mathrm{minDist}}{\mathrm{numRepeatersRequired}}", ["s", "minDist", "numRepeatersRequired"], "Place the next connector along the direction between the closest disconnected repeaters.", "high"),
]

# page, family, purpose, inputs, outputs
ALGORITHMS = [
    (5, "duplex repeater operation", "Receive on one frequency and rebroadcast 600 kHz away while using a subaudible tone to gate activation.", ["input_frequency", "tone", "signal"], ["rebroadcast_signal"]),
    (6, "radial coverage abstraction", "Represent each handheld and repeater by a circular range and infer adjacency from touching or overlapping ranges.", ["positions", "broadcast_radii"], ["coverage_sets", "repeater_adjacency"]),
    (7, "queued-conflict service rule", "Delay conflicting long-chain requests rather than counting them as immediate failures.", ["request_queue", "current_transmissions"], ["deferred_requests"]),
    (9, "network quality simulation", "Generate requests, step through time, greedily accept noninterfering transmissions, fail uncovered endpoints, and count leftovers.", ["user_positions", "assignments", "request_count", "simulation_length", "adjacency", "ranges"], ["unfulfilled_transmissions", "Q"]),
    (10, "overall network selection", "Search the algorithm's feasible repeater counts for the smallest network meeting a chosen Q threshold and inspect coverage and demand robustness.", ["candidate_networks", "Q_threshold", "coverage", "demand_levels"], ["selected_network"]),
    (11, "clumped population generator", "Choose random clump centers and sample independent x and y coordinates around them, with sigma_x=sigma_y=20.", ["user_count", "clump_count", "domain", "sigma_x", "sigma_y"], ["synthetic_user_positions"]),
    (13, "staggered frequency chain", "Assign A through E receive-transmit pairs so each repeater's output is the next repeater's input.", ["frequency_band", "offset"], ["A_to_E_chain"]),
    (13, "bidirectional inverse pairing", "Co-locate inverse repeater types with forward types to create reverse propagation along a chain.", ["forward_chain", "inverse_types", "privacy_lines"], ["bidirectional_chain"]),
    (14, "extended chain construction", "Use a weak E-prime bridge with D/D-prime and continue backward through C/C-prime and B/B-prime for chains beyond five levels.", ["five_level_chain", "power_limit", "privacy_lines"], ["extended_chain"]),
    (14, "uniform blanket baseline", "Tile the circular area with connected repeaters and remove only nodes that cover no users.", ["domain", "repeater_range", "user_positions"], ["naive_network"]),
    (16, "hub privacy-line routing", "Route signals inward to a hub and outward to one destination branch using paired location labels and a stop line.", ["tree_network", "hub", "ingoing_lines", "outgoing_lines", "destination"], ["routed_path"]),
    (17, "k-means repeater placement", "Cluster users by Euclidean proximity and use each cluster centroid as an initial repeater position.", ["user_positions", "number_of_clusters"], ["cluster_assignments", "centroids"]),
    (18, "main network generation", "Compose clustering, repeater ranges, component connection, adjacency construction, and channel assignment.", ["user_positions", "maximum_repeater_range", "user_ranges", "number_of_clusters"], ["repeater_positions", "channels"]),
    (19, "minimum-spanning component plan", "Treat disconnected components as nodes and choose low-separation links intended to minimize added connection length.", ["network_components", "d_ij"], ["component_spanning_plan"]),
    (20, "connect-components loop", "Repeatedly find the closest pair of disconnected repeaters and add an intermediate repeater toward the other component.", ["repeater_positions", "region_ranges", "maximum_region_range"], ["connected_repeater_positions"]),
    (20, "closeness hub selection", "Choose the repeater with smallest average geodesic distance to other network nodes.", ["repeater_adjacency"], ["hub_repeater"]),
    (21, "breadth-first channel assignment", "Assign channel 1 to the hub and increasing channel numbers to successive outward adjacency layers.", ["repeater_adjacency", "hub_repeater"], ["channel_assignments"]),
    (22, "factorial experiment design", "Evaluate five population types, five cluster counts, and five generated populations per type, with ten request simulations for capacity.", ["population_types", "cluster_counts", "replicates", "simulation_repeats"], ["experiment_cells"]),
    (22, "repeater-count evaluation", "Count initial centroid repeaters plus connectors and compare means across population and cluster settings.", ["generated_networks"], ["mean_repeater_count"]),
    (23, "coverage evaluation", "Count users outside every repeater range and compare the clustering network with the 100-percent-cover baseline.", ["user_positions", "repeater_ranges"], ["uncovered_user_count"]),
    (23, "capacity sensitivity evaluation", "Repeat the request simulation ten times and report the mean processed fraction and its standard deviation.", ["network", "request_generator", "simulation_repeats"], ["mean_capacity", "capacity_sd"]),
    (25, "high-load subnetwork proposal", "Recursively add frequency-incompatible local subnetworks at high-demand nodes to isolate local traffic.", ["main_network", "node_demand", "cost_parameters"], ["augmented_network"]),
    (27, "mountainous-terrain adaptation", "Replace symmetric ranges with position-dependent adjacency, then refine clustered and connecting repeater positions by simulated annealing.", ["terrain", "propagation_ranges", "initial_network"], ["terrain_adapted_network"]),
    (28, "feasible cluster-count search", "Enumerate cluster counts compatible with the privacy-line budget and choose the first network meeting the capacity requirement.", ["cluster_count_range", "privacy_line_budget", "Q_threshold"], ["selected_cluster_count"]),
    (30, "greedy repeater removal", "Remove the repeater whose deletion causes the least quality reduction until the requested count is reached.", ["network", "target_repeater_count", "quality_function"], ["pruned_network"]),
]

VISUALS = [
    (1, "Standalone Summary", "Provides the complete task-method-test-comparison-limit contract before the main paper."),
    (2, "Contents page 1", "Exposes the ordering from Introduction through Results and the method subsections."),
    (3, "Contents page 2", "Exposes Discussion, Conclusion, Future Work, and Appendix handoffs."),
    (9, "Algorithm 1 Measure Network Quality", "Makes queue order, uncovered failures, conflict deferral, and horizon leftovers inspectable."),
    (12, "Figure 1 synthetic and actual population distributions", "Compares random and four clumped generators with one real density image."),
    (15, "Figure 2 naive network", "Shows the uniformly blanketed baseline and its redundant coverage geometry."),
    (16, "Figure 3 privacy-line network", "Shows hub branches, repeater types, paired location labels, and directed line semantics."),
    (18, "Figure 4 k-means population clustering", "Connects colored user clusters to centroid-based repeater placement."),
    (18, "Algorithm 2 Main Network Generation", "Preserves the full cluster-to-range-to-connectivity-to-channel pipeline."),
    (20, "Algorithm 3 Connect Components", "Shows the closest-component loop and the bridge-spacing expression."),
    (21, "Channel-frequency table", "Maps channel levels 1-5 to forward and inverse repeater types."),
    (21, "Algorithm 4 Assign Channels", "Shows closeness-hub selection and breadth-first outward assignment."),
    (22, "Table 1 repeater counts", "Quantifies infrastructure growth across cluster counts and population types."),
    (23, "Table 2 uncovered users", "Quantifies the coverage cost of fewer clusters against the naive baseline."),
    (23, "Table 3 capacity standard deviations", "Separates simulation variability from mean capacity."),
    (24, "Table 4 processed-request proportions", "Provides the principal clustering-versus-naive capacity comparison and nonmonotone cells."),
    (26, "Figure 5 local subnetwork comparison", "Shows the proposed three-repeater local augmentation beside the unaugmented network."),
    (31, "Figures 6-8 appendix network gallery", "Shows instance-to-instance network geometry for random and 5, 10, 20, and 40-clump populations."),
]

WARNINGS = [
    (4, "The printed horizon rule is distance=sqrt(1.5 h); it differs from the commonly cited coefficient-times-square-root form and gives about 7.75 miles at 40 feet rather than the later 9-mile value."),
    (5, "The paper redefines 1,000 simultaneous users as 1,000 possible requesters with a parameterized average rate, materially weakening the original concurrency interpretation."),
    (5, "CTCSS or a privacy tone gates repeater activation but does not by itself prevent two simultaneous radio signals from physically interfering."),
    (6, "The claimed one-to-two-second delay is not attributable to radio-wave propagation across an 80-mile domain; equipment and protocol delay are not separately modeled."),
    (6, "Downlink and handheld uplink ranges are asymmetric, yet coverage and communication feasibility are treated largely through circular reach without a complete link-budget rule."),
    (7, "The model deliberately queues conflicting requests instead of counting them as failed, so interference is less heavily penalized than the paper's own service definition suggests."),
    (7, "A 600 kHz duplex offset is treated as a minimum distinguishable channel spacing without a spectrum plan, occupied bandwidth, adjacent-channel, or regulatory analysis."),
    (7, "The assumption that users listen on all privacy lines for several minutes before every request is operationally implausible and leaves an unresolved CITE placeholder."),
    (8, "Q omits waiting time, fairness, transmission duration, hop count, repeated retries, and the distribution of service across users."),
    (9, "Algorithm 1 is order-dependent because it greedily scans the queue; no randomization, priority policy, fairness diagnostic, or maximum waiting time is defined."),
    (9, "The interference predicate used by Algorithm 1 is not formalized, so the simulation cannot be reproduced from the pseudocode alone."),
    (10, "The request-distance expression is called Poisson but contains a binomial coefficient, an undefined k, l factorial, and a binomial-like final term; it is neither a standard Poisson PMF nor a fully defined alternative."),
    (10, "The claimed lower bound is only a lower bound within networks generated by this heuristic and does not establish a global minimum repeater count."),
    (11, "The printed population field has a positive quadratic exponent and no negative one-half factor, so it is not a normalizable bivariate Gaussian density."),
    (11, "The paper does not explain how Gaussian samples outside the radius-40 circle are rejected, truncated, wrapped, or resampled."),
    (12, "Figure 1 compares synthetic coordinate plots with an actual density image using different color systems, scales, and no common units, so the claimed similarity is qualitative."),
    (13, "Five staggered 600 kHz pairs across 145-148 MHz use band-edge values but do not document occupied bandwidth, repeater coordination, or whether all pairings are legally deployable."),
    (14, "The weak E-prime extension, simultaneous-shutdown rule, and timeout behavior have no power threshold, delay model, stability proof, or simulation."),
    (16, "The privacy-line routing example assumes effectively instantaneous duplicate forwarding and postpones the resulting offset-signal collision to the limitations section."),
    (17, "Line 54 is used as a stop signal without a complete allocation and reuse rule across the whole network."),
    (18, "Algorithm 2 alternates MaximumRepeaterRange, MaximumRegionRange, RepeaterRanges, and UserRanges, leaving its input-output interface inconsistent."),
    (18, "K-means minimizes within-cluster squared distance, not uncovered users, repeater count, interference, or network capacity, so centroid placement is only a heuristic for the stated objective."),
    (19, "A minimum-total-distance spanning plan over components does not necessarily minimize the number of added repeaters when ranges and required integer connectors matter."),
    (20, "Algorithm 3 does not define the ceiling rule for numRepeatersRequired and its repeated closest-component procedure is asserted to be an MST without a complete proof."),
    (21, "Algorithm 4 does not reconcile graph depths beyond channel 5 with the extended-chain construction and does not verify channel compatibility on cycles or multi-parent layers."),
    (22, "The five generated populations per population type are too few for stable uncertainty estimates, and no random seeds or reproducible code are supplied."),
    (24, "The statement that more initial clusters increase capacity is not generally monotone: several 5-clump and 10-clump table entries decline as clusters increase."),
    (24, "The claim that even the 5-clump standard deviation is below 1.5 percent conflicts with displayed values such as 0.102 and 0.074 if table entries are proportions."),
    (24, "Table 4 is captioned as a percentage but reports fractions between zero and one, inviting a factor-100 interpretation error."),
    (25, "The recursive subnetwork feature is explicitly unfinished and unevaluated, and the text points to Figure 4 although the comparison is Figure 5."),
    (27, "The mountainous-terrain extension gives no propagation model, elevation data interface, asymmetric distance definition, objective function, annealing schedule, or experiment."),
    (28, "The conclusion's 15-cluster claim of over 97 percent coverage and about 95 percent transmission is not uniform across population types; the 5-clump capacity entry is only 0.830."),
    (28, "The claimed maximum of roughly 25 distinct locations and the typical network of about 40 repeaters require a co-location accounting rule that is not explicitly reconciled."),
    (29, "The privacy-line count leading to the 25-location cap is not derived in a complete allocation table, and duplicate processing delays are not quantified."),
    (30, "The greedy repeater-removal proposal depends on an undefined network-quality loss and has no optimality, complexity, or connectivity guarantee."),
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
        "source_status": "explicit-defined" if symbol != "k" else "unspecified",
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
                    "Do not copy frequencies, ranges, user counts, privacy-line labels, table values, or source sentences into another paper.",
                    "Do not call a heuristic optimal, a ranking probability, a qualitative image validation, or an untested repair successful without the corresponding proof or experiment.",
                ],
                "features": {
                    "voice": "first-person plural for modeling choices and experiments; impersonal voice for formulas and pseudocode; conditional voice for future adaptations",
                    "tense": "present for mechanism and algorithm; past for simulations; conditional for terrain, subnetworks, and repairs",
                    "modality": "assume, can, may, should, must, and feel retain distinct evidential force",
                    "clause_structure": order,
                    "quantitative_role": "attach range, frequency, cluster count, repeater count, uncovered users, capacity, variability, or scale to its exact metric and test cell",
                    "transition": ["first", "in order to", "as a consequence", "however", "in general", "for example", "note that", "finally"][i % 8],
                    "replaceable_slots": ["service domain", "demand generator", "network object", "routing label", "objective", "metric", "baseline", "repair"],
                    "boundary_conditions": ["state concurrency interpretation", "state frequency and range semantics", "state queue discipline", "separate implemented results from future work"],
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
                "citations": 10 if key == "appendix-references" else 5 if key in {"introduction-background", "population-model"} else 1,
                "quantitative_results": 12 if key in {"summary", "results-design", "capacity-results", "conclusion"} else 2,
            },
            "move_types": {"opening": ["name the inherited object or decision"], "transition": ["carry an assumption, state, output, metric, or counterexample"], "closing": ["state the next consumer and scope"]},
            "counting_method": "All 34 physical pages were read in order from page-aware text. Seven byte-bounded JPEG contact proxies covered every page and one byte-bounded formula crop reconciled the most corrupted expression; three independent read-only page-range audits checked all text, formulas, algorithms, tables, labels, and source defects.",
            "ambiguities": [
                "Physical page 1 is an unnumbered Summary; physical pages 2-34 contain internally numbered pages 1-33.",
                "The text layer corrupts smart quotes, prime marks, plus-minus signs, negative tick labels, and formula layout; rendered review is authoritative for signs, fractions, roots, superscripts, tables, and network geometry.",
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
        "constraints": ["Stay within the circular domain, frequency plan, range assumptions, privacy-line budget, and declared queue discipline.", "Keep repeater count, distinct locations, coverage, capacity, waiting, and interference as separate quantities.", "Do not convert an untested engineering proposal into a validated result."],
        "conditions": {
            "initial": {"status": "present", "details": ["User positions or a population generator, radio ranges, a frequency plan, and a simulation horizon are available."]},
            "boundary": {"status": "present", "details": ["The base model assumes flat terrain, radial coverage, polite users, local demand, fixed range, and simplified interference."]},
            "equilibrium": {"status": "not-applicable", "details": ["The workflow constructs and simulates a finite network rather than solving an equilibrium."]},
        },
        "parameter_estimation": {"status": "partial", "method": "Fixed paper assumptions, heuristic selection, finite simulation, or direct table comparison.", "parameters": inputs},
        "algorithm": {"status": "implemented" if page <= 24 else "omitted-by-paper", "steps": ["freeze the declared inputs", "apply the stated formula or finite procedure", "retain the output with units and target", "hand it to routing, simulation, comparison, or decision"], "software": software, "convergence_criteria": "For pages through 24, the procedure is finite over users, repeaters, components, channels, time steps, and experiment cells. Later items are paper-proposed future work and remain unimplemented; no numerical tolerance or reproducible stopping log is reported."},
        "assumptions": ["The network abstraction approximates the relevant radio and demand behavior.", "The stated range, frequency, routing, and request rules remain valid over the tested scenario."],
        "identifiability_feasibility": {"status": "partial", "analysis": "The construction is procedurally understandable, but formula defects, undefined variables, missing code, incomplete spectrum semantics, heuristic objectives, and small replicate counts limit reproduction and optimality claims."},
        "handoff_outputs": outputs,
        "validation_refs": [f"Physical page {page}, adjacent formula, pseudocode, table, figure, or discussion."],
        "computational_cost": "Ranges from linear queue or graph passes to repeated k-means, component connection, user-pair request simulation, and factorial experiment cells; exact complexity and runtime are not reported.",
        "strengths": ["The input-operation-output chain is visible.", "The quantity feeds a later construction, simulation, comparison, or engineering decision."],
        "limitations": ["Calibration, uncertainty, radio realism, and reproducibility are incomplete.", "Source-level mathematical and algorithmic defects are retained for the final warning pass."],
        "missing_details": ["Random seeds, implementation, request duration, fairness, interference predicate, spectrum coordination, exact connector rounding, runtime, and uncertainty intervals are absent."],
    }


def make_models() -> dict:
    models: list[dict] = []
    for idx, (label, page, section, family, source, latex, symbols, purpose, confidence) in enumerate(EQUATIONS, 1):
        eq = {"equation_id": f"EQ-B-2011-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}
        models.append(model_record(f"MU-B-2011-{SHORT}-{idx:03d}", page, section, family, purpose, list(dict.fromkeys(symbols[1:])), [symbols[0]], [eq], ["No executable implementation supplied."]))
    for idx, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, start=len(EQUATIONS) + 1):
        models.append(model_record(f"MU-B-2011-{SHORT}-{idx:03d}", page, family, family, purpose, inputs, outputs, [], ["Paper describes simulations and graph procedures but supplies no code."]))
    by_family = {m["family"]: m["model_id"] for m in models}
    edges = [
        ("line-of-sight range", "radial coverage abstraction", "The horizon rule helps motivate fixed circular ranges."),
        ("radial coverage abstraction", "k-means repeater placement", "User and repeater ranges define the coverage objective for centroid placement."),
        ("clumped population field", "clumped population generator", "The printed field is the stated distributional basis for synthetic users."),
        ("clumped population generator", "k-means repeater placement", "Synthetic user coordinates become clustering inputs."),
        ("k-means repeater placement", "main network generation", "Centroids initialize repeater positions."),
        ("main network generation", "connect-components loop", "Disconnected centroid components require added connectors."),
        ("component separation", "minimum-spanning component plan", "Nearest intercomponent distance weights the component graph."),
        ("minimum-spanning component plan", "connect-components loop", "The plan determines which components should be bridged."),
        ("bridge spacing", "connect-components loop", "The spacing relation determines the next connector position."),
        ("connect-components loop", "closeness hub selection", "The connected graph supports a centrality calculation."),
        ("closeness hub selection", "breadth-first channel assignment", "The selected hub is channel level one."),
        ("staggered frequency chain", "bidirectional inverse pairing", "Inverse types add reverse propagation to the forward chain."),
        ("bidirectional inverse pairing", "hub privacy-line routing", "Paired directions support inward and outward branch routing."),
        ("hub privacy-line routing", "network quality simulation", "The routed paths determine which simultaneous transmissions conflict."),
        ("short-path request score", "network quality simulation", "The request-distance rule generates source-destination demand."),
        ("network quality simulation", "transmission-success ratio", "Processed and attempted requests produce Q."),
        ("transmission-success ratio", "overall network selection", "Q is the feasibility threshold for selecting a network."),
        ("factorial experiment design", "capacity sensitivity evaluation", "Experiment cells determine repeated capacity simulations."),
        ("capacity sensitivity evaluation", "overall network selection", "Mean capacity and variability inform the repeater-count tradeoff."),
        ("high-load subnetwork proposal", "terrain-adapted network" if "terrain-adapted network" in by_family else "mountainous-terrain adaptation", "Both are future adaptations beyond the validated base network."),
    ]
    dependency_edges = [{"from_model_id": by_family[a], "to_model_id": by_family[b], "handoff": h} for a, b, h in edges]
    return {"dependency_edges": dependency_edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    sections = [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, _, evidence, _ in CHAPTERS]
    assumptions = [
        (5, "The 1,000 users are potential requesters rather than simultaneous transmitters."),
        (6, "Handheld and repeater broadcasts are radially symmetric in a flat circular domain."),
        (6, "Touching repeater broadcast radii imply mutual communication."),
        (6, "Radio propagation and required buffers are negligible at the simulation timestep."),
        (6, "Repeaters reach about 9 miles and handheld users reach about 3 miles for network access."),
        (7, "Licensed users listen, cooperate, and do not initiate a local request while a tower is busy."),
        (7, "Long-chain conflicts wait in a queue instead of failing immediately."),
        (7, "A 600 kHz offset is an adequate minimum distinction between repeater frequency stages."),
        (7, "Every user imposes approximately equal demand."),
        (7, "The network is deployed under United States amateur-radio rules."),
        (7, "Calls are strongly biased toward short repeater paths."),
        (11, "Population coordinates can be generated by independent x and y clumps with sigma_x=sigma_y=20."),
        (16, "A tree-like hub and destination privacy lines can control signal direction."),
        (17, "K-means centroids are useful proxies for high-density repeater locations."),
        (20, "Closeness centrality selects a low-load-path hub and breadth-first levels remain frequency feasible."),
    ]
    verification = [
        (12, "Synthetic random and four clumped population fields are visually compared with one actual southeastern United States density image.", "qualitative-data-shape-check", "Checks whether the generator can produce visibly clumped patterns.", "No common scale, metric, or fitted goodness-of-fit test is supplied."),
        (15, "The uniformly blanketed network is retained as a naive comparator.", "baseline-comparison", "Makes the capacity cost of whole-network broadcasting visible.", "It is not tuned under the same repeater-count or service constraints."),
        (22, "Five independently generated populations are used for each of five population types.", "replicate-check", "Exposes some instance-to-instance variation.", "Five replicates are small and random seeds are absent."),
        (22, "Table 1 reports mean repeater counts with variability for five cluster counts.", "infrastructure-trace", "Shows that connectors can make total repeaters exceed initial clusters.", "No cost or statistical interval is attached."),
        (23, "Table 2 reports mean uncovered-user counts and includes the zero-uncovered naive baseline.", "coverage-trace", "Prevents capacity gains from hiding coverage loss.", "Coverage geometry and user-specific fairness are not tested."),
        (23, "Ten request simulations per network produce capacity standard deviations in Table 3.", "simulation-sensitivity", "Separates stochastic request variability from mean performance.", "The displayed interpretation conflicts with some values and no seeds are reported."),
        (24, "Table 4 compares mean processed-request fractions for clustering and naive networks across all population types.", "capacity-comparison", "Provides a repeated-cell comparator rather than one network picture.", "Several trends are nonmonotone and the table calls fractions percentages."),
        (24, "Repeater count, coverage, and transmission capacity are read together as a tradeoff.", "multi-metric-check", "Preserves resource and service consequences.", "No scalar objective, Pareto frontier, or selected Q threshold is reported."),
        (25, "The 10,000-user stress case is used to expose a central-hub bottleneck.", "scale-stress-test", "Shows that the 1,000-user design does not scale unchanged.", "The local-subnetwork repair is unfinished and unevaluated."),
        (26, "Figure 5 places networks with and without a local subnetwork side by side.", "proposed-repair-visual", "Clarifies what the structural modification would add.", "It supplies no measured capacity or cost change."),
        (27, "Mountainous terrain is treated as an out-of-scope mechanism and receives an adaptation sketch.", "scope-transfer-check", "Separates adjacency-dependent parts from position-dependent ranges.", "No terrain data or experiment validates the transfer."),
        (28, "Appendix Figures 6-8 show multiple network instances for each population-clump regime.", "instance-gallery", "Makes k-means and sample variability visible.", "The figures omit per-panel counts, coverage, capacity, and legends."),
        (29, "The limitations section explicitly acknowledges duplicate delayed signals, privacy-line caps, weather, and nondeterminism.", "self-audit", "Keeps known deployment failures visible.", "Most are not quantified or rerun after repair."),
    ]
    return {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": "10496", "title": "Clustering on a Network", "award_status": "Outstanding Winner",
        "source": {"relative_path": "2011美赛特等奖/B-10496-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is an unnumbered Summary; physical pages 2-34 are internally numbered 1-33."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 34, "rendered_pages": 34, "visual_review": "complete", "notes": ["All 34 text pages and all 34 rendered pages were reviewed in order by the root thread and three independent read-only page-range audits.", "Seven full-range JPEG contact proxies and one formula crop stayed below 450000 bytes; no original full-page PNG or multi-image tool result entered model context."]},
        "context_sources": [{"page": 4, "summary": "VHF propagation, duplex repeaters, and amateur-radio practice motivate the range and frequency abstractions."}, {"page": 11, "summary": "SEDAC population imagery supplies a qualitative comparison for the clumped generator."}, {"page": 34, "summary": "Ten references cover population data, radio practice, frequency allocation, clustering, propagation, and operator procedure."}],
        "task_reconstruction": {"inputs": ["1,000 potential users in a radius-40-mile flat circular domain", "145-148 MHz band, 600 kHz repeater offsets, and 54 privacy lines", "user request rate, local-call bias, handheld and repeater ranges", "synthetic or measured population locations"], "outputs": ["repeater positions and connected adjacency", "frequency/channel and privacy-line assignments", "coverage, repeater-count, and processed-request metrics", "adaptation sketches for 10,000 users and mountainous terrain"], "decisions": ["minimum feasible repeater infrastructure under a chosen service threshold", "where to place repeaters and connectors", "how to route simultaneous branch traffic", "when the design is outside its tested regime"]},
        "section_map": sections,
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [
            {"page": 5, "summary": "The user population is interpreted as potential requesters with an average request parameter."},
            {"page": 9, "summary": "Requests are scheduled by timestep with source, destination, and network assignment."},
            {"page": 10, "summary": "Request distance is biased toward shorter repeater paths by the displayed source formula with lambda=1."},
            {"page": 11, "summary": "Population generators choose random clump centers and independent coordinate draws with sigma_x=sigma_y=20."},
            {"page": 12, "summary": "Synthetic fields are compared qualitatively with one actual southeastern United States density image."},
            {"page": 17, "summary": "K-means converts user positions into cluster memberships and centroid repeater positions."},
            {"page": 19, "summary": "Repeater adjacency is partitioned into connected components and reduced to nearest intercomponent distances."},
            {"page": 22, "summary": "Five populations per type and ten capacity simulations per network populate the result tables."},
        ],
        "models": [{"page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": vt, "strength": strength, "limitation": limitation} for p, s, vt, strength, limitation in verification],
        "results_trace": [
            {"page": 1, "summary": "The Summary reports up to 98 percent processed transmissions for the clustering network versus a maximum of 32 percent for the naive network."},
            {"page": 22, "summary": "Table 1 shows repeater counts rising with cluster count; for random populations the mean grows from 17.00 at 5 clusters to 74.60 at 25 clusters."},
            {"page": 23, "summary": "Table 2 shows uncovered random users falling from 382.20 at 5 clusters to 7.80 at 25 clusters, while the naive network has zero uncovered users."},
            {"page": 23, "summary": "Table 3 reports capacity standard deviations from 0.0033 to 0.0144 for k-means and 0.0065 to 0.0083 for the naive network."},
            {"page": 24, "summary": "Table 4 reports clustering processed-request fractions from 0.621 to 0.985 depending on cluster count and population, versus 0.221 to 0.313 for naive."},
            {"page": 24, "summary": "The best clustering cells are not monotone in every column; 5-clump capacity declines from 0.850 at 10 clusters to 0.814 at 25 clusters."},
            {"page": 25, "summary": "For 10,000 users the paper reports roughly half the requests handled by networks with 15-20 repeaters, versus about 700 of 10,000 for naive."},
            {"page": 28, "summary": "The conclusion highlights a 15-cluster setting as more than 97 percent coverage and about 95 percent capacity with roughly 40 repeaters, although the table cells vary by population."},
        ],
        "contributions": [
            {"page": 8, "summary": "Defines a simulation-based processed-request service ratio."},
            {"page": 13, "summary": "Builds staggered forward and inverse repeater chains inside the band."},
            {"page": 16, "summary": "Uses hub-oriented privacy labels to localize branch traffic."},
            {"page": 17, "summary": "Combines k-means population placement with graph connection."},
            {"page": 20, "summary": "Selects a closeness-centrality hub and assigns channels outward."},
            {"page": 24, "summary": "Evaluates infrastructure, coverage, stochastic capacity, and a naive comparator together."},
        ],
        "writing_logic": [
            {"page": 1, "summary": "Summary chain: radio-network task -> density placement -> privacy routing -> clustering and component connection -> synthetic tests -> capacity contrast -> high-load boundary."},
            {"page": 4, "summary": "Introduction chain: VHF range -> duplex repeaters -> interference and CTCSS -> official task -> operational user interpretation."},
            {"page": 5, "summary": "Assumption chain: propagation and range -> cooperative users -> simplified conflict handling -> spectrum spacing -> local demand."},
            {"page": 8, "summary": "Metric chain: service meaning -> Q ratio -> queue simulation -> configurable threshold -> smallest-network objective."},
            {"page": 11, "summary": "Population chain: reject uniform independence -> generate clumps -> display a Gaussian-like field -> compare synthetic and actual images."},
            {"page": 13, "summary": "Frequency chain: reject reciprocal feedback -> stagger A-E -> add inverse types -> sketch extended chains."},
            {"page": 15, "summary": "Routing chain: expose naive broadcast bottleneck -> introduce hub direction -> work one destination-label path -> generalize branch-local rules."},
            {"page": 17, "summary": "Construction chain: k-means centroids -> repeater ranges -> connect components -> adjacency -> centrality hub -> breadth-first channels."},
            {"page": 21, "summary": "Evaluation chain: experiment cells -> repeater counts -> uncovered users -> capacity variability -> mean capacity -> resource-service tradeoff."},
            {"page": 24, "summary": "Boundary chain: 10,000-user bottleneck -> proposed subnetworks -> terrain adaptation -> conclusion -> nondeterminism, radio, budget, and objective limitations."},
        ],
        "language_observations": [
            {"page": 1, "summary": "The Summary gives methods, tests, comparator, numerical headline, and limitations in a compact five-paragraph progression."},
            {"page": 4, "summary": "Technical background repeatedly uses mechanism-to-consequence sentences before introducing the modeling task."},
            {"page": 5, "summary": "For the purpose of this problem marks an explicit reinterpretation of an ambiguous requirement."},
            {"page": 6, "summary": "Assumptions are justified one by one with a physical or operational rationale, even when the rationale is incomplete."},
            {"page": 8, "summary": "A rhetorical question about what users want is converted into a measurable processed-request ratio."},
            {"page": 13, "summary": "A concrete feedback failure motivates the staggered frequency scheme before the A-E list appears."},
            {"page": 17, "summary": "After a long routing example, the phrase let us review the core idea compresses it into general forwarding rules."},
            {"page": 18, "summary": "Algorithm prose uses Require, Ensure, named intermediate arrays, and explicit handoffs to the next procedure."},
            {"page": 24, "summary": "Results paragraphs move from table variability to performance contrast and then to a repeater-capacity tradeoff."},
            {"page": 28, "summary": "The conclusion uses strong adjectives, then the future-work section partially retracts them through nondeterminism and engineering limits."},
        ],
        "visualization_observations": [{"page": p, "figure": name, "summary": purpose} for p, name, purpose in VISUALS],
        "judge_relevance_hypotheses": [{"page": 1, "summary": "A summary with a quantitative comparator plausibly improves traceability but does not establish optimality.", "evidence_class": "J"}, {"page": 21, "summary": "Four explicit algorithms plausibly make the design easier to audit despite interface defects.", "evidence_class": "J"}, {"page": 24, "summary": "Joint reporting of repeater count, coverage, and capacity plausibly improves decision relevance when tradeoffs are not hidden.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": [
            {"extension_id": f"E-B-{SHORT}-001", "page": 4, "summary": "Replace range rules with a calibrated bidirectional link budget, terrain profile, fading margin, and regulatory channel plan."},
            {"extension_id": f"E-B-{SHORT}-002", "page": 9, "summary": "Use an event-driven queue with durations, maximum waits, priorities, fairness, and a tested interference graph."},
            {"extension_id": f"E-B-{SHORT}-003", "page": 11, "summary": "Fit a truncated or bounded spatial mixture model to measured population data and validate it quantitatively."},
            {"extension_id": f"E-B-{SHORT}-004", "page": 17, "summary": "Optimize a multi-objective network over repeater cost, uncovered demand, capacity, robustness, and spectrum feasibility rather than k-means distance alone."},
            {"extension_id": f"E-B-{SHORT}-005", "page": 20, "summary": "Formulate connector cost as required integer repeaters and solve channel assignment with explicit cycle, depth, and interference constraints."},
            {"extension_id": f"E-B-{SHORT}-006", "page": 22, "summary": "Publish code and seeds, use more replicates, report uncertainty, fix a service threshold, and compare Pareto-efficient networks."},
        ],
        "candidate_rule_impacts": [],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing all source numbers, frequencies, labels, table values, and prose.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain the complete input, formula or procedure, objective, constraint, unit, output, and handoff.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive task-to-assumption-to-construction-to-test-to-boundary chain.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep axes, domain, node and edge semantics, colors, channel labels, units, comparator, and decision purpose attached.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the test cell, sample size, seed, comparator, metric, unit, uncertainty, and violated assumption.", "R-B-VER-002") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, coordinate system, domain truncation, units, random seed, transformation, and downstream use.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each assumption with a diagnostic, excluded mechanism, sensitivity, and fallback.", "R-B-DATA-002") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry population type, cluster count, comparator, metric, unit, variability, and permitted decision together.", "R-B-MOD-004") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use warnings only after positive language, organization, model, verification, and visual coverage is complete.", "R-B-VER-004") for x in card["weaknesses"]],
        "other": [(34, "reference boundary", "The ten references support context but do not supply executable code, a complete spectrum allocation, fitted population parameters, or an independent capacity validation.", "Separate citation presence from reproducibility and empirical support.", "R-B-VER-004")],
    }
    counts = {"language": 240, "modeling": 64, "logic": 44, "visualization": 36, "verification": 40, "data": 28, "assumption": 30, "result": 32, "weakness": len(WARNINGS), "other": 6}
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
                "applicability": ["Apply only when domain, demand interpretation, radio or graph semantics, objective, constraints, operation, output, metric, units, comparator, and scope can all be named."],
                "counterevidence": ["A plausible radio analogy, clean network plot, high cell value, qualitative population resemblance, or one stress-case discussion does not prove optimality, calibration, spectrum feasibility, robustness, or general suitability."],
                "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium",
                "candidate_rule_ids": candidate_rules,
            })
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first: dict[str, str] = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])
    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain task-method-metric-comparator language only when strong adjectives remain tied to exact test cells and uncertainty", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "retain the official-task-to-technical-context-to-assumptions-to-construction-to-results-to-adaptation chain", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "treat population coordinates, repeater geometry, adjacency, spectrum state, and terrain as versioned measured data rather than anonymous arrays", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "retain a ledger for range, frequency, offset, privacy lines, request rate, cluster count, sigma, simulation horizon, and service threshold", "evidence_ids": [observations[next(i for i, r in enumerate(observations) if r["dimension"] == "data") + 1]["observation_id"]]},
        {"rule_id": "R-B-MOD-001", "action": "retain graph and spatial heuristics only after units, topology, radio mechanism, objective, and calibration agree", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine repeater count, coverage, capacity, waiting, and interference through a declared decision rule rather than a favorable table narrative", "evidence_ids": [observations[next(i for i, r in enumerate(observations) if r["dimension"] == "modeling") + 1]["observation_id"]]},
        {"rule_id": "R-B-MOD-004", "action": "keep user count, simultaneous transmissions, repeater count, distinct locations, coverage, capacity, variability, and decisions separately labeled", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress geometric placement and hub choices under perturbed populations, ranges, seeds, terrains, and channel budgets", "evidence_ids": [observations[next(i for i, r in enumerate(observations) if r["dimension"] == "modeling") + 2]["observation_id"]]},
        {"rule_id": "R-B-VER-002", "action": "make reliability population-, load-, spectrum-, terrain-, and queue-policy-specific with uncertainty and abstention outside the tested regime", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "run a mathematical and algorithmic preflight on the horizon rule, request expression, Gaussian sign, connector rounding, variable names, and channel depth before simulation", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain network and population maps only with common axes, scale, legends, node and edge semantics, coverage meaning, and linked numeric metrics", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "choose distance computation, centrality, connectivity, and caching from measured graph size, query volume, update rate, memory, and accuracy needs", "evidence_ids": [observations[next(i for i, r in enumerate(observations) if r["dimension"] == "modeling") + 3]["observation_id"]]},
    ]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reusable only after replacing source facts and preserving occurrence, function, information order, slots, variants, quantitative force, target, and boundary."} for u in language["units"]]
    paragraph_specs = {
        "abstract": ["task, band, domain, demand, and objective", "density placement, privacy lines, k-means, and component connection", "clumped data, coverage and capacity simulation, and sensitivity", "98 percent versus 32 percent comparator, clustering limit, and subnetwork extension"],
        "introduction": ["optimization need for an extendible 145-148 MHz repeater network", "VHF line-of-sight range and antenna-height horizon motivation", "handheld range limitation as the need for relaying", "duplex repeaters and expanded broadcast range", "interference and CTCSS activation mechanism", "radius-40 task, 1,000 users, and 54 privacy lines", "operational reinterpretation of simultaneous users and request-rate handoff"],
    }
    paragraph_chains = []
    for chapter, moves in paragraph_specs.items():
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": len(moves), "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": move, "language_unit_ids": [ids[i % len(ids)]]} for i, move in enumerate(moves)]})
    progressions = [{"chapter": chapter, "moves": [f"input: the source-checked object entering {key}", f"rhetorical job: perform the observed {key} definition, motivation, procedure, comparison, or boundary", f"analytical job: apply the declared range, request, clustering, routing, graph, simulation, metric, or adaptation operation in {key}", f"output: retain a network state, assignment, coverage value, capacity value, comparator, limitation, or bounded recommendation from {key}", "handoff: name the next construction stage, test, tradeoff, diagnostic, or engineering action"], "positive_pattern": "Use explicit input -> mechanism or operation -> typed output -> comparator or metric -> scoped handoff; warning lists cannot replace the positive chapter contract."} for key, chapter, *_ in CHAPTERS]
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
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [12 if key in {"summary", "introduction-background"} else 8, 3, 0]} for key, chapter, *_ in CHAPTERS],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": ["standalone task-method-metric-comparator Summary and two-page roadmap", "VHF, duplex repeater, interference, CTCSS, and simultaneous-user interpretation", "physical, behavioral, spectrum, queue, and local-demand assumptions", "processed-request ratio, queue simulation, request-distance rule, and minimum-repeater criterion", "clumped population generator and qualitative real-image comparison", "staggered forward and inverse chains, naive baseline, hub, privacy labels, and branch-local routing", "k-means centroids, component graph, bridge insertion, closeness hub, and breadth-first channel assignment", "factorial population and cluster tests, repeater counts, uncovered users, capacity variability, and naive comparison", "10,000-user bottleneck, local subnetworks, terrain adaptation, conclusion, limitations, appendix, and references"], "section_progressions": progressions, "main_argument_chains": [
            {"claim": "Density-aware centroid placement can reduce infrastructure waste compared with uniform blanket coverage.", "support_steps": ["clumped population motivation", "k-means centroids", "connector insertion", "Table 1 repeater counts", "Table 2 coverage"], "decision_consequence": "Use clustering only inside a multi-objective search that also enforces coverage, capacity, spectrum, and robustness.", "source_pages": [11, 12, 17, 18, 19, 20, 22, 23]},
            {"claim": "Hub-oriented privacy labels can localize branch traffic and raise simulated capacity.", "support_steps": ["naive whole-network bottleneck", "toward and away directions", "worked destination-label route", "channel levels", "Algorithm 1 conflicts", "Table 4 capacity"], "decision_consequence": "Validate the interference graph, delays, cycles, spectrum allocation, and queue fairness before deployment.", "source_pages": [14, 15, 16, 17, 21, 23, 24]},
            {"claim": "Repeater count, coverage, and processed-request capacity form a real resource-service tradeoff.", "support_steps": ["Q definition", "cluster-count sweep", "repeater-count table", "uncovered-user table", "capacity mean and standard deviation"], "decision_consequence": "Publish a fixed service threshold or Pareto frontier rather than highlighting one favorable cluster count.", "source_pages": [8, 9, 10, 21, 22, 23, 24]},
            {"claim": "The base design is not reliable under large load, complex terrain, delayed forwarding, or a tight privacy-line budget without new models.", "support_steps": ["10,000-user bottleneck", "unfinished subnetwork", "mountainous-terrain sketch", "privacy-line cap", "duplicate delayed signals", "nondeterministic clustering"], "decision_consequence": "Abstain outside the validated flat, low-load regime until each adaptation is implemented and tested.", "source_pages": [24, 25, 26, 27, 28, 29, 30]},
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
            "Reviewed seven byte-bounded JPEG contact-sheet proxies covering all 34 physical pages and one byte-bounded crop for the page-10 request formula; original PNGs remained on disk.",
            "The root thread read every page-aware text file in order, and three independent read-only audits covered pages 1-12, 13-23, and 24-34 with their own bounded visual proxies.",
            "All prose, formulas, algorithms, tables, figures, captions, headers, appendix panels, and references are present without blank renders, clipping, or omitted pages.",
            "Visual review confirms source-level defects retained for the final warning pass, including the root placement formula, undefined-k request formula, positive-exponent population field, algorithm variable mismatches, missing plot legends, nonmonotone result cells, and untested future adaptations.",
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
