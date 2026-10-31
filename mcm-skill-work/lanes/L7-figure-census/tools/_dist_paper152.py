"""Hand pass for P-B-2018-91566-2607f7ec (2018 MCM B, team 91566, "Forecasting the
Language Distribution": an Abrams-Strogatz competition model with migration, then a
six-office siting model on top of it).

26 pages, 24 measured regions on 15 of them. The paper pastes almost every formula as a
raster image, so most regions are displays rather than exhibits, and most of its tables
(Table 2 on p19 and Tables A1-A8 in the appendix) are native text-layer columns that the
region pass never boxes. Those unboxed tables are declared as coverage gaps in the note.

Usage: python -I tools/_dist_paper152.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2018-91566-2607f7ec"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))

DIMS = {pg["page"]: (pg["width"], pg["height"]) for pg in LAYOUT["pages"]}
REG = {(pg["page"], i): list(r["bbox"])
       for pg in LAYOUT["pages"] for i, r in enumerate(pg["regions"], 1)}
MEASURED = {(p, tuple(b)) for (p, _), b in REG.items()}

# Headings the extractor cannot see (they were pasted inside raster screenshots)
# and the appendix, which the paper never numbers, are recorded under this prefix.
UNCAP = "未编号标题："


def bb(page: int, index: int) -> tuple[int, list[float]]:
    return page, REG[(page, index)]


def place(page: int, bbox: list[float], path: list[str], kind: str) -> dict:
    w, h = DIMS[page]
    mid = (bbox[1] + bbox[3]) / 2
    z = "top" if mid < h / 3 else ("middle" if mid < 2 * h / 3 else "bottom")
    frac = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (w * h)
    return {
        "section_path": list(path),
        "section_numbered": not path[0].startswith(UNCAP),
        "section_kind": kind,
        "doc_order": 0,
        "page_order": 1,
        "page_zone": z,
        "area_frac": round(frac, 4),
        "solo_page": False,
    }


def cap(v: str, numbering: str = "Figure N", *, position: str = "below",
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
           panel_of: str = "", other_note: str = "") -> dict:
    page, bbox = B[key]
    item = {
        "page": page,
        "bbox": bbox,
        "family": geom["family"],
        "confidence": "high",
        "panel_count": geom["panel_count"],
        "is_panel_of": panel_of,
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
    if caption["numbering"] == "Figure N":
        caption = dict(caption, numbering="Table N")
    if caption["position"] == "below":
        caption = dict(caption, position="above")
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
B: dict[str, tuple[int, list[float]]] = {}

S_1 = ["1 Introduction"]
S_13 = ["1 Introduction", "1.3 Related Work"]
S_2 = ["2 Assumptions and Notations"]
S_22 = ["2 Assumptions and Notations", "2.2 Notations"]
S_3 = ["3 Model Construction"]
S_31 = S_3 + ["3.1 Worldwide Language Shift Model"]
S_311 = S_31 + ["3.1.1 Factors"]
S_312 = S_31 + ["3.1.2 Data Pre-processing"]
S_313 = S_31 + ["3.1.3 Worldwide Language Shift Model Construction"]
S_32 = S_3 + ["3.2 Domestic Language Shift Model"]
S_321 = S_32 + ["3.2.1 Domestic Language Shift Model Construction"]
S_33 = S_3 + ["3.3 Migration Model"]
S_331 = S_33 + ["3.3.1 Data Pre-processing"]
S_4 = ["4 Model Implementation and Results"]
S_42 = S_4 + ["4.2 Part I Problem B"]
S_43 = S_4 + ["4.3 Part I Problem C"]
S_45 = S_4 + ["4.5 Part II Problem B"]
S_5 = ["5 Sensitivity Analysis"]
S_51 = S_5 + ["5.1 Sensitivity Analysis for Ki"]
S_53 = S_5 + ["5.3 Sensitivity Analysis for Fitting Parameters"]
S_6 = ["6 Strengths and weaknesses"]
S_34 = [UNCAP + "3.4 Geographic Language Shift Model"]
S_APP = UNCAP


def app(title: str) -> list[str]:
    return [S_APP + "Appendices", S_APP + title]
# Pages 6-11: the notations table, Figure 1's transfer schematic, and the seven
# pasted equation blocks that surround them.

EXCLUDED.append(("p6-r1", bb(6, 1), "not-an-exhibit"))

B["nt1"] = bb(7, 1)
TABLES.append(table(
    "nt1", uncap("above"),
    mention(7, first=None, style=[], lead="", pattern="none", trail="", read=0),
    grid(18, 2, header=1, numeric=0, txt=2, rule="booktabs"),
    path=S_22, kind="symbols", caption_source="none",
    note="The notations table, printed with no number, no title and no caption: one header "
         "row over seventeen symbol rows (t, l, P, Q, T, tiev, w, G, Pr, K, c, a, s, D, R, V, "
         "M). Unlike every formula in this paper, the table is typeset rather than pasted, so "
         "it carries three booktabs rules and no vertical rule at all."))

EXCLUDED.append(("p9-r1", bb(9, 1), "not-an-exhibit"))
EXCLUDED.append(("p9-r2", bb(9, 2), "not-an-exhibit"))
EXCLUDED.append(("p10-r1", bb(10, 1), "not-an-exhibit"))

B["f1"] = bb(10, 2)
FIGURES.append(figure(
    "f1", cap("Figure 1: Global language shift schematic diagram"),
    mention(10, first=None, style=[], lead="", pattern="none",
            trail="The shift possibility can be expressed as:", read=1),
    geo("node-link-network", legend="none", numbers=True, labels=True),
    path=S_313, kind="model",
    note="Four population boxes inside one rounded container, joined by paired coloured "
         "arrows whose weights are written on the arrows themselves (Q(1,t) x P(1->2) and so "
         "on). No legend, no axes, no units: the encoding is entirely inline labelling, and "
         "the artwork is a drawing-tool export rather than a plot."))

EXCLUDED.append(("p10-r3", bb(10, 3), "not-an-exhibit"))
EXCLUDED.append(("p11-r1", bb(11, 1), "not-an-exhibit"))
EXCLUDED.append(("p11-r2", bb(11, 2), "not-an-exhibit"))
# Pages 12-18: three whole-page pasted screenshots, Figure 2's migration
# schematic, the Table 1 fitting result, and four pasted chart pairs where one
# embedded image carries two separately numbered figures.

EXCLUDED.append(("p12-r1", bb(12, 1), "not-an-exhibit"))
EXCLUDED.append(("p13-r1", bb(13, 1), "not-an-exhibit"))
EXCLUDED.append(("p14-r1", bb(14, 1), "not-an-exhibit"))

B["f2"] = bb(15, 1)
FIGURES.append(figure(
    "f2", cap("Figure 2: Geographical language shift schematic diagram"),
    mention(15, first=None, style=[], lead="", pattern="none", trail="", read=0),
    geo("flowchart-or-schematic", legend="none", numbers=True, labels=True,
        panels=3, layout="1+2"),
    path=S_34, kind="model",
    note="Three grey rounded panels - one nation centred on top, two below - holding four "
         "coloured community ellipses each, joined inside a panel by four double-headed "
         "arrows and between panels by one weighted arrow per route labelled "
         "Q(i1,l1,t) x V(i1,i2). The weights live on the arrows, so there is no legend, no "
         "axis and no unit anywhere; the whole diagram is a pasted JPEG rather than drawn "
         "vectors."))

B["t1"] = bb(15, 2)
TABLES.append(table(
    "t1", cap("Table 1: Fitting Result", "Table N:"),
    mention(15, first=None, style=[], lead="", pattern="none", trail="", read=0),
    grid(3, 3, header=1, numeric=3, txt=0, rule="booktabs"),
    path=S_34, kind="model", caption_source="typed-from-crop",
    note="Nine fitted parameters in a 3x3 block with no column headings at all, so the "
         "first row stands in for a header. Title and body are one pasted screenshot: the "
         "caption sits inside the image and never reaches the text layer, which is why it "
         "is transcribed from the crop rather than quoted. Three horizontal rules only."))

EXCLUDED.append(("p16-r1", bb(16, 1), "not-an-exhibit"))

B["f34"] = bb(16, 2)
FIGURES.append(figure(
    "f34", cap("Figure 3: Native Speakers Quantities in 2068 "
               "Figure 4: Total Speakers Quantities in 2068"),
    mention(16, first=16, style=["Figure 3", "Figure 4"], count=2,
            lead="Figure 3 and figure 4 indicates the number changes and Figure 5 and "
                 "figure 6 indicates the proportion changes.",
            pattern="direct", read=0),
    geo("composite-panel", legend="inside", numbers=True, panels=2, layout="1x2"),
    path=S_42, kind="result",
    note="Two stacked-area charts pasted as ONE embedded image: native speakers on the "
         "left, total speakers on the right, 26 language bands each, legends dropped below "
         "the x axis inside the image. Both x axes run 2017 to 2068 in three-year steps but "
         "the y axes disagree in notation - 5E+09 on the left, 6000000000 on the right - "
         "and neither carries an axis title or a data label. The two captions share one "
         "printed line under the pair."))

B["f56"] = bb(17, 1)
FIGURES.append(figure(
    "f56", cap("Figure 5: Native Speakers Proportions inFigure 6: Total Speakers "
               "Proportions in 2068"),
    mention(17, first=16, style=["Figure 5", "Figure 6"], count=2,
            lead="Figure 5 and figure 6 indicates the proportion changes.",
            pattern="direct",
            trail="In this way, we can say that other 25 languages geographical "
                  "distribution will not change a lot in the next 50 years.", read=3),
    geo("composite-panel", legend="inside", numbers=True, panels=2, layout="1x2"),
    path=S_43, kind="result",
    note="The same two languages sets re-plotted as 100% stacked areas, left native and "
         "right total, again one embedded image with 26-entry legends below each x axis. "
         "Y axes are percent only, 0 to 100 in tens. The caption line is physically broken: "
         "Figure 5's text runs straight into 'Figure 6:' with no separator and the year "
         "'2068' wraps alone onto the next line. This row's x axes stop at 2067 in "
         "two-year steps while the page-16 pair ran three-year steps to 2068."))

B["f78"] = bb(17, 2)
FIGURES.append(figure(
    "f78", cap("Figure 7: Native Speakers Rank in 50 years "
               "Figure 8: Total Speakers Rank in 50 years"),
    mention(17, first=16, style=["Figure 7", "Figure 8"], count=2,
            lead="we plot the top 15 rank of languages according to native speakers "
                 "quantities and total speakers quantities in 50 years.",
            pattern="parenthetical",
            trail="Among the top 10 languages native speakers languages, only Punjabi "
                  "(10th th) is replaced by Wu Chinese.", read=2),
    geo("composite-panel", legend="inside", numbers=True, panels=2, layout="1x2"),
    path=S_43, kind="result",
    note="Two rank line charts in one embedded image, 15 languages each, y axis inverted "
         "1 to 19 so rank 1 sits at the top and ranks are read off position rather than "
         "printed labels. Legends inside the image below the x axis. Cited parenthetically "
         "as '(Figure 7 and figure 8)' before the pair appears, which is the only mention "
         "either gets."))

B["f910"] = bb(18, 1)
FIGURES.append(figure(
    "f910", cap("Figure 9: Distribution of English in 2018 "
                "Figure 10: Distribution of English in 2068"),
    mention(18, first=17, style=["Figure 9", "Figure 10"], count=1,
            lead="We can observe the geographical distribution of English straightly from "
                 "Figure 9 and 10.",
            pattern="direct", read=0),
    geo("composite-panel", legend="none", numbers=False, panels=2, layout="1x2"),
    path=S_43, kind="result",
    note="Two choropleth world maps - English in 2018 beside English in 2068 - inside one "
         "embedded image. No legend, no colourbar, no country names, no scale bar, no "
         "graticule and no printed numbers: the shading is the entire encoding, so a reader "
         "cannot calibrate a shade to a value."))

EXCLUDED.append(("p18-r2", bb(18, 2), "not-an-exhibit"))
# Pages 20-25: Figure 11's three-panel sensitivity strip and the appendix table
# fragments that the region pass happens to box.

B["f11"] = bb(20, 1)
FIGURES.append(figure(
    "f11", cap("Figure 11: Sensitivity Analysis for Fitting Parameters", "Figure N:"),
    mention(20, first=20, style=["Figure 11"], count=2,
            lead="These three parameters impact the whole model during prediction and are "
                 "very important.",
            pattern="as-shown-in",
            trail="The results are showed in the Figure 11.", read=3),
    geo("composite-panel", legend="below", panels=3, layout="1x3", labels=False),
    path=S_53, kind="sensitivity",
    note="Three stacked-area panels a/b/c in one row, one per fitting parameter, each with "
         "its own frame, its own y axis repeated from 0 to 30,000,000 and no axis titles or "
         "units at all. One unbordered 26-entry key sits below the row and serves all three "
         "panels, so the legend is below rather than inside as in every other figure here. "
         "The panel letters are the only thing tying a strip to a parameter."))

B["ta3c"] = bb(24, 1)
TABLES.append(table(
    "ta3c", uncap("above"),
    mention(24, first=None, style=[], lead="", pattern="none", trail="", read=0),
    grid(12, 3, header=1, numeric=2, txt=1, rule="booktabs", continued=True),
    path=app("Table A3: Language ANOVA"), kind="appendix", caption_source="none",
    note="Twelve continuation rows of Table A3 (Malay through Yue Chinese) after the caption "
         "and the Language / F-value / P-value header stayed behind on p23. Horizontal rules "
         "only, no vertical rule, numbers left-aligned so the columns are ragged on the right."))

B["ta4c"] = bb(25, 1)
TABLES.append(table(
    "ta4c", uncap("above"),
    mention(25, first=None, style=[], lead="", pattern="none", trail="", read=0),
    grid(2, 3, header=1, numeric=2, txt=1, rule="booktabs", continued=True),
    path=app("Table A4: Country ANOVA"), kind="appendix", caption_source="none",
    note="The last two rows of Table A4 (United States, Viet Nam) carrying no header and no "
         "caption of their own; the caption inside this crop belongs to Table A5 below it."))

B["ta7"] = bb(25, 2)
TABLES.append(table(
    "ta7", cap("Table A7: ANOVA Analysis of the Language Population Proportions in 2068",
               "Table N:"),
    mention(25, first=None, style=[], lead="", pattern="none", trail="", read=0),
    grid(4, 3, header=1, numeric=2, txt=1, rule="booktabs"),
    path=app("Table A7: ANOVA Analysis of the Language Population Proportions in 2068"),
    kind="appendix",
    note="Header q / F-value / F-crit over three q values, no vertical rules. Its near-twin "
         "Table A6 sits directly above it with the same q and F-crit columns and different "
         "F-values, so this is the second of a pair rather than a duplicated paste. The one "
         "F-value prints as 8.8131 followed by a detached superscript 10-5, and the text "
         "layer renders the decimal point as a colon."))
RULES: list[str] = [
    "Caption side is decided by kind, not by fit: every figure is captioned below the "
    "artwork (7 of 7) and every boxed table above it (5 of 5), so a reader never has to "
    "look twice for the label. [caption.position]",
    "This paper always prints the colon form - 'Figure 2:', 'Table 1:' - on both kinds, "
    "and the colon is the only numbering style present, so the extractor's colonless "
    "'Figure N' should be treated as a stale default here. [caption.numbering]",
    "Five of the seven figures are composite-panel, because the authors pasted two "
    "separately numbered figures into a single embedded image rather than laying out two "
    "objects; the census must therefore count printed numbers, not regions. "
    "[geometry.panel_count]",
    "Every panel pair is laid out side by side, never stacked, and where a panel has a key "
    "it keeps its own, so a pair is read as one exhibit with two independent axes rather "
    "than one continuous series. [geometry.family]",
    "The legend never floats free of the artwork: it sits inside the image under the x axis "
    "on the three chart pairs, below the whole strip on Figure 11, and is absent with no "
    "substitute on the two schematics and on the map pair. [geometry.legend]",
    "Nothing in this paper is three-dimensional - every exhibit is a flat area, rank line, "
    "choropleth or hand-drawn schematic - confirmed on the page crops rather than assumed "
    "from the family. [geometry.three_d]",
    "No caption names a variable, states a unit, gives a condition or draws a conclusion: "
    "captions are bare 'what + where/when' noun phrases throughout. [caption.variables]",
    "The year is the only quantity a chart caption ever carries, and it is the only place "
    "the horizon is stated; axes carry no title, so the year in the caption is load-bearing. "
    "[caption.words]",
    "All five boxed tables share one recipe: horizontal rules only, no vertical divider, "
    "which makes the columns read as flowing prose blocks rather than a grid. "
    "[table.rule_style]",
    "Continuation fragments keep no header and no caption of their own - the appendix "
    "tables that cross a page boundary resume as bare rows. [table.continued]",
    "No table uses zebra striping, merged cells or a diagonal header, so a wide numeric "
    "table is disambiguated by rule position alone. [table.zebra]",
    "Header rows are minimal: the fitting-result table prints no headings at all and the "
    "notations table prints exactly one, so the recorded header row is the minimum the "
    "schema allows rather than what the eye sees. [table.header_rows]",
    "The two kinds occupy disjoint territories: figures live in the model, result and "
    "sensitivity sections, tables in the symbols, model and appendix sections, and neither "
    "kind appears in the introduction, the assumptions or the conclusion. "
    "[place.section_kind]",
    "Five of the seven figures are cited by number and three of those pointers are on an "
    "earlier page than the artwork; the two that are never cited are the two schematics, "
    "which are self-explanatory by design. [mention.first_page]",
    "Pre-figure pointers prefer naming the exhibit inside a running sentence ('Figure 3 "
    "and figure 4 indicates ...') over a parenthetical or a bare cross-reference, and the "
    "parenthetical is reserved for the rank pair. [mention.lead_pattern]",
    "Two of the five cited charts are never interpreted in prose; the other three get "
    "between two and three reading sentences each, so half of this paper's chart space "
    "carries no written reading. [mention.read_sentences]",
    "No table in the paper is ever cited by number - not the captioned Table 2, not the "
    "eight appendix tables - so a table number here is a label for the reader's eye, not a "
    "cross-reference target. [mention.style]",
    "Post-figure prose sits immediately after the caption line with no blank-paragraph "
    "buffer, so a context weld has to key on the caption, not on vertical whitespace. "
    "[place.page_order]",
    "Every exhibit is part of a page, never alone on one, and the largest occupies well "
    "under half the sheet, so no exhibit here earns a page of its own. [place.solo_page]",
    "The unboxed tables are the census's real gap: Table 2 and the appendix tables are "
    "native text-layer columns that never became a region, so boxed-count alone would "
    "under-state the paper's tables by a factor of two. [place.area_frac]",
]

NOTE = (
    "Coverage gap, declared rather than patched. The measured layout boxes 24 regions on "
    "15 of the 26 pages, and only 12 of those regions are exhibits: 7 figures and 5 tables. "
    "The rest are pasted equation blocks (pages 12, 13, 14 are each a single page-sized "
    "screenshot of prose plus display mathematics, and equations 28, 29 and 30 are separate "
    "smaller pastes). Several tables were never boxed at all, because they are native "
    "text-layer columns rather than images: Table 2 (Office Locations, p19) and Tables A1, "
    "A2, A3, A4, A5, A6, A7 and A8 in the appendix. Of those, A3, A4 and A7 happen to fall "
    "inside regions that the layout did box (p24 and p25), so the three entries recorded "
    "here are the continuation rows and the final table of a longer appendix run; the "
    "remaining five appendix tables and Table 2 are recorded nowhere in this payload and "
    "are known to exist. Any aggregation of table shapes from this record should be read as "
    "'the five boxed tables', not 'the paper's tables'. "
    "Two further cautions for anyone reusing these fields. First, four regions each hold "
    "TWO separately numbered figures pasted into one embedded image (Figures 3+4 on p16, "
    "5+6 and 7+8 on p17, 9+10 on p18), so one region carries one composite-panel item and "
    "the printed numbers outrun the region count. Second, those caption lines are physically "
    "unreliable: on p16 and p18 the two captions run together on one printed line with no "
    "separator, and on p17 the pair collides ('Proportions inFigure 6') and wraps a stray "
    "'2068' onto the following line, so a caption-to-panel mapping taken from line adjacency "
    "will mis-assign; the left/right position on the page is the only safe key. "
    "The two schematics (Figures 1 and 2) are pasted raster exports with no axes, no "
    "legend and no unit, and their encodings are inline arrow labels; Figure 2's caption is "
    "the only thing that says which nation is which. Table 1's caption lives inside its "
    "screenshot and never reaches the text layer, so it is transcribed from the crop and "
    "marked typed-from-crop; the same is true of the notations table's absent title."
)
ALL: list[dict] = FIGURES + TABLES
_order = sorted(ALL, key=lambda it: (it["page"],
                                     round((it["bbox"][1] + it["bbox"][3]) / 2),
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
    f"unclaimed {sorted(MEASURED - _claimed)} extra {sorted(_claimed - MEASURED)}")
assert len(ALL) + len(EXCLUDED) == len(MEASURED) == 24, (
    len(ALL), len(EXCLUDED), len(MEASURED))

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": FIGURES,
    "tables": TABLES,
    "excluded_regions": [
        {"key": k, "page": p, "bbox": b, "reason": r} for k, (p, b), r in EXCLUDED
    ],
    "rules": RULES,
    "note": NOTE,
}


def main() -> None:
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"figures {len(FIGURES)} tables {len(TABLES)} excluded {len(EXCLUDED)} "
          f"-> {out.name}")
    fam: dict[str, int] = {}
    for it in FIGURES:
        fam[it["geometry"]["family"]] = fam.get(it["geometry"]["family"], 0) + 1
    print("families", dict(sorted(fam.items())))
    legs: dict[str, int] = {}
    for it in FIGURES:
        legs[it["geometry"]["legend"]] = legs.get(it["geometry"]["legend"], 0) + 1
    print("legends", dict(sorted(legs.items())))
    pos = {"figure": {}, "table": {}}
    for it in FIGURES:
        pos["figure"][it["caption"]["position"]] = pos["figure"].get(
            it["caption"]["position"], 0) + 1
    for t in TABLES:
        pos["table"][t["caption"]["position"]] = pos["table"].get(
            t["caption"]["position"], 0) + 1
    print("caption side", pos)
    rules: dict[str, int] = {}
    for t in TABLES:
        rules[t["table"]["rule_style"]] = rules.get(t["table"]["rule_style"], 0) + 1
    print("rule styles", rules)
    widths = sorted({round(t["bbox"][2] - t["bbox"][0], 1) for t in TABLES})
    print("table widths pt", widths)
    print("cited exhibits", sum(1 for it in FIGURES if it["mention"]["first_page"]))
    print("numbered captions",
          sum(1 for it in FIGURES if it["caption"]["numbering"] != "none"))
    kinds: dict[str, int] = {}
    for it in ALL:
        kinds[it["place"]["section_kind"]] = kinds.get(it["place"]["section_kind"], 0) + 1
    print("section kinds", dict(sorted(kinds.items())))


if __name__ == "__main__":
    main()
