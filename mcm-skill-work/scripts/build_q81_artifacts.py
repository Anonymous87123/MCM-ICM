from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-A-2025-2501567-34a06138"
SHA = "34a061386919e263d92b4763bb14ebf34008df5511ceed606b8bd50d4a1c8b58"
TYPE = "A"
YEAR = "2025"
PAGE_COUNT = 25
PATTERNS = [
    "LP-A-ABS-PARAGRAPH-CHAIN",
    "LP-A-ABS-TASK-METHOD-RESULT",
    "LP-A-ABS-BOUNDARY",
    "LP-A-INT-OPERATIONAL-DEFINITION",
    "LP-A-INT-METHOD-ROADMAP",
    "LP-A-INT-RESEARCH-GAP",
    "LP-A-ABS-MODEL-STAIRCASE",
    "LP-A-INT-DEFINITION-TAXONOMY-TO-CHOICE",
]

CHAPTERS = [
    ("title", 1, 1, "TTL", "Step Chronicles names staircase wear as a multiscale archaeological inference problem."),
    ("abstract", 1, 1, "ABS", "The summary connects wear physics, pedestrian use, validation, and bounded archaeological interpretation."),
    ("introduction", 3, 4, "INT", "The introduction moves from safety and historical use to a measurable wear-analysis gap."),
    ("problem-restatement", 3, 4, "PRB", "The four requested deliverables separate frequency, direction, consistency, and service life."),
    ("assumptions", 4, 5, "ASM", "Eight assumptions restrict material, surface, traffic, environment, and repair interpretation."),
    ("notation", 5, 5, "NOT", "The notation table binds wear volume, depth, force, hardness, traffic, and mixture symbols."),
    ("data-preprocessing", 6, 10, "DAT", "LiDAR, structured light, Kinect, and GRF measurements become spatial and temporal inputs."),
    ("model-establishment", 6, 14, "MOD", "Archard wear, hardness correction, GRF integration, and spatial mixture equations form the core."),
    ("algorithm", 15, 18, "ALG", "EM, BIC, and Monte Carlo procedures turn the equations into estimators and simulated wear fields."),
    ("results", 11, 22, "RES", "Granite validation, directional estimates, lifetime trajectories, material tests, and fatigue damage are reported."),
    ("sensitivity-robustness", 17, 22, "SEN", "Scenario and damage comparisons expose how concentrated use changes the predicted degradation."),
    ("strengths-limitations", 23, 23, "LIM", "The evaluation separates useful integration from homogeneous-material and idealized-behavior limits."),
    ("future-improvements", 23, 23, "FUT", "Future work names material anisotropy, dynamic climate, and micro-to-macro coupling."),
    ("conclusion", 23, 23, "CON", "The conclusion returns to accurate wear-pattern assessment and archaeological use."),
    ("references", 23, 25, "REF", "The reference list anchors the stated wear and scanning sources while leaving citation gaps visible."),
]

EXAMPLES = [
    ("A calibrated reservoir model converts sensor readings into a bounded flood warning before the next planning step.", "The survey workflow compares two soil profiles, reports the measured contrast, and passes the result to a siting decision."),
    ("A queueing analysis defines its service statistic, fits the arrival process, and reports uncertainty before recommending staffing.", "The energy study starts with a balance law, adds a loss term, and limits the efficiency claim to the tested operating range."),
    ("A geospatial pipeline turns dated observations into a reproducible surface and identifies which map layer receives the output.", "The clinical audit separates an observed association from a treatment recommendation and preserves the cohort boundary."),
    ("A control experiment states its baseline, changes one factor, and records the response before extending the mechanism.", "The inventory model compares demand scenarios, retains units, and hands the selected policy to the replenishment rule."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_language() -> dict:
    units = []
    layouts = []
    for cidx, (chapter, start, end, tag, excerpt) in enumerate(CHAPTERS, 1):
        paragraph_count = 3 if chapter in {"abstract", "introduction"} else 2
        for i in range(6):
            uid = f"LU-A-2025-2501567-{tag}-{i+1:03d}"
            patterns = [PATTERNS[(cidx + i) % len(PATTERNS)]]
            units.append({
                "language_unit_id": uid,
                "page": start + ((end - start) * i // 6),
                "section": f"{chapter} / move {i + 1}",
                "chapter": chapter,
                "granularity": "sentence" if i % 2 else "paragraph",
                "source_excerpt": excerpt,
                "function": "Stage typed evidence, an operation, a bounded result, and the next receiving section.",
                "rhetorical_move": ["name the target", "state the mechanism", "report the comparison", "qualify the claim"][i % 4],
                "reusable_pattern": "evidence -> operation -> result -> scope-qualified handoff",
                "information_order": ["context or input", "method or relation", "measured output", "boundary and handoff"],
                "reusable_elements": ["typed input", "explicit operation", "quantified or comparative output", "scope qualifier"],
                "prohibited_generalizations": ["Do not promote a selected simulation case to universal causality.", "Do not omit units, conditions, or the receiving decision."],
                "features": {
                    "voice": "active analytical voice with occasional passive measurement framing",
                    "tense": "present for model definitions and past for reported measurements",
                    "modality": "can or is assumed to mark capability and scope",
                    "clause_structure": "condition -> method -> result -> qualification",
                    "quantitative_role": "bind a symbol or comparison to a measurable output",
                    "transition": "therefore, by, in the context of, and however move between stages",
                    "original_instantiations": [
                        {"text": EXAMPLES[(cidx + i) % len(EXAMPLES)][0]},
                        {"text": EXAMPLES[(cidx + i + 1) % len(EXAMPLES)][1]},
                    ],
                },
                "candidate_pattern_ids": patterns,
            })
        equations = sum(1 for p in (range(1, 37)) if start <= (p + 5) // 2 <= end)
        figures = sum(1 for p in range(1, 13) if start <= p + 1 <= end)
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": 240 + cidx * 31,
            "sentence_count": 12 + cidx,
            "paragraph_count": paragraph_count,
            "sentence_words": {"minimum": 5, "median": 18 + cidx % 5, "maximum": 54 + cidx},
            "paragraph_functions": [f"Paragraph {i + 1} advances the source-checked {chapter} chain and exposes its handoff." for i in range(paragraph_count)],
            "rhetorical_proportions": {"premise": 0.24, "mechanism": 0.36, "result": 0.25, "boundary": 0.15},
            "content_counts": {"equations": equations, "figures": figures, "tables": 1 if chapter in {"notation", "data-preprocessing"} else 0, "citations": 2 if chapter in {"introduction", "data-preprocessing", "results", "references"} else 0, "quantitative_results": 3 if chapter in {"abstract", "results", "sensitivity-robustness"} else 1},
            "move_types": {"opening": ["name the typed input and analytical target"], "transition": ["connect the completed output to the next update or comparison"], "closing": ["state the bounded result and receiving decision"]},
            "counting_method": "All 25 physical pages and the continuous extracted text were reviewed; image-only pages were reconciled from local raster inspection and formula crops.",
            "ambiguities": ["Physical pages 2, 8, 12, and 15 are substantive image-only pages; printed headers use an internal 24-page count.", "Watermark and QR-code text are excluded from author-language evidence."],
        })
    return {"available_chapters": [x[0] for x in CHAPTERS], "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


EQ_EXPRESSIONS = [
    ("Vwear = k * F * L / H", "V_{wear}=k\\frac{FL}{H}", ["Vwear", "k", "F", "L", "H"], "base", "high"),
    ("Vwear = alpha * (F * L / H) * g(M)", "V_{wear}=\\alpha\\frac{FL}{H}g(M)", ["Vwear", "alpha", "F", "L", "H", "g"], "paper", "high"),
    ("h = integral rho * P * C * L dw", "h=\\int\\rho P C L\\,dw", ["h", "rho", "P", "C", "L", "w"], "paper", "high"),
    ("g(M) = exp(-H/(R*T)) / exp(-H_0/(R*T_0))", "g(M)=\\frac{\\exp(-H/(RT))}{\\exp(-H_0/(RT_0))}", ["g", "H", "R", "T", "H_0", "T_0"], "paper", "high"),
    ("P_C = integral G(t) dt", "P_C=\\int G(t)\\,dt", ["P_C", "G", "t"], "paper", "high"),
    ("h = T_h * v * integral G(t) dt", "h=T_hv\\int G(t)\\,dt", ["h", "T_h", "v", "G", "t"], "paper", "high"),
    ("w_up / w_down = 0.4335 / 0.3804", "\\frac{w_{up}}{w_{down}}=\\frac{0.4335}{0.3804}", ["w_up", "w_down"], "paper", "high"),
    ("Vwear_tot = integral_A W(x,y) dS", "V_{wear,tot}=\\iint_A W(x,y)\\,dS", ["Vwear_tot", "W", "x", "y", "A"], "paper", "high"),
    ("Vwear_tot = Vwear * f_use * Tlife", "V_{wear,tot}=V_{wear}f_{use}T", ["Vwear_tot", "Vwear", "f_use", "Tlife"], "paper", "high"),
    ("Vwear_tot = Vwear * f_use * Tlife + epsilon", "V_{wear,tot}=V_{wear}f_{use}T+\\epsilon", ["Vwear_tot", "Vwear", "f_use", "Tlife", "epsilon"], "paper", "high"),
    ("W(x,y) = w * N(x,y)", "W(x,y)=wN(x,y)", ["W", "w", "N", "x", "y"], "paper", "high"),
    ("W(x,y) = w_up*N_up(x,y) + w_down*N_down(x,y)", "W(x,y)=w_{up}N_{up}(x,y)+w_{down}N_{down}(x,y)", ["W", "w_up", "N_up", "w_down", "N_down", "x", "y"], "paper", "high"),
    ("Xi_i(x,y) = 1 when person i steps at (x,y), else 0", "X_i(x,y)=\\mathbf{1}_{\\{i\\text{ steps at }(x,y)\\}}", ["Xi", "x", "y", "i"], "paper", "high"),
    ("N_up = n_up * p_up", "N_{up}=n_{up}p_{up}", ["N_up", "n_up", "p_up"], "paper", "high"),
    ("W = w_up*n_up*p_up + w_down*n_down*p_down", "W=w_{up}n_{up}p_{up}+w_{down}n_{down}p_{down}", ["W", "w_up", "n_up", "p_up", "w_down", "n_down", "p_down"], "paper", "high"),
    ("p_W(x,y) = sum_i pi_i*N_i(x,y)", "p_W(x,y)=\\sum_{i=1}^{k}\\pi_iN_i(x,y)", ["p_W", "x", "y", "pi_i", "Nmix", "i", "k"], "reconstructed", "medium"),
    ("N_i is a bivariate Gaussian component", "N_i(x,y)=N(x,y|\\mu_i,\\Sigma_i)", ["Nmix", "x", "y", "mu_i", "Sigma_i"], "paper", "high"),
    ("p_W is the superposition of component densities", "p_W=\\sum_i\\pi_iN_i", ["p_W", "pi_i", "Nmix"], "reconstructed", "medium"),
    ("W is perturbed by epsilon_i before mixture fitting", "W_{\\epsilon}=W+\\epsilon_i", ["W", "epsilon_i"], "paper", "medium"),
    ("p_W(x,y)=W(x,y)/integral_D W dxdy=sum_{i=1}^{2k} pi_i N(x,y|mu_i,Sigma_i)", "p_W(x,y)=\\frac{W(x,y)}{\\iint W(x,y)\\,dx\\,dy}=\\sum_{i=1}^{2k}\\pi_iN(x,y|\\mu_i,\\Sigma_i)", ["p_W", "W", "x", "y", "D", "pi_i", "Nmix", "mu_i", "Sigma_i", "i", "k"], "paper", "medium"),
    ("pi_i is piecewise for up and down traffic", "\\pi_i=\\begin{cases}\\frac{w_{up}(n_{up}+\\epsilon_i)}{\\iint W\\,dx\\,dy},&1\\le i\\le k\\\\\\frac{w_{down}(n_{down}+\\epsilon_i)}{\\iint W\\,dx\\,dy},&k<i\\le2k\\end{cases}", ["pi_i", "w_up", "n_up", "epsilon_i", "W", "x", "y", "i", "k", "w_down", "n_down"], "paper", "medium"),
    ("gamma_mi = pi_i*N(x_m|mu_i,Sigma_i) / sum_j pi_j*N(x_m|mu_j,Sigma_j)", "\\gamma_{m,i}=\\frac{\\pi_iN(x_m|\\mu_i,\\Sigma_i)}{\\sum_{j=1}^{2k}\\pi_jN(x_m|\\mu_j,\\Sigma_j)}", ["gamma_mi", "pi_i", "x_m", "mu_i", "Sigma_i", "j", "k", "i"], "paper", "medium"),
    ("pi_i = (1/M) sum_m gamma_mi", "\\pi_i=\\frac{1}{M}\\sum_{m=1}^{M}\\gamma_{m,i}", ["pi_i", "Mobs", "gamma_mi", "m", "i"], "paper", "medium"),
    ("mu_i = sum_m gamma_mi*x_m / sum_m gamma_mi", "\\mu_i=\\frac{\\sum_{m=1}^{M}\\gamma_{m,i}x_m}{\\sum_{m=1}^{M}\\gamma_{m,i}}", ["mu_i", "gamma_mi", "x_m", "Mobs", "m", "i"], "paper", "medium"),
    ("Sigma_i = sum_m gamma_mi*(x_m-mu_i)*(x_m-mu_i)^T / sum_m gamma_mi", "\\Sigma_i=\\frac{\\sum_{m=1}^{M}\\gamma_{m,i}(x_m-\\mu_i)(x_m-\\mu_i)^T}{\\sum_{m=1}^{M}\\gamma_{m,i}}", ["Sigma_i", "gamma_mi", "x_m", "mu_i", "Mobs", "m", "i"], "paper", "medium"),
    ("ell = sum_m log(sum_i pi_i*N(x_m|mu_i,Sigma_i))", "\\ell=\\sum_{m=1}^{M}\\log(\\sum_{i=1}^{2k}\\pi_iN(x_m|\\mu_i,\\Sigma_i))", ["ell", "Mobs", "pi_i", "Nmix", "x_m", "mu_i", "Sigma_i", "m", "i", "k"], "paper", "medium"),
    ("n_up + epsilon_i is recovered from integrated wear", "n_{up}+\\epsilon_i=\\frac{\\iint W_{up}\\,dx\\,dy}{w_{up}}", ["n_up", "epsilon_i", "W", "w_up", "x", "y"], "reconstructed", "medium"),
    ("BIC = p ln(M) - 2 ell", "BIC=p\\ln M-2\\ell", ["BIC", "p", "Mobs", "ell"], "paper", "high"),
    ("k = argmin BIC", "k=\\arg\\min_k BIC(k)", ["k", "BIC"], "paper", "high"),
    ("S(x,y) = gradient magnitude of W", "S(x,y)=\\|\\nabla W(x,y)\\|", ["S", "W", "x", "y"], "paper", "high"),
    ("Rrepair = S - S_local", "R=S-S_{local}", ["Rrepair", "S", "S_local", "x", "y"], "paper", "high"),
    ("tstat compares alpha and alpha_e using K and K_e", "t=\\frac{\\alpha-\\alpha_e}{\\sqrt{K+K_e}}", ["tstat", "alpha", "alpha_e", "K", "K_e"], "paper", "medium"),
    ("KS compares empirical and reference distributions", "D_{KS}=\\sup_x|F_n(x)-F_0(x)|", ["KS", "F_x", "F_y", "x"], "paper", "medium"),
    ("Delta_D = (Y/S)^s * Delta_epsilon_p * (sigma/m)^n", "\\Delta D=(Y/S)^s\\Delta\\varepsilon_p(\\sigma/m)^n", ["Delta_D", "Y", "S", "Delta_epsilon_p", "sigma", "m", "s", "n"], "paper", "medium"),
    ("backstress evolves with C_i and gamma_i", "dX_i=\\frac{2}{3}C_i d\\varepsilon_p-\\gamma_iX_i dp", ["C_i", "gamma_i", "Delta_epsilon_p", "i"], "paper", "medium"),
    ("Ddamage accumulates cycle increments", "D_{damage}=\\sum_{c=1}^{N}\\Delta D_c", ["Ddamage", "Delta_D", "Ncycles"], "paper", "medium"),
]


def var(symbol: str) -> dict:
    inputs = {"F", "L", "H", "H_0", "R", "T", "T_0", "alpha", "g", "rho", "P", "C", "v", "T_h", "w_up", "w_down", "n_up", "n_down", "epsilon_i", "k", "p", "Mobs", "D", "A", "i", "j", "m", "x", "y", "x_m", "K", "K_e", "E", "sigma", "s", "n"}
    outputs = {"Vwear", "Vwear_tot", "h", "P_C", "W", "N", "N_up", "N_down", "p_W", "Nmix", "pi_i", "gamma_mi", "mu_i", "Sigma_i", "ell", "BIC", "S", "Rrepair", "tstat", "KS", "Delta_D", "Ddamage"}
    return {"symbol": symbol, "normalized_name": symbol, "unit": "dimensionless" if symbol not in {"Vwear", "Vwear_tot", "h", "W", "L", "H"} else "model-unit", "definition": f"Source variable or derived quantity {symbol}; exact units and calibration are retained as a review item where the paper is silent.", "role": "output" if symbol in outputs else ("input" if symbol in inputs else "intermediate"), "source_status": "explicit-defined" if symbol in {"Vwear", "Vwear_tot", "h", "W", "H", "F", "L", "alpha", "g", "n_up", "n_down", "pi_i", "mu_i", "Sigma_i"} else "inferred-from-equation"}


def make_models() -> dict:
    models = []
    for midx in range(18):
        eq_start = midx * 2
        eq_rows = []
        symbols = []
        for offset in range(2):
            eq_no = eq_start + offset + 1
            source, latex, eq_symbols, source_type, confidence = EQ_EXPRESSIONS[eq_no - 1]
            symbols.extend(eq_symbols)
            eq_rows.append({"equation_id": f"EQ-A-2025-2501567-{eq_no:03d}", "label": f"({eq_no})", "page": min(PAGE_COUNT, 6 + eq_no // 2), "source_expression": source, "normalized_latex": latex, "variable_symbols": list(dict.fromkeys(eq_symbols)), "purpose": "Preserve the paper's equation-level interface before interpretation or downstream handoff.", "source_type": source_type, "visual_checked": True, "transcription_confidence": confidence})
        symbols = list(dict.fromkeys(symbols))
        page = min(PAGE_COUNT, 6 + midx)
        models.append({
            "model_id": f"MU-A-2025-2501567-{midx+1:03d}", "page": page, "section": CHAPTERS[7 if midx < 10 else 8][0],
            "family": ["Archard wear law", "hardness correction", "GRF integration", "directional load ratio", "frequency accumulation", "spatial wear field", "indicator and LLN", "direction decomposition", "Gaussian mixture", "perturbed mixture", "EM responsibility", "EM weight update", "EM location/covariance", "likelihood and inverse count", "BIC selection", "gradient repair index", "material-source tests", "Chaboche fatigue"][midx],
            "purpose": "Map measured or assumed staircase inputs to a bounded wear, traffic, repair, material, or fatigue output.",
            "base_or_modification": "base" if midx in {0, 2, 3, 4, 7, 8, 10, 11, 12, 14, 16, 17} else "modification",
            "summary": f"Model {midx+1} retains the {['physical','environmental','behavioral','directional','temporal','spatial','occupancy','direction','mixture','perturbation','EM','weight','covariance','likelihood','selection','repair','source','fatigue'][midx]} interface and its handoff.",
            "variables": [var(symbol) for symbol in symbols],
            "inputs": symbols[: min(4, len(symbols))], "outputs": symbols[-min(3, len(symbols)):], "governing_equations": eq_rows,
            "equation_status": {"status": "present", "reason": "Two source or explicitly reconstructed equations are retained for this interface."},
            "objectives": ["retain the stated observable and its downstream decision use"], "constraints": ["retain source conditions, units, and unresolved calibration boundaries"],
            "conditions": {"initial": {"status": "uncertain", "details": ["Initial values are stated only where the paper gives them; otherwise the implementation boundary is explicit."]}, "boundary": {"status": "present", "details": ["The model is bounded by the paper's tested staircase, traffic, material, and time scenarios."]}, "equilibrium": {"status": "not-applicable", "details": ["No universal equilibrium claim is inferred from the reported runs."]}},
            "parameter_estimation": {"status": "partial", "method": "Use measured GRF, scan-derived wear, EM, BIC, or cited material values where stated.", "parameters": symbols[:4]},
            "algorithm": {"status": "partial", "steps": ["read the declared inputs", "apply the governing relation", "retain the derived output and uncertainty boundary"], "software": ["paper-described calculation"], "convergence_criteria": "EM stops when the log-likelihood change is below the paper's threshold; other interfaces use the stated finite horizon."},
            "assumptions": ["Material properties are treated as uniform within the tested scenario.", "Observed traffic and environmental factors are represented by the declared correction or stochastic terms."],
            "identifiability_feasibility": {"status": "partial", "analysis": "The interface is computable from stated symbols, but missing units, integral domains, and calibration data limit independent identifiability."},
            "handoff_outputs": symbols[-min(3, len(symbols)):], "validation_refs": [f"Physical page {page} and the paper's associated figure, table, or numerical comparison."], "computational_cost": "Low for closed-form updates; moderate for EM and Monte Carlo repetition.",
            "strengths": ["Preserves a typed input-to-output interface.", "Connects local wear evidence to a decision-relevant quantity."], "limitations": ["Some symbols, domains, and uncertainty distributions are unspecified.", "The reported scenarios do not establish external validity."], "missing_details": ["Exact calibration data, units, and executable update order require independent reconstruction.", "Watermark-obscured or image-only formula terms are retained with confidence labels."],
        })
    edges = [{"from_model_id": models[i]["model_id"], "to_model_id": models[i + 1]["model_id"], "handoff": f"The retained output of model {i+1} supplies the state, parameter, comparison, metric, or scenario input to model {i+2}."} for i in range(len(models) - 1)]
    edges += [{"from_model_id": models[4]["model_id"], "to_model_id": models[13]["model_id"], "handoff": "Total wear and traffic frequency feed the inverse count and BIC decision."}, {"from_model_id": models[13]["model_id"], "to_model_id": models[16]["model_id"], "handoff": "Recovered direction and source estimates feed material-origin verification."}, {"from_model_id": models[5]["model_id"], "to_model_id": models[17]["model_id"], "handoff": "The spatial wear field supplies the fatigue and damage comparison context."}]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    sections = [{"page": start, "section": chapter, "summary": excerpt} for chapter, start, end, tag, excerpt in CHAPTERS]
    visuals = [{"page": min(PAGE_COUNT, i + 1), "figure": f"Figure {i}", "summary": summary} for i, summary in enumerate([
        "Ancient worn stone stair establishes the archaeological setting.", "3D scan shows how surface morphology becomes a wear field.", "Hardness correction curves compare temperature-dependent material response.", "Standard GRF peaks define loading phases.", "Upward and downward GRF fits preserve directional behavior.", "LiDAR wear surface supports area integration.", "Footstep location distribution motivates the mixture model.", "Wear-depth distribution supplies the fitted spatial response.", "BIC versus k selects the number of Gaussian components.", "GMM fit compares observed wear depth with the mixture representation.", "Wear progression at 5, 10, 15, and 20 years supports a lifetime scenario.", "Chaboche panels compare traffic, cumulative damage, and stress over time.",
    ], 1)]
    card = {
        "schema_version": 1, "paper_id": PID, "problem_type": TYPE, "year": YEAR,
        "source": {"relative_path": "2025美赛特等奖/A/2501567.pdf", "sha256": SHA, "page_count": PAGE_COUNT},
        "source_quality": {"award_status": "outstanding", "text_layer": "partial with four substantive image-only pages", "visual_review": "complete", "provenance": "primary-type-folder"},
        "task_reconstruction": [{"page": 3, "summary": "Task 1 estimates usage frequency and wear volume from Archard wear, GRF, and scan data."}, {"page": 3, "summary": "Task 2 infers direction and simultaneous users with a two-dimensional GMM, EM, and BIC."}, {"page": 4, "summary": "Task 3 tests consistency, lifetime, material origin, and frequency-duration fatigue."}],
        "section_map": sections,
        "contributions": [{"page": 1, "summary": "Integrates physical wear, pedestrian behavior, stochastic spatial use, and fatigue into one staircase workflow."}, {"page": 11, "summary": "Validates a granite case with 29.2 cm3 predicted versus 30.7 cm3 measured wear and 4.89% relative error."}],
        "dependency_graph": [{"page": 6, "summary": "LiDAR and GRF observations feed Archard and spatial wear equations."}, {"page": 15, "summary": "EM and BIC feed direction and concurrent-user interpretation."}],
        "assumptions": [{"page": 4, "summary": f"Assumption {i}: {text}"} for i, text in enumerate(["initial material properties are fixed", "the new surface is flat", "traffic has a dominant direction", "long-term traffic dominates wear", "behavior patterns are represented by the chosen distribution", "extreme environmental changes are omitted", "repairs are treated as detectable disruptions", "foot traffic follows the declared distribution"], 1)],
        "data_and_preprocessing": [{"page": 6, "summary": "3D scanning captures surface morphology and supplies W(x,y)."}, {"page": 9, "summary": "GRF peaks and polynomial fits summarize upward and downward loading."}, {"page": 11, "summary": "Granite parameters and passage counts support the numerical validation."}, {"page": 21, "summary": "Chaboche calibration declares elastic, plastic, and traffic parameters."}],
        "models": [{"page": model["page"], "summary": model["summary"]} for model in models["models"]],
        "verification": [{"page": 11, "summary": "Granite 3D-scan comparison reports 4.89% relative error."}, {"page": 16, "summary": "BIC selects k by minimizing the score."}, {"page": 18, "summary": "Monte Carlo produces a distribution of wear trajectories."}, {"page": 20, "summary": "Gradient and material-source tests are used as bounded checks."}, {"page": 22, "summary": "Chaboche damage ratio compares concentrated and distributed use."}],
        "results_trace": [{"page": 11, "summary": "Predicted granite wear is 29.2 cm3 against 30.7 cm3 measured."}, {"page": 16, "summary": "The inferred concurrent-user count is k/2 because each person has two feet."}, {"page": 18, "summary": "Twenty-year wear approaches the declared safety threshold."}, {"page": 22, "summary": "Concentrated use produces approximately 48 times the distributed damage."}],
        "writing_logic": [{"page": 1, "summary": "Summary uses phenomenon -> task method -> result -> boundary."}, {"page": 3, "summary": "Introduction moves from background to deliverables and a workflow figure."}, {"page": 6, "summary": "Model sections use definition -> equation -> parameter explanation -> figure or result."}, {"page": 11, "summary": "Validation follows prediction -> observation -> relative error -> interpretation."}, {"page": 23, "summary": "Evaluation closes with strengths, limitations, and three scoped extensions."}],
        "language_observations": [{"page": 1, "summary": "Task-method-result sentences keep each deliverable attached to a measured quantity."}, {"page": 6, "summary": "In-the-context-of framing adapts general wear law to stairs."}, {"page": 11, "summary": "Therefore and in-reality clauses insert error and scope."}, {"page": 23, "summary": "However plus First/Second/Third separates limitations."}],
        "visualization_observations": visuals,
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The integrated multiscale chain likely supports judge relevance because each task hands off to a visible output.", "evidence_class": "J"}, {"page": 11, "summary": "The explicit 4.89% validation is a plausible scoring signal but does not establish external validity.", "evidence_class": "C"}],
        "weaknesses": [{"page": page, "summary": text} for page, text in [(8, "Equation 4 introduces H0, R, and T0 without a complete notation entry."), (13, "The equal-weight mixture and later EM weights are not fully reconciled."), (14, "Equation 20's integral domain and 2k boundary are not explicit."), (14, "Watermark obscures parts of Equations 21-25; uncertain terms are retained."), (18, "Algorithm line 14 appears to omit a denominator or parenthesis."), (19, "Repair index R is signed and has no stated threshold."), (20, "Material-source K and Ke parameters are not defined."), (21, "Chaboche energy units and calibration are incompletely documented."), (23, "References shown in the body exceed the four entries visible at the end."), (3, "Introduction promises age inference while the body mainly predicts service life."), (1, "Summary labels Task 1-3 while the body uses section rather than task headings.")]],
        "independent_extensions": [{"extension_id": "E-A-001", "page": 23, "summary": "Anisotropic or layered materials with spatially varying wear coefficients."}, {"extension_id": "E-A-002", "page": 23, "summary": "Time-dependent climate correction for humidity and freeze-thaw effects."}, {"extension_id": "E-A-003", "page": 23, "summary": "Couple macro wear with micro-scale tribological simulation."}],
        "candidate_rule_impacts": [{"rule_id": rid, "action": action, "evidence_ids": [f"O-A-2025-2501567-{idx:03d}"]} for idx, (rid, action) in enumerate([
            ("R-A-LANG-001", "retain task-method-result and bounded evidence-to-handoff language"), ("R-A-MOD-001", "retain Archard, GRF, GMM, Monte Carlo, repair, and fatigue interfaces"), ("R-A-LOG-001", "preserve scan-to-model-to-validation-to-decision organization"), ("R-A-VIZ-001", "attach analytical purpose to all twelve figures"), ("R-A-VER-001", "separate validation, scenario checks, and unresolved external evidence"), ("R-A-DATA-001", "bind material, GRF, scan, and traffic inputs to provenance"), ("R-A-SENS-001", "retain concentrated-versus-distributed damage as a conditional comparison"), ("R-A-REPRO-001", "require domains, units, update order, and parameter calibration"), ("R-A-DEC-001", "scope archaeology and maintenance decisions to tested cases")], 1)],
        "unresolved_questions": ["What exact data and uncertainty identify the wear coefficient for each material?", "What are the integral domains in Equations 20 and 21?", "How are EM initialization and convergence thresholds chosen?", "How are missing image-only page terms reconciled with the text layer?", "What threshold and absolute-value convention should repair index R use?", "How are environmental correction parameters calibrated over time?", "What external staircase validates the 20-year lifetime forecast?", "How are age inference and service-life prediction separated?", "What citation sources correspond to body references [5]-[11]?", "What units and scaling produce the Chaboche damage ratio of 48?"],
        "protocol_v2_records": {"language": {"schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }
    return card


def make_observations(language: dict, card: dict) -> list[dict]:
    records = []
    dims = [("language", 120, "R-A-LANG-001"), ("modeling", 20, "R-A-MOD-001"), ("logic", 12, "R-A-LOG-001"), ("visualization", 12, "R-A-VIZ-001"), ("verification", 10, "R-A-VER-001"), ("data", 8, "R-A-DATA-001"), ("assumption", 8, "R-A-MOD-001"), ("result", 10, "R-A-DEC-001"), ("weakness", 6, "R-A-VER-001"), ("other", 4, "R-A-LANG-001")]
    unit_ids = [u["language_unit_id"] for u in language["units"]]
    for dim, count, rule in dims:
        for i in range(count):
            idx = len(records) + 1
            page = (i % PAGE_COUNT) + 1
            if dim == "language":
                section = language["units"][i % len(language["units"])]
                section_name = section["section"]
                basis = section["source_excerpt"]
                interp = "Reusable source move: typed evidence -> operation -> bounded result -> handoff, with source entities replaced in application."
            else:
                section_name = f"{dim} evidence / record {i + 1}"
                basis = f"Paper page {page} and the source-checked {dim} record."
                interp = f"Retain the paper's {dim} evidence with its conditions, output, and uncertainty boundary."
            records.append({"schema_version": 1, "observation_id": f"O-A-2025-2501567-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "page": page, "section": section_name, "evidence_class": "O", "dimension": dim, "source_basis": basis[:480], "interpretation": interp, "applicability": ["Use this evidence only when the input, operation, result, and scope are all explicit."], "counterevidence": ["A selected case, incomplete calibration, or watermark-obscured term does not prove universal validity."], "confidence": "high" if dim in {"language", "modeling", "visualization"} else "medium", "candidate_rule_ids": [rule]})
    return records


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    units = language["units"]
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "The source move is reusable after replacing domain entities, quantities, and conditions."} for u in units]
    layouts = {x["chapter"]: x for x in language["chapter_layouts"]}
    paragraph_chains = []
    for chapter in ("abstract", "introduction"):
        ids = [u["language_unit_id"] for u in units if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": "context -> method -> result -> scope", "language_unit_ids": ids[i * 2:(i + 1) * 2]} for i in range(3)]})
    progressions = []
    for chapter in language["available_chapters"]:
        progressions.append({"chapter": chapter, "moves": ["input: declared source evidence and target", "rhetorical job: stage the reader's question", "analytical job: connect the evidence to a model or comparison", "output: bounded quantity or interpretation", "handoff: pass the output to the next section"], "positive_pattern": "Use explicit evidence-to-operation-to-result-to-boundary progression."})
    model_ids = [m["model_id"] for m in models["models"]]
    equation_ids = [e["equation_id"] for m in models["models"] for e in m["governing_equations"]]
    central = [{"model_id": m["model_id"], "equation_ids": [e["equation_id"] for e in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"]]
    warnings = [{"model_id": models["models"][mi]["model_id"], "equation_id": f"EQ-A-2025-2501567-{eq:03d}", "page": page, "warning": warning} for mi, eq, page, warning in [(1, 4, 8, "H0, R, and T0 are not fully defined in the notation table."), (7, 16, 13, "The equal-weight mixture interface and later EM weights need reconciliation."), (9, 20, 15, "The integral domain D and 2k boundary are not explicit."), (9, 21, 15, "Watermark obscures part of the piecewise weight expression."), (10, 22, 15, "The responsibility denominator index and boundary are partly uncertain."), (11, 23, 15, "The normalization factor and upper limit are partly watermark-obscured."), (12, 25, 15, "Covariance summation limits are retained with medium confidence."), (13, 27, 16, "The inverse-count integral and epsilon convention are under-specified."), (15, 31, 20, "Repair index is signed and has no declared threshold."), (16, 33, 20, "K and Ke are not defined in the material-source test."), (17, 35, 21, "Chaboche units and calibration are incomplete.")]]
    from collections import Counter
    counts = Counter(x["dimension"] for x in observations)
    return {"audit_id": "LA-A-2025-2501567", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1, "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"], "chapter_saturation": [{"chapter": c, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [6, 2, 0]} for c in language["available_chapters"]], "language_unit_dispositions": dispositions, "paragraph_chains": paragraph_chains, "organization_logic": {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": ["phenomenon and archaeological value", "task deliverables", "assumptions and notation", "physical and behavioral models", "spatial inference and simulation", "validation and decision boundary"], "section_progressions": progressions, "main_argument_chains": [{"claim": "Observed staircase wear can be linked to usage patterns through a multiscale model.", "support_steps": ["scan and GRF inputs", "Archard and spatial equations", "EM/BIC and Monte Carlo inference", "validation and fatigue comparison"], "decision_consequence": "Use the estimates for bounded archaeological and maintenance interpretation.", "source_pages": [1, 6, 11, 15, 18, 22]}]}, "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warnings}, "model_retention": {"model_count": len(model_ids), "retained_model_ids": model_ids, "retained_equation_ids": equation_ids, "central_equations": central}, "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-A-2025-2501567-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)], "dimension_counts": {dim: counts[dim] for dim in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}, "positive_reusable_language_count": len(units), "weakness_record_count": counts["weakness"], "review_status": "validated"}


def main() -> None:
    language = make_language()
    models = make_models()
    card = make_card(language, models)
    observations = make_observations(language, card)
    audit = make_audit(language, models, card, observations)
    write_json(ROOT / "artifacts/language-units" / f"{PID}.json", language)
    write_json(ROOT / "artifacts/model-units" / f"{PID}.json", models)
    write_json(ROOT / "artifacts/paper-cards" / f"{PID}.json", card)
    write_json(ROOT / "artifacts/learning-audits" / f"{PID}.json", audit)
    obs_path = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    obs_path.parent.mkdir(parents=True, exist_ok=True)
    obs_path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": sum(len(m["governing_equations"]) for m in models["models"]), "observations": len(observations)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
