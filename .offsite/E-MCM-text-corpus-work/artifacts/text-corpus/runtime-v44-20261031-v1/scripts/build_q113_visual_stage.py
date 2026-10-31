from __future__ import annotations

"""Build the source-ordered G6 figure and table record for Queue 113."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2016-42745-4dc9ed2b"
TYPE = "B"
YEAR = "2016"
SHORT = "42745"
SHA256 = "4dc9ed2b48ba9415c26b12506e36e0a144491324a4f44445d6ae8083ad7c5b46"
STAGE = ROOT / "tmp/q113-visual-stage-v1"


def mid(*indexes: int) -> list[str]:
    return [f"MU-{TYPE}-{YEAR}-{SHORT}-{index:03d}" for index in indexes]


# label, physical page, model indexes, normalized caption, form, purpose, exact claim, source status
SPECS = [
    ("Unnumbered Summary Figure", 2, (4, 5, 6), "Simulation Space Debris Distribution.", "low-contrast annular debris scatter plot", "Preview the synthetic field before the executive summary compares removal alternatives.", "The page shows a ring-shaped simulated distribution on axes running roughly 0-1000; it is an unnumbered model illustration, not observed orbital data.", "paper-authored synthetic simulation output"),
    ("Unnumbered Notation Table", 8, (1, 2, 3, 4, 5, 6, 9), "Notations.", "symbol-definition table", "Expose the financial, probability, debris, removal, and policy interfaces used later.", "The rendered table clearly defines N_t, R_t, C_t, N_T, n_t, w, alpha, C_1t, C_2t, p_t, q_t, Pr(t), delta, Q_t, and epsilon; most symbols are corrupted in text extraction.", "paper-authored notation table"),
    ("Figure 1", 13, (4,), "NASA debris spatial-density curve by height.", "cited height-density line chart", "Provide empirical-looking radial context for the Gamma representation.", "The cited NASA curve varies debris density with altitude and motivates a radial model; it does not supply the paper's Gamma parameters or a filtered 1-10 cm calibration dataset.", "third-party NASA chart reproduced with citation"),
    ("Figure 2", 13, (4,), "Gamma probability density function.", "Gamma-family density curve", "Show a qualitative family shape for comparison with the NASA altitude curve.", "The curve supports only a visual-shape analogy; alpha_G, beta_G, estimation data, and goodness of fit are absent.", "paper-authored standard-distribution illustration"),
    ("Figure 3", 13, (4,), "NASA image of debris surrounding Earth.", "three-dimensional orbital debris visualization", "Establish that the physical system is spatially three-dimensional before reduction.", "The cited visualization shows orbital debris around Earth; it is contextual and does not validate the paper's two-dimensional binary field.", "third-party NASA visualization reproduced with citation"),
    ("Figure 4", 13, (4,), "Spatial Gamma P.D.F.", "annular heat map with color bar", "Translate the radial Gamma family into a two-dimensional spatial intensity pattern.", "The heat map preserves a ring-shaped radial representation and excluded central region; scale, parameters, and probability normalization are not reproducible from the figure.", "paper-authored model representation"),
    ("Figure 5", 14, (4,), "Simulated space debris distribution.", "1000 by 1000 annular binary scatter field", "Show the random field used by annual removal, growth, and collision operations.", "The field is a hand-set approximately 15-percent binary occupancy realization; faint points and missing seed information prevent exact reconstruction.", "paper-authored synthetic simulation output"),
    ("Figure 6", 16, (6,), "The Amount of Satellites launched.", "2001-2015 annual launch-count line chart", "Supply historical launch context before projecting n_1=110 with five-percent annual growth.", "The Space-Track series supports time variation in annual launches; the source does not fit or validate the later five-percent recurrence from the plotted data.", "paper-authored chart using cited Space-Track data"),
    ("Figure 7", 17, (1, 5, 7), "The Profits v.s. the Number of Debris remaining, land alternative.", "dual-series profit and debris chart", "Align accumulated profit with remaining debris for land-only removal.", "The chart shows a blue accumulated-profit series and orange dashed debris-left series over the common horizon; the paper interprets an early loss period and limited net debris growth without uncertainty bands.", "paper-authored scenario output"),
    ("Figure 8", 17, (4, 5, 7), "Ending debris distribution, land alternative.", "annular debris scatter field", "Show the spatial ending state for land-only removal.", "The ending synthetic field visually retains substantial debris outside the land working band; no machine-readable array, seed, or replicate range is supplied.", "paper-authored synthetic scenario output"),
    ("Figure 9", 18, (1, 5, 7), "Profits and remaining debris, space alternative.", "dual-series profit and debris chart", "Align accumulated profit with remaining debris for space-only removal.", "The chart supports the source's claim of favorable finances but later inner-layer debris growth; this is one unreported stochastic run protocol rather than a distribution of outcomes.", "paper-authored scenario output"),
    ("Figure 10", 18, (4, 5, 7), "Ending debris distribution, space alternative.", "annular debris scatter field", "Show the spatial ending state for space-only removal.", "The field indicates uneven control across radial layers and supports the qualitative altitude-band tradeoff only within the paper's binary grid.", "paper-authored synthetic scenario output"),
    ("Figure 11", 18, (1, 5, 7), "Profits and remaining debris, combined alternative.", "dual-series profit and debris chart", "Compare combined removal on the same financial and environmental axes.", "The chart is the principal visual support for the combined recommendation and reported near-16-billion accumulated profit; exact yearly arrays and uncertainty are absent.", "paper-authored scenario output"),
    ("Figure 12", 18, (4, 5, 7), "Ending debris distribution, combined alternative.", "annular debris scatter field", "Show the ending spatial state when both removal bands operate.", "The combined field is visually sparser and supports the reported removal of more than 2000 debris only under the paper's occupancy and update rules.", "paper-authored synthetic scenario output"),
    ("Figure 13", 19, (5, 8), "Ending debris distribution at four-percent growth.", "annular growth-scenario field", "Show the combined alternative under a lower debris-growth setting.", "The source reports 9,932 ending debris at four-percent growth versus 12,302 at the five-percent baseline; the field is a local scenario, not a policy forecast.", "paper-authored synthetic sensitivity output"),
    ("Figure 14", 19, (5, 8), "Ending debris distribution at three-percent growth.", "annular growth-scenario field", "Continue the growth-policy comparison.", "The source reports 8,004 ending debris at three-percent growth; the figure has no uncertainty, implementation-cost, or compliance model.", "paper-authored synthetic sensitivity output"),
    ("Figure 15", 20, (5, 8), "Ending debris distribution at two-percent growth.", "annular growth-scenario field", "Show the strongest percentage-growth control scenario.", "The source reports 6,374 ending debris; the printed claim that the decrease from 8,004 is 1,670 conflicts with the arithmetic difference of 1,630.", "paper-authored synthetic sensitivity output"),
    ("Figure 16", 20, (5, 8), "Ending debris distribution under logarithmic growth.", "annular logarithmic-growth field", "Compare a different growth-function family with the percentage cases.", "The source reports 5,313 ending debris under its unspecified logarithmic trend; no equation, fitted parameters, or empirical scenario likelihood is printed.", "paper-authored synthetic sensitivity output"),
    ("Figure 17", 21, (2, 8), "Accumulated Profits_lifetime_3.", "15-year accumulated-profit line chart", "Record the reusable-rocket scenario at three uses.", "The figure supplies one profit trajectory when rocket lifetime is set to three; all other costs and stochastic settings are unreported but treated as fixed.", "paper-authored deterministic scenario output"),
    ("Figure 18", 21, (2, 8), "Accumulated Profits_lifetime_6.", "15-year accumulated-profit line chart", "Record the reusable-rocket scenario at six uses.", "The six-use path is one point in a four-level local technology sweep and does not establish a calibrated lifetime distribution.", "paper-authored deterministic scenario output"),
    ("Figure 19", 21, (2, 8), "Accumulated Profits_lifetime_9.", "15-year accumulated-profit line chart", "Record the reusable-rocket scenario at nine uses.", "The nine-use path contributes to the reported small profit sensitivity relative to compensation liability; exact arrays are absent.", "paper-authored deterministic scenario output"),
    ("Figure 20", 21, (2, 8), "Accumulated Profits_lifetime_12.", "15-year accumulated-profit line chart", "Record the reusable-rocket scenario at twelve uses.", "Across Figures 17-20 the source reports a maximum-minimum difference of 15.4 percent of total profit and 0.38 billion per additional use, conditional on its cost model.", "paper-authored deterministic scenario output"),
    ("Figure 21", 22, (1, 3, 8), "Accumulated profits at alpha=6 percent.", "15-year accumulated-profit line chart", "Show the high end of the insurance-rate sweep.", "The six-percent path is the most favorable of the four displayed rate cases under fixed demand and exposure assumptions.", "paper-authored deterministic sensitivity output"),
    ("Figure 22", 22, (1, 3, 8), "Accumulated profits at alpha=5 percent.", "15-year accumulated-profit line chart", "Support the source's preferred stable commission range.", "The five-percent path is used to recommend rates at or above five percent, but no demand response, competition, or payout calibration is modeled.", "paper-authored deterministic sensitivity output"),
    ("Figure 23", 22, (1, 3, 8), "Accumulated profits at alpha=4 percent.", "15-year accumulated-profit line chart", "Show the claimed minimum feasible commission case.", "The four-percent path is interpreted as breaking even after an early loss period; the threshold is local to four discrete rates and fixed unreported inputs.", "paper-authored deterministic sensitivity output"),
    ("Figure 24", 22, (1, 3, 8), "Accumulated profits at alpha=3 percent.", "15-year accumulated-profit line chart", "Show the low-rate boundary case.", "The plotted path is negative for roughly the first nine years, contradicting the prose phrase 'enjoy net income in the first 9 years'; the figure supports an early-loss interpretation.", "paper-authored deterministic sensitivity output"),
    ("Unnumbered Payoff Matrix 1", 23, (9,), "Baseline owner-firm payoff matrix.", "3 by 3 bimatrix table", "Expose both players' payoffs and pure best responses before policy.", "Best-response inspection confirms two pure equilibria: half insured/remove considerably at (-21,-8.4) and fully insured/remove some at (-27,-11.7); payoff derivation and units are absent.", "paper-authored strategic payoff table"),
    ("Unnumbered Payoff Matrix 2", 23, (9,), "Policy-adjusted owner-firm payoff matrix.", "3 by 3 bimatrix table", "Show the policy-induced payoff changes and new best-response intersection.", "The unique pure equilibrium is half insured/remove considerably at (-19.5,-3.3), which improves both displayed player payoffs relative to either baseline equilibrium within the supplied matrices.", "paper-authored strategic payoff table"),
]


def visual(index: int, spec: tuple) -> dict:
    label, page, model_indexes, caption, form, purpose, claim, source_status = spec
    is_table = "Table" in label or "Matrix" in label
    is_sensitivity = "sensitivity" in form or "scenario" in form
    return {
        "visual_record_id": f"V-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "paper_card_visual_index": index,
        "source_page": page,
        "printed_page": f"Physical PDF page {page} of 26",
        "figure": label,
        "caption": caption,
        "analytical_purpose": purpose,
        "source_model_ids": mid(*model_indexes),
        "source_model_or_data": [source_status, "Surrounding formulas, assumptions, scenario settings, cited data, or payoff text were reconciled with the rendered page and the complete extracted text."],
        "form": form,
        "encodings": (["Rows and columns encode symbols, definitions, player strategies, payoff pairs, or scenario identities.", "Numeric cells, ordered strategies, and labels carry the evidence; missing units or derivations are not inferred from layout."] if is_table else ["Position, radial band, occupancy point, line, column, color, marker, or panel title encodes the source quantity or scenario.", "Caption and surrounding prose establish whether the visual is cited context, standard-family illustration, synthetic field, financial result, or sensitivity output."]),
        "axes_units_scales": ["Grid plots use approximately 0-1000 coordinates; financial plots use years and billions where printed; debris plots use counts; rates and lifetimes use their stated scenario values.", "Faint small labels, missing arrays, color scales, exact ticks, probability normalization, and coordinate-to-altitude mapping remain missing rather than inferred."],
        "normalization": "Profit/debris charts and fields inherit the source simulation; Gamma visuals inherit an unspecified family and ring allocation; payoff matrices use printed pairs. No unprinted normalization, interpolation, confidence interval, or statistic is manufactured.",
        "color_annotation_layout": ["Blue bars or lines, orange dashed lines, annular point fields, color bars, and payoff-cell annotations are retained only at the level required for the supported claim.", "All 26 rendered pages were reviewed; formula and notation fidelity on pages 8-11 received a focused crop review, and page-level review found no clipping, overlap, black output, missing page, or rendering damage."],
        "uncertainty": ("This is a local deterministic or synthetic scenario output with no confidence interval, replicate distribution, joint perturbation, calibrated error, or out-of-sample test." if is_sensitivity else "No complete uncertainty encoding is supplied; cited context, a standard curve, a synthetic field, one plotted path, or a payoff table must not be read as calibration or real-world validation."),
        "exact_claim_supported": claim,
        "reproducible_construction_procedure": ["Use the source-defined field, formula, scenario, launch path, removal alternative, commission, lifetime, or payoff matrix associated with this record.", "Rebuild the named chart, field, table, or matrix with direct labels, physical-page provenance, model links, and the same evidence class.", "Verify only the bounded claim and do not infer missing arrays, seeds, Gamma parameters, cell scale, cost inputs, payoff derivation, or uncertainty from apparent geometry."],
        "missing_reproduction_information": ["Complete model inputs, Gamma fit, grid mapping, random seeds and repetitions, MATLAB version and code, annual arrays, and raw plotting data are not supplied.", "Cost calibration, currency year, launch distribution, collision geometry, policy implementation, payoff derivation, and uncertainty propagation remain incomplete.", "Normalized descriptions are source-checked visual records; they do not invent values or labels absent from the rendered source."],
        "problem_type_applicability": [TYPE],
        "applicability": ["Use for commercial-opportunity, intervention-comparison, stochastic-field, one-factor scenario, or strategic-policy work only when definitions, data, units, uncertainty, and decision scope are rebuilt."],
        "forbidden_scenarios": ["Do not treat a cited image, Gamma resemblance, synthetic occupancy field, smooth profit path, ending scatter plot, four-point sweep, or asserted payoff matrix as empirical calibration, prediction, global robustness, or social-welfare proof.", "Do not transfer the visual to another debris population, orbit geometry, technology, price regime, insurance market, policy, time horizon, or payoff system without rebuilding its inputs."],
        "accessibility_and_interpretability": ["Several scatter fields and scenario charts use faint lines and small labels; reuse requires readable scale, direct labeling, and redundant series encoding.", "Standalone reuse must state axes and units, scenario, fixed inputs, source status, uncertainty boundary, and the exact supported claim."],
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
            "physical_pages": 26,
            "review_proxy_ranges": ["all pages 1-26 through seven bounded page-group JPEG proxies"],
            "focused_review_pages": ["8-11 formula and notation crop"],
            "figure_numbers": [f"Figure {index}" for index in range(1, 25)],
            "figure_count": 24,
            "unnumbered_figure_count": 1,
            "substantive_table_numbers": ["Unnumbered Notation Table", "Unnumbered Payoff Matrix 1", "Unnumbered Payoff Matrix 2"],
            "substantive_table_count": 3,
            "non_substantive_table_of_contents_excluded": True,
        },
        "transport_safety": {
            "one_image_per_tool_call": True,
            "max_proxy_bytes": 450000,
            "observed_max_proxy_bytes": 448554,
            "full_page_original_detail_used": False,
            "context_segments": 1,
            "review_executor": "fresh read-only subagent; root received text report only",
            "total_bounded_jpeg_proxies": 8,
            "total_proxy_bytes": 3096688,
            "notes": "Seven byte-bounded page-group JPEG proxies covered all 26 pages and one focused crop reconciled pages 8-11 notation and formulas. The subagent inspected one proxy per call and reported only text; no original full-page PNG, original-detail contact sheet, multi-image tool result, or complete session JSONL entered the root context.",
        },
        "gate_attestation": {
            "g1_g3_language_status": "validated",
            "g4_organization_status": "passed",
            "g5_model_status": "validated",
            "g6_visual_status": "passed",
            "g7_warning_opened": False,
            "all_numbered_figures_dispositioned": True,
            "all_substantive_tables_dispositioned": True,
            "all_unnumbered_analytical_visuals_dispositioned": True,
            "visual_count": len(records),
        },
        "visuals": records,
    }


def validate(record: dict) -> None:
    records = record["visuals"]
    if len(records) != 28:
        raise ValueError(f"expected 24 figures, one unnumbered figure, and three substantive tables, found {len(records)} records")
    figures = [item["figure"] for item in records if item["figure"].startswith("Figure")]
    if figures != [f"Figure {index}" for index in range(1, 25)]:
        raise ValueError("figure records must exactly cover Figures 1-24 in source order")
    if [item["paper_card_visual_index"] for item in records] != list(range(1, 29)):
        raise ValueError("paper-card visual indexes must be contiguous")
    known_models = set(mid(*range(1, 11)))
    required_lists = ("source_model_or_data", "encodings", "axes_units_scales", "color_annotation_layout", "reproducible_construction_procedure", "missing_reproduction_information", "applicability", "forbidden_scenarios", "accessibility_and_interpretability")
    for item in records:
        if not 1 <= item["source_page"] <= 26:
            raise ValueError(f"{item['figure']} source page out of bounds")
        if not set(item["source_model_ids"]) <= known_models:
            raise ValueError(f"{item['figure']} references an unknown q113 model")
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
    print(json.dumps({"paper_id": PAPER_ID, "visual_records": len(record["visuals"]), "figures": 24, "unnumbered_figure": 1, "tables": 3, "proxy_bytes": record["transport_safety"]["total_proxy_bytes"], "stage": str(target), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
