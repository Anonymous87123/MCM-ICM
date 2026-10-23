"""Hand pass for P-B-2014-28875-728f6f07 (a 2014 B paper that ranks college coaches with
an analytic hierarchy process and fuzzy comprehensive evaluation, then splits the metrics
into two levels, extends the model to football, baseball and women's basketball, plots each
coach's composite score against the time line horizon and finally tests the model four ways
before reprinting the results as a Sports Illustrated article), 35 PDF pages.

Thirty-eight measured regions over twenty-four pages, all accounted for: eleven figure
rows, eighteen tables, nine refusals. Page 12 carries twenty-three vector paths with no
measured region - the six display formulas of the consistency model - so no exhibit is
missing a box.

    page    region   what it is
    2       r1       prose fragment, no exhibit
    7       r1       Table 1 Variables
    8       r1       Figure 1 NCAA Basketball metric tree
    9       r1       Figure 2 NCAA Football metric tree
    9       r2       Figure 3 NCAA baseball metric tree
    10      r1       display-formula fragment, no exhibit
    14      r1       Table 2 the weight for each metrics
    15      r1       Table 3 AHP-FCE top five in NCAA Basketball
    16      r1       Figure 4 Goal > Classification > metric tree
    16      r2       Table 4 the weight of the two level metrics - FIRST fragment, the
                     remaining six rows at the top of page 17
    17      r2       Figure 5 College coaches metrics system
    19      r1       Table 5 the weight of Achievement and Competency
    20      r1       Table 6 IAHP-FCE top five in NCAA Basketball
    21      r1       Table 7 the weight of Experience, Achievement and Competency
    21      r2       Table 8 top five in NCAA Football
    22      r1       Table 9 top five in NCAA Baseball
    23      r1       Table 10 the weight of each woman-coach metric
    24      r1       Table 11 top five woman coaches
    24      r2       prose fragment, no exhibit
    24      r3       Table 12 the best all time college coach
    24      r4       Figure 6 raster photograph of Pat Summitt
    25      r1       Table 13 Dean Smith year by year
    25      r2       Figure 7 line chart, Dean Smith
    26      r1       Figure 8 line chart, Pat Summitt
    27      r1       Figure 9 line chart, Joe Paterno
    27      r2       Figure 10 line chart, Bobby Bowden
    28      r1       prose fragment, no exhibit
    28      r2       Table 14 Basketball Coaches deviation grid
    29      r1       Table 15 Women's basketball coach deviation grid
    29      r2       Table 16 Football coaches deviation grid
    29      r3       Table 17 Baseball coach deviation grid
    29      r4       prose fragment, no exhibit
    30      r1       prose fragment, no exhibit
    30      r2       Figure 11 sensitivity analysis flow chart
    31      r1       Table 18 metrics score sensitivity analysis
    32      r1       prose fragment, no exhibit
    34      r1       reference-list fragment, no exhibit

Every printed number is unique in this paper (Table 1-18, Figure 1-11) but two of them are
misused in the prose: page 16 points at "Figure 1" while describing Figure 4, and Figure 9
is never introduced before it prints, only compared with afterwards. Both are recorded.

Usage: python -I tools/_dist_paper61.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2014-28875-728f6f07"
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

# The heading pass found seven headings, one of them a fragment of a printed numbers list,
# so every label below is the heading as printed on the page, prefixed with 未编号标题 and
# recorded with section_numbered false.
INTRO = "未编号标题 Introduction"
SYMBOLS = "未编号标题 Symbols Definitions"
DEV = "未编号标题 The developing of models"
COLLECT = "未编号标题 Data collection and pretreatment"
CHOOSE = "未编号标题 Choose the metrics for assessment"
TESTMODEL = "未编号标题 Testing the model"
CALCWEIGHT = "未编号标题 Calculate the weight"
IMPROVE = "未编号标题 Improving the model"
METRICSYS = "未编号标题 Determine the metrics system for assessment"
DETWEIGHT = "未编号标题 Determine the weight"
IAHP = "未编号标题 Using the IAHP-FCE model"
BBALL = "未编号标题 Model’s Top 5 coaches in NCAA Basketball"
FBALL = "未编号标题 Model’s Top 5 coaches in NCAA Football"
BASEBALL = "未编号标题 Model’s Top 5 coaches in NCAA Baseball"
CLASSES = "未编号标题 For the Classification---- Achievement and Competency"
GENDER = "未编号标题 Applied the model across both genders"
BEST = "未编号标题 Finding out the Best all time college coach"
TIMELINE = "未编号标题 The difference as the time line horizon"
DIFFGEN = "未编号标题 Different gender of the same sports"
DIFFSPORT = "未编号标题 Different sports of the same gender"
SAMESPORT = "未编号标题 Same sports of the same gender"
MODTEST = "未编号标题 Modeling test"
DEVTEST = "未编号标题 Model and model solution deviation test"
SENS = "未编号标题 Sensitivity analysis of the model parameters[32,33,34]"

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def place(page: int, reg: int, path: list[str], kind: str, numbered: bool = False) -> dict:
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
          trail: str = "", read: int = 1, gap: int | None = None) -> dict:
    """A by-number citation the text layer prints; check_mention re-quotes both sentences."""
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": schema.norm(lead),
            "trail_sentence": schema.norm(trail), "lead_pattern": "direct",
            "read_sentences": read, "gap_sentences": gap}


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
           position: str = "below", note: str = "", other_note: str = "") -> None:
    word = q(cap, cap_page or page) if (cap and source == "text-layer") else schema.norm(cap)
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
        "place": place(page, reg, path, kind),
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
          cap_page: int | None = None, position: str = "above") -> None:
    word = q(cap, cap_page or page) if (cap and source == "text-layer") else schema.norm(cap)
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": word,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, path, kind),
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


def build() -> None:
    # ---- Table 1, the notation grid ----------------------------------------
    table(7, 1, 9, 2, "Table 1 Variables", "Table N",
          cited(7, 7, ["table 1"], 3, "you can look it up in the table 1.",
                "Arrange NCAA Basketball, Football and Baseball are shown as follows table 1, "
                "table2 and table 3."),
          [INTRO, SYMBOLS], "symbols", rules="boxed", txt=2,
          note="a header Variables | Description over eight rows (m, n, w, B, s(i), CIC(n), "
               "minCIC(n), z(j)) in the paper's full-frame style: outer box, a rule under "
               "every row, one vertical between the two columns, no shading. The paragraph "
               "that introduces it is split across the page break, so the pointer sentence "
               "that opens page 7 reads 'a variables or something, you can look it up in "
               "the table 1.'")

    # ---- the five metric trees ----------------------------------------------
    figure(8, 1, "flowchart-or-schematic",
           "Figure 1 The metrics for NCAA Basketball coach.", "Figure N",
           none_mention(), [DEV, CHOOSE], "model", ticks=False, labels=True,
           note="one box reading NCAA Basketball at the top and thirteen connector lines "
                "fanning down to a row of rotated leaf cells (Champ NCAA, WL%, SRS, SOS, "
                "Years, AP High, AP Final, Game, NCAA, AP Pre, Final Fours, CREG, CTRN). "
                "Drawn in Word, no axes, no legend, no numbers. The prose never points at "
                "it by number: the only pointer on the page sends the reader to 'table 1, "
                "table2 and table 3'")
    figure(9, 1, "flowchart-or-schematic",
           "Figure 2 The metrics for NCAA Football coach.", "Figure N",
           none_mention(), [DEV, CHOOSE], "model", ticks=False, labels=True,
           source="typed-from-crop",
           note="same tree as Figure 1 with twelve leaves (Bowls, PCT, SRS, SOS, AP post, "
                "Years, Bowls Game, AP Pre, Overall Game, AP High, Bowls PCT, SRS). Caption "
                "typed from the crop because the text layer prints a stray in-art 'SOS' "
                "token between the bold number and the caption sentence, which is not on "
                "the printed caption line")
    figure(9, 2, "flowchart-or-schematic",
           "Figure 3 The metrics for NCAA Baseball coach.", "Figure N",
           none_mention(), [DEV, CHOOSE], "model", ticks=False, labels=True,
           note="same tree with six leaves (Years, Game, PCT, Win, Lost, Championship) and "
                "a boxed frame rather than the open connectors of Figures 1 and 2; the "
                "text layer reads 'Basebal l' inside the art but the caption line itself "
                "prints Baseball")
    # ---- the two weight and result grids of model I ------------------------
    table(14, 1, 4, 8, "Table 2 The weight for each metrics", "Table N",
          cited(14, 14, ["table 2"], 1,
                "calculate the weight for each metrics shown as table 2."),
          [TESTMODEL, CALCWEIGHT], "model", rules="boxed", num=7, txt=1,
          note="FOUR printed rows in one eight-column frame: a 'Metrics 1..7' label row over "
               "its weight row, then 'Metrics 8..13' over the second weight row, so thirteen "
               "weights sit in two blocks with the label row repeated rather than a header "
               "spanning both. The two label rows carry the only grey fill in the paper's "
               "tables; the body is white. The second block rules a seventh numeric column "
               "and leaves it empty because 13 is one short of two sevens")
    table(15, 1, 6, 3, "Table 3 AHP-FCE model’s top 5 coaches in NCAA Basketball",
          "Table N",
          cited(15, 15, ["table 3"], 1,
                "list AHP-FCE model’s top 5 coaches in NCAA Basketball as table 3."),
          [TESTMODEL, CALCWEIGHT], "result", rules="booktabs", width="half", num=2, txt=1,
          note="NO VERTICALS: one rule above the header, one under it, one under the last "
               "row, and nothing else - the first of seven booktabs grids in a paper whose "
               "other eleven grids are fully boxed. Rank | Coach | Composite score with five "
               "coaches, and the grid is set narrow and centred rather than to the full "
               "measure. The fifth name is truncated to 'Jim Calhou'. This is the model-I "
               "result that the next section spends a page demolishing")

    # ---- the improved model's two-level weight grid -------------------------
    figure(16, 1, "flowchart-or-schematic",
           "Figure 4 A simple metrics system for assessment.", "Figure N",
           cited(16, 16, ["Figure 4", "Figure 1"], 2,
                 "A simple metrics system for assessment is as follow Figure 4.",
                 "As shown in Figure 1, the first level is Classifications", read=2),
           [IMPROVE, METRICSYS], "model", ticks=False, labels=True,
           note="three-level box tree: Goal at the top, Classification 1-3 below it, nine M "
                "boxes below those, and a vertical ellipsis under each classification. The "
                "M row prints the label 'M 5' TWICE where M 4, M 5, M 6 belong, and the "
                "rightmost boxes run past the text measure. The sentence that follows the "
                "figure points at it as 'Figure 1', which is a mis-citation of this tree")
    table(16, 2, 17, 6, "Table 4 The Weight of the two level metrics", "Table N",
          cited(16, 16, ["table4"], 1,
                "and calculate the weight list as follow table4."),
          [IMPROVE, DETWEIGHT], "model", rules="booktabs", merged=True, txt=6,
          note="SIX columns because both halves are merged pairs: the header cells 'The first "
               "level metrics' and 'The second level metrics' each span a code column and a "
               "name column, and every body row carries a level code, its name, its level "
               "weight, then a metric code, its name and its metric weight. A1 and A2 span "
               "their whole block vertically. The grid is split by the page break after "
               "metric x: the six remaining rows (Classification 3 through metric n) print at "
               "the top of page 17 with no repeated header and no continued marker, and are "
               "recorded as a refusal. Seventeen printed rows over two pages")
    figure(17, 2, "flowchart-or-schematic",
           "Figure 5 College coaches metrics system for assessment", "Figure N",
           cited(17, 17, ["figure 5", "Figure 5"], 2,
                 "we constructed the Basketball college coaches metrics system for "
                 "assessment as follow figure 5.",
                 "As shown in Figure 5, we determined Competency, Achievement and "
                 "Experience", read=2),
           [IAHP, BBALL], "model", ticks=False, labels=True,
           note="the two-level system: The Best College Basketball Coach over three group "
                "boxes (Experience, Achievement, Competency) over rotated leaf cells, three "
                "under Experience and six and four under the other two, each group sitting "
                "inside its own bracket frame. The caption prints with no full stop")

    # ---- the five weight grids and the four ranking grids of model II --------
    table(19, 1, 3, 10, "Table 5 The weight of Classification Achievement and Competency.",
          "Table N",
          cited(19, 19, ["Table 5"], 1,
                "The weight of each level is shown as Table 5."),
          [IAHP, CLASSES], "result", header_rows=2, rules="boxed", merged=True,
          num=10,
          note="TWO header rows: a group row over a w4..w13 label row, with 'Achievement' "
               "spanning five columns and 'Competency' spanning five, then a single value row. "
               "The caption names three classifications and the grid prints TWO - the "
               "Experience weights are simply not there. The label row also prints w12 before "
               "w11")
    table(20, 1, 6, 4, "Table 6 Model’s Top 5 coaches in NCAA Basketball", "Table N",
          cited(19, 20, ["Table 6"], 1,
                "Using EXCEL to calculate and obtain the model’s Top 5 coaches as Table 6."),
          [IAHP, BBALL], "result", rules="booktabs", num=2, txt=2,
          note="the same booktabs frame as Table 3 but set to the full measure: Rank | Coach "
               "| Composite score | Years with five coaches and six-decimal scores. Cited on "
               "the page before it prints, so the lead sentence and the grid are separated by "
               "the page break")
    table(21, 1, 3, 10, "Table 7 The weight of Experience, Achievement and Competency.",
          "Table N",
          cited(21, 21, ["table 7"], 1,
                "calculate d the weight list as follow table 7."),
          [IAHP, FBALL], "result", header_rows=2, rules="boxed", merged=True, num=10,
          note="two header rows over a single value row: Experience spans three columns, "
               "Competency three, Achievement four, ten weights in all. Boxed, with a vertical "
               "between every column like Table 5. The pointer sentence carries the paper's "
               "typo 'calculate d the weight list'")
    table(21, 2, 6, 4, "Table 8 Model’s Top 5 coaches in NCAA Football", "Table N",
          cited(21, 21, ["Table 8"], 1,
                "We used EXCEL to calculate and ranking the model’s Top 5 coaches as Table 8."),
          [IAHP, FBALL], "result", rules="booktabs", num=2, txt=2,
          note="Rank | Coach | Composite score | Years, booktabs, five football coaches with "
               "three-decimal scores. Two of the five seasons are ranges that end before the "
               "coach's last year in the ranking table above")
    table(22, 1, 6, 4, "Table 9 Model’s Top 5 coaches in NCAA Baseball", "Table N",
          cited(22, 22, ["table 9"], 1,
                "We used EXCEL to calculate and ranking the model’s Top 5 coaches as table 9."),
          [IAHP, BASEBALL], "result", rules="booktabs", num=2, txt=2,
          note="the same four columns for baseball. The coach column is corrupted in the "
               "typesetting: row 1 reads 'Gordie Gillespie Augie' because the second-placed "
               "surname has been pulled into the first cell, row 4 reads 'Gene StephensonBill' "
               "for the same reason, and row 5 keeps only 'Holowaty'")
    table(23, 1, 2, 7, "Table 10 The weight of each metrics", "Table N",
          cited(23, 23, ["table 10"], 1,
                "calculate the weight of each metrics as table 10."),
          [IAHP, GENDER], "result", rules="boxed", num=7,
          note="two rows only: a w1..w7 label row over the seven weights of the seven "
               "woman-coach metrics. Boxed with verticals, like Table 5 and Table 7 rather than "
               "like the ranking grids. The caption has no full stop")
    table(24, 1, 6, 4,
          "Table 11 Model’s Top 5 Woman coaches in NCAA Women's Basketball", "Table N",
          cited(23, 24, ["Table 11"], 1,
                "We used EXCEL to calculate and ranking the model’s Top 5 coaches as Table 11."),
          [IAHP, GENDER], "result", rules="booktabs", num=2, txt=2,
          note="Rank | Coach | Composite score | Years, booktabs, the five woman coaches. Cited "
               "on page 23, printed at the top of page 24, so the pointer and the grid sit on "
               "opposite sides of the page break")
    table(24, 3, 6, 4, "Table 12 The Top 5 Coaches of College", "Table N",
          cited(24, 24, ["table 12"], 1,
                "We find out these best coaches and make the rank top 5 as table 12."),
          [IAHP, BEST], "result", rules="booktabs", num=2, txt=2,
          note="the cross-sport grid: Rank | Coach | Composite score | College Sports, one "
               "coach per sport at the top, two basketball coaches in places 3 and 4, and the "
               "scores carry three and six decimals in the same column because two of them are "
               "copied from the six-decimal basketball grid")

    # ---- the raster portrait ------------------------------------------------
    figure(24, 4, "photo-or-raster-image", "Figure 6 Pat Summitt", "Figure N",
           cited(24, 24, ["figure 6"], 1,
                 "Here goes a brief introduction and figure 6 for our Best all time college "
                 "coach."),
           [IAHP, BEST], "result", ticks=False,
           note="a colour photograph of Pat Summitt on a ladder cutting down a net, one "
                "raster image in the right-hand column, no frame. Its caption is not a "
                "caption line: 'Figure 6 Pat Summitt' prints at the tail of the last body "
                "line of the prose paragraph beside it")

    # ---- the four time-line line charts -------------------------------------
    table(25, 1, 8, 10, "Table 13 The composite score of Dean Smith each year", "Table N",
          cited(25, 25, ["table 13"], 1,
                "Then calculate the composite score of Dean Smith each year from 1961 to 1997 "
                "shown as table 13."),
          [IAHP, TIMELINE], "result", rules="boxed", num=9, txt=1,
          note="NO HEADER ROW: the grid is four year/score pairs - a row of years behind a "
               "'year' stub, then the matching scores behind a 'score' stub - so the first "
               "printed row is data and the census floors header_rows at 1. Ten columns (stub "
               "plus nine years), eight rows, boxed with a vertical between every column. Only "
               "the year-row stubs carry a light grey fill; the value cells are white. The "
               "last pair stops at 1996 while the prose promises 1961 to 1997, and 1997 is the "
               "point the chart below plots")
    figure(25, 2, "line",
           "Figure 7 The line chart for basketball coach Dean Smith", "Figure N",
           cited(25, 25, ["figure 7", "Figure 7"], 4,
                 "we used EXCEL to draw a line chart of Time Line Horizon -Coaching as "
                 "figure 7.",
                 "The figure compares with figure 7, we found the fluctuation range", read=3),
           [IAHP, TIMELINE], "result", labels=False,
           note="single Excel series with round markers on the default grey plot field, "
                "horizontal gridlines only, in-art title 'The time line horizon-coaching', "
                "y axis Coaching 0-0.8, x axis Time line horizon labelled every other year. "
                "No legend and no data labels; every point is 1961-1997 for one coach")
    figure(26, 1, "line",
           "Figure 8 The line chart for women’s basketball coach Pat Summitt", "Figure N",
           cited(26, 26, ["figure 8", "Figure 8"], 2,
                 "draw a line chat of Time Line Horizon -Coaching as figure 8.",
                 "The results similar to Figure 7, Figure 8, as to different gender of the "
                 "same sports, time line horizon makes a difference in coaching.", read=2),
           [TIMELINE, DIFFGEN], "result", labels=False,
           note="the same Excel chart for a women's coach: grey plot field, horizontal "
                "gridlines, y axis 0-0.6, years 1974-2012. The pointer sentence calls it a "
                "'line chat'")
    figure(27, 1, "line", "Figure 9 The line chart for football coach Joe Paterno",
           "Figure N",
           cited(27, 27, ["Figure 9", "figure 9"], 2,
                 "The results similar to Figure 7, Figure 9, as to different sport of the "
                 "same gender, time line horizon makes a difference in coaching.",
                 "The results similar to Figure 9, Figure 10, as to same sport of the same "
                 "gender, time line horizon makes a difference in coaching.", read=2),
           [TIMELINE, DIFFSPORT], "result", labels=False,
           note="same chart, y axis 0-0.8, years 1966-2011. NOBODY INTRODUCES IT: the "
                "section heading runs straight into the chart and the only sentences that "
                "name it come after it, comparing it with Figures 7 and 10")
    figure(27, 2, "line", "Figure 10 The line chart for football coach Bobby Bowden",
           "Figure N",
           cited(27, 27, ["Figure 10"], 1,
                 "The results similar to Figure 9, Figure 10, as to same sport of the same "
                 "gender, time line horizon makes a difference in coaching."),
           [TIMELINE, SAMESPORT], "result", labels=False,
           note="same chart, y axis 0-0.8, years 1970-2009. Cited only from the page after "
                "it prints, in the same sentence as Figure 9")

    # ---- the flow chart -----------------------------------------------------
    figure(30, 2, "flowchart-or-schematic",
           "Figure 11 Sensitivity analysis process flowchart", "Figure N",
           cited(30, 30, ["figure 11"], 1,
                 "Sensitivity analysis process of single metric score shows in figure 11."),
           [MODTEST, SENS], "sensitivity", ticks=False, labels=True,
           note="a vertical flow chart in a single column: Original data evaluation, Sort, "
                "Given initial r, Re-evaluation, Sort, a consistency decision with a Y and "
                "an N branch, the r=r+dr increment looping back, and Get the final score of "
                "r at the foot. Black boxes and arrows, no axes, no legend")

    # ---- the four deviation grids and the sensitivity grid -------------------
    table(28, 2, 3, 6, "Table 14 Basketball Coaches", "Table N",
          cited(28, 28, ["table 14"], 1, "comparison table as below table 14."),
          [MODTEST, DEVTEST], "test", rules="boxed", num=5, txt=1,
          note="the deviation grid: a header Rank | 1 | 2 | 3 | 4 | 5 over two body rows, "
               "one for the five names the model drew and one for the five the official "
               "website publishes, each name wrapped over two lines inside one tall cell. "
               "Boxed with a vertical between every column, no shading. The point of the grid "
               "is that the two rows contain the same five names in a different order")
    table(29, 1, 3, 6, "Table 15 Women’s basketball coach", "Table N", none_mention(),
          [MODTEST, DEVTEST], "test", rules="boxed", num=5, txt=1,
          note="the same six columns and two stub rows for the woman coaches; never cited by "
               "number, its caption is the only naming it gets. Here the two rows hold the same "
               "five names in a different order and one name (Tara VanDerveer) swaps places "
               "with Nancy Fahey")
    table(29, 2, 3, 6, "Table 16 Football coaches", "Table N", none_mention(),
          [MODTEST, DEVTEST], "test", rules="boxed", num=5, txt=1,
          note="the same grid for football; never cited by number. Rank | 1..5 over the model "
               "row and the website row, both wrapping surnames over two lines. Boxed, no "
               "shading")
    table(29, 3, 3, 6, "Table 17 Baseball coach", "Table N", none_mention(),
          [MODTEST, DEVTEST], "test", rules="boxed", num=5, txt=1,
          note="the same grid for baseball, and the one whose two rows disagree: only two of "
               "the five names survive, the website row prints names with quotation marks and "
               "the surname 'Slcip schaly' split across two lines. Never cited by number")
    table(31, 1, 3, 4, "Table 18 Metrics score sensitivity analysis", "Table N",
          cited(31, 31, ["table 18"], 1,
                "Using MATLAB, sensitivity analysis results in the table 18."),
          [MODTEST, SENS], "sensitivity", rules="boxed", num=3, txt=1,
          note="three rows by four columns: a header 'Metrics variables | years | Winning | "
               "Games' where the last two words are one column name split by the typesetting, "
               "a wrapped stub row 'Metrics score change threshold' over three bracketed "
               "intervals, and an 'Interval Range' row over the three ranges. Boxed with a "
               "vertical between every column")

    # ---- refusals -----------------------------------------------------------
    exclude(2, 1, "not-an-exhibit",
            "the prose fragment '0.0297, average interval of evaluation metrics in "
            "sensitivity analysis is less than 10%' boxed by two rules; no exhibit")
    exclude(10, 1, "not-an-exhibit",
            "the tail of formula (4): the square-root and sigma glyphs of the standard "
            "deviation, five paths, no exhibit")
    exclude(17, 1, "split-across-pages",
            "the six remaining body rows of Table 4 (A2 Classification 3 through Bn metric "
            "n), no repeated header, no continued marker; the row is the topmost fragment on "
            "page 16")
    exclude(24, 2, "not-an-exhibit",
            "the body sentences 'Using the model we also can get the NCAA women's Basketball "
            "top 5 woman coaches' with four paths of typesetting debris")
    exclude(28, 1, "not-an-exhibit",
            "the text of the dimensional consistency test, boxed by nine paths of rule "
            "artefacts")
    exclude(29, 4, "not-an-exhibit",
            "the reasonable-hypothesis-test paragraph, seven paths")
    exclude(30, 1, "not-an-exhibit",
            "the two-line tail of the baseball deviation paragraph carried over from page "
            "29, two paths")
    exclude(32, 1, "not-an-exhibit",
            "three lines of the Sports Illustrated article's closing paragraph")
    exclude(34, 1, "not-an-exhibit",
            "the reference list, six paths of link underlines")


def main() -> int:
    build()
    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": ITEMS,
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": RULES,
        "note": NOTE,
    }
    out = PROXY / "pc61-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{out} items={len(ITEMS)} tables={len(TABLES)} excluded={len(EXCLUDED)}")
    return 0


RULES: list[str] = [
    "All eighteen table captions print above the grid and all eleven figure captions print "
    "below the art; nothing in this paper puts a caption above a chart [caption.position]",
    "Two house frames, split by exhibit type rather than by section: every ranking grid is "
    "booktabs with no verticals at all, and every weight, deviation and sensitivity grid is "
    "fully boxed with a rule between every row and a vertical between every column "
    "[table.rule_style]",
    "No grid in the paper bands its rows: the only grey fills are the two label rows of "
    "Table 2, the year stubs of Table 13, and the plot fields of the four Excel charts "
    "[table.zebra]",
    "A grouped header is always a real merge, never a repeated word: 'The first level "
    "metrics' and 'The second level metrics' each span two columns in Table 4, and the "
    "three classifications span three, three and four columns in Table 7 [table.merged_cells]",
    "Only the three-group weight grids carry two header rows; the year/score grid carries "
    "none and keeps its stub labels inside the data rows [table.header_rows]",
    "One grid is set narrow and centred and seventeen run to the full measure "
    "[table.width]",
    "Captions are quoted with the paper's own punctuation, full stops and missing full "
    "stops included, and no table caption is a sentence with a verb [caption.verbatim]",
    "One grid crosses a page break and the topmost fragment is the row that carries it; the "
    "continuation is a refusal, not a second table [table.continued]",
    "The heading detector found seven headings in thirty-five pages, so every section label "
    "recorded here is the heading as printed, marked unnumbered [place.section_numbered]",
    "Five of the eleven figures are metric trees and one is a flow chart; the closed "
    "vocabulary has no tree member, so all six land on the schematic family "
    "[geometry.family]",
    "Only the four time-line charts print numbers on their axes; the trees and the flow "
    "chart carry text labels and no axes at all [geometry.printed_numbers]",
    "No chart in the paper carries a legend and none labels its points [geometry.legend]",
    "Exact decimal alignment is absent everywhere: every numeric column is centred with "
    "identical digit counts, so nothing here demonstrates a decimal axis "
    "[table.decimal_aligned]",
    "Numbers are printed once each and never reused - Figure 1 to Figure 11 and Table 1 to "
    "Table 18 - but page 16 points at 'Figure 1' while describing Figure 4 [mention.count]",
    "A section label follows the heading, not the pointer sentence: where the pointer prints "
    "on the far side of a page break the label still names the section the exhibit sits in "
    "[place.section_path]",
]

NOTE = (
    "Eleven figure rows and eighteen tables over 38 measured regions on 24 of 35 pages, plus "
    "nine refusals. Families: table-grid 18, flowchart-or-schematic 6 (five metric trees and "
    "Figure 11's flow chart), line 4, photo-or-raster-image 1.\n"
    "\n"
    "Declared decisions. (1) Page 12 carries twenty-three vector paths with no measured "
    "region; the page prints the consistency conditions, formulas (6) and (7) and the single "
    "objective model, so the paths are formula glyphs and no exhibit is missing a box. "
    "(2) Figure 2's caption is typed from the crop: the text layer prints a stray in-art 'SOS' "
    "token between the bold number and the caption sentence, which the printed caption line "
    "does not contain. (3) Figure 6's caption is not a caption line - 'Figure 6 Pat Summitt' "
    "prints at the tail of the last body line of the paragraph beside the photograph. "
    "(4) Table 4 is one table over two pages: the header and ten rows at the foot of page 16, "
    "six rows at the top of page 17 with no repeated header; the page-17 fragment is a "
    "split-across-pages refusal. (5) Table 13 prints no header row, so header_rows is floored "
    "at 1 with the first printed row being data. (6) The paper reuses no exhibit number, but "
    "its prose misdirects twice: page 16 says 'As shown in Figure 1' while describing "
    "Figure 4, and Figure 9 is never introduced before it prints."
)

if __name__ == "__main__":
    sys.exit(main())
