from __future__ import annotations

"""Build the source-checked G5 model record for Queue 113 without promotion."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2016-42745-4dc9ed2b"
TYPE = "B"
YEAR = "2016"
SHORT = "42745"
SHA256 = "4dc9ed2b48ba9415c26b12506e36e0a144491324a4f44445d6ae8083ad7c5b46"
STAGE = ROOT / "tmp/q113-model-stage-v2"


def variable(symbol: str, name: str, unit: str, definition: str, role: str, status: str = "explicit-defined") -> dict:
    return {"symbol": symbol, "normalized_name": name, "unit": unit, "definition": definition, "role": role, "source_status": status}


def equation(index: int, page: int, label: str, source_expression: str, normalized_latex: str, symbols: list[str], purpose: str, confidence: str = "high", source_type: str = "paper") -> dict:
    return {
        "equation_id": f"EQ-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "page": page,
        "label": label,
        "source_expression": source_expression,
        "normalized_latex": normalized_latex,
        "purpose": purpose,
        "variable_symbols": symbols,
        "source_type": source_type,
        "visual_checked": True,
        "transcription_confidence": confidence,
    }


def condition(status: str, *details: str) -> dict:
    return {"status": status, "details": list(details)}


def model(index: int, page: int, section: str, family: str, purpose: str, variables: list[dict], inputs: list[str], outputs: list[str], equations: list[dict], assumptions: list[str], steps: list[str], validation_refs: list[str], limitations: list[str], missing_details: list[str], *, parameter_method: str = "The paper mixes cited values, hand-set values, educated guesses, algebraic constructions, and one-factor scenarios; it does not report a jointly estimated or uncertainty-propagated parameter set.", feasibility: str = "partial", feasibility_analysis: str = "Equations, figures, scenario outputs, and payoff tables make the intended route inspectable, but no code, frozen parameter file, seed manifest, raw run array, calibration dataset, or independent validation package is supplied.", convergence: str = "Finite annual loops and scenario grids are described. Random repetition count, seed protocol, sampling error, grid convergence, optimizer tolerance, and statistical stopping rules are omitted.", cost: str = "Cost depends on a one-million-cell field, annual removal-growth-launch-collision updates, repeated random placement, three alternatives, scenario reruns, and payoff inspection; runtime and hardware are not reported.") -> dict:
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
        "equation_status": {"status": "present" if equations else "omitted-by-paper", "reason": "Every assigned displayed or prose-reconstructed equation was reconciled against the rendered source." if equations else "This component is specified through prose, figures, scenario outputs, or payoff tables rather than a separate displayed equation."},
        "objectives": [purpose, "Return a source-traceable financial, debris, collision, scenario, strategic, or decision output without upgrading simulated or hand-set evidence to empirical validation."],
        "constraints": ["Keep year, rate convention, monetary unit, removal technology, altitude band, debris population, grid resolution, random protocol, scenario setting, and payoff source explicit.", "Retain printed self-reference, symbol conflicts, missing growth terms, and unidentified parameters as source evidence; any corrected implementation is a separate extension."],
        "conditions": {
            "initial": condition("present", "A 2016-2030 horizon, firm structure, launch series, satellite value, commission, removal parameters, initial debris field, Gamma representation, and policy scenario must be declared before the relevant component runs."),
            "boundary": condition("present", "The source ignores discounting, reduces orbital geometry to two dimensions, uses a binary same-cell collision rule, hand-sets occupancy and several costs, and reports only local one-factor scenarios."),
            "equilibrium": condition("present" if index == 9 else "not-applicable", "Model 9 inspects pure-strategy best responses in two finite payoff matrices." if index == 9 else "This component uses identities, finite simulation updates, scenario reruns, or recommendation synthesis rather than an equilibrium solve."),
        },
        "parameter_estimation": {"status": "partial", "method": parameter_method, "parameters": parameters},
        "algorithm": {"status": "partial", "steps": steps, "software": ["The paper names MATLAB for simulation but supplies no source code, version, dependencies, input archive, seed list, run log, or raw output arrays."], "convergence_criteria": convergence},
        "assumptions": assumptions,
        "identifiability_feasibility": {"status": feasibility, "analysis": feasibility_analysis},
        "handoff_outputs": outputs,
        "validation_refs": validation_refs,
        "computational_cost": cost,
        "strengths": ["The component has a typed place in the opportunity -> accounting -> debris field -> collision -> alternatives -> scenarios -> game -> recommendation chain.", "Observed context, assumed inputs, algebraic definitions, simulated outputs, plotted comparisons, and strategic claims remain distinguishable."],
        "limitations": limitations,
        "missing_details": missing_details,
    }


def build_models() -> dict:
    eq = {
        1: equation(1, 9, "annual net income", "N_t = R_t - C_t", r"N_t=R_t-C_t", ["N_t", "R_t", "C_t"], "Define annual commercial performance."),
        2: equation(2, 10, "accumulated net income", "N_T = sum from i=1 to t of N_i, t <= t_max", r"N_T=\sum_{i=1}^{t}N_i,\quad t\le t_{\max}", ["N_T", "N_t", "i", "t"], "Aggregate annual profit through the current year."),
        3: equation(3, 10, "insurance revenue", "R_t = n_t * w * alpha%", r"R_t=n_t w\alpha", ["R_t", "n_t", "w", "alpha"], "Compute premium revenue from launches, insured value, and commission.", "medium"),
        4: equation(4, 10, "total cost split", "C_t = C_1t + C_2t", r"C_t=C_{1t}+C_{2t}", ["C_t", "C_1t", "C_2t"], "Separate removal cost from collision compensation."),
        5: equation(5, 11, "generic removal-cost family", "C_1t = sum over all types of p_t q_t rho", r"C_{1t}=\sum_{a\in\mathcal A}p_{a,t}q_{a,t}\rho_a", ["C_1t", "A", "a", "p_at", "q_at", "rho_a"], "Activate the cost of each selected removal type.", "medium"),
        6: equation(6, 17, "land-based cost family", "C_1t = C_land,t + C_0; C_land,t = p_land,t q_land,t", r"C_{1t}=C_{\mathrm{land},t}+C_0,\quad C_{\mathrm{land},t}=p_{\mathrm{land},t}q_{\mathrm{land},t}", ["C_1t", "C_land_t", "C0", "p_land_t", "q_land_t"], "Specialize removal cost to the land alternative."),
        7: equation(7, 17, "space-based cost family", "C_1t = C_space,t; C_space,t = p_space,t q_space,t", r"C_{1t}=C_{\mathrm{space},t},\quad C_{\mathrm{space},t}=p_{\mathrm{space},t}q_{\mathrm{space},t}", ["C_1t", "C_space_t", "p_space_t", "q_space_t"], "Specialize removal cost to the space alternative."),
        8: equation(8, 18, "combined removal cost", "C_1t = C_land,t + C_space,t + C_0", r"C_{1t}=C_{\mathrm{land},t}+C_{\mathrm{space},t}+C_0", ["C_1t", "C_land_t", "C_space_t", "C0"], "Combine both technology costs."),
        9: equation(9, 11, "expected compensation cost", "C_2t = Pr(t) * epsilon * n_(t-1) * delta", r"C_{2t}=Pr(t)\,\varepsilon n_{t-1}\delta", ["C_2t", "Pr_t", "epsilon", "n_t_minus_1", "delta"], "Route collision probability to expected monetary compensation."),
        10: equation(10, 11, "Cobb-Douglas utility", "U(x1,x2) = mu x1^c x2^d", r"U(x_1,x_2)=\mu x_1^c x_2^d", ["U", "x1", "x2", "mu", "c", "d"], "Introduce the utility form used to construct compensation."),
        11: equation(11, 11, "normalized utility family", "k = c/(c+d); U' = mu' x1^k x2^(1-k)", r"k=\frac{c}{c+d},\quad U'=\mu' x_1^k x_2^{1-k}", ["k", "c", "d", "U_prime", "mu_prime", "x1", "x2"], "Normalize the two utility exponents through a monotone transform."),
        12: equation(12, 12, "single-collision compensation", "x1=w, x2=alpha w, k=0.5; delta = mu w alpha^(1/2)", r"x_1=w,\quad x_2=\alpha w,\quad k=0.5,\quad \delta=\mu w\alpha^{1/2}", ["x1", "x2", "w", "alpha", "k", "delta", "mu"], "Turn satellite value and commission into the paper's compensation amount.", "medium"),
        13: equation(13, 13, "Gamma radial family", "X ~ Gamma(alpha, beta)", r"X\sim\operatorname{Gamma}(\alpha_G,\beta_G)", ["X", "alpha_G", "beta_G"], "Represent the radial debris-density shape; the paper gives no fitted parameter values."),
        14: equation(14, 15, "printed debris removal update, repeated on page 18", "Q_t = Q_t - (q_land,t + epsilon q_space,t)", r"Q_t=Q_t-(q_{\mathrm{land},t}+\varepsilon q_{\mathrm{space},t})", ["Q_t", "q_land_t", "epsilon", "q_space_t"], "Record the source's removal update exactly, including its self-reference and omitted growth term.", "medium"),
        15: equation(15, 16, "collision-frequency estimate", "Pr(t) = collisions in year t / satellites launched in year t", r"Pr(t)=\frac{K_t}{n_t}", ["Pr_t", "K_t", "n_t"], "Estimate annual collision probability from same-cell overlap frequency."),
        16: equation(16, 16, "launch-count recurrence reconstructed from prose", "n_1 = 110; n_t = 1.05 n_(t-1)", r"n_1=110,\quad n_t=1.05n_{t-1}", ["n_1", "n_t", "n_t_minus_1"], "Encode the stated initial launch count and annual five-percent increase.", "medium", "reconstructed"),
        17: equation(17, 16, "law-of-large-numbers claim", "Pr(t) converges in probability to b", r"Pr(t)\xrightarrow{p}b", ["Pr_t", "b"], "State the source's convergence claim for repeated random simulation.", "medium"),
    }

    models = [
        model(1, 9, "4.2 projected income and revenue", "time-dependent business accounting", "Compute annual and accumulated net income from launch premiums and total modeled cost.",
            [variable("N_t", "annual net income", "currency per year", "Revenue minus modeled cost in year t.", "output"), variable("N_T", "accumulated net income", "currency", "Sum of annual net income through year t.", "output"), variable("R_t", "annual insurance revenue", "currency per year", "Premium income from launches in year t.", "intermediate"), variable("C_t", "annual total cost", "currency per year", "Removal plus compensation cost.", "input"), variable("C_1t", "annual removal cost", "currency per year", "Removal-cost component supplied by Model 2.", "input"), variable("C_2t", "annual compensation cost", "currency per year", "Collision-compensation component supplied by Model 3.", "input"), variable("n_t", "satellites launched in year t", "count per year", "Annual insured launch count.", "input"), variable("w", "insured satellite value", "currency per satellite", "Guaranteed value per launched satellite.", "parameter"), variable("alpha", "insurance commission", "rate or percent", "Premium rate, with inconsistent percent convention in the source.", "parameter"), variable("i", "summation year", "index", "Index for annual income aggregation.", "state", "inferred-from-equation"), variable("t", "current year index", "index", "Current simulation year.", "state", "inferred-from-equation")],
            ["n_t", "w", "alpha", "C_t", "t"], ["R_t", "N_t", "N_T"], [eq[i] for i in range(1, 5)],
            ["All launchers buy collision insurance.", "The insurer and debris-removal firm are one company.", "Revenue is represented by premiums and modeled costs by removal and compensation.", "The time value of money is ignored."],
            ["Set the 15-year horizon and launch path.", "Compute R_t.", "Receive C_t from the cost components.", "Compute N_t and accumulate N_T."],
            ["Figures 7, 9, and 11 plot accumulated profit for the three alternatives.", "Insurance-rate Figures 21-24 rerun this accounting path."],
            ["The alpha-percent convention is ambiguous; demand, taxes, capital cost, operating overhead, policy uptake, and discounting are absent."],
            ["Frozen yearly inputs, currency year, alpha numeric convention, complete revenue categories, discount rate, and cash-flow workbook are absent."]),

        model(2, 10, "4.2 and 6.1-6.3 removal costs", "technology-activated removal cost", "Compute generic and alternative-specific land, space, and combined removal costs.",
            [variable("C_1t", "annual removal cost", "currency per year", "Removal component of total cost.", "output"), variable("A", "removal technology set", "set", "Land and space technology types.", "input", "inferred-from-equation"), variable("a", "technology index", "index", "Selected removal type.", "state", "inferred-from-equation"), variable("p_at", "unit removal price", "currency per operation or unit", "Price associated with type a in year t.", "parameter"), variable("q_at", "type-specific removal quantity or operations", "count", "Quantity whose meaning conflicts across sections.", "input"), variable("rho_a", "technology activation", "binary", "Whether type a is selected.", "parameter"), variable("C_land_t", "land removal cost", "currency per year", "Recurring land-system cost.", "intermediate"), variable("C_space_t", "space removal cost", "currency per year", "Recurring space-system cost.", "intermediate"), variable("C0", "land initial investment", "currency", "One-time cost in prose but added without a first-year indicator.", "parameter"), variable("p_land_t", "land unit price", "currency per operation or unit", "Land-specific unit price.", "parameter"), variable("q_land_t", "land removal quantity or operations", "count", "Land-specific quantity.", "input"), variable("p_space_t", "space unit price", "currency per operation or unit", "Space-specific unit price.", "parameter"), variable("q_space_t", "space removal quantity or operations", "count", "Space-specific quantity.", "input")],
            ["A", "p_at", "q_at", "rho_a", "C0", "p_land_t", "q_land_t", "p_space_t", "q_space_t"], ["C_land_t", "C_space_t", "C_1t"], [eq[i] for i in range(5, 9)],
            ["Removal cost is price times quantity or operation count.", "A binary coefficient activates each technology.", "Land initial investment C0 is included in the printed yearly cost expression."],
            ["Select land, space, or both.", "Set unit prices and quantities.", "Compute component costs.", "Add C0 according to the printed source expression.", "Pass C_1t to total cost."],
            ["Pages 17-18 specialize the generic formula for all three alternatives.", "Figures 7-12 compare their resulting paths."],
            ["q_t changes meaning between captured amount and operation count; C0 may be charged every year despite being called initial; units and price years are not reconciled."],
            ["Complete cost table, quantity definition, inflation, maintenance, launch cadence, failure rate, first-year indicator, and procurement uncertainty are absent."]),

        model(3, 11, "4.2 collision compensation", "probability-weighted utility compensation", "Convert simulated collision probability into annual expected compensation cost through a Cobb-Douglas construction.",
            [variable("C_2t", "annual collision compensation cost", "currency per year", "Expected collision-payment component.", "output"), variable("Pr_t", "annual collision probability", "probability", "Output from the same-cell simulation.", "input"), variable("epsilon", "space catcher capacity", "debris per catcher", "Source symbol unexpectedly multiplied into compensation exposure.", "parameter"), variable("n_t_minus_1", "previous-year launches", "count per year", "Exposure proxy used by the source.", "input"), variable("delta", "single-collision compensation", "currency per collision", "Utility-derived payment amount.", "output"), variable("U", "Cobb-Douglas utility", "utility units", "Utility before normalization.", "intermediate"), variable("U_prime", "normalized utility", "utility units", "Monotone transform with exponents summing to one.", "intermediate"), variable("x1", "first utility good", "currency", "Set to satellite value w.", "intermediate"), variable("x2", "second utility good", "currency", "Set to alpha times w and described inconsistently.", "intermediate"), variable("mu", "utility scale", "unspecified", "Uncalibrated utility or compensation scale.", "parameter"), variable("mu_prime", "transformed utility scale", "unspecified", "Scale after normalization.", "parameter"), variable("c", "first utility exponent", "dimensionless", "Original Cobb-Douglas exponent.", "parameter"), variable("d", "second utility exponent", "dimensionless", "Original Cobb-Douglas exponent.", "parameter"), variable("k", "normalized first exponent", "dimensionless", "c divided by c+d, then set to 0.5.", "parameter"), variable("w", "satellite value", "currency", "Insured satellite value.", "input"), variable("alpha", "insurance commission", "rate or percent", "Commission entering x2 and delta.", "input")],
            ["Pr_t", "epsilon", "n_t_minus_1", "w", "alpha", "mu", "c", "d"], ["x1", "x2", "k", "U", "U_prime", "delta", "C_2t"], [eq[i] for i in range(9, 13)],
            ["Cobb-Douglas utility can proxy risk attitude.", "x1=w, x2=alpha w, and k=0.5.", "Previous-year launches proxy collision exposure."],
            ["Set utility variables and exponents.", "Compute delta.", "Receive Pr(t).", "Multiply probability, exposure, epsilon, and delta."],
            ["The compensation formula is visible on page 11 and delta on page 12.", "The insurance-rate sweep changes alpha while holding the remaining simulation fixed."],
            ["epsilon is defined as debris removed per space catcher and is dimensionally unrelated to insured collision count; x2 and mu lack economic calibration; only n_(t-1) represents exposure."],
            ["In-orbit insured stock, retirement, policy term, deductibles, payout data, risk-aversion calibration, utility-to-currency mapping, and alpha convention are absent."]),

        model(4, 12, "5.1-5.3 Gamma debris field", "2D layered stochastic occupancy field", "Reduce orbital debris to four Gamma-weighted rings in a 1000 by 1000 binary matrix.",
            [variable("X", "radial debris coordinate", "grid or altitude coordinate", "Random coordinate represented by a Gamma family.", "state"), variable("alpha_G", "Gamma shape", "dimensionless", "Shape parameter, distinct from insurance alpha.", "parameter"), variable("beta_G", "Gamma rate or scale", "inverse coordinate or coordinate", "Unspecified parameter convention.", "parameter"), variable("M", "debris occupancy matrix", "1000 by 1000 binary cells", "Synthetic two-dimensional field.", "output"), variable("rings", "four radial layers", "cell bands", "Concentric layer partition.", "input"), variable("occupancy", "filled-cell rate", "fraction", "Hand-set approximately 15 percent.", "parameter"), variable("Q_0", "initial debris count", "occupied cells", "Initial modeled inventory.", "output")],
            ["alpha_G", "beta_G", "rings", "occupancy"], ["X", "M", "Q_0"], [eq[13]],
            ["Relevant 1-10 cm debris is represented in two dimensions.", "Debris is locally uniform within selected altitude bands.", "The Gamma curve sufficiently resembles the NASA height-density plot.", "About 15 percent of valid cells are filled and each cell is binary."],
            ["Create the grid and exclude Earth and atmosphere.", "Partition four rings.", "Assign Gamma mass by ring.", "Randomly set valid cells to one until the occupancy target is reached."],
            ["Figures 1-5 compare NASA context, the Gamma family, and the generated field.", "The unnumbered summary plot previews a similar synthetic field."],
            ["No Gamma parameters, fit criterion, ring boundaries, unit mapping, measured 1-10 cm dataset, or occupancy calibration is supplied; 2D cell occupancy is not physical orbital density."],
            ["NASA data rows, fitting code, integration limits, cell-to-altitude conversion, object-size filter, multiple occupancy, and seed protocol are absent."]),

        model(5, 15, "5.4-5.5 debris removal and growth", "annual debris-state transition", "Update debris inventory under land and space removal and exogenous debris growth.",
            [variable("Q_t", "debris inventory in year t", "occupied cells or debris count", "Annual state, printed on both sides of the source equation.", "output"), variable("q_land_t", "land removal amount or operations", "count", "Land-based removal term.", "input"), variable("q_space_t", "space removal operations or amount", "count", "Space-based term.", "input"), variable("epsilon", "debris removed per space catcher", "debris per catcher", "Capacity multiplier.", "parameter"), variable("g", "debris growth rule", "count or rate per year", "Described as linear while a five-percent annual rate is also used.", "parameter"), variable("M_t", "annual debris matrix", "binary cells", "Field after removals and insertions.", "state")],
            ["Q_t", "q_land_t", "q_space_t", "epsilon", "g", "M_t"], ["Q_t", "M_t"], [eq[14]],
            ["Debris does not naturally disappear without intervention.", "Land operates mainly at 600-800 km and space at 800-1000 km.", "New debris is randomly inserted according to the Gamma pattern.", "Two exceptional historic collision events are removed from the growth fit."],
            ["Remove randomly accessible debris.", "Apply the stated but incompletely specified growth rule.", "Insert new occupied cells by the Gamma pattern.", "Return Q_t and M_t."],
            ["Figures 13-16 show ending fields under growth scenarios.", "The combined Q_t expression is repeated on page 18."],
            ["Q_t is self-referential rather than lagged, the full growth-plus-removal recurrence is never printed, linear growth conflicts with a percentage recurrence, and tail events are deliberately excluded."],
            ["Initial state year, Q_(t-1) convention, fitted growth equation, exceptional-event rationale, collision-created debris, natural decay, insertion conflicts, and mass conservation are absent."]),

        model(6, 15, "5.6 launching and collision process", "same-cell Monte Carlo collision frequency", "Place a growing number of satellites in the binary field and estimate collision frequency from debris-cell overlap.",
            [variable("n_1", "initial annual launches", "count", "Source-set value 110.", "parameter"), variable("n_t", "launches in year t", "count per year", "Five-percent recurring projection.", "input"), variable("n_t_minus_1", "previous-year launches", "count per year", "Prior recurrence state.", "state"), variable("K_t", "same-cell collisions in year t", "count", "Number of launched satellite points landing in occupied cells.", "output"), variable("Pr_t", "estimated collision probability", "probability", "K_t divided by n_t.", "output"), variable("b", "claimed true collision probability", "probability", "Limit named in the LLN statement.", "parameter"), variable("M_t", "debris occupancy field", "binary cells", "Field receiving satellite points.", "input"), variable("seed", "random seed", "integer", "Mentioned but not enumerated.", "parameter", "unspecified")],
            ["n_1", "n_t_minus_1", "M_t", "seed"], ["n_t", "K_t", "Pr_t"], [eq[i] for i in range(15, 18)],
            ["Launch points are placed randomly in the field.", "A satellite and debris in the same cell constitute a collision.", "Repeated random runs justify convergence to a true probability."],
            ["Project n_t from n_(t-1).", "Randomly place n_t satellites.", "Count occupied-cell overlaps K_t.", "Compute Pr(t).", "Repeat with unspecified seeds and pass Pr(t) to compensation cost."],
            ["Figure 6 supplies historical launch context.", "The source states multiple run-times and a law-of-large-numbers rationale."],
            ["Grid scale determines collision probability; orbital inclination, velocity, cross-section, time exposure, active stock, and avoidance are absent; no replicate count or interval supports the convergence claim."],
            ["Seed list, repetitions, random generator, placement distribution, cell scale, launch-orbit distribution, observed collision calibration, sampling error, and convergence plot are absent."]),

        model(7, 16, "6 three-alternative simulation", "common-horizon alternative evaluation", "Run land-only, space-only, and combined removal over 15 years on aligned profit and debris metrics.",
            [variable("alternative", "removal alternative", "land, space, or combined", "Technology selection.", "input"), variable("C_1t", "removal cost path", "currency per year", "Output from Model 2.", "input"), variable("C_2t", "compensation cost path", "currency per year", "Output from Model 3.", "input"), variable("Pr_t", "collision-probability path", "probability per year", "Output from Model 6.", "input"), variable("Q_t", "remaining debris path", "count", "Output from Model 5.", "input"), variable("N_t", "annual net income", "currency per year", "Output from Model 1.", "input"), variable("N_T", "accumulated net income", "currency", "Decision metric.", "output"), variable("comparison", "aligned alternative comparison", "decision table and plots", "Profit/debris tradeoff across three runs.", "output")],
            ["alternative", "C_1t", "C_2t", "Pr_t", "Q_t", "N_t"], ["N_T", "comparison"], [],
            ["All alternatives share the 2016-2030 horizon and unreported fixed parameters.", "Profit and remaining debris are sufficient for the commercial choice."],
            ["Run the annual field and financial loop for land.", "Repeat for space.", "Repeat for combined removal.", "Compare N_T and Q_t on the same horizon."],
            ["Figures 7-12 provide paired profit and ending-field outputs.", "The prose reports fewer than 1000 net new debris for land and more than 2000 removed for the combination."],
            ["No common parameter table, uncertainty intervals, replicate distributions, statistical comparison, discounted cash flow, or observed baseline makes the option ranking robust."],
            ["Exact yearly arrays, run counts, common random numbers, alternative budgets, ending values for every metric, and comparison criterion are absent."]),

        model(8, 19, "7 what-if and sensitivity scenarios", "one-factor scenario suite", "Perturb debris growth, reusable-rocket lifetime, and insurance commission around the selected alternative.",
            [variable("growth_rate", "debris growth setting", "percent per year or logarithmic case", "Five, four, three, two percent and a logarithmic trend.", "input"), variable("ending_debris", "ending debris inventory", "count", "Reported output by growth scenario.", "output"), variable("rocket_lifetime", "reusable launches per rocket", "uses", "Three, six, nine, or twelve.", "input"), variable("alpha", "insurance commission", "percent", "Three, four, five, or six percent.", "input"), variable("accumulated_profit", "ending accumulated profit", "currency", "Scenario financial output.", "output"), variable("break_even", "break-even year", "year index", "First nonnegative accumulated-profit point as interpreted.", "output"), variable("fixed_protocol", "held-fixed model state", "scenario contract", "All inputs other than the named factor.", "parameter", "unspecified")],
            ["growth_rate", "rocket_lifetime", "alpha", "fixed_protocol"], ["ending_debris", "accumulated_profit", "break_even"], [],
            ["Each scenario changes only the named factor.", "The combined alternative remains the relevant baseline.", "Discrete local settings are treated as sufficient for recommendation."],
            ["Rerun growth settings and record ending debris.", "Rerun rocket lifetimes and record profit paths.", "Rerun alpha values and record profit and break-even.", "State only local response and untested dimensions."],
            ["Figures 13-16 cover growth, Figures 17-20 rocket lifetime, and Figures 21-24 alpha.", "The printed outputs allow checking the 8004-6374 arithmetic and the alpha=3 percent prose conflict."],
            ["All are sparse one-factor sweeps without joint uncertainty, stochastic intervals, threshold bracketing, demand response, or structural alternatives; two reported interpretations contain arithmetic or sign errors."],
            ["All fixed values, run pairing, repeat counts, output arrays, uncertainty, scenario likelihoods, decision loss, and outside-range behavior are absent."]),

        model(9, 22, "8 policy game", "two-player finite strategic game", "Compare owner insurance and firm removal strategies before and after a policy-induced payoff change.",
            [variable("S_owner", "satellite-owner strategy set", "three strategies", "Uninsured, half insured, or fully insured.", "input"), variable("S_firm", "insurer-remover strategy set", "three strategies", "Do nothing, remove some, or remove considerably.", "input"), variable("P_base", "baseline payoff matrix", "3 by 3 payoff pairs", "Supplied owner and firm payoffs before policy.", "input"), variable("P_policy", "policy payoff matrix", "3 by 3 payoff pairs", "Supplied payoffs after policy.", "input"), variable("NE_base", "baseline pure Nash equilibria", "strategy pairs", "Two best-response intersections.", "output"), variable("NE_policy", "policy pure Nash equilibrium", "strategy pair", "One best-response intersection.", "output"), variable("pareto_claim", "within-matrix payoff comparison", "boolean and payoff deltas", "Both players improve at the new equilibrium relative to the old equilibria.", "output")],
            ["S_owner", "S_firm", "P_base", "P_policy"], ["NE_base", "NE_policy", "pareto_claim"], [],
            ["The game has complete information.", "Players choose simultaneously from the displayed strategies.", "The supplied payoff numbers encode all relevant consequences and policy effects."],
            ["Enumerate both strategy sets.", "Check row and column best responses in P_base.", "Record two pure equilibria.", "Repeat for P_policy.", "Compare both players' equilibrium payoffs."],
            ["Both unnumbered page-23 matrices were visually checked cell by cell.", "The two baseline equilibria and unique policy equilibrium agree with best-response inspection."],
            ["Payoff units and derivation from prior models are absent; the regulator is not a player; policy cost, compliance, mixed equilibria, externalities, and uncertainty are omitted."],
            ["Payoff construction table, model-to-payoff mapping, utility convention, policy instrument, enforcement cost, alternative equilibria, and social-welfare definition are absent."],
            parameter_method="The payoff entries are asserted to come from prior model values but no derivation, unit, calibration, or uncertainty record is printed.",
            convergence="All nine cells can be inspected for pure-strategy best responses; no mixed-strategy calculation, equilibrium-selection rule, or uncertainty analysis is reported.",
            cost="A 3 by 3 pure best-response check is trivial; the substantive missing cost is constructing and validating the payoff matrices."),

        model(10, 23, "9-10 integrated decision and repair", "evidence-bounded decision synthesis", "Synthesize commercial, parameter, and policy decisions while preserving the paper's repair directions and evidence limits.",
            [variable("commercial_choice", "removal-business decision", "decision", "Conditional selection of the combined alternative.", "output"), variable("rate_choice", "insurance-rate decision", "percent recommendation", "Paper's four-to-five-percent guidance.", "output"), variable("policy_choice", "regulatory decision", "decision", "Industrial standards and international policy recommendation.", "output"), variable("model_evidence", "retained model outputs", "typed evidence bundle", "Profit, debris, scenario, and payoff results.", "input"), variable("warnings", "source and validation boundaries", "risk register", "Formula, calibration, stochastic, financial, scenario, and policy limits.", "input"), variable("repairs", "future model extensions", "work program", "3D geometry, resource allocation, and start-time optimization plus reproducibility repairs.", "output")],
            ["model_evidence", "warnings"], ["commercial_choice", "rate_choice", "policy_choice", "repairs"], [],
            ["The displayed scenario and payoff outputs are treated as sufficient for source-level recommendations.", "Claim strength must be bounded by the missing calibration and validation record."],
            ["Separate commercial, parameter, and policy outputs.", "Trace each to its supporting model or table.", "Attach formula, data, uncertainty, and scope warnings.", "State repairs without silently altering source results."],
            ["Pages 23-24 state conclusions, strengths, and future improvements.", "The full formula, figure, table, and warning record supports a bounded synthesis."],
            ["The source overstates reliability and practical certainty relative to educated guesses, unseeded simulation, omitted discounting, local sweeps, and uncalibrated payoff matrices."],
            ["Independent data, implementation, external validation, uncertainty propagation, 3D dynamics, resource optimization, optimal start timing, and policy-cost evaluation remain future work."],
            parameter_method="No new parameter estimation occurs; this layer classifies source results, evidence strength, and proposed repairs.",
            convergence="Decision synthesis terminates after all required model, visual, scenario, strategic, and warning records are present.",
            cost="The main cost is evidence reconciliation across formulas, simulation outputs, scenario plots, payoff tables, and provenance rather than numerical solution."),
    ]

    edges = [
        (1, 7, "Annual revenue and net-income identities receive scenario-specific total cost and produce the common profit metric."),
        (2, 7, "Alternative-specific removal costs enter each 15-year simulation."),
        (3, 7, "Expected compensation cost enters total cost for every alternative."),
        (4, 5, "The Gamma occupancy field supplies the debris state updated by removal and growth."),
        (4, 6, "The binary field supplies occupied cells for satellite overlap counting."),
        (5, 6, "The annually updated debris field is the collision simulator's state."),
        (6, 3, "Estimated Pr(t) is multiplied into expected collision compensation."),
        (5, 7, "Remaining debris Q_t supplies the environmental alternative metric."),
        (6, 7, "Collision-frequency paths couple the physical simulation to the financial comparison."),
        (7, 8, "The combined alternative becomes the baseline for growth, rocket, and rate reruns."),
        (2, 8, "Rocket lifetime perturbs the space-removal cost interface."),
        (1, 8, "Insurance alpha perturbs premium revenue and break-even timing."),
        (3, 8, "Insurance alpha also enters the constructed compensation amount."),
        (5, 8, "Growth scenarios perturb the debris transition and ending inventory."),
        (7, 9, "Prior commercial outputs are asserted to inform the payoff matrices, though the mapping is missing."),
        (1, 9, "Owner insurance and firm revenue logic motivate the game strategies and payoffs."),
        (2, 9, "Removal alternatives motivate the firm's three game strategies."),
        (7, 10, "The aligned alternative comparison supplies the commercial recommendation."),
        (8, 10, "Local scenario responses supply rate, technology, and growth-policy qualifications."),
        (9, 10, "The checked equilibrium shift supplies the within-matrix policy conclusion."),
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
    if len(equations) != 17:
        raise ValueError(f"expected 17 displayed or prose-reconstructed equation records, found {len(equations)}")
    if [item["equation_id"] for item in equations] != [f"EQ-B-2016-42745-{index:03d}" for index in range(1, 18)]:
        raise ValueError("equation records must retain source order")
    if len(record["dependency_edges"]) != 20:
        raise ValueError("expected 20 typed model dependency edges")


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    record = build_models()
    validate(record)
    STAGE.mkdir(parents=True)
    target = STAGE / "models.json"
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "models": len(record["models"]), "equations": 17, "dependency_edges": len(record["dependency_edges"]), "stage": str(target), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
