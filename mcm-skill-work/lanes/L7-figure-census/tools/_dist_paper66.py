"""Hand census of P-C-2014-28199-d39873d7 (C-28199-Outstanding, 21 pages).

Fourteen measured regions over eleven pages. Twelve carry a printed caption - seven figures
and five tables - and two do not:

  p1  r1  Figure 1   Model Design Process        flowchart-or-schematic
  p4  r1  Figure 2   co-author network, degree-sized nodes
  p4  r2  Figure 3   degree distribution, two series
  p5  r1  Table 1    empirical results, booktabs, no verticals
  p6  r1  Table 2    properties of network, closed grid, diagonal header cell
  p8  r1  Table 3    top 10 co-authors, closed grid, CONTINUES onto p9
  p9  r1  (the rest of Table 3, ranks 5 to 10, no repeated header)  EXCLUDED
  p10 r1  Figure 4   Movie Star Network, 20 labels / 18 discs
  p10 r2  Table 4    top 5 movie stars, closed grid
  p14 r1  Figure 5   extensive citation network with the virtual N+1 node
  p14 r2  (the partitioned (N+1)x(N+1) adjacency matrix)            EXCLUDED
  p16 r1  Table 5    Pagerank results, three header bands
  p18 r1  Figure 6   Shapley value versus parameter k
  p19 r1  Figure 7   Pagerank value versus parameter d

The heading pass on this paper is polluted a third time in the lane: p8, p9 and p10 return
sixteen printed table rows ('2 GYARFAS, ANDRAS SOS, VERA TURAN', '5 POMERANCE, CARL', '1 Matt
Damon Matt Damon', ...) as headings because the table cells are set in a display face. The real
headings are unnumbered and set at 20 pt (sections) and 15 pt (subsections); every path below is
the printed label of the heading that governs the region, read off the size-and-font dump, not
off the nearest detector record.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2014-28199-d39873d7"
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

ERDOS = "未编号标题 Erdos Network"
INTRO = "未编号标题 Introduction"
UNDIRECTED = "未编号标题 Influence Measure for undirected network:"
DIRECTED = "未编号标题 Influence measure for directed network:"
PAGERANK = "未编号标题 Optimized Pagerank"
SENSITIVITY = "未编号标题 Sensitivity analysis"

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
          pattern: str = "as-shown-in", read: int = 1, gap: int | None = None,
          trail: str = "") -> dict:
    """A by-number citation the text layer prints; check_mention re-quotes the sentence."""
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": schema.norm(lead),
            "trail_sentence": schema.norm(trail), "lead_pattern": pattern,
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
           three_d: str = "no", source: str = "text-layer", numbered: bool = False,
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
          note_sentence: str, note: str, *, rule: str = "vertical-rules", numeric: int = 1,
          header_rows: int = 1, numbered: bool = False, width: str = "half",
          zebra: bool = False, merged: bool = False, decimal: bool = False,
          diagonal: bool = False, continued: bool = False, cap: str = "",
          position: str = "above", mention: dict | None = None) -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": q(cap, page) if cap else "",
        "caption_source": "text-layer" if cap else "none",
        "note": note,
        "place": place(page, reg, path, kind, numbered),
        "mention": mention or none_mention(),
        "caption": caption(q(cap, page) if cap else "", "Table N." if cap else "none", position),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued, "note_sentence": schema.norm(note_sentence)},
    })


# ---------------------------------------------------------------- p1 to p6, the summary and Erdos
figure(1, 1, "flowchart-or-schematic",
       "Figure 1. Model Design Process",
       "Figure N.", none_mention(),
       ["未编号标题 Model Design"], "model", labels=True, numbers=False,
       note="vector, one left-to-right chain on the MCM summary sheet: six rounded rectangles, "
            "'Conventional Measures' fanning out to 'Cohesion Measure' and 'Shapley Approach', "
            "both converging on 'Shapley Value', then across a vertical dashed divider to 'Basic "
            "Pagerank' and 'Optimized Pagerank'. Every arrowhead points right, so the flow is one "
            "pass with a 1-to-2 fan-out and a 2-to-1 fan-in and not a serpentine row. The group "
            "labels '(undirected)' under the left half and '(directed)' under the right half sit "
            "in the divider, and they name the argument the whole paper makes: the Shapley half "
            "handles undirected graphs, the Pagerank half directed ones. No frame, no axis, no "
            "legend, no panel letters. The paper never cites it by number - the summary sheet "
            "prints the drawing and moves straight into 'Results', so the only prose anywhere "
            "near it is the abstract paragraph above.")

figure(4, 1, "node-link-network",
       "Figure 2. Node size corresponds to the degree of each author, a simple measure of influence.",
       "Figure N.",
       cited(3, 4, ["Figure 2"], 1,
             "Given the adjacent matrix, we can visualize the network with PAJEK, which is "
             "represented in Figure 2.", pattern="direct"),
       [ERDOS, "未编号标题 Network Visualization"], "model", numbers=True,
       note="raster, one embedded bitmap 440.25 by 221.25 pt, a force-directed author graph: a "
            "compact core of large discs ringed by small leaves, curved and dashed grey edges, no "
            "arrowheads, no frame, no axis, no legend and no size key. Every node carries a small "
            "NUMERIC id - 257, 429, 400, 444, 184, 436, 211, 25, 76 - and the caption says 'Numbers "
            "beside the nodes represent the corresponding author', but the paper prints no key "
            "that turns a number into a surname, so not one node can be named from the art. Node "
            "diameters run from about 4 to about 18 px, a core-to-leaf ratio near 4:1, consistent "
            "with degree-proportional sizing. The bitmap runs from 90.0 to 530.25 pt and so "
            "overhangs the 506.9 pt right text edge by 23.4 pt. Cited once by number, on p3, one "
            "page before the art.")

figure(4, 2, "line",
       "Figure 3. Degree Distribution of Erdos Network & Random Network with Same Number of Nodes",
       "Figure N.",
       cited(4, 4, ["Figure 3"], 2,
             "To demonstrate better the feature of the degree distribution of this network, we "
             "plot the degree frequencies in Figure 3.",
             trail="while the degrees of Erdos network follow the power-law distribution, showing "
                   "a feature of scale-free networks.",
             pattern="direct"),
       [ERDOS, "未编号标题 Properties of Network"], "model",
       legend="inside", numbers=True,
       note="vector, one axes, two marker-plus-line series in the Office default palette: cyan "
            "upward triangles joined by a light blue line for 'Erdos Network' and red squares "
            "joined by a red line for 'Random Network', legend inside the plot at the upper "
            "right, full rectangular border, no gridlines. x axis 'Degree' with ticks 0 to 51, y "
            "axis printed as a rho followed by '-Frequency' with ticks 0 to 90; both linear. The "
            "Erdos series spikes to about 84 at degree 2, drops to 46 at degree 3 and decays to "
            "the axis by about degree 16; the random series climbs from 0 at degree 0 to a "
            "plateau of 76 at degree 5 and 75 at degree 6, then falls to the axis by about degree "
            "18. Two defects stand as printed: a LINEAR frequency axis is used to read off a "
            "power-law claim, and the degree axis stops at 51 while the same section counts 511 "
            "nodes, so the long tail is cut off and only the scattered points at degrees 18 to 51 "
            "are left of it. Cited twice by number, once on this page and once on p5 as 'As is "
            "shown in Figure 3'.")

table(5, 1, 2, 4, [ERDOS, "未编号标题 Properties of Network"], "model",
      "we use PAJEK to generate a random network with same number of nodes, which is compared "
      "with Erdos network in Table 1.",
      "Booktabs, and the only grid in the paper with no vertical rule: three rules spanning the "
      "full 341.8 pt, a hairline top rule at 553.4 pt, a HEAVY 1 pt midrule at 580.3 pt under "
      "the header and a hairline bottom rule at 601.0 pt, so two printed rows and a single data "
      "row. 341.8 pt against the 418.3 pt text measure (81.7 %), inset from both margins, with "
      "the caption left-aligned to the grid's own left edge at 127 pt rather than to the body "
      "margin. The header prints L and CC in italic with roman 'actual' and 'random' subscripts, "
      "so the four columns are L actual, L random, CC actual and CC random; the single data row "
      "reads 3.82, 3.64, 0.3428 and 0.0153. Every column holds one value, so decimal alignment is "
      "not assessable and is recorded false; values are centred in their columns. The caption "
      "says 'results of networks' plural while the grid prints one row, and the prose below it "
      "reads the small-world claim off these four numbers as 'L L but CC CC' with the actual and "
      "random subscripts flattened into the sentence",
      cap="Table 1. Empirical results of networks", numeric=4, width="full",
      mention=cited(5, 5, ["Table 1"], 1,
                    "we use PAJEK to generate a random network with same number of nodes, which "
                    "is compared with Erdos network in Table 1.", pattern="direct"))

table(6, 1, 4, 4, [ERDOS, "未编号标题 Properties of Network"], "model",
      "",
      "Closed grid on five horizontal rules at 244.5, 307.7, 371.0, 403.5 and 445.8 pt and five "
      "full-height verticals at 84.4, 166.9, 278.7, 386.0 and 502.3 pt, so four rows and four "
      "columns: Networks, Clustering Coefficient, Average Path Length, Degree Distribution. The "
      "top-left cell is a DIAGONAL header cell - 'Properties' over the diagonal, 'Networks' under "
      "it - the only one in the paper and the reason the detector returns 'Properties Clustering "
      "Average Path Degree' and 'Networks' as separate lines. 419.0 pt against the 418.3 pt "
      "measure (100.2 %), the widest object in the paper and the only one that overhangs the "
      "right margin. Header band 63.2 pt against 32.6 pt per body row because the header wraps to "
      "three lines. All four columns are text: Regular, Random and Scale Free against High, Low, "
      "Variable and 'Equal and fixed In/Out degrees to each node', Exponential and 'Power-law "
      "distribution'. No numeric column and no decimal alignment is possible. The prose calls the "
      "diagonal elements the small-world Erdos network, but Erdos is not a row of this grid at all "
      "- the three rows are the textbook prototypes Regular, Random and Scale Free",
      cap="Table 2. Properties of network: diagonal elements characterize small-world network",
      numeric=0, width="full", diagonal=True)

# ---------------------------------------------------------------- p8 to p10, the two applications
table(8, 1, 11, 3, [ERDOS, "未编号标题 Application in Edros Network"], "result",
      "We find the Top 10 influential co-authors, and compare the results with that ranked by "
      "betweenness, as is shown in Table 3.",
      "Closed grid, 383.0 pt against the 418.3 pt measure (91.6 %), four full-height verticals at "
      "106.5, 148.5, 318.0 and 488.5 pt and six horizontal rules, which is THREE columns and five "
      "printed rows on this page: one header reading 'Rank Name(Shapley value) Name(Betweenness)' "
      "over ranks 1 to 4. The Shapley and betweenness values are printed in parentheses on a "
      "second line INSIDE each name cell, which is why each data row is 38.9 pt tall against the "
      "19.7 pt header - the 4-boundary reading of the drawn grid makes this look like four "
      "columns and it is not. The table does not finish here: it continues on p9 with ranks 5 to "
      "10 under the same four verticals, no repeated header band, and a closing rule at 343.4 pt. "
      "Eleven printed rows in all, counted once, so continued is true and the p9 fragment is "
      "excluded as split-across-pages rather than booked as a second grid. Column 1 is the only "
      "numeric column, ranks 1 to 10; the two name columns are text with a centred parenthesised "
      "number under each, so the values are neither decimal- nor left-aligned: '(-0.0013609)' is "
      "indented further right than '(-0.001494127)'",
      cap="Table 3. Top 10 influential co-authors ranked by Shapley value and Betweenness",
      numeric=1, width="full", continued=True,
      mention=cited(8, 8, ["Table 3"], 2,
                    "We find the Top 10 influential co-authors, and compare the results with that "
                    "ranked by betweenness, as is shown in Table 3.",
                    trail="We can see from Table 3 that ALON, NOGA M. makes the most contribution "
                          "to the Edros Network’s cohesion"))

figure(10, 1, "node-link-network",
       "Figure 4. the Movie Star Network (The width of the edges reflects the times the two stars "
       "have cooperated, and the size of the nodes reflects their degrees)",
       "Figure N.", none_mention(),
       ["未编号标题 Application in Movie Star Network"], "result", labels=True,
       note="raster, one bitmap 404.25 by 203.25 pt, a force-directed star graph with undirected "
            "edges whose stroke widths vary by an order of magnitude - the heavy black spokes run "
            "from Matt Damon to Alec Baldwin, Tom Hanks and Gwyneth Paltrow while the rest are "
            "hairlines. No arrowheads, no axis, no frame, no legend, no size key. The prose on p9 "
            "says the network is the 20 movie stars who have all cooperated with Jude Law; the "
            "drawing prints twenty name labels but only eighteen discs, two of them - 'Ethan "
            "Haw', cut mid-word at the 499.4 pt right edge of the bitmap, and 'Clive Owen' - carry "
            "no disc at all, and the label 'Jude Law' does not appear anywhere in the art. Node "
            "sizes vary from 9 to about 22 px, consistent with the caption's degree claim. Never "
            "cited by number: the p9 prose describes the network but points at nothing")

table(10, 2, 6, 3, ["未编号标题 Application in Movie Star Network"], "result",
      "",
      "Closed grid, 360.92 pt against the 418.3 pt measure (86.3 %), four full-height verticals "
      "at 117.3, 158.7, 328.7 and 477.7 pt and seven horizontal rules, so three columns and six "
      "printed rows: one header 'Rank Name(Shapley) Name(Betweenness)' over ranks 1 to 5. Same "
      "construction as Table 3 - the parenthesised values sit on a second line inside each name "
      "cell and each data row is 38.9 pt tall - but the header here abbreviates to 'Name(Shapley)' "
      "where Table 3 prints 'Name(Shapley value)'. Column 1 is the only numeric column; the two "
      "name columns are text, values centred and not decimal-aligned, the Shapley column mixing "
      "eight and nine decimal places. Rank 5 is the interesting row: Gwyneth Paltrow heads the "
      "Shapley column and Kate Winslet heads the betweenness column, so the two name columns are "
      "two independent rankings printed side by side and not one ranking with two scores. The "
      "prose below the grid reads the difference and says removing Paltrow hurts cohesion more "
      "than removing Winslet, although the latter bridges more pairs",
      cap="Table 4. Top 5 influential movie stars ranked by Shapley value and Betweenness",
      numeric=1, width="full")

# ---------------------------------------------------------------- p14 to p19, the directed half
figure(14, 1, "node-link-network",
       "Figure 5. Extensive citation network. The size of a node corresponds to the all degree "
       "(in and out) of a paper. Arrows mean one paper cites another. Imaginary line separates "
       "the initial citation network and the outside virtual node.",
       "Figure N.",
       cited(13, 14, ["Figure 5"], 1,
             "we assume that there is a virtual N+1 node, which presents all of the other papers "
             "beyond the 16 papers (see Figure 5).", pattern="parenthetical"),
       [DIRECTED, PAGERANK], "model", numbers=True,
       note="vector, directed citation graph: sixteen blue discs labelled '1' to '16' and joined "
            "by thin black arrows with visible heads, the discs enclosed in a hand-drawn red "
            "dashed contour labelled 'Paper citation network' inside the art at the lower left. "
            "Node 11 is the largest disc by a factor of about three over the leaves, which is the "
            "caption's degree claim. The virtual node is drawn outside that contour at the upper "
            "right as a large red-outlined circle lettered 'Virtual node', joined back to the "
            "'2'/'11' cluster by two leader lines and carrying no number, so the seventeenth node "
            "of the (N+1) adjacency matrix below it is not one of the sixteen. No frame, no axis, "
            "no legend. Cited once by number, on p13, one page before the art")

table(16, 1, 8, 4, [DIRECTED, PAGERANK, "未编号标题 Results"], "result",
      "",
      "Closed grid, 338.6 pt against the 418.3 pt measure (81.0 %), five full-height verticals at "
      "128.2, 164.7, 285.5, 372.2 and 466.8 pt and nine horizontal rules, so four columns and "
      "eight printed rows. THREE header bands, and the only merged header in the paper: band 1 is "
      "'Rank', band 2 splits into 'Basic Pagerank Model' over one column and 'Optimized Pagerank "
      "Model' spanning two, band 3 reads 'No Times Cited' and 'With Times Cited' over the "
      "optimized pair; 'Rank' runs down all three bands and 'Optimized Pagerank Model' spans two "
      "columns sideways. Each data cell prints a bold paper number with its Pagerank in "
      "parentheses under it, which is why a data row is 38.9 pt against a 19.7 pt header band. "
      "Ranks run 1 to 5 only of the sixteen papers the section counts, and the columns disagree "
      "from rank 2 on - paper 3 under the basic model, paper 4 under both optimized models - "
      "which is the whole point of the comparison. Not decimal-aligned: the parenthesised values "
      "are centred and the precision runs from four to nine places, one cell printing (0.295) "
      "against (0.2871) beside it",
      cap="Table 5. Pagerank results of three methods in the Pagerank model",
      numeric=4, width="full", header_rows=3, merged=True,
      mention=cited(13, 16, ["Table 5"], 4,
                    "The importance ranking results can be seen in Table 5, where the value under "
                    "the paper number is its Pagerank value."))

figure(18, 1, "line",
       "Figure 6. Sensitivity analysis results of Shapley value to parameter k.",
       "Figure N.",
       cited(18, 18, ["Figure 6"], 1,
             "tracing 5 co-authors’ rank under different k, as is shown in Figure 6.",
             pattern="as-shown-in"),
       [SENSITIVITY, "未编号标题 Shapley value’s sensitivity to parameter k"], "sensitivity",
       legend="below", numbers=True,
       note="vector, one axes at 409.35 by 247.98 pt (97.9 % of the measure), five plain "
            "polylines with no markers, full rectangular border, no interior gridlines, legend "
            "OUTSIDE the axes below the plot in two columns. x axis 'parameter k' from 100 to "
            "500, y axis 'Rank' from 0 to 70, both linear, and the y axis counts DOWN - a better "
            "rank is a smaller number plotted lower, which no axis label says. Five series: "
            "ALON, NOGA M.; GYARFAS, ANDRAS; SOS, VERA TURAN; KLEITMAN, DANIEL J.; TUZA, ZSOLT - "
            "the top five of Table 3's Shapley column, so the figure does test what it claims. "
            "SOS, VERA TURAN spikes to about 62 near k=210 and about 57 near k=385, KLEITMAN to "
            "about 52 near k=330; the other three stay under 40. Cited once by number")

_P19 = schema.page_text(PID, 19)
_A = _P19.find("Figure 7. Sensitivity analysis results of Pagerank values")
FIG7_CAP = _P19[_A:_P19.find(" The 5 different lines", _A)]

figure(19, 1, "line",
       FIG7_CAP,
       "Figure N.",
       cited(19, 19, ["Figure 7"], 1,
             "The outcome of sensitivity analysis can be seen in Figure 7.", pattern="direct"),
       [SENSITIVITY, "未编号标题 Pagerank value’s sensitivity to parameter d"], "sensitivity",
       legend="outside-right", numbers=True,
       note="vector, one axes at 415.32 by 241.20 pt (99.3 % of the measure), five FLAT "
            "polylines with one marker glyph each - circle for No.14, triangle for No.4, diamond "
            "for No.2, square for No.11, cross for No.1 - full rectangular border, no gridlines, "
            "legend outside at the right. x axis 'Parameter d' with rotated tick labels 0.05 to 1 "
            "in steps of 0.05, y axis 'Rank' 0 to 6 and NOT inverted, so rank 1 sits at the "
            "bottom. Nothing moves: across twenty values of d every one of the five papers holds "
            "its rank, which is why the caption and the sentence above it only promise that the "
            "outcome 'can be seen'. The flatness is the finding and it is recorded here as one. "
            "The text layer also scrambles the five series labels out of the plot, printing "
            "'No.14 k n a No.4 R No.2 No.11 No.1' with the y-axis title 'Rank' broken into two "
            "letters around them. Cited once by number")

EXCLUDED.append({
    "page": 9,
    "bbox": REG[(9, 1)],
    "kind": KIND[(9, 1)],
    "reason": "split-across-pages",
    "note": "the rest of Table 3 - ranks 5 to 10 - printed at the top of p9 under the same four "
            "verticals at 106.5, 148.5, 318.0 and 488.5 pt as the p8 part, with no repeated header "
            "band, closed by its own bottom rule at 343.4 pt. It is counted once as Table 3's "
            "eleven printed rows, not booked as a second grid. The row carrying rank 9 runs to "
            "three lines (FAUDREE, RALPH JASPER, JR., then BOLLOBAS, BELA, then JR.) and so stands "
            "58.0 pt tall against 38.9 pt for its neighbours, which is why the rule spacing here "
            "looks irregular. The 2 pt rule at 66.2 pt across the full measure is the running-head "
            "rule, not the table's top border."
})

EXCLUDED.append({
    "page": 14,
    "bbox": REG[(14, 2)],
    "kind": KIND[(14, 2)],
    "reason": "not-an-exhibit",
    "note": "the partitioned (N+1)x(N+1) adjacency matrix the text calls 'a new modified "
            "adjacency matrix(N+1×N+1) of the extensive citation network'. Seven stacked 12 pt "
            "slices, which is why the geometry pass reports seven tiny images in one box; the one "
            "vertical rule at 368.0 pt and the one horizontal rule at 568.9 pt are its dashed "
            "partition lines separating the augmented last column and last row, not a grid of "
            "cells. Three coloured callout rectangles are drawn over the augmented column, the "
            "augmented row and the r(N+1)(N+1) corner but add no column structure. No caption, no "
            "number, no header row: a display equation, so it is typeset maths in the flow of "
            "Figure 5's caption and not an exhibit."
})

# ---------------------------------------------------------------- payload
RULES = [
    "rows counts every printed row including the header bands, and the count comes from the "
    "horizontal rules minus one rather than from the text layer's line order: Table 3's five "
    "rules on p8 and six on p9 are five and six rows, eleven in all once the continuation is "
    "folded in [table.rows]",
    "a drawn boundary count is not a column count: Table 3's four verticals over a header that "
    "prints three labels are three columns, because the Shapley and betweenness values sit on a "
    "second line inside each name cell and not in columns of their own [table.cols]",
    "a grid is vertical-rules when full-height verticals close every column, booktabs when it "
    "prints horizontal rules only: Table 1 is the paper's single booktabs grid on three rules "
    "with a heavy midrule, and the other four are closed [table.rule_style]",
    "a table that turns a page is one row with continued true and its far-page fragment is "
    "excluded split-across-pages, so Table 3 is eleven rows over two regions and not two grids "
    "[table.continued]",
    "a two-line header band is one header row: Table 1's L/CC with actual/random subscripts and "
    "Table 2's three-line header both take header_rows 1, while Table 5's three stacked bands "
    "take 3 [table.header_rows]",
    "merged header cells are recorded as merged: Table 5's 'Rank' runs down three bands and "
    "'Optimized Pagerank Model' spans two columns sideways [table.merged_cells]",
    "a diagonal stroke in the top-left cell makes it a diagonal header cell rather than two "
    "labels, so Table 2 keeps 4 columns and 4 rows with diagonal_header true [table.diagonal_header]",
    "centred parenthesised values are not decimal alignment: every scored column in this paper is "
    "centred and mixes precision from four to nine places, so decimal_aligned is false throughout "
    "[table.decimal_aligned]",
    "a grid over 75 per cent of the local measure is full: the five grids here run 81.0, 81.7, "
    "86.3, 91.6 and 100.2 per cent of the 418.3 pt measure and every one of them is full, with "
    "the percentage named in its note [table.width]",
    "a note_sentence must be a printed sentence on the grid's own page or the next one, so the "
    "three grids whose only prose sits a page or three earlier - Tables 2, 4 and 5 - carry the "
    "empty string and the pointer goes into the item note [table.note_sentence]",
    "captions for this paper print the number with a full stop and no gloss - 'Figure 1. Model "
    "Design Process' - so numbering is Figure N. and Table N. throughout [caption.numbering]",
    "every caption here prints below its figure and above its table without exception, and "
    "Figure 1's sits on the summary sheet between the drawing and the 'Results' heading "
    "[caption.position]",
    "a caption that names the wrong thing is recorded as printed: Figure 2's 'Numbers beside the "
    "nodes represent the corresponding author' names a key the paper never prints, and Table 2's "
    "diagonal claim names a network that is not a row of the grid [caption.verbatim]",
    "an exhibit the prose never numbers by name is still a row with count 0 and first_page null: "
    "Figures 1 and 4 and Table 4 print their captions but are never pointed at [mention.count]",
    "an exhibit cited more than once keeps its FIRST citing page: Table 5's first_page is 13 "
    "although its grid is on p16 and its four citations straddle six pages [mention.lead_pages]",
    "the heading detector reads sixteen printed table rows as headings on p8, p9 and p10, so "
    "every section_path here is the printed label of the heading that governs the region and all "
    "of them are marked section_numbered false [place.section_numbered]",
    "a display equation measured as a region is not an exhibit: p14's seven stacked slices under "
    "one vertical and one horizontal dashed rule are one partitioned matrix and are excluded "
    "not-an-exhibit [place.section_kind]",
]

NOTE = (
    "Fourteen measured regions over eleven of twenty-one pages, all accounted for: twelve rows - "
    "seven figures and five tables - plus two excluded regions, no refusals and no unmeasured "
    "exhibit. The paper numbers seven figures and five tables and all twelve own a region, so "
    "there is no ghost grid here either. Two of the regions are not exhibits at all: Table 3 "
    "runs off the foot of p8 and finishes at the head of p9 under the same four verticals with no "
    "repeated header, and p14's region is the partitioned (N+1)x(N+1) adjacency matrix the text "
    "calls a 'new modified adjacency matrix', seven stacked slices under one vertical and one "
    "horizontal dashed partition line - a display equation counted by the geometry pass as seven "
    "tiny images in one box.\n\n"
    "One ruling register, five times over, with one exception: Tables 2, 3, 4 and 5 are closed "
    "boxes with full-height verticals at every column boundary, and Table 1 is the paper's only "
    "booktabs grid - three rules, no vertical anywhere, a heavy midrule under a two-line header "
    "and a single data row. Table 2 is the widest object at 419.0 pt against a 418.3 pt measure "
    "and the only grid with a diagonal header cell; Table 5 is the only one with three header "
    "bands and merged cells. Every scored column in the paper is centred rather than "
    "decimal-aligned and Table 3's 'four columns' are three: the parenthesised Shapley and "
    "betweenness values ride on a second line inside each name cell.\n\n"
    "Defects recorded, not corrected: Figure 4's caption and the p9 prose promise twenty movie "
    "stars who all cooperated with Jude Law, while the drawing prints twenty labels for eighteen "
    "discs, cuts 'Ethan Haw' mid-word at the bitmap edge, leaves 'Clive Owen' without a disc and "
    "never prints 'Jude Law' at all; Figure 2's nodes are numbered and the caption says the "
    "numbers are the authors, but no key is printed anywhere in the paper; Figure 3 reads a "
    "power-law claim off a linear frequency axis whose degree scale stops at 51 while the same "
    "section counts 511 nodes; Table 2's caption calls the diagonal elements the small-world "
    "Erdos network although Erdos is not one of the grid's three rows; Table 1's caption says "
    "'results of networks' plural over a single data row; Table 3 splits without repeating its "
    "header; and Figure 7 is five dead-flat lines over twenty values of d, so the sensitivity "
    "study finds nothing to report. The typos stand as printed: 'Application in Edros Network', "
    "'Edros Network', 'unweithed network', 'weithed netwok', 'betweeness', 'free-scale network' "
    "for scale-free, and the sentence 'The two preceding measures are calculated as follows' "
    "introducing two formulas and one table."
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

out = PROXY / "pc66-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
