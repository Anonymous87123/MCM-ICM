"""Hand pass for P-B-2014-28414-5bd5b982 (a 2014 B paper that ranks college coaches
with AHP, fuzzy synthetic evaluation and an aggregation model, then extends the model
to football and ice hockey, sweeps each parameter in turn and finally ranks the US
presidents), 33 PDF pages.

Fifty-six measured regions over twenty-three pages, all accounted for: twenty-two
tables, ten figure rows, twenty-four refusals.

    page    region   what it is
    4       r1       unnumbered Symbol/Definition grid, evaluation norms
    4       r2       unnumbered Symbol/Definition grid, analytic hierarchy process
    4       r3       unnumbered Symbol/Definition grid, fuzzy synthetic evaluation -
                     FIRST fragment, continues at the top of page 5
    5       r2       unnumbered Symbol/Definition grid, aggregation model
    8       r1       Figure 3.1 first level evaluation norms (pentagon)
    8       r2       Figure 3.2 second level evaluation norms (five boxes)
    9       r1       Table 3.1 candidate coaches data, 15 columns
    9       r2       Table 3.2 Larry Brown season by season
    10      r1       Table 4.1 three-hierarchy structure
    12      r1       Table 4.2 top ten under AHP
    15      r1       Table 4.3 results for FSE
    16      r1       Table 5.1 results for evaluation
    17      r1       Table 5.2 ranking comparison - FIRST fragment, caption on p18
    18      r2       Table 6.1 women's basketball ranking
    18      r3       Table 6.2 Yahoo ranking - FIRST fragment, caption on p19
    19      r2       Table 6.3 time weights
    20      r1       Table 6.4 AHP with/without time weight - FIRST fragment
    21      r2       Table 6.5 FSE with/without time weight
    22      r1       Table 6.6 AM with/without time weight
    22      r2       Figure 6.1 Bob Knight's evaluation by year
    23      r1       Table 6.7 metrics for football - FIRST fragment
    25      r1       Figure 6.2 the four-step flow chart
    25      r3       Table 6.8 football and hockey top five
    26      r1       Table 7.1 membership functions
    26      r2       Figure 7.1 weight of each factor by k
    27      r1       Figure 7.2 sensitivity to k
    27      r2       Figure 7.3 sensitivity to the win/lose weight
    28      r1       Figure 7.4 sensitivity to the AHP weight, rankings
    28      r2       Figure 7.5 sensitivity to the AHP weight, hit score
    29      r1       Figure 7.6 five-aspect president norm (radar)
    29      r2       Table 7.2 presidents - FIRST fragment, caption on p30
    30      r2       captionless photo block, ranks 1-5 across three sports -
                     the nine portrait rasters on p30-p31 are its fragments

Usage: python -I tools/_dist_paper60.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2014-28414-5bd5b982"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]
        KIND[(_pg["page"], _i)] = _r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

for _key, _bbox in REG.items():
    _ctx = CTXREG.get(_key)
    if _ctx is None or max(abs(a - b) for a, b in zip(_ctx["bbox"], _bbox)) > 0.5:
        raise SystemExit(f"region numbering disagrees with the context dump at {_key}")

SYMBOLS = "2.1 Symbols and Definitions"
NORMS = "3.1 Specify evaluation norms"
COLLECT = "3.2 Collect data"
AHP = "4.1 Model I: Analytic Hierarchy Process (AHP)"
HIERARCHY = "4.1.1 The three-hierarchy structure"
AHP_RESULTS = "4.1.3 Results & analysis"
FSE = "4.2 Model II: Fuzzy Synthetic Evaluation (FSE)"
FSE_RESULTS = "4.2.4 Results & analysis"
INDIVIDUAL = "5.1 Evaluation of individual model"
COMBINED = "5.3 Results & analysis"
GENDER = "6.1 Genders do not matter"
TIMEFACTOR = "6.2 Time factor does make a difference"
WHYTIME = "6.2.1 Why time factor matters?"
HOWTIME = "6.2.2 How time factor matters?"
OTHERSPORTS = "6.3 Model also works in other sports"
SENSITIVITY71 = "7.1 Sensitivity Analysis on FSE"
MEMBERSHIP = "7.1.1 Vary Membership function"
CALCRULE = "7.1.2 Vary calculation rule"
AGGWEIGHT = "7.2 Sensitivity Analysis on Aggregation weight"
PRESIDENT = "7.3 Exploration: Evaluating Best President"
NONTECHNICAL = "IX. Non-technical Explanation"

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def place(page: int, reg: int, path: list[str], kind: str, numbered: bool = True) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(path),
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": c["region"],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def none_mention() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          trail: str = "", read: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": lead, "trail_sentence": trail,
            "lead_pattern": "direct", "read_sentences": read, "gap_sentences": None}


def caption(verbatim: str, numbering: str, position: str) -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": 1 if verbatim else 0,
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap: str, numbering: str, mention: dict,
           path: list[str], kind: str, *, panels: int = 1, layout: str = "1",
           legend: str = "none", ticks: bool = True, labels: bool = False,
           source: str = "text-layer", cap_page: int | None = None,
           position: str = "below", numbered: bool = True, note: str = "",
           other_note: str = "") -> None:
    word = q(cap, cap_page or page) if cap else ""
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "other_note": other_note,
        "panel_count": panels,
        "caption_verbatim": word,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, path, kind, numbered),
        "mention": mention,
        "caption": caption(word, numbering, position),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": ticks,
            "data_labels": labels,
        },
    })


def table(page: int, reg: int, rows: int, cols: int, cap: str, numbering: str,
          mention: dict, path: list[str], kind: str, *, header_rows: int = 1,
          rules: str = "boxed", zebra: bool = False, merged: bool = False,
          num: int = 0, txt: int = 0, width: str = "full",
          note_sentence: str = "", note: str = "", source: str = "text-layer",
          cap_page: int | None = None, position: str = "below",
          numbered: bool = True) -> None:
    word = q(cap, cap_page or page) if cap else ""
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": word,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, path, kind, numbered),
        "mention": mention,
        "caption": caption(word, numbering, position),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": rules,
            "zebra": zebra,
            "merged_cells": merged,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": False,
            "numeric_cols": num,
            "text_cols": txt,
            "width": width,
            "orientation": "portrait",
            "continued": False,
            "note_sentence": note_sentence,
        },
    })


def exclude(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "region": reg, "bbox": REG[(page, reg)],
                     "reason": reason, "note": note})


def build() -> str:
    # ---- 2.1 the four unnumbered notation grids ------------------------------
    table(4, 1, 8, 2, "", "none", none_mention(), [SYMBOLS], "symbols",
          txt=2, zebra=True, position="above", source="none",
          note="unnumbered: the first of four Symbol/Definition grids, introduced by the "
               "bullet 'Symbols for evaluation norms:' that prints directly above its top "
               "rule. Header row Symbol | Definition, then seven rows for a_i, b_i, R, O, "
               "the playoff class counts, the award weights and the contribution points; "
               "the symbol cells are set in the paper's bold math font and several "
               "definitions wrap to two lines inside one row")
    table(4, 2, 9, 2, "", "none", none_mention(), [SYMBOLS], "symbols",
          txt=2, zebra=True, position="above", source="none",
          note="unnumbered: the grid under 'Symbols for Analytic Hierarchy Process:', same "
               "Symbol | Definition header and the same boxed frame as every other grid; "
               "eight rows (the judging matrix, its greatest eigenvalue, CI, CR, RI, the two "
               "weight vectors and the model-I grade). Like its siblings it prints no "
               "number, so the row exists only because the frame does")
    table(4, 3, 8, 2, "", "none", none_mention(), [SYMBOLS], "symbols",
          txt=2, zebra=True, position="above", source="none",
          note="unnumbered: 'Symbols for Fuzzy Synthetic Evaluation:' grid, and THE FIRST "
               "FRAGMENT ONLY - the header and two rows at the foot of page 4, with the "
               "remaining five rows at the top of page 5, no repeated header and no "
               "continued marker. Eight rows over two pages")
    table(5, 2, 4, 2, "", "none", none_mention(), [SYMBOLS], "symbols",
          txt=2, zebra=True, position="above", source="none",
          note="unnumbered: 'Symbols for Aggregation Model:' grid, header plus three rows "
               "(the average offset distance, the weight for model I, the aggregation "
               "grade). The lead-in bullet sits above the region and the 2.2 General "
               "Assumptions heading follows immediately below it, so this is the last "
               "exhibit of section 2.1")

    # ---- 3.1 / 3.2 the two evaluation-norm diagrams --------------------------
    figure(8, 1, "flowchart-or-schematic", "Figure 3.1 First level evaluation norms",
           "Figure N", none_mention(), [NORMS], "evaluation", ticks=False,
           note="one filled pentagon with its five vertices labelled (historical record, "
                "gold content, playoff performance, honours, contribution) and the word "
                "Grade at the centre - a schematic, exported as a bitmap, with no axes, no "
                "legend and no numbers. The pointing sentence is numberless: 'A figure is "
                "prepared to conclude the evaluation norms above. (See figure)'")
    figure(8, 2, "flowchart-or-schematic", "Figure 3.2 Second level evaluation norms",
           "Figure N", none_mention(), [NORMS], "evaluation", ticks=False,
           note="five rounded-rectangle boxes in a row, one per norm, each holding its "
                "second-level criteria as text; the boxes are NOT joined by any connector, "
                "so this is a labelled diagram rather than a flow chart. Bitmap, no "
                "numbers, no legend; shares the numberless '(See figure)' pointer with "
                "Figure 3.1")

    # ---- 3.2 the two data grids ---------------------------------------------
    table(9, 1, 6, 15,
          "Table 3.1 the relevant data of the “best college coaches” candidates",
          "Table N", none_mention(), [COLLECT], "other", num=14, txt=1,
          note="15 columns (Name, from, to, year, win, lose, SRS, SOS, FR, SR, SS, EE, FF, "
               "RU, CH) and only SIX printed rows: a header, four coaches (Boeheim, "
               "Calhoun, Brown, Krzyzewski) and a row that holds nothing but an ellipsis. "
               "The prose promises 'statistics of 10 coaches as an example' and the grid "
               "prints four, then refuses to pretend the rest are there. The seven "
               "two-letter abbreviations are expanded by a sentence printed above the "
               "header, not by a table note. NEVER CITED BY NUMBER")
    table(9, 2, 10, 9,
          "Table 3.2 the college basketball coaching record about each season of Larry Brown",
          "Table N", none_mention(), [COLLECT], "other", num=6, txt=3,
          note="a header and nine seasons of one coach: Season, win, lose, SRS, SOS, AP "
               "Pre, AP High, AP Final, Result. The seasons jump from 1987-88 to 2012-13 "
               "with no omission marker and no gap row, so eight seasons are simply absent; "
               "the two modern rows print an em dash in the three AP columns and one row "
               "leaves the AP-Final cell blank where its neighbours print the dash. NEVER "
               "CITED BY NUMBER")

    # ---- 4 the two models ---------------------------------------------------
    table(10, 1, 15, 3, "Table 4.1 the three hierarchy structure of our model",
          "Table N", none_mention(), [AHP, HIERARCHY], "model", txt=3, merged=True,
          note="the paper's only true cell merges: Goal 'The influence of coach' spans all "
               "fourteen body rows, and Criteria hold 2, 2, 3, 2 and 5 alternatives under "
               "the five norms. Bold black header on white, no shading, full box. The "
               "playoff row prints a lone ellipsis between First Round and Champion, which "
               "is the paper admitting it left classes out. NEVER CITED BY NUMBER")
    table(12, 1, 6, 6, "Table 4.2 the top ten college basketball coaches’ rankings",
          "Table N", none_mention(), [AHP, AHP_RESULTS], "result", num=2, txt=4,
          note="TWO HALVES IN ONE FRAME: the header Rank | Name | Grade(Y1) is printed "
               "twice, once per half, with a vertical divider down the middle, so six "
               "printed columns carry ten ranks in five body rows. Header cell shaded "
               "grey, body unshaded. NEVER CITED BY NUMBER")
    table(15, 1, 13, 7, "Table 4.3 the results for FSE", "Table N", none_mention(),
          [FSE, FSE_RESULTS], "result", num=6, txt=1, rules="booktabs", zebra=True,
          note="NO COLUMN VERTICALS: an outer box and a rule under the header and between "
               "row pairs, nothing else, which is booktabs and the one grid in the paper "
               "that departs from the full-frame house style. The header mislabels BOTH the "
               "fourth and the fifth aspect column 'X3'. The last two rows are the keyless "
               "entropy vector g_j and weight vector w_j - printed as rows inside the grid "
               "with no stub label. Banding runs in two-row pairs. NEVER CITED BY NUMBER")

    # ---- 5 the two models combined ------------------------------------------
    table(16, 1, 7, 3, "Table 5.1 the results for evaluation", "Table N",
          none_mention(), [INDIVIDUAL], "evaluation", num=2, txt=1,
          note="six results (D_alpha, D_beta, D, g_alpha, g_beta, g) against AHP and FSE "
               "under a BLANK stub-column header cell; the four metric stubs print in the "
               "bold math font and the two grades keep four and two decimals respectively. "
               "Introduced by the prose line 'Here are our results:'. NEVER CITED BY NUMBER")
    table(17, 1, 13, 4, "Table 5.2 the ranking comparison among the models", "Table N",
          none_mention(), [COMBINED], "result", num=1, txt=3, zebra=True, cap_page=18,
          note="THE FIRST FRAGMENT: header AHP | FSE | AM and ten rank rows at the foot of "
               "page 17, then the two hit-score rows at the top of page 18 and the caption "
               "BELOW them, so the caption belongs to the tail of the grid while the header "
               "belongs to its head. Thirteen rows over four columns. NEVER CITED BY NUMBER")

    # ---- 6.1 gender ---------------------------------------------------------
    table(18, 2, 6, 6, "Table 6.1 the ranking for coaches of women’s basketball",
          "Table N", none_mention(), [GENDER], "result", num=4, txt=2,
          note="two halves again - Rank | Name | Grade printed twice - ten women coaches in "
               "five body rows; the name and grade cells are split across two text lines "
               "each inside one row, which is why the layer reads 'Pat Summitt / 1 0.8532'. "
               "Introduced by 'Coaches' ranking with the Aggregation Model:'. NEVER CITED "
               "BY NUMBER")
    table(18, 3, 6, 4, "Table 6.2 the ranking from Yahoo", "Table N",
          none_mention(), [GENDER], "result", num=2, txt=2, cap_page=19,
          note="THE FIRST FRAGMENT: header and two rows at the foot of page 18, three more "
               "at the top of page 19 with no repeated header, caption below the tail. Rank "
               "and name only - no grade column, unlike Table 6.1 - so the two rankings are "
               "not the same shape. NEVER CITED BY NUMBER")

    # ---- 6.2 time weight ----------------------------------------------------
    table(19, 2, 7, 3, "Table 6.3 the time weights for each time period", "Table N",
          none_mention(), [TIMEFACTOR, WHYTIME], "other", num=1, txt=2,
          note="six historical periods against their turning points and the weight w_i. The "
               "turning-point cell wraps to three lines in two of the six rows - one cell, "
               "not a merge - and those two rows alone are shaded, with no legend. The "
               "weight column header prints as a symbol, not a word. The citing sentence is "
               "numberless: 'The following table shows the critical years in the NCAA "
               "history'. NEVER CITED BY NUMBER")
    table(20, 1, 13, 4,
          "Table 6.4 what is different in AHP introducing time weight?", "Table N",
          none_mention(), [TIMEFACTOR, HOWTIME], "test", num=2, txt=2, zebra=True,
          cap_page=21,
          note="THE FIRST FRAGMENT: header, seven ranks at the foot of page 20, three more "
               "ranks and the two hit-score rows at the top of page 21, caption below. Four "
               "printed columns (name, grade, name, grade) carrying the same ranking with and "
               "without the time weight; names whose rank moved are set in BOLD - the "
               "highlight is weight, not shading, while the row fills alternate 238/255. "
               "NEVER CITED BY NUMBER")
    table(21, 2, 13, 4,
          "Table 6.5 what is different in FSE introducing time weight?", "Table N",
          none_mention(), [TIMEFACTOR, HOWTIME], "test", num=2, txt=2, zebra=True,
          note="the FSE twin of Table 6.4 and the only grid of the three that fits on one "
               "page: header, ten ranks and two hit-score rows. Same bold-not-shaded "
               "convention for moved names, same 238/255 banding, same dark header row. "
               "NEVER CITED BY NUMBER")
    table(22, 1, 13, 4,
          "Table 6.6 what is different in AM introducing time weight?", "Table N",
          none_mention(), [TIMEFACTOR, HOWTIME], "test", num=2, txt=2, zebra=True,
          note="the aggregation-model twin; ten ranks plus two hit-score rows on one page. "
               "The right half prints Tom Izzo and Phog Allen entering the top ten, so the "
               "two halves are not a permutation of the same ten names. NEVER CITED BY "
               "NUMBER")
    figure(22, 2, "line", "Figure 6.1 every year’s evaluation of Bob Knight", "Figure N",
           none_mention(), [TIMEFACTOR, HOWTIME], "test", legend="inside",
           note="a flat 2-D Excel line chart in a bitmap: two series, the red solid-circle "
                "line labelled 'with temporal weighting factor' and the blue dash-dot star "
                "line 'without', legend INSIDE the plot at the upper right, both axis "
                "titles, numeric ticks on both axes, no data labels, and an in-art title "
                "'Analysis for Bob Knight's career' that the printed caption does not "
                "repeat. Pointed at with 'the following figure shows how evaluation grade "
                "changes in the two different situations'. NEVER CITED BY NUMBER")

    # ---- 6.3 the model on other sports --------------------------------------
    table(23, 1, 18, 3, "Table 6.7 the metrics for college football", "Table N",
          none_mention(), [OTHERSPORTS], "model", header_rows=2, txt=3, merged=True,
          width="half", cap_page=24,
          note="THE FIRST FRAGMENT: two header rows ('5-aspect norms' plus the two sport "
               "columns) and four metric rows at the foot of page 23, the remaining twelve "
               "metric rows at the top of page 24, caption below. Three columns, and the "
               "aspect stub is VERTICALLY MERGED over its metric rows, which is why "
               "'Playoff Performance' splits into two printed lines and why one football "
               "cell is merged over two rows. NEVER CITED BY NUMBER")
    figure(25, 1, "flowchart-or-schematic", "Figure 6.2 the flow chart of the four steps",
           "Figure N", none_mention(), [OTHERSPORTS], "model", ticks=False,
           note="a vector SmartArt stack: rounded rectangles and block arrows descending the "
                "page from an oval 'Start' to 'Solve the model'. Four of the five labels are "
                "text-layer strings inside the region; the fifth, 'Solve the model', is a "
                "separate small raster nested in the last box and is refused as a fragment "
                "(p25 r2). Caption below. Pointed at with 'The following figure shows the "
                "steps of applying the model into all possible sports'")
    table(25, 3, 6, 4, "Table 6.8 the rankings for football & hockey", "Table N",
          none_mention(), [OTHERSPORTS], "result", num=2, txt=2,
          note="two sports side by side, name and grade each, five rows per sport under one "
               "header; the body carries a UNIFORM grey fill rather than alternating bands, "
               "so it is shading without a key and not zebra. Never cited by number")

    # ---- 7.1.1 membership functions -----------------------------------------
    table(26, 1, 4, 2, "Table 7.1 membership functions", "Table N", none_mention(),
          [SENSITIVITY71, MEMBERSHIP], "model", num=1, txt=1, source="typed-from-crop",
          note="three membership functions in a Type | Membership function frame, every "
               "formula printed in full - row 3's exponent is NOT clipped, its baseline sits "
               "just inside the bottom rule. The caption cannot be quoted from the layer: "
               "the page prints it on the same line as the tail of formula 3, so the layer "
               "interleaves the two ('Table 7.1mu_i m...embership functions') and this "
               "verbatim is the reading of the crop. NEVER CITED BY NUMBER")
    figure(26, 2, "bar", "Figure 7.1 the weight of each factor for each aspect",
           "Figure N",
           cited(26, 26, ["Figure 7.1"], 1,
                 "changes of weight distribution can be seen clearly in Figure 7.1"),
           [SENSITIVITY71, MEMBERSHIP], "sensitivity", legend="inside",
           note="a grouped column chart: four series (the four aspects) over five x "
                "categories X1-X5, legend INSIDE at the top right, y ticks 0 to 0.35, x "
                "axis titled 'evaluation factors' although the caption says 'the weight of "
                "each factor for each aspect', no in-art title and no data labels. THE "
                "PAPER'S ONLY BY-NUMBER CITATION: 'Weight distribution is sensitive to the "
                "value of k and changes of weight distribution can be seen clearly in Figure "
                "7.1', one sentence, on the same page as the art")

    # ---- 7.1.2 / 7.2 the two remaining sweeps -------------------------------
    figure(27, 1, "line", "Figure 7.2 sensitivity analysis on k for FSE", "Figure N",
           none_mention(), [SENSITIVITY71, MEMBERSHIP], "sensitivity", legend="inside",
           note="three line series, one per membership function, against k; legend inside "
                "at the top right, numeric ticks on both axes, no data labels, in-art title "
                "'Sensitivity Analysis to the value of k'. The caption is a bare number and "
                "title with no sentence")
    figure(27, 2, "line", "Figure 7.3 sensitivity analysis to the weight of win and lose",
           "Figure N", none_mention(), [SENSITIVITY71, CALCRULE], "sensitivity",
           note="a single-series line with NO legend and no legend room: the parameter in "
                "play is disclosed by a green callout reading 'the chosen point' with an "
                "arrow onto the curve at k = 2, which is the only annotation in the paper's "
                "charts. In-art title 'Sensitivity Analysis of Hit score to the weight of "
                "win and lose'. NEVER CITED BY NUMBER")
    figure(28, 1, "line", "Figure 7.4 && 7.5", "Figure N", none_mention(),
           [AGGWEIGHT], "sensitivity", legend="outside-right",
           note="SIX line series in one panel, one per coach, with the legend placed OUTSIDE "
                "the plot area at the right in its own framed panel - the only such legend "
                "in the paper - and a categorical y axis of ranks 1-7 instead of a continuous "
                "score axis. In-art title 'Sensitivity Analysis to the weight of AHP model'. "
                "Shares its caption line with Figure 7.5")
    figure(28, 2, "line", "Figure 7.4 && 7.5", "Figure N", none_mention(),
           [AGGWEIGHT], "sensitivity",
           note="the hit-score companion to Figure 7.4: single series, no legend, in-art "
                "title 'Sensitivity Analysis of hit score to the weight of AHP Model'. TWO "
                "FIGURES, ONE CAPTION LINE: the page prints 'Figure 7.4 && 7.5' once, below "
                "both charts, so that string is the verbatim caption of each of the two rows "
                "and neither has a unique caption of its own. NEVER CITED BY NUMBER")

    # ---- 7.3 the presidents -------------------------------------------------
    figure(29, 1, "other", "Figure 7.6 5-aspect norm of president of USA", "Figure N",
           none_mention(), [PRESIDENT], "other", ticks=False,
           other_note="radar/spider plot: the family vocabulary has no radar member",
           note="A RADAR PLOT - a five-spoke spider pentagon with the spoke labels around "
                "the rim and 'Grade' at the centre, no rings labelled, no ticks, no legend "
                "and no in-art title. The family vocabulary has no radar/spider member, so "
                "this is recorded as other rather than forced into every-radar-is-a-line or "
                "surface-or-3D. It is the only exhibit of its kind in the paper")
    table(29, 2, 6, 4, "Table 7.2 the ranking of presidents of the United States",
          "Table N", none_mention(), [PRESIDENT], "result", num=2, txt=2, width="half",
          cap_page=30,
          note="THE FIRST FRAGMENT: header and two ranks at the foot of page 29, the other "
               "eight ranks over the top of page 30 with no repeated header, caption below "
               "the tail. Rank | Name printed twice, so four columns carry ten presidents. "
               "Introduced by 'The ranking of presidents of the United States is shown in "
               "following table.' NEVER CITED BY NUMBER")

    # ---- IX the captionless photo block -------------------------------------
    table(30, 2, 6, 4, "", "none", none_mention(), [NONTECHNICAL], "other", num=1, txt=3,
          rules="no-rules", zebra=True, position="above", source="none",
          note="AN EXHIBIT WITH NO NUMBER AND NO CAPTION: header 'Rank | college basketball "
               "| college football | college hockey' and five ranks, but the header row "
               "prints just ABOVE the measured region and only its first rank falls inside "
               "it. Rules are hairlines plus banded grey rank rows, no verticals. Each of "
               "the fifteen coach portraits is a separate raster region (three per sport "
               "per rank), so the block is counted once here and those portraits are refused "
               "as fragments of it, and the three grey row bands that follow on page 31 are "
               "refused as continuations")

    # ---- the refused regions -------------------------------------------------
    exclude(5, 1, "split-across-pages",
            "the tail of the Fuzzy Synthetic Evaluation notation grid, five more rows at "
            "the top of page 5 with no repeated header; the header and first two rows are "
            "at the foot of page 4")
    exclude(18, 1, "split-across-pages",
            "the two hit-score rows of Table 5.2 ('Top5 Hit score', 'Top10 Hit score') in a "
            "thin headerless strip at the top of page 18; the header and all ten ranks are "
            "at the foot of page 17 and the caption prints below this strip")
    exclude(19, 1, "split-across-pages",
            "ranks 3-10 of Table 6.2, headerless, at the top of page 19, closing with the "
            "caption 'Table 6.2 the ranking from Yahoo'; the header and ranks 1-2 are at the "
            "foot of page 18")
    exclude(21, 1, "split-across-pages",
            "ranks 8-10 and the two hit-score rows of Table 6.4, headerless, at the top of "
            "page 21 under the caption line printed for them; the header and ranks 1-7 are "
            "at the foot of page 20")
    exclude(24, 1, "split-across-pages",
            "the twelve remaining metric rows of Table 6.7 at the top of page 24, headerless "
            "and with their merged aspect stubs reprinted, closing with the caption; the two "
            "header rows and the first four metrics are at the foot of page 23")
    exclude(30, 1, "split-across-pages",
            "ranks 3-10 of Table 7.2 at the top of page 30, headerless, closing with the "
            "caption 'Table 7.2 the ranking of presidents of the United States'; the header "
            "and ranks 1-2 are at the foot of page 29")
    exclude(25, 2, "fragment-of-other",
            "a small raster nested inside Figure 6.2's last rounded rectangle - the words "
            "'Solve the model' exported as a bitmap while the other four labels stayed in "
            "the text layer; one label of the diagram, not a second exhibit")
    exclude(30, 3, "fragment-of-other",
            "the left portrait of rank 1, John Wooden, in the captionless three-sport photo "
            "block; every portrait in the block is its own raster region and the block is "
            "counted once at p30 r2")
    exclude(30, 4, "fragment-of-other",
            "the centre portrait of rank 1, Bear Bryant; same captionless block")
    exclude(30, 5, "fragment-of-other",
            "the right portrait of rank 1, Bob Johnson; same captionless block")
    exclude(31, 1, "fragment-of-other",
            "the basketball portrait of rank 2, Mike Krzyzewski; the rank rows below the "
            "first continue the same three-sport block")
    exclude(31, 2, "fragment-of-other",
            "the football portrait of rank 2, Knute Rockne; same block")
    exclude(31, 3, "fragment-of-other",
            "the hockey portrait of rank 2, Red Berenson; same block")
    exclude(31, 4, "split-across-pages",
            "the grey rank band of rank 3 on page 31 - the row's rank cell, shading and "
            "rules, with its three portraits as separate raster regions below it; the table "
            "itself is counted once at p30 r2")
    exclude(31, 5, "fragment-of-other",
            "the hockey portrait of rank 3, Jack Parker; same block")
    exclude(31, 6, "fragment-of-other",
            "the basketball portrait of rank 3, Adolph Rupp; same block")
    exclude(31, 7, "fragment-of-other",
            "the football portrait of rank 3, Tom Osborne; same block")
    exclude(31, 8, "fragment-of-other",
            "the basketball portrait of rank 4, Dean Smith; same block")
    exclude(31, 9, "fragment-of-other",
            "the football portrait of rank 4, Joe Paterno; same block")
    exclude(31, 10, "fragment-of-other",
            "the hockey portrait of rank 4, Jerry York; same block")
    exclude(31, 11, "split-across-pages",
            "the grey rank band of rank 5 on page 31, with its three portraits as separate "
            "raster regions below it; same captionless block as p30 r2")
    exclude(31, 12, "fragment-of-other",
            "the hockey portrait of rank 5, Ron Mason; same block")
    exclude(31, 13, "fragment-of-other",
            "the basketball portrait of rank 5, Bob Knight; same block")
    exclude(31, 14, "fragment-of-other",
            "the football portrait of rank 5, Bobby Bowden; last region of the block")

    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": ITEMS,
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": [
            "Every caption in this paper prints BELOW its exhibit, without exception - the "
            "twenty-two numbered grids, the six charts, the three diagrams and the two "
            "symbolic norm drawings all put the number under the object, which is the exact "
            "opposite of the lane's other 2014 paper [caption.position]",
            "Five of the numbered grids have their caption on a different page from the "
            "fragment that carries their header - Table 5.2, 6.2, 6.4, 6.7 and 7.2 all break "
            "between the last data row and the caption - so the row is the TOPMOST fragment "
            "(the one holding the header) and the caption is quoted from the page that "
            "prints it [caption.position]",
            "The four unnumbered notation grids carry no number and no caption of any kind; "
            "each is introduced by a bold bullet ('Symbols for AHP:', etc.) printed above "
            "its top rule, and one of the four is itself split across pages 4 and 5 "
            "[caption.numbering]",
            "The house style is a full frame - outer box, a rule between every row and a "
            "vertical between every column - and exactly three grids depart from it: Table "
            "4.3 and Table 6.1 and Table 6.2 print horizontals only, with no column "
            "verticals at all [table.rule_style]",
            "Two grids are two tables printed inside one frame: Table 4.2 and Table 6.1 "
            "repeat their header and drop a vertical divider down the middle, so six printed "
            "columns carry ten ranks in five body rows [table.merged_cells]",
            "Only Table 4.1 and Table 6.7 merge cells, and both merge vertically: Table "
            "4.1's Goal cell spans all fourteen body rows and Table 6.7's aspect stubs span "
            "their metric rows. A wrapped header or a two-line turning-point cell is one "
            "cell, not a merge, and neither is counted [table.merged_cells]",
            "Shading is used three different ways and only two are zebra: the comparison "
            "grids 6.4-6.6 band alternate rows 238/255 while marking movers in BOLD rather "
            "than with fill, Table 4.3 bands in two-row pairs, Tables 6.3 and 6.8 shade a "
            "fixed set of rows with no key at all, and Tables 3.1/3.2/4.1/4.2/5.2/6.7/7.2 "
            "shade only their header [table.zebra]",
            "The paper points at most of its exhibits without a number - 'the following "
            "table shows', 'shown in following table', 'Here are our results:', 'The "
            "following figure shows', '(See figure)' - so twenty-five of the twenty-six "
            "numbered exhibits have mention count zero and only Figure 7.1 is cited by "
            "number, once, on its own page [mention.count]",
            "The charts are all Excel or PowerPoint exports flattened into bitmaps, and they "
            "carry no data labels anywhere: the reader gets ticks and a legend and must read "
            "values off the mark. Two of them have no legend at all and identify their "
            "parameter through an in-art title or a callout [geometry.data_labels]",
            "The six charts print an in-art title that is a SECOND title, different from the "
            "caption, and in Figure 7.1 the two disagree about what the x axis is ('evaluation "
            "factors' vs 'the weight of each factor for each aspect') [geometry.family]",
            "Two exhibits have no number and no caption: the four notation grids, and the "
            "three-sport photo block that closes section IX. The block prints five ranks of "
            "coach portraits with a header row above the measured region and no title under "
            "it at all [caption.verbatim]",
            "The photo block is the only exhibit in the paper built out of rasters rather "
            "than one picture: fifteen separate portrait images, three per sport per rank, "
            "each its own measured region. The block is counted once and the fifteen are "
            "refused as fragments [geometry.panel_count]",
            "Nothing in the paper is landscape, nothing is three-dimensional, nothing has a "
            "colour bar, and no chart shares an axis with another [table.orientation]",
        ],
        "note": (
            "Family tally: table-grid 22, line 6, flowchart-or-schematic 3, bar 1, other 1. "
            "Coverage: 22 table rows + 10 figure rows + 24 refusals = 56 measured regions "
            "over 23 of the 33 pages. Declared rather than repaired: Figure 7.6 is a radar "
            "pentagon and the family vocabulary has no radar member, so it is filed as other "
            "instead of being forced into line or surface-or-3D; Table 7.1's caption is the "
            "one caption the text layer cannot be quoted from, because the page prints it on "
            "the same line as the tail of formula 3, so that verbatim is typed from the crop "
            "and marked typed-from-crop; Table 3.1 prints only four of the ten coaches its "
            "own prose promises, with an ellipsis row standing where the other six would be, "
            "and the row count records what the page prints. The three-sport photo block "
            "prints its header row just above the measured region, so the region holds the "
            "header of nothing and the first rank row only. Seven of the twenty-two tables "
            "are split across a page break and five of those keep their caption on the far "
            "side."
        ),
    }
    out = PROXY / "pc60-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    sys.exit(main())
