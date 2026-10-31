from __future__ import annotations

"""Create Queue 109 G1-G3 language evidence without entering model work."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-36178-d0225ad0"
SHORT = "36178"
SHA = "d0225ad0b9c2d2dcdb91f20526f5bed617d1c221aff50ab700ad9cf85b1df9ff"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 20
TEXT_DIR = ROOT / "artifacts/papers" / PAPER_ID / "text/pages"
STAGE = ROOT / "tmp/q109-language-stage-v4"

CHAPTERS = [
    ("summary", "abstract", 1, 1, "ABS", "The summary moves from the missing-aircraft decision to a bounded location field, daily drift update, conditional algorithm choice, and time-to-find estimate."),
    ("contents", "title", 2, 3, "TTL", "The contents makes a route from assumptions and components through search geometry, comparison, sensitivity, model analysis, conclusion, and a stakeholder press communication explicit."),
    ("introduction", "introduction", 4, 4, "INT", "The introduction frames a time-critical maritime search, then decomposes it into initial location estimation, adaptable search, and current-informed recovery."),
    ("assumptions-and-justifications", "assumptions", 4, 4, "ASM", "Nine operational and physical simplifications are paired with mechanisms, unavailable data, or stated scope limits before calculations begin."),
    ("parameters", "notation", 4, 5, "PAR", "Aircraft state, search-plane capacity, time, weather, visibility, and current parameters are connected to the decisions they constrain."),
    ("problem-hypotheses", "problem-analysis", 5, 5, "HYP", "The paper splits the incident into splash-down prediction and search, rejects inefficient paths, and promotes adaptable straight-line sweeps."),
    ("model-components-through-drift", "model-establishment", 5, 9, "MOD", "The source-heading map covers Statement of Model, Components, generic downed and search planes, current drift, reverse tracing, and the geometric splash-down construction."),
    ("discrete-drift-and-detection-inputs", "data-preprocessing", 9, 10, "DAT", "A discrete current grid, markers, daily displacement, and area/search inputs prepare a changing polygon for detection and route calculations."),
    ("detection-and-parallel-baseline", "algorithm", 10, 11, "ALG", "POD, effective sweep width, searchleg geometry, range-based aircraft assignment, and swept-area computation define the baseline algorithm."),
    ("diagonal-and-optimized-search", "model-improvement", 12, 13, "OPT", "Diagonal and capacity-aware parallel paths explain their distinct coverage geometry, turn costs, re-use of aircraft, and area formulas."),
    ("main-equation-backtracking-and-comparison", "robustness-verification", 13, 15, "VER", "The main detection-to-days relation, reverse tracking, real-world comparison, and scenario results test whether the route remains operationally useful."),
    ("sensitivity-analysis", "sensitivity-analysis", 15, 16, "SEN", "A declared baseline is varied one parameter at a time to report local altitude, wind, aircraft-count, and visibility response patterns."),
    ("strengths-and-weaknesses", "strengths-limitations", 16, 17, "SWK", "The source balances low-input adaptability and dynamic drift against rectangular over-search, local-current dependence, survivor behavior, and missing glide-state detail."),
    ("future-improvements", "future-improvements", 17, 17, "FUT", "Future work names concrete current-data, loss-mode, method-comparison, map-visualization, and deployment-input extensions."),
    ("conclusion", "conclusion", 17, 17, "CON", "The conclusion reconnects bounding area, probability-guided daily coverage, current drift, conditional path choice, and the operational uncertainty boundary."),
    ("references", "references", 18, 18, "REF", "References expose aviation, search-and-rescue, convex-hull, current, and aircraft dependencies while leaving executable data and scenario artifacts absent."),
    ("press-communication", "memo", 19, 20, "MEM", "The press communication translates the technical route into incident inputs, bounding area, rectangular path choice, debris evidence, and iterative operational action."),
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
    ("incident-to-route", "State the incident decision, reconstructible inputs, location/drift route, search choice, and bounded outcome in that order.", "incident -> inputs -> route -> operation -> boundary"),
    ("assumption-contract", "Pair a simplification with the physical or operational mechanism, justification, enabled calculation, and excluded regime.", "entity -> assumption -> justification -> enabled operation -> boundary"),
    ("parameter-to-operation", "Name a parameter, define its decision role, connect it to a calculation, and identify the downstream search action.", "parameter -> role -> calculation -> handoff"),
    ("uncertainty-to-bound", "Turn an uncertainty source into a conservative geometric bound before path selection.", "uncertainty -> physical constraint -> bounded region -> algorithm input"),
    ("path-comparison", "Connect feasible path geometry, swept area, detection objective, scenario response, and conditional recommendation.", "constraints -> path -> coverage -> detection -> decision boundary"),
    ("scenario-to-decision", "Change a declared operating condition, rerun the same mechanism, report the response, and delimit the recommendation.", "scenario -> changed input -> rerun -> result -> scope"),
    ("strength-limit-repair", "Preserve an operational strength while naming the mechanism, a precise limit, and the concrete repair direction.", "strength -> mechanism -> limitation -> repair"),
    ("audience-translation", "Translate a technical route into stakeholder inputs, next actions, evidence feedback, and iterative revision.", "audience need -> input -> operation -> evidence -> iteration"),
]

EXAMPLES = [
    ("A maritime response begins with last contact, aircraft state, and weather before defining a conservative location field.", "The route remains conditional on the data quality and operational search limits."),
    ("An assumption identifies the neglected mechanism and explains which calculation becomes tractable because of it.", "The deployment record states the circumstances in which the simplification must be replaced."),
    ("A search-plane parameter is defined before its effect on sweep width and daily coverage is calculated.", "The next section identifies which routing decision receives that calculation."),
    ("Uncertain heading and turn capability are transformed into a reachable region rather than reduced to a point estimate.", "Wind expansion is bounded by the stated data rather than treated as an exact crash location."),
    ("Two route geometries are compared through effective coverage and probability of detection before a field recommendation is made.", "The recommendation retains aircraft count, area size, and weather as decision conditions."),
    ("A poor-visibility scenario reruns the common search calculation and reports a slower completion result.", "That response is not transferred to a different observation regime without recalibration."),
    ("A strengths section links low-input adaptability to its dynamic-region mechanism while admitting a missing global-current input.", "A future version adds the missing data interface rather than concealing the scope limit."),
    ("A public communication lists the facts needed to initiate a search and explains how debris evidence revises the next search area.", "It does not promise a precise discovery time outside the model's stated conditions."),
]

PROFILE_DETAILS = {
    "abstract": ("Compress a missing-aircraft decision into bounded location, moving debris, adaptable search methods, scenario evidence, and a conditional time-to-find claim.", ["incident", "location inputs", "drift", "algorithm set", "scenario", "outcome"], ["incident", "location bound", "drift", "search", "scenario result", "scope"]),
    "title": ("Use the contents as an executable route from assumptions and components through algorithms, testing, reflection, and communication.", ["section", "purpose", "input", "output"], ["route", "scope", "handoff"]),
    "introduction": ("Move from the high-stakes incident to the three linked tasks of location estimation, adaptable search, and current-informed recovery.", ["incident", "stake", "task", "method", "handoff"], ["context", "need", "task route", "model purpose"]),
    "assumptions": ("Make every physical and operational simplification explicit with an enabling reason and a stated exclusion.", ["entity", "assumption", "reason", "calculation", "limit"], ["entity", "constraint", "justification", "operation", "boundary"]),
    "notation": ("Define operational parameters through their decision role before formulas consume them.", ["parameter", "meaning", "unit or role", "consumer"], ["definition", "role", "calculation handoff"]),
    "problem-analysis": ("Decompose the incident into location and search subproblems, eliminate unadaptable candidates, and motivate the route family.", ["problem", "subproblem", "candidate", "criterion", "selection"], ["decomposition", "screen", "candidate route", "rationale"]),
    "model-establishment": ("Turn aircraft state, current data, operational capacity, and search geometry into an ordered model interface.", ["input", "mechanism", "intermediate", "output", "next model"], ["inputs", "mechanism", "computed state", "handoff"]),
    "algorithm": ("Specify the path inputs, coverage calculation, detection criterion, update action, and return value in operational order.", ["inputs", "path", "coverage", "criterion", "output"], ["inputs", "algorithm", "metric", "result", "handoff"]),
    "model-improvement": ("Introduce an alternative path through the baseline limitation, altered geometry, resource use, and conditional tradeoff.", ["baseline", "limitation", "alternative", "geometry", "tradeoff"], ["baseline", "repair", "calculation", "comparison", "boundary"]),
    "results": ("Separate comparison context, scenario outputs, mechanism explanation, and conditional operational selection.", ["baseline", "scenario", "metric", "result", "decision"], ["comparison", "scenario", "result", "interpretation", "recommendation"]),
    "sensitivity-analysis": ("Declare a baseline, perturb one parameter, report the observed response, and identify its local interpretation.", ["baseline", "parameter", "perturbation", "response", "limit"], ["baseline", "change", "rerun", "response", "scope"]),
    "strengths-limitations": ("Connect a concrete strength to its enabling mechanism before stating a distinct limit and targeted future repair.", ["strength", "mechanism", "limitation", "impact", "repair"], ["strength", "mechanism", "boundary", "extension"]),
    "conclusion": ("Reconnect the full decision route and preserve the uncertainty that keeps its recommendations conditional.", ["route step", "model output", "condition", "decision", "boundary"], ["route recap", "result", "operation", "scope"]),
    "references": ("Frame external sources by the physical, operational, numerical, or data dependency they support, including missing reproducibility artifacts.", ["source", "role", "dependency", "absence"], ["citation", "use", "provenance boundary"]),
    "memo": ("Translate the model into stakeholder facts, daily action, found-debris feedback, and iterative re-planning.", ["audience", "incident facts", "area", "path", "evidence", "next action"], ["need", "input", "operation", "feedback", "iteration"]),
}

for _chapter in ("model-overview", "downed-plane", "debris-drift", "search-aircraft", "search-area-geometry", "detection-theory"):
    PROFILE_DETAILS[_chapter] = PROFILE_DETAILS["model-establishment"]
for _chapter in ("parallel-search", "main-equation-backtracking"):
    PROFILE_DETAILS[_chapter] = PROFILE_DETAILS["algorithm"]
PROFILE_DETAILS["data-preprocessing"] = PROFILE_DETAILS["model-establishment"]
PROFILE_DETAILS["robustness-verification"] = PROFILE_DETAILS["results"]
PROFILE_DETAILS["future-improvements"] = PROFILE_DETAILS["strengths-limitations"]

EVIDENCE = {
    "abstract": [(1, "develop a model for finding a plane that was lost over a large body of water"), (1, "last known location and heading"), (1, "search area would move from day to day, as well as change shape"), (1, "over 900 unique search scenarios")],
    "title": [(2, "Introduction to Problem"), (2, "Assumptions and Parameters"), (2, "Statement of Model"), (3, "Error/Sensitivity Analysis")],
    "introduction": [(4, "most effectively search for a lost airplane"), (4, "find lost planes in the least amount of time"), (4, "search algorithm that adapts to new information"), (4, "location of the lost plane based on ocean currents")],
    "assumptions": [(4, "make the search the most difficult"), (4, "air drag will not affect the distance a plane travels"), (4, "rely on visual search alone"), (4, "sufficient daylight for searching for only 10 hours each day")],
    "notation": [(4, "altitude, velocity, and mass of the downed plane as parameters"), (4, "wind speed at the time of the crash is also considered"), (5, "number of search planes that are available"), (5, "speed and direction of the ocean currents and the time since the crash")],
    "problem-analysis": [(5, "split into two parts: predicting where it went down, and searching that area"), (5, "modeling how far a plane can glide without power"), (5, "currents of the ocean would be moving the debris away"), (5, "straight lines as much as possible when searching an area would maximize the efficiency")],
    "model-establishment": [(5, "provides suggestions for searchers throughout the entire search process"), (5, "calculates the area in which the plane could have crashed"), (5, "provides estimates for the time required to find crash debris"), (5, "trace debris back to its original location")],
    "data-preprocessing": [(9, "placed it over a grid"), (9, "Each square in the grid was given a search marker"), (10, "search area only moves discretely overnight"), (10, "drifted by a whole day’s displacement")],
    "algorithm": [(10, "maximize the Probability of Detection"), (10, "time allotted to perform the search"), (11, "The parallel search method is the simplest search algorithm"), (11, "maximize the time spent on these segments")],
    "model-improvement": [(12, "based on the same principles as the parallel search method"), (12, "allows search planes to make much longer sweeps"), (12, "many more turns must be made"), (12, "assigning extra search planes to sweep the area again")],
    "robustness-verification": [(13, "approximate how many days it will take to complete the search"), (13, "trace the object back to its original location"), (13, "compare our model’s result to the 2009 crash of Air France flight 447"), (14, "none of our search methods are perfect for every search")],
    "sensitivity-analysis": [(15, "sensitivity analysis will be based on a median problem"), (15, "changing the input parameters affects the number of days"), (15, "changed each parameter individually"), (15, "until we had a change on both sides")],
    "strengths-limitations": [(16, "using only the altitude, speed, and last known coordinates"), (16, "more realistic search shape than just a circle or rectangle"), (17, "lack the data necessary to model ocean currents globally"), (17, "survivors floating on debris or in rafts")],
    "future-improvements": [(17, "local current data measured at the site of the last known point of contact"), (17, "more possible types of loss-of-contact"), (17, "incorporate other search methods and continue comparing them"), (17, "latitude and longitude coordinates at the corners")],
    "conclusion": [(17, "give a maximum bounding area of the plane’s location"), (17, "report the probability that debris from the crash will be found"), (17, "there is no one perfect way to search for a missing plane"), (17, "too many unknowns, too many variables")],
    "references": [(18, "United States National Search and Rescue Supplement"), (18, "A Simple Guide to Conducting Ground Search and Rescue Detection Experiments"), (18, "Convex hull"), (18, "Data Download for Ocean Surface Currents")],
    "memo": [(19, "summarized by three stages"), (19, "finding an approximate location for the site"), (19, "searching this location for evidence"), (19, "better approximation for the location of the plane")],
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
    q104 = load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q109_language")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q109_language")
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
            "Do not transfer the aircraft class, last-contact precision, glide distance, wind direction, current field, search-plane capability, local visibility, simulated days, or route ranking without reconstructing the receiving incident and deployment constraints.",
            "Do not turn a conservative bound, scenario simulation, local current field, search-theory probability, or a conditional algorithm comparison into a guarantee of finding the aircraft or a universal best method.",
        ]
        unit["features"]["quantitative_role"] = "bind aircraft state, turn geometry, area, current displacement, coverage, probability of detection, aircraft count, weather, visibility, time, scenario result, and operational decision to a declared mechanism"
        unit["features"]["transition"] = "first, once, after, however, because, based on, in addition, therefore, and otherwise connect incident state, geometric bounds, drift updates, route comparison, sensitivity, decision, and future scope"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 20 UTF-8 physical-page files were read sequentially. Four one-at-a-time bounded JPEG overview proxies covered pages 1-20; original rendered PNGs remain local coordinate authority for later formula and figure crops."
        layout["ambiguities"] = [
            "The text extractor flattens integrals, summations, superscripts, theta, arrows, piecewise branches, charts, and some hyphenation; equation fidelity remains a G5 visual-crop task.",
            "Physical pages 2-3 contain contents; physical page 18 is references; physical pages 19-20 are a separately formatted stakeholder press communication retained as a memo chapter.",
            "No official 2015 problem-statement manifest row was available, so task reconstruction is bounded to the paper's explicit restatement and summary.",
        ]
        if layout["chapter"] == "abstract":
            layout["paragraph_count"] = 4
            layout["paragraph_functions"] = [
                "State the incident and robust search objective.",
                "Bound the initial splash-down area from last-contact and flight information.",
                "Move the area with currents and use debris for reverse tracing.",
                "Compare three adaptable algorithms over scenarios and state the conditional time-to-find use.",
            ]
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = 1
            layout["paragraph_functions"] = [
                "Frame the lost-aircraft decision and enumerate the linked location, adaptable-search, and current-informed recovery tasks.",
            ]
    STAGE.mkdir(parents=True)
    output = STAGE / "language.json"
    output.write_text(json.dumps(language, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "chapters": len(language["available_chapters"]),
                "language_units": len(language["units"]),
                "output": str(output),
                "status": "pass",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
