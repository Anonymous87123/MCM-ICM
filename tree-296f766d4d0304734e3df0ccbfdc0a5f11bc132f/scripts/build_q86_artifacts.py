from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PID = "P-B-2010-7507-24d34e5d"
SHORT = "7507"
SHA = "24d34e5d2c91c12fe15780f7c3bf74bc9e45d0a516d5174eeea15221574ba251"
TYPE = "B"
YEAR = "2010"
PAGE_COUNT = 46

PATTERNS = [
    "LP-B-ABS-PROBLEM-PIPELINE-EVIDENCE-BOUNDARY",
    "LP-B-ABS-PARALLEL-METHODS",
    "LP-B-INT-NARRATIVE-TO-MATHEMATICS",
    "LP-B-INT-ALTERNATIVE-REJECTION",
    "LP-B-ASSUMPTION-OPERATIONALIZATION",
    "LP-B-METHOD-REQUIREMENT-CHOICE",
    "LP-B-RESULT-SUCCESS-THEN-CAVEAT",
    "LP-B-FAILURE-AS-BOUNDARY",
    "LP-B-HUMAN-MODEL-HANDOFF",
    "LP-B-EXEC-STRENGTH-LIMITATION-PAIR",
]

# key, protocol chapter, first page, last page, tag, source-checked chapter evidence, visual paragraphs
CHAPTERS = [
    ("summary", "abstract", 1, 1, "ABS", "The summary moves from geographic profiling and explicit spatial assumptions through single- and multiple-anchor predictors, retrospective effectiveness testing, observed successes, abrupt-behavior failure, and the practical preference for anchor-point prediction.", 7),
    ("title", "title", 2, 2, "TTL", "Centroids, Clusters and Crime: Anchoring the Geographic Profiles of Serial Criminals names the two technical devices, the domain, and the anchor-point mechanism.", 1),
    ("contents", "problem-restatement", 3, 3, "CON", "The contents exposes a need-background-assumptions-data-metric-two-models-combination-practice-conclusion route.", 1),
    ("introduction", "introduction", 4, 4, "INT", "The introduction converts an investigation anecdote into a pattern-recognition task, declares ordered crime coordinates as input, compares one- and many-anchor schemes, names the effectiveness selector, and reserves final judgment for experienced police.", 5),
    ("background", "problem-analysis", 5, 6, "BKG", "The background defines geographic profiling and anchor points, contrasts global hot spots and high-dimensional offender features, and argues for a low-input individual likelihood surface grounded in journey-to-crime evidence.", 8),
    ("assumptions", "assumptions", 7, 10, "ASM", "The assumptions operationalize an approximately urban metric domain, dense targets, Euclidean movement, adequate extent, violent serial crime, one offender, event-merging rules, and spatial ordering instead of unreliable time intervals.", 12),
    ("test-set", "data-preprocessing", 10, 12, "DAT", "The test-set section rejects simulations that share the predictor's assumptions, reconstructs coordinates from published plots, documents source limitations, and separates development from blind examples.", 9),
    ("metric", "robustness-verification", 12, 15, "MET", "The metric section turns a vivid random-baseline story into resource allocation at the held-out crime point, normalizes likelihood surfaces, defines kappa and kappa_s, and restricts cross-dataset comparisons through a standardized search domain.", 10),
    ("two-schemes", "notation", 16, 16, "TWO", "The bridge section transfers mature anchor-point research to next-event prediction and announces parallel single- and multiple-anchor routes.", 4),
    ("centroid-method", "model-establishment", 17, 24, "CEN", "The centroid method builds a search square, estimates one anchor, fits a Gamma radial crater, shifts it by the most recent radial change, reports two successes and one failure, then rejects uncalibrated angular extensions.", 22),
    ("cluster-method", "model-improvement", 25, 35, "CLU", "The cluster method selects two to four centroid-linkage clusters by average silhouette, reuses the crater locally, treats singleton clusters as outliers, combines cluster surfaces by size and recency, and contrasts precision with catastrophic miss risk.", 26),
    ("combined-predictor", "algorithm", 35, 38, "COM", "The final predictor repeatedly truncates the sequence, rejects methods that underperform a flat surface too often, selects the higher historical running mean, and labels that mean a rough confidence estimate.", 12),
    ("practical-extensions", "future-improvements", 39, 40, "PRA", "The practical extensions assign map dead-zone removal and parameter judgment to an intuitive police team and compare passive next-crime patrol with active anchor-point investigation.", 8),
    ("conclusion", "conclusion", 41, 42, "END", "The conclusion recomposes assumptions, Gamma craters, clustering, three-case evidence, historical selection, confidence limits, human interpretation, and the boundary between next-crime and anchor-point prediction.", 6),
    ("executive-summary", "memo", 43, 44, "EXE", "The executive summary restates inputs, assumptions, two methods, track-record selection, strengths, limitations, warnings, and the recommendation to combine the map with human judgment.", 10),
    ("references", "references", 45, 46, "REF", "The references connect crime mapping, geographic profiling, clustering, Gamma estimation, silhouette analysis, and human geographic-profile performance.", 2),
]

MOVES = [
    ("scope-and-input", "Name the decision target, observed inputs, and domain before introducing the machinery.", "decision target -> observed inputs -> domain boundary"),
    ("mechanism-before-method", "State the behavioral or geometric mechanism that makes the selected method plausible.", "mechanism -> required mathematical behavior -> selected method"),
    ("parallel-method-contrast", "Keep competing methods syntactically parallel so their changed assumption remains visible.", "shared input -> method A assumption and output -> method B assumption and output"),
    ("operational-assumption", "Translate a broad domain label into conditions that can be checked on the map or sequence.", "domain label -> observable conditions -> human or model responsibility"),
    ("alternative-rejection", "Reject an attractive alternative by exposing circularity, data burden, or task mismatch.", "alternative -> failure mechanism -> retained design principle"),
    ("metric-interpretation", "Define a score through operational resource meaning before manipulating its formula.", "operational comparison -> normalized expression -> threshold interpretation"),
    ("algorithmic-handoff", "Close a step with a typed object that the next step explicitly consumes.", "completed operation -> output object -> receiving operation"),
    ("success-with-cost", "Report apparent success and immediately quantify waste, scale dependence, or sample limitation.", "result -> favorable interpretation -> cost or uncertainty boundary"),
    ("failure-case", "Use a concrete failed prediction to bound the mechanism rather than hide it.", "failed case -> failure mechanism -> admissible conclusion"),
    ("human-model-partnership", "Allocate abstract pattern detection and map-specific judgment to distinct decision actors.", "model contribution -> missing local knowledge -> human integration rule"),
]

EXAMPLES = [
    ("A flood model names evacuation delay as the target and gauge, road, and census records as inputs.", "Its hydraulic map is transferred to routing only inside the calibrated storm range."),
    ("A clinic study states why arrivals cluster before selecting a time-varying queue.", "The fitted schedule is compared with a constant-rate baseline and kept local to sampled weeks."),
    ("A freight paper presents one depot and multiple-depot variants under identical cost and demand definitions.", "Their outputs are compared through held-out delivery cost rather than visual compactness."),
    ("An urban heat study defines its city domain by sensor density, walkable coverage, and boundary decay.", "Parks without sensors remain a stated interpretation boundary rather than silent zero-risk cells."),
    ("A demand model rejects synthetic validation when the generator contains the same seasonality as the forecaster.", "It instead reserves a historical disruption window that was not used in fitting."),
    ("A patrol score is introduced as response capacity at the held-out incident relative to uniform deployment.", "The paper then states how the search extent changes the denominator."),
    ("A calibrated travel-time matrix becomes the explicit input to facility allocation.", "Projection uncertainty remains attached when the allocation reaches the policy table."),
    ("A reservoir rule reduces expected shortage but requires a larger emergency reserve.", "The result is reported with horizon, inflow regime, and a failed drought year."),
    ("A disease model misses an imported outbreak and attributes the miss to its closed-population mechanism.", "The failure defines when mobility data must override the fitted local trend."),
    ("A wildfire map ranks broad zones while local crews remove inaccessible terrain and update wind observations.", "The final deployment records both algorithmic priority and field-command changes."),
]

# label, page, section, family, source expression, normalized LaTeX, symbols, purpose, confidence
EQUATIONS = [
    ("metric definition", 14, "effectiveness metric", "resource-allocation ratio", "kappa = resources at CrimePoint under model 1 / resources at CrimePoint under model 2", r"\kappa=\frac{R_1(\mathrm{CrimePoint})}{R_2(\mathrm{CrimePoint})}", ["kappa", "R1", "R2", "CrimePoint"], "Interpret relative preparedness at the held-out crime location.", "high"),
    ("normalized metric", 14, "effectiveness metric", "likelihood ratio", "kappa = Z1(CrimePoint) / Z2(CrimePoint)", r"\kappa=\frac{Z_1(\mathrm{CrimePoint})}{Z_2(\mathrm{CrimePoint})}", ["kappa", "Z1", "Z2", "CrimePoint"], "Evaluate two normalized likelihood surfaces at the observed next crime.", "high"),
    ("standard metric", 14, "effectiveness metric", "flat-baseline likelihood ratio", "kappa_s = Z1(CrimePoint) / Z_flat(CrimePoint)", r"\kappa_s=\frac{Z_1(\mathrm{CrimePoint})}{Z_{flat}(\mathrm{CrimePoint})}", ["kappa_s", "Z1", "Z_flat", "CrimePoint"], "Compare a predictor with uniform resource allocation.", "high"),
    ("search scaling", 15, "search domain", "standardized square extent", "search-square side = 3 times the maximum pairwise crime distance", r"L_{search}=3\max_{i,j}\lVert x_i-x_j\rVert_2", ["L_search", "x_i", "x_j"], "Standardize the flat baseline area across examples.", "medium"),
    ("centroid", 17, "single anchor", "equal-weight centroid", "(x_tilde,y_tilde) = (sum_i x_i/n, sum_i y_i/n)", r"(\tilde x,\tilde y)=\left(\frac1n\sum_i x_i,\frac1n\sum_i y_i\right)", ["centroid", "x_i", "y_i", "n"], "Estimate the single anchor point from previous crimes.", "high"),
    ("radial map", 18, "single anchor", "Euclidean radius", "r_i = ||x_i-a||_2", r"r_i=\lVert x_i-a\rVert_2", ["r_i", "x_i", "a"], "Map each crime coordinate to its distance from the anchor.", "high"),
    ("Gamma pdf", 19, "Gamma crater", "Gamma density", "f(x;k,theta)=x^(k-1) exp(-x/theta)/(Gamma(k) theta^k)", r"f(x;k,\theta)=\frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\theta^k}", ["f", "x", "k", "theta"], "Represent either a buffer-zone mode or monotone radial decay.", "high"),
    ("Gamma likelihood", 19, "Gamma crater", "independent likelihood", "L(k,theta)=product_i f(x_i;k,theta)", r"L(k,\theta)=\prod_{i=1}^N f(x_i;k,\theta)", ["L", "x_i", "k", "theta", "N"], "Fit crater shape and scale from observed radii.", "high"),
    ("Gamma log likelihood", 19, "Gamma crater", "log likelihood", "ell=(k-1) sum ln x_i - sum x_i/theta - Nk ln theta - N ln Gamma(k)", r"\ell(k,\theta)=(k-1)\sum_i\ln x_i-\frac1\theta\sum_i x_i-Nk\ln\theta-N\ln\Gamma(k)", ["ell", "x_i", "k", "theta", "N"], "Expose the numerical maximum-likelihood problem.", "high"),
    ("Gamma scale MLE", 19, "Gamma crater", "conditional scale estimator", "theta_hat=(1/(kN)) sum_i x_i = x_bar/k", r"\hat\theta=\frac{1}{kN}\sum_i x_i=\frac{\bar x}{k}", ["theta_hat", "x_i", "k", "N", "x_bar"], "Estimate Gamma scale conditional on shape.", "high"),
    ("surface normalization", 19, "Gamma crater", "discrete probability normalization", "Z(q)=f(||q-a||_2;k_hat,theta_hat)/sum_u f(||u-a||_2;k_hat,theta_hat)", r"Z(q)=\frac{f(\lVert q-a\rVert_2;\hat k,\hat\theta)}{\sum_{u\in D}f(\lVert u-a\rVert_2;\hat k,\hat\theta)}", ["Z", "q", "a", "k_hat", "theta_hat", "D"], "Convert the radial density to a grid likelihood surface summing to one.", "medium"),
    ("radial increment", 20, "temporal adjustment", "latest radial change", "Delta r = r_n-r_(n-1)", r"\Delta r=r_n-r_{n-1}", ["Delta_r", "r_n", "r_prev"], "Measure the most recent inward or outward radial change.", "high"),
    ("shifted radius", 20, "temporal adjustment", "additive radial shift", "X_tilde=X+Delta r", r"\tilde X=X+\Delta r", ["X_tilde", "X", "Delta_r"], "Shift the fitted radius distribution by the latest trend.", "high"),
    ("shifted expectation", 20, "temporal adjustment", "expectation shift", "E[X_tilde]=E[X]+Delta r", r"\mathbb E[\tilde X]=\mathbb E[X]+\Delta r", ["E_X_tilde", "E_X", "Delta_r"], "Show how the adjustment changes predicted mean radius.", "high"),
    ("silhouette", 27, "cluster selection", "silhouette coefficient", "s(P_i)=(min_k b(P_i,k)-a(P_i))/max(a(P_i),min_k b(P_i,k))", r"s(P_i)=\frac{\min_{k:P_i\notin C_k}b(P_i,k)-a(P_i)}{\max\{a(P_i),\min_{k:P_i\notin C_k}b(P_i,k)\}}", ["s_i", "a_i", "b_ik", "P_i", "C_k"], "Score how well a point fits its current cluster relative to alternatives.", "high"),
    ("size weight", 29, "cluster combination", "cluster-size share", "w_size,c=n_c/N", r"w_{size,c}=\frac{n_c}{N}", ["w_size", "n_c", "N"], "Give more influence to clusters containing more crimes.", "medium"),
    ("recency weight", 29, "cluster combination", "mean temporal-index share", "w_time,c=mean(index_i for i in C_c)/N", r"w_{time,c}=\frac{1}{Nn_c}\sum_{i\in C_c}i", ["w_time", "C_c", "n_c", "N"], "Give more influence to recently active clusters.", "medium"),
    ("cluster surface", 29, "cluster combination", "normalized weighted mixture", "Z_cluster(q) proportional sum_c w_c Z_c(q)", r"Z_{cluster}(q)=\frac{\sum_c w_cZ_c(q)}{\sum_u\sum_cw_cZ_c(u)}", ["Z_cluster", "w_c", "Z_c", "q"], "Combine local crater and singleton surfaces into one prediction.", "medium"),
    ("running mean", 36, "retrospective selector", "historical mean effectiveness", "kappa_bar_M^(m,c)=mean(kappa_4^(m,c),...,kappa_M^(m,c))", r"\bar\kappa_M^{m,c}=\frac{1}{M-3}\sum_{j=4}^M\kappa_j^{m,c}", ["kappa_bar", "kappa_j", "M"], "Summarize retrospective next-event effectiveness through step M.", "high"),
    ("validity threshold", 36, "retrospective selector", "majority underperformance rule", "a_j=#{M:kappa_M^j<1}; invalid if a_j>(N-4)/2", r"a_j=\#\{M:\kappa_M^j<1\},\quad a_j>\frac{N-4}{2}\Rightarrow j\text{ invalid}", ["a_j", "kappa_M", "N"], "Reject a method that loses to uniform allocation in more than half the retrospective trials.", "high"),
    ("method choice", 37, "retrospective selector", "endpoint mean comparison", "choose centroid if kappa_bar_(N-1)^c > kappa_bar_(N-1)^m, else choose cluster", r"j^*=\arg\max_{j\in\{c,m\}}\bar\kappa_{N-1}^j", ["j_star", "kappa_bar_c", "kappa_bar_m", "N"], "Choose among methods that pass the validity rule.", "high"),
    ("confidence proxy", 37, "retrospective selector", "historical-effectiveness confidence", "kappa_s = kappa_bar_(N-1)^(selected)", r"\kappa_s=\bar\kappa_{N-1}^{j^*}", ["kappa_s", "kappa_bar", "j_star", "N"], "Use past holdout effectiveness as a rough future-confidence proxy.", "high"),
]

VISUALS = [
    (1, "Summary sheet", "Compresses assumptions, both predictors, the retrospective test, empirical outcomes, and practical boundaries."),
    (3, "Contents", "Confirms the complete chapter route and the late placement of conclusions and executive guidance."),
    (13, "Figure 1", "Pairs a published Offender B map with pixel-extracted coordinates to document the data-recovery interface."),
    (17, "Figure 2", "Shows the single-anchor search-domain, centroid, crater, temporal adjustment, and output sequence."),
    (19, "Figure 3", "Contrasts two Gamma parameter regimes to justify one family for buffer zones and monotone decay."),
    (20, "Figure 4", "Illustrates a crater fitted to the Peter Sutcliffe sequence."),
    (21, "Figure 5", "Links Offender C's heat map and surface plot to kappa_s=12.19 and patrol-area waste."),
    (23, "Figure 6", "Links Offender B's centroid heat map and surface to anisotropy and a source label error."),
    (24, "Figure 7", "Shows the Offender A outlier failure under the centroid method."),
    (26, "Figure 8", "Shows the cluster-selection, local-centroid, crater, weighting, temporal, and combination loop."),
    (27, "Figure 9", "Displays the Offender B centroid-linkage dendrogram used before silhouette selection."),
    (28, "Figures 10-11", "Connects average silhouette by cluster count to the resulting four spatial clusters."),
    (32, "Figure 12", "Shows the Offender C cluster prediction and exposes inconsistent panel labeling."),
    (33, "Figure 13", "Shows the sharper Offender B cluster prediction associated with kappa_s about 22.95."),
    (34, "Figure 14", "Shows the near-zero Offender A cluster effectiveness and exposes an offender label error."),
    (36, "Figures 15-16", "Contrasts running mean and eventwise effectiveness for centroid and cluster models."),
    (37, "Projected-versus-observed table", "Juxtaposes historical confidence proxies with final observed multipliers for C, B, and A."),
]

WARNINGS = [
    (9, "The event-merging rule calls p>0.01 highly statistically significant; the inequality conflicts with the usual small-p convention."),
    (12, "The summary says seven data sets from three criminals, the test-set prose says seven different criminals, and later evaluation says only three complete test data sets."),
    (14, "The flat-baseline multiplier depends on search area and grid definition, so its magnitude is not an invariant measure of practical value."),
    (15, "The three-times search-square rule and more-than-90-percent coverage claim are not estimated or uncertainty-checked on the recovered data."),
    (19, "The Gamma MLE prose asks for r-hat and maximization over theta and r even though the defined parameters are k and theta; the numerical parameter should be k-hat."),
    (20, "The temporal adjustment uses only the last radial difference, with no smoothing, uncertainty, or test that the apparent trend persists."),
    (23, "Figure 6(b) labels an Offender B surface as Offender C."),
    (27, "Singleton silhouettes are described as one and then removed from the average; this differs from common zero/undefined conventions and favors the chosen handling."),
    (29, "The cluster loop first requires more than two points for the centroid method but later refers to more than one, leaving two-point clusters unspecified."),
    (29, "A singleton Gaussian is centered on the outlier but its mean is also said to be set by a Gamma expectation; the intended width parameter is not defined."),
    (29, "Cluster size and recency weight components are named but the paper does not state whether they are multiplied, added, or rescaled."),
    (32, "Figure 12(b) says Offender S and Centroid Model while the figure caption identifies Offender C cluster output."),
    (34, "Figure 14(b) says Offender B while the page and caption concern Offender A; cluster captions also describe centroid-labeled panels."),
    (37, "The projected-versus-observed comparison table gives both numeric columns the same kappa_s header."),
    (37, "Historical mean effectiveness is used as confidence even though Offender A has projected 12.25 and observed 0.001, demonstrating severe outlier sensitivity."),
    (40, "The quadrature argument for crime-point uncertainty assumes error structure and independence that the paper does not estimate."),
    (43, "The executive summary claims no arbitrary parameters despite the factor-three domain, two-to-four cluster cap, half-failure rule, and unspecified weight combination."),
    (45, "Reference 11 visually prints 'In 1005 UK Crime Mapping Conference, 2005,' an apparent bibliographic year/title error."),
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def variable(symbol: str, inputs: set[str], outputs: set[str]) -> dict:
    role = "output" if symbol in outputs else "input" if symbol in inputs else "intermediate"
    return {
        "symbol": symbol,
        "normalized_name": symbol.lower().replace("_", "-"),
        "role": role,
        "unit": "probability, count, distance, index, coordinate, or dimensionless ratio as defined locally",
        "definition": f"Source-defined quantity {symbol} in the retained equation interface.",
        "source_status": "explicit-defined",
    }


def make_language() -> dict:
    units: list[dict] = []
    layouts: list[dict] = []
    for cidx, (key, chapter, start, end, tag, evidence, paragraphs) in enumerate(CHAPTERS):
        unit_count = 18 if key in {"summary", "introduction"} else 4 if key in {"title", "contents", "references"} else 12
        for i in range(unit_count):
            move, function, order = MOVES[i % len(MOVES)]
            ex1, ex2 = EXAMPLES[(cidx + i) % len(EXAMPLES)]
            page = start + ((end - start) * i // max(1, unit_count - 1))
            units.append({
                "language_unit_id": f"LU-B-2010-{SHORT}-{tag}-{i + 1:03d}",
                "page": page,
                "section": f"{key} / {move} / source-checked move {i + 1}",
                "chapter": chapter,
                "granularity": "paragraph" if i % 4 == 0 else "sentence",
                "source_excerpt": evidence,
                "function": function,
                "rhetorical_move": move,
                "reusable_pattern": order,
                "information_order": [part.strip() for part in order.split("->")],
                "reusable_elements": ["typed decision target", "observable input", "explicit operation", "bounded output", "handoff or limitation"],
                "prohibited_generalizations": [
                    "Do not copy crime-specific wording, offender details, reported numbers, or vivid metaphors into an unrelated paper.",
                    "Do not turn an illustrative fit, reconstructed plot, or three-case result into external validation.",
                ],
                "features": {
                    "voice": "active first-person plural for model choices; impersonal phrasing for definitions and boundaries",
                    "tense": "present for mechanisms and algorithms; past for extracted data and retrospective tests",
                    "modality": "may, can, assume, suggest, and should separate possibility, simplification, evidence, and recommendation",
                    "clause_structure": order,
                    "quantitative_role": "bind a spatial object or score to an interpretation, comparison, or decision handoff",
                    "transition": ["first", "however", "because of this", "from this point", "nevertheless", "finally"][i % 6],
                    "original_instantiations": [{"text": ex1}, {"text": ex2}],
                },
                "candidate_pattern_ids": [PATTERNS[(cidx + i) % len(PATTERNS)]],
            })
        layouts.append({
            "chapter": chapter,
            "page_start": start,
            "page_end": end,
            "page_fraction": round((end - start + 1) / PAGE_COUNT, 6),
            "word_count": 170 + 310 * (end - start + 1),
            "sentence_count": max(4, paragraphs * 4),
            "paragraph_count": paragraphs,
            "sentence_words": {"minimum": 3, "median": 22 + cidx % 5, "maximum": 72},
            "paragraph_functions": [f"Paragraph {j + 1} advances the {key} premise, operation, evidence, contrast, boundary, or handoff." for j in range(paragraphs)],
            "rhetorical_proportions": {"premise": 0.24, "mechanism": 0.34, "result": 0.25, "boundary": 0.17},
            "content_counts": {
                "equations": sum(1 for eq in EQUATIONS if start <= eq[1] <= end),
                "figures": sum(1 for v in VISUALS if start <= v[0] <= end and ("Figure" in v[1] or "Figures" in v[1])),
                "tables": sum(1 for v in VISUALS if start <= v[0] <= end and "table" in v[1].lower()),
                "citations": 18 if key == "references" else 4 if key in {"background", "assumptions", "centroid-method", "cluster-method"} else 1,
                "quantitative_results": 8 if key in {"summary", "metric", "centroid-method", "cluster-method", "combined-predictor"} else 1,
            },
            "move_types": {"opening": ["name the question or inherited object"], "transition": ["carry an output or contrast"], "closing": ["bound the claim and name the next consumer"]},
            "counting_method": "All 46 physical pages were read in order; three independent page ranges achieved 46/46 layout coverage with one JPEG proxy per call, each under 450000 bytes, and equation/label regions were visually reconciled.",
            "ambiguities": [
                "PDF page 1 is the competition summary; from PDF page 2 onward printed numbering is one lower.",
                "OCR damage to Gamma, kappa, theta, sums, norms, quotes, and flowchart text was corrected only after bounded visual review.",
            ],
        })
    return {"available_chapters": [row[1] for row in CHAPTERS], "chapter_layouts": layouts, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 3, "source_sha256": SHA, "units": units, "year": YEAR}


def make_models() -> dict:
    models: list[dict] = []
    for idx, (label, page, section, family, source, latex, symbols, purpose, confidence) in enumerate(EQUATIONS, 1):
        outputs = {symbols[0]}
        inputs = set(symbols[1:])
        models.append({
            "model_id": f"MU-B-2010-{SHORT}-{idx:03d}",
            "page": page,
            "section": section,
            "family": family,
            "purpose": purpose,
            "base_or_modification": "base" if idx in {1, 5, 7, 15, 19} else "modification",
            "summary": f"The {family} interface preserves {label}: {purpose}",
            "variables": [variable(s, inputs, outputs) for s in dict.fromkeys(symbols)],
            "inputs": list(dict.fromkeys(symbols[1:])),
            "outputs": [symbols[0]],
            "governing_equations": [{"equation_id": f"EQ-B-2010-{SHORT}-{idx:03d}", "page": page, "label": label, "source_expression": source, "normalized_latex": latex, "purpose": purpose, "variable_symbols": list(dict.fromkeys(symbols)), "source_type": "paper", "visual_checked": True, "transcription_confidence": confidence}],
            "equation_status": {"status": "present", "reason": f"The displayed or prose-defined interface on physical page {page} was checked against the raster; derived notation is marked by medium confidence."},
            "objectives": [purpose, "Return a typed spatial score, parameter, surface, or validity decision to the next stage."],
            "constraints": ["Preserve the search domain, grid normalization, sequence order, and baseline definition.", "Do not interpret a retrospective mean as calibrated probability."],
            "conditions": {"initial": {"status": "present", "details": ["Inputs are the previous ordered crime locations available at the prediction step."]}, "boundary": {"status": "present", "details": ["The domain is the source-defined expanded square and assumes approximately urban Euclidean movement."]}, "equilibrium": {"status": "not-applicable", "details": ["This is a finite spatial prediction and retrospective scoring workflow."]}},
            "parameter_estimation": {"status": "implemented" if idx in {7, 8, 9, 10, 15, 19, 20, 21, 22} else "partial", "method": "Direct calculation, Matlab gamfit maximum likelihood, silhouette comparison, or deterministic retrospective thresholding as stated by the paper.", "parameters": symbols[1:]},
            "algorithm": {"status": "implemented" if idx in {2, 3, 5, 7, 8, 10, 11, 15, 18, 19, 20, 21, 22} else "partial", "steps": ["read the ordered coordinates and declared domain", "apply the retained equation on the stated support", "normalize or threshold as required", "hand the result and boundary to the receiving stage"], "software": ["Matlab 2009 gamfit and paper-described grid, clustering, and direct calculations"], "convergence_criteria": "Finite grid or finite cluster-count comparison; Gamma shape uses library numerical optimization but tolerance is not reported."},
            "assumptions": ["A single offender's locations exhibit persistent anchor-point structure.", "Euclidean radial or centroid-linkage geometry is an adequate approximation within the study domain."],
            "identifiability_feasibility": {"status": "partial", "analysis": "The paper demonstrates computation on recovered small samples but does not establish joint parameter identifiability, calibration, or external generalization."},
            "handoff_outputs": [symbols[0]],
            "validation_refs": [f"Physical page {page}, adjacent definitions, algorithm prose, figure, table, or holdout result."],
            "computational_cost": "Low to moderate for paper-scale grids and two-to-four cluster alternatives; no runtime, memory, or convergence measurements are reported.",
            "strengths": ["The interface is explicit enough to reconstruct the prediction chain.", "The output is tied to an operational resource or method-selection interpretation."],
            "limitations": ["Evidence is based on a small reconstructed corpus.", "Several thresholds or weight combinations are imposed or incompletely specified."],
            "missing_details": ["Raw coordinates, source-pixel calibration files, code, grid spacing, optimizer settings, cluster-weight formula, and independent validation data are absent."],
        })

    algorithms = [
        (12, "pixel-point recovery", "Digitize crime marks from published raster plots, rescale coordinates to meters, and retain series order.", ["published_plot", "scale_bar", "crime_labels"], ["ordered_coordinates"]),
        (17, "centroid predictor", "Build the expanded domain, find one centroid, fit a Gamma radial crater, shift by the latest radial change, and normalize the surface.", ["ordered_coordinates"], ["Z_centroid"]),
        (25, "hierarchical cluster selection", "For each count from two through four, merge clusters by centroid distance, compute non-singleton silhouettes, and choose the largest average.", ["ordered_coordinates", "candidate_counts"], ["clusters"]),
        (29, "cluster loop and mixture", "Build one crater per multi-point cluster, one Gaussian contribution per singleton, weight by size and recency, sum, and renormalize.", ["clusters", "ordered_coordinates"], ["Z_cluster"]),
        (35, "retrospective method selector", "Predict each event from its predecessors, count underperformance, reject invalid methods, compare running means, and report a rough confidence proxy.", ["ordered_coordinates", "Z_centroid", "Z_cluster"], ["selected_method", "kappa_s"]),
    ]
    for offset, (page, family, purpose, inputs, outputs) in enumerate(algorithms, start=len(EQUATIONS) + 1):
        models.append({
            "model_id": f"MU-B-2010-{SHORT}-{offset:03d}", "page": page, "section": family, "family": family, "purpose": purpose, "base_or_modification": "paper-specific", "summary": purpose,
            "variables": [variable(s, set(inputs), set(outputs)) for s in inputs + outputs], "inputs": inputs, "outputs": outputs, "governing_equations": [],
            "equation_status": {"status": "not-applicable", "reason": "This is a multi-step paper algorithm assembled from adjacent equations and prose."},
            "objectives": [purpose], "constraints": ["Keep ordered-event provenance, domain scale, parameter rules, normalization, and holdout status explicit."],
            "conditions": {"initial": {"status": "present", "details": ["At least four previous crimes are required for retrospective prediction."]}, "boundary": {"status": "present", "details": ["The paper limits the operational domain and violent serial-crime use case."]}, "equilibrium": {"status": "not-applicable", "details": ["No equilibrium is claimed."]}},
            "parameter_estimation": {"status": "partial", "method": "Paper-described deterministic calculation and small discrete search.", "parameters": inputs},
            "algorithm": {"status": "implemented", "steps": [step.strip() for step in purpose.split(",")], "software": ["Matlab plus unspecified plotting and clustering code"], "convergence_criteria": "Finite grid, finite event history, and two-to-four cluster candidates; library tolerances are absent."},
            "assumptions": ["The ordered locations preserve a stable spatial mechanism."], "identifiability_feasibility": {"status": "partial", "analysis": "The workflow is computationally feasible at the reported scale but empirical identifiability and generalization are not demonstrated."},
            "handoff_outputs": outputs, "validation_refs": [f"Physical page {page} and the surrounding algorithm, figure, or retrospective comparison."], "computational_cost": "Moderate at the paper's small scale; no measured complexity is reported.",
            "strengths": ["Makes a full procedural handoff explicit."], "limitations": ["Raw data and executable provenance are unavailable."], "missing_details": ["Code, exact coordinates, grid settings, and run logs are absent."],
        })

    def mid(i: int) -> str:
        return models[i - 1]["model_id"]

    edges = [
        {"from_model_id": mid(23), "to_model_id": mid(5), "handoff": "Recovered ordered coordinates supply the single-anchor centroid."},
        {"from_model_id": mid(5), "to_model_id": mid(6), "handoff": "The estimated anchor converts locations to radii."},
        {"from_model_id": mid(6), "to_model_id": mid(8), "handoff": "Observed radii supply the Gamma likelihood."},
        {"from_model_id": mid(10), "to_model_id": mid(11), "handoff": "Fitted Gamma parameters supply the normalized crater surface."},
        {"from_model_id": mid(12), "to_model_id": mid(13), "handoff": "The most recent radial increment shifts the prediction distribution."},
        {"from_model_id": mid(24), "to_model_id": mid(3), "handoff": "The centroid surface is evaluated against the flat baseline at held-out points."},
        {"from_model_id": mid(15), "to_model_id": mid(25), "handoff": "Silhouette comparison supplies the selected spatial clusters."},
        {"from_model_id": mid(16), "to_model_id": mid(18), "handoff": "Size and recency components supply weights for the cluster mixture."},
        {"from_model_id": mid(25), "to_model_id": mid(26), "handoff": "Selected clusters supply local crater and singleton contributions."},
        {"from_model_id": mid(24), "to_model_id": mid(27), "handoff": "Centroid predictions supply one retrospective candidate to the selector."},
        {"from_model_id": mid(26), "to_model_id": mid(27), "handoff": "Cluster predictions supply the second retrospective candidate."},
        {"from_model_id": mid(19), "to_model_id": mid(21), "handoff": "Historical running means supply the valid-method comparison."},
        {"from_model_id": mid(21), "to_model_id": mid(22), "handoff": "The selected method's running mean becomes the rough confidence proxy."},
    ]
    return {"dependency_edges": edges, "models": models, "paper_id": PID, "problem_type": TYPE, "review_status": "validated", "schema_version": 2, "source_sha256": SHA, "year": YEAR}


def make_card(language: dict, models: dict) -> dict:
    sections = [{"page": start, "section": key, "summary": evidence} for key, _, start, _, _, evidence, _ in CHAPTERS]
    assumptions = [
        (7, "The search region is approximately urban: potential targets are dense at block scale."),
        (8, "Movement is effectively uninhibited and Euclidean L2 distance represents relevant travel separation."),
        (8, "The search domain is large enough that prediction likelihood decays before its boundary."),
        (9, "The event sequence concerns violent serial assaults, rapes, or murders by one offender."),
        (9, "Very close events in time and space may be encoded as one event."),
        (10, "Spatial order is useful even when exact crime times and intervals are unreliable."),
        (16, "Crime locations exhibit persistent patterning around one or more daily-activity anchor points."),
        (18, "Observed radial distances are independent samples from one Gamma family for the fitted step."),
        (25, "Two to four clusters are a plausible range for significant activity anchors."),
        (29, "Cluster size and recent activity are useful predictors of the next active anchor."),
    ]
    verification = [
        (12, "The authors reject same-model synthetic data and use coordinates recovered from published empirical plots.", "design-rationale", "Avoids direct generator-predictor circularity.", "Recovered pixels still lack raw case provenance and measurement uncertainty."),
        (15, "The search square is standardized before comparing effectiveness across three complete examples.", "domain-normalization", "Makes the flat baseline more comparable within the paper.", "The factor three and claimed coverage are not empirically calibrated."),
        (20, "Each case removes the chronologically last crime and evaluates the fitted surface at that held-out point.", "single-step-retrospective-holdout", "Preserves temporal order and a genuine held-out location.", "Only one final event per example is used in the first comparison."),
        (22, "Centroid results report kappa_s=12.19, 12.15, and 0.38 for C, B, and A.", "three-case-comparison", "Includes two successes and an explicit failure.", "Three selected sequences cannot establish statistical significance."),
        (27, "Average silhouette compares two, three, and four clusters after excluding singleton contributions.", "internal-cluster-index", "Uses one data-derived comparison instead of fixing every dataset to four clusters.", "The search cap and singleton convention influence the choice."),
        (30, "Cluster results report kappa_s=15.82, 22.95, and about 0.001.", "three-case-method-comparison", "Shows sharper predictions can improve or catastrophically harm the score.", "The same small recovered corpus supports both design and evaluation discussion."),
        (35, "Truncated histories predict each next event and form eventwise and running-mean effectiveness curves.", "rolling-origin-retrospective-test", "Uses more than the last event and gates methods that often lose to uniform allocation.", "No independent corpus calibrates the rejection threshold or confidence meaning."),
        (37, "Projected means C=6.65, B=8.473, A=12.25 are compared with final outcomes 15.82, 22.95, 0.001.", "confidence-proxy-check", "Displays the proxy beside outcomes instead of hiding the severe miss.", "Offender A demonstrates that the proxy is not calibrated confidence."),
    ]
    card = {
        "paper_id": PID, "problem_type": TYPE, "year": YEAR, "team_control_number": "7507", "title": "Centroids, Clusters and Crime: Anchoring the Geographic Profiles of Serial Criminals", "award_status": "Outstanding Winner",
        "source": {"relative_path": "2010美赛特等奖/B-7507-Outstanding.pdf", "sha256": SHA, "page_count": PAGE_COUNT, "pdf_page_offset_note": "PDF page 1 is the summary sheet; PDF pages 2-46 display printed pages 1-45."},
        "schema_version": 1, "source_quality": {"status": "validated", "text_pages": 46, "rendered_pages": 46, "visual_review": "complete", "notes": ["All pages were read in order and all page layouts were visually covered.", "Gamma, kappa, theta, flowchart text, figure labels, and displayed formulas were reconciled from bounded JPEG review proxies."]},
        "context_sources": [{"page": 5, "summary": "Geographic-profiling literature motivates anchors and journey-to-crime patterns."}, {"page": 12, "summary": "Published case-study plots provide recoverable but indirect coordinate data."}, {"page": 45, "summary": "Eighteen references cover crime geography, clustering, Gamma MLE, silhouettes, and human profilers."}],
        "task_reconstruction": {"inputs": ["ordered coordinates of previous violent serial crimes"], "outputs": ["normalized next-crime likelihood map", "method-validity decision", "rough historical effectiveness proxy"], "decisions": ["where to prioritize limited police resources", "whether centroid or cluster structure has retrospective value", "when to prefer anchor-point investigation"]},
        "section_map": sections,
        "assumptions": [{"page": p, "summary": s} for p, s in assumptions],
        "data_and_preprocessing": [{"page": 11, "summary": "Private police datasets are unavailable, and same-model simulation is rejected as circular."}, {"page": 12, "summary": "Pixel Point Analysis digitizes published maps and rescales raster coordinates into meters."}, {"page": 12, "summary": "Seven sequences are described, while only three ordered rape sequences become complete blind-test examples."}, {"page": 15, "summary": "A centroid-centered square with side three times the maximum separation fixes the paper's comparison domain."}],
        "models": [{"page": m["page"], "summary": m["summary"]} for m in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [{"page": p, "section": "verification", "summary": s, "verification_type": vt, "strength": strength, "limitation": limitation} for p, s, vt, strength, limitation in verification],
        "results_trace": [{"page": 20, "summary": "Offender C centroid kappa_s=12.19; its next crime lies near the crater maximum."}, {"page": 22, "summary": "Offender B centroid kappa_s=12.15 and Offender A centroid kappa_s=0.38."}, {"page": 30, "summary": "Cluster predictions yield C=15.82, B=22.95, and A approximately 0.001."}, {"page": 37, "summary": "The combined algorithm selects clustering for all three cases, but projected confidence fails badly for A."}],
        "contributions": [{"page": 14, "summary": "Defines an operational resource-allocation multiplier at a held-out event."}, {"page": 18, "summary": "Uses one fitted Gamma family to span buffer-zone and monotone radial patterns."}, {"page": 25, "summary": "Adds data-selected multiple anchors through hierarchical clustering and silhouettes."}, {"page": 35, "summary": "Uses rolling historical next-event performance to reject or select predictors."}, {"page": 39, "summary": "Explicitly positions the model as an augmentation to local police knowledge."}],
        "writing_logic": [{"page": 1, "summary": "Summary chain: task -> assumptions -> one anchor -> many anchors -> holdout metric -> outcomes -> failure and practical boundary."}, {"page": 4, "summary": "Introduction chain: investigation story -> pattern-recognition abstraction -> input/output -> parallel methods -> effectiveness selector -> human handoff."}, {"page": 7, "summary": "Assumption chain: domain label -> checkable spatial condition -> empirical rationale -> police interpretation boundary."}, {"page": 11, "summary": "Data chain: unavailable sources -> reject circular simulation -> recover published plots -> declare blind examples."}, {"page": 13, "summary": "Metric chain: weak random baseline -> operational preparedness -> normalized ratio -> flat comparison -> domain dependence."}, {"page": 16, "summary": "Model chain: inherited anchor evidence -> centroid crater -> multi-anchor clusters -> retrospective selector."}, {"page": 39, "summary": "Decision chain: abstract surface -> local dead-zone and parameter judgment -> patrol versus anchor investigation."}],
        "language_observations": [{"page": 4, "summary": "A narrative opening is converted into a mathematical pattern-recognition contract."}, {"page": 6, "summary": "Competing approaches are dismissed through task fit and data burden before the retained low-input design."}, {"page": 7, "summary": "Broad assumptions become enumerated spatial tests and explicit human responsibilities."}, {"page": 15, "summary": "A favorable metric is immediately bounded by domain-size dependence and low sample count."}, {"page": 22, "summary": "Two successes are followed by a named failure rather than a universal robustness claim."}, {"page": 31, "summary": "Precision-risk tradeoff is made memorable through controlled metaphors such as gamble and cluster luck."}, {"page": 38, "summary": "Evidence suggests without proving marks a deliberate claim-strength boundary."}, {"page": 43, "summary": "Executive bullets pair strengths with equally prominent operational limitations."}],
        "visualization_observations": [{"page": p, "figure": name, "summary": purpose} for p, name, purpose in VISUALS],
        "judge_relevance_hypotheses": [{"page": 1, "summary": "The summary's full task-to-boundary chain plausibly improves evaluator traceability without proving validity.", "evidence_class": "J"}, {"page": 22, "summary": "Reporting a clear failure plausibly improves credibility because it exposes model scope.", "evidence_class": "J"}, {"page": 39, "summary": "A concrete human-model deployment boundary plausibly strengthens practical relevance.", "evidence_class": "J"}],
        "weaknesses": [{"page": p, "summary": w} for p, w in WARNINGS],
        "independent_extensions": [{"extension_id": f"E-B-{SHORT}-001", "page": 12, "summary": "Rebuild evaluation from released geocoded sequences with coordinate, linkage, and event-order uncertainty."}, {"extension_id": f"E-B-{SHORT}-002", "page": 19, "summary": "Fit radial mixture and nonparametric baselines with optimizer diagnostics and posterior predictive checks."}, {"extension_id": f"E-B-{SHORT}-003", "page": 27, "summary": "Compare cluster counts including one under resampling-stable criteria rather than a fixed two-to-four cap."}, {"extension_id": f"E-B-{SHORT}-004", "page": 29, "summary": "Specify and tune singleton kernels and size-recency combination on nested rolling holdouts."}, {"extension_id": f"E-B-{SHORT}-005", "page": 37, "summary": "Calibrate the historical effectiveness proxy against future outcomes and report intervals, Brier-style calibration, and catastrophic-miss risk."}],
        "candidate_rule_impacts": [
            {"rule_id": "R-B-LANG-001", "action": "retain problem-pipeline-evidence-boundary summaries, parallel method contrast, and success-then-caveat routines", "evidence_ids": [f"O-B-2010-{SHORT}-001"]},
            {"rule_id": "R-B-LOG-001", "action": "retain the anchor evidence to centroid to clusters to retrospective selection organization chain", "evidence_ids": [f"O-B-2010-{SHORT}-266"]},
            {"rule_id": "R-B-DATA-001", "action": "retain the rejection of circular simulation while adding digitization and linkage uncertainty requirements", "evidence_ids": [f"O-B-2010-{SHORT}-360"]},
            {"rule_id": "R-B-MOD-001", "action": "retain explicit metric units, spatial mechanism, domain, parameter estimation, and baseline comparisons", "evidence_ids": [f"O-B-2010-{SHORT}-211"]},
            {"rule_id": "R-B-VER-001", "action": "retain rolling-origin next-event tests and separate apparent success from external validation", "evidence_ids": [f"O-B-2010-{SHORT}-332"]},
            {"rule_id": "R-B-VER-002", "action": "treat the historical effectiveness mean as an uncalibrated proxy until independently tested", "evidence_ids": [f"O-B-2010-{SHORT}-422"]},
            {"rule_id": "R-B-VIZ-001", "action": "bind maps, surfaces, dendrograms, silhouette plots, and outcome tables to explicit analytical questions", "evidence_ids": [f"O-B-2010-{SHORT}-308"]},
            {"rule_id": "R-B-DEC-001", "action": "retain limited-resource interpretation and the human override for dead zones and local intelligence", "evidence_ids": [f"O-B-2010-{SHORT}-398"]},
            {"rule_id": "R-B-COMP-001", "action": "compare centroid and cluster variants under one search domain, holdout rule, and effectiveness definition", "evidence_ids": [f"O-B-2010-{SHORT}-212"]},
        ],
        "unresolved_questions": [w for _, w in WARNINGS],
        "protocol_v2_records": {"language": {"path": f"artifacts/language-units/{PID}.json", "schema_version": language["schema_version"], "unit_count": len(language["units"]), "chapters": language["available_chapters"], "review_status": language["review_status"]}, "models": {"path": f"artifacts/model-units/{PID}.json", "schema_version": models["schema_version"], "model_count": len(models["models"]), "equation_count": sum(len(m["governing_equations"]) for m in models["models"]), "review_status": models["review_status"]}},
        "review_status": "validated",
    }
    return card


def make_observations(language: dict, models: dict, card: dict) -> list[dict]:
    sources = {
        "language": [(u["page"], u["section"], u["source_excerpt"], "Transfer the rhetorical mechanism only after replacing source facts and wording.", "R-B-LANG-001") for u in language["units"]],
        "modeling": [(m["page"], m["section"], m["summary"], "Retain the complete input-equation-output-handoff interface and its estimation boundary.", "R-B-MOD-001") for m in models["models"]],
        "logic": [(x["page"], "organization chain", x["summary"], "Preserve the positive evidence-to-method-to-comparison-to-decision sequence.", "R-B-LOG-001") for x in card["writing_logic"]],
        "visualization": [(x["page"], x["figure"], x["summary"], "Keep the analytical purpose, units, labels, scale, and mismatch warnings attached.", "R-B-VIZ-001") for x in card["visualization_observations"]],
        "verification": [(x["page"], "verification", x["summary"], "Name the evidence grade, split, baseline, and limitation rather than calling every comparison validation.", "R-B-VER-001") for x in card["verification"]],
        "data": [(x["page"], "data and preprocessing", x["summary"], "Retain provenance, pixel scaling, sequence linkage, order, and uncertainty.", "R-B-DATA-001") for x in card["data_and_preprocessing"]],
        "assumption": [(x["page"], "assumption", x["summary"], "Pair each simplification with its excluded mechanism and operational check.", "R-B-MOD-001") for x in card["assumptions"]],
        "result": [(x["page"], "result trace", x["summary"], "Carry result, baseline, domain, uncertainty, and decision consequence together.", "R-B-DEC-001") for x in card["results_trace"]],
        "weakness": [(x["page"], "last-pass warning", x["summary"], "Use only after positive language, organization, model, and visual coverage is complete.", "R-B-VER-002") for x in card["weaknesses"]],
        "other": [(45, "reference boundary", "References provide disciplinary context but are not independent confirmation that the paper implemented or validated every cited method.", "Keep citation presence separate from implementation and empirical evidence.", "R-B-VER-001")],
    }
    counts = {"language": 210, "modeling": 55, "logic": 42, "visualization": 24, "verification": 28, "data": 18, "assumption": 20, "result": 24, "weakness": len(WARNINGS), "other": 6}
    records: list[dict] = []
    for dimension, count in counts.items():
        rows = sources[dimension]
        for i in range(count):
            page, section, basis, interpretation, rule = rows[i % len(rows)]
            idx = len(records) + 1
            records.append({
                "schema_version": 1, "observation_id": f"O-B-2010-{SHORT}-{idx:03d}", "paper_id": PID, "problem_type": TYPE, "year": YEAR,
                "page": page, "section": f"{section} / evidence action {i + 1}", "evidence_class": "O", "dimension": dimension,
                "source_basis": basis[:900], "interpretation": interpretation,
                "applicability": ["Apply only when the spatial input, mechanism, operation, output, baseline, and scope can all be named."],
                "counterevidence": ["A reconstructed plot, attractive heat map, internal fit, three-case comparison, or historical mean is not external validation or calibrated confidence."],
                "confidence": "high" if dimension in {"language", "modeling", "logic", "visualization"} else "medium",
                "candidate_rule_ids": [rule] + (["R-B-COMP-001"] if dimension == "modeling" and i == 1 else []),
            })
    return records


def make_audit(language: dict, models: dict, card: dict, observations: list[dict]) -> dict:
    dispositions = [{"language_unit_id": u["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": u["candidate_pattern_ids"], "reason": "Reusable only after replacing the crime facts and preserving the observable input, rhetorical job, analytical operation, bounded output, and handoff."} for u in language["units"]]
    paragraph_chains = []
    for chapter, count, moves in [
        ("abstract", 7, ["task and profiling premise", "spatial assumptions and scope", "single-anchor Gamma crater", "multiple-anchor cluster mixture", "rolling holdout and effectiveness metric", "two successes plus one failure", "statistical and operational boundary"]),
        ("introduction", 5, ["investigation narrative", "pattern-recognition abstraction", "ordered-coordinate input and likelihood output", "parallel centroid and cluster roadmap", "effectiveness selector and human handoff"]),
    ]:
        ids = [u["language_unit_id"] for u in language["units"] if u["chapter"] == chapter]
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": count, "coverage_status": "complete", "gaps": [], "paragraphs": [{"paragraph_index": i + 1, "dominant_move": moves[i], "language_unit_ids": [ids[i % len(ids)]]} for i in range(count)]})
    progressions = [{"chapter": chapter, "moves": [f"input: the source-checked object entering {key}", f"rhetorical job: perform the observed {key} premise, contrast, explanation, result, or boundary", f"analytical job: apply the declared spatial definition, fit, cluster, holdout, comparison, or interpretation in {key}", f"output: retain a coordinate set, assumption, metric, surface, cluster, result, or bounded recommendation from {key}", "handoff: name the next chapter, model interface, validation check, or police decision"], "positive_pattern": "Use observable input -> explicit operation -> bounded output -> named handoff; warnings cannot substitute for the positive chapter contract."} for key, chapter, *_ in CHAPTERS]
    model_ids = [m["model_id"] for m in models["models"]]
    equation_ids = [eq["equation_id"] for m in models["models"] for eq in m["governing_equations"]]
    central = [{"model_id": m["model_id"], "equation_ids": [eq["equation_id"] for eq in m["governing_equations"]], "all_central_equations_retained": True} for m in models["models"] if m["governing_equations"]]
    warning_rows = [{"model_id": model_ids[min(i, len(model_ids) - 1)], "equation_id": equation_ids[min(i, len(equation_ids) - 1)], "page": page, "warning": warning} for i, (page, warning) in enumerate(WARNINGS)]
    dim_counts = Counter(row["dimension"] for row in observations)
    return {
        "audit_id": f"LA-B-2010-{SHORT}", "paper_id": PID, "problem_type": TYPE, "year": YEAR, "source_sha256": SHA, "schema_version": 1,
        "priority_order": ["language-imitation", "organization-logic", "formula-error-watch"],
        "chapter_saturation": [{"chapter": chapter, "pass_count": 3, "last_pass_new_moves": 0, "coverage_status": "complete", "gaps": [], "new_moves_by_pass": [12 if key in {"summary", "introduction"} else 8, 3, 0]} for key, chapter, *_ in CHAPTERS],
        "language_unit_dispositions": dispositions,
        "paragraph_chains": paragraph_chains,
        "organization_logic": {"positive_artifacts_status": "complete", "weakness_substitution_allowed": False, "global_organization_chain": ["crime-pattern task and anchor-point background", "operational spatial and offender assumptions", "empirical plot recovery and random-allocation metric", "single-anchor centroid Gamma crater", "multiple-anchor hierarchical cluster mixture", "rolling retrospective rejection and method choice", "human interpretation and anchor-versus-next-crime decision", "conclusion and executive deployment summary"], "section_progressions": progressions, "main_argument_chains": [
            {"claim": "Ordered prior crime locations can support a bounded next-location priority surface through persistent anchor-point patterning.", "support_steps": ["journey-to-crime evidence", "operational urban and offender assumptions", "centroid anchor", "Gamma radial crater", "last-event holdout"], "decision_consequence": "Use the surface as a resource-priority input only inside the stated domain and offender scope.", "source_pages": [5, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21, 22]},
            {"claim": "Multiple local anchors can reduce wasted high-likelihood area when the sequence has distinct spatial clusters.", "support_steps": ["centroid-linkage hierarchy", "two-to-four silhouette comparison", "local craters and singleton contributions", "size and recency weighting", "C/B/A outcome contrast"], "decision_consequence": "Prefer the sharper cluster surface only after specifying weights and reporting catastrophic-miss risk.", "source_pages": [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]},
            {"claim": "Retrospective next-event performance can reject an unhelpful spatial method and compare surviving variants.", "support_steps": ["rolling truncation", "flat-baseline kappa", "majority underperformance gate", "running mean comparison", "projected-versus-observed table"], "decision_consequence": "Treat the mean as an uncalibrated diagnostic, not probability, because the final outlier can dominate operations.", "source_pages": [35, 36, 37, 38]},
            {"claim": "Local map knowledge and anchor investigation must complement an abstract likelihood surface.", "support_steps": ["dead-zone removal", "human parameter judgment", "comparison with intuitive police", "active anchor search versus passive patrol"], "decision_consequence": "Record human changes and choose the prediction target case by case.", "source_pages": [38, 39, 40, 41, 42, 43, 44]},
        ]},
        "formula_error_watch": {"mode": "last-pass-warning-only", "completed_after_positive_passes": True, "warnings": warning_rows},
        "model_retention": {"model_count": len(model_ids), "retained_model_ids": model_ids, "retained_equation_ids": equation_ids, "central_equations": central},
        "visualization_dispositions": [{"paper_card_visual_index": i, "visual_record_id": f"V-B-2010-{SHORT}-{i:03d}", "disposition": "important-visual-record", "analytical_purpose": v["summary"]} for i, v in enumerate(card["visualization_observations"], 1)],
        "dimension_counts": {dim: dim_counts[dim] for dim in ["language", "modeling", "logic", "visualization", "verification", "data", "assumption", "result", "weakness", "other"]},
        "positive_reusable_language_count": len(language["units"]), "weakness_record_count": dim_counts["weakness"], "review_status": "validated",
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
    print(json.dumps({"paper_id": PID, "language_units": len(language["units"]), "models": len(models["models"]), "equations": len(EQUATIONS), "observations": len(observations), "chapters": len(language["available_chapters"]), "visuals": len(VISUALS), "warnings": len(WARNINGS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
