from __future__ import annotations

"""Assemble create-only Queue 112 G7-G8 learning artifacts."""

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-40612-8bcdc1a7"
SHORT = "40612"
SHA = "8bcdc1a780f3e08a678c1f450512da6656300cbb3c537ac5e97b29824f07322f"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 34
STAGE = ROOT / "tmp/q112-stage-v1"
LANGUAGE_PATH = ROOT / "tmp/q112-language-stage-v1/language.json"
ORGANIZATION_PATH = ROOT / "tmp/q112-organization-stage-v1/organization.json"
MODELS_PATH = ROOT / "tmp/q112-model-stage-v2/models.json"
VISUALS_PATH = ROOT / "tmp/q112-visual-stage-v1/visuals.json"
EXTRACTION_PATH = ROOT / f"artifacts/papers/{PAPER_ID}/extraction.json"


WARNINGS = [
    {"page": 10, "model_id": "MU-B-2015-40612-001", "equation_id": "EQ-B-2015-40612-001", "summary": "N0=alpha V is structurally clear, but alpha is neither identified from aircraft/debris data nor given a unit-consistent value; it must remain an uncalibrated parameter."},
    {"page": 11, "model_id": "MU-B-2015-40612-002", "equation_id": "EQ-B-2015-40612-003", "summary": "The printed velocity components are v_x=cos(theta) and v_y=sin(theta), omitting multiplication by v and conflicting dimensionally with the later I=mv sin(theta) expression."},
    {"page": 11, "model_id": "MU-B-2015-40612-002", "equation_id": "EQ-B-2015-40612-004", "summary": "The prose calls m total weight while the impulse equation treats m as mass; units must be reconciled before numerical use."},
    {"page": 12, "model_id": "MU-B-2015-40612-002", "equation_id": "EQ-B-2015-40612-005", "summary": "The piecewise beta rule is explicit, but I0 and gamma have no data source, fitted values, units audit, or uncertainty, so it cannot yield a reproduced drifter count."},
    {"page": 12, "model_id": "MU-B-2015-40612-003", "equation_id": None, "summary": "The system module combines current data and computer random motion without specifying distributions, time step, interpolation details, seeds, execution environment, or archived trajectories; its output is synthetic rather than an exact answer."},
    {"page": 15, "model_id": "MU-B-2015-40612-004", "equation_id": "EQ-B-2015-40612-006", "summary": "Equation (6) is retained as F(D)=1-2^2/(D^2+2^2) with medium transcription confidence, but the nine-accident sample, distance units, fitting criterion, residuals, and uncertainty are absent."},
    {"page": 15, "model_id": "MU-B-2015-40612-004", "equation_id": None, "summary": "The 50/50 mixture of LKP reachability and accident-distance distributions is a cited heuristic choice, not a calibrated mixing estimate."},
    {"page": 16, "model_id": "MU-B-2015-40612-005", "equation_id": None, "summary": "The reverse-drift model uses a 0.25 speed coefficient and linear current interpolation without a reproducible OSCAR snapshot, leeway model, interpolation equation, boundary treatment, or validation against tracked debris."},
    {"page": 17, "model_id": "MU-B-2015-40612-006", "equation_id": None, "summary": "The 70/30 surface-prior mixture is justified qualitatively by current uncertainty but is not inferred from observations or stress-tested jointly with the drift model."},
    {"page": 18, "model_id": "MU-B-2015-40612-006", "equation_id": "EQ-B-2015-40612-007", "summary": "Equation (7) is a normalized Bayes form, but P(B|S_i,j), report semantics, detection rates, cell evidence, and numerical arrays are not parameterized, preventing posterior reproduction."},
    {"page": 18, "model_id": "MU-B-2015-40612-006", "equation_id": None, "summary": "The surface update assumes at most one drifter per cell and identical drifter movement/detection despite a shared initial point and heterogeneous debris, with no grid-resolution check."},
    {"page": 19, "model_id": "MU-B-2015-40612-007", "equation_id": None, "summary": "The underwater prior's 30/70 weights, wreckage likelihood PAkW, phase evidence, and stopping/suspension policy are not calibrated; recursion alone does not establish convergence or localization reliability."},
    {"page": 22, "model_id": "MU-B-2015-40612-008", "equation_id": None, "summary": "The branch-and-bound claim lacks formal decision variables, constraints, bounds, branching rules, search trace, and optimality certificate; parallel rankings and a diagram do not reproduce the stated maximization."},
    {"page": 24, "model_id": "MU-B-2015-40612-009", "equation_id": None, "summary": "AF447 validation consists only of the reported location lying inside a displayed suggestive area; region area, nominal coverage, baseline comparison, temporal holdout, and scoring rule are absent."},
    {"page": 27, "model_id": "MU-B-2015-40612-009", "equation_id": None, "summary": "The MH370 result imports a cited arc distribution and assumes no detection in both search stages; without frozen data, likelihoods, or outcome validation it is a conditional scenario, not a verified wreckage prediction."},
    {"page": 29, "model_id": "MU-B-2015-40612-010", "equation_id": None, "summary": "The nine synthetic aircraft types are not mapped to the real platforms in Table 1, and Table 6 repeats the 7+9 row; the capability experiment is therefore illustrative rather than fleet-calibrated."},
    {"page": 30, "model_id": "MU-B-2015-40612-010", "equation_id": None, "summary": "Tables 3-9 vary one factor across only three or selected nominal cases with no joint perturbation, uncertainty interval, normalization audit, or external test; narrow local changes do not establish robustness, credibility, flexibility, or universality."},
    {"page": 23, "model_id": "MU-B-2015-40612-009", "equation_id": None, "summary": "Application prose says the process follows Figure 1 although the probability workflow is Figure 2, and invokes drifter data from Table 3 before Table 3 appears as a later sensitivity table; cross-reference provenance is broken."},
    {"page": 32, "model_id": "MU-B-2015-40612-010", "equation_id": None, "summary": "The strengths and press sections overstate accuracy, efficiency, robustness, reliability, and broad applicability relative to the paper's uncalibrated parameters, synthetic module, local sensitivity, and limited case checks."},
]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_json(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def validate_inputs(language: dict, organization: dict, models: dict, visuals: dict) -> None:
    if any(record.get("paper_id") != PAPER_ID for record in (language, organization, models, visuals)):
        raise ValueError("q112 stage paper IDs do not agree")
    if language.get("review_status") != "validated" or len(language.get("units", [])) != 68:
        raise ValueError("G1-G3 language stage must be validated at 68 units")
    if len(language.get("available_chapters", [])) != 17 or len(organization.get("section_contracts", [])) != 17:
        raise ValueError("G4 must retain all 17 normalized chapters and contracts")
    if len(organization.get("paragraph_chains", {}).get("abstract", [])) != 3:
        raise ValueError("abstract chain must retain three visual paragraphs")
    if len(organization.get("paragraph_chains", {}).get("introduction", [])) != 3:
        raise ValueError("introduction chain must retain three visual paragraphs")
    if models.get("review_status") != "validated" or len(models.get("models", [])) != 10:
        raise ValueError("G5 must retain 10 model units")
    if sum(len(item.get("governing_equations", [])) for item in models["models"]) != 7:
        raise ValueError("G5 must retain all seven displayed equations or equation families")
    if len(models.get("dependency_edges", [])) != 19:
        raise ValueError("G5 must retain 19 dependency edges")
    if visuals.get("review_status") != "validated" or len(visuals.get("visuals", [])) != 23:
        raise ValueError("G6 must retain 14 figures and nine substantive tables")
    safety = visuals.get("transport_safety", {})
    if safety.get("total_bounded_jpeg_proxies") != 8 or safety.get("total_proxy_bytes") != 1854278:
        raise ValueError("G6 transport-safety ledger must retain all eight bounded proxies and exact bytes")
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
        (8, "The plane is fully loaded; accidents are divided into air and water disintegration; all broken pieces share one size."),
        (8, "Water impact is treated as an ideal collision with negligible horizontal impulse."),
        (8, "All drifters begin at the impact point and bodies and aircraft debris receive the same modeled movement effects."),
        (8, "Surface drift is generated only from current data plus unspecified computer random motion."),
        (9, "Underwater parts remain static after reaching the seafloor."),
        (9, "Surface drifters share movement and detection probability and remain stationary during each search phase."),
        (9, "No signal is available from the crashed aircraft and search vehicles are restricted to aircraft."),
        (9, "Aircraft capability is reduced to area limit and detection rate and is invariant to weather."),
        (9, "Underwater sensing reaches beyond seafloor depth."),
        (9, "Sensors have no false positives but may miss a present target."),
        (9, "Voyage constraints are replaced by search-area limits."),
        (18, "At most one drifter occupies a cell for the surface Bayes update."),
        (26, "MH370 surface and underwater phases are treated as nondetections for conditional propagation."),
    ]
    data = [
        (6, "AF447 and MH370 histories establish delayed-recovery stakes but are contextual cases, not a calibration sample."),
        (7, "Aircraft size, passenger load, material, crash state, and debris type motivate the target-count interface."),
        (8, "Table 1 compares three real search platforms by speed, voyage, and sensors, while later capability types are synthetic."),
        (10, "Table 2 defines N0, N, V, m, alpha, beta, v, theta, I, cell probabilities, and surface/underwater detection terms."),
        (12, "The system module uses an OSCAR current date, interpolation, a one-quarter current-speed coefficient, and random motion without freezing inputs."),
        (15, "Nine cited loss-of-control accidents provide the distance curve combined with LKP reachability."),
        (16, "Reverse drift depends on marine geography, surface currents, winds, spotted drifters, and backward trajectory construction."),
        (18, "Surface search reports B and aircraft-cell detection probability feed the normalized posterior."),
        (21, "Aircraft ranking uses area limit and surface/underwater detection probabilities as its capability interface."),
        (23, "AF447 wreckage location, date, depth, and initial-search information are drawn from the BEA report."),
        (25, "MH370 arc maps and constrained autopilot/data-error regions are imported from cited analyses."),
        (28, "Sensitivity inputs include N, fleet count, nine synthetic capability types, and three sets of prior-mixture weights."),
    ]
    verification = [
        {"page": 12, "section": "collision geometry", "summary": "Figure 1 and Equations (3)-(5) trace angle to impulse to a piecewise disintegration fraction.", "verification_type": "formula-and-diagram trace", "strength": "The intended physical handoff is visible.", "limitation": "Velocity components, mass/weight, I0, and gamma are unresolved."},
        {"page": 14, "section": "search workflow", "summary": "Figure 2 exposes mixture weights and surface/underwater phase ordering.", "verification_type": "architecture trace", "strength": "The end-to-end process and branch handoffs are inspectable.", "limitation": "Weights and observation likelihoods are heuristic or absent."},
        {"page": 17, "section": "drift behavior", "summary": "Figure 5 shows divergence of synthetic trajectories over two days.", "verification_type": "synthetic behavior check", "strength": "The reason for down-weighting drift is visually legible.", "limitation": "No random protocol, observed comparator, or archived inputs are supplied."},
        {"page": 18, "section": "surface Bayes update", "summary": "Equation (7) and Figure 7 connect a search report to a normalized posterior field.", "verification_type": "formula-to-output trace", "strength": "The posterior normalization structure is explicit.", "limitation": "Likelihoods and numerical arrays are not reproducible."},
        {"page": 22, "section": "allocation", "summary": "Figure 10 links cell and aircraft rankings to a heterogeneous allocation layout.", "verification_type": "algorithm schematic", "strength": "The intended priority matching is visible.", "limitation": "No branch-and-bound formulation or certificate is provided."},
        {"page": 24, "section": "AF447 application", "summary": "Figure 11 overlays the actual wreckage point on the suggested region.", "verification_type": "retrospective inclusion check", "strength": "A real case point is compared with a model region.", "limitation": "Area, coverage, baseline, and holdout metrics are absent."},
        {"page": 27, "section": "MH370 application", "summary": "Figures 12-14 trace a cited arc distribution through four conditional search fields.", "verification_type": "conditional scenario trace", "strength": "The stage-to-stage visual handoff is preserved.", "limitation": "The imported data and likelihood calculations are not frozen or externally validated."},
        {"page": 28, "section": "sensitivity", "summary": "Tables 3-9 expose response to target count, fleet quantity/type, and three mixture choices.", "verification_type": "local deterministic sensitivity", "strength": "Directions and small local weight changes are numerically visible.", "limitation": "No joint uncertainty, calibration, baseline, or out-of-sample validation is reported."},
    ]
    results = [
        (10, "Maximum target capacity is represented as N0=alpha V and actual targets as N=beta N0."),
        (12, "Water disintegration maps impact impulse through a zero-linear-saturation beta rule."),
        (15, "Flight dynamics combines LKP reachability and the accident-distance distribution at 50/50."),
        (17, "Surface prior combines flight dynamics and reverse drift at 70/30 after synthetic trajectories motivate lower drift weight."),
        (18, "Surface posterior uses normalized Bayes updating over the contemporary search area."),
        (20, "Underwater prior combines surface posterior and flight prior at 30/70 and unsuccessful phases recurse."),
        (22, "Allocation sorts cells and aircraft by probability/capability before invoking branch-and-bound maximization."),
        (24, "The reported AF447 wreckage point lies within the displayed suggested area."),
        (27, "MH370 yields four conditional prior/posterior fields under assumed surface and underwater nondetection."),
        (28, "Reported cumulative localization probability rises from 0.545 to 0.619 as N moves from 50 to 200."),
        (29, "Selected two-aircraft capability combinations report cumulative values between 0.434 and 0.554."),
        (30, "The three mixture sweeps vary reported cumulative probability only within 0.508-0.520 under fixed settings."),
    ]
    contributions = [
        (7, "Types the crashed-aircraft target and search-platform capability inputs before modeling."),
        (10, "Separates maximum drifter capacity from crash-dependent release fraction."),
        (12, "Adds a synthetic drift module to expose time-dependent dispersion before probability fusion."),
        (14, "Organizes surface and underwater search as staged prediction and update loops."),
        (15, "Combines reachability and accident-distance evidence into a flight-dynamics prior."),
        (16, "Uses reverse drift from spotted targets to connect currents with impact-location inference."),
        (18, "Normalizes cell probabilities after search reports rather than treating searched cells as certainly empty."),
        (21, "Connects heterogeneous aircraft capability to cell-priority allocation."),
        (24, "Carries the pipeline into AF447 and a conditional MH370 scenario with explicit evidence boundaries."),
        (32, "Translates the technical chronology into a press-facing account after the analytical sections."),
    ]
    extensions = [
        (10, "Estimate alpha, debris size classes, buoyancy, passenger survival targets, and uncertainty from aircraft and crash data."),
        (11, "Replace the printed component equations with a unit-checked collision model and calibrate I0 and gamma from impact tests or simulations."),
        (12, "Archive current fields, leeway coefficients, interpolation, stochastic distributions, seeds, time step, and trajectory outputs."),
        (18, "Define sensor-specific true/false detection likelihoods, cell occupancy, grid resolution, and normalized sequential evidence updates."),
        (21, "Formulate a reproducible mixed-integer allocation with coverage, time, endurance, coordination, revisit, and uncertainty constraints."),
        (24, "Evaluate case regions with proper scores, nominal coverage, area, baselines, temporal holdouts, and multiple incidents."),
        (28, "Run global and joint sensitivity with calibrated parameter ranges, uncertainty propagation, and decision-stability metrics."),
        (34, "Publish machine-readable inputs, equations, plots, optimizer traces, software versions, execution logs, and regression tests."),
    ]
    return {
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "Searching for a Lost Plane",
        "award_status": "outstanding",
        "source": {
            "relative_path": "2015美赛特等奖/B-40612-Outstanding.pdf",
            "sha256": SHA,
            "page_count": PAGE_COUNT,
            "pdf_page_offset_note": "Physical PDF pages and printed Page n of 34 labels agree one-to-one across pages 1-34.",
        },
        "schema_version": 1,
        "source_quality": {
            "status": "validated",
            "text_pages": PAGE_COUNT,
            "rendered_pages": PAGE_COUNT,
            "visual_review": "complete",
            "notes": [
                "All 34 physical pages were read sequentially through the title, contents, every substantive section, Tables 1-9, press paper, and References 1-19.",
                "Eight one-at-a-time byte-bounded JPEG proxies totaling 1,854,278 bytes covered pages 1-34 and focused the piecewise collision rule, branch weights, and normalized Bayes formula; no original full-page PNG entered model context.",
                "Seven displayed equations or equation families, Figures 1-14, and Tables 1-9 have source-ordered retention and dispositions.",
                "No clipping, overlap, missing page, blank page, black box, or formula-rendering failure was found; source formula, parameter, cross-reference, optimization, validation, and scope defects remain last-pass warnings.",
                "The official problem statement is not frozen with this paper, so task reconstruction is bounded to the paper's explicit objectives and outputs.",
            ],
        },
        "context_sources": [
            {"type": "paper", "path": "2015美赛特等奖/B-40612-Outstanding.pdf"},
            {"type": "extraction", "path": f"artifacts/papers/{PAPER_ID}/extraction.json"},
            {"type": "text-pages", "path": f"artifacts/papers/{PAPER_ID}/text/pages"},
            {"type": "visual-stage", "path": "tmp/q112-visual-stage-v1/visuals.json"},
        ],
        "task_reconstruction": {
            "status": "incomplete-official-task-unavailable",
            "inputs": ["aircraft volume, load, material, impact velocity and angle", "current fields, winds, spotted drifters, random-motion assumptions", "last-known position, accident-distance data, surface and underwater reports", "cell probabilities and aircraft area/detection capabilities", "AF447 location evidence, MH370 arc analyses, and sensitivity settings"],
            "outputs": ["maximum and actual drifter counts", "synthetic drift trajectories", "surface and underwater prior/posterior fields", "aircraft-cell allocation", "AF447 region comparison", "conditional MH370 fields", "sensitivity tables and press paper"],
            "decisions": ["how many targets may be detectable", "where surface and underwater search should concentrate", "how missed searches change priority", "which aircraft should search which cells", "what each case and sensitivity study actually supports"],
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
            {"page": 1, "summary": "The summary previews collision, staged Bayesian search, allocation, two cases, sensitivity, and limitations as one operational chain; award status does not prove which move caused judging success.", "evidence_class": "J"},
            {"page": 14, "summary": "The flowchart makes mixture weights and surface/underwater handoffs scannable before the detailed formulas.", "evidence_class": "J"},
            {"page": 24, "summary": "The AF447 overlay provides an immediate real-case comparison, although its validation strength is limited to qualitative inclusion.", "evidence_class": "J"},
            {"page": 32, "summary": "The press paper closes the technical-to-public loop after model, case, sensitivity, and limitation sections.", "evidence_class": "J"},
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
        "language": "Reuse the rhetorical mechanism only after replacing incident, aircraft, drifter, current, prior, likelihood, cell, resource, case, statistic, and audience entities.",
        "modeling": "Retain target generation, drift, mixture support, observation likelihood, posterior normalization, phase state, allocation constraints, validation, and decision handoff together.",
        "logic": "Preserve the positive incident-to-physical-state-to-surface/underwater-evidence-to-allocation-to-case-to-public-action chain before warnings.",
        "visualization": "Keep figure or table identity, axes, units, mixture, stage, scenario, source status, uncertainty, and exact supported claim together.",
        "verification": "Name the exact formula trace, flowchart handoff, synthetic behavior, posterior update, allocation schematic, case inclusion, scenario trace, or sensitivity table.",
        "data": "Retain source, date, units, aircraft/debris class, current product, interpolation, incident record, likelihood input, version, and downstream consumer.",
        "assumption": "Pair each collision, drifter, motion, sensor, seafloor, weather, signal, area-limit, occupancy, or nondetection assumption with its enabled computation and excluded regime.",
        "result": "Keep capacity, actual count, prior, posterior, phase, allocation, case overlay, scenario field, sensitivity value, and public claim distinct.",
        "weakness": "Record formula, parameter, likelihood, data, optimizer, validation, sensitivity, reference, and scope risks only after positive G1-G6 learning.",
        "other": "Separate cited context, imported maps, source text, mathematical intent, synthetic output, executable evidence, observed case data, and predictive validation.",
    }
    provenance = [
        (34, "references", "Nineteen references identify aviation, ocean-current, search-theory, AF447, and MH370 sources but do not freeze their bytes, versions, or calibration datasets."),
        (6, "incident history", "AF447 and MH370 timelines motivate the search problem without forming a representative evaluation sample."),
        (7, "target taxonomy", "Passenger, body, debris, material, load, and crash-state distinctions motivate target count while the final model collapses many classes."),
        (8, "platform specifications", "Three cited platform examples establish heterogeneity but do not calibrate the later nine synthetic capability types."),
        (10, "notation contract", "Table 2 exposes core symbols while several later parameters and assignment terms are absent."),
        (12, "collision source", "The rendered piecewise beta rule is source-checked, while I0 and gamma remain unidentified."),
        (12, "simulation provenance", "The source mentions current data and computer random motion without preserving a runnable protocol."),
        (14, "workflow weights", "The flowchart exposes 50/50, 70/30, and 30/70 choices as model architecture rather than fitted evidence."),
        (15, "accident-distance source", "Nine accidents motivate F(D), but the observations and fit diagnostics are not archived."),
        (16, "OSCAR source", "A current product and date are named without a frozen grid, query, interpolation implementation, or leeway data."),
        (18, "Bayes interface", "Equation (7) is normalized symbolically but lacks numerical likelihood and cell arrays."),
        (22, "allocation interface", "Quicksort and branch-and-bound are named without a formal optimization record."),
        (24, "AF447 comparator", "The reported wreckage point supports an inclusion check, not calibrated regional forecast validation."),
        (25, "MH370 maps", "Cited search and arc maps provide conditional scenario context without frozen source computations."),
        (28, "sensitivity outputs", "Seven small tables expose local responses without a joint uncertainty design."),
        (32, "press translation", "The public narrative preserves chronology but inherits the technical evidence and scope limits."),
    ]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = ["Apply only when incident evidence, target classes, units, current data, distribution support, likelihood, cell geometry, resource constraints, uncertainty, and receiving decision are explicit."]
        row["counterevidence"] = ["A smooth probability field, synthetic trajectory, ranked allocation, one included case point, conditional map, or three-level table does not prove calibration, posterior correctness, global optimality, reproducibility, robustness, or universal transfer."]
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
        ("R-B-LANG-001", "retain incident framing, physical target generation, mixture construction, posterior update, phase recursion, allocation, case trace, sensitivity boundary, limitation, public chronology, and provenance with typed slots", first["language"]),
        ("R-B-LOG-001", "trace target capacity through collision, synthetic drift, surface and underwater evidence, ranked assets, AF447/MH370 cases, sensitivity, and bounded public action", first["logic"]),
        ("R-B-DATA-001", "version aircraft/debris definitions, platform specifications, current products, accident records, likelihood inputs, case locations, arc analyses, units, and execution environment", first["data"]),
        ("R-B-DATA-002", "maintain assumptions for load, equal piece size, ideal collision, shared starting point, identical motion/detection, static phases, sensor errors, weather invariance, seafloor reach, cell occupancy, and nondetection", evidence("R-B-DATA-002")),
        ("R-B-MOD-001", "retain capacity, disintegration, synthetic drift, flight and reverse priors, surface posterior, underwater recursion, resource allocation, case application, sensitivity, and decision interfaces", first["modeling"]),
        ("R-B-MOD-003", "combine physical target state, spatial priors, search likelihood, normalized posterior, phase transition, fleet assignment, and case decision only through typed unit, support, probability, time, and evidence contracts", evidence("R-B-MOD-003")),
        ("R-B-MOD-004", "keep maximum/actual drifters, prior/posterior, surface/underwater phase, capability type, assignment, case overlay, conditional forecast, local sensitivity, and public claim distinct", first["result"]),
        ("R-B-MOD-005", "stress alpha, I0, gamma, drift coefficient, random protocol, mixture weights, likelihoods, grid occupancy, recursion, allocation constraints, case scoring, and joint sensitivity", evidence("R-B-MOD-005")),
        ("R-B-VER-002", "make every reliability claim formula-, workflow-, trajectory-, posterior-, allocation-, case-, scenario-, sensitivity-, and provenance-specific", first["verification"]),
        ("R-B-VER-004", "reconcile velocity units, mass/weight, unidentified parameters, heuristic weights, missing likelihoods, absent optimizer trace, weak case checks, duplicate sensitivity rows, broken references, and unsupported scope claims", first["weakness"]),
        ("R-B-VIZ-001", "retain collision geometry, probability workflow, fitted distance curve, synthetic paths, stage PDFs, allocation, case maps, and all nine tables with labels, source status, uncertainty, and exact claims", first["visualization"]),
        ("R-B-COMP-001", "measure collision units, trajectory simulation, distribution normalization, likelihood evaluation, recursive updates, assignment optimization, case scores, sensitivity interactions, and reproducible runtime separately", evidence("R-B-COMP-001")),
    ]
    card["candidate_rule_impacts"] = [
        {"rule_id": rule_id, "action": action, "evidence_ids": [observation_id]}
        for rule_id, action, observation_id in entries
    ]


def build_audit(template, language: dict, organization: dict, models: dict, visuals: dict, card: dict, observations: list[dict]) -> dict:
    audit = template.make_audit(language, models, card, observations)
    paragraph_chains = []
    for chapter in ("abstract", "introduction"):
        paragraphs = []
        for source in organization["paragraph_chains"][chapter]:
            paragraphs.append({
                "paragraph_index": source["paragraph"],
                "dominant_move": f"{source['dominant_move']}: {source['claim']} -> {source['consequence']} -> {source['next_link']}",
                "language_unit_ids": source["language_unit_ids"],
            })
        paragraph_chains.append({"chapter": chapter, "visual_paragraph_count": len(paragraphs), "coverage_status": "complete", "gaps": [], "paragraphs": paragraphs})
    audit["paragraph_chains"] = paragraph_chains
    audit["language_unit_dispositions"] = [
        {"language_unit_id": unit["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": unit["candidate_pattern_ids"], "reason": "The rhetorical mechanism transfers only after replacing incident, target, aircraft, current, prior, likelihood, cell, phase, allocation, case, sensitivity, and audience entities."}
        for unit in language["units"]
    ]
    argument_metadata = {
        "physical-and-evidence-to-search-state": {"claim": "Aircraft properties, impact severity, and current-driven motion define what may be detectable and where evidence may originate.", "source_pages": [7, 8, 9, 10, 11, 12]},
        "surface-prior-to-posterior": {"claim": "LKP reachability, accident distance, reverse drift, and a search report move the surface stage from prior mixture to normalized posterior.", "source_pages": [13, 14, 15, 16, 17, 18]},
        "surface-to-underwater-recursion": {"claim": "Surface evidence and flight dynamics form an underwater prior that becomes recursively updated after each unsuccessful phase.", "source_pages": [18, 19, 20]},
        "ranked-assets-to-case-decisions": {"claim": "Ranked cell and platform capability interfaces carry the probability state into allocation, AF447 comparison, and conditional MH370 fields.", "source_pages": [21, 22, 23, 24, 25, 26, 27]},
        "sensitivity-to-public-and-provenance": {"claim": "Local target, fleet, and weight sweeps delimit what can be communicated through limitations, press chronology, and reference provenance.", "source_pages": [27, 28, 29, 30, 31, 32, 33, 34]},
    }
    chains = []
    for chain in organization["main_argument_chains"]:
        metadata = argument_metadata[chain["name"]]
        chains.append({"claim": metadata["claim"], "support_steps": chain["chain"], "decision_consequence": chain["decision"], "source_pages": metadata["source_pages"]})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": organization["global_progression"] + ["Only after the positive language, organization, model, and visual chain is complete does G7 record formula, parameter, likelihood, optimizer, validation, sensitivity, reference, and scope warnings."],
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
        "request_body_guard": {"bounded_jpeg_proxies": 8, "total_proxy_bytes": 1854278, "original_full_page_png_in_context": False},
    }
    return audit


def write_json_create(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    language = read_json(LANGUAGE_PATH)
    organization = read_json(ORGANIZATION_PATH)
    models = read_json(MODELS_PATH)
    visuals = read_json(VISUALS_PATH)
    extraction = read_json(EXTRACTION_PATH)
    validate_inputs(language, organization, models, visuals)
    if extraction.get("paper_id") != PAPER_ID or extraction.get("page_count") != PAGE_COUNT:
        raise ValueError("q112 extraction identity or page count does not match the current paper")

    template = load_module(ROOT / "scripts/build_q100_artifacts.py", "q100_template_for_q112")
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
    extraction["visual_review_status"] = "complete"
    extraction["visual_review"] = {
        "status": "complete",
        "reviewed_pages": list(range(1, PAGE_COUNT + 1)),
        "notes": [
            "All 34 physical pages were inspected through eight one-at-a-time byte-bounded JPEG proxies totaling 1,854,278 bytes. No clipping, overlap, missing page, blank page, black box, or formula-rendering failure was found.",
            "Figures 1-14, Tables 1-9, and seven displayed equations or equation families were reconciled by source page. Focused proxies covered the page-12 piecewise rule, page-14 probability flowchart, and page-18 normalized Bayes formula.",
            "No original full-page PNG, original-detail contact sheet, batched image response, or complete session JSONL entered model context.",
            "Source defects are retained separately, including formula/unit conflicts, unidentified parameters, heuristic weights, absent likelihoods, missing optimizer traces, weak case validation, local-only sensitivity, and broken cross-references.",
        ],
    }

    STAGE.mkdir(parents=True)
    write_json_create(STAGE / "language.json", language)
    write_json_create(STAGE / "models.json", models)
    write_json_create(STAGE / "card.json", card)
    write_json_create(STAGE / "audit.json", audit)
    write_json_create(STAGE / "extraction.json", extraction)
    with (STAGE / "observations.jsonl").open("x", encoding="utf-8", newline="\n") as handle:
        for row in observations:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

    print(json.dumps({"paper_id": PAPER_ID, "stage": str(STAGE), "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "models": len(models["models"]), "equations": 7, "dependency_edges": len(models["dependency_edges"]), "visuals": len(visuals["visuals"]), "observations": len(observations), "warnings": len(WARNINGS), "proxy_bytes": visuals["transport_safety"]["total_proxy_bytes"], "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
