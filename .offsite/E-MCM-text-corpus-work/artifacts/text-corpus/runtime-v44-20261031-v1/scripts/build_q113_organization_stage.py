from __future__ import annotations

"""Create Queue 113 G4 organization evidence from validated language units."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2016-42745-4dc9ed2b"
LANGUAGE = ROOT / "tmp/q113-language-stage-v3/language.json"
STAGE = ROOT / "tmp/q113-organization-stage-v1"


CONTRACTS = [
    {
        "source_headings": ["MCM/ICM Summary Sheet"], "chapter": "abstract", "pages": [1, 1],
        "input": "A debris-removal business question, two intervention classes, collision exposure, and a possible regulatory response.",
        "rhetorical_job": "Compress the threat, firm role, three-model architecture, principal results, recommendation, and parameter caveat.",
        "analytical_job": "Preview annual profit accounting, Gamma-grid collision simulation, three removal alternatives, three scenario families, and a policy game.",
        "output": "A conditional claim that a combined insurer-remover can find a commercial opportunity under declared rates and assumptions.",
        "handoff": "The executive summary expands each alternative and scenario before the main paper defines the machinery.",
        "transition_cue": "Threat -> firm -> economic model -> collision model -> policy model -> recommendation -> boundary.",
    },
    {
        "source_headings": ["Executive Summary"], "chapter": "problem-restatement", "pages": [2, 3],
        "input": "The compact three-model promise and a private firm that both insures launches and removes debris.",
        "rhetorical_job": "Expand the method, alternative, sensitivity, policy, and recommendation sequence without introducing equations.",
        "analytical_job": "Distinguish land, space, and combined runs; lower-growth regulation; recyclable rockets; insurance-rate changes; and the payoff-matrix intervention.",
        "output": "A decision-facing comparison of commercial and regulatory conclusions.",
        "handoff": "The title and contents expose where each component is developed and reviewed.",
        "transition_cue": "Business setup -> model roles -> three alternatives -> what-if cases -> policy -> recommendations.",
    },
    {
        "source_headings": ["Strategies to Eliminating Space Debris", "Contents"], "chapter": "title", "pages": [4, 5],
        "input": "The executive summary's promised time-dependent evaluation, collision model, alternatives, scenarios, and game.",
        "rhetorical_job": "Make the complete source order inspectable before technical details.",
        "analytical_job": "Index methods, terminology, financial model, collision model, results, what-if scenarios, game theory, conclusions, improvements, and references.",
        "output": "A 23-page internal roadmap nested inside 26 physical PDF pages.",
        "handoff": "The introduction converts the physical problem into a four-part commercial-opportunity test.",
        "transition_cue": "Front matter -> context and methods -> two models -> evidence -> decisions -> provenance.",
    },
    {
        "source_headings": ["1 Introduction"], "chapter": "introduction", "pages": [6, 6],
        "input": "More than 500,000 debris pieces, collision damage, candidate removal technologies, and uneven costs and benefits.",
        "rhetorical_job": "Turn a physical hazard into a measurable commercial-opportunity question for a private firm.",
        "analytical_job": "Decompose opportunity into demand, means, application, and benefit; treat the last two as the unresolved modeling target.",
        "output": "A time-dependent profitability objective with named stakeholders and technologies.",
        "handoff": "Existing Methods classifies the technologies that later create removal costs and capacities.",
        "transition_cue": "Hazard evidence -> removal need -> opportunity definition -> missing elements -> model objective.",
    },
    {
        "source_headings": ["2 Existing Methods", "2.1 Land Based", "2.2 Space Based"], "chapter": "problem-analysis", "pages": [6, 7],
        "input": "Laser Broom, Huff-and-Puff, Snagging and Moving, and Solar Sail proposals.",
        "rhetorical_job": "Classify interventions by deployment location and compare operating mechanisms and practical limits.",
        "analytical_job": "Separate fixed from recurring cost, working altitude, removal capacity, launch dependence, and collision or targeting risk.",
        "output": "Two alternative families used by the cost and debris-update models.",
        "handoff": "Terminology and notation define the financial and physical interfaces used to combine them.",
        "transition_cue": "Land mechanisms -> space mechanisms -> cost/capability tradeoff -> formal symbols.",
    },
    {
        "source_headings": ["3 Terminologies", "Notations"], "chapter": "notation", "pages": [7, 8],
        "input": "Insurance, compensation, utility, debris, launch, removal, probability, and game concepts.",
        "rhetorical_job": "Stabilize terms and symbols before they cross the economic, simulation, and policy models.",
        "analytical_job": "Define annual and cumulative income, two cost terms, commission, collision probability, debris state, removal quantities, and space-device capacity.",
        "output": "A typed interface for N_t, R_t, C_t, N_T, n_t, w, alpha, C_1t, C_2t, p_t, q_t, Pr(t), delta, Q_t, and epsilon.",
        "handoff": "Model One composes the financial quantities into revenue, cost, compensation, and profit.",
        "transition_cue": "Business definitions -> utility definition -> symbol table -> annual accounting identity.",
    },
    {
        "source_headings": ["4 Model One", "4.1 Assumptions", "4.2 Model Establishment"], "chapter": "model-establishment", "pages": [9, 12],
        "input": "A 2016-2030 horizon, launch counts, satellite value, insurance rate, removal choices, collision probability, and compensation parameters.",
        "rhetorical_job": "Make commercial opportunity measurable through annual and accumulated net income.",
        "analytical_job": "Decompose income into premium revenue, removal cost, and collision compensation; derive compensation through a Cobb-Douglas construction.",
        "output": "N_t and N_T for any removal alternative once Pr(t) and removal quantities are supplied.",
        "handoff": "Model Two supplies the time-dependent collision probability and debris inventory.",
        "transition_cue": "Assumptions -> accounting identity -> revenue -> cost split -> utility-based compensation -> probability handoff.",
    },
    {
        "source_headings": ["5 Model Two", "5.1 Assumptions", "5.2 Gamma Distribution"], "chapter": "assumptions", "pages": [12, 13],
        "input": "A three-dimensional orbital debris field and a need for a tractable collision-frequency simulation.",
        "rhetorical_job": "Declare the physical reduction and distributional rationale before constructing a numerical field.",
        "analytical_job": "Restrict the hazard to 1-10 cm debris, assume local uniformity and persistence, reduce the orbit to two dimensions, and select a Gamma radial family by visual similarity.",
        "output": "A two-dimensional radial representation with explicit but weakly calibrated assumptions.",
        "handoff": "The distribution section discretizes the representation into four rings and a binary matrix.",
        "transition_cue": "Hazard class -> motion assumptions -> 3D difficulty -> 2D reduction -> Gamma choice.",
    },
    {
        "source_headings": ["5.3 Modeling the Spatial Distribution of Space Debris"], "chapter": "data-preprocessing", "pages": [14, 14],
        "input": "A Gamma radial shape, four altitude layers, a 1000 by 1000 domain, and a hand-set occupancy rate.",
        "rhetorical_job": "Convert the distributional story into a field that can be changed by removal, growth, and launches.",
        "analytical_job": "Assign Gamma mass to rings, exclude the Earth and atmosphere, randomly fill about 15 percent of valid cells, and encode occupancy as zero or one.",
        "output": "A synthetic binary debris matrix.",
        "handoff": "The annual simulation processes remove cells, add debris, launch satellites, and count overlaps.",
        "transition_cue": "Grid -> layers -> Gamma mass -> random occupancy -> simulated field.",
    },
    {
        "source_headings": ["5.4 Removing Process", "5.5 Growing Process", "5.6 Launching and Collision Process"], "chapter": "algorithm", "pages": [15, 16],
        "input": "The binary field, land and space working bands, debris growth, annual launches, and a same-cell collision rule.",
        "rhetorical_job": "Order the physical and stochastic operations that generate the financial model's collision input.",
        "analytical_job": "Randomly remove accessible debris, add linearly described but five-percent-recurring debris, grow launches from 110, count co-occupied cells, and normalize by launches.",
        "output": "Annual Q_t and Pr(t) paths for a removal scenario.",
        "handoff": "Results combine those paths with the corresponding removal-cost equations.",
        "transition_cue": "State -> remove -> grow -> launch -> overlap -> annual collision frequency.",
    },
    {
        "source_headings": ["6 Results", "6.1 Land Based", "6.2 Space Based", "6.3 Combination"], "chapter": "results", "pages": [16, 19],
        "input": "A common 15-year horizon and three removal-cost and debris-update regimes.",
        "rhetorical_job": "Compare alternatives on aligned profit and remaining-debris outputs before choosing one.",
        "analytical_job": "Run land-only, space-only, and combined scenarios; interpret break-even behavior, inner-layer control, ending debris, and accumulated profit.",
        "output": "A recommendation for the combined alternative under the paper's parameter settings.",
        "handoff": "What-if sections perturb growth, reusable-launch lifetime, and insurance rate around that choice.",
        "transition_cue": "Land result -> space result -> combined result -> shared tradeoff -> selected baseline.",
    },
    {
        "source_headings": ["7 Some What If Scenarios", "7.1 International Policies"], "chapter": "sensitivity-analysis", "pages": [19, 20],
        "input": "The combined alternative and debris-growth settings of five, four, three, two percent plus a logarithmic trend.",
        "rhetorical_job": "Translate lower growth into ending inventories and a bounded case for international regulation.",
        "analytical_job": "Hold the model fixed, rerun the growth process, compare ending debris counts and marginal reductions, and interpret diminishing changes.",
        "output": "A local policy scenario linking stronger growth control with less ending debris.",
        "handoff": "The next scenario changes space-removal launch cost through reusable-rocket lifetime.",
        "transition_cue": "Policy lever -> growth levels -> ending debris -> marginal comparison -> recommendation boundary.",
    },
    {
        "source_headings": ["7.2 Recyclable Rocket"], "chapter": "robustness-verification", "pages": [20, 21],
        "input": "The space-based cost structure and reusable-rocket lifetimes of three, six, nine, and twelve uses.",
        "rhetorical_job": "Check whether a plausible launch technology change materially alters accumulated profit.",
        "analytical_job": "Rerun the financial path for four lifetimes, compare maximum and minimum profit, and relate the limited effect to compensation liability.",
        "output": "A local claim that rocket reuse affects profit less than the dominant modeled costs.",
        "handoff": "The insurance-rate sweep changes the revenue and compensation interface directly.",
        "transition_cue": "Future technology -> lifetime levels -> profit paths -> effect size -> mechanism.",
    },
    {
        "source_headings": ["7.3 Sensitivity Analysis on alpha"], "chapter": "sensitivity-robustness", "pages": [21, 22],
        "input": "Insurance rates of three, four, five, and six percent under otherwise fixed simulation conditions.",
        "rhetorical_job": "Connect the central business parameter to break-even timing and accumulated profit.",
        "analytical_job": "Compare four profit paths, estimate the reported marginal profit and break-even shift, and infer a recommended rate range.",
        "output": "A local commission threshold claim, not a joint uncertainty or market-demand result.",
        "handoff": "Game theory then changes insurer and owner incentives through a policy payoff matrix.",
        "transition_cue": "Parameter rationale -> rate sweep -> paths -> threshold -> recommendation -> local scope.",
    },
    {
        "source_headings": ["8 A Game Theory Approach"], "chapter": "model-improvement", "pages": [22, 23],
        "input": "Satellite-owner insurance choices, firm removal choices, assumed complete information, and two 3 by 3 payoff matrices.",
        "rhetorical_job": "Turn the commercial analysis into a strategic policy argument with inspectable equilibria.",
        "analytical_job": "Enumerate strategies, check best responses in the baseline matrix, alter payoffs under policy, identify the new equilibrium, and compare both players' payoffs.",
        "output": "A policy-induced equilibrium shift that is Pareto-improving only within the supplied matrices.",
        "handoff": "Conclusions restate the commercial, rate, and policy decisions and then name model repairs.",
        "transition_cue": "Players -> strategies -> baseline payoffs -> equilibria -> policy matrix -> new equilibrium -> bounded welfare claim.",
    },
    {
        "source_headings": ["9 Conclusions", "10 Strengths and Further Improvements"], "chapter": "strengths-limitations", "pages": [23, 24],
        "input": "The three alternative runs, three scenario families, two payoff matrices, and the paper's own model assessment.",
        "rhetorical_job": "Separate decision claims from claimed strengths and concrete future repairs.",
        "analytical_job": "Restate commercial opportunity, combined removal, commission, standards, and regulation; then identify 3D geometry, resource allocation, and optimal-start-time extensions.",
        "output": "A capability-and-repair contract for transfer rather than an unconditional solution claim.",
        "handoff": "References expose the technology, launch, debris, distribution, cost, and policy provenance.",
        "transition_cue": "Findings -> recommendations -> claimed strengths -> limitations -> affected outputs -> repairs.",
    },
    {
        "source_headings": ["References"], "chapter": "references", "pages": [25, 26],
        "input": "Business, removal-technology, launch, debris, Gamma-distribution, cost, game, and policy claims.",
        "rhetorical_job": "Expose which external sources support context and inputs and what cannot be reproduced.",
        "analytical_job": "Map eighteen citations to claims while recording missing retrieval freezes, datasets, parameters, code, seeds, run logs, and payoff derivations.",
        "output": "A provenance boundary rather than a complete reproduction package.",
        "handoff": "The paper ends without executable MATLAB, frozen model inputs, raw simulation output, or a policy-cost record.",
        "transition_cue": "Claim family -> citation -> model interface -> archival gap -> reproduction boundary.",
    },
]


def chain(paragraph: int, move: str, claim: str, support: str, qualifier: str, consequence: str, next_link: str, unit_ids: list[str]) -> dict:
    return {"paragraph": paragraph, "dominant_move": move, "claim": claim, "support": support, "qualifier": qualifier, "consequence": consequence, "next_link": next_link, "language_unit_ids": unit_ids}


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    language = json.loads(LANGUAGE.read_text(encoding="utf-8"))
    if language.get("review_status") != "validated":
        raise ValueError("G1-G3 language stage must be validated before G4")
    units_by_chapter: dict[str, list[str]] = {}
    for unit in language["units"]:
        units_by_chapter.setdefault(unit["chapter"], []).append(unit["language_unit_id"])
    contracts = []
    for item in CONTRACTS:
        contract = dict(item)
        contract["linked_language_unit_ids"] = units_by_chapter[item["chapter"]]
        contract["coverage_decision"] = "positive-contract-complete"
        contracts.append(contract)
    au = units_by_chapter["abstract"]
    iu = units_by_chapter["introduction"]
    result = {
        "paper_id": PAPER_ID,
        "source_task_context": {
            "official_problem_statement_status": "reconstructed-from-paper",
            "paper_explicit_task": "Evaluate whether space-debris removal creates a commercial opportunity by coupling a time-dependent insurer-remover profit model, a Gamma-grid collision simulation, three removal alternatives, policy and technology scenarios, and a strategic policy game.",
            "stakeholders": ["satellite owners and launchers", "insurers", "debris-removal firms", "space agencies", "international regulators", "space-service customers"],
            "required_outputs_observed": ["annual and cumulative profit", "remaining debris", "collision probability", "three-alternative comparison", "growth-policy scenario", "rocket-lifetime scenario", "insurance-rate sensitivity", "policy payoff matrices", "recommendations", "future repairs"],
        },
        "source_heading_map": [{"source_headings": item["source_headings"], "normalized_chapter": item["chapter"], "pages": item["pages"]} for item in CONTRACTS],
        "global_progression": [
            "debris threat and commercial-opportunity test", "land and space intervention taxonomy", "financial and physical notation", "annual profit decomposition", "utility-based compensation", "2D Gamma representation", "binary debris field", "removal-growth-launch-collision loop", "land/space/combined comparison", "growth-policy scenario", "rocket-lifetime scenario", "insurance-rate sensitivity", "baseline and policy payoff matrices", "commercial and regulatory decisions", "strengths and repairs", "source and reproducibility boundary",
        ],
        "section_contracts": contracts,
        "paragraph_chains": {
            "abstract": [
                chain(1, "threat-and-objective", "Debris creates collision exposure and a potential private-service opportunity.", "the summary names the physical threat and a commercial evaluation objective", "scale and demand are contextual rather than calibrated", "sets the decision target", "defines the firm and model chain", [au[0]]),
                chain(2, "firm-and-architecture", "A merged insurer-remover allows one accounting model to connect premiums, removal, and collision losses.", "three models are previewed", "the merger is an assumption, not observed market structure", "defines the modeled decision maker", "opens the profit model", [au[1]]),
                chain(3, "economic-model", "Annual revenue and two cost classes can represent time-dependent commercial performance.", "premium, removal, compensation, and accumulated profit are named", "discounting and market demand are omitted", "creates the financial output", "requests collision probability", [au[2]]),
                chain(4, "collision-model", "A Gamma-filled matrix and repeated random placement are used to estimate collision frequency.", "the summary names the 1000 by 1000 matrix and removal alternatives", "calibration, seeds, and replicate counts are absent", "supplies Pr(t) and Q_t", "moves to policy", [au[3]]),
                chain(5, "policy-model", "A two-player matrix can compare behavior before and after regulation.", "the summary names players, strategies, and a policy shift", "payoff derivation is not shown", "creates an equilibrium claim", "combines decisions", [au[0], au[1]]),
                chain(6, "parameter-boundary", "Commercial conclusions depend materially on the insurance rate and the no-discounting assumption.", "the summary explicitly flags commission and time value", "other parameter and model uncertainties remain wider", "qualifies transfer", "states recommendations", [au[2]]),
                chain(7, "decision", "The combined alternative, a sufficient commission, and an industrial standard are recommended.", "the summary joins the model outputs into actions", "recommendations hold only under the paper's supplied structure and values", "closes the compact argument", "the executive summary expands it", [au[3]]),
            ],
            "introduction": [
                chain(1, "hazard-context", "Debris scale and collision consequences make removal consequential.", "the opening names debris counts, harm, and candidate technologies", "counts mix debris populations and sources", "establishes demand", "asks about implementation", [iu[0]]),
                chain(2, "commercial-question", "The unresolved issue is whether removal can be implemented as a viable service.", "technology cost, risk, and benefit differ", "viability is not established by need alone", "frames the commercial question", "defines opportunity", [iu[1]]),
                chain(3, "opportunity-decomposition", "Demand, means, application, and benefit form the paper's opportunity test.", "the source names four elements and treats two as already present", "the decomposition is conceptual rather than externally validated", "identifies missing outputs", "commits to modeling", [iu[2]]),
                chain(4, "quantitative-commitment", "A time-dependent private-firm model will test application and benefit.", "the final introduction paragraph commits to projected net income", "market structure and parameter sources remain assumptions", "creates an inspectable objective", "methods type the alternatives", [iu[3]]),
            ],
        },
        "main_argument_chains": [
            {"name": "threat-to-commercial-objective", "chain": ["debris hazard", "stakeholders", "four-part opportunity test", "merged insurer-remover", "15-year net-income objective"], "decision": "measure the opportunity through a bounded private-firm accounting model"},
            {"name": "financial-and-collision-handoff", "chain": ["launch count and satellite value", "premium revenue", "removal choice and cost", "Gamma debris field", "same-cell collision frequency", "compensation cost", "annual and cumulative profit"], "decision": "keep physical collision output and financial loss connected through an explicit typed handoff"},
            {"name": "field-to-time-dependent-risk", "chain": ["2D reduction", "four Gamma rings", "15 percent binary occupancy", "removal", "growth", "launches", "overlap count", "Pr(t) and Q_t"], "decision": "produce scenario-specific risk paths while retaining calibration and grid boundaries"},
            {"name": "alternatives-to-combined-choice", "chain": ["land cost and range", "space cost and capacity", "common 15-year horizon", "profit paths", "remaining-debris paths", "combined run", "conditional recommendation"], "decision": "choose the combined alternative only within the aligned scenario and metrics"},
            {"name": "scenarios-to-bounded-parameters", "chain": ["growth-rate policy", "ending debris", "rocket lifetime", "accumulated profit", "insurance rate", "break-even timing", "local parameter recommendations"], "decision": "separate one-factor response from global robustness or market optimality"},
            {"name": "payoffs-to-policy-claim", "chain": ["owners and firm", "three strategies each", "baseline matrix", "two pure equilibria", "policy matrix", "one equilibrium", "within-matrix Pareto comparison"], "decision": "retain the equilibrium calculation while bounding the welfare claim by unreported payoff derivation and policy costs"},
        ],
        "organization_skeleton_test": {
            "status": "pass",
            "result": "With debris counts, rates, payoffs, and named technologies removed, the route remains hazard -> stakeholder opportunity test -> alternative taxonomy -> financial identity -> physical risk generator -> common-option comparison -> controlled scenarios -> strategic policy shift -> bounded recommendations and repairs.",
            "weakness_substitution": False,
        },
    }
    STAGE.mkdir(parents=True)
    output = STAGE / "organization.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "section_contracts": len(contracts), "main_argument_chains": len(result["main_argument_chains"]), "output": str(output), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
