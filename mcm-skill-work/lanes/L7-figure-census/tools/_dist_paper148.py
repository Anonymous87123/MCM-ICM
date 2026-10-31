"""Hand pass for P-B-2018-73410-069a3764 (2018 MCM B, "Team 73410", language population projection).

28 pages, 47 measured regions on 23 pages. Resolution: 24 exhibit rows (12 figures, 12 grids)
and 23 exclusions. Every exclusion is display mathematics - equations, parameter blocks and the
22x22 / 44x44 matrices. The mathematics is typeset live, not scanned, but `fig_extract.py` boxes
it as a raster region anyway, so this paper is the batch's cleanest case of the detector reading
equations as pictures.

Usage: python -I tools/_dist_paper148.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2018-73410-069a3764"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
MEASURED = {(pg["page"], tuple(r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}

B = {
    "t_sym": (3, [64.8, 471.2, 549.4, 736.18]),
    "f1": (5, [189.6, 205.32, 405.6, 361.68]),
    "f2": (7, [117.6, 157.56, 477.6, 261.72]),
    "t1": (9, [133.56, 142.15, 462.0, 316.28]),
    "t_add": (11, [64.8, 98.52, 529.92, 439.8]),
    "f3": (12, [189.6, 72.0, 405.6, 262.32]),
    "f4": (15, [117.6, 72.0, 477.6, 237.36]),
    "f5": (16, [117.6, 72.0, 477.6, 247.68]),
    "f6": (16, [189.6, 299.88, 405.6, 459.0]),
    "f7": (17, [117.6, 271.68, 477.6, 447.36]),
    "f8": (18, [117.6, 72.0, 477.6, 247.68]),
    "t42": (19, [64.8, 99.12, 535.92, 374.16]),
    "t_a2017": (20, [82.0, 72.48, 547.0, 251.58]),
    "t_a2067": (21, [82.0, 72.48, 479.0, 231.13]),
    "t_memo1": (22, [82.0, 535.0, 517.44, 651.38]),
    "t_memo2": (23, [82.0, 72.48, 545.16, 352.93]),
    "t4": (25, [104.0, 380.48, 492.0, 534.51]),
    "t6": (26, [64.8, 48.5, 530.45, 194.08]),
    "t7": (26, [66.0, 267.55, 529.0, 383.88]),
    "t8": (26, [64.8, 457.4, 542.0, 728.79]),
    "f9": (27, [81.6, 115.68, 513.6, 259.92]),
    "f10": (27, [81.6, 312.72, 513.6, 456.96]),
    "f11": (27, [81.6, 509.76, 513.6, 708.24]),
    "f12": (28, [81.6, 307.8, 513.6, 506.28]),
}

EXCLUDED = {
    "p5 equation (1) as an image": (5, [79.2, 448.44, 518.64, 610.44], "not-an-exhibit"),
    "p6 equation (2)": (6, [207.48, 274.56, 529.92, 308.28], "not-an-exhibit"),
    "p6 equation (3)": (6, [234.48, 354.6, 529.2, 380.88], "not-an-exhibit"),
    "p6 steady-state derivation": (6, [200.04, 442.44, 530.04, 516.72], "not-an-exhibit"),
    "p6 parameter set and matrix": (6, [195.48, 530.64, 529.92, 598.2], "not-an-exhibit"),
    "p6 eigenvalue condition": (6, [230.04, 624.0, 529.2, 691.56], "not-an-exhibit"),
    "p7 equation (7) 22x22 matrix": (7, [91.8, 519.72, 534.96, 600.36], "not-an-exhibit"),
    "p8 rate expressions": (8, [150.48, 176.04, 529.92, 221.76], "not-an-exhibit"),
    "p8 learning-rate ratio": (8, [233.04, 272.88, 529.2, 299.16], "not-an-exhibit"),
    "p8 indifference assumption": (8, [126.48, 372.96, 529.92, 402.24], "not-an-exhibit"),
    "p8 normalized learning rate": (8, [87.48, 459.12, 529.2, 615.12], "not-an-exhibit"),
    "p8 annual learning rate": (8, [228.48, 687.96, 529.2, 720.96], "not-an-exhibit"),
    "p9 eigenvector and eigenvalue": (9, [173.52, 501.48, 531.96, 545.76], "not-an-exhibit"),
    "p12 block transition matrix and (14)-(15)": (12, [65.04, 324.48, 552.84, 722.28],
                                                "not-an-exhibit"),
    "p13 English-only matrix": (13, [65.04, 115.68, 529.8, 339.84], "not-an-exhibit"),
    "p13 exogenous-factor equation": (13, [180.48, 675.84, 529.2, 711.84], "not-an-exhibit"),
    "p14 initial vector": (14, [219.48, 118.56, 535.92, 162.12], "not-an-exhibit"),
    "p14 learning-rate definition": (14, [140.04, 206.16, 535.2, 291.72], "not-an-exhibit"),
    "p14 similarity parameter": (14, [82.56, 355.68, 468.0, 400.68], "not-an-exhibit"),
    "p17 k-exponent modification (17)": (17, [224.64, 180.6, 369.36, 227.88],
                                         "not-an-exhibit"),
    "p18 rating model": (18, [184.56, 662.4, 528.72, 751.68], "not-an-exhibit"),
    "p19 weight coefficients": (19, [64.8, 584.28, 541.56, 730.92], "not-an-exhibit"),
    "p20 2067 weight coefficients": (20, [195.6, 507.84, 416.04, 543.84], "not-an-exhibit"),
}

for _name, (_p, _b, _r) in EXCLUDED.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
for _name, (_p, _b) in B.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B) + len(EXCLUDED) == 47, len(MEASURED)


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    w, h = DIMS[page]
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < h / 3 else ("middle" if mid < 2 * h / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (w * h)
    return {
        "section_path": path,
        "section_numbered": True,
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
         width: str = "full", note: str = "") -> dict:
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
        "continued": False,
        "note_sentence": note,
    }


def table(key: str, caption: dict, men: dict, g: dict, *, path: list[str], kind: str,
          note: str = "", caption_source: str = "text-layer") -> dict:
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
    """A grid the paper prints without any caption line, only a section heading above it."""
    return cap("", "none", position=position)


P_SYM = ["2 Preliminary Model", "2.1 Notations and Symbol Description",
         "2.1.1 Symbol Description"]
P_231 = ["2 Preliminary Model", "2.3 Analysis of the Problem", "2.3.1 N=2 Model"]
P_24 = ["2 Preliminary Model", "2.4 Calculating and Simplifying the Model"]
P_25 = ["2 Preliminary Model", "2.5 The Model Results"]
P_312 = ["3 Modified Model", "3.1 Notations and Symbool Description",
         "3.1.2 Additional Symbol Description"]
P_33 = ["3 Modified Model", "3.3 Analysis of the Problem"]
P_351 = ["3 Modified Model", "3.5 The Model Results",
         "3.5.1 Graph of Population of Different Language Groups"]
P_352 = ["3 Modified Model", "3.5 The Model Results",
         "3.5.2 Graph of the Scale of Migration"]
P_353 = ["3 Modified Model", "3.5 The Model Results",
         "3.5.3 Distribution of Non-native English Speakers"]
P_361 = ["3 Modified Model", "3.6 Sensitivity Analysis", "3.6.1 High Uniformity Scenario"]
P_362 = ["3 Modified Model", "3.6 Sensitivity Analysis", "3.6.2 Low Uniformity Scenario"]
P_42 = ["4 Application of Our Model", "4.2 Symbol Descrption"]
P_431 = ["4 Application of Our Model", "4.3 Calculating and Simplifying",
         "4.3.1 The Year of 2017"]
P_432 = ["4 Application of Our Model", "4.3 Calculating and Simplifying",
         "4.3.2 The Year of 2067"]
P_MEMO = ["6 Memo"]
P_APPA = ["References"]

FIGURES = [
    figure("f1",
           cap("Figure 1: Transition Between Different Groups with Only Two Languages"),
           mention(5, first=5, style=["Figure 1"], count=1,
                   lead="we are able to plot the transition between different groups of people "
                        "(See Figure 1)",
                   pattern="parenthetical"),
           geo("node-link-network", labels=True),
           path=P_231, kind="model",
           note="state-transition graph, not a plot: four circles Y1, Y2, y1, y2 on the corners "
                "of a diamond, each with a self-loop labelled 1+alpha11-beta11, "
                "1+alpha22-beta22, 1-beta33 and 1-beta44, and four directed edges labelled "
                "gamma32, alpha24, alpha13 and gamma41. No axes, no key, no printed numbers - "
                "every quantity in the frame is a symbol, and the same four self-loop labels "
                "reappear verbatim as the diagonal of equation (1) directly above. The drawing "
                "is the whole N=2 model: births on two self-loops, survival on the other two, "
                "and learning on the cross edges"),
    figure("f2",
           cap("Figure 2: Correlation Between the Proportion of Non-native Speakers and Learning "
               "Rate ( )"),
           mention(7, first=7, style=["Figure 2"], count=1,
                   lead="By employing the Matlab, we derive the quantitative influence of "
                        "learning rate on the proportion of non-native speakers.",
                   pattern="none",
                   trail="We can see in (Figure 2), when > 0:021, the proportion of non-native "
                         "speakers",
                   read=3),
           geo("line"),
           path=P_24, kind="model",
           note="one straight trace through the origin: x 'Learning rate(gamma)' 0 to 0.05 in "
                "0.005 steps, y 'Ratio of non-native speakers' 0 to 1.2 in 0.2 steps, plus a "
                "dashed horizontal reference line at 0.5 marking where non-native speakers "
                "outnumber native. No key, no markers, no printed values. The axis title keeps "
                "the symbol (gamma) while the caption loses it - 'Rate ( )' with an empty "
                "bracket pair - so the parameter the paper draws against survives only in the "
                "artwork"),
    figure("f3",
           cap("Figure 3: Example Graph of Transition Between Different Groups in a Bilingual "
               "Model"),
           mention(12, first=11, style=["Figure 3"], count=1,
                   lead="Example graph of transition between different groups in a bilingual "
                        "model with regard to learners and immigrants is shown below (Figure 3):",
                   pattern="as-shown-in"),
           geo("node-link-network", labels=True),
           path=P_33, kind="result",
           note="the eight-state version of Figure 1, drawn as a ring rather than a diamond: "
                "Y1, Y2, y1, y2, W1, W2, S12 and S21 sit on a circle, each with a self-loop, and "
                "the ring edges carry alpha-bar, p12a2, 1/(sigma2 d12), p21a1, r1, r2 and "
                "1/(sigma1 d21). Two edge labels are quotient expressions set as stacked "
                "fractions inside the drawing, which is why this frame measures as one tall "
                "region. No axes, no key. Where Figure 1 split native from non-native, this one "
                "splits each group twice - learners (W) and migrants (S) - which is the whole "
                "claim of the modified model"),
    figure("f4",
           cap("Figure 4: Graph of Population of Top Five Language Groups in the Next Fifty "
               "Years", variables=1),
           mention(15, first=14, style=["Figure 4"], count=1,
                   lead="Through repeated alterations, we can plot the graph of population of "
                        "different language groups in the next fifty years (Figure 4).",
                   pattern="parenthetical"),
           geo("line", labels=True),
           path=P_351, kind="model",
           note="the projection frame of the whole paper: x 'Time/year' 2017 to 2070, y "
                "'Population/(million)' 0 to 1200, one curve per language with the top five "
                "labelled inline (Mandarin, English, Spanish, Arabic, Hindustani) and the other "
                "twenty-one left as an unlabelled bundle between 200 and 300 million. No key "
                "box. The caption announces five groups and the frame draws twenty-six, which "
                "the second caption line admits - '(See in Apendix B for the rest twenty-one "
                "language groups)' - misspelling Appendix. The Mandarin-English crossing around "
                "2050, the paper's central result, is two thin lines touching"),
    figure("f5",
           cap("Figure 5: Graph of the Scale of Migration in the Next Fifty Years (Starting "
               "from the year of 2017)"),
           mention(16, first=15, style=["Figure 5"], count=1,
                   lead="Additionally, we can easily derive the graph of the scale of migration "
                        "starting from the year of 2017 (Figure 5)",
                   pattern="parenthetical"),
           geo("line", labels=True),
           path=P_352, kind="model",
           note="migration volume by destination region: x 'Time/year' with decade ticks from "
                "about 2025 to 2075, y 'Population/million' 0 to 120 in 20 steps, one dominant "
                "S-curve rising from 0 to about 110 for English and four near-zero traces with "
                "'French', 'German' and 'Russian' labelled at their ends. Open axes, no key, no "
                "markers. The prose says only the top four attractive regions are labelled; "
                "those labels sit on the right margin and cannot be separated from each other "
                "at the baseline"),
    figure("f6",
           cap("Figure 6: Distribution of Non-native English Speakers in 2067"),
           mention(16, first=15, style=["Figure 6"], count=1,
                   lead="We can also easily derive the distribution of non-native English "
                        "speakers (Figure 6):",
                   pattern="parenthetical"),
           geo("other", numbers=False, labels=True),
           path=P_353, kind="model",
           other_note="pie chart - no FAMILIES member covers a circular share-of-total diagram, "
                      "and it is neither a bar nor a map: eleven wedges labelled outside the "
                      "circle",
           note="the paper's only pie chart and its only exhibit without axes: eleven wedges "
                "(Mandarin, Others, Spanish, Hindustani, Arabic, Bengali, Portuguese, Punjabi, "
                "Russian, Hausa, Japanese) labelled outside the circle in slice colour, with no "
                "percentages, no values and no key. Two wedges are near-identical greys, so the "
                "ordering is recoverable only from the label text. The caption calls it a "
                "distribution 'in 2067' while the prose reads it as a statement about geography"),
    figure("f7",
           cap("Figure 7: Graph of Population of Different Language Groups When k=0.1"),
           mention(17, first=17, style=["Figure 7"], count=1,
                   lead="The initial model adopts k = 1, and when k = 0:1, the graph of population "
                        "of different language groups are as follows: (Figure 7).",
                   pattern="parenthetical"),
           geo("line", legend="outside-right"),
           path=P_361, kind="sensitivity",
           note="the high-uniformity sensitivity run: twenty-six curves on x 'Time/year' 2010 to "
                "2070 and y 'Population/million' 0 to 1200, identified only by a bordered "
                "twenty-six-entry key placed OUTSIDE the plotting area at the upper right. At "
                "print size the key is a grey blur and the bottom eighteen curves merge into one "
                "band below 350 million, so the exhibit's message - that English no longer "
                "overtakes Mandarin when learning is more evenly distributed - has to be taken "
                "from the prose beside it"),
    figure("f8",
           cap("Figure 8: Graph of Population of Different Language Groups When k=10"),
           mention(18, first=17, style=["Figure 8"], count=1,
                   lead="When k = 10, the graph of population of different language groups is as "
                        "follows (Figure 8).",
                   pattern="parenthetical"),
           geo("line", legend="outside-right"),
           path=P_362, kind="sensitivity",
           note="the low-uniformity twin of Figure 7, printed a page later with the same frame, "
                "the same twenty-six-entry outside key and only the y top changed (0 to 1500 "
                "against 0 to 1200) - which is how the reader is meant to see English rocketing. "
                "The pair is the paper's only sensitivity evidence and the only place a "
                "parameter change is shown as two printed pages rather than as curves in one "
                "frame"),
    figure("f9",
           cap("Figure 9: Graph of Birth Rate in the Next Fifty Years"),
           mention(27, first=None, style=[], count=0),
           geo("composite-panel", panels=10, layout="2x5"),
           path=P_APPA, kind="appendix",
           note="appendix plate: ten boxed panels in a 2x5 grid, one per language (Mandarin, "
                "English, Hindustani, Spanish, Arabic / Malay, Russian, Bengali, Portuguese, "
                "French), each panel with its own y limits and its own repeated axis titles - x "
                "'Time/year' with ticks 1950, 2000, 2050, 2100 and y 'Death rate/%'. Two series "
                "per panel: red asterisks for the observations and one pale fitted line. The "
                "caption says Birth Rate and every single y axis inside the frame says Death "
                "rate, so the two appendix plates are told apart only by their captions. Never "
                "cited from the body - the body only says 'See: Apendix B'"),
    figure("f10",
           cap("Figure 10: Graph of Death Rate in the Next Fifty Years"),
           mention(27, first=None, style=[], count=0),
           geo("composite-panel", panels=10, layout="2x5"),
           path=P_APPA, kind="appendix",
           note="the second appendix plate, panel-for-panel identical in construction to Figure "
                "9 - same ten languages in the same order, same boxed 2x5 grid, same repeated "
                "'Time/year' and 'Death rate/%' titles, same red asterisks - with different y "
                "limits per panel and a dark-blue connecting line instead of the pale fit. "
                "Because Figure 9's axes also read 'Death rate', the pair is visually "
                "indistinguishable except by y range: two different quantities share one axis "
                "title"),
    figure("f11",
           cap("Figure 11: Graph of Population of Top 6 to 16 Language Groups in the Next Fifty "
               "Years"),
           mention(27, first=None, style=[], count=0),
           geo("line", labels=True),
           path=P_APPA, kind="appendix",
           note="appendix plate of the mid-ranked languages: x 'Time/year' 2010 to 2070, y "
                "'Population/million' 50 to 350 in 50 steps where the axis starts at 50 rather "
                "than 0, so every curve is vertically exaggerated. Fifteen curves with inline "
                "labels (Bengali, Malay, Hausa, Russian, French, Portuguese, Punjabi, Japanese, "
                "German, Persian, Swahili, Javanese, Telugu, Korean, Wu) against a caption "
                "promising groups 6 to 16, which is eleven - four more labels than the title "
                "accounts for, and several labels sit across crossing lines"),
    figure("f12",
           cap("Figure 12: Graph of Population of Top 17 to 26 Language Groups in the Next Fifty "
               "Years"),
           mention(28, first=None, style=[], count=0),
           geo("line", labels=True),
           path=P_APPA, kind="appendix",
           note="the last appendix plate and the only page of the paper with a single exhibit: x "
                "'Time/year' 2010 to 2070, y 'Population/million' 50 to 120 with the same "
                "truncated baseline as Figure 11, ten curves with inline labels (Javanese, "
                "Telugu, Korean, Tamil, Kannada, Vietnamese, Wu, Yue, Turkish, Italian). Ten "
                "labels against a caption promising ranks 17 to 26, which is also ten - the one "
                "appendix plate whose count matches its title"),
]

TABLES = [
    table("t_sym",
          uncap(),
          mention(3, first=None, style=[], count=0),
          grid(11, 2, header=1, numeric=0, txt=2),
          path=P_SYM, kind="symbols", caption_source="none",
          note="the section 2.1.1 notation grid, first of three uncaptioned symbol tables: eleven "
               "rows against two columns (Symbol, Description), booktabs with a rule under the "
               "header only, no verticals, no shading, no note row. No caption is printed - the "
               "section heading above does that job. Its own defect is that the symbol 'ii' is "
               "spent on two different quantities, the annual birth rate and the annual death "
               "rate of native speakers, so the two rows cannot be told apart from the table "
               "alone. The heading itself is misspelt 'Symbol Descrption'"),
    table("t1",
          cap("Table 1: Projections for Population Statistics of Major Languages in 2017",
              "Table N:", position="below"),
          mention(9, first=9, style=["Table 1"], count=1,
                  lead="Y(4) = A4Y(0) (Presenting only the top 10 figures) (Table 1):",
                  pattern="parenthetical"),
          grid(10, 5, header=2, numeric=4, txt=1, merged=True, width="half"),
          path=P_25, kind="model",
          note="the projection-versus-reality check: ten languages against five columns - "
               "Language, Native (predict), Native (real), Non-native (predict), Non-native "
               "(real) - where 'Language' is a single cell spanning both header rows and the "
               "four measure labels wrap onto two lines each. Booktabs with top, header and "
               "bottom rules, no verticals; runs about 60 percent of the text measure, so its "
               "header wraps instead of widening. Magnitudes are printed bare, in millions, with "
               "no unit anywhere, and the Japanese row prints '?' in both non-native columns - "
               "the only admitted missing data in the paper's tables"),
    table("t_add",
          uncap(),
          mention(11, first=None, style=[], count=0),
          grid(17, 2, header=1, numeric=0, txt=2),
          path=P_312, kind="symbols", caption_source="none",
          note="the section 3.1.2 additional-symbol grid, the paper's longest table: seventeen "
               "rows against two columns, booktabs, no verticals, no shading, no caption. Its "
               "row for p_ji prints the constraint as '0 < p_ij < 1', flipping the subscript "
               "inside its own parenthetical, and the argument order of d_ji (similarity of i "
               "and j) runs opposite to S_ji (learners of j from i) without either row saying "
               "so"),
    table("t42",
          uncap(),
          mention(19, first=None, style=[], count=0),
          grid(8, 2, header=1, numeric=0, txt=2),
          path=P_42, kind="symbols", caption_source="none",
          note="the section 4.2 symbol grid for the office-siting model: eight rows, two "
               "columns, booktabs, no key and no caption, plus a closing line below the last "
               "rule that defines the j = 0 subscript. That line is inside the region's raster "
               "and never reaches the text layer, so note_sentence is left empty and the fact is "
               "recorded here only. Units are printed inside the description cells rather than "
               "in the header, and only on two of the eight rows ('(Unit: million)' and "
               "'(Unit: ten billion USD)'), so the other six silently inherit them. The measured "
               "box also swallows the '4.3 Calculating and Simplifying' heading below it"),
    table("t_a2017",
          uncap(),
          mention(20, first=None, style=[], count=0),
          grid(6, 2, header=1, numeric=1, txt=1),
          path=P_431, kind="other", caption_source="none",
          note="the 2017 office-siting result for six offices: six rows against two columns "
               "(Office location, Covering languages (Exclusive of English)) plus a totals row "
               "'Accumulated scores 43.0' set off by its own rule - the only grid in the paper "
               "with a footer band. Uncaptioned; the ranking lives in the prose. The measured "
               "box cuts the five-office table printed directly beneath it after four rows, so "
               "the region is one table plus a fragment of the next, and the language cells "
               "carry lower-case 'marathi' and spaces before commas ('Arabic ,Russian ,Bengali')"),
    table("t_a2067",
          uncap(),
          mention(21, first=None, style=[], count=0),
          grid(6, 2, header=1, numeric=1, txt=1),
          path=P_432, kind="other", caption_source="none",
          note="the 2067 counterpart of the 2017 grid: six offices, two columns, totals row "
               "'Accumulated scores 236.2'. The offices have moved - Jakarta and Dubai appear, "
               "Moscow and Paris survive with different portfolios - so the pair is the paper's "
               "only evidence for its own relocation recommendation, and the two grids are "
               "otherwise indistinguishable in construction. The measured box again cuts the "
               "five-office table below it"),
    table("t_memo1",
          uncap(),
          mention(22, first=None, style=[], count=0),
          grid(6, 2, header=1, numeric=0, txt=2),
          path=P_MEMO, kind="other", caption_source="none",
          note="the office proposal restated inside the Memo, uncaptioned and introduced only by "
               "the sentence 'we hereby propose the optimal location options for new offices'. "
               "Six rows, two columns, booktabs, no totals row and no key; its rules run about "
               "80 percent of the text measure, narrower than every other grid in the paper. "
               "'Germany' stands where the language German is meant"),
    table("t_memo2",
          uncap(),
          mention(23, first=None, style=[], count=0),
          grid(6, 2, header=1, numeric=0, txt=2),
          path=P_MEMO, kind="other", caption_source="none",
          note="the second Memo proposal, and the one measured box in the paper that holds TWO "
               "printed tables: both six rows by two columns, booktabs, uncaptioned, separated "
               "only by the paragraph 'If your company offers non-necessities'. The table fields "
               "describe the first grid and this note records the second. One row label is "
               "misspelt 'Beilin' for Berlin, and this is the paper's last exhibit before the "
               "signature"),
    table("t4",
          cap("Table 4: Birth Rate and Death Rate of Major Language Groups", "Table N:",
              position="below", variables=2),
          mention(25, first=None, style=[], count=0),
          grid(10, 3, header=1, numeric=2, txt=1, decimal=True),
          path=P_APPA, kind="appendix",
          note="weighted birth and death rates by language, ten rows against three columns, and "
               "the one grid in the paper whose numbers are decimal-aligned (four decimals "
               "throughout). Booktabs, no verticals, no shading, caption below. No unit is "
               "printed anywhere - the rates are bare factors - and the measured box is larger "
               "than the table: it reaches up into the previous grid's caption ('Table 3: Major "
               "Countries...') and down through its own caption into the header of Table 5, so "
               "the region holds three printed objects and only the middle one is this row"),
    table("t6",
          cap("Table 6: Office Location Selections When 1 = 2; 2 = 3 = 1 (More regard to "
              "population)", "Table N:", position="below", variables=1),
          mention(26, first=None, style=[], count=0),
          grid(6, 2, header=1, numeric=0, txt=2),
          path=P_APPA, kind="appendix",
          note="the population-weighted siting variant in Appendix A: six offices, two columns, "
               "booktabs, caption below. Its caption is the paper's clearest typographic loss - "
               "the weighting condition prints as '1 = 2; 2 = 3 = 1' because both eta glyphs "
               "dropped out, so the reader cannot tell which weight is which, and the condition "
               "is repeated as bare numbers in the note text as well"),
    table("t7",
          cap("Table 7: Office Location Selections When 1 = 2; 2 = 3 = 1 (More regard to "
              "population)", "Table N:", position="below", variables=1),
          mention(26, first=None, style=[], count=0),
          grid(6, 2, header=1, numeric=0, txt=2),
          path=P_APPA, kind="appendix",
          note="the second population-weighted variant, and the paper's worst caption defect: "
               "its caption is word for word identical to Table 6's - only the number changes - "
               "although the office sets differ (Jakarta and Beilin appear, Moscow keeps a "
               "different list). Two different results therefore carry one identical description, "
               "and the prose introducing them numbers neither"),
    table("t8",
          cap("Table 8: Economic Outlook for the Next Fifty Years", "Table N:", position="below",
              variables=1),
          mention(26, first=None, style=[], count=0),
          grid(19, 7, header=1, numeric=6, txt=1),
          path=P_APPA, kind="appendix",
          note="the cycle-projection substrate of the whole siting model: nineteen economies "
               "against seven columns - a row-label column with no header of its own, four cycle "
               "multipliers to eight decimals, then 2017 GDP and 2067 GDP in E-notation. The "
               "widest and densest grid in the paper, still booktabs with three rules, no "
               "verticals, no shading, no note row and no source line. Spain is printed twice "
               "with different numbers, 'Rassia' stands for Russia and 'Bengaladesh' for "
               "Bangladesh, and the two GDP columns carry 17 to 19 significant digits of false "
               "precision"),
]

ALL = FIGURES + TABLES
_order = sorted(ALL, key=lambda it: (it["page"], (it["bbox"][1] + it["bbox"][3]) / 2))
_page_seen: dict[int, int] = {}
for i, item in enumerate(_order, 1):
    item["place"]["doc_order"] = i
    pg = item["page"]
    _page_seen[pg] = _page_seen.get(pg, 0) + 1
    item["place"]["page_order"] = _page_seen[pg]

RULES = [
    "Numbering is one colon grammar twice over - every figure caption prints 'Figure N:' and "
    "every captioned grid prints 'Table N:' with the same colon, no period and no roman - but "
    "only five of the paper's twelve grids carry a number at all: the three symbol grids of "
    "sections 2.1.1, 3.1.2 and 4.2, the two 4.3 office grids and both Memo grids are bare "
    "[caption.numbering].",
    "Caption side follows exhibit kind without exception: all twelve figure captions print BELOW "
    "the artwork and all five captioned grids print BELOW their last rule, so this paper puts "
    "every caption at the foot - #145's convention, and the opposite of #146 and #147, whose "
    "tables carried theirs above [caption.position].",
    "Caption length is one line almost everywhere: the twelve figure captions run 9 to 19 words "
    "and the five grid captions 9 to 15, print in roman sentence case with no full stop and no "
    "bold, and no caption anywhere states a unit, a conclusion or a numeric condition "
    "[caption.words].",
    "Symbols reach the captions only on the figure side - three of them name a parameter "
    "('When k=0.1', 'When k=10', 'Top 6 to 16 Language Groups') - while none of the five "
    "captioned grids names a variable, so a reader holding only the table captions cannot "
    "recover a single column heading's units or argument order [caption.variable_count].",
    "Three captions are wrong at the level of the noun and one is empty where a symbol belongs: "
    "Figure 9 is captioned 'Birth Rate' while its own axes read 'Death rate/%', Table 7 repeats "
    "Table 6's caption word for word, Table 1 promises 'Projections' for columns that mix "
    "prediction with realisation, and Figure 2 prints 'Rate ( )' with the parameter dropped out "
    "of the brackets [caption.verbatim].",
    "No caption prints a unit and no caption states a result; the units that exist in this "
    "paper live inside the artwork (axis titles) or inside two cells of the section 4.2 symbol "
    "grid ('(Unit: million)', '(Unit: ten billion USD)') [caption.units].",
    "The drawing is one engine and three idioms: seven of the twelve figures are MATLAB line "
    "plots, two are hand-laid transition graphs, two are 2x5 panel plates and one is a pie "
    "chart [geometry.family].",
    "Nothing in the paper is three-dimensional and nothing carries a colour scale - no surf "
    "plot, no heatmap, no contour - so every quantity is read off a position against a printed "
    "tick, and the twelve figures together contain no key legible at print size "
    "[geometry.three_d].",
    "Keys are rare and never inside the frame: two figures (7 and 8) key their twenty-six "
    "curves in a bordered box placed OUTSIDE the plotting area at the upper right, seven figures "
    "(1, 3, 4, 5, 6, 11, 12) label their marks inline, and the other three carry no key and no "
    "labels - a single-trace plot and the two plates whose panels are titled instead "
    "[geometry.legend].",
    "Panel grammar has exactly two states: a single frame, or a 2x5 grid of ten titled panels "
    "in the two appendix plates. Only those two use panels, they do not share axes - every "
    "panel repeats its own 'Time/year' and 'Death rate/%' titles - and no panel letter (a)/(b) "
    "exists anywhere in the paper [geometry.panel_count].",
    "Shared axes are used zero times: every multi-panel exhibit repeats its full axis labels "
    "panel by panel, and every multi-curve exhibit carries one y scale for all curves, which is "
    "why the eighteen bottom curves of Figures 7 and 8 merge into a single band below 350 "
    "million [geometry.shared_axes].",
    "Printed values are absent from every figure - no data labels, no annotated points, no "
    "value strip under the plots: the only printed numbers in the artwork are axis ticks, so "
    "the three figures that matter most (4, 7, 8) present their twenty-six curves as "
    "indistinguishable hairlines [geometry.printed_numbers].",
    "Every grid in the paper is booktabs: three horizontal rules (top, below the header, "
    "bottom), no vertical rule at any cell boundary, no outer box, no zebra shading and no "
    "slanted corner cell - the style is invariant across twelve grids, including the four whose "
    "content reaches the layout as a raster rather than as vectors [table.rule_style].",
    "Merged cells appear exactly once: Table 1's 'Language' cell spans both header rows while "
    "the four measure labels wrap inside the second row. No other grid merges a cell, and no "
    "grid prints a diagonal header [table.merged_cells].",
    "Header depth is one row for eleven of the twelve grids; only Table 1 needs two, and only "
    "the 2017 and 2067 office grids add a body band - a rule above their 'Accumulated scores' "
    "totals row - which is the sole footer structure in the paper [table.header_rows].",
    "Grid width splits by function, not by size: the single comparison grid (Table 1) is set at "
    "about 60 percent of the measure while the nineteen-row economic table (Table 8) and the "
    "seventeen-row symbol grid run the full measure, so the paper lets its widest tables run "
    "wide and only the one it wants read against prose wrap [table.width].",
    "Decoration is absent on the grid side as completely as on the figure side: no grid is "
    "striped, none is turned into landscape, none continues onto a second page, and not one of "
    "the twelve prints a source line or a table note that reaches the text layer - the only "
    "note-like row in the paper is the closing line of the section 4.2 grid, and it is inside "
    "the raster [table.note_sentence].",
    "Announcement is same-page for four cited rows and one page early for five: Figures 3, 4, "
    "5, 6 and 8 are named in the prose on the page before their artwork prints, while Figures "
    "1, 2, 7 and Table 1 are cited on their own page, so this paper's habit is to lead its "
    "exhibits by a page [mention.lead_pages].",
    "Fifteen of the twenty-four rows are never cited from the body at all - Figures 9 to 12 and "
    "the eleven uncaptioned or appendix grids - and every one of them sits either at the foot "
    "of a section or inside the appendices, reached only by the bare gestures 'See: Apendix B', "
    "'See: Appendix A' and 'the data in 2013 is in Appendix A' [mention.count].",
    "Citation vocabulary is a parenthetical rotation: eight of the nine cited rows are "
    "introduced by '(Figure N)' or '(Table N)' glued to the end of a sentence, and only Figure 3 "
    "gets a full as-shown-in construction ('Example graph ... is shown below (Figure 3)') "
    "[mention.lead_pattern].",
    "Placement follows the argument down the page: thirteen rows sit in the top third, seven in "
    "the middle band and four at the foot, and the four foot cases are the third panel of the "
    "appendix plate, the section 2.1.1 symbol grid that closes its page and two grids that fill "
    "the bottom half of a page of tables [place.page_zone].",
    "Exhibit density is where the work is: six model rows, one result row, two sensitivity runs "
    "and three symbol grids fill sections 2 and 3, four uncaptioned grids belong to the "
    "application section and its Memo, and the appendices hold eight rows - four grids and four "
    "plates - while the introduction, the strengths section and the references carry nothing at "
    "all [place.section_kind].",
    "Twenty-three of the forty-seven measured boxes are not exhibits: every one of them is "
    "display mathematics - equations (1) to (18), the parameter blocks, the 22x22 and 44x44 "
    "matrices and the phi ratios - which the detector boxes as an image region although the "
    "maths is typeset rather than scanned, so the region pass reads this paper's equations as "
    "artwork and at the same time misses three of its printed tables [place.area_frac].",
]

NOTE = (
    "Forty-seven measured regions resolve to 24 exhibit rows (12 figures, 12 grids) and 23 "
    "exclusions, unaccounted 0. Every exclusion is display mathematics: equation (1) on p5, "
    "equations (2)-(6) on p6, the 22x22 matrix (7) on p7, the rate definitions on p8, the "
    "eigenvector and eigenvalue on p9, the block transition matrix and (14)-(15) on p12, the "
    "English-only matrix on p13, the initial vector and similarity parameter on p14, the "
    "k-exponent modification (17) on p17, the rating model (18) on p18 and the weight-coefficient "
    "lines on pp19-20. The mathematics is typeset, not pasted - decimal points print as colons "
    "('[k = 0:1]', '[when > 0:021]') and both eta glyphs have dropped out of the siting "
    "captions - yet `fig_extract.py` boxes it as a raster region anyway, so this paper is the "
    "batch's cleanest case of the detector counting equations as pictures.\n\n"
    "What this paper adds to the lane. (1) The caption side rule now has a third direction: "
    "#146 and #147 put figure captions below and table captions above, #145 put both below, and "
    "#148 puts both below again, so 'tables above' is one paper's habit rather than a batch "
    "convention. (2) It is the first paper in the batch whose grids are mostly uncaptioned: "
    "seven of twelve grids carry neither a number nor a caption, being symbol and result tables "
    "announced by their own section heading. They still have to be recorded - a census of what "
    "was drawn cannot skip the grids without numbers - so their caption block is empty with "
    "caption_source 'none'. (3) Three printed tables are missing from the layout entirely: "
    "Table 2 on p15 and Tables 3 and 5 on p25 are native text tables with rules, and the region "
    "pass boxes only Table 4 on p25, because that one happened to be a raster object. They are "
    "invisible to the detector and are recorded here only in this note. (4) Three measured "
    "boxes cut across printed objects: the p25 box runs from Table 3's caption through Table 4 "
    "into Table 5's header, and the p20 and p21 boxes each hold one office grid plus four rows "
    "of the next one. (5) File the figures as one engine, three idioms: seven MATLAB line plots, "
    "two hand-laid transition graphs, two 2x5 plates and one pie chart - and one exhibit family "
    "the vocabulary has no name for, which is why Figure 6 is filed 'other' with a note.\n\n"
    "Defects worth recording. Figure 2's caption prints 'Rate ( )' where the learning-rate "
    "symbol fell out. Figure 5's inline region labels are 5-6 pt. Figures 7 and 8 carry "
    "twenty-six-entry key boxes placed outside the axes and illegible at print size, and their "
    "bottom eighteen curves merge below 350 million. Figure 9 is captioned Birth Rate while "
    "every panel axis reads 'Death rate/%', and Figure 10's axes read the same, so the two "
    "plates cannot be told apart from their labels. Figures 11 and 12 truncate their y axis at "
    "50, inflating every trend. Figure 11 labels fifteen languages against a caption promising "
    "ranks 6 to 16, which is eleven. Table 1 prints '?' in both non-native Japanese columns. "
    "Tables 6 and 7 share one caption word for word, with both eta glyphs missing so the "
    "weighting condition prints as '1 = 2; 2 = 3 = 1'. Table 8 prints Spain twice, 'Rassia' for "
    "Russia and 'Bengaladesh' for Bangladesh, with 17 to 19 significant digits. The Memo grid "
    "misspells Berlin as 'Beilin'. The section 2.1.1 symbol grid spends 'ii' on two different "
    "rates, the section 3.1.2 grid writes its own constraint with the subscript flipped "
    "('[0 < p_ij < 1]' in the p_ji row), and the section 4.2 grid puts a unit on two rows and "
    "none on the other six. A red Chinese shop-watermark band crosses the running header on "
    "every page.\n\n"
    "Section grammar. This paper draws its model before it uses it: the N=2 transition graph "
    "(Figure 1), the learning-rate correlation that fixes the model's parameter range (Figure "
    "2), the parameter-free validation against 2017 (Table 1), the eight-state graph of the "
    "modified model (Figure 3), then the projections themselves (Figure 4), the migration scale "
    "(Figure 5), the non-native distribution (Figure 6), the two sensitivity runs (Figures 7 "
    "and 8), the siting grids with the 2017 and 2067 office results (uncaptioned, in the body), "
    "the economic substrate (Table 8), and finally four appendix plates (Figures 9-12) that "
    "carry the twenty-one language groups the body could not fit. Three symbol grids stand in "
    "front of the three model blocks and none of them is captioned. What is missing is any "
    "figure of the object the paper is nominally about: no map, no scatter, no density, nothing "
    "geographic in a paper whose title promises the location."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"page": _p, "bbox": _b, "reason": _r, "note": _k}
        for _k, (_p, _b, _r) in EXCLUDED.items()
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
    twords = [it["caption"]["words"] for it in TABLES if it["caption"]["words"]]
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


if __name__ == "__main__":
    sys.exit(main())
