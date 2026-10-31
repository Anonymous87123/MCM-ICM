from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2014-29696-84be6e3a"
SHORT = "29696"
SHA = "84be6e3a46047658aa778eebecbb5701706457c2a4f20f2be233ee06fe4efae4"
TYPE = "B"
YEAR = "2014"
PAGE_COUNT = 44
TEXT_DIR = ROOT / "artifacts/papers" / PID / "text/pages"
STAGE = ROOT / "tmp/q106-stage-v2"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHAPTERS = [
    ("summary-and-execution-flow", "abstract", 1, 2, "ABS", "The summary sheet and execution flow state the best-coach decision, PCA factor compression, cosine ranking, time and gender adjustments, extension, sensitivity, and robustness claims."),
    ("illustrated-problem-and-contents", "title", 3, 6, "TTL", "The illustrated problem framing, question list, and contents translate a broad all-time coach comparison into factor selection, ranking, adjustment, extension, and stability work."),
    ("introduction", "introduction", 7, 7, "INT", "The introduction frames college-coach ranking as a multi-factor comparison, identifies the intended sports and genders, and announces an evaluation-system route."),
    ("assumptions", "assumptions", 8, 8, "ASM", "The assumptions table declares representativeness, data reliability, and the role of time horizon and gender in the later adjustment models."),
    ("pca-factor-analysis", "problem-analysis", 9, 12, "PCA", "The paper lists twelve coach factors, standardizes them, builds a correlation matrix, extracts principal components, and interprets ability, college influence, and social influence."),
    ("cosine-ranking", "model-establishment", 13, 18, "COS", "The ranking model defines an ideal coach, uses cosine similarity and an adjusted form, clusters sixty coaches by Euclidean single linkage, then reports the baseline list."),
    ("baseline-results-and-time-rationale", "results", 19, 19, "RES", "The initial top-ten table is used to introduce timeline and gender differences as reasons to modify the basic similarity ranking."),
    ("timeline-regression-and-difficulty", "sensitivity-analysis", 20, 23, "TIM", "The time-line module regresses active NCAA coaches on year, converts the relation into a career-average difficulty coefficient, caps the giant effect, adjusts Google searches, and reranks."),
    ("gender-anova-and-whitening", "model-improvement", 24, 28, "GEN", "The gender module uses one-way ANOVA to select differing factors, then rescales female wins by data whitening before a final basketball ranking."),
    ("factor-pool-and-transfer", "algorithm", 29, 31, "XFR", "A factor pool maps shared and sport-specific fields before football, softball, baseball, and Chinese basketball coach ranking demonstrations."),
    ("result-presentation", "conclusion", 32, 35, "OUT", "Photo-backed basketball, football, and baseball tables and a U.S. regional map turn the ranking outputs into a decision-facing presentation."),
    ("stability-and-robustness", "sensitivity-robustness", 36, 37, "ROB", "The source compares rankings before and after adjustments, adds unspecified noise to the first fifteen coaches, and uses limited order stability as stability and robustness evidence."),
    ("strengths-weaknesses", "strengths-limitations", 38, 38, "SWK", "The closing evaluation names credibility, accessibility, self-improvement, reliability, and adaptability, then admits narrow-factor and lower-ability ranking limits."),
    ("conclusion-and-references", "references", 39, 40, "REF", "The conclusion restates the similarity, timeline, gender, transfer, and robustness claims; the references expose web and method dependencies without frozen computational inputs."),
    ("appendix-data", "data-preprocessing", 41, 44, "APP", "The appendix supplies original and modified rows for the sixty basketball coaches, making several transformations inspectable while leaving their full pipeline and provenance incomplete."),
]

PATTERNS = [
    "LP-B-SUMMARY-FACTOR-RANK-ADJUST-TRANSFER-CHECK",
    "LP-B-PROBLEM-QUESTION-DELIVERABLE-MODEL-ROUTE",
    "LP-B-ASSUMPTION-ROLE-ENABLED-OPERATION-BOUNDARY",
    "LP-B-FACTOR-STANDARDIZE-CORRELATE-COMPRESS-INTERPRET",
    "LP-B-IDEAL-VECTOR-SIMILARITY-CLUSTER-RANK",
    "LP-B-DEFECT-EXAMPLE-ADJUSTMENT-RERANK",
    "LP-B-REGRESSION-ERA-COEFFICIENT-CAREER-AVERAGE-CAP",
    "LP-B-TEST-FACTOR-ANOVA-TRANSFORM-RERUN",
    "LP-B-FACTOR-POOL-RECEIVING-FIELDS-RERUN-SCOPE",
    "LP-B-TABLE-RESULT-COMPARISON-INTERPRETATION",
    "LP-B-NOISE-INPUT-RANK-COMPARISON-BOUNDARY",
    "LP-B-STRENGTH-LIMIT-REPAIR-TRANSFER",
    "LP-B-REFERENCE-PROVENANCE-REPRODUCTION-BOUNDARY",
    "LP-B-APPENDIX-RAW-MODIFIED-TRACEABILITY",
    "LP-B-VISUAL-FIGURE-TABLE-FORMULA-DECISION-ROLE",
]

MOVES = [
    ("decision-route", "Lead from the coach-selection decision through factor construction, ranking, corrections, extensions, and a bounded final list.", "decision -> factor system -> rank -> adjustment -> rerun -> scope"),
    ("factor-compression", "Define variables before standardization, correlation, eigenvalue selection, loading interpretation, and component naming.", "factors -> standardized matrix -> PCA -> retained components -> meanings"),
    ("ideal-comparison", "Make the ideal reference vector explicit before comparing each coach, exposing the cosine limitation, and adding a correction.", "reference vector -> similarity -> counterexample -> adjustment -> rank"),
    ("hierarchical-clustering", "Separate standardization, a declared distance rule, linkage, cluster selection, and the rank-eligible group.", "coach rows -> z scores -> distance -> linkage -> cluster -> eligible ranking"),
    ("timeline-adjustment", "Show an observed timeline relation before deriving a career aggregate, cap, social correction, and rerank.", "year data -> regression -> coefficient -> career aggregate -> corrected inputs -> rank"),
    ("gender-adjustment", "Test the factor difference before selecting a transformation and showing its before-and-after variance.", "gender groups -> ANOVA -> selected factor -> whitening -> variance check -> rank"),
    ("transfer-interface", "Map fields in the receiving sport or country before applying a common ranking calculation.", "receiving domain -> factor pool -> field mapping -> rerun -> scoped list"),
    ("stability-boundary", "Name changed inputs and the observed rank response before limiting the robustness claim to that perturbation.", "declared adjustment or noise -> output list -> comparison -> bounded inference"),
]

EXAMPLES = [
    ("A coach-ranking study declares every career factor, its direction, and its source before using a composite comparison.", "Later conclusions remain conditional on the roster, definitions, and source version."),
    ("A PCA section reports the standardized variables, correlation structure, retained components, and loading interpretation in that order.", "A component label is treated as an interpretation of the displayed loadings, not a measured trait."),
    ("A similarity model constructs an ideal reference vector and then demonstrates a direction-only failure case before changing the transformation.", "The corrected score is not called valid until its scale and comparator are independently tested."),
    ("A time adjustment presents the observed relation, the coefficient formula, the career aggregation, and the cap before reranking.", "Its causal interpretation remains limited when the regression inputs and calibration rationale are incomplete."),
    ("A gender analysis tests each candidate field before applying a variance transformation to the selected fields.", "Equalized dispersion is reported as a transformation result, not proof that the underlying comparisons are fair."),
    ("A transfer section exposes the receiving sport's fields before reusing the model interface.", "A top-five list demonstrates a scoped rerun, not cross-sport external validation."),
    ("A robustness section names the perturbed records and compares the resulting rank order with the original order.", "Stable top places under one noise realization do not establish parameter, data, or structural robustness."),
    ("An appendix preserves original and modified rows so that model inputs can be reconciled.", "A reproducible claim still needs transformation code, sources, seeds, and a full provenance ledger."),
]

PROFILES = {
    "abstract": ("Compress the decision, factor route, baseline ranking, two corrections, transfer, and bounded stability claim without conflating them.", ["decision target", "PCA factors", "similarity model", "time and gender correction", "scope"], ["decision", "model route", "outputs", "qualification"]),
    "title": ("Turn the contest prompt into explicit questions and deliverables before the method sections begin.", ["audience", "sports", "gender", "ranking questions", "planned models"], ["context", "questions", "route", "handoff"]),
    "introduction": ("Locate the coach-comparison problem, data need, and multi-factor evaluation intent.", ["decision context", "candidate scope", "factor variety", "planned evaluation"], ["problem", "motivation", "scope", "method handoff"]),
    "assumptions": ("Tie each representativeness, data, timeline, and gender assumption to the operation it permits.", ["assumption", "enabled calculation", "excluded uncertainty", "consumer"], ["entity", "assumption", "operation", "boundary"]),
    "problem-analysis": ("Build the twelve-factor PCA route from definitions through standardization and loading interpretation.", ["factor", "sample matrix", "standardization", "correlation", "component", "loading"], ["inputs", "transform", "PCA result", "interpretation"]),
    "model-establishment": ("Move from ideal vector and cosine comparison through adjustment and clustering into a rank-eligible coach group.", ["ideal coach", "vector", "cosine", "counterexample", "distance", "cluster"], ["reference", "score", "repair", "selection"]),
    "results": ("Report the baseline top list and identify the temporal and gender comparison problems that trigger later modules.", ["rank", "factor difference", "timeline", "gender", "next model"], ["baseline output", "diagnosis", "handoff"]),
    "sensitivity-analysis": ("Derive the timeline correction in observable steps from regression through career averaging and capped adjustment.", ["year", "active-coach count", "regression", "difficulty", "career interval", "social coefficient"], ["data", "relation", "coefficient", "rerun"]),
    "model-improvement": ("Use ANOVA and a visible whitening transformation to modify only selected gender-sensitive fields.", ["gender groups", "ANOVA statistic", "p value", "variance", "whitening", "rank"], ["test", "selected fields", "transform", "result"]),
    "algorithm": ("Expose the factor-pool interface before rerunning it for another sport or country.", ["shared fields", "domain-specific fields", "mapping", "receiving roster", "rank"], ["pool", "mapping", "rerun", "scope"]),
    "conclusion": ("Present result tables and maps as evidence-bearing outputs connected to their roster and factor scope.", ["ranked person", "career values", "table", "map", "interpretation"], ["result", "display", "comparison", "boundary"]),
    "sensitivity-robustness": ("Separate adjustment comparison from input-noise response and state exactly which rank stability was observed.", ["changed factor", "noise", "affected coaches", "before list", "after list", "claim limit"], ["perturbation", "comparison", "result", "limit"]),
    "strengths-limitations": ("Pair each claimed benefit with its mechanism and each stated weakness with a precise untested boundary.", ["strength", "mechanism", "weakness", "repair"], ["benefit", "evidence", "limitation", "next action"]),
    "references": ("Distinguish citations and links from archived data, transformations, code, and independent validation.", ["source", "method role", "input dependency", "missing artifact"], ["citation", "use", "provenance boundary"]),
    "data-preprocessing": ("Use original and modified appendix rows to trace transformations without inventing missing pipeline detail.", ["original row", "modified row", "field", "transform", "consumer"], ["source data", "derived data", "comparison", "boundary"]),
}


def configure(q104, base, template) -> None:
    values = {"PID": PID, "SHORT": SHORT, "SHA": SHA, "TYPE": TYPE, "YEAR": YEAR, "PAGE_COUNT": PAGE_COUNT, "TEXT_DIR": TEXT_DIR, "STAGE": STAGE, "CHAPTERS": CHAPTERS, "PATTERNS": PATTERNS, "MOVES": MOVES, "EXAMPLES": EXAMPLES}
    for module in (q104, base, template):
        for name, value in values.items():
            setattr(module, name, value)


def build_language(q104, base, template, pages):
    configure(q104, base, template)
    language = q104.build_language(base, template, pages)
    for unit in language["units"]:
        purpose, slots, order = PROFILES[unit["chapter"]]
        unit["function"] = purpose
        unit["reusable_pattern"] = " -> ".join(order)
        unit["information_order"] = order
        unit["reusable_elements"] = slots
        unit["prohibited_generalizations"] = [
            "Do not transfer coach lists, PCA labels, similarity scores, time coefficients, gender transformations, sport fields, or noise results without rebuilding the receiving data and measurement contract.",
            "Do not call rank stability, ANOVA significance, a regression fit, or a variance match external validation, causal proof, or universal fairness.",
        ]
        unit["features"]["quantitative_role"] = "bind a factor value, standardized value, loading, score, distance, coefficient, p value, variance, rank, and perturbation to its declared operation"
        unit["features"]["transition"] = "first, then, based on, therefore, however, accordingly, likewise, and finally connect factors, models, corrections, extensions, and evidence boundaries"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 44 UTF-8 physical-page files were read sequentially. Eight one-at-a-time byte-bounded JPEG contact sheets covered pages 1-44, and ten byte-bounded equation or plot crops checked the formula-dense regions."
        layout["ambiguities"] = [
            "Text extraction flattens sums, roots, matrix indices, table rows, and chart labels; original 150-DPI PNGs remain authoritative and the JPEGs were transport-only review proxies.",
            "Physical pages 1-2 are summary and execution-flow sheets; printed page numbering begins later, so physical-page citations are retained throughout.",
        ]
        if layout["chapter"] == "abstract":
            layout["paragraph_count"] = 7
            layout["paragraph_functions"] = ["State the coach-selection purpose and multi-factor scope.", "Name PCA factor analysis and the component meanings.", "Introduce the ideal coach, cosine ranking, and clustering route.", "Preview time-line regression and difficulty adjustment.", "Preview ANOVA and data whitening for gender differences.", "Name cross-sport and country factor-pool extensions.", "Close with stability, robustness, and intended use claims."]
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = 4
            layout["paragraph_functions"] = ["Frame the all-time college-coach decision.", "Explain why one metric cannot represent coaching ability.", "Name data collection and factor analysis as the bridge to ranking.", "Hand off from background to assumptions and PCA."]
    return language


def eq(q104, index, page, label, latex, symbols, purpose, confidence="high"):
    return q104.equation(index, page, label, latex, symbols, purpose, confidence)


def build_models(q104, base, template):
    configure(q104, base, template)
    pca = [
        eq(q104, 1, 10, "principal-component combination", r"Z_i=\sum_{j=1}^{12}a_{ij}X_j", ["Z_i", "a_ij", "X_j"], "Express each retained component as a weighted combination of standardized coach factors.", "medium"),
        eq(q104, 2, 10, "z-score standardization", r"X'_i=(X_i-E_i)/S_i", ["X_i", "E_i", "S_i", "X'_i"], "Center and scale a factor before correlation analysis."),
        eq(q104, 3, 10, "correlation coefficient", r"r_{ij}=\frac{\sum_k(X_{ki}-E_i)(X_{kj}-E_j)}{\sqrt{\sum_k(X_{ki}-E_i)^2}\sqrt{\sum_k(X_{kj}-E_j)^2}}", ["r_ij", "X_ki", "X_kj", "E_i", "E_j"], "Populate the factor correlation matrix.", "medium"),
        eq(q104, 4, 11, "eigenvalue equation", r"\det(\lambda I-R)=0", ["lambda", "I", "R"], "Obtain the correlation-matrix eigenvalues for principal components."),
        eq(q104, 5, 11, "component contribution", r"V_i=\lambda_i/\sum_{k=1}^{p}\lambda_k", ["V_i", "lambda_i", "p"], "Calculate the explained-variance share of component i."),
        eq(q104, 6, 11, "cumulative contribution", r"P_m=\sum_{i=1}^{m}\lambda_i/\sum_{i=1}^{p}\lambda_i", ["P_m", "lambda_i", "m", "p"], "Calculate the cumulative retained-component share.", "medium"),
    ]
    ranking = [
        eq(q104, 7, 14, "dot-product cosine identity", r"a\cdot b=\lVert a\rVert\lVert b\rVert\cos\theta", ["a", "b", "theta"], "Relate vector angle to cosine similarity."),
        eq(q104, 8, 14, "coach-to-ideal cosine", r"\cos\theta=\frac{X_i\cdot X_s}{\lVert X_i\rVert\lVert X_s\rVert}", ["X_i", "X_s", "theta"], "Compare a coach vector with the ideal-coach vector.", "medium"),
        eq(q104, 9, 15, "coach factor vector", r"V_i=(x_{i1},x_{i2},\ldots,x_{i12})", ["V_i", "x_ij"], "Represent one coach by twelve collected factors."),
        eq(q104, 10, 16, "adjusted cosine input", r"x'_{ij}=\frac{x_{ij}-E_j}{X_{j,max}-X_{j,min}}", ["x_ij", "E_j", "X_jmax", "X_jmin"], "Center a factor before adjusted cosine comparison."),
        eq(q104, 11, 16, "factor mean", r"\bar{x}_j=\frac{1}{n}\sum_i x_{ij}", ["xbar_j", "x_ij", "n"], "Calculate the factor mean for standardization."),
        eq(q104, 12, 16, "factor standard deviation", r"s_j=\sqrt{\frac{1}{n-1}\sum_i(x_{ij}-\bar{x}_j)^2}", ["s_j", "x_ij", "xbar_j", "n"], "Calculate the factor standard deviation.", "medium"),
        eq(q104, 13, 16, "cluster z-score", r"x^*_{ij}=\frac{x_{ij}-\bar{x}_j}{s_j}", ["xstar_ij", "x_ij", "xbar_j", "s_j"], "Standardize coach rows before distance clustering."),
        eq(q104, 14, 17, "Minkowski distance", r"d_{ij}=[\sum_{k=1}^{p}|x_{ik}-x_{jk}|^q]^{1/q}", ["d_ij", "x_ik", "x_jk", "q", "p"], "Measure distance between two coach vectors.", "medium"),
        eq(q104, 15, 17, "Euclidean distance", r"d_{ij}(2)=[\sum_{k=1}^{p}(x_{ik}-x_{jk})^2]^{1/2}", ["d_ij", "x_ik", "x_jk", "p"], "Specialize the clustering metric to q=2."),
        eq(q104, 16, 17, "single-linkage distance", r"D_k(p,q)=\min\{d_{jl}:j\in G_p,l\in G_q\}", ["D_k", "G_p", "G_q", "d_jl"], "Define distance between two clusters."),
        eq(q104, 17, 17, "single-linkage merge", r"D_{kr}=\min\{D_{kp},D_{kq}\}", ["D_kr", "D_kp", "D_kq"], "Update distance after clusters p and q merge.", "medium"),
    ]
    timeline = [
        eq(q104, 18, 20, "active-coach regression", r"A(t)=0.734t-1421.8", ["A_t", "t"], "Approximate annual active NCAA coaches from calendar year."),
        eq(q104, 19, 20, "difficulty proportionality", r"D(t)=kA(t)", ["D_t", "k", "A_t"], "Declare a difficulty coefficient proportional to active coach count."),
        eq(q104, 20, 21, "printed difficulty coefficient", r"D(t)=(0.734t-1421.8)/k", ["D_t", "k", "t"], "Record the later printed coefficient form for source reconciliation.", "medium"),
        eq(q104, 21, 21, "career-average difficulty", r"C_i=\frac{1}{T_{i,end}-T_{i,start}}\int_{T_{i,start}}^{T_{i,end}}D(t)\,dt", ["C_i", "T_istart", "T_iend", "D_t"], "Aggregate difficulty over a coach's career."),
        eq(q104, 22, 21, "difficulty min-max", r"C_{si}=\frac{C_i-C_{min}}{C_{max}-C_{min}}", ["C_si", "C_i", "C_min", "C_max"], "Scale career difficulty across coaches."),
        eq(q104, 23, 22, "capped difficulty adjustment", r"C'_i=\begin{cases}1.5,&C_{si}\ge0.5\\C_{si}+1,&C_{si}<0.5\end{cases}", ["Cprime_i", "C_si"], "Cap the source's giant-effect difficulty multiplier.", "medium"),
        eq(q104, 24, 22, "social-influence coefficient", r"G=\frac{s-s_{min}}{s_{max}-s_{min}}+1", ["G", "s", "s_min", "s_max"], "Adjust Google-search visibility by start-coaching year."),
    ]
    gender = [
        eq(q104, 25, 24, "ANOVA between-group sum", r"SSA=\sum_i n_i\bar{y}_i^2-N\bar{y}^2", ["SSA", "n_i", "ybar_i", "N", "ybar"], "Compute the ANOVA between-group component.", "medium"),
        eq(q104, 26, 24, "ANOVA within-group sum", r"SSE=\sum_i\sum_k y_{i,k}^2-\sum_i n_i\bar{y}_i^2", ["SSE", "y_ik", "n_i", "ybar_i"], "Compute the ANOVA residual component."),
        eq(q104, 27, 24, "ANOVA statistic", r"F=\frac{SSA/(I-1)}{SSE/(N-I)}", ["F", "SSA", "SSE", "I", "N"], "Form the one-way ANOVA test statistic.", "medium"),
        eq(q104, 28, 26, "female-win whitening", r"x'_{fwi}=E_{fw}+(x_{fwi}-E_{fw})\sqrt{S_{mw}^2/S_{fw}^2}", ["xprime_fwi", "E_fw", "x_fwi", "S_mw", "S_fw"], "Rescale female win values to the male variance target.", "medium"),
    ]

    def model(index, page, section, family, purpose, inputs, outputs, equations):
        return q104.make_model(base, template, f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, section, family, purpose, inputs, outputs, equations)

    models = [
        model(1, 8, "assumptions and factor collection", "comparison-system setup", "Declare the sixty-coach basketball sample and twelve candidate factors before evaluation.", ["coach records", "twelve factor definitions", "gender and timeline labels"], ["coach-by-factor table", "scope assumptions"], []),
        model(2, 9, "principal component analysis", "PCA factor compression", "Standardize twelve factors, construct correlations, retain components, and interpret their loadings.", ["coach-by-factor matrix", "means", "standard deviations"], ["correlation matrix", "eigenvalues", "Z1-Z3", "component labels"], pca),
        model(3, 13, "ideal-coach cosine ranking", "vector similarity", "Construct the ideal factor vector and score every coach by cosine similarity.", ["coach vectors", "factor maxima"], ["similarities", "baseline rank"], ranking[:3]),
        model(4, 16, "adjusted cosine and clustering", "standardization and hierarchical clustering", "Center factor values, use Euclidean single linkage, and select the best cluster for ranking.", ["coach factor table", "means", "standard deviations"], ["adjusted vectors", "clusters", "rank-eligible group"], ranking[3:]),
        model(5, 19, "baseline ranking analysis", "rank result interpretation", "Use the baseline top ten to identify timeline and gender comparability problems.", ["baseline similarities", "coach attributes"], ["top-ten table", "adjustment requirements"], []),
        model(6, 20, "timeline regression", "era difficulty adjustment", "Regress active coaches on time and translate the result to a career-average capped difficulty coefficient.", ["active-coach years", "career start/end years"], ["D(t)", "C_i", "C'_i"], timeline[:6]),
        model(7, 22, "social influence correction", "search-era adjustment", "Normalize coaching start year and divide search counts by the social-influence coefficient.", ["Google searches", "start year"], ["G", "adjusted search factor"], timeline[6:]),
        model(8, 24, "gender difference screen", "one-way ANOVA", "Test male and female factor differences before selecting fields for adjustment.", ["male and female factor groups", "alpha=0.05"], ["SSA", "SSE", "F", "p values", "selected fields"], gender[:3]),
        model(9, 25, "gender data whitening", "variance matching", "Rescale affected female factor values and verify the displayed before/after variance.", ["female wins", "male and female means and variances"], ["modified female wins", "variance comparison"], gender[3:]),
        model(10, 29, "factor-pool transfer", "cross-sport and country mapping", "Map common and sport-specific factors before producing receiving-domain coach lists.", ["factor pool", "football, softball, baseball, Chinese coach data"], ["mapped factor sets", "top-five lists"], []),
        model(11, 32, "result presentation", "decision-facing ranking output", "Present basketball, football, baseball, and regional outputs with named coaches and selected statistics.", ["ranked score outputs", "coach records"], ["tables", "portraits", "regional map"], []),
        model(12, 36, "stability and noise test", "local perturbation check", "Compare adjusted rankings and add noise to the first fifteen coach records before comparing top places.", ["before/after rankings", "noisy first-fifteen factors"], ["rank comparison", "limited stability observation"], []),
    ]
    edges = [
        {"from_model_id": models[0]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "Declared coach records and twelve factor columns enter standardization and PCA."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[2]["model_id"], "handoff": "The chosen factor system supplies the ideal vector and coach comparison dimensions."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "The cosine limitation motivates centering and cluster-based eligibility."},
        {"from_model_id": models[3]["model_id"], "to_model_id": models[4]["model_id"], "handoff": "The initial rank reveals timeline and gender variables that are not yet adjusted."},
        {"from_model_id": models[4]["model_id"], "to_model_id": models[5]["model_id"], "handoff": "Timeline data and career dates enter the active-coach regression and career average."},
        {"from_model_id": models[5]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "Start year is reused to normalize the Google-search social-influence field."},
        {"from_model_id": models[5]["model_id"], "to_model_id": models[7]["model_id"], "handoff": "The timeline-adjusted coach table is the input on which gender differences are tested."},
        {"from_model_id": models[7]["model_id"], "to_model_id": models[8]["model_id"], "handoff": "ANOVA-selected factors receive the variance-matching transformation."},
        {"from_model_id": models[8]["model_id"], "to_model_id": models[9]["model_id"], "handoff": "The adjusted basketball interface is generalized through the factor pool."},
        {"from_model_id": models[9]["model_id"], "to_model_id": models[10]["model_id"], "handoff": "Receiving-domain ranks are displayed as tables and regional context."},
        {"from_model_id": models[10]["model_id"], "to_model_id": models[11]["model_id"], "handoff": "The reported lists provide before/after outputs for adjustment and noise comparison."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def build_card(models):
    assumptions = [
        (8, "The chosen factors are assumed to represent coach ability and the selected coaches to represent the intended leading pool."),
        (8, "Collected statistics and Google-search counts are assumed reliable enough for the calculations."),
        (8, "Timeline horizon and gender are assumed to create ranking differences that can be addressed by the named adjustments."),
        (20, "The number of active NCAA coaches is assumed proportional to coaching difficulty."),
        (20, "The fitted active-coach relation is assumed adequate for all career years used in the integral."),
        (22, "The giant-effect cap of 1.5 is chosen as a minor rather than dominant correction without a calibration criterion."),
        (24, "One-way ANOVA at alpha 0.05 is assumed appropriate for each factor comparison."),
        (26, "Matching a selected variance is assumed to remove enough gender influence for reranking."),
        (29, "The factor pool is assumed sufficiently portable across sports and countries after field selection."),
    ]
    data = [
        (9, "Twelve factors include tenure, NCAA tenure, wins, losses, games, winning rate, teams, Final Fours, NCAA championships, conference championships, Google searches, and awards."),
        (15, "The ideal coach vector combines factor-wise maxima from the sixty coach rows."),
        (18, "Table 5 assigns sixty coaches to clusters before the first-group ranking calculation."),
        (20, "The timeline regression uses active NCAA coaches from 1942 to 2013 but does not ship the source series."),
        (21, "Career start and stop years are used to integrate a coach-specific difficulty coefficient."),
        (25, "Table 9 lists p values for factor comparisons between thirty male and thirty female coaches."),
        (26, "Table 10 reports male and female win standard deviations and variances before whitening."),
        (30, "Tables 13-15 provide football, softball, and baseball top-five outputs but not their complete source rosters."),
        (41, "Appendix rows provide original basketball records, and later pages show modified wins, games, and winning rates."),
    ]
    verification = [
        (11, "Table 2 reports eigenvalues and cumulative contribution rates for all twelve principal components.", "PCA intermediate output", "The retained component calculation is visible.", "Factor measurement and component-retention criterion are not independently validated."),
        (12, "Table 3 displays factor loadings for Z1, Z2, and Z3.", "loading inspection", "The component labels can be checked against displayed loadings.", "Labels remain interpretive and Google-search provenance is absent."),
        (18, "Table 5 displays cluster membership for the sixty coach records.", "cluster-output inspection", "The selected cluster step is visible.", "The number of clusters and cut criterion are not justified."),
        (23, "Tables 7 and 8 compare the top ten before and after the timeline adjustment.", "before-after rank comparison", "The effect of the stated correction is inspectable.", "Near-unchanged order does not validate the difficulty or search mechanism."),
        (25, "Table 9 reports ANOVA p values for factor differences.", "hypothesis-test output", "The selected significance mechanism is displayed.", "Definitions, degrees of freedom, multiple testing, and raw factor distributions are incomplete."),
        (27, "Table 11 compares male and female win variance after the whitening transformation.", "transformation check", "The reported variance target can be compared.", "A variance match is not evidence of comparability or fairness."),
        (30, "Tables 13-15 show top-five lists in three receiving sports.", "transfer demonstration", "The field-mapping result is visible.", "No independent receiving-sport validation or data archive is supplied."),
        (36, "Table 20 compares rank order before and after combined adjustments.", "local stability comparison", "Several top positions can be checked.", "The changed settings, data versions, and acceptance threshold are not fully specified."),
        (37, "Table 22 compares the noisy and original lists after noise is added to the first fifteen coaches.", "noise perturbation", "A limited top-rank response is shown.", "Noise distribution, magnitude, seed, repetitions, and full-rank effect are absent."),
    ]
    results = [
        (12, "The source names Z1 coach ability, Z2 college influence, and Z3 social influence after inspecting the component matrix."),
        (19, "The initial cosine ranking lists John Wooden first, followed by Geno Auriemma and Pat Summitt."),
        (23, "Timeline adjustment replaces John Thompson with Billy Donovan in the displayed top ten while retaining the leading nine places."),
        (28, "After gender and timeline adjustment, Tara VanDerveer appears ninth and Tom Izzo tenth in the displayed top ten."),
        (30, "The transfer tables rank Bear Bryant first in football and Sue Enquist first in softball; Table 15 is labeled softball despite baseball names."),
        (31, "The country extension reports a Chinese basketball coach top five after an unspecified factor-pool update."),
        (32, "The final basketball presentation begins with John Wooden, Geno Auriemma, Pat Summitt, Dean Smith, and Mike Krzyzewski."),
        (37, "The noise comparison keeps John Wooden, Geno Auriemma, and Pat Summitt as the displayed first three after perturbation."),
    ]
    visuals = [
        {"page": 1, "figure": "Summary Sheet", "summary": "The source's first page states the complete decision, method, adjustment, extension, and stability route."},
        {"page": 2, "figure": "Model Execution Flow", "summary": "The flow table makes PCA, clustering, cosine ranking, time and gender corrections, extension, sensitivity, and robustness explicit."},
        {"page": 3, "figure": "Figure 1", "summary": "The illustrative sports panels communicate the multi-sport best-coach objective before formulas."},
        {"page": 4, "figure": "Figure 2", "summary": "The idealistic-coach graphic binds observed coach factors to the ideal-vector comparison."},
        {"page": 8, "figure": "Table 1", "summary": "The assumptions table is the source contract for representativeness, data reliability, timeline, and gender adjustments."},
        {"page": 10, "figure": "PCA equations and correlation matrix", "summary": "The visual formula block preserves standardization, correlation, and component construction."},
        {"page": 11, "figure": "Table 2", "summary": "Eigenvalues and cumulative contribution rates establish the displayed retained-component evidence."},
        {"page": 12, "figure": "Table 3", "summary": "The component loading matrix supports the named ability, college-influence, and social-influence labels."},
        {"page": 13, "figure": "Figure 1 component influence", "summary": "The bar chart visually orders Z1, Z2, and Z3 influence."},
        {"page": 14, "figure": "Figure 2 and cosine formula", "summary": "The vector-angle diagram and dot-product expression define similarity and reveal the source's direction-only comparison."},
        {"page": 15, "figure": "Table 4 and Figure 3", "summary": "The ideal coach row and vector comparison explain the baseline ranking reference."},
        {"page": 16, "figure": "Figure 4 and standardization formulas", "summary": "The overlap example motivates adjusted cosine and exposes the factor transforms."},
        {"page": 17, "figure": "Single-linkage formulas and Figure 5", "summary": "Minkowski, Euclidean, linkage, merge equations, and the cluster plot show the eligibility calculation."},
        {"page": 18, "figure": "Table 5", "summary": "The cluster-membership table records the actual grouping used before ranking."},
        {"page": 19, "figure": "Table 6", "summary": "The baseline top-ten table is the direct comparison object that triggers adjustment modules."},
        {"page": 20, "figure": "Figure 6", "summary": "The active-coach scatter, fit line, R-squared label, and prediction-interval label are the timeline-regression evidence."},
        {"page": 21, "figure": "Figure 7 and career integral", "summary": "The difficulty line and career-average equation connect annual trend to individual correction."},
        {"page": 22, "figure": "Figure 8", "summary": "The capped difficulty-adjustment plot and social coefficient define the two time-line transformations."},
        {"page": 23, "figure": "Tables 7-8", "summary": "The before-after ranking tables reveal which timeline changes actually occur."},
        {"page": 25, "figure": "Table 9", "summary": "The p-value table is the visual gate for selecting gender-sensitive factors."},
        {"page": 26, "figure": "Table 10, Figure 9, and whitening equations", "summary": "Male/female win variance and the whitening expression are shown before the transformation claim."},
        {"page": 27, "figure": "Table 11 and Figure 10", "summary": "The post-adjustment variance display is the source's direct whitening check."},
        {"page": 29, "figure": "Figure 11", "summary": "The factor-pool diagram separates shared and sport-specific fields before transfer."},
        {"page": 30, "figure": "Tables 13-15", "summary": "Three cross-sport top-five tables expose the transfer results and a mislabeled final table."},
        {"page": 32, "figure": "Table 17", "summary": "Photo-backed basketball ranking rows keep person, tenure, wins, games, and rate together."},
        {"page": 35, "figure": "Table 19 and Figure 12", "summary": "The baseball table and U.S. regional map turn rank outputs into decision-facing displays."},
        {"page": 36, "figure": "Table 20", "summary": "The adjusted versus unadjusted top-ten table supports the stability comparison."},
        {"page": 37, "figure": "Table 21, Figure 13, and Table 22", "summary": "The noise test displays changed rows, overlapping color-coded marks, and a limited rank comparison."},
        {"page": 41, "figure": "Appendix original data", "summary": "The original coach records permit partial reconciliation of the twelve-factor input table."},
        {"page": 42, "figure": "Appendix modified data start", "summary": "The modified rows expose that timeline and gender operations change wins, games, and winning rate."},
        {"page": 43, "figure": "Appendix modified data continuation", "summary": "The continuation preserves transformations for the remaining coaches."},
    ]
    warnings = [
        (10, "The displayed correlation denominator's second sum is indexed i=1..n while the term uses x_kj, leaving a visible index mismatch."),
        (11, "The cumulative contribution numerator visibly uses an inconsistent upper index, so the retained-component formula needs a typed reconstruction before implementation."),
        (14, "The printed cosine formula continues below the page region and the text states eleven standardized dimensions despite later defining a twelve-factor vector."),
        (16, "The standard-deviation summand visibly uses xbar_ij while the mean is defined as xbar_j, a subscript inconsistency."),
        (17, "The printed general Minkowski expression omits absolute values and the merge line labels D_kr squared while the right side is an unsquared minimum distance."),
        (20, "The source first states D(t)=kA(t) but then prints D(t)=(0.734t-1421.8)/k, so the role of k and units are contradictory."),
        (22, "The giant-effect piecewise rule is visually ambiguous and its 0.5 threshold and 1.5 cap are not calibrated or sensitivity-tested."),
        (24, "The ANOVA notation defines N as the two coach kinds while using N-I degrees of freedom, and the printed grand-mean notation is inconsistent."),
        (25, "The narrative says losses have p>alpha although Table 9 prints L=0.004, which is below 0.05."),
        (26, "The source's printed whitening ratio must be reconciled with the intended variance target before using the formula; a variance claim alone does not establish fair comparison."),
        (30, "Table 15 is titled Softball Coach Ranking but lists baseball names and repeats Ron Fraser, so the transfer output cannot be accepted without source reconciliation."),
        (37, "The noise test gives no distribution, scale, random seed, repetitions, or full-order effect and visually relies on overlapping red and blue marks."),
        (40, "No frozen raw data, source snapshots, factor definitions, transformation code, clustering settings, regression data, ANOVA output, seeds, or independent validation package is supplied."),
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 9, "summary": "Publish a versioned data dictionary for all twelve factors, including source, collection date, unit, direction, missingness, and each coach identifier."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 10, "summary": "Implement and test PCA equations with unambiguous summation indices, a justified retention rule, sign conventions, and reproducible component labels."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 14, "summary": "Compare cosine, scale-aware distances, and rank-aggregation alternatives using a predeclared fairness and predictive criterion."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 17, "summary": "Specify linkage, cluster-count selection, distance scaling, and cluster stability resampling before selecting the rank-eligible group."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 20, "summary": "Fit and publish a timeline model with units, residual diagnostics, confidence intervals, sensitivity to historical data definition, and a causal boundary."},
        {"extension_id": f"E-B-{SHORT}-006", "page": 24, "summary": "Use a documented ANOVA or regression design with correct degrees of freedom, multiplicity handling, effect sizes, diagnostics, and explicitly justified transformation targets."},
        {"extension_id": f"E-B-{SHORT}-007", "page": 29, "summary": "Require sport-specific field maps, normalized score contracts, complete receiving rosters, and held-out comparators before treating transfer lists as validated."},
        {"extension_id": f"E-B-{SHORT}-008", "page": 37, "summary": "Run seeded replicated perturbations across data, parameters, clustering, timeline, and transformation choices; report full-rank distributions and failure cases."},
        {"extension_id": f"E-B-{SHORT}-009", "page": 40, "summary": "Release raw and derived tables, source snapshots, code, environment lock, model configuration, regression and ANOVA outputs, and an end-to-end reproduction log."},
    ]
    return {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": SHORT,
        "title": "Looking for the best all time college coaches? See here!", "award_status": "outstanding",
        "source": {"relative_path": "2014美赛特等奖/B-29696-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical pages 1-2 are the summary and execution-flow sheets; later printed page labels differ, so this record uses physical-page citations."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["All 44 UTF-8 physical-page files were read sequentially, with the summary sheet and introduction preceding the later models.", "Eight JPEG contact-sheet proxies of 42,333-167,386 bytes covered every physical page one at a time; ten focused JPEG crops of 95,756-213,965 bytes checked formula and plot fidelity.", "No original full-page PNG or multi-image result entered model transport; originals remain on disk as coordinate authority.", "No blank, clipped, overlapping, or missing page was found. Physical page 44 contains only the terminal appendix row by source design."]},
        "context_sources": [{"type": "paper", "path": "2014美赛特等奖/B-29696-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "text-pages", "path": f"artifacts/papers/{PID}/text/pages"}],
        "task_reconstruction": {"status": "paper-restatement-complete", "inputs": ["male and female college coach records", "twelve basketball factors", "career dates", "Google searches", "sport-specific factor fields", "rank comparison outputs"], "outputs": ["best-coach ranking model", "timeline correction", "gender correction", "cross-sport and country extensions", "stability and robustness discussion"], "decisions": ["which factors define comparison", "how ideal similarity is calculated", "how clusters restrict candidates", "how era and gender adjustments alter fields", "whether transfer and robustness claims are warranted"]},
        "section_map": [{"page": start, "section": key, "summary": summary} for key, _chapter, start, _end, _tag, summary in CHAPTERS],
        "assumptions": [{"page": page, "summary": summary} for page, summary in assumptions],
        "data_and_preprocessing": [{"page": page, "summary": summary} for page, summary in data],
        "models": [{"model_id": item["model_id"], "page": item["page"], "summary": item["summary"]} for item in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": page, "section": "verification", "summary": summary, "verification_type": kind, "strength": strength, "limitation": limitation} for page, summary, kind, strength, limitation in verification],
        "results_trace": [{"page": page, "summary": summary} for page, summary in results],
        "contributions": [{"page": 9, "summary": "Twelve explicit coach factors create a visible measurement interface."}, {"page": 12, "summary": "The component matrix exposes the basis for three named factor groupings."}, {"page": 16, "summary": "The direction-only cosine counterexample motivates a stated scale-aware adjustment."}, {"page": 20, "summary": "Timeline correction is expressed as regression, career aggregation, and a capped multiplier rather than an undocumented bonus."}, {"page": 24, "summary": "ANOVA is used as a declared selection gate before gender transformation."}, {"page": 29, "summary": "The factor pool makes shared and sport-specific fields visible before transfer."}, {"page": 37, "summary": "The paper at least displays a noisy-input comparison rather than asserting stability with no perturbation evidence."}],
        "writing_logic": [{"page": start, "summary": summary} for _key, _chapter, start, _end, _tag, summary in CHAPTERS],
        "language_observations": [{"page": start, "summary": summary} for _key, _chapter, start, _end, _tag, summary in CHAPTERS],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The summary presents a complete route from factor analysis through adjustment and transfer, without proving that the route itself caused award recognition.", "evidence_class": "J"}, {"page": 16, "summary": "The source openly demonstrates cosine's scale limitation before proposing an adjustment, which improves inspectability without validating the corrected rank.", "evidence_class": "J"}, {"page": 29, "summary": "The factor-pool diagram makes transfer assumptions visible before result tables, without proving cross-sport equivalence.", "evidence_class": "J"}],
        "weaknesses": [{"page": page, "summary": summary} for page, summary in warnings],
        "independent_extensions": extensions, "candidate_rule_impacts": [], "unresolved_questions": [summary for _page, summary in warnings], "protocol_v2_records": {}, "review_status": "validated",
    }


def build_observations(template, language, models, card):
    observations = template.make_observations(language, models, card)
    interpretations = {
        "language": "Reuse the rhetorical move only after replacing the coach population, factor definitions, transformations, comparison target, time span, and decision scope.",
        "modeling": "Retain the factor system, equations, clustering, timeline, ANOVA, whitening, transfer mappings, and handoffs together.",
        "logic": "Preserve the positive factor-to-PCA-to-similarity-to-adjustment-to-transfer-to-stability chain before recording source defects.",
        "visualization": "Keep each figure, table, formula, label, row/column meaning, axis, and analytical decision role together.",
        "verification": "Name the exact PCA, rank comparison, regression, ANOVA, variance, transfer, or noise object that was checked.",
        "data": "Retain coach roster, factor definition, unit, source, time span, transformation, missingness, and downstream consumer.",
        "assumption": "Pair each representativeness, data, proportionality, transformation, and transfer assumption with its enabled calculation and excluded regime.",
        "result": "Keep component labels, similarities, clusters, coefficients, p values, variances, ranks, and stability observations distinct.",
        "weakness": "Record notation, inference, transfer, robustness, and reproducibility defects only after the positive language, organization, model, and visual passes.",
        "other": "Separate cited background and web links from frozen inputs, executable transformations, and independent validation evidence.",
    }
    provenance = [(7, "introduction", "The problem background supplies decision context rather than frozen factor data."), (8, "assumptions", "The assumptions table declares calculation scope but does not validate it."), (9, "factor list", "The twelve-factor list is the measurement interface before PCA."), (10, "PCA equations", "The displayed standardization and correlation expressions are visually checked source evidence."), (11, "PCA table", "Eigenvalues and contribution rates are displayed but no source matrix is packaged."), (12, "component matrix", "Loadings support interpretive labels only within the selected sample."), (15, "ideal vector", "The factor maxima form the reference vector without a provenance ledger."), (18, "cluster table", "Cluster membership is visible but the cut rule is not reproducible."), (20, "timeline regression", "The figure shows a fit and label but no active-coach series or model diagnostics."), (24, "ANOVA formulas", "The test equations and alpha are displayed without a complete design record."), (26, "whitening formula", "The visual formula and variance table expose the intended transformation but not its implementation."), (29, "factor pool", "The pool diagram is an interface map, not evidence of receiving-domain validity."), (30, "sport tables", "Top-five tables show outputs without complete receiving rosters."), (37, "noise plot", "The plot supplies one limited perturbation display with color-overlap limitations."), (40, "references", "Web and method citations do not freeze data, code, or transformations."), (41, "appendix", "Original and modified rows support partial reconciliation but lack source and run provenance.")]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = ["Apply only when the coach roster, sport, gender coding, factor definitions, time window, data sources, transformations, comparison criterion, and decision scope are explicit."]
        row["counterevidence"] = ["A PCA loading, cosine rank, tight regression line, p value, variance match, transferred top five, or stable leading rank under one noise display does not establish fairness, causality, external validity, or reproducibility."]
        if row["dimension"] == "other":
            page, section, basis = provenance[other_index]
            other_index += 1
            row["page"] = page
            row["section"] = f"{section} / evidence action {other_index}"
            row["source_basis"] = basis
    if other_index != len(provenance):
        raise RuntimeError(f"expected {len(provenance)} provenance records, found {other_index}")
    return observations


def attach_rule_impacts(card, observations):
    first = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])

    def evidence(rule_id):
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])

    card["candidate_rule_impacts"] = [
        {"rule_id": "R-B-LANG-001", "action": "retain the decision-to-factor-to-PCA-to-similarity-to-adjustment-to-transfer-to-stability rhetorical route with an explicit scope boundary", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "trace factor rows through PCA, ideal-vector comparison, clustering, time and gender corrections, factor-pool mappings, ranking outputs, and perturbation checks", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "version coach records, factor definitions, era dates, Google-search observations, gender groups, receiving-sport fields, appendices, and all transformations", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for representativeness, data reliability, difficulty proportionality, whitening, and transfer comparability", "evidence_ids": [evidence("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain PCA, cosine, adjustment, clustering, regression, career aggregation, ANOVA, whitening, and transfer models with their handoffs", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "require explicit scale and mapping contracts whenever factor values, ideal vectors, timeline coefficients, gender transforms, or sport fields are combined", "evidence_ids": [evidence("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep loadings, ranks, p values, variances, correction coefficients, and visual outputs distinct rather than treating them as one validity score", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress PCA retention, distance/linkage choice, timeline regression, cap, social correction, ANOVA design, whitening ratio, factor mapping, and noise protocol", "evidence_ids": [evidence("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make every claim PCA-, rank-, regression-, ANOVA-, variance-, transfer-, or perturbation-trace-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile formula indices, difficulty coefficient direction, ANOVA notation, whitening ratio, table labels, noise protocol, and missing reproducibility files before reuse", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain execution flow, loading matrices, ideal-vector diagrams, equations, clusters, regression, variance displays, factor pool, ranking tables, noise plot, and appendix rows with purpose", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "measure preprocessing, PCA, similarity, clustering, regression, numerical integration, ANOVA, whitening, transfer reruns, and seeded robustness experiments as separate costs", "evidence_ids": [evidence("R-B-COMP-001")]},
    ]


def build_audit(template, language, models, card, observations):
    audit = template.make_audit(language, models, card, observations)
    layouts = {item["chapter"]: item for item in language["chapter_layouts"]}
    units = language["units"]
    chains = [
        ("abstract", ["best-coach decision -> multi-factor need", "PCA -> component interpretation", "ideal coach and cosine -> clustered baseline ranking", "timeline regression -> difficulty and social correction", "ANOVA -> whitening -> rerank", "factor pool -> sports and country extensions", "noise and comparison -> bounded stability claim"]),
        ("introduction", ["all-time coach question -> multi-factor data problem", "data and factor variety -> evaluation-system need", "comparison purpose -> explicit model route", "introduction -> assumptions and factor analysis handoff"]),
    ]
    audit["paragraph_chains"] = []
    for chapter, moves in chains:
        ids = [unit["language_unit_id"] for unit in units if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": index + 1, "dominant_move": move, "language_unit_ids": [ids[index % len(ids)]]} for index, move in enumerate(moves)]})
    audit["language_unit_dispositions"] = [{"language_unit_id": unit["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": unit["candidate_pattern_ids"], "reason": "The source move is reusable only after replacing coaches, factors, transformations, time scope, receiving domain, comparison criterion, and claim boundary."} for unit in units]
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete", "weakness_substitution_allowed": False,
        "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["Only after the positive language, organization, model, result, and visual chains are complete does the final pass record notation, inference, transfer, robustness, and reproducibility warnings."],
        "section_progressions": [{"chapter": chapter, "moves": [f"input: source-checked coach data, factor, table, formula, visual, or decision question entering {chapter}", f"rhetorical job: define, derive, compare, adjust, transfer, present, test, or bound the object in {chapter}", f"analytical job: standardize, correlate, decompose, compare vectors, cluster, regress, integrate, test, transform, rerun, or perturb", f"output: retain a typed factor, component, score, cluster, coefficient, p value, variance, rank, visual, or appendix artifact", "handoff: state the next model interface, correction, receiving-domain mapping, comparison, or evidence boundary"], "positive_pattern": "Use explicit input -> typed operation -> inspectable output -> scoped handoff; warnings remain a final pass."} for chapter in language["available_chapters"]],
        "main_argument_chains": [
            {"claim": "A multi-factor coach comparison becomes inspectable when the factor table passes through standardization, correlation, PCA, and visible loading interpretation.", "support_steps": ["twelve factors", "standardization", "correlation matrix", "eigenvalues", "contribution table", "component matrix", "component labels"], "decision_consequence": "Use the three labels only as sample-specific interpretations until factor definitions and retention choices are validated.", "source_pages": [9, 10, 11, 12]},
            {"claim": "An ideal-coach similarity ranking needs a scale-aware repair and an explicit cluster selection before its top list is interpreted.", "support_steps": ["ideal factor maxima", "cosine diagram", "direction-only counterexample", "adjusted values", "Euclidean distance", "single linkage", "cluster table", "ranking table"], "decision_consequence": "Do not treat the rank as a complete ability measurement without testing the reference, scaling, linkage, and group-selection rules.", "source_pages": [13, 14, 15, 16, 17, 18, 19]},
            {"claim": "A timeline correction is traceable when the active-coach series, regression, career integral, cap, social correction, and before-after ranks are all retained.", "support_steps": ["active-coach scatter", "linear fit", "difficulty coefficient", "career integral", "min-max coefficient", "cap", "search correction", "rank comparison"], "decision_consequence": "Treat the correction as conditional until its proportionality, units, calibration, data, and uncertainty are justified.", "source_pages": [20, 21, 22, 23]},
            {"claim": "A gender transformation is interpretable only when the test design, selected factors, whitening ratio, variance target, and reranking effect remain distinct.", "support_steps": ["ANOVA definitions", "p-value table", "win variance table", "whitening formula", "post-transform variance", "final ranking"], "decision_consequence": "Variance equalization cannot by itself establish fairness or eliminate all gender-linked measurement differences.", "source_pages": [24, 25, 26, 27, 28]},
            {"claim": "A factor pool supports transfer only after receiving-domain field mapping, data provenance, and evaluation are specified.", "support_steps": ["factor-pool diagram", "football mapping", "softball table", "baseball table", "country list", "additional-factor discussion"], "decision_consequence": "Treat the displayed lists as scoped demonstrations, not evidence that the ranking model is universal across sports or countries.", "source_pages": [29, 30, 31]},
            {"claim": "Adjustment and noise comparisons can support a limited stability observation when the changed fields, outputs, and untested dimensions are visible.", "support_steps": ["before-after adjusted list", "noisy John Wooden row", "noise plot", "noisy rank table", "stated strengths and weaknesses"], "decision_consequence": "Expand to seeded repeated sensitivity and structural checks before using robustness as a quality claim.", "source_pages": [36, 37, 38]},
        ],
    }
    model_rows = models["models"]
    audit["formula_error_watch"] = {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": [{"model_id": model_rows[1]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-003", "page": 10, "warning": "The visual correlation denominator has an index mismatch in its second sum; reconstruct indices before implementation."}, {"model_id": model_rows[1]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-006", "page": 11, "warning": "The printed cumulative-contribution upper index is inconsistent; verify the intended retained-component sum."}, {"model_id": model_rows[3]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-012", "page": 16, "warning": "The standard-deviation summand uses a different mean subscript from the stated mean."}, {"model_id": model_rows[3]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-017", "page": 17, "warning": "The general Minkowski expression omits absolute values and the merge relation mixes squared and unsquared distance notation."}, {"model_id": model_rows[5]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-020", "page": 21, "warning": "The printed difficulty equation divides by k after the preceding text defines D(t)=kA(t); reconcile direction and units."}, {"model_id": model_rows[7]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-027", "page": 24, "warning": "The ANOVA notation uses N inconsistently and needs correct group and total-observation degrees of freedom."}, {"model_id": model_rows[8]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-028", "page": 26, "warning": "Validate the whitening variance ratio and target rather than assuming a displayed variance match establishes a fair comparison."}]}
    counts = Counter(item["dimension"] for item in observations)
    audit["dimension_counts"] = {dimension: counts[dimension] for dimension in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}
    audit["positive_reusable_language_count"] = len(units)
    audit["weakness_record_count"] = counts["weakness"]
    return audit


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    if STAGE.exists() and any(STAGE.iterdir()):
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    q104 = load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q106")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q106")
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
    card["protocol_v2_records"] = {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(model["governing_equations"]) for model in models["models"]), "review_status": models["review_status"]}}
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
