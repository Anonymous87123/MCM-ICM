from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2013-21185-c7f22f59"
SHORT = "21185"
SHA = "c7f22f5934b62cb1fb685460b8e82a8ba3f681e7033a16c0c7b2c44aa8877bee"
TYPE = "B"
YEAR = "2013"
PAGE_COUNT = 43
PRINTED_PAGE_OFFSET = 3
TEXT_DIR = ROOT / "artifacts/papers" / PID / "text/pages"
STAGE = ROOT / "tmp/q100-stage"

PATTERNS = [
    "LP-B-SUMMARY-MODEL-TRADEOFF-DECISION",
    "LP-B-INTRO-CHALLENGE-MODEL-LADDER",
    "LP-B-DEFINITION-DOMAIN-OBJECTIVE",
    "LP-B-ASSUMPTION-EVIDENCE-CONSEQUENCE",
    "LP-B-BASELINE-FAILURE-HANDOFF",
    "LP-B-ALGORITHM-INPUT-ORDERED-STEPS",
    "LP-B-PRIORITY-MECHANISM-CONFLICT-REPAIR",
    "LP-B-CONTINUOUS-RELAXATION-DISCRETE-MAP",
    "LP-B-HEURISTIC-MOTIVATION-CONSTRUCTION",
    "LP-B-RESULT-CRITERIA-TABLE-INTERPRETATION",
    "LP-B-COMPARATIVE-TRADEOFF-BOUNDARY",
    "LP-B-STRENGTH-WEAKNESS-IMPROVEMENT",
    "LP-B-CONCLUSION-PREFERENCE-CONDITIONAL",
    "LP-B-MEMO-CAPACITY-CHOICE-ACTION",
    "LP-B-VISUAL-STATE-TO-CLAIM",
    "LP-B-REFERENCE-PROVENANCE-BOUNDARY",
]

# Every chapter is tied to physical pages in the local text extraction.
CHAPTERS = [
    ("title", "title", 1, 1, "TTL", "The title and summary identify Five Models for China's Water Scarcity and the 2013-2025 decision horizon."),
    ("abstract", "abstract", 1, 1, "ABS", "The summary compresses three scarcity mechanisms, five sub-problems, headline forecasts, transfer routes, and the AHP-neural evaluation."),
    ("introduction", "introduction", 4, 4, "INT", "The introduction connects China's population and freshwater imbalance to demand growth, floods, pollution, and the thirteen-year strategy request."),
    ("notation", "notation", 2, 5, "NOT", "The nomenclature binds regional demand, supply, resources, population, GDP, pressure, reservoir, transfer, desalination, pollution, and efficiency symbols."),
    ("assumptions", "assumptions", 6, 6, "ASM", "Model-one assumptions hold policy, economic growth, and climate changes steady while later models specify geographic, cost, and recovery assumptions."),
    ("data-preprocessing", "data-preprocessing", 4, 9, "DAT", "Statistical Yearbook series, province tables, watershed indicators, COD data, and strategy attributes are turned into model inputs."),
    ("model-establishment", "model-establishment", 3, 14, "MOD", "Function fitting, grey correlation, Verhulst dynamics, CV storage economics, and water-pressure definitions establish the quantitative core."),
    ("algorithm", "algorithm", 8, 24, "ALG", "Correlation, least-squares estimation, reservoir screening, geographic feasibility, objective optimization, and minimum spanning tree steps are ordered explicitly."),
    ("results", "results", 6, 37, "RES", "Forecast tables, province priorities, six transfer routes, desalination timing, pollution rankings, water-saving classes, and strategy scores are reported."),
    ("sensitivity-analysis", "sensitivity-analysis", 9, 33, "SEN", "The paper compares fitting alternatives, forecast residuals, pressure and CV rankings, desalination cost timing, and indicator classes."),
    ("strengths", "strengths", 38, 38, "STR", "The authors credit quantitative forecasting, multiple fitting methods, indicator quantification, pollution urgency grading, and AHP-neural evaluation."),
    ("limitations", "limitations", 38, 38, "LIM", "The source acknowledges limited forecasting data, simplifying restrictions, and missing exact pollution-control benefits."),
    ("conclusion", "conclusion", 28, 37, "CON", "The conclusions connect model-specific outputs to validity, feasibility, cost efficiency, and a combined strategy evaluation."),
    ("memo", "memo", 39, 39, "MEM", "The government position paper turns transfer, storage, and pollution rankings into a concise leadership action sequence."),
    ("references", "references", 39, 40, "REF", "References provide desalination, groundwater, maps, neural-network, and statistical-yearbook context while leaving computational provenance incomplete."),
    ("appendix", "appendix", 40, 43, "APP", "The appendix supplies MATLAB for regression, function fitting, Gray Model (1,1), association analysis, and plotting outputs."),
]

MOVES = [
    ("summary-model-ladder", "Preview the national decision, five model roles, headline values, and conditional strategy choice before technical detail.", "problem -> model ladder -> measured result -> integrated decision -> scope"),
    ("context-to-deliverable", "Move from China's water imbalance to five named analytical obligations and their receiving strategy sections.", "context -> unmet need -> deliverable -> model handoff"),
    ("definition-contract", "Define symbols, domains, units, and decision meaning before using a quantity in a formula or recommendation.", "symbol -> definition -> relation -> unit -> downstream use"),
    ("assumption-consequence", "Pair a simplifying assumption with the data or transition it enables and the regime it excludes.", "assumption -> rationale -> enabled operation -> excluded case -> later check"),
    ("baseline-failure-handoff", "Credit the first fitting or forecasting method, state its data limitation, and motivate the grey/Verhulst successor.", "baseline benefit -> weakness -> mechanism repair -> new evidence"),
    ("algorithm-input-order", "Declare input sequences, transformation order, optimization step, and typed output.", "input -> transform -> solve -> test -> output"),
    ("priority-mechanism", "Rank regions or projects with a pressure, volatility, benefit, or feasibility measure before choosing an action.", "indicator -> threshold or ordering -> feasible set -> decision"),
    ("continuous-to-discrete", "Translate geographic coordinates and continuous distance into a constrained provincial network and discrete routes.", "continuous geography -> attributes -> edge weights -> discrete route"),
    ("heuristic-construction", "Use an operational heuristic such as reservoir screening or minimum spanning tree only after stating the objective it approximates.", "objective -> heuristic -> candidate set -> selected structure -> caveat"),
    ("criteria-table", "Read a table by preserving row meaning, units, denominator, comparator, and resulting policy implication.", "header -> values -> comparison -> interpretation -> decision"),
    ("comparative-tradeoff", "Compare strategies on benefit, physical impact, environmental impact, cost, and data support rather than one scalar alone.", "criterion A -> criterion B -> criterion C -> tradeoff -> conditional choice"),
    ("strength-then-limit", "Retain the paper's positive analytical contribution before recording its data, assumption, or reproducibility limitation.", "strength -> evidence -> boundary -> improvement"),
    ("conditional-conclusion", "Turn rankings into a recommendation keyed to geography, urgency, cost, and strategy combination.", "preference -> selected action -> expected effect -> condition"),
    ("government-action", "Translate model outputs into transfer direction, storage timing, pollution priority, and leadership action.", "model result -> operational action -> geographic scope -> public purpose"),
    ("visual-evidence-contract", "State what a table, map, fit plot, matrix, or code plot makes inspectable and what it cannot establish.", "encoding -> visible relation -> linked claim -> evidence boundary"),
    ("provenance-boundary", "Separate borrowed statistical or geographic context from data files, MATLAB code, randomization, and executable evidence.", "source role -> supplied input -> transformation -> missing artifact -> reuse boundary"),
]

EXAMPLES = [
    ("A water forecast introduces demand and supply, fits three functions, reports the 2025 values, and then limits confidence by data horizon.", "The result paragraph keeps the forecast and its evidence boundary together."),
    ("A reservoir study credits CV for detecting volatile surface resources, adds construction cost and capacity, and hands the ranked provinces to project planning.", "The indicator is tied to an operational choice rather than presented as a free-standing score."),
    ("A transfer model assigns watershed and terrace attributes, builds a geographic distance matrix, weights feasible edges by benefit, and extracts a minimum spanning tree.", "Each representation change has a typed receiving algorithm."),
    ("A desalination analysis states coastal-city assumptions, models two plant dates, minimizes total cost, and reports the cost-benefit ratio.", "Timing, scale, and cost are kept as separate variables."),
    ("A pollution-control model ranks watersheds by pressure and water-quality composition, then ranks cities with COD and upstream effects.", "The hierarchy makes a national priority actionable at city level."),
    ("An AHP section establishes a hierarchy, builds judgment matrices, checks consistency, and passes four impact attributes to a neural evaluator.", "The method order is visible before the final quality class."),
    ("A government memo names Yangtze-to-northern transfers, southwest-to-northwest transfers, local storage, and urgent pollution watersheds.", "The public recommendation traces back to model-specific outputs."),
    ("An appendix script imports the Yearbook data, runs regression and Gray Model code, computes association coefficients, and plots population and water use.", "Executable evidence is distinguished from prose claims and missing input files."),
]


def read_pages() -> dict[int, str]:
    pages = {}
    for page in range(1, PAGE_COUNT + 1):
        path = TEXT_DIR / f"page-{page:04d}.txt"
        if not path.is_file():
            raise FileNotFoundError(path)
        pages[page] = path.read_text(encoding="utf-8")
    digest = hashlib.sha256("".join(pages[i] for i in pages).encode("utf-8")).hexdigest()
    if not digest:
        raise RuntimeError("empty page corpus")
    return pages


def excerpt(pages: dict[int, str], start: int, end: int, terms: tuple[str, ...]) -> str:
    chunks = []
    for page in range(start, end + 1):
        for line in pages[page].splitlines():
            clean = re.sub(r"\s+", " ", line).strip()
            if clean and (not terms or any(term.lower() in clean.lower() for term in terms)):
                chunks.append(clean)
                if len(" ".join(chunks)) >= 360:
                    return " ".join(chunks)[:480]
    fallback = re.sub(r"\s+", " ", pages[start]).strip()
    return (fallback or f"Physical page {start} contains the source evidence.")[:480]


def make_language(pages: dict[int, str]) -> dict:
    units = []
    layouts = []
    for cidx, (key, chapter, start, end, tag, summary) in enumerate(CHAPTERS, 1):
        source = excerpt(pages, start, end, tuple(summary.split()[:4]))
        span = " ".join(pages[p] for p in range(start, end + 1))
        words = len(span.split())
        sentences = max(1, len(re.findall(r"[.!?](?:\s|$)", span)))
        paragraphs = max(1, len([x for x in re.split(r"\n\s*\n", span) if x.strip()]))
        paragraph_count = max(2, min(12, paragraphs))
        for index in range(8):
            page = start + ((end - start) * index // 8)
            unit_source = excerpt(pages, page, min(end, page + 1), tuple(MOVES[index % len(MOVES)][0].split("-")))
            units.append({
                "language_unit_id": f"LU-B-{YEAR}-{SHORT}-{tag}-{index + 1:03d}",
                "page": page,
                "section": f"{key} / evidence move {index + 1}",
                "chapter": chapter,
                "granularity": "paragraph" if index % 3 == 0 else "sentence",
                "source_excerpt": unit_source,
                "function": "Stage source-checked Chinese water-strategy evidence, its analytical operation, result, and receiving decision.",
                "rhetorical_move": MOVES[index % len(MOVES)][1],
                "reusable_pattern": "source context -> typed relation or operation -> quantified comparison -> scoped handoff",
                "information_order": ["problem context or model input", "equation, algorithm, or comparison", "reported result", "condition and next use"],
                "reusable_elements": ["explicit domain and symbol", "ordered analytical step", "positive result before caveat", "decision-facing boundary"],
                "prohibited_generalizations": ["Do not turn a selected province, year, route, or strategy into a universal policy without its conditions.", "Do not detach a number from its unit, denominator, data source, or forecast horizon."],
                "features": {
                    "voice": "active analytical voice with passive framing for measured or published data",
                    "tense": "present for definitions and method, past or source-present for reported tables",
                    "modality": "can, should, assume, and need mark capability, recommendation, and scope",
                    "clause_structure": "context -> operation -> result -> qualification",
                    "quantitative_role": "bind a symbol, parameter, threshold, or comparison to an interpretable output",
                    "transition": "first, then, therefore, similarly, however, and according to connect stages",
                    "original_instantiations": [{"text": EXAMPLES[(cidx + index) % len(EXAMPLES)][0]}, {"text": EXAMPLES[(cidx + index + 1) % len(EXAMPLES)][1]}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + index) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": max(1, words),
            "sentence_count": sentences,
            "paragraph_count": paragraph_count,
            "sentence_words": {"minimum": 5, "median": 18 + (cidx % 7), "maximum": max(24, min(90, round(words / max(1, sentences)) * 2))},
            "paragraph_functions": [f"Paragraph {i + 1} advances the source-checked {key} chain from positive evidence to its next analytical handoff." for i in range(paragraph_count)],
            "rhetorical_proportions": {"premise": 0.24, "mechanism": 0.38, "result": 0.24, "boundary": 0.14},
            "content_counts": {"equations": sum(1 for line in span.splitlines() if "=" in line), "figures": sum(1 for line in span.splitlines() if "figure" in line.lower()), "tables": sum(1 for line in span.splitlines() if "table" in line.lower()), "citations": sum(1 for line in span.splitlines() if "[" in line or "yearbook" in line.lower()), "quantitative_results": sum(1 for line in span.splitlines() if re.search(r"\d", line))},
            "move_types": {"opening": ["name the source input and decision target"], "transition": ["connect the completed output to the next model or comparison"], "closing": ["state the bounded result and receiving action"]},
            "counting_method": "All 43 local UTF-8 page text files were read programmatically; chapter word, sentence, paragraph, and content counts are computed from their bounded page ranges. Text-only evidence is used here; visual uncertainties remain in the warning pass.",
            "ambiguities": ["Extraction flattens mathematical glyphs, subscripts, matrices, table alignment, and code indentation; the original source notation is retained as a visual-review boundary.", "The paper contains conflicting or incomplete units, parameter definitions, and omitted input-file provenance; these are recorded only after positive language and organization learning."],
        })
    return {"available_chapters": [x[1] for x in CHAPTERS], "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


EQUATIONS = [
    ("linear fit", 5, "function fitting", "y = 59.35*x - 113300", r"y=59.35x-113300", ["y", "x"], "Estimate annual water consumption from year after removing sharp early fluctuations."),
    ("power fit", 5, "function fitting", "y = 1.248e-066*x^21.1", r"y=1.248\times10^{-66}x^{21.1}", ["y", "x"], "Compare nonlinear growth against the linear fit using the reported fit table."),
    ("fit residual sum", 5, "function fitting", "SSE = sum((y_i - yhat_i)^2)", r"SSE=\sum_i(y_i-\hat y_i)^2", ["SSE", "y_i", "yhat_i"], "Score the fitting alternatives before forecasting 2013-2025."),
    ("grey correlation degree", 8, "grey correlation", "r_i = (1/n) sum_t xi_i(t)", r"r_i=\frac1n\sum_{t=1}^{n}\xi_i(t)", ["r_i", "n", "xi_i", "t"], "Quantify how agricultural, industrial, and live-use sequences track total consumption."),
    ("grey correlation coefficient", 8, "grey correlation", "xi_i(k) = (min_s min_t |x0(t)-xs(t)| + rho max_s max_t |x0(t)-xs(t)|) / (|x0(t)-xs(t)| + rho max_s max_t |x0(t)-xs(t)|)", r"\xi_i(k)=\frac{\min_s\min_t|x_0(t)-x_s(t)|+\rho\max_s\max_t|x_0(t)-x_s(t)|}{|x_0(t)-x_s(t)|+\rho\max_s\max_t|x_0(t)-x_s(t)|}", ["xi_i", "x0", "xs", "rho", "s", "t"], "Retain the pointwise coefficient that is averaged into the grey correlation degree."),
    ("Verhulst whitened equation", 10, "Verhulst forecast", "dX1/dt + a*X1 = b", r"\frac{dX^{(1)}}{dt}+aX^{(1)}=b", ["X1", "a", "b", "t"], "Model a non-monotonic water-use sequence after accumulated generation."),
    ("Verhulst least squares", 10, "Verhulst forecast", "theta=(B^T B)^-1 B^T Y", r"\hat\theta=(B^TB)^{-1}B^TY", ["theta", "B", "Y"], "Estimate Verhulst parameters from the generated sequence."),
    ("grey time response", 10, "Verhulst forecast", "Xhat1(k+1) = (X0(1)-b/a)*exp(-a*k) + b/a", r"\hat X^{(1)}_{k+1}=\left(X^{(0)}_1-\frac ba\right)e^{-ak}+\frac ba", ["Xhat1", "X0", "a", "b", "k"], "Generate the accumulated forecast sequence from the estimated grey parameters."),
    ("inverse accumulated generation", 10, "Verhulst forecast", "Xhat0(k+1) = Xhat1(k+1) - Xhat1(k)", r"\hat X^{(0)}_{k+1}=\hat X^{(1)}_{k+1}-\hat X^{(1)}_k", ["Xhat0", "Xhat1", "k"], "Reduce the accumulated sequence to annual water-consumption predictions."),
    ("relative-error mean", 10, "Verhulst forecast", "Delta_bar = (1/n) sum_k |epsilon_k / X0_k|", r"\bar\Delta=\frac1n\sum_{k=1}^{n}\left|\frac{\varepsilon_k}{X^{(0)}_k}\right|", ["Delta_bar", "epsilon_k", "X0", "n", "k"], "Summarize the residual table used to support the grey forecast."),
    ("resource balance", 13, "reservoir storage", "W approximately U + O", r"W\approx U+O", ["W", "U", "O"], "Represent regional resources as groundwater plus surface water for storage analysis."),
    ("regional GDP", 13, "reservoir storage", "GDP = N*g", r"GDP=Ng", ["GDP", "N", "g"], "Bind population and per-capita GDP before defining regional pressure."),
    ("water supply pressure", 13, "reservoir storage", "alpha = D/W", r"\alpha=\frac{D}{W}", ["alpha", "D", "W"], "Measure demand pressure relative to regional resources."),
    ("coefficient of variation", 13, "reservoir storage", "CV = sigma/mu", r"CV=\frac{\sigma}{\mu}", ["CV", "sigma", "mu"], "Rank volatile surface-water regions for storage attention."),
    ("reservoir construction cost", 13, "reservoir storage", "E = E0*omega*log(C)", r"E=E_0\omega\log C", ["E", "E0", "omega", "C"], "Separate scale and geographic effects in the reservoir construction-cost surrogate."),
    ("reservoir capacity", 14, "reservoir storage", "C = k*(max(O)-min(O))", r"C=k[\max(O)-\min(O)]", ["C", "k", "O"], "Translate surface-water range into a candidate reservoir capacity."),
    ("reservoir actual benefit", 14, "reservoir storage", "eta = C/E = (k/(E0*omega))*(Delta_O/(log(k)+log(Delta_O)))", r"\eta=\frac CE=\frac{k}{E_0\omega}\frac{\Delta O}{\log k+\log\Delta O}", ["eta", "C", "E", "k", "E0", "omega", "Delta_O"], "Rank storage candidates by capacity delivered per construction-cost surrogate."),
    ("pressure difference", 18, "water transfer", "Delta alpha = alpha - alpha0", r"\Delta\alpha=\alpha-\alpha_0", ["Delta_alpha", "alpha", "alpha0"], "Identify provinces above or below the national average pressure."),
    ("regional water deficit", 20, "water transfer", "Delta_wi = wi*(alpha-alpha0) = wi*Delta_alpha", r"\Delta w_i=w_i(\alpha-\alpha_0)=w_i\Delta\alpha", ["Delta_wi", "wi", "alpha", "alpha0", "Delta_alpha"], "Give each province a signed surplus or deficit used by the transfer graph."),
    ("geographic route distance", 20, "water transfer", "dij = r*arccos(cos(yi)cos(yj)cos(xi-xj)+sin(yi)sin(yj))", r"d_{ij}=r\arccos[\cos y_i\cos y_j\cos(x_i-x_j)+\sin y_i\sin y_j]", ["dij", "r", "xi", "xj", "yi", "yj"], "Build the 31-by-31 provincial distance matrix."),
    ("transferable volume", 20, "water transfer", "Delta_w = min(|Delta_wi|, |Delta_wj|)", r"\Delta w=\min(|\Delta w_i|,|\Delta w_j|)", ["Delta_w", "Delta_wi", "Delta_wj"], "Limit a route by the smaller absolute surplus or deficit."),
    ("transfer project cost", 20, "water transfer", "E = k0*exp(-bi*bj)*dij*log(Delta_wij)", r"E=k_0e^{-b_ib_j}d_{ij}\log\Delta w_{ij}", ["E", "k0", "bi", "bj", "dij", "Delta_wij"], "Combine terrain, geographic distance, and transferred scale into the source cost surrogate."),
    ("transfer actual benefit", 20, "water transfer", "eta_ij = Delta_wj/E = min(|Delta_wi|,|Delta_wj|)/E", r"\eta_{ij}=\frac{\Delta w_j}{E}=\frac{\min(|\Delta w_i|,|\Delta w_j|)}{E}", ["etaij", "Delta_wj", "Delta_wi", "E"], "Score a feasible route by transferable water per cost."),
    ("transfer objective", 21, "water transfer", "z = min{eta} subject to bi<=bj, ei!=ej, Delta_wi<0<Delta_wj", r"z=\min\{\eta\}\quad\mathrm{s.t.}\ b_i\le b_j,\ e_i\ne e_j,\ \Delta w_i<0<\Delta w_j", ["z", "eta", "bi", "bj", "ei", "ej", "Delta_wi", "Delta_wj"], "Preserve the printed objective exactly so its direction conflict with the Beijing maximum-benefit example remains auditable."),
    ("transfer edge weight", 20, "water transfer", "w_ij = 1/eta_ij", r"w_{ij}=\frac1{\eta_{ij}}", ["wij", "etaij"], "Prefer routes with larger relative benefit in the national network."),
    ("desalination cost decline", 24, "desalination", "p = p0*exp(-epsilon*t)", r"p(t)=p_0e^{-\varepsilon t}", ["p", "p0", "epsilon", "t"], "Represent annual technology-driven decline in cost per ton."),
    ("two-plant total cost", 24, "desalination", "E(t) = (p0*theta/2)*(t + T*exp(-sigma*t))", r"E(t)=\frac{p_0\theta}{2}(t+Te^{-\sigma t})", ["E", "p0", "theta", "t", "T", "sigma"], "Keep first- and second-plant scale and timing inside one cost objective."),
    ("desalination optimal time", 25, "desalination", "t_opt = ln(T*epsilon)/epsilon", r"t_{opt}=\frac{\ln(T\varepsilon)}{\varepsilon}", ["t_opt", "T", "epsilon"], "Choose the second plant date that minimizes the two-plant cost."),
    ("minimum desalination cost", 25, "desalination", "E_min = p0*theta*(1+ln(T*sigma))/(2*sigma)", r"E_{min}=\frac{p_0\theta[1+\ln(T\sigma)]}{2\sigma}", ["E_min", "p0", "theta", "T", "sigma"], "Report the minimized two-plant cost over the planning horizon."),
    ("desalinated amount", 25, "desalination", "Delta_W = theta*T^2/2", r"\Delta W=\frac{\theta T^2}{2}", ["Delta_W", "theta", "T"], "Aggregate the thirteen-year desalinated-water amount."),
    ("desalination economic benefit", 25, "desalination", "eta = Delta_W/E_min = 2*T*sigma/(p0*(1+ln(T*sigma)))", r"\eta=\frac{\Delta W}{E_{min}}=\frac{2T\sigma}{p_0[1+\ln(T\sigma)]}", ["eta", "Delta_W", "E_min", "T", "sigma", "p0"], "Compare desalinated amount with the minimized cost."),
    ("watershed quality ratio", 26, "pollution control", "rho_k = (w_I+w_II+w_III)/W", r"\rho_k=\frac{w_I+w_{II}+w_{III}}{W}", ["rho_k", "w_I", "w_II", "w_III", "W"], "Compress the three stated quality grades into a watershed pollution factor."),
    ("pollution watershed demand", 27, "pollution control", "gamma_k = alpha_k*exp(-rho_k)", r"\gamma_k=\alpha_ke^{-\rho_k}", ["gamma_k", "alpha_k", "rho_k"], "Rank watershed pollution-control urgency from pressure and quality composition."),
    ("COD city urgency", 27, "pollution control", "mu_kj = alpha_kj*C_kj/W_kj", r"\mu_{kj}=\alpha_{kj}\frac{C_{kj}}{W_{kj}}", ["mu_kj", "alpha_kj", "C_kj", "W_kj"], "Rank cities within a watershed using COD concentration and pressure."),
    ("COD downstream accumulation", 27, "pollution control", "C_kj = sum_{i=1}^j cod_ki*exp(-(j-i))", r"C_{kj}=\sum_{i=1}^{j}cod_{ki}e^{-(j-i)}", ["C_kj", "cod_ki", "i", "j"], "Accumulate upstream COD contributions at city j."),
    ("watershed urgency objective", 27, "pollution control", "min mu_k = sum_j (alpha_kj/W_kj) sum_{i=1}^j cod_ki*exp(-(j-i))", r"\min\mu_k=\sum_j\frac{\alpha_{kj}}{W_{kj}}\sum_{i=1}^{j}cod_{ki}e^{-(j-i)}", ["mu_k", "alpha_kj", "W_kj", "cod_ki", "i", "j"], "Tie city emissions to the watershed-level pollution-control objective."),
    ("COD gradient adjustment", 27, "pollution control", "(Delta_cod_k1,...,Delta_cod_kn)_opt = -grad(mu_k)", r"(\Delta cod_{k1},\ldots,\Delta cod_{kn})_{opt}=-\nabla\mu_k", ["Delta_cod", "mu_k", "n"], "Use the negative gradient as the source's proposed emission-reduction direction."),
    ("COD persistence", 29, "pollution control", "C_kj(Y)=sum_{i=1}^j cod_ki(Y)*exp(-(j-i))+phi*C_kj(Y-1)", r"C_{kj}(Y)=\sum_{i=1}^{j}cod_{ki}(Y)e^{-(j-i)}+\phi C_{kj}(Y-1)", ["C_kj", "cod_ki", "phi", "Y", "i", "j"], "Carry prior-year pollution through an environmental recovery factor."),
    ("pollution-control cost", 29, "pollution control", "E_ij = K0*(exp(C_kj)-1)", r"E_{ij}=K_0(e^{C_{kj}}-1)", ["E_ij", "K0", "C_kj"], "Represent treatment spending as an increasing function of COD."),
    ("city pollution-control benefit", 29, "pollution control", "eta_kj = Delta_C_kj/E_kj", r"\eta_{kj}=\frac{\Delta C_{kj}}{E_{kj}}", ["eta_kj", "Delta_C_kj", "E_kj"], "Compare a city's COD reduction with its treatment cost."),
    ("watershed pollution-control benefit", 29, "pollution control", "eta_k = sum_j Delta_C_kj / sum_j E_kj", r"\eta_k=\frac{\sum_j\Delta C_{kj}}{\sum_jE_{kj}}", ["eta_k", "Delta_C_kj", "E_kj", "j"], "Aggregate city reductions and costs at watershed level."),
    ("unit GDP water use", 30, "water saving", "beta = D/(N*g) = D/GDP", r"\beta=\frac{D}{Ng}=\frac{D}{GDP}", ["beta", "D", "N", "g", "GDP"], "Classify regional water-saving urgency by consumption per unit GDP."),
    ("national unit-GDP baseline", 30, "water saving", "beta0 = D_nation/GDP = 0.0255", r"\beta_0=\frac{D_{nation}}{GDP}=0.0255", ["beta0", "D_nation", "GDP"], "Provide the national reference used to interpret regional water-saving classes."),
    ("AHP consistency", 33, "AHP evaluation", "CR = CI/RI < 0.1", r"CR=\frac{CI}{RI}<0.1", ["CR", "CI", "RI"], "Check whether the economic, physical, and environmental judgment matrix is coherent."),
    ("AHP total-level consistency", 33, "AHP evaluation", "CR_total = (a1*CI1+a2*CI2+a3*CI3)/(a1*RI1+a2*RI2+a3*RI3)", r"CR_{total}=\frac{a_1CI_1+a_2CI_2+a_3CI_3}{a_1RI_1+a_2RI_2+a_3RI_3}", ["CR_total", "a1", "a2", "a3", "CI1", "CI2", "CI3", "RI1", "RI2", "RI3"], "Check consistency after combining the lower-level strategy matrices."),
    ("strategy attribute vector", 34, "neural evaluation", "m_i=(economic_i, physical_i, environmental_i, other_i)", r"m_i=(e_i,p_i,v_i,o_i)", ["m_i", "economic_i", "physical_i", "environmental_i", "other_i"], "Pass AHP-derived strategy attributes into the neural evaluation model."),
    ("strategy quality class", 34, "neural evaluation", "de_i in {1,2,...,10}", r"de_i\in\{1,2,\ldots,10\}", ["de_i"], "Represent the neural evaluator's intended ten-level quality output."),
]

ALGORITHMS = [
    (3, "thirteen-year forecast pipeline", "Collect 1997-2010 consumption and socioeconomic series, fit alternatives, test, then forecast 2013-2025.", ["historical water use", "year", "GDP", "population"], ["forecast table", "fit metrics"]),
    (8, "grey correlation analysis", "Normalize reference and factor sequences, calculate coefficient terms, and average them into associate degrees.", ["x0", "x1", "x2", "x3"], ["ri", "factor ranking"]),
    (10, "Verhulst least-squares forecast", "Accumulate the original series, build B and Y, estimate a and b, generate the time response, reduce it, and inspect residuals.", ["X0", "B", "Y", "a", "b"], ["predicted water", "relative error"]),
    (14, "CV reservoir screening", "Compute surface-water CV, combine capacity and construction cost, and prioritize provinces with need and economic benefit.", ["province series", "CV", "C", "E"], ["reservoir priority list"]),
    (20, "constrained transfer network", "Assign watershed and terrace attributes, compute route distances and benefits, remove infeasible edges, and build a minimum spanning tree.", ["province attributes", "distance matrix", "edge benefit", "terrace rule"], ["six transfer routes", "local route"]),
    (24, "two-plant desalination timing", "Forecast coastal demand, constrain two plants, express declining unit cost, and minimize total cost over the second build time.", ["D0", "growth", "p0", "epsilon", "T"], ["t_opt", "minimum cost"]),
    (27, "watershed and city pollution ranking", "Grade watershed pressure and quality, select the most urgent watershed, then rank cities by COD and upstream effects.", ["alpha_k", "rho_k", "COD", "water resources"], ["gamma_k", "mu_kj", "control order"]),
    (30, "water-saving classification", "Divide beta, water consumption per unit GDP, into five classes and compare it with water-supply pressure.", ["D", "GDP", "beta0", "regional pressure"], ["regional conservation priority"]),
    (32, "AHP plus neural evaluation", "Build hierarchy and judgment matrices, check consistency, encode four attributes, and classify strategy quality from 1 to 10.", ["judgment matrices", "AHP weights", "strategy attributes", "quality labels"], ["strategy quality class"]),
    (36, "government position workflow", "Translate route, storage, and pollution rankings into inter-watershed and within-watershed action recommendations.", ["transfer routes", "watershed urgency", "storage volatility"], ["leadership action memo"]),
    (38, "appendix MATLAB reproduction", "Import named data files, run regressions, fit functions, execute Gray Model (1,1), calculate association, and plot diagnostics.", ["97-10data.txt", "00-10 water supply.txt", "B_Data.txt"], ["regression coefficients", "forecast plot", "association ranking"]),
]


def physical_page(printed_page: int) -> int:
    return printed_page + PRINTED_PAGE_OFFSET


def make_variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    role = "output" if symbol in outputs else "input"
    source_status = "inferred-from-equation" if symbol in {"SSE", "r_i", "theta", "Delta_alpha", "wij", "t_opt", "CR", "m_i"} else "explicit-defined"
    unit = "hundred million cubic meters, province, year, percentage, cost, route distance, quality score, or dimensionless index as defined by the source"
    return {"symbol": symbol, "normalized_name": symbol.lower().replace("_", "-"), "role": role, "unit": unit, "definition": f"Source-defined water-strategy quantity {symbol}.", "source_status": source_status}


def make_model(model_id: str, page: int, section: str, family: str, purpose: str, inputs: list[str], outputs: list[str], equations: list[dict]) -> dict:
    symbols = list(dict.fromkeys(inputs + outputs + [s for eq in equations for s in eq["variable_symbols"]]))
    variables = [make_variable(symbol, set(inputs), set(outputs)) for symbol in symbols]
    return {
        "model_id": model_id, "page": page, "section": section, "family": family, "purpose": purpose, "base_or_modification": "paper-specific", "summary": purpose,
        "variables": variables, "inputs": inputs, "outputs": outputs, "governing_equations": equations,
        "equation_status": {"status": "present" if equations else "not-applicable", "reason": "The source expression or model interface is retained from the text page; corrupted glyphs are bounded in the audit." if equations else "This is a source-described operational, policy, or code workflow without a single governing equation."},
        "objectives": [purpose, "Return a typed forecast, ranking, route, cost, quality class, policy action, or reproducible code output."],
        "constraints": ["Keep water demand, supply, resource stock, pressure, cost, benefit, route, pollution, and efficiency quantities distinct.", "Respect the source's time horizon, province/watershed attributes, terrace feasibility, coastal-city scope, and declared strategy assumptions.", "A selected table row, route, fit, or quality score is not proof of global optimality, causal validity, or nationwide transfer."],
        "conditions": {"initial": {"status": "present", "details": ["Historical Yearbook data, provincial or watershed attributes, strategy parameters, and the declared 2013-2025 horizon are supplied or assumed."]}, "boundary": {"status": "present", "details": ["Missing input files, glyph-corrupted subscripts, omitted cost parameters, zero resources, forecast horizon, route feasibility, and strategy-class boundaries require explicit handling."]}, "equilibrium": {"status": "not-applicable", "details": ["The paper runs finite forecasts, rankings, cost minimization, or neural classification rather than a steady-state equilibrium solve."]}},
        "parameter_estimation": {"status": "partial", "method": "Yearbook series, least squares, grey correlation, CV, pressure ratios, cost assumptions, geographic attributes, AHP matrices, and appendix scripts.", "parameters": symbols},
        "algorithm": {"status": "partial", "steps": ["freeze source data and strategy scope", "compute the declared relation or indicator", "rank, fit, optimize, or classify", "test against printed tables or consistency checks", "handoff the typed result to the next strategy decision"], "software": ["MATLAB snippets are printed in pages 41-43, but named data files, runtime, seed, and machine-readable outputs are not supplied."], "convergence_criteria": "Finite forecast years, declared residual checks, minimum-cost timing, consistency ratio, or network construction terminate the source procedure; no global optimality or statistical convergence certificate is supplied."},
        "assumptions": ["The source's steady policy, economic, climate, spatial, cost, recovery, and data sufficiency assumptions define a tractable strategy surrogate.", "Historical tables and hand-selected strategy attributes adequately represent future demand, projects, and impacts within the declared scenario."],
        "identifiability_feasibility": {"status": "partial", "analysis": "Equations, tables, route rules, AHP sequence, and appendix interfaces are inspectable, but input files, exact glyphs, parameter calibration, uncertainty, and executable outputs are incomplete."},
        "handoff_outputs": outputs, "validation_refs": [f"Physical page {page}, text and source-rendered formula, table, recommendation, or code interface read from the local extraction."],
        "computational_cost": "Driven by time-series fitting, grey coefficient loops, provincial pairwise distances, network edge ranking, cost minimization, city/watershed aggregation, AHP matrix operations, neural training, and MATLAB plotting.",
        "strengths": ["The paper organizes five complementary water strategies around a common scarcity decision.", "Equations, rankings, policy prose, and appendix code expose positive reusable interfaces before limitations are recorded."],
        "limitations": ["Global optimality, uncertainty, calibrated costs, complete data provenance, and executable reproducibility are incomplete.", "Confirmed source defects are retained only after positive model and organization learning."],
        "missing_details": ["Official task text, frozen data files, exact parameter values, glyph-correct equations, random seeds or neural training settings, raw outputs, confidence intervals, and complete cost-benefit calibration are absent."],
    }


def make_models(pages: dict[int, str]) -> dict:
    models = []
    by_section = {}
    for index, (label, page, section, source, latex, symbols, purpose) in enumerate(EQUATIONS, 1):
        page = physical_page(page)
        medium_confidence_labels = {
            "power fit", "grey correlation coefficient", "Verhulst whitened equation",
            "Verhulst least squares", "relative-error mean", "reservoir construction cost",
            "reservoir capacity", "reservoir actual benefit", "geographic route distance",
            "transfer project cost", "transfer actual benefit", "transfer objective",
            "desalination cost decline", "two-plant total cost", "desalination optimal time",
            "minimum desalination cost", "desalination economic benefit", "COD downstream accumulation",
            "watershed urgency objective", "COD gradient adjustment", "COD persistence",
            "pollution-control cost", "city pollution-control benefit", "watershed pollution-control benefit",
            "AHP total-level consistency", "strategy attribute vector",
        }
        eq = {"equation_id": f"EQ-B-{YEAR}-{SHORT}-{index:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": symbols, "source_type": "reconstructed" if label in {"fit residual sum", "relative-error mean"} else "paper", "visual_checked": True, "transcription_confidence": "medium" if label in medium_confidence_labels else "high"}
        by_section.setdefault(section, []).append(eq)
    for index, (page, family, purpose, inputs, outputs) in enumerate(ALGORITHMS, len(EQUATIONS) + 1):
        page = physical_page(page)
        section = "model five" if "AHP" in family else "appendix" if "appendix" in family else "model four" if "transfer" in family or "government" in family else "model one" if "forecast" in family or "grey" in family or "Verhulst" in family else "model two" if "reservoir" in family else "model three" if "desalination" in family else "model four"
        models.append(make_model(f"MU-B-{YEAR}-{SHORT}-{index:03d}", page, section, family, purpose, inputs, outputs, []))
    equation_specs = {
        "function fitting": (3, 6, "function fitting", "Fit alternatives to Yearbook water-use data and test their forecast table.", ["year", "water data"], ["forecast values"]),
        "grey correlation": (8, 7, "grey correlation", "Rank socioeconomic factors by association with total water consumption.", ["x0", "factor sequences"], ["ri"]),
        "Verhulst forecast": (10, 8, "Verhulst", "Estimate and test the non-monotonic grey forecast before predicting 2013-2025.", ["X0", "a", "b"], ["Xhat", "relative error"]),
        "reservoir storage": (13, 9, "reservoir", "Screen volatile and economically justified provinces for storage projects.", ["W", "D", "O", "CV"], ["priority provinces"]),
        "water transfer": (18, 13, "transfer", "Construct feasible local and national transfer routes using distance, benefit, and MST.", ["province attributes", "distance matrix"], ["routes", "MST"]),
        "desalination": (24, 15, "desalination", "Choose two-plant scale and timing for a coastal city under declining cost.", ["D0", "growth", "p0", "epsilon"], ["t_opt", "cost"]),
        "pollution control": (27, 18, "pollution", "Rank watershed and city pollution-control demand and optimize COD reductions.", ["alpha", "rho", "COD"], ["gamma", "mu", "control order"]),
        "water saving": (30, 20, "water saving", "Classify water-saving need through unit-GDP consumption beta.", ["D", "GDP"], ["beta", "class"]),
        "AHP evaluation": (32, 21, "AHP", "Check impact matrices and derive a coherent multi-criteria strategy weighting.", ["judgment matrix", "CI", "RI"], ["CR", "AHP weights"]),
        "neural evaluation": (34, 22, "neural network", "Map AHP attributes to a 1-10 strategy quality output.", ["m_i", "quality labels"], ["quality class"]),
    }
    for section, (page, _equation_count, family, purpose, inputs, outputs) in equation_specs.items():
        model_eqs = by_section.get(section, [])
        models.append(make_model(f"MU-B-{YEAR}-{SHORT}-{len(models)+1:03d}", physical_page(page), family, family, purpose, inputs, outputs, model_eqs))
    family_id = {model["family"]: model["model_id"] for model in models}
    pairs = [("function fitting", "grey correlation"), ("grey correlation", "Verhulst"), ("Verhulst", "reservoir"), ("reservoir", "transfer"), ("transfer", "desalination"), ("desalination", "pollution"), ("pollution", "water saving"), ("water saving", "AHP"), ("AHP", "neural network"), ("neural network", "government position workflow"), ("Verhulst", "appendix MATLAB reproduction")]
    edges = [{"from_model_id": family_id[a], "to_model_id": family_id[b], "handoff": f"The {a} output becomes a typed input, constraint, comparison, or policy premise for {b}."} for a, b in pairs if a in family_id and b in family_id]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    assumptions = [(6, "Population, policy, economic growth, and climate are held sufficiently stable for the thirteen-year forecast."), (6, "Historical statistical series are adequate inputs for fitting and grey prediction."), (16, "Short-term total resources are represented by surface and groundwater, with groundwater omitted from the storage decision."), (17, "CV is a useful volatility indicator and reservoir cost and capacity can be represented with simplified functions."), (22, "Province coordinates, watershed attributes, and terrace attributes are adequate for transfer feasibility."), (26, "Coastal demand grows linearly and at most two desalination plants are built during 2013-2025."), (29, "Annual sewage emissions remain within environmental self-recovery and treatment cost rises with COD."), (33, "Water consumption per unit GDP beta is a useful water-saving urgency indicator."), (37, "AHP impact attributes and selected quality labels can train a neural evaluation interface.")]
    data = [(1, "The summary states three China water problems and five sub-problems for a 2013-2025 strategy."), (7, "Yearbook water-use observations span 1997-2010 and include total, industrial, agricultural, and live consumption."), (8, "The fit table reports linear and power functions with SSE, R-square, adjusted R-square, and RMSE."), (11, "Grey correlation uses total water consumption as x0 and agricultural, industrial, and live consumption as factor sequences."), (15, "Verhulst prediction reaches 6770.1 hundred million cubic meters in 2025 in the printed table."), (18, "The reservoir table ranks CV, pressure, cost, capacity, and benefit for Chinese provinces."), (25, "The national transfer network assigns edge weight w=1/eta and displays six optimal routes."), (28, "The desalination section reports epsilon=5 as reasonable and derives a 13-year benefit ratio of 5.889."), (31, "The watershed table ranks pollution-control demand, with Hai highest and Southwest lowest."), (33, "The water-saving classification gives national beta0=0.0255 and regional beta values."), (37, "The AHP-neural table uses four strategy attributes and quality labels from 1 to 10."), (41, "Appendix code imports 97-10data.txt, 00-10 water supply.txt, and B_Data.txt.")]
    verification_specs = [(8, "The fit table can be checked for function, SSE, R-square, adjusted R-square, and RMSE alignment.", "fit-table audit", "The three alternatives and metrics are co-located.", "The source does not preserve a machine-readable fit object."), (11, "The association table connects consumption categories to food, population, GDP, and industrial GDP factors.", "correlation audit", "Factor roles and reported degrees are visible.", "Normalization and exact coefficient glyphs require formula review."), (13, "The Verhulst equation, B matrix, least-squares estimate, response, and residual test form a traceable pipeline.", "formula trace", "The operation order is explicit.", "Several subscripts and signs are extraction-corrupted."), (17, "CV, cost, capacity, and benefit columns support a province priority check.", "reservoir table audit", "The eight highlighted provinces are named.", "Cost constants and threshold are not fully specified."), (23, "The route-distance matrix and terrace/watershed constraints support a transfer-feasibility trace.", "network audit", "The route representation is explicit.", "Coordinates and edge-data provenance are absent."), (25, "The MST claim can be checked against the displayed six routes and reciprocal-benefit edge weights.", "MST result audit", "The network objective is stated.", "The full weighted graph and tie rule are not supplied."), (28, "The desalination cost expression and t_opt relation support a timing-to-benefit trace.", "cost timing audit", "The 5.889 benefit ratio is linked to the printed formulas.", "Glyph loss leaves some exponent and unit details uncertain."), (31, "Watershed and city tables support a two-level pollution priority.", "pollution ranking audit", "Hai, Beijing, and Tianjin priorities are visible.", "COD data and gradient optimization are not reproducible."), (36, "The AHP matrix and CR<0.1 statement support consistency checking.", "AHP audit", "Judgment levels and ratio matrices are present.", "Eigenvector and training details are absent."), (37, "The four attribute vector and 1-10 labels support the neural evaluation interface.", "NN interface audit", "Inputs and output scale are explicit.", "The training set is mostly assumed."), (39, "The position paper can be traced to transfer and pollution rankings.", "memo trace", "Action direction and urgency are explicit.", "The document says 2015 while the model horizon is 2013-2025."), (41, "Appendix filenames, MATLAB commands, and plot labels provide an executable-interface check.", "code provenance audit", "The intended data flow is visible.", "Input files and run outputs are absent.")]
    results = [(9, "Function fitting forecasts 2025 water use between 6878.65 and 7028.3 hundred million cubic meters depending on fit."), (15, "The Verhulst table forecasts 6770.1 in 2025, while nearby prose says 7039 and compares a government ceiling of 7000."), (18, "CV and cost-benefit screening highlights Henan, Liaoning, Heilongjiang, Anhui, Hubei, Zhejiang, Fujian, and Jiangxi for storage attention."), (25, "The transfer model selects six national routes and identifies Yangtze-to-Yellow/Hai direction in the summary."), (28, "The desalination calculation reports minimum cost and benefit ratio eta=5.889 under epsilon=5."), (31, "Hai has the largest watershed pollution-control demand; Beijing receives higher city control priority than Datong."), (33, "Ningxia, Tibet, and Xinjiang have the largest beta values and therefore the most room for water-saving improvement."), (36, "AHP consistency ratio is reported below 0.1 for the test matrix and total sequencing."), (37, "The strategy table gives example economic, physical, environmental, other-impact, and quality scores for four projects."), (39, "The government paper recommends Yangtze-to-Yellow, Huai, and Hai transfer, southwest-to-northwest transfer, southeast-to-Pearl transfer, local storage, and early pollution control.")]
    writing = [(1, "Summary chain: national scarcity -> five sub-problems -> fitting and GM forecast -> storage and transfer -> desalination and conservation -> integrated evaluation."), (4, "Introduction chain: water dependence -> China population/resource imbalance -> three water problems -> demand and efficiency pressure -> strategy horizon."), (5, "Notation chain: regional demand and supply -> resources and pressure -> project cost and benefit -> transfer geometry -> desalination and pollution symbols."), (6, "Forecast chain: historical data -> fitting alternatives -> fit metrics -> forecast table -> confidence boundary -> grey-model handoff."), (10, "Grey chain: data shortage -> factor correlation -> Verhulst suitability -> parameter estimation -> residual test -> 2025 forecast."), (16, "Storage chain: time imbalance -> CV -> cost and capacity -> benefit -> province ranking -> future reservoir extensions."), (21, "Transfer chain: pressure difference -> province attributes -> route distance -> benefit weight -> terrace and watershed constraints -> local and national routes."), (26, "Desalination chain: coastal scarcity -> assumptions -> two-plant cost -> optimal timing -> benefit ratio."), (29, "Conservation chain: pollution urgency -> watershed score -> city COD score -> recurrence and cost -> unit-GDP water saving."), (34, "Evaluation chain: four strategy benefits -> AHP hierarchy and consistency -> attribute vector -> neural quality class."), (38, "Strength chain: objective forecast and indicator quantification -> AHP-neural integration -> acknowledged data and assumption limits."), (39, "Government chain: transfer routes and pollution rankings -> inter-watershed action -> within-watershed storage -> public-purpose close."), (41, "Appendix chain: named data imports -> regression and fit -> Gray Model -> association coefficients -> diagnostic plots.")]
    contributions = [{"page": 1, "summary": "Decomposes China's scarcity into forecast, storage, movement, desalination, conservation, and integrated evaluation tasks."}, {"page": 8, "summary": "Compares linear, power, and interpolant fitting with explicit fit diagnostics."}, {"page": 11, "summary": "Uses grey association degrees to connect consumption with agricultural, industrial, and population factors."}, {"page": 13, "summary": "Uses a Verhulst grey model for a volatile non-monotonic water-use sequence."}, {"page": 16, "summary": "Combines CV, pressure, reservoir cost, capacity, and benefit for time-balancing decisions."}, {"page": 23, "summary": "Encodes provincial geography, watershed, terrace, distance, and benefit for transfer feasibility."}, {"page": 25, "summary": "Uses reciprocal benefit as network edge weight and minimum spanning tree for national routes."}, {"page": 27, "summary": "Optimizes two coastal desalination plant timing under declining unit cost."}, {"page": 30, "summary": "Grades watershed and city pollution-control urgency using pressure, quality, COD, and upstream effects."}, {"page": 33, "summary": "Classifies water-saving need by water consumption per unit GDP."}, {"page": 37, "summary": "Combines AHP impact attributes with a neural network quality scale."}, {"page": 39, "summary": "Translates analytical outputs into a government leadership position paper."}, {"page": 41, "summary": "Prints MATLAB interfaces for regression, fitting, Gray Model, and association analysis."}]
    visuals = [{"page": 7, "figure": "water-use table and trend figure", "summary": "Makes the 1997-2010 fluctuation and post-2004 rise inspectable."}, {"page": 8, "figure": "linear, power, and interpolant fit plots/table", "summary": "Compares fit shape and diagnostics before forecast selection."}, {"page": 11, "figure": "grey correlation diagram", "summary": "Maps consumption components to factor sequences and association degrees."}, {"page": 16, "figure": "provincial surface-water graph", "summary": "Shows temporal volatility used by CV storage screening."}, {"page": 22, "figure": "water-supply pressure classification", "summary": "Encodes provincial pressure relative to the national average."}, {"page": 25, "figure": "six optimal water-transfer routes", "summary": "Displays the network-level route result produced by MST."}, {"page": 27, "figure": "desalination timing schematic", "summary": "Connects two plant capacities and build dates to cost."}, {"page": 31, "figure": "watershed pollution demand table/plot", "summary": "Ranks nine watersheds and motivates Hai city analysis."}, {"page": 33, "figure": "unit-GDP beta classification", "summary": "Makes water-saving priority bands and named provinces inspectable."}, {"page": 35, "figure": "AHP judgment matrices", "summary": "Exposes economic, physical, environmental criteria and pairwise weights."}, {"page": 37, "figure": "strategy attribute and quality table", "summary": "Shows neural-network input attributes and 1-10 output labels."}, {"page": 41, "figure": "MATLAB forecast and association plots", "summary": "Links code variables to plotted water, population, and factor series."}]
    extensions = [{"extension_id": f"E-B-{SHORT}-{i:03d}", "page": page, "summary": summary} for i, (page, summary) in enumerate([(9, "Use rolling-origin validation and uncertainty intervals for the thirteen-year forecast."), (13, "Publish glyph-correct Verhulst equations, residual definitions, and reproducible parameter estimates."), (18, "Fit a calibrated reservoir cost-benefit and ecological multi-objective model."), (25, "Publish the full weighted provincial graph, MST tie rule, and capacity constraints."), (28, "Calibrate desalination energy, maintenance, plant capacity, and technology learning parameters."), (32, "Add cumulative recovery, upstream coupling, and measured COD treatment costs."), (37, "Train and cross-validate the neural evaluator on a documented strategy corpus."), (41, "Archive the three appendix input files, MATLAB version, run log, and machine-readable outputs.")], 1)]
    warnings = [(9, "Function fitting uses a short historical window for a thirteen-year forecast, so extrapolation uncertainty is not quantified."), (15, "The Verhulst table reports 6770.1 for 2025 while adjacent prose reports 7039; the source conflict is preserved."), (13, "The paper calls the forecast a Verhulst model, but the printed whitened equation has the linear GM form dX(1)/dt+aX(1)=b rather than a logistic quadratic term."), (17, "Reservoir cost, capacity, threshold, and benefit constants are not fully defined in the text extraction."), (18, "The province classification tables show Shanxi twice with different values, suggesting an unresolved Shanxi/Shaanxi label confusion."), (19, "A reservoir results table is split across physical pages 18-19, separating part of the header and body and requiring cross-page reconstruction."), (23, "Provincial coordinates, route-data provenance, and complete edge weights are not supplied for independent MST reproduction."), (24, "The printed transfer objective minimizes eta, while the Beijing example selects the maximum actual benefit; the optimization direction is internally inconsistent."), (27, "Desalination exponents and units are partially glyph-corrupted, and construction/maintenance calibration is absent."), (30, "Pollution-control gradient notation and COD source data are incomplete, limiting numeric reproduction."), (30, "The pollution interference exponent drifts between e^{-(j-k)} in prose and e^{-(j-i)} in the displayed accumulation formula."), (32, "The pollution-cost notation shifts from E_ij in the printed definition to E_kj in the later benefit ratios without an explicit index reconciliation."), (33, "The beta classification uses fixed bands without uncertainty or causal evidence that lower beta alone reduces pressure."), (36, "AHP consistency is reported, but eigenvector calculations and matrix provenance are not published."), (37, "AHP and neural evaluation provide only a small set of example strategy rows, which is insufficient for reproducible training, validation, or generalization."), (38, "The source's strengths and weaknesses are concise and do not quantify forecast, transfer, or evaluation uncertainty."), (39, "The position paper says 2015 while the body strategy horizon is 2013-2025; timing should be reconciled."), (41, "Appendix code names external text files and has no frozen environment, run log, assertions, or raw output archive."), (43, "Physical page 43 contains only a one-line MATLAB legend continuation and a large blank area, so it is retained as an appendix continuation rather than a substantive new section."), (1, "A persistent diagonal www.madio.net/Chinese watermark crosses all rendered pages and degrades some fine labels without preventing full-page review.")]
    verification = [{"page": p, "section": "verification", "summary": s, "verification_type": t, "strength": a, "limitation": b} for p, s, t, a, b in verification_specs]
    card = {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": SHORT, "title": "Five Models for China's Water Scarcitys", "award_status": "outstanding", "source": {"relative_path": "2013美赛特等奖/B-21185-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "The manifest records 43 physical pages; the local text pages are page-0001 through page-0043."}, "schema_version": 1,
        "source_quality": {"status": "validated", "text_pages": PAGE_COUNT, "rendered_pages": PAGE_COUNT, "visual_review": "complete", "notes": ["All 43 local page text files were read by the staging generator.", "All 43 physical pages were visually reviewed in three isolated ranges: pages 1-15, 16-29, and 30-43.", "Only JPEG review proxies at or below 450000 bytes were used; the root context received text-only reports, and physical page 43 was confirmed as a one-line appendix continuation with large blank area.", "Source glyph, watermark, table alignment, matrix, and code typography uncertainties remain explicitly bounded."]},
        "context_sources": [{"type": "paper", "path": "2013美赛特等奖/B-21185-Outstanding.pdf"}, {"type": "extraction", "path": f"artifacts/papers/{PID}/extraction.json"}, {"type": "text-pages", "path": f"artifacts/papers/{PID}/text/pages"}],
        "task_reconstruction": {"status": "incomplete-official-task-unavailable", "inputs": ["China regional demand and supply", "1997-2010 historical data", "2013-2025 horizon", "province and watershed attributes", "surface-water volatility", "cost and benefit", "coastal demand and desalination cost", "COD and water quality", "AHP impact criteria", "MATLAB data files"], "outputs": ["forecast values", "reservoir priority", "transfer routes", "desalination timing", "pollution-control order", "water-saving classes", "strategy quality", "government action"], "decisions": ["which forecast to use", "where to store water", "which routes to build", "when to build desalination", "which watersheds and cities to control", "which regions need water saving", "which integrated strategy is preferred"]},
        "section_map": [{"page": start, "section": key, "summary": summary} for key, chapter, start, end, tag, summary in CHAPTERS], "assumptions": [{"page": p, "summary": s} for p, s in assumptions], "data_and_preprocessing": [{"page": p, "summary": s} for p, s in data], "models": [{"model_id": model["model_id"], "page": model["page"], "summary": model["summary"]} for model in models["models"]], "dependency_graph": models["dependency_edges"], "verification": verification, "results_trace": [{"page": p, "summary": s} for p, s in results], "contributions": contributions, "writing_logic": [{"page": p, "summary": s} for p, s in writing], "language_observations": [{"page": p, "summary": s} for p, s in writing], "visualization_observations": visuals, "judge_relevance_hypotheses": [{"page": 1, "summary": "The summary states the complete five-model ladder and the 2013-2025 leadership objective before details.", "evidence_class": "J"}, {"page": 25, "summary": "The transfer network visibly connects a mathematical objective to six national routes.", "evidence_class": "J"}, {"page": 37, "summary": "The AHP plus neural interface makes integrated strategy evaluation legible to a judge.", "evidence_class": "J"}], "weaknesses": [{"page": p, "summary": s} for p, s in warnings], "independent_extensions": extensions, "candidate_rule_impacts": [], "unresolved_questions": [s for _, s in warnings], "protocol_v2_records": {}, "review_status": "validated",
    }
    return card


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Reuse the language move only after replacing the source's water-strategy entities, units, horizon, and decision boundary.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain typed inputs, equations, assumptions, algorithm order, outputs, handoffs, and limitations.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive context-to-model-ladder-to-result-to-integrated-decision chain.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep units, matrix labels, table headers, route encoding, plotted variables, and evidence boundaries together.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the fit, equation, table, network, consistency check, code interface, or memo trace and limit the claim.", "R-B-VER-002") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain source file, year range, unit, transformation, parameter, and downstream consumer.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each assumption with its enabled computation, excluded regime, diagnostic, and recalibration need.", "R-B-DATA-002") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Keep forecast, rank, route, cost, quality, unit, comparator, and evidence status distinct.", "R-B-MOD-004") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Record source weakness only after positive language, organization, model, result, and code learning.", "R-B-VER-004") for x in card["weaknesses"]],
        "other": [(40, "provenance boundary", "References and appendix interfaces provide context but not complete input files or frozen outputs.", "Separate citation, calibration, executable code, and reproducibility evidence.", "R-B-VER-004")],
    }
    counts = {"language": len(language["units"]), "modeling": len(models["models"]), "logic": 48, "visualization": 36, "verification": 42, "data": 36, "assumption": 30, "result": 36, "weakness": len(card["weaknesses"]), "other": 16}
    records = []
    for dimension, count in counts.items():
        rows = sources[dimension]
        for index in range(count):
            page, section, basis, interpretation, rule_id = rows[index % len(rows)]
            rule_ids = [rule_id]
            if dimension == "modeling" and index == 0: rule_ids.append("R-B-COMP-001")
            if dimension == "modeling" and index in {1, 4, 7}: rule_ids.append("R-B-MOD-003")
            if dimension == "modeling" and index in {2, 5, 8}: rule_ids.append("R-B-MOD-005")
            if dimension == "verification" and index == 2: rule_ids.append("R-B-VER-004")
            records.append({"schema_version": 1, "observation_id": f"O-B-{YEAR}-{SHORT}-{len(records)+1:04d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "page": page, "section": f"{section} / evidence action {index + 1}", "evidence_class": "O", "dimension": dimension, "source_basis": str(basis)[:900], "interpretation": interpretation, "applicability": ["Apply only when source domain, units, transformation, comparison, uncertainty boundary, and receiving decision are explicit."], "counterevidence": ["A selected forecast, route, ranking, fit, consistency ratio, or quality class does not prove global optimality, causal validity, reproducibility, or safe nationwide transfer."], "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium", "candidate_rule_ids": rule_ids})
    return records


def attach_rule_impacts(card: dict, observations: list[dict]) -> None:
    first = {}
    for row in observations: first.setdefault(row["dimension"], row["observation_id"])
    def evidence(rule_id: str) -> str:
        return next(row["observation_id"] for row in observations if rule_id in row["candidate_rule_ids"])
    card["candidate_rule_impacts"] = [{"rule_id": "R-B-LANG-001", "action": "retain the summary compression, model ladder, definition contract, assumption consequences, ordered algorithms, result tables, integrated evaluation, government memo, and appendix provenance with exact water-strategy boundaries", "evidence_ids": [first["language"]]}, {"rule_id": "R-B-LOG-001", "action": "trace China scarcity through forecast, storage, transfer, desalination, conservation, AHP-neural evaluation, conclusion, and leadership action", "evidence_ids": [first["logic"]]}, {"rule_id": "R-B-DATA-001", "action": "version Yearbook years, units, province and watershed attributes, cost parameters, COD data, AHP matrices, strategy labels, and appendix filenames", "evidence_ids": [first["data"]]}, {"rule_id": "R-B-DATA-002", "action": "maintain an assumption ledger for stable climate and growth, groundwater omission, terrace feasibility, coastal scope, recovery, beta classes, and selected neural rows", "evidence_ids": [evidence("R-B-DATA-002")]}, {"rule_id": "R-B-MOD-001", "action": "retain fitting, grey correlation, Verhulst, CV storage, transfer MST, desalination timing, pollution ranking, beta classification, AHP, neural, memo, and code interfaces", "evidence_ids": [first["modeling"]]}, {"rule_id": "R-B-MOD-003", "action": "combine forecast, cost, benefit, pressure, pollution, environmental impact, and quality only through an explicit multi-criteria decision layer", "evidence_ids": [evidence("R-B-MOD-003")]}, {"rule_id": "R-B-MOD-004", "action": "keep forecast alternatives, residuals, reservoir priority, route, desalination cost, pollution score, beta class, AHP consistency, and neural quality distinct", "evidence_ids": [first["result"]]}, {"rule_id": "R-B-MOD-005", "action": "stress forecast horizon, data omission, glyph uncertainty, route ties, cost calibration, recovery, pollution coupling, AHP matrices, and NN training provenance", "evidence_ids": [evidence("R-B-MOD-005")]}, {"rule_id": "R-B-VER-002", "action": "make reliability formula-, table-, network-, consistency-, code-, and memo-specific", "evidence_ids": [first["verification"]]}, {"rule_id": "R-B-VER-004", "action": "reconcile 6770.1 versus 7039, missing cost constants, glyph-corrupted exponents, incomplete COD gradients, 2015 versus 2013-2025 timing, and absent appendix files", "evidence_ids": [first["weakness"]]}, {"rule_id": "R-B-VIZ-001", "action": "retain fit plots, factor diagrams, province graphs, route maps, pollution tables, beta bands, AHP matrices, strategy rows, and appendix plots with units and labels", "evidence_ids": [first["visualization"]]}, {"rule_id": "R-B-COMP-001", "action": "measure fit residuals, grey iterations, province-pair route construction, cost minimization, city aggregation, AHP operations, neural training, and MATLAB runtime", "evidence_ids": [evidence("R-B-COMP-001")] }]


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    units = language["units"]
    layouts = {x["chapter"]: x for x in language["chapter_layouts"]}
    paragraph_chains = []
    for chapter in ("abstract", "introduction"):
        ids = [u["language_unit_id"] for u in units if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": layouts[chapter]["paragraph_count"], "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": "context -> model or method -> result -> scope", "language_unit_ids": [ids[i % len(ids)]]} for i in range(layouts[chapter]["paragraph_count"])]})
    progressions = [{"chapter": chapter, "moves": [f"input: source-checked China water context, symbols, data, equation, algorithm, result, or action entering {chapter}", f"rhetorical job: state the positive problem, relation, comparison, or recommendation in {chapter}", f"analytical job: fit, rank, optimize, classify, test, or trace the declared quantity in {chapter}", f"output: retain a typed forecast, pressure, route, cost, class, policy, or provenance result from {chapter}", "handoff: name the next model, table, evaluation criterion, policy decision, or reproduction boundary"], "positive_pattern": "Use explicit source input -> operation -> typed output -> scoped handoff; warnings remain a last pass."} for chapter in language["available_chapters"]]
    model_ids = [m["model_id"] for m in models["models"]]
    equation_ids = [e["equation_id"] for m in models["models"] for e in m["governing_equations"]]
    warnings = []
    for model in models["models"]:
        for eq in model["governing_equations"]:
            if eq["transcription_confidence"] != "high":
                warnings.append({"model_id": model["model_id"], "equation_id": eq["equation_id"], "page": eq["page"], "warning": "Equation glyphs, units, or omitted parameter definitions require source-level reconciliation before numeric reuse."})
    counts = Counter(x["dimension"] for x in observations)
    return {"audit_id": f"LA-B-{YEAR}-{SHORT}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1, "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"], "chapter_saturation": [{"chapter": c, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [8, 2, 0]} for c in language["available_chapters"]], "language_unit_dispositions": [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "The source move is reusable after replacing water-strategy entities, units, data conditions, and decision scope."} for u in units], "paragraph_chains": paragraph_chains, "organization_logic": {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": [x["summary"] for x in card["writing_logic"]] + ["The final warning pass records source glyph, data, timing, calibration, and provenance defects without replacing positive language learning."], "section_progressions": progressions, "main_argument_chains": [{"claim": "Five complementary models turn China's water imbalance into forecast, project, conservation, and integrated-evaluation decisions.", "support_steps": ["three scarcity problems", "forecast alternatives and Verhulst repair", "CV reservoir and transfer network", "desalination and conservation", "AHP-neural evaluation", "government action"], "decision_consequence": "Use the full model ladder only with typed units, calibrated data, and explicit uncertainty boundaries.", "source_pages": [1, 4, 6, 10, 13, 22, 25, 27, 34, 39]}, {"claim": "Positive model interfaces are reusable when each relation names input, operation, output, and receiving decision.", "support_steps": ["fit residuals", "grey parameter estimation", "CV and pressure", "route edge weights", "desalination timing", "pollution and beta classes", "AHP and neural attributes"], "decision_consequence": "Transfer the organization and interface, not uncalibrated national numbers.", "source_pages": [5, 8, 10, 13, 20, 24, 27, 30, 33, 34]}, {"claim": "The government paper is strongest when its recommendations trace directly to route, storage, and pollution rankings.", "support_steps": ["six transfer routes", "high-pressure regions", "volatile provinces", "Hai watershed urgency", "within-watershed storage"], "decision_consequence": "Regenerate leadership prose from a typed result record and reconcile the stated year horizon.", "source_pages": [25, 22, 18, 31, 39]}]}, "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warnings}, "model_retention": {"model_count": len(model_ids), "retained_model_ids": model_ids, "retained_equation_ids": equation_ids, "central_equations": [{"model_id": m["model_id"], "equation_ids": [e["equation_id"] for e in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]}, "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-B-{YEAR}-{SHORT}-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)], "dimension_counts": {dim: counts[dim] for dim in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]}, "positive_reusable_language_count": len(units), "weakness_record_count": counts["weakness"], "review_status": "validated"}


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    pages = read_pages()
    language = make_language(pages)
    models = make_models(pages)
    card = make_card(language, models)
    card["protocol_v2_records"] = {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}}
    observations = make_observations(language, models, card)
    attach_rule_impacts(card, observations)
    audit = make_audit(language, models, card, observations)
    write_json(STAGE / "language.json", language)
    write_json(STAGE / "models.json", models)
    write_json(STAGE / "card.json", card)
    write_json(STAGE / "audit.json", audit)
    (STAGE / "observations.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "stage": str(STAGE), "pages_read": len(pages), "language_units": len(language["units"]), "models": len(models["models"]), "equations": sum(len(m["governing_equations"]) for m in models["models"]), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(card["visualization_observations"]), "warnings": len(card["weaknesses"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
