"""Hand census of P-A-2015-32722-037c369c (Team 32722, 39 pages: 36 numbered plus a 2-page memo).

Thirty-three measured regions over seventeen pages, all of them exhibits but one: 29 figure
boxes, 3 tables, and the p1 title band. Nothing unresolved.

   p1  r1  title band, two rules and the paper's title          excluded not-an-exhibit
   p4  r1  Figure 1   colourised electron micrograph of the virus
   p5  r1  Figure 2   five-nation locator map of West Africa
   p8  r1  Figure 3   three-level nested schematic with a compartment inset
   p10 r1  Figure 4   the state-transition compartment graph
   p11 r1  Table 1    eleven fitted parameters, two country columns
   p13 r1  Table 2    four modified-gravity constants
   p17 r1  Figure 5a  single-city, 5 per cent initial latent
   p17 r2  Figure 5b  single-city, 20 per cent initial latent
   p19 r1  Figure 6a  city of 35,000
   p19 r2  Figure 6b  city of 350,000
   p20 r1  Figure 7a  medicine efficacy 2
   p20 r2  Figure 7b  medicine efficacy 5
   p20 r3  Figure 7c  medicine efficacy 10
   p21 r1  Figure 8a  100 vaccines every five days
   p21 r2  Figure 8b  1,000 vaccines every five days
   p21 r3  Figure 8c  10,000 vaccines every five days
   p21 r4  Figure 8d  20,000 vaccines every five days
   p22 r1  Table 3    the four toy-model cities
   p23 r1  Figure 9a  rural infection, vaccine to rural
   p23 r2  Figure 9b  rural infection, vaccine to urban
   p23 r3  Figure 9c  urban infection, vaccine to urban
   p23 r4  Figure 9d  urban infection, vaccine to rural
   p25 r1  Figure 10a rural infection, cure to rural
   p25 r2  Figure 10b rural infection, cure to urban
   p25 r3  Figure 10c urban infection, cure to urban
   p25 r4  Figure 10d urban infection, cure to rural
   p26 r1  Figure 11a movement factor k = 1
   p26 r2  Figure 11b movement factor k = 5
   p27 r1  Figure 12a all four cities in Liberia
   p27 r2  Figure 12b all four cities in Sierra Leone
   p27 r3  Figure 12c two cities in each
   p32 r1  Figure 13  the geography-based network on its basemap

No declared gaps: every printed exhibit on this paper carries a measured region, which is the
first time that has been true since paper 65. The paper prints thirteen figure numbers and
three tables, and every one of the sixteen is here.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2015-32722-037c369c"
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

MEASURE = 468.0
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
           shared_axes: bool = False) -> None:
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
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
          position: str = "below", mention: dict | None = None,
          source: str = "text-layer") -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": source if cap_text else "none",
        "note": note,
        "place": place(page, reg, kind, path, numbered),
        "mention": mention or none_mention(),
        "caption": caption(cap_text, "Table N:" if cap_text else "none", position),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued,
                  "note_sentence": qp(note_sentence, [page, page + 1]) if note_sentence else ""},
    })


# ---------------------------------------------------------------- section paths
SEC_INTRO = ["1 Introduction", "1.1 Context of the Problem"]
SEC_TASK = ["1 Introduction", "1.2 The Task at Hand"]
SEC_MODEL = ["2 Our Model", "2.3 The Multi-Layer State Based Stochastic Epidemic Model"]
SEC_LAYER = ["2 Our Model", "2.3 The Multi-Layer State Based Stochastic Epidemic Model",
             "2.3.1 Individual Layer - Stochastic State Based Model"]
SEC_MOBIL = ["2 Our Model", "2.3 The Multi-Layer State Based Stochastic Epidemic Model",
             "2.3.3 Human Mobility Model"]
SEC_SENS = ["3 Sensitivity Analysis and Results", "3.0.1 Individual Region Tests"]
SEC_VACC = ["3 Sensitivity Analysis and Results", "3.0.2 Vaccine Quantity and Frequency of Shipments"]
SEC_MULTI = ["3 Sensitivity Analysis and Results", "3.0.3 Multiple-Region Simulations"]
SEC_DIST = ["3 Sensitivity Analysis and Results", "3.0.4 Vaccine Distribution"]
SEC_CURE = ["3 Sensitivity Analysis and Results", "3.0.5 Cure Distribution"]
SEC_FUT = ["4 Conclusion", "4.3 Future Work", "4.3.1 Geography Based Modeling"]

# ---------------------------------------------------------------- the p1 title band
EXCLUDED.append({
    "page": 1,
    "bbox": REG[(1, 1)],
    "kind": KIND[(1, 1)],
    "reason": "not-an-exhibit",
    "note": "the title block between the two rules that open the paper: 0.72 pt rules at 50.3 pt "
            "and 165.3 pt at full measure, holding 'Turning the Tables: Modeling the Fight "
            "against Ebola' at 19.1 pt and 'Team 32722' below it at 15.3 pt, with 115.1 pt of "
            "white space between. The block measures as one region because the two rules close "
            "it top and bottom; nothing is drawn in it but two lines of type",
})

# ---------------------------------------------------------------- p4, Figure 1
figure(4, 1, "photo-or-raster-image",
       cap(4, "Figure 1:", "[3]"), "Figure N:", none_mention(), "introduction", SEC_INTRO,
       note="A 700x394 px colourised electron micrograph, 280.8 by 158.1 pt at 60.0 per cent of "
            "the measure: one yellow-brown filamentous virion bent into a loose S across a "
            "violet field, with a second, fainter particle entering at the upper left and a "
            "credit mark '© AP' in the lower right. No axes, no legend, no scale bar, no "
            "magnification factor, no stain named - the only exhibit on the paper that is an "
            "unredacted press photograph rather than the team's own output, and the only one "
            "whose caption is a bare title. It is the paper's only figure in section 1 and it "
            "is cited by nothing: no sentence in the body points to it, so count is 0.")

# ---------------------------------------------------------------- p5, Figure 2
figure(5, 1, "map-or-plan-view",
       cap(5, "Figure 2:", "active outbreak [1]."), "Figure N:", none_mention(),
       "introduction", SEC_TASK, legend="none", labels=True,
       note="A 1220x763 px locator map, 351.0 by 219.5 pt at 75.0 per cent of the measure, drawn "
            "flat rather than as a data page: sea in mid-blue, land in pale cream, internal "
            "country borders as thin white lines, a small white-edged inset rectangle in the "
            "upper left that repeats the same five nations inside the outline of Africa. Five "
            "countries are filled red - Senegal, Guinea, Sierra Leone, Liberia and Nigeria - and "
            "each is named in white leader lines except Nigeria, which is labelled inside its "
            "own shape. A white sans-serif banner across the foot of the art reads 'EBOLA "
            "OUTBREAK IN WEST AFRICA'. There is no legend, no scale bar, no date, no case count "
            "and no shading ramp: the fill encodes membership in the list, not magnitude, so the "
            "map shows which nations the paper is talking about and nothing quantitative. Mali, "
            "named in the prose as a third country with reported cases, is NOT filled. Its "
            "two-sentence caption prints below the art and is the longest sentence on the paper "
            "to name the countries.")

# ---------------------------------------------------------------- p8, Figure 3
figure(8, 1, "flowchart-or-schematic",
       cap(8, "Figure 3:", "Sec. 2.3.1."), "Figure N:", none_mention(), "model", SEC_MODEL,
       labels=True, numbers=False,
       note="A 1024x768 px diagram, 374.4 by 280.8 pt at 80.0 per cent of the measure, drawn to "
            "show the model's three layers nesting into one another. Top left: three large green "
            "circles joined by heavy black edges and labelled 'Regions'. A square is drawn on the "
            "right-hand circle and two leader lines drop from it to a boxed sub-graph of five "
            "blue squares joined by heavy edges, labelled 'Cities'; a second square on that "
            "sub-graph leads down to a box of scattered coloured dots labelled 'Individuals'. A "
            "further pair of leader lines runs from the same city box up to a small inset "
            "compartment diagram at the upper right - Susceptible to Vaccinated, Latent to "
            "Vaccination, Early Stage, Late Stage, Hospitalized, Buried, Unburied, Doctor, Cured, "
            "with two dotted contact inputs (Early-Stage, Late-Stage, Unburied) into Latent and a "
            "dotted Doctor input into Hospitalized. That inset is a miniature of Figure 4, and the "
            "caption says so: 'cf. Fig. 4 and Sec. 2.3.1'. Nothing is plotted; there are no axes, "
            "no legend and no printed values, and the compartment inset carries the rate symbols "
            "at 5 pt, well below the body size. Filed as a schematic, not a network: the nodes "
            "and edges carry the model's structure, not measured relations.")

# ---------------------------------------------------------------- p10, Figure 4
figure(10, 1, "flowchart-or-schematic",
       cap(10, "Figure 4:", "progress to the next state."), "Figure N:",
       cited(9, 10, ["Fig. 4"], 3,
             qtail(9, "progress through the states defined in Fig. 4.", 11)),
       "model", SEC_LAYER, labels=True,
       note="A 1024x768 px state diagram, 409.6 by 307.2 pt at 87.5 per cent of the measure - the "
            "largest diagram on the paper and the exhibit the whole model rests on. Nine "
            "compartment boxes in two columns: Susceptible (green border) to Latent (orange) to "
            "Early-Stage (red) to Late-Stage (red) and Hospitalized (orange), then Unburied (red) "
            "to Buried (blue), Hospitalized to Cured (blue), and Susceptible to Vaccinated (blue). "
            "Four grey contact boxes hang off the left (Early-Stage, Late-Stage, Unburied, feeding "
            "Latent through labelled beta parameters) and two off the right (Vaccination, Doctor). "
            "Every edge is labelled with the transition rate it stands for - beta_c1, beta_c2, "
            "beta_f, gamma_w1, gamma_w2, gamma_h1, gamma_h2, gamma_d, gamma_dh, gamma_R, gamma_f - "
            "and the vaccination edges are dotted where the others are solid. The colour key is "
            "not in the art at all: the caption IS the key ('red states both carry and are able to "
            "spread the infection, the orange states carry the virus but are not able to spread "
            "it, and the blue states do not further interact with the simulation'), which makes "
            "this the paper's only caption that carries data rather than describing the art. "
            "Cited four times, twice before the drawing (p9 prose, p8 inside Figure 3's caption) "
            "and twice after it (p12 prose, p35 in Appendix B).")

# ---------------------------------------------------------------- p17, Figure 5
FIG5 = cap(17, "Figure 5:", "starting in the latent state.")
FIG5_TAIL = (
    " Seven series under a bordered legend inside the upper left, the same inventory and the same "
    "colour order in every chart on this paper: blue, green, red, cyan, magenta, olive and black. "
    "Blue is the infected curve and cyan the deaths on every plot; the remaining five are keyed "
    "to cured, vaccinated, hospitalized, medicated and vaccine-consumed quantities, though at "
    "this raster resolution the two shortest keys are too coarse to read with certainty and are "
    "recorded by colour alone. All seven keys print on every plot but only two carry visible ink "
    "at these scales, the rest lying flat on the axis. White field, no gridlines, no title inside "
    "the art.")


def fig5(reg: int, detail: str) -> None:
    figure(17, reg, "line", FIG5, "Figure N:", none_mention(), "sensitivity", SEC_SENS,
           legend="inside", layout="2", shared_axes=False, note=detail + FIG5_TAIL)


fig5(1,
     "The left panel of Figure 5, its own box 252.2 by 189.2 pt at 53.9 per cent of the measure, "
     "the pair spanning 74.7 to 560.2 pt - 485.5 pt wide against the 468.0 pt text block, so the "
     "two panels start 2.7 pt inside the left margin and stop 20.2 pt past the right one. Y axis "
     "'Quantity (units/day)' 0 to 300 in steps of 50, x axis 'Time (days)' ticked 0, 50, 100, "
     "150 with the axis carried on to about 185 unlabelled. Blue Infected and cyan Died are the "
     "only two curves off the floor, the blue one showing the high-frequency sawtooth of an "
     "integer-count simulation rather than a smooth solution. Printed defect: the blue curve "
     "enters at the very top of the frame and runs along y = 300 for the first days, so the "
     "initial transient is clipped by the axis maximum and the peak is not in the picture. "
     "Panel label '(a) 5% latent' prints below the art on its own centred line.")
fig5(2,
     "The right panel, the same 252.3 by 189.2 pt box, with the y axis rescaled to 0 to 6,000 in "
     "steps of 1,000 while x is unchanged - the pair therefore does NOT share a y measure, which "
     "is what makes the 20 per cent initial-latent case comparable in shape but not in size. "
     "Panel label '(b) 20% latent' below the art. Same seven-key legend inside the upper left, "
     "same white field, same false starts at the axis ceiling: the blue curve is cut at 6,000 for "
     "the first days of the run, exactly as in panel (a).")

# ---------------------------------------------------------------- p19, Figure 6
FIG6 = cap(19, "Figure 6:", "(actual scale).")
FIG6_TAIL = (
    " Seven-key legend inside the upper left as everywhere else on the paper. The cyan and "
    "magenta curves show visible staircase quantisation, a property of counting individuals "
    "rather than of the rendering. Its caption is word for word the caption printed under Figure "
    "7 on the next page - the same sentence, describing the same two city sizes - although "
    "Figure 7 plots medicine efficacy and contains no city-size comparison at all, so the "
    "duplicate is a copy-paste defect in the paper and not a mis-grouping here.")


def fig6(reg: int, detail: str) -> None:
    figure(19, reg, "line", FIG6, "Figure N:", none_mention(), "sensitivity", SEC_SENS,
           legend="inside", layout="2", note=detail + FIG6_TAIL)


fig6(1,
     "The left panel of Figure 6, 252.2 by 189.2 pt at 53.9 per cent of the measure, the pair "
     "again 485.5 pt wide and overhanging the right margin by 20.2 pt. Y axis 'Quantity "
     "(units/day)' 0 to 600 in steps of 100, x 'Time (days)' ticked to 150 and running on to "
     "about 185. Blue Infected peaks near 420, cyan Died just under it at 410, magenta "
     "Hospitalized at 275 and green Cured at 85, with Vaccinated, Medicated and Vaccinated Died "
     "flat on zero. Panel label '(a) ≈ 35, 000 people' below the art - the layer prints a real "
     "≈ and a stray space after the comma in all four city-size labels on this page and p20.")
fig6(2,
     "The right panel, same box, y axis 0 to 45,000 in steps of 5,000: the tenfold city gives a "
     "seventy-fivefold y range, which is the paper's argument that the outbreak is not linear in "
     "population. Blue Infected reaches about 44,000 and cyan Died about 38,000, with magenta "
     "Hospitalized at only 5,000 and green Cured at 1,500. Printed defect: the blue curve climbs "
     "into the top-right corner and is cut by the 45,000 ceiling before x = 185, so the arithmetic "
     "case for the paper's claim is not fully visible. Panel label '(b) ≈ 350, 000 people'.")

# ---------------------------------------------------------------- p21, Figure 8
FIG8 = cap(21, "Figure 8:", "distributed to a single city.")
FIG8_TAIL = (
    " All four panels carry the same seven-key legend inside the upper left, and all four are the "
    "smallest boxes on the paper at 210.6 by 158.0 pt, 45.0 per cent of the measure each, inside "
    "a 2x2 block whose columns run 93.5 to 304.1 pt and 307.9 to 518.5 pt - centred, 425.0 pt "
    "wide. Printed defects, three of them: the art text is aliased to the point where legend "
    "words are unreadable ('Cured' reads as 'C' L ed'), so these four panels behave like a "
    "downsampled paste rather than the crisp vector plotting of Figures 5, 6 and 7; the panel "
    "labels drop the word 'added' after panel (a); and the y axis is labelled 'Quantity (units)' "
    "here where Figures 5 and 6 print 'Quantity (units/day)', while the caption calls the same "
    "quantity a 'Total infection rate' - three names for one axis across three pages.")


def fig8(reg: int, detail: str) -> None:
    figure(21, reg, "line", FIG8, "Figure N:", none_mention(), "sensitivity", SEC_VACC,
           legend="inside", layout="4", note=detail + FIG8_TAIL)


fig8(1,
     "Upper-left panel of Figure 8: 210.6 by 158.0 pt, y 'Quantity (units)' 0 to 50,000 in steps "
     "of 10,000, x 'Time (days)' ticked 0, 50, 100, 150 and carried on to about 185. Blue "
     "Infected climbs to 45,000 and cyan Died tracks just under it at 42,000; green, magenta and "
     "black stay within a few thousand of zero and Vaccinated is flat. Panel label "
     "'(a) 100 vaccines added every 5 days' below the art - the only label on the paper that "
     "keeps the word 'added'.")
fig8(2,
     "Upper-right panel: same axes, x2 of the vaccine does not separate the curves - blue reaches "
     "46,000 and cyan 40,000, while red Vaccinated and black Vaccinated Died climb together to "
     "about 30,000 and 28,000 tracking one another within a line width. The blue curve approaches "
     "the 50,000 ceiling without being cut, the only panel of the four where the peak is inside "
     "the frame. Panel label '(b) 1000 vaccines every 5 days'.")
fig8(3,
     "Lower-left panel: the y axis jumps by a factor of seven to 0 to 350,000 in steps of 50,000, "
     "which is the whole point of the exhibit and is stated nowhere in the caption. Blue, red and "
     "black rise as one thick dark band to about 310,000 to 320,000 and cannot be told apart at "
     "this size, while cyan Died stays at 35,000, green Cured at 10,000 and magenta Hospitalized "
     "at 8,000. Panel label '(c) 10000 vaccines every 5 days', printing below the art.")
fig8(4,
     "Lower-right panel: the same 0 to 350,000 axis as panel (c), and the same indiscriminate "
     "bundle of blue, red and black to about 310,000 - doubling the shipment from 10,000 to 20,000 "
     "vaccines every five days changes the outcome by an amount the eye cannot resolve at 45.0 per "
     "cent of the measure. The plateau sits well inside the 350,000 ceiling, so nothing is clipped "
     "here. Panel label '(d) 20000 vaccines every 5 days', below the art and above the caption, "
     "which prints beneath the whole 2x2 block rather than under any single panel.")

# ---------------------------------------------------------------- p11, Table 1
table(11, 1, 12, 4, "model", SEC_LAYER,
      qtail(12, "cf. Table 1.", 12),
      "Eleven fitted parameters over two country columns and a Factor column: header "
      "'Parameter' against 'Liberia Value', 'Sierra Leone Value' and 'Factor', the two country "
      "headings each wrapping onto a second line because the columns are only 48.2 and 75.9 pt "
      "wide. Full-ruled rather than booktabs: a 0.72 pt rule at 75.2 pt above the header, a "
      "DOUBLED header rule at 104.5 and 106.5 pt two points apart, a 0.72 pt rule under each of "
      "the eleven body rows at 121.3 through 269.8 pt, and five verticals at 93.1, 158.2, 206.4, "
      "282.3 and 518.9 pt running the full height, so the grid has a complete outer box and one "
      "vertical between every pair of columns. 425.8 pt wide, 91.0 per cent of the 468.0 pt "
      "measure. All 22 numbers carry four decimals and are right-aligned, so the columns are "
      "decimal aligned by construction. Printed defects: the twelve symbol cells are typeset "
      "maths whose subscripts drop below the rule they sit on, so beta_f's f prints outside its "
      "row; the Factor column carries the citation '[10]' welded onto the end of one description "
      "only; and guinea's column is absent altogether, the caption explaining that 'Guinea "
      "shares the same parameters as Liberia'.",
      rule="vertical-rules", numeric=2, decimal=True,
      mention=cited(9, 11, ["Table 1"], 5, qtail(9, "defined in Table 1", 12)),
      cap_text=cap(11, "Table 1:", "Rivers et al. [9]"))

# ---------------------------------------------------------------- p13, Table 2
table(13, 1, 5, 3, "model", SEC_MOBIL,
      qtail(14, "cf. Table 2.", 16),
      "The four modified-gravity constants, one to a row, over Constant / Value / Implication. "
      "298.2 pt wide - 63.7 per cent of the measure, the narrowest grid on the paper and the one "
      "that makes the half/full split unavoidable - centred rather than flush, so it sits at "
      "156.9 to 455.1 pt inside a 72.0 to 540.0 pt text block. Full-ruled in the same register "
      "as Table 1: a 0.72 pt top rule at 75.2 pt, the header rule DOUBLED at 90.0 and 92.0 pt, a "
      "rule under each of the four body rows at 106.9, 121.7, 136.6 and 151.4 pt, and four "
      "verticals at 156.9, 215.4, 256.0 and 455.1 pt making a complete outer box with one "
      "vertical between every pair of columns. Three of the four constants are Greek letters "
      "that the layer prints as single glyphs; the fourth row's name is a bare italic k and its "
      "value cell holds an em dash, the only empty-looking cell in any grid on this paper. "
      "Printed defect: the Value column mixes two decimals with three (0.78, 1.60, 1.54) so the "
      "alignment is decimal only by accident, and the caption is one long sentence that names "
      "the Guinea mobility census as its fit source while the prose applies the same constants "
      "to Liberia and Sierra Leone on the strength of no data at all.",
      rule="vertical-rules", numeric=1, width="half",
      mention=cited(14, 13, ["Table 2"], 1, qtail(14, "cf. Table 2.", 12)),
      cap_text=cap(13, "Table 2:", "census microdata."))

# ---------------------------------------------------------------- p22, Table 3
table(22, 1, 5, 5, "sensitivity", SEC_MULTI, "",
      "The four toy-model cities, and the only grid on the paper that leaves the text block: "
      "497.8 pt wide against the 468.0 pt measure - 106.4 per cent - running from 72.0 pt, "
      "exactly the left edge of the text, to 569.8 pt, which is 29.8 pt past the right edge of a "
      "612 pt page. Five columns (City, Population, Latitude and Longitude, Initial Percent "
      "Infected (Latent), Parameter Set) and five printed rows, one of them the header. "
      "Full-ruled in the same register as the other two grids - top rule at 333.1 pt, header "
      "rule doubled at 347.9 and 349.9 pt, a rule under each of the four body rows at 364.7, "
      "379.6, 394.4 and 409.3 pt, and six verticals at 72.0, 106.1, 173.8, 307.7, 484.5 and "
      "569.8 pt for a complete outer box with a vertical between every pair of columns. "
      "Unnumbered in the text: the prose never refers to it, so count is 0, and its caption is "
      "the only name it has. Printed defects: the coordinate column prints '9.31N , -12.16E' "
      "with a stray space before the comma while its three neighbours print '9.17N, -12.82E'; "
      "the latitudes are all northern and the longitudes all eastern though the paper's own "
      "baseline city is '9.18S and -12.822 W', so the toy cities sit in the Gulf of Guinea; and "
      "all four rows carry the same Parameter Set, which makes the column a constant.",
      rule="vertical-rules", numeric=2,
      cap_text=cap(22, "Table 3:", "parameter sets"))

# ---------------------------------------------------------------- p23, Figure 9
FIG9 = cap(23, "Figure 9:", "vaccine distribution.")
FIG9_TAIL = (
    " The seven-key legend sits inside the upper left of every panel, and the axes print only a "
    "bottom spine - the y side carries tick marks with no continuous axis line, and there is no "
    "top or right frame. The four scenarios are the four enumerated in the prose on p22, in the "
    "same order, so the exhibit is a direct illustration of that list. Printed defects, four of "
    "them: every panel label is hard-hyphenated across two lines ('vaccines dis-' / 'tributed to "
    "rural regions'), so each label is broken mid-word in the art; the olive series runs off the "
    "top of the axis in panels (c) and (d) at about 29,400 of a 30,000 ceiling, ending with no "
    "break marker; the red Vaccinated and black Vaccine used series lie on top of one another in "
    "panels (a) and (b) with the z-order flipped between the rows, so only one of the two is "
    "visible in each half of the figure; and the pairs (a)/(b) and (c)/(d) differ by a few pixels "
    "at the right edge, so the vaccine routing that the figure exists to compare changes almost "
    "nothing. The caption calls the axis an 'infection count' where the art labels it 'Quantity "
    "(units)'.")


def fig9(reg: int, detail: str) -> None:
    figure(23, reg, "line", FIG9, "Figure N:", none_mention(), "sensitivity", SEC_DIST,
           legend="inside", layout="4", shared_axes=True, note=detail + FIG9_TAIL)


fig9(1,
     "Upper-left panel of Figure 9: 210.6 by 157.9 pt, 45.0 per cent of the measure, in a 2x2 "
     "block whose columns run 93.5 to 304.1 and 307.9 to 518.5 pt. Y 'Quantity (units)' 0 to "
     "30,000 in steps of 5,000 with no thousands separators, x 'Time (days)' ticked 0, 50, 100, "
     "150 with the axis carried on to about 181. Blue rises to the top of the frame and ends in "
     "the corner at about 29,500 still climbing, so the curve is truncated rather than resolved; "
     "cyan sits near 12,000 and the rest near zero, with red buried under black. Label '(a) Rural "
     "regions infected, vaccines dis-tributed to rural regions', hyphenated in the art.")
fig9(2,
     "Upper-right panel: identical axes and identical art to panel (a) to within a few pixels at "
     "the right edge, which is the figure's central weakness - sending the vaccine to the urban "
     "centres instead of the rural districts moves the curves by less than the line width. Blue "
     "again exits through the top-right corner at about 29,500. Label '(b) Rural regions infected, "
     "vaccines dis-tributed to urban regions'.")
fig9(3,
     "Lower-left panel: the only panel where the olive Medicine use series becomes visible, rising "
     "faster than blue and crossing it near day 60 before being cut off at the 30,000 ceiling at "
     "about day 67, roughly two thirds of the way along the x axis. Blue on this panel flattens "
     "near 27,000 instead of exiting the corner, and cyan drops to about 8,000. Label '(c) Urban "
     "regions infected, vaccines dis-tributed to urban regions'.")
fig9(4,
     "Lower-right panel: near-identical to panel (c), with the olive series again clipped at about "
     "29,400 around day 67 and the same flat blue near 27,000. Label '(d) Urban regions infected, "
     "vaccines dis-tributed to rural regions'. The caption prints below the whole block, one line, "
     "under the row-two labels.")

# ---------------------------------------------------------------- p25, Figure 10
FIG10 = cap(25, "Figure 10:", "medicine distribution.")
FIG10_TAIL = (
    " Geometrically and visually this is Figure 9 with one word changed in each label "
    "('vaccines' becomes 'medicine') and one word in the caption ('vaccine' becomes 'medicine'): "
    "the two 2x2 blocks agree to a mean absolute pixel difference of 4.1 out of 255 with best "
    "alignment at zero shift, and about three per cent of the pixels differ at all. The seven-key "
    "legend, the axes, the clipped olive series and the hidden red series are all carried over "
    "unchanged, so the paper's comparison of a vaccine distribution policy against a medicine "
    "distribution policy is drawn twice from essentially the same data.")


def fig10(reg: int, detail: str) -> None:
    figure(25, reg, "line", FIG10, "Figure N:", none_mention(), "sensitivity", SEC_CURE,
           legend="inside", layout="4", shared_axes=True, note=detail + FIG10_TAIL)


fig10(1,
     "Upper-left panel of Figure 10: the same 210.6 by 157.9 pt box as every other panel in this "
     "pair of figures, y 'Quantity (units)' 0 to 30,000 in steps of 5,000, x 'Time (days)' ticked "
     "to 150 and drawn to about 181. Blue ends in the top-right corner at about 29,500, still "
     "rising, exactly as in Figure 9. Label '(a) Rural regions infected, medicine dis-tributed to "
     "rural regions', hyphenated in the art like all sixteen labels across the two figures.")
fig10(2,
     "Upper-right panel: the same axes and the same traces as panel (a), with red Vaccinated "
     "hidden beneath black Vaccine used as before. Label '(b) Rural regions infected, medicine "
     "dis-tributed to urban regions'.")
fig10(3,
     "Lower-left panel: the olive Medicine use series visible again, crossing blue near day 60 and "
     "cut at the 30,000 ceiling around day 67; blue flattens near 27,000 and cyan falls to about "
     "8,000. Label '(c) Urban regions infected, medicine dis-tributed to urban regions'.")
fig10(4,
     "Lower-right panel: the same picture as panel (c) with the series within a line width of one "
     "another. Label '(d) Urban regions infected, medicine dis-tributed to rural regions'. The "
     "caption, below the block, names a 'Total infection count' where the axis prints 'Quantity "
     "(units)'.")

# ---------------------------------------------------------------- p20, Figure 7
FIG7 = cap(20, "Figure 7:", "(actual scale).")
FIG7_NOTE_TAIL = (
    " Its caption is a copy of Figure 6's, word for word, and describes a comparison between "
    "two city sizes that this figure does not contain - the three panels carry three medicine "
    "efficacies, and the only place the efficacy values appear is the panel labels, so the "
    "paper's own prose ('Medicine efficacy multipliers were set at 2, 5 and 10, representing "
    "recovery times of 8 days, 3 days, and less than 1 day') cannot be checked against the "
    "caption at all.")


def fig7(reg: int, label: str, detail: str) -> None:
    figure(20, reg, "line", FIG7, "Figure N:", none_mention(), "sensitivity", SEC_SENS,
           legend="inside", layout="3",
           note=detail + FIG7_NOTE_TAIL)


fig7(1, "a",
     "The left panel of Figure 7, measured as its own box 252.2 by 189.2 pt at 53.9 per cent of "
     "the measure, with the panel pair spanning 74.7 to 560.2 pt - 485.5 pt, 20.2 pt past the "
     "right margin of the 72.0 to 540.0 pt text block. Axes 'Quantity (units)' 0 to 50,000 in "
     "steps of 10,000 against 'Time (days)' 0 to about 180 in steps of 50, on a cream field "
     "rather than white. Six series under a boxed legend inside the upper left: Infected (Stage "
     "II) in blue rising to 48,000; Dead in cyan rising to 37,000; Medicine used in yellow "
     "rising to 32,000; and Cured (green), Vaccinated (red), Hospitalized (magenta) and "
     "Vaccinated used (black) all pinned within a few hundred units of zero. No gridlines. "
     "Printed defect: 'Dead' climbs to 37,000 individuals, which cannot be right for a "
     "35,000-person city and reads like the series keyed to the wrong line.")
fig7(2, "b",
     "The middle panel, the same 252.3 by 189.2 pt box and the same six-series legend, with the "
     "blue Infected curve reaching the 50,000 ceiling of the axes just before day 180 and the "
     "cyan Dead curve at 41,000. Same axes, same cream field, same absence of gridlines. The "
     "printed panel label under it is '(b) 5 (approximately 3 days)' with a missing opening "
     "bracket and no 'Medicine efficacy of', so the label is unreadable on its own - only the "
     "'(a)' panel next to it tells a reader what the numbers mean.")
fig7(3, "c",
     "The bottom panel, centred at 191.3 to 443.6 pt rather than left-aligned under the pair, "
     "the same 252.2 by 189.2 pt box with the same legend and axes. Blue Infected flattens near "
     "46,000 by day 180 where panel (a) needed to day 250 to reach 48,000, and the cyan Dead "
     "series is correspondingly the lowest of the three panels - the one visible sign that the "
     "efficacy change did anything. Its label reads '(c) 10 (approximately 1 day)' and sits "
     "between the art and the caption, as every panel label on this paper does.")

# ---------------------------------------------------------------- p26, Figure 11
FIG11 = cap(26, "Figure 11:", "movement factos.")
FIG11_TAIL = (
    " Its caption carries the paper's typo - 'varying movement factos' - which is recorded as "
    "printed. The two panels differ in scale by a factor of two (the left one tops out at 30,000, "
    "the right at 60,000) and their frames are drawn differently from Figure 12's: left and "
    "bottom spines with floating inward ticks on the right, no enclosing box, where Figure 12 has "
    "a full box. The panel qualifiers read backwards at first sight - k = 1 is the HIGHER "
    "movement rate - and the prose on the facing page explains why ('1 represents a higher "
    "transportation rate than 5 (essentially the probability of moving is divided by k)'), so the "
    "labels are right; but the same prose claims that the end quantities 'tend to increase with "
    "increasing mobility' while panel (b), the low-mobility case, is plotted on an axis twice as "
    "tall as panel (a)'s, which is the opposite ordering. This figure sits under the 3.0.5 Cure "
    "Distribution heading although it varies mobility: the printed heading is what is recorded, "
    "and the exhibit belongs to 3.0.5.2 Movement Parameter Variation by its run-in title.")


def fig11(reg: int, detail: str) -> None:
    figure(26, reg, "line", FIG11, "Figure N:", none_mention(), "sensitivity", SEC_CURE,
           legend="inside", layout="2", note=detail + FIG11_TAIL)


fig11(1,
     "The left panel of Figure 11: 210.6 by 158.0 pt, 45.0 per cent of the measure, the pair "
     "centred at 93.5 to 518.5 pt. Y 'Quantity (units)' 0 to 30,000 in steps of 5,000, x 'Time "
     "(days)' ticked 0, 50, 100, 150 and drawn on to about 180. Blue climbs to the frame top and "
     "the olive Medicine used curve is cut at the 30,000 ceiling by about day 70, so in the higher "
     "mobility case both of the interesting curves leave the picture; red Vaccinated and black "
     "Vaccines Used are printed on top of one another and read as a single series. Label "
     "'(a) Movement factor k = 1, higher movement rate', wrapped onto a second line at 'rate', "
     "set in crisp vector type below a raster panel.")
fig11(2,
     "The right panel: the same box and the same seven-key legend inside the upper left, but the y "
     "axis is redrawn at 0 to 60,000 in steps of 10,000 - twice the range of panel (a) - for a "
     "case the caption calls the LOWER movement rate. Blue reaches about 58,000 and the olive "
     "curve no longer clips, which is the one honest signal in the figure that the parameter "
     "moved, and it moves the outcome in the direction opposite to the one the prose predicts. "
     "Label '(b) Movement factor k = 5, lower movement rate'.")

# ---------------------------------------------------------------- p27, Figure 12
FIG12 = cap(27, "Figure 12:", "parameters chosen.")
FIG12_TAIL = (
    " The three panels are laid out two abreast with the third centred beneath them - 74.7 to "
    "560.2 pt for the top pair, 191.3 to 443.6 pt for the bottom box - so the block is asymmetric "
    "in a way that pairs with Figure 7's layout rather than with Figure 11's two-up. Panels (a) "
    "and (b) are plotted on different y ranges (0 to 60,000 and 0 to 30,000), which puts the two "
    "single-country systems on different scales inside one figure and makes the visual comparison "
    "of Liberia against Sierra Leone invalid on its face. These are the only fully boxed panels "
    "on the paper apart from Figure 7's. Red Vaccinated and black Vaccines Used overprint each "
    "other exactly in all three panels, and in panel (c) the legend box itself sits on top of the "
    "rising olive curve.")


def fig12(reg: int, detail: str) -> None:
    figure(27, reg, "line", FIG12, "Figure N:", none_mention(), "sensitivity", SEC_CURE,
           legend="inside", layout="3", note=detail + FIG12_TAIL)


fig12(1,
     "Upper-left panel of Figure 12: 252.2 by 189.2 pt, 53.9 per cent of the measure, the largest "
     "of the three. Y 'Quantity (units)' 0 to 60,000 in steps of 10,000, x 'Time (days)' ticked "
     "to 150 and drawn to about 180, fully boxed. Blue and cyan climb steeply on a 60,000 range "
     "where the two panels beside and below it use 30,000. Label '(a) All cities in Liberia', "
     "below the art in vector type.")
fig12(2,
     "Upper-right panel: the same 252.3 by 189.2 pt box but the y axis is halved to 0 to 30,000 in "
     "steps of 5,000, so the Sierra Leone system is drawn at half the scale of the Liberian one "
     "directly beside it. Label '(b) All cities in Sierra Leone'.")
fig12(3,
     "The centred bottom panel: 252.2 by 189.2 pt at 191.3 to 443.6 pt, y 0 to 30,000 in steps of "
     "5,000. The olive Medicine used curve is clipped at the 30,000 ceiling from about day 100 on, "
     "and the legend box in the upper left overlaps that same rising curve, so part of the key is "
     "drawn over data. Label '(c) 2 cities in Liberia, 2 cities in Sierra Leone'.")

# ---------------------------------------------------------------- p32, Figure 13
figure(32, 1, "node-link-network",
       cap(32, "Figure 13:", "Background image from [20]."), "Figure N:",
       cited(14, 32, ["Fig. 13"], 1,
             qtail(14, "cf. Fig. 13.", 14), pattern="direct"),
       "other", SEC_FUT, legend="inside", labels=True,
       note="A 327.6 by 271.2 pt box at 70.0 per cent of the measure: a grey political basemap of "
            "Guinea, Sierra Leone and Liberia with country names in dark grey capitals, the three "
            "capitals and one intermediate city printed in black (Conakry, Freetown, Mellandou, "
            "Monrovia), and eight coloured circles standing on the places: green for Urban, "
            "yellow for Rural, orange for Isolated, keyed by a three-entry legend at the lower "
            "left. Heavy black straight edges join the circles into a graph, so the exhibit is a "
            "network drawn on a map rather than a map with data shading. The caption credits the "
            "basemap ('Background image from [20]', a Deutsche Welle page) and the prose promises "
            "that 'These nodes, and their geographic positions, were chosen in an arbitrary "
            "manner' - which the basemap then contradicts, since the nodes sit on real cities and "
            "the paper's own text calls them 'the major urban centers of each nation'. Filed as "
            "node-link-network, not map-or-plan-view: the geography locates the graph and the "
            "graph is the exhibit. Cited once, from p14, eighteen pages before the drawing.")

# ---------------------------------------------------------------- payload
# doc_order follows the page, not the order in which the blocks above were written: sort the
# figures and the grids together by (page, region) and number them straight through.
for _n, _row in enumerate(sorted(ITEMS + TABLES, key=lambda r: (r["page"], r["place"]["page_order"])), 1):
    _row["place"]["doc_order"] = _n

RULES: list[str] = [
    "Panels are measured boxes, not figure numbers: the two-panel exhibits contribute two rows "
    "and the four-panel ones four, each with a panel_count of one [geometry.panel_count].",
    "Full width means 75 per cent or more of this paper's own 468.0 pt text measure, never of the "
    "612 pt page: Table 1 at 91.0 per cent is full, Table 2 at 63.7 per cent is half, and Table 3 "
    "at 106.4 per cent is full by a margin that measures the overhang [table.width].",
    "Every exhibit on this paper prints its caption below the art, the three grids included, so "
    "no row carries a position of above [caption.position].",
    "All sixteen captions use the colon form - 'Figure N:' and 'Table N:' - and not one of them "
    "ends in a period, so the numbering is recorded as printed rather than normalised "
    "[caption.numbering].",
    "All three grids are fully ruled: a top rule, a header rule doubled two points apart, a rule "
    "under every body row and a vertical between every pair of columns, which is vertical-rules "
    "and not booktabs [table.rule_style].",
    "Every line chart on the paper carries the same seven-series inventory under a bordered "
    "legend drawn inside the plot frame, so the legend reads inside on all twenty-four line "
    "panels [geometry.legend].",
    "Where the prose cites an exhibit more than once the count records the printed instances and "
    "first_page the earliest of them, not the page the art sits on [mention.count].",
    "A back-reference printed before its exhibit - cf. Table 2 and cf. Fig. 13, both on p14 - is "
    "recorded with the lead_pages it implies rather than dropped for being negative or large "
    "[mention.lead_pages].",
    "Exhibits that the prose never names keep a mention with a count of zero and no sentences: "
    "twelve of the sixteen are never cited outside their own caption, so count is one of the "
    "commonest values on this paper [mention.first_page].",
    "The p1 title band is excluded rather than measured: two full-measure rules close a block "
    "that holds nothing but the title and the team number [place.area_frac].",
    "Section paths are taken from the printed headings, and where the context dump attached a "
    "run-in sub-heading to the wrong parent - Figure 7 to 3.0.2, Table 3 to 3.0.4, Figure 13 to "
    "4.3.3 - the printed heading wins [place.section_path].",
    "Two exhibits print the same caption text, Figure 6 and Figure 7, and both keep it verbatim: "
    "the census records what the paper prints and the defect goes in the note rather than being "
    "edited away [caption.words].",
]

NOTE = (
    "Paper 71, Team 32722. Thirty-three measured regions over seventeen of the thirty-nine pages, "
    "and all thirty-three are accounted for: twenty-nine figure boxes, three grids and the p1 "
    "title band, so unaccounted is zero and nothing is left unresolved. The paper numbers "
    "thirteen figures and three tables and every one of the sixteen is here.\n\n"
    "The variety is small for the count. Five kinds of drawing carry the whole paper: a press "
    "photograph of the virion, a locator map, two schematics, one network on a basemap, and "
    "twenty-four panels of the same MATLAB multi-series line plot. Every one of the twenty-nine "
    "figure regions is an embedded raster - a pasted bitmap - while the three grids are vector "
    "table rules drawn by the word processor, which is why the axes and legends degrade where "
    "the type does not.\n\n"
    "Defects worth recording. Figure 6 and Figure 7 print the same caption word for word, though "
    "Figure 7 plots medicine efficacy and contains no city-size comparison. Figure 10 is Figure 9 "
    "with 'vaccines' changed to 'medicine' in the labels and the caption: the two 2x2 blocks agree "
    "to a mean absolute pixel difference of 4.1 out of 255 with best alignment at zero shift, so "
    "the vaccine-versus-medicine comparison is drawn twice from essentially one dataset. Nine "
    "curves are clipped by their own axis ceilings - both Figure 5 panels, Figure 6 panel (b), the "
    "olive series in Figures 9(c), 9(d), 10(c), 10(d), 11(a) and 12(c). The Figure 7 panel labels "
    "lose their opening bracket and their approximation sign in panels (b) and (c), reading "
    "'5 ≈ 3 days)' and '10 ≈ 1 day)'; the Figure 9 and Figure 10 labels are each hard-hyphenated "
    "across two lines at 'dis-tributed'; and the axis is called 'Quantity (units/day)' in Figures "
    "5 and 6, 'Quantity (units)' from Figure 7 on, and 'infection count' in the captions of "
    "Figures 9, 10 and 11.\n\n"
    "Two failures of internal consistency. Figure 11's panel (b), the LOWER movement case, is "
    "plotted on an axis twice as tall as panel (a)'s, while the prose two centimetres away says "
    "the end quantities 'tend to increase with increasing mobility'. Figure 12 plots Liberia on a "
    "60,000 axis and Sierra Leone on a 30,000 axis side by side, so the comparison the figure "
    "exists for cannot be read off it.\n\n"
    "Table 3 leaves the text block: 497.8 pt wide against the 468.0 pt measure, 106.4 per cent, "
    "flush with the left margin and 29.8 pt into the right one. Its row B prints '9.31N , -12.16E' "
    "with a stray space, its four latitude/longitude pairs are all north and east although the "
    "paper's own baseline city is '9.18S and -12.822 W', and its Parameter Set column is the "
    "constant 'Liberia' in all four rows. Table 1 carries a doubled header rule two points apart "
    "and subscripts that drop below the rules they sit on; Table 2 mixes two-decimal and "
    "three-decimal values in a column the caption calls fitted constants.\n\n"
    "Citation practice is thin. Four of the sixteen exhibits are ever named in the prose - "
    "Figure 4 three times, Table 1 five times, Table 2 and Figure 13 once each, the last two from "
    "a single page (p14) that cites both backwards before either is drawn. The other twelve are "
    "orphans: no sentence outside their own captions points at them."
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

out = PROXY / "pc71-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
