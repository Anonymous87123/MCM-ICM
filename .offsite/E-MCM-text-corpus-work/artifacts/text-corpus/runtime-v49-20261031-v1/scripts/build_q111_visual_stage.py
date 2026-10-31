from __future__ import annotations

"""Build the source-ordered G6 figure and table record for Queue 111."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-39173-b8260835"
TYPE = "B"
YEAR = "2015"
SHORT = "39173"
SHA256 = "b82608352dbbe043cd7092dabcaea179ff110677e0a4598d1f78ad33f956b813"
STAGE = ROOT / "tmp/q111-visual-stage-v1"


def mid(*indexes: int) -> list[str]:
    return [f"MU-{TYPE}-{YEAR}-{SHORT}-{index:03d}" for index in indexes]


# label, page, model indexes, normalized caption, form, purpose, exact supported claim, source status
SPECS = [
    ("Figure 1", 6, (2,), "One standard deviation is the cross-track landing distance produced by a pi/8 glide deviation from the IFP.", "flight-path and glide-deviation geometry diagram", "Explain the physical construction of sigma_x before the normal cross-track density is introduced.", "The paper defines one standard deviation as Gh sin(pi/8); the diagram is a modeling convention rather than observed trajectory validation.", "paper-authored conceptual geometry"),
    ("Figure 2", 7, (3,), "The discretization method shown as an N by 6 search-region matrix; the example has N=4.", "indexed rectangular search-grid diagram", "Make the three positive and three negative sigma bands and N along-track partitions inspectable.", "The continuous field is represented by six cross-track bands and N timed along-track cells, with N=4 only as a diagram example.", "paper-authored model-structure diagram"),
    ("Figure 3", 8, (4,), "Location of a region r_(u,l)=(l,u) relative to the IFP and sigma_x.", "local-coordinate cell-index diagram", "Define the local axes and integer cell references used by the latitude-longitude transform.", "A cell is addressed by along-track partition u and cross-track sigma multiple l before geographic conversion.", "paper-authored coordinate diagram"),
    ("Figure 4", 13, (8,), "f(G) at (x,y_I)=(0.5,0.5), used to illustrate the reported curvature of f(G) and f(theta).", "single response curve", "Show the one-at-a-time response of the density expression to glide/deviation parameters.", "For the fixed demonstration point, the plotted density response decreases rapidly over the displayed parameter range; it does not establish a joint G+theta law.", "paper-authored sensitivity output"),
    ("Figure 5", 13, (5, 8), "POD(theta), with theta in radians.", "single response curve", "Show how wider assumed off-course dispersion changes detection through cell area.", "Under the fixed working-example inputs, the displayed POD drops as theta increases; the curve is conditional on the source detector model.", "paper-authored sensitivity output"),
    ("Figure 6", 14, (5, 8), "POD(G).", "single response curve", "Show the detector response to a larger glide ratio and therefore larger search geometry.", "Under fixed source inputs, the displayed POD decreases as G enlarges the denominator/search area.", "paper-authored sensitivity output"),
    ("Figure 7", 14, (5, 8), "POD(h_s) for 0<=h_s<epsilon.", "single response curve", "Expose the search-altitude effect and the effective-range feasibility boundary.", "The displayed POD decreases as h_s approaches effective instrument range, supporting the paper's low-altitude recommendation inside its geometric detector model.", "paper-authored sensitivity output"),
    ("Figure 8", 15, (5, 8), "POD as search-plane count n varies; the printed caption incorrectly names h_s.", "single response curve", "Show the resource response to synchronized search-plane count.", "Under fixed geometry and instrument assumptions, the displayed POD increases with n; the source caption/prose identify different x variables.", "paper-authored sensitivity output with source-label conflict"),
    ("Figure 9", 18, (9,), "Flight ABCD joint density, showing where POC is largest and smallest.", "three-dimensional probability surface", "Visualize the instantiated cross-track and along-track containment field before cell integration.", "The source's Flight ABCD field is highest near the last-contact/IFP region and declines across the modeled support; exact normalization remains equation-dependent.", "paper-authored worked-example output"),
    ("Figure 10", 19, (9,), "Discretized POC of Flight ABCD.", "three-dimensional cell-probability display", "Show how the continuous joint density becomes 36 regional containment probabilities.", "The example uses six along-track partitions and six cross-track bands, yielding 36 POC cells with nonuniform mass.", "paper-authored worked-example output"),
    ("Figure 11", 19, (9, 10), "Map representation of POC allocated to each Flight ABCD search region.", "plan-view numeric probability grid", "Make region identity and relative POC available to the update/path algorithm.", "The highest initial cells lie near the IFP and earlier along-track region under the source prior; the map is an example input, not an empirical crash map.", "paper-authored worked-example probability map"),
    ("Figure 12", 21, (7, 10), "Search path produced by the neighborhood algorithm in Appendix C.", "ordered route over probability grid", "Show the adjacency-constrained sequence generated after repeated miss-driven POC updates.", "The displayed route usually moves among neighboring cells and permits revisits; one path does not prove global time or fuel optimality.", "paper-authored algorithm output"),
    ("Figure 13", 22, (7, 10), "Search path from a similar algorithm without the adjacency requirement, implemented in Appendix D.", "ordered route over probability grid", "Provide the comparator needed to explain the neighborhood restriction's travel rationale.", "The unrestricted path visibly crosses between reflected high-POC regions more often; the paper supplies no numeric distance/fuel comparison.", "paper-authored comparator output"),
    ("Table 1 (unnumbered)", 19, (9,), "Numeric Flight ABCD POC cell values embedded in the discretized grid/map presentation.", "six-by-six probability matrix", "Retain the numerical cell masses consumed by the POC update loops rather than only the rendered surface.", "The source supplies distinct symmetric POC values for 36 regions, later initialized in Appendix C; rounding and normalization details are not fully reported.", "paper-authored numerical table embedded with worked-example visuals"),
    ("Table 2 (unnumbered)", 23, (4, 10), "Latitude-longitude bounding coordinates for the selected Flight ABCD region from sigma,N=2 to 3.", "four-corner coordinate result table", "Deliver one model-selected cell in operational geographic coordinates.", "The worked example produces four bounding coordinates after applying phi=-0.057939 and the numeric rotation matrix; the table is a handoff, not a geodetic validation.", "paper-authored coordinate output table"),
    ("Table 3 (unnumbered)", 26, (4, 10), "Appendix B Excel input table for the IFP-referenced to latitude-longitude calculation.", "spreadsheet input and intermediate table", "Expose the route, scale, corner, and rotation inputs behind the coordinate result.", "The appendix retains spreadsheet-level inputs/intermediates for the example transform, but the workbook formulas and file are not frozen.", "paper-authored spreadsheet screenshot"),
    ("Table 4 (unnumbered)", 26, (4, 10), "Appendix B Excel transformed-coordinate table.", "spreadsheet calculation/output table", "Expose the numeric multiplication and translation path behind the page-23 corner coordinates.", "The visible table links local corner values to reported geographic outputs; exact cell formulas, order conventions, and precision are not executable from the screenshot alone.", "paper-authored spreadsheet screenshot"),
]


def visual(index: int, spec: tuple) -> dict:
    label, page, model_indexes, caption, form, purpose, claim, source_status = spec
    is_table = label.startswith("Table")
    is_response = "response curve" in form
    return {
        "visual_record_id": f"V-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "paper_card_visual_index": index,
        "source_page": page,
        "printed_page": f"Page {page} of 32",
        "figure": label,
        "caption": caption,
        "analytical_purpose": purpose,
        "source_model_ids": mid(*model_indexes),
        "source_model_or_data": [source_status, "Source equations, scenario inputs, regional probabilities, code outputs, or spreadsheet calculations described in the surrounding section and reconciled on the rendered page."],
        "form": form,
        "encodings": (["Rows and columns encode cell indexes, coordinate components, inputs, intermediates, or outputs.", "Numeric text and cell position carry the payload; borders or shading organize regions but do not add an unreported statistic."] if is_table else ["Position, line, surface height, cell height/color, arrows, path order, or numeric annotation encode the quantity named by the source.", "Figure numbering, nearby prose, and page context establish the model/scenario identity."]),
        "axes_units_scales": ["Spatial diagrams and grids use local miles or indexed cells; coordinate tables use degrees; response plots use the source parameter on x and probability/density on y where labels are visible.", "Absent tick values, exact numeric scales, sigma/region orientation, legend values, or coordinate order remain missing rather than inferred from shape."],
        "normalization": "POC visuals inherit the source joint-density integration and rounded cell values; POD curves inherit the source exponential. Exact normalization, plotting grids, and rounding are retained as missing when not printed.",
        "color_annotation_layout": ["Color, surface height, path lines, arrows, numeric cells, and annotations are recorded only as visually observed and are not converted into unstated values.", "All 32 rendered pages were checked for clipping, overlap, blank/black output, missing pages, and figure/table continuity; no transport or rendering defect was found."],
        "uncertainty": ("The displayed curve is a deterministic one-at-a-time response under fixed working-example parameters; it carries no confidence band, joint uncertainty, calibration error, or field variability." if is_response else "No complete uncertainty encoding is supplied; a conceptual geometry, probability surface, numeric grid, one path, or spreadsheet table must not be read as field calibration or confidence evidence."),
        "exact_claim_supported": claim,
        "reproducible_construction_procedure": ["Use the source-defined scenario, distribution, coordinate frame, cell ordering, detector inputs, update semantics, or code output associated with this record.", "Rebuild the named diagram, curve, surface, matrix, path, or table with direct labels and retain source page and model links.", "Verify the rebuilt visual against the exact bounded claim and do not infer missing coordinates, plot samples, matrix values, or workbook formulas from apparent geometry."],
        "missing_reproduction_information": ["Complete Mathematica notebooks, Excel workbooks, software versions, cell formulas, execution logs, and machine-readable outputs are not supplied.", "Exact plotting samples, curve ranges, surface grids, color maps, path distances, table precision, and geographic conventions are limited to what the source visibly prints.", "The page text extractor omits most raster plot/table labels, so normalized descriptions are source-checked visual records rather than verbatim captions."],
        "problem_type_applicability": [TYPE],
        "applicability": ["Use for missing-object containment, operational grid handoff, detector sensitivity, adaptive cell search, worked-example traceability, or stakeholder explanation only when the receiving variables, units, scenario, uncertainty, and claim are explicit."],
        "forbidden_scenarios": ["Do not treat a conceptual diagram, one sensitivity curve, one POC grid, one path, or a spreadsheet screenshot as field validation, posterior correctness, or global path optimality.", "Do not transfer the visual to another route, aircraft, sensor, weather condition, fleet size, prior, coordinate convention, or drift regime without rebuilding its model and data."],
        "accessibility_and_interpretability": ["Small labels, thin curves, dense cells, and path crossings require a readable print scale or direct-label redesign; color or surface height should not be the sole probability encoding.", "Standalone reuse must state axes/units, scenario, cell indexing, fixed parameters, source status, and the exact supported claim."],
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
            "physical_pages": 32,
            "review_proxy_ranges": ["1-8", "9-16", "17-24", "25-32"],
            "focused_review_pages": ["5", "9", "11", "14-15"],
            "figure_numbers": [f"Figure {index}" for index in range(1, 14)],
            "figure_count": 13,
            "substantive_table_count": 4,
            "non_substantive_table_of_contents_excluded": True,
        },
        "transport_safety": {
            "one_image_per_tool_call": True,
            "max_proxy_bytes": 450000,
            "full_page_original_detail_used": False,
            "context_segments": 1,
            "total_bounded_jpeg_proxies": 8,
            "total_proxy_bytes": 1367613,
            "notes": "Four byte-bounded overview JPEG proxies covered pages 1-32 and four focused proxies reconciled the page-5 distribution, page-9 coordinate transform, page-11 update, and pages-14-15 sensitivity plots. No original full-page PNG or contact sheet entered model context.",
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
    if len(records) != 17:
        raise ValueError(f"expected 13 figures and four substantive tables, found {len(records)} records")
    figures = [item["figure"] for item in records if item["figure"].startswith("Figure")]
    tables = [item["figure"] for item in records if item["figure"].startswith("Table")]
    if figures != [f"Figure {index}" for index in range(1, 14)]:
        raise ValueError("figure records must exactly cover Figures 1-13 in source order")
    if len(tables) != 4:
        raise ValueError("all four substantive numerical/spreadsheet tables must be retained")
    if [item["paper_card_visual_index"] for item in records] != list(range(1, 18)):
        raise ValueError("paper-card visual indexes must be contiguous and source ordered")
    known_models = set(mid(*range(1, 12)))
    required_lists = ("source_model_or_data", "encodings", "axes_units_scales", "color_annotation_layout", "reproducible_construction_procedure", "missing_reproduction_information", "applicability", "forbidden_scenarios", "accessibility_and_interpretability")
    for item in records:
        if not 1 <= item["source_page"] <= 32:
            raise ValueError(f"{item['figure']} source page out of bounds")
        if not set(item["source_model_ids"]) <= known_models:
            raise ValueError(f"{item['figure']} references an unknown q111 model")
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
    print(json.dumps({"paper_id": PAPER_ID, "visual_records": len(record["visuals"]), "figures": 13, "tables": 4, "stage": str(target), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
