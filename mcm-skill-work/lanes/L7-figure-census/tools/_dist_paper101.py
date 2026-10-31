"""Hand census of P-C-2016-50193-615bc62f (Team 50193, 24 pages, 15 measured regions).

A Goodgrant-Foundation allocation paper: screen 2977 colleges, impute the missing columns, score ROI
with AHP weights, then maximise it under risk, count and budget constraints. Fifteen measured regions
resolve into SEVEN FIGURE ROWS, SEVEN TABLE ROWS and ONE EXCLUSION, with nothing unaccounted.

  p7  r1  Table 1    table-grid       the ten columns needing imputation, two side-by-side blocks
  p7  r2  Table 2    table-grid       the eighteen integral columns, same two-block shape
  p8  r1  Table 3    table-grid       the five k-means clusters and one imputed value each
  p12 r1  Figure 1   node-link-network  eight weighted arrows into three sums and one ROI node
  p13 r1  Figure 2   line             grey-prediction panels (a) and (b), side by side
  p13 r2  --         excluded         panel (b) of the same Figure 2; one row cannot become two
  p14 r1  Table 4    table-grid       ten constants, two columns, no header row
  p14 r2  Table 5    table-grid       two variables, two columns, no header row
  p16 r1  Table 6    table-grid       the fourteen selected institutions, three columns, no header
  p16 r2  Figure 3   bar              four factors for fourteen schools, UNITIDs on the abscissa
  p16 r3  Figure 4   other            a pie of the money allocation, fourteen UNITID slices
  p17 r1  Figure 5   table-as-figure  a printed five-year allocation grid numbered as a figure
  p18 r1  Figure 6   line             max return against max acceptable risk
  p19 r1  Figure 7   line             max return against number of schools awarded
  p19 r2  Table 7    table-grid       four distribution policies, max return and gap

FIGURE 2 CARRIES THE UNPLACED CAPTION 'Figure 2: general title.' and both its panels are sublabelled
'Grey Predicting for Future ROI', naming no school.

TABLE 6 CARRIES TABLE 1'S CAPTION, WORD FOR WORD, OVER A LIST OF INSTITUTIONS.

FIGURE 5'S PRINTED COLUMN TOTALS ARE A TENTH OF THE VALUES ABOVE THEM.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2016-50193-615bc62f"
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


def cited(first_page: int, page: int, style: list[str], count: int, lead: str = "",
          trail: str = "", pattern: str = "direct", read: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page) if lead else "",
            "trail_sentence": q(trail, first_page) if trail else "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": None}


def caption(verbatim: str, number: str = "1", kind: str = "Figure",
            position: str = "below", variables: int = 0) -> dict:
    return {"verbatim": schema.norm(verbatim), "numbering": f"{kind} N:",
            "words": len(schema.words(verbatim)), "sentences": 1, "units": False,
            "variables": variables > 0, "variable_count": variables,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def geometry(family: str, panels: int = 1, layout: str = "1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = False,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


def head(page: int, prefix: str) -> str:
    for h in CTX["headings"]:
        if h["page"] == page and h["label"].startswith(prefix):
            return h["label"]
    raise SystemExit(f"no heading on p{page} starting {prefix!r}")


S_22 = [head(6, "2.2 Data imputation")]
S_31 = [head(9, "3.1 Concept of ROI")]
S_32 = [head(12, "3.2 Using Grey Theory to predict ROI")]
S_41 = [head(14, "4.1 Definition of Risk")]
S_42 = [head(14, "4.2 Basic Model")]
S_43 = [head(15, "4.3 Results of basic model")]
S_44 = [head(17, "4.4 Time series model")]
S_51 = [head(18, "5.1 Risk-Return")]
S_52 = [head(18, "5.2 School number")]
S_53 = [head(19, "5.3 Policy of distribution")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
for _group in (S_22, S_31, S_32, S_41, S_42, S_43, S_44, S_51, S_52, S_53):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN:
            raise SystemExit(f"section label is not an indexed heading: {_label!r}")

CAPT1 = caption("Table 1: Missing data columns", kind="Table", position="above")
CAPT2 = caption("Table 2: Integral data columns", kind="Table", position="above")
CAPT3 = caption("Table 3: Clustering Output and Imputation Value", kind="Table", position="above")
CAPT4 = caption("Table 4: constant", kind="Table", position="above")
CAPT5 = caption("Table 5: variable", kind="Table", position="above")
CAPT6 = caption("Table 6: Missing data columns", kind="Table", position="above")
CAPT7 = caption("Table 7:  return-policy", kind="Table", position="above")
CAP1 = caption("Figure 1: The model of ROI evaluation system")
CAP2 = caption("Figure 2: general title.")
CAP3 = caption("Figure 3: Factors of the investment schools")
CAP4 = caption("Figure 4: Allocation of the money")
CAP5 = caption("Figure 5: list of five years")
CAP6 = caption("Figure 6: Return-Risk")
CAP7 = caption("Figure 7: Return-Number of selected School")

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_block: dict, cap_src: str, mention: dict,
           section: list[str], note: str, geo: dict | None = None, number: str = "",
           section_kind: str = "other", confidence: str = "high", order: int = 1,
           other_note: str = "") -> None:
    ITEMS.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)], "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap_block["verbatim"],
        "caption": cap_block, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section, order),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
        "other_note": other_note,
    })


def table(page: int, reg: int, section: list[str], note: str, spec: dict,
          cap_block: dict | None = None, cap_src: str = "none", mention: dict | None = None,
          section_kind: str = "other", order: int = 1) -> None:
    block = cap_block or caption("", kind="Table")
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)],
        "family": "table-grid", "caption_source": cap_src,
        "caption_verbatim": block["verbatim"], "caption": block, "table": spec,
        "place": place(page, reg, section_kind, section, order),
        "mention": mention or uncited(), "note": note, "confidence": "high",
    })


OPEN = {"rule_style": "vertical-rules", "zebra": False, "diagonal_header": False,
        "units_in_header": False, "decimal_aligned": False, "orientation": "portrait",
        "note_sentence": ""}

# ============================================================ 2.2: the two column lists
table(7, 1, S_22,
      "The columns that need imputing, printed as TWO SIDE-BY-SIDE BLOCKS of two columns each - "
      "'Number | Variable Name' twice over - so the physical grid is four columns and ten body rows, "
      "numbered 1 to 5 and 6 to 10, with the header wording repeated in both blocks. RULES: a rule "
      "above the header, a rule under it and a rule at the foot, vertical rules between the columns of "
      "each block and a doubled vertical rule at the block join, and NO left or right edge rule and NO "
      "rule between any pair of body rows. The ten entries MIX REGISTERS: the first two are "
      "human-readable ('Net Price', 'Retention Rate') and the remaining eight are raw database names in "
      "two different casings ('GRAD_DEBT_MDN_SUPP', 'GRAD_DEBT_MDN10YR_SUPP', 'RPY_3YR_RT_SUPP' above "
      "against 'gt_25k_p6', 'md_earn_wne_p10', 'sd_earn_wne_p10', 'md_earn_wne_p6', "
      "'sd_earn_wne_p6' below), so one column list is written in two conventions at once. The caption "
      "prints ABOVE and the lead sentence is 'In our data files, the missing data columns needed to be "
      "filled are listed as below'.",
      dict(rows=11, cols=4, header_rows=1, merged_cells=False, numeric_cols=2, text_cols=2,
           width="full", continued=False, **OPEN),
      CAPT1, "text-layer",
      cited(7, 7, ["Table 1"], 1,
            lead="the missing data columns needed to be filled are listed as below"),
      section_kind="model")

table(7, 2, S_22,
      "The integral columns, in the same two-block, four-column shape as Table 1, eighteen body rows "
      "numbered 1 to 9 and 10 to 18, header wording repeated in both blocks, same ruling (rule above "
      "the header, under the header, at the foot, verticals between columns, no outer edges, no rules "
      "between body rows). EVERY ENTRY IS A RAW DATABASE NAME with no gloss - PREDDEG, CONTROL, HBCU, "
      "PBI, ANNHI, TRIBAL, AANAPII, HSI, NANTI, MENONLY, WOMENONLY, PCIP_XXXXX, DISTANCEONLY, UGDS, "
      "UGDS_XXXXX, PPTUG_EF, PCTFLOAN, PCTPELL - and two of them ('PCIP_XXXXX', 'UGDS_XXXXX') still "
      "carry the literal mask XXXXX where a subject or a race breakdown should be. The caption is "
      "tinted 'Integral', a word the section never uses, over a list of variables. Caption prints "
      "ABOVE; lead sentence 'Following are some integral data columns for us to use'.",
      dict(rows=19, cols=4, header_rows=1, merged_cells=False, numeric_cols=2, text_cols=2,
           width="full", continued=False, **OPEN),
      CAPT2, "text-layer",
      cited(7, 7, ["Table 2"], 1, lead="Following are some integral data columns for us to use"),
      section_kind="model", order=2)

# ============================================================ 2.2: the cluster means
table(8, 1, S_22,
      "The k-means output used to impute missing earnings: three columns - an unlabelled cluster "
      "number, a 'Size' column and a header printed as the raw variable name 'md_earn_wne_p10' - over "
      "five rows, with sizes 27, 5, 1151, 1499 and 11 against means 19655.56, 24980.11, 31176.46, "
      "40780.52 and 42063.64. The ruling is open at both edges with vertical rules between all three "
      "columns and horizontal rules only above the header, under it and at the foot. THE CLUSTER SIZES "
      "ARE WILDLY UNEQUAL - two clusters of 5 and 11 schools against two of 1151 and 1499 - and the "
      "table gives no note that 'Size' is a count of schools, no total, and no cluster description, so "
      "which of the five means is being imputed into which column of which school is left to the "
      "prose. The values are centred, not decimal-aligned. Caption prints ABOVE ('Table 3: Clustering "
      "Output and Imputation Value'); lead sentence 'Following is the results of K-means clustering and "
      "an example of the imputation value of \"md_earn_wne_p10\"'.",
      dict(rows=6, cols=3, header_rows=1, merged_cells=False, numeric_cols=2, text_cols=1,
           width="half", continued=False, **OPEN),
      CAPT3, "text-layer",
      cited(8, 8, ["Table 3"], 1, lead="Following is the results of K-means clustering"),
      section_kind="model")

# ============================================================ 3.1: the weighted network
figure(12, 1, "node-link-network", CAP1, "text-layer",
       cited(11, 12, ["a picture"], 1,
             lead="we draw a picture to visually represent our ROI evaluation system"),
       S_31,
       "The ROI evaluation system drawn as a weighted network rather than a chart: eight labelled "
       "arrows feed three summing nodes and the three sums feed one output. Into the top sum, labelled "
       "'output', come Salary (w1), Enhance (w2), Retention (w3) and Repayment (w4). Into the bottom "
       "sum, labelled 'Urgency', come Federal Loan (w6), Pell Grant (w7) and Debt (w8). Net Price (w5) "
       "is the middle branch, and it runs through an EMPTY CIRCLE - no sum sign inside it, unlike the "
       "other two - and is labelled 'Input'. All three then meet at a final sum whose single outgoing "
       "arrow is labelled ROI, and the urgency branch's arrow into that last sum is labelled a^-1 "
       "rather than with a w, so one edge is written as a matrix inverse while its seven siblings are "
       "written as weights. No axes, no numbers, no scale, no legend and no title inside the frame. "
       "The second top-branch label reads 'Enhance', which no equation in the paper defines. Caption "
       "prints BELOW; the sentence that introduces it names no number - 'On the basis of the discussion "
       "above, we draw a picture to visually represent our ROI evaluation system.'",
       geometry("node-link-network", labels=True), "1", section_kind="model")

# ============================================================ 3.2: the grey prediction pair
figure(13, 1, "line", CAP2, "text-layer",
       cited(13, 13, ["figures"], 1,
             lead="Following are some figures of outcome of Grey Prediction for different schools"),
       S_32,
       "A TWO-PANEL figure, panels side by side, each a small blue-circle series with a smooth orange "
       "prediction curve over it: panel (a) rises from 0.011 at 2009 to 0.106 at 2023 and panel (b) "
       "falls from 0.054 at 2009 to 0.008 at 2023, against a 2008-to-2024 abscissa and ordinates of "
       "0.01 to 0.11 and 0.005 to 0.055. NEITHER AXIS IS NAMED, no panel names the school it belongs "
       "to, no year is marked as observed against predicted, and there is no legend - the only thing "
       "separating the observed points from the forecast is the colour of the marker against the colour "
       "of the curve, which collapses in greyscale. THE TWO SUBLABELS ARE IDENTICAL, '(a) Grey "
       "Predicting for Future ROI' and '(b) Grey Predicting for Future ROI', so neither panel says "
       "which of the two it is; the panel letter is the only discriminator. In panel (b) the observed "
       "point at 2012 sits at 0.026 while the fitted curve passes 0.043 there, and the fit still runs "
       "on to a forecast, so one of the two panels is a visibly poor fit used as if it were a "
       "confirmation. THE CAPTION IS AN UNPLACED PLACEHOLDER: 'Figure 2: general title.' - a template "
       "string the authors never replaced, and the pass marks it suspect for that reason.",
       geometry("line", panels=2, layout="1x2", labels=True), "2", section_kind="model")

# ============================================================ 4.2: the model's notation
table(14, 1, S_42,
      "The constants, printed as a two-column notation list with NO HEADER ROW AT ALL - a bare symbol "
      "in the left column and its gloss in the right, ten rows, a single vertical rule down the middle "
      "and a rule above the first row and below the last, no rule between any pair of rows. Symbols are "
      "set as ROI_i, r_i, A^max_i, A^min_i, s_i, N^max, N^min, r^max, S^min and A. THE CAPTION NAMES A "
      "CLASS THE LIST DOES NOT KEEP: it reads 'constant', yet ROI_i and r_i are described as 'derived "
      "from the pervious work' for each school (the paper's own wording), so two of the ten 'constants' "
      "vary school by school. The two school-count bounds are glossed 'maximum investment school number' "
      "and 'minimum investment school number', which names a count of schools as an investment. School "
      "size s_i is glossed 'number of student in school i' (singular). A is 'sum of the fund', the only "
      "row whose gloss carries no 'i in S'. THE TABLE PRINTS NO HEADER ROW and 'header_rows' holds the "
      "schema floor of 1. Caption prints ABOVE and no sentence names the table, the "
      "lead into it being 'Denote the list of candidate school is i ∈ S = {1, 2, ..., S}, the constant "
      "and the variables are as following.'",
      dict(rows=10, cols=2, header_rows=1, merged_cells=False, numeric_cols=0, text_cols=2,
           width="half", continued=False, **OPEN),
      CAPT4, "text-layer", section_kind="symbols")

table(14, 2, S_42,
      "The decision variables, in the same headerless two-column shape, two rows and a single vertical "
      "divider. Row one is x_i, 'Investment of school i, i ∈ S'. Row two is y_i ∈ {0, 1}, glossed "
      "'State of school i ,0 means not the the prize list, 1 means in the recommendation list ,0 means "
      "not in the recommendation list' - WHICH DEFINES ZERO TWICE, in two different words ('not the the "
      "prize list' and 'not in the recommendation list'), so the gloss for one value of a binary variable "
      "is written twice and the gloss for one is written not at all; 'the the' is printed, and spaces "
      "are set before the commas. The two rows are given unequal heights in the source, so the divider "
      "does not line up. Caption prints ABOVE ('Table 5: variable'); no sentence names the table.",
      dict(rows=2, cols=2, header_rows=1, merged_cells=False, numeric_cols=0, text_cols=2,
           width="half", continued=False, **OPEN),
      CAPT5, "text-layer", section_kind="symbols", order=2)

# ============================================================ 4.3: the fourteen schools
table(16, 1, S_43,
      "The fourteen schools the basic model selected, printed as three headerless columns - a bare rank, "
      "a bare six-digit UNITID and the institution name - over fourteen rows, in the model's own output "
      "order rather than alphabetical (1 Uta Mesivta of Kiryas Joel, 2 Florida Memorial University, 3 "
      "Everglades University, 4 United Talmudical Seminary, 5 Johnson Wales University-Charlotte, 6 "
      "Johnson Wales University-North Miami, 7 University of Maine at Farmington, 8 Washington & "
      "Jefferson College, 9 The Sage Colleges, 10 Baker College of Port Huron, 11 Juniata College, 12 "
      "SUNY College at Potsdam, 13 Knox College, 14 Johnson Wales University-Denver). THREE OF THE "
      "FOURTEEN ARE CAMPUSES OF ONE SYSTEM and two of those three are the same city's campuses, so a "
      "list presented as a diversified recommendation sends three fourteenths of the money to one "
      "university. NO COLUMN IS HEADED and nothing labels the rank or the UNITID, both of which are "
      "bare integers whose difference in width is the only cue. THE TABLE PRINTS NO HEADER ROW and "
      "'header_rows' holds the schema floor of 1. The names run to the column edge with no "
      "wrapping. Caption prints ABOVE and DUPLICATES TABLE 1'S - 'Table 6: Missing data columns' - over a "
      "list of institutions, the caption of a column inventory put on a shortlist. Ruling is a rule above "
      "the first row and one below the last with no verticals and no rule between rows. The table is "
      "named by no sentence; the lead into the page is on the previous page, 'we get a list of schools "
      "that should be recommended according to our model'.",
      dict(rows=14, cols=3, header_rows=1, merged_cells=False, numeric_cols=2, text_cols=1,
           width="full", continued=False, **OPEN),
      CAPT6, "text-layer", section_kind="result")

# ============================================================ 4.3: the four factors
figure(16, 2, "bar", CAP3, "text-layer",
       cited(17, 16, ["Figure(3)"], 1, lead="Figure(3) shows the factors of the ROI"),
       S_43,
       "A grouped bar chart with FOUR SERIES - risk, output, input, urgency - over FOURTEEN schools "
       "whose abscissa labels are bare UNITIDs (196200, 445708, 414823, 161226, 197018, 195128, "
       "446604, 133979, 213251, 146427, 216667, 439288, 385619, 381617). Legend below the plot inside "
       "the frame, four lowercase words; ordinate 0 to 2.5 with horizontal gridlines and no axis title; "
       "NO ABSCISSA TITLE and no unit on either axis. The chart's own top edge clips a stray glyph run. "
       "ONE BAR DOMINATES EVERYTHING: the risk bar for 446604 stands at 2.26 while every other risk bar "
       "is below 0.7 and all three other series sit between 0.5 and 0.95, so a single school's risk is "
       "plotted three times the range of every other quantity on the same axis and the four factors are "
       "compared on a scale only one of them needs. Reading the chart requires the UNITID-to-name "
       "mapping from Table 6 on the same page. Caption prints BELOW; the figure is named on the "
       "FOLLOWING page, 'Figure(3) shows the factors of the ROI, including risk, output, input and "
       "urgency, of the schools that is selected by our model.'",
       geometry("bar", legend="below", labels=True), "3", section_kind="result", order=1)

figure(16, 3, "other", CAP4, "text-layer",
       cited(17, 16, ["Figure(4)"], 1,
             lead="Figure(4) shows the money allocation of each selected schools"),
       S_43,
       "A PIE CHART of the money allocation, in-frame title 'ALLOCATION', fourteen slices labelled with "
       "bare UNITIDs and their percentages - 196200 13%, 445708 9%, 414823 8%, 161226 8%, 197018 7%, "
       "195128 7%, 446604 6%, 133979 6%, 213251 6%, 146427 6%, 216667 6%, 439288 6%, 385619 6%, "
       "381617 5% - under a legend row of fourteen numbered swatches (1 to 14) that duplicates the "
       "slice labels without adding the school names. NO VALUES, ONLY PERCENTAGES: the twelve millions "
       "of dollars each school receives are not on the figure, so the allocation it is captioned for "
       "cannot be read from it, and a pie is the one chart form in which fourteen parts of 5 to 13 per "
       "cent cannot be compared by eye. Six slices tie at 6% and the printed percentages sum to 96, so "
       "the residual 4% is spread silently across the rounded slices. Caption prints BELOW; named on "
       "the following page, 'Figure(4) shows the money allocation of each selected schools, the labels "
       "of both figures are the UNITID of the school.'",
       geometry("other", legend="above", labels=True), "4", section_kind="result", order=2,
       other_note="a pie chart: fourteen wedges on a circle with the UNITID and the percentage set "
                  "inside each wedge, an 'ALLOCATION' title inside the region and a row of fourteen "
                  "numbered swatches above the circle, with no axis, no scale and no dollar value")

# ============================================================ 4.4: the five-year allocation grid
figure(17, 1, "table-as-figure", CAP5, "text-layer",
       uncited(),
       S_44,
       "A PRINTED GRID NUMBERED AS A FIGURE: two identity columns (UNITID, INSTNM) and five year "
       "columns under a spanning header 'Investment in year i' headed 2016, 2017, 2018, 2019 and 2020, "
       "over fifteen school rows and a foot row 'sum of the money in the year'. Every cell is an amount "
       "in dollars with no unit stated and no decimals; most schools receive 5000000 in a single year "
       "and nothing in the other four. THE FOOT ROW DOES NOT ADD UP, BY A FACTOR OF TEN: the 2016 "
       "column's fifteen printed values sum to about 100.3 million (5000000 + 23960000 + 5000000 + "
       "5000000 + 14224000 + 5000000 + 5000000 + 0 + 0 + 5000000 + 0 + 0 + 13792000 + 0 + 18288000 + 0) "
       "while its foot cell prints 10000000, and the five foot cells sum to 100,000,000 although the "
       "model whose result this is states that 1000000000 is to be distributed. Three different totals "
       "for one allocation. Closed box with vertical rules between every column and horizontal rules "
       "between every row. Caption prints BELOW; no sentence names it as a figure, the lead being 'get "
       "the global optimal solution and receive the following result'.",
       geometry("table-as-figure", numbers=True), "5", section_kind="result")

# ============================================================ 5.1 and 5.2: the two sensitivity curves
figure(18, 1, "line", CAP6, "text-layer",
       cited(18, 18, ["figure(6)"], 1,
             trail="From the figure(6), we find that as the max acceptable risk become greater"),
       S_51,
       "A single thin blue curve, no markers, no gridline, in a full frame: 'max return' against 'max "
       "acceptable risk', the ordinate carried by a floating multiplier 'x 10^7' over the range 4 to "
       "5.5 and the abscissa running 0.2 to 1.0. The curve rises almost linearly to 0.6, curves over "
       "and FLATTENS COMPLETELY past about 0.85, so the last three ticks buy nothing. Axes ARE named "
       "here, unlike Figures 3 and 5; there is no legend, no title, no marker at the point the model "
       "chose, and no unit on either axis (the ordinate's dollars are implied by nothing but the "
       "magnitude). Caption prints BELOW and the reference comes after it, 'From the figure(6), we find "
       "that as the max acceptable risk become greater, the max return we can get also become greater'.",
       geometry("line"), "6", section_kind="sensitivity")

figure(19, 1, "line", CAP7, "text-layer",
       cited(19, 19, ["figure(7)"], 1,
             trail="From the figure(7), we find that as the number of the schools ought to be chosen"),
       S_52,
       "A second single thin blue curve in the same frame: 'max return' against 'awarded school number "
       "in each year', ordinate 1.4 to 1.75 under a floating 'x 10^8', abscissa 4 to 24. The curve "
       "climbs steeply from 1.4 at four schools, peaks at about 1.705 at twelve and then declines "
       "steadily to 1.60 at twenty-four, so the plot's own optimum is twelve schools. THE TWO "
       "SENSITIVITY CURVES DISAGREE ON THE SAME QUANTITY: Figure 6 caps max return at 5.5 x 10^7 while "
       "Figure 7 reaches 1.75 x 10^8, a factor of three higher for the same maximand under a different "
       "sweep, and neither caption or sentence reconciles them. The text reads the peak as a validation "
       "of its own list - 'The optimal school number is about 12, which lies in our model's school "
       "number constraint between 10 and 30' - which the curve cannot establish, since a constraint "
       "that already excludes everything outside 10 to 30 makes any interior peak inside it "
       "unsurprising. Caption prints BELOW; the reference follows it in running text.",
       geometry("line"), "7", section_kind="sensitivity", order=1)

# ============================================================ 5.3: the policy comparison
table(19, 2, S_53,
      "The four distribution policies compared on two numbers: a header 'policy | max return | gap' "
      "over four rows numbered 1 to 4, with max returns 54579267, 157020989, 169677616 and 17545328 and "
      "gaps 0.689, 0.107, 0.035 and A DASH - the last policy's gap cell prints no number at all, in a "
      "column whose header promises one. THE 'policy' COLUMN IS A BARE INDEX: the four policies are "
      "described only in the prose that follows (all in year one, evenly at 200000000 a year, uneven "
      "with bounds, and a fourth never named in the row), so the row of the table cannot be matched to "
      "the policy it reports without reading the next paragraph. 'max return' gives no currency and "
      "'gap' is never defined. Ruling is open at the edges with vertical rules between all three "
      "columns and horizontal rules only above the header, under it and at the foot; the numbers are "
      "right-aligned, not decimal-aligned. Caption prints ABOVE ('Table 7:  return-policy', with the "
      "double space printed) and no sentence names the table.",
      dict(rows=5, cols=3, header_rows=1, merged_cells=False, numeric_cols=2, text_cols=1,
           width="half", continued=False, **OPEN),
      CAPT7, "text-layer", section_kind="solution")

# ============================================================ the second panel of Figure 2
EXCLUDED.append({
    "page": 13, "bbox": REG[(13, 2)], "reason": "fragment-of-other",
    "note": "The second panel of Figure 2. The measured regions of p13 both sit on the same "
            "abscissa band, one from x = 196 to 904 and one from x = 749 to 1457, i.e. the left and "
            "right halves of one two-panel figure whose single caption, 'Figure 2: general title.', "
            "prints under the pair. The figure is recorded once as a two-panel row; this region holds "
            "panel (b), the falling series.",
})

RULES = [
    "Measure first, then read the pixels: fifteen measured regions resolve into seven figure rows, "
    "seven table rows and one exclusion, and every region is accounted for once [place.doc_order].",
    "A figure can be two measured regions: p13's two regions are the left and right panels of one "
    "two-panel figure sharing one caption, so the second is an exclusion rather than a row of its own "
    "[geometry.panel_count].",
    "A caption can be an unfilled template: Figure 2 prints 'Figure 2: general title.' and both its "
    "panels are sublabelled 'Grey Predicting for Future ROI', naming no school [caption.verbatim].",
    "A caption can be copied from another table: Table 6 prints 'Table 6: Missing data columns', the "
    "same three words Table 1 uses, over a list of fourteen institutions [caption.verbatim].",
    "An exhibit's own arithmetic can be a tenth of itself: Figure 5's 2016 column sums to about 100.3 "
    "million while its foot cell prints 10000000, and the five foot cells sum to 100,000,000 against "
    "the 1000000000 the model says it distributes [table.numeric_cols].",
    "A printed grid can be numbered as a figure: Figure 5 is a fifteen-row allocation table with a "
    "foot row, recorded as a table-as-figure rather than as a chart [geometry.family].",
    "A chart can require another exhibit to be read: Figures 3 and 4 label their categories with bare "
    "UNITIDs and the mapping is the institution list in Table 6 [geometry.data_labels].",
    "Two sensitivity curves can disagree about one quantity: Figure 6 caps max return at 5.5 x 10^7 "
    "and Figure 7 reaches 1.75 x 10^8, and no sentence reconciles them [geometry.shared_axes].",
    "Citation is uneven and often unnumbered: six figure rows are named by a sentence but only four "
    "carry a number at the point of naming, Figure 1 is introduced as 'a picture' and Figure 2 as "
    "'figures', Figure 5 is named by no sentence at all, and Tables 4, 5, 6 and 7 by none "
    "[mention.count].",
]

NOTE = """\
Paper 101, Team 50193: screen 2977 colleges to a shortlist, impute missing IPEDS columns by k-means,
score ROI through an AHP-weighted network, and allocate a budget by mixed-integer programming, first
without and then with the five-year time axis. Twenty-four pages, fifteen measured regions over nine
of them, resolving into SEVEN FIGURE ROWS, SEVEN TABLE ROWS and ONE EXCLUSION, with nothing
unaccounted.

Tables 1 and 2 are the same shape - two side-by-side blocks of 'Number | Variable Name', four physical
columns, the header wording repeated in both blocks, no rule between body rows and no outer edge rule.
Table 1 mixes registers inside one list: 'Net Price' and 'Retention Rate' are prose, the other eight
are raw database names in two different casings. Table 2 is entirely raw, and two of its entries still
carry the literal mask 'XXXXX' where a subject or race breakdown belongs. Table 3 prints five k-means
cluster sizes of 27, 5, 1151, 1499 and 11 against their mean earnings, in a table whose third header
cell is the variable name 'md_earn_wne_p10'.

Figure 1 is the ROI network: eight weighted arrows into three sums - output, Input, Urgency - and one
ROI node. The Input branch runs through an empty circle with no sum sign while the other two carry one,
and the urgency arrow into the final sum is labelled a^-1 where every sibling edge is a w. The label
'Enhance' is defined by no equation in the paper.

Figure 2 has two panels and no caption: it prints 'Figure 2: general title.', the template string the
authors never replaced. Both sublabels read 'Grey Predicting for Future ROI', so neither panel names
its school, and in panel (b) the observed point at 2012 sits at 0.026 while the fitted curve passes
0.043 there before forecasting twenty years out.

Tables 4 and 5 are the model's notation, printed as two-column symbol/definition lists with no header
row at all and a single vertical divider. Table 4's caption is 'constant' although it includes
per-school quantities (ROI_i, r_i, s_i, A_i), and its two rows for the school-count bounds read
'maximum investment school number' and 'minimum investment school number'. Table 5's y_i cell defines
zero twice in adjacent lines - '0 means not the the prize list' and '0 means not in the recommendation
list'.

Table 6 lists the fourteen selected institutions under Table 1's caption, word for word - 'Missing
data columns' - with no header row, an unlabelled six-digit UNITID column, and an arbitrary order.

Figures 3 and 4 come in one page: a grouped bar chart of four factors over fourteen schools and a pie
of the allocation. The bar chart's legend is below the frame, the abscissa is bare UNITIDs with no
title, and the risk bar for school 446604 stands at 2.26 while every other quantity on the chart is
under 0.95, so one outlier sets the scale for four series. The pie is titled 'ALLOCATION', labels its
fourteen slices with UNITIDs and percentages that sum to 96, prints no dollar value at all, and
duplicates its slices in a legend row of numbers 1 to 14 that add no information. Reading either
figure requires Table 6's list.

Figure 5 is a printed grid numbered as a figure: fifteen schools against the years 2016 to 2020 under
'Investment in year i', with a foot row 'sum of the money in the year'. The 2016 column's fifteen
values sum to about 100.3 million while the foot cell prints 10000000; the five foot cells sum to
100,000,000; and the model whose result this is distributes 1,000,000,000. Three totals for one
allocation.

Figures 6 and 7 are the sensitivity sweeps, both single thin curves with named axes. Figure 6 flattens
completely past a risk of 0.85. Figure 7 peaks at twelve schools and declines after, which the text
reads as validating its own list - but the constraint it invokes already excludes everything outside
10 to 30. The two curves disagree about the same maximand: Figure 6 tops out at 5.5 x 10^7 and Figure
7 at 1.75 x 10^8.

Table 7 compares four distribution policies on 'max return' and 'gap', with the policies identified
only in the following paragraph and the fourth row's gap cell printing a dash.

Families: table-grid 7, line 3, bar 1, node-link-network 1, other 1, table-as-figure 1.
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

out = PROXY / "pc101-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
