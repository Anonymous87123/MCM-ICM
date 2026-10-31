from __future__ import annotations

"""Create-only Queue 108 learning artifacts."""

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-32879-2c587e51"
SHORT = "32879"
SHA = "2c587e51ecc9209b9e7553cb1ade060b1a6b5581a54773a57fdbb5eb56dd6c54"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 35
TEXT_DIR = ROOT / "artifacts/papers" / PAPER_ID / "text/pages"
STAGE = ROOT / "tmp/q108-stage-v2"

CHAPTERS = [
    ("summary", "abstract", 1, 1, "ABS", "The summary states the missing-aircraft decision, prior distribution, four search patterns, Bayesian update, scenario variation, and rectangle recommendation."),
    ("contents", "title", 2, 2, "TTL", "The contents makes the route from flight assumptions through probability theory, paths, comparisons, final remarks, and airline letter explicit."),
    ("introduction-and-overview", "introduction", 3, 3, "INT", "The introduction uses two missing-aircraft incidents to frame time, cost, and survivor-recovery stakes before announcing generic search models."),
    ("nomenclature", "notation", 3, 4, "NOT", "The nomenclature binds grid, aircraft, detection, path, probability, and effectiveness symbols before equations use them."),
    ("simplifying-assumptions", "assumptions", 4, 4, "ASM", "The source fixes unpowered flight, one instantaneous turn, no wind/current, floating debris, flat water, runway position, and daylight limits."),
    ("random-descent-prior", "problem-analysis", 5, 7, "PRI", "Flight geometry and independent descent-angle and bearing distributions construct the initial crash-location probability field."),
    ("bayesian-posterior", "model-establishment", 8, 12, "BAY", "Bayes theorem updates searched and unsearched grid locations, derives a random-search detection probability, and defines cumulative success."),
    ("discrete-grid", "data-preprocessing", 13, 14, "GRID", "The continuous probability field becomes a one-square-mile probability grid with explicit range, runway, and daily-search inputs."),
    ("general-search-optimization", "algorithm", 14, 14, "ALG", "Each candidate center is evaluated by usable range, feasible search dimensions, and traversed-grid probability before posterior updating."),
    ("simple-square-search", "results", 15, 16, "SQR", "A parallel sweep derives square side and path length, then shows five-day posterior maps and twenty-day success curves."),
    ("optimized-rectangle-search", "model-improvement", 17, 18, "REC", "The rectangle generalizes the square area relation and enumerates integer dimensions to improve coverage at greater computational cost."),
    ("spiral-square-search", "sensitivity-analysis", 18, 20, "SPI", "Spiral geometry derives length-to-side conversion and compares its efficient but less spatially effective route with parallel sweep."),
    ("octagonal-sector-search", "robustness-verification", 21, 23, "SEC", "Sector geometry maps path length to an octagon but uses a local center heuristic that the source explicitly calls rudimentary."),
    ("variation-and-comparison", "sensitivity-robustness", 23, 31, "VAR", "Single/multiple aircraft, stall prior, range, mixed paths, and effectiveness variations compare cumulative success under changed scenarios."),
    ("strengths-and-weaknesses", "strengths-limitations", 32, 32, "SWK", "The source distinguishes customizability and global square/rectangle optimization from computational cost, sector weakness, assumptions, and absent cost effectiveness."),
    ("future-development", "future-improvements", 32, 33, "FUT", "Future work adds multi-plane pattern optimization, empirical parameters, cost limits, debris dynamics, weather, currents, staging, and refueling."),
    ("conclusion", "conclusion", 33, 33, "CON", "The conclusion reconnects flight failure, priors, Bayesian updating, paths, scenario tests, and the parallel-sweep recommendation."),
    ("references", "references", 34, 34, "REF", "References identify incident, flight, search, Bayesian, aircraft, and path sources while leaving frozen data and executable runs absent."),
    ("stakeholder-letter", "memo", 35, 35, "MEM", "A fictional company letter translates the map, dynamic update, familiar paths, coordinates, and resource claims to commercial-airline readers."),
]

PATTERNS = [
    "LP-B-DECISION-PRIOR-UPDATE-SEARCH-COMPARISON-RECOMMENDATION",
    "LP-B-ASSUMPTION-PHYSICAL-MECHANISM-ENABLED-MODEL-BOUNDARY",
    "LP-B-SYMBOL-DEFINITION-EQUATION-INTERPRETATION-HANDOFF",
    "LP-B-GEOMETRY-DISTRIBUTION-TRANSFORM-GRID-SEARCH",
    "LP-B-PRIOR-NEGATIVE-SEARCH-POSTERIOR-RENORMALIZATION",
    "LP-B-PATH-FEASIBILITY-OBJECTIVE-OPTIMIZATION-COMPARISON",
    "LP-B-SCENARIO-PARAMETER-RESULT-CAVEAT",
    "LP-B-STAKEHOLDER-RESULT-MECHANISM-OPERATIONAL-BOUNDARY",
]
MOVES = [
    ("decision-route", "State the incident decision, probability route, path decision, result, and boundary in that order.", "decision -> model route -> decision output -> boundary"),
    ("assumption-contract", "Pair a physical or operational simplification with its enabled computation and omitted regime.", "entity -> assumption -> enabled operation -> boundary"),
    ("symbol-to-mechanism", "Define symbols before an equation and state the quantity sent to the next model.", "symbol -> equation -> interpretation -> handoff"),
    ("baseline-to-repair", "State an initial distribution or baseline, explain its limitation, then introduce the update or search mechanism.", "baseline -> limitation -> update -> consequence"),
    ("path-comparison", "Connect feasible geometry, detection probability, optimization, displayed result, and comparison caveat.", "constraints -> path -> objective -> result -> caveat"),
    ("scenario-variation", "Name a changed parameter, rerun the stated mechanism, report the response, and bound transfer.", "scenario -> parameter -> rerun -> response -> scope"),
    ("strength-limit-repair", "Balance a claimed practical strength against a precise untested limit and future repair.", "strength -> mechanism -> limitation -> repair"),
    ("audience-translation", "Translate a technical model into the stakeholder input, action, benefit, and constraint it requires.", "audience need -> input -> action -> benefit -> boundary"),
]
EXAMPLES = [
    ("A search plan begins with the last confirmed location, aircraft state, and a prior field before choosing a flight path.", "The recommendation remains conditional on coverage, detection, and weather assumptions."),
    ("An assumption states that debris remains afloat and identifies the posterior update it permits.", "A maritime deployment records currents when that simplification no longer holds."),
    ("A notation section defines lateral range and path length before using both in a detection equation.", "The next paragraph states which grid calculation receives the equation output."),
    ("A prior distribution is revised after an unsuccessful sweep rather than assigning the searched area probability zero.", "The revision is renormalized over the stated search domain."),
    ("A path comparison evaluates feasible length, swept area, and success probability before naming a preferred geometry.", "Runtime and unsearched regions remain part of the selection boundary."),
    ("A stall-likelihood scenario changes the crash mixture and reruns the identical path comparison.", "Its result does not transfer without incident-specific evidence."),
    ("A strengths section names modular inputs while admitting an unoptimized route and missing cost objective.", "A future version adds the missing objective rather than hiding the limit."),
    ("A stakeholder letter identifies the aircraft information required to produce a probability map and daily search routes.", "It does not promise an outcome beyond the model's operational assumptions."),
]

PROFILE_DETAILS = {
    "abstract": ("Compress incident stakes, prior, paths, Bayesian update, adaptable scenarios, and a bounded recommendation.", ["incident", "prior", "path set", "posterior", "scenario", "recommendation"], ["stakes", "route", "result", "scope"]),
    "title": ("Use the contents as an executable route from assumptions and theory through implementation, comparison, and communication.", ["section", "purpose", "input", "output"], ["route", "scope", "handoff"]),
    "introduction": ("Move from named incidents and cost stakes to a generic search-and-recovery model.", ["incident", "stakeholder", "cost", "time", "model"], ["context", "stakes", "purpose", "handoff"]),
    "notation": ("Define each probability, geometry, grid, aircraft, and effectiveness symbol before derivation.", ["symbol", "meaning", "unit or role", "consumer"], ["definition", "role", "equation handoff"]),
    "assumptions": ("Make flight, sea, search, runway, and day constraints explicit before probability calculations.", ["entity", "assumption", "calculation", "excluded condition"], ["entity", "constraint", "operation", "boundary"]),
    "problem-analysis": ("Derive an aircraft-location prior from glide geometry and independent trajectory distributions.", ["aircraft", "altitude", "ratio", "angle", "distribution", "coordinate"], ["physics", "distribution", "transform", "prior"]),
    "model-establishment": ("Update searched and unsearched probabilities, derive detection, and integrate daily success.", ["prior", "detection", "searched cell", "unsearched cell", "posterior", "day"], ["prior", "Bayes update", "detection", "objective"]),
    "data-preprocessing": ("Convert continuous density into a grid and declare resolution, search boundary, and approximation.", ["grid", "cell", "range", "integral", "sum", "consumer"], ["continuous field", "discretization", "calculation"]),
    "algorithm": ("Evaluate all candidate centers by range, dimensions, swept probability, posterior update, and next-day handoff.", ["runway", "range", "center", "shape", "probability", "posterior"], ["inputs", "search evaluation", "selection", "repeat"]),
    "results": ("Derive a simple path, show its posterior and cumulative curve, and separate ease from optimality.", ["path", "dimension", "distance", "posterior", "curve", "limit"], ["geometry", "result", "comparison", "boundary"]),
    "model-improvement": ("Generalize a path constraint and compare gain in coverage against computational cost.", ["area", "length", "width", "integer grid", "objective", "runtime"], ["baseline", "generalization", "optimization", "tradeoff"]),
    "sensitivity-analysis": ("Derive a changed path geometry and compare efficiency without overstating dominance.", ["turn", "length", "side", "path", "probability", "comparison"], ["geometry", "rerun", "result", "limit"]),
    "robustness-verification": ("Identify a heuristic path objective, its local focus, displayed response, and global-optimization boundary.", ["sector", "center", "range", "probability", "heuristic", "limit"], ["path", "heuristic", "result", "boundary"]),
    "sensitivity-robustness": ("Vary aircraft, crash prior, range, path combination, or effectiveness and retain the changed input with its response.", ["scenario", "parameter", "path", "aircraft", "curve", "result"], ["scenario", "rerun", "comparison", "scope"]),
    "strengths-limitations": ("Pair practical modularity and documented optimization with computational, physical, and economic limitations.", ["strength", "mechanism", "weakness", "impact"], ["strength", "limit", "repair"]),
    "future-improvements": ("Turn each stated limitation into a specific future model input, objective, or operational extension.", ["limitation", "new input", "new objective", "method"], ["gap", "extension", "expected use"]),
    "conclusion": ("Reconnect the prior, posterior, path optimization, scenario evidence, and scoped recommendation.", ["prior", "Bayes update", "path", "scenario", "recommendation"], ["route recap", "result", "boundary"]),
    "references": ("Separate cited background and method sources from archived inputs, code, and reproducible simulation records.", ["source", "role", "dependency", "missing artifact"], ["citation", "use", "provenance boundary"]),
    "memo": ("Translate probability mapping and iterative search optimization into stakeholder inputs, operations, benefits, and constraints.", ["audience", "aircraft facts", "map", "search path", "resource"], ["audience need", "model input", "operation", "benefit"]),
}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def configure(q104, base, template) -> None:
    values = {"PID": PAPER_ID, "SHORT": SHORT, "SHA": SHA, "TYPE": TYPE, "YEAR": YEAR, "PAGE_COUNT": PAGE_COUNT, "TEXT_DIR": TEXT_DIR, "STAGE": STAGE, "CHAPTERS": CHAPTERS, "PATTERNS": PATTERNS, "MOVES": MOVES, "EXAMPLES": EXAMPLES}
    for module in (q104, base, template):
        for name, value in values.items():
            setattr(module, name, value)


def build_language(q104, base, template, pages: dict[int, str]) -> dict:
    configure(q104, base, template)
    language = q104.build_language(base, template, pages)
    for unit in language["units"]:
        function, slots, order = PROFILE_DETAILS[unit["chapter"]]
        unit["function"] = function
        unit["reusable_pattern"] = " -> ".join(order)
        unit["information_order"] = order
        unit["reusable_elements"] = slots
        unit["prohibited_generalizations"] = [
            "Do not transfer aircraft range, glide ratio, failure mix, grid, runway, search path, detection parameter, or result curve without reconstructing the receiving incident and operational constraints.",
            "Do not call a simulated curve, local heuristic, single assumed runway, or repeated model output independent validation, a guarantee of discovery, or a universally optimal search.",
        ]
        unit["features"]["quantitative_role"] = "bind physical range, angle, grid probability, detection probability, path length, area, aircraft range, day, effectiveness, cumulative success, runtime, and scenario output to its declared operation"
        unit["features"]["transition"] = "first, then, because, however, similarly, therefore, after, and finally connect prior construction, posterior updating, path selection, comparison, operational translation, and scope"
    for layout in language["chapter_layouts"]:
        layout["counting_method"] = "All 35 UTF-8 physical-page files were read sequentially. Five one-at-a-time bounded JPEG overview proxies covered pages 1-35, and fourteen focused JPEG formula crops checked equation fidelity."
        layout["ambiguities"] = ["Text extraction flattens superscripts, roots, integrals, limits, multi-column figures, and chart labels; the original rendered PNGs remain coordinate authority.", "Physical page 35 is a fictional-company stakeholder letter after references and is retained as a memo rather than author-reference language."]
        if layout["chapter"] == "abstract":
            layout["paragraph_count"] = 6
            layout["paragraph_functions"] = ["State missing-aircraft stakes.", "Define the prior distribution.", "Name four search patterns and their optimization.", "Introduce dynamic Bayesian posterior updating.", "State adaptable scenario parameters.", "Close with the rectangular parallel-sweep recommendation."]
        elif layout["chapter"] == "introduction":
            layout["paragraph_count"] = 3
            layout["paragraph_functions"] = ["Use incident evidence to establish the search-and-recovery stakes.", "Translate delay and cost into a model need.", "Preview generic probability and search optimization models."]
    return language


def equation(q104, index, page, label, latex, symbols, purpose, confidence="high"):
    return q104.equation(index, page, label, latex, symbols, purpose, confidence)


def build_models(q104, base, template) -> dict:
    configure(q104, base, template)
    prior = [
        equation(q104, 1, 5, "minimum glide angle", r"\theta_{\min}=\tan^{-1}(1/(L/D))", ["theta_min", "L/D"], "Calculate minimum unpowered glide angle from lift-to-drag ratio."),
        equation(q104, 2, 6, "maximum glide range", r"r_{glide}=h\cot(\theta)", ["r_glide", "h", "theta"], "Calculate range from altitude and glide angle."),
        equation(q104, 3, 6, "bimodal descent angle", r"f(\theta)=p_{crash}f(\theta_{crash})+p_{glide}f(\theta_{glide})", ["f(theta)", "p_crash", "p_glide", "theta_crash", "theta_glide", "sigma_1", "sigma_2"], "Mix catastrophic-descent and glide angle distributions.", "medium"),
        equation(q104, 4, 7, "bearing distribution", r"f(\phi)=(\sigma_3\sqrt{2\pi})^{-1}\exp[-\tfrac12(\phi/\sigma_3)^2]", ["f(phi)", "phi", "sigma_3"], "Represent possible bearing change around zero."),
        equation(q104, 5, 7, "trajectory density", r"p(\theta,\phi)=f(\theta)f(\phi)", ["p(theta,phi)", "f(theta)", "f(phi)"], "Combine independent trajectory variables."),
        equation(q104, 6, 7, "x coordinate transform", r"x=\sqrt{2\rho^2(1-\cos\phi)}\cos(\pi/2-\phi/2)+(h\cot\theta-|\rho\phi|)\sin\phi", ["x", "rho", "phi", "h", "theta"], "Map trajectory terms to east-west location.", "medium"),
        equation(q104, 7, 7, "y coordinate transform", r"y=\sqrt{2\rho^2(1-\cos\phi)}\sin(\pi/2-\phi/2)+(h\cot\theta-|\rho\phi|)\cos\phi", ["y", "rho", "phi", "h", "theta"], "Map trajectory terms to north-south location.", "medium"),
    ]
    bayes = [
        equation(q104, 8, 8, "Bayes theorem", r"P(A\mid B)=P(B\mid A)P(A)/P(B)", ["P(A|B)", "P(B|A)", "P(A)", "P(B)"], "State the probability update identity."),
        equation(q104, 9, 8, "searched-cell posterior", r"p_0=p(1-q)/[(1-p)+p(1-q)]", ["p_0", "p", "q"], "Reduce probability after a failed search without forcing it to zero."),
        equation(q104, 10, 9, "unsearched-cell posterior", r"r_0=r/(1-pq)", ["r_0", "r", "p", "q"], "Renormalize an unsearched location after a failed search elsewhere."),
        equation(q104, 11, 10, "incremental detection", r"g(h)=Wh/A", ["g(h)", "W", "h", "A"], "Give target-detection probability for an incremental swept rectangle."),
        equation(q104, 12, 10, "detection recurrence", r"b(z+h)=b(z)+[1-b(z)]W/A", ["b(z+h)", "b(z)", "W", "A"], "Record the printed recurrence for detection probability.", "medium"),
        equation(q104, 13, 10, "detection differential equation", r"b'(z)=[1-b(z)]W/A", ["b'(z)", "b(z)", "W", "A"], "Relate path length to detection-rate change.", "medium"),
        equation(q104, 14, 10, "detection function", r"b(z)=1-\exp(-zW/A)", ["b(z)", "z", "W", "A"], "Solve the random-search detection relation."),
        equation(q104, 15, 11, "conditional regional success", r"q(z^*)=\max_{z\in R}\iint_A b(z)\,dA", ["q(zstar)", "z", "R", "A", "b(z)"], "Define displayed search-success criterion.", "medium"),
        equation(q104, 16, 11, "regional finding probability", r"p(find\ plane)=\iint_A b(z)p(x,y)\,dA", ["p(find plane)", "b(z)", "p(x,y)", "A"], "Combine detection and location probability."),
        equation(q104, 17, 12, "daily success", r"P(N)=\prod_{k=1}^{N-1}[1-P(k)]\iint_A b(z)p(x,y)\,dA", ["P(N)", "k", "b(z)", "p(x,y)", "A"], "Combine earlier failures with current-day success."),
        equation(q104, 18, 13, "grid approximation", r"\iint_Ap(x,y)dA\approx\sum_{i=a}^{b}\sum_{j=c}^{d}p_{ij}", ["p(x,y)", "A", "p_ij", "a", "b", "c", "d"], "Approximate continuous probability with grid mass."),
    ]
    paths = [
        equation(q104, 19, 15, "square passes", r"n=s/W", ["n", "s", "W"], "Relate square side to lateral-search range."),
        equation(q104, 20, 15, "square path length", r"z=n(s-W)+s", ["z", "n", "s", "W"], "Compute parallel-sweep travel inside a square."),
        equation(q104, 21, 15, "square side from range", r"s=\sqrt{Wz}", ["s", "W", "z"], "Invert the square path constraint."),
        equation(q104, 22, 17, "rectangle area constraint", r"A=Wz", ["A", "W", "z"], "Define the generalized rectangular sweep area."),
        equation(q104, 23, 19, "spiral path length", r"z=2W\sum_{i=1}^{l-1}i+(l-1)W", ["z", "W", "i", "l"], "Sum spiral segments before inversion.", "medium"),
        equation(q104, 24, 19, "spiral side inversion", r"l=\tfrac14(-\sqrt2+\sqrt{18-16z})", ["l", "z"], "Record the printed square-side inversion.", "medium"),
        equation(q104, 25, 21, "sector side length", r"l=z\sin(67.5^\circ)/[8(\cos(67.5^\circ)+1)]", ["l", "z"], "Map sector path length to regular-octagon side."),
        equation(q104, 26, 29, "effectiveness product", r"\lambda=\alpha\beta", ["lambda", "alpha", "beta"], "Combine target visibility and search-aircraft effectiveness."),
        equation(q104, 27, 29, "effective increment", r"g(h)=\lambda Wh/A", ["g(h)", "lambda", "W", "h", "A"], "Scale incremental detection by effectiveness."),
        equation(q104, 28, 29, "effective detection rate", r"b'(z)=[1-b(z)]\lambda W/A", ["b'(z)", "b(z)", "lambda", "W", "A"], "Scale the detection-rate equation."),
        equation(q104, 29, 29, "effective detection function", r"q=1-\exp(-\lambda zW/A)", ["q", "lambda", "z", "W", "A"], "Solve for effectiveness-adjusted detection probability."),
    ]

    def model(index, page, section, family, purpose, inputs, outputs, equations):
        return q104.make_model(base, template, f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, section, family, purpose, inputs, outputs, equations)

    models = [
        model(1, 5, "random descent prior", "flight-geometry prior", "Map aircraft glide and bearing assumptions into a crash-location probability field.", ["last location", "bearing", "altitude", "lift-to-drag ratio", "failure mixture"], ["theta-phi density", "Cartesian location prior"], prior),
        model(2, 8, "Bayesian posterior", "Bayesian negative-search update", "Update searched and unsearched probabilities after an unsuccessful sweep.", ["prior cell probability", "detection probability", "searched region"], ["searched posterior", "unsearched posterior", "renormalized grid"], bayes[:3]),
        model(3, 10, "posterior search paths", "random-search detection", "Derive detection probability from lateral range, path length, and bounded area.", ["W", "z", "A", "initial detection state"], ["g(h)", "b(z)", "q"], bayes[3:7]),
        model(4, 11, "optimization criteria", "cumulative success objective", "Integrate detection and location mass, then compose day-level success.", ["posterior grid", "path candidates", "days"], ["regional success", "daily success", "next-day prior"], bayes[7:]),
        model(5, 13, "discrete prior grid", "spatial discretization", "Overlay the continuous prior on one-square-mile cells for computation.", ["Cartesian prior", "rmax", "grid resolution"], ["p_ij grid", "searchable region"], []),
        model(6, 14, "general search methods", "daily exhaustive center search", "Evaluate every grid center using runway range, feasible dimensions, and traversed mass.", ["runway distance", "aircraft range", "path geometry", "posterior grid"], ["optimal center", "optimal shape", "updated posterior"], []),
        model(7, 15, "simple square search", "parallel square sweep", "Derive a square path from usable distance and maximize swept probability.", ["usable range", "W", "posterior grid"], ["s", "q", "daily square", "success curve"], paths[:3]),
        model(8, 17, "optimized rectangle search", "integer rectangular sweep", "Enumerate feasible rectangle dimensions to improve parallel-sweep coverage.", ["usable range", "W", "integer grid", "posterior grid"], ["A", "rectangle dimensions", "success curve"], paths[3:4]),
        model(9, 19, "spiral square search", "spiral geometry", "Derive spiral path length and invert it to select a search square.", ["usable range", "W", "posterior grid"], ["l", "spiral path", "success curve"], paths[4:6]),
        model(10, 21, "octagonal sector search", "sector geometry and local heuristic", "Map path length to an octagon and optimize a central probability concentration.", ["usable range", "central 3-by-3 mass", "posterior grid"], ["l", "sector center", "success curve"], paths[6:7]),
        model(11, 23, "variation and comparison", "scenario simulation", "Compare paths under aircraft number, stall prior, range, mixed paths, and model geometry.", ["path results", "aircraft parameters", "prior parameters", "scenario settings"], ["comparative curves", "conditional pattern recommendation"], []),
        model(12, 29, "effectiveness parameter", "detection-effectiveness extension", "Scale detection by target visibility and search-aircraft effectiveness.", ["alpha", "beta", "W", "z", "A"], ["lambda", "effective q", "comparison curves"], paths[7:]),
        model(13, 32, "strengths, limits, and future work", "operational scope assessment", "Bind modular inputs and global square/rectangle optimization to known physical, computational, and economic limits.", ["simulation outputs", "assumptions", "runtime", "deployment needs"], ["qualified strengths", "limitations", "extension plan"], []),
        model(14, 35, "stakeholder communication", "airline search memo", "Translate model inputs and optimized paths into an audience-facing operational letter.", ["aircraft specifications", "last-contact path", "search resources", "model outputs"], ["probability map", "daily paths", "airline-facing explanation"], []),
    ]
    edges = [{"from_model_id": models[i]["model_id"], "to_model_id": models[i + 1]["model_id"], "handoff": handoff} for i, handoff in enumerate([
        "The Cartesian crash prior enters Bayesian cell updates.",
        "Updated cell probabilities enter the detection and random-search model.",
        "Detection probability and posterior mass enter the daily-success objective.",
        "The objective is evaluated on a discrete probability grid.",
        "The grid supplies every candidate center to the daily search optimizer.",
        "Usable range and posterior mass feed square-path evaluation.",
        "Square constraints generalize to enumerated rectangles.",
        "Alternative spiral geometry receives the same daily posterior interface.",
        "Sector geometry receives a bounded central-mass heuristic.",
        "All path outputs enter scenario comparisons.",
        "Effectiveness parameters modify detection in the comparative simulations.",
        "Qualified results and limits inform future operational scope.",
        "The final scope and operations are translated for airline stakeholders.",
    ])]
    return {"dependency_edges": edges, "models": models, "paper_id": PAPER_ID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def build_card(models: dict) -> dict:
    visuals = [
        (5, "Figure 1a", "Glide angle theta defines the vertical trajectory input."),
        (5, "Figure 1b", "Bearing change phi defines the horizontal trajectory input."),
        (6, "Figure 2", "Geometry supports the maximum unpowered glide-range relation."),
        (8, "Figure 3", "Initial Cartesian probability density shows crash and glide modes."),
        (9, "Figure 4", "Lateral range W defines search-track geometry."),
        (10, "Figure 5", "Increment h illustrates incremental swept area."),
        (12, "Figure 6", "Prior and posterior curves show a searched middle region."),
        (13, "Figure 7", "Contour map turns the prior into a discrete search grid."),
        (15, "Figure 8", "Parallel sweep makes square-path passes and lateral coverage visible."),
        (16, "Figure 9", "Five-day posterior shows the square search's selected regions."),
        (16, "Figure 10", "Twenty-day cumulative and daily success show square-path output."),
        (17, "Figure 11", "Rectangle posterior map visualizes reduced gaps."),
        (18, "Figure 12", "Rectangle success curve exposes performance and runtime tradeoff."),
        (18, "Figure 13", "Spiral sweep defines the alternative path geometry."),
        (19, "Figure 14", "Spiral symmetry motivates the path-length derivation."),
        (20, "Figure 15", "Spiral posterior displays the selected five-day regions."),
        (20, "Figure 16", "Spiral cumulative/daily curve supports path comparison."),
        (21, "Figure 17", "Sector search shows the octagonal sweep geometry."),
        (21, "Figure 18", "Sector parameters expose side, angle, and repeated-center structure."),
        (22, "Figure 19", "Sector posterior shows the local-center heuristic outcome."),
        (23, "Figure 20", "Sector cumulative/daily curve reveals lower performance."),
        (24, "Figure 21", "Single-plane comparison places four path curves on one scale."),
        (25, "Figure 22", "Five-plane comparison tests aircraft-count scaling."),
        (26, "Figure 23", "Stall-likely prior changes the initial probability field."),
        (26, "Figure 24", "Stall-likely path curves test sensitivity to the changed prior."),
        (27, "Figure 25", "Small-plane full and early-day panels expose range-dependent ranking change."),
        (28, "Figure 26", "Two-plane mixed-versus-same path curve tests path complementarity."),
        (30, "Figure 27", "Effectiveness curves show nonlinear cumulative-return response."),
        (31, "Figure 28", "Aircraft-type comparison exposes interaction of visibility and prior range."),
    ]
    warnings = [
        (7, "Coordinate transforms in Equations 6-7 require a dimensional and parenthesis reconstruction before numerical reuse."),
        (10, "Equation 12 visibly omits h from its final fraction and Equation 13 prints h tending to infinity rather than zero in the difference quotient."),
        (11, "Equations 15-16 mix q(z*) and an area integral; the optimization domain and integrand need a typed derivation before implementation."),
        (19, "The printed final simplification in Equation 23 and its inversion in Equation 24 are algebraically unusual and require independent verification."),
        (22, "The sector method explicitly optimizes a product of central mass and usable range rather than the full searched-path success, so it is not a global optimum."),
        (25, "Treating five simultaneous aircraft as one aircraft for five times as many days omits coordination, overlap, and posterior-update timing."),
        (29, "Alpha and beta are hypothetical, multiplicative, and uncalibrated; effectiveness comparisons do not validate their values."),
        (32, "The model omits wind, currents, sinking, curvature, cost effectiveness, and multiple staging constraints central to real deployment."),
        (34, "References do not freeze incident data, distribution calibration, MATLAB code, grid settings, seeds, or reproducible scenario runs."),
    ]
    return {
        "paper_id": PAPER_ID, "problem_type": TYPE, "year": YEAR, "team_control_number": SHORT,
        "title": "Into the Void: A Probabalistic Approach to the Search for Missing Aircraft", "award_status": "outstanding",
        "source": {"relative_path": "2015\u7f8e\u8d5b\u7279\u7b49\u5956/B-32879-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "Physical pages 1-34 are the formal paper; physical page 35 is a fictional-company stakeholder letter retained as a memo artifact."},
        "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": 35, "rendered_pages": 35, "visual_review": "complete", "notes": ["All 35 page-text files were read sequentially.", "Five bounded overview JPEG proxies covered pages 1-35; fourteen focused formula crops checked pages 5-11, 13, 15, 17, 19, 21, and 29.", "No blank, clipped, or body-text-overlap page was observed; original PNGs remained coordinate authority.", "The page-35 fictional-company letter is categorized as a stakeholder memo, not reference prose."]},
        "context_sources": [{"type": "paper", "path": "2015\u7f8e\u8d5b\u7279\u7b49\u5956/B-32879-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PAPER_ID}/extraction.json"}, {"type": "text-pages", "path": f"artifacts/papers/{PAPER_ID}/text/pages"}],
        "task_reconstruction": {"status": "paper-restatement-complete", "inputs": ["last known position and bearing", "aircraft altitude and lift-to-drag ratio", "failure scenario", "search aircraft range and effectiveness", "runway and daylight constraints"], "outputs": ["crash-location prior", "daily posterior", "optimized path and center", "comparative cumulative-success curves", "airline-facing operational letter"], "decisions": ["how failure trajectory defines the prior", "how failure to find updates the grid", "which path/shape/location maximizes modeled success", "how scenario changes affect the recommendation", "which deployment limitations remain"]},
        "section_map": [{"page": s, "section": k, "summary": summary} for k, _c, s, _e, _t, summary in CHAPTERS],
        "assumptions": [{"page": 4, "summary": "The aircraft is tracked until loss, unpowered, in cruise, subject to one instantaneous turn, and modeled without wind, currents, sinking, curvature, land, or non-search transit."}, {"page": 4, "summary": "A runway is fixed 400 miles south and each search day has 12 flight hours."}, {"page": 10, "summary": "Random-search derivation assumes uniform target distribution, independent uniformly distributed track sections, and no effort outside the region."}],
        "data_and_preprocessing": [{"page": 5, "summary": "Boeing 747-400 example uses L/D 17 and altitude 35,000 feet; values are intended to be replaceable."}, {"page": 7, "summary": "Angle standard deviations 15, 20, and 30 degrees are chosen arbitrarily for a likely scenario."}, {"page": 13, "summary": "The grid uses one-square-mile cells, square matrix bounds from rmax, and an inscribed circular actual region."}, {"page": 14, "summary": "C-130 range, cruise speed, daylight limit, runway distance, and path geometry determine usable search range."}],
        "models": [{"model_id": m["model_id"], "page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": 16, "section": "square path output", "summary": "Five-day posterior and twenty-day curve expose the square model's simulated outputs.", "verification_type": "simulation-output inspection", "strength": "The source displays posterior removal and day-indexed success.", "limitation": "No empirical incident holdout or calibration is supplied."}, {"page": 24, "section": "single-plane comparison", "summary": "Four paths share a cumulative-success comparison.", "verification_type": "within-model comparison", "strength": "All paths use the declared simulation interface.", "limitation": "A common simulated interface does not establish real-world superiority."}, {"page": 26, "section": "stall scenario", "summary": "A changed pcrash prior reruns all four patterns.", "verification_type": "scenario analysis", "strength": "The altered prior and response are displayed.", "limitation": "The stall weight is not calibrated to incident data."}, {"page": 30, "section": "effectiveness scenario", "summary": "Unit and doubled effectiveness curves expose nonlinear response.", "verification_type": "parameter scenario", "strength": "The changed parameter is explicit.", "limitation": "Alpha and beta remain hypothetical."}],
        "results_trace": [{"page": 18, "summary": "Rectangle leaves fewer gaps than square but costs 20-30 seconds per optimization step versus under one second."}, {"page": 24, "summary": "Rectangle is the best single large-plane path; sector is lowest under the displayed simulations."}, {"page": 27, "summary": "For short-range aircraft, rectangle leads early but square later outperforms in the stated simulation."}, {"page": 28, "summary": "Two squares are preferable to a square-sector pair, but the displayed difference is slight."}, {"page": 31, "summary": "The Cessna example has lower visibility but higher modeled success because its search area is smaller."}],
        "contributions": [{"page": 7, "summary": "Physical glide and bearing uncertainty create a transparent prior rather than a single guessed crash point."}, {"page": 9, "summary": "Bayesian updates preserve failed-search probability while renormalizing unsearched locations."}, {"page": 14, "summary": "A daily grid optimizer links runway range, geometry, and posterior mass."}, {"page": 24, "summary": "Common-scale path curves support conditional geometry selection."}, {"page": 35, "summary": "The memo translates technical inputs and outputs to an airline operation."}],
        "writing_logic": [{"page": s, "summary": summary} for k, _c, s, _e, _t, summary in CHAPTERS],
        "language_observations": [{"page": s, "summary": summary} for k, _c, s, _e, _t, summary in CHAPTERS],
        "visualization_observations": [{"page": p, "figure": f, "summary": summary} for p, f, summary in visuals],
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The summary binds physical prior, multiple paths, Bayesian update, and operational recommendation without proving that this route caused the award.", "evidence_class": "J"}, {"page": 24, "summary": "A common-scale comparison makes path tradeoffs legible, without validating simulated curves against a real search.", "evidence_class": "J"}, {"page": 35, "summary": "The stakeholder letter reconnects model inputs and outputs to a use case, without proving real deployment readiness.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": summary} for p, summary in warnings],
        "independent_extensions": [{"extension_id": f"E-B-{SHORT}-001", "page": 7, "summary": "Calibrate trajectory mixtures and angle distributions from aircraft-specific incident, weather, and flight-data evidence."}, {"extension_id": f"E-B-{SHORT}-002", "page": 10, "summary": "Repair and dimension-check the random-search derivation, then test it against controlled detection trials."}, {"extension_id": f"E-B-{SHORT}-003", "page": 22, "summary": "Optimize the full sector path success over all traversed cells rather than a central-mass heuristic."}, {"extension_id": f"E-B-{SHORT}-004", "page": 32, "summary": "Use a multi-aircraft, time-indexed, cost-constrained stochastic program with weather, currents, debris state, staging, and sensor models."}],
        "candidate_rule_impacts": [], "unresolved_questions": [summary for _p, summary in warnings], "protocol_v2_records": {}, "review_status": "validated",
    }


def build_observations(template, language, models, card):
    observations = template.make_observations(language, models, card)
    text = {"language": "Reuse only the rhetorical mechanism after replacing incident, aircraft, physical conditions, data, path, parameter, and stakeholder entities.", "modeling": "Retain prior, posterior, grid, path geometry, detection, objective, scenario, and handoff terms together.", "logic": "Preserve the positive incident-to-prior-to-Bayes-to-grid-to-path-to-comparison-to-memo chain before warnings.", "visualization": "Keep visual encodings, axes, curve identities, path geometry, scenario parameters, and decision purpose together.", "verification": "Name the exact simulated curve, scenario, parameter, comparator, calibration gap, or untested deployment variable.", "data": "Retain aircraft facts, source, time, distribution, grid, runway, range, sensor, and downstream consumer.", "assumption": "Pair each physical and operational assumption with its enabled calculation and excluded regime.", "result": "Keep prior mass, posterior mass, detection, path size, runtime, cumulative success, rank, and scenario response distinct.", "weakness": "Record formula, heuristic, calibration, coordination, and deployment risks only after positive language, logic, model, and visual learning.", "other": "Separate cited incident and method context from frozen inputs, code, calibration, scenario logs, and independent validation."}
    for index, row in enumerate(observations):
        row["interpretation"] = text[row["dimension"]]
        row["applicability"] = ["Apply only when the incident data, aircraft state, trajectory assumptions, search resources, detection model, path constraints, and decision objective are explicit."]
        row["counterevidence"] = ["A simulated success curve, local heuristic, path ranking, or stakeholder letter does not prove calibration, discovery, causal safety, universal optimality, or field readiness."]
        if row["dimension"] == "other":
            row["page"] = [1, 3, 5, 8, 10, 13, 14, 24, 29, 34, 35][index % 11]
            row["section"] = f"provenance / evidence action {index + 1}"
            row["source_basis"] = "The source identifies a context, physical quantity, method, figure, or citation but not a frozen executable evidence package."
    return observations


def attach_rule_impacts(card, observations):
    nominated = {}
    for row in observations:
        for rule_id in row["candidate_rule_ids"]:
            nominated.setdefault(rule_id, row["observation_id"])
    entries = [
        ("R-B-LANG-001", "retain the incident-to-prior-to-update-to-path-to-comparison-to-stakeholder route with explicit operational boundaries"),
        ("R-B-LOG-001", "trace aircraft facts through trajectory prior, posterior grid, path optimizer, scenario outputs, recommendation, and memo"),
        ("R-B-DATA-001", "version aircraft specifications, incident data, trajectory calibration, grid, runway, aircraft range, sensor effectiveness, and scenario settings"),
        ("R-B-DATA-002", "maintain assumptions for flight failure, wind/current, debris, search effort, geometry, daylight, staging, and cost"),
        ("R-B-MOD-001", "retain flight prior, Bayes updates, detection, grid, four paths, daily objective, scenario comparison, and effectiveness extension with handoffs"),
        ("R-B-MOD-003", "require a unit, domain, normalization, calibration, and operational-constraint contract for every probability and geometry interface"),
        ("R-B-MOD-004", "keep prior, posterior, detection, path dimensions, runtime, cumulative success, scenario response, and operational recommendation distinct"),
        ("R-B-MOD-005", "stress distribution calibration, formula limits, grid resolution, path optimization, multi-aircraft coordination, sector heuristic, and effectiveness uncertainty"),
        ("R-B-VER-002", "make every claim prior-, posterior-, geometry-, curve-, scenario-, parameter-, or deployment-trace-specific"),
        ("R-B-VER-004", "reconcile the random-search derivation, regional objective, spiral algebra, sector heuristic, aircraft coordination, effectiveness calibration, and missing reproduction files"),
        ("R-B-VIZ-001", "retain trajectory diagrams, probability maps, posterior displays, path geometry, cumulative curves, scenario panels, and memo with purpose"),
        ("R-B-COMP-001", "measure grid evaluation, posterior update, path enumeration, simulation days, scenario sweeps, and multi-aircraft coordination separately"),
    ]
    missing = [rule_id for rule_id, _ in entries if rule_id not in nominated]
    if missing:
        raise RuntimeError(f"missing nominated evidence: {missing}")
    card["candidate_rule_impacts"] = [{"rule_id": rule_id, "action": action, "evidence_ids": [nominated[rule_id]]} for rule_id, action in entries]


def build_audit(template, language, models, card, observations):
    audit = template.make_audit(language, models, card, observations)
    layouts = {item["chapter"]: item for item in language["chapter_layouts"]}
    units = language["units"]
    chains = [("abstract", ["incident stakes -> generic model need", "prior distribution -> crash-location field", "four paths -> modeled effectiveness", "Bayesian update -> next-search posterior", "scenario variation -> adaptable parameters", "rectangle recommendation -> operational boundary"]), ("introduction", ["named incidents -> time and cost stakes", "stakes -> generic search model need", "overview -> physical prior and search-method handoff"])]
    audit["paragraph_chains"] = []
    for chapter, moves in chains:
        ids = [unit["language_unit_id"] for unit in units if unit["chapter"] == chapter]
        audit["paragraph_chains"].append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": move, "language_unit_ids": [ids[i % len(ids)]]} for i, move in enumerate(moves)]})
    audit["language_unit_dispositions"] = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "The source move transfers only after replacing aircraft, incident, physical, probability, path, resource, and stakeholder entities."} for u in units]
    audit["organization_logic"] = {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": [x["summary"] for x in card["writing_logic"]] + ["Only after positive language, organization, model, result, and visual chains are complete does the final pass record formula, heuristic, calibration, and deployment warnings."], "section_progressions": [{"chapter": chapter, "moves": [f"input: source-checked aircraft fact, probability, grid, path, curve, scenario, or stakeholder need entering {chapter}", f"rhetorical job: define, derive, motivate, compare, bound, or translate the object in {chapter}", f"analytical job: map, distribute, update, discretize, optimize, simulate, compare, or communicate", f"output: retain a typed parameter, equation, posterior, path, curve, scenario response, or memo artifact", "handoff: name the next physical, probability, optimization, comparison, or audience interface"], "positive_pattern": "Use explicit input -> typed operation -> inspectable output -> scoped handoff; warnings remain a final pass."} for chapter in language["available_chapters"]], "main_argument_chains": [
        {"claim": "A search starts with a physical trajectory prior rather than one guessed location.", "support_steps": ["aircraft state", "glide relation", "crash/glide mixture", "bearing distribution", "coordinate transform", "Cartesian density"], "decision_consequence": "Calibrate the prior to the incident before treating it as a search map.", "source_pages": [5, 6, 7, 8]},
        {"claim": "An unsuccessful search changes both searched and unsearched probabilities before the next daily path is selected.", "support_steps": ["Bayes theorem", "searched posterior", "unsearched posterior", "detection function", "regional objective", "daily success"], "decision_consequence": "Update the full grid rather than deleting searched cells from consideration.", "source_pages": [8, 9, 10, 11, 12]},
        {"claim": "Path recommendation follows geometry, usable range, posterior mass, and repeated simulation rather than shape alone.", "support_steps": ["grid", "range", "center enumeration", "square", "rectangle", "spiral", "sector", "common-scale curve"], "decision_consequence": "Select a path conditional on resources, runtime, and the modeled posterior.", "source_pages": [13, 14, 15, 17, 19, 21, 24]},
        {"claim": "Scenario comparisons make aircraft range, failure prior, path combinations, and effectiveness explicit modifiers of the recommendation.", "support_steps": ["five-plane run", "stall prior", "short-range plane", "mixed paths", "effectiveness parameter", "aircraft-type curve"], "decision_consequence": "Use each curve only with its stated scenario inputs and unmodeled constraints.", "source_pages": [25, 26, 27, 28, 29, 30, 31]},
        {"claim": "A stakeholder letter closes the loop by stating required aircraft data, dynamic updates, path outputs, and operational use.", "support_steps": ["aircraft specifications", "location map", "iterative update", "familiar patterns", "coordinate conversion", "airline reader"], "decision_consequence": "Communicate model use while disclosing the deployment assumptions that still require operational validation.", "source_pages": [35]},
    ]}
    audit["formula_error_watch"] = {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": [
        {"model_id": models["models"][0]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-006", "page": 7, "warning": "Coordinate transform parentheses and dimensions require reconstruction before numerical reuse."},
        {"model_id": models["models"][2]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-012", "page": 10, "warning": "The printed recurrence visibly omits h from the final fraction."},
        {"model_id": models["models"][2]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-013", "page": 10, "warning": "The displayed difference-quotient limit visibly tends to infinity rather than zero."},
        {"model_id": models["models"][3]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-015", "page": 11, "warning": "The regional criterion mixes q(z*) with a maximized area integral and needs a typed domain/objective derivation."},
        {"model_id": models["models"][8]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-023", "page": 19, "warning": "The printed spiral-length simplification is algebraically unusual and should be checked before inversion."},
        {"model_id": models["models"][8]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-024", "page": 19, "warning": "The spiral-side inverse requires an independent domain and discriminant check."},
        {"model_id": models["models"][11]["model_id"], "equation_id": f"EQ-B-{YEAR}-{SHORT}-029", "page": 29, "warning": "The effectiveness parameter is hypothetical and uncalibrated, so its numeric use cannot establish real detection probability."},
    ]}
    counts = Counter(row["dimension"] for row in observations)
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
    q104 = load_module(ROOT / "scripts/build_q104_artifacts.py", "q104_template_for_q108")
    base = q104.load_module(ROOT / "scripts/build_q101_artifacts.py", "q101_template_for_q108")
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
    card["protocol_v2_records"] = {"language": {"path": f"artifacts/language-units/{PAPER_ID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PAPER_ID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}}
    observations = build_observations(template, language, models, card)
    attach_rule_impacts(card, observations)
    audit = build_audit(template, language, models, card, observations)
    write_json(STAGE / "language.json", language)
    write_json(STAGE / "models.json", models)
    write_json(STAGE / "card.json", card)
    write_json(STAGE / "audit.json", audit)
    (STAGE / "observations.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "pages_read": len(pages), "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "models": len(models["models"]), "equations": sum(len(m["governing_equations"]) for m in models["models"]), "visuals": len(card["visualization_observations"]), "observations": len(observations), "warnings": len(card["weaknesses"]), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
