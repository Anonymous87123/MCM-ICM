from __future__ import annotations

"""Assemble create-only Queue 110 G7-G8 learning artifacts."""

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-38720-26d38781"
SHORT = "38720"
SHA = "26d38781a179b71806799b0d20f118a5f0b09aa1cf6b8bc7a5e32562a7886a42"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 61
STAGE = ROOT / "tmp/q110-stage-v2"
LANGUAGE_PATH = ROOT / "tmp/q110-language-stage-v1/language.json"
ORGANIZATION_PATH = ROOT / "tmp/q110-organization-stage-v1/organization.json"
MODELS_PATH = ROOT / "tmp/q110-model-stage-v1/models.json"
VISUALS_PATH = ROOT / "tmp/q110-visual-stage-v1/visuals.json"
EXTRACTION_PATH = ROOT / f"artifacts/papers/{PAPER_ID}/extraction.json"


WARNINGS = [
    {"page": 15, "model_id": "MU-B-2015-38720-002", "equation_id": "EQ-B-2015-38720-002", "summary": "Equation 2 multiplies a dimensionless glide ratio by altitude in feet but reports r in miles without an explicit feet-to-miles conversion. Preserve the source expression and require a typed conversion before numeric reuse."},
    {"page": 23, "model_id": "MU-B-2015-38720-003", "equation_id": "EQ-B-2015-38720-004", "summary": "Equation 4 visibly compares the vector difference S_i-(x_crash,y_crash) with scalar d without a norm, and the crash-coordinate notation conflicts with the earlier (x_c,y_c) table. A runnable detector needs a scalar distance and one coordinate contract."},
    {"page": 24, "model_id": "MU-B-2015-38720-004", "equation_id": "EQ-B-2015-38720-006", "summary": "Equations 6, 11, 13, and 16 advance the search plane with v even though v was defined for the lost aircraft and v_s for the search plane. The implementation must resolve the symbol rather than silently assuming 400 mph."},
    {"page": 26, "model_id": "MU-B-2015-38720-005", "equation_id": "EQ-B-2015-38720-007", "summary": "Equations 7, 8, and 12 use the set-union symbol between Boolean boundary conditions. Corner precedence, simultaneous x/y violations, and equality behavior are also omitted, so the printed rule is not an executable boundary contract."},
    {"page": 29, "model_id": "MU-B-2015-38720-006", "equation_id": "EQ-B-2015-38720-009", "summary": "The weighted random path fixes a factor of 15 without calibration or sensitivity analysis. Its confidence-interval overlap with bounded random is treated as no significant difference, although interval overlap is not the reported hypothesis test."},
    {"page": 35, "model_id": "MU-B-2015-38720-008", "equation_id": "EQ-B-2015-38720-014", "summary": "Equations 14 and 17 define C(u) as a dimensionless alternating integer while the route uses it as a physical stripe displacement. The visually printed formulas appear to omit a sight-range scale such as d."},
    {"page": 35, "model_id": "MU-B-2015-38720-008", "equation_id": "EQ-B-2015-38720-015", "summary": "Equation 15 does not make clear whether C(j) is an absolute vertical coordinate or an incremental displacement, nor whether j and epsilon update before or after the move. Preserve this ambiguity in any transcription."},
    {"page": 38, "model_id": "MU-B-2015-38720-009", "equation_id": "EQ-B-2015-38720-018", "summary": "Equation 18 adds scalar C(j)r to vector S_i, reuses r from lost-aircraft glide range, and flips epsilon although its downstream role is unclear. The printed transition is dimensionally and algorithmically incomplete."},
    {"page": 43, "model_id": "MU-B-2015-38720-010", "equation_id": "EQ-B-2015-38720-023", "summary": "The source rounds a cited 97-percent operator recognition probability to one, raising P(D_u) from about 0.776 to 0.8. Its minimum-90-second view claim assumes a full 20-mile diameter crossing and does not cover a marginal target encounter."},
    {"page": 46, "model_id": "MU-B-2015-38720-003", "equation_id": "EQ-B-2015-38720-005", "summary": "The Bayesian B777 interval is arithmetically inconsistent: 6.21463 plus or minus 2(0.246568) gives a lower bound about 5.72149, not 5.57215. The page also describes samples of size 100 although this run used 500 trials and 475 successes."},
    {"page": 47, "model_id": "MU-B-2015-38720-003", "equation_id": "EQ-B-2015-38720-005", "summary": "Uncertain-model means and intervals omit trials not found by 24 hours. Comparing Bayesian 95-percent completion with spiral 80-percent completion through success-conditional intervals does not compare overall time-to-discovery distributions; censoring or restricted-time analysis is required."},
    {"page": 49, "model_id": "MU-B-2015-38720-010", "equation_id": None, "summary": "The C172 discovery probability is produced by linearly scaling rectangular aircraft size from the B777 to 2 percent. No evidence shows radar/debris detectability is proportional to that geometric area, and the reported SD/SE imply a sample count inconsistent with 411 successes."},
    {"page": 1, "model_id": "MU-B-2015-38720-011", "equation_id": None, "summary": "The abstract attributes an average time of about 4.7 hours to the Bayesian method, while the body reports Bayesian mean 6.21463 hours; 4.76078 hours belongs to the uncertain spiral route. The recommendation must use route-labeled result records."},
    {"page": 7, "model_id": "MU-B-2015-38720-011", "equation_id": None, "summary": "The paper dates MH370's departure as March 4, 2014 rather than March 8, and page 6 states that Amelia Earhart fragments were finally found although its cited context remains unresolved. These contextual facts require source verification before reuse."},
    {"page": 56, "model_id": "MU-B-2015-38720-011", "equation_id": None, "summary": "Page 56 visibly ends the sentence 'Furthermore, the Bayesian Solution' before the recommendation, and page 61 labels image references as 8.2 after Section 10. These are genuine source organization/provenance defects rather than extraction clipping."},
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
        raise ValueError("q110 stage paper IDs do not agree")
    if language.get("review_status") != "validated" or len(language.get("units", [])) != 64:
        raise ValueError("G1-G3 language stage must be validated at 64 units")
    if len(language.get("available_chapters", [])) != 16 or len(organization.get("section_contracts", [])) != 16:
        raise ValueError("G4 must retain all 16 normalized chapters and contracts")
    if len(organization.get("paragraph_chains", {}).get("abstract", [])) != 7:
        raise ValueError("abstract chain must retain seven visual paragraphs")
    if len(organization.get("paragraph_chains", {}).get("introduction", [])) != 4:
        raise ValueError("introduction chain must retain four visual paragraphs")
    if models.get("review_status") != "validated" or len(models.get("models", [])) != 11:
        raise ValueError("G5 must retain 11 model units")
    if sum(len(item.get("governing_equations", [])) for item in models["models"]) != 23:
        raise ValueError("G5 must retain all 23 displayed equations")
    if visuals.get("review_status") != "validated" or len(visuals.get("visuals", [])) != 42:
        raise ValueError("G6 must retain 37 figures and five substantive tables")
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
    return {
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out",
        "award_status": "outstanding",
        "source": {
            "relative_path": "2015\u7f8e\u8d5b\u7279\u7b49\u5956/B-38720-Outstanding.pdf",
            "sha256": SHA,
            "page_count": PAGE_COUNT,
            "pdf_page_offset_note": "Physical PDF pages and printed Page n of 61 labels agree one-to-one across pages 1-61.",
        },
        "schema_version": 1,
        "source_quality": {
            "status": "validated",
            "text_pages": PAGE_COUNT,
            "rendered_pages": PAGE_COUNT,
            "visual_review": "complete",
            "notes": [
                "All 61 UTF-8 page-text files were read sequentially, with Summary and Introduction studied before the remaining substantive chapters.",
                "Eighteen one-at-a-time JPEG proxies, each no larger than 450,000 bytes, covered pages 1-61 in three fresh contexts; no original full-page PNG entered model context.",
                "All 23 numbered equations were reconciled by page, all 37 numbered figures and five substantive unnumbered tables have source-ordered dispositions, and no clipping, overlap, blank page, black box, missing glyph, or formula-rendering defect was found.",
                "The text extraction contains mojibake and omits raster equations/captions/table cells; rendered-page review remains the authority for formulas and visuals.",
                "No official 2015 problem-statement manifest row is available, so task reconstruction is bounded to the paper's explicit requests and deliverables.",
            ],
        },
        "context_sources": [
            {"type": "paper", "path": "2015\u7f8e\u8d5b\u7279\u7b49\u5956/B-38720-Outstanding.pdf"},
            {"type": "extraction", "path": f"artifacts/papers/{PAPER_ID}/extraction.json"},
            {"type": "text-pages", "path": f"artifacts/papers/{PAPER_ID}/text/pages"},
            {"type": "visual-stage", "path": "tmp/q110-visual-stage-v1/visuals.json"},
        ],
        "task_reconstruction": {
            "status": "incomplete-official-task-unavailable",
            "inputs": [
                "last-known flight path, speed, altitude, failure-time uncertainty, glide ratio, and aircraft size",
                "open-ocean search geometry and crash-location containment prior",
                "search-aircraft speed, altitude, radar radius, count, and operator performance",
                "route state, time step, random directions, boundary state, and posterior cell probabilities",
                "rescue-time benchmark and communication needs",
            ],
            "outputs": [
                "bounded rectangular search field and containment distribution",
                "random and systematic candidate paths",
                "discovery-time distributions and approximate intervals",
                "Bayesian posterior updates under missed detection",
                "24-hour completion proportions, C172 and two-plane checks",
                "conditional search recommendation and press procedure",
            ],
            "decisions": [
                "how to convert uncertain crash state into a searchable area",
                "where a route should search first under a nonuniform prior",
                "how missed detections change subsequent route priority",
                "how target size and aircraft count affect transfer",
                "which route to recommend when completion and conditional time disagree",
            ],
        },
        "section_map": section_map,
        "assumptions": [
            {"page": 20, "summary": "The lost aircraft follows a straight route, fails within a fixed half-hour window, and glides according to representative speed, altitude, and glide ratio."},
            {"page": 20, "summary": "The search domain is open ocean and is represented as a rectangle around the candidate flight segment."},
            {"page": 20, "summary": "Crash x is uniform and cross-track y follows the selected normal containment model."},
            {"page": 21, "summary": "The P-8 flies at constant speed and ideal trials detect every target inside a fixed 10-mile radius."},
            {"page": 21, "summary": "Weather, fatigue, refueling, turn time, coordination conflicts, currents, debris drift, and sea-state effects are excluded from the path simulations."},
            {"page": 43, "summary": "Uncertain trials use radar success 0.8, round operator recognition from 0.97 to one, and cap runs at 24 hours."},
        ],
        "data_and_preprocessing": [
            {"page": 7, "summary": "Historical missing-aircraft and MH370 context motivates an Atlantic open-ocean case; these sources are contextual rather than a statistical training population."},
            {"page": 13, "summary": "Two notation tables define lost-plane and search-state variables before their equations, although later symbols drift."},
            {"page": 16, "summary": "B777, G450, and C172 specifications are compared; the B777 baseline fixes 640 mph, 35,000 ft, 15:1 glide, r=100 mi, and L=320 mi."},
            {"page": 18, "summary": "P-3 and P-8 specifications are compared; the P-8 baseline fixes 400 mph and a 10-mile sensor radius."},
            {"page": 22, "summary": "The crash sampler generates 5,000 points for prior inspection and separate route experiments use 100 trials under ideal detection."},
            {"page": 43, "summary": "Discovery-uncertainty experiments use 500 trials and retain successful times separately from completion proportions."},
        ],
        "models": [{"model_id": item["model_id"], "page": item["page"], "summary": item["summary"]} for item in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [
            {"page": 22, "section": "containment sampler", "summary": "A 5,000-point scatter visually checks center concentration in the bounded prior.", "verification_type": "simulation input inspection", "strength": "The intended spatial shape is visible.", "limitation": "No distributional goodness-of-fit or parameter disclosure is supplied."},
            {"page": 28, "section": "bounded random", "summary": "Histogram, mean, median, standard deviation, standard error, and approximate interval summarize 100 trials.", "verification_type": "repeated-run summary", "strength": "Skew and variability are exposed.", "limitation": "No seed, convergence, raw output, or field comparator is supplied."},
            {"page": 37, "section": "ideal systematic routes", "summary": "Descending, spiral, and sinusoidal routes are compared under one containment/detection harness.", "verification_type": "within-model baseline comparison", "strength": "A common ideal scenario isolates route-order differences.", "limitation": "Turn dynamics and implementation ambiguities remain shared or route-specific."},
            {"page": 46, "section": "imperfect discovery", "summary": "Bayesian and fixed spiral routes report 500-trial completion counts and conditional time distributions.", "verification_type": "scenario comparison with cap", "strength": "Failure proportions become visible.", "limitation": "Conditional intervals do not compare the complete censored distributions."},
            {"page": 49, "section": "Cessna stability", "summary": "A smaller aircraft and search region test a limited target-transfer scenario.", "verification_type": "scenario transfer check", "strength": "Target size is not ignored.", "limitation": "Detection is linearly scaled by aircraft area without calibration."},
            {"page": 51, "section": "two-plane stability", "summary": "A two-plane striped route tests one resource extension.", "verification_type": "resource scenario", "strength": "Aircraft count reaches the decision layer.", "limitation": "No coordination, separation, staging, or refueling model is tested."},
        ],
        "results_trace": [
            {"page": 28, "summary": "Bounded random: 100 trials, median 24.425 h, mean 42.7105 h, interval [33.2348,52.1862]."},
            {"page": 31, "summary": "Weighted bounded random: median 16.6 h, mean 37.5575 h, interval [26.4795,48.6755]; overlap is descriptive, not a formal test."},
            {"page": 34, "summary": "Descending stripes: median 7.031 h and mean 7.10273 h."},
            {"page": 37, "summary": "Ideal spiral stripes: median 3.113 h and mean 3.62286 h, the best one-plane ideal-detection result."},
            {"page": 40, "summary": "Sinusoidal route: median 4.489 h and mean 6.44989 h."},
            {"page": 46, "summary": "Bayesian B777: 475/500 found, median 4.05 h and success-conditional mean 6.21463 h."},
            {"page": 47, "summary": "Uncertain spiral B777: 399/500 found, median 4.05 h and success-conditional mean 4.76078 h."},
            {"page": 49, "summary": "Bayesian C172: 411/500 found, median 6.435 h and success-conditional mean 8.38549 h."},
            {"page": 52, "summary": "Two-plane stripes: 100 trials, median 2.1435 h and mean 2.39551 h."},
            {"page": 56, "summary": "The paper recommends normal containment with discovery uncertainty and a Bayesian-adjusted route, prioritizing higher completion despite conditional-time tradeoffs."},
        ],
        "contributions": [
            {"page": 11, "summary": "Containment and detection are separated conceptually before route design."},
            {"page": 15, "summary": "Aircraft state is converted into an explicit bounded search geometry."},
            {"page": 22, "summary": "One crash sampler and statistical harness support a route-learning ladder from weak random baselines to center-first systematic paths."},
            {"page": 35, "summary": "Alternating spiral stripes align route order with the cross-track prior rather than only enforcing geometric coverage."},
            {"page": 42, "summary": "Missed detections update searched and unsearched cell probabilities, linking sensing uncertainty to adaptive route choice."},
            {"page": 49, "summary": "Target-size and aircraft-count scenarios probe two practical transfer axes."},
            {"page": 58, "summary": "A separate press document translates the modeled procedure into stakeholder-facing operations."},
        ],
        "writing_logic": [{"page": c["pages"][0], "summary": f"{c['chapter']}: {c['rhetorical_job']} {c['handoff']}"} for c in organization["section_contracts"]],
        "language_observations": [{"page": c["pages"][0], "summary": f"{c['chapter']}: {c['input']} -> {c['output']}"} for c in organization["section_contracts"]],
        "visualization_observations": visual_records,
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The Summary routes urgency through geometry, simulation, uncertainty, transfer, and recommendation with explicit numbers; award status does not establish which move caused judging success.", "evidence_class": "J"},
            {"page": 53, "summary": "Shared-scale comparison plots make route tradeoffs scannable, while their statistical interpretation remains bounded.", "evidence_class": "J"},
            {"page": 58, "summary": "The press document closes the technical-to-stakeholder loop without proving operational deployment readiness.", "evidence_class": "J"},
        ],
        "weaknesses": [dict(item) for item in WARNINGS],
        "independent_extensions": [
            {"extension_id": "E-B-38720-001", "page": 15, "summary": "Replace the rectangle with a probabilistic reachable set using failure time, aircraft dynamics, winds, currents, and navigation uncertainty."},
            {"extension_id": "E-B-38720-002", "page": 23, "summary": "Publish a deterministic simulation contract with coordinate system, time step, norm, boundary precedence, route state machine, seeds, and raw trials."},
            {"extension_id": "E-B-38720-003", "page": 35, "summary": "Define stripe coordinates in physical units and optimize path order with turn cost, sensor footprint, posterior mass, and route feasibility."},
            {"extension_id": "E-B-38720-004", "page": 42, "summary": "Calibrate a cell-level observation likelihood by target, debris, radar, altitude, operator, sea state, weather, and dwell time."},
            {"extension_id": "E-B-38720-005", "page": 46, "summary": "Analyze capped trials with survival curves, restricted mean discovery time, completion probability, paired seeds, and uncertainty rather than success-only intervals."},
            {"extension_id": "E-B-38720-006", "page": 49, "summary": "Validate target-size transfer with sensor-signature experiments rather than linear geometric-area scaling."},
            {"extension_id": "E-B-38720-007", "page": 51, "summary": "Formulate multi-aircraft posterior coverage with staging, separation, turns, fuel, communication, overlap, and dynamic reassignment."},
        ],
        "candidate_rule_impacts": [],
        "unresolved_questions": [item["summary"] for item in WARNINGS],
        "protocol_v2_records": {},
        "review_status": "validated",
    }


def make_observations(template, language: dict, models: dict, card: dict) -> list[dict]:
    observations = template.make_observations(language, models, card)
    interpretations = {
        "language": "Reuse the rhetorical mechanism only after replacing incident, aircraft, sensor, prior, route, statistic, evidence, and audience entities.",
        "modeling": "Retain search geometry, containment, path state, sensor rule, posterior update, stopping/censoring, scenario, and handoff terms together.",
        "logic": "Preserve the positive urgency-to-context-to-geometry-to-route-ladder-to-uncertainty-to-stability-to-recommendation chain before warnings.",
        "visualization": "Keep route identity, geometry, axes, units, trial denominator, failure handling, uncertainty, source status, and supported claim together.",
        "verification": "Name the exact sampler, route comparator, repeated-run distribution, capped completion check, transfer scenario, or decision trace.",
        "data": "Retain source, aircraft class, units, prior support, sensor setting, trial count, cap, transformation, and downstream consumer.",
        "assumption": "Pair each motion, containment, sensing, environment, resource, or statistical assumption with its enabled computation and excluded regime.",
        "result": "Keep route, target, aircraft count, trial denominator, found count, conditionality, median, mean, spread, interval, and decision distinct.",
        "weakness": "Record notation, unit, algorithm, statistics, calibration, fact, organization, and provenance risks only after positive G1-G6 learning.",
        "other": "Separate cited context, visible source evidence, extracted text, executable implementation, simulation output, and field validation.",
    }
    provenance = [
        (59, "references", "References identify incident, aircraft, radar, operator, and survival context but do not freeze every external source byte."),
        (7, "MH370 context", "The reproduced search map motivates geometry but is not the data-generating basis of the paper's rectangle."),
        (8, "missing-aircraft context", "The infographic motivates domain choice but does not establish a representative population."),
        (13, "notation provenance", "Variable tables establish intended symbols while later equations expose symbol drift and missing units."),
        (16, "aircraft specifications", "Aircraft values support scenarios but the exact extraction and conversion chain is not archived."),
        (18, "sensor specifications", "P-8 speed and range are selected from cited context without a calibrated debris-detection curve."),
        (22, "crash sampler", "The 5,000-point visual checks shape but raw coordinates, distribution parameters, and seed are absent."),
        (28, "route trials", "Histograms expose 100-trial outputs while code, time step, and raw completion times remain absent."),
        (43, "operator evidence", "A cited 97-percent recognition rate is rounded to one and not preserved as a full likelihood model."),
        (46, "Bayesian trials", "Completion count and conditional times are reported without censored raw records."),
        (49, "C172 transfer", "Target-size transfer is scenario evidence under a geometric scaling assumption, not radar calibration."),
        (51, "two-plane transfer", "The resource extension shows simulated benefit without an operational coordination model."),
        (53, "comparison plots", "Approximate interval plots support descriptive comparison but not the stated significance logic."),
        (56, "survival context", "The external cold-water curve supplies urgency but is not integrated as a calibrated objective."),
        (58, "press communication", "The stakeholder artifact reuses the recommendation and adds no technical validation."),
        (61, "image references", "Image-source numbering is structurally inconsistent and licensing/source bytes are not frozen."),
    ]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = ["Apply only when geometry, coordinates, target, sensor, prior, route state, trial design, censoring, units, uncertainty, and receiving decision are explicit."]
        row["counterevidence"] = ["A selected path, one trace, simulation histogram, interval overlap, completion proportion, contextual figure, or press recommendation does not prove field calibration, significance, causal superiority, or universal transfer."]
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
        ("R-B-LANG-001", "retain urgency-to-model, assumption-to-mechanism, route-to-result, uncertainty-to-decision, strength-to-boundary, and stakeholder-procedure routines with typed slots", first["language"]),
        ("R-B-LOG-001", "trace crash state through geometry, containment, baseline failures, systematic path repairs, missed-detection updates, stability checks, recommendation, and public action", first["logic"]),
        ("R-B-DATA-001", "version aircraft and sensor specifications, coordinate system, distribution parameters, trial design, time cap, raw outcomes, and external context", first["data"]),
        ("R-B-DATA-002", "maintain assumptions for motion, glide, rectangularization, containment, ideal and uncertain detection, weather, turns, fatigue, coordination, and censoring", evidence("R-B-DATA-002")),
        ("R-B-MOD-001", "retain probability factorization, search geometry, common harness, four random/systematic path families, Bayesian update, scenario stability, and recommendation interfaces", first["modeling"]),
        ("R-B-MOD-003", "combine spatial prior, path geometry, sensor likelihood, posterior update, resource state, and rescue decision only through typed coordinate, unit, probability, and time contracts", evidence("R-B-MOD-003")),
        ("R-B-MOD-004", "keep found count, completion proportion, conditional time, median, mean, spread, interval, route, target, resource case, and decision distinct", first["result"]),
        ("R-B-MOD-005", "stress boundary logic, stripe scale, vector transitions, detection calibration, grid resolution, trial cap, interval arithmetic, target scaling, and multi-aircraft coordination", evidence("R-B-MOD-005")),
        ("R-B-VER-002", "make every reliability claim sampler-, equation-, route-, trial-, completion-, censoring-, transfer-, figure-, and decision-trace-specific", first["verification"]),
        ("R-B-VER-004", "reconcile missing norm, v/v_s, union-as-OR, stripe units, malformed vector update, interval misuse, censored means, result mismatch, source facts, and section numbering", first["weakness"]),
        ("R-B-VIZ-001", "retain maps, notation/specification tables, priors, vector rules, path traces, histograms, posterior maps, interval comparisons, and survival context with source and uncertainty boundaries", first["visualization"]),
        ("R-B-COMP-001", "measure sampler generation, time steps, boundary correction, posterior-grid updates, route coverage, Monte Carlo trials, censored analysis, scenario transfer, and coordination cost separately", evidence("R-B-COMP-001")),
    ]
    card["candidate_rule_impacts"] = [{"rule_id": rule_id, "action": action, "evidence_ids": [observation_id]} for rule_id, action, observation_id in entries]


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
    audit["language_unit_dispositions"] = [{"language_unit_id": unit["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": unit["candidate_pattern_ids"], "reason": "The rhetorical mechanism transfers only after replacing incident, aircraft, sensor, prior, route, statistic, evidence, and audience entities."} for unit in language["units"]]
    argument_metadata = {
        "search-field construction": {"claim": "Aircraft state, failure-time uncertainty, glide geometry, and a nonuniform prior turn the open ocean into a bounded probability field.", "source_pages": [7, 11, 13, 15, 16, 17, 18, 22]},
        "path-learning ladder": {"claim": "Successive baselines expose boundary and probability-order failures, leading to center-first systematic coverage under ideal detection.", "source_pages": [24, 26, 29, 32, 35, 38, 40]},
        "realism-to-recommendation": {"claim": "Missed-detection Bayesian updates trade a higher success-conditional mean for materially greater 24-hour completion than a fixed spiral route.", "source_pages": [41, 42, 43, 44, 45, 46, 47, 53, 54, 56]},
        "rescue-and-scope loop": {"claim": "Target/resource checks and the survival benchmark bound the recommendation as an adaptable modeled procedure rather than a field guarantee.", "source_pages": [49, 50, 51, 52, 55, 56, 57, 58]},
    }
    chains = []
    for chain in organization["main_argument_chains"]:
        metadata = argument_metadata[chain["name"]]
        chains.append({"claim": metadata["claim"], "support_steps": chain["chain"], "decision_consequence": chain["decision"], "source_pages": metadata["source_pages"]})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": organization["global_progression"] + ["Only after the positive language, organization, model, and visual chain is complete does G7 record notation, statistics, calibration, fact, and provenance warnings."],
        "section_progressions": [{"chapter": c["chapter"], "moves": [f"input: {c['input']}", f"rhetorical job: {c['rhetorical_job']}", f"analytical job: {c['analytical_job']}", f"output: {c['output']}", f"handoff: {c['handoff']}"], "positive_pattern": "Use the source-anchored input -> rhetorical job -> analytical job -> output -> handoff contract; warnings remain a last pass."} for c in organization["section_contracts"]],
        "main_argument_chains": chains,
    }
    audit["formula_error_watch"] = {
        "mode": "last-pass-warning-only",
        "completed_after_positive_passes": True,
        "warnings": [{"model_id": w["model_id"], "equation_id": w["equation_id"], "page": w["page"], "warning": w["summary"]} for w in WARNINGS if w["equation_id"] is not None],
    }
    model_ids = [item["model_id"] for item in models["models"]]
    equation_ids = [eq["equation_id"] for item in models["models"] for eq in item["governing_equations"]]
    audit["model_retention"] = {
        "model_count": len(model_ids),
        "retained_model_ids": model_ids,
        "retained_equation_ids": equation_ids,
        "central_equations": [{"model_id": item["model_id"], "equation_ids": [eq["equation_id"] for eq in item["governing_equations"]], "all_central_equations_retained": True} for item in models["models"] if item["governing_equations"]],
    }
    audit["visualization_dispositions"] = [{"paper_card_visual_index": item["paper_card_visual_index"], "visual_record_id": item["visual_record_id"], "disposition": item["disposition"], "analytical_purpose": item["analytical_purpose"]} for item in visuals["visuals"]]
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
        raise ValueError("q110 extraction identity or page count does not match the current paper")

    template = load_module(ROOT / "scripts/build_q100_artifacts.py", "q100_template_for_q110")
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
            "All 61 physical pages were inspected through 18 one-at-a-time JPEG proxies of at most 450,000 bytes in three fresh contexts. No clipping, overlap, blank page, black box, missing glyph, or formula-rendering failure was found.",
            "Figures 1-37, five substantive unnumbered tables, and Equations 1-23 were reconciled by source page. Focused formula review returned text only; no original full-page PNG entered model context.",
            "Source defects retained separately include the incomplete sentence on page 56 and the duplicate 8.2 image-reference heading on page 61.",
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

    print(json.dumps({"paper_id": PAPER_ID, "stage": str(STAGE), "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "models": len(models["models"]), "equations": 23, "visuals": len(visuals["visuals"]), "observations": len(observations), "warnings": len(WARNINGS), "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
