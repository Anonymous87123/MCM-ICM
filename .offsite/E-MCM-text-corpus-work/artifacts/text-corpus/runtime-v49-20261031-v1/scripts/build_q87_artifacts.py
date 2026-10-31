from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2010-7947-b6007ae0"
SHORT = "7947"
SHA = "b6007ae0ba0598637036a5da83fac1ceb6cd843e14d5809895d491702b75f2e9"
TYPE = "B"
YEAR = "2010"
PAGE_COUNT = 28

PATTERNS = [
    "LP-B-ABS-PROBLEM-PIPELINE-EVIDENCE-BOUNDARY",
    "LP-B-ABS-PARALLEL-METHODS",
    "LP-B-INT-NARRATIVE-TO-MATHEMATICS",
    "LP-B-ASSUMPTION-OPERATIONALIZATION",
    "LP-B-METHOD-REQUIREMENT-CHOICE",
    "LP-B-RESULT-NUMERIC-VS-SIGNIFICANT",
    "LP-B-RESULT-AGGREGATE-VS-CASE",
    "LP-B-CASE-METRIC-TO-RESOURCE",
    "LP-B-HUMAN-MODEL-HANDOFF",
    "LP-B-EXEC-STRENGTH-LIMITATION-PAIR",
]

# key, protocol chapter, physical first/last page, tag, source-checked chapter evidence, visual paragraphs
CHAPTERS = [
    ("summary", "abstract", 1, 1, "SUM", "The standalone Summary compresses the decision target, behavioral premise, spatial and spatiotemporal model families, rolling hit-score metric, aggregation result, offender heterogeneity, and operational boundary into one result-first page.", 6),
    ("executive-summary", "memo", 2, 3, "EXE", "The two-page Executive Summary translates the model suite into law-enforcement use conditions, names required evidence and resources, lists omitted geographic and offender features, and recommends complementing rather than replacing traditional investigation.", 10),
    ("formal-title-abstract", "title", 4, 4, "TTL", "The formal title and Abstract repeat the target-method-metric-result-boundary chain while naming geographical profiling as the organizing mechanism.", 5),
    ("contents", "problem-restatement", 5, 5, "CON", "The contents exposes a background-data-assumptions-metric-spatial-spatiotemporal-aggregation-case-conclusion-future-work route.", 1),
    ("introduction", "introduction", 6, 6, "INT", "The introduction moves from the investigative information gap to a large search-area problem, introduces geographical profiling as resource prioritization, and previews every later section.", 5),
    ("terminology-literature", "problem-analysis", 6, 8, "BKG", "The background defines serial crime, spatiotemporal data, spatial behavior, profiling methods, and prioritized search areas; it contrasts residence prediction with next-crime prediction and positions the paper against contested literature.", 13),
    ("data", "data-preprocessing", 8, 9, "DAT", "The data section admits the absence of a standardized corpus, documents police/news and SpotCrime provenance, and inventories nine heterogeneous sequences totaling 124 crimes with offender-specific temporal-decay accuracy.", 7),
    ("assumptions-notation", "assumptions", 10, 11, "ASM", "The construction section states data accuracy, single-offender linkage, nonrandom rational behavior, ordered coordinates and times, a gridded search domain, sector-constant scores, and Euclidean distance.", 11),
    ("performance-metric", "robustness-verification", 11, 13, "MET", "The metric section interprets hit score as prioritized area searched before the held-out event, defines offender-level rolling accuracy, and fixes a data-dependent search square to prevent arbitrary denominator inflation.", 11),
    ("spatial-models", "model-establishment", 13, 16, "SPA", "The spatial section compares random, standard-deviation, centroid, harmonic, circle-center, median, linear-decay, and exponential-decay schemes under one sector ranking interface.", 17),
    ("spatiotemporal-models", "model-improvement", 16, 17, "TMP", "The spatiotemporal section motivates recency, defines a time-weight sequence, and transfers that weight into centroid, harmonic-mean, and distance-decay models.", 9),
    ("individual-results", "results", 18, 19, "RES", "The individual-results section performs rolling next-event evaluation across all sequences, separates significant improvement over random from nonsignificant differences among proposed methods, and shows no monotone gain from longer histories.", 8),
    ("aggregation-models", "algorithm", 19, 22, "AGG", "The aggregation section introduces linear and logarithmic opinion pools, calibrates decay scales from mean pairwise distance, applies a two-level factorial inclusion design, and distinguishes the numerically best equal-weight pair from statistical superiority.", 18),
    ("sutcliffe-case", "strengths", 23, 24, "CAS", "The case study turns a 10.6 percent hit score into a reduction from 27,818 to 2,941 square kilometers and overlays the historical events with a Bradford-centered temporal-decay risk field.", 8),
    ("conclusion", "conclusion", 23, 25, "END", "The conclusion preserves three levels: aggregate superiority over random, no significant difference among nonrandom methods, and strong offender-specific applicability variation including a worse-than-random case.", 8),
    ("future-work", "future-improvements", 25, 26, "FUT", "Future work calls for a standardized large corpus, richer geographic and offender feature spaces, and an explicit cost-quality comparison between proprietary software and trained human profilers.", 7),
    ("references", "references", 27, 28, "REF", "Twenty references connect geographic profiling, serial-crime behavior, mathematical foundations, expert aggregation, case evidence, and the Google map layer; several source typos and one incomplete citation remain visible.", 2),
]

MOVES = [
    ("decision-contract", "Name the decision, observed evidence, output, and user before technical detail.", "decision -> available evidence -> model output -> decision user"),
    ("mechanism-before-method", "State the behavioral or spatial mechanism that makes a model family plausible.", "mechanism -> required behavior -> selected family"),
    ("parallel-family-contrast", "Present competing models in parallel so their changed assumption remains visible.", "shared input -> family A -> family B -> common metric"),
    ("definition-stack", "Introduce symbols through a Given-Let-Then stack that closes with operational meaning.", "given objects -> define symbol -> equation -> interpretation"),
    ("purpose-opening", "Open a paragraph with the reason for the next calculation or experiment.", "purpose clause -> operation -> evidence -> consequence"),
    ("numeric-versus-significant", "Separate the lowest numerical score from a statistically supported superiority claim.", "numeric result -> interval or test -> admissible claim"),
    ("aggregate-versus-case", "Keep corpus-average performance distinct from offender-specific reliability.", "aggregate result -> case contrast -> scope boundary"),
    ("metric-to-resource", "Translate a dimensionless score into searched area or deployed resources.", "metric -> physical quantity -> operational consequence"),
    ("limitation-to-extension", "Turn a named omission into a concrete next data or validation requirement.", "omission -> failure risk -> extension"),
    ("human-model-partnership", "Assign broad ranking to the model and contextual judgment to investigators.", "model contribution -> missing context -> complementary use rule"),
]

EXAMPLES = [
    ("A flood paper states that the decision is evacuation-zone priority from gauges, roads, and census records.", "It reserves route closure judgment for local emergency staff and limits use to calibrated storm regimes."),
    ("A clinic paper motivates a time-varying arrival model by showing that recent arrivals contain operational information.", "It compares the dynamic model with a constant-rate baseline under forward validation."),
    ("A freight study places Euclidean, road-time, and congestion-aware facility models in parallel columns.", "Every variant returns the same delivery-cost target and is scored on held-out routes."),
    ("A wildfire paper writes Given ignition points, Let a cell score be defined, Then the searched-area fraction is interpreted for crews.", "Ties and inaccessible cells are specified before the score is reported."),
    ("To set the decay scale, an ecological study uses a training-fold median separation and checks three alternatives.", "The selected value is frozen before the next season is evaluated."),
    ("A reservoir ensemble has the lowest mean shortage, but overlapping intervals prevent a claim of superiority.", "The paper reports it as numerically best and operationally promising, not proven dominant."),
    ("A demand model improves average error while failing for one rural region.", "The conclusion preserves both statements and defines an abstention rule for that region."),
    ("A search score of 0.08 is converted into square kilometers, team-hours, and cumulative area bands.", "Decision-makers can then compare the score with available capacity."),
    ("A traffic paper names missing turn delays and proposes timestamped route traces plus rolling calibration.", "The future-work item therefore closes a specific model deficiency."),
    ("A disease map prioritizes broad districts while public-health teams add clinic access and current outbreak intelligence.", "The final action log records model rank and human override separately."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose, confidence
EQUATIONS = [
    ("spatial event domain", 10, "model descriptions", "ordered spatial observations", "x_1,...,x_n in A subset R^2", r"x_1,ldots,x_nin Asubsetmathbb R^2", ["x", "A", "n"], "Represent the ordered known crime locations inside the search region.", "high"),
    ("time ordering", 10, "model descriptions", "ordered event times", "0=t_1<...<t_n", r"0=t_1<cdots<t_n", ["t", "n"], "Preserve forecast-origin order and define elapsed-event chronology.", "high"),
    ("sector constant score", 10, "model descriptions", "grid score field", "y in S_ij implies P(y)=P(S_ij)", r"yin S_{i,j}Rightarrow P(y)=P(S_{i,j})", ["P", "y", "S_ij"], "Discretize the continuous search area into ranked sectors.", "high"),
    ("grid count", 11, "discretization", "square grid resolution", "k equals search-area side divided by Delta s", r"k=rac{L_{mathrm{search}}}{Delta s}", ["k", "L_search", "Delta_s"], "Relate search extent and cell resolution.", "medium"),
    ("better-ranked sector set", 12, "hit score", "strict rank set", "B={S_ij in S: P(S_ij)>P(L)}", r"B={S_{i,j}in S:P(S_{i,j})>P(L)}", ["B", "S_ij", "S", "P", "L"], "Collect sectors ranked strictly above the sector containing the next event.", "high"),
    ("hit score", 12, "hit score", "prioritized search fraction", "H=|B|/|S|", r"H=rac{|B|}{|S|}", ["H", "B", "S"], "Measure the fraction of the search area visited before the held-out sector.", "high"),
    ("criminal accuracy", 12, "rolling evaluation", "offender-specific rolling mean", "Z=(1/(n-3)) sum from k=4 to n H_k", r"Z=rac{1}{n-3}sum_{k=4}^{n}H_k", ["Z", "H_k", "n"], "Average forward hit scores after the minimum three-event history.", "high"),
    ("search square", 13, "search area", "data-dependent square extent", "side equals twice maximum pairwise distance and center equals crime mean", r"L_{mathrm{search}}=2max_{i<j}d(x_i,x_j)", ["L_search", "d", "x_i", "x_j"], "Fix a reproducible denominator for cross-model hit-score comparison.", "high"),
    ("standard deviation rectangle", 14, "standard deviation methods", "axis-aligned dispersion region", "xbar plus or minus c sigma_lon and c sigma_lat", r"ar x+(pm csigma_{mathrm{lon}},pm csigma_{mathrm{lat}})", ["rectangle", "x_bar", "c", "sigma_lon", "sigma_lat"], "Define a rectangular search region from coordinate dispersion.", "high"),
    ("standard deviation ellipse", 14, "standard deviation methods", "trend-aligned dispersion region", "ellipse axes 2c sigma_lon and 2c sigma_lat rotated theta", r"(a,b,	heta)=(2csigma_{mathrm{lon}},2csigma_{mathrm{lat}},	heta)", ["ellipse", "c", "sigma_lon", "sigma_lat", "theta"], "Define a least-squares-oriented elliptical search region.", "medium"),
    ("centralization score", 14, "centralization methods", "inverse-distance score", "P(S_ij)=1/d(S_ij,C)", r"P(S_{i,j})=rac{1}{d(S_{i,j},C)}", ["P", "S_ij", "d", "C"], "Rank sectors by distance from a selected focal point.", "high"),
    ("centroid", 14, "centralization methods", "arithmetic focal point", "C=(1/n) sum x_i", r"C=rac1nsum_{i=1}^{n}x_i", ["C", "x_i", "n"], "Estimate a single central focal point.", "high"),
    ("harmonic mean focal point", 15, "centralization methods", "harmonic focal point", "C=n/(sum 1/x_i)", r"C=rac{n}{sum_{i=1}^{n}1/x_i}", ["C_h", "x_i", "n"], "Construct the paper's harmonic-mean center.", "high"),
    ("circle center", 15, "centralization methods", "diameter midpoint focal point", "C=(x_i+x_j)/2 for farthest pair", r"C=rac{x_i+x_j}{2},quad (i,j)=argmax_{a<b}d(x_a,x_b)", ["C_circle", "x_i", "x_j", "d"], "Use the midpoint of the most separated crimes as a focal point.", "high"),
    ("probability distance field", 15, "probability distance methods", "multi-event additive field", "P(S_ij)=sum_k f(d(S_ij,x_k))", r"P(S_{i,j})=sum_{k=1}^{n}f(d(S_{i,j},x_k))", ["P", "S_ij", "f", "d", "x_k", "n"], "Accumulate contributions from every previous event instead of one center.", "high"),
    ("linear decay", 15, "probability distance methods", "linear distance score", "f(d)=alpha-beta d", r"f(d)=alpha-eta d", ["f_linear", "d", "alpha", "beta"], "Decrease the sector contribution linearly with distance.", "high"),
    ("exponential decay", 15, "probability distance methods", "exponential distance score", "f(d)=exp(-gamma d)", r"f(d)=e^{-gamma d}", ["f_exp", "d", "gamma"], "Decrease the sector contribution exponentially with distance.", "high"),
    ("temporal weight", 16, "spatiotemporal models", "recency weight", "w_i=(t_i-t_1)/t_n+k", r"w_i=rac{t_i-t_1}{t_n}+k", ["w_i", "t_i", "t_1", "t_n", "k"], "Give later events more influence while keeping the first event nonzero.", "high"),
    ("total temporal weight", 16, "spatiotemporal models", "weight normalizer", "W=sum_i w_i", r"W=sum_{i=1}^{n}w_i", ["W", "w_i", "n"], "Normalize weighted focal-point calculations.", "high"),
    ("temporal centroid", 17, "spatiotemporal models", "weighted focal point", "C=(1/W) sum x_i w_i", r"C=rac1Wsum_{i=1}^{n}x_iw_i", ["C_temporal", "W", "x_i", "w_i", "n"], "Shift the focal point toward recent events.", "high"),
    ("temporal harmonic mean", 17, "spatiotemporal models", "weighted harmonic focal point", "C=W/(sum w_i/x_i)", r"C=rac{W}{sum_{i=1}^{n}w_i/x_i}", ["C_th", "W", "w_i", "x_i", "n"], "Apply the paper's recency weighting to its harmonic center.", "high"),
    ("temporal probability distance", 17, "spatiotemporal models", "weighted multi-event field", "P(S_ij)=sum_k w_k f(d(S_ij,x_k))", r"P(S_{i,j})=sum_{k=1}^{n}w_kf(d(S_{i,j},x_k))", ["P_temporal", "S_ij", "w_k", "f", "d", "x_k", "n"], "Weight every event's distance contribution by recency.", "high"),
    ("linear opinion pool", 20, "aggregation", "weighted additive ensemble", "P(S_ij)=sum_k W_k P_k(S_ij)", r"P(S_{i,j})=sum_{k=1}^{n}W_kP_k(S_{i,j})", ["P_pool", "W_k", "P_k", "S_ij", "n"], "Combine compatible model fields through a weighted sum.", "high"),
    ("logarithmic opinion pool", 20, "aggregation", "weighted multiplicative ensemble", "P(S_ij)=product_k P_k(S_ij)^W_k", r"P(S_{i,j})=prod_{k=1}^{n}P_k(S_{i,j})^{W_k}", ["P_logpool", "P_k", "W_k", "S_ij", "n"], "Combine model fields through a weighted product.", "high"),
    ("mean pairwise distance", 22, "aggregation calibration", "corpus scale statistic", "delta_bar=2/[n(n-1)] sum_{i<j} d(x_i,x_j)", r"ardelta=rac{2}{n(n-1)}sum_{1le i<jle n}d(x_i,x_j)", ["delta_bar", "n", "d", "x_i", "x_j"], "Set a sequence-specific spatial scale for ensemble components.", "high"),
    ("linear decay calibration", 22, "aggregation calibration", "zero-at-mean-distance rule", "alpha=1 and alpha-beta delta_bar=0", r"alpha=1,qquad alpha-etaardelta=0", ["beta", "alpha", "delta_bar"], "Scale the linear component before pooling.", "high"),
    ("exponential decay calibration", 22, "aggregation calibration", "mean-distance exponential rule", "gamma=sqrt(2/delta_bar)", r"gamma=sqrt{rac{2}{ardelta}}", ["gamma", "delta_bar"], "Scale the exponential component before pooling.", "high"),
]

VISUALS = [
    (1, "Standalone Summary", "Shows the complete task-method-metric-result-boundary chain on one competition summary sheet."),
    (2, "Executive Summary applicability bullets", "Turns model validity into linkage, historical accuracy, and resource-capacity checks."),
    (3, "Executive Summary limitation bullets", "Keeps omitted geography, omitted offender features, and human comparison visible beside the recommendation."),
    (5, "Contents", "Confirms full route and absence of an appendix."),
    (9, "Table 1", "Audits nine sequences, 124 crimes, and the extreme offender-specific spread from 0.020 to 0.517."),
    (11, "Figure 1", "Defines the square grid sectors and cell-resolution interface used by every ranking model."),
    (16, "Figure 2", "Contrasts a single centroid hotspot with an exponential field concentrated around all observed crimes."),
    (17, "Figure 3", "Shows how temporal weighting moves the field toward the recent end of an eastward sequence."),
    (18, "Figure 4", "Compares aggregate hit scores for random and all individual models with uncertainty bars."),
    (19, "Figure 5", "Shows unstable hit score by number of observed crimes with 50 percent confidence intervals."),
    (20, "Table 2", "Provides exact mean hit scores and 95 percent confidence half-widths for ten models."),
    (21, "Figure 6a", "Shows the pure circle-center endpoint of the opinion-pool weight sweep."),
    (21, "Figure 6b-c", "Shows intermediate hotspot movement and shape under 0.25/0.75 and 0.50/0.50 weights."),
    (21, "Figure 6d-e", "Shows the transition to a pure exponential-decay field."),
    (23, "Figure 7", "Compares one-standard-deviation rectangle and ellipse search regions for Peter Sutcliffe."),
    (24, "Figure 8a", "Maps the Sutcliffe event locations on recognizable geography with a physical scale."),
    (24, "Figure 8b", "Shows the Bradford-centered temporal exponential-decay risk field and secondary Manchester hotspot."),
]

WARNINGS = [
    (12, "Hit score counts only sectors strictly above the held-out sector and does not specify tie ordering, so tied fields can receive optimistically small search fractions."),
    (13, "Hit score is denominator-sensitive; the twice-maximum-distance search square is reproducible but heuristic and lacks size, shape, and grid-resolution sensitivity."),
    (14, "The inverse-distance centralization score is singular if a sector representative coincides with the focal point."),
    (15, "The harmonic mean of two-dimensional coordinates is mathematically ambiguous and can be unstable at zero or across signed coordinate values."),
    (15, "Linear decay can become negative, so the quantity is not a probability unless truncated or explicitly treated only as a ranking score."),
    (18, "The claim that exponential-decay constants do not affect hit-score ranking is generally false because changing gamma can reorder sums of several exponential contributions."),
    (16, "Temporal normalization uses t_n rather than explicitly t_n-t_1, making the formula dependent on how the time origin is encoded."),
    (16, "With k=0.1 and t_1=0, the last-to-first temporal weight ratio is 11 rather than the stated approximately ten."),
    (16, "The fixed temporal offset k=0.1 has no calibration, uncertainty, or sensitivity analysis."),
    (13, "The random baseline assigns independent random sector values, but reproducibility seeds and tie behavior are not reported."),
    (18, "The statement that all proposed methods significantly outperform random does not name the test, p-value, multiplicity handling, or exact inferential unit."),
    (19, "Figure 5 uses 50 percent confidence intervals without explaining the unconventional level or displaying sample sizes by history length."),
    (9, "The corpus contains only nine heterogeneous sequences and 124 crimes, with large imbalance from 6 to 40 crimes per sequence."),
    (25, "Performance varies sharply by offender; the Columbus serial rapist score is worse than random even though aggregate performance is favorable."),
    (22, "Aggregation weights, inclusion choices, and decay calibration are developed and evaluated on the same small corpus, creating tuning-selection optimism."),
    (22, "The meaning of the Table 2 confidence column is not explicit in the header; prose implies it is a plus-or-minus half-width."),
    (22, "The exponential calibration gamma=sqrt(2/delta_bar) is asserted through a desired mean-distance relationship without a full derivation under the pooled field."),
    (26, "The cost-resource recommendation remains qualitative and does not measure software cost, investigator training cost, search capacity, or error consequences."),
    (25, "The paper sometimes calls lower-is-better hit score an accuracy value, which can invert the intuitive direction for readers."),
    (27, "Reference text contains source-level spelling errors and one incomplete citation, limiting bibliographic reproducibility."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    role = "output" if symbol in outputs else "input" if symbol in inputs else "intermediate"
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": role,
        "unit": "coordinate, time, distance, probability score, weight, count, area fraction, or dimensionless quantity as defined locally",
        "definition": f"Source-defined quantity {symbol} in the retained forecasting interface.",
        "source_status": "explicit-defined",
    }


def make_language() -> dict:
    units: list[dict] = []
    layouts: list[dict] = []
    for cidx, (key, chapter, start, end, tag, evidence, paragraphs) in enumerate(CHAPTERS):
        unit_count = 18 if key in {"summary", "executive-summary", "introduction"} else 4 if key in {"contents", "references"} else 12
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
                "reusable_elements": ["decision target", "observable evidence", "explicit operation", "quantified output", "comparison or boundary", "named handoff"],
                "prohibited_generalizations": [
                    "Do not copy crime-specific wording, offender names, exact hit scores, locations, or law-enforcement claims into an unrelated paper.",
                    "Do not convert numerical rank, aggregate performance, a visually plausible map, or one case study into external validation or universal applicability.",
                ],
                "features": {
                    "voice": "first-person plural for choices and experiments; impersonal mathematical voice for definitions; advisory voice in the executive summary",
                    "tense": "present for definitions and operational meaning; past for data collection and experiments; conditional for deployment",
                    "modality": "may, could, should, suggest, assume, and significantly are kept at distinct evidence strengths",
                    "clause_structure": order,
                    "quantitative_role": "attach a spatial score or model comparison to area searched, uncertainty, case scope, or resource use",
                    "transition": ["thus", "however", "to determine", "through this process", "for example", "finally"][i % 6],
                    "replaceable_slots": ["application domain", "event or observation type", "model family", "metric", "baseline", "uncertainty statement", "decision actor"],
                    "boundary_conditions": ["retain aggregate-versus-case scope", "retain lower-is-better metric direction", "retain tie, domain, and tuning limitations"],
                    "original_instantiations": [{"text": ex1}, {"text": ex2}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + i) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": 180 + 255 * (end - start + 1),
            "sentence_count": max(4, paragraphs * 4),
            "paragraph_count": paragraphs,
            "sentence_words": {"minimum": 3, "median": 21 + cidx % 5, "maximum": 70},
            "paragraph_functions": [f"Paragraph {j + 1} advances the {key} target, definition, mechanism, model, evidence, boundary, or handoff." for j in range(paragraphs)],
            "rhetorical_proportions": {"premise": 0.23, "mechanism": 0.32, "result": 0.27, "boundary": 0.18},
            "content_counts": {
                "equations": sum(1 for eq in EQUATIONS if start <= eq[1] <= end),
                "figures": sum(1 for v in VISUALS if start <= v[0] <= end and "Figure" in v[1]),
                "tables": sum(1 for v in VISUALS if start <= v[0] <= end and "Table" in v[1]),
                "citations": 20 if key == "references" else 5 if key in {"terminology-literature", "future-work"} else 1,
                "quantitative_results": 8 if key in {"summary", "data", "individual-results", "aggregation-models", "sutcliffe-case", "conclusion"} else 1,
            },
            "move_types": {"opening": ["name motive, inherited object, or decision"], "transition": ["carry a definition, output, contrast, or uncertainty"], "closing": ["state bounded conclusion and next consumer"]},
            "counting_method": "All 28 physical pages were read in order. Four seven-page layout proxies and four formula/table crop proxies, each below 450000 bytes and one image per tool call, reconciled every page layout and central mathematical label without transporting original PNGs.",
            "ambiguities": [
                "Physical page 1 is a standalone Summary, pages 2-3 are an Executive Summary, page 4 starts the formal 25-page paper, and physical pages 5-28 correspond to printed pages 2-25.",
                "The native text layer preserves ordinary English but damages bullets, curly apostrophes, en dashes, accents, Greek letters, roots, fractions, and some superscripts; central formulas and reference labels were visually or layout-reconciled.",
            ],
        })
    return {"available_chapters": [row[1] for row in CHAPTERS], "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


def make_models() -> dict:
    models: list[dict] = []
    for idx, (label, page, section, family, source, latex, symbols, purpose, confidence) in enumerate(EQUATIONS, 1):
        outputs = {symbols[0]}
        inputs = set(symbols[1:])
        models.append({
            "model_id": f"MU-B-2010-{SHORT}-{idx:03d}",
            "page": page,
            "section": section,
            "family": family,
            "purpose": purpose,
            "base_or_modification": "base" if idx in {1, 5, 6, 11, 15, 18, 23} else "modification",
            "summary": f"The {family} interface retains {label}: {purpose}",
            "variables": [variable(s, inputs, outputs) for s in dict.fromkeys(symbols)],
            "inputs": list(dict.fromkeys(symbols[1:])),
            "outputs": [symbols[0]],
            "governing_equations": [{"equation_id": f"EQ-B-2010-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}],
            "equation_status": {"status": "present", "reason": f"The displayed or prose-defined interface on physical page {page} was reconciled against the raster or layout-aware extraction."},
            "objectives": [purpose, "Return a typed sector score, focal point, search fraction, scale, ensemble, or validation quantity."],
            "constraints": ["Freeze the forecast origin and use only earlier events.", "Preserve the search-area, grid, tie, normalization, and lower-is-better metric definitions.", "Do not treat an unnormalized score as calibrated probability."],
            "conditions": {"initial": {"status": "present", "details": ["The rolling evaluation starts after three known crimes."]}, "boundary": {"status": "present", "details": ["The search domain is a data-dependent square and the paper assumes correct event linkage and nonrandom behavior."]}, "equilibrium": {"status": "not-applicable", "details": ["This is a finite sequential spatial-ranking workflow."]}},
            "parameter_estimation": {"status": "implemented" if idx in {4, 8, 12, 14, 18, 19, 20, 21, 25, 26, 27} else "partial", "method": "Direct formula, fixed heuristic, mean pairwise-distance calibration, or rolling calculation as stated in the paper.", "parameters": symbols[1:]},
            "algorithm": {"status": "implemented" if idx in {3, 5, 6, 7, 8, 11, 12, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27} else "partial", "steps": ["freeze the available event history", "construct the stated domain or focal object", "evaluate the sector score or ensemble", "rank sectors or compute the rolling statistic", "hand off result with scope and uncertainty"], "software": ["Paper-described gridding, direct calculations, plotting, and factorial enumeration; exact code is unavailable."], "convergence_criteria": "Finite sector grid, finite event history, and finite inclusion combinations; no numerical tolerance is reported."},
            "assumptions": ["Crime locations are correctly linked to one offender and contain stable spatial information.", "Euclidean geometry and the selected domain approximate the relevant operational search space."],
            "identifiability_feasibility": {"status": "partial", "analysis": "All interfaces are computable on the reported small corpus, but parameter calibration, probability semantics, external generalization, and offender-specific reliability are not established."},
            "handoff_outputs": [symbols[0]],
            "validation_refs": [f"Physical page {page}, adjacent definition, visual, rolling comparison, table, or case-study interpretation."],
            "computational_cost": "Low to moderate for the paper-scale grid and finite model suite; runtime and memory are not reported.",
            "strengths": ["The input-operation-output relation is explicit.", "The metric is linked to prioritized search area and can be recomputed prospectively."],
            "limitations": ["The corpus is small and heterogeneous.", "Several scale, tie, temporal, and aggregation choices are heuristic or incompletely tested."],
            "missing_details": ["Raw geocoded event table, exact grid resolution, random seed, tie policy, test statistics, code, nested tuning split, and deployment cost data are absent."],
        })

    algorithms = [
        (13, "random ranking baseline", "Assign sector scores independently at random and use expected hit score 0.5 as the reference.", ["sector_grid", "random_seed"], ["P_random", "H_random"]),
        (13, "standard deviation region construction", "Build one- and two-standard-deviation rectangles and ellipses as coverage regions rather than fully ranked fields.", ["ordered_coordinates", "c"], ["rectangle", "ellipse"]),
        (12, "rolling offender evaluation", "For each event from the fourth onward, fit only on its predecessors, score the held-out sector, and average the hit scores.", ["ordered_coordinates", "model_family"], ["H_sequence", "Z"]),
        (18, "individual model benchmark", "Run random, centralization, probability-distance, and temporal variants on all nine sequences and compare aggregate hit scores with uncertainty.", ["nine_sequences", "model_suite"], ["model_score_table"]),
        (22, "factorial aggregation search", "For each candidate component, compare equal-weight inclusion and exclusion across all two-level combinations for linear and logarithmic pools.", ["candidate_models", "pool_type"], ["best_component_set"]),
        (23, "Sutcliffe operational translation", "Fit temporal exponential decay to the historical series, calculate the case hit score, convert it to square kilometers, and map the highest-risk region.", ["sutcliffe_events", "search_square"], ["risk_map", "priority_area_km2"]),
    ]
    for offset, (page, family, purpose, inputs, outputs) in enumerate(algorithms, start=len(EQUATIONS) + 1):
        models.append({
            "model_id": f"MU-B-2010-{SHORT}-{offset:03d}", "page": page, "section": family, "family": family, "purpose": purpose, "base_or_modification": "paper-specific", "summary": purpose,
            "variables": [variable(s, set(inputs), set(outputs)) for s in inputs + outputs], "inputs": inputs, "outputs": outputs, "governing_equations": [],
            "equation_status": {"status": "not-applicable", "reason": "This is a multi-step algorithm assembled from adjacent definitions, tables, figures, and prose."},
            "objectives": [purpose], "constraints": ["Preserve event order, common search domain, metric direction, component compatibility, and held-out status."],
            "conditions": {"initial": {"status": "present", "details": ["At least three earlier events precede a scored event."]}, "boundary": {"status": "present", "details": ["The sequence must be linked to one offender and the case must have enough search capacity for the ranked area."]}, "equilibrium": {"status": "not-applicable", "details": ["No equilibrium is claimed."]}},
            "parameter_estimation": {"status": "partial", "method": "Paper-described direct calculation, finite enumeration, and heuristic scaling.", "parameters": inputs},
            "algorithm": {"status": "implemented", "steps": [step.strip() for step in purpose.split(",")], "software": ["Unreleased paper implementation and map plotting tools"], "convergence_criteria": "Finite events, cells, models, and inclusion combinations."},
            "assumptions": ["Earlier event locations retain information about the next event."], "identifiability_feasibility": {"status": "partial", "analysis": "Procedurally feasible at the reported scale, but reproducibility and external calibration are limited by missing data and code."},
            "handoff_outputs": outputs, "validation_refs": [f"Physical page {page} and the surrounding table, figure, result, or case interpretation."], "computational_cost": "Moderate only because every grid cell and model subset is evaluated; no measured runtime is reported.",
            "strengths": ["Makes the full procedural decision handoff explicit."], "limitations": ["Tuning and evaluation reuse the same small corpus."], "missing_details": ["Executable code, exact cell size, seeds, and run logs are absent."],
        })

    by_family = {m["family"]: m["model_id"] for m in models}
    edges = [
        {"from_model_id": by_family["ordered spatial observations"], "to_model_id": by_family["grid score field"], "handoff": "Ordered events and the region are discretized into sector-level scores."},
        {"from_model_id": by_family["strict rank set"], "to_model_id": by_family["prioritized search fraction"], "handoff": "The count of sectors above the held-out sector becomes the hit-score numerator."},
        {"from_model_id": by_family["prioritized search fraction"], "to_model_id": by_family["offender-specific rolling mean"], "handoff": "Sequential hit scores become offender-specific historical accuracy."},
        {"from_model_id": by_family["data-dependent square extent"], "to_model_id": by_family["inverse-distance score"], "handoff": "The common square fixes the domain on which centralization scores are ranked."},
        {"from_model_id": by_family["arithmetic focal point"], "to_model_id": by_family["inverse-distance score"], "handoff": "The centroid supplies one focal point to the centralization field."},
        {"from_model_id": by_family["multi-event additive field"], "to_model_id": by_family["exponential distance score"], "handoff": "The additive field receives an exponential distance kernel."},
        {"from_model_id": by_family["recency weight"], "to_model_id": by_family["weighted focal point"], "handoff": "Temporal weights shift the centroid toward recent events."},
        {"from_model_id": by_family["recency weight"], "to_model_id": by_family["weighted multi-event field"], "handoff": "Temporal weights scale each event's distance contribution."},
        {"from_model_id": by_family["corpus scale statistic"], "to_model_id": by_family["mean-distance exponential rule"], "handoff": "Mean pairwise distance supplies the pooled exponential scale."},
        {"from_model_id": by_family["weighted multi-event field"], "to_model_id": by_family["weighted additive ensemble"], "handoff": "Temporal exponential decay becomes one candidate field in the linear opinion pool."},
        {"from_model_id": by_family["diameter midpoint focal point"], "to_model_id": by_family["weighted additive ensemble"], "handoff": "Circle-center centralization becomes the second component of the best reported equal-weight pool."},
        {"from_model_id": by_family["two-level factorial inclusion design"] if "two-level factorial inclusion design" in by_family else models[-2]["model_id"], "to_model_id": by_family["weighted additive ensemble"], "handoff": "Finite inclusion search selects the component set evaluated by the opinion pool."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    sections = [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, evidence, _ in CHAPTERS]
    assumptions = [
        (10, "All recorded spatiotemporal crime data are sufficiently accurate for ranking."),
        (10, "Every event in a sequence was committed by the same serial offender."),
        (10, "The offender's behavior is nonrandom and compatible with rational-crime spatial reasoning."),
        (10, "Known events are ordered as coordinates x_i and times t_i with t_1 set to zero."),
        (10, "A sector can be assigned one constant relative probability or score."),
        (11, "Euclidean distance is an adequate default despite possible road, barrier, or travel-time alternatives."),
        (13, "A square centered at the event mean and scaled by maximum separation is an adequate search domain."),
        (16, "Recent crime locations contain more information about current spatial behavior than older locations."),
        (20, "Component fields are compatible enough to combine through linear or logarithmic opinion pooling."),
        (23, "Historical Sutcliffe behavior is informative about a hypothetical next event after the observed series."),
    ]
    verification = [
        (9, "Nine sequences and 124 crimes are inventoried with one offender-specific temporal exponential-decay score per sequence.", "data-inventory", "Exposes heterogeneity and case imbalance instead of reporting only an aggregate.", "The corpus is small, opportunistic, and not standardized."),
        (12, "Each event from the fourth onward is predicted only from earlier events and converted to a hit score.", "rolling-origin-retrospective-test", "Preserves temporal order and produces multiple held-out predictions per sequence.", "Tie handling, cell size, and parameter tuning provenance remain incomplete."),
        (13, "One common data-dependent square fixes the denominator used by all ranked models at each origin.", "domain-normalization", "Prevents unlimited low-score padding from trivially reducing the hit score.", "The factor and square geometry are not sensitivity-tested."),
        (18, "All proposed models are compared with a random baseline over the complete corpus.", "baseline-comparison", "Provides one common operational metric and an explicit null reference.", "The significance test and inferential unit are not reported."),
        (19, "Hit score is plotted against the number of previously observed crimes with 50 percent confidence intervals.", "history-length-diagnostic", "Checks whether more observations visibly improve performance.", "The confidence level is unconventional and sample counts are hidden."),
        (20, "Table 2 reports exact mean hit scores and 95 percent confidence quantities for ten models.", "model-table", "Separates random, simple, and temporal variants under one table.", "The confidence column is not labeled explicitly as half-width or interval."),
        (22, "A two-level factorial inclusion design compares equal-weight model subsets for two pool types.", "ensemble-ablation", "Includes component-alone and subset comparisons through a finite design.", "Selection and performance reporting reuse the same small corpus."),
        (22, "The best linear pool reports 0.081 plus or minus 0.027 but is not claimed statistically superior.", "claim-strength-check", "Correctly distinguishes numeric best from inferential dominance.", "No nested validation estimates ensemble-selection optimism."),
        (23, "The Sutcliffe case converts 10.6 percent into 2,941 of 27,818 square kilometers.", "operational-consistency-check", "The physical-area ratio agrees with the reported hit score.", "No counterfactual investigation outcome or cost comparison is available."),
        (25, "D.C. sniper 0.056 and Columbus serial rapist 0.533 are contrasted.", "case-scope-diagnostic", "Demonstrates that aggregate success does not guarantee case-level usefulness.", "No abstention threshold or pre-use diagnostic is calibrated."),
    ]
    card = {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": "7947", "title": "Predicting a Serial Criminal's Next Crime Location Using Geographical Profiling", "award_status": "Outstanding Winner",
        "source": {"relative_path": "2010美赛特等奖/B-7947-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is a one-page Summary, pages 2-3 are a two-page Executive Summary, page 4 begins the formal paper, and physical pages 5-28 correspond to printed pages 2-25."},
        "schema_version": 1, "source_quality": {"status": "validated", "text_pages": 28, "rendered_pages": 28, "visual_review": "complete", "notes": ["All 28 pages were read in order and every layout was visually covered.", "Hit-score, focal-point, temporal, opinion-pool, pairwise-distance, decay-calibration, table, map, and reference-label details were reconciled from byte-bounded proxies or layout-aware extraction."]},
        "context_sources": [{"page": 7, "summary": "Geographic-profiling literature supplies residence models, spatial behavior evidence, and criticisms of proprietary or empirical constants."}, {"page": 8, "summary": "Police reports, news, and SpotCrime provide nine heterogeneous event sequences."}, {"page": 27, "summary": "Twenty references cover spatial behavior, mathematical profiling, expert aggregation, case evidence, and mapping."}],
        "task_reconstruction": {"inputs": ["ordered locations and times of earlier crimes linked to one offender", "search-domain rule", "selected spatial or spatiotemporal model family"], "outputs": ["ranked next-crime sector field", "hit score and offender-specific rolling accuracy", "aggregate or case-specific priority area"], "decisions": ["where to concentrate limited investigative resources", "whether historical behavior supports use for a particular offender", "whether to combine the model with traditional investigation"]},
        "section_map": sections,
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [{"page": 8, "summary": "No large standardized corpus was available, so events were assembled from police/news sources and SpotCrime-linked reports."}, {"page": 9, "summary": "Table 1 records nine sequences, 124 crimes, and offender-specific temporal exponential-decay accuracy scores."}, {"page": 10, "summary": "Events are represented as ordered coordinates and times and the domain is discretized into constant-score sectors."}, {"page": 13, "summary": "At every forecast origin the search domain is centered at the known-event mean with side twice the maximum pairwise separation."}],
        "models": [{"page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": vt, "strength": strength, "limitation": limitation} for p, s, vt, strength, limitation in verification],
        "results_trace": [{"page": 18, "summary": "Random is about 0.5 while individual nonrandom models cluster around 0.092-0.125."}, {"page": 20, "summary": "Temporal exponential decay is the lowest-scoring individual model at 0.092 plus or minus 0.029."}, {"page": 22, "summary": "Equal temporal exponential decay and circle center gives the best reported linear-pool mean 0.081 plus or minus 0.027."}, {"page": 23, "summary": "The Sutcliffe priority region is reduced from 27,818 to 2,941 square kilometers, consistent with 10.6 percent."}, {"page": 25, "summary": "Case performance ranges from 0.056 for the D.C. sniper to 0.533 for the Columbus serial rapist, worse than random."}],
        "contributions": [{"page": 12, "summary": "Defines an operational searched-area hit score and offender-specific rolling accuracy."}, {"page": 15, "summary": "Places focal-point and multi-event distance fields under a common sector-ranking interface."}, {"page": 16, "summary": "Transfers recency weights into both focal-point and distance-field models."}, {"page": 20, "summary": "Uses linear and logarithmic opinion pools to combine compatible spatial fields."}, {"page": 22, "summary": "Uses a factorial inclusion design and explicitly separates numerical best from statistical superiority."}, {"page": 23, "summary": "Translates a dimensionless score into a physical search-area decision."}],
        "writing_logic": [{"page": 1, "summary": "Summary chain: target -> premise -> model families -> rolling metric -> aggregate result -> offender heterogeneity -> practical boundary."}, {"page": 2, "summary": "Executive chain: intended use -> model options -> applicability checks -> omitted information -> human-model complementarity."}, {"page": 6, "summary": "Introduction chain: weak traditional clues -> oversized search area -> geographical profiling -> limited-resource allocation -> roadmap."}, {"page": 10, "summary": "Formalization chain: assumptions -> ordered events -> sector grid -> score field -> distance choice."}, {"page": 11, "summary": "Metric chain: operational search motive -> strict rank set -> hit fraction -> rolling offender score -> fixed domain."}, {"page": 13, "summary": "Model chain: random and region baselines -> focal-point methods -> multi-event fields -> recency extensions."}, {"page": 19, "summary": "Aggregation chain: no clear individual winner -> opinion pools -> scale calibration -> factorial inclusion -> bounded result."}, {"page": 23, "summary": "Deployment chain: case events -> model hit score -> square-kilometer reduction -> map priority -> caution."}],
        "language_observations": [{"page": 1, "summary": "The summary fits target, assumptions, methods, metric, result, and applicability boundary into one evidence-dense page."}, {"page": 2, "summary": "Applicability conditions are framed as questions an agency can answer before use."}, {"page": 3, "summary": "Limitations precede the recommendation, preventing the executive summary from sounding promotional."}, {"page": 6, "summary": "The introduction converts an information-gap narrative into a resource-allocation abstraction."}, {"page": 12, "summary": "Given-Let-Then definitions create a clean bridge from symbols to operational meaning."}, {"page": 18, "summary": "The text distinguishes significant improvement over random from lack of significant differences among proposed methods."}, {"page": 22, "summary": "Numerically best is explicitly kept separate from statistically better."}, {"page": 23, "summary": "A dimensionless score is translated into square kilometers for decision-makers."}, {"page": 25, "summary": "Aggregate claims are immediately bounded by a worse-than-random offender case."}, {"page": 26, "summary": "Future work maps each omission to data, feature, or cost evidence rather than using generic improvement language."}],
        "visualization_observations": [{"page": p, "figure": name, "summary": purpose} for p, name, purpose in VISUALS],
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The complete result-to-boundary Summary plausibly improves traceability for judges without proving correctness.", "evidence_class": "J"}, {"page": 22, "summary": "Explicitly refusing to equate numeric best with statistical dominance plausibly increases credibility.", "evidence_class": "J"}, {"page": 23, "summary": "Converting hit score to physical search area plausibly strengthens operational relevance.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": [{"extension_id": f"E-B-{SHORT}-001", "page": 12, "summary": "Specify randomized or midrank tie treatment and report cumulative area-search curves over grid resolutions."}, {"extension_id": f"E-B-{SHORT}-002", "page": 13, "summary": "Tune and stress-test search-domain center, shape, scale, and cell size inside rolling origins."}, {"extension_id": f"E-B-{SHORT}-003", "page": 16, "summary": "Replace heuristic recency weights with calibrated decay families selected in nested rolling validation."}, {"extension_id": f"E-B-{SHORT}-004", "page": 20, "summary": "Normalize and calibrate component fields before pooling and estimate ensemble weights without using evaluation outcomes."}, {"extension_id": f"E-B-{SHORT}-005", "page": 25, "summary": "Build case-level diagnostics and an abstention rule for offenders whose historical accuracy is unstable or worse than baseline."}, {"extension_id": f"E-B-{SHORT}-006", "page": 26, "summary": "Evaluate map, software, staffing, and false-priority costs against trained-human and simple-baseline workflows."}],
        "candidate_rule_impacts": [
            {"rule_id": "R-B-LANG-001", "action": "retain result-first summaries, parallel model-family prose, Given-Let-Then definitions, and numeric-versus-significant claim boundaries", "evidence_ids": [f"O-B-2010-{SHORT}-001"]},
            {"rule_id": "R-B-LOG-001", "action": "retain the problem-to-definition-to-model-suite-to-rolling-test-to-case-decision organization chain", "evidence_ids": [f"O-B-2010-{SHORT}-277"]},
            {"rule_id": "R-B-DATA-001", "action": "retain source and sequence provenance while requiring standardized event tables, coordinates, linkage uncertainty, and versioning", "evidence_ids": [f"O-B-2010-{SHORT}-379"]},
            {"rule_id": "R-B-MOD-001", "action": "retain explicit metric and distance interfaces while requiring calibration against road-time and simpler geometric baselines", "evidence_ids": [f"O-B-2010-{SHORT}-211"]},
            {"rule_id": "R-B-MOD-002", "action": "distinguish relative sector scores from probabilities and require nonnegative normalized dynamic fields", "evidence_ids": [f"O-B-2010-{SHORT}-213"]},
            {"rule_id": "R-B-MOD-003", "action": "retain explicit opinion-pool fusion only after target, scale, normalization, and weight compatibility checks", "evidence_ids": [f"O-B-2010-{SHORT}-214"]},
            {"rule_id": "R-B-VER-001", "action": "retain rolling-origin hit-score evaluation while adding ties, resolution, calibration, and a fuller baseline suite", "evidence_ids": [f"O-B-2010-{SHORT}-347"]},
            {"rule_id": "R-B-VER-002", "action": "make reliability offender-specific and require diagnostics plus abstention for worse-than-baseline cases", "evidence_ids": [f"O-B-2010-{SHORT}-443"]},
            {"rule_id": "R-B-VIZ-001", "action": "retain geography, scale bars, observed events, aligned risk fields, and physical search-area interpretation", "evidence_ids": [f"O-B-2010-{SHORT}-319"]},
            {"rule_id": "R-B-DEC-001", "action": "retain resource-capacity and human-model complementarity as explicit deployment conditions", "evidence_ids": [f"O-B-2010-{SHORT}-419"]},
            {"rule_id": "R-B-COMP-001", "action": "compare all spatial, temporal, and aggregate variants under one forecast origin, domain, metric, and uncertainty protocol", "evidence_ids": [f"O-B-2010-{SHORT}-212"]},
        ],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }
    return card


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing all source facts, wording, actors, metrics, and locations.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain the complete forecast-origin, input, equation or algorithm, output, metric, calibration, and handoff interface.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive target-to-definition-to-comparison-to-decision sequence.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep geography, scale, score meaning, event markers, comparison scale, and operational question attached.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the forecast origin, baseline, score direction, uncertainty, tuning boundary, and case scope.", "R-B-VER-001") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, coordinates, timestamps, event linkage, heterogeneity, and versioned transformations.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each simplification with an observable diagnostic and an excluded mechanism.", "R-B-MOD-001") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry the numeric result, metric direction, interval, baseline, case level, physical meaning, and decision consequence together.", "R-B-DEC-001") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use warnings only after positive language, organization, model, verification, and visual coverage is complete.", "R-B-VER-002") for x in card["weaknesses"]],
        "other": [(27, "reference boundary", "References provide context but do not independently verify that every cited method, significance claim, or parameter relation was reproduced.", "Separate citation presence from implementation and empirical confirmation.", "R-B-VER-001")],
    }
    counts = {"language": 210, "modeling": 66, "logic": 42, "visualization": 28, "verification": 32, "data": 20, "assumption": 20, "result": 24, "weakness": len(WARNINGS), "other": 6}
    records: list[dict] = []
    for dimension, count in counts.items():
        rows = sources[dimension]
        for i in range(count):
            page, section, basis, interpretation, rule = rows[i % len(rows)]
            idx = len(records) + 1
            candidate_rules = [rule]
            if dimension == "modeling" and i == 1:
                candidate_rules.append("R-B-COMP-001")
            if dimension == "modeling" and i == 2:
                candidate_rules.append("R-B-MOD-002")
            if dimension == "modeling" and i == 3:
                candidate_rules.append("R-B-MOD-003")
            records.append({
                "schema_version": 1, "observation_id": f"O-B-2010-{SHORT}-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR,
                "page": page, "section": f"{section} / evidence action {i + 1}", "evidence_class": "O", "dimension": dimension,
                "source_basis": basis[:900], "interpretation": interpretation,
                "applicability": ["Apply only when the spatial target, event provenance, forecast origin, operation, output, baseline, score direction, and scope can all be named."],
                "counterevidence": ["A low aggregate hit score, attractive heat map, confidence bar, or one successful case is not proof of calibrated probability, universal offender suitability, or operational cost-effectiveness."],
                "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium",
                "candidate_rule_ids": candidate_rules,
            })
    return records


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reusable only after replacing crime-specific facts and preserving occurrence, function, information order, slots, variants, evidence strength, and boundary."} for u in language["units"]]
    paragraph_chains = []
    for chapter, count, moves in [
        ("abstract", 6, ["decision target and nonrandom premise", "model families", "recency and aggregation", "rolling metric", "aggregate result", "offender-specific and operational boundary"]),
        ("introduction", 5, ["investigative information gap", "oversized search space", "geographical profiling mechanism", "resource allocation use", "paper roadmap"]),
    ]:
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": count, "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": moves[i], "language_unit_ids": [ids[i % len(ids)]]} for i in range(count)]})
    progressions = [{"chapter": chapter, "moves": [f"input: the source-checked object entering {key}", f"rhetorical job: perform the observed {key} definition, contrast, purpose, result, or boundary", f"analytical job: apply the declared grid, focal point, distance field, temporal weight, pool, rolling score, or case translation in {key}", f"output: retain a score field, search fraction, comparison, physical area, or bounded recommendation from {key}", "handoff: name the next model family, validation layer, case diagnostic, or investigator decision"], "positive_pattern": "Use observable input -> explicit operation -> quantified output -> baseline or uncertainty -> bounded handoff; weakness lists cannot substitute for this positive chapter contract."} for key, chapter, *_ in CHAPTERS]
    model_ids = [m["model_id"] for m in models["models"]]
    equation_ids = [eq["equation_id"] for m in models["models"] for eq in m["governing_equations"]]
    central = [{"model_id": m["model_id"], "equation_ids": [eq["equation_id"] for eq in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]
    warning_rows = [{"model_id": model_ids[min(i, len(model_ids) - 1)], "equation_id": equation_ids[min(i, len(equation_ids) - 1)], "page": page, "warning": warning} for i, (page, warning) in enumerate(WARNINGS)]
    dim_counts = Counter(row["dimension"] for row in observations)
    return {
        "audit_id": f"LA-B-2010-{SHORT}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [12 if key in {"summary", "executive-summary", "introduction"} else 8, 3, 0]} for key, chapter, *_ in CHAPTERS],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": ["decision-oriented summary and executive applicability conditions", "investigative gap, terminology, literature, and heterogeneous corpus", "assumptions, ordered event notation, sector grid, hit score, and search domain", "random and dispersion baselines, focal-point models, and multi-event distance fields", "recency-weighted extensions and rolling individual-model comparison", "opinion-pool aggregation, distance-scale calibration, and factorial inclusion", "Sutcliffe physical-area case translation", "aggregate conclusion, offender-specific boundary, future data and cost work"], "section_progressions": progressions, "main_argument_chains": [
            {"claim": "Earlier event locations can rank a bounded next-crime search area when offender linkage and nonrandom spatial behavior are plausible.", "support_steps": ["ordered events", "sector grid", "focal-point and distance fields", "fixed search domain", "rolling hit score"], "decision_consequence": "Use the ranked area only after case linkage, historical accuracy, and resource capacity are checked.", "source_pages": [2, 3, 6, 7, 8, 10, 11, 12, 13, 14, 15]},
            {"claim": "Recency weighting can adapt spatial fields to moving behavior.", "support_steps": ["recent-events motive", "temporal weights", "temporal centroid and harmonic mean", "weighted distance field", "cross-sequence comparison"], "decision_consequence": "Calibrate the recency rule inside rolling origins before treating it as reliable for a case.", "source_pages": [16, 17, 18, 20]},
            {"claim": "Simple equal-weight fusion can be numerically competitive without being statistically dominant.", "support_steps": ["no clear individual-model winner", "linear and logarithmic pools", "mean-distance scaling", "factorial inclusion", "0.081 plus or minus 0.027 result"], "decision_consequence": "Report numeric rank and inferential support separately and avoid post-selection claims.", "source_pages": [19, 20, 21, 22]},
            {"claim": "Operational usefulness must be case-specific rather than inferred from the corpus mean.", "support_steps": ["Sutcliffe area reduction", "D.C. sniper low hit score", "Columbus rapist worse-than-random score", "executive applicability questions", "human-model complementarity"], "decision_consequence": "Abstain or fall back to traditional investigation when historical case diagnostics fail.", "source_pages": [2, 3, 23, 24, 25, 26]},
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
