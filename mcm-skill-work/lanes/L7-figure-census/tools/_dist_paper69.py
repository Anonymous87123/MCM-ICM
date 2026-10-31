"""Hand census of P-C-2014-31262-1f9007fa (C-31262, 20 pages).

Twenty-five measured regions over ten pages: eight figure rows and eleven table rows,
five exclusions, nothing unmeasured. The paper prints eight figures and ten tables.

  p11 r1  Table 1     summary statistics for the co-author network
  p11 r2  Figure 1a   bar chart of the five connected components
  p11 r3  Figure 1b   degree histogram
  p12 r1  Figure 2    the co-author network, Gephi layout with a circular zoom inset
  p12 r5  Table 3     top 30 authors by betweenness centrality
  p13 r1  Table 5     top 30 authors by PageRank
  p13 r2  Table 6     variable glossary for the PCA model
  p13 r3  Table 7a    the five rankings, rows 1-5
  p14 r1  Table 7b    the five rankings, rows 6-10
  p14 r2  Figure 7    three-spoke radar, top three authors
  p14 r3  Table 8a    the sixteen papers, header and rows 1-3 / 9-11
  p15 r1  Table 8b    the sixteen papers, rows 4-8 / 12-16
  p15 r2  Figure 3    citation network of the sixteen papers
  p15 r3  Table 9     the sixteen papers ranked four ways
  p16 r1  Figure 5    the citation network, detail of paper 11 and 12
  p16 r2  Figure 4    four series of normalised values over the sixteen papers
  p17 r1  Figure 6    the department network, three colleges
  p17 r2  Table 10a   the ten Douban users, rows 1-6
  p18 r1  Table 10b   the ten Douban users, rows 7-10
  p18 r2  Figure 8    distribution of the impact measure over 971 users

Declared gaps: Tables 2 and 4 own no region. The drawing pass chains every grid on this
paper into its neighbour, because the gap between one grid's closing rule and the next
grid's top rule is 18 to 34 pt, well under the 120 pt the detector uses to close a table.
So the p12 box spans Table 2's top rule at 446.1 pt to Table 4's header rule at 712.8 pt
with Table 3 whole inside it, and the p13 box spans Table 4's six rows to Table 5's
closing rule at 275.1 pt. Each box is recorded once, as the exhibit it contains whole -
Table 3 and Table 5 - and Tables 2 and 4 are declared here instead of being given a box
they do not own.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2014-31262-1f9007fa"
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

PROPS = "4.1.2 Analyzing the properties of this network"
TASK2 = "4.2 Task2"
CITEMODEL = "4.3.2 Developing the co-author (citation) model"
MEASUREMENT = "4.3.3 Paper influence measurement"
UTILITIES = "4.3.4 Utilities in other areas"
DOUBAN = "4.4.2 User influential analysis"

MEASURE = 506.7
DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def qp(text: str, pages: list[int]) -> str:
    """Same guard, for a sentence that may print on a neighbouring page."""
    for page in pages:
        if schema.norm(text) in schema.page_text(PID, page):
            return schema.norm(text)
    raise KeyError((pages, text[:70]))


def pct(span: float) -> str:
    return f"{span / MEASURE * 100:.1f}"


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
          pattern: str = "direct", read: int = 1, gap: int | None = None,
          trail: str = "") -> dict:
    """A by-number citation the text layer prints; check_mention re-quotes the sentence."""
    pages = sorted({page - 1, page, page + 1, first_page - 1, first_page, first_page + 1})
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": qp(lead, pages) if lead else "",
            "trail_sentence": qp(trail, pages) if trail else "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": gap}


def caption(verbatim: str, numbering: str = "none", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap: str, numbering: str, mention: dict,
           path: list[str], kind: str, *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           three_d: str = "no", source: str = "text-layer", numbered: bool = True,
           position: str = "below", note: str = "", other_note: str = "") -> None:
    word = q(cap, page) if (cap and source == "text-layer") else schema.norm(cap)
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
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": False, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, rows: int, cols: int, path: list[str], kind: str,
          note_sentence: str, note: str, *, rule: str = "booktabs", numeric: int = 1,
          header_rows: int = 1, numbered: bool = True, width: str = "full",
          zebra: bool = False, merged: bool = False, decimal: bool = False,
          diagonal: bool = False, continued: bool = False, cap: str = "",
          position: str = "above", mention: dict | None = None) -> None:
    word = q(cap, page) if cap else ""
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": word,
        "caption_source": "text-layer" if cap else "none",
        "note": note,
        "place": place(page, reg, path, kind, numbered),
        "mention": mention or none_mention(),
        "caption": caption(word, "TABLE N" if cap else "none", position),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued,
                  "note_sentence": qp(note_sentence, [page, page + 1]) if note_sentence else ""},
    })


# ---------------------------------------------------------------- p11, the opening grid
table(11, 1, 11, 2, [PROPS], "other",
      "The value of the average degree of all the vertices means that in average, each author "
      "collaborates with 6.920 authors.",
      "A two-column grid ruled top, under the header and bottom - the top and bottom rules are "
      "1.44 pt thick and doubled, the header rule 0.72 pt - with ONE vertical stroke at x 338.7 pt "
      "running the height of the table in one segment per row, and no side borders, so the rule "
      "style is vertical-rules rather than booktabs. Eleven printed rows: the header 'Value' and "
      "ten statistics - Nodes 474, Edges 1640, Average Degree 6.920, Connected Components 5, "
      "Density 0.015, Average Clustering Coefficient 0.282, Modularity 0.493, Number of Triangles "
      "1828, Diameter (Longest Path Length) 10, Average Path Length 3.825. 254.2 pt against the "
      "506.7 pt measure (50.2 per cent), so the narrowest grid in the paper and recorded half; it "
      "is also the only grid on the paper that does not run into the margins. Labels are centred "
      "against centred values of unequal width, so nothing is decimal-aligned. The caption prints "
      "15.4 pt above the top rule, with a double space after the stop that the layer reproduces "
      "('TABLE 1.  Summary statistics').",
      numeric=1, width="half", rule="vertical-rules",
      cap="TABLE 1. Summary statistics for co-author network",
      mention=cited(10, 11, ["TABLE 1"], 1,
                    "we import the data into Gephi and get some information from it, showing in "
                    "TABLE 1."))

# ---------------------------------------------------------------- p11, the two-panel Figure 1
figure(11, 2, "bar",
       "Figure 1. Component and degree distribution", "Figure N.",
       cited(11, 11, ["FIGURE 1"], 2,
             "In order to have a more direct recognition, we visualize some properties in "
             "FIGURE 1.",
             trail="FIGURE 1 shows the distribution of components and degrees."),
       [PROPS], "other", numbers=True, labels=False,
       note="The LEFT of the two framed panels that print under one caption, and the pair is "
            "recorded as two rows because the drawing pass measures two boxes 52.3 pt apart and "
            "each holds a different chart. This one is a filled bar chart: five vertical columns on "
            "a categorical x axis 'Coponent ID' 0 to 4 - the misspelling is printed inside the "
            "figure - against 'Count' 0 to 500. Component 0 rises to about 470 and the other four "
            "sit on the axis, which is exactly the five connected components Table 1 lists on the "
            "same page with one component holding nearly every vertex. Y-axis tick labels only, no "
            "values printed over the bars, no legend, no gridlines, full rectangular frame, MATLAB "
            "default blue. The caption prints 26.3 pt below the panel at y 590.4 pt. Cited twice "
            "by number, both on its own page.")

figure(11, 3, "histogram",
       "Figure 1. Component and degree distribution", "Figure N.",
       cited(11, 11, ["FIGURE 1"], 2,
             "In order to have a more direct recognition, we visualize some properties in "
             "FIGURE 1.",
             trail="FIGURE 1 shows the distribution of components and degrees."),
       [PROPS], "other", numbers=True, labels=False,
       note="The RIGHT panel of Figure 1: contiguous bars on a continuous x axis 'Degree' -10 to "
            "60, 'Count' 0 to 90, bin width one degree, so a degree distribution and not a "
            "categorical bar chart. The mode is at degree 1 with about 83 vertices and the tail runs "
            "to 55, which matches the average degree 6.920 and the diameter 10 that Table 1 prints "
            "beside it. The axis starts at -10 although no degree is negative, so the first tenth "
            "of the plot area carries no data. No value is printed over any bar and there is no "
            "legend; the two panels share no axis and carry separate titles inside the art "
            "('Statistic of Component', 'Statistic of Degree'). Cited twice by number on p11.")

# ---------------------------------------------------------------- p12, the Gephi layout
figure(12, 1, "node-link-network",
       "Figure 2.The co-author network", "Figure N.",
       cited(11, 12, ["Figure 2"], 2, "See Figure 2.",
             trail="In Figure 2, there are many circles with different colors."),
       [PROPS], "other", numbers=False, labels=True, legend="outside-right",
       note="A pasted Gephi screenshot, not line art: four image blocks in the top band of the "
            "page - the main layout 708x700 px at 104.2 to 336.0 pt, two leader lines and the "
            "circular inset ring as vector paths at 193.0 to 520.0 pt, and the inset itself in two "
            "nested rasters, 445x415 px at 366.5 to 512.4 pt and 316x293 px at 381.5 to 495.6 pt. "
            "The main layout is a force-directed hairball of about 470 vertices drawn as small "
            "discs in eight or nine colours with a dense grey edge mat; two leader lines run from a "
            "hand-drawn ellipse over its centre to the circular inset at the right, which magnifies "
            "that centre into some forty labelled magenta discs. Vertex labels are surnames in "
            "small type and are barely legible even at review resolution, so they are recorded as "
            "present but not transcribed; no numeric value is printed inside the art. The prose "
            "says the circles are coloured by modularity class and sized by degree, which is what "
            "the two-tone inner rings and the varying disc radii show. One printed caption, one "
            "row: the inset is a magnified detail of the same drawing, not a second exhibit, so "
            "panel_count stays 1 and the three other regions are recorded as fragments.")

EXCLUDED.append({
    "page": 12,
    "bbox": REG[(12, 2)],
    "kind": KIND[(12, 2)],
    "reason": "fragment-of-other",
    "note": "the two leader lines and the inset ring of Figure 2, 193.0 to 520.0 pt by 125.9 to "
            "287.0 pt, drawn as four vector paths. They join the main layout to its magnified "
            "detail and carry no data of their own; counting them would book a third of the "
            "exhibit separately",
})

EXCLUDED.append({
    "page": 12,
    "bbox": REG[(12, 3)],
    "kind": KIND[(12, 3)],
    "reason": "fragment-of-other",
    "note": "the circular zoom inset of Figure 2, a 445x415 px raster at 366.5 to 512.4 pt by "
            "137.9 to 273.8 pt, holding about forty labelled magenta discs - the magnified centre "
            "of the layout recorded as the p12 r1 row",
})

EXCLUDED.append({
    "page": 12,
    "bbox": REG[(12, 4)],
    "kind": KIND[(12, 4)],
    "reason": "duplicate",
    "note": "a 316x293 px raster at 381.5 to 495.6 pt by 153.6 to 259.4 pt sitting wholly inside "
            "the inset above it - the same magnified discs printed twice, once as the frame and "
            "once as its content. Duplicate, not a second panel",
})

# ---------------------------------------------------------------- p12, the first of the top-30 grids
table(12, 5, 7, 10, [TASK2], "other",
      "TABLE 2 to TABLE 5 show the top 30 authors based on closeness centrality, betweenness "
      "centrality, degree centrality, and PageRank.",
      "A booktabs grid of three rules - top 1.44 pt at 570.3 pt, header 0.72 pt at 585.1 pt, "
      "closing 1.44 pt at 665.0 pt - spanning 47.9 to 563.5 pt with no vertical stroke anywhere, "
      "the top and closing rules visibly thicker than the header rule and each broken into "
      "segments at the five block boundaries. Seven printed rows over ten columns: one header row "
      "reading 'Rank Name' five times, then the six ranks that carry all thirty authors, ranks 1 "
      "to 30 dealt three ways - down each block and across the page. 515.6 pt against the 506.7 pt "
      "measure is 101.8 per cent: the grid overhangs the text measure by 6.1 pt on the left and "
      "2.8 pt on the right, as every wide grid on this paper does. Integers in the rank column and "
      "surnames with initials in the name column, both centred, so nothing is decimal-aligned. "
      "THIS BOX IS NOT THIS GRID ALONE: the measured region spans Table 2's top rule at 446.1 pt "
      "to Table 4's header rule at 712.8 pt, with Table 2's six rows above and Table 4's caption "
      "and header band below. Table 3 is the only exhibit wholly inside it, so the box is booked "
      "here and Tables 2 and 4 are declared gaps in the note.",
      numeric=5, width="full",
      cap="TABLE 3. Top 30 authors based on betweenness centrality",
      mention=cited(12, 12, ["TABLE 3"], 1,
                    "TABLE 2 to TABLE 5 show the top 30 authors based on closeness centrality, "
                    "betweenness centrality, degree centrality, and PageRank."))

# ---------------------------------------------------------------- p13, two grids and the glossary
table(13, 1, 7, 10, [TASK2], "other",
      "A few authors are highly ranked in all the tables.",
      "Booktabs, three rules at 182.9 pt (1.44 thick), 197.1 pt (0.72) and 273.6 pt (1.44), "
      "spanning 47.9 to 563.5 pt, no vertical stroke. Seven printed rows over ten columns - one "
      "header row 'Rank Name' five times and the six ranks holding all thirty authors by "
      "PageRank. 515.6 pt, 101.8 per cent of the measure, overhanging both margins like every wide "
      "grid here. THIS BOX CARRIES TWO EXHIBITS: its top edge is the closing rule of Table 4 at "
      "149.3 pt, whose six data rows print at 73.9 to 137.6 pt above this grid's caption, with "
      "Table 4's own caption and header band left behind on p12. Table 5 is the exhibit wholly "
      "inside the box and is what this row records; Table 4 is a declared gap.",
      numeric=5, width="full",
      cap="TABLE 5. Top 30 authors based on PageRank",
      mention=cited(12, 13, ["TABLE 5"], 2,
                    "TABLE 2 to TABLE 5 show the top 30 authors based on closeness centrality, "
                    "betweenness centrality, degree centrality, and PageRank."))

table(13, 2, 6, 2, [TASK2], "symbols",
      "Some variables and their meanings are listed here for convenience",
      "A two-column glossary, and the only grid in the paper ruled the other way: a full-width "
      "rule at 442.4 pt under the caption, a full-width rule at 457.4 pt under the header, a "
      "vertical stroke at x 236.6 pt running the whole table in one segment per row, and then two "
      "rules at 486.9 and 516.5 pt that stop at that vertical - 237.3 to 460.1 pt only. The left "
      "column therefore has no rule below its header and no closing rule at all, so rule_style is "
      "vertical-rules and not booktabs and the grid is open at the foot of the Variable side. Six "
      "printed rows: Variable/Meaning header, then IM/Impact measurement, Central/The metric for "
      "Centralizing Characteristics, Connect/..., Spread/... and the fourth row's Greek symbols "
      "alpha, beta, gamma with 'Weighting coefficient'. 308.0 pt against the 506.7 pt measure "
      "(60.8 per cent), centered, recorded half. No numeric column, so numeric_cols is 0 and "
      "decimal_aligned false. The caption sits 14.4 pt above the top rule, and the sentence that "
      "introduces the grid ends in a full-width colon the crop preserves and the layer flattens.",
      numeric=0, width="half", rule="vertical-rules",
      cap="TABLE 6. Variable and their meaning",
      mention=cited(13, 13, ["TABLE 6"], 1,
                    "Some variables and their meanings are listed here for convenience"))

table(13, 3, 7, 10, [TASK2], "result",
      "TABLE 7 shows the top 10 authors according to each characteristic respectively",
      "The first half of a grid that breaks over the page foot. Two header rows and no rule "
      "between them: a spanner row at 626.2 pt reading Central, Connect, Spread, Final IM, Final IM "
      "and a rank row at 638.8 pt reading 'Rank Name' five times, all under one 1.44 pt rule at "
      "623.7 pt and over rows 1 to 5, which print at 651.4 to 701.9 pt. A 1.44 pt rule at 713.6 pt "
      "closes the page, and the grid resumes at the top of p14. No vertical stroke separates the "
      "five blocks - whitespace does. 515.6 pt, 101.8 per cent of the measure. Ten columns and "
      "seven rows on this page; the five rank columns are integers and the five name columns are "
      "surnames, all centred, so nothing is decimal-aligned. The caption prints 14.9 pt above the "
      "top rule with a full stop and no colon.",
      numeric=5, header_rows=2, width="full",
      cap="TABLE 7. Top 10 authors based on central, connect and spread",
      mention=cited(13, 13, ["TABLE 7"], 2,
                    "TABLE 7 shows the top 10 authors according to each characteristic respectively",
                    trail="From TABLE 7, we obtain the final comprehensive rank of these authors."))

table(14, 1, 5, 10, [TASK2], "result",
      "From TABLE 7, we obtain the final comprehensive rank of these authors.",
      "The second half of Table 7: rows 6 to 10 at 74.5 to 124.9 pt, closed by one 1.44 pt rule "
      "at 136.7 pt, with NO header row repeated on this page - the spanner row and the rank row "
      "print only on p13, which is why header_rows stays 1 and continued is true. 515.6 pt against "
      "the 506.7 pt measure. Rows 1 to 5 on p13 plus these five give the ten printed rows the "
      "caption promises on each of the five rankings; the rightmost block carries ranks 1 to 10 "
      "and the left blocks 1 to 5 here and 1 to 5 there, so the reading order is block-major.",
      numeric=5, width="full", continued=True)

# ---------------------------------------------------------------- p14, the radar
figure(14, 2, "other",
       "Figure 7. Comparison of top three author in the final rank", "Figure N.",
       cited(14, 14, ["Figure 7"], 1,
             "Figure 7 provides the comparison between Top3 authors."),
       [TASK2], "other", numbers=True, labels=False, legend="outside-right",
       other_note="A three-spoke radar (spider) plot with three overlaid closed polylines. The "
                  "closed vocabulary has no radar member and the ink is neither line-over-axes "
                  "nor bar, so it is filed as other rather than forced into a family.",
       note="A radar chart, and the only exhibit in the paper with no family to name it. Three "
            "spokes at 120 degrees - Centralizing Characteristics at the top, Connecting "
            "Characteristics lower right, Spreading Characteristics lower left - over a pentagon "
            "grid of two rings at 0.5 and 1.0, one closed polyline per author. The three series "
            "are ALON,N rank1 (blue, square markers), RODL,V rank2 (black, triangles) and "
            "GRAHAM,RL rank3 (green, squares), keyed in a legend OUTSIDE the frame at the upper "
            "right, which also carries the ranks. ALON,N sits highest on Centralizing and lowest "
            "on Connecting; GRAHAM,RL is the mirror image, which is the difference the prose claims "
            "the figure shows. Titles are printed INSIDE the art in two lines above the plot; the "
            "caption prints 6 pt under the frame at 417.4 pt. Cited once by number, on p14.")

# ---------------------------------------------------------------- p14/p15, the sixteen papers
table(14, 3, 4, 4, [CITEMODEL], "model",
      "For each paper, we assign a number from one to sixteen to it for convenience (shown in "
      "TABLE 8).",
      "The head of a grid that breaks over the page foot and, unusually, is left OPEN at the "
      "bottom: three thin 0.72 pt rules at 648.6, 662.9 and 678.0 pt, a vertical stroke at x 95.4 "
      "pt after each Number column, and no closing rule anywhere - the box ends where p14 ends and "
      "p15 resumes with more rows, and the last of them is closed by nothing at all. Four "
      "columns laid as two side-by-side blocks of (Number, Article Name): header row 'Number "
      "Article Name Number Article Name' at 649.9 pt, then rows 1-3 on the left and 9-11 on the "
      "right. 515.6 pt against the 506.7 pt measure, 101.8 per cent. The grid is the paper's own "
      "index of the sixteen papers, and it is the list against which Table 9 and Figures 3, 4 and "
      "5 number their vertices. Rule style is booktabs plus one vertical per block, recorded "
      "vertical-rules.",
      numeric=2, rule="vertical-rules", width="full",
      cap="TABLE 8. Articles’ Number")

table(15, 1, 5, 4, [CITEMODEL], "model",
      "",
      "The rest of Table 8 on the far side of the page turn: rows 4-8 on the left and 12-16 on "
      "the right, three thin rules at 72.0, 101.4 and 141.3 pt, the same vertical at x 95.4 pt, no "
      "header repeated and NO closing rule - the grid simply stops at 156.4 pt and Figure 3's "
      "frame begins 16 pt below it. Four columns, four blocks of (Number, Article Name). Together "
      "with the p14 part this is one printed grid of seventeen rows over four columns, measured as "
      "two regions and booked as two rows with continued true.",
      numeric=2, rule="vertical-rules", width="full", continued=True)

# ---------------------------------------------------------------- p15, the citation network
figure(15, 2, "node-link-network",
       "Figure 3. The citation network of 16 papers", "Figure N.",
       cited(14, 15, ["FIGURE 3"], 2,
             "FIGURE 3 shows the structure of our model.",
             trail="In FIGURE 3, we demonstrate the citation relation of the sixteen papers."),
       [CITEMODEL], "model", numbers=False, labels=True, legend="none",
       note="A pasted screenshot, not line art: sixteen circles of strongly varying radius filled "
            "with radial gradient shading in red, yellow, green, blue and magenta, standing on the "
            "white page with no frame, no axes and no gridlines. Each circle carries a truncated "
            "paper title in very small type - the same sixteen papers Table 8 indexes and Tables 9 "
            "and 10 rank - and NOT a number, so printed_numbers is false and data_labels true. "
            "Edges are directed straight arrowheads drawn between circle edges in as many colours "
            "as the discs, and they overlap heavily in the middle. No legend and no key: the "
            "colours repeat the vertex colours of Figure 2 and are never explained. The prose "
            "reads size as degree and calls out circle 11 as the largest with a low rank and circle "
            "12 as small with the top rank. Caption below the art at 356.8 pt. Cited twice by "
            "number, once on p14 a page before the art.",
       )

table(15, 3, 18, 8, [MEASUREMENT], "result",
      "In TABLE 9, we list the rank of the sixteen papers according to their centralizing, "
      "connecting, spreading and comprehensive contributions to the whole network.",
      "Booktabs: one 1.44 pt rule at 416.4 pt above the spanner row, NO rule under the header "
      "band, and one 1.44 pt closing rule at 652.7 pt, spanning 47.9 to 559.9 pt with no vertical "
      "stroke between the four blocks. Eighteen printed rows over eight columns: a spanner row at "
      "418.9 pt reading Central, Connect, Spread, IM over a rank row at 431.7 pt reading 'Rank "
      "No.' four times, then sixteen rows, one per paper, 444.3 to 640.3 pt. 512.0 pt against the "
      "506.7 pt measure, 101.0 per cent. Every column is an integer - a rank 1 to 16 and a paper "
      "number 1 to 16 - so numeric_cols is 8, text_cols 0, and both are centred on one width, "
      "which is not decimal alignment. The spanner row is what makes this the paper's key exhibit: "
      "the four columns are the four rankings and the last is the composite IM the model is built "
      "to produce.",
      numeric=8, header_rows=2, width="full",
      cap="TABLE 9. Articles’ rank based on central, connect and spread",
      mention=cited(15, 15, ["TABLE 9"], 2,
                    "In TABLE 9, we list the rank of the sixteen papers according to their "
                    "centralizing, connecting, spreading and comprehensive contributions to the "
                    "whole network.",
                    trail="the circle 11, with the largest size, has a low rank (8) in the last "
                          "column of TABLE 9"))

# ---------------------------------------------------------------- p16, the two companion drawings
figure(16, 1, "node-link-network",
       "Figure 5. A detail of citation network", "Figure N.",
       cited(16, 16, ["FIGURE 5"], 1,
             "If we further observe FIGURE 5, we could find from the detailed drawing"),
       [MEASUREMENT], "other", numbers=True, labels=True, legend="none",
       note="The right half of the pair printed under two captions on one line, and the same "
            "citation network as Figure 3 redrawn at detail: sixteen numbered discs - 1 to 16 set "
            "in black inside each circle - coloured red, yellow, green, purple and blue, with thin "
            "blue citation arrows between them and one large red disc for paper 11 and a purple one "
            "for 12. A hand-drawn circle marks the 11-12 pair and two straight leader lines run to "
            "the right, where a second, larger view draws paper 11 and 12 alone with the arrows "
            "between them. Numbers are the only labels, so data_labels is false here and "
            "printed_numbers true - the inverse of Figure 3, which labels by title and prints no "
            "number. The caption prints 1.9 pt under the art. Cited once by number, on p16.")

figure(16, 2, "line",
       "Figure 4. Influence analysis result of 16 papers", "Figure N.",
       cited(16, 16, ["FIGURE 4"], 1,
             "we use FIGURE 4, which demonstrates the normalized result of the characteristics of "
             "the sixteen papers, to show the superficial paradox"),
       [MEASUREMENT], "other", numbers=False, labels=False, legend="outside-right",
       note="The left half of the pair: four polylines over sixteen categorical x positions "
            "labelled P1 to P16, y 'Normalized Value' 0 to 1.25 with gridlines at 0.25, markers at "
            "every point, and a legend at the right keyed Final (blue circle), centralizing (black "
            "triangle), connecting (green square) and spreading (red cross). The series cross "
            "repeatedly and the two papers the prose cares about are visible as extremes: P11 near "
            "the top on spreading and the bottom on connecting, P12 the reverse, which is exactly "
            "the argument the paragraph makes. One figure, four series, so family line and not "
            "composite-panel; no y axis title beyond the one word, no values printed on the "
            "markers. Caption under the art at 303.9 pt, printed on the same line as Figure 5's.")

# ---------------------------------------------------------------- p17, the department layout
figure(17, 1, "node-link-network",
       "Figure 6 The department network", "Figure N.",
       none_mention(),
       [UTILITIES], "other", numbers=False, labels=False, legend="none",
       note="Four grey ellipses - three of them filled light grey and labelled College 1, College "
            "2 and College 3 inside the ellipse - holding about fifteen small colour-coded dots, "
            "roughly ten in the first and a handful in each of the others, joined by thin grey "
            "straight edges within a college and by a few long edges between colleges. Pasted as a "
            "low-resolution bitmap: the dot fills are pixel-sharp and the ellipse greys are "
            "dithered, so the whole drawing is a raster and the geometry pass sees one image block "
            "with no vector rules. No node is labelled, no edge carries a weight, no axis and no "
            "key: the only text inside the art is the three college names. The caption prints 1.5 "
            "pt under the frame and the prose that follows never names it, so the mention count is "
            "zero - the figure is placed between the sentence that introduces it and the paragraph "
            "that explains it.")

# ---------------------------------------------------------------- p17/p18, the Douban ranking
table(17, 2, 8, 8, [DOUBAN], "result",
      "We implement our algorithm on this set, and get TABLE 10.",
      "The head of the last grid in the paper, same register as Table 9: a 1.44 pt rule at 605.3 "
      "pt above the spanner row, no rule under the header band, and the page-foot rule at 710.0 "
      "pt, spanning 47.9 to 559.9 pt, no vertical stroke. Eight printed rows over eight columns - "
      "spanner row at 607.7 pt (Central, Connect, Spread, IM), rank row at 620.3 pt ('Rank No.' "
      "four times), then six rows at 633.1 to 697.6 pt. 512.0 pt, 101.0 per cent of the measure. "
      "All eight columns are integers, centred, so numeric_cols 8 and decimal_aligned false. The "
      "grid ranks USER IDS, not the users themselves: the No. column prints numbers such as 856, "
      "713, 620, 967, which are vertex indices in the 971-user network the prose describes, so "
      "the ranking cannot be read off the page without that table's key - and the paper prints no "
      "key. The caption prints 14.7 pt above the top rule with a DOUBLE space after TABLE.",
      numeric=8, header_rows=2, width="full",
      cap="TABLE 10. Top10 of the user of Douban based on central, connecting, spreading and final "
           "characteristics")

table(18, 1, 4, 8, [DOUBAN], "result",
      "",
      "The tail of Table 10 on the far side of the page turn: rows 7 to 10 at 74.5 to 113.1 pt, "
      "four 1.44 pt rules framing them at 72.0 and 125.4 pt, no header repeated and no vertical "
      "stroke. Eight columns of integers, same block layout as p17. Together with the p17 part "
      "this is one printed grid of twelve rows over eight columns - two header rows and ten ranked "
      "users - measured as two regions and booked as two rows with continued true. The prose "
      "directly below reads the disagreement between this composite rank and the first two "
      "single-measure ranks.",
      numeric=8, width="full", continued=True)

# ---------------------------------------------------------------- p18, the distribution
figure(18, 2, "line",
       "Figure 8. Impact Measurement distribution of 971 Douban users", "Figure N.",
       none_mention(),
       [DOUBAN], "result", numbers=True, labels=False,
       note="One open-circle polyline, not a bar chart: twenty points at 0.05 intervals from 0 to "
            "1 on the x axis labelled IM, joined by a thin line, y 'Count' 0 to 120, full "
            "rectangular frame, no gridlines. The prose calls it 'the distribution of 971 Douban "
            "users' and says it is built by 'set 0.05 as step length and calculate the number of "
            "the user in this interval' - a binned count - but the ink is a connected series of "
            "markers in a MATLAB axes, so by the family-follows-the-ink rule it is recorded line "
            "and not histogram; the gap between what the method produces and what was drawn is "
            "the finding. The mode sits at 0.75 with 117 users and a second lobe at 0.65 with 107, "
            "a long thin left half and a drop to 8 users in the last bin. Vector: 122 drawing "
            "paths including the frame, one vertical at x 199.3 pt and the frame rules at 183.6 and "
            "359.9 pt. Caption below at 388.9 pt; the prose never names the figure, so the mention "
            "count is zero.",
       )

# ---------------------------------------------------------------- page furniture
EXCLUDED.append({
    "page": 1,
    "bbox": REG[(1, 1)],
    "kind": KIND[(1, 1)],
    "reason": "not-an-exhibit",
    "note": "the official MCM Summary Sheet control form: the 'For office use only' box with its "
            "T1-T4 and F1-F4 fill-in rules, the team control number 31262, 'Problem Chosen C', the "
            "title, the typed abstract and the keyword line. 194 drawing paths, all of them form "
            "rules and hairlines. No chart, no diagram, no plotted ink",
})

EXCLUDED.append({
    "page": 20,
    "bbox": REG[(20, 1)],
    "kind": KIND[(20, 1)],
    "reason": "not-an-exhibit",
    "note": "the reference list, 72.0 to 556.9 pt by 484.9 to 670.3 pt: thirteen vector paths that "
            "are the hanging indents and leader rules of the bibliography, not a frame. No caption, "
            "no number, no grid",
})


# ---------------------------------------------------------------- payload
RULES = [
    "rows counts every printed row the region carries, header bands included, and a grid split "
    "over a page turn is two rows with continued true: Table 7 prints two header rows and five "
    "ranks on p13 and five more on p14, so p13 r3 records 7 and p14 r1 records 5 [table.rows]",
    "a region that holds more than one printed grid is booked once, as the grid it contains "
    "wholly, and the neighbours are declared gaps: the p12 box spans Table 2's top rule to Table "
    "4's header rule with Table 3 whole inside it, so the row is Table 3 [table.cols]",
    "rule_style is vertical-rules when any vertical stroke prints, booktabs when nothing but "
    "horizontals prints: Tables 1, 6 and 8 carry verticals and the other seven grids carry none "
    "[table.rule_style]",
    "a grid wider than 75 per cent of the local measure is full: eight of the ten grids run 101.0 "
    "to 101.8 per cent of the 506.7 pt measure because they overhang both margins, and Tables 1 "
    "and 6 at 50.2 and 60.8 per cent are the two recorded half [table.width]",
    "header_rows counts printed header bands, and a spanner row over a rank row is two bands: "
    "Tables 7, 9 and 10 print 'Central Connect Spread' over 'Rank Name', so each records 2 "
    "[table.header_rows]",
    "a table whose cells are all integers has numeric_cols equal to cols and text_cols zero, and "
    "a column of equal-width integers is not decimal alignment: Tables 9 and 10 record 8 and 0 "
    "with decimal_aligned false [table.numeric_cols]",
    "a two-block grid prints its headers and ranks twice and cols counts the physical columns: "
    "Table 8 is two side-by-side (Number, Article Name) pairs, so cols is 4 and numeric_cols 2 "
    "[table.cols]",
    "a note_sentence must be a printed sentence on the grid's own page or the next one, and a "
    "continuation half leaves it empty: p14 r1 and p18 r1 carry no heading of their own, so both "
    "record an empty note_sentence and continued true [table.note_sentence]",
    "two panels of one printed figure are two rows when the drawing pass measures two boxes and "
    "the panels are different families: Figure 1's bar panel and its degree histogram are booked "
    "separately as bar and histogram [geometry.family]",
    "a radar has no family in the closed vocabulary, so it is recorded other with an other_note "
    "naming the ink rather than forced into line or bar [geometry.family]",
    "the family follows the ink and not the method: Figure 8 counts users per 0.05 IM bin and is "
    "described as a distribution, but it is drawn as a connected marker series in MATLAB axes, so "
    "it is line and not histogram [geometry.family]",
    "a magnified inset inside one drawing is a fragment of that drawing and not a second panel: "
    "Figure 2's two nested inset rasters and its leader-line paths are excluded, so panel_count "
    "stays 1 [geometry.panel_count]",
    "a caption line in the text layer is not a citation: Figure 6 and Figure 8 print their "
    "numbers in their own captions and the prose never names them, so both record count 0 with "
    "first_page null [mention.count]",
    "a citation that lands a page before the art records lead_pages 1 and one on the art's own "
    "page records 0: Figure 3 is named on p14 and prints on p15, Table 1 is named on p10 [mention.lead_pages]",
]

NOTE = (
    "Twenty-five measured regions over ten of twenty pages: eight figure rows, eleven table "
    "rows, five exclusions, nothing unmeasured. The paper prints eight figures and ten tables, "
    "and two of those ten tables own no box of their own - declared gaps, not invented bboxes.\n\n"
    "The gaps are a chaining defect, not a width defect. Every grid on this paper is wide - the "
    "narrowest runs 50.2 per cent of the measure and the rest overhang it - so the half-page seed "
    "that cost papers 67 and 68 their grids never fires here. What fires instead is "
    "`rule_table_regions`'s grouping rule: it closes a table only after a 120 pt gap, and the gap "
    "between one grid's closing rule and the next grid's opening rule on this paper is 18 to 34 "
    "pt. So p12's region spans 446.1 to 713.5 pt - Table 2's top rule at 446.1, its header rule "
    "at 460.1 and its closing rule at 536.7, Table 3 whole at 570.3, 585.1 and 665.0, and Table "
    "4's caption at 683.7 with its two header rules at 698.6 and 712.8 - and p13's region spans "
    "72.0 to 275.1 pt, which is Table 4's six data rows at 73.9 to 137.6 closed at 149.3 and then "
    "Table 5's caption at 168.0 and its three rules at 182.9, 197.1 and 273.6. Each box is "
    "recorded once, as the grid it contains whole - Table 3 and Table 5 - and Tables 2 and 4 are "
    "declared here. Table 2 is the top thirty authors by closeness centrality, a booktabs grid of "
    "seven rows over ten columns; Table 4 is the same grid by degree centrality, its caption and "
    "header band at the foot of the p12 box and its six rows at the head of the p13 box.\n\n"
    "One ruling register, three dialects. Seven of the ten grids are three horizontal rules over "
    "one or two header bands with no vertical stroke anywhere, and the top and closing rules are "
    "cut at 1.44 pt against 0.72 pt for the rule under the header - Tables 3, 5, 7, 8, 9 and 10. "
    "Table 8 adds one vertical per block, at x 95.4 pt, to separate Number from Article Name. "
    "Table 1 and Table 6 are the two grids ruled the other way: a vertical stroke the height of "
    "the table, no side borders, and, in Table 6, two of the four horizontal rules stopping at "
    "that vertical - 486.9 and 516.5 pt span only 237.3 to 460.1 pt - so the Variable column has "
    "no rule below its header and no closing rule at all. Every wide grid overhangs the text "
    "measure: 47.9 to 563.5 pt against the 54.0 to 560.7 pt measure, which is 101.8 per cent, and "
    "the two narrow ones are 50.2 and 60.8 per cent.\n\n"
    "Table 8 breaks over the page turn and is left open at the bottom. Its three thin rules sit "
    "at 648.6, 662.9 and 678.0 pt, rows 9 to 11 on the right, and the grid resumes on p15 at "
    "72.0, 101.4 and 141.3 pt with rows 4 to 8 and 12 to 16. No header is repeated on the far "
    "page and no closing rule is drawn at either end: the last rule of the whole grid is the 141.3 "
    "pt rule and Figure 3's frame begins 16 pt under it. A reader cannot tell from the page where "
    "the grid ends, and nothing in the prose says the table continues.\n\n"
    "The figures sort into three drawing technologies and one family that has no name. Figures 2, "
    "3, 4, 5 and 6 are all pasted raster screenshots - Gephi for the co-author network, MATLAB for "
    "the series plot, and the same graph tool twice for the citation network - and only Figures 1 "
    "and 8 are vector MATLAB axes. Figure 7 is a three-spoke radar, the paper's one exhibit with "
    "no family in the closed vocabulary, so it is recorded other with the ink named in its "
    "other_note, exactly as paper 60 filed its radar pentagon. Figure 1 prints as one caption over "
    "two separately framed panels and is booked as two rows, bar and histogram, because each box "
    "holds its own chart. Figure 8 is the inverse trap of Figure 1: the prose calls it the "
    "distribution of 971 users and says the method bins at 0.05, but the ink is a connected "
    "open-circle series in a MATLAB axes, so the family is line. Figure 2 carries a magnified "
    "inset of its own centre in two nested rasters, with two leader lines drawn as vector paths; "
    "the inset is a detail of the same drawing, so the row keeps panel_count 1 and the three other "
    "regions are excluded as fragment, fragment and duplicate.\n\n"
    "Two mentions are zero and one number is missing from the page. Figure 6 and Figure 8 print "
    "their numbers only in their own captions; the prose introduces Figure 6 with 'The "
    "vertices(departments) are separated into several communities(colleges)' and Figure 8 with "
    "'we plot the distribution of 971 Douban users as follow:' and never cites either by number. "
    "Table 10 ranks users by a No. column that prints vertex ids - 856, 713, 620, 736, 163, 967, "
    "107, 352, 306, 654 - and the paper prints no key from id to user, so its 'Top10 of the user "
    "of Douban' cannot be read off the page. Table 8's two blocks leave the sixteen paper numbers "
    "in the same position: the grid indexes them, and every later exhibit refers to them by index "
    "only.\n\n"
    "Printed defects, recorded not corrected. Table 6's caption reads 'Variable and their "
    "meaning'. Figure 1's x axis reads 'Coponent ID' and its two in-art titles are broken into "
    "words by the axis labels the layer interleaves ('Statistic of ComponentStatistic of Degree'). "
    "Table 10's caption prints 'TABLE  10.' with a double space, and the same double space sits "
    "after 'TABLE 1.' The heading detector is unusable on this paper for the same reason it was on "
    "paper 68: it reads every rank column of the ten-column grids as a heading number, which is "
    "why the context dump carries '4 GAAL,S 10 DARLING, D 16 KHARE, SP' and '6 FUREDI,Z 12 "
    "CHUNG,FRK 18 NESETRIL,J' as sections of the paper, and why the paper's real headings are the "
    "only section labels recorded here. Page 8 carries nineteen horizontal rules of zero "
    "thickness, no verticals, two non-rule paths and no region at all: they are the fraction bars "
    "of equations 17 to 22, typeset maths and not an exhibit. "
    "Page 1 is the contest's own control sheet and page 20's region is the bibliography; both are "
    "excluded as not-an-exhibit, and the bibliography's thirteen paths are its hanging indents."
)

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc69-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
