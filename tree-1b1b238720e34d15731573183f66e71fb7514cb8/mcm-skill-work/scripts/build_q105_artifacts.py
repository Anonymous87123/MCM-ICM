from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2014-28875-728f6f07"
SHORT = "28875"
SHA = "728f6f07835cc296fec1768eacd79b721bae1978918ae2275dbbdade8a975b64"
TYPE = "B"
YEAR = "2014"
PAGE_COUNT = 35
TEXT_DIR = ROOT / "artifacts/papers" / PID / "text/pages"
STAGE = ROOT / "tmp/q105-stage-v2"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHAPTERS = [
    ("summary-sheet", "title", 1, 2, "SUM", "The two-page summary moves from the coach-selection goal through the AHP-FCE baseline, the classified IAHP-FCE repair, cross-sport and gender applications, a cross-pool winner, time-line plots, four tests, and practical transfer claims."),
    ("abstract", "abstract", 3, 3, "ABS", "The abstract compresses baseline construction and 80 percent fit, the two-level repair and claimed 100 percent fit, three-sport and women-coach lists, Pat Summitt, time-horizon behavior, testing, and broader-use claims."),
    ("introduction-and-task", "introduction", 4, 4, "INT", "The opening identifies Sports Illustrated and then restates four deliverables: choose coaches, test time horizon, transfer across gender and sport, and write a nontechnical article."),
    ("literature-and-approach", "problem-analysis", 4, 6, "LIT", "The literature review contrasts peer review, surveys, content analysis, and bibliometrics before selecting AHP and fuzzy comprehensive evaluation as complementary qualitative-quantitative methods."),
    ("assumptions-and-symbols", "assumptions", 6, 7, "ASM", "The assumptions define the candidate pool, Internet-data trust, retained metrics, classification logic, and three first-level concepts, while the notation table binds sample size, weights, judgment matrix, dispersion, CIC, and score."),
    ("data-and-metric-selection", "data-preprocessing", 8, 9, "DAT", "The data section chooses Internet collection, applies an approximately top-40 screening line per sport, displays sport-specific metric hierarchies, and passes nonnegative metric arrays to normalization."),
    ("normalization-to-consistency", "model-establishment", 9, 13, "BAS", "The baseline model defines benefit, cost, and middle-type membership formulas, a fuzzy matrix, dispersion-driven pairwise judgments, reciprocal consistency conditions, a CIC correction program, and a weighted composite score."),
    ("baseline-test-and-failure", "robustness-verification", 13, 15, "TST", "The basketball test builds a 13-by-13 matrix, estimates weights in LINGO, reports CIC 0.032, ranks five coaches, rejects the list against external examples, and turns that failure into requirements for classification and simpler calculation."),
    ("hierarchical-improvement", "model-improvement", 15, 17, "IMP", "The repair groups metrics into first-level classifications, calculates within-group weights, introduces classification weights, and aggregates local scores into the IAHP-FCE final score."),
    ("basketball-application", "algorithm", 17, 20, "BBL", "The basketball application fixes Experience, Achievement, and Competency, solves three local matrices, assigns top-level weights 0.35, 0.40, and 0.25, and produces an improved top-five list."),
    ("football-application", "problem-restatement", 20, 21, "FTB", "The football application reuses the interface with a sport-specific ten-metric structure, three local matrices, the same top-level weights, and a 76-coach ranking."),
    ("baseball-and-gender", "results", 22, 24, "XFR", "The paper falls back to the unclassified model for three baseball metrics and seven women-basketball metrics, producing two more top-five lists and claiming broad sport and gender applicability."),
    ("best-all-time-decision", "conclusion", 24, 25, "DEC", "The decision section compares scores produced from different sport-specific metric systems and names Pat Summitt the overall winner before supplying a short biographical justification."),
    ("time-horizon", "sensitivity-analysis", 25, 28, "TIM", "Annual composite-score tables and four coach plots compare gender and sport combinations, then infer bounded fluctuation with a slight upward career trend."),
    ("model-tests", "sensitivity-robustness", 28, 31, "VER", "The testing section invokes dimension consistency, top-five membership overlap, assumption reasonableness, and a one-factor baseball rank-stability sweep before declaring the model qualified."),
    ("sports-illustrated-article", "memo", 31, 32, "MEM", "The audience article explains the less-than-ten versus more-than-nine branch, lists sport winners, dramatizes Pat Summitt, and translates the time-horizon claim into advice for coaches."),
    ("strengths-limitations-future", "strengths-limitations", 33, 33, "SWK", "The final evaluation praises standardization, decomposition, metric quantification, classification, and universality, then identifies indicator burden and missing team-management data and proposes better collection and quantification."),
    ("references", "references", 34, 35, "REF", "The references identify method, sports, ranking, and sensitivity sources but do not freeze the input datasets, external rankings, spreadsheets, LINGO files, or MATLAB code used in the calculations."),
]


PATTERNS = [
    "LP-B-SUMMARY-GOAL-BASELINE-REPAIR-TRANSFER-CHECK",
    "LP-B-ABSTRACT-BASELINE-FAILURE-IMPROVEMENT-RESULT",
    "LP-B-INTRO-AUDIENCE-DELIVERABLES",
    "LP-B-PRIOR-METHOD-LIMIT-ROUTE",
    "LP-B-ASSUMPTION-SCOPE-SYMBOL-DEFINITION",
    "LP-B-METRIC-SPORT-SOURCE-PREPROCESS",
    "LP-B-NORMALIZE-DISPERSION-MATRIX-CONSISTENCY-SCORE",
    "LP-B-BASELINE-RANK-FAILURE-REPAIR",
    "LP-B-CLASSIFY-METRICS-LOCAL-WEIGHTS-GLOBAL-SCORE",
    "LP-B-APPLICATION-INPUT-MATRIX-WEIGHTS-RANK",
    "LP-B-CROSS-SPORT-SAME-INTERFACE-RANK",
    "LP-B-LOW-DIMENSION-FALLBACK-SUBGROUP-RERUN",
    "LP-B-CROSS-POOL-SCORE-COMPARISON-DECISION",
    "LP-B-TIMELINE-ANNUAL-SCORE-PLOT-TREND",
    "LP-B-TEST-OVERLAP-SENSITIVITY-BOUNDARY",
    "LP-B-NONTECHNICAL-THRESHOLD-ROUTE-LIST",
    "LP-B-STRENGTH-LIMIT-REPAIR-TRANSFER",
    "LP-B-REFERENCE-PROVENANCE-BOUNDARY",
]


MOVES = [
    ("summary-route", "Compress the goal, baseline, repair, applications, tests, and audience output into a result-led route.", "goal -> baseline -> repair -> applications -> tests -> conclusion"),
    ("deliverable-list", "Convert the prompt into explicit modeling, temporal, transfer, ranking, and communication deliverables.", "audience -> required decisions -> outputs"),
    ("method-selection", "Contrast candidate evaluation methods by scope and limitation before naming the combined route.", "candidate methods -> limits -> selected pair -> purpose"),
    ("assumption-contract", "Group assumptions by coach, data, and metric role and state which calculation each enables.", "entity -> assumption -> enabled step -> boundary"),
    ("metric-handoff", "Name sport-specific metrics and screening before any normalization or weighting.", "sport -> candidate pool -> metrics -> model input"),
    ("formula-chain", "Move from normalization through dispersion, judgment, consistency repair, and weighted score.", "raw value -> membership -> dispersion -> matrix -> repair -> score"),
    ("failure-to-repair", "Use the baseline ranking failure to justify hierarchy depth and calculation changes.", "baseline output -> comparator -> diagnosed mechanism -> repair"),
    ("hierarchical-aggregation", "Separate within-class weights from first-level class weights before composing the final score.", "classification -> local matrix -> local score -> class weight -> global score"),
    ("application-replay", "Replay the same declared interface with sport- or subgroup-specific metrics and roster sizes.", "receiving domain -> mapped metrics -> weights -> score -> list"),
    ("trend-claim", "Show annual scores and comparison plots before making a bounded time-horizon claim.", "annual data -> score series -> plot -> comparison -> trend boundary"),
    ("test-claim", "Name the test object, statistic, comparator, and acceptance interpretation separately.", "test input -> statistic -> comparator -> conclusion -> limitation"),
    ("public-explanation", "Translate the threshold branch and weighted-sum mechanism into a fan-facing list and decision story.", "reader question -> branch -> score construction -> list -> takeaway"),
]


EXAMPLES = [
    ("A ranking paper states the candidate pool and metric directions before calculating weights.", "The resulting list remains conditional on that roster and source version."),
    ("A baseline model is rejected because its failure is tied to matrix size and calculation burden.", "The revised hierarchy changes the mechanism rather than merely relabeling the same score."),
    ("A two-level score reports local criterion weights and top-level class weights separately.", "Readers can reproduce the handoff from local scores to the final ranking."),
    ("A cross-sport rerun maps receiving-domain fields before reusing the scoring engine.", "Transfer demonstrates interface flexibility but requires new validation."),
    ("A time analysis plots annual scores for declared coaches before describing trend and fluctuation.", "The prose distinguishes observed examples from a population-wide temporal law."),
    ("A validation table distinguishes exact order agreement from top-k membership overlap.", "The reported accuracy metric states which kind of agreement it measures."),
    ("A sensitivity sweep names the perturbed variable, step, stopping event, and preserved outputs.", "Rank stability is not treated as proof that the original measurements are valid."),
    ("A public article explains why the computation changes when the metric count crosses a threshold.", "The list is delivered with a plain-language scope and evidence boundary."),
]


PROFILE_DETAILS = {
    "title": ("Preview the full coach-ranking transaction while keeping baseline, repair, transfer, and validation claims distinct.", ["selection goal", "baseline model and result", "hierarchical repair", "sport/gender/time applications", "testing and scope"], ["goal", "model stage", "reported list or statistic", "qualification and next stage"]),
    "abstract": ("Compress the source's result-led argument without turning media-list agreement into external validity.", ["problem importance", "baseline failure", "improved model", "ranked outputs", "tests and transfer"], ["problem", "method", "intermediate comparison", "final result", "boundary"]),
    "introduction": ("Translate the contest prompt into four explicit analytical and communication obligations.", ["named audience", "time span", "candidate sports and genders", "three-sport top five", "nontechnical article"], ["decision context", "deliverable list", "scope"]),
    "problem-analysis": ("Compare candidate evaluation methods by observed use and limitation before selecting AHP-FCE.", ["method name", "strength", "limitation", "selection rationale", "combined role"], ["alternatives", "tradeoffs", "chosen route"]),
    "assumptions": ("Bind coach, data, and metric assumptions plus symbols to downstream scoring operations.", ["assumption category", "enabled calculation", "excluded uncertainty", "symbol meaning", "consumer"], ["entity", "assumption or definition", "enabled operation", "boundary"]),
    "data-preprocessing": ("Fix sources, screening, sport-specific metrics, and indicator direction before normalization.", ["collection mode", "candidate screen", "sport hierarchy", "sample dimensions", "direction class"], ["source", "roster", "metrics", "preprocessing handoff"]),
    "model-establishment": ("Present normalization, dispersion, judgment construction, consistency repair, and score in executable order.", ["raw metric", "membership rule", "fuzzy matrix", "dispersion", "judgment entry", "CIC program", "score"], ["input array", "transformation", "matrix", "constraint", "output"]),
    "robustness-verification": ("Turn a poor baseline list into a mechanism-specific diagnosis and a concrete redesign requirement.", ["test roster", "matrix and weights", "CIC", "top five", "external counterexample", "repair target"], ["baseline", "observed failure", "cause", "redesign"]),
    "model-improvement": ("Separate local metric weighting from first-level classification weighting and expose their final composition.", ["classification rule", "local criteria", "local weight", "class weight", "global score"], ["grouping", "within-group solve", "between-group solve", "aggregate"]),
    "algorithm": ("Replay the hierarchy on basketball with declared inputs, matrices, weights, CIC, and list output.", ["roster size", "metric direction", "dispersion", "three matrices", "local weights", "top-level weights", "rank"], ["data", "local solves", "composition", "result"]),
    "problem-restatement": ("Map football fields into the scoring interface and retain sport-specific data and validation limits.", ["receiving sport", "metric count", "roster", "local matrices", "weights", "rank"], ["mapping", "rerun", "list", "scope"]),
    "results": ("Explain the low-dimensional fallback and gender rerun without equating top-five overlap with universal applicability.", ["metric count", "fallback branch", "roster size", "weights", "top-five overlap", "claim boundary"], ["receiving case", "branch", "score", "comparison", "scope"]),
    "conclusion": ("Trace the overall-winner claim to its cross-pool comparison and expose the comparability condition.", ["sport-specific scores", "cross-pool ordering", "winner", "biographical support", "measurement-invariance boundary"], ["component lists", "comparison", "decision", "qualification"]),
    "sensitivity-analysis": ("Move from annual scores through four plotted examples to a bounded time-horizon interpretation.", ["coach identity", "annual interval", "score series", "plot", "comparison pairing", "trend statement"], ["annual data", "visual trace", "cross-case comparison", "trend boundary"]),
    "sensitivity-robustness": ("Keep each test's object, metric, comparator, and inference boundary visible.", ["dimension check", "top-five overlap", "assumption inference", "perturbation sweep", "rank-stability interval"], ["test", "evidence", "acceptance claim", "limitation"]),
    "memo": ("Translate the metric-count branch, weighted score, lists, winner, and time claim for sports fans.", ["reader hook", "less-than-ten branch", "more-than-nine branch", "sport lists", "winner", "career advice"], ["question", "plain mechanism", "ranked output", "takeaway"]),
    "strengths-limitations": ("Pair each claimed strength with the mechanism it refers to and each weakness with a repair.", ["strength", "mechanism", "weakness", "missing evidence", "repair", "transfer limit"], ["positive feature", "constraint", "future action"]),
    "references": ("Identify source categories while distinguishing citations from frozen computational provenance.", ["method source", "sports source", "ranking source", "sensitivity source", "missing snapshot or code"], ["citation", "used role", "unfrozen dependency", "boundary"]),
}


def configure(q104, base, template) -> None:
    values = {
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
    }
    for module in (q104, base, template):
        for name, value in values.items():
            setattr(module, name, value)


def build_language(q104, base, template, pages):
    configure(q104, base, template)
    language = q104.build_language(base, template, pages)
    for unit in language["units"]:
        purpose, slots, order = PROFILE_DETAILS[unit["chapter"]]
        unit["function"] = purpose
        unit["reusable_pattern"] = " -> ".join(order)
        unit["information_order"] = order
        unit["reusable_elements"] = slots
        unit["prohibited_generalizations"] = [
            "Do not transfer coach scores, metric directions, hierarchy depth, class weights, media overlap, or time trends without reconstructing the receiving roster and measurement contract.",
            "Do not call top-five membership overlap exact ranking accuracy, and do not compare composite scores across sports until their scales and criteria are demonstrably commensurate.",
        ]
        unit["features"]["quantitative_role"] = "bind roster size, metric direction, normalized value, dispersion, matrix entry, local weight, class weight, CIC, composite score, rank, perturbation, or overlap statistic to its declared role"
        unit["features"]["transition"] = "first, then, therefore, owing to, based on, similarly, contrast with, in order to, finally, and in summary connect baseline, repair, application, testing, and communication"

    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 35 physical-page UTF-8 text files were read in order; four byte-bounded contact-sheet proxies covered pages 1-7, 8-14, 15-25, and 26-35, and four focused proxies checked formula regions on pages 10, 11, 12, and 30."
        layout["ambiguities"] = [
            "Text extraction flattens piecewise cases, subscripts, matrix columns, table rows, and plot labels; the original 150-DPI PNGs remain authoritative and the eight JPEG proxies were transport-only review aids.",
            "Printed page numbering begins on physical page 3, so physical page equals printed page plus two from that point onward.",
        ]
        if layout["chapter"] == "title":
            layout["paragraph_count"] = 9
            layout["paragraph_functions"] = [
                "State the best-coach goal, fairness criteria, retained metrics, and IAHP-FCE destination.",
                "Sequence baseline normalization, membership, judgment, consistency, and basketball top-five output.",
                "Diagnose the need for classification and introduce the improved two-level model.",
                "Claim cross-sport reuse through football and baseball rankings.",
                "Claim cross-gender reuse through women-basketball ranking.",
                "Name Pat Summitt by comparing final composite scores.",
                "Preview annual score plots and the bounded upward-trend claim.",
                "List four model tests and the 0.0297 sensitivity interval.",
                "Close with simplified calculation, claimed accuracy, utility, and practical-domain transfer.",
            ]
        elif layout["chapter"] == "abstract":
            layout["paragraph_count"] = 7
            layout["paragraph_functions"] = [
                "State the decision and IAHP-FCE model.",
                "Describe metrics, standardization, baseline AHP-FCE, and 80 percent comparison.",
                "Introduce classification, model II, multi-sport and women-coach outputs, and claimed perfect fit.",
                "Name Pat Summitt as the overall winner.",
                "Summarize the time-line comparison and slight upward trend.",
                "Summarize four tests and the 0.0297 interval.",
                "Conclude with calculation, accuracy, utility, and transfer claims.",
            ]
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = 1
            layout["paragraph_functions"] = [
                "Identify the Sports Illustrated audience and century-wide male-or-female coach selection context before the four-item task restatement.",
            ]
    return language


def eq(q104, index, page, label, latex, symbols, purpose, confidence="high"):
    return q104.equation(index, page, label, latex, symbols, purpose, confidence)


def build_models(q104, base, template):
    configure(q104, base, template)
    normalization = [
        eq(q104, 1, 10, "benefit normalization (1)", r"r(i,j)=\frac{x(i,j)}{x_{max}(i)+x_{min}(i)}", ["r_ij", "x_ij", "x_max", "x_min"], "Scale a benefit-oriented metric before fuzzy evaluation."),
        eq(q104, 2, 10, "cost normalization (2)", r"r(i,j)=\frac{x_{max}(i)+x_{min}(i)-x(i,j)}{x_{max}(i)+x_{min}(i)}", ["r_ij", "x_ij", "x_max", "x_min"], "Reverse a cost-oriented metric on the paper's chosen scale."),
        eq(q104, 3, 10, "middle-optimum normalization (3)", r"r(i,j)=\begin{cases}\frac{x(i,j)}{x_{mid}(i)+x_{min}(i)},&x_{min}(i)\le x(i,j)<x_{mid}(i)\\\frac{x_{max}(i)+x_{mid}(i)-x(i,j)}{x_{max}(i)+x_{mid}(i)},&x_{mid}(i)\le x(i,j)<x_{max}(i)\end{cases}", ["r_ij", "x_ij", "x_min", "x_mid", "x_max"], "Scale a metric whose stated optimum lies in the middle of its observed range.", "medium"),
        eq(q104, 4, 10, "fuzzy evaluation matrix", r"R=(r(i,j))_{n\times m}", ["R", "r_ij", "n", "m"], "Collect metric-by-coach membership values into the fuzzy matrix."),
    ]
    judgment = [
        eq(q104, 5, 11, "sample mean", r"\bar r_i=\frac{1}{m}\sum_{j=1}^{m}r(i,j)", ["r_bar_i", "r_ij", "m"], "Calculate the mean of one metric's coach memberships."),
        eq(q104, 6, 10, "sample dispersion", r"s(i)=\sqrt{\frac{1}{m}\sum_{j=1}^{m}(r(i,j)-\bar r_i)^2}", ["s_i", "r_ij", "r_bar_i", "m"], "Measure how much ranking information a metric appears to carry."),
        eq(q104, 7, 11, "dispersion judgment entry (4)", r"b_{ij}=\begin{cases}\frac{s(i)-s(j)}{s_{max}-s_{min}}(b_m-1)+1,&s(i)\ge s(j)\\\left[\frac{s(j)-s(i)}{s_{max}-s_{min}}(b_m-1)+1\right]^{-1},&s(i)<s(j)\end{cases}", ["b_ij", "s_i", "s_j", "s_max", "s_min", "b_m"], "Convert dispersion differences into reciprocal pairwise judgments.", "medium"),
        eq(q104, 8, 11, "maximum judgment degree", r"b_m=\min\left\{i,\operatorname{int}\left(\frac{s_{max}}{s_{min}+0.5}\right)\right\}", ["b_m", "i", "s_max", "s_min"], "Bound the paper's pairwise-importance scale.", "low"),
    ]
    consistency = [
        eq(q104, 9, 11, "ideal weight ratio (5)", r"b_{ij}=\frac{w_i}{w_j}", ["b_ij", "w_i", "w_j"], "State the ideal reciprocal weight relation."),
        eq(q104, 10, 12, "consistency residual (6)", r"\sum_{i=1}^{n}\sum_{j=1}^{n}|b_{ij}w_j-w_i|=0", ["b_ij", "w_i", "w_j", "n"], "Express full multiplicative consistency as zero weighted residual."),
        eq(q104, 11, 12, "consistency correction objective (7)", r"\min CIC(n)=\frac{1}{n^2}\sum_{i=1}^{n}\sum_{j=1}^{n}|y_{ij}-b_{ji}|+\frac{1}{n^2}\sum_{i=1}^{n}\sum_{j=1}^{n}|y_{ij}w_j-w_i|", ["CIC", "n", "y_ij", "b_ji", "w_i", "w_j"], "Balance proximity to the printed judgment matrix with weighted consistency.", "medium"),
        eq(q104, 12, 13, "consistency program constraints", r"y_{ii}=1;\ y_{ij}=1/y_{ji}\in[b_{ij}-db_{ij},b_{ij}+db_{ij}];\ w_i>0;\ \sum_{i=1}^{n}w_i=1", ["y_ii", "y_ij", "y_ji", "b_ij", "d", "w_i", "n"], "Constrain the corrected reciprocal matrix and normalized positive weights.", "medium"),
    ]
    score = [eq(q104, 13, 13, "baseline composite score (8)", r"z(j)=\sum_{i=1}^{n}w_i r(i,j)", ["z_j", "w_i", "r_ij", "n"], "Return one weighted fuzzy score per coach.")]
    hierarchy = [eq(q104, 14, 17, "hierarchical final score (9)", r"Z(j)=\sum_{i=1}^{x}W_1z_i(j)+\sum_{i=x+1}^{y}W_2z_i(j)+\sum_{i=y+1}^{n}W_3z_i(j)+\cdots", ["Z_j", "W_1", "W_2", "W_3", "z_i", "x", "y", "n"], "Aggregate within-class fuzzy scores using first-level classification weights.")]
    sensitivity = [
        eq(q104, 15, 30, "first-metric perturbation", r"z'_1(j)=w_1r(i,j)(1+r_j)+w_2r(i,j)+w_3r(i,j)", ["z1_prime", "w_1", "w_2", "w_3", "r_ij", "r_j"], "Perturb the first baseball metric and rerank until order changes.", "medium"),
        eq(q104, 16, 30, "second-metric perturbation", r"z'_2(j)=w_1r(i,j)+w_2r(i,j)(1+r_j)+w_3r(i,j)", ["z2_prime", "w_1", "w_2", "w_3", "r_ij", "r_j"], "Perturb the second baseball metric and rerank until order changes.", "medium"),
        eq(q104, 17, 30, "third-metric perturbation", r"z'_3(j)=w_1r(i,j)+w_2r(i,j)+w_3r(i,j)(1+r_j)", ["z3_prime", "w_1", "w_2", "w_3", "r_ij", "r_j"], "Perturb the third baseball metric and rerank until order changes.", "medium"),
    ]

    def model(index, page, section, family, purpose, inputs, outputs, equations):
        return q104.make_model(base, template, f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, section, family, purpose, inputs, outputs, equations)

    models = [
        model(1, 8, "data collection, screening, and sport metrics", "metric-system construction", "Select candidate coaches and sport-specific metrics and expose direction classes before scoring.", ["Internet sports records", "candidate screening line", "sport definitions"], ["coach-by-metric arrays", "metric direction classes"], []),
        model(2, 9, "standardization and fuzzy matrix", "fuzzy normalization", "Convert benefit, cost, and middle-optimum metric values into the fuzzy membership matrix.", ["x_ij", "x_min", "x_mid", "x_max"], ["r_ij", "R"], normalization),
        model(3, 10, "dispersion-driven judgment matrix", "objective pairwise weighting", "Use across-coach dispersion to generate bounded reciprocal pairwise judgments.", ["R", "metric membership series"], ["r_bar_i", "s_i", "b_m", "B"], judgment),
        model(4, 11, "weight and consistency program", "matrix consistency correction", "Correct a judgment matrix toward reciprocal weighted consistency and return positive normalized weights.", ["B", "d", "n"], ["Y", "CIC", "w_i"], consistency),
        model(5, 13, "AHP-FCE composite score", "weighted fuzzy evaluation", "Combine membership values and metric weights into one coach score and rank.", ["R", "w_i"], ["z_j", "coach ranking"], score),
        model(6, 13, "baseline basketball test", "baseline evaluation", "Run the 13-metric baseline on 39 basketball coaches and diagnose ranking and calculation failures.", ["39-coach data", "13 metrics", "external examples"], ["baseline top five", "CIC", "repair requirements"], []),
        model(7, 15, "IAHP-FCE classification repair", "hierarchical fuzzy evaluation", "Partition many metrics into classes, solve local weights, and combine local scores with class weights.", ["metric classification", "local matrices", "class weights"], ["local z_i", "Z_j", "hierarchical ranking"], hierarchy),
        model(8, 17, "basketball IAHP-FCE application", "sport-specific hierarchical ranking", "Solve Experience, Achievement, and Competency weights for 39 basketball coaches and report the improved list.", ["13 basketball metrics", "three class matrices", "0.35/0.40/0.25 class weights"], ["basketball scores", "basketball top five"], []),
        model(9, 20, "football application", "cross-sport hierarchical ranking", "Map ten football metrics into the same three-class interface and rank 76 coaches.", ["76-coach football data", "ten metrics", "three matrices"], ["football scores", "football top five"], []),
        model(10, 22, "baseball and women-basketball fallback", "low-dimensional and subgroup transfer", "Use the baseline model when metric count is small and rerun it for baseball and women basketball.", ["69 baseball coaches", "15 women coaches", "three or seven metrics"], ["baseball top five", "women top five"], []),
        model(11, 24, "best-all-time comparison", "cross-pool decision", "Compare reported sport-specific composite scores and select one overall coach.", ["basketball list", "football list", "baseball list", "women list"], ["cross-pool top five", "Pat Summitt decision"], []),
        model(12, 25, "time-line horizon analysis", "annual score trend analysis", "Calculate annual coach scores, plot four selected careers, and compare gender and sport pairings.", ["annual coach records", "fixed metric weights", "four selected careers"], ["annual score series", "four plots", "trend claim"], []),
        model(13, 28, "model test suite", "validation by overlap and internal checks", "Combine dimensional, list-overlap, assumption, and sensitivity checks into a qualification claim.", ["normalized data", "published top-five lists", "assumptions", "baseball metrics"], ["overlap rates", "reasonableness claim", "qualification"], []),
        model(14, 30, "baseball score sensitivity", "one-factor rank-stability sweep", "Perturb one normalized baseball metric at a time until the ranking changes.", ["w_1/w_2/w_3", "r_ij", "0.001 step"], ["negative and positive thresholds", "interval ranges", "average 0.0297"], sensitivity),
        model(15, 31, "Sports Illustrated article", "nontechnical decision communication", "Explain the metric-count branch and publish four top-five lists, an overall winner, and a time-horizon takeaway.", ["validated method summary", "sport lists", "winner", "time claim"], ["fan-facing article", "rank lists", "coach advice"], []),
    ]
    edges = [
        {"from_model_id": models[0]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "Sport-specific arrays and metric directions determine which normalization branch is used."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[2]["model_id"], "handoff": "The fuzzy matrix supplies each metric's across-coach membership series and dispersion."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "The dispersion-generated judgment matrix enters the CIC correction program."},
        {"from_model_id": models[3]["model_id"], "to_model_id": models[4]["model_id"], "handoff": "Positive normalized weights multiply the fuzzy memberships in the composite score."},
        {"from_model_id": models[4]["model_id"], "to_model_id": models[5]["model_id"], "handoff": "The baseline score is run on the 39-coach basketball test and compared with external examples."},
        {"from_model_id": models[5]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "Baseline matrix-size, ranking, and calculation failures motivate the classified hierarchy."},
        {"from_model_id": models[6]["model_id"], "to_model_id": models[7]["model_id"], "handoff": "The improved hierarchy receives basketball metrics, local matrices, and top-level class weights."},
        {"from_model_id": models[6]["model_id"], "to_model_id": models[8]["model_id"], "handoff": "The same classified interface is populated with football metrics and coach records."},
        {"from_model_id": models[4]["model_id"], "to_model_id": models[9]["model_id"], "handoff": "Low-dimensional baseball and women-coach cases reuse the baseline weighted fuzzy score."},
        {"from_model_id": models[7]["model_id"], "to_model_id": models[10]["model_id"], "handoff": "The basketball list contributes scores to the cross-pool overall comparison."},
        {"from_model_id": models[8]["model_id"], "to_model_id": models[10]["model_id"], "handoff": "The football list contributes scores to the cross-pool overall comparison."},
        {"from_model_id": models[9]["model_id"], "to_model_id": models[10]["model_id"], "handoff": "Baseball and women-coach lists contribute scores to the cross-pool comparison."},
        {"from_model_id": models[7]["model_id"], "to_model_id": models[11]["model_id"], "handoff": "Fixed basketball weights are reused to produce annual score series for selected coaches."},
        {"from_model_id": models[7]["model_id"], "to_model_id": models[12]["model_id"], "handoff": "The basketball top five enters the membership-overlap validation table."},
        {"from_model_id": models[9]["model_id"], "to_model_id": models[13]["model_id"], "handoff": "The three-metric baseball model supplies weights and memberships for the perturbation sweep."},
        {"from_model_id": models[12]["model_id"], "to_model_id": models[14]["model_id"], "handoff": "The paper's qualification claim and rank outputs are translated into the audience article."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def build_card(models):
    assumptions = [
        (6, "Approximately 200 selected coaches are assumed to contain the best coach and to represent leaders of their sports."),
        (6, "The overall winner is assumed to come from basketball, football, baseball, or women's basketball rather than every sport named in the task."),
        (6, "Internet data and all statistical processing are assumed true, reliable, and error-free."),
        (6, "Retained metrics and their classifications are assumed important, reasonable, and sufficient for coaching evaluation."),
        (6, "Abandoned coaching attributes are assumed to have little effect on coaching ability."),
        (6, "Experience, Achievement, and Competency are assumed to proxy coaching skill and team-management ability."),
        (10, "Every metric is treated as nonnegative and classified as benefit, cost, or middle-optimum before scoring."),
        (11, "Across-coach dispersion is assumed to represent the amount of comprehensive-evaluation information and therefore metric importance."),
        (13, "A CIC value no greater than 0.1 is assumed to establish satisfactory judgment-matrix consistency."),
        (19, "Top-level class weights 0.35, 0.40, and 0.25 are imported from unspecified relevant information and reused across applications."),
        (24, "Composite scores from different sport-specific metric systems are assumed directly comparable when selecting one overall coach."),
        (25, "Four selected career series are assumed sufficient to characterize the effect of time horizon across sports and genders."),
    ]
    data = [
        (8, "Internet collection is chosen over face-to-face, telephone, postal, and self-completion methods; sports-reference.com and ncaa.com are named as principal sources."),
        (8, "A screening line selects about 40 better coaches for each sport before Excel tables are constructed."),
        (8, "Basketball uses 13 displayed metrics spanning years, games, records, ratings, polls, playoffs, and championships."),
        (9, "Football and baseball use different displayed metric sets, including bowls and poll fields for football and years, games, wins, losses, percentage, and championships for baseball."),
        (13, "The baseline basketball test uses 39 coaches and 13 metrics, with metrics five through eight treated as cost-oriented."),
        (18, "The improved basketball run retains 39 coaches and partitions 13 metrics into Experience, Achievement, and Competency."),
        (20, "The football run uses 76 coaches and ten metrics, with metrics seven through nine treated as cost-oriented."),
        (22, "The baseball run uses 69 coaches and three benefit metrics."),
        (23, "The women-basketball run uses 15 coaches and seven benefit metrics."),
        (25, "Dean Smith's annual score table covers 1961 through 1996; the prose describes 1961 through 1997, leaving an endpoint mismatch."),
        (26, "Pat Summitt, Joe Paterno, and Bobby Bowden plots are used with Dean Smith to compare gender and sport combinations."),
        (28, "External coach lists are presented as authority or website comparators without archived bytes, retrieval dates, or a unified roster protocol."),
    ]
    verification = [
        (13, "The baseline 13-metric matrix is solved with d=0.2 and reported CIC 0.032.", "internal consistency", "The source exposes a numerical threshold before accepting weights.", "The printed matrix contains suspicious entries and no LINGO model or recomputation file is supplied."),
        (15, "The baseline basketball top five is checked against named counterexamples outside the list.", "failure-oriented external comparison", "The paper uses a poor list to motivate redesign rather than hiding it.", "The comparator is informal and the diagnostic does not isolate which formula caused each rank error."),
        (18, "The Experience matrix displays local weights and asserts a satisfactory but numerically blank CIC result.", "local consistency", "The local-weight calculation is visible.", "The printed expression is only 'min CIC(n)=<0.1', so the claimed value is not auditable."),
        (19, "Achievement and Competency matrices report CIC 0.014 and their local weights.", "local consistency", "Both matrices and weights are displayed.", "Top-level weights remain externally asserted and no uncertainty is shown."),
        (20, "The improved basketball top five is compared with a Sports Illustrated list.", "top-five overlap", "All five names appear in both lists.", "Order differs, so 100 percent membership overlap is not 100 percent ranking accuracy."),
        (21, "Football reports CIC 0.051 and a top-five list.", "cross-sport rerun", "The model interface is exercised on a larger roster.", "External agreement and receiving-sport calibration are not independently measured."),
        (22, "Baseball reports CIC 0.028 and a top-five list.", "low-dimensional rerun", "The paper follows its stated fallback branch.", "Only two of five website names overlap, and the input table is not frozen."),
        (23, "Women basketball reports CIC 0.036 and a top-five list.", "gender subgroup rerun", "The subgroup calculation is visible.", "One roster and top-five membership overlap cannot establish gender invariance."),
        (25, "Four annual-score examples are plotted across sport and gender pairings.", "time-horizon scenario comparison", "The plots expose fluctuation and career-stage variation.", "Selection is called random but no sampling frame, regression, uncertainty, or population test is supplied."),
        (28, "Tables 14 through 17 compare model and website top-five lists.", "model-result deviation", "Membership overlap is visible by sport.", "The metric labels exact-order and unordered overlap identically and calls 100 percent overlap small deviation."),
        (29, "The paper infers that data and assumptions are reasonable from overall model-list overlap.", "assumption reasonableness", "The intended inference chain is explicit.", "The check is circular because the same assumptions create the scores being used to validate them."),
        (30, "One normalized baseball metric is perturbed in 0.001 steps until rank order changes.", "local sensitivity", "The flowchart states the stopping rule and Table 18 reports intervals.", "Symbols are ambiguous, negative perturbations can exceed feasible ranges, and rank stability does not validate measurements."),
        (31, "The average interval 0.0297 is compared with a 10 percent threshold.", "aggregate sensitivity claim", "A numerical summary is reported.", "The 10 percent acceptance threshold is not justified and interval width is mislabeled as model sensitivity."),
        (31, "The Sports Illustrated article explains both metric-count branches and reproduces the key lists.", "communication trace", "The audience artifact is connected to the model route.", "It repeats universality and time claims without the analytical caveats required by the evidence."),
    ]
    results = [
        (15, "The baseline AHP-FCE ranks Dean Smith first at 0.774 and omits several cited historically prominent coaches."),
        (20, "The improved basketball model ranks Mike Krzyzewski, Dean Smith, John Wooden, Bob Knight, and Roy Williams."),
        (21, "The football model ranks Joe Paterno, John Gagliardi, Bobby Dodd, Eddie Robinson, and Bear Bryant."),
        (22, "The baseball model ranks Gordie Gillespie, Augie Garrido, Chuck Hartman, Gene Stephenson, and Bill Holowaty."),
        (24, "The women-basketball model ranks Pat Summitt, Tara VanDerveer, Nancy Fahey, Amy Ruley, and Jody Conradt."),
        (24, "A cross-pool table names Pat Summitt the best all-time college coach because her reported score is 0.883."),
        (25, "Dean Smith's annual scores fluctuate while the source describes a slight upward career trend."),
        (26, "The Pat Summitt plot is described as more variable but broadly similar to Dean Smith's."),
        (27, "Joe Paterno and Bobby Bowden plots are used to extend the time-horizon claim across and within sports."),
        (28, "Basketball, women basketball, and football each achieve five-of-five top-list membership overlap despite order changes."),
        (29, "Baseball achieves two-of-five membership overlap, reported as 40 percent."),
        (31, "Sensitivity intervals are reported as 0.009 for years, 0.051 for winning, and 0.029 for games, averaging 0.0297."),
        (32, "The public article republishes four sport lists, Pat Summitt, and the slight upward time-horizon narrative."),
    ]
    visuals = [
        {"page": 7, "figure": "Table 1", "summary": "The symbol table binds m, n, w, B, s(i), CIC, minimum CIC, and z(j) to the baseline calculation."},
        {"page": 8, "figure": "Figure 1", "summary": "The basketball metric hierarchy displays 13 sport-specific inputs."},
        {"page": 9, "figure": "Figures 2 and 3", "summary": "Football and baseball metric hierarchies expose the receiving-domain fields before transfer."},
        {"page": 10, "figure": "Equations 1-3 and fuzzy matrix", "summary": "The three normalization branches and R matrix define the coach-by-metric fuzzy input."},
        {"page": 11, "figure": "Equation 4 and Equation 5", "summary": "The dispersion judgment rule, b_m expression, ideal weight ratio, and matrix form expose the intended pairwise-weight mechanism."},
        {"page": 12, "figure": "Consistency identities and Equations 6-7", "summary": "Reciprocity, transitivity, zero residual, and the CIC objective define the consistency repair target."},
        {"page": 13, "figure": "CIC constraints and Equation 8", "summary": "The constraint block and weighted score complete the baseline optimization-to-ranking handoff."},
        {"page": 14, "figure": "13-by-13 judgment matrix", "summary": "The dense baseline matrix is the main auditable input to the reported metric weights."},
        {"page": 14, "figure": "Table 2", "summary": "Thirteen weights and CIC 0.032 summarize the baseline basketball solution."},
        {"page": 15, "figure": "Table 3", "summary": "The baseline basketball top five exposes the failure that motivates model II."},
        {"page": 16, "figure": "Figure 4", "summary": "A generic two-level hierarchy separates classifications from their local metrics."},
        {"page": 16, "figure": "Table 4, first part", "summary": "The first half of the cross-page table distinguishes class weights W from local metric weights w."},
        {"page": 17, "figure": "Table 4 continuation and Equation 9", "summary": "The continued table and final-score equation show the local-to-global aggregation interface."},
        {"page": 17, "figure": "Figure 5", "summary": "The basketball hierarchy maps Experience, Achievement, and Competency to 13 metrics."},
        {"page": 18, "figure": "Experience matrix and local weights", "summary": "The first local solve exposes B1 and three normalized weights."},
        {"page": 19, "figure": "Achievement and Competency matrices with Table 5", "summary": "The two remaining local matrices, weights, and CIC 0.014 complete the basketball hierarchy."},
        {"page": 20, "figure": "Table 6", "summary": "The improved basketball list binds coach, score, and career years."},
        {"page": 20, "figure": "Football B1", "summary": "The first football local matrix starts the cross-sport replay."},
        {"page": 21, "figure": "Football B2/B3 and Tables 7-8", "summary": "Local matrices, weights, CIC, and the football top five make the transfer calculation inspectable."},
        {"page": 22, "figure": "Baseball matrix and Table 9", "summary": "The low-dimensional fallback presents its three weights and baseball top five; visual review confirms names occupy separate rows despite text-extraction merging."},
        {"page": 23, "figure": "Women-coach matrix and Table 10", "summary": "The subgroup rerun exposes a seven-by-seven matrix and seven metric weights."},
        {"page": 24, "figure": "Tables 11-12", "summary": "The women top five and cross-pool overall top five drive the gender and best-coach conclusions."},
        {"page": 24, "figure": "Figure 6", "summary": "The Pat Summitt photograph turns the analytical winner into the paper's principal person-facing result."},
        {"page": 25, "figure": "Table 13 and Figure 7", "summary": "Dean Smith's annual score table and plot establish the source's time-series example."},
        {"page": 26, "figure": "Figure 8", "summary": "Pat Summitt's annual line supports the different-gender same-sport comparison."},
        {"page": 27, "figure": "Figures 9-10", "summary": "Joe Paterno and Bobby Bowden plots support different-sport and same-sport comparisons."},
        {"page": 28, "figure": "Table 14", "summary": "Basketball model and website lists show full membership overlap with different order."},
        {"page": 29, "figure": "Tables 15-17", "summary": "Women, football, and baseball comparison tables expose 100, 100, and 40 percent membership overlap."},
        {"page": 30, "figure": "Perturbation equations and Figure 11", "summary": "Three one-factor score equations and the flowchart define the rank-change stopping process."},
        {"page": 31, "figure": "Table 18", "summary": "Negative and positive rank-change thresholds yield interval ranges for years, winning, and games."},
        {"page": 32, "figure": "Public ranking lists", "summary": "The fan-facing article presents four top-five lists in a compact command-and-result format."},
    ]
    warnings = [
        (10, "Equations 1 and 2 divide by x_max+x_min, so they generally do not map observed extrema to 0 and 1 despite being described as standardization and membership."),
        (10, "Equation 3 excludes x=x_max, has no explicit out-of-range branch, and its denominators do not center the optimum at one under general positive endpoints."),
        (11, "Equation 4 visibly prints an extra 's(i)=' inside the first b_ij branch, and the following b_m definition ends with a dangling 'min'."),
        (12, "Equation 7 visibly minimizes |y_ij-b_ji| rather than |y_ij-b_ij|, so the intended proximity target must be confirmed before implementation."),
        (14, "The printed 13-by-13 matrix contains entries such as 27.42 and visually suspicious reciprocal inconsistencies even though CIC 0.032 is reported."),
        (18, "The Experience consistency result is printed only as 'min CIC(n)=<0.1' without a numeric CIC value."),
        (20, "The paper calls five-of-five name overlap 100 percent accuracy even when the ranking order differs."),
        (24, "Pat Summitt's 0.883, baseball scores, basketball scores, and football scores come from different metric systems and scales, so the cross-sport maximum is not established as comparable."),
        (25, "The time-horizon conclusion generalizes from four selected coach plots without a documented randomization frame, statistical trend model, or uncertainty."),
        (29, "The reasonable-hypothesis test infers data reliability and assumption validity from outputs produced by those same data and assumptions."),
        (30, "The sensitivity equations use r(i,j) for normalized values and r_j for the perturbation magnitude without a clean symbol contract; the sweep can also leave feasible normalized ranges."),
        (35, "No frozen source tables, retrieval snapshots, spreadsheets, LINGO program, MATLAB code, environment lock, or end-to-end reproduction log is supplied."),
    ]
    contributions = [
        {"page": 8, "summary": "Sport-specific metric diagrams make the measurement interface visible before scoring."},
        {"page": 10, "summary": "Three direction-aware branches acknowledge that benefit, cost, and middle-optimum metrics require different treatment."},
        {"page": 11, "summary": "Dispersion-driven judgments attempt to replace purely verbal pairwise importance with a data-linked mechanism."},
        {"page": 12, "summary": "A correction program states an explicit consistency objective rather than relying only on an eigenvalue check."},
        {"page": 15, "summary": "The paper uses baseline failure to motivate a structural repair instead of presenting only its preferred model."},
        {"page": 17, "summary": "The hierarchical score exposes the distinction between local metric weights and top-level classification weights."},
        {"page": 20, "summary": "Basketball, football, baseball, and women-coach applications reveal how the interface changes with metric count and domain."},
        {"page": 25, "summary": "Annual tables and plots expose the temporal evidence behind the time-horizon narrative."},
        {"page": 28, "summary": "Four named testing modes organize consistency, overlap, assumptions, and sensitivity checks."},
        {"page": 31, "summary": "The nontechnical article translates the metric-count branch and weighted-sum logic for a sports audience."},
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 8, "summary": "Freeze every coach row, field definition, unit, source URL, retrieval time, missingness flag, and candidate-screening decision."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 10, "summary": "Replace the endpoint-sum formulas with declared min-max, target-distance, or monotone utility functions and test their bounds."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 11, "summary": "Reconstruct Equation 4 and b_m from a typed specification and verify reciprocity, boundedness, and monotonic response to dispersion."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 12, "summary": "Compare the printed b_ji CIC objective with a b_ij version and publish the complete LINGO model and solution diagnostics."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 19, "summary": "Elicit or estimate top-level class weights with documented experts, uncertainty, and sensitivity rather than importing 0.35/0.40/0.25."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 20, "summary": "Evaluate exact order, rank correlation, top-k overlap, calibration, and held-out predictive relevance as separate validation targets."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 24, "summary": "Establish measurement invariance or normalize to a common cross-sport utility scale before selecting an overall winner."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 25, "summary": "Fit hierarchical trend models across a declared coach population and report slope uncertainty, era effects, and survivorship bias."},
        {"extension_id": f"E-B-{SHORT}-009", "page": 30, "summary": "Use feasible perturbations, unambiguous symbols, multiple outputs, and global or probabilistic sensitivity rather than rank-change thresholds alone."},
        {"extension_id": f"E-B-{SHORT}-010", "page": 35, "summary": "Ship reproducible data, code, environment, intermediate matrices, assertions, and audit logs with the audience article."},
    ]
    return {
        "paper_id": PID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "Finding Out The Best All Time College Coach",
        "award_status": "outstanding",
        "source": {"relative_path": "2014\u7f8e\u8d5b\u7279\u7b49\u5956/B-28875-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical pages 1-2 are the MCM Summary Sheet; physical page 3 is printed page 1, so physical page equals printed page plus two thereafter."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["All 35 UTF-8 page files were read completely in physical-page order, with Summary, Abstract, and Introduction studied before later chapters.", "Visual review used four JPEG contact-sheet proxies of 163936-292171 bytes covering pages 1-7, 8-14, 15-25, and 26-35, plus four formula crops of 106537-135811 bytes for pages 10, 11, 12, and 30.", "No original full-page PNG or multi-image result entered model transport; all 35 original 150-DPI PNGs remain on disk as coordinate and fidelity authority.", "No blank, clipped, black, overlapping, missing, or failed-render page was found; Table 4 intentionally continues from physical page 16 to 17.", "The visually separate baseball coach rows on page 22 confirm that merged names in extracted text are a column-layout artifact rather than source content."]},
        "context_sources": [{"type": "paper", "path": "2014\u7f8e\u8d5b\u7279\u7b49\u5956/B-28875-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "text-pages", "path": f"artifacts/papers/{PID}/text/pages"}],
        "task_reconstruction": {"status": "paper-restatement-complete", "inputs": ["male and female college-coach candidates", "sport-specific career and annual records", "metric directions", "classification hierarchy", "external coach lists", "time horizon"], "outputs": ["mathematical ranking model", "time-horizon analysis", "cross-gender and cross-sport discussion", "top five in three sports", "best all-time coach", "one-to-two-page Sports Illustrated article"], "decisions": ["which coaches enter the pool", "which metrics represent performance", "when to use flat or classified weighting", "how to validate rank output", "whether scores can be compared across sports", "how to communicate the result"]},
        "section_map": [{"page": start, "section": key, "summary": summary} for key, chapter, start, end, tag, summary in CHAPTERS],
        "assumptions": [{"page": page, "summary": summary} for page, summary in assumptions],
        "data_and_preprocessing": [{"page": page, "summary": summary} for page, summary in data],
        "models": [{"model_id": item["model_id"], "page": item["page"], "summary": item["summary"]} for item in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": page, "section": "verification", "summary": summary, "verification_type": kind, "strength": strength, "limitation": limitation} for page, summary, kind, strength, limitation in verification],
        "results_trace": [{"page": page, "summary": summary} for page, summary in results],
        "contributions": contributions,
        "writing_logic": [{"page": start, "summary": summary} for _key, _chapter, start, _end, _tag, summary in CHAPTERS],
        "language_observations": [{"page": start, "summary": summary} for _key, _chapter, start, _end, _tag, summary in CHAPTERS],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The summary exposes baseline, repair, applications, tests, and audience output, but award status does not prove this sequence caused the result.", "evidence_class": "J"}, {"page": 15, "summary": "The source openly rejects model I and motivates model II, which may improve auditability without proving the revised rankings are valid.", "evidence_class": "J"}, {"page": 31, "summary": "The public article provides a direct decision artifact for the named audience, without proving its universality claims.", "evidence_class": "J"}],
        "weaknesses": [{"page": page, "summary": summary} for page, summary in warnings],
        "independent_extensions": extensions,
        "candidate_rule_impacts": [],
        "unresolved_questions": [summary for _page, summary in warnings],
        "protocol_v2_records": {},
        "review_status": "validated",
    }


def build_observations(template, language, models, card):
    observations = template.make_observations(language, models, card)
    interpretations = {
        "language": "Reuse the rhetorical move only after replacing coach pool, sport, metric, matrix, comparator, time horizon, and decision scope.",
        "modeling": "Retain raw metrics, membership rules, dispersion, matrices, local and class weights, CIC, scores, ranks, perturbations, and handoffs.",
        "logic": "Preserve the positive data-to-baseline-to-failure-to-hierarchical-repair-to-application-to-test-to-audience chain.",
        "visualization": "Keep figure or table identity, row and column semantics, formula labels, score scale, rank order, axis, and analytical purpose together.",
        "verification": "Name the matrix, CIC value, comparator, overlap definition, annual series, perturbation rule, or communication trace being checked.",
        "data": "Retain roster, sport, year range, source, retrieval state, metric definition, unit, direction, missingness, and downstream consumer.",
        "assumption": "Pair each data, metric, classification, comparability, or transfer assumption with the calculation it enables and the regime it excludes.",
        "result": "Keep local weights, class weights, score, list membership, exact order, overlap, trend, threshold, and evidence status distinct.",
        "weakness": "Record formula, inference, comparability, validation, and reproducibility defects only after positive language, organization, model, and visual learning.",
        "other": "Separate cited method or sports context from frozen input data, executable calculations, archived comparators, and independent validation evidence.",
    }
    provenance = [
        (34, "references", "Method citations identify AHP, FCE, Delphi, statistics, and sensitivity context but not the exact implementation used."),
        (35, "references", "Ranking URLs and sports sources lack frozen snapshots and retrieval dates."),
        (8, "metric hierarchy", "The basketball hierarchy preserves the declared metric interface before weighting."),
        (9, "cross-sport metrics", "Football and baseball diagrams expose different receiving-domain fields."),
        (10, "normalization support", "The formula block visibly distinguishes benefit, cost, and middle-optimum branches."),
        (11, "judgment support", "The formula block shows dispersion, b_ij, b_m, and ideal weight ratios while retaining printed defects."),
        (12, "consistency support", "The CIC objective is visually source-checked, including the b_ji term."),
        (14, "baseline matrix", "The full 13-by-13 matrix is displayed but no machine-readable input is supplied."),
        (17, "hierarchical support", "The cross-page table and Equation 9 distinguish local and class weights."),
        (20, "basketball output", "Table 6 preserves score and career-year fields for the improved list."),
        (21, "football output", "Table 8 preserves the receiving-sport list and scores."),
        (22, "baseball output", "Visual review resolves separately printed names that text extraction merged."),
        (24, "overall decision", "Tables 11 and 12 expose the subgroup and cross-pool score comparison."),
        (25, "time support", "The annual score table and plot preserve the example underlying the trend claim."),
        (29, "validation support", "The comparison tables expose exact order and top-five membership separately enough for independent recounting."),
        (30, "sensitivity support", "The equations and flowchart expose the one-factor rank-change procedure while retaining symbol ambiguity."),
    ]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = ["Apply only when candidate pool, sport, gender, era, metric definitions, source versions, transformations, hierarchy, comparator, and score scale are explicit."]
        row["counterevidence"] = ["A low CIC, top-five overlap, stable local rank, smooth career plot, transferred list, or audience-ready article does not prove measurement validity, fairness, causality, comparability, or reproducibility."]
        if row["dimension"] == "other":
            page, section, basis = provenance[other_index]
            other_index += 1
            row["page"] = page
            row["section"] = f"{section} / evidence action {other_index}"
            row["source_basis"] = basis
            row["interpretation"] = "Preserve the displayed support and its limits; do not promote citations or screenshots into frozen executable evidence."
    if other_index != len(provenance):
        raise RuntimeError(f"expected {len(provenance)} provenance observations, found {other_index}")
    return observations


def attach_rule_impacts(card, observations):
    first = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])

    def evidence(rule_id):
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])

    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain goal-to-baseline-to-failure-to-classified-repair-to-application-to-test-to-audience language with explicit claim boundaries", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "trace candidate pool and metrics through normalization, dispersion, matrices, CIC, local scores, class scores, domain reruns, tests, and decision", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "version coach pools, sports, seasons, metric definitions, directions, sources, missingness, screens, external lists, and annual series", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for data truth, omitted attributes, hierarchy sufficiency, dispersion-as-importance, class weights, and cross-sport comparability", "evidence_ids": [evidence("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain all three normalization branches, fuzzy matrix, dispersion judgments, consistency program, flat score, hierarchy composition, reruns, time series, and sensitivity equations", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine local and first-level models only through documented metric mappings, scale contracts, positive weights, and aggregation equations", "evidence_ids": [evidence("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep raw values, memberships, dispersion, pairwise entries, corrected matrices, local weights, class weights, scores, exact ranks, and top-k overlap distinct", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress normalization endpoints, judgment construction, CIC target, matrix entries, class weights, comparator definitions, cross-pool scales, annual trends, and perturbation feasibility", "evidence_ids": [evidence("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make every claim matrix-, CIC-, overlap-, trend-, sensitivity-, subgroup-, sport-, and audience-trace-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile printed formula defects, suspicious matrix entries, blank CIC, accuracy semantics, cross-sport scale, circular validation, and missing reproduction files", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain metric hierarchies, formulas, dense matrices, weight tables, ranking tables, career plots, comparison tables, flowchart, and public lists with labels and purpose", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "measure coach-by-metric normalization, dense local matrix work, CIC optimization, hierarchy reruns, annual score construction, list comparison, and sensitivity iterations", "evidence_ids": [evidence("R-B-COMP-001")]},
    ]


def build_audit(template, language, models, card, observations):
    audit = template.make_audit(language, models, card, observations)
    layouts = {item["chapter"]: item for item in language["chapter_layouts"]}
    units = language["units"]
    abstract_moves = [
        "decision importance -> IAHP-FCE destination",
        "metric selection -> standardization -> baseline top five -> 80 percent comparison",
        "classification repair -> model II -> basketball, football, baseball, and women-coach lists -> claimed perfect fit",
        "cross-pool composite scores -> Pat Summitt",
        "annual score plots -> bounded fluctuation -> slight upward trend",
        "four test families -> 0.0297 interval -> qualification",
        "simpler calculation -> claimed accuracy and utility -> practical transfer",
    ]
    introduction_moves = [
        "Sports Illustrated audience -> previous-century male-or-female coach decision -> four deliverables",
    ]
    audit["paragraph_chains"] = []
    for chapter, moves in (("abstract", abstract_moves), ("introduction", introduction_moves)):
        ids = [unit["language_unit_id"] for unit in units if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": index + 1, "dominant_move": move, "language_unit_ids": [ids[index % len(ids)]]} for index, move in enumerate(moves)]})
    audit["language_unit_dispositions"] = [{"language_unit_id": unit["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": unit["candidate_pattern_ids"], "reason": "The source move is reusable after replacing coach pool, sport, metric, matrix, comparator, time, score-scale, and decision entities."} for unit in units]
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["Only after the positive language, organization, model, result, and visual chain is complete does the final pass record formula, matrix, inference, comparability, and reproducibility warnings."],
        "section_progressions": [{"chapter": chapter, "moves": [f"input: source-checked coach pool, metric, table, formula, matrix, score, list, annual series, comparator, or audience need entering {chapter}", f"rhetorical job: perform the observed definition, method selection, derivation, failure diagnosis, repair, application, comparison, test, conclusion, or explanation in {chapter}", f"analytical job: select, classify, normalize, measure dispersion, construct or correct a matrix, weight, aggregate, rank, compare, plot, perturb, or translate the declared object in {chapter}", f"output: retain a typed metric array, membership, matrix, weight, CIC, score, rank, overlap, trend, threshold, decision, or communication artifact from {chapter}", "handoff: name the next formula, local solve, hierarchy level, sport or subgroup rerun, verification, decision, audience artifact, or evidence boundary"], "positive_pattern": "Use explicit input -> typed operation -> inspectable output -> scoped handoff; warnings remain a final pass."} for chapter in language["available_chapters"]],
        "main_argument_chains": [
            {"claim": "A coach-ranking baseline is inspectable when sport metrics pass through declared normalization, dispersion, judgment, consistency, and score equations.", "support_steps": ["sport metric diagrams", "three normalization branches", "fuzzy matrix", "dispersion", "judgment construction", "CIC correction", "weighted score"], "decision_consequence": "Reuse the baseline only after repairing its endpoint scale and printed judgment/CIC defects.", "source_pages": [8, 9, 10, 11, 12, 13]},
            {"claim": "The model-II repair responds to an observed baseline failure by separating local metric weights from first-level class weights.", "support_steps": ["baseline top five", "counterexamples", "matrix-size diagnosis", "generic two-level hierarchy", "Equation 9", "basketball hierarchy", "three local matrices"], "decision_consequence": "Keep the failure-to-repair logic, but document class-weight provenance and uncertainty.", "source_pages": [14, 15, 16, 17, 18, 19, 20]},
            {"claim": "Cross-sport and gender applications demonstrate a reusable calculation interface only when each receiving roster and metric mapping remains explicit.", "support_steps": ["basketball list", "football metrics and list", "baseball fallback", "women-coach fallback", "top-five comparison tables"], "decision_consequence": "Treat each list as a scoped rerun rather than proof of universal sport or gender invariance.", "source_pages": [20, 21, 22, 23, 24, 28, 29]},
            {"claim": "An overall best-coach decision requires a common score contract that the source's sport-specific systems do not establish.", "support_steps": ["different metric sets", "different roster sizes", "different normalization ranges", "Table 12 cross-pool scores", "Pat Summitt biography"], "decision_consequence": "Do not compare the displayed composite scores until measurement invariance or common-utility calibration is demonstrated.", "source_pages": [20, 21, 22, 23, 24]},
            {"claim": "Time-horizon and sensitivity evidence is useful when annual observations, selection rules, perturbations, outputs, and uncertainty are all visible.", "support_steps": ["Dean Smith annual table", "four career plots", "cross-case comparisons", "three perturbation equations", "rank-change flowchart", "threshold table"], "decision_consequence": "Replace anecdotal trend and rank-stability claims with population sampling, feasible perturbations, and uncertainty.", "source_pages": [25, 26, 27, 28, 29, 30, 31]},
            {"claim": "The Sports Illustrated article preserves value when its plain-language branch and lists remain connected to validated analytical evidence.", "support_steps": ["less-than-ten branch", "more-than-nine branch", "weighted score explanation", "four top-five lists", "Pat Summitt decision", "time-horizon takeaway"], "decision_consequence": "Publish the audience artifact with corrected accuracy, comparability, validation, and reproducibility disclosures.", "source_pages": [31, 32, 33]},
        ],
    }
    audit["formula_error_watch"] = {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": [
        {"model_id": models["models"][1]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-001", "page": 10, "warning": "Benefit and cost formulas divide by x_max+x_min and generally do not map observed extrema to the stated unit membership scale; verify the intended standardization before reuse."},
        {"model_id": models["models"][1]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-003", "page": 10, "warning": "The middle-optimum piecewise rule excludes x=x_max and lacks a complete endpoint and out-of-range contract."},
        {"model_id": models["models"][2]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-007", "page": 11, "warning": "The visual source prints an extra s(i)= inside the first b_ij branch and a dangling min after the b_m definition; reconstruct the intended rule before implementation."},
        {"model_id": models["models"][3]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-011", "page": 12, "warning": "The printed CIC objective compares y_ij with b_ji rather than b_ij; confirm whether the transpose is intentional before solving."},
        {"model_id": models["models"][13]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-015", "page": 30, "warning": "The sensitivity equations use r(i,j) for membership and r_j for perturbation without a clean symbol or feasibility contract, so the reported thresholds are not directly reusable."},
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
    q104 = load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q105")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q105")
    template = base.load_template_module()
    configure(q104, base, template)
    pages = {}
    for page in range(1, PAGE_COUNT + 1):
        source = TEXT_DIR / f"page-{page:04d}.txt"
        if not source.is_file():
            raise FileNotFoundError(source)
        pages[page] = source.read_text(encoding="utf-8")
    language = build_language(q104, base, template, pages)
    models = build_models(q104, base, template)
    card = build_card(models)
    card["protocol_v2_records"] = {
        "language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]},
        "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(model["governing_equations"]) for model in models["models"]), "review_status": models["review_status"]},
    }
    observations = build_observations(template, language, models, card)
    attach_rule_impacts(card, observations)
    audit = build_audit(template, language, models, card, observations)
    write_json(STAGE / "language.json", language)
    write_json(STAGE / "models.json", models)
    write_json(STAGE / "card.json", card)
    write_json(STAGE / "audit.json", audit)
    (STAGE / "observations.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "stage": str(STAGE), "pages_read": len(pages), "language_units": len(language["units"]), "models": len(models["models"]), "equations": sum(len(model["governing_equations"]) for model in models["models"]), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(card["visualization_observations"]), "warnings": len(card["weaknesses"]), "formula_warnings": len(audit["formula_error_watch"]["warnings"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
