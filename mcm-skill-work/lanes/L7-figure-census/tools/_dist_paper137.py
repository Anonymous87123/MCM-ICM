"""Hand pass for P-E-2017-68242-753e0037 (smart growth, Wellington and Anchorage).

Shape of the paper: a three-E metric system (SSG = SEP + SSE + SES) built section by section,
then a grey-relational evaluation of two cities' current plans, then seven initiatives per city
ranked by an index of potential. Ten printed figures and nine printed tables against 23 measured
regions and 3 exclusions.

What the record has to say out loud:

1. Nine of the ten figures are not plots. Figures 1, 3, 4 and 5 are the same three-circle Venn
   template drawn four times (one per section that introduces a component set), Figure 2 and
   Figure 10 are box-and-arrow schematics, and only Figures 6, 7, 8 and 9 carry axes. The Venns
   are recorded as family "other": no nodes, no axes, every label printed inside its circle and a
   single leader-line annotation in the upper right naming the whole drawing - which is not a
   legend, since it repeats no entry and keys no colour.
2. Caption side splits by exhibit type and never mixes: all ten figure captions print below the
   artwork, all ten table captions print above the grid.
3. The numbering never settles. "Figure1." through "Figure4." glue the number to the title with no
   space, "Figure 5." spaces it and keeps the stop, "Figure 6" and "Figure 7" space it and drop the
   stop, "Figure 8." to "Figure 10." return to the stop, and "Table 5" through "Table 9" drop the
   stop the four indicator tables carry. All recorded normatively with the printed form in the note.
4. Four exhibits are cited late or never: Figure 2 and Figure 9 are named by deixis only, and
   Figure 10 is cited seven pages before it prints ("More intuitive flow refers to figure
   10(Appendix)" on p15, the drawing on p22).
5. Three grids are announced as "table N" and then never numbered again, while Tables 2, 3 and 4
   are named a second time on p12 in a single sentence ("Refer to Table 2, Table 3 and Table 4"),
   which is the only cross-reference in the paper that bundles exhibits.
6. Half-measured and unmeasured: Table 8's landscape of two stacked city blocks returns a region
   for the Anchorage block only, so the Wellington block is a declared gap rather than a row;
   Table 7 breaks across p15/p16 with no header repeat; Figure 7 and Figure 8 are two panels each
   and only one panel per figure is measured.
7. One row with no caption at all: the variable glossary on p5 prints 15 symbols with a
   "First appearing page" column and neither a caption nor a number.

Usage: python -I tools/_dist_paper137.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-E-2017-68242-753e0037"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((LANE / f".proxy/{PID}-ctx.json").read_text(encoding="utf-8"))

MEASURED = {(pg["page"], tuple(round(v, 1) for v in r["bbox"]))
            for pg in LAYOUT["pages"] for r in pg["regions"]}
PAGE_W = LAYOUT["pages"][0]["width"]
PAGE_H = LAYOUT["pages"][0]["height"]

HEAD: dict[str, str] = {}
for _h in CTX["headings"]:
    _n, _l = _h.get("number"), _h.get("label")
    if not _n or not _l or not _l.startswith(_n + " "):
        continue
    if _n not in HEAD:
        HEAD[_n] = _l


def H(*numbers: str) -> list[str]:
    return [HEAD[n] for n in numbers]


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


S_INTRO = H("1")
S_13 = H("1", "1.3")
S_VARS = H("3")
S_POLICY = H("4")
S_51 = H("5", "5.1")
S_511 = H("5", "5.1", "5.1.1")
S_52 = H("5", "5.2")
S_521 = H("5", "5.2", "5.2.1")
S_522 = H("5", "5.2", "5.2.2")
S_53 = H("5", "5.3")
S_531 = H("5", "5.3", "5.3.1")
S_532 = H("5", "5.3", "5.3.2")
S_622 = H("6", "6.2", "6.2.2")
S_73 = H("7", "7.3")
S_74 = H("7", "7.4")
S_75 = H("7", "7.5")
S_76 = H("7", "7.6")
S_77 = H("7", "7.7")
S_APP = ["未编号标题：Appendix"]

# (page, bbox) for every row, checked against the measurement on build.
B = {
    "fig1": (3, [156.8, 392.2, 440.2, 583.1]),
    "fig2": (4, [93.6, 469.2, 541.3, 684.6]),
    "vars": (5, [67.0, 327.1, 527.6, 710.9]),
    "tab1": (6, [64.8, 232.6, 534.9, 629.3]),
    "fig3": (7, [135.8, 285.3, 460.8, 480.2]),
    "tab2": (8, [86.5, 160.9, 508.8, 316.9]),
    "fig4": (8, [146.3, 577.6, 471.3, 772.5]),
    "tab3": (9, [65.5, 449.9, 529.8, 555.5]),
    "fig5": (10, [160.2, 112.0, 437.4, 265.7]),
    "tab4": (11, [65.5, 160.9, 529.8, 290.1]),
    "tab5": (13, [79.6, 376.9, 515.1, 433.6]),
    "fig6": (13, [168.1, 496.8, 453.0, 652.8]),
    "tab6": (15, [65.5, 412.1, 529.8, 597.8]),
    "tab7": (15, [65.5, 676.5, 529.8, 783.0]),
    "fig7": (16, [72.6, 609.2, 289.2, 768.2]),
    "tab8": (17, [64.3, 562.3, 531.0, 602.2]),
    "tab9": (17, [100.5, 710.9, 494.1, 769.9]),
    "fig8": (19, [72.7, 57.0, 281.6, 233.8]),
    "fig9": (19, [164.2, 382.8, 433.0, 584.2]),
    "fig10": (22, [165.8, 107.1, 431.3, 476.4]),
    # measured but not an exhibit row of its own
    "fig7r": (16, [308.8, 610.4, 521.3, 768.2]),
    "tab7b": (16, [65.5, 53.9, 529.8, 127.7]),
    "fig8r": (19, [327.9, 57.0, 525.6, 234.8]),
}

for _name, (_p, _b) in B.items():
    assert (_p, tuple(_b)) in MEASURED, f"{_name} bbox is not a measured region"
assert len(MEASURED) == len(B)


def place(page: int, bbox: list[float], path: list[str], kind: str,
          numbered: bool = True, solo: bool = False) -> dict:
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (PAGE_W * PAGE_H)
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 0,
        "page_zone": z,
        "area_frac": round(frac, 3),
        "solo_page": solo,
    }


def caption(v: str, *, numbering: str, cond: bool = False, concl: bool = False,
            units: bool = False, vars_: int = 0, pos: str = "below",
            voice: str = "none") -> dict:
    return {
        "verbatim": v,
        "numbering": numbering,
        "words": len(schema.words(v)),
        "sentences": len(schema.sentences(v)),
        "units": units,
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": cond,
        "concludes": concl,
        "voice": voice,
        "position": pos,
    }


def tcap(v: str, *, numbering: str, vars_: int = 0) -> dict:
    """Every table caption in this paper prints above its grid."""
    return caption(v, numbering=numbering, pos="above", vars_=vars_)


def mention(page: int, *, first: int | None = None, style: list[str] | None = None,
            count: int = 0, lead: str = "", pattern: str = "none", read: int = 0,
            trail: str = "") -> dict:
    return {
        "first_page": first,
        "lead_pages": None if first is None else page - first,
        "style": style or [],
        "count": count,
        "lead_sentence": lead,
        "trail_sentence": trail,
        "lead_pattern": pattern,
        "read_sentences": read,
        "gap_sentences": None if first is None else abs(page - first),
    }


def figure(key: str, family: str, cap: dict, men: dict, *, path: list[str],
           kind: str, legend: str = "none", printed: bool = False, labels: bool = False,
           panels: int = 1, layout: str = "1", shared: bool = False, colorbar: bool = False,
           three_d: str = "no", numbered: bool = True, source: str = "text-layer",
           other_note: str | None = None, solo: bool = False, note: str = "") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "family": family,
        "other_note": other_note,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
        "note": note,
        "place": place(page, bbox, path, kind, numbered, solo),
        "mention": men,
        "caption": cap,
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": layout,
            "shared_axes": shared,
            "legend": legend,
            "colorbar": colorbar,
            "three_d": three_d,
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }


def table(key: str, cap: dict, men: dict, grid: dict, *, path: list[str],
          kind: str, note: str = "", numbered: bool = True,
          source: str = "text-layer") -> dict:
    page, bbox = B[key]
    return {
        "page": page,
        "bbox": bbox,
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
        "note": note,
        "place": place(page, bbox, path, kind, numbered),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "boxed", zebra: bool = False,
         merged: bool = False, diag: bool = False, units_hdr: bool = False,
         decimal: bool = False, numeric: int = 0, txt: int = 0, width: str = "full",
         orient: str = "portrait", continued: bool = False,
         note_sentence: str = "") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "header_rows": header,
        "rule_style": rules,
        "zebra": zebra,
        "merged_cells": merged,
        "diagonal_header": diag,
        "units_in_header": units_hdr,
        "decimal_aligned": decimal,
        "numeric_cols": numeric,
        "text_cols": txt,
        "width": width,
        "orientation": orient,
        "continued": continued,
        "note_sentence": note_sentence,
    }


VENN = ("three-circle Venn, the same template four times: no nodes, no axes, every circle label "
        "printed inside its own circle, and one leader-line annotation in the upper right naming "
        "the whole drawing - an annotation, not a legend, since it keys no colour and repeats no "
        "entry")

RADAR = ("radar (spider) chart on one polar axes, eight spokes and two closed polygons; the "
         "vocabulary has no radar family, so it is recorded as other rather than widened")

TAIL_VENN = (" its three circle labels sit inside the circles and the drawing carries one "
             "leader-line annotation in the upper right instead of a legend")

ALL = [
    figure("fig1", "other",
           caption("Figure1. The three E’s of sustainability of smart growth",
                   numbering="Figure N."),
           mention(3, first=3, style=["figure 1"], count=1, pattern="direct", read=1,
                   lead="To embrace a more depict description of the smart growth, pay attention "
                        "to figure 1.",
                   trail="Except for adhering to the goal of three E’s of sustainability"),
           path=S_INTRO, kind="introduction", other_note=VENN,
           note="the goal statement drawn as a Venn: 'Economically Prosperous' in the blue upper "
                "circle, 'Socially Equitable' in the grey left circle, 'Environmentally "
                "Sustainable' in the green lower-right circle, and a filled dot with a leader line "
                "to the triple overlap labelled 'Smart Growth' in the upper right" + TAIL_VENN
                + ". The caption glues the number to the title ('Figure1.'), which no other "
                  "figure does with a stop and no space except Figures 2, 3 and 4"),
    figure("fig2", "flowchart-or-schematic",
           caption("Figure2. The structure of sustainability", numbering="Figure N."),
           mention(4, lead="The structure of sustainability is as follows, where T represents 10 "
                           "principles of smart growth.", pattern="direct", read=1,
                   trail="The three E’s of sustainability is a broad statement of general "
                         "goals of a city’s smart growth"),
           path=S_13, kind="introduction",
           note="box-and-arrow schematic tying the three E's to the ten principles: four boxes with "
                "directional arrows and edge labels ('Supporting Workers', 'T1 T2 T3 T6 ...') "
                "printed outside the boxes. The only exhibit in the paper cited purely by deixis - "
                "'as follows' - with no number in the sentence and no number anywhere in the prose"),
    table("vars",
          caption("", numbering="none", pos="above"),
          mention(5),
          grid(16, 3, header=1, rules="vertical-rules", numeric=1, txt=2),
          path=S_VARS, kind="symbols", source="none",
          note="the variable glossary of section 3: 15 symbols (Ti, Gi, SSG, SEP, SSE, SES, SEPij, "
               "SSEij, SESij, sij, gamma-ij, delta-i, Wi, Ai, Pi) each with its description and the "
               "page it first appears on. No caption, no table number, no 'Table' word anywhere "
               "near it - the grid is introduced by its own section heading and nothing else, "
               "which is why caption_source is none and every caption field is a placeholder"),
    table("tab1",
          tcap("Table 1. Policy tools for smart growth (G1: Economically prosperity.G2: social "
               "Equity G3:Environmental sustainability)", numbering="Table N.", vars_=3),
          mention(6, first=6, style=["table 1"], count=1, pattern="direct", read=1,
                  lead="we show it in table 1.",
                  trail="If a city mainly intends to achieve Economical prosperity, the "
                        "initiatives should pay prior attention to policy tools T1, T6, T7, T8, "
                        "and T9"),
          grid(11, 4, header=1, rules="boxed", merged=False, numeric=0, txt=4),
          path=S_POLICY, kind="model",
          note="the ten principles against their keywords and their target goals: a tinted T-number "
               "column, a two-line 'Principles as General policy Tools' cell, the keyword column "
               "and an 'Intentions' column printing G1/G3 strings. The two-line caption above the "
               "grid carries the goal legend in parentheses '(G1: ...)' and the G1/G2/G3 band reads as "
               "part of it, so no spanning cell is counted in the grid itself. Verticals are "
               "partial - one rule after the Principles cell in the header row only, and the "
               "T-number column is separated from the principle by tint rather than by a rule"),
    figure("fig3", "other",
           caption("Figure3. The three components of smart growth economical prosperity",
                   numbering="Figure N."),
           mention(7, first=7, style=["figure 3"], count=1, pattern="direct", read=1,
                   lead="To embrace a more depict description of the components of economical "
                        "prosperity, pay attention to figure 3.",
                   trail="This component of a smart growth economic development strategy focuses "
                         "on understanding the current composition"),
           path=S_511, kind="model", other_note=VENN,
           note="second use of the Venn template, now for economic prosperity's three components "
                "(supporting businesses, workers, quality of life), with the leader-line annotation "
                "reading 'Smart Growth Economically Prosperous'. The caption line runs straight "
                "into the body text of the following bullet - the text layer prints "
                "'...economical prosperity  Supporting Businesses.' - so the recorded caption stops "
                "at the title and the residue is the first bullet of the list below the drawing"),
    table("tab2",
          tcap("Table 2. Indicators in SEP metric system.", numbering="Table N."),
          mention(8, first=8, style=["table 2"], count=2, pattern="direct", read=1,
                  lead="We show the metric of SEP in table 2.",
                  trail="The target ↑ (↓) indicates that the increase (decrease) of the "
                        "value will help promote the extent to success of economical prosperity in "
                        "smart growth."),
          grid(11, 6, header=1, rules="vertical-rules", merged=True, numeric=0, txt=6,
               note_sentence="The target ↑ (↓) indicates that the increase (decrease) of "
                             "the value will help promote the extent to success of economical "
                             "prosperity in smart growth."),
          path=S_51, kind="model",
          note="ten SEP indicators in six columns: the outer 'SEP' cell, a 'Supporting ...' group "
               "cell and its SEP<i> code, the indicator name, the notation (SEP11...) and the "
               "Target arrow column. The outer cell spans all ten data rows, the three group cells "
               "and their codes span 3, 4 and 3 rows, and the tint is column-wise (peach on the "
               "outer block, light blue on the codes, orange on Target) - no row is striped. Named "
               "twice: once here and once on p12 in the bundled cross-reference 'Refer to Table 2, "
               "Table 3 and Table 4'"),
    figure("fig4", "other",
           caption("Figure4. The three components of smart growth social equity",
                   numbering="Figure N."),
           mention(8, first=8, style=["figure 4"], count=1, pattern="direct", read=1,
                   lead="The component relationship of social equity is displayed in figure 4.",
                   trail="Fair Treatment. Fair treatment means that no group of people should bear "
                         "a disproportionate share of the negative environmental consequences"),
           path=S_521, kind="model", other_note=VENN,
           note="third use of the Venn template, here for social equity's components (fair "
                "treatment, meaningful involvement, equitable development), leader-line annotation "
                "'Smart Growth Socially Equitable'. Only exhibit on p8 besides Table 2, and it "
                "sits below the table with body prose between the two"),
    table("tab3",
          tcap("Table 3. Indicators in SSE metric system.", numbering="Table N."),
          mention(9, first=9, style=["table 3"], count=2, pattern="direct", read=1,
                  lead="We show the metric of SSE in table 3.",
                  trail="In addition, the extent of religious freedom and racial equity are "
                        "calculated by formula of formula of Shannon's diversity index"),
          grid(6, 6, header=1, rules="vertical-rules", merged=True, numeric=0, txt=6,
               note_sentence="The target ↑ indicates that the increase of the value will help "
                             "promote the extent to success of social equity in smart growth."),
          path=S_522, kind="model",
          note="five SSE indicators in six columns, the same grouped layout as Table 2 on a shorter "
               "body: outer 'SSE' cell spanning rows 2-6, group cells and codes spanning 2, 1 and 2 "
               "rows. No numeric column at all - every value cell is a notation code or an arrow"),
    figure("fig5", "other",
           caption("Figure 5. The three components of smart growth environmental sustainability",
                   numbering="Figure N."),
           mention(10, first=10, style=["figure 5"], count=1, pattern="direct", read=1,
                   lead="We show this relationship in figure 5.",
                   trail="The intuitive indicators to measure environmental sustainability are the "
                         "environment quality"),
           path=S_531, kind="model", other_note=VENN,
           note="fourth and last use of the Venn template, for environmental sustainability "
                "(environment quality, utility of land, multiple transportation), leader-line "
                "annotation in the upper right. This caption is the one that spaces the number "
                "('Figure 5.') after three figures that glue it ('Figure1.')" + TAIL_VENN),
    table("tab4",
          tcap("Table 4. Indicators in SES metric system.", numbering="Table N."),
          mention(11, first=11, style=["table 4"], count=2, pattern="direct", read=1,
                  lead="As showed in table 4.",
                  trail="The target ↑ (↓) indicates that a high (low) value of the "
                        "indicator is expected to enhance the environmental sustainability"),
          grid(9, 6, header=1, rules="vertical-rules", merged=True, numeric=0, txt=6,
               note_sentence="The target ↑ (↓) indicates that a high (low) value of the "
                             "indicator is expected to enhance the environmental sustainability"),
          path=S_532, kind="model",
          note="eight SES indicators, the longest of the three indicator grids: outer 'SES' cell "
               "spanning rows 2-9, group cells and codes spanning 3, 3 and 2 rows. The note "
               "sentence under the grid also states the function form SES = f(SES1, SES2, SES3), "
               "so it is quoted whole rather than truncated at the comma"),
    table("tab5",
          tcap("Table 5 rational grade of each metric in two cities", numbering="Table N"),
          mention(13, first=13, style=["table 5"], count=1, pattern="direct", read=1,
                  lead="We show the GRA results in table 5.",
                  trail="After calculating the average of each metric, we get Wellington (SEP "
                        "(0.7227), SSE (0.7245), SES (0.7500))"),
          grid(4, 9, header=2, rules="vertical-rules", merged=True, decimal=True, numeric=8,
               txt=1),
          path=S_622, kind="result",
          note="the GRA output: two header rows (a group row where SEP spans three columns, SSE two "
               "and SES three, over a label row of SEP1..SES3) and two city rows of 4-dp grades, "
               "point-aligned in all eight numeric columns. SSE2 is missing, because the paper "
               "declares meaningful involvement unquantifiable - the same eight columns the radar "
               "chart of Figure 6 plots. No printed note sentence"),
    figure("fig6", "other",
           caption("Figure 6 Rational grades for the first class indicators.", numbering="Figure N"),
           mention(13, first=13, style=["figure 6"], count=1, pattern="direct", read=1,
                   lead="For a depict comparison, we draw a radar chart as showed in figure 6.",
                   trail="To analyze how successful the city’s current growth plan is"),
           path=S_622, kind="result", other_note=RADAR, legend="outside-right", shared=True,
           printed=True,
           note="the eight Table 5 columns plotted on one polar axes as two closed polygons "
                "(Wellington blue, Anchorage red) with a key parked to the right of the plot, "
                "radial ticks 0-1 printed. Both cities share the same axes, so 'shared_axes' is "
                "true even though the panel count is one - there is no second frame to compare "
                "against. Caption drops the stop after the number ('Figure 6 Rational grades')"),
    table("tab6",
          tcap("Table 6 Growth plan for Wellington", numbering="Table N"),
          mention(15, first=15, style=["table 6"], count=1, pattern="direct", read=1,
                  lead="we give specific initiatives, the corresponding policy tools and the "
                       "indicators involved in each initiative in table 6.",
                  trail="Plan for Anchorage, we also give seven initiatives with consideration of "
                        "principle components (two for SEP, two for SSE, two for SEP)"),
          grid(8, 4, header=1, rules="vertical-rules", merged=True, numeric=0, txt=4),
          path=S_73, kind="solution",
          note="seven Wellington initiatives W1-W7 in four columns: metric (SES/SSE/SEP), policy "
               "tools (T-string), indicator components and the initiative sentence. The metric cell "
               "spans 2, 2 and 3 rows and the policy-tool cell spans the same three blocks, so the "
               "left half of the grid is a two-column group table bolted to a four-line right half"),
    table("tab7",
          tcap("Table 7 Growth plan for Anchorage", numbering="Table N"),
          mention(15, first=15, style=["table7"], count=1, pattern="direct", read=1,
                  lead="we show the plan in table7.",
                  trail="A5: Adopt comprehensive plans and sub-area plans"),
          grid(8, 4, header=1, rules="vertical-rules", merged=True, numeric=0, txt=4,
               continued=True),
          path=S_73, kind="solution",
          note="seven Anchorage initiatives A1-A7, same four-column layout as Table 6, breaking "
               "after A4: the header row and rows A1-A4 print on p15, rows A5-A7 plus the SES group "
               "print at the top of p16 with no header repeat and no 'continued' word. The row "
               "carries the p15 head; the p16 fragment is excluded as split-across-pages. The "
               "citation glues the number to the word ('table7'), the only exhibit in the paper "
               "printed that way"),
    figure("fig7", "surface-or-3D",
           caption("Figure 7 The expected distribution of the three metrics under our plan",
                   numbering="Figure N"),
           mention(16, first=16, style=["figure 7"], count=1, pattern="direct", read=1,
                   lead="We give a intuitive show in figure 7.",
                   trail="From above figures, our plans demonstrate increasing positive effects on "
                         "value of each metric"),
           path=S_74, kind="result", panels=2, layout="1x2", shared=True, colorbar=True,
           three_d="perspective-bars", note="two extruded 3-D column blocks side by side, each with "
                "its own colour bar (0.7-0.73 Wellington, 0.7-0.72 Anchorage) and its own title "
                "line printed above it ('The performance of growth plan for "
                "Wellington(SSE,SES,SEP)' / '...for Anchorage(SSE,SES,SEP)'), sharing one z axis "
                "caption 'Grey rational grade' and one caption below the pair. Arrow annotations "
                "label the four periods (Origin, Short-term, Medium-term, Long-term); no legend "
                "and no printed data labels. Two panels, two measured boxes, and this row carries "
                "the left one - the right panel is excluded as a fragment of the same exhibit, so "
                "the row's area_frac counts one panel only"),
    table("tab8",
          tcap("Table 8 Index of potential for initiatives", numbering="Table N"),
          mention(17, first=17, style=["Table 8"], count=1, pattern="figure-n-shows", read=1,
                  lead="Table 8 shows the potential of initiatives for Wellington and Anchorage.",
                  trail="Based the results above, we rank the initiatives with the smart growth "
                        "plan for each city, as shown in table 9."),
          grid(4, 10, header=1, rules="booktabs", merged=True, decimal=True, numeric=7, txt=3,
               note_sentence="The symbol “-”indicates that the initiative aims at "
                             "maintaining the current level of the related indicators"),
          path=S_75, kind="result",
          note="two stacked city blocks in one printed table - Wellington (W1-W7) above, Anchorage "
               "(A1-A7) below - each a header row carrying the city name merged over its three "
               "stage rows plus an 'Initiative' and a 'Potential' column. Only the Anchorage block "
               "returns a measured region, so this row records that block and the Wellington block "
               "is a declared gap: its header and three 4-dp rows print between the caption and "
               "y=562.3 pt and fall inside no measured region. No verticals anywhere; the two rules "
               "are a header rule and a closing rule"),
    table("tab9",
          tcap("Table 9 Rank of initiatives according to potential", numbering="Table N"),
          mention(17, first=17, style=["table 9"], count=1, pattern="as-shown-in", read=1,
                  lead="we rank the initiatives with the smart growth plan for each city, as shown "
                       "in table 9.",
                  trail="For Wellington. W2, providing condition for Greenfield growth is the most "
                         "potential."),
          grid(4, 3, header=1, rules="booktabs", merged=False, numeric=0, txt=3,
               note_sentence=""),
          path=S_75, kind="result",
          note="the ranking table: a stage column and one column per city, each cell a chain of "
               "inequalities ('W2>W1>W4>W5>W3>W6>W7'). Booktabs with a header rule and no closing "
               "rule - the only table in the paper that ends without a bottom line. One cell of the "
               "Anchorage medium-term row prints a doubled separator ('A5>>A1')"),
    figure("fig8", "bar",
           caption("Figure 8. The long-term performance of our plans", numbering="Figure N."),
           mention(19, first=19, style=["figure 8"], count=1, pattern="as-shown-in", read=1,
                   lead="As is shown in figure 8, under the circumstances of an additional 50% "
                        "increase of the population by 2050",
                   trail="After adjustments of our hypothesized settings to meet the growth needs"),
           path=S_76, kind="result", panels=2, layout="1x2", shared=True, legend="below",
           note="two framed panels of grouped bars, Wellington left (three metric groups x three "
                "plan variants) and Anchorage right, sharing one legend inside the frame below the "
                "bars ('after adjustment', 'before adjustment', 'current plan'). The two panels "
                "print different y ranges - the left ticks 0.62 to 0.76 in steps of 0.02, the right "
                "0 to 1 - so a shared axis frame is a shared legend and a shared category axis, not "
                "a shared scale. Two measured boxes, one row: this row carries the left panel and "
                "the right is excluded as a fragment of the same exhibit"),
    figure("fig9", "line",
           caption("Figure 9. The sensitivity of resolution ratio", numbering="Figure N."),
           mention(19, pattern="none", read=1,
                   lead="We test the sensitivity of grey rational grade with and without our plan.",
                   trail="Take the example for the long-term plan. It is obvious that grey rational "
                         "grade with our plan is higher than that without plan."),
           path=S_77, kind="sensitivity", legend="inside",
           note="two curves of grey relational grade against the resolution ratio, keyed inside the "
                "plot in the upper right ('with plan' black squares, 'without plan' red squares), "
                "with a printed annotation at ratio=0.5 and a chart title above the frame. Named by "
                "deixis only - the sentence before it says 'We test the sensitivity ...' and never "
                "prints the number, so the mention block has an empty style list and a null "
                "first_page like Figure 2's"),
    figure("fig10", "flowchart-or-schematic",
           caption("Figure 10. Model Schematic Diagram", numbering="Figure N."),
           mention(22, first=15, style=["figure 10"], count=1, pattern="direct", read=0,
                   lead="More intuitive flow refers to figure 10(Appendix)."),
           path=S_APP, kind="appendix", numbered=False, solo=True,
           note="the model flow as a single column of six boxes joined by block arrows (Start, "
                "Addressing missing data, How is the data related to each factors, Choose the "
                "principle data related to SSG, Develop the plan in accordance with the priciple "
                "data) plus one box hanging off the right ('Determine the data related to reference "
                "series') fed by a right arrow and returning by a left one. Spelled 'priciple' "
                "inside the box. Prints alone on p22 under the 'Appendix' heading - the only "
                "solo-page exhibit in the paper - and is cited seven pages earlier, on p15: 'More "
                "intuitive flow refers to figure 10(Appendix)'"),
]

TABLES = [t for t in ALL if "table" in t]
FIGS = [t for t in ALL if "table" not in t]

EXCLUDED = [
    {"page": B["fig7r"][0], "bbox": B["fig7r"][1], "reason": "fragment-of-other",
     "note": "right panel of Figure 7 (Anchorage block of the 3-D column surface). The Figure 7 "
             "row carries the left panel; the two share one caption and one z axis label, and each "
             "draws its own colour bar"},
    {"page": B["tab7b"][0], "bbox": B["tab7b"][1], "reason": "split-across-pages",
     "note": "top of p16: rows A5-A7 of Table 7 plus the SES group cell, after the page turn. No "
             "header repeats and no 'continued' word prints. The Table 7 row carries the p15 head "
             "and rows A1-A4"},
    {"page": B["fig8r"][0], "bbox": B["fig8r"][1], "reason": "fragment-of-other",
     "note": "right panel of Figure 8 (Anchorage bars). The Figure 8 row carries the left panel; "
             "the two share one caption and one legend, but print different y ranges"},
]

RULES = [
    "Nine of the ten figures are drawings, not plots: Figures 1, 3, 4 and 5 are one three-circle "
    "Venn template reused for one component set per section (recorded family other, since no "
    "node, axis or scale is drawn) and Figures 2 and 10 are box-and-arrow schematics, so the only "
    "plotted exhibits are the radar, the two 3-D column blocks and the bar pair [geometry.family].",
    "Caption side splits by exhibit type and never mixes in this paper: all ten figure captions "
    "print under the artwork and all ten table captions print over the grid [caption.position].",
    "The numbering never settles: 'Figure1.' to 'Figure4.' glue the number to the title, 'Figure 5.' "
    "spaces it and keeps the stop, 'Figure 6' and 'Figure 7' space it and drop the stop, and "
    "'Figure 8.' to 'Figure 10.' return to the stop; the first four tables carry a stop after the "
    "number and Tables 5-9 drop it, all normalised to Figure N./Figure N and Table N./Table N "
    "with the printed form kept in the row note [caption.numbering].",
    "Every numbered exhibit is cited exactly once by number in the prose except four: Figures 2 and "
    "9 are never cited by number at all (deixis only) and Tables 2, 3 and 4 are cited twice, the "
    "second time together in one sentence on p12 [mention.count].",
    "The citation style is the plain imperative 'pay attention to figure N' / 'we show it in table "
    "N' for fifteen of the twenty rows; only Table 8 quotes its own number as subject ('Table 8 "
    "shows ...') and only Table 9 and Figure 8 use 'as shown in' [mention.lead_pattern].",
    "Lowercase 'figure N' and 'table N' is the house form; the single exception is 'table7', where "
    "the number is glued to the word, and the only capitalised citations are the three on p12 and "
    "the one on p17 [mention.style].",
    "One exhibit is cited seven pages before it prints: Figure 10 is announced on p15 as 'More "
    "intuitive flow refers to figure 10(Appendix)' and appears alone on the appendix page p22 "
    "[mention.lead_pages].",
    "The grids live in the model sections and the numbers live in the result sections: the "
    "indicator and plan grids sit under section kinds model and solution, the GRA table, the radar, "
    "the potential/rank tables and the performance figures under result, and the sensitivity curve "
    "alone under sensitivity [place.section_kind].",
    "The exhibit that eats the page is Table 1 at 0.372 of the page and the one that eats nothing is "
    "the measured half of Table 8 at 0.037; no exhibit in the paper is full-page, and the only "
    "solo-page one is the appendix schematic, which fills 0.196 of its page [place.area_frac].",
    "Exactly one row is extruded: Figure 7, whose two panels are both perspective column "
    "surfaces, and no other exhibit in the paper is drawn in depth [geometry.three_d].",
    "Exactly one row carries colour bars - Figure 7, one bar beside each of its two panels - and "
    "no other exhibit in the paper prints one [geometry.colorbar].",
    "Legends appear twice: the radar parks its key outside the plot on the right and the bar pair "
    "prints its key inside the frame below the bars. The four Venns look as though they have a "
    "legend in the upper right but it is a leader-line annotation, so they record none "
    "[geometry.legend].",
    "Only two figures are multi-panel and both are one row of two (Figure 7, Figure 8), each panel "
    "returning its own measured box, so one row per figure carries one panel [geometry.panel_count].",
    "The three indicator grids share one grouped layout: an outer metric cell spanning every data "
    "row, a group cell and its code spanning each block, and the tint applied per column and per "
    "block - not one table in the paper is row-striped [table.merged_cells].",
    "Three rule styles: Tables 2, 3, 4, 6 and 7 draw a rule between every column and the variables "
    "glossary does the same, Table 5 draws them inside its two header rows only, Table 1 draws a "
    "frame and per-row rules with partial verticals, and Tables 8 and 9 are booktabs - the rank "
    "table ending with no closing rule at all [table.rule_style].",
    "Only Table 5 prints two header rows, and only because it groups eight metric columns under "
    "three metric names [table.header_rows].",
    "Decimal alignment appears in exactly the two grids built from 4-dp grades, Table 5 and the "
    "measured block of Table 8 [table.decimal_aligned].",
    "One grid breaks across a page turn - Table 7, p15 into p16 - and like every other broken grid "
    "in this corpus it repeats nothing: no header row, no 'continued' word [table.continued].",
    "Only one caption names symbols: Table 1's parenthetical band prints G1, G2 and G3, and every "
    "other caption in the paper is a bare title with no unit, no condition and no parameter "
    "[caption.variable_count].",
    "Figure captions run 5 to 12 words and are single-sentence titles; not one states a unit, a "
    "condition or a conclusion, and all are nominal phrases rather than active clauses "
    "[caption.words].",
]

NOTE = (
    "Ten figures, nine tables and one uncaptioned variable glossary against 23 measured regions and "
    "3 exclusions. The exclusions are one table continuation (Table 7, p15 to p16, no header "
    "repeat) and two outer panels (the right half of Figure 7's 3-D column pair and the right half "
    "of Figure 8's bar pair). Nine of the ten figures are drawings rather than plots: Figures 1, 3, "
    "4 and 5 are one three-circle Venn template reused section by section, Figures 2 and 10 are "
    "box-and-arrow schematics, and only Figures 6, 7, 8 and 9 carry axes. The Venns are recorded as "
    "family other - no node, no axis, labels inside the circles, and the upper-right text is a "
    "leader-line annotation rather than a legend. Captions never mix sides: figures below, tables "
    "above, all twenty of them. The numbering splinters four ways ('Figure1.' glued, 'Figure 5.' "
    "spaced with a stop, 'Figure 6' spaced without one, 'Table 5' without a stop) and one citation "
    "glues its number to the word ('table7'). Two exhibits are never cited by number - Figure 2 and "
    "Figure 9 - and one is cited seven pages before it prints, Figure 10 on p15 pointing at the "
    "appendix page p22. Two coverage gaps are declared rather than patched: Table 8's Wellington "
    "block prints between its caption and y=562.3 pt with no measured region, and the four "
    "three-circle drawings carry their labels as artwork text that the text layer returns as body "
    "prose (Figure 3's caption runs straight into its first bullet)."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

for _e in ALL:
    _e["page_order"] = sorted(
        [x for x in ALL if x["page"] == _e["page"]],
        key=lambda x: (x["bbox"][1], x["bbox"][0])).index(_e) + 1
    _e["place"]["page_order"] = _e["page_order"]
for _n, _e in enumerate(sorted(ALL, key=lambda x: (x["page"], x["page_order"])), 1):
    _e["place"]["doc_order"] = _n


def main() -> int:
    from collections import Counter

    print("figures", len(FIGS), "tables", len(TABLES), "excluded", len(EXCLUDED))
    for k in ("family", "legend", "panel_count", "shared_axes", "three_d", "colorbar",
              "printed_numbers", "data_labels"):
        print(k, dict(Counter(e["geometry"][k] for e in FIGS)))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in ALL)))
    for k in ("position", "numbering", "voice", "words", "sentences", "units", "variables",
              "conditions", "concludes"):
        print("cap." + k, dict(Counter(e["caption"][k] for e in ALL)))
    for k in ("first_page", "lead_pages", "count", "lead_pattern", "read_sentences"):
        print("mention." + k, dict(Counter(e["mention"][k] for e in ALL)))
    for k in ("rule_style", "zebra", "merged_cells", "header_rows", "units_in_header",
              "decimal_aligned", "width", "orientation", "continued"):
        print("table." + k, dict(Counter(t["table"][k] for t in TABLES)))
    print("area", [e["place"]["area_frac"] for e in ALL])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
