"""Hand pass for P-C-2014-27688-856eb1b7 (a 2014 C paper that scores Erdos1 co-authorship by
centrality, reads a 16-paper citation network through a topological-sorting algorithm, and then
runs the same algorithm over a 500-company US media ownership network), 19 PDF pages.

Fourteen measured regions over ten pages: thirteen rows and one exclusion, nothing unaccounted.

    page    region   what it is
    4       r1       Figure 1, the co-author network, raster
    5       r1       Table 1, basic data of centrality
    6       r1       Figure 2, the co-author relationship of A, B, C, D, raster, two panels
    7       r1       Table 2, top 20 researchers
    8       r1       Figure 3, citation graph of the 16 papers, raster
    9       r1       Figure 4, the larger citation network, raster
    9       r2       Figure 5, citation chain against coauthor chain, raster, two panels
    10      r1       Table 3, four kinds of centrality over 16 papers
    12      r1       Figure 6, the ruled box holding pseudo-code and the flowchart
    12      r2       the bitmap inside Figure 6's right cell - excluded, fragment-of-other
    12      r3       Table 4, contribution coefficient of the 16 papers
    13      r1       Table 5, self-contribution coefficient at four settings of S
    15      r1       Table 6, 15 companies by score and in-degree
    15      r2       Table 7, the published top 20 companies of 2001

Nothing is unmeasured here: the paper numbers six figures and seven tables, thirteen numbers in
all, and every one of them owns a region. All seven grids are closed boxes - full-height vertical
rules at every column boundary plus a horizontal rule on every row - so the whole table set is
vertical-rules and not one booktabs grid prints in the paper.

Figure 6 is the paper's one composite: a four-sided rule box divided at 276.2 pt into a typeset
pseudo-code cell and a bitmap flowchart cell, with the caption printed INSIDE the box. The bitmap
is a measured region of its own and is excluded as a fragment of that row rather than counted as a
second exhibit.

Usage: python -I tools/_dist_paper65.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2014-27688-856eb1b7"
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

# The heading pass on this paper is polluted twice over: p12 returns the pseudo-code lines as
# headings ('2 Ci = Ncited (i) / ...', '7 Ci = Ci x S', '8 Sort( C )', '9 Print( C )') because the
# algorithm block is set in a display font the detector reads as a heading, and p15 returns the
# twelve printed rows of Table 7 as headings. Every path below is the printed label of the heading
# that actually governs the region, not the nearest detector record.
BUILD = "3.1 Building the model"
SIGNIFICANT = "3.2 Find Significant Researchers"
CITENET = "4.1 Construct the Citation Network"
COMPARE = "4.2 Compare the coauthor and citation"
MODEL = "4.3.1 Modeling"
SOLUTION = "4.3.2 Solution and Result Analysis"
STABILITY = "4.3.3 Stability Test"
OWNERSHIP = "5.2 Result and Analysis"

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
          note_sentence: str, note: str, *, rule: str = "vertical-rules", numeric: int = 1,
          header_rows: int = 1, numbered: bool = True, width: str = "half",
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


# ---------------------------------------------------------------- 3.1 to 3.2, the coauthor network
figure(4, 1, "node-link-network",
       "Figure 1: the co-author network",
       "Figure N:", cited(4, 4, ["Figure 1"], 2,
                          "We use software Gephi to draw the graph and the network diagram is "
                          "shown in Figure 1."),
       [BUILD], "model",
       note="raster, one embedded bitmap 590x595, a Gephi spring layout of the Erdos1 coauthorship "
            "graph: no arrowheads, no axes, no ticks, no frame, no legend and NOT ONE node label. "
            "Node fill and node radius carry the same variable twice - the prose says the radius is "
            "the coauthoring count with Erdos and that darker is more coauthors - so a dense core of "
            "small dark discs is ringed by larger pink and red ones. No size reference box is "
            "printed. The prose fixes the graph at 511 vertices and 18000 edges; the drawing is far "
            "too dense to count against either figure and shows only a few hundred discs, so both "
            "counts are taken from the text and not measured off the art. Cited twice by number: "
            "here, and again on p6 as 'According to the above table and Figure 1'")

table(5, 1, 4, 5, [BUILD], "model",
      "Then, we use the UCINET to calculate some basic metrics and show them in table 1.",
      "Closed box: full-height vertical rules at 119.9, 190.9, 261.9, 333.0, 404.0 and 475.1 pt "
      "plus a horizontal rule above the header, under it and between every row - five rules, four "
      "rows, so header_rows 1 and the three body rows are Average, Minimum and Maximum. 356.2 pt "
      "against the 418.3 pt text measure (85 %), indented from both margins. The header prints "
      "'type' in lower case beside 'Degree', 'Closeness', 'Betweenness' and 'Eigenvector'. Every "
      "value carries exactly three decimals but is LEFT-aligned in its cell - 1.292, 0.000 and "
      "10.392 all start on the same x - so decimal_aligned is false even though the digits line up "
      "by luck of a fixed format. Re-read one page on as 'According to the above table and Figure "
      "1'",
      cap="Table 1: the basic data of centrality", numeric=4, width="full",
      mention=cited(5, 5, ["table 1"], 1,
                    "Then, we use the UCINET to calculate some basic metrics and show them in "
                    "table 1."))

figure(6, 1, "node-link-network",
       "Figure 2: the co-author relationship of A,B,C,D",
       "Figure N:", none_mention(),
       [SIGNIFICANT], "model", panels=2, layout="1x2", labels=True,
       note="raster, 795x284, two drawings on one baseline with no (a) or (b) letters, no frame, no "
            "axis and no legend. The left drawing puts four open circles at the corners of a square "
            "labelled A, B, C, D and joins every pair - all six edges including both diagonals - "
            "with 'Paper i' printed under the square. The right drawing prints the same four letters "
            "over open circles in a horizontal row joined by three edges forming a path, with 'Paper "
            "i', 'Paper j' and 'Paper k' under the links. The two panels contrast a set that shared "
            "one paper with a chain that shared three, which is exactly the argument the section "
            "makes; both are the same family, so one row with panel_count 2. Never cited by number - "
            "the prose says only 'There are two kinds of coauthor relationship in the network.'")

table(7, 1, 11, 6, [SIGNIFICANT], "model",
      "Table 2: the top 20 researches with highest importance",
      "Closed box, and the widest grid in the paper: 416.5 pt against the 418.3 pt measure (99.6 %), "
      "flush to both margins and overhanging the right one by about 1 pt. Vertical rules at 89.4, "
      "255.6, 290.5, 325.1, 435.9, 470.6 and 505.4 pt, horizontal rules above the header, under it "
      "and after every row: twelve rules, eleven printed rows. The 20 researchers are set as TWO "
      "side-by-side blocks of the same three columns, so the header band prints twice - "
      "'Name(1-10) Ce Ca Name(11-20) Ce Ca' - and cols counts the physical 6. The header band is "
      "the only tall one in the paper at 31.7 pt against 16.1 pt for every body row. Unlike Table "
      "1, the four numeric columns ARE decimal-aligned, on two decimals throughout. The caption says "
      "'researches' for researchers and the prose above says 52 researchers survived the Ca>=2 "
      "filter",
      cap="Table 2: the top 20 researches with highest importance", numeric=4, width="full",
      decimal=True)

# ---------------------------------------------------------------- 4.1 to 4.2, the citation network
figure(8, 1, "node-link-network",
       "Figure 3: the citation relationship among the 16 papers",
       "Figure N:", none_mention(),
       [CITENET], "model", numbers=True,
       note="raster, 805x483, the 16-paper citation digraph: sixteen circles each holding its "
            "printed number 1 to 16, thin straight edges with small filled arrowheads (paper 11 -> "
            "paper 1 means 11 cited 1), no frame, no legend, no axis labels and no names. A single "
            "horizontal line under the art carries the year ticks 1959, 1979, 1987, 1996, 1998, 1999, "
            "2000, 2001, 2002, 2003, 2006, 2007 and 2011 with a right-pointing arrowhead, but it is "
            "unlabelled and no node sits on it - so the claim the prose makes, that the graph shows "
            "publication time as well as citation, rests on a scale the drawing does not use. Never "
            "cited by number: the prose reads 'In this graph[10][11], a vertex reprsents a paper'")

figure(9, 1, "node-link-network",
       "Figure 4: network of the papers’ citation relationship",
       "Figure N:", none_mention(),
       [CITENET], "model", numbers=True,
       note="raster, 466x481, and NOT the 16-paper network: about eight large orange and red hubs "
            "carrying the numbers 1, 2, 4, 8, 9, 10, 13 and 14, a few faint grey numbered nodes, and "
            "some hundreds of tiny unlabelled black dots fanned out on radial hairlines that show no "
            "arrowheads at this scale. The two numbered hubs that do not fit the 16-paper label set "
            "(8, 13) and the unnumbered mass say the art was drawn from a wider citation set than "
            "the section counts, and the page never reconciles the two - the prose below it says only "
            "'Similarly, this is a Directed Acyclic Graph (DAG)'. It prints at the head of p9 with "
            "about 8 pt of white above the topmost marks, so nothing is clipped by the page edge, "
            "and its caption prints below it on the same page")

figure(9, 2, "flowchart-or-schematic",
       "Figure 5: the citation relationship and the coauthor relationship",
       "Figure N:", none_mention(),
       [COMPARE], "other", panels=2, layout="1x2", labels=True,
       note="raster, 846x222, two panels on one baseline. Left, three ruled boxes labelled A, B and "
            "C holding 'Theory 1', 'Theory 1 / Theory 2' and 'Theory 1 / Theory 2 / Theory 3', with "
            "grey arrows between them labelled 'cite' pointing right to left, C -> B -> A. Right, "
            "three open circles in a horizontal chain, each link labelled 'coauthor' above it and A, "
            "B, C printed under the nodes. The left panel is a box-and-arrow schematic and the right "
            "is a small node-link chain, but both state the same contrast the section draws and "
            "neither is separable from the other, so this is one schematic row with panel_count 2 "
            "rather than composite-panel. Never cited by number - the section reads 'there exists "
            "transitive relation while in the coauthor network, there does not exist transitive "
            "relation'")

# ---------------------------------------------------------------- 4.3, the contribution model
table(10, 1, 16, 4, [MODEL], "model",
      "The respective sequence of Degree Centrality, Closeness Centrality, Betweenness Centrality "
      "and Eigenvector Centrality is shown in Table 3.",
      "Closed box over 4 columns of paper numbers: vertical rules at 181.0, 233.0, 285.6, 353.2 and "
      "413.8 pt, seventeen horizontal rules, so sixteen printed rows - one header and the fifteen "
      "ranks of papers 1 to 16 with paper 7 absent from the top row of every column. 233.3 pt "
      "against the 418.3 pt measure (56 %), a narrow centred grid. The header prints 'In Degree' as "
      "ONE cell over the first column as the word positions show ('In' at 186.6-194.8 and 'Degree' "
      "at 197.2-227.9 pt, both inside the 181.0-233.0 column), so the four labels are In Degree, "
      "Closeness, Betweenness and Eigenvector and the first column does NOT spill into its "
      "neighbour. All four columns are integers, centred, so nothing is decimal-aligned",
      cap="Table 3: four kinds of centrality", numeric=4, width="half",
      mention=cited(10, 10, ["Table 3"], 1,
                    "The respective sequence of Degree Centrality, Closeness Centrality, Betweenness "
                    "Centrality and Eigenvector Centrality is shown in Table 3."))

figure(12, 1, "composite-panel",
       "Figure 6: the flowsheet of the algorithms",
       "Figure N:", none_mention(),
       [MODEL], "model", panels=2, layout="1x2", position="above",
       note="one RULED BOX, 84.4 to 511.1 pt wide and 72.0 to 369.4 pt tall, closed on all four "
            "sides and divided by a full-height rule at 276.2 pt into two cells - which is why the "
            "measured region is the box and not an image. The LEFT cell is TYPESET, not drawn: the "
            "word 'Pseudo-Code', the call 'AL-CITATION (V,E,d)' and nine numbered algorithm lines "
            "set in LaTeX math. The RIGHT cell holds the only bitmap (356x500): start ellipse, "
            "C_i = Ncited(i)/[t_now - t_pub(i)], a decision diamond d_in(i)=0 and d_out(i)!=0 with "
            "labelled Yes and No branches, 'Distribute part of C averagely', C_i=C_i*S, 'Delete "
            "vertex i' with a feedback arrow back to the diamond, sort(C), print(C), End. Two cells "
            "of different kinds - typeset code beside a drawn flowchart - so composite-panel with "
            "panel_count 2. The caption prints INSIDE the box at the bottom of the right cell "
            "(y 358 pt, above the 369.4 pt bottom rule), the only caption in the paper set that way, "
            "and the prose reaches the exhibit only as 'The pseudo-code and the flowchart of this "
            "citation algorithm are shown below.' on p11")

EXCLUDED.append({
    "page": 12,
    "bbox": REG[(12, 2)],
    "kind": KIND[(12, 2)],
    "reason": "fragment-of-other",
    "note": "the flowchart bitmap, 281.8 to 505.2 pt by 77.9 to 347.5 pt, sits wholly inside "
            "Figure 6's right cell and is the drawn half of that one caption. Counting it would "
            "double the exhibit; it is recorded as a fragment of the row on p12 r1",
})

table(12, 3, 9, 4, [SOLUTION], "solution",
      "We calculate the contribution coefficient of 16 given papers and list in table 4.",
      "Closed box over two side-by-side (Paper Number, C) pairs, so the header band prints twice and "
      "cols counts the physical 4: 'Paper Number(1-8) C Paper Number(9-16) C'. Vertical rules at "
      "172.2, 265.4, 297.4, 396.0 and 422.7 pt, ten horizontal rules, nine printed rows - one header "
      "and the eight ranks that carry all sixteen papers. 251.0 pt against the 426.7 pt measure on "
      "this page (59 %), a narrow centred grid. Values are integers down to 78 and 209 with no "
      "decimals, centred, so nothing is decimal-aligned. The left block runs 2037, 1347, 1128, 869, "
      "767, 738, 716, 567 and the right 479, 426, 218, 209, 209, 103, 78, 78 - two ties at 209 and "
      "two at 78 print as identical strings with no tie mark",
      cap="Table 4: the contribution coefficient of 16 given papers", numeric=4, width="half",
      mention=cited(12, 12, ["table 4"], 1,
                    "We calculate the contribution coefficient of 16 given papers and list in "
                    "table 4."))

table(13, 1, 8, 5, [STABILITY], "test",
      "Table 5: the value of self-contribution coefficient(s) with different values of S",
      "Closed box: vertical rules at 164.9, 211.1, 262.6, 308.7, 377.8 and 430.0 pt, nine horizontal "
      "rules, eight printed rows - one header and seven ranks. 265.6 pt against the 417.5 pt "
      "measure (64 %), centred. Five columns of paper numbers: C(S=0.5), C(S=0.75), C(S=0.9), "
      "C(S(0.5-0.95)) and PageRank, the last a sixth measure set beside the paper's own at four "
      "settings of its parameter. The fourth header names the range 0.5 to 0.95 while the prose "
      "that sets the experiment says 'a random value(0-1)' - the header and the sentence disagree "
      "about the range, and only the later sentence ('a random value from 0.5 to 0.95') matches the "
      "grid. Integers throughout, centred, no decimal alignment",
      cap="Table 5: the value of self-contribution coefficient(s) with different values of S",
      numeric=5, width="half")

# ---------------------------------------------------------------- 5.2, the ownership network
table(15, 1, 16, 3, [OWNERSHIP], "result",
      "The result is shown in Table 6.",
      "Closed box: vertical rules at 148.8, 329.8, 376.9 and 446.0 pt, seventeen horizontal rules, "
      "sixteen printed rows - one header and the fifteen companies the algorithm ranks. 297.7 pt "
      "against the 418.3 pt measure (71 %), centred. Name is the only text column, so numeric_cols "
      "is 2 for Score and Indegree(d_in). The Score column is NOT decimal-aligned: 3825 prints with "
      "no decimal at all, 2231.1 with one place and 970.924 with three, all centred, so the decimal "
      "points stand at different x. Only three of the fifteen companies print a non-zero in-degree "
      "(AT&T 1, Comcast 2, Viacom 2) and every other row prints 0, so the ranking is carried by the "
      "score alone. 'AT&T' is the only name with an ampersand and it prints as a bare '&' in the "
      "cell",
      cap="Table 6: result from the algorithm", numeric=2, width="half",
      mention=cited(15, 15, ["Table 6"], 1, "The result is shown in Table 6."))

table(15, 2, 11, 4, [OWNERSHIP], "result",
      "Table 7: the top 20 companies ranked in 2001 from the web",
      "Closed box over two (Rank, Company) pairs: vertical rules at 168.7, 200.6, 293.8, 325.7 and "
      "426.2 pt, twelve horizontal rules, eleven printed rows - one header reading 'Rank Company "
      "Rank Company' and ten body rows carrying ranks 1 to 20. 257.9 pt against the 418.3 pt "
      "measure (62 %), centred. numeric_cols is 2 for the two rank columns; the two company columns "
      "are text. No merged cells: the 2-up layout is four genuine columns and the header repeats "
      "rather than spanning. The list is the 2001 published ranking taken from the web, not output "
      "of the model, so this grid and Table 6 above it are different objects on the same page - the "
      "prose compares them, claims 9 of the 15 appear in the top 20, and gets 9 only if Clear "
      "Channel, Viacom Inc against Viacom, Cox against Cox Enterprises, Hearst, Gannett, Comcast, "
      "Vivendi Universal against ViVendi Universal, Disney against The Walt Disney Co and Time "
      "Warner are matched loosely",
      cap="Table 7: the top 20 companies ranked in 2001 from the web", numeric=2, width="half")

# ---------------------------------------------------------------- payload
RULES = [
    "every grid in this paper is a closed box - full-height vertical rules at every column boundary "
    "plus a horizontal rule on every row - so all seven tables are vertical-rules and the paper "
    "prints no booktabs grid at all [table.rule_style]",
    "rows counts every printed row including the header band: Table 3's header over fifteen rank "
    "rows is sixteen, and the count comes from the number of horizontal rules minus one, not from "
    "the text layer's line order [table.rows]",
    "cols counts the PHYSICAL grid, so a table set as two side-by-side blocks of the same columns "
    "and a table set as two (Rank, Company) pairs both print their header twice and take 6 and 4 "
    "columns respectively [table.cols]",
    "a grid indented well inside the measure keeps width half: 56 to 71 per cent of the local 417 "
    "to 427 pt measure, while the two flush grids at 85 and 99.6 per cent are full, and the "
    "percentage is named in each note [table.width]",
    "a header cell that prints two words over what looks like one column is still one cell: 'In "
    "Degree' sits entirely inside the 181.0 to 233.0 pt column and the grid keeps 4 columns, not 5 "
    "[table.header_rows]",
    "fixed decimal places are not decimal alignment: Table 1's three-decimal values are "
    "left-aligned and Table 6's mixed-precision scores are centred, so both are decimal_aligned "
    "false while Table 2's two-decimal columns are true [table.decimal_aligned]",
    "the measured box is the exhibit even when the box holds typeset text beside art: Figure 6's "
    "region is the whole four-sided rule box, 84.4 to 511.1 pt, because that box is what the "
    "caption owns [table.note_sentence]",
    "captions follow the exhibit type without exception - every figure caption prints below its art "
    "and every table caption above its grid - and Figure 6 is the single exception, its caption "
    "printed INSIDE the box at the bottom of the right cell [caption.position]",
    "captions print the number with a colon and a lowercase gloss, 'Figure 6: the flowsheet of the "
    "algorithms', so numbering is Figure N: and Table N: throughout and no caption names a variable "
    "[caption.numbering]",
    "a caption that names its own subject wrongly is recorded as printed and the mismatch goes into "
    "the item note; Figure 4's caption calls a drawing of hundreds of nodes the network of the 16 "
    "papers [caption.verbatim]",
    "a grid the prose never numbers by number is still a table row: Table 2 is reached with 'The "
    "table below lists', Table 5 with 'Table shows' and Table 7 with 'in Table', all unnamed "
    "[mention.count]",
    "a lowercase by-name citation is recorded as it prints, case-sensitively: 'show them in table 1' "
    "and 'list in table 4' are style 'table 1' and 'table 4' and would not match a capitalised "
    "spelling [mention.style]",
    "an exhibit cited more than once keeps the FIRST citing page in first_page and counts the "
    "citations, so Figure 1 carries count 2 with lead_pages 0 even though its second citation is "
    "two pages later [mention.lead_pages]",
    "two panels that differ in what they draw - typeset pseudo-code beside a drawn flowchart - are "
    "composite-panel with panel_count 2, while two node-link drawings of the same family stay one "
    "row [geometry.panel_count]",
    "a bitmap measured inside a ruled frame is a fragment of that exhibit, not a second one: "
    "Figure 6's flowchart is excluded fragment-of-other and only the frame is a row "
    "[place.section_numbered]",
    "the heading detector reads a display-set algorithm block and a table's printed rows as "
    "headings, so every section_path here is the printed label of the heading that governs the "
    "region and never the nearest detector record [place.page_zone]",
]

NOTE = (
    "Fourteen measured regions over ten of nineteen pages, all accounted for: thirteen rows - six "
    "figures and seven tables - plus one excluded region, no refusals and no unmeasured exhibit. The "
    "paper numbers six figures and seven tables and all thirteen own a region, so this is the first "
    "paper in the lane with no ghost grid. Every table is a closed box: full-height vertical rules at "
    "every column boundary plus a horizontal rule on every row, 4 to 7 rules across and 5 to 17 down, "
    "so the whole set is vertical-rules and not one booktabs grid prints here.\n\n"
    "Three grids are two blocks side by side inside one frame - Tables 2, 4 and 7 each print their "
    "header band twice - so cols is the physical column count in each, and Table 2 is the widest "
    "object in the paper at 416.5 pt against a 418.3 pt measure, overhanging the right margin by "
    "about a point. Figure 6 is the one composite: a four-sided rule box divided at 276.2 pt into a "
    "typeset pseudo-code cell and a 356x500 bitmap flowchart cell, and the bitmap is a measured "
    "region of its own, recorded as a fragment of the frame rather than as a second exhibit. Its "
    "caption is the paper's only caption printed inside the box it names.\n\n"
    "Defects recorded, not corrected: Figure 4 draws hundreds of nodes with hubs numbered 8 and 13 "
    "where the section counts 16 papers, and the page never reconciles the two; Figure 3 hangs a "
    "year axis under the art that no node sits on, so the publication-time claim has no scale "
    "behind it; Figure 1 claims 511 vertices and 18000 edges for a drawing that shows a few hundred "
    "discs and carries no node labels at all; Table 5's fourth header column prints the range "
    "C(S(0.5-0.95)) while the sentence setting the experiment says a random value from 0 to 1 and "
    "the sentence below the grid says 0.5 to 0.95; Table 6's score column mixes whole numbers with "
    "one- and three-place decimals and only three of its fifteen companies have a non-zero "
    "in-degree; Table 3's first header cell prints the two words 'In Degree' over one column; and "
    "the prose typos stand as printed, among them 'a vertex reprsents a paper', 'This graph do not "
    "only reflect the citation relation', 'There are 9 companies list in Table can be found in top "
    "20', 'a vertex reprsents' and the caption 'the top 20 researches with highest importance'."
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

out = PROXY / "pc65-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
