from __future__ import annotations

"""Assemble create-only Queue 109 G7-G8 learning artifacts."""

import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-36178-d0225ad0"
SHORT = "36178"
SHA = "d0225ad0b9c2d2dcdb91f20526f5bed617d1c221aff50ab700ad9cf85b1df9ff"
TYPE = "B"
YEAR = "2015"
PAGE_COUNT = 20
STAGE = ROOT / "tmp/q109-stage-v2"
LANGUAGE_PATH = ROOT / "tmp/q109-language-stage-v4/language.json"
ORGANIZATION_PATH = ROOT / "tmp/q109-organization-stage-v1/organization.json"
MODELS_PATH = ROOT / "tmp/q109-model-stage-v1/models.json"
VISUALS_PATH = ROOT / "tmp/q109-visual-stage-v2/visuals.json"


WARNINGS = [
    {
        "page": 8,
        "model_id": "MU-B-2015-36178-001",
        "equation_id": "EQ-B-2015-36178-001",
        "summary": (
            "Equation 1 inserts 1.5t directly into cosine after defining the turn rate as 1.5 degrees per "
            "second. A numerical implementation must state whether the trigonometric function receives degrees "
            "or radians and apply the conversion explicitly."
        ),
    },
    {
        "page": 12,
        "model_id": "MU-B-2015-36178-006",
        "equation_id": "EQ-B-2015-36178-008",
        "summary": (
            "Equation 7 visibly spaces the total-leg symbol as T L_i and compresses the summand around L_i, "
            "1, 2, and 3. Preserve the printed ambiguity and reconstruct the intended finite sequence with "
            "typed indices before coding it."
        ),
    },
    {
        "page": 13,
        "model_id": "MU-B-2015-36178-007",
        "equation_id": "EQ-B-2015-36178-010",
        "summary": (
            "Equation 9 prints the region name with a visibly spaced n-gon token while defining A_search as "
            "maximum width times maximum height. That quantity is the axis-aligned bounding rectangle, not the "
            "area of the drifting polygon, and the distinction must survive transcription."
        ),
    },
    {
        "page": 13,
        "model_id": "MU-B-2015-36178-007",
        "equation_id": "EQ-B-2015-36178-010",
        "summary": (
            "The daily stopping rule is displayed as a sum of POD values exceeding 0.95. Daily PODs are not "
            "automatically additive probabilities; a reusable implementation needs an explicit conditional miss "
            "or survival update, dependence assumptions for repeated passes, and the day-specific moving area."
        ),
    },
    {
        "page": 7,
        "model_id": "MU-B-2015-36178-003",
        "equation_id": "EQ-B-2015-36178-005",
        "summary": (
            "Effective sweep width is interpolated from an unfrozen external table and later altered by an "
            "unstated piecewise wind function. Target size, observer performance, sensor mode, units, interpolation "
            "domain, and calibration evidence are missing, so the resulting POD is not a field-calibrated detection probability."
        ),
    },
    {
        "page": 10,
        "model_id": "MU-B-2015-36178-002",
        "equation_id": "EQ-B-2015-36178-004",
        "summary": (
            "The current update lacks a frozen current grid, coordinate reference system, longitude/latitude unit "
            "contract, spatial interpolation rule, boundary behavior, and time-step convergence check. The source "
            "also limits available current data to the MH370 vicinity, so neither forward nor reverse drift transfers globally."
        ),
    },
    {
        "page": 9,
        "model_id": "MU-B-2015-36178-001",
        "equation_id": None,
        "summary": (
            "Convex-hull closure fills nonconvex gaps in the endpoint set, and the later maximum-width by "
            "maximum-height rectangle adds further area outside that hull. Both conservative inflations must be "
            "measured separately because they directly enlarge coverage time and can dominate route comparisons."
        ),
    },
    {
        "page": 12,
        "model_id": "MU-B-2015-36178-006",
        "equation_id": "EQ-B-2015-36178-008",
        "summary": (
            "Plane assignment is sequential and greedy: each plane takes the block of its type with most empty "
            "space, delayed aircraft lose one leg, and extra aircraft repeat earlier coverage. No joint scheduling "
            "optimality, conflict separation, overlap correlation, or independent repeated-pass detection model is established."
        ),
    },
    {
        "page": 14,
        "model_id": "MU-B-2015-36178-009",
        "equation_id": None,
        "summary": (
            "Figure 7 compresses more than 900 heterogeneous scenarios into an unpublished index, uses dense "
            "red/blue overplotting without a plotted legend or axis titles, and reports no uncertainty or paired "
            "scenario table. It supports a conditional within-model comparison, not a reproducible or universal route ranking."
        ),
    },
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
    records = (language, organization, models, visuals)
    if any(record.get("paper_id") != PAPER_ID for record in records):
        raise ValueError("q109 stage paper IDs do not agree")
    if language.get("review_status") != "validated" or len(language.get("units", [])) != 68:
        raise ValueError("authoritative G1-G3 language stage is not validated at 68 units")
    if len(organization.get("section_contracts", [])) != 17:
        raise ValueError("G4 must retain 17 section contracts")
    if models.get("review_status") != "validated" or len(models.get("models", [])) != 9:
        raise ValueError("authoritative G5 model stage is not validated at nine models")
    equation_count = sum(len(model.get("governing_equations", [])) for model in models["models"])
    if equation_count != 11:
        raise ValueError(f"G5 must retain 11 equations, found {equation_count}")
    if visuals.get("review_status") != "validated" or len(visuals.get("visuals", [])) != 7:
        raise ValueError("authoritative G6 stage is not validated at seven visuals")
    if len(WARNINGS) >= len(language["units"]):
        raise ValueError("G7 warnings must be a strict minority of positive language units")


def build_card(organization: dict, models: dict, visuals: dict) -> dict:
    section_map = []
    for contract in organization["section_contracts"]:
        section_map.append(
            {
                "page": contract["pages"][0],
                "section": " / ".join(contract["source_headings"]),
                "summary": (
                    f"Input: {contract['input']} Analytical job: {contract['analytical_job']} "
                    f"Output: {contract['output']} Handoff: {contract['handoff']}"
                ),
            }
        )
    visual_records = []
    for visual in visuals["visuals"]:
        visual_records.append(
            {
                "page": visual["source_page"],
                "figure": visual["figure"],
                "visual_record_id": visual["visual_record_id"],
                "caption": visual["caption"],
                "source_model_ids": visual["source_model_ids"],
                "summary": (
                    f"{visual['analytical_purpose']} Exact supported claim: {visual['exact_claim_supported']} "
                    f"Uncertainty boundary: {visual['uncertainty']}"
                ),
                "disposition": visual["disposition"],
                "evidence_role": visual["evidence_role"],
            }
        )
    weaknesses = [dict(item) for item in WARNINGS]
    return {
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "team_control_number": SHORT,
        "title": "So You Lost a Plane?",
        "award_status": "outstanding",
        "source": {
            "relative_path": "2015\u7f8e\u8d5b\u7279\u7b49\u5956/B-36178-Outstanding.pdf",
            "sha256": SHA,
            "page_count": PAGE_COUNT,
            "pdf_page_offset_note": (
                "Physical page 1 is the unnumbered Summary; physical pages 2-18 contain printed pages 1-17; "
                "physical pages 19-20 are a separate press communication."
            ),
        },
        "schema_version": 1,
        "source_quality": {
            "status": "validated",
            "text_pages": PAGE_COUNT,
            "rendered_pages": PAGE_COUNT,
            "visual_review": "complete",
            "notes": [
                "All 20 UTF-8 page-text files were read sequentially, with Summary and Introduction studied first.",
                "Four byte-bounded overview proxies covered physical pages 1-20 and focused proxies reconciled formulas and Figures 3-7; no original full-page PNG was transported.",
                "All seven numbered figures have a source-ordered, model-linked disposition; repeated press renderings of Figures 1, 2, and 5 do not inflate the count.",
                "The official 2015 problem statement is not available in the manifest, so task reconstruction is limited to the paper's own statements and deliverables.",
            ],
        },
        "context_sources": [
            {"type": "paper", "path": "2015\u7f8e\u8d5b\u7279\u7b49\u5956/B-36178-Outstanding.pdf"},
            {"type": "extraction", "path": f"artifacts/papers/{PAPER_ID}/extraction.json"},
            {"type": "text-pages", "path": f"artifacts/papers/{PAPER_ID}/text/pages"},
            {"type": "visual-stage", "path": "tmp/q109-visual-stage-v2/visuals.json"},
        ],
        "task_reconstruction": {
            "status": "incomplete-official-task-unavailable",
            "inputs": [
                "last known coordinates and heading",
                "downed-aircraft family, speed, altitude, mass, glide, and turn behavior",
                "crash wind and local current field",
                "search-aircraft type, range, speed, count, daylight, weather, and visibility",
                "found-debris time and coordinates",
            ],
            "outputs": [
                "initial conservative crash region",
                "daily drifting debris-search polygon",
                "parallel, diagonal, and optimized-parallel swept areas",
                "modeled days to a 95-percent detection threshold",
                "reverse-current crash-origin estimate",
                "conditional route recommendation and public explanation",
            ],
            "decisions": [
                "how aircraft state bounds initial location",
                "how currents update that region each day",
                "which search route uses available resources",
                "how repeated coverage affects the stopping rule",
                "how debris evidence revises the crash estimate",
                "which uncertainty and provenance limits remain",
            ],
        },
        "section_map": section_map,
        "assumptions": [
            {"page": 4, "summary": "A worst-case open-water power-loss crash is modeled with negligible drag, flat water, and debris remaining afloat."},
            {"page": 4, "summary": "Search is visual-only, unaffected by fatigue, limited to ten daylight hours, and staged 200 nautical miles from the search area."},
            {"page": 8, "summary": "A 1.5-degree-per-second turn and unpowered glide geometry bound reachable endpoints after last contact."},
            {"page": 9, "summary": "Wind direction is unknown, so the perimeter is expanded by wind speed along outward normals before convex closure."},
            {"page": 10, "summary": "Debris-current motion is advanced in discrete 24-hour Euler steps rather than continuously."},
            {"page": 12, "summary": "Staggered same-type aircraft lose one search leg per delayed start and are assumed to finish within the common window."},
        ],
        "data_and_preprocessing": [
            {"page": 6, "summary": "Five aircraft families are represented by one named aircraft each; source specifications feed speed, altitude, mass, and range interfaces."},
            {"page": 7, "summary": "Search sweep widths are interpolated in Mathematica from an external search-and-rescue table that is not frozen with the paper."},
            {"page": 9, "summary": "Endpoint samples are wind-expanded, convex-hulled, placed on a longitude-latitude grid, and marked for daily drift."},
            {"page": 10, "summary": "A local MH370-area current field advances markers by Euler updates and a new hull encloses each day's positions."},
            {"page": 13, "summary": "More than 900 combinations vary area, aircraft, weather, wind, visibility, and related search settings, but the scenario matrix is not published."},
            {"page": 15, "summary": "Sensitivity uses one declared median baseline and changes one parameter at a time until a day count changes on one or both sides."},
        ],
        "models": [
            {"model_id": model["model_id"], "page": model["page"], "summary": model["summary"]}
            for model in models["models"]
        ],
        "dependency_graph": models["dependency_edges"],
        "verification": [
            {"page": 13, "section": "AF447 comparison", "summary": "The paper compares its conservative 125-nautical-mile radius with AF447's 40-nautical-mile search radius.", "verification_type": "context comparison", "strength": "The discrepancy is reported and explained through information precision.", "limitation": "Different incident information makes this a scope illustration, not calibration or validation."},
            {"page": 14, "section": "algorithm scenario comparison", "summary": "Diagonal and optimized-parallel day counts are compared across more than 900 stated scenarios.", "verification_type": "within-model scenario sweep", "strength": "The paper exposes conditional best and worst regimes.", "limitation": "The scenario table, code, paired outputs, and uncertainty are absent."},
            {"page": 15, "section": "height and crash-wind sensitivity", "summary": "One-at-a-time perturbations report day-count changes around the 11-day baseline.", "verification_type": "local sensitivity", "strength": "Baseline and changed inputs are explicit.", "limitation": "One or two changes cannot establish the claimed global functional forms."},
            {"page": 16, "section": "aircraft, search-wind, and visibility sensitivity", "summary": "Resource and observation inputs are perturbed and their modeled day responses are stated.", "verification_type": "local sensitivity", "strength": "Decision-facing inputs are linked to completion time.", "limitation": "No interaction, uncertainty, calibration, or repeated-run analysis is supplied."},
            {"page": 17, "section": "strengths and weaknesses", "summary": "The source itself identifies rectangular over-search, local current data, survivor drift, and omitted glide-speed state.", "verification_type": "source scope audit", "strength": "Concrete mechanisms are named.", "limitation": "Self-reported limitations do not measure their quantitative impact."},
        ],
        "results_trace": [
            {"page": 13, "summary": "The simple parallel route ranges from 3 to 3,581 modeled days and cannot exploit capacity beyond one daily sweep."},
            {"page": 14, "summary": "Diagonal search is usually two modeled days faster than simple parallel but reaches more than 35,000 days in adverse cases."},
            {"page": 15, "summary": "Optimized parallel is recommended for few-plane/large-area/bad-weather and many-plane/small-area/good-weather regimes; diagonal is recommended otherwise."},
            {"page": 15, "summary": "The declared sensitivity baseline is an 85,957-square-nautical-mile region with a modeled 11-day search."},
            {"page": 16, "summary": "Altitude, crash wind, aircraft count, search wind, and visibility perturbations change the rounded day output by different local amounts."},
            {"page": 17, "summary": "The conclusion retains a conditional method choice because weather, area, aircraft count, and unknown crash behavior alter the result."},
        ],
        "contributions": [
            {"page": 8, "summary": "Turn-constrained glide endpoints replace a single circular radius with a more explicit reachable-boundary construction."},
            {"page": 10, "summary": "Marker-wise current advection makes the search region move and reshape between daily operations."},
            {"page": 11, "summary": "Productive searchlegs are separated from crossleg and turn overhead before swept area is counted."},
            {"page": 12, "summary": "Diagonal and repeated parallel blocks expose different resource and corner-geometry tradeoffs."},
            {"page": 13, "summary": "The same current interface is reversed after debris is found, closing an evidence-to-location feedback loop."},
            {"page": 15, "summary": "Conditional route rules are stated from scenario behavior rather than naming one method universally best."},
            {"page": 19, "summary": "The press communication translates required facts, bounded area, field search, found debris, and iterative replanning for a public audience."},
        ],
        "writing_logic": [
            {"page": contract["pages"][0], "summary": f"{contract['chapter']}: {contract['rhetorical_job']} {contract['handoff']}"}
            for contract in organization["section_contracts"]
        ],
        "language_observations": [
            {"page": contract["pages"][0], "summary": f"{contract['chapter']}: {contract['input']} -> {contract['output']}"}
            for contract in organization["section_contracts"]
        ],
        "visualization_observations": visual_records,
        "judge_relevance_hypotheses": [
            {"page": 1, "summary": "The Summary gives a complete location-to-drift-to-search-to-decision route, but award status does not prove which element caused the judgment.", "evidence_class": "J"},
            {"page": 14, "summary": "A shared-scale scenario comparison makes conditional route behavior visible, without establishing field validity or global optimality.", "evidence_class": "J"},
            {"page": 19, "summary": "The separate public communication closes the technical-to-stakeholder loop, without proving operational readiness.", "evidence_class": "J"},
        ],
        "weaknesses": weaknesses,
        "independent_extensions": [
            {"extension_id": "E-B-36178-001", "page": 8, "summary": "Use aircraft-specific energy, drag, failure-mode, bank-angle, and uncertainty models to produce a probabilistic reachable set rather than a single hull."},
            {"extension_id": "E-B-36178-002", "page": 10, "summary": "Archive georeferenced current fields and propagate particles with interpolation, adaptive steps, diffusion, windage, and ensemble uncertainty."},
            {"extension_id": "E-B-36178-003", "page": 10, "summary": "Calibrate sweep width and detection curves from target-, sensor-, observer-, sea-state-, altitude-, visibility-, and weather-specific trials."},
            {"extension_id": "E-B-36178-004", "page": 12, "summary": "Formulate joint multi-aircraft routing with separation, staging, refueling, turn dynamics, overlap, and conditional repeated-pass detection."},
            {"extension_id": "E-B-36178-005", "page": 13, "summary": "Replace additive daily POD with a documented conditional miss/survival update on the moving region and report uncertainty in days-to-threshold."},
            {"extension_id": "E-B-36178-006", "page": 14, "summary": "Publish the full scenario matrix and paired outputs, then use explicit factors, paired differences, uncertainty, and held-out incident comparisons."},
            {"extension_id": "E-B-36178-007", "page": 17, "summary": "Measure hull and rectangle inflation and let routes operate on the actual nonrectangular search geometry when operationally feasible."},
        ],
        "candidate_rule_impacts": [],
        "unresolved_questions": [item["summary"] for item in weaknesses],
        "protocol_v2_records": {},
        "review_status": "validated",
    }


def make_observations(template, language: dict, models: dict, card: dict) -> list[dict]:
    observations = template.make_observations(language, models, card)
    interpretations = {
        "language": "Reuse the rhetorical mechanism only after replacing incident, aircraft, current, search, resource, evidence, and audience entities.",
        "modeling": "Retain reachable-set, current, detection, path, coverage, stopping-rule, reverse-trace, scenario, and handoff terms together.",
        "logic": "Preserve the positive incident-to-location-to-drift-to-route-to-comparison-to-evidence-feedback chain before warnings.",
        "visualization": "Keep geometry, axes, units, scenario identity, method encoding, uncertainty, source status, and decision purpose together.",
        "verification": "Name the exact scenario, comparator, sensitivity input, source-scope statement, or evidence boundary being checked.",
        "data": "Retain aircraft facts, source, units, coordinate system, current field, sweep-width table, scenario settings, and downstream consumer.",
        "assumption": "Pair every physical, sensing, operational, and temporal assumption with its enabled calculation and excluded regime.",
        "result": "Keep swept area, daily POD, cumulative threshold, modeled days, scenario state, route choice, and field evidence distinct.",
        "weakness": "Record notation, probability, calibration, geometry, scheduling, provenance, and visual risks only after positive G1-G6 learning.",
        "other": "Separate cited context and displayed support from frozen inputs, executable algorithms, run logs, and independent validation.",
    }
    provenance = [
        (18, "references", "The references identify aircraft, search-theory, geometry, current, and incident context but do not freeze the exact source bytes used."),
        (7, "sweep-width source", "The external search-and-rescue table supports the sweep-width concept but the interpolated table and function are not archived."),
        (10, "current-field source", "The MH370-area current demonstration supplies context but not a versioned georeferenced current grid or interpolation contract."),
        (8, "turn geometry", "The worked 500-knot and 40-nautical-mile example supports a geometric illustration, not aircraft-wide calibration."),
        (9, "convex hull", "The displayed hull explanation supports containment while leaving sampling density and inflation unmeasured."),
        (11, "searchleg schematic", "The cited searchleg diagram supports terminology but not the paper's complete scheduling or detection implementation."),
        (13, "AF447 context", "The incident comparison exposes information-bound differences but does not validate the paper's radius calculation."),
        (14, "scenario comparison", "Figure 7 supports a conditional within-model comparison while the scenario-index mapping remains unpublished."),
        (15, "sensitivity baseline", "The stated median scenario permits local reruns but not a probability distribution over real search conditions."),
        (16, "source limitations", "The paper names local current, survivor, and glide-speed gaps without quantifying their effect on outputs."),
        (17, "references", "Citations provide attribution but no code, Mathematica notebook, parameter table, scenario matrix, seeds, or environment lock."),
        (19, "press communication", "The audience artifact reuses model outputs but supplies no additional technical validation."),
        (20, "press communication", "The operational loop is readable for stakeholders while remaining conditional on the technical assumptions."),
        (10, "coordinate provenance", "Longitude and latitude markers are named without a coordinate-reference or wraparound contract."),
        (13, "daily stopping rule", "The displayed threshold statement exposes the intended stopping decision but not a valid dependence model across days."),
        (14, "scenario provenance", "The more-than-900 scenario claim is not accompanied by a machine-readable design or paired result table."),
    ]
    other_index = 0
    for row in observations:
        row["interpretation"] = interpretations[row["dimension"]]
        row["applicability"] = [
            "Apply only when incident state, coordinate system, aircraft dynamics, current field, sensing model, resources, route constraints, probability update, and decision scope are explicit."
        ]
        row["counterevidence"] = [
            "A conservative hull, simulated day count, opaque scenario plot, local sensitivity, or press explanation does not prove calibration, field effectiveness, global optimality, or universal transfer."
        ]
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
        ("R-B-LANG-001", "retain the incident-to-location-to-drift-to-route-to-comparison-to-evidence-feedback-to-public-communication sequence with explicit boundaries", first["language"]),
        ("R-B-LOG-001", "trace last contact through reachable geometry, current updates, search blocks, probability threshold, reverse drift, route choice, and stakeholder action", first["logic"]),
        ("R-B-DATA-001", "version aircraft specifications, coordinate systems, current grids, sweep-width tables, weather, visibility, scenario designs, and found-debris records", first["data"]),
        ("R-B-DATA-002", "maintain assumptions for drag, crash mode, sensing, daylight, fatigue, staging, debris persistence, current motion, and repeated coverage", evidence("R-B-DATA-002")),
        ("R-B-MOD-001", "retain glide and turn geometry, wind expansion, current advection, POD, three routes, daily threshold, reverse trace, scenarios, and handoffs", first["modeling"]),
        ("R-B-MOD-003", "combine reachable sets, moving polygons, coverage, detection, scheduling, and route selection only through typed coordinate, unit, probability, and resource contracts", evidence("R-B-MOD-003")),
        ("R-B-MOD-004", "keep polygon area, bounding rectangle, swept area, daily POD, cumulative detection, days, scenario state, and route recommendation distinct", first["result"]),
        ("R-B-MOD-005", "stress angle units, hull inflation, current interpolation, sweep-width calibration, daily dependence, greedy scheduling, route interactions, and scenario uncertainty", evidence("R-B-MOD-005")),
        ("R-B-VER-002", "make every reliability claim incident-, equation-, geometry-, scenario-, sensitivity-, figure-, or deployment-trace-specific", first["verification"]),
        ("R-B-VER-004", "reconcile degree/radian use, T L_i notation, n-gon versus rectangle, additive POD, missing provenance, repeated-pass dependence, and Figure 7 opacity", first["weakness"]),
        ("R-B-VIZ-001", "retain candidate patterns, current vectors, reachable loci, searchleg geometry, scenario comparison, audience reuse, captions, encodings, and uncertainty boundaries", first["visualization"]),
        ("R-B-COMP-001", "measure endpoint sampling, hull construction, marker advection, block assignment, path coverage, scenario sweeps, sensitivity reruns, and multi-aircraft scheduling separately", evidence("R-B-COMP-001")),
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
            paragraphs.append(
                {
                    "paragraph_index": source["paragraph"],
                    "dominant_move": (
                        f"{source['dominant_move']}: {source['claim']} -> {source['consequence']} -> {source['next_link']}"
                    ),
                    "language_unit_ids": source["language_unit_ids"],
                }
            )
        paragraph_chains.append(
            {
                "chapter": chapter,
                "visual_paragraph_count": len(paragraphs),
                "coverage_status": "complete",
                "gaps": [],
                "paragraphs": paragraphs,
            }
        )
    audit["paragraph_chains"] = paragraph_chains
    audit["language_unit_dispositions"] = [
        {
            "language_unit_id": unit["language_unit_id"],
            "disposition": "supports-existing",
            "target_pattern_ids": unit["candidate_pattern_ids"],
            "reason": "The rhetorical mechanism transfers only after replacing incident, aircraft, current, search, resource, evidence, and audience entities.",
        }
        for unit in language["units"]
    ]
    argument_metadata = {
        "initial-search-area argument": {
            "claim": "The initial search region is a conservative reachable set constrained by aircraft state, glide-turn geometry, and crash wind rather than a point-centered circle.",
            "source_pages": [4, 6, 8, 9],
        },
        "daily-route-selection argument": {
            "claim": "Daily route choice follows from the drifting region, sensing conditions, aircraft resources, route geometry, and a scenario-conditioned detection-time comparison.",
            "source_pages": [7, 10, 11, 12, 13, 14, 15, 16, 17],
        },
        "evidence-feedback argument": {
            "claim": "Found debris should be propagated backward through the current field to revise the crash estimate and the next forward search cycle.",
            "source_pages": [10, 13, 17],
        },
    }
    main_argument_chains = []
    for chain in organization["main_argument_chains"]:
        name = chain["name"]
        if name not in argument_metadata:
            raise ValueError(f"unmapped G4 argument chain: {name}")
        metadata = argument_metadata[name]
        main_argument_chains.append(
            {
                "claim": metadata["claim"],
                "support_steps": chain["chain"],
                "decision_consequence": chain["decision"],
                "source_pages": metadata["source_pages"],
            }
        )

    audit["organization_logic"] = {
        "positive_artifacts_status": "complete",
        "weakness_substitution_allowed": False,
        "global_organization_chain": organization["global_progression"]
        + ["Only after the complete positive chain does G7 record notation, probability, calibration, geometry, scheduling, provenance, and visual warnings."],
        "section_progressions": [
            {
                "chapter": contract["chapter"],
                "moves": [
                    f"input: {contract['input']}",
                    f"rhetorical job: {contract['rhetorical_job']}",
                    f"analytical job: {contract['analytical_job']}",
                    f"output: {contract['output']}",
                    f"handoff: {contract['handoff']}",
                ],
                "positive_pattern": "Use the source-anchored input -> rhetorical job -> analytical job -> output -> handoff contract; warnings remain a last pass.",
            }
            for contract in organization["section_contracts"]
        ],
        "main_argument_chains": main_argument_chains,
    }
    audit["formula_error_watch"] = {
        "mode": "last-pass-warning-only",
        "completed_after_positive_passes": True,
        "warnings": [
            {
                "model_id": warning["model_id"],
                "equation_id": warning["equation_id"],
                "page": warning["page"],
                "warning": warning["summary"],
            }
            for warning in WARNINGS
            if warning["equation_id"] is not None
        ],
    }
    audit["visualization_dispositions"] = [
        {
            "paper_card_visual_index": visual["paper_card_visual_index"],
            "visual_record_id": visual["visual_record_id"],
            "disposition": visual["disposition"],
            "analytical_purpose": visual["analytical_purpose"],
        }
        for visual in visuals["visuals"]
    ]
    counts = Counter(row["dimension"] for row in observations)
    audit["dimension_counts"] = {
        dimension: counts[dimension]
        for dimension in [
            "language",
            "modeling",
            "logic",
            "visualization",
            "verification",
            "data",
            "assumption",
            "result",
            "weakness",
            "other",
        ]
    }
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
    validate_inputs(language, organization, models, visuals)

    template = load_module(ROOT / "scripts/build_q100_artifacts.py", "q100_template_for_q109")
    for name, value in {
        "PID": PAPER_ID,
        "SHORT": SHORT,
        "SHA": SHA,
        "TYPE": TYPE,
        "YEAR": YEAR,
        "PAGE_COUNT": PAGE_COUNT,
    }.items():
        setattr(template, name, value)

    card = build_card(organization, models, visuals)
    card["protocol_v2_records"] = {
        "language": {
            "path": f"artifacts/language-units/{PAPER_ID}.json",
            "schema_version": language["schema_version"],
            "unit_count": len(language["units"]),
            "chapters": language["available_chapters"],
            "review_status": language["review_status"],
        },
        "models": {
            "path": f"artifacts/model-units/{PAPER_ID}.json",
            "schema_version": models["schema_version"],
            "model_count": len(models["models"]),
            "equation_count": sum(len(model["governing_equations"]) for model in models["models"]),
            "review_status": models["review_status"],
        },
    }
    observations = make_observations(template, language, models, card)
    attach_rule_impacts(card, observations)
    audit = build_audit(template, language, organization, models, visuals, card, observations)

    STAGE.mkdir(parents=True)
    write_json_create(STAGE / "language.json", language)
    write_json_create(STAGE / "models.json", models)
    write_json_create(STAGE / "card.json", card)
    write_json_create(STAGE / "audit.json", audit)
    with (STAGE / "observations.jsonl").open("x", encoding="utf-8", newline="\n") as handle:
        for row in observations:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "stage": str(STAGE),
                "chapters": len(language["available_chapters"]),
                "language_units": len(language["units"]),
                "models": len(models["models"]),
                "equations": sum(len(model["governing_equations"]) for model in models["models"]),
                "visuals": len(visuals["visuals"]),
                "observations": len(observations),
                "warnings": len(WARNINGS),
                "status": "pass",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
