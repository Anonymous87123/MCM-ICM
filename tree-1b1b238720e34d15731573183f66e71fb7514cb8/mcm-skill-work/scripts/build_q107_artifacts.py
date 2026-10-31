from __future__ import annotations

"""Create-only staged learning artifacts for Queue 107."""

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2014-30680-9f0c0d05"
SHORT = "30680"
SOURCE_SHA256 = "9f0c0d05a192ebd4b1432ec1467b0edc68b1bf67b55df8f9c56d0590147c9ed9"
TYPE = "B"
YEAR = "2014"
PAGE_COUNT = 21
TEXT_DIR = ROOT / "artifacts/papers" / PAPER_ID / "text/pages"
STAGE = ROOT / "tmp/q107-stage-v4"


CHAPTERS = [
    ("summary", "abstract", 1, 1, "ABS", "The summary compresses the sport scope, yearly network route, eigenvector ranking, coach-player separation, optimization, and century ranking."),
    ("public-explainer-and-technical-title", "title", 2, 5, "TTL", "The public explainer, technical title, and contents convert the broad coach question into data, network, separation, optimization, ranking, and testing sections."),
    ("problem-and-planned-approach", "introduction", 6, 6, "INT", "The paper restates the all-time coach task and presents a six-step route from annual game graphs to historical coach ranking."),
    ("assumptions", "assumptions", 6, 7, "ASM", "The assumptions fix annual team skill, multiplicative team composition, and the player-gap condition under which coaching affects a result."),
    ("data-sources-and-collection", "data-preprocessing", 7, 9, "DAT", "The data section describes game-result collection, coach matching, standardized names, and sport-specific coverage limits."),
    ("network-construction", "problem-analysis", 9, 10, "NET", "A weighted directed graph encodes annual wins, repeated meetings, and score margins before any team ranking is calculated."),
    ("centrality-selection", "model-establishment", 9, 13, "CEN", "The paper contrasts degree, betweenness, closeness, and eigenvector centrality, then validates the chosen ranking against published polls."),
    ("coach-effect-separation", "model-improvement", 13, 16, "SEP", "Team skill is factorized into coach and player skill, then player gaps damp coach effect and determine the margin-likelihood expression."),
    ("probability-optimization", "algorithm", 16, 17, "OPT", "The joint likelihood is converted to a squared objective, rejected methods are documented, and Powell search is retained for yearly coach vectors."),
    ("career-ranking", "results", 18, 18, "RANK", "Annual top-five appearances are normalized by active years to produce the final cross-century coach lists."),
    ("testing-strengths-weaknesses", "sensitivity-robustness", 18, 20, "TEST", "Two single-game perturbations, strengths, and computational limitations bound the claimed robustness of the ranking."),
    ("conclusion-and-references", "conclusion", 20, 21, "CON", "The conclusion restates the graph-to-ranking route and the references expose the web and method dependencies needed to reproduce it."),
]

PATTERNS = [
    "LP-B-DECISION-DATA-GRAPH-CENTRALITY-OPTIMIZATION-RANK",
    "LP-B-ASSUMPTION-MECHANISM-ENABLED-CALCULATION-BOUNDARY",
    "LP-B-DATA-SOURCE-NORMALIZATION-MATCHING-COVERAGE",
    "LP-B-BASELINE-LIMITATION-REPLACEMENT-VALIDATION",
    "LP-B-EQUATION-SYMBOL-MECHANISM-HANDOFF",
    "LP-B-ALGORITHM-CANDIDATE-RESULT-SELECTION-BOUNDARY",
    "LP-B-RANK-METRIC-TABLE-INTERPRETATION-SCOPE",
    "LP-B-PERTURBATION-EXPECTED-RESPONSE-OBSERVED-BOUNDARY",
]

MOVES = [
    ("decision-route", "State a decision, then expose the data, model route, output, and limit that determine whether it can be used.", "decision -> data and model route -> output -> qualification"),
    ("assumption-contract", "Tie an assumption to its mechanism, enabled calculation, excluded uncertainty, and downstream recipient.", "entity -> assumption -> enabled operation -> boundary -> handoff"),
    ("data-provenance", "Identify the source, normalization or matching step, coverage, and downstream model consumer.", "source -> preparation -> coverage -> model input"),
    ("baseline-replacement", "Explain why a familiar baseline is insufficient before naming a more relevant metric or method.", "baseline -> limitation -> replacement -> reason"),
    ("equation-handoff", "Define the equation, its symbols, the mechanism it represents, and the quantity handed to the next step.", "definition -> symbols -> mechanism -> output"),
    ("algorithm-selection", "Compare attempted algorithms by the observed search behavior before retaining one operational route.", "candidate -> observed behavior -> decision -> limitation"),
    ("result-interpretation", "Present a calculated rank or table, interpret its metric, and preserve the population and time boundary.", "computed result -> interpretation -> scope"),
    ("sensitivity-boundary", "Describe the changed input, expected direction, observed response, and what the limited test cannot establish.", "perturbation -> expectation -> observed response -> boundary"),
]

EXAMPLES = [
    ("A ranking study states the decision target, constructs one annual interaction graph, and names the ranking measure before presenting a coach list.", "The conclusion limits that list to the data coverage and score definition used."),
    ("An assumption explains why a player-gap term suppresses the effect of a managerial decision in a lopsided contest.", "The same section names the comparison regime in which that decision can affect the result."),
    ("A data section records the source, name-matching rule, time range, and missing coverage before passing rows to a graph builder.", "A later rank is not described as historical truth when those inputs are incomplete."),
    ("A model section shows why a win-loss ratio ignores opponent strength before adopting a centrality measure.", "The replacement is checked against a declared external ranking rather than only asserted."),
    ("A formula is introduced with every variable and the quantity it transfers to the objective function.", "A source ambiguity is preserved until a visual or mathematical reconciliation resolves it."),
    ("An optimization section records a slow genetic search and a local Nelder-Mead outcome before retaining a faster Powell run.", "The selected method is still bounded by initialization and convergence diagnostics."),
    ("A career score divides repeated annual top-five appearances by active years before displaying an all-time table.", "The table does not erase sport, roster, or eligibility boundaries."),
    ("A sensitivity test identifies one altered game and compares the resulting score and rank with the original run.", "One perturbation is not called a complete robustness study."),
]

PROFILES = {
    "abstract": ("Compress the coach-selection target, data spans, graph ranking, separation mechanism, optimization route, final lists, and scope in one evidence-bearing summary.", ["sports", "data span", "graph", "centrality", "coach-player relation", "optimization", "rank"], ["decision", "route", "result", "scope"]),
    "title": ("Use an accessible problem frame, technical title, and contents to turn a public question into a graph, mechanism, and decision route without substituting informal claims for evidence.", ["audience question", "technical title", "section sequence", "graph", "player gap", "coach decision"], ["context", "route", "mechanism", "handoff"]),
    "introduction": ("Turn the requested coach ranking into explicit annual-network, centrality, separation, likelihood, optimization, and aggregation operations.", ["requested output", "annual graph", "centrality", "skill separation", "optimizer", "career score"], ["task", "steps", "outputs", "handoff"]),
    "assumptions": ("Pair each skill, data, and causal simplification with the calculation it enables and the regime it omits.", ["entity", "assumption", "enabled calculation", "excluded regime"], ["entity", "assumption", "operation", "boundary"]),
    "data-preprocessing": ("Describe source collection, standardization, name matching, and historical coverage before using data in the annual graphs.", ["source", "field", "matching rule", "time span", "missingness", "consumer"], ["source", "preparation", "coverage", "handoff"]),
    "problem-analysis": ("Define the weighted win graph, edge direction, repeated-game weight, and margin payload before centrality is computed.", ["team", "edge", "winner", "loser", "weight", "margin", "season"], ["data", "graph representation", "stored payload", "handoff"]),
    "model-establishment": ("Compare centrality candidates, reject metrics whose graph distance has the wrong meaning, then retain eigenvector centrality with a poll comparison.", ["baseline metric", "limitation", "eigenvector", "equation", "poll comparator"], ["candidates", "selection", "equation", "check"]),
    "model-improvement": ("Separate team, player, and coach skill; damp coaching by player difference; then pass the combined effect to the probability model.", ["team skill", "coach skill", "player skill", "player gap", "coach effect", "margin"], ["factorization", "gap adjustment", "likelihood handoff"]),
    "algorithm": ("Transform a game-level likelihood into an annual objective, compare solvers, retain the observed operational method, and state search limits.", ["probability", "product", "cost", "candidate solver", "result", "stopping behavior"], ["objective", "candidate comparison", "selected solver", "boundary"]),
    "results": ("Translate annual optimized coach vectors into an active-years-normalized career measure and a scoped all-time top-five table.", ["annual top five", "appearances", "active years", "career value", "sport", "rank"], ["annual output", "aggregation", "career result", "scope"]),
    "sensitivity-robustness": ("Name the altered game record, expected direction, observed percentage and rank response, then bound the inference to that local test.", ["input error", "altered game", "expected response", "score change", "rank change", "untested risk"], ["perturbation", "result", "interpretation", "limit"]),
    "conclusion": ("Reconnect the game graph, centrality, coach-player separation, optimization, and career aggregation while retaining data and reproducibility limits.", ["graph", "centrality", "skill relation", "probability", "optimizer", "career ranking", "sources"], ["route recap", "result", "boundary"]),
}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def configure(q104, base, template) -> None:
    values = {
        "PID": PAPER_ID,
        "SHORT": SHORT,
        "SHA": SOURCE_SHA256,
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


def build_language(q104, base, template, pages: dict[int, str]) -> dict:
    configure(q104, base, template)
    language = q104.build_language(base, template, pages)
    for unit in language["units"]:
        function, slots, order = PROFILES[unit["chapter"]]
        unit["function"] = function
        unit["reusable_pattern"] = " -> ".join(order)
        unit["information_order"] = order
        unit["reusable_elements"] = slots
        unit["prohibited_generalizations"] = [
            "Do not transfer a coach ranking, centrality score, skill relation, optimizer outcome, or career list without the receiving sport, game records, source version, time range, and decision rule.",
            "Do not treat a poll overlap, solver output, one-game perturbation, or a top-five table as causal proof, independent validation, or universal coach quality.",
        ]
        unit["features"]["quantitative_role"] = "bind game counts, seasons, centrality values, player gaps, margins, likelihood terms, solver outcomes, career appearances, and rank changes to their stated operation"
        unit["features"]["transition"] = "first, then, however, therefore, because, although, and finally connect graph construction, team ranking, coach separation, optimization, career aggregation, and bounded testing"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 21 UTF-8 physical-page files were read in order. Four one-at-a-time byte-bounded JPEG overview proxies covered pages 1-21, and five 107,188-216,982 byte equation crops checked formula fidelity."
        layout["ambiguities"] = [
            "The source begins with an informal public explainer on physical pages 2-3 before the technical title on page 4; all physical-page anchors are retained.",
            "Extracted text flattens displayed equations and link annotations; original rendered PNGs remain the coordinate authority and bounded JPEGs were transport-only review proxies.",
        ]
        if layout["chapter"] == "abstract":
            layout["paragraph_count"] = 3
            layout["paragraph_functions"] = [
                "State the sports, data, and annual directed-network construction.",
                "Explain eigenvector team ranking and the skill-separation mechanism.",
                "State optimization, all-time lists, and their normalized career score.",
            ]
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = 3
            layout["paragraph_functions"] = [
                "Restate the stakeholder's all-time coach question and requested scope.",
                "Turn the requested output into annual network and team-skill operations.",
                "Sequence coach separation, probability optimization, and historical aggregation.",
            ]
    return language


def equation(q104, index, page, label, latex, symbols, purpose, confidence="high"):
    return q104.equation(index, page, label, latex, symbols, purpose, confidence)


def build_models(q104, base, template) -> dict:
    configure(q104, base, template)
    eigen = [
        equation(q104, 1, 11, "eigenvector centrality", r"x_n=\lambda^{-1}\sum_{t\in M(n)}x_t=\lambda^{-1}\sum_{t\in G}a_{n,t}x_t", ["x_n", "lambda", "M(n)", "a_n,t"], "Define a node score from the scores of connected nodes."),
        equation(q104, 2, 11, "eigenvector equation", r"Ax=\lambda x", ["A", "x", "lambda"], "Express the graph-score relation in matrix form."),
        equation(q104, 3, 11, "walk-series intuition", r"S=A+\lambda^{-1}A^2+\lambda^{-2}A^3+\cdots+\lambda^{n-1}A^n+\cdots", ["S", "A", "lambda", "n"], "Give the source's walk-based intuition for eigenvector centrality.", "medium"),
    ]
    separation = [
        equation(q104, 4, 14, "team skill factorization", r"T_s=C_s\cdot P_s", ["T_s", "C_s", "P_s"], "Represent team skill as coach skill times player skill."),
        equation(q104, 5, 15, "damped coach effect", r"(C_A-C_B)\left[1/(1+\alpha|P_A-P_B|)\right]", ["C_A", "C_B", "P_A", "P_B", "alpha"], "Reduce the coach-skill difference when player skill is uneven."),
    ]
    objective = [
        equation(q104, 6, 15, "margin probability", r"K\exp\{-[(C\cdot player\ effect+D\cdot coach\ effect-margin)/E]^2\}", ["K", "C", "D", "E", "player effect", "coach effect", "margin"], "Assign a Gaussian-shaped likelihood to a game margin.", "medium"),
        equation(q104, 7, 16, "annual joint likelihood", r"\prod_{all\ games}K\exp\{-[(C\cdot player\ effect+D\cdot coach\ effect-margin)/E]^2\}", ["K", "C", "D", "E", "margin"], "Multiply the displayed game likelihood over one annual network.", "medium"),
        equation(q104, 8, 16, "squared coach objective", r"J(C_s)=\sum_{all\ games}(C\cdot player\ effect+D\cdot coach\ effect-margin)^2", ["J", "C_s", "C", "D", "margin"], "Convert the source likelihood maximization to a squared residual objective."),
    ]
    career = [
        equation(q104, 9, 18, "career top-five frequency", r"C_v=N_a/N_c", ["C_v", "N_a", "N_c"], "Normalize annual top-five appearances by active coaching years."),
    ]

    def model(index, page, section, family, purpose, inputs, outputs, equations):
        return q104.make_model(base, template, f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, section, family, purpose, inputs, outputs, equations)

    models = [
        model(1, 7, "data sources and collection", "sports-record integration", "Collect game scores and coach assignments, normalize team names, and retain sport-specific coverage limits.", ["game results", "final scores", "team names", "coach records"], ["seasonal sport records", "team-coach matches"], []),
        model(2, 9, "building the network", "weighted directed game graph", "Represent every game in one sport-year as a winner-to-loser edge with a count and margin list.", ["season game records"], ["weighted digraph", "edge margins"], []),
        model(3, 9, "analyzing the network", "eigenvector centrality", "Compare centrality measures and retain eigenvector centrality as the team-skill score.", ["weighted digraph", "adjacency matrix"], ["team centrality vector", "annual team ranking"], eigen),
        model(4, 14, "separating the coach effect", "multiplicative team-skill relation", "Express team skill as coach skill times player skill before optimizing the unknown coach vector.", ["team centrality", "coach skill", "player skill"], ["player skill as a function of team and coach skill"], separation[:1]),
        model(5, 15, "when coach skill is important", "player-gap damped coach effect", "Diminish coach-effect magnitude when player skills differ and retain it when teams are evenly matched.", ["coach skills", "player skills", "gap scale alpha"], ["coach effect"], separation[1:]),
        model(6, 15, "margin of win probability", "Gaussian margin likelihood", "Map player and coach effects to the probability of a signed game margin.", ["player effect", "coach effect", "margin", "weights"], ["per-game probability"], objective[:1]),
        model(7, 16, "optimizing the probability function", "joint likelihood and least-squares objective", "Aggregate likelihood across annual games and minimize the equivalent displayed squared cost.", ["annual game probabilities", "coach vector"], ["J(C_s)", "optimized annual coach vector"], objective[1:]),
        model(8, 16, "genetic algorithm", "stochastic evolutionary search", "Initialize coach and player vectors and evolve them, then reject the attempt for slow convergence and nonoptimal values.", ["random vectors", "fitness function"], ["rejected solver result"], []),
        model(9, 17, "Nelder-Mead method", "simplex search", "Iterate a coach-skill vector with a simplex, then reject the method after local extrema give little likelihood improvement.", ["initial coach vector", "objective"], ["rejected local solution"], []),
        model(10, 17, "Powell's method", "direction-set optimization", "Use bidirectional search along search vectors to lower the cost function for each available year.", ["initial coach vector", "search vectors", "objective"], ["selected annual coach vector", "yearly top-three table"], []),
        model(11, 18, "ranking coaches", "career-frequency aggregation", "Turn each annual optimized top-five list into an active-years-normalized career value.", ["annual top-five lists", "active years"], ["career coach values", "sport-specific top-five ranks"], career),
        model(12, 18, "testing and limitations", "local input perturbation", "Delete or reverse one recorded game and compare the resulting score and first-place rank with the unmodified run.", ["original game record", "altered game record", "annual ranking"], ["percentage score change", "rank response", "bounded robustness statement"], []),
    ]
    edges = [
        {"from_model_id": models[0]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "Matched sport-year game and coach records become weighted winner-to-loser edges with margin lists."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[2]["model_id"], "handoff": "The annual adjacency structure supplies the centrality calculation and team ranking."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "Annual team centrality is treated as team skill in the coach-player factorization."},
        {"from_model_id": models[3]["model_id"], "to_model_id": models[4]["model_id"], "handoff": "Player skill derived from team and coach skill supplies the player-gap damping term."},
        {"from_model_id": models[4]["model_id"], "to_model_id": models[5]["model_id"], "handoff": "The damped coach effect and player effect enter the margin likelihood."},
        {"from_model_id": models[5]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "Per-game likelihoods are multiplied and rewritten as the annual squared objective."},
        {"from_model_id": models[6]["model_id"], "to_model_id": models[7]["model_id"], "handoff": "The same objective is first attempted with the genetic algorithm."},
        {"from_model_id": models[7]["model_id"], "to_model_id": models[8]["model_id"], "handoff": "The unresolved annual objective is next attempted with Nelder-Mead."},
        {"from_model_id": models[8]["model_id"], "to_model_id": models[9]["model_id"], "handoff": "The failed local search motivates Powell's retained direction-set route."},
        {"from_model_id": models[9]["model_id"], "to_model_id": models[10]["model_id"], "handoff": "Each annual Powell result contributes a top-five appearance count and active-year denominator."},
        {"from_model_id": models[10]["model_id"], "to_model_id": models[11]["model_id"], "handoff": "The career ranking is perturbed by one deleted and one reversed game to inspect local input sensitivity."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PAPER_ID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SOURCE_SHA256, "year": YEAR}


def build_card(models: dict) -> dict:
    assumptions = [
        (7, "Coach skill is expressed through wins and margin, so a coach whose team wins no games is not considered good by this model."),
        (7, "Team skill is constant within a year, despite injuries and changing player skill."),
        (7, "Wins over better teams improve team skill more, enabling eigenvector centrality as the annual skill measure."),
        (7, "Team skill is multiplicative in coach and player skill, giving each coach the same effect on each player."),
        (7, "Coach effect is large only when player skills are close, and is the only win-margin factor when they are similarly matched."),
    ]
    data = [
        (8, "Game-result and coach data are collected from multiple websites, standardized, and matched through a manually created name table when source spellings differ."),
        (8, "Football results cover 1869-2013; basketball covers 1939-2013; baseball has tournament-game coverage from 1947-2013 in the summary and 1949-present in the technical section."),
        (9, "Each annual graph stores winner-to-loser edge counts and a list of score margins for repeated meetings."),
        (17, "Powell search is implemented in Python across each available yearly network, but no frozen game records, matching table, source snapshot, or run configuration is supplied."),
    ]
    verification = [
        (12, "The 2009-2010 basketball top ten from eigenvector centrality is compared with AP and USA Today lists, with six reported overlaps.", "external-list comparison", "The source exposes a named comparator and a top-ten overlap.", "A partial poll overlap is not an independent validation of historical coach effects or the probability model."),
        (19, "Deleting a 1975 Alabama win is reported to lower the coach score by about 1% without changing first place.", "single-record sensitivity", "The direction and rank response of a stated deletion are inspectable.", "One selected game and one outcome do not characterize data, parameter, structural, or solver robustness."),
        (19, "Reversing that game is reported to lower the Alabama coach score by about 4% and change first place.", "single-record stress test", "The source reports a larger directed input change and its rank consequence.", "The perturbation has no distribution, repetitions, seed, or full-ranking response."),
    ]
    results = [
        (17, "Powell's method is reported faster than Nelder-Mead and to lower the displayed cost over several thousand iterations."),
        (18, "Career value is annual top-five appearances divided by active years, yielding listed basketball, football, and baseball top fives."),
        (19, "The two changed-game tests produce approximately 1% and 4% reductions, with only the latter changing the first-ranked coach."),
        (20, "The conclusion restates the graph, eigenvector, coach-player separation, probability, annual optimization, and career-ranking chain."),
    ]
    visuals = [
        {"page": 2, "figure": "public game graph explainer", "summary": "A two-team directed-edge illustration explains the winner-to-loser encoding before the technical paper begins."},
        {"page": 3, "figure": "all-time coach ranking table", "summary": "The public explainer displays the final top-five names for the three sports."},
        {"page": 5, "figure": "contents", "summary": "The contents exposes the source sequence from data and network ranking to separation, optimization, ranking, testing, and conclusion."},
        {"page": 10, "figure": "Figure 1 annual basketball network", "summary": "The network diagram shows nodes as teams and edges as games, with conference clustering visible."},
        {"page": 11, "figure": "eigenvector equations", "summary": "The centrality definition, matrix eigenvector relation, and walk series make the selected team-ranking mechanism inspectable."},
        {"page": 12, "figure": "poll comparison table", "summary": "The three-column top-ten table compares eigenvector centrality with AP and USA Today rankings."},
        {"page": 13, "figure": "Figure 2 complete network", "summary": "Node size and darkness encode relative eigenvector centrality in the complete seasonal network."},
        {"page": 14, "figure": "team skill equation", "summary": "The centered product equation connects team skill to coach and player skill."},
        {"page": 15, "figure": "Figures 3-4 and damped effect equation", "summary": "Two margin-probability sketches and the player-gap damping expression motivate when coach effect is used."},
        {"page": 16, "figure": "joint likelihood and cost equations", "summary": "The annual product and squared objective make the optimization handoff visible."},
        {"page": 17, "figure": "Powell result table", "summary": "Three widely separated yearly top-three lists serve as the source's selected-solver output."},
        {"page": 18, "figure": "career ranking equation and table", "summary": "The career-frequency ratio and three-sport table translate annual output into the final decision artifact."},
        {"page": 19, "figure": "sensitivity narrative", "summary": "The two perturbation cases connect one changed game to score and rank response."},
    ]
    warnings = [
        (11, "The walk-series term visibly changes from negative inverse powers to lambda^(n-1) A^n; reconcile the exponent before implementing the stated intuition."),
        (14, "The multiplicative team-skill relation does not state an identifiability or normalization constraint for separately recovering coach and player skill."),
        (15, "The source writes multiword quantities such as player effect and coach effect as italicized mathematical variables; preserve and normalize their definitions before computation."),
        (16, "The likelihood-to-objective equivalence is asserted after algebra without a complete parameter, normalization, and domain specification."),
        (17, "The source acknowledges local minima and initialization sensitivity for Powell search but supplies no repeated-start protocol, tolerance, or convergence log."),
        (19, "The sensitivity evidence changes one selected game in two ways; it lacks a perturbation distribution, repetitions, full-rank analysis, and source-data audit."),
        (21, "References identify web and method sources but do not preserve versioned game records, coach matching, processed tables, solver code, or executable run settings."),
    ]
    extensions = [
        {"extension_id": f"E-B-{SHORT}-001", "page": 8, "summary": "Publish a versioned game-and-coach data dictionary, name-matching table, coverage report, and reproducible annual graph constructor."},
        {"extension_id": f"E-B-{SHORT}-002", "page": 11, "summary": "Specify centrality orientation, positivity condition, convergence tolerance, disconnected-graph handling, and a corrected walk-series derivation before reuse."},
        {"extension_id": f"E-B-{SHORT}-003", "page": 14, "summary": "Add an identifiability constraint or hierarchical model for coach and player skill, then compare alternatives against held-out game outcomes."},
        {"extension_id": f"E-B-{SHORT}-004", "page": 17, "summary": "Run seeded multi-start optimization with stopping rules, diagnostics, objective distribution, and independent out-of-sample validation."},
        {"extension_id": f"E-B-{SHORT}-005", "page": 19, "summary": "Use repeated, stratified game perturbations and report rank intervals, top-k stability, and solver uncertainty rather than two selected changes."},
    ]
    return {
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "A Networks and Machine Learning Approach to Determine the Best College Coaches of the 20th-21st Centuries",
        "award_status": "outstanding",
        "source": {"relative_path": "2014\u7f8e\u8d5b\u7279\u7b49\u5956/B-30680-Outstanding.pdf", "sha256": SOURCE_SHA256, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical pages 1-3 are a separate public explainer; the technical title appears on physical page 4 and printed technical page labels begin there."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["All 21 UTF-8 physical-page files were read sequentially, beginning with the summary and public explainer before the technical paper.", "Four one-at-a-time bounded JPEG overview proxies covered pages 1-21. Five focused JPEG equation crops of 107,188-216,982 bytes checked pages 11, 14, 15, 16, and 18.", "No original full-page PNG or multi-image result entered model transport; originals remain on disk as coordinate authority.", "No blank page, clipping, or body-text overlap was found. Red and cyan link or annotation boxes are visible on contents, headers, and references." ]},
        "context_sources": [{"type": "paper", "path": "2014\\u7f8e\\u8d5b\\u7279\\u7b49\\u5956/B-30680-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PAPER_ID}/extraction.json"}, {"type": "text-pages", "path": f"artifacts/papers/{PAPER_ID}/text/pages"}],
        "task_reconstruction": {"status": "paper-restatement-complete", "inputs": ["college game results and final margins", "team and coach identities", "season and sport labels", "published poll rankings"], "outputs": ["annual team rankings", "annual coach rankings", "career normalized top-five lists", "local sensitivity statement"], "decisions": ["which centrality ranks teams", "how team skill is separated into player and coach effects", "which optimizer generates annual coach vectors", "how annual ranks become career values", "how far local data sensitivity can be claimed"]},
        "section_map": [{"page": start, "section": key, "summary": summary} for key, _chapter, start, _end, _tag, summary in CHAPTERS],
        "assumptions": [{"page": page, "summary": summary} for page, summary in assumptions],
        "data_and_preprocessing": [{"page": page, "summary": summary} for page, summary in data],
        "models": [{"model_id": item["model_id"], "page": item["page"], "summary": item["summary"]} for item in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": page, "section": "verification", "summary": summary, "verification_type": kind, "strength": strength, "limitation": limitation} for page, summary, kind, strength, limitation in verification],
        "results_trace": [{"page": page, "summary": summary} for page, summary in results],
        "contributions": [{"page": 6, "summary": "The six-step planned approach exposes an end-to-end route before detailed mathematics."}, {"page": 9, "summary": "Winner-to-loser graph edges preserve opponent structure and score-margin payloads."}, {"page": 11, "summary": "The centrality equations and poll table make team-ranking selection inspectable."}, {"page": 15, "summary": "The player-gap term makes the intended coach-effect condition explicit."}, {"page": 16, "summary": "The likelihood and squared objective expose the annual optimization interface."}, {"page": 17, "summary": "Rejected and retained solver paths reveal a practical selection rationale."}, {"page": 19, "summary": "Two directed input changes provide a bounded, visible rank-sensitivity example."}],
        "writing_logic": [{"page": start, "summary": summary} for key, _chapter, start, _end, _tag, summary in CHAPTERS],
        "language_observations": [{"page": start, "summary": summary} for key, _chapter, start, _end, _tag, summary in CHAPTERS],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [{"page": 6, "summary": "The explicit stepwise route makes the requested decision traceable, but award status does not prove that this organization caused the award.", "evidence_class": "J"}, {"page": 12, "summary": "The named poll comparison makes an external comparator visible, without proving independent validity of coach effects.", "evidence_class": "J"}, {"page": 19, "summary": "The source reports a directed sensitivity test rather than only asserting stability, without proving complete robustness.", "evidence_class": "J"}],
        "weaknesses": [{"page": page, "summary": summary} for page, summary in warnings],
        "independent_extensions": extensions,
        "candidate_rule_impacts": [],
        "unresolved_questions": [summary for _page, summary in warnings],
        "protocol_v2_records": {},
        "review_status": "validated",
    }


def build_observations(template, language: dict, models: dict, card: dict) -> list[dict]:
    observations = template.make_observations(language, models, card)
    interpretations = {
        "language": "Reuse the rhetorical mechanism only after replacing sport, team, coach, game, time, ranking metric, solver, and decision entities.",
        "modeling": "Retain game provenance, edge orientation, centrality, skill relation, objective, solver behavior, annual aggregation, and career ranking handoffs together.",
        "logic": "Preserve the positive data-to-graph-to-team-ranking-to-coach-separation-to-optimization-to-career-ranking chain before recording warnings.",
        "visualization": "Keep figure or table labels, graph encodings, formula symbols, rank rows, comparison target, and analytical purpose together.",
        "verification": "Name the exact poll comparison, changed game, solver result, score difference, rank response, or untested uncertainty being considered.",
        "data": "Retain source, collection date, name matching, coverage, season, sport, edge orientation, margin, missingness, and downstream consumer.",
        "assumption": "Pair each skill, player-gap, data-coverage, and optimization assumption with its enabled calculation and excluded regime.",
        "result": "Keep annual centrality, player effect, coach effect, margin likelihood, objective value, top-five appearance, active years, and career value distinct.",
        "weakness": "Record source notation, identifiability, optimization, sensitivity, and reproducibility risks only after the positive learning gates.",
        "other": "Separate cited web and method context from frozen game records, matching tables, optimizer settings, executable code, and independent validation data.",
    }
    source_pages = [1, 3, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 21]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = ["Apply only when sport, season, game records, team-name matching, graph orientation, centrality convention, skill normalization, solver settings, and ranking rule are explicit."]
        row["counterevidence"] = ["A poll overlap, selected optimization run, career top-five list, or one-game sensitivity response does not establish causal coach effect, independent predictive validity, universal ranking truth, or reproducibility."]
        if row["dimension"] == "other":
            page = source_pages[other_index % len(source_pages)]
            other_index += 1
            row["page"] = page
            row["section"] = f"source provenance / evidence action {other_index}"
            row["source_basis"] = "The source identifies context, data, formula, rank, or reference material but does not preserve a versioned executable evidence package."
    return observations


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    nominated = {}
    for row in observations:
        for rule_id in row["candidate_rule_ids"]:
            nominated.setdefault(rule_id, row["observation_id"])
    rule_actions = [
        ("R-B-LANG-001", "retain the decision-to-data-to-graph-to-centrality-to-separation-to-optimization-to-ranking route with an explicit evidence boundary", "language"),
        ("R-B-LOG-001", "trace game records through graph orientation, centrality, coach-player separation, objective, solver, annual ranks, career aggregation, and sensitivity output", "logic"),
        ("R-B-DATA-001", "version game results, source retrieval, team-name matching, coach assignments, seasons, score margins, and coverage gaps", "data"),
        ("R-B-DATA-002", "maintain an assumption ledger for annual constancy, multiplicative skill, player-gap damping, data coverage, and historical comparability", "assumption"),
        ("R-B-MOD-001", "retain annual game graphs, eigenvector centrality, team-skill factorization, coach-effect damping, likelihood, objective, solver, and career aggregation with their handoffs", "modeling"),
        ("R-B-MOD-003", "require an orientation, scale, normalization, and identifiability contract whenever centrality, player skill, coach skill, and margins are combined", "modeling"),
        ("R-B-MOD-004", "keep centrality, team skill, player effect, coach effect, likelihood, objective, annual rank, and career value distinct", "result"),
        ("R-B-MOD-005", "stress graph direction, centrality convergence, skill identifiability, gap coefficient, likelihood parameters, solver starts, and career aggregation sensitivity", "modeling"),
        ("R-B-VER-002", "make every claim poll-, perturbation-, solver-, score-, rank-, or provenance-trace-specific", "verification"),
        ("R-B-VER-004", "reconcile the centrality series, multiword variables, coach-player identifiability, solver protocol, sensitivity scope, and missing reproduction files before reuse", "weakness"),
        ("R-B-VIZ-001", "retain graph encodings, centrality equations, poll table, probability sketches, objective equations, solver table, career table, and sensitivity trace with purpose", "visualization"),
        ("R-B-COMP-001", "measure source matching, annual graph construction, centrality convergence, objective evaluation, multi-start search, career aggregation, and repeated sensitivity runs separately", "other"),
    ]
    missing = [rule_id for rule_id, _action, _dimension in rule_actions if rule_id not in nominated]
    if missing:
        raise RuntimeError(f"missing nominated evidence for rule impacts: {missing}")
    card["candidate_rule_impacts"] = [{"rule_id": rule_id, "action": action, "evidence_ids": [nominated[rule_id]]} for rule_id, action, _dimension in rule_actions]


def build_audit(template, language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    audit = template.make_audit(language, models, card, observations)
    layouts = {item["chapter"]: item for item in language["chapter_layouts"]}
    units = language["units"]
    chains = [
        ("abstract", ["sports and data coverage -> annual game graphs", "eigenvector ranking -> team-skill interpretation", "coach-player separation -> likelihood, optimization, and career list"]),
        ("introduction", ["stakeholder coach question -> scope and output", "annual network and centrality -> team ranking", "skill separation and objective -> optimizer and historical aggregation"]),
    ]
    audit["paragraph_chains"] = []
    for chapter, moves in chains:
        ids = [unit["language_unit_id"] for unit in units if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": index + 1, "dominant_move": move, "language_unit_ids": [ids[index % len(ids)]]} for index, move in enumerate(moves)]})
    audit["language_unit_dispositions"] = [{"language_unit_id": unit["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": unit["candidate_pattern_ids"], "reason": "The source move is reusable only after replacing the sport, record system, graph convention, skill variables, solver, and decision scope."} for unit in units]
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": [item["summary"] for item in card["writing_logic"]] + ["Only after the positive language, organization, model, result, and visual chains are complete does the final pass record notation, identifiability, solver, sensitivity, and reproducibility warnings."],
        "section_progressions": [{"chapter": chapter, "moves": [f"input: source-checked game record, graph, equation, table, solver result, or decision question entering {chapter}", f"rhetorical job: define, motivate, derive, compare, select, aggregate, test, or bound the object in {chapter}", f"analytical job: collect, match, encode, rank, factorize, damp, optimize, normalize, or perturb", f"output: retain a typed source, graph, centrality score, skill term, objective, solver result, rank, or sensitivity response", "handoff: state the next model interface, decision table, validation comparison, or evidence boundary"], "positive_pattern": "Use explicit input -> typed operation -> inspectable output -> scoped handoff; warnings remain a final pass."} for chapter in language["available_chapters"]],
        "main_argument_chains": [
            {"claim": "Annual team comparison becomes more opponent-aware when winner-to-loser game records are encoded as weighted directed graphs and scored by eigenvector centrality.", "support_steps": ["game records", "winner-to-loser edges", "edge weights and margins", "centrality alternatives", "eigenvector equations", "poll comparison"], "decision_consequence": "Use the team score only with the stated graph orientation, sport-year coverage, and centrality convergence conditions.", "source_pages": [8, 9, 10, 11, 12, 13]},
            {"claim": "Coach ranking is made operational by factorizing team skill, damping coach differences by player gaps, and fitting a margin likelihood across annual games.", "support_steps": ["team skill", "coach-player product", "player-gap cases", "damped coach effect", "margin probability", "joint likelihood", "squared objective"], "decision_consequence": "Do not interpret separate coach skill as identified without an explicit normalization and data-generating contract.", "source_pages": [14, 15, 16]},
            {"claim": "A yearly coach vector is selected only after the source compares attempted solvers and retains Powell's method for its observed cost reduction.", "support_steps": ["genetic initialization", "slow convergence", "Nelder-Mead local extrema", "Powell direction search", "yearly top-three table"], "decision_consequence": "Run documented multi-start diagnostics before treating a selected local search as a stable optimum.", "source_pages": [16, 17]},
            {"claim": "The all-time tables follow from annual top-five appearances divided by active years, then receive a limited single-game sensitivity check.", "support_steps": ["annual top-five outputs", "career frequency ratio", "three-sport table", "deleted game", "reversed game", "score and rank response"], "decision_consequence": "Publish rank uncertainty and coverage limits rather than treating two directed changes as general robustness.", "source_pages": [18, 19, 20]},
        ],
    }
    audit["formula_error_watch"] = {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": [
        {"model_id": models["models"][2]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-003", "page": 11, "warning": "The walk-series term visibly changes the exponent sign convention; verify whether the final exponent should remain negative before implementation."},
        {"model_id": models["models"][3]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-004", "page": 14, "warning": "The team-skill product does not state the normalization needed to identify coach and player skill separately."},
        {"model_id": models["models"][4]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-005", "page": 15, "warning": "The damped-effect expression needs a calibrated alpha and an explicit regime for the approximation of similarly matched players."},
        {"model_id": models["models"][5]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-006", "page": 15, "warning": "The probability expression uses italic multiword quantities and lacks a complete parameter, normalization, and domain specification."},
        {"model_id": models["models"][6]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-007", "page": 16, "warning": "The joint product is asserted without a complete normalization or dependence contract across games."},
        {"model_id": models["models"][6]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-008", "page": 16, "warning": "The likelihood-to-objective equivalence is asserted after algebra; reconstruct the constants and objective domain before numerical reuse."},
        {"model_id": models["models"][10]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-009", "page": 18, "warning": "The active-years-normalized top-five frequency remains conditional on top-five thresholding, sport coverage, and the annual optimizer."},
    ]}
    counts = Counter(item["dimension"] for item in observations)
    audit["dimension_counts"] = {dimension: counts[dimension] for dimension in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}
    audit["positive_reusable_language_count"] = len(units)
    audit["weakness_record_count"] = counts["weakness"]
    return audit


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    q104 = load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q107")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q107")
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
        "language": {"path": f"artifacts/language-units/{PAPER_ID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]},
        "models": {"path": f"artifacts/model-units/{PAPER_ID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(model["governing_equations"]) for model in models["models"]), "review_status": models["review_status"]},
    }
    observations = build_observations(template, language, models, card)
    attach_rule_impacts(card, observations)
    audit = build_audit(template, language, models, card, observations)
    write_json(STAGE / "language.json", language)
    write_json(STAGE / "models.json", models)
    write_json(STAGE / "card.json", card)
    write_json(STAGE / "audit.json", audit)
    (STAGE / "observations.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "stage": str(STAGE), "pages_read": len(pages), "language_units": len(language["units"]), "models": len(models["models"]), "equations": sum(len(model["governing_equations"]) for model in models["models"]), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(card["visualization_observations"]), "warnings": len(card["weaknesses"]), "formula_warnings": len(audit["formula_error_watch"]["warnings"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
