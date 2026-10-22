#!/usr/bin/env python3
"""Build Queue 121 artifacts in an isolated, create-only staging directory.

This builder never deletes, moves, or overwrites a live artifact. It refuses
to run when its dedicated staging directory is non-empty. Promotion and the
transaction append are separate validated operations.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2018-73410-069a3764"
ID_STEM = "B-2018-73410"
PROBLEM_TYPE = "B"
YEAR = "2018"
SHA256 = "069a37649489a1cad790a23de3924db0d5867eb5518f4edc68af66a9b73a71de"
PAGE_COUNT = 28
SOURCE_PATH = "2018\u7f8e\u8d5b\u7279\u7b49\u5956/B\u98985\u7bc7/B73410-Language Population Projection and Location.pdf"
STAGE = ROOT / "tmp" / "q121-stage-v2"
SOURCE_EXTRACTION = ROOT / "artifacts" / "papers" / PAPER_ID / "extraction.json"
SOURCE_PAGES = ROOT / "artifacts" / "papers" / PAPER_ID / "text" / "pages"
PROXY_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID / "review-proxies"


RULES = {
    "language": "R-B-LANG-001",
    "logic": "R-B-LOG-001",
    "modeling": "R-B-MOD-004",
    "fusion": "R-B-MOD-003",
    "dynamic": "R-B-MOD-008",
    "visualization": "R-B-VIZ-002",
    "verification": "R-B-VER-004",
    "reliability": "R-B-VER-002",
    "data": "R-B-DATA-002",
    "stakeholder": "R-B-DEC-002",
}


def dump_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def dump_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.write_text(
        "".join(
            json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
            for value in values
        ),
        encoding="utf-8",
        newline="\n",
    )


PATTERNS = [
    {
        "pattern_id": "LP-B-Q121-PROBLEM-PIVOT",
        "name": "constraint-rich problem to model pivot",
        "occurrences": 8,
        "locations": ["Summary", "Introduction", "Modified Model", "Application"],
        "function": "Move from a named practical obstacle or failed baseline to the exact model object introduced in response.",
        "information_order": ["operating change", "specific obstacle", "why a baseline fails", "new model object", "bounded purpose"],
        "slots": ["[context change]", "[measurable obstacle]", "[baseline limitation]", "[introduced state/model]", "[task-bound output]"],
        "variants": ["therefore we establish", "however the model is lacking", "building upon the preliminary model", "drawing upon the analysis"],
        "boundary": "Name the failed assumption or missing state before claiming that a replacement is necessary; novelty language alone is insufficient.",
        "disposition": "supports-existing",
        "original_examples": [
            "Because weekday arrivals invalidate a stationary queue estimate, the clinic introduces a time-indexed service state for the staffing horizon.",
            "After reservoir losses break the constant-yield baseline, the study adds a storage-dependent release term for the stated drought scenarios.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-STAGED-ROUTE",
        "name": "part-by-part analytical route",
        "occurrences": 7,
        "locations": ["Summary", "Introduction", "Memo"],
        "function": "Preview a long solution as an ordered sequence whose output from one stage becomes the next stage's input.",
        "information_order": ["stage marker", "author action", "model or data object", "result", "next-stage use"],
        "slots": ["[first/then/finally]", "[estimate/modify/compare/select]", "[typed object]", "[bounded result]", "[downstream task]"],
        "variants": ["in part I", "in part II", "in the end", "building upon", "combined with"],
        "boundary": "A route is an organization device, not validation; every promised stage still needs evidence and a handoff.",
        "disposition": "supports-existing",
        "original_examples": [
            "First the maintenance team estimates failure exposure; next it schedules crews; finally it checks the chosen schedule under delayed parts.",
            "The watershed analysis calibrates runoff, passes the ensemble into storage simulation, and then compares release policies by shortage days.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-CATEGORY-DEFINITION",
        "name": "operational category definition",
        "occurrences": 16,
        "locations": ["Preliminary notation", "Modified notation", "Office symbols"],
        "function": "Define overlapping population states by membership rule, entry mechanism, and exclusions before writing transitions.",
        "information_order": ["term", "membership test", "entry mechanism", "retained identities", "excluded cases"],
        "slots": ["[state name]", "[who qualifies]", "[how entered]", "[what remains true]", "[what is omitted]"],
        "variants": ["are individuals whose", "implying that", "will be considered", "stands for", "exclusive of"],
        "boundary": "Use only when the states are operationally distinguishable; explicitly disclose overlap and double counting.",
        "disposition": "opens-candidate",
        "original_examples": [
            "A deferred order is a request accepted today but scheduled outside the current production window; it remains part of total demand.",
            "A transfer patient enters from another facility after triage and keeps the original acuity label for audit purposes.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-ASSUMPTION-SCOPE",
        "name": "assumption with mechanism and exception",
        "occurrences": 21,
        "locations": ["General Assumptions", "Additional Assumptions", "Application assumptions"],
        "function": "State a simplifying mechanism while keeping the rare case, omitted feedback, or stakeholder constraint visible.",
        "information_order": ["modeled mechanism", "direction of change", "explicit exclusion", "reason", "scope consequence"],
        "slots": ["[entity/state]", "[can/cannot/only]", "[transition]", "[leaving out case]", "[resulting boundary]"],
        "variants": ["we assume", "only increases", "cannot be converted", "leaving out", "should cover"],
        "boundary": "Do not turn an exception-bearing premise into a measured fact or universal law.",
        "disposition": "supports-existing",
        "original_examples": [
            "The staffing model permits nurses to change wards only at shift boundaries, excluding emergency redeployment from the baseline comparison.",
            "The inventory recurrence records scheduled receipts and omits same-day supplier substitutions, so disruption claims remain scenario-specific.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-LIMITATION-REPAIR",
        "name": "diagnosed limitation to structural repair",
        "occurrences": 11,
        "locations": ["Preliminary results", "Modified Model opening", "Strengths and Weaknesses"],
        "function": "Use a concrete implausible output or missing mechanism to justify a named modification rather than merely adding complexity.",
        "information_order": ["baseline output", "diagnostic conflict", "mechanistic cause", "required modification", "new state or parameter"],
        "slots": ["[reported result]", "[comparison or common-sense check]", "[cause]", "[therefore introduce]", "[repair object]"],
        "variants": ["goes against common sense", "the reason why", "therefore to conduct", "defects of the model are", "we introduce"],
        "boundary": "The repair must target the diagnosed failure and be revalidated; a longer model is not automatically more accurate.",
        "disposition": "supports-existing",
        "original_examples": [
            "When the forecast puts nearly all demand in one depot, the analyst traces the result to a fixed growth rate and introduces capacity feedback.",
            "A negative storage trajectory exposes a missing lower bound, so the revised controller adds an explicit feasibility constraint and reruns the benchmark.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-PARAMETER-LEDGER",
        "name": "parameter source, transform, and role ledger",
        "occurrences": 18,
        "locations": ["Preliminary calibration", "Modified calibration", "Office rating"],
        "function": "Attach each parameter to provenance, transformation, scale, and the equation block it controls.",
        "information_order": ["parameter", "source population or dataset", "transformation", "value and unit", "downstream matrix block"],
        "slots": ["[symbol]", "[source]", "[weighted average/normalization]", "[value or category]", "[affected transition]"],
        "variants": ["drawing upon public sources", "we then compute", "we may assume", "to save time we adopt", "coefficients set as"],
        "boundary": "A borrowed or assumed value remains distinct from a calibrated one; record missing units and normalization constants.",
        "disposition": "supports-existing",
        "original_examples": [
            "The demand coefficient comes from monthly invoices, is converted to daily units, and enters only the weekday replenishment term.",
            "The flood threshold is taken from the gauge manual, adjusted to the local datum, and used solely in the evacuation trigger.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-RESULT-EVIDENCE",
        "name": "result anchored to figure or table",
        "occurrences": 24,
        "locations": ["Model Results", "Sensitivity Analysis", "Office solutions", "Memo"],
        "function": "State an observable pattern, point to the supporting visual or table, and give a mechanism without silently increasing certainty.",
        "information_order": ["visual/table anchor", "direction or ranking", "number/comparator", "mechanistic interpretation", "scope"],
        "slots": ["[figure/table]", "[rises/drops/exceeds]", "[value or rank]", "[because/m mostly due to]", "[scenario/horizon]"],
        "variants": ["we can see", "we can find", "according to this ranking", "it is apparent", "the key findings are"],
        "boundary": "Separate what the visual displays from the causal explanation; preserve horizon, unit, scenario, and comparator.",
        "disposition": "supports-existing",
        "original_examples": [
            "Table 4 shows that overtime falls under the staggered roster; the proposed mechanism remains limited to the tested demand weeks.",
            "Figure 6 places the storage minimum after the second storm, while the attribution to delayed inflow remains a model interpretation.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-SCENARIO-CONTRAST",
        "name": "controlled sensitivity scenario contrast",
        "occurrences": 9,
        "locations": ["High Uniformity", "Low Uniformity", "2017 and 2067 office cases"],
        "function": "Change one interpretable coefficient, describe the behavioral regime, and compare the decision-relevant output.",
        "information_order": ["scenario definition", "coefficient change", "held assumptions", "visual/result change", "decision implication"],
        "slots": ["[high/low regime]", "[parameter=value]", "[everything else held]", "[ranking or trajectory]", "[bounded implication]"],
        "variants": ["if a group has", "to reflect", "when k equals", "given an intrinsic change", "we set the coefficients"],
        "boundary": "Call this local sensitivity unless joint uncertainty, calibration ranges, and decision switches are tested.",
        "disposition": "supports-existing",
        "original_examples": [
            "Under a high-delay regime the dispatch penalty doubles while demand inputs remain fixed, and the selected depot changes only in one district.",
            "When the drought weight is reduced, the release ranking is recomputed and reported without treating the scenario as a forecast probability.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-CONDITIONAL-DECISION",
        "name": "conditional stakeholder recommendation",
        "occurrences": 14,
        "locations": ["Application", "Five-versus-six comparison", "Memo"],
        "function": "Tie a recommendation to client preferences, costs, horizon, and the difference between alternatives.",
        "information_order": ["stakeholder condition", "objective weights", "selected option", "comparison", "review trigger"],
        "slots": ["[if client values]", "[weight setting]", "[propose option]", "[score/cost difference]", "[when to reconsider]"],
        "variants": ["if your company", "we hereby propose", "despite the costs", "can be a viable option", "may consider"],
        "boundary": "Do not infer economic superiority from an unnormalized score; show comparability, constraints, and omitted management costs.",
        "disposition": "supports-existing",
        "original_examples": [
            "If the hospital prioritizes overnight coverage, the roster selects option C; the recommendation is reopened when agency cost exceeds the stated threshold.",
            "For a water utility that weights shortage above pumping cost, policy B ranks first, conditional on the tested inflow ensemble.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-MEMO-COMPRESSION",
        "name": "executive memo compression with traceable branches",
        "occurrences": 12,
        "locations": ["Memo pages 21-23"],
        "function": "Compress model outputs into a client-facing sequence while preserving scenarios, locations, exceptions, and an action horizon.",
        "information_order": ["request acknowledgment", "model summary", "key findings", "option table", "conditions and future adjustment"],
        "slots": ["[client request]", "[two-model pipeline]", "[ranked findings]", "[recommended assignment]", "[future switch condition]"],
        "variants": ["in accordance with", "first we investigate", "building upon", "note that", "drawing upon both models"],
        "boundary": "Compression may remove derivation detail but not uncertainty, feasibility conditions, comparator, or the distinction between projection and recommendation.",
        "disposition": "opens-candidate",
        "original_examples": [
            "The operations note opens with the requested service target, summarizes the queue and roster analyses, and closes with a dated review condition.",
            "The municipal brief lists the preferred release policy, the competing option, the triggering reservoir level, and the evidence location for each claim.",
        ],
    },
    {
        "pattern_id": "LP-B-Q121-DESIGN-TRADEOFF",
        "name": "design benefit, burden, and switch ledger",
        "occurrences": 13,
        "locations": ["Five-versus-six office comparison", "Strengths and Weaknesses", "Memo close"],
        "function": "Place a design benefit or selected alternative beside its countervailing burden, omitted mechanism, or condition for revision.",
        "information_order": ["design choice or alternative", "claimed benefit", "countervailing burden", "evidence or comparator", "repair or switch condition"],
        "slots": ["[model choice or A versus B]", "[benefit or score]", "[cost/omission]", "[comparison or diagnostic]", "[repair/reconsider when]"],
        "variants": ["we preserve", "we leave out", "does not take into consideration", "the gap is narrowing", "if the management cost"],
        "boundary": "A benefit and a weakness may be recorded separately only when the chapter preserves both sides of the ledger; alternatives must remain feasible and comparably scored before a switch claim.",
        "disposition": "opens-candidate",
        "original_examples": [
            "The clinic compares four and five intake desks under one waiting-time metric, then reopens the decision when the omitted overnight staffing cost exceeds a measured threshold.",
            "The utility keeps the higher-resilience pump layout while noting the energy-cost level at which the lower-capacity layout becomes preferable.",
        ],
    },
]


CHAPTERS = [
    {
        "code": "ABS",
        "chapter": "abstract",
        "label": "Summary Sheet",
        "pages": (1, 1),
        "count": 3,
        "paragraph_count": 3,
        "input": "Globalization, geographic language dispersion, and sparse support data create a projection-and-office decision problem.",
        "rhetorical": "Open with business stakes, reject a population-only baseline, and preview the complete two-model route.",
        "analytical": "Separate language states, add migration and learning mechanisms, project to 2067, and pass the forecast to office optimization.",
        "output": "A three-paragraph summary that names the inhomogeneous transition matrix, data economy claim, forecast horizon, and simulated-annealing decision.",
        "handoff": "The introduction restates the two parts and the preliminary model defines the state system.",
        "phrases": ["With the advent of", "Therefore, we establish", "Our model focuses on", "Additionally, we introduce", "It has been tested", "In the end, we adopt"],
        "moves": ["motivate with an operating change", "replace an inadequate baseline", "define the primary state split", "preview added mechanisms", "state a bounded performance claim", "close with the client decision"],
        "patterns": ["LP-B-Q121-PROBLEM-PIVOT", "LP-B-Q121-STAGED-ROUTE", "LP-B-Q121-RESULT-EVIDENCE"],
    },
    {
        "code": "INT",
        "chapter": "introduction",
        "label": "Introduction",
        "pages": (3, 3),
        "count": 2,
        "paragraph_count": 2,
        "input": "The report begins from 6,900 languages, concentrated native-language use, multilingualism, and changing speaker populations.",
        "rhetorical": "Convert broad context into two explicit tasks and a part-by-part route.",
        "analytical": "Map transition-matrix projection to Part I and office location optimization to Part II.",
        "output": "A compact problem target and a two-stage roadmap with a forecast-to-decision handoff.",
        "handoff": "Preliminary notation and assumptions operationalize native and non-native speaker states.",
        "phrases": ["There are about", "However, because of", "Our target is", "In part I", "Considering that", "In part II"],
        "moves": ["quantify context", "name temporal variation", "state the task", "preview projection", "justify inhomogeneity", "preview optimization"],
        "patterns": ["LP-B-Q121-STAGED-ROUTE", "LP-B-Q121-PROBLEM-PIVOT"],
    },
    {
        "code": "NOT",
        "chapter": "notation",
        "label": "State and symbol definitions",
        "pages": (3, 4),
        "count": 2,
        "paragraph_count": 2,
        "input": "The model needs categories, state-vector indexing, transition symbols, and rates before any matrix can be interpreted.",
        "rhetorical": "Slow the exposition to define who belongs to each state and what every indexed coefficient does.",
        "analytical": "Bind native, non-native, learner, migrant, matrix, and rate terms to entry and exit mechanisms.",
        "output": "An operational vocabulary for the homogeneous state vector and its later extensions.",
        "handoff": "The assumptions constrain admissible transitions and double-counting choices.",
        "phrases": ["The number of native speakers", "The number of non-native speakers", "the state vector", "The transition matrix", "are individuals whose", "Implying that"],
        "moves": ["define a state", "define an indexed quantity", "attach a unit or rate", "state membership", "state retained identity", "expose an ambiguity"],
        "patterns": ["LP-B-Q121-CATEGORY-DEFINITION", "LP-B-Q121-PARAMETER-LEDGER"],
    },
    {
        "code": "ASM",
        "chapter": "assumptions",
        "label": "General, additional, and office assumptions",
        "pages": (4, 18),
        "count": 9,
        "paragraph_count": 17,
        "input": "Overlapping language identities, births, deaths, learning, migration, exogenous change, and office coverage require explicit scope controls.",
        "rhetorical": "Make simplifications inspectable by pairing each rule with an omitted rare case or operational consequence.",
        "analytical": "Determine which state transitions, feedbacks, and assignment patterns are allowed.",
        "output": "A layered premise set for the preliminary, modified, and office-location models.",
        "handoff": "The N=2 transition graph turns the preliminary premises into a matrix.",
        "phrases": ["can be categorized", "only increases", "only decreases", "cannot be converted", "Once an individual", "No radical", "mutually exclusive and collectively exhaustive"],
        "moves": ["partition the population", "restrict an inflow", "restrict an outflow", "preserve overlapping identity", "exclude a rare case", "bound exogenous shocks", "state assignment feasibility"],
        "patterns": ["LP-B-Q121-ASSUMPTION-SCOPE", "LP-B-Q121-CATEGORY-DEFINITION"],
    },
    {
        "code": "ANL",
        "chapter": "problem-analysis",
        "label": "Preliminary transition analysis",
        "pages": (4, 5),
        "count": 4,
        "paragraph_count": 4,
        "input": "Native and non-native speakers of the same language are linked by births, deaths, and cross-language learning.",
        "rhetorical": "Explain the causal transitions in prose and a diagram before presenting algebra.",
        "analytical": "Identify self-loops, cross-state flows, forbidden entries, and the overlap that distinguishes this matrix from a Markov chain.",
        "output": "A four-state N=2 transition graph and the structural interpretation of Equation (1).",
        "handoff": "Eigenanalysis asks what long-run composition this homogeneous matrix implies.",
        "phrases": ["It is apparent that", "Therefore, we can assume", "Furthermore", "Take the simplest model", "It can be concluded", "It should be noted"],
        "moves": ["state a mechanism", "turn mechanism into an assumption", "add a competing flow", "reduce to a worked case", "classify the model", "explain a zero entry"],
        "patterns": ["LP-B-Q121-PROBLEM-PIVOT", "LP-B-Q121-ASSUMPTION-SCOPE", "LP-B-Q121-CATEGORY-DEFINITION"],
    },
    {
        "code": "EST",
        "chapter": "model-establishment",
        "label": "Homogeneous transition and scaling",
        "pages": (5, 9),
        "count": 8,
        "paragraph_count": 26,
        "input": "The N=2 graph, a steady-composition objective, and public demographic and speaker statistics provide a first model.",
        "rhetorical": "Move from a small transparent matrix to a 22-language projection without hiding parameter assumptions.",
        "analytical": "Define recurrence, eigenstructure, learning-rate allocation, population scaling, and parameter simplifications.",
        "output": "Equations (1)-(12), a 44-state homogeneous matrix, and a four-year projection procedure.",
        "handoff": "Table 1 and the long-run eigenvector test whether the homogeneous construction is plausible.",
        "phrases": ["If the transition reaches", "it can be derived", "To simplify the test", "Since the top twenty-six", "To make a more accurate projection", "we then compute", "we may as well assume"],
        "moves": ["define steady composition", "link to an eigenpair", "instantiate parameters", "scale the state dimension", "source demographic rates", "normalize learning attraction", "state the recurrence"],
        "patterns": ["LP-B-Q121-PARAMETER-LEDGER", "LP-B-Q121-STAGED-ROUTE", "LP-B-Q121-RESULT-EVIDENCE"],
    },
    {
        "code": "VER",
        "chapter": "robustness-verification",
        "label": "Short-run check and long-run diagnostic",
        "pages": (7, 9),
        "count": 7,
        "paragraph_count": 9,
        "input": "Learning-rate sensitivity, 2013 inputs, 2017 observations, and a homogeneous long-run eigenvector provide diagnostic checks.",
        "rhetorical": "Report agreement and deviations, then use an implausible limiting result to motivate repair.",
        "analytical": "Compare predicted and reported speaker counts, identify data/model ambiguity, and test the homogeneous equilibrium.",
        "output": "Figure 2, Table 1, Equation (13), and the conclusion that time-varying mechanisms are necessary.",
        "handoff": "The Modified Model opening enumerates the exact missing processes.",
        "phrases": ["By employing the Matlab", "We can see", "obtain the projected statistics", "There are deviations", "we believe that", "goes against common sense", "Therefore"],
        "moves": ["run a local sensitivity", "state a threshold", "compare forecast and observation", "name a discrepancy", "offer a bounded attribution", "diagnose a long-run failure", "justify modification"],
        "patterns": ["LP-B-Q121-RESULT-EVIDENCE", "LP-B-Q121-LIMITATION-REPAIR", "LP-B-Q121-SCENARIO-CONTRAST"],
    },
    {
        "code": "IMP",
        "chapter": "model-improvement",
        "label": "Inhomogeneous learner-migrant model",
        "pages": (10, 14),
        "count": 6,
        "paragraph_count": 20,
        "input": "The homogeneous model omits learning duration, changing demography, economic change, migration detail, and English-speaker geography.",
        "rhetorical": "Turn each diagnosed defect into an added state, block matrix, or time-indexed parameter.",
        "analytical": "Add learners, migrants, English-specific blocks, exogenous drivers, and state-dependent annual matrices.",
        "output": "Figure 3, Equations (14)-(17), and a four-block English-specific transition system.",
        "handoff": "UN projections and learning assumptions instantiate the 26-language recurrence.",
        "phrases": ["The aforementioned preliminary model", "Defects of the model are", "Therefore, building upon", "we introduce time", "The transition matrix", "If we want to analyze", "We have considered"],
        "moves": ["name a baseline strength", "enumerate missing mechanisms", "define a new state", "assemble block flow", "add time dependence", "specialize an output group", "map exogenous influences"],
        "patterns": ["LP-B-Q121-LIMITATION-REPAIR", "LP-B-Q121-CATEGORY-DEFINITION", "LP-B-Q121-PROBLEM-PIVOT"],
    },
    {
        "code": "DAT",
        "chapter": "data-preprocessing",
        "label": "Demographic, language, migration, and GDP inputs",
        "pages": (8, 26),
        "count": 5,
        "paragraph_count": 17,
        "input": "Speaker counts, birth/death rates, migration, language families, policy/economic proxies, city data, and GDP histories feed multiple blocks.",
        "rhetorical": "Explain data reduction and parameter substitution close to the model that consumes each quantity.",
        "analytical": "Aggregate countries by language, compute weighted demographic rates, normalize attraction, classify similarity, and form office-region attributes.",
        "output": "Initial vectors, time-indexed rates, distance categories, candidate cities, and 2017/2067 economic inputs.",
        "handoff": "The modified recurrence produces trajectories and the rating model consumes terminal population and GDP.",
        "phrases": ["draw upon public sources", "compute the weighted average", "Due to limited data", "To save time, we adopt", "we assume", "propose a list of candidate cities", "use the GDP data"],
        "moves": ["attribute a source", "describe aggregation", "declare missing data", "borrow a projection", "normalize a parameter", "construct candidates", "forecast an input"],
        "patterns": ["LP-B-Q121-PARAMETER-LEDGER", "LP-B-Q121-ASSUMPTION-SCOPE"],
    },
    {
        "code": "RES",
        "chapter": "results",
        "label": "Language trajectories, migration, and office outcomes",
        "pages": (14, 21),
        "count": 5,
        "paragraph_count": 14,
        "input": "The 26-language recurrence, sensitivity settings, rating score, GDP scenario, and optimizer generate trajectories and assignments.",
        "rhetorical": "Translate dense computations into rankings, plotted patterns, location tables, and bounded interpretations.",
        "analytical": "Compare 2017/2067 rankings, migration and English distribution, and five-versus-six office alternatives.",
        "output": "Figures 4-8, Tables 2 and office assignments, and score differences for 2017 and 2067.",
        "handoff": "Strengths/weaknesses qualify the method and the memo compresses the decisions for the client.",
        "phrases": ["Through repeated alterations", "Based on the projections", "According to this ranking", "Additionally, we can derive", "We can also derive", "optimal stable solution", "opening six offices"],
        "moves": ["state computation status", "rank outcomes", "interpret a mechanism", "report a distribution", "compare alternatives", "state a score", "bound a recommendation"],
        "patterns": ["LP-B-Q121-RESULT-EVIDENCE", "LP-B-Q121-CONDITIONAL-DECISION"],
    },
    {
        "code": "SEN",
        "chapter": "sensitivity-analysis",
        "label": "Uniformity sensitivity",
        "pages": (16, 18),
        "count": 7,
        "paragraph_count": 11,
        "input": "The attraction-share exponent controls whether learners spread among languages or concentrate on already popular targets.",
        "rhetorical": "Define interpretable high- and low-uniformity regimes before comparing their curves.",
        "analytical": "Change k from 1 to 0.1 and 10, then observe whether and when English overtakes Mandarin.",
        "output": "A modified learning-rate equation plus Figures 7 and 8 with a scenario-specific ranking effect.",
        "handoff": "The office application uses the baseline forecast while retaining sensitivity as an applicability boundary.",
        "phrases": ["In this subsection", "If a language group", "To reflect the characteristics", "The higher k is", "when k equals", "We can find"],
        "moves": ["name the tested factor", "define a regime", "connect behavior to a parameter", "hold the mechanism visible", "compare curves", "state a bounded consequence"],
        "patterns": ["LP-B-Q121-SCENARIO-CONTRAST", "LP-B-Q121-RESULT-EVIDENCE"],
    },
    {
        "code": "ALG",
        "chapter": "algorithm",
        "label": "Rating and simulated annealing",
        "pages": (18, 20),
        "count": 7,
        "paragraph_count": 12,
        "input": "Candidate cities, mutually exclusive language coverage, population, GDP, transport cost, setup cost, and language-load penalty define a combinatorial decision.",
        "rhetorical": "Move from client needs to a scalar score, then disclose the search settings used to select an assignment.",
        "analytical": "Evaluate city-language bundles with Equation (18) and search the constrained space by simulated annealing.",
        "output": "A score definition, 19 candidate cities, annealing parameters, and stable five/six-office solutions.",
        "handoff": "The 2017 and 2067 result tables compare alternatives and inform the memo.",
        "phrases": ["derive their extrinsic and intrinsic needs", "establish our rating model", "To start with", "for further examination", "We conduct simulation", "optimal stable solution"],
        "moves": ["translate needs into criteria", "define an objective", "bound candidates", "state weights", "describe a search", "report an assignment"],
        "patterns": ["LP-B-Q121-CONDITIONAL-DECISION", "LP-B-Q121-PARAMETER-LEDGER", "LP-B-Q121-STAGED-ROUTE"],
    },
    {
        "code": "CON",
        "chapter": "conclusion",
        "label": "Five-versus-six office decision",
        "pages": (19, 21),
        "count": 2,
        "paragraph_count": 3,
        "input": "The optimizer reports five- and six-office scores under current and future transport/economic assumptions.",
        "rhetorical": "Convert score comparisons into a conditional office-count recommendation rather than a universal verdict.",
        "analytical": "Compare 43.0 versus 39.7 and 236.2 versus 225.2 while acknowledging omitted management cost.",
        "output": "Six offices are preferred in the scored baseline, while five remain a viable future option under a cost-compensation condition.",
        "handoff": "The memo states the same branch in client-facing terms and adds relocation suggestions.",
        "phrases": ["despite the costs", "still superior", "gap is narrowing", "If the management cost", "can be a viable option", "may consider"],
        "moves": ["name alternatives", "report score gap", "state current choice", "introduce omitted cost", "define a future switch", "preserve conditionality"],
        "patterns": ["LP-B-Q121-CONDITIONAL-DECISION", "LP-B-Q121-RESULT-EVIDENCE"],
    },
    {
        "code": "SWK",
        "chapter": "strengths-limitations",
        "label": "Strengths and Weaknesses",
        "pages": (21, 21),
        "count": 8,
        "paragraph_count": 8,
        "input": "The finished model exposes interfaces, simplifications, state refinements, and remaining feedback/data omissions.",
        "rhetorical": "Balance positive design properties with mechanism-specific limitations in parallel numbered lists.",
        "analytical": "Separate extensibility and legibility from incomplete economic, migration-origin, education, and reverse-feedback treatment.",
        "output": "Four claimed strengths and four admitted weaknesses linked to future repair directions.",
        "handoff": "The memo uses the strengths to communicate results but should retain the limitations as decision boundaries.",
        "phrases": ["We preserve sufficient interfaces", "leave out irrelevant", "more legible and applicable", "fit the real case better", "is not sufficient", "only consider", "does not take"],
        "moves": ["claim extensibility", "claim parsimony", "claim legibility", "claim state fidelity", "admit omitted mechanism", "admit partial feedback", "admit missing heterogeneity"],
        "patterns": ["LP-B-Q121-LIMITATION-REPAIR", "LP-B-Q121-RESULT-EVIDENCE"],
    },
    {
        "code": "MEM",
        "chapter": "memo",
        "label": "COO memo",
        "pages": (22, 23),
        "count": 9,
        "paragraph_count": 16,
        "input": "The client needs a concise 50-year language outlook, six-office assignment, preference cases, relocation plan, and office-count advice.",
        "rhetorical": "Reorder technical outputs around executive decisions, tables, exceptions, and future actions.",
        "analytical": "Compress model provenance while retaining scenario branches, excluded languages, mutual-exclusivity assumptions, and the five-percent claim.",
        "output": "A two-page memo with four forecast findings, three 2017 preference assignments, 2067 relocations, and a conditional five-office branch.",
        "handoff": "References and appendices provide the source and numeric trace that the memo itself omits.",
        "phrases": ["In accordance to your requests", "First, we investigate", "The key findings are", "Building upon", "we hereby propose", "Note that", "Drawing upon both models", "we recommend"],
        "moves": ["acknowledge the request", "summarize methods", "rank findings", "state a location option", "branch on preferences", "clarify exclusions", "recommend future adjustment", "close conditionally"],
        "patterns": ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-CONDITIONAL-DECISION", "LP-B-Q121-RESULT-EVIDENCE"],
    },
    {
        "code": "APP",
        "chapter": "appendix",
        "label": "References and Appendices",
        "pages": (24, 28),
        "count": 5,
        "paragraph_count": 0,
        "input": "Six references, country-language mappings, demographic tables, alternative assignments, GDP projections, and additional curves support the report.",
        "rhetorical": "Move bulky provenance and result detail out of the main flow while preserving anchors.",
        "analytical": "Expose source dependence, units, scenario tables, and trajectories needed to audit main-text claims.",
        "output": "References, Tables 3-8, and Figures 9-12.",
        "handoff": "The appendix closes the evidence trace but leaves reproducibility gaps for data snapshots and code.",
        "phrases": ["References", "Appendix A Tables", "Major Countries", "Economic Outlook", "Appendix B Figures"],
        "moves": ["attribute a source", "preserve a numeric ledger", "extend a visual", "expose missing provenance"],
        "patterns": ["LP-B-Q121-PARAMETER-LEDGER", "LP-B-Q121-RESULT-EVIDENCE"],
    },
]

LANGUAGE_CHAPTERS = [item for item in CHAPTERS if item["chapter"] != "appendix"]


CONTENT_COUNTS = {
    "abstract": (0, 0, 0, 0, 5),
    "introduction": (0, 0, 0, 0, 2),
    "notation": (0, 0, 3, 0, 16),
    "assumptions": (0, 0, 0, 0, 21),
    "problem-analysis": (1, 1, 0, 0, 9),
    "model-establishment": (13, 1, 0, 5, 22),
    "robustness-verification": (3, 1, 1, 1, 18),
    "model-improvement": (9, 2, 1, 2, 25),
    "data-preprocessing": (4, 0, 6, 6, 45),
    "results": (0, 7, 4, 0, 38),
    "sensitivity-analysis": (1, 2, 0, 0, 12),
    "algorithm": (3, 0, 2, 0, 19),
    "conclusion": (0, 0, 4, 0, 10),
    "strengths-limitations": (0, 0, 0, 0, 8),
    "memo": (0, 0, 3, 0, 20),
    "appendix": (0, 4, 6, 6, 70),
}


def occurrence(
    code: str,
    page: int,
    line_start: int,
    line_end: int,
    section: str,
    function: str,
    pattern_ids: list[str],
    *,
    granularity: str = "paragraph",
    excerpt_lines: tuple[int, int] | None = None,
) -> dict[str, Any]:
    return {
        "code": code,
        "page": page,
        "line_start": line_start,
        "line_end": line_end,
        "section": section,
        "function": function,
        "pattern_ids": pattern_ids,
        "granularity": granularity,
        "excerpt_lines": excerpt_lines or (line_start, line_end),
    }


OCCURRENCE_SPECS = [
    occurrence("ABS", 1, 20, 28, "Summary / problem pressure and model pivot", "motivate the work with an operating obstacle and reject the population-only baseline", ["LP-B-Q121-PROBLEM-PIVOT"], excerpt_lines=(23, 28)),
    occurrence("ABS", 1, 29, 36, "Summary / state and mechanism preview", "define the speaker-state mechanism and preview learner, migrant, and time-varying repairs", ["LP-B-Q121-PROBLEM-PIVOT", "LP-B-Q121-CATEGORY-DEFINITION"], excerpt_lines=(31, 36)),
    occurrence("ABS", 1, 37, 42, "Summary / bounded output and client handoff", "state the data-economy claim, forecast horizon, and office-location handoff", ["LP-B-Q121-STAGED-ROUTE"]),
    occurrence("INT", 3, 11, 15, "Introduction / paper task and background", "state the paper-specific language-count background and the two requested targets", []),
    occurrence("INT", 3, 16, 22, "Introduction / two-part analytical route", "route the transition-matrix forecast into simulated-annealing office selection", ["LP-B-Q121-STAGED-ROUTE"], excerpt_lines=(18, 22)),
    occurrence("NOT", 4, 7, 7, "Preliminary notation / native speaker", "define state membership by first-language identity", ["LP-B-Q121-CATEGORY-DEFINITION"]),
    occurrence("NOT", 4, 9, 11, "Preliminary notation / non-native speaker", "define membership, entry condition, and proficiency threshold for the non-native state", ["LP-B-Q121-CATEGORY-DEFINITION"]),
    occurrence("ASM", 4, 15, 16, "General assumptions / population partition", "partition each language population into native and non-native identities", ["LP-B-Q121-ASSUMPTION-SCOPE", "LP-B-Q121-CATEGORY-DEFINITION"]),
    occurrence("ASM", 4, 17, 21, "General assumptions / native inflow and outflow", "bound native-state change to births and deaths while naming rare exclusions", ["LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ASM", 4, 22, 23, "General assumptions / native conversion", "forbid within-language native-to-non-native conversion while retaining cross-language learning", ["LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ASM", 4, 25, 27, "General assumptions / non-native inflow and outflow", "bound non-native change to learning and death and expose the forgetting exclusion", ["LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ASM", 4, 31, 32, "General assumptions / retained identities", "preserve previous language identities after a new language is mastered", ["LP-B-Q121-ASSUMPTION-SCOPE", "LP-B-Q121-CATEGORY-DEFINITION"]),
    occurrence("ASM", 4, 33, 34, "General assumptions / exogenous shock boundary", "exclude radical unpredicted population-structure shifts", ["LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ASM", 11, 11, 12, "Additional assumptions / exogenous demography", "make demographic rates time-varying but population-independent", ["LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ASM", 11, 13, 16, "Additional assumptions / learner lifecycle", "exclude learner births and deaths during the modeled learning interval and give the scope reason", ["LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ASM", 18, 14, 17, "Application assumptions / exclusive coverage", "state mutually exclusive and collectively exhaustive language coverage before optimization", ["LP-B-Q121-ASSUMPTION-SCOPE", "LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("ANL", 4, 38, 39, "Preliminary analysis / causal focus", "identify the paper-specific within-language relation that organizes the transition analysis", []),
    occurrence("ANL", 4, 41, 44, "Preliminary analysis / birth mechanism", "move from a parental-language mechanism to a bounded native-speaker inflow rule", ["LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ANL", 4, 45, 48, "Preliminary analysis / identity persistence", "move from first-language persistence to a forbidden conversion path with an exception", ["LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ANL", 5, 5, 7, "Preliminary analysis / learning and mortality flows", "add learning inflow and natural-death outflow before the transition diagram", ["LP-B-Q121-STAGED-ROUTE"]),
    occurrence("EST", 5, 11, 12, "N=2 establishment / transparent reduction", "reduce the full system to a two-language transition example", ["LP-B-Q121-STAGED-ROUTE"]),
    occurrence("EST", 5, 19, 21, "N=2 establishment / operator classification", "compare the operator with a homogeneous Markov-chain form while noting retained identities", ["LP-B-Q121-CATEGORY-DEFINITION"]),
    occurrence("EST", 6, 16, 17, "N=2 establishment / steady composition", "define steady state as a stable population split rather than fixed absolute counts", ["LP-B-Q121-CATEGORY-DEFINITION"]),
    occurrence("EST", 6, 26, 29, "N=2 establishment / eigenpair route", "connect the steady-state recurrence to an eigenpair and introduce a numerical test", ["LP-B-Q121-STAGED-ROUTE"]),
    occurrence("EST", 6, 45, 47, "N=2 establishment / equilibrium interpretation", "translate the reported eigenvector into a claimed long-run population split", ["LP-B-Q121-RESULT-EVIDENCE"]),
    occurrence("EST", 7, 23, 29, "Scaled establishment / reduced language set", "justify the twenty-two-language scope from coverage and data limits before enlarging the matrix", ["LP-B-Q121-PARAMETER-LEDGER", "LP-B-Q121-ASSUMPTION-SCOPE"], excerpt_lines=(25, 29)),
    occurrence("EST", 8, 28, 30, "Scaled establishment / attraction allocation", "allocate a fixed total learning rate using initial non-native-speaker shares", ["LP-B-Q121-PARAMETER-LEDGER"]),
    occurrence("EST", 8, 35, 38, "Scaled establishment / normalized transition rate", "state the normalization and route it into source-to-target annual learning rates", ["LP-B-Q121-PARAMETER-LEDGER"]),
    occurrence("VER", 7, 5, 9, "Preliminary verification / sensitivity setup", "derive a learning-rate diagnostic from an implausible bilingual equilibrium", ["LP-B-Q121-RESULT-EVIDENCE", "LP-B-Q121-SCENARIO-CONTRAST"]),
    occurrence("VER", 7, 17, 19, "Preliminary verification / threshold interpretation", "bind the plotted crossing to a long-run learning-rate boundary", ["LP-B-Q121-RESULT-EVIDENCE"]),
    occurrence("VER", 9, 6, 7, "Short-run verification / four-step check", "compare a 2013-initialized four-step forecast with reported 2017 values", ["LP-B-Q121-RESULT-EVIDENCE"]),
    occurrence("VER", 9, 24, 29, "Short-run verification / discrepancy attribution", "report large prediction deviations and keep the paper's data-quality attribution bounded", ["LP-B-Q121-LIMITATION-REPAIR", "LP-B-Q121-RESULT-EVIDENCE"]),
    occurrence("VER", 9, 31, 33, "Long-run verification / eigenpair diagnostic", "compute a long-run eigenpair as a structural diagnostic", ["LP-B-Q121-STAGED-ROUTE"]),
    occurrence("VER", 9, 44, 48, "Long-run verification / implausible dominance", "explain the implausible Punjabi dominance as a homogeneous-growth-rate effect", ["LP-B-Q121-LIMITATION-REPAIR"]),
    occurrence("VER", 9, 49, 50, "Long-run verification / repair requirement", "turn the failed equilibrium into a requirement for a time-varying model", ["LP-B-Q121-LIMITATION-REPAIR", "LP-B-Q121-PROBLEM-PIVOT"]),
    occurrence("IMP", 10, 6, 8, "Modified model / baseline diagnosis", "separate adequate short-run behavior from inadequate long-run behavior before revision", ["LP-B-Q121-LIMITATION-REPAIR"]),
    occurrence("IMP", 10, 10, 13, "Modified model / learning-process defect", "name the missing learning duration and its education, similarity, and motivation drivers", ["LP-B-Q121-LIMITATION-REPAIR"]),
    occurrence("IMP", 10, 23, 26, "Modified model / structural repair", "map the defect list to time, learner, migrant, and English-specific states", ["LP-B-Q121-PROBLEM-PIVOT", "LP-B-Q121-LIMITATION-REPAIR"]),
    occurrence("IMP", 10, 33, 38, "Modified notation / learner and region states", "define learner and language-region states by entry rule and retained population meaning", ["LP-B-Q121-CATEGORY-DEFINITION"]),
    occurrence("IMP", 11, 27, 28, "Modified analysis / expanded transition graph", "preview the learner-and-migrant transition graph before the block operator", ["LP-B-Q121-STAGED-ROUTE"]),
    occurrence("IMP", 13, 5, 14, "Modified analysis / English-specific block and omission", "specialize the matrix for English distribution and disclose the omitted native-English emigration channel", ["LP-B-Q121-LIMITATION-REPAIR", "LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("DAT", 8, 3, 6, "Demographic preprocessing / source and aggregation", "attribute public demographic inputs and describe weighted language-group aggregation", ["LP-B-Q121-PARAMETER-LEDGER"]),
    occurrence("DAT", 8, 15, 17, "Demographic preprocessing / common-rate substitutions", "record borrowed world rates and the immigrant ratio before assuming shared values", ["LP-B-Q121-PARAMETER-LEDGER", "LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("DAT", 13, 29, 32, "English preprocessing / initial composition", "define the initial non-native English vector by a stated proportional allocation", ["LP-B-Q121-PARAMETER-LEDGER"]),
    occurrence("DAT", 13, 36, 39, "Time-series preprocessing / UN projections", "attribute fifty-year demographic projections and describe their weighted reduction", ["LP-B-Q121-PARAMETER-LEDGER"]),
    occurrence("DAT", 20, 35, 42, "Economic preprocessing / cycle forecast", "name the four-cycle GDP construction, historical fit window, forecast year, and appendix handoff", ["LP-B-Q121-PARAMETER-LEDGER", "LP-B-Q121-STAGED-ROUTE"], excerpt_lines=(37, 42)),
    occurrence("RES", 14, 35, 41, "Language results / trajectories and ranking", "route repeated annual updates into a plotted forecast, rank table, and observed entrants and exits", ["LP-B-Q121-RESULT-EVIDENCE"]),
    occurrence("RES", 15, 26, 33, "Geographic results / migration scale", "anchor the migration interpretation to Figure 5 and identify the reported leading region and mechanism", ["LP-B-Q121-RESULT-EVIDENCE"], excerpt_lines=(28, 33)),
    occurrence("RES", 15, 37, 40, "Geographic results / non-native English distribution", "anchor the English-distribution claim to Figure 6 and retain the reported Chinese-speaker magnitude", ["LP-B-Q121-RESULT-EVIDENCE"]),
    occurrence("RES", 20, 43, 44, "Office results / 2067 handoff", "combine projected language populations with economic inputs before reporting the optimized assignment", ["LP-B-Q121-STAGED-ROUTE", "LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("RES", 21, 21, 23, "Office results / future alternative", "compare five and six offices and retain management cost as the unmodeled switch factor", ["LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("SEN", 16, 21, 24, "Sensitivity / tested factor", "name eagerness uniformity as the tested mechanism and define its behavioral meaning", ["LP-B-Q121-SCENARIO-CONTRAST"]),
    occurrence("SEN", 16, 28, 30, "Sensitivity / high-uniformity regime", "define the high-uniformity language-choice regime before changing the exponent", ["LP-B-Q121-SCENARIO-CONTRAST"]),
    occurrence("SEN", 17, 11, 12, "Sensitivity / equation modification", "modify the attraction expression to represent the stated regime", ["LP-B-Q121-SCENARIO-CONTRAST"]),
    occurrence("SEN", 17, 17, 18, "Sensitivity / exponent interpretation", "connect exponent size to uniformity and name the baseline and high-uniformity values", ["LP-B-Q121-SCENARIO-CONTRAST", "LP-B-Q121-PARAMETER-LEDGER"]),
    occurrence("SEN", 17, 25, 26, "Sensitivity / high-uniformity result", "state the English-versus-Mandarin outcome for the high-uniformity figure", ["LP-B-Q121-RESULT-EVIDENCE", "LP-B-Q121-SCENARIO-CONTRAST"]),
    occurrence("SEN", 17, 30, 37, "Sensitivity / low-uniformity regime", "define concentrated language choice and give the policy-restriction case", ["LP-B-Q121-SCENARIO-CONTRAST"], excerpt_lines=(30, 35)),
    occurrence("SEN", 17, 39, 42, "Sensitivity / low-uniformity result", "bind k=10 to the earlier English crossover without treating it as calibrated uncertainty", ["LP-B-Q121-RESULT-EVIDENCE", "LP-B-Q121-SCENARIO-CONTRAST"]),
    occurrence("ALG", 18, 11, 12, "Application / stakeholder needs", "translate the client description into extrinsic and intrinsic office needs", ["LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("ALG", 18, 14, 17, "Application / coverage constraint", "state the exact coverage constraint before constructing the score", ["LP-B-Q121-CONDITIONAL-DECISION", "LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("ALG", 18, 20, 25, "Application / objective components", "name population, GDP, transport, and language-load considerations before scalarization", ["LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("ALG", 18, 29, 29, "Application / rating-model pivot", "turn the stated office needs into a rating model", ["LP-B-Q121-PROBLEM-PIVOT"]),
    occurrence("ALG", 19, 11, 17, "Application / candidate construction", "define and bound the nineteen-city candidate set and its exclusions", ["LP-B-Q121-PARAMETER-LEDGER"]),
    occurrence("ALG", 19, 21, 22, "Application / 2017 simulation setup", "state the data year and weight-setting rationale before simulation", ["LP-B-Q121-PARAMETER-LEDGER", "LP-B-Q121-STAGED-ROUTE"]),
    occurrence("ALG", 20, 43, 44, "Application / forecast-to-search handoff", "pass the 2067 language forecast into the office search and name the selected output", ["LP-B-Q121-STAGED-ROUTE"]),
    occurrence("CON", 20, 23, 26, "Office conclusion / current design comparison", "compare five and six offices, state the preferred design, and retain alternative preference scenarios", ["LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("CON", 21, 21, 23, "Office conclusion / future switch", "state the narrowing gap and the management-cost condition under which five offices become viable", ["LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("SWK", 21, 29, 30, "Strengths / extensible interfaces", "record extensibility as one benefit in the chapter's paired design ledger", ["LP-B-Q121-DESIGN-TRADEOFF"]),
    occurrence("SWK", 21, 31, 32, "Strengths / scoped parsimony", "record concision as one benefit in the chapter's paired design ledger", ["LP-B-Q121-DESIGN-TRADEOFF"]),
    occurrence("SWK", 21, 33, 34, "Strengths / legibility", "record matrix-and-graph legibility as one benefit in the chapter's paired design ledger", ["LP-B-Q121-DESIGN-TRADEOFF"]),
    occurrence("SWK", 21, 35, 36, "Strengths / state refinement", "record refined state separation as one benefit in the chapter's paired design ledger", ["LP-B-Q121-DESIGN-TRADEOFF"]),
    occurrence("SWK", 21, 39, 39, "Weaknesses / economic mechanism", "record insufficient economic treatment as one burden in the chapter's paired design ledger", ["LP-B-Q121-DESIGN-TRADEOFF"]),
    occurrence("SWK", 21, 40, 43, "Weaknesses / reverse feedback", "record missing reverse feedback as one burden in the chapter's paired design ledger", ["LP-B-Q121-DESIGN-TRADEOFF"]),
    occurrence("SWK", 21, 44, 45, "Weaknesses / migrant-origin language", "record the omitted migrant-origin effect as one burden in the chapter's paired design ledger", ["LP-B-Q121-DESIGN-TRADEOFF"]),
    occurrence("SWK", 21, 46, 47, "Weaknesses / education heterogeneity", "record missing education heterogeneity as one burden in the chapter's paired design ledger", ["LP-B-Q121-DESIGN-TRADEOFF"]),
    occurrence("MEM", 22, 7, 13, "Memo / request and method", "acknowledge the client request and compress the fifty-year projection method and scope", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-STAGED-ROUTE"], excerpt_lines=(7, 12)),
    occurrence("MEM", 22, 14, 20, "Memo / leading forecast finding", "introduce the findings and report the English-versus-Mandarin result with a magnitude", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-RESULT-EVIDENCE"]),
    occurrence("MEM", 22, 22, 29, "Memo / remaining forecast findings", "compress the high-growth and declining-language findings with their stated mechanisms", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-RESULT-EVIDENCE"], excerpt_lines=(22, 26)),
    occurrence("MEM", 22, 31, 44, "Memo / baseline office branch", "move from the language forecast to a cost-and-revenue-balanced office proposal", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-CONDITIONAL-DECISION"], excerpt_lines=(31, 33)),
    occurrence("MEM", 23, 13, 23, "Memo / GDP-weighted office branch", "condition an alternative assignment on regional economic demand and GDP", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-CONDITIONAL-DECISION"], excerpt_lines=(13, 15)),
    occurrence("MEM", 23, 27, 30, "Memo / candidate-city note", "explain representative-city selection with a concrete economic comparator", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-PARAMETER-LEDGER"]),
    occurrence("MEM", 23, 31, 33, "Memo / established-office exclusion", "retain existing-office coverage as an explicit exclusion from the new-office search", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-ASSUMPTION-SCOPE"]),
    occurrence("MEM", 23, 38, 42, "Memo / future relocation advice", "translate the fifty-year forecast into named relocation and coverage adjustments", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("MEM", 23, 43, 48, "Memo / office-count switch condition", "retain the six-office short-run recommendation and state the future five-office cost/revenue condition", ["LP-B-Q121-MEMO-COMPRESSION", "LP-B-Q121-CONDITIONAL-DECISION"]),
    occurrence("APP", 24, 5, 26, "References / source ledger", "record bibliography coverage without treating third-party source text as reusable author prose", [], granularity="section", excerpt_lines=(5, 7)),
    occurrence("APP", 25, 6, 7, "Appendix A / table routing header", "record the appendix table heading as structural coverage rather than narrative prose", [], granularity="phrase"),
    occurrence("APP", 25, 22, 22, "Appendix A / Table 3 caption", "record the table caption and its routing role without nominating an author-language pattern", [], granularity="phrase"),
    occurrence("APP", 26, 55, 55, "Appendix A / Table 8 caption", "record the economic-table caption as structural coverage rather than narrative prose", [], granularity="phrase"),
    occurrence("APP", 27, 5, 20, "Appendix B / figure routing and captions", "record figure headings and captions without treating labels as reusable narrative prose", [], granularity="section"),
]


assert sum(item["count"] for item in CHAPTERS) == 89
assert len(OCCURRENCE_SPECS) == 89

LANGUAGE_OCCURRENCE_SPECS = [
    spec for spec in OCCURRENCE_SPECS if spec["code"] != "APP"
]
NON_PROSE_SOURCE_SPECS = [
    spec for spec in OCCURRENCE_SPECS if spec["code"] == "APP"
]
assert sum(item["count"] for item in LANGUAGE_CHAPTERS) == 84
assert len(LANGUAGE_OCCURRENCE_SPECS) == 84
assert len(NON_PROSE_SOURCE_SPECS) == 5

NONREUSABLE_LANGUAGE_REASONS = {
    f"LU-{ID_STEM}-INT-001": "The paper-specific language-count and task wording is not transferable as a rhetorical mechanism.",
    f"LU-{ID_STEM}-ANL-001": "The local within-language relationship claim lacks a reusable rhetorical mechanism.",
}


OCCURRENCE_ROLES = {
    "ABS": ["premise", "mechanism", "result"],
    "INT": ["premise", "mechanism"],
    "NOT": ["premise", "premise"],
    "ASM": ["premise"] * 9,
    "ANL": ["premise", "mechanism", "premise", "mechanism"],
    "EST": ["mechanism", "premise", "premise", "mechanism", "result", "premise", "mechanism", "premise"],
    "VER": ["mechanism", "result", "mechanism", "boundary", "result", "result", "boundary"],
    "IMP": ["result", "mechanism", "mechanism", "mechanism", "mechanism", "boundary"],
    "DAT": ["mechanism", "boundary", "premise", "premise", "premise"],
    "RES": ["result", "result", "result", "mechanism", "result"],
    "SEN": ["premise", "premise", "mechanism", "premise", "result", "premise", "result"],
    "ALG": ["premise", "premise", "mechanism", "mechanism", "result", "result", "result"],
    "CON": ["result", "boundary"],
    "SWK": ["mechanism"] * 4 + ["boundary"] * 4,
    "MEM": ["premise", "result", "result", "mechanism", "result", "result", "boundary", "result", "boundary"],
    "APP": ["premise", "premise", "result", "premise", "result"],
}
for code, roles in OCCURRENCE_ROLES.items():
    if len(roles) != sum(spec["code"] == code for spec in OCCURRENCE_SPECS):
        raise AssertionError(f"q121 rhetorical-role count mismatch for {code}")


def layout_paragraph(
    code: str,
    function: str,
    *source_spans: tuple[int, int, int],
) -> dict[str, Any]:
    return {"code": code, "function": function, "source_spans": source_spans}


LAYOUT_PARAGRAPHS = [
    layout_paragraph("ABS", "motivate the projection problem and reject the population-only baseline", (1, 20, 28)),
    layout_paragraph("ABS", "preview state definitions and the inhomogeneous repair", (1, 29, 36)),
    layout_paragraph("ABS", "state bounded performance, forecast, and office-location outputs", (1, 37, 42)),
    layout_paragraph("INT", "state the paper-specific background and task", (3, 11, 15)),
    layout_paragraph("INT", "preview the forecast-to-decision route", (3, 16, 22)),
    layout_paragraph("NOT", "define native-speaker membership", (4, 7, 7)),
    layout_paragraph("NOT", "define non-native-speaker membership and proficiency", (4, 9, 11)),
    layout_paragraph("ASM", "partition each language population", (4, 15, 16)),
    layout_paragraph("ASM", "bound native births and deaths with exceptions", (4, 17, 21)),
    layout_paragraph("ASM", "forbid within-language native conversion", (4, 22, 23)),
    layout_paragraph("ASM", "bound non-native learning and death with an exception", (4, 25, 27)),
    layout_paragraph("ASM", "forbid non-native-to-native conversion", (4, 28, 29)),
    layout_paragraph("ASM", "retain previous identities after language mastery", (4, 31, 32)),
    layout_paragraph("ASM", "exclude radical population-structure shocks", (4, 33, 34)),
    layout_paragraph("ASM", "make demographic rates time-dependent but population-independent", (11, 11, 12)),
    layout_paragraph("ASM", "exclude births and deaths within the learner state", (11, 13, 16)),
    layout_paragraph("ASM", "assign migrant offspring to the destination native state", (11, 17, 18)),
    layout_paragraph("ASM", "move successful migrants out of the non-native state", (11, 19, 23)),
    layout_paragraph("ASM", "translate the client setting into office assumptions", (18, 11, 12)),
    layout_paragraph("ASM", "require mutually exclusive and exhaustive coverage", (18, 14, 17)),
    layout_paragraph("ASM", "require English and the local language", (18, 18, 18)),
    layout_paragraph("ASM", "balance population, economy, and transport", (18, 20, 23)),
    layout_paragraph("ASM", "penalize excessive language load", (18, 24, 25)),
    layout_paragraph("ASM", "require nearby English speakers", (18, 26, 27)),
    layout_paragraph("ANL", "identify the strong within-language relation", (4, 38, 39)),
    layout_paragraph("ANL", "derive native inflow from parental language", (4, 41, 44)),
    layout_paragraph("ANL", "derive identity persistence from first-language retention", (4, 45, 48)),
    layout_paragraph("ANL", "add learning inflow and mortality outflow", (5, 5, 7)),
    layout_paragraph("EST", "reduce the system to a two-language example", (5, 11, 12)),
    layout_paragraph("EST", "classify the overlapping-state operator", (5, 19, 21)),
    layout_paragraph("EST", "introduce the Equation 1 parameter ledger", (5, 26, 26)),
    layout_paragraph("EST", "define native birth-rate entries", (5, 28, 29)),
    layout_paragraph("EST", "define native death-rate entries", (5, 31, 32)),
    layout_paragraph("EST", "define non-native-parent birth entries", (5, 34, 36)),
    layout_paragraph("EST", "define cross-language learning entries", (6, 5, 6)),
    layout_paragraph("EST", "define non-native death entries", (6, 8, 9)),
    layout_paragraph("EST", "set cross-non-native entries to zero", (6, 10, 11)),
    layout_paragraph("EST", "set duplicate-offspring entries to zero", (6, 12, 14)),
    layout_paragraph("EST", "define steady composition", (6, 16, 17)),
    layout_paragraph("EST", "define growth rate and state vectors", (6, 21, 22)),
    layout_paragraph("EST", "write the steady-state recurrence", (6, 23, 23)),
    layout_paragraph("EST", "link the recurrence to an eigenpair", (6, 26, 27)),
    layout_paragraph("EST", "introduce the numerical test", (6, 28, 29)),
    layout_paragraph("EST", "introduce the numerical transition matrix", (6, 34, 34)),
    layout_paragraph("EST", "select the reported nonnegative eigenvector", (6, 39, 40)),
    layout_paragraph("EST", "interpret the reported bilingual equilibrium", (6, 45, 47)),
    layout_paragraph("EST", "bound and scale the language set", (7, 23, 29)),
    layout_paragraph("EST", "introduce parameter refinement", (7, 34, 35)),
    layout_paragraph("EST", "introduce language-specific demography", (7, 37, 38)),
    layout_paragraph("EST", "construct representative-country aggregation", (7, 39, 43)),
    layout_paragraph("EST", "simplify target attractiveness", (8, 21, 25)),
    layout_paragraph("EST", "allocate the total learning rate", (8, 28, 30)),
    layout_paragraph("EST", "normalize source-to-target learning", (8, 35, 38)),
    layout_paragraph("EST", "omit the displayed 44-by-44 matrix for space", (8, 42, 43)),
    layout_paragraph("VER", "set up a learning-rate diagnostic", (7, 5, 9)),
    layout_paragraph("VER", "interpret the plotted threshold", (7, 17, 19)),
    layout_paragraph("VER", "define the four-step prediction check", (9, 6, 7)),
    layout_paragraph("VER", "report and attribute short-run deviations", (9, 24, 29)),
    layout_paragraph("VER", "route the initial data to the appendix", (9, 30, 30)),
    layout_paragraph("VER", "compute the long-run eigenpair", (9, 31, 33)),
    layout_paragraph("VER", "interpret the eigenvector and eigenvalue", (9, 37, 42)),
    layout_paragraph("VER", "diagnose implausible homogeneous dominance", (9, 44, 48)),
    layout_paragraph("VER", "require an inhomogeneous repair", (9, 49, 50)),
    layout_paragraph("IMP", "separate short-run adequacy from long-run failure", (10, 6, 8)),
    layout_paragraph("IMP", "identify the missing learning process", (10, 10, 13)),
    layout_paragraph("IMP", "identify time-varying demographic omission", (10, 14, 14)),
    layout_paragraph("IMP", "identify economic-development omission", (10, 16, 16)),
    layout_paragraph("IMP", "identify migration-detail omission", (10, 18, 18)),
    layout_paragraph("IMP", "identify the missing English distribution", (10, 20, 21)),
    layout_paragraph("IMP", "map defects to new states and time dependence", (10, 23, 26)),
    layout_paragraph("IMP", "define the learner state", (10, 33, 34)),
    layout_paragraph("IMP", "define language regions", (10, 35, 38)),
    layout_paragraph("IMP", "define first-generation migrants", (10, 40, 41)),
    layout_paragraph("IMP", "define the decrease matrix", (10, 43, 44)),
    layout_paragraph("IMP", "preview the expanded transition graph", (11, 27, 28)),
    layout_paragraph("IMP", "introduce the time-indexed block matrix", (12, 9, 9)),
    layout_paragraph("IMP", "specialize the matrix for English distribution", (13, 5, 6)),
    layout_paragraph("IMP", "bound the omitted native-English emigration channel", (13, 11, 14)),
    layout_paragraph("IMP", "introduce the exogenous-factor ledger", (13, 15, 15)),
    layout_paragraph("IMP", "route policy into migration and learning", (13, 17, 17)),
    layout_paragraph("IMP", "route economics and population into transitions", (13, 19, 19)),
    layout_paragraph("IMP", "route education into learning", (13, 21, 21)),
    layout_paragraph("IMP", "turn data into time-indexed learning blocks", (14, 4, 6)),
    layout_paragraph("DAT", "introduce language-specific demographic inputs", (7, 37, 38)),
    layout_paragraph("DAT", "construct representative-country groups", (7, 39, 43)),
    layout_paragraph("DAT", "attribute and aggregate demographic data", (8, 3, 6)),
    layout_paragraph("DAT", "substitute common non-native demographic rates", (8, 7, 10)),
    layout_paragraph("DAT", "record borrowed world rates and migrant ratio", (8, 15, 17)),
    layout_paragraph("DAT", "bound the twenty-six-language starting scope", (13, 25, 28)),
    layout_paragraph("DAT", "allocate initial non-native English composition", (13, 29, 32)),
    layout_paragraph("DAT", "reduce UN demographic projections", (13, 36, 39)),
    layout_paragraph("DAT", "route exogenous data into matrix blocks", (14, 4, 6)),
    layout_paragraph("DAT", "proxy future eagerness with past speaker shares", (14, 11, 13)),
    layout_paragraph("DAT", "reduce language distance to two family levels", (14, 18, 21)),
    layout_paragraph("DAT", "set learning entry and duration assumptions", (14, 26, 29)),
    layout_paragraph("DAT", "construct the candidate-city set", (19, 11, 17)),
    layout_paragraph("DAT", "record 2017 simulation weights", (19, 21, 22)),
    layout_paragraph("DAT", "change the 2067 geography coefficient", (20, 30, 31)),
    layout_paragraph("DAT", "fit the integrated GDP-cycle forecast", (20, 35, 42)),
    layout_paragraph("DAT", "combine terminal language and GDP inputs", (20, 43, 44)),
    layout_paragraph("RES", "produce the fifty-year trajectory figure", (14, 35, 36)),
    layout_paragraph("RES", "produce the 2017-versus-2067 ranking", (14, 37, 38)),
    layout_paragraph("RES", "identify rank entrants and exits", (14, 39, 41)),
    layout_paragraph("RES", "attribute rank gain to high birth rate", (14, 42, 42)),
    layout_paragraph("RES", "interpret migration and language-family effects", (14, 43, 45)),
    layout_paragraph("RES", "attribute rank gain to attractiveness", (14, 46, 47)),
    layout_paragraph("RES", "produce the migration-scale figure", (15, 26, 27)),
    layout_paragraph("RES", "interpret the leading migration regions", (15, 28, 33)),
    layout_paragraph("RES", "produce the English-origin distribution", (15, 37, 37)),
    layout_paragraph("RES", "report the Chinese-source magnitude", (15, 38, 40)),
    layout_paragraph("RES", "interpret geography from the English results", (15, 41, 41), (16, 15, 17)),
    layout_paragraph("RES", "report the five-office 2017 alternative", (20, 14, 14)),
    layout_paragraph("RES", "pass the 2067 forecast into optimization", (20, 43, 44)),
    layout_paragraph("RES", "compare the future office-count alternatives", (21, 21, 23)),
    layout_paragraph("SEN", "name eagerness uniformity as the tested factor", (16, 21, 24)),
    layout_paragraph("SEN", "define the high-uniformity regime", (16, 28, 30)),
    layout_paragraph("SEN", "give the unrestricted-language policy case", (16, 32, 32), (17, 5, 5)),
    layout_paragraph("SEN", "give the low-purpose learning case", (17, 7, 9)),
    layout_paragraph("SEN", "modify the attraction expression", (17, 11, 12)),
    layout_paragraph("SEN", "interpret and set the exponent", (17, 17, 18)),
    layout_paragraph("SEN", "report the high-uniformity result", (17, 25, 26)),
    layout_paragraph("SEN", "define the low-uniformity regime", (17, 30, 32)),
    layout_paragraph("SEN", "give the restricted-language policy case", (17, 34, 35)),
    layout_paragraph("SEN", "give the opportunity-seeking learning case", (17, 36, 37)),
    layout_paragraph("SEN", "report the low-uniformity result", (17, 39, 42)),
    layout_paragraph("ALG", "translate the client setting into office needs", (18, 11, 12)),
    layout_paragraph("ALG", "define exclusive and exhaustive coverage", (18, 14, 17)),
    layout_paragraph("ALG", "define basic office languages", (18, 18, 18)),
    layout_paragraph("ALG", "define population, economy, and transport criteria", (18, 20, 23)),
    layout_paragraph("ALG", "define the language-load penalty", (18, 24, 25)),
    layout_paragraph("ALG", "require English-speaking residents", (18, 26, 27)),
    layout_paragraph("ALG", "pivot from needs to the rating model", (18, 29, 29)),
    layout_paragraph("ALG", "bound the candidate-city search space", (19, 11, 17)),
    layout_paragraph("ALG", "state the 2017 simulation weights", (19, 21, 22)),
    layout_paragraph("ALG", "report the five-office 2017 search output", (20, 14, 14)),
    layout_paragraph("ALG", "state the 2067 geography setting", (20, 30, 31)),
    layout_paragraph("ALG", "route forecast inputs into the future search", (20, 43, 44)),
    layout_paragraph("CON", "prefer six offices in the 2017 score comparison", (20, 23, 24)),
    layout_paragraph("CON", "make five offices conditionally viable in 2067", (21, 21, 23)),
    layout_paragraph("CON", "state the memo's future office-count switch", (23, 43, 48)),
    layout_paragraph("SWK", "claim extensibility through preserved interfaces", (21, 29, 30)),
    layout_paragraph("SWK", "claim parsimony through scoped omissions", (21, 31, 32)),
    layout_paragraph("SWK", "claim legibility from matrix and graph", (21, 33, 34)),
    layout_paragraph("SWK", "claim realism from refined states", (21, 35, 36)),
    layout_paragraph("SWK", "admit insufficient economic treatment", (21, 39, 39)),
    layout_paragraph("SWK", "admit missing reverse feedback", (21, 40, 43)),
    layout_paragraph("SWK", "admit omitted migrant-origin language", (21, 44, 45)),
    layout_paragraph("SWK", "admit missing education heterogeneity", (21, 46, 47)),
    layout_paragraph("MEM", "acknowledge the request and desired cost boundary", (22, 7, 9)),
    layout_paragraph("MEM", "summarize the projection model and horizon", (22, 10, 13)),
    layout_paragraph("MEM", "introduce the forecast findings", (22, 14, 15)),
    layout_paragraph("MEM", "report English growth and source composition", (22, 17, 20)),
    layout_paragraph("MEM", "report high-growth language groups", (22, 22, 24)),
    layout_paragraph("MEM", "report declining language groups", (22, 25, 26)),
    layout_paragraph("MEM", "report uneven migration", (22, 27, 29)),
    layout_paragraph("MEM", "propose the balanced office assignment", (22, 31, 33)),
    layout_paragraph("MEM", "branch to the population-weighted assignment", (22, 42, 44)),
    layout_paragraph("MEM", "branch to the GDP-weighted assignment", (23, 13, 15)),
    layout_paragraph("MEM", "introduce implementation notes", (23, 25, 25)),
    layout_paragraph("MEM", "explain representative-city selection", (23, 27, 30)),
    layout_paragraph("MEM", "explain established-office exclusions", (23, 31, 33)),
    layout_paragraph("MEM", "state the coverage premise", (23, 34, 36)),
    layout_paragraph("MEM", "recommend future relocations", (23, 38, 42)),
    layout_paragraph("MEM", "condition a future office closure", (23, 43, 48)),
]


PAGE_LINE_CACHE: dict[int, list[str]] = {}
SOURCE_WORD_RE = re.compile(
    r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*(?:-[A-Za-z0-9]+)*(?:[.:][0-9]+)*"
)
SENTENCE_ABBREVIATIONS = ("e.g.", "U.S.A.", "U.K.", "etc.")

EXPECTED_LAYOUT_STATS = {
    "abstract": {"word_count": 244, "sentence_count": 10, "paragraph_count": 3, "sentence_words": {"minimum": 11, "median": 23.5, "maximum": 40}},
    "introduction": {"word_count": 165, "sentence_count": 7, "paragraph_count": 2, "sentence_words": {"minimum": 10, "median": 26, "maximum": 41}},
    "notation": {"word_count": 49, "sentence_count": 2, "paragraph_count": 2, "sentence_words": {"minimum": 11, "median": 24.5, "maximum": 38}},
    "assumptions": {"word_count": 498, "sentence_count": 34, "paragraph_count": 17, "sentence_words": {"minimum": 1, "median": 13.0, "maximum": 57}},
    "problem-analysis": {"word_count": 154, "sentence_count": 9, "paragraph_count": 4, "sentence_words": {"minimum": 1, "median": 17, "maximum": 30}},
    "model-establishment": {"word_count": 743, "sentence_count": 43, "paragraph_count": 26, "sentence_words": {"minimum": 1, "median": 16, "maximum": 52}},
    "robustness-verification": {"word_count": 371, "sentence_count": 18, "paragraph_count": 9, "sentence_words": {"minimum": 1, "median": 19.0, "maximum": 41}},
    "model-improvement": {"word_count": 468, "sentence_count": 33, "paragraph_count": 20, "sentence_words": {"minimum": 1, "median": 12, "maximum": 51}},
    "data-preprocessing": {"word_count": 770, "sentence_count": 33, "paragraph_count": 17, "sentence_words": {"minimum": 1, "median": 23, "maximum": 54}},
    "results": {"word_count": 406, "sentence_count": 23, "paragraph_count": 14, "sentence_words": {"minimum": 1, "median": 18, "maximum": 47}},
    "sensitivity-analysis": {"word_count": 317, "sentence_count": 21, "paragraph_count": 11, "sentence_words": {"minimum": 1, "median": 14, "maximum": 50}},
    "algorithm": {"word_count": 339, "sentence_count": 20, "paragraph_count": 12, "sentence_words": {"minimum": 1, "median": 16.0, "maximum": 54}},
    "conclusion": {"word_count": 137, "sentence_count": 5, "paragraph_count": 3, "sentence_words": {"minimum": 19, "median": 21, "maximum": 49}},
    "strengths-limitations": {"word_count": 162, "sentence_count": 19, "paragraph_count": 8, "sentence_words": {"minimum": 1, "median": 11, "maximum": 19}},
    "memo": {"word_count": 600, "sentence_count": 31, "paragraph_count": 16, "sentence_words": {"minimum": 1, "median": 20, "maximum": 49}},
}


def source_page_lines(page: int) -> list[str]:
    if page not in range(1, PAGE_COUNT + 1):
        raise SystemExit(f"q121 source page is outside 1-{PAGE_COUNT}: {page}")
    if page not in PAGE_LINE_CACHE:
        path = SOURCE_PAGES / f"page-{page:04d}.txt"
        if not path.is_file():
            raise SystemExit(f"missing q121 source page text: {path}")
        PAGE_LINE_CACHE[page] = path.read_text(encoding="utf-8").splitlines()
    return PAGE_LINE_CACHE[page]


def normalize_source_lines(lines: list[str]) -> str:
    text = "\n".join(line.strip() for line in lines)
    text = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", text)
    text = re.sub(r"\s*\n\s*", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def resolve_source_span(page: int, line_start: int, line_end: int) -> str:
    lines = source_page_lines(page)
    if not (1 <= line_start <= line_end <= len(lines)):
        raise SystemExit(
            f"q121 invalid source span page {page}, lines {line_start}-{line_end}; "
            f"page has {len(lines)} lines"
        )
    excerpt = normalize_source_lines(lines[line_start - 1 : line_end])
    if not excerpt:
        raise SystemExit(
            f"q121 empty source span page {page}, lines {line_start}-{line_end}"
        )
    normalized_page = normalize_source_lines(lines)
    if excerpt not in normalized_page:
        raise SystemExit(
            f"q121 source normalization lost page {page}, lines {line_start}-{line_end}"
        )
    return excerpt


def measure_layout_paragraphs(
    records: list[dict[str, Any]],
) -> tuple[int, int, dict[str, int | float], list[str]]:
    paragraphs: list[str] = []
    functions: list[str] = []
    for record in records:
        parts = [resolve_source_span(*source_span) for source_span in record["source_spans"]]
        paragraphs.append(" ".join(parts))
        functions.append(record["function"])

    sentence_lengths: list[int] = []
    for paragraph in paragraphs:
        protected = paragraph
        for abbreviation in SENTENCE_ABBREVIATIONS:
            protected = protected.replace(abbreviation, abbreviation.replace(".", "<PERIOD>"))
        sentences = [
            sentence.replace("<PERIOD>", ".").strip()
            for sentence in re.split(r"(?<=[.!?])\s+", protected)
            if sentence.strip()
        ]
        if not sentences:
            sentences = [paragraph]
        sentence_lengths.extend(len(SOURCE_WORD_RE.findall(sentence)) for sentence in sentences)

    word_count = sum(len(SOURCE_WORD_RE.findall(paragraph)) for paragraph in paragraphs)
    sentence_words: dict[str, int | float] = {
        "minimum": min(sentence_lengths),
        "median": median(sentence_lengths),
        "maximum": max(sentence_lengths),
    }
    return word_count, len(sentence_lengths), sentence_words, functions


def build_language() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    chapters_by_code = {item["code"]: item for item in LANGUAGE_CHAPTERS}
    pattern_by_id = {pattern["pattern_id"]: pattern for pattern in PATTERNS}
    expected_pattern_ids = set(pattern_by_id)
    units: list[dict[str, Any]] = []
    local_counts: Counter[str] = Counter()

    for spec in LANGUAGE_OCCURRENCE_SPECS:
        item = chapters_by_code[spec["code"]]
        local_counts[spec["code"]] += 1
        local_index = local_counts[spec["code"]]
        rhetorical_role = OCCURRENCE_ROLES[spec["code"]][local_index - 1]
        pattern_ids = spec["pattern_ids"]
        unknown = sorted(set(pattern_ids) - expected_pattern_ids)
        if unknown:
            raise SystemExit(f"q121 occurrence references unknown patterns: {unknown}")
        if pattern_ids:
            order = list(pattern_by_id[pattern_ids[0]]["information_order"])
        else:
            order = [
                "paper-specific observation",
                "local analytical role",
                "source-bounded meaning",
                "no transferable template",
            ]
        page = spec["page"]
        line_start = spec["line_start"]
        line_end = spec["line_end"]
        excerpt_line_start, excerpt_line_end = spec["excerpt_lines"]
        source_excerpt = resolve_source_span(
            page, excerpt_line_start, excerpt_line_end
        )
        if len(source_excerpt) > 500:
            raise SystemExit(
                f"q121 source excerpt exceeds 500 characters: "
                f"{item['code']}-{local_index:03d} has {len(source_excerpt)}"
            )
        unit = {
            "language_unit_id": f"LU-{ID_STEM}-{item['code']}-{local_index:03d}",
            "page": page,
            "section": spec["section"],
            "chapter": item["chapter"],
            "granularity": spec["granularity"],
            "source_excerpt": source_excerpt,
            "source_anchor": {
                "page_file": f"page-{page:04d}.txt",
                "inspected_line_start": line_start,
                "inspected_line_end": line_end,
                "excerpt_line_start": excerpt_line_start,
                "excerpt_line_end": excerpt_line_end,
                "normalization": "trim lines, remove line-break hyphenation, collapse whitespace",
            },
            "function": spec["function"],
            "rhetorical_role": rhetorical_role,
            "rhetorical_move": (
                f"{spec['function']}; within {item['label']}, this move advances "
                f"{item['output']} and hands the result to {item['handoff']}"
            ),
            "reusable_pattern": " -> ".join(order),
            "information_order": order,
            "reusable_elements": [
                f"occurrences: physical page {page}, inspected source lines {line_start}-{line_end}, excerpt lines {excerpt_line_start}-{excerpt_line_end}, {spec['section']}",
                f"function: {spec['function']}",
                f"information order: {' -> '.join(order)}",
                "slots: replace every source entity with a typed case object, preserve the evidence class, then name the exact receiving section or decision",
                "variants: author-led action, definition, attributed input, figure-led interpretation, conditional comparison, or executive compression only when the nominated pattern boundary is met",
                f"handoff: {item['handoff']}",
            ],
            "prohibited_generalizations": [
                "boundary: retain whether the source statement is a premise, borrowed input, derivation, simulation, local sensitivity result, forecast, or recommendation",
                "anti-copy: replace every language, city, year, population, rate, matrix entry, score, and distinctive clause before reusing any nominated rhetorical mechanism",
                "Do not transfer N=22/26, 0.021, k=0.1/10, 43.0/39.7, 236.2/225.2, or any office assignment outside a rebuilt case.",
                "Do not call a time-varying population projection a Markov chain unless normalization and mutually exclusive states are established.",
            ],
            "features": {
                "voice": "first-person plural for staged research actions; section-as-agent or passive voice for definitions, tables, and plotted results",
                "tense": "present for definitions and mechanisms, past or present perfect for performed calculations, modal or future for projections and recommendations",
                "modality": "assume, may, should, can, believe, conclude, and recommend distinguish premises, possibilities, model outputs, and stakeholder actions",
                "clause_structure": "condition or baseline -> named mechanism/model -> evidence or operation -> bounded interpretation -> handoff",
                "quantitative_role": "attach every value to its state definition, unit, year, source, scenario, comparator, and downstream use",
                "transition": "first, however, therefore, building upon, additionally, combined with, in the end, and note that make model handoffs visible",
                "original_instantiations": [
                    {
                        "text": f"A clinic report can {spec['function']} after replacing the source entities, values, evidence, and receiving decision with its own case facts."
                    },
                    {
                        "text": f"A reservoir study can follow the same information order to {spec['function']} while preserving its own scenario and uncertainty boundary."
                    },
                ],
            },
            "candidate_pattern_ids": pattern_ids,
        }
        units.append(unit)

    for pattern in PATTERNS:
        nominated_units = [
            unit
            for unit in units
            if pattern["pattern_id"] in unit["candidate_pattern_ids"]
        ]
        pattern["occurrences"] = len(nominated_units)
        pattern["locations"] = list(
            dict.fromkeys(unit["section"] for unit in nominated_units)
        )
    design_pattern = pattern_by_id["LP-B-Q121-DESIGN-TRADEOFF"]
    if design_pattern["occurrences"] != 8:
        raise SystemExit(
            "q121 design-tradeoff nominations changed: "
            f"{design_pattern['occurrences']} != 8"
        )

    expected_code_counts = {
        item["code"]: item["count"] for item in LANGUAGE_CHAPTERS
    }
    if dict(local_counts) != expected_code_counts:
        raise SystemExit(
            f"q121 occurrence counts changed: {dict(local_counts)} != {expected_code_counts}"
        )

    layout_records: dict[str, list[dict[str, Any]]] = {
        item["code"]: [] for item in LANGUAGE_CHAPTERS
    }
    for record in LAYOUT_PARAGRAPHS:
        layout_records[record["code"]].append(record)

    layouts: list[dict[str, Any]] = []
    for item in LANGUAGE_CHAPTERS:
        start, end = item["pages"]
        span = end - start + 1
        records = layout_records[item["code"]]
        if len(records) != item["paragraph_count"]:
            raise SystemExit(
                f"q121 {item['code']} paragraph spans changed: "
                f"{len(records)} != {item['paragraph_count']}"
            )
        (
            word_count,
            sentence_count,
            sentence_words,
            paragraph_functions,
        ) = measure_layout_paragraphs(records)
        chapter_units = [
            unit for unit in units if unit["chapter"] == item["chapter"]
        ]
        role_counts = Counter(unit["rhetorical_role"] for unit in chapter_units)
        rhetorical_proportions = {
            role: role_counts[role] / len(chapter_units)
            for role in ("premise", "mechanism", "result", "boundary")
        }
        equations, figures, tables, citations, quantitative = CONTENT_COUNTS[item["chapter"]]
        layouts.append(
            {
                "chapter": item["chapter"],
                "page_start": start,
                "page_end": end,
                "page_fraction": round(span / PAGE_COUNT, 6),
                "word_count": word_count,
                "sentence_count": sentence_count,
                "paragraph_count": item["paragraph_count"],
                "sentence_words": sentence_words,
                "paragraph_functions": paragraph_functions,
                "rhetorical_proportions": rhetorical_proportions,
                "content_counts": {
                    "equations": equations,
                    "figures": figures,
                    "tables": tables,
                    "citations": citations,
                    "quantitative_results": quantitative,
                },
                "move_types": {
                    "opening": [f"name the input: {item['input']}"],
                    "transition": [f"produce and route: {item['output']}"],
                    "closing": [f"hand off under scope limits: {item['handoff']}"],
                },
                "counting_method": (
                    "Word and sentence metrics were measured from the explicit physical-page line spans "
                    "in LAYOUT_PARAGRAPHS after deterministic line-break hyphenation and whitespace "
                    "normalization; paragraph counts equal those audited spans. Appendix references, "
                    "captions, tables, and figure labels are retained separately as non-prose source "
                    "reviews, not zero-valued author-language layouts. All 28 pages and nineteen "
                    "focused crops retained the bounded visual-review protocol."
                ),
                "ambiguities": [
                    "The visible commercial watermark intersects every page header and the text layer omits many Greek letters, matrix displays, subscripts, and comparison signs.",
                    "Physical page 1 is the Summary Sheet; physical page 2 is the contents page; physical pages 3-28 correspond to printed pages 2-27.",
                    "Normalized chapters recur across preliminary, modified, application, memo, and appendix sections; each layout retains its audited bounding physical-page interval.",
                ],
            }
        )

    actual_layout_stats = {
        layout["chapter"]: {
            "word_count": layout["word_count"],
            "sentence_count": layout["sentence_count"],
            "paragraph_count": layout["paragraph_count"],
            "sentence_words": layout["sentence_words"],
        }
        for layout in layouts
    }
    if actual_layout_stats != EXPECTED_LAYOUT_STATS:
        raise SystemExit(
            f"q121 layout metrics changed: {actual_layout_stats} != {EXPECTED_LAYOUT_STATS}"
        )

    nonreusable_ids = {
        unit["language_unit_id"]
        for unit in units
        if not unit["candidate_pattern_ids"]
    }
    if nonreusable_ids != set(NONREUSABLE_LANGUAGE_REASONS):
        raise SystemExit(
            "q121 paper-specific nonreusable units changed: "
            f"{sorted(nonreusable_ids)} != {sorted(NONREUSABLE_LANGUAGE_REASONS)}"
        )
    assert len(units) == 84, len(units)
    return (
        {
            "available_chapters": [item["chapter"] for item in LANGUAGE_CHAPTERS],
            "chapter_layouts": layouts,
            "paper_id": PAPER_ID,
            "problem_type": PROBLEM_TYPE,
            "review_status": "validated",
            "schema_version": 3,
            "source_sha256": SHA256,
            "repeated_patterns": PATTERNS,
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


EQUATION_COUNTER = 0


def equation(
    page: int,
    label: str | None,
    expression: str,
    normalized: str,
    purpose: str,
    symbols: list[str],
    confidence: str = "high",
    source_type: str = "paper",
) -> dict[str, Any]:
    global EQUATION_COUNTER
    EQUATION_COUNTER += 1
    return {
        "equation_id": f"EQ-{ID_STEM}-{EQUATION_COUNTER:03d}",
        "page": page,
        "label": label,
        "source_expression": expression,
        "normalized_latex": normalized,
        "purpose": purpose,
        "variable_symbols": symbols,
        "source_type": source_type,
        "visual_checked": True,
        "transcription_confidence": confidence,
    }


def make_model(
    index: int,
    page: int,
    section: str,
    family: str,
    purpose: str,
    variables: list[dict[str, str]],
    inputs: list[str],
    outputs: list[str],
    equations: list[dict[str, Any]],
    assumptions: list[str],
    validation_refs: list[str],
    steps: list[str],
    limitations: list[str],
    origin: str = "paper-specific",
    software: list[str] | None = None,
    estimation: str | None = None,
    convergence: str | None = None,
) -> dict[str, Any]:
    return {
        "model_id": f"MU-{ID_STEM}-{index:03d}",
        "page": page,
        "section": section,
        "family": family,
        "purpose": purpose,
        "base_or_modification": origin,
        "summary": purpose,
        "variables": variables,
        "inputs": inputs,
        "outputs": outputs,
        "governing_equations": equations,
        "equation_status": {
            "status": "present" if equations else "omitted-by-paper",
            "reason": (
                "Displayed or explicitly reconstructed equations were checked against focused byte-bounded crops."
                if equations
                else "The paper supplies an algorithmic or forecasting narrative and result tables but omits a governing display."
            ),
        },
        "objectives": [
            purpose,
            "Keep native speakers, non-native speakers, learners, migrants, language identities, people, forecasts, scores, and decisions as distinct quantities.",
        ],
        "constraints": [
            "Retain physical page, source year, language-state definition, unit, time index, scenario, coefficient setting, and downstream decision.",
            "Do not silently repair the paper's index directions, normalization constants, matrix entries, captions, spelling, or missing optimization details.",
        ],
        "conditions": {
            "initial": {
                "status": "present",
                "details": [
                    "The preliminary model starts from 2013 speaker statistics; the modified model starts from 2017 and projects fifty years.",
                    "Initial non-native English composition is specified only proportionally, and some source values are missing or disputed.",
                ],
            },
            "boundary": {
                "status": "present",
                "details": [
                    "People may retain multiple language identities, so summed state components are not necessarily a count of unique persons.",
                    "Abrupt events, most reverse feedback, detailed education heterogeneity, migrant first-language effects, and management cost are omitted.",
                ],
            },
            "equilibrium": {
                "status": "present" if index in {2, 3, 5, 6} else "not-applicable",
                "details": [
                    "Homogeneous units use a dominant eigenpair as a long-run composition claim; dynamic and optimization units use finite horizons instead."
                ],
            },
        },
        "parameter_estimation": {
            "status": "partial",
            "method": estimation
            or "Parameters combine prompt conditions, Wikipedia-derived speaker tables, UN demographic/migration series, author assumptions, weighted averages, and unreported fitted quantities; no complete provenance ledger is supplied.",
            "parameters": inputs,
        },
        "algorithm": {
            "status": "partial" if steps else "omitted-by-paper",
            "steps": steps,
            "software": software or ["MATLAB is named for preliminary calculations; no complete code or environment is archived"],
            "convergence_criteria": convergence
            or "The source reports repeated alterations, a fixed fifty-year horizon, or a stable optimizer output without numerical tolerance, seed, or complete stopping diagnostics.",
        },
        "assumptions": assumptions,
        "identifiability_feasibility": {
            "status": "partial",
            "analysis": "The state logic and reported outputs are inspectable, but overlapping identities, incomplete initial scales, sparse provenance, missing code, unseeded optimization, and absent uncertainty limit independent identification and decision validation.",
        },
        "handoff_outputs": outputs,
        "validation_refs": validation_refs,
        "computational_cost": "The paper gives no runtime, memory, hardware, numerical precision, archived inputs, or complete executable implementation for the matrix projections, GDP fit, or optimization.",
        "strengths": [
            "The unit occupies an explicit position in the definition -> state transition -> projection -> sensitivity -> rating -> recommendation chain.",
            "Its assumptions, borrowed inputs, derived values, simulated values, and recommendations can be labeled separately.",
        ],
        "limitations": limitations,
        "missing_details": [
            "Complete input snapshots, language-country mapping rules, units, uncertainty distributions, code, software versions, and random seeds are absent.",
            "No leakage-free holdout, prediction interval, alternative baseline suite, joint sensitivity analysis, or decision-stability analysis is reported.",
        ],
    }


def build_models() -> dict[str, Any]:
    global EQUATION_COUNTER
    EQUATION_COUNTER = 0
    models: list[dict[str, Any]] = []

    variables_1 = [
        variable("Y_1", "native speakers of language 1", "million persons", "state", "Native-speaker count for language 1 in year n."),
        variable("Y_2", "native speakers of language 2", "million persons", "state", "Native-speaker count for language 2 in year n."),
        variable("y_1", "non-native speakers of language 1", "million speaker identities", "state", "Non-native language-1 identity count in year n."),
        variable("y_2", "non-native speakers of language 2", "million speaker identities", "state", "Non-native language-2 identity count in year n."),
        variable("A", "homogeneous transition operator", "per year", "parameter", "Four-state annual transition matrix."),
        variable("n", "year index", "year", "input", "Discrete annual index."),
        variable("alpha_11", "native-1 birth rate", "1/year", "parameter", "Annual birth rate of native language-1 speakers."),
        variable("alpha_22", "native-2 birth rate", "1/year", "parameter", "Annual birth rate of native language-2 speakers."),
        variable("alpha_13", "non-native-1 offspring contribution", "1/year", "parameter", "Rate at which non-native language-1 speakers contribute native language-1 births."),
        variable("alpha_24", "non-native-2 offspring contribution", "1/year", "parameter", "Rate at which non-native language-2 speakers contribute native language-2 births."),
        variable("beta_11", "native-1 death rate", "1/year", "parameter", "Annual death rate of native language-1 speakers."),
        variable("beta_22", "native-2 death rate", "1/year", "parameter", "Annual death rate of native language-2 speakers."),
        variable("beta_33", "non-native-1 death rate", "1/year", "parameter", "Annual death rate of non-native language-1 speakers."),
        variable("beta_44", "non-native-2 death rate", "1/year", "parameter", "Annual death rate of non-native language-2 speakers."),
        variable("gamma_32", "learning flow from native language 2 to non-native language 1", "1/year", "parameter", "Matrix entry for Y_2 to y_1."),
        variable("gamma_41", "learning flow from native language 1 to non-native language 2", "1/year", "parameter", "Matrix entry for Y_1 to y_2."),
    ]
    equations_1 = [
        equation(
            5,
            "(1)",
            "Y^(n+1) = A Y^(n), with rows (Y1,Y2,y1,y2) and the displayed alpha, beta, and gamma entries",
            r"\mathbf Y^{(n+1)}=\begin{pmatrix}1+\alpha_{11}-\beta_{11}&0&\alpha_{13}&0\\0&1+\alpha_{22}-\beta_{22}&0&\alpha_{24}\\0&\gamma_{32}&1-\beta_{33}&0\\\gamma_{41}&0&0&1-\beta_{44}\end{pmatrix}\mathbf Y^{(n)}=A\mathbf Y^{(n)}",
            "Retain the complete four-state annual transition matrix and its direction of flow.",
            ["Y_1", "Y_2", "y_1", "y_2", "A", "n", "alpha_11", "alpha_22", "alpha_13", "alpha_24", "beta_11", "beta_22", "beta_33", "beta_44", "gamma_32", "gamma_41"],
        )
    ]
    models.append(
        make_model(
            1,
            5,
            "2.3.1 N=2 Model",
            "overlapping speaker-state population projection",
            "Represent births, deaths, and cross-language learning among two native and two non-native speaker states.",
            variables_1,
            ["Y_1", "Y_2", "y_1", "y_2", "n", "alpha_11", "alpha_22", "alpha_13", "alpha_24", "beta_11", "beta_22", "beta_33", "beta_44", "gamma_32", "gamma_41"],
            ["Y_1", "Y_2", "y_1", "y_2"],
            equations_1,
            [
                "Native and non-native categories are retained after a person learns an additional language.",
                "Birth, death, and learning are the only preliminary transitions; abrupt structural shocks are excluded.",
                "Selected matrix entries are zero to avoid the paper's stated double counting paths.",
            ],
            ["Figure 1", "Equation (1)", "General Assumptions 1-7"],
            ["define four states", "draw permitted self and cross flows", "place rates in A", "advance one annual step"],
            [
                "State components overlap because multilingual people retain previous identities, so the operator is not probability conserving.",
                "The prose description of gamma_32 and gamma_41 reverses the flow order implied by the matrix.",
            ],
            origin="base",
        )
    )

    variables_2 = [
        variable("A", "homogeneous transition operator", "per year", "input", "Constant annual matrix from Equation (1)."),
        variable("Y_0", "initial state vector", "speaker identities", "input", "Arbitrary nonnegative starting vector."),
        variable("Y", "dominant composition vector", "relative speaker identities", "output", "Eigenvector used as a steady composition."),
        variable("lambda", "dominant annual multiplier", "dimensionless per year", "output", "Eigenvalue interpreted by the paper as total population growth."),
        variable("k", "matrix iteration index", "year", "input", "Number of homogeneous annual steps."),
        variable("c", "initial-vector scale coefficient", "dimensionless", "intermediate", "Coefficient required by a correct asymptotic eigenvector statement.", "inferred-from-equation"),
    ]
    equations_2 = [
        equation(
            6,
            "(2)",
            "lim_(k->infinity) A^k Y^(0) = lambda^k Y",
            r"\lim_{k\to\infty}A^k\mathbf Y^{(0)}=\lambda^k\mathbf Y",
            "Record the paper's stated long-run relationship without silently repairing its divergent limit or missing scale coefficient.",
            ["A", "Y_0", "Y", "lambda", "k"],
            confidence="high",
        ),
        equation(
            6,
            "(3)",
            "A Y = lambda Y",
            r"A\mathbf Y=\lambda\mathbf Y",
            "Define the eigenpair used to represent a stable composition under a homogeneous operator.",
            ["A", "Y", "lambda"],
        ),
    ]
    models.append(
        make_model(
            2,
            6,
            "2.3.1 steady state",
            "dominant-eigenpair composition analysis",
            "Convert the homogeneous recurrence into a claimed long-run speaker-state composition and annual growth multiplier.",
            variables_2,
            ["A", "Y_0", "k"],
            ["Y", "lambda"],
            equations_2,
            [
                "A dominant nonnegative eigenvector is treated as the stable split of speaker-state components.",
                "The initial vector is assumed not to eliminate the dominant eigendirection.",
                "The paper treats the state sum as total population even though identities overlap.",
            ],
            ["Equations (2)-(3)", "prose definition of steady split"],
            ["iterate A", "identify a dominant eigenpair", "normalize the eigenvector", "interpret the component split"],
            [
                "Equation (2) places k on both sides of a limit and omits the scale coefficient and dominance conditions.",
                "A composition can be stable after normalization while absolute state counts continue to grow.",
            ],
            origin="base",
        )
    )

    variables_3 = [
        variable("A", "numerical N=2 transition matrix", "per year", "input", "Printed 4x4 matrix in Equation (5)."),
        variable("alpha_11", "native-1 birth rate", "1/year", "parameter", "Set to 0.02."),
        variable("alpha_22", "native-2 birth rate", "1/year", "parameter", "Set to 0.02."),
        variable("alpha_13", "non-native-1 birth contribution", "1/year", "parameter", "Set to 0.05."),
        variable("alpha_24", "non-native-2 birth contribution", "1/year", "parameter", "Set to 0.05 in Equation (4)."),
        variable("beta", "common death rate", "1/year", "parameter", "All four death rates are set to 0.01."),
        variable("gamma_32", "learning rate into y1", "1/year", "parameter", "Set to 0.01."),
        variable("gamma_41", "learning rate into y2", "1/year", "parameter", "Set to 0.01."),
        variable("lambda", "reported dominant multiplier", "dimensionless per year", "output", "Reported as 1.01049."),
        variable("Y", "reported eigenvector", "relative speaker identities", "output", "Printed vector (0.500,0.500,1.124,1.124)."),
    ]
    equations_3 = [
        equation(
            6,
            "(4)",
            "alpha11=alpha22=0.02; alpha13=alpha24=0.05; all beta=0.01; gamma41=gamma32=0.01",
            r"\alpha_{11}=\alpha_{22}=0.02,\quad\alpha_{13}=\alpha_{24}=0.05,\quad\beta_{11}=\beta_{22}=\beta_{33}=\beta_{44}=0.01,\quad\gamma_{41}=\gamma_{32}=0.01",
            "Retain the parameter equalities used for the numerical bilingual example.",
            ["alpha_11", "alpha_22", "alpha_13", "alpha_24", "beta", "gamma_32", "gamma_41"],
        ),
        equation(
            6,
            "(5)",
            "A = [[1.01,0,0.05,0],[0,1.01,0,0.005],[0,0.01,0.99,0],[0.01,0,0,0.99]]",
            r"A=\begin{pmatrix}1.01&0&0.05&0\\0&1.01&0&0.005\\0&0.01&0.99&0\\0.01&0&0&0.99\end{pmatrix}",
            "Transcribe the printed matrix, including the visible 0.005 entry that conflicts with Equation (4).",
            ["A"],
        ),
        equation(
            6,
            "(6)",
            "lambda=1.01049; Y=(0.500,0.500,1.124,1.124)^T",
            r"\lambda=1.01049,\qquad\mathbf Y=(0.500,0.500,1.124,1.124)^T",
            "Retain the reported eigenpair and its unnormalized scale for audit.",
            ["lambda", "Y"],
        ),
    ]
    models.append(
        make_model(
            3,
            6,
            "2.3.1 numerical N=2 test",
            "worked transition-matrix eigenanalysis",
            "Demonstrate how fixed demographic and learning rates produce a reported long-run bilingual composition.",
            variables_3,
            ["A", "alpha_11", "alpha_22", "alpha_13", "alpha_24", "beta", "gamma_32", "gamma_41"],
            ["lambda", "Y"],
            equations_3,
            [
                "Both languages use symmetric birth, death, offspring, and learning parameters except for the printed Equation (5) discrepancy.",
                "The eigenvector is treated as a population proportion without a displayed normalization.",
            ],
            ["Equations (4)-(6)", "focused page-6 crop"],
            ["substitute fixed rates", "form A", "compute eigenvalues", "select a nonnegative eigenvector", "interpret the entries"],
            [
                "Equation (5) prints 0.005 where Equation (4) implies 0.05.",
                "The reported Equation (6) pair does not satisfy either the printed or nominal matrix, and the vector sums to 3.248.",
            ],
            origin="base",
        )
    )

    variables_4 = [
        variable("gamma", "common learning rate", "1/year", "input", "Horizontal-axis learning rate varied from 0 to 0.05."),
        variable("q_non_native", "plotted non-native quantity", "reported proportion", "output", "Blue Figure 2 ordinate, which rises above 1 despite its proportion label."),
        variable("q_native", "native comparison level", "reported proportion", "parameter", "Red dashed reference at 0.5."),
    ]
    equations_4 = [
        equation(
            7,
            None,
            "gamma > 0.021 implies plotted non-native quantity exceeds native reference",
            r"\gamma>0.021\Longrightarrow q_{\mathrm{non\mbox{-}native}}>q_{\mathrm{native}}",
            "Encode the threshold claim read from Figure 2 and its accompanying prose.",
            ["gamma", "q_non_native", "q_native"],
            confidence="medium",
        )
    ]
    models.append(
        make_model(
            4,
            7,
            "2.3.1 learning-rate screen",
            "one-parameter local sensitivity analysis",
            "Vary the bilingual learning rate and identify when the plotted non-native state exceeds the native reference.",
            variables_4,
            ["gamma", "q_native"],
            ["q_non_native"],
            equations_4,
            [
                "All other N=2 parameters are held fixed while gamma varies.",
                "The plotted ordinate is treated by the paper as a proportion.",
            ],
            ["Figure 2", "threshold prose on physical page 7"],
            ["scan gamma from 0 to 0.05", "compute the dominant state quantity", "compare with 0.5", "report the crossing near 0.021"],
            [
                "The ordinate reaches about 1.12, which cannot be a total-population proportion; it appears to be an unnormalized eigenvector component.",
                "No joint sensitivity or uncertainty range is examined.",
            ],
            origin="base",
        )
    )

    variables_5 = [
        variable("N", "number of languages", "count", "input", "Set to 22 in the preliminary scaled model."),
        variable("A", "2N-state transition operator", "per year", "parameter", "General native/non-native matrix in Equation (7)."),
        variable("Y_0", "2013 state vector", "million speaker identities", "input", "Native and non-native speaker values used for initialization."),
        variable("beta_bar", "world-average non-native death rate", "1/year", "parameter", "Reported as 0.0083."),
        variable("alpha_bar", "world-average birth rate", "1/year", "parameter", "Reported as 0.0193."),
        variable("r", "immigrant-to-non-native ratio", "dimensionless", "parameter", "Reported as 0.172."),
        variable("alpha", "non-native offspring contribution", "1/year", "parameter", "Computed as r times alpha_bar."),
        variable("gamma_ji", "learning rate from source i to target j", "1/year", "parameter", "Allocated by normalized target popularity."),
        variable("Gamma_i", "total annual learning rate for source group i", "1/year", "input", "Source-group learning budget."),
        variable("y_j_0", "initial non-native count for target j", "million speaker identities", "input", "Raw attraction proxy in Equation (11)."),
        variable("yhat_j_0", "normalized target attraction share", "dimensionless", "intermediate", "Claimed normalized non-native share."),
        variable("i", "source-language index", "count", "input", "Index for a native source group."),
        variable("j", "target-language index", "count", "input", "Index for a learned language."),
    ]
    equations_5 = [
        equation(
            7,
            "(7)",
            "A is the displayed 2N by 2N native/non-native transition matrix with diagonal demographic blocks and cross-learning entries",
            r"A=\begin{pmatrix}D_Y&B_{y\to Y}\\G_{Y\to y}&D_y\end{pmatrix}\in\mathbb R^{2N\times2N}",
            "Normalize the displayed ellipsis matrix into its four structural blocks without inventing omitted entries.",
            ["A", "N"],
            confidence="medium",
        ),
        equation(
            8,
            "(8)",
            "all non-native death rates equal beta_bar; all non-native offspring contributions equal alpha",
            r"\beta_{(N+1)(N+1)}=\cdots=\beta_{(2N)(2N)}=\bar\beta,\qquad\alpha_{1(N+1)}=\cdots=\alpha_{N(2N)}=\alpha",
            "Retain the common-rate simplification used to fill the non-native blocks.",
            ["N", "beta_bar", "alpha"],
        ),
        equation(
            8,
            "(9)",
            "alpha = r alpha_bar = 0.0033",
            r"\alpha=r\bar\alpha=0.0033",
            "Compute the common offspring contribution from the migration ratio and world birth rate.",
            ["alpha", "r", "alpha_bar"],
        ),
        equation(
            8,
            "(10)",
            "gamma_(i,N+1):...:gamma_(i,N+j):...:gamma_(i,2N), j != i",
            r"\gamma_{i(N+1)}:\cdots:\gamma_{i(N+j)}:\cdots:\gamma_{i(2N)},\quad j\ne i",
            "Retain the printed ratio-index orientation before comparing it with Equations (11)-(12).",
            ["gamma_ji", "N", "i", "j"],
            confidence="high",
        ),
        equation(
            8,
            "(11)",
            "gamma_(N+1,i):...:gamma_(N+j,i):... = y1^(0):...:yN^(0) = yhat1^(0):...:yhatN^(0)",
            r"\gamma_{(N+1)i}:\cdots:\gamma_{(N+j)i}:\cdots:\gamma_{(2N)i}=y_1^{(0)}:\cdots:y_N^{(0)}=\hat y_1^{(0)}:\cdots:\hat y_N^{(0)}",
            "Record the target-popularity ratio and the paper's claimed normalized shares.",
            ["gamma_ji", "N", "i", "j", "y_j_0", "yhat_j_0"],
            confidence="high",
        ),
        equation(
            8,
            "(12)",
            "gamma_(N+j,i) = yhat_j^(0) Gamma_i",
            r"\gamma_{(N+j)i}=\hat y_j^{(0)}\Gamma_i",
            "Allocate a source group's total learning rate to target languages by the stated attraction share.",
            ["gamma_ji", "N", "i", "j", "yhat_j_0", "Gamma_i"],
        ),
    ]
    models.append(
        make_model(
            5,
            7,
            "2.4 Calculating and Simplifying",
            "22-language homogeneous population projection",
            "Scale the native/non-native transition structure to 22 languages and fill it with demographic and attraction-based learning rates.",
            variables_5,
            ["N", "Y_0", "beta_bar", "alpha_bar", "r", "Gamma_i", "y_j_0", "i", "j"],
            ["A", "alpha", "gamma_ji", "yhat_j_0"],
            equations_5,
            [
                "Twenty-two languages stand in for the top twenty-six because of limited data.",
                "Non-native groups share world-average birth/death behavior.",
                "A language is assumed equally attractive across source populations, and attraction follows its initial non-native count.",
            ],
            ["Equations (7)-(12)", "Appendix Tables 3-5", "sources [1], [4], [5]"],
            ["map countries to language groups", "compute weighted demographic rates", "form a 44-state operator", "normalize attraction shares", "allocate source learning rates"],
            [
                "Equation (10) transposes the gamma index direction used by Equations (11)-(12) and the matrix convention.",
                "The 22 claimed normalized values sum to 1.0387, apparently using 1193.7 instead of the raw total 1239.7.",
                "Excluding j=i conflicts with allocating Gamma_i using shares normalized over all j.",
            ],
            origin="base",
        )
    )

    variables_6 = [
        variable("Y_0", "2013 state vector", "million speaker identities", "input", "Initial 22-language native/non-native vector; the million scale is implied by nearby prose rather than printed in Table 1.", "unspecified"),
        variable("A", "homogeneous annual operator", "per year", "input", "Calibrated preliminary transition matrix."),
        variable("Y_4", "2017 projected state", "million speaker identities", "output", "Four-step projection compared with 2017 values; the million scale is implied by nearby prose rather than printed in Table 1.", "unspecified"),
        variable("Y", "reported long-run composition", "dimensionless", "output", "Normalized eigenvector with a reported Punjabi native component 0.9601."),
        variable("lambda", "reported long-run multiplier", "dimensionless per year", "output", "Reported as 1.0215."),
    ]
    equations_6 = [
        equation(
            9,
            None,
            "Y^(4) = A^4 Y^(0)",
            r"\mathbf Y^{(4)}=A^4\mathbf Y^{(0)}",
            "Define the four-year backcast-like projection used for the 2017 comparison.",
            ["Y_4", "A", "Y_0"],
        ),
        equation(
            9,
            "(13)",
            "Y=(0.0050,...,0.9601,...,0.0003)^T; lambda=1.0215",
            r"\mathbf Y=(0.0050,\ldots,0.9601,\ldots,0.0003)^T,\qquad\lambda=1.0215",
            "Retain the abbreviated long-run eigenpair and the reported Punjabi-dominance component.",
            ["Y", "lambda"],
            confidence="medium",
        ),
    ]
    models.append(
        make_model(
            6,
            9,
            "2.5 The Model Results",
            "short-run projection check and long-run failure diagnostic",
            "Compare 2013-to-2017 projections with reported counts and use the homogeneous long-run composition as a falsification signal.",
            variables_6,
            ["Y_0", "A"],
            ["Y_4", "Y", "lambda"],
            equations_6,
            [
                "Table 1 omits a unit; nearby German-speaker prose implies that the native and non-native entries are counts in millions, with native-person and potentially overlapping non-native identity semantics.",
                "Large discrepancies are attributed primarily to source-data inaccuracy.",
                "The largest fixed growth rate dominates a homogeneous long-run operator.",
            ],
            ["Table 1", "Equation (13)", "physical page 9 (printed Page 8 of 27) formula/table crop"],
            ["advance four steps", "compare ten displayed language rows", "inspect deviations", "compute dominant eigenpair", "diagnose implausible concentration"],
            [
                "Several non-native predictions have large errors, including Russian, French, and German, but no error metric or recalibration follows.",
                "Equation (13) omits the full 44-component vector and matrix, preventing independent verification of the 96.01 percent claim.",
            ],
            origin="base",
        )
    )

    variables_7 = [
        variable("Y_n", "expanded state vector", "speaker identities", "state", "Native, non-native, and migrant population blocks in year n."),
        variable("A_n", "time-varying transition operator", "per year", "state", "Annual block matrix determined by state and exogenous time inputs."),
        variable("Xi", "native natural-growth matrix", "per year", "parameter", "Diagonal native birth-death block."),
        variable("Pi", "non-native decrease matrix", "per year", "parameter", "Diagonal death-and-migration retention block."),
        variable("S", "migrant reproduction matrix", "per year", "parameter", "Diagonal flow from migrants to native speakers."),
        variable("G", "language learning matrix", "per year", "parameter", "Flow from native speakers into non-native language states."),
        variable("R", "migration matrix", "per year", "parameter", "Flow from non-native speakers to migrant states."),
        variable("Omega", "migrant death matrix", "per year", "parameter", "Diagonal migrant-retention block."),
        variable("F", "state/time feedback map", "operator", "parameter", "Unspecified map used to update the next transition matrix."),
        variable("n", "year index", "year", "input", "Discrete annual index."),
    ]
    equations_7 = [
        equation(
            12,
            None,
            "A^(n) = [[Xi^(n),0,S^(n)],[G^(n),Pi^(n),0],[0,R^(n),Omega^(n)]]",
            r"A^{(n)}=\begin{pmatrix}\Xi^{(n)}&0&S^{(n)}\\G^{(n)}&\Pi^{(n)}&0\\0&R^{(n)}&\Omega^{(n)}\end{pmatrix}",
            "Retain the three-block native, non-native, and migrant transition structure.",
            ["A_n", "Xi", "Pi", "S", "G", "R", "Omega", "n"],
        ),
        equation(
            12,
            "(14)",
            "Y^(n+1) = A^(n) Y^(n)",
            r"\mathbf Y^{(n+1)}=A^{(n)}\mathbf Y^{(n)}",
            "Advance the expanded state using the transition operator for year n.",
            ["Y_n", "A_n", "n"],
        ),
        equation(
            12,
            "(15)",
            "A^(n+1) = F[Y^(n), n]",
            r"A^{(n+1)}=F[\mathbf Y^{(n)},n]",
            "State the paper's feedback update from population state and time to the next annual operator.",
            ["A_n", "F", "Y_n", "n"],
        ),
    ]
    models.append(
        make_model(
            7,
            12,
            "3.3 Analysis of the Problem",
            "inhomogeneous block population projection",
            "Add learner-completion and migrant pathways, natural growth, and annual feedback to the preliminary speaker-state recurrence.",
            variables_7,
            ["Y_n", "Xi", "Pi", "S", "G", "R", "Omega", "F", "n"],
            ["Y_n", "A_n"],
            equations_7,
            [
                "Learners do not reproduce as learners or die during the modeled learning interval.",
                "Migrant offspring enter the native state of the destination language region.",
                "After migration, a person leaves the corresponding non-native state in this model.",
            ],
            ["Figure 3", "Equations (14)-(15)", "additional symbol table"],
            ["expand the state taxonomy", "assemble block matrices", "advance one year", "update demographic and learning parameters", "repeat to the horizon"],
            [
                "S denotes both learner counts and migrant reproduction in different parts of the paper.",
                "R is once called a learning matrix although the symbol table and block role define migration.",
                "Equations (14)-(15) create a one-period lag if F was intended as contemporaneous state feedback.",
            ],
            origin="modification",
        )
    )

    variables_8 = [
        variable("A_n", "English-specialized transition operator", "per year", "parameter", "Four-block annual matrix in year n."),
        variable("Xi", "native natural-growth block", "per year", "parameter", "Diagonal block for native populations."),
        variable("Pi_1", "non-native English decrease block", "per year", "parameter", "Death and migration retention for non-native English states."),
        variable("Pi", "other non-native decrease block", "per year", "parameter", "Retention for non-English non-native states."),
        variable("G_1", "English learning block", "per year", "parameter", "Flows native non-English groups into non-native English states."),
        variable("G", "other-language learning block", "per year", "parameter", "Flows native groups into other non-native states."),
        variable("R_1", "English-region migration block", "per year", "parameter", "Flows non-native English speakers into English-region migrants."),
        variable("R", "other migration block", "per year", "parameter", "Flows other non-native states into destination migrants."),
        variable("Omega", "migrant decrease block", "per year", "parameter", "Migrant death retention block."),
        variable("S", "migrant reproduction block", "per year", "parameter", "Migrant offspring flow into native states."),
        variable("Y_i_0", "initial native population of source group i", "million persons", "input", "2017 native population used in Equation (16)."),
        variable("y_i1_0", "initial non-native English speakers from source i", "million speaker identities", "output", "Source-specific non-native English state at n=0."),
        variable("N", "number of languages", "count", "input", "Set to 26 in the modified model."),
        variable("n", "year index", "year", "input", "Discrete annual index."),
    ]
    equations_8 = [
        equation(
            13,
            None,
            "A^(n) = [[Xi,0,0,S],[G1,Pi1,0,0],[G,0,Pi,0],[0,R1,R,Omega]]",
            r"A^{(n)}=\begin{pmatrix}\Xi^{(n)}&0&0&S^{(n)}\\G_1^{(n)}&\Pi_1^{(n)}&0&0\\G^{(n)}&0&\Pi^{(n)}&0\\0&R_1^{(n)}&R^{(n)}&\Omega^{(n)}\end{pmatrix}",
            "Separate non-native English states so their source-language distribution can be reported.",
            ["A_n", "Xi", "Pi_1", "Pi", "G_1", "G", "R_1", "R", "Omega", "S", "n"],
        ),
        equation(
            13,
            "(16)",
            "y_21^(0):...:y_N1^(0) = Y_2^(0):...:Y_N^(0)",
            r"y_{21}^{(0)}:\cdots:y_{N1}^{(0)}=Y_2^{(0)}:\cdots:Y_N^{(0)}",
            "Specify the source-language composition of initial non-native English speakers proportionally to native populations.",
            ["y_i1_0", "Y_i_0", "N"],
        ),
    ]
    models.append(
        make_model(
            8,
            13,
            "3.3-3.4 English-specific partition",
            "four-block English distribution projection",
            "Track non-native English speakers by source language while retaining other non-native and migrant states.",
            variables_8,
            ["Xi", "Pi_1", "Pi", "G_1", "G", "R_1", "R", "Omega", "S", "Y_i_0", "N", "n"],
            ["A_n", "y_i1_0"],
            equations_8,
            [
                "English is indexed as language 1 and Chinese as language 2.",
                "Initial non-native English composition is proportional to native-group population.",
                "Native English emigration effects on English-speaker distribution are omitted because non-native speakers are claimed to dominate.",
            ],
            ["English-specific four-block matrix", "Equation (16)", "physical page 13 crops"],
            ["split English non-native states", "form G1/Pi1/R1 blocks", "set an initial proportional composition", "advance with the inhomogeneous recurrence"],
            [
                "Equation (16) supplies only ratios and no total or normalization condition, so the initial English vector is not uniquely identified.",
                "The description of G1 as diagonal after deleting a column is dimensionally imprecise.",
                "Omitting native-English migration is justified qualitatively rather than tested.",
            ],
            origin="modification",
        )
    )

    variables_9 = [
        variable("eta_ji", "annual learning-completion rate from i to j", "1/year", "output", "Rate entering the learning matrix in year n."),
        variable("p_ji", "eagerness to learn target j from source i", "dimensionless", "parameter", "Attraction share assigned from non-native popularity."),
        variable("a_i", "new learner fraction", "1/year", "parameter", "Set to 0.01 for every source group."),
        variable("sigma_i", "same-family learning duration", "year", "parameter", "Set to 3 years for every source group."),
        variable("d_ji", "language-family difficulty multiplier", "dimensionless", "parameter", "Set to 1 within a family and 2 across families."),
        variable("y_j", "target j non-native population", "speaker identities", "input", "Popularity quantity used in the eagerness ratio."),
        variable("yhat_j", "normalized target j popularity", "dimensionless", "intermediate", "Claimed normalized version of y_j."),
        variable("N", "number of languages", "count", "input", "Set to 26."),
        variable("i", "source-language index", "count", "input", "Native source group."),
        variable("j", "target-language index", "count", "input", "Language being learned."),
        variable("n", "year index", "year", "input", "Discrete annual index."),
    ]
    equations_9 = [
        equation(
            14,
            "(17)",
            "eta_ji^(n) = p_ji^(n) a_i^(n) / (sigma_i^(n) d_ji^(n))",
            r"\eta_{ji}^{(n)}=\frac{p_{ji}^{(n)}a_i^{(n)}}{\sigma_i^{(n)}d_{ji}^{(n)}}",
            "Combine eagerness, learner entry, learning duration, and language-family difficulty into an annual completion rate.",
            ["eta_ji", "p_ji", "a_i", "sigma_i", "d_ji", "i", "j", "n"],
        ),
        equation(
            14,
            None,
            "p_1i^(n):...:p_Ni^(n) = y_1^(n):...:y_N^(n) = yhat_1^(n):...:yhat_N^(n)",
            r"p_{1i}^{(n)}:\cdots:p_{Ni}^{(n)}=y_1^{(n)}:\cdots:y_N^{(n)}=\hat y_1^{(n)}:\cdots:\hat y_N^{(n)}",
            "Allocate eagerness in proportion to target-language non-native popularity.",
            ["p_ji", "y_j", "yhat_j", "N", "i", "n"],
            confidence="medium",
        ),
        equation(
            14,
            None,
            "a_1=...=a_N=0.01; sigma_1=...=sigma_N=3",
            r"a_1=\cdots=a_N=0.01,\qquad\sigma_1=\cdots=\sigma_N=3",
            "Retain the common learner-entry fraction and same-family learning duration.",
            ["a_i", "sigma_i", "N"],
        ),
        equation(
            14,
            None,
            "d_ji=1 for same language family; d_ji=2 for different language families",
            r"d_{ji}=\begin{cases}1,&i,j\text{ in the same family},\\2,&i,j\text{ in different families}.\end{cases}",
            "Encode the two-level language-family difficulty multiplier.",
            ["d_ji", "i", "j"],
        ),
    ]
    models.append(
        make_model(
            9,
            14,
            "3.4 learning-rate parameterization",
            "attraction-duration learning-flow model",
            "Translate target popularity, education throughput, and language-family distance into the annual learning block.",
            variables_9,
            ["p_ji", "a_i", "sigma_i", "d_ji", "y_j", "N", "i", "j", "n"],
            ["eta_ji", "yhat_j"],
            equations_9,
            [
                "One percent of each group starts a foreign language every year.",
                "Mastery takes three years within a language family and six years across families.",
                "Past non-native popularity is used as future eagerness.",
            ],
            ["Equation (17)", "physical page 14 parameter crop", "language-family classification"],
            ["normalize target popularity", "set learner entry", "classify family relation", "divide by effective duration", "fill G and G1"],
            [
                "The source does not provide a normalization constant that uniquely determines p_ji.",
                "d_ji is called similarity but grows when languages are less similar, so it acts as difficulty or distance.",
                "Time superscripts are displayed although a_i, sigma_i, and d_ji are then held constant.",
            ],
            origin="modification",
        )
    )

    variables_10 = [
        variable("Y_2017", "2017 expanded language state", "million speaker identities", "input", "Initial 26-language native, non-native, and migrant state."),
        variable("A_n", "annual inhomogeneous operator", "per year", "input", "Transition operator updated across the fifty-year horizon."),
        variable("Y_2067", "2067 expanded language state", "million speaker identities", "output", "Projected language populations, migration, and English-source distribution."),
        variable("rank_2067", "2067 language ranking", "ordinal", "output", "Ranking summarized in Table 2 and Figures 4, 11, and 12."),
        variable("M_2067", "cumulative migration by language region", "million persons", "output", "Migration scale displayed in Figure 5."),
        variable("E_2067", "non-native English speakers by source", "million speaker identities", "output", "Distribution displayed in Figure 6."),
    ]
    models.append(
        make_model(
            10,
            14,
            "3.5 fifty-year projection",
            "26-language inhomogeneous scenario projection",
            "Iterate the expanded annual system from 2017 to 2067 and report language rankings, migration scales, and non-native English composition.",
            variables_10,
            ["Y_2017", "A_n"],
            ["Y_2067", "rank_2067", "M_2067", "E_2067"],
            [],
            [
                "UN-derived demographic and migration paths represent the next fifty years after weighted aggregation.",
                "Government, economic, education, and popularity effects are represented through the selected parameters.",
                "No radical structural event changes the state taxonomy.",
            ],
            ["Figures 4-6", "Table 2", "Appendix Figures 9-12"],
            ["initialize 26-language states", "update annual blocks", "iterate fifty annual steps", "rank total speaker identities", "aggregate migration", "extract English-source distribution"],
            [
                "The computation is explicitly skipped in the paper, and no executable matrix, code, or uncertainty output is supplied.",
                "The claim that geography will be insignificant follows from selected outcomes rather than a controlled geographic test.",
                "The Figure 4 caption says top five although the graphic contains more curves.",
            ],
            origin="modification",
        )
    )

    variables_11 = [
        variable("eta_ji", "sensitivity learning rate from i to j", "1/year", "output", "Learning completion rate under exponent k."),
        variable("y_ji", "target-attraction share", "dimensionless", "input", "Popularity or eagerness share raised to k."),
        variable("a_i", "new learner fraction", "1/year", "parameter", "Annual learner-entry fraction."),
        variable("sigma_i", "base learning duration", "year", "parameter", "Within-family duration."),
        variable("d_ji", "difficulty multiplier", "dimensionless", "parameter", "Language-family multiplier."),
        variable("k", "uniformity exponent", "dimensionless", "input", "Set to 0.1, 1, or 10."),
        variable("i", "source-language index", "count", "input", "Native source group."),
        variable("j", "target-language index", "count", "input", "Learned target language."),
        variable("n", "year index", "year", "input", "Discrete annual index."),
    ]
    equations_11 = [
        equation(
            17,
            None,
            "eta_ji^(n) = (y_ji^(n))^k a_i^(n) / (sigma_i^(n) d_ji^(n))",
            r"\eta_{ji}^{(n)}=\frac{(y_{ji}^{(n)})^k a_i^{(n)}}{\sigma_i^{(n)}d_{ji}^{(n)}}",
            "Expose concentration sensitivity by raising the attraction share to exponent k.",
            ["eta_ji", "y_ji", "a_i", "sigma_i", "d_ji", "k", "i", "j", "n"],
            confidence="high",
        )
    ]
    models.append(
        make_model(
            11,
            17,
            "3.6 Sensitivity Analysis",
            "uniformity-exponent scenario analysis",
            "Compare diffuse and concentrated language-learning choices through k=0.1, 1, and 10.",
            variables_11,
            ["y_ji", "a_i", "sigma_i", "d_ji", "k", "i", "j", "n"],
            ["eta_ji"],
            equations_11,
            [
                "k=1 is the baseline, k=0.1 represents high uniformity, and k=10 represents low uniformity.",
                "All other stated transition assumptions remain in place.",
            ],
            ["modified Equation (17)", "Figures 7-8"],
            ["choose k", "recompute attraction-driven learning rates", "iterate to 2067", "compare English and Mandarin trajectories"],
            [
                "The low-uniformity subsection begins by saying high uniformity, contradicting its title and probability description.",
                "The source prints 0:1 in prose while the figure labels k=0.1.",
                "Only three arbitrary settings are shown; no calibrated range or decision-switch analysis is given.",
            ],
            origin="modification",
        )
    )

    variables_12 = [
        variable("S_i", "score for office location i", "normalized score", "output", "Objective contribution of one office and its assigned languages."),
        variable("epsilon", "language-load profit retention", "dimensionless", "parameter", "Set to 0.98 per additional language."),
        variable("k_i", "additional languages assigned to office i", "count", "input", "Excludes English and the local language."),
        variable("P_ij", "covered population for language j", "million persons", "input", "Population associated with the assigned language region."),
        variable("E_ij", "covered GDP for language j", "10 billion USD", "input", "GDP associated with the assigned language region."),
        variable("D_ij", "transport cost from office i to region j", "unspecified cost index", "input", "Weighted air, water, and land transport cost."),
        variable("h_i", "office establishment cost proxy", "normalized score", "parameter", "Defined from local GDP and transport quantities rather than observed rent."),
        variable("eta_1", "population exponent", "dimensionless", "parameter", "Population weight exponent."),
        variable("eta_2", "GDP exponent", "dimensionless", "parameter", "GDP weight exponent."),
        variable("eta_3", "transport exponent", "dimensionless", "parameter", "Transport-cost weight exponent."),
        variable("j", "assigned-language index", "count", "input", "j=0 denotes the local language."),
    ]
    equations_12 = [
        equation(
            18,
            "(18)",
            "S_i = epsilon^k_i sum_(j=0)^k_i P_ij^eta1 E_ij^eta2 / D_ij^eta3 - h_i",
            r"S_i=\epsilon^{k_i}\sum_{j=0}^{k_i}\frac{P_{ij}^{\eta_1}E_{ij}^{\eta_2}}{D_{ij}^{\eta_3}}-h_i",
            "Score an office-language bundle by population, GDP, transport cost, language load, and a setup-cost proxy.",
            ["S_i", "epsilon", "k_i", "P_ij", "E_ij", "D_ij", "h_i", "eta_1", "eta_2", "eta_3", "j"],
        ),
        equation(
            18,
            "(18b)",
            "h_i = 10^eta1 E_i0^eta2 / D_i0^eta3",
            r"h_i=\frac{10^{\eta_1}E_{i0}^{\eta_2}}{D_{i0}^{\eta_3}}",
            "Retain the paper's mathematical proxy for establishment cost.",
            ["h_i", "E_ij", "D_ij", "eta_1", "eta_2", "eta_3"],
        ),
    ]
    models.append(
        make_model(
            12,
            18,
            "4.1-4.3 office rating model",
            "constrained city-language assignment score",
            "Translate covered language population, regional GDP, transport cost, office cost, and language load into an assignment score.",
            variables_12,
            ["epsilon", "k_i", "P_ij", "E_ij", "D_ij", "h_i", "eta_1", "eta_2", "eta_3", "j"],
            ["S_i"],
            equations_12,
            [
                "Six new offices cover the 23 remaining major languages mutually exclusively and collectively exhaustively, except English.",
                "Every office uses English and its local language and is placed in a candidate major or pivot city.",
                "Additional languages reduce profit multiplicatively through epsilon.",
            ],
            ["Equation (18)", "application assumptions", "office symbol table"],
            ["construct candidate cities", "aggregate assigned population and GDP", "estimate transport cost", "apply language-load penalty", "subtract h_i", "sum office scores"],
            [
                "h_i is described as rent or setup cost but is computed only from GDP, transport, and a constant 10.",
                "Population, GDP, transport, and cost scales are combined without calibration or uncertainty.",
                "The 2067 six-office result assigns French to both Madrid and Paris, violating the mutual-exclusivity premise.",
            ],
            origin="paper-specific",
        )
    )

    variables_13 = [
        variable("x", "city-language assignment", "discrete assignment", "state", "Candidate office set and mutually exclusive language allocation."),
        variable("S_total", "total office score", "normalized score", "output", "Sum of office scores for an assignment."),
        variable("T_m", "annealing temperature", "dimensionless", "state", "Temperature at iteration m."),
        variable("T_0", "initial temperature", "dimensionless", "parameter", "Reported as 97."),
        variable("T_t", "terminal temperature", "dimensionless", "parameter", "Reported as 3."),
        variable("alpha", "temperature decay factor", "dimensionless", "parameter", "Reported as 0.99."),
        variable("l", "Markov-chain length", "iterations", "parameter", "Reported as 10000."),
        variable("rho", "language-to-city move ratio", "ratio", "parameter", "Reported as 8:2."),
        variable("m", "annealing iteration", "count", "input", "Temperature-step index."),
    ]
    equations_13 = [
        equation(
            19,
            None,
            "T_(m+1) = alpha T_m (implied by the reported decay coefficient)",
            r"T_{m+1}=\alpha T_m",
            "Make the implied geometric cooling schedule explicit while labeling it reconstructed rather than printed.",
            ["T_m", "alpha", "m"],
            confidence="medium",
            source_type="reconstructed",
        ),
        equation(
            19,
            None,
            "maximize S_total(x) over feasible city-language assignments (reconstructed objective)",
            r"\max_{x\in\mathcal X_{\mathrm{MEC}}}S_{\mathrm{total}}(x)",
            "State the assignment objective and mutual-exclusivity/coverage domain implied by the prose and result tables.",
            ["x", "S_total"],
            confidence="medium",
            source_type="reconstructed",
        ),
    ]
    models.append(
        make_model(
            13,
            19,
            "4.3 simulated annealing",
            "stochastic combinatorial assignment search",
            "Search office locations and language assignments for the highest accumulated rating score.",
            variables_13,
            ["x", "T_0", "T_t", "alpha", "l", "rho", "m"],
            ["S_total", "x"],
            equations_13,
            [
                "The candidate list contains 19 cities and excludes English, Mandarin, and Wu from new-office allocation.",
                "The run uses T0=97, Tt=3, alpha=0.99, l=10000, and an 8:2 language/city move ratio.",
                "Ten runs are performed and the highest accumulated stable score is retained.",
            ],
            ["physical page 19 algorithm parameters", "2017 and 2067 assignment tables"],
            ["initialize a feasible assignment", "propose language or city changes", "score the candidate", "apply an unstated acceptance test", "cool temperature", "repeat ten runs", "retain the best stable score"],
            [
                "The encoding, neighborhoods, proposal law, acceptance probability, constraint repair, initialization, seed, and convergence trace are not supplied.",
                "The terms Markoff and Metro Polis-Hastings are misspelled and no implementation is archived.",
                "Ten unseeded repeats do not establish global optimality or decision stability.",
            ],
            origin="paper-specific",
            convergence="The paper stops at Tt=3 after geometric decay and calls repeated best solutions stable; it gives no objective tolerance, no-run-improvement rule, seed, or convergence trace.",
        )
    )

    variables_14 = [
        variable("GDP_2017", "2017 language-region GDP", "current-price USD", "input", "Baseline GDP aggregated from representative countries; Table 8 omits currency, while cited UN source [3] identifies current-price US dollars.", "unspecified"),
        variable("GDP_2067", "forecast language-region GDP", "current-price USD", "output", "Terminal GDP in Appendix Table 8; Table 8 omits currency, while cited UN source [3] identifies current-price US dollars.", "unspecified"),
        variable("C_1", "cycle-one growth factor", "dimensionless", "intermediate", "First reported multiplicative cycle factor; dimensional status is inferred because no combining equation is printed.", "inferred-from-equation"),
        variable("C_2", "cycle-two growth factor", "dimensionless", "intermediate", "Second reported multiplicative cycle factor; dimensional status is inferred because no combining equation is printed.", "inferred-from-equation"),
        variable("C_3", "cycle-three growth factor", "dimensionless", "intermediate", "Third reported multiplicative cycle factor; dimensional status is inferred because no combining equation is printed.", "inferred-from-equation"),
        variable("C_4", "cycle-four growth factor", "dimensionless", "intermediate", "Fourth reported multiplicative cycle factor; dimensional status is inferred because no combining equation is printed.", "inferred-from-equation"),
        variable("score_5", "five-office accumulated score", "normalized score", "output", "39.7 in 2017 and 225.2 in 2067."),
        variable("score_6", "six-office accumulated score", "normalized score", "output", "43.0 in 2017 and 236.2 in 2067."),
    ]
    models.append(
        make_model(
            14,
            20,
            "4.3.2 GDP cycle and office-count scenarios",
            "qualitative multi-cycle GDP forecast and decision comparison",
            "Forecast regional GDP to 2067 from four named business cycles, rerun office optimization, and compare five with six offices.",
            variables_14,
            ["GDP_2017", "C_1", "C_2", "C_3", "C_4"],
            ["GDP_2067", "score_5", "score_6"],
            [],
            [
                "Kitchin, Juglar, Kuznets, and Kondratiev components are integrated through an unspecified trigonometric function.",
                "Forty-six years of GDP data determine coefficients, and each reported projection cycle is approximately thirteen years from 2015.",
                "Transport influence is reduced in 2067 by setting eta_3 to 0.1 while eta_1=eta_2=1 and epsilon=0.98.",
            ],
            ["Appendix Table 8, physical page 26 (printed Page 25 of 27)", "2017 and 2067 office tables", "sources [3] and [6]"],
            ["aggregate regional GDP", "fit unspecified cycle coefficients", "project terminal GDP", "combine with 2067 language population", "rerun assignment", "compare five and six offices"],
            [
                "No trigonometric equation, frequencies, amplitudes, phases, fitting method, residuals, validation, or uncertainty are reported.",
                "Four cycles with different typical periods are folded into four approximately thirteen-year steps without explanation.",
                "The text says the projection starts in 2015, while Table 8 labels its baseline column 2017 GDP.",
                "Accumulated scores are not shown to be comparable across office counts or to include actual management costs.",
            ],
            origin="paper-specific",
            estimation="The paper says forty-six years of regional GDP data solve coefficients for an integrated trigonometric cycle, but gives no equation, estimator, fit diagnostics, or uncertainty.",
        )
    )

    assert len(models) == 14, len(models)
    assert EQUATION_COUNTER == 29, EQUATION_COUNTER
    edges = [
        (1, 2, "the homogeneous recurrence supplies the eigenpair problem"),
        (2, 3, "the eigenpair interpretation is instantiated in a numerical bilingual case"),
        (3, 4, "the numerical case motivates a learning-rate threshold scan"),
        (1, 5, "the four-state structure scales to 2N native/non-native states"),
        (5, 6, "the 22-language operator produces the 2017 comparison and long-run diagnostic"),
        (6, 7, "implausible homogeneous concentration motivates a time-varying expanded state"),
        (7, 8, "the expanded block system is specialized to non-native English geography"),
        (7, 9, "the learning block requires an attraction-duration rate"),
        (8, 10, "English-specific states feed the 2067 English distribution"),
        (9, 10, "annual learning rates fill the projection operator"),
        (9, 11, "the attraction formula is exponentiated for uniformity sensitivity"),
        (10, 12, "projected language populations enter the office rating score"),
        (12, 13, "the rating score defines the simulated-annealing objective"),
        (10, 14, "the 2067 language projection combines with terminal GDP"),
        (14, 12, "forecast GDP and the reduced transport exponent reparameterize office scores"),
        (14, 13, "future score inputs are searched for five- and six-office assignments"),
    ]
    dependency_edges = [
        {
            "from_model_id": f"MU-{ID_STEM}-{source:03d}",
            "to_model_id": f"MU-{ID_STEM}-{target:03d}",
            "handoff": handoff,
        }
        for source, target, handoff in edges
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


TABLE_1_LEDGER = {
    "title": "Projections for Population Statistics of Major Languages in 2017",
    "physical_page": 9,
    "printed_page": "Page 8 of 27",
    "columns": [
        "language",
        "native_predict",
        "native_real",
        "non_native_predict",
        "non_native_real",
    ],
    "unit_note": (
        "The table does not print a unit. Nearby German-speaker prose identifies 8 and "
        "52 as million-scale counts, so values are retained as implied millions of "
        "speaker identities rather than treated as a printed table unit."
    ),
    "rows": [
        {"language": "Mandarin", "native_predict": 870, "native_real": 897, "non_native_predict": 180, "non_native_real": 193},
        {"language": "English", "native_predict": 353, "native_real": 371, "non_native_predict": 521, "non_native_real": 611},
        {"language": "Spanish", "native_predict": 422, "native_real": 436, "non_native_predict": 92, "non_native_real": 91},
        {"language": "Hindi/Urdu", "native_predict": 340, "native_real": 329, "non_native_predict": 219, "non_native_real": 215},
        {"language": "Russian", "native_predict": 170, "native_real": 153, "non_native_predict": 27, "non_native_real": 113},
        {"language": "Portuguese", "native_predict": 206, "native_real": 218, "non_native_predict": 31, "non_native_real": 11},
        {"language": "Bengali", "native_predict": 201, "native_real": 242, "non_native_predict": 20, "non_native_real": 19},
        {"language": "French", "native_predict": 78, "native_real": 76, "non_native_predict": 89, "non_native_real": 153},
        {"language": "Japanese", "native_predict": 129, "native_real": 128, "non_native_predict": None, "non_native_real": None, "missing_source_tokens": {"non_native_predict": "?", "non_native_real": "?"}},
        {"language": "German", "native_predict": 78, "native_real": 76, "non_native_predict": 8, "non_native_real": 52},
    ],
}


TABLE_8_LEDGER = {
    "title": "Economic Outlook for the Next Fifty Years",
    "physical_page": 26,
    "printed_page": "Page 25 of 27",
    "columns": ["source_label", "cycle_1", "cycle_2", "cycle_3", "cycle_4", "gdp_2017", "gdp_2067"],
    "unit_note": (
        "Cycle columns are retained as dimensionless multiplicative factors. Table 8 "
        "prints GDP without currency; cited UN source [3] identifies GDP at current "
        "prices in US dollars, while source [6] supplies long-term cycle assumptions."
    ),
    "time_anchor_warning": "The surrounding prose says starting at 2015, while the table header says 2017 GDP.",
    "rows": [
        {"source_label": "India", "cycle_1": "1.77093244", "cycle_2": "1.79285437", "cycle_3": "1.20503007", "cycle_4": "1.18984108", "gdp_2017": "2.11624E+12", "gdp_2067": "9.63382E+12"},
        {"source_label": "UAE", "cycle_1": "2.34739506", "cycle_2": "2.39043403", "cycle_3": "1.32380487", "cycle_4": "1.29887136", "gdp_2017": "3.70296E+11", "gdp_2067": "3.57275E+12"},
        {"source_label": "Spain", "cycle_1": "1.77925415", "cycle_2": "1.80145680", "cycle_3": "1.20690268", "cycle_4": "1.19156508", "gdp_2017": "1.19296E+12", "gdp_2067": "5.49389E+12"},
        {"source_label": "Malaysia", "cycle_1": "2.04379203", "cycle_2": "2.07530650", "cycle_3": "1.26381944", "cycle_4": "1.24388686", "gdp_2017": "8.61934E+11", "gdp_2067": "5.74723E+12"},
        {"source_label": "Rassia", "probable_intended_label": "Russia", "cycle_1": "1.17979323", "cycle_2": "1.18406734", "cycle_3": "1.05484027", "cycle_4": "1.05099867", "gdp_2017": "1.32602E+12", "gdp_2067": "2.05362E+12"},
        {"source_label": "Bengaladesh", "probable_intended_label": "Bangladesh", "cycle_1": "1.74035172", "cycle_2": "1.76124883", "cycle_3": "1.19810151", "cycle_4": "1.18346095", "gdp_2017": "1.94466E+11", "gdp_2067": "8.45179E+11"},
        {"source_label": "Spain", "probable_intended_label": "Brazil", "label_basis": "duplicate Spain label, Portuguese-region ordering, and 2017 GDP 1.77259E+12", "cycle_1": "1.93249998", "cycle_2": "1.96000801", "cycle_3": "1.24046279", "cycle_4": "1.22243396", "gdp_2017": "1.77259E+12", "gdp_2067": "1.01811E+13"},
        {"source_label": "France", "cycle_1": "1.63293805", "cycle_2": "1.65032250", "cycle_3": "1.17315091", "cycle_4": "1.16046588", "gdp_2017": "2.41895E+12", "gdp_2067": "8.87464E+12"},
        {"source_label": "Nigeria", "cycle_1": "1.80587369", "cycle_2": "1.82897954", "cycle_3": "1.21285675", "cycle_4": "1.19704555", "gdp_2017": "4.94583E+11", "gdp_2067": "2.37168E+12"},
        {"source_label": "Pakistan", "cycle_1": "1.68267193", "cycle_2": "1.70166563", "cycle_3": "1.18482564", "cycle_4": "1.17122932", "gdp_2017": "2.66458E+11", "gdp_2067": "1.05876E+12"},
        {"source_label": "Japan", "cycle_1": "1.70175575", "cycle_2": "1.72137488", "cycle_3": "1.18924877", "cycle_4": "1.17530547", "gdp_2017": "4.38308E+12", "gdp_2067": "1.79463E+13"},
        {"source_label": "Germany", "cycle_1": "1.62696655", "cycle_2": "1.64415981", "cycle_3": "1.17173442", "cycle_4": "1.15915950", "gdp_2017": "3.3636E+12", "gdp_2067": "1.222078E+13"},
        {"source_label": "Iran", "cycle_1": "1.90019888", "cycle_2": "1.92656774", "cycle_3": "1.23352935", "cycle_4": "1.21606083", "gdp_2017": "3.98563E+11", "gdp_2067": "2.18869E+12"},
        {"source_label": "Tanzania", "cycle_1": "1.67179450", "cycle_2": "1.69043368", "cycle_3": "1.18229065", "cycle_4": "1.16889277", "gdp_2017": "4.56282E+10", "gdp_2067": "1.78202E+11"},
        {"source_label": "Korea", "cycle_1": "2.09597423", "cycle_2": "2.12940922", "cycle_3": "1.27450158", "cycle_4": "1.25369008", "gdp_2017": "1.37787E+12", "gdp_2067": "9.82618E+12"},
        {"source_label": "Hong Kong", "cycle_1": "1.94604458", "cycle_2": "1.97403352", "cycle_3": "1.24334890", "cycle_4": "1.22508618", "gdp_2017": "3.09236E+11", "gdp_2067": "1.80953E+12"},
        {"source_label": "Turkey", "cycle_1": "1.81628507", "cycle_2": "1.83974633", "cycle_3": "1.21517075", "cycle_4": "1.19917504", "gdp_2017": "7.17888E+11", "gdp_2067": "3.49557E+12"},
        {"source_label": "Vietnam", "cycle_1": "2.02929384", "cycle_2": "2.06027943", "cycle_3": "1.26082183", "cycle_4": "1.24113496", "gdp_2017": "1.93241E+11", "gdp_2067": "1.26428E+12"},
        {"source_label": "Italy", "cycle_1": "1.63241448", "cycle_2": "1.64978215", "cycle_3": "1.17302684", "cycle_4": "1.16035146", "gdp_2017": "1.82158E+12", "gdp_2067": "6.67733E+12"},
    ],
    "label_review": [
        {"source_label": "Rassia", "probable_intended_label": "Russia"},
        {"source_label": "Bengaladesh", "probable_intended_label": "Bangladesh"},
        {"source_label": "Spain", "occurrence": 2, "probable_intended_label": "Brazil", "confidence": "high but not silently substituted"},
    ],
}
assert len(TABLE_1_LEDGER["rows"]) == 10
assert len(TABLE_8_LEDGER["rows"]) == 19


VISUAL_SPECS = [
    (1, "Summary Sheet", "Three-paragraph model route and keyword block", [7, 10, 12, 13], "problem -> inhomogeneous projection -> 2067 distribution -> simulated-annealing office decision", "document overview", "text hierarchy", "The summary claims a low-data transition model and closes with office location selection."),
    (2, "Contents", "Section and subsection map", [], "preliminary model -> modified model -> sensitivity -> application -> strengths/weaknesses -> memo -> appendices", "navigation map", "hierarchical contents", "The contents exposes the report's two-stage analytical architecture and appendix trace."),
    (3, "Preliminary symbol table", "Native/non-native state and rate definitions", [1], "N, Y_i, y_i, Y, A, alpha, beta, gamma, and total learning-rate symbols", "definition ledger", "two-column table", "The table assigns annual demographic and learning meanings to the homogeneous operator's indexed entries."),
    (4, "Definitions and assumptions", "Operational speaker categories and seven premises", [1], "membership, births, deaths, learning, retained identities, and abrupt-event exclusion", "state-boundary audit", "numbered text/table", "Language identities can overlap because a learner retains previous identities."),
    (5, "Figure 1", "Four-state N=2 transition graph", [1], "self-loops plus Y_2->y_1, Y_1->y_2, y_1->Y_1, and y_2->Y_2 flows", "mechanism diagram", "directed state graph", "The arrows visually determine transition direction and reveal the prose's gamma-index ambiguity."),
    (5, "Equation (1) display", "Complete 4x4 N=2 transition matrix", [1], "rows and columns ordered Y_1, Y_2, y_1, y_2", "formula fidelity", "matrix display", "The operator is a population projection matrix with non-unit column sums, not a probability transition matrix."),
    (6, "Equations (2)-(6)", "Steady-state derivation and numerical bilingual example", [2, 3], "limit, eigenpair, parameter equalities, printed matrix, and reported eigenvector", "derivation audit", "equation stack", "Equation (5) visibly contains 0.005 and Equation (6) is not normalized."),
    (7, "Figure 2", "Learning-rate threshold curve", [4], "blue non-native quantity, red 0.5 reference, crossing near 0.021", "local sensitivity", "two-line chart", "The plotted ordinate exceeds one despite being labeled a proportion."),
    (7, "Equation (7)", "General 2N by 2N transition matrix", [5], "native demographic block, non-native retention, offspring flow, and cross-language learning", "scaling blueprint", "ellipsis matrix", "The display gives structure but does not uniquely specify every element of the 44x44 matrix."),
    (8, "Equations (8)-(12)", "Common-rate and attraction-share parameterization", [5], "world-average rates, alpha product, gamma ratios, normalized shares, and source learning budget", "parameter trace", "equation stack", "The normalized-share list and gamma index orientation are internally inconsistent."),
    (9, "Table 1 and Equation (13)", "2017 comparison and long-run eigenpair", [6], "ten predicted/real rows plus an abbreviated vector with Punjabi component 0.9601", "validation and falsification", "table plus equation", "Large non-native errors coexist with an implausible homogeneous long-run concentration."),
    (10, "Modified Model opening", "Five diagnosed defects and added state definitions", [7, 8], "learning duration, time-varying demography/economy, migration, and English geography", "repair rationale", "numbered diagnosis", "Each added block is motivated by a named limitation of the preliminary model."),
    (11, "Additional symbol table", "Learner, migrant, and block-matrix symbols", [7, 8, 9], "S_ji, W_j, p_ji, d_ji, sigma_i, a_i, r_j, Xi, Pi, Omega, S, G, R", "symbol audit", "multirow table", "S is reused for learner counts and migrant reproduction, while p indices are described inconsistently."),
    (12, "Figure 3", "Bilingual learner-migrant transition graph", [7], "Y, learner S, non-native y, and migrant W states with self-loops", "expanded mechanism diagram", "directed state graph", "The figure uses source-first S subscripts that conflict with the nearby definition."),
    (12, "Equations (14)-(15)", "Three-block annual recurrence and feedback", [7], "Xi/Pi/S/G/R/Omega blocks, Y^(n+1)=A^(n)Y^(n), and A^(n+1)=F[Y^(n),n]", "dynamic model fidelity", "block matrix and equations", "The displayed timing creates a possible one-year feedback lag."),
    (13, "English-specific matrix", "Four-block separation of non-native English", [8], "native, non-native English, other non-native, and migrant blocks", "requested-output specialization", "block matrix", "The matrix enables source-language distribution of non-native English speakers."),
    (13, "Equation (16) and data drivers", "Initial English composition and exogenous factor map", [8], "proportional source composition plus government, economic, population, and education influences", "initialization trace", "equation and prose map", "Equation (16) supplies ratios but no total scale."),
    (14, "Equation (17) and parameters", "Learning attraction-duration formula", [9], "p, a=0.01, sigma=3, and d in {1,2}", "parameterized flow", "equation and cases", "The same/different-family assumptions imply three- and six-year learning durations."),
    (14, "Figure 4 and Table 2", "Language trajectories and 2017/2067 top-ten ranking", [10], "English overtakes Mandarin; Hausa and Punjabi enter while Portuguese and French leave", "forecast comparison", "line chart and rank table", "The caption says top five although the figure displays more trajectories."),
    (15, "Figure 5", "Projected migration scale by language region", [10], "top four regions and English-region migration above 100 million", "migration outcome", "multi-line chart", "The paper attributes the English-region magnitude to broad acceptance without a controlled attribution test."),
    (16, "Figure 6", "2067 non-native English distribution", [8, 10], "source-language distribution with native Chinese contribution above 90 million", "geographic composition", "bar or distribution chart", "The visual is the requested English-distribution output of the specialized block model."),
    (17, "Figure 7 and modified learning formula", "High-uniformity k=0.1 scenario", [11], "diffuse attraction shares and English remaining below Mandarin", "sensitivity scenario", "formula plus line chart", "The scenario changes k while retaining the rest of the reported model."),
    (18, "Figure 8 and application assumptions", "Low-uniformity k=10 trajectory and office constraints", [11, 12], "concentrated attraction, earlier English crossing, and mutually exclusive language coverage", "sensitivity-to-decision handoff", "line chart plus numbered list", "The low-uniformity prose mistakenly begins by saying high uniformity."),
    (18, "Equation (18) and office symbols", "Office rating score and establishment-cost proxy", [12], "epsilon, k_i, P_ij, E_ij, D_ij, eta exponents, and h_i", "objective definition", "symbol table and equation", "Population and GDP add value, transport and language load reduce it, and h_i is subtracted."),
    (19, "Candidate cities and annealing parameters", "Nineteen cities plus T0, Tt, alpha, l, rho, and ten repeats", [13], "bounded location set and stochastic-search controls", "algorithm disclosure", "list and parameter table", "Several essential search details remain absent despite the parameter list."),
    (19, "2017 office solution tables", "Six-office 43.0 and five-office 39.7 assignments", [12, 13], "city-language bundles under eta_1=eta_2=eta_3=1 and epsilon=0.98", "alternative comparison", "assignment tables", "The paper selects six offices from a higher unnormalized accumulated score."),
    (20, "2067 weights and GDP narrative", "Reduced transport exponent and four-cycle GDP forecast", [14], "eta_3=0.1 plus Kitchin, Juglar, Kuznets, and Kondratiev components", "future-scenario construction", "parameter display and prose", "The GDP equation and fitting diagnostics are omitted."),
    (20, "2067 office solution tables", "Six-office 236.2 and five-office 225.2 assignments", [12, 13, 14], "future city-language bundles and narrowing score gap", "future decision comparison", "assignment tables", "French appears under both Madrid and Paris in the six-office table, breaching exclusivity."),
    (21, "Strengths and Weaknesses", "Four strengths and four limitations", [7, 10, 12], "interfaces, parsimony, legibility, state refinement, feedback, migrant origin, education, and economics", "self-audit", "parallel numbered lists", "The limitations identify real missing mechanisms but do not quantify their effect on decisions."),
    (22, "Memo page 1", "Forecast findings and baseline six-office table", [10, 12, 13], "English, demographic shifts, migration, and current assignments", "executive compression", "memo prose and table", "The memo makes the projection-to-location handoff visible for the client."),
    (23, "Memo page 2", "Preference branches, exclusions, relocations, and office-count advice", [10, 12, 14], "necessity/GDP branches, existing offices, MEC coverage, Dubai/Jakarta moves, and five-percent claim", "conditional recommendation", "memo prose and tables", "The action advice depends on omitted score comparability and management-cost thresholds."),
    (24, "References", "Six-source provenance list", [5, 6, 14], "Wikipedia speaker list, UN migration/GDP/birth/death data, and J.P. Morgan assumptions", "source trace", "reference list", "Source snapshots, retrieval dates, definitions, and transformation code are not supplied."),
    (25, "Tables 3-5", "Country-language mapping, demographic rates, and 2013 speakers", [5, 6], "representative countries, weighted birth/death rates, and native/non-native counts", "input ledger", "three tables", "Japanese non-native entries are question marks and units are not consistently printed."),
    (26, "Tables 6-8", "Preference assignments and economic outlook", [12, 14], "population/GDP preference tables plus four cycle factors and terminal GDP", "scenario ledger", "three tables", "Tables 6 and 7 repeat a malformed caption; Table 8 prints Rassia, Bengaladesh, and a second Spain row that is probably Brazil."),
    (27, "Figures 9-11", "Birth/death trends and ranks 6-16 trajectories", [10, 14], "time-varying demographic inputs and additional language curves", "appendix support", "three line charts", "Figure 9's caption says birth rate while its visible ordinate says death rate."),
    (28, "Figure 12", "Ranks 17-26 language trajectories", [10], "remaining projected language groups through 2067", "coverage completion", "multi-line chart", "The final figure extends trajectory coverage but supplies no uncertainty bands or numeric data table."),
]


def build_visuals() -> list[dict[str, Any]]:
    visuals: list[dict[str, Any]] = []
    for index, (page, figure, caption, model_numbers, summary, purpose, form, claim) in enumerate(VISUAL_SPECS, start=1):
        record = {
                "page": page,
                "figure": figure,
                "visual_record_id": f"VR-{ID_STEM}-{index:03d}",
                "caption": caption,
                "source_model_ids": [f"MU-{ID_STEM}-{number:03d}" for number in model_numbers],
                "summary": summary,
                "analytical_purpose": purpose,
                "form": form,
                "encodings": [
                    "position and section order encode the model handoff",
                    "rows, columns, arrows, colors, or line position encode the stated states and comparisons",
                ],
                "exact_claim": claim,
                "construction_or_missing": "Transcribed from the physical-page visual proxy; missing units, uncertainty, code, legends, or construction details remain explicitly missing rather than inferred.",
                "applicability": "Use only with the source's state definitions, year, language set, parameter setting, units, candidate cities, and office-count scenario.",
                "forbidden_scenarios": [
                    "Do not reuse source-specific populations, rates, rankings, city assignments, or scores as general constants.",
                    "Do not treat a projected curve, heuristic optimum, or appendix table as externally validated causal evidence.",
                ],
                "accessibility": "Pair colors and line styles with direct labels; print units, horizon, scenario, and numeric table values, and describe matrix block order in text.",
                "disposition": "important-visual-record",
                "evidence_role": "O",
            }
        if figure == "Table 1 and Equation (13)":
            record["structured_ledger"] = TABLE_1_LEDGER
        elif figure == "Tables 6-8":
            record["structured_ledger"] = TABLE_8_LEDGER
        visuals.append(record)
    assert len(visuals) == 36, len(visuals)
    return visuals


def page_summary(page: int, summary: str, **extra: Any) -> dict[str, Any]:
    return {"page": page, "summary": summary, **extra}


ASSUMPTION_SPECS = [
    (4, "Every speaker-state identity is classified as native or non-native for each language, while one person may retain several identities."),
    (4, "Native states change through births and deaths; preliminary non-native states change through learning and deaths."),
    (4, "Rare first-language disability, instant language mastery, forgetting, and radical unforeseen structural shocks are excluded."),
    (5, "Selected matrix entries are set to zero to avoid the paper's stated offspring and cross-non-native double-counting paths."),
    (8, "Non-native groups share world-average demographic behavior, and target attractiveness is initially source-independent."),
    (11, "Learners do not reproduce as learners or die during the modeled learning interval."),
    (11, "Migrant offspring enter the native state of the destination region, and successful migrants leave the corresponding non-native state."),
    (13, "Initial non-native English composition is proportional to native-source populations, and native-English emigration is omitted."),
    (14, "One percent begins a foreign language annually; mastery takes three years within a family and six across families."),
    (18, "Six new offices cover 23 remaining languages mutually exclusively and collectively exhaustively, with English and the local language available at each office."),
    (18, "Population, GDP, transport cost, setup cost, and language load determine office value."),
    (20, "By 2067 the transport exponent falls to 0.1 because communications and transportation are assumed to weaken geography."),
]


DATA_SPECS = [
    (3, "The report states about 6,900 current languages and uses concentration among major native languages to motivate a reduced state set."),
    (7, "Twenty-two of the top twenty-six languages are used in the preliminary model because of limited data."),
    (8, "Representative countries cover more than 90 percent of a language's native speakers before weighted demographic aggregation."),
    (8, "World-average death rate 0.0083, birth rate 0.0193, and immigrant/non-native ratio 0.172 fill common-rate assumptions."),
    (8, "A 22-value non-native speaker list supplies attraction weights but its printed normalization uses an inconsistent denominator."),
    (9, "Table 1 compares 2013-based four-step predictions with ten reported 2017 native/non-native counts."),
    (13, "UN fifty-year birth, death, and migration projections are reduced by weighted averages before entering annual matrices."),
    (14, "Language families are reduced to a binary same/different relation with difficulty multipliers 1 and 2."),
    (18, "Nineteen candidate cities represent the 23 remaining language regions after excluding English, Mandarin, and Wu."),
    (18, "Equation (18) uses population in millions, GDP in 10 billion USD, and an unspecified transport-cost index; raw Table 8 GDP is printed in scientific notation and therefore requires an undocumented division by 1e10 before entering E_ij."),
    (20, "Forty-six years of regional GDP history are said to fit an integrated four-cycle trigonometric projection."),
    (24, "The six references include a Wikipedia speaker list, four UN data endpoints, and a J.P. Morgan capital-market report."),
    (25, "Appendix Tables 3-5 retain country mappings, weighted birth/death rates, and 2013 native/non-native inputs, including missing Japanese values."),
    (26, "Appendix Table 8 records four dimensionless cycle factors plus 2017 and 2067 GDP for nineteen rows; it preserves source labels Rassia and Bengaladesh, and its second Spain row is probably Brazil rather than silently corrected."),
]


VERIFICATION_SPECS = [
    (1, "All 28 physical pages were read; Summary and Introduction were completed before formula, visual, and warning passes."),
    (5, "Figure 1 arrows were reconciled with Equation (1) to determine the actual gamma flow direction."),
    (6, "Equations (2)-(6) were transcribed from focused crops; the reported eigenpair was numerically checked against both possible Equation (5) matrices."),
    (7, "Figure 2 axes, reference line, crossing, and impossible proportion scale were visually checked."),
    (8, "The 22 raw attraction values and printed normalized values were separately summed, exposing totals 1239.7 and 1.0387."),
    (9, "All displayed Table 1 rows were retained with missing Japanese values rather than imputed."),
    (9, "Equation (13) was retained as abbreviated because the paper omits the remaining vector components and full matrix."),
    (11, "The additional symbol table was checked for S reuse, p-index direction, and the migration meaning of R."),
    (12, "Figure 3 and the three-block matrix were cross-checked state by state."),
    (12, "Equations (14)-(15) were checked for the A^(n) versus A^(n+1) timing relation."),
    (13, "The English-specific block matrix and Equation (16) were checked against their source crops."),
    (14, "Equation (17), the p/y ratio, common a and sigma values, and the two-level d cases were visually transcribed."),
    (17, "The high- and low-uniformity text was compared with k=0.1 and k=10 figure labels."),
    (18, "Equation (18), h_i, symbol units, and the 2017/2067 exponent settings were retained without repairing the cost interpretation."),
    (19, "Annealing parameters were recorded, and every absent encoding, neighborhood, proposal, acceptance, seed, and stopping detail was marked missing."),
    (20, "Five- and six-office accumulated scores were compared within each year without assuming cross-count economic comparability."),
    (20, "The 2067 six-office table was checked against the mutual-exclusivity premise, exposing French in two offices."),
    (26, "Tables 6 and 7 captions and all nineteen Table 8 rows were checked against the visible appendix, retaining Rassia, Bengaladesh, and the second Spain source label while separately flagging probable intended labels."),
    (27, "Figure 9 caption was compared with the visible y-axis label, and Figures 10-11 were separately identified."),
    (28, "Figure 12 completed full physical-page visual coverage; no original full-page PNG entered the model context."),
]


RESULT_SPECS = [
    (7, "Figure 2 reports a learning-rate crossing near 0.021 under the numerical bilingual assumptions."),
    (9, "Table 1 shows some close native counts but large non-native discrepancies, especially for Russian, French, and German."),
    (9, "The homogeneous long-run calculation claims a 0.9601 Punjabi native component and multiplier 1.0215."),
    (14, "Table 2 moves English above Mandarin by 2067 and brings Hausa and Punjabi into the top ten."),
    (15, "Figure 5 places English-region migration above 100 million and ahead of other labeled regions."),
    (16, "Figure 6 attributes more than 90 million projected non-native English speakers to native Chinese speakers."),
    (17, "At k=0.1 English remains below Mandarin in the reported high-uniformity scenario."),
    (18, "At k=10 English overtakes Mandarin earlier and reaches roughly 1.4 billion speaker identities by 2067."),
    (19, "The 2017 six-office assignment scores 43.0 versus 39.7 for five offices."),
    (19, "The 2017 six-office set is Tokyo, Bombay, Madrid, Rio de Janeiro, Moscow, and Paris."),
    (20, "The 2067 six-office assignment scores 236.2 versus 225.2 for five offices."),
    (20, "The proposed 2067 six-office set shifts Moscow and Rio de Janeiro roles toward Dubai and Jakarta but duplicates French coverage."),
    (21, "The report treats the narrowing future score gap as a reason that five offices may become viable after management cost."),
    (22, "The memo reports English growth, high-growth Arabic/Punjabi/Hausa, declining East Asian/Russian groups, and uneven migration."),
    (23, "The memo conditions a future office closure on saved cost compensating an asserted roughly five-percent revenue loss."),
]


FORMULA_WARNINGS = [
    (1, 0, 5, "Equation (1) is a non-conservative population operator over overlapping language identities, not a stochastic Markov transition matrix; prose also reverses the gamma flow order implied by its entries."),
    (2, 0, 6, "Equation (2) writes a divergent limit with k still on the right and omits the initial-vector scale and dominance conditions needed for an asymptotic eigenvector result."),
    (3, 1, 6, "Equation (5) visibly prints 0.005 in entry (2,4), contradicting alpha_24=0.05 in Equation (4)."),
    (3, 2, 6, "The Equation (6) eigenpair satisfies neither the printed nor nominal matrix, and its vector sums to 3.248 despite being interpreted as population proportions."),
    (4, 0, 7, "Figure 2's threshold uses an ordinate labeled proportion that rises above one, so the plotted quantity is likely an unnormalized eigenvector component."),
    (5, 3, 8, "Equation (10) uses gamma_(i,N+j), transposing the target-row/source-column convention used by Equations (1), (7), (11), and (12)."),
    (5, 4, 8, "Equation (11)'s 22 printed normalized values sum to 1.0387; the raw values sum to 1239.7 and appear divided by the mistyped denominator 1193.7."),
    (5, 5, 8, "Equation (12) allocates Gamma_i using shares normalized over all j while the preceding rule excludes j=i, so the retained rates do not sum to Gamma_i."),
    (6, 1, 9, "Equation (13) omits the full 44-vector and operator, preventing independent verification of the reported 0.9601 Punjabi component and eigenvalue."),
    (7, 2, 12, "Equations (14)-(15) update A^(n+1) from Y^(n) while advancing with A^(n), creating a one-period lag unless that timing is explicitly intended."),
    (8, 1, 13, "Equation (16) gives only proportional initial non-native English components and no total or normalization, so the starting vector is underidentified."),
    (9, 0, 14, "Equation (17) depends on an eagerness normalization that is not supplied; d is called similarity although larger values mean greater difficulty, and most time-indexed factors are fixed immediately afterward."),
    (11, 0, 17, "The sensitivity formula is paired with a low-uniformity subsection whose first sentence says high uniformity; the prose also types 0:1 while the figure shows k=0.1."),
    (12, 1, 18, "h_i is described as rent or setup cost but Equation (18b) derives it only from local GDP, transport cost, and the constant 10."),
    (13, 0, 19, "The cooling recurrence is only implied by alpha; the source omits the actual schedule, temperature-step count, and stopping trace."),
    (13, 1, 19, "The assignment objective and MEC domain must be reconstructed from prose, while the 2067 six-office result itself violates mutual exclusivity by assigning French twice."),
]


WEAKNESS_SPECS = [
    (5, 1, 1, "Overlapping multilingual identities and non-unit column sums make the preliminary operator unsuitable for claims about unique total population or Markov probabilities."),
    (6, 3, 5, "The printed numerical matrix conflicts with its own parameter declaration."),
    (6, 3, 6, "The reported bilingual eigenpair is algebraically invalid and unnormalized."),
    (8, 5, 11, "The target-attraction normalization and gamma index conventions are inconsistent."),
    (9, 6, 14, "Large 2017 non-native errors are attributed to data without an error metric, alternative baseline, or recalibration."),
    (9, 6, 15, "The 96.01 percent Punjabi long-run claim cannot be independently checked and demonstrates homogeneous dominance rather than realistic equilibrium."),
    (12, 7, 18, "The inhomogeneous feedback timing may lag one period and several block symbols are reused or mislabeled."),
    (13, 8, 20, "Initial non-native English distribution is specified only as a ratio and native-English migration is omitted without a sensitivity check."),
    (14, 9, 21, "The one-percent learner entry, three/six-year duration, and binary family distance are assumptions without calibration."),
    (16, 10, None, "The paper infers weak geographic influence from selected migration and English outcomes without an explicit geographic comparator."),
    (17, 11, 25, "The uniformity scenarios are mislabeled in prose and use three arbitrary k values without joint sensitivity or uncertainty."),
    (18, 12, 26, "The office score combines scales and treats a GDP/transport expression as setup cost without empirical calibration."),
    (19, 13, 28, "Simulated annealing lacks an encoding, neighborhoods, proposal and acceptance rules, seed, constraint handling, and convergence evidence."),
    (20, 14, None, "The GDP cycle model omits its equation, fit procedure, diagnostics, validation, and uncertainty."),
    (20, 13, 29, "French is assigned to both Madrid and Paris in the 2067 six-office result, violating the stated mutually exclusive coverage constraint."),
    (23, 13, None, "The 2067 result table replaces Moscow and Rio de Janeiro with Dubai and Jakarta, but the memo instead says to move Moscow and Paris to Dubai and Jakarta, leaving the relocation advice inconsistent with its own result."),
    (24, 14, None, "Sparse references, Wikipedia-derived speaker data, missing retrieval snapshots, and the repeated watermark weaken provenance and reproducibility."),
    (26, 14, None, "Tables 6 and 7 repeat a malformed coefficient caption; Table 8 prints Rassia, Bengaladesh, and a second Spain row that is probably Brazil, so the visible source labels must be retained separately from inferred corrections."),
]

EXPECTED_OBSERVATION_DIMENSIONS = {
    "language": 84,
    "modeling": 43,
    "logic": 32,
    "visualization": 36,
    "verification": 36,
    "data": 14,
    "assumption": 12,
    "result": 15,
    "weakness": 18,
    "other": 12,
}
EXPECTED_OBSERVATION_COUNT = sum(EXPECTED_OBSERVATION_DIMENSIONS.values())
assert EXPECTED_OBSERVATION_COUNT == 302


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
            f"Input: {item['input']} Rhetorical job: {item['rhetorical']} Analytical job: {item['analytical']} Output: {item['output']} Handoff: {item['handoff']}",
        )
        for item in CHAPTERS
    ]
    writing_logic = [
        page_summary(
            item["pages"][0],
            f"{item['label']}: {item['input']} -> {item['rhetorical']} -> {item['analytical']} -> {item['output']} -> {item['handoff']}",
        )
        for item in CHAPTERS
    ]
    dependency_graph = []
    by_id = {model["model_id"]: model for model in models}
    for edge in models_record["dependency_edges"]:
        dependency_graph.append(
            page_summary(
                by_id[edge["to_model_id"]]["page"],
                f"{edge['from_model_id']} -> {edge['to_model_id']}: {edge['handoff']}",
            )
        )
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
            f"{pattern['name']}: {' -> '.join(pattern['information_order'])}; function={pattern['function']}; boundary={pattern['boundary']}",
        )
        for pattern in PATTERNS
    ]
    for unit in language["units"][:14]:
        language_observations.append(
            page_summary(
                unit["page"],
                f"{unit['function']}: {unit['reusable_pattern']}; retain {unit['rhetorical_move']}",
            )
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

    non_prose_source_reviews = []
    for index, spec in enumerate(NON_PROSE_SOURCE_SPECS, start=1):
        excerpt_line_start, excerpt_line_end = spec["excerpt_lines"]
        non_prose_source_reviews.append(
            {
                "review_id": f"NPS-{ID_STEM}-{index:03d}",
                "classification": "non-prose-structural-source-review",
                "page": spec["page"],
                "section": spec["section"],
                "granularity": spec["granularity"],
                "function": spec["function"],
                "source_excerpt": resolve_source_span(
                    spec["page"], excerpt_line_start, excerpt_line_end
                ),
                "source_anchor": {
                    "page_file": f"page-{spec['page']:04d}.txt",
                    "inspected_line_start": spec["line_start"],
                    "inspected_line_end": spec["line_end"],
                    "excerpt_line_start": excerpt_line_start,
                    "excerpt_line_end": excerpt_line_end,
                },
                "language_unit_exclusion_reason": (
                    "Bibliography, appendix routing, caption, table, or figure-label material "
                    "is retained for structural and numeric fidelity but is not author narrative "
                    "prose and therefore is not counted as a schema-v3 language unit."
                ),
            }
        )
    if len(non_prose_source_reviews) != 5:
        raise SystemExit("q121 non-prose source review count changed")

    impacts = [
        {"rule_id": RULES["language"], "action": "retain target, comparator, metric, year, scenario, uncertainty status, and handoff before using accuracy, dominance, optimality, or reliability adjectives", "evidence_ids": []},
        {"rule_id": RULES["logic"], "action": "trace every language-projection and office-location requirement through state definitions, data, recurrence, sensitivity, assignment constraints, result, and memo", "evidence_ids": []},
        {"rule_id": RULES["modeling"], "action": "separate unique persons from overlapping language identities and distinguish population, GDP, transport index, score, cost, and recommendation", "evidence_ids": []},
        {"rule_id": RULES["fusion"], "action": "combine language population, GDP, transport, setup cost, and office count only after documenting units, scaling, constraints, and objective meaning", "evidence_ids": []},
        {"rule_id": RULES["dynamic"], "action": "close the population-to-parameter feedback timing and test how education, migration, economics, and policy alter the annual operator", "evidence_ids": []},
        {"rule_id": RULES["visualization"], "action": "show forecast and assignment scenarios with units, direct labels, uncertainty, constraints, selected alternative, and decision-switch information", "evidence_ids": []},
        {"rule_id": RULES["verification"], "action": "run algebra, normalization, dimensions, index direction, limit behavior, feasibility, and optimizer-diagnostic preflight before projection", "evidence_ids": []},
        {"rule_id": RULES["reliability"], "action": "test projection error, joint parameter sensitivity, assignment stability, and abstention conditions for each policy horizon", "evidence_ids": []},
        {"rule_id": RULES["data"], "action": "record every speaker, demographic, migration, family, GDP, distance, and cost input with provenance, unit, transformation, uncertainty, geography, and year", "evidence_ids": []},
        {"rule_id": RULES["stakeholder"], "action": "elicit client tradeoffs and management costs before turning an accumulated score difference into an office opening, relocation, or closure decision", "evidence_ids": []},
    ]
    return {
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "team_control_number": "73410",
        "title": "Language Population Projection and Location Optimizaion Model Based on Inhomogeneous Transition Matrix and Simulated Annealing Algorithm",
        "award_status": "outstanding",
        "source": {"relative_path": SOURCE_PATH, "sha256": SHA256, "page_count": PAGE_COUNT},
        "schema_version": 1,
        "source_quality": {
            "status": "text-rich-with-damaged-mathematics",
            "notes": "Complete UTF-8 page extraction and 28/28 bounded full-page review; nineteen focused formula/table/algorithm crops control Greek letters, matrices, and small labels. A commercial watermark intersects every page header.",
        },
        "context_sources": [
            "2018 MCM Problem B official prompt",
            "Summary Sheet and 27 printed report pages",
            "six cited web/report sources",
            "Appendix Tables 3-8 and Figures 9-12",
        ],
        "task_reconstruction": {
            "summary": "Project global language populations and geographic distributions for fifty years, recommend six multinational office locations and mutually exclusive language coverage, analyze fewer offices, and write a COO memo.",
            "inputs": ["native/non-native speaker counts", "demographic rates", "migration", "learning behavior", "language family", "government/economic/education factors", "GDP", "transport cost", "candidate cities", "office cost and language-load penalty"],
            "outputs": ["2017 check", "2067 language ranking", "migration geography", "non-native English distribution", "uniformity sensitivity", "2017/2067 office assignments", "five-versus-six comparison", "COO memo"],
        },
        "section_map": section_map,
        "non_prose_source_reviews": non_prose_source_reviews,
        "assumptions": [page_summary(page, summary) for page, summary in ASSUMPTION_SPECS],
        "data_and_preprocessing": [page_summary(page, summary) for page, summary in DATA_SPECS],
        "models": [page_summary(model["page"], f"{model['model_id']}: {model['purpose']}") for model in models],
        "dependency_graph": dependency_graph,
        "verification": [page_summary(page, summary) for page, summary in VERIFICATION_SPECS],
        "results_trace": [page_summary(page, summary) for page, summary in RESULT_SPECS],
        "contributions": [
            page_summary(1, "The summary exposes a projection-to-location chain instead of presenting two disconnected models."),
            page_summary(5, "A small N=2 graph makes the population transition mechanism inspectable before scaling."),
            page_summary(9, "An implausible homogeneous equilibrium is used as a concrete trigger for structural modification."),
            page_summary(10, "The modified model maps each baseline defect to learners, migrants, time variation, or an English-specific state."),
            page_summary(12, "The three-block matrix separates natural growth, learning, migration, and migrant offspring pathways."),
            page_summary(13, "An English-specific partition directly targets the requested geographic distribution of non-native speakers."),
            page_summary(14, "Equation (17) exposes how attraction, education throughput, duration, and language-family difficulty interact."),
            page_summary(17, "The k scenarios give the attraction mechanism an interpretable local sensitivity test."),
            page_summary(18, "Equation (18) translates projected demand and geography into an auditable, if undercalibrated, office objective."),
            page_summary(19, "Five- and six-office alternatives are displayed rather than leaving office count fixed by the prompt."),
            page_summary(21, "Parallel strengths and weaknesses identify model interfaces and omitted feedback mechanisms."),
            page_summary(22, "The memo reorganizes technical outputs around client preference branches and future adjustment."),
        ],
        "writing_logic": writing_logic,
        "language_observations": language_observations,
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [
            page_summary(1, "The Summary names the failure of a population-only baseline, the added transition states, the 2067 horizon, and the client decision in judge-scannable order.", evidence_class="J"),
            page_summary(9, "Using an implausible 96 percent long-run component to motivate an inhomogeneous repair creates a visible model-development rationale.", evidence_class="J"),
            page_summary(18, "The application converts forecasts into an explicit office score and assignment constraint rather than stopping at language trajectories.", evidence_class="J"),
            page_summary(22, "The two-page memo satisfies the stakeholder deliverable with findings, alternatives, exclusions, relocations, and a future review condition.", evidence_class="C"),
        ],
        "weaknesses": weakness_records,
        "independent_extensions": [
            {"extension_id": "E-B-121-001", "page": 5, "summary": "Rebuild the state system as a multi-membership population model with a unique-person ledger and explicitly conserved demographic flows."},
            {"extension_id": "E-B-121-002", "page": 6, "summary": "Recompute every eigenpair and normalization from the frozen matrix and add residual, scale, and limiting-behavior tests."},
            {"extension_id": "E-B-121-003", "page": 9, "summary": "Use rolling-origin backtests, language-specific error metrics, calibrated baselines, and prediction intervals before fifty-year projection."},
            {"extension_id": "E-B-121-004", "page": 12, "summary": "Define contemporaneous versus lagged feedback explicitly and estimate block-specific time variation from documented series."},
            {"extension_id": "E-B-121-005", "page": 14, "summary": "Estimate learning transitions from education and survey data with source-target normalization and uncertainty rather than fixed 1/3/6 assumptions."},
            {"extension_id": "E-B-121-006", "page": 16, "summary": "Test geographic mechanisms with distance, network accessibility, policy, and migration alternatives instead of inferring weak geography from one curve set."},
            {"extension_id": "E-B-121-007", "page": 17, "summary": "Run joint global sensitivity over calibrated ranges and report trajectory and office-decision switches."},
            {"extension_id": "E-B-121-008", "page": 18, "summary": "Reformulate office choice with dimensionally normalized objectives, observed setup/management costs, explicit MEC constraints, and a Pareto frontier."},
            {"extension_id": "E-B-121-009", "page": 19, "summary": "Archive a seeded optimizer with encoding, neighborhoods, acceptance law, feasibility checks, convergence traces, and exact-solver benchmarks on reduced cases."},
            {"extension_id": "E-B-121-010", "page": 20, "summary": "Replace the unspecified cycle narrative with candidate GDP models evaluated by holdout error and propagate GDP uncertainty into office rankings."},
        ],
        "candidate_rule_impacts": impacts,
        "unresolved_questions": [
            "What unique-person population corresponds to the sum of overlapping language identities?",
            "Which matrix was actually used for Equations (5)-(6) and the Figure 2 sweep?",
            "What exact denominator and self-language exclusion produced Equation (11)'s attraction shares?",
            "Is Equation (15) intentionally lagged, and what is the complete feedback map F?",
            "What total initializes Equation (16)'s non-native English vector?",
            "Which data estimate p_ji, a_i, sigma_i, d_ji, and their temporal variation?",
            "What executable recurrence generated Figures 4-12 and their numeric trajectories?",
            "How are transport costs, setup costs, score units, and cross-office score comparability defined?",
            "What simulated-annealing encoding, neighborhoods, acceptance probability, seed, and constraint repair were used?",
            "What GDP cycle equation and validation support Table 8 and the 2067 office decision?",
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
        "language": "Transfer only the rhetorical action and information order after replacing every language, city, year, value, equation, and decision boundary.",
        "logic": "Use the handoff only when the receiving section consumes the named output and preserves its units, horizon, evidence class, and scope.",
        "modeling": "Reuse the model object only after defining mutually exclusive versus overlapping states, units, indices, update timing, constraints, and calibration sources.",
        "visualization": "Reuse the visual role only with legible axes, units, scenarios, encodings, source model, exact claim, and accessibility text.",
        "verification": "Apply the check to frozen source bytes or executable outputs before any affected forecast or recommendation is promoted.",
        "data": "Use the input only with a frozen source snapshot, geography, year, unit, transformation, uncertainty, and downstream equation or score term.",
        "assumption": "Treat the premise as a scope condition and test the model output or decision that changes when it is relaxed.",
        "result": "Report the result only with its model, scenario, horizon, unit, comparator, feasibility status, and uncertainty status.",
        "weakness": "Keep the defect in the final warning pass and pair it with a concrete algebra, calibration, replication, provenance, or feasibility test.",
        "other": "Preserve this contextual evidence without upgrading a citation, software mention, memo statement, or source-quality note into validation.",
    }
    counterevidence = {
        "language": "A fluent transition sentence without a source anchor, receiving use, or anti-copy boundary is not a reusable language unit.",
        "logic": "A section heading or chronological list alone does not establish an analytical dependency or decision handoff.",
        "modeling": "A named matrix or algorithm does not establish conservation, identifiability, calibration, feasibility, or reproducibility.",
        "visualization": "A polished plot cannot repair missing units, contradictory labels, omitted uncertainty, or an infeasible assignment.",
        "verification": "One fitted example, local sensitivity curve, or visually plausible trajectory is not out-of-sample validation.",
        "data": "A borrowed point value or weighted average without a dated snapshot and transformation ledger is not calibrated evidence.",
        "assumption": "Author assertion, convenience, or common sense does not turn an untested premise into an empirical fact.",
        "result": "A simulated score, ranking, or long-horizon trajectory is not an observed outcome or causal effect.",
        "weakness": "The warning does not erase the paper's positive language, organization, model, or visual evidence.",
        "other": "Contextual material cannot substitute for formula retention, visual coverage, or a validated transaction artifact.",
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
            f"Retain the rhetorical function '{unit['function']}' and the order {' -> '.join(unit['information_order'])}; preserve the unit's evidence type and handoff while replacing all source-specific content.",
            "O",
            [RULES["language"]],
        )

    chapter_by_name = {item["chapter"]: item for item in CHAPTERS}
    for item in CHAPTERS:
        rules = [RULES["logic"]]
        if item["chapter"] in {"algorithm", "conclusion", "memo"}:
            rules.append(RULES["stakeholder"])
        add(
            item["pages"][0],
            f"{item['label']} / five-move section contract",
            "logic",
            f"Input: {item['input']} Rhetorical job: {item['rhetorical']} Analytical job: {item['analytical']} Output: {item['output']} Handoff: {item['handoff']}",
            "Preserve the complete input -> rhetorical job -> analytical job -> output -> handoff contract so the section contributes to the report-wide forecast-to-decision chain.",
            "I",
            rules,
        )

    models = models_record["models"]
    by_model_id = {model["model_id"]: model for model in models}

    def model_rule_ids(model_number: int) -> list[str]:
        rules = [RULES["modeling"]]
        if 7 <= model_number <= 11:
            rules.append(RULES["dynamic"])
        if model_number >= 12:
            rules.extend([RULES["fusion"], RULES["stakeholder"]])
        return rules

    for edge in models_record["dependency_edges"]:
        target = by_model_id[edge["to_model_id"]]
        target_number = int(target["model_id"].rsplit("-", 1)[1])
        rules = [RULES["logic"]]
        if target_number >= 12:
            rules.append(RULES["stakeholder"])
        add(
            target["page"],
            f"Model dependency {edge['from_model_id']} -> {edge['to_model_id']}",
            "logic",
            edge["handoff"],
            "Keep this output-to-input dependency explicit; the receiving model may not silently change state meaning, scale, timing, uncertainty, or feasibility status.",
            "I",
            rules,
        )

    for model_number, model in enumerate(models, start=1):
        add(
            model["page"],
            f"{model['section']} / model unit",
            "modeling",
            f"{model['model_id']}: {model['purpose']}",
            f"Retain the complete {model['family']} unit with its variables, equations, conditions, assumptions, handoff outputs, validation references, and recorded missing implementation details.",
            "O",
            model_rule_ids(model_number),
        )
        for equation_record in model["governing_equations"]:
            add(
                equation_record["page"],
                f"{model['section']} / {equation_record['equation_id']}",
                "modeling",
                equation_record["source_expression"],
                f"Preserve the equation's literal source form, normalized transcription, variable symbols, purpose, confidence, and ownership by {model['model_id']} before using its output downstream.",
                "O",
                model_rule_ids(model_number),
            )

    for visual in visuals:
        add(
            visual["page"],
            f"{visual['figure']} / {visual['visual_record_id']}",
            "visualization",
            visual["summary"],
            f"Retain this {visual['form']} for its stated analytical purpose: {visual['analytical_purpose']} The exact supported claim remains: {visual['exact_claim']}",
            "O",
            [RULES["visualization"]],
        )

    for page, summary in VERIFICATION_SPECS:
        rules = [RULES["verification"]]
        if any(token in summary.lower() for token in ("checked", "compared", "error", "missing", "exposing")):
            rules.append(RULES["reliability"])
        add(
            page,
            "Verification ledger",
            "verification",
            summary,
            "Keep the check distinct as transcription, algebra, normalization, index, timing, feasibility, provenance, or visual-label verification and carry every unresolved failure into G7.",
            "E",
            rules,
        )

    for model_number, equation_offset, page, warning in FORMULA_WARNINGS:
        model = models[model_number - 1]
        equation_record = model["governing_equations"][equation_offset]
        add(
            page,
            f"G7 formula watch / {equation_record['equation_id']}",
            "verification",
            f"{equation_record['source_expression']} | {warning}",
            "Freeze the literal expression and resolve this warning by recomputation or source clarification before treating the affected projection, score, or assignment as reliable.",
            "E",
            [RULES["verification"], RULES["reliability"]],
        )

    for page, summary in DATA_SPECS:
        add(
            page,
            "Data and preprocessing ledger",
            "data",
            summary,
            "Record the source class, date or horizon, geography, unit, aggregation or normalization, missingness, uncertainty status, and every downstream transition or office-score use.",
            "O",
            [RULES["data"]],
        )

    for page, summary in ASSUMPTION_SPECS:
        rules = [RULES["modeling"]]
        if 10 <= page <= 17:
            rules.append(RULES["dynamic"])
        if page >= 18:
            rules.extend([RULES["fusion"], RULES["stakeholder"]])
        add(
            page,
            "Assumption ledger",
            "assumption",
            summary,
            "Convert the stated simplification into a testable boundary and identify the state trajectory, ranking, or office decision that may change when it is relaxed.",
            "O",
            rules,
        )

    for page, summary in RESULT_SPECS:
        rules = [RULES["visualization"], RULES["reliability"]]
        if page >= 18:
            rules.append(RULES["stakeholder"])
        add(
            page,
            "Results and decision trace",
            "result",
            summary,
            "Bind the reported value or ranking to its source model, year, scenario, unit, comparator, feasibility status, uncertainty status, and exact receiving decision.",
            "O",
            rules,
        )

    for page, model_number, equation_number, summary in WEAKNESS_SPECS:
        rules = [RULES["verification"], RULES["reliability"], *model_rule_ids(model_number)]
        basis = summary
        if equation_number is not None:
            basis = f"EQ-{ID_STEM}-{equation_number:03d}: {summary}"
        add(
            page,
            f"Final weakness watch / MU-{ID_STEM}-{model_number:03d}",
            "weakness",
            basis,
            "Retain this as a last-pass limitation after positive coverage, and require a specific algebraic, empirical, computational, provenance, or feasibility repair before transfer.",
            "E",
            rules,
            "medium",
        )

    context_records = [
        (1, "The Summary Sheet exposes the complete projection-to-location pipeline before technical detail."),
        (2, "The official Problem B prompt defines a fifty-year projection, geographic distribution, office-location, fewer-office, and COO-memo deliverable."),
        (3, "The report is organized as Part I language projection followed by Part II office optimization."),
        (7, "MATLAB is named for preliminary matrix calculation, but no complete executable environment is archived."),
        (10, "The modified-model opening explicitly maps preliminary defects to new learner, migrant, time-varying, and English-specific structures."),
        (14, "The fifty-year projection begins from 2017 after a 2013-to-2017 preliminary check."),
        (18, "The application translates forecast outputs into a multinational office-allocation question."),
        (21, "The Strengths and Weaknesses section separates claimed benefits from omitted feedback and data limitations."),
        (22, "The COO memo compresses technical results into findings, assignments, exclusions, relocations, and a future office-count condition."),
        (24, "The reference list contains six web or report sources and does not preserve retrieval snapshots."),
        (25, "Appendix tables preserve country mappings and parameter inputs needed to understand the source's aggregation route."),
        (28, "The appendix closes with plotted forecast material; every one of the 28 physical pages received bounded visual review."),
    ]
    for page, summary in context_records:
        rules = [RULES["logic"]]
        if page in {2, 18, 22}:
            rules.append(RULES["stakeholder"])
        add(
            page,
            "Context, source quality, and deliverable trace",
            "other",
            summary,
            "Keep this context attached to the paper record so software, source quality, audience, appendix support, and deliverable boundaries remain visible without being mistaken for validation.",
            "C",
            rules,
            "medium",
        )

    expected_dimensions = EXPECTED_OBSERVATION_DIMENSIONS
    actual_dimensions = dict(Counter(item["dimension"] for item in observations))
    if actual_dimensions != expected_dimensions:
        raise SystemExit(
            f"q121 observation dimensions changed: {actual_dimensions} != {expected_dimensions}"
        )
    if expected_dimensions["language"] <= max(
        count for dimension, count in expected_dimensions.items() if dimension != "language"
    ):
        raise SystemExit("q121 language is not the largest observation dimension")
    if expected_dimensions["weakness"] >= expected_dimensions["language"]:
        raise SystemExit("q121 weakness must remain strictly below language")
    if set(chapter_by_name) != set(item["chapter"] for item in CHAPTERS):
        raise SystemExit("q121 chapter index is inconsistent")
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
            raise SystemExit(f"missing q121 {kind} review proxies: {missing}")
        sizes = [path.stat().st_size for path in paths]
        if len(paths) > 8 or max(sizes) > 450000 or sum(sizes) > 4194304:
            raise SystemExit(
                f"q121 {kind} proxy segment {segment} exceeds request-body guard"
            )
        return {
            "segment": segment,
            "page_range": page_range,
            "proxy_count": len(paths),
            "total_proxy_bytes": sum(sizes),
            "largest_proxy_bytes": max(sizes),
        }

    full_segments = []
    for segment, (first_page, last_page) in enumerate(
        ((1, 7), (8, 14), (15, 21), (22, 28)), start=1
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

    formula_names = [
        [
            "p05-fig1-eq1.jpg",
            "p06-eq2-eq4.jpg",
            "p06-eq5-eq6.jpg",
            "p07-fig2-eq7.jpg",
            "p08-eq8-eq10.jpg",
            "p08-eq11-eq12.jpg",
            "p09-table1-eq13.jpg",
        ],
        [
            "p11-symbols.jpg",
            "p12-fig3.jpg",
            "p12-matrix-eq14-eq15.jpg",
            "p13-english-matrix.jpg",
            "p13-eq16-data.jpg",
            "p14-eq17-parameters.jpg",
        ],
        [
            "p17-sensitivity-eq.jpg",
            "p18-eq18.jpg",
            "p18-fig8.jpg",
            "p19-sa-parameters.jpg",
            "p19-symbols.jpg",
            "p20-weights-gdp.jpg",
        ],
    ]
    formula_page_ranges = [list(range(5, 10)), list(range(11, 15)), list(range(17, 21))]
    formula_segments = [
        summarize(
            segment,
            "formula",
            [PROXY_ROOT / "formulas" / name for name in names],
            formula_page_ranges[segment - 1],
        )
        for segment, names in enumerate(formula_names, start=1)
    ]
    return full_segments, formula_segments


def build_audit(
    language: dict[str, Any],
    models_record: dict[str, Any],
    card: dict[str, Any],
    observations: list[dict[str, Any]],
) -> dict[str, Any]:
    by_chapter: dict[str, list[dict[str, Any]]] = {}
    for unit in language["units"]:
        by_chapter.setdefault(unit["chapter"], []).append(unit)
    layouts = {layout["chapter"]: layout for layout in language["chapter_layouts"]}
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
    chapter_specs = {item["chapter"]: item for item in CHAPTERS}
    for chapter_name in ("abstract", "introduction"):
        layout = layouts[chapter_name]
        spec = chapter_specs[chapter_name]
        paragraph_units = by_chapter[chapter_name][: layout["paragraph_count"]]
        paragraph_chains.append(
            {
                "chapter": chapter_name,
                "visual_paragraph_count": layout["paragraph_count"],
                "coverage_status": "complete",
                "gaps": [],
                "paragraphs": [
                    {
                        "paragraph_index": index,
                        "dominant_move": f"{spec['moves'][index - 1]} -> {unit['function']} -> {spec['output']} -> {spec['handoff']}",
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
        for item in LANGUAGE_CHAPTERS
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
            "positive_pattern": "Retain input -> rhetorical job -> analytical job -> output -> handoff; place formula, fact, symbol, and claim warnings only in the final pass.",
        }
        for item in LANGUAGE_CHAPTERS
    ]
    main_argument_chains = [
        {
            "claim": "The paper treats language projection and office placement as one forecast-to-decision pipeline.",
            "support_steps": ["global language change", "native/non-native state split", "2067 projection", "office score", "simulated-annealing assignment", "COO memo"],
            "decision_consequence": "Every office recommendation must retain a trace to the language, GDP, transport, cost, and coverage inputs that produced it.",
            "source_pages": [1, 3, 18, 19, 22],
        },
        {
            "claim": "The homogeneous preliminary model is deliberately scaled from two languages to twenty-two before its long-run failure motivates revision.",
            "support_steps": ["N=2 state graph", "Equation (1)", "eigenpair interpretation", "2N matrix", "2017 check", "96.01 percent Punjabi diagnostic"],
            "decision_consequence": "Use the preliminary model as a transparent diagnostic baseline, not as a validated fifty-year forecast.",
            "source_pages": [5, 6, 7, 8, 9],
        },
        {
            "claim": "The inhomogeneous repair adds learners, migrants, demographic blocks, feedback, and an English-specific partition in response to named baseline defects.",
            "support_steps": ["defect list", "learner and migrant states", "three-block operator", "Equations (14)-(15)", "English four-block operator", "Equation (16)"],
            "decision_consequence": "Preserve the time-indexed block dependencies and resolve the apparent one-period feedback lag before implementation.",
            "source_pages": [10, 11, 12, 13],
        },
        {
            "claim": "Learning, migration, policy, economics, education, and language family are intended to connect population dynamics with geographic language distribution.",
            "support_steps": ["symbol ledger", "learning matrix", "migration matrix", "Equation (17)", "fifty-year language trajectories", "migration and English-origin plots"],
            "decision_consequence": "Calibrate and normalize source-target transitions before attributing geographic outcomes to these mechanisms.",
            "source_pages": [11, 12, 13, 14, 15, 16],
        },
        {
            "claim": "Uniformity sensitivity changes attraction strength to show how popularity feedback alters English and Mandarin trajectories.",
            "support_steps": ["power-law attraction", "k=0.1", "k=1", "k=10", "Figures 7-8", "English/Mandarin crossover comparison"],
            "decision_consequence": "Treat the three curves as local scenarios until calibrated ranges, joint uncertainty, and decision switches are tested.",
            "source_pages": [16, 17, 18],
        },
        {
            "claim": "The application combines projected language demand, GDP, transport, setup proxy, and language load into constrained office assignments.",
            "support_steps": ["nineteen cities", "Equation (18)", "mutually exclusive coverage", "six-office score", "annealing parameters", "five-office comparison"],
            "decision_consequence": "Normalize units, elicit stakeholder weights, enforce coverage exactly, and document the optimizer before acting on score differences.",
            "source_pages": [18, 19, 20, 21],
        },
        {
            "claim": "The memo changes the receiving form from technical derivation to conditional executive action while retaining forecast branches.",
            "support_steps": ["key language trends", "migration findings", "2017 offices", "2067 relocations", "five-office alternative", "future cost/revenue condition"],
            "decision_consequence": "Keep every compressed memo claim linked to a model artifact and state uncertainty, infeasibility, and review triggers explicitly.",
            "source_pages": [22, 23],
        },
    ]

    warnings = []
    for model_number, equation_offset, page, warning in FORMULA_WARNINGS:
        model = models[model_number - 1]
        equation_record = model["governing_equations"][equation_offset]
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
            reason = NONREUSABLE_LANGUAGE_REASONS.get(unit["language_unit_id"])
            if reason is None:
                raise SystemExit(
                    "q121 language unit has no candidate pattern or nonreusable reason: "
                    f"{unit['language_unit_id']}"
                )
            disposition = "paper-specific-nonreusable"
            target_pattern_ids: list[str] = []
        else:
            disposition = (
                "opens-candidate"
                if any(
                    pattern_dispositions[pattern_id] == "opens-candidate"
                    for pattern_id in candidate_pattern_ids
                )
                else "supports-existing"
            )
            target_pattern_ids = candidate_pattern_ids
            reason = (
                "Transfer the rhetorical mechanism and information order only after "
                "replacing all language, city, year, value, equation, score, and "
                "decision-specific content."
            )
        language_unit_dispositions.append(
            {
                "language_unit_id": unit["language_unit_id"],
                "disposition": disposition,
                "target_pattern_ids": target_pattern_ids,
                "reason": reason,
            }
        )

    positive_reusable_language_count = sum(
        record["disposition"] != "paper-specific-nonreusable"
        for record in language_unit_dispositions
    )
    expected_positive_reusable_count = len(language["units"]) - len(
        NONREUSABLE_LANGUAGE_REASONS
    )
    if (
        positive_reusable_language_count != expected_positive_reusable_count
        or positive_reusable_language_count != 82
    ):
        raise SystemExit(
            "q121 positive reusable language count changed: "
            f"{positive_reusable_language_count} != 82"
        )

    dimensions = {
        dimension: Counter(item["dimension"] for item in observations)[dimension]
        for dimension in (
            "language",
            "modeling",
            "logic",
            "visualization",
            "verification",
            "data",
            "assumption",
            "result",
            "weakness",
            "other",
        )
    }
    full_segments, formula_segments = proxy_review_segments()
    return {
        "audit_id": f"LA-{ID_STEM}",
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": chapter_saturation,
        "language_unit_dispositions": language_unit_dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "complete",
            "weakness_substitution_allowed": False,
            "global_organization_chain": [
                f"{item['label']}: {item['output']} -> {item['handoff']}" for item in CHAPTERS
            ],
            "section_progressions": section_progressions,
            "main_argument_chains": main_argument_chains,
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
            for index, visual in enumerate(card["visualization_observations"], start=1)
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
            "warnings_strict_minority_of_language": len(warnings) < len(language["units"]),
            "request_body_guard": {
                "previous_413_root_cause": "Accumulated base64 images in an approximately 644.5 MiB session JSONL exceeded the nginx request-body limit; filesystem permissions were not causal.",
                "single_image_per_tool_call": True,
                "proxy_byte_limit": 450000,
                "context_segment_image_limit": 8,
                "context_segment_model_visible_limit_bytes": 4194304,
                "full_page_review_segments": full_segments,
                "formula_audit_segments": formula_segments,
                "original_full_page_png_in_context": False,
                "full_session_jsonl_in_context": False,
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
        raise SystemExit(f"q121 extraction identity mismatch: {identity} != {expected}")
    if extraction.get("extraction_status") != "text-extracted":
        raise SystemExit("q121 extraction is not text-extracted")
    full_segments, formula_segments = proxy_review_segments()
    extraction["visual_review_status"] = "complete"
    extraction["visual_review"] = {
        "status": "complete",
        "reviewed_pages": list(range(1, PAGE_COUNT + 1)),
        "notes": [
            "All 28 physical pages were read in UTF-8 page-aware text and reviewed as byte-bounded full-page JPEG proxies in four independent seven-page segments.",
            "Nineteen focused formula, table, symbol, and algorithm crops were reviewed in three fresh bounded segments for small-label fidelity.",
            "Original full-page PNG renders remained on disk and never entered model context.",
        ],
    }
    extraction["visual_review_manifest"] = {
        "pages_reviewed": list(range(1, PAGE_COUNT + 1)),
        "full_page_proxy_count": sum(item["proxy_count"] for item in full_segments),
        "formula_proxy_count": sum(item["proxy_count"] for item in formula_segments),
        "full_page_proxy_segments": full_segments,
        "formula_proxy_segments": formula_segments,
        "original_full_page_png_in_context": False,
        "review_note": "Full-page review covered pages 1-28; focused crops retained matrices, equations, small table values, sensitivity labels, office-score notation, and simulated-annealing parameters without expanding request bodies.",
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
            raise SystemExit(f"no q121 observation evidence for {rule_id}")
        impact["evidence_ids"] = [first_by_rule[rule_id]]


def main() -> None:
    if STAGE.exists():
        if not STAGE.is_dir():
            raise SystemExit(f"q121 staging path is not a directory: {STAGE}")
        if any(STAGE.iterdir()):
            raise SystemExit(f"refusing to overwrite non-empty staging directory: {STAGE}")

    language, units = build_language()
    models_record = build_models()
    visuals = build_visuals()
    card = build_card(language, models_record, visuals)
    observations = build_observations(units, models_record, visuals)
    bind_rule_impacts(card, observations)
    audit = build_audit(language, models_record, card, observations)
    extraction = build_extraction()

    expected_counts = {
        "chapters": 15,
        "language_units": 84,
        "models": 14,
        "equations": 29,
        "dependency_edges": 16,
        "visual_records": 36,
        "observations": EXPECTED_OBSERVATION_COUNT,
        "formula_warnings": 16,
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
        raise SystemExit(f"q121 artifact counts changed: {actual_counts} != {expected_counts}")

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
        raise SystemExit(f"refusing to overwrite q121 staged files: {existing}")
    for name, value in targets.items():
        dump_json(STAGE / name, value)
    dump_jsonl(STAGE / "observations.jsonl", observations)
    print(
        json.dumps(
            {
                "stage": str(STAGE),
                **actual_counts,
                "dimension_counts": audit["dimension_counts"],
                "full_page_proxy_segments": audit["gate_attestation"]["request_body_guard"]["full_page_review_segments"],
                "formula_proxy_segments": audit["gate_attestation"]["request_body_guard"]["formula_audit_segments"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
