from __future__ import annotations

"""Assemble create-only Queue 111 G7-G8 learning artifacts."""

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-39173-b8260835"
SHORT = "39173"
SHA = "b82608352dbbe043cd7092dabcaea179ff110677e0a4598d1f78ad33f956b813"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 32
STAGE = ROOT / "tmp/q111-stage-v2"
LANGUAGE_PATH = ROOT / "tmp/q111-language-stage-v2/language.json"
ORGANIZATION_PATH = ROOT / "tmp/q111-organization-stage-v1/organization.json"
MODELS_PATH = ROOT / "tmp/q111-model-stage-v1/models.json"
VISUALS_PATH = ROOT / "tmp/q111-visual-stage-v1/visuals.json"
EXTRACTION_PATH = ROOT / f"artifacts/papers/{PAPER_ID}/extraction.json"


WARNINGS = [
    {"page": 5, "model_id": "MU-B-2015-39173-001", "equation_id": "EQ-B-2015-39173-005", "summary": "The printed CDF derivation retains squared terms and dy_C in its alleged antiderivative. Preserve the source form as evidence only and re-derive the integral before numeric reuse."},
    {"page": 5, "model_id": "MU-B-2015-39173-001", "equation_id": "EQ-B-2015-39173-006", "summary": "The translated impact variable Y_I=Y_C+Gh should shift both support limits, but the printed upper support remains y_B-y_R rather than y_B-y_R+Gh."},
    {"page": 6, "model_id": "MU-B-2015-39173-002", "equation_id": "EQ-B-2015-39173-010", "summary": "The joint density inherits the impact-density support inconsistency, so its normalization and every downstream regional integral require a corrected support audit."},
    {"page": 9, "model_id": "MU-B-2015-39173-004", "equation_id": "EQ-B-2015-39173-013", "summary": "The printed indexed x inequality is not an unambiguous lower-and-upper cell-bound contract; the role and sign of l must be made explicit before generating corners."},
    {"page": 9, "model_id": "MU-B-2015-39173-004", "equation_id": "EQ-B-2015-39173-014", "summary": "The printed y bound uses y_B-y_0-Gh and does not clearly preserve the earlier radar-horizon and impact-support terms, creating a geometry mismatch between density, partition, and coordinates."},
    {"page": 9, "model_id": "MU-B-2015-39173-004", "equation_id": "EQ-B-2015-39173-021", "summary": "rho is described as miles per degree but is multiplied in C_L=rho R C+y_0. A miles-to-degrees transform normally requires the reciprocal convention, so units and direction must be reconciled."},
    {"page": 11, "model_id": "MU-B-2015-39173-006", "equation_id": "EQ-B-2015-39173-029", "summary": "Multiplying the searched-cell POC by 1-POD is a likelihood step, but the subsequent uniform mass redistribution is a mass-conserving heuristic rather than a normalized Bayesian posterior conditioned on nondetection."},
    {"page": 11, "model_id": "MU-B-2015-39173-007", "equation_id": None, "summary": "Selecting the largest updated adjacent POC reduces some travel relative to unrestricted probability chasing, but no global time, fuel, coverage, or detection-optimality proof is supplied."},
    {"page": 13, "model_id": "MU-B-2015-39173-008", "equation_id": None, "summary": "Separate one-at-a-time curves for G and theta do not establish the prose claim about the combined quantity G+theta; joint interactions and parameter domains are not tested."},
    {"page": 14, "model_id": "MU-B-2015-39173-008", "equation_id": None, "summary": "The altitude discussion refers to Figure 4 while the relevant plot is Figure 7, so figure-to-claim traceability is broken at the point of sensitivity interpretation."},
    {"page": 14, "model_id": "MU-B-2015-39173-008", "equation_id": None, "summary": "The prose says POD increases with search altitude, but the plotted curve and square-root detector term decrease as altitude approaches effective instrument reach; the later low-altitude recommendation contradicts the first sentence."},
    {"page": 15, "model_id": "MU-B-2015-39173-008", "equation_id": None, "summary": "Figure 8 varies search-plane count n but its caption labels the curve POD(h_s), so the displayed independent variable must be recovered from axes and surrounding prose."},
    {"page": 17, "model_id": "MU-B-2015-39173-009", "equation_id": "EQ-B-2015-39173-032", "summary": "Flight ABCD's numerical impact-density center and support do not transparently follow the general Y_I=Y_C+Gh translation, and no normalization or substitution audit is shown."},
    {"page": 19, "model_id": "MU-B-2015-39173-010", "equation_id": "EQ-B-2015-39173-035", "summary": "The methodology defines the condition factor as kappa, but the worked-example and Appendix C POD expression use k; the executable code must bind one symbol explicitly."},
    {"page": 25, "model_id": "MU-B-2015-39173-003", "equation_id": "EQ-B-2015-39173-012", "summary": "Appendix A integrates y_I from zero-based partition bounds and does not visibly add the Gh offset used by the impact variable, so its 36 POC values may not represent the declared density support."},
    {"page": 28, "model_id": "MU-B-2015-39173-006", "equation_id": "EQ-B-2015-39173-030", "summary": "Appendices C and D apply Ceiling to a probability-matrix redistribution term. Integer rounding is incompatible with fractional POC conservation and may collapse or inflate the update."},
    {"page": 28, "model_id": "MU-B-2015-39173-007", "equation_id": None, "summary": "The Mathematica While conditions are separated by semicolons, and local 3x3 minima are matched through a global Position call. Loop termination, index safety, and selected-cell locality are not executable without clarification."},
    {"page": 27, "model_id": "MU-B-2015-39173-007", "equation_id": None, "summary": "Appendix C is introduced as the neighborhood algorithm in the body but its page-28 heading says the loop is without adjacency, conflicting with the local 3x3 selection intended to distinguish it from Appendix D."},
    {"page": 23, "model_id": "MU-B-2015-39173-011", "equation_id": None, "summary": "The conclusion claims applicability to all aircraft and search-plane types from one hypothetical Boeing 777 scenario with uncalibrated sensing and no field comparator."},
    {"page": 24, "model_id": "MU-B-2015-39173-011", "equation_id": None, "summary": "Claims that the plan is valid, maximizes resources, is a breakthrough, and will be implemented are not supported by optimization certificates, calibrated data, field validation, or deployment evidence."},
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
        raise ValueError("q111 stage paper IDs do not agree")
    if language.get("review_status") != "validated" or len(language.get("units", [])) != 68:
        raise ValueError("G1-G3 language stage must be validated at 68 units")
    if len(language.get("available_chapters", [])) != 17 or len(organization.get("section_contracts", [])) != 17:
        raise ValueError("G4 must retain all 17 normalized chapters and contracts")
    if len(organization.get("paragraph_chains", {}).get("abstract", [])) != 3:
        raise ValueError("abstract chain must retain three visual paragraphs")
    if len(organization.get("paragraph_chains", {}).get("introduction", [])) != 3:
        raise ValueError("introduction chain must retain three visual paragraphs")
    if models.get("review_status") != "validated" or len(models.get("models", [])) != 11:
        raise ValueError("G5 must retain 11 model units")
    if sum(len(item.get("governing_equations", [])) for item in models["models"]) != 37:
        raise ValueError("G5 must retain all 37 displayed equations or equation families")
    if len(models.get("dependency_edges", [])) != 15:
        raise ValueError("G5 must retain 15 dependency edges")
    if visuals.get("review_status") != "validated" or len(visuals.get("visuals", [])) != 17:
        raise ValueError("G6 must retain 13 figures and four substantive tables")
    safety = visuals.get("transport_safety", {})
    if safety.get("total_bounded_jpeg_proxies") != 8 or safety.get("total_proxy_bytes") != 1367613:
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
    return {
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "Searching for a Lost Plane",
        "award_status": "outstanding",
        "source": {
            "relative_path": "2015\u7f8e\u8d5b\u7279\u7b49\u5956/B-39173-Outstanding.pdf",
            "sha256": SHA,
            "page_count": PAGE_COUNT,
            "pdf_page_offset_note": "Physical PDF pages and printed Page n of 32 labels agree one-to-one across pages 1-32.",
        },
        "schema_version": 1,
        "source_quality": {
            "status": "validated",
            "text_pages": PAGE_COUNT,
            "rendered_pages": PAGE_COUNT,
            "visual_review": "complete",
            "notes": [
                "All 32 UTF-8 page-text files were read sequentially, including all references, Appendix A-D code, and printed outputs.",
                "Eight one-at-a-time byte-bounded JPEG proxies totaling 1,367,613 bytes covered pages 1-32 and focused formula, coordinate, update, and sensitivity regions; no original full-page PNG entered model context.",
                "All 37 displayed equations or equation families, Figures 1-13, and four substantive unnumbered tables have source-ordered retention and dispositions.",
                "No clipping, overlap, missing page, blank page, black box, or formula-rendering failure was found; source notation and algorithm defects are retained as last-pass warnings rather than mistaken for rendering defects.",
                "No official 2015 problem-statement manifest row is available, so task reconstruction is bounded to the paper's explicit search-and-rescue objectives and outputs.",
            ],
        },
        "context_sources": [
            {"type": "paper", "path": "2015\u7f8e\u8d5b\u7279\u7b49\u5956/B-39173-Outstanding.pdf"},
            {"type": "extraction", "path": f"artifacts/papers/{PAPER_ID}/extraction.json"},
            {"type": "text-pages", "path": f"artifacts/papers/{PAPER_ID}/text/pages"},
            {"type": "visual-stage", "path": "tmp/q111-visual-stage-v1/visuals.json"},
        ],
        "task_reconstruction": {
            "status": "incomplete-official-task-unavailable",
            "inputs": [
                "last communication, intended flight path, destination radar boundary, aircraft speed, altitude, and glide ratio",
                "possible cross-track deviation and a sparse incident prior",
                "search-aircraft speed, altitude, sensor reach, condition factor, count, and half-hour traversal target",
                "cell geometry, current POC matrix, cell-specific POD, searched-cell identity, and neighborhood state",
                "latitude-longitude endpoints, local flight-vector components, references, and computational appendices",
            ],
            "outputs": [
                "continuous casualty, impact-distance, cross-track, and joint containment densities",
                "an N by 6 regional POC matrix and geographic cell corners",
                "region-level POD and a nondetection update",
                "adjacent and unrestricted search sequences",
                "Flight ABCD probability surfaces, grid/map, path comparison, and public summary",
            ],
            "decisions": [
                "how to bound a sparse-evidence transoceanic search region",
                "how to convert continuous probability into timed operational cells",
                "how search assets and conditions affect detection feasibility",
                "which neighboring cell to search after a miss and when to revisit",
                "how to communicate the conditional recommendation without overstating validation",
            ],
        },
        "section_map": section_map,
        "assumptions": [
            {"page": 12, "summary": "The missing aircraft follows a linear pre-established route from A to B."},
            {"page": 12, "summary": "The aircraft glides into the ocean and does not explode before water impact."},
            {"page": 12, "summary": "Debris separates upon water impact."},
            {"page": 12, "summary": "Cross-track deviation remains within three times Gh sin(pi/8)."},
            {"page": 12, "summary": "Currents and other forces do not move the aircraft or debris after impact."},
            {"page": 12, "summary": "Lost and search aircraft maintain constant velocities."},
            {"page": 12, "summary": "The aircraft is more likely to lie near the last communication point."},
            {"page": 12, "summary": "The aircraft remains afloat and detectable throughout the search."},
            {"page": 12, "summary": "All search aircraft share instrumentation, speed, and altitude."},
        ],
        "data_and_preprocessing": [
            {"page": 2, "summary": "Missing-aircraft counts and Air France/MH370 narratives motivate the sparse-evidence domain but are not a calibrated incident population."},
            {"page": 4, "summary": "Last-contact distance, remaining route, coastal radar geometry, altitude, and glide ratio are converted into along-track variables."},
            {"page": 6, "summary": "A fixed pi/8 deviation scale and independence assumption extend the along-track distribution into a joint surface."},
            {"page": 7, "summary": "Search speed and a 0.5-hour traversal target determine N; three cross-track sigma bands on either side produce an N by 6 grid."},
            {"page": 9, "summary": "Cell indices, endpoint coordinates, flight-vector components, rotation, and a mile-degree factor feed the geographic handoff."},
            {"page": 10, "summary": "Sensor range, weather-condition factor, search altitude, swath distance, and aircraft count parameterize POD."},
            {"page": 17, "summary": "Flight ABCD fixes Boston-Lisbon geometry, last contact at 40.9275 N and 46.2575 W, y_B=1912 miles, speed 560 mph, altitude 7.58 miles, y_R=199.86, and G=19."},
            {"page": 20, "summary": "The worked search uses v_s=550 mph, t_0.5=0.5 h, epsilon=4 miles, kappa=0.98, h_s=2000/5280 miles, and n=8 aircraft."},
        ],
        "models": [{"model_id": item["model_id"], "page": item["page"], "summary": item["summary"]} for item in models["models"]],
        "dependency_graph": models["dependency_edges"],
        "verification": [
            {"page": 6, "section": "containment geometry", "summary": "Figure 1 connects the pi/8 deviation assumption to the cross-track standard deviation.", "verification_type": "geometric interpretation", "strength": "The source makes the intended triangle-to-band relation visible.", "limitation": "The angle and normal law are assumed rather than estimated."},
            {"page": 7, "section": "cell discretization", "summary": "Figure 2 makes the N by 6 grid and half-hour along-track interpretation inspectable.", "verification_type": "algorithm schematic", "strength": "Continuous-to-cell handoff is explicit.", "limitation": "No resolution sensitivity or traversal optimization is reported."},
            {"page": 9, "section": "coordinate transform", "summary": "Figure 3, det(R)=1, and Appendix B tables trace one local cell to geographic corners.", "verification_type": "transform trace", "strength": "The operational coordinate handoff is not left implicit.", "limitation": "Unit direction, sign conventions, and exact corner bounds remain ambiguous."},
            {"page": 13, "section": "sensitivity", "summary": "Figures 4-8 vary G, theta, search altitude, and aircraft count around the worked-example settings.", "verification_type": "one-at-a-time parameter response", "strength": "Direction and a sensor feasibility boundary are visible.", "limitation": "There are no joint interactions, uncertainty ranges, quantitative robustness metrics, or calibration data."},
            {"page": 18, "section": "Flight ABCD containment", "summary": "Figures 9-11 expose the instantiated joint density, discretized POC, and mapped 36-cell field.", "verification_type": "worked-example trace", "strength": "The model reaches an inspectable spatial result.", "limitation": "No normalization check, raw integration audit, or independent implementation is supplied."},
            {"page": 21, "section": "path comparison", "summary": "Figures 12-13 compare neighborhood and unrestricted sequences under the same symmetric POC surface.", "verification_type": "within-model visual comparator", "strength": "Back-and-forth movement caused by unrestricted selection is visible.", "limitation": "No distance, time, fuel, coverage, or detection totals quantify superiority."},
            {"page": 25, "section": "appendix reproduction", "summary": "Mathematica and Excel artifacts expose regional integration, coordinate inputs, POD, update loops, tie handling, and printed sequences.", "verification_type": "partial computational provenance", "strength": "Key interfaces and outputs can be audited against the prose.", "limitation": "The archive lacks an executable environment, exact files, assertions, and ambiguity-free code."},
        ],
        "results_trace": [
            {"page": 17, "summary": "Flight ABCD sets y_B=1912 miles, speed 560 mph, altitude 7.58 miles, y_R=199.86 miles, and glide ratio G=19 from the Boston-Lisbon scenario."},
            {"page": 17, "summary": "The source prints casualty support 0<=y_C<1712.14 and impact support 144.02<=y_I<1712.14, with the latter retained as a flagged transformation boundary."},
            {"page": 18, "summary": "The instantiated joint surface is integrated into 36 search regions (N=6 along-track by six cross-track bands)."},
            {"page": 19, "summary": "Figures 10-11 present the numerical POC grid and map; Appendix C begins with symmetric near-track values including 0.13367 in the first along-track band."},
            {"page": 20, "summary": "With v_s=550, epsilon=4, kappa=0.98, h_s=2000/5280, and eight search aircraft, the paper reports POD=0.677831."},
            {"page": 21, "summary": "The neighborhood algorithm produces a locally adjacent sequence and allows revisits after nondetection updates."},
            {"page": 22, "summary": "The unrestricted comparator visibly alternates across the symmetric IFP more often; the paper reports greater travel qualitatively but supplies no distance or fuel total."},
            {"page": 22, "summary": "For the sigma,N=2-to-3 region, the source reports phi=-0.057939 and a displayed 2 by 2 rotation with coefficients about 0.9983 and 0.0579 before listing geographic corners."},
            {"page": 23, "summary": "The conclusion recommends the neighborhood method with careful resource selection and more aircraft, while retaining currents and debris motion as future work."},
            {"page": 24, "summary": "The press summary translates POC, POD, missed-detection revisits, neighborhood movement, and straight-route restrictions into public chronology."},
        ],
        "contributions": [
            {"page": 3, "summary": "Containment, detection, and miss-driven updating are separated before formulas, preserving distinct probability roles."},
            {"page": 4, "summary": "Last contact, radar horizon, and glide translate sparse flight evidence into a bounded along-track distribution."},
            {"page": 6, "summary": "Cross-track uncertainty and discretization convert a continuous surface into half-hour operational cells."},
            {"page": 9, "summary": "A rotation-and-translation interface connects local probability cells to latitude-longitude deployment coordinates."},
            {"page": 10, "summary": "The POD layer exposes sensor reach, conditions, altitude, swath distance, and fleet size as decision parameters."},
            {"page": 11, "summary": "Nondetection retains residual probability and enables revisits rather than treating a searched cell as empty."},
            {"page": 21, "summary": "The worked example compares travel-aware neighborhood selection with unrestricted probability chasing."},
            {"page": 23, "summary": "A public summary carries the technical sequence and restrictions into stakeholder communication."},
        ],
        "writing_logic": [{"page": c["pages"][0], "summary": f"{c['chapter']}: {c['rhetorical_job']} {c['handoff']}"} for c in organization["section_contracts"]],
        "language_observations": [{"page": c["pages"][0], "summary": f"{c['chapter']}: {c['input']} -> {c['output']}"} for c in organization["section_contracts"]],
        "visualization_observations": visual_records,
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The abstract previews containment, detection, updating, sensitivity, worked example, and strengths as one operational chain; award status does not prove which move caused judging success.", "evidence_class": "J"},
            {"page": 19, "summary": "A density-to-grid-to-map sequence lets a judge inspect how probability becomes an actionable region rather than only seeing formulas.", "evidence_class": "J"},
            {"page": 21, "summary": "Side-by-side path figures make the intended travel-efficiency contrast scannable even though quantitative optimality is unproved.", "evidence_class": "J"},
            {"page": 23, "summary": "The press-conference section closes the technical-to-public loop while still exposing restrictions.", "evidence_class": "J"},
        ],
        "weaknesses": [dict(item) for item in WARNINGS],
        "independent_extensions": [
            {"extension_id": "E-B-39173-001", "page": 4, "summary": "Estimate casualty timing and reachable impact sets from flight telemetry, route phase, failure modes, winds, aircraft dynamics, and calibrated uncertainty rather than an intuitive quadratic prior."},
            {"extension_id": "E-B-39173-002", "page": 6, "summary": "Fit cross-track deviation and dependence from incident or simulator data, then normalize the corrected joint density on a geodesic support."},
            {"extension_id": "E-B-39173-003", "page": 7, "summary": "Choose adaptive cells by probability mass, sensor footprint, turn cost, terrain/ocean constraints, and computation instead of a fixed half-hour N by 6 grid."},
            {"extension_id": "E-B-39173-004", "page": 9, "summary": "Replace the local flat rotation with a documented geodesic coordinate library, typed miles/degrees units, corner tests, and round-trip validation."},
            {"extension_id": "E-B-39173-005", "page": 10, "summary": "Calibrate the observation likelihood using aircraft/debris signature, sea state, weather, altitude, sensor mode, dwell time, operator performance, and false alarms."},
            {"extension_id": "E-B-39173-006", "page": 11, "summary": "Use a normalized Bayesian filter for missed detections and propagate spatial drift through currents, debris separation, and time-varying detectability."},
            {"extension_id": "E-B-39173-007", "page": 11, "summary": "Optimize multi-aircraft routes over posterior mass, travel, turns, fuel, refueling, separation, coordination, revisit value, and stopping criteria; compare against the greedy neighborhood rule."},
            {"extension_id": "E-B-39173-008", "page": 25, "summary": "Publish a deterministic reproduction package with corrected formulas, exact cell matrix, Mathematica/Excel versions, seeds, tests, raw paths, travel totals, and coordinate fixtures."},
        ],
        "candidate_rule_impacts": [],
        "unresolved_questions": [item["summary"] for item in WARNINGS],
        "protocol_v2_records": {},
        "review_status": "validated",
    }


def make_observations(template, language: dict, models: dict, card: dict) -> list[dict]:
    observations = template.make_observations(language, models, card)
    interpretations = {
        "language": "Reuse the rhetorical mechanism only after replacing incident, aircraft, route, prior, cell, sensor, update, statistic, resource, and audience entities.",
        "modeling": "Retain containment support, coordinate and unit contracts, discretization, sensor likelihood, miss update, path state, stopping rule, and decision handoff together.",
        "logic": "Preserve the positive sparse-evidence-to-containment-to-cells-to-detection-to-update-to-path-to-example-to-public-action chain before warnings.",
        "visualization": "Keep figure identity, axes, units, cell indexing, parameter values, algorithm variant, source defect, and exact supported claim together.",
        "verification": "Name the exact geometry check, grid construction, transform trace, sensitivity curve, worked example, path comparator, or appendix interface.",
        "data": "Retain source, coordinates, units, aircraft/search platform, condition, parameter transformation, version, and downstream consumer.",
        "assumption": "Pair each route, motion, deviation, debris, current, speed, detectability, or fleet assumption with its enabled computation and excluded regime.",
        "result": "Keep scenario, support, N, cell probability, POD, fleet, path variant, coordinate transform, qualitative comparison, and recommendation distinct.",
        "weakness": "Record algebra, support, unit, update, caption, sensitivity, implementation, validation, and scope risks only after positive G1-G6 learning.",
        "other": "Separate cited context, visual source evidence, extracted text, mathematical intent, executable behavior, worked output, and field validation.",
    }
    provenance = [
        (25, "references", "Six references identify glide, search theory, radar, missing-aircraft, and MH370 context but do not freeze external bytes or calibration datasets."),
        (2, "missing-aircraft context", "The 83-aircraft count motivates the domain without defining a representative casualty-time distribution."),
        (2, "Air France comparator", "Air France debris evidence illustrates an informative prior rather than calibrating the sparse-prior model."),
        (3, "MH370 comparator", "MH370 motivates the no-signal setting but contributes no archived likelihood data to Flight ABCD."),
        (4, "radar horizon", "The 200-mile coastal radar premise is cited context and simplified geometry, not a verified coverage surface."),
        (4, "glide physics", "Glide ratio translates altitude into distance while winds, aircraft state, and failure mode are absent."),
        (6, "deviation geometry", "The pi/8 deviation scale is visually explained but not estimated from incident data."),
        (7, "regional integration", "The N by 6 scheme exposes integrals but Appendix A does not preserve an unambiguous translated support."),
        (9, "coordinate transform", "Figure 3 and Appendix B expose interfaces while exact spreadsheet formulas and unit direction require audit."),
        (10, "Koopman adaptation", "The exponential form is cited, but the modified sweep and condition parameters are not sensor-calibrated."),
        (11, "miss update", "The source retains total POC through redistribution without deriving a conditional posterior."),
        (13, "sensitivity plots", "One-at-a-time curves show local directions while figure references, captions, and altitude prose conflict."),
        (18, "Flight ABCD surface", "The worked density and grid are visible without a normalization or independent numerical audit."),
        (21, "path comparison", "Two route plots support a qualitative travel contrast without distance, fuel, or optimality totals."),
        (25, "Appendix A-B", "Integration code and coordinate tables expose partial reproduction evidence but no exact executable workbook or environment."),
        (27, "Appendix C-D", "Code and printed sequences expose algorithm intent while symbol, rounding, loop-condition, and local/global selection defects remain."),
    ]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = ["Apply only when incident evidence, density support, coordinates, units, cell geometry, sensor likelihood, update normalization, route state, resource constraints, uncertainty, and receiving decision are explicit."]
        row["counterevidence"] = ["A smooth density, selected cell, one-at-a-time curve, worked scenario, plotted route, mass-conserving update, appendix listing, or public claim does not prove calibration, posterior validity, optimality, reproducibility, or universal transfer."]
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
        ("R-B-LANG-001", "retain sparse-evidence framing, containment construction, cell operationalization, detector definition, miss-to-action update, sensitivity interpretation, worked-example trace, bounded conclusion, public chronology, and appendix provenance with typed slots", first["language"]),
        ("R-B-LOG-001", "trace last communication through radar/glide containment, cross-track uncertainty, timed cells, coordinates, POD, nondetection, neighborhood choice, Flight ABCD outputs, restrictions, and public action", first["logic"]),
        ("R-B-DATA-001", "version incident coordinates, endpoint distance, aircraft and search-platform specifications, units, sensor reach, weather factor, cell matrix, algorithm variant, references, and appendix environment", first["data"]),
        ("R-B-DATA-002", "maintain assumptions for linear route, glide and impact, debris breakup, deviation bound, stationary debris, constant speeds, near-contact prior, persistent detectability, and homogeneous fleet", evidence("R-B-DATA-002")),
        ("R-B-MOD-001", "retain casualty and impact densities, cross-track and joint containment, N by 6 integration, geospatial transform, Koopman POD, miss update, neighborhood route, sensitivity, scenario, and recommendation interfaces", first["modeling"]),
        ("R-B-MOD-003", "combine spatial prior, timed cell geometry, geodesic coordinates, sensor likelihood, normalized posterior, route/fleet state, and rescue decision only through typed support, unit, probability, and time contracts", evidence("R-B-MOD-003")),
        ("R-B-MOD-004", "keep support, N, POC cell, POD, fleet size, adjacent/unrestricted route, revisit state, coordinate output, qualitative travel claim, and recommendation distinct", first["result"]),
        ("R-B-MOD-005", "stress casualty prior, support translation, deviation dependence, grid resolution, geodesic units, sensor calibration, posterior normalization, route optimality, drift, fleet coordination, and stopping criteria", evidence("R-B-MOD-005")),
        ("R-B-VER-002", "make every reliability claim geometry-, integral-, transform-, curve-, scenario-, path-, code-, coordinate-, and decision-trace-specific", first["verification"]),
        ("R-B-VER-004", "reconcile malformed CDF, shifted support, cell bounds, rho direction, heuristic redistribution, figure/caption conflicts, altitude direction, kappa/k, Ceiling, loop semantics, appendix headings, and unsupported scope claims", first["weakness"]),
        ("R-B-VIZ-001", "retain deviation geometry, discretization, indexed cells, sensitivity curves, joint density, POC grid/map, path pair, and coordinate tables with exact labels, source defects, and uncertainty boundaries", first["visualization"]),
        ("R-B-COMP-001", "measure density normalization, regional integration, coordinate conversion, POD evaluation, posterior update, neighborhood/global selection, route travel, revisit coverage, multi-aircraft coordination, and reproducible runtime separately", evidence("R-B-COMP-001")),
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
        {"language_unit_id": unit["language_unit_id"], "disposition": "supports-existing", "target_pattern_ids": unit["candidate_pattern_ids"], "reason": "The rhetorical mechanism transfers only after replacing incident, aircraft, route, prior, sensor, cell, update, result, resource, and audience entities."}
        for unit in language["units"]
    ]
    argument_metadata = {
        "sparse-evidence-to-location-field": {"claim": "Last communication, radar horizon, glide, and cross-track deviation turn sparse flight evidence into a bounded joint containment field.", "source_pages": [2, 3, 4, 5, 6]},
        "location-field-to-operational-cells": {"claim": "Timed discretization and an explicit coordinate transform turn the continuous field into search-region probabilities and geographic corners.", "source_pages": [6, 7, 8, 9]},
        "sensor-and-miss-to-next-action": {"claim": "A resource-parameterized detector and miss update connect imperfect sensing to a travel-aware neighboring-cell sequence with revisits.", "source_pages": [10, 11, 12]},
        "parameter-and-example-to-recommendation": {"claim": "Sensitivity and Flight ABCD show how incident and fleet parameters propagate through 36 POC cells, POD, two route variants, and an operational recommendation.", "source_pages": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]},
        "technical-to-public-and-reproducibility": {"claim": "Strength/limit boundaries, the press summary, references, and appendices carry the model to public action while exposing unresolved evidence and execution gaps.", "source_pages": [15, 16, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]},
    }
    chains = []
    for chain in organization["main_argument_chains"]:
        metadata = argument_metadata[chain["name"]]
        chains.append({"claim": metadata["claim"], "support_steps": chain["chain"], "decision_consequence": chain["decision"], "source_pages": metadata["source_pages"]})
    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": organization["global_progression"] + ["Only after the positive language, organization, model, and visual chain is complete does G7 record algebra, support, unit, update, caption, implementation, validation, and scope warnings."],
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
        "request_body_guard": {"bounded_jpeg_proxies": 8, "total_proxy_bytes": 1367613, "original_full_page_png_in_context": False},
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
        raise ValueError("q111 extraction identity or page count does not match the current paper")

    template = load_module(ROOT / "scripts/build_q100_artifacts.py", "q100_template_for_q111")
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
            "All 32 physical pages were inspected through eight one-at-a-time byte-bounded JPEG proxies totaling 1,367,613 bytes. No clipping, overlap, missing page, blank page, black box, or formula-rendering failure was found.",
            "Figures 1-13, four substantive tables, and 37 displayed equations or equation families were reconciled by source page. Focused proxies covered page-5 distributions, page-9 coordinates, page-11 updating, and pages-14-15 sensitivity labels.",
            "No original full-page PNG, contact sheet at original detail, batched image response, or complete session JSONL entered model context.",
            "Source defects are retained separately, including support/algebra conflicts, figure-caption mismatches, ambiguous Mathematica code, and unsupported validation claims.",
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

    print(json.dumps({"paper_id": PAPER_ID, "stage": str(STAGE), "chapters": len(language["available_chapters"]), "language_units": len(language["units"]), "models": len(models["models"]), "equations": 37, "dependency_edges": len(models["dependency_edges"]), "visuals": len(visuals["visuals"]), "observations": len(observations), "warnings": len(WARNINGS), "proxy_bytes": visuals["transport_safety"]["total_proxy_bytes"], "status": "pass"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
