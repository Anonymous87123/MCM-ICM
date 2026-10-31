"""Hand census of P-C-2016-42939-5fccbebc (Team 42939, 25 pages, 14 measured regions).

A Goodgrant-Foundation donation-strategy paper (education ROI). Fourteen measured regions resolve into
TWELVE FIGURE ROWS, TWO TABLE ROWS and ONE EXCLUSION.

  p4  r1  --         excluded         a measured raster that renders as pure white, no ink at all
  p7  r1  Table 1    table-grid       the data-source list, 2 by 4, ruled on every row and column
  p8  r1  Figure 1   flowchart-or-schematic  the whole model pipeline, tall, one page
  p9  r1  --         table-as-figure  the definitions table, three columns and ten rows, PRINTED AS AN
                                     IMAGE - the page has no text layer under its heading at all
  p12 r1  Table 2    table-grid       "The Top 10 Institutions", 2 by 10, and nine rows print
  p13 r1  Figure 2   line             LASSO coefficient paths against shrinkage
  p13 r2  Figure 3   line             cross-validated MSE, markers with error bars and no line
  p15 r1  Figure 4   scatter          GAM fit of PCTPELL against donation
  p16 r1  Figure 5   scatter          the same plot again with delta-h, delta-x and delta-f drawn on
  p17 r1  Figure 6   line             the assumed curve from deviation to the tuning parameter
  p18 r1  Figure 7   line             the same curve approximated by seven straight segments
  p20 r1  Figure 8   map-or-plan-view a US map with fifteen red pins, screenshot with clipped callouts
  p25 r1  Figure 9   scatter          GAM fit of PPTUG_EF against donation
  p25 r2  Figure 10  scatter          GAM fit of student/faculty ratio against donation

SIX PRINTED TABLES HAVE NO MEASURED REGION and therefore no row: Table 3 (post-LASSO results, p14) and
Tables 4 to 8 (the investment strategy of years 1 to 5, pp19/21/22) are declared gaps, as is the
untitled institution listing that runs off the foot of the p2 letter onto p3.

FIGURE 4 AND FIGURE 5 ARE THE SAME PICTURE. The second adds three annotation glyphs and is cited for a
different quantity.

TABLE 2 IS TITLED "TOP 10" AND PRINTS NINE ROWS.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2016-42939-5fccbebc"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]
        KIND[(_pg["page"], _i)] = _r["kind"]

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

for _key, _bbox in REG.items():
    _ctx = CTXREG.get(_key)
    if _ctx is None or max(abs(a - b) for a, b in zip(_ctx["bbox"], _bbox)) > 0.5:
        raise SystemExit(f"region numbering disagrees with the context dump at {_key}")

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def place(page: int, reg: int, kind: str, path: list[str], order: int = 1) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": order,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def uncited() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          pattern: str = "direct", read: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below",
            variables: int = 0, sentences: int = 1) -> dict:
    """Caption block. `verbatim` is what the page prints under (or over) the exhibit."""
    return {"verbatim": schema.norm(verbatim), "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": sentences, "units": False,
            "variables": variables > 0, "variable_count": variables,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def no_caption() -> dict:
    """The block for an exhibit that prints no caption at all: the p9 definitions image."""
    return {"verbatim": "", "numbering": "none", "words": 0, "sentences": 0, "units": False,
            "variables": False, "variable_count": 0, "conditions": False, "concludes": False,
            "voice": "none", "position": "below"}


def geometry(family: str, panels: int = 1, layout: str = "1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = False,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


def head(page: int, prefix: str) -> str:
    """The indexed heading on `page` whose label starts with `prefix`, exactly as printed."""
    for h in CTX["headings"]:
        if h["page"] == page and h["label"].startswith(prefix):
            return h["label"]
    raise SystemExit(f"no heading on p{page} starting {prefix!r}")


S_12 = [head(6, "1 Introduction"), head(6, "1.2 Baseline Model")]
S_131 = [head(9, "1.3 Detailed Definitions & Assumptions"), head(9, "1.3.1 Detailed Definitions:")]
S_32 = [head(11, "3 Determining the Performance Index"),
        head(11, "3.2 Performance Index via Principal-Component Factors")]
S_4 = [head(12, "4 Identifying Performance Contributing Variables via post-LASSO")]
S_5 = [head(14, "5 Determining Investment Strategy based on ROI")]
S_51 = [S_5[0], "5.1 Fitted Curve between Performance Contributing Variables and Donation Amount"]
S_521 = [S_5[0], "5.2.1 Model of Fitted ROIs of Performance Contributing Variables f ROIi"]
S_522 = [S_5[0], head(17, "5.2.2 Model of the tuning parameter Pi")]
S_523 = [S_5[0], head(18, "5.2.3 Calculation of ROI")]
S_53 = [S_5[0], head(19, "5.3 School Selection & Investment Strategy")]
S_A = [head(25, "Appendix")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_PRINTED = schema.printed_lines(PID)
for _group in (S_12, S_131, S_32, S_4, S_5, S_51, S_521, S_522, S_523, S_53, S_A):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN and schema.norm(_label) not in _PRINTED:
            raise SystemExit(f"section label is neither an indexed heading nor a printed line: "
                             f"{_label!r}")

# The printed captions. Two of them are over their exhibit rather than under it (Tables 1 and 2).
CAPT1 = caption("Table 1: Data Source", numbering="Table N:", position="above")
CAPT2 = caption("Table 2: The Top 10 Institutions in Terms of Performance Index",
                numbering="Table N:", position="above")
CAP1 = caption("Figure 1: Flow Chart Demonstration of the Model")
CAP2 = caption("Figure 2: LASSO path-coefficients as a function of shrinkage factor s")
CAP3 = caption("Figure 3: Cross-validated MSE")
CAP4 = caption("Figure 4: GAM Approximation")
CAP5 = caption("Figure 5: Demonstration of f ROI1", variables=1)
CAP6 = caption("Figure 6: Function from Deviation to Pi", variables=1)
CAP7 = caption("Figure 7: Approximated Function from Deviation to Pi", variables=1)
CAP8 = caption("Figure 8: Geographical Distribution of Selected Institutions")
CAP9 = caption("Figure 9: GAM Approximation of Share of Students Who Are Part-time vs Donation Amount")
CAP10 = caption("Figure 10: GAM Approximation of Student-to-faculty Ratio vs Donation Amount")

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_block: dict, cap_src: str, mention: dict,
           section: list[str], note: str, geo: dict | None = None, number: str = "",
           section_kind: str = "other", confidence: str = "high", order: int = 1) -> None:
    ITEMS.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)], "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap_block["verbatim"],
        "caption": cap_block, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section, order),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    })


def table(page: int, reg: int, section: list[str], note: str, spec: dict,
          cap_block: dict | None = None, cap_src: str = "none", mention: dict | None = None,
          section_kind: str = "other", order: int = 1) -> None:
    block = cap_block or no_caption()
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)],
        "family": "table-grid", "caption_source": cap_src,
        "caption_verbatim": block["verbatim"], "caption": block, "table": spec,
        "place": place(page, reg, section_kind, section, order),
        "mention": mention or uncited(), "note": note, "confidence": "high",
    })


# ============================================================ 1.2: the data-source list
table(7, 1, S_12,
      "A two-column, four-row grid at the foot of the baseline-model section: a header row "
      "'Variable | Dataset' and three body rows that name the three inputs the model uses - "
      "Performance index, Performance contributing variables, Donation amount - against where each "
      "comes from, 'Excel table', 'Excel table and pdf file' and 'Pdf file'. RULING IS A FULL GRID, "
      "not the booktabs shape: a rule above the header, a rule under the header, a rule between every "
      "pair of body rows and a rule at the foot, plus VERTICAL RULES at the left edge, between the two "
      "columns and at the right edge, all at the same 0.4 pt weight, so the table closes into a box "
      "and the three sources are separated by line rather than by white space. The caption prints "
      "ABOVE it, 'Table 1: Data Source', after the prose note 'Note: we only use data from the "
      "provided excel table and that mentioned in the pdf file.'; NO SENTENCE NAMES IT. The table is "
      "279 pt wide against a 453 pt measure, left-offset rather than centred, and it is the only "
      "'table' in the paper whose content is a provenance statement rather than a result.",
      {"rows": 4, "cols": 2, "header_rows": 1, "rule_style": "vertical-rules", "zebra": False,
       "merged_cells": False, "diagonal_header": False, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 0, "text_cols": 2, "width": "half",
       "orientation": "portrait", "continued": False, "note_sentence": ""},
      CAPT1, "text-layer", section_kind="model")

# ============================================================ 1.2: the pipeline chart
figure(8, 1, "flowchart-or-schematic", CAP1, "text-layer",
       cited(7, 8, ["Fig 1"], 1,
             "The flow chart of the whole model is presented below in Fig 1"),
       S_12,
       "A tall box-and-arrow pipeline, one page high and one column wide, drawn in a presentation tool: "
       "blue rounded 'Start', a filled rectangle 'addressing missing data', a decision diamond 'How is "
       "the data related to students' performance?', two branches into 'choosing performance "
       "contributing variables and determining their coefficients' and 'determining performance "
       "index', a second diamond 'Does donation amount affect the data directly?' with a 'No' arm to "
       "an oval 'Drop' and a 'Yes' arm into 'determining investment strategy', a long feedback line up "
       "the left margin labelled 'Donation amount', an 'Accounting for time duration and geographical "
       "distribution' box, and a right-hand column of four boxes from 'Fitting the relation between "
       "performance contributing variables and donation amount' to 'Maximizing ROI and determining "
       "investment strategy'. Arrow labels carry the data names - 'All data', 'Addressed data', "
       "'Performance indicators', 'Performance index', 'Potential performance contributing "
       "variables', 'Final results For year 1', 'Final results For year 2-5'. NO AXES, no number and "
       "no value anywhere on it. TWO FEEDBACK PATHS CROSS THE FLOW WITHOUT A JUNCTION MARK: the "
       "left-margin 'Donation amount' line runs the height of the page through the same channel as the "
       "downward arrows, and the bracket from the right-hand column re-enters 'determining investment "
       "strategy' from below, so which arrow feeds which box at the crossings can only be guessed. The "
       "'Final results' arrows converge on a single 'Finish' oval. Caption below; cited by the sentence "
       "that ends section 1.2, 'The flow chart of the whole model is presented below in Fig 1:'.",
       geometry("flowchart-or-schematic"), "1", section_kind="model")

# ============================================================ 1.3.1: the definitions table as a raster
figure(9, 1, "table-as-figure", no_caption(), "none", uncited(), S_131,
       "The definitions table, printed as an EMBEDDED IMAGE rather than as type: the page carries only "
       "its heading '1.3 Detailed Definitions & Assumptions' and the sub-heading '1.3.1 Detailed "
       "Definitions:', and everything under them is a bitmap, so the whole table has no text layer and "
       "no selectable cell. Three columns - a Name column, a Definition column of full sentences and a "
       "Denotation column of mathematics - over a header row and ten body rows, from 'Donation amount' "
       "(X_j) through 'ROI of the performance index (also referred as ROI for simplicity)' (ROI_j), "
       "every row ruled on all four sides in the same full grid as Table 1. NO CAPTION AND NO NUMBER: "
       "it is the only table in the paper that is never numbered, and the one that actually carries the "
       "paper's notation. The definition text is justified inside its column, which opens wide word "
       "gaps in two cells, and the denotation of 'Performance index' is a bare Greek upsilon with no "
       "subscript while its neighbours all carry one. Because it is an image, no figure or table "
       "extractor reads a cell of it, and the paper's own notation is therefore invisible to any "
       "downstream search.",
       geometry("table-as-figure"), "", section_kind="assumption")

# ============================================================ 3.2: the top-ten ranking
table(12, 1, S_32,
      "A two-column ranked list under the heading '3.2 Performance Index via Principal-Component "
      "Factors': a header 'Institution | Performance index' and NINE body rows from 'Los Angeles "
      "County College of Nursing and Allied Health' at 79.60372162 down to 'Weill Cornell Medical "
      "College' at 78.14334106. THE CAPTION PROMISES TEN AND THE TABLE PRINTS NINE - 'Table 2: The Top "
      "10 Institutions in Terms of Performance Index' - and the text layer confirms that no tenth row "
      "exists on the page or on the two after it, so the count is nine. Full grid ruling as in Table 1: "
      "rule above the header, rule under it, a rule between every row and a rule at the foot, with "
      "vertical rules at the left edge, between the columns and at the right edge. The caption prints "
      "ABOVE the table, is preceded by the sentence that cites it ('Table 2 presents the 10 "
      "institutions with largest values of the performance index.'), and the table carries NO RANK "
      "COLUMN although its whole purpose is a ranking, so the order is asserted by position alone. "
      "Every score prints EIGHT DECIMALS - 79.60372162 against 79.06066895 at the top - for an index "
      "that its own section builds as a weighted sum of four 0-to-100 variables and that the paper "
      "then reports to two decimal places nowhere; the eighth decimal separates the top two "
      "institutions by a margin smaller than any step in the underlying data.",
      {"rows": 10, "cols": 2, "header_rows": 1, "rule_style": "vertical-rules", "zebra": False,
       "merged_cells": False, "diagonal_header": False, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 1, "text_cols": 1, "width": "full",
       "orientation": "portrait", "continued": False, "note_sentence": ""},
      CAPT2, "text-layer",
      cited(12, 12, ["Table 2"], 1,
            "Table 2 presents the 10 institutions with largest values of the performance index"),
      section_kind="result")

# ============================================================ 4: the LASSO pair
figure(13, 1, "line", CAP2, "text-layer",
       cited(14, 13, ["Fig 2"], 2,
             "Fig 2. displays the results of LASSO procedure and Fig 3 displays the cross-validated "
             "MSE for different shrinkage factors"),
       S_4,
       "A LASSO coefficient-path plot: about ten thin polylines, most of them dashed, radiating from "
       "the left origin against 'Shrinkage Factor s' graduated 0.0 to 1.0, on a 'Standardized "
       "Coefficients' ordinate running minus 200 to 200. Two paths rise to about plus 210 and plus 150, "
       "four fall to minus 100, minus 130, minus 160 and minus 190, and a cluster of small blue dots "
       "sits near the origin between s = 0.45 and 0.65. A SECOND, UNLABELLED AXIS RUNS ALONG THE TOP "
       "with twelve thin vertical rules and the tick numbers 0 1 2 3 4 5 7 9 12 13 15 20 at irregular "
       "spacing - the non-zero count implied by each shrinkage, never named as such, with no unit and "
       "no label. The six variable names are printed OUTSIDE the frame at the right margin, each tied "
       "to a black square marker on the frame edge by a short rule: Tuition&Fee2010, "
       "Carnegie_HighResearchActivity, Carnegie_PublicRural, StudentToFaculty_ratio, PPTUG_EF, "
       "PCTPELL. There is no legend, no title, no gridline and no marker for the shrinkage factor the "
       "paper selects; the six labels crowd each other around the zero line. Caption below. Cited on "
       "the NEXT page ('Fig 2. displays the results of LASSO procedure') and again as 'find in Fig 2 "
       "that 6 variables have nonzero coefficients' - the figure prints before the sentence that reads "
       "it.",
       geometry("line", legend="outside-right"), "2", section_kind="model", order=1)

figure(13, 2, "line", CAP3, "text-layer",
       cited(14, 13, ["Fig 3"], 1,
             "Fig 2. displays the results of LASSO procedure and Fig 3 displays the cross-validated "
             "MSE for different shrinkage factors"),
       S_4,
       "The cross-validation panel of the same LASSO run: about thirty open markers with vertical "
       "error bars and NO CONNECTING LINE, one tall bar at s near 0.02 reaching 135, a steep descent "
       "through 55, 35 and 25 by s near 0.05, then a flat run at about 40 out to s = 1.0, against "
       "'Cross-Validated MSE' graduated 40 to 140 and 'Shrinkage Factor s' graduated 0.0 to 1.0. No "
       "gridline, no title, no legend and NO MARKER AT THE CHOSEN SHRINKAGE: the prose says 'the "
       "cross-validated MSE reaches minimum with shrinkage factor between 0.4-0.8. We choose 0.6', but "
       "the plotted trace is FLAT AT ABOUT 40 FROM 0.1 TO 1.0, so the flat region the sentence "
       "describes as a minimum between 0.4 and 0.8 is indistinguishable from every other s past 0.1, "
       "and the choice of 0.6 cannot be read off the exhibit at all. The leftmost bars are compressed "
       "into a few pixels, so their error extents are unreadable. Caption below; cited by the same "
       "next-page sentence as Figure 2.",
       geometry("line"), "3", section_kind="model", order=2)

# ============================================================ 5.1 and 5.2.1: the GAM pair
figure(15, 1, "scatter", CAP4, "text-layer",
       cited(15, 15, ["Fig 4"], 1,
             "The fitted curve of percentage of students who receive a Pell Grant is depicted below "
             "in Fig 4"),
       S_51,
       "A dense point cloud - thousands of small black diamond markers on a pale grey panel - with a "
       "single blue GAM curve over it and a grey confidence ribbon following the curve: the fitted "
       "PCTPELL against 'Donation' on an abscissa graduated 0e+00, 3e+08, 6e+08, 9e+08, and an "
       "ordinate graduated 0.25, 0.50, 0.75, 1.00 whose 'PCTPELL' label is printed ONE LETTER PER LINE "
       "down the left margin. The in-frame title is 'GAM estimation of PCTPELL vs Donation'. No legend, "
       "no data label and no printed value; the curve starts near 0.37 at zero donation, dips to about "
       "0.23 near 5e8 and recovers to about 0.26. THE POINTS ARE NOT READABLE AS A DISTRIBUTION: the "
       "overplotting is total near zero donation, where most institutions sit, so the cloud is a solid "
       "black mass across the first third of the abscissa and the shape the fit is drawn through cannot "
       "be checked by eye. The caption 'Figure 4: GAM Approximation' prints below, and the citing "
       "sentence adds '(see the other two fitted curves in Appendix)' - which is where Figures 9 and "
       "10 are, on the last page.",
       geometry("scatter"), "4", section_kind="model", order=1)

figure(16, 1, "scatter", CAP5, "text-layer", uncited(), S_521,
       "THE SAME PICTURE AS FIGURE 4 - the same diamond cloud, the same blue GAM curve, the same "
       "ribbon, the same axes 0e+00 to 9e+08 and 0.25 to 1.00, the same title 'GAM estimation of "
       "PCTPELL vs Donation', the same one-character-per-line 'PCTPELL' margin label - with THREE "
       "ANNOTATIONS ADDED OVER IT: an orange segment marking a local bump on the curve with the label "
       "delta-h, an orange vertical tick, and a green bracket carrying the labels delta-x and delta-f "
       "together with a caret over the bump. The caption 'Figure 5: Demonstration of f ROI1' and the "
       "prose that follows it define fitted ROI as delta-f over delta-x, so the exhibit is a definition "
       "drawn on a plot the paper has already printed: the second printing exists to carry three "
       "glyphs, and it carries no caption text that says so. NO SENTENCE NAMES FIGURE 5 - the "
       "definition it illustrates is written in the body text, and the only pointer to any exhibit in "
       "the section is the 'Fig 4' sentence on the previous page. The added labels are set small and "
       "in low contrast, so at print size the distinction the figure exists to make is the least "
       "legible thing on it.",
       geometry("scatter"), "5", section_kind="model", order=2)

# ============================================================ 5.2.2 and 5.2.3: the tuning curve
figure(17, 1, "line", CAP6, "text-layer",
       cited(17, 17, ["Fig 6"], 3,
             "The shape of the function is as shown in Fig 6 because of the following reasons"),
       S_522,
       "A single smooth curve on a fine grey grid, drawn by a mathematics package rather than a "
       "statistics one: roughly sinusoidal, dipping to about 0.35 near x = minus 1.3 and peaking at "
       "about 1.6 near x = 0.9, with axes through the origin and ticks minus 3 to 3 in halves on the "
       "abscissa and 2, 1, minus 1, minus 2 on the ordinate. THE AXES ARE NOT NAMED ANYWHERE: the "
       "prose says 'deviation is on the x-axis while Pi is on the y-axis', and the reader is expected "
       "to carry that in from the paragraph. The ordinate labels are drawn to the RIGHT of the y axis, "
       "inside the plot area, rather than in the left margin. Two small red circular markers sit ON the "
       "x axis at 0 and at 1, unexplained by the prose, the caption or the curve. No legend, no title, "
       "no value printed anywhere; the caption 'Figure 6: Function from Deviation to Pi' prints below, "
       "and the exhibit is cited three times on its own page ('the function has the shape shown in Fig "
       "6', 'The shape of the function is as shown in Fig 6', 'the function mapping deviation to Pi is "
       "similar to Fig 6') - more citations than any other exhibit in the paper, for a sketch the text "
       "itself calls an assumption.",
       geometry("line"), "6", section_kind="model")

figure(18, 1, "line", CAP7, "text-layer",
       cited(18, 18, ["Fig 7"], 1, "as is shown in Fig 7"),
       S_523,
       "The piecewise-linear replacement for Figure 6: a dark-blue polyline through small red circular "
       "markers at seven breakpoints, zigzagging down, up and down again, on the same fine grid, with "
       "the same unnamed axes and the same right-side ordinate labels (2, 1, minus 1, minus 2) and "
       "abscissa ticks minus 1, minus 0.5, 0.5, 1.5. Red markers are also drawn ON the x axis at 0, "
       "0.5 and 1.0 with one magenta marker at 1.5, which nothing explains. NO LEGEND, NO TITLE, NO "
       "AXIS NAMES and no value printed. The list of endpoints the prose supplies for this very "
       "polyline DISAGREES WITH ITSELF: it gives '(The minimum of deviations of all institutions, 2)', "
       "then halves, quarters and zero, then quarters and halves of the maximum with the value written "
       "'2/4' where its mirror image on the left is '4/3', and closes with '(The minimum of deviations "
       "of all institutions, 0)' where the maximum is obviously meant - so the two ends of the "
       "approximation are described by the same phrase, one value in the list is typed as an "
       "unreduced fraction of the wrong pair, and the curve drawn cannot be checked against the "
       "endpoints that define it. Caption below; cited by 'as is shown in Fig 7' on the same page.",
       geometry("line"), "7", section_kind="model")

# ============================================================ 5.3: the map
figure(20, 1, "map-or-plan-view", CAP8, "text-layer",
       cited(19, 20, ["Fig 8"], 1, "below in Table 4 and Fig 8"),
       S_53,
       "A screenshot of a mapping tool, not a chart: a light green and blue US base map with state "
       "outlines and state names set in grey capitals, city dots labelled Seattle, San Francisco, Las "
       "Vegas, Los Angeles, San Diego, Houston, New York, Chicago, Toronto and Ottawa, and FIFTEEN RED "
       "PINS with text callouts naming the selected institutions - University of Minnesota, The State "
       "University of..., United States Merchant..., Truman State University, Wabash Valley College, "
       "Virginia State Univers..., Illinois College, Institute of American..., East San Gabriel "
       "Valle..., Western Texas College, Marion Military Instit..., Louisiana State Univer..., New "
       "College of Florida, AVTEC. NO AXES, no graticule, no scale bar, no projection statement and no "
       "legend: the pins carry no magnitude, so the map shows WHERE the chosen institutions are and "
       "nothing about how much each receives - the amounts are in Table 4, which has no measured "
       "region. The callouts are TRUNCATED WITH ELLIPSES by their own tool, two of them collide "
       "('SUNY at FredoniaBoston'), one white box near the top right obscures map content, and the "
       "Alaska inset and the north-east corner carry labels cut by the frame. The caption 'Figure 8: "
       "Geographical Distribution of Selected Institutions' prints below; cited only by the joint "
       "sentence 'the results for year 1 and geographical distribution of selected institutions are "
       "presented below in Table 4 and Fig 8'.",
       geometry("map-or-plan-view"), "8", section_kind="solution")

# ============================================================ appendix: the other two GAM curves
figure(25, 1, "scatter", CAP9, "text-layer", uncited(), S_A,
       "The third GAM panel, on the appendix page: a diamond point cloud crowded at zero donation and "
       "sparse to the right, a blue curve falling from about 0.40 to a minimum near 0.03 between 5e8 "
       "and 6e8 and rising to about 0.08, a grey ribbon that WIDENS TO THE RIGHT AND DROPS BELOW ZERO "
       "at the frame edge, against 'Donation' 0e+00 to 9e+08 and an ordinate 0.00 to 1.00 labelled "
       "'PPTUG_EF' vertically. In-frame title 'GAM estimation of PPTUG_EF vs Donation'. No legend, no "
       "value, no title beyond the in-frame one. The 'URL of the axis label sits in the same column as "
       "the tick numbers and the tick '0.50' collides with it, so the ordinate's own scale is damaged "
       "at its middle tick. The ribbon crossing below zero is a proportion that cannot be negative. "
       "The caption 'Figure 9: GAM Approximation of Share of Students Who Are Part-time vs Donation "
       "Amount' prints below; NO SENTENCE NAMES IT, and the only pointer to the appendix pair is the "
       "parenthesis '(see the other two fitted curves in Appendix)' attached to Figure 4, twelve pages "
       "earlier. The page carries the heading 'Appendix' and nothing else.",
       geometry("scatter"), "9", section_kind="appendix", order=1)

figure(25, 2, "scatter", CAP10, "text-layer", uncited(), S_A,
       "The fourth GAM panel, same template, same page: diamond points stacked in near-vertical bands "
       "at low donation and thinning rightward, two outliers high at about 59 and 38, a blue curve "
       "declining gently from about 21 to about 17.5, and a grey ribbon widening to span roughly 11 to "
       "25 at the right edge, against the same 'Donation' axis 0e+00 to 9e+08 and an ordinate "
       "graduated 20, 40, 60 labelled 'Student/Faculty Ratio'. In-frame title 'GAM estimation of "
       "Student/Faculty Ratio vs Donation'. No legend, no value printed. THE FOUR PANELS OF THIS "
       "FAMILY ARE NOT DRAWN ON A COMMON SCALE: Figures 4, 5 and 9 use an ordinate of 0.00 to 1.00, "
       "this one 0 to 60, and all four share the same 'Donation' abscissa while the fitting relation "
       "is the thing compared - so the four fits cannot be laid against each other by eye, which is "
       "the only use a four-panel appendix has. The vertical banding of the points is an artefact of "
       "the integer variables being plotted against a continuous donation amount. Caption below; "
       "named by no sentence.",
       geometry("scatter"), "10", section_kind="appendix", order=2)

# ============================================================ the blank measured raster
EXCLUDED.append({
    "page": 4, "bbox": REG[(4, 1)], "reason": "background",
    "note": "The measured region on the title page renders as PURE WHITE: a raster of uniform 255 "
            "across the whole crop, with no ink, no box, no rule and no glyph. It sits above the "
            "title text 'An Optimal Strategy of Donation for Educational Purpose Control Number: "
            "#42939 February , 2016', so either an empty image was placed on the title page or the "
            "title block's image is white on white. Nothing can be counted in it, so it is excluded "
            "as background rather than recorded as an exhibit.",
})

RULES = [
    "Measure first, then read the pixels: fourteen measured regions resolve into twelve figure rows, "
    "two table rows and one exclusion, and every region is accounted for once [place.doc_order].",
    "A measured raster can be empty: the p4 region on the title page is uniform white across the whole "
    "crop, so the census excludes it as background instead of inventing an exhibit for it "
    "[caption.numbering].",
    "A table can be printed as an image: the definitions table on p9 has no text layer at all under "
    "its headings, so it is recorded as a table-as-figure row and no cell of the paper's own notation "
    "is machine-readable [geometry.family].",
    "Six printed tables carry no measured region and therefore no row - Table 3's post-LASSO results "
    "and Tables 4 to 8's five years of investment strategy - and the untitled institution listing that "
    "runs off p2 onto p3 has neither caption nor region, so all seven are declared gaps in the note "
    "[table.rule_style].",
    "Two exhibits print the same picture: Figure 4 and Figure 5 are the same diamond cloud, curve, "
    "ribbon, axes and in-frame title, and the second differs only by three annotation glyphs [geometry."
    "family].",
    "A caption can promise more than the table prints: 'Table 2: The Top 10 Institutions in Terms of "
    "Performance Index' has nine body rows, and the text layer of the page and the two after it holds "
    "no tenth [caption.verbatim].",
    "A chosen parameter can be unreadable on the exhibit the paper chose it from: the cross-validation "
    "trace of Figure 3 is flat from s = 0.1 to s = 1.0, so the 'minimum between 0.4-0.8' that the prose "
    "reports cannot be located, and no marker shows the 0.6 that was taken [geometry.data_labels].",
    "A four-panel appendix is not drawn on a common scale: Figures 4, 5 and 9 run 0.00 to 1.00 on the "
    "ordinate and Figure 10 runs 0 to 60, so the four fits it exists to compare cannot be compared "
    "[geometry.shared_axes].",
    "Citation is thin: six figure rows and both measured tables are named by a sentence, Table 1 is "
    "not, and Figures 5, 9 and 10 are named by nothing, while Figure 6 is named three times on one "
    "page [mention.count].",
]

NOTE = """\
Paper 99, Team 42939, a donation-strategy model for the Goodgrant Foundation built on a composite
education-performance index. Twenty-five pages, fourteen measured regions on twelve of them,
resolving into TWELVE FIGURE ROWS, TWO TABLE ROWS and ONE EXCLUSION - the pure-white raster on the
title page - with nothing unaccounted.

Seven printed tables carry no measured region and therefore no row: Table 3 (the post-LASSO
coefficients, p14), Tables 4 to 8 (the investment strategy of years 1 to 5, pp19, 21 and 22), and the
untitled institution listing that runs off the foot of the letter on p2 and continues at the head of
p3. Every one of the five yearly tables prints the same three columns (UNITID, names, ROI, donation)
against twenty institutions, and the two that share a page print with no rule between them.

The definitions table is an image. On p9 the page prints the heading "1.3 Detailed Definitions &
Assumptions", the sub-heading "1.3.1 Detailed Definitions:" and then a bitmap: three columns (Name,
Definition, Denotation) over a header row and ten body rows, every row ruled on all four sides. The
paper's entire notation - X_j, delta-X_j, Y_1j to Y_mj, F_1 to F_i, beta_1 to beta_i, ROI_1j,
fROI_1j, P_1j, ROI_j - exists inside that picture and nowhere in the text layer, and it is the only
table in the paper that is neither numbered nor captioned.

Table 2 is titled "The Top 10 Institutions in Terms of Performance Index" and prints NINE rows, from
Los Angeles County College of Nursing and Allied Health at 79.60372162 to Weill Cornell Medical
College at 78.14334106. No tenth row exists on the page or on the two pages after it. Every score is
printed to eight decimals even though the index is a weighted sum of four variables uniformized to
0 to 100, and the table carries no rank column although ranking is its only content. Both it and
Table 1 are ruled as full grids - a rule under the header, a rule between every pair of body rows and
vertical rules at both edges and between the columns - the opposite of the booktabs shape the rest of
the sample uses.

Figure 1 is the whole pipeline, one page high, drawn in a presentation tool: two decision diamonds,
a 'No' arm to a 'Drop' oval, a left-margin "Donation amount" feedback line that runs the height of the
page through the same channel as the downward arrows, a right-hand column of four boxes that re-enters
"determining investment strategy" from below, and no junction marks at any crossing.

Figures 2 and 3 are the LASSO pair, printed a page BEFORE the sentences that read them. Figure 2's
top axis carries twelve vertical rules and the tick numbers 0 1 2 3 4 5 7 9 12 13 15 20 with no label,
no unit and no name, and its six variable labels sit outside the frame at the right margin tied to
square markers on the frame edge. Figure 3's cross-validated trace is flat at about 40 from s = 0.1 to
s = 1.0 and carries no marker at the chosen shrinkage, so the "minimum with shrinkage factor between
0.4-0.8. We choose 0.6" that the next page reports is not readable on the exhibit.

Figures 4 and 5 are one picture printed twice. Both are the same diamond cloud of institutions, the
same blue GAM curve, the same grey ribbon, the same axes (0e+00 to 9e+08, 0.25 to 1.00) and the same
in-frame title "GAM estimation of PCTPELL vs Donation"; Figure 5 adds an orange segment labelled
delta-h, an orange tick and a green bracket labelled delta-x and delta-f. Figure 5 is named by no
sentence - it exists to illustrate the definition of fitted ROI that the body text states in symbols.
Both print "PCTPELL" one character per line down the left margin, and both are dominated near zero
donation by point overplotting so dense that the shape the curve is fitted to cannot be checked.

Figures 6 and 7 are the tuning-parameter curve and its piecewise approximation, drawn by a
mathematics package on a fine grid with unnamed axes, ordinate labels set inside the plot area, and
unexplained red markers on the x axis. The endpoint list the prose supplies for Figure 7 contradicts
itself: both ends are described as "The minimum of deviations of all institutions", one value is
written 2/4 where its mirror is 4/3, and the curve cannot be checked against the points that define
it. Figure 6 is cited three times on one page and Figure 7 once, which makes this sketch the most
cited exhibit in the paper.

Figure 8 is a screenshot of a mapping tool: fifteen red pins with callouts truncated by the tool
itself ("The State University of...", "Marion Military Instit..."), two collided into
"SUNY at FredoniaBoston", no scale bar, no graticule, no legend, and no magnitude on any pin. The
amounts the map cannot show are in Table 4, which has no measured region.

The appendix page prints the remaining two GAM fits, Figures 9 and 10, with no text but their
captions. The four panels of this family are not on a common scale - three run 0.00 to 1.00 on the
ordinate and the fourth runs 0 to 60 - so the four fits cannot be laid against each other. Figure 9's
confidence ribbon crosses below zero, and its ordinate label collides with the 0.50 tick.

Families: scatter 4, line 4, flowchart-or-schematic 1, map-or-plan-view 1, table-as-figure 1,
table-grid 2.
"""

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc99-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
