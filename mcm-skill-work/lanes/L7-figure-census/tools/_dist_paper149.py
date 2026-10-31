"""Hand pass for P-B-2018-74316-1198d12d (2018 MCM B, "Team 74316", language
distribution over time and geography, office siting).

39 PDF pages (28 printed, page 9 blank apart from the watermark), 115 measured
regions on 32 pages. Every region is claimed exactly once: body and appendix
figures, grids printed as raster, appendix data dumps, and display mathematics
as exclusions.

Usage: python -I tools/_dist_paper149.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2018-74316-1198d12d"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
REG = {(pg["page"], i): list(r["bbox"])
       for pg in LAYOUT["pages"] for i, r in enumerate(pg["regions"], 1)}
MEASURED = {(p, tuple(b)) for (p, _), b in REG.items()}


def bb(page: int, index: int) -> tuple[int, list[float]]:
    return page, REG[(page, index)]


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    w, h = DIMS[page]
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < h / 3 else ("middle" if mid < 2 * h / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (w * h)
    return {
        "section_path": [f"未编号标题：{p}" for p in path],
        "section_numbered": False,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 1,
        "page_zone": z,
        "area_frac": round(frac, 4),
        "solo_page": False,
    }


def cap(v: str, numbering: str = "Figure N:", *, position: str = "below",
        units: bool = False, variables: int = 0, conditions: bool = False,
        concludes: bool = False, voice: str = "none") -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)) if v else 0,
        "sentences": len(schema.sentences(v)) if v else 0,
        "units": units,
        "variables": variables > 0,
        "variable_count": variables,
        "conditions": conditions,
        "concludes": concludes,
        "voice": voice,
        "position": position,
    }


def mention(page: int, *, first: int | None, style: list[str], count: int = 0,
            lead: str = "", pattern: str = "none", trail: str = "",
            read: int = 0) -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style,
        "count": 0 if first is None else count,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": None if first is None else abs(page - first),
    }


def geo(family: str, *, legend: str = "none", numbers: bool = True,
        colorbar: bool = False, three_d: str = "no", panels: int = 1,
        layout: str = "1", shared: bool = False, labels: bool = False) -> dict:
    return {
        "family": family,
        "panel_count": panels,
        "panel_layout": layout,
        "shared_axes": shared,
        "legend": legend,
        "colorbar": colorbar,
        "three_d": three_d,
        "printed_numbers": numbers,
        "data_labels": labels,
    }


def figure(key: str, caption: dict, men: dict, geom: dict, *, path: list[str],
           kind: str, note: str = "", caption_source: str = "text-layer",
           other_note: str = "") -> dict:
    page, bbox = B[key]
    item = {
        "page": page,
        "bbox": bbox,
        "family": geom["family"],
        "confidence": "high",
        "panel_count": geom["panel_count"],
        "is_panel_of": "",
        "caption_verbatim": caption["verbatim"],
        "caption_source": caption_source,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "geometry": geom,
    }
    if other_note:
        item["other_note"] = other_note
    return item


def grid(rows: int, cols: int, *, header: int = 1, numeric: int = 0, txt: int = 1,
         rule: str = "booktabs", zebra: bool = False, merged: bool = False,
         diagonal: bool = False, units_in_header: bool = False, decimal: bool = False,
         width: str = "full", continued: bool = False, note: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rule,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": diagonal,
        "units_in_header": units_in_header,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": "portrait",
        "continued": continued,
        "note_sentence": note,
    }


def table(key: str, caption: dict, men: dict, g: dict, *, path: list[str], kind: str,
          note: str = "", caption_source: str = "text-layer") -> dict:
    # A grid's caption is numbered the table way; only the figure helper defaults to
    # "Figure N:".
    if caption["numbering"] == "Figure N:":
        caption = dict(caption, numbering="Table N:")
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": caption["verbatim"],
        "caption_source": caption_source,
        "note": note,
        "place": place(page, bbox, path, kind),
        "mention": men,
        "caption": caption,
        "table": g,
    }


def uncap(position: str = "above") -> dict:
    """An exhibit the paper prints with no caption line of its own."""
    return cap("", "none", position=position)


FIGURES: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[tuple[str, tuple[int, list[float]], str]] = []
S_M1 = ["Model 1 – Language Speakers’ Quantitatively Distribution"]
S_INTA = S_M1 + ["Introduction and Assumptions"]
S_VARS = S_INTA + ["Variables and Parameters"]
S_SHORT = S_M1 + ["Short-term Models"]
S_AR = S_SHORT + ["Native Speaker Model - Autoregressive model"]
S_ECM = S_M1 + ["Non-native Speaker Model – Error Correction Model"]
S_LONG = S_M1 + ["Long-term Models – Logistic Model"]
S_DESIGN = S_LONG + ["Model Design"]
S_PRED = S_M1 + ["Predictions"]
S_SENS = S_M1 + ["Validation of Model 1", "Sensitivity Analysis"]
S_M2 = ["Model 2 - Geographic distribution"]
S_MARKOV = S_M2 + ["Migration Patterns – Markov Process"]
S_MKVARS = S_MARKOV + ["Assumptions and Variables"]
S_MKSET = S_MARKOV + ["Model Settings"]
S_LDIST = S_M2 + ["Language Distributions"]
S_LPRED = S_LDIST + ["Prediction"]
S_M2CMP = S_M2 + ["Conclusion", "Comparison of Model 1&2"]
S_M3 = ["Model 3 – Offices Location Decisions"]
S_CLUST = S_M3 + ["Model in Short-term and Long-term - Cluster Analysis & MODM"]
S_M3SET = S_CLUST + ["The Settings and Solutions of Model"]
S_MINE = S_M3 + ["Resource-saving Suggestions – MINE Model"]
S_RESULTS = ["Results"]
S_APPX = ["Appendix"]

B: dict[str, tuple[int, list[float]]] = {
    "t1": bb(4, 1),
    "t2": bb(6, 1),
    "f3": bb(6, 2),
    "f1": bb(6, 3),
    "f2": bb(6, 4),
    "f5": bb(6, 5),
    "f4": bb(6, 6),
    "t3h": bb(6, 7),
    "t3t": bb(7, 1),
    "t4": bb(7, 3),
    "t5": bb(8, 2),
    "t6": bb(8, 3),
    "t6h": bb(8, 4),
    "t7": bb(10, 1),
    "t8": bb(10, 3),
    "f6": bb(11, 3),
    "f7": bb(11, 4),
    "f8": bb(11, 5),
    "f9": bb(11, 6),
    "t9": bb(12, 1),
    "f10": bb(12, 2),
    "t10": bb(12, 3),
    "f11": bb(13, 1),
    "f12a": bb(13, 2),
    "t11": bb(13, 3),
}

FIGURES += [
    figure("f3",
           cap("Figure 3: Number of Total Speakers (Unit: Millions)", units=True),
           mention(6, first=None, style=[]),
           geo("line", legend="above"),
           path=S_AR, kind="model",
           note="right-hand cell of a row of three 2003-2017 series plots: ten curves "
                "(Mandarin Chinese, English, Hindustani, Spanish, Arabic, Malay, Russian, "
                "Bengali, Portuguese, French) drawn over the fourteen observed years, key in "
                "a single-row box above the frame. The unit tag '(Unit: Millions)' printed "
                "after the third caption belongs to all three plots - the axis title itself "
                "carries no unit"),
    figure("f1",
           cap("Figure 1: Number of L1 Speakers"),
           mention(6, first=None, style=[]),
           geo("line", legend="above"),
           path=S_AR, kind="model",
           note="left-hand cell of the same row: the L1 curves of the ten languages over "
                "2003-2017. It is the only one of the three whose ordinate is titled by the "
                "caption alone - the axis prints no unit, so a reader has to carry 'Millions' "
                "across from Figure 3's caption"),
    figure("f2",
           cap("Figure 2: Number of L2 Speakers"),
           mention(6, first=None, style=[]),
           geo("line", legend="above"),
           path=S_AR, kind="model",
           note="middle cell of the same row, L2 curves. Same key box, same years, ordinate "
                "0-600 against Figure 1's 0-1000 - the only difference between the two "
                "frames is the variable plotted"),
    figure("f5",
           cap("Figure 5: Autocorrelation and Partial Correlation"),
           mention(6, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_AR, kind="model",
           note="right-hand cell: an EViews-style correlogram, three blocks side by side - "
                "an ACF bar panel, a PACF bar panel and a printed statistics grid of twelve "
                "lag rows with AC, PAC, Q-Stat and Prob columns. The drawn bars carry no tick "
                "labels at all, so every readable number in the frame is in the third block. "
                "Dashed confidence bands are the only annotation. The caption line prints "
                "'Figure 5: Autocorrelation and Partial Correlation' and the language name "
                "'of Mandarin Chinese' falls after it, on the same text line but after "
                "Figure 4's name, so the pair reads as 'of English of Mandarin Chinese'"),
    figure("f4",
           cap("Figure 4: Autocorrelation and Partial Correlation"),
           mention(6, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_AR, kind="model",
           note="left-hand cell of the correlangram pair, the same three-block template for "
                "English. Reading order is caption then language: the text layer prints "
                "'Figure 4: ... of English' only by joining the two lines, which is why the "
                "quote here stops at the colon-title"),
    figure("f6",
           cap("Figure 6: L1 Speakers Versus Time when N(0)>Nm"),
           mention(11, first=None, style=[]),
           geo("line", legend="inside", labels=False),
           path=S_DESIGN, kind="model",
           note="the first of four logistic-model plots planted two by two: Time 0-100 "
                "against L1 speakers 0-800, four curves keyed N(0)=100/300/500/1000 in a box "
                "inside the upper right. Straight rising lines that flatten towards Nm - the "
                "picture of an approach to a carrying capacity"),
    figure("f7",
           cap("Figure 7: L1 Speakers Versus Time when (δ=-0.1, Nm=1000)"),
           mention(11, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_DESIGN, kind="model",
           note="the only plot in the paper with a negative ordinate: ticks 0 to -8 with a "
                "x10^6 scale marker, four curves keyed N(0)=1500/1300/1200/1100, and the "
                "curves leave the frame at about -7. The printed caption repeats its "
                "condition, text layer 'when (d=-0.1, Nm=1000) N(0)>Nm (d=-0.1, Nm=1000)', "
                "and the tick labels collide with the scale marker at top left"),
    figure("f8",
           cap("Figure 8: L1 Speakers Versus Time ( =0.1, Nm=1000)"),
           mention(11, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_DESIGN, kind="model",
           note="the delta glyph is missing from the caption - the parenthesis opens on a "
                "blank, so the printed condition reads '( =0.1, Nm=1000)'. Four curves keyed "
                "N(0)=500/800/1200/1400 rising into a plateau"),
    figure("f9",
           cap("Figure 9: Total Speakers Versus Time for Different Initial Value ( =0.1, "
               "Nm=1000,  =3)"),
           mention(11, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_DESIGN, kind="model",
           note="same four-curve frame as Figure 8 but the ordinate is the total (L1+L2) and "
                "the caption adds mu=3 - both the delta and the mu glyphs are lost, so the "
                "caption prints two blanks where the parameters belong"),
    figure("f10",
           cap("Figure 10: Number of Speakers Versus Time for Mandarin Chinese"),
           mention(12, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_DESIGN, kind="model",
           note="Time 0-1000 against 0-5000, three curves keyed Total / L1 / L2 in the upper "
                "left; the only plot in the paper that shows the whole composition of one "
                "language over a millennium instead of a parameter sweep"),
    figure("f11",
           cap("Figure 11: Predictions for Malay and Russian"),
           mention(13, first=None, style=[]),
           geo("composite-panel", panels=2, layout="1x2", legend="inside"),
           path=S_PRED, kind="other",
           note="two independently framed line panels side by side, each with its own key "
                "(L2/L1/Total upper right) and its own ordinate - Malay 0-350 against "
                "Russian 0-500 - under inline panel titles 'Malay' and 'Russian'. One caption "
                "covers both, so the frame is a plate rather than a single plot"),
    figure("f12a",
           cap("Figure 12: Number of Total Speakers for 4 Special Languages"),
           mention(13, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_PRED, kind="other",
           note="Time 0-80 against 100-900 with four curves keyed Hausa / German / Russian / "
                "Malay. The caption says four special languages and the key names all four, "
                "but the printed number is 12 - the same number the sensitivity plate on "
                "page 14 carries, so the paper prints two different Figure 12s"),
]

TABLES += [
    table("t1",
          cap("Table 1: Variables and Parameters for Model 1", "Table N:", position="below"),
          mention(4, first=None, style=[]),
          grid(12, 2, numeric=1, txt=1, rule="boxed"),
          path=S_VARS, kind="symbols",
          note="twelve rows of symbol against definition, ruled as a full grid - every "
               "vertical cell boundary and a horizontal rule under the header band 'PARAMETERS "
               "| DEFINITION', which is itself merged across the two columns. The symbol "
               "column is nearly empty in the render: the Greek letters and delta/epsilon "
               "glyphs did not survive, so the definitions stand beside blank cells, and the "
               "definition column is offset one row against the symbols"),
    table("t2",
          cap("Table 2: List of Languages by Numbers of Speakers （Unit: Millions）",
              "Table N:", units=True),
          mention(6, first=10, style=["Table 2"], count=1,
                  trail="According to the difference equation from formula (3) and Table 2"),
          grid(51, 12, header=2, numeric=12, txt=0, merged=True, decimal=False),
          path=S_AR, kind="model",
          note="the paper's widest grid: ten language blocks printed in three bands of four, "
               "four and two, each band repeating the fifteen year rows 2003-2017 and each "
               "block covering three columns (L1 Speakers, L2 Speakers, Total). Header depth "
               "is two rows - the language name spans its three columns, the measure row "
               "names them - so the band header is the only merged cell in the table. Body "
               "text prints at roughly four points and is not legible at native render even "
               "at 300 dpi, which is why the row count is read from the printed year labels "
               "rather than from the numbers"),
    table("t3h",
          uncap("below"),
          mention(6, first=None, style=[]),
          grid(7, 5, numeric=4, txt=1, decimal=True),
          path=S_AR, kind="model", caption_source="none",
          note="first half of the AR(1) estimation grid, printed at the foot of page 6 with "
               "neither number nor caption: header Languages / phi1 / sigma / P-Value / R^2 "
               "and six languages. The three remaining languages and the caption print on the "
               "next page, so this cell is the head of a table the detector cut in two"),
    table("t3t",
          cap("Table 3: AR(1) Model for Different Languages"),
          mention(7, first=None, style=[]),
          grid(3, 5, header=1, numeric=4, txt=1, decimal=True, continued=True),
          path=S_AR, kind="model",
          note="the tail of the same grid - Bengali, Portuguese, French with their estimates "
               "- carrying the caption and no header row at all, so the reader has to look "
               "back a page to know which column is sigma. header_rows is recorded as 1 "
               "because the field has no zero state; nothing in this region is a header"),
    table("t4",
          cap("Table 4: Akaike Information Criterion Test"),
          mention(7, first=None, style=[]),
          grid(22, 10, header=2, numeric=9, txt=1, merged=True, rule="boxed", decimal=True),
          path=S_AR, kind="model",
          note="the only fully ruled grid in the paper: a box around every cell, spanner "
               "headers FPE / AIC / BIC each covering three P=0,1,2 columns, and the language "
               "name merged down its two sub-rows. Ten languages at two rows each. Every "
               "value matches Table 3's phi1 to three decimals, so the grid is three "
               "selection criteria recomputed on the same fits"),
    table("t5",
          cap("Table 5: EG Co-integration Test"),
          mention(8, first=10, style=["Table 5"], count=1,
                  trail="In connection with the six estimations in Table 5"),
          grid(7, 4, numeric=3, txt=1, decimal=True),
          path=S_ECM, kind="model",
          note="six languages against ADF-t statistic, a yes/no 'Is {eps_t} a Unit Root?' "
               "column and a co-integration verdict. Half the cells are words, not numbers, "
               "and the two verdict columns say the same thing twice ('No Exist' in both)"),
    table("t6",
          cap("Table 6: Consequence of The First Step of EG Method"),
          mention(8, first=None, style=[]),
          grid(7, 6, numeric=5, txt=1, decimal=True),
          path=S_ECM, kind="model",
          note="six languages against five coefficients. The header row for the five numeric "
               "columns is not on this block - it prints after the caption, at the very foot "
               "of the page, as the separate header-only region recorded below"),
    table("t6h",
          uncap("below"),
          mention(8, first=None, style=[]),
          grid(1, 6, numeric=5, txt=1, continued=True),
          path=S_ECM, kind="model", caption_source="none",
          note="an orphan: the header row 'Languages beta11 beta21 beta31 beta41 -lambda' "
               "printed at the bottom of page 8, after Table 6's body and after its caption "
               "line. It is the only header Table 6 has, and it sits below the numbers it "
               "describes"),
    table("t7",
          cap("Table 7: Consequence of The Second Step of EG Method"),
          mention(10, first=None, style=[]),
          grid(6, 6, header=1, numeric=5, txt=1, decimal=True),
          path=S_ECM, kind="model",
          note="six languages against five columns with no header inside the measured box - "
               "the header prints above the region boundary, so this grid arrives as numbers "
               "only. Its five columns are the same five as Table 6's, and header_rows is "
               "recorded as 1 only because the field has no zero state"),
    table("t8",
          cap("Table 8: Consequence of Dickey-Fuller Test"),
          mention(10, first=None, style=[]),
          grid(7, 3, numeric=2, txt=1, decimal=True),
          path=S_ECM, kind="model",
          note="six languages against a PP statistic and a yes/no stationarity verdict; the "
               "caption line prints '(See Appendix 6 for details)' immediately before the "
               "header, the paper's only cross-reference that lives inside a table"),
    table("t9",
          cap("Table 9: Approximation of Parameters in Long-term Models"),
          mention(12, first=None, style=[]),
          grid(11, 4, numeric=3, txt=1, decimal=True),
          path=S_DESIGN, kind="model",
          note="ten languages against the three fitted parameters of the logistic model "
               "delta, Nm and mu. The header prints the three glyphs, and two of them reach "
               "the text layer as private-use blanks, so the columns are identified only by "
               "position"),
    table("t10",
          cap("Table10: Predictions for current Top 10 Languages in Next 50 years", "Table N:"),
          mention(12, first=None, style=[]),
          grid(11, 4, numeric=3, txt=1, decimal=True),
          path=S_PRED, kind="other",
          note="the number is glued to the word - 'Table10:' with no space, the only caption "
               "in the paper that does so. Ten languages against L1 speakers, total speakers "
               "and an endogenous-growth column holding signed percentages that pass 100 and "
               "go negative (Hindustani 193.4%, Arabic 278.5%, Russian -33.0%), with two "
               "languages left blank and a dash for the reference row"),
    table("t11",
          cap("Table 11: Sensitivity Analysis on", "Table N:"),
          mention(13, first=None, style=[]),
          grid(8, 5, numeric=4, txt=1, decimal=True),
          path=S_SENS, kind="sensitivity",
          note="seven delta values against the equilibrium, the 50-year L1 prediction and two "
               "bias columns, one of them a dash for the central case. The caption stops at "
               "'on' because the symbol it modifies never printed, so the table's subject is "
               "only recoverable from the paper text above it"),
]
B.update({
    "t12": bb(14, 1),
    "f12b": bb(14, 2),
    "f13": bb(14, 3),
    "f14a": bb(15, 1),
    "f14b": bb(15, 2),
    "t13": bb(15, 3),
    "f15": bb(17, 2),
    "f16": bb(17, 3),
    "f17a": bb(18, 1),
    "f17b": bb(18, 2),
    "f17c": bb(18, 3),
    "f17d": bb(18, 4),
    "t14": bb(18, 5),
    "f18a": bb(19, 1),
    "f18b": bb(19, 2),
    "f18c": bb(19, 3),
    "f18d": bb(19, 4),
    "t15": bb(20, 2),
    "t16": bb(20, 3),
    "f19": bb(21, 2),
    "f20": bb(21, 3),
    "f21": bb(21, 4),
    "f22": bb(22, 1),
    "f23": bb(22, 2),
})

EXCLUDED += [
    ("p7 equations (4)-(6), the FPE/AIC/BIC criteria", bb(7, 2), "not-an-exhibit"),
    ("p7 equation (8), the co-integration relation", bb(7, 4), "not-an-exhibit"),
    ("p8 the ECM derivation and equation (9)", bb(8, 1), "not-an-exhibit"),
    ("p10 equation (13), logistic growth", bb(10, 2), "not-an-exhibit"),
    ("p11 equation (16), the piecewise total-speaker system", bb(11, 1), "not-an-exhibit"),
    ("p11 the d2N/dt2 boundary conditions", bb(11, 2), "not-an-exhibit"),
    ("p16 equation (27), the 226x226 transition matrix", bb(16, 1), "not-an-exhibit"),
    ("p16 equations (1)-(2) and (28), the n-step matrix", bb(16, 2), "not-an-exhibit"),
    ("p16 equations (29)-(31), the population recursion", bb(16, 3), "not-an-exhibit"),
    ("p16 equation (32) and the steady-state product", bb(16, 4), "not-an-exhibit"),
    ("p17 equation (33), the M0 matrix", bb(17, 1), "not-an-exhibit"),
    ("p20 equation (45), the fuzzy relation matrix", bb(20, 1), "not-an-exhibit"),
    ("p21 equations (48)-(51), the density and MIC definitions", bb(21, 1),
     "not-an-exhibit"),
]

FIGURES += [
    figure("f12b",
           cap("Figure 12: Comprehensive Sensitivity Analysis for Mandarin Chinese"),
           mention(14, first=None, style=[]),
           geo("composite-panel", panels=4, layout="1x4", legend="inside"),
           path=S_SENS, kind="sensitivity",
           note="four line panels in a row under inline titles mu=3, mu=3.2, mu=3.4, mu=2.7, "
                "each with its own in-box key of four sigma values and its own ordinate - the "
                "third panel reaches 6000 where the others stop at 5000. The number 12 is "
                "printed a second time here, four pages after Figure 12 on page 13"),
    figure("f13",
           cap("Figure 13: Sensitivity Analysis on Initial Value of N for Russian Model"),
           mention(14, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_SENS, kind="sensitivity",
           note="Time 0-100 against 70-160 for the L2 speakers of Russian, four curves keyed "
                "N(0)=153/160/150/140. The tight ordinate is the point of the figure - four "
                "initial values converging on one plateau"),
    figure("f14a",
           cap("Figure 14: Monte Carlo Simulation on L1 Speakers and Total Speakers for "
               "Mandarin Chinese"),
           mention(15, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_SENS, kind="sensitivity",
           note="left panel of a two-panel Monte Carlo plate: L1 speakers 850-1100 with four "
                "curves keyed sigma=5/7/9 plus the deterministic origin. One caption covers "
                "both panels, and the caption is the only thing that says 'Monte Carlo' - the "
                "panels themselves are plain line plots like all the others"),
    figure("f14b",
           cap("Figure 14: Monte Carlo Simulation on L1 Speakers and Total Speakers for "
               "Mandarin Chinese"),
           mention(15, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_SENS, kind="sensitivity",
           note="right panel of the same plate: total speakers 1000-1600, four curves keyed "
                "by a PAIR of sigmas (sN=3,sS=1 / sN=5,sS=1.5 / sN=7,sS=2) plus the origin. "
                "Printed as two separate measured regions because the two frames never touch"),
    figure("f15",
           cap("Figure 15: Share of population born abroad of Each Country (Visualized "
               "Moving-in Matrix M0 )"),
           mention(17, first=None, style=[]),
           geo("map-or-plan-view", legend="inside", numbers=False),
           path=S_LDIST, kind="other",
           note="the paper's only map: a world choropleth of the share of population born "
                "abroad, class breaks in a six-entry legend box inside the frame "
                "(0~2.5 / 2.51~5.0 / 5.01~16.0 / 10.01~50.0 / 50.01~90 / no data). The third "
                "and fourth classes overlap - 10.01~50.0 sits inside 5.01~16.0 - so the "
                "legend cannot be read as a partition. No axes, no scale bar, no country "
                "labels"),
    figure("f16",
           cap("Figure 16: Visualize G by The Mobile Average Data of Population Naturally "
               "Growth Rate (2005-2016 Partially）"),
           mention(17, first=None, style=[]),
           geo("bar", legend="none"),
           path=S_LPRED, kind="other",
           note="horizontal bars, country names down the left (Russian Federation, Cyprus, "
                "Andorra, Ireland, Netherlands Antilles, Saint Lucia, Panama, Falkland "
                "Islands, Greenland, India, Malaysia, Vanuatu, New Caledonia, Australia) "
                "against an unlabelled 0-0.12 axis, two bars per country in two tones of blue "
                "with no key. The closing bracket of the caption is full-width while the "
                "opening one is ASCII"),
    figure("f17a",
           cap("Figure 17: Geographic Distribution of Mandarin Chinese in The Next 50 Years"),
           mention(18, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_LPRED, kind="other",
           note="panel one of four: a MATLAB surface of total speakers against longitude and "
                "latitude with a flat 'Lands' swatch in the lower left and the year 2017 "
                "printed under the frame. Each of the four panels is a separately rendered "
                "image with its own axes box and legend, laid in a row under one caption"),
    figure("f17b",
           cap("Figure 17: Geographic Distribution of Mandarin Chinese in The Next 50 Years"),
           mention(18, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_LPRED, kind="other",
           note="panel two of four, year 2027. Same camera, same z scale, same lands swatch - "
                "the only difference from panel one is the year label and the height of the "
                "ridge over east Asia"),
    figure("f17c",
           cap("Figure 17: Geographic Distribution of Mandarin Chinese in The Next 50 Years"),
           mention(18, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_LPRED, kind="other",
           note="panel three of four, year 2037"),
    figure("f17d",
           cap("Figure 17: Geographic Distribution of Mandarin Chinese in The Next 50 Years"),
           mention(18, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_LPRED, kind="other",
           note="panel four of four, year 2067. The four years 2017/2027/2037/2067 are the "
                "only labels that distinguish the panels; the caption names none of them"),
    figure("f18a",
           cap("Figure 18: Cluster Dendrograms for 4 Vectors of Variables when t=5"),
           mention(19, first=None, style=[]),
           geo("node-link-network", legend="none"),
           path=S_CLUST, kind="model",
           note="first of four square dendrograms: a threshold tree over the samples of one "
                "vector, y axis 0-200000 with no axis titles, no legend, one printed leaf "
                "label. The four panels sit in a row under one caption and differ only in "
                "the vector they cluster"),
    figure("f18b",
           cap("Figure 18: Cluster Dendrograms for 4 Vectors of Variables when t=5"),
           mention(19, first=None, style=[]),
           geo("node-link-network", legend="none"),
           path=S_CLUST, kind="model",
           note="second dendrogram, y axis in scientific notation 0.0e+00 to 1.2e+06, one "
                "leaf label"),
    figure("f18c",
           cap("Figure 18: Cluster Dendrograms for 4 Vectors of Variables when t=5"),
           mention(19, first=None, style=[]),
           geo("node-link-network", legend="none"),
           path=S_CLUST, kind="model",
           note="third dendrogram, y axis 0.0e+00 to 8.0e+03 - three orders of magnitude "
                "below its neighbours, which is why the four thresholds cannot be compared "
                "at a glance"),
    figure("f18d",
           cap("Figure 18: Cluster Dendrograms for 4 Vectors of Variables when t=5"),
           mention(19, first=None, style=[]),
           geo("node-link-network", legend="none"),
           path=S_CLUST, kind="model",
           note="fourth dendrogram, plain 0-8 axis, the only one whose scale is readable "
                "without the exponent"),
    figure("f19",
           cap("Figure 19: Distribution of MIC for Short-term Samples"),
           mention(21, first=None, style=[]),
           geo("surface-or-3D", legend="outside-right", three_d="surface-mesh"),
           path=S_MINE, kind="model",
           note="MIC against longitude and latitude, z 0.5-1, with a banner legend outside "
                "the frame ('MIC vs. Longitude, Altitude'). Printed to the RIGHT of Figure 20 "
                "though it carries the lower number, so the pair runs 20 then 19 across the "
                "page"),
    figure("f20",
           cap("Figure 20: Geographic Distribution of 8"),
           mention(21, first=None, style=[]),
           geo("scatter", legend="inside", labels=True, numbers=False),
           path=S_MINE, kind="model",
           note="a schematic rather than a plot: eight offices and economic centres marked "
                "on a dashed lat/long frame with unnumbered arrows for axes, a two-entry key "
                "inside the right edge, nine inline city labels (Ottawa, New York, London, "
                "Paris, Tokyo, Shanghai, HK, Singapore, Canberra). The caption breaks after "
                "'of 8' because 'Offices and Economic Centers' is printed after Figure 19's "
                "caption line in the text layer"),
    figure("f21",
           cap("Figure 21: Distribution of MIC after Improving"),
           mention(21, first=None, style=[]),
           geo("surface-or-3D", legend="outside-right", three_d="surface-mesh"),
           path=S_MINE, kind="model",
           note="the same MIC surface re-plotted after two offices are removed, z 0-1 against "
                "Figure 19's 0.5-1. This is the only before/after pair in the paper that "
                "changes the number of data points as well as the picture"),
    figure("f22",
           cap("Figure 22: Distribution of MIC for Original Plan"),
           mention(22, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_MINE, kind="model",
           note="left half of a two-surface plate closing the MINE section: MIC 0.5-1 with "
                "the legend box inside the frame at top right, against Figure 23's 0.2-1. The "
                "two surfaces differ only in the ordinate window, which makes the improvement "
                "look larger than the data does"),
    figure("f23",
           cap("Figure 23: Distribution of MIC for New Plan in Long-term"),
           mention(22, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_MINE, kind="model",
           note="right half of the same plate, z 0.2-1"),
]

TABLES += [
    table("t12",
          cap("Table 12: Sensitivity Analysis on μ", "Table N:"),
          mention(14, first=None, style=[]),
          grid(8, 4, numeric=3, txt=1, units_in_header=True),
          path=S_SENS, kind="sensitivity",
          note="seven mu values against the 50-year L2 prediction, the 50-year total "
               "prediction and a bias column. The header carries the horizon inside the "
               "column names ('Prediction of L2 Speakers (50 Years)'), which is the only "
               "place in the paper where a header states a time span instead of a quantity, "
               "and the bias column prints a dash for the central case"),
    table("t13",
          cap("Table 13: Variables for Model 2"),
          mention(15, first=None, style=[]),
          grid(11, 2, numeric=0, txt=2, merged=True, rule="boxed"),
          path=S_MKVARS, kind="symbols",
          note="eleven rows of symbol against definition, fully boxed. Only two symbols "
               "survive into the render - a lone 'P' and 'I, J' - and the definitions keep "
               "their prose but lose every inline glyph ('Matrix formed by [blank]'), so the "
               "table states what the model needs without naming half of it"),
    table("t14",
          cap("Table 14: Difference Between Predictions of 2 Models"),
          mention(18, first=None, style=[]),
          grid(11, 4, numeric=3, txt=1, decimal=True),
          path=S_M2CMP, kind="model",
          note="ten languages against the Markov prediction, the differential-model "
               "prediction and the signed difference. It is the paper's one reconciliation "
               "grid: both models' numbers for the same year sit in adjacent columns, and "
               "the difference column runs from -73 to 165"),
    table("t15",
          cap("Table 15: Short-term results"),
          mention(20, first=None, style=[]),
          grid(7, 6, header=1, numeric=4, txt=2, rule="boxed"),
          path=S_M3SET, kind="solution",
          note="six countries against a composite score, capital city, English and Chinese "
               "speaker proportions and GDP per capital. Fully boxed, the heaviest ruling in "
               "the body after Table 4"),
    table("t16",
          cap("Table 16: Long-term results"),
          mention(20, first=20, style=["table 16"], count=1,
                  lead="the top 6 countries are shown in the table 16",
                  pattern="as-shown-in"),
          grid(7, 5, header=1, numeric=3, txt=2, rule="boxed"),
          path=S_M3SET, kind="solution",
          note="the long-horizon twin of Table 15, five columns instead of six - the GDP "
               "column is dropped - and a different six countries. It is the only exhibit in "
               "the paper announced in prose before it prints, and the announcement "
               "lower-cases the label: 'shown in the table 16'"),
]
B.update({
    "fx": bb(24, 1),
    "a_hn": bb(26, 1),
    "a_sp": bb(26, 2),
    "a_ml": bb(26, 5),
    "a_ar": bb(26, 6),
    "a_ru": bb(26, 9),
    "a_bn": bb(26, 10),
    "a_fre": bb(26, 13),
    "a_pt": bb(26, 14),
    "t27": bb(27, 2),
    "t28": bb(28, 1),
    "t29a": bb(29, 1),
    "t29b": bb(29, 2),
    "f5app": bb(30, 1),
    "t30m": bb(30, 2),
    "t30e": bb(30, 3),
    "t30s": bb(30, 4),
    "t31a": bb(31, 1),
    "t31r": bb(31, 2),
    "t31f": bb(31, 3),
    "f31pt": bb(31, 4),
    "f31en": bb(31, 5),
    "f32ar": bb(32, 1),
    "f32sp": bb(32, 2),
    "f32hi": bb(32, 3),
    "f32fr": bb(32, 4),
    "f32mu": bb(32, 5),
    "f33sp": bb(33, 1),
    "f33pt": bb(33, 2),
    "t35": bb(35, 1),
    "f37en17": bb(37, 2),
    "f37en67": bb(37, 3),
    "f37es": bb(37, 4),
    "f38fr17": bb(38, 1),
    "f38fr67": bb(38, 2),
    "f38de": bb(38, 3),
    "t38": bb(38, 4),
    "t39a": bb(39, 1),
})

EXCLUDED += [
    ("p26 caption band of the Hindustani correlogram", bb(26, 3), "not-an-exhibit"),
    ("p26 caption band of the Spanish correlogram", bb(26, 4), "not-an-exhibit"),
    ("p26 caption band of the Arabic correlogram", bb(26, 7), "not-an-exhibit"),
    ("p26 caption band of the Malay correlogram", bb(26, 8), "not-an-exhibit"),
    ("p26 caption band of the Russian correlogram", bb(26, 11), "not-an-exhibit"),
    ("p26 caption band of the Bengali correlogram", bb(26, 12), "not-an-exhibit"),
    ("p27 left column slice of the appendix 2 panel table", bb(27, 1), "not-an-exhibit"),
    ("p27 middle column slice of the appendix 2 panel table", bb(27, 3), "not-an-exhibit"),
    ("p27 right column slice of the appendix 2 panel table", bb(27, 4), "not-an-exhibit"),
    ("p28 left column slice of Table2", bb(28, 2), "not-an-exhibit"),
    ("p28 middle column slice of Table2", bb(28, 3), "not-an-exhibit"),
]

FIGURES += [
    figure("fx",
           cap("Figure: Appropriate Locations of International Offices According to New Plan",
               "none"),
           mention(24, first=None, style=[]),
           geo("map-or-plan-view", legend="outside-right", labels=True, numbers=False),
           path=S_RESULTS, kind="result",
           note="the only figure in the paper with NO NUMBER - the caption is the bare word "
                "'Figure' followed by a colon, printed under a schematic lon/lat frame with "
                "numbered axes at the origin only, a four-entry key outside the right edge "
                "(Office in short-term / World Economic Center / Original Office / Office in "
                "long-term) and nine hand-placed city labels. It sits in the memo, after the "
                "recommendation it illustrates, and it is the second map of office locations "
                "after Figure 20"),
    figure("a_hn",
           cap("Autocorrelation and Partial Correlation of Hindustani", "none"),
           mention(26, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_APPX, kind="appendix",
           note="Appendix 1, first of eight EViews correlograms: ACF bars, PACF bars and a "
                "twelve-lag statistics grid. No figure number and no caption number - the "
                "language name IS the caption"),
    figure("a_sp",
           cap("Autocorrelation and Partial Correlation of Hindustani Spanish", "none"),
           mention(26, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_APPX, kind="appendix",
           note="second correlogram, Spanish. Captions print in pairs across the two columns, "
                "so the language word of the right-hand panel falls after the left-hand "
                "panel's title on the text layer; the quoted string is the pair as printed "
                "and the panel belongs to Spanish"),
    figure("a_ml",
           cap("Autocorrelation and Partial Correlation of Arabic Malay", "none"),
           mention(26, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_APPX, kind="appendix",
           note="fifth measured region, the Malay correlogram; quoted as the printed pair "
                "'Arabic Malay' for the same two-column reason"),
    figure("a_ar",
           cap("Autocorrelation and Partial Correlation of Arabic", "none"),
           mention(26, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_APPX, kind="appendix",
           note="the Arabic correlogram, the left-hand panel of the second row"),
    figure("a_ru",
           cap("Autocorrelation and Partial Correlation of Russian", "none"),
           mention(26, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_APPX, kind="appendix",
           note="third row, left panel"),
    figure("a_bn",
           cap("Autocorrelation and Partial Correlation of Russian Bengali", "none"),
           mention(26, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_APPX, kind="appendix",
           note="third row, right panel: Bengali, quoted as the printed pair"),
    figure("a_fre",
           cap("Autocorrelation and Partial Correlation of Portuguese FRE", "none"),
           mention(26, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_APPX, kind="appendix",
           note="fourth row, right panel, captioned 'FRE' - the paper's abbreviation for "
                "French, used nowhere else; quoted as the printed pair"),
    figure("a_pt",
           cap("Autocorrelation and Partial Correlation of Portuguese", "none"),
           mention(26, first=None, style=[]),
           geo("composite-panel", panels=3, layout="1x3"),
           path=S_APPX, kind="appendix",
           note="fourth row, left panel"),
    figure("f5app",
           cap("Figure 5: Analysis Simulation for Prediction Error of Marinda Chinese "
               "(Variance of Error Versus Prediction Step-length=1:50)"),
           mention(30, first=None, style=[]),
           geo("line", legend="none"),
           path=S_APPX, kind="appendix",
           note="a single open-circle series rising nearly linearly from 0 to about 140 over "
                "fifty steps, no axis titles at all, no key, horizontal gridlines only. The "
                "caption calls it Figure 5, the number Figure 5 already carries six pages "
                "earlier in the body, and it misspells Mandarin as 'Marinda'"),
    figure("f31pt",
           cap("Appendix 7 Number of Speakers Versus Time for Each Language", "none",
               position="above"),
           mention(31, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_APPX, kind="appendix",
           note="one cell of the six-language small-multiple set of Appendix 7, title "
                "Portuguese printed above: Time 0-1000 against 0-3000, three series keyed "
                "L1, L2, Total - except the key prints 'L1' twice, so the middle curve's "
                "identity is lost. The cell is visually identical to the French cell on the "
                "next page"),
    figure("f31en",
           cap("Appendix 7 Number of Speakers Versus Time for Each Language", "none",
               position="above"),
           mention(31, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_APPX, kind="appendix",
           note="the English cell, ordinate 0 to about 12000 with garbled and overlapping "
                "tick labels (12700, 10303, 8000), key L1/L2/Total in the upper left"),
    figure("f32ar",
           cap("Appendix 7 Number of Speakers Versus Time for Each Language", "none",
               position="above"),
           mention(32, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_APPX, kind="appendix",
           note="the Arabic cell: the only one of the six whose x range is 0-100 instead of "
                "0-1000, and the only one where L2 declines (130 to 40) while L1 rises"),
    figure("f32sp",
           cap("Appendix 7 Number of Speakers Versus Time for Each Language", "none",
               position="above"),
           mention(32, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_APPX, kind="appendix",
           note="the Spanish cell, 0-7000 with L2 flat near 1100"),
    figure("f32hi",
           cap("Appendix 7 Number of Speakers Versus Time for Each Language", "none",
               position="above"),
           mention(32, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_APPX, kind="appendix",
           note="the Hindustani cell, x 0-100, y 0-900"),
    figure("f32fr",
           cap("Appendix 7 Number of Speakers Versus Time for Each Language", "none",
               position="above"),
           mention(32, first=None, style=[]),
           geo("line", legend="inside"),
           path=S_APPX, kind="appendix",
           note="the French cell, pixel-for-pixel the same shape as the Portuguese cell on "
                "page 31, including the doubled 'L1' key entry"),
    figure("f32mu",
           cap("Appendix 8 Sensitivity Analysis Results of Each Language", "none",
               position="above"),
           mention(32, first=None, style=[]),
           geo("composite-panel", panels=4, layout="2x2", legend="inside"),
           path=S_APPX, kind="appendix",
           note="the English sensitivity plate: a shared Time 0-1000 by 0-15000 frame split "
                "four ways, subplot titles mu=9, mu=8, mu=9.5, mu=10, key (sigma=0.007, 0.005, "
                "0.003, 0.009) in the first subplot only"),
    figure("f33sp",
           cap("Appendix 8 Sensitivity Analysis Results of Each Language", "none",
               position="above"),
           mention(33, first=None, style=[]),
           geo("composite-panel", panels=4, layout="2x2", legend="inside"),
           path=S_APPX, kind="appendix",
           note="the Spanish plate, subplot titles mu=5, mu=5.5, mu=4.5, mu=4, key only in "
                "the top-left panel. Captions for the appendix plates are carried by the "
                "Appendix heading alone - no panel has a line of its own"),
    figure("f33pt",
           cap("Appendix 8 Sensitivity Analysis Results of Each Language", "none",
               position="above"),
           mention(33, first=None, style=[]),
           geo("composite-panel", panels=4, layout="2x2"),
           path=S_APPX, kind="appendix",
           note="the Portuguese plate, subplot titles mu=2, mu=2.5, mu=3, mu=3.5, ordinate "
                "0-3000, no key at all in any of the four panels - the only plate in the set "
                "without one"),
    figure("f37en17",
           cap("Appendix 13 3D Image of the Number of Particular Language Speakers – "
               "Geographic Distribution", "none", position="above"),
           mention(37, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_APPX, kind="appendix",
           note="English 2017 surface, longitude -150 to 150 against latitude -60 to 60, z to "
                "2.5x10^3, black dot markers sitting on the surface, banner legend inside the "
                "top of the frame, year printed under the panel"),
    figure("f37en67",
           cap("Appendix 13 3D Image of the Number of Particular Language Speakers – "
               "Geographic Distribution", "none", position="above"),
           mention(37, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_APPX, kind="appendix",
           note="English 2067, the same template with the exponent clipped by the region edge"),
    figure("f37es",
           cap("Appendix 13 3D Image of the Number of Particular Language Speakers – "
               "Geographic Distribution", "none", position="above"),
           mention(37, first=None, style=[]),
           geo("composite-panel", panels=2, layout="1x2", legend="inside",
               three_d="surface-mesh"),
           path=S_APPX, kind="appendix",
           note="Spanish printed as a two-panel band 2017 against 2067 with the language "
                "heading below, z 8x10^7 and 10x10^7; the left panel's legend banner and "
                "axis overlap the frame and the panel titles are cropped out"),
    figure("f38fr17",
           cap("Appendix 13 3D Image of the Number of Particular Language Speakers – "
               "Geographic Distribution", "none", position="above"),
           mention(38, first=None, style=[]),
           geo("surface-or-3D", legend="inside", three_d="surface-mesh"),
           path=S_APPX, kind="appendix",
           note="French 2017, z to 12x10^7, language heading below the panel"),
    figure("f38fr67",
           cap("Appendix 13 3D Image of the Number of Particular Language Speakers – "
               "Geographic Distribution", "none", position="above"),
           mention(38, first=None, style=[]),
           geo("surface-or-3D", legend="outside-left", three_d="surface-mesh"),
           path=S_APPX, kind="appendix",
           note="French 2067, z to 2.5x10^8 - an order of magnitude above its 2017 twin - "
                "and the only surface in the paper whose legend box is cut off at the left "
                "edge of the measured region"),
    figure("f38de",
           cap("Appendix 13 3D Image of the Number of Particular Language Speakers – "
               "Geographic Distribution", "none", position="above"),
           mention(38, first=None, style=[]),
           geo("composite-panel", panels=2, layout="1x2", legend="inside",
               three_d="surface-mesh"),
           path=S_APPX, kind="appendix",
           note="German as a two-panel band 2017 against 2067, green surface instead of the "
                "jet palette every other surface uses, z 0-150 against 0-80"),
]

TABLES += [
    table("t27",
          cap("Appendix 2 Data for the Short-term Model of Non-native Speaker in Model 1",
              "none", position="above"),
          mention(27, first=None, style=[]),
          grid(54, 8, header=1, numeric=5, txt=3, merged=True, rule="boxed", decimal=True,
               units_in_header=True),
          path=S_APPX, kind="appendix",
          note="a pasted World Bank panel: nine year blocks 2008-2016, six languages per "
               "block, year merged down its six rows, eight columns from the country through "
               "GDP per capita to the Gini coefficient and the Gross National Happiness "
               "Index. Units live inside the header ('(per capita)'). Source line under the "
               "grid: 'Data Source: The World Bank Database'"),
    table("t28",
          cap("Table2: Formed Panel by factors influencing the number of non-native speakers "
              "in2008-2016", "Table N:", units=True),
          mention(28, first=None, style=[]),
          grid(54, 8, header=1, numeric=5, txt=3, merged=True, rule="boxed", decimal=True,
               units_in_header=True),
          path=S_APPX, kind="appendix",
          note="the appendix twin of Table 2 and the second table in the paper to print its "
               "number glued to the word - 'Table2:' with no space, duplicating a number the "
               "body already used. Same 54-row panel shape as Appendix 2 with different "
               "variables (migrants, labour productivity, CPI, tourism income, transaction "
               "software), a note row naming all ten units, and the same World Bank source "
               "line"),
    table("t29a",
          uncap("above"),
          mention(29, first=None, style=[]),
          grid(9, 10, header=2, numeric=9, txt=1, merged=True, rule="boxed", decimal=True),
          path=S_APPX, kind="appendix", caption_source="none",
          note="Appendix 3, the Engel-Granger critical values, printed as two stacked boxes "
               "under the raster-only title 'Engel-Granger cointegration critical values' - "
               "that title never reaches the text layer, so this grid has no quotable "
               "caption. Three spanner groups (no constant or trend / constant but no trend / "
               "constant and trend) over 1%, 5%, 10%, with the first group's cells left blank "
               "in both blocks and the label column empty for every row"),
    table("t29b",
          cap("Appendix 4 Error Correction Terms of Each Language", "none", position="above"),
          mention(29, first=None, style=[]),
          grid(9, 7, header=1, numeric=6, txt=1, decimal=True),
          path=S_APPX, kind="appendix",
          note="eight ECM years 2008-2015 against six languages, horizontal rules only, bold "
               "header. It is the only table in the appendix that is typeset rather than "
               "pasted, and its numbers reappear nowhere else in the paper"),
    table("t30m",
          uncap("below"),
          mention(30, first=None, style=[]),
          grid(6, 3, numeric=2, txt=1, decimal=True),
          path=S_APPX, kind="appendix", caption_source="none",
          note="Appendix 6, first of six EViews panel unit-root dumps: statistic name, "
               "statistic, probability, under the language label Mandarin Chinese. No caption "
               "line of its own - the Appendix heading covers all six"),
    table("t30e",
          uncap("below"),
          mention(30, first=None, style=[]),
          grid(6, 3, numeric=2, txt=1, decimal=True),
          path=S_APPX, kind="appendix", caption_source="none",
          note="the English dump, same five statistics as the Mandarin block"),
    table("t30s",
          uncap("below"),
          mention(30, first=None, style=[]),
          grid(6, 3, numeric=2, txt=1, decimal=True),
          path=S_APPX, kind="appendix", caption_source="none",
          note="the Spanish dump"),
    table("t31a",
          uncap("below"),
          mention(31, first=None, style=[]),
          grid(6, 3, numeric=2, txt=1, decimal=True),
          path=S_APPX, kind="appendix", caption_source="none",
          note="the Arabia dump - the label misspells the continent for the language, and it "
               "is the only one of the six that also prints a Breitung statistic"),
    table("t31r",
          uncap("below"),
          mention(31, first=None, style=[]),
          grid(6, 3, numeric=2, txt=1, decimal=True),
          path=S_APPX, kind="appendix", caption_source="none",
          note="the Russian dump"),
    table("t31f",
          uncap("below"),
          mention(31, first=None, style=[]),
          grid(6, 3, numeric=2, txt=1, decimal=True),
          path=S_APPX, kind="appendix", caption_source="none",
          note="the French dump, the last of the six; every language block is a separate "
               "measured region because the raster has a frame per language"),
    table("t35",
          cap("Appendix 10 Part of One-Step Transition Probability Matrix", "none",
              position="above"),
          mention(35, first=None, style=[]),
          grid(63, 11, header=1, numeric=10, txt=1, decimal=True),
          path=S_APPX, kind="appendix",
          note="sixty-three origin countries against eleven Pacific state codes, every cell a "
               "transition probability in scientific notation, row labels merged two columns "
               "(name plus ISO code). The rows are the only part of the 226x226 matrix the "
               "appendix shows, and they are all Pacific and east Asian - the sample the "
               "model actually uses"),
    table("t38",
          uncap("above"),
          mention(38, first=None, style=[]),
          grid(4, 6, header=1, numeric=5, txt=1, decimal=True),
          path=S_APPX, kind="appendix", caption_source="none",
          note="Appendix 14, a three-row ANOVA output (Columns / Error / Total against SS, "
               "df, MS, F, Prob>F) with F=0.01 and p=0.9437 - the paper's own test that the "
               "two models' predictions do not differ. No caption reaches the text layer; "
               "only the Appendix heading survives"),
    table("t39a",
          cap("Appendix 15 Score for Model 3 of Each Countries", "none", position="above"),
          mention(39, first=None, style=[]),
          grid(39, 5, header=1, numeric=4, txt=1),
          path=S_APPX, kind="appendix",
          note="thirty-nine countries against their integer class assignment in four "
               "groupings G1-G4, the raw scores the clustering turned into the office "
               "decisions. Integer cells are centred rather than decimal-aligned, which is "
               "why this grid cannot be read as a numeric table at a glance"),
]
B.update({
    "t34": bb(34, 1),
    "t36": bb(36, 1),
    "t37": bb(37, 1),
    "t39b": bb(39, 2),
})

TABLES += [
    table("t34",
          cap("Appendix 9 Part of Matrix Formed by the Number of Migrant in Different "
              "Countries", "none", position="above"),
          mention(34, first=None, style=[]),
          grid(83, 16, header=1, numeric=15, txt=1, rule="boxed"),
          path=S_APPX, kind="appendix",
          note="the migrant-count matrix: 83 printed rows of origin countries against fifteen "
               "destination-state columns, framed cell by cell, with a source line 'Data "
               "Source: The Global Migrant Origin Database' under it. The page break clips an "
               "eighty-fourth row mid-height and the table continues past the bottom of the "
               "page. Unlike the probability matrix of Appendix 10 the cells are absolute "
               "counts, so the widest numbers sit in the same column as zeroes, and no "
               "column of digits is aligned on anything"),
    table("t36",
          cap("Appendix 11 Part of Population of countries in decades", "none",
              position="above"),
          mention(36, first=None, style=[]),
          grid(35, 5, header=1, numeric=4, txt=1, rule="boxed"),
          path=S_APPX, kind="appendix",
          note="thirty-five origin countries against four decade columns N1 / N10 / N20 / N50 - "
               "the projected population of each country at four horizons, printed as a pasted "
               "block with a full outer box and no unit in any header cell"),
    table("t37",
          cap("Appendix 12 Part of Latitude and Longitude of Coordinates of Various "
              "National Centers", "none", position="above"),
          mention(37, first=None, style=[]),
          grid(33, 15, header=1, numeric=10, txt=5, rule="vertical-rules"),
          path=S_APPX, kind="appendix",
          note="five Country / Latitude / Longitude blocks side by side on one page, 33 row "
               "positions in all, ruled ONLY vertically - a line between every column and "
               "none between the rows, so the eye reads across a horizontal band instead of "
               "down a column. The header 'Origin Countries | Latitude | Longitude' repeats "
               "over each block, and a 'Data Source: The Wikipedia' line closes the set. It "
               "is the coordinate substrate for the 3D surfaces that follow on the same and "
               "the next two pages"),
    table("t39b",
          uncap("above"),
          mention(39, first=None, style=[]),
          grid(14, 5, header=1, numeric=5, txt=0, rule="boxed"),
          path=S_APPX, kind="appendix", caption_source="none",
          note="the closing vector: seven country-name rows alternating with their seven value "
               "rows across five columns (Australia 0.6, New Zealand 0.69, American Samoa "
               "0.76 ...), boxed cell by cell, with no header row at all - header_rows is "
               "recorded as 1 only because the field has no zero state. Only the Appendix "
               "heading names it, and it is the last thing printed in the paper: the single "
               "number each office site was finally scored on"),
]
ALL: list[dict] = FIGURES + TABLES

# Reading order: page, then top-to-bottom within the page, left-to-right when two
# exhibits share a row.
_order = sorted(ALL, key=lambda it: (it["page"], round((it["bbox"][1] + it["bbox"][3]) / 2),
                                     it["bbox"][0]))
_page_seen: dict[int, int] = {}
for _i, _it in enumerate(_order, 1):
    _it["place"]["doc_order"] = _i
    _pg = _it["page"]
    _page_seen[_pg] = _page_seen.get(_pg, 0) + 1
    _it["place"]["page_order"] = _page_seen[_pg]

_claimed = {(it["page"], tuple(it["bbox"])) for it in ALL}
_claimed |= {(p, tuple(b)) for _k, (p, b), _r in EXCLUDED}
assert _claimed == MEASURED, (
    f"claimed {len(_claimed)} of {len(MEASURED)} measured regions; "
    f"unclaimed {sorted(MEASURED - _claimed)[:5]} "
    f"phantom {sorted(_claimed - MEASURED)[:5]}")
assert len(ALL) + len(EXCLUDED) == len(MEASURED) == 115

RULES = [
    "Numbering splits the paper in two: 32 of the 56 figures print 'Figure N:' and 24 print "
    "no number at all - the eight Appendix-1 correlograms, the Appendix-7 cells, the "
    "Appendix-8 plates and the Appendix-13 surfaces are captioned by their Appendix heading "
    "- and the numbered half repeats itself, Figure 12 on p13 and again on p14, Figure 5 on "
    "p6 and again on p30, plus one drawing captioned with the bare word 'Figure' and no "
    "number [caption.numbering].",
    "Caption side follows kind and the appendix flips it: 41 of 56 figure captions print "
    "BELOW the artwork, and every one of the 15 that print above is an appendix plate whose "
    "caption is the Appendix heading sitting over the frame; grids split 25 below and 10 "
    "above, the above ones always being the pasted panel tables of Appendices 2, 9, 11 and "
    "12 [caption.position].",
    "Caption length is a caption, not a sentence: figure captions run 6 to 18 words and grid "
    "captions 4 to 14, no caption concludes anything, no caption states a condition or a "
    "parameter range, and not one uses a reporting voice [caption.words].",
    "Units reach the caption exactly three times out of 91: once on the figure side - "
    "Figure 3's '(Unit: Millions)', carried by a single caption of the three it covers but "
    "governing all of them - and twice on the grid side, Table 2's full-width '（Unit: "
    "Millions）' and Table2's ten-unit note row, while the other 88 exhibits put the unit in "
    "an axis title, in a header cell, or nowhere at all [caption.units].",
    "Neither side names its variables: no figure caption names a series or an axis, and no "
    "grid caption names a column. Parameters appear as bare values ('when (δ=-0.1, "
    "Nm=1000)', 'mu=3'), so a caption tells you what the object is and never what it is "
    "made of [caption.variable_count].",
    "Drawing is three idioms plus three singletons: 19 line plots, 17 multi-panel plates, 12 "
    "MATLAB surface meshes, 4 dendrograms, 2 schematic lon/lat maps, 1 bar chart and 1 "
    "scatter schematic. There is no histogram, no box plot, no heatmap, no contour map and "
    "no pie anywhere in the paper, and the only chart a reader could mistake for a heatmap "
    "is the eight-class world map of Figure 15 [geometry.family].",
    "Three dimensions are used for one thing only - a quantity spread over geography: 14 "
    "exhibits leave the plane, the 12 surface figures plus the 2 Appendix-13 plate figures "
    "whose four panels are each a mesh, and all 14 are surfaces over longitude and latitude "
    "in section 4.2 or Appendix 13. Every one is a MATLAB mesh: none isometric, none drawn "
    "as perspective bars, none a 3D scatter. No other section of the paper leaves the plane "
    "[geometry.three_d].",
    "No figure in the paper carries a colourbar: 0 of 56. Height encodes the value and a "
    "single blue-to-red ramp is assumed, so nothing in the frame states what the top of the "
    "surface means in absolute terms [geometry.colorbar].",
    "Keys sit inside the frame or not at all: 32 inside, 17 with no key, 3 above the frame "
    "in the p6 triple, 3 outside right and 1 outside left. The four that put the key outside "
    "the plot area are the only cases where the reader's eye has to leave the marks, and two "
    "of those keys are cut by the measured region [geometry.legend].",
    "Panel grammar has four states and no others: a single frame (39 figures), a 1x3 strip "
    "for a correlogram with its statistics grid (10), a 1x4 or 2x2 block for a parameter "
    "sweep (4), and a 1x2 before/after pair (3). Panel identity is always inline text - "
    "mu=3, 2017, 'Portuguese' - never a panel letter and never a second caption "
    "[geometry.panel_count].",
    "Ruling has three registers and one outlier: 23 grids use booktabs (horizontal rules "
    "only, no box), 11 are fully boxed cell by cell, and exactly one grid is ruled "
    "vertically only - the Appendix-12 coordinate blocks, a line between every column and "
    "none between the rows. No grid is unruled, none is zebra-striped and none carries a "
    "diagonal header [table.rule_style].",
    "Merged cells appear in 6 of 35 grids and always for one of two jobs - a spanner over "
    "grouped columns (Table 2's language families, Table 4's three information criteria, "
    "Appendix 3's three trend specifications) or a label merged down the rows it repeats "
    "(Table 13's symbols, the two 54-row panel tables, Appendix 9's continent headers) - "
    "never for emphasis alone [table.merged_cells].",
    "Header depth is one row in 32 of 35 grids; the three that need two are Table 2, Table 4 "
    "and Appendix 3's critical-value block, which are exactly the three grids that spanner "
    "their own columns [table.header_rows].",
    "Numbers are decimal-aligned in 23 of 35 grids. The 12 exceptions are the grids whose "
    "cells are integers rather than measurements (the migrant-count matrix of Appendix 9, "
    "the population block of Appendix 11, the Appendix-15 score card, the closing evaluation "
    "vector) and the grids whose cells are words ('No Exist', 'Yes', 'Unit Root?', the "
    "coordinate blocks of Appendix 12), which are centred instead [table.decimal_aligned].",
    "A unit reaches a header cell three times only - Table 12's '(50 Years)' inside the "
    "column names, the two panel tables' '(per capita)' - and everywhere else the header "
    "names the quantity and leaves the unit to the note row or to nothing [table."
    "units_in_header].",
    "Every grid runs the full text measure: 35 of 35 are full-width. Nothing in this paper "
    "is typeset for a narrow column, so even the two-column symbol grids of Tables 1 and 13 "
    "spread across the whole page [table.width].",
    "The appendix is where the exhibits are: 41 of the 91 rows sit under the Appendix "
    "heading, against 30 in model sections, 9 in 'other', 6 in sensitivity, 2 symbol grids, "
    "2 solution grids and 1 in the memo's Results. A reader who stops at the body loses half "
    "the drawings [place.section_kind].",
    "No exhibit owns a page: 0 of 91 is alone on its page, and the vertical band splits 29 "
    "top, 43 middle, 19 bottom, so every exhibit is wedged between prose and the next "
    "exhibit [place.solo_page].",
    "Announcement is almost absent: 3 of 91 exhibits are named in prose at all, all three "
    "grids, and two of them are named AFTER they printed - Table 2 and Table 5 are re-read "
    "on p10, four and two pages on. Not one figure is cited by number anywhere in the body "
    "[mention.lead_pages].",
    "Citation vocabulary is one construction: the single prose citation of an exhibit is "
    "as-shown-in ('the top 6 countries are shown in the table 16'), lowercased, and every "
    "other exhibit is reached only through 'as following', 'the graphs' or 'the table' "
    "[mention.lead_pattern].",
    "Reading sentences are stock: 'The graph shows that ...' and 'From the results ...' "
    "repeat verbatim across sections and across exhibit kinds, so what follows a figure is a "
    "template, not an observation [mention.trail_sentence].",
    "Two labels are duplicated and one is missing, and none of it is an extraction artefact: "
    "the paper prints two different Figure 12s, two different Figure 5s and one unnumbered "
    "figure, and the appendix prints a 'Table2' that re-uses a body number with its colon "
    "glued to the word [caption.verbatim].",
]

NOTE = (
    "P-B-2018-74316-1198d12d, 2018 MCM B, Team 74316, 39 PDF pages of which 28 are printed "
    "and one (PDF p9) is blank apart from the shop watermark. 115 measured regions on 32 "
    "pages resolve to 56 figures, 35 grids and 24 exclusions. The exclusions are display "
    "mathematics (11 regions: the FPE/AIC/BIC criteria, the ECM derivation, the 226x226 "
    "transition matrix and its recursion, the M0 matrix, the fuzzy relation, the density and "
    "MIC definitions), repeated caption bands the detector boxed as separate artwork (6 "
    "regions of the Appendix-1 correlograms) and column slices of the two pasted panel "
    "tables (5 regions of Appendix 2 and Table2), which is the first paper in this batch "
    "where the same object is measured several times because the raster is wider than one "
    "region. The paper is a language-population forecast in three models: an autoregressive "
    "short-term model, a logistic long-term model and a Markov migration model, closed by an "
    "office-siting MINE model and a memo. Drawing is MATLAB throughout: 19 line plots, 17 "
    "plates, 14 surfaces, 4 dendrograms, 2 schematic maps, a bar chart and a scatter, with "
    "no colourbar, no heatmap and no contour in the paper, so the three-dimensional surfaces "
    "carry absolute value on height alone. Captions are almost all below their exhibit in "
    "the body and above it in the appendix, never state units, never name a variable, and 24 "
    "of 56 figures have no number at all - the appendix captions its plates with the "
    "Appendix heading. Numbering itself is broken twice over: Figure 12 and Figure 5 are each "
    "printed twice for different drawings, Figure 19 and 20 are printed out of order on p21, "
    "one figure prints no number, and the appendix re-uses 'Table2' with the colon glued to "
    "the word. Announcement is nearly absent: three grids are named in prose and no figure "
    "is, and the two grids that are re-read later are re-read after they printed. Two "
    "coverage gaps. First, half the paper's grids are pasted raster panels (Appendices 2, 9, "
    "10, 11, 12, 15, 16 and Table2) whose text layer keeps only the numbers the OCR could "
    "reach, so their cell counts are read from the printed rows and headers in the render, "
    "not from the text layer. Second, the detector counts one wide raster as three or four "
    "overlapping regions, which forces column slices into the exclusion list and makes the "
    "Appendix-6 unit-root dumps six separate grids where the paper prints one table of six "
    "language blocks."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"page": _p, "bbox": _b, "reason": _r, "note": _k}
        for _k, (_p, _b), _r in EXCLUDED
    ],
    "rules": RULES,
    "note": NOTE,
}


def main() -> int:
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, indent=1, ensure_ascii=False), encoding="utf-8")
    fam: dict[str, int] = {}
    for it in FIGURES:
        fam[it["family"]] = fam.get(it["family"], 0) + 1
    leg: dict[str, int] = {}
    for it in FIGURES:
        leg[it["geometry"]["legend"]] = leg.get(it["geometry"]["legend"], 0) + 1
    zone: dict[str, int] = {}
    for it in ALL:
        zone[it["place"]["page_zone"]] = zone.get(it["place"]["page_zone"], 0) + 1
    kind: dict[str, int] = {}
    for it in ALL:
        kind[it["place"]["section_kind"]] = kind.get(it["place"]["section_kind"], 0) + 1
    lead: dict = {}
    for it in ALL:
        lead[it["mention"]["lead_pages"]] = lead.get(it["mention"]["lead_pages"], 0) + 1
    words = [it["caption"]["words"] for it in FIGURES if it["caption"]["words"]]
    twords = [it["caption"]["words"] for it in TABLES if t_ok(it)]
    print(f"{PID}: figures={len(FIGURES)} tables={len(TABLES)} excluded={len(EXCLUDED)} "
          f"regions={len(MEASURED)}")
    print("fam", dict(sorted(fam.items())))
    print("legend", dict(sorted(leg.items())))
    print("zone", dict(sorted(zone.items())))
    print("kind", dict(sorted(kind.items())))
    print("lead", dict(sorted(lead.items(), key=lambda kv: str(kv[0]))))
    print("figwords", min(words), max(words), words)
    print("tabwords", min(twords), max(twords), twords)
    print("payload", out)
    return 0


def t_ok(t: dict) -> bool:
    return bool(t["caption"]["words"])


if __name__ == "__main__":
    sys.exit(main())
