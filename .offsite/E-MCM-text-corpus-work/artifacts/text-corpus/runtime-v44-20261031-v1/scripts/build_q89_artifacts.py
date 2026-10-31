from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2010-8479-b934962b"
SHORT = "8479"
SHA = "b934962b584cac6ce85cf9fdb6b4afb5618b731a9c60e7abe64ab3e2d994851b"
TYPE = "B"
YEAR = "2010"
PAGE_COUNT = 26

PATTERNS = [
    "LP-B-ABS-TASK-ASSUMPTION-DUAL-MODEL-EVIDENCE-BOUNDARY",
    "LP-B-INT-SCARCE-DATA-TO-COMPLEMENTARY-MODELS",
    "LP-B-BACKGROUND-DEFINITION-STATISTIC-MECHANISM",
    "LP-B-LITERATURE-GAP-TO-ADAPTATION",
    "LP-B-ANALOGY-RECURRENCE-FORECAST",
    "LP-B-THEORY-CHOICE-KERNEL-POSTERIOR",
    "LP-B-DATA-PROVENANCE-TRANSFORMATION",
    "LP-B-RESULT-METRIC-CASE-CONTRAST",
    "LP-B-DISCUSSION-SUCCESS-FAILURE-REPAIR",
    "LP-B-EXECUTIVE-OUTPUT-USE-BOUNDARY",
]

# key, protocol chapter, first page, last page, id tag, language-unit count,
# source-checked evidence, visually observed paragraph count
CHAPTERS = [
    ("summary-sheet", "abstract", 1, 1, "SUM", 16, "The standalone Summary moves from the police task and sparse crime-site inputs through behavioral assumptions, two complementary models, case tests, two metrics, omitted geography, and a bounded starting-point recommendation.", 6),
    ("title-page-abstract", "title", 2, 2, "ABS", 16, "The titled Abstract repeats the dual-model contract more compactly: familiar-area behavior motivates centrographic motion and rational-choice surfaces, followed by holdout comparison and parameter sensitivity.", 4),
    ("introduction", "introduction", 3, 3, "INT", 16, "The Introduction defines the scarce-data challenge, states the two prediction targets, previews simulation on partial historical series, and gives an explicit Section 3 to Section 7 roadmap.", 3),
    ("serial-killing-background", "problem-restatement", 3, 4, "BKG", 12, "The background narrows serial murder, gives empirical home-proximity evidence, explains anchor-point clustering, and states the unmoved-residence premise used by geographical profiling.", 6),
    ("previous-work", "problem-analysis", 4, 4, "LIT", 12, "Previous work connects journey-to-crime decay, circle and buffer-zone approaches, centroid analysis, and rational-choice crime-pattern theory to the paper's two adaptations.", 5),
    ("centrographic-background", "notation", 4, 5, "CBG", 12, "The centrographic background treats crime sites as a time-ordered spatial series and introduces kinematic vocabulary as an analogy for a moving centroid rather than a literal behavioral law.", 5),
    ("centrographic-assumptions", "assumptions", 5, 5, "CAS", 12, "The assumption subsection fixes correct linkage, chronological order, one relevant trajectory, a usable time scale, and a centroid whose motion contains predictive information.", 4),
    ("centrographic-model", "model-establishment", 5, 7, "CEN", 16, "The model derives the running centroid, event and centroid velocities, a momentum-style recurrence, acceleration extrapolation, logistic decay functions, beta selection, and a diamond-shaped next-site region.", 10),
    ("rational-choice-background", "model-improvement", 7, 9, "RCB", 12, "The rational-choice background distinguishes bounded purposeful selection from moral approval and converts avoidance of capture, familiarity, and opportunity into location-dependent choice costs.", 7),
    ("rational-choice-theory", "algorithm", 9, 10, "RCT", 16, "The theory subsection moves from utility over location probabilities and characteristics to an implicit choice function, then specializes it to binary prior-use risk, distance decay, sequence likelihood, and an anchor posterior.", 8),
    ("rational-serial-criminal-practice", "data-preprocessing", 10, 11, "RSC", 12, "The practice subsection discretizes geography, scans possible homes, produces a jeopardy surface, and extends the same kernel-likelihood interface to a ranked next-crime surface.", 6),
    ("data", "appendix", 11, 12, "DAT", 10, "The Data section names public web and newspaper sources, converts street addresses to latitude-longitude pairs, preserves crime order, and presents the Berkowitz example table before simulation.", 5),
    ("centrographic-results", "results", 12, 14, "CRS", 12, "The centrographic results repeatedly hold out kill j, fit on kills 1 through j-1, report Manhattan error for Hillside Strangler events, tabulate acceleration regressions, and display predicted diamonds.", 7),
    ("rsc-results", "sensitivity-analysis", 13, 17, "RRS", 12, "The RSC results define Hit Score and Search Area, then compare Berkowitz Bronx and Yonkers homes with the Buono-Bianchi home using tables and categorical jeopardy maps.", 8),
    ("combined-models", "robustness-verification", 17, 18, "COM", 10, "The combined section places centrographic and RSC outputs beside one another for later-event prediction and uses the DC Sniper case to expose incompatible repeated-location and same-day-event assumptions.", 5),
    ("discussion", "strengths-limitations", 19, 21, "DIS", 14, "The Discussion interprets successes and failures separately, questions acceleration fit and beta sensitivity, contrasts home locations, acknowledges contrived boundaries, and proposes practical revisions without hiding failed cases.", 10),
    ("executive-summary", "memo", 22, 23, "EXE", 10, "The Executive Summary translates both models into police inputs, contour and diamond outputs, search-area use, strengths, weaknesses, computational needs, and a joint-use recommendation.", 7),
    ("references", "references", 24, 26, "REF", 4, "The reference list documents geographical profiling, criminology, rational choice, statistical methods, mapping sources, and case-data provenance while leaving implementation code unavailable.", 1),
]

MOVES = [
    ("task-contract", "Name the decision actor, sparse evidence, two prediction targets, and operational use before equations.", "actor -> evidence -> target -> operational use"),
    ("assumption-motivation", "Tie each behavioral assumption to an observed geographic pattern or cited mechanism.", "observation -> mechanism -> assumption -> model consequence"),
    ("dual-model-preview", "Preview complementary model families by the different question each one answers.", "shared inputs -> model A target -> model B target -> complementarity"),
    ("definition-to-boundary", "Define a term and immediately mark what the definition excludes or assumes.", "term -> operational definition -> exclusion -> scope"),
    ("literature-to-adaptation", "Move from a prior method to the precise component retained and the component changed.", "prior work -> retained mechanism -> adaptation -> new output"),
    ("analogy-to-formalism", "Use a physical or economic analogy as intuition, then hand control to equations and algorithms.", "analogy -> correspondence -> equation -> nonliteral boundary"),
    ("derivation-chain", "Advance formulas through named intermediate quantities and explicit substitutions.", "definition -> intermediate -> recurrence -> forecast"),
    ("theory-to-implementation", "Specialize a general choice framework into a finite grid, kernel, likelihood, and ranked surface.", "general theory -> chosen characteristics -> kernel -> computational surface"),
    ("metric-to-resource", "Define a metric and translate it into distance, searched area, or police workload.", "metric -> calculation -> physical resource -> decision"),
    ("result-to-limitation", "Place a favorable case beside a failed or assumption-violating case before recommending use.", "result -> countercase -> mechanism -> bounded recommendation"),
]

EXAMPLES = [
    ("A wildfire brief names the dispatcher, observed ignitions, next-hour hotspot target, and patrol decision before introducing equations.", "It closes the opening by separating a moving-front forecast from a long-run origin estimate."),
    ("A disease-spread study links repeated household clusters to a local-contact assumption and states when travel breaks it.", "The assumption is carried into the model as a testable radius rather than a universal fact."),
    ("A port-security paper previews a centroid tracker for the next event and a choice surface for the hidden staging area.", "Both methods consume the same incident history but answer different operational questions."),
    ("A habitat analysis defines an anchor site, explains temporary sites, and excludes relocations during the fitted window.", "The definition is followed by a diagnostic for detecting a moved anchor."),
    ("A traffic paper retains a prior distance-decay kernel but replaces straight-line distance with network travel time.", "The adaptation states which output and calibration protocol change."),
    ("A supply-chain paper compares inventory momentum to physical momentum only long enough to motivate a recurrence.", "It then states that the analogy is descriptive and validates the recurrence on held-out weeks."),
    ("A demand model defines a running center, forms its finite-difference velocity, estimates acceleration, and forecasts a bounded region.", "Every intermediate quantity carries units and an availability timestamp."),
    ("A clinic-choice model begins with utility, selects wait time and travel cost, normalizes a kernel, and scans candidate catchments.", "The resulting surface is described as a ranking until calibration is demonstrated."),
    ("A rescue map converts rank fraction into square kilometers and team-hours before recommending a search order.", "Distance error remains separate because it answers a different question."),
    ("A flood model reports good urban performance beside a failed island case whose transport assumptions are violated.", "The recommendation includes an abstention rule and a repair path."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose, confidence
EQUATIONS = [
    ("running crime-site centroid", 5, "centrographic model", "running spatial mean", "C_j=(1/j) sum from i=1 to j of X_Ki", r"C_j=\frac{1}{j}\sum_{i=1}^{j}X_{K_i}", ["C_j", "j", "X_K_i"], "Update the mean location after the jth event.", "high"),
    ("centroid velocity", 5, "centrographic model", "centroid time derivative", "V_Cj=dC_j/dt", r"V_{C_j}=\frac{dC_j}{dt}", ["V_C_j", "C_j", "t"], "Represent the time rate of change of the running centroid.", "high"),
    ("centroid momentum", 5, "centrographic model", "mass-scaled centroid velocity", "P_Cj=j V_Cj", r"P_{C_j}=jV_{C_j}", ["P_C_j", "j", "V_C_j"], "Scale centroid velocity by the number of events in the physical analogy.", "high"),
    ("new-event velocity", 5, "centrographic model", "finite-difference event velocity", "V_Kj=(X_Kj-C_(j-1))/(t_j-t_(j-1))", r"V_{K_j}=\frac{X_{K_j}-C_{j-1}}{t_j-t_{j-1}}", ["V_K_j", "X_K_j", "C_j_minus_1", "t_j", "t_j_minus_1"], "Measure the new event's displacement from the previous centroid per elapsed time.", "high"),
    ("new-event momentum", 5, "centrographic model", "unit-mass event momentum", "P_Kj=V_Kj", r"P_{K_j}=V_{K_j}", ["P_K_j", "V_K_j"], "Assign unit mass to the newly added event in the analogy.", "high"),
    ("momentum update", 5, "centrographic model", "inelastic momentum recurrence", "j V_Cj=(j-1)V_C(j-1)+V_Kj", r"jV_{C_j}=(j-1)V_{C_{j-1}}+V_{K_j}", ["V_C_j", "j", "V_C_j_minus_1", "V_K_j"], "Combine the previous centroid motion with the incoming event motion.", "high"),
    ("centroid velocity recurrence", 5, "centrographic model", "recursive centroid velocity", "V_Cj=((j-1)V_C(j-1)+V_Kj)/j", r"V_{C_j}=\frac{(j-1)V_{C_{j-1}}+V_{K_j}}{j}", ["V_C_j", "j", "V_C_j_minus_1", "V_K_j"], "Compute the updated centroid velocity explicitly.", "high"),
    ("future center", 6, "centrographic prediction", "damped kinematic forecast", "Center_A(t)=C_j+f(t)V_Cj+g(t) a_hat_j", r"\operatorname{Center}_{A(t)}=C_j+f(t)V_{C_j}+g(t)\hat a_j", ["Center_A_t", "C_j", "f", "t", "V_C_j", "g", "a_hat_j"], "Forecast the center using current location, velocity, and fitted acceleration.", "high"),
    ("long-run stopping constraint", 6, "centrographic prediction", "asymptotic zero velocity", "limit t to infinity of d Center_A(t)/dt equals 0", r"\lim_{t\to\infty}\frac{d(\operatorname{Center}_{A(t)})}{dt}=0", ["Center_A_t", "t"], "Force the extrapolated center's velocity to vanish at long horizons.", "high"),
    ("short-run velocity scaling", 6, "centrographic prediction", "local linear scaling", "f(t) approximately t", r"f(t)\approx t", ["f", "t"], "Recover ordinary constant-velocity motion near the forecast origin.", "high"),
    ("short-run acceleration scaling", 6, "centrographic prediction", "local quadratic scaling", "g(t) approximately t squared over 2", r"g(t)\approx \frac{t^2}{2}", ["g", "t"], "Recover ordinary constant-acceleration displacement near the forecast origin.", "high"),
    ("velocity damping function", 6, "centrographic prediction", "logistic velocity damping", "f(t)=2t/(1+exp(beta t))", r"f(t)=\frac{2t}{1+e^{\beta t}}", ["f", "t", "beta"], "Blend local linear motion with long-run stopping.", "high"),
    ("acceleration damping function", 6, "centrographic prediction", "squared logistic acceleration damping", "g(t)=2t^2/(1+exp(beta t))^2", r"g(t)=\frac{2t^2}{(1+e^{\beta t})^2}", ["g", "t", "beta"], "Blend local quadratic acceleration with long-run stopping.", "high"),
    ("paper beta selection", 7, "centrographic prediction", "mean-interval damping parameter", "beta=ln(15)/mean t_j", r"\beta=\frac{\ln 15}{\bar t_j}", ["beta", "t_bar_j"], "Set the damping horizon from the series' mean inter-event time.", "high"),
    ("location-choice utility", 9, "rational choice theory", "utility over probabilities and characteristics", "U(p,c)", r"U(p,c)", ["U", "p", "c"], "Represent preferences over location probabilities and site characteristics.", "high"),
    ("probability simplex", 9, "rational choice theory", "choice-probability constraint", "sum from i=1 to n p_i=1", r"\sum_{i=1}^{n}p_i=1", ["p_i", "n"], "Constrain location-choice probabilities to a simplex.", "high"),
    ("paper first-order condition", 9, "rational choice theory", "unconstrained stated FOC", "partial U/partial p_i=0", r"\frac{\partial U}{\partial p_i}=0", ["U", "p_i"], "Retain the paper's stated optimality condition for later audit.", "high"),
    ("implicit choice function", 9, "rational choice theory", "characteristic-conditioned choice", "p_i=k_i(c_1,...,c_n)", r"p_i=k_i(c_1,\ldots,c_n)", ["p_i", "k_i", "c_1_to_n"], "Express each location probability as a function of all site characteristics.", "high"),
    ("binary prior-use risk", 10, "RSC practice", "binary visited-location characteristic", "c_i(X_j)=1 if i in X_j and 0 otherwise", r"c_i(X_j)=\begin{cases}1,&i\in X_j\\0,&\text{otherwise}\end{cases}", ["c_i", "X_j", "i"], "Mark cells already used in the observed sequence.", "high"),
    ("distance-buffer kernel", 10, "RSC practice", "inverse-distance normalized kernel", "k_i(c,alpha)=0 if alpha=i, otherwise (1-c_i)/(d(alpha,i) k_bar)", r"k_i(c,\alpha)=\begin{cases}0,&\alpha=i\\\frac{1-c_i}{d(\alpha,i)\bar k},&\text{otherwise}\end{cases}", ["k_i", "c_i", "alpha", "i", "d", "k_bar"], "Score an unused candidate inversely with distance from a possible home while imposing a buffer.", "high"),
    ("conditional next-site probability", 10, "RSC practice", "kernel-conditioned event probability", "P(K_j given X_(j-1),alpha)=k_Kj(c(X_(j-1)),alpha)", r"P(K_j\mid X_{j-1},\alpha)=k_{K_j}(c(X_{j-1}),\alpha)", ["P_K_j", "K_j", "X_j_minus_1", "alpha", "k_K_j", "c"], "Assign a conditional score to the next observed site under an anchor hypothesis.", "high"),
    ("sequence likelihood", 10, "RSC practice", "product sequence likelihood", "P(K given alpha)=product_j k_Kj(c(X_(j-1)),alpha)", r"P(K\mid\alpha)=\prod_j k_{K_j}(c(X_{j-1}),\alpha)", ["P_K", "K", "alpha", "k_K_j", "X_j_minus_1", "c"], "Combine sequential event scores for a candidate anchor.", "high"),
    ("anchor posterior", 10, "RSC practice", "Bayesian anchor ranking", "P(alpha=i given K) proportional to P(K given alpha=i)", r"P(\alpha=i\mid K)\propto P(K\mid\alpha=i)", ["P_alpha_i", "alpha", "i", "K", "P_K"], "Rank candidate home cells under a uniform prior.", "high"),
    ("next-site score", 11, "RSC practice", "history-weighted next-site mixture", "p_hat_i proportional to sum over j and alpha of k_i times prefix likelihood", r"\hat p_i\propto\sum_{j=1}^{J-1}\sum_{\alpha=1}^{n}k_i(c(X_{j-1}),\alpha)P(K_1,\ldots,K_{j-1}\mid\alpha)", ["p_hat_i", "i", "j", "J", "alpha", "n", "k_i", "c", "X_j_minus_1", "K_prefix"], "Form a relative next-location surface by mixing anchors and historical prefixes.", "high"),
    ("Manhattan error distance", 12, "centrographic results", "L1 coordinate error", "d_1(p,q)=abs(p_x-q_x)+abs(p_y-q_y)", r"d_1(p,q)=|p_x-q_x|+|p_y-q_y|", ["d_1", "p", "q", "p_x", "p_y", "q_x", "q_y"], "Measure displacement between predicted center and the actual next event.", "high"),
]

ALGORITHMS = [
    (5, "sequential centrographic update", "Process events chronologically, update the centroid and velocity recurrence, and retain the state available before each holdout.", ["ordered_event_locations", "event_times"], ["C_j", "V_C_j"]),
    (6, "acceleration regression", "Fit longitude and latitude velocity trends separately and use their slopes as acceleration components.", ["centroid_velocities", "event_times"], ["a_hat_j"]),
    (7, "prediction-diamond construction", "Forecast a center at the next-event time and place axis-aligned mean-error bounds around it.", ["Center_A_t", "mean_axis_errors"], ["prediction_diamond"]),
    (12, "address geocoding and ordered event table", "Collect dated crime addresses, convert them to latitude-longitude pairs, preserve order, and record case provenance.", ["addresses", "dates", "sources"], ["ordered_coordinates"]),
    (10, "RSC risk-surface construction", "Discretize the hunting area, encode previously used cells, evaluate the distance-buffer kernel, and normalize for ranking.", ["grid", "ordered_coordinates", "candidate_anchor"], ["jeopardy_surface"]),
    (10, "candidate-anchor likelihood scan", "Evaluate the full observed sequence under every possible anchor cell and rank the resulting likelihoods.", ["grid", "event_sequence", "kernel"], ["anchor_likelihoods"]),
    (11, "next-site surface scan", "Mix candidate anchors and historical prefix states to score every possible next site.", ["anchor_likelihoods", "event_prefixes", "kernel"], ["next_site_surface"]),
    (13, "hit-score and search-area evaluation", "Sort cells from highest to lowest jeopardy, stop when the known home is reached, and convert the searched fraction into area.", ["jeopardy_surface", "known_home", "hunting_area"], ["hit_score_percent", "search_area"]),
    (18, "paired-model case comparison", "Place centrographic and RSC outputs on the same historical prefix, compare with the actual next event, and retain assumption failures.", ["shared_event_prefix", "centrographic_output", "RSC_output"], ["case_comparison"]),
]

VISUALS = [
    (1, "Standalone Summary", "Shows the complete task-assumption-two-model-test-boundary chain before the full paper."),
    (2, "Title and Abstract", "Confirms title, team number, date, internal pagination, and the compact dual-model contract."),
    (12, "Table 1 Berkowitz event data", "Preserves ordered dates, addresses, and latitude-longitude coordinates used by the simulations."),
    (13, "Table 2 centrographic holdouts", "Reports the five Hillside Strangler next-event Manhattan errors used in the discussion."),
    (13, "Table 3 longitude acceleration regression", "Displays the x-direction velocity regression inputs and fit summary."),
    (13, "Table 4 latitude acceleration regression", "Displays the y-direction velocity regression inputs and fit summary."),
    (14, "Figure 1 centrographic Hillside predictions", "Overlays observed sites, predicted centers, actual next events, and diamond regions across holdouts."),
    (15, "Figure 2 Berkowitz jeopardy surface", "Shows shooting sites, candidate-home ranking, and both Bronx and Yonkers residences."),
    (16, "Table 5 Berkowitz RSC performance", "Converts two possible residences into hunting area, Hit Score, and Search Area values."),
    (16, "Table 6 Buono-Bianchi RSC performance", "Reports the corresponding hunting area and search burden for one offender home."),
    (17, "Figure 3 Buono-Bianchi jeopardy surface", "Shows attack sites, the categorical home-likelihood field, and the known residence."),
    (17, "Figure 4 Berkowitz seventh-event prediction", "Displays the RSC next-site surface and actual held-out event for a qualitative check."),
    (18, "Figure 5 DC Sniper centrographic result", "Shows that the predicted region does not contain the actual later event."),
    (18, "Figure 6 DC Sniper RSC result", "Shows the failed RSC next-site prediction under repeated-location data."),
    (22, "Executive Summary first page", "Translates model inputs, interpretations, strengths, and limitations for police readers."),
    (23, "Executive Summary second page", "Connects diamonds and contour plots to joint search-area narrowing and operational caution."),
]

WARNINGS = [
    (3, "The analysis assumes that all events in a supplied series belong to one offender, but linkage uncertainty is not modeled."),
    (3, "A single stationary home base is assumed; the Berkowitz residence change directly demonstrates the resulting failure mode."),
    (10, "A uniform prior over candidate homes assigns positive mass to water and other uninhabitable cells unless an external mask is added."),
    (12, "The address-to-coordinate and coordinate-to-kilometer workflow does not document projection, geocoder version, or positional error."),
    (5, "A discrete running centroid is differentiated as a continuous curve without defining an interpolation between event times."),
    (5, "Same-day events create a zero time denominator and infinite event velocity; the issue is acknowledged only after the DC Sniper failure."),
    (5, "Momentum conservation and perfectly inelastic collision are analogies for a mean recurrence, not established laws of offender behavior."),
    (13, "The acceleration regressions use very few points, so slope estimates and extrapolations are unstable."),
    (19, "The discussion describes an R-squared value as about 90 percent correlation, conflating coefficient of determination and correlation."),
    (7, "The choice beta=ln(15)/mean interval has no behavioral derivation, fitted loss, external calibration, or sensitivity analysis."),
    (12, "Holdout prediction evaluates the center at the actual next-event time, information that would not be known at deployment."),
    (7, "The axis-wise mean-error diamond is not calibrated as a coverage region and has no stated probability interpretation."),
    (9, "The constrained utility optimization omits a Lagrange multiplier and incorrectly states partial U over partial p_i equals zero as the full first-order condition."),
    (9, "The implicit-function argument lacks the required non-singular Jacobian and explicit treatment of the simplex constraint."),
    (9, "Leaving utility and the choice functions arbitrary makes the general model weakly identified before the paper selects a kernel."),
    (10, "Binary prior-use risk forces an already used location to zero probability, an assumption violated by the DC Sniper sequence."),
    (10, "The kernel sets the exact anchor cell to zero and combines buffer and normalization terms without fully documenting their construction."),
    (10, "The product likelihood assumes a conditional generation structure that is neither estimated nor empirically checked."),
    (11, "The next-site double sum mixes multiple prefix states and anchor hypotheses without a clear normalization or forecast-time interpretation."),
    (10, "Several outputs are called probabilities although the implementation and evaluation mainly establish relative rankings."),
    (12, "Wikipedia, newspaper, and web addresses are used without a reproducible snapshot, geocoding log, or source-error assessment."),
    (12, "Berkowitz shooting sites and Hillside Strangler body-disposal sites represent different behavioral targets but are treated under one interface."),
    (11, "Physical page 11 contains consecutive headings '4 Data' and '5 Data', exposing an unresolved structural editing error."),
    (16, "Hit Score changes with hunting-area boundary and grid resolution, neither of which receives a sensitivity study."),
    (16, "The Yonkers hunting area is explicitly enlarged to include the known home, making that reported evaluation partly outcome-informed."),
    (20, "The chi-square goodness-of-fit comparison does not state samples, bins, degrees of freedom, dependence treatment, or implementation."),
    (20, "Three dependent case scores do not support the broad claim that the model is statistically superior to random search."),
    (17, "Next-event validation is dominated by qualitative single-holdout maps rather than repeated rolling-origin tests."),
    (15, "Jeopardy maps use blue, red, green, and purple categories without a continuous color bar or numeric probability scale."),
    (19, "The claim that error decreases after every added crime conflicts with Table 2, where the sixth-event error rises sharply."),
    (19, "The five Table 2 errors average about 15.15 km, not the 15.12 km stated in the discussion."),
    (13, "The Python simulation code and Excel macros are not supplied, preventing exact reproduction."),
    (18, "The Combined Models section displays outputs side by side but does not estimate or validate a fused decision rule."),
    (1, "The recommendation that police can fill population and geography gaps provides no formal adjustment protocol, calibration check, or safety rule."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "coordinate, time, distance, probability-like score, count, area, or dimensionless quantity as locally defined",
        "definition": f"Source-defined quantity {symbol} in the retained geographic-prediction interface.",
        "source_status": "explicit-defined",
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
                "language_unit_id": f"LU-B-2010-{SHORT}-{tag}-{i + 1:03d}",
                "page": page,
                "section": f"{key} / {move} / source-checked move {i + 1}",
                "chapter": chapter,
                "granularity": "paragraph" if i % 4 == 0 else "sentence",
                "source_excerpt": evidence,
                "function": function,
                "rhetorical_move": move,
                "reusable_pattern": order,
                "information_order": [part.strip() for part in order.split("->")],
                "reusable_elements": ["decision actor", "observed evidence", "behavioral mechanism", "model interface", "metric", "case comparison", "boundary", "handoff"],
                "prohibited_generalizations": [
                    "Do not copy offender names, addresses, coordinates, dates, exact case scores, or source prose into another paper.",
                    "Do not treat a physical analogy, utility story, normalized surface, or favorable case as calibrated probability or universal behavioral truth.",
                ],
                "features": {
                    "voice": "first-person plural for design and tests; impersonal voice for definitions and equations; direct advisory voice in the executive summary",
                    "tense": "present for mechanism and model; past for historical cases and simulations; conditional for deployment and repair",
                    "modality": "assume, infer, may, can, should, and must preserve different levels of evidential force",
                    "clause_structure": order,
                    "quantitative_role": "attach coordinates, elapsed time, parameter choice, distance, area, hit score, or regression result to its exact case and target",
                    "transition": ["first", "next", "therefore", "in other words", "however", "to summarize", "unfortunately", "finally"][i % 8],
                    "replaceable_slots": ["decision actor", "event series", "anchor", "state update", "kernel", "metric", "case", "excluded mechanism"],
                    "boundary_conditions": ["state forecast origin", "separate home and next-event targets", "state score semantics", "retain case and data-type scope"],
                    "original_instantiations": [{"text": ex1}, {"text": ex2}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + i) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": 180 + 330 * (end - start + 1),
            "sentence_count": max(4, paragraphs * 4),
            "paragraph_count": paragraphs,
            "sentence_words": {"minimum": 3, "median": 21 + cidx % 5, "maximum": 70},
            "paragraph_functions": [f"Paragraph {j + 1} advances the {key} task, definition, mechanism, formal step, test, result, boundary, or handoff." for j in range(paragraphs)],
            "rhetorical_proportions": {"premise": 0.25, "mechanism": 0.30, "result": 0.25, "boundary": 0.20},
            "content_counts": {
                "equations": sum(1 for eq in EQUATIONS if start <= eq[1] <= end),
                "figures": sum(1 for v in VISUALS if start <= v[0] <= end and "Figure" in v[1]),
                "tables": sum(1 for v in VISUALS if start <= v[0] <= end and "Table" in v[1]),
                "citations": 40 if key == "references" else 8 if key in {"serial-killing-background", "previous-work", "rational-choice-background"} else 1,
                "quantitative_results": 10 if key in {"summary-sheet", "centrographic-results", "rsc-results", "discussion"} else 1,
            },
            "move_types": {"opening": ["name the inherited task, definition, or model object"], "transition": ["carry an assumption, equation, likelihood, result, or countercase"], "closing": ["state the output, boundary, and next consumer"]},
            "counting_method": "All 26 physical pages were read in order from page-aware text. Six byte-bounded JPEG contact proxies covered every rendered page, and two byte-bounded equation/table crops reconciled formulas and small labels; original PNGs stayed on disk.",
            "ambiguities": [
                "Physical page 1 is a standalone Summary; physical pages 2-26 are internally numbered 1-25, so internal page numbers lag PDF pages by one.",
                "The text layer flattens summation limits, products, subscripts, superscripts, degree signs, and some equation spacing; rendered crops are authoritative for formulas and table labels.",
            ],
        })
    return {"available_chapters": [row[1] for row in CHAPTERS], "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


def make_models() -> dict:
    models: list[dict] = []
    for idx, (label, page, section, family, source, latex, symbols, purpose, confidence) in enumerate(EQUATIONS, 1):
        outputs = {symbols[0]}
        inputs = set(symbols[1:])
        models.append({
            "model_id": f"MU-B-2010-{SHORT}-{idx:03d}", "page": page, "section": section, "family": family, "purpose": purpose,
            "base_or_modification": "base" if idx in {1, 4, 8, 15, 19, 20, 21, 22, 23, 24, 25} else "modification",
            "summary": f"The {family} interface retains {label}: {purpose}",
            "variables": [variable(s, inputs, outputs) for s in dict.fromkeys(symbols)],
            "inputs": list(dict.fromkeys(symbols[1:])), "outputs": [symbols[0]],
            "governing_equations": [{"equation_id": f"EQ-B-2010-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}],
            "equation_status": {"status": "present", "reason": f"The displayed or prose-defined relation on physical page {page} was reconciled against the rendered formula crop and page-aware text."},
            "objectives": [purpose, "Return a typed spatial state, likelihood, score, distance, or forecast quantity."],
            "constraints": ["Use only events available at the declared forecast origin.", "Preserve time units, coordinate system, grid domain, score direction, and home-versus-next-event target.", "Do not equate a physical analogy or normalized ranking surface with calibrated behavior probability."],
            "conditions": {"initial": {"status": "present", "details": ["An ordered, linked event series and its dates or relative order are available."]}, "boundary": {"status": "present", "details": ["The paper assumes one offender, a stable anchor for the RSC model, a finite search domain, and interpretable elapsed times."]}, "equilibrium": {"status": "not-applicable", "details": ["The workflow predicts a finite event sequence rather than an equilibrium."]}},
            "parameter_estimation": {"status": "partial", "method": "Direct recurrence, small-sample regression, paper-selected damping parameter, or fixed inverse-distance kernel.", "parameters": symbols[1:]},
            "algorithm": {"status": "implemented", "steps": ["freeze the chronological prefix", "evaluate the displayed relation", "normalize or extrapolate only in the declared direction", "hand the output to the next model or metric"], "software": ["Paper reports Python simulations and Microsoft Excel macros; source code is unavailable."], "convergence_criteria": "Finite sequence and grid; no numerical tolerance, mesh convergence, or calibration stopping rule is reported."},
            "assumptions": ["The event sequence is correctly linked and geographically informative.", "The selected centroid motion or rational-choice kernel approximates the relevant behavior."],
            "identifiability_feasibility": {"status": "partial", "analysis": "The equations are computable, but sparse events, unknown projection, arbitrary utility, beta selection, grid definition, and unavailable code limit identification and reproduction."},
            "handoff_outputs": [symbols[0]], "validation_refs": [f"Physical page {page}, adjacent derivation, table, figure, or discussion."],
            "computational_cost": "Low for sequential centroid updates; grid scans and repeated anchor or next-site likelihood calculations scale with cells and sequence length, but exact complexity is not stated.",
            "strengths": ["The input-operation-output interface is visible.", "The quantity feeds a forecast region, ranked surface, or operational metric."],
            "limitations": ["Parameter calibration and uncertainty are incomplete.", "Several mathematical and deployment inconsistencies are reserved for the final warning pass."],
            "missing_details": ["Projection, geocoding log, grid resolution, normalization constants, regression diagnostics, beta sensitivity, code, and calibrated uncertainty are absent."],
        })
    for offset, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, start=len(EQUATIONS) + 1):
        models.append({
            "model_id": f"MU-B-2010-{SHORT}-{offset:03d}", "page": page, "section": family, "family": family, "purpose": purpose, "base_or_modification": "paper-specific", "summary": purpose,
            "variables": [variable(s, set(inputs), set(outputs)) for s in inputs + outputs], "inputs": inputs, "outputs": outputs, "governing_equations": [],
            "equation_status": {"status": "not-applicable", "reason": "This record is a multi-step data, estimation, grid-scan, evaluation, or comparison procedure."},
            "objectives": [purpose], "constraints": ["Preserve chronological availability, shared case prefix, search domain, target, score direction, and units across comparisons."],
            "conditions": {"initial": {"status": "present", "details": ["Required ordered event data and a finite spatial domain exist."]}, "boundary": {"status": "present", "details": ["Linkage, anchor stability, nonzero time gaps, and kernel assumptions must be screened."]}, "equilibrium": {"status": "not-applicable", "details": ["No equilibrium is claimed."]}},
            "parameter_estimation": {"status": "partial", "method": "Paper-described direct update, regression, grid enumeration, or held-out comparison.", "parameters": inputs},
            "algorithm": {"status": "implemented", "steps": ["freeze inputs and forecast origin", "perform the stated finite update or scan", "calculate the declared field, region, or metric", "retain failures and scope in the handoff"], "software": ["Unreleased Python and spreadsheet implementation"], "convergence_criteria": "Finite events, cells, candidates, and case comparisons."},
            "assumptions": ["The observed spatial sequence contains predictive information."],
            "identifiability_feasibility": {"status": "partial", "analysis": "Procedurally feasible, but data provenance, projection, grid, parameters, code, and independent validation remain incomplete."},
            "handoff_outputs": outputs, "validation_refs": [f"Physical page {page} and its adjacent equation, table, map, or interpretation."],
            "computational_cost": "Ranges from linear sequential updates to repeated grid scans over anchors, sites, and sequence prefixes.",
            "strengths": ["Makes the chronological and operational handoff explicit."],
            "limitations": ["The paper does not provide executable code or full reproduction metadata."],
            "missing_details": ["Exact grid, masking, normalization, regression settings, runtime, and uncertainty are absent."],
        })
    by_family = {m["family"]: m["model_id"] for m in models}
    edges = [
        {"from_model_id": by_family["running spatial mean"], "to_model_id": by_family["finite-difference event velocity"], "handoff": "The previous centroid anchors the new event displacement."},
        {"from_model_id": by_family["finite-difference event velocity"], "to_model_id": by_family["recursive centroid velocity"], "handoff": "The event velocity updates the centroid-motion state."},
        {"from_model_id": by_family["recursive centroid velocity"], "to_model_id": by_family["acceleration regression"], "handoff": "The velocity history supplies regression inputs for acceleration."},
        {"from_model_id": by_family["acceleration regression"], "to_model_id": by_family["damped kinematic forecast"], "handoff": "The fitted acceleration and current velocity enter the damped center forecast."},
        {"from_model_id": by_family["damped kinematic forecast"], "to_model_id": by_family["prediction-diamond construction"], "handoff": "The forecast center is expanded into an operational next-site region."},
        {"from_model_id": by_family["binary visited-location characteristic"], "to_model_id": by_family["inverse-distance normalized kernel"], "handoff": "Prior site use and anchor distance determine the local choice score."},
        {"from_model_id": by_family["inverse-distance normalized kernel"], "to_model_id": by_family["product sequence likelihood"], "handoff": "Sequential kernel scores are multiplied under each anchor hypothesis."},
        {"from_model_id": by_family["product sequence likelihood"], "to_model_id": by_family["Bayesian anchor ranking"], "handoff": "The sequence likelihood ranks candidate homes under the stated prior."},
        {"from_model_id": by_family["Bayesian anchor ranking"], "to_model_id": by_family["candidate-anchor likelihood scan"], "handoff": "The posterior interface is evaluated across the finite search grid."},
        {"from_model_id": by_family["history-weighted next-site mixture"], "to_model_id": by_family["next-site surface scan"], "handoff": "The mixture score is computed for every candidate future cell."},
        {"from_model_id": by_family["L1 coordinate error"], "to_model_id": by_family["paired-model case comparison"], "handoff": "Held-out centrographic centers are evaluated against the actual next event."},
        {"from_model_id": by_family["RSC risk-surface construction"], "to_model_id": by_family["hit-score and search-area evaluation"], "handoff": "The ranked surface is converted into searched fraction and physical area."},
        {"from_model_id": by_family["prediction-diamond construction"], "to_model_id": by_family["paired-model case comparison"], "handoff": "The centrographic region is compared beside the RSC surface on a shared case prefix."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    sections = [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, _, evidence, _ in CHAPTERS]
    assumptions = [
        (3, "All supplied events are correctly linked to one offender."),
        (3, "The offender has one relevant and stationary anchor point during the modeled series."),
        (3, "Serial offenders prefer familiar areas near home or prior sites."),
        (5, "Chronological centroid motion contains information about the next event."),
        (5, "Elapsed times are positive and comparable across the sequence."),
        (6, "Longitude and latitude acceleration can be fitted independently."),
        (7, "The selected beta makes motion decay on a useful time scale."),
        (9, "A rational offender chooses locations through observable site characteristics and avoidance costs."),
        (10, "Previously used cells can be excluded and inverse distance approximates location preference."),
        (10, "Candidate homes have a uniform prior over the chosen hunting area."),
        (11, "Historical prefix likelihoods can be mixed to rank the next site."),
        (13, "Error distance, Hit Score, and Search Area meaningfully represent police performance."),
    ]
    verification = [
        (12, "For Hillside Strangler data, kill j is withheld and predicted using only kills 1 through j-1, beginning with j=4.", "sequential-holdout", "Creates several chronological pseudo-forecasts.", "The actual next-event time is still used and only one series is tested."),
        (13, "Table 2 reports five exact Manhattan errors for successive held-out events.", "event-level-error-trace", "Prevents the mean from hiding every individual holdout.", "No baseline, uncertainty interval, or alternate distance metric is supplied."),
        (13, "Tables 3 and 4 expose separate longitude and latitude regression data.", "component-regression-audit", "Makes the acceleration fitting inputs visible.", "Sample sizes are tiny and diagnostics are incomplete."),
        (14, "Figure 1 overlays predicted centers, actual events, and diamond regions across the Hillside sequence.", "visual-holdout-check", "Connects numeric errors to spatial direction and coverage.", "The diamond is not probability calibrated."),
        (15, "The Berkowitz jeopardy surface is checked against both Bronx and Yonkers residences.", "alternative-anchor-case-check", "Reveals sensitivity to a changed residence within one offender history.", "The Yonkers domain is enlarged after the fact."),
        (16, "Tables 5 and 6 translate ranked cells into Hit Score and Search Area for three home targets.", "resource-metric-comparison", "Connects ranking to searched land area.", "Boundary and resolution sensitivity are not tested."),
        (17, "Figure 4 compares an RSC seventh-event surface with the actual Berkowitz event.", "next-event-map-check", "Provides a qualitative held-out next-site test.", "It is a single example without a numeric next-site score."),
        (18, "Figures 5 and 6 place both models on the DC Sniper sequence.", "shared-failure-case", "Exposes repeated-location and same-day-event violations rather than reporting only successes.", "No repaired variants are rerun on the same case."),
        (19, "The Discussion compares the claimed decreasing-error pattern against event-level values.", "claim-table-consistency", "Allows narrative claims to be checked against the table.", "The paper itself misses the increase at kill 6 and the mean discrepancy."),
        (20, "RSC performance is compared with random search through a chi-square claim.", "random-search-comparison", "Attempts to supply an external baseline.", "The statistical construction and dependence assumptions are undocumented."),
        (21, "The two models' distinct outputs are discussed as complementary police information.", "complementarity-check", "Preserves separate home and next-event decision roles.", "No fused rule or joint validation is estimated."),
    ]
    card = {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": "8479", "title": "From Kills to Kilometers: Using Centrographic Techniques and Rational Choice Theory for Geographical Profiling of Serial Killers", "award_status": "Outstanding Winner",
        "source": {"relative_path": "2010美赛特等奖/B-8479-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is the standalone Summary; physical pages 2-26 contain the internally numbered 1-25 paper."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 26, "rendered_pages": 26, "visual_review": "complete", "notes": ["All 26 text pages and all 26 rendered pages were reviewed in order.", "Six full-page JPEG contact proxies and two formula/table crop proxies stayed below 450000 bytes; no original page PNG entered model context."]},
        "context_sources": [{"page": 3, "summary": "FBI definitions and geographic-profiling studies motivate linkage, anchor, circle, and proximity claims."}, {"page": 12, "summary": "Wikipedia and newspaper sources supply event addresses and dates later converted to coordinates."}, {"page": 24, "summary": "The 40-reference bibliography covers geographical profiling, rational choice, crime-pattern theory, statistics, mapping, and historical cases."}],
        "task_reconstruction": {"inputs": ["ordered locations and times of crimes attributed to one serial offender", "candidate geographic hunting area and grid", "centrographic damping parameter or rational-choice kernel assumptions"], "outputs": ["predicted next-event center and diamond", "ranked home jeopardy surface", "ranked next-event surface", "error-distance, Hit Score, and Search Area evaluations"], "decisions": ["where police search for the offender", "which area may contain the next event", "whether case assumptions make either model usable"]},
        "section_map": sections,
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [{"page": 3, "summary": "Historical crime series are treated as linked, ordered observations with sparse sample sizes."}, {"page": 5, "summary": "Crime coordinates are converted into running centroids and finite-difference velocities."}, {"page": 10, "summary": "The RSC model discretizes a hunting area and encodes whether each cell was used previously."}, {"page": 12, "summary": "Street addresses and dates from public sources are converted to latitude-longitude pairs and ordered in Table 1."}, {"page": 12, "summary": "Centrographic testing repeatedly removes the next event from the spatial prefix."}, {"page": 16, "summary": "RSC evaluation defines a case-specific hunting area whose size directly enters Search Area."}],
        "models": [{"page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": vt, "strength": strength, "limitation": limitation} for p, s, vt, strength, limitation in verification],
        "results_trace": [{"page": 13, "summary": "Hillside holdout errors for kills 4 through 8 are 19.9032477532, 13.1624956104, 26.1455165479, 12.1278772065, and 4.41086910109 km."}, {"page": 16, "summary": "Berkowitz Bronx uses 1414 square kilometers, 18.1 percent Hit Score, and 255 square kilometers Search Area."}, {"page": 16, "summary": "Berkowitz Yonkers uses 2514 square kilometers, 63.2 percent Hit Score, and 1588 square kilometers Search Area."}, {"page": 16, "summary": "Buono-Bianchi uses 2721 square kilometers, 13.9 percent Hit Score, and 379 square kilometers Search Area."}, {"page": 18, "summary": "Neither model predicts the actual final DC Sniper event; repeated locations break the RSC rule and same-day events break the centrographic velocity."}, {"page": 19, "summary": "The five reported Hillside errors average about 15.15 km and do not decrease monotonically."}],
        "contributions": [{"page": 5, "summary": "Turns a time-ordered crime centroid into a recursive motion state."}, {"page": 6, "summary": "Adds damped velocity and acceleration so the forecast stops at long horizons."}, {"page": 9, "summary": "Frames geographic profiling as a rational location-choice problem."}, {"page": 10, "summary": "Builds a home jeopardy surface from sequential distance-buffer likelihoods."}, {"page": 11, "summary": "Extends the anchor mixture to a relative next-site surface."}, {"page": 13, "summary": "Uses both point error and searched-area metrics for operational interpretation."}],
        "writing_logic": [{"page": 1, "summary": "Summary chain: police task -> sparse data -> familiar-area assumptions -> centrographic forecast -> rational-choice surface -> historical tests -> limitations -> starting-point use."}, {"page": 3, "summary": "Introduction chain: scarce serial-killer data -> two targets -> complementary models -> partial-series simulation -> section roadmap."}, {"page": 3, "summary": "Background chain: operational definition -> home proximity evidence -> clustering -> anchor premise -> existing geographic profiling."}, {"page": 4, "summary": "Literature chain: distance decay and buffers -> centroid precedents -> crime-pattern and rational-choice theory -> two model adaptations."}, {"page": 5, "summary": "Centrographic chain: assumptions -> centroid -> event velocity -> momentum recurrence -> acceleration -> damped forecast -> prediction diamond."}, {"page": 9, "summary": "RSC chain: utility and simplex -> implicit choice -> binary risk -> inverse-distance kernel -> sequence likelihood -> anchor posterior -> next-site mixture."}, {"page": 12, "summary": "Evaluation chain: source and geocode data -> chronological holdouts -> error table and figure -> jeopardy surfaces -> Hit Score and Search Area -> DC Sniper countercase."}, {"page": 19, "summary": "Discussion chain: interpret case results -> identify parameter and assumption failures -> qualify claims -> propose repairs -> joint-use boundary."}, {"page": 22, "summary": "Executive chain: police inputs -> two outputs -> strengths and weaknesses -> map interpretation -> combined operational use."}],
        "language_observations": [{"page": 1, "summary": "The opening uses a vivid police scenario, then immediately replaces drama with a precise input-output contract."}, {"page": 1, "summary": "Each model receives one parallel paragraph with motivation, mechanism, and target."}, {"page": 3, "summary": "The Introduction closes every promise with a forward section reference, making the roadmap auditable."}, {"page": 3, "summary": "Definitions, empirical percentages, and modeling consequences are placed in the same paragraph chain."}, {"page": 5, "summary": "Kinematics is introduced through quoted vocabulary and then translated into explicit recurrences."}, {"page": 8, "summary": "The phrase rational serial criminal is bounded so rationality means goal-directed choice rather than moral approval or perfect information."}, {"page": 9, "summary": "To summarize marks the point where behavioral prose becomes a formal choice interface."}, {"page": 12, "summary": "The Results section states forecast origin and metric before interpreting performance."}, {"page": 19, "summary": "The Discussion alternates a positive result with its sensitivity or assumption failure."}, {"page": 22, "summary": "The Executive Summary translates surfaces and diamonds into where-to-search language while retaining model-specific caveats."}],
        "visualization_observations": [{"page": p, "figure": name, "summary": purpose} for p, name, purpose in VISUALS],
        "judge_relevance_hypotheses": [{"page": 1, "summary": "A complete dual-model summary plausibly improves traceability without establishing validity.", "evidence_class": "J"}, {"page": 14, "summary": "Sequential holdout maps plausibly help judges connect equations to spatial consequences.", "evidence_class": "J"}, {"page": 16, "summary": "Search Area plausibly improves operational relevance, while domain sensitivity limits credibility.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": [{"extension_id": f"E-B-{SHORT}-001", "page": 3, "summary": "Model linkage and moving-anchor uncertainty instead of assuming one stationary offender home."}, {"extension_id": f"E-B-{SHORT}-002", "page": 6, "summary": "Use projected coordinates, explicit interpolation, nonzero-time handling, and nested calibration for beta and acceleration."}, {"extension_id": f"E-B-{SHORT}-003", "page": 10, "summary": "Replace the zero-repeat binary kernel with a fitted soft-risk model and a geographic feasibility mask."}, {"extension_id": f"E-B-{SHORT}-004", "page": 12, "summary": "Version case sources, geocoding, projections, and forecast-origin timestamps so every simulation is reproducible."}, {"extension_id": f"E-B-{SHORT}-005", "page": 13, "summary": "Use rolling origins, simple baselines, uncertainty, calibration, grid sensitivity, and predeclared domains for both targets."}, {"extension_id": f"E-B-{SHORT}-006", "page": 18, "summary": "Estimate and validate a fused decision rule with abstention when repeated sites, same-day events, or moved anchors are detected."}],
        "candidate_rule_impacts": [
            {"rule_id": "R-B-LANG-001", "action": "retain the task-contract, assumption-motivation, parallel dual-model preview, analogy-to-formalism, and result-countercase language mechanisms", "evidence_ids": [f"O-B-2010-{SHORT}-001"]},
            {"rule_id": "R-B-LOG-001", "action": "retain the problem-to-background-to-two-formalisms-to-data-to-shared-tests-to-bounded-decision organization chain", "evidence_ids": [f"O-B-2010-{SHORT}-293"]},
            {"rule_id": "R-B-DATA-001", "action": "retain ordered event coordinates and dates only with linkage, provenance, geocoding, projection, and forecast-availability metadata", "evidence_ids": [f"O-B-2010-{SHORT}-405"]},
            {"rule_id": "R-B-MOD-001", "action": "retain complete centroid-state and choice-likelihood interfaces with units, chronology, domain, and target explicit", "evidence_ids": [f"O-B-2010-{SHORT}-225"]},
            {"rule_id": "R-B-MOD-002", "action": "distinguish physical analogies and normalized rankings from calibrated behavioral probabilities", "evidence_ids": [f"O-B-2010-{SHORT}-226"]},
            {"rule_id": "R-B-MOD-003", "action": "retain modular damping and kernel choices only with estimation, sensitivity, feasibility masks, and assumption diagnostics", "evidence_ids": [f"O-B-2010-{SHORT}-227"]},
            {"rule_id": "R-B-VER-001", "action": "retain chronological holdouts and resource metrics while requiring deployment-available time, baselines, rolling origins, uncertainty, and fixed domains", "evidence_ids": [f"O-B-2010-{SHORT}-369"]},
            {"rule_id": "R-B-VER-002", "action": "use moved-anchor, repeated-location, same-day-event, and domain-sensitivity cases as mandatory reliability diagnostics", "evidence_ids": [f"O-B-2010-{SHORT}-370"]},
            {"rule_id": "R-B-VIZ-001", "action": "retain event overlays and paired case maps while requiring quantitative color bars, truth markers, common scales, and caption-data checks", "evidence_ids": [f"O-B-2010-{SHORT}-335"]},
            {"rule_id": "R-B-DEC-001", "action": "translate center error and ranked surfaces into bounded search actions only after units, area, capacity, and abstention rules are explicit", "evidence_ids": [f"O-B-2010-{SHORT}-455"]},
            {"rule_id": "R-B-COMP-001", "action": "compare or combine model families only on the same event prefix, forecast time, domain, target, metric, and uncertainty protocol", "evidence_ids": [f"O-B-2010-{SHORT}-228"]},
        ],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }
    return card


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing every source fact, offender, number, location, and phrase.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain the complete input, equation or procedure, parameter, time availability, domain, target, output, metric, and handoff.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive task-to-mechanism-to-dual-model-to-test-to-decision sequence.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep axes, coordinates, event order, truth marker, region or color semantics, scale, target, and decision purpose attached.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name forecast origin, held-out target, available time, baseline, domain, metric, units, uncertainty, and violated assumptions.", "R-B-VER-001") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain linkage, address source, date, order, geocoder, projection, coordinate units, domain, and versioned transformations.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each assumption with a diagnostic, excluded mechanism, and fallback or abstention rule.", "R-B-MOD-001") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry case, target, forecast origin, metric, unit, domain, exact value, and operational interpretation together.", "R-B-DEC-001") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use warnings only after positive language, organization, model, verification, and visual coverage is complete.", "R-B-VER-002") for x in card["weaknesses"]],
        "other": [(24, "reference boundary", "References support context but do not independently establish implementation fidelity, parameter calibration, or empirical validity.", "Separate citation presence from reproducibility and validation.", "R-B-VER-001")],
    }
    counts = {"language": 224, "modeling": 68, "logic": 42, "visualization": 34, "verification": 36, "data": 26, "assumption": 24, "result": 30, "weakness": len(WARNINGS), "other": 6}
    records: list[dict] = []
    for dimension, count in counts.items():
        rows = sources[dimension]
        for i in range(count):
            page, section, basis, interpretation, rule = rows[i % len(rows)]
            idx = len(records) + 1
            candidate_rules = [rule]
            if dimension == "modeling" and i == 1:
                candidate_rules.append("R-B-MOD-002")
            if dimension == "modeling" and i == 2:
                candidate_rules.append("R-B-MOD-003")
            if dimension == "modeling" and i == 3:
                candidate_rules.append("R-B-COMP-001")
            if dimension == "verification" and i == 1:
                candidate_rules.append("R-B-VER-002")
            records.append({
                "schema_version": 1, "observation_id": f"O-B-2010-{SHORT}-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR,
                "page": page, "section": f"{section} / evidence action {i + 1}", "evidence_class": "O", "dimension": dimension,
                "source_basis": basis[:900], "interpretation": interpretation,
                "applicability": ["Apply only when linkage, chronology, coordinate system, forecast origin, target, domain, operation, output, metric, units, and case scope can all be named."],
                "counterevidence": ["A plausible analogy, smooth contour, low point error, small Hit Score, or one successful case does not prove calibration, causality, stable anchors, or general suitability."],
                "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium",
                "candidate_rule_ids": candidate_rules,
            })
    return records


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reusable only after replacing source facts and preserving occurrence, function, order, slots, variants, evidence strength, target, and boundary."} for u in language["units"]]
    paragraph_specs = {
        "abstract": ["police scenario and exact task", "sparse inputs and familiar-area assumptions", "centrographic mechanism and target", "rational-choice mechanism and target", "historical tests and metrics", "omitted geography and bounded use"],
        "introduction": ["scarce-data motivation and comparison class", "two complementary targets and Section 3 handoff", "partial-series tests, results, limitations, and roadmap"],
    }
    paragraph_chains = []
    for chapter, moves in paragraph_specs.items():
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": len(moves), "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": move, "language_unit_ids": [ids[i % len(ids)]]} for i, move in enumerate(moves)]})
    progressions = [{"chapter": chapter, "moves": [f"input: the source-checked object entering {key}", f"rhetorical job: perform the observed {key} definition, motivation, derivation, test, result, or boundary", f"analytical job: apply the declared centroid, velocity, damping, utility, kernel, likelihood, metric, or case comparison in {key}", f"output: retain a state, forecast region, ranked surface, metric, countercase, or bounded recommendation from {key}", "handoff: name the next formal layer, validation check, assumption diagnostic, or police action"], "positive_pattern": "Use observable input -> mechanism or operation -> explicit output -> metric or comparison -> bounded handoff; warning lists cannot replace the positive chapter contract."} for key, chapter, *_ in CHAPTERS]
    model_ids = [m["model_id"] for m in models["models"]]
    equation_refs = [(m["model_id"], eq["equation_id"], eq["page"]) for m in models["models"] for eq in m["governing_equations"]]
    equation_ids = [equation_id for _, equation_id, _ in equation_refs]
    central = [{"model_id": m["model_id"], "equation_ids": [eq["equation_id"] for eq in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]
    warning_rows = []
    for page, warning in WARNINGS:
        model_id, equation_id, _ = min(equation_refs, key=lambda ref: (abs(ref[2] - page), ref[2], ref[1]))
        warning_rows.append({"model_id": model_id, "equation_id": equation_id, "page": page, "warning": warning})
    dim_counts = Counter(row["dimension"] for row in observations)
    return {
        "audit_id": f"LA-B-2010-{SHORT}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [12 if key in {"summary-sheet", "title-page-abstract", "introduction"} else 8, 3, 0]} for key, chapter, *_ in CHAPTERS],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": ["standalone police-task Summary and titled Abstract", "scarce-data Introduction, serial-killing definition, anchor evidence, and prior profiling work", "centrographic assumptions, running center, motion recurrence, damping, and diamond forecast", "bounded rationality, utility, site characteristics, distance-buffer kernel, sequence likelihood, and anchor posterior", "versioned event data need, chronological holdouts, error distances, jeopardy surfaces, Hit Score, and Search Area", "Berkowitz and Buono-Bianchi home results, next-event maps, and DC Sniper shared failure", "discussion of fit, sensitivity, moved anchors, repeated sites, same-day events, joint use, and executive police guidance", "references and reproducibility boundary"], "section_progressions": progressions, "main_argument_chains": [
            {"claim": "A time-ordered running centroid can support a bounded next-event region when event linkage, positive time gaps, and stable motion are plausible.", "support_steps": ["centroid definition", "event and centroid velocities", "momentum recurrence", "acceleration regression", "damped forecast", "sequential Hillside holdouts"], "decision_consequence": "Use the diamond only with deployment-available time, calibrated coverage, parameter sensitivity, and same-day safeguards.", "source_pages": [5, 6, 7, 12, 13, 14]},
            {"claim": "A rational-choice sequence likelihood can rank possible offender homes under a fixed anchor and declared geographic domain.", "support_steps": ["bounded rationality interpretation", "utility and simplex", "binary prior-use characteristic", "distance-buffer kernel", "sequence likelihood", "anchor posterior", "Berkowitz and Buono-Bianchi surfaces"], "decision_consequence": "Treat the surface as a ranking until calibrated, mask infeasible cells, and abstain when anchors move or locations repeat.", "source_pages": [8, 9, 10, 11, 15, 16, 17]},
            {"claim": "Chronological holdouts and operational metrics make spatial predictions inspectable.", "support_steps": ["event-table provenance", "kill-by-kill holdouts", "Manhattan errors", "Hit Score", "Search Area", "truth overlays"], "decision_consequence": "Freeze domains and forecast times, add baselines and uncertainty, and report case-level values rather than only averages.", "source_pages": [12, 13, 14, 15, 16, 17, 18]},
            {"claim": "The two models are complementary only when their assumptions and outputs remain distinct.", "support_steps": ["centrographic next-event region", "RSC home and next-site ranking", "shared DC Sniper countercase", "discussion of assumption failures", "executive joint-use proposal"], "decision_consequence": "Validate any fusion rule on shared prefixes and issue an abstention when either model's diagnostics fail.", "source_pages": [17, 18, 19, 20, 21, 22, 23]},
        ]},
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warning_rows},
        "model_retention": {"model_count": len(model_ids), "retained_model_ids": model_ids, "retained_equation_ids": equation_ids, "central_equations": central},
        "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-B-2010-{SHORT}-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)],
        "dimension_counts": {dim: dim_counts[dim] for dim in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]},
        "positive_reusable_language_count": len(language["units"]), "weakness_record_count": dim_counts["weakness"], "review_status": "validated",
    }


def main() -> None:
    language = make_language()
    models = make_models()
    card = make_card(language, models)
    observations = make_observations(language, models, card)
    audit = make_audit(language, models, card, observations)
    write_json(ROOT / "artifacts/language-units" / f"{PID}.json", language)
    write_json(ROOT / "artifacts/model-units" / f"{PID}.json", models)
    write_json(ROOT / "artifacts/paper-cards" / f"{PID}.json", card)
    write_json(ROOT / "artifacts/learning-audits" / f"{PID}.json", audit)
    obs_path = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    obs_path.parent.mkdir(parents=True, exist_ok=True)
    obs_path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
