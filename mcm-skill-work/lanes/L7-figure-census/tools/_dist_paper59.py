"""Hand pass for P-B-2014-26636-060c74b1 (a 2014 B paper that ranks college coaches
with a fuzzy consistent matrix, validates it against three other published rankings,
adds a Shannon-entropy cross-check and then sweeps the parameter of the matrix), 38
PDF pages.

Forty-eight measured regions over twenty-two pages, all accounted for: twenty-seven
tables, four figure rows, seventeen refusals. The paper is almost entirely a table
census - it prints twenty-five numbered grids plus two unnumbered notation grids, and
only four exhibits are pictures at all.

    page    region   what it is
    5       r1       unnumbered Notations/Explanations grid, 11 x 2
    8       r1       Table 1   factors and explanations
    10      r1       Table 2   interrelationship among the four factors
    10      r2       Table 3   correlation / standard data array - FIRST fragment,
                     caption at y=607; the grid continues on p11 (whole page) and
                     p12 (two-row tail)
    12      r2       Table 4   grey relational coefficient / degree matrix
    13      r2       Table 5   rank of the college men's basketball coaches
    14      r1       Table 5   continuation, 17 rows + the table footnote
    15      r1       Table 6.1 factors and explanations in football
    15      r2       Table 6.2 factors and explanations in ice hockey
    15      r3       Table 7.1 top 5 football coaches
    16      r1       Table 7.2 top 5 ice-hockey coaches - caption stayed on p15
    16      r2       Table 8   rank comparison, basketball
    16      r3       Table 9   rank comparison, football
    16      r4       Table 10  rank comparison, ice hockey
    18      r1       Figure 1  mean winning percentage by era
    18      r2       Figure 2  mean wins by era
    18      r3       Figure 3  mean NCAAB championships by era - caption on p19
    19      r1       Table 11  one-way ANOVA
    19      r2       Table 12  one-way ANOVA
    20      r1       Table 13  rank of the top 10 before adjustment
    20      r2       Table 14  rank of the top 10 after adjustment - FIRST fragment
    21      r1       Table 14  continuation, 6 rows
    21      r2       Table 15  top 5 college women's basketball coaches
    22      r2       unnumbered Notation/Explanation grid for the entropy method
    24      r1       Table 16  results based on the entropy method
    25      r1       Table 16  continuation, 6 rows
    25      r2       Table 17  comparison of the two methods
    25      r3       Table 18  comparative importance among factors after adjustment
    26      r1       Table 18  continuation, 2 rows
    26      r2       Table 19  rank after adjustment, 27 rows
    26      r3       Table 20  comparison of the two fuzzy consistent matrices
    27      r1       Table 20  continuation, ranks 5-10
    27      r2       Table 21  rank with rho = 0.5
    27      r3       Table 22  rank with rho = 0.4 - FIRST fragment, one row only
    28      r1       Table 22  continuation, ranks 2-10
    28      r2       Table 23  rank with rho = 0.6
    37      r6       a strip of three coach photographs butted edge to edge; r4 and r5
                     are panels 2 and 3 of the same captionless strip, r1-r3 are prose
                     paragraphs the producer emitted as white text-frame patches

Usage: python -I tools/_dist_paper59.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2014-26636-060c74b1"
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

RHO = ""  # the Symbol-font rho the paper prints in the three captions

MODEL = "2 Model"
NOTATIONS22 = "2.2 Notations and definitions"
NOTATIONS221 = "2.2.1 Notations"
APPLICATION = "3 Application"
SELECTION = "3.2 The selection of factors"
CALCULATION = "3.4 Calculation"
OTHERSPORTS = "3.5 Application of our model to other sports"
COMPARISON4 = "4 Comparison of the ranks from different sources"
TIMELINE = "5 The analysis of time line horizon"
PROCEDURES = "5.2 Procedures"
GENDER = "6 The analysis of gender"
STABILITY = "7 Stability test"
INTRO711 = "7.1.1 Introduction"
NOTATION712 = "7.1.2 Notation"
OUTCOMES714 = "7.1.4 Comparison of the outcomes"
SENSITIVITY72 = "7.2 Testing the influence of changing the comparative im-"
SENSITIVITY8 = "8 Sensitivity test"
APPENDIX = "Appendix"

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
           legend: str = "none", labels: bool = False, source: str = "text-layer",
           cap_page: int | None = None, numbered: bool = True, note: str = "") -> None:
    word = q(cap, cap_page or page) if cap else ""
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": word,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, path, kind, numbered),
        "mention": mention,
        "caption": caption(word, numbering, "below"),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": True,
            "data_labels": labels,
        },
    })


def table(page: int, reg: int, rows: int, cols: int, cap: str, numbering: str,
          mention: dict, path: list[str], kind: str, *, header_rows: int = 1,
          rules: str = "boxed", zebra: bool = False, merged: bool = False,
          num: int = 0, txt: int = 0, decimal: bool = False,
          note_sentence: str = "", note: str = "", source: str = "text-layer",
          cap_page: int | None = None) -> None:
    word = q(cap, cap_page or page) if cap else ""
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": word,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, path, kind),
        "mention": mention,
        "caption": caption(word, numbering, "above"),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header_rows,
            "rule_style": rules,
            "zebra": zebra,
            "merged_cells": merged,
            "diagonal_header": False,
            "units_in_header": False,
            "decimal_aligned": decimal,
            "numeric_cols": num,
            "text_cols": txt,
            "width": "full",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": note_sentence,
        },
    })


def exclude(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "region": reg, "bbox": REG[(page, reg)],
                     "reason": reason, "note": note})


def build() -> str:
    # ---- 2.2.1 Notations: an unnumbered glossary grid -------------------------
    table(5, 1, 11, 2, "", "none", none_mention(),
          [MODEL, NOTATIONS22, NOTATIONS221], "symbols", txt=2, source="none",
          note="unnumbered: the grid sits directly under the heading 2.2.1 Notations with "
               "no caption and no table number, its header row being the two words "
               "Notations and Explanations; italic symbol stubs on the left, prose "
               "definitions that wrap to two or three lines on the right")

    # ---- 3.2 / 3.4 the factor model ------------------------------------------
    table(8, 1, 4, 2, "Table 1 Factors and Explanations", "Table N",
          cited(8, 8, ["Table 1"], 1, "Table 1 shows the definition of each fac-"),
          [APPLICATION, SELECTION], "other", txt=2,
          note="four factors - Wins, Pct., NCAAB Champions, Coach Awards - against their "
               "definitions; the caption line is welded to the grid's top rule and the "
               "Coach Awards explanation runs to four lines")
    table(10, 1, 4, 5, "Table 2.Interrelationship among the four factors5", "Table N.",
          cited(9, 10, ["Table 2"], 1,
                "Table 2 summarizes the interrelationship among the four factors."),
          [APPLICATION, CALCULATION], "solution", num=4, txt=1,
          note="a 4 x 4 fuzzy preferential relation matrix over the same four factors; the "
               "stub header cell above the left column is BLANK, and the caption carries a "
               "footnote marker that the text layer welds to the last word, 'factors5'")
    table(10, 2, 27, 6, "Table 3.Correlation data array and standard data array", "Table N.",
          cited(10, 10, ["Table 3"], 1,
                "Table 3 dis- plays the correlation data array and the standard data array."),
          [APPLICATION, CALCULATION], "solution", num=5, txt=1,
          note="THE FIRST FRAGMENT ONLY: three data rows at the foot of page 10 under the "
               "caption, then the whole of page 11 (22 more rows, no repeated header, one "
               "orphan row carrying a lone '9') and a two-row tail at the top of page 12 "
               "with the table's foot rule. 27 rows over six columns for 27 coaches; both "
               "continuations are refused as split-across-pages")
    table(12, 2, 27, 6, "Table 4. Grey relational coefficient and Grey relational degree matrix",
          "Table N.",
          none_mention(), [APPLICATION, CALCULATION], "solution", num=2, txt=4,
          note="18 rows on page 12 and 9 more at the top of page 13, whose first line is a "
               "clipped header stump; the grid is the grey relational coefficient and "
               "degree matrix for the same 27 coaches. NEVER CITED BY NUMBER")
    table(13, 2, 27, 6, "Table 5. Rank of college men’s basketball coaches", "Table N.",
          none_mention(), [APPLICATION, CALCULATION], "solution", num=2, txt=4, zebra=True,
          note="10 rows under the caption and 17 more on page 14, which also prints the "
               "table footnote 'Coaches marked in gray are the top 5 basketball coaches of "
               "all time.'; that footnote is the key to the grey block over the first five "
               "rows, so zebra is true for this table but the shading marks the top five "
               "rather than alternating - it is not striping. NEVER CITED BY NUMBER")

    # ---- 3.5 the same model applied to two other sports ----------------------
    table(15, 1, 4, 2, "Table 6.1. Factors and Explanations in football", "Table N.",
          cited(14, 15, ["Table 6.1"], 1,
                "The factors and explanations are shown in Table 6.1 and Table 6.2."),
          [APPLICATION, OTHERSPORTS], "model", txt=2,
          note="the football restatement of Table 1; the NCAA National Championship "
               "explanation is truncated on the page to the phrase 'The amount of Bowl'. "
               "Cited on page 14 together with Table 6.2 by one sentence")
    table(15, 2, 4, 2, "Table 6.2. Factors and Explanations in ice-hockey", "Table N.",
          cited(14, 15, ["Table 6.2"], 1,
                "The factors and explanations are shown in Table 6.1 and Table 6.2."),
          [APPLICATION, OTHERSPORTS], "model", txt=2,
          note="the ice-hockey restatement; prints 'NCCA Champions' for NCAA Champions")
    table(15, 3, 5, 6, "Table 7.1.Top 5college men’s football coaches", "Table N.",
          cited(14, 15, ["Table 7.1"], 1,
                "The top 5 of both sports are shown in Table 7.1 and Table 7.2 respectively."),
          [APPLICATION, OTHERSPORTS], "model", num=5, txt=1,
          note="five football coaches with wins, percentage, national championships, coach "
               "awards and the grey relational degree; no shading here even though it is "
               "likewise a top-five grid, unlike Table 5; the caption runs the number into "
               "the word, 'Top 5college'")
    table(16, 1, 5, 6, "Table 7.2.Top 5 college men’s ice hockey coaches", "Table N.",
          cited(14, 16, ["Table 7.2"], 1,
                "The top 5 of both sports are shown in Table 7.1 and Table 7.2 respectively."),
          [APPLICATION, OTHERSPORTS], "model", num=5, txt=1,
          cap_page=15,
          note="THE ONE TABLE WHOSE CAPTION AND GRID SIT ON DIFFERENT PAGES: the caption "
               "prints at y=725 on page 15, below Table 7.1, and the grid starts at the top "
               "of page 16 with only a clipped header remnant ('Awards', 'al degree') above "
               "its five rows")

    # ---- 4 comparison against four published rankings ------------------------
    table(16, 2, 5, 5, "Table 8.Comparison of the rank of top 5 college men’s basketball coaches",
          "Table N.", none_mention(), [COMPARISON4], "other", num=1, txt=4,
          note="the paper's own top five against The Model, Bleacher Report, ESPN (including "
               "women) and Yahoo Sports; capitalisation is inconsistent ('John wooden', "
               "'Bob knight', 'John Mclendon') and the last Yahoo cell prints the duplicated "
               "fragment 'Jerry Tar-Tar-kanian'. NEVER CITED BY NUMBER")
    table(16, 3, 5, 5, "Table 9.Comparison of the rank of top 5 college men’s football coaches",
          "Table N.", none_mention(), [COMPARISON4], "other", num=1, txt=4,
          note="the football twin of Table 8; header cells are source names, one abbreviated "
               "to 'Statesman'. NEVER CITED BY NUMBER")
    table(16, 4, 5, 3, "Table 10. Comparison of the rank of top 5 college men’s ice-hockey coaches",
          "Table N.", none_mention(), [COMPARISON4], "other", num=1, txt=2,
          note="DECLARED PARTIAL MEASUREMENT: only four of the five rows fall inside this "
               "region; the fifth, Ned Harkness, sits at the top of page 17 in a block the "
               "detector saw as 23 paths but measured as no region, so the row count is the "
               "printed five and the region holds four. NEVER CITED BY NUMBER")

    # ---- 5 the timeline analysis, its three charts and two ANOVAs ------------
    figure(18, 1, "line", "Figure 1.The mean values of winning percentages", "Figure N.",
           cited(17, 18, ["Figure 1"], 1,
                 "Figure 1 shows the means of winning percentages in all groups."),
           [TIMELINE, PROCEDURES], "other", legend="below",
           note="one Excel line chart exported as a bitmap inside a thin vector frame: in-art "
                "title 'winning percentage', y 0.52-0.64, five era categories from 'Before "
                "1930s' to '1990s and 2000s', horizontal gridlines only, single series and a "
                "legend below the plot area. Cited twice on page 17, the page before the art")
    figure(18, 2, "line", "Figure 2.The mean values of wins", "Figure N.",
           cited(17, 18, ["Figure 2"], 1, "Figure 2 shows the means of wins in all groups."),
           [TIMELINE, PROCEDURES], "other", legend="below",
           note="the same construction and the same five era categories, y 0-500, series "
                "labelled 'Wins'; flat at about 380 until the last category drops to 300")
    figure(18, 3, "line", "Figure 3.The mean values of NCAAB Champions6", "Figure N.",
           cited(17, 18, ["Figure 3"], 1,
                 "Figure 3 shows the mean values of the times of winning NCAAB champi-"),
           [TIMELINE, PROCEDURES], "other", legend="below", cap_page=19,
           note="third chart of the same family, y 0-0.7, a peak in the 1930s-1940s bin; its "
                "caption was pushed to the top of page 19, so the art is on 18 and the "
                "caption on 19, and the text layer welds a footnote marker to the title, "
                "'NCAAB Champions6'. The in-art title repeats the paper's NCAA/NCAAB misspelling")
    table(19, 1, 3, 7, "Table 11.", "Table N.", cited(19, 19, ["Table 11"], 1,
                                                      "Table 11 demonstrates that the P-value is greater than 0.05"),
          [TIMELINE, PROCEDURES], "other", num=5, txt=2,
          note="a one-way ANOVA grid - Source of SS, Df, MS, F, P-value, F crit - with three "
               "rows (among the five groups, within each group, sum) and NO printed title, the "
               "caption being the bare 'Table 11.'; the F value wraps mid-number and the "
               "P-value and F crit cells are blank on the two lower rows")
    table(19, 2, 3, 7, "Table 12.", "Table N.",
          cited(19, 19, ["Table 12"], 1,
                "Table 12 shows that there is a significant difference of variances among all five groups."),
          [TIMELINE, PROCEDURES], "other", num=5, txt=2,
          note="the second bare 'Table 12.' ANOVA grid; three numeric cells wrap mid-number "
               "('3.3817 / 495', '0.009770 / 28', '2.3950026 / 16') and the sum row is bold")

    # ---- 5/6 the rank adjustment --------------------------------------------
    table(20, 1, 10, 3, "Table 13.The rank of Top 10 college men’s basketball coaches before adjustment",
          "Table N.",
          cited(20, 20, ["Table 13"], 1,
                "Table 13 shows the winning percentages and grey relational degree of top 10 coaches before adjustment"),
          [TIMELINE, PROCEDURES], "other", num=2, txt=1,
          note="despite the title there is no rank column: name, percentage and grey "
               "relational degree only, ten rows; one value drops trailing precision ('0.75')")
    table(20, 2, 10, 4, "Table 147.The rank of Top 10 college men’s basketball coaches after adjustment",
          "Table N.",
          cited(20, 20, ["Table 14"], 1,
                "while Table 14 shows the winning percentages and grey relational degree of top 10 coaches after adjustment."),
          [TIMELINE, PROCEDURES], "other", num=2, txt=2,
          note="THE TEXT LAYER WELDS THIS CAPTION INTO 'Table 147.' - the page prints "
               "'Table 14.' followed by the period, and the italic period plus the next word "
               "extracts as a 7, so the quoted caption is the layer's form and the note "
               "records the printed one. Four rows under the caption and six at the top of "
               "page 21, with no repeated header and no continued marker; the table gains a "
               "correction-factor column the before-adjustment grid does not have")
    table(21, 2, 5, 6, "Table 15 The top 5 of college women’s basketball coaches", "Table N",
          cited(21, 21, ["Table 15"], 1,
                "Table 15 displays the top 5 of college women’s basketball coaches."),
          [GENDER], "result", num=5, txt=1,
          note="two rows under the caption and three more at the top of page 22, so the "
               "printed five are split 2 + 3 across the page break; header cells wrap to two "
               "and three lines but each is one cell, not a merge")

    # ---- 7.1.2 the entropy notation grid ------------------------------------
    table(22, 2, 5, 2, "", "none", none_mention(),
          [STABILITY, INTRO711, NOTATION712], "symbols", txt=2, source="none",
          note="unnumbered: the Notation/Explanation grid for the Shannon entropy method, "
               "five rows (C, C-prime, Q, h_i, W) under the heading 7.1.2 Notation, printed "
               "with a full box like every other grid in the paper and with visibly looser "
               "row padding than the numbered tables")
    table(24, 1, 27, 6, "Table 16.Results based on Entropy Method", "Table N.",
          cited(24, 24, ["Table 16"], 1,
                "Table 16 shows the rank of college coaches based on Shannon’s entropy method and grey correlation analysis."),
          [STABILITY, NOTATION712], "symbols", num=2, txt=4, zebra=True,
          note="21 rows on page 24 and 6 on page 25 where the table note 'Coaches marked in "
               "grey are the top 5 basketball coaches of all time' explains the grey block "
               "over the first five rows - semantic highlighting, not striping, so zebra is "
               "true and the note says which rows it covers")
    table(25, 2, 10, 3, "Table 17.Comparison between Fuzzy Consistent Matrix Method and Entropy Method",
          "Table N.",
          cited(25, 25, ["Table 17"], 1,
                "Table 17 shows that the name lists of top 10 coaches generated from the above two methods are identical"),
          [STABILITY, OUTCOMES714], "result", num=2, txt=1,
          note="ten ranks against the two methods; the caption line is printed INSIDE the "
               "measured region, welded to the grid, so the crop shows the title as well as "
               "the table. Five rows (2, 3, 7, 8, 9) are shaded with no legend and no "
               "pattern - neither alternation nor a disagreement marker, since row 7 agrees - "
               "so zebra stays false")

    # ---- 7.2 the parameter sweep --------------------------------------------
    table(25, 3, 4, 5, "Table 18.The comparative importance among factors after adjustment",
          "Table N.", none_mention(), [STABILITY, SENSITIVITY72], "test", num=4, txt=1,
          note="a 4 x 4 importance matrix of the four factors; the stub-column header cell is "
               "BLANK and the header spells 'NCCAB Champions' where Table 16 on the previous "
               "page spells 'NCAAB Champions'. Two rows here and two at the top of page 26")
    table(26, 2, 27, 6, "Table 19.Rank of college men’s basketball coaches after adjustment",
          "Table N.",
          cited(26, 26, ["Table 19"], 1,
                "Table 19 displays the rank of college men’s basketball coaches after adjustment."),
          [STABILITY, SENSITIVITY72], "test", num=2, txt=4, zebra=True,
          note="27 rows, the paper's longest single grid and its only genuinely alternating "
               "grey fill; the relational-degree column keeps nine decimals while every other "
               "numeric cell rounds to three; this is the only table whose whole body sits on "
               "one page")
    table(26, 3, 10, 3, "Table 20.Comparison of outcomes based on two different Fuzzy Consistent Matrixes",
          "Table N.",
          cited(26, 26, ["Table 20"], 2,
                "Table 20 compares the outcome in this section with the outcome in the previous section."),
          [STABILITY, SENSITIVITY72], "test", num=2, txt=1,
          note="rank under two fuzzy consistent matrices side by side; four rows on page 26 "
               "and six at the top of page 27 with no repeated header. Cited twice - on page "
               "26 and again on 27, where 'We can see from Table 20 that the outcome is "
               "slightly different' is the paper's only statement of the discrepancy")

    # ---- 8 the rho sensitivity sweep ----------------------------------------
    table(27, 2, 10, 3,
          "Table 21. Rank of college men’s basketball coaches ( " + RHO + " =0.5)", "Table N.",
          cited(27, 27, ["Table 21"], 1, "Table 21 shows the rank of coaches when"),
          [SENSITIVITY8], "test", num=2, txt=1,
          note="the parameter is printed as the Symbol-font rho, not a lambda, and the caption "
               "leaves a space before the equals sign: '( rho =0.5)'. Rank, name and grey "
               "relational degree for ten coaches; the caption line itself was not captured "
               "by the caption pass, only by the heading and mention passes, so the verbatim "
               "here comes from the text layer")
    table(27, 3, 10, 3,
          "Table 22. Rank of college men’s basketball coaches ( " + RHO + " =0.4)", "Table N.",
          cited(27, 27, ["Table 22"], 1, "Table 22 and Table 23show the rank of coaches when"),
          [SENSITIVITY8], "test", num=2, txt=1,
          note="ONE row under the caption before the page break and nine more at the top of "
               "page 28, with no repeated header, so the tail is a headerless column of ranks "
               "and numbers; the citing sentence welds the two table numbers together as "
               "'Table 23show'")
    table(28, 2, 10, 3,
          "Table 23.Rank of college men’s basketball coaches ( " + RHO + " =0.6)", "Table N.",
          cited(27, 28, ["Table 23"], 1, "Table 22 and Table 23show the rank of coaches when"),
          [SENSITIVITY8], "test", num=2, txt=1,
          note="the last grid of the paper; its header cell prints the stray Chinese "
               "characters 'gong shi' (formula) directly after the closing parenthesis of "
               "'Grey Relational Degree ( rho =0.6)', the only Chinese text in the document")

    # ---- appendix: three photographs butted into one captionless strip -------
    figure(37, 6, "composite-panel", "", "none", none_mention(),
           [f"未编号标题 {APPENDIX}"], "appendix", panels=3, layout="1x3",
           source="none", numbered=False,
           note="three REAL COLOUR PHOTOGRAPHS butted edge to edge with zero gutter - x "
                "111-247, 247-395, 395-489 on page 37 - of John Wooden, 'Bear' Bryant and Pat "
                "Summitt in that left-to-right order, matching the three prose paragraphs above "
                "them ('May be he is John Wooden ... / May be he is \"Bear\" Bryant ... / May "
                "be she is Pat Summitt ...'). No figure number, no caption, no rules, so the "
                "row is the leftmost panel with panel_count 3 and the other two panels are "
                "refused as fragments of the same strip")

    # ---- the refused regions -------------------------------------------------
    exclude(3, 1, "not-an-exhibit",
            "one paragraph of the literature review, 'their coaches (Rushall, B. S., et al., "
            "1985), interviewing coaches (Cassidy., et al., 2006), ...'; the four vector paths "
            "are the invisible white text-frame patches this document's producer emits per "
            "line, not a rule, box or highlight")
    exclude(7, 1, "not-an-exhibit",
            "a display formula - 'min min x(k) x(k ...' - set as a vector block of nine paths; "
            "it is an equation, not an exhibit")
    exclude(11, 1, "split-across-pages",
            "the body of Table 3, 22 rows filling page 11 with no repeated header and one "
            "orphan row carrying a lone '9'; continues the grid captioned on page 10")
    exclude(12, 1, "split-across-pages",
            "the two-row tail of Table 3 at the top of page 12, ending with the table's foot "
            "rule; same grid as the p10 fragment")
    exclude(13, 1, "split-across-pages",
            "nine more rows of Table 4 above the page's own Table 5 caption, the first line "
            "being a clipped header stump ('76', '06', '3'); Table 4's caption and first "
            "eighteen rows are on page 12")
    exclude(14, 1, "split-across-pages",
            "seventeen more rows of Table 5, page 14, closing with the table footnote 'Coaches "
            "marked in gray are the top 5 basketball coaches of all time.'; Table 5's caption "
            "and first ten rows are on page 13")
    exclude(21, 1, "split-across-pages",
            "the tail of Table 14, ranks 5-10, at the top of page 21 with no repeated header "
            "and no continued marker")
    exclude(22, 1, "split-across-pages",
            "the three-row tail of Table 15 (Tara VanDerveer, Sylvia Hatchell, Barbara "
            "Stevens) at the top of page 22; Table 15's caption and first two rows are on "
            "page 21")
    exclude(25, 1, "split-across-pages",
            "six more rows of Table 16 at the top of page 25, closing with the grey-band "
            "footnote; the caption and twenty-one rows are on page 24")
    exclude(26, 1, "split-across-pages",
            "the two-row tail of Table 18 (NCCAB Champions, Coach Awards) in a thin strip at "
            "the top of page 26; the caption and the first two rows are on page 25")
    exclude(27, 1, "split-across-pages",
            "ranks 5-10 of Table 20 at the top of page 27, with five of the six rows shaded "
            "irregularly and no repeated header; the caption and ranks 1-4 are on page 26")
    exclude(28, 1, "split-across-pages",
            "ranks 2-10 of Table 22 at the top of page 28, headerless; Table 22's caption and "
            "its single first row are at the foot of page 27")
    exclude(37, 1, "not-an-exhibit",
            "a body paragraph ('May be he is John Wooden, the legend on basketball court, "
            "who ...') emitted as two invisible white fill rectangles, one per text line; the "
            "detector read them as vector regions and the crop shows plain prose with no mark")
    exclude(37, 2, "not-an-exhibit",
            "the second of the same three rhetorical paragraphs ('May be he is \"Bear\" Bryant, "
            "the hero in the field of ...'), again two white per-line fill rectangles and "
            "nothing drawn")
    exclude(37, 3, "not-an-exhibit",
            "the third rhetorical paragraph ('May be she is Pat Summitt, the most successful "
            "woman basketball coach, ...'), same invisible text-frame patches, no exhibit")
    exclude(37, 4, "fragment-of-other",
            "the middle photograph of the three-panel strip, x 247-395, 'Bear' Bryant in his "
            "hounds-tooth fedora; the strip prints no number and no caption, so it is counted "
            "once on the leftmost panel")
    exclude(37, 5, "fragment-of-other",
            "the right-hand photograph of the strip, x 395-489, Pat Summitt; same captionless "
            "strip as the leftmost panel, so it is not a separate row")

    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": ITEMS,
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": [
            "Every table in the paper is the same full-ruled grid: an outer box on all four "
            "sides plus a rule between every row and a vertical separator between every pair "
            "of columns. Not one grid is booktabs, none is rule-free, and the two unnumbered "
            "notation grids are boxed exactly like the numbered ones [table.rule_style]",
            "Captions print ABOVE their grids in all twenty-five numbered tables, and every "
            "one of them sits flush against the table's top rule, so the measured crop "
            "clips the caption's upper half [caption.position]",
            "The layer's caption strings are erratic in a way the page is not: some print "
            "'Table 2.Interrelationship' with no space after the period, some 'Table 11.' with "
            "no title at all, and one welds into 'Table 147.' where the page reads 'Table 14.' "
            "- all quoted as the layer prints them [caption.numbering]",
            "The three charts are one construction repeated: an Excel line chart exported as "
            "a bitmap inside a thin vector frame, in-art title, horizontal gridlines only, a "
            "single series and a legend placed BELOW the plot area. Nothing in the paper is a "
            "bar, scatter, pie or 3-D chart [geometry.family]",
            "The paper's charts carry no data labels - the reader gets five era categories and "
            "a tick scale and must read heights off the line [geometry.data_labels]",
            "Twelve of the twenty-seven grids are split across a page break and NONE of the "
            "continuations reprints its header row, so five tails are headerless columns of "
            "numbers whose meaning survives only from the previous page [table.continued]",
            "Shading is semantic, never decorative: Tables 5 and 16 shade exactly the top "
            "five coaches and say so in a table footnote, Table 19 is the only truly "
            "alternating zebra, and Table 17's five shaded rows have no key and no pattern "
            "[table.zebra]",
            "Two grids print a blank stub-column header cell - Table 2 over the factor names "
            "and Table 18 over the adjusted factors - and neither indents its stub, which is "
            "why the blank cell reads as a missing label [table.header_rows]",
            "Eight of the twenty-five tables are never cited by number: 4, 5, 8, 9, 10, 18, "
            "and both unnumbered notation grids, which have no number to cite [mention.count]",
            "The two tables that share one pointing sentence are cited only together - 'The "
            "factors and explanations are shown in Table 6.1 and Table 6.2' and 'The top 5 of "
            "both sports are shown in Table 7.1 and Table 7.2 respectively' - so each of those "
            "four rows carries the joint sentence [mention.style]",
            "Three of the four picture rows are cited on the page BEFORE the art: page 17's "
            "'Figure 1 shows the means of winning percentages in all groups' and its two "
            "siblings describe charts that print on page 18, so lead_pages is +1 rather than "
            "negative [mention.lead_pages]",
            "The appendix strip is the only exhibit with no number and no caption, and it is "
            "three photographs rather than a drawing or a chart [geometry.panel_count]",
            "Twenty-two pages carry measured regions and the other sixteen are pure prose: "
            "the paper has no landscape tables, no figures inside the numbered sections other "
            "than the three timeline charts, and no exhibit printed sideways [table.orientation]",
        ],
        "note": (
            "Family tally: table-grid 27, line 3, composite-panel 1. There is no bar, "
            "scatter, map or schematic anywhere - this is a ranking paper whose exhibits are "
            "almost entirely numeric grids. Coverage: 27 table rows + 4 figure rows + 17 "
            "refusals = 48 measured regions. DECLARED PARTIAL: Table 10's fifth row (Ned "
            "Harkness) sits at the top of page 17, where the detector counted 23 vector paths "
            "but produced no region, so the table is recorded with its printed five rows and "
            "four of them fall inside the measured box. Also declared rather than repaired: "
            "three pages of body prose (p3, p37) and one display formula (p7) are measured as "
            "vector regions because this document's producer emits an invisible white fill "
            "rectangle behind every text line; all four are refused as not-an-exhibit. The "
            "paper prints twenty-five numbered tables and two unnumbered notation grids, and "
            "all twenty-seven are measured."
        ),
    }
    out = PROXY / "pc59-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    sys.exit(main())
