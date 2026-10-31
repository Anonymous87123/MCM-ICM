"""Hand census of P-B-2016-42745-4dc9ed2b (Team 42745, 26 pages, 43 measured regions).

A space-debris economics paper. Forty-three measured regions resolve into TWENTY-FIVE FIGURE ROWS,
THREE TABLE ROWS and FIFTEEN EXCLUSIONS.

  p2  r1  --         scatter              the debris matrix, executive-summary teaser
  p8  r1  --         table-grid           the notations table, 2 by 16, unruled box, unnumbered
  p13 r2  Figure 1   histogram            catalogued density against altitude, 3 overlaid curves
  p13 r1  Figure 2   line                 the gamma p.d.f.
  p13 r4  Figure 3   scatter              the debris shell over a NASA Earth image
  p13 r3  Figure 4   heatmap-or-contour   the 3D p.d.f. seen from above, colour bar 0 to 0.035
  p13 r5-r8 --       exclusions           four image tiles inside Figure 4
  p14 r1  Figure 5   scatter              the debris matrix again, twice the size
  p16 r1  Figure 6   line                 satellites launched, 2001 to 2015
  p17 r1  Figure 7   bar                  profits v.s. debris left, land-based alternative
  p17 r2  Figure 8   scatter              the debris matrix again, a quarter of the size
  p18 r1  Figure 9   bar                  the same chart for the space-based alternative
  p18 r2  Figure 10  scatter              the debris matrix again
  p18 r3  Figure 11  bar                  the same chart for the two alternatives combined
  p18 r4  Figure 12  scatter              the debris matrix again
  p19 r1  Figure 13  scatter              the matrix at a 4% increase rate
  p19 r2  Figure 14  scatter              at 3%
  p20 r1  Figure 15  scatter              at 2%
  p20 r2  Figure 16  scatter              at a logarithmic increase rate
  p21 r1-r4 Figure 17-20 bar              accumulated profits for rocket lifetimes 3, 6, 9, 12
  p22 r1-r4 Figure 21-24 bar              accumulated profits for alpha 6%, 5%, 4%, 3%
  p23 r1  --         table-grid           the payoff matrix, 4 by 4
  p23 r2  --         table-grid           the new payoff matrix, 4 by 4

THE CAPTION IS A NUMBER AND NOTHING ELSE. Twenty-four figures print a label; eighteen of those are
the bare form "Figure N", one appends a citation marker ("Figure 1 [12]"), one appends a data-source
credit ("Figure 6 (Data Source: Space-Track.org)") and four append the parameter the run used
("Figure 13, 4%" ... "Figure 16, logarithm"). Not one caption describes its exhibit. The only
descriptive text lives INSIDE the plotting frame, where MATLAB drew it, and the three tables carry
no caption and no number at all.

ONE PICTURE IS PRINTED NINE TIMES. The 1000 by 1000 debris matrix - a grey grid, axes X and Y from
0 to 1000, a central void, a dense ring at a radius of 700 to 800 cells - appears as the executive
summary's teaser, as Figure 5, as Figures 8, 10 and 12 beside the profit charts, and as Figures 13
to 16 at four increase rates. Every one of the nine boxes has the same aspect, 1.117, at four
different printed sizes (0.179, 0.088, 0.064 and 0.045 of the page).

The exhibits are cited by nothing. Only Figures 1, 2, 3, 4 and 5 are named by a sentence, and all
five are named on the two pages they print on; Figures 6 to 24 are pointed at only by phrases such
as "the results are presented in the following figures", "present the corresponding figures" and
"The figures presented above are also developed by using the combined alternative", none of which
names a figure.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2016-42745-4dc9ed2b"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]
        KIND[(_pg["page"], _i)] = _r["kind"]

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


def place(page: int, reg: int, kind: str, path: list[str], order: int = 1) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": order,
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


def caption(verbatim: str, numbering: str = "Figure N", position: str = "below",
            variables: int = 0, sentences: int = 1) -> dict:
    """Caption block. `verbatim` is what the page prints under the exhibit."""
    return {"verbatim": schema.norm(verbatim), "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": sentences, "units": False,
            "variables": variables > 0, "variable_count": variables,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def no_caption() -> dict:
    """The block for an exhibit that prints no caption at all: the p2 teaser and the three tables."""
    return {"verbatim": "", "numbering": "none", "words": 0, "sentences": 0, "units": False,
            "variables": False, "variable_count": 0, "conditions": False, "concludes": False,
            "voice": "none", "position": "below"}


def geometry(family: str, panels: int = 1, layout: str = "1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = False,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


def head(page: int, prefix: str) -> str:
    """The indexed heading on `page` whose label starts with `prefix`, exactly as printed."""
    for h in CTX["headings"]:
        if h["page"] == page and h["label"].startswith(prefix):
            return h["label"]
    raise SystemExit(f"no heading on p{page} starting {prefix!r}")


S_ABS = ["Executive Summary"]
S_32 = [head(7, "3 Terminologies"), head(8, "3.2 Notations Table")]
S_52 = [head(12, "5 Model Two"), head(12, "5.2 Some Thoughts")]
S_53 = [head(12, "5 Model Two"), head(14, "5.3 Establishing")]
S_56 = [head(12, "5 Model Two"), head(15, "5.6 Satellites")]
S_61 = [head(16, "6 Results"), head(16, "6.1 Land-Based")]
S_62 = [head(16, "6 Results"), head(17, "6.2 Space-based")]
S_63 = [head(16, "6 Results"), head(18, "6.3 The Combination")]
S_71 = [head(19, "7 Some"), head(19, "7.1 Scenario 1")]
S_72 = [head(19, "7 Some"), head(20, "7.2 Scenario 2")]
S_73 = [head(19, "7 Some"), head(21, "7.3 A Sensitivity")]
S_8 = [head(22, "8 A Game Theory")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_PRINTED = schema.printed_lines(PID)
for _group in (S_ABS, S_32, S_52, S_53, S_56, S_61, S_62, S_63, S_71, S_72, S_73, S_8):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN and schema.norm(_label) not in _PRINTED:
            raise SystemExit(f"section label is neither an indexed heading nor a printed line: "
                             f"{_label!r}")

# The printed labels. Eighteen are the bare "Figure N"; the exceptions keep whatever they append.
CAP1 = caption("Figure 1 [12]")
CAP6 = caption("Figure 6 (Data Source: Space-Track.org)")
CAP13 = caption("Figure 13, 4%")
CAP14 = caption("Figure 14, 3%")
CAP15 = caption("Figure 15, 2%")
CAP16 = caption("Figure 16, logarithm")


def cap(n: int) -> dict:
    return caption(f"Figure {n}")

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_block: dict, cap_src: str, mention: dict,
           section: list[str], note: str, geo: dict | None = None, number: str = "",
           section_kind: str = "other", confidence: str = "high", order: int = 1) -> None:
    ITEMS.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)], "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap_block["verbatim"],
        "caption": cap_block, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section, order),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    })


def table(page: int, reg: int, section: list[str], note: str, spec: dict,
          section_kind: str = "other", order: int = 1) -> None:
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)],
        "family": "table-grid", "caption_source": "none", "caption_verbatim": "",
        "caption": no_caption(), "table": spec,
        "place": place(page, reg, section_kind, section, order),
        "mention": uncited(), "note": note, "confidence": "high",
    })


def exclude(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note})


# ============================================================ the executive summary teaser
figure(2, 1, "scatter", no_caption(), "none", uncited(), S_ABS,
       "A teaser on the second page of the paper, not a result: a 1000 by 1000 lattice of small grey "
       "dots with a circular void about 300 cells across at its centre and a dense black ring at a "
       "radius of roughly 700 to 800 cells, thinning outward. The only text on it is the in-plot "
       "title 'Simulation Space Debris Distribution' and the cell indices X and Y from 0 to 1000; no "
       "colour bar, no legend, no annotation, no unit. It prints three pages before the body's first "
       "figure and it is the same plot as Figure 5, printed here at 0.088 of the page against that "
       "row's 0.179, with identical box aspect (1.117). The sentence that introduces it names no "
       "exhibit - 'The simulated debris distribution is as follows:' - and it is the only exhibit in "
       "the paper that sits in an abstract.",
       geometry("scatter"), section_kind="abstract")

# ============================================================ the notations table
table(8, 1, S_32,
      "The paper's only table of definitions: two columns headed 'Symbols' and 'Meanings' and "
      "fifteen body rows - N_t net income, R_t revenue from insurance, C_t total cost, NT cumulative "
      "net income, n_t satellites launched, w the guaranteed amount, alpha the actuarial constant, "
      "C1_t and C2_t the two cost terms, p_t price, q_t quantity trapped, Pr(t) the collision chance, "
      "delta the compensating parameter, Q_t debris in space, epsilon the removal per trapper. "
      "Ruling: heavy rules above the header, under it and at the foot, a thin rule between EVERY "
      "body row, and one full-height vertical rule between the two columns - no outer box and no "
      "side strokes beyond that single interior vertical. The Symbols column is centred italic "
      "mathematics. NO CAPTION AND NO NUMBER: the table is introduced only by 'The following table "
      "provides meanings of important notations used in our models.', and only the last cell's "
      "meaning ends with a full stop.",
      {"rows": 16, "cols": 2, "header_rows": 1, "rule_style": "vertical-rules", "zebra": False,
       "merged_cells": False, "diagonal_header": False, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 0, "text_cols": 2, "width": "full",
       "orientation": "portrait", "continued": False, "note_sentence": ""},
      section_kind="symbols")

# ============================================================ 5.2: the four p13 figures
figure(13, 2, "histogram", CAP1, "text-layer",
       cited(13, 13, ["Figure 1"], 2,
             "Figure 1 shows the spatial density of debris in accordance with altitude in LEO",
             "figure-n-shows"),
       S_52,
       "A stepped histogram of the catalogued population against altitude: a thick blue stair-step "
       "series across 'Altitude (km)' 200 to 1900 on an ordinate 'Spatial Density (no./km3)' running "
       "0 to 6.5E-08, rising to a double peak near 800 and 850 km, collapsing to almost nothing by "
       "1200 km and showing a second small cluster near 1400 to 1500 km. Three smooth curves are "
       "laid over it - black (FR + Iridium + Cosmos fragments), red (FY-1C fragments) and green "
       "(Iridium + Cosmos fragments) - keyed by a four-entry legend inside the frame at the top "
       "right, blue being 'All objects'. A red-outlined text box inside the plot area reads "
       "'Cataloged objects only: as of January 2013'. The figure prints no title of its own, and its "
       "caption is the number plus a citation marker, 'Figure 1 [12]', with no describing word.",
       geometry("histogram", legend="inside"), "1", section_kind="other", order=1)

figure(13, 1, "line", cap(2), "text-layer",
       cited(13, 13, ["figure 2"], 2,
             "The shape of the curves in Figure 1 is analogous with the probability density function "
             "of gamma distribution, shown in figure 2", pattern="parenthetical"),
       S_52,
       "The gamma p.d.f. the whole model is built on: one smooth black curve peaking at about 0.038 "
       "at x = 30 and decaying to zero by x = 80, against 'x' 0 to 90 and 'probability' 0 to 0.045, "
       "with the in-plot title '2D Gamma P.D.F' and a one-entry legend inside the frame at the top "
       "right reading 'gamma'. NO PARAMETER IS PRINTED ON THE FIGURE: the shape and rate parameters "
       "the text names can only be read back off the curve's peak. This is also the only exhibit "
       "cited in the lower case - 'shown in figure 2' - in a paper that otherwise capitalises.",
       geometry("line", legend="inside"), "2", order=2)

figure(13, 4, "scatter", cap(3), "text-layer",
       cited(13, 13, ["Figure 3"], 1,
             "Figure 3 is the three dimensional spread of debris, denoted by black dots, in LEO [12]"),
       S_52,
       "The three-dimensional spread of debris over a pale blue Earth: a dense black shell of points "
       "hugging the globe, thinning outward into scattered dots, with no axes, no scale, no legend "
       "and no title. A NASA credit line, '(Source: Image of the day, NASA, 2009)', prints in italic "
       "below the image and immediately above its 'Figure 3' label, so the credit belongs to the "
       "Earth picture underneath the data - it is the only exhibit in the paper that carries a source "
       "credit. The exhibit therefore mixes a borrowed raster with the paper's own point data and "
       "prints nothing that separates the two.",
       geometry("scatter"), "3", order=3)

figure(13, 3, "heatmap-or-contour", cap(4), "text-layer",
       cited(13, 13, ["Figure 4"], 1,
             "Thus, we use the diameter of the earth plus the thickness of the atmosphere from the "
             "3D gamma p.d.f. and derive Figure 4"),
       S_52,
       "The same p.d.f. seen from above: a colour-mapped annulus titled 'Spatial Gamma P.D.F.' on a 0 "
       "to 100 by 0 to 100 cell grid, dark blue inside a circle of radius 30 cells, a hot red band at "
       "a radius of about 45 to 55 cells, cooling outward and running into the top edge of the frame, "
       "with a colour bar on the right from 0 to 0.035 in steps of 0.005. Neither axis carries a unit "
       "- x and y are cell indices - and nothing states what the colour means beyond the title. The "
       "four image tiles the extractor measured within this figure's area are declared exclusions, "
       "not four more exhibits; the paper derives it in one sentence from the 3D p.d.f. without "
       "saying what was integrated.",
       geometry("heatmap-or-contour", colorbar=True), "4", order=4)

# ============================================================ 5.3: the matrix at full size
figure(14, 1, "scatter", cap(5), "text-layer",
       cited(14, 14, ["Figure 5"], 1,
             "The simulated scattering of space debris can be vividly shown in the following "
             "Figure 5, Figure 5"),
       S_53,
       "The debris matrix as the paper renders it: the same 1000 by 1000 cell picture as the "
       "executive summary's teaser, printed here at about twice that size (0.179 of the page) with "
       "the same frame aspect, axes 'X' and 'Y' from 0 to 1000, a grey grid, a central void and a "
       "dense ring of points at a radius of roughly 700 to 800 cells, under the in-plot title "
       "'Simulation Space Debris Distribution'. No legend and no colour bar. Its caption is 'Figure "
       "5', and the pointer sentence prints the label twice - '... can be vividly shown in the "
       "following Figure 5, Figure 5' - because the sentence's own trailing label is immediately "
       "followed by the printed one.",
       geometry("scatter"), "5", section_kind="model")

# ============================================================ 5.6: the launch record
figure(16, 1, "line", CAP6, "text-layer", uncited(), S_56,
       "The historical launch record the model starts from: about fifteen round markers at annual "
       "spacing from 2001 to 2015 joined by a line, each marker printing its value above it, over "
       "'Year' and an ordinate simply labelled 'Amount' from 0 to 300, in-plot title 'The Amount of "
       "Satellites launched', with a thin dotted straight trend drawn across the series that no "
       "legend keys. THE SERIES DOES NOT SHOW THE MODEL'S OWN ASSUMPTION: the text says 'The "
       "initially quantity of orbiting satellites is set to 110, and this number will increase by 5% "
       "each year', which would be a monotone rise, while the plotted record is the observed "
       "catalogue instead - it falls away to 40 and climbs back to 150 - so the exhibit and the "
       "sentence describe different objects, and the dotted trend matches neither. The caption's "
       "second line, '(Data Source: Space-Track.org)', is the only attribution any exhibit here gets.",
       geometry("line", labels=True, numbers=True), "6", section_kind="model")

# ============================================================ 6.1: land-based alone
figure(17, 1, "bar", cap(7), "text-layer", uncited(), S_61,
       "A bar-and-line chart on twin ordinates: blue bars of accumulated profit per year against "
       "'Accumulated Profits (billions)' on the left axis, -2 to 10 in steps of 2, and an orange "
       "dashed series of debris on the right axis, 11500 to 12500, which ends in a large arrowhead "
       "at year 15. The two series are keyed by an unboxed legend ABOVE the data frame, a bar swatch "
       "beside 'Accumulated Profits (billions)' and a dashed-arrow swatch beside 'Debris left'. THE "
       "TITLE AND THE AXIS NAME THE SAME SERIES DIFFERENTLY - the title reads 'The Profits v.s. the "
       "Number of Debris remaining' and the right axis reads 'Debris left' - and the right axis "
       "prints no unit at all. The first eight bars are negative, which is the net loss the prose "
       "reads off the exhibit, and the abscissa prints only 1 to 15 although the prose's window is "
       "2016 to 2030.",
       geometry("bar", legend="above"), "7", section_kind="result", order=1)

figure(17, 2, "scatter", cap(8), "text-layer", uncited(), S_61,
       "The debris matrix again, printed beside the profit chart at a quarter of Figure 5's size "
       "(0.045 of the page, the same 1.117 frame aspect): same 1000 by 1000 frame, same grey grid, "
       "same ring, same in-plot title 'Simulation Space Debris Distribution', no legend and no colour "
       "bar. Nothing on the page says which simulation year or which alternative it belongs to, and "
       "the prose names no figure - the section points at its exhibits only with 'the results are "
       "presented in the following figures'.",
       geometry("scatter"), "8", section_kind="result", order=2)

# ============================================================ 6.2: space-based alone
figure(18, 1, "bar", cap(9), "text-layer", uncited(), S_62,
       "The same chart template for the space-based alternative: bars of accumulated profit against "
       "a left axis now running 0 to 30 in steps of 5, the same orange dashed debris series on a "
       "right axis 11500 to 13500, the same unboxed legend above the frame, the same title 'The "
       "Profits v.s. the Number of Debris remaining' and the same disagreement with its own right "
       "axis label 'Debris left'. Nothing on the exhibit distinguishes it from Figure 7 except the "
       "axis numbers, so the two alternatives are compared by a reader who has to remember which "
       "page they were on.",
       geometry("bar", legend="above"), "9", section_kind="result", order=1)

figure(18, 2, "scatter", cap(10), "text-layer", uncited(), S_62,
       "The debris matrix a third time, the same 0.045-of-page box as Figure 8 with the identical "
       "frame aspect, axes, grid and in-plot title. The prose beside it reads a sharp rise over the "
       "last five years off the picture, and nothing on the picture dates it or gives it a count.",
       geometry("scatter"), "10", section_kind="result", order=2)

# ============================================================ 6.3: the two combined
figure(18, 3, "bar", cap(11), "text-layer", uncited(), S_63,
       "The combined alternative's profit chart: the same template again, left axis labelled "
       "'Accumulated Profits (billions)' with odd ticks from -3 to 17, the dashed debris series on a "
       "right axis 7000 to 14000, legend above the frame, and the same title/axis mismatch "
       "('remaining' against 'left'). This is the chart whose result the paper adopts - the prose "
       "reads a net profit of nearly 16 billion at year 15 off it - and no value is printed on the "
       "bar it points at, so the 16 has to be read off the ticks.",
       geometry("bar", legend="above"), "11", section_kind="result", order=3)

figure(18, 4, "scatter", cap(12), "text-layer", uncited(), S_63,
       "The debris matrix a fourth time, in the same quarter-page box as Figures 8 and 10: identical "
       "frame, identical in-plot title, no legend, no colour bar, no date and no total. Four of this "
       "paper's exhibits are the same picture at the same size, three of them on the two pages of "
       "section 6, and none of them is labelled with the simulation run it shows.",
       geometry("scatter"), "12", section_kind="result", order=4)

# ============================================================ 7.1: four increase rates
def matrix_run(page: int, reg: int, cap_block: dict, order: int, which: str,
               extra: str = "") -> None:
    figure(page, reg, "scatter", cap_block, "text-layer", uncited(), S_71,
           f"The debris matrix as it renders at {which}: the same square template as Figure 5 - "
           f"identical frame, grey grid, axes X and Y from 0 to 1000, in-plot title 'Simulation "
           f"Space Debris Distribution' with an increase-rate clause appended - distinguishable only "
           f"by the density of the point cloud. THE PARAMETER IS PRINTED AS A SUFFIX ON THE CAPTION "
           f"AND NOWHERE ELSE that is legible: the in-plot title is too small at printed size to "
           f"read, the axes carry cell indices and no count, and the prose introduces all four with "
           f"'present the corresponding figures', which names no figure. {extra}",
           geometry("scatter"), cap_block["verbatim"].split(",")[0].split()[-1],
           section_kind="sensitivity", order=order)


matrix_run(19, 1, CAP13, 1, "an increase rate of 4 percent",
           "It is one of a pair printed side by side on the same page, two captions and nothing "
           "between them, so the reader is asked to compare densities by eye across two pictures "
           "that print no count, no total and no scale.")
matrix_run(19, 2, CAP14, 2, "an increase rate of 3 percent")
matrix_run(20, 1, CAP15, 1, "an increase rate of 2 percent",
           "It is the first thing printed on its page - the figure pair sits at the very top, above "
           "all of the prose - while the discussion it belongs to began at the foot of the previous "
           "page.")
matrix_run(20, 2, CAP16, 2, "a logarithmic increase rate",
           "This is the sparsest of the four point clouds, which is the one thing that distinguishes "
           "it from its three companions and which agrees with the numbers the prose quotes for it "
           "(debris down from 6374 to 5313 across the step, the smallest of the four reductions).")

# ============================================================ 7.2: rocket lifetimes
def profit_bars(page: int, reg: int, n: int, title: str, ticks: str, order: int,
                tail: str = "") -> None:
    figure(page, reg, "bar", cap(n), "text-layer", uncited(), S_72,
           f"A column chart of accumulated profit against year, in-plot title '{title}', left axis "
           f"'Profits (Billions)' with ticks {ticks}, abscissa 'Years' from 1 to 15, no legend, no "
           f"gridline, and no value printed on any bar - the only numbers on the exhibit are the "
           f"axis ticks. The caption below it is nothing but 'Figure {n}', and the title is a "
           f"variable name with an underscore rather than a sentence, so the parameter that "
           f"distinguishes this chart from the other seven is printed inside the frame only. {tail}",
           geometry("bar"), str(n), section_kind="sensitivity", order=order)


profit_bars(21, 1, 17, "Accumulated Profits_lifetime_3", "-5 to 25 in steps of 5", 1)
profit_bars(21, 2, 18, "Accumulated Profits_lifetime_6", "-5 to 25 in steps of 5", 2)
profit_bars(21, 3, 19, "Accumulated Profits_lifetime_9", "-5 to 25 in steps of 5", 3,
            "Same frame and same scale as its three companions, so the four lifetime runs are the "
            "first set in the paper that can be read against one another at a glance.")
profit_bars(21, 4, 20, "Accumulated Profits_lifetime_12", "-5 to 25 in steps of 5", 4,
            "The four charts of this page carry the section's whole result - the prose reads a "
            "0.38 billion rise per extra year of lifetime off them - and none of them prints a "
            "value on a bar or a scale beyond its nine ticks.")

# ============================================================ 7.3: the alpha sweep
profit_bars(22, 1, 21, "Accumulated Profits_alpha_6%", "-5 to 30 in steps of 5", 1)
profit_bars(22, 2, 22, "Accumulated Profits_alpha_5%", "-5 to 30 in steps of 5", 2)
profit_bars(22, 3, 23, "Accumulated Profits_alpha_4%", "-5 to 30 in steps of 5", 3)
profit_bars(22, 4, 24, "Accumulated Profits_alpha_3%", "-5 to 30 in steps of 5", 4,
            "The alpha sweep runs downward - 6, 5, 4, 3 - while the lifetime page above runs "
            "upward, and neither page prints anything that orders its four charts but their "
            "position.")

# ============================================================ 8: the two payoff matrices
table(23, 1, S_8,
      "The game's payoff matrix as a 4 by 4 grid: a stub column headed 'Player1/2', three column "
      "heads ('Do nothing', 'Remove some', 'Remove considerably') and three row stubs ('Uninsured', "
      "'Half insured', 'Fully insured'), with nine cells each holding a pair like '(-45,0)'. Ruling: "
      "one vertical rule between the stub column and the payoff columns and one horizontal rule "
      "under the header row, and nothing else - no top rule, no foot rule, no box, no interior "
      "lines, no zebra. THE TWO NASH EQUILIBRIA THE PROSE NAMES ARE MARKED ONLY BY UNDERLINING: "
      "'(-21,-8.4)' at (half insured, remove considerably) and '(-27,-11.7)' at (fully insured, "
      "remove some) are underlined, and not one line of text says what an underline means. No unit "
      "is printed anywhere in either matrix - the pairs are billions of profit and of compensation, "
      "which the reader carries over from the axes of Figures 7 to 12 - and no caption or number "
      "stands above or below it.",
      {"rows": 4, "cols": 4, "header_rows": 1, "rule_style": "vertical-rules", "zebra": False,
       "merged_cells": False, "diagonal_header": True, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 3, "text_cols": 1, "width": "half",
       "orientation": "landscape", "continued": False, "note_sentence": ""},
      section_kind="other", order=1)

table(23, 2, S_8,
      "The same matrix recomputed as the paper's new payoff matrix after the proposed standards: "
      "identical 4 by 4 structure, ruling and cell style as the matrix above, with different values "
      "in every cell, and exactly ONE cell underlined, '(-19.5,-3.3)' at (half insured, remove "
      "considerably) - the single Nash equilibrium the prose claims the new standards shift the game "
      "to. The pair of matrices is the only exhibit pair in the paper whose read-out is a marking "
      "convention rather than a shape, and the convention is never stated. Both matrices repeat the "
      "same stub header 'Player1/2' without ever saying who player 1 and player 2 are; the prose has "
      "to be read to learn that they are the launch operator and the insurance provider.",
      {"rows": 4, "cols": 4, "header_rows": 1, "rule_style": "vertical-rules", "zebra": False,
       "merged_cells": False, "diagonal_header": True, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 3, "text_cols": 1, "width": "half",
       "orientation": "landscape", "continued": False, "note_sentence": ""},
      section_kind="other", order=2)

# ============================================================ exclusions
for _r in (1, 2, 3, 4, 5):
    exclude(6, _r, "not-an-exhibit",
            "a block of the Introduction's prose that the extractor boxed because its text lines are "
            "drawn as paths: the words are the discussion of the land-based methods and of the laser "
            "broom, with no picture, rule, caption or number in it")
for _r in (1, 2, 3, 4, 5):
    exclude(7, _r, "not-an-exhibit",
            "the same kind of boxed prose, here the discussion of Huff-and-Puff, snagging and nets - "
            "body text, not an exhibit")
for _r in (5, 6, 7, 8):
    exclude(13, _r, "fragment-of-other",
            "one of the four image tiles that make up Figure 4's own picture: the exhibit is recorded "
            "once on the figure's own region above it, so this tile is a fragment of that exhibit and "
            "not a fifth figure")
exclude(25, 1, "not-an-exhibit",
        "the References block: a citation list whose hanging indents and rules counted as drawn "
        "paths; it is apparatus, not an exhibit")

RULES = [
    "Measure first, then read the pixels: forty-three measured regions resolve into twenty-five "
    "figure rows, three table rows and fifteen exclusions, and no region is counted twice "
    "[place.doc_order].",
    "The caption is a number and nothing else: twenty-four figures print a label and eighteen of "
    "them print the bare form 'Figure N', while Figure 1 appends a citation marker, Figure 6 a "
    "data-source credit and Figures 13 to 16 the parameter their run used - so no row's caption "
    "block is built out of anything but what prints below the exhibit [caption.words].",
    "The plotting program's title is not a caption: nine rows print 'Simulation Space Debris "
    "Distribution' inside their own frame and eight print '_lifetime_N' or '_alpha_N%' there, and "
    "every one of those titles is carried in the note and in the geometry instead of being promoted "
    "to a caption [caption.verbatim].",
    "A bare pointer is not a citation: 'the results are presented in the following figures', "
    "'present the corresponding figures' and 'The figures presented above are also developed by "
    "using the combined alternative' name no exhibit, so twenty figure rows and all three tables "
    "record no citation at all [mention.count].",
    "An abstract can print an exhibit: the teaser on p2 is recorded as its own row with no caption "
    "and no citation because the same plot is printed again as Figure 5, and both printings are "
    "measured regions [place.page_zone].",
    "A region inside a region is a fragment of the exhibit, not a second exhibit: the four image "
    "tiles measured inside Figure 4's frame are exclusions, and the nine prose blocks on pp6-7 and "
    "the references block on p25 are exclusions because they carry no picture [place.area_frac].",
    "Placement follows the heading index, which indexed every heading this paper prints including "
    "the one whose label carries mathematics; p20 prints two figures at its very top and the "
    "'7.2 Scenario 2' heading at its foot, so those two rows belong to 7.1 [place.section_path].",
    "A caption suffix that names a parameter stays in the caption: 'Figure 13, 4%' keeps the 4%, "
    "because the increase rate is the only thing that distinguishes the four point clouds of "
    "pp19-20 from one another [caption.numbering].",
]

NOTE = """\
Paper 96, Team 42745, a space-debris removal and insurance model. Twenty-six pages, forty-three
measured regions on fifteen of them, resolving into TWENTY-FIVE FIGURE ROWS, THREE TABLE ROWS and
FIFTEEN EXCLUSIONS. Unaccounted zero. Ten of the exclusions are prose blocks the extractor boxed
because their text lines are drawn as paths, four are the image tiles that make up one figure, and
one is the references list.

The caption situation is the starkest in the lane so far. Twenty-four figures print a label and
eighteen of those are the bare form "Figure N" - no description, no unit, no condition, nothing.
Figure 1 appends a citation marker ("Figure 1 [12]"), Figure 6 appends a data-source credit
("Figure 6 (Data Source: Space-Track.org)"), and Figures 13 to 16 append the parameter their run
used ("Figure 13, 4%" through "Figure 16, logarithm"). Not one caption in the paper contains a word
describing its exhibit, which means the only identifying text is whatever MATLAB drew inside the
frame. The three tables carry no caption and no number at all: the notations table is introduced
only by "The following table provides meanings of important notations used in our models." and the
two payoff matrices are introduced by the two sentences that precede them.

One picture is printed nine times. The 1000 by 1000 debris matrix - grey grid, axes X and Y from 0
to 1000, a central void about 300 cells across, a dense ring at a radius of 700 to 800 cells, title
"Simulation Space Debris Distribution" inside the frame - appears as the executive summary's teaser
on p2, as Figure 5 at full size on p14, as Figures 8, 10 and 12 beside the profit charts at a
quarter of that size, and as Figures 13 to 16 at four increase rates on pp19-20. All nine boxes have
the same aspect, 1.117, at four different printed sizes. The four rate variants are distinguishable
only by the density of the point cloud and by the suffix on the caption; the in-plot title's
increase-rate clause is too small at printed size to read, and the axes carry cell indices with no
count, no total and no date anywhere.

Citation is close to absent. Only Figures 1, 2, 3, 4 and 5 are named by a sentence, all five on the
two pages where they print - "Figure 1 shows the spatial density of debris in accordance with
altitude in LEO; Figure 3 is the three dimensional spread of debris, denoted by black dots, in LEO",
"shown in figure 2" in the lower case, "and derive Figure 4", and "can be vividly shown in the
following Figure 5, Figure 5" where the pointer's own trailing label collides with the printed one.
Figures 6 to 24 are pointed at only by phrases that name nothing: "the results are presented in the
following figures", "present the corresponding figures", "The figures presented above are also
developed by using the combined alternative". A reader who wants to know which of the eight
identical profit charts is the 9-year run has to read the title inside the frame.

Two exhibits contradict the sentences beside them. Figure 6 prints the observed launch catalogue -
markers falling from 115 to 40 and climbing back to 150 between 2001 and 2015, with a dotted trend
line that no legend keys - while the text says the model starts at 110 satellites and "will increase
by 5% each year"; a monotone 5% growth is not what the picture shows, and the dotted trend matches
neither. Figure 7 and its three twins carry the title "The Profits v.s. the Number of Debris
remaining" over a right axis labelled "Debris left", name the same series two different ways, and
print no unit on that axis at all. Both defects are in what the exhibit says, not in how it is
drawn.

Design. The two payoff matrices on p23 are 4 by 4 grids with a single vertical rule between the stub
column and the payoff cells and a single rule under the header - no box, no interior lines - and
their read-out depends entirely on underlining: two cells are underlined in the first matrix, which
are exactly the two Nash equilibria the prose names, and one cell is underlined in the second, which
is the single equilibrium the new standards are claimed to produce. No line of text explains the
convention, and neither matrix prints a unit, so the pairs are billions of profit and of
compensation only if the reader carries that over from the axes of Figures 7 to 12. The notations
table on p8 rules every body row and closes no box.

Families: bar 11, scatter 10, line 2, histogram 1, heatmap-or-contour 1, table-grid 3.
"""

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc96-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
