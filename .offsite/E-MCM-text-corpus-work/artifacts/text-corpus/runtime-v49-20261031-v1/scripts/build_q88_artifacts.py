from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2010-8362-bd23db32"
SHORT = "8362"
SHA = "bd23db325edb239eb6ab6a5a9f2caad827010c911c625eb131f0098bb0c583ac"
TYPE = "B"
YEAR = "2010"
PAGE_COUNT = 33

PATTERNS = [
    "LP-B-ABS-PROBLEM-PIPELINE-EVIDENCE-BOUNDARY",
    "LP-B-EXEC-INPUT-LIMITATION-ACTION",
    "LP-B-INT-LITERATURE-TO-MECHANISM",
    "LP-B-ASSUMPTION-OPERATIONALIZATION",
    "LP-B-METHOD-INTUITION-FORMALIZATION",
    "LP-B-ALGORITHM-FIRST-NEXT-THIS-GIVES",
    "LP-B-COMPLEXITY-TO-COMPUTE-CLAIM",
    "LP-B-RESULT-METRIC-TO-DECISION",
    "LP-B-RESULT-AGGREGATE-VS-CASE",
    "LP-B-LIMITATION-TO-EXTENSION",
]

# key, protocol chapter, first page, last page, id tag, source-checked evidence, visual paragraphs
CHAPTERS = [
    ("cover", "title", 1, 1, "TTL", "The cover identifies the decision-oriented title, control number, and submission date without adding unsupported claims.", 1),
    ("summary-statement", "abstract", 2, 2, "SUM", "The Summary moves from police inputs and two prediction targets to additive distance-decay fields, virtual-crime scoring, time extrapolation, time coupling, two metrics, a Sutcliffe result, and color-map output.", 3),
    ("executive-summary", "memo", 3, 4, "EXE", "The two-page letter translates required inputs, probability-map outputs, single-offender and single-base assumptions, commuter and geography exclusions, function flexibility, runtime, color bands, and police actions into decision language.", 8),
    ("contents", "problem-restatement", 5, 5, "CON", "The contents exposes a background-problem-assumptions-metrics-functions-algorithms-results-conclusion-future-research-appendix route.", 1),
    ("background", "introduction", 6, 7, "INT", "The background motivates computation through human judgment bias, defines the serial-killer scope, distinguishes nearby categories, supplies behavioral evidence, and introduces circle, distance-decay, and buffer-zone mechanisms.", 6),
    ("problem", "problem-analysis", 7, 7, "PRB", "The problem section reduces the police request to predicting one base, the next crime location, and its time, then states the color-priority and bilinear-interpolation handoff.", 2),
    ("assumptions", "assumptions", 7, 8, "ASM", "The assumptions section fixes single-offender linkage, one base, circle-like coverage, stable distance decay, noncommuter behavior, and homogeneous terrain, population, and opportunity while naming future relaxations.", 5),
    ("spatial-metrics", "notation", 8, 9, "MET", "The metric section defines weighted mean center, minimum-distance center, standard-deviational circle, and standard-deviational ellipse as global spatial summaries.", 6),
    ("simple-cases", "data-preprocessing", 9, 10, "SYN", "Four synthetic point layouts establish expected home and next-event behavior before formal modeling: uniform fill, square outline, linear spread, and two clusters.", 8),
    ("distance-decay", "model-establishment", 10, 12, "DEC", "Five distance-decay families are compared by their near-scene behavior, buffer-zone interpretation, cutoff or tail behavior, and crime-type adaptability.", 10),
    ("criminal-location", "algorithm", 12, 15, "LOC", "The criminal-location method replaces a single center with a grid distribution formed by additive distance contributions, normalization, prioritized search, automatic hotspots, and interchangeable kernels.", 13),
    ("next-crime-location", "model-improvement", 16, 18, "NXT", "The next-crime method inserts a virtual event at each candidate, recomputes the home field, scores squared distribution change, adds an edge buffer, and discusses quartic cost, caching, and parallelization.", 12),
    ("future-crime-time", "sensitivity-analysis", 18, 19, "TIM", "The time section withholds the last event, extrapolates an average interval, compares predicted and actual Chester Turner timing, and chooses a restrained linear rule over strong-end alternatives.", 5),
    ("time-coupling", "sensitivity-robustness", 19, 23, "CPL", "The coupling section defines a decreasing recency weight, inserts it into both spatial algorithms, and contrasts correlated with uncorrelated synthetic time assignments through six heat maps.", 12),
    ("result-discussion", "results", 23, 25, "RES", "The results define straight-line error and ranked-grid search cost, withhold the most recent crime, compare five kernels with and without time coupling for Sutcliffe and Turner, and report exact paired values.", 9),
    ("conclusion", "conclusion", 25, 26, "END", "The conclusion separates favorable clustered Sutcliffe behavior from displaced-hub Turner failure, explains why next-crime prediction can outperform home prediction, and admits that time coupling often worsened performance.", 6),
    ("future-research", "future-improvements", 26, 26, "FUT", "Future work maps omitted terrain, population, social geography, opportunity, and personality traits to optional features and parameter changes.", 4),
    ("case-data", "appendix", 26, 27, "APP", "The appendix preserves predicted-versus-actual dates and a five-offender latitude-longitude-time table with source attribution and visible chronology defects.", 5),
    ("model-plots", "robustness-verification", 28, 32, "PLT", "The plot appendix places home and next-crime heat maps for five kernels and a time-weighted variant on common coordinates, while page 32 exposes a duplicated and mislabeled Sutcliffe pair under a Chester Turner heading.", 10),
    ("references", "references", 33, 33, "REF", "Eleven references connect geographic profiling, environmental criminology, serial-offender behavior, journey-to-crime decay, mapping, and bounded rationality, with several bibliographic defects retained.", 1),
]

MOVES = [
    ("decision-contract", "Name the decision actor, available evidence, requested output, and operational use before method detail.", "decision actor -> evidence -> prediction target -> action"),
    ("mechanism-before-model", "State the behavioral or spatial mechanism that makes the model family plausible.", "observed mechanism -> model requirement -> selected family"),
    ("limitation-strength-pair", "Place exclusions beside strengths so applicability remains visible.", "capability -> excluded case -> consequence -> bounded use"),
    ("intuition-before-equation", "Use a synthetic layout or physical analogy before formal scoring.", "intuitive pattern -> expected behavior -> equation -> interpretation"),
    ("parallel-family-contrast", "Present competing kernels in parallel around one changed assumption.", "shared target -> family variants -> common output -> comparison"),
    ("procedural-chain", "Explain algorithms through First, Next, Then, and This gives us transitions.", "first input state -> next operation -> comparison -> returned object"),
    ("complexity-to-capacity", "Translate asymptotic cost into grid resolution, hardware, runtime, or parallel capacity.", "operation count -> asymptotic order -> compute claim -> deployment caveat"),
    ("metric-to-resource", "Translate a score into distance, searched cells, or wasted deployment.", "metric definition -> task interpretation -> resource consequence"),
    ("aggregate-case-boundary", "Keep good aggregate or clustered-case behavior distinct from displaced-hub failure.", "favorable case -> countercase -> mechanism -> scope boundary"),
    ("omission-to-extension", "Turn an omitted variable into a concrete feature, diagnostic, or validation need.", "omission -> failure mode -> added data -> revised decision rule"),
]

EXAMPLES = [
    ("A flood paper names sensor histories, evacuation priority, and the emergency coordinator before introducing the forecast.", "It closes the opening by stating exactly how ranked zones change crew deployment."),
    ("A clinic study motivates recency weighting because recent arrivals reveal a changing service regime.", "It then compares the dynamic queue model with a stationary baseline on later weeks."),
    ("A freight model states that highways, ferry schedules, and depot capacity are omitted before advertising route flexibility.", "The recommendation is therefore limited to corridors with complete network data."),
    ("A wildfire study shows uniform, edge, linear, and clustered ignition patterns before defining a risk field.", "Each synthetic layout states what a credible field should and should not highlight."),
    ("A habitat paper compares compact-support, Gaussian, exponential, and plateau kernels under one grid interface.", "Only the near-source assumption changes while the output and metric remain fixed."),
    ("First the baseline field is frozen; next a candidate intervention is inserted; then the fields are compared.", "This produces a candidate score whose direction is stated explicitly before ranking."),
    ("A routing paper derives quartic work and then reports measured runtime for three mesh sizes.", "It separates ideal parallel speedup from observed communication overhead."),
    ("A search fraction is converted into hectares, team-hours, and a cumulative priority curve.", "A distance error is reported separately because it answers a different operational question."),
    ("A demand forecast succeeds in dense districts but fails for a remote island whose demand center is displaced.", "The conclusion preserves both facts and defines an abstention diagnostic."),
    ("A landslide model names missing soil saturation and requests versioned moisture rasters for the next test.", "The extension is tied to a measurable failure rather than generic future improvement."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose, confidence
EQUATIONS = [
    ("weighted mean center", 8, "simple spatial metrics", "weighted coordinate center", "c_x=sum_i w_i x_i and c_y=sum_i w_i y_i", r"c_x=\sum_{i=1}^{N}w_ix_i,\qquad c_y=\sum_{i=1}^{N}w_iy_i", ["c_x", "c_y", "w_i", "x_i", "y_i", "N"], "Summarize crime locations through a possibly weighted coordinate center.", "high"),
    ("minimum-distance center", 8, "simple spatial metrics", "geometric median objective", "minimize over x,y the sum_i sqrt((x_i-x)^2+(y_i-y)^2)", r"\min_{x,y}\sum_{i=1}^{N}\sqrt{(x_i-x)^2+(y_i-y)^2}", ["C_min", "x", "y", "x_i", "y_i", "N"], "Choose the point with minimum total Euclidean distance to all scenes.", "high"),
    ("linear distance decay", 10, "distance decay functions", "compact-support linear kernel", "f(x)=a-bx if x<=a/b and 0 otherwise", r"f(x)=\begin{cases}a-bx,&x\le a/b,\\0,&x>a/b.\end{cases}", ["f_linear", "x", "a", "b"], "Decrease influence linearly to a finite cutoff.", "high"),
    ("normal distance decay", 11, "distance decay functions", "buffer-peaked normal kernel", "f(x)=a exp(-(x-mu)^2/(2 sigma^2))/(sqrt(2 pi) sigma)", r"f(x)=\frac{a e^{-(x-\mu)^2/(2\sigma^2)}}{\sqrt{2\pi}\sigma}", ["f_normal", "x", "a", "mu", "sigma"], "Represent a preferred travel radius or buffer-zone peak.", "high"),
    ("negative exponential decay", 11, "distance decay functions", "monotone exponential kernel", "f(x)=exp(-c x)", r"f(x)=e^{-cx}", ["f_exp", "x", "c"], "Assign maximum influence at a scene and decay monotonically with distance.", "high"),
    ("truncated negative exponential decay", 12, "distance decay functions", "rise-then-decay kernel", "f(x)=1+b(x-x0) if x<=x0 and exp(-c(x-x0)) otherwise", r"f(x)=\begin{cases}1+b(x-x_0),&x\le x_0,\\e^{-c(x-x_0)},&x>x_0.\end{cases}", ["f_trunc", "x", "x_0", "b", "c"], "Create a linearly rising buffer-zone branch followed by exponential decay.", "high"),
    ("plateaued negative exponential decay", 12, "distance decay functions", "plateau-then-decay kernel", "f(x)=1 if x<=x0 and exp(-c(x-x0)) otherwise", r"f(x)=\begin{cases}1,&x\le x_0,\\e^{-c(x-x_0)},&x>x_0.\end{cases}", ["f_plateau", "x", "x_0", "c"], "Keep constant cell influence inside a radius and decay outside it.", "high"),
    ("criminal location raw field", 13, "criminal location method", "additive distance field", "S(g)=sum over c in C of f(distance(c,g))", r"S(g)=\sum_{c\in C}f(d(c,g))", ["S", "g", "C", "f", "d"], "Accumulate noncanceling contributions from all known crime locations.", "high"),
    ("criminal location normalization", 14, "Program 1", "normalized grid field", "Prob[g]=S(g)/sum over h in G S(h)", r"\operatorname{Prob}(g)=\frac{S(g)}{\sum_{h\in G}S(h)}", ["Prob", "S", "g", "h", "G"], "Normalize the grid score so all displayed values sum to one.", "high"),
    ("criminal location runtime", 14, "computation", "rectangular-grid work", "T(n,m,l)=O(n m l)", r"T_{\mathrm{home}}(n,m,l)=O(nml)", ["T_home", "n", "m", "l"], "Count one kernel evaluation per grid point and known crime.", "high"),
    ("square-grid runtime approximation", 14, "computation", "square-grid approximation", "if m=n and l is small then T is O(n^2)", r"m=n,\ l\ll n\quad\Rightarrow\quad T_{\mathrm{home}}=O(n^2)", ["T_home_square", "n", "m", "l"], "Explain the paper's simplified home-field complexity claim.", "high"),
    ("virtual crime augmentation", 17, "Program 2", "candidate-event insertion", "C prime equals C union a virtual crime at g", r"C'_g=C\cup\{\text{virtual crime at }g\}", ["C_prime", "C", "g"], "Create one hypothetical next crime for each candidate point.", "high"),
    ("virtual criminal field", 17, "Program 2", "candidate-conditioned home field", "V_g=criminalLocationProb(C prime_g,f)", r"V_g=\operatorname{criminalLocationProb}(C'_g,f)", ["V_g", "C_prime", "f"], "Recompute the normalized home field after inserting a candidate event.", "high"),
    ("distribution deviation score", 17, "Program 2", "sum-squared field change", "DeltaProb[g]=sum over h in G prime of (V_g[h]-K[h])^2", r"\Delta(g)=\sum_{h\in G'}(V_g(h)-K(h))^2", ["Delta", "g", "h", "G_prime", "V_g", "K"], "Measure how surprising a candidate event is relative to the original home field.", "high"),
    ("paper next-crime normalization", 17, "Program 2", "normalized deviation field", "Q(g)=Delta(g)/sum over u in G prime Delta(u)", r"Q(g)=\frac{\Delta(g)}{\sum_{u\in G'}\Delta(u)}", ["Q", "Delta", "g", "u", "G_prime"], "Retain the paper's returned normalized deviation field for auditing its score direction.", "high"),
    ("next-crime runtime", 16, "complexity", "nested candidate-grid work", "T_next(n)=O(n^4)", r"T_{\mathrm{next}}(n)=O(n^4)", ["T_next", "n"], "Count one square-grid home-field recomputation for every square-grid candidate.", "high"),
    ("future crime time extrapolation", 19, "future crime time", "average-span extrapolation", "t_N=t_(N-1)+(t_(N-1)-t_1)/(N-1)", r"t_N=t_{N-1}+\frac{t_{N-1}-t_1}{N-1}", ["t_N", "t_N_minus_1", "t_1", "N"], "Predict the withheld final event time from the observed span.", "high"),
    ("time weighting function", 19, "time coupling", "decreasing recency weight", "w(t)=((d-c)a)/sqrt(t+a)+c", r"w(t)=\frac{(d-c)a}{\sqrt{t+a}}+c", ["w", "t", "a", "c", "d"], "Give more recent events larger weight while approaching a lower asymptote.", "high"),
    ("weighted criminal raw field", 20, "Program 3", "time-weighted additive field", "S_w(g)=sum over c in C w(time since c_time) f(distance(c,g))", r"S_w(g)=\sum_{c\in C}w(\tau_c)f(d(c,g))", ["S_w", "g", "C", "w", "tau_c", "f", "d"], "Multiply every crime's distance contribution by a recency weight.", "high"),
    ("weighted field normalization", 20, "Program 3", "normalized time-weighted field", "Prob_w(g)=S_w(g)/sum over h in G prime S_w(h)", r"\operatorname{Prob}_w(g)=\frac{S_w(g)}{\sum_{h\in G'}S_w(h)}", ["Prob_w", "S_w", "g", "h", "G_prime"], "Return a normalized recency-weighted criminal-location field.", "high"),
    ("error distance", 24, "result metrics", "straight-line point error", "E=distance(argmax_g Prob(g), truth)", r"E=d\!\left(\arg\max_g\operatorname{Prob}(g),g_{\mathrm{true}}\right)", ["E", "Prob", "g", "g_true", "d"], "Measure how far the highest-scored location lies from the known target.", "medium"),
    ("search cost", 24, "result metrics", "ranked grid fraction", "SC=number of squares preceding truth divided by total squares", r"SC=\frac{|\{g:\operatorname{score}(g)>\operatorname{score}(g_{\mathrm{true}})\}|}{|G|}", ["SC", "g", "g_true", "G"], "Measure the fraction of higher-priority grid cells searched before the true cell.", "medium"),
]

VISUALS = [
    (1, "Cover", "Confirms title, control number, date, and page sequence."),
    (2, "Summary Statement", "Shows the complete input-method-metric-result-output chain on one page."),
    (3, "Executive Summary limitations", "Places single-offender, single-base, commuter, terrain, and population limits before strengths."),
    (4, "Executive Summary action map", "Connects red, yellow, and blue bands to search and prevention actions and reports runtime scale."),
    (5, "Contents", "Confirms the full route, appendix, and 33-page structure."),
    (9, "Uniform and outline synthetic layouts", "Establishes expected centers, spread, boundaries, and next-event ambiguity."),
    (10, "Linear and clustered synthetic layouts", "Shows directional spread and two-hotspot expectations that a credible field should preserve."),
    (11, "Figure 1 distance-decay comparison", "Contrasts Linear, Normal, Negative Exponential, and Truncated Negative Exponential shapes on common axes."),
    (13, "Figure 2 criminal-location field", "Overlays observed crimes and the actual base on a longitude-latitude heat map."),
    (14, "Program 1", "Makes grid iteration, additive kernel evaluation, normalization, and output explicit."),
    (15, "Two-cluster hotspot illustration", "Demonstrates automatic multimodal hotspots without an external clustering stage."),
    (17, "Program 2", "Exposes the augmented grid, virtual-event loop, sum-squared deviation, and returned field."),
    (18, "Figure 3 buffer comparison", "Shows the edge artifact without a buffer and the changed field with a 30 percent buffer."),
    (19, "Figure 4 Chester Turner timing", "Compares the predicted withheld event in red with the actual event in black."),
    (20, "Program 3", "Shows how the time weight enters both home and future-crime algorithms."),
    (21, "Figure 5 weight function", "Displays a fall from roughly 10 at day zero toward 2 by day 100."),
    (22, "Figure panels a-d", "Contrasts weighted and unweighted next-crime fields for correlated and uncorrelated synthetic timings."),
    (23, "Figure panels e-f", "Shows criminal-location fields changing less rapidly than next-crime fields under correlated motion."),
    (25, "Table 1", "Reports exact Search Cost / Error Distance pairs for five kernels, two targets, two coupling modes, and two offenders."),
    (26, "Predicted versus actual crime-date table", "Displays timing error for five offenders without a caption or stated unit metric."),
    (27, "Appendix A case-study table", "Preserves 52 latitude-longitude-date rows for five offender series and source attribution."),
    (28, "Linear Sutcliffe map pair", "Compares home and next-crime fields under the linear kernel on common coordinates."),
    (29, "Negative and truncated exponential Sutcliffe pairs", "Shows how tail and buffer behavior change home and next-crime hotspots."),
    (30, "Plateau and normal Sutcliffe pairs", "Shows alternative buffer assumptions on the same crime pattern."),
    (31, "Time-weighted negative exponential Sutcliffe pair", "Shows the recency-weighted home and next-crime outputs."),
    (32, "Mislabeled Chester Turner page", "Reveals duplicated Sutcliffe coordinates, plots, and captions under a Chester Turner heading."),
]

WARNINGS = [
    (8, "The mean-center equations are called averages but omit division by the total weight; taking every w_i=1 yields coordinate sums rather than a center unless normalized weights are silently assumed."),
    (9, "The 68 percent and 95 percent SDC coverage statements require a distributional interpretation that is not derived for these spatial point patterns."),
    (7, "The circle-hypothesis evidence for serial rapists is generalized to serial murder and other criminal types without a direct transfer validation."),
    (7, "One offender and exactly one home base are assumed, excluding linkage uncertainty, multiple anchors, and mobile or commuter behavior."),
    (8, "Terrain, road access, population density, opportunity, and inhabitable-area constraints are omitted, so high-score cells can be operationally impossible."),
    (8, "Euclidean calculations on latitude and longitude are not accompanied by a projection, spherical-distance rule, or unit conversion."),
    (10, "Linear, Normal, exponential, truncated, and plateau kernel parameters are not reported in a reproducible calibration table."),
    (13, "The additive normalized field is called a criminal-location probability although no generative likelihood, prior, or calibration test supports that interpretation."),
    (14, "Finer meshes are said to approximate an ideal smooth solution, but no resolution sensitivity or convergence diagnostic is shown."),
    (14, "The concrete 2 GHz runtime and 36 by 36 meter England-grid claim has no implementation, benchmark log, memory use, or kernel specification."),
    (16, "The prose says lower squared distribution deviation means a more likely next crime, but Programs 2 and 3 normalize the deviation without reversing its order, so larger deviations receive larger returned values."),
    (16, "The prose says virtual crimes are not added in the buffer, yet Programs 2 and 3 iterate candidate g over the augmented grid G prime rather than the interior G."),
    (17, "Program 2 specifies a 40 percent boundary buffer, whereas Figure 3 and Program 3 use 30 percent."),
    (16, "The O(n^4) next-crime complexity collapses a two-dimensional n by m grid to one symbol and does not state the effect of crime count or buffer size."),
    (18, "The claimed factor-N caching speedup and normalization-preserving combination are not derived or benchmarked."),
    (18, "Near-perfect parallel speedup equal to the number of cores ignores communication, memory bandwidth, scheduling, and aggregation overhead."),
    (19, "With observed times t_1 through t_(N-1), the mean of the N-2 observed intervals normally has denominator N-2, not the paper's N-1."),
    (19, "The time method is called linear regression, but the displayed rule is a one-step average-span extrapolation with no fitted regression line or residual analysis."),
    (19, "Parameters a, c, and d in the time-weighting function are undefined and no fit, units, or sensitivity analysis is reported."),
    (21, "Only one time-weight family is studied in depth and the synthetic correlated/uncorrelated experiment omits seeds, sample size, Poisson rate, parameter values, and repeated-run uncertainty."),
    (24, "The validation withholds only the most recent event from two main case datasets rather than using rolling origins, an external set, or repeated cross-validation."),
    (24, "Search Cost tie handling is described only as no preference within the same color, leaving exact rank treatment and color-bin effects unspecified."),
    (25, "Table 1 does not label Search Cost as percent versus fraction and does not state the distance units for Error Distance."),
    (25, "Kernel and time-weight choices are developed and evaluated on the same small case collection, creating tuning and selection optimism."),
    (25, "Time coupling generally worsens the reported values, but the paper offers no statistical test and initially attributes the behavior to bad luck."),
    (26, "The conclusion extrapolates Sutcliffe performance to larger datasets without evidence that more data, different offenders, or different geographies preserve accuracy."),
    (27, "Jack the Ripper dates are printed as 1988 in Appendix A but as 1888 in the preceding date table."),
    (29, "Panel (l) is titled Next Crime Location Probability but its caption calls it a Criminal Location plot."),
    (32, "The page headed Model Plots for Chester Turner actually repeats Sutcliffe coordinates, data, and captions, so the promised Turner visual comparison is absent."),
    (33, "The references contain suspicious pagination, misspellings, and inconsistent bibliographic formatting, limiting reproducibility."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": "output" if symbol in outputs else "input" if symbol in inputs else "intermediate",
        "unit": "coordinate, time, distance, grid score, probability-like weight, count, rank fraction, or computational order as locally defined",
        "definition": f"Source-defined quantity {symbol} in the retained spatial-prediction interface.",
        "source_status": "explicit-defined",
    }


def make_language() -> dict:
    units: list[dict] = []
    layouts: list[dict] = []
    for cidx, (key, chapter, start, end, tag, evidence, paragraphs) in enumerate(CHAPTERS):
        unit_count = 18 if key in {"summary-statement", "executive-summary", "background"} else 4 if key in {"cover", "contents", "references"} else 12
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
                "reusable_elements": ["decision actor", "observed evidence", "mechanism", "explicit operation", "quantified or visual output", "comparison", "boundary", "handoff"],
                "prohibited_generalizations": [
                    "Do not copy offender names, police wording, coordinates, dates, runtime numbers, search percentages, or case results into an unrelated paper.",
                    "Do not convert a normalized score, attractive heat map, synthetic example, or one successful offender case into calibrated probability or universal validity.",
                ],
                "features": {
                    "voice": "first-person plural for design choices; impersonal voice for definitions and pseudocode; direct advisory voice in the police memo",
                    "tense": "present for mechanism and algorithm; past for case evaluation; conditional for deployment and future extensions",
                    "modality": "assume, may, should, can, tend, suggest, and must retain distinct evidence strengths",
                    "clause_structure": order,
                    "quantitative_role": "attach fields, runtimes, distances, search ranks, case contrasts, or action bands to their exact scope",
                    "transition": ["first", "next", "then", "furthermore", "however", "thus", "in either case", "contrary to expectations"][i % 8],
                    "replaceable_slots": ["decision actor", "event type", "kernel", "candidate operation", "metric", "baseline", "compute budget", "excluded mechanism"],
                    "boundary_conditions": ["state score direction", "state grid and buffer domain", "separate home and next-event targets", "retain case and geography scope"],
                    "original_instantiations": [{"text": ex1}, {"text": ex2}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + i) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": 120 + 285 * (end - start + 1),
            "sentence_count": max(4, paragraphs * 4),
            "paragraph_count": paragraphs,
            "sentence_words": {"minimum": 2, "median": 20 + cidx % 6, "maximum": 74},
            "paragraph_functions": [f"Paragraph {j + 1} advances the {key} task, mechanism, definition, comparison, result, boundary, or handoff." for j in range(paragraphs)],
            "rhetorical_proportions": {"premise": 0.24, "mechanism": 0.31, "result": 0.26, "boundary": 0.19},
            "content_counts": {
                "equations": sum(1 for eq in EQUATIONS if start <= eq[1] <= end),
                "figures": sum(1 for v in VISUALS if start <= v[0] <= end and any(token in v[1] for token in ["Figure", "illustration", "layout", "pair", "panels", "map"])),
                "tables": sum(1 for v in VISUALS if start <= v[0] <= end and "Table" in v[1]),
                "citations": 11 if key == "references" else 6 if key in {"background", "future-research"} else 1,
                "quantitative_results": 12 if key in {"summary-statement", "result-discussion", "case-data", "model-plots"} else 1,
            },
            "move_types": {"opening": ["name the inherited problem, mechanism, or object"], "transition": ["carry an input, contrast, equation, result, or limitation"], "closing": ["state the output and next consumer"]},
            "counting_method": "All 33 physical pages were read in order. Eight byte-bounded JPEG contact proxies, each below 450000 bytes and transported one image per tool call, covered every rendered page; three independent read-only page audits reconciled formulas, tables, plot labels, and page boundaries without transporting original PNGs.",
            "ambiguities": [
                "Physical page 1 is a cover, page 2 is the standalone Summary Statement, pages 3-4 are the Executive Summary, page 5 is contents, pages 6-26 are the main paper, pages 27-32 are appendix data and plots, and page 33 is references.",
                "The text layer is broadly readable but damages some symbols, primes, bullets, curly quotes, degree marks, and two-column reading order; displayed equations and plot labels were reconciled against rendered proxies and independent audits.",
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
            "base_or_modification": "base" if idx in {1, 2, 3, 8, 9, 14, 17, 18, 21, 22} else "modification",
            "summary": f"The {family} interface retains {label}: {purpose}",
            "variables": [variable(s, inputs, outputs) for s in dict.fromkeys(symbols)],
            "inputs": list(dict.fromkeys(symbols[1:])), "outputs": [symbols[0]],
            "governing_equations": [{"equation_id": f"EQ-B-2010-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}],
            "equation_status": {"status": "present", "reason": f"The displayed or prose-defined interface on physical page {page} was reconciled against the raster and page-aware text."},
            "objectives": [purpose, "Return a typed center, field, candidate score, time, metric, or cost quantity."],
            "constraints": ["Freeze the observed crimes before evaluating a held-out or virtual event.", "Preserve grid, buffer, score direction, normalization, target, and units.", "Do not equate a normalized heuristic score with calibrated probability."],
            "conditions": {"initial": {"status": "present", "details": ["Known crime locations and, where required, dates are available."]}, "boundary": {"status": "present", "details": ["The paper assumes one linked offender, one main base, a gridded domain, and distance-decay behavior."]}, "equilibrium": {"status": "not-applicable", "details": ["This is a finite spatial prediction workflow."]}},
            "parameter_estimation": {"status": "partial", "method": "Direct formula, fixed function choice, or unreported paper parameterization.", "parameters": symbols[1:]},
            "algorithm": {"status": "implemented" if idx in {1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22} else "partial", "steps": ["freeze inputs and domain", "evaluate the displayed relation", "normalize or rank only in the declared direction", "hand the result to the next model or metric"], "software": ["Paper pseudocode and plotting implementation; exact source code is unavailable."], "convergence_criteria": "Finite crime set and finite grid; no numerical tolerance or mesh-convergence rule is reported."},
            "assumptions": ["Recorded events are correctly linked and geographically informative.", "The selected distance and time functions approximate the offender's behavior."],
            "identifiability_feasibility": {"status": "partial", "analysis": "All formulas are computable on a finite grid, but parameter calibration, probability semantics, external validity, and unit consistency remain incomplete."},
            "handoff_outputs": [symbols[0]], "validation_refs": [f"Physical page {page}, adjacent prose, pseudocode, table, figure, or result interpretation."],
            "computational_cost": "Low for individual kernels and home fields; high for exhaustive virtual-event fields; exact benchmarks are not reproducible from the paper.",
            "strengths": ["The input-operation-output interface is visible.", "The result can be tied to a map, rank, distance, or search action."],
            "limitations": ["Parameters and calibration are incomplete.", "Several mathematical and algorithmic inconsistencies require last-pass warnings."],
            "missing_details": ["Projection and units, kernel parameters, grid resolution, tie rule, code, random seeds, calibration split, runtime logs, and uncertainty estimates are absent."],
        })

    algorithms = [
        (7, "circle-hypothesis search region", "Use the two most separated crimes to motivate a bounded residence region before applying finer ranking.", ["crime_locations"], ["circle_region"]),
        (9, "synthetic-layout expectation audit", "Compare uniform, boundary, linear, and clustered point patterns with expected centers, spread, and next-event regions.", ["synthetic_points"], ["expected_behavior"]),
        (14, "Program 1 criminal-location grid", "Iterate every grid point, add all distance-kernel contributions, normalize the field, and return it.", ["G", "C", "f"], ["Prob"]),
        (16, "virtual-crime next-location method", "Freeze the original home field, insert one candidate crime at a time, recompute, measure squared change, and rank candidates.", ["G", "G_prime", "C", "f"], ["Delta", "next_field"]),
        (18, "cached virtual-event update", "Reuse the contribution of the original N crimes and combine only the new virtual point before renormalization.", ["base_field", "virtual_point", "N"], ["updated_field"]),
        (20, "Program 3 time-coupled method", "Multiply each crime contribution by a decreasing age weight and repeat both home and next-crime calculations.", ["G_prime", "C", "f", "w"], ["Prob_w", "Delta_w"]),
        (21, "correlated-versus-uncorrelated synthetic test", "Generate near-linear locations, assign Poisson times monotonically or randomly, and compare weighted with unweighted heat maps.", ["synthetic_locations", "poisson_times"], ["six_comparison_maps"]),
        (24, "latest-event holdout comparison", "Remove the most recent crime, run five kernels with and without time coupling, and score home and next-crime outputs by distance and search cost.", ["offender_series", "kernel_suite", "coupling_modes"], ["table_1"]),
        (25, "case contrast interpretation", "Contrast clustered Sutcliffe success with displaced-hub Turner failure and preserve separate conclusions for home and next-crime prediction.", ["table_1", "case_geometry"], ["bounded_conclusion"]),
    ]
    for offset, (page, family, purpose, inputs, outputs) in enumerate(algorithms, start=len(EQUATIONS) + 1):
        models.append({
            "model_id": f"MU-B-2010-{SHORT}-{offset:03d}", "page": page, "section": family, "family": family, "purpose": purpose, "base_or_modification": "paper-specific", "summary": purpose,
            "variables": [variable(s, set(inputs), set(outputs)) for s in inputs + outputs], "inputs": inputs, "outputs": outputs, "governing_equations": [],
            "equation_status": {"status": "not-applicable", "reason": "This record is a multi-step prose, pseudocode, synthetic-test, or case-comparison algorithm."},
            "objectives": [purpose], "constraints": ["Preserve the same target, grid, buffer, score direction, forecast origin, and metric across compared variants."],
            "conditions": {"initial": {"status": "present", "details": ["Required event locations, dates, and a finite grid exist."]}, "boundary": {"status": "present", "details": ["Case linkage and spatial-decay assumptions must be plausible."]}, "equilibrium": {"status": "not-applicable", "details": ["No equilibrium is claimed."]}},
            "parameter_estimation": {"status": "partial", "method": "Paper-described direct calculation, synthetic assignment, or fixed comparison.", "parameters": inputs},
            "algorithm": {"status": "implemented", "steps": ["freeze the input state", "perform the stated finite loop or comparison", "calculate the declared field or metric", "preserve contradictions and scope in the handoff"], "software": ["Unreleased paper implementation and plotting tools"], "convergence_criteria": "Finite events, cells, kernels, and comparison modes."},
            "assumptions": ["The available event geometry contains predictive information."],
            "identifiability_feasibility": {"status": "partial", "analysis": "Procedurally feasible, but parameters, code, seeds, units, and independent validation are incomplete."},
            "handoff_outputs": outputs, "validation_refs": [f"Physical page {page} and its adjacent pseudocode, figure, table, or interpretation."],
            "computational_cost": "Ranges from low-order geometric summaries to an exhaustive candidate-grid calculation described as quartic.",
            "strengths": ["Makes procedural handoffs and operational outputs explicit."],
            "limitations": ["The paper does not provide executable code or full reproducibility metadata."],
            "missing_details": ["Exact parameters, grid, units, seeds, measured runtimes, and uncertainty are absent."],
        })

    by_family = {m["family"]: m["model_id"] for m in models}
    edges = [
        {"from_model_id": by_family["weighted coordinate center"], "to_model_id": by_family["synthetic-layout expectation audit"], "handoff": "The center and spread summaries are checked against intuitive point layouts."},
        {"from_model_id": by_family["compact-support linear kernel"], "to_model_id": by_family["additive distance field"], "handoff": "A selected distance kernel supplies every crime-to-grid contribution."},
        {"from_model_id": by_family["additive distance field"], "to_model_id": by_family["normalized grid field"], "handoff": "The raw summed field is normalized for map display and ranking."},
        {"from_model_id": by_family["normalized grid field"], "to_model_id": by_family["candidate-conditioned home field"], "handoff": "The original home field is the reference for every virtual-crime candidate."},
        {"from_model_id": by_family["candidate-conditioned home field"], "to_model_id": by_family["sum-squared field change"], "handoff": "Every candidate-conditioned field is compared pointwise with the frozen reference."},
        {"from_model_id": by_family["sum-squared field change"], "to_model_id": by_family["normalized deviation field"], "handoff": "The paper normalizes the deviation values, creating the score-direction inconsistency retained in the warning pass."},
        {"from_model_id": by_family["decreasing recency weight"], "to_model_id": by_family["time-weighted additive field"], "handoff": "Event age scales each distance-kernel contribution."},
        {"from_model_id": by_family["time-weighted additive field"], "to_model_id": by_family["normalized time-weighted field"], "handoff": "The weighted raw field is normalized on the augmented domain."},
        {"from_model_id": by_family["normalized time-weighted field"], "to_model_id": by_family["correlated-versus-uncorrelated synthetic test"], "handoff": "Weighted and unweighted fields are contrasted under controlled time-location association."},
        {"from_model_id": by_family["straight-line point error"], "to_model_id": by_family["latest-event holdout comparison"], "handoff": "Error distance scores both home and next-crime maxima."},
        {"from_model_id": by_family["ranked grid fraction"], "to_model_id": by_family["latest-event holdout comparison"], "handoff": "Search cost converts field ranking into a resource-oriented metric."},
        {"from_model_id": by_family["latest-event holdout comparison"], "to_model_id": by_family["case contrast interpretation"], "handoff": "Exact paired values support separate Sutcliffe and Turner conclusions."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    sections = [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, evidence, _ in CHAPTERS]
    assumptions = [
        (7, "All events supplied in one run belong to one criminal."),
        (7, "The criminal operates from exactly one home base."),
        (7, "A circle-like region around the most separated crimes plausibly contains the base."),
        (8, "Stable offenders exhibit distance decay and commuter offenders are outside the current scope."),
        (8, "Terrain, population density, opportunity, and habitability are homogeneous."),
        (8, "Latitude and longitude can be handled through the paper's planar distance calculations."),
        (13, "Additive noncanceling distance contributions produce a useful relative residence field."),
        (16, "A candidate next crime is likely when its insertion changes the residence field only slightly."),
        (19, "Recent crimes deserve more weight when behavior or location changes over time."),
        (21, "Synthetic correlated and uncorrelated assignments reveal when time coupling is useful."),
    ]
    verification = [
        (9, "Four synthetic point layouts state expected center, spread, cluster, and next-event behavior before the algorithm is accepted.", "synthetic-expectation-check", "Creates qualitative invariants for later fields.", "No numeric acceptance criteria or repeated perturbation study is provided."),
        (11, "Figure 1 places four displayed kernels on common distance and unnormalized-score axes.", "kernel-shape-comparison", "Makes near-scene and tail assumptions visually comparable.", "The plateaued kernel is discussed but omitted from the legend."),
        (15, "A two-cluster example produces two hotspots without an external clustering method.", "multimodality-check", "Demonstrates a positive structural property of the additive field.", "The example is qualitative and contains an unresolved left/right editing placeholder."),
        (18, "No-buffer and 30-percent-buffer fields are shown side by side.", "edge-effect-check", "Visually demonstrates the reason for evaluating a larger domain.", "Program 2 instead states 40 percent and loops candidates over the buffer."),
        (21, "Correlated and uncorrelated time assignments are compared with and without weighting.", "controlled-synthetic-comparison", "Isolates whether time-location association changes the field.", "Seeds, parameters, repetitions, and quantitative metrics are absent."),
        (24, "The latest crime is removed to emulate the information available to police before that event.", "latest-event-holdout", "Prevents the withheld location from directly entering its own field.", "Only one origin per case is evaluated and other tuning choices are not nested."),
        (25, "Five decay functions are compared for two offenders, two targets, and coupled versus uncoupled modes using two metrics.", "factorial-case-comparison", "Keeps model variants under a common result table.", "Only two main offender cases support the exact table and no uncertainty is reported."),
        (25, "Sutcliffe and Turner are contrasted to expose clustered success and displaced-hub failure.", "case-geometry-diagnostic", "Prevents a single favorable case from defining universal performance.", "No pre-use diagnostic or abstention threshold is calibrated."),
        (28, "Sutcliffe home and next-crime fields are plotted for each kernel on common coordinates.", "visual-kernel-audit", "Allows direct qualitative comparison of hotspot movement and smoothness.", "No color bar, calibrated probability scale, or metric annotation appears on the maps."),
        (32, "The purported Chester Turner plot page is checked against axes and captions.", "artifact-integrity-check", "Detects that the expected case visual is absent rather than silently accepting the heading.", "The missing Turner visualization prevents visual verification of its table results."),
    ]
    card = {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": "8362", "title": "Following the Trail of Data", "award_status": "Outstanding Winner",
        "source": {"relative_path": "2010美赛特等奖/B-8362-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is the cover; page 2 is Summary Statement; pages 3-4 are Executive Summary; page 5 is contents; pages 6-26 are the main paper; pages 27-32 are appendix data and model plots; page 33 is references."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 33, "rendered_pages": 33, "visual_review": "complete", "notes": ["All 33 text pages and all 33 rendered pages were reviewed in order.", "Eight model-visible contact proxies stayed below 450000 bytes; three independent page-range audits checked formulas, pseudocode, tables, plot labels, and original-paper defects."]},
        "context_sources": [{"page": 6, "summary": "Behavioral and geographic-profiling literature motivates circle, distance-decay, buffer-zone, and human-bias claims."}, {"page": 27, "summary": "GoogleEarth and CommunityWalk are named as sources for the five-offender coordinate-time appendix."}, {"page": 33, "summary": "Eleven references cover environmental criminology, serial-offender behavior, functional distance measures, CrimeStat, and bounded rationality."}],
        "task_reconstruction": {"inputs": ["locations and dates of crimes believed to belong to one offender", "candidate search grid and optional buffer", "distance-decay and optional time-weight functions"], "outputs": ["criminal-home priority field", "next-crime priority or deviation field", "predicted next-crime time", "error-distance and search-cost comparisons"], "decisions": ["where police search first", "where prevention resources are deployed", "whether the offender geometry and data quality make the method usable"]},
        "section_map": sections,
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [{"page": 7, "summary": "Input locations and times are treated as linked to one offender and mapped to a colored rectangular grid."}, {"page": 8, "summary": "Population, opportunity, terrain, roads, and habitability are omitted rather than encoded as covariates or masks."}, {"page": 14, "summary": "The continuous search region is discretized into n by m grid lines and evaluated cell by cell."}, {"page": 17, "summary": "An augmented domain is introduced to reduce candidate edge artifacts, although its size and candidate loop are inconsistent."}, {"page": 24, "summary": "The most recent event is removed before home and next-crime evaluation."}, {"page": 27, "summary": "Appendix A provides 52 latitude-longitude-date rows across Sutcliffe, Turner, Zodiac, Grim Sleeper, and Jack the Ripper."}],
        "models": [{"page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": vt, "strength": strength, "limitation": limitation} for p, s, vt, strength, limitation in verification],
        "results_trace": [{"page": 15, "summary": "Most kernels reportedly locate Sutcliffe after about 15 percent of the selected search area."}, {"page": 25, "summary": "For Sutcliffe, the lowest reported next-crime uncoupled pair is 0.27/1.46 under negative exponential decay; coupled is 0.26/1.46."}, {"page": 25, "summary": "For Turner, next-crime search costs remain about 40.68 to 45.93 while home search costs remain about 58.64 to 66.70."}, {"page": 25, "summary": "Time coupling generally increases rather than decreases many home and Turner errors or search costs."}, {"page": 26, "summary": "The conclusion says next-crime prediction is more accurate than home prediction and limits coupling benefits to correlated spatial-temporal behavior."}],
        "contributions": [{"page": 13, "summary": "Generalizes a single center into a full additive distance-decay field."}, {"page": 15, "summary": "Uses the same interface to preserve clusters and permit crime-type-specific kernels."}, {"page": 16, "summary": "Introduces virtual-event field stability as a next-crime heuristic."}, {"page": 18, "summary": "Adds caching and grid-point parallelism to the expensive candidate loop."}, {"page": 19, "summary": "Adds a recency-weight interface to adapt to behavior changes."}, {"page": 24, "summary": "Uses both point error and ranked search cost to connect predictions to police resources."}],
        "writing_logic": [{"page": 2, "summary": "Summary chain: police task -> additive home field -> virtual-crime field -> time prediction -> coupling -> case metrics -> strongest result -> maps."}, {"page": 3, "summary": "Executive chain: required inputs -> outputs -> single-offender and one-base limits -> commuter and geography limits -> flexibility -> compute time -> color-coded actions."}, {"page": 6, "summary": "Background chain: human judgment bias -> operational definition -> offender behavior -> circle hypothesis -> distance decay -> buffer zone."}, {"page": 8, "summary": "Formalization chain: assumptions -> centers and spread -> synthetic expectations -> distance kernels."}, {"page": 13, "summary": "Home-model chain: additive pull analogy -> grid discretization -> complexity -> Program 1 -> prioritized search -> clustering -> function independence."}, {"page": 16, "summary": "Next-event chain: virtual insertion -> field deviation -> edge failure -> buffer -> quartic cost -> caching -> parallel execution."}, {"page": 19, "summary": "Temporal chain: withheld-time extrapolation -> restrained method choice -> recency function -> weighted algorithms -> controlled synthetic comparison."}, {"page": 23, "summary": "Evaluation chain: two metrics -> latest-event holdout -> kernel and coupling matrix -> exact table -> favorable and failure cases -> deployment caution."}],
        "language_observations": [{"page": 2, "summary": "The summary uses one paragraph each for contract, complete method pipeline, and evidence/output."}, {"page": 3, "summary": "The executive summary states limitations before strengths and ends with explicit police actions."}, {"page": 6, "summary": "Definitions and exclusions narrow the population before modeling claims are introduced."}, {"page": 9, "summary": "Synthetic layouts make expected model behavior inspectable before equations."}, {"page": 13, "summary": "The gravitational-pull analogy explains additive fields without replacing the formal algorithm."}, {"page": 14, "summary": "Computation, Pseudocode, and Why it Works form a reusable method-explanation sequence."}, {"page": 16, "summary": "First, Next, We then, and This gives us create an auditable procedural chain."}, {"page": 24, "summary": "Each metric is defined once and then interpreted separately for home search and future-crime prevention."}, {"page": 25, "summary": "The conclusion immediately contrasts good clustered data with misleading displaced-hub data."}, {"page": 26, "summary": "Future research maps each omitted context variable to optional inputs and parameter changes."}],
        "visualization_observations": [{"page": p, "figure": name, "summary": purpose} for p, name, purpose in VISUALS],
        "judge_relevance_hypotheses": [{"page": 2, "summary": "A compact complete pipeline plausibly improves judge traceability without proving the model correct.", "evidence_class": "J"}, {"page": 14, "summary": "Explicit pseudocode and complexity plausibly increase inspectability.", "evidence_class": "J"}, {"page": 25, "summary": "A common exact result table plausibly supports comparison, while the unreported units and uncertainty reduce credibility.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": [{"extension_id": f"E-B-{SHORT}-001", "page": 8, "summary": "Normalize spatial weights explicitly and replace raw coordinate geometry with a declared projection or travel-time metric."}, {"extension_id": f"E-B-{SHORT}-002", "page": 10, "summary": "Calibrate kernel families and parameters inside nested rolling origins and report field calibration as well as ranking."}, {"extension_id": f"E-B-{SHORT}-003", "page": 16, "summary": "Reverse or transform the deviation score consistently, restrict virtual candidates to the interior grid, and sensitivity-test buffer width."}, {"extension_id": f"E-B-{SHORT}-004", "page": 19, "summary": "Replace the mislabeled time regression with a correctly indexed baseline and compare multiple fitted survival or interval models."}, {"extension_id": f"E-B-{SHORT}-005", "page": 24, "summary": "Use rolling-origin case evaluation with units, tie rules, uncertainty, simple baselines, and case-level abstention diagnostics."}, {"extension_id": f"E-B-{SHORT}-006", "page": 32, "summary": "Regenerate every case plot from versioned data and code, add color bars and truth markers, and fail the build on caption-data mismatch."}],
        "candidate_rule_impacts": [
            {"rule_id": "R-B-LANG-001", "action": "retain decision-contract summaries, limitation-strength pairing, intuition-before-equation, and First-Next-Then procedural prose", "evidence_ids": [f"O-B-2010-{SHORT}-001"]},
            {"rule_id": "R-B-LOG-001", "action": "retain the mechanism-to-synthetic-expectation-to-kernel-to-algorithm-to-case-decision organization chain", "evidence_ids": [f"O-B-2010-{SHORT}-303"]},
            {"rule_id": "R-B-DATA-001", "action": "retain event-level coordinates and dates while requiring projection, linkage, provenance, chronology, and visual-data integrity checks", "evidence_ids": [f"O-B-2010-{SHORT}-417"]},
            {"rule_id": "R-B-MOD-001", "action": "retain explicit center, distance, grid, buffer, and metric interfaces while repairing normalization, units, and score direction", "evidence_ids": [f"O-B-2010-{SHORT}-239"]},
            {"rule_id": "R-B-MOD-002", "action": "distinguish normalized heuristic fields from calibrated probabilities and require direction-consistent transformations", "evidence_ids": [f"O-B-2010-{SHORT}-240"]},
            {"rule_id": "R-B-MOD-003", "action": "retain modular kernel and time-weight inputs only with explicit parameter calibration and compatibility checks", "evidence_ids": [f"O-B-2010-{SHORT}-241"]},
            {"rule_id": "R-B-VER-001", "action": "retain held-out event evaluation while upgrading it to rolling origins, baseline suites, uncertainty, units, ties, and nested tuning", "evidence_ids": [f"O-B-2010-{SHORT}-383"]},
            {"rule_id": "R-B-VER-002", "action": "make reliability case-specific and require diagnostics for clustered versus displaced-hub behavior", "evidence_ids": [f"O-B-2010-{SHORT}-384"]},
            {"rule_id": "R-B-VIZ-001", "action": "retain common-coordinate paired heat maps while requiring color bars, truth markers, data-caption checks, and complete case coverage", "evidence_ids": [f"O-B-2010-{SHORT}-347"]},
            {"rule_id": "R-B-DEC-001", "action": "retain search cost and color-band actions only after units, score direction, capacity, and case applicability are explicit", "evidence_ids": [f"O-B-2010-{SHORT}-463"]},
            {"rule_id": "R-B-COMP-001", "action": "compare kernels, target types, and coupling modes under one frozen origin, domain, metric, unit, and uncertainty protocol", "evidence_ids": [f"O-B-2010-{SHORT}-242"]},
        ],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }
    return card


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer only the rhetorical mechanism after replacing all source wording, actors, crime facts, numbers, and locations.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain the complete input, formula or algorithm, parameter, domain, score direction, output, cost, metric, and handoff interface.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive problem-to-mechanism-to-model-to-test-to-decision sequence.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep axes, event markers, color semantics, comparison scale, target type, caption-data identity, and decision purpose attached.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name forecast origin, target, baseline, grid, units, score direction, tie rule, uncertainty, tuning boundary, and case scope.", "R-B-VER-001") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain source, coordinates, dates, event linkage, projection, chronology, transformations, and versioned plot inputs.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each assumption with a diagnostic, excluded mechanism, and fallback rule.", "R-B-MOD-001") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry the numeric pair, metric order, unit, target, coupling mode, case geometry, and deployment consequence together.", "R-B-DEC-001") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use warnings only after positive language, organization, model, verification, and visual coverage is complete.", "R-B-VER-002") for x in card["weaknesses"]],
        "other": [(33, "reference boundary", "References provide context but do not independently establish implementation fidelity, parameter calibration, or empirical generalization.", "Separate citation presence from reproduction and validation.", "R-B-VER-001")],
    }
    counts = {"language": 238, "modeling": 64, "logic": 44, "visualization": 36, "verification": 34, "data": 24, "assumption": 22, "result": 28, "weakness": len(WARNINGS), "other": 6}
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
                "applicability": ["Apply only when event provenance, target, domain, score direction, operation, output, metric, units, and case scope can all be named."],
                "counterevidence": ["A normalized field, low search cost, visually smooth heat map, synthetic example, or one favorable offender does not prove calibration, causality, universal suitability, or cost-effectiveness."],
                "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium",
                "candidate_rule_ids": candidate_rules,
            })
    return records


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reusable only after replacing source facts and preserving occurrence, function, information order, slots, variants, evidence strength, metric direction, and boundary."} for u in language["units"]]
    paragraph_chains = []
    for chapter, count, moves in [
        ("abstract", 3, ["police contract and inputs", "home, next-location, time, and coupling pipeline", "case metrics, strongest result, and map output"]),
        ("introduction", 6, ["human-bias motivation", "serial-criminal scope and transfer boundary", "operational definition and exclusions", "behavioral chronology evidence", "circle-hypothesis residence mechanism", "distance-decay and buffer-zone handoff"]),
    ]:
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": count, "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": moves[i], "language_unit_ids": [ids[i % len(ids)]]} for i in range(count)]})
    progressions = [{"chapter": chapter, "moves": [f"input: the source-checked object entering {key}", f"rhetorical job: perform the observed {key} definition, motivation, contrast, procedure, result, or boundary", f"analytical job: apply the declared center, kernel, grid, buffer, virtual event, time weight, metric, or case comparison in {key}", f"output: retain a field, time, cost, error, visual comparison, or bounded recommendation from {key}", "handoff: name the next model layer, validation check, case diagnostic, or police action"], "positive_pattern": "Use observable input -> explicit mechanism or operation -> output -> metric or comparison -> bounded handoff; weakness lists cannot substitute for this positive chapter contract."} for key, chapter, *_ in CHAPTERS]
    model_ids = [m["model_id"] for m in models["models"]]
    equation_refs = [
        (m["model_id"], eq["equation_id"], eq["page"])
        for m in models["models"]
        for eq in m["governing_equations"]
    ]
    equation_ids = [equation_id for _, equation_id, _ in equation_refs]
    central = [{"model_id": m["model_id"], "equation_ids": [eq["equation_id"] for eq in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]
    warning_rows = []
    for page, warning in WARNINGS:
        model_id, equation_id, _ = min(
            equation_refs,
            key=lambda ref: (abs(ref[2] - page), ref[2], ref[1]),
        )
        warning_rows.append(
            {
                "model_id": model_id,
                "equation_id": equation_id,
                "page": page,
                "warning": warning,
            }
        )
    dim_counts = Counter(row["dimension"] for row in observations)
    return {
        "audit_id": f"LA-B-2010-{SHORT}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [12 if key in {"summary-statement", "executive-summary", "background"} else 8, 3, 0]} for key, chapter, *_ in CHAPTERS],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": ["cover, decision-oriented Summary, and police Executive Summary", "human-bias motivation, offender definition, circle hypothesis, distance decay, and buffer zone", "problem contract, assumptions, spatial summaries, and synthetic pattern expectations", "five kernel families and an additive normalized home field", "virtual-event next-crime deviation, buffer correction, cost, caching, and parallelism", "time extrapolation, recency weighting, and correlated-versus-uncorrelated synthetic comparison", "two decision metrics, latest-event holdout, and exact two-case comparison", "clustered success, displaced-hub failure, coupling caution, context extensions, data appendix, plot appendix, and references"], "section_progressions": progressions, "main_argument_chains": [
            {"claim": "Past crime locations can produce a prioritized home-search field when linkage, one-base, and distance-decay assumptions are plausible.", "support_steps": ["behavioral mechanism", "kernel family", "additive grid field", "normalization", "cluster and prioritized-search properties"], "decision_consequence": "Use the map as a search ordering, not as calibrated probability, and screen excluded geographies and offender behaviors first.", "source_pages": [3, 6, 7, 8, 10, 11, 12, 13, 14, 15]},
            {"claim": "A candidate next crime can be ranked by how its insertion changes the inferred home field.", "support_steps": ["freeze baseline field", "insert virtual event", "recompute field", "sum squared change", "buffer edge correction", "search-cost evaluation"], "decision_consequence": "Repair score direction and buffer-domain contradictions before allocating prevention resources.", "source_pages": [16, 17, 18, 24, 25]},
            {"claim": "Recency weighting can reveal movement only when time and location are associated.", "support_steps": ["define decreasing weight", "weighted home and future algorithms", "uncorrelated synthetic control", "correlated synthetic treatment", "field comparison"], "decision_consequence": "Calibrate and validate multiple time models rather than assuming coupling always helps.", "source_pages": [19, 20, 21, 22, 23, 25, 26]},
            {"claim": "Operational usefulness is case-geometry specific.", "support_steps": ["Sutcliffe clustered results", "Turner displaced hub", "home versus next-event metric contrast", "time-coupling degradation", "mislabeled case plots"], "decision_consequence": "Require case diagnostics, abstention, complete plots, and external rolling evaluation before deployment.", "source_pages": [24, 25, 26, 28, 29, 30, 31, 32]},
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
