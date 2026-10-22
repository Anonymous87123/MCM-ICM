from __future__ import annotations

"""Assemble create-only Queue 113 G7-G8 learning artifacts."""

import json
from collections import Counter
from pathlib import Path

import build_q112_artifacts as q112


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2016-42745-4dc9ed2b"
SHORT = "42745"
SHA = "4dc9ed2b48ba9415c26b12506e36e0a144491324a4f44445d6ae8083ad7c5b46"
TYPE = "B"
YEAR = "2016"
PAGE_COUNT = 26
STAGE = ROOT / "tmp/q113-stage-v1"
LANGUAGE_PATH = ROOT / "tmp/q113-language-stage-v3/language.json"
ORGANIZATION_PATH = ROOT / "tmp/q113-organization-stage-v1/organization.json"
MODELS_PATH = ROOT / "tmp/q113-model-stage-v2/models.json"
VISUALS_PATH = ROOT / "tmp/q113-visual-stage-v1/visuals.json"
EXTRACTION_PATH = ROOT / f"artifacts/papers/{PAPER_ID}/extraction.json"


WARNINGS = [
    {"page": 10, "model_id": "MU-B-2016-42745-001", "equation_id": "EQ-B-2016-42745-003", "summary": "Insurance alpha is explicitly arbitrary, w is equated to an unspecified fair value, and no market, loss, demand, or percent-convention calibration supports the premium-revenue equation."},
    {"page": 11, "model_id": "MU-B-2016-42745-002", "equation_id": "EQ-B-2016-42745-005", "summary": "The generic removal-cost sum multiplies p_t by q_t although p_t is alternately a catcher price or conduct cost and q_t is alternately debris capacity or conduct count; units and indexing conflict."},
    {"page": 11, "model_id": "MU-B-2016-42745-003", "equation_id": "EQ-B-2016-42745-009", "summary": "The compensation formula multiplies by epsilon even though the notation table defines epsilon as debris removed per space trapper; n_(t-1) is also not reconciled with exposure from surviving satellites."},
    {"page": 12, "model_id": "MU-B-2016-42745-003", "equation_id": "EQ-B-2016-42745-012", "summary": "The Cobb-Douglas construction sets x2=alpha*w and k=0.5 without economic estimation, leaves mu unidentified, and converts utility into compensation without a dimensional or actuarial justification."},
    {"page": 13, "model_id": "MU-B-2016-42745-004", "equation_id": "EQ-B-2016-42745-013", "summary": "The symbol alpha is reused for the insurance rate and Gamma shape, while Gamma parameters, fitted observations, ring boundaries, normalization, and goodness of fit are absent."},
    {"page": 13, "model_id": "MU-B-2016-42745-004", "equation_id": None, "summary": "Visual resemblance between a cited NASA curve and one Gamma-family curve is not parameter estimation or evidence that a two-dimensional radial law represents the selected 1-10 cm debris population."},
    {"page": 14, "model_id": "MU-B-2016-42745-004", "equation_id": None, "summary": "The approximately fifteen-percent binary occupancy is admitted to be an educated guess; the area-to-count explanation has no units, debris count, valid-cell denominator, or reproducible calculation."},
    {"page": 14, "model_id": "MU-B-2016-42745-006", "equation_id": None, "summary": "Same-cell collision probability depends on the arbitrary 1000 by 1000 grid, cell-to-altitude mapping, occupancy rules, satellite footprint, and time step, none of which receive a resolution study."},
    {"page": 15, "model_id": "MU-B-2016-42745-005", "equation_id": "EQ-B-2016-42745-014", "summary": "The printed debris update is self-referential Q_t=Q_t-(...) rather than a transition from Q_(t-1), and it omits the growth term described immediately afterward; it is retained verbatim rather than silently repaired."},
    {"page": 15, "model_id": "MU-B-2016-42745-005", "equation_id": None, "summary": "The source calls its baseline debris trend linear but implements or discusses a five-percent annual increase; no complete linear, geometric, or logarithmic recurrence and no fitted parameters are supplied."},
    {"page": 15, "model_id": "MU-B-2016-42745-005", "equation_id": None, "summary": "Random removal and growth omit coordinate-to-altitude conversion, accessible-cell selection, overflow and boundary handling, random seeds, repetition counts, and a mass-balance diagnostic."},
    {"page": 16, "model_id": "MU-B-2016-42745-006", "equation_id": "EQ-B-2016-42745-016", "summary": "The launch recurrence n_1=110 and n_t=1.05*n_(t-1) is reconstructed from prose; the plotted 2001-2015 series is not fitted to justify either 110 or five percent."},
    {"page": 16, "model_id": "MU-B-2016-42745-006", "equation_id": "EQ-B-2016-42745-017", "summary": "The law-of-large-numbers statement has no independent-run protocol, sample size, seed ledger, convergence plot, Monte Carlo error, confidence interval, or check that the simulated trials match the claimed probability."},
    {"page": 17, "model_id": "MU-B-2016-42745-002", "equation_id": "EQ-B-2016-42745-006", "summary": "The land equation adds initial cost C0 to C_1t without a one-time indicator, so the printed form can charge the initial investment every year rather than only at project start."},
    {"page": 18, "model_id": "MU-B-2016-42745-007", "equation_id": None, "summary": "The land, space, and combined paths rely on unreported prices, removal counts, insured values, commission, compensation scale, growth arrays, seeds, MATLAB code, and raw yearly outputs."},
    {"page": 19, "model_id": "MU-B-2016-42745-007", "equation_id": None, "summary": "The near-16-billion combined result is a single undiscounted scenario with no currency year, financing constraint, opportunity cost, demand response, joint uncertainty, or external commercial validation."},
    {"page": 20, "model_id": "MU-B-2016-42745-008", "equation_id": None, "summary": "The paper reports 8,004-6,374 as 1,670, but the arithmetic difference is 1,630; the printed sensitivity sequence must preserve this source error and use 1,630 in any corrected analysis."},
    {"page": 20, "model_id": "MU-B-2016-42745-008", "equation_id": None, "summary": "The logarithmic-growth scenario reports an ending count of 5,313 without an equation, fitted historical data, parameters, time origin, or comparable scenario likelihood."},
    {"page": 21, "model_id": "MU-B-2016-42745-008", "equation_id": None, "summary": "Rocket lifetimes of 3, 6, 9, and 12 form a four-point one-factor sweep; launch cadence, refurbishment cost, failure risk, capacity, replacement rule, and derivation of 0.38 billion per additional use are absent."},
    {"page": 22, "model_id": "MU-B-2016-42745-008", "equation_id": None, "summary": "The alpha=3 percent prose says the firm enjoys net income in the first nine years, while Figure 24 is negative for roughly those years; the visual supports an early-loss, not early-income, interpretation."},
    {"page": 22, "model_id": "MU-B-2016-42745-008", "equation_id": None, "summary": "Alpha changes both premium revenue and the constructed compensation amount, but the sensitivity narrative treats it mainly as revenue and ignores insurance demand, competition, claims frequency, percent conventions, and joint parameter changes."},
    {"page": 23, "model_id": "MU-B-2016-42745-009", "equation_id": None, "summary": "Best-response inspection confirms the stated baseline and policy pure equilibria, but payoff derivation, units, probability weighting, strategy costs, policy implementation cost, and external validity are not supplied."},
    {"page": 23, "model_id": "MU-B-2016-42745-009", "equation_id": None, "summary": "The Pareto-improvement claim is supportable only inside the two printed matrices; it omits policymakers, third parties, orbital externalities, enforcement, mixed strategies, uncertainty, and welfare aggregation."},
    {"page": 24, "model_id": "MU-B-2016-42745-010", "equation_id": None, "summary": "Claims of robust profit, accurate graphs, thorough sensitivity, optimal removal, and necessary standards exceed the uncalibrated field, arbitrary parameters, local sweeps, missing code, undiscounted accounting, and absent joint or out-of-sample validation."},
]


def validate_inputs(language: dict, organization: dict, models: dict, visuals: dict) -> None:
    if any(record.get("paper_id") != PAPER_ID for record in (language, organization, models, visuals)):
        raise ValueError("q113 stage paper IDs do not agree")
    if language.get("review_status") != "validated" or len(language.get("units", [])) != 68:
        raise ValueError("G1-G3 language stage must be validated at 68 units")
    if len(language.get("available_chapters", [])) != 17 or len(organization.get("section_contracts", [])) != 17:
        raise ValueError("G4 must retain all 17 normalized chapters and contracts")
    if len(organization.get("paragraph_chains", {}).get("abstract", [])) != 7:
        raise ValueError("abstract chain must retain seven source paragraphs")
    if len(organization.get("paragraph_chains", {}).get("introduction", [])) != 4:
        raise ValueError("introduction chain must retain four source paragraphs")
    if models.get("review_status") != "validated" or len(models.get("models", [])) != 10:
        raise ValueError("G5 must retain 10 model units")
    if sum(len(item.get("governing_equations", [])) for item in models["models"]) != 17:
        raise ValueError("G5 must retain all 17 formula records")
    if len(models.get("dependency_edges", [])) != 20:
        raise ValueError("G5 must retain 20 dependency edges")
    if visuals.get("review_status") != "validated" or len(visuals.get("visuals", [])) != 28:
        raise ValueError("G6 must retain 24 figures and four unnumbered analytical visuals")
    safety = visuals.get("transport_safety", {})
    if safety.get("total_bounded_jpeg_proxies") != 8 or safety.get("total_proxy_bytes") != 3096688:
        raise ValueError("G6 transport-safety ledger must retain all eight bounded proxies and exact bytes")
    if safety.get("observed_max_proxy_bytes", 450001) > safety.get("max_proxy_bytes", 450000):
        raise ValueError("G6 contains an oversized visual proxy")
    if len(WARNINGS) >= len(language["units"]):
        raise ValueError("G7 warnings must remain a strict minority of positive language units")


def build_card(organization: dict, models: dict, visuals: dict) -> dict:
    section_map = [
        {
            "page": contract["pages"][0],
            "section": " / ".join(contract["source_headings"]),
            "summary": f"Input: {contract['input']} Analytical job: {contract['analytical_job']} Output: {contract['output']} Handoff: {contract['handoff']}",
        }
        for contract in organization["section_contracts"]
    ]
    visual_records = [
        {
            "page": item["source_page"],
            "figure": item["figure"],
            "visual_record_id": item["visual_record_id"],
            "caption": item["caption"],
            "source_model_ids": item["source_model_ids"],
            "summary": f"{item['analytical_purpose']} Exact supported claim: {item['exact_claim_supported']} Uncertainty boundary: {item['uncertainty']}",
            "disposition": item["disposition"],
            "evidence_role": item["evidence_role"],
        }
        for item in visuals["visuals"]
    ]
    assumptions = [
        (9, "All LEO satellite launchers buy collision insurance at a fixed percentage of satellite value."),
        (9, "The insurer and debris-removal operator are merged into one private firm."),
        (9, "Commercial opportunity is measured by projected net income over fifteen years."),
        (9, "Time value of money is ignored."),
        (12, "Debris is locally uniform in altitude bands, persists without human removal, and follows uniform circular motion."),
        (12, "Only 1-10 cm debris threatens satellites; larger objects are avoidable and smaller objects are nonfatal."),
        (12, "A three-dimensional orbital problem can be reduced to a representative two-dimensional circular field."),
        (14, "Each grid cell is binary and approximately fifteen percent of valid cells are occupied."),
        (15, "Removal and debris growth select cells randomly within stated working ranges."),
        (16, "A satellite-debris same-cell overlap is a collision and an empty cell is fully safe."),
        (17, "Land removal has a large initial cost and low conduct cost; space removal has launch-weighted recurring cost."),
        (20, "Growth, rocket lifetime, and commission sensitivities change one named factor while other inputs remain fixed."),
        (22, "The two-player insurance-removal game has perfect information and only the printed three strategies per player."),
    ]
    data = [
        (6, "The paper cites more than 500,000 debris pieces and the 2009 collision as threat context, not as a frozen calibration dataset."),
        (6, "Laser Broom, Huff-and-Puff, nets, and Solar Sail sources establish technology categories, costs, altitude limits, and qualitative capacity claims."),
        (8, "The notation table links annual income, launch count, insured value, rate, removal cost, collision probability, debris state, and trapper capacity."),
        (10, "Space-Track launch records motivate n_t, but the source query result and preprocessing are not archived."),
        (13, "A cited NASA altitude-density curve and orbital visualization motivate the Gamma-shaped radial representation."),
        (14, "Four ring masses and a 1000 by 1000 binary matrix preprocess the radial story into a simulation field."),
        (15, "Land and space working ranges are stated as roughly 600-800 km and 800-1000 km."),
        (15, "NASA catalog growth excludes Fengyun-1C and Iridium-Cosmos events as abnormal outliers before trend selection."),
        (16, "The plotted 2001-2015 launch counts provide historical context while the simulation starts from 110 and grows five percent annually."),
        (17, "Technology, launch, debris, and cost citations are invoked for alternative runs without freezing numerical inputs."),
        (20, "Policy scenarios use ending counts 12,302, 9,932, 8,004, 6,374, and 5,313 across growth assumptions."),
        (23, "Two printed 3 by 3 bimatrices contain owner and firm payoffs before and after the asserted policy change."),
    ]
    verification = [
        {"page": 10, "section": "financial identities", "summary": "Equations 1-4 trace launches and premiums through annual and cumulative profit.", "verification_type": "formula-chain trace", "strength": "The accounting handoff is explicit.", "limitation": "Calibration, units, discounting, and exposure stock are incomplete."},
        {"page": 13, "section": "Gamma representation", "summary": "Figures 1-4 trace cited radial context into a two-dimensional annular intensity.", "verification_type": "source-to-model visual trace", "strength": "The dimensional reduction is inspectable.", "limitation": "Parameters, fitted data, and goodness of fit are absent."},
        {"page": 14, "section": "binary field", "summary": "Figure 5 displays the approximately fifteen-percent annular occupancy used by the simulator.", "verification_type": "synthetic-state inspection", "strength": "The simulation state is visually legible.", "limitation": "No seed, array, ring boundaries, or occupancy derivation is supplied."},
        {"page": 16, "section": "collision estimate", "summary": "The overlap ratio and law-of-large-numbers statement connect annual launches to Pr(t).", "verification_type": "formula-and-convergence claim trace", "strength": "The intended estimator is explicit.", "limitation": "Runs, errors, resolution, and independent trials are absent."},
        {"page": 17, "section": "land alternative", "summary": "Figures 7-8 align accumulated profit and ending debris for land-only removal.", "verification_type": "scenario output trace", "strength": "Financial and environmental outputs share a horizon.", "limitation": "Only one unreproducible stochastic path is shown."},
        {"page": 18, "section": "space and combined alternatives", "summary": "Figures 9-12 compare both remaining-debris fields and accumulated-profit paths.", "verification_type": "aligned alternative comparison", "strength": "The recommendation has two common metrics.", "limitation": "Inputs, raw arrays, uncertainty, and discounting are absent."},
        {"page": 20, "section": "growth policy", "summary": "Figures 13-16 expose ending debris under four, three, two percent and logarithmic growth.", "verification_type": "local scenario trace", "strength": "The ending-count direction is visible.", "limitation": "One arithmetic error and the missing log equation block strong inference."},
        {"page": 21, "section": "rocket lifetime", "summary": "Figures 17-20 compare four reusable-rocket lifetime paths.", "verification_type": "one-factor sensitivity", "strength": "The tested levels are explicit.", "limitation": "Technology costs, risks, and uncertainty are not modeled."},
        {"page": 22, "section": "insurance alpha", "summary": "Figures 21-24 compare four commission-rate profit paths.", "verification_type": "one-factor sensitivity and contradiction check", "strength": "The plot ordering is visible.", "limitation": "The alpha=3 percent prose conflicts with Figure 24 and joint effects are ignored."},
        {"page": 23, "section": "payoff matrices", "summary": "Cell-by-cell best responses confirm two baseline pure equilibria and one policy pure equilibrium.", "verification_type": "independent equilibrium check", "strength": "The stated pure equilibria are internally correct.", "limitation": "Payoff derivation, policy cost, uncertainty, and external welfare are absent."},
    ]
    results = [
        (10, "Annual profit is R_t-C_t and cumulative profit sums annual values through t."),
        (11, "Total cost separates removal expense from expected collision compensation."),
        (14, "The collision state is a four-ring 1000 by 1000 binary field with hand-set occupancy."),
        (16, "Pr(t) is estimated as same-cell collisions divided by annual launches."),
        (17, "Land-only removal holds total debris growth below roughly 1,000 but shows loss for the first eight years."),
        (18, "Space-only removal has favorable profit but loses control of inner-layer debris late in the horizon."),
        (19, "The combined alternative reports more than 2,000 debris removed and nearly 16 billion accumulated profit."),
        (20, "Ending debris falls from 12,302 to 9,932, 8,004, 6,374, and 5,313 across lower-growth and logarithmic scenarios."),
        (21, "Rocket lifetimes 3-12 produce a reported maximum-minimum profit gap equal to 15.4 percent of total profit."),
        (22, "Commission rates 3-6 percent materially reorder early profit and reported break-even timing."),
        (23, "The baseline matrix has pure equilibria at half insured/remove considerably and fully insured/remove some."),
        (23, "The policy matrix has one pure equilibrium at half insured/remove considerably, with both printed payoffs improved relative to either baseline equilibrium."),
        (24, "The paper recommends combined removal, alpha at least four percent and preferably five percent, and new debris standards."),
    ]
    contributions = [
        (6, "Frames debris removal as a four-part commercial-opportunity test rather than only a physical cleanup problem."),
        (8, "Creates a shared notation interface across insurance, removal, collision, debris inventory, and policy."),
        (9, "Connects a merged insurer-remover to annual and cumulative profit over a common horizon."),
        (12, "Reduces a three-dimensional debris field to a tractable annular representation before simulation."),
        (14, "Uses one binary field for removal, growth, launch, collision, and ending-state comparisons."),
        (17, "Compares land, space, and combined alternatives on both profit and remaining debris."),
        (19, "Uses explicit what-if sections to separate policy growth, rocket technology, and commission effects."),
        (22, "Adds a two-player payoff matrix to translate model outputs into an inspectable policy argument."),
        (23, "Checks how a policy-induced payoff change moves the pure-strategy equilibrium."),
        (24, "Names three concrete repair directions: three-dimensional geometry, better data, and dynamic resource allocation."),
    ]
    extensions = [
        (10, "Calibrate launch demand, insured value, premium rate, claims exposure, payout severity, currency year, and discount rate from market data."),
        (11, "Replace the compensation utility shortcut with an actuarial frequency-severity model and a unit-checked exposure stock."),
        (13, "Fit a three-dimensional orbital debris distribution by size, altitude, inclination, and epoch with goodness-of-fit and uncertainty."),
        (14, "Define cell geometry and collision cross-section, then run grid-convergence and time-step sensitivity studies."),
        (15, "Write a complete Q_(t-1)-to-Q_t transition with growth, removal capacity, band constraints, and mass-balance tests."),
        (16, "Archive launch and debris data, MATLAB code, seeds, repetitions, raw arrays, convergence diagnostics, and regression tests."),
        (18, "Optimize annual capital allocation and start time across land and space methods under financing, capacity, and risk constraints."),
        (20, "Run global and joint uncertainty over growth, prices, rates, Gamma parameters, collision risk, technology reliability, and policy compliance."),
        (23, "Derive payoffs from model outputs, include policy and third-party costs, and test mixed, incomplete-information, and dynamic games."),
        (24, "Evaluate decision stability with external cases, baselines, out-of-sample years, calibrated loss metrics, and reproducible scenario reporting."),
    ]
    return {
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "Strategies to Eliminating Space Debris: Approaches from a Time Dependent Evaluation Model",
        "award_status": "outstanding",
        "source": {
            "relative_path": "2016\u7f8e\u8d5b\u7279\u7b49\u5956/B-42745-Outstanding.pdf",
            "sha256": SHA,
            "page_count": PAGE_COUNT,
            "pdf_page_offset_note": "Physical pages 1-4 contain the summary, executive summary, and title; physical pages 5-26 correspond to printed Pages 2-23 of 23.",
        },
        "schema_version": 1,
        "source_quality": {
            "status": "validated",
            "text_pages": PAGE_COUNT,
            "rendered_pages": PAGE_COUNT,
            "visual_review": "complete",
            "notes": [
                "All 26 physical pages were read sequentially through the summary, executive summary, contents, every substantive section, both payoff matrices, conclusions, improvements, and References 1-18.",
                "Eight one-at-a-time byte-bounded JPEG proxies totaling 3,096,688 bytes covered pages 1-26 and focused pages 8-11 notation and formulas; the largest proxy was 448,554 bytes and no original full-page PNG entered the root context.",
                "Seventeen formula records, Figures 1-24, one unnumbered summary figure, one notation table, and two payoff matrices have source-ordered retention and dispositions.",
                "No clipping, overlap, missing page, blank page, black output, or formula-rendering failure was found; source formula, calibration, simulation, arithmetic, contradiction, game, and scope defects remain last-pass warnings.",
                "The official problem statement is not frozen with this paper, so task reconstruction is bounded to the paper's explicit commercial-opportunity and policy objectives.",
            ],
        },
        "context_sources": [
            {"type": "paper", "path": "2016\u7f8e\u8d5b\u7279\u7b49\u5956/B-42745-Outstanding.pdf"},
            {"type": "extraction", "path": f"artifacts/papers/{PAPER_ID}/extraction.json"},
            {"type": "text-pages", "path": f"artifacts/papers/{PAPER_ID}/text/pages"},
            {"type": "visual-stage", "path": "tmp/q113-visual-stage-v1/visuals.json"},
        ],
        "task_reconstruction": {
            "status": "incomplete-official-task-unavailable",
            "inputs": ["debris population and removal technologies", "launch count, insured value, commission, compensation, and cost", "Gamma field, removal bands, growth, launch placement, and collision overlap", "land, space, and combined alternatives", "growth, rocket-lifetime, commission, and payoff scenarios"],
            "outputs": ["annual and cumulative profit", "synthetic debris and collision paths", "alternative profit and ending-debris comparisons", "local sensitivity paths", "baseline and policy equilibria", "commercial and regulatory recommendations"],
            "decisions": ["whether debris removal is a commercial opportunity", "which removal alternative to use", "what commission range is locally viable", "whether standards reduce modeled debris growth", "whether the supplied policy matrix improves both players"],
        },
        "section_map": section_map,
        "assumptions": [{"page": page, "summary": summary} for page, summary in assumptions],
        "data_and_preprocessing": [{"page": page, "summary": summary} for page, summary in data],
        "models": [{"model_id": item["model_id"], "page": item["page"], "summary": item["summary"]} for item in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": verification,
        "results_trace": [{"page": page, "summary": summary} for page, summary in results],
        "contributions": [{"page": page, "summary": summary} for page, summary in contributions],
        "writing_logic": [{"page": c["pages"][0], "summary": f"{c['chapter']}: {c['rhetorical_job']} {c['handoff']}"} for c in organization["section_contracts"]],
        "language_observations": [{"page": c["pages"][0], "summary": f"{c['chapter']}: {c['input']} -> {c['output']}"} for c in organization["section_contracts"]],
        "visualization_observations": visual_records,
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The summary previews three distinct models, three alternatives, key sensitivity findings, and the policy recommendation before technical details; award status does not identify a causal judging factor.", "evidence_class": "J"},
            {"page": 8, "summary": "The notation table makes the financial-to-physical interfaces scannable before equations cross model boundaries.", "evidence_class": "J"},
            {"page": 18, "summary": "Side-by-side profit and ending-debris outputs make the combined recommendation immediately comparable on two decision metrics.", "evidence_class": "J"},
            {"page": 23, "summary": "Two compact payoff matrices make the policy-induced equilibrium shift inspectable, while payoff validity remains unresolved.", "evidence_class": "J"},
        ],
        "weaknesses": [dict(item) for item in WARNINGS],
        "independent_extensions": [{"extension_id": f"E-B-{SHORT}-{index:03d}", "page": page, "summary": summary} for index, (page, summary) in enumerate(extensions, start=1)],
        "candidate_rule_impacts": [],
        "unresolved_questions": [item["summary"] for item in WARNINGS],
        "protocol_v2_records": {},
        "review_status": "validated",
    }


def make_observations(template, language: dict, models: dict, card: dict) -> list[dict]:
    observations = template.make_observations(language, models, card)
    interpretations = {
        "language": "Reuse the rhetorical mechanism only after replacing debris, technology, insurer, launcher, premium, collision, grid, scenario, payoff, and policy entities.",
        "modeling": "Retain financial identities, removal cost, compensation, spatial field, annual transition, collision estimator, scenario comparison, sensitivity, game, and decision handoffs together.",
        "logic": "Preserve the positive threat-to-opportunity-to-financial-and-physical-model-to-alternative-to-scenario-to-policy chain before warnings.",
        "visualization": "Keep figure or table identity, axes, units, radial band, scenario, source status, uncertainty, and exact supported claim together.",
        "verification": "Name the exact formula trace, synthetic-state check, aligned scenario comparison, sensitivity path, arithmetic check, or best-response calculation.",
        "data": "Retain source, date, debris size class, launch query, technology band, price unit, distribution input, scenario setting, version, and downstream consumer.",
        "assumption": "Pair each insurance, persistence, size, dimension, occupancy, randomness, collision, cost, fixed-input, or perfect-information assumption with its enabled computation and excluded regime.",
        "result": "Keep annual versus cumulative profit, collision probability, debris inventory, alternative, local scenario, equilibrium, and policy claim distinct.",
        "weakness": "Record formula, unit, calibration, grid, simulation, arithmetic, uncertainty, payoff, validation, and scope risks only after positive G1-G6 learning.",
        "other": "Separate cited context, source statements, reconstructed equations, synthetic output, executable evidence, corrected arithmetic, internal equilibrium checks, and real-world validation.",
    }
    provenance = [
        (25, "references", "Eighteen references identify technology, launch, debris, cost, Gamma, and policy sources but do not freeze their bytes, datasets, or numerical inputs."),
        (6, "threat context", "The 500,000-piece statement and 2009 collision motivate the problem without calibrating the selected debris class or field."),
        (6, "opportunity contract", "The four-element business-opportunity test defines the modeling target while demand and means are treated as given."),
        (7, "technology taxonomy", "Laser, gas-pulse, net, and sail examples motivate two families but do not specify a complete feasible technology set."),
        (8, "notation contract", "The table exposes cross-model symbols and also reveals q_t, epsilon, and alpha conflicts that must not be silently normalized."),
        (10, "launch source", "Space-Track is cited without a frozen query result, filters, treatment of launches versus objects, or fitted projection."),
        (13, "NASA context", "NASA curves and images motivate radial structure but do not provide Gamma parameters for the target debris subset."),
        (14, "occupancy construction", "The field is visibly synthetic and the fifteen-percent fill is an educated guess rather than observed occupancy."),
        (15, "annual transition", "Removal, growth, and launching are described sequentially without a complete executable recurrence or mass-balance record."),
        (16, "Monte Carlo interface", "The paper invokes random placement and large numbers without seeds, repetitions, convergence error, or raw collision counts."),
        (17, "cost provenance", "Cited technology and launch sources do not freeze the values used in the land, space, and combined financial paths."),
        (18, "scenario outputs", "Profit lines and ending fields are source-checked images, not machine-readable arrays or replicate distributions."),
        (20, "policy growth cases", "Five ending counts expose local response while the arithmetic and logarithmic recurrence remain incomplete."),
        (22, "rate cases", "Four alpha paths expose sensitivity and a prose-figure contradiction without a market or actuarial calibration."),
        (23, "payoff matrices", "Best responses are internally checkable, but the numerical payoff construction and policy cost are not reported."),
        (24, "conclusion boundary", "Recommendations and strengths are source claims whose transfer is bounded by missing calibration, discounting, uncertainty, code, and external validation."),
    ]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = ["Apply only when debris population, geometry, units, costs, launch exposure, probability support, simulation protocol, uncertainty, payoff derivation, and receiving decision are explicit."]
        row["counterevidence"] = ["A smooth Gamma curve, synthetic occupancy field, single profit path, ending scatter plot, four-level sweep, or asserted payoff matrix does not prove calibration, prediction, commercial viability, global robustness, or social welfare."]
        if row["dimension"] == "other":
            page, section, basis = provenance[other_index]
            other_index += 1
            row["page"] = page
            row["section"] = f"{section} / evidence action {other_index}"
            row["source_basis"] = basis
    if other_index != len(provenance):
        raise RuntimeError(f"expected {len(provenance)} provenance observations, found {other_index}")
    return observations


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first: dict[str, str] = {}
    for row in observations:
        first.setdefault(row["dimension"], row["observation_id"])

    def evidence(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])

    entries = [
        ("R-B-LANG-001", "retain threat framing, opportunity test, financial-physical handoff, alternative comparison, scenario boundary, payoff argument, conclusion, repair, and provenance with typed slots", first["language"]),
        ("R-B-LOG-001", "trace debris threat through opportunity, technology taxonomy, accounting, Gamma field, annual simulation, alternatives, local scenarios, payoffs, and bounded decisions", first["logic"]),
        ("R-B-DATA-001", "version debris class and epoch, technology range and cost, launch query, satellite value, Gamma inputs, grid geometry, scenario arrays, payoffs, currency, and runtime", first["data"]),
        ("R-B-DATA-002", "maintain assumptions for insurance uptake, merged firm, discounting, debris persistence and size, 2D reduction, occupancy, randomness, same-cell collision, fixed sensitivities, and perfect information", evidence("R-B-DATA-002")),
        ("R-B-MOD-001", "retain profit accounting, alternative costs, actuarial compensation, Gamma field, debris transition, collision estimator, alternative comparison, sensitivities, game, and decision interfaces", first["modeling"]),
        ("R-B-MOD-003", "combine launch exposure, removal choice, field state, collision frequency, compensation, annual profit, sensitivity, and policy only through typed unit, time, support, and evidence contracts", evidence("R-B-MOD-003")),
        ("R-B-MOD-004", "keep annual and cumulative profit, collision frequency, debris inventory, alternative output, growth case, rocket case, rate case, equilibrium, and welfare claim distinct", first["result"]),
        ("R-B-MOD-005", "stress alpha, w, delta, Gamma parameters, occupancy, grid scale, transition recurrence, launch growth, seeds, costs, discounting, joint sensitivity, and payoff derivation", evidence("R-B-MOD-005")),
        ("R-B-VER-002", "make every commercial and policy claim formula-, field-, simulation-, alternative-, sensitivity-, arithmetic-, equilibrium-, and provenance-specific", first["verification"]),
        ("R-B-VER-004", "reconcile symbol and unit conflicts, self-referential Q_t, missing growth recurrence, absent seeds, repeated C0, 1,630 arithmetic, alpha prose-figure conflict, and unsupported welfare scope", first["weakness"]),
        ("R-B-VIZ-001", "retain the summary field, notation table, Figures 1-24, and both payoff matrices with page, source status, axes, scenario, uncertainty, and exact supported claim", first["visualization"]),
        ("R-B-COMP-001", "measure field generation, ring assignment, annual removal and growth, launch placement, collision counting, repetitions, cost aggregation, scenario reruns, best responses, and reproducible runtime separately", evidence("R-B-COMP-001")),
    ]
    card["candidate_rule_impacts"] = [
        {"rule_id": rule_id, "action": action, "evidence_ids": [observation_id]}
        for rule_id, action, observation_id in entries
    ]


def build_audit(template, language: dict, organization: dict, models: dict, visuals: dict, card: dict, observations: list[dict]) -> dict:
    audit = template.make_audit(language, models, card, observations)
    paragraph_chains = []
    for chapter in ("abstract", "introduction"):
        paragraphs = [
            {
                "paragraph_index": source["paragraph"],
                "dominant_move": f"{source['dominant_move']}: {source['claim']} -> {source['consequence']} -> {source['next_link']}",
                "language_unit_ids": source["language_unit_ids"],
            }
            for source in organization["paragraph_chains"][chapter]
        ]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": len(paragraphs), "coverage_status": "complete", "gaps": [], "paragraphs": paragraphs})
    audit["paragraph_chains"] = paragraph_chains
    audit["language_unit_dispositions"] = [
        {"language_unit_id": unit["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": unit["candidate_pattern_ids"], "reason": "The rhetorical mechanism transfers only after replacing debris, technology, firm, launch, premium, collision, grid, scenario, payoff, policy, and evidence-boundary entities."}
        for unit in language["units"]
    ]
    argument_metadata = {
        "threat-to-commercial-objective": {"claim": "Debris hazard and available interventions create a commercial question that is measured through a merged insurer-remover's fifteen-year income.", "source_pages": [1, 2, 3, 6, 7, 8, 9]},
        "financial-and-collision-handoff": {"claim": "Launch premiums, removal cost, collision frequency, and compensation form one typed handoff from physical state to annual and cumulative profit.", "source_pages": [8, 9, 10, 11, 12, 15, 16]},
        "field-to-time-dependent-risk": {"claim": "A reduced Gamma ring field is changed by removal, growth, and launches before same-cell overlaps produce scenario-specific risk.", "source_pages": [12, 13, 14, 15, 16]},
        "alternatives-to-combined-choice": {"claim": "Land, space, and combined alternatives share a horizon, profit metric, and debris metric before the conditional combined recommendation.", "source_pages": [16, 17, 18, 19]},
        "scenarios-to-bounded-parameters": {"claim": "Growth, rocket lifetime, and commission reruns expose local response without establishing global robustness or market optimality.", "source_pages": [19, 20, 21, 22]},
        "payoffs-to-policy-claim": {"claim": "Best responses support the equilibrium shift and within-matrix payoff improvement while payoff derivation and external welfare remain unresolved.", "source_pages": [22, 23, 24]},
    }
    chains = []
    for chain in organization["main_argument_chains"]:
        metadata = argument_metadata[chain["name"]]
        chains.append({"claim": metadata["claim"], "support_steps": chain["chain"], "decision_consequence": chain["decision"], "source_pages": metadata["source_pages"]})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": organization["global_progression"] + ["Only after the positive language, organization, model, and visual chain is complete does G7 record formula, unit, calibration, simulation, arithmetic, payoff, validation, and scope warnings."],
        "section_progressions": [
            {"chapter": c["chapter"], "moves": [f"input: {c['input']}", f"rhetorical job: {c['rhetorical_job']}", f"analytical job: {c['analytical_job']}", f"output: {c['output']}", f"handoff: {c['handoff']}"], "positive_pattern": "Use the source-anchored input -> rhetorical job -> analytical job -> output -> handoff contract; warnings remain a last pass."}
            for c in organization["section_contracts"]
        ],
        "main_argument_chains": chains,
    }
    audit["formula_error_watch"] = {
        "mode": "last-pass-warning-only",
        "completed_after_positive_passes": True,
        "warnings": [
            {"model_id": warning["model_id"], "equation_id": warning["equation_id"], "page": warning["page"], "warning": warning["summary"]}
            for warning in WARNINGS if warning["equation_id"] is not None
        ],
    }
    model_ids = [item["model_id"] for item in models["models"]]
    equation_ids = [equation["equation_id"] for item in models["models"] for equation in item["governing_equations"]]
    audit["model_retention"] = {
        "model_count": len(model_ids),
        "retained_model_ids": model_ids,
        "retained_equation_ids": equation_ids,
        "central_equations": [
            {"model_id": item["model_id"], "equation_ids": [equation["equation_id"] for equation in item["governing_equations"]], "all_central_equations_retained": True}
            for item in models["models"] if item["governing_equations"]
        ],
    }
    audit["visualization_dispositions"] = [
        {"paper_card_visual_index": item["paper_card_visual_index"], "visual_record_id": item["visual_record_id"], "disposition": item["disposition"], "analytical_purpose": item["analytical_purpose"]}
        for item in visuals["visuals"]
    ]
    counts = Counter(row["dimension"] for row in observations)
    audit["dimension_counts"] = {dimension: counts[dimension] for dimension in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}
    audit["positive_reusable_language_count"] = len(language["units"])
    audit["weakness_record_count"] = counts["weakness"]
    audit["gate_attestation"] = {
        "g1_g3_language": "validated-before-G4",
        "g4_organization": "passed-before-G5-G6",
        "g5_models": "validated-before-G7",
        "g6_visuals": "passed-before-G7",
        "g7_warning_mode": "last-pass-warning-only",
        "g7_warning_count": len(WARNINGS),
        "warnings_strict_minority_of_language": len(WARNINGS) < len(language["units"]),
        "request_body_guard": {"bounded_jpeg_proxies": 8, "total_proxy_bytes": 3096688, "largest_proxy_bytes": 448554, "original_full_page_png_in_context": False},
    }
    return audit


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    language = q112.read_json(LANGUAGE_PATH)
    organization = q112.read_json(ORGANIZATION_PATH)
    models = q112.read_json(MODELS_PATH)
    visuals = q112.read_json(VISUALS_PATH)
    extraction = q112.read_json(EXTRACTION_PATH)
    validate_inputs(language, organization, models, visuals)
    if extraction.get("paper_id") != PAPER_ID or extraction.get("page_count") != PAGE_COUNT:
        raise ValueError("q113 extraction identity or page count does not match the current paper")

    template = q112.load_module(ROOT / "scripts/build_q100_artifacts.py", "q100_template_for_q113")
    for name, value in {"PID": PAPER_ID, "SHORT": SHORT, "SHA": SHA, "TYPE": TYPE, "YEAR": YEAR, "PAGE_COUNT": PAGE_COUNT}.items():
        setattr(template, name, value)

    card = build_card(organization, models, visuals)
    card["protocol_v2_records"] = {
        "language": {"path": f"artifacts/language-units/{PAPER_ID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]},
        "models": {"path": f"artifacts/model-units/{PAPER_ID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(item["governing_equations"]) for item in models["models"]), "review_status": models["review_status"]},
    }
    observations = make_observations(template, language, models, card)
    attach_rule_impacts(card, observations)
    audit = build_audit(template, language, organization, models, visuals, card, observations)
    extraction["source_relative_path"] = "2016\u7f8e\u8d5b\u7279\u7b49\u5956/B-42745-Outstanding.pdf"
    extraction["visual_review_status"] = "complete"
    extraction["visual_review"] = {
        "status": "complete",
        "reviewed_pages": list(range(1, PAGE_COUNT + 1)),
        "notes": [
            "All 26 physical pages were inspected through eight one-at-a-time byte-bounded JPEG proxies totaling 3,096,688 bytes; the largest was 448,554 bytes. No clipping, overlap, missing page, blank page, black output, or formula-rendering failure was found.",
            "Figures 1-24, the unnumbered summary field, notation table, two payoff matrices, and seventeen formula records were reconciled by source page. A focused crop covered pages 8-11 notation and formulas.",
            "No original full-page PNG, original-detail contact sheet, batched image response, or complete session JSONL entered the root model context.",
            "Source defects remain separate last-pass warnings, including symbol and unit conflicts, missing Gamma and simulation calibration, self-referential Q_t, absent growth recurrence, 1,630 arithmetic, alpha prose-figure contradiction, missing payoff derivation, and bounded Pareto scope.",
        ],
    }

    STAGE.mkdir(parents=True)
    q112.write_json_create(STAGE / "language.json", language)
    q112.write_json_create(STAGE / "models.json", models)
    q112.write_json_create(STAGE / "card.json", card)
    q112.write_json_create(STAGE / "audit.json", audit)
    q112.write_json_create(STAGE / "extraction.json", extraction)
    with (STAGE / "observations.jsonl").open("x", encoding="utf-8", newline="\n") as handle:
        for row in observations:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

    print(json.dumps({"paper_id": PAPER_ID, "stage": str(STAGE), "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "models": len(models["models"]), "equations": 17, "dependency_edges": len(models["dependency_edges"]), "visuals": len(visuals["visuals"]), "observations": len(observations), "warnings": len(WARNINGS), "proxy_bytes": visuals["transport_safety"]["total_proxy_bytes"], "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
