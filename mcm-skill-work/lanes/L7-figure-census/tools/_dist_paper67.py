"""Hand census of P-C-2014-28747-f6ef544f (C-28747-Outstanding, 21 pages).

Eleven measured regions over nine pages, every one an exhibit: seven figures and four
tables. Two of the seven tables are printed but unmeasured and are declared gaps.

  p5  r1  (no caption) symbol list, booktabs, titled by the section heading
  p6  r2  Figure 1   co-author graph, 10 labelled discs
  p6  r1  Figure 2   the same graph with node 8 deleted, 7/9/10 ringed red
  p7  r2  Figure 3   node 2 deleted, one connected component
  p7  r1  Figure 4   node 4 deleted, two components and node 5 ringed red
  p9  r1  Table 1    top ten researchers by importance degree
  p12 r1  Table 3    fourteen researchers, three colour zones, header above the box
  p14 r1  Figure 5   citation network among papers
  p16 r1  Table 5    top ten movie stars
  p19 r1  Figure 6   two papers A and B with reciprocal arrows
  p20 r1  Figure 7   deviation degree against u

Not measured, declared in the note: Tables 2 (p11), 4 (p15) and 6 (p19). All three are
booktabs grids whose rules span 261.1, 221.8 and 266.5 pt - 43.9, 37.3 and 44.8 per cent
of the 595.3 pt page width, under the half-page threshold rule_table_regions applies to
candidate rules - so the geometry pass never sees them. The lane already carries this
as a known gap from paper 9.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2014-28747-f6ef544f"
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

SYMBOLS = "3 Symbol Description"
INFLUENCE = "4 The influence of researchers"
RESULT = "4.3 Result analysis: some interesting data"
CITING = "5.1 The citing network of papers"
EXTENSION = "6.1 Applying models to a specific area"
SENSITIVITY = "7.2 Sensitivity analysis of the citing network"

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


def slice_caption(page: int, start: str, stop: str) -> str:
    """Cut a caption out of the page text between its label and the next printed token.

    The three two-column caption blocks on pp. 6 and 7 interleave their left and right
    halves in the text layer, so those four captions are typed off the crop instead.
    """
    text = schema.page_text(PID, page)
    a = text.find(start)
    if a < 0:
        raise KeyError((page, start))
    b = text.find(stop, a)
    if b < 0:
        raise KeyError((page, start, stop))
    return text[a:b].strip()


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


# ---------------------------------------------------------------- p5, the symbol list
table(5, 1, 6, 2, [SYMBOLS], "symbols",
      "In the section, we use some symbols for constructing the model as follows.",
      "Booktabs, three rules at 184.8, 205.6 and 327.5 pt spanning 321.5 pt, no vertical "
      "rule anywhere, and the only counted grid in the paper with no caption: the band "
      "between the top rule and the header text is blank, so the table's only title is the "
      "section heading directly above it, '3 Symbol Description'. Six printed rows over two "
      "columns, Symbol and Description, and the five symbols are p, q, H, IF and E with the "
      "node index as a subscript. Three of the five descriptions wrap to two lines, which is "
      "why the body band runs 122 pt for five rows. 321.5 pt against the 418.3 pt measure "
      "(76.9 per cent), inset from both margins. Description is the only text column and the "
      "symbol column is centred display maths, so no column is decimal-aligned. The prose "
      "that introduces it is one sentence and never names a number, and the paper never "
      "changes that: the list is referred to nowhere after it prints.",
      numeric=0, width="full",
      mention=none_mention())

# ---------------------------------------------------------------- pp6-7, the co-author graph
FIG1 = "Figure 1: The diagram which describes the relation among 10 researchers"
FIG2 = "Figure 2: After deleting node 8, the connectivity of the graph has been destroyed."
FIG3 = "Figure 3: The condition of connection after deleting node 2."
FIG4 = "Figure 4: The condition of connection after deleting node 4 network."

figure(6, 2, "node-link-network", FIG1, "Figure N.",
       cited(5, 6, ["Figure 1"], 2,
             "To facilitate understanding and further analysis, we give the schematic dia- "
             "gram of the network model , shown in Figure 1."),
       [INFLUENCE], "other", numbers=True,
       source="typed-from-crop", labels=False,
       note="raster, one 514 by 404 px bitmap 141.7 by 111.4 pt: ten empty circles with "
            "green rings, the numerals 1 to 10 set black at their centres, joined by eleven "
            "plain thick black segments with no arrowheads, no edge labels, no weights, no "
            "legend, no frame and no axes. The layout is a three-tier ladder - 6 alone on "
            "top, the chain 1-2-3-4-5 across the middle, 7-8-9-10 hanging under 8 - so the "
            "graph is undirected and node 8 is its hub with four incident edges (4-8, 8-7, "
            "8-9, 8-10). The caption is the left half of a two-column caption block printed "
            "under both panels and interleaved with Figure 2's left half in the text layer, "
            "so it is typed off the crop rather than cut from the layer. Cited twice by "
            "number, first on p5 one page before the art and again on p6 as 'In Figure 1, "
            "node 8 has the most node degree, or k8 = 4.'")

figure(6, 1, "node-link-network", FIG2, "Figure N.",
       cited(6, 6, ["Figure 2"], 1,
             "If delete it, as shown in Figure 2 , node7,9 and 10 become isolated, the "
             "connectivity of the network are badly affected."),
       [INFLUENCE], "other", numbers=True,
       source="typed-from-crop", labels=False,
       note="raster, the same 513 by 405 px drawing one column to the right with node 8 "
            "removed: nine circles labelled 1 to 7, 9 and 10, its four edges gone, and the "
            "seven left edges (6-1, 6-2, 6-3, 1-2, 2-3, 3-4, 4-5) keeping one component "
            "while 7, 9 and 10 sit alone. The three orphans are drawn with RED rings and "
            "every connected node keeps a green one, so the colour is doing the work the "
            "caption only describes, and no legend explains it. The prose claim on p6 - "
            "'node7,9 and 10 become isolated' - is exactly what the art prints. No arrows, "
            "no weights, no frame, no axes. Second half of the p6 caption block, again "
            "interleaved with Figure 1's half in the text layer.")

figure(7, 2, "node-link-network", FIG3, "Figure N.",
       cited(6, 7, ["Figure 3"], 2,
             "We analyze it in the following, as is shown in Figure 3 and 4 shown:"),
       [INFLUENCE], "other", numbers=True,
       source="typed-from-crop", labels=False,
       note="raster, 515 by 404 px, the pair's left panel: node 2 deleted and nine circles "
            "left (1, 3, 4, 5, 6, 7, 8, 9, 10) joined by eight edges into ONE connected "
            "component - 1-6, 6-3, 3-4, 4-5, 4-8, 8-7, 8-9, 8-10 - so deleting a degree-3 "
            "node off the ladder leaves the graph whole, which is the contrast the next "
            "panel is printed to make. All nine rings green, nothing isolated, no arrows, "
            "no weights, no frame. Caption printed under the left column and so again "
            "interleaved with Figure 4's half in the layer.")

figure(7, 1, "node-link-network", FIG4, "Figure N.",
       cited(6, 7, ["Figure 4"], 2,
             "We analyze it in the following, as is shown in Figure 3 and 4 shown:"),
       [INFLUENCE], "other", numbers=True,
       source="typed-from-crop", labels=False,
       note="raster, 512 by 404 px, right panel of the same row: node 4 deleted and the "
            "graph falls into TWO components - the near-clique 1, 2, 3, 6 (1-6, 1-2, 2-6, "
            "2-3, 6-3) and the star 7-8-9-10 under hub 8 - while node 5, red-ringed, is "
            "left with no incident edge at all. Nine circles labelled 1, 2, 3, 5, 6, 7, 8, "
            "9, 10. The prose pairs the two panels as 'node 2 and 4 have the same "
            "quantities of degree' and reads their triangles as equal, but the drawings do "
            "not agree: the panel on this page loses a whole component and the p7 left "
            "panel loses nothing. The caption as printed ends with the stray word "
            "'network' - 'after deleting node 4 network.' - and that is recorded as "
            "printed.")

# ---------------------------------------------------------------- p9, Table 1
table(9, 1, 11, 5, [INFLUENCE], "other",
      "we get the qi of 511 researchers and list the top ten researchers as shown in Table 1.",
      "Booktabs, three rules at 214.6, 235.3 and 385.9 pt spanning 389.7 pt, no vertical "
      "rule and no box, one hairline midrule under the header. Eleven printed rows and five "
      "columns: Rank, Name, q, Cooperation Year, Times, with the q set in italic maths. The "
      "only text column is Name; Rank and Times are right-aligned integers and q is a column "
      "of 0.xxxx values all of one width, so decimal alignment is not assessable anywhere "
      "and is recorded false. 389.7 "
      "pt against the 418.3 pt measure (93.2 per cent) but indented about 14 pt from each "
      "margin rather than set flush, which is why the caption is indented with it. Rank 2 "
      "carries an asterisk after the surname ('HARARY, FRANK*') and the paper prints no "
      "footnote to say what it means. The caption prints the index as a bare italic qi with "
      "the i subscript flattened into the line.",
      numeric=4, width="full",
      cap=slice_caption(9, "Table 1: The ranking", " Rank"),
      mention=cited(9, 9, ["Table 1"], 2,
                    "we get the qi of 511 researchers and list the top ten researchers as "
                    "shown in Table 1.", pattern="as-shown-in"))

# ---------------------------------------------------------------- p12, Table 3
table(12, 1, 15, 6, [RESULT], "result",
      "",
      "Booktabs with five horizontal rules and no vertical stroke anywhere: 142.9 pt above "
      "the header, 192.4 pt under it, 271.1 and 349.7 pt between the body and 414.0 pt at "
      "the foot, every one spanning 346.9 pt. Fifteen printed rows - a two-line header and "
      "fourteen researchers - over six columns: Name, q rank, p rank, p-q, Year, times, "
      "with the two rank words stacked one above the other under their italic letters. The "
      "measured box begins at the 192.4 pt midrule, so the top rule and the header row "
      "print ABOVE it and only the fourteen data rows sit inside the region; the count of "
      "fifteen is the grid's, not the box's. The four rules below the header do not rule "
      "rows: they bound three COLOUR ZONES of five, five and four rows, and the shading "
      "fills only the Name cell of each row - pale yellow (0.980, 0.855, 0.553) for the "
      "stable quintet, light green (0.682, 0.867, 0.506) for the five who improve most and "
      "a pale teal (0.537, 0.745, 0.698) for the four who lose ground. The prose calls the "
      "third zone red and there is no red pixel anywhere in the table. 346.9 pt against the "
      "418.3 pt measure (82.9 per cent). Five numeric columns, all integers and LEFT-"
      "aligned, so -132 and 351 and 1 all start at the same ink edge and nothing is decimal-"
      "aligned; the names carry an asterisk on MAXSEIN only. The sentence that names it - "
      "'we show it in Table 3' - "
      "prints on p11, one page early and outside the two-page window a note_sentence may "
      "quote, so the field is empty.",
      numeric=5, width="full",
      cap=slice_caption(12, "Table 3: The schematic", " q p Name"),
      mention=cited(11, 12, ["Table 3"], 1,
                    "However, analyzing the remaining data, we find some interesting "
                    "phenomenon,we show it in Table 3"))

# ---------------------------------------------------------------- p14, Figure 5
figure(14, 1, "node-link-network",
       slice_caption(14, "Figure 5: The citation", " Set the adjacency"), "Figure N.",
       cited(13, 14, ["Figure 5"], 1,
             "we assume that the effects of interaction of two papers exist citing relation "
             "are equal), shown in the Figure 5."),
       [CITING], "other", numbers=True,
       note="raster, one 430 by 422 px bitmap 170.1 by 166.9 pt centred on the 418.3 pt "
            "measure, a circular layout of fifteen papers labelled 1 to 15: green-outlined "
            "circles with white fill and black numerals, except nodes 5 and 15 which are tiny "
            "solid green discs with their numerals set outside the marker. DIRECTED - every "
            "edge ends in a small solid black arrowhead at its head node, with a fan of "
            "arrows leaving 10 and several converging on 4 - so this is the directed half of "
            "the paper's argument and not a repeat of the co-author graphs on pp. 6 and 7, "
            "which carry no arrowheads at all. No edge weights, no colour or thickness "
            "variation, no legend, no axes, no frame, no title inside the art. Marker "
            "diameters vary by a factor of ten or more, with 10 the largest at about 31 pt "
            "across and 1 at about 21 pt, which reads as a degree or influence encoding the "
            "drawing never keys. The art covers 40.7 per cent of the local measure, the "
            "narrowest exhibit in the paper.")

# ---------------------------------------------------------------- p16, Table 5
table(16, 1, 11, 5, [EXTENSION], "model",
      "Analyzing the Table 5, we can find out that the box-office indicating the actors "
      "strength has some contribution",
      "Booktabs, three rules at 535.9, 556.6 and 707.2 pt spanning 343.9 pt, no vertical "
      "rule. Eleven printed rows and five columns - rank, degrees, Name, influence degree, "
      "box-office - with four numeric columns, every one of them CENTRED under a centred "
      "header rather than right- or decimal-aligned, so '10' sits centred under 'rank'; the "
      "two score columns are 0.xxxx throughout and line up at both ends only because every "
      "value is the same width. Name is the single text column and its header is centred "
      "35 pt to the right of where its left-aligned names start. 343.9 pt against the "
      "418.3 pt measure (82.2 per cent). The closing rule at 707.2 pt prints 4.0 pt BELOW the bottom "
      "of the measured region at 703.2 pt, the same shortfall the lane recorded on paper "
      "64: the box the geometry pass returns stops just above the foot rule, so the grid's "
      "last hairline sits outside the region while every row stays inside it. The caption "
      "calls the ranks 'the movie starts'.",
      numeric=4, width="full",
      cap=slice_caption(16, "Table 5: The indexes", " rank degrees"),
      mention=cited(17, 16, ["Table 5"], 2,
                    "Analyzing the Table 5, we can find out that the box-office indicating "
                    "the actors strength has some contribution", pattern="direct"))

# ---------------------------------------------------------------- pp19-20, the sensitivity pair
figure(19, 1, "node-link-network",
       slice_caption(19, "Figure 6: The schematic", " Similarity,"), "Figure N.",
       none_mention(), [SENSITIVITY], "sensitivity", numbers=True, labels=True,
       note="raster, one 540 by 266 px bitmap 170.1 by 83.8 pt: two white ellipses with "
            "green outlines sitting side by side, a bold serif A in the left one and a bold "
            "serif B in the right, joined by a PAIR of opposite-facing arrows - red from A "
            "to B above, cyan from B to A below - each carrying a small numeral: the upper "
            "one reads 1, the lower reads 1 followed by a glyph the print renders as a "
            "question mark. The prose fixes what those two should be - the paper A cites B "
            "with impact ratio u, 'we set the impact ratio of B to A and A to B as u' - but "
            "the artwork prints no u anywhere, so the lower label is illegible as printed. "
            "Two labelled nodes with reciprocal directed edges and no frame, no axes and no "
            "legend. Never cited by number: the caption is the only prose that names it, and "
            "the paragraph after it talks about E and u without pointing back.")

figure(20, 1, "line",
       slice_caption(20, "Figure 7: The changing", " For a evaluation"), "Figure N.",
       cited(20, 20, ["Figure 7"], 1,
             "The following Figure 7 reflects the E along with the changes of the u.",
             pattern="direct"),
       [SENSITIVITY], "sensitivity", numbers=True,
       note="raster, one 561 by 413 px bitmap 170.1 by 125.2 pt: a single dark-blue "
            "dash-dot-dot polyline with no markers, one panel, no legend, no gridlines and "
            "no title inside the plot. The frame is L-shaped on the bottom and RIGHT, an "
            "unusual corner: one baseline at the foot spanning 231 to 367 pt and one vertical "
            "at x 367 pt running up the right edge, with no left axis line and no top rule. "
            "The y ticks run 0, 0.5, 1, 1.5, 2, 2.5 and 3 and the x ticks 0.1 to 0.9 in "
            "steps of 0.1, with the leftmost label clipped and the 2.5 label smudged. Neither "
            "axis carries a printed title, so the prose has to name them E and u. The curve "
            "sits near 2.7 for u below 0.4, drops to 0.3 at 0.45 and 0.1 at 0.5, spikes back "
            "to 2.7 at 0.6 and is flat on the axis from 0.7 out. The prose reads stability "
            "off it: 'when u gets in the interval of [0.7,1] the variation of the results is "
            "relatively small', which the drawn range 0.1 to 0.9 does not contain.")


# ---------------------------------------------------------------- payload
RULES = [
    "rows counts every printed row including the header band, and never the number of "
    "bands between rules: Table 3's five rules bound three colour zones of five, five and "
    "four rows, so its four body bands and its fifteen printed rows are different numbers "
    "[table.rows]",
    "a header that prints outside the measured box is still the grid's header: Table 3's "
    "two-line header sits between the 142.9 pt toprule and the 192.4 pt midrule, above the "
    "region the geometry pass returns, and is counted as one header row all the same "
    "[table.header_rows]",
    "a two-line header band is one header row, not two: 'q' over 'rank' and 'p' over 'rank' "
    "are five columns' worth of labels set on two lines [table.header_rows]",
    "every printed grid in this paper is booktabs: seven grids, three horizontal hairlines "
    "each, no vertical rule anywhere in twenty-one pages, so rule_style is booktabs and "
    "zebra is false throughout [table.rule_style]",
    "a fill behind one cell is not zebra striping: Table 3 shades only the Name cell of "
    "each row, in three colour zones that mark the prose's stable, positive and negative "
    "bands [table.zebra]",
    "a grid over 75 per cent of the local measure is full: the four counted grids run 76.9, "
    "82.2, 82.9 and 93.2 per cent of the 418.3 pt measure and each percentage is named in "
    "its note [table.width]",
    "a column of equal-width values is not decimal alignment: Table 1's q column is 0.xxxx "
    "eleven times and Table 5's two score columns are 0.xxxx ten times each, so nothing is "
    "aligned on a point and decimal_aligned is false in all four grids [table.decimal_aligned]",
    "a note_sentence must be a printed sentence on the grid's own page or the next one; "
    "Table 3's only naming sentence, 'we show it in Table 3', prints on p11 and so the "
    "field is empty and the pointer goes into the item note [table.note_sentence]",
    "an uncaptioned table records numbering none and an empty verbatim: p5's symbol list "
    "prints a header band and no caption line at all, its title being the section heading "
    "above it [caption.numbering]",
    "a two-column caption block interleaved in the text layer is typed off the crop: the "
    "four captions on pp. 6 and 7 print in two halves side by side and the layer reads them "
    "alternately, so caption_source is typed-from-crop and the caption quote is skipped "
    "[caption.verbatim]",
    "printed_numbers records numerals the art carries of its own - node ids on the six "
    "network panels and tick labels on the case-extension chart - and data_labels records "
    "names set inside the art, which only Figure 6's A and B do [geometry.printed_numbers]",
    "an exhibit the prose never numbers by name keeps count 0 with first_page null: Figure "
    "6 and the p5 symbol list print a caption or a title and are pointed at nowhere "
    "[mention.count]",
    "a citation that lands a page BEFORE the exhibit keeps its first page and records "
    "lead_pages 1, and one that lands after it records a negative lead: Figure 1 is first "
    "named on p5, Table 5 only on p17 [mention.lead_pages]",
    "a bitmap that prints labelled discs joined by arrows is node-link-network and not "
    "flowchart-or-schematic, whether the edges carry arrowheads or not, so all six graphs "
    "here share one family [geometry.family]",
]

NOTE = (
    "Eleven measured regions over nine of twenty-one pages, all accounted for: eleven rows - "
    "seven figures and four tables - no exclusions, no refusals, nothing unmeasured. The "
    "paper numbers seven figures and six tables, so three of the thirteen printed exhibits "
    "have no region and are declared gaps rather than invented boxes: Table 2 on p11, Table "
    "4 on p15 and Table 6 on p19. All three are real booktabs grids - the drawing pass finds "
    "three ruled lines each, at 251.8, 272.5 and 423.1 pt over x 167.1 to 428.2 pt on p11, "
    "at 393.0, 411.1 and 477.0 pt over x 186.8 to 408.5 pt on p15 and at 142.9, 163.6 and "
    "213.1 pt over x 164.4 to 430.9 pt on p19 - and they are lost because each set of rules "
    "spans only 261.1, 221.8 and 266.5 pt, between 37 and 45 per cent of the page width, "
    "while rule_table_regions collects a candidate rule only when it spans at least half the "
    "page. That is the same half-page threshold that made Table 6 of paper 9 a declared gap. "
    "Their contents are on the record here anyway: Table 2 lists ranks 1 to 10 of the "
    "influence ranking over Rank, Name and p; Table 4 lists the top five papers over rank, "
    "Paper's number, H, IF and r; Table 6 lists three researchers over Name, E and q.\n\n"
    "One ruling register, seven times over, and one grid that breaks it. Every printed grid "
    "in the paper is booktabs - horizontal hairlines only, no vertical stroke anywhere in "
    "twenty-one pages - at 76.9, 82.2, 82.9 and 93.2 per cent of the 418.3 pt measure for "
    "the four counted grids. Table 3 is the exception in every other respect: its five rules "
    "bound three COLOUR ZONES of five, five and four rows rather than ruling rows, its "
    "header prints above the measured box, its shading fills only the Name cell of each row, "
    "and its four numeric columns are left-aligned so that 1 and 362 and -132 all start at "
    "the same ink edge. Table 1 is indented 14 pt from both margins, which is why its "
    "caption is indented with it, and Table 5 is centred column by column with its Name "
    "header 35 pt to the right of where its names start.\n\n"
    "Defects recorded, not corrected: the prose beside Table 3 defines a red zone for the "
    "four researchers whose p-q goes negative, and the drawn third band is a pale teal with "
    "no red pixel anywhere in the table; Figure 7 is drawn over u from 0.1 to 0.9 while the "
    "paragraph beside it reads stability off 'the interval of [0.7,1]', which the plot does "
    "not cover; Figure 4's caption ends with the stray word 'network'; Figure 6's lower "
    "arrow is labelled 1 followed by a glyph that prints as a question mark where the prose "
    "requires u; Figure 4 leaves the graph in two components and an isolated node 5 while "
    "Figure 3 leaves it in one, although the prose pairs the two as equal; Table 5's fifth "
    "column is headed 'box-office' with no unit and its caption calls the ranks 'the movie "
    "starts'; Table 1's rank 2 carries an asterisk no footnote explains; and Figures 2 and 4 "
    "use red rings to mark the isolated nodes with no legend anywhere in the paper. The "
    "prose typos stand as printed: 'The researcher is importance degree in the net-work', "
    "'It is unquestionable that the feedback of citing is subsistent', 'Similarity, we "
    "define E as the index', 'we find some interesting phenomenon,we show it in Table 3' "
    "with no space after the comma, and the paragraph on p16 that repeats 'we decide to "
    "replace the Erdos in the previous network model with him' twice."
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

out = PROXY / "pc67-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
