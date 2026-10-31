from __future__ import annotations

"""Create Queue 110 G1-G3 language evidence without entering model work."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-38720-26d38781"
SHORT = "38720"
SHA = "26d38781a179b71806799b0d20f118a5f0b09aa1cf6b8bc7a5e32562a7886a42"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 61
TEXT_DIR = ROOT / "artifacts/papers" / PAPER_ID / "text/pages"
STAGE = ROOT / "tmp/q110-language-stage-v1"

CHAPTERS = [
    ("summary", "abstract", 1, 1, "ABS", "The summary moves from rescue urgency through a probability field and increasingly realistic path simulations to a Bayesian recommendation."),
    ("contents", "title", 2, 3, "TTL", "The contents exposes the full research-to-foundation-to-model-to-decision route and separates ideal detection from discovery uncertainty."),
    ("introduction", "introduction", 4, 5, "INT", "The introduction states a ranked success criterion and previews the evidence, assumptions, simulations, stability checks, and recommendation."),
    ("research-and-candidate-screening", "problem-analysis", 6, 12, "RES", "Historical cases, crash classes, communication delays, search theory, aircraft, and sensors narrow a broad incident into a modelable Atlantic search case."),
    ("variables-scenario-and-search-plane", "notation", 13, 19, "VAR", "Definitions and sourced aircraft specifications connect last contact, glide geometry, containment, sensor sight, and search motion to later calculations."),
    ("general-assumptions", "assumptions", 20, 21, "ASM", "Environmental, crash, and search assumptions define a deliberately idealized first operating regime and its rectangular coordinate system."),
    ("normal-model-foundation", "model-establishment", 22, 23, "MOD", "A normal containment field, ideal detection rule, completion condition, and confidence-interval protocol establish the common simulation interface."),
    ("random-search-baselines", "algorithm", 24, 31, "ALG", "Unbounded, bounded, and containment-weighted random walks create failure and redundancy baselines before systematic routes are introduced."),
    ("systematic-search-paths", "model-improvement", 32, 40, "IMP", "Descending stripes, center-out spiral stripes, and sinusoidal passes progressively reduce overlap and focus effort on high-containment regions."),
    ("discovery-uncertainty-and-bayes", "robustness-verification", 41, 48, "BAY", "Imperfect radar/operator detection triggers Bayesian redistribution, adaptive pass selection, and a fair comparison with a fixed spiral route."),
    ("solution-stability", "sensitivity-robustness", 49, 52, "STA", "A smaller target and a second search plane test whether the recommended logic responds coherently to target size and resource changes."),
    ("comparative-results", "results", 53, 55, "RSL", "Confidence intervals, skew, medians, and success proportions support separate ideal-model and uncertain-discovery comparisons."),
    ("recommendation", "conclusion", 56, 56, "CON", "The recommendation returns to rescue time, rejects idealized speed alone, and selects the uncertainty-aware Bayesian route by discovery rate."),
    ("strengths-weaknesses-and-limits", "strengths-limitations", 57, 57, "SWL", "The evaluation preserves flexibility and rescue-window performance while naming computational, overlap, physical, mobilization, fuel, and cost limits."),
    ("press-conference-document", "memo", 58, 58, "MEM", "The stakeholder document translates prediction, deployment, posterior updating, equipment imperfections, and continued search into public-facing commitments."),
    ("references-and-image-provenance", "references", 59, 61, "REF", "The references expose aviation, search-theory, radar, Bayesian, survival, software, and image dependencies together with provenance gaps."),
]

PATTERNS = [
    "LP-B-INCIDENT-STATE-LOCATION-DRIFT-SEARCH-RECOMMENDATION",
    "LP-B-ASSUMPTION-MECHANISM-JUSTIFICATION-ENABLED-BOUNDARY",
    "LP-B-PARAMETER-ROLE-CALCULATION-OPERATIONAL-HANDOFF",
    "LP-B-GEOMETRY-UNCERTAINTY-BOUND-ALGORITHM-AREA",
    "LP-B-BASELINE-PATH-COVERAGE-DETECTION-COMPARISON",
    "LP-B-SCENARIO-CONDITION-RESULT-DECISION-BOUNDARY",
    "LP-B-STRENGTH-MECHANISM-LIMIT-FUTURE-REPAIR",
    "LP-B-STAKEHOLDER-INPUT-OPERATION-EVIDENCE-ITERATION",
]

MOVES = [
    ("incident-to-decision", "Rank the human objective, reconstruct the uncertain location state, compare executable routes, and retain the decision boundary.", "stake -> state -> candidates -> evidence -> recommendation -> boundary"),
    ("research-to-model-interface", "Use historical and technical research to screen the case, select representative entities, and expose the later model inputs.", "research question -> evidence -> screening criterion -> selected interface"),
    ("assumption-contract", "Pair an idealization with the calculation it enables and the operating condition it excludes.", "mechanism -> assumption -> enabled calculation -> excluded regime"),
    ("baseline-to-repair", "Expose a route failure, add one controlled mechanism, rerun the common experiment, and compare like metrics.", "baseline -> failure -> modification -> rerun -> comparison"),
    ("probability-update", "Connect imperfect observation to a posterior redistribution and let the updated field select the next action.", "prior -> searched area -> nondetection -> posterior -> next pass"),
    ("distribution-to-decision", "Report sample size, center, spread, interval, skew, and success proportion before selecting a route.", "trial protocol -> distribution -> uncertainty -> operational criterion -> choice"),
    ("stability-transfer", "Change a target or resource assumption, preserve the mechanism, and test whether the response remains interpretable.", "baseline -> changed condition -> recalibration -> result -> transfer limit"),
    ("audience-translation", "Translate the technical loop into stakeholder facts, immediate action, evidence feedback, and bounded commitments.", "audience concern -> input -> operation -> feedback -> commitment -> boundary"),
]

EXAMPLES = [
    ("A missing-aircraft response first states the rescue objective and the available last-contact evidence.", "The recommendation remains conditional on the observation and deployment assumptions."),
    ("Historical incidents and sensor specifications are screened for the variables they can defensibly support.", "A representative aircraft is not treated as the full incident population."),
    ("An ideal-detection assumption makes route geometry comparable in the first experiment.", "A later stage replaces it before operational advice is issued."),
    ("A random route establishes redundancy and failure behavior before a structured pass pattern is tested.", "Every candidate is evaluated under the same containment field and stopping rule."),
    ("A failed pass lowers the searched strip's posterior containment and raises the relative mass elsewhere.", "The next pass follows the updated maximum rather than a fixed schedule."),
    ("A skewed time distribution is summarized with both medians and completion proportions.", "The lower conditional mean is not preferred when it excludes many failures."),
    ("A smaller target receives a recalibrated detection probability while the Bayesian mechanism is preserved.", "The comparison states where the transfer differs statistically from the baseline aircraft."),
    ("A public procedure names prediction, deployment, updating, and continued search in operational order.", "It does not promise performance under omitted currents, weather, fuel, or mobilization delays."),
]

PROFILE_DETAILS = {
    "abstract": ("Compress urgency, location construction, route comparison, imperfect detection, measured performance, flexibility, and the final Bayesian decision.", ["stake", "inputs", "model", "candidate routes", "result", "recommendation", "boundary"], ["urgency", "location field", "ideal comparison", "uncertain detection", "decision"]),
    "title": ("Make the document route inspectable from research and variable definition through two model regimes, stability, results, recommendation, communication, and provenance.", ["section", "analytical purpose", "input", "output", "handoff"], ["research", "foundation", "models", "stability", "results", "decision", "communication"]),
    "introduction": ("Rank discovery and rescue time, declare representative entities, and preview the complete evidence-to-recommendation workflow.", ["incident", "stake", "ranked criteria", "research route", "model route", "validation route", "decision"], ["context", "criteria", "approach", "expected decision"]),
    "problem-analysis": ("Convert crash history, communication rules, search theory, and sensor research into a bounded Atlantic incident and candidate model interface.", ["case evidence", "population evidence", "screen", "communication bound", "search principle", "sensor choice"], ["history", "classification", "lost-plane trigger", "probability objective", "sensor boundary"]),
    "notation": ("Define each state, geometric, probability, aircraft, and motion quantity by its unit and downstream consumer before simulation.", ["entity", "symbol", "meaning", "unit", "source or estimate", "consumer"], ["definition", "calculation role", "selected value", "handoff"]),
    "assumptions": ("Group idealizations by environment, crash, and search operation so later realism upgrades have explicit targets.", ["domain", "assumption", "enabled representation", "affected output", "excluded condition"], ["domain", "simplification", "calculation", "scope"]),
    "model-establishment": ("Establish a shared containment field, observation rule, stopping event, and statistical comparison protocol for all candidate routes.", ["distribution", "detection rule", "simulation state", "stopping criterion", "summary statistic"], ["field", "motion input", "completion", "comparison"]),
    "algorithm": ("Present each random baseline through description, update rule, path behavior, trial statistics, diagnosis, and repair handoff.", ["baseline", "state update", "constraint", "trial", "distribution", "failure mechanism", "next repair"], ["route rule", "simulation", "evidence", "diagnosis"]),
    "model-improvement": ("Modify path geometry to remove overlap or prioritize containment, then compare the same time-distribution outputs.", ["prior limitation", "geometry change", "coverage rule", "trial statistics", "comparison", "remaining tradeoff"], ["limitation", "repair", "rerun", "result", "handoff"]),
    "robustness-verification": ("Replace perfect discovery with radar/operator uncertainty, update containment after nondetection, and compare adaptive with fixed routes under a capped horizon.", ["invalid idealization", "detection model", "Bayesian update", "next-action rule", "trial outcomes", "success proportion", "boundary"], ["uncertainty", "posterior", "adaptive route", "comparison", "decision"]),
    "sensitivity-robustness": ("Perturb target size/detectability and search-plane count while preserving the route logic and reporting response distributions.", ["baseline mechanism", "changed condition", "recalibration", "simulation", "interval", "interpretation"], ["condition", "rerun", "result", "transfer limit"]),
    "results": ("Separate ideal and uncertain regimes, compare intervals and skew responsibly, and use completion proportion when censored times distort means.", ["model regime", "candidate set", "sample evidence", "uncertainty", "comparison", "operational choice"], ["regime", "metric", "contrast", "decision"]),
    "conclusion": ("Reconnect the ranked success criteria to the realistic model and choose the route that balances median rescue time with discovery probability.", ["success criteria", "candidate realism", "median", "completion proportion", "recommendation", "scope"], ["criteria", "evidence", "tradeoff", "choice"]),
    "strengths-limitations": ("Attribute strengths to mechanisms and enumerate computational, geometric, physical, temporal, and resource boundaries of the recommendation.", ["strength", "mechanism", "evidence", "limitation", "impact", "repair need"], ["strength", "support", "boundary", "consequence"]),
    "memo": ("Translate posterior-guided search into immediate public-facing prediction, deployment, observation, adjustment, and continuation commitments.", ["audience", "trust concern", "initial input", "deployment", "evidence update", "continued action", "future refinement"], ["concern", "procedure", "feedback", "commitment", "boundary"]),
    "references": ("Expose the source roles for cases, aircraft, radar, search theory, Bayesian updating, survival, images, and computation while retaining reproducibility gaps.", ["source", "claim supported", "artifact role", "access detail", "missing executable dependency"], ["citation", "use", "provenance boundary"]),
}

EVIDENCE = {
    "abstract": [(1, "time is of the essence"), (1, "construct a Gaussian normal distribution bounded by a rectangular search area"), (1, "reducing redundancy and focusing on high probability areas"), (1, "Applying Bayesian Search Theory to our most efficient solution")],
    "title": [(2, "Research"), (2, "Foundation of Analysis"), (2, "Normal Distribution with Discovery Uncertainty"), (3, "Press Conference Document")],
    "introduction": [(4, "The primary objective is to find the missing plane"), (4, "reduce the time it takes to find the plane and any surviving passengers"), (5, "consider what would happen to the search time if we have non-ideal sensor accuracy"), (5, "make recommendations for a useful procedure for finding lost airplanes")],
    "problem-analysis": [(7, "the most modern and applicable case study"), (9, "Types of Incidents We Will Consider"), (11, "probability that a given area contains the lost plane"), (12, "focus on the radar search and imagine that it is an ideal sensor")],
    "notation": [(13, "Crash Uncertainty Time"), (15, "sweep a circle with radius r along the entire segment of length L"), (17, "probability of the plane's location is evenly distributed parallel to the flight path"), (19, "how should our search plane determine its route")],
    "assumptions": [(20, "Wind and ocean currents will not affect the lost plane"), (20, "will not deviate from the flight path until that instant"), (21, "Finding the debris is equivalent to finding the lost plane itself"), (21, "Cost and fuel are not an issue")],
    "model-establishment": [(22, "normal distribution model"), (22, "radar has a 100% probability of detection"), (23, "completion of the search to be when the plane debris is found"), (23, "mean, median, standard deviation, standard error of the mean, and 95% confidence interval")],
    "algorithm": [(24, "travel randomly"), (25, "frequently never finds the crashed aircraft because its path is unbounded"), (26, "redirected orthogonally back into the search area"), (31, "path often overlaps with places it has searched")],
    "model-improvement": [(32, "systematically eliminating stripes of the search area"), (34, "difference between the descending stripes solution and the bounded random solution is statistically significant"), (35, "start in the area with the highest probability"), (40, "spiral striped solution offers the lowest search times")],
    "robustness-verification": [(41, "probability of detection is 100%"), (42, "adjust P(C) after each pass if we don't find the debris"), (44, "different locations for each pass depending on where the new peak"), (48, "proportion of planes found is greater with the Bayesian solution")],
    "sensitivity-robustness": [(49, "adjust the search area to match the Cessna's and the probability of detection"), (50, "difference between finding the Cessna 172 and Boeing 777 is statistically significant"), (51, "start both planes in the center flying opposite directions"), (52, "included an extra search plane to double the effort")],
    "results": [(53, "7 solutions are tested"), (54, "none of the CIs for the nonrandom solutions overlap"), (55, "medians are equal for both cases"), (55, "Bayesian solution, which finds 95% of crashed planes within 24 hours, is preferable")],
    "conclusion": [(56, "measure of success for our solutions is first, whether they find the lost plane"), (56, "medians, which are equal at 4.05 hours each"), (56, "Bayesian Solution finds 95% of Boeing 777s within 24 hours"), (56, "paired with the Bayesian Search flight path")],
    "strengths-limitations": [(57, "adjusted for, many different probabilities of detection"), (57, "becomes exponentially harder to use the Bayesian Solution"), (57, "does not entirely eliminate unnecessary overlap"), (57, "do not take into account fuel and cost")],
    "memo": [(58, "revising and updating our emergency search procedures"), (58, "predict its location based on its last transmitted signal and flight path"), (58, "use data we collect during our search to update our prediction"), (58, "continue to look until the plane is found")],
    "references": [(59, "Aviation Safety Network"), (60, "The Theory of Search: A Simplified Explanation"), (60, "Bayesian Search Models"), (61, "Wolfram Research, Inc., Mathematica")],
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


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    q104 = load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q110_language")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q110_language")
    template = base.load_template_module()
    configure(q104, base, template)
    pages: dict[int, str] = {}
    for page in range(1, PAGE_COUNT + 1):
        source = TEXT_DIR / f"page-{page:04d}.txt"
        if not source.is_file():
            raise FileNotFoundError(source)
        pages[page] = source.read_text(encoding="utf-8")
    language = q104.build_language(base, template, pages)
    selected = []
    per_chapter: dict[str, int] = {}
    for unit in language["units"]:
        chapter = unit["chapter"]
        ordinal = per_chapter.get(chapter, 0)
        if ordinal < 4:
            selected.append(unit)
            per_chapter[chapter] = ordinal + 1
    language["units"] = selected
    if set(per_chapter) != set(PROFILE_DETAILS) or any(value != 4 for value in per_chapter.values()):
        raise RuntimeError(f"language saturation failed: {per_chapter}")
    for unit in language["units"]:
        ordinal = int(unit["language_unit_id"].rsplit("-", 1)[1]) - 1
        function, slots, order = PROFILE_DETAILS[unit["chapter"]]
        page, excerpt = EVIDENCE[unit["chapter"]][ordinal]
        unit["page"] = page
        unit["source_excerpt"] = excerpt
        unit["function"] = function
        unit["reusable_pattern"] = " -> ".join(order)
        unit["information_order"] = order
        unit["reusable_elements"] = slots
        unit["prohibited_generalizations"] = [
            "Do not transfer aircraft class, crash distribution, communication delay, glide range, search-area size, sensor accuracy, target visibility, search speed, time cap, sample result, or route ranking without reconstructing the receiving incident.",
            "Do not turn an ideal sensor, simulated containment field, capped-time conditional mean, confidence-interval comparison, or Bayesian heuristic into a field-validated discovery guarantee or universal best route.",
        ]
        unit["features"]["quantitative_role"] = "bind last-contact time, glide geometry, containment, detection, route motion, target size, sample distribution, time censoring, success proportion, and rescue criterion to a declared decision"
        unit["features"]["transition"] = "first, based on, because, however, unlike, after, therefore, additionally, while, and ultimately connect research, assumptions, baseline failure, path repair, uncertainty update, comparison, and recommendation"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 61 UTF-8 physical-page files were read sequentially. Eighteen one-at-a-time byte-bounded JPEG overview proxies covered pages 1-61 in three fresh contexts; original rendered PNGs remain local coordinate authority for equation, table, and small-label crops."
        layout["ambiguities"] = [
            "The text extractor omits most displayed notation in Equations 1-23 and flattens arrows, primes, subscripts, superscripts, tables, plot labels, and some citations; equation fidelity remains separately crop-verified in G5.",
            "Physical pages 2-3 are contents, pages 59-61 are references, and page 58 is a separately formatted stakeholder press document retained as a memo chapter.",
            "Physical page 56 contains a visibly incomplete sentence ending 'Furthermore, the Bayesian Solution'; physical page 61 labels image references as 8.2 despite Section 10.",
            "No official 2015 problem-statement manifest row was available, so task reconstruction is bounded to the paper's explicit introduction, research choices, and summary.",
        ]
        if layout["chapter"] == "abstract":
            layout["paragraph_count"] = 7
            layout["paragraph_functions"] = [
                "Establish rescue urgency and the failure motivating a faster response.",
                "Connect crash-state and search-plane inputs to candidate path simulation.",
                "State the bounded Gaussian location representation.",
                "Use ideal detection to contrast random and systematic paths.",
                "Introduce imperfect discovery and report Bayesian performance.",
                "State transferability to aircraft count and target size.",
                "Close with the realistic Bayesian recommendation.",
            ]
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = 4
            layout["paragraph_functions"] = [
                "Frame disappearance over open ocean and the affected families.",
                "Rank finding the aircraft, reducing rescue time, and accommodating aircraft and sensor types.",
                "Route research through cases, communication, search theory, sensors, variables, and representative inputs.",
                "Route simulations through ideal and uncertain detection, stability checks, data analysis, and recommendation.",
            ]
    STAGE.mkdir(parents=True)
    output = STAGE / "language.json"
    output.write_text(json.dumps(language, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
