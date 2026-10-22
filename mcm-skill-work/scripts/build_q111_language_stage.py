from __future__ import annotations

"""Create Queue 111 G1-G3 language evidence without entering model work."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-39173-b8260835"
SHORT = "39173"
SHA = "b82608352dbbe043cd7092dabcaea179ff110677e0a4598d1f78ad33f956b813"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 32
TEXT_DIR = ROOT / "artifacts/papers" / PAPER_ID / "text/pages"
STAGE = ROOT / "tmp/q111-language-stage-v2"

CHAPTERS = [
    ("abstract", "abstract", 1, 1, "ABS", "The abstract moves from sparse transoceanic evidence through containment, detection, updating, neighborhood search, assumptions, and bounded transfer."),
    ("contents", "title", 2, 2, "TTL", "The contents exposes the complete containment-to-detection-to-search-to-example route and keeps assumptions, sensitivity, limitations, communication, and code visible."),
    ("introduction", "introduction", 2, 3, "INT", "The introduction contrasts radar gaps and two prior-information regimes before stating a sparse-prior, time-efficient search objective."),
    ("model-overview", "problem-analysis", 3, 3, "PRB", "The model overview decomposes the missing-flight decision into containment, detection, and continuously updated location priorities."),
    ("containment-construction", "model-establishment", 3, 6, "CNT", "A casualty-distance prior, radar horizon, glide translation, cross-track dispersion, and independence assumption construct a joint impact-location density."),
    ("search-region-discretization", "algorithm", 6, 8, "DSC", "A three-standard-deviation cross-track bound and half-hour along-track partition create an N by 6 POC grid through regional integration."),
    ("latitude-longitude-transformation", "data-preprocessing", 8, 9, "CRD", "Local cell corners are rotated, scaled, and translated into operational latitude-longitude coordinates."),
    ("probability-of-detection", "model-improvement", 10, 10, "DET", "A Koopman-style exponential combines search area, sweep width, search effort, altitude, instrumentation, conditions, and aircraft count."),
    ("poc-update-and-neighborhood-search", "robustness-verification", 11, 11, "UPD", "Nondetection reduces the searched cell, redistributes mass, and selects the highest adjacent updated POC to limit deadhead travel."),
    ("methodology-assumptions", "assumptions", 12, 12, "ASM", "Nine physical and operational assumptions define the linear, stationary, detectable, constant-speed search regime."),
    ("sensitivity-analysis", "sensitivity-robustness", 12, 15, "SEN", "Parameter sweeps connect glide, deviation, altitude, detection range, conditions, and search-plane count to POC, POD, and feasibility."),
    ("strengths-and-weaknesses", "strengths-limitations", 15, 16, "SWL", "The evaluation attributes transfer and efficiency to specific mechanisms while naming geometric over-allocation and omitted currents."),
    ("flight-abcd-working-example", "results", 16, 23, "EXM", "A Boston-to-Lisbon Boeing case instantiates every interface from casualty density through coordinates and adjacency comparison."),
    ("conclusion", "conclusion", 23, 23, "CON", "The conclusion converts the example and sensitivity findings into a resource-aware neighborhood-search recommendation and a currents extension."),
    ("press-conference-summary", "memo", 23, 24, "MEM", "The public summary translates last contact, glide, POC, POD, neighborhood updating, revisit logic, and restrictions into nontechnical order."),
    ("references", "references", 25, 25, "REF", "Six references expose the glide, search-theory, radar, missing-aircraft, and incident-context sources used by the paper."),
    ("appendices-a-through-d", "appendix", 25, 32, "APP", "Probability integration, coordinate spreadsheets, POC initialization, adjacency and nonadjacency loops, and printed paths expose the computational handoff."),
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
    ("evidence-gap-to-search-objective", "State the observation gap, contrast available priors, and define the bounded search decision that the model must support.", "gap -> contrasting cases -> missing state -> decision target -> scope"),
    ("state-to-containment", "Transform last contact and aircraft physics into a probability field while keeping every distributional assumption visible.", "last contact -> casualty prior -> glide -> cross-track uncertainty -> joint field"),
    ("field-to-operational-grid", "Partition a continuous field into timed search cells and map their boundaries into coordinates crews can use.", "field -> bounds -> cells -> probability integration -> coordinates"),
    ("sensor-to-detection", "Separate containment from detection and tie detection to sweep geometry, effort, resources, and operating conditions.", "cell area -> sensor reach -> sweep width -> effort -> POD -> feasibility"),
    ("nondetection-to-next-action", "Update the searched cell after a miss, preserve total mass, and use local priority to select an efficient next action.", "prior POC -> search -> miss -> update -> neighborhood comparison -> next cell"),
    ("parameter-to-response", "Vary a named physical or resource parameter, trace the response through POC or POD, and state its operational consequence.", "parameter -> affected term -> response -> feasibility or resource decision -> boundary"),
    ("mechanism-to-evaluation", "Attribute each strength or weakness to the exact model mechanism and identify the affected transfer or repair.", "mechanism -> benefit or defect -> consequence -> applicability -> repair"),
    ("technical-to-public-loop", "Translate the mathematical chain into last-contact evidence, search action, miss feedback, revisiting, and bounded public commitment.", "audience context -> evidence -> operation -> feedback -> continued action -> restriction"),
]

EXAMPLES = [
    ("A remote-vessel response begins with the last reliable position and states which observation channels disappear offshore.", "The recommendation remains conditional on the stated reporting interval and environmental evidence."),
    ("A failure-time prior is translated by reachable distance before lateral uncertainty is introduced.", "The receiving case must re-estimate both the support and the deviation law."),
    ("A continuous hazard field is divided into cells whose traversal time matches the available patrol speed.", "Cell corners are then converted into the coordinate system used by the operating team."),
    ("Detection probability combines sensor reach, altitude, weather effectiveness, swept distance, and the number of synchronized assets.", "A feasibility condition is checked before the probability is used for deployment."),
    ("A missed inspection reduces the searched cell's retained mass and changes nearby action priorities.", "The next location is chosen under an explicit travel-efficiency rule rather than by probability alone."),
    ("A resource sweep reports which term changes, how the response curve moves, and where the operation becomes infeasible.", "The paper distinguishes useful sensitivity from evidence of broad robustness."),
    ("A model's adaptive updating is credited as a strength while its stationary-debris assumption is recorded as a transfer limit.", "A current-aware drift layer is proposed as a separate repair rather than implied to exist."),
    ("A public briefing explains prediction, detection, missed-search feedback, and possible revisits in chronological order.", "It retains the straight-path and observability restrictions instead of promising universal recovery."),
]

PROFILE_DETAILS = {
    "abstract": ("Compress the complete evidence-to-search route and close with assumptions, sensitivity, reusable mechanisms, and scope.", ["observation gap", "last-contact input", "containment model", "detection model", "updating rule", "search decision", "boundary"], ["gap", "containment", "detection", "update", "search", "transfer"]),
    "title": ("Make the source route inspectable before technical detail, including positive model stages, evaluation, public communication, and executable appendices.", ["section", "analytical purpose", "input", "output", "handoff"], ["context", "model", "evaluation", "example", "decision", "communication", "code"]),
    "introduction": ("Contrast observation and prior-information regimes, then state the sparse-prior and time-efficiency objective.", ["historical scope", "radar gap", "communication trigger", "contrasting cases", "prior scarcity", "search objective"], ["gap", "case contrast", "unmet need", "objective"]),
    "problem-analysis": ("Decompose the operational question into containment, detection, resource use, and iterative location priority.", ["flight state", "containment", "detection", "resource criterion", "updated priority"], ["state", "subproblems", "integration target"]),
    "model-establishment": ("Convert last contact into a joint impact-location density through source-ordered physical and probabilistic interfaces.", ["last contact", "casualty distance", "radar horizon", "glide translation", "cross-track spread", "joint support"], ["prior", "physics", "lateral uncertainty", "joint field"]),
    "algorithm": ("Turn the continuous joint density into an N by 6 matrix whose cells have timed search meaning and integrated POC.", ["joint field", "three-sigma bound", "half-hour length", "cell index", "regional integral", "POC list"], ["bound", "partition", "integrate", "assign"]),
    "data-preprocessing": ("Transform local cell bounds into latitude-longitude corners through explicit orientation, scaling, translation, and a determinant check.", ["local cell", "corner matrix", "flight vector", "rotation", "scale", "translation", "check"], ["local coordinates", "orientation", "transform", "operational coordinates"]),
    "model-improvement": ("Build POD from cell area, effective sensor reach, altitude, condition factor, swept distance, and synchronized search effort.", ["cell area", "detection distance", "condition factor", "altitude", "sweep width", "effort", "POD"], ["Koopman baseline", "geometry", "resources", "probability", "feasibility"]),
    "robustness-verification": ("Connect nondetection to a mass-preserving POC update and a local next-cell rule that reduces nonproductive travel.", ["searched cell", "POD", "retained mass", "redistributed mass", "adjacent differences", "next cell"], ["miss", "update", "local comparison", "action"]),
    "assumptions": ("Group physical, motion, debris, detectability, and fleet equivalence assumptions as the operating contract for every later result.", ["domain", "assumption", "enabled calculation", "affected output", "excluded regime"], ["geometry", "flight", "debris", "detection", "resources", "scope"]),
    "sensitivity-robustness": ("Trace parameter changes through named POC, POD, and feasibility terms before interpreting operational consequences.", ["parameter", "fixed quantities", "affected term", "curve direction", "decision consequence", "valid range"], ["distribution response", "detection response", "resource response", "feasibility", "scope"]),
    "strengths-limitations": ("Attribute positive transfer and efficiency to mechanisms, then isolate geometric allocation and current-drift omissions for repair.", ["mechanism", "benefit", "evidence", "limitation", "impact", "future repair"], ["distribution", "coordinates", "detection", "updating", "boundary"]),
    "results": ("Instantiate every model interface with one declared route, aircraft, fleet, cell matrix, path output, and coordinate calculation.", ["scenario", "parameter", "equation instance", "intermediate result", "algorithm output", "comparison", "coordinate handoff"], ["inputs", "containment", "detection", "path", "comparison", "coordinates"]),
    "conclusion": ("Reconnect parameter sensitivity and adjacency efficiency to a resource-aware recommendation while naming the unmodeled current extension.", ["modeled result", "resource effect", "search mechanism", "recommendation", "limitation", "extension"], ["result", "resource decision", "recommendation", "future work"]),
    "memo": ("Translate last-contact evidence, glide-based containment, POD, neighborhood updating, revisits, and restrictions for a public audience.", ["audience context", "observable input", "plain-language mechanism", "search action", "feedback", "restriction"], ["problem", "prediction", "detection", "iteration", "boundary"]),
    "references": ("Expose the source roles behind glide physics, search theory, radar range, missing-aircraft context, and incident comparisons.", ["source", "claim supported", "model interface", "access detail", "unfrozen dependency"], ["citation", "use", "provenance boundary"]),
    "appendix": ("Expose implementation inputs, integration loops, coordinate tables, POC matrices, update loops, tie handling, and printed action sequences.", ["parameter setup", "data structure", "loop condition", "update", "selection", "output", "missing execution detail"], ["inputs", "calculation", "algorithm", "output", "reproducibility boundary"]),
}

EVIDENCE = {
    "abstract": [(1, "most probable locations of a missing transoceanic flight"), (1, "quadratic distance to casualty probability density function"), (1, "redistributes probabilities if the search plane is not found"), (1, "neighborhood-based, continuously-updating search mechanism")],
    "title": [(2, "Constructing Probabilities of Containment"), (2, "The POC-Updating Algorithm"), (2, "Working Example: Flight ABCD"), (2, "Appendix D")],
    "introduction": [(2, "Lost transoceanic flights are among the hardest flights to locate"), (3, "available prior information"), (3, "Malaysian Flight 370 contained little prior information"), (3, "time-efficiency is prioritized")],
    "problem-analysis": [(3, "starts at some location A"), (3, "probabilities of containment"), (3, "probabilities of detecting the plane"), (3, "continuously updating probabilities")],
    "model-establishment": [(3, "how far the plane most likely travels after a signal is lost"), (4, "distance to casualty"), (4, "YI = YC + Gh"), (6, "joint probability density function")],
    "algorithm": [(6, "divided into distinct regions"), (7, "bounded on both sides by three standard deviations"), (7, "half an hour sweeping a length"), (8, "list of probability values")],
    "data-preprocessing": [(8, "bounds of each region in latitude and longitude"), (9, "build a 2 x m matrix"), (9, "verify that det(R) = 1"), (9, "CL = rho RC + y0")],
    "model-improvement": [(10, "POD = 1 - e-coverage"), (10, "effective sweep width"), (10, "effort is said to be ds n"), (10, "POD is uniform among all regions")],
    "robustness-verification": [(11, "probability that the lost plane in region q went undetected"), (11, "probability lost"), (11, "minimize flight between nonadjacent regions"), (11, "highest adjacent POC")],
    "assumptions": [(12, "linear path from point A to point B"), (12, "does not explode in the sky"), (12, "no forces (eg. currents)"), (12, "same instrumentation")],
    "sensitivity-robustness": [(12, "impacts of changing parameters"), (13, "POD rapidly decreases from one to zero"), (14, "lowest possible altitude"), (15, "square root of a negative number")],
    "strengths-limitations": [(15, "quadratic probability density function rather than"), (16, "constantly updating algorithm"), (16, "slightly over-allocated"), (16, "lack of consideration of currents")],
    "results": [(17, "Flight ABCD from Boston, MA to Lisbon Portugal"), (18, "discretized into 36 subregion"), (20, "POD = 0.677831"), (22, "more back-and-forth movement")],
    "conclusion": [(23, "valid, time-efficient search plan"), (23, "number of search planes drastically increases"), (23, "neighborhood-based search plan"), (23, "incorporate the impacts of currents")],
    "memo": [(23, "narrows the search region"), (24, "probabilities will tell searchers"), (24, "adding more search parties"), (24, "possibility of revisiting certain areas")],
    "references": [(25, "Glide Angle"), (25, "Principles of Search Theory"), (25, "Technologies behind the Search"), (25, "Search Theory: A Mathematical Theory")],
    "appendix": [(25, "Mathematica Code for Probability Generation"), (27, "Set up parameters and define POC matrix"), (28, "highest or one of the highest initial POC regions"), (30, "without the requirement of adjacency")],
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
    q104 = load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q111_language")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q111_language")
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
            "Do not transfer a flight route, last-contact state, casualty prior, glide ratio, deviation angle, radar horizon, sensor range, weather factor, fleet size, cell geometry, POC, POD, or search order without rebuilding the receiving incident.",
            "Do not turn a source assumption, one worked example, greedy neighborhood path, sensitivity curve, or simulated probability into field validation, global optimality, or a universal recovery guarantee.",
        ]
        unit["features"]["quantitative_role"] = "bind last contact, casualty distance, glide, deviation, cell geometry, coordinates, sweep width, detection, updating, resources, sensitivity, and search order to a declared operational handoff"
        unit["features"]["transition"] = "because, therefore, next, after, given, assuming, thus, however, first, finally, and essentially connect state construction, discretization, coordinates, detection, updating, comparison, and decision"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 32 UTF-8 physical-page files were read sequentially, including a second bounded reread of pages 8-20 after an earlier display truncation. Four byte-bounded overview JPEG proxies covered pages 1-32 and four focused proxies reconciled formulas, coordinate notation, updating, and sensitivity plots."
        layout["ambiguities"] = [
            "The extractor flattens piecewise braces, roots, exponents, subscripts, Greek symbols, matrices, tables, code lines, and figure labels; bounded visual review remains the fidelity authority for G5-G6.",
            "Physical page 2 contains both the contents and the first Introduction paragraph; page 23 contains the conclusion, the start of the press summary, and a coordinate table from the working example.",
            "Appendix headings and prose conflict over adjacency in places, and long Mathematica lines are visibly clipped by the page layout; those source boundaries are preserved for G7 rather than silently repaired.",
            "No official 2015 problem-statement manifest row was available, so the task is reconstructed only from the paper's own abstract, introduction, model overview, example, and public summary.",
        ]
        if layout["chapter"] == "abstract":
            layout["paragraph_count"] = 3
            layout["paragraph_functions"] = [
                "Construct containment from last contact, casualty distance, glide, lateral deviation, discretization, and POC.",
                "Construct detection and the miss-driven neighborhood search, then name the Flight ABCD demonstration.",
                "State assumptions, parameter sensitivity, transferable plane inputs, and the main distribution/update strengths.",
            ]
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = 3
            layout["paragraph_functions"] = [
                "Establish the offshore radar gap and communication-loss trigger.",
                "Contrast Air France 447's informative priors with MH370's sparse priors and delayed evidence.",
                "Define the sparse-prior, possible-deviation, signal-less, time-efficient search objective.",
            ]
    STAGE.mkdir(parents=True)
    output = STAGE / "language.json"
    output.write_text(json.dumps(language, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
