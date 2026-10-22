from __future__ import annotations

"""Build the source-ordered G6 figure and table record for Queue 110."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-38720-26d38781"
TYPE = "B"
YEAR = "2015"
SHORT = "38720"
SHA256 = "26d38781a179b71806799b0d20f118a5f0b09aa1cf6b8bc7a5e32562a7886a42"
STAGE = ROOT / "tmp/q110-visual-stage-v1"


def mid(*indexes: int) -> list[str]:
    return [f"MU-{TYPE}-{YEAR}-{SHORT}-{index:03d}" for index in indexes]


# label, page, model indexes, normalized caption, form, purpose, exact supported claim, source status
SPECS = [
    ("Figure 1", 7, (2,), "Search Area of Malaysia Flight MH370.", "annotated regional search map", "Ground the candidate-region discussion in the published MH370 search geometry and final satellite arc.", "A large open-ocean aircraft search can be bounded around a last-known path/arc for modeling, but this map does not validate the paper's rectangle.", "third-party map reproduced with citation"),
    ("Figure 2", 8, (11,), "Total Missing Aircraft.", "world route map with categorical summary charts", "Show the historical geographic and aircraft-type scope used to choose a representative ocean scenario.", "The source compilation contains many unresolved aircraft cases and motivates studying an Atlantic open-ocean setting; it is contextual rather than a calibrated sample.", "third-party infographic reproduced with citation"),
    ("Table 1 (unnumbered)", 13, (2, 3), "Lost Plane Variables.", "two-column notation table", "Define lost-aircraft timing, glide, path, and search-domain symbols before equations are introduced.", "The paper explicitly defines v, alpha, T, failure, A-prime, r, kappa, tau, B-prime, L, and endpoints A/B.", "paper-authored notation table"),
    ("Table 2 (unnumbered)", 14, (3, 4, 5, 6, 7, 8, 9), "Search Variables.", "two-column notation table", "Define search-plane, sensor, crash-point, path-state, direction, endpoint-distance, and iteration notation.", "The route equations depend on v_s, d, a, t, l, Z, crash coordinates, S, epsilon, d_A, d_B, j, and u, although later notation is not fully consistent.", "paper-authored notation table"),
    ("Figure 3", 15, (2,), "Diagram of Search Area.", "local-coordinate geometry diagram", "Construct the rectangular search domain from the uncertain flight segment and two glide-radius endpoint circles.", "The enclosing rectangle has dimensions (L+2r) by 2r around points A, A-prime, B-prime, and B.", "paper-authored geometry diagram"),
    ("Table 3 (unnumbered)", 16, (2, 11), "Potential lost-aircraft specifications.", "three-aircraft comparison table", "Compare Boeing 777, Gulfstream G450, and Cessna 172 inputs and select the B777 baseline.", "The selected B777 values are 640 mph, 35,000 ft, 15:1 glide, r=100 mi, L=320 mi, and 104,000 square miles.", "paper-authored specification comparison using cited values"),
    ("Figure 4", 17, (3,), "Realistic Distributed Search Area.", "two-dimensional crash-location scatter", "Show a richer path-and-endpoint containment pattern before replacing it with a tractable distribution.", "A physically richer prior would concentrate near the path and thin around endpoint regions, so a uniform field is not the intended baseline.", "paper-authored conceptual simulation figure"),
    ("Figure 5", 17, (3,), "Normally Distributed 3-D Graph.", "three-dimensional probability surface", "Visualize the simplified prior that is uniform along the flight direction and Gaussian across it.", "The paper's tractable containment field is constant in x and normally distributed in y within the bounded domain.", "paper-authored probability-surface figure"),
    ("Figure 6", 18, (1, 3), "Figure 6.", "generic radar-screen image", "Provide sensor context beside the P-8/P-3 radar discussion.", "The image supports only that radar is the assumed sensing modality; it carries no model parameter or quantitative validation.", "third-party illustrative image with no descriptive caption"),
    ("Table 4 (unnumbered)", 18, (3, 11), "Search-aircraft and sensor specifications.", "two-aircraft comparison table", "Compare P-3 and P-8 search resources and fix the P-8 simulation baseline.", "The chosen P-8 values are 400 mph, AN/APS-119 radar, 1,000 ft search altitude, and a 10-mile sight radius.", "paper-authored specification comparison using cited values"),
    ("Figure 7", 22, (3,), "Five thousand normally distributed simulated crash locations.", "two-dimensional point cloud in search rectangle", "Check that the crash sampler follows the selected center-weighted containment field.", "Five thousand simulated points concentrate around the flight-path axis inside the rectangular support.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 8", 24, (4,), "Random-vector construction for the completely random route.", "vector construction diagram", "Explain how a random vector is normalized to generate one route increment.", "The unbounded baseline uses fixed-length steps with randomly selected directions.", "paper-authored algorithm diagram; caption normalized from visual QA"),
    ("Figure 9", 25, (4,), "Example completely random search path.", "route trace over search rectangle", "Show why an unconstrained random walk can leave the probability field and fail to finish.", "The example path spends substantial effort outside the bounded search region; it is illustrative, not a completion-rate estimate.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 10", 27, (5,), "Bounded-vector redirection rule.", "boundary vector diagram", "Explain the horizontal and vertical center-return vectors used after a boundary crossing.", "The bounded route replaces an out-of-domain increment with a direction toward the rectangle's center axis.", "paper-authored algorithm diagram; caption normalized from visual QA"),
    ("Figure 11", 27, (5,), "Example bounded-random search path.", "route trace over search rectangle", "Show the boundary-corrected random route remaining inside the candidate domain.", "Boundary correction contains the route but does not impose probability-aware coverage.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 12", 28, (5,), "Bounded-random discovery-time histogram.", "histogram with summary statistics", "Expose the highly right-skewed distribution of bounded-random completion times.", "For 100 trials the paper reports median 24.425 h and mean 42.7105 h with interval [33.2348,52.1862].", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 13", 29, (6,), "Endpoint-weighted random-vector construction.", "vector construction diagram", "Show how a random direction and a farther-endpoint direction are combined.", "The route adds a fixed weight-15 endpoint bias before normalizing the next step.", "paper-authored algorithm diagram; caption normalized from visual QA"),
    ("Figure 14", 30, (6,), "Example weighted bounded-random path.", "route trace over search rectangle", "Show a stochastic route biased toward the path endpoints and central probability band.", "The weighted route remains exploratory while shifting coverage toward selected geometry; one trace does not establish faster expected discovery.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 15", 31, (6,), "Weighted bounded-random discovery-time histogram.", "histogram with summary statistics", "Compare weighted-random time shape with the prior random baselines.", "For 100 trials the paper reports median 16.6 h and mean 37.5575 h; its interval overlaps the bounded-random interval.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 16", 33, (7,), "Descending-stripe construction.", "boustrophedon path diagram", "Explain center-start horizontal stripes that descend by one radar diameter at each turn.", "The path provides systematic coverage but orders one side of the symmetric prior before the other.", "paper-authored algorithm diagram; caption normalized from visual QA"),
    ("Figure 17", 33, (7,), "Example descending-stripe trial.", "route trace with crash marker", "Show a simulated discovery along the deterministic descending-stripe route.", "The route covers adjacent horizontal bands without random wandering; the example alone is not a distributional comparison.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 18", 34, (7,), "Descending-stripe discovery-time histogram.", "histogram with summary statistics", "Summarize systematic-stripe discovery times under ideal detection.", "For 100 trials the paper reports median 7.031 h and mean 7.10273 h with interval [6.62073,7.58473].", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 19", 36, (8,), "Spiral-stripe center-out construction.", "alternating stripe path diagram", "Explain how alternating center-out stripe order targets the highest Gaussian mass first.", "The route alternates above and below the path center rather than sweeping monotonically through the tails.", "paper-authored algorithm diagram; caption normalized from visual QA"),
    ("Figure 20", 36, (8,), "Example spiral-stripe trial.", "route trace with crash marker", "Show a simulated discovery along the center-out alternating route.", "The example makes the center-first sequence legible but cannot establish its mean without the trial distribution.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 21", 37, (8,), "Ideal spiral-stripe discovery-time histogram.", "histogram with summary statistics", "Summarize the paper's strongest ideal one-plane route.", "For 100 trials the paper reports median 3.113 h and mean 3.62286 h with interval [3.05261,4.19311].", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 22", 39, (9,), "Sinusoidal-stripe construction.", "sinusoidal path diagram", "Explain the tangent-stepped sine route and alternating vertical transitions.", "The path replaces straight stripes with waves of stated amplitude d and wavelength 2d, subject to ambiguous transition notation.", "paper-authored algorithm diagram; caption normalized from visual QA"),
    ("Figure 23", 39, (9,), "Example sinusoidal search trial.", "route trace with crash marker", "Show one simulated discovery on the sinusoidal center-out route.", "The sinusoidal trace remains systematic but is longer and more notation-dependent than straight spiral stripes.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 24", 40, (9,), "Sinusoidal discovery-time histogram.", "histogram with summary statistics", "Summarize ideal-detection performance of the sinusoidal alternative.", "For 100 trials the paper reports median 4.489 h and mean 6.44989 h with interval [5.23314,7.66664].", "paper-authored simulation output; caption normalized from visual QA"),
    ("Table 5 (unnumbered)", 41, (10,), "Discovery-uncertainty variables.", "two-column notation table", "Define radar, operator, total discovery, searched-cell, and alternative-cell probabilities before Bayesian updating.", "The Bayesian layer uses P(D_u), P(R), P(O), P(O|R), P(C), and P(C_i), but does not define cell dimensions.", "paper-authored notation table"),
    ("Figure 25", 44, (10,), "Initial three-dimensional containment prior.", "three-dimensional probability surface", "Show the initial Gaussian cross-track and uniform along-track grid before any search pass.", "Initial mass is concentrated near the flight path and serves as the Bayesian search priority field.", "paper-authored posterior-grid visualization; caption normalized from visual QA"),
    ("Figure 26", 44, (10,), "Initial two-dimensional containment prior.", "two-dimensional probability heat map", "Provide a plan-view counterpart to the three-dimensional prior.", "The heat map makes high-probability center cells available for route selection, without declaring the grid resolution.", "paper-authored posterior-grid visualization; caption normalized from visual QA"),
    ("Figure 27", 44, (10,), "Posterior after an unsuccessful center pass.", "two-dimensional probability heat map with candidate paths", "Show how a missed central search depresses visited probability and shifts the next priorities to y=+/-20 miles.", "Equations 19-20 move relative mass away from the searched center stripe after a miss.", "paper-authored posterior-grid visualization; caption normalized from visual QA"),
    ("Figure 28", 45, (10,), "Posterior after the second unsuccessful pass.", "two-dimensional probability heat map with next target", "Continue the adaptive update and identify the next most probable stripe.", "Sequential misses change route order through posterior mass rather than a fixed spiral schedule.", "paper-authored posterior-grid visualization; caption normalized from visual QA"),
    ("Figure 29", 46, (10,), "Bayesian B777 discovery-time histogram.", "histogram with completion annotation", "Summarize adaptive-search times among successful trials and report the 24-hour completion proportion.", "The run finds 475/500 targets; among successes it reports median 4.05 h and mean 6.21463 h, with a flawed lower CI bound.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 30", 47, (10,), "Uncertain spiral B777 discovery-time histogram.", "histogram with completion annotation", "Compare the fixed spiral path under the same imperfect-discovery setting.", "The run finds 399/500 targets; among successes it reports median 4.05 h and mean 4.76078 h, so completion and conditional time must be read together.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 31", 49, (10, 11), "Bayesian Cessna 172 discovery-time histogram.", "histogram with completion annotation", "Check limited target-size and search-area transfer for the Bayesian route.", "The C172 run finds 411/500 targets and reports a conditional mean of 8.38549 h, but the 2-percent detection scaling is uncalibrated.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 32", 51, (7, 11), "Example two-plane striped search.", "two-route spatial trace", "Show how two aircraft divide systematic stripe coverage.", "Splitting the stripe plan between two search planes reduces simulated completion time under the same idealized coordination assumptions.", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 33", 52, (7, 11), "Two-plane stripe discovery-time histogram.", "histogram with summary statistics", "Summarize the resource extension from one to two search aircraft.", "For 100 trials the paper reports median 2.1435 h and mean 2.39551 h with interval [2.11644,2.67458].", "paper-authored simulation output; caption normalized from visual QA"),
    ("Figure 34", 53, (11,), "Random-solution confidence-interval comparison.", "interval comparison plot", "Compare the bounded and weighted random-route mean intervals.", "The plotted intervals overlap under the paper's approximation; this supports descriptive overlap only, not a formal no-difference conclusion.", "paper-authored comparison plot; caption normalized from visual QA"),
    ("Figure 35", 53, (11,), "Nonrandom-solution confidence-interval comparison.", "interval comparison plot", "Place systematic ideal-route intervals on a common visual scale.", "The ideal spiral interval is lowest among the one-plane systematic routes in the paper's simulation harness.", "paper-authored comparison plot; caption normalized from visual QA"),
    ("Figure 36", 54, (10, 11), "Discovery-uncertainty confidence-interval comparison.", "interval comparison plot", "Compare conditional successful-trial times for Bayesian and fixed spiral routes under imperfect discovery.", "The conditional Bayesian interval is higher while its completion proportion is 95 percent versus 80 percent, so interval height alone cannot select the route.", "paper-authored comparison plot; caption normalized from visual QA"),
    ("Figure 37", 56, (11,), "Cold-water survival curve.", "external survival probability curve", "Relate modeled discovery times to the recommendation's 18-hour rescue benchmark.", "Shorter searches are decision-relevant because survival declines with cold-water exposure, but the external curve is not integrated into the simulation objective.", "third-party survival curve reproduced with citation"),
]


def visual(index: int, spec: tuple) -> dict:
    label, page, model_indexes, caption, form, purpose, claim, source_status = spec
    is_table = label.startswith("Table")
    is_distribution = "histogram" in form or "interval" in form
    is_external = source_status.startswith("third-party")
    return {
        "visual_record_id": f"V-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "paper_card_visual_index": index,
        "source_page": page,
        "printed_page": f"Page {page} of 61",
        "figure": label,
        "caption": caption,
        "analytical_purpose": purpose,
        "source_model_ids": mid(*model_indexes),
        "source_model_or_data": [
            source_status,
            "Source parameters, simulated outputs, or cited context described in the surrounding section and visually reconciled on the rendered page.",
        ],
        "form": form,
        "encodings": (
            ["Rows encode variables or aircraft classes and columns encode definitions or compared specifications.", "Text, symbols, units, and numeric cells carry the analytical payload; emphasis marks selected baselines."]
            if is_table
            else ["Position, path geometry, point density, bars, intervals, surface height, or color encode the source quantity appropriate to this visual.", "Figure numbering and nearby prose establish route, prior, scenario, or comparison identity."]
        ),
        "axes_units_scales": [
            "Spatial plots use the paper's local mile-scale rectangle where axes are shown; time distributions and intervals use hours; probability views use relative mass or probability.",
            "Any absent tick labels, grid resolution, bin boundaries, coordinate reference, or numeric legend remain missing rather than inferred from apparent geometry.",
        ],
        "normalization": "Probability maps and distributions use the paper's stated simulation summaries; exact grid, density, bin, and posterior normalization details are retained as missing when not printed.",
        "color_annotation_layout": [
            "Color, line, bar, point, panel, and annotation roles are recorded only as visually observed and are not converted into unstated numeric values.",
            "The rendered page was checked for clipping, overlap, blank output, missing glyphs, and figure/table continuity; none of those transport defects was found.",
        ],
        "uncertainty": (
            "The source reports sampling spread or approximate intervals, but the visual does not encode failure censoring, parameter uncertainty, seed variation, or field calibration."
            if is_distribution
            else "No complete uncertainty encoding is supplied; conceptual geometry, one route trace, a notation table, or a contextual external image must not be read as a confidence statement."
        ),
        "exact_claim_supported": claim,
        "reproducible_construction_procedure": [
            "Use the source-defined model, scenario, variables, units, route order, trial population, and displayed summary appropriate to the record.",
            "Rebuild the declared diagram, table, trace, distribution, map, or posterior view with direct labels and retain the source page and model links.",
            "Verify the rebuilt visual against the recorded claim and do not use apparent geometry to fill missing numeric specifications.",
        ],
        "missing_reproduction_information": [
            "Executable plotting/simulation code, software version, random seed, raw trial table, and exact styling are not supplied by the paper.",
            "Some figure captions are only numbered in the raster/extraction; descriptive wording here is normalized from bounded visual QA rather than represented as a verbatim quotation.",
            "External source bytes and licensing are not frozen with the paper." if is_external else "Exact coordinates, bins, grid resolution, numeric annotations, or table-source transforms remain limited to what the source visibly prints.",
        ],
        "problem_type_applicability": [TYPE],
        "applicability": [
            "Use for bounded spatial-search explanation, route comparison, probability updating, simulation diagnostics, or decision communication when the same variables and estimands are explicit.",
        ],
        "forbidden_scenarios": [
            "Do not treat a contextual image, one simulated path, histogram, approximate interval, or selected specification table as field validation or universal route optimality.",
            "Do not transfer results to different target sizes, sensors, priors, weather, search areas, aircraft counts, time caps, or failure handling without rebuilding the model and visual.",
        ],
        "accessibility_and_interpretability": [
            "Small labels and thin marks require a readable print scale or direct-label redesign; color should not be the only method or probability encoding.",
            "Standalone reuse must state units, scenario, trial denominator, treatment of failures, source status, and the exact bounded claim.",
        ],
        "disposition": "important-visual-record",
        "evidence_role": "important-positive-record" if not is_external else "bounded-context-record",
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
            "physical_pages": 61,
            "review_proxy_ranges": ["1-4", "5-8", "9-12", "13-16", "17-21", "22-25", "26-29", "30-33", "34-37", "38-41", "42-45", "46-49", "50-53", "54-57", "58-61"],
            "figure_numbers": [f"Figure {index}" for index in range(1, 38)],
            "figure_count": 37,
            "substantive_table_count": 5,
            "non_substantive_table_of_contents_excluded": True,
        },
        "transport_safety": {
            "one_image_per_tool_call": True,
            "max_proxy_bytes": 450000,
            "full_page_original_detail_used": False,
            "context_segments": 3,
            "total_bounded_jpeg_proxies": 18,
            "notes": "All 61 pages were covered through byte-bounded JPEG review proxies in fresh contexts; focused formula review was text-only on return. No full PDF-page PNG or contact sheet was returned with original detail.",
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
    if len(records) != 42:
        raise ValueError(f"expected 37 figures and five tables, found {len(records)} records")
    figures = [item["figure"] for item in records if item["figure"].startswith("Figure")]
    tables = [item["figure"] for item in records if item["figure"].startswith("Table")]
    if figures != [f"Figure {index}" for index in range(1, 38)]:
        raise ValueError("figure records must exactly cover Figures 1-37 in source order")
    if len(tables) != 5:
        raise ValueError("all five substantive unnumbered tables must be retained")
    if [item["paper_card_visual_index"] for item in records] != list(range(1, 43)):
        raise ValueError("paper-card visual indexes must be contiguous and source ordered")
    known_models = set(mid(*range(1, 12)))
    required_lists = (
        "source_model_or_data", "encodings", "axes_units_scales", "color_annotation_layout",
        "reproducible_construction_procedure", "missing_reproduction_information", "applicability",
        "forbidden_scenarios", "accessibility_and_interpretability",
    )
    for item in records:
        if not 1 <= item["source_page"] <= 61:
            raise ValueError(f"{item['figure']} source page out of bounds")
        if not set(item["source_model_ids"]) <= known_models:
            raise ValueError(f"{item['figure']} references an unknown q110 model")
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
    print(json.dumps({"paper_id": PAPER_ID, "visual_records": len(record["visuals"]), "figures": 37, "tables": 5, "stage": str(target), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
