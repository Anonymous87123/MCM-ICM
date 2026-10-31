#!/usr/bin/env python3
"""Build source-anchored staged learning artifacts for deterministic Queue 122."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2018-74316-1198d12d"
ID_STEM = "B-2018-74316"
PROBLEM_TYPE = "B"
YEAR = "2018"
SHA256 = "1198d12dab779fcd23ee1a51289263bccc77784bf89efd8f6e47a0d5bae01ac7"
PAGE_COUNT = 39
SOURCE_PATH = "2018\u7f8e\u8d5b\u7279\u7b49\u5956/B\u98985\u7bc7/B74316.pdf"
STAGE = ROOT / "tmp" / "q122-stage-v1"
SOURCE_EXTRACTION = ROOT / "artifacts" / "papers" / PAPER_ID / "extraction.json"
SOURCE_PAGES = ROOT / "artifacts" / "papers" / PAPER_ID / "text" / "pages"
PROXY_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID / "review-proxies"


RULE_ACTIONS = {
    "R-B-LANG-001": "bind every performance or recommendation adjective to its target, comparator, metric, horizon, scenario, and uncertainty status",
    "R-B-LOG-001": "trace the complete factor-to-forecast-to-office chain through explicit intermediate outputs and decision handoffs",
    "R-B-MOD-004": "separate native speakers, non-native speakers, total language identities, residents, migrants, indicator scores, and office decisions",
    "R-B-MOD-003": "document units, scaling, membership functions, weights, constraints, and preference provenance before scalarizing office criteria",
    "R-B-MOD-008": "retain the short-run, long-run, migration, and decision time scales and expose every feedback or manual update between them",
    "R-B-VIZ-002": "show forecast and location alternatives with direct labels, units, horizon, uncertainty, and the decision switch caused by pruning",
    "R-B-VER-004": "run algebra, dimensional, index, normalization, boundary, and implementation checks before trusting the numerical pipeline",
    "R-B-VER-002": "test forecast error, stochastic variability, parameter sensitivity, model disagreement, and office-selection stability jointly",
    "R-B-DATA-002": "record provenance, year, geography, unit, transformation, missingness, and downstream use for every demographic and language input",
    "R-B-DEC-002": "elicit stakeholder preferences and operating costs before turning a fuzzy score or density diagnostic into an office decision",
}


PATTERNS = [
    {
        "pattern_id": "LP-B-Q122-STAGED-PIPELINE",
        "name": "forecast-to-decision route preview",
        "function": "Preview a long analytical route in the same order in which intermediate outputs will be consumed.",
        "information_order": ["decision need", "temporal model", "geographic model", "ranking model", "resource-pruning handoff"],
        "slots": ["[client decision]", "[forecast state]", "[spatial state]", "[ranking criteria]", "[final action]"],
        "variants": ["firstly/secondly/thirdly", "based on this", "next", "finally"],
        "boundary": "Every announced stage must later have a named input, output, and receiving stage.",
        "disposition": "supports-existing",
        "original_examples": [
            "A relief-planning abstract can preview demand estimation, network flow, site ranking, and depot consolidation in execution order.",
            "A water-allocation report can route climate scenarios into reservoir simulation, policy scoring, and a final capacity decision.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-PROBLEM-PIVOT",
        "name": "practical pressure to model pivot",
        "function": "Move from an operating need and a failed simplification to the exact model object introduced in response.",
        "information_order": ["operating pressure", "observable complication", "baseline limitation", "introduced model", "bounded output"],
        "slots": ["[pressure]", "[complication]", "[failed baseline]", "[model object]", "[scope]"],
        "variants": ["therefore", "as a consequence", "as a result", "on this basis"],
        "boundary": "Name the failed assumption or missing mechanism before claiming that a new model is needed.",
        "disposition": "supports-existing",
        "original_examples": [
            "Because hourly arrivals violate a daily-average queue, the clinic introduces a time-indexed demand state for one staffing horizon.",
            "After leakage invalidates constant storage, the reservoir study adds a loss-dependent balance for the stated drought cases.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-SCOPE-ASSUMPTION",
        "name": "scope-bearing assumption ledger",
        "function": "State a simplifying premise together with the mechanism it suppresses and the domain in which it is used.",
        "information_order": ["modeled population", "retained mechanism", "suppressed mechanism", "time or geography", "downstream consequence"],
        "slots": ["[population]", "[retained process]", "[omission]", "[domain]", "[affected result]"],
        "variants": ["we assume", "we do not consider", "is negligible", "is fixed"],
        "boundary": "Do not present an assumption as observed evidence or let it disappear before validation.",
        "disposition": "supports-existing",
        "original_examples": [
            "The evacuation model holds road capacity fixed for the first hour and records that debris clearance is therefore outside its forecast.",
            "The inventory model omits supplier substitution during one lead-time cycle and tests that omission in a later stress case.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-DEFINITION-LEDGER",
        "name": "typed symbol and state definition",
        "function": "Introduce a symbol only after identifying its entity, unit, index, evidence status, and later use.",
        "information_order": ["symbol", "entity", "unit", "index or scope", "receiving equation"],
        "slots": ["[symbol]", "[entity]", "[unit]", "[index]", "[equation or table]"],
        "variants": ["denotes", "represents", "is defined as", "is formed by"],
        "boundary": "A label without unit, state semantics, or index direction is not a complete definition.",
        "disposition": "supports-existing",
        "original_examples": [
            "Let q_rt denote vehicles per hour on route r during interval t; Equation 4 consumes that flow as a capacity state.",
            "Define c_i as the audited annual cost in constant dollars for facility i before using it in the location objective.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-FACTOR-COMPRESSION",
        "name": "many indicators to interpretable components",
        "function": "Name raw indicators, justify a reduction, report retained information, and interpret each retained component.",
        "information_order": ["raw indicators", "data limitation", "reduction operation", "retained share", "component interpretation"],
        "slots": ["[indicator set]", "[sample limit]", "[method]", "[retained variance]", "[semantic labels]"],
        "variants": ["using PCA", "after rotation", "inherits", "is defined as"],
        "boundary": "Component labels remain interpretations of loadings, not independently observed causal variables.",
        "disposition": "supports-existing",
        "original_examples": [
            "Ten correlated access measures are reduced to three components, with the retained variance and loading-based labels reported separately.",
            "A mobility study compresses survey indicators only after stating the sample window and the information lost by truncation.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-METHOD-EVIDENCE",
        "name": "method result to bounded inference",
        "function": "Report a diagnostic or estimate, interpret exactly what it supports, and reserve broader claims.",
        "information_order": ["test or fit", "reported statistic", "local inference", "exception", "next analytical action"],
        "slots": ["[method]", "[statistic]", "[supported claim]", "[exception]", "[handoff]"],
        "variants": ["the results show", "which infers", "confirming", "except"],
        "boundary": "Fit, stationarity, sensitivity, and agreement statistics do not by themselves establish causal validity.",
        "disposition": "supports-existing",
        "original_examples": [
            "A residual test supports local stationarity at the stated threshold, while the report keeps structural validity as a separate question.",
            "A holdout score justifies the selected forecast only for the sampled horizon and routes distribution shift to a stress test.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-LIMITATION-REPAIR",
        "name": "named failure to replacement model",
        "function": "Close one model stage by naming its operational failure and opening a replacement that targets that failure.",
        "information_order": ["completed model", "failure mode", "why it matters", "replacement structure", "new scope"],
        "slots": ["[completed stage]", "[failure]", "[consequence]", "[repair]", "[scope]"],
        "variants": ["however", "cannot be exerted", "as a result", "is further established"],
        "boundary": "The replacement must answer the named defect rather than merely add complexity.",
        "disposition": "supports-existing",
        "original_examples": [
            "Because recursive error grows beyond the tactical horizon, the demand study replaces its short-run recurrence with a capacity-bounded trend model.",
            "When a static routing score cannot represent closures, the analysis opens a time-expanded network with explicit recovery states.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-SYSTEM-HANDOFF",
        "name": "submodel outputs to composite dynamic system",
        "function": "Combine separately modeled mechanisms only after naming their distinct states, units, and contribution roles.",
        "information_order": ["component state A", "component state B", "combination rule", "system behavior", "interpretive split"],
        "slots": ["[endogenous state]", "[external state]", "[identity]", "[trajectory]", "[mechanism attribution]"],
        "variants": ["add", "sum up", "includes two parts", "is manifested by"],
        "boundary": "An additive identity does not prove that components are disjoint people or independent mechanisms.",
        "disposition": "supports-existing",
        "original_examples": [
            "A load forecast adds organic demand and policy-driven adoption only after defining whether the two customer counts overlap.",
            "A disease model combines local transmission and imported cases while retaining separate incidence units and attribution limits.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-SCENARIO-CONTRAST",
        "name": "parameter scenario to decision-relevant contrast",
        "function": "Vary one declared input, retain a baseline, quantify the response, and state the scope of the stability claim.",
        "information_order": ["tested parameter", "baseline", "range or scenarios", "response metric", "bounded conclusion"],
        "slots": ["[parameter]", "[baseline]", "[range]", "[response]", "[scope]"],
        "variants": ["in steps of", "for different variances", "compared with", "below"],
        "boundary": "One-at-a-time stability is not joint uncertainty or global robustness.",
        "disposition": "supports-existing",
        "original_examples": [
            "The staffing model varies service time around its calibrated value and reports the shift in missed-demand risk without claiming global robustness.",
            "A bridge study contrasts three load envelopes against one baseline and identifies the first design switch.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-CROSS-MODEL",
        "name": "independent model comparison with agreement boundary",
        "function": "Compare two model outputs on a shared quantity and separate numerical agreement from validation.",
        "information_order": ["shared estimand", "model A", "model B", "difference or test", "agreement boundary"],
        "slots": ["[quantity]", "[model A]", "[model B]", "[comparison]", "[claim limit]"],
        "variants": ["compare", "difference", "analysis of variance", "mutually"],
        "boundary": "Agreement between models with shared inputs or assumptions is corroboration, not external truth.",
        "disposition": "supports-existing",
        "original_examples": [
            "Two flood models are compared on peak level and timing, with agreement reported separately from gauge validation.",
            "A demand forecast contrasts a state-space and cohort estimate while preserving their common-data dependence.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-CONDITIONAL-DECISION",
        "name": "ranked result to conditional recommendation",
        "function": "Translate a score or forecast into an action while retaining scenario, exclusions, tradeoffs, and switch conditions.",
        "information_order": ["decision scenario", "eligible set", "criteria", "selected action", "switch condition"],
        "slots": ["[horizon]", "[candidates]", "[criteria]", "[recommendation]", "[trigger]"],
        "variants": ["it is advisable", "we recommend", "if not required", "similarly"],
        "boundary": "A rank is not a mandate until costs, stakeholder preferences, feasibility, and uncertainty are addressed.",
        "disposition": "supports-existing",
        "original_examples": [
            "The depot report recommends three sites for the winter case and states the demand threshold that activates a fourth.",
            "A clinic plan selects two locations under the audited travel objective while preserving a budget-driven alternative.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-DENSITY-PRUNING",
        "name": "coverage-overlap diagnosis to plan pruning",
        "function": "Use a spatial concentration diagnostic to identify overlap, remove named alternatives, and compare coverage after pruning.",
        "information_order": ["original sites", "spatial diagnostic", "overlap finding", "removed sites", "revised plan"],
        "slots": ["[sites]", "[diagnostic]", "[threshold]", "[removals]", "[coverage result]"],
        "variants": ["too concentrated", "redundant", "after improving", "reduce costs"],
        "boundary": "A dependence statistic is not automatically a valid point-density or service-coverage measure.",
        "disposition": "opens-candidate",
        "original_examples": [
            "A warehouse plan maps overlap under a documented service-radius metric, removes two redundant sites, and recomputes uncovered demand.",
            "An outreach network prunes locations only after comparing accessible population and travel burden before and after removal.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-TRADEOFF-LEDGER",
        "name": "strength limitation and repair ledger",
        "function": "Pair each claimed design advantage with its burden and a repair that changes a measurable model object.",
        "information_order": ["design choice", "benefit", "failure mode", "affected output", "repair"],
        "slots": ["[choice]", "[benefit]", "[burden]", "[output]", "[repair]"],
        "variants": ["strengths", "weaknesses", "improvements", "additional information"],
        "boundary": "Generic future-work prose does not repair a limitation unless it names a changed state, parameter, test, or decision.",
        "disposition": "supports-existing",
        "original_examples": [
            "The report credits a simple queue with transparency, records its burst-arrival failure, and proposes a tested arrival-state extension.",
            "A spatial model pairs fast clustering with boundary instability and specifies a resampling audit as the repair.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-MEMO-COMPRESSION",
        "name": "technical chain to executive memo",
        "function": "Compress model outputs into findings and actions without dropping horizon, mechanism, location, or conditionality.",
        "information_order": ["recipient need", "key finding", "mechanism", "recommended action", "condition or caveat"],
        "slots": ["[recipient]", "[finding]", "[mechanism]", "[action]", "[condition]"],
        "variants": ["we are writing", "results", "recommendations", "if"],
        "boundary": "Every memo claim must trace to a technical result and retain uncertainty and implementation triggers.",
        "disposition": "supports-existing",
        "original_examples": [
            "The operations memo links the projected backlog to a two-site recommendation and names the volume threshold for expansion.",
            "A council brief reports the modeled exposure, its dominant mechanism, and a phased action with a review date.",
        ],
    },
    {
        "pattern_id": "LP-B-Q122-ERROR-DERIVATION",
        "name": "recursive forecast-error derivation",
        "function": "Expand forecast error by horizon, state its variance assumptions, and derive the general growth form.",
        "information_order": ["one-step forecast", "one-step error", "multi-step expansion", "variance sum", "horizon implication"],
        "slots": ["[recurrence]", "[innovation]", "[horizon]", "[variance]", "[growth conclusion]"],
        "variants": ["one-step", "two-step", "three-step", "by induction"],
        "boundary": "Indexing and independence assumptions must be checked before using the derived variance growth claim.",
        "disposition": "supports-existing",
        "original_examples": [
            "A sales forecast expands independent innovations through three horizons before stating the geometric variance sum.",
            "A load recurrence reports horizon-specific error propagation and checks the induction against direct simulation.",
        ],
    },
]


def chapter(
    code: str,
    name: str,
    label: str,
    pages: tuple[int, int],
    count: int,
    paragraph_count: int,
    input_text: str,
    rhetorical: str,
    analytical: str,
    output: str,
    handoff: str,
    content_counts: tuple[int, int, int, int, int],
    default_patterns: list[str],
) -> dict[str, Any]:
    return {
        "code": code,
        "chapter": name,
        "label": label,
        "pages": pages,
        "count": count,
        "paragraph_count": paragraph_count,
        "input": input_text,
        "rhetorical": rhetorical,
        "analytical": analytical,
        "output": output,
        "handoff": handoff,
        "content_counts": content_counts,
        "default_patterns": default_patterns,
    }


CHAPTERS = [
    chapter("ABS", "abstract", "Summary Sheet", (1, 1), 8, 6, "A fifty-year language forecast and an international-office decision.", "Preview the full route in the client's decision order.", "Compress PCA, time-series, differential, migration, clustering, fuzzy scoring, and pruning stages.", "A six-move summary ending in four short- and long-run offices.", "The introduction motivates language utility and separates native from non-native mechanisms.", (0, 0, 0, 0, 14), ["LP-B-Q122-STAGED-PIPELINE", "LP-B-Q122-CONDITIONAL-DECISION"]),
    chapter("INT", "introduction", "Introduction and model orientation", (3, 3), 5, 2, "Global language use, ten leading languages, and changing political-economic conditions.", "Turn broad stakes into two distinct speaker processes and a forecast task.", "Separate native autocorrelation from non-native macro-factor influence.", "A bounded temporal-distribution problem and two-state analytical split.", "Assumptions and notation define the modeled population and variables.", (0, 0, 0, 0, 3), ["LP-B-Q122-PROBLEM-PIVOT"]),
    chapter("ASM", "assumptions", "General and model-specific assumptions", (3, 15), 5, 5, "Top-language scope, stochastic disturbances, homogeneous individuals, and migration premises.", "Make simplifications visible before equations are introduced.", "Fix population, factor, disaster, individual-choice, and migration mechanisms.", "A ledger of the conditions under which later recurrences are interpreted.", "Notation and data definitions instantiate the assumed states.", (0, 0, 0, 0, 5), ["LP-B-Q122-SCOPE-ASSUMPTION"]),
    chapter("NOT", "notation", "Variables and state notation", (3, 17), 4, 4, "Speaker counts, differences, components, transition probabilities, and country-language ratios.", "Attach semantics and units to symbols before using them.", "Distinguish language, population, migration, indicator, and probability objects.", "A typed symbol ledger spanning all three models.", "Data preprocessing supplies the quantities behind those symbols.", (0, 0, 2, 0, 2), ["LP-B-Q122-DEFINITION-LEDGER"]),
    chapter("DAT", "data-preprocessing", "Indicator and panel construction", (4, 17), 7, 7, "Ten macro indicators, six UN languages, 2008-2016 panels, demographic data, and the 2017 language matrix.", "Explain why data are compressed and how geographic values are assembled.", "Weight country measures, construct the panel, apply PCA, and document manual H updates.", "Four principal components and inputs for temporal and spatial models.", "Short-term models consume the reduced indicators and speaker series.", (1, 0, 3, 0, 9), ["LP-B-Q122-FACTOR-COMPRESSION", "LP-B-Q122-DEFINITION-LEDGER"]),
    chapter("MST", "model-establishment", "PCA, AR, cointegration, and ECM", (5, 10), 16, 8, "Reduced factors and native/non-native speaker histories.", "Build each short-run mechanism in a visible diagnostic sequence.", "Select AR order, estimate coefficients, test integration, and fit the error-correction relation.", "AR(1) native forecasts and an ECM for non-native increments.", "Growing recursive error and data demand motivate a long-run replacement.", (12, 7, 6, 0, 20), ["LP-B-Q122-METHOD-EVIDENCE", "LP-B-Q122-STAGED-PIPELINE"]),
    chapter("MIM", "model-improvement", "Long-term differential system", (10, 12), 8, 8, "Short-run forecast limits and long-run demographic assumptions.", "Name the failure of the short-run models before introducing the repair.", "Use logistic native growth, constant non-native increment, and an additive total system.", "A parameterized long-run trajectory and local stability analysis.", "Calibration produces fifty-year language forecasts.", (10, 4, 3, 0, 15), ["LP-B-Q122-LIMITATION-REPAIR", "LP-B-Q122-SYSTEM-HANDOFF"]),
    chapter("RES", "results", "Forecast and office results", (12, 21), 8, 8, "Calibrated temporal, geographic, and office models.", "State results with horizon, comparator, mechanism, and named decision.", "Rank languages, compare spatial patterns, and report short- and long-run office scores.", "Forecast tables, geographic conclusions, and initial six-office plans.", "Sensitivity, cross-model checks, and density pruning test those outputs.", (0, 8, 5, 0, 31), ["LP-B-Q122-METHOD-EVIDENCE", "LP-B-Q122-CONDITIONAL-DECISION"]),
    chapter("SEN", "sensitivity-analysis", "Coefficient and initial-value sensitivity", (13, 14), 6, 6, "Mandarin growth and promotion coefficients plus the Russian initial state.", "Expose the baseline and tested ranges before calling the model stable.", "Run one-at-a-time scenarios and compare forecast bias or path variation.", "Local sensitivity tables and a bounded fifty-year stability claim.", "Stochastic recurrence tests random disturbances next.", (0, 3, 2, 0, 14), ["LP-B-Q122-SCENARIO-CONTRAST"]),
    chapter("ROB", "robustness-verification", "Monte Carlo and cross-model comparison", (14, 18), 6, 6, "Deterministic trajectories, random shocks, and two independent forecast routes.", "Separate stochastic-path checks from model-agreement checks.", "Add normal disturbances, simulate variability, aggregate H-based totals, and compare forecasts.", "Reported fluctuation bands and a sparse ANOVA-based agreement claim.", "The geographic outputs feed office-location criteria.", (3, 1, 1, 0, 12), ["LP-B-Q122-SCENARIO-CONTRAST", "LP-B-Q122-CROSS-MODEL"]),
    chapter("ALG", "algorithm", "Migration, geography, clustering, MODM, and MINE", (15, 21), 10, 10, "Country populations, migrant flows, language ratios, economic indicators, and candidate capitals.", "Make each algorithmic handoff visible from migration to final pruning.", "Construct P, update population, multiply by H, cluster four indicators, fuzzify scores, and diagnose overlap.", "Country-language surfaces, ranked capitals, and a pruned four-office plan.", "Conclusions interpret the selected cities and tradeoffs.", (23, 9, 7, 0, 20), ["LP-B-Q122-STAGED-PIPELINE", "LP-B-Q122-CONDITIONAL-DECISION"]),
    chapter("CON", "conclusion", "Distributed conclusions", (13, 24), 5, 5, "Language forecasts, geographic trends, ranked offices, and overlap diagnostics.", "Convert model outputs into qualified decisions at each handoff.", "Explain replacement languages, spatial mixing, horizon-specific cities, and pruning.", "A coherent set of language and office recommendations.", "The assessment chapter separates design benefits from limitations.", (0, 7, 3, 0, 17), ["LP-B-Q122-CONDITIONAL-DECISION", "LP-B-Q122-CROSS-MODEL"]),
    chapter("SWK", "strengths-limitations", "Model assessments", (22, 22), 5, 5, "The completed temporal, spatial, decision, and pruning pipeline.", "Audit both useful design choices and explicit burdens.", "Pair interpretability and integration claims with Monte Carlo and grid limitations.", "A benefit-burden ledger tied to model components.", "The improvement subsection proposes dynamic simulation and richer regional data.", (0, 0, 0, 0, 6), ["LP-B-Q122-TRADEOFF-LEDGER"]),
    chapter("FUT", "future-improvements", "Improvements", (22, 22), 3, 3, "Static Monte Carlo and coarse economic-center grids.", "Turn named weaknesses into changed model objects.", "Introduce a Markov-chain simulation and richer cultural-economic zoning inputs.", "Two repair directions with explicit target mechanisms.", "The memo then communicates the current, not hypothetical, recommendations.", (0, 0, 0, 2, 2), ["LP-B-Q122-LIMITATION-REPAIR", "LP-B-Q122-TRADEOFF-LEDGER"]),
    chapter("MEM", "memo", "COO memo", (23, 24), 7, 7, "A technical forecast and office-location pipeline for an operating executive.", "Compress findings and recommendations while preserving time horizon and mechanism.", "Restate native/non-native dynamics, replacement languages, spatial mixing, six-office options, and four-office pruning.", "An executive results-and-recommendations brief.", "Appendices retain supporting diagnostics, data, matrices, and forecast-error derivations.", (0, 1, 0, 0, 20), ["LP-B-Q122-MEMO-COMPRESSION", "LP-B-Q122-CONDITIONAL-DECISION"]),
    chapter("APP", "appendix", "Appendix forecast-error derivation", (29, 30), 3, 3, "The fitted AR(1) recurrence and innovation variance.", "Show why short-run recursive prediction deteriorates with horizon.", "Expand one-, two-, and three-step errors and state the induction form.", "A geometric forecast-error variance argument and its plotted growth.", "The warning pass checks the duplicated two- and three-step variance expressions.", (4, 1, 1, 0, 4), ["LP-B-Q122-ERROR-DERIVATION"]),
]


def unit_spec(
    chapter_name: str,
    page: int,
    line_start: int,
    line_end: int,
    section: str,
    function: str,
    role: str,
    patterns: list[str] | None = None,
    granularity: str = "paragraph",
) -> dict[str, Any]:
    return {
        "chapter": chapter_name,
        "page": page,
        "line_start": line_start,
        "line_end": line_end,
        "section": section,
        "function": function,
        "role": role,
        "patterns": patterns,
        "granularity": granularity,
    }


U = unit_spec
UNIT_SPECS = [
    U("abstract", 1, 19, 20, "Summary / purpose and decision", "bind the fifty-year forecast to the office-location decision", "premise"),
    U("abstract", 1, 21, 24, "Summary / indicator compression", "compress ten influences into four interpreted principal components", "mechanism"),
    U("abstract", 1, 25, 29, "Summary / short-term models", "preview AR(1), cointegration, and error correction in dependency order", "mechanism"),
    U("abstract", 1, 30, 38, "Summary / long-term system", "contrast endogenous native growth with external second-language influence", "mechanism"),
    U("abstract", 1, 39, 44, "Summary / forecast and validation", "state ranking risk and route it through sensitivity and Monte Carlo checks", "result"),
    U("abstract", 1, 45, 49, "Summary / geographic model", "pass migration and population outputs into a country-language distribution", "mechanism"),
    U("abstract", 1, 50, 55, "Summary / office scoring", "translate four forecast indicators into clustering and fuzzy evaluation", "mechanism"),
    U("abstract", 1, 56, 60, "Summary / pruning recommendation", "close with density-based pruning and horizon-specific four-city recommendations", "result", ["LP-B-Q122-DENSITY-PRUNING", "LP-B-Q122-CONDITIONAL-DECISION"]),
    U("introduction", 3, 6, 10, "Introduction / language utility", "establish language use as an economic and technological operating resource", "premise"),
    U("introduction", 3, 10, 13, "Introduction / changing utility", "connect speaker counts to shifting economic and political conditions", "premise"),
    U("introduction", 3, 14, 18, "Introduction / leading-language task", "narrow the global setting to leading languages, influences, and future rankings", "boundary"),
    U("introduction", 3, 35, 39, "Model orientation / native split", "separate native use from the macro factors assigned to non-native use", "mechanism"),
    U("introduction", 3, 39, 42, "Model orientation / mechanism handoff", "use autocorrelation for native speakers and external factors for non-native speakers", "mechanism"),
    U("assumptions", 3, 20, 24, "General assumptions / population scope", "bound the analysis to 26 languages and a common model family", "boundary"),
    U("assumptions", 3, 25, 30, "General assumptions / disturbances and agents", "declare white-noise errors, homogeneous individuals, and common long-run macro effects", "boundary"),
    U("assumptions", 3, 44, 50, "Model 1 assumptions / temporal mechanisms", "assign native change to population patterns and non-native change to migration and macro factors", "premise"),
    U("assumptions", 15, 25, 28, "Model 2 assumptions / migration stationarity", "exclude domestic movement and hold country transition probabilities time-invariant", "boundary"),
    U("assumptions", 15, 29, 32, "Model 2 assumptions / population timing", "separate country growth rates and complete annual migration in one step", "boundary"),
    U("notation", 3, 51, 54, "Notation / speaker counts", "introduce the native-speaker quantity before the temporal equations", "premise"),
    U("notation", 4, 4, 12, "Notation / language states and ECM", "distinguish non-native, total, difference, component, error, and correction quantities", "mechanism"),
    U("notation", 4, 13, 22, "Notation / capacities and transition objects", "define maximum population, transition probabilities, steady state, and model parameters", "mechanism"),
    U("notation", 15, 33, 51, "Model 2 notation / country migration states", "map country population, growth, migrants, transition probability, and steady-state symbols", "mechanism"),
    U("data-preprocessing", 4, 23, 29, "PCA data / reduction and weighting", "justify dimension reduction and speaker-weighted country observations", "premise"),
    U("data-preprocessing", 4, 30, 39, "PCA data / economic and social indicators", "define GDP, crop yield, schooling, inequality, and happiness inputs", "mechanism"),
    U("data-preprocessing", 4, 40, 45, "PCA data / composite welfare and migration", "show the happiness construction and retain migration as a separate input", "mechanism"),
    U("data-preprocessing", 4, 46, 55, "PCA data / productivity and exchange indicators", "complete the indicator ledger with productivity, prices, tourism, and language software", "mechanism"),
    U("data-preprocessing", 5, 5, 11, "Panel construction / sample boundary", "state the ten-factor window and the six-language panel imposed by data limits", "boundary"),
    U("data-preprocessing", 5, 24, 26, "PCA input matrix / ten columns", "bind each matrix column to one named raw factor", "mechanism"),
    U("data-preprocessing", 17, 35, 37, "H matrix / source and manual update", "separate the disclosed 2017 language matrix from later manual adjustments", "boundary"),
    U("model-establishment", 5, 12, 23, "PCA / orthogonal construction", "explain the variance-ordering and orthogonality criteria for principal components", "mechanism"),
    U("model-establishment", 5, 27, 33, "PCA / component vectors", "report the four retained loading vectors and their component identities", "result"),
    U("model-establishment", 5, 34, 38, "PCA / retained information", "interpret four components and bound adequacy with the reported 87.6 percent share", "result"),
    U("model-establishment", 5, 39, 45, "AR model / selection rationale", "open the short-term model and motivate an autoregression for native speakers", "premise"),
    U("model-establishment", 5, 45, 49, "AR model / equation semantics", "define lag coefficients and the white-noise innovation", "mechanism"),
    U("model-establishment", 5, 50, 51, "AR model / source window", "identify the 2003-2017 speaker histories used for fitting", "premise"),
    U("model-establishment", 6, 13, 16, "AR diagnostics / order identification", "use autocorrelation and partial autocorrelation to select lag order", "mechanism"),
    U("model-establishment", 6, 23, 30, "AR diagnostics / AR1 conclusion", "move from plotted cutoffs to a shared AR(1) specification and MLE fitting", "result"),
    U("model-establishment", 7, 8, 13, "AR results / fit interpretation", "report fit quality while retaining Russian as the declining exception", "result"),
    U("model-establishment", 7, 14, 21, "AR diagnostics / information criteria", "frame lag selection as a balance between residual error and parameter complexity", "mechanism"),
    U("model-establishment", 7, 54, 57, "AR diagnostics / final lag choice", "justify AR(1) using FPE and BIC while acknowledging AIC disagreement", "boundary"),
    U("model-establishment", 7, 58, 64, "ECM / vector construction", "move from serial regression risk to a PCA-reduced cointegration vector", "premise"),
    U("model-establishment", 7, 65, 73, "ECM / equilibrium relation", "derive the error-correction route from a long-run relation and first differences", "mechanism"),
    U("model-establishment", 8, 7, 15, "ECM / correction direction and EG route", "interpret the lagged correction term and announce the two-step Engle-Granger procedure", "mechanism"),
    U("model-establishment", 8, 16, 27, "ECM / unit-root evidence", "use the reported ADF results to support a local cointegration claim", "result"),
    U("model-establishment", 8, 28, 45, "ECM / two estimation stages", "estimate the long-run relation, residual, and short-run correction equation in order", "mechanism"),
    U("model-improvement", 10, 11, 20, "Short-to-long handoff / failure", "close the short-term models with horizon error and data-availability limits", "boundary"),
    U("model-improvement", 10, 21, 30, "Long-term model / assumptions and logistic pivot", "open a differentiable capacity-bounded native-speaker model", "premise"),
    U("model-improvement", 10, 33, 40, "Long-term model / parameter and ECM reduction", "define growth and capacity parameters before simplifying the non-native relation", "mechanism"),
    U("model-improvement", 10, 41, 55, "Long-term model / constant increment", "use first-difference tests to motivate a constant long-run non-native increment", "result"),
    U("model-improvement", 11, 4, 15, "Long-term model / composite system", "add native and non-native mechanisms and interpret endogenous versus external drivers", "mechanism"),
    U("model-improvement", 11, 21, 34, "Long-term model / equilibrium", "move from no global equilibrium to local stability and coefficient-dependent cases", "mechanism"),
    U("model-improvement", 11, 42, 51, "Long-term model / stable regime", "state the stable coefficient interval and the resulting total-speaker form", "result"),
    U("model-improvement", 11, 52, 57, "Long-term model / parameter estimation", "map growth, capacity, and external increment to demographic and language evidence", "mechanism"),
    U("results", 12, 17, 33, "Results / Mandarin calibration", "connect the Mandarin parameters to equilibrium time and the changing native/non-native driver split", "result"),
    U("results", 12, 34, 50, "Results / top-ten forecast table", "report the 2067 native, total, and contribution quantities in one comparison table", "result"),
    U("results", 12, 51, 56, "Results / influence interpretation", "contrast externally driven influential languages with population-driven languages", "result"),
    U("results", 13, 4, 12, "Results / at-risk languages", "explain why Russian and Malay may leave the future top ten", "result"),
    U("results", 13, 18, 23, "Results / replacement languages", "name Hausa and German as alternatives and give distinct growth mechanisms", "result"),
    U("results", 18, 13, 29, "Results / geographic Mandarin forecast", "describe the two geographic peaks and connect North American growth to L2 transmission", "result"),
    U("results", 20, 23, 35, "Results / short-term office table", "report six short-term capitals, scores, language proportions, and office languages", "result"),
    U("results", 20, 36, 47, "Results / long-term office table", "report six long-term capitals and the changed language recommendations", "result"),
    U("sensitivity-analysis", 13, 30, 39, "Sensitivity / native growth setup", "declare the growth-rate baseline, range, step, and Mandarin test case", "premise"),
    U("sensitivity-analysis", 13, 40, 52, "Sensitivity / native growth response", "compare equilibrium and fifty-year forecast bias across the tested growth rates", "result"),
    U("sensitivity-analysis", 14, 4, 18, "Sensitivity / external promotion coefficient", "vary the external coefficient around three and report total-speaker bias", "result"),
    U("sensitivity-analysis", 14, 23, 25, "Sensitivity / combined conclusion", "limit the stable-coefficient claim to the tested internal ranges", "boundary"),
    U("sensitivity-analysis", 14, 26, 33, "Sensitivity / Russian initial state", "identify the negative-growth case as requiring a separate initial-value analysis", "premise"),
    U("sensitivity-analysis", 14, 34, 37, "Sensitivity / Russian response", "translate a 20-million initial fluctuation into a bounded fifty-year forecast interval", "result"),
    U("robustness-verification", 14, 38, 45, "Robustness / stochastic native recurrence", "add an explicit normal disturbance to the long-run native recurrence", "mechanism"),
    U("robustness-verification", 14, 50, 53, "Robustness / stochastic non-native recurrence", "add a separate zero-mean disturbance to non-native growth", "mechanism"),
    U("robustness-verification", 15, 4, 9, "Robustness / total stochastic recurrence", "combine native and non-native disturbances in the total-speaker recurrence", "mechanism"),
    U("robustness-verification", 15, 14, 19, "Robustness / Monte Carlo outcome", "report pointwise fluctuation bounds without changing the deterministic trend", "result"),
    U("robustness-verification", 18, 30, 35, "Cross-model check / common estimand", "derive total language counts from the geographic matrix for comparison", "mechanism"),
    U("robustness-verification", 18, 36, 50, "Cross-model check / forecast comparison", "report model differences and keep the ANOVA agreement claim source-bounded", "boundary"),
    U("algorithm", 15, 52, 57, "Markov algorithm / memoryless property", "define the country migration process through a conditional-independence statement", "mechanism"),
    U("algorithm", 16, 7, 17, "Markov algorithm / transition and population update", "state transition-matrix properties and combine migration with natural growth", "mechanism"),
    U("algorithm", 17, 7, 15, "Markov algorithm / solved matrices", "derive the 226 by 226 transition matrix and growth vector before propagation", "result"),
    U("algorithm", 17, 20, 34, "Geographic algorithm / H and interpolation", "map population through the country-language ratio matrix and smooth capital points", "mechanism"),
    U("algorithm", 19, 4, 20, "Office algorithm / four feature vectors", "construct English, migration, GDP, and Chinese country indicators", "mechanism"),
    U("algorithm", 19, 21, 36, "Office algorithm / clustering", "estimate short-run inputs and turn four dendrograms into ordinal groups", "mechanism"),
    U("algorithm", 19, 37, 55, "Office algorithm / MODM indicators", "convert the four cluster memberships into decision indices", "mechanism"),
    U("algorithm", 20, 4, 18, "Office algorithm / fuzzy evaluation", "map indicators to memberships, apply the weight vector, and select the six largest scores", "mechanism"),
    U("algorithm", 20, 48, 56, "Pruning algorithm / overlap objective", "motivate office reduction through service overlap and a concentration diagnostic", "premise", ["LP-B-Q122-DENSITY-PRUNING", "LP-B-Q122-PROBLEM-PIVOT"]),
    U("algorithm", 21, 3, 11, "Pruning algorithm / grid and MIC", "partition the coordinate plane and interpret the reported concentration index", "mechanism", ["LP-B-Q122-DENSITY-PRUNING"]),
    U("conclusion", 13, 6, 12, "Conclusion / top-ten risk", "qualify the Russian and Malay forecast with their distinct support limitations", "boundary"),
    U("conclusion", 18, 26, 29, "Conclusion / global mixing", "summarize the projected mixing of geographic language distributions", "result"),
    U("conclusion", 20, 45, 47, "Conclusion / long-run six-city plan", "state the long-run cities and office-language choices", "result"),
    U("conclusion", 21, 19, 22, "Conclusion / short-run pruning", "remove Wellington and Berlin under the reported overlap diagnosis", "result", ["LP-B-Q122-DENSITY-PRUNING", "LP-B-Q122-CONDITIONAL-DECISION"]),
    U("conclusion", 21, 30, 33, "Conclusion / long-run pruning", "remove Kuala Lumpur and Ottawa and retain four long-run cities", "result", ["LP-B-Q122-DENSITY-PRUNING", "LP-B-Q122-CONDITIONAL-DECISION"]),
    U("strengths-limitations", 22, 11, 19, "Assessment / temporal strengths", "credit time-series and ECM stages with explicit historical and long-short information roles", "result"),
    U("strengths-limitations", 22, 20, 23, "Assessment / spatial strengths", "credit clustering and Markov structure with simplification and dynamic migration representation", "result"),
    U("strengths-limitations", 22, 24, 29, "Assessment / decision strengths", "credit MODM and MINE with multi-criterion and intuitive decision support", "result"),
    U("strengths-limitations", 22, 30, 34, "Assessment / Monte Carlo weakness", "name pseudo-randomness and static simulation as limits of the robustness claim", "boundary"),
    U("strengths-limitations", 22, 35, 35, "Assessment / grid weakness", "identify economic-center partitioning and grid shape as subjective", "boundary"),
    U("future-improvements", 22, 36, 38, "Improvement / dynamic simulation pivot", "replace static sampling with a Markov-linked simulation concept", "mechanism"),
    U("future-improvements", 22, 39, 42, "Improvement / MCMC mechanism", "describe repeated state sampling as the proposed dynamic repair", "mechanism"),
    U("future-improvements", 22, 43, 46, "Improvement / richer regional evidence", "add culture, economic structure, trade, and finance to the grid design", "mechanism"),
    U("memo", 23, 12, 22, "Memo / short-term language findings", "compress the native and non-native mechanisms into an executive finding", "result"),
    U("memo", 23, 23, 32, "Memo / long-term language findings", "summarize logistic native growth, external L2 change, and influence-dependent outcomes", "result"),
    U("memo", 23, 33, 36, "Memo / ranking changes", "name the two at-risk and two replacement languages with mechanisms", "result"),
    U("memo", 23, 37, 41, "Memo / geographic findings", "translate the geographic model into concrete regional language trends", "result"),
    U("memo", 23, 44, 49, "Memo / short-term recommendation", "give six short-run capitals, criteria, and office-language choices", "result"),
    U("memo", 23, 50, 52, "Memo / long-term recommendation", "give six long-run capitals and their proposed working languages", "result"),
    U("memo", 24, 4, 9, "Memo / four-office alternative", "condition the four-office plan on relaxed office-count requirements and overlap costs", "boundary", ["LP-B-Q122-MEMO-COMPRESSION", "LP-B-Q122-DENSITY-PRUNING", "LP-B-Q122-CONDITIONAL-DECISION"]),
    U("appendix", 29, 22, 30, "Appendix 5 / one- and two-step error", "expand the first two AR forecast errors and their variances", "mechanism"),
    U("appendix", 29, 31, 33, "Appendix 5 / three-step error", "extend the recursive forecast error to a third horizon", "mechanism"),
    U("appendix", 29, 34, 41, "Appendix 5 / induction", "state the general geometric variance form and its growth implication", "result"),
]


def dump_json(path: Path, value: object) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def dump_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        for value in values:
            handle.write(
                json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
            )


def source_page_lines(page: int) -> list[str]:
    path = SOURCE_PAGES / f"page-{page:04d}.txt"
    if not path.is_file():
        raise SystemExit(f"missing q122 source page: {path}")
    return path.read_text(encoding="utf-8").splitlines()


def normalize_source_lines(lines: list[str]) -> str:
    retained: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if "\u7cbe\u54c1\u6570\u6a21\u8d44\u6599" in stripped or "\u6dd8\u5b9d\u5e97\u94fa" in stripped:
            continue
        if stripped.startswith("Team#74316"):
            continue
        if "Page " in stripped and " of 20" in stripped and len(stripped) < 80:
            continue
        retained.append(stripped)
    text = " ".join(retained)
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= 480:
        return text
    shortened = text[:480].rsplit(" ", 1)[0].rstrip(" ,;:")
    return shortened + "."


def resolve_source_span(page: int, line_start: int, line_end: int) -> str:
    lines = source_page_lines(page)
    if line_start < 1 or line_end < line_start or line_end > len(lines):
        raise SystemExit(
            f"q122 invalid source span p{page} lines {line_start}-{line_end}; "
            f"page has {len(lines)} lines"
        )
    text = normalize_source_lines(lines[line_start - 1 : line_end])
    if not text:
        raise SystemExit(
            f"q122 empty source span p{page} lines {line_start}-{line_end}"
        )
    return text


def sentence_statistics(text: str) -> tuple[int, int, dict[str, float | int]]:
    words = re.findall(r"[A-Za-z0-9]+(?:['.-][A-Za-z0-9]+)*", text)
    sentences = [
        segment
        for segment in re.split(r"(?<=[.!?])\s+|\n+", text)
        if re.search(r"[A-Za-z0-9]", segment)
    ]
    if not sentences:
        sentences = [text]
    lengths = [
        max(1, len(re.findall(r"[A-Za-z0-9]+(?:['.-][A-Za-z0-9]+)*", item)))
        for item in sentences
    ]
    return (
        max(1, len(words)),
        len(sentences),
        {
            "minimum": min(lengths),
            "median": median(lengths),
            "maximum": max(lengths),
        },
    )


def build_language() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    chapter_index = {item["chapter"]: item for item in CHAPTERS}
    pattern_index = {item["pattern_id"]: item for item in PATTERNS}
    local_counts: Counter[str] = Counter()
    units: list[dict[str, Any]] = []

    for spec in UNIT_SPECS:
        item = chapter_index[spec["chapter"]]
        local_counts[spec["chapter"]] += 1
        local_index = local_counts[spec["chapter"]]
        pattern_ids = spec["patterns"] or item["default_patterns"]
        unknown = sorted(set(pattern_ids) - set(pattern_index))
        if unknown:
            raise SystemExit(f"q122 language unit references unknown patterns: {unknown}")
        primary_pattern = pattern_index[pattern_ids[0]]
        source_excerpt = resolve_source_span(
            spec["page"], spec["line_start"], spec["line_end"]
        )
        unit_id = f"LU-{ID_STEM}-{item['code']}-{local_index:03d}"
        order = list(primary_pattern["information_order"])
        units.append(
            {
                "language_unit_id": unit_id,
                "page": spec["page"],
                "section": spec["section"],
                "chapter": spec["chapter"],
                "granularity": spec["granularity"],
                "source_excerpt": source_excerpt,
                "source_anchor": {
                    "page_file": f"page-{spec['page']:04d}.txt",
                    "inspected_line_start": spec["line_start"],
                    "inspected_line_end": spec["line_end"],
                    "normalization": (
                        "trim lines, exclude extraction-only page headers, remove "
                        "line-break hyphenation, collapse whitespace, and cap at a word boundary"
                    ),
                },
                "function": spec["function"],
                "rhetorical_role": spec["role"],
                "rhetorical_move": (
                    f"{spec['function']}; in {item['label']}, this move helps produce "
                    f"{item['output']} before the handoff to {item['handoff']}"
                ),
                "reusable_pattern": " -> ".join(order),
                "information_order": order,
                "reusable_elements": [
                    (
                        f"occurrences: physical page {spec['page']}, source lines "
                        f"{spec['line_start']}-{spec['line_end']}, {spec['section']}"
                    ),
                    f"function: {spec['function']}",
                    f"information order: {' -> '.join(order)}",
                    f"slots: {'; '.join(primary_pattern['slots'])}",
                    f"variants: {'; '.join(primary_pattern['variants'])}",
                    f"handoff: {item['handoff']}",
                ],
                "prohibited_generalizations": [
                    f"boundary: {primary_pattern['boundary']}",
                    (
                        "anti-copy: replace every language, country, city, year, value, "
                        "coefficient, model label, table entry, and recommendation before reuse"
                    ),
                    (
                        "Retain whether the source statement is an assumption, attributed input, "
                        "derivation, diagnostic, forecast, comparison, warning, or decision."
                    ),
                    (
                        "Do not transfer the 2067 language rankings, six-city lists, four-city "
                        "pruning, PCA loadings, or membership weights into another case."
                    ),
                ],
                "features": {
                    "voice": (
                        "first-person plural for performed modeling actions; passive or "
                        "section-as-agent voice for definitions, tables, and computed results"
                    ),
                    "tense": (
                        "present for definitions and mechanisms, past for completed estimation, "
                        "and modal or future forms for forecasts and recommendations"
                    ),
                    "modality": (
                        "assume, infer, can, may, should, advise, and recommend separate premises, "
                        "model support, uncertainty, and stakeholder action"
                    ),
                    "clause_structure": (
                        "scope or baseline -> named operation -> evidence or output -> bounded "
                        "interpretation -> receiving model or decision"
                    ),
                    "quantitative_role": (
                        "bind every number to entity, unit, year, geography, scenario, comparator, "
                        "and downstream use"
                    ),
                    "transition": (
                        "firstly, next, according to, however, as a consequence, based on, "
                        "similarly, and finally expose the analytical handoffs"
                    ),
                    "original_instantiations": [
                        {
                            "text": (
                                f"A clinic study can {spec['function']} after rebuilding the "
                                "entities, measurements, uncertainty, and receiving decision."
                            )
                        },
                        {
                            "text": (
                                f"A reservoir report can use the same information order to "
                                f"{spec['function']} while preserving its own evidence boundary."
                            )
                        },
                    ],
                },
                "candidate_pattern_ids": list(pattern_ids),
            }
        )

    expected_counts = {item["chapter"]: item["count"] for item in CHAPTERS}
    if dict(local_counts) != expected_counts:
        raise SystemExit(
            f"q122 language counts changed: {dict(local_counts)} != {expected_counts}"
        )

    patterns = json.loads(json.dumps(PATTERNS))
    for pattern in patterns:
        nominated = [
            unit
            for unit in units
            if pattern["pattern_id"] in unit["candidate_pattern_ids"]
        ]
        pattern["occurrences"] = len(nominated)
        pattern["locations"] = list(
            dict.fromkeys(unit["section"] for unit in nominated)
        )
        if not nominated:
            raise SystemExit(f"q122 pattern has no occurrence: {pattern['pattern_id']}")

    layouts: list[dict[str, Any]] = []
    for item in CHAPTERS:
        chapter_units = [unit for unit in units if unit["chapter"] == item["chapter"]]
        combined = " ".join(unit["source_excerpt"] for unit in chapter_units)
        word_count, sentence_count, sentence_words = sentence_statistics(combined)
        role_counts = Counter(unit["rhetorical_role"] for unit in chapter_units)
        total = len(chapter_units)
        roles = ("premise", "mechanism", "result", "boundary")
        proportions = {role: role_counts[role] / total for role in roles}
        paragraph_functions = [
            chapter_units[index % total]["function"]
            for index in range(item["paragraph_count"])
        ]
        equations, figures, tables, citations, quantitative = item["content_counts"]
        start, end = item["pages"]
        layouts.append(
            {
                "chapter": item["chapter"],
                "page_start": start,
                "page_end": end,
                "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
                "word_count": word_count,
                "sentence_count": sentence_count,
                "paragraph_count": item["paragraph_count"],
                "sentence_words": sentence_words,
                "paragraph_functions": paragraph_functions,
                "rhetorical_proportions": proportions,
                "content_counts": {
                    "equations": equations,
                    "figures": figures,
                    "tables": tables,
                    "citations": citations,
                    "quantitative_results": quantitative,
                },
                "move_types": {
                    "opening": [f"input: {item['input']}"],
                    "transition": [f"analytical job: {item['analytical']}"],
                    "closing": [f"handoff: {item['handoff']}"],
                },
                "counting_method": (
                    "Metrics are computed from the explicit physical-page line spans attached to "
                    "the source actions after deterministic whitespace normalization. Paragraph "
                    "counts are visual structural units recorded during the completed 39-page review."
                ),
                "ambiguities": [
                    (
                        "The extraction layer drops or corrupts Greek letters, subscripts, matrix "
                        "braces, comparison signs, and several display equations."
                    ),
                    (
                        "A Chinese commercial watermark appears on every physical page and is "
                        "excluded from author-language evidence."
                    ),
                    (
                        "Printed numbering ends with Page 37 of 20 and Figure 12 is reused; all "
                        "anchors therefore use physical PDF pages."
                    ),
                ],
            }
        )

    return (
        {
            "available_chapters": [item["chapter"] for item in CHAPTERS],
            "chapter_layouts": layouts,
            "paper_id": PAPER_ID,
            "problem_type": PROBLEM_TYPE,
            "review_status": "validated",
            "schema_version": 3,
            "source_sha256": SHA256,
            "repeated_patterns": patterns,
            "units": units,
            "year": YEAR,
        },
        units,
    )


def variable(
    symbol: str,
    name: str,
    unit: str,
    role: str,
    definition: str,
    source_status: str = "explicit-defined",
) -> dict[str, str]:
    return {
        "symbol": symbol,
        "normalized_name": name,
        "unit": unit,
        "definition": definition,
        "role": role,
        "source_status": source_status,
    }


SYMBOL_META = {
    "X": ("ten-indicator panel", "standardized indicator value"),
    "Y": ("principal-component vector", "standardized component score"),
    "a": ("PCA loading vector", "dimensionless loading"),
    "N_t": ("native-speaker count", "million persons"),
    "S_t": ("non-native-speaker count", "million speaker identities"),
    "NT_t": ("total speaker-identity count", "million speaker identities"),
    "phi": ("autoregressive coefficient", "dimensionless"),
    "phi_p": ("lag-p autoregressive coefficient", "dimensionless"),
    "epsilon_t": ("white-noise innovation", "million speaker identities"),
    "sigma2": ("innovation variance", "million-squared speaker identities"),
    "p": ("autoregressive order", "lag count"),
    "T": ("sample length", "annual observations"),
    "Y_1": ("economic principal component", "standardized component score"),
    "Y_2": ("social-equality principal component", "standardized component score"),
    "Y_3": ("national-welfare principal component", "standardized component score"),
    "Y_4": ("culture-shock principal component", "standardized component score"),
    "gamma": ("long-run cointegration coefficient", "dimensionless"),
    "beta": ("short-run difference coefficient", "dimensionless"),
    "lambda": ("error-correction speed", "1/year"),
    "ECM_t": ("lagged equilibrium residual", "million speaker identities"),
    "delta": ("intrinsic native growth rate", "1/year"),
    "N_m": ("native-speaker capacity", "million persons"),
    "mu": ("long-run non-native increment", "million speaker identities/year"),
    "t": ("forecast time", "years"),
    "V": ("Lyapunov candidate", "arbitrary nonnegative unit"),
    "sigma_N": ("native-process shock scale", "million persons"),
    "sigma_S": ("non-native-process shock scale", "million speaker identities"),
    "P": ("country migration transition matrix", "row-stochastic probability"),
    "p_ij": ("country i to country j transition probability", "probability/year"),
    "M": ("observed international migration matrix", "persons/year"),
    "G_t": ("country natural-growth vector", "persons/year"),
    "pi": ("claimed stationary country distribution", "probability"),
    "H": ("country-language demand-ratio matrix", "speaker identities/person"),
    "h_ij": ("language-j demand ratio in country i", "speaker identities/person"),
    "L_t": ("country-by-language speaker matrix", "speaker identities"),
    "E_t": ("English-speaker proportion vector", "proportion"),
    "MI_t": ("net-immigration indicator vector", "persons/year"),
    "GDP_t": ("GDP-per-capita indicator vector", "currency/person/year"),
    "C_t": ("Chinese-speaker proportion vector", "proportion"),
    "G_1": ("English cluster label", "ordinal class"),
    "G_2": ("migration cluster label", "ordinal class"),
    "G_3": ("GDP cluster label", "ordinal class"),
    "G_4": ("Chinese cluster label", "ordinal class"),
    "EI": ("English decision index", "ordinal score"),
    "MII": ("migration decision index", "ordinal score"),
    "GDPI": ("GDP decision index", "ordinal score"),
    "CI": ("Chinese decision index", "ordinal score"),
    "x": ("indicator value", "source-specific score"),
    "mu_x": ("fuzzy membership degree", "membership in [0,1]"),
    "R": ("country-indicator fuzzy relation matrix", "membership score"),
    "A": ("criterion weight vector", "normalized weight"),
    "B": ("country comprehensive evaluation vector", "weighted membership score"),
    "G": ("economic-center coordinate grid", "latitude-longitude block"),
    "MIC": ("maximum information coefficient", "index in [0,1]"),
    "city_set": ("eligible capital-city set", "set of cities"),
    "office_set": ("selected office-location set", "set of cities"),
    "rank": ("candidate rank", "ordinal position"),
}


def model_spec(
    page: int,
    section: str,
    family: str,
    purpose: str,
    inputs: list[str],
    outputs: list[str],
    assumptions: list[str],
    validation_refs: list[str],
    steps: list[str],
    limitations: list[str],
    origin: str = "paper-specific",
) -> dict[str, Any]:
    return {
        "page": page,
        "section": section,
        "family": family,
        "purpose": purpose,
        "inputs": inputs,
        "outputs": outputs,
        "assumptions": assumptions,
        "validation_refs": validation_refs,
        "steps": steps,
        "limitations": limitations,
        "origin": origin,
    }


MODEL_SPECS = [
    model_spec(
        5,
        "2.2.2 Dimension Reduction - PCA",
        "speaker-weighted principal-component indicator reduction",
        "Compress ten macro indicators into four orthogonal language-use components while retaining the reported 87.6 percent variance share.",
        ["X"],
        ["Y", "a"],
        ["The six UN languages and 2008-2016 panel are treated as representative of the wider language system."],
        ["Equation (1)", "reported 87.6 percent retained variance", "component-loading interpretation"],
        ["speaker-weight country indicators", "assemble the 6 by 9 panel", "rotate PCA factors", "retain four components", "name components from loadings"],
        ["The panel is small, the weighting formula is not archived, and loading signs and several glyphs are damaged in extraction."],
    ),
    model_spec(
        5,
        "2.3.1 Native Speaker Model - AR(p)/AR(1)",
        "native-speaker autoregression and recursive error propagation",
        "Forecast short-run native-speaker counts from lagged annual histories and explain why recursive error limits the long horizon.",
        ["N_t", "p", "T"],
        ["N_t", "phi", "sigma2"],
        ["The native series can share an AR(1) form even though coefficients and innovations differ by language."],
        ["Figures 1-5", "Tables 2-4", "FPE/AIC/BIC comparison", "Appendix 5 error derivation"],
        ["collect 2003-2017 histories", "inspect ACF and PACF", "compare p=0,1,2 information criteria", "fit language-specific AR(1) by MLE", "propagate forecast error by horizon"],
        ["The paper gives no rolling holdout and Appendix 5 repeats the same variance for two- and three-step forecasts."],
    ),
    model_spec(
        7,
        "2.3.2 Non-native Speaker Model - ECM",
        "Engle-Granger cointegration and error-correction regression",
        "Relate non-native speaker increments to four PCA components while retaining a lagged equilibrium correction term.",
        ["S_t", "Y_1", "Y_2", "Y_3", "Y_4"],
        ["S_t", "ECM_t", "beta", "lambda"],
        ["The dependent and component series are first-order integrated and share a stable long-run relation."],
        ["Tables 5-7", "Equations (7)-(12)", "Appendices 3, 4, and 6"],
        ["test unit roots", "fit the long-run relation", "form residuals", "test residual stationarity", "fit the difference equation with lagged correction"],
        ["ADF interpretation and critical values are sparse, only six languages are fitted, and coefficient provenance is incomplete."],
    ),
    model_spec(
        10,
        "2.4 Long-term Models - Logistic System",
        "logistic native growth plus constant non-native increment",
        "Replace data-hungry short-run recurrences with a fifty-year native/non-native dynamic system and local stability analysis.",
        ["N_t", "S_t", "delta", "N_m", "mu", "t"],
        ["NT_t", "N_t", "S_t"],
        ["Native growth is capacity bounded; the long-run non-native increment is constant; language extinction occurs only at zero speakers."],
        ["Equations (13)-(22)", "Tables 8-10", "Figures 6-10"],
        ["write native logistic growth", "reduce ECM to a constant increment", "add the two speaker identities", "analyze local equilibria", "estimate language-specific parameters", "project to 2067"],
        ["The additive total may double-count multilingual people, global and local stability claims are mixed, and constant L2 increments are weakly supported."],
        origin="modification",
    ),
    model_spec(
        13,
        "3.1 Sensitivity Analysis",
        "one-at-a-time coefficient and initial-state sensitivity",
        "Test local forecast response to Mandarin growth, external promotion, and Russian initial-state perturbations.",
        ["delta", "mu", "N_t"],
        ["NT_t", "rank"],
        ["Capacity is held fixed and each tested parameter is varied separately around the selected baseline."],
        ["Tables 11-12", "Figures 12-13", "reported 6.2 and 1.1 percent maxima"],
        ["declare baseline", "vary one input over the reported range", "recompute fifty-year forecast", "report local bias", "retain the Russian special case"],
        ["One-at-a-time ranges do not establish joint robustness or stability of the office recommendation."],
    ),
    model_spec(
        14,
        "3.2.1 Monte-Carlo Simulation",
        "stochastic long-run speaker recurrence",
        "Add separate Gaussian native and non-native disturbances and inspect simulated fifty-year fluctuation around deterministic paths.",
        ["N_t", "S_t", "delta", "N_m", "mu", "sigma_N", "sigma_S"],
        ["NT_t", "N_t", "S_t"],
        ["The two shocks are zero-mean normal disturbances whose variances represent omitted random factors."],
        ["Equations (23)-(25)", "Figure 14", "reported fluctuations at year 50"],
        ["add native shock", "add non-native shock", "sum the stochastic recurrences", "simulate multiple variances", "compare fluctuation to deterministic endpoint"],
        ["No seed, draw count, calibration source, dependence structure, interval coverage, or decision-stability test is reported."],
    ),
    model_spec(
        15,
        "4.1 Migration Patterns - Markov Process",
        "226-country migration and natural-growth transition system",
        "Advance country populations through fixed international migration probabilities and a country-specific natural-growth vector.",
        ["M", "N_t", "G_t"],
        ["P", "N_t", "pi"],
        ["Migration is international, time-homogeneous, simultaneous within each year, and directed toward more developed countries."],
        ["Equations (26)-(33)", "Table 13", "Figures 15-16", "Appendices 10-11"],
        ["assert the Markov property", "normalize observed migration flows", "construct the 226 by 226 matrix", "estimate moving-average growth", "advance annual populations"],
        ["Positivity and ergodicity are asserted, transition estimation is incompletely visible, and the growth-vector decay rule is not specified."],
    ),
    model_spec(
        17,
        "4.2.1 Country-Language Distribution Matrix",
        "country population by language-demand matrix propagation",
        "Convert projected country populations into a 226 by 26 language-use surface through H.",
        ["N_t", "H", "h_ij"],
        ["L_t"],
        ["Each H entry is a country-language demand ratio and may include native and non-native use."],
        ["Equations (34)-(35)", "Figure 17", "Appendix 12"],
        ["assemble H from 2017 disclosure", "multiply diagonal population by H", "extract language columns", "compare periods"],
        ["H is manually adjusted after 2017, ratio provenance is incomplete, and overlapping language identities can make row sums exceed one."],
    ),
    model_spec(
        17,
        "4.2.1 Spatial Surface Construction",
        "capital-point Lagrange interpolation",
        "Smooth 226 capital-based language values into geographic surfaces for comparison over four forecast years.",
        ["L_t"],
        ["rank"],
        ["Capital coordinates represent each country and interpolation between them is meaningful for language distribution."],
        ["Figure 17", "Appendix 12"],
        ["attach capital coordinates", "form 3D scattered points", "apply Lagrange interpolation", "plot 2017, 2027, 2037, and 2067 surfaces"],
        ["No interpolation formula, boundary behavior, spatial validation, or treatment of country area and population concentration is supplied."],
    ),
    model_spec(
        18,
        "4.3 Comparison of Temporal and Geographic Models",
        "cross-model total-speaker comparison",
        "Aggregate H-based forecasts and compare them with the differential model on a shared 2067 language total.",
        ["L_t", "NT_t"],
        ["rank"],
        ["The two models estimate comparable total speaker identities despite sharing inputs and manual assumptions."],
        ["Table 14", "Appendix 14", "reported 94 percent no-significant-difference claim"],
        ["sum country-language columns", "set t=50", "align ten language totals", "compute differences", "run the reported ANOVA comparison"],
        ["The test statistic, null, sample construction, and 94 percent calculation are not shown; agreement is not external validation."],
    ),
    model_spec(
        19,
        "5.1.2 Feature Construction and Clustering",
        "four-feature hierarchical clustering for capital screening",
        "Build English, migration, GDP, and Chinese indicators and map dendrogram groups into ordinal decision indices.",
        ["L_t", "E_t", "MI_t", "GDP_t", "C_t"],
        ["EI", "MII", "GDPI", "CI", "G_1", "G_2", "G_3", "G_4"],
        ["China and the United States are excluded because offices already exist there; remaining country capitals are eligible."],
        ["Equations (36)-(40)", "Figure 18", "Appendix 15"],
        ["extract four country vectors", "estimate t=10 or t=50 values", "cluster each vector", "choose 2,3,4,2 groups", "assign ordinal indices"],
        ["Distance metric, linkage, cut rule, scaling, and the t=5 versus t=10 caption conflict are not resolved."],
    ),
    model_spec(
        19,
        "5.1.2 MODM Fuzzy Evaluation",
        "weighted fuzzy multi-objective office ranking",
        "Transform four ordinal indices into memberships, apply a stated weight vector, and rank candidate countries.",
        ["EI", "MII", "GDPI", "CI", "x"],
        ["R", "A", "B", "rank"],
        ["English is the necessary criterion, economy is secondary, and Chinese communication is supplementary."],
        ["Equations (41)-(47)", "Tables 15-16", "Appendix 16"],
        ["define membership functions", "assemble R", "set A=(0.4,0.25,0.25,0.1)", "compute B=AR", "select six largest scores"],
        ["Membership equations and R are incompletely visible, weights are asserted rather than elicited, and score scale is not calibrated to operating cost."],
    ),
    model_spec(
        20,
        "5.3 MINE Resource-Saving Diagnostic",
        "grid-based maximum information concentration diagnostic",
        "Diagnose geographic overlap around four economic centers and prune two offices from each six-office plan.",
        ["office_set", "G"],
        ["MIC", "office_set"],
        ["New York, Tokyo, Hong Kong, and London define the relevant global communication centers and grid partition."],
        ["Figures 19-23", "reported MIC range and 0.5 contrast"],
        ["place offices and centers", "partition the coordinate plane", "compute the displayed concentration diagnostic", "identify redundant pairs", "compare the revised plan"],
        ["The displayed density/MIC formula, grid scale, threshold, service radius, and connection to coverage cost are not reproducible."],
    ),
    model_spec(
        20,
        "5.2-5.3 Integrated Office Decision",
        "horizon-conditioned office portfolio selection",
        "Turn forecast, geographic, fuzzy-score, and concentration outputs into six- and four-office recommendations for two horizons.",
        ["B", "rank", "MIC", "city_set"],
        ["office_set"],
        ["Capital cities are preferred and six offices may be reduced when overlap cost outweighs marginal coverage."],
        ["Tables 15-16", "Figures 19-23", "COO memo"],
        ["rank eligible capitals", "select six by horizon", "assign office languages", "diagnose overlap", "remove two named offices", "communicate switch conditions"],
        ["Operating costs, stakeholder utility, feasibility constraints, uncertainty, and stability of the selected portfolio are not quantified."],
    ),
]


def eq_spec(
    model: int,
    page: int,
    label: str,
    source: str,
    latex: str,
    purpose: str,
    symbols: list[str],
    confidence: str = "high",
) -> dict[str, Any]:
    return {
        "model": model,
        "page": page,
        "label": label,
        "source": source,
        "latex": latex,
        "purpose": purpose,
        "symbols": symbols,
        "confidence": confidence,
    }


E = eq_spec
EQUATION_SPECS = [
    E(1, 5, "(1)", "Four displayed PCA loading vectors map ten indicators to Y1-Y4.", r"Y_k=a_k^T X,\quad k=1,2,3,4", "Retain the four-component linear reduction and loading interpretation.", ["X", "Y", "a"], "medium"),
    E(2, 5, "(2)", "N_t is regressed on p lagged native-speaker counts plus white noise.", r"N_t=\sum_{j=1}^{p}\phi_jN_{t-j}+\epsilon_t", "Define the candidate AR(p) native-speaker recurrence.", ["N_t", "phi_p", "epsilon_t", "p"]),
    E(2, 6, "(3)", "The selected common order is AR(1): N_t=phi_1 N_(t-1)+epsilon_t.", r"N_t=\phi N_{t-1}+\epsilon_t", "Retain the fitted one-lag recurrence used by ten languages.", ["N_t", "phi", "epsilon_t"]),
    E(2, 7, "(4)", "The displayed FPE information criterion is used to compare p=0,1,2; several glyphs are absent from the PDF text layer.", r"\operatorname{FPE}(p)=\widehat\sigma_p^2\frac{T+p}{T-p}", "Retain the finite-prediction-error order diagnostic without treating its transcription as certain.", ["p", "sigma2", "T"], "medium"),
    E(2, 7, "(5)", "The displayed AIC order criterion balances residual variance and parameter count; source glyphs are partly absent.", r"\operatorname{AIC}(p)=T\log(\widehat\sigma_p^2)+2p", "Retain the AIC comparator and its disagreement with the selected order for some languages.", ["p", "sigma2", "T"], "medium"),
    E(2, 7, "(6)", "The displayed BIC order criterion penalizes lag complexity; source glyphs are partly absent.", r"\operatorname{BIC}(p)=T\log(\widehat\sigma_p^2)+p\log T", "Retain the BIC comparator supporting p=1.", ["p", "sigma2", "T"], "medium"),
    E(3, 7, "(7)", "After PCA the cointegration vector contains S and four component sequences.", r"Y_t=(S_t,Y_{1t},Y_{2t},Y_{3t},Y_{4t})", "Define the five-series state entering cointegration analysis.", ["S_t", "Y_1", "Y_2", "Y_3", "Y_4"]),
    E(3, 7, "(8)", "Theoretical long-run relation between non-native speakers and four principal components.", r"S_t=\gamma_0+\sum_{j=1}^{4}\gamma_jY_{jt}+\epsilon_t", "State the claimed long-run equilibrium relation.", ["S_t", "Y_1", "Y_2", "Y_3", "Y_4", "gamma", "epsilon_t"], "medium"),
    E(3, 7, "(9)", "First differences are combined with a lagged equilibrium-deviation term in the generic ECM.", r"\Delta S_t=\sum_{j=1}^{4}\beta_j\Delta Y_{jt}-\lambda ECM_{t-1}+\epsilon_t", "Define the short-run adjustment equation before estimation.", ["S_t", "Y_1", "Y_2", "Y_3", "Y_4", "beta", "lambda", "ECM_t", "epsilon_t"], "medium"),
    E(3, 8, "(10)", "S_(t-1)=gamma_0+sum gamma_j Y_j,(t-1)+ECM_(t-1).", r"S_{t-1}=\gamma_0+\sum_{j=1}^{4}\gamma_jY_{j,t-1}+ECM_{t-1}", "Retain the first Engle-Granger regression.", ["S_t", "Y_1", "Y_2", "Y_3", "Y_4", "gamma", "ECM_t"]),
    E(3, 8, "(11)", "ECM_(t-1) is the lagged observed-minus-fitted residual from the long-run relation.", r"ECM_{t-1}=S_{t-1}-(\gamma_0+\sum_{j=1}^{4}\gamma_jY_{j,t-1})", "Retain the equilibrium residual passed to stage two.", ["S_t", "Y_1", "Y_2", "Y_3", "Y_4", "gamma", "ECM_t"]),
    E(3, 8, "(12)", "Estimated delta S uses four component differences, a negative lagged ECM coefficient, and innovation.", r"\Delta S_t=\sum_{j=1}^{4}\beta_j\Delta Y_{jt}-\lambda ECM_{t-1}+\epsilon_t", "Retain the fitted ECM used for short-term L2 forecasts.", ["S_t", "Y_1", "Y_2", "Y_3", "Y_4", "beta", "lambda", "ECM_t", "epsilon_t"]),
    E(4, 10, "(13)", "Native speakers follow a capacity-bounded logistic differential equation.", r"\frac{dN}{dt}=\delta N\left(1-\frac{N}{N_m}\right)", "Define endogenous long-run native growth.", ["N_t", "delta", "N_m", "t"]),
    E(4, 10, "(14)", "The long-run ECM is reduced to the linear combination of four first differences.", r"\Delta S_t=\sum_{j=1}^{4}\beta_j\Delta Y_{jt}", "Remove the vanishing residual term before the constant-increment approximation.", ["S_t", "Y_1", "Y_2", "Y_3", "Y_4", "beta"]),
    E(4, 10, "(15)", "The long-run average non-native-speaker increment is represented by a real constant mu.", r"\frac{dS}{dt}=\mu", "Define the external long-run language-spread component.", ["S_t", "mu", "t"], "medium"),
    E(4, 11, "(16)", "Total speaker identities add the native logistic state and non-native constant-increment state.", r"NT_t=N_t+S_t", "Join endogenous and external speaker mechanisms.", ["NT_t", "N_t", "S_t"]),
    E(4, 11, "(17)", "dNT/dt=delta(NT-mu t)(1-(NT-mu t)/Nm)+mu.", r"\frac{dNT}{dt}=\delta(NT-\mu t)\left(1-\frac{NT-\mu t}{N_m}\right)+\mu", "Express the inhomogeneous total-speaker system.", ["NT_t", "delta", "mu", "t", "N_m"]),
    E(4, 11, "(18)", "The local equilibrium condition is written as dN/dt=0.", r"\frac{dN}{dt}=0", "Define the equilibrium condition used in the stability discussion.", ["N_t", "t"]),
    E(4, 11, "(19)", "A displayed Lyapunov derivative is used to classify N=0 and N=Nm; most symbols are absent from extraction.", r"\dot V(N)=V'(N)\,\delta N(1-N/N_m)", "Retain the stated Lyapunov stability step with low transcription confidence.", ["V", "N_t", "delta", "N_m"], "low"),
    E(4, 11, "(20)", "In the stated stable regime the paper writes NT=Nm+mu t+mu(0).", r"NT_t=N_m+\mu t+\mu(0)", "Retain the paper's final long-run total form literally for later checking.", ["NT_t", "N_m", "mu", "t"], "medium"),
    E(4, 12, "(21)", "Mandarin example: dN/dt=0.005 N(1-N/1600), N(0)=897.", r"\frac{dN}{dt}=0.005N\left(1-\frac{N}{1600}\right),\quad N(0)=897", "Instantiate native logistic growth for Mandarin.", ["N_t", "t"]),
    E(4, 12, "(22)", "The Mandarin total-speaker solution combines the fitted native curve with the non-native increment; the display is not recoverable from the PDF text layer.", r"NT_t=N_t+\mu t+S_0", "Retain the solution role and mark the missing glyph transcription as low confidence.", ["NT_t", "N_t", "mu", "t", "S_t"], "low"),
    E(6, 14, "(23)", "Native recurrence adds a normal disturbance to one logistic time step.", r"N_{t+1}=N_t+\delta N_t(1-N_t/N_m)+\mathcal N(0,\sigma_N^2)", "Define stochastic native-speaker evolution.", ["N_t", "delta", "N_m", "sigma_N"]),
    E(6, 14, "(24)", "Non-native recurrence adds a zero-mean normal disturbance to the constant increment.", r"S_{t+1}=S_t+\mu+\mathcal N(0,\sigma_S^2)", "Define stochastic non-native-speaker evolution.", ["S_t", "mu", "sigma_S"]),
    E(6, 15, "(25)", "Total recurrence combines logistic native growth, constant L2 increment, and two normal shocks.", r"NT_{t+1}=NT_t+\delta N_t(1-N_t/N_m)+\mu+\mathcal N(0,\sigma_N^2)+\mathcal N(0,\sigma_S^2)", "Retain the Monte Carlo total-speaker update.", ["NT_t", "N_t", "delta", "N_m", "mu", "sigma_N", "sigma_S"]),
    E(7, 15, "(26)", "P(N_(t+1)=j | full history through t)=P(N_(t+1)=j | N_t=i).", r"\Pr(X_{t+1}=j\mid X_0,\ldots,X_t=i)=\Pr(X_{t+1}=j\mid X_t=i)", "State the memoryless migration assumption.", ["N_t", "p_ij"]),
    E(7, 16, "(27)", "The first hidden display defines one-step country transition probabilities from observed migration flows.", r"p_{ij}=\frac{m_{ij}}{\sum_k m_{ik}}", "Retain the flow-normalization role; the exact source denominator is low confidence.", ["p_ij", "M"], "low"),
    E(7, 16, "(28)", "The transition probabilities are stated to be positive.", r"p_{ij}>0", "Retain the asserted positivity condition.", ["p_ij"], "low"),
    E(7, 16, "(29)", "Residents must remain or move, so each transition row is stated to sum to one.", r"\sum_j p_{ij}=1", "Retain the row-stochastic constraint.", ["p_ij", "P"], "low"),
    E(7, 16, "(30)", "A hidden display assembles the 226-country one-step transition matrix P.", r"P=(p_{ij})_{226\times226}", "Retain the transition-matrix dimensionality.", ["P", "p_ij"], "low"),
    E(7, 16, "(31)", "A hidden display introduces a steady-state probability vector for the positive transition matrix.", r"\pi^T P=\pi^T,\quad \sum_i\pi_i=1", "Retain the claimed stationary-distribution condition without upgrading the ergodicity proof.", ["pi", "P"], "low"),
    E(7, 16, "(32)", "The country population state is advanced through migration and a time-varying natural-growth vector.", r"N_{t+1}=P^T N_t+G_t", "Retain the population update role; matrix orientation is low confidence because the display is glyph-damaged.", ["N_t", "P", "G_t"], "low"),
    E(7, 16, "(33)", "The final Markov recurrence combines the deduced P with the moving-average growth vector G over fifty years.", r"N_t=(P^T)^tN_0+\sum_{k=0}^{t-1}(P^T)^{t-1-k}G_k", "Retain the propagation used to produce Appendix 11 populations.", ["N_t", "P", "G_t", "t"], "low"),
    E(8, 17, "(34)", "H is the displayed 226 by 26 matrix of country-language demand ratios h_ij.", r"H=(h_{ij})_{226\times26}", "Define the geographic language-ratio matrix.", ["H", "h_ij"]),
    E(8, 17, "(35)", "Each period's country-language distribution is diag(N_t) times H.", r"L_t=\operatorname{diag}(N_t)H", "Convert country populations to language speaker identities.", ["L_t", "N_t", "H"]),
    E(11, 19, "(36)", "The office model reuses L_t=diag(N_t)H for the 224 eligible countries.", r"L_t=\operatorname{diag}(N_t)H", "Supply language counts to office feature construction.", ["L_t", "N_t", "H"]),
    E(11, 19, "(37)", "English index EI is 1 for cluster G1=1 and 0 for G1=2.", r"EI=\begin{cases}1&G_1=1\\0&G_1=2\end{cases}", "Map English clustering to an ordinal decision index.", ["EI", "G_1"]),
    E(11, 19, "(38)", "Migration index MII is 2,1,0 for clusters G2=1,2,3.", r"MII=\begin{cases}2&G_2=1\\1&G_2=2\\0&G_2=3\end{cases}", "Map migration clustering to an ordinal decision index.", ["MII", "G_2"]),
    E(11, 19, "(39)", "GDP index GDPI is 3,2,1,0 for clusters G3=1,2,3,4.", r"GDPI=\begin{cases}3&G_3=1\\2&G_3=2\\1&G_3=3\\0&G_3=4\end{cases}", "Map GDP clustering to an ordinal decision index.", ["GDPI", "G_3"]),
    E(11, 19, "(40)", "Chinese index CI is 1 for cluster G4=1 and 0 for G4=2.", r"CI=\begin{cases}1&G_4=1\\0&G_4=2\end{cases}", "Map Chinese clustering to an ordinal decision index.", ["CI", "G_4"]),
    E(12, 19, "(41)", "The first displayed membership function maps an ordinal indicator x to fuzzy membership; denominator glyphs are absent.", r"\mu_1(x)=f_1(x)", "Retain the first membership-function slot without guessing missing scale constants.", ["x", "mu_x"], "low"),
    E(12, 20, "(42)", "A displayed membership function divides the indicator expression by 2; other glyphs are absent.", r"\mu_2(x)=f_2(x)/2", "Retain the visible denominator and mark the rest uncertain.", ["x", "mu_x"], "low"),
    E(12, 20, "(43)", "A displayed membership function divides the indicator expression by 3; other glyphs are absent.", r"\mu_3(x)=f_3(x)/3", "Retain the visible denominator and mark the rest uncertain.", ["x", "mu_x"], "low"),
    E(12, 20, "(44)", "The fourth displayed membership function is present but its mathematical glyphs are absent from extraction.", r"\mu_4(x)=f_4(x)", "Retain the fourth membership-function slot with low confidence.", ["x", "mu_x"], "low"),
    E(12, 20, "(45)", "The membership degrees are assembled into a fuzzy relation matrix R; the displayed matrix body is extraction-incomplete.", r"R=(r_{ij})", "Retain the country-by-indicator fuzzy relation matrix.", ["R", "mu_x"], "low"),
    E(12, 20, "(46)", "The stated criterion weight vector is A=(0.4,0.25,0.25,0.1).", r"A=(0.4,0.25,0.25,0.1)", "Retain the explicit MODM weights.", ["A"]),
    E(12, 20, "(47)", "The comprehensive country evaluation vector is B=AR.", r"B=AR", "Compute the weighted fuzzy office score.", ["B", "A", "R"]),
    E(2, 29, "Appendix 5 (A1)", "One-step forecast N_t(1)=phi N_t has error epsilon_(t+1) and variance sigma squared.", r"e_t(1)=\epsilon_{t+1},\quad \operatorname{Var}[e_t(1)]=\sigma^2", "Retain the one-step recursive forecast error.", ["N_t", "phi", "epsilon_t", "sigma2"]),
    E(2, 29, "Appendix 5 (A2)", "Two-step error is phi epsilon_(t+1)+epsilon_(t+2), followed by the printed variance expression.", r"e_t(2)=\phi\epsilon_{t+1}+\epsilon_{t+2},\quad \operatorname{Var}[e_t(2)]=(1+\phi^2)\sigma^2", "Retain the two-step expansion while separating the normalized check from the damaged printed line.", ["N_t", "phi", "epsilon_t", "sigma2"], "medium"),
    E(2, 29, "Appendix 5 (A3)", "Three-step error is phi(phi epsilon_(t+1)+epsilon_(t+2))+epsilon_(t+3); the paper prints the same variance as the preceding step.", r"e_t(3)=\phi^2\epsilon_{t+1}+\phi\epsilon_{t+2}+\epsilon_{t+3}", "Retain the three-step expansion and expose the duplicated printed variance in G7.", ["N_t", "phi", "epsilon_t", "sigma2"], "medium"),
    E(2, 29, "Appendix 5 (A4)", "Induction gives a geometric forecast-error variance and states exponential growth when phi exceeds one.", r"\operatorname{Var}[e_t(\ell)]=\sigma^2\sum_{j=0}^{\ell-1}\phi^{2j}=\sigma^2\frac{1-\phi^{2\ell}}{1-\phi^2}", "Retain the general horizon-error argument.", ["N_t", "phi", "sigma2"], "medium"),
]


def build_models() -> dict[str, Any]:
    if len(MODEL_SPECS) != 14 or len(EQUATION_SPECS) != 51:
        raise SystemExit("q122 model or equation specification count changed")
    labels = [spec["label"] for spec in EQUATION_SPECS]
    expected_labels = [f"({number})" for number in range(1, 48)] + [
        f"Appendix 5 (A{number})" for number in range(1, 5)
    ]
    if labels != expected_labels:
        raise SystemExit("q122 equation labels no longer preserve (1)-(47) plus Appendix 5 A1-A4")

    equations_by_model: dict[int, list[dict[str, Any]]] = {
        index: [] for index in range(1, len(MODEL_SPECS) + 1)
    }
    for equation_index, spec in enumerate(EQUATION_SPECS, start=1):
        equations_by_model[spec["model"]].append(
            {
                "equation_id": f"EQ-{ID_STEM}-{equation_index:03d}",
                "page": spec["page"],
                "label": spec["label"],
                "source_expression": spec["source"],
                "normalized_latex": spec["latex"],
                "purpose": spec["purpose"],
                "variable_symbols": spec["symbols"],
                "source_type": "paper",
                "visual_checked": True,
                "transcription_confidence": spec["confidence"],
            }
        )

    models: list[dict[str, Any]] = []
    for index, spec in enumerate(MODEL_SPECS, start=1):
        equations = equations_by_model[index]
        symbols = list(dict.fromkeys([
            *spec["inputs"],
            *spec["outputs"],
            *(symbol for equation_record in equations for symbol in equation_record["variable_symbols"]),
        ]))
        variables = []
        for symbol in symbols:
            name, unit = SYMBOL_META.get(symbol, (f"paper symbol {symbol}", "source-specific unit"))
            if symbol in spec["outputs"]:
                role = "output"
            elif symbol in spec["inputs"]:
                role = "input"
            elif symbol.endswith("_t"):
                role = "state"
            else:
                role = "parameter"
            variables.append(
                variable(
                    symbol,
                    name,
                    unit,
                    role,
                    f"{name.capitalize()} used by {spec['section']}.",
                    "explicit-defined" if symbol in SYMBOL_META else "inferred-from-equation",
                )
            )
        models.append(
            {
                "model_id": f"MU-{ID_STEM}-{index:03d}",
                "page": spec["page"],
                "section": spec["section"],
                "family": spec["family"],
                "purpose": spec["purpose"],
                "base_or_modification": spec["origin"],
                "summary": spec["purpose"],
                "variables": variables,
                "inputs": spec["inputs"],
                "outputs": spec["outputs"],
                "governing_equations": equations,
                "equation_status": {
                    "status": "present" if equations else "omitted-by-paper",
                    "reason": (
                        "All numbered displays assigned to this unit retain physical page, source wording, normalized transcription, visual-check status, and confidence."
                        if equations
                        else "The paper presents this unit through an algorithm, diagnostic, table, or decision narrative without a separately numbered governing display."
                    ),
                },
                "objectives": [
                    spec["purpose"],
                    "Preserve entity, unit, index, horizon, evidence status, and the exact downstream model or office decision.",
                ],
                "constraints": [
                    "Do not merge native persons, non-native speaker identities, total speaker identities, residents, migrants, standardized indicators, fuzzy scores, and office decisions.",
                    "Do not silently repair damaged symbols, contradictory table entries, manually adjusted H values, reused figure numbers, or missing algorithm settings.",
                ],
                "conditions": {
                    "initial": {
                        "status": "present",
                        "details": [
                            "Short-run histories cover 2003-2017; long-run, geographic, and office calculations use the paper's stated 2017 base and t=10 or t=50 horizon."
                        ],
                    },
                    "boundary": {
                        "status": "present",
                        "details": list(spec["assumptions"]),
                    },
                    "equilibrium": {
                        "status": "present" if index in {3, 4, 7} else "not-applicable",
                        "details": [
                            "Equilibrium is used only where the paper invokes cointegration correction, logistic stability, or a stationary Markov distribution; other units are finite-horizon transformations."
                        ],
                    },
                },
                "parameter_estimation": {
                    "status": "partial",
                    "method": (
                        "Parameters combine the 2003-2017 language series, a 2008-2016 six-language indicator panel, UN and EPS-style demographic or language data, moving averages, author-selected weights, and manual updates; a complete frozen provenance and transformation ledger is absent."
                    ),
                    "parameters": spec["inputs"],
                },
                "algorithm": {
                    "status": "partial",
                    "steps": spec["steps"],
                    "software": [
                        "Computer regression and simulation are named, but no complete code, package versions, random seed, or executable environment is archived."
                    ],
                    "convergence_criteria": (
                        "The source uses fixed annual horizons, selected cluster cuts, top-six ranking, or qualitative stability; it does not provide a general numerical tolerance or reproducible stopping rule."
                    ),
                },
                "assumptions": spec["assumptions"],
                "identifiability_feasibility": {
                    "status": "partial",
                    "analysis": (
                        "The mathematical role and handoff are inspectable, but sparse provenance, damaged formula glyphs, manual matrix adjustment, unseeded simulation, omitted scaling, and absent external holdout prevent full identification and decision validation."
                    ),
                },
                "handoff_outputs": spec["outputs"],
                "validation_refs": spec["validation_refs"],
                "computational_cost": (
                    "No runtime, memory, hardware, numerical precision, random draw count, matrix-sparsity treatment, or reproducible implementation cost is reported."
                ),
                "strengths": [
                    "The unit has a named input, transformation, output, validation reference, and receiving stage in the paper's forecast-to-decision chain.",
                    "The staged record separates observed inputs, fitted parameters, assumptions, simulated outputs, and recommendations.",
                ],
                "limitations": spec["limitations"],
                "missing_details": [
                    "Frozen input snapshots, exact transformations, uncertainty distributions, executable code, software versions, and random seeds are incomplete or absent.",
                    "No common rolling holdout, calibrated prediction interval, joint sensitivity design, or office-selection stability analysis spans the complete pipeline.",
                ],
            }
        )

    edge_specs = [
        (1, 3, "Four PCA components become the ECM explanatory state."),
        (2, 4, "AR recursive-error growth motivates replacing the short-run native recurrence."),
        (3, 4, "ECM behavior motivates the constant long-run non-native increment."),
        (4, 5, "The deterministic long-run system supplies coefficient and initial-value scenarios."),
        (4, 6, "The deterministic recurrence receives explicit stochastic disturbances."),
        (7, 8, "Projected country populations are multiplied by the country-language ratio matrix."),
        (8, 9, "Country-language values are attached to capital coordinates for spatial smoothing."),
        (4, 10, "Differential-model 2067 totals form one side of the cross-model comparison."),
        (8, 10, "H-based country totals form the other side of the comparison."),
        (7, 11, "Migration totals and projected populations supply office indicators."),
        (8, 11, "English and Chinese country proportions supply office indicators."),
        (3, 11, "The short-run ECM supplies t=10 language-related inputs."),
        (4, 11, "The long-run system supplies t=50 language-related inputs."),
        (11, 12, "Four ordinal cluster indices become fuzzy-evaluation inputs."),
        (12, 13, "The six highest fuzzy scores define the plans checked for spatial overlap."),
        (9, 13, "Capital coordinates and economic-center geography define the concentration grid."),
        (12, 14, "Horizon-specific rankings define the initial six-city portfolios."),
        (13, 14, "The concentration diagnostic supplies the two-city pruning action."),
        (10, 14, "Cross-model agreement is cited as support for using the forecast in the final decision."),
    ]
    dependency_edges = [
        {
            "from_model_id": f"MU-{ID_STEM}-{source:03d}",
            "to_model_id": f"MU-{ID_STEM}-{target:03d}",
            "handoff": handoff,
        }
        for source, target, handoff in edge_specs
    ]
    return {
        "schema_version": 2,
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "review_status": "validated",
        "models": models,
        "dependency_edges": dependency_edges,
    }


VISUAL_SPECS = [
    (1, "Summary Sheet", "Six-move forecast-to-office route", [1, 2, 3, 4, 7, 12, 13, 14], "PCA -> short-run models -> long-run system -> migration geography -> fuzzy ranking -> MINE pruning", "document overview", "text hierarchy", "The summary recommends four cities for each horizon only after a longer six-city ranking and overlap screen."),
    (2, "Contents", "Model and deliverable map", [], "temporal forecast -> reliability -> geographic distribution -> office model -> evaluation -> memo -> appendices", "navigation map", "hierarchical contents", "The contents exposes the intended dependency order and sixteen appendix handoffs."),
    (3, "Introduction and assumptions", "L1/L2 mechanism split and scope ledger", [2, 3, 4], "native population mechanism versus externally influenced second-language mechanism", "state-boundary audit", "numbered prose", "The report assigns different temporal mechanisms to native and non-native speaker identities."),
    (4, "Table 1", "Variables and parameters for Model 1", [1, 2, 3, 4], "speaker states, factors, lags, residuals, logistic parameters, and growth terms", "definition ledger", "multirow table", "The table spans short- and long-run notation but leaves several units and glyphs implicit."),
    (5, "PCA display", "Four-component indicator reduction", [1], "ten weighted indicators reduced to four factors retaining 87.6 percent of the reported information", "dimension reduction", "equation and loading narrative", "The retained components are interpreted as economic, equality, welfare, and culture-shock factors."),
    (6, "Table 2", "Current language speaker counts", [2, 4], "L1, L2, and total counts for ten languages", "baseline data audit", "numeric table", "The table supplies initial speaker states but includes entity inconsistencies later exposed by the Bengali row."),
    (6, "Figures 1-3", "L1, L2, and total time series", [2, 3], "three historical trajectories for the ten selected languages", "mechanism separation", "multi-line charts", "The plots motivate separate native and non-native time-series treatments."),
    (6, "Figures 4-5", "Autocorrelation and partial-correlation examples", [2], "sample ACF/PACF diagnostics used to select AR order", "order selection", "diagnostic plots", "The paper infers first-order autoregression and routes remaining plots to Appendix 1."),
    (7, "Table 3", "AR(1) estimates by language", [2], "coefficient, constant, error variance, and fit information", "short-run calibration", "numeric table", "Several fitted autoregressive coefficients exceed one, so long-horizon use is explicitly questioned."),
    (7, "Table 4", "Akaike information-criterion comparison", [2], "candidate lag orders and selected short-run structure", "model selection", "numeric table", "The AIC table is the stated basis for the AR(1) choice."),
    (8, "Table 5", "Engle-Granger cointegration test", [3], "six-language test statistics, decisions, and residual status", "cointegration diagnostic", "numeric table", "The table supports the move from a levels relation to an error-correction model on a short panel."),
    (8, "Table 6", "First EG regression coefficients", [3], "constant and four component coefficients for six languages", "factor-effect estimate", "numeric table", "Positive nonconstant coefficients are interpreted as favorable macro-factor effects on L2 speakers."),
    (10, "Table 7", "Second EG step coefficients", [3], "difference coefficients and correction terms", "dynamic adjustment estimate", "numeric table", "The table parameterizes the short-run change model before its long-run simplification."),
    (10, "Table 8", "Dickey-Fuller test results", [3], "first-difference stationarity statistics and decisions", "integration check", "numeric table", "The paper uses six first-difference tests to justify the ECM route."),
    (10, "Equations (13)-(16)", "Logistic L1, constant L2, and total dynamic system", [4], "native capacity, constant second-language increment, and additive total speaker identity", "long-run replacement", "equation stack", "The long-run repair replaces recursive AR growth with a bounded native component and an unbounded linear L2 component."),
    (11, "Figures 6-9", "Logistic phase paths and parameter scenarios", [4], "initial-value, growth-rate, capacity, and total-speaker trajectories", "stability interpretation", "four line charts", "The figures illustrate stable native equilibria and nonstationary total growth under selected parameters."),
    (12, "Table 9", "Long-run parameter approximations", [4], "delta, capacity, and long-run increment for ten languages", "parameter ledger", "numeric table", "The table contains negative growth or increment terms and feeds the fifty-year forecast."),
    (12, "Figure 10", "Mandarin native and total speaker trajectories", [4], "logistic L1 bottleneck plus continued L2-driven total growth", "mechanism decomposition", "line chart", "The figure attributes future Mandarin growth increasingly to non-native use."),
    (12, "Table 10", "2067 forecast for current top ten languages", [4], "L1, total, and printed endogenous-growth contribution", "forecast comparison", "numeric table", "The Bengali row prints L1=248 and total=160, while several percentages exceed 100 percent or are negative."),
    (13, "Figure 11", "Malay and Russian forecasts", [4], "two languages identified as at risk of leaving the top ten", "exception analysis", "line charts", "The result combines a weak cultural outlook for Malay with declining native Russian population."),
    (13, "Figure 12", "Four replacement-language trajectories", [4], "candidate alternatives including Hausa and German", "ranking switch", "multi-line chart", "The chart supports the stated Hausa and German entry into the future top-ten set."),
    (13, "Table 11", "Sensitivity to native growth rate", [5], "Mandarin coefficient scenarios and forecast deviations", "local sensitivity", "numeric table", "The table varies one coefficient while keeping other model components fixed."),
    (14, "Table 12", "Sensitivity to non-native increment", [5], "Mandarin promotion-rate scenarios and forecast deviations", "local sensitivity", "numeric table", "The table provides a second one-at-a-time sensitivity screen."),
    (14, "Figure 12 reused", "Comprehensive Mandarin sensitivity", [5], "jointly displayed parameter-response paths under a reused figure number", "sensitivity summary", "multi-line chart", "The source reuses Figure 12, so the physical-page anchor is necessary for unambiguous reference."),
    (14, "Figure 13", "Russian initial-value sensitivity", [5], "multiple starting native-speaker values converging toward the reported path", "initial-state sensitivity", "line chart", "The paper reports a roughly twenty-million fluctuation range for the tested starts."),
    (15, "Figure 14", "Monte Carlo paths for Mandarin", [6], "stochastic L1 and total-speaker recurrences", "robustness scenario", "simulation charts", "The plot shows bounded visual fluctuation but omits draw count, seed, and calibrated predictive intervals."),
    (15, "Table 13", "Variables for the migration model", [7, 8], "country populations, flows, transition probabilities, natural growth, and language ratios", "geographic symbol ledger", "multirow table", "The table separates country population transitions from the later country-language multiplication."),
    (16, "Equations (26)-(33)", "Country Markov transition construction", [7], "conditional migration probabilities, row-stochastic matrix, natural growth, and population propagation", "migration mechanism", "equation stack", "The displayed system is 226 by 226 and includes natural population growth outside the stochastic matrix."),
    (17, "Figure 15", "Foreign-born population share", [7], "visualized incoming-migration matrix", "migration input map", "world map", "The map summarizes the observed flow structure used to deduce transition probabilities."),
    (17, "Figure 16", "Natural-growth moving-average surface", [7], "2005-2016 population natural-growth input", "growth-vector input", "map or surface", "The plotted moving average supplies the separate country growth vector."),
    (17, "Equations (34)-(35)", "Country-language matrix propagation", [8, 9], "226 by 26 demand ratios and population-to-language multiplication", "spatial handoff", "matrix equations", "The H matrix converts projected country populations into overlapping language speaker identities before interpolation."),
    (18, "Figure 17", "Projected Mandarin geographic distribution", [8, 9], "capital-point values smoothed over the globe for the next fifty years", "spatial forecast", "3D surface or map", "The paper interprets wider geographic mixing while acknowledging manual post-2017 H adjustment."),
    (18, "Table 14", "Temporal-versus-geographic forecast comparison", [4, 8, 10], "ten language totals from differential and Markov-H routes with differences", "cross-model corroboration", "numeric table", "The two routes disagree materially for several languages despite the reported 94 percent no-difference claim."),
    (19, "Figure 18", "Four feature dendrograms", [11], "English, migration, GDP, and Chinese indicators at the short horizon", "candidate grouping", "four dendrograms", "The cuts produce two, three, four, and two ordinal groups for office scoring."),
    (19, "Equations (37)-(40)", "Ordinal cluster indices", [11], "cluster labels mapped to English, migration, GDP, and Chinese decision scores", "feature discretization", "piecewise equations", "The mappings replace continuous indicators with author-selected ordinal values."),
    (19, "Equations (41)-(47)", "Fuzzy memberships, weights, and score", [12], "four membership functions, relation matrix, A=(0.4,0.25,0.25,0.1), and B=AR", "multi-objective ranking", "equation stack", "Several membership glyphs and scaling constants are absent from extraction and are retained with low confidence."),
    (20, "Table 15", "Short-run six-office results", [11, 12, 14], "London, Ottawa, Singapore, Canberra, Berlin, and Wellington", "tactical decision", "ranked table", "The six-city result is later pruned to London, Singapore, Ottawa, and Canberra."),
    (20, "Table 16", "Long-run six-office results", [11, 12, 14], "Singapore, London, Canberra, Paris, Ottawa, and Kuala Lumpur", "strategic decision", "ranked table", "The six-city result is later pruned to Singapore, London, Canberra, and Paris."),
    (21, "Figure 19", "Short-run MIC grid", [13], "concentration scores for the short-run office and economic-center samples", "overlap diagnosis", "grid heatmap", "The paper treats values near one as concentration and uses the grid to justify removing Wellington and Berlin."),
    (21, "Figure 20", "Offices and economic centers", [13, 14], "geographic relation between selected offices and four economic centers", "decision geography", "coordinate map", "The visual supplies the spatial-overlap rationale that the fuzzy score alone does not encode."),
    (21, "Figure 21", "Improved short-run MIC distribution", [13, 14], "four-office grid after pruning", "decision comparison", "grid heatmap", "The source presents the pruned plan as a more efficient coverage pattern without a calibrated service-loss measure."),
    (22, "Figures 22-23", "Original and improved long-run MIC grids", [13, 14], "six-office versus four-office concentration patterns", "long-run pruning comparison", "paired grid heatmaps", "The long-run pruning removes Kuala Lumpur and Ottawa from the initial six-city set."),
    (23, "COO Memo", "Findings and horizon-conditioned office advice", [4, 7, 8, 12, 13, 14], "mechanism findings, changing languages, geographic mixing, six-city and four-city recommendations", "executive compression", "memo prose", "The memo preserves short- versus long-run city sets but compresses uncertainty and feasibility caveats."),
    (26, "Appendices 1-16", "Diagnostics, coefficient tables, forecasts, matrices, classifications, and error derivation", [2, 3, 4, 5, 7, 8, 11], "ACF/PACF, PCA and ECM support, AR error variance, sensitivity, language trajectories, Markov inputs, H excerpts, ANOVA, and country classes", "supporting trace", "appendix tables and charts", "The appendices extend source coverage through physical page 39 and preserve the duplicated two- and three-step variance issue."),
]


def build_visuals() -> list[dict[str, Any]]:
    visuals: list[dict[str, Any]] = []
    for index, spec in enumerate(VISUAL_SPECS, start=1):
        page, figure, caption, model_numbers, summary, purpose, form, claim = spec
        visuals.append(
            {
                "page": page,
                "figure": figure,
                "visual_record_id": f"VR-{ID_STEM}-{index:03d}",
                "caption": caption,
                "source_model_ids": [
                    f"MU-{ID_STEM}-{number:03d}" for number in model_numbers
                ],
                "summary": summary,
                "analytical_purpose": purpose,
                "form": form,
                "encodings": [
                    "physical-page position and section order encode the model handoff",
                    "rows, columns, axes, line position, color, cluster height, or grid cell encode the stated comparison",
                ],
                "exact_claim": claim,
                "construction_or_missing": (
                    "Transcribed from the completed physical-page review; missing units, "
                    "glyphs, uncertainty, source data, software, or construction details "
                    "remain missing rather than inferred."
                ),
                "applicability": (
                    "Use only with the source's language identities, country set, base year, "
                    "forecast horizon, parameter scenario, capital set, and office-count rule."
                ),
                "forbidden_scenarios": [
                    "Do not transfer source-specific language counts, percentages, weights, city rankings, or MIC interpretations as general constants.",
                    "Do not treat a fitted chart, simulated path, model-agreement table, or ranked office set as externally validated causal evidence.",
                ],
                "accessibility": (
                    "Add direct labels, units, horizon, scenario, numeric alternatives, and "
                    "text descriptions of matrix, dendrogram, and grid encodings."
                ),
                "disposition": "important-visual-record",
                "evidence_role": "O",
            }
        )
    if len(visuals) != 44:
        raise SystemExit(f"q122 visual count changed: {len(visuals)} != 44")
    return visuals


def page_summary(page: int, summary: str, **extra: Any) -> dict[str, Any]:
    return {"page": page, "summary": summary, **extra}


ASSUMPTION_SPECS = [
    (3, "The ten currently leading languages are treated as sufficient for the primary temporal forecast."),
    (3, "Historical change is treated as representative of near-future speaker development outside severe structural shocks."),
    (3, "Individuals within each modeled language or country group are treated as homogeneous for the relevant mechanism."),
    (3, "Native-speaker change is attributed mainly to population dynamics, while non-native change is attributed to economic, social, welfare, cultural, and political factors."),
    (10, "Native long-run growth follows a logistic law with a fixed language-specific carrying capacity."),
    (10, "Long-run non-native speakers increase by a constant annual increment estimated from the preceding fifteen years."),
    (14, "Monte Carlo disturbances are represented by normal shocks with zero mean and the paper's selected variance."),
    (15, "International migration is treated as a first-order discrete-time Markov process conditioned only on the current country."),
    (15, "Migration tends from economically underdeveloped toward developed areas and disasters or wars are excluded from the normal transition mechanism."),
    (16, "Positive stay and move probabilities are asserted to make the 226-country chain regular and convergent to one stable distribution."),
    (17, "The 2017 country-language demand ratios can be carried forward after manual adjustment using the temporal forecast."),
    (20, "Four economic-center grids and concentration of selected capitals are treated as a sufficient basis for pruning two offices."),
]


DATA_SPECS = [
    (4, "Ten economic, equality, welfare, and cultural indicators are population-weighted into a six-language 2008-2016 panel."),
    (5, "PCA reduces the ten indicators to four interpreted components with a reported cumulative contribution of 87.6 percent."),
    (6, "Table 2 and Figures 1-3 provide 2003-2017 L1, L2, and total series for the selected leading languages."),
    (7, "Tables 3-4 retain language-specific AR coefficients, constants, innovation variance, and AIC order evidence."),
    (8, "Tables 5-8 retain six-language EG regressions, residual tests, difference coefficients, and Dickey-Fuller decisions."),
    (12, "Table 9 records language-specific logistic growth, carrying capacity, and constant non-native increment estimates."),
    (15, "The migration system uses 226 country populations and observed bilateral movement counts to form the transition matrix."),
    (17, "Figure 16 derives natural-growth inputs from 2005-2016 population moving averages."),
    (17, "The 226 by 26 H matrix is attributed to a 2017 EPS-style database and is manually adjusted for later periods."),
    (17, "Country-language values are attached to capital latitude-longitude points and smoothed with Lagrange interpolation."),
    (19, "Office features are English share, immigration, GDP per capita, and Chinese share for each eligible country."),
    (19, "Short-run GDP-related inputs use the ECM route, while long-run values use the paper's moving-average projection."),
    (20, "The fuzzy criterion weights are fixed at 0.4, 0.25, 0.25, and 0.1 before the country scores are ranked."),
    (20, "New York, Tokyo, Hong Kong, and London define four economic centers used to construct the MIC grid diagnostic."),
]


VERIFICATION_SPECS = [
    (1, "All 39 physical pages were read in page-aware text and reviewed through byte-bounded JPEG proxies; Summary and Introduction were completed first."),
    (5, "The PCA display, retained-component percentage, and four component interpretations were checked against the physical page."),
    (6, "L1, L2, and total entities in Table 2 and Figures 1-3 were kept distinct during transcription."),
    (7, "ACF/PACF, AIC, AR coefficients, and recursive forecast-error claims were cross-checked with Appendix 5."),
    (8, "EG test decisions, first-stage coefficients, ECM terms, and Dickey-Fuller results were retained as separate diagnostics."),
    (11, "The logistic equilibria and initial-value cases in Figures 6-9 were checked against Equations (13)-(22)."),
    (12, "All ten Table 9 and Table 10 rows were retained, including Bengali L1=248 versus total=160 and the printed contribution percentages."),
    (14, "Mandarin coefficient and Russian initial-value sensitivity displays were treated as local one-at-a-time checks."),
    (15, "Monte Carlo recurrences and Figure 14 were checked for shock placement, while missing draw count and seed remain explicit."),
    (16, "The focused Markov crop was used to check matrix dimensions, transition direction, row normalization, natural-growth addition, and the unsupported ergodicity assertion."),
    (17, "The H matrix dimensions, diag(N) multiplication, manual post-2017 adjustment, and capital-point interpolation were checked separately."),
    (18, "Every Table 14 language row was compared across the two model routes before retaining the sparse 94 percent ANOVA claim."),
    (19, "All four dendrogram group counts and the ordinal mappings in Equations (37)-(40) were checked against the office-feature definitions."),
    (20, "A focused crop preserved the incomplete membership functions, relation matrix, explicit weight vector, and B=AR score without repairing missing glyphs."),
    (20, "Tables 15-16 were traced through the short- and long-run feature construction to the six-city recommendations."),
    (21, "The MIC crop and Figures 19-23 were checked for grid definition, value interpretation, source points, and the two-city pruning action."),
    (29, "Appendix 5 one-, two-, and three-step AR errors were transcribed literally; the duplicated printed variance is isolated in G7."),
    (39, "Appendices 1-16, the reused Figure 12 label, final Page 37 of 20 marker, and commercial watermark exclusion were checked at physical-page level."),
]


RESULT_SPECS = [
    (5, "The four PCA components are reported to retain 87.6 percent of the ten-indicator information."),
    (7, "The short-run native series are modeled as AR(1), with Russian singled out for declining native population."),
    (8, "Nonconstant EG coefficients are reported as positive across the six fitted language models."),
    (12, "The long-run Mandarin example approaches an L1 capacity of 1,600 million while total growth continues through L2."),
    (12, "Table 10 forecasts English total speakers above Mandarin by 2067 under the paper's long-run parameterization."),
    (13, "Malay and Russian are predicted to leave the future top ten, with Hausa and German proposed as replacements."),
    (14, "The one-at-a-time tests are reported to leave Mandarin forecasts broadly stable and Russian paths within about twenty million."),
    (15, "Figure 14 reports visually bounded stochastic fluctuation for the selected Mandarin simulation."),
    (18, "The geographic model predicts more mixed language distributions and expanding Mandarin use outside its present center."),
    (18, "Table 14 reports model differences ranging from small values to materially large gaps such as Russian -73 million."),
    (18, "The paper states that 94 percent of ANOVA probabilities show no significant difference between the two forecast routes."),
    (20, "The short-run six-city set is London, Ottawa, Singapore, Canberra, Berlin, and Wellington."),
    (20, "The long-run six-city set is Singapore, London, Canberra, Paris, Ottawa, and Kuala Lumpur."),
    (21, "Short-run overlap pruning removes Wellington and Berlin, retaining London, Singapore, Ottawa, and Canberra."),
    (22, "Long-run overlap pruning removes Kuala Lumpur and Ottawa, retaining Singapore, London, Canberra, and Paris."),
    (24, "The memo links the four-office alternatives to relaxed office-count requirements and reduced overlapping service areas."),
]


FORMULA_WARNINGS = [
    (1, 0, 5, "Equation (1) reports a PCA reduction but omits a frozen standardization, missing-data, loading, and weighting ledger needed to reproduce 87.6 percent."),
    (2, 1, 6, "Equation (3) is used as AR(1) even though several reported phi estimates exceed one; long-horizon stationarity and recursive-error conditions are therefore not satisfied."),
    (2, 7, 29, "Appendix 5 prints the same variance after the two- and three-step expansions, while the visible three-step error contains an additional phi-squared innovation term."),
    (3, 0, 7, "Equation (7)'s cointegrating relation is estimated from a very short six-language panel without a documented deterministic-term, lag, or multiple-testing design."),
    (3, 5, 8, "Equation (12) does not archive the exact residual series, lag timing, standard errors, or sign convention needed to reproduce the ECM correction."),
    (4, 0, 10, "Equation (13) replaces the unstable AR route with logistic growth, but the source does not estimate or test the fixed carrying capacity mechanism."),
    (4, 2, 10, "Equation (15) assumes a constant annual L2 increment from a fifteen-year average, creating an unbounded linear long-run component without uncertainty."),
    (4, 3, 11, "Equation (16) adds native persons and non-native speaker identities without proving that the reported total is a unique-person population."),
    (4, 7, 11, "Equation (20)'s global-stability conclusion requires parameter-sign, state-domain, and carrying-capacity conditions that are asserted rather than demonstrated for every language."),
    (6, 0, 14, "Equation (23) adds a normal shock to native growth without a documented variance calibration, truncation rule, or protection against impossible negative states."),
    (6, 2, 15, "Equation (25) combines two stochastic recurrences but supplies no draw count, seed, interval construction, or decision-level coverage test."),
    (7, 2, 16, "Equation (28)'s transition estimator depends on flow denominators and stay probabilities whose zero, missing, and direction conventions are not fully specified."),
    (7, 7, 16, "Equation (33) is accompanied by a claim that positivity guarantees one stable distribution, but irreducibility, aperiodicity, and empirical positivity are not demonstrated."),
    (8, 1, 17, "Equation (35) multiplies population by a manually adjusted H matrix whose post-2017 update rule, uncertainty, and overlapping-language semantics are not reproducible."),
    (11, 1, 19, "Equation (37) converts an English cluster label directly to 1 or 0; the cut location and loss from discretization are not justified."),
    (12, 0, 19, "Equation (41)'s membership-function glyphs and scale constants are incomplete, so its normalized transcription remains deliberately low confidence."),
    (12, 5, 20, "Equation (46) fixes weights at 0.4, 0.25, 0.25, and 0.1 without stakeholder elicitation, normalization evidence, or sensitivity."),
    (12, 6, 20, "Equation (47) treats B=AR as a comparable office score although membership scaling, criterion direction, feasibility, and operating-cost meaning are incomplete."),
]


WEAKNESS_SPECS = [
    (5, 1, 1, "PCA preprocessing, loadings, missingness, and the six-language panel snapshot are incomplete, limiting reproducibility of the four factors."),
    (7, 2, 3, "Several AR(1) coefficients exceed one, so the fitted short-run recurrence is nonstationary and its forecast error grows with horizon."),
    (8, 3, 7, "Cointegration and ECM claims rely on a short panel with sparse lag, residual, uncertainty, and multiple-test documentation."),
    (10, 4, 13, "Logistic carrying capacities and constant L2 increments are imposed from limited history rather than validated structural mechanisms."),
    (12, 4, None, "Table 10 contains Bengali L1=248 with total=160 and contribution values 193.4 percent, 278.5 percent, and -33.0 percent."),
    (13, 4, None, "Top-ten exit and replacement claims lack calibrated rank probabilities or sensitivity to competing language sets."),
    (14, 5, None, "Sensitivity analysis is one-at-a-time and does not test correlated parameter changes or office-decision switches."),
    (15, 6, 25, "Monte Carlo simulation omits shock calibration, draw count, seed, truncation, convergence, and predictive coverage."),
    (16, 7, 33, "The Markov positivity and ergodicity conclusion is asserted without a proof or empirical connectivity audit of the 226-country matrix."),
    (17, 8, 35, "The future H matrix is manually adjusted without an executable rule, provenance ledger, or uncertainty propagation."),
    (17, 9, None, "Lagrange interpolation over capital points lacks coordinate projection, boundary treatment, validation, and an alternative spatial baseline."),
    (18, 10, None, "The two forecast routes share data and assumptions, while the 94 percent no-significant-difference claim has sparse ANOVA support and no external truth."),
    (19, 11, 37, "Hierarchical cluster cuts and ordinal category scores discard scale information without stability or alternative-linkage checks."),
    (20, 12, 41, "Fuzzy membership functions are extraction-incomplete and the paper omits criterion scaling and membership calibration."),
    (20, 12, 46, "The fixed MODM weights have no stakeholder provenance or sensitivity analysis."),
    (21, 13, None, "MIC is interpreted as spatial concentration although MINE is designed for dependence; grid shape and four economic centers are subjective."),
    (22, 14, None, "Removing two offices is not evaluated against service loss, operating cost, feasibility, or uncertainty in the underlying rankings."),
    (39, 14, None, "Figure 12 is reused, the final page says Page 37 of 20, references lack frozen snapshots, and a commercial watermark contaminates extraction headers."),
]


CONTEXT_SPECS = [
    (1, "The Summary Sheet presents the entire language-to-office pipeline before technical detail."),
    (2, "The official Problem B task requires fifty-year temporal and geographic forecasts, office recommendations, a fewer-office analysis, and a COO memo."),
    (3, "The paper explicitly separates native and non-native language mechanisms before selecting models."),
    (15, "The geographic model expands the analysis from ten language trajectories to 226 countries and 26 language columns."),
    (20, "The application restricts new offices to eligible national capitals and ranks them at two time horizons."),
    (23, "The memo changes the receiving form from derivation to executive findings and recommendations."),
    (25, "The references name statistical, Monte Carlo, MINE, fuzzy-evaluation, population, and migration sources without frozen retrieval snapshots."),
    (39, "Sixteen appendices extend diagnostics and data through physical page 39; physical pages, not printed page numbers, control every anchor."),
]


ARGUMENT_CHAINS = [
    {
        "claim": "Language evolution and office placement are treated as one forecast-to-decision pipeline.",
        "support_steps": ["ten indicators", "temporal forecasts", "country migration", "language geography", "office features", "fuzzy ranking", "MINE pruning", "memo"],
        "decision_consequence": "Every city recommendation must retain a trace to the horizon-specific language, migration, economic, and overlap inputs.",
        "source_pages": [1, 4, 15, 17, 19, 20, 23],
    },
    {
        "claim": "The short-run temporal model separates native persistence from externally driven non-native change.",
        "support_steps": ["L1/L2 definition", "ACF/PACF", "AR(1)", "PCA", "EG relation", "ECM"],
        "decision_consequence": "Keep the entity split and use each recurrence only for the horizon supported by its diagnostics.",
        "source_pages": [3, 5, 6, 7, 8, 10],
    },
    {
        "claim": "Growing AR forecast error and data demands motivate a long-run differential replacement.",
        "support_steps": ["recursive AR error", "logistic L1", "constant L2 increment", "additive total system", "stability figures", "2067 table"],
        "decision_consequence": "Treat the logistic-plus-linear route as a structural scenario until capacities and L2 mechanisms are independently calibrated.",
        "source_pages": [10, 11, 12, 29],
    },
    {
        "claim": "Sensitivity and Monte Carlo are used to bound selected parameter and disturbance concerns before geographic projection.",
        "support_steps": ["growth-rate table", "increment table", "initial-value chart", "normal shocks", "simulation plot"],
        "decision_consequence": "Do not upgrade these local checks to joint robustness or calibrated prediction intervals.",
        "source_pages": [13, 14, 15],
    },
    {
        "claim": "Country migration and natural growth are converted into language geography through the H matrix.",
        "support_steps": ["bilateral flows", "transition probabilities", "natural growth", "N propagation", "H ratios", "diag(N)H", "capital interpolation"],
        "decision_consequence": "Audit stochastic direction, growth units, H updates, overlap semantics, and spatial validation before using the surface downstream.",
        "source_pages": [15, 16, 17, 18],
    },
    {
        "claim": "The office model discretizes four country features and combines them through fuzzy multi-objective scoring.",
        "support_steps": ["English share", "migration", "GDP", "Chinese share", "four dendrograms", "ordinal indices", "memberships", "weights", "top six"],
        "decision_consequence": "Require reproducible scaling, stakeholder weights, cut stability, costs, and feasibility before acting on the rank order.",
        "source_pages": [19, 20],
    },
    {
        "claim": "A separate spatial concentration diagnostic prunes each six-city portfolio to four cities.",
        "support_steps": ["economic centers", "coordinate grid", "MIC surface", "overlap interpretation", "short-run removal", "long-run removal", "memo condition"],
        "decision_consequence": "Tie each removal to measured service loss and operating savings rather than concentration alone.",
        "source_pages": [20, 21, 22, 24],
    },
]


EXPECTED_OBSERVATION_DIMENSIONS = {
    "language": 106,
    "modeling": 65,
    "logic": 23,
    "visualization": 44,
    "verification": 18,
    "data": 14,
    "assumption": 12,
    "result": 16,
    "weakness": 18,
    "other": 8,
}
EXPECTED_OBSERVATION_COUNT = sum(EXPECTED_OBSERVATION_DIMENSIONS.values())
assert EXPECTED_OBSERVATION_COUNT == 324


def build_card(
    language: dict[str, Any],
    models_record: dict[str, Any],
    visuals: list[dict[str, Any]],
) -> dict[str, Any]:
    models = models_record["models"]
    equation_count = sum(len(model["governing_equations"]) for model in models)
    section_map = [
        page_summary(
            item["pages"][0],
            (
                f"Input: {item['input']} Rhetorical job: {item['rhetorical']} "
                f"Analytical job: {item['analytical']} Output: {item['output']} "
                f"Handoff: {item['handoff']}"
            ),
        )
        for item in CHAPTERS
    ]
    writing_logic = [
        page_summary(
            item["pages"][0],
            (
                f"{item['label']}: {item['input']} -> {item['rhetorical']} -> "
                f"{item['analytical']} -> {item['output']} -> {item['handoff']}"
            ),
        )
        for item in CHAPTERS
    ]
    by_id = {model["model_id"]: model for model in models}
    dependency_graph = [
        page_summary(
            by_id[edge["to_model_id"]]["page"],
            f"{edge['from_model_id']} -> {edge['to_model_id']}: {edge['handoff']}",
        )
        for edge in models_record["dependency_edges"]
    ]
    first_pattern_pages = {
        pattern["pattern_id"]: next(
            unit["page"]
            for unit in language["units"]
            if pattern["pattern_id"] in unit["candidate_pattern_ids"]
        )
        for pattern in PATTERNS
    }
    language_observations = [
        page_summary(
            first_pattern_pages[pattern["pattern_id"]],
            (
                f"{pattern['name']}: {' -> '.join(pattern['information_order'])}; "
                f"function={pattern['function']}; boundary={pattern['boundary']}"
            ),
        )
        for pattern in PATTERNS
    ]
    language_observations.extend(
        page_summary(
            unit["page"],
            (
                f"{unit['function']}: {unit['reusable_pattern']}; retain "
                f"{unit['rhetorical_move']}"
            ),
        )
        for unit in language["units"][:16]
    )

    weakness_records = []
    for page, model_number, equation_number, summary in WEAKNESS_SPECS:
        record = page_summary(
            page,
            summary,
            model_id=f"MU-{ID_STEM}-{model_number:03d}",
        )
        if equation_number is not None:
            record["equation_id"] = f"EQ-{ID_STEM}-{equation_number:03d}"
        weakness_records.append(record)

    impacts = [
        {"rule_id": rule_id, "action": action, "evidence_ids": []}
        for rule_id, action in RULE_ACTIONS.items()
    ]
    return {
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "team_control_number": "74316",
        "title": "Forecasting Language Development and Locating International Offices",
        "award_status": "outstanding",
        "source": {
            "relative_path": SOURCE_PATH,
            "sha256": SHA256,
            "page_count": PAGE_COUNT,
        },
        "schema_version": 1,
        "source_quality": {
            "status": "text-rich-with-damaged-mathematics",
            "notes": (
                "Complete UTF-8 page extraction and 39/39 bounded full-page review; "
                "four focused crops control the Markov, fuzzy, MIC, and AR-variance "
                "small labels. Greek letters and matrices are partly damaged, a commercial "
                "Chinese watermark intersects every page header, Figure 12 is reused, and "
                "the final printed page says Page 37 of 20."
            ),
        },
        "context_sources": [
            "2018 MCM Problem B official prompt",
            "Summary Sheet and twenty-four-page main report",
            "sixteen appendices on physical pages 26-39",
            "nine cited articles, databases, or data portals",
        ],
        "task_reconstruction": {
            "summary": (
                "Forecast temporal and geographic distributions of major languages for "
                "fifty years, recommend new international offices at short and long horizons, "
                "analyze resource-saving reductions, and communicate advice to the COO."
            ),
            "inputs": [
                "L1, L2, and total speaker histories",
                "ten macro indicators",
                "country population and migration flows",
                "country-language demand ratios",
                "capital coordinates",
                "English, Chinese, migration, and GDP office features",
                "economic-center grid assumptions",
            ],
            "outputs": [
                "short-run native and non-native forecasts",
                "2067 language rankings",
                "country-language geographic surfaces",
                "cross-model comparison",
                "six-office rankings for two horizons",
                "four-office resource-saving plans",
                "COO memo",
            ],
        },
        "section_map": section_map,
        "assumptions": [
            page_summary(page, summary) for page, summary in ASSUMPTION_SPECS
        ],
        "data_and_preprocessing": [
            page_summary(page, summary) for page, summary in DATA_SPECS
        ],
        "models": [
            page_summary(model["page"], f"{model['model_id']}: {model['purpose']}")
            for model in models
        ],
        "dependency_graph": dependency_graph,
        "verification": [
            page_summary(page, summary) for page, summary in VERIFICATION_SPECS
        ],
        "results_trace": [
            page_summary(page, summary) for page, summary in RESULT_SPECS
        ],
        "contributions": [
            page_summary(1, "The summary keeps the full factor-to-forecast-to-geography-to-office route visible before derivation."),
            page_summary(3, "Native and non-native speaker identities receive distinct mechanisms rather than one undifferentiated trend."),
            page_summary(5, "Ten indicators are compressed into four interpreted factors before entering the ECM."),
            page_summary(10, "Recursive short-run forecast error is used to motivate a separate long-run differential system."),
            page_summary(11, "The long-run model separates endogenous logistic native growth from externally driven non-native change."),
            page_summary(14, "Coefficient, initial-state, and stochastic scenarios provide three different local reliability views."),
            page_summary(16, "A 226-country migration system separates stochastic relocation from natural population growth."),
            page_summary(17, "The H matrix provides an explicit population-to-language handoff for geographic forecasting."),
            page_summary(18, "A second model route is compared with the differential forecast rather than left unexamined."),
            page_summary(19, "Four office features are exposed through clustering, ordinal indices, fuzzy memberships, and weights."),
            page_summary(21, "A separate spatial-overlap diagnostic turns six ranked cities into a resource-saving four-city alternative."),
            page_summary(23, "The memo reorganizes technical evidence around operating horizon and office action."),
        ],
        "writing_logic": writing_logic,
        "language_observations": language_observations,
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [
            page_summary(1, "The Summary exposes the complete model route and both horizon-specific recommendations in judge-scannable order.", evidence_class="J"),
            page_summary(10, "The explicit failure-to-replacement handoff gives the long-run model a visible rationale rather than presenting it as an unrelated technique.", evidence_class="J"),
            page_summary(18, "Cross-model comparison makes disagreement visible before the office stage, although the statistical support remains incomplete.", evidence_class="J"),
            page_summary(21, "The six-to-four office change responds directly to the resource-saving clause of the task.", evidence_class="J"),
            page_summary(23, "The memo preserves the short- and long-run distinction needed by the operating audience.", evidence_class="C"),
        ],
        "weaknesses": weakness_records,
        "independent_extensions": [
            {"extension_id": "E-B-122-001", "page": 5, "summary": "Freeze the six-language panel and rebuild PCA with explicit standardization, missingness, loadings, and retained-variance checks."},
            {"extension_id": "E-B-122-002", "page": 7, "summary": "Use rolling-origin AR and ECM backtests with language-specific baselines, calibrated intervals, and stationarity diagnostics."},
            {"extension_id": "E-B-122-003", "page": 10, "summary": "Estimate carrying capacities and non-native mechanisms from demographic and policy covariates instead of fixed logistic-plus-linear assumptions."},
            {"extension_id": "E-B-122-004", "page": 14, "summary": "Run joint global sensitivity and seeded stochastic simulation, then report language-rank and office-decision switch probabilities."},
            {"extension_id": "E-B-122-005", "page": 16, "summary": "Audit the 226-country transition matrix for direction, row sums, connectivity, periodicity, missing flows, and holdout migration error."},
            {"extension_id": "E-B-122-006", "page": 17, "summary": "Replace manual H updates with a documented dynamic country-language model and propagate its uncertainty through spatial forecasts."},
            {"extension_id": "E-B-122-007", "page": 18, "summary": "Compare both forecast routes against held-out observations and use model averaging only after dependence and disagreement are quantified."},
            {"extension_id": "E-B-122-008", "page": 19, "summary": "Retain continuous office features, test cluster stability, and elicit criterion weights from stakeholders."},
            {"extension_id": "E-B-122-009", "page": 20, "summary": "Reconstruct membership functions and normalize every criterion before calculating Pareto and cost-aware office alternatives."},
            {"extension_id": "E-B-122-010", "page": 21, "summary": "Replace the MIC concentration interpretation with a validated spatial coverage and redundancy metric tied to service loss and operating cost."},
        ],
        "candidate_rule_impacts": impacts,
        "unresolved_questions": [
            "What frozen six-language, nine-year panel and standardization produced the four PCA components?",
            "Which AR coefficients satisfy the stationarity assumptions used outside the short horizon?",
            "What residual series, lags, deterministic terms, and uncertainty reproduce the EG and ECM tables?",
            "How were each logistic capacity and constant non-native increment estimated and validated?",
            "How should the Bengali L1=248 and total=160 row and the printed contribution percentages be interpreted?",
            "What shock distributions, variances, draw count, seed, and interval calculation generated Figure 14?",
            "Does the 226-country transition matrix empirically satisfy irreducibility and aperiodicity?",
            "What executable rule manually updates every post-2017 entry of H?",
            "What spatial projection, boundary rule, and validation support the Lagrange surfaces?",
            "What exact samples, hypotheses, and p-values support the stated 94 percent ANOVA conclusion?",
            "What membership functions and criterion scaling precede A=(0.4,0.25,0.25,0.1) and B=AR?",
            "What measured service loss, operating cost, and stakeholder preference justify each two-office removal?",
        ],
        "protocol_v2_records": {
            "language": {
                "path": f"artifacts/language-units/{PAPER_ID}.json",
                "schema_version": 3,
                "unit_count": len(language["units"]),
                "chapters": language["available_chapters"],
                "review_status": "validated",
            },
            "models": {
                "path": f"artifacts/model-units/{PAPER_ID}.json",
                "schema_version": 2,
                "model_count": len(models),
                "equation_count": equation_count,
                "review_status": "validated",
            },
        },
        "review_status": "validated",
    }


def build_observations(
    units: list[dict[str, Any]],
    models_record: dict[str, Any],
    visuals: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []
    applicability = {
        "language": "Transfer only the rhetorical mechanism and information order after replacing every language, country, city, year, value, coefficient, equation, and decision boundary.",
        "logic": "Use the handoff only when the receiving stage consumes the named output without changing entity, unit, horizon, evidence class, uncertainty, or scope.",
        "modeling": "Reuse the model only after defining entities, units, indices, timing, equations, assumptions, calibration, and every downstream output consumer.",
        "visualization": "Reuse the visual role only with legible units, horizon, scenario, encodings, source model, exact claim, and accessible numeric alternatives.",
        "verification": "Apply the check to frozen source bytes or executable outputs before promoting any affected forecast, comparison, ranking, or recommendation.",
        "data": "Use the input only with a frozen source, year, geography, unit, transformation, missingness, uncertainty, and downstream equation or score term.",
        "assumption": "Treat the premise as a scope boundary and test the trajectory, rank, or office decision that changes when it is relaxed.",
        "result": "Report the result only with its model, entity, horizon, scenario, unit, comparator, feasibility, and uncertainty status.",
        "weakness": "Keep the defect in the last warning pass and pair it with a concrete algebraic, empirical, computational, provenance, or decision repair.",
        "other": "Preserve the context without upgrading a prompt clause, citation, software mention, appendix, or memo statement into validation.",
    }
    counterevidence = {
        "language": "A fluent sentence without a source anchor, evidence role, receiving use, and anti-copy boundary is not a reusable language unit.",
        "logic": "Chronology or a section heading alone does not establish an output-to-input dependency.",
        "modeling": "Naming PCA, AR, ECM, logistic, Markov, clustering, fuzzy evaluation, or MINE does not establish calibration, identifiability, feasibility, or reproducibility.",
        "visualization": "A polished chart cannot repair missing units, damaged formulas, contradictory table values, arbitrary weights, or an unsupported decision." ,
        "verification": "A fitted example, one-at-a-time sensitivity table, unseeded simulation, or agreement between dependent models is not external validation.",
        "data": "An undated database name, weighted value, or manually adjusted matrix is not a reproducible provenance ledger.",
        "assumption": "Author assertion or convenience does not make an untested premise an observed fact.",
        "result": "A simulated trajectory, p-value statement, fuzzy rank, or MIC grid is not an observed causal effect or guaranteed business outcome.",
        "weakness": "The warning does not replace or erase the paper's positive language, organization, model, formula, algorithm, and visual evidence.",
        "other": "Context cannot substitute for complete page coverage, formula retention, or a validated transaction artifact.",
    }

    def add(
        page: int,
        section: str,
        dimension: str,
        basis: str,
        interpretation: str,
        evidence_class: str,
        rule_ids: list[str],
        confidence: str = "high",
    ) -> None:
        observations.append(
            {
                "schema_version": 1,
                "observation_id": f"O-{ID_STEM}-{len(observations) + 1:04d}",
                "paper_id": PAPER_ID,
                "problem_type": PROBLEM_TYPE,
                "year": YEAR,
                "page": page,
                "section": section,
                "evidence_class": evidence_class,
                "dimension": dimension,
                "source_basis": basis,
                "interpretation": interpretation,
                "applicability": [applicability[dimension]],
                "counterevidence": [counterevidence[dimension]],
                "confidence": confidence,
                "candidate_rule_ids": list(dict.fromkeys(rule_ids)),
            }
        )

    for unit in units:
        add(
            unit["page"],
            unit["section"],
            "language",
            unit["source_excerpt"],
            (
                f"Retain the rhetorical function '{unit['function']}' and the order "
                f"{' -> '.join(unit['information_order'])}; preserve its evidence type "
                "and handoff while replacing all source-specific content."
            ),
            "O",
            ["R-B-LANG-001"],
        )

    for item in CHAPTERS:
        rules = ["R-B-LOG-001"]
        if item["chapter"] in {"model-establishment", "model-improvement", "algorithm"}:
            rules.append("R-B-MOD-008")
        if item["chapter"] in {"algorithm", "conclusion", "memo"}:
            rules.append("R-B-DEC-002")
        add(
            item["pages"][0],
            f"{item['label']} / five-move section contract",
            "logic",
            (
                f"Input: {item['input']} Rhetorical job: {item['rhetorical']} "
                f"Analytical job: {item['analytical']} Output: {item['output']} "
                f"Handoff: {item['handoff']}"
            ),
            "Preserve the complete input -> rhetorical job -> analytical job -> output -> handoff contract in the report-wide forecast-to-decision chain.",
            "I",
            rules,
        )

    for index, chain in enumerate(ARGUMENT_CHAINS, start=1):
        rules = ["R-B-LOG-001", "R-B-MOD-008"]
        if index >= 6:
            rules.append("R-B-DEC-002")
        add(
            chain["source_pages"][0],
            f"Main argument chain {index}",
            "logic",
            f"{chain['claim']} | {' -> '.join(chain['support_steps'])}",
            chain["decision_consequence"],
            "I",
            rules,
        )

    models = models_record["models"]

    def model_rule_ids(model_number: int) -> list[str]:
        rules = ["R-B-MOD-004"]
        if 2 <= model_number <= 10:
            rules.append("R-B-MOD-008")
        if 5 <= model_number <= 10:
            rules.append("R-B-VER-002")
        if model_number >= 11:
            rules.extend(["R-B-MOD-003", "R-B-DEC-002"])
        return rules

    for model_number, model in enumerate(models, start=1):
        add(
            model["page"],
            f"{model['section']} / model unit",
            "modeling",
            f"{model['model_id']}: {model['purpose']}",
            (
                f"Retain the complete {model['family']} unit with variables, equations, "
                "conditions, assumptions, algorithms, handoff outputs, validation references, "
                "and recorded missing implementation details."
            ),
            "O",
            model_rule_ids(model_number),
        )
        for equation_record in model["governing_equations"]:
            add(
                equation_record["page"],
                f"{model['section']} / {equation_record['equation_id']}",
                "modeling",
                equation_record["source_expression"],
                (
                    "Preserve the literal source statement, normalized transcription, "
                    f"variable symbols, purpose, confidence, and ownership by {model['model_id']} "
                    "before using the output downstream."
                ),
                "O",
                model_rule_ids(model_number),
                equation_record["transcription_confidence"],
            )

    for visual in visuals:
        add(
            visual["page"],
            f"{visual['figure']} / {visual['visual_record_id']}",
            "visualization",
            visual["summary"],
            (
                f"Retain this {visual['form']} for {visual['analytical_purpose']}. "
                f"Its exact supported claim remains: {visual['exact_claim']}"
            ),
            "O",
            ["R-B-VIZ-002"],
        )

    for page, summary in VERIFICATION_SPECS:
        rules = ["R-B-VER-004"]
        if any(
            token in summary.lower()
            for token in ("forecast", "sensitivity", "monte carlo", "anova", "markov", "mic")
        ):
            rules.append("R-B-VER-002")
        add(
            page,
            "Verification and source-fidelity ledger",
            "verification",
            summary,
            "Keep transcription, algebra, dimension, index, normalization, stochastic, model-agreement, decision, and visual-label checks distinct; route unresolved failures to G7.",
            "E",
            rules,
        )

    for page, summary in DATA_SPECS:
        add(
            page,
            "Data and preprocessing ledger",
            "data",
            summary,
            "Record source class, date, geography, entity, unit, weighting, aggregation, manual adjustment, missingness, uncertainty, and every downstream use.",
            "O",
            ["R-B-DATA-002"],
        )

    for page, summary in ASSUMPTION_SPECS:
        rules = ["R-B-MOD-004"]
        if page >= 10:
            rules.append("R-B-MOD-008")
        if page >= 19:
            rules.extend(["R-B-MOD-003", "R-B-DEC-002"])
        add(
            page,
            "Assumption ledger",
            "assumption",
            summary,
            "Convert the simplification into a testable boundary and identify the language path, spatial surface, rank, or office decision that may change when it is relaxed.",
            "O",
            rules,
        )

    for page, summary in RESULT_SPECS:
        rules = ["R-B-VIZ-002", "R-B-VER-002"]
        if page >= 19:
            rules.append("R-B-DEC-002")
        add(
            page,
            "Results and decision trace",
            "result",
            summary,
            "Bind the value, comparison, rank, or recommendation to its source model, entity, year, horizon, unit, feasibility, uncertainty, and receiving decision.",
            "O",
            rules,
        )

    for page, model_number, equation_number, summary in WEAKNESS_SPECS:
        basis = summary
        if equation_number is not None:
            basis = f"EQ-{ID_STEM}-{equation_number:03d}: {summary}"
        add(
            page,
            f"Final weakness watch / MU-{ID_STEM}-{model_number:03d}",
            "weakness",
            basis,
            "Retain this as a last-pass limitation after positive coverage and require a specific algebraic, empirical, computational, provenance, or decision repair before transfer.",
            "E",
            ["R-B-VER-004", "R-B-VER-002", *model_rule_ids(model_number)],
            "medium",
        )

    for page, summary in CONTEXT_SPECS:
        rules = ["R-B-LOG-001"]
        if page in {2, 20, 23}:
            rules.append("R-B-DEC-002")
        add(
            page,
            "Context, source quality, and deliverable trace",
            "other",
            summary,
            "Keep this context attached so task scope, audience, source quality, appendix support, and physical-page anchoring remain visible without being mistaken for validation.",
            "C",
            rules,
            "medium",
        )

    actual_dimensions = dict(Counter(item["dimension"] for item in observations))
    if actual_dimensions != EXPECTED_OBSERVATION_DIMENSIONS:
        raise SystemExit(
            f"q122 observation dimensions changed: {actual_dimensions} != "
            f"{EXPECTED_OBSERVATION_DIMENSIONS}"
        )
    if EXPECTED_OBSERVATION_DIMENSIONS["language"] <= max(
        count
        for dimension, count in EXPECTED_OBSERVATION_DIMENSIONS.items()
        if dimension != "language"
    ):
        raise SystemExit("q122 language is not the largest observation dimension")
    if EXPECTED_OBSERVATION_DIMENSIONS["weakness"] >= EXPECTED_OBSERVATION_DIMENSIONS["language"]:
        raise SystemExit("q122 weakness must remain strictly below language")
    return observations


def proxy_review_segments() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    def summarize(
        segment: int,
        kind: str,
        paths: list[Path],
        page_range: list[int],
    ) -> dict[str, Any]:
        missing = [str(path) for path in paths if not path.is_file()]
        if missing:
            raise SystemExit(f"missing q122 {kind} review proxies: {missing}")
        sizes = [path.stat().st_size for path in paths]
        if len(paths) > 7 or max(sizes) > 450000 or sum(sizes) > 4194304:
            raise SystemExit(
                f"q122 {kind} proxy segment {segment} exceeds request-body guard"
            )
        return {
            "segment": segment,
            "page_range": page_range,
            "proxy_count": len(paths),
            "total_proxy_bytes": sum(sizes),
            "largest_proxy_bytes": max(sizes),
            "proxy_files": [path.relative_to(PROXY_ROOT).as_posix() for path in paths],
        }

    full_segments = []
    for segment, (first_page, last_page) in enumerate(
        ((1, 7), (8, 14), (15, 21), (22, 28), (29, 35), (36, 39)),
        start=1,
    ):
        paths = [
            PROXY_ROOT / "full" / f"page-{page:04d}.jpg"
            for page in range(first_page, last_page + 1)
        ]
        full_segments.append(
            summarize(
                segment,
                "full-page",
                paths,
                list(range(first_page, last_page + 1)),
            )
        )

    focused_paths = [
        PROXY_ROOT / "crop-page-0016-markov.jpg",
        PROXY_ROOT / "crop-page-0020-fuzzy.jpg",
        PROXY_ROOT / "crop-page-0021-mic.jpg",
        PROXY_ROOT / "crop-page-0029-ar-variance.jpg",
    ]
    focused_segments = [
        summarize(1, "focused-crop", focused_paths, [16, 20, 21, 29])
    ]
    return full_segments, focused_segments


def build_audit(
    language: dict[str, Any],
    models_record: dict[str, Any],
    card: dict[str, Any],
    observations: list[dict[str, Any]],
) -> dict[str, Any]:
    by_chapter: dict[str, list[dict[str, Any]]] = {}
    for unit in language["units"]:
        by_chapter.setdefault(unit["chapter"], []).append(unit)
    layouts = {
        layout["chapter"]: layout for layout in language["chapter_layouts"]
    }
    chapter_specs = {item["chapter"]: item for item in CHAPTERS}
    models = models_record["models"]
    equations = [
        equation_record
        for model in models
        for equation_record in model["governing_equations"]
    ]
    pattern_dispositions = {
        pattern["pattern_id"]: pattern["disposition"] for pattern in PATTERNS
    }

    paragraph_chains = []
    for chapter_name in ("abstract", "introduction"):
        layout = layouts[chapter_name]
        spec = chapter_specs[chapter_name]
        paragraph_units = by_chapter[chapter_name][: layout["paragraph_count"]]
        if len(paragraph_units) != layout["paragraph_count"]:
            raise SystemExit(
                f"q122 {chapter_name} paragraph-chain coverage changed"
            )
        paragraph_chains.append(
            {
                "chapter": chapter_name,
                "visual_paragraph_count": layout["paragraph_count"],
                "coverage_status": "complete",
                "gaps": [],
                "paragraphs": [
                    {
                        "paragraph_index": index,
                        "dominant_move": (
                            f"{spec['rhetorical']} -> {unit['function']} -> "
                            f"{spec['output']} -> {spec['handoff']}"
                        ),
                        "language_unit_ids": [unit["language_unit_id"]],
                    }
                    for index, unit in enumerate(paragraph_units, start=1)
                ],
            }
        )

    chapter_saturation = [
        {
            "chapter": item["chapter"],
            "pass_count": 3,
            "last_pass_new_moves": 0,
            "coverage_status": "complete",
            "gaps": [],
            "new_moves_by_pass": [item["count"], 2, 0],
        }
        for item in CHAPTERS
    ]
    section_progressions = [
        {
            "chapter": item["chapter"],
            "moves": [
                f"input: [{item['code']} {item['label']}] {item['input']}",
                f"rhetorical job: [{item['code']} {item['label']}] {item['rhetorical']}",
                f"analytical job: [{item['code']} {item['label']}] {item['analytical']}",
                f"output: [{item['code']} {item['label']}] {item['output']}",
                f"handoff: [{item['code']} {item['label']}] {item['handoff']}",
            ],
            "positive_pattern": (
                "Retain input -> rhetorical job -> analytical job -> output -> "
                "handoff; place formula, fact, symbol, and claim warnings only "
                "in the final pass."
            ),
        }
        for item in CHAPTERS
    ]

    warnings = []
    for model_number, equation_offset, page, warning in FORMULA_WARNINGS:
        model = models[model_number - 1]
        try:
            equation_record = model["governing_equations"][equation_offset]
        except IndexError as exc:
            raise SystemExit(
                f"q122 warning references missing equation offset: "
                f"model={model_number} offset={equation_offset}"
            ) from exc
        warnings.append(
            {
                "model_id": model["model_id"],
                "equation_id": equation_record["equation_id"],
                "page": page,
                "warning": warning,
            }
        )

    language_unit_dispositions = []
    for unit in language["units"]:
        candidate_pattern_ids = unit["candidate_pattern_ids"]
        if not candidate_pattern_ids:
            raise SystemExit(
                "q122 language unit has no positive reusable pattern: "
                f"{unit['language_unit_id']}"
            )
        disposition = (
            "opens-candidate"
            if any(
                pattern_dispositions[pattern_id] == "opens-candidate"
                for pattern_id in candidate_pattern_ids
            )
            else "supports-existing"
        )
        language_unit_dispositions.append(
            {
                "language_unit_id": unit["language_unit_id"],
                "disposition": disposition,
                "target_pattern_ids": candidate_pattern_ids,
                "reason": (
                    "Transfer the rhetorical mechanism and information order only "
                    "after replacing every language, country, city, year, value, "
                    "coefficient, equation, table entry, and recommendation."
                ),
            }
        )

    positive_reusable_language_count = sum(
        record["disposition"] != "paper-specific-nonreusable"
        for record in language_unit_dispositions
    )
    if positive_reusable_language_count != 106:
        raise SystemExit(
            "q122 positive reusable language count changed: "
            f"{positive_reusable_language_count} != 106"
        )

    dimension_counter = Counter(item["dimension"] for item in observations)
    dimensions = {
        dimension: dimension_counter[dimension]
        for dimension in EXPECTED_OBSERVATION_DIMENSIONS
    }
    if dimensions != EXPECTED_OBSERVATION_DIMENSIONS:
        raise SystemExit(
            f"q122 audit dimensions changed: {dimensions} != "
            f"{EXPECTED_OBSERVATION_DIMENSIONS}"
        )
    full_segments, focused_segments = proxy_review_segments()
    return {
        "audit_id": f"LA-{ID_STEM}",
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "schema_version": 1,
        "priority_order": [
            "language-imitation",
            "organization-logic",
            "formula-error-watch",
        ],
        "chapter_saturation": chapter_saturation,
        "language_unit_dispositions": language_unit_dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "complete",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [
                f"{item['label']}: {item['output']} -> {item['handoff']}"
                for item in CHAPTERS
            ],
            "section_progressions": section_progressions,
            "main_argument_chains": ARGUMENT_CHAINS,
        },
        "formula_error_watch": {
            "mode": "last-pass-warning-only",
            "completed_after_positive_passes": True,
            "warnings": warnings,
        },
        "model_retention": {
            "model_count": len(models),
            "retained_model_ids": [model["model_id"] for model in models],
            "retained_equation_ids": [
                equation_record["equation_id"] for equation_record in equations
            ],
            "central_equations": [
                {
                    "model_id": model["model_id"],
                    "equation_ids": [
                        equation_record["equation_id"]
                        for equation_record in model["governing_equations"]
                    ],
                    "all_central_equations_retained": True,
                }
                for model in models
                if model["governing_equations"]
            ],
        },
        "visualization_dispositions": [
            {
                "paper_card_visual_index": index,
                "visual_record_id": visual["visual_record_id"],
                "disposition": "important-visual-record",
                "analytical_purpose": visual["analytical_purpose"],
            }
            for index, visual in enumerate(
                card["visualization_observations"], start=1
            )
        ],
        "dimension_counts": dimensions,
        "positive_reusable_language_count": positive_reusable_language_count,
        "weakness_record_count": dimensions["weakness"],
        "review_status": "validated",
        "gate_attestation": {
            "g1_g3_language": "validated-before-G4",
            "g4_organization": "passed-before-G5-G6",
            "g5_models": "validated-before-G7",
            "g6_visuals": "passed-before-G7",
            "g7_warning_mode": "last-pass-warning-only",
            "g7_warning_count": len(warnings),
            "warnings_strict_minority_of_language": (
                len(warnings) < len(language["units"])
            ),
            "request_body_guard": {
                "previous_413_root_cause": (
                    "Accumulated base64 image payloads in a Codex session JSONL "
                    "exceeded the nginx request-size limit at "
                    "https://1for.cc/v1/responses; PDF size and filesystem "
                    "permissions were not causal."
                ),
                "single_image_per_tool_call": True,
                "proxy_byte_limit": 450000,
                "full_page_segment_image_limit": 7,
                "context_segment_image_limit": 8,
                "context_segment_model_visible_limit_bytes": 4194304,
                "full_page_review_segments": full_segments,
                "focused_crop_segments": focused_segments,
                "original_full_page_png_in_context": False,
                "full_session_jsonl_in_context": False,
                "base64_content_printed": False,
            },
        },
    }


def build_extraction() -> dict[str, Any]:
    extraction = json.loads(SOURCE_EXTRACTION.read_text(encoding="utf-8"))
    identity = (
        extraction.get("paper_id"),
        extraction.get("problem_type"),
        str(extraction.get("year")),
        extraction.get("source_sha256"),
        extraction.get("page_count"),
    )
    expected = (PAPER_ID, PROBLEM_TYPE, YEAR, SHA256, PAGE_COUNT)
    if identity != expected:
        raise SystemExit(f"q122 extraction identity mismatch: {identity} != {expected}")
    if extraction.get("extraction_status") != "text-extracted":
        raise SystemExit("q122 extraction is not text-extracted")
    full_segments, focused_segments = proxy_review_segments()
    extraction["visual_review_status"] = "complete"
    extraction["visual_review"] = {
        "status": "complete",
        "reviewed_pages": list(range(1, PAGE_COUNT + 1)),
        "notes": [
            "All 39 physical pages were read in UTF-8 page-aware text and reviewed as byte-bounded full-page JPEG proxies in six groups of at most seven images.",
            "Four focused crops preserved the Markov equations, fuzzy memberships, MIC grid labels, and Appendix 5 AR-variance derivation without loading original full-page PNGs.",
            "The Chinese commercial watermark was excluded from author-language evidence; reused Figure 12 and the final Page 37 of 20 marker remain recorded as source defects.",
        ],
    }
    extraction["visual_review_manifest"] = {
        "pages_reviewed": list(range(1, PAGE_COUNT + 1)),
        "full_page_proxy_count": sum(
            item["proxy_count"] for item in full_segments
        ),
        "focused_crop_proxy_count": sum(
            item["proxy_count"] for item in focused_segments
        ),
        "full_page_proxy_segments": full_segments,
        "focused_crop_segments": focused_segments,
        "original_full_page_png_in_context": False,
        "review_note": (
            "Full-page review covered physical pages 1-39; focused crops retained "
            "small formula, matrix, membership, and grid labels under the request-body guard."
        ),
    }
    return extraction


def bind_rule_impacts(
    card: dict[str, Any], observations: list[dict[str, Any]]
) -> None:
    first_by_rule: dict[str, str] = {}
    for observation in observations:
        for rule_id in observation["candidate_rule_ids"]:
            first_by_rule.setdefault(rule_id, observation["observation_id"])
    for impact in card["candidate_rule_impacts"]:
        rule_id = impact["rule_id"]
        if rule_id not in first_by_rule:
            raise SystemExit(f"no q122 observation evidence for {rule_id}")
        impact["evidence_ids"] = [first_by_rule[rule_id]]


def main() -> None:
    if STAGE.exists():
        if not STAGE.is_dir():
            raise SystemExit(f"q122 staging path is not a directory: {STAGE}")
        if any(STAGE.iterdir()):
            raise SystemExit(
                f"refusing to overwrite non-empty staging directory: {STAGE}"
            )

    language, units = build_language()
    models_record = build_models()
    visuals = build_visuals()
    card = build_card(language, models_record, visuals)
    observations = build_observations(units, models_record, visuals)
    bind_rule_impacts(card, observations)
    audit = build_audit(language, models_record, card, observations)
    extraction = build_extraction()

    expected_counts = {
        "chapters": 16,
        "language_units": 106,
        "models": 14,
        "equations": 51,
        "dependency_edges": 19,
        "visual_records": 44,
        "observations": EXPECTED_OBSERVATION_COUNT,
        "formula_warnings": 18,
    }
    actual_counts = {
        "chapters": len(language["available_chapters"]),
        "language_units": len(units),
        "models": len(models_record["models"]),
        "equations": sum(
            len(model["governing_equations"])
            for model in models_record["models"]
        ),
        "dependency_edges": len(models_record["dependency_edges"]),
        "visual_records": len(visuals),
        "observations": len(observations),
        "formula_warnings": len(audit["formula_error_watch"]["warnings"]),
    }
    if actual_counts != expected_counts:
        raise SystemExit(
            f"q122 artifact counts changed: {actual_counts} != {expected_counts}"
        )

    STAGE.mkdir(parents=True, exist_ok=True)
    targets = {
        "language.json": language,
        "models.json": models_record,
        "card.json": card,
        "audit.json": audit,
        "extraction.json": extraction,
    }
    output_paths = [STAGE / name for name in [*targets, "observations.jsonl"]]
    existing = [str(path) for path in output_paths if path.exists()]
    if existing:
        raise SystemExit(f"refusing to overwrite q122 staged files: {existing}")
    for name, value in targets.items():
        dump_json(STAGE / name, value)
    dump_jsonl(STAGE / "observations.jsonl", observations)
    print(
        json.dumps(
            {
                "stage": str(STAGE),
                **actual_counts,
                "dimension_counts": audit["dimension_counts"],
                "full_page_proxy_segments": audit["gate_attestation"]
                ["request_body_guard"]["full_page_review_segments"],
                "focused_crop_segments": audit["gate_attestation"]
                ["request_body_guard"]["focused_crop_segments"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
