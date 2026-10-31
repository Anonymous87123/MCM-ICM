from __future__ import annotations

"""Build the source-checked G5 model record for Queue 112 without promotion."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-40612-8bcdc1a7"
TYPE = "B"
YEAR = "2015"
SHORT = "40612"
SHA256 = "8bcdc1a780f3e08a678c1f450512da6656300cbb3c537ac5e97b29824f07322f"
STAGE = ROOT / "tmp/q112-model-stage-v2"


def variable(symbol: str, name: str, unit: str, definition: str, role: str, status: str = "explicit-defined") -> dict:
    return {"symbol": symbol, "normalized_name": name, "unit": unit, "definition": definition, "role": role, "source_status": status}


def equation(index: int, page: int, label: str, source_expression: str, normalized_latex: str, symbols: list[str], purpose: str, confidence: str = "high") -> dict:
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
    parameter_method: str = "The paper assigns aircraft, collision, drift, mixture, detection, and search values from cited context, qualitative judgment, or hand-selected scenarios; it does not fit a jointly identified incident model.",
    feasibility: str = "partial",
    feasibility_analysis: str = "The paper supplies an analytical workflow, deterministic figures and tables, and two case narratives, but no executable archive, independent holdout protocol, optimization trace, or operational trial.",
    convergence: str = "Finite formulas, grids, ranking steps, and recursive search phases are described; no numerical tolerance, random seed, phase budget, branch-and-bound stopping trace, grid convergence, or recursion termination analysis is reported.",
    cost: str = "Cost depends on current-field interpolation, trajectory simulation, cell likelihood updates, posterior normalization, platform-cell assignments, branch-and-bound candidates, search phases, and sensitivity reruns; runtime and hardware are not reported.",
) -> dict:
    parameters = [item["symbol"] for item in variables if item["role"] == "parameter"]
    return {
        "model_id": f"MU-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "page": page,
        "section": section,
        "family": family,
        "purpose": purpose,
        "base_or_modification": "paper-specific",
        "summary": purpose,
        "variables": variables,
        "inputs": inputs,
        "outputs": outputs,
        "governing_equations": equations,
        "equation_status": {
            "status": "present" if equations else "omitted-by-paper",
            "reason": "All displayed equations assigned to this component were reconciled against the rendered source and bounded review proxies." if equations else "The source supplies this layer through prose, figures, tables, or a named algorithm without a separate displayed mathematical equation.",
        },
        "objectives": [purpose, "Produce a source-traceable physical, probabilistic, allocation, application, sensitivity, or decision output without upgrading simulated or retrospective evidence to field validation."],
        "constraints": [
            "Retain the source's target class, probability role, phase, cell domain, mixture weights, platform capability, report outcome, and case-specific inputs at every handoff.",
            "Preserve printed notation, units, formula defects, missing likelihoods, and absent optimization constraints as evidence boundaries; corrected implementations are separate extensions.",
        ],
        "conditions": {
            "initial": condition("present", "Aircraft properties, incident evidence, current data, initial target state, mixture weights, cell grid, search reports, and platform capabilities must be declared before the relevant component runs."),
            "boundary": condition("present", "The source assumes equal fragments, common initial drifter position, simplified currents and random motion, static wreckage, stationary targets during a search phase, no false positives, aircraft-only search, weather-invariant capability, and area limits replacing range."),
            "equilibrium": condition("not-applicable", "The paper uses finite collision mappings, simulated trajectories, Bayesian phase updates, ranking, assignment, and sensitivity grids rather than an equilibrium solve."),
        },
        "parameter_estimation": {"status": "partial", "method": parameter_method, "parameters": parameters},
        "algorithm": {"status": "partial", "steps": algorithm_steps, "software": ["No source code, configuration, dependency version, seed manifest, run log, machine-readable cell grid, or optimization trace is bundled with the paper."], "convergence_criteria": convergence},
        "assumptions": assumptions,
        "identifiability_feasibility": {"status": feasibility, "analysis": feasibility_analysis},
        "handoff_outputs": outputs,
        "validation_refs": validation_refs,
        "computational_cost": cost,
        "strengths": ["The component has an explicit place in the aircraft -> drifters -> drift evidence -> surface posterior -> underwater recursion -> allocation -> case decision chain.", "Its observed, assumed, derived, simulated, and display-only quantities remain distinguishable from later warnings and proposed repairs."],
        "limitations": limitations,
        "missing_details": missing_details,
    }


def build_models() -> dict:
    eq = {
        1: equation(1, 10, "Equation (1), maximum drifter count", "N0 = alpha V", r"N_0=\alpha V", ["N0", "alpha", "V"], "Scale the maximum number of floating targets by aircraft volume."),
        2: equation(2, 11, "Equation (2), actual drifter count", "N = beta N0", r"N=\beta N_0", ["N", "beta", "N0"], "Apply the disintegration fraction to the maximum count."),
        3: equation(3, 11, "Equation (3), printed velocity components", "v_x = cos(theta); v_y = sin(theta)", r"v_x=\cos\theta,\qquad v_y=\sin\theta", ["v_x", "v_y", "theta"], "Record the printed component expressions used before the impulse calculation.", "medium"),
        4: equation(4, 11, "Equation (4), vertical impulse", "I = m v_y = m v sin(theta)", r"I=mv_y=mv\sin\theta", ["I", "m", "v_y", "v", "theta"], "Approximate collision impulse from the vertical momentum component."),
        5: equation(5, 12, "Equation (5), piecewise disintegration degree", "beta=0 for I<=I0; beta=gamma(I-I0) for I0<I<I0+1/gamma; beta=1 for I>=I0+1/gamma", r"\beta=\begin{cases}0,&I\le I_0,\\\gamma(I-I_0),&I_0<I<I_0+1/\gamma,\\1,&I\ge I_0+1/\gamma.\end{cases}", ["beta", "I", "I0", "gamma"], "Map impulse to a bounded zero-linear-saturation disintegration fraction."),
        6: equation(6, 15, "Equation (6), accident-distance cumulative distribution", "F(D) = 1 - 2^2/(D^2 + 2^2)", r"F(D)=1-\frac{2^2}{D^2+2^2}", ["F_D", "D"], "Fit the cumulative fraction of nine loss-of-control accidents by distance from emergency to impact.", "medium"),
        7: equation(7, 18, "Equation (7), surface-search Bayes update", "P_D(S_i,j|B) = P(B|S_i,j) P_D(S_i,j) / sum_{S_m,n in S} P(B|S_m,n) P_D(S_m,n)", r"P_D(S_{i,j}\mid B)=\frac{P(B\mid S_{i,j})P_D(S_{i,j})}{\sum_{S_{m,n}\in S}P(B\mid S_{m,n})P_D(S_{m,n})}", ["P_D_post", "B", "S_ij", "P_B_given_S", "P_D", "S"], "Normalize cell probabilities after a successful or unsuccessful search report."),
    }

    models = [
        model(
            1, 10, "6.1 maximum drifter capacity", "aircraft-volume capacity model", "Estimate the maximum number of potentially floating targets from the crashed aircraft's volume.",
            [variable("N0", "maximum drifter count", "count", "Maximum bodies and debris pieces capable of floating.", "output"), variable("alpha", "drifter-volume ratio", "count per volume", "Ratio of maximum drifters to aircraft volume.", "parameter"), variable("V", "aircraft volume", "volume", "Full-loaded crashed-aircraft volume.", "input")],
            ["alpha", "V"], ["N0"], [eq[1]],
            ["The aircraft is full-loaded.", "Maximum floating-object count is directly proportional to total aircraft volume."],
            ["Classify the crashed aircraft.", "Obtain or assume V and alpha.", "Compute N0=alpha V."],
            ["Section 3 relates size, passenger capacity, and material to debris potential.", "The collision model carries N0 into actual drifter count."],
            ["A single volume coefficient collapses cabin contents, passenger count, material, buoyancy, and breakup geometry."],
            ["Aircraft-specific V, definition and units of alpha, floating-object inventory, uncertainty, and calibration observations are absent."],
        ),
        model(
            2, 11, "6.1.1-6.1.2 disintegration and collision impulse", "piecewise collision-severity model", "Convert disintegration regime and impact impulse into the actual number of surface drifters.",
            [variable("N", "actual drifter count", "count", "Modeled bodies and debris pieces after the crash.", "output"), variable("N0", "maximum drifter count", "count", "Capacity output from Model 1.", "input"), variable("beta", "degree of disintegration", "dimensionless in [0,1]", "Fraction of maximum drifters released.", "output"), variable("m", "aircraft mass", "mass", "Full-loaded aircraft mass at impact.", "input"), variable("v", "impact speed", "length per time", "Flight velocity magnitude at water collision.", "input"), variable("theta", "water contact angle", "radians", "Angle between aircraft velocity and water surface.", "input"), variable("v_x", "printed horizontal velocity component", "dimensionless as printed", "Source expression omits multiplication by v.", "intermediate", "explicit-defined"), variable("v_y", "vertical velocity component", "length per time in Equation (4)", "Vertical speed entering the impulse.", "intermediate"), variable("I", "vertical collision impulse", "momentum", "Impulse after neglecting horizontal direction.", "intermediate"), variable("I0", "disintegration threshold", "momentum", "Impulse below which beta is zero.", "parameter"), variable("gamma", "linear disintegration slope", "inverse momentum", "Slope between zero and saturation.", "parameter")],
            ["N0", "m", "v", "theta", "I0", "gamma"], ["v_x", "v_y", "I", "beta", "N"], [eq[i] for i in range(2, 6)],
            ["Air disintegration has one constant beta for the whole plane.", "Water disintegration is an ideal collision with negligible horizontal impulse.", "All broken pieces have the same size.", "Beta is zero below I0, linear in the middle regime, and one after saturation."],
            ["Choose the disintegration regime.", "For water impact, calculate the printed velocity components and I.", "Map I through the piecewise beta function.", "Compute N=beta N0."],
            ["Figure 1 diagrams the water-impact geometry.", "The page-12 piecewise expression was checked on a focused bounded proxy."],
            ["Equation (3) omits speed v from the printed components, while Equation (4) restores v in m v sin(theta); the two equations are not dimensionally equivalent as printed.", "I0 and gamma are said obtainable from practical data but no data or values are supplied."],
            ["Regime classifier, alpha, beta for air breakup, fragment-size distribution, hydrodynamic impulse, aircraft orientation, threshold data, and uncertainty are absent."],
        ),
        model(
            3, 12, "6.2 System Module", "current-driven stochastic drift simulation", "Generate synthetic debris locations and trajectories for inspecting or correcting the search model.",
            [variable("X0", "common impact position", "latitude-longitude", "Initial position shared by all simulated drifters.", "input"), variable("U", "surface current field", "distance per time", "OSCAR-derived current forcing over space and time.", "input"), variable("eta", "computer random motion", "unspecified stochastic displacement", "Unspecified random motion added by the simulation.", "parameter"), variable("t", "simulation time", "time", "Trajectory time coordinate.", "state"), variable("X_t", "simulated drifter positions", "latitude-longitude", "Synthetic positions and trajectories after forcing and randomness.", "output"), variable("truth_role", "simulator evidence class", "categorical", "Synthetic hidden state used for within-model diagnostics, not observed ground truth.", "output")],
            ["X0", "U", "eta", "t"], ["X_t", "truth_role"], [],
            ["All drifters begin at the same impact position.", "Bodies and debris respond identically.", "Surface motion uses currents and computer random motion only.", "Underwater parts become static on the seabed."],
            ["Load a current field.", "Initialize drifters at X0.", "Apply current forcing and unspecified random motion through time.", "Record trajectories and compare search outputs with the synthetic hidden state."],
            ["Figure 5 shows imagined trajectories over two days.", "Section 6.2 states that the module is used to measure and correct the search model."],
            ["The source calls the simulator an exact answer, but the state is generated by simplified forcing and unspecified randomness, so it is simulated evidence only."],
            ["State-update equation, interpolation grid, time step, integration method, random distribution, seeds, boundary handling, leeway model, validation observations, and correction criterion are absent."],
        ),
        model(
            4, 14, "6.4.1.1 Flight Dynamics Prior PDF", "mixture flight-dynamics prior", "Combine last-known-position reachability with an accident-distance distribution to form a flight-dynamics prior.",
            [variable("LKP", "last known position", "latitude-longitude", "Last reported aircraft position.", "input"), variable("T_gap", "unreported travel interval", "time", "Time from last report to missing scheduled ACARS response.", "input"), variable("R_max", "maximum feasible travel radius", "distance", "Reachable radius under flight-dynamics assumptions.", "intermediate"), variable("D", "emergency-to-impact distance", "distance", "Distance used by the nine-accident cumulative distribution.", "state"), variable("F_D", "accident-distance cumulative fraction", "probability", "Fitted cumulative distribution across nine accidents.", "output"), variable("w_LKP", "LKP component weight", "dimensionless", "Weight of equal-probability reachable circle.", "parameter"), variable("w_acc", "accident component weight", "dimensionless", "Weight of accident-distance distribution.", "parameter"), variable("P_F", "flight-dynamics prior", "spatial probability density", "Fifty-fifty mixture of the two components.", "output")],
            ["LKP", "T_gap", "D", "w_LKP", "w_acc"], ["R_max", "F_D", "P_F"], [eq[6]],
            ["Every point in the maximum reachable circle has equal impact probability.", "Nine loss-of-control accidents represent the relevant distance pattern.", "Both components receive weight 0.5."],
            ["Compute a reachable circle from LKP and elapsed time.", "Evaluate the fitted F(D).", "Convert the cumulative curve into the source's spatial component.", "Mix the two components at 50/50."],
            ["Figures 3-4 display the accident-distance curve and flight-dynamics prior.", "The MH370 application later substitutes an external probability distribution for P_F."],
            ["The paper does not list the nine observations, fit diagnostics, spatial conversion from F(D), reachable-speed assumptions, or a rationale that identifies equal weights."],
            ["Accident sample rows, units of D and the constant 2, density derivation, normalization domain, aircraft-state uncertainty, ACARS interval, and weight calibration are absent."],
        ),
        model(
            5, 16, "6.4.1.2 Reverse Drift Prior PDF", "reverse current interpolation and drifter backtracking", "Backtrack spotted surface targets through interpolated ocean currents to form a reverse-drift prior.",
            [variable("X_obs", "observed drifter locations", "latitude-longitude", "Positions of bodies or debris spotted during surface search.", "input"), variable("U_OSCAR", "OSCAR mean current field", "distance per time", "At least five-day mean currents by latitude, longitude, and date.", "input"), variable("lambda", "drifter-to-current speed ratio", "dimensionless", "Source-set value 0.25.", "parameter"), variable("U_d", "effective drifter speed", "distance per time", "Quarter of interpolated current speed.", "intermediate"), variable("X_impact", "backtracked impact positions", "latitude-longitude", "Estimated initial positions at crash time.", "output"), variable("P_R", "reverse-drift prior", "spatial probability density", "Sum of distributions produced from each spotted target.", "output")],
            ["X_obs", "U_OSCAR", "lambda"], ["U_d", "X_impact", "P_R"], [],
            ["Wind affects drifters only through its influence on currents.", "Bodies and debris share one movement model.", "Linear interpolation is adequate for the current field.", "Actual drifter speed is 0.25 of current speed."],
            ["Select the incident period and area in OSCAR.", "Linearly interpolate currents.", "Scale speed by lambda=0.25.", "Integrate positions backward to the crash time.", "Sum the resulting location distributions."],
            ["Section 6.4.1.2 names OSCAR coverage from 1992-10-15 to 2015-02-05.", "Figure 5 illustrates trajectory divergence in the separate simulator."],
            ["The 0.25 coefficient is justified qualitatively by currents, winds, and temperature rather than identified from drifter observations; wind leeway is omitted as a separate mechanism."],
            ["OSCAR files and version, interpolation formula, temporal resolution, integration method, uncertainty kernel, observation errors, target-specific leeway, coast boundaries, and backtracking validation are absent."],
        ),
        model(
            6, 16, "6.4.1.3-6.4.2 Surface Search Prior and Posterior", "weighted prior fusion and Bayesian cell update", "Fuse flight and reverse-drift priors, then update cell probabilities from surface-search detection reports.",
            [variable("P_F", "flight-dynamics prior", "spatial probability density", "Output from Model 4.", "input"), variable("P_R", "reverse-drift prior", "spatial probability density", "Output from Model 5.", "input"), variable("w_F", "surface flight-prior weight", "dimensionless", "Source-set value 0.70.", "parameter"), variable("w_R", "surface reverse-drift weight", "dimensionless", "Source-set value 0.30.", "parameter"), variable("P_D", "surface target prior", "cell probability", "Prior probability that a drifter occupies S_i,j.", "input"), variable("S_ij", "candidate search cell", "cell index", "One equal-size cell in the current surface-search area.", "state"), variable("S", "current search domain", "set of cells", "Whole search area for the contemporary phase.", "input"), variable("B", "surface search report", "successful or unsuccessful", "Observed binary report from the assigned aircraft.", "input"), variable("P_B_given_S", "surface observation likelihood", "probability", "Chance of report B if the target is in a cell.", "parameter"), variable("P_AkD", "aircraft surface detection probability", "probability", "Conditional detection capability for aircraft A_k and a drifter in S_i,j.", "parameter"), variable("P_surface_prior", "surface-search prior", "spatial probability density", "Weighted fusion before practical surface search.", "output"), variable("P_D_post", "surface posterior", "cell probability", "Normalized posterior after report B.", "output")],
            ["P_F", "P_R", "w_F", "w_R", "P_D", "S", "B", "P_B_given_S", "P_AkD"], ["P_surface_prior", "P_D_post"], [eq[7]],
            ["There is at most one drifter in a cell.", "Cells are equal size.", "Targets do not move during a search phase.", "Drifters share one detection probability.", "Sensors have no false positives but may miss present targets."],
            ["Mix P_F and P_R at 70/30.", "Assign aircraft to a first surface-search phase.", "Translate successful or unsuccessful report B into cell likelihoods.", "Normalize Equation (7) over S.", "Pass the posterior to the underwater phase."],
            ["Figure 6 shows the surface prior and Figure 7 the posterior.", "The page-18 formula and denominator domain were checked on a focused bounded proxy."],
            ["The mixture weights express a qualitative uncertainty judgment, not calibration; the paper defines P_AkD but never specifies the likelihood mapping for success and failure."],
            ["Cell size and grid, prior normalization, aircraft search coverage, report-to-likelihood mapping, repeated-search dependence, false-negative calibration, and numeric posterior values are absent."],
        ),
        model(
            7, 19, "6.5 Underwater Search Model", "phase-recursive underwater Bayesian filter", "Construct an underwater prior and recursively update wreckage-cell probabilities after unsuccessful phases.",
            [variable("P_D_post", "surface posterior", "spatial probability density", "Surface-search output from Model 6.", "input"), variable("P_F", "flight-dynamics prior", "spatial probability density", "Flight prior reused after surface search.", "input"), variable("w_surface", "underwater surface-posterior weight", "dimensionless", "Source-set value 0.30.", "parameter"), variable("w_flight", "underwater flight-prior weight", "dimensionless", "Source-set value 0.70.", "parameter"), variable("P_W", "wreckage prior", "cell probability", "Probability wreckage lies in S_i,j before a phase.", "input"), variable("P_AkW", "aircraft underwater detection probability", "probability", "Conditional probability of detecting wreckage in a cell.", "parameter"), variable("B_W", "underwater report", "successful or unsuccessful", "Phase observation.", "input"), variable("P_U_prior", "underwater phase prior", "spatial probability density", "Weighted initial or previous-phase prior.", "output"), variable("P_W_post", "underwater phase posterior", "cell probability", "Posterior after one phase.", "output"), variable("phase", "underwater phase index", "positive integer", "Recursion counter.", "state"), variable("stop", "search termination state", "boolean", "Detection or intentional suspension.", "output")],
            ["P_D_post", "P_F", "w_surface", "w_flight", "P_W", "P_AkW", "B_W", "phase"], ["P_U_prior", "P_W_post", "stop"], [],
            ["Wreckage remains static on the seafloor.", "Surface search stops once underwater phases begin.", "Underwater sensors can reach beyond seafloor depth.", "The surface Bayes form applies after substituting wreckage states and likelihoods."],
            ["Mix 30% surface posterior with 70% flight prior for Phase I.", "Search according to the current prior.", "Substitute P_W and P_AkW into the Bayes update.", "Use the posterior as the next phase's prior after a miss.", "Stop on detection or intentional suspension."],
            ["Figures 8-9 show the underwater prior and posterior.", "Section 6.5.4 explicitly defines posterior-to-prior recursion."],
            ["The same aircraft-only platform assumption is used for underwater search without a sonar geometry, depth model, likelihood calibration, or phase budget."],
            ["Underwater cell likelihoods, depth and bathymetry inputs, sensor footprints, platform feasibility, phase duration, cumulative dependence, search costs, suspension rule, and numeric posterior grids are absent."],
        ),
        model(
            8, 21, "7 Allocation Model", "ranked branch-and-bound aircraft-cell assignment", "Assign heterogeneous search aircraft to high-probability cells to maximize stated cumulative detection probability.",
            [variable("p_cell", "updated cell probability", "probability", "Current PDF value for a search cell.", "input"), variable("c_aircraft", "aircraft search capability", "area limit and detection probability", "Capability score used for ranking.", "input"), variable("rank_cells", "descending cell order", "ordered cells", "Quicksort output by p_cell.", "intermediate"), variable("rank_aircraft", "descending aircraft order", "ordered platforms", "Quicksort output by capability.", "intermediate"), variable("x_akij", "aircraft-cell assignment", "binary decision", "Whether aircraft A_k is allocated to cell S_i,j.", "output", "inferred-from-equation"), variable("P_cum", "cumulative detection objective", "probability sum as stated", "Sum of probabilities at allocated points or cells.", "output"), variable("allocation", "search-plane allocation plan", "assignment", "Matched aircraft and cells.", "output")],
            ["p_cell", "c_aircraft"], ["rank_cells", "rank_aircraft", "x_akij", "P_cum", "allocation"], [],
            ["Higher-ranked aircraft should be paired with higher-probability cells.", "Area limit and detection rate adequately summarize platform capability.", "The sum of point or cell probabilities is an appropriate objective."],
            ["Quicksort cells by updated PDF.", "Quicksort aircraft by search capability.", "Generate high-priority candidate pairings.", "Apply branch-and-bound to maximize the stated cumulative detection probability.", "Return the allocation."],
            ["Figure 10 illustrates larger rectangles for better aircraft in higher-priority areas.", "Section 7.1 states generic lower/upper-bound pruning logic."],
            ["No formal decision-variable definition, objective equation, constraints, bounds, branching rule, incumbent trace, or solved numeric instance is supplied, so optimality and even exact feasibility cannot be reproduced."],
            ["One-aircraft/one-cell capacities, overlap, travel time, base range, voyage, fuel, phase duration, multiple targets, PDF-POD combination, search-area discretization, and termination certificate are absent."],
        ),
        model(
            9, 22, "8 AF447 and MH370 applications", "retrospective and conditional case application", "Instantiate the probability pipeline for an AF447 location comparison and a conditional MH370 search distribution.",
            [variable("AF_LKP", "AF447 last known position", "latitude-longitude", "Case reference position.", "input"), variable("AF_wreck", "AF447 observed wreckage location", "latitude-longitude", "Known point about 6.5 NM from LKP at 3,900 m depth.", "input"), variable("AF_surface", "AF447 initial-search drifter distribution", "spatial probability density", "Table 3 distribution treated as surface posterior.", "input"), variable("AF_prior", "AF447 underwater prior", "spatial probability density", "70% flight prior plus 30% surface posterior.", "output"), variable("AF_region", "AF447 suggested area", "spatial region", "Area containing the known point in Figure 11.", "output"), variable("MH_path", "MH370 external path distribution", "spatial probability density", "Constrained autopilot and data-error distribution adopted from cited analyses.", "input"), variable("MH_report", "assumed MH370 search reports", "all unsuccessful", "No-detection assumption for both phases.", "input"), variable("MH_pdfs", "MH370 phase distributions", "four spatial probability densities", "Surface prior/posterior and underwater prior/posterior in Figure 14.", "output")],
            ["AF_LKP", "AF_wreck", "AF_surface", "MH_path", "MH_report"], ["AF_prior", "AF_region", "MH_pdfs"], [],
            ["AF447 initial-search position data can stand in for the surface posterior.", "The point of highest underwater-prior density defines a suggested location.", "The external MH370 probability distribution can replace the paper's flight-dynamics prior.", "MH370 surface and underwater phases yield no detections."],
            ["Build the AF447 underwater prior and compare its suggested area with the known wreckage point.", "Adopt the external MH370 path distribution.", "Apply no-detection surface and underwater updates.", "Plot four MH370 phase PDFs."],
            ["Figure 11 marks the AF447 wreckage point inside the suggested area.", "Figures 12-14 trace external MH370 search regions and the paper's four phase distributions."],
            ["AF447 reuses known incident information and reports only region inclusion, without area, coverage, baseline, holdout, or likelihood calibration; MH370 is conditional on assumed nondetections and an externally supplied prior."],
            ["AF447 Table 3 data, exact region boundary, distance from predicted maximum, comparison method, MH370 raster values, search footprints, likelihoods, and later outcome evaluation are absent."],
        ),
        model(
            10, 27, "9 Sensitivity and 10-11 decision communication", "local sensitivity and evidence-bounded recommendation", "Measure local response to target count, fleet quantity/type, and mixture weights, then delimit technical and public claims.",
            [variable("N", "drifter count", "count", "Tested at 50, 100, and 200.", "input"), variable("n_planes", "search-plane count", "count", "Tested at two, three, and four identical platforms.", "input"), variable("plane_pair", "search-aircraft type combination", "categorical pair", "Selected pairs from nine hand-set profiles.", "input"), variable("w", "prior mixture weights", "30/70, 50/50, or 70/30", "Three local two-component weight grids.", "input"), variable("P_loc", "cumulative wreckage localization probability", "probability", "Reported sum of P_AkW(S_i,j) used as sensitivity metric.", "output"), variable("sensitivity_scope", "supported stability class", "categorical", "Local direction and weight response under the displayed settings.", "output"), variable("recommendation", "bounded search recommendation", "decision", "Use fast sequential updating and capability-aware allocation subject to assumptions and parameter gaps.", "output"), variable("public_paper", "press-conference artifact", "communication", "Nontechnical search chronology and commitment.", "output")],
            ["N", "n_planes", "plane_pair", "w"], ["P_loc", "sensitivity_scope", "recommendation", "public_paper"], [],
            ["The displayed test settings hold all unreported factors fixed.", "One cumulative probability metric is sufficient for local comparison.", "The AF447 application and small sensitivity grids are treated by the source as evidence of accuracy and robustness."],
            ["Evaluate P_loc for three drifter counts.", "Evaluate P_loc for three fleet counts.", "Compare selected two-aircraft profiles.", "Sweep each of three mixture pairs over three weights.", "Separate local direction and weight stability from untested parameter, structural, numerical, and external dimensions.", "Translate the bounded workflow for the public."],
            ["Tables 3-9 retain all displayed sensitivity values.", "Section 10 names computation, unrealistic assumptions, and hard parameters.", "Section 11 retains rapid response, recursive updates, allocation, and continued search."],
            ["The grids are deterministic and sparse; no uncertainty, repeat simulation, seed, solver, joint interaction, structural alternative, threshold stability, or external validation supports the source's universal robustness and precision claims."],
            ["Baseline case identity, all fixed inputs, metric denominator, probability aggregation semantics, run artifacts, confidence intervals, significance criteria, opposite-result policy, and decision thresholds are absent."],
        ),
    ]

    edges = [
        (1, 2, "Maximum drifter capacity is reduced by collision-specific disintegration."),
        (2, 3, "Actual drifter count and impact origin initialize the synthetic movement environment."),
        (3, 5, "The movement concept motivates reverse-drift reconstruction, although the exact simulator is not reused as observed data."),
        (4, 6, "The flight-dynamics prior supplies the dominant surface-prior component."),
        (5, 6, "The reverse-drift prior supplies the lower-weight surface component."),
        (6, 7, "The surface posterior enters the underwater Phase-I prior."),
        (4, 7, "The flight-dynamics prior is reintroduced as the dominant underwater component."),
        (6, 8, "Updated surface cell probabilities can be ranked for aircraft allocation."),
        (7, 8, "Updated underwater cell probabilities can be ranked for later allocation."),
        (4, 9, "AF447 and MH370 applications instantiate or replace the flight prior."),
        (6, 9, "The surface prior/posterior pipeline is applied to both cases."),
        (7, 9, "The underwater recursion produces the case phase maps."),
        (8, 9, "The intended allocation layer supplies the case-specific resource handoff, though no complete trace is printed."),
        (2, 10, "Drifter-count sensitivity perturbs the collision-model output."),
        (4, 10, "Flight-prior mixture sensitivity perturbs Model 4's component weight."),
        (6, 10, "Surface-prior mixture sensitivity and cumulative localization metrics depend on the surface update."),
        (7, 10, "Underwater-prior mixture sensitivity and recursive outcome claims depend on the underwater update."),
        (8, 10, "Fleet count and platform-type sensitivity act through the intended allocation interface."),
        (9, 10, "Case outputs are summarized into technical and public recommendations."),
    ]
    return {
        "schema_version": 2,
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "review_status": "validated",
        "models": models,
        "dependency_edges": [{"from_model_id": models[source - 1]["model_id"], "to_model_id": models[target - 1]["model_id"], "handoff": handoff} for source, target, handoff in edges],
    }


def validate(record: dict) -> None:
    equations = [item for model_unit in record["models"] for item in model_unit["governing_equations"]]
    if len(record["models"]) != 10:
        raise ValueError(f"expected 10 models, found {len(record['models'])}")
    if len(equations) != 7:
        raise ValueError(f"expected 7 displayed equations, found {len(equations)}")
    if [item["equation_id"] for item in equations] != [f"EQ-B-2015-40612-{index:03d}" for index in range(1, 8)]:
        raise ValueError("equation records must retain source order")
    if len(record["dependency_edges"]) != 19:
        raise ValueError("expected 19 typed model dependency edges")


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    record = build_models()
    validate(record)
    STAGE.mkdir(parents=True)
    target = STAGE / "models.json"
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "models": len(record["models"]), "equations": 7, "dependency_edges": len(record["dependency_edges"]), "stage": str(target), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
