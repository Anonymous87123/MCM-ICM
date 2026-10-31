"""Hand census of P-D-2015-34985-c7be0d8b (Team 34985, 20 pages, 14 measured regions).

Eleven figure rows, three table rows, nothing excluded and nothing unaccounted. The paper prints
nine numbered figures and no numbered table at all; the three grids carry in-grid titles or the
appendix heading instead of a "Table N" caption.

  p1  r1  (unnumbered) node-link-network     the cost-to-index function map on the summary sheet
  p5  r1  (unnumbered) table-grid            the GWP weight table, two column pairs in one box
  p6  r1  Fig.1       map-or-plan-view       world choropleth of the Ecological Impact Index
  p7  r1  Fig.2       line                   theoretical and adjusted income distributions
  p8  r1  Fig.3       map-or-plan-view       world choropleth of the Development Index
  p9  r1  Fig.4       composite-panel        A scatter of D against E, B mean-level bar pair
  p10 r1  (unnumbered) table-grid            the top-ten country ranking, four country columns
  p12 r2  Fig.5(a)    heatmap-or-contour     random seed: wealth and population automata
  p12 r1  Fig.5(b)    heatmap-or-contour     trended seed: the same automata
  p13 r1  Fig.6       node-link-network       the Zambia function map, cost to D_i and E_i
  p15 r1  Fig.7       line                   sustainability against investment, three alphas
  p16 r1  Fig.8       bar                    investment per factor, solid and hatched decades
  p16 r2  Fig.9       composite-panel        D_i, E_i and S trends in three panels
  p20 r1  (unnumbered) table-grid            the twelve iterated-function equations

Three printed faults shape this record. The summary sheet repeats Figure 6's function map as an
unnumbered picture. The caption glyph runs on pp7 and p12 reach the layer with every space
dropped ("Figure5: Comparisonoftwoseeds"), so both captions are typed from the crops. And the
p13 caption is set INSIDE a sentence - the paragraph ends p12 with "we created a map of the main
factors that influence the Socioeconomic" and resumes under the caption with "and Ecological
Indices of Zambia."
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2015-34985-c7be0d8b"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

for _key, _bbox in REG.items():
    _ctx = CTXREG.get(_key)
    if _ctx is None or max(abs(a - b) for a, b in zip(_ctx["bbox"], _bbox)) > 0.5:
        raise SystemExit(f"region numbering disagrees with the context dump at {_key}")

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


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


def uncited() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          pattern: str = "direct", read: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below",
            units: bool = False, variables: int = 0, conditions: bool = False,
            concludes: bool = False, voice: str = "none") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim.strip() else 0),
            "units": units, "variables": variables > 0, "variable_count": variables,
            "conditions": conditions, "concludes": concludes, "voice": voice,
            "position": position}


def geometry(family: str, panels: int = 1, layout: str = "1x1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = True,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


# ---------------------------------------------------------------- section paths
# Read off the printed headings. The heading index in the context dump carries no text at all
# (every entry has text null and top 0), so every path here is typed from the printed line, which
# the validators accept because a printed line is a heading even when the detector missed it.
SEC_SUMMARY = ["Mathematical Contest in Modeling (MCM/ICM) Summary Sheet"]
SEC_41 = ["4 Environmental Resource Management Model", "4.1 Quantifying Pollution"]
SEC_52 = ["5 Development for Better Life Quality", "5.2 Socioeconomic Development Index"]
SEC_6 = ["6 Ecological-Economic Trade off"]
SEC_71 = ["7 20-year plan for Zambia", "7.1 Population Growth and Economic Development"]
SEC_72 = ["7 20-year plan for Zambia", "7.2 Iterated Function Map"]
SEC_75 = ["7 20-year plan for Zambia", "7.5 Particle Swarm Optimization"]
SEC_76 = ["7 20-year plan for Zambia", "7.6 Evaluating the 20-year Plan"]
SEC_A = ["A Equations for Iterated Function Map"]

ITEMS: list[dict] = []


def figure(page: int, reg: int, number: str, family: str, cap: dict, cap_src: str,
           mention: dict, kind: str, section: list[str], note: str,
           geo: dict | None = None, confidence: str = "high",
           numbered_section: bool = True, section_kind: str = "model") -> None:
    bbox = REG[(page, reg)]
    ITEMS.append({
        "page": page, "bbox": bbox, "kind": kind, "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap["verbatim"],
        "caption": cap, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section, numbered_section),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    })


# ------------------------------------------------------------------- p1 summary sheet
MAP_NOTE = (
    "The cost-to-index function map, drawn as a bitmap: the boxed word COST at the foot of the "
    "picture, thirty arrows rising out of it through the factor boxes (Education, Health Care "
    "Expenditures, Doctors, Life Expectancy, HIV, Contraceptives, Jobs, Advertisements, Tourism, "
    "Agriculture, Availability, Wealth, Mining, Copper, Cobalt, Coal, Pollution, Non Renewable, "
    "Solar, Hydropower, Dams, Renewable, Resource Consumption) into the two sink boxes "
    "'Socioeconomic Development Index' and 'Ecological Impact Index'. Blue arrows feed the "
    "socioeconomic index, orange the ecological one, and nothing on the sheet keys the two "
    "colours. No caption, no number, no axes, no values. This is the same map Figure 6 prints on "
    "p13, repeated on the summary sheet unnumbered and uncited - the paper never cross-references "
    "back to it."
)
figure(1, 1, "none", "node-link-network", caption("", numbering="none", position="above"),
       "none", uncited(), "raster", SEC_SUMMARY, MAP_NOTE,
       geometry("node-link-network", numbers=False))

# ------------------------------------------------------------------- p6 Figure 1
figure(6, 1, "1", "map-or-plan-view",
       caption(q("Figure 1: Worldwide view of country Ecological Impact Index (Di ) values", 6),
               units=False, variables=1),
       "text-layer", uncited(), "raster", SEC_41,
       "A world choropleth in one raster: country shapes filled from a five-step orange-yellow-"
       "red ramp, no borders, no graticule, no projection note. The key sits INSIDE the picture at "
       "the lower left, printed 'Ecological Index' over a stepped colour bar lettered 'Low' and "
       "'High' at its ends, so the classes carry no numbers and a reader cannot recover the index "
       "value at all. Countries with no data are left white (Europe, Russia, most of the Sahel) "
       "while the prose says they are coloured grey, and Greenland and Antarctica are solid grey. "
       "The caption is the only text the layer prints with its spaces intact; its subscript i "
       "arrives on its own line.",
       geometry("map-or-plan-view", legend="inside", colorbar=True, numbers=False))

# ------------------------------------------------------------------- p7 Figure 2
figure(7, 1, "2", "line",
       caption("Figure 2: Graph of the theoretical income distribution I(x) and adjusted income "
               "distribution A(x)"),
       "typed-from-crop", uncited(), "raster", SEC_52,
       "Two smooth curves, not a scatter: the red 'Theoretical Income Distribution I(x)' rising "
       "from the origin to about 0.92 at x = 0.9, and the blue 'Adjusted Income Distribution "
       "(1-x)I(x)' arching to a peak near x = 0.55 and falling back, with the red curve above the "
       "blue one everywhere but at the two ends. Each curve is named in a boxed annotation with a "
       "leader line inside the plot, so the legend is inside and carries no colour chrome. The x "
       "axis is lettered 0 to 0.9 but the ticks are printed as 0.1, 0.2 and so on with no axis "
       "title; there is NO y axis at all - no ticks, no title, no scale. The caption reaches the "
       "layer with every space dropped ('Figure2: Graphofthetheoreticalincomedistribution') and "
       "wraps its last token, 'A(x)', onto a second line, so the verbatim here is typed from the "
       "crop.",
       geometry("line", legend="inside", labels=True))

# ------------------------------------------------------------------- p8 Figure 3
figure(8, 1, "3", "map-or-plan-view",
       caption(q("Figure 3: Worldwide view of country Development Index (Di ) values", 8),
               variables=1),
       "text-layer", uncited(), "raster", SEC_52,
       "The same world choropleth machinery as Figure 1 with a different variable: the same five-"
       "step ramp now keyed inside the lower left as 'Development Index' between 'Low' and "
       "'High'. The geographic reading is the inverse of Figure 1 by construction - the "
       "underdeveloped Sahel and central Africa sit at the red end here and the yellow end there - "
       "which is the paper's own point. No graticule, no numbers on the key, no data-label, and "
       "the no-data countries are white here too against the prose's 'coloured grey'.",
       geometry("map-or-plan-view", legend="inside", colorbar=True, numbers=False))

# ------------------------------------------------------------------- p9 Figure 4
figure(9, 1, "4", "composite-panel",
       caption(q("Figure 4: Tradeoff dynamics. A: Socioeconomic Development Index (Di vs. "
                 "Ecological Impact Index Ei for any given country iB: Mean Index levels for "
                 "underdeveloped vs. other nations.", 9),
               variables=2),
       "text-layer",
       cited(9, 9, ["Figure 4"], 1, "This is highlighted in Figure 4 below"),
       "raster", SEC_6,
       "Two panels in one raster, marked 'A.' and 'B.' at their upper left. Panel A is a diamond "
       "scatter of the Socioeconomic Development Index (x, 0 to 1) against the Ecological Impact "
       "Index (y, 0 to 1) for about ninety countries, falling from 0.85 at x = 0.05 to 0.25 at "
       "x = 0.95, with its legend INSIDE at the lower left on a grey plate: orange 'Other Nation', "
       "blue 'Underdeveloped Nation'. Panel B is four vertical bars in two groups - Economic and "
       "Ecological - blue and orange, 32 against 70 and 77 against 49, on a y axis 0 to 100 with "
       "NO legend, so the panel's colour code is only recoverable from panel A's legend. The "
       "caption welds both panels' descriptions into one run-on line with no space between 'i' and "
       "'B:' and never ends the A-sentence.",
       geometry("composite-panel", panels=2, layout="1x2", legend="inside", labels=True))

# ------------------------------------------------------------------- p12 Figure 5 (two regions)
FIG5_CAP = ("Figure 5: Comparison of two seeds: random and biased wealth distribution with even "
            "initial population distribution. For the red-blue gradients on the wealth and "
            "population automata, red indicates higher values of wealth and population while blue "
            "indicates lower values.")
FIG5_NOTE = (
    "One of the two measured halves of Figure 5, printed as its own pasted bitmap. The drawing is "
    "a three-row by two-column block of cellular-automata snapshots: 'Wealth Distribution' down "
    "the left column and 'Population Distribution' down the right, the rows lettered 'Initial', "
    "'10 Years' and '20 Years' on a vertical arrow between the columns. Cells are red for high and "
    "blue for low, with white where the cell is empty, and the class breaks are not printed "
    "anywhere. The 10-year and 20-year rows are smooth because the automaton diffuses; the initial "
    "row is fine-grained noise. No axes, no scale, no legend inside - the red-blue key exists only "
    "in the caption sentence. The half is labelled below its picture, not by the caption: '(a) "
    "Random initial wealth distribution.' on the left half and '(b) Trended initial wealth "
    "distribution.' on the right, and the main caption is set once under both."
)
figure(12, 2, "5", "heatmap-or-contour", caption(FIG5_CAP), "typed-from-crop",
       cited(11, 12, ["Figure 5"], 2,
             "The results of our cellular automata model over the course of 20 years are shown in "
             "Figure 5.", read=2),
       "raster", SEC_71,
       FIG5_NOTE + " This is the (a) random half; the pair is recorded as two rows because the "
       "region pass measures each half separately and no region spans both.",
       geometry("heatmap-or-contour", panels=6, layout="3x2", numbers=False))
figure(12, 1, "5", "heatmap-or-contour", caption(FIG5_CAP), "typed-from-crop",
       cited(11, 12, ["Figure 5"], 2,
             "The results of our cellular automata model over the course of 20 years are shown in "
             "Figure 5.", read=2),
       "raster", SEC_71,
       FIG5_NOTE + " This is the (b) half: its own subcaption prints 'Trended initial wealth "
       "distribution.' while the shared caption above calls the same seed 'biased', so the pair "
       "names one seed two ways. The trended seed starts its wealth in the lower-right corner, as "
       "the prose says, and its population begins empty outside that corner.",
       geometry("heatmap-or-contour", panels=6, layout="3x2", numbers=False))

# ------------------------------------------------------------------- p13 Figure 6
figure(13, 1, "6", "node-link-network",
       caption(q("Figure 6: Di and Ei with regards to features of Zambia, in terms of cost.", 13),
               variables=2),
       "text-layer",
       cited(14, 13, ["Figure 6"], 2,
             "in the sustainability-cost map (Figure 6) through a number of relationships."),
       "raster", SEC_72,
       "The Zambia function map, drawn as a pasted bitmap: the boxed word COST at the foot, "
       "twenty-five factor boxes above it joined by arrows into the two index sinks, exactly the "
       "topology of the unnumbered map on the summary sheet but with Zambia-specific factors "
       "added (Copper, Cobalt, Mining, Agriculture, Tourism, Solar, Dams, Hydropower). The two "
       "arrow colours still carry the socioeconomic and ecological split and still have no key. "
       "Despite 'in terms of cost' in the caption there is no axis, no scale and not one number on "
       "the picture, so cost is shown only as the direction of an arrow. The caption is set INSIDE "
       "a sentence: p12 ends 'we created a map of the main factors that influence the "
       "Socioeconomic' and the page resumes under the caption with 'and Ecological Indices of "
       "Zambia.', so the region also splits a paragraph.",
       geometry("node-link-network", numbers=False))

# ------------------------------------------------------------------- p15 Figure 7
figure(15, 1, "7", "line",
       caption(q("Figure 7: Effect of alpha on resulting sustainability. The black line represents "
                 "an example budget/investment of 1.2 billion dollars.", 15)),
       "text-layer",
       cited(15, 15, ["Figure 7"], 2,
             "Figure 7 shows the relationship between investment and the resulting "
             "sustainability.", read=2),
       "raster", SEC_75,
       "Three curves with round markers over a near-vertical knee: sustainability against "
       "'ICM Financial Investment' (x, printed 0 to 2E+09 with mixed notation - plain integers for "
       "the first two ticks, scientific for the rest) and 'Resulting Sustainability' (y, 0.315 to "
       "0.35). The legend is INSIDE at the lower right, boxed, lettered in the Greek alpha "
       "('a = 0.5', 'a = 1.0', 'a = 1.5') which the caption renders as the word 'alpha'. One "
       "vertical reference line marks 1.2 billion, the example budget the prose points at. Units "
       "are absent from both axes although the x quantity is dollars; the top of the y window is "
       "chosen so that all three alphas crowd into the last two ticks.",
       geometry("line", legend="inside", labels=True))

# ------------------------------------------------------------------- p16 Figure 8
figure(16, 1, "8", "bar",
       caption(q("Figure 8: Amount of money that should be invested based on the α level. Solid "
                 "represents the first 10 years of the plan and striped represents the second 10 "
                 "years. These numbers are based on a 1.2 billion dollar budget.", 16)),
       "text-layer", uncited(), "raster", SEC_75,
       "Seven groups of paired vertical bars - Contraceptives, Health, Education, Agriculture, "
       "Mining, Tourism, Solar - against 'Financial Investment' on y (0 to 500000000, no unit "
       "printed) and no x axis title. The six-entry legend is INSIDE at the upper right and prints "
       "each alpha twice ('0.5', '0.5', '1', '1', '1.5', '1.5'), leaving solid against hatched as "
       "the only cue for first decade against second, which the caption alone explains. The "
       "hatched sample for 0.5 is drawn blue while the hatched bars it keys are pink, the top y "
       "tick collides with the plot border and reads as a run-on '500000000 0', and the last three "
       "groups are near zero and unreadable. Figure 7's legend prefixes the same alphas with the "
       "Greek letter; this one drops it.",
       geometry("bar", legend="inside", labels=False))

# ------------------------------------------------------------------- p16 Figure 9
figure(16, 2, "9", "composite-panel",
       caption(q("Figure 9: Di , Ei and S trends over time, respectively. Blue represents α = 0.5, "
                 "red represents α = 1, and green represents α = 1.5.", 16), variables=3),
       "text-layer",
       cited(16, 16, ["Figure 9"], 1,
             "The trends in Figure 9 give us some insight on what to expect with an optimized"),
       "raster", SEC_76,
       "Three panels side by side in one raster: three lines with markers in each, x ticked 0 to "
       "20 in every panel, and NOTHING else - no axis titles, no y tick numbers, no subpanel "
       "letters, no per-panel title, and no legend; the caption is the only place the colours are "
       "mapped to alphas. The middle panel is scaled differently from its neighbours, so the three "
       "are not visually comparable even though the caption's word 'respectively' implies they "
       "are, and with the y magnitudes unprinted the paper's own claim that E_i falls while D_i "
       "and S rise cannot be read off the picture.",
       geometry("composite-panel", panels=3, layout="1x3", numbers=True))


# ------------------------------------------------------------------- tables
TABLES: list[dict] = []


def table(page: int, reg: int, cap: dict, cap_src: str, mention: dict, section: list[str],
          note: str, rows: int, cols: int, numeric: int, text: int, rule: str,
          header_rows: int = 1, merged: bool = False, zebra: bool = False,
          diagonal: bool = False, units_in_header: bool = False, decimal: bool = False,
          continued: bool = False, width: str = "full", kind_note: str = "table-grid",
          note_sentence: str = "", confidence: str = "high") -> None:
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": "vector",
        "caption_source": cap_src, "caption_verbatim": cap["verbatim"], "caption": cap,
        "place": place(page, reg, "model" if section is not SEC_A else "appendix", section),
        "mention": mention, "note": note, "confidence": confidence,
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": units_in_header,
                  "decimal_aligned": decimal, "numeric_cols": numeric, "text_cols": text,
                  "width": width, "orientation": "portrait", "continued": continued,
                  "note_sentence": note_sentence},
        "family": kind_note,
    })


table(5, 1,
      caption(q("Global Warming Potentials (IPCC 2013) [6]", 5), numbering="none",
              position="above"),
      "text-layer", uncited(), SEC_41,
      "The GWP weight table, ruled as a closed box: a title row spanning all four columns, a "
      "two-line header ('Pollutant' / '100-year GWP' repeated over the right-hand pair), then "
      "THREE body rows carrying six pollutants as two side-by-side column pairs - Carbon Dioxide "
      "(CO2) 1, Methane (CH4) 28, Nitrous Oxide (N2O) 265 on the left; Hydrofluorocarbons 12400, "
      "Perfluorocompounds 11100, Sulfur Hexafluoride 23500 on the right. The pair-within-one-grid "
      "layout is what makes 3 rows read as 6 entries, so cols counts the physical four. No number, "
      "no 'Table' word, no caption outside the grid; the title is inside the box and is what this "
      "row records as its caption. Body text runs above and below the box, so the table is set "
      "mid-paragraph rather than floated.",
      rows=3, cols=4, numeric=2, text=2, rule="boxed", header_rows=2, merged=True)

table(10, 1,
      caption(q("Top 10 Most Sustainable Countries", 10), numbering="none", position="above"),
      "text-layer",
      cited(10, 10, ["the table"], 1,
            "Only countries that both we and the SSF had data for were ranked. As seen in the "
            "table", pattern="as-shown-in"),
      SEC_6,
      "The ranking grid, a closed box with vertical rules on all four column boundaries: a title "
      "row spanning the width, a two-line header ('Our Di' / 'SSF Human Well-being' / 'Our Ei' / "
      "'SSF Enviro. Well-being') and TEN body rows of country names in all four columns - no "
      "numeric column at all, which is the point of the table: it is a set of four rankings laid "
      "side by side so the reader can count the overlaps. Headers wrap internally, and the 'Our "
      "Di' header mixes italic math with roman text while the other three do not. Nothing is "
      "numbered and the prose calls it only 'the table'.",
      rows=10, cols=4, numeric=0, text=4, rule="boxed", header_rows=2, merged=True)

table(20, 1,
      caption("", numbering="none", position="above"), "none", uncited(), SEC_A,
      "The appendix equation table: four physical columns headed '#', 'Feature', 'Inputs' and "
      "'Equation', thirteen body rows because the row number 3 is printed twice (1, 2, 3, 3, 4 "
      "through 12). Every cell is enclosed, so the grid is boxed with vertical rules; no cell is "
      "merged, and the multi-line cell contents (long feature names, stacked fractions) are "
      "wrapping, not merging. The paper's title for it is the appendix heading 'A Equations for "
      "Iterated Function Map' printed above the grid, so the caption block is empty and the "
      "heading supplies the name. Printed damage: the birth-rate equation loses its decimal point "
      "and reads '.070428-5.62ln(x)', the fourth row reuses the number 3, 'Non-Renewable' is "
      "hyphenated as 'Renev-able' across a line break, 'ln(X)' capitalises where its neighbours "
      "use 'ln(x)', and the last four rows' equations overrun their column and stack fractions "
      "with no visible summation.",
      rows=13, cols=4, numeric=1, text=3, rule="boxed",
      note_sentence=q("The equations in the above table were derived through linearized plots of "
                      "data extracted from", 20))

RULES = [
    "Measure first, then read the pixels: the fourteen measured regions of this paper resolve "
    "into eleven figure rows and three table rows with nothing refused and nothing unaccounted, "
    "because every region here is either a framed drawing or a ruled grid "
    "[place.area_frac].",
    "A bitmap of arrows between labelled boxes is a node-link-network and not a flowchart, and it "
    "is the family only when the arrows carry a quantity: the summary map and Figure 6 both draw "
    "COST at the foot fanning into the two index sinks [geometry.family].",
    "Two measured regions under one printed caption are two rows, never one row with a union box: "
    "Figure 5's (a) and (b) halves each own a region and each carries the same caption verbatim "
    "[caption.verbatim].",
    "When a caption glyph run reaches the layer with its spaces stripped, the verbatim is typed "
    "from the crop instead of quoted, and the row's source is marked accordingly; Figure 5 and "
    "Figure 2 are the only two such rows here [caption.numbering].",
    "A caption printed inside the grid is a caption: the GWP table's title row and the top-ten "
    "grid's title row are recorded with numbering 'none' and position 'above' "
    "[caption.numbering].",
    "An unnumbered grid with no title of its own takes its name from the appendix heading printed "
    "above it, so its caption block stays empty and its numbering is 'none' [caption.numbering].",
    "Every key on this paper is drawn inside its picture, so legend is 'inside' on all eleven "
    "figure rows and there is not one outside legend to record [geometry.legend].",
    "Count the physical columns, not the logical ones: the GWP grid prints four columns holding "
    "two side-by-side pairs and the ranking grid prints four country columns and no numeric "
    "column at all [table.cols].",
    "A table whose cells are all enclosed is 'boxed', and a spanning title row makes "
    "merged_cells true, while multi-line cell contents alone do not [table.merged_cells].",
    "Rows are counted as printed, so the appendix table's repeated row number 3 gives thirteen "
    "rows for twelve numbers [table.rows].",
    "Choropleths here key their classes with the words Low and High and no numbers, so "
    "printed_numbers is false on both map rows [geometry.printed_numbers].",
    "A picture with no axes at all - the two function maps - still prints no numbers and is "
    "recorded with printed_numbers false [geometry.printed_numbers].",
    "A caption that reaches the layer only after its subscripts are split to their own line is "
    "quoted with the subscript run fused into the token the page prints, e.g. 'Impact Index Ei' "
    "[mention.lead_sentence].",
    "An exhibit first named a page after it prints takes a negative lead_pages, so Figure 6 "
    "records -1 against a first mention on p14 [mention.lead_pages].",
    "An exhibit the prose never names records count 0 with a null first_page and no style "
    "spelling - Figures 1, 2, 3 and 8 here [mention.count].",
    "A caption printed inside a sentence is recorded as printed and the split paragraph declared "
    "in the row note rather than repaired [place.section_path].",
]

NOTE = """Paper 85, Team 34985. Fourteen measured regions over twelve of the twenty pages of what the
running head calls nineteen, all fourteen accounted for: eleven figure rows, three table rows, no
refusals, so unaccounted is zero and nothing is left unresolved. The paper numbers nine figures -
1 through 9 with no gap - and not one table: the word "Table" never appears in the text layer, and
the three grids are named by a title row inside the box or by the appendix heading above it.

The region pass needed no argument on this paper, which is unusual in this lane. Every region is
either a framed, pasted chart or a ruled grid, and the page-wide vector bands that wrecked papers
72 and 73 do not appear at all: the eight prose pages carry no closed rule box, so they never
become regions. What the pass did do is split one printed figure into two, and the record follows
it - Figure 5's (a) and (b) halves are two pasted bitmaps side by side with their own subcaptions
and a single caption under both, so two rows carry the identical caption text.

The repetition on the summary sheet is the finding this paper contributes to the census. The
bitmap on p1 - COST at the foot, thirty arrows through the factor boxes into "Socioeconomic
Development Index" and "Ecological Impact Index" - is the same map Figure 6 prints on p13, drawn
again with slightly different factor labels and no number, no caption and no citation. The paper
therefore carries a second, invisible copy of its central diagram where a reader is most likely to
see it, and never refers back to it from the body.

The captions fail in three different ways. Figure 5's caption and Figure 2's caption reach the
text layer with every space dropped, so both are typed from the crop - "Figure2:
GraphofthetheoreticalincomedistributionI(x)andadjustedincomedistribution" is what the layer
holds, and its last token "A(x)" is pushed onto a second line. Figure 6's caption is set inside a
sentence, with the paragraph ending p12 on "we created a map of the main factors that influence
the Socioeconomic" and resuming under the caption with "and Ecological Indices of Zambia." And
Figure 4's caption welds its two panels into one run-on line with no space between the subscript
"i" and the panel letter "B:", while Figure 9's caption promises panels that are "respectively"
D_i, E_i and S but the picture carries no panel letters, no axis titles and no y numbers at all.

What the pictures show, all of it read off the crops. Figures 1 and 3 are the same world
choropleth in the same five-step ramp, keyed inside the lower left with the words Low and High and
no numbers, and both leave their no-data countries white while the prose says they are coloured
grey. Figure 4 pairs a ninety-point tradeoff scatter with four bars whose colour code is only
recoverable from the scatter's legend. Figure 5's two halves are three-by-two blocks of
automata snapshots - wealth down the left, population down the right, Initial, 10 Years and 20
Years on the arrow between them - with class breaks printed nowhere. Figure 7 is the one honest
chart on the paper: three marked curves against a labelled investment axis, an inside legend in
the Greek alpha, and a vertical rule at the 1.2 billion budget the prose points to. Figure 8 puts
six legend entries over seven groups of paired bars and prints each alpha twice, so solid against
hatched is the only cue for decade one against decade two, and its hatched 0.5 swatch is blue
while the bars it keys are pink.

The appendix grid carries the paper's arithmetic and its arithmetic errors together: thirteen
rows for twelve numbers because row 3 is printed twice, and the birth-rate equation arriving as
".070428-5.62ln(x)" with the leading 0.5 of 0.70428 gone. Row 12's equation is a stack of three
fractions that overruns its column and prints without the summation that the prose describes.

Citation is the weakest block of this paper. Four of the nine numbered figures - 1, 2, 3 and 8 -
are never named in the prose at all; Figure 4 gets one pointer on its own page, Figure 5 two,
Figure 7 two, Figure 9 one, and Figure 6 is named twice but both times a page or more away from
the art, once on p14 with a negative lead and once on p20 from the appendix. The three grids are
cited only as "the table" and "the above table" - no grid on this paper ever carries a number, so
there is nothing to cite."""

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT.get("layout_sha256") or LAYOUT.get("sha256", ""),
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": [],
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc85-payload.json"
out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "rules", len(RULES))
print("wrote", out)
