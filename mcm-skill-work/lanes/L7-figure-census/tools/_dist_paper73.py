"""Hand census of P-A-2015-35532-1a9fa997 (Team 35532, 34 pages, 59 measured regions).

Every exhibit in this paper is pasted as a bitmap and then framed by vector rules, so the
measurer reports a vector container next to the raster it wraps. Where the container holds
one figure the container is the row; where it holds several separately numbered figures
(p8, three plots in three boxes) the individual bitmaps are the rows and the container is
excluded as the band that carries the caption strips.

   p1  r1  three clipped summary lines                        excluded not-an-exhibit
   p2  r1  symbol list (1), header + 7 rows, grey zebra
   p3  r1  same list, 9 more rows, header not repeated
   p3  r2  symbol list (2) for model II, 12 rows
   p4  r1  same list, 8 more rows
   p4  r2  symbol list (3) for model III, 10 rows
   p5  r1  Fig.1   the four-box SEIR cartoon
   p5  r2  the bitmap inside Fig.1                          excluded fragment-of-other
   p6  r1  Table 1  parameters, header + first row only
   p7  r1  the other four rows of Table 1                    excluded split-across-pages
   p8  r1  three border boxes and three caption strips        excluded caption-background
   p8  r2  Fig.2.1  Guinea, deaths against simulation
   p8  r3  Fig.2.2  Liberia
   p8  r4  Fig.2.3  Sierra Leone
   p9  r1  Fig.3   the SEIIR cartoon
   p9  r2  the bitmap inside Fig.3                          excluded fragment-of-other
   p11 r1  Fig.4   two panels, deaths and uncontrolled cases
   p11 r2/r3  the two panel bitmaps                          excluded fragment-of-other
   p12 r1  Fig.5   two panels, with and without the drug
   p12 r2/r3  the two panel bitmaps                          excluded fragment-of-other
   p14 r1  Fig.6   the twelve districts of Sierra Leone
   p14 r2  the map bitmap                                    excluded fragment-of-other
   p14 r3  the caption strip                                 excluded fragment-of-other
   p14 r4  Table 2  the distance matrix, caption band and first row
   p15 r1  the twelve remaining rows of Table 2              excluded split-across-pages
   p15 r2  Table.3  thirteen districts, three blocks of two
   p16 r1  Fig.7   the seven medical centres
   p16 r2  prose and one display equation                    excluded not-an-exhibit
   p17 r1  TOPSIS prose, three collapsed equations           excluded not-an-exhibit
   p18 r1  prose and F_n                                     excluded not-an-exhibit
   p18 r2  prose and K                                       excluded not-an-exhibit
   p19 r1  TOPSIS steps, matrices and separations            excluded not-an-exhibit
   p20 r1  the four TOPSIS steps, equations                  excluded not-an-exhibit
   p20 r2  Table4   the district data, 12 of 13 rows
   p21 r1  the thirteenth row, its note, prose and a heading  excluded split-across-pages
   p22 r1  Table 5  the three countries, and Table 6 under it
   p26 r1  Fig.8   drug output over time
   p26 r2  the plot bitmap                                   excluded fragment-of-other
   p27 r1  Table 7  initial populations
   p27 r2  two plots above two grids, uncaptioned            one composite row
   p27 r3/r4  the two plot bitmaps                           excluded fragment-of-other
   p28 r1  four plots and four grids, uncaptioned            one composite row
   p28 r2-r5  the four plot bitmaps                          excluded fragment-of-other
   p29 r1  prose and one display equation                    excluded not-an-exhibit
   p29 r2  Table 8  the three factors, header and first row
   p30 r1  the other five rows of Table 8                    excluded split-across-pages
   p30 r2  Fig.9   deaths against beta
   p30 r3  Fig.10  deaths against E0
   p30 r4/r5  the plot bitmap and its caption strip          excluded fragment-of-other
   p31 r1  prose closing the E0 sensitivity                 excluded not-an-exhibit
   p31 r2  Table 9  days against output
   p32 r1  Fig.11  control time against daily output

Fifteen figure rows, thirteen table rows, thirty-one exclusions, nothing unresolved.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2015-35532-1a9fa997"
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

# 595.32 x 841.92 pt page, text block x 90.0 to 505.4
MEASURE = 415.4
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


def qtail(page: int, marker: str, nwords: int) -> str:
    """Quote the nwords words that end at a printed marker - the sentence may be too long."""
    text = schema.page_text(PID, page)
    end = text.find(marker)
    if end < 0:
        raise KeyError((page, marker))
    end += len(marker)
    start = end
    seen = 0
    while start > 0 and seen < nwords:
        start -= 1
        if text[start].isspace() and text[start + 1:start + 2] not in ("", " "):
            seen += 1
    return schema.norm(text[start:end].strip())


def cap(page: int, prefix: str, tail: str) -> str:
    """Take the caption verbatim out of the layer: from its number to its last printed word."""
    text = schema.page_text(PID, page)
    start = text.find(prefix)
    if start < 0:
        raise KeyError((page, prefix))
    end = text.find(tail, start)
    if end < 0:
        raise KeyError((page, tail))
    return schema.norm(text[start:end + len(tail)])


def pct(span: float) -> str:
    return f"{span / MEASURE * 100:.1f}"


def place(page: int, reg: int, kind: str, path: list[str], numbered: bool = True) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
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
    pages = sorted({page - 1, page, page + 1, first_page - 1, first_page, first_page + 1})
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": qp(lead, pages) if lead else "",
            "trail_sentence": qp(trail, pages) if trail else "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": gap}


def caption(verbatim: str, numbering: str = "none", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           three_d: str = "no", source: str = "text-layer", numbered: bool = True,
           position: str = "below", note: str = "", other_note: str = "",
           shared_axes: bool = False, confidence: str = "high") -> None:
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": confidence,
        "other_note": other_note,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, kind, path, numbered),
        "mention": mention,
        "caption": caption(cap_text, numbering, position),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, rows: int, cols: int, kind: str, path: list[str],
          note_sentence: str, note: str, *, rule: str = "booktabs", numeric: int = 1,
          header_rows: int = 1, numbered: bool = True, width: str = "full",
          zebra: bool = False, merged: bool = False, decimal: bool = False,
          diagonal: bool = False, continued: bool = False, cap_text: str = "",
          numbering: str = "Table N:", position: str = "below",
          mention: dict | None = None, source: str = "text-layer") -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": source if cap_text else "none",
        "note": note,
        "place": place(page, reg, kind, path, numbered),
        "mention": mention or none_mention(),
        "caption": caption(cap_text, numbering if cap_text else "none", position),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued,
                  "note_sentence": qp(note_sentence, [page - 1, page, page + 1]) if note_sentence else ""},
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "reason": reason,
        "note": note,
    })


# ---------------------------------------------------------------- section paths
SEC_SUMMARY = ["Summary"]
SEC_INTRO = ["Introduction"]
SEC_MODEL1 = ["Model I"]
SEC_MODEL2 = ["Model II"]
SEC_EVAL = ["1 Specify evaluation norms"]
SEC_DATA = ["2 Collect data"]
SEC_RESULTS = ["Results & analysis"]
SEC_SENS = ["Sensitivity Analysis"]

# ---------------------------------------------------------------- symbol lists, p2-p4
excluded(1, 1, "not-an-exhibit",
         "The last two lines of the abstract, cut off after 'and death cases decreases with the "
         "decrease of the minimum daily output of drugs'; the only drawn marks are the two "
         "fraction/bracket strokes inside the clipped sentence. Not an exhibit.")
table(2, 1, 7, 2, "symbols", SEC_INTRO, "", (
    "The list has no number and no caption; its only title is the heading 'Symbols and "
    "definitions' at the foot of p2. Header 'Symbol | definitions', seven rows S through D, "
    "a rule under the header and one at the bottom, a single internal vertical rule after the "
    "symbol column, and alternating grey shading; left and right stay open. It is the first "
    "slice of one list that runs unrepeatedly over three pages."),
    rule="vertical-rules", numeric=0, zebra=True, continued=True)
table(3, 1, 9, 2, "symbols", SEC_INTRO, "", (
    "Second slice of the same symbol list: nine rows from N to G(t), header not repeated, so "
    "the reader has to turn back to p2 for the column titles. Same vertical rule and grey "
    "zebra; the mu definition wraps onto a second line."),
    rule="vertical-rules", numeric=0, zebra=True, continued=True)
table(3, 2, 12, 2, "symbols", SEC_INTRO, "", (
    "Third slice, opened by the clipped sub-caption '(2)Symbol for model II' (the text layer "
    "reads 'ymbol for model II'). Header repeated, twelve rows, same single vertical rule and "
    "grey zebra. The distance definition drops its leading t and reads 'he shortest distance "
    "between', r_n and m_n carry stray semicolons, and I_n's definition stops mid-sentence."),
    rule="vertical-rules", numeric=0, zebra=True, continued=True)
table(4, 1, 8, 2, "symbols", SEC_INTRO, "", (
    "Fourth slice: eight rows, header not repeated, same vertical rule and zebra. The open "
    "degree row is defined twice - F_n and then C_n repeating F_n's own wording - and J_n ends "
    "with a stray 'i'."),
    rule="vertical-rules", numeric=0, zebra=True, continued=True)
table(4, 2, 10, 2, "symbols", SEC_INTRO, "", (
    "Last slice, under the clipped sub-caption '(3)Symbol for model III'. Header repeated, ten "
    "rows, this one closing the list. t_n and the isolated-infectious row wrap onto second "
    "lines, which is why three wrapped definitions in a row read as six short rows."),
    rule="vertical-rules", numeric=0, zebra=True)

# ---------------------------------------------------------------- figures, model I
figure(5, 1, "flowchart-or-schematic", cap(5, "Fig.1", "model"),
       "Fig. N", cited(5, 5, ["Fig.1"], 1, "Fig.1 shows the process."),
       "model", SEC_MODEL1, numbers=False, labels=False, note=(
           "Four blue boxes S, E, I and R in a row, joined by three arrows labelled beta I / N, "
           "sigma and (1-f)gamma. The prose says an infectious individual 'either recover and "
           "survive R or die D' and then draws the figure with no D compartment at all, so the "
           "cartoon and the system of equations below it disagree. The caption prints inside "
           "the border box, under the boxes, with no space after 'Fig.1'."))
excluded(5, 2, "fragment-of-other",
         "The pasted bitmap of the four blue boxes and their arrows; the border box, the three "
         "edge labels and the caption are vector, so the exhibit is recorded on the container "
         "p5 r1 and this is its inner raster.")
table(6, 1, 5, 4, "model", SEC_MODEL1,
      "All important parameters’ value are listed in Table 1.",
      ("Header Parameter / Guinea / Sierra Leone / Liberia, a rule above, a heavy rule under "
       "the header, a rule at the bottom and one internal vertical rule after the parameter "
       "column; no closed frame. Only the first of the five body rows - 1/sigma, 5.3 5.3 5.3 - "
       "prints on this page; the other four, including the row of onset dates, sit on p7 under "
       "the running head, and the split carries no continuation mark."),
      rule="vertical-rules", numeric=3, continued=True,
      cap_text="Table 1. Parameter estimates for the 2014 EBOV outbreak",
      numbering="Table N.", position="above",
      mention=cited(6, 6, ["Table 1"], 1,
                    "All important parameters’ value are listed in Table 1."))
excluded(7, 1, "split-across-pages",
         "The last four body rows of Table 1 - 1/gamma, the transmission rate, the case fatality "
         "rate and the date of the first infectious case - printed at the top of p7 with the "
         "header not repeated and no continuation mark. The table is recorded once, on p6 r1.")
excluded(8, 1, "caption-background",
         "The vector band that carries the three border boxes and the three white caption "
         "strips of Figs 2.1 to 2.3. Its box reaches the page-wide header rule at y=65.5, which "
         "is why one region spans all three figures instead of one region per figure; the three "
         "plots themselves are the rasters below it.")
for _reg, _suffix in ((2, "Guinea"), (3, "Liberia"), (4, "Sierra Leone")):
    figure(8, _reg, "line",
           qp(f"Fig.2.{_reg - 1}the early EBOV transmission period of {_suffix}", [8]),
           "Fig. N", none_mention(), "model", SEC_MODEL1, legend="inside", numbers=True,
           note=(
               "One panel: reported deaths as dots labelled 'Deaths vs. t' against a blue line "
               "labelled 'Simulation', legend inside the top right of the axes, dotted grid, "
               "x axis t and y axis Deaths. The caption is a pasted strip under the plot with no "
               "space after the figure number, and it prints inside the border box. The three "
               "panels carry no individual prose citation - the paper names the group once, as "
               "'(shown in Fig.2)' on p7, and the shared caption 'Fig 2. Dynamics of 2014 EBOV "
               "outbreaks in Guinea, Sierra Leone and Liberia.' prints under the third."))

# ---------------------------------------------------------------- figures, model I continued
figure(9, 1, "flowchart-or-schematic", "Fig.3 the process of the SEIIR model", "Fig. N",
       cited(9, 9, ["Fig.3"], 1, "Fig.3 shows the process."),
       "model", SEC_MODEL1, numbers=False, note=(
           "Five blue boxes S, E, I_free, I_q and R. E splits into I_free and I_q, and both feed "
           "R; the five edge labels are beta I_free / N, sigma, mu, 1-mu, f1 and f2. Bitmapped "
           "box letters sit next to vector edge labels and the bitmap is visibly ragged against "
           "them. Caption inside the border box, below the art."))
excluded(9, 2, "fragment-of-other",
         "The pasted bitmap of the five boxes inside Fig.3's border box; recorded on the "
         "container p9 r1.")
figure(11, 1, "line", "Fig.4 the result of SEIIR model", "Fig. N",
       cited(10, 11, ["Fig.4"], 1, "The results shows in Fig.4."),
       "model", SEC_MODEL1, panels=2, layout="1x2", legend="inside", numbers=True, note=(
           "Two boxed panels side by side, both against time in days from 100 to 150. Left: "
           "death cases up to about 14 x 10^4, a blue curve rising and a green one flattening. "
           "Right: uncontrolled infected individuals up to 2.5 x 10^4. Each panel keeps its own "
           "legend inside the top right, and in both the legend sits over the curve it labels; "
           "the tick labels are blurred bitmap, and the right panel's legend is so pale it "
           "almost disappears. Caption below, inside the border box."))
excluded(11, 2, "fragment-of-other",
         "The left panel bitmap of Fig.4; the frame, the caption rule and the second panel are "
         "recorded on the container p11 r1.")
excluded(11, 3, "fragment-of-other",
         "The right panel bitmap of Fig.4; recorded on the container p11 r1.")
figure(12, 1, "line", "Fig.5 the result of SEIIR model with effective medication", "Fig. N",
       cited(12, 12, ["Fig.5"], 1, "The results shows in Fig.5."),
       "model", SEC_MODEL1, panels=2, layout="1x2", legend="inside", numbers=True, note=(
           "Same two-panel layout as Fig.4, now over days 150 to 180 and with the drug in play. "
           "Left: uncontrolled infectious individuals, a blue curve rising and a green one "
           "falling, legend 'without drug' / 'with drug'. Right: death cases, a blue curve to "
           "about 4.9 x 10^4 and a green one flattening at 4 x 10^4, legend 'with drug' / "
           "'with out drug'. The two legends map the same colour to opposite cases across the "
           "pair, so nothing on the page tells a reader which blue is with the drug. Caption "
           "below, inside the border box."))
excluded(12, 2, "fragment-of-other",
         "The left panel bitmap of Fig.5; recorded on the container p12 r1.")
excluded(12, 3, "fragment-of-other",
         "The right panel bitmap of Fig.5; recorded on the container p12 r1.")

# ---------------------------------------------------------------- model II
figure(14, 1, "map-or-plan-view",
       "Fig.6 The 12 districts and 2 areas of Sierra Leone.", "Fig. N",
       cited(14, 14, ["Fig.6"], 1, "Fig.6 shows it."),
       "model", SEC_MODEL2, numbers=False, labels=True, note=(
           "A choropleth of Sierra Leone with no choropleth: all twelve districts carry one "
           "flat pink fill, so the map encodes no value and only supplies the district names "
           "and their shapes. The Western Area is drawn as a small inset with numeral call-outs "
           "1 and 2 and the key '1 - Western Area Urban / 2 - Western Area Rural'. Caption "
           "below, inside the border box, and it ends with a dangling 'Source:' label with "
           "nothing after the colon."))
excluded(14, 2, "fragment-of-other", "The map bitmap inside Fig.6's border box; recorded on p14 r1.")
excluded(14, 3, "fragment-of-other",
         "The caption strip below the map bitmap of Fig.6; recorded on p14 r1.")
table(14, 4, 13, 14, "model", SEC_MODEL2,
      "and the results be shown in Table 2.",
      ("A closed grid with a vertical rule at every column boundary: the caption prints as the "
       "first band inside the frame, then a header row of thirteen district names broken "
       "mid-word ('Kail ahu n', 'Koi du', 'Ka mbi a'), then the Kailahun row. One column at the "
       "right of the header band is empty and unfilled. The other twelve rows, and the "
       "'(unit: kilometer) (source: google earth)' line, run onto p15."),
      rule="boxed", numeric=13, continued=True,
      cap_text=qp("Table 2 :the shortest path and distance between any two capitals", [14]),
      numbering="Table N:", position="above",
      mention=cited(14, 14, ["Table 2"], 1, "and the results be shown in Table 2."))
excluded(15, 1, "split-across-pages",
         "The twelve remaining rows of Table 2, header not repeated, with several values broken "
         "across two lines inside their cell (227 prints as '22' over '7', 309 as '30' over "
         "'9'), so a reader can take the wrong number at a glance; the row labelled Mattrujong "
         "sits on the diagonal that belongs to Bonthe. The table is recorded once, on p14 r4.")
table(15, 2, 13, 6, "model", SEC_MODEL2,
      "Measuring the need of every district hi",
      ("Three two-column blocks set side by side, each with its own 'h' header and its own rules "
       "above, under and below, so the single table reads as six columns and five row bands "
       "while holding 5 + 4 + 4 rows. Heavy vertical rules separate the blocks and no outer "
       "frame closes the left or right edge. The districts are listed in no order a reader can "
       "recover. Caption above the rules, printed 'Table.3' with no space before the digit."),
      rule="vertical-rules", numeric=3,
      cap_text="Table.3 the revolution of city", numbering="Table N.", position="above",
      mention=cited(21, 15, ["Table 3"], 1,
                    "we use the data to calculate the h with TOPSIS, and the results has been "
                    "shown Table 3."))
figure(16, 1, "map-or-plan-view", "Fig.7 locations of medical centers in Sierra Leone", "Fig. N",
       cited(16, 16, ["Fig. 7"], 1,
             "The Fig. 7 shows the scope that every mental center manages."),
       "model", SEC_MODEL2, numbers=False, labels=True, note=(
           "The same flat pink Sierra Leone outline as Fig.6, now with seven red stars and black "
           "arrows for the chosen medical centres. A numeral key for the Western Area Urban and "
           "Rural halves prints at the lower left. District names collide with boundaries and "
           "with the stars at Kambia and Kailahun, and the whole map is soft bitmap. Caption "
           "below, inside the border box; in the text layer it repeats itself and welds the next "
           "heading on, reading '...in Sierra Leone locations of medical centers in Part III'."))
excluded(16, 2, "not-an-exhibit",
         "Prose and one display equation after the Part III heading, not a ruled exhibit: the "
         "paragraph on population density, the density formulas and the eight evaluation "
         "aspects. The page-top rule is the only drawn mark.")
excluded(17, 1, "not-an-exhibit",
         "TOPSIS prose with three display equations; the only drawn marks are the page-top rule "
         "and the fraction bars. The three equations collapse to a bare symbol on the page - "
         "B_n, C_n and I_n each print with their right-hand side missing - and the humidity "
         "block is headed 'The temperature of the area is'.")
excluded(18, 1, "not-an-exhibit",
         "Prose and the F_n = C_open / C_all equation; no table, no rules, no shading.")
excluded(18, 2, "not-an-exhibit",
         "Prose and the K = (K_14~65 + K_65) / K_all equation; fraction strokes only.")
excluded(19, 1, "not-an-exhibit",
         "The four TOPSIS steps with decision matrices: prose, matrices and separation formulas, "
         "no ruled exhibit. The matrix header prints 'X' where the column should read X_j and the "
         "negative-ideal exponent renders as a dot.")
excluded(20, 1, "not-an-exhibit",
         "The rest of the TOPSIS steps - separation measures, relative closeness - as prose and "
         "display equations over the top half of p20. No table.")
table(20, 2, 13, 6, "model", SEC_DATA,
      "We finally conclude the relative statistics of those areas and list them in a form.",
      ("Header row in italic capitals - Population density, Open coefficient, Temperature (C), "
       "Humidity (%), Current disease situation - over twelve italic row labels, one light rule "
       "above, a heavy rule under the header and one internal vertical rule after the label "
       "column. No closed frame and no unit row: the units live in a note on p21 that reads "
       "item 1 only and stops at 'People /per km'. The thirteenth district, Western Area, and "
       "that note print on the next page."),
      rule="vertical-rules", numeric=5, continued=True,
      cap_text="Table4:the data of the different district", numbering="Table N:", position="above")
excluded(21, 1, "split-across-pages",
         "The thirteenth body row of Table 4 - Western Area, 25996.65, 50, 26, 81, 5 - with its "
         "rule above and its note below, then prose, the unnumbered heading 'The effect on beta "
         "of external factors', a bullet on the open degree of ETC and one display equation. The "
         "box is nine tenths text; the table is recorded once, on p20 r2.")
table(22, 1, 3, 9, "model", SEC_DATA,
      "we final get data needed from the website of World Bank.",
      ("Two grids share this one measured box and the census can carry it only once, so this row "
       "is Table 5 and Table 6 is recorded here in words only. Table 5: 3 rows of three "
       "countries, 9 columns (population density, temperature, humidity, open coefficient, "
       "economy, education, age, current disease situation), one rule above, one below, one "
       "internal vertical rule after the stub, header heavier than the body rules. Its header "
       "order disagrees with its own data - 'current disease situation' stands over 2917 and "
       "'Population density' over 45.5 - and 'Sierra Leone' wraps. Table 6, directly under it, "
       "is 3 rows x 2 columns of influence coefficients, horizontal rules only, no vertical, "
       "with the sentence that introduces it stopping at 'shown in Table' and losing the "
       "number. The box also carries one display equation and its prose above both grids."),
      rule="vertical-rules", numeric=8,
      cap_text="Table 5: the data of the three country", numbering="Table N:", position="above")

# ---------------------------------------------------------------- results and the six-month plan
figure(26, 1, "line", "Fig.8 the model based on logisitic", "Fig. N",
       cited(26, 26, ["Fig.8"], 1, "The result is shown in Fig.8."),
       "model", SEC_RESULTS, numbers=True, note=(
           "One black sigmoid against time in days from 0 to 150, y axis the daily drug output "
           "up to 2 x 10^5, no legend and no markers. The y tick numbers are rotated "
           "unreadably, the x title prints with doubled glyphs, and the curve renders dashed "
           "although it is a smooth production function. Caption below, inside the border box, "
           "in bold."))
excluded(26, 2, "fragment-of-other", "The plot bitmap inside Fig.8's border box; recorded on p26 r1.")
table(27, 1, 3, 7, "model", SEC_RESULTS,
      "We get our delivery plan for six month shown as following table and figure.",
      ("A closed grid with both horizontal and vertical internal rules, a grey filled header row "
       "carrying S_0, E_0, I_0,free, I_0,isolated, R_0 and D_0, alternating grey shading on the "
       "body rows, and an empty stub corner. 'Sierra Leone' wraps, and the word 'Leone' "
       "overflows below the bottom rule. Caption above, outside the frame, printed 'Table 7' "
       "with no punctuation; the prose cites it as 'Table.7' at the foot of p26."),
      rule="boxed", numeric=6, zebra=True,
      cap_text="Table 7 the value of parameters that moment", numbering="Table N", position="above",
      mention=cited(26, 27, ["Table.7"], 1,
                    "Suppose we start to distribute the drug from the 100th day since the "
                    "epidemic spread. Table.7"))
figure(27, 2, "composite-panel", "", "none", none_mention(), "result", SEC_RESULTS,
       panels=4, layout="2x2", source="none", note=(
           "One measured box holding four exhibits and no caption and no number: two MATLAB "
           "plots side by side with tiny illegible ticks and no legends, and directly under them "
           "two grids side by side, each 3 body rows x 4 columns (country, infected case, death "
           "case, portion), closed, vertical rules only, no shading, empty stub headers, "
           "'Sierra Leone' wrapping in every row. The prose introduces the whole six-month plan "
           "with 'We get our delivery plan for six month shown as following table and figure.' "
           "and the paper never numbers any of the six plans."))
excluded(27, 3, "fragment-of-other",
         "The left plot bitmap of the first delivery-plan pair; recorded in the composite row "
         "on p27 r2.")
excluded(27, 4, "fragment-of-other",
         "The right plot bitmap of the first delivery-plan pair; recorded in the composite row "
         "on p27 r2.")
figure(28, 1, "composite-panel", "", "none", none_mention(), "result", SEC_RESULTS,
       panels=8, layout="2x2+2x2", source="none", note=(
           "Four more biweekly plans stacked in one boxed band: plot pair, grid pair, plot pair, "
           "grid pair. Each grid is 3 body rows x 4 columns, closed, vertical rules only, no "
           "shading, with the header broken mid-word ('Infect' / 'ed' / 'case') and 'Sierra "
           "Leone' wrapping in every row; the word 'Leone' collides with the bottom rule at the "
           "lower left. Thin rules run down both margins and across the top of the band, which is "
           "what made the measurer take the whole stack as one region. No caption and no number "
           "on any of the eight panels."))
for _reg in (2, 3, 4, 5):
    excluded(28, _reg, "fragment-of-other",
             "One of the four plot bitmaps inside the p28 delivery-plan band; recorded in the "
             "composite row on p28 r1.")
excluded(29, 1, "not-an-exhibit",
         "The paragraph closing Part IV and opening the model-extension section, with one display "
         "equation; prose, not an exhibit.")
table(29, 2, 6, 4, "model", SEC_SENS,
      "We analysis the effect of the three factors on the death case by changing them.",
      ("Header row Initial value / Changed value / Changed percent with no text for the stub "
       "column, a rule above, a heavy rule under the header, a rule at the bottom and no side "
       "rules. Only the 1/sigma group prints here - header and one body row; the other five body "
       "rows (1/gamma, beta and their death-case outcomes) are on p30 with no continuation mark. "
       "The body alternates a factor row with an italic 'the death case' row, so the table reads "
       "as three treatments of three factors. The caption prints just above the top rule and its "
       "baseline strikes it."),
      rule="booktabs", numeric=3, continued=True,
      cap_text="Table 8:the three factors on the death case", numbering="Table N:", position="above",
      mention=cited(30, 29, ["table 8"], 1, qtail(30, "The table 8 shows that", 11)))
excluded(30, 1, "split-across-pages",
         "The other five body rows of Table 8, header not repeated; the last of them reads "
         "'the death case 119556 9343221 681.4%', a death count an order of magnitude larger "
         "than the same row's initial value. The region also encloses the bitmap of Fig.9, which "
         "is recorded separately from its own raster. The table is recorded once, on p29 r2.")
figure(30, 2, "line", "Fig. 9: The changes, and death cases", "Fig. N",
       cited(30, 30, ["fig.9"], 1, "and fig.9 shows the result graphicall"),
       "model", SEC_SENS, numbers=True, note=(
           "One rising S-curve with no markers, no legend and no grid. The y axis is labelled "
           "'1/Death_case' with a multiplier printed detached at the top left, and the x axis "
           "label 'Beta' is cut off at its right end. The caption below the art loses its own "
           "title: 'The changes, and death cases' is a fragment."))
figure(30, 3, "line", "Fig.10: creases, and death cases increases", "Fig. N",
       cited(31, 30, ["fig. 10"], 1,
             "As we can see from fig. 10, the death case increases related to E0 increases."),
       "model", SEC_SENS, numbers=True, note=(
           "One curve of the death case against E0 over the second half of p30. The caption "
           "below the art has lost its beginning - only 'creases, and death cases increases' "
           "survives, which is the tail of the prose sentence 'As Gm decreases, and death cases "
           "increases' - so the exhibit is named only by its number. The measured container also "
           "carries the paragraph that introduces it."))
excluded(30, 4, "fragment-of-other",
         "The plot bitmap of Fig.10 inside the container p30 r3; recorded on that container.")
excluded(30, 5, "fragment-of-other",
         "The caption strip of Fig.10, a pasted bitmap of the caption line alone; recorded on "
         "the container p30 r3.")
excluded(31, 1, "not-an-exhibit",
         "Two paragraphs closing the E0 sensitivity and opening the delivery-model sensitivity; "
         "prose with no drawn mark but the page-top rule.")
table(31, 2, 3, 3, "model", SEC_SENS,
      "The results of sensitivity analysis to r is shown on Table.9.",
      ("Three body rows and three columns with no side rules, a heavy internal vertical rule, "
       "rules above the header, under it, between the first and second body rows and at the "
       "bottom, but none between the second and third. The header wraps to 'The days use / to "
       "control' and never says what the last column holds. Cells mix bare counts with bracketed "
       "percentages - 50 against 629128, then 100(100%) against 162(35.3%), then 200(400%) "
       "against 102(59.2%) - so the reader cannot tell a changed input from an outcome, and the "
       "sentence that follows the table cites 'Table 2' instead of Table 9."),
      rule="vertical-rules", numeric=2,
      cap_text="Table 9", numbering="Table N", position="above",
      mention=cited(31, 31, ["Table.9"], 1,
                    "The results of sensitivity analysis to r is shown on Table.9."))
figure(32, 1, "line", "Fig.11", "Fig. N",
       cited(31, 32, ["Fig.11"], 1, qtail(31, "in the Fig.11", 10)),
       "result", SEC_SENS, numbers=True, note=(
           "One black decay curve: the days needed to bring the epidemic under control against "
           "the maximum daily drug output, y axis 0 to 4 x 10^4, x axis 0 to 10000 doses, no "
           "legend and no markers. The exhibit is labelled by nothing but a bare 'Fig.11' under "
           "the art - the sentence that says what it shows sits in the body text above, so the "
           "figure has no title at all."))

# ---------------------------------------------------------------- emit
for _n, _row in enumerate(sorted(ITEMS + TABLES, key=lambda r: (r["page"], r["place"]["page_order"])), 1):
    _row["place"]["doc_order"] = _n

RULES: list[str] = [
    "Full width means 75 per cent or more of this paper's own 415.4 pt measure: the narrowest "
    "recorded grid is Table 9 at 80.5 per cent and the widest is the p22 band at 102.2, so all "
    "thirteen tables are full and none is half, while the figures run from a 47.7 per cent "
    "sensitivity plot to the 102.2 per cent Fig.4 [table.width].",
    "This PDF draws four thin rules around every single line of type, so prose bands and display "
    "equations arrive as page-wide measured regions - the page-header rule at y=65.5 stretches a "
    "band's box to the full text measure. The white-fill test that separated prose from exhibits "
    "on an earlier paper returns nothing here, so the eight not-an-exhibit and the four "
    "split-across-pages rejections were made by looking at the render, not by an area or fill "
    "threshold [place.area_frac].",
    "Every pasted plot arrives as a bitmap inside a drawn frame, and most frames carry the caption "
    "as a second, separate bitmap strip, so the frame is the exhibit row and the seventeen inner "
    "rasters are excluded as fragments of it rather than counted as seventeen more exhibits "
    "[place.page_order].",
    "Two printed floats can share one measured box: on p22 Table 5 and Table 6 sit one above the "
    "other inside a single region, and the census can carry that box only once, so Table 6 - three "
    "body rows, two columns, horizontal rules only, introduced by a sentence that loses its own "
    "number at 'shown in Table' - is recorded in words on the Table 5 row and is not a row of its "
    "own [table.rows].",
    "Rows counts body rows only, never the header: the p2 symbol slice is 7 rows, the p3 slices 9 "
    "and 12, the p4 slices 8 and 10, Table 1 is 5 body rows although only 1 prints beside its "
    "caption, and the delivery-plan grids are 3 body rows each [table.rows].",
    "Rule style is read literally: boxed means a closed four-sided frame, which only Table 2 and "
    "Table 7 have; vertical-rules means horizontal rules with an internal vertical divider and "
    "open left and right edges, which is ten of the thirteen; booktabs means horizontal rules "
    "alone, which is Table 8 [table.rule_style].",
    "Eight grids continue onto a following page with the header not repeated and no continuation "
    "mark - the four symbol slices on pp3-4, Table 1, Table 2, Table 4 and Table 8 - so continued "
    "is true on the row that keeps the header and the tail is excluded as split-across-pages "
    "instead of becoming a second table [table.continued].",
    "A box that holds two or more different families and no caption and no number is one "
    "composite-panel row, not two rows: the p27 band is two plots above two grids and the p28 "
    "band is four plots and four grids, and neither carries a number the paper ever explains "
    "[geometry.panel_count].",
    "Position splits by exhibit type without exception - all eight numbered table rows print "
    "their caption above the grid and all thirteen numbered figures print theirs below the art - "
    "and the two uncaptioned composite rows and the five symbol slices keep the default while "
    "caption_source stays none [caption.position].",
    "The printed caption forms have no single convention - 'Fig.2.1the', 'Fig. 9:', 'Table.3', "
    "'Table4:the', 'Table 5: the', bare 'Fig.11' and bare 'Table 9' all occur, three of them with "
    "no space after the number - so numbering records the nearest vocabulary form and the exact "
    "printing is described per row [caption.numbering].",
    "Three exhibits are named in the prose before the page they print on - Table 3 six pages "
    "early, Table 8 and Fig.10 one page early - so lead_pages is negative on those three rows and "
    "first_page points backwards; twelve of the twenty-eight exhibit rows are never named in the "
    "prose at all [mention.lead_pages].",
    "Section paths follow the printed heading above the block, including three the heading pass "
    "missed - 'Model I' on p5, 'Model II' on p13 and 'Results & analysis' on p25 - which are "
    "accepted because each is a printed line of the text layer [place.section_path].",
    "Note sentences are quoted from the layer that introduces the grid, which is why two of them "
    "carry the paper's own breakage: 'Measuring the need of every district hi' and 'we final get "
    "data needed from the website of World Bank' [table.note_sentence].",
]

NOTE = (
    "Paper 73, Team 35532. Fifty-nine measured regions over twenty-seven of the thirty-four pages, "
    "all fifty-nine accounted for: twenty-eight exhibit regions - thirteen numbered figures, the "
    "two uncaptioned delivery-plan bands, and thirteen tables - and thirty-one exclusions, so "
    "unaccounted is zero and nothing is left unresolved. Seventeen exclusions are inner rasters of "
    "framed plots, eight are prose or equation bands, four are the tails of tables that break "
    "across a page, one is the band that carries three caption strips, and one is the abstract's "
    "last lines. The paper numbers thirteen figures and nine tables; every figure is here, and "
    "eight of the nine tables are rows because Table 6 shares p22's measured box with Table 5.\n\n"
    "The measuring defect on this paper is new to the lane and shapes the whole census. The PDF "
    "draws a set of thin rules around every individual line of type, so a paragraph or a display "
    "equation comes out as a page-wide vector region, and the running-head rule at y=65.5 drags "
    "those boxes out to the full 415.4 pt measure. Nothing mechanical separates them from real "
    "exhibits: the white-fill discriminator used on the previous paper returns nothing usable "
    "here, and area buys nothing either, since a prose band reaches 0.59 of the page while the "
    "p27 delivery band that holds four exhibits reaches 0.21. Every rejection on this paper was "
    "made by looking at the render, and the eight not-an-exhibit rows are all prose with the "
    "page-top rule as their only drawn mark.\n\n"
    "Every pasted plot is framed by vector rules after it was pasted, so the container and its "
    "content are two regions. Where the frame holds one plot - Figs 1, 3, 4, 5, 6, 7, 8, 9, 10 "
    "and 11 - the frame is the row and the raster is excluded; where it holds three separately "
    "numbered plots, as on p8, the three rasters are the rows and the frame is excluded as the "
    "band carrying their caption strips. The result is that this census records thirteen figures "
    "from fifteen figure regions plus two composite bands, and seventeen regions of pasted "
    "bitmap that are not exhibits in their own right.\n\n"
    "What the exhibits are. Nine line plots carry the two model fits, the drug-production curve, "
    "the two sensitivity sweeps and the control-time curve; two are flow charts - the four-box "
    "SEIR cartoon of Fig.1 and the five-box SEIIR cartoon of Fig.3; two are the Sierra Leone "
    "district maps of Figs 6 and 7; two are the uncaptioned delivery-plan bands of pp27-28; and "
    "thirteen are grids. The line plots are pasted Matlab bitmaps throughout: Fig.4 and Fig.5 "
    "each hold two panels with their own legends inside the axes, and Fig.5's two legends map the "
    "same colour to opposite cases, so 'with drug' is the blue curve on one panel and the green "
    "curve on the other and nothing on the page resolves it.\n\n"
    "The quietest failure is the delivery plan. Six monthly plans are introduced by one sentence - "
    "'We get our delivery plan for six month shown as following table and figure.' - and none of "
    "the six is numbered: two plots and two grids on p27, four plots and four grids on p28, every "
    "grid 3 rows by 4 columns of country, infected case, death case and portion, with 'Sierra "
    "Leone' wrapping onto a second line in every one of them and the word 'Leone' colliding with "
    "the bottom rule at the lower left of p28. The header of those grids breaks mid-word, reading "
    "'Infect' over 'ed' over 'case', so the column cannot be read as one label. None of the six "
    "carries a scale, a legend or a unit on either plot.\n\n"
    "The tables carry their own damage. The three symbol lists run to five slices across pp2-4 "
    "with the header printed only twice, and the slices disagree with themselves: the open-degree "
    "row is defined twice in a row on p4 with C_n repeating F_n's own wording, G(t) wraps onto a "
    "second line so the list reads as six short rows, and three definitions in a row are cut "
    "mid-sentence. Table 5's header disagrees with its own body - 'current disease situation' "
    "stands over 2917 and 'Population density' over 45.5 - and Table 4's unit note stops at 'People "
    "/per km' after item 1 of what should be four. In Table 2 several distances are broken across "
    "two lines inside their cell, so 227 prints as '22' over '7' and 309 as '30' over '9'. "
    "Table 9's header reads 'The days use / to control' and never says what the last column is, "
    "and its cells mix bare counts with bracketed percentages so a reader cannot tell the changed "
    "input from the outcome; the sentence that follows it also cites 'Table 2' instead of Table 9. "
    "Table 8's last row reports a death case of 119556 against an initial value an order of "
    "magnitude smaller, and the caption of Table 8 has its baseline struck through by the top rule "
    "of its own grid.\n\n"
    "On the figure side, Fig.1 draws four compartments S, E, I and R while the text beside it says "
    "an infectious individual 'either recover and survive R or die D', so the cartoon has no D at "
    "all. Fig.3's box letters are bitmaps pasted next to vector edge labels and sit visibly ragged "
    "against them. Fig.6's choropleth encodes nothing - all twelve districts carry one flat pink "
    "fill - so the map is only a key to district names and shapes, and its caption ends in a "
    "dangling 'Source:' with nothing after the colon. Fig.7 reuses the same fill and collides its "
    "district names with seven red star markers. Fig.8's y tick numbers are rotated unreadably, "
    "Fig.9's x axis label 'Beta' is cut off at its right end and its caption has lost its own "
    "title, and Fig.10's caption has lost its beginning - only 'creases, and death cases increases' "
    "survives, which is the tail of the prose sentence above it. Fig.11 is labelled by nothing but "
    "a bare 'Fig.11' under the art, so the paper's last figure has no title at all.\n\n"
    "Citation practice is thin. Sixteen of the twenty-eight exhibit rows are named in the prose and "
    "each is cited exactly once; twelve are never named - the three p8 plots, the two delivery "
    "bands, the five symbol slices, Table 4 and Table 5. Three citations point backwards across a "
    "page break, Table 3 by six pages, which is why lead_pages is negative there. The prose also "
    "loses its own pointer in two places: 'shown in Table' for Table 6 without the number, and "
    "'shown Table 3' for Table 3 without the preposition.\n\n"
    "The heading layer is worse than the prose. The pass that builds the section index missed 'Model "
    "I' on p5, 'Model II' on p13 and 'Results & analysis' on p25, and invented a heading '2 "
    "December' out of a date in the data prose, so the paths recorded here use the printed lines "
    "the pass dropped. Three printed captions have no space after their number - 'Fig.2.1the early "
    "EBOV transmission period of Guinea', 'Table4:the data of the different district', "
    "'Table 9 The days use' - and the caption vocabulary has no lower-case or unpunctuated form, so "
    "the nearest form is recorded and the printing itself is described on each row."
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
out = PROXY / "pc73-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
