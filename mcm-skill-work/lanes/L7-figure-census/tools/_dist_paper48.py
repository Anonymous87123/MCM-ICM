"""Hand pass for P-B-2013-21185-c7f22f59 (a Chinese water-resources strategy paper: water demand
forecasting, storage and transfer, desalination, pollution control, water-saving), 43 pp.

Forty-one measured regions resolve to 37 counted rows and 4 exclusions... no: 39 counted rows
(22 figure rows + 17 printed tables) and 2 exclusions - the two display equations on p24. The
arithmetic that `check.py` enforces is 22 + 17 + 2 = 41.

    p5-r1   table   Nomenclatures (glossary grid, 2 cols)
    p6-r1   table   the same glossary continued
    p7-r1   table   China's water use 1997-2010
    p7-r2   line    demand for water resources over time
    p8-r1   scatter observations with a linear fit
    p8-r2   scatter observations with quadratic and power fits
    p8-r3   scatter observations with three fits overlaid
    p9-r1   table   forecast 2013-2025 by three fitting methods
    p10-r1  schematic  decomposition of water consumption into drivers
    p11-r1  line    four single-line panels (demand, agriculture, industry, live)
    p12-r1  line    three dual-axis panels (use against population/food/GDP)
    p12-r2  table   correlation degrees of consumption factors
    p14-r1  line    GM prediction
    p14-r2  table   residual, relative and limit deviation of the GM prediction
    p15-r1  table   forecast 2013-2025 (year/value bands)
    p17-r1  line    31 provincial surface-water series, 2000-2010
    p18-r1  table   province CV and benefit ranking, head
    p19-r1  table   the same ranking continued
    p20-r1  map     China's nine watersheds
    p20-r2  map     China's three terraces
    p22-r1  table-as-figure  colour-scaled water supply pressure alpha
    p22-r2  map     water supply pressure choropleth
    p22-r3  table   province numbering, rows 9-16
    p23-r1  table   the same numbering, rows 17-31
    p25-r1  map     six optimal water transfer routes
    p26-r1  table   desalination terminology
    p27-r1  line    the optimal desalination build year
    p29-r1  table   pollution-control terminology
    p30-r1  table   demand, resources and pressure per watershed
    p31-r1  bar     demand for pollution control by watershed
    p31-r2  table   three cities of the Hai watershed
    p33-r1..r5  table-as-figure  beta per province, five shaded blocks, 31 provinces
    p35-r1  schematic  AHP hierarchy of the evaluation
    p37-r1  table   neural-network strategy ratings

Excluded: p24-r1 and p24-r2, the objective function and the constraint set, `in-body-diagram`.

Captions: this paper numbers no exhibit at all. Five caption lines print as bare "Figure" or
"Figure." with no digit, so their records carry `numbering: none` and the word is quoted as printed;
the p22 caption is garbled in the text layer ("Figure Colored Graph Based on at r pply pr r α") and
is typed from the crop instead. Every other exhibit is introduced by prose alone ("as shown below",
"the figure above"), so it records `caption_source: none`.

Usage: python -I tools/_dist_paper48.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2013-21185-c7f22f59"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

NOMEN = "2 Nomenclatures"
M1 = "3 Model one: Water demand and supply Forecast"
S331 = "3.3.1 Analysis of China\u2019s water use"
S33 = "3.3 Function Fit Model"
S333 = "3.3.3 Prediction Results and Conclusion"
S341 = "3.4.1 Reasons for Improvement"
S342 = "3.4.2 Correlation Degree Analysis"
S346 = "3.4.6 Results and Conclusions"
S423 = "4.2.3 Model Solution"
S424 = "4.2.4 Conclusion"
S432 = "4.3.2 Backgrounds and Water Movement Principles"
S433 = "4.3.3 Model Analysis"
S434 = "4.3.4 Objective Function of water transfer strategy"
S435 = "4.3.5 Model Testing"
S437 = "4.3.7 Conclusion"
S52 = "5.2 Terminology"
S55 = "5.5 Model Solving"
S623 = "6.2.3 Terminology"
S625 = "6.2.5 Model solution:"
S626 = "6.2.6 Model analysis:"
S632 = "6.3.2 Analysis and Conclusion"
S73 = "7.3 Evaluation of Economic, Physical, and Environmental"
S742 = "7.4.2 Conclusion"

PATH = {
    5: ([NOMEN], "symbols"),
    6: ([M1], "symbols"),
    7: ([S331], "result"),
    8: ([S33], "model"),
    9: ([S333], "result"),
    10: ([S341], "model"),
    11: ([S342], "model"),
    12: ([S342], "model"),
    14: ([S346], "result"),
    15: ([S346], "result"),
    17: ([S423], "model"),
    18: ([S423], "model"),
    19: ([S424], "model"),
    20: ([S432], "other"),
    22: ([S433], "model"),
    23: ([S433], "model"),
    24: ([S434], "model"),
    25: ([S437], "result"),
    26: ([S52], "model"),
    27: ([S55], "model"),
    29: ([S623], "model"),
    30: ([S625], "model"),
    31: ([S626], "model"),
    33: ([S632], "result"),
    35: ([S73], "evaluation"),
    37: ([S742], "evaluation"),
}
# the two equations on p24 sit under different headings from the table that follows them
PATH_ONE = {(24, 2): ([S435], "model")}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

VENTION = {5: 1, 6: 1, 7: 2, 8: 3, 9: 1, 10: 1, 11: 1, 12: 2, 14: 2, 15: 1, 17: 1,
           18: 1, 19: 1, 20: 2, 22: 3, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 29: 1,
           30: 1, 31: 2, 33: 5, 35: 1, 37: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: list[dict] = []
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}

CAP_P22 = "Figure Colored Graph Based on water supply pressure \u03b1"


def printed(page: int, text: str) -> str:
    """Verify a caption string really prints on the page, once Unicode-normalised."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text))
    return text


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH_ONE.get((page, reg), PATH[page])
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, source: str, position: str) -> dict:
    return {
        "verbatim": text,
        "numbering": "none",
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": position,
    }


def figure(page: int, reg: int, family: str, caption_text: str = "", *, source: str = "none",
           position: str = "above", panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = True, labels: bool = False,
           other_note: str = "", note: str = "") -> None:
    ORDER.append((page, reg))
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg),
        "mention": dict(NULL_MENTION),
        "caption": caption_block(caption_text, source, position),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, caption_text: str = "", *, source: str = "none",
          rows: int, cols: int, header_rows: int = 1, rules: str = "booktabs",
          numeric_cols: int = 0, text_cols: int = 0, merged: bool = False,
          continued: bool = False, note: str = "") -> None:
    ORDER.append((page, reg))
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": caption_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg),
        "mention": dict(NULL_MENTION),
        "caption": caption_block(caption_text, source, "above"),
        "table": {
            "rows": rows, "cols": cols, "header_rows": header_rows,
            "rule_style": rules, "zebra": False, "merged_cells": merged,
            "diagonal_header": False, "units_in_header": False,
            "decimal_aligned": False, "numeric_cols": numeric_cols,
            "text_cols": text_cols, "width": "full", "orientation": "portrait",
            "continued": continued, "note_sentence": "",
        },
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note})


def build() -> str:
    # --- Model one: data, fits and forecasts --------------------------------------------
    table(5, 1, rows=38, cols=2, numeric_cols=0, text_cols=2,
          note="The paper's notation list, ruled as a two-column grid and headed by the "
               "section title 'Nomenclatures' rather than by a table caption: 38 printed rows of "
               "symbol | definition (D = the fresh water demand of a region, GDP = gross domestic "
               "product, omega = the edge weights of the national water transfer network). A rule "
               "between every row and no vertical rules. No header row is printed; the header sits "
               "in the section heading, so `header_rows` keeps the schema minimum.")
    table(6, 1, rows=5, cols=2, numeric_cols=0, text_cols=2, continued=True,
          note="The last five rows of the same notation grid, continued over the page break: "
               "W_kj, C_kj, COD, cod_kj and B. No header and no repeated section title, so the "
               "record keeps `header_rows` at 1 and this note stands for the missing one; two "
               "definitions wrap onto a second line inside their cell.")
    table(7, 1, rows=4, cols=8, header_rows=2, numeric_cols=7, text_cols=1,
          note="China's water use 1997-2010, printed as two stacked half-bands because the years "
               "will not fit on one line: 'Water 1997 ... 2003' over 5566 ... 5320.4, then "
               "'Water 2004 ... 2010' over 5547.8 ... 6021.99, with the unit "
               "'100 million m^3' stacked in the stub. Two year headers, so `header_rows` is 2; "
               "horizontal rules only and no vertical rules.")
    figure(7, 2, "line",
           note="One thin blue curve through the fourteen annual values, y 'Water consumption / "
                "Million m3' from 5300 to 6100 by 100, x 'year' 1996 to 2010 by two. In-figure "
                "title 'Demand for water resouces changes with time curve in China' (the typo is "
                "printed); no markers, no legend, no gridlines, plain boxed axes. Exported as a "
                "raster inside the page, so the vector layer holds none of its text.")

    figure(8, 1, "scatter", legend="inside", layout="1 of 2",
           note="Left half of a two-figure row: the fourteen annual observations as small purple "
                "markers with one straight red line through them, legend inside the upper left "
                "with two entries, 'water_consumption vs. year' and 'linear fitting'. Dashed "
                "gridlines at every major tick, y 5400 to 6000 by 100, x 1998 to 2010 by two, no "
                "axis titles and no in-figure title. The markers are the data, so the family "
                "follows them and not the fitted line.")
    figure(8, 2, "scatter", legend="inside", layout="2 of 2",
           note="Right half of the same row: the same fourteen markers with a U-shaped quadratic "
                "fit and a rising power fit, legend inside the upper left with three entries "
                "('water_consumption vs. year', 'quadratic fitting', 'power fitting'). y 5400 to "
                "6100 by 100, x 1998 to 2010 by two. Printed as its own measured raster with its "
                "own axes, and the paper calls the pair 'the two linear and non-linear figures'.")
    figure(8, 3, "scatter", legend="inside",
           note="A single wide plot holding the observations twice over: one marker set and a "
                "five-entry legend inside the upper left - 'total_water_consumption vs. year', "
                "'linear fitting', 'power fitting', 'total_water_consumption vs. year (smooth)' "
                "and 'shape-preserving fitting'. The red piecewise curve rises, flattens over "
                "2000-2001 and climbs again after 2005, the shape-preserving fit the text calls "
                "'interpolant'. x labelled for every year 2000-2010, y 5400 to 6000 by 100.")
    table(9, 1, rows=14, cols=4, numeric_cols=3, text_cols=1,
          note="Forecast by three fitting methods: header 'Year | Linear fitting | Power fitting | "
               "Interpolant fitting' over thirteen body rows, 2013 to 2025, values 6166.41 to "
               "7028.3. Horizontal rule under the header only, plus the closing rule. The record "
               "counts the thirteen data rows and the header; no units are printed in the cells "
               "and the unit is stated in the surrounding sentence.")

    # --- Model one: grey forecasting ----------------------------------------------------
    figure(10, 1, "flowchart-or-schematic", labels=True,
           note="A three-level breakdown, not a plot: one rounded box 'Water consumption' over "
                "three rounded boxes (agricultural, industrial, live water consumption), which in "
                "turn open onto the drivers - food production, population and agricultural GDP for "
                "the first, industrial GDP for the second, population and GDP for the third. Thin "
                "straight connectors, no arrowheads, no shading, no legend. Live vector boxes and "
                "type; the typo 'Agricultrual' is printed in the box.")
    figure(11, 1, "line", panels=4, layout="2x2", legend="none",
           note="Four single-line charts on one measured raster, each with its own grey frame and "
                "boxed axes: total demand, agricultural demand, industrial demand and live demand "
                "against year 1996-2010. In-figure titles read 'Water resources demand changes "
                "curve in China', 'Agriculture water demand changes curve in China', 'Industrial "
                "water demand changes curve in China' and 'Live water demand changes with in "
                "China' (printed as is); each y title is 'Consumption/Million m3'. One family in "
                "four panels, so the family stays `line` with a panel count.")
    figure(12, 1, "line", panels=3, layout="3x1", legend="inside",
           note="Three stacked dual-axis panels over 1996-2010: water use against population, "
                "water for agriculture against food production, and water for industry against "
                "industrial GDP. A red solid series on the left axis and a black dash-dot series "
                "on the right axis per panel, legend inside the upper right of each, units "
                "'hundred million m3', 'million', 'million tons' and '10^4' printed in the series "
                "names. The top tick of two panels is clipped in the source raster.")
    table(12, 2, rows=10, cols=4, numeric_cols=2, text_cols=2, merged=True,
          note="Correlation degrees of the drivers: a bold title row 'Water Consumption "
               "Correlation Analysis' spanning all four columns, then 'Factors | Associate "
               "degree(1) | Sub-factors | Associate degree(2)'. Three factor blocks with the "
               "second column merged across the sub-factor rows (0.9998, 0.9997, 0.3746) and "
               "right-hand values 0.9388, 0.9090, 0.6799, 0.7053, 0.9022, 0.7081. The title is "
               "printed inside the grid, not as a caption; horizontal rules between blocks only.")
    figure(14, 1, "line", legend="none",
           note="'GM Prediction': observed years as open-circle markers joined by thin segments "
                "with one green straight fit drawn through them out to 2025. x 'Year' 1995-2025 by "
                "five, y 'Water consumption' 5200 to 6800 by 200, no legend, no gridlines. The "
                "curve dips at 2003 and the fit ignores the dip - the point of the paragraph "
                "under it.")
    table(14, 2, rows=12, cols=6, numeric_cols=5, text_cols=1,
          note="The residual analysis of the grey prediction: 'Year | Actual water consumption | "
               "Predicted water consumption | Residual Error | Relative Error | Limit Deviation "
               "Value' over eleven body rows, 1999 to 2009 (5613.3 / 5484.9 / 128.5 / 0.0229 / "
               "0.0176 for the first). Header words wrap onto three lines inside their cells; no "
               "rules are drawn in this band, the grid is held by alignment alone.")
    table(15, 1, rows=3, cols=8, continued=True,
          note="The tail of the 2013-2025 forecast, printed transposed: 'Water Consumption' over "
               "6143.9 to 6449.1, then 'Year' over 2020 to 2025, then 'Water Consumption' over "
               "6501.5 to 6770.1. The 2013-2019 block and the table's own header print above the "
               "measured band on p15 and are counted here; horizontal rules only.")

    # --- Model two: storage and transfer ------------------------------------------------
    figure(17, 1, "line",
           caption_text=printed(17, "The 2000-2010 line graph of surface water resources in "
                                    "China provinces"),
           source="text-layer", position="above", legend="outside-right", numbers=True,
           note="Thirty-one provincial series on one pair of axes, 2000-2010, drawn with a "
                "different marker per province and listed two-column in a legend at the right. y "
                "0 to 35000 by 5000 with faint gridlines and no axis title; the series stack into "
                "three bands that all dip at 2004 and 2009 and climb steeply in 2010. The line "
                "above the picture is the only caption-like line in the paper that is not the "
                "word 'Figure': it prints as a sentence, not as 'Figure N'.")
    table(18, 1, rows=4, cols=4, numeric_cols=3, text_cols=1,
          note="The head of the province ranking: 'Province | CV | delta O | eta', three body "
               "rows (Ningxia 0.206058 / 4.77 / 7.030023, Beijing, Tianjin) with the province "
               "column shaded pale blue. The header prints just above the measured band and is "
               "counted in `rows`; thin horizontal rules only. The ranking runs onto p19.")
    table(19, 1, rows=17, cols=4, numeric_cols=3, text_cols=1, continued=True,
          note="The same ranking continued: seventeen rows from Shanghai to Jiangxi with the "
               "province column shaded along a pale-blue-to-orange gradient that tracks the CV "
               "order. No header is repeated on this page - `header_rows` keeps the schema "
               "minimum and this note stands for it. Watermarks cross the right-hand columns; the "
               "shading is decoration, not a separate exhibit.")

    # --- Model two: background maps and parameters --------------------------------------
    figure(20, 1, "map-or-plan-view",
           caption_text=printed(20, "Figure China\u2019s Nine Watersheds"),
           source="text-layer", position="above", numbers=False,
           note="A greyscale map of China with the nine first-order basins divided by thick dark "
                "strokes and labelled Songliao, Hai, Huai, Yellow, Yangtze, Pearl, Southeast, "
                "Southwest and Northwest. No axes, no scale bar, no legend, no values: the "
                "labelled region is the exhibit. Caption prints above, with no number.")
    figure(20, 2, "map-or-plan-view",
           caption_text=printed(20, "Figure. China\u2019s Three Terrace"),
           source="text-layer", position="above", legend="inside", numbers=False,
           note="A coloured relief map of China titled 'CHINA' in the image's own black bar, three "
                "heavy curved boundaries dividing it into THE FIRST, SECOND and THIRD TERRACE, "
                "with the source map's legend box and scale bar at the bottom. Captioned above "
                "with no number, one period after the word 'Figure'.")
    figure(22, 1, "table-as-figure", caption_text=CAP_P22, source="typed-from-crop",
           position="below", panels=5, layout="5 stacked bands", numbers=True,
           note="A colour-scaled grid of the signed water supply pressure offset (alpha minus its "
                "mean) for all 31 provinces, printed as five shaded blocks running from deep blue "
                "through pale orange to bright orange, each block a header row of province names "
                "over one value row (Tibet -0.26262 climbing to Ningxia 2.53323). A screenshot of "
                "a spreadsheet colour scale, so it is one raster, not live cells. The paper "
                "numbers it as a Figure, so it stays in the figure block as `table-as-figure`; the "
                "caption is garbled in the text layer ('Figure Colored Graph Based on at r pply pr "
                "r alpha') and is typed from the crop.")
    figure(22, 2, "map-or-plan-view", caption_text=CAP_P22, source="typed-from-crop",
           position="above", legend="inside", numbers=False,
           note="The map the grid above keys: China with each province filled on the same "
                "blue-to-orange scale as its alpha offset, province names in English, a thin red "
                "river and boundary network and a small legend mark at the upper left. No printed "
                "colour values - the classes are readable only against the block above. Shares "
                "the caption that prints between the grid and the map.")
    table(22, 3, rows=2, cols=9, text_cols=9, continued=True,
          note="The province numbering for the model, printed two rows at a time with no grid: a "
               "header row 'Province' with thirteen names and an index row 'i' under it. The "
               "measured band holds rows for indices 9-16; the indices 1-8 row prints immediately "
               "above it and is counted with this record, which stays `continued` because the "
               "table runs on to p23. Several province names wrap inside their narrow cells "
               "('Shanx i', 'Heilo ngjia ng').")
    table(23, 1, rows=5, cols=9, text_cols=9, continued=True,
          note="The same numbering continued over the page break: indices 17-24, 25-31 and a "
               "trailing row of names with an empty last cell (Yunnan through Xinjiang). No "
               "header is repeated at the top of p23, so `header_rows` keeps the schema minimum "
               "and this note stands for it.")
    table(24, 3, rows=6, cols=6, numeric_cols=5, text_cols=1, rules="no-rules",
          note="The worked Beijing example: five province columns (Hunan, "
          "Jiangxi, Fujian, Sichuan, Guizhou) over five rows - d_i,1 distance, b_i, c_i, delta w "
          "and the relative efficiency eta (0.10968278 down to 0.084805997). Borderless: no "
          "vertical and no horizontal rules, alignment alone, which is why the header row prints "
          "above the first measured rule. The row label printed 'c_i' disagrees with the model's "
          "own symbol e_i.")
    figure(25, 1, "map-or-plan-view",
           caption_text=printed(25, "Figure. Six Optimal Water Transfer Routes of China"),
           source="text-layer", position="above", legend="inside", numbers=True,
           note="The alpha choropleth again with six numbered green routes drawn across it, each "
                "route a straight segment between provincial nodes. Route numbers 1-6 are printed "
                "on the map; no legend ties a number to its province, and the text below names "
                "only routes 4, 5 and 6 (the Middle, West and Eastern Route schemes).")

    # --- Model three: desalination -------------------------------------------------------
    table(26, 1, rows=7, cols=2, text_cols=2, rules="boxed",
          note="The desalination notation list: D0, Theta, T, p, p0, t_opt and sigma against "
               "their definitions, printed under the heading '5.2 Terminology'. A rule after the "
               "symbol column and between every row - the only cells in this paper drawn with a "
               "vertical rule besides the pollution glossary and the strategy table. No caption "
               "and no header row.")
    figure(27, 1, "line", legend="none", numbers=False,
           note="One ascending blue line with faint markers inside a fully ticked frame, x "
                "labelled 2012-2026 and y carrying no numbers at all, only the rotated title "
                "'water consumption'. The magnitudes are annotated instead of scaled: D0 at the "
                "origin, D = D0 + 0.5 theta t_opt and D0 + 0.5 theta (t_opt + T) beside two "
                "horizontal brackets, and the axis marks '2013+t_opt' and '2013+T'. Because the y "
                "axis is unnumbered the line's values cannot be read off.")

    # --- Model four: pollution control ---------------------------------------------------
    table(29, 1, rows=11, cols=2, text_cols=2, rules="boxed",
          note="The pollution-control notation list under '6.2.3 Terminology': gamma_k, alpha_k, "
               "the three water-quality grades I, II and III, rho_k, mu_k,j, W_kj, C_kj, COD and "
               "cod_kj, eleven rows with a vertical rule after the symbol column and a rule "
               "between rows. No caption, no header row.")
    table(30, 1, rows=6, cols=10, numeric_cols=9, text_cols=1,
          note="The watershed data and solution: header row of the nine basins over the index row "
               "k = 1..9, then rho_k as percentages (43.1% to 90.3%), D_k and W_k in 10^8 m^3, and "
               "the dimensionless alpha_k and gamma_k. Nine data columns; horizontal rules only. "
               "The region measures the six printed rows below the header, which prints just "
               "above it and is counted in `rows`.")
    figure(31, 1, "bar", legend="none", numbers=True,
           note="Nine solid cyan bars on a grey plate inside a four-sided frame, x 'k: the number "
                "of watershed' 1-9 and y 'gamma_k: Demand for water treatment degrees' 0 to 1.8 "
                "by 0.2. No value labels, no legend, no gridlines; the bar for watershed 2 stands "
                "about six times the tallest of the rest, which is the sentence under it. The axis "
                "titles survive only in the raster, so this is an exported picture, not live text.")
    table(31, 2, rows=4, cols=4, numeric_cols=3, text_cols=1,
          note="The Hai watershed worked in three cities - Datong, Beijing, Tianjin - over three "
               "rows: water consumption and water resources in 10^8 m^3 and the formula stub "
               "alpha_kj / W_kj times a decreasing sum. The city header prints just above the "
               "measured band and is counted in `rows`; horizontal rules only, units carried in "
               "the row stubs.")

    # --- Model five: water saving --------------------------------------------------------
    cap33 = printed(33, "Figure. Classification of Water Consumption of a Unit GDP "
                        "(\U0001d6c3)")
    BETA_BLOCKS = [
        (1, "0.005079 to 0.014475", "Beijing, Tianjin, Shandong, Shanghai, Shanxi, Zhejiang and "
                                    "Liaoning"),
        (2, "0.0177 to 0.0248", "Shanxi, Henan, Hebei, Guangdong, Chongqing, Fujian, Sichuan, "
                                "Jiangsu and Jilin"),
        (3, "0.032379 to 0.043392", "Hubei, Anhui, Inner Mongolia, Yunnan, Hunan, Guizhou and "
                                    "Hainan"),
        (4, "0.046207 to 0.063333", "Qinghai, Jiangxi, Heilongjiang, Gansu and Guangxi"),
        (5, "0.10345 to 0.176276", "Ningxia, Tibet and Xinjiang"),
    ]
    for reg, span, body in BETA_BLOCKS:
        figure(33, reg, "table-as-figure", caption_text=cap33, source="text-layer",
               position="above", numbers=True,
               note=f"Block {reg} of five: a shaded header band of province names over one beta "
                    f"row, values {span}. This block carries {body}. The five blocks print as five "
                    "separate framed blocks in one ascending ranking of all 31 provinces, one "
                    "caption over the set ('Figure. Classification of Water Consumption of a Unit "
                    "GDP (beta)'), and the paper later calls it 'the table above' - a grid "
                    "numbered as a figure, so `table-as-figure` with the caption quoted once per "
                    "measured block.")

    # --- Model six: evaluation -----------------------------------------------------------
    figure(35, 1, "flowchart-or-schematic", labels=True, numbers=False,
           note="The analytic-hierarchy tree printed as the paper's evaluation figure: a bordered "
                "box 'Evaluation Results' above three unboxed criteria (economic, physical and "
                "environmental impact) above four strategy classes (storage, movement, "
                "de-salination, sewage treatment) above the box 'Strategies which needs to value', "
                "with the three tiers labelled in the left margin as target, rule and measure "
                "hierarchy. The middle-to-bottom connectors cross densely; there are no values, no "
                "weights and no legend on the drawing. An exported picture: none of its labels "
                "survive in the text layer.")
    table(37, 1, rows=6, cols=6, numeric_cols=5, text_cols=1, rules="boxed",
          note="The neural-network input matrix: five strategy rows (Three Gorges Reservoir, the "
               "South-North Water Transfer Project, Tianjin Dagang Desalination Plant, Taihu Lake "
               "Sewage Treatment, Others) against the five impact columns e_c_i, ph_i, en_i, "
               "others_i, de_i, rated 1 to 10, the Others row carrying ellipses. A full cell "
               "grid, vertical and horizontal rules, header cell over the strategy column left "
               "blank; the note '(All various numerical range is 1-10)' prints under the grid.")

    # --- excluded regions ---------------------------------------------------------------
    excluded(24, 1, "in-body-diagram",
             "A displayed equation inside the argument of section 4.3.4, not an exhibit: the "
             "objective function z = min{ eta = delta w / E = min{|delta w_i|, |delta w_j|} / E } "
             "over the constraint set b_i <= b_j, e_i != e_j, delta w_i < 0 < delta w_j. Live "
             "vector math, no frame, no grid, no bars - the smallest measured region on p24 "
             "(0.025 of the page).")
    excluded(24, 2, "in-body-diagram",
             "The second half of the same displayed argument, wrapped across a page turn: the "
             "constraint bracket b_i <= b_j / e_i != e_j / delta w_i < 0 < delta w_j with the "
             "worked value delta w_j = 29.1552 under it. Vector math with a watermark across it, "
             "0.009 of the page; the table it feeds is recorded separately on the same page.")

    rules = [
        "Not one exhibit in this paper carries a number. The caption lines that exist print as "
        "bare 'Figure' or 'Figure.' with no digit, and every other exhibit is introduced by prose "
        "alone ('the following table shows the results', 'the figure above'), so all 39 counted "
        "rows record numbering `none` and every mention block stays empty [caption.numbering].",
        "Nine of the seventeen printed tables have no caption at all - the nomenclature grids, "
        "the correlation table, the province rankings and the watershed grid are announced by a "
        "heading and a sentence - so those records quote nothing and say so in their notes "
        "[caption.verbatim].",
        "Five figure rows are grids the paper prints as figures: the alpha colour scale on p22 "
        "and the five beta blocks on p33 are labelled 'Figure' and 'Figure.' and are read as "
        "tables inside the figure block, `table-as-figure`, not as plots [geometry.family].",
        "Three tables are drawn as full cell grids - the two terminology glossaries and the "
        "neural-network matrix, each with a vertical rule after the symbol column or between "
        "every column - while every other table in the paper prints horizontal rules only or, in "
        "one case, no rules at all [table.rule_style].",
        "Two measured regions are display equations, not exhibits: the objective function and its "
        "constraint set on p24 are the smallest regions on their page (0.025 and 0.009 of the "
        "page area) and are excluded rather than recorded [place.area_frac].",
        "Two figure regions hold several charts of one family rather than a mixture: four "
        "single-line panels on p11 and three dual-axis panels on p12, so each keeps `line` with a "
        "panel count instead of taking `composite-panel` [geometry.panel_count].",
        "Three figure rows are scatter plots of the same annual series with fitted curves drawn "
        "over the markers: the markers are the observations and the curves are the fit, so the "
        "family follows the markers on all three of the p8 charts [geometry.data_labels].",
        "Four figure rows are maps - the nine watersheds and three terraces on p20, the alpha "
        "choropleth on p22 and the six-route transfer map on p25 - of which only the two on p22 "
        "and p25 carry any printed numbers, and none carries a scale value or a colour key of its "
        "own [geometry.printed_numbers].",
        "Tables split across a page break keep `continued` and say in their note where the header "
        "prints, because `header_rows` cannot fall below one in this scheme; the province ranking "
        "on p18-p19 and the province numbering on p22-p23 both run that way [table.header_rows].",
        "The paper numbers its headings (2, 3.3.1, 4.2.3, 6.2.5, 7.4.2), so `section_path` quotes "
        "the printed heading and `section_numbered` is true throughout - including the notation "
        "list, whose heading is simply '2 Nomenclatures' [place.section_numbered].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2013\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "B-21185-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Forty-one measured regions over 26 pages, all accounted: 22 figure rows, 17 printed "
            "tables and 2 exclusions (the two display equations on p24). This paper numbers "
            "nothing - no 'Figure 1', no 'Table 1' - so every exhibit carries numbering `none`, "
            "nine tables carry no caption at all, and the only captions that print at all are the "
            "five 'Figure'/Figure.' lines on p17, p20, p22, p25 and p33, the last repeated over "
            "the five beta blocks. Two tables (the province ranking p18-p19 and the province "
            "numbering p22-p23) run across a page break and record `continued`. No exhibit is "
            "cited by number anywhere in the prose, so every mention block is empty. One declared "
            "gap: p36 prints two 4x4 AHP judgment matrices (ratios such as 1, 5/6, 5/6, 5/3 and "
            "1, 6/7, 6/4, 6/9) as 108 vector paths, and `fig_extract` returns no measured region "
            "on that page at all, so the matrices are recorded as a gap rather than given an "
            "invented bbox."
        ),
    }
    out = PROXY / "pb48-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
