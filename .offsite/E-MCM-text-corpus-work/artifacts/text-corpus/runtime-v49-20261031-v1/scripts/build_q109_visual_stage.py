from __future__ import annotations

"""Build the source-checked G6 visual record for Queue 109 without promotion."""

import json
from pathlib import Path


ROOT = Path(r"F:/MCM/mcm-skill-work")
PAPER_ID = "P-B-2015-36178-d0225ad0"
TYPE = "B"
YEAR = "2015"
SHORT = "36178"
SHA256 = "d0225ad0b9c2d2dcdb91f20526f5bed617d1c221aff50ab700ad9cf85b1df9ff"
STAGE = ROOT / "tmp/q109-visual-stage-v2"


def visual(
    index: int,
    page: int,
    printed_page: str,
    figure: str,
    caption: str,
    purpose: str,
    source_model_ids: list[str],
    source_model_or_data: list[str],
    form: str,
    encodings: list[str],
    axes_units_scales: list[str],
    normalization: str,
    color_annotation_layout: list[str],
    uncertainty: str,
    claim_supported: str,
    construction_procedure: list[str],
    missing_reproduction_information: list[str],
    applicability: list[str],
    forbidden_scenarios: list[str],
    accessibility_interpretability: list[str],
    evidence_role: str,
    source_status: str,
    audience_reuse: list[dict] | None = None,
) -> dict:
    return {
        "visual_record_id": f"V-{TYPE}-{YEAR}-{SHORT}-{index:03d}",
        "paper_card_visual_index": index,
        "source_page": page,
        "printed_page": printed_page,
        "figure": figure,
        "caption": caption,
        "analytical_purpose": purpose,
        "source_model_ids": source_model_ids,
        "source_model_or_data": source_model_or_data,
        "form": form,
        "encodings": encodings,
        "axes_units_scales": axes_units_scales,
        "normalization": normalization,
        "color_annotation_layout": color_annotation_layout,
        "uncertainty": uncertainty,
        "exact_claim_supported": claim_supported,
        "reproducible_construction_procedure": construction_procedure,
        "missing_reproduction_information": missing_reproduction_information,
        "problem_type_applicability": [TYPE],
        "applicability": applicability,
        "forbidden_scenarios": forbidden_scenarios,
        "accessibility_and_interpretability": accessibility_interpretability,
        "disposition": "important-visual-record",
        "evidence_role": evidence_role,
        "source_status": source_status,
        "audience_reuse": audience_reuse or [],
    }


def build_visuals() -> dict:
    records = [
        visual(
            1,
            5,
            "4 of 17",
            "Figure 1",
            "Some of our initial ideas for how to search a rectangular area.",
            "Place three candidate rectangular-area search patterns side by side so the method discussion can reject the inward spiral and retain parallel and diagonal sweeps for quantitative development.",
            [
                "MU-B-2015-36178-004",
                "MU-B-2015-36178-005",
                "MU-B-2015-36178-006",
            ],
            [
                "The paper's qualitative hypothesis screen before the sweep-area equations are introduced.",
                "Parallel boustrophedon, 45-degree diagonal, and inward-spiral path concepts inside a rectangular search area.",
            ],
            "Three monochrome route schematics arranged horizontally: parallel back-and-forth legs, diagonal back-and-forth legs, and an inward rectangular spiral.",
            [
                "Black path lines encode the aircraft route.",
                "Arrowheads encode route direction or entry/exit orientation.",
                "Spacing between neighboring path legs qualitatively suggests sweep spacing, but no numeric width is encoded.",
                "Panel position distinguishes the three alternatives; the figure has no formal panel labels or legend.",
            ],
            [
                "No coordinate axes, physical units, rectangular dimensions, aircraft speed, track spacing, turn radius, or detection width are shown.",
                "The three sketches are conceptual and should not be compared by apparent path length or covered area.",
            ],
            "No normalization is stated or implied; the panels are not declared to share a geometric scale.",
            [
                "The figure uses black strokes on white and does not rely on color.",
                "The panels are separated only by whitespace, so method names must be supplied by nearby prose or a rebuilt figure legend.",
                "The spiral's nested shape and the two sweep orientations are visually distinguishable at normal print size.",
            ],
            "No uncertainty, efficiency interval, turn-cost range, or coverage-quality distribution is shown.",
            "The figure supports only the qualitative claim that several plausible search geometries were considered and that the paper proceeds with parallel and diagonal searches after discussing adaptability and efficiency; it does not establish which method is faster or more effective.",
            [
                "Draw one common rectangular boundary or explicitly state that panel scales differ.",
                "Construct each route with a declared entry point, direction, track spacing, number of turns, and termination point.",
                "Label parallel, diagonal, and spiral panels directly and preserve identical dimensions if visual comparison is intended.",
                "Attach quantitative distance, time, repeated-coverage, and POD calculations outside the schematic before using it for method selection.",
            ],
            [
                "Exact rectangle dimensions and whether the sketches share scale.",
                "The track spacing, path-length calculation, turn-time penalty, detection width, boundary-clipping rule, and starting-location rule for each candidate.",
                "A quantitative comparison connecting these initial sketches to the later 900-plus scenarios.",
            ],
            [
                "Early method generation and transparent hypothesis filtering for bounded-area search design.",
                "A compact audience-facing explanation of why parallel and diagonal sweeps remain candidate methods.",
            ],
            [
                "Do not use the sketch as proof of optimality, complete coverage, equal travel distance, or operational feasibility.",
                "Do not infer numeric efficiency from drawn density, panel size, or apparent number of turns.",
            ],
            [
                "Monochrome routes survive grayscale reproduction.",
                "Direct labels are absent, so a standalone reuse should add panel titles and textual route descriptions.",
                "Thin arrows and close spiral turns may be difficult to distinguish in a reduced print or low-resolution copy.",
            ],
            "important-positive-record",
            "paper-authored conceptual comparison",
            [
                {
                    "source_page": 20,
                    "artifact": "press-facing plan",
                    "reuse": "The stakeholder document repeats only the parallel and diagonal subsets under the caption 'The different search patterns'; this is a communication reuse, not a new analytical visual.",
                }
            ],
        ),
        visual(
            2,
            7,
            "6 of 17",
            "Figure 2",
            "A vector field representing the ocean currents moving an object.[21]",
            "Make the current-field mechanism visually concrete before the paper uses forward drift to move a crash/search area and reverse drift to infer an origin from found debris.",
            ["MU-B-2015-36178-002", "MU-B-2015-36178-008"],
            [
                "A third-party vector-field image cited as source [21], rather than output produced by the paper's own OSCAR-current-data workflow.",
                "Cyan current arrows, a white traced path or coastline-like line, a dark spatial background, and one small coordinate readout.",
            ],
            "Raster map-like vector field with directional arrows and an overlaid white trajectory or geographic line.",
            [
                "Arrow orientation encodes local current direction.",
                "Arrow length or shape may suggest magnitude, but the source figure supplies no scale that permits a numeric interpretation.",
                "Cyan arrows, a white line, and a black background separate current vectors from context.",
                "The small yellow coordinate text is not integrated into labeled axes or a geographic frame.",
            ],
            [
                "No labeled longitude/latitude axes, map projection, distance scale, time stamp, depth, current-speed units, or arrow-magnitude legend are visible.",
                "The spatial and temporal relation between the pictured field and the paper's selected OSCAR data is not established.",
            ],
            "The paper does not state arrow normalization or whether arrow length is proportional to speed.",
            [
                "The dark raster is embedded inside a white page and is visually separated from the surrounding prose.",
                "The small arrows and coordinate readout are difficult to audit at print scale.",
                "The figure has no internal legend; its meaning depends on the caption and the preceding current-drift explanation.",
            ],
            "No data uncertainty, temporal variability, interpolation uncertainty, or reverse-integration error is encoded.",
            "The figure supports the qualitative mechanism that a spatial current field can advect floating debris and can motivate a reverse-drift calculation; it does not validate the paper's selected field, recurrence, or crash-origin estimate.",
            [
                "Acquire a versioned current product for a declared date, depth, coordinate system, grid resolution, and region.",
                "Project the current components consistently, draw arrows with a numeric speed legend, and label longitude/latitude or map coordinates.",
                "Overlay the modeled debris path with start/end/time annotations and distinguish observations from simulated positions.",
                "Add field/interpolation uncertainty or an ensemble of trajectories when the figure is used to support a location claim.",
            ],
            [
                "The exact underlying data array, date, depth, projection, bounding box, arrow subsampling, vector scaling, and meaning of the white line.",
                "A machine-readable link between this cited image and the current records used in Equations 3 and 10.",
                "Forward/reverse numerical settings and uncertainty needed to reproduce a debris-origin estimate.",
            ],
            [
                "Conceptual explanation of current-driven transport and the data structure needed by spatial drift models.",
                "A bounded source-context illustration before a reproducible vector-field figure is built from the actual model inputs.",
            ],
            [
                "Do not present this third-party picture as paper-generated output, exact MH370-area evidence, calibration, validation, or an origin probability surface.",
                "Do not infer current magnitude or travel time from arrow appearance without a scale and time reference.",
            ],
            [
                "Cyan-on-black gives local contrast, but dense small arrows and yellow coordinate text are difficult at reduced size.",
                "Direction should also be available through arrow orientation and a textual description, not color alone.",
                "A rebuilt version should add a light-background accessible palette, numeric legend, direct start/end labels, and a recognizable geographic reference.",
            ],
            "bounded-source-context",
            "third-party cited visual",
            [
                {
                    "source_page": 20,
                    "artifact": "press-facing plan",
                    "reuse": "The stakeholder document repeats the same vector-field raster under a simplified explanatory caption; it remains the same cited source visual.",
                }
            ],
        ),
        visual(
            3,
            8,
            "7 of 17",
            "Figure 3",
            "The more our example airplane turns, the less it can fly after the turn ends.",
            "Translate the turn-radius and remaining-glide calculation into an inspectable geometric mechanism before the parametric endpoint equations are introduced.",
            ["MU-B-2015-36178-001"],
            [
                "The paper's example aircraft traveling at 500 knots with a stated 40-nautical-mile maximum glide and a 5.30-nautical-mile turn radius.",
                "The source text compares zero, 90-degree, and 180-degree turns and the figure adds intermediate endpoint rays.",
            ],
            "Monochrome trajectory schematic with a gray circular turn arc, radial post-turn directions, a turn-center point, and numeric remaining-distance annotations.",
            [
                "The gray arc encodes the distance consumed while turning around the marked center.",
                "Black rays encode straight post-turn trajectories for sampled headings.",
                "Labels 40, 35.83, 31.66, 27.5, and 23.33 NM encode remaining distance after increasing turn angle.",
                "The 5.30 NM label encodes the example turn radius.",
            ],
            [
                "Distance is expressed in nautical miles, but the diagram has no Cartesian axes, angle labels, or declared drawing scale.",
                "The sequence of rays is qualitative; the exact sampled turn angles must be recovered from the model rather than the picture alone.",
            ],
            "No normalization is used; the values are one example aircraft configuration, not proportions or universal ratios.",
            [
                "Black trajectories and gray turn geometry work in grayscale.",
                "Numeric labels are placed adjacent to the corresponding rays, but the rays themselves lack angle labels.",
                "The caption states the intended monotone relation so the viewer does not have to infer the claim from shape alone.",
            ],
            "No uncertainty in glide ratio, speed, wind, bank angle, aircraft mass, or turn radius is shown.",
            "For the paper's example inputs, increasing turn angle consumes more of the available glide path and reduces the remaining straight-line distance after the turn.",
            [
                "Fix aircraft speed, maximum glide distance, bank-angle convention, and turn-radius equation.",
                "For each sampled turn angle, compute turn arc length and subtract it from the available glide distance.",
                "Draw the common turn circle/arc, the post-turn tangent direction, and the corresponding remaining-distance segment.",
                "Label angle, radius, distance, and units; compare the numeric labels with the source equations before plotting.",
            ],
            [
                "The exact list of sampled angles and plotting code.",
                "Coordinate orientation and geometric construction used to position the annotated rays.",
                "Uncertainty or sensitivity in speed, bank angle, wind, and glide performance.",
            ],
            [
                "Mechanism explanation for turn-constrained reachability, mobile-agent range, or path-budget problems.",
                "A pre-equation schematic that makes a non-obvious resource tradeoff visible with units.",
            ],
            [
                "Do not treat the example numbers as a calibrated aircraft envelope or a probability distribution.",
                "Do not use the sketch when variable wind, lift/drag dynamics, multiple maneuvers, or terrain require a dynamic trajectory model.",
            ],
            [
                "The monochrome geometry is accessible without color and the numeric labels are readable in the focused crop.",
                "Add direct angle labels and a coordinate orientation for standalone use.",
                "The 5.30 NM radius label is close to the center/arc and can be confused with another path length at small print size.",
            ],
            "important-positive-record",
            "paper-authored model-mechanism visual",
        ),
        visual(
            4,
            9,
            "8 of 17",
            "Figure 4",
            "The possible end locations for our example plane, if it turns only to the left. The smaller circle represents the airplane's turn radius.",
            "Show how the parametric turn-and-glide equations map sampled left-turn angles into a noncircular endpoint locus and distinguish that locus from the turn-radius circle.",
            ["MU-B-2015-36178-001"],
            [
                "Endpoints generated by Equation 2 for the example aircraft over the paper's left-turn angle range.",
                "The turn-radius circle and the filled endpoint envelope plotted in a Cartesian frame.",
            ],
            "Filled Cartesian endpoint-locus plot with blue boundary markers and a smaller gray reference circle.",
            [
                "Blue dots encode sampled possible terminal positions after a left turn and remaining glide.",
                "The connecting blue boundary and pale-blue fill encode the displayed endpoint envelope, not a probability density.",
                "The gray circle encodes the 5.30-nautical-mile turn radius.",
                "Horizontal and vertical Cartesian positions are shown by tick marks approximately spanning -40 to 40.",
            ],
            [
                "The axes are linear and centered near the initial contact/orientation geometry, but neither axis is titled and nautical-mile units appear only in the surrounding derivation.",
                "No heading arrow, north/east convention, origin label, equal-aspect statement, or scale bar is supplied.",
            ],
            "The figure uses the source example's absolute distance values; no probability, density, or normalized reachability score is encoded.",
            [
                "Blue points and fill distinguish the endpoint locus from the gray turn circle.",
                "The smaller circle is explained directly in the caption, while the outer boundary depends on preceding prose and Equation 2.",
                "The pale fill may visually suggest a reachable area even though the plotted mathematical object is described as possible end locations.",
            ],
            "No parameter uncertainty, endpoint probability, wind uncertainty, discretization error, or model-validation band is shown.",
            "Equation 2 produces an asymmetric locus of possible terminal locations for left turns, and the smaller circle gives a geometric reference for the aircraft's turn radius.",
            [
                "Define a Cartesian origin and orientation at the last known point and declare units.",
                "Sample the permitted left-turn angle range at a stated resolution and evaluate the source x(theta), y(theta) equations.",
                "Plot endpoints, connect only if the locus ordering is preserved, and draw the turn-radius circle separately.",
                "Use equal aspect, axis titles, a heading arrow, and a caption that distinguishes locus, filled envelope, and probability.",
            ],
            [
                "The sampled angle step, exact domain, plotting software/code, aspect-ratio setting, and reason the interior is filled.",
                "The coordinate origin/orientation and whether all points inside the shaded region are dynamically reachable.",
                "Wind, drag, glide-performance, and aircraft-state uncertainty.",
            ],
            [
                "Reachable-set or endpoint-locus visualization after a parameterized geometric model.",
                "Comparison of a turning constraint with the larger terminal-position envelope.",
            ],
            [
                "Do not interpret fill intensity as probability, confidence, or search priority.",
                "Do not transfer the envelope to another aircraft or weather state without recomputing the model and coordinate convention.",
            ],
            [
                "Blue-versus-gray separation is visible, but the plot should use line style and direct labels so it remains clear under color-vision deficiency and grayscale printing.",
                "Missing axis titles and units weaken standalone interpretability.",
                "Boundary points remain legible in the focused crop, while the pale interior should be described textually as an envelope rather than probability.",
            ],
            "important-positive-record",
            "paper-authored model-output visual",
        ),
        visual(
            5,
            9,
            "8 of 17",
            "Figure 5",
            "The full range of end locations for our example plane.",
            "Mirror the left-turn locus to include right turns and expose the nonconvex full endpoint boundary that is subsequently wind-expanded and simplified by a convex hull.",
            ["MU-B-2015-36178-001"],
            [
                "The Figure 4 left-turn endpoint set and its vertical mirror for right turns.",
                "The source's example turn radius and endpoint equations before wind-normal expansion and convex-hull simplification.",
            ],
            "Filled Cartesian full endpoint-envelope plot with mirrored blue boundary markers and two gray turn-radius reference circles.",
            [
                "Blue points encode sampled left- and right-turn terminal positions.",
                "The outer and inner blue boundary arcs encode the full modeled endpoint locus; pale fill visually groups the envelope.",
                "Two gray circles show the mirrored turn-radius geometry.",
                "Linear horizontal and vertical position ticks span approximately -40 to 40 without axis names.",
            ],
            [
                "Distance is inferably in nautical miles from the surrounding section, but the axes themselves lack labels, units, origin meaning, orientation, and scale declaration.",
                "The plot appears equal-aspect, but this is not documented.",
            ],
            "Absolute example distances are plotted; the pale fill is not a normalized probability, likelihood, or confidence region.",
            [
                "Blue point/line/fill separates the endpoint envelope from gray turn circles.",
                "The mirrored geometry makes left/right inclusion visually immediate.",
                "The inner loop and overlapping gray circles are visually dense and require the caption plus prior Figure 4 explanation.",
            ],
            "No uncertainty in aircraft state, trajectory, wind, reachability, or hull expansion is encoded.",
            "Allowing both turn directions yields the displayed full endpoint locus, which provides the geometric input that the paper later expands for wind and encloses with a convex hull to obtain an initial search area.",
            [
                "Generate the source-checked left-turn locus with a declared angle grid.",
                "Mirror the appropriate coordinate to generate right-turn endpoints and preserve correspondence between sampled angles.",
                "Plot both loci with equal aspect and direct labels; show turn-radius references separately.",
                "If a search polygon is needed, display wind expansion and convex hull as distinct later layers rather than implying they already appear in Figure 5.",
            ],
            [
                "Angle resolution, plotting code, coordinate orientation, and whether the filled interior is reachable.",
                "The exact wind-normal expansion, hull vertices, and area change that occur after the plotted stage.",
                "Parameter distributions or validation data needed to convert geometry into a calibrated search region.",
            ],
            [
                "Full reachable-set visualization before spatial buffering, hull construction, or search-area optimization.",
                "A layered explanation of how left/right alternatives enlarge a constrained endpoint set.",
            ],
            [
                "Do not call the fill a crash probability surface, confidence region, or already wind-adjusted convex hull.",
                "Do not hide the nonconvex inner boundary when its geometry matters to area or search planning.",
            ],
            [
                "The outer boundary is distinct, but blue/gray-only encoding should be reinforced with direct labels and line styles.",
                "Axis names, units, heading orientation, and a concise explanation of the inner loop are needed for standalone accessibility.",
                "The dense central geometry remains readable only at sufficient resolution.",
            ],
            "important-positive-record",
            "paper-authored model-output visual",
            [
                {
                    "source_page": 19,
                    "artifact": "press-facing plan",
                    "reuse": "The stakeholder document reuses the same full endpoint-envelope geometry to explain the initial search area; the reused drawing is not a second model result.",
                }
            ],
        ),
        visual(
            6,
            11,
            "10 of 17",
            "Figure 6",
            "A visual representation of one leg of a search plane's search path. (Source: United States National Search and Rescue Supplement to the International Aeronautical and Maritime Search and Rescue Manual)",
            "Define searchleg, crossleg, track-space, searchleg-length, and turn-diameter geometry so the parallel swept-area algorithm can separate searching distance from repositioning distance.",
            ["MU-B-2015-36178-004"],
            [
                "A third-party diagram cited from the United States National Search and Rescue Supplement to the International Aeronautical and Maritime Search and Rescue Manual.",
                "One repeated parallel-search leg containing two searchleg straightaways, two rounded turns, and a crossleg straightaway.",
            ],
            "Monochrome operational-geometry schematic with dimension arrows and direct terminology labels.",
            [
                "Horizontal straight segments labeled searchleg straightaway encode distance spent actively searching.",
                "The vertical segment labeled crossleg straightaway encodes relocation to the next sweep line.",
                "Track space S encodes separation between neighboring search tracks.",
                "Searchleg length L and repeated TD/2 margins encode longitudinal geometry and half-turn-diameter allowances.",
                "Rounded corners encode the two quarter-turns that join each crossleg and searchleg.",
            ],
            [
                "No absolute units or numeric values are supplied; S, L, TD/2, and the source's y label are symbolic lengths.",
                "The schematic is not plotted on geographic axes and does not encode aircraft speed or elapsed time.",
            ],
            "No normalization is used; the diagram defines symbolic geometry that must be populated with scenario-specific distances.",
            [
                "Black lines, arrowheads, and direct text labels work in grayscale.",
                "Several TD/2 labels are small and crowded near turns, so high-resolution rendering is needed.",
                "Direct labels reduce legend lookup and make the search-versus-reposition distinction explicit.",
            ],
            "No variability in turn diameter, track spacing, detection width, aircraft speed, or boundary clipping is shown.",
            "A parallel-search leg can be decomposed into searchable straightaways and nonsearch crossleg/turn components, which supports the paper's later swept-area and full-leg calculations.",
            [
                "Cite the source and preserve its terminology rather than presenting the diagram as a paper-original definition.",
                "Draw two parallel searchleg straightaways separated by track space S and connect them with a crossleg and two quarter-turns.",
                "Annotate L, S, turn diameter or radius, and every component counted or excluded by the area/time equation.",
                "Pair the geometry with an explicit distance/time budget and state whether turns and crosslegs contribute to detection.",
            ],
            [
                "The paper does not freeze the underlying source image file, drawing dimensions, or reproduction code.",
                "The source-to-paper mapping among S, L, TD, y, sweep width, block geometry, and Equation 5 is not fully tabulated.",
                "Aircraft-specific turn performance, speed changes, boundary behavior, and sensing during turns/crosslegs.",
            ],
            [
                "Operational search-path terminology, parallel-sweep implementation, and distance-accounting explanations.",
                "Any bounded-area coverage algorithm that must distinguish productive traversal from repositioning overhead.",
            ],
            [
                "Do not treat the source schematic as evidence that the paper's allocation algorithm is complete, optimal, or physically flyable.",
                "Do not omit units or assume that track spacing equals effective sweep width without a stated detection model.",
            ],
            [
                "Monochrome direct labeling is strong, but small dimension text and dense turn annotations may be unreadable in a reduced figure.",
                "A rebuilt version should enlarge critical labels, define every symbol in adjacent text, and use consistent terminology with equations.",
                "The productive-versus-repositioning distinction should be repeated in the caption for non-specialist readers.",
            ],
            "bounded-source-context",
            "third-party cited visual",
        ),
        visual(
            7,
            14,
            "13 of 17",
            "Figure 7",
            "A visual representation of the results from our analysis of different search methods. Red dots represent results from the diagonal search algorithm; blue dots represent the optimized parallel search algorithm. The horizontal axis is the unique index of the search in our data. The vertical axis is the number of days in which the search was completed. Values toward the right of the plot represent searches with more planes and higher wind speeds.",
            "Compare modeled completion days for diagonal and optimized-parallel searches over the paper's indexed scenario set and connect scenario outcomes to conditional algorithm recommendations.",
            [
                "MU-B-2015-36178-005",
                "MU-B-2015-36178-006",
                "MU-B-2015-36178-009",
            ],
            [
                "The paper's 900-plus combinations of search-area size, aircraft count/type, weather, wind, visibility, and related fixed model inputs.",
                "Modeled days to the paper's daily/cumulative 95-percent POD stopping rule for diagonal and optimized-parallel searches.",
            ],
            "Dense two-series scenario-index scatter/strip plot with substantial point overlap.",
            [
                "Red dots encode diagonal-search completion days.",
                "Blue dots encode optimized-parallel completion days.",
                "Horizontal position encodes a unique scenario index rather than a physical variable; the caption states that values farther right have more planes and higher wind speeds.",
                "Vertical position encodes modeled days until the search is completed.",
                "Repeated points at common day values form horizontal bands and heavy overplotting near the bottom of the chart.",
            ],
            [
                "Both axes appear linear; the horizontal range covers roughly 1-900 scenario indices and the vertical range extends beyond 150 days.",
                "The plot itself has tick numbers but no axis titles or units; the caption supplies the semantic meanings and days unit.",
                "The scenario-index ordering is not reconstructible from the figure because the parameter map is absent.",
            ],
            "No normalization is applied to completion days; scenario ordering compresses several heterogeneous physical and operational inputs into an opaque categorical index.",
            [
                "Red and blue point color is the only internal method key; there is no plotted legend and the caption acts as the decoder.",
                "Small points and dense overlap reduce visibility of paired method differences.",
                "The single panel puts both methods on a common y-scale, which supports direct day comparison when a scenario pair can be identified.",
            ],
            "No confidence interval, stochastic variation, input uncertainty, scenario weight, repeated-run variability, or model-error band is shown.",
            "Within the source's selected scenarios and model assumptions, diagonal search usually has fewer modeled days, while optimized parallel can perform best in some configurations; the figure supports conditional comparison rather than universal optimality.",
            [
                "Freeze a table with one row per scenario, all parameter values, stable scenario ID, both modeled completion-day outputs, and model version.",
                "Plot paired outputs on a common linear day scale with direct axis titles, units, a legend, and deterministic ordering by one declared parameter or performance difference.",
                "Use transparency, jitter, connected pairs, faceting, or summarized distributions to resolve overlap while preserving exact observations.",
                "Annotate the method-switch regions and expose the number of planes, wind speed, visibility, and area rather than relying on an opaque index.",
                "Add uncertainty or scenario weights if the result is used for an operational recommendation.",
            ],
            [
                "The complete scenario matrix, parameter ordering, source data file, code, method outputs, and any failed or censored runs.",
                "A pointwise pairing key visible in the plot, the basic-parallel series, and quantitative counts of wins/ties/losses.",
                "Uncertainty, interaction analysis, representativeness of the scenario set, and validation against real search durations.",
            ],
            [
                "Scenario-based comparison of discrete search algorithms when every scenario and method output is reproducibly frozen.",
                "Decision-rule construction after an opaque index is replaced by explicit resource, weather, area, and visibility encodings.",
            ],
            [
                "Do not use the plotted cloud as proof of global optimality, field effectiveness, causal superiority, or a representative operational frequency distribution.",
                "Do not compare apparent color density without resolving overplotting and paired scenario identity.",
                "Do not transfer the conditional recommendation beyond the paper's uncalibrated POD, area, drift, aircraft, and scheduling assumptions.",
            ],
            [
                "Red/blue color-only method encoding is vulnerable to color-vision deficiencies; add shape, line, facet, or direct labels.",
                "The absent legend and axis titles force readers to search the caption.",
                "Overplotting obscures point counts and paired differences, while the unexplained scenario index blocks local interpretation.",
                "A redesigned paired-difference or faceted plot would make method switches and high-day outliers substantially more auditable.",
            ],
            "important-positive-record-with-auditability-boundary",
            "paper-authored model-comparison visual",
        ),
    ]
    return {
        "schema_version": 1,
        "paper_id": PAPER_ID,
        "problem_type": TYPE,
        "year": YEAR,
        "source_sha256": SHA256,
        "review_status": "validated",
        "gate": "G6-important-visual-retention",
        "supersession": {
            "authoritative_stage": "tmp/q109-visual-stage-v2/visuals.json",
            "rejected_stage": "tmp/q109-visual-stage-v1/visuals.json",
            "reason": "The first visual draft truncated source captions, cited Figure 2 as [20] instead of [21], and reversed the Figure 7 caption's aircraft-count direction. The rejected stage remains untouched and must not be promoted.",
        },
        "source_page_coverage": {
            "physical_pages": 20,
            "contact_sheet_ranges": ["1-5", "6-10", "11-15", "16-20"],
            "figure_numbers": [f"Figure {index}" for index in range(1, 8)],
            "figure_count": 7,
            "audience_reuse_pages": [19, 20],
            "audience_reuse_policy": "Repeated memo/press renderings of Figures 1, 2, and 5 are linked to their original visual records and do not inflate the important-visual count.",
        },
        "transport_safety": {
            "one_image_per_tool_call": True,
            "max_proxy_bytes": 450000,
            "proxies_inspected_in_context_segment": 8,
            "full_page_original_detail_used": False,
            "notes": "Four bounded contact sheets covered all 20 pages; focused bounded crops checked Figures 3, 4-5, 6, and 7. Figures 1 and 2 were readable in the bounded contact sheets. No full-page PNG was returned to model context.",
        },
        "gate_attestation": {
            "g1_g3_language_status": "validated",
            "g4_organization_status": "passed",
            "g5_model_status": "validated",
            "g6_visual_status": "passed",
            "g7_warning_opened": False,
            "all_numbered_figures_dispositioned": True,
            "visual_count": 7,
        },
        "visuals": records,
    }


def validate(record: dict) -> None:
    records = record["visuals"]
    required = {
        "visual_record_id",
        "paper_card_visual_index",
        "source_page",
        "printed_page",
        "figure",
        "caption",
        "analytical_purpose",
        "source_model_ids",
        "source_model_or_data",
        "form",
        "encodings",
        "axes_units_scales",
        "normalization",
        "color_annotation_layout",
        "uncertainty",
        "exact_claim_supported",
        "reproducible_construction_procedure",
        "missing_reproduction_information",
        "problem_type_applicability",
        "applicability",
        "forbidden_scenarios",
        "accessibility_and_interpretability",
        "disposition",
        "evidence_role",
        "source_status",
        "audience_reuse",
    }
    if len(records) != 7:
        raise ValueError(f"expected seven visual records, found {len(records)}")
    if [item["figure"] for item in records] != [f"Figure {index}" for index in range(1, 8)]:
        raise ValueError("visual records must exactly cover Figures 1-7 in source order")
    if [item["paper_card_visual_index"] for item in records] != list(range(1, 8)):
        raise ValueError("paper-card visual indexes must be contiguous and source ordered")
    ids = [item["visual_record_id"] for item in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate visual record ID")
    known_models = {f"MU-{TYPE}-{YEAR}-{SHORT}-{index:03d}" for index in range(1, 10)}
    for item in records:
        missing = required - item.keys()
        if missing:
            raise ValueError(f"{item.get('figure')} missing fields: {sorted(missing)}")
        if not 1 <= item["source_page"] <= 20:
            raise ValueError(f"{item['figure']} source page out of bounds")
        if item["problem_type_applicability"] != [TYPE]:
            raise ValueError(f"{item['figure']} must retain manifest-derived type B")
        if item["disposition"] != "important-visual-record":
            raise ValueError(f"{item['figure']} is missing its important-visual disposition")
        if not set(item["source_model_ids"]) <= known_models:
            raise ValueError(f"{item['figure']} references an unknown q109 model")
        for key in (
            "source_model_or_data",
            "encodings",
            "axes_units_scales",
            "color_annotation_layout",
            "reproducible_construction_procedure",
            "missing_reproduction_information",
            "applicability",
            "forbidden_scenarios",
            "accessibility_and_interpretability",
        ):
            if not item[key]:
                raise ValueError(f"{item['figure']} has an empty required list: {key}")
    gate = record["gate_attestation"]
    if gate["g7_warning_opened"] or not gate["all_numbered_figures_dispositioned"]:
        raise ValueError("G6 must finish before G7 opens")
    if gate["visual_count"] != len(records):
        raise ValueError("G6 attestation count mismatch")


def main() -> None:
    if STAGE.exists():
        raise SystemExit(f"refusing to overwrite existing stage: {STAGE}")
    record = build_visuals()
    validate(record)
    STAGE.mkdir(parents=True)
    target = STAGE / "visuals.json"
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "paper_id": PAPER_ID,
                "visuals": len(record["visuals"]),
                "figures": [item["figure"] for item in record["visuals"]],
                "stage": str(target),
                "status": "pass",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
