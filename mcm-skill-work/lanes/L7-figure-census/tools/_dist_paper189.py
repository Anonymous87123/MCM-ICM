"""Hand census of P-A-2019-1902727-2e04a61b (Team 1902727, 24 pages, 15 measured regions).

A dragons paper for problem A 2019: a logistic mass-age fit, a Kleiber-law energy model, a
Malthus sheep-flock model, a Legendre-polynomial forage-yield regression, a seven-level
ecosystem table, an NPP degradation model, and a two-axis sensitivity sweep. Fifteen measured
regions resolve into SEVEN FIGURE ROWS and SEVEN TABLE ROWS; the fifteenth region is the
addressee block of the closing letter to George R.R. Martin and is refused.

  p5     r1  Notation      table-grid               three columns, twenty-seven body rows
  p6     r1  Figure 1      line                     the mass-age fit, clip art over the data
  p8     r1  Figure 2      line                     intake and expenditure against age
  p9     r1  Figure 3      flowchart-or-schematic   three boxes, two arrows
  p9     r2  Figure 4      flowchart-or-schematic   four boxes, three unlabelled arrows
  p13    r1  Table 2       table-grid               sensitivity coefficients by month
  p13    r2  Figure 5      line                     the same coefficients as curves
  p14    r1  Table 3       table-grid               forage yield and area by region
  p14    r2  Figure 6      map-or-plan-view         four plan-view footprints, one labelled
  p15    r1  Table 4       table-grid               seven ecosystems and a level number
  p17    r1  Table 5       table-grid               NPP and biomass for the same seven
  p18    r1  Figure 7      line                     two panels, both titled Daily Intake
  p19    r1  Table 6       table-grid               weight deviation, ten offsets, ages 1-8
  p19    r2  Table 7       table-grid               intake deviation, the same template

The paper prints no Table 1: p13's prose says 'as shown in table 1' for the integral regression
model that is equation (16) three pages later, and no grid answers to the number. Table 3 is
typeset 'Table3 :' - the digits run into the word and a space precedes the colon.

The fifteenth region, p22 r1, is a two-path vector block at y=62-158 holding 'To: George R.R.
Martin / Date: Sunday, Janurary 26 , 2019 / Subject: Fun Facts About Game of Thrones' - the
addressee block of the closing letter. Measured because the letter's header rule brackets it;
not an exhibit.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2019-1902727-2e04a61b"
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


def cited(first_page: int, page: int, style: list[str], count: int, lead: str = "",
          trail: str = "", pattern: str = "direct", read: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page) if lead else "",
            "trail_sentence": q(trail, first_page) if trail else "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": None}


def caption(verbatim: str, kind: str = "Figure", position: str = "below",
            variables: int = 0, numbering: str | None = None) -> dict:
    return {"verbatim": schema.norm(verbatim),
            "numbering": numbering or f"{kind} N:",
            "words": len(schema.words(verbatim)), "sentences": 1, "units": False,
            "variables": variables > 0, "variable_count": variables,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def geometry(family: str, panels: int = 1, layout: str = "1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = False,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


def head(page: int, prefix: str) -> str:
    for h in CTX["headings"]:
        if h["page"] == page and h["label"].startswith(prefix):
            return h["label"]
    raise SystemExit(f"no heading on p{page} starting {prefix!r}")


def printed(page: int, text: str) -> str:
    """A heading the layout pass failed to index, accepted only as a printed line."""
    line = schema.norm(text)
    if line not in schema.printed_lines(PID):
        raise SystemExit(f"not a printed line of the paper: {line!r}")
    if line not in schema.page_text(PID, page):
        raise SystemExit(f"printed line is not on p{page}: {line!r}")
    return line


S_NOT = [head(5, "3 Notation")]
S_41 = [head(5, "4.1 Dragon’s weight growth equation based on Logistics Model")]
S_423 = [head(8, "4.2.3 Comparison of energy consumption and intake")]
S_43 = [printed(9, "4.3 Predation area required to support dragon under different climate")]
S_433 = [printed(13, "4.3.3 Predation area needed to support dragons in three types of regions")]
S_432 = [head(11, "4.3.2 Herbage yield under different climate conditions")]
S_44 = [printed(14, "4.4 Community required to provide different level of assistance for drag-")]
S_452 = [printed(17, "4.5.2 Degree of degradation in production capacity and declination in biomass")]
S_51 = [head(18, "5.1 The sensitivity analysis of dragon’s weight")]
S_52 = [head(18, "5.2 Reliability verification")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_KNOWN |= schema.printed_lines(PID)
for _group in (S_NOT, S_41, S_423, S_43, S_433, S_432, S_44, S_452, S_51, S_52):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN:
            raise SystemExit(f"section label is not an indexed heading: {_label!r}")

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_block: dict, cap_src: str, mention: dict,
           section: list[str], note: str, geo: dict | None = None, number: str = "",
           section_kind: str = "other", confidence: str = "high", order: int = 1,
           other_note: str = "") -> None:
    ITEMS.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)], "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap_block["verbatim"],
        "caption": cap_block, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section, order),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
        "other_note": other_note,
    })


def table(page: int, reg: int, section: list[str], note: str, spec: dict,
          cap_block: dict | None = None, cap_src: str = "none", mention: dict | None = None,
          section_kind: str = "other", order: int = 1) -> None:
    block = cap_block or caption("", kind="Table")
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)],
        "family": "table-grid", "caption_source": cap_src,
        "caption_verbatim": block["verbatim"], "caption": block, "table": spec,
        "place": place(page, reg, section_kind, section, order),
        "mention": mention or uncited(), "note": note, "confidence": "high",
    })


def exclude(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason, "note": note})


CAP_N = caption("3 Notation", kind="Table", position="above", numbering="none")
CAP1 = caption("Figure 1: Dragon Age-Weight relation")
CAP2 = caption("Figure 2: Dragon Intake-age, expenditure-age relation")
CAP3 = caption("Figure 3: Food Chain")
CAP4 = caption("Figure 4: Modeling flow")
CAPT2 = caption("Table 2: sensitivity coefficient of monthly forage yield in three types of areas",
                kind="Table", position="above")
CAP5 = caption("Figure 5: Change of sensitivity coefficients")
CAPT3 = caption("Table3 : Forage yield and predation area needed to support dragons in three "
                "types of regions", kind="Table", position="above", numbering="Table N:")
CAP6 = caption("Figure 6: The area of land required for dragon in different climates")
CAPT4 = caption("Table 4: Different ecosystem and corresponding Level of Assistance",
                kind="Table", position="above")
CAPT5 = caption("Table 5: Mean net primary production (NPP) and mean biomass values for "
                "different ecosystems", kind="Table", position="above")
CAP7 = caption("Figure 7: The deviation of Dragon’s weight, daily intake if change the "
               "hypothesis weight at age 1 by ±3%")
CAPT6 = caption("Table 6: Sensitivity Analysis of dragon’s weight", kind="Table",
                position="above")
CAPT7 = caption("Table 7: Sensitivity Analysis of dragon’s daily energy intake", kind="Table",
                position="above")

BOOKTABS = {"rule_style": "booktabs", "zebra": False, "diagonal_header": False,
            "units_in_header": False, "decimal_aligned": False, "orientation": "portrait",
            "note_sentence": ""}
BOXED = dict(BOOKTABS, rule_style="boxed")
GRID = dict(BOXED, diagonal_header=True)

# ============================================================ 3: the notation grid
table(5, 1, S_NOT,
      "Three columns - Abbreviation | Description | Unit - over twenty-seven body rows, ruled "
      "booktabs with no verticals, a rule above the first row and one at the foot. The symbol "
      "column is set in two conventions: plain italic for single letters (a, b, d, y, G), italic "
      "with a matching subscript for indexed forms (w(a), q(a), u(a), s(a), hi (t), xi (t), ci, "
      "Si, fi, Fi, ni), and a third treatment for the two derived deltas (∆N P P ij, ∆Fij) whose "
      "subscripts are set as loose capitals with the exponent notation broken up. FOUR ROWS "
      "CARRY NO UNIT AT ALL - G 'Scale of sheep flock under an ecological balance', g(t) 'The "
      "number of sheep after breeding for t days', g0 'Sensitive coefficient of forage yield' and "
      "xi (t) 'meteorological element' - and the two of them that the model later uses are used "
      "as the sheep-flock scale and as the initial flock, so the empty cells sit on quantities "
      "the arithmetic needs. g0 IS DEFINED AS THE WRONG QUANTITY: the row prints 'Sensitive "
      "coefficient of forage yield', but p10 writes 'let g0 be the initial number of sheep' and "
      "equation (13) sets g(0)=g0, so the table's one definition of g0 contradicts the model. "
      "sm IS TRUNCATED MID-SENTENCE - 'The number of sheep the three dragons' with no verb, and "
      "the printed unit day −1 belongs to a count, not to a rate. THE UNIT COLUMN IS INTERNALLY "
      "INCONSISTENT: s(a) and b and d are counts of sheep, given day −1 and day −1; hi (t) is "
      "given kg/hm2 for a monthly yield and Yt kg/hm2 for a sum of eighteen regression terms; "
      "ni is given g × year/m2 where the same quantity is written g/year in ∆N P P ij two rows "
      "down; and ci is given kcal × day/m2, a unit the paper never uses again. The caption is "
      "the section heading itself - '3 Notation' printed above the grid with no 'Table 1' "
      "anywhere - so the table the paper calls Table 1 on p13 is not this one and no page "
      "identifies it. NO SENTENCE NAMES THE GRID.",
      dict(rows=28, cols=3, header_rows=1, merged_cells=False, numeric_cols=0, text_cols=3,
           width="full", continued=False, **BOOKTABS),
      CAP_N, "text-layer", section_kind="symbols")

# ============================================================ 4.1: the mass-age fit
figure(6, 1, "line", CAP1, "text-layer",
       cited(6, 6, ["Figure 1"], 2,
             lead="According to the above formula, we can fit a curve of the weight-age of the "
                  "dragon , as shown in Figure 1."),
       S_41,
       "A MATLAB line plot of body mass against age: one solid blue curve, y ticked 0 to 14 in "
       "twos with a free-floating 'x 10^5' multiplier at the top left and ylim autoscaled to "
       "about 14.8, x 0 to 12 ticked every second year, axis titles Mass(kg) and Age(year), and "
       "the fitted equation pasted into the plot as a raster in italic LaTeX - "
       "Mass = 1.481×10^6/(1+147656×e^{-2.417×Age}). A LARGE DRAGON CLIP ART IS PASTED OVER THE "
       "DATA FIELD with the word 'Dragon' set in large blue type at its right, covering the "
       "abscissa from about age 2 to age 9 and the ordinate from about 1 to about 11 x 10^5 - "
       "that is, the whole of the curve's steep segment, so the only part of the plate a reader "
       "can check is the flat head and the flat tail. THE CURVE IS THE PRINTED EQUATION, SAMPLED "
       "YEARLY: digitizing the stroke and solving the axes from the tick marks puts the drawn "
       "polyline within 0.03 x 10^5 (0.2 per cent of the axis) of the straight segments joining "
       "eq (4) at ages 0, 1, 2 ... 12, so between the samples it departs from the smooth logistic "
       "by up to about 0.9 x 10^5 near age 5.4 - a fifth of a tick, invisible at print size. THE "
       "EQUATION DOES NOT PASS THROUGH THE DATA IT SAYS IT WAS FITTED TO: eq (4) reproduces "
       "w(0)=10.03 kg and w(3)=14003.8 kg almost exactly but returns w(1)=112.45 kg against the "
       "text's 'the weight after one year is about 35kg' - a factor of 3.2 - and no real "
       "(wm, r0) satisfies all three constraints at once, so the two parameters were fixed on two "
       "of the three points and the third was left to fall where it would. The plotted value at "
       "age 1 is therefore 112 kg on the plate and 35 kg in the paragraph, and nothing on the "
       "page remarks on it. The asymptote 14.81 x 10^5 kg is 1481 tonnes, which the summary "
       "states as '14.8 x 10^5 kg' and which fixes the plate's ylim; the summary also says the "
       "dragon 'grew rapidly from age 3 to age 5' where the paragraph on this page says 'from 3 "
       "to 7 years old'. Cited twice on its own page, once by the lead-in and once by 'As can be "
       "seen from Figure 1'.",
       geometry("line", labels=True, numbers=True), "1", section_kind="model")

# ============================================================ 4.2.3: intake against expenditure
figure(8, 1, "line", CAP2, "text-layer",
       cited(8, 8, ["Figure 2"], 2,
             lead="we can visually see the relationship between the calorie consumption and "
                  "intake of the dragon, as shown in Figure 2."),
       S_423,
       "Two dashed curves on one frame: 'Daily Intake' in blue dashes with round markers and "
       "'Expenditure' in red dashes, y 0 to 6 with an 'x 10^6' multiplier outside the frame, x 0 "
       "to 20 ticked every second year, y-title 'Daily Intake(Kcal)' and x-title 'Age(year)', "
       "legend boxed inside the upper right. THE Y-TITLE NAMES ONLY ONE OF THE TWO SERIES, and "
       "the caption 'Dragon Intake-age, expenditure-age relation' names both, so the axis label "
       "and the caption disagree about what the frame holds. THE TWO CURVES CROSS AND THEN "
       "COINCIDE, which the paper reads as the dragon's maintenance point: intake peaks at about "
       "5.6 x 10^6 at age 5 and falls to about 4.9 x 10^6, expenditure rises more slowly, the "
       "two meet at about age 6.6 near 4.9 x 10^6, and from age 8 to 20 they lie on top of each "
       "other, so the second half of the plate carries no information. THE ARITHMETIC BEHIND "
       "THEM DOES NOT CLOSE: equation (7) is printed with the constant 4868598 where the paper's "
       "own equation (5) and (6) give q0·wm^{3/4}/80^{3/4} = 4366737 - a 1.115 ratio, which is "
       "the same 1.115 that separates the two sheep counts later - and the model's plateau at "
       "4.36 x 10^6 kcal/day supports s(8) = 43 sheep rather than the 56 the text states, 56 "
       "requiring 5.68 x 10^6. The prose also gets its own age wrong: p9 says 'the difference "
       "between the intake and consumption is about 5 years old. The value reached the maximum' "
       "while the plotted intake peak is at age 5 and the crossing is at 6.6. No value is "
       "printed anywhere on the plate and no integral, no total and no error bar is drawn.",
       geometry("line", legend="inside", labels=True, numbers=True), "2", section_kind="result")

# ============================================================ 4.3: the food chain
figure(9, 1, "flowchart-or-schematic", CAP3, "text-layer",
       cited(9, 9, ["Figure 3"], 1,
             lead="The simplified food chain is shown in Figure 3."),
       S_43,
       "Three rounded boxes in a row with two grey block arrows between them, left to right: a "
       "long box 'Grass(corresponding to a certain grassland area)', then 'Sheep', then 'Dragon'. "
       "THE CHAIN IS DRAWN WITH NO TROPHIC LABEL AND NO RATE: the arrows carry no word, the "
       "boxes carry no quantity, and nothing on the plate marks predation, growth or conversion, "
       "although the model that follows turns each arrow into an equation (the sheep count s(a), "
       "the flock scale G, the forage demand). The parenthetical in the first box is the only "
       "thing tying the schematic to the region model, and it is a clause rather than a label. "
       "The paper's own paragraph two pages later calls the same chain 'herbage, sheep, dragon' "
       "in the summary, so the plate's first node is named Grass here and herbage there. The "
       "region is the shallowest measured on the paper (area 0.021, aspect 14.2) and the figure "
       "is a bare three-node strip much narrower than its caption's promise of a food chain.",
       geometry("flowchart-or-schematic", labels=True), "3", section_kind="model")

# ============================================================ 4.3: the modeling flow
figure(9, 2, "flowchart-or-schematic", CAP4, "text-layer",
       cited(9, 9, ["Figure 4"], 1,
             lead="Based on the above analysis, the main modeling ideas in this section are shown "
                  "in Figure 4."),
       S_43,
       "Four rounded boxes in a row with three grey block arrows, each box holding a wrapped "
       "phrase rather than a symbol or a quantity: 'The size of the sheep flock required under "
       "ecological balance', 'Total amount of grass needed to maintain the sheep flock', 'Grass "
       "yield per unit area under different climatic conditions', 'The area of grassland "
       "required for different climatic conditions (ie the food area of the dragon)'. The four "
       "boxes are the section's four unknowns in dependency order and the last one names the "
       "deliverable, so the strip is a correct dependency chain. WHAT IT DOES NOT CARRY IS ANY "
       "OF THE SECTION'S ARITHMETIC: no equation number, no symbol from the notation grid "
       "(neither sm, G, hi, Y nor S appears), no rate and no unit, so a reader cannot join the "
       "flow to equations (10) to (16) except by matching words; and the third box's 'different "
       "climatic conditions' is the only place the three named regions - arid, warm and polar - "
       "would belong, and they are not named. Its arrows, like Figure 3's, carry no label.",
       geometry("flowchart-or-schematic", panels=1, labels=True), "4", section_kind="model",
       order=2)

# ============================================================ 4.3.2: the coefficient grid
table(13, 1, S_432,
      "Four columns - 'Types of region' | Temperature | Rainfall | Sunshine hours - over three "
      "rows, arid, temperate and arctic, in a closed box with a rule between every row and a "
      "vertical rule between every column. THE BODY CELLS ARE NOT NUMBERS: each one is a "
      "Legendre expansion of degree three to five, keyed by a symbol - aT, aR, aS - that the "
      "header row does not explain, so the table is a coefficient list rather than a measurement "
      "table and cannot be read as a grid of values. THE HEADER AND THE BODY DISAGREE ON WHAT A "
      "COLUMN MEANS: the header names meteorological ELEMENTS (Temperature, Rainfall, Sunshine "
      "hours) while the cells are keyed by RESPONSE coefficients (aT, aR, aS), and the two "
      "readings only coincide because the column index and the subscript letter run together - "
      "the Temperature column is entirely aT, the Rainfall column entirely aR and the Sunshine "
      "column entirely aS, which is a layout convention the caption never states. THE CAPTION "
      "CALLS THE BODY SOMETHING ELSE AGAIN: it says 'sensitivity coefficient of monthly forage "
      "yield', and p11 defines that quantity hi (t) as a per-unit change in kg/hm2, whereas "
      "these cells are the coefficients aij of equation (17) - the fit, not the index - and the "
      "caption of the figure below says 'Change of sensitivity coefficients', using a third "
      "name for the same objects. ONE CELL IS A BARE HYPHEN: arid temperature has no expansion "
      "at all, so the paper fits two meteorological elements in the arid region and three in "
      "the other two, and no sentence says why - the omission is invisible in the surrounding "
      "text, which cites temperature[6] for the arid region on the very next page. THE "
      "COEFFICIENTS ARE PRINTED TO FOUR DIFFERENT PRECISIONS IN ONE COLUMN (1.681, 0.024, "
      "0.122, 0.518; 2.8522 against 17.128; 4.6 with one digit against 21.723 with three), so "
      "the columns cannot be decimal-aligned even though they are all in the same units. The "
      "degree of each expansion differs by cell - five in the arid rainfall row, three in "
      "temperate, two in arctic - and the polynomial index set starts at phi0 in some cells and "
      "phi1 in others, so the pairs are not comparable term by term. Cited once by the sentence "
      "above it, which introduces the table as the output of a computation the paper calls "
      "'successively calculated' and then never shows.",
      dict(rows=4, cols=4, header_rows=1, merged_cells=False, diagonal_header=False,
           units_in_header=False, decimal_aligned=False, orientation="portrait",
           note_sentence="", rule_style="boxed", zebra=False, numeric_cols=3, text_cols=1,
           width="full", continued=False),
      CAPT2, "text-layer",
      cited(13, 13, ["Table 2"], 1,
            lead="the sensitivity indexes of herbage yield to temperature[6], precipitation[7] "
                 "and sunshine[8] hours"),
      section_kind="result")

# ============================================================ 4.3.2: the three sensitivity curves
figure(13, 2, "line", CAP5, "text-layer",
       cited(13, 13, ["Figure 5"], 1,
             lead="of sensitive index of herbage yield to temperature, precipitation and sunshine "
                  "duration with month was made, as shown in Figure 5."),
       S_432,
       "Three panels side by side on one row, each a month-by-month polyline of a sensitivity "
       "coefficient: 'The impact of temperature change' (ordinate -100 to 100 ticked every 50), "
       "'The impact of sunshine hour' (ordinate -9.6 to -11.4 ticked every 0.2, an 1.8-unit "
       "window) and 'The impact of rainfall' (ordinate -3 to 3 ticked every 1). Abscissa 0 to 12 "
       "ticked every second month in all three, axis titles Month and 'Sensitivity Coefficient', "
       "a box legend inside each panel, curves drawn as straight chords between monthly samples "
       "with no markers. THE SERIES ARE COUNTRIES AND THE PAPER'S REGIONS ARE CLIMATES: the legend "
       "keys Egypt, Australia and Iceland, while every other passage in sections 4.3 and 4.4 "
       "works in arid, warm and polar regions and in Table 2's arid / temperate / arctic rows. "
       "The three country names appear ONCE in the whole paper, in one sentence on p22 ('The "
       "realworld data from Iceland, Australia and Egypt is used to simulate the herbage yield of "
       "the three types of areas'), so the reader must carry that sentence fifteen pages forward "
       "to map legend to row, and nothing on the plate does the mapping. THE THREE PANELS DO NOT "
       "SHARE A SCALE AND NO TWO OF THEM ARE ON THE SAME ORDER OF MAGNITUDE: temperature spans 200 "
       "units, rainfall 6 and sunshine 1.8, so a wiggle that fills half a panel's height means "
       "100 units in the first, 3 in the second and 0.9 in the third, and the reader who compares "
       "curve shapes across the row is comparing three magnifications a hundredfold apart. On "
       "that scale the sunshine window is the flattest of the three and the text reads all three "
       "as comparable sensitivity indexes. THE ORDINATES CARRY NO UNIT, although p11 defines the "
       "sensitivity index as kg/hm2 per unit of the element - the temperature axis is in hundreds "
       "of those and the sunshine axis in tenths - and the middle panel's window is centred on "
       "-10.5 rather than on zero, so the reader cannot see from the plate whether that element "
       "helps or hurts yield. Each panel is titled for the element and no panel repeats the "
       "region, so the three colours carry the only identity in the figure. Cited by the sentence "
       "above it, 'as shown in Figure 5'.",
       geometry("line", panels=3, layout="1x3", labels=True, numbers=True), "5",
       section_kind="result")

# ============================================================ 4.3.3: the three yields and areas
table(14, 1, S_433,
      "Four columns - 'Types of region' | Arid | Temperate | Arctic - over two body rows, 'Grass "
      "yield (kg/hm2× year)' and 'Predation area (hm2)', in a closed box with rules between the "
      "rows and between the columns. The three yields are 33087.43, 42858.35 and 21085.43 and the "
      "three areas 3738.08, 2382.62 and 4843.12. THE TABLE IS THE PAPER'S ONE ARITHMETICALLY "
      "CHECKABLE EXHIBIT AND ITS OWN TWO ROWS DO NOT MULTIPLY OUT: yield times area gives 1.237e8, "
      "1.021e8 and 1.021e8 kg/year, i.e. 338859, 279768 and 279779 kg/day, while the forage "
      "demand the paper states on p13 - 266609 sheep at 1.8 kg/day - is 479896 kg/day, so each "
      "region's printed area supports between 58 and 71 per cent of the flock the table exists to "
      "feed. Using the paper's earlier flock figure of 296297 sheep (533335 kg/day) the shortfall "
      "is larger still. The two rows are consistent only with each other if one divides the "
      "demand by the area, which implies yields of 46859, 73517 and 36167 kg/(hm2 year) - that is "
      "4686, 7352 and 3617 g/(m2 year) - and those are 2.1, 3.3 and 1.6 times Table 5's own NPP "
      "ceiling of 2200 g/(m2 year) for tropical rain forest, the most productive ecosystem the "
      "paper lists; so whichever row is right, the yield row exceeds every natural ecosystem in "
      "the paper's own table. THE COLUMN ORDER IS NOT THE ORDER OF THE REGIONS IN THE PROSE: the "
      "table runs arid, temperate, arctic, the text of 4.3.3 introduces 'arid, warm and polar', "
      "the caption of the figure below says 'different climates', and Figure 5's legend says "
      "Egypt, Australia and Iceland; 'warm' and 'temperate' are never equated, and neither are "
      "'polar' and 'arctic'. THE ROW LABEL'S UNIT IS BROKEN: 'kg/hm2× year' puts the multiplication "
      "sign between the area and the year without a space, so the quantity reads as kilograms per "
      "hectare-times-year rather than per hectare per year, and the area row is in hm2 with no "
      "per-anything. THE YIELDS CARRY TWO DECIMALS AND THE AREAS TWO, uniformly, which is the one "
      "place in the paper where a column is printed to a consistent precision. Cited twice on its "
      "own page - once by the lead-in that introduces it as the output of section 4.3.2 and once "
      "by 'Combined with Table 3 and Figure 6', the sentence that draws the region ranking from it.",
      dict(rows=3, cols=4, header_rows=1, merged_cells=False, diagonal_header=False,
           units_in_header=False, decimal_aligned=False, orientation="portrait",
           note_sentence="", rule_style="boxed", zebra=False, numeric_cols=3, text_cols=1,
           width="full", continued=False),
      CAPT3, "text-layer",
      cited(14, 14, ["Table 3"], 2,
            lead="the land area needed to support the life of dragons, as shown in Table 3."),
      section_kind="result")

# ============================================================ 4.3.3: the four plan views
figure(14, 2, "map-or-plan-view", CAP6, "text-layer",
       cited(14, 14, ["Figure 6", "Table 3"], 2,
             lead="it is easy to see that the area of land required by dragons to live in warm "
                  "regions is the smallest"),
       S_433,
       "Four plan-view panels in a 2x2 grid on square axes, all four on the same frame: "
       "x(km) and y(km) each 0 to 8 ticked every two kilometres, no north arrow, no scale bar, no "
       "grid. Three panels draw concentric rounded rectangles - an outer footprint in solid "
       "colour (Arctic cyan, Temperate green, Arid yellow), one nested box inside it and a small "
       "third inside that - with NO LEGEND AND NO LABEL on any of the three rings, so the three "
       "levels a reader might read as area, region and reserve are identified nowhere. The fourth "
       "panel is titled '100 Standard Olympic Track Field' and draws a single small red "
       "rectangle near (4.0, 4.0). MEASURED AGAINST THE PAGE'S OWN TABLE: Arctic's outer "
       "footprint spans about 5.7 by 6.1 km (34.8 km2) where Table 3 prints 4843.12 hm2 = "
       "48.43 km2; Arid about 5.0 by 5.3 km (26.5 km2) against 3738.08 hm2 = 37.38 km2; "
       "Temperate about 2.1 by 2.6 km (5.46 km2) against 2382.62 hm2 = 23.83 km2. The three "
       "drawn areas are therefore 0.72, 0.71 and 0.23 of their printed values - the ORDERING "
       "survives and the magnitudes do not, and the Temperate panel is off by more than four "
       "times. THE PANEL THAT MAKES THE PLATE READABLE HAS NO AREA ON IT: '100 Standard Olympic "
       "Track Field' is a unit of comparison, drawn as a red box about 1.0 by 1.0 km, and a "
       "standard 400 m track oval is nowhere near a square kilometre, so the comparison the "
       "fourth panel exists to supply cannot be used either. The prose's claim that 'the area of "
       "land required by dragons to live in warm regions is the smallest, followed by arid "
       "regions and the polar regions is the largest' does agree with both Table 3's ordering "
       "and the drawn ordering. The caption prints BELOW.",
       geometry("map-or-plan-view", panels=4, layout="2x2", labels=True), "6",
       section_kind="result")

# ============================================================ 4.4: the ecosystem levels
table(15, 1, S_44,
      "Four columns - Type of ecosystem | Level of assistance | Specie richness | Average "
      "biomass fi(kg/m2) - over seven ecosystems in a closed grid with a rule between every row, "
      "the caption above the header. As printed the seven rows descend by species richness: "
      "tropical rain forest at level 1 with biomass 45, temperate evergreen broad-leaved forest "
      "at 2 with 35, swamp and wetland at 3 with 12.3, savanna at 4 with 4, temperate grassland "
      "at 5 with 1.6, desert at 6 with 0.6 and ice sheet at 7 with 0.02. THE TWO VALUE COLUMNS "
      "ARE NOT THE SAME KIND OF NUMBER: the level column is an ordinal position from 1 to 7 "
      "assigned by the prose ('corresponding to 7 assistance levels, from high to low are "
      "recorded as Level 1, Level 2, Level 3...'), and it runs in the same direction as the "
      "biomass column, so the best-supported ecosystem carries the lowest level number - the "
      "opposite of what 'level of assistance' reads as, and the paper never says which way the "
      "scale runs. THE BIOMASS COLUMN IS PRINTED TO WILDLY VARYING PRECISION: 45 and 35 are "
      "integers, 12.3, 1.6 and 0.6 carry one decimal, 4 carries none and 0.02 carries two, so "
      "the column cannot be decimal-aligned and the ratio between the largest and smallest "
      "entries is 2250. 'Specie richness' is printed as a word in the header with NO VALUES "
      "BENEATH IT - the column has a heading and no cells - so the ordering the table is built "
      "on is asserted in the header and not shown in the grid; and the prose's justification "
      "('the higher the species richness of the ecosystem, the higher the level of aid') cannot "
      "be checked against a single printed richness figure. The unit kg/m2 appears in the header "
      "with the symbol's subscript broken off, and no row labels the ecosystem by climate region, "
      "so the connection to Table 3's arid / warm / polar is left to the body text, which "
      "asserts it on p16 ('The temperate grassland corresponds to the level 5 assitance'). Cited "
      "twice on its own page.",
      dict(rows=8, cols=4, header_rows=1, merged_cells=False, numeric_cols=3, text_cols=1,
           width="full", continued=False, **BOXED),
      CAPT4, "text-layer",
      cited(15, 15, ["Table 4"], 2,
            lead="Looking at the relevant data, we can get the average biomass per unit area of "
                 "different ecosystems, as shown in Table 4."),
      section_kind="model")

# ============================================================ 4.5.2: the NPP grid
table(17, 1, S_452,
      "Three columns - the ecosystem name, 'Average NPP(g/m2× year)' and 'Average biomass(kg/m2)' "
      "- over the same seven ecosystems in the same order and the same closed grid as Table 4: "
      "tropical rain forest 2200 and 45, temperate evergreen broad-leaved forest 1300 and 35, "
      "swamp and wetland 2000 and 12.3, savanna 900 and 4, temperate grassland 600 and 1.6, "
      "desert 140 and 0.6, ice sheet 3 and 0.02. THE BIOMASS COLUMN IS TABLE 4'S BIOMASS COLUMN "
      "REPEATED DIGIT FOR DIGIT, two pages apart, with no cross-reference and no note - so the "
      "paper prints one data set twice and the second printing is what equations (23) and (24) "
      "draw their f values from, which at least makes the two consistent by construction. THE "
      "NPP COLUMN IS THE ONE NEW DATA SET IN THE PAPER, and its ORDER IS NOT THE ORDER OF EITHER "
      "OF THE TABLE'S OTHER TWO COLUMNS: swamp and wetland takes 2000 g/(m2 year) - second only "
      "to the rain forest and above the temperate forest's 1300 - while its biomass is 12.3, a "
      "quarter of the forest's 35; so the table pairs a high-productivity, low-standing-stock "
      "ecosystem with its neighbours and the paper reads the two columns as if they ordered the "
      "same way. THE UNITS ARE SET THREE WAYS IN ONE HEADER ROW: 'g/m2× year' with a multiplication "
      "sign and no space before it, 'kg/m2' with none, and the ecosystem column with no unit at "
      "all. THE PAPER'S OWN WORKED EXAMPLE DOES NOT USE THE ROW IT NAMES: p17 computes "
      "'ecosystem types for Temperate evergreen forest ... degrade into Temperate grasslands' and "
      "substitutes (1300 - 600) and (35 - 1.6), which are the rows the table numbers 2 and 5 - "
      "both printed correctly - but the model's degradation pair is then asserted for a forest "
      "the table never identifies by latitude or climate. Cited by the sentence above it with "
      "the pointer set in lower case ('shown in table 5').",
      dict(rows=8, cols=3, header_rows=1, merged_cells=False, numeric_cols=2, text_cols=1,
           width="full", continued=False, **BOXED),
      CAPT5, "text-layer",
      cited(17, 17, ["table 5"], 1,
            lead="For relevant information, the average net primary production (NPP) and average "
                 "biomass values of different ecosystems are shown in table 5."),
      section_kind="result")

# ============================================================ 5.1: the two-panel deviation
figure(18, 1, "line", CAP7, "text-layer",
       cited(18, 18, ["Figure 7"], 1,
             lead="Through the above figure, it can be intuitively found that the model is "
                  "realatively stable."),
       S_51,
       "Two side-by-side MATLAB panels on x-title Age(year), ticks 0 to 12 every second year, "
       "each with a boxed legend inside the lower right listing three entries in the order "
       "'-3%' (dotted, blue), '+3%' (dashed, red-orange) and '+0%' (solid, yellow-orange). THE "
       "CAPTION AND THE PANELS DISAGREE ABOUT WHAT IS PLOTTED: the caption reads 'The deviation "
       "of Dragon's weight, daily intake if change the hypothesis weight at age 1 by +-3%' and "
       "promises a weight panel and a daily-intake panel, while BOTH panels carry the identical "
       "y-title 'Daily Intake(kcal)' - no panel on the plate is titled Weight, no panel letter "
       "or sub-title distinguishes them, and the two panels differ in scale only ('x 10^6' at the "
       "left panel's top left with ticks 0 to 7, 'x 10^5' at the right with ticks 0 to 18). "
       "Read against the two axes, the left panel peaks near 6.1 x 10^6 at age 4.8 and settles "
       "near 4.7 x 10^6, the right panel peaks near 17.3 x 10^5 at age 6.4 and settles near "
       "16.5 x 10^5 - so the two are not one quantity at two scales either, since their peaks "
       "sit two years apart. THE +-3% BAND IS NOT SYMMETRIC IN EITHER PANEL: at the plateau the "
       "left panel's +3% arm sits about 4.3% above the baseline and its -3% arm about 6.4% "
       "below, and the right panel's arms are about +4.8% and -10.3%, so at a stated symmetric "
       "perturbation one arm deviates roughly twice as far as the other and the two panels "
       "disagree with each other by a further factor of 1.5 to 2. THE FIGURE COVERS THREE OF THE "
       "TEN OFFSETS THE PAPER SWEEPS: the section immediately below prints +5 to -5 in unit steps "
       "in Tables 6 and 7, and the plate shows only the +-3% endpoints plus the baseline, at "
       "labelled percentages stated against the hypothesised age-1 weight rather than against "
       "the plotted quantity. All three curves are indistinguishable below about age 3 and again "
       "from age 8, so the deviation is drawn only in the growth window. The citing sentence "
       "('Through the above figure ... realatively stable') reads the plate without naming "
       "either panel.",
       geometry("line", panels=2, layout="1x2", legend="inside", labels=True), "7",
       section_kind="sensitivity")

# ============================================================ 5.2: the two offset grids
SENS = dict(rows=11, cols=8, header_rows=1, merged_cells=False, numeric_cols=7, text_cols=1,
            width="full", continued=False, **GRID)

table(19, 1, S_52,
      "Eight columns - 'Weight Offset' then ages 1 to 7 with a closing '>=8' column - over ten "
      "rows of offsets +5% to -5% in unit steps, ten-by-eight in a closed grid with a rule "
      "between every row. THE CORNER CELL IS SPLIT DIAGONALLY holding 'Age' above the diagonal "
      "and 'Weight Offset' below it, so the row header and the column header are one cell. THE "
      "GRID HAS TEN ROWS AND NO ZERO ROW: +5, +4, +3, +2, +1, -1, -2, -3, -4, -5, with the "
      "unperturbed case the figure two pages earlier plots as '+0%' printed nowhere, so the "
      "baseline the deviations are deviations FROM is not in the table. TRANSCRIBED: +5% 5.37 "
      "6.09 6.87 7.42 7.30 9.86 8.42 6.44; +4% 4.37 4.52 3.79 2.87 4.19 6.27 6.03 5.42; +3% 2.15 "
      "1.78 2.36 2.44 2.89 4.27 5.02 5.36; +2% 2.13 2.35 3.48 4.62 4.35 3.52 4.07 4.35; +1% "
      "0.02 0.01 0.01 0.18 1.18 2.03 2.15 2.17; -1% 0.07 0.09 0.19 0.19 2.30 2.39 2.78 3.05; "
      "-2% 1.03 1.27 1.98 2.37 2.05 3.40 3.57 3.92; -3% 2.33 1.54 2.88 2.97 3.23 3.89 4.12 "
      "5.22; -4% 3.33 4.52 3.79 3.60 4.19 7.23 6.58 6.72; -5% 6.28 5.40 3.21 8.32 8.54 11.23 "
      "9.87 8.40. NO COLUMN IS MONOTONE IN THE OFFSET, in either direction: at age 5 the +2% row "
      "prints 4.35 against the +3% row's 2.89, and the +4% row's 4.19 against the +5% row's 7.30; "
      "the +1% row is the column minimum at every one of the eight ages, so the smallest "
      "perturbation gives the smallest deviation on both signs and the response is not smooth "
      "through zero. TWO ROWS ARE IDENTICAL CELL BY CELL where they should differ: +4% and -4% "
      "print the same values at ages 2 (4.52), 3 (3.79) and 5 (4.19), three of eight columns. ONE "
      "CELL IS OUT OF FAMILY: -5% at age 3 prints 3.21% where its own row runs 5.40 and 8.32 on "
      "either side and every -2, -3 and -4 value in that column is higher. NO CELL CARRIES A "
      "UNIT: the caption's 'deviation' is not defined as a percentage of weight or of the age-1 "
      "weight, and the + signs on the positive rows and the bare digits on the negative rows are "
      "the only indication of direction. The caption prints ABOVE, and the grid carries no note.",
      SENS, CAPT6, "text-layer",
      cited(19, 19, ["Table 6", "Table 7"], 1,
            lead="The results show that the dragon’s weight and stability of the required energy "
                 "are not good enough, but it is still acceptable."),
      section_kind="sensitivity", order=1)

table(19, 2, S_52,
      "The same ten-by-eight template as Table 6, with the corner cell split between 'Age' and "
      "'Intake Offset' and the same ten offsets (no zero row) over ages 1 to 7 plus '>=8': "
      "+5% 4.27 6.09 7.80 6.54 6.72 11.32 12.36 12.68; +4% 4.56 5.32 3.97 3.29 5.32 7.84 5.46 "
      "8.78; +3% 3.15 2.89 3.35 3.62 3.98 5.67 5.98 8.98; +2% 2.35 3.35 4.52 4.52 5.34 4.36 4.80 "
      "5.90; +1% 0.35 0.45 1.34 1.02 1.89 3.65 3.98 2.17; -1% 0.43 0.18 4.23 1.53 2.58 4.56 3.42 "
      "2.89; -2% 3.21 3.45 2.36 2.66 3.45 4.78 3.89 4.57; -3% 3.56 4.56 4.88 3.98 3.89 4.20 6.53 "
      "8.22; -4% 4.52 4.32 5.68 4.58 6.09 7.89 7.88 8.98; -5% 7.68 8.62 3.90 9.34 9.52 10.42 "
      "11.42 11.35. THE TWO GRIDS USE THE SAME TEMPLATE BUT NOT THE SAME COLUMNS: Table 6 is "
      "monotone in the offset and this one is not at any age either - the +1% row is the column "
      "minimum at five of the eight ages and the -1% row at the other three, and at age 3 the "
      "+1% row prints 1.34 against the -1% row's 4.23. "
      "ONE CELL IS WILDLY OUT OF FAMILY: -1% at age 3 prints 4.23% between 0.18% and 1.53% on its "
      "own row, and -5% at age 3 prints 3.90% between 8.62% and 9.34% on its own row, so the "
      "age-3 column holds two numbers that belong to neither neighbouring offset nor to their "
      "own row. THE TWO GRIDS DISAGREE ABOUT WHICH ROW IS THE OUTLIER: -5% is the column maximum at "
      "seven of the eight ages in Table 6 and at only five of eight here, and the +5% row is the "
      "column maximum at ages 3, 6, 7 and in the closing '>=8' column here against only ages 2 "
      "and 3 there. The +1% row is the column minimum at all eight ages in Table 6 and at five "
      "of eight here, so the smallest perturbation gives the smallest deviation on both signs "
      "without exception in the weight grid and with three exceptions in the intake grid. NO ROW "
      "OR COLUMN SUMS, no baseline row exists, and no cell carries a unit. Both grids are named "
      "in one sentence, which is the only sentence either has.",
      SENS, CAPT7, "text-layer",
      cited(19, 19, ["Table 6", "Table 7"], 1,
            lead="The results show that the dragon’s weight and stability of the required energy "
                 "are not good enough, but it is still acceptable."),
      section_kind="sensitivity", order=2)

BANNER = ("The addressee block of the closing letter: a two-path vector rule pair holding 'To: "
          "George R.R. Martin / Date: Sunday, Janurary 26 , 2019 / Subject: Fun Facts About "
          "'Game of Thrones ': The Ecological Impacts of Dragons'. Measured as a region because "
          "the letter's header rules bracket it; no exhibit of any kind.")

exclude(22, 1, "not-an-exhibit", BANNER)

RULES = [
    "Measure first, then read the pixels: fifteen measured regions over twenty-four pages "
    "resolve into seven figure rows, seven table rows and one refusal, with nothing unaccounted "
    "[place.doc_order].",
    "The paper prints no Table 1: p13's prose cites 'table 1' for the integral regression model "
    "that is equation (16), and the only unnumbered grid is the notation block on p5, captioned "
    "by its own section heading [table.header_rows].",
    "The mass-age figure draws the equation it prints but the equation contradicts the paper's "
    "own data: the curve follows the pasted logistic at yearly samples to within 0.03 x 10^5, "
    "while that logistic returns 112.45 kg at age 1 against the 35 kg the text states, and no "
    "real (wm, r0) satisfies w(0)=10, w(1)=35, w(3)=14000 at once [geometry.family].",
    "The paper's own constants disagree by a factor of 1.115 in three places: equation (7)'s "
    "4868598 against q0·wm^{3/4}/80^{3/4} = 4366737, and the two sheep counts 296297 (p11) "
    "against 266609 (p13) with their two forage demands 533335 and 479896 kg/day "
    "[table.text_cols].",
    "Both sensitivity grids print ten offsets +5 to -5 and no 0% row, on a seven-column age grid "
    "closed by a '>=8' column, with the corner cell split diagonally between 'Age' and the "
    "offset label [table.diagonal_header].",
    "Two of the four plan-view panels carry no area label at all, and all three labelled panels "
    "under-draw the areas Table 3 prints: arctic 34.8 against 48.43 km2, arid 26.5 against "
    "37.38, temperate 5.46 against 23.83 [geometry.family].",
    "Figure 7's caption promises a weight panel and a daily-intake panel, and both panels are "
    "labelled 'Daily Intake(kcal)' - no panel on the plate is titled Weight [caption.verbatim].",
    "The notation grid's unit column is empty on four rows and inconsistent on two more: ni is "
    "g × year/m2 where the reduced quantity below it is g/year, and sm's unit day -1 is attached "
    "to a count [table.numeric_cols].",
    "Two exhibits carry no sentence that names them - the notation grid, captioned only by its "
    "section heading, and Figure 5, whose citation is the deictic 'as shown in Figure 5' "
    "following a sentence about sensitivity indexes [mention.count].",
    "The one region refused is the closing letter's addressee block, measured because the "
    "letter's header rules bracket it [place.page_zone].",
    "Seven of the fourteen exhibits are printed tables, and the paper's only plan-view plate is "
    "drawn from the same three numbers the adjacent table prints [geometry.panel_count]",
]

NOTE = """\
Paper 189, Team 1902727: the dragons of A Song of Ice and Fire, for problem A 2019. A logistic
mass-age fit, a Kleiber-law energy budget, a Malthus sheep flock, a Legendre-polynomial forage
regression over three climate regions, a seven-level ecosystem table, an NPP degradation model,
and a ten-offset sensitivity sweep. Twenty-four pages, fifteen measured regions, of which
fourteen are exhibits: SEVEN FIGURE ROWS and SEVEN TABLE ROWS, one refusal, nothing unaccounted.

THE MODEL'S TWO CONSTANTS DO NOT AGREE WITH THE MODEL. Equation (7) prints the Kleiber
coefficient as 4868598; substituting the paper's own equation (4) into equation (6) with q0 =
1926/0.7 gives 4366737, a ratio of 1.115. The same 1.115 appears again downstream: p11 carries
the flock scale as 296297 and the forage demand as 533335 kg/day, p13 carries 266609 and 479896
kg/day, and the two pairs differ by exactly that factor, so one of the two passages was written
with the other's constant. Neither passage says which.

THE LOGISTIC CANNOT PASS THROUGH ITS OWN DATA POINTS. The text fixes w(0)=10, w(1)=35 and
w(3)=14000 and then prints a three-parameter logistic. Solved exactly, those three constraints
have no real solution; the printed coefficients give w(1) = 112.45 kg, three times the stated
35 kg, and an asymptote of 1.481 million kg - 1481 tonnes, which the summary rounds to
'14.8 x 10^5 kg' and Figure 1 draws as a flat line from age 7. Figure 1 does draw the printed
logistic - digitized, the stroke sits within 0.03 x 10^5 of eq (4) evaluated at whole ages and
joined by straight chords, so between samples it departs from the smooth curve by at most about
0.9 x 10^5 - which means the 112 kg the plate shows at age 1 is the equation's value and the
35 kg is the prose's, and the large dragon clip art pasted over ages 2 to 9 hides the segment
where a reader would have noticed.

THE TWO SHEEP MODELS ARE ONE MODEL WITH TWO RATES. Equation (12) gives G = sm/(e^{b-d} - 1) with
the text's b-d = 0.0567, which would give G = 2880 and a negative breeding time; with b-d read
as a percentage, 0.000567, it gives G = 296212 and T = 16.4 years, which matches p11. p13's
266609 corresponds to b-d = 0.00063, i.e. to the assumptions page's 0.107% minus 0.044%, so the
paper switches from one rate to the other without a word and the two sheep counts, the two
forage demands and the two grassland areas all inherit the switch.

SEVEN OF THE FOURTEEN EXHIBITS ARE PRINTED TABLES, and the four plan views are drawn from the
same three numbers. Table 4 assigns seven ecosystems an assistance level 1 to 7 and a biomass;
Table 5 prints for the same seven the NPP and a biomass column that duplicates Table 4's exactly,
so the paper's one ecological data set is printed twice. Table 3's three areas imply forage
yields of 46859, 73517 and 36167 kg/(hm2 year) - between 3617 and 7352 g/(m2 year) - where
Table 5's own ceiling for the most productive ecosystem is 2200 g/(m2 year), so the three
regions the paper computes are two to three times more productive than any ecosystem in its own
table. Figure 6 draws the three areas as plan-view rectangles and the fourth panel as a single
red box labelled '100 Standard Olympic Track Field'; measured against Table 3 the drawn areas
are 0.72, 0.71 and 0.23 of the printed ones, so the ORDERING survives and the magnitudes do not.

THE SENSITIVITY SECTION IS TWO OFFSET GRIDS AND ONE FIGURE, and they do not cover the same
ground. Tables 6 and 7 print ten offsets, +5% to -5% in unit steps, over ages 1 to 7 and a
closing '>=8' column, all in per-cent deviation; Figure 7 prints only -3%, +3% and +0%, and
both its panels are titled 'Daily Intake(kcal)' although the caption promises a weight panel and
an intake panel. On the plate the +-3% curves do not straddle the baseline evenly - the right
panel's negative arm deviates about twice as far as its positive arm - and the two panels fan
differently from the same stated perturbation. Inside the grids the numbers are more orderly but
still anomalous: Table 6 gives +4% and -4% identical values at ages 2, 3 and 5 (4.52%, 3.79%,
4.19%), and Table 7 has -1% at age 3 printing 4.23% between 0.18% and 1.53%.

WHAT THE PAPER DOES WELL: every equation the exhibits rest on is printed with its number, the
two flow charts are correct dependency strips, the seven-level ecosystem ordering is stated in
one sentence and then used consistently, and the closing letter's four headline claims - 50+
sheep a day, 3738/2383/4843 hm2, 3.81 x 10^7 kg, 1.75 x 10^10 g of NPP - are each traceable to
a printed exhibit. The failures are internal: constants that do not propagate, a fit that cannot
produce its own points, and a sensitivity figure that answers a narrower question than its
caption asks.

Families: table-grid 7 (notation, Tables 2 to 7), line 4 (Figures 1, 2, 5, 7),
flowchart-or-schematic 2 (Figures 3, 4), map-or-plan-view 1 (Figure 6).
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

out = PROXY / "pc189-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
