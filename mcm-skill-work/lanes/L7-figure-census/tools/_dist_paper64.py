"""Hand pass for P-C-2014-25318-eac62e81 (a 2014 C paper that scores Erdos1 co-authorship with degree,
betweenness and eigenvector centrality, then reads a 24-paper citation network through a revised
PageRank and plots each node on an authority-popularity plane), 21 PDF pages.

Fourteen measured regions over twelve pages, all accounted for: eleven figure rows, three tables, no
refusals.

    page    region   what it is
    5       r1       Figure 1, the Erdos1 co-author network, raster
    8       r1       Figure 2, 511 measure vectors in a 3-D scatter box, raster
    10      r1       Figure 3, degree distribution against the power law, raster
    12      r1       Figure 4, the directed citation network, raster
    13      r1       Table 4, weights for the 24 papers
    14      r1       Figure 5, flow chart of the iteration, raster
    14      r2       Table 5, PageRank ranks 1-24
    15      r1       Table 6, cited quantities per year
    15      r2       Figure 6, authority-popularity plane for the citation network
    16      r1       Figure 7, the co-star network with weights on the links
    17      r1       Figure 8, the two-panel diagram of the modified algorithm
    18      r1       Figure 9, authority-popularity plane for the co-star network
    19      r1       Figure 10, sensitivity to the damp coefficient
    21      r1       Figure 11, the shortcut diagram

Four numbered tables print with NO measured region - Table 1 (p3), Table 2 (p8), Table 3 (p9) and
Table 7 (p18). Each is a two-rule booktabs grid, and the two rules of each stand 314.1, 178.7, 178.5
and 180.4 pt apart, past the extractor's 120 pt grouping gap, so no cluster forms. The table-tail
fallback does not recover them either: it takes its lower bound from `max(b[3] for rules with
b[3] <= box[1])`, and a stroked rule comes back from get_drawings with zero height, so the closing
rule's own bottom equals its top and the search window collapses to nothing (fig_extract.py:493).
They are declared gaps, not invented boxes.

The paper sets captions by exhibit type and never mixes: every figure caption prints below its art,
every table caption above its grid. Two grids are two side-by-side blocks inside one ruled frame
(Tables 5 and 6 each print their header twice), so `cols` counts the physical grid.

Usage: python -I tools/_dist_paper64.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2014-25318-eac62e81"
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

# Every page of this paper is inside a numbered section except the reference list, which prints the
# unnumbered heading 'References' over the p21 art. The heading pass is otherwise clean here - 20
# records, all real headings - so each path below is the printed label of the heading that governs
# the region, and every label is present in the text layer.
METHOD = "4.2.2 Methodology"
RESULTS = "4.2.3 Results and Analysis"
ERDOS = "4.4 Properties of the Erdos1 network"
APMODEL = "5.2 Authority-Popularity Evaluation Model based on the revised"
COSTAR = "5.3 The Co-star Network for Requirement 4"
SENSITIVITY = "5.4 Sensitivity Analysis"
STRENGTHS = "5.5 Strengths and Weaknesses"
PHILOSOPHY = "6 The philosophy of the scale-free network"

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
          continued: bool = False, cap: str = "", position: str = "above",
          mention: dict | None = None) -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": q(cap, page) if cap else "",
        "caption_source": "text-layer" if cap else "none",
        "note": note,
        "place": place(page, reg, path, kind, numbered),
        "mention": mention or none_mention(),
        "caption": caption(q(cap, page) if cap else "", "Table N:" if cap else "none", position),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": False, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued, "note_sentence": schema.norm(note_sentence)},
    })


# ---------------------------------------------------------------- 4.2, the Erdos1 network
figure(5, 1, "node-link-network",
       "Figure 1: The co-author network of the Erdos1.",
       "Figure N:", cited(7, 5, ["Figure 1"], 1,
                          "to draw the network in UCINET, as is shown in Figure 1."),
       [METHOD], "model",
       note="raster, one embedded bitmap, undirected spring layout with no arrowheads, no axes and "
            "no frame. Nodes are circles whose diameter grows with degree - five large dark red "
            "discs carry white capitalised names inside them (PAUL ERDOS, ALON NOGA M., HARARY "
            "FRANK, FOLDES ZOLTAN, CHVATAL VASEK), mid-sized pink discs carry dark names, and the "
            "white periphery carries numeric IDs only. Edges are teal hairlines. The look is NetDraw "
            "or Pajek rather than MATLAB. Cited a page and a half AFTER it prints, from the 4.2.3 "
            "text, and by the phrase 'the top 50 Erdos1 authors' - the prose never says how many "
            "nodes the drawing holds. Small-node ID labels print near-white on white and are "
            "marginally legible")

figure(8, 1, "scatter",
       "Figure 2: Measure vectors of 511 Erdos1 authors, the big red point(1,1,0) stands for the "
       "ideal vector of the most crucial one.",
       "Figure N:", cited(7, 8, ["Figure 2"], 1,
                          "The three-dimensional graph is shown in Figure 2", pattern="as-shown-in"),
       [RESULTS], "result", three_d="isometric", legend="inside", numbers=True, labels=True,
       note="a MATLAB 3-D scatter: about 500 small dark blue markers inside a dashed perspective "
            "box, one large red flattened marker on the floor corner labelled (1,1,0) in red bold "
            "italic, and a pale green two-line legend at the upper right ('measure vector' / 'of "
            "Erdos1 author'). Axis labels print green, rotated: 'Normalization Betweenness "
            "Centrality' on the left axis (0 to 0.8) and 'Normalization Degree Centrality' on BOTH "
            "the vertical axis (0.094 to 0.102) and the receding one (0 to 1.2) - the same string "
            "twice, so one of the three axes is mislabelled, almost certainly the vertical one, "
            "which should read closeness. The caption calls it three-dimensional and the prose "
            "calls it 'the three-dimensional graph'; the caption writes the ideal vector without a "
            "space: 'point(1,1,0)'")

figure(10, 1, "line",
       "Figure 3: The degree distribution of the Erdos1 network and the approximative power-law "
       "distribution.",
       "Figure N:", cited(10, 10, ["Figure 3"], 1,
                         "and the approximative power- law distribution is shown below in Figure 3."),
       [ERDOS], "other", legend="inside", numbers=True,
       note="two series in a boxed frame: a solid dark blue degree curve with markers and a red "
            "dashed approximative line, dashed black gridlines at every tick, legend inside at the "
            "upper right. Axes print 'degree(k)' 0-60 and 'P(k)' 0-0.18, both LINEAR, so the power "
            "law the caption names cannot be read off the drawing - the reference line is a fit in "
            "linear coordinates and the exponent -1.6 quoted on the page has no slope to sit on. "
            "The only figure caption in the paper set as a justified two-line paragraph across the "
            "full measure instead of a centred single line")

figure(12, 1, "node-link-network",
       "Figure 4: The directed citation network with weight added to nodes.",
       "Figure N:", cited(11, 12, ["Figure 4"], 1, "The Citation net- work is shown as Figure 4."),
       [APMODEL], "evaluation",
       note="raster, the 24-paper citation network, spring layout, thin black edges with small "
            "filled arrowheads. Node radius and fill both carry the paper weight - a near-white "
            "small circle for a light paper, a saturated dark blue disc with a printed weight for "
            "the six heaviest (0.322, 31.027, 39.265, 40.664 and two that print small enough to be "
            "uncertain at 150 dpi). Node IDs 1-24 print outside the circles in grey at about 5-6 pt. "
            "Arrow direction is untraceable wherever edges cross in the centre. The caption says "
            "weight is added to NODES, which is what the drawing does")

# ---------------------------------------------------------------- 5.2, the revised PageRank
table(13, 1, 6, 8, [APMODEL], "evaluation",
      "with ID of each paper are listed in Table 4.",
      "LaTeX grid set as three stacked bands of two rows each, 8 columns wide: an ID row "
      "(No.1-No.8, No.9-No.16, No.17-No.24) over its weight row, three times. Six rules in all - one "
      "above and one below each band - and no vertical, no outer box and no rule between an ID row "
      "and its weights, so the pairing is held by position only. 311.1 pt against the 419.4 pt text "
      "measure (74 %), centred. Unnumbered in the body but captioned on the line above: 'Table 4: "
      "ID of papers and their Weight', title case and no closing stop, the only table title set that "
      "way. Header_rows counts the first ID row; each column below it alternates a text label with "
      "its numeric value, so no column is purely text. Four weights repeat across different IDs "
      "(31.027 at No.4 and No.13, 38.597 at No.8 and No.14, 3.381 at No.6 and No.16, 9.737 at No.10, "
      "No.22 and No.23) - two papers in the same journal share its impact factor",
      cap="Table 4: ID of papers and their Weight", numeric=8,
      mention=cited(13, 13, ["Table 4"], 1,
                    "with ID of each paper are listed in Table 4."))

figure(14, 1, "flowchart-or-schematic",
       "Figure 5: The flow chart of iteration process",
       "Figure N:", none_mention(),
       [APMODEL], "evaluation",
       note="raster, a two-lane Microsoft Office flow chart - orange-to-peach gradient lane bars "
            "with drop shadows, rounded boxes with bevel and shadow, blue-grey connectors. Top lane "
            "runs G -> D -> a box holding 'A=qGD+(1-q)/N' -> an UNLABELLED circle holding only a "
            "multiplication cross -> PR(0) -> 'Impact factor', tagged 'initialization'. Bottom lane "
            "runs 'PR(k)=A*PR(k-1)' -> 'Max(abs(PR(k)-PR(k-1))) <0.0001' -> 'Yes' -> 'PageRank=PR(k)' "
            "with a 'No' feedback edge. Box text prints at 7-8 pt. Never cited by number: the prose "
            "below it says 'We implement the iteration based on the equation above', so the drawing "
            "is reached by position")

table(14, 2, 25, 6, [APMODEL], "evaluation",
      "as is shown in Table 5.",
      "LaTeX grid, 24 ranks as two side-by-side blocks of three columns each (Ranking, PR_i(k), ID), "
      "header band printed twice, so cols counts the physical 6. Three rules only - above the "
      "header, under the header, below the last row - and no vertical anywhere, not even between the "
      "two blocks. 367.1 pt against the 419.4 pt measure (88 %), centred. MEASURED BOX STOPS SHORT: "
      "the box ends at 564.1 pt, so the last two printed lines - ranks 11 and 23 at 565.5 pt and "
      "ranks 12 and 24 at 576.9 pt - and the closing rule at 589.6 pt all fall below the measured "
      "bottom, and the bbox the record carries is the one fig_extract measured, not the whole table. "
      "Values right-aligned to four or five decimals with "
      "ties printed as identical strings (five 0.00047, three 0.00051, two 0.00142) and no tie mark",
      cap="Table 5: The rank of papers by the stable PageRank value.", numeric=4,
      mention=cited(14, 14, ["Table 5"], 1, "as is shown in Table 5."))

table(15, 1, 13, 4, [APMODEL], "evaluation",
      "Table 6: Cited quantities per year of each paper.",
      "LaTeX grid, two side-by-side blocks inside one ruled frame, each block 'ID' over 'cited "
      "quantities/year' with 12 body rows, header band printed twice, so cols counts the physical 4. "
      "Rules: one above the header, one under it, one below the last row, plus ONE full-height "
      "vertical between the two blocks and no outer side verticals - horizontal ruling throughout, "
      "so booktabs with a centre divider rather than a closed grid. 321.6 pt against the 419.4 pt "
      "measure (77 %), centred. The right block is not monotone: 11.0, then 0.5, then 3.125. Values "
      "are right-aligned, so 1355.5, 97.1 and 3.125 all end on the same x and the decimal points do "
      "not line up",
      cap="Table 6: Cited quantities per year of each paper.", numeric=2,
      mention=cited(14, 15, ["Table 6"], 1, "as the parameter, which is shown in Table 6"))

figure(15, 2, "scatter",
       "Figure 6: Authority-Popularity Diagram for the citation network",
       "Figure N:", cited(14, 15, ["Figure 6"], 1,
                          "we draw a picture of 24 nodes (as is shown in Figure 6)."),
       [APMODEL], "evaluation", numbers=True, labels=True,
       note="MATLAB axes holding 24 dark red upward triangles, boxed frame, ticks inward on all four "
            "spines, no gridlines and no legend: x prints 'cited quantities/year' 0.5-4.5 and y "
            "prints 'PageRank' 2.6-4.2, both linear, and neither tick value is the quantity its own "
            "axis title names: the page above sets log10 of a multiple of PR(k) as ordinate and "
            "log10 of ten times the cited quantities per year as abscissa, so the ticks carry the "
            "LOGARITHMS. Four rounded white quadrant labels were pasted on top "
            "of the plot - 'High authority / More popular' at the upper right, 'Low authority / "
            "More popular' at the lower right, 'High authority / Less popular' and 'Low authority / "
            "Less popular' on the left - with one strong dashed vertical at 2.5 and a horizontal "
            "divider near 3.4 that prints faint enough to vanish in reproduction. An orange callout "
            "box at the upper left names 'No.14: Watts,D. and Strogatz.S. / Collective dynamics of "
            "'small-world' networks' and a thick curved arrow links it to the node ringed in open "
            "green at about (3.9, 4.12); the arrowhead sits at the BOX end, so it points away from "
            "the node. Second by-number citation on the same page ('we divided Figure 6 into four "
            "regions'), the only exhibit the prose reads back by number")

# ---------------------------------------------------------------- 5.3 to 5.5
figure(16, 1, "node-link-network",
       "Figure 7: The directed citation network with weight added to links.",
       "Figure N:", cited(16, 16, ["Figure 7"], 1,
                          "to construct a co-star network(as is shown in Figure 7)."),
       [COSTAR], "other",
       note="raster, NetDraw-style directed network of 15 film stars plus one blue square at the "
            "centre that carries NO label, so 16 nodes. All nodes are identical small blue squares "
            "with dark borders - neither size nor colour encodes anything, unlike Figure 4 - and "
            "grey labels sit outside them. Edges are thin grey arcs with small arrowheads, most of "
            "them carrying a grey numeric weight (7.4, 8.6, 5.3, 8.9, 4.9 ...). The caption is copied "
            "verbatim from Figure 4 two sections earlier and still says 'directed citation network', "
            "while the page addresses a co-star network of actors - the caption is wrong about its "
            "own subject. Labels stack on top of one another and on top of the arcs where edges "
            "converge (Brad Pitt, Angelina Jolie, Tom Hanks), and the 'Toby Maguire' label misspells "
            "Tobey")

figure(17, 1, "flowchart-or-schematic",
       "Figure 8: The diagram for modified algorithm.",
       "Figure N:", cited(16, 17, ["Figure 8"], 1, "as is shown in Figure 8."),
       [SENSITIVITY], "sensitivity", panels=2, layout="1x2",
       note="raster, two panels side by side, Office drawing shapes: three filled blue ellipses "
            "lettered i, k and n with thick black arrows i->k and i->n, 'PageRank=1' printed under "
            "node i in both panels. The left panel labels both arrows 0.5; the right panel replaces "
            "them with stacked fractions 3/(3+4) x1 and 4/(3+4) x1, and a large blue block arrow "
            "between the panels carries the word 'improve'. Two panels of the SAME family, so one "
            "row with panel_count 2 rather than two rows. Stroke weights differ from arrow to arrow "
            "within one panel: the right-hand i->n arrow prints visibly heavier than its i->k "
            "neighbour. 'PageRank=1' prints with no spaces around the equals sign")

figure(18, 1, "scatter",
       "Figure 9: Authority-Popularity Diagram for the co-star network",
       "Figure N:", cited(17, 18, ["Figure 9"], 1,
                         "In Figure 9 , we set log10 (the number of Google search results) as abscissa",
                         pattern="direct"),
       [SENSITIVITY], "sensitivity", numbers=True, labels=True,
       note="raster, Excel-style axes with outward ticks and a full box frame, navy asterisk markers "
            "on white: x prints 'Results of Google Search' on a LOG scale with only three ticks, 10^6, "
            "10^7 and 10^8, and y prints 'PageRank' linear from 0 to 0.15. The caption calls it an "
            "authority-popularity diagram and the body gives it no units; the abscissa is the raw "
            "search count in millions, not its log10, even though the prose above promises the "
            "logarithm. Two dashed black reference dividers, horizontal near 0.076 and vertical near "
            "1.5e7, sit under four bevel-textured green quadrant boxes - 'High authority / More "
            "popular', 'High authority / Less popular', 'Low authority / More popular', 'Low "
            "authority / Less popular' - exactly as Figure 6 does. FOURTEEN markers print against the "
            "FIFTEEN rows of Table 7 on the same page: the point for 238 million searches "
            "(Tom Cruise, PR 0.117486) is absent, and two of the fourteen are clipped by the right "
            "frame. One point is labelled 'Angelina Jolie' in red with an arrow to the top-right "
            "marker - the only printed data label in the paper")

figure(19, 1, "line",
       "Figure 10: Sensitivity to Damp Coefficient q",
       "Figure N:", cited(19, 19, ["Figure 10"], 1, "The results were shown in Figure 10."),
       [STRENGTHS], "evaluation", numbers=True,
       note="raster, one thick black polyline with filled red triangle markers and dotted gridlines "
            "at every major tick in both directions: x prints 'Damp Coefficient q' from 0.2 to 1 and "
            "y prints 'Similarity' from 0.4 to 1, both linear, no legend, no fitted line and no "
            "printed data labels. Thirteen markers at q = 0.30, 0.40, 0.50, 0.55, 0.60, 0.65, 0.70, "
            "0.75, 0.80, 0.85, 0.90, 0.95 and 1.00, drawn against the frame with no scale given "
            "anywhere: the curve sits near 0.40 at q 0.3, dips to about 0.74 at q 0.6, plateaus at "
            "the top frame for q 0.80-0.85 and settles back near 0.74. The q 0.30 marker and both "
            "plateau markers are clipped by the frame, and the rotated y title is squeezed into the "
            "tick-label gutter at 5-6 pt. The prose reads a 'slow change' off a curve whose plateau "
            "touches 1.0")

figure(21, 1, "node-link-network",
       "Figure 11: The shortcut to boost influence",
       "Figure N:", none_mention(),
       [PHILOSOPHY], "other",
       note="raster, a PowerPoint-style concentric diagram rather than a graph-tool export: pale "
            "blue gradient rings draw a bullseye and about 40 circles sit on it in four classes - "
            "small white discs at the rim, periwinkle mid, saturated blue inner, and one small navy "
            "hub at the centre - so radius from the hub and fill both carry the same variable, with "
            "no node labels and no legend. Edges are 0.5 pt straight lines with no arrowheads except "
            "two short maroon stubs at the hub. A thick orange arrow labelled 'The shortcut' enters "
            "from outside the right frame into a blue node one ring off the centre. The art prints at "
            "the TOP of the reference page, so the unnumbered 'References' heading and the whole "
            "bibliography sit BELOW it; its section is the numbered 6 on p20, whose unnumbered "
            "sub-heading 'Shortcut to boost influence' asks the question. Never cited by number - "
            "the prose points at it with 'The solution we propose by our model is shown as below:' "
            "followed by three bullets")

# ---------------------------------------------------------------- payload
RULES = [
    "a numbered table whose two rules stand 180 pt apart is measured by no region at all, so four "
    "of the seven tables in this paper are declared gaps instead of receiving an invented bbox "
    "[table.rule_style]",
    "a grid drawn as two side-by-side blocks inside one ruled frame is one table: cols counts the "
    "physical columns and the header band prints twice [table.cols]",
    "horizontal rules with one full-height centre divider and no side verticals are booktabs, not "
    "vertical-rules and not boxed, because no cell is closed [table.rule_style]",
    "a band of two alternating rows - an ID row over its value row, three times - is six printed "
    "rows and one header row, not three rows [table.rows]",
    "a grid set short of the measure keeps width full: 74 to 88 per cent of the local 419.4 pt "
    "measure is a wide table with air around it, and the percentage is named in the note "
    "[table.width]",
    "the measured box is not the exhibit: Table 5's region stops at 564.1 pt while its closing rule "
    "prints at 589.6 pt, and the record keeps the measured bbox with the shortfall in the note "
    "[table.note_sentence]",
    "a caption printed above the grid belongs to that grid even when the previous exhibit's caption "
    "printed below its art: the side follows the exhibit type, and this paper splits cleanly - "
    "figures below, tables above [caption.position]",
    "a numbered caption that names the wrong subject is recorded as printed and the mismatch goes "
    "into the item note; Figure 7 carries Figure 4's caption word for word over a different network "
    "[caption.verbatim]",
    "a 3-D scatter drawn in a dashed perspective box is scatter with three_d isometric, not "
    "surface-or-3D, because the axes hold point markers and no mesh [geometry.three_d]",
    "two panels of the same family print as one row with panel_count 2, and only exhibits whose "
    "panels differ in family become composite-panel [geometry.panel_count]",
    "printed_numbers is about the axes: a scatter whose ticks print 0.5 to 4.5 carries them, while "
    "the illustration that follows has no scale at all [geometry.printed_numbers]",
    "an exhibit the prose never numbers is still a row when it fills the page slot - Figure 5 is "
    "introduced as 'the equation above' and Figure 11 as nothing at all [mention.count]",
    "a figure cited a page or two BEFORE it prints carries a negative lead_pages, and the value is "
    "the exhibit page minus the citing page, never an absolute [mention.lead_pages]",
    "a heading printed below the art can still govern the page, but here every path is the printed "
    "label of the heading that actually governs the region, so section_numbered is true throughout "
    "except the unnumbered reference list [place.section_numbered]",
    "a legend pasted into the plot area counts as legend inside, and an annotation box with an "
    "arrow is not a legend: Figure 6 keys nothing and carries legend none [geometry.legend]",
]

NOTE = (
    "Fourteen measured regions over twelve of twenty-one pages, all accounted for, no refusals: "
    "eleven figure rows and three tables. The paper numbers eleven figures and seven tables and "
    "never mixes the two - every figure caption prints below its art and every table caption above "
    "its grid. Two grids print their header twice because they are two blocks side by side inside "
    "one frame (Tables 5 and 6), so both carry the physical column count.\n\n"
    "Unmeasured, declared rather than invented: Table 1 on p3, Table 2 on p8, Table 3 on p9 and "
    "Table 7 on p18 all print as two-rule booktabs grids, and the two rules of each stand 314.1, "
    "178.7, 178.5 and 180.4 pt apart, past the 120 pt grouping gap, so the layout pass never "
    "clusters them - and the table-tail fallback cannot either, because it seeds its window from a "
    "rule's own bottom edge and a stroked rule has zero height. Table 1 is the "
    "symbol table, 2 columns with three centred bold group rows merged across both, rule under the "
    "header and closing rule, 316.9 pt or 76 per cent of the measure. Table 2 is 4 columns over 15 "
    "ranks "
    "('Ranking', 'D_C(x)', 'ID', 'Name of authors'), 336.9 pt or 80 per cent. Table 3 is 4 columns "
    "over 15 "
    "ranks ('Ranking', 'E value', 'ID', 'Name of authors'), 334.9 pt or 80 per cent, and its rank 1 "
    "value "
    "prints 0.26 against 0.234, 0.209 everywhere else. Table 7 is 3 columns over 15 stars ('Name', "
    "'PR value', 'Google search results(million)'), 321.7 pt or 77 per cent, and it is the table "
    "Figure 9's "
    "abscissa is taken from.\n\n"
    "Defects recorded, not corrected: Figure 2 labels two of its three axes 'Normalization Degree "
    "Centrality', so one label is wrong; Figure 3's caption promises a power-law distribution while "
    "both axes are linear, so the -1.6 exponent the prose quotes has nothing to sit on; Figure 7 "
    "carries Figure 4's caption verbatim ('directed citation network') over a co-star network of "
    "actors, and its 'Toby Maguire' label misspells Tobey; Figure 8 prints 'PageRank=1' with no "
    "spaces and mixes two stroke weights between arrows of the same panel; Figure 6's dashed "
    "quadrant divider at y 3.4 prints faint enough to disappear in reproduction and its callout "
    "arrow points at the box rather than at the node; Table 4 halves its caption into title case "
    "with no closing stop, and four impact factors repeat across different papers because two "
    "papers share a journal; Table 5 truncates its values to four or five decimals with five ties "
    "printed as identical strings and no tie mark; Table 6's right block runs 11.0, 0.5, 3.125, out "
    "of order; every use of 'MATLAB@2012b' on the page should be a registered mark; and the prose "
    "typos stand as printed: 'The Citation net- work', 'network(as is shown in Figure 7)', "
    "'Strogatz.S.', 'Watts,D.'."
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

out = PROXY / "pc64-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
