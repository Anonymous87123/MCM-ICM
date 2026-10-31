from __future__ import annotations

"""Create Queue 112 G1-G3 language evidence without entering model work."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-40612-8bcdc1a7"
SHORT = "40612"
SHA = "8bcdc1a780f3e08a678c1f450512da6656300cbb3c537ac5e97b29824f07322f"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 34
TEXT_DIR = ROOT / "artifacts/papers" / PAPER_ID / "text/pages"
STAGE = ROOT / "tmp/q112-language-stage-v1"


CHAPTERS = [
    ("abstract", "abstract", 1, 2, "ABS", "The summary previews collision-derived target count, drift simulation, sequential Bayesian surface and underwater search, resource allocation, two incident applications, sensitivity, and limitations."),
    ("contents", "title", 3, 5, "TTL", "The contents exposes a source-ordered route from physical target generation through priors, posterior recursion, allocation, applications, sensitivity, public communication, and references."),
    ("introduction", "introduction", 6, 6, "INT", "The introduction turns two delayed maritime recoveries and sparse ocean information into seven explicit modeling and decision tasks."),
    ("base-analysis", "problem-analysis", 7, 8, "PRB", "The base analysis separates crashed-aircraft properties from search-aircraft capabilities before any probability model is built."),
    ("assumptions", "assumptions", 8, 9, "ASM", "Five assumption groups define collision, drift, surface search, underwater search, and aircraft-allocation regimes."),
    ("variables", "notation", 10, 10, "NOT", "The notation table distinguishes drifter counts, crash mechanics, spatial states, three probability roles, and platform-specific detection probabilities."),
    ("collision-model", "model-establishment", 10, 12, "COL", "A volume-based maximum and impulse-threshold disintegration function produce the modeled number of searchable drifters."),
    ("simulation-module", "data-preprocessing", 12, 12, "SIM", "A current-driven random-motion module is proposed as a synthetic scenario generator and search-model correction environment."),
    ("search-overview", "problem-restatement", 13, 14, "OVR", "A Bayesian prediction-update explanation and flowchart separate surface and underwater phases while preserving their probability handoffs."),
    ("surface-search", "model-improvement", 14, 18, "SUR", "Flight-dynamics evidence and reverse drift are mixed into a surface prior, then detection outcomes update it by Bayes' rule."),
    ("underwater-search", "robustness-verification", 19, 20, "UND", "The surface posterior and flight prior form an underwater prior that is recursively updated after unsuccessful phases."),
    ("allocation", "algorithm", 21, 22, "ALL", "Quicksort ranks cells and aircraft, while a stated branch-and-bound objective seeks higher cumulative detection probability."),
    ("applications", "results", 22, 27, "APP", "AF447 supplies a retrospective location comparison and MH370 supplies a conditional prediction under no-detection assumptions."),
    ("sensitivity", "sensitivity-robustness", 27, 30, "SEN", "Hand-selected grids vary drifter count, aircraft count and type, and three mixture weights against one cumulative detection metric."),
    ("strengths-weaknesses", "strengths-limitations", 31, 31, "SWL", "The evaluation claims accuracy, efficiency, applicability, and robustness while admitting computation, assumptions, and parameter-identification gaps."),
    ("press-conference", "memo", 32, 33, "MEM", "The public paper translates current-aware search, Bayesian updating, allocation, rapid response, and continued search into a chronological narrative."),
    ("references", "references", 33, 34, "REF", "Nineteen references expose incident reports, search theory, current data, algorithms, and web sources, with uneven archival specificity."),
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
    ("incident-gap-to-system-objective", "State the delayed-recovery evidence, observation limits, and the physical, probabilistic, allocation, and communication decisions the system must support.", "incident history -> evidence gap -> phased tasks -> decision target -> boundary"),
    ("aircraft-properties-to-drifter-count", "Separate capacity from crash severity and identify which quantities are assumed, measured, or left for calibration.", "aircraft type -> maximum count -> collision regime -> disintegration degree -> actual count"),
    ("heterogeneous-evidence-to-prior", "Build each prior from named evidence streams and expose every mixture weight and uncertainty judgment.", "last-known state -> accident distance -> reverse drift -> weights -> surface prior"),
    ("observation-to-posterior", "Define the cell state, outcome likelihood, normalization domain, and recursive handoff after a search report.", "prior -> assigned search -> detection report -> likelihood -> posterior -> next phase"),
    ("ranked-resources-to-allocation", "Rank cells and platforms, then state the objective and missing constraints rather than calling the pairing optimal by inspection.", "cell PDF -> platform capability -> ranking -> candidate assignment -> objective -> allocation"),
    ("case-to-bounded-comparison", "Trace each application from accessible information through substitutions and outputs to an explicitly limited comparator.", "case evidence -> model input -> computation -> spatial output -> comparator -> validity boundary"),
    ("perturbation-to-qualified-sensitivity", "Name changed and fixed factors, report the response grid, and separate local direction or weight stability from model validation.", "factor -> fixed protocol -> output values -> pattern -> supported scope -> untested dimensions"),
    ("technical-to-public-sequence", "Translate probability and allocation into observable inputs, actions, feedback, and stopping conditions without upgrading evidence strength.", "public context -> evidence -> surface action -> underwater update -> allocation -> continued search -> caveat"),
]


EXAMPLES = [
    ("A wildfire response plan begins with the last verified perimeter and identifies which sensing channels are delayed or absent.", "Its recommendation remains conditional on the stated wind field, revisit interval, and detection model."),
    ("A warehouse-damage model separates the maximum number of releasable items from the fraction released by impact severity.", "Thresholds are labeled assumed until collision-test data identify them."),
    ("A coastal-spill prior combines vessel telemetry with reverse advection from sampled slick locations.", "The mixture weights and interpolation window are reported as scenario choices rather than measured truth."),
    ("A failed inspection updates every candidate compartment through a normalized observation likelihood.", "The next round consumes the posterior while preserving the inspected region's nonzero residual probability."),
    ("Emergency crews and zones are ranked under explicit capability and priority scores before a constrained assignment is solved.", "The report states capacity, travel, overlap, and stopping constraints next to the objective."),
    ("A retrospective flood map is compared with one observed inundation point and a declared coverage area.", "The comparison is described as a case trace, not independent predictive validation."),
    ("A scheduling study varies fleet size and one priority weight while recording all fixed budgets and seeds.", "Stable ranking over three settings is reported as local weight stability only."),
    ("A public briefing explains forecast, field observation, missed-detection feedback, and redeployment in chronological order.", "It retains uncertainty and the conditions that can suspend the operation."),
]


PROFILE_DETAILS = {
    "abstract": ("Compress the full target-generation-to-search route and retain application, sensitivity, and limitation boundaries.", ["incident gap", "collision output", "drift prior", "Bayesian update", "allocation", "case result", "boundary"], ["context", "physical model", "search model", "allocation", "applications", "scope"]),
    "title": ("Make the complete analytical route inspectable before detail, including all surface, underwater, allocation, case, evaluation, communication, and source stages.", ["section", "purpose", "input", "operation", "output", "handoff"], ["context", "assumptions", "models", "allocation", "applications", "evaluation", "communication"]),
    "introduction": ("Use delayed recovery and sparse ocean evidence to motivate a finite list of model and decision outputs.", ["incident", "delay", "data limitation", "system need", "task list", "decision use"], ["history", "gap", "goal", "deliverables"]),
    "problem-analysis": ("Separate crashed-object attributes from search-platform capabilities and connect both to later model interfaces.", ["object type", "capacity", "material", "platform type", "speed", "range", "sensor"], ["target heterogeneity", "platform heterogeneity", "allocation implication"]),
    "assumptions": ("Group idealizations by the exact model component they enable and the real mechanisms they exclude.", ["component", "assumption", "enabled calculation", "held-fixed factor", "excluded regime"], ["collision", "drift", "surface", "underwater", "allocation"]),
    "notation": ("Define count, mechanics, state, prior, posterior, and detection symbols before they are composed.", ["symbol", "meaning", "unit or domain", "role", "source status", "consumer"], ["counts", "mechanics", "space", "probabilities", "platform likelihood"]),
    "model-establishment": ("Convert aircraft volume and collision impulse into an actual drifter count through explicit threshold and saturation behavior.", ["maximum count", "volume", "mass", "velocity", "angle", "impulse", "disintegration", "actual count"], ["capacity", "collision", "piecewise response", "count output"]),
    "data-preprocessing": ("Describe the synthetic movement environment, forcing data, stochastic term, and evidence class before using it to assess search behavior.", ["initial state", "current field", "time step", "random motion", "output trajectories", "comparison use", "missing protocol"], ["state", "forcing", "simulation", "diagnostic boundary"]),
    "problem-restatement": ("Separate the target-location state, prior, detection report, posterior, surface phase, and underwater phase before detailed formulas.", ["unknown state", "prior", "report", "likelihood", "posterior", "phase handoff"], ["Bayesian object", "prediction", "update", "surface", "underwater"]),
    "model-improvement": ("Fuse flight and reverse-drift evidence into a surface prior, then update it from search outcomes with a normalized cell likelihood.", ["flight prior", "accident distance", "reverse drift", "mixture weights", "cell", "likelihood", "posterior"], ["flight evidence", "drift evidence", "fusion", "search update"]),
    "robustness-verification": ("Carry the surface result into a recursively updated underwater search while distinguishing phase assumptions and stopping conditions.", ["surface posterior", "flight prior", "underwater weight", "search phase", "outcome", "posterior", "recursion", "stop"], ["prior handoff", "phase search", "update", "recursion"]),
    "algorithm": ("Connect ranked cells and ranked aircraft to a stated cumulative-detection objective and expose the missing optimization contract.", ["cell score", "platform score", "rank", "candidate", "objective", "constraint", "assignment"], ["sorting", "matching", "branching", "bounding", "allocation"]),
    "results": ("Trace AF447 and MH370 from case-specific evidence through substitutions and spatial outputs to bounded comparisons.", ["case", "available evidence", "assumption", "prior", "posterior", "output region", "comparator", "limitation"], ["AF447 trace", "comparison", "MH370 prior", "conditional prediction"]),
    "sensitivity-robustness": ("Report each discrete perturbation grid, fixed settings, cumulative detection output, and the exact level of stability supported.", ["factor", "levels", "fixed inputs", "metric", "values", "direction", "boundary"], ["target count", "fleet count", "fleet type", "weight sweeps", "scope"]),
    "strengths-limitations": ("Pair each claimed benefit with its evidence and each admitted limitation with the affected decision and repair need.", ["claim", "mechanism", "evidence", "counterevidence", "impact", "repair"], ["accuracy", "efficiency", "application", "robustness", "limitations"]),
    "memo": ("Translate current-informed Bayesian search and platform allocation into public chronology while preserving uncertainty and continuation rules.", ["audience context", "observable input", "plain mechanism", "search action", "feedback", "allocation", "caveat"], ["problem", "environment", "surface search", "underwater search", "allocation", "continued action"]),
    "references": ("Expose which sources support incidents, drift data, Bayesian search, algorithms, and MH370 geometry, and which dependencies remain unfrozen.", ["source", "claim", "model interface", "access date", "archival status", "missing artifact"], ["incident", "ocean data", "search theory", "algorithms", "case geometry", "provenance boundary"]),
}


EVIDENCE = {
    "abstract": [(1, "collision model to predict the number of drifters"), (1, "search model based on Bayes' theorem"), (1, "branch and bound algorithm"), (2, "computational complexity, some unrealistic assumptions")],
    "title": [(3, "Collision Model"), (3, "Surface Search Posterior PDF for Impact Location"), (4, "Allocation Model"), (4, "Sensitivity Analysis")],
    "introduction": [(6, "nearly 2 years later"), (6, "paucity of data and scant knowledge of ocean geography"), (6, "Build simulation module"), (6, "Predict the possible location of MH370 wreckage")],
    "problem-analysis": [(7, "number of drifters produced by a crash"), (7, "recovering bodies may be of more value"), (7, "search speed, voyage and search electronics and sensors"), (8, "employ distinguished aircrafts for distinct search areas")],
    "assumptions": [(8, "broken pieces are of the same size"), (8, "random motion exerted by computer"), (9, "Drifters are assumed not to move during the search phase"), (9, "sensors are assumed to give no false target detection")],
    "notation": [(10, "Maximum amount of drifters"), (10, "Degree of disintegration of the plane"), (10, "Probability of drifters at Si,j"), (10, "Detecting Probability of wreckage at Si,j")],
    "model-establishment": [(10, "N0 = alpha V"), (11, "N = beta N0"), (11, "I = mv sin theta"), (12, "beta remains to be 1 when I is large enough")],
    "data-preprocessing": [(12, "generate real scenarios of the crashed plane"), (12, "serves as the exact answer"), (12, "random motion given by computer"), (17, "Imagined Trajectories in System Simulation in Two Days")],
    "problem-restatement": [(13, "unknown variable is the target location Si,j"), (13, "posterior distribution PD(Si,j|B)"), (13, "prediction and update in sequence"), (14, "water surface search model and underwater search model")],
    "model-improvement": [(15, "F(D) = 1 - 22/(D2 + 22)"), (15, "mixture weighted by 50% for each distribution"), (16, "actual speed of the drifters is given as a quarter"), (18, "compute the posterior probability PD(Si,j|B)")],
    "robustness-verification": [(19, "mixture of 30% of the surface search posterior"), (19, "water surface searches are not conducted any more"), (19, "replace PD(Si,j), PAkD(Si,j) with PW(Si,j), PAkW(Si,j)"), (19, "recursion continues until the wreckage is pinpointed")],
    "algorithm": [(21, "Quicksort algorithm and branch-and-bound algorithm"), (21, "rank the search areas based on updated PDF"), (21, "rank the available search aircrafts"), (22, "cumulative probability of detection")],
    "results": [(23, "found about 6.5 NM from the last known position"), (23, "impact location is located in our suggestive area"), (26, "covers 80% of the highest probability paths"), (26, "assume that search planes have no detection")],
    "sensitivity-robustness": [(28, "N 200 0.619"), (28, "Number of Search Planes 2 0.340"), (29, "Weights in Computing Flight Dynamics PDF"), (30, "insensitive to the weights allocated to each prior")],
    "strengths-limitations": [(31, "precisely predict the location of AF447"), (31, "relatively shorter period of time"), (31, "weights set in prior have little impact"), (31, "Some of our parameters are hard to determine")],
    "memo": [(32, "location estimate will grow even more uncertain as time goes by"), (32, "Bayesian decentralized data fusion algorithm"), (33, "correct and update our search project"), (33, "Only when the wreckage is pinpointed")],
    "references": [(33, "Final report on the accident"), (34, "Data Download for Ocean Surface Currents"), (34, "Branch and bound algorithms-principles and examples"), (34, "Australian Transport Safety Bureau")],
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
        "PID": PAPER_ID, "SHORT": SHORT, "SHA": SHA, "TYPE": TYPE,
        "YEAR": YEAR, "PAGE_COUNT": PAGE_COUNT, "TEXT_DIR": TEXT_DIR,
        "STAGE": STAGE, "CHAPTERS": CHAPTERS, "PATTERNS": PATTERNS,
        "MOVES": MOVES, "EXAMPLES": EXAMPLES,
    }
    for module in (q104, base, template):
        for name, value in values.items():
            setattr(module, name, value)


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    q104 = load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q112_language")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q112_language")
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
            "Do not transfer incident locations, aircraft size, drifter count, crash thresholds, current fields, drift coefficients, mixture weights, detection probabilities, cell geometry, fleet capabilities, or search outcomes without rebuilding the receiving case.",
            "Do not turn a hand-set parameter, synthetic trajectory, one observed case point, three-level sensitivity grid, ranked pairing, or probability map into calibration, external validation, global optimality, broad robustness, or a recovery guarantee.",
        ]
        unit["features"]["quantitative_role"] = "bind target count, impulse thresholds, current interpolation, prior weights, cell likelihoods, posterior recursion, platform capacities, case coordinates, and sensitivity grids to a declared search decision"
        unit["features"]["transition"] = "first, then, according to, in light of, after, analogous to, moreover, however, consequently, and to sum connect physical generation, evidence fusion, observation update, allocation, application, and scope"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 34 UTF-8 physical-page files were read sequentially. Five byte-bounded overview JPEG proxies covered pages 1-34 and three focused proxies reconciled the page-12 piecewise disintegration function, page-14 probability-flow diagram, and page-18 Bayes formula."
        layout["ambiguities"] = [
            "The extractor flattens piecewise braces, Greek symbols, subscripts, summation domains, table alignment, and raster figure labels; the bounded visual review remains the fidelity authority for G5-G6.",
            "Physical pages 1-2 share the Summary, pages 3-5 are contents, and pages 33-34 combine the public paper and references; chapter contracts preserve those physical boundaries.",
            "The source calls a synthetic random-motion module an exact answer, calls one case-region overlap verification, and calls small weight sweeps robustness; those evidence-strength conflicts are preserved for G7 rather than silently upgraded or deleted.",
            "No separate code, simulation configuration, cell matrix, optimization trace, or frozen external dataset is bundled with the paper, so executable and external-validation states remain not run.",
        ]
        if layout["chapter"] == "abstract":
            layout["paragraph_count"] = 3
            layout["paragraph_functions"] = [
                "Establish the maritime-loss context and physical drifter-count input.",
                "Preview sequential Bayesian search, allocation, simulation, and two applications.",
                "State sensitivity, claimed strengths, and admitted computation, assumption, and parameter boundaries.",
            ]
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = 3
            layout["paragraph_functions"] = [
                "Use MH370 and AF447 recovery delays to establish the operational stakes.",
                "Identify sparse data and ocean geography as the observation bottleneck.",
                "Commit to collision, simulation, Bayesian search, allocation, case application, and evaluation deliverables.",
            ]
    STAGE.mkdir(parents=True)
    output = STAGE / "language.json"
    output.write_text(json.dumps(language, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
