"""Hand pass for P-B-2014-29696-84be6e3a (a 2014 B paper that ranks college coaches with a
PCA factor model, an adjusted-cosine-similarity ranking, then two optimisation passes - time
line horizon and gender - before extending the factor pool to other sports and countries and
stressing the model with noise), 44 PDF pages.

Seventy-six measured regions over thirty-four pages, all accounted for: sixteen figure rows,
seventeen tables (fifteen numbered grids plus the two unnumbered appendix blocks), forty-three
refusals. Seven numbered tables print with no measured region at all - 4, 10, 13, 14, 15, 16
and 20 - and are declared in the note rather than invented as rows.

    page    region   what it is
    1       r1       MCM summary sheet block, no exhibit
    2       r1       unnumbered execution flow chart, no caption
    2       r2       duplicate detection of the same chart
    2       r3       rotated side label, fragment of the chart
    3       r1       Figure 1, three coach photographs on podium blocks
    3       r2       r3       second panel (basketball) and its duplicate
    3       r4       r5       r6       first panel duplicate, third panel, its duplicate
    4       r1       Figure 2, the factor ladder schematic
    4       r2       r3       r4       r5       the two pictures inside it and their duplicates
    8       r1       Table 1 General assumption
    10      r1       display-formula fragment, no exhibit
    11      r1       Table 2 Result of PCA process
    12      r1       Table 3 Component Matrix - the header band only
    13      r1       Fig 1, bar chart of the three principal components
    14      r1       Fig 2, the two-vector angle illustration
    14      r2       r3       two display equations, no exhibit
    15      r1       inline V_i definition, fragment
    15      r2       caption band plus Table 4's top rule, fragment
    15      r3       Fig 3, the three-vector raster diagram
    16      r1       Fig 4, the overlapping-vector diagram
    16      r2-r5    four display equations, no exhibit
    17      r1       loose 3-path group wrapping Fig 5 and its caption, fragment
    17      r2       Fig 5, three-cluster scatter with linear boundaries
    18      r1       Table 5 Result of clustering analysis
    19      r1       Table 6 Ranking result of cosine similarity model
    20      r1       Fig 6, scatter with fitted line
    21      r1       Fig 7, the difficulty curve
    22      r1       Fig 8, the two-segment difficulty adjustment
    23      r1       Table 7 Final ranking result
    23      r2       Table 8 Camparson of the 2 ranking result
    25      r1       Table 9 Result of ANOVA
    26      r1       Fig 9, variance comparison bar chart
    27      r1       Table 11 Var. of 'win games' after adjusted
    27      r2       Fig 10, the modified variance bar chart
    28      r1       Table 12 Ranking result after gender factor adjusted
    29      r1       Fig 11, the factors pool diagram
    32      r1       Table 17 Basketball Coach Ranking - header band; r2-r5 the row portraits
    33      r1       Table 17's last portrait; r2 Table 18's header band; r3-r5 its portraits
    34      r1 r2    Table 18's last two portraits; r3 Table 19's header band; r4 r5 portraits
    35      r1       Table 19's last three rows; r2-r4 their portraits; r5 Fig 12 the US map;
                     r6 the same map again
    37      r1       Table 21 Data comparison of John Wooden
    37      r2       Fig 13, the before/after stem plot
    37      r3       Table 22 Comparison of adding noise
    38      r1       Table 22's remaining seven pairs
    41      r1       Appendix Original Data, 38 rows
    42      r1       the same block's next 22 rows; r2 Appendix Modified Data, 18 rows
    43      r1       Modified Data's next 41 rows
    44      r1       Modified Data's last row

The paper runs TWO number series: the summary sheet prints bold 'Figure 1' and 'Figure 2'
with no caption text, the body prints 'Fig 1.' to 'Fig 13', and the count works out at
sixteen exhibits for fifteen printed numbers because the page-2 flow chart is never numbered.

Usage: python -I tools/_dist_paper62.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2014-29696-84be6e3a"
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

# The heading pass is unusable here - 112 heading records and every one of them has a null
# text, while the section paths it does emit are rows of racing results ('8 Bill Self M',
# '10 John Thompson Billy Donovan', '12 Different Factors'). The paper itself is cleanly
# numbered, and all forty printed labels below are present verbatim in the text layer, so
# every path is the printed heading with section_numbered true.
SUMMARY = "未编号标题 Summary"
ASSUME = "2. Assumptions"
MODELFORM = "3.3. Model formulation"
RESULT34 = "3.4. Result analysis"
CH4 = "4. Coaches Ranking Model Based on Cosine"
MODJUST = "4.2. Model justification"
MOD43 = "4.3. Model formulation"
IDEAL = "4.3.1. Vector definition of the “idealistic coach” and ranking"
COSINE = "4.3.2. Adjusted Cosine Similarity"
CLUSTER = "4.3.3. Model computing by Euclidean distance-based clustering analysis"
RESULT44 = "4.4. Results analysis"
CH5 = "5. Model Optimization of Time Line"
GENBASE = "5.2. Generation-based model optimization"
DIFFICULTY = "5.2.2. Coaching difficulty optimization"
RESULT54 = "5.4. Generation-based results analysis"
CH6 = "6. Model Optimization of Gender Based"
GENDER62 = "6.2. Gender-based model optimization"
GENDER63 = "6.3. Gender-based optimization results"
GENDER64 = "6.4. Gender-based results analysis"
EXTEND71 = "7.1. Establishment of factors pool"
RESULT81 = "8.1. Results"
ILLUSTRATE82 = "8.2. What the results illustrate"
ROBUST92 = "9.2. Robustness analysis"
APPENDIX = "12. Appendix"

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
           source: str = "text-layer", numbered: bool = True,
           cap_page: int | None = None, position: str = "below", note: str = "",
           other_note: str = "") -> None:
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
          numbered: bool = True, cap_page: int | None = None,
          position: str = "above") -> None:
    word = q(cap, cap_page or page) if (cap and source == "text-layer") else schema.norm(cap)
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


def build() -> None:
    # ---- the summary sheet's two unnumbered drawings -------------------------
    figure(2, 1, "flowchart-or-schematic", "", "none", none_mention(),
           [SUMMARY], "other", ticks=False, labels=True, source="none", numbered=False,
           note="the only unnumbered exhibit in the paper: a banded table-shaped flow chart "
                "whose in-art title band reads 'Model Execution Flow / College Coaches "
                "Ranking Model', with STEP rows divided into two and three columns, band "
                "rules but no connectors, and three orange arrows entering from a side "
                "label. No caption line prints anywhere on the page, so caption_source is "
                "none rather than a typed title. The detector boxes the same art twice, "
                "r2's frame 51 pt shorter at the foot; r2 is recorded as a duplicate")
    figure(3, 1, "photo-or-raster-image", "Figure 1", "Figure N",
           cited(3, 3, ["figure 1"], 1,
                 "Through the system, we find out the top 5 best coaches in basketball, "
                 "football and baseball as the following figure 1."),
           [SUMMARY], "other", panels=3, layout="2 over 1", ticks=False, numbered=False,
           note="three colour photographs of coach fives arranged as a collage: football "
                "top right, basketball top left, baseball bottom centre, each group posed "
                "on a printed podium block, no frame and no panel letter. The only caption "
                "is the bold 'Figure 1' under the collage, with no caption text at all - "
                "the three sport names inside the art are the only labels")
    figure(4, 1, "flowchart-or-schematic", "Figure 2", "Figure N",
           cited(4, 4, ["figure 2"], 1,
                 "The following in figure 2 evaluation factors are weighed in our system."),
           [SUMMARY], "other", ticks=False, labels=True, numbered=False,
           note="the factor ladder: a navy banner over seven boxes (Pct, Tenure, Games lost, "
                "Games won, Games directed, Teams directed, Social influence) flanked by a "
                "'Ranked coach' picture on the left and an '“Idealistic coach”' picture on "
                "the right. NO ARROWS, no frame and no connective drawing at all, so the "
                "relation the caption claims is carried by layout alone")
    exclude(1, 1, "not-an-exhibit",
            "the MCM summary sheet's title block - '2014 Mathematical Contest in Modeling "
            "(MCM)' over 'College Coaches' Mount Rushmore', with four undrawn signature rules "
            "under it; a control page, not an exhibit")
    exclude(2, 2, "duplicate",
            "the same execution flow chart boxed a second time, the frame 51 pt shorter at "
            "the foot; one drawing, not two")
    exclude(2, 3, "fragment-of-other",
            "the rotated 'Sensitivity and Robustness Analysis' box and its three arrows, "
            "detached at the right edge of the flow chart")
    exclude(3, 2, "fragment-of-other",
            "the basketball panel of Figure 1, second of the three panels")
    exclude(3, 3, "duplicate", "the basketball panel boxed a second time")
    exclude(3, 4, "duplicate", "the football panel boxed a second time")
    exclude(3, 5, "fragment-of-other",
            "the baseball panel of Figure 1, third of the three panels")
    exclude(3, 6, "duplicate", "the baseball panel boxed a second time")
    exclude(4, 2, "fragment-of-other",
            "the '“Idealistic coach”' picture inside Figure 2's bbox")
    exclude(4, 3, "duplicate", "the same picture boxed a second time")
    exclude(4, 4, "fragment-of-other", "the 'Ranked coach' picture inside Figure 2's bbox")
    exclude(4, 5, "duplicate", "the same picture boxed a second time")

    # ---- model I: the PCA grids ---------------------------------------------
    table(8, 1, 5, 2, "Table 1. General assumption", "Table N.",
          none_mention(), [ASSUME], "assumption", rules="boxed", txt=2,
          note="two columns of prose, Assumptions against Justification of assumptions, over "
               "four assumption rows: a rule above the header, a DOUBLE rule under it, a rule "
               "between every row and one centre vertical, but NO outer side borders, so the "
               "grid reads as an open boxed table. Never cited by number - its pointer is the "
               "caption. The bbox also swallows the section heading and the two prose columns "
               "that sit above the grid")
    exclude(10, 1, "not-an-exhibit",
            "the tail of a display formula - eleven glyph paths of a squared bracket and "
            "sigma group, no exhibit")
    table(11, 1, 12, 3, "Table 2. Result of PCA process", "Table N.",
          cited(11, 11, ["Table 2"], 1, "The results is shown in Table 2."),
          [MODELFORM], "model", rules="booktabs", num=3,
          note="three columns (Component, % of Variance, Cumulative %) over eleven components; "
               "the write-up mentions three but the grid prints all eleven because the third "
               "component stops at 76.966 per cent. Three horizontal rules only - top, a "
               "widened rule under the header and bottom - with no verticals. Set at about "
               "three quarters of the text measure and centred; the first three rows are bold")
    table(12, 1, 12, 4, "Table3. Component Matrix", "Table N.",
          none_mention(), [RESULT34], "result", rules="booktabs", num=4,
          note="the measured region is the HEADER BAND ONLY: the top rule and the double "
               "rule under 'Factors | Z1 | Z2 | Z3', everything below open. The eleven factor "
               "rows (Tenure, NCAA Tenure, Wins, Losses, Games, Winning Rate, Teams, NCAA "
               "Final Fours, NCAA Champions, Conference Champion, Googles) print as unruled "
               "text with no bottom rule at all. The caption prints with no space - "
               "'Table3.' - and the prose that introduces it is the only pointer: 'The "
               "Component Matrix of Z1, Z2 and Z3 is shown as follow.'")

    # ---- model II: the ranking figures and grids ----------------------------
    figure(13, 1, "bar", "Fig 1. The Influence of Principal Components", "Fig. N",
           cited(12, 13, ["Fig. 1"], 1, "It is shown as follows in Fig. 1"),
           [CH4, MODJUST], "model", legend="inside",
           note="a clustered column chart with three solid bars (blue Z1, red Z2, green Z3) "
                "standing side by side in ONE category position labelled 'Principal "
                "Component'; no value labels. Horizontal gridlines only, an outer grey border "
                "around plot and key, and the key inside that border at the right. The y-axis "
                "title prints 'Inflence', the paper's own misspelling. Cited on the page "
                "before it prints")
    figure(14, 1, "other",
           "Fig 2.Explanation of Cosine Similarity", "Fig. N", none_mention(),
           [MOD43, IDEAL], "model", panels=2, layout="2 stacked", ticks=False, labels=True,
           other_note="a two-vector geometry illustration - arrows A and B from a common "
                      "origin with a blue angle arc, once at 10 degrees and once at 68 "
                      "degrees, each with a leader line to a sentence of commentary; no axes, "
                      "no frame, no data",
           note="two drawings stacked in one box: the small-angle case captioned 'The angle "
                "between two vectors is small, so they are similar.' and the large-angle case "
                "with its negative counterpart. The caption prints with no space after the "
                "number - 'Fig 2.Explanation'. Never cited from the body")
    exclude(14, 2, "not-an-exhibit",
            "the display equation a-b = |a|x|b|cos(theta), five glyph paths")
    exclude(14, 3, "not-an-exhibit",
            "the display equation for cos(theta) as an inner product over two norms, eighteen "
            "fraction and radical paths")
    exclude(15, 1, "not-an-exhibit",
            "the inline vector definition V_i = (x_i1, x_i2, ..., x_i12), one path")
    exclude(15, 2, "fragment-of-other",
            "twenty-five paths confined to Table 4's caption band and its top rule - the "
            "outlined caption glyph strokes, not a table grid")
    figure(15, 3, "other",
           "Fig 3. Comparison between coaches and the “idealistic coach”", "Fig. N",
           none_mention(), [MOD43, COSINE], "model", ticks=False, labels=True,
           other_note="a raster three-vector illustration: 'Vector of Coach A' at 13 degrees "
                      "and 'Vector of Coach B' at 35 degrees against a red 'Vector of Best "
                      "Coach' arrow, with a bordered callout box explaining the ranking; no "
                      "axes, no data",
           note="the argument of the paper drawn as an angle comparison, with the reasoning "
                "typed into a framed note inside the art. Never cited by number: the prose "
                "says 'The example is as follows.' and the only by-number pointer on the "
                "page, 'It is illustrated in Fig 4.', belongs to the next page's Fig 4")
    figure(16, 1, "other", "Fig 4. Situation when two vectors overlap", "Fig. N",
           cited(15, 16, ["Fig 4"], 1, "It is illustrated in Fig 4."),
           [MOD43, CLUSTER], "model", ticks=False, labels=True,
           other_note="one degenerate vector pair - a long red 'Vector A' and a short black "
                      "'Vector B' from the same origin with a 0-degree arc; no axes, no frame",
           note="the 0-degree case drawn as two nearly collinear arrows, the labels burned "
                "into the art, and the caption inside the measured box at its foot. Cited a "
                "page early from the end of the cosine-similarity paragraph")
    exclude(16, 2, "not-an-exhibit",
            "display equation x'_ij = (x_ij - E_j)/(X_jmax - X_jmin) with its index range, no "
            "artwork")
    exclude(16, 3, "not-an-exhibit", "display equation for the column mean x-bar_j")
    exclude(16, 4, "not-an-exhibit", "display equation for the column deviation s_j")
    exclude(16, 5, "not-an-exhibit", "display equation for the standardized value x*_ij")
    exclude(17, 1, "fragment-of-other",
            "a loose three-path group wrapping the Fig 5 raster and its caption; no frame is "
            "drawn at this box - padded crop shows clean white on all four sides")
    figure(17, 2, "scatter", "Fig 5. Demonstration of Cluster Analysis.[21]", "Fig. N",
           cited(17, 17, ["Fig 5"], 1,
                 "Fig 5 shows the demonstration of Cluster Analysis."),
           [MOD43, CLUSTER], "model", labels=False,
           note="a 2-D scatter of three colour-coded clusters (red upper left, blue centre "
                "right, green lower centre) cut by three black straight boundaries meeting at "
                "a junction - a k-means partition, NOT a dendrogram, with no leaves and no "
                "merged groups. Both axes run 0 to 1 with a tick every 0.1, no axis titles, "
                "no legend, no gridlines. The caption carries a citation marker, "
                "'Cluster Analysis.[21]'")
    table(18, 1, 15, 6, "Table 5. Result of clustering analysis", "Table N.",
          cited(18, 18, ["Table 5"], 1,
                "Finally, we get the results of the clustering analysis is shown in Table 5."),
          [MOD43, CLUSTER], "model", rules="booktabs", num=3, txt=3,
          note="one exhibit printed as two stacked blocks: three Name/Cluster column pairs "
               "side by side, fourteen body rows in all, with 'Name Cluster Name Cluster "
               "Name Cluster' repeated as a header at the top of the second block. Booktabs "
               "only - a thick rule above and below the header and a thick closing rule, no "
               "verticals, no rule between any two body rows, no shading. Fourteen numbered "
               "clusters, each printed as 'rank:name' with the cluster number beside it")
    table(19, 1, 11, 3, "Table 6. Ranking result of cosine similarity model", "Table N.",
          none_mention(), [RESULT44], "result", rules="booktabs", num=1, txt=2,
          note="the measured region stops at the top of the body: it holds the section "
               "heading, the caption, the header 'Ranking | Name. | Gender' and row 1, while "
               "rows 2 to 10 print BELOW the box with the grid's rules - top rule, heavy rule "
               "under the header, no verticals and no rule between body rows. Ten body rows, "
               "the first ten of the same ranking that Table 7 reprints after the time-line "
               "pass. Never cited by number")
    figure(20, 1, "scatter",
           "Fig 6. Approximate linear relationship between the number of active coaches and "
           "the time line horizon", "Fig. N",
           cited(20, 20, ["Fig 6"], 1,
                 "Here is the approximate linear relationship between the number of active "
                 "coaches and the time line horizon in Fig 6. based on regression analysis."),
           [CH5, DIFFICULTY], "model", labels=True,
           note="a point cloud of one dot per year with a straight fitted line through it, "
                "both annotations burned into the art: 'Linear Regression with 95.0 % Mean "
                "Prediction Interval' and 'R2 Linear = 0.919'. Axis titles 'ActiveCoaches' "
                "and 'Years', no legend, no gridlines, no frame. The caption runs to sixteen "
                "words and wraps under the plot")
    figure(21, 1, "line", "Fig 7. Relation between Coaching difficulty and Generation",
           "Fig. N", cited(21, 21, ["Fig 7"], 1, "It is shown in Fig 7."),
           [CH5, DIFFICULTY], "model",
           note="one continuous red curve of the fitted difficulty law over the years, in a "
                "boxed MATLAB axes frame with inward ticks on all four sides, no gridlines, "
                "no legend, y 'Difficulty' and x 'Years' printed as axis titles")
    figure(22, 1, "line", "Fig 8. Adjustment of Difficulty Coefficient", "Fig. N",
           none_mention(), [CH5, DIFFICULTY], "model",
           note="the piecewise adjustment drawn as two straight segments: a 45-degree rise "
                "from (1,1) to (1.5,1.5) and then a flat run at C' = 1.5 out to 2. Both axes "
                "boxed, tick labels only, no legend and no axis titles. NEVER CITED - the "
                "piecewise rule above it is quoted in the prose instead")
    table(23, 1, 11, 3, "Table 7. Final ranking result", "Table N.",
          cited(23, 23, ["Table 7"], 1, "The final result is in Table 7."),
          [CH5, RESULT54], "result", rules="booktabs", num=2, txt=1,
          note="Ranking | Name. | Gender over ten coaches, horizontal rules only - a thin "
               "rule above the header, a heavy rule under it and a heavy closing rule, with "
               "no box, no verticals and no rule between body rows. Set at 76 per cent of the "
               "text measure. The identical ten-row list that Table 6 already printed")
    table(23, 2, 12, 3, "Table 8. Camparson of the 2 ranking result", "Table N.",
          none_mention(), [CH5, RESULT54], "result", header_rows=2, rules="booktabs",
          merged=True, num=1, txt=2,
          note="TWO header rows: a spanner 'before time optimized' over the first name "
               "column and 'After time optimized' over the second, then a leftover "
               "'Ranking | Name. | Gender' label row that the data outgrows - the body prints "
               "rank, the before name and the after name, and no gender value at all. Ten "
               "rows, the last one the only pair that disagrees (John Thompson becomes Billy "
               "Donovan). The caption misspells 'Comparison' as 'Camparson' and the grid is "
               "set at 85 per cent of the measure")

    # ---- model III and IV: the gender pass ----------------------------------
    table(25, 1, 2, 12, "Table 9. Result of ANOVA", "Table N.",
          cited(25, 25, ["Table 9"], 1,
                "We input the two groups of data belong to male and female coaches "
                "respectively in SPSS, and the result is illustrated in Table 9."),
          [CH6, GENDER62], "model", rules="booktabs", num=11, txt=1,
          note="the SPSS result cut down to two rows: a twelve-label header (Factors, then "
               "NC T W L G WR T NFF NCC CC G - T is spent twice, as is G) over a single "
               "Sig.(p) row that prints only ten values, so the last two columns carry no "
               "number. Three rules, no verticals. Set at the full measure")
    figure(26, 1, "bar", "Fig 9 Variance Comparison of Wins across gender", "Fig. N",
           none_mention(), [CH6, GENDER62], "model", legend="inside",
           note="a clustered column chart of one category ('malecoach or femalecoach') with "
                "two bars, blue 'Std. Deviation of malecoach Wins' and red 'female coach "
                "Wins', inside a light-grey outer frame with the key at the right. Horizontal "
                "gridlines every ten from 300 to 390, no vertical gridlines, y title 'Std. "
                "Deviation' set horizontally at the top left. Printed with no full stop after "
                "the number - 'Fig 9 Variance ...' - and never cited")
    table(27, 1, 3, 4, "Table 11. Var. of „win games‟ after adjusted", "Table N.",
          cited(27, 27, ["Table 11"], 1,
                "The optimized variance result is demonstrated in Table 11."),
          [CH6, GENDER63], "result", rules="booktabs", num=3, txt=1,
          note="Factors | N | Std. Deviation | Variance over the two gender rows, the N of "
               "30 printed once per row. A thick top rule, a double rule under the header (a "
               "3 pt bar and a hairline) and a thick closing rule, with no verticals and no "
               "rule between the two rows. Set at 77 per cent of the measure")
    figure(27, 2, "bar", "Fig 10. Modified Variance of Wins", "Fig. N",
           none_mention(), [CH6, GENDER64], "model", legend="inside",
           note="the same clustered column chart after the whitening pass: two bars, "
                "horizontal gridlines 300 to 340, key inside the frame at the upper right, y "
                "title 'Std. Deviation' and x title 'Male coach or Female coach'. Never cited")
    table(28, 1, 11, 3, "Table 12. Ranking result after gender factor adjusted",
          "Table N.",
          cited(27, 28, ["Table 12"], 1,
                "The ranking list after gender optimization and time line horizon "
                "optimization is shown in Table 12."),
          [CH6, GENDER64], "result", rules="booktabs", num=2, txt=1,
          note="the third ten-row ranking: Ranking | Name. | Gender after the gender factor "
               "is normalized, so Geno Auriemma moves from F(M) to second and Tara "
               "VanDerveer enters at ninth while John Calipari and Roy Williams climb. Shown "
               "as one rule above the header, a double rule under it and a heavy closing "
               "rule, no verticals, no row rules, 76 per cent of the measure")

    # ---- model extension: the factor pool and the sport grids ----------------
    figure(29, 1, "flowchart-or-schematic", "Fig 11. The demonstration of Factors Pool",
           "Fig. N",
           cited(28, 29, ["Fig 11"], 1, "The factors pool is demonstrated in Fig 11."),
           [EXTEND71], "model", ticks=False, labels=True,
           note="a central column of fourteen white factor boxes (Tenure, Tenure in NCAA, "
                "Wins, Losses, Ties, Games, Winning Rate, Teams, Awards, Bowl Times, Bowl "
                "Wins, Bowl Losses, Bowl Ties, Google Searches) with four sport labels beside "
                "it - Basketball and Baseball on the left, Softball and Football on the "
                "right - joined by orthogonal elbow connectors of four colours. NO legend, no "
                "title in the art and no grouping brackets: membership is carried by the "
                "connector colour alone, which is unreadable at print size")

    # ---- the four sport grids, whose cells hold portraits -------------------
    table(32, 1, 6, 6, "Table 17. Basketball Coach Ranking", "Table N.",
          none_mention(), [RESULT81], "result", rules="booktabs", num=5, txt=1,
          note="the measured region is the header band - 'Ranking | Name | Tenure | Wins | "
               "Games | Winning Rate' with 'Rate' wrapped to a second line - over a grid "
               "with no verticals, no side borders, a thick top rule, a thick rule under the "
               "header and a fine dashed separator between body rows. Five body rows, four "
               "of them on this page and the fifth at the head of the next, and EVERY ROW "
               "CARRIES A COLOUR PORTRAIT OF THE COACH inside the Name column, which the "
               "detector reports as four separate regions and which are fragments of this "
               "table. Wins print red and Winning Rate cyan. Never cited by number")
    table(33, 2, 6, 6, "Table 18. Football Coach Ranking", "Table N.",
          none_mention(), [RESULT81], "result", rules="booktabs", num=5, txt=1,
          note="the same construction for football, five rows with a portrait per row: Bear "
               "Bryant, Vince Dooley, Joe Paterno, Lou Holtz and Darrell Royal, two of them "
               "at the foot of this page and two on the next. Never cited by number")
    table(34, 3, 6, 6, "Table 19. Baseball Coach Ranking", "Table N.",
          none_mention(), [RESULT81], "result", rules="booktabs", num=5, txt=1,
          note="the same construction for baseball: Don Schaly and Ron Fraser here, Ray "
               "Tanner, Bill Holowaty and Mike Martin on the next page, one portrait per row "
               "and the closing rule at the foot of page 35. Never cited by number")
    exclude(32, 2, "fragment-of-other",
            "coach portrait in Table 17's Name column, row 1 (John Wooden)")
    exclude(32, 3, "fragment-of-other",
            "coach portrait in Table 17's Name column, row 2 (Geno Auriemma)")
    exclude(32, 4, "fragment-of-other",
            "coach portrait in Table 17's Name column, row 3 (Pat Summitt)")
    exclude(32, 5, "fragment-of-other",
            "coach portrait in Table 17's Name column, row 4 (Dean Smith)")
    exclude(33, 1, "fragment-of-other",
            "coach portrait for Table 17's row 5 (Mike Krzyzewski), printed above Table 18's "
            "closing rule")
    exclude(33, 3, "fragment-of-other",
            "coach portrait in Table 18's Name column, row 1 (Bear Bryant)")
    exclude(33, 4, "fragment-of-other",
            "coach portrait in Table 18's Name column, row 2 (Vince Dooley)")
    exclude(33, 5, "fragment-of-other",
            "coach portrait in Table 18's Name column, row 3 (Joe Paterno)")
    exclude(34, 1, "fragment-of-other",
            "coach portrait in Table 18's Name column, row 4 (Lou Holtz)")
    exclude(34, 2, "fragment-of-other",
            "coach portrait in Table 18's Name column, row 5 (Darrell Royal); the photograph "
            "carries 'DARRELL K. ROYAL / TEXAS MEMORIAL STADIUM' burned into it")
    exclude(34, 4, "fragment-of-other",
            "coach portrait in Table 19's Name column, row 1 (Don Schaly)")
    exclude(34, 5, "fragment-of-other",
            "coach portrait in Table 19's Name column, row 2 (Ron Fraser)")
    exclude(35, 1, "fragment-of-other",
            "the text band of Table 19's last three rows (3 Ray Tanner, 4 Bill Holowaty, 5 "
            "Mike Martin), no header, no caption")
    exclude(35, 2, "fragment-of-other",
            "coach portrait in Table 19's Name column, row 3 (Ray Tanner)")
    exclude(35, 3, "fragment-of-other",
            "coach portrait in Table 19's Name column, row 4 (Bill Holowaty); a second figure "
            "is half cropped at the left edge of the photograph itself")
    exclude(35, 4, "fragment-of-other",
            "coach portrait in Table 19's Name column, row 5 (Mike Martin)")

    # ---- Fig 12, the map ----------------------------------------------------
    figure(35, 5, "map-or-plan-view", "Fig.12 Map of U.S.A. [22]", "Fig. N",
           none_mention(), [ILLUSTRATE82], "result", ticks=False, labels=False,
           note="an illustrated pictorial map of the contiguous United States - teal water, "
                "flat pale-green land, cartoon sports figures planted on the states, faint "
                "state boundaries, no per-state shading, no scale, no north arrow, no state "
                "labels and no title inside the art. The caption credits the source with a "
                "reference marker and a right-aligned note under the grid above reads 'Images "
                "come from Google Image Search'. The detector boxes it twice, r6 overlapping "
                "r5 with more slack top and bottom")
    exclude(35, 6, "duplicate",
            "the same US map boxed a second time, the frame padded above and below")

    # ---- the noise test -----------------------------------------------------
    table(37, 1, 3, 13, "Table 21. Data comparison of John Wooden", "Table N.",
          cited(37, 37, ["Table 21"], 1,
                "The data comparison of a coach is shown in Table 21."),
          [ROBUST92], "test", rules="booktabs", num=12, txt=0,
          note="TWO body rows only, the raw and the noised factor vectors of one coach, under "
               "a heavy rule above the header, a heavy rule under it and a heavy rule below "
               "the last row, with no verticals and no rule between the two rows. Thirteen "
               "labels print in the header (T NC T W L G WR T NFF NCC CC G A) against twelve "
               "numeric fields per row, so the trailing labels have no column; the '1.2' and "
               "'1' at the left of the region belong to Fig 13's y axis, not to this grid")
    figure(37, 2, "line", "Fig. 13 Data Comparison of John Wooden before and after noise "
           "input", "Fig. N", none_mention(), [ROBUST92], "test", legend="inside",
           note="a MATLAB stem plot: one open circle per factor with a stem dropped to zero "
                "and no connecting line, two series (red 'Original Data', blue 'Data added "
                "with noise'), key boxed inside the plot at the upper right, y 'Standardized "
                "Score of Factors', x '12 Different Factors', no gridlines. Never cited by "
                "number, and the x-axis title at the head of the region is what the heading "
                "detector read as a section called '12 Different Factors'")
    table(37, 3, 11, 2, "Table 22. Comparison of adding noise", "Table N.",
          cited(37, 37, ["Table 22"], 1, "The new ranking is shown in Table 22."),
          [ROBUST92], "test", rules="booktabs", num=0, txt=2,
          note="two rank lists side by side under one header row - 'Ranking list after noise "
               "input' and 'Ranking list before noise input' - with a rule above the header, a "
               "rule under it and a closing rule, no vertical divider between the lists and "
               "no rule between rows. NO RANK NUMERALS: the lists are read by position, and "
               "the names are the only content. Three pairs print on this page and the "
               "remaining seven on the next, which is a refusal")
    exclude(38, 1, "split-across-pages",
            "the continuation of Table 22: seven more name pairs with no repeated header, no "
            "caption and no closing rule, ending with Tom Izzo against Billy Donovan")

    # ---- the appendix blocks ------------------------------------------------
    table(41, 1, 39, 9, "", "none", none_mention(), [APPENDIX], "appendix",
          rules="boxed", num=7, txt=2, source="none",
          note="the unnumbered 'Original Data' block, the first of two 60-row data dumps: nine "
               "columns (Name., G for gender, Exp, NExp, W, L, G for games, WR, T) in a FULL "
               "GRID - outer box, a rule between every row and a vertical at every column "
               "boundary - with the block title and one header row and no header repeat. "
               "Thirty-eight rows here, twenty-two on the next page. The header spends G "
               "twice, on gender and on games, and the tail of the previous column of the "
               "page prints 'Appendix' as the only label the block gets")
    exclude(42, 1, "split-across-pages",
            "the continuation of the Original Data block: the remaining twenty-two rows, no "
            "repeated header, no closing rule")
    table(42, 2, 19, 9, "", "none", none_mention(), [APPENDIX], "appendix",
          rules="boxed", num=7, txt=2, source="none",
          note="the unnumbered 'Modified Data' block, the same nine columns in a new full "
               "grid with its own title line and a repeated header, carrying the whitened "
               "values that run to seven decimals against the two and three of the Original "
               "block. Eighteen rows here, forty-one on the next page and one on the last, so "
               "sixty in all - the two blocks are the same sixty coaches")
    exclude(43, 1, "split-across-pages",
            "the continuation of the Modified Data block: forty-one rows, no repeated header, "
            "no closing rule")
    exclude(44, 1, "split-across-pages",
            "the last row of the Modified Data block (Regina Miller) with the wrapped "
            "fragment 'Elliott' left over from the previous page's name column")


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
    out = PROXY / "pc62-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{out} items={len(ITEMS)} tables={len(TABLES)} excluded={len(EXCLUDED)}")
    return 0


RULES: list[str] = [
    "Caption side splits by kind and holds throughout: every one of the fifteen figure "
    "captions prints below its art and every grid caption prints above its grid "
    "[caption.position]",
    "The paper runs two independent number series - the summary sheet's bold 'Figure 1' and "
    "'Figure 2' with no caption text, then the body's 'Fig 1.' to 'Fig 13' - so fifteen "
    "printed numbers cover sixteen exhibits once the unnumbered page-2 flow chart is counted "
    "[caption.numbering]",
    "Ruling is three registers and no grid crosses them: the empirical SPSS grids are "
    "booktabs with three horizontal rules and no verticals at all, Table 1 is a boxed grid "
    "with open sides, and the two appendix data dumps are full grids with a rule under every "
    "row and a vertical at every column boundary [table.rule_style]",
    "No grid in the paper bands a row and none shades a cell; the only colour is inside the "
    "figures and inside the coach portraits that sit in the cells of Tables 17 to 19 "
    "[table.zebra]",
    "A grouped header prints as a spanner: Table 8 spanners 'before time optimized' and "
    "'After time optimized' over two name columns, and that is the paper's only merged cell "
    "[table.merged_cells]",
    "Only Table 8 carries two header rows; the seven sport grids carry one and the appendix "
    "dumps repeat a single header at the top of each block [table.header_rows]",
    "Nine grids are set short of the text measure - 76 to 87 per cent, each measured and "
    "declared in its note - and the rest run full, so 'full' here means the wide bucket, not "
    "the exact measure [table.width]",
    "Two grids print a header with more labels than the body has fields - Table 9 prints "
    "twelve labels over ten Sig. values and Table 21 thirteen over twelve - because a label "
    "column collapsed in typesetting [table.numeric_cols]",
    "Decimals never align on the point: the SPSS values are right-aligned with ragged digit "
    "counts and the appendix blocks mix two, three and seven decimals in one column "
    "[table.decimal_aligned]",
    "The heading detector is unusable on this paper - 112 heading records, every one with a "
    "null text, and section paths assembled from racing-result rows ('8 Bill Self M', '12 "
    "Different Factors') - so all forty section labels are the printed headings, which the "
    "text layer does carry verbatim, with section_numbered true [place.section_numbered]",
    "Two of the sixteen figure rows are schematics the vocabulary cannot name more precisely: "
    "the three vector-angle illustrations are filed 'other' with an other_note, while the "
    "execution flow chart, the factor ladder and the factors pool land on the schematic "
    "family [geometry.family]",
    "Every chart prints numbers on at least one axis; the schematic, the three vector "
    "diagrams and the map print no numbers at all, and only the map prints no labels either "
    "[geometry.printed_numbers]",
    "Three charts key their series inside the frame and no chart ever keys outside it; the "
    "factors pool keys nothing and relies on the colour of its connectors [geometry.legend]",
    "Nothing in the paper is three-dimensional and no colourbar appears anywhere "
    "[geometry.three_d]",
    "Citation is optional here: ten of the sixteen figure rows and eight of the seventeen "
    "table rows are never cited by number at all, four figures are reached by deixis only, "
    "and the two appendix blocks have no numbering to cite [mention.count]",
]

NOTE = (
    "Sixteen figure rows and seventeen tables over 76 measured regions on 34 of 44 pages, "
    "plus 43 refusals. Families: table-grid 17, flowchart-or-schematic 3, bar 3, line 3, "
    "other 3, scatter 2, photo-or-raster-image 1, map-or-plan-view 1.\n"
    "\n"
    "Coverage gap that cannot become a row. Seven numbered tables print with no measured "
    "region: Table 4 on page 15 (its caption band is boxed as a 25-path fragment and the "
    "grid below it was never boxed), Table 10 on page 25, Tables 13, 14 and 15 on page 30, "
    "Table 16 on page 31 and Table 20 on page 36 - every one of those pages has zero regions "
    "except page 15. All seven are visibly ruled, each with the same three-rule house style "
    "(heavy rule under the caption, double rule under the header, heavy closing rule, no "
    "verticals), and they print at 158 to 437 pt of a 595 pt page, so the region pass had no "
    "enclosing box to key on. Numbers they carry: 4 is one data row against a twelve-label "
    "header, 10 is two gender rows, 13 and 14 are the football and softball top fives, 15 is "
    "the baseball top five mis-titled 'Softball Coach Ranking' with Ron Fraser printed twice, "
    "16 is the Chinese top five, and 20 is a two-column nine-row before/after list whose "
    "header label prints 'Ranking before adjustment' over both columns. With those seven "
    "declared, the paper's 22 numbered tables and 2 unnumbered appendix blocks are all "
    "accounted for by 15 numbered rows and 2 unnumbered rows.\n"
    "\n"
    "Declared decisions. (1) The page-2 execution flow chart is one exhibit boxed twice, and "
    "the detector also boxes its side label and the three arrows, which are fragments. "
    "(2) Figure 1's three panels are photographs boxed six times and Figure 2's two flanking "
    "pictures twice; one row each, panels 3 and 1, the repeats refused as duplicates or "
    "fragments. (3) Table 3's region is the header band only - the eleven factor rows below "
    "it are unruled text with no bottom rule. (4) Table 6's region holds its heading, caption, "
    "header and first body row, with rows 2 to 10 printing outside the box. (5) Tables 17 to "
    "19 carry a coach photograph inside the Name column of every row; the twelve portraits are "
    "fragments of those three tables and one of them is printed above the closing rule of the "
    "next table. (6) Fig 12 and Table 22 each cross a page: the map is boxed twice over and "
    "Table 22's seven remaining pairs are a split-across-pages refusal. (7) The appendix is "
    "two 60-row dumps - 'Original Data' and 'Modified Data' - each split over three pages and "
    "each recorded as one unnumbered table with three refusals.\n"
    "\n"
    "Recorded defects. 'Inflence' is the y-axis title of Fig 1; Fig 2's caption runs the "
    "number into the title with no space ('Fig 2.Explanation'); Table 8 misspells Comparison "
    "as 'Camparson'; Table 3 numbers without a space ('Table3.'); Table 4's caption line is "
    "extracted twice on page 15; Table 9's header spends both T and G twice, and Table 21's "
    "header prints thirteen labels over twelve fields; Table 15 is titled 'Softball Coach "
    "Ranking' while listing baseball coaches; the appendix header spends G twice, on gender "
    "and on games; two coach names are truncated in the Original block ('Brenda Fres') and "
    "three are wrapped across the row in the Modified block; and the p35 map carries a "
    "half-cropped second figure at the left edge of one portrait.\n"
    "\n"
    "Citation behaviour. Ten rows are never named by number (Fig 8, Fig 9, Fig 10, Fig 12, "
    "Fig 13, and Tables 1, 3, 6, 8, 17, 18, 19 - Table 6 and Table 3 are introduced by "
    "deixis, 'shown as follow.'), four are cited a page before they print (Fig 1 from page "
    "12, Fig 4 from page 15, Fig 11 from page 28, Table 12 from page 27), and page 20 puts "
    "the number mid-sentence - 'in Fig 6. based on regression analysis'."
)

if __name__ == "__main__":
    sys.exit(main())
