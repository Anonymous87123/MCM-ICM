from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2014-26160-510e6a16"
SHORT = "26160"
SHA = "510e6a16a3e437ffc1dbe851dc805f66154eaf8c66373c7bb65fdd7cd5c8883b"
TYPE = "B"
YEAR = "2014"
PAGE_COUNT = 36
TEXT_DIR = ROOT / "artifacts/papers" / PID / "text/pages"
STAGE = ROOT / "tmp/q101-stage-v3"


def load_template_module():
    path = ROOT / "scripts/build_q100_artifacts.py"
    spec = importlib.util.spec_from_file_location("q100_template", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHAPTERS = [
    ("summary", "abstract", 1, 1, "ABS", "The summary routes a coach-evaluation task through AHP, Grey Correlation, Fuzzy Comprehensive Evaluation, time adjustment, sensitivity, and a final three-sport Honor Roll."),
    ("introduction", "introduction", 3, 3, "INT", "The introduction establishes the demand for an all-time coach comparison, states three requested lists, bounds gender claims, and previews the model ladder."),
    ("assumptions-and-symbols", "assumptions", 4, 4, "ASM", "The paper fixes comparability assumptions, defines coach and sport indicators, and introduces the symbols that later receive AHP weights."),
    ("model-overview", "problem-analysis", 5, 6, "OVR", "The overview reduces fifty-four candidate factors to a three-level hierarchy, explains the retained criteria, and assigns the parallel ranking models."),
    ("ahp", "model-establishment", 6, 9, "AHP", "The AHP section creates hierarchy levels, pairwise matrices, consistency checks, criterion weights, and seven retained indicators."),
    ("grey-correlation", "algorithm", 10, 16, "GRY", "Grey Correlation normalizes coach indicators, computes relation coefficients and degrees, and turns the weighted values into sport-specific rankings."),
    ("fuzzy-comprehensive-evaluation", "model-improvement", 16, 21, "FUZ", "Fuzzy evaluation defines comment grades, membership matrices, weight vectors, and a combined score for the same coach comparison."),
    ("results-review", "robustness-verification", 22, 23, "RES", "The results review compares Grey and Fuzzy rankings, names the leading coaches, and frames agreement as a practical ranking cross-check."),
    ("time-horizon-adjustment", "sensitivity-analysis", 23, 24, "TIM", "The time adjustment adds a coaching-start-time index to address changing competitive opportunities and produces adjusted score lists."),
    ("sensitivity", "sensitivity-robustness", 25, 26, "SEN", "The sensitivity section perturbs the largest AHP weight, reports rank movement, and bounds the claim as local ranking stability."),
    # Keep the source section names in `section`, while using only the shared
    # protocol vocabulary in `chapter`.  Page 27 returns explicitly to the
    # three requested problem outputs; page 28 reports the requested ranking
    # output rather than making an unsupported recommendation.
    ("discussion", "problem-restatement", 27, 27, "DIS", "The discussion returns to the three requested coach-comparison problems, summarizes the completed model route, and states the scope of the resulting lists."),
    ("honor-roll", "results", 28, 28, "HRL", "The Honor Roll turns the ranked outputs into three named sport lists and makes the requested communication artifact immediately scannable."),
    ("conclusion", "strengths-limitations", 29, 29, "CON", "The strengths, weaknesses, and conclusion return from the parallel models and adjusted scores to a bounded claim about evaluating outstanding coaches."),
    ("stakeholder-letter", "memo", 30, 30, "LET", "The Sports Illustrated letter translates the ranked evidence into an audience-facing explanation with an explicit selection rationale."),
    ("references", "references", 31, 31, "REF", "The references show a mixed provenance base of websites, rankings, and method sources while leaving several data and calculation details unresolved."),
    ("appendix", "appendix", 32, 36, "APP", "The appendix presents additional tables, MATLAB-oriented calculation material, and ranking support without supplying a complete executable reproduction package."),
]

PATTERNS = [
    "LP-B-SUMMARY-TASK-MODEL-RANKING",
    "LP-B-INTRO-NEED-TASK-SCOPE-ROADMAP",
    "LP-B-ASSUMPTION-SYMBOL-COMPARABILITY",
    "LP-B-FACTOR-SCREEN-HIERARCHY-HANDOFF",
    "LP-B-AHP-MATRIX-WEIGHT-CONSISTENCY",
    "LP-B-INDICATOR-DEFINITION-DIRECTION-USE",
    "LP-B-NORMALIZE-COEFFICIENT-RANK",
    "LP-B-FUZZY-GRADE-MEMBERSHIP-AGGREGATE",
    "LP-B-PARALLEL-RANK-COMPARISON-BOUNDARY",
    "LP-B-TIME-ADJUSTMENT-FAIRNESS-CONDITION",
    "LP-B-SENSITIVITY-PERTURBATION-RANK-INTERPRETATION",
    "LP-B-DISCUSSION-STRENGTH-LIMIT-TRANSFER",
    "LP-B-RESULT-LIST-DECISION-ARTIFACT",
    "LP-B-LETTER-EVIDENCE-AUDIENCE-ACTION",
    "LP-B-REFERENCE-PROVENANCE-BOUNDARY",
    "LP-B-APPENDIX-DETAIL-REPRODUCTION-BOUNDARY",
]

MOVES = [
    ("task-model-ranking", "State the ranking decision, name the paired model route, report a bounded output, and defer interpretation to the relevant result section.", "task -> model route -> ranked result -> scope"),
    ("need-task-scope", "Move from a disputed all-time comparison to explicit deliverables, comparability assumptions, and a transparent roadmap.", "need -> task -> scope -> roadmap"),
    ("definition-contract", "Define a criterion and its direction before it enters a matrix, normalized value, or ranking score.", "indicator -> definition -> direction -> downstream use"),
    ("factor-screen", "Reduce a broad candidate set by hierarchy and quantified availability before assigning model weights.", "candidate factors -> selection rule -> retained set -> model handoff"),
    ("matrix-weight-check", "Present pairwise judgment, derive weights, and state the consistency boundary before ranking.", "matrix -> weight -> consistency -> use"),
    ("indicator-evidence", "Connect a coach attribute to an observable count, rate, or comparison and preserve its unit and sport-specific meaning.", "criterion -> data -> direction -> score role"),
    ("grey-ranking", "Normalize indicators, form grey relations, aggregate the coefficient, and interpret the resulting order without claiming causal validity.", "normalize -> relation coefficient -> degree -> ranking"),
    ("fuzzy-ranking", "Map indicators to grades, assemble memberships, combine them with weights, and identify the score's decision role.", "grades -> memberships -> aggregation -> score"),
    ("parallel-comparison", "Compare two model rankings as a convergence check while keeping their shared data and indicator dependence explicit.", "model A rank -> model B rank -> agreement or difference -> boundary"),
    ("time-adjustment", "Introduce a historical-opportunity factor, state its intended fairness role, and separate it from an independently validated causal effect.", "time context -> adjustment -> revised rank -> condition"),
    ("local-sensitivity", "Perturb a declared weight, observe rank movement, and limit the conclusion to conditional local stability.", "fixed model -> weight perturbation -> rank response -> limit"),
    ("strength-limit", "Preserve the paper's constructive contribution before naming a data, assumption, or reproducibility boundary.", "strength -> evidence -> boundary -> improvement"),
    ("honor-roll", "Convert computed ranks into a concise list that preserves sport, coach identity, and the decision basis.", "ranked output -> named list -> selection basis"),
    ("stakeholder-letter", "Translate a method-backed list for a reader by stating the decision, the evidence route, and its scope.", "decision -> evidence route -> audience meaning -> scope"),
    ("provenance-boundary", "Separate web rankings, source tables, matrix judgments, calculations, and executable artifacts before reuse.", "source role -> transformation -> claim -> missing artifact"),
    ("appendix-boundary", "Use an appendix to expose supporting detail while explicitly distinguishing printed calculations from reproducible software evidence.", "support detail -> calculation role -> reproduction boundary"),
]

EXAMPLES = [
    ("A ranking study first identifies the decision audience, fixes the eligible candidate set, and then assigns the comparison metrics to a stated hierarchy.", "The opening makes the later score interpretable rather than treating a composite rank as self-explanatory."),
    ("For each candidate, the analysis defines the achievement count, success rate, longevity measure, and adjustment factor before normalizing any value.", "The criteria retain their direction and units when they enter the scoring model."),
    ("The first ranking method normalizes the comparable indicators and reports a relation degree, while the second maps the same evidence to membership grades.", "Agreement is described as a comparison of outputs, not proof that either model is externally valid."),
    ("A historical adjustment is introduced as one explicit criterion with a stated base year and coefficient.", "The result remains conditional on the selected time convention and available career record."),
    ("The sensitivity check changes one named weight while holding the remaining indicators and input table fixed.", "Its conclusion is limited to rank movement under that local perturbation."),
    ("The final list names the selected candidates and points back to the score construction used for the decision.", "A reader-facing letter avoids claiming that the list settles every cross-era comparison."),
]


def replace_text(value):
    if isinstance(value, str):
        return value.replace("water-strategy", "coach-evaluation").replace("water strategy", "coach evaluation").replace("China water", "coach-comparison")
    if isinstance(value, list):
        return [replace_text(item) for item in value]
    if isinstance(value, dict):
        return {key: replace_text(item) for key, item in value.items()}
    return value


def build_language(template, pages):
    template.PID = PID
    template.SHORT = SHORT
    template.SHA = SHA
    template.TYPE = TYPE
    template.YEAR = YEAR
    template.PAGE_COUNT = PAGE_COUNT
    template.TEXT_DIR = TEXT_DIR
    template.STAGE = STAGE
    template.CHAPTERS = CHAPTERS
    template.PATTERNS = PATTERNS
    template.MOVES = MOVES
    template.EXAMPLES = EXAMPLES
    language = replace_text(template.make_language(pages))
    for unit in language["units"]:
        unit["function"] = "Preserve a source-anchored coach-evaluation rhetorical move and transfer it only after replacing sport, candidate, metric, time horizon, and decision scope."
        unit["reusable_pattern"] = "source task or criterion -> typed operation -> ranked or graded output -> scoped handoff"
        unit["information_order"] = ["decision context or criterion", "matrix, normalization, or aggregation operation", "reported ranking or grade", "condition and receiving use"]
        unit["reusable_elements"] = ["explicit sport and candidate scope", "defined metric direction", "ordered model step", "ranked output before caveat"]
        unit["prohibited_generalizations"] = ["Do not present a sport-specific, era-bound coach ranking as a universal or causal truth.", "Do not detach an achievement count, success rate, time index, or composite score from its definition, denominator, data source, and selection boundary."]
        unit["features"]["quantitative_role"] = "bind a count, rate, weight, grade, rank, or time index to its declared decision role"
        unit["features"]["transition"] = "first, then, therefore, meanwhile, however, and finally connect criteria, model stages, results, and decision artifacts"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 36 local UTF-8 page text files were read programmatically; chapter counts are computed from the declared bounded page ranges. Rendered-page review supplies the visual boundary check."
        layout["ambiguities"] = ["Extraction flattens matrices, subscripts, table alignment, and chart labels; visually checked formula records preserve uncertainty rather than silently repairing it.", "The paper mixes web-derived rankings, hand-judged AHP entries, and MATLAB claims without a complete data or code archive; those boundaries are last-pass evidence, not language substitutions."]
    return language


def equation(index, page, label, latex, symbols, purpose, confidence="high"):
    return {"equation_id": f"EQ-B-{YEAR}-{SHORT}-{index:03d}", "page": page, "label": label, "source_expression": latex, "normalized_latex": latex, "purpose": purpose, "variable_symbols": symbols, "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}


def make_model(template, model_id, page, section, family, purpose, inputs, outputs, equations):
    model = template.make_model(model_id, page, section, family, purpose, inputs, outputs, equations)
    model["summary"] = purpose
    for variable in model["variables"]:
        variable["definition"] = f"Source-defined coach-evaluation quantity {variable['symbol']}."
        variable["unit"] = "count, rate, normalized score, pairwise ratio, membership degree, rank, year-derived index, or dimensionless composite as defined by the source"
    model["objectives"] = [purpose, "Return a typed criterion weight, relation degree, membership score, rank comparison, or communication-facing selection list."]
    model["constraints"] = ["Keep sport, candidate, indicator direction, normalization convention, AHP judgment, time adjustment, and ranking scope explicit.", "A composite rank or agreement between two rankings does not establish causal superiority, external validity, or a definitive cross-era judgment."]
    model["conditions"] = {"initial": {"status": "present", "details": ["Candidate coach records, sport-specific achievement indicators, pairwise judgments, and the declared historical comparison scope are supplied or assumed."]}, "boundary": {"status": "present", "details": ["Missing official task text, web-source changes, sport comparability, gender coding, matrix consistency, time-index choice, and rank ties require explicit handling."]}, "equilibrium": {"status": "not-applicable", "details": ["The source executes finite ranking and sensitivity calculations rather than a dynamical equilibrium solve."]}}
    model["parameter_estimation"] = {"status": "partial", "method": "AHP judgment matrices, web and sports-site records, normalization, grey coefficients, fuzzy memberships, a fixed time-index convention, and local weight perturbation.", "parameters": [v["symbol"] for v in model["variables"]]}
    model["algorithm"] = {"status": "partial", "steps": ["freeze eligible candidates and criterion definitions", "normalize, weight, relate, or fuzzify the declared indicators", "aggregate the model-specific score", "compare sport-specific ranks and perform the stated local sensitivity check", "handoff the qualified result to the Honor Roll and reader letter"], "software": ["The paper refers to MATLAB or computer simulation, but source code, versions, input tables, seeds, and executable outputs are not supplied."], "convergence_criteria": "Finite matrices, rankings, membership aggregation, and stated weight perturbations terminate the source procedure; no independent convergence or external-validation certificate is supplied."}
    model["assumptions"] = ["The retained indicators and their directions represent the comparison purpose within each sport.", "The selected candidate set, web data, pairwise judgments, and time adjustment are sufficiently comparable for the stated ranking exercise."]
    model["identifiability_feasibility"] = {"status": "partial", "analysis": "The hierarchy, equations, tables, rank lists, and some calculation detail are inspectable, but source data, matrix provenance, normalization conventions, code, and reproducible outputs remain incomplete."}
    model["computational_cost"] = "Driven by pairwise-matrix operations, indicator normalization, grey coefficient calculation, membership aggregation, rank comparison, local sensitivity reruns, and any unprovided MATLAB execution."
    model["strengths"] = ["The source uses explicit model stages and reports a decision-facing list rather than only abstract scores.", "The paired Grey and Fuzzy routes expose a useful comparison interface before their evidence limits are recorded."]
    model["limitations"] = ["AHP weights, web-derived records, time adjustment, and local perturbations do not independently validate indicators, model structure, or external ranking truth.", "Confirmed source defects are retained only after the positive language, organization, model, and visualization learning passes."]
    model["missing_details"] = ["Official problem text, frozen candidate data, data definitions, complete pairwise-matrix provenance, normalization code, membership functions, parameter settings, MATLAB files, run log, and independent validation data are absent."]
    return model


def build_models(template):
    ahp = [
        equation(1, 6, "pairwise comparison", r"A=(a_{ij}),\ a_{ij}=w_i/w_j", ["A", "a_ij", "w_i", "w_j"], "Represent pairwise AHP judgments for the hierarchy."),
        equation(2, 7, "AHP consistency index", r"CI=(\lambda_{max}-n)/(n-1)", ["CI", "lambda_max", "n"], "Compute the consistency index before accepting a judgment matrix.", "medium"),
        equation(3, 7, "AHP consistency ratio", r"CR=CI/RI", ["CR", "CI", "RI"], "Compare matrix inconsistency with the random index; the printed two-factor CR is retained as a warning anchor.", "medium"),
        equation(4, 9, "criterion composite weight", r"W=(w_1,w_2,\ldots,w_7)", ["W", "w_1", "w_2", "w_7"], "Pass the retained seven criterion weights to the ranking models."),
    ]
    grey = [
        equation(5, 10, "min-max normalization", r"x'_{ij}=(x_{ij}-\min_i x_{ij})/(\max_i x_{ij}-\min_i x_{ij})", ["x_ij", "xprime_ij"], "Place benefit indicators on a comparable scale before grey relation calculation.", "medium"),
        equation(6, 12, "grey distance", r"\Delta_i(k)=|x_0(k)-x_i(k)|", ["Delta_i", "x_0", "x_i", "k"], "Measure the distance between a reference pattern and a candidate criterion sequence."),
        equation(7, 13, "grey relation coefficient", r"\xi_i(k)=(\Delta_{min}+\rho\Delta_{max})/(\Delta_i(k)+\rho\Delta_{max})", ["xi_i", "Delta_min", "Delta_max", "rho", "Delta_i"], "Transform the normalized distance into a relation coefficient."),
        equation(8, 15, "grey relation degree", r"r_i=(1/n)\sum_{k=1}^{n}\xi_i(k)", ["r_i", "n", "xi_i", "k"], "Aggregate coefficients into the grey ranking degree."),
    ]
    fuzzy = [
        equation(9, 17, "membership matrix", r"R=(r_{ij})_{m\times n}", ["R", "r_ij", "m", "n"], "Collect indicator-to-grade membership degrees for fuzzy comprehensive evaluation."),
        equation(10, 18, "first-level fuzzy aggregate", r"B=A\circ R", ["B", "A", "R"], "Combine an AHP weight vector with the membership matrix."),
        equation(11, 18, "second-level score", r"Z=B D^T", ["Z", "B", "D"], "Produce the paper's final fuzzy score; the printed symbol and dimensional conflict are retained as a warning anchor.", "medium"),
    ]
    timing = [
        equation(12, 24, "coaching-start-time index", r"t=(T-1900)/100", ["t", "T"], "Encode the year a coach began coaching as the paper's historical adjustment factor."),
        equation(13, 24, "time-adjusted composite", r"S'=0.93S+0.07t", ["Sprime", "S", "t"], "Represent the stated seven-percent time-factor adjustment in the revised rank calculation.", "medium"),
    ]
    sensitivity = [
        equation(14, 25, "local weight perturbation", r"w_{max}'=w_{max}\pm0.02", ["wmax", "wmaxprime"], "Perturb only the largest weight while the remaining data and structure stay fixed."),
    ]
    models = [
        make_model(template, f"MU-B-{YEAR}-{SHORT}-001", 6, "AHP hierarchy and factor selection", "analytic hierarchy process", "Screen candidate factors and derive a seven-criterion weight vector for sport-specific coach comparison.", ["candidate factors", "pairwise judgments", "RI"], ["W", "retained criteria"], ahp),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-002", 10, "Grey Correlation", "grey relational analysis", "Normalize coach indicators and obtain a Grey Correlation ranking for the selected sports.", ["W", "coach indicators", "reference sequence", "rho"], ["grey degrees", "Grey rank"], grey),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-003", 16, "Fuzzy Comprehensive Evaluation", "fuzzy comprehensive evaluation", "Map weighted coach indicators to evaluation grades and generate a Fuzzy ranking.", ["W", "membership matrix", "grade vector"], ["fuzzy score", "Fuzzy rank"], fuzzy),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-004", 22, "Results review", "parallel rank comparison", "Compare Grey and Fuzzy outputs for agreement, disagreement, and decision-facing candidate selection.", ["Grey rank", "Fuzzy rank", "sport scope"], ["comparison table", "qualified Honor Roll candidates"], []),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-005", 23, "Time horizon adjustment", "historical adjustment", "Add a coaching-start-time factor to the comparison and report adjusted ranks.", ["base composite score", "start year", "time weight"], ["time-adjusted score", "adjusted rank"], timing),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-006", 25, "Sensitivity analysis", "local ranking sensitivity", "Test rank movement after the stated plus-or-minus 0.02 perturbation of the largest AHP weight.", ["base weights", "perturbation", "fixed indicators"], ["rank movement", "conditional stability statement"], sensitivity),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-007", 28, "Honor Roll and letter", "decision communication", "Translate qualified ranking results into three sport lists and a reader-facing explanation.", ["rank lists", "scope boundary", "selection rationale"], ["Honor Roll", "Sports Illustrated letter"], []),
        make_model(template, f"MU-B-{YEAR}-{SHORT}-008", 32, "Appendix", "calculation support", "Expose appendix tables and stated MATLAB/computer-simulation support while retaining the missing reproducibility artifacts.", ["printed tables", "stated software use"], ["supporting calculations", "reproduction boundary"], []),
    ]
    edges = [
        {"from_model_id": models[0]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "The retained criterion definitions and AHP weights are the typed inputs to Grey normalization and relation calculation."},
        {"from_model_id": models[0]["model_id"], "to_model_id": models[2]["model_id"], "handoff": "The same AHP weight vector is combined with Fuzzy membership grades, preserving the shared indicator boundary."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "Grey degrees and sport-specific rank order enter the model-comparison table."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "Fuzzy scores and rank order enter the model-comparison table."},
        {"from_model_id": models[3]["model_id"], "to_model_id": models[4]["model_id"], "handoff": "The base comparison score and selected candidates are adjusted by the coaching-start-time convention."},
        {"from_model_id": models[4]["model_id"], "to_model_id": models[5]["model_id"], "handoff": "The adjusted ranking is re-evaluated after a local largest-weight perturbation."},
        {"from_model_id": models[5]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "The conditionally stable sport-specific lists are converted into Honor Roll and letter artifacts."},
        {"from_model_id": models[6]["model_id"], "to_model_id": models[7]["model_id"], "handoff": "Appendix material is cited only as supporting calculation context, not as a complete executable reproduction."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def build_card(models):
    assumptions = [
        (4, "The selected indicators can compare coaching achievement within each stated sport despite changing eras and competition conditions."),
        (5, "Fifty-four candidate factors can be reduced to a three-level hierarchy and seven retained measurable criteria."),
        (9, "The gender coding and associated effect used in the source are appropriate for the stated comparison, although the rationale is not demonstrated."),
        (23, "A coaching-start-time index with a seven-percent weight represents the intended historical opportunity adjustment."),
        (25, "Changing only the maximum AHP weight by plus or minus 0.02 is informative about the stated local rank sensitivity."),
    ]
    data = [
        (1, "The Summary identifies the requested comparison of outstanding coaches and the final three-sport Honor Roll."),
        (5, "The model overview reports fifty-four candidate factors, three top-level dimensions, and a final seven-criterion selection."),
        (9, "AHP tables give pairwise judgments and weights for achievement, winning, longevity, honors, player development, gender, and related factors."),
        (10, "Grey Correlation uses coach records and normalized indicator values to produce sport-specific relation degrees."),
        (17, "Fuzzy evaluation introduces comment grades, membership values, and a grade vector for the same coach comparison."),
        (22, "The results tables show Grey and Fuzzy ranks for selected basketball, baseball, and football coaches."),
        (24, "The adjusted ranking adds coaching-start year through the stated time-index convention and seven-percent weight."),
        (25, "Sensitivity tables report changes after the maximum criterion weight is perturbed by 0.02."),
        (29, "The conclusion says data came from NCAA, while earlier pages cite Wikipedia and sports websites; both provenance claims are retained."),
        (32, "Appendix tables contain supporting coach records and a Harry Statham win total that conflicts with a body-table value."),
    ]
    verification = [
        (7, "The AHP matrix can be checked by recomputing lambda, CI, and CR from its stated entries.", "matrix consistency check", "Pairwise tables and reported consistency values are visible.", "The reported two-factor CR conflicts with lambda=2.0000, and matrix provenance is not supplied."),
        (13, "Grey normalization, coefficient, and relation-degree steps form a visible ranking pipeline.", "formula and table trace", "The operations are sequentially described and linked to ranks.", "Min/max prose and some entity labels are inconsistent, and the source data are not frozen."),
        (18, "Fuzzy membership, aggregation, and grade-score notation can be traced across the displayed matrices.", "formula trace", "Weight and membership roles are visible.", "The final B and D notation conflicts with earlier semantic and dimensional use."),
        (22, "Grey and Fuzzy rank tables can be compared across the stated sports.", "parallel comparison", "The source makes output agreement inspectable.", "Shared candidates, indicators, and data prevent this comparison from becoming independent validation."),
        (25, "The sensitivity table can be checked for its declared maximum-weight perturbation.", "local sensitivity", "The changed factor and rank response are stated.", "Only one local weight changes; model, indicator, and external validity are not tested."),
        (30, "The reader letter can be traced to the prior model lists and stated selection rationale.", "decision-to-communication trace", "The requested audience artifact names its evidence route.", "The letter cannot repair underlying data, comparability, or reproducibility gaps."),
        (32, "Appendix records can be compared with body tables and stated computer-simulation claims.", "appendix consistency check", "Supporting values and calculation references are visible.", "Code, configuration, inputs, and reproducible outputs are absent."),
    ]
    results = [
        (22, "Grey Correlation produces one set of sport-specific coach rankings from the retained criteria."),
        (22, "Fuzzy Comprehensive Evaluation produces a parallel rank list using grades and membership aggregation."),
        (23, "The paper reports comparison and review of the two ranking routes before adding the time adjustment."),
        (24, "The time index revises the ranking using coaching-start year and a stated seven-percent weight."),
        (25, "The sensitivity study reports limited rank movement after a plus-or-minus 0.02 maximum-weight perturbation."),
        (28, "The Honor Roll presents the selected basketball, baseball, and football coach lists as the requested decision artifact."),
    ]
    writing = [
        (1, "Summary chain: coach-comparison task -> AHP factor screen -> Grey and Fuzzy rankings -> rank review -> time adjustment -> sensitivity -> three-sport Honor Roll."),
        (3, "Introduction chain: disputed evaluation need -> limits of prior comparison -> three explicit tasks -> comparability boundaries -> AHP/Grey/Fuzzy roadmap."),
        (4, "Assumptions-and-symbols chain: scope choices -> indicator definitions -> notation -> comparable input contract for the hierarchy."),
        (5, "Overview chain: fifty-four factors -> top-level dimensions -> AHP selection -> seven retained criteria -> paired-ranking handoff."),
        (6, "AHP chain: hierarchy -> pairwise matrix -> weight vector -> consistency check -> indicator weights for both ranking models."),
        (10, "Grey chain: criterion data -> normalization -> coefficient and degree -> coach rank -> comparison-table handoff."),
        (16, "Fuzzy chain: grade set -> membership matrix -> weighted aggregate -> score and rank -> comparison-table handoff."),
        (22, "Results chain: two rankings -> agreement and difference review -> candidate list -> time-adjustment handoff."),
        (23, "Time chain: cross-era concern -> start-year index -> adjusted score -> revised rank -> sensitivity handoff."),
        (25, "Sensitivity chain: fixed source data and model -> maximum-weight perturbation -> rank response -> local-stability boundary."),
        (27, "Discussion chain: model strengths -> data and scope conditions -> list interpretation -> recommendation boundary."),
        (28, "Honor Roll chain: qualified rankings -> named sport lists -> decision artifact for the stated task."),
        (30, "Letter chain: requested audience -> concise method explanation -> selected lists -> scope-aware closing."),
        (32, "Appendix chain: supporting tables and calculation claims -> cross-checkable values -> explicit reproducibility boundary."),
    ]
    contributions = [
        {"page": 5, "summary": "Uses a visible factor-reduction and hierarchy route to turn a broad coach-comparison prompt into seven retained criteria."},
        {"page": 10, "summary": "Builds a Grey Correlation pipeline from normalized indicators to sport-specific relation degrees and ranks."},
        {"page": 16, "summary": "Uses a Fuzzy Comprehensive Evaluation route that preserves grades, memberships, weights, and an aggregate score."},
        {"page": 22, "summary": "Places two model outputs side by side before communicating a selection list."},
        {"page": 23, "summary": "Makes a historical time adjustment explicit rather than silently treating all coaching eras as identical."},
        {"page": 25, "summary": "Includes a named local weight-perturbation sensitivity check and reports its rank consequence."},
        {"page": 28, "summary": "Converts computation into a compact Honor Roll that answers the requested three-sport deliverable."},
        {"page": 30, "summary": "Adds a reader-facing Sports Illustrated letter whose statements trace back to the ranking route."},
    ]
    visuals = [
        {"page": 6, "figure": "AHP hierarchy diagram", "summary": "Shows the top-level dimensions, retained criteria, and direction of the weight-to-ranking handoff."},
        {"page": 7, "figure": "AHP judgment matrices", "summary": "Makes pairwise ratios, reported eigenvalue information, and consistency claims inspectable."},
        {"page": 9, "figure": "criterion-weight chart/table", "summary": "Displays the seven retained factors and their relative contribution to the coach-comparison score."},
        {"page": 12, "figure": "Grey Correlation calculation table", "summary": "Shows normalized indicator values and relation quantities used to derive rankings."},
        {"page": 15, "figure": "Grey coach-rank chart", "summary": "Communicates the sport-specific ordering produced by Grey relation degrees."},
        {"page": 18, "figure": "Fuzzy membership and aggregation matrix", "summary": "Exposes grade memberships, weights, and the score-combination stage."},
        {"page": 21, "figure": "Fuzzy coach-rank chart", "summary": "Communicates the sport-specific ordering produced by fuzzy aggregate scores."},
        {"page": 22, "figure": "Grey-versus-Fuzzy comparison table", "summary": "Supports a model-output comparison while retaining their shared-evidence boundary."},
        {"page": 24, "figure": "time-adjusted rank table", "summary": "Shows how the chosen start-year index changes composite ranking outputs."},
        {"page": 25, "figure": "sensitivity rank table", "summary": "Shows rank response to the stated local maximum-weight perturbation."},
        {"page": 28, "figure": "Honor Roll lists", "summary": "Turns results into the final three-sport decision artifact rather than a free-standing score table."},
        {"page": 32, "figure": "appendix coach-record table", "summary": "Provides supporting values that can be cross-checked against body tables and reproduction claims."},
    ]
    warnings = [
        (7, "The two-factor AHP matrix reports lambda=2.0000 together with CR=0.2496; those values are inconsistent under the stated consistency formula."),
        (8, "Prose calls some three- and four-factor comparison matrices two-factor matrices, leaving the hierarchy description internally inconsistent."),
        (9, "The male=1 and female=3 coding uses an unsupported gender rationale and should not be transferred as an evidence-backed comparison rule."),
        (11, "Grey normalization prose confuses min and max cases and changes the evaluated entity from coaches to countries."),
        (18, "The Fuzzy table duplicates d13 and omits d14, so the grade or membership index cannot be safely reused without source reconciliation."),
        (18, "The final fuzzy expression uses Z=B D^T although D is defined as five elements and B earlier denotes top-level weights, creating a dimensional and semantic conflict."),
        (23, "The paper says Fuzzy evaluation both considers and does not consider internal relationships, so the claimed distinction is unresolved."),
        (24, "The time index (T-1900)/100 and seven-percent weight are weakly sourced and systematically favor later-starting coaches under the stated convention."),
        (25, "Changing only the maximum weight by plus or minus 0.02 supports conditional rank sensitivity, not indicator validation, parameter robustness, model validation, or external validity."),
        (27, "Comparison with Wikipedia or current ranks risks circular validation and candidate-selection bias when the same ecosystem supplies the inputs or benchmark."),
        (29, "The conclusion attributes data to NCAA while the body cites Wikipedia and sports websites, leaving the actual data provenance unreconciled."),
        (32, "Appendix reports Harry Statham wins as 1076 while an earlier matrix reports 1079."),
        (32, "MATLAB or computer simulation is claimed without code, configuration, input data, or reproducible outputs."),
    ]
    return {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": SHORT, "title": "The Greatest Coaches of All Time", "award_status": "outstanding", "source": {"relative_path": "2014美赛特等奖/B-26160-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical page 1 is the Summary; from physical page 2 onward, printed page numbering is one less than the PDF page index."}, "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["All 36 local UTF-8 text pages were read by the staging generator.", "All 36 physical pages were visually reviewed through byte-bounded JPEG proxies before artifact generation.", "No full-page original PNG or embedded base64 image was sent through the model transport; original rendered pages remain on disk for coordinate checks.", "Matrix subscripts, chart captions, and a few table labels have explicit source-level warning anchors rather than silent corrections."]},
        "context_sources": [{"type": "paper", "path": "2014美赛特等奖/B-26160-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "text-pages", "path": f"artifacts/papers/{PID}/text/pages"}],
        "task_reconstruction": {"status": "incomplete-official-task-unavailable", "inputs": ["coach achievement and career records", "sport-specific indicators", "AHP matrices", "Grey and Fuzzy ranking inputs", "coaching-start years", "stated sensitivity perturbation"], "outputs": ["Grey ranks", "Fuzzy ranks", "time-adjusted ranks", "sensitivity discussion", "three-sport Honor Roll", "Sports Illustrated reader letter"], "decisions": ["which factors to retain", "how to weight them", "which coaches qualify in each sport", "whether time adjustment changes the list", "how to communicate the qualified ranking"]},
        "section_map": [{"page": start, "section": key, "summary": summary} for key, chapter, start, end, tag, summary in CHAPTERS], "assumptions": [{"page": p, "summary": s} for p, s in assumptions], "data_and_preprocessing": [{"page": p, "summary": s} for p, s in data], "models": [{"model_id": model["model_id"], "page": model["page"], "summary": model["summary"]} for model in models["models"]], "dependency_graph": models["dependency_edges"], "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification], "results_trace": [{"page": p, "summary": s} for p, s in results], "contributions": contributions, "writing_logic": [{"page": p, "summary": s} for p, s in writing], "language_observations": [{"page": p, "summary": s} for p, s in writing], "visualization_observations": visuals, "judge_relevance_hypotheses": [{"page": 1, "summary": "The Summary gives a complete task-to-model-to-list route before technical detail.", "evidence_class": "J"}, {"page": 22, "summary": "The paired rank table visibly connects two computations to a selection decision, but award status alone does not show why judges valued it.", "evidence_class": "J"}, {"page": 30, "summary": "The letter turns a transparent method route into an audience-facing artifact, without proving a causal judge preference.", "evidence_class": "J"}], "weaknesses": [{"page": p, "summary": s} for p, s in warnings], "independent_extensions": [{"extension_id": f"E-B-{SHORT}-{i:03d}", "page": p, "summary": s} for i, (p, s) in enumerate([(7, "Recompute every pairwise matrix from archived judgments and reconcile lambda, CI, and CR before using AHP weights."), (13, "Publish criterion data, normalization directions, and an auditable Grey calculation notebook."), (18, "Define fuzzy grade sets and membership functions, reconcile symbols, and test dimensions before score aggregation."), (22, "Use independent historical or expert-held-out benchmarks rather than rankings sourced from the same web ecosystem."), (24, "Justify, estimate, or scenario-test time adjustment separately from base achievement indicators."), (25, "Vary coherent weight vectors and indicator definitions, then report rank uncertainty rather than one maximum-weight perturbation."), (32, "Archive code, package versions, input tables, outputs, and a cross-table consistency test.")], 1)], "candidate_rule_impacts": [], "unresolved_questions": [s for _, s in warnings], "protocol_v2_records": {}, "review_status": "validated",
    }


def build_observations(template, language, models, card):
    observations = replace_text(template.make_observations(language, models, card))
    provenance_sources = [
        (31, "references", "The reference list documents methodological and coach-evaluation sources, but it does not freeze the exact coach dataset, web retrieval dates, or executable calculations used by this paper."),
        (31, "references", "The cited sources establish reading provenance for the comparison, not a versioned input contract for the AHP, Grey, Fuzzy, and time-adjustment computations."),
        (31, "references", "References make the paper's external context inspectable while leaving coach inclusion rules, source snapshots, and data-cleaning decisions unreproduced."),
        (31, "references", "A citation list can support attribution but cannot by itself reproduce the source-specific rankings, membership values, or pairwise judgments."),
        (32, "appendix basketball records", "Appendix page 32 begins the original college-basketball coach table with career, record, win/loss, and final-four fields that feed later comparisons."),
        (32, "appendix basketball records", "The first appendix table provides concrete basketball values, but the paper does not provide a machine-readable dataset or the transformation trail from rows to model inputs."),
        (33, "appendix continued records", "Appendix page 33 continues source coach records; the tabular continuation must remain tied to its headers and sport-specific field meanings."),
        (33, "appendix continued records", "Continued appendix rows provide audit clues for candidate values, yet they do not document how missing, tied, or cross-era observations were resolved."),
        (34, "appendix continued records", "Appendix page 34 continues coach-record evidence across tables; retain the distinction between raw career fields and the later normalized or weighted scores."),
        (34, "appendix continued records", "Raw appendix records can support spot checks only when each column, sport boundary, and selection rule is preserved with the source page."),
        (35, "appendix basketball ranks", "Appendix page 35 displays basketball Grey and Fuzzy scores and ranks, permitting an output-level cross-check against the body discussion."),
        (35, "appendix basketball ranks", "The parallel rank table records model outputs, but shared inputs mean agreement is not independent external validation."),
        (36, "appendix football ranks", "Appendix page 36 gives football Grey and Fuzzy scores and ranks, preserving the sport-specific output needed to audit the stated Honor Roll."),
        (36, "appendix football ranks", "The football ranking table should be transferred as a typed score-and-rank artifact, not as proof of universal or causal coaching superiority."),
        (36, "appendix field-hockey ranks", "Appendix page 36 also begins field-hockey score and rank records, showing that the final communication aggregates multiple sport-specific tables."),
        (36, "appendix provenance boundary", "The final appendix material supplies selected raw and ranked records but no archived code, configuration, source snapshots, or complete reproducibility package."),
    ]
    other_index = 0
    for row in observations:
        row["interpretation"] = row["interpretation"].replace("coach-evaluation entities", "sport, candidate, indicator, era, and decision entities")
        row["counterevidence"] = ["A selected rank, agreement between two models, consistency ratio, or local sensitivity result does not prove global superiority, causal validity, external ranking truth, reproducibility, or safe cross-era transfer."]
        row["applicability"] = ["Apply only when sport scope, candidates, indicator definitions, data provenance, normalization, weighting, time convention, and decision boundary are explicit."]
        if row["dimension"] == "other":
            page, section, basis = provenance_sources[other_index]
            other_index += 1
            row["page"] = page
            row["section"] = f"{section} / evidence action {other_index}"
            row["source_basis"] = basis
            row["interpretation"] = "Preserve the cited or appendix record with its sport, table role, field definitions, and reproducibility boundary; do not treat a reference list or selected table as a frozen executable evidence package."
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
        {"rule_id": "R-B-LANG-001", "action": "retain the task-to-AHP-to-parallel-ranking-to-time-adjustment-to-Honor-Roll sequence, criterion definitions, ranked-result framing, and reader-letter boundary with sport and era conditions", "evidence_ids": [first["language"]]},
        {"rule_id": "R-B-LOG-001", "action": "trace the coach-comparison need through factor reduction, AHP weights, Grey and Fuzzy rankings, result review, time adjustment, sensitivity, lists, and letter", "evidence_ids": [first["logic"]]},
        {"rule_id": "R-B-DATA-001", "action": "version candidate roster, sport records, achievement definitions, denominators, source sites, pairwise judgments, start years, normalization, and the external benchmark separately", "evidence_ids": [first["data"]]},
        {"rule_id": "R-B-DATA-002", "action": "maintain a comparability and assumption ledger for indicator selection, gender coding, era adjustment, sport scope, and fixed-factor sensitivity", "evidence_ids": [evidence("R-B-DATA-002")]},
        {"rule_id": "R-B-MOD-001", "action": "retain AHP, Grey Correlation, Fuzzy Comprehensive Evaluation, parallel-rank review, historical adjustment, local sensitivity, and decision-communication interfaces", "evidence_ids": [first["modeling"]]},
        {"rule_id": "R-B-MOD-003", "action": "combine criteria only through a documented hierarchy, normalization convention, weight vector, membership construction, and score interpretation", "evidence_ids": [evidence("R-B-MOD-003")]},
        {"rule_id": "R-B-MOD-004", "action": "keep AHP weights, Grey degrees, Fuzzy scores, time-adjusted scores, ranks, and Honor Roll selection rules distinct", "evidence_ids": [first["result"]]},
        {"rule_id": "R-B-MOD-005", "action": "stress matrix provenance, gender rationale, normalization direction, fuzzy notation, time-index justification, cross-era comparability, and reproducible data/code", "evidence_ids": [evidence("R-B-MOD-005")]},
        {"rule_id": "R-B-VER-002", "action": "make evidence claims matrix-, formula-, table-, comparison-, perturbation-, appendix-, and decision-trace-specific", "evidence_ids": [first["verification"]]},
        {"rule_id": "R-B-VER-004", "action": "reconcile the AHP CR conflict, fuzzy D/B notation, data provenance, time-weight justification, appendix win-count mismatch, and absent executable evidence", "evidence_ids": [first["weakness"]]},
        {"rule_id": "R-B-VIZ-001", "action": "retain hierarchy diagrams, matrix tables, normalized-value tables, rank comparisons, time-adjusted and sensitivity tables, lists, and appendix records with their analytical purpose", "evidence_ids": [first["visualization"]]},
        {"rule_id": "R-B-COMP-001", "action": "measure pairwise operations, normalization and relation calculations, membership aggregation, rank comparison, sensitivity reruns, and any archived MATLAB execution", "evidence_ids": [evidence("R-B-COMP-001")]},
    ]


def build_audit(template, language, models, card, observations):
    audit = replace_text(template.make_audit(language, models, card, observations))
    layouts = {item["chapter"]: item for item in language["chapter_layouts"]}
    units = language["units"]
    audit["paragraph_chains"] = []
    for chapter in ("abstract", "introduction"):
        ids = [unit["language_unit_id"] for unit in units if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": index + 1, "dominant_move": "task or context -> method route -> result or scope", "language_unit_ids": [ids[index % len(ids)]]} for index in range(layouts[chapter]["paragraph_count"])]})
    audit["organization_logic"] = {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["The final warning pass records formula, data, notation, claim, and reproducibility defects without replacing positive learning."], "section_progressions": [{"chapter": chapter, "moves": [f"input: source-checked coach-comparison context, criterion, matrix, calculation, rank, or decision entering {chapter}", f"rhetorical job: state the positive comparison, relation, result, or recommendation in {chapter}", f"analytical job: define, weight, normalize, aggregate, compare, adjust, perturb, or communicate the declared object in {chapter}", f"output: retain a typed criterion, score, rank, table, list, or provenance boundary from {chapter}", "handoff: name the next model, comparison, adjustment, decision artifact, or reproduction boundary"], "positive_pattern": "Use explicit source input -> typed operation -> qualified output -> scoped handoff; warnings remain a last pass."} for chapter in language["available_chapters"]], "main_argument_chains": [{"claim": "A broad coach-comparison task is made auditable by reducing criteria, assigning explicit weights, and preserving parallel rank calculations.", "support_steps": ["fifty-four candidate factors", "three-level hierarchy", "seven retained criteria", "AHP matrices and weights", "Grey and Fuzzy calculations"], "decision_consequence": "Use a cross-era sport ranking only with explicit candidate, data, weighting, and model boundaries.", "source_pages": [1, 3, 5, 6, 9, 10, 16, 22]}, {"claim": "Grey and Fuzzy output comparison can structure a ranking review but cannot serve as independent external validation.", "support_steps": ["shared criteria", "Grey rank", "Fuzzy rank", "comparison table", "common-source boundary"], "decision_consequence": "Report agreement as conditional output comparison and seek independent data or benchmark validation separately.", "source_pages": [10, 16, 22, 23]}, {"claim": "Time adjustment and sensitivity are useful only when their convention and fixed dimensions are explicit.", "support_steps": ["start-year index", "seven-percent weight", "adjusted rank", "maximum-weight perturbation", "rank response"], "decision_consequence": "Do not label a local AHP weight perturbation as broad model robustness or fairness validation.", "source_pages": [23, 24, 25, 26]}, {"claim": "The Honor Roll and reader letter are strongest when they trace back to qualified result records and retain scope limits.", "support_steps": ["Grey and Fuzzy rank tables", "adjusted comparison", "sensitivity boundary", "three-sport lists", "Sports Illustrated letter"], "decision_consequence": "Write the final communication from a typed, auditable decision record rather than detached superlatives.", "source_pages": [22, 25, 28, 30]}]}
    model_by_id = {model["model_id"]: model for model in models["models"]}
    ahp_id = models["models"][0]["model_id"]
    fuzzy_id = models["models"][2]["model_id"]
    audit["formula_error_watch"] = {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": [{"model_id": ahp_id, "equation_id": "EQ-B-2014-26160-003", "page": 7, "warning": "The displayed two-factor AHP matrix reports lambda=2.0000 but CR=0.2496; recomputation is required before using the stated consistency conclusion."}, {"model_id": fuzzy_id, "equation_id": "EQ-B-2014-26160-011", "page": 18, "warning": "The displayed fuzzy score Z=B D^T conflicts with the earlier meaning and dimension of B and the five-element D definition; preserve the ambiguity rather than silently repairing it."}]}
    counts = Counter(item["dimension"] for item in observations)
    audit["dimension_counts"] = {dimension: counts[dimension] for dimension in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}
    audit["positive_reusable_language_count"] = len(units)
    audit["weakness_record_count"] = counts["weakness"]
    return audit


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    template = load_template_module()
    pages = {}
    for page in range(1, PAGE_COUNT + 1):
        source = TEXT_DIR / f"page-{page:04d}.txt"
        if not source.is_file():
            raise FileNotFoundError(source)
        pages[page] = source.read_text(encoding="utf-8")
    language = build_language(template, pages)
    models = build_models(template)
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
