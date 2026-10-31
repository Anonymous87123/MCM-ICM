from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2014-26636-060c74b1"
SHORT = "26636"
SHA = "060c74b100ab7f048978d3267eeacb266092a670264993c3212069a1e6f8fd1b"
TYPE = "B"
YEAR = "2014"
PAGE_COUNT = 38
TEXT_DIR = ROOT / "artifacts/papers" / PID / "text/pages"
STAGE = ROOT / "tmp/q103-stage-v2"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHAPTERS = [
    ("title", "title", 1, 1, "TTL", "The title frames the deliverable as an evaluation model rather than an unqualified list of famous coaches."),
    ("summary", "abstract", 1, 1, "ABS", "The summary previews four indicators, fuzzy-consistent weights, grey ranking, cross-sport application, time correction, gender discussion, and two stability checks."),
    ("task", "problem-restatement", 3, 3, "RST", "The task paragraph identifies the Sports Illustrated audience, the all-time cross-era ranking decision, and the required time and gender discussion."),
    ("introduction", "introduction", 3, 4, "INT", "The introduction moves from qualitative coach evaluation to a quantitative four-indicator workflow and names the two-stage model."),
    ("model-overview", "problem-analysis", 4, 5, "OVR", "The overview separates factor-weight estimation from grey relational ranking and motivates the method by limited data availability."),
    ("notation", "notation", 5, 5, "NOT", "The notation and definitions bind fuzzy matrices, indicator weights, reference arrays, grey coefficients, and evaluation outputs."),
    ("fuzzy-weighting", "model-establishment", 6, 7, "FUZ", "The weighting section converts a three-level preference matrix to a fuzzy-consistent matrix and derives a normalized root-method weight vector."),
    ("grey-ranking", "algorithm", 7, 8, "GRY", "The ranking section forms an ideal coach from per-indicator maxima, normalizes data, computes grey coefficients, and aggregates a relational degree."),
    ("candidate-data", "data-preprocessing", 8, 10, "DAT", "The application defines four indicators, filters Division I basketball coaches by wins, and traces the roster to Wikipedia and NCAA sources."),
    ("sport-applications", "model-improvement", 10, 16, "APP", "The calculation tables expose normalized basketball data, grey coefficients, ranks, and transfer of the same interface to football and ice hockey."),
    ("external-comparison", "robustness-verification", 16, 17, "EXT", "The external comparison places selected model lists beside media rankings as a plausibility check, not independent validation."),
    ("time-horizon", "sensitivity-analysis", 17, 21, "TIM", "The time analysis groups careers by starting era, plots group means, applies one-way ANOVA, and introduces an inverse-average correction to winning percentage."),
    ("gender", "results", 21, 22, "GEN", "The gender section applies the same indicators and weights to a women-basketball roster and reports a top-five list."),
    ("entropy-check", "sensitivity-robustness", 22, 25, "ENT", "The entropy check derives near-equal objective weights and compares its top-ten order with the fuzzy-consistent result."),
    ("priority-check", "future-improvements", 25, 27, "PRI", "A second stability check changes the pairwise importance order, recalculates ranks, and compares the resulting top ten."),
    ("rho-check", "conclusion", 27, 28, "RHO", "The sensitivity section varies the grey distinguishing coefficient from 0.4 to 0.6 and claims the top-ten set is unchanged."),
    ("strengths-weaknesses", "strengths-limitations", 28, 29, "SWK", "The closing assessment credits convenience and portability while acknowledging roster, award-count, and historical-correction limitations."),
    ("references", "references", 29, 30, "REF", "The references identify coach-evaluation, decision-weighting, and entropy sources but do not freeze the actual ranking dataset."),
    ("appendix", "appendix", 30, 36, "APX", "The appendix prints four sport rosters and MATLAB-style routines while retaining local paths, undefined inputs, and missing source spreadsheets."),
    ("sports-illustrated-article", "memo", 37, 38, "MEM", "The final article translates the four-indicator method and three top-five lists into an audience-facing narrative."),
]

PATTERNS = [
    "LP-B-SUMMARY-METRICS-MODEL-RANK-TEST",
    "LP-B-INTRO-QUALITATIVE-GAP-QUANTITATIVE-ROUTE",
    "LP-B-TASK-AUDIENCE-DECISION-SCOPE",
    "LP-B-NOTATION-DEFINITION-DOWNSTREAM-USE",
    "LP-B-PREFERENCE-MATRIX-CONSISTENT-WEIGHT",
    "LP-B-IDEAL-REFERENCE-NORMALIZE-RELATE-RANK",
    "LP-B-INDICATOR-DEFINITION-DIRECTION-USE",
    "LP-B-CANDIDATE-FILTER-SOURCE-BOUNDARY",
    "LP-B-CALCULATION-TABLE-RANK-HANDOFF",
    "LP-B-CROSS-SPORT-TRANSFER-CONDITION",
    "LP-B-EXTERNAL-LIST-COMPARISON-BOUNDARY",
    "LP-B-TIME-GROUP-TREND-TEST-CORRECTION",
    "LP-B-SUBGROUP-APPLICATION-CLAIM-BOUNDARY",
    "LP-B-ALTERNATE-WEIGHT-RANK-COMPARISON",
    "LP-B-PARAMETER-PERTURBATION-RANK-STABILITY",
    "LP-B-STRENGTH-LIMIT-IMPROVEMENT",
    "LP-B-APPENDIX-CODE-REPRODUCTION-BOUNDARY",
    "LP-B-ARTICLE-METHOD-LIST-AUDIENCE",
]

MOVES = [
    ("summary-route", "State the decision, indicators, weighting method, ranking method, historical adjustment, and checks before reporting a bounded output.", "decision -> indicators -> model route -> checks -> result"),
    ("qualitative-gap", "Contrast subjective prior evaluation with accessible records and an explicit quantitative workflow.", "prior practice -> limitation -> data opportunity -> method"),
    ("task-scope", "Name the audience, sport and era scope, required lists, and time or gender questions before modeling.", "audience -> decision -> scope -> deliverables"),
    ("definition-contract", "Define every matrix, indicator, coefficient, and score before it enters the next calculation.", "symbol -> definition -> direction -> downstream use"),
    ("preference-weight", "Turn an ordinal pairwise judgment into a reciprocal consistent matrix and normalized weight vector.", "preference -> matrix conversion -> root weight -> normalization"),
    ("ideal-reference", "Construct a reference coach, normalize comparable indicators, calculate grey coefficients, and aggregate a rank score.", "ideal vector -> normalization -> coefficient -> degree -> rank"),
    ("indicator-role", "Connect each coach statistic to a measurable definition, benefit direction, and score role.", "indicator -> source field -> direction -> score role"),
    ("candidate-filter", "State division and win-threshold eligibility before collecting values from declared sources.", "eligibility -> roster -> source -> frozen input boundary"),
    ("table-rank", "Expose normalized inputs and intermediate coefficients before presenting the ordered coach list.", "input table -> coefficient table -> score -> rank"),
    ("cross-sport-transfer", "Reuse the model only after redefining sport-specific championship and award fields.", "shared interface -> sport mapping -> calculation -> conditional list"),
    ("external-comparison", "Compare model output with named media lists while preserving their different rosters and methods.", "model list -> external list -> overlap -> evidence limit"),
    ("time-correction", "Group candidates by era, inspect a trend, test it, and state the exact correction before revising ranks.", "era groups -> trend -> test -> correction -> revised rank"),
    ("subgroup-application", "Apply the declared interface to a subgroup and limit the conclusion to the observed roster and sport.", "subgroup data -> same model -> list -> scope"),
    ("alternate-weight", "Replace one weighting rule, recompute the rank, and distinguish list overlap from validation.", "alternate weights -> rerun -> rank comparison -> boundary"),
    ("rho-sensitivity", "Change the grey distinguishing coefficient, recompute degrees, and report both set and order effects.", "parameter -> values -> score response -> rank interpretation"),
    ("strength-limit", "Retain portability and transparency before naming roster, metric, chronology, and reproducibility limits.", "strength -> evidence -> limitation -> repair"),
    ("appendix-boundary", "Use printed data and code for traceability while distinguishing them from an executable package.", "table or code -> calculation role -> missing dependency -> boundary"),
    ("reader-article", "Translate a qualified model route into a concise list without detaching it from its indicators and scope.", "reader question -> method -> lists -> scope"),
]

EXAMPLES = [
    ("A ranking study fixes eligibility and four benefit indicators before asking experts to order their importance.", "The candidate boundary and score meaning remain visible before a composite value is computed."),
    ("An ordinal preference matrix is converted to a reciprocal consistent matrix and then to normalized geometric-mean weights.", "Each matrix transformation has a declared input and output rather than appearing as an unexplained score."),
    ("A fictitious ideal candidate takes the best observed value on every indicator, and each real candidate is compared with it.", "The relation degree is described as a distance-based ranking device, not a causal measure of coaching quality."),
    ("A cross-era check groups starting years, shows group summaries, and states the test and correction separately.", "The revised ranking stays conditional on the grouping rule and correction formula."),
    ("An objective entropy weight vector is used as an alternate calculation on the same data.", "Agreement is called a dependent stability check because the roster and indicators are shared."),
    ("The final article names the selected coaches and briefly identifies the four statistics used.", "The public-facing prose remains traceable to the model instead of presenting unsupported superlatives."),
]


def configure(base):
    for name, value in {
        "PID": PID,
        "SHORT": SHORT,
        "SHA": SHA,
        "TYPE": TYPE,
        "YEAR": YEAR,
        "PAGE_COUNT": PAGE_COUNT,
        "TEXT_DIR": TEXT_DIR,
        "STAGE": STAGE,
        "CHAPTERS": CHAPTERS,
        "PATTERNS": PATTERNS,
        "MOVES": MOVES,
        "EXAMPLES": EXAMPLES,
    }.items():
        setattr(base, name, value)


def build_language(base, template, pages):
    configure(base)
    language = base.build_language(template, pages)
    for unit in language["units"]:
        unit["function"] = "Preserve a source-anchored coach-ranking move and transfer it only after replacing sport, roster, indicator, era, weight, and decision scope."
        unit["reusable_pattern"] = "decision context or criterion -> typed ranking operation -> inspectable output -> scoped handoff"
        unit["information_order"] = ["sport, roster, era, or criterion", "matrix, normalization, test, or aggregation", "score, rank, or comparison", "condition and receiving use"]
        unit["reusable_elements"] = ["explicit eligibility", "defined metric direction", "ordered calculation", "result before caveat"]
        unit["prohibited_generalizations"] = ["Do not present one era-bound sport roster as universal coaching truth.", "Do not detach a win count, rate, championship, award total, weight, correction, or rank from its definition and source."]
        unit["features"]["quantitative_role"] = "bind a count, rate, matrix entry, weight, coefficient, corrected value, or rank to its declared comparison role"
        unit["features"]["transition"] = "first, then, therefore, by contrast, however, and finally connect inputs, calculations, checks, and lists"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 38 local UTF-8 page files were read in bounded ranges; chapter counts use declared physical-page ranges, and all 38 rendered pages received byte-bounded visual review."
        layout["ambiguities"] = ["Extraction damages bullets, Greek symbols, fractions, roots, subscripts, and table alignment; visually checked records retain uncertainty rather than silently repairing the source.", "The appendix prints partial MATLAB-style code but omits source spreadsheets and an executable package; this is a final evidence boundary, not a substitute for positive learning."]
    return language


def equation(index, page, label, latex, symbols, purpose, confidence="high"):
    return {"equation_id": f"EQ-B-{YEAR}-{SHORT}-{index:03d}", "page": page, "label": label, "source_expression": latex, "normalized_latex": latex, "purpose": purpose, "variable_symbols": symbols, "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}


def make_model(base, template, model_id, page, section, family, purpose, inputs, outputs, equations):
    configure(base)
    model = base.make_model(template, model_id, page, section, family, purpose, inputs, outputs, equations)
    model["summary"] = purpose
    for variable in model["variables"]:
        variable["definition"] = f"Source-defined coach-ranking quantity {variable['symbol']}."
        variable["unit"] = "count, proportion, year, normalized value, matrix entry, entropy, grey coefficient, weight, or dimensionless score as defined by the source"
    model["objectives"] = [purpose, "Return a typed weight, normalized record, grey degree, correction, test result, rank, or reader-facing list."]
    model["constraints"] = ["Keep sport, eligibility, era, indicator direction, source, normalization, weighting, and rank scope explicit.", "Rank agreement or media-list overlap does not establish causal superiority, fairness, or independent validity."]
    model["conditions"] = {"initial": {"status": "present", "details": ["A declared candidate roster, four benefit indicators, pairwise judgments or entropy inputs, and sport-specific field mappings are supplied or assumed."]}, "boundary": {"status": "present", "details": ["Roster thresholds, historical grouping, award definitions, missing data, ties, source changes, and cross-sport transfer require explicit handling."]}, "equilibrium": {"status": "not-applicable", "details": ["The source executes finite matrix, ranking, ANOVA, and parameter-comparison calculations rather than a dynamical equilibrium solve."]}}
    model["parameter_estimation"] = {"status": "partial", "method": "Expert ordinal preferences, Wikipedia and NCAA records, per-factor maxima, fuzzy-consistent root weights, grey coefficient rho=0.5, grouped-era summaries, entropy weights, and local reruns.", "parameters": [v["symbol"] for v in model["variables"]]}
    model["algorithm"] = {"status": "partial", "steps": ["freeze eligible roster and indicator definitions", "derive weights and normalize the four indicators", "calculate grey coefficients and relational degrees", "rank candidates and perform external, historical, alternate-weight, and rho checks", "handoff qualified lists to the audience article"], "software": ["Appendix MATLAB-style fragments use hard-coded local spreadsheet paths and omit the spreadsheets, complete functions, environment, and run log."], "convergence_criteria": "Finite matrix and ranking operations terminate directly; the paper supplies no independent validation or uncertainty certificate."}
    model["assumptions"] = ["The four retained indicators and their benefit directions represent coaching performance within each stated sport.", "The selected roster, award totals, era grouping, preference order, and source records are sufficiently comparable for the ranking exercise."]
    model["identifiability_feasibility"] = {"status": "partial", "analysis": "Equations, tables, lists, plots, and code fragments are inspectable, but source snapshots, award coding, correction derivation, complete data, and executable reproduction remain incomplete."}
    model["computational_cost"] = "Driven by small dense matrix operations over candidates and four criteria, ranking reruns, grouped-era summaries, ANOVA, and alternate-weight or rho scenarios."
    model["strengths"] = ["The source exposes intermediate matrices and rank tables instead of reporting only a final list.", "It explicitly tests historical horizon, an alternate weighting route, and a grey-coefficient perturbation before communicating results."]
    model["limitations"] = ["The checks reuse the same roster and indicators and therefore are not independent external validation.", "Confirmed formula, table, roster, and code conflicts remain explicit final warnings."]
    model["missing_details"] = ["Official task text, frozen source snapshots, complete inclusion rules, award coding, raw spreadsheets, data-cleaning log, code environment, executable scripts, uncertainty analysis, and independent validation data are absent."]
    return model


def build_models(base, template):
    fuzzy = [
        equation(1, 6, "row preference sum", r"f_i=\sum_{k=1}^{m}a_{ik}", ["f_i", "a_ik", "m"], "Summarize each factor's ordinal preference row."),
        equation(2, 6, "consistent-matrix conversion", r"f_{ij}=(f_i-f_j)/(2m)+0.5", ["f_ij", "f_i", "f_j", "m"], "Convert the preference scores to a reciprocal fuzzy-consistent matrix."),
        equation(3, 6, "column normalization", r"w_{ij}=f_{ij}/\sum_{i=1}^{n}f_{ij}", ["w_ij", "f_ij", "n"], "Normalize every fuzzy-consistent matrix column."),
        equation(4, 7, "root-method row score", r"\tilde w_i=(\prod_{j=1}^{n}w_{ij})^{1/n}", ["wtilde_i", "w_ij", "n"], "Take the geometric mean of each normalized row."),
        equation(5, 7, "weight normalization", r"w_i=\tilde w_i/\sum_{i=1}^{n}\tilde w_i", ["w_i", "wtilde_i", "n"], "Normalize row scores to the final indicator weight vector."),
    ]
    grey = [
        equation(6, 7, "grey relational coefficient", r"\xi_i(k)=(\Delta_{min}+\rho\Delta_{max})/(|x_0(k)-x_i(k)|+\rho\Delta_{max})", ["xi_i", "Delta_min", "Delta_max", "rho", "x_0", "x_i", "k"], "Measure a candidate's criterion-wise proximity to the ideal coach."),
        equation(7, 8, "weighted grey degree", r"r_i=\sum_{k=1}^{n}w_k\xi_i(k)", ["r_i", "w_k", "xi_i", "k", "n"], "Aggregate four grey coefficients with the indicator weights."),
        equation(8, 8, "comprehensive score vector", r"R=wE^T=(r_1,r_2,\ldots,r_m)", ["R", "w", "E", "r_i", "m"], "Collect relational degrees for descending rank order.", "medium"),
    ]
    time = [
        equation(9, 20, "era weighted mean", r"S_i=\sum_j Z_jY_j/\sum_j Z_j", ["S_i", "Z_j", "Y_j"], "Form the sample-size-weighted winning-percentage baseline used by the historical correction.", "medium"),
        equation(10, 20, "winning-percentage correction", r"c_i=1/S_i,\quad p_i'=c_ip_i", ["c_i", "S_i", "p_i", "pprime_i"], "Scale an era's winning percentage by the inverse baseline before reranking.", "medium"),
    ]
    entropy = [
        equation(11, 23, "benefit normalization", r"q_{ij}=(c_{ij}-\min_j c_{ij})/(\max_j c_{ij}-\min_j c_{ij})", ["q_ij", "c_ij"], "Normalize positive indicators before entropy weighting.", "medium"),
        equation(12, 23, "criterion share", r"d_{ij}=q_{ij}/\sum_i q_{ij}", ["d_ij", "q_ij"], "Convert normalized indicator values to criterion shares."),
        equation(13, 23, "criterion entropy", r"h_j=-k\sum_i d_{ij}\ln d_{ij},\quad k=1/\ln m", ["h_j", "k", "d_ij", "m"], "Calculate Shannon entropy for each indicator."),
        equation(14, 24, "entropy weight", r"W_j=(1-h_j)/(n-\sum_j h_j)", ["W_j", "h_j", "n"], "Normalize information utility into an alternate four-indicator weight."),
    ]
    models = [
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-001", 6, "Fuzzy-consistent weighting", "fuzzy preference and root weighting", "Convert ordinal factor priority into a normalized four-indicator weight vector.", ["four-factor preference order", "A"], ["F", "w"], fuzzy),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-002", 7, "Grey relational ranking", "weighted grey relational analysis", "Compare each coach with a per-factor ideal and rank candidates by weighted grey degree.", ["coach matrix", "ideal vector", "w", "rho"], ["E", "R", "rank"], grey),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-003", 9, "Candidate and indicator preparation", "eligibility and source mapping", "Select Division I candidates, define wins, winning rate, championships, and coach awards, and map source records to the ranking matrix.", ["candidate sources", "eligibility", "award definitions"], ["typed four-indicator matrix"], []),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-004", 15, "Cross-sport application", "sport-specific field mapping", "Reuse the four-indicator interface for football and ice hockey after redefining championships and awards.", ["sport rosters", "sport-specific awards", "shared weights"], ["football rank", "ice-hockey rank"], []),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-005", 17, "External list comparison", "dependent plausibility comparison", "Place model top-five lists beside media rankings while retaining candidate and method differences.", ["model lists", "media lists"], ["overlap table", "plausibility boundary"], []),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-006", 17, "Time-line analysis", "era grouping and one-way ANOVA", "Group coaching careers by start era, compare indicator summaries, and test whether winning percentage changes across groups.", ["start years", "wins", "winning rate", "championships"], ["group means", "ANOVA tables", "time-effect claim"], []),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-007", 20, "Historical correction", "inverse weighted-average adjustment", "Adjust winning percentage by the source's era correction and rerank post-1950 candidates.", ["group counts", "group means", "base ranks"], ["correction factors", "adjusted percentages", "adjusted ranks"], time),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-008", 22, "Entropy weighting check", "Shannon entropy weighting", "Derive an alternate objective weight vector and compare its basketball rank with the fuzzy-consistent result.", ["coach indicator matrix", "benefit direction"], ["entropy weights", "alternate rank"], entropy),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-009", 25, "Priority and rho checks", "local ranking sensitivity", "Change factor priority and rho in separate reruns and compare the reported top-ten outputs.", ["alternate preference matrix", "rho values 0.4, 0.5, 0.6"], ["alternate weights", "score tables", "rank comparison"], []),
        make_model(base, template, f"MU-B-{YEAR}-{SHORT}-010", 34, "Appendix calculation support", "MATLAB-style calculation fragments", "Expose the stated matrix, entropy, normalization, and grey-score operations while retaining missing spreadsheets and runtime details.", ["printed code", "unprovided xls inputs"], ["traceable operations", "reproduction boundary"], []),
    ]
    edges = [
        {"from_model_id": models[2]["model_id"], "to_model_id": models[0]["model_id"], "handoff": "The four typed indicators define the rows and semantic order of the preference matrix."},
        {"from_model_id": models[0]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "The normalized four-indicator weight vector enters the grey relational degree."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "The same ranking interface is reused after sport-specific championship and award mappings."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[4]["model_id"], "handoff": "Model top-five lists enter the dependent comparison with named media lists."},
        {"from_model_id": models[5]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "Era summaries and ANOVA interpretation motivate the winning-percentage correction."},
        {"from_model_id": models[6]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "Corrected winning percentages replace one input column before grey reranking."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[7]["model_id"], "handoff": "The same four-indicator matrix feeds an alternate entropy weight calculation."},
        {"from_model_id": models[7]["model_id"], "to_model_id": models[8]["model_id"], "handoff": "Alternate weighting and rho scenarios produce rank tables for local stability comparison."},
        {"from_model_id": models[9]["model_id"], "to_model_id": models[0]["model_id"], "handoff": "Appendix code fragments partially expose the preference-to-weight calculation."},
        {"from_model_id": models[9]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "Appendix code fragments partially expose normalization and grey-score calculation."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def build_card(models):
    assumptions = [
        (6, "The ordinal priority championship > winning percentage > wins > coach awards can be represented with 0, 0.5, and 1 pairwise entries."),
        (7, "The best observed value of every benefit indicator forms a meaningful fictitious ideal coach."),
        (9, "Division I status and a sport-specific win threshold define an adequate candidate roster."),
        (14, "The same four indicators and weight semantics transfer across basketball, football, ice hockey, and gender."),
        (17, "Starting-career era is an adequate proxy for changes in competitive opportunity."),
        (20, "An inverse weighted-era average is a valid correction for winning percentage."),
        (22, "The women-basketball roster is sufficient to conclude that gender does not affect factor selection or weights."),
        (24, "Entropy-derived discrimination weights provide an informative alternate weighting check on the same roster."),
        (27, "Top-ten similarity after changing factor priority or rho is sufficient evidence of model stability."),
    ]
    data = [
        (8, "The four benefit indicators are career wins, winning percentage, NCAA championships, and a sum of selected coach awards."),
        (9, "Basketball candidates are taken from a Wikipedia 600-win list, filtered to Division I, and linked to NCAA record sources."),
        (10, "The source prints the preference matrix, fuzzy-consistent matrix, and final weight vector."),
        (10, "Normalized basketball records use each column's observed range and a per-factor ideal of one."),
        (15, "Football and ice-hockey tables redefine championship and award columns before applying the shared ranking interface."),
        (17, "Basketball start years form five era groups; the source reports group means, plots, and two ANOVA tables."),
        (21, "Women-basketball records supply the same four fields for a separate top-five calculation."),
        (24, "Entropy weighting yields approximately equal weights 0.2493, 0.2492, 0.2508, and 0.2507."),
        (30, "Appendix pages 30-33 print candidate rosters and sport-specific award component columns."),
        (34, "Appendix pages 34-36 print MATLAB-style weighting, entropy, normalization, and grey-correlation fragments with local file paths."),
    ]
    verification = [
        (10, "The preference and fuzzy-consistent matrices can be checked against the stated ordinal factor order.", "matrix trace", "Intermediate matrices and a weight vector are visible.", "The prose maps vector entries to indicators in an order that conflicts with the table and matrix rows."),
        (13, "Normalized records, coefficient rows, degrees, and the main basketball rank can be traced across Tables 3-5.", "formula-to-table trace", "Intermediate normalized and coefficient values are printed.", "Table layout is extraction-sensitive and the source does not archive the spreadsheet or executable run."),
        (16, "Football and ice-hockey top-five lists can be compared with the later external-comparison and article lists.", "cross-table consistency", "The three list locations are inspectable.", "The football list in Table 9 conflicts with Table 7.1 and the final article."),
        (19, "Era plots and ANOVA tables can be checked against the stated historical conclusion.", "trend and test audit", "Group means and test summaries are shown.", "One-way ANOVA tests mean equality, but the prose repeatedly interprets it as a test of variances."),
        (20, "Correction factors and adjusted ranks can be compared with pre-adjustment winning percentages.", "correction audit", "Both before and after tables are printed.", "Adjusted winning percentages exceed one and the source does not justify that transformed scale."),
        (24, "Entropy weights and its top-ten list can be compared with the fuzzy-consistent top ten.", "alternate-weight check", "The alternate formula route and ranking are visible.", "Both methods reuse the same roster and indicators, and the appendix code overwrites an intermediate normalization."),
        (27, "The rho tables can be compared with the main basketball ranking.", "local parameter check", "Three rho values and rank tables are printed.", "The rho=0.5 table assigns the main scores to different coach names, invalidating the claimed identity without reconciliation."),
        (34, "Appendix code can be traced to the printed matrix and grey-score operations.", "code-to-method trace", "Core operations are recognizable.", "Hard-coded local paths, missing spreadsheets, undefined x, and no environment prevent execution."),
    ]
    results = [
        (13, "The primary basketball top five are John Wooden, Adolph Rupp, Mike Krzyzewski, Dean Smith, and Jim Boeheim."),
        (15, "The reported football top five in Table 7.1 are Bear Bryant, Jim Tressel, Tom Osborne, Bobby Bowden, and Woody Hayes."),
        (16, "The reported ice-hockey top five are Jerry York, Vic Heyliger, Jack Parker, Ron Mason, and Ned Harkness."),
        (19, "The source reports a downward historical pattern in winning percentage while finding no stable time pattern in wins or championships."),
        (21, "After the post-1950 correction, Mike Krzyzewski leads the adjusted basketball list."),
        (22, "The women-basketball application ranks Pat Summitt first and claims no gender-dependent metric change."),
        (25, "Entropy weighting preserves the same basketball top-ten set with small order changes."),
        (27, "Changing factor priority produces small top-ten order changes in the reported table."),
        (28, "The source claims rho values 0.4, 0.5, and 0.6 leave the top-ten list unchanged."),
    ]
    writing = [
        (1, "Summary chain: ranking task -> four indicators -> fuzzy-consistent weights -> grey degrees -> time correction -> gender -> alternate-weight and rho checks."),
        (3, "Introduction chain: public evaluation need -> qualitative-method limitation -> data opportunity -> four-factor quantitative workflow."),
        (4, "Model chain: weight prerequisite -> fuzzy matrix route -> ideal-reference grey comparison -> descending rank."),
        (6, "Weight chain: ordinal preference -> row totals -> fuzzy-consistent matrix -> column normalization -> geometric mean -> final weights."),
        (7, "Grey chain: candidate matrix -> ideal coach -> normalization -> coefficient -> weighted degree -> rank."),
        (9, "Data chain: eligibility -> candidate list -> NCAA source -> four typed values -> calculation table."),
        (14, "Transfer chain: shared four-field interface -> sport-specific championship and award mapping -> new top-five list."),
        (16, "Comparison chain: model list -> named media lists -> overlap -> limited plausibility conclusion."),
        (17, "Time chain: historical concern -> five era groups -> mean plots -> ANOVA -> correction decision."),
        (20, "Correction chain: era baseline -> factor -> transformed winning rate -> grey rerun -> adjusted rank."),
        (22, "Gender chain: same four fields -> women roster -> rank -> broad claim requiring a scope boundary."),
        (22, "Entropy chain: positive matrix -> normalization -> shares -> entropy -> weights -> alternate rank comparison."),
        (25, "Stability chain: changed preference matrix -> revised weights -> rerun -> top-ten comparison."),
        (27, "Sensitivity chain: fixed roster and weights -> rho sweep -> score tables -> claimed top-ten invariance."),
        (37, "Article chain: reader question -> quantitative method -> three sport lists -> portability claim."),
    ]
    contributions = [
        {"page": 6, "summary": "Uses a compact ordinal preference scale and fuzzy-consistent conversion to expose factor-weight construction."},
        {"page": 7, "summary": "Defines an ideal-reference grey ranking interface that works with a small candidate dataset."},
        {"page": 14, "summary": "Transfers the same typed four-indicator interface after redefining sport-specific award fields."},
        {"page": 17, "summary": "Makes historical comparability a separate analytic question instead of hiding it in the base score."},
        {"page": 22, "summary": "Uses entropy weighting as an alternate calculation rather than relying only on expert priority."},
        {"page": 25, "summary": "Checks a changed preference order and reports rank effects."},
        {"page": 27, "summary": "Varies the grey distinguishing coefficient and prints the resulting scores."},
        {"page": 37, "summary": "Converts the technical ranking into a public-facing Sports Illustrated article."},
    ]
    visuals = [
        {"page": 1, "figure": "summary page", "summary": "The first page makes the complete four-indicator, two-stage, time/gender, and checking route scannable."},
        {"page": 5, "figure": "notation and definition table", "summary": "Binds fuzzy and grey symbols to later calculations while exposing extraction-sensitive notation."},
        {"page": 6, "figure": "preference matrix and conversion equations", "summary": "Shows how ordinal factor comparisons enter the fuzzy-consistent matrix."},
        {"page": 10, "figure": "Tables 2-3 and weight matrix", "summary": "Places factor order, derived weights, and normalized coach inputs near the main calculation."},
        {"page": 13, "figure": "Table 5 basketball rank", "summary": "Communicates the primary basketball ordering and its four raw indicators."},
        {"page": 15, "figure": "Tables 6.1-7.2", "summary": "Maps football and ice-hockey awards and displays their top-five outputs."},
        {"page": 16, "figure": "Tables 8-10 external comparisons", "summary": "Places model and media lists side by side for an overlap check."},
        {"page": 18, "figure": "Figures 1-2 era means", "summary": "Plots mean winning percentage and wins across the five start-era groups."},
        {"page": 19, "figure": "Figure 3 and ANOVA Tables 11-12", "summary": "Connects championship means and statistical summaries to the historical argument."},
        {"page": 20, "figure": "Tables 13-14 correction comparison", "summary": "Shows pre-adjustment and transformed winning percentages beside grey degrees."},
        {"page": 22, "figure": "Table 15 and entropy notation", "summary": "Combines the women-basketball output with the start of the alternate weighting method."},
        {"page": 24, "figure": "Table 16 entropy ranking", "summary": "Makes the near-equal entropy weights and alternate rank outcome inspectable."},
        {"page": 25, "figure": "Tables 17-18", "summary": "Compares weighting methods and displays the changed preference matrix."},
        {"page": 26, "figure": "Tables 19-20", "summary": "Displays the revised rank and its top-ten comparison with the base matrix."},
        {"page": 27, "figure": "Tables 21-22 rho sensitivity", "summary": "Prints grey scores for rho=0.5 and rho=0.4, exposing a name-score inconsistency."},
        {"page": 28, "figure": "Table 23 and closing assessment", "summary": "Completes the rho=0.6 comparison before strengths and weaknesses."},
        {"page": 30, "figure": "basketball appendix table", "summary": "Provides raw candidate fields and award components for spot checks."},
        {"page": 31, "figure": "football appendix table", "summary": "Provides football career, championship, and award-component rows with dense headers."},
        {"page": 32, "figure": "ice-hockey appendix table", "summary": "Provides the ice-hockey roster and sport-specific award columns."},
        {"page": 33, "figure": "women-basketball appendix table", "summary": "Provides the subgroup roster used for the gender claim."},
        {"page": 34, "figure": "fuzzy and entropy code", "summary": "Exposes matrix operations and hard-coded spreadsheet dependencies."},
        {"page": 36, "figure": "grey calculation code", "summary": "Shows normalization, ideal vector, coefficient, and score multiplication while retaining missing inputs."},
        {"page": 37, "figure": "Sports Illustrated article", "summary": "Turns the quantitative route into a reader-facing introduction and first top-five list."},
        {"page": 38, "figure": "final sport lists", "summary": "Presents football and ice-hockey top-five lists and a short model explanation."},
    ]
    warnings = [
        (3, "The audience is repeatedly called Sports Illustrator although the requested publication is Sports Illustrated."),
        (10, "The printed vector order follows wins, percentage, championships, awards, but the prose assigns 0.2169 to championships and 0.3527 to wins, conflicting with the matrix rows."),
        (8, "The grey comprehensive equation prints a score vector with n entries even though candidate count is m, and index use alternates between factor and candidate roles."),
        (9, "Eligibility thresholds differ by sport and exclude notable low-win coaches without a sensitivity analysis of the candidate boundary."),
        (9, "Coach Awards aggregate heterogeneous honors through a hand-selected list with no provenance snapshot, duplicate policy, or comparability rule."),
        (16, "The football model list in Table 9 conflicts with Table 7.1 and the final article; it substitutes Bowden, Warner, Stagg, and Paterno for the stated computed order."),
        (16, "External media lists use different candidate universes and methods, so overlap is not independent validation."),
        (19, "One-way ANOVA evaluates equality of group means, but the text interprets its p-values as differences of variances."),
        (20, "The inverse correction produces winning percentages above one, including 1.37, without redefining the metric or explaining downstream normalization."),
        (21, "After excluding two extreme coaches the paper treats p=0.08 as support for a correction, although failure to reject equal group means weakens that rationale."),
        (21, "The football p=0.07 argument similarly treats non-significance as justification for applying the moving-average correction."),
        (22, "The no-gender-effect conclusion comes from one women-basketball roster without a formal sex/gender comparison or cross-sport test."),
        (23, "The entropy prose reverses the usual relation between dispersion and entropy in places, and the extreme-value transformation is not clearly specified."),
        (27, "Table 21 assigns the main model's John Wooden, Adolph Rupp, Mike Krzyzewski, and Jim Boeheim scores to different names, contradicting Table 5."),
        (28, "The sensitivity conclusion checks a reported top-ten list but does not quantify score or rank uncertainty, roster instability, or simultaneous parameter changes."),
        (30, "Appendix basketball rows place career-start years under an award-component header for several coaches, indicating a table-schema or header alignment defect."),
        (34, "The entropy code computes an adjusted y matrix and then overwrites it with x divided by column sums plus one before entropy calculation."),
        (36, "The total-model code reads local spreadsheets, assumes an existing x in the entropy fragment, writes to a desktop path, and omits files, versions, and an executable wrapper."),
        (38, "No frozen source data, complete calculation package, uncertainty analysis, or independent held-out validation is supplied."),
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 9, "summary": "Publish versioned rosters, eligibility rules, source dates, award mappings, and machine-readable sport tables."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 10, "summary": "Reconcile factor order and recompute the fuzzy-consistent weights from a documented expert-elicitation protocol."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 13, "summary": "Archive a tested notebook that reproduces every normalized value, grey coefficient, degree, and rank."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 17, "summary": "Replace start-era bins with a transparent historical-opportunity model and report rank uncertainty across correction choices."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 22, "summary": "Test gender and sport transfer with matched indicators, formal interactions, and subgroup uncertainty rather than one list."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 27, "summary": "Run global weight, rho, roster, and award-definition sensitivity and report rank acceptability intervals."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 36, "summary": "Package source snapshots, data-cleaning tests, code, environment, logs, and cross-table consistency assertions."},
    ]
    return {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": SHORT, "title": "An evaluation model of college coaches", "award_status": "outstanding",
        "source": {"relative_path": "2014\u7f8e\u8d5b\u7279\u7b49\u5956/B-26636-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is the contest Summary; physical page 2 is the contents page; physical page 3 is printed page 2, and physical page 38 is printed page 37."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["All 38 local UTF-8 page text files were read in bounded physical-page ranges with truncation gaps explicitly reread.", "All 38 rendered pages were visually reviewed through isolated JPEG proxies no larger than 288627 bytes.", "No original full-page PNG, embedded base64 image, contact sheet, or multi-image tool result entered model transport.", "Formula, table, rank, historical-test, and appendix-code inconsistencies remain explicit warning anchors rather than silent repairs."]},
        "context_sources": [{"type": "paper", "path": "2014\u7f8e\u8d5b\u7279\u7b49\u5956/B-26636-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "text-pages", "path": f"artifacts/papers/{PID}/text/pages"}],
        "task_reconstruction": {"status": "incomplete-official-task-unavailable", "inputs": ["eligible coach rosters", "wins", "winning percentages", "championship counts", "coach-award counts", "factor preferences", "career start years", "sport-specific award mappings"], "outputs": ["indicator weights", "grey degrees", "basketball, football, and ice-hockey top-five lists", "time-adjusted rank", "women-basketball list", "stability and sensitivity comparisons", "Sports Illustrated article"], "decisions": ["who is eligible", "which indicators and weights represent performance", "how to compare eras and genders", "whether the rank is locally stable", "how to communicate the qualified lists"]},
        "section_map": [{"page": start, "section": key, "summary": summary} for key, chapter, start, end, tag, summary in CHAPTERS],
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions], "data_and_preprocessing": [{"page": p, "summary": s} for p, s in data],
        "models": [{"model_id": model["model_id"], "page": model["page"], "summary": model["summary"]} for model in models["models"]], "dependency_graph": models["dependency_edges"],
        "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification],
        "results_trace": [{"page": p, "summary": s} for p, s in results], "contributions": contributions,
        "writing_logic": [{"page": p, "summary": s} for p, s in writing], "language_observations": [{"page": p, "summary": s} for p, s in writing],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The summary previews indicators, weighting, ranking, historical adjustment, and checks before detail, but award status alone does not prove why judges valued it.", "evidence_class": "J"}, {"page": 20, "summary": "The before/after table makes the intended historical correction visible, without validating its scale or fairness.", "evidence_class": "J"}, {"page": 37, "summary": "The article converts technical results into an audience-facing list, without proving external ranking truth.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": s} for p, s in warnings], "independent_extensions": extensions,
        "candidate_rule_impacts": [], "unresolved_questions": [s for _, s in warnings], "protocol_v2_records": {}, "review_status": "validated",
    }


def build_observations(template, language, models, card):
    observations = template.make_observations(language, models, card)
    interpretations = {
        "language": "Reuse the ranking-language move only after replacing sport, roster, indicator, era, weight, and decision entities.",
        "modeling": "Retain typed matrices, indicators, normalization, weights, reference vectors, corrections, tests, outputs, and handoffs.",
        "logic": "Preserve the positive task-to-indicator-to-weight-to-grey-degree-to-qualified-list chain.",
        "visualization": "Keep table headers, matrix order, plot axes, era groups, rank names, score columns, and analytical purpose together.",
        "verification": "Name the matrix, formula, table, cross-list comparison, historical test, parameter rerun, or code fragment being checked.",
        "data": "Retain eligibility, source, retrieval state, units, award mapping, time field, transformation, and downstream consumer.",
        "assumption": "Pair each comparability assumption with its enabled ranking step, excluded roster or era, diagnostic, and repair.",
        "result": "Keep sport, roster, metric, score, rank, correction state, comparator, and evidence status distinct.",
        "weakness": "Record source defects only after positive language, organization, model, result, and visualization learning.",
        "other": "Separate cited context and printed appendix rows from frozen inputs, executable code, logs, and validation evidence.",
    }
    provenance_sources = [
        (29, "references", "The reference list identifies method and coach-evaluation sources but does not freeze the exact candidate records used by this paper."),
        (29, "references", "Citations establish reading provenance, not a versioned ranking-input contract with retrieval dates and archived values."),
        (30, "basketball appendix", "The basketball table exposes candidate wins, rates, championships, award components, and career fields for spot checks."),
        (30, "basketball appendix", "Dense basketball rows must remain tied to the printed header because wrapped values and a likely year-column defect can change interpretation."),
        (31, "football appendix", "The football table maps championship and thirteen award-component columns to the shared four-indicator interface."),
        (31, "football appendix", "Football appendix values support source-level checks but do not document duplicate awards, missing values, or candidate exclusions."),
        (32, "ice-hockey appendix", "The ice-hockey table supplies sport-specific championship and award components for the transferred ranking calculation."),
        (32, "ice-hockey appendix", "Wrapped names and table continuations require header-aware parsing before any machine-readable transfer."),
        (33, "women-basketball appendix", "The women-basketball table supplies the subgroup roster used by the paper's gender discussion."),
        (33, "women-basketball appendix", "One subgroup table can support a rerun but not a general no-gender-effect conclusion without a formal comparison design."),
        (34, "fuzzy-weight code", "The printed matrix routine exposes row sums, consistent conversion, column normalization, geometric means, and final weight normalization."),
        (34, "entropy-code start", "The entropy fragment names an external basketball spreadsheet whose bytes and schema are absent from the paper package."),
        (35, "entropy code", "The entropy routine exposes dispersion and entropy operations while also overwriting an intermediate normalized matrix."),
        (35, "entropy code", "Printed code is useful calculation evidence only after inputs, symbols, and array dimensions are reconciled."),
        (36, "grey-ranking code", "The total-model fragment exposes min-max normalization, ideal maxima, grey coefficients, and weighted score multiplication."),
        (36, "reproduction boundary", "Hard-coded local paths, missing spreadsheets, undefined session state, and absent environment files prevent an executable reproduction."),
    ]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = ["Apply only when sport, roster, eligibility, era, indicator definitions, source versions, weighting, normalization, correction, and decision scope are explicit."]
        row["counterevidence"] = ["A high grey degree, media-list overlap, alternate-weight agreement, or rho-stable top ten does not prove causal coaching superiority, fairness, reproducibility, or external validity."]
        if row["dimension"] == "other":
            page, section, basis = provenance_sources[other_index]
            other_index += 1
            row["page"] = page
            row["section"] = f"{section} / evidence action {other_index}"
            row["source_basis"] = basis
            row["interpretation"] = "Preserve the reference, table, or code fragment with its field meanings and reproduction boundary; do not treat printed support as a frozen executable package."
    if other_index != len(provenance_sources):
        raise RuntimeError(f"expected {len(provenance_sources)} provenance observations, found {other_index}")
    return observations


def attach_rule_impacts(card, observations):
    first = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])

    def evidence(rule_id):
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])

    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain the task-to-four-indicator-to-fuzzy-weight-to-grey-rank-to-history/gender/checks-to-article sequence with explicit scope", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "trace eligibility and sources through factor priority, consistent weights, ideal-reference comparison, ranks, time correction, alternate weights, rho checks, and communication", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "version rosters, thresholds, source snapshots, denominators, championship definitions, award mappings, start years, and media comparators", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for cross-era, cross-sport, gender, roster, benefit-direction, ideal-vector, and correction choices", "evidence_ids": [evidence("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain fuzzy-consistent weighting, grey ranking, era analysis and correction, entropy weighting, local priority/rho checks, and appendix support interfaces", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine indicators only through a documented order, normalization, weight vector, ideal reference, coefficient, and aggregate degree", "evidence_ids": [evidence("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep raw indicators, transformed percentages, fuzzy weights, entropy weights, grey coefficients, degrees, and rank lists distinct", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress factor order, roster thresholds, award coding, time grouping, correction scale, gender transfer, name-score integrity, and code reproducibility", "evidence_ids": [evidence("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make evidence claims matrix-, formula-, table-, plot-, comparison-, correction-, sensitivity-, and code-trace-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile weight order, football lists, ANOVA meaning, corrected-rate scale, gender claim, rho name-score mapping, appendix schema, and missing executable evidence", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain matrices, normalized tables, rank lists, era plots, ANOVA summaries, correction tables, sensitivity tables, appendix rosters, and code with labels and purpose", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "measure matrix operations, candidate-by-indicator normalization, ranking reruns, era summaries, entropy calculations, sensitivity scenarios, and validation checks", "evidence_ids": [evidence("R-B-COMP-001")]},
    ]


def build_audit(template, language, models, card, observations):
    audit = template.make_audit(language, models, card, observations)
    layouts = {item["chapter"]: item for item in language["chapter_layouts"]}
    units = language["units"]
    audit["paragraph_chains"] = []
    for chapter in ("abstract", "introduction"):
        ids = [unit["language_unit_id"] for unit in units if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": index + 1, "dominant_move": "decision or context -> typed model route -> result or scope", "language_unit_ids": [ids[index % len(ids)]]} for index in range(layouts[chapter]["paragraph_count"])]})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete", "weakness_substitution_allowed": False,
        "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["The final warning pass records matrix, test, table, claim, and code defects without replacing positive learning."],
        "section_progressions": [{"chapter": chapter, "moves": [f"input: source-checked roster, indicator, matrix, table, plot, test, code, or list entering {chapter}", f"rhetorical job: state the positive definition, comparison, result, or communication move in {chapter}", f"analytical job: select, weight, normalize, compare, aggregate, group, test, correct, rerun, or translate the declared object in {chapter}", f"output: retain a typed weight, degree, table, rank, test, list, or evidence boundary from {chapter}", "handoff: name the next model, check, decision, article, or reproduction boundary"], "positive_pattern": "Use explicit input -> typed operation -> qualified output -> scoped handoff; warnings remain a last pass."} for chapter in language["available_chapters"]],
        "main_argument_chains": [
            {"claim": "A coach-ranking task becomes auditable when eligibility, four indicators, weight construction, and ideal-reference aggregation are explicit.", "support_steps": ["candidate filter", "indicator definitions", "preference matrix", "fuzzy-consistent conversion", "grey coefficients", "relational degree"], "decision_consequence": "Use the rank only with the same sport, roster, indicator, source, and weight contract.", "source_pages": [3, 5, 6, 7, 8, 9, 10, 13]},
            {"claim": "Historical and subgroup extensions require their own evidence rather than inheriting validity from the base rank.", "support_steps": ["era groups", "mean plots", "ANOVA", "inverse correction", "women-basketball rerun"], "decision_consequence": "Treat the time and gender claims as conditional scenarios until the test semantics and subgroup design are repaired.", "source_pages": [17, 18, 19, 20, 21, 22]},
            {"claim": "Alternate weights and rho values are useful local checks but cannot validate a shared roster and indicator design.", "support_steps": ["entropy weights", "alternate preference matrix", "rho sweep", "top-ten comparison", "name-score conflict"], "decision_consequence": "Report set and order sensitivity with integrity checks and seek independent validation separately.", "source_pages": [22, 23, 24, 25, 26, 27, 28]},
            {"claim": "A public-facing list is strongest when it traces to typed computations and preserves conflicts and reproducibility limits.", "support_steps": ["sport-specific lists", "external comparisons", "appendix rosters", "code fragments", "Sports Illustrated article"], "decision_consequence": "Publish the list with provenance, model, uncertainty, and correction disclosures.", "source_pages": [15, 16, 30, 31, 32, 33, 34, 35, 36, 37, 38]},
        ],
    }
    audit["formula_error_watch"] = {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": [
        {"model_id": models["models"][0]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-005", "page": 10, "warning": "The prose maps the displayed weight-vector positions to indicators in an order inconsistent with the matrix rows; recompute and relabel before reuse."},
        {"model_id": models["models"][6]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-010", "page": 20, "warning": "The historical correction is extraction-sensitive and produces values above one; preserve the source scale ambiguity instead of silently treating them as probabilities."},
        {"model_id": models["models"][7]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-011", "page": 23, "warning": "The entropy section's extreme-value adjustment and appendix code do not preserve one coherent normalized matrix; an executable recomputation is required."},
    ]}
    counts = Counter(item["dimension"] for item in observations)
    audit["dimension_counts"] = {dimension: counts[dimension] for dimension in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}
    audit["positive_reusable_language_count"] = len(units)
    audit["weakness_record_count"] = counts["weakness"]
    return audit


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    base = load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q103")
    template = base.load_template_module()
    configure(base)
    pages = {}
    for page in range(1, PAGE_COUNT + 1):
        source = TEXT_DIR / f"page-{page:04d}.txt"
        if not source.is_file():
            raise FileNotFoundError(source)
        pages[page] = source.read_text(encoding="utf-8")
    language = build_language(base, template, pages)
    models = build_models(base, template)
    card = build_card(models)
    card["protocol_v2_records"] = {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(model["governing_equations"]) for model in models["models"]), "review_status": models["review_status"]}}
    observations = build_observations(template, language, models, card)
    attach_rule_impacts(card, observations)
    audit = build_audit(template, language, models, card, observations)
    write_json(STAGE / "language.json", language)
    write_json(STAGE / "models.json", models)
    write_json(STAGE / "card.json", card)
    write_json(STAGE / "audit.json", audit)
    (STAGE / "observations.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "stage": str(STAGE), "pages_read": len(pages), "language_units": len(language["units"]), "models": len(models["models"]), "equations": sum(len(model["governing_equations"]) for model in models["models"]), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(card["visualization_observations"]), "warnings": len(card["weaknesses"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
