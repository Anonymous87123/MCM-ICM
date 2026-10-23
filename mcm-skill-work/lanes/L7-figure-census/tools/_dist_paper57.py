"""Hand pass for P-B-2014-26160-510e6a16 (a 2014 B paper that ranks the all-time best
college coaches of basketball, field hockey and football with an AHP weight model, a
Grey Correlation model and a Fuzzy Comprehensive model), 36 PDF pages.

Fifty-seven measured regions over twenty-nine pages. Every one of them is accounted
for: thirty-two printed tables, fourteen figures, and eleven regions refused.

    page  region  what it is
    1     r1      final rank table inside the abstract, uncaptioned, unnumbered
    4     r1      symbols table (Symbol / Explanation), uncaptioned
    5     r1      Figure 1, the solution flow diagram
    7     r1      Figure 2, the criterion hierarchy diagram
    7     r2-r3   Table 1, Table 2 (pairwise comparison matrices)
    8     r1-r3   Table 3, Table 4, Table 5
    9     r1      Table 6 (seven criteria, star ratings)
    10    r1-r2   two uncaptioned top-5 rank tables (Grey and Fuzzy)
    12    r1-r2   one Table 7 split into header band (r1) and body (r2)
    14    r1-r3   Table 8, Figure 3, and the bitmap plot body of Figure 3
    15    r1-r4   Table 9, Figure 4, plot body, Table 10
    16    r1-r2   Figure 5 and its plot body
    17    r1      comment set (Level / Score over five star levels), uncaptioned
    18    r1      Table 11 (weight vector, merged first column)
    19    r1-r4   Table 12 header band, Table 12 body, Figure 6, plot body
    20    r1-r2   Table 13, Table 14
    21    r1-r5   Figure 7, body, Table 15, Figure 8, body
    22    r1-r2   Table 15 again (ranks comparison), Figure 9
    24    r1-r2   Figure 10, Figure 11
    25    r1      Figure 12
    26    r1-r2   Figure 13 and its plot body
    27    r1      final rank table of section 9.1, uncaptioned
    28    r1-r2   the illustrated Honor Roll poster, and one clip-art icon inside it
    30    r1      the same final rank table again, inside the letter
    31    r1      the reference list, not an exhibit
    32-36 r1-r2  the six appendix data and score tables

Usage: python -I tools/_dist_paper57.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2014-26160-510e6a16"
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

SUMMARY = "Summary"
LETTER = "A Letter to Sports Illustrated"
APPENDIX = "Appendix"
SYMBOLS = "3 Symbols Definition"
OVERVIEW = "4 Model Overview"
AHP = "5 AHP Model"
HIER = "5.1 Establish a Hierarchical Model"
CMPMAT = "5.2 Structure Comparison Matrix"
WEIGHTS = "5.2.1 Weights of Evaluation Criterion"
SELECT = "5.2.2 Select Evaluation Criterion"
ADV = "6 Advanced Model"
METHODS = "6.1 Overview of Evaluation Methods"
GREY = "6.2 Grey Correlation Model"
DATAPROC = "6.2.1 Data Processing"
GREYRES = "6.2.3 Results of Grey Correlation Model"
FUZZY = "6.3 Fuzzy Comprehensive Evaluation Model"
FUZZYINTRO = "6.3.1 Introduction of Fuzzy Comprehensive Algorithm"
COMMENT = "3 Determining the comment set"
BWEIGHTS = "5 Getting weights according to AHP"
FUZZYCALC = "6.3.2 Concrete Calculation"
REVIEW = "6.4 Results Review"
TIMELINE = "7 Is Time Line Horizon Influential?"
SENS = "8 Sensitivity Analysis"
SENSGREY = "8.1 Sensitivity of Grey Correlation Method"
SENSFUZZY = "8.2 Sensitivity of Fuzzy Comprehensive Method"
DISCUSS = "9 Discussion and Conclusion"
SOLUTIONS = "9.1 Solutions to All Problems"
HONOR = "9.2 Honor Roll"

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def place(page: int, reg: int, path: list[str], kind: str, *, numbered: bool = True) -> dict:
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


def deictic(page: int, sentence: str) -> dict:
    """A pointer that names no exhibit number, so it is not a named citation."""
    return {"first_page": page, "lead_pages": 0, "style": [], "count": 0,
            "lead_sentence": sentence, "trail_sentence": "", "lead_pattern": "direct",
            "read_sentences": 1, "gap_sentences": None}


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
           path: list[str], kind: str, *, numbered: bool = True, panels: int = 1,
           layout: str = "1", legend: str = "none", three_d: str = "no",
           printed: bool = True, labels: bool = False, note: str = "") -> None:
    word = q(cap, page) if cap else ""
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": word,
        "caption_source": "text-layer" if word else "none",
        "note": note,
        "place": place(page, reg, path, kind, numbered=numbered),
        "mention": mention,
        "caption": caption(word, numbering if word else "none", "below"),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    })


def table(page: int, reg: int, rows: int, cols: int, cap: str, numbering: str,
          mention: dict, path: list[str], kind: str, *, header_rows: int = 1,
          rules: str = "booktabs", zebra: bool = False, merged: bool = False,
          num: int = 0, txt: int = 0, decimal: bool = False, continued: bool = False,
          numbered: bool = True, note_sentence: str = "", note: str = "") -> None:
    word = q(cap, page) if cap else ""
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": word,
        "caption_source": "text-layer" if word else "none",
        "note": note,
        "place": place(page, reg, path, kind, numbered=numbered),
        "mention": mention,
        "caption": caption(word, numbering if word else "none", "above"),
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
            "continued": continued,
            "note_sentence": note_sentence,
        },
    })


def exclude(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "region": reg, "bbox": REG[(page, reg)],
                     "reason": reason, "note": note})


def header_band(page: int, reg: int, which: str, owner: list[float]) -> None:
    exclude(page, reg, "fragment-of-other",
            f"the header band of {which} at y {REG[(page, reg)][1]:.0f}-{REG[(page, reg)][3]:.0f}; "
            f"the table is counted once, on the body region at y {owner[1]:.0f}-{owner[3]:.0f}")


def plot_body(page: int, reg: int, which: str) -> None:
    exclude(page, reg, "fragment-of-other",
            f"the bitmap plot body of {which} - the bars and gridlines as a pasted raster - "
            "sitting inside the vector region that carries the title and the axis labels of "
            "the same chart; one chart, one row")


def build() -> str:
    # ---- page 1: the final rank table inside the abstract ----------------------
    table(1, 1, 6, 4, "", "none",
          deictic(1, q("The final rank table is as follows:", 1)),
          [f"未编号标题 {SUMMARY}"], "abstract", num=1, txt=3, numbered=False,
          note="Header Rank / Basketball / Field hockey / Football over five rows, one per "
               "ranked coach, booktabs rules with no shading. No caption and no table "
               "number; the only lead-in is the abstract sentence quoted in the mention "
               "block. It prints the same five-name ranking that p10, p27 and p30 print "
               "again [caption.numbering].")

    # ---- page 4: the symbols table --------------------------------------------
    table(4, 1, 8, 2, "", "none", none_mention(),
          [SYMBOLS], "symbols", num=0, txt=2,
          note="Symbol / Explanation over seven data rows - A, B, C, Z, R, D, T - the symbol "
               "cells set in italic math. Sits directly under the heading '3 Symbols "
               "Definition' and carries no caption or table number of its own "
               "[caption.verbatim].")

    # ---- page 5: Figure 1 ----------------------------------------------------
    figure(5, 1, "flowchart-or-schematic",
           "Figure 1. Flow diagram of solution", "Figure N.",
           cited(5, 5, ["Figure 1"], 1,
                 q("The process of developing models is shown in Figure 1.", 5)),
           [OVERVIEW], "model",
           legend="inside",
           note="Single-page process flow in shadowed stencil shapes with a built-in shape "
                "key box at the lower left - the key is part of the artwork, which is why "
                "the legend reads inside rather than none. The flow forks after the model "
                "steps into a 'Not considering time' branch that ends in Rank 1 (Grey "
                "Correlation) and Rank 2 (Fuzzy Evaluation) and a 'Considering time' branch "
                "that ends in Final rank, and a dashed connector feeds the final rank back "
                "to the data step [geometry.legend].")

    # ---- page 7: Figure 2, Table 1, Table 2 ----------------------------------
    figure(7, 1, "flowchart-or-schematic", "Figure 2. Hierarchy figure", "Figure N.",
           cited(7, 7, ["Figure 2"], 2,
                 q("which affect evaluation significantly, hierarchy figure is shown in "
                   "Figure 2.", 7),
                 q("In Figure 2, C-Time represents Coaching Time.", 7), read=2),
           [AHP, HIER], "model",
           printed=False,
           note="The AHP criterion tree drawn as boxed labels joined by plain connectors: "
                "'Comprehensive impact' over three second-level boxes - Personal qualities, "
                "Team achievements, Training qualities - over nine leaf boxes, Gender and "
                "C-Time under personal quality, Wins, Losses, W-L and Perfomance under team "
                "achievements, OC, MC and RCC under training quality. Draws no numbers, no "
                "scale and no legend; the abbreviations are spelled out in the sentence "
                "that follows it [geometry.printed_numbers].")

    table(7, 2, 4, 5, "Table 1. Pairwise comparison matrix of hierarchyⅠ-Ⅱ", "Table N.",
          cited(7, 7, ["Table 1"], 1,
                q("Then, we get the weights of personal quality, training quality and team "
                  "achievements as is shown in Table 1.", 7)),
          [AHP, CMPMAT, WEIGHTS], "evaluation", num=4, txt=1,
          note="A three-by-three AHP comparison matrix - Comprehensive impact against "
               "Personal quality, Training quality and Team achievements - with a Weight "
               "column of four decimals (0.2496, 0.1565, 0.5938). Fractions print as "
               "'1/5', '1/3', '1/8' inside the cells [table.numeric_cols].")

    table(7, 3, 3, 4, "Table 2. Pairwise comparison matrix of hierarchyⅡ-Ⅲ", "Table N.",
          none_mention(), [AHP, CMPMAT, WEIGHTS], "evaluation", num=3, txt=1,
          note="The two-by-two personal-quality matrix, Coaching time against Gender, weights "
               "0.5498 and 0.4502. Uncited: the paragraph under Table 1 introduces the next "
               "step and then reads the maximum eigenvalue straight off this grid without "
               "naming it [mention.count].")

    # ---- page 8: Table 3, Table 4, Table 5 -----------------------------------
    table(8, 1, 4, 5, "Table 3. Pairwise comparison matrix of hierarchyⅡ-Ⅲ", "Table N.",
          none_mention(), [AHP, CMPMAT, WEIGHTS], "evaluation", num=4, txt=1,
          note="The three-by-three training-quality matrix - Organizational, Management and "
               "Race command capability - weights 0.2473, 0.2024, 0.5503. Uncited, and it "
               "carries the SAME caption text as Table 2 above it, so the two grids differ "
               "only by number [caption.verbatim].")

    table(8, 2, 5, 6, "Table 4. Pairwise comparison matrix of hierarchyⅡ-Ⅲ", "Table N.",
          none_mention(), [AHP, CMPMAT, WEIGHTS], "evaluation", num=5, txt=1,
          note="The four-by-four team-achievements matrix. Its caption prints above but the "
               "measured region covers only the header band at the top of the grid: the four "
               "data rows (C6, Losses, Win-loss percentage, Performance in league matches) "
               "carry no interior rules, so the region detector saw the top rules and stopped "
               "[table.rows]. Yet a third grid with this same caption text [caption.verbatim].")

    table(8, 3, 10, 2, "Table 5. Criterion’s weights to overall objects", "Table N.",
          cited(8, 8, ["Table 5"], 2,
                q("Combination Weight Vector of criterion with respect to evaluation method "
                  "of college coaches is shown in Table 5.", 8),
                q("According to importance of every criteria shown in Table 5, we choose "
                  "several main criterion and decide the final evaluation method.", 9)),
          [AHP, CMPMAT, WEIGHTS], "evaluation", num=1, txt=1,
          note="Nine criteria against their combination weights, 0.1373 down to 0.0317, the "
               "only two-column table in the AHP block. It is the one table in section 5.2 "
               "that the prose reads twice, once as its result and once a page later when the "
               "seven surviving criteria are selected [mention.count].")

    # ---- page 9: Table 6 -----------------------------------------------------
    table(9, 1, 8, 3, "Table 6. Final seven criterion to evaluate college coaches", "Table N.",
          cited(9, 9, ["Table 6"], 1, q("The final seven criterion are shown in Table 6.", 9)),
          [AHP, SELECT], "evaluation", num=1, txt=2,
          note="Criterion / Symbol / Weight over seven rows. The Symbol column prints C1 to C7 "
               "and the Weight column is not a number at all but a five-point star rating - "
               "five filled stars for Win-loss percentage down to one for Losses - so the "
               "table's third column is a rating mark, not a value [table.numeric_cols].")

    # ---- page 10: two uncaptioned rank tables --------------------------------
    table(10, 1, 6, 4, "", "none",
          deictic(10, q("Top 5 coaches in basketball, field hockey and football are "
                        "represented as:", 10)),
          [ADV, METHODS], "evaluation", num=1, txt=3,
          note="The Grey Correlation top-5 ranking, Rank over Basketball / Field hockey / "
               "Football, uncaptioned and unnumbered. It repeats the p1 abstract table "
               "verbatim, which is why the same three blocks of five names appear four times "
               "in the paper [caption.numbering].")
    table(10, 2, 6, 4, "", "none",
          deictic(10, q("Top 5 coaches in basketball, field hockey and football are "
                        "represented as:", 10)),
          [ADV, METHODS], "evaluation", num=1, txt=3,
          note="The Fuzzy Comprehensive top-5 ranking on the same page, introduced by the SAME "
               "sentence as the table above it and differing from it in football and in "
               "positions 1-5 - Bobby Bowden first here, Joe Paterno first there. Two models, "
               "two rank tables, one lead-in sentence [mention.lead_sentence].")

    # ---- page 12: Table 7 ---------------------------------------------------
    table(12, 2, 11, 8, "Table 7. Standardization of basketball college coaches", "Table N.",
          none_mention(), [GREY, DATAPROC], "model", num=7, txt=1, zebra=True, decimal=True,
          note="Ten basketball coaches over seven normalised criteria, values in fixed three "
               "decimals and aligned on the point. Measured as two bands - the header plus the "
               "first row in this grid's upper strip and the nine remaining rows below it - but "
               "one table: the shading alternates straight through the seam with no second "
               "bottom rule. Uncited; the prose says only 'we get the normalized value' "
               "[table.decimal_aligned].")
    header_band(12, 1, "Table 7", REG[(12, 2)])

    # ---- page 14: Table 8, Figure 3 ----------------------------------------
    table(14, 1, 16, 4, "Table 8. Scores of top 15 basketball coaches (Grey Correlation Model)",
          "Table N.",
          cited(13, 14, ["Table 8"], 1, q("The results are shown in Table 8.", 13)),
          [GREY, GREYRES], "model", num=2, txt=2, zebra=True,
          note="Rank / Coach / Last School / Scores over the fifteen coaches, scored 0.834 "
               "down to 0.462 in pale-blue zebra rows. Like Table 4, only the header band was "
               "measured - the rest of the grid carries no interior rules - so the region is "
               "the strip at its top [table.rows].")
    figure(14, 2, "bar", "Figure 3. Scores of top 15 basketball coaches", "Figure N.",
           cited(14, 14, ["Figure 3"], 1,
                 q("we draw Figure 3. as follows by the data from Table 8.", 14)),
           [GREY, GREYRES], "model",
           three_d="perspective-bars",
           note="One series of fifteen perspective bars in descending score order, the "
                "in-artwork title 'Scores of top 15 basketball coaches' over a y axis titled "
                "Scores running 0 to 0.9 and rotated coach names on x; horizontal gridlines "
                "only, no legend and no data labels. The same chart is rendered three times in "
                "the paper - Excel 3D here and on the next two plates, then again in flat 2D "
                "style on p19 [geometry.three_d]. The lead sentence quoted in the mention "
                "block reads the figure and not the caption.")
    plot_body(14, 3, "Figure 3")

    # ---- page 15: Table 9, Figure 4, Table 10 -------------------------------
    table(15, 1, 3, 6, "Table 9. Scores of top 5 field hockey coaches", "Table N.",
          cited(14, 15, ["Table 9"], 1,
                q("We can get score of top 5 field hockey coaches in Grey Correlation "
                  "Method, which is shown in Table 9.", 14)),
          [GREY, GREYRES], "model", num=5, txt=1,
          note="A transposed five-coach table: the coach names Jan Trapp, Pat Rudy, Jan "
               "Hutchinson, Nancy Stevens and Sharon Pfluger print as the header row and only "
               "Scores (0.847 down to 0.663) and Rank (1 to 5) print as rows, so the grid is "
               "three rows deep and the header is the widest thing on it [table.rows].")
    figure(15, 2, "bar", "Figure 4. Scores of top 15 field hockey coaches", "Figure N.",
           cited(15, 15, ["Figure 4"], 1,
                 q("we draw Figure 4. as follows by the data from Table 9.", 15)),
           [GREY, GREYRES], "model",
           three_d="perspective-bars",
           note="The field hockey twin of Figure 3: fifteen perspective bars, y Scores 0 to "
                "0.9, rotated coach names, horizontal gridlines, no legend, no labels. Its "
                "caption promises the top 15 while the prose above it only four sentences "
                "earlier talks about the top 5 and Table 9 lists just five coaches "
                "[caption.verbatim].")
    plot_body(15, 3, "Figure 4")
    table(15, 4, 3, 6, "Table 10. Scores of top 5 football coaches", "Table N.",
          cited(15, 15, ["Table 10"], 1,
                q("We can get scores of top 5 football college coaches in the same method, "
                  "which is shown in Table 10.", 15)),
          [GREY, GREYRES], "model", num=5, txt=1,
          note="The football twin of Table 9 on the same page: five coach names as the header "
               "row, Scores 0.834 down to 0.513 and Rank 1 to 5 as the only two data rows, "
               "transposed the same way [table.rows].")

    # ---- page 16: Figure 5 -------------------------------------------------
    figure(16, 1, "bar", "Figure 5. Scores of top 15 football coaches", "Figure N.",
           cited(15, 16, ["Figure 5"], 1,
                 q("we draw Figure 5. as follows by the data from Table 10.", 15)),
           [GREY, GREYRES], "model",
           three_d="perspective-bars",
           note="The third and last of the Grey Correlation bar plates, football, same "
                "construction: fifteen perspective bars, y Scores 0 to 0.9, horizontal "
                "gridlines only, no legend and no labels. It is the only one of the three "
                "whose plate is a page of its own, with nothing above the chart but the "
                "running head [place.solo_page].")
    plot_body(16, 2, "Figure 5")

    # ---- page 17: comment set ----------------------------------------------
    table(17, 1, 2, 6, "", "none",
          deictic(17, q("In this problem, we define the comment set as follows:", 17)),
          [FUZZY, FUZZYINTRO, COMMENT], "other", num=5, txt=1,
          note="The five-level comment set printed transposed: the two row labels are Level "
               "and Score and the five columns are the levels, five filled stars down to one. "
               "It prints NO header row at all, so `header_rows` is recorded as 1 with this "
               "note standing in for it, and the ledger's floor of one is the only reason the "
               "field is not zero [table.header_rows].")

    # ---- page 18: Table 11 -------------------------------------------------
    table(18, 1, 8, 9, "Table 11. Weight vector of this model", "Table N.",
          none_mention(), [FUZZY, FUZZYINTRO, BWEIGHTS], "other",
          num=7, txt=2, merged=True,
          note="The largest table in the body: first-level criterion, its weight B_i, "
               "second-level criterion, its B_ij and five membership columns d1 to d5. The "
               "first-level cells merge down - Personal quality over two rows, Training "
               "quality over one, Team achievements over four - with the B_i column merged to "
               "match, and a row of star markers prints inside the header above the d columns. "
               "The only table in the paper with merged cells [table.merged_cells].")

    # ---- page 19: Table 12, Figure 6 ---------------------------------------
    table(19, 2, 21, 8, "Table 12. Scores of top 15 basketball coaches’ quality", "Table N.",
          none_mention(), [FUZZY, FUZZYCALC], "solution", num=7, txt=1, zebra=True,
          note="Twenty coach rows of integer quality scores 1 to 5 across CT, Gender, RCC, "
               "Wins, Lose, W-L% and FF in pale-blue zebra, plus two unruled legend lines "
               "below the bottom rule. The caption promises the top 15 and the grid prints 20 "
               "coaches - the paper's own text says 'we choose top 15' two sentences earlier "
               "[table.rows].")
    header_band(19, 1, "Table 12", REG[(19, 2)])
    figure(19, 3, "bar", "Figure 6. Scores of top 15 basketball coaches", "Figure N.",
           cited(19, 19, ["Figure 6"], 1,
                 q("From the figure we can find the top 5 basketball college coaches are "
                   "Harry Statham, Herb Magee, Danny Miles , Adolph Rupp, Mike Krzyzewski.",
                   19)),
           [FUZZY, FUZZYCALC], "solution",
           three_d="perspective-bars",
           note="The fuzzy-model plate: fifteen perspective bars on an INTEGER axis 0 to 5, "
                "one unit per tick, not the 0-to-0.9 score axis of the Grey plates. The "
                "caption says basketball and the in-artwork title says 'Scores of top 15 field "
                "hockey coaches', and the three coaches that gatecrash the top of the order - "
                "Enza Steele, Sally Scatton, Brenda Meese - are field-hockey names, so the "
                "artwork contradicts the caption [caption.verbatim].")
    plot_body(19, 4, "Figure 6")

    # ---- page 20: Table 13, Table 14 ---------------------------------------
    table(20, 1, 16, 4, "Table 13. Scores and rank of top 15 basketball coaches (Fuzzy "
                        "Comprehensive Evaluation Model)", "Table N.",
          cited(20, 20, ["Table 13"], 1,
                q("Finally, we get final grades and ranks by fuzzy calculation of Fuzzy "
                  "Decision Matrix (R) and Weight Matrix (B), which is shown in Table 13.", 20)),
          [FUZZY, FUZZYCALC], "solution", num=2, txt=2, zebra=True,
          note="Ranking / Coach / Last School / Score over the fifteen basketball coaches, "
               "scores 4.1557 down to 2.6944 in pale-blue zebra, the complete grid rather than "
               "a top band. Its caption runs to two lines once the model name is counted "
               "[caption.words].")
    table(20, 2, 3, 6, "Table 14. Scores and rank of top 5 field hockey college coaches",
          "Table N.",
          cited(20, 20, ["Table 14"], 1, q("Top 5 of them are listed in Table 14.", 20)),
          [FUZZY, FUZZYCALC], "solution", num=5, txt=1,
          note="Transposed like Table 9: five coach names as the header row - two of them "
               "wrapping onto two lines - with Scores 4.22 to 3.60 and Rank 1 to 5 as the only "
               "data rows [table.rows].")

    # ---- page 21: Figure 7, Table 15, Figure 8 ------------------------------
    figure(21, 1, "bar", "Figure 7. Scores of top 15 field hockey college coaches", "Figure N.",
           cited(20, 21, ["Figure 7"], 1,
                 q("From the figure we know that top 5 field hockey coaches are Jan "
                   "Hutchinson, Jan Trapp, Nancy Stevens, Pat Rudy, Beth Anders.", 20)),
           [FUZZY, FUZZYCALC], "solution",
           three_d="perspective-bars",
           note="Fifteen perspective bars against y Scores 0 to 5.000 by 0.500, horizontal "
                "gridlines only. The in-artwork title reads 'Scores of top 15 football "
                "coaches' while the caption and the prose both call it field hockey, so the "
                "artwork on this plate is a second-hand copy of the plate below it "
                "[caption.verbatim].")
    plot_body(21, 2, "Figure 7")
    table(21, 3, 3, 6, "Table 15. Scores and rank of top 5 football college coaches", "Table N.",
          cited(21, 21, ["Table 15"], 1, q("Top 5 of them are listed in Table 15.", 21)),
          [FUZZY, FUZZYCALC], "solution", num=5, txt=1,
          note="Transposed five-coach table for football, Scores 4.805 down to 3.407 and Rank "
               "1 to 5, the third of the three identical three-row grids [table.rows].")
    figure(21, 4, "bar", "Figure 8. Scores of top 15 football college coaches", "Figure N.",
           cited(21, 21, ["Figure 8"], 1,
                 q("From the figure we know that top 5 football coaches are Bobby Bowden, Joe "
                   "Paterno, Bear Bryant, Tom Osborne, Pop Warner.", 21)),
           [FUZZY, FUZZYCALC], "solution",
           three_d="perspective-bars",
           note="The second chart on the same page and a near-duplicate of Figure 7: same "
                "fifteen names in the same descending order, but the y axis is titled 'Score' "
                "in the singular and its ticks step by 1.000 from 0 to 5.000 instead of by "
                "0.500 - two separately exported copies of one chart on one page "
                "[geometry.printed_numbers].")
    plot_body(21, 5, "Figure 8")

    # ---- page 22: Table 15 again, Figure 9 --------------------------------
    table(22, 1, 11, 4, "Table 15. Ranks comparison", "Table N.",
          cited(22, 22, ["Table 15"], 1,
                q("Grey Correlation rank, Fuzzy Comprehensive rank and Current rank are "
                  "listed in Table 15.", 22)),
          [ADV, REVIEW], "test", num=3, txt=1, zebra=True,
          note="THE SECOND TABLE NUMBERED 15: ten coaches against three ranks - Grey "
               "Correlation, Fuzzy Comprehensive and Current - in pale-blue zebra. The paper "
               "therefore prints two different tables both labelled Table 15, six pages apart: "
               "this one and the football top-5 grid on p21 [caption.numbering].")
    figure(22, 2, "line", "Figure 9. Two models’ rank comparison", "Figure N.",
           cited(22, 22, ["Figure 9"], 2,
                 q("To show the difference apparently, we draw the figure of three ranks, "
                   "which is shown in Figure 9.", 22),
                 q("Comparing normalized scores with former scores, the difference between "
                   "ranks considering coaching start time or not is shown in Figure 9.", 23)),
           [ADV, REVIEW], "test", legend="outside-right",
           note="Three line series with markers - Fuzzy Rank in blue diamonds, Grey Rank in "
                "orange squares, Current Rank in grey triangles - over the ten basketball "
                "coaches, keyed outside the frame at the right, y Ranks 0 to 14, x titled "
                "Basketball Coaches, title drawn inside the plot. THE p23 RE-READ IS A "
                "MISNUMBER: the sentence about the effect of coaching start time belongs to "
                "Figure 10 but cites Figure 9 [mention.trail_sentence].")

    # ---- page 24: Figure 10, Figure 11 ------------------------------------
    figure(24, 1, "bar", "Figure 10. Comparison between ranks considering coaching start time "
                         "or not of basketball", "Figure N.",
           cited(24, 24, ["Figure 10"], 1,
                 q("In Figure 10. the horizontal coordinate represents rank that has not "
                   "considered coaching start time.", 24)),
           [TIMELINE], "other",
           note="Flat MATLAB-style column chart, NOT the Excel 3D bar of the earlier plates: "
                "rank differences against rank, single series of blue bars about a zero "
                "baseline running from about -4 to +7, boxed axes with tick marks on all four "
                "sides, no gridlines, no legend, and one dashed orange annotation box with an "
                "arrow labelled 'Rank difference is very little for top coaches'. Its x axis "
                "is unlabelled on the plate and the number the prose quotes is a rank, not a "
                "coach [geometry.family].")
    figure(24, 2, "bar", "Figure 11. Comparison between ranks considering coaching start time "
                         "or not of football", "Figure N.",
           cited(24, 24, ["Figure 11"], 1,
                 q("To examine above conclusion, we use football coaches’ data to verify the "
                   "results, which are shown in Figure 11.", 24)),
           [TIMELINE], "other",
           note="The football check of Figure 10, same construction: flat single-series "
                "columns about a zero baseline, boxed axes, no gridlines, no legend, with a "
                "dashed annotation box labelled 'Rank difference is little for top 10'. The "
                "two plates are the paper's only flat 2D bars [geometry.family].")

    # ---- page 25: Figure 12 ----------------------------------------------
    figure(25, 1, "line", "Figure 12. The effect of resolution ratio on evaluating results",
           "Figure N.",
           cited(25, 25, ["Figure 12"], 1,
                 q("After being processed by computer, ranks of top 10 coaches are shown in "
                   "Figure 12.", 25)),
           [SENS, SENSGREY], "sensitivity", legend="inside",
           note="Five line series with markers, one per resolution ratio from beta=0.1 to "
                "beta=0.9, over the ten coaches labelled A B C D F G E H I J - the missing E "
                "in position five is the paper's own ordering, not a reading error. Legend "
                "inside the frame at the upper right, y titled Z(i) running 0.500 to 0.850, x "
                "titled Coaches, title drawn inside the artwork. Each legend entry also prints "
                "the rank order that ratio produces [geometry.legend].")

    # ---- page 26: Figure 13 ----------------------------------------------
    figure(26, 1, "bar", "Figure 13. The score in different weight", "Figure N.",
           cited(26, 26, ["Figure 13"], 1, q("The results are showing in Figure 13.", 26)),
           [SENS, SENSFUZZY], "sensitivity", legend="outside-right",
           three_d="perspective-bars",
           note="Three grouped perspective bars per coach - Maximum weight increased 0.02, "
                "Maximum weight decreased 0.02 and initial score - over the top ten basketball "
                "coaches, keyed outside the right with the 0.02 split onto a second line. y "
                "runs 2.5 to 4.5, title drawn inside the artwork, no data labels: the bars are "
                "within a tenth of each other, which is the stability claim the prose makes "
                "[geometry.legend].")
    plot_body(26, 2, "Figure 13")

    # ---- page 27: final rank table ---------------------------------------
    table(27, 1, 6, 4, "", "none",
          deictic(27, q("Besides, considering time line horizon, we provide the final general "
                        "ranks, which are shown as follows:", 27)),
          [DISCUSS, SOLUTIONS], "solution", num=1, txt=3,
          note="The paper's answer, uncaptioned and unnumbered: Rank over Basketball / Field "
               "hockey / Football with the same five names the abstract prints. Third of the "
               "four identical copies of this table [caption.numbering].")

    # ---- page 28: the Honor Roll poster ----------------------------------
    figure(28, 1, "composite-panel", "", "none",
           none_mention(), [DISCUSS, HONOR], "other", panels=3, layout="column of 3",
           note="A decorative full-page poster rather than a typeset figure: an olive border, "
                "a gold medal ribbon and three sport clip-art icons around the words 'Honor "
                "Roll', with THREE separate ranked tables stacked down the page - basketball, "
                "football and field hockey, each Rank / Coach / Teams over five rows. Nothing "
                "in the artwork names a number, and the three tables are inside one raster, so "
                "the plate is one composite of three panels and not three tableau rows "
                "[geometry.panel_count]. It is also the only page in the paper whose exhibits "
                "were drawn as an image rather than typeset.")
    exclude(28, 2, "in-body-diagram",
            "the 82-point square clip-art of a football player that sits between the first two "
            "honor-roll tables - one of the three sport icons decorating the poster, not an "
            "exhibit")

    # ---- page 30: the letter's rank table --------------------------------
    table(30, 1, 6, 4, "", "none",
          deictic(30, q("Therefore, the ranking from grey model is as follows.", 30)),
          [f"未编号标题 {LETTER}"], "other", num=1, txt=3, numbered=False,
          note="The rank table printed inside the letter to Sports Illustrated, uncaptioned "
               "and unnumbered and identical in content to the p27 table - the fourth and last "
               "copy of the same five-name ranking [caption.numbering].")

    # ---- page 31: the reference list -------------------------------------
    exclude(31, 1, "not-an-exhibit",
            "the tail of the reference list - entries [1] to [18] in hanging-indent two-column "
            "prose, ending in bare URLs. Text, not a table or a figure")

    # ---- pages 32-36: the appendix ---------------------------------------
    table(32, 1, 38, 9, "1. Original data of college basketball coaches", "none",
          none_mention(), [f"未编号标题 {APPENDIX}"], "appendix", num=7, txt=2, numbered=False,
          note="The basketball raw data, 37 coach rows of coaching time, gender, RCC, wins, "
               "losses, win-loss percentage and final-four appearances, running to the bottom "
               "of the page and continuing on p33 where the header row is printed again. Its "
               "only title is the appendix list item above it, so it carries no table number "
               "[table.continued].")
    table(33, 1, 10, 9, "", "none", none_mention(),
          [f"未编号标题 {APPENDIX}"], "appendix", num=7, txt=2, numbered=False, continued=True,
          note="Basketball raw data continued: the header row repeats and nine more coaches "
               "run down to Teresa Lawrence, who is the only woman in the grid and the only row "
               "whose gender cell reads 3 [table.continued].")
    table(33, 2, 29, 7, "2. Original data of college field hockey coaches", "none",
          none_mention(), [f"未编号标题 {APPENDIX}"], "appendix", num=5, txt=2, numbered=False,
          note="Field hockey raw data, 28 coach rows of coaching time, wins, losses, win-loss "
               "percentage and ties, starting mid-page after the basketball grid closes and "
               "continuing onto p34 [table.rows].")
    table(34, 1, 13, 7, "", "none", none_mention(),
          [f"未编号标题 {APPENDIX}"], "appendix", num=5, txt=2, numbered=False, continued=True,
          note="Field hockey raw data continued: header row repeated, twelve more coaches from "
               "Hawthorne down to Linda Arena, closing the grid [table.continued].")
    table(34, 2, 27, 8, "3. Original data of college football coaches", "none",
          none_mention(), [f"未编号标题 {APPENDIX}"], "appendix", num=6, txt=2, numbered=False,
          note="Football raw data, 26 coach rows of coaching time, R-c-c, wins, losses, "
               "win-loss percentage and performance, running past the page bottom into p35 "
               "[table.rows].")
    table(35, 1, 19, 8, "", "none", none_mention(),
          [f"未编号标题 {APPENDIX}"], "appendix", num=6, txt=2, numbered=False, continued=True,
          note="Football raw data continued: header repeated, eighteen more coaches from "
               "Jerry Claiborne to Bobby Dodd, and the grid closes two thirds down the page "
               "where a new table begins [table.continued].")
    table(35, 2, 21, 7, "4. Scores and ranks for basketball coaches of two models", "none",
          none_mention(), [f"未编号标题 {APPENDIX}"], "appendix", num=5, txt=2, numbered=False,
          note="Twenty basketball coaches with both models' scores and ranks side by side - "
               "Grey Scores, Grey Rank, Fuzzy Scores, Fuzzy Rank - the only appendix table that "
               "puts the two models in one grid [table.cols].")
    table(36, 1, 16, 7, "5. Scores and ranks for football coaches of two models", "none",
          none_mention(), [f"未编号标题 {APPENDIX}"], "appendix", num=5, txt=2, numbered=False,
          note="The football counterpart, fifteen coaches, both models' scores and ranks, "
               "starting at the top of the page [table.rows].")
    table(36, 2, 16, 6, "6. Scores and ranks for field hockey coaches of two models", "none",
          none_mention(), [f"未编号标题 {APPENDIX}"], "appendix", num=4, txt=2, numbered=False,
          note="The field hockey counterpart, fifteen coaches, starting mid-page after the "
               "football grid closes. It is the one appendix grid that drops the Last School "
               "column, which is why it is six columns wide and not seven [table.cols].")

    rules = [
        "Fifty-seven measured regions over thirty-six pages account exactly: thirty-two "
        "printed tables, fourteen figures, eleven refusals, nothing left over. The tables "
        "dominate because the paper prints four identical copies of its five-name rank table "
        "(p1, p10 twice, p27, p30) and six appendix grids of raw coach data "
        "[place.doc_order].",
        "Every table in the paper uses the same rule style: a top rule, a rule under the "
        "header and a bottom rule, with no vertical rules and no outer box anywhere - "
        "`booktabs` on all thirty-two rows. Zebra shading is used on only five of them: "
        "Table 7 on p12, Table 8 on p14, Table 12 on p19, Table 13 on p20 and the ranks "
        "comparison Table 15 on p22 [table.rule_style].",
        "The paper numbers three different criteria matrices Table 2, Table 3 and Table 4 "
        "with the SAME caption, 'Pairwise comparison matrix of hierarchyⅡ-Ⅲ', and numbers "
        "two unrelated tables Table 15 six pages apart. Captions are quoted verbatim and the "
        "duplicate numbers are called out in the row notes rather than repaired "
        "[caption.verbatim].",
        "Five tables are measured only as a header band, because a grid whose interior "
        "carries no rules cannot be separated from the text above it: Table 4 on p8, Table 8 "
        "on p14, and the header strips of Table 7 on p12 and Table 12 on p19. The row records "
        "the measured band and states in its note that the grid below it is unruled and "
        "unmeasured [table.rows].",
        "Where one printed table was measured as two regions - the p12 and p19 header strips "
        "and their bodies - the table is counted once on the larger region and the strip is "
        "refused as `fragment-of-other`; the same rule refuses the seven bitmap plot bodies "
        "that sit inside the vector regions of the Excel charts [table.rule_style].",
        "Seven of the chart plates are an Excel 3D column chart pasted as a bitmap inside a "
        "vector frame that carries the title and the axis text: Figure 3, 4, 5, 6, 7, 8 and "
        "13. Each is one chart and one row, with `three_d` perspective-bars, and the nested "
        "raster is refused rather than counted [geometry.three_d].",
        "The chart families are not uniform across the paper even where the subject repeats: "
        "the three Grey Correlation score plates are vertical bars, the two time-horizon "
        "plates on p24 are flat 2D MATLAB columns with annotation boxes, the two comparison "
        "plates on p22 and p25 are line charts, and the Honor Roll page is a decorated "
        "poster with three tables inside it [geometry.family].",
        "Two plates contradict their own captions. Figure 6 is captioned 'Scores of top 15 "
        "basketball coaches' while its artwork is titled field hockey and carries "
        "field-hockey coach names; Figure 7 is captioned field hockey while its artwork is "
        "titled football and duplicates the chart printed under it. Both are recorded as "
        "printed, with the contradiction in the note [caption.verbatim].",
        "The p23 sentence 'the difference between ranks considering coaching start time or "
        "not is shown in Figure 9' misnumbers the figure it means - the subject belongs to "
        "Figure 10 on the next page. The row records the second citation as a trailing "
        "sentence on the p22 Figure 9 row rather than inventing a citation for Figure 10 "
        "[mention.trail_sentence].",
        "Four copies of the five-name rank table (p1, p10 twice, p27, p30) print no caption "
        "and no number, as do the p4 symbols table, the p17 comment set and the three-row "
        "coach tables: their `caption_verbatim` is empty and `caption_source` is none, with "
        "the lead-in sentence recorded in the mention block instead [caption.numbering].",
        "The appendix grids carry their appendix list item as the caption - '1. Original data "
        "of college basketball coaches' and so on - with `numbering` none, because the item "
        "number is not a table number. Four of those grids continue across a page break, "
        "where the header row is reprinted: the first fragment gets the title, the "
        "continuation gets `continued` true and an empty caption [table.continued].",
        "The comment set on p17 prints two rows and five level columns with NO header row, "
        "and the schema floors `header_rows` at one, so the row records 1 and says so in its "
        "note rather than leaving the block unexplained [table.header_rows].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2014\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "B-26160-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": ITEMS,
        "tables": TABLES,
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Fifty-seven measured regions over twenty-nine of thirty-six pages, all "
            "accounted: thirty-two printed tables, fourteen figures, eleven refusals. "
            "Families: bar 9, line 2, flowchart-or-schematic 2, composite-panel 1, plus 32 "
            "table-grid. The paper is table-heavy because it prints the same five-name rank "
            "table four times and six appendix grids of raw coach data. Every table is "
            "booktabs - top rule, rule under the header, bottom rule, no verticals - and only "
            "five carry zebra shading. Seven chart plates are one Excel 3D column chart "
            "exported as a bitmap inside a vector frame, which is why seven regions are "
            "refused as plot bodies. Traps worth carrying: Tables 2, 3 and 4 share one "
            "caption text, two unrelated tables are both numbered 15, Figure 6's artwork says "
            "field hockey under a basketball caption and Figure 7 the reverse, p23 cites "
            "Figure 9 for what is Figure 10, five tables were measured only as a header band "
            "because their interiors carry no rules, and the p17 comment set prints no header "
            "row at all while the schema floors header_rows at one. Nothing is unresolved."
        ),
    }
    out = PROXY / "pc57-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
