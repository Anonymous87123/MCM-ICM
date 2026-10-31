"""Hand census of P-C-2014-30221-7af27341 (C-30221-Outstanding, 20 pages).

Fifteen measured regions over ten pages: two figures and thirteen tables. Six of the
nineteen printed tables carry no region and are declared gaps.

  p4  r1  Table 1    basic properties of the co-authoring graph
  p4  r2  Table 2    degree distribution
  p6  r1  Figure 1   the 511-node co-author network, drawn by stress majorisation
  p9  r1  Table 7    the seven authors who appear in every one of the four rankings
  p10 r1  Figure 2   the 15-paper citation network, labelled author-year(Cite:n)
  p11 r1  Table 8    top-3 papers by each measure, co-bibliography
  p11 r2  Table 9    top-3 papers by each measure, co-citation
  p12 r1  Table 10   top-3 papers, directed graph, with an MKC column
  p13 r1  Table 11   top-5 singers, basic model
  p14 r1  Table 12   top-5 movie actors, basic model
  p14 r2  Table 13   top-5 singers, bipartite model
  p14 r3  Table 14   top-5 songwriters, bipartite model
  p15 r1  Table 15   top-5 movie actors, bipartite model
  p15 r2  Table 16   top-5 films, bipartite model, one column short
  p16 r1  Table 17   best single co-author to add, eigenvector centrality

Not measured, declared in the note: Tables 3 (p6), 4 (p7), 5 (p8), 6 (p9), 18 (p17) and
19 (p18). Each is a real booktabs grid whose three rules span 233.2, 244.8, 233.2, 252.7,
292.1 and 193.5 pt - 32.5 to 49.1 per cent of the 595.3 pt page width - and the geometry
pass collects a rule only when it spans at least half the page, so none of the six is
visible to it. Table 18 misses that threshold by 5.5 pt.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2014-30221-7af27341"
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

TASK1 = "3 Task 1: Co-author Network of the Erdos1 Author"
TASK2 = "4 Task 2: Centrality"
DEGREE = "4.1 Degree Centrality"
EIGEN = "4.2 Eigenvector Centrality"
CLOSE = "4.3 Closeness Centrality"
BETWEEN = "4.4 Betweenness Centrality"
SUMM = "4.5 Summary of Centrality"
TASK3 = "5 Task 3: The Citation Network"
UNDIRECTED = "5.1 Undirected Graph Method"
DIRECTED = "5.2 Directed Graph Method"
TASK4 = "6 Task 4: Applications in Singers and Movie Actors"
BASIC = "6.1 Basic Model"
BIPARTITE = "6.2 Bipartite Graph Model"
TASK5 = "7 Task 5: Heuristics"
SENSITIVITY = "8 Sensitivity Analysis"
NONPARAM = "8.1 Non-parametric Models"

MEASURE = 418.3
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
          pattern: str = "as-shown-in", read: int = 1, gap: int | None = None,
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
          header_rows: int = 1, numbered: bool = True, width: str = "half",
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
        "caption": caption(word, "Table N." if cap else "none", position),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued,
                  "note_sentence": qp(note_sentence, [page, page + 1]) if note_sentence else ""},
    })


# ---------------------------------------------------------------- p4, the two opening grids
table(4, 1, 2, 4, [TASK1], "other",
      "",
      "Booktabs, three rules at 140.2, 157.4 and 174.5 pt spanning 351.3 pt, no vertical "
      "rule and no box, inset from both margins and centred. Two printed rows over four "
      "columns - Number of vertices, Number of edges, Average degree, Transitivity ratio - "
      "with one data row reading 511, 1713, 6.70 and 0.2238, every cell centred under its "
      "header. One data row of one width each, so decimal alignment is not assessable and "
      "is recorded false. 351.3 pt against the 418.3 pt measure (84.0 per cent). The "
      "caption prints 21.3 pt above the top rule at y 118.9 and the grid follows it "
      "immediately; the paragraph after the grid cites the same two numbers back "
      "('the average degree 6.70 is far less than 511') but never names Table 1, and no "
      "other page names it either, so the count is zero.",
      numeric=4, width="full",
      cap="Table 1: Basic Properties for Co-authoring Relationship",
      mention=none_mention())

table(4, 2, 2, 8, [TASK1], "other",
      "To see deeper into this graph, we summarize its degree distribution in Table 2.",
      "Booktabs, three rules at 283.7, 300.8 and 317.9 pt spanning 364.9 pt, no vertical "
      "rule, centred. Two printed rows over eight columns: the stub 'Range of degree' plus "
      "seven bins - 0, [1,2], [3,5], [6,10], [11,20], [21,30] and [31,dmax=52], the last "
      "with a 7 pt subscript that the crop resolves and the text layer flattens. The single "
      "data row is 37, 150, 122, 114, 51, 23 and 14, which sums to 511, exactly the vertex "
      "count Table 1 prints on the same page. 364.9 pt against the 418.3 pt measure (87.2 "
      "per cent). The text layer collapses that row into the digit run '37150122114512314' "
      "with no spacing, so the cell boundaries were read off the crop. The prose beside it "
      "says 'a fraction (16%) of researchers ... have co-authored with many researchers "
      "(more than 10)' while the table's three upper bins give 88 of 511, which is 17.2 per "
      "cent; the discrepancy is recorded, not corrected.",
      numeric=7, width="full",
      cap="Table 2: Degree Distribution",
      mention=cited(4, 4, ["Table 2"], 1,
                    "To see deeper into this graph, we summarize its degree distribution "
                    "in Table 2."))

# ---------------------------------------------------------------- p6, the co-author layout
figure(6, 1, "node-link-network",
       "Figure 1: The Graph Layout", "Figure N.",
       cited(5, 6, ["Figure 1"], 4,
             "Hence, despite its drawbacks, Figure 1 is a good characterization for "
             "co-authoring relationship.",
             pattern="as-shown-in"),
       [DEGREE], "other", numbers=False, labels=False,
       note="Vector art, not a bitmap: 3,950 drawing paths inside a 288.0 by 288.0 pt box "
            "whose only frame is a hairline rectangle at 155.4 to 440.7 pt square, with no "
            "axes, no ticks, no gridlines, no legend and no title inside the frame. Nodes "
            "print as small red triangles and edges as thin blue straight segments with "
            "arrowheads, so the drawing is directed even though the co-author relation it "
            "depicts is symmetric. No node carries a label or an id and no edge carries a "
            "weight, so nothing in the art can be counted at 150 dpi: the dense middle is an "
            "unresolved mat of blue lines and a few dozen isolated red triangles sit outside "
            "it, which is the 2-D stress-majorisation layout the surrounding prose blames "
            "for 'the unclear large-degree vertices'. The caption prints 20 pt under the "
            "foot rule at y 421.0 and is cut cleanly from the layer. Four by-number cita-"
            "tions, three of them on p5 a page before the art and the fourth on p10.")

# ---------------------------------------------------------------- p9, the cross-measure ranking
table(9, 1, 8, 5, [SUMM], "other",
      "We summarize some influential researchers in terms of all four measures in Table 7.",
      "Booktabs, three rules at 481.7, 498.8 and 587.6 pt spanning 391.8 pt, no vertical "
      "rule, centred, and the widest-counted grid after Table 9. Eight printed rows over "
      "five columns: Name, Rank of DC, Rank of EC, Rank of CC, Rank of BC, with one header "
      "band and seven researcher rows - only the seven names that place in all four "
      "rankings, not the ten the four single-measure tables print. Rank cells are "
      "right-aligned under centred headers, the name column is centred, and no column of "
      "integers can be decimal-aligned, so decimal_aligned is false. 391.8 pt against the "
      "418.3 pt measure (93.7 per cent). SOS, VERA TURAN prints EC rank 19 against 8, 5 and "
      "3 in the other three columns, the one row that breaks the caption's claim that the "
      "four measures 'give the same top influential researcher'. The detector reads the "
      "header words out of order and returns 'Name Rank of DC Rank of EC Rank of CC Rank "
      "of' as the region's inside text.",
      numeric=4, width="full",
      cap="Table 7: Most Influential Authors",
      mention=cited(9, 9, ["Table 7"], 1,
                    "We summarize some influential researchers in terms of all four "
                    "measures in Table 7."))

# ---------------------------------------------------------------- p10, the citation layout
figure(10, 1, "node-link-network",
       "Figure 2: Illustration for the Citation Network", "Figure N.",
       cited(10, 10, ["Figure 2"], 3,
             "Note that i → j in Figure 2 means cij = 1",
             pattern="as-shown-in"),
       [UNDIRECTED], "model", numbers=True, labels=True,
       note="Wide vector drawing, 428.6 by 139.4 pt, 132 drawing paths and 92 curves, with no "
            "frame, axis, tick, legend or title inside it. Sixteen nodes print as "
            "square-cornered rectangles on a pale yellow fill (1.000/1.000/0.698) with a "
            "blue-violet border (0.298/0.298/1.000) at 0.425 pt, holding black ArialMT text "
            "at 3.98 pt in the label form 'AuthorYear(Cite:n)': Snijders2011(33), "
            "Watts2007(680), Watts2002(835), Kleinberg2000(1246), Barabasi1999(18843), "
            "Watts1998(21688), Albert2002(13250), Newman2001(2)(2748), Newman2003(10616), "
            "Newman2001(1523), Valente1996(498), Borgatti2000(763), Bonacich1987(1956), "
            "Bollobas2001(5957), Erdos1959(4531) and Ahuja1993(9153). The labels are 150-dpi "
            "illegible one character at a time - the first pass misread nine of the sixteen "
            "citation counts - and were transcribed from a 600 dpi render of the same page, "
            "against which the text layer agrees on all sixteen strings. Thirty-two filled "
            "triangular arrowheads on gray strokes (0.496/0.496/0.496) at 0.212 pt, so every "
            "connector is directed; 28 of the 60 connector fragments carry cubic Bezier "
            "segments, so roughly half the edges arc. No label overlaps another label or any "
            "stroke, and the arrowheads touch box borders without covering glyphs. The text "
            "layer offers 'Matlab 2011a' as a caption above the region, which is the toolbox "
            "credit mid-paragraph, not a caption; the real caption prints under the drawing. "
            "Three by-number citations: two on p10 itself and one on p11 reading it as "
            "evidence that Table 8's papers are cited while Table 9's cite.")

# ---------------------------------------------------------------- p11, the two top-3 grids
table(11, 1, 4, 6, [UNDIRECTED], "model",
      "",
      "Booktabs, three rules at 140.2, 157.4 and 198.4 pt spanning 387.9 pt, no vertical "
      "rule, centred. Four printed rows over six columns - Rank, DC, EC, CC, BC, Citation - "
      "with three paper rows, one per measure, each cell giving the paper that measure "
      "ranks first, second and third. Rank right-aligned, the five name columns centred, no "
      "numeric column other than the rank, so decimal_aligned is false. 387.9 pt against "
      "the 418.3 pt measure (92.7 per cent). Cited four times, first on p10 a page before "
      "the grid in a sentence whose superscript 6 collides with the sentence's full stop in "
      "the text layer - 'Table 8 and Table 96 .' as printed - which is why the recorded "
      "quote is the p11 sentence instead.",
      numeric=1, width="full",
      cap="Table 8: Most Influential Papers Using Co-bibliography Relationship",
      mention=cited(10, 11, ["Table 8"], 4,
                    "Finally, according to Figure 2, papers in Table 8 tend to be cited by "
                    "others while those in Table 9 tend to cite others."))

table(11, 2, 4, 6, [UNDIRECTED], "model",
      "",
      "Booktabs, three rules at 232.2, 249.3 and 290.3 pt spanning 418.9 pt, no vertical "
      "rule. Four printed rows over the same six columns as Table 8, three paper rows "
      "again, and the grid the widest-counted in the paper: 418.9 pt against the 418.3 pt "
      "measure (100.1 per cent), flush to both margins - 0.4 pt wider than the running-head "
      "rule that defines the measure. Its caption prints between the two grids at y 210.8, "
      "so the p11 top rule belongs to Table 8 and the pair is read top to bottom. Same "
      "centred cells, same right-aligned rank column, decimal_aligned false. Three "
      "by-number citations, all of them naming it beside Table 8.",
      numeric=1, width="full",
      cap="Table 9: Most Influential Papers Using Co-citation Relationship",
      mention=cited(10, 11, ["Table 9"], 3,
                    "Finally, according to Figure 2, papers in Table 8 tend to be cited by "
                    "others while those in Table 9 tend to cite others."))

# ---------------------------------------------------------------- p12, the directed-graph grid
table(12, 1, 4, 5, [DIRECTED], "model",
      "We summarize the top-3 influential papers under these measures in Table 10.",
      "Booktabs, three rules at 461.4, 478.5 and 519.5 pt spanning 362.5 pt, no vertical "
      "rule, centred. Four printed rows over five columns: Rank, DC, EC, MKC(p = 1/2, "
      "b = 0.2), Citation. The MKC header is set as running text with the parameter values "
      "inside the cell, and the layer breaks it into '= 1/2, b', 'MKC(p' and '0.2)' in that "
      "order, which is why the detector reports the header as the bare token 'MKC()'; the "
      "crop resolves the cell as printed and that string is what is recorded. Three paper "
      "rows, one of them a compound - 'Erdos1959, etc.' in the DC column against 'Erdos1959' "
      "in the MKC column. 362.5 pt against the 418.3 pt measure (86.7 per cent). Cited "
      "twice on p12, the second time reading robustness off the near-identical paper "
      "titles.",
      numeric=1, width="full",
      cap="Table 10: Most Influential Papers Using Directed Graph",
      mention=cited(12, 12, ["Table 10"], 2,
                    "We summarize the top-3 influential papers under these measures in "
                    "Table 10."))

# ---------------------------------------------------------------- p13, top-5 singers
table(13, 1, 6, 5, [BASIC], "model",
      "We apply the four measures in Task 2 to this dataset, and the top-5 singers are "
      "listed in Table 11.",
      "Booktabs, three rules at 500.2, 517.3 and 582.2 pt spanning 344.7 pt, no vertical "
      "rule, centred on the page axis. Six printed rows over five columns: Rank, DC, EC, "
      "CC, BC, with five singer rows and every cell centred under its header - rank 1 "
      "Bibi Chou, DC Bibi Chou, EC Eason Chan, CC Bibi Chou, BC Jane Zhang. No numeric "
      "column but the rank, so decimal_aligned is false. 344.7 pt against the 418.3 pt "
      "measure (82.4 per cent), and exactly the width and geometry Table 13 repeats one "
      "page later. The graph behind it is 195 vertices and 4,929 edges as the prose states, "
      "which the grid gives no way to check. Caption 21.9 pt above the top rule at y 478.9, "
      "cited once by number in the sentence on the same page.",
      numeric=1, width="full",
      cap="Table 11: Top-5 Singers in 2011-2013 Using Basic Model",
      mention=cited(13, 13, ["Table 11"], 1,
                    "We apply the four measures in Task 2 to this dataset, and the top-5 "
                    "singers are listed in Table 11."))

# ---------------------------------------------------------------- p14, three grids
table(14, 1, 6, 5, [BASIC], "model",
      "",
      "Booktabs, three rules at 140.2, 157.4 and 222.3 pt spanning 320.2 pt, no vertical "
      "rule, centred. Six printed rows over five columns, Rank and the four measure "
      "columns, five movie actors from Bo Huang to Willian Feng ('Willian' is the paper's "
      "spelling). All cells centred. 320.2 pt against the 418.3 pt measure (76.5 per cent), "
      "and the same geometry Table 15 reprints a page later. Named once, on p13 in the "
      "sentence that finishes the basic-model paragraph, one page before the grid prints; "
      "no sentence on p14 or p15 names it.",
      numeric=1, width="full",
      cap="Table 12: Top-5 Movie Actors in 2011-2013 Using Basic Model",
      mention=cited(13, 14, ["Table 12"], 1,
                    "Then we obtain a graph with 453 vertices and 743 edges, and top-5 movie "
                    "actors are listed in Table 12."))

table(14, 2, 6, 5, [BIPARTITE], "model",
      "The ranking of top singers as well as songwriters are given in Table 13 and 14, "
      "respectively.",
      "Booktabs, three rules at 427.3, 444.4 and 509.3 pt spanning 344.7 pt, no vertical "
      "rule, centred. Six printed rows over five columns, the same skeleton as Table 11 and "
      "the identical rule span to the point: 344.7 pt against the 418.3 pt measure (82.4 "
      "per cent). The bipartite projection changes the answer rather than the layout - "
      "Bibi Chou leads DC here and Jane Zhang leads BC, against Bibi Chou and Jane Zhang "
      "leading the same two measures in Table 11 - which is the comparison the two grids "
      "exist to make and the prose does not draw. Caption at y 409.4, one printed header "
      "line, all cells centred, decimal_aligned false.",
      numeric=1, width="full",
      cap="Table 13: Top-5 Singers in 2011-2013 Using Bipartite Graph Model",
      mention=cited(14, 14, ["Table 13"], 1,
                    "The ranking of top singers as well as songwriters are given in Table "
                    "13 and 14, respectively."))

table(14, 3, 6, 5, [BIPARTITE], "model",
      "The ranking of top singers as well as songwriters are given in Table 13 and 14, "
      "respectively.",
      "Booktabs, three rules at 555.0, 572.1 and 637.1 pt spanning 318.0 pt, no vertical "
      "rule, centred. Six printed rows over five columns, the five songwriters behind the "
      "singers - Ruolong Yao, Albert Leung, Francis Lee, Qian Yao and Vincent Fang. 318.0 pt "
      "against the 418.3 pt measure (76.0 per cent). All cells centred, one header band, no "
      "fill, decimal_aligned false. Cited only inside the sentence that names Table 13 at "
      "the same time, and the grid itself prints under a caption 17.1 pt above the top "
      "rule. Below it, outside any grid, p14 carries footnote 8 in 9.4 pt type.",
      numeric=1, width="full",
      cap="Table 14: Top-5 Songwriters in 2011-2013 Using Bipartite Graph Model",
      mention=cited(14, 14, ["Table 14"], 1,
                    "The ranking of top singers as well as songwriters are given in Table "
                    "13 and 14, respectively."))

# ---------------------------------------------------------------- p15, the actor-film pair
table(15, 1, 6, 5, [BIPARTITE], "model",
      "",
      "Booktabs, three rules at 140.2, 157.4 and 222.3 pt spanning 320.2 pt, no vertical "
      "rule, centred - the same three coordinates and the same width as Table 12, printed a "
      "page apart, and the two grids differ only in their rows. Six printed rows over five "
      "columns, Rank, DC, EC, CC, BC. 320.2 pt against the 418.3 pt measure (76.5 per "
      "cent). Its caption is word for word the caption Table 16 prints 116 pt lower on the "
      "same page, so the column number is the only thing that tells the two grids apart on "
      "the printed page. Named once, on p14, one page early.",
      numeric=1, width="full",
      cap="Table 15: Top-5 Movie Actors in 2011-2013 Using Bipartite Graph Model",
      mention=cited(14, 15, ["Table 15"], 1,
                    "As for the results in the actor-film bipartite graph, we refer readers "
                    "to Table 15 and 16 below"))

table(15, 2, 6, 4, [BIPARTITE], "model",
      "",
      "Booktabs, three rules at 256.1, 273.2 and 338.1 pt spanning 398.2 pt, no vertical "
      "rule, centred. Six printed rows over FOUR columns, not five: the header prints Rank, "
      "EC, CC, BC and the DC column is absent outright - no empty cell, no blank header, no "
      "rule gap, EC simply begins where DC ended in the grid above. Footnote 8 on p14 "
      "explains why: 'there is no ranking result in terms of the degree centrality in Table "
      "16, for degrees of all films are 3 due to our specific selection strategy', every "
      "film having three actors by construction. Its rows list films rather than people, "
      "although the caption keeps saying 'Movie Actors' and is word for word Table 15's. "
      "398.2 pt against the 418.3 pt measure (95.2 per cent), the widest of the four artist "
      "grids and the only one that trades a column for width. Two by-number mentions, both "
      "on p14: the sentence that pairs it with Table 15, and footnote 8 itself.",
      numeric=1, width="full",
      cap="Table 16: Top-5 Movie Actors in 2011-2013 Using Bipartite Graph Model",
      mention=cited(14, 15, ["Table 16"], 2,
                    "As for the results in the actor-film bipartite graph, we refer readers "
                    "to Table 15 and 16 below",
                    trail="Note: there is no ranking result in terms of the degree "
                          "centrality in Table 16, for degrees of all films are 3"))

# ---------------------------------------------------------------- p16, the heuristic grid
table(16, 1, 11, 3, [TASK5], "other",
      "The simulation results are summarized in Table 17 and 18.",
      "Booktabs, three rules at 429.6, 446.8 and 571.5 pt spanning 303.8 pt, no vertical "
      "rule, centred. Eleven printed rows over three columns: Rank, Co-author's Name, "
      "Newcomer's Centrality, with ten ranked researchers from ALON, NOGA M. at 0.2605 down "
      "to FAUDREE, RALPH JASPER, JR. at 0.1617. Ranks right-aligned, names centred, "
      "centrality values all four decimals starting at the same ink edge; a column of "
      "equal-width values cannot be decimal-aligned and is recorded false. 303.8 pt against "
      "the 418.3 pt measure (72.6 per cent) - the only counted grid in the paper under the "
      "three-quarter line, and therefore the only one recorded half. The header prints the "
      "apostrophe as an acute accent in the text layer ('Co-author s Name') and the crop "
      "resolves the proper glyph. Cited once, on p16, in the sentence that also names "
      "Table 18.",
      numeric=2, width="half",
      cap="Table 17: Best Choices to Boost Eigenvector Centrality",
      mention=cited(16, 16, ["Table 17"], 1,
                    "The simulation results are summarized in Table 17 and 18."))


# ---------------------------------------------------------------- payload
RULES = [
    "rows counts every printed row including the header band, never the number of bands "
    "between rules: every counted grid in this paper prints one header band and its body, "
    "so Table 17's ten ranked researchers and its header are eleven rows over three rules "
    "[table.rows]",
    "every printed grid in this paper is booktabs: nineteen tables, three horizontal rules "
    "each, and not one vertical stroke in twenty pages, so rule_style is booktabs and zebra "
    "is false throughout [table.rule_style]",
    "a grid over 75 per cent of the local measure is full: twelve of the thirteen counted "
    "grids run 76.0 to 100.1 per cent of the 418.3 pt measure and Table 17 is the single "
    "exception at 72.6 per cent, recorded half, with each percentage named in its note "
    "[table.width]",
    "a column of equal-width values is not decimal alignment: the centrality columns of "
    "Tables 11 to 17 and the rank columns everywhere are set on one width and centred or "
    "right-aligned, so nothing is aligned on a point and decimal_aligned is false in every "
    "grid [table.decimal_aligned]",
    "a missing measure column is a column the grid does not print: Table 16 headers Rank, "
    "EC, CC and BC and records cols 4, because footnote 8 explains that degree centrality "
    "ranks nothing when every film has three actors [table.cols]",
    "a header cell that holds running text is one printed cell: Table 10's MKC column is "
    "headed 'MKC(p = 1/2, b = 0.2)' and the text layer scatters it into three fragments, so "
    "the crop is authoritative for the header string [table.header_rows]",
    "a note_sentence must be a printed sentence on the grid's own page or the next one, and "
    "a grid named only one page early keeps the field empty: Table 8's naming sentence "
    "prints on p10 and Tables 12 and 15 are named on p13 and p14 respectively, so all "
    "three leave note_sentence empty and the pointer goes into the item note "
    "[table.note_sentence]",
    "two grids that print one identical caption are recorded as printed: Table 15 and "
    "Table 16 carry the same caption word for word, and the column number is the only "
    "difference on the page [caption.verbatim]",
    "a caption line in the text layer is not a citation: Table 1 prints its number in its "
    "own caption and nowhere else, so count 0 with first_page null, exactly as Table 5 "
    "which is named only in its caption on p8 [mention.count]",
    "a citation that lands a page before the grid records lead_pages 1 and one on the same "
    "page records 0: Tables 3, 8, 9, 12, 15, 16 and 18 are all named a page early, Figure "
    "1 three times on p5 [mention.lead_pages]",
    "a drawing of markers joined by lines is node-link-network and not "
    "flowchart-or-schematic whether the art is a vector graph or a toolbox screenshot, so "
    "Figure 1's 3,950 vector paths and Figure 2's 132 paths and 92 curves share one family "
    "[geometry.family]",
    "printed_numbers records numerals the art carries of its own and data_labels records "
    "names set inside it: Figure 1 prints neither, Figure 2 prints both, since every node is "
    "a rounded rectangle holding 'AuthorYear(Cite:n)' [geometry.printed_numbers]",
]

NOTE = (
    "Fifteen measured regions over ten of twenty pages, all accounted for: fifteen rows - "
    "two figures and thirteen tables - no exclusions, no refusals, nothing unmeasured. The "
    "paper numbers nineteen tables and two figures, so six of the twenty-one printed "
    "exhibits have no region and are declared gaps rather than invented boxes: Table 3 on "
    "p6, Table 4 on p7, Table 5 on p8, Table 6 on p9, Table 18 on p17 and Table 19 on p18. "
    "All six are real booktabs grids - the drawing pass finds three ruled lines each, at "
    "464.9, 482.0 and 618.7 pt on p6, at 260.8, 277.9 and 402.6 pt on p7, at 140.2, 157.4 "
    "and 282.1 pt on p8, at 218.8, 235.9 and 360.6 pt on p9, at 140.2, 157.4 and 282.1 pt "
    "on p17 and at 137.6, 154.7 and 195.7 pt on p18 - and every one of them is lost to the "
    "same half-page threshold as paper 67's three ghosts: their rules span 233.2, 244.8, "
    "233.2, 252.7, 292.1 and 193.5 pt, which is 39.2, 41.1, 39.2, 42.4, 49.1 and 32.5 per "
    "cent of the 595.3 pt page width, against the 297.64 pt the detector requires. Table 18 "
    "misses by 5.5 pt, the closest call this lane has recorded. Their contents are on the "
    "record here anyway, read off the rendered pages: Tables 3, 4, 5 and 6 all print eleven "
    "rows over three columns - Rank, Name, Centrality - listing the ten researchers with "
    "the largest degree, eigenvector, closeness and betweenness centrality, the same ten "
    "names in four different orders; Table 18 prints the same eleven rows for the best "
    "co-author to add by closeness centrality, 0.020193 down to 0.020145, one page after "
    "Table 17 gives the eigenvector answer for the same question; and Table 19 prints four "
    "rows over five columns, 'Largest Deviation' plus DC, EC, CC and BC, with the three "
    "rows 0, 1, 2 and the counts 4, 8, 7, 3 / 3, 1, 3, 5 / 3, 1, 0, 2.\n\n"
    "One ruling register, nineteen times over. Every grid in the paper is three horizontal "
    "rules over one header band and a body, with no vertical rule anywhere, and every grid "
    "is centred on the page axis rather than set flush - which is why the widths run from "
    "72.6 to 100.1 per cent of the measure and why the six ghosts above were narrow enough "
    "to disappear. The counted widths in order of printing: 84.0, 87.2, 93.7, 92.7, 100.1, "
    "86.7, 82.4, 76.5, 82.4, 76.0, 76.5, 95.2 and 72.6 per cent.\n\n"
    "Defects recorded, not corrected. Tables 15 and 16 print one identical caption, "
    "'Top-5 Movie Actors in 2011-2013 Using Bipartite Graph Model', although Table 16's rows "
    "are films rather than actors and its DC column is missing altogether - the paper's own "
    "footnote 8 on p14 knows about the missing column and not about the caption. Table 2's "
    "prose reads 16 per cent of researchers off bins that give 88 of 511, which is 17.2 per "
    "cent. Table 7's caption and the paragraph above it claim the four measures 'give the "
    "same top influential researcher', which holds for rank 1 and fails immediately below "
    "it: SOS, VERA TURAN is 8th on DC, 19th on EC, 5th on CC and 3rd on BC, and the grid "
    "prints that row. Figure 2 draws sixteen papers, each labelled with its citation count, "
    "while the three grids built on the same citation network rank three papers per "
    "measure, and its labels are unreadable at 150 dpi - nine of the sixteen citation "
    "counts misread on the first pass - so they were transcribed from a 600 dpi render. "
    "Figure 1 draws "
    "directed arrowheads on a symmetric co-author relation. The detector's heading pass "
    "mistakes every rank column for a heading number, which is why the context dump carries "
    "'4 RODL, VOJTECH 43' and '6 TUZA, ZSOLT 40' as sections of the paper. The prose typos "
    "stand as printed: 'we count the degree of each vertices', 'The ranking of top singers "
    "as well as songwriters are given', and the footnote marker that collides with the "
    "full stop in 'Table 8 and Table 96 .'."
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

out = PROXY / "pc68-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
