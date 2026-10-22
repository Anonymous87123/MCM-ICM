from __future__ import annotations

"""Create Queue 113 G1-G3 language evidence before model work."""

import json
from pathlib import Path

import build_q112_language_stage as q112


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2016-42745-4dc9ed2b"
SHORT = "42745"
SHA = "4dc9ed2b48ba9415c26b12506e36e0a144491324a4f44445d6ae8083ad7c5b46"
TYPE = "B"
YEAR = "2016"
PAGE_COUNT = 26
TEXT_DIR = ROOT / "artifacts/papers" / PAPER_ID / "text/pages"
STAGE = ROOT / "tmp/q113-language-stage-v3"


CHAPTERS = [
    ("abstract", "abstract", 1, 1, "ABS", "The summary moves from the debris threat through three complementary models to a combined commercial and policy recommendation with an explicit parameter caveat."),
    ("executive-summary", "problem-restatement", 2, 3, "EXE", "The executive summary expands the full model-result-sensitivity-policy route and distinguishes land, space, combined, regulatory, rocket, and insurance conclusions."),
    ("contents-title", "title", 4, 5, "TTL", "The title and contents expose a source-ordered route from methods and notation through two models, three alternatives, scenarios, game theory, conclusions, and improvements."),
    ("introduction", "introduction", 6, 6, "INT", "The introduction converts the space-debris threat into a four-element commercial-opportunity test and a time-dependent feasibility objective."),
    ("existing-methods", "problem-analysis", 6, 7, "MET", "The methods review classifies laser and gas systems as land based and nets and sails as space based, with cost and operating boundaries."),
    ("terminology-notation", "notation", 7, 8, "NOT", "Definitions and a notation table establish the financial, physical, probability, removal, and game-theoretic interfaces used later."),
    ("model-one", "model-establishment", 9, 12, "M1", "The economic model decomposes annual and cumulative income into insurance revenue, removal cost, and collision compensation linked through a utility function."),
    ("model-two-framing", "assumptions", 12, 13, "M2F", "The collision model states debris-motion and hazard assumptions, reduces a three-dimensional orbit to a two-dimensional representation, and selects a Gamma family."),
    ("debris-distribution", "data-preprocessing", 14, 14, "DST", "A 1000 by 1000 binary matrix, four radial layers, Gamma mass, and a hand-set 15 percent occupancy generate a synthetic debris field."),
    ("simulation-processes", "algorithm", 15, 16, "SIM", "Removal, growth, launch, and collision processes update the field and estimate annual collision frequency from cell co-occupancy."),
    ("alternative-results", "results", 16, 19, "RES", "Three fifteen-year simulations compare land-only, space-only, and combined removal on cumulative profits and remaining debris."),
    ("policy-scenario", "sensitivity-analysis", 19, 20, "POL", "A policy scenario maps lower debris-growth rates and a logarithmic trend to ending debris counts and a bounded regulatory recommendation."),
    ("rocket-scenario", "robustness-verification", 20, 21, "RKT", "A recyclable-rocket scenario varies lifetime and reports the limited effect of launch-cost savings on accumulated profit."),
    ("alpha-sensitivity", "sensitivity-robustness", 21, 22, "ALP", "An insurance-rate sweep connects alpha to break-even timing and accumulated profit while holding the rest of the simulation fixed."),
    ("game-theory", "model-improvement", 22, 23, "GAM", "Two 3 by 3 payoff matrices compare insurer and satellite-owner strategies before and after a policy intervention."),
    ("conclusions-improvements", "strengths-limitations", 23, 24, "CON", "The conclusion restates the commercial and policy decisions, then pairs claimed strengths with three concrete repair directions."),
    ("references", "references", 25, 26, "REF", "Eighteen references expose the business, technology, launch, debris, distribution, and policy sources while revealing archival gaps."),
]


PATTERNS = [
    "LP-B-THREAT-STAKEHOLDER-MODEL-RESULT-DECISION-BOUNDARY",
    "LP-B-ALTERNATIVES-COST-MECHANISM-TRADEOFF-HANDOFF",
    "LP-B-ASSUMPTION-REDUCTION-REPRESENTATION-ENABLED-BOUNDARY",
    "LP-B-ACCOUNTING-IDENTITY-DECOMPOSITION-SUBMODEL-HANDOFF",
    "LP-B-SYNTHETIC-FIELD-PROCESS-METRIC-INTERPRETATION",
    "LP-B-BASELINE-ALTERNATIVES-COMPARISON-RECOMMENDATION",
    "LP-B-SCENARIO-PERTURBATION-RESPONSE-SCOPE",
    "LP-B-PAYOFF-MATRIX-EQUILIBRIUM-POLICY-SHIFT",
]


MOVES = [
    ("threat-to-commercial-test", "Convert a physical hazard into named stakeholders, a measurable commercial criterion, and a bounded decision target.", "hazard -> affected parties -> opportunity test -> model objective -> boundary"),
    ("alternatives-to-cost-logic", "Classify candidate interventions by location and expose fixed cost, recurring cost, operating range, and removal capacity.", "alternative class -> mechanism -> cost profile -> capability -> limitation -> model handoff"),
    ("economic-decomposition", "Start from annual net income, decompose revenue and two costs, and route collision probability to compensation.", "income identity -> revenue -> removal cost -> collision cost -> cumulative output"),
    ("physical-reduction", "State the dimensional reduction and distributional assumptions before constructing the simulated field.", "physical system -> simplifying assumption -> 2D representation -> Gamma layers -> occupancy field"),
    ("field-process-to-probability", "Apply removal, growth, and launch operations in order, then define collision frequency from cell overlap.", "field state -> removal -> growth -> launches -> collisions -> annual probability"),
    ("alternatives-to-bounded-choice", "Compare each option on the same financial and debris metrics before selecting the combined alternative.", "shared horizon -> option outputs -> tradeoff -> combined run -> recommendation"),
    ("perturbation-to-qualified-claim", "Name the changed parameter, fixed protocol, response values, interpretation, and untested dimensions.", "parameter levels -> fixed model -> output series -> local pattern -> decision boundary"),
    ("strategies-to-policy-effect", "Define players and strategies, inspect payoffs, identify equilibria, and state how policy changes the matrix.", "players -> strategies -> payoff matrix -> equilibrium -> policy matrix -> welfare claim"),
]


EXAMPLES = [
    ("A coastal-risk study names the exposed assets before defining a measurable opportunity for a private mitigation service.", "Its recommendation remains conditional on the declared hazard and financing assumptions."),
    ("A flood-control comparison separates levees with high fixed cost from mobile barriers with high recurring deployment cost.", "Operating range and protected capacity are reported beside each option."),
    ("A maintenance business model decomposes annual income into subscriptions, intervention cost, and failure compensation.", "The failure-risk model supplies only the compensation term."),
    ("A three-dimensional contamination plume is reduced to a cross-section only after the omitted vertical dynamics are listed.", "The fitted radial family is labeled a representation rather than measured truth."),
    ("A synthetic warehouse grid applies removals, new arrivals, and inspections before counting item-slot conflicts.", "Seeds, repetitions, and occupancy calibration are stated with the estimate."),
    ("Three transport plans are compared over the same horizon on cost and unmet demand.", "The combined plan is recommended only where both metrics improve under the common scenario."),
    ("A pricing analysis varies one commission rate while freezing demand, cost, and discount assumptions.", "It reports local break-even movement without claiming global robustness."),
    ("A regulator changes one payoff matrix by imposing a verified safety standard.", "The equilibrium shift is checked from best responses and kept separate from a broad welfare proof."),
]


PROFILE_DETAILS = {
    "abstract": ("Compress threat, three-model architecture, principal results, recommendation, and caveat without hiding evidence strength.", ["hazard", "firm role", "economic model", "collision model", "policy model", "result", "boundary"], ["context", "system setup", "model sequence", "results", "decision", "limitation"]),
    "executive-summary": ("Expand each alternative and sensitivity result while preserving the bridge from model output to final commercial and policy action.", ["problem", "assumed firm", "models", "alternatives", "metrics", "scenario", "recommendation"], ["stakes", "approach", "land result", "space result", "combined result", "sensitivity", "decision"]),
    "contents-title": ("Make the full analytical route inspectable before details and expose where results, sensitivity, game theory, and limitations occur.", ["section", "input", "operation", "output", "handoff"], ["context", "methods", "notation", "models", "results", "scenarios", "policy", "evaluation"]),
    "introduction": ("Turn the physical threat into a four-element opportunity definition and identify the two missing commercial elements the model must test.", ["hazard", "evidence", "need", "means", "application", "benefit", "model objective"], ["background", "stakes", "opportunity definition", "gap", "quantitative objective"]),
    "existing-methods": ("Classify interventions by deployment location and compare their mechanism, cost profile, working range, and practical weakness.", ["method", "class", "mechanism", "fixed cost", "recurring cost", "range", "limitation"], ["category", "example", "operation", "advantage", "constraint", "model handoff"]),
    "terminology-notation": ("Define financial and physical quantities before composing the profit, collision, removal, and policy models.", ["term", "symbol", "definition", "unit or domain", "producer", "consumer"], ["business terms", "probability terms", "physical terms", "symbols", "interfaces"]),
    "model-one": ("Decompose projected business performance into annual income, cumulative income, insurance revenue, removal cost, and collision compensation.", ["horizon", "income", "revenue", "removal cost", "collision probability", "utility", "cumulative profit"], ["assumptions", "identity", "revenue", "cost split", "compensation", "handoff"]),
    "model-two-framing": ("State the orbit, persistence, time, and debris-size assumptions before reducing the geometry and selecting the Gamma representation.", ["physical regime", "hazard class", "dimension", "radial density", "shape", "boundary"], ["assumptions", "3D challenge", "2D reduction", "reference figures", "distribution choice"]),
    "debris-distribution": ("Convert the Gamma representation into a layered binary occupancy field while naming the hand-set density and its interpretation.", ["grid", "cell state", "radial layers", "Gamma mass", "occupancy rate", "random placement", "output"], ["representation", "partition", "sampling", "calibration claim", "field"]),
    "simulation-processes": ("Order removal, debris growth, satellite launches, and cell-overlap counting into one annual collision-probability loop.", ["field state", "method range", "removal amount", "growth law", "launch count", "collision rule", "probability"], ["remove", "grow", "launch", "count", "normalize", "handoff"]),
    "alternative-results": ("Evaluate land, space, and combined options over the same horizon with aligned profit and debris metrics.", ["alternative", "cost equation", "removal regime", "horizon", "profit path", "debris path", "decision"], ["land setup", "land result", "space setup", "space result", "combined setup", "comparison"]),
    "policy-scenario": ("Translate lower debris-growth rates into ending inventories and a policy recommendation while retaining the scenario boundary.", ["policy", "growth levels", "fixed model", "ending debris", "marginal change", "interpretation", "scope"], ["motivation", "perturbation", "outputs", "diminishing change", "decision"]),
    "rocket-scenario": ("Vary rocket lifetime, compare accumulated-profit trajectories, and explain why savings are small relative to other costs.", ["technology", "lifetime levels", "fixed alternative", "profit paths", "range", "mechanism", "boundary"], ["future capability", "reruns", "comparison", "effect size", "explanation"]),
    "alpha-sensitivity": ("Connect insurance commission levels to break-even timing and accumulated profit under fixed simulation conditions.", ["alpha", "levels", "fixed inputs", "profit path", "break-even", "marginal response", "recommendation"], ["parameter rationale", "sweep", "outputs", "threshold", "decision", "scope"]),
    "game-theory": ("Move from players and strategies through two payoff matrices to checked equilibria and the claimed policy-induced shift.", ["players", "strategies", "payoffs", "best responses", "equilibria", "policy change", "welfare claim"], ["game assumptions", "baseline matrix", "equilibria", "policy matrix", "new equilibrium", "claim"]),
    "conclusions-improvements": ("Separate supported commercial and policy conclusions from claimed strengths and specific future repairs.", ["finding", "metric", "recommendation", "strength", "limitation", "affected output", "repair"], ["commercial decision", "parameter decision", "policy decision", "strengths", "model repairs"]),
    "references": ("Expose which source supports each technology, launch series, debris profile, distribution, cost, or policy input and what remains unfrozen.", ["source", "claim", "model interface", "date", "URL", "archive status", "missing input"], ["business", "methods", "launches", "debris", "distribution", "policy", "provenance boundary"]),
}


EVIDENCE = {
    "abstract": [(1, "focus on evaluating potential commercial opportunities"), (1, "Three models are presented"), (1, "1000*1000 matrix"), (1, "insurance commission determinant shall be set")],
    "executive-summary": [(2, "private firm involved can both provide insurance services"), (2, "classified the prevailing methods"), (3, "run this model for a third time"), (3, "Further conducted sensitivity analysis")],
    "contents-title": [(4, "Strategies to Eliminating Space Debris"), (5, "A Time-Dependent Evaluation Model"), (5, "Some What If Scenarios"), (5, "A Game Theory Approach")],
    "introduction": [(6, "roughly over 500,000 pieces"), (6, "Commercial opportunity generally consists"), (6, "former two elements already exist"), (6, "time-dependent model shall be constructed")],
    "existing-methods": [(6, "classified into two categories"), (6, "Laser Broom"), (7, "Snagging and Moving"), (7, "Solar Sail")],
    "terminology-notation": [(7, "Compensation"), (8, "Cobb-Douglas utility function"), (8, "Net income generated"), (8, "Chance of collision")],
    "model-one": [(9, "projected net income is established"), (9, "N_t = R_t - C_t"), (10, "R_t = n_t times w times alpha"), (11, "C_2t = Pr(t)")],
    "model-two-framing": [(12, "uniformly distributed in low earth orbit"), (12, "middle sized debris"), (12, "smashing this spatial problem"), (13, "X Gamma alpha beta")],
    "debris-distribution": [(14, "1000*1000 1-0 matrix"), (14, "four consecutive ring-shaped layers"), (14, "random seeds to plant debris"), (14, "15% cell filled")],
    "simulation-processes": [(15, "removed randomly from this model"), (15, "linear growth model"), (16, "initially quantity of orbiting satellites is set to 110"), (16, "same cell")],
    "alternative-results": [(17, "land-based alternative"), (18, "space-based alternative"), (18, "combination of previous alternatives"), (19, "deduction of more than 2000")],
    "policy-scenario": [(19, "decreasing the iteration speed"), (20, "ending space debris is reduced"), (20, "pattern makes sense"), (20, "government regulations")],
    "rocket-scenario": [(20, "recyclable rocket can be used"), (21, "recycle time be 3, 6, 9 and 12"), (21, "difference between the maximum and minimum"), (21, "compensations liability")],
    "alpha-sensitivity": [(21, "alpha is likely to change"), (22, "alpha set to 3%"), (22, "greater or equal than 5%"), (22, "average of 7.4 billion")],
    "game-theory": [(22, "perfect information game"), (23, "three choices"), (23, "pure strategy Nash Equilibrium"), (23, "Pareto improvement")],
    "conclusions-improvements": [(23, "potential commercial opportunity does exist"), (24, "insurance commission"), (24, "three-dimensional model"), (24, "operation research on allocating resources")],
    "references": [(25, "Satellite Situation Report"), (25, "Briefing to the NASA Advisory Council"), (25, "Gamma distribution"), (26, "Space Debris Elimination")],
}


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
    q104 = q112.load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q113_language")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q113_language")
    template = base.load_template_module()
    configure(q104, base, template)

    pages = {
        page: (TEXT_DIR / f"page-{page:04d}.txt").read_text(encoding="utf-8")
        for page in range(1, PAGE_COUNT + 1)
    }
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
    expected_chapters = {chapter for _section, chapter, *_rest in CHAPTERS}
    if set(per_chapter) != expected_chapters or any(value != 4 for value in per_chapter.values()):
        raise RuntimeError(f"language saturation failed: {per_chapter}")

    for unit in language["units"]:
        ordinal = int(unit["language_unit_id"].rsplit("-", 1)[1]) - 1
        section = unit["section"].split(" / evidence move", 1)[0]
        function, slots, order = PROFILE_DETAILS[section]
        page, excerpt = EVIDENCE[section][ordinal]
        unit["page"] = page
        unit["source_excerpt"] = excerpt
        unit["function"] = function
        unit["reusable_pattern"] = " -> ".join(order)
        unit["information_order"] = order
        unit["reusable_elements"] = slots
        unit["prohibited_generalizations"] = [
            "Do not transfer debris density, orbit geometry, cost, launch count, collision rate, removal range, insurance rate, utility parameter, growth rate, rocket lifetime, payoff, or policy effect without rebuilding the receiving case.",
            "Do not turn a hand-set occupancy, unseeded simulation, shared-cell collision rule, one-factor sweep, plotted trajectory, or asserted equilibrium into empirical calibration, predictive validation, global robustness, optimality, or a welfare proof.",
        ]
        unit["features"]["quantitative_role"] = "bind annual profit, cumulative profit, cost components, Gamma occupancy, removal and growth updates, launch-cell collisions, scenario levels, payoff entries, and break-even timing to a declared decision"
        unit["features"]["transition"] = "first, meanwhile, to be precise, therefore, subsequently, inversely, further, however, thus, and admittedly connect setup, model, result, scenario, policy, and boundary"

    abstract_functions = [
        "Frame the debris threat and the commercial-opportunity objective.",
        "Define the merged insurer-remover and preview the three-model architecture.",
        "Describe the time-dependent revenue and cost decomposition.",
        "Describe the Gamma-grid collision simulation and repeated-run rationale.",
        "Describe the policy-maker game and scenario comparison.",
        "Admit sensitivity to the insurance commission and omitted time value of money.",
        "State the combined-alternative, commission, and industrial-standard recommendations.",
    ]
    introduction_functions = [
        "Establish debris scale, collision consequences, candidate technologies, and their differing costs, risks, and benefits.",
        "Turn the need to implement removal technology into the central commercial-opportunity question.",
        "Decompose a commercial opportunity into demand, means, application, and benefit.",
        "Identify application and benefit as the missing elements and commit to a time-dependent private-firm feasibility model.",
    ]
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 26 UTF-8 physical-page files were read sequentially. Original 144-DPI PNG pages remained on disk; byte-bounded JPEG proxies were reserved for a separate one-image-at-a-time visual review."
        layout["ambiguities"] = [
            "The extractor flattens subscripts, percentages, summation signs, matrix cells, payoff tables, superscripts, Greek symbols, plotted series, and page-spanning captions; G5-G6 visual review remains the fidelity authority.",
            "Physical page 1 is the required summary, pages 2-3 add an executive summary, pages 4-5 are title and contents, and pages 25-26 are references; chapter contracts preserve those separate rhetorical jobs.",
            "The source calls a hand-set 15 percent occupancy convincing, invokes the law of large numbers without a replicate protocol, and labels selected scenario sweeps sensitivity; these evidence-strength conflicts are retained for G7.",
            "No executable code, seed list, random-run count, Gamma calibration file, raw output array, payoff derivation workbook, or archived source dataset is bundled with the paper.",
        ]
        if layout["chapter"] == "abstract":
            layout["paragraph_count"] = len(abstract_functions)
            layout["paragraph_functions"] = abstract_functions
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = len(introduction_functions)
            layout["paragraph_functions"] = introduction_functions

    STAGE.mkdir(parents=True)
    output = STAGE / "language.json"
    output.write_text(json.dumps(language, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
