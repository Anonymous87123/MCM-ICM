"""Hand pass for P-E-2017-65123-e36461ec (smart growth index, 15 figures + 3 tables).

Shape of the paper: five pasted Office drawings that stand in for figures and tables of the
method (Fig 1 flow chart, Fig 2 EWM steps, Fig 3 GDM tree, Fig 4 indicator mind map, Fig 5
standard composite), one satellite pair (Fig 6), one radar-plus-bar composite (Fig 7), one SVM
contour (Fig 8), four evaluation line charts (Figs 9-12), two five-radar decade strips (Figs
13-14) and one MATLAB surface (Fig 15). Three printed tables: an uncaptioned symbol glossary,
the 25-indicator framework that breaks across a page, and the nested weight table.

What the record has to say out loud:

1. Ten of the fifteen figures are not drawn for print: Figs 1-4 are Office drawings pasted as
   low-resolution rasters with drop shadows and broken words inside the shapes ("Compartment",
   "Developm ent", "Coordi nation"), Figs 8 and 15 are raw libsvm/MATLAB exports, Fig 6 is a
   web-GIS screenshot pair. Nothing on these pages carries an axis title.
2. The caption grammar has no steady state: "Fig.1", "Fig.2", "Fig.3.", "Fig.13." (space, no
   period), "Fig 14.", "Fig.15", "Tab.1", "Tab.2" - four spellings of the figure prefix and one
   of the table prefix that the numbering vocabulary does not contain.
3. The three tables are ruled three ways and none of them is boxed except Tab.2: the symbol
   glossary is booktabs and carries no caption at all, Tab.1 has a filled navy header band,
   row rules and zebra shading with no frame, and Tab.2 is fully boxed with vertical merges.
4. Two cross-references point at the wrong exhibit and one at the wrong kind of exhibit: the
   standard-of-smart-growth text cites "fig.4" for what Fig.5 draws, the Ningguo population
   paragraph cites "Fig.8" (the SVM contour) for the growth curve of Fig.12, and the two
   evaluation diagrams are read as "the result of ranking the individual initiatives".
5. Two coverage gaps are declared: the two 5x5 judgment matrices at the foot of page 9 print
   with no rules and no caption, so the detector returns no region for them, and the appendix
   MATLAB listing on page 23 is a full-page code block with no region either.

Usage: python -I tools/_dist_paper134.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-E-2017-65123-e36461ec"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((LANE / f".proxy/{PID}-ctx.json").read_text(encoding="utf-8"))

REG = {}
PAGE_W = PAGE_H = None
for pg in LAYOUT["pages"]:
    PAGE_W = pg["width"]
    PAGE_H = pg["height"]
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

HEAD: dict[str, str] = {}
for _h in CTX["headings"]:
    _n, _l = _h.get("number"), _h.get("label")
    if not _n or not _l or not _l.startswith(_n + " "):
        continue
    if _n not in HEAD:
        HEAD[_n] = _l


def P(*numbers: str) -> list[str]:
    return [HEAD[n] for n in numbers]


EXCLUDED = [
    {"page": 6, "bbox": REG[(6, 1)], "reason": "fragment-of-other",
     "note": "continuation of Tab.1 on the next page: 17 more indicator rows (x9 to x19) with "
             "no header row repeated and the split row 'Industrial waste gas emission: x8' cut "
             "in half, its Unit cell (ppm) and Type cell (ESU) left on page 5."},
    {"page": 8, "bbox": REG[(8, 2)], "reason": "in-body-diagram",
     "note": "the correlation-coefficient display equation r(E,S) sitting in step III of the EWM "
             "text: typeset math with no caption and no frame. The detector box also under-covers "
             "it - its left edge starts at the numerator's sigma, so the 'r(E,S) =' prefix is "
             "outside the measured region."},
    {"page": 13, "bbox": REG[(13, 3)], "reason": "fragment-of-other",
     "note": "right half of Figure 6: the Ningguo satellite tile. One printed number covers the "
             "pair and the caption is centred under both, so the Figure 6 row carries the "
             "Pittsburgh tile and this is the second panel, not a second exhibit."},
]


def text(page: int) -> str:
    return schema.norm((PAGES / f"page-{page:04d}.txt").read_text(
        encoding="utf-8", errors="replace"))


def place(page: int, idx: int, path: list[str], kind: str, numbered: bool = True) -> dict:
    b = REG[(page, idx)]
    mid = (b[1] + b[3]) / 2
    z = "top" if mid < PAGE_H / 3 else ("middle" if mid < 2 * PAGE_H / 3 else "bottom")
    frac = (b[2] - b[0]) * (b[3] - b[1]) / (PAGE_W * PAGE_H)
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 0,
        "page_zone": z,
        "area_frac": round(frac, 3),
        "solo_page": frac > 0.5,
    }


def caption(v: str, *, numbering: str = "Fig. N", cond: bool = False,
            concl: bool = False, units: bool = False, vars_: int = 0,
            pos: str = "below", voice: str = "none") -> dict:
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


def figure(page: int, idx: int, family: str, cap: dict, men: dict, *, path: list[str],
           kind: str, legend: str = "none", printed: bool = False,
           labels: bool = False, panels: int = 1, layout: str = "1",
           shared: bool = False, colorbar: bool = False, three_d: str = "no",
           numbered: bool = True, note: str = "") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "family": family,
        "other_note": None,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": cap["verbatim"],
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, idx, path, kind, numbered),
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


def table(page: int, idx: int, cap: dict, men: dict, grid: dict, *, path: list[str],
          kind: str, note: str = "", numbered: bool = True,
          source: str = "text-layer") -> dict:
    return {
        "page": page,
        "bbox": REG[(page, idx)],
        "caption_verbatim": cap["verbatim"],
        "caption_source": source,
        "note": note,
        "place": place(page, idx, path, kind, numbered),
        "mention": men,
        "caption": cap,
        "table": grid,
    }


def grid(rows: int, cols: int, *, header: int = 1, rules: str = "boxed", zebra: bool = False,
         merged: bool = False, diag: bool = False, units_hdr: bool = False,
         decimal: bool = False, numeric: int = 0, txt: int = 0, width: str = "column",
         orient: str = "portrait", continued: bool = False, note_sentence: str = "") -> dict:
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


_LIG = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"}


def _fold(s: str) -> tuple[str, list[int]]:
    out: list[str] = []
    idx: list[int] = []
    for i, ch in enumerate(s):
        rep = _LIG.get(ch, ch)
        for c in rep:
            out.append(c)
            idx.append(i)
    return "".join(out), idx


def _find(page: int, needle: str, after: int = 0) -> tuple[str, int, int]:
    t = text(page)
    f, idx = _fold(t)
    n, _ = _fold(needle)
    j = f.find(n, after)
    assert j >= 0, f"{needle!r} not on page {page}"
    return t, idx[j], idx[j + len(n) - 1] + 1


def _to_word_end(page: int, pos: int) -> int:
    t = text(page)
    k = t.find(" ", pos)
    return len(t) if k < 0 else k


def span(page: int, start: str, end: str) -> str:
    t, i, _ = _find(page, start)
    _, j, jend = _find(page, end, i)
    q = t[i:_to_word_end(page, jend)].strip()
    assert len(schema.words(q)) <= 25, f"{len(schema.words(q))} words: {q}"
    return q


S12 = P("1.2")
S22 = P("2.2")
S321 = P("3.2.1")
S331 = P("3.3.1")
S332 = P("3.3.2")
S341 = P("3.4.1")
S342 = P("3.4.2")
S352 = P("3.5.2")
S41 = P("4.1")
S42 = P("4.2")
S521 = P("5.2.1")
S53 = P("5.3")
S61 = P("6.1")
S62 = P("6.2")
S71 = P("7.1")
S72 = P("7.2")
S8 = P("8")

ALL = [
    figure(3, 1, "flowchart-or-schematic",
           caption("Fig.1 The flow chart in this paper", numbering="Fig. N"),
           mention(3, first=3, style=["fig.1"], count=1, pattern="as-shown-in",
                   lead=span(3, "Through the above analysis",
                             "shown in fig.1")),
           path=S12, kind="introduction",
           note="a PowerPoint-style flow chart pasted as a raster: two dashed rounded frames "
                "(analysis above, solution below), five olive index bars (TOL/CD/SED/EDL/TQ), "
                "five yellow TASK I-V ovals, grey method bubbles and detached callouts, plus a "
                "decorative mini bar chart labelled 'The ten principles' and 'SMART GROWTH'. No "
                "axes, no legend, no numbers. Words inside the shapes are mistyped ('Compartson "
                "and research', 'TASKV', 'SVV', 'WMM / AM')"),
    figure(8, 1, "flowchart-or-schematic",
           caption("Fig.2 The flow of calculation weights of indicators using EWM",
                   numbering="Fig. N"),
           mention(8, first=8, style=["fig.2"], count=1, pattern="as-shown-in",
                   lead=span(8, "The detailed algorithm is shown", "in fig.2.")),
           path=S331, kind="model",
           note="a five-stage left-to-right process strip pasted as a low-resolution raster: five "
                "drop-shadowed rounded boxes ('Dimension For Data', 'Entropy value', 'Correlation "
                "coefficient', 'Portfolio Optimization', 'Weight Obtain') above five circles "
                "Step I-V joined by block arrows. The second tier is not aligned with the first - "
                "'Portfolio Optimization' sits left of its own circle. No axes, no numbers"),
    figure(9, 1, "node-link-network",
           caption("Fig.3. The GDM for determine planning scheme of city",
                   numbering="Fig. N", pos="below"),
           mention(9, first=9, style=["Fig.3"], count=1, pattern="parenthetical",
                   lead=span(9, "We get the indicators in the above text", "(cf. Fig.3):")),
           path=S332, kind="model",
           note="a three-level hierarchy drawn as a raster with drop shadows: a top box 'Smart "
                "Growth(SG)' over four expert boxes joined by edges labelled lambda1-lambda4, then "
                "five leaf boxes for the five metrics. Edges cross densely and no key relates the "
                "lambdas to the experts. Two words are hard-wrapped inside their boxes "
                "('Developm ent', 'Coordi nation'). No axes, no numbers"),
    figure(12, 1, "node-link-network",
           caption("Fig.4. Three-level indicator system diagram", numbering="Fig. N"),
           mention(12, first=11, style=["Fig.4", "fig.4"], count=3, pattern="as-shown-in",
                   lead=span(11, "The three levels of evaluation indicators", "Fig.4"),
                   read=1,
                   trail=span(12, "From the fig.4, we can see",
                              "divided into three levels.")),
           path=S342, kind="model",
           note="a radial mind map with curved connectors and glow halos, three rings of word-art "
                "ellipses: the SDSG root, the five first-class metrics and their second-class "
                "indicators. Two ellipses collide ('Collaboration in development' over "
                "'Industrial solid waste emission') and one label is broken mid-word ('Water "
                "consumptio n'). No axes, no numbers, no legend. The sentence that introduces it "
                "sits at the foot of page 11, the drawing at the head of page 12"),
    figure(13, 1, "composite-panel",
           caption("Fig.5. The Standard of Smart Growth", numbering="Fig. N"),
           mention(13, first=13, style=["fig.5"], count=1, pattern="as-shown-in",
                   lead=span(13, "The standard line is also shown", "in the fig.5.")),
           path=S352, kind="model", legend="inside", printed=True, labels=True,
           panels=7, layout="strips-and-radar",
           note="a seven-part composite: five horizontal qualitative range strips on the left "
                "(Standard of CD / IOL / EDL / SED / TQ, each running 0 to 1 with two printed "
                "thresholds), a five-axis radar on the right carrying the same nine vertex values "
                "as Fig.7, and one wide SDSG strip along the bottom. Legend inside the radar "
                "(blue 'Super Line' / orange 'Bottom Line'). The strips are swatches, not data: "
                "the colour spans the whole 0-1 width in every one of them. A second in-drawing "
                "title reads 'Radar diagram of standard with 5 indexes'"),
    figure(13, 2, "photo-or-raster-image",
           caption("Fig.6. The satellite map of the selected city", numbering="Fig. N"),
           mention(13, first=13, style=["fig.6"], count=1, pattern="as-shown-in",
                   lead=span(13, "As shown in fig.6", "on the right.")),
           path=S41, kind="other", panels=2, layout="1x2",
           note="two satellite tiles side by side under one caption and one number: Pittsburgh "
                "left, Ningguo right, told apart only by the running sentence - neither tile is "
                "labelled. Both are web-GIS screenshots, complete with place labels, icons, red "
                "markers and a traced white boundary polygon that the text never explains. No "
                "axes, no legend, no scale"),
    figure(14, 1, "composite-panel",
           caption("Fig.7. The index value of the selected city", numbering="Fig. N"),
           mention(14, first=14, style=["fig.7"], count=2, pattern="as-shown-in",
                   lead=span(14, "The result is shown in fig.7", "as fellows."),
                   read=1,
                   trail=span(14, "Firstly, as we can see", "from fig.7.")),
           path=S42, kind="evaluation", legend="inside", printed=True, labels=True,
           panels=2, layout="1x2",
           note="radar on the left, grouped bar chart on the right, one number, two panels that do "
                "not share a scale (the radar has no ticks, the bars run 0-1). Two legends: one "
                "inside the radar ('Ningguo' / 'Pittsburgh'), one under the bar chart in two rows "
                "('Bottom line' / 'Super Line'). All ten bar values printed on the bars (0.320 to "
                "0.724), the nine radar vertices repeat Fig.5's numbers exactly. The bar order "
                "(IOL, TQ, SED, CD, EDL) differs from the radar's clockwise order"),
    figure(16, 1, "heatmap-or-contour",
           caption("Fig.8. The result of the grid search method on SVM", numbering="Fig. N"),
           mention(16, first=16, style=["fig.8"], count=2, pattern="as-shown-in",
                   lead=span(16, "The result of grid search is shown", "in fig.8."),
                   read=1,
                   trail=span(16, "From the fig.8, we can see",
                              "outstanding performance")),
           path=S521, kind="model", printed=True,
           note="a libsvm grid-search contour plot: coloured contour bands over a dense scatter of "
                "search points, labelled contours in red (67 to 82) and an unlabelled dashed grid. "
                "x 'log2c', y 'log2g', both -8..8 step 2; the y title is overprinted by its own "
                "tick labels. No legend, no colourbar, no marked best point although the text "
                "reports c = 2^4, g = 2^-3. Raw tool export, not journal-styled"),
    figure(17, 1, "line",
           caption("Fig.9 The evaluation diagram of smart growth plan", numbering="Fig. N"),
           mention(17, first=17, style=["fig.9"], count=1, read=1,
                   trail=span(17, "From fig.9 we can see", "growth in general.")),
           path=S53, kind="evaluation", legend="inside", printed=True, labels=True,
           note="four line series (new and current plan for each city) with the legend inside the "
                "plot along the top, plus a two-line in-plot key 'P: Pittsburgh / N: Ningguo'. x "
                "2016-2030 step 2, y 0-1 step 0.2, neither axis titled although the text claims "
                "both are. Only two values are printed on the data (0.595259 and 0.315635). Three "
                "hand-drawn curved arrows annotated 'Rapid growth' and 'Stable fluctuate' (the "
                "second label duplicated) sit over the curves; the text calls the new-plan line "
                "yellow although it is drawn orange"),
    figure(17, 2, "line",
           caption("Fig.10 The evaluation diagram of smart growth plan in Pittsburgh",
                   numbering="Fig. N"),
           mention(17, first=17, style=["fig 10", "fig.10"], count=2, pattern="as-shown-in",
                   lead=span(17, "With this method, forecasting results", "fig 10 and fig.11."),
                   read=1,
                   trail=span(18, "Fig.10 is the result of ranking", "initiatives in Pittsburgh.")),
           path=S61, kind="result", legend="inside", printed=True, labels=True,
           note="line-and-bar combo on two y axes: four legend entries inside the plot along the "
                "top ('Initiatives 1', 'Initiatives 3', 'Initiatives 2', 'Current plan' - the "
                "3-before-2 order is the paper's), left axis 0-1, right axis 0-0.1, x 2016-2030. "
                "Neither axis is titled and nothing says which series belongs to which axis; the "
                "bar strip has no legend entry of its own although the text calls it 'the "
                "histogram'. City name printed inside the plot as a heading. One value labelled "
                "(0.595259)"),
    figure(18, 1, "line",
           caption("Fig.11 The evaluation diagram of smart growth plan in Ningguo",
                   numbering="Fig. N"),
           mention(18, first=17, style=["fig.11"], count=3, pattern="as-shown-in",
                   lead=span(17, "With this method, forecasting results", "fig 10 and fig.11."),
                   read=1,
                   trail=span(18, "Fig.11 is the result of ranking", "initiatives in Ningguo.")),
           path=S61, kind="result", legend="inside", printed=True, labels=True,
           note="the same dual-axis template as Fig.10 with two legend rows (Initiatives 1/2/3 and "
                "Current plan, then Initiatives 4/5), same untitled axes, same unexplained bar "
                "strip, Ningguo printed inside the plot. One labelled value (0.315635). The paper "
                "reads both evaluation diagrams as rankings of the individual initiatives"),
    figure(19, 1, "line",
           caption("Fig.12. The population growth of two cities", numbering="Fig. N"),
           mention(19, first=18, style=["fig.12"], count=1, pattern="as-shown-in",
                   lead=span(18, "The prediction of population growth",
                             "fig.12 as follows.")),
           path=S62, kind="result", legend="inside", printed=True,
           note="two dotted line series (Ningguo, Pittsburgh) with a boxed legend inside the plot "
                "at the upper right, x 1996-2016 step 2, y 0-60 step 10. The unit note '10000 "
                "people' is printed inside the frame instead of as a y-axis title, and no value is "
                "labelled on any point. The last Ningguo point runs past the final tick. The "
                "caption says 'growth' but the axis plots absolute population"),
    figure(19, 2, "composite-panel",
           caption("Fig 13. Dynamic change of SDSG in decades with 50% population till 2050 in "
                   "Pittsburgh City", numbering="Fig. N", cond=True),
           mention(19, first=19, style=["fig.13"], count=1, pattern="direct",
                   lead=span(19, "By planning the rule adaptively", "like the fig.13.")),
           path=S71, kind="result", panels=5, layout="3-2 zig-zag", shared=True,
           note="five radars on the same five uncalibrated axes (CD, SED, TQ, EDL, IOL), arranged "
                "three over two and chained by four curved arrows labelled 'One decade' three "
                "times and 'Half decade' once - though the last hop is 2046 to 2050, four years. "
                "Years are printed in grey tags outside each radar; each polygon is a different "
                "colour with no legend mapping colour to year. No ticks, no numbers at any vertex, "
                "no colourbar. Same template as Fig.14"),
    figure(20, 1, "composite-panel",
           caption("Fig 14. Dynamic change of SDSG in decades with 50% population till 2050 in "
                   "Ningguo City", numbering="Fig. N", cond=True),
           mention(20, style=[], count=0),
           path=S72, kind="result", panels=5, layout="3-2 zig-zag", shared=True,
           note="the Fig.13 template a second time, only the polygon shapes and stroke colours "
                "differ: identical arrow geometry, identical grey year tags (2016 to 2050), "
                "identical orange reference band, identical 'Half decade' error on the 2046-2050 "
                "hop. Never cited by number - the text points at it as 'the figure as shown "
                "below'"),
    figure(20, 2, "surface-or-3D",
           caption("Fig.15 The sensitivity analysis of SVM predict model", numbering="Fig. N"),
           mention(20, first=20, style=["fig.15"], count=1, pattern="as-shown-in",
                   lead=span(20, "The sensitivity analysis of the SVM is shown",
                             "in fig.15.")),
           path=S8, kind="sensitivity", three_d="surface-mesh",
           note="a MATLAB surf export: coloured MSE surface with an unexplained flat red wireframe "
                "floating above it, x 'log2c', y 'log2g', z 'MSE' (clipped at the left edge), z "
                "0-1, x and y labelled -5, 0, 5. No colourbar and no legend, so the height cannot "
                "be read off the plane; vertical grid lines cross the surface. Caption says "
                "'predict' for prediction"),
]

TABLES = [
    table(4, 1,
          caption("", numbering="none"),
          mention(4, style=[], count=0),
          grid(9, 2, header=1, rules="booktabs", numeric=0, txt=2, width="full"),
          path=S22, kind="symbols", source="none",
          note="the symbol glossary of section 2.2 printed with no caption and no number at all: "
               "one bold header row ('Symbol', 'Definition') and eight rows, booktabs rules "
               "(top, under the header, bottom) and not one vertical rule. No units, no numbers, "
               "no note row. The prose never refers to it by name"),
    table(5, 1,
          caption("Tab.1 Framework of sustainability indicators", numbering="Table N",
                  pos="above"),
          mention(5, first=5, style=["Tab. 1"], count=1, pattern="direct",
                  lead=span(5, "Primary indicators are shown", "in Tab. 1.")),
          grid(26, 4, header=1, rules="no-rules", zebra=True, numeric=1, txt=3, width="full",
               continued=True),
          path=S321, kind="model",
          note="the 25-indicator framework in four columns (Indicator, Unit, Explanation, Type): "
               "a filled navy header band, one thin rule between every row, zebra row shading - "
               "and no outer frame and no vertical rule anywhere, so it is recorded as no-rules "
               "rather than booktabs. Units stand in their own column (Percent, Sq. M, Ton, ppm, "
               "'-'), never in the header. It breaks across the page: 8 rows on page 5, 17 more on "
               "page 6 with the header NOT repeated and one row cut in half, and no 'continued' "
               "marker is printed anywhere. A prose paragraph explaining the Type codes follows "
               "the grid on page 6, outside the table. Its own introducing sentence breaks the same "
               "way the grid does: 'The composition of the second-class indicators and the weight "
               "composition are' ends page 10 and 'shown as below.' opens page 11 above the caption"),
    table(11, 1,
          caption("Tab.2 The weight of second-class indicator", numbering="Table N",
                  pos="above"),
          mention(11, first=11, style=["Tab.2"], count=1, pattern="direct",
                  lead=span(10, "The composition of the second-class indicators",
                            "weight composition are")),
          grid(21, 4, header=1, rules="boxed", merged=True, numeric=0, txt=4, width="full"),
          path=S341, kind="model",
          note="the only boxed table in the paper: outer frame, a vertical rule between every "
               "column, a rule around every row, and a header row that prints the same pair of "
               "titles twice ('Second-class indicator' / 'Primary indicator and weight' for the "
               "left and right halves). Vertical merges carry each first-class metric over its "
               "block - IOL and SED over five rows, CD over five, TQ over four, EDL over three - "
               "and two cells ('Gross Domestic Product (19%)', 'Per capita fiscal expenditure "
               "(27%)') are merged across the two right-hand columns with no second-class partner. "
               "No zebra; pale block fills instead. Percentages are printed inline in every label"),
]

RULES = [
    "版式跟着论证阶段走：model 章吃掉 7 件（Fig 2、3、4、5、8 与 Tab.1、Tab.2），evaluation 2 件"
    "（Fig 7、Fig 9），result 5 件（Fig 10-14），sensitivity 只有 1 件（Fig 15），introduction "
    "1 件（Fig 1），symbols 1 件（无题注的符号表）[place.section_kind]。",
    "七张图是贴上去或工具导出的，不是为印刷画的：Fig 1、2、3、4 是带投影的 Office 剪贴栅格（形状里还有 "
    "'Compartson'、'Developm ent'、'Coordi nation' 这类断词与错词），Fig 8 是 libsvm 网格搜索导出，"
    "Fig 15 是 MATLAB surf 导出，Fig 6 是两张网页 GIS 截图 [geometry.family]。",
    "手工拼的图基本不写轴题：Fig 9/10/11 的横纵轴只有刻度没有名字，要紧靠正文补一句“横轴是时间、"
    "纵轴是 SDSG”才读得懂，Fig 12 把单位 '10000 people' 印在绘图区里当注记；全篇只有 Fig 8 与 "
    "Fig 15 两张工具导出图带轴题（log2c / log2g / MSE）[geometry.printed_numbers]。",
    "有图例就全在绘图区内、没有一图例在外：6 张图的图例全部 inside（Fig 5、7、9、10、11、12，"
    "雷达图例在右上、折线与柱的图例沿顶边横排），其余 9 张根本没有图例；15 张图零 colorbar，连 "
    "Fig 15 这张三维曲面也没有，高度无从读起 [geometry.legend][geometry.colorbar]。",
    "三维只有一处：Fig 15 是 surface-mesh，其余 14 张全是二维平面图，没有一张透视图或等轴图 "
    "[geometry.three_d]。",
    "复合版是两种不同的拼法：Fig 5 是“5 条区间色带 + 1 个雷达 + 1 条 SDSG 长条”共 7 个部件拼成一个"
    "编号，Fig 7 是雷达与分组柱左右并列（两栏量程不同，shared_axes=false）；Fig 13/14 是 5 个雷达"
    "按 3-2 蛇形排开并共用同一组五轴（shared_axes=true）；Fig 6 是一个编号下两张卫星瓦片 "
    "[geometry.panel_count][geometry.panel_layout][geometry.shared_axes]。",
    "题注方位按展品类型分工且没有例外：15 张图的题注一律在图形下方，2 张带题注的表一律在表格上方，"
    "符号表根本没有题注（caption_source=none）[caption.position]。",
    "编号写法全篇不统一：'Fig.1' 与 'Fig.2' 无点，'Fig.3.' 到 'Fig.12.' 有点，'Fig 13.' 与 "
    "'Fig 14.' 用空格代替点，'Fig.15' 又无点；表一律写 'Tab.1'/'Tab.2' 而正文写 'Tab. 1'。封闭词表"
    "里没有 'Fig N'、'Fig N.' 与 'Tab. N'，因此 15 张图统一记成 'Fig. N'、2 张表统一记成 "
    "'Table N'（表题实际印 'Tab.1'/'Tab.2'，也都不带句点），具体印法写进行注 "
    "[caption.numbering]。",
    "题注全是名词短语、不给单位也不下结论：词数 5-16，voice 18 条全为 none，units 与 variables 全假；"
    "句数 8 条为 1、9 条为 2——凡编号带句点的题注都被那个句点切成了两句，是排版假象不是双句题注；"
    "唯一带条件的是 Fig 13/14（'with 50% population till 2050'）[caption.words][caption.sentences]"
    "[caption.voice][caption.conditions]。",
    "指代靠 'as shown in' 铺满全篇：11 张图的首引是 'shown in fig.N' / 'as shown in fig.N' 句式，Fig 3 "
    "用括号式 'cf. Fig.3'，Fig 13 是直陈式，Fig 9 没有引出句只留解读句，Fig 14 从头到尾只被“下图”"
    "指过（first_page=null）；Fig 1、2、5、6 的正文写法是小写 'fig.N' [mention.lead_pattern]"
    "[mention.style][mention.first_page]。",
    "首次提及页通常就是展品页（13 件 lead_pages=0），三个例外：Fig 4 在 p11 页末点名、p12 页首印出"
    "（lead_pages=1），Fig 11 与 Fig 12 分别由前一页的同一句预告（lead_pages=1），Fig 4 的首引句与"
    "图之间还隔着一行页码 [mention.lead_pages]。",
    "图后解读句几乎不写：15 张图里只有 6 张有解读句（Fig 4、7、8、9、10、11），其余 9 张读完就换节；"
    "引用次数也低，11 件只被点一次，Fig 4 与 Fig 11 各三次、Fig 7/8/10 各两次，Fig 14 与符号表从头到尾"
    "没被点过名 [mention.read_sentences][mention.count]。",
    "三张表三种规制，说明这套模板里没有统一的表风格：符号表是 booktabs 且无题注，Tab.1 是“填充"
    "表头带 + 行间细线 + 隔行底纹 + 无外框”（记为 no-rules，因为它一条竖线也没有），只有 Tab.2 "
    "是全包围并带纵向合并 [table.rule_style][table.zebra][table.merged_cells]。",
    "跨页续表的代价写进记录：Tab.1 在 p5 断在 'Industrial waste gas emission: x8' 这一行中间，"
    "p6 续 17 行却不重复表头，也没有 continued 标记，读者只能靠列宽猜列名；续表那块区域登记为 "
    "fragment-of-other [table.continued][table.header_rows]。",
    "单位从不写进表头：Tab.1 专设 Unit 列（Percent、Sq. M、Ton、ppm、'-'），Tab.2 把百分比写进每个"
    "指标名，符号表没有单位；三张表没有一张做小数点对齐，宽度都是满版心、都是纵向 "
    "[table.units_in_header][table.decimal_aligned][table.width][table.orientation]。",
    "排除项三处，全部是“同一件展品的另一半”或“正文里的数学”：p6 中段是 Tab.1 的续表，p13 右半是 "
    "Fig 6 的第二张瓦片，p8 底部是 EWM 第三步的相关系数公式（in-body-diagram）[place.area_frac]。",
    "两处覆盖缺口明说：p9 页脚两个 5x5 判断矩阵既无框也无题注，检测器不给区域；p23 整页 MATLAB "
    "代码同样没有区域——都按缺口登记，不拿自造 bbox 去补 [table.rows]。",
]

NOTE = (
    "Fifteen figures and three tables on 23 pages against 21 measured regions: 18 exhibits, 3 "
    "exclusions and two declared coverage gaps. Seven of the fifteen figures are not drawn for "
    "print - Figs 1-4 are Office drawings pasted as low-resolution rasters whose shapes carry "
    "broken words, Fig 8 is a libsvm grid-search export, Fig 15 a MATLAB surface export, and Fig "
    "6 a pair of web-GIS screenshots - so not one figure in the paper prints an axis title. The "
    "caption grammar never settles: 'Fig.1', 'Fig.3.', 'Fig 13.', 'Fig.15' are four different "
    "figure prefixes and the tables are 'Tab.1' / 'Tab.2', none of them inside the numbering "
    "vocabulary, so all are recorded normatively with the printed form in the row note. Every "
    "figure caption prints below its artwork and both captioned tables print above the grid; the "
    "symbol glossary on page 4 prints with no caption at all. The three tables are ruled three "
    "ways and only Tab.2 is boxed: the glossary is booktabs, Tab.1 is a filled header band with "
    "zebra rows and no frame that breaks across pages without repeating its header, and Tab.2 "
    "merges each first-class metric over its block. Two cross-references point at the wrong "
    "exhibit ('fig.4' for the standard drawn in Fig.5, 'Fig.8' for the population curve of Fig.12) "
    "and the two evaluation diagrams are read as rankings. Figures 13 and 14 are one template "
    "printed twice."
)

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ALL,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

for _e in ALL + TABLES:
    _e["page_order"] = sorted(
        [x for x in ALL + TABLES if x["page"] == _e["page"]],
        key=lambda x: (x["bbox"][1], x["bbox"][0])).index(_e) + 1
    _e["place"]["page_order"] = _e["page_order"]
for _n, _e in enumerate(sorted(ALL + TABLES, key=lambda x: (x["page"], x["page_order"])), 1):
    _e["place"]["doc_order"] = _n


def main() -> int:
    from collections import Counter

    rows = ALL + TABLES
    print("figures", len(ALL), "tables", len(TABLES), "excluded", len(EXCLUDED))
    for k in ("family", "legend", "panel_count", "shared_axes", "three_d", "colorbar",
              "printed_numbers", "data_labels"):
        print(k, dict(Counter(e["geometry"][k] for e in ALL)))
    print("kind", dict(Counter(e["place"]["section_kind"] for e in rows)))
    print("section", dict(Counter(" > ".join(e["place"]["section_path"]) for e in rows)))
    for k in ("position", "numbering", "voice", "words", "sentences", "units", "variables",
              "conditions", "concludes"):
        print("cap." + k, dict(Counter(e["caption"][k] for e in rows)))
    for k in ("first_page", "lead_pages"):
        print("mention." + k, dict(Counter(e["mention"][k] for e in rows)))
    print("pattern", dict(Counter(e["mention"]["lead_pattern"] for e in rows)))
    print("count", dict(Counter(e["mention"]["count"] for e in rows)))
    print("read", dict(Counter(e["mention"]["read_sentences"] for e in rows)))
    for k in ("rule_style", "zebra", "merged_cells", "header_rows", "units_in_header",
              "decimal_aligned", "width", "orientation", "continued"):
        print("table." + k, dict(Counter(t["table"][k] for t in TABLES)))
    print("zone", dict(Counter(e["place"]["page_zone"] for e in rows)))
    print("doc_order", [(e["page"], e["place"]["doc_order"]) for e in sorted(rows, key=lambda x: x["place"]["doc_order"])])
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
