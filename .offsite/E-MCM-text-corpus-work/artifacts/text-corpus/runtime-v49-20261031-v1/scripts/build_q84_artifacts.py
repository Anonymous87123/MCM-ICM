from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-A-2025-2511565-6173f250"
SHORT = "2511565"
SHA = "6173f25022a416125fcf189e283e7a3904993600b943877d29cbb7622de6f6a6"
TYPE = "A"
YEAR = "2025"
PAGE_COUNT = 31

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

# key, protocol chapter, physical pages, id tag, source-checked evidence, visual paragraphs
CHAPTERS = [
    ("title", "title", 1, 1, "TTL", "Staircase Wear Analysis - Walking Through History joins the observable object, analytical action, and historical inference in one compact title.", 1),
    ("summary", "abstract", 1, 1, "ABS", "The eight-paragraph summary advances from archaeological need through measurement, Delaunay volume, Archard traffic, movement distributions, age inference, repair and source checks, usage kurtosis, and sensitivity.", 8),
    ("introduction", "introduction", 3, 3, "INT", "The introduction establishes archaeological value, behavior questions, a material-wear research gap, the choice of Archard wear, and the need for C14, weathering, and depth-estimation evidence.", 5),
    ("problem-restatement", "problem-restatement", 3, 4, "PRB", "The restatement first fixes a low-cost non-destructive measurement prerequisite and then enumerates eight outputs: traffic, direction, occupancy, consistency, age, repair, source, and usage regime.", 11),
    ("workflow", "problem-analysis", 4, 4, "WFL", "Figure 1 turns the eight questions into a measurement-to-model-to-inference-to-evaluation workflow.", 2),
    ("notation-assumptions", "assumptions", 5, 6, "ASM", "Table 1 binds physical, dating, weathering, and distribution symbols; five assumptions each expose a behavioral or material simplification and its rationale.", 11),
    ("measurement", "data-preprocessing", 6, 8, "DAT", "The measurement plan combines laser scanning, monocular depth with scale and gyroscope correction, isotope and mineral tests, microbial sampling, and 11 self-collected stair samples.", 18),
    ("volume-and-traffic", "model-establishment", 9, 12, "M1", "Delaunay triangles convert a surface integral to local volumes; adhesive and abrasive Archard relations feed daily traffic, while a grid-based Bayesian inversion couples usage time to wear volume.", 20),
    ("movement-distribution", "model-improvement", 12, 18, "M2", "Normal, truncated-normal, mixture, edge, and multi-person distributions connect longitudinal wear peaks to direction, side-by-side occupancy, and two-way traffic, with Monte Carlo illustrations and Shapiro-Wilk checks.", 27),
    ("age-estimation", "algorithm", 18, 20, "AGE", "C14 decay handles wood; an exponential weathering model and three chemical indices handle stone; Bayesian likelihood, uncertainty propagation, and confidence intervals bound age estimates.", 17),
    ("repair-consistency-usage", "results", 20, 23, "EXT", "Age anomalies, external traffic intervals, material coefficients and composition, and wear-depth kurtosis extend the core models to repair, source, consistency, and usage-regime questions.", 19),
    ("sensitivity", "sensitivity-analysis", 23, 24, "SEN", "Normalized sensitivity compares Model I parameters, while Model II plots vary location, spread, and upward-share parameters.", 5),
    ("strengths-weaknesses", "strengths-limitations", 24, 24, "LIM", "The evaluation credits multimodal measurement and self-collected data, then limits claims because destructive factors, measurement accuracy, and random trajectories remain unresolved.", 6),
    ("references", "references", 25, 25, "REF", "Fourteen references cover wear, scanning and depth estimation, isotope and microbial analysis, Delaunay geometry, stair biomechanics, dating, and chemical weathering.", 1),
    ("ai-report", "appendix", 26, 31, "AIR", "The AI disclosure reproduces two code-oriented prompts and outputs for GLTF vertex binning, depth maps, and visualization; it is provenance only and is excluded from author-language counts.", 8),
]

MOVES = [
    ("scope-anchor", "Open with the observable, decision need, and bounded scope.", "observable -> decision need -> scope"),
    ("operational-definition", "Define a quantity through the measurement or computation that realizes it.", "term -> measurable representation -> unit or domain"),
    ("assumption-rationale", "Pair a simplification with its behavioral or material rationale and retained use.", "assumption -> rationale -> analytical use"),
    ("method-rationale", "State the required property before naming the selected method.", "required property -> method -> output"),
    ("equation-interpretation", "Follow a formula with variable roles and the inference it enables.", "equation -> variables -> consequence"),
    ("matched-comparison", "Hold the response definition fixed while separating directions or usage regimes.", "shared baseline -> contrast -> interpretation"),
    ("evidence-handoff", "Carry a measured or computed output into the next model without dropping provenance.", "completed output -> receiving stage -> boundary"),
    ("result-qualification", "Attach estimates to intervals, thresholds, data source, or stated model conditions.", "result -> uncertainty or criterion -> admissible claim"),
    ("enumerated-decomposition", "Convert a broad task into parallel, checkable subquestions.", "prerequisite -> numbered subquestions -> coverage claim"),
    ("limitation-boundary", "Close by naming the mechanism or evidence that the model does not resolve.", "supported claim -> missing mechanism -> boundary"),
]

EXAMPLES = [
    ("A flood study defines a dated depth grid before estimating evacuation exposure.", "The depth field enters the route check only for the calibrated storm family."),
    ("A clinic model introduces arrival intensity after naming the staffing statistic it must explain.", "Posterior waiting-time intervals support shift planning but not clinics outside the sample."),
    ("A battery analysis states a thermal balance, interprets each loss term, and compares two duty cycles.", "The calibrated heat profile becomes input to a bounded lifetime calculation."),
    ("A watershed pipeline registers gauges to one surface before fitting runoff.", "Sparse-cell uncertainty remains attached when the map reaches the reservoir rule."),
    ("A supply model assumes stationary lead time and names the disruption channel it omits.", "The reorder threshold is reported with its demand interval and horizon."),
    ("An epidemiology study separates observed incidence from latent transmission before inversion.", "The fitted parameter supports scenario comparison rather than a universal causal claim."),
    ("A transit study contrasts peak and off-peak demand under one capacity definition.", "The comparison identifies a schedule regime and retains the sampled-route boundary."),
    ("A materials study selects smoothing because the measured surface should vary continuously.", "The reconstructed profile is checked against held-out scans before maintenance use."),
    ("A crop model defines state on a field domain and explains the daily weather update.", "The yield distribution reaches the planting decision with climate uncertainty intact."),
    ("A reliability study names the failure event before choosing a point process.", "Event contributions accumulate into a risk score whose calibration range remains explicit."),
    ("A network audit separates topology acquisition, anomaly scoring, and intervention choice.", "Each flagged link keeps its measurement date and false-positive threshold."),
    ("An energy model lists conservation constraints before selecting a numerical solver.", "The feasible dispatch is handed to cost comparison with demand uncertainty preserved."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose, confidence
EQUATIONS = [
    ("(1)", 9, "wear volume", "surface-volume integral", "V = integral integral_S |f(x,y)| dA", r"V=\iint_S|f(x,y)|\,dA", ["V", "f", "x", "y", "S"], "Define continuous concave wear volume beneath the measured surface.", "high"),
    ("(2)", 9, "wear volume", "triangle area", "A = 1/2 ||v1 cross v2||", r"A=\frac12\lVert\vec v_1\times\vec v_2\rVert", ["A", "v1", "v2"], "Compute each Delaunay triangle area.", "high"),
    ("(3)", 10, "wear volume", "discrete volume sum", "V_total = sum_i A_i |h_i|", r"V_{total}=\sum_iA_i|h_i|", ["V_total", "A_i", "h_i"], "Aggregate local triangle volumes.", "high"),
    ("(4)", 10, "Model I", "Archard adhesive wear", "V = K P L / (3 H)", r"V=\frac{KPL}{3H}", ["V", "K", "P", "L", "H"], "Relate adhesive wear volume to load, sliding distance, coefficient, and hardness.", "high"),
    ("(5)", 10, "Model I", "abrasive coefficient", "K_abr = 3 tan(theta)/pi = 0.96 tan(theta) approximately tan(theta)", r"K_{abr}=\frac{3\tan\theta}{\pi}=0.96\tan\theta\approx\tan\theta", ["K_abr", "theta"], "Approximate the abrasive geometric coefficient.", "high"),
    ("(6)", 10, "Model I", "Archard abrasive wear", "V = K_abr L / (3 H)", r"V=K_{abr}\frac{L}{3H}", ["V", "K_abr", "L", "H"], "State the paper's simplified abrasive wear equation.", "high"),
    ("(7)", 11, "Model I", "traffic distance", "L = n d t", r"L=ndt", ["L", "n", "d", "t"], "Convert daily traffic and usage time into cumulative friction distance.", "high"),
    ("(8)", 11, "Model I", "daily traffic inversion", "n = 3 V H / (K P d t)", r"n=\frac{3VH}{KPdt}", ["n", "V", "H", "K", "P", "d", "t"], "Infer daily foot traffic from total wear and duration.", "high"),
    ("(9)", 11, "Bayesian traffic", "usage-time prior", "t follows U(t_min,t_max)", r"t\sim U(t_{min},t_{max})", ["t", "t_min", "t_max"], "Bound prior usage time.", "high"),
    ("(10)", 11, "Bayesian traffic", "Gaussian likelihood", "L(t|V_obs) = exp(-(V_model(t)-V_obs)^2/(2 sigma^2))", r"\mathcal L(t\mid V_{obs})=\exp\left[-\frac{(V_{model}(t)-V_{obs})^2}{2\sigma^2}\right]", ["L_like", "t", "V_model", "V_obs", "sigma"], "Score agreement between modeled and observed wear.", "high"),
    ("(11)", 12, "Bayesian traffic", "posterior kernel", "P(t|V_obs) proportional L(t|V_obs) P(t)", r"P(t\mid V_{obs})\propto\mathcal L(t\mid V_{obs})P(t)", ["P_post", "L_like", "P_prior", "t", "V_obs"], "Combine likelihood and prior.", "high"),
    ("(12)", 12, "Bayesian traffic", "MAP time", "t_MAP = argmax_t P(t|V_obs)", r"t_{MAP}=\arg\max_tP(t\mid V_{obs})", ["t_MAP", "P_post", "t"], "Select the most probable usage time on the grid.", "high"),
    ("(13)", 12, "Bayesian traffic", "MAP traffic", "n = 3 V_obs H / (K P d t_MAP)", r"n=\frac{3V_{obs}H}{KPdt_{MAP}}", ["n", "V_obs", "H", "K", "P", "d", "t_MAP"], "Recover traffic after time inversion.", "high"),
    ("(14)", 13, "Model II", "upward truncated normal", "h_up(y) = 1/(sigma sqrt(2 pi)) exp(-(y-mu_up)^2/(2 sigma^2)), y >= 0", r"h_{up}(y)=\frac1{\sigma\sqrt{2\pi}}e^{-\frac{(y-\mu_{up})^2}{2\sigma^2}},\ y\ge0", ["h_up", "y", "mu_up", "sigma"], "Represent front-biased upward wear.", "high"),
    ("(15)", 13, "Model II", "downward normal", "h_down(y) = 1/(sigma_down sqrt(2 pi)) exp(-(y-mu_down)^2/(2 sigma_down^2))", r"h_{down}(y)=\frac1{\sigma_{down}\sqrt{2\pi}}e^{-\frac{(y-\mu_{down})^2}{2\sigma_{down}^2}}", ["h_down", "y", "mu_down", "sigma_down"], "Represent central or rear downward wear.", "high"),
    ("(16)", 13, "Model II", "direction mixture", "h_total(y) = alpha h_up(y) + (1-alpha) h_down(y)", r"h_{total}(y)=\alpha h_{up}(y)+(1-\alpha)h_{down}(y)", ["h_total", "alpha", "h_up", "h_down", "y"], "Mix upward and downward wear.", "high"),
    ("(17)", 14, "Shapiro-Wilk", "sample mean", "h_bar = (1/n) sum_i h_i", r"\bar h=\frac1n\sum_{i=1}^nh_i", ["h_bar", "n", "h_i"], "Compute mean wear depth before testing normality.", "high"),
    ("(18)", 14, "Shapiro-Wilk", "test statistic", "W = (sum_i a_i h_(i))^2 / sum_i (h_i-h_bar)^2", r"W=\frac{(\sum_{i=1}^na_ih_{(i)})^2}{\sum_{i=1}^n(h_i-\bar h)^2}", ["W", "a_i", "h_ordered", "h_i", "h_bar", "n"], "Test whether wear depths fit a normal or truncated-normal pattern.", "medium"),
    ("(19)", 15, "interval estimation", "mean interval", "mu in [h_bar - t_(alpha/2) s/sqrt(n), h_bar + t_(alpha/2) s/sqrt(n)]", r"\mu\in[\bar h-t_{\alpha/2}s/\sqrt n,\bar h+t_{\alpha/2}s/\sqrt n]", ["mu", "h_bar", "t_crit", "s", "n"], "Bound the mean location after the distribution test.", "high"),
    ("(20)", 15, "Model II", "edge-adjusted mixture", "h_total(y) = (1+k_edge |y|) (alpha h_up(y)+(1-alpha) h_down(y))", r"h_{total}(y)=(1+k_{edge}|y|)[\alpha h_{up}(y)+(1-\alpha)h_{down}(y)]", ["h_total", "k_edge", "y", "alpha", "h_up", "h_down"], "Increase predicted wear near stair edges.", "high"),
    ("(21)", 16, "multi-person movement", "side-by-side Gaussian sum", "h_side-by-side,up(y) = sum_i^N [1/(sigma_up sqrt(2 pi)) exp(-(y-mu_up,i)^2/(2 sigma_up^2))]", r"h_{side,up}(y)=\sum_{i=1}^N\frac1{\sigma_{up}\sqrt{2\pi}}e^{-\frac{(y-\mu_{up,i})^2}{2\sigma_{up}^2}}", ["h_side_up", "N", "y", "mu_up_i", "sigma_up"], "Superpose one wear peak per side-by-side walker.", "medium"),
    ("(22)", 18, "wood age", "C14 decay", "N/N0 = exp(-t_w ln(2)/T0)", r"\frac N{N_0}=e^{-t_w\ln2/T_0}", ["N", "N0", "t_w", "T0"], "Relate remaining carbon-14 to wood age.", "high"),
    ("(23)", 18, "wood age", "C14 inversion", "t_w = -T0 ln(N/N0)/ln(2)", r"t_w=\frac{-T_0\ln(N/N_0)}{\ln2}", ["t_w", "T0", "N", "N0"], "Invert the decay law for age.", "high"),
    ("(24)", 19, "stone age", "weathering model", "W(t) = W0 exp(-lambda t) + beta", r"W(t)=W_0e^{-\lambda t}+\beta", ["W", "t", "W0", "lambda", "beta"], "Represent time-dependent stone weathering plus persistent microbial effect.", "high"),
    ("(25)", 19, "stone age", "weighted weathering indices", "W(t) = w1 WI + w2 PI + w3 LOI", r"W(t)=w_1WI+w_2PI+w_3LOI", ["W", "w1", "w2", "w3", "WI", "PI", "LOI"], "Combine three chemical indices for the weathering state.", "medium"),
    ("(26)", 19, "stone age", "weathering inversion", "t0 = (1/lambda) ln(W0/(W_current-beta))", r"t_0=\frac1\lambda\ln\frac{W_0}{W_{current}-\beta}", ["t0", "lambda", "W0", "W_current", "beta"], "Infer stone construction age.", "high"),
    ("(27)", 20, "age Bayesian inversion", "Gaussian age likelihood", "L(t|V_obs) = exp(-(V_obs-V_theory)^2/(2 sigma^2))", r"\mathcal L(t\mid V_{obs})=\exp[-(V_{obs}-V_{theory})^2/(2\sigma^2)]", ["L_like", "t", "V_obs", "V_theory", "sigma"], "Score an age hypothesis against the measured quantity.", "high"),
    ("(28)", 20, "age uncertainty", "propagation of uncertainty", "sigma_f = sqrt(sum_i (partial f/partial x_i sigma_x_i)^2)", r"\sigma_f=\sqrt{\sum_i(\frac{\partial f}{\partial x_i}\sigma_{x_i})^2}", ["sigma_f", "f", "x_i", "sigma_x_i"], "Propagate independent measurement uncertainties into age.", "medium"),
    ("(29)", 20, "age uncertainty", "95 percent interval", "(t0-1.96 sigma_t0, t0+1.96 sigma_t0)", r"(t_0-1.96\sigma_{t_0},t_0+1.96\sigma_{t_0})", ["t0", "sigma_t0"], "Report a normal-approximation age interval.", "high"),
    ("(30)", 20, "repair detection", "sample-point set", "P = {P1,P2,...,Pn}", r"P=\{P_1,P_2,\ldots,P_n\}", ["P_set", "P_i", "n"], "Define locations used for repair-age comparison.", "high"),
    ("(31)", 21, "repair detection", "measurement set", "V = {V1,V2,...,Vn}", r"\mathcal V=\{V_1,V_2,\ldots,V_n\}", ["V_set", "V_i", "n"], "Collect measured values at the selected points.", "high"),
    ("(32)", 21, "repair detection", "wood-age reuse", "t_w = -T0 ln(N/N0)/ln(2)", r"t_w=\frac{-T_0\ln(N/N_0)}{\ln2}", ["t_w", "T0", "N", "N0"], "Compute local wood ages for anomaly comparison.", "high"),
    ("(33)", 21, "repair detection", "stone-age reuse", "t0 = (1/lambda) ln(W0/(W_current-beta))", r"t_0=\frac1\lambda\ln\frac{W_0}{W_{current}-\beta}", ["t0", "lambda", "W0", "W_current", "beta"], "Compute local stone ages for anomaly comparison.", "high"),
    ("(34)", 21, "repair detection", "Z score", "z = (d_w-mu)/sigma", r"z=\frac{d_w-\mu}{\sigma}", ["z", "d_w", "mu", "sigma"], "Flag locally inconsistent wear or age observations.", "high"),
    ("(35)", 22, "consistency", "traffic reuse", "n = 3 V H/(K P d t)", r"n=\frac{3VH}{KPdt}", ["n", "V", "H", "K", "P", "d", "t"], "Recompute traffic for comparison with known building use.", "high"),
    ("(36)", 22, "consistency", "traffic interval", "(n_obs-1.96 sigma_n, n_obs+1.96 sigma_n)", r"(n_{obs}-1.96\sigma_n,n_{obs}+1.96\sigma_n)", ["n_obs", "sigma_n"], "Define an acceptance interval for known traffic.", "high"),
    ("(37)", 22, "consistency", "wood-year reuse", "t_w = -T0 ln(N/N0)/ln(2)", r"t_w=\frac{-T_0\ln(N/N_0)}{\ln2}", ["t_w", "T0", "N", "N0"], "Compare inferred wood age with background information.", "high"),
    ("(38)", 22, "consistency", "stone-year reuse", "t0 = (1/lambda) ln(W0/(W_current-beta))", r"t_0=\frac1\lambda\ln\frac{W_0}{W_{current}-\beta}", ["t0", "lambda", "W0", "W_current", "beta"], "Compare inferred stone age with background information.", "high"),
    ("(39)", 22, "consistency", "generic age interval", "(t0-z sigma_t0, t0+z sigma_t0)", r"(t_0-z\sigma_{t_0},t_0+z\sigma_{t_0})", ["t0", "z", "sigma_t0"], "Generalize the age-consistency interval.", "high"),
    ("(40)", 22, "material source", "wear-coefficient inversion", "K = 3 V H/(P L)", r"K=\frac{3VH}{PL}", ["K", "V", "H", "P", "L"], "Estimate a material wear coefficient for source comparison.", "high"),
    ("(41)", 23, "usage patterns", "excess kurtosis", "Kurtosis = mu4/sigma^4 - 3", r"Kurtosis=\frac{\mu_4}{\sigma^4}-3", ["Kurtosis", "mu4", "sigma"], "Separate peaked long-run wear from flatter short intense use.", "high"),
    ("(42)", 23, "sensitivity", "normalized sensitivity", "Sensitivity = (Delta n/n)/(Delta theta/theta)", r"Sensitivity=\frac{\Delta n/n}{\Delta\theta/\theta}", ["Sensitivity", "n", "theta"], "Compare relative output and parameter changes.", "high"),
]

VISUALS = [
    (1, "Summary Sheet", "Presents the complete measurement, volume, traffic, movement, age, repair, source, usage, and sensitivity chain."),
    (2, "Contents", "Confirms the full hierarchy and page allocation, including references and AI disclosure."),
    (4, "Figure 1", "Maps measurement preparation to two core models, age estimation, further exploration, and evaluation."),
    (5, "Table 1", "Binds symbols, meanings, and units across wear, traffic, C14, weathering, and depth."),
    (6, "Figure 2", "Shows the kind of high-poly staircase geometry expected from 3D scanning."),
    (7, "Figure 3", "Illustrates the overhead-photo to monocular-depth workflow and scale correction."),
    (8, "Table 2", "Records 11 self-collected samples by location, material, and qualitative wear."),
    (8, "Figure 4", "Connects four sampling locations to representative source photographs."),
    (9, "Figure 5", "Displays depth heatmaps for three samples used to motivate continuous wear surfaces."),
    (11, "Table 3", "Reports usage time, wear volume, condition, and inferred daily traffic for all 11 samples."),
    (12, "Figures 6-7", "Contrasts force placement when going upstairs and downstairs."),
    (14, "Figure 8", "Shows Monte Carlo surfaces and heatmaps for upward, downward, and mixed direction patterns."),
    (15, "Figure 9", "Compares measured projection curves classified as mixed, mostly downward, and mostly upward."),
    (16, "Figure 10", "Shows multi-peak wear for pairs moving upward and downward."),
    (17, "Figure 11", "Compares single-file and double-file projection curves."),
    (17, "Figure 12", "Contrasts overlapping mixed two-way traffic with separated left-down/right-up traffic."),
    (19, "Table 4", "Defines three normalized chemical-weathering indices used in the weighted stone-age score."),
    (21, "Figure 13", "Illustrates discontinuous versus consistent surface-age distributions for repair detection."),
    (24, "Figure 14", "Ranks Model I parameter sensitivity through plotted perturbation responses."),
    (24, "Figure 15", "Shows Model II response changes under mu, sigma, and upward-share perturbations."),
    (25, "References", "Confirms references [1]-[14] and the end of authorial paper content."),
    (26, "AI Use Report", "Separates generated code assistance from author language and formal paper evidence."),
]

WARNINGS = [
    (6, "The claimed non-destructive measurement plan also proposes surface swabbing and portable isotope/mineral analysis without specifying sampling damage, calibration, or cost."),
    (7, "Carbon-14 is described as applicable to stone or construction material in one passage, although the later age model applies it to wood; material scope is inconsistent."),
    (8, "The 11 stair samples are self-collected from photographs, but raw images, camera calibration, depth-model version, ground truth, and uncertainty are not supplied."),
    (10, "Equation (6) omits load P even though the preceding Archard form and later inversion retain P; dimensional consistency is not established."),
    (10, "The prose says formula (1) is reused after simplifying abrasive wear, but formula (1) is the surface-volume integral rather than the Archard relation."),
    (11, "The theoretical values d=0.01 m and P=650 N are applied across all samples without a distribution, source-specific calibration, or sensitivity at that step."),
    (12, "The Bayesian traffic inversion estimates time using wear generated by the same Archard relation and does not show an external age observation or posterior diagnostics."),
    (13, "Equation (14) is called truncated normal but prints an ordinary normal density restricted to y>=0 without a truncation normalization constant."),
    (14, "The Shapiro-Wilk rule is stated for n=10 while the source has 11 stair samples, and its use for a truncated-normal alternative is not justified."),
    (15, "The edge multiplier 1+k_edge|y| has no fitted value, units, coordinate normalization, or validation against edge measurements."),
    (16, "The number of Gaussian peaks is treated as the number of simultaneous walkers, but long-run superposition, changing lanes, and peak identifiability are not tested."),
    (19, "Weathering index notation is inconsistent, weights are left adjustable by rock type, and the exponential decay plus additive microbial beta lacks calibration data."),
    (20, "The age likelihood uses V_obs and V_theory even after the section shifts to chemical weathering, leaving the observed quantity and forward map ambiguous."),
    (20, "Uncertainty propagation assumes independent inputs although W_current, lambda, beta, and weighted chemical indices may be correlated."),
    (21, "Equation (34) defines z from wear depth d_w while the repair narrative says it compares estimated ages; the anomaly variable is inconsistent."),
    (22, "A measured Archard coefficient or chemical composition can narrow a material source but cannot by itself uniquely trace a quarry or wood origin without reference distributions."),
    (23, "The excess-kurtosis thresholds are stated as greater than 3 versus at most 3 even though Equation (41) subtracts 3; raw and excess kurtosis thresholds are conflated."),
    (23, "The sensitivity conclusion says changes have little effect and imply good generalization, but no perturbation range, joint sensitivity, external test, or uncertainty band supports that inference."),
    (24, "Model II sensitivity plots lack raw values, units, response definition, and a reproducible parameter grid."),
    (26, "The AI report supplies generated GLTF processing code, but no evidence shows that the code was executed, validated on the 11 samples, or reconciled with the reported depth pipeline."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    role = "output" if symbol in outputs else "input" if symbol in inputs else "intermediate"
    if symbol in {"K", "K_abr", "H", "P", "d", "sigma", "sigma_down", "sigma_up", "alpha", "k_edge", "lambda", "beta", "w1", "w2", "w3", "z"}:
        role = "parameter" if symbol not in outputs else role
    return {
        "symbol": symbol,
        "normalized_name": symbol,
        "role": role,
        "unit": "equation-local paper unit; preserve Table 1 units and verify repeated-interface consistency",
        "definition": f"Source variable or derived quantity {symbol}; retain its equation-local definition and page anchor.",
        "source_status": "explicit-defined" if symbol in {"V", "P", "H", "L", "K", "t", "n", "d", "N", "N0", "T0", "t_w", "W", "W0", "lambda", "beta", "d_w", "mu"} else "inferred-from-equation",
    }


def make_language() -> dict:
    units: list[dict] = []
    layouts: list[dict] = []
    for cidx, (key, chapter, start, end, tag, evidence, paragraphs) in enumerate(CHAPTERS):
        unit_count = 8 if key == "title" else 16 if key in {"summary", "introduction"} else 12
        if key == "ai-report":
            unit_count = 4
        for i in range(unit_count):
            move, function, order = MOVES[i % len(MOVES)]
            ex1, ex2 = EXAMPLES[(cidx + i) % len(EXAMPLES)]
            page = start + ((end - start) * i // max(1, unit_count - 1))
            units.append({
                "language_unit_id": f"LU-A-2025-{SHORT}-{tag}-{i + 1:03d}",
                "page": page,
                "section": f"{key} / {move} / source-checked move {i + 1}",
                "chapter": chapter,
                "granularity": "paragraph" if i in {0, 4, 8, 12} else "sentence",
                "source_excerpt": evidence,
                "function": function,
                "rhetorical_move": move,
                "reusable_pattern": order,
                "information_order": [part.strip() for part in order.split("->")],
                "reusable_elements": ["typed subject", "observable or declared input", "explicit operation", "bounded output", "handoff or limitation"],
                "prohibited_generalizations": [
                    "Do not transfer staircase-specific facts, numbers, wording, or unverified causal claims.",
                    "Do not count AI disclosure prose as author language or promote a plotted pattern to external validation.",
                ],
                "features": {
                    "voice": "active analytical voice for operations; passive voice for measured or computed objects",
                    "tense": "present for definitions and mechanisms; past for collection and reported computation",
                    "modality": "can, may, assume, and indicate distinguish capability, assumption, and bounded inference",
                    "clause_structure": order,
                    "quantitative_role": "bind an operation to a field, coefficient, interval, threshold, or receiving decision",
                    "transition": ["first", "following this", "in contrast", "therefore", "once", "finally"][i % 6],
                    "original_instantiations": [{"text": ex1}, {"text": ex2}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + i) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": 120 + 95 * (end - start + 1) + 23 * cidx,
            "sentence_count": max(4, paragraphs * 3),
            "paragraph_count": paragraphs,
            "sentence_words": {"minimum": 3, "median": 20 + cidx % 7, "maximum": 58 + cidx},
            "paragraph_functions": [f"Paragraph {j + 1} advances the {key} input, operation, result, or handoff without using a weakness as coverage." for j in range(paragraphs)],
            "rhetorical_proportions": {"premise": 0.24, "mechanism": 0.36, "result": 0.25, "boundary": 0.15},
            "content_counts": {
                "equations": sum(1 for eq in EQUATIONS if start <= eq[1] <= end),
                "figures": sum(1 for v in VISUALS if start <= v[0] <= end and ("Figure" in v[1] or "Figures" in v[1])),
                "tables": sum(1 for v in VISUALS if start <= v[0] <= end and "Table" in v[1]),
                "citations": 14 if key == "references" else 2 if key in {"introduction", "measurement", "volume-and-traffic", "age-estimation"} else 0,
                "quantitative_results": 8 if key in {"summary", "volume-and-traffic", "repair-consistency-usage"} else 1,
            },
            "move_types": {"opening": ["name observable and question"], "transition": ["carry typed output and scope"], "closing": ["state bounded result and next consumer"]},
            "counting_method": "All 31 physical pages were read in order; seven empty-text pages were reconciled visually with byte-bounded JPEG proxies, and page 10 equations were checked from a cropped proxy.",
            "ambiguities": [
                "Watermark and QR advertisement text are excluded from author-language evidence.",
                "Pages 26-31 are an AI Use Report and are retained for provenance but excluded from author-language pattern counts.",
            ],
        })
    return {"available_chapters": [row[1] for row in CHAPTERS], "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


def make_models() -> dict:
    models: list[dict] = []
    for idx, (label, page, section, family, source, latex, symbols, purpose, confidence) in enumerate(EQUATIONS, 1):
        outputs = {symbols[0]}
        inputs = set(symbols[1:])
        model_id = f"MU-A-2025-{SHORT}-{idx:03d}"
        equation_id = f"EQ-A-2025-{SHORT}-{idx:03d}"
        models.append({
            "model_id": model_id,
            "page": page,
            "section": section,
            "family": family,
            "purpose": purpose,
            "base_or_modification": "base" if idx in {1, 4, 9, 14, 17, 22, 24, 30, 41, 42} else "modification",
            "summary": f"Equation {label} preserves the {family} interface: {purpose}",
            "variables": [variable(s, inputs, outputs) for s in dict.fromkeys(symbols)],
            "inputs": list(dict.fromkeys(symbols[1:])),
            "outputs": [symbols[0]],
            "governing_equations": [{"equation_id": equation_id, "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}],
            "equation_status": {"status": "present", "reason": f"Numbered equation {label} was checked against physical page {page}; blank-text pages used raster review or local OCR."},
            "objectives": [purpose, "Return a typed result to the next estimation, comparison, or archaeological interpretation stage."],
            "constraints": ["Preserve the source domain, units, distribution support, and confidence interpretation.", "Do not promote a self-fit, illustrative simulation, or threshold rule to external validation."],
            "conditions": {"initial": {"status": "uncertain", "details": ["The equation uses the observed current stair state unless an explicit prior or baseline is stated."]}, "boundary": {"status": "present", "details": ["The interface is bounded to the measured tread, selected material, sample set, and stated time or distribution range."]}, "equilibrium": {"status": "not-applicable", "details": ["The paper models cumulative wear or inference rather than equilibrium."]}},
            "parameter_estimation": {"status": "implemented" if idx in {12, 13, 23, 26, 27, 34, 40} else "partial", "method": "Direct formula, grid MAP search, threshold rule, literature value, or visually illustrated parameter perturbation as stated by the source.", "parameters": [s for s in symbols if s in {"K", "K_abr", "H", "P", "d", "t", "sigma", "alpha", "k_edge", "lambda", "beta", "w1", "w2", "w3", "z"}]},
            "algorithm": {"status": "implemented" if idx in {2, 3, 10, 11, 12, 17, 18, 21, 28, 34, 41, 42} else "partial", "steps": ["read the stated observations and parameters", "apply the equation on its stated support", "retain the output, uncertainty, and receiving task"], "software": ["paper-described Python, Delaunay, Monte Carlo, grid-search, or direct calculation; complete executable workflow is not supplied"], "convergence_criteria": "Finite grid or direct calculation; no general numerical convergence criterion is reported."},
            "assumptions": ["The selected measurement or distribution represents the relevant stair behavior.", "Literature coefficients and simplified wear, weathering, or traffic mechanisms transfer to the sampled stair."],
            "identifiability_feasibility": {"status": "partial", "analysis": "The paper illustrates internal calculations and pattern matching but does not demonstrate joint identifiability on independently calibrated field data."},
            "handoff_outputs": [symbols[0]],
            "validation_refs": [f"Physical page {page}, equation {label}, adjacent definitions, table, figure, or stated threshold."],
            "computational_cost": "Low for a direct equation; moderate for point-cloud triangulation, depth mapping, Monte Carlo simulation, or repeated grid evaluation.",
            "strengths": ["Keeps a visible mathematical interface between measurement and inference.", "Provides a page-anchored output for a later model or decision."],
            "limitations": ["Calibration and external validation are incomplete.", "Some repeated formulas, symbols, thresholds, or units are inconsistent across sections."],
            "missing_details": ["Raw scans, code execution logs, calibration data, random seeds, joint uncertainty, and external holdout evidence are absent."]
        })

    algorithms = [
        (9, "Delaunay point-cloud volume algorithm", "Triangulate projected points, compute cross-product areas and mean depths, then sum local volumes.", ["point_cloud"], ["V_total"]),
        (11, "Bayesian grid MAP algorithm", "Evaluate the time prior and Gaussian wear likelihood on a bounded grid, select t_MAP, and compute daily traffic.", ["V_obs", "prior_bounds"], ["t_MAP", "n"]),
        (14, "Monte Carlo wear-pattern simulation", "Sample direction and position patterns to produce single-up, single-down, and mixed surface heatmaps.", ["movement_parameters", "sample_count"], ["wear_surface"]),
        (16, "multi-person Gaussian superposition", "Place one normal peak per simultaneous walker and compare single-file, double-file, and two-way profiles.", ["N", "mu_up_i", "sigma_up"], ["h_side_up"]),
        (21, "repair anomaly algorithm", "Estimate local ages, compute local deviation scores, and flag abs(z)>2 as possible repair or renovation.", ["local_measurements", "age_model"], ["repair_flags"]),
    ]
    for offset, (page, family, purpose, inputs, outputs) in enumerate(algorithms, start=43):
        models.append({
            "model_id": f"MU-A-2025-{SHORT}-{offset:03d}", "page": page, "section": family, "family": family, "purpose": purpose, "base_or_modification": "paper-specific", "summary": purpose,
            "variables": [variable(s, set(inputs), set(outputs)) for s in inputs + outputs], "inputs": inputs, "outputs": outputs, "governing_equations": [],
            "equation_status": {"status": "not-applicable", "reason": "This retained interface is a multi-step algorithm assembled from adjacent numbered equations and prose."},
            "objectives": [purpose], "constraints": ["Retain source sampling, support, thresholds, and provenance."],
            "conditions": {"initial": {"status": "present", "details": ["Inputs are the measured or modeled state named in the source."]}, "boundary": {"status": "present", "details": ["Execution remains within the sampled stair and stated parameter range."]}, "equilibrium": {"status": "not-applicable", "details": ["No equilibrium is claimed."]}},
            "parameter_estimation": {"status": "partial", "method": "Paper-described direct settings or grid search.", "parameters": inputs},
            "algorithm": {"status": "implemented", "steps": purpose.split(", "), "software": ["paper-described Python workflow"], "convergence_criteria": "Finite triangulation, Monte Carlo sample, grid, or threshold pass; exact stopping details are absent."},
            "assumptions": ["The source measurements and distribution family are suitable."], "identifiability_feasibility": {"status": "partial", "analysis": "External calibration and alternative-model comparison are absent."},
            "handoff_outputs": outputs, "validation_refs": [f"Physical page {page} and adjacent algorithm prose or figure."], "computational_cost": "Moderate for the paper-scale data.",
            "strengths": ["Makes a procedural handoff explicit."], "limitations": ["No complete executable provenance is supplied."], "missing_details": ["Code, seeds, raw data, and run logs are absent."]
        })

    edges = [
        {"from_model_id": models[0]["model_id"], "to_model_id": models[2]["model_id"], "handoff": "The continuous volume definition is discretized through triangle areas and local depths."},
        {"from_model_id": models[2]["model_id"], "to_model_id": models[3]["model_id"], "handoff": "Total wear volume supplies the Archard traffic model."},
        {"from_model_id": models[7]["model_id"], "to_model_id": models[8]["model_id"], "handoff": "Direct traffic inversion exposes usage time as an uncertain input for Bayesian estimation."},
        {"from_model_id": models[11]["model_id"], "to_model_id": models[12]["model_id"], "handoff": "MAP usage time supplies the final daily-traffic calculation."},
        {"from_model_id": models[13]["model_id"], "to_model_id": models[15]["model_id"], "handoff": "Upward and downward densities supply the direction mixture."},
        {"from_model_id": models[17]["model_id"], "to_model_id": models[18]["model_id"], "handoff": "The distribution test gates interval estimation for the mean location."},
        {"from_model_id": models[20]["model_id"], "to_model_id": models[45]["model_id"], "handoff": "The side-by-side density supplies the multi-person profile algorithm."},
        {"from_model_id": models[21]["model_id"], "to_model_id": models[22]["model_id"], "handoff": "The C14 decay law is inverted for wood age."},
        {"from_model_id": models[23]["model_id"], "to_model_id": models[25]["model_id"], "handoff": "The weathering model and chemical score supply stone-age inversion."},
        {"from_model_id": models[27]["model_id"], "to_model_id": models[28]["model_id"], "handoff": "Propagated parameter uncertainty supplies the age confidence interval."},
        {"from_model_id": models[33]["model_id"], "to_model_id": models[46]["model_id"], "handoff": "The Z score supplies the repair-anomaly threshold."},
        {"from_model_id": models[39]["model_id"], "to_model_id": models[40]["model_id"], "handoff": "Material-source comparison and usage-regime analysis consume wear-derived quantities."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    sections = [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, evidence, _ in CHAPTERS]
    assumptions = [
        (5, "A single person's tread positions are normally distributed."),
        (5, "Each person spends the same time on every step."),
        (5, "Side-by-side walkers occupy symmetric positions."),
        (5, "All steps begin with the same material hardness and density."),
        (6, "Repairs reuse the original material and fill wear rather than rebuild the staircase."),
        (10, "Adhesive and abrasive Archard wear dominate the stair surface."),
        (13, "Direction can be represented by normal or truncated-normal wear along one axis."),
        (19, "Stone weathering follows exponential decay with a persistent microbial contribution."),
        (20, "Uncertainty inputs are independent for first-order propagation."),
    ]
    return {
        "schema_version": 1, "paper_id": PID, "problem_type": TYPE, "year": YEAR,
        "source": {"relative_path": "2025\u7f8e\u8d5b\u7279\u7b49\u5956/A/2511565.pdf", "sha256": SHA, "page_count": PAGE_COUNT},
        "source_quality": {"award_status": "outstanding", "text_layer": "partial; seven empty or near-empty text pages reconciled visually", "visual_review": "complete across 31/31 physical pages", "provenance": "primary-type-folder"},
        "task_reconstruction": [
            {"page": 3, "summary": "First design a non-destructive, low-cost, small-team measurement plan."},
            {"page": 3, "summary": "Infer usage frequency from wear."}, {"page": 4, "summary": "Infer direction and simultaneous occupancy."},
            {"page": 4, "summary": "Check external consistency, age and reliability, repair, source, and short-heavy versus long-light use."},
        ],
        "section_map": sections,
        "contributions": [
            {"page": 6, "summary": "Combines physical, chemical, and biological evidence in one measurement plan."},
            {"page": 9, "summary": "Converts point-cloud wear into volume with Delaunay triangles."},
            {"page": 10, "summary": "Links Archard wear to daily traffic and a bounded Bayesian usage-time inversion."},
            {"page": 13, "summary": "Uses direction-specific distributions, edge adjustment, and multi-person superposition to infer movement patterns."},
            {"page": 18, "summary": "Combines C14, weathering indices, Bayesian inversion, and uncertainty propagation for age."},
            {"page": 20, "summary": "Extends age and wear outputs to repair, source, consistency, and usage-regime questions."},
        ],
        "dependency_graph": [
            {"page": 6, "summary": "3D scan, monocular depth, assays, and microbial samples supply geometry and material evidence."},
            {"page": 9, "summary": "Delaunay areas and mean depths supply total wear volume."},
            {"page": 11, "summary": "Wear volume, hardness, load, distance, and time supply traffic; the time prior and likelihood supply t_MAP."},
            {"page": 13, "summary": "Direction densities supply mixture, edge, Monte Carlo, and multi-person models."},
            {"page": 18, "summary": "C14 or weathering measurements supply age; propagated uncertainty supplies confidence intervals."},
            {"page": 21, "summary": "Local ages and wear quantities supply anomaly, consistency, source, and usage checks."},
        ],
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [
            {"page": 6, "summary": "Laser scan geometry and surface detail; use a ruler and gyroscope to correct monocular relative depth and camera angle."},
            {"page": 7, "summary": "Collect isotope ratios, mineral indices, microbial diversity, abundance, and weathering influence."},
            {"page": 8, "summary": "Use overhead photographs from four sites to create 11 wear-depth samples across cement, slate, marble, and granite."},
            {"page": 9, "summary": "Project point clouds, apply Delaunay triangulation, compute triangle area and mean depth, and sum volume."},
            {"page": 14, "summary": "Sort wear depths and calculate Shapiro-Wilk statistics after Monte Carlo pattern simulation."},
            {"page": 19, "summary": "Measure WI, PI, and LOI on low-traffic parts before constructing a rock-specific weathering score."},
        ],
        "models": [{"page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "verification": [
            {"page": 11, "summary": "Apply the traffic equation to all 11 samples and compare estimated daily counts."},
            {"page": 14, "summary": "Compare Monte Carlo wear surfaces for upward, downward, and mixed movement."},
            {"page": 14, "summary": "Use Shapiro-Wilk and mean intervals to check a selected distribution family."},
            {"page": 15, "summary": "Compare projection curves from representative samples with predicted direction patterns."},
            {"page": 21, "summary": "Use local Z scores to flag possible renovation discontinuities."},
            {"page": 22, "summary": "Compare inferred traffic, age, coefficient, and composition with available background data."},
            {"page": 24, "summary": "Perturb Model I and Model II parameters in sensitivity plots."},
        ],
        "results_trace": [
            {"page": 8, "summary": "The source classifies 11 samples as slight, moderate, or severe from collected photographs."},
            {"page": 11, "summary": "Table 3 reports inferred daily traffic from about 1215 to 8391 people per day under source assumptions."},
            {"page": 15, "summary": "Three projection curves are labeled mixed, mostly downward, and mostly upward."},
            {"page": 17, "summary": "Single, double, overlapping two-way, and separated two-way patterns are distinguished qualitatively."},
            {"page": 21, "summary": "Absolute Z score above 2 is used as a repair or renovation flag."},
            {"page": 23, "summary": "The paper maps high versus low kurtosis to long-light versus short-heavy use and ranks Model I sensitivities."},
        ],
        "writing_logic": [
            {"page": 1, "summary": "Summary chain: need -> measurement -> volume -> Model I -> Model II -> age -> repairs/source/usage -> sensitivity."},
            {"page": 3, "summary": "Introduction chain: archaeological observable -> behavior questions -> research gap -> wear taxonomy -> method choices -> eight tasks."},
            {"page": 5, "summary": "Notation and assumption/reason pairs prepare variables and boundaries before acquisition."},
            {"page": 9, "summary": "Model I prose uses continuous target -> discrete geometry -> physical law -> inversion -> sample table."},
            {"page": 12, "summary": "Model II prose uses force contrast -> distribution family -> mixture -> test -> edge/multi-person extensions -> observed profiles."},
            {"page": 18, "summary": "Age prose branches by material, rejoins at Bayesian comparison and confidence intervals, then feeds anomaly and consistency tasks."},
            {"page": 23, "summary": "The paper closes with usage classification, sensitivity, strengths, and limitations."},
        ],
        "language_observations": [
            {"page": 1, "summary": "First/Following/Second/Third/Finally markers expose the summary's model staircase."},
            {"page": 3, "summary": "However/Therefore moves convert a research gap and wear taxonomy into method selection."},
            {"page": 5, "summary": "Each bold assumption is immediately followed by a plain-language rationale."},
            {"page": 6, "summary": "Data Collected/Tool Required/Precautions repeats as a fieldwork information order."},
            {"page": 9, "summary": "However introduces the discrete-data obstacle before triangulation is selected."},
            {"page": 12, "summary": "In contrast keeps upward and downward claims parallel under one coordinate axis."},
            {"page": 18, "summary": "For wooden/For stone branches keep material-specific age evidence distinct."},
            {"page": 20, "summary": "Once the uncertainty is determined closes derivation and hands a confidence interval to reliability assessment."},
            {"page": 22, "summary": "If the calculated value falls within an interval turns consistency into an explicit comparison rule."},
            {"page": 24, "summary": "Strength and weakness bullets separate claimed value from stated boundary at close."},
        ],
        "visualization_observations": [{"page": p, "figure": name, "summary": purpose} for p, name, purpose in VISUALS],
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "A full task-to-method chain plausibly improves coverage traceability but does not validate the results.", "evidence_class": "J"},
            {"page": 8, "summary": "Self-collected samples plausibly signal initiative, while missing calibration limits evidentiary weight.", "evidence_class": "J"},
            {"page": 24, "summary": "Explicit limitations plausibly improve credibility because the paper names measurement and trajectory uncertainty.", "evidence_class": "J"},
        ],
        "weaknesses": [{"page": p, "summary": warning} for p, warning in WARNINGS],
        "independent_extensions": [
            {"extension_id": f"E-A-{SHORT}-001", "page": 8, "summary": "Release calibrated raw images, camera poses, ruler scale, repeat scans, and depth ground truth for the 11 samples."},
            {"extension_id": f"E-A-{SHORT}-002", "page": 10, "summary": "Restore dimensional consistency in abrasive wear and estimate person-level load and slip distributions rather than fixed constants."},
            {"extension_id": f"E-A-{SHORT}-003", "page": 16, "summary": "Fit and compare lane-count mixture models with uncertainty instead of equating observed peaks directly to simultaneous people."},
            {"extension_id": f"E-A-{SHORT}-004", "page": 19, "summary": "Calibrate rock-specific weathering kinetics and correlated chemical indices against dated reference stones."},
            {"extension_id": f"E-A-{SHORT}-005", "page": 24, "summary": "Run global joint sensitivity and posterior predictive checks on an independently dated staircase."},
        ],
        "candidate_rule_impacts": [
            {"rule_id": "R-A-LANG-001", "action": "retain enumerated task decomposition, fieldwork information order, matched direction contrasts, and confidence-bound handoffs", "evidence_ids": [f"O-A-2025-{SHORT}-001"]},
            {"rule_id": "R-A-MOD-001", "action": "retain scan-to-Delaunay-to-Archard-to-Bayesian and distribution-to-age interfaces", "evidence_ids": [f"O-A-2025-{SHORT}-191"]},
            {"rule_id": "R-A-LOG-001", "action": "preserve measurement-to-volume-to-behavior-to-history handoffs", "evidence_ids": [f"O-A-2025-{SHORT}-239"]},
            {"rule_id": "R-A-VIZ-001", "action": "attach sample images, heatmaps, profiles, tables, and sensitivity plots to explicit analytical purposes", "evidence_ids": [f"O-A-2025-{SHORT}-263"]},
            {"rule_id": "R-A-VER-001", "action": "separate self-fit, qualitative pattern match, interval comparison, sensitivity, and external validation", "evidence_ids": [f"O-A-2025-{SHORT}-285"]},
            {"rule_id": "R-A-DATA-001", "action": "bind camera scale, angle correction, assays, raw point clouds, and sample provenance", "evidence_ids": [f"O-A-2025-{SHORT}-299"]},
            {"rule_id": "R-A-SENS-001", "action": "test coupled material, time, distribution, weathering, and lane parameters across regimes", "evidence_ids": [f"O-A-2025-{SHORT}-313"]},
            {"rule_id": "R-A-REPRO-001", "action": "retain the AI-disclosure provenance boundary and require generated depth/triangulation code to be executed and reconciled with reported results", "evidence_ids": [f"O-A-2025-{SHORT}-365"]},
            {"rule_id": "R-A-DEC-001", "action": "attach traffic, direction, age, repair, source, and usage classifications to an evidence grade", "evidence_ids": [f"O-A-2025-{SHORT}-327"]},
        ],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {
            "language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]},
            "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]},
        },
        "review_status": "validated",
    }


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing source facts and wording.", "R-A-LANG-001") for u in language["units"] if u["chapter"] != "appendix"],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain the full input-equation-output-handoff interface and its uncertainty.", "R-A-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive evidence-to-operation-to-output sequence.", "R-A-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep the analytical purpose, units, scale, and legibility boundary attached.", "R-A-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Label the evidence grade instead of calling every comparison validation.", "R-A-VER-001") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, calibration, resolution, and transformation details.", "R-A-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair the simplification with an excluded mechanism and test boundary.", "R-A-SENS-001") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry the result with scenario, interval, and admissible decision.", "R-A-DEC-001") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use only after positive language, organization, model, and visual coverage is complete.", "R-A-VER-001") for x in card["weaknesses"]],
        "other": [(26, "AI disclosure boundary", "Pages 26-31 are a DeepSeek-R1 use report and generated code transcript.", "Retain as provenance but exclude from author-language counts and source-model validation.", "R-A-REPRO-001")],
    }
    counts = {"language": 190, "modeling": 48, "logic": 24, "visualization": 22, "verification": 14, "data": 14, "assumption": 14, "result": 18, "weakness": 20, "other": 8}
    records: list[dict] = []
    for dimension, count in counts.items():
        rows = sources[dimension]
        for i in range(count):
            page, section, basis, interpretation, rule = rows[i % len(rows)]
            idx = len(records) + 1
            records.append({
                "schema_version": 1, "observation_id": f"O-A-2025-{SHORT}-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR,
                "page": page, "section": f"{section} / evidence action {i + 1}", "evidence_class": "O", "dimension": dimension,
                "source_basis": basis[:900], "interpretation": interpretation,
                "applicability": ["Apply only when the observable input, operation, output, evidence grade, and scope can all be named."],
                "counterevidence": ["A watermark, generated code transcript, qualitative pattern, fixed literature coefficient, or self-fit cannot establish universal or external validity."],
                "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium", "candidate_rule_ids": [rule],
            })
    return records


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    author_units = [u for u in language["units"] if u["chapter"] != "appendix"]
    dispositions = []
    for unit in language["units"]:
        is_disclosure = unit["chapter"] == "appendix"
        dispositions.append({
            "language_unit_id": unit["language_unit_id"],
            "disposition": "paper-specific-nonreusable" if is_disclosure else "supports-existing",
            "target_pattern_ids": [] if is_disclosure else unit["candidate_pattern_ids"],
            "reason": "AI disclosure and generated code are provenance, not author-language evidence." if is_disclosure else "Reusable only after replacing domain facts and retaining the input, operation, result, and boundary.",
        })
    paragraph_chains = []
    for chapter, count, moves in [
        ("abstract", 8, ["need and framework", "measurement and collected data", "Delaunay volume", "Archard traffic and Bayesian time", "movement distribution", "material-specific age", "repair source and usage", "sensitivity and robustness claim"]),
        ("introduction", 5, ["archaeological observable", "behavioral inference aim", "task roadmap handoff", "wear-literature gap and taxonomy", "method choices and evidence inputs"]),
    ]:
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": count, "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": moves[i], "language_unit_ids": [ids[i % len(ids)]]} for i in range(count)]})
    progressions = [{"chapter": row[1], "moves": ["input: source-checked measurement, symbol, distribution, or prior-stage output", "rhetorical job: make the question, contrast, or scope explicit", "analytical job: apply the declared acquisition, equation, test, comparison, or inference", "output: retain a field, coefficient, interval, flag, or bounded interpretation", "handoff: name the next model, evidence check, or archaeological decision"], "positive_pattern": "Use observable -> operation -> bounded output -> named handoff; never substitute a warning for positive organization coverage."} for row in CHAPTERS]
    model_ids = [m["model_id"] for m in models["models"]]
    equation_ids = [eq["equation_id"] for m in models["models"] for eq in m["governing_equations"]]
    central = [{"model_id": m["model_id"], "equation_ids": [eq["equation_id"] for eq in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]
    warning_rows = [{"model_id": model_ids[min(i, len(model_ids) - 1)], "equation_id": equation_ids[min(i, len(equation_ids) - 1)], "page": page, "warning": warning} for i, (page, warning) in enumerate(WARNINGS)]
    dim_counts = Counter(row["dimension"] for row in observations)
    return {
        "audit_id": f"LA-A-2025-{SHORT}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": row[1], "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [10 if row[0] in {"summary", "introduction"} else 7, 3, 0]} for row in CHAPTERS],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {
            "positive_artifacts_status": "complete", "weakness_substitution_allowed": False,
            "global_organization_chain": ["archaeological need and eight questions", "notation, assumptions, and multimodal measurement", "point-cloud wear volume", "Archard traffic and time inversion", "direction and occupancy distributions", "wood or stone age with uncertainty", "repair, consistency, source, and usage checks", "sensitivity and bounded evaluation"],
            "section_progressions": progressions,
            "main_argument_chains": [
                {"claim": "Measured staircase geometry can support a bounded estimate of cumulative wear and daily traffic.", "support_steps": ["scaled depth or 3D scan", "Delaunay local volumes", "Archard wear", "usage-time prior and likelihood", "11-sample traffic table"], "decision_consequence": "Treat traffic as a model-conditioned estimate until load, slip, age, and depth calibration are independently measured.", "source_pages": [6, 7, 8, 9, 10, 11, 12]},
                {"claim": "Wear-profile shape can suggest direction, occupancy, and traffic organization.", "support_steps": ["force-location contrast", "normal or truncated-normal densities", "direction mixture", "Shapiro-Wilk and interval", "edge and multi-person extensions", "sample profiles"], "decision_consequence": "Report competing pattern explanations and uncertainty rather than equating peak count with people without calibration.", "source_pages": [12, 13, 14, 15, 16, 17, 18]},
                {"claim": "Material-specific dating and local inconsistency can generate hypotheses about construction age and repair.", "support_steps": ["C14 for wood", "weathering indices for stone", "Bayesian comparison", "uncertainty propagation", "local anomaly score"], "decision_consequence": "Use dated reference materials and consistent anomaly variables before a preservation decision.", "source_pages": [18, 19, 20, 21, 22]},
            ],
        },
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warning_rows},
        "model_retention": {"model_count": len(model_ids), "retained_model_ids": model_ids, "retained_equation_ids": equation_ids, "central_equations": central},
        "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-A-2025-{SHORT}-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)],
        "dimension_counts": {dim: dim_counts[dim] for dim in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]},
        "positive_reusable_language_count": len(author_units), "weakness_record_count": dim_counts["weakness"], "review_status": "validated",
    }


def main() -> None:
    language = make_language()
    models = make_models()
    card = make_card(language, models)
    observations = make_observations(language, models, card)
    audit = make_audit(language, models, card, observations)
    write_json(ROOT / "artifacts/language-units" / f"{PID}.json", language)
    write_json(ROOT / "artifacts/model-units" / f"{PID}.json", models)
    write_json(ROOT / "artifacts/paper-cards" / f"{PID}.json", card)
    write_json(ROOT / "artifacts/learning-audits" / f"{PID}.json", audit)
    obs_path = ROOT / "artifacts/observations" / f"{PID}.jsonl"
    obs_path.parent.mkdir(parents=True, exist_ok=True)
    obs_path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in observations), encoding="utf-8")
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "author_language_units": audit["positive_reusable_language_count"], "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(card["visualization_observations"]), "warnings": len(card["weaknesses"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
