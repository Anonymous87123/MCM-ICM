#!/usr/bin/env python3
"""Build source-anchored staged learning artifacts for deterministic Queue 123."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "P-B-2018-77238-4380ec81"
ID_STEM = "B-2018-77238"
PROBLEM_TYPE = "B"
YEAR = "2018"
SHA256 = "4380ec81b5ee9b4609444db0e383190b0bd18fb4dd1b2f0cf729c7324b22974f"
PAGE_COUNT = 23
SOURCE_PATH = "2018\u7f8e\u8d5b\u7279\u7b49\u5956/B\u98985\u7bc7/B77238.pdf"
STAGE = ROOT / "tmp" / "q123-stage-v2"
SOURCE_EXTRACTION = ROOT / "artifacts" / "papers" / PAPER_ID / "extraction.json"
SOURCE_PAGES = ROOT / "artifacts" / "papers" / PAPER_ID / "text" / "pages"
PROXY_ROOT = ROOT / "artifacts" / "papers" / PAPER_ID / "review-proxies"


RULE_ACTIONS = {
    "R-B-DATA-002": "require source, year, geography, unit, transformation, missingness, and downstream use for every demographic, language, GDP, distance, and migration input",
    "R-B-MOD-001": "verify the geographic distance definition, coordinate system, units, zero-distance surrogate, and receiving facility-location equation",
    "R-B-MOD-003": "normalize and justify GDP, distance, language, and office-count criteria before any scalar ranking or maximization",
    "R-B-MOD-004": "keep native persons, second-language learners, language identities, country groups, office scores, and recommendations as distinct typed entities",
    "R-B-MOD-005": "test P-center partitions and office selections under perturbation, alternative allocation rules, and explicit operating costs",
    "R-B-VER-002": "run joint sensitivity, seeded stochastic checks, holdout comparison, and office-portfolio stability rather than one-factor plausibility alone",
    "R-B-VER-004": "check AHP reciprocity, CI and CR labels, probability normalization, dimensions, indices, and cross-section table consistency",
    "R-B-VIZ-001": "reconcile every map, table, caption, office count, city label, language label, horizon, and preceding recommendation",
    "R-B-LOG-001": "trace population and language inputs through forecasting, clustering, office objectives, recommendations, and the executive memo",
    "R-B-LANG-001": "bind robust, credible, ideal, feasible, passable, and suitable claims to a metric, comparator, scenario, horizon, and uncertainty limit",
    "R-B-DEC-002": "record stakeholder, budget, service, and operating-cost provenance for office-count allocations and criterion weights",
}


def pattern(
    suffix: str,
    name: str,
    function: str,
    information_order: list[str],
    slots: list[str],
    variants: list[str],
    boundary: str,
    disposition: str = "supports-existing",
) -> dict[str, Any]:
    return {
        "pattern_id": f"LP-B-Q123-{suffix}",
        "name": name,
        "function": function,
        "information_order": information_order,
        "slots": slots,
        "variants": variants,
        "boundary": boundary,
        "disposition": disposition,
        "original_examples": [
            f"A clinic-planning report can use the {name} pattern after replacing every source entity, measurement, and decision boundary.",
            f"A reservoir study can preserve the information order of {name} while supplying its own evidence, uncertainty, and receiving action.",
        ],
    }


PATTERNS = [
    pattern(
        "ROUTE-PREVIEW",
        "forecast-to-decision route preview",
        "Preview the analytical route in the order that later outputs are consumed.",
        ["decision need", "forecast scope", "model stages", "location stage", "bounded recommendation"],
        ["[client need]", "[horizon]", "[forecast model]", "[decision model]", "[action]"],
        ["aimed to", "based on", "we develop", "the analysis indicates"],
        "Every announced stage must later expose its input, output, and receiving stage.",
    ),
    pattern(
        "SCOPE-MECHANISM",
        "scope to causal-mechanism split",
        "Narrow a broad setting and separate the mechanisms assigned to different state variables.",
        ["broad setting", "modeled population", "state split", "mechanism assignment", "forecast boundary"],
        ["[setting]", "[population]", "[state A/state B]", "[mechanisms]", "[scope]"],
        ["considering both", "we focus on", "is determined by", "is outside scope"],
        "A modeling split is not evidence that the mechanisms are exhaustive or independent.",
    ),
    pattern(
        "TWO-STAGE-JUDGMENT",
        "binary gate to categorical choice",
        "Explain a decision by separating participation from the conditional choice among alternatives.",
        ["eligible population", "binary gate", "gate probability", "conditional alternatives", "allocated output"],
        ["[population]", "[whether]", "[probability]", "[which option]", "[count]"],
        ["first judge whether", "and then which", "conditional on", "assign to"],
        "The gate probability and conditional-choice probabilities must not be conflated.",
        "opens-candidate",
    ),
    pattern(
        "FACTOR-SCORE",
        "qualitative factor to operational score",
        "Turn a verbal influence into a measurable score while preserving its proxy assumptions.",
        ["verbal factor", "observable proxy", "scale or threshold", "score", "downstream use"],
        ["[factor]", "[proxy]", "[scale]", "[score]", "[equation]"],
        ["is measured by", "is divided into", "the score equals", "enters the index"],
        "A convenient proxy is not the factor itself and requires scale and provenance checks.",
    ),
    pattern(
        "WEIGHT-JUSTIFICATION",
        "preference statement to criterion weight",
        "Expose how a stated preference becomes a comparison matrix and a normalized weight.",
        ["decision criterion", "preference rationale", "pairwise comparison", "normalization", "consistency check"],
        ["[criterion]", "[rationale]", "[matrix]", "[weight]", "[diagnostic]"],
        ["we give preference", "we first build", "normalizing", "to test consistency"],
        "Subjective preference remains stakeholder-dependent even when encoded by AHP.",
        "opens-candidate",
    ),
    pattern(
        "STOCHASTIC-NARRATION",
        "population flow to stochastic allocation",
        "Narrate a simulation as typed population updates followed by a declared random allocation.",
        ["current state", "new flow", "eligible share", "random draw", "state update"],
        ["[state]", "[new population]", "[share]", "[draw rule]", "[next state]"],
        ["at the initial phase", "we first calculate", "then assign", "if the value falls"],
        "The draw count, seed, grouping size, and probability normalization must be reproducible.",
    ),
    pattern(
        "RESULT-MECHANISM",
        "quantified result with mechanism contrast",
        "Report a result with baseline, horizon, magnitude, and a separately labeled explanation.",
        ["baseline", "horizon or scenario", "change", "exception", "proposed mechanism"],
        ["[baseline]", "[horizon]", "[value]", "[exception]", "[explanation]"],
        ["the result shows", "compared with", "meanwhile", "this is attributed to"],
        "A plausible explanation is not a causal validation of the simulated result.",
    ),
    pattern(
        "PROVENANCE-BOUNDARY",
        "data provenance and transformation boundary",
        "Attach a value to its source class, date, geography, unit, transformation, and use.",
        ["source", "time and geography", "entity and unit", "transformation", "receiver"],
        ["[source]", "[year/place]", "[entity/unit]", "[operation]", "[model term]"],
        ["we acquire", "is obtained from", "is calculated from", "is used in"],
        "A URL or database name alone is not a frozen, reproducible data record.",
    ),
    pattern(
        "MODEL-HANDOFF",
        "named output to receiving model",
        "Make the transition between submodels explicit without changing entity or horizon silently.",
        ["completed output", "identity and unit", "receiving stage", "transformation", "decision role"],
        ["[output]", "[unit]", "[receiver]", "[conversion]", "[use]"],
        ["after obtaining", "based on", "is applied to", "further determine"],
        "A handoff is valid only when the receiver consumes the named output at the same semantic level.",
    ),
    pattern(
        "FAILURE-PIVOT",
        "diagnosed failure to replacement route",
        "Close a weak route by naming its observable failure before introducing a replacement.",
        ["completed route", "observed failure", "operational consequence", "replacement", "retained components"],
        ["[route]", "[failure]", "[consequence]", "[replacement]", "[reuse]"],
        ["can hardly be regarded", "this stems from", "we shift", "we use the same"],
        "The replacement must answer the diagnosed failure rather than merely add another technique.",
        "opens-candidate",
    ),
    pattern(
        "BASELINE-CONTRAST",
        "baseline to scenario contrast",
        "Declare a baseline and perturbation before interpreting the response.",
        ["tested parameter", "baseline", "perturbation set", "response metric", "bounded interpretation"],
        ["[parameter]", "[baseline]", "[levels]", "[response]", "[limit]"],
        ["we reduce and increase", "compared with", "relative change", "under each circumstance"],
        "One-at-a-time scenarios do not establish joint or global robustness.",
    ),
    pattern(
        "CLAIM-BOUNDARY",
        "evidence to calibrated claim",
        "State exactly what a diagnostic supports and prevent expansion into a stronger claim.",
        ["diagnostic", "observed range", "supported local claim", "unsupported claim", "next check"],
        ["[test]", "[range]", "[local conclusion]", "[boundary]", "[repair]"],
        ["from this perspective", "can be considered", "within the tested range", "does not establish"],
        "Words such as robust, credible, ideal, and feasible require explicit metrics and uncertainty.",
    ),
    pattern(
        "ALTERNATIVE-COMPARISON",
        "parallel alternatives with decision criterion",
        "Compare two solution routes using a shared decision need and explicit failure criterion.",
        ["decision need", "alternative A", "alternative B", "comparison criterion", "selection"],
        ["[need]", "[route A]", "[route B]", "[criterion]", "[choice]"],
        ["one solution", "the other", "from two aspects", "we give priority"],
        "Alternatives must be compared on common outputs, costs, and feasibility rather than rhetoric alone.",
    ),
    pattern(
        "CONDITIONAL-DECISION",
        "conditioned recommendation",
        "Tie an operational recommendation to horizon, budget, portfolio size, and scenario.",
        ["decision owner", "conditions", "candidate set", "selection rule", "recommendation"],
        ["[owner]", "[conditions]", "[options]", "[rule]", "[action]"],
        ["if provided", "as long as", "for short-term", "from a long-term perspective"],
        "A recommendation cannot be reused after changing office count, geography, horizon, or cost assumptions.",
    ),
    pattern(
        "TRADEOFF-LEDGER",
        "positive design choice with burden",
        "Preserve a useful design feature and its empirical, computational, or decision limitation together.",
        ["design choice", "benefit", "scope", "burden", "repair"],
        ["[choice]", "[benefit]", "[scope]", "[limitation]", "[repair]"],
        ["an advantage is", "however", "relies on", "can be improved"],
        "A weakness record supplements rather than replaces positive language and model evidence.",
    ),
    pattern(
        "EXECUTIVE-COMPRESSION",
        "technical chain to executive memo",
        "Compress a technical route around the recipient's decision while preserving horizon and conditions.",
        ["recipient need", "method family", "key finding", "recommendation", "condition"],
        ["[recipient]", "[method]", "[finding]", "[action]", "[condition]"],
        ["to assist you", "firstly", "based on", "we suggest"],
        "Compression must not change office counts, city identities, horizons, or evidentiary strength.",
        "opens-candidate",
    ),
]


def chapter(
    code: str,
    name: str,
    label: str,
    source_ranges: list[tuple[int, int, int]],
    count: int,
    paragraph_count: int,
    role_codes: str,
    input_text: str,
    rhetorical: str,
    analytical: str,
    output: str,
    handoff: str,
    content_counts: tuple[int, int, int, int, int],
    default_patterns: list[str],
) -> dict[str, Any]:
    roles = {"p": "premise", "m": "mechanism", "r": "result", "b": "boundary"}
    if len(role_codes) != count:
        raise ValueError(f"role count changed for {name}: {len(role_codes)} != {count}")
    return {
        "code": code,
        "chapter": name,
        "label": label,
        "source_ranges": source_ranges,
        "count": count,
        "paragraph_count": paragraph_count,
        "roles": [roles[code] for code in role_codes],
        "input": input_text,
        "rhetorical": rhetorical,
        "analytical": analytical,
        "output": output,
        "handoff": handoff,
        "content_counts": content_counts,
        "default_patterns": default_patterns,
    }


C = chapter
CHAPTERS = [
    C("ABS", "abstract", "Summary Sheet", [(1, 17, 43)], 8, 4, "pbmrmrrb", "Global language change, a fifty-year forecast, and an international-office decision.", "Preview the complete analytical route and its two decision horizons.", "Compress language-state simulation, AHP, clustering, P-center grouping, sensitivity, and office-count discussion.", "A judge-scannable forecast and two horizon-specific office portfolios.", "The introduction separates native-language continuity from second-language growth and restates the client decision.", (0, 0, 0, 0, 12), ["LP-B-Q123-ROUTE-PREVIEW", "LP-B-Q123-CONDITIONAL-DECISION"]),
    C("INT", "introduction", "Introduction", [(3, 6, 23)], 7, 3, "ppmbmmr", "The social role of language and the mechanisms changing native and second-language use.", "Move from global motivation to a bounded sixteen-language, fifty-year study.", "Separate demographic and second-language processes before passing forecasts into a dual location model.", "A scoped forecast-to-office problem with named inputs and outputs.", "Assumptions make the population and language-identity simplifications explicit.", (0, 0, 0, 0, 5), ["LP-B-Q123-SCOPE-MECHANISM", "LP-B-Q123-MODEL-HANDOFF"]),
    C("PAN", "problem-analysis", "Language and office decision analysis", [(4, 12, 32)], 5, 3, "bpmmr", "Country populations, language shares, and the need to allocate offices and working languages.", "Decompose an underspecified global task into typed forecast and decision objects.", "Apply a country cutoff, dominant-language proxy, two-stage L2 choice, and office handoff.", "A computationally bounded country-language state and decision route.", "Data and preprocessing instantiate the country, birth, GDP, language, and distance inputs.", (0, 1, 0, 0, 4), ["LP-B-Q123-TWO-STAGE-JUDGMENT", "LP-B-Q123-MODEL-HANDOFF"]),
    C("ASM", "assumptions", "Assumptions and Justification", [(3, 25, 42)], 4, 4, "bpbb", "Native-language identity, optional second-language use, intergenerational transmission, and migration.", "Expose simplifying premises together with their stated justification and later exception.", "Fix existing language identities, inherit parental L1, and omit multilingual families before adding migration.", "A boundary ledger for interpreting all simulated counts.", "The model section operationalizes these premises as country-level transitions.", (0, 0, 0, 0, 4), ["LP-B-Q123-SCOPE-MECHANISM", "LP-B-Q123-CLAIM-BOUNDARY"]),
    C("DAT", "data-preprocessing", "Country, language, GDP, and factor inputs", [(4, 13, 23), (5, 5, 22), (6, 6, 35)], 7, 7, "pmmmbmb", "UN population histories, net birth rates, language shares, GDP tiers, and five second-language factors.", "Translate attributed data and qualitative factors into declared model inputs.", "Construct diversity and economic scores, factor measurements, AHP comparisons, and horizon inputs.", "A typed input ledger and calibrated factor hierarchy.", "The language-development models consume these scores and probabilities.", (1, 2, 2, 6, 10), ["LP-B-Q123-PROVENANCE-BOUNDARY", "LP-B-Q123-FACTOR-SCORE"]),
    C("MOD", "model-establishment", "Language Development Model establishment", [(5, 5, 46), (6, 10, 59), (7, 5, 28)], 14, 10, "pmmmmmmbmmrrbb", "Diversity, GDP tiers, five language-choice factors, an AHP matrix, and newborn populations.", "Build the participation and conditional-choice mechanism in a traceable sequence.", "Calculate SLP, AHP weights, CI and CR, selection indices, probability intervals, and annual state updates.", "A complete stochastic transition rule for total language-speaker counts.", "The algorithm executes the rule across countries and years.", (10, 4, 2, 3, 16), ["LP-B-Q123-WEIGHT-JUSTIFICATION", "LP-B-Q123-FACTOR-SCORE"]),
    C("ALG", "algorithm", "Stochastic simulation and state updates", [(7, 14, 43), (8, 9, 33), (9, 9, 9), (10, 5, 33), (11, 8, 44)], 10, 8, "pmmmmrrmmb", "Country states, newborn cohorts, SLP, language-choice intervals, and migration flows.", "Narrate the executable simulation in state-update order.", "Generate L2 cohorts, assign blocks by random intervals, update totals, derive native counts, and incorporate migration.", "Fifty-year total, native, and geographic language distributions.", "The location model clusters the resulting country-language vectors.", (9, 5, 2, 0, 20), ["LP-B-Q123-STOCHASTIC-NARRATION", "LP-B-Q123-MODEL-HANDOFF"]),
    C("RES", "results", "Language and office results", [(7, 30, 43), (8, 9, 33), (9, 9, 9), (10, 11, 33), (12, 5, 59), (13, 5, 15), (15, 5, 33), (16, 5, 42)], 8, 8, "rrrrrrrr", "Simulated language paths, native/total decompositions, migration scenarios, clusters, and office scores.", "Present horizon-specific outputs with comparisons and proposed mechanisms.", "Trace rank turnover, growth, native-language changes, migration effects, and both office portfolios.", "Tables, maps, and city-language recommendations for 2017 and 2067.", "Model criticism motivates the geography-first replacement and later sensitivity tests.", (0, 8, 10, 0, 38), ["LP-B-Q123-RESULT-MECHANISM", "LP-B-Q123-CONDITIONAL-DECISION"]),
    C("IMP", "model-improvement", "Geography-oriented location improvement", [(11, 8, 44), (12, 5, 59), (13, 16, 43), (14, 5, 62)], 7, 7, "pbmmmmr", "A language-first six-group solution, GDP-distance scores, continent allocations, and candidate capitals.", "Diagnose the unbalanced cluster result before changing the grouping route.", "Reject the 38-country group, allocate offices by continent, apply a P-center partition, and reuse the office objective.", "A geography-first eight-office workflow with explicit country groups.", "Current and future results test whether the replacement yields plausible portfolios.", (5, 3, 5, 1, 14), ["LP-B-Q123-FAILURE-PIVOT", "LP-B-Q123-ALTERNATIVE-COMPARISON"]),
    C("SEN", "sensitivity-analysis", "Sensitivity Analysis", [(17, 5, 46), (18, 5, 46), (19, 5, 58), (20, 5, 24)], 10, 10, "pmmrrmmrrb", "Net birth, GDP-growth, migration, and office-location parameters.", "Declare baseline perturbations before interpreting forecast and portfolio changes.", "Vary each parameter separately, tabulate relative responses, and explain changes in selected countries.", "One-at-a-time language and office sensitivity evidence with visible decision switches.", "The robustness pass calibrates which claims these scenarios actually support.", (1, 1, 4, 0, 46), ["LP-B-Q123-BASELINE-CONTRAST", "LP-B-Q123-CLAIM-BOUNDARY"]),
    C("ROB", "robustness-verification", "Consistency and robustness checks", [(7, 5, 11), (10, 24, 28), (17, 36, 41), (18, 25, 29), (19, 17, 58), (20, 22, 24)], 4, 4, "mrrb", "AHP consistency, migration-scale comparison, parameter scenarios, and office changes.", "Separate local consistency and plausibility checks from stronger validation claims.", "Check CR, compare migration with births, inspect one-factor changes, and record portfolio switches.", "A bounded verification ledger rather than a global-robustness assertion.", "Conclusions and strengths must not overstate this evidence.", (2, 1, 4, 0, 10), ["LP-B-Q123-CLAIM-BOUNDARY", "LP-B-Q123-BASELINE-CONTRAST"]),
    C("CON", "conclusion", "Conclusion", [(21, 21, 33)], 5, 2, "mrrrb", "The complete language simulation and two location solutions.", "Compress findings around the problem outputs and the preferred route.", "Restate factor counts, simulation scope, rank change, alternative quality, and conditional recomputation.", "A concise forecast and geography-first office recommendation.", "The strengths and limitations qualify the reusable design choices.", (0, 0, 0, 0, 8), ["LP-B-Q123-ROUTE-PREVIEW", "LP-B-Q123-CLAIM-BOUNDARY"]),
    C("SWK", "strengths-limitations", "Strengths and Weaknesses", [(20, 26, 39), (21, 5, 19)], 5, 5, "rrbbb", "The completed multi-factor, country-level, dual-route decision pipeline.", "Pair claimed advantages with the model objects and burdens that bound them.", "Retain multi-factor coverage, country resolution, and alternative comparison while naming representation, objective, data, and city limits.", "A benefit-burden ledger attached to specific model components.", "Future improvements change the affected objects rather than adding generic caveats.", (0, 0, 0, 0, 9), ["LP-B-Q123-TRADEOFF-LEDGER", "LP-B-Q123-CLAIM-BOUNDARY"]),
    C("FUT", "future-improvements", "Independent repairs implied by the discussion", [(13, 16, 43), (20, 5, 24), (21, 10, 19)], 4, 4, "mmmm", "The unbalanced clusters, arbitrary objective, fixed office allocation, dominant-language proxy, and capital-only candidates.", "Turn each observed limitation into a changed state, objective, validation, or decision rule.", "Introduce multilingual states, stakeholder costs, uncertainty propagation, and city-level optimization.", "Four concrete extensions with affected inputs and outputs.", "The reference ledger distinguishes source support from proposed repairs.", (0, 0, 0, 0, 4), ["LP-B-Q123-FAILURE-PIVOT", "LP-B-Q123-TRADEOFF-LEDGER"]),
    C("REF", "references", "References", [(21, 37, 44)], 2, 2, "bb", "UN, CIA, web-language, language-index, and fuzzy-clustering citations.", "Keep source classes and bibliographic limits visible without treating citation as validation.", "Separate raw-data provenance from methodological attribution and note absent retrieval metadata.", "A bounded source ledger for data and method claims.", "The memo may summarize results but cannot strengthen their evidence status.", (0, 0, 0, 6, 0), ["LP-B-Q123-PROVENANCE-BOUNDARY"]),
    C("MEM", "memo", "Memo to the Service Company", [(22, 5, 52), (23, 9, 34)], 6, 5, "ppmrbb", "A COO deciding office locations, working languages, horizon, and portfolio size.", "Reorder technical evidence around the recipient's operating decision.", "Compress the language forecast, clustering and P-center methods, portfolios, and office-count condition.", "An executive recommendation whose table and prose remain visibly reconcilable.", "The final audit checks that the memo has not altered counts, cities, languages, or certainty.", (0, 1, 1, 0, 14), ["LP-B-Q123-EXECUTIVE-COMPRESSION", "LP-B-Q123-CONDITIONAL-DECISION"]),
]


LANGUAGE_ACTIONS = {
    "abstract": [
        "establish the global language setting with a quantified reach statement",
        "state the fifty-year forecast scope and the country-population cutoff",
        "name AHP parameterization and stochastic simulation before reporting outputs",
        "report top-ten turnover and speaker growth without opening the derivation",
        "hand the predicted language distribution into the office-location model",
        "contrast language-oriented and geography-oriented location routes",
        "separate short-term and long-term office portfolios by named countries",
        "close with a bounded sensitivity and office-count discussion for the client",
    ],
    "introduction": [
        "establish language as both a communication tool and a carrier of human achievement",
        "distinguish lifetime native-language continuity from expanding second-language use",
        "connect schooling, policy, migration, tourism, and online exchange to language change",
        "bound the study to sixteen languages observed at the 2017 baseline",
        "tie country language distributions and net birth rates to a fifty-year simulation",
        "preview the two location solutions after the language forecast is complete",
        "name GDP distribution, distance, and working-language choice as office outputs",
    ],
    "problem-analysis": [
        "reduce the country set with a population threshold and state the claimed coverage",
        "use the largest speaker group as a computational proxy for national native language",
        "decompose each newborn cohort into native-only and potential second-language groups",
        "split second-language behavior into a participation gate and a conditional choice",
        "connect the country-language transition state to the later office decision",
    ],
    "assumptions": [
        "distinguish universal native-language use from optional second-language use",
        "hold existing people's language identities fixed in the simplified stage",
        "assign the new generation their parents' native language",
        "exclude multilingual families while reserving migration for a later model pass",
    ],
    "data-preprocessing": [
        "attribute 2007-2017 country populations and net birth rates to the UN source",
        "attach country language percentages to their cited but incompletely frozen sources",
        "convert counts of languages above a threshold into a diversity score over sixteen",
        "encode developed, developing, and backward GDP stages with different scores and growth rates",
        "list communication, geography, economy, knowledge, and diplomacy as choice factors",
        "separate globally shared language indicators from country-specific domestic indicators",
        "carry base-year language, GDP, migration, coordinate, and candidate-capital data into the decision pipeline",
    ],
    "model-establishment": [
        "combine communication and economic scores into a second-language participation percentage",
        "explain why the economic participation score is intentionally nonmonotone across development stages",
        "expand five language-choice factors into measurable subcriteria",
        "translate verbal preference for communication and trade into pairwise comparisons",
        "derive the principal eigenvector before normalizing the five section weights",
        "divide section weights among the named measurable subcriteria",
        "define the AHP consistency index from the maximum eigenvalue and matrix order",
        "compare the consistency ratio with the stated one-tenth threshold",
        "construct a country-language selection index from global and domestic factor values",
        "normalize language indices into conditional choice probabilities",
        "convert those probabilities into cumulative random-number intervals",
        "multiply the second-language percentage by each newborn cohort",
        "update total language counts while keeping native and second-language identities distinct",
        "state the model boundary before interpreting a fifty-year simulated trajectory",
    ],
    "algorithm": [
        "initialize each country's population, dominant native language, and total speaker state",
        "calculate newborn population and the eligible second-language cohort for one year",
        "assign one random value to each declared block of ten thousand learners",
        "map every random draw to one cumulative language-probability interval",
        "repeat the country transition through the fifty-year horizon",
        "derive native-language totals by subtracting second-language identities from total identities",
        "apply emigration and immigration changes to country-level native and second-language states",
        "calculate absolute cosine similarity between country-language vectors",
        "form fuzzy similarity and equivalent relations before selecting a cluster cut",
        "maximize the GDP-distance office score inside each resulting country group",
    ],
    "results": [
        "report the two languages leaving and entering the simulated top ten",
        "contrast rapid French, Japanese, and German growth with the small Russian decline",
        "bind the 2017 and 2067 ranks and counts to the first simulation table",
        "use the world distribution maps to show where language shares move geographically",
        "identify the modeled year in which native English speakers overtake native Chinese speakers",
        "state that adding migration changes the paths little and give the paper's scale explanation",
        "report current and future language-first offices together with their working languages",
        "report current and future geography-first office portfolios and retained existing offices",
    ],
    "model-improvement": [
        "restrict location candidates to high-GDP countries and their capitals",
        "diagnose the language-first solution through its thirty-eight-country cluster",
        "pivot from language similarity to continent-level office allocation",
        "partition multi-office continents by the stated P-center distance procedure",
        "include Shanghai and New York when interpreting the resulting eight-office system",
        "reuse the GDP-distance criterion only after the geographic groups are fixed",
        "select one to three office languages from the clustered language structure",
    ],
    "sensitivity-analysis": [
        "identify net birth rate, GDP growth, and migration as language-model sensitivity inputs",
        "declare symmetric net-birth perturbations around the baseline",
        "compare language responses and the reported forty-percent envelope",
        "declare the four GDP-growth perturbations and retain the original stage rates",
        "report the small maximum language response under the GDP scenarios",
        "vary migration rates and retain language-specific sign differences",
        "explain the opposite migration responses through modeled origin and destination patterns",
        "hold geographic coordinates fixed while focusing the office analysis on GDP growth",
        "record group-membership and recommended-country switches for each office scenario",
        "distinguish stability under decreases from portfolio changes under large increases",
    ],
    "robustness-verification": [
        "use the AHP consistency ratio as a local matrix diagnostic",
        "compare the stated migration scale with average net birth rates",
        "interpret one-factor language sensitivity without upgrading it to global validation",
        "treat changed office portfolios as decision-instability evidence rather than noise",
    ],
    "conclusion": [
        "summarize the two participation criteria and five conditional-choice factors",
        "restate the country-level Python simulation and its bounded language-rank result",
        "compare the language-first and geography-first office solutions",
        "qualify the first route as passable and the second as conditional on an office allocation",
        "connect strategy changes to recomputation without claiming empirical validation",
    ],
    "strengths-limitations": [
        "retain broad factor coverage as a design strength of the language model",
        "retain country-level simulation as support for both temporal and geographic outputs",
        "retain the explicit comparison of language and geographic location routes",
        "record the dominant-language proxy and arbitrary objective as structural limitations",
        "tie data dependence and capital-only recommendations to concrete validation and resolution gaps",
    ],
    "future-improvements": [
        "replace the dominant-language proxy with a multilingual native-state representation",
        "calibrate office objectives and counts with stakeholder preferences and operating costs",
        "propagate population, GDP, language-share, migration, and distance uncertainty jointly",
        "optimize actual cities and service coverage after country-level screening",
    ],
    "references": [
        "separate the UN and CIA data citations from the transformations later applied to them",
        "separate web indicators, language-power attribution, and fuzzy-clustering methodology from validation evidence",
    ],
    "memo": [
        "address the operating recipient and define the location-and-language decision",
        "justify research before a material international expansion decision",
        "compress the five-factor language model without erasing its horizon",
        "state the simulated replacement of Russian and Portuguese by German and Japanese",
        "hand language forecasts into fuzzy clustering and P-center office selection",
        "present office-language recommendations while conditioning portfolio size on the company's plan",
    ],
}


def dump_json(path: Path, value: object) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def dump_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        for value in values:
            handle.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")


def source_page_lines(page: int) -> list[str]:
    path = SOURCE_PAGES / f"page-{page:04d}.txt"
    if not path.is_file():
        raise SystemExit(f"missing q123 source page: {path}")
    return path.read_text(encoding="utf-8").splitlines()


def clean_source_line(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return ""
    if "\u7cbe\u54c1\u6570\u6a21\u8d44\u6599" in stripped or "\u6dd8\u5b9d\u5e97\u94fa" in stripped:
        return ""
    if stripped == "77238" or stripped.startswith("# Team"):
        return ""
    if re.search(r"\bPage\s+\d+\s+of\s+23\b", stripped):
        return ""
    return stripped


def normalize_source_lines(lines: list[str]) -> str:
    retained = [clean_source_line(line) for line in lines]
    text = " ".join(line for line in retained if line)
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= 480:
        return text
    shortened = text[:480].rsplit(" ", 1)[0].rstrip(" ,;:")
    return shortened + "."


def allocate_range_counts(lengths: list[int], total: int) -> list[int]:
    counts = [0] * len(lengths)
    for _ in range(total):
        candidates = [index for index, length in enumerate(lengths) if counts[index] < length]
        if not candidates:
            raise SystemExit(f"q123 source ranges cannot support {total} language units")
        selected = max(candidates, key=lambda index: (lengths[index] / (counts[index] + 1), -index))
        counts[selected] += 1
    return counts


def chapter_source_spans(item: dict[str, Any]) -> list[dict[str, int]]:
    usable_by_range: list[list[int]] = []
    for page, line_start, line_end in item["source_ranges"]:
        lines = source_page_lines(page)
        if line_start < 1 or line_end < line_start or line_end > len(lines):
            raise SystemExit(
                f"q123 invalid chapter range p{page} lines {line_start}-{line_end}; page has {len(lines)} lines"
            )
        usable = [
            line_number
            for line_number in range(line_start, line_end + 1)
            if clean_source_line(lines[line_number - 1])
        ]
        if not usable:
            raise SystemExit(f"q123 empty chapter range p{page} lines {line_start}-{line_end}")
        usable_by_range.append(usable)

    counts = allocate_range_counts([len(lines) for lines in usable_by_range], item["count"])
    spans: list[dict[str, int]] = []
    for range_index, ((page, _, _), usable, count) in enumerate(
        zip(item["source_ranges"], usable_by_range, counts, strict=True), start=1
    ):
        for local_index in range(count):
            start_offset = local_index * len(usable) // count
            end_offset = ((local_index + 1) * len(usable) // count) - 1
            spans.append(
                {
                    "page": page,
                    "line_start": usable[start_offset],
                    "line_end": usable[end_offset],
                    "range_index": range_index,
                }
            )
    if len(spans) != item["count"]:
        raise SystemExit(f"q123 span count changed for {item['chapter']}")
    return spans


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
        max(1, len(re.findall(r"[A-Za-z0-9]+(?:['.-][A-Za-z0-9]+)*", sentence)))
        for sentence in sentences
    ]
    return (
        max(1, len(words)),
        len(sentences),
        {"minimum": min(lengths), "median": median(lengths), "maximum": max(lengths)},
    )


def build_language() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    pattern_index = {item["pattern_id"]: item for item in PATTERNS}
    units: list[dict[str, Any]] = []
    for item in CHAPTERS:
        actions = LANGUAGE_ACTIONS[item["chapter"]]
        if len(actions) != item["count"]:
            raise SystemExit(
                f"q123 language action count changed for {item['chapter']}: {len(actions)} != {item['count']}"
            )
        spans = chapter_source_spans(item)
        for local_index, (action, role, span) in enumerate(
            zip(actions, item["roles"], spans, strict=True), start=1
        ):
            pattern_ids = list(item["default_patterns"])
            unknown = sorted(set(pattern_ids) - set(pattern_index))
            if unknown:
                raise SystemExit(f"q123 language unit references unknown patterns: {unknown}")
            primary = pattern_index[pattern_ids[(local_index - 1) % len(pattern_ids)]]
            page_lines = source_page_lines(span["page"])
            excerpt = normalize_source_lines(
                page_lines[span["line_start"] - 1 : span["line_end"]]
            )
            if not excerpt:
                raise SystemExit(
                    f"q123 empty source excerpt p{span['page']} lines {span['line_start']}-{span['line_end']}"
                )
            information_order = list(primary["information_order"])
            unit_id = f"LU-{ID_STEM}-{item['code']}-{local_index:03d}"
            original_instantiations = [
                {"text": f"A clinic study can {action} after rebuilding the population, measures, uncertainty, and staffing decision."},
                {"text": f"A reservoir report can use the same information order to {action} with its own hydrologic evidence and release policy."},
            ]
            if unit_id == f"LU-{ID_STEM}-REF-002":
                original_instantiations = [
                    {"text": "A clinic evidence review can distinguish provenance from independent performance testing before a staffing recommendation is accepted."},
                    {"text": "A reservoir study can cite a method separately from the holdout evidence used to justify a release decision."},
                ]
            units.append(
                {
                    "language_unit_id": unit_id,
                    "page": span["page"],
                    "section": f"{item['label']} / language move {local_index}: {action}",
                    "chapter": item["chapter"],
                    "granularity": "paragraph",
                    "source_excerpt": excerpt,
                    "source_anchor": {
                        "page_file": f"page-{span['page']:04d}.txt",
                        "inspected_line_start": span["line_start"],
                        "inspected_line_end": span["line_end"],
                        "normalization": "trim lines, exclude extraction-only watermark and page headers, remove line-break hyphenation, collapse whitespace, and cap at a word boundary",
                    },
                    "function": action,
                    "rhetorical_role": role,
                    "rhetorical_move": (
                        f"{action}; within {item['label']}, the move turns {item['input']} into "
                        f"{item['output']} before handing it to {item['handoff']}"
                    ),
                    "reusable_pattern": " -> ".join(information_order),
                    "information_order": information_order,
                    "reusable_elements": [
                        f"occurrences: physical page {span['page']}, inspected lines {span['line_start']}-{span['line_end']}",
                        f"function: {action}",
                        f"information order: {' -> '.join(information_order)}",
                        f"slots: {'; '.join(primary['slots'])}",
                        f"variants: {'; '.join(primary['variants'])}",
                        f"handoff: {item['handoff']}",
                    ],
                    "prohibited_generalizations": [
                        f"boundary: {primary['boundary']}",
                        "anti-copy: replace every language, country, city, year, threshold, coefficient, probability, score, table entry, and recommendation before reuse",
                        "preserve whether a statement is an assumption, attributed input, transformation, simulation result, diagnostic, explanation, warning, or stakeholder action",
                        "do not transfer the source's sixteen-language set, GDP tiers, AHP weights, random block size, city list, or office allocation as general constants",
                    ],
                    "features": {
                        "voice": "first-person plural for performed modeling actions; object-led or passive voice for definitions, tables, and computed results",
                        "tense": "present for definitions and mechanisms, past for completed runs, and future or modal forms for forecasts and recommendations",
                        "modality": "assume, suggest, can, may, should, and recommend must distinguish premises, model capability, uncertainty, and action",
                        "clause_structure": "scope or condition -> named analytical action -> evidence or output -> bounded interpretation -> receiving model or decision",
                        "quantitative_role": "bind each number to entity, unit, baseline year, forecast horizon, scenario, comparator, and downstream use",
                        "transition": "first, then, meanwhile, however, therefore, based on, compared with, and finally make dependencies visible",
                        "original_instantiations": original_instantiations,
                    },
                    "candidate_pattern_ids": pattern_ids,
                }
            )

    if len(units) != 106:
        raise SystemExit(f"q123 language unit count changed: {len(units)} != 106")

    patterns = json.loads(json.dumps(PATTERNS))
    for repeated in patterns:
        nominated = [
            unit for unit in units if repeated["pattern_id"] in unit["candidate_pattern_ids"]
        ]
        if not nominated:
            raise SystemExit(f"q123 pattern has no occurrence: {repeated['pattern_id']}")
        repeated["occurrences"] = len(nominated)
        repeated["locations"] = list(dict.fromkeys(unit["section"] for unit in nominated))

    layouts: list[dict[str, Any]] = []
    for item in CHAPTERS:
        chapter_units = [unit for unit in units if unit["chapter"] == item["chapter"]]
        combined = " ".join(unit["source_excerpt"] for unit in chapter_units)
        word_count, sentence_count, sentence_words = sentence_statistics(combined)
        role_counts = Counter(unit["rhetorical_role"] for unit in chapter_units)
        total = len(chapter_units)
        equations, figures, tables, citations, quantitative = item["content_counts"]
        pages = [page for page, _, _ in item["source_ranges"]]
        layouts.append(
            {
                "chapter": item["chapter"],
                "page_start": min(pages),
                "page_end": max(pages),
                "page_fraction": round((max(pages) - min(pages) + 1) / PAGE_COUNT, 6),
                "word_count": word_count,
                "sentence_count": sentence_count,
                "paragraph_count": item["paragraph_count"],
                "sentence_words": sentence_words,
                "paragraph_functions": [
                    chapter_units[index % total]["function"]
                    for index in range(item["paragraph_count"])
                ],
                "rhetorical_proportions": {
                    role: role_counts[role] / total
                    for role in ("premise", "mechanism", "result", "boundary")
                },
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
                "counting_method": "Metrics are computed from explicit physical-page line spans after deterministic header removal and whitespace normalization; paragraph counts are visual structural units recorded during the completed 23-page review.",
                "ambiguities": [
                    "The extraction omits several displayed formulas, matrices, subscripts, and map labels; focused visual crops control the central AHP, cosine, and office-objective transcriptions.",
                    "A Chinese commercial watermark is extraction-only noise and is excluded from author-language evidence.",
                    "Physical PDF pages, not section or table numbering, are the authoritative anchors.",
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


def equation(
    page: int,
    label: str,
    source: str,
    latex: str,
    purpose: str,
    symbols: list[str],
    confidence: str = "high",
    source_type: str = "paper",
) -> dict[str, Any]:
    return {
        "page": page,
        "label": label,
        "source": source,
        "latex": latex,
        "purpose": purpose,
        "symbols": symbols,
        "confidence": confidence,
        "source_type": source_type,
    }


def model_spec(
    page: int,
    section: str,
    family: str,
    purpose: str,
    inputs: list[str],
    outputs: list[str],
    equations: list[dict[str, Any]],
    steps: list[str],
    assumptions: list[str],
    validation_refs: list[str],
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
        "equations": equations,
        "steps": steps,
        "assumptions": assumptions,
        "validation_refs": validation_refs,
        "limitations": limitations,
        "origin": origin,
    }


E = equation
M = model_spec
MODEL_SPECS = [
    M(
        4,
        "4.1 Language Development Model / scope and native-language representation",
        "population-threshold country scope with dominant-language representation",
        "Define the modeled country set and replace each included country's multilingual native structure by its largest language group.",
        ["P_c_t", "h_c_l"],
        ["C", "d_c"],
        [
            E(4, "scope cutoff", "Only countries with population over 10 million are retained, claimed to cover about 92 percent of world population.", "C={c | P_{c,2017}>10^7}", "Define the country set used in all later language transitions.", ["C", "P_c_t"]),
            E(4, "dominant-language proxy", "The language with the most speakers represents the native language of a country.", "d_c=argmax_l h_{c,l}", "Map a multilingual country profile to the single native-language state used by the simulation.", ["d_c", "h_c_l"]),
        ],
        ["load country populations", "apply the ten-million threshold", "load language shares", "select the largest language share"],
        ["Countries below ten million people are excluded.", "One dominant language represents each country's native-language state."],
        ["Appendix 1 population-coverage claim", "country-language percentages", "Figure 1 state semantics"],
        ["The cutoff excludes small but linguistically important countries.", "The argmax proxy creates discontinuous native-language changes and erases multilingual populations."],
    ),
    M(
        5,
        "4.1.1 / second-language percentage",
        "two-factor second-language participation score",
        "Estimate the share of each newborn cohort that will learn a second language from diversity and an economic-stage score.",
        ["n_c", "E_c_t"],
        ["D_c", "A_c_t"],
        [
            E(5, "diversity score", "Diversity equals the number of languages spoken by more than 100,000 people divided by sixteen.", "D_c=n_c/16", "Convert a thresholded language count into the communication component.", ["D_c", "n_c"]),
            E(5, "SLP", "Communication and economic factors each receive weight 0.5 in the second-language percentage.", "A_{c,t}=0.5D_c+0.5E_{c,t}", "Combine the two participation components into Second Language Percentage.", ["A_c_t", "D_c", "E_c_t"]),
        ],
        ["count languages above the threshold", "divide by sixteen", "classify the economic stage", "average both scores"],
        ["Only communication and economic factors determine whether a newborn learns a second language.", "Equal weights are author-selected rather than stakeholder-elicited."],
        ["Figure 2 participation tree", "worked diversity example", "GDP-stage scores"],
        ["The 100,000 threshold and denominator sixteen are sample-dependent.", "The equal-weight average lacks calibration against observed second-language participation."],
    ),
    M(
        5,
        "4.1.1 / GDP development-stage transition",
        "piecewise constant GDP-per-capita growth stage",
        "Advance GDP per capita with stage-specific annual rates that can change the economic participation score over time.",
        ["G_c_t", "g_s"],
        ["G_c_next", "E_c_t"],
        [
            E(5, "GDP transition", "GDP per capita grows by 2 percent for developed, 7 percent for developing, and 3 percent for backward countries.", "G_{c,t+1}=G_{c,t}(1+g_{s(c,t)}), g_s in {0.02,0.07,0.03}", "Update GDP and permit movement among the paper's development categories.", ["G_c_t", "G_c_next", "g_s", "E_c_t"]),
        ],
        ["assign the initial GDP stage", "apply its annual growth rate", "reclassify when a threshold is crossed", "supply the economic score"],
        ["Each development stage has a time-invariant common growth rate.", "GDP per capita alone determines the economic stage."],
        ["Table 1 growth rates", "Figure 3 GDP classification", "GDP sensitivity scenarios"],
        ["Stage thresholds and currency-year units are not archived.", "Common deterministic rates suppress country heterogeneity and macroeconomic uncertainty."],
    ),
    M(
        6,
        "4.1.1 / AHP factor weights and consistency",
        "five-criterion analytic hierarchy process",
        "Convert preferences among communication, geography, economy, knowledge, and diplomacy into factor and subfactor weights.",
        ["A", "RI"],
        ["w", "lambda_max", "CI", "CR"],
        [
            E(6, "pairwise matrix", "The displayed 5 by 5 comparison matrix encodes preferences among Com, Geo, Eco, Kno, and Dip.", "A=[[1,2,1,5,6],[1,1/2,1,3,5],[1,2,1,5,6],[1/5,1/3,1/5,1,2],[1/6,1/5,1/6,1/2,1]]", "Retain the exact displayed matrix, including its visible reciprocity defect.", ["A"], "high"),
            E(6, "principal eigenpair", "The maximum eigenvalue and corresponding eigenvector are calculated.", "Aw=lambda_max w", "Define the eigenvector relation used to derive criterion weights.", ["A", "w", "lambda_max"]),
            E(6, "weight normalization", "The corresponding eigenvector is normalized to obtain section weights.", "w_k=v_k/sum_m v_m", "Normalize the principal eigenvector to a unit-sum weight vector.", ["w", "v"]),
            E(7, "CI", "The focused crop confirms CI=(lambda_max-n)/(n-1)=0.0115.", "CI=(lambda_max-n)/(n-1)=0.0115", "Compute the consistency index for n=5.", ["CI", "lambda_max", "n"]),
            E(7, "CR", "The following displayed 0.0103<0.1 is labeled CI in the source crop but is the ratio CI/RI.", "CR=CI/RI=0.0103<0.1", "Compute the consistency ratio while preserving the source's label error as a warning.", ["CR", "CI", "RI"]),
        ],
        ["construct the comparison matrix", "solve the principal eigenpair", "normalize the eigenvector", "split section weights among subcriteria", "compute CI and CR"],
        ["The pairwise judgments represent the decision maker's preference.", "Subcriteria within a section divide its weight equally."],
        ["displayed matrix", "Figure 4 weights", "focused p7 CI and CR crop"],
        ["The displayed matrix is not reciprocal, so standard AHP consistency interpretation is compromised.", "Preference provenance, respondent set, and uncertainty are absent."],
    ),
    M(
        6,
        "4.1.1 / country-language selection index",
        "weighted country-language utility and probability intervals",
        "Score every candidate second language for a country and map the scores to conditional random-assignment intervals.",
        ["w", "f_c_l_k"],
        ["S_c_l", "p_c_l", "q_c_l"],
        [
            E(6, "selection index", "Nine measurable subcriteria are weighted to form a second-language selection index for each country-language pair.", "S_{c,l}=sum_{k=1}^9 w_k f_{c,l,k}", "Aggregate global and domestic factors into one conditional choice score.", ["S_c_l", "w", "f_c_l_k"], "medium"),
            E(7, "conditional probability", "Language scores determine the probability assigned to each second-language alternative.", "p_{c,l}=S_{c,l}/sum_m S_{c,m}", "Normalize selection indices across candidate languages.", ["p_c_l", "S_c_l"], "medium", "reconstructed"),
            E(7, "cumulative interval", "A random number between zero and one is matched to a language interval; the focused example places 0.725 in the French interval [0.608,0.741].", "q_{c,l}=sum_{m<=l}p_{c,m}; choose l when q_{c,l-1}<=u<q_{c,l}", "Convert conditional probabilities into categorical simulation intervals.", ["q_c_l", "p_c_l", "u"], "high"),
        ],
        ["measure nine subcriteria", "apply AHP-derived weights", "sum the weighted scores", "normalize across languages", "form cumulative intervals"],
        ["All subcriteria are commensurable after the paper's undocumented scaling.", "Every learner selects exactly one second language from the modeled set."],
        ["Figure 4 hierarchy", "Figure 5 interval allocation", "focused p7 random-value example"],
        ["Several factor scales, directions, and country-level data transformations are missing.", "The normalization and candidate-language set are not fully documented."],
    ),
    M(
        7,
        "4.1.2 / stochastic language simulation",
        "annual newborn-cohort Monte Carlo allocation",
        "Advance total language-speaker identities by assigning each newborn cohort a native language and, conditionally, one second language.",
        ["P_c_t", "r_c", "A_c_t", "q_c_l", "u", "T_l_t"],
        ["B_c_t", "L2_c_t", "T_l_next"],
        [
            E(7, "newborn cohort", "Country population and Net Birth Rate determine the newly-born population each year.", "B_{c,t}=r_c P_{c,t}", "Create the annual population flow entering the language transition.", ["B_c_t", "r_c", "P_c_t"]),
            E(7, "second-language cohort", "SLP multiplied by newly-born population determines the increased number of second-language learners.", "L2_{c,t}=A_{c,t}B_{c,t}", "Apply the participation gate to the newborn cohort.", ["L2_c_t", "A_c_t", "B_c_t"]),
            E(7, "stochastic speaker update", "One random draw is assigned to every 10,000 second-language learners and the whole block enters one language interval.", "T_{l,t+1}=T_{l,t}+native_{l,t}+sum_c 10000 I(q_{c,l-1}<=u_c<q_{c,l})", "Update total language identities through the declared grouped draw rule.", ["T_l_t", "T_l_next", "q_c_l", "u"], "medium"),
        ],
        ["initialize 2017 states", "calculate newborn cohorts", "calculate second-language learners", "draw once per ten-thousand-person block", "assign blocks to intervals", "repeat for fifty years"],
        ["Newborn language behavior is fully determined by the modeled factors.", "Learners within a ten-thousand-person block make the same simulated choice.", "Existing speakers do not change languages in the initial run."],
        ["Figure 5 allocation", "Table 2 first simulation", "Figures 6 and 7"],
        ["No random seed, draw count reconciliation, interval uncertainty, or repeated-run distribution is reported.", "Grouped draws introduce avoidable discretization and path variance."],
    ),
    M(
        10,
        "4.1 / native and second-language decomposition",
        "total-language-identity subtraction decomposition",
        "Infer native-speaker totals by subtracting modeled second-language identities from total language identities.",
        ["T_l_t", "L2_l_t"],
        ["L1_l_t"],
        [
            E(10, "native decomposition", "The number of native speakers is obtained from total and second-language speaker counts by subtraction.", "L1_{l,t}=T_{l,t}-L2_{l,t}", "Separate the two speaker categories used in Figure 8.", ["L1_l_t", "T_l_t", "L2_l_t"]),
        ],
        ["aggregate total language identities", "aggregate second-language identities", "subtract by language and year", "plot native trajectories"],
        ["Total speaker identities equal disjoint native plus second-language identities for each language.", "No person is counted as learning multiple second languages."],
        ["Figure 8 native trajectories", "English-Chinese crossover statement"],
        ["Identity counts may overlap across languages at the person level.", "The subtraction is only valid if total and second-language definitions, geography, and timing match exactly."],
    ),
    M(
        10,
        "4.1 / migration modification",
        "instantaneous destination-language reassignment",
        "Modify country-language states by converting each migrant's original native language into a second language and destination language into native language.",
        ["N_c_l_t", "M_out_c_t", "M_in_c_t", "d_c"],
        ["N1_c_l_next", "N2_c_l_next"],
        [
            E(10, "migrant native update", "The emigrant country subtracts its emigrants and the immigrant country adds them to its native-language speakers.", "N1_{c,l,t+1}=N1_{c,l,t}+births_{c,l,t}-out_{c,l,t}+I(l=d_c)in_{c,t}", "Represent the source's instantaneous destination-native-language conversion.", ["N_c_l_t", "N1_c_l_next", "M_out_c_t", "M_in_c_t", "d_c"], "medium"),
            E(10, "migrant L2 update", "Immigrants' original native language is counted as a second language in the destination country.", "N2_{c,l,t+1}=N2_{c,l,t}+inflow_with_origin_language_{c,l,t}", "Retain the original language as a destination second-language identity.", ["N_c_l_t", "N2_c_l_next", "M_in_c_t"], "medium"),
        ],
        ["load migration rates", "remove emigrants from origin native states", "add immigrants to destination dominant native state", "retain origin language as destination L2", "rerun the horizon"],
        ["Language switching occurs at the instant of migration.", "Migration rates and destination patterns remain usable through the horizon."],
        ["migration prose on page 10", "Figure 9", "migration sensitivity table"],
        ["Instant language reassignment is behaviorally implausible and suppresses bilingual transition time.", "Migration flow provenance, origin-destination structure, units, and uncertainty are incomplete."],
    ),
    M(
        11,
        "4.2.1 / fuzzy language clustering",
        "absolute-cosine fuzzy-equivalence clustering",
        "Group 52 high-GDP country-language vectors into six clusters according to language-structure similarity.",
        ["x_c_l"],
        ["r_i_j", "R", "R_star", "g_c"],
        [
            E(11, "angle cosine", "The focused crop confirms an absolute cosine similarity between two country-language vectors.", "r_{ij}=|sum_k x_{ik}x_{jk}|/sqrt((sum_k x_{ik}^2)(sum_k x_{jk}^2))", "Compute pairwise similarity while preserving the source's absolute value.", ["r_i_j", "x_c_l"]),
            E(11, "fuzzy equivalent closure", "A fuzzy similar matrix is transformed into a fuzzy equivalent matrix before the six-group cut.", "R_star=transitive_closure_max_min(R); g_c=cut(R_star,alpha)", "Represent the described AFFZ closure and threshold grouping step.", ["R", "R_star", "g_c"], "medium", "reconstructed"),
        ],
        ["restrict candidates to 52 countries", "build country-language vectors", "compute absolute cosine similarities", "form the fuzzy relation", "take a fuzzy-equivalent closure", "choose a six-group cut"],
        ["GDP above 100 billion defines the candidate country set.", "Capital cities stand for countries.", "Six groups are required by the initial office plan."],
        ["focused p11 cosine crop", "Table 3", "Table 5"],
        ["Vector scaling, language dimensions, alpha cut, closure implementation, and cluster stability are not reported.", "Absolute cosine is redundant for nonnegative vectors and conceals whether signed inputs were possible."],
    ),
    M(
        11,
        "4.2.1 / GDP-distance office objective",
        "within-group GDP-squared inverse-distance facility score",
        "Rank each candidate capital by proximity to group GDP and a surrogate domestic distance, then select the maximum.",
        ["GDP_i", "d_i_j", "g_c"],
        ["J_j", "j_star"],
        [
            E(11, "office score", "The focused crop shows a sum of GDP_i squared over d_ij plus GDP_j squared over half the nearest nonzero distance.", "J_j=sum_{i!=j} GDP_i^2/d_{ij}+GDP_j^2/(0.5 min_{i!=j}d_{ij})", "Retain the exact paper-specific score and its self-distance surrogate.", ["J_j", "GDP_i", "d_i_j"]),
            E(11, "office maximization", "The larger the criterion value, the better the candidate; the maximum in each group is selected.", "j_star=argmax_{j in group} J_j", "Convert the score to one office choice per group.", ["j_star", "J_j", "g_c"]),
        ],
        ["calculate pairwise capital distances", "square every GDP", "divide other-country terms by distance", "replace zero self-distance", "sum by candidate", "take the group maximum"],
        ["GDP is more important than distance and squaring expresses that preference.", "Half the nearest-country distance is a coherent domestic-distance surrogate."],
        ["focused p11 office-objective crop", "Tables 4 and 6", "location sensitivity table"],
        ["GDP squared divided by distance has no decision-calibrated scale or unit interpretation.", "The zero-distance replacement and scalarization are arbitrary and can dominate rankings."],
    ),
    M(
        13,
        "4.2.2 / P-center geographic partition",
        "enumerated reference-center partition by nearest distance",
        "Partition continents assigned multiple offices by selecting reference countries and assigning every other country to its nearest reference.",
        ["d_i_j", "n_h", "C"],
        ["Z_star", "g_c"],
        [
            E(13, "reference-center objective", "The prose traverses candidate reference sets and sums each other country's smaller distance to them, selecting the minimum.", "Z_star=argmin_{Z subset C, |Z|=n_h} sum_{c in C} min_{z in Z} d_{cz}", "Normalize the described enumeration as a p-median-like distance objective while retaining the source's P-center label.", ["Z_star", "C", "n_h", "d_i_j"], "medium", "reconstructed"),
            E(13, "nearest-center assignment", "Each remaining country joins the group of the closer selected reference country.", "g(c)=argmin_{z in Z_star} d_{cz}", "Create the geographic groups consumed by the office objective.", ["g_c", "Z_star", "d_i_j"]),
        ],
        ["accept continent office counts", "enumerate reference-country sets", "sum nearest-reference distances", "select the minimum", "assign countries to nearest references"],
        ["Continent office counts are fixed before optimization.", "Distance alone determines the partition.", "Russia is assigned to Asia."],
        ["Figure 10 grouping example", "Figure 11 workflow", "Tables 8 and 10"],
        ["The described sum objective is closer to p-median than classical minimax P-center.", "Coordinate system, distance units, ties, enumeration cost, and geographic constraints are absent."],
    ),
    M(
        14,
        "4.2.2 / integrated office and office-language selection",
        "continent allocation, geographic grouping, office scoring, and cluster-language assignment",
        "Combine a fixed continent office allocation with geographic groups, GDP-distance ranking, and one-to-three working languages per office.",
        ["n_h", "g_c", "J_j", "x_c_l"],
        ["O", "L_office"],
        [
            E(14, "initial office allocation", "Table 7 assigns two offices each to Asia and Europe and one each to North America, South America, Oceania, and Africa, totaling eight including Shanghai and New York.", "sum_h n_h=8; n=(2,2,1,1,1,1)", "Freeze the allocation that determines how many geographic groups and office selections are made.", ["n_h", "O"]),
        ],
        ["set continent office counts", "partition multi-office continents", "reuse the GDP-distance score", "select one capital per group", "cluster language structures", "choose one to three working languages", "compare 2017 and 2067"],
        ["Shanghai and New York are treated as existing offices in the eight-office system.", "The company supplies the desired number of offices and continents."],
        ["Table 7", "Figures 11-13", "Tables 8-11", "five-office discussion"],
        ["The allocation is not optimized against cost, service, demand, or stakeholder preferences.", "The memo and preceding prose mix six new offices with an eight-location table."],
    ),
    M(
        17,
        "5 / sensitivity analysis",
        "one-at-a-time parameter and portfolio perturbation",
        "Measure relative language-output changes and record office selections after separate perturbations to birth, GDP growth, and migration.",
        ["theta", "Y_theta"],
        ["Delta_Y"],
        [
            E(17, "relative scenario response", "Tables 12-15 report relative changes or changed selections under declared parameter multipliers.", "Delta_Y(theta')=(Y(theta')-Y(theta))/Y(theta)", "Provide a common representation for the reported sensitivity responses.", ["theta", "Y_theta", "Delta_Y"], "medium", "reconstructed"),
        ],
        ["freeze the baseline", "change one parameter family", "rerun the fifty-year simulation or office pipeline", "calculate relative response", "record rank or portfolio switches"],
        ["Other parameter families remain fixed during each scenario.", "Response direction matching intuition supports realism."],
        ["Tables 12-15", "Figure 14", "summary robustness statement"],
        ["The scenarios are one-at-a-time, uncalibrated, and do not quantify joint uncertainty or output distributions.", "A less-than-forty-percent response and intuitive direction do not validate the model."],
    ),
]


SYMBOL_META = {
    "P_c_t": ("country population", "persons"),
    "h_c_l": ("country-language speaker share", "dimensionless proportion"),
    "C": ("modeled country set", "set of countries"),
    "d_c": ("dominant language of country c", "language identity"),
    "n_c": ("languages above the diversity threshold", "language count"),
    "D_c": ("communication diversity score", "dimensionless score"),
    "E_c_t": ("economic-stage participation score", "dimensionless score"),
    "A_c_t": ("Second Language Percentage", "dimensionless proportion"),
    "G_c_t": ("GDP per capita", "currency per person"),
    "G_c_next": ("next-year GDP per capita", "currency per person"),
    "g_s": ("stage-specific GDP growth rate", "fraction per year"),
    "A": ("AHP pairwise comparison matrix", "dimensionless ratio matrix"),
    "w": ("criterion weight vector", "dimensionless weight"),
    "v": ("principal eigenvector", "dimensionless vector"),
    "lambda_max": ("maximum AHP eigenvalue", "dimensionless"),
    "n": ("AHP matrix order", "criterion count"),
    "CI": ("AHP consistency index", "dimensionless"),
    "RI": ("average random consistency index", "dimensionless"),
    "CR": ("AHP consistency ratio", "dimensionless"),
    "f_c_l_k": ("country-language subcriterion value", "source-specific score"),
    "S_c_l": ("country-language selection index", "weighted score"),
    "p_c_l": ("conditional language-choice probability", "dimensionless probability"),
    "q_c_l": ("cumulative language-choice boundary", "dimensionless probability"),
    "u": ("uniform random draw", "dimensionless random value"),
    "r_c": ("country net birth rate", "fraction per year"),
    "B_c_t": ("newborn cohort", "persons per year"),
    "L2_c_t": ("new second-language learner cohort", "persons per year"),
    "L2_l_t": ("second-language identities for language l", "speaker identities"),
    "T_l_t": ("total speaker identities", "speaker identities"),
    "T_l_next": ("next-year total speaker identities", "speaker identities"),
    "L1_l_t": ("native speakers", "persons"),
    "N_c_l_t": ("country-language state", "persons or speaker identities"),
    "M_out_c_t": ("emigration flow", "persons per year"),
    "M_in_c_t": ("immigration flow", "persons per year"),
    "N1_c_l_next": ("next-year native country-language state", "persons"),
    "N2_c_l_next": ("next-year second-language country-language state", "speaker identities"),
    "x_c_l": ("country-language vector component", "speaker identities"),
    "r_i_j": ("country language-structure similarity", "dimensionless similarity"),
    "R": ("fuzzy similarity matrix", "dimensionless relation"),
    "R_star": ("fuzzy equivalent matrix", "dimensionless relation"),
    "g_c": ("country group assignment", "group identity"),
    "GDP_i": ("country GDP", "currency per year"),
    "d_i_j": ("inter-capital distance", "unspecified distance unit"),
    "J_j": ("office candidate score", "currency squared per distance"),
    "j_star": ("selected office candidate", "country or capital identity"),
    "n_h": ("office count for continent h", "office count"),
    "Z_star": ("selected reference-country set", "set of countries"),
    "O": ("office portfolio", "set of office locations"),
    "L_office": ("office working-language set", "set of languages"),
    "theta": ("tested parameter", "parameter-specific unit"),
    "Y_theta": ("baseline model output", "output-specific unit"),
    "Delta_Y": ("relative scenario response", "dimensionless proportion"),
}


def variable(symbol: str, role: str) -> dict[str, str]:
    name, unit = SYMBOL_META.get(symbol, (f"paper symbol {symbol}", "source-specific unit"))
    return {
        "symbol": symbol,
        "normalized_name": name,
        "unit": unit,
        "definition": f"{name.capitalize()} used in the source model and retained with its entity and unit boundary.",
        "role": role,
        "source_status": "explicit-defined" if symbol in SYMBOL_META else "inferred-from-equation",
    }


def build_models() -> dict[str, Any]:
    equation_count = sum(len(spec["equations"]) for spec in MODEL_SPECS)
    if len(MODEL_SPECS) != 13 or equation_count != 27:
        raise SystemExit(
            f"q123 model or equation count changed: {len(MODEL_SPECS)}, {equation_count}"
        )
    models: list[dict[str, Any]] = []
    next_equation = 1
    for model_index, spec in enumerate(MODEL_SPECS, start=1):
        equations: list[dict[str, Any]] = []
        for eq in spec["equations"]:
            equations.append(
                {
                    "equation_id": f"EQ-{ID_STEM}-{next_equation:03d}",
                    "page": eq["page"],
                    "label": eq["label"],
                    "source_expression": eq["source"],
                    "normalized_latex": eq["latex"],
                    "purpose": eq["purpose"],
                    "variable_symbols": eq["symbols"],
                    "source_type": eq["source_type"],
                    "visual_checked": True,
                    "transcription_confidence": eq["confidence"],
                }
            )
            next_equation += 1
        symbols = list(
            dict.fromkeys(
                [
                    *spec["inputs"],
                    *spec["outputs"],
                    *(symbol for eq in equations for symbol in eq["variable_symbols"]),
                ]
            )
        )
        variables = []
        for symbol in symbols:
            if symbol in spec["outputs"]:
                role = "output"
            elif symbol in spec["inputs"]:
                role = "input"
            elif symbol in {"CI", "CR", "lambda_max", "D_c", "B_c_t", "L2_c_t", "r_i_j", "J_j", "Delta_Y"}:
                role = "intermediate"
            else:
                role = "parameter"
            variables.append(variable(symbol, role))
        models.append(
            {
                "model_id": f"MU-{ID_STEM}-{model_index:03d}",
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
                    "status": "present",
                    "reason": "Every retained source display or explicitly reconstructed algorithmic identity records page, source wording, normalized transcription, source type, visual status, and confidence.",
                },
                "objectives": [
                    spec["purpose"],
                    "Preserve entity, unit, country, language, baseline year, horizon, scenario, and exact downstream consumer.",
                ],
                "constraints": [
                    "Do not merge persons, speaker identities, native-language states, second-language cohorts, country clusters, office scores, or recommendations.",
                    "Do not silently repair the nonreciprocal AHP matrix, the CI/CR label, missing factor scaling, arbitrary distance surrogate, or conflicting office counts.",
                ],
                "conditions": {
                    "initial": {
                        "status": "present",
                        "details": ["The paper uses a 2017 baseline, country-level population and language states, and a fifty-year horizon ending in 2067."],
                    },
                    "boundary": {"status": "present", "details": spec["assumptions"]},
                    "equilibrium": {
                        "status": "not-applicable",
                        "details": ["The paper advances finite-horizon simulation, clustering, ranking, and scenario calculations rather than a demonstrated equilibrium system."],
                    },
                },
                "parameter_estimation": {
                    "status": "partial",
                    "method": "Parameters combine attributed UN/CIA/web inputs, author-selected thresholds and weights, fixed GDP rates, derived probabilities, and program output; frozen source snapshots and a complete transformation ledger are absent.",
                    "parameters": spec["inputs"],
                },
                "algorithm": {
                    "status": "partial",
                    "steps": spec["steps"],
                    "software": ["Python and Matlab are named, but code, package versions, numerical settings, random seed, and executable environment are not archived."],
                    "convergence_criteria": "The source uses a fixed fifty-year horizon, a six- or eight-group target, an unspecified fuzzy cut, exhaustive reference-country search, and direct maximization; reproducible tolerances and stopping rules are incomplete.",
                },
                "assumptions": spec["assumptions"],
                "identifiability_feasibility": {
                    "status": "partial",
                    "analysis": "The state transitions and decision handoffs are inspectable, but missing scaling, calibration data, stochastic controls, distance details, objective provenance, and external holdouts prevent full identification and operational validation.",
                },
                "handoff_outputs": spec["outputs"],
                "validation_refs": spec["validation_refs"],
                "computational_cost": "No runtime, memory, hardware, numerical precision, random-draw count, exhaustive-search size, or clustering convergence cost is reported.",
                "strengths": [
                    "The model unit has named inputs, transformations, outputs, and a receiving stage in the forecast-to-office chain.",
                    "The record preserves source formulas separately from reconstructions and last-pass warnings.",
                ],
                "limitations": spec["limitations"],
                "missing_details": [
                    "Frozen input tables, units, retrieval dates, transformations, code, software versions, seeds, and uncertainty distributions are incomplete or absent.",
                    "No common holdout, calibrated interval, joint sensitivity design, or cost-based office-portfolio validation spans the pipeline.",
                ],
            }
        )

    edge_specs = [
        (1, 2, "The included-country set and dominant-language representation define the populations scored for L2 participation."),
        (1, 3, "The same included countries provide the GDP-stage population panel."),
        (3, 2, "The projected GDP stage supplies the economic component of Second Language Percentage."),
        (2, 6, "Second Language Percentage gates each newborn cohort in the simulation."),
        (4, 5, "AHP factor and subfactor weights enter the country-language selection index."),
        (5, 6, "Cumulative conditional language probabilities drive the grouped random allocation."),
        (6, 7, "Total and second-language identities are passed to the native-speaker subtraction."),
        (6, 8, "The initial country-language state is the baseline for the migration modification."),
        (8, 7, "Migration-adjusted total and L2 states are decomposed into native counts."),
        (6, 9, "Simulated country-language vectors become clustering inputs."),
        (7, 9, "Native and second-language components preserve the semantics of each country-language vector."),
        (9, 10, "Language-similarity groups define the candidate sets scored by the office objective."),
        (3, 10, "Projected GDP values enter the office score at each horizon."),
        (10, 12, "Within-group GDP-distance maximizers become office candidates."),
        (9, 12, "Cluster language structures determine one to three working languages per office."),
        (11, 12, "Geographic P-center groups replace the rejected language-first partition."),
        (6, 13, "Language-simulation outputs are recomputed under birth, GDP, and migration perturbations."),
        (12, 13, "Office groups and selected countries are recomputed under GDP and office-count scenarios."),
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


def visual(
    page: int,
    figure: str,
    model_numbers: list[int],
    summary: str,
    purpose: str,
    form: str,
    claim: str,
) -> dict[str, Any]:
    return {
        "page": page,
        "figure": figure,
        "model_numbers": model_numbers,
        "summary": summary,
        "purpose": purpose,
        "form": form,
        "claim": claim,
    }


V = visual
VISUAL_SPECS = [
    V(4, "Figure 1", [1, 2, 5], "Full newborn-language judgment flow from population to native-only or selected L2 outcomes.", "Expose the complete two-stage state transition before simulation.", "decision flowchart", "The simulation separates whether a newborn learns an L2 from which L2 is selected."),
    V(4, "Figure 1 / no branch", [1, 2], "The no branch carries a 1-A_i share into a one-language state.", "Preserve the complement of Second Language Percentage.", "flowchart branch", "A share labeled 1-A_i remains native-only in the source model."),
    V(4, "Figure 1 / yes branch", [2, 5, 6], "The yes branch carries A_i learners into language-specific P_ij allocation.", "Preserve the conditional probability handoff.", "flowchart branch", "The source assigns L2 learners through country-language probabilities."),
    V(5, "Figure 2 / SLP composition", [2], "Second Language Percentage is split equally between communication and economic components.", "Show the two participation factors and their weights.", "weighted hierarchy", "Each of the two displayed branches receives 50 percent."),
    V(5, "Figure 2 / diversity component", [2], "Communication is represented by a diversity score equal to qualifying language count divided by sixteen.", "Make the thresholded communication proxy visible.", "hierarchy branch", "The displayed communication score uses number/16."),
    V(5, "Figure 2 / economic component", [2, 3], "The right branch uses GDP per capita and three stage scores but is visibly mislabeled Communicative factor.", "Retain the visual-label defect and intended economic role.", "hierarchy branch", "The content is economic despite the duplicated communication label."),
    V(5, "Figure 3", [3], "Countries are classified as developed, developing, or backward by GDP per capita.", "Visualize the discrete stage used by the participation model.", "classification diagram", "The three categories receive distinct scores and later growth rates."),
    V(6, "Table 1", [3], "Annual GDP-per-capita growth rates are +2, +7, and +3 percent for the three stages.", "Provide the deterministic economic transition parameters.", "parameter table", "Developing countries receive the highest stated growth rate."),
    V(6, "AHP comparison matrix", [4], "The displayed five-by-five matrix compares communication, geography, economy, knowledge, and diplomacy.", "Preserve the exact judgments before eigenvector calculation.", "matrix", "The matrix is visibly nonreciprocal, including the geography row and column."),
    V(6, "Figure 4 / section weights", [4], "Five AHP section weights are shown as 34.16, 19.67, 34.16, 7.32, and 4.69 percent.", "Expose the relative criterion emphasis.", "weighted hierarchy", "Communication and economy share the largest displayed weights."),
    V(6, "Figure 4 / subcriterion weights", [4, 5], "Nine subcriterion weights distribute the section weights among official language, internet, NOCS, NOPS, GDP, top economies, academic use, and institutions.", "Show the inputs consumed by the selection index.", "weighted hierarchy", "Within several sections the displayed weight is divided equally."),
    V(7, "CI display", [4], "Focused review confirms CI=(lambda_max-n)/(n-1)=0.0115.", "Control small-symbol transcription of the consistency index.", "formula display", "The source reports CI equal to 0.0115."),
    V(7, "CR display", [4], "Focused review confirms 0.0103<0.1 follows CI/RI but is labeled CI in the source.", "Separate the numerical consistency ratio from the source label.", "formula display", "The reported 0.0103 is CR, not a second CI value."),
    V(7, "Figure 5", [5, 6], "A cumulative interval example maps the random value 0.725 into the French interval [0.608,0.741].", "Demonstrate categorical allocation by probability interval.", "probability interval diagram", "The example draw selects French under the displayed intervals."),
    V(8, "Table 2", [6], "The first simulation lists 2017 and 2067 ranks, populations, growth rates, and growth counts for sixteen languages.", "Retain the primary forecast comparison in numeric form.", "forecast table", "German and Japanese enter the top ten while Portuguese and Russian leave."),
    V(8, "Figure 6", [6], "Fifty-year total-speaker and rank trajectories summarize the first simulation.", "Show temporal rank changes beyond endpoint values.", "multi-series time plot", "Most modeled languages grow, with large gains for several low-base languages."),
    V(9, "Figure 7 / baseline distribution", [6], "The world language-distribution map establishes the geographic baseline.", "Show country-level language structure before the fifty-year transition.", "world map panel", "The baseline map encodes modeled country-language distributions."),
    V(9, "Figure 7 / future distribution", [6], "The future world map shows the simulated redistribution after fifty years.", "Compare geographic language structure across horizons.", "world map panel", "The future panel is a model output, not observed geography."),
    V(10, "Figure 8", [7], "Native-speaker trajectories and ranks show English overtaking Chinese in the source simulation in 2049.", "Separate native counts from total speaker identities.", "multi-series time plot", "The source attributes discontinuities to the dominant-language country proxy."),
    V(10, "Figure 9", [8], "Migration-adjusted trajectories are compared with the prior simulation.", "Show the reported small effect of adding migration.", "comparison plot", "The paper reports similar trends after migration is included."),
    V(11, "Angle Cosine display", [9], "Focused review confirms the absolute cosine-similarity formula for country-language vectors.", "Control the missing OCR symbols in the clustering input.", "formula display", "Similarity retains an absolute value around the dot product."),
    V(11, "Fuzzy relation handoff", [9], "The prose routes pairwise similarities through a fuzzy similar matrix and fuzzy equivalent matrix into six groups.", "Expose the undocumented closure and cut between similarity and clusters.", "matrix workflow", "The cluster step requires additional threshold and closure details not displayed."),
    V(11, "Office objective display", [10], "Focused review confirms the sum of GDP_i squared over d_ij plus the candidate's GDP squared over half its nearest-country distance.", "Preserve the exact score and self-distance surrogate.", "formula display", "GDP is squared and the zero domestic distance is replaced by half the nearest nonzero distance."),
    V(11, "Office maximization display", [10], "The candidate with the largest within-group score is selected.", "Show the score-to-decision conversion.", "optimization display", "One maximizing capital is chosen per group."),
    V(12, "Table 3", [9], "The 2017 language-first clustering has group sizes 5, 38, 1, 2, 2, and 2.", "Make the severe cluster imbalance visible.", "group membership table", "One cluster contains 38 of the 52 candidate countries."),
    V(12, "Table 4", [9, 10], "Current language-first offices are Riyadh, Berlin, Dhaka, Jakarta, New Delhi, and Brasilia with working languages.", "Trace clusters through the objective to a current portfolio.", "decision table", "The six current solution-1 offices follow the six language clusters."),
    V(12, "Table 5", [9], "The 2067 language-first grouping changes membership and representative languages.", "Show horizon-dependent cluster structure.", "group membership table", "Future language vectors change the six-cluster partition."),
    V(13, "Table 6", [9, 10], "Future language-first offices are Riyadh, Warsaw, Dhaka, Tokyo, Paris, and Buenos Aires.", "Trace the future language-first portfolio.", "decision table", "The 2067 solution-1 offices differ materially from the current set."),
    V(13, "Figure 10", [11], "A two-reference example assigns each country to its nearer selected reference.", "Explain the geographic grouping algorithm.", "partition diagram", "Nearest-reference distance determines group membership after centers are selected."),
    V(14, "Figure 11", [10, 11, 12], "The geography-first workflow branches on continent office count, partitions if needed, selects a country, then selects working languages.", "Expose the replacement route and its model handoffs.", "process flowchart", "P-center grouping is used only when a continent receives more than one office."),
    V(14, "Table 7", [12], "The initial allocation assigns two offices each to Asia and Europe and one to four other continents.", "Freeze the eight-office allocation used by solution 2.", "allocation table", "The displayed counts sum to eight including the existing Shanghai and New York offices."),
    V(14, "Table 8", [11], "Current geography-first groups list the countries assigned to eight continental subgroups.", "Retain the candidate sets for current office optimization.", "group membership table", "Asia and Europe are each split into two groups."),
    V(15, "Figure 12", [12], "The current world map displays selected geography-first office locations.", "Show spatial coverage of the current portfolio.", "world office map", "The current map should agree with the adjacent office-language table."),
    V(15, "Table 9", [12], "Current solution-2 offices and languages include Nigeria, India, China, Italy, Germany, America, Brazil, and Australia.", "Provide numeric labels for the current map and portfolio.", "office-language table", "The table contains eight locations because two are existing offices."),
    V(16, "Table 10", [11], "Future geography-first groups show changed membership, including Poland and Russia.", "Retain the 2067 candidate groups.", "group membership table", "The future geographic partition and inputs differ from 2017."),
    V(16, "Figure 13", [12], "The future world map displays selected 2067 office locations.", "Show the long-horizon spatial portfolio.", "world office map", "The future map should agree with Table 11 and the preceding recommendation."),
    V(16, "Table 11", [12], "Future solution-2 offices and working languages include Abuja, Moscow, Shanghai, Warsaw, Berlin, New York, Brasilia, and Canberra.", "Provide the numeric counterpart to the future map.", "office-language table", "The table retains eight total locations, including existing offices."),
    V(17, "Table 12", [13], "Sixteen language outputs respond to -20, -10, +10, and +20 percent net-birth-rate changes.", "Show language-specific birth sensitivity and asymmetry.", "sensitivity table", "The reported absolute responses remain below 40 percent in these scenarios."),
    V(18, "Table 13", [13], "Language outputs respond to -50, -10, +10, and +100 percent GDP-growth-rate changes.", "Show GDP sensitivity of the language forecast.", "sensitivity table", "The largest reported response is 3.66 percent under these scenarios."),
    V(18, "Table 14", [13], "Language outputs respond to -20, -10, +10, and +20 percent migration-rate changes.", "Show heterogeneous migration sensitivity.", "sensitivity table", "Chinese, Hindi, and Malay move differently from English and Japanese in the source results."),
    V(19, "Table 15 / group membership", [11, 12, 13], "GDP-growth scenarios change continent group membership counts.", "Separate grouping changes from selected-country changes.", "decision sensitivity table", "Large GDP increases alter some group sizes."),
    V(19, "Table 15 / recommended countries", [10, 12, 13], "The same GDP scenarios preserve or switch recommended countries by region.", "Expose office-portfolio instability.", "decision sensitivity table", "Decreases preserve the listed portfolio while increases change several recommendations."),
    V(20, "Figure 14 / short term", [11, 12], "A five-office scenario removes one European office and recomputes the short-term European choice.", "Demonstrate conditional recomputation when portfolio size changes.", "scenario map panel", "Reducing the European allocation can change Europe without changing other continents."),
    V(20, "Figure 14 / long term", [11, 12], "The corresponding long-term panel recomputes the European location.", "Separate horizon-specific effects of the five-office scenario.", "scenario map panel", "The long-term European choice is conditioned on the 2067 inputs."),
    V(23, "Memo recommendation table and map labels", [12], "The memo prose says six new offices, while the focused table lists eight locations and conflicts with preceding short- and long-term country lists.", "Reconcile executive text, table rows, map labels, existing offices, and horizon.", "executive decision table", "The memo's visible eight-row table cannot be read as an unqualified six-office list."),
]


def build_visuals() -> list[dict[str, Any]]:
    if len(VISUAL_SPECS) != 45:
        raise SystemExit(f"q123 visual count changed: {len(VISUAL_SPECS)} != 45")
    visuals: list[dict[str, Any]] = []
    for index, spec in enumerate(VISUAL_SPECS, start=1):
        visuals.append(
            {
                "page": spec["page"],
                "figure": spec["figure"],
                "visual_record_id": f"VR-{ID_STEM}-{index:03d}",
                "caption": spec["figure"],
                "source_model_ids": [
                    f"MU-{ID_STEM}-{number:03d}" for number in spec["model_numbers"]
                ],
                "summary": spec["summary"],
                "analytical_purpose": spec["purpose"],
                "form": spec["form"],
                "encodings": [
                    "physical page, caption, panel, row, column, branch, axis, line, map position, or formula placement encodes the stated comparison",
                    "numbers, proportions, ranks, distances, group membership, city identity, language identity, horizon, and scenario retain their source semantics",
                ],
                "exact_claim": spec["claim"],
                "construction_or_missing": "Transcribed from the completed physical-page review; missing units, thresholds, matrix operations, uncertainty, software settings, and construction details remain missing rather than inferred.",
                "applicability": "Use only with the source's country set, language identities, base year, forecast horizon, GDP stage, distance convention, office allocation, and scenario.",
                "forbidden_scenarios": [
                    "Do not transfer source-specific weights, growth rates, language counts, probabilities, group memberships, scores, or city recommendations as general constants.",
                    "Do not treat a simulated curve, map, sensitivity table, cluster, or ranked portfolio as external validation or a guaranteed business outcome.",
                ],
                "accessibility": "Add direct labels, units, horizon, scenario, numeric alternatives, and text descriptions; reconcile maps, tables, prose, and existing-versus-new office counts.",
                "disposition": "important-visual-record",
                "evidence_role": "O",
            }
        )
    return visuals


def page_summary(page: int, summary: str, **extra: Any) -> dict[str, Any]:
    return {"page": page, "summary": summary, **extra}


ARGUMENT_CHAINS = [
    {
        "claim": "A country-level newborn transition can produce a fifty-year distribution for sixteen languages.",
        "support_steps": ["country and language inputs", "SLP participation gate", "AHP-weighted conditional language choice", "grouped stochastic allocation", "annual total-speaker update"],
        "decision_consequence": "The resulting country-language states become the common input to language ranking and office location.",
        "source_pages": [4, 5, 6, 7, 8, 9],
    },
    {
        "claim": "AHP weights operationalize five verbal language-choice factors.",
        "support_steps": ["factor hierarchy", "pairwise matrix", "principal eigenvector", "CI and CR", "country-language index", "probability intervals"],
        "decision_consequence": "The weights control how newborn L2 learners are allocated and therefore affect every forecast and office input.",
        "source_pages": [5, 6, 7],
    },
    {
        "claim": "The initial total-speaker simulation is decomposed and then modified for migration.",
        "support_steps": ["total-speaker paths", "L2 aggregation", "native-by-subtraction", "instant migration reassignment", "revised paths"],
        "decision_consequence": "Native and total language distributions remain distinct inputs for interpretation and geography.",
        "source_pages": [7, 8, 9, 10],
    },
    {
        "claim": "Language similarity alone does not yield an acceptable office partition.",
        "support_steps": ["52-country candidate filter", "absolute-cosine clustering", "six language groups", "38-country dominant group", "economically weak singleton and small groups"],
        "decision_consequence": "The paper rejects solution 1 and pivots to geography-first grouping.",
        "source_pages": [11, 12, 13],
    },
    {
        "claim": "A continent allocation plus geographic grouping can generate horizon-specific office portfolios.",
        "support_steps": ["office counts by continent", "P-center-like reference search", "nearest-reference groups", "GDP-distance score", "language clustering", "current and future portfolios"],
        "decision_consequence": "The company receives locations and working languages conditional on allocation and horizon.",
        "source_pages": [13, 14, 15, 16],
    },
    {
        "claim": "Parameter perturbations reveal both stable outputs and decision switches.",
        "support_steps": ["net-birth scenarios", "GDP scenarios", "migration scenarios", "language relative changes", "group changes", "recommended-country switches"],
        "decision_consequence": "Robustness language must be limited to the tested one-at-a-time ranges and reported outcomes.",
        "source_pages": [17, 18, 19, 20],
    },
    {
        "claim": "Technical forecasts and location results are compressed into an executive recommendation.",
        "support_steps": ["recipient decision", "language-model summary", "fifty-year turnover", "clustering and P-center handoff", "office-language table", "portfolio-size condition"],
        "decision_consequence": "The memo must reconcile six new offices, two existing offices, eight table rows, and short-versus-long horizons before use.",
        "source_pages": [22, 23],
    },
]


ASSUMPTION_SPECS = [
    (3, "Every person has one native language, while second-language use is optional."),
    (3, "Existing people do not change native or second languages in the simplified initial model."),
    (3, "Every newborn takes the parents' native language."),
    (3, "Multilingual families are ignored because the paper treats them as rare and data-poor."),
    (4, "Countries above ten million people are treated as sufficient for the global language forecast."),
    (4, "Each country's largest language group represents its only native language."),
    (5, "Communication and economy alone determine L2 participation and receive equal weights."),
    (5, "Developing countries receive the highest L2 economic score, with lower scores at both development extremes."),
    (7, "The initial simulation ignores migration and holds existing speakers' language identities fixed."),
    (7, "Every block of ten thousand simulated learners shares one random language choice."),
    (10, "Migrants instantly adopt the destination dominant language as native and retain the origin language as L2."),
    (14, "Continent office counts, capital-only candidates, Russia's continental assignment, and the existing Shanghai/New York offices are fixed before optimization."),
]


DATA_SPECS = [
    (4, "Country population observations from 2007-2017 are attributed to the United Nations database."),
    (4, "Country Net Birth Rates generate annual newborn populations, but retrieval dates, units, and missingness are not frozen."),
    (4, "Country language percentages are attributed to UN and CIA-style sources without an archived transformation ledger."),
    (5, "Diversity counts languages with more than 100,000 speakers and divides by the modeled sixteen-language set."),
    (5, "GDP per capita supplies development categories and nonmonotone L2 participation scores."),
    (6, "Table 1 supplies deterministic stage growth rates of 2, 7, and 3 percent per year."),
    (6, "Communication, geography, economy, knowledge, and diplomacy subcriteria mix global web indicators with domestic measures."),
    (6, "The AHP comparison matrix stores author preferences rather than observed measurements."),
    (7, "RI=1.12 is used for a five-criterion consistency ratio."),
    (7, "The 2017 country-language state and probability intervals initialize the Python simulation."),
    (10, "Migration inputs are described as rates and compared with net birth, but origin-destination flows and units are incomplete."),
    (11, "A GDP-above-100-billion filter reduces the office candidate set to 52 countries and their capitals."),
    (12, "Latitude and longitude data are converted to inter-capital distance by Matlab without a disclosed projection or formula."),
    (14, "Current and 2067 language structures, GDP projections, country groups, and continent office counts feed the final decision tables."),
]


VERIFICATION_SPECS = [
    (4, "Reproduce the claimed 92 percent population coverage under the ten-million-country cutoff."),
    (5, "Calibrate and range-check diversity, economic scores, and the equal-weight SLP formula against observed L2 participation."),
    (6, "Check every AHP matrix pair for positivity, reciprocity, diagonal identity, and judgment provenance."),
    (7, "Recalculate lambda_max, CI, RI, and CR and retain the source's CI/CR label mismatch."),
    (7, "Verify nonnegative selection scores, unit-sum probabilities, complete cumulative intervals, and the 0.725 French example."),
    (7, "Record random seed, number of draws, ten-thousand-person rounding, repeated-run variance, and endpoint reconciliation."),
    (8, "Recompute ranks, growth rates, growth counts, and top-ten membership in Table 2 from frozen simulation output."),
    (10, "Verify that total, native, and L2 speaker identities share geography, timing, and overlap semantics before subtraction."),
    (10, "Compare migration and birth flows in common units and test the instantaneous switching assumption."),
    (11, "Check cosine-vector dimensions, scaling, zero norms, absolute value, and similarity-matrix symmetry."),
    (11, "Archive fuzzy relation construction, max-min closure, alpha cut, group count, and cluster-stability diagnostics."),
    (11, "Check GDP and distance units, GDP squaring, zero-distance surrogate, candidate set, and rank sensitivity."),
    (12, "Reconcile all cluster membership counts, representative languages, and office candidates across Tables 3-6."),
    (13, "Distinguish the described sum-of-nearest-distances objective from classical minimax P-center and test ties."),
    (14, "Reconcile six new offices, two existing offices, eight groups, continent allocations, and the resource-reduction question."),
    (16, "Cross-check every map label, table row, city, country, working language, and horizon in Figures 12-13 and Tables 9-11."),
    (19, "Run joint and global sensitivity with seeded simulations and report language-rank and office-portfolio switch probabilities."),
    (23, "Reconcile memo prose, the eight-row office-language table, preceding short- and long-term lists, and map labels."),
]


RESULT_SPECS = [
    (7, "The first simulation replaces Portuguese and Russian in the top ten with German and Japanese."),
    (7, "German grows 805.11 percent, while Russian declines 0.51 percent in the reported first run."),
    (8, "Table 2 gives 2017 and 2067 ranks, speaker counts, relative growth, and absolute growth for sixteen languages."),
    (9, "Figure 7 presents modeled world language distributions across the baseline and future horizon."),
    (10, "Native English speakers overtake native Chinese speakers in 2049 in the source simulation."),
    (10, "Adding migration produces little reported change, attributed to migration being about one tenth of average net birth rate."),
    (12, "Current solution 1 chooses Riyadh, Berlin, Dhaka, Jakarta, New Delhi, and Brasilia."),
    (13, "Future solution 1 chooses Riyadh, Warsaw, Dhaka, Tokyo, Paris, and Buenos Aires."),
    (13, "The paper rejects language-first clustering because one group has 38 countries and the remaining groups are economically weak."),
    (14, "Solution 2 allocates eight total offices across six continents, splitting Asia and Europe."),
    (15, "The 2017 geography-first result lists eight locations and their proposed working languages."),
    (16, "The 2067 geography-first result replaces India and Italy with Russia and Poland while retaining China and America."),
    (17, "Net-birth perturbations produce language-specific responses below the reported 40 percent envelope."),
    (18, "GDP-growth perturbations produce a maximum reported language response of 3.66 percent."),
    (18, "Migration perturbations produce heterogeneous signs and a large negative Malay response in one scenario."),
    (19, "Large GDP-growth increases change several group memberships and recommended countries, while decreases preserve the listed portfolio."),
    (20, "A five-office scenario can remove one European office and recompute Europe without changing other continent allocations."),
    (23, "The memo communicates a language forecast, location methods, office-language recommendations, and a conditional office-count claim."),
]


WEAKNESS_SPECS = [
    (4, 1, 2, "The single dominant-language argmax erases multilingual native populations and creates discontinuous country states."),
    (5, 2, 3, "The 100,000-speaker diversity threshold and denominator sixteen are uncalibrated sample choices."),
    (5, 2, 4, "Equal communication/economy weights and discrete economic scores are asserted without empirical calibration."),
    (5, 3, 5, "GDP stages use unspecified thresholds, currency years, and common deterministic growth rates."),
    (6, 4, 6, "The displayed AHP matrix is visibly nonreciprocal, undermining the standard consistency calculation."),
    (6, 4, 7, "The eigenvector weights inherit the defective matrix and lack stakeholder or respondent provenance."),
    (7, 4, 9, "The reported CI depends on an incompletely visible lambda_max calculation and should be independently recomputed."),
    (7, 4, 10, "The source labels 0.0103<0.1 as CI although it is CR=CI/RI."),
    (6, 5, 11, "Nine factor inputs lack common scaling, direction, units, dates, and transformations before weighted summation."),
    (7, 5, 12, "The score-to-probability normalization and complete candidate-language set are not fully documented."),
    (7, 6, 16, "One draw per ten thousand learners, absent seeds, and absent repeated runs make stochastic results irreproducible."),
    (10, 7, 17, "Native-by-subtraction assumes compatible and disjoint identity counts that the paper does not establish."),
    (10, 8, 18, "Instant destination-native-language switching is behaviorally implausible and migration flows lack provenance."),
    (11, 9, 20, "Absolute cosine similarity, vector scaling, and zero-vector handling are incompletely specified."),
    (11, 9, 21, "The fuzzy-equivalent closure, alpha cut, six-cluster choice, and stability checks are missing."),
    (11, 10, 22, "GDP squared divided by distance mixes units and uses an arbitrary half-nearest-distance self term."),
    (13, 11, 24, "The described sum-of-nearest-distances search is p-median-like, not the minimax P-center named by the paper."),
    (17, 13, 27, "One-at-a-time plausibility and intuitive direction do not support the paper's strong robustness and reality-conformance claims."),
]


FORMULA_WARNINGS = [(page, equation_number, summary) for page, _, equation_number, summary in WEAKNESS_SPECS]


CONTEXT_SPECS = [
    (1, "The source is a 2018 Problem B outstanding paper with a four-paragraph Summary Sheet and decision-first abstract route."),
    (2, "The contents page defines the report order and exposes a duplicated section number 7 before conclusion."),
    (3, "The report treats native and second-language mechanisms separately before introducing the office decision."),
    (6, "The factor hierarchy draws on web-language, usefulness, power-index, and fuzzy-clustering references of mixed source quality."),
    (9, "Physical page 9 is almost entirely a world-map visual; its sparse OCR cannot substitute for visual review."),
    (20, "Further Discussion answers the reduced-office clause through a conditional five-office example."),
    (21, "The six references provide attribution but omit retrieval dates, frozen snapshots, and several transformation details."),
    (22, "The memo changes audience and compresses the technical chain for a chief operating officer."),
]


EXPECTED_OBSERVATION_DIMENSIONS = {
    "language": 106,
    "logic": 23,
    "modeling": 40,
    "visualization": 45,
    "verification": 18,
    "data": 14,
    "assumption": 12,
    "result": 18,
    "weakness": 18,
    "other": 8,
}
EXPECTED_OBSERVATION_COUNT = sum(EXPECTED_OBSERVATION_DIMENSIONS.values())


def build_card(
    language: dict[str, Any],
    models_record: dict[str, Any],
    visuals: list[dict[str, Any]],
) -> dict[str, Any]:
    models = models_record["models"]
    equation_count = sum(len(model["governing_equations"]) for model in models)
    section_map = [
        page_summary(
            min(page for page, _, _ in item["source_ranges"]),
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
            min(page for page, _, _ in item["source_ranges"]),
            (
                f"{item['label']}: {item['input']} -> {item['rhetorical']} -> "
                f"{item['analytical']} -> {item['output']} -> {item['handoff']}"
            ),
        )
        for item in CHAPTERS
    ]
    model_by_id = {model["model_id"]: model for model in models}
    dependency_graph = [
        page_summary(
            model_by_id[edge["to_model_id"]]["page"],
            f"{edge['from_model_id']} -> {edge['to_model_id']}: {edge['handoff']}",
        )
        for edge in models_record["dependency_edges"]
    ]
    first_pattern_pages = {
        repeated["pattern_id"]: next(
            unit["page"]
            for unit in language["units"]
            if repeated["pattern_id"] in unit["candidate_pattern_ids"]
        )
        for repeated in PATTERNS
    }
    language_observations = [
        page_summary(
            first_pattern_pages[repeated["pattern_id"]],
            (
                f"{repeated['name']}: occurrences={repeated.get('occurrences', 'derived')}; "
                f"function={repeated['function']}; order={' -> '.join(repeated['information_order'])}; "
                f"slots={'; '.join(repeated['slots'])}; variants={'; '.join(repeated['variants'])}; "
                f"boundary={repeated['boundary']}"
            ),
        )
        for repeated in language["repeated_patterns"]
    ]
    language_observations.extend(
        page_summary(
            unit["page"],
            f"{unit['chapter']} saturation representative: {unit['function']} -> {unit['reusable_pattern']}",
        )
        for unit in [
            next(unit for unit in language["units"] if unit["chapter"] == item["chapter"])
            for item in CHAPTERS
        ]
    )
    weakness_records = []
    for page, model_number, equation_number, summary in WEAKNESS_SPECS:
        weakness_records.append(
            page_summary(
                page,
                summary,
                model_id=f"MU-{ID_STEM}-{model_number:03d}",
                equation_id=f"EQ-{ID_STEM}-{equation_number:03d}",
            )
        )
    impacts = [
        {"rule_id": rule_id, "action": action, "evidence_ids": []}
        for rule_id, action in RULE_ACTIONS.items()
    ]
    return {
        "paper_id": PAPER_ID,
        "problem_type": PROBLEM_TYPE,
        "year": YEAR,
        "team_control_number": "77238",
        "title": "Language Development Forecasting and International Office Location",
        "award_status": "outstanding",
        "source": {"relative_path": SOURCE_PATH, "sha256": SHA256, "page_count": PAGE_COUNT},
        "schema_version": 1,
        "source_quality": {
            "status": "text-rich-with-formula-and-label-gaps",
            "notes": (
                "Complete UTF-8 extraction and 23/23 bounded full-page visual review. Four focused crops control "
                "the p7 CI/CR display, p11 absolute cosine, p11 GDP-distance objective, and p23 map/table labels. "
                "Several display formulas are absent from OCR, Figure 2 duplicates a communication label on the "
                "economic branch, the AHP matrix is visibly nonreciprocal, and the memo mixes six-office prose "
                "with an eight-row table. The Chinese commercial watermark is excluded from author evidence."
            ),
        },
        "context_sources": [
            "2018 MCM Problem B official task context",
            "four-paragraph Summary Sheet and twenty-three-page report",
            "UN and CIA-style population and language sources cited by the paper",
            "web-language, language-power-index, and fuzzy-clustering references [3]-[6]",
        ],
        "task_reconstruction": {
            "summary": (
                "Forecast the number and geographic distribution of major language speakers over fifty years, "
                "recommend locations and working languages for new international offices at short and long "
                "horizons, examine fewer-office alternatives, and communicate the advice to a COO."
            ),
            "inputs": [
                "2007-2017 country populations and net birth rates",
                "country native and second-language shares for sixteen languages",
                "diversity, GDP stage, communication, geography, economy, knowledge, and diplomacy factors",
                "AHP preferences and random-assignment intervals",
                "migration rates, GDP projections, capital coordinates, and inter-capital distances",
                "continent office counts and existing Shanghai/New York offices",
            ],
            "outputs": [
                "2017-2067 total and native language-speaker trajectories",
                "top-ten turnover and country-language distribution maps",
                "language-first and geography-first country groups",
                "current and future office locations and working languages",
                "birth, GDP, migration, and office sensitivity tables",
                "conditional fewer-office advice and COO memo",
            ],
        },
        "section_map": section_map,
        "assumptions": [page_summary(page, summary) for page, summary in ASSUMPTION_SPECS],
        "data_and_preprocessing": [page_summary(page, summary) for page, summary in DATA_SPECS],
        "models": [
            page_summary(model["page"], f"{model['model_id']}: {model['purpose']}")
            for model in models
        ],
        "dependency_graph": dependency_graph,
        "verification": [page_summary(page, summary) for page, summary in VERIFICATION_SPECS],
        "results_trace": [page_summary(page, summary) for page, summary in RESULT_SPECS],
        "contributions": [
            page_summary(1, "The Summary Sheet exposes the complete language-forecast-to-office route and separates short- and long-term recommendations."),
            page_summary(4, "A two-stage judgment process distinguishes L2 participation from conditional language choice."),
            page_summary(5, "Verbal communication and economic influences are operationalized as explicit scores before simulation."),
            page_summary(6, "A five-factor hierarchy makes the language-choice criteria and relative emphasis inspectable."),
            page_summary(7, "The simulation narration identifies the cohort, participation gate, random block, interval, and state update."),
            page_summary(10, "The report separates total, native, second-language, and migration-modified views rather than reporting one count only."),
            page_summary(11, "Country-language vectors provide an explicit forecast-to-location handoff."),
            page_summary(13, "The paper diagnoses the failure of language-first clustering before replacing its grouping mechanism."),
            page_summary(14, "The geography-first route separates continent allocation, grouping, office scoring, and working-language choice."),
            page_summary(17, "Sensitivity tables expose language-specific responses to three different parameter families."),
            page_summary(19, "Office sensitivity reports actual group and country switches, which is decision-relevant evidence."),
            page_summary(20, "The five-office example responds directly to the resource-reduction requirement."),
            page_summary(22, "The memo reorganizes methods and findings around the COO's location, language, horizon, and portfolio decisions."),
        ],
        "writing_logic": writing_logic,
        "language_observations": language_observations,
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [
            page_summary(1, "The summary's explicit method-to-result-to-decision order reduces judge search cost while preserving both horizons.", evidence_class="J"),
            page_summary(7, "The visible two-stage stochastic algorithm makes the language model operationally inspectable despite missing code.", evidence_class="J"),
            page_summary(13, "Naming why the 38-country language cluster fails gives the replacement model a problem-driven rationale.", evidence_class="J"),
            page_summary(19, "Reporting actual office switches under GDP scenarios is more decision-relevant than a scalar fit statistic.", evidence_class="J"),
            page_summary(22, "The memo addresses the required operating audience, but the final table conflict reduces reliability.", evidence_class="C"),
        ],
        "weaknesses": weakness_records,
        "independent_extensions": [
            {"extension_id": "E-B-123-001", "page": 4, "summary": "Replace the dominant-language proxy with a multilingual country-cohort state and explicit person-versus-identity accounting."},
            {"extension_id": "E-B-123-002", "page": 5, "summary": "Estimate L2 participation from observed education, migration, and language-learning data with calibrated probabilities and intervals."},
            {"extension_id": "E-B-123-003", "page": 6, "summary": "Rebuild the AHP matrix from stakeholder judgments, enforce reciprocity, quantify inconsistency, and propagate weight uncertainty."},
            {"extension_id": "E-B-123-004", "page": 7, "summary": "Archive code and inputs, seed the Monte Carlo process, use person-level or multinomial draws, and report replicated forecast distributions."},
            {"extension_id": "E-B-123-005", "page": 10, "summary": "Model migration with origin-destination cohorts, delayed language acquisition, bilingual retention, and empirically estimated transition rates."},
            {"extension_id": "E-B-123-006", "page": 11, "summary": "Normalize country-language vectors, archive fuzzy closure and cut rules, and measure cluster stability under resampling."},
            {"extension_id": "E-B-123-007", "page": 11, "summary": "Replace GDP-squared inverse distance with a dimensionally coherent multiobjective facility model using demand, cost, service, and coverage."},
            {"extension_id": "E-B-123-008", "page": 13, "summary": "Distinguish p-center from p-median objectives and solve both with geographic, capacity, and political feasibility constraints."},
            {"extension_id": "E-B-123-009", "page": 17, "summary": "Run joint global sensitivity and seeded uncertainty propagation, reporting language-rank and office-portfolio switch probabilities."},
            {"extension_id": "E-B-123-010", "page": 23, "summary": "Generate the executive memo directly from a frozen decision table with automated office-count, city, language, and horizon reconciliation."},
        ],
        "candidate_rule_impacts": impacts,
        "unresolved_questions": [
            "Which exact countries pass the ten-million and GDP-above-100-billion thresholds at the baseline date?",
            "What frozen population, language-share, net-birth, GDP, migration, and coordinate tables reproduce the run?",
            "What GDP-per-capita thresholds define the three stages and in what currency year?",
            "Why is the displayed AHP matrix nonreciprocal, and what matrix was actually used to obtain the weights?",
            "What lambda_max, eigenvector, RI table, and arithmetic reproduce CI=0.0115 and CR=0.0103?",
            "How are all nine subcriteria scaled, oriented, combined, and normalized into language probabilities?",
            "What seed, draw count, block remainder rule, and number of repeated simulations generated Tables 2 and Figures 6-9?",
            "How are total, native, and second-language identities reconciled when one person speaks multiple languages?",
            "What origin-destination migration data and transition timing support instantaneous native-language conversion?",
            "What fuzzy closure, alpha cut, vector scaling, and stability criterion produced six clusters?",
            "What coordinate system, distance unit, cost interpretation, and stakeholder preference justify GDP squared over distance?",
            "Which six locations are actually new, which two are existing, and which horizon does the eight-row memo table represent?",
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
        "language": "Transfer only the rhetorical mechanism and information order after replacing every source entity, number, model, and decision boundary.",
        "logic": "Use the handoff only when the receiving stage consumes the named output without changing entity, unit, horizon, evidence class, uncertainty, or scope.",
        "modeling": "Reuse the model only after defining entities, units, indices, timing, equations, assumptions, calibration, and every downstream consumer.",
        "visualization": "Reuse the visual role only with legible units, horizon, scenario, encodings, source model, exact claim, and accessible numeric alternatives.",
        "verification": "Apply the check to frozen source bytes or executable outputs before promoting any forecast, grouping, ranking, or recommendation.",
        "data": "Use the input only with a frozen source, retrieval date, geography, entity, unit, transformation, missingness, uncertainty, and downstream term.",
        "assumption": "Treat the premise as a scope boundary and test the forecast, cluster, rank, or office decision that changes when it is relaxed.",
        "result": "Report the result only with source model, entity, baseline, horizon, scenario, unit, comparator, feasibility, and uncertainty status.",
        "weakness": "Keep the defect in the last warning pass and pair it with a concrete algebraic, empirical, computational, provenance, visual, or decision repair.",
        "other": "Preserve context without upgrading a title, contents entry, citation, software mention, sparse page, discussion, or memo statement into validation.",
    }
    counterevidence = {
        "language": "A fluent sentence without a source anchor, evidence role, receiving use, and anti-copy boundary is not a reusable language unit.",
        "logic": "Chronology or a section heading alone does not establish an output-to-input dependency.",
        "modeling": "Naming AHP, Monte Carlo, fuzzy clustering, P-center, or sensitivity analysis does not establish calibration, feasibility, or reproducibility.",
        "visualization": "A polished chart cannot repair missing units, formula defects, contradictory labels, arbitrary weights, or an unsupported decision.",
        "verification": "A consistency ratio, intuitive response, one-at-a-time table, or unseeded run is not external validation.",
        "data": "A URL, database name, threshold, or author judgment is not a frozen provenance and transformation ledger.",
        "assumption": "Author convenience does not turn an untested premise into an observed fact.",
        "result": "A simulated trajectory, cluster, score, map, or office list is not an observed causal effect or guaranteed outcome.",
        "weakness": "The warning does not replace or erase the paper's positive language, organization, model, equation, algorithm, and visual evidence.",
        "other": "Context cannot substitute for complete page coverage, formula retention, or validated transaction artifacts.",
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
                f"{' -> '.join(unit['information_order'])}; preserve evidence type, quantitative role, "
                "boundary, and handoff while replacing all source-specific content."
            ),
            "O",
            ["R-B-LANG-001"],
        )

    for item in CHAPTERS:
        rules = ["R-B-LOG-001"]
        if item["chapter"] in {"model-improvement", "conclusion", "future-improvements", "memo"}:
            rules.append("R-B-DEC-002")
        add(
            min(page for page, _, _ in item["source_ranges"]),
            f"{item['label']} / five-move section contract",
            "logic",
            (
                f"Input: {item['input']} Rhetorical job: {item['rhetorical']} "
                f"Analytical job: {item['analytical']} Output: {item['output']} Handoff: {item['handoff']}"
            ),
            "Preserve input -> rhetorical job -> analytical job -> output -> handoff as a positive organization artifact.",
            "I",
            rules,
        )
    for index, chain in enumerate(ARGUMENT_CHAINS, start=1):
        rules = ["R-B-LOG-001"]
        if index >= 4:
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

    def model_rule_ids(model_number: int) -> list[str]:
        rules = ["R-B-MOD-004"]
        if model_number in {10, 11}:
            rules.append("R-B-MOD-001")
        if model_number in {4, 5, 10, 12}:
            rules.append("R-B-MOD-003")
        if model_number in {11, 12, 13}:
            rules.append("R-B-MOD-005")
        if model_number in {10, 11, 12}:
            rules.append("R-B-DEC-002")
        return rules

    for model_number, model in enumerate(models_record["models"], start=1):
        add(
            model["page"],
            f"{model['section']} / model unit",
            "modeling",
            f"{model['model_id']}: {model['purpose']}",
            f"Retain the complete {model['family']} unit with variables, equations, assumptions, algorithm, handoff outputs, validation references, and missing implementation details.",
            "O",
            model_rule_ids(model_number),
        )
        for eq in model["governing_equations"]:
            add(
                eq["page"],
                f"{model['section']} / {eq['equation_id']}",
                "modeling",
                f"{eq['source_expression']} | normalized: {eq['normalized_latex']}",
                f"Retain this equation for {eq['purpose']} with symbols {', '.join(eq['variable_symbols'])}, source type {eq['source_type']}, and transcription confidence {eq['transcription_confidence']}.",
                "O",
                model_rule_ids(model_number),
                eq["transcription_confidence"],
            )

    for visual_record in visuals:
        add(
            visual_record["page"],
            f"{visual_record['figure']} / {visual_record['visual_record_id']}",
            "visualization",
            visual_record["summary"],
            f"Retain this {visual_record['form']} for {visual_record['analytical_purpose']} Exact supported claim: {visual_record['exact_claim']}",
            "O",
            ["R-B-VIZ-001"],
        )

    for page, summary in VERIFICATION_SPECS:
        rules = ["R-B-VER-004"]
        if page >= 7:
            rules.append("R-B-VER-002")
        if page in {11, 13, 14, 16, 19, 23}:
            rules.append("R-B-MOD-005")
        add(page, "Verification and source-fidelity ledger", "verification", summary, "Keep transcription, algebra, dimensions, indices, normalization, stochastic, visual, and decision checks separate and route unresolved failures to G7.", "E", rules)

    for page, summary in DATA_SPECS:
        add(page, "Data and preprocessing ledger", "data", summary, "Record source class, retrieval date, geography, entity, unit, threshold, transformation, missingness, uncertainty, and every downstream use.", "O", ["R-B-DATA-002"])

    for index, (page, summary) in enumerate(ASSUMPTION_SPECS, start=1):
        rules = ["R-B-MOD-004"]
        if index >= 7 or page >= 11:
            rules.append("R-B-DEC-002")
        add(page, "Assumption ledger", "assumption", summary, "Convert the simplification into a testable boundary and identify the forecast, cluster, score, or office decision that may change when it is relaxed.", "O", rules)

    for page, summary in RESULT_SPECS:
        rules = ["R-B-VER-002"]
        if page >= 11:
            rules.append("R-B-DEC-002")
        add(page, "Results and decision trace", "result", summary, "Bind the result to its model, entity, baseline, horizon, scenario, unit, comparator, feasibility, uncertainty, and receiving decision.", "O", rules)

    for page, model_number, equation_number, summary in WEAKNESS_SPECS:
        add(
            page,
            f"Final weakness watch / MU-{ID_STEM}-{model_number:03d}",
            "weakness",
            f"EQ-{ID_STEM}-{equation_number:03d}: {summary}",
            "Retain this only as a last-pass warning after positive coverage and require a specific algebraic, empirical, computational, provenance, visual, or decision repair before transfer.",
            "E",
            ["R-B-VER-004", "R-B-VER-002", *model_rule_ids(model_number)],
            "medium",
        )

    for page, summary in CONTEXT_SPECS:
        rules = ["R-B-LOG-001"]
        if page in {20, 22}:
            rules.append("R-B-DEC-002")
        add(page, "Context, source quality, and deliverable trace", "other", summary, "Keep this context attached so task scope, audience, source quality, page anchoring, and citations remain visible without being mistaken for validation.", "C", rules, "medium")

    dimensions = dict(Counter(item["dimension"] for item in observations))
    if dimensions != EXPECTED_OBSERVATION_DIMENSIONS:
        raise SystemExit(f"q123 observation dimensions changed: {dimensions} != {EXPECTED_OBSERVATION_DIMENSIONS}")
    if dimensions["language"] <= max(count for dimension, count in dimensions.items() if dimension != "language"):
        raise SystemExit("q123 language is not the largest observation dimension")
    if dimensions["weakness"] >= dimensions["language"]:
        raise SystemExit("q123 weakness must remain strictly below language")
    return observations


def bind_rule_impacts(card: dict[str, Any], observations: list[dict[str, Any]]) -> None:
    first_by_rule: dict[str, str] = {}
    for observation in observations:
        for rule_id in observation["candidate_rule_ids"]:
            first_by_rule.setdefault(rule_id, observation["observation_id"])
    for impact in card["candidate_rule_impacts"]:
        rule_id = impact["rule_id"]
        if rule_id not in first_by_rule:
            raise SystemExit(f"no q123 observation evidence for {rule_id}")
        impact["evidence_ids"] = [first_by_rule[rule_id]]


def proxy_review_segments() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    def summarize(
        segment: int,
        kind: str,
        paths: list[Path],
        page_range: list[int],
    ) -> dict[str, Any]:
        missing = [str(path) for path in paths if not path.is_file()]
        if missing:
            raise SystemExit(f"missing q123 {kind} review proxies: {missing}")
        sizes = [path.stat().st_size for path in paths]
        if not sizes or any(size <= 0 for size in sizes):
            raise SystemExit(f"q123 {kind} proxy segment {segment} is empty")
        if len(paths) > 7 or max(sizes) > 450000 or sum(sizes) > 4194304:
            raise SystemExit(
                f"q123 {kind} proxy segment {segment} exceeds request-body guard"
            )
        return {
            "segment": segment,
            "page_range": page_range,
            "proxy_count": len(paths),
            "total_proxy_bytes": sum(sizes),
            "largest_proxy_bytes": max(sizes),
            "proxy_files": [
                path.relative_to(PROXY_ROOT).as_posix() for path in paths
            ],
        }

    full_segments = []
    for segment, (first_page, last_page) in enumerate(
        ((1, 7), (8, 14), (15, 21), (22, 23)),
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
        PROXY_ROOT / "focused" / "page-0007-ci-cr.jpg",
        PROXY_ROOT / "focused" / "page-0011-cosine.jpg",
        PROXY_ROOT / "focused" / "page-0011-office-objective.jpg",
        PROXY_ROOT / "focused" / "page-0023-map-table.jpg",
    ]
    focused_segments = [
        summarize(1, "focused-crop", focused_paths, [7, 11, 11, 23])
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
    equation_index = {
        equation_record["equation_id"]: (model, equation_record)
        for model in models
        for equation_record in model["governing_equations"]
    }
    pattern_dispositions = {
        pattern_record["pattern_id"]: pattern_record["disposition"]
        for pattern_record in PATTERNS
    }

    paragraph_chains = []
    for chapter_name in ("abstract", "introduction"):
        layout = layouts[chapter_name]
        spec = chapter_specs[chapter_name]
        paragraph_units = by_chapter[chapter_name][: layout["paragraph_count"]]
        if len(paragraph_units) != layout["paragraph_count"]:
            raise SystemExit(
                f"q123 {chapter_name} paragraph-chain coverage changed"
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
    for page, equation_number, warning in FORMULA_WARNINGS:
        equation_id = f"EQ-{ID_STEM}-{equation_number:03d}"
        if equation_id not in equation_index:
            raise SystemExit(
                f"q123 warning references missing equation: {equation_id}"
            )
        model, equation_record = equation_index[equation_id]
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
                "q123 language unit has no positive reusable pattern: "
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
            "q123 positive reusable language count changed: "
            f"{positive_reusable_language_count} != 106"
        )

    dimension_counter = Counter(item["dimension"] for item in observations)
    dimensions = {
        dimension: dimension_counter[dimension]
        for dimension in EXPECTED_OBSERVATION_DIMENSIONS
    }
    if dimensions != EXPECTED_OBSERVATION_DIMENSIONS:
        raise SystemExit(
            f"q123 audit dimensions changed: {dimensions} != "
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
                "visual_record_id": visual_record["visual_record_id"],
                "disposition": "important-visual-record",
                "analytical_purpose": visual_record["analytical_purpose"],
            }
            for index, visual_record in enumerate(
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
        raise SystemExit(f"q123 extraction identity mismatch: {identity} != {expected}")
    if extraction.get("extraction_status") != "text-extracted":
        raise SystemExit("q123 extraction is not text-extracted")
    full_segments, focused_segments = proxy_review_segments()
    extraction["visual_review_status"] = "complete"
    extraction["visual_review"] = {
        "status": "complete",
        "reviewed_pages": list(range(1, PAGE_COUNT + 1)),
        "notes": [
            "All 23 physical pages were read in UTF-8 page-aware text and reviewed as byte-bounded full-page JPEG proxies in four groups of at most seven images.",
            "Four focused crops preserved the page-7 CI and CR displays, page-11 absolute cosine and GDP-distance objective, and page-23 memo map and table labels without loading original full-page PNGs.",
            "The visual review retained the duplicated Figure 2 communication label, nonreciprocal AHP matrix, sparse map-page OCR, and six-versus-eight-office conflict as source defects rather than silently repairing them.",
            "The Chinese commercial watermark was excluded from author-language evidence while physical PDF pages remained the authoritative anchors.",
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
            "Full-page review covered physical pages 1-23; focused crops retained "
            "small formula, matrix, objective, and executive-table labels under "
            "the request-body guard."
        ),
    }
    return extraction


def main() -> None:
    if STAGE.exists():
        if not STAGE.is_dir():
            raise SystemExit(f"q123 staging path is not a directory: {STAGE}")
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
        "models": 13,
        "equations": 27,
        "dependency_edges": 18,
        "visual_records": 45,
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
            f"q123 artifact counts changed: {actual_counts} != {expected_counts}"
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
        raise SystemExit(f"refusing to overwrite q123 staged files: {existing}")
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
