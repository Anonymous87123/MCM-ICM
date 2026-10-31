from __future__ import annotations

"""Build the source-ordered G6 figure and table record for Queue 112."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-40612-8bcdc1a7"
TYPE = "B"
YEAR = "2015"
SHORT = "40612"
SHA256 = "8bcdc1a780f3e08a678c1f450512da6656300cbb3c537ac5e97b29824f07322f"
STAGE = ROOT / "tmp/q112-visual-stage-v1"


def mid(*indexes: int) -> list[str]:
    return [f"MU-{TYPE}-{YEAR}-{SHORT}-{index:03d}" for index in indexes]


# label, page, model indexes, normalized caption, form, purpose, exact supported claim, source status
SPECS = [
    ("Table 1", 8, (8,), "Comparison between Different Types of Search Planes.", "three-platform capability table", "Establish speed, voyage, and sensor heterogeneity before the allocation model.", "The source compares SH-60B, P-3C, and C-130H and motivates capability-sensitive allocation; three examples do not calibrate a universal aircraft ranking.", "paper-authored comparison using cited specifications"),
    ("Table 2", 10, (1, 2, 4, 6, 7, 8), "Variable and Definition.", "two-column notation table", "Expose the symbols connecting drifter count, collision, cell probabilities, and surface/underwater detection.", "The table defines the principal N0-to-PAkW interfaces, while later I0, gamma, mixture weights, likelihood terms, and assignment variables remain incompletely specified.", "paper-authored notation table"),
    ("Figure 1", 12, (2,), "The Diagram for Water Disintegration.", "impact-geometry schematic", "Connect the contact angle and velocity decomposition to the impulse-based disintegration rule.", "The schematic supports the intended vertical-impact story, but the printed velocity-component equations omit the factor v and must be retained as a source inconsistency.", "paper-authored conceptual geometry"),
    ("Figure 2", 14, (4, 5, 6, 7, 8), "Summary of the Probability Distribution Computation.", "branched search-process flowchart", "Make the 50/50 flight prior, 70/30 surface prior, recursive Bayes updates, underwater transition, and allocation handoffs inspectable.", "The paper routes a flight prior and reverse-drift prior through separate surface and underwater branches; the percentages are heuristic mixture weights rather than fitted parameters.", "paper-authored model-architecture flowchart"),
    ("Figure 3", 15, (4,), "Cumulative Distribution of Distance from Beginning of Emergency to Impact Location.", "empirical cumulative curve with fitted function", "Supply the accident-distance component of the flight-dynamics prior.", "Nine cited loss-of-control accidents motivate the displayed cumulative distance curve and Equation (6); the sample, fitting residuals, and uncertainty are not reported.", "paper-authored fit to cited accident data"),
    ("Figure 4", 15, (4,), "Flight Dynamics Prior PDF.", "two-dimensional probability field", "Combine the LKP reachability field and accident-distance distribution into one search prior.", "The plotted field represents the paper's 50/50 flight-dynamics mixture; its normalization grid and numerical construction are not preserved.", "paper-authored model output"),
    ("Figure 5", 17, (3, 5), "Imagined Trajectories in System Simulation in Two Days.", "multi-trajectory synthetic drift plot", "Illustrate divergence under the paper's system module and motivate down-weighting reverse drift.", "The synthetic trajectories spread over two simulated days, but absent initial-condition sampling, random protocol, and current-data archive prevent treating the plot as observed or reproducible drift evidence.", "paper-authored synthetic simulation output"),
    ("Figure 6", 17, (4, 5, 6), "Surface Search Prior PDF for Impact Location.", "two-dimensional probability field", "Show the 70-percent flight and 30-percent reverse-drift mixture before search reports arrive.", "The field is the stated heuristic surface prior; its apparent concentration does not establish calibration or posterior validity.", "paper-authored model output"),
    ("Figure 7", 18, (6,), "Surface Search Posterior PDF for Impact Location.", "two-dimensional posterior probability field", "Visualize the normalized Bayes update after a surface-search report.", "The source depicts a surface posterior under Equation (7), but P(B|S), cell observations, detection rates, and numerical normalization inputs are not supplied.", "paper-authored model output"),
    ("Figure 8", 20, (7,), "Underwater Search Prior PDF for Impact Location.", "two-dimensional probability field", "Transfer the surface-stage result and flight prior into the first underwater search phase.", "The underwater prior uses the stated 30-percent surface-posterior and 70-percent flight-prior mixture; the weights are asserted rather than calibrated.", "paper-authored model output"),
    ("Figure 9", 20, (7,), "Underwater Search Posterior PDF for Impact Location.", "two-dimensional recursive posterior field", "Show how an unsuccessful underwater phase changes the next-phase search distribution.", "The figure represents one recursive underwater update, while phase evidence, likelihood parameters, stopping conditions, and numerical arrays remain absent.", "paper-authored model output"),
    ("Figure 10", 22, (8,), "Allocation Plan of the Search Aircrafts.", "cell-allocation diagram with heterogeneous rectangles", "Make the ranked matching of stronger aircraft to higher-probability cells concrete.", "Larger rectangles in the upper-left high-priority area denote better aircraft, illustrating a heuristic allocation; the diagram does not supply branch-and-bound variables, bounds, constraints, or an optimality trace.", "paper-authored allocation concept/output"),
    ("Figure 11", 24, (9,), "Underwater Search Prior PDF for AF447.", "case-comparison probability field with actual-location marker", "Compare the source pipeline's suggested AF447 region with the reported wreckage location.", "The actual AF447 point lies inside the displayed suggested area, which is a qualitative inclusion check without region area, coverage probability, comparator, or holdout validation.", "paper-authored retrospective case overlay using cited location"),
    ("Figure 12", 25, (9,), "The Search for MH370.", "dated regional search-area map", "Show how successive MH370 search proposals shifted across large arc-shaped regions.", "The reproduced map establishes that published candidate regions changed over time; it does not validate the paper's later conditional probability field.", "third-party map reproduced with citation"),
    ("Figure 13", 26, (9,), "Representation of Probability Distribution.", "satellite-arc probability-region map", "Provide the constrained-autopilot and data-error distribution used as the conditional MH370 flight prior.", "The cited analysis identifies overlapping high-probability latitude bands on the sixth and seventh arcs; the paper imports the representation without freezing its data or computation.", "third-party analytical map reproduced with citations"),
    ("Figure 14", 27, (7, 9), "PDFs for MH370.", "four-panel prior/posterior probability fields", "Carry the conditional MH370 distribution through surface prior, surface posterior, underwater prior, and underwater posterior stages.", "The four panels demonstrate pipeline propagation under assumed nondetection, not a location forecast with calibrated likelihoods, uncertainty intervals, or subsequent outcome validation.", "paper-authored conditional model output"),
    ("Table 3", 28, (10,), "Sensitivity Tests on the Number of Drifters.", "three-row deterministic sensitivity table", "Expose how the stated cumulative localization probability changes with N.", "For N=50,100,200 the table reports 0.545,0.583,0.619, supporting a local positive direction only under fixed unreported settings.", "paper-authored sensitivity output"),
    ("Table 4", 28, (8, 10), "Sensitivity Tests on the Number of Search Planes.", "three-row deterministic sensitivity table", "Expose the local resource response when nominal aircraft capability is fixed.", "For two, three, and four planes the reported cumulative values are 0.340,0.354,0.368; the small monotone change is not a fleet-level validation.", "paper-authored sensitivity output"),
    ("Table 5", 29, (8, 10), "Types of Search Planes according to Search Capabilities.", "nine-type capability parameter table", "Define area limits and surface/underwater detection inputs for allocation sensitivity.", "Nine synthetic capability types vary cell limits and detection probabilities, but the values are not tied to the real platforms in Table 1 or to calibration data.", "paper-authored synthetic parameter table"),
    ("Table 6", 29, (8, 10), "Sensitivity Tests on the Types of Search Planes.", "pairwise capability-combination result table", "Compare cumulative localization values for selected two-aircraft type combinations.", "The reported combinations range from 0.434 to 0.554 and generally favor stronger nominal inputs; one row is duplicated and no optimization trace or uncertainty is reported.", "paper-authored sensitivity output"),
    ("Table 7", 29, (4, 10), "Sensitivity Tests on the Weights in Computing Flight Dynamics PDF.", "three-mixture sensitivity table", "Check the output response to LKP-versus-distance mixture weights.", "Changing weights from 30/70 through 70/30 changes the reported value from 0.520 to 0.508, a narrow local range that does not establish global robustness.", "paper-authored sensitivity output"),
    ("Table 8", 30, (5, 6, 10), "Sensitivity Tests on the Weights in Computing Surface Search Prior PDF.", "three-mixture sensitivity table", "Check the output response to flight-versus-reverse-drift surface-prior weights.", "The three reported values are 0.518,0.518,0.520 under fixed conditions; the table supports local insensitivity only for these three mixtures.", "paper-authored sensitivity output"),
    ("Table 9", 30, (7, 10), "Sensitivity Tests on the Weights in Computing Underwater Search Prior PDF.", "three-mixture sensitivity table", "Check the output response to surface-posterior-versus-flight underwater-prior weights.", "The three reported values are 0.516,0.518,0.519 under fixed conditions; they do not justify reliability, universality, or calibrated uncertainty.", "paper-authored sensitivity output"),
]


def visual(index: int, spec: tuple) -> dict:
    label, page, model_indexes, caption, form, purpose, claim, source_status = spec
    is_table = label.startswith("Table")
    is_sensitivity = "sensitivity" in form
    return {
        "visual_record_id": f"V-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "paper_card_visual_index": index,
        "source_page": page,
        "printed_page": f"Page {page} of 34",
        "figure": label,
        "caption": caption,
        "analytical_purpose": purpose,
        "source_model_ids": mid(*model_indexes),
        "source_model_or_data": [source_status, "Source equations, mixture weights, cited incident context, synthetic inputs, cell probabilities, or scenario outputs described in the surrounding section and reconciled on the rendered page."],
        "form": form,
        "encodings": (["Rows encode variables, platforms, sensitivity cases, or aircraft combinations; columns encode definitions, capabilities, mixture weights, and reported cumulative probability.", "Symbols, units, percentages, and numeric cells carry the payload; no unstated statistic is inferred from table layout."] if is_table else ["Position, line, arrow, region, color, surface height, cell shape, marker, or panel order encodes the quantity or process named by the source.", "Caption, page context, and nearby prose establish whether the visual is conceptual, cited, simulated, prior, posterior, allocation, or case-comparison evidence."]),
        "axes_units_scales": ["Distance uses nautical miles or kilometers where printed; probabilities are dimensionless; platform speed is km/h, voyage is km, and mixture weights are percentages.", "Missing axis values, coordinate grids, legends, cell sizes, probability scales, trajectory timestamps, and map projections remain missing rather than inferred from appearance."],
        "normalization": "Probability fields inherit the source mixtures and Equation (7); sensitivity tables report the source cumulative quantity. Numerical grids, likelihoods, normalization checks, and rounding procedures are retained as missing when not printed.",
        "color_annotation_layout": ["Color, line weight, surface height, rectangles, markers, and panel letters are recorded only at the level needed to preserve the source's analytical role.", "All 34 rendered pages were checked for clipping, overlap, blank/black output, missing pages, and figure/table continuity; focused crops reconciled the page-12 piecewise rule, page-14 branch weights, and page-18 Bayes formula."],
        "uncertainty": ("This is a deterministic local sensitivity table over three or selected nominal settings; it has no confidence interval, sampling design, joint perturbation, calibrated error, or out-of-sample test." if is_sensitivity else "No complete uncertainty encoding is supplied; a conceptual diagram, synthetic trajectory set, smooth probability field, imported map, allocation sketch, or one retrospective overlay must not be read as calibration or predictive validation."),
        "exact_claim_supported": claim,
        "reproducible_construction_procedure": ["Use the source-defined scenario, equations, mixture, current interpolation, cell semantics, detection assumptions, allocation ranking, or cited case input associated with this record.", "Rebuild the named diagram, field, trajectory plot, map, panel, or table with direct labels and retain source page and model links.", "Verify the rebuilt visual against the bounded claim and do not infer missing arrays, random seeds, likelihoods, coordinates, optimizer traces, or external data from apparent geometry."],
        "missing_reproduction_information": ["Complete datasets, OSCAR snapshots, random protocols, software versions, plotting arrays, optimizer implementation, execution logs, and machine-readable outputs are not supplied.", "Exact grid resolution, map projection, cell probabilities, likelihood parameters, curve samples, trajectory seeds, and numerical normalization are limited to what the source visibly prints.", "Normalized descriptions are source-checked visual records; they do not manufacture labels or values absent from the rendered source."],
        "problem_type_applicability": [TYPE],
        "applicability": ["Use for missing-aircraft probability pipelines, staged surface/underwater search, heterogeneous resource allocation, case overlays, or local sensitivity reporting only when variables, data provenance, units, likelihoods, uncertainty, and decision scope are explicit."],
        "forbidden_scenarios": ["Do not treat a conceptual figure, synthetic simulation, imported map, smooth PDF, allocation sketch, one case inclusion, or three-point sensitivity table as empirical calibration, posterior correctness, optimal allocation, global robustness, or universal reliability.", "Do not transfer the visual to another aircraft, sensor, current regime, crash type, search phase, prior, cell grid, fleet, location, or time horizon without rebuilding its data and model."],
        "accessibility_and_interpretability": ["Small labels, dense fields, multiple panels, similar colors, and symbolic table headers require readable scale, direct labels, and redundant probability encoding.", "Standalone reuse must state axes/units, scenario, mixture, fixed parameters, source status, uncertainty boundary, and the exact supported claim."],
        "disposition": "important-visual-record",
        "evidence_role": "important-positive-record",
        "source_status": source_status,
        "audience_reuse": [],
    }


def build_visuals() -> dict:
    records = [visual(index, spec) for index, spec in enumerate(SPECS, start=1)]
    return {
        "schema_version": 1,
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "review_status": "validated",
        "gate": "G6-important-visual-retention",
        "source_page_coverage": {
            "physical_pages": 34,
            "review_proxy_ranges": ["1-7", "8-14", "15-21", "22-28", "29-34"],
            "focused_review_pages": ["12", "14", "18"],
            "figure_numbers": [f"Figure {index}" for index in range(1, 15)],
            "figure_count": 14,
            "substantive_table_numbers": [f"Table {index}" for index in range(1, 10)],
            "substantive_table_count": 9,
            "non_substantive_table_of_contents_excluded": True,
        },
        "transport_safety": {
            "one_image_per_tool_call": True,
            "max_proxy_bytes": 450000,
            "full_page_original_detail_used": False,
            "context_segments": 1,
            "total_bounded_jpeg_proxies": 8,
            "total_proxy_bytes": 1854278,
            "notes": "Five byte-bounded overview JPEG proxies covered pages 1-34 and three focused proxies reconciled the page-12 piecewise disintegration rule, page-14 probability flowchart, and page-18 normalized Bayes update. No original full-page PNG, original-detail contact sheet, multi-image tool result, or complete session JSONL entered model context.",
        },
        "gate_attestation": {
            "g1_g3_language_status": "validated",
            "g4_organization_status": "passed",
            "g5_model_status": "validated",
            "g6_visual_status": "passed",
            "g7_warning_opened": False,
            "all_numbered_figures_dispositioned": True,
            "all_substantive_tables_dispositioned": True,
            "visual_count": len(records),
        },
        "visuals": records,
    }


def validate(record: dict) -> None:
    records = record["visuals"]
    if len(records) != 23:
        raise ValueError(f"expected 14 figures and nine substantive tables, found {len(records)} records")
    figures = [item["figure"] for item in records if item["figure"].startswith("Figure")]
    tables = [item["figure"] for item in records if item["figure"].startswith("Table")]
    if figures != [f"Figure {index}" for index in range(1, 15)]:
        raise ValueError("figure records must exactly cover Figures 1-14 in source order")
    if tables != [f"Table {index}" for index in range(1, 10)]:
        raise ValueError("table records must exactly cover Tables 1-9 in source order")
    if [item["paper_card_visual_index"] for item in records] != list(range(1, 24)):
        raise ValueError("paper-card visual indexes must be contiguous")
    known_models = set(mid(*range(1, 11)))
    required_lists = ("source_model_or_data", "encodings", "axes_units_scales", "color_annotation_layout", "reproducible_construction_procedure", "missing_reproduction_information", "applicability", "forbidden_scenarios", "accessibility_and_interpretability")
    for item in records:
        if not 1 <= item["source_page"] <= 34:
            raise ValueError(f"{item['figure']} source page out of bounds")
        if not set(item["source_model_ids"]) <= known_models:
            raise ValueError(f"{item['figure']} references an unknown q112 model")
        if item["problem_type_applicability"] != [TYPE] or item["disposition"] != "important-visual-record":
            raise ValueError(f"{item['figure']} has an invalid type or disposition")
        for key in required_lists:
            if not item[key]:
                raise ValueError(f"{item['figure']} has an empty required list: {key}")


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    record = build_visuals()
    validate(record)
    STAGE.mkdir(parents=True)
    target = STAGE / "visuals.json"
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"paper_id": PAPER_ID, "visual_records": len(record["visuals"]), "figures": 14, "tables": 9, "proxy_bytes": record["transport_safety"]["total_proxy_bytes"], "stage": str(target), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
