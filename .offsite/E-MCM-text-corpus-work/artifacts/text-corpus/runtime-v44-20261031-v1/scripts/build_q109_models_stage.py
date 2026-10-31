from __future__ import annotations

"""Build the source-checked G5 model record for Queue 109 without promotion."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-36178-d0225ad0"
TYPE = "B"
YEAR = "2015"
SHORT = "36178"
SHA256 = "d0225ad0b9c2d2dcdb91f20526f5bed617d1c221aff50ab700ad9cf85b1df9ff"
STAGE = ROOT / "tmp/q109-model-stage-v1"


def variable(symbol: str, name: str, unit: str, definition: str, role: str) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": name,
        "unit": unit,
        "definition": definition,
        "role": role,
        "source_status": "explicit-defined",
    }


def equation(
    index: int,
    page: int,
    label: str | None,
    source_expression: str,
    normalized_latex: str,
    symbols: list[str],
    purpose: str,
    confidence: str = "high",
) -> dict:
    return {
        "equation_id": f"EQ-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "page": page,
        "label": label,
        "source_expression": source_expression,
        "normalized_latex": normalized_latex,
        "purpose": purpose,
        "variable_symbols": symbols,
        "source_type": "paper",
        "visual_checked": True,
        "transcription_confidence": confidence,
    }


def condition(status: str, *details: str) -> dict:
    return {"status": status, "details": list(details)}


def model(
    index: int,
    page: int,
    section: str,
    family: str,
    purpose: str,
    variables: list[dict],
    inputs: list[str],
    outputs: list[str],
    equations: list[dict],
    assumptions: list[str],
    algorithm_steps: list[str],
    validation_refs: list[str],
    limitations: list[str],
    missing_details: list[str],
    *,
    origin: str = "paper-specific",
    initial: dict | None = None,
    boundary: dict | None = None,
    parameter_method: str = "The source supplies a finite calculation procedure but not a reproducible calibration package.",
    parameter_status: str = "partial",
    feasibility: str = "partial",
    feasibility_analysis: str = "The purpose, source pages, intermediate quantities, and output handoff are inspectable, but calibration data, executable implementation, and independent field validation are not frozen.",
    software: list[str] | None = None,
    convergence: str = "The stated finite calculation terminates after the declared path, time-step, or scenario loop; no numerical tolerance or independent convergence study is reported.",
    cost: str = "Cost is governed by the number of trajectory points, grid markers, candidate paths, planes, time steps, and simulated scenarios.",
    strengths: list[str] | None = None,
    handoff_outputs: list[str] | None = None,
) -> dict:
    return {
        "model_id": f"MU-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
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
            "reason": "The displayed equations were checked against bounded page crops." if equations else "This component is specified as a finite workflow and scenario comparison without an additional displayed governing equation.",
        },
        "objectives": [
            purpose,
            "Return an explicitly bounded intermediate quantity or decision input rather than treating a simulated output as a field-validated discovery guarantee.",
        ],
        "constraints": [
            "Retain the source page, units, coordinate convention, aircraft/search-resource scope, time scale, and downstream consumer for every interface.",
            "Do not convert the source's simplified geometry, current data, detection relation, or scenario result into a globally calibrated operational claim.",
        ],
        "conditions": {
            "initial": initial or condition("present", "The source inputs and the stated initial location, search boundary, or scenario configuration must be supplied before this component runs."),
            "boundary": boundary or condition("present", "The source's geographic, daylight, weather, visibility, aircraft, and time-step limitations bound the component's use."),
            "equilibrium": condition("not-applicable", "The paper uses finite geometry, recurrence, sweep, and scenario calculations rather than an equilibrium solve."),
        },
        "parameter_estimation": {
            "status": parameter_status,
            "method": parameter_method,
            "parameters": [item["symbol"] for item in variables if item["role"] == "parameter"],
        },
        "algorithm": {
            "status": "partial",
            "steps": algorithm_steps,
            "software": software or ["The paper names Mathematica for sweep-width interpolation but supplies no source code, version, input table, seed, or executable run log for the full model."],
            "convergence_criteria": convergence,
        },
        "assumptions": assumptions,
        "identifiability_feasibility": {"status": feasibility, "analysis": feasibility_analysis},
        "handoff_outputs": handoff_outputs or outputs,
        "validation_refs": validation_refs,
        "computational_cost": cost,
        "strengths": strengths or [
            "The component declares an input-to-output interface that can be traced to a later search, probability, comparison, or stakeholder decision.",
            "Displayed equations and surrounding prose preserve the intended mechanism before the final warning pass records limitations.",
        ],
        "limitations": limitations,
        "missing_details": missing_details,
    }


def build_models() -> dict:
    trajectory = [
        equation(
            1,
            8,
            None,
            "d = altitude / tan(theta)",
            r"d=\frac{\mathit{altitude}}{\tan(\theta)}",
            ["d", "altitude", "theta"],
            "Compute the maximum unpowered glide distance used as the outer travel bound.",
        ),
        equation(
            2,
            8,
            "(1)",
            "V_x(t) = speed * cos(1.5t), r = integral_0^60 V_x(t) dt",
            r"V_x(t)=\mathit{speed}\cos(1.5t),\qquad r=\int_0^{60}V_x(t)\,dt",
            ["V_x", "t", "speed", "r"],
            "Integrate the stated horizontal velocity during a 90-degree turn to obtain turn radius.",
            "medium",
        ),
        equation(
            3,
            8,
            "(2)",
            "x(theta) = r sin(theta) + cos(theta)(d - arclength(theta,r)); y(theta) = r(-cos(theta)+1) + sin(theta)(d-arclength(theta,r))",
            r"x(\theta)=r\sin\theta+\cos\theta\,[d-\operatorname{arclength}(\theta,r)],\quad y(\theta)=r(1-\cos\theta)+\sin\theta\,[d-\operatorname{arclength}(\theta,r)]",
            ["x", "y", "theta", "r", "d", "arclength"],
            "Map each possible turn angle to a terminal horizontal coordinate before the boundary is rotated and hull-enclosed.",
            "medium",
        ),
    ]
    forward_drift = [
        equation(
            4,
            10,
            "(3)",
            "(longitude_n, latitude_n) approximately equals (longitude_0, latitude_0) plus the time-scaled current velocity terms through step n-1",
            r"(\lambda_n,\varphi_n)\approx(\lambda_0,\varphi_0)+\sum_{k=0}^{n-1}\Delta t\left(\frac{\partial\lambda_k}{\partial h},\frac{\partial\varphi_k}{\partial h}\right)",
            ["longitude_0", "latitude_0", "longitude_n", "latitude_n", "delta_t", "dlongitude_dhours", "dlatitude_dhours"],
            "Advance each search marker with the local ocean-current velocity using the source's discrete Euler description.",
            "medium",
        )
    ]
    detection = [
        equation(
            5,
            10,
            "(4)",
            "POD = 1 - exp(-t*r*n*s/a)",
            r"\mathrm{POD}=1-\exp\!\left(-\frac{t r n s}{a}\right)",
            ["POD", "t", "search_rate", "n", "sweep_width", "search_area"],
            "Convert time, searcher count, rate, effective sweep width, and area into the paper's probability-of-detection measure.",
        )
    ]
    parallel = [
        equation(
            6,
            11,
            "(5)",
            "A = sum_i (sweepwidth(plane_i) * numlegs(plane_i) * 2) * L",
            r"A_{\parallel}=\sum_{i=1}^{n}\left[\operatorname{sweepwidth}(\mathit{plane}_i)\,\operatorname{numlegs}(\mathit{plane}_i)\,2\right]L",
            ["A_parallel", "plane_i", "sweep_width_i", "numlegs_i", "n", "L"],
            "Sum the effective area swept by straight parallel legs for the available search planes.",
        )
    ]
    diagonal = [
        equation(
            7,
            12,
            "(6)",
            "SW = sum_i sweepwidth(plane_i)*numlegs(plane_i)*2; c1 = h*sin(pi/4); c2 = w*sin(pi/4); piecewise A(SW)",
            r"SW=\sum_{i=1}^{n}\operatorname{sweepwidth}(\mathit{plane}_i)\operatorname{numlegs}(\mathit{plane}_i)2,\quad c_1=h\sin\!\left(\frac{\pi}{4}\right),\quad c_2=w\sin\!\left(\frac{\pi}{4}\right),\quad A_{\diag}=\begin{cases}SW^2,&SW<c_1\\c_1^2+2c_1(SW-c_1),&c_1\le SW<c_2\\wh-(c_2+c_1-SW)^2,&c_2\le SW\le c_2+c_1\end{cases}",
            ["SW", "plane_i", "sweep_width_i", "numlegs_i", "n", "c1", "c2", "w", "h", "A_diagonal"],
            "Translate 45-degree sweeps over a rectangular region into a piecewise covered-area calculation.",
            "medium",
        )
    ]
    optimized_parallel = [
        equation(
            8,
            12,
            "(7)",
            "TL_i = L_i*P_i - P_i*(P_i-1)/2",
            r"TL_i=L_iP_i-\frac{P_i(P_i-1)}{2}",
            ["TL_i", "L_i", "P_i"],
            "Count staggered total search legs in a search block when each following plane completes one fewer leg.",
        ),
        equation(
            9,
            13,
            "(8)",
            "A_swept = sum_i (sweepwidth(block_i) * TL_i * 2) * L",
            r"A_{\mathrm{swept}}=\sum_{i=1}^{n}\left[\operatorname{sweepwidth}(\mathit{block}_i)\,TL_i\,2\right]L",
            ["A_swept", "block_i", "sweep_width_block_i", "TL_i", "n", "L"],
            "Aggregate block-level staggered legs into repeated-coverage swept area.",
        ),
    ]
    day_decision = [
        equation(
            10,
            13,
            "(9)",
            "A_search = (max width of n-gon)*(max height of n-gon); POD = 1-exp(-A_swept/A_search); sum POD > 0.95",
            r"A_{\mathrm{search}}=(\max\operatorname{width\ of\ }n\text{-gon})(\max\operatorname{height\ of\ }n\text{-gon}),\quad \mathrm{POD}=1-\exp\!\left(-\frac{A_{\mathrm{swept}}}{A_{\mathrm{search}}}\right),\quad \sum_{i=1}^{\mathrm{days}}\mathrm{POD}_i>0.95",
            ["A_search", "n_gon", "A_swept", "POD", "POD_i", "days", "threshold"],
            "Turn a bounding rectangle and accumulated swept area into the paper's daily search-completion criterion.",
            "medium",
        )
    ]
    reverse_drift = [
        equation(
            11,
            13,
            "(10)",
            "(longitude_0, latitude_0) approximately equals (longitude_f, latitude_f) minus the time-scaled current velocity terms through the preceding steps",
            r"(\lambda_0,\varphi_0)\approx(\lambda_f,\varphi_f)-\sum_{k=1}^{f}\Delta t\left(\frac{\partial\lambda_k}{\partial h},\frac{\partial\varphi_k}{\partial h}\right)",
            ["longitude_0", "latitude_0", "longitude_f", "latitude_f", "delta_t", "dlongitude_dhours", "dlatitude_dhours"],
            "Trace a found debris point backward under the same discrete current field to refine a crash-origin estimate.",
            "medium",
        )
    ]

    models = [
        model(
            1,
            8,
            "4.2 Generating the Search Area",
            "aircraft glide-turn reachability and convex hull boundary",
            "Generate an initial crash-area boundary from last contact, glide geometry, turn radius, heading, and a wind-speed perimeter expansion.",
            [
                variable("altitude", "cruising altitude", "feet in the paper examples", "Altitude of the downed aircraft used in the glide-distance calculation.", "input"),
                variable("theta", "descent angle", "angle", "Angle between the incoming trajectory and ocean surface.", "input"),
                variable("d", "maximum glide distance", "nautical miles after unit conversion", "Maximum unpowered travel distance from the last contact point.", "output"),
                variable("speed", "aircraft speed", "knots in the prose; nautical miles per second for the integration", "Speed used in the horizontal-turn calculation.", "input"),
                variable("t", "turn time", "seconds", "Time during the 90-degree horizontal turn.", "intermediate"),
                variable("V_x", "horizontal velocity", "nautical miles per second", "Horizontal component of the turning aircraft velocity.", "intermediate"),
                variable("r", "turn radius", "nautical miles", "Integrated horizontal travel during the source's 60-second turn.", "intermediate"),
                variable("x", "terminal x coordinate", "nautical miles in local geometry", "Horizontal terminal coordinate at a candidate turn angle.", "output"),
                variable("y", "terminal y coordinate", "nautical miles in local geometry", "Vertical terminal coordinate at a candidate turn angle.", "output"),
                variable("arclength", "turn arc length", "nautical miles", "Length expended by the aircraft while turning through theta with radius r.", "intermediate"),
                variable("heading", "last known heading", "degrees", "Direction used to rotate the generated shape to the last known flight orientation.", "input"),
                variable("wind_speed", "crash-time wind speed", "knots", "Magnitude used to scale normal-vector expansion of each boundary point; direction is not supplied.", "parameter"),
                variable("hull", "initial search polygon", "geospatial polygon", "Convex hull of rotated and wind-expanded reachable points.", "output"),
            ],
            ["altitude", "theta", "speed", "heading", "wind_speed"],
            ["d", "x", "y", "hull"],
            trajectory,
            [
                "A generic representative aircraft family supplies cruising altitude, speed, and mass rather than an incident-specific flight state.",
                "The source starts with horizontal motion, uses a 1.5-degree-per-second turn, and uses a 60-second 90-degree turn interval.",
                "Wind speed is known but wind direction is not; the model expands the perimeter by speed instead of applying a directional crash-time displacement.",
                "Debris splash dispersion and ocean curvature are treated as negligible for the initial geometric boundary.",
            ],
            [
                "Compute d from the supplied altitude and descent angle.",
                "Integrate the stated horizontal velocity through the fixed turn interval to obtain r.",
                "Evaluate candidate terminal coordinates over turn angles, mirror for right turns, then rotate by heading.",
                "Expand each edge point along its normal by the stated wind-speed magnitude and compute a convex hull.",
            ],
            [
                "Pages 13-14 compare the model's outer bound with the Air France 447 search radius and explicitly explain that less crash information produces a larger bound.",
                "The paper supplies no incident-specific trajectory holdout, wind-direction test, or observed crash-point error distribution.",
            ],
            [
                "The source gives no derivation or unit reconciliation for the numerical angular rate inside cos(1.5t).",
                "Mass is said to matter for crosswind resistance but is not carried into the displayed reachability equations.",
                "A convex hull deliberately encloses unreachable concavities and can enlarge the operational search area.",
            ],
            [
                "Aircraft-specific descent angle, speed at loss of power, wind direction, gusts, flight-control state, and validated glide/turn data.",
                "A declared coordinate reference, unit conversion path, boundary-point density, hull implementation, and numerical tolerances.",
            ],
            parameter_method="Representative aircraft specifications and a fixed turn-rate scenario are selected from cited sources; no incident-specific calibration or uncertainty distribution is reported.",
            cost="Linear in sampled turn angles plus the convex-hull computation; the source does not declare point density or hull implementation.",
            handoff_outputs=["hull", "d", "x", "y"],
        ),
        model(
            2,
            10,
            "4.3 Adjusting the Search Area Over Time",
            "forward Euler ocean-current drift",
            "Move every marker in the initial search area through a 24-hour current field, then rebuild a containing polygon for the next day.",
            [
                variable("longitude_0", "initial longitude", "longitude coordinate", "Longitude of a marker before the forward drift cycle.", "input"),
                variable("latitude_0", "initial latitude", "latitude coordinate", "Latitude of a marker before the forward drift cycle.", "input"),
                variable("longitude_n", "forward longitude", "longitude coordinate", "Longitude after n Euler updates.", "output"),
                variable("latitude_n", "forward latitude", "latitude coordinate", "Latitude after n Euler updates.", "output"),
                variable("delta_t", "Euler time interval", "hours", "Time interval scaling the current velocity; the prose describes a 24-hour overnight cycle.", "parameter"),
                variable("dlongitude_dhours", "longitude current velocity", "longitude units per hour", "Local longitude component of the ocean-current velocity.", "input"),
                variable("dlatitude_dhours", "latitude current velocity", "latitude units per hour", "Local latitude component of the ocean-current velocity.", "input"),
                variable("marker_set", "search markers", "geospatial point set", "Grid markers placed in the initial search area and individually advected.", "input"),
                variable("drifted_hull", "drifted search polygon", "geospatial polygon", "Convex hull surrounding all forward-drifted markers.", "output"),
            ],
            ["longitude_0", "latitude_0", "delta_t", "dlongitude_dhours", "dlatitude_dhours", "marker_set"],
            ["longitude_n", "latitude_n", "drifted_hull"],
            forward_drift,
            [
                "The current field is discretized into overnight movement rather than continuous ocean transport.",
                "Current data from the vicinity of the MH370 crash stand in for the modeled crash area.",
                "Each marker follows the local current velocity without an explicitly modeled diffusion, windage, sinking, or object-specific drag term.",
            ],
            [
                "Place the initial hull over a grid and record longitude/latitude for every retained marker.",
                "Read the local current vector, scale it by the time interval, and add the displacement to each marker.",
                "After all markers are advanced, call the convex-hull procedure to define the next day's containing polygon.",
            ],
            [
                "The source states a mechanism for daily drift but supplies no error comparison against a trajectory buoy, debris track, or observed recovery path.",
                "The paper later acknowledges the current model only covers the MH370 vicinity and lacks global current data.",
            ],
            [
                "Euler error can accumulate over repeated daily updates, particularly in spatially varying or turbulent current fields.",
                "The recomputed convex hull converts a marker cloud into an outer boundary and can mask internal density and divergence.",
            ],
            [
                "Current-grid resolution, source timestamps, interpolation rule, coordinate projection, marker spacing, integration step sensitivity, and observed-track validation.",
            ],
            parameter_method="Current speed and direction are treated as source data, but the paper does not freeze data files, spatial/temporal resolution, interpolation, or calibration.",
            cost="Proportional to marker count times time steps plus a daily convex-hull reconstruction.",
            handoff_outputs=["drifted_hull", "longitude_n", "latitude_n"],
        ),
        model(
            3,
            10,
            "4.4 Search Theory and generic search-plane inputs",
            "probability-of-detection coverage relation",
            "Estimate probability of detecting debris from allotted time, number of searchers, search rate, effective sweep width, and total area.",
            [
                variable("POD", "probability of detection", "probability", "Paper's modeled chance of detection over the stated search effort and area.", "output"),
                variable("t", "allotted search time", "time", "Time allowed for the search or elapsed search time.", "input"),
                variable("search_rate", "search rate", "distance per time", "Rate or speed at which a searcher performs the search.", "input"),
                variable("n", "number of searchers", "count", "Number of search planes or searchers deployed.", "input"),
                variable("sweep_width", "effective sweep width", "nautical miles", "Width within which a search pass has the paper's effective ability to find debris.", "parameter"),
                variable("search_area", "area to search", "square nautical miles", "Total area used as the denominator of the detection relation.", "input"),
            ],
            ["t", "search_rate", "n", "sweep_width", "search_area"],
            ["POD"],
            detection,
            [
                "The search-theory relation is used as the source definition of POD for the stated homogeneous search setting.",
                "Effective sweep width is drawn from published tables by altitude, weather, and target size, then interpolated; the source states there is no one direct formula.",
                "Visual search is assumed because small debris is considered undetectable by the stated radar or infrared methods.",
            ],
            [
                "Obtain sweep-width values for the search-plane altitude, weather, and lost-object conditions.",
                "Insert time, rate, number of planes, sweep width, and area into the POD relation.",
                "Use the resulting detection quantity to compare daily search patterns rather than as an independently calibrated field probability.",
            ],
            [
                "Sections 5.1-5.2 compare generated area/search durations and algorithm scenarios, not a measured detection-trial calibration of POD itself.",
                "The conclusion frames 95 percent as a modeled search-sufficiency target rather than evidence that debris will certainly be found.",
            ],
            [
                "The paper does not provide the interpolated sweep-width function, table values, target-detection experiment, or correlation/overlap treatment among multiple searchers.",
                "The relation treats coverage in a compact scalar form while real visibility, sea state, fatigue, sensor performance, and target drift vary spatially and temporally.",
            ],
            [
                "Sweep-width tables, interpolation procedure, aircraft/target lookup criteria, detection trials, search-path overlap, and uncertainty calibration.",
            ],
            parameter_method="Sweep width is said to be interpolated in Mathematica from National Search and Rescue Committee tables; the fitted function and inputs are not preserved.",
            software=["Mathematica is named for the sweep-width interpolation; no interpolation notebook, table extract, or version is included."],
            handoff_outputs=["POD"],
        ),
        model(
            4,
            11,
            "4.5.1 Parallel Search",
            "parallel rectangular sweep allocation",
            "Assign search planes straight paths parallel to the long edge and sum their effective swept area for the day.",
            [
                variable("plane_i", "search plane i", "aircraft instance", "One available plane with search speed, range, altitude, and sweep-width properties.", "input"),
                variable("sweep_width_i", "plane-specific sweep width", "nautical miles", "Effective sweep width assigned to plane i.", "parameter"),
                variable("numlegs_i", "completed legs", "count", "Number of full search legs plane i can complete in the day.", "intermediate"),
                variable("L", "full sweep length", "nautical miles", "Length of one full sweep across the search rectangle.", "input"),
                variable("n", "plane count", "count", "Number of planes used in the parallel search.", "input"),
                variable("A_parallel", "parallel swept area", "square nautical miles", "Total modeled effective area swept by the parallel algorithm.", "output"),
            ],
            ["plane_i", "sweep_width_i", "L", "n"],
            ["numlegs_i", "A_parallel"],
            parallel,
            [
                "Search planes fly straight along the long edge to minimize time spent turning.",
                "Each later leg consists of two search-leg straightaways and two cross segments; the first leg has one cross segment.",
                "A plane's daily completed-leg count depends on range, search speed, and remaining area within the allotted daylight period.",
            ],
            [
                "For each available plane, compute feasible full legs from range, speed, travel-to-area, and remaining rectangle dimensions.",
                "Assign width to that plane, record its search legs, and continue until the rectangle or available planes are exhausted.",
                "Multiply each plane's effective sweep width by the stated two-way leg factor and full sweep length, then sum across planes.",
            ],
            [
                "Figure 6 explains searchleg/crossleg geometry, while the later scenario comparison reports relative days to the 95-percent target.",
                "The source does not compare the allocated legs to logged search-flight telemetry or observed debris detections.",
            ],
            [
                "The formula's factor of two is source-retained but the exact correspondence between leg geometry, searched tracks, and area requires an implementation-level convention.",
                "The method stops benefiting from added planes after one full area sweep, which motivates the optimized parallel variation.",
            ],
            [
                "Exact crossleg distances, turn-radius calculation for search aircraft, travel-to-search-area time, nonuniform sweep width, route deconfliction, and coverage-overlap accounting.",
            ],
            handoff_outputs=["A_parallel", "numlegs_i"],
        ),
        model(
            5,
            12,
            "4.5.2 Diagonal Search",
            "45-degree diagonal rectangular sweep",
            "Compute coverage from diagonal sweeps that lengthen central tracks but introduce short corner legs and additional turns.",
            [
                variable("plane_i", "search plane i", "aircraft instance", "One search aircraft allocated to the diagonal pattern.", "input"),
                variable("sweep_width_i", "plane-specific sweep width", "nautical miles", "Effective sweep width for plane i under the current conditions.", "parameter"),
                variable("numlegs_i", "completed diagonal legs", "count", "Number of diagonal search legs completed by plane i.", "intermediate"),
                variable("n", "plane count", "count", "Number of participating search planes.", "input"),
                variable("w", "long rectangle dimension", "nautical miles", "Longer search-area dimension used in the geometry.", "input"),
                variable("h", "short rectangle dimension", "nautical miles", "Shorter search-area dimension used in the geometry.", "input"),
                variable("SW", "aggregate diagonal sweep width", "nautical miles", "Total sweep-width equivalent accumulated across planes and legs.", "intermediate"),
                variable("c1", "first diagonal threshold", "nautical miles", "Short-dimension diagonal breakpoint h*sin(pi/4).", "intermediate"),
                variable("c2", "second diagonal threshold", "nautical miles", "Long-dimension diagonal breakpoint w*sin(pi/4).", "intermediate"),
                variable("A_diagonal", "diagonal swept area", "square nautical miles", "Piecewise area covered by the diagonal pattern.", "output"),
            ],
            ["plane_i", "sweep_width_i", "numlegs_i", "n", "w", "h"],
            ["SW", "c1", "c2", "A_diagonal"],
            diagonal,
            [
                "Search tracks are fixed at 45 degrees to the longer rectangle edge.",
                "Long central tracks improve straight-line search time, whereas corner tracks become short and require more turns.",
                "The paper treats the rectangular bounding area as the searchable geometry.",
            ],
            [
                "Compute the total SW from each plane's effective sweep width and legs.",
                "Derive c1 and c2 from the rectangle dimensions at 45 degrees.",
                "Choose the displayed piecewise area branch according to SW and pass the coverage to the POD/day calculation.",
            ],
            [
                "The Figure 7 scenario comparison evaluates diagonal and optimized-parallel days across the stated scenarios.",
                "The source finds diagonal search usually faster but also reports severe adverse-condition cases with extremely long predicted times.",
            ],
            [
                "The piecewise formula is visually retained but the text does not derive all branch conditions or establish continuity/dimensional checks.",
                "No route-level collision, turn-time, or weather-driven visibility validation is supplied for the diagonal allocation.",
            ],
            [
                "Exact diagonal-leg generation, path ordering, turn timing, crossleg distances, branch-test cases, coverage overlap, and empirical validation.",
            ],
            handoff_outputs=["A_diagonal", "SW"],
        ),
        model(
            6,
            12,
            "4.5.3 Optimized Parallel Search",
            "staggered repeated-coverage block allocation",
            "Reuse parallel-search blocks by staggering additional same-type planes so excess capacity can resweep the area and raise modeled coverage.",
            [
                variable("block_i", "search block i", "search-path block", "Stored parallel-search path for a given aircraft type.", "input"),
                variable("L_i", "legs in block i", "count", "Number of available legs in block i.", "input"),
                variable("P_i", "planes in block i", "count", "Number of staggered planes assigned to block i.", "input"),
                variable("TL_i", "total staggered legs", "count", "Total legs searched by all planes in block i after the one-leg decrement rule.", "output"),
                variable("sweep_width_block_i", "block sweep width", "nautical miles", "Effective sweep width of the aircraft type assigned to block i.", "parameter"),
                variable("n", "block count", "count", "Number of stored search blocks.", "input"),
                variable("L", "full sweep length", "nautical miles", "Length of one full sweep across the search area.", "input"),
                variable("A_swept", "optimized swept area", "square nautical miles", "Total effective area swept including repeated block coverage.", "output"),
            ],
            ["block_i", "L_i", "P_i", "sweep_width_block_i", "n", "L"],
            ["TL_i", "A_swept"],
            optimized_parallel,
            [
                "A block can contain no more planes than it has search legs.",
                "Planes in the same block start in sequence; each subsequent plane completes one fewer leg so all finish before the allotted time expires.",
                "The algorithm assigns each consecutive plane to a block of its type with the most available capacity.",
            ],
            [
                "Run the baseline parallel allocation and retain each aircraft-type path as a block.",
                "Assign extra planes sequentially to eligible blocks with maximum available space.",
                "Compute TL_i by the displayed finite series, then sum block contributions to A_swept.",
            ],
            [
                "The source compares this method with diagonal search in Figure 7 and uses it in its conditional recommendation.",
                "No schedule feasibility test, overlap measurement, or multi-aircraft operational exercise is reported.",
            ],
            [
                "The scheduling heuristic is greedy and the source does not prove it is globally optimal for heterogeneous aircraft, transit delays, or repeated coverage value.",
                "Repeated swept area is converted into POD through the later scalar relation without a direct detection-correlation model.",
            ],
            [
                "Aircraft availability times, deconfliction rules, base locations, fuel reserve constraints, repeated-pass correlation, greedy-assignment proof or benchmark, and operational simulation logs.",
            ],
            handoff_outputs=["A_swept", "TL_i"],
        ),
        model(
            7,
            13,
            "4.6 Full Statement of the Model's Main Equation",
            "daily detection threshold and algorithm-selection objective",
            "Convert the bounding n-gon and a selected algorithm's swept area into the paper's modeled number of days to exceed 95-percent cumulative detection.",
            [
                variable("n_gon", "search boundary polygon", "geospatial polygon", "Convex-hull n-gon bounding the daily search area.", "input"),
                variable("A_search", "bounding search area", "square nautical miles", "Maximum polygon width times maximum polygon height used as the rectangular denominator.", "intermediate"),
                variable("A_swept", "selected algorithm swept area", "square nautical miles", "Daily area supplied by the chosen parallel, diagonal, or optimized-parallel method.", "input"),
                variable("POD", "daily probability of detection", "probability", "POD from the source's A_swept/A_search exponential expression.", "output"),
                variable("POD_i", "day i detection value", "probability", "Daily POD contribution used in the displayed cumulative threshold statement.", "intermediate"),
                variable("days", "search-day count", "days", "Number of daily cycles until the paper's stated threshold is exceeded.", "output"),
                variable("threshold", "completion threshold", "probability", "The source's 0.95 modeled detection threshold.", "parameter"),
            ],
            ["n_gon", "A_swept", "threshold"],
            ["A_search", "POD", "days"],
            day_decision,
            [
                "The irregular hull is represented for this step by the maximum-width times maximum-height rectangle.",
                "Daily algorithm outputs are repeatedly evaluated until the displayed cumulative POD expression exceeds 0.95.",
                "The source uses modeled search coverage and not a verified real-world discovery probability as the selection objective.",
            ],
            [
                "Receive the day's drifted hull and an algorithm-specific swept area.",
                "Compute the rectangular A_search approximation and the displayed POD expression.",
                "Repeat the daily calculation, compare algorithms under scenario inputs, and report days to the stated threshold.",
            ],
            [
                "Section 5.2 reports three algorithms across more than 900 stated search scenarios and gives conditional algorithm recommendations.",
                "The paper's Air France 447 comparison checks an outer-bound area scale, not independent validation of daily POD or days-to-detection.",
            ],
            [
                "The rectangular denominator can include substantial unreachable or already-low-probability space.",
                "The displayed sum of daily POD values is retained verbatim as a source formula but is not derived as a probability composition law and requires independent verification before deployment.",
            ],
            [
                "Formal daily-probability composition, daily posterior update rule, path overlap treatment, hull-area alternative, scenario data table, 900-run records, and code producing recommendations.",
            ],
            handoff_outputs=["POD", "days"],
        ),
        model(
            8,
            13,
            "4.7 Tracing the Findings to the Crash",
            "reverse Euler debris-origin reconstruction",
            "Use a found debris location, elapsed time, and current field to step backward toward a refined crash-origin estimate.",
            [
                variable("longitude_f", "found-debris longitude", "longitude coordinate", "Longitude recorded when debris is found.", "input"),
                variable("latitude_f", "found-debris latitude", "latitude coordinate", "Latitude recorded when debris is found.", "input"),
                variable("longitude_0", "estimated origin longitude", "longitude coordinate", "Back-propagated longitude near the crash origin.", "output"),
                variable("latitude_0", "estimated origin latitude", "latitude coordinate", "Back-propagated latitude near the crash origin.", "output"),
                variable("delta_t", "reverse Euler time interval", "hours", "Time increment subtracted from the current displacement.", "parameter"),
                variable("dlongitude_dhours", "longitude current velocity", "longitude units per hour", "Local longitude component of the current field.", "input"),
                variable("dlatitude_dhours", "latitude current velocity", "latitude units per hour", "Local latitude component of the current field.", "input"),
                variable("elapsed_hours", "elapsed drift duration", "hours", "Time from crash to found debris that determines repeated reverse steps.", "input"),
            ],
            ["longitude_f", "latitude_f", "delta_t", "dlongitude_dhours", "dlatitude_dhours", "elapsed_hours"],
            ["longitude_0", "latitude_0"],
            reverse_drift,
            [
                "The found time and location are recorded accurately enough to define a reverse path.",
                "The same current-field representation used for forward drift can be applied in reverse.",
                "Floating debris follows the modeled currents and has not sunk or moved independently against the current.",
            ],
            [
                "Record the debris location and elapsed drift time.",
                "At each reverse time step, subtract the local current displacement from the current estimated position.",
                "Return the reverse-propagated point as a refined origin estimate to restart the search cycle.",
            ],
            [
                "The paper gives a causal role for found debris but no observed debris-to-crash backtrace error test.",
                "The future-work section requests local current data and acknowledges that current coverage is geographically limited.",
            ],
            [
                "Backward integration is sensitive to current-field error and elapsed-time uncertainty, and the source omits a posterior uncertainty region around the reconstructed origin.",
                "The formula uses a visually checked recurrence but does not provide a coordinate projection, integration step study, or data assimilation procedure.",
            ],
            [
                "Debris object properties, current-data uncertainty, time/location measurement error, interpolation, reverse-integration stability analysis, and truth-set validation.",
            ],
            handoff_outputs=["longitude_0", "latitude_0"],
        ),
        model(
            9,
            14,
            "5.2 Results, Section 6 Sensitivity, and Section 8 Conclusion",
            "scenario comparison and conditional search-method recommendation",
            "Compare diagonal and optimized-parallel search durations under resource, weather, area, visibility, and aircraft scenarios, then state conditional method rules.",
            [
                variable("algorithm", "candidate search algorithm", "categorical method", "Parallel, diagonal, or optimized-parallel algorithm being evaluated.", "input"),
                variable("plane_count", "available search planes", "count", "Number of aircraft available for the search scenario.", "input"),
                variable("weather", "weather conditions", "scenario descriptor", "Weather inputs affecting visibility and sweep width in the stated scenarios.", "input"),
                variable("visibility", "visibility range", "nautical miles", "Visible distance that affects effective sweep width.", "input"),
                variable("area_size", "search-area size", "square nautical miles", "Area scenario supplied to the daily coverage calculation.", "input"),
                variable("predicted_days", "predicted search duration", "days", "Model output used to compare search algorithms.", "output"),
                variable("recommendation", "conditional method recommendation", "categorical decision", "Recommended algorithm under the source's scenario conditions.", "output"),
            ],
            ["algorithm", "plane_count", "weather", "visibility", "area_size"],
            ["predicted_days", "recommendation"],
            [],
            [
                "The tested scenarios use the paper's current model, including its search-area, sweep-width, and POD simplifications.",
                "The reported 900-plus scenarios cover the source's selected combinations rather than a representative real-world operational distribution.",
                "The conclusion selects optimized parallel for few planes/large area/bad weather and many planes/small area/good weather; otherwise it selects diagonal search.",
            ],
            [
                "Run each named algorithm over a declared combination of planes, weather, visibility, and search area.",
                "Calculate days until the model's 95-percent threshold and plot/compare the outcomes.",
                "Use the source's conditional rules while retaining the adverse-condition exception and unmodeled deployment boundaries.",
            ],
            [
                "Figure 7 shows diagonal and optimized-parallel outcomes over the stated scenario index.",
                "Section 6 varies six parameters one at a time around a baseline 11-day prediction and reports qualitative response patterns.",
            ],
            [
                "Scenario output is a within-model comparison, not a validation against real search operations or a proof of globally optimal scheduling.",
                "One-at-a-time sensitivity changes do not identify interactions among altitude, wind, visibility, aircraft count, area, and current drift.",
            ],
            [
                "The 900-scenario matrix, input distributions, output table, code, randomization/seeds, statistical uncertainty, interaction analysis, and independent operational holdout.",
            ],
            parameter_method="The paper fixes a baseline of altitude, crash-plane speed, crash-time wind, search-plane count, search-time wind, and visibility, then changes one parameter at a time; sampling and calibration procedures are not supplied.",
            cost="Proportional to the number of algorithms, scenario combinations, daily iterations, aircraft assignments, and drift/coverage calculations; the source does not report runtime or hardware.",
            handoff_outputs=["predicted_days", "recommendation"],
        ),
    ]
    edges = [
        {"from_model_id": models[0]["model_id"], "to_model_id": models[1]["model_id"], "handoff": "The initial convex-hull boundary supplies markers and the first daily search polygon for forward drift."},
        {"from_model_id": models[1]["model_id"], "to_model_id": models[2]["model_id"], "handoff": "The drifted hull defines the day-specific search area used by the detection relation."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "Effective sweep width and detection semantics constrain the parallel allocation's area contribution."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[4]["model_id"], "handoff": "The same search-plane effectiveness inputs are used by the diagonal swept-area calculation."},
        {"from_model_id": models[3]["model_id"], "to_model_id": models[5]["model_id"], "handoff": "The baseline parallel blocks are retained so extra aircraft can be assigned for staggered repeated coverage."},
        {"from_model_id": models[3]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "Parallel swept area is one candidate A_swept input to the daily detection threshold."},
        {"from_model_id": models[4]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "Diagonal swept area is an alternative A_swept input to the daily detection threshold."},
        {"from_model_id": models[5]["model_id"], "to_model_id": models[6]["model_id"], "handoff": "Optimized repeated-coverage A_swept enters the same daily POD/day comparison."},
        {"from_model_id": models[6]["model_id"], "to_model_id": models[7]["model_id"], "handoff": "A found-debris-triggered refinement uses elapsed time and the current field to return an updated crash-origin estimate."},
        {"from_model_id": models[6]["model_id"], "to_model_id": models[8]["model_id"], "handoff": "Modeled days-to-threshold and scenario outcomes become the evidence for the conditional algorithm recommendation."},
        {"from_model_id": models[7]["model_id"], "to_model_id": models[0]["model_id"], "handoff": "The reverse-drift origin estimate is intended to restart the search cycle with a refined initial location."},
    ]
    return {
        "schema_version": 2,
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "review_status": "validated",
        "models": models,
        "dependency_edges": edges,
    }


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    record = build_models()
    STAGE.mkdir(parents=True)
    target = STAGE / "models.json"
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    equation_count = sum(len(item["governing_equations"]) for item in record["models"])
    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "models": len(record["models"]),
                "equations": equation_count,
                "dependency_edges": len(record["dependency_edges"]),
                "stage": str(target),
                "status": "pass",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
