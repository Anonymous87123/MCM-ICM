from __future__ import annotations

"""Build the source-checked G5 model record for Queue 110 without promotion."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-38720-26d38781"
TYPE = "B"
YEAR = "2015"
SHORT = "38720"
SHA256 = "26d38781a179b71806799b0d20f118a5f0b09aa1cf6b8bc7a5e32562a7886a42"
STAGE = ROOT / "tmp/q110-model-stage-v1"


def variable(
    symbol: str,
    name: str,
    unit: str,
    definition: str,
    role: str,
    status: str = "explicit-defined",
) -> dict:
    return {
        "symbol": symbol,
        "normalized_name": name,
        "unit": unit,
        "definition": definition,
        "role": role,
        "source_status": status,
    }


def equation(
    index: int,
    page: int,
    source_expression: str,
    normalized_latex: str,
    symbols: list[str],
    purpose: str,
    confidence: str = "high",
) -> dict:
    return {
        "equation_id": f"EQ-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "page": page,
        "label": f"({index})",
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
    parameter_method: str = "The paper fixes representative values from cited specifications and simulation choices; it does not fit a calibrated field model.",
    feasibility: str = "partial",
    feasibility_analysis: str = "The source supplies a finite simulation and decision workflow, but not executable code, seeds, field calibration, or an independent incident holdout.",
    convergence: str = "Each run stops at discovery or the stated time cap; the paper reports no time-step, sample-size, or random-seed convergence study.",
    cost: str = "Cost scales with simulated crash points, path time steps, posterior-grid updates, routes, aircraft, and Monte Carlo trials; runtime and hardware are not reported.",
) -> dict:
    parameters = [item["symbol"] for item in variables if item["role"] == "parameter"]
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
            "reason": (
                "All displayed equations assigned to this component were visually reconciled against bounded page proxies and focused formula review."
                if equations
                else "The paper gives this comparison and recommendation layer in prose, plots, and reported statistics without another displayed equation."
            ),
        },
        "objectives": [
            purpose,
            "Produce a traceable search-time, completion, posterior, comparison, or recommendation output without treating the simulation as field validation.",
        ],
        "constraints": [
            "Retain the paper's rectangular search domain, units, aircraft class, sensor range, time step, stopping rule, and trial population at every interface.",
            "Preserve visible notation defects as source evidence; any repaired implementation must be labeled as an extension rather than silently substituted.",
        ],
        "conditions": {
            "initial": condition("present", "The crash prior, search-plane start, aircraft specifications, path state, and simulation controls must be initialized before this component runs."),
            "boundary": condition("present", "The component is bounded by the stated open-ocean rectangular domain, idealized weather and sensor assumptions, and any 24-hour uncertainty-model cap."),
            "equilibrium": condition("not-applicable", "The paper uses finite path recurrences and Monte Carlo trials rather than an equilibrium solution."),
        },
        "parameter_estimation": {
            "status": "partial",
            "method": parameter_method,
            "parameters": parameters,
        },
        "algorithm": {
            "status": "partial",
            "steps": algorithm_steps,
            "software": [
                "The paper describes simulated path generation and statistical summaries but gives no source code, environment, time step, pseudo-random generator, or seed."
            ],
            "convergence_criteria": convergence,
        },
        "assumptions": assumptions,
        "identifiability_feasibility": {"status": feasibility, "analysis": feasibility_analysis},
        "handoff_outputs": outputs,
        "validation_refs": validation_refs,
        "computational_cost": cost,
        "strengths": [
            "The component has a source-ordered input-to-output role in the paper's containment-to-path-to-detection-to-decision chain.",
            "Equations, reported statistics, and downstream handoffs remain distinguishable from later warnings and independent improvements.",
        ],
        "limitations": limitations,
        "missing_details": missing_details,
    }


def build_models() -> dict:
    eq = {
        1: equation(1, 11, "P = P(C) * P(D)", r"P=P(C)P(D)", ["P", "P_C", "P_D"], "Factor total discovery probability into containment and conditional detection."),
        2: equation(2, 15, "r = kappa alpha", r"r=\kappa\alpha", ["r", "kappa", "alpha"], "Convert cruise altitude and glide ratio into maximum glide range."),
        3: equation(3, 15, "L = v tau", r"L=v\tau", ["L", "v", "tau"], "Convert aircraft speed and the crash-time uncertainty interval into along-track distance."),
        4: equation(4, 23, "S_i - (x_crash,y_crash) < d", r"\vec S_i-(x_{\mathrm{crash}},y_{\mathrm{crash}})<d", ["S_i", "x_crash", "y_crash", "d"], "State the printed discovery stopping rule; the source visibly omits a norm.", "medium"),
        5: equation(5, 23, "95% CI = [mu - 2(SE), mu + 2(SE)], SE = sigma/sqrt(n)", r"95\%\ \mathrm{CI}=[\mu-2\mathrm{SE},\mu+2\mathrm{SE}],\quad \mathrm{SE}=\frac{\sigma}{\sqrt n}", ["CI", "mu", "SE", "sigma", "n"], "Summarize simulated discovery times with the paper's approximate mean interval."),
        6: equation(6, 24, "S_0=(0,0); S_i=S_(i-1)+v Delta t R/|R|", r"\vec S_0=(0,0),\quad \vec S_i=\vec S_{i-1}+v\Delta t\frac{\vec R}{|\vec R|}", ["S_0", "S_i", "v", "delta_t", "R"], "Advance an unbounded isotropic random walk by one fixed-length step."),
        7: equation(7, 26, "if S_ix>L+2r union S_ix<0: S_(i+1)=S_i+v Delta t Norm(<(L+2r)/2-S_ix,0>)", r"S_{ix}>L+2r\ \cup\ S_{ix}<0:\ \vec S_{i+1}=\vec S_i+v\Delta t\operatorname{Norm}\!\left(\left\langle\frac{L+2r}{2}-S_{ix},0\right\rangle\right)", ["S_ix", "L", "r", "S_i", "v", "delta_t"], "Redirect an out-of-bounds horizontal step toward the rectangle center line.", "medium"),
        8: equation(8, 26, "if S_iy>r union S_iy<-r: S_(i+1)=S_i+v Delta t Norm(<0,-S_iy>)", r"S_{iy}>r\ \cup\ S_{iy}<-r:\ \vec S_{i+1}=\vec S_i+v\Delta t\operatorname{Norm}(\langle0,-S_{iy}\rangle)", ["S_iy", "r", "S_i", "v", "delta_t"], "Redirect an out-of-bounds vertical step toward the flight-path axis.", "medium"),
        9: equation(9, 29, "if d_A>d_B: S_(i+1)=S_i+v Delta t Norm(15R/|R|+Norm(A-S_i))", r"d_A>d_B:\ \vec S_{i+1}=\vec S_i+v\Delta t\operatorname{Norm}\!\left(15\frac{\vec R}{|\vec R|}+\operatorname{Norm}(A-\vec S_i)\right)", ["d_A", "d_B", "S_i", "v", "delta_t", "R", "A"], "Bias the bounded random step toward endpoint A when A is farther."),
        10: equation(10, 29, "if d_A<=d_B: S_(i+1)=S_i+v Delta t Norm(15R/|R|+Norm(B-S_i))", r"d_A\le d_B:\ \vec S_{i+1}=\vec S_i+v\Delta t\operatorname{Norm}\!\left(15\frac{\vec R}{|\vec R|}+\operatorname{Norm}(B-\vec S_i)\right)", ["d_A", "d_B", "S_i", "v", "delta_t", "R", "B"], "Bias the bounded random step toward endpoint B when B is at least as far."),
        11: equation(11, 32, "S_(i+1)=S_i+v Delta t epsilon <1,0>", r"\vec S_{i+1}=\vec S_i+v\Delta t\,\varepsilon\langle1,0\rangle", ["S_i", "v", "delta_t", "epsilon"], "Move horizontally along one descending stripe."),
        12: equation(12, 32, "at S_ix>=L+2r union S_ix<=0: epsilon=-epsilon; S_(i+1)=S_i+<0,-2d>", r"S_{ix}\ge L+2r\ \cup\ S_{ix}\le0:\ \varepsilon\leftarrow-\varepsilon,\quad \vec S_{i+1}=\vec S_i+\langle0,-2d\rangle", ["S_ix", "L", "r", "epsilon", "S_i", "d"], "Reverse direction at a vertical boundary and descend by one radar diameter.", "medium"),
        13: equation(13, 35, "S_(i+1)=S_i+v Delta t epsilon <1,0>", r"\vec S_{i+1}=\vec S_i+v\Delta t\,\varepsilon\langle1,0\rangle", ["S_i", "v", "delta_t", "epsilon"], "Move horizontally along one spiral-ordered stripe."),
        14: equation(14, 35, "C(u)=2(-1)^u u", r"C(u)=2(-1)^u u", ["C_u", "u"], "Generate alternating stripe displacement indices around the flight path.", "medium"),
        15: equation(15, 35, "at either x-edge: S_(i+1)=S_i+<0,epsilon C(j)> -> (j=j+1,epsilon=-epsilon)", r"\vec S_{i+1}=\vec S_i+\langle0,\varepsilon C(j)\rangle\ \longrightarrow\ (j\leftarrow j+1,\ \varepsilon\leftarrow-\varepsilon)", ["S_i", "epsilon", "C_j", "j"], "Apply the next alternating vertical transition at each horizontal edge.", "medium"),
        16: equation(16, 38, "S_(i+1)=S_i+v Delta t epsilon Norm(<1,pi cos((2pi/lambda)S_ix)>)", r"\vec S_{i+1}=\vec S_i+v\Delta t\,\varepsilon\operatorname{Norm}\!\left(\left\langle1,\pi\cos\!\left(\frac{2\pi}{\lambda}S_{ix}\right)\right\rangle\right)", ["S_i", "v", "delta_t", "epsilon", "lambda", "S_ix"], "Step along the tangent direction of the paper's sinusoidal search path."),
        17: equation(17, 38, "C(u)=2(-1)^(u-1)u", r"C(u)=2(-1)^{u-1}u", ["C_u", "u"], "Generate alternating transitions between sinusoidal stripes.", "medium"),
        18: equation(18, 38, "at either x-edge: S_(i+1)=S_i+C(j)r -> (j=j+1,epsilon=-epsilon)", r"\vec S_{i+1}=\vec S_i+C(j)r\ \longrightarrow\ (j\leftarrow j+1,\ \varepsilon\leftarrow-\varepsilon)", ["S_i", "C_j", "r", "j", "epsilon"], "Retain the source's printed sinusoidal edge-transition update, including its scalar-vector ambiguity.", "low"),
        19: equation(19, 42, "P'(C)=P(C)(1-P(D_u))/((1-P(C))+P(C)(1-P(D_u)))=P(C)(1-P(D_u))/(1-P(C)P(D_u))<P(C)", r"P'(C)=\frac{P(C)[1-P(D_u)]}{[1-P(C)]+P(C)[1-P(D_u)]}=\frac{P(C)[1-P(D_u)]}{1-P(C)P(D_u)}<P(C)", ["P_C_post", "P_C", "P_Du"], "Reduce the posterior probability of a searched cell after an unsuccessful pass."),
        20: equation(20, 42, "P'(C_i)=P(C_i)/(1-P(C)P(D_u))>P(C_i)", r"P'(C_i)=\frac{P(C_i)}{1-P(C)P(D_u)}>P(C_i)", ["P_Ci_post", "P_Ci", "P_C", "P_Du"], "Renormalize unsearched cells upward after a missed detection elsewhere."),
        21: equation(21, 42, "P(D_u)=P(R)P(O|R)", r"P(D_u)=P(R)P(O\mid R)", ["P_Du", "P_R", "P_O_given_R"], "Factor imperfect discovery into radar detection and operator recognition."),
        22: equation(22, 43, "P(O) approximately 1; P(O|R) approximately 1", r"P(O)\approx1,\quad P(O\mid R)\approx1", ["P_O", "P_O_given_R"], "Round the cited operator success rate to certainty for the simulation."),
        23: equation(23, 43, "P(D_u)=P(R)P(O|R) approximately 0.8", r"P(D_u)=P(R)P(O\mid R)\approx0.8", ["P_Du", "P_R", "P_O_given_R"], "Fix the uncertain-discovery probability used by the Bayesian and spiral trials."),
    }

    models = [
        model(1, 11, "2.5 Searching for a Lost Object", "containment-times-detection search probability", "Define discovery success as the product of containment and detection so location priors and sensor performance remain separate.", [variable("P", "total discovery probability", "probability", "Probability that the search discovers the lost aircraft.", "output"), variable("P_C", "containment probability", "probability", "Probability the target lies in the searched area.", "input"), variable("P_D", "detection probability", "probability", "Probability the target is detected conditional on containment.", "input")], ["P_C", "P_D"], ["P"], [eq[1]], ["Containment and detection can be combined through the stated product for the paper's search event."], ["Specify the searched area and its containment probability.", "Specify conditional sensor discovery probability and multiply the two factors."], ["The later uncertainty model separates containment-cell updates from imperfect radar/operator discovery."], ["The source does not fully state the conditional-independence semantics behind the product."], ["A calibrated containment prior, sensor likelihood, dependence structure, and field truth set."]),
        model(2, 15, "3.3 Lost Aircraft Profile", "glide-and-time rectangular search geometry", "Construct a rectangular candidate region from aircraft glide reach and the distance traveled during the uncertain failure interval.", [variable("r", "glide range", "miles", "Maximum forward distance during an unpowered glide.", "output"), variable("kappa", "glide ratio", "forward distance per unit descent", "Aircraft glide ratio.", "parameter"), variable("alpha", "cruising altitude", "feet", "Representative altitude at failure.", "input"), variable("L", "uncertain along-track distance", "miles", "Distance flown during the failure-time uncertainty window.", "output"), variable("v", "lost-aircraft airspeed", "miles per hour", "Representative lost-aircraft speed.", "input"), variable("tau", "failure-time uncertainty", "hours", "Half-hour interval used to bound possible failure time.", "parameter")], ["alpha", "kappa", "v", "tau"], ["r", "L"], [eq[2], eq[3]], ["The aircraft maintains representative cruise speed until failure and then glides according to a constant ratio.", "The path is straight and the candidate region can be represented by a rectangle of size (L+2r) by 2r."], ["Compute r and L.", "Extend the path by r at both ends and by r on both sides."], ["The Boeing 777 example yields L=320 miles, r=100 miles, and a 520 by 200 mile region."], ["Feet-to-miles conversion is omitted from Equation 2 and the rectangular approximation ignores turns, winds, currents, and failure-state dynamics."], ["Unit conversion, trajectory uncertainty, wind/current displacement, terrain/coast effects, and a calibrated failure-time prior."]),
        model(3, 22, "5.1 Normal Distribution / Completed Simulation / Statistical Analysis", "Gaussian containment and Monte Carlo discovery-time harness", "Sample crash locations uniformly along the flight direction and normally across it, stop a path at detection, and summarize discovery time with histograms and approximate confidence intervals.", [variable("x_crash", "crash x coordinate", "miles", "Simulated along-track crash coordinate.", "state"), variable("y_crash", "crash y coordinate", "miles", "Simulated cross-track crash coordinate.", "state"), variable("S_i", "search-plane position", "miles in local coordinates", "Plane position at simulation step i.", "state"), variable("d", "sensor sight radius", "miles", "Detection radius fixed at 10 miles for P-8 trials.", "parameter"), variable("CI", "reported confidence interval", "hours", "Approximate interval for the simulated mean discovery time.", "output"), variable("mu", "sample mean", "hours", "Mean time among the observations included in a summary.", "output"), variable("SE", "standard error", "hours", "Reported standard error of the mean.", "intermediate"), variable("sigma", "sample standard deviation", "hours", "Spread of simulated discovery times.", "intermediate"), variable("n", "included sample count", "count", "Number of discovery-time observations used for the interval.", "input")], ["x_crash", "y_crash", "S_i", "d", "n"], ["mu", "CI"], [eq[4], eq[5]], ["Crash x is uniform over the rectangular path length and y follows the selected normal containment model.", "The P-8 travels at constant speed and detects a target whenever the printed distance condition is met.", "Simulated completion times are summarized as if repeated draws support the paper's approximate interval."], ["Generate a crash point from the containment distribution.", "Advance the selected route until the stopping rule fires.", "Repeat the declared trial count and compute mean, median, standard deviation, standard error, and the printed interval."], ["Figures 7 and 12-24 expose crash samples and route-specific time distributions.", "Reported mean/median differences reveal skew and permit within-harness comparisons."], ["Equation 4 lacks a norm, and Equation 5 is an approximate interval rather than a stated hypothesis test.", "No code, time step, seeds, distribution parameters, convergence analysis, or incident holdout is supplied."], ["Exact Gaussian parameters and truncation, random generator/seed, time step, failure handling, estimator definition, and raw trial output."]),
        model(4, 24, "Solution 5.1.1", "unbounded isotropic random walk", "Generate a baseline search path from normalized random vectors without enforcing the search boundary.", [variable("S_0", "initial search position", "miles", "Origin of the simulated route.", "input"), variable("S_i", "search position", "miles", "Position at step i.", "state"), variable("v", "printed step speed", "miles per hour", "Speed symbol used in the recurrence, although the search-plane table defines v_s.", "parameter"), variable("delta_t", "simulation time step", "hours", "Unreported time increment per route step.", "parameter", "unspecified"), variable("R", "random direction vector", "dimensionless vector", "Random vector normalized to a direction.", "state")], ["S_0", "v", "delta_t"], ["S_i"], [eq[6]], ["Each random vector is isotropic and independent and the plane may leave the candidate rectangle."], ["Initialize at the origin.", "Draw and normalize R, advance one fixed-length step, and stop on discovery."], ["The source reports that most unbounded random trials do not finish, establishing an intentionally poor baseline."], ["The route wastes effort outside the containment area and uses v rather than the defined search speed v_s."], ["Direction distribution, time step, seed, maximum duration, completion count, and raw paths."]),
        model(5, 26, "Solution 5.1.2", "boundary-corrected random walk", "Keep random search steps inside the rectangular domain by redirecting out-of-bounds coordinates toward its center axes.", [variable("S_i", "search position", "miles", "Position at step i.", "state"), variable("S_ix", "search x coordinate", "miles", "Horizontal coordinate checked against the rectangle.", "state"), variable("S_iy", "search y coordinate", "miles", "Vertical coordinate checked against the rectangle.", "state"), variable("L", "uncertain path length", "miles", "Along-track failure interval length.", "input"), variable("r", "glide range", "miles", "Half-height and endpoint extension of the rectangle.", "input"), variable("v", "printed step speed", "miles per hour", "Speed symbol used in the recurrence.", "parameter"), variable("delta_t", "simulation time step", "hours", "Unreported route increment.", "parameter", "unspecified"), variable("detection_time", "bounded-random discovery time", "hours", "Trial completion time.", "output")], ["S_i", "L", "r", "v", "delta_t"], ["detection_time"], [eq[7], eq[8]], ["A coordinate crossing a boundary is redirected by the printed horizontal or vertical rule."], ["Draw a random step.", "When x or y lies outside its bound, substitute the corresponding return vector.", "Stop at detection and repeat 100 trials."], ["The 100-trial mean is 42.7105 hours, median 24.425, and reported interval [33.2348,52.1862]."], ["The union symbol is used as logical OR and corner behavior/order of the two rules is not specified."], ["Corner precedence, equality behavior, normalized-vector definition, time step, seeds, and raw trials."]),
        model(6, 29, "Solution 5.1.3", "endpoint-weighted bounded random walk", "Bias random motion toward the farther endpoint to spend more time near the normal distribution's center while retaining stochastic exploration.", [variable("d_A", "distance to endpoint A", "miles", "Current distance to A.", "state"), variable("d_B", "distance to endpoint B", "miles", "Current distance to B.", "state"), variable("S_i", "search position", "miles", "Position at step i.", "state"), variable("v", "printed step speed", "miles per hour", "Step-speed symbol.", "parameter"), variable("delta_t", "simulation time step", "hours", "Unreported route increment.", "parameter", "unspecified"), variable("R", "random direction vector", "dimensionless vector", "Random exploratory direction.", "state"), variable("A", "left endpoint", "miles in local coordinates", "One flight-path endpoint.", "input"), variable("B", "right endpoint", "miles in local coordinates", "Other flight-path endpoint.", "input"), variable("detection_time", "weighted-random discovery time", "hours", "Trial completion time.", "output")], ["S_i", "A", "B", "v", "delta_t"], ["detection_time"], [eq[9], eq[10]], ["The normalized endpoint vector is added to a random component weighted by the fixed factor 15."], ["Compare d_A and d_B.", "Bias the next normalized step toward the farther endpoint.", "Apply boundary control, stop on discovery, and repeat 100 trials."], ["The mean is 37.5575 hours and median 16.6; its reported interval overlaps the bounded-random interval."], ["The weight 15 is unsupported and the interval comparison is treated as a significance test without a direct paired or two-sample test."], ["Weight calibration, boundary integration, seed, raw paired trials, and a valid comparison test."]),
        model(7, 32, "Solution 5.1.4", "descending boustrophedon stripes", "Sweep parallel horizontal tracks from the high-probability center downward with vertical spacing equal to one radar diameter.", [variable("S_i", "search position", "miles", "Current route coordinate.", "state"), variable("S_ix", "search x coordinate", "miles", "Horizontal coordinate used for turns.", "state"), variable("v", "printed step speed", "miles per hour", "Horizontal search speed symbol.", "parameter"), variable("delta_t", "simulation time step", "hours", "Unreported horizontal step interval.", "parameter", "unspecified"), variable("epsilon", "horizontal direction", "plus or minus one", "Alternating direction sign.", "state"), variable("L", "uncertain path length", "miles", "Rectangle length component.", "input"), variable("r", "glide range", "miles", "Rectangle endpoint extension.", "input"), variable("d", "sensor sight radius", "miles", "Half of the stripe separation.", "parameter"), variable("detection_time", "descending-stripe discovery time", "hours", "Trial completion time.", "output")], ["S_i", "L", "r", "v", "delta_t", "d"], ["detection_time"], [eq[11], eq[12]], ["The normal prior is symmetric but the route begins at the center and covers only one side before the other is discussed through alternatives."], ["Traverse one horizontal stripe.", "At an x boundary reverse direction and descend by 2d.", "Stop at discovery and repeat 100 trials."], ["Mean 7.10273 hours, median 7.031, reported interval [6.62073,7.58473]."], ["The route order gives asymmetric discovery times across the symmetric prior and ignores turn duration."], ["Start coordinate, upper/lower completion rule, turn kinematics, exact time step, seed, and raw trials."]),
        model(8, 35, "Solution 5.1.5", "center-out alternating spiral stripes", "Sweep horizontal tracks in an alternating center-out order to cover the highest-probability bands before the tails.", [variable("S_i", "search position", "miles", "Current route coordinate.", "state"), variable("v", "printed step speed", "miles per hour", "Horizontal step speed.", "parameter"), variable("delta_t", "simulation time step", "hours", "Unreported route increment.", "parameter", "unspecified"), variable("epsilon", "horizontal direction", "plus or minus one", "Alternating direction sign.", "state"), variable("C_u", "alternating stripe function", "printed as dimensionless", "Function that orders stripes about the center.", "intermediate"), variable("u", "stripe function index", "count", "Input to C.", "state"), variable("C_j", "next stripe displacement", "printed as miles by context", "C evaluated at transition index j.", "intermediate"), variable("j", "transition index", "count", "Counts horizontal boundary transitions.", "state"), variable("detection_time", "ideal spiral discovery time", "hours", "Trial completion time.", "output")], ["S_i", "v", "delta_t"], ["detection_time"], [eq[13], eq[14], eq[15]], ["The normal prior is symmetric about the flight path and stripe order should alternate around that center."], ["Traverse a horizontal stripe.", "At each x edge use C(j) to select the next alternating vertical transition.", "Repeat until detection over 100 trials."], ["Mean 3.62286 hours, median 3.113, reported interval [3.05261,4.19311], the best ideal one-plane result."], ["C(u) has no sight-range factor or declared unit, and Equation 15 does not resolve whether C is a coordinate or displacement."], ["Physical scaling of C, transition order, edge behavior, turn time, time step, seeds, and raw trials."]),
        model(9, 38, "Solution 5.1.6", "sinusoidal center-out stripes", "Replace straight horizontal stripes with a sinusoidal tangent-stepping path while preserving alternating center-out coverage.", [variable("S_i", "search position", "miles", "Current route coordinate.", "state"), variable("S_ix", "search x coordinate", "miles", "x value inside the cosine tangent.", "state"), variable("v", "printed step speed", "miles per hour", "Path step speed.", "parameter"), variable("delta_t", "simulation time step", "hours", "Unreported route increment.", "parameter", "unspecified"), variable("epsilon", "path direction", "plus or minus one", "Alternating direction sign.", "state"), variable("lambda", "sine wavelength", "miles", "Wavelength fixed to 2d by the prose.", "parameter"), variable("C_u", "alternating stripe function", "printed as dimensionless", "Function used to change sine stripes.", "intermediate"), variable("u", "stripe function index", "count", "Input to C.", "state"), variable("C_j", "next stripe transition", "printed as dimensionless", "C evaluated at transition j.", "intermediate"), variable("r", "printed transition multiplier", "miles", "Glide-range symbol reused in Equation 18.", "input"), variable("j", "transition index", "count", "Counts edge transitions.", "state"), variable("detection_time", "sinusoidal discovery time", "hours", "Trial completion time.", "output")], ["S_i", "v", "delta_t", "lambda", "r"], ["detection_time"], [eq[16], eq[17], eq[18]], ["A sine path of amplitude d and wavelength 2d is intended to cover the plane without leaving sensor gaps."], ["Advance along the normalized tangent vector.", "At an x edge apply the printed C(j)r transition and update j and epsilon.", "Repeat 100 discovery trials."], ["Mean 6.44989 hours, median 4.489, and reported interval [5.23314,7.66664]."], ["Equation 18 adds a scalar to a vector, reuses glide range r, and updates epsilon although the next recurrence's semantics are unclear."], ["Correct vector transition, amplitude/wavelength derivation, physical stripe spacing, time step, seed, and raw paths."]),
        model(10, 41, "5.2 Normal Distribution with Discovery Uncertainty", "Bayesian missed-detection grid update", "Update searched-cell containment after imperfect detection, choose the next high-probability stripe, and compare adaptive Bayesian and fixed spiral routes under a 24-hour cap.", [variable("P_C_post", "searched-cell posterior", "probability", "Posterior of cell C after an unsuccessful search.", "output"), variable("P_C", "searched-cell prior", "probability", "Prior mass of cell C.", "input"), variable("P_Du", "uncertain discovery probability", "probability", "Probability that radar and operator jointly detect the target.", "parameter"), variable("P_Ci_post", "other-cell posterior", "probability", "Renormalized posterior for cell i.", "output"), variable("P_Ci", "other-cell prior", "probability", "Prior mass of an unsearched cell.", "input"), variable("P_R", "radar detection probability", "probability", "Probability the radar registers the aircraft.", "parameter"), variable("P_O", "operator recognition probability", "probability", "Unconditional operator recognition term printed in Equation 22.", "parameter"), variable("P_O_given_R", "operator recognition given radar", "probability", "Conditional recognition probability.", "parameter"), variable("posterior_grid", "updated containment grid", "probability distribution", "Cell probabilities after each unsuccessful pass.", "output"), variable("detection_time", "conditional discovery time", "hours", "Time among trials discovered before the cap.", "output"), variable("success_rate", "24-hour completion proportion", "proportion", "Fraction of all trials discovered by 24 hours.", "output")], ["P_C", "P_Ci", "P_R", "P_O", "P_O_given_R"], ["P_C_post", "P_Ci_post", "posterior_grid", "detection_time", "success_rate"], [eq[19], eq[20], eq[21], eq[22], eq[23]], ["The containment field is discretized into cells even though cell size is not defined.", "Radar succeeds with probability 0.8 and a cited 0.97 operator rate is rounded to one.", "An unsuccessful search lowers the visited cell and proportionally raises all others.", "Trials stop at discovery or 24 hours."], ["Initialize the Gaussian containment grid.", "Search the current highest-priority stripe/cell.", "On a miss apply Equations 19-20 and renormalize.", "Repeat 500 trials and report success proportion plus conditional discovery-time statistics."], ["Bayesian B777 finds 475/500 and uncertain spiral 399/500; C172 Bayesian finds 411/500.", "Posterior maps in Figures 25-28 expose the center-first update sequence."], ["Cell discretization and likelihood independence are omitted, operator detection is rounded upward, and means exclude capped failures.", "The Bayesian B777 reported lower CI bound is arithmetically inconsistent with its mean and SE."], ["Cell dimensions, normalization checks, posterior code, likelihood calibration, censored-time analysis, raw outcomes, seeds, and field validation."]),
        model(11, 49, "6 Solution Stability / 7 Results / 8 Conclusion", "scenario stability and conditional decision synthesis", "Compare target classes, one versus two search planes, route distributions, completion proportions, and rescue timing to recommend Bayesian adaptive search with explicit scope limits.", [variable("aircraft_class", "lost-aircraft class", "categorical", "Boeing 777 or Cessna 172 scenario.", "input"), variable("search_plane_count", "search-plane count", "count", "One- or two-plane resource scenario.", "input"), variable("route", "candidate route", "categorical", "Random, bounded, weighted, stripe, spiral, sinusoidal, or Bayesian route.", "input"), variable("mean_time", "reported mean discovery time", "hours", "Mean among included trial times.", "output"), variable("median_time", "reported median discovery time", "hours", "Median among included trial times.", "output"), variable("success_rate", "completion proportion", "proportion", "Fraction found before any cap.", "output"), variable("survival_benchmark", "rescue benchmark", "hours", "The 18-hour cold-water survival comparison used in the recommendation.", "parameter"), variable("recommendation", "search recommendation", "categorical decision", "Bayesian-adjusted center-first search with resource adaptation.", "output")], ["aircraft_class", "search_plane_count", "route", "survival_benchmark"], ["mean_time", "median_time", "success_rate", "recommendation"], [], ["Within-model simulations are comparable only when target, prior, sensor, time cap, and handling of failures are aligned.", "Cold-water survival is used as a decision benchmark rather than as a modeled physiological distribution."], ["Collect route-level distribution summaries and success proportions.", "Repeat selected tests for Cessna and two-plane scenarios.", "Compare evidence against the rescue benchmark and state a bounded recommendation."], ["Cessna and two-plane scenarios test limited transfer; Figures 34-36 compare intervals and Figure 37 supplies the external survival context."], ["Overlapping intervals are misused as significance tests, capped failures are excluded from means, and the stability checks change several mechanisms without a factorial design."], ["Common estimand across capped and uncapped routes, survival/censoring analysis, paired trials, hypothesis tests, scenario matrix, operational constraints, and incident holdout."]),
    ]

    edges = [
        (1, 3, "Containment and detection factors define the discovery criterion used by the simulation harness."),
        (2, 3, "Glide range r and uncertain distance L define the 520-by-200-mile B777 simulation domain and crash prior support."),
        (3, 4, "The common crash sampler and detection-time statistics evaluate the unbounded random route."),
        (3, 5, "The same crash samples, rectangle, and stopping rule evaluate bounded random search."),
        (5, 6, "Boundary control is retained while endpoint-directed bias modifies the bounded random route."),
        (3, 7, "The common ideal-detection harness evaluates descending stripes."),
        (7, 8, "Straight stripe coverage is reordered center-out using alternating vertical transitions."),
        (8, 9, "The center-out ordering is retained while each stripe becomes sinusoidal."),
        (3, 10, "The Gaussian containment prior and detection harness become a discrete posterior grid with imperfect discovery."),
        (8, 10, "The ideal spiral route supplies the fixed-path comparator under discovery uncertainty."),
        (10, 11, "Bayesian/spiral success proportions and conditional time distributions enter the final comparison."),
        (7, 11, "Descending-stripe results enter the route comparison and two-plane extension."),
        (8, 11, "Ideal spiral results establish the best one-plane ideal-detection baseline."),
        (9, 11, "Sinusoidal results provide the final systematic-route alternative."),
        (2, 11, "Aircraft geometry is changed for the C172 transfer check."),
    ]
    return {
        "schema_version": 2,
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "review_status": "validated",
        "models": models,
        "dependency_edges": [
            {
                "from_model_id": models[source - 1]["model_id"],
                "to_model_id": models[target - 1]["model_id"],
                "handoff": handoff,
            }
            for source, target, handoff in edges
        ],
    }


def validate(record: dict) -> None:
    equations = [item for model_unit in record["models"] for item in model_unit["governing_equations"]]
    if len(record["models"]) != 11:
        raise ValueError(f"expected 11 models, found {len(record['models'])}")
    if len(equations) != 23:
        raise ValueError(f"expected 23 equations, found {len(equations)}")
    if [item["label"] for item in equations] != [f"({index})" for index in range(1, 24)]:
        raise ValueError("equations must exactly cover labels (1)-(23) in source order")
    if len(record["dependency_edges"]) != 15:
        raise ValueError("expected 15 typed model dependency edges")


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    record = build_models()
    validate(record)
    STAGE.mkdir(parents=True)
    target = STAGE / "models.json"
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "models": len(record["models"]), "equations": 23, "dependency_edges": len(record["dependency_edges"]), "stage": str(target), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
