"""Hand census of P-A-2015-32150-b7715ba1 (A-32150, 36 pages).

Forty-five measured regions over twenty pages: 31 figure rows, 7 table rows, 7 exclusions,
nothing unmeasured. The paper prints 19 captioned figures (Figures 1 to 19, with Figures 2,
8, 13, 14, 16 and 19 printed as multi-panel groups), one uncaptioned reprint of the
delivery map, five numbered tables, and one unnumbered symbol grid that breaks over the
page turn.

   p3 r1   Figure 1    CDC choropleth of the outbreak, 4 February 2015
   p6 r1   symbol grid rows 1-7
   p7 r1   symbol grid rows 8-19
   p9 r1   Figure 2a   Guinea panel
   p9 r2   Figure 2b   Sierra Leone panel
  p10 r1   Figure 2c   Liberia panel
  p10 r2   Figure 3     SEIHCR (CT) compartmental schematic
  p14 r1   Figure 4     cumulative cases, Guinea
  p14 r2   Figure 5     cumulative cases, Sierra Leone
  p15 r1   Figure 6     cumulative cases, Liberia
  p16 r1   Figure 7     unit dose per day, three countries
  p17 r1   Figure 8a    cumulative patients in Freetown
  p17 r2   Figure 8b    medicine per week in Freetown
  p20 r1   Figure 9     J_m against cluster count c
  p20 r2   Figure 10    delivery locations, 4 February baseline
  p21 r1   Table 2      locations of the six headquarters
  p21 r2   Table 3      doses per headquarters, every four weeks
  p22 r1   Table 4      doses per country, every four weeks
  p23 r1   Figure 11    gamma_H sensitivity
  p24 r1   Figure 12    delta_H sensitivity
  p25 r1   Figure 13a   alpha = 0.05
  p25 r2   Figure 13b   alpha = 0.1
  p25 r3   Figure 13c   alpha = 0.3
  p25 r4   Figure 13d   alpha = 0.2
  p27 r1   Figure 14b   panel 2, kappa
  p27 r2   Figure 14a   panel 1, alpha
  p27 r3   Figure 14d   panel 4, delta_H
  p27 r4   Figure 14c   panel 3, 1/gamma_H
  p27 r5   Table 5      parameter bands by colour
  p28 r1   Figure 15    eradicating date against introduction time
  p29 r1   Figure 16a   efficacy of medicine, red fan
  p29 r2   Figure 16b   efficacy of medicine, cyan fan
  p29 r3   Figure 17    transmission-rate fan with a grey envelope
  p30 r1   Figure 18    incubation-period fan
  p31 r1   Figure 19a   noise on delta_H, left panel
  p31 r2   Figure 19b   noise on delta_H, right panel
  p33 r1   uncaptioned  reprint of the delivery map, 14 February baseline
  p34 r1   uncaptioned  reprint of Table 2

Exclusions: p3 r2, p4 r1, p11 r1, p11 r2, p12 r1 are the 14.2 pt text-background bands behind
displayed equations and the intro, and p35 r1, p36 r1 are bibliography hangers.

Declared gap: Table 1 on p8 owns no region. Its three rules print at 598.15, 617.71 and
746.98 pt - 414.9 pt wide, 99.2 per cent of the 418.3 pt measure - but the last cell is
painted with a near-white fill (0.976) at 435.3 to 483.3 pt by 726.8 to 741.0 pt, 6.0 pt
above the closing rule, so at tol 8 the fill and the rule fuse into a 21.6 pt cluster that
fails RULE_HEIGHT_PT, and the two rules left over span 19.6 pt, under MIN_SIDE_PT. The grid
is real: header 'Parameter Guinea Sierra Leone Liberia' at 603.4 pt over R0 1.51 / 2.53 /
1.59, transmission rate without control intervention 0.27 / 0.45 / 0.28, k 0.048 three
times, and N 12,000,000 / 6,100,000 / 4,092,310. It is named in the note instead of being
given a box it does not own.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2015-32150-b7715ba1"
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


def place(page: int, reg: int, kind: str, numbered: bool = True) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(c["section_path"]),
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
           kind: str, *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           three_d: str = "no", source: str = "text-layer", numbered: bool = True,
           position: str = "below", note: str = "", other_note: str = "") -> None:
    word = qp(cap, [page - 1, page, page + 1]) if (cap and source == "text-layer") else schema.norm(cap)
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
        "place": place(page, reg, kind, numbered),
        "mention": mention,
        "caption": caption(word, numbering, position),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": False, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, rows: int, cols: int, kind: str,
          note_sentence: str, note: str, *, rule: str = "booktabs", numeric: int = 1,
          header_rows: int = 1, numbered: bool = True, width: str = "full",
          zebra: bool = False, merged: bool = False, decimal: bool = False,
          diagonal: bool = False, continued: bool = False, cap: str = "",
          position: str = "above", mention: dict | None = None,
          source: str = "text-layer") -> None:
    word = qp(cap, [page - 1, page, page + 1]) if cap else ""
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": word,
        "caption_source": source if cap else "none",
        "note": note,
        "place": place(page, reg, kind, numbered),
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


# ---------------------------------------------------------------- p3, the CDC map
figure(3, 1, "map-or-plan-view",
       "Figure 1. Ebola Outbreak Distribution Map in West Africa on 4th Feb, 2015",
       "Figure N.", none_mention(), "introduction",
       legend="inside", numbers=True, labels=True,
       note="A 665x565 px pasted raster, 286.5 by 243.3 pt - 68.5 per cent of the measure - "
            "at 154.4 to 440.9 pt by 313.7 to 557.0 pt, and the only exhibit on the paper that "
            "comes from a published source rather than from the team's own MATLAB session. "
            "Administrative districts are filled in five orange steps keyed 1-5, 6-20, 21-100, "
            "101-500 and 501-4,000 under a 'Total Cases' heading in the lower-left legend, with "
            "a sixth empty swatch for 'No cases reported' and two outlined keys below it, 'Newly "
            "Infected' and 'Cases in last 21 days'. Country names print in a large maroon serif; "
            "the WHO roadmap date '04 February 2015' and its source line are burned into the "
            "image's lower right. The caption prints 5.1 pt under the art and carries the CDC "
            "page URL on its second line, which the text layer reproduces as body text - that "
            "URL is the only caption on the paper that names a source. The map is cut at the "
            "left edge of its own frame, so Guinea-Bissau is clipped mid-label. The prose never "
            "names the figure by number: it introduces it with 'countries can be seen clearly "
            "by the latest outbreak situation graph released by the World Health Organization'.")

# ---------------------------------------------------------------- p6 and p7, the symbol grid
table(6, 1, 8, 2, "symbols", "",
      "The first half of the paper's only unnumbered grid: a two-column Symbol / Description "
      "list introduced by the heading '3.2. Symbol Description' and nothing else - no table "
      "number, no caption, no note. Eight printed rows: the header band 'Symbol Description' "
      "at 613.8 pt and seven symbols from R0 to C(t), each description a full clause ('Number "
      "of infectious individuals outside hospital at time t'). The ruling is the paper's one "
      "register with a rule under EVERY body row: a 1.44 pt rule at 608.6 pt, another 1.44 pt "
      "at 628.1 pt under the header, then 0.48 pt rules at 647.6, 666.1, 684.6, 703.1, 721.5, "
      "740.0 and 758.6 pt, all of them full measure, every one broken into two segments at x "
      "196.4 pt with a 1.4 pt gap where the column gutter falls. No vertical stroke anywhere, "
      "no side or foot border, so rule_style is booktabs as the nearest of the four closed "
      "labels and this note carries the truth that every row is ruled. 415.7 pt wide, 99.4 per "
      "cent of the measure. The Symbol column is typeset maths and arrives as private-use "
      "glyphs; the Description column is plain text.",
      numeric=0, header_rows=1, continued=False)

table(7, 1, 12, 2, "symbols", "",
      "The second half of the same grid, continued over the page turn with NO header row "
      "repeated: twelve more symbols from R(t) and CUM(t) through the three transmission rates, "
      "1/sigma, alpha, the gamma, delta, pi and omega pairs, 1/psi and kappa to the ratio of "
      "exposure probabilities. Twelve 0.48 pt rules at 72.0, 90.5, 109.0, 145.6, 164.1, 182.5, "
      "219.0, 255.5, 292.0, 310.6, 347.1 and 383.6 pt, one above each row, and the 1.44 pt "
      "closing rule at 456.2 pt. The measured box begins at 61.6 pt on the running-head rule, "
      "which is not part of the grid: the rule at 61.6 pt spans 88.6 to 506.9 pt at 0.72 pt and "
      "is the head of the page. The last two rows are multi-line descriptions ('Ratio of "
      "probability that contact traced individual is (exposed, infectious) at time of "
      "originating case identification to the probability a random individual in the population "
      "is (exposed, infectious)') and the right-hand column of the description runs from x 201.8 "
      "pt to 505.2 pt, so the grid's 19 rows do not line up with the rule count on either page.",
      numeric=0, header_rows=1, continued=True)

# ---------------------------------------------------------------- p9 and p10, Figure 2
FIG2 = "Figure 2. Cumulative number of individuals for Guinea, Sierra Leone and Liberia respectively"

figure(9, 1, "line", FIG2, "Figure N.", none_mention(), "result", legend="inside",
       note="The Guinea panel of a three-panel figure whose single caption prints on p10 under "
            "the Liberia panel, 168 pt away from this box: 272.0 by 195.9 pt of pasted MATLAB "
            "raster, 65.0 per cent of the measure. 'Cumulative number of individuals' 0 to 3500 "
            "in steps of 500 against 'Time (day)' 0 to 350 in steps of 50: a dash-dot series "
            "with x markers labelled 'Actual Data' over a plain solid 'Calculated Data' curve, "
            "legend in a box inside the axes at upper centre, no gridlines, full frame. The panel "
            "title 'Guinea' prints at 380.6 pt above the art, inside the measured box. Printed "
            "defect: past day 300 the calculated curve sits 250 to 350 individuals under the "
            "reported trace, and the dashed observed series breaks up around day 240.")

figure(9, 2, "line", FIG2, "Figure N.", none_mention(), "result", legend="inside",
       note="The Sierra Leone panel, measured as its own box 205.4 pt below the Guinea panel "
            "and 1006.0 pt from the caption it shares. Same two series and the same dash-dot "
            "over solid convention, legend at upper right rather than upper centre, y axis 0 to "
            "12000 in steps of 2000, x axis 0 to 350. The panel title 'Sierra Leone' prints at "
            "583.3 pt between the two boxes. Printed defect: the observed series ends near day "
            "330 at about 11,000 while the calculated curve is still at 9,500 at day 340, a "
            "divergence of some 1,500 cases that the prose never mentions, and the marker points "
            "are sparse enough that the trace is interrupted for long stretches.")

figure(10, 1, "line", FIG2, "Figure N.", none_mention(), "result", legend="inside",
       note="The Liberia panel, and the box the caption belongs to: the quote prints 12.4 pt "
            "under it at 295.4 pt. Y axis 0 to 9000 in steps of 1000, x axis 0 to 350, legend "
            "upper centre. Printed defect: the observed x markers detach from their connecting "
            "dash-dot line over days 215 to 255, and the two curves cross twice - near day 210 "
            "and again near day 292 - with the observed series finishing above the calculated "
            "one, 8,600 against 7,700. Three panels, one caption, three measured boxes, so three "
            "rows; the phrase 'respectively' is the only thing that maps a panel to a country, "
            "and it maps them in the order Guinea, Sierra Leone, Liberia.")

# ---------------------------------------------------------------- p10, the schematic
figure(10, 2, "flowchart-or-schematic",
       "Figure 3. Compartmental flow of the SEIHCR (CT) model", "Figure N.",
       cited(10, 10, ["Figure 3"], 2,
             "Figure 3 shows a schematic presentation of the improved model SEIHCR (CT), and "
             "indicates the compartmental states and the transition rates among the states."),
       "model", labels=True,
       note="294.3 by 146.0 pt of true vector line work - the paper's only diagram and one of "
            "only two exhibits not pasted as raster. Six rounded boxes in a row-major flow: S to "
            "E to I along the top left, each arrow labelled with its rate (lambda, sigma), then "
            "a dashed frame labelled 'CUM' enclosing the four compartments H, C, I and R with "
            "the recovery and death transitions drawn as cross arrows labelled alpha, "
            "(1-delta_H)gamma_H, delta_H v_H, (1-delta_I)gamma_I, delta_I v_I and psi. No axes, "
            "no numbers, no legend; the only printed text inside the art is the six compartment "
            "letters, the CUM frame title and the rate labels, all set in the paper's own "
            "equation font and therefore arriving in the text layer as private-use glyphs. Cited "
            "twice by number on p10, once in the prose above it and once in its own caption.")

# ---------------------------------------------------------------- p14 and p15, Figures 4 to 6
ABSTRACT45 = ("The model’s results (Fig.4,5,6), whose parameters are decided using computer "
              "simulation")

figure(14, 1, "line",
       "Figure 4. Simulation of cumulative cases in Guinea from March 25th, 2014 to Feb 4th,",
       "Figure N.", cited(1, 14, ["Fig.4"], 1, ABSTRACT45, pattern="parenthetical"), "result",
       legend="inside",
       note="276.1 by 207.0 pt of pasted raster, 66.0 per cent of the measure. 'Cumulative "
            "number of individuals' 0 to 3000 in steps of 500 against 'Time (day)' 0 to 350 in "
            "steps of 50; dash-dot 'Actual Data' with markers over a solid 'Calculated Data' "
            "curve, legend in a box inside the axes at upper centre, no gridlines, four-spine "
            "frame. Between this box and the next the page prints the fitted parameter block as "
            "body text - N = 12,000,000, beta_I0 = 0.205, alpha = 0.2, gamma_I = 1/32, "
            "gamma_H = 1/10, v_I = 1/8, kappa = 0, k = 0.03, tau = 200 - which belongs to the "
            "figure but prints as a paragraph between the two, not inside either art. The "
            "caption is cut by the layer at its date: the printed line ends at 'to Feb 4th,' and "
            "the year continues into the maths. The abstract names Figs 4, 5 and 6 in one "
            "parenthetical, which is the only by-number citation any of the three ever gets.")

figure(14, 2, "line",
       "Figure 5. Simulation of cumulative cases in Sierra Leone from May 27th, 2014 to Feb",
       "Figure N.", cited(1, 14, ["Fig.4,5,6"], 1, ABSTRACT45, pattern="parenthetical"), "result",
       legend="inside",
       note="The Sierra Leone half of the pair, 69.1 pt under the first, same 276.1 by 207.0 pt "
            "box. Y axis 0 to 12000, x axis 0 to 250 - the shortest time axis on the paper, and "
            "shorter than the Guinea axis by 100 days because the Sierra Leone series starts two "
            "months later. Dash-dot observed over solid calculated, legend upper centre, no "
            "gridlines. Its fitted parameter block prints BELOW its caption, unlike Figure 4's. "
            "The caption is again cut at the date by the layer ('to Feb' with the day and year "
            "swallowed by the maths run).")

figure(15, 1, "line",
       "Figure 6. Simulation of cumulative cases in Liberia from March 27th, 2014 to Feb 4th,",
       "Figure N.", cited(1, 15, ["Fig.4,5,6"], 1, ABSTRACT45, pattern="parenthetical"), "result",
       legend="inside",
       note="The third simulation chart, alone at the head of p15 and the only exhibit on that "
            "page. Same 276.1 by 207.0 pt raster and the same two-series convention, but the "
            "observed trace carries asterisk markers rather than the x of Figures 4 and 5, and "
            "the marker count is roughly half: this is a country whose reporting is thinner. Y "
            "axis 0 to 9000 in steps of 1000, x axis 0 to 350. Legend boxed inside the axes at "
            "upper centre. No legend entry is added for the asterisks, so a reader has to infer "
            "that they are the same 'Actual Data' key as before from the dash-dot line they sit "
            "on.")

# ---------------------------------------------------------------- p16, the dose chart
figure(16, 1, "line",
       "Figure 7. Unit dose of the medicine needed per day for Guinea, Liberia and Sierra Leone",
       "Figure N.",
       cited(1, 16, ["Fig.7"], 1,
             "The total quantity of the medicine needed is based on the cumulative number of "
             "individuals CUM (Fig.7).", pattern="parenthetical"),
       "result", legend="above", numbers=False, labels=True,
       note="True vector line work, 398.3 by 222.7 pt, the widest single-panel exhibit on the "
            "paper at 95.2 per cent of the measure. 'Unit dose of the medicine needed' 0 to 2500 "
            "in steps of 500 against a calendar x axis from 12/30/13 to 01/31/15 in fourteen "
            "ticks. Four things are inked: a light grey filled area for the total quantity, "
            "peaking near 2,250 units, and three heavy unmarked country curves in blue (Guinea, "
            "about 430), orange (Liberia, about 880) and green (Sierra Leone, about 1,450). The "
            "four-key legend prints ABOVE the axes rather than inside them, which is why "
            "geometry.legend is 'above'. Light horizontal gridlines run behind the curves. "
            "Printed defect: the caption says 'per day' while the axis reads 'Unit dose of the "
            "medicine needed', and the prose calls the blue, orange and green curves the dose of "
            "each country without saying which is which.")

# ---------------------------------------------------------------- p17, the two-panel Figure 8
FIG8 = "Figure 8. Cumulative number of patients in Freetown and quantity of needed medicine per week"
FIG8M = cited(17, 17, ["Figure 8"], 2,
              "The left graph in Figure 8 presents the changes of the cumulative numbers with "
              "time in Freetown.")

figure(17, 1, "line", FIG8, "Figure N.", FIG8M, "result", legend="inside",
       note="The LEFT panel of Figure 8: 226.7 by 170.4 pt, pasted raster, 54.2 per cent of the "
            "measure, and the first of two boxes printed side by side with one caption centred "
            "under the pair at 457.0 pt. 'Cumulative number of individuals' 0 to 2500 against "
            "'Time (day)' 0 to 300, dash-dot observed with x markers over solid calculated, "
            "legend boxed inside at upper centre, no gridlines. The right-hand box overhangs the "
            "text measure: it ends at 529.8 pt where the measure ends at 508.4 pt, so the pair "
            "breaks the right margin by 21.4 pt while this box stops at 292.2 pt. Printed defect: "
            "the calculated curve stops near day 280 and the observed markers near day 250, so "
            "the last thirty days of the panel hold one line only.")

figure(17, 2, "line", FIG8, "Figure N.", FIG8M, "result", legend="inside",
       note="The RIGHT panel of Figure 8: the same 226.7 by 170.4 pt box, but a different "
            "quantity and a different ink. 'Unit dose of the medicine needed' 0 to 500 in steps "
            "of 100 against 'time (day)' 0 to 300 - the axis label is lowercase here where the "
            "left panel's is capitalised. A grey filled area labelled 'Calculated Data' peaks "
            "near 450 units at day 180; an open-circle black line labelled 'Actual Data' peaks "
            "near 500 at day 225 and falls to 85 by day 265, cutting the filled area twice, near "
            "day 180 and again near day 240. Legend boxed inside at upper right. The prose that "
            "names the figure speaks only of the left graph, so nothing in the text tells a "
            "reader what the circle series is beyond the legend key.")

# ---------------------------------------------------------------- p20, the cluster curve and the map
figure(20, 1, "line",
       "Figure 9. The variation of J m with c", "Figure N.",
       cited(20, 20, ["Figure 9"], 2,
             "From Figure 9, we can see that choosing 6 clusters and consequently 6 headquarters"),
       "result", numbers=True, labels=True,
       note="268.4 by 188.6 pt of pasted raster, 64.2 per cent of the measure. Thirteen open "
            "circles joined by a heavy black line on an axis of 'c', the cluster count, 0 to 14 "
            "in steps of 2 against J_m 0 to 8000 in steps of 1000, falling from 7,600 at c = 1 to "
            "1,300 at c = 13. Dotted gridlines in both directions - the only exhibit on the paper "
            "with a full grid. The art annotates itself: an arrow labelled 'Inflection Point' "
            "points to the circle at c = 6, about 2,500, and a solid vertical guideline drops "
            "from it to the axis. That annotation is what the prose reads off ('choosing 6 "
            "clusters'), so the cluster number the whole delivery system rests on is printed "
            "inside a picture and nowhere in the text. The y axis label arrives from the layer as "
            "the two fragments 'J' and 'm', which is the subscript.")


# ---------------------------------------------------------------- p21 and p22, Tables 2 to 4
table(21, 1, 3, 7, "result",
      "The geographical locations for these 6 headquarters are presented in Table 2.",
      "A three-row, seven-column booktabs grid - header 'Location 1 2 3 4 5 6' over Latitude "
      "and Longitude - ruled at 151.8, 171.4 and 207.9 pt, the outer rules 1.44 pt thick and the "
      "header rule 0.48 pt, every rule broken into seven segments at the gutters, no vertical "
      "stroke, no side border. 440.2 pt wide against the 418.3 pt measure: 105.2 per cent, so "
      "the grid overhangs BOTH margins, by 12.8 pt on the left and 9.0 pt on the right, which "
      "makes it the widest exhibit in the paper and the only one that leaves the text block on "
      "both sides. Six coordinate columns of degrees with a hemisphere letter, right-aligned "
      "within their columns but not on any decimal rule. Printed defect: the sixth latitude "
      "reads '10.5202 E', a longitude suffix on a latitude, an error the p34 reprint copies "
      "exactly. The six values are 8.4897 N / 10.3315 N / 10.9935 N / 6.9627 N / 8.5729 N / "
      "10.5202 E over 9.1702 W / 13.4050 W / 10.8677 W / 10.5202 W / 12.4282 W / 8.3181 W.",
      numeric=6,
      cap="Table 2. Geographical locations for the delivery points")

table(21, 2, 17, 8, "result",
      "Besides, percentage of the medicine that will be allocated for these 6 headquarters is "
      "also calculated to facilitate further delivery.",
      "Seventeen printed rows over eight columns: a header band 'Every 4 weeks 1 2 3 4 5 6 Sum', "
      "fifteen fortnightly-to-monthly dates from 2013/12/30 to 2015/1/26, and a 'Percentage' row "
      "of 13.93% / 6.21% / 0.79% / 27.00% / 50.83% / 1.25% over 100%. The ruling is the "
      "paper's oddest: three rules at 460.1, 479.7 and 768.2 pt, the outer two 1.44 pt and the "
      "header rule 0.48 pt, but each spans only 90.0 to 176.3 pt - 86.3 pt, 20.6 per cent of the "
      "measure - while the grid's text runs out to 505.4 pt. The rules cover the date column and "
      "stop dead at the first data column, so the six headquarters columns and their Sum are "
      "ungridded and a reader following the Sum column has no rule to land on. No vertical "
      "stroke anywhere. The row of percentages is the delivery plan the rest of section 5.2 is "
      "built on, and it is right-aligned within its columns, not decimal-aligned. Width is taken "
      "from the printed text span, 415.4 pt, 99.3 per cent, not from the stub rules.",
      numeric=7,
      cap="Table 3. Doses of medicine for the 6 headquarters and their delivery percentage")

table(22, 1, 17, 5, "result",
      "From the calculated doses of medicine before, the average quantity of daily needed "
      "medicine is 106.2 unit dose per day.",
      "The country-level twin of Table 3 on the same sixteen dates: header 'Every 4 weeks "
      "Guinea Liberia Sierra Leone Sum' over fifteen body rows and a Percentage row of 18.64% / "
      "21.85% / 59.51% / 100.00%. Booktabs at 169.8, 189.4 and 477.9 pt, outer rules 1.44 pt and "
      "header rule 0.48 pt, each cut into five segments at the column gutters, no vertical "
      "stroke, no border. 415.4 pt wide, 99.3 per cent of the measure. The percentages here are "
      "printed with COMMA decimals - 18,64% against Table 3's 13.93% - so the two tables that "
      "split the same 111 unit doses between headquarters and countries do not agree on a "
      "decimal mark. Decimal alignment is therefore false even though the numbers are "
      "right-aligned by column.",
      numeric=4,
      cap="Table 4. Doses of medicine for Guinea, Liberia and Sierra Leone and their delivery percentage")

# ---------------------------------------------------------------- p23 and p24, Figures 11 and 12
FIG11 = "Figure 11. Simulation of predicted cumulative cases in Sierra Leone from Feb 4th, 2015"
FIG12 = "Figure 12. Simulation of predicted cumulative cases in Sierra Leone from Feb 4th, 2015"
FIG13 = "Figure 13. Simulation of predicted cumulative cases in Sierra Leone from Feb 4th, 2015"
TRUNC = (" The layer stops printing words at the first maths glyph, so the quote is cut there: the "
         "tail of the caption is described in the note instead of being typed from the crop.")

figure(23, 1, "line", FIG11, "Figure N.",
       cited(23, 23, ["Figure 11"], 2, "In Figure 11, five values have been set to"),
       "result",
       note="272.1 by 198.9 pt of pasted raster, 65.1 per cent of the measure. 'Cumulative number "
            "of individuals' 0 to 14000 in steps of 2000 against 'Time (day)' 0 to 500 in steps "
            "of 50. Three inks: a light solid grey forecast curve, a dense run of filled dots for "
            "the observed series up to day 255, and a vertical dashed reference line at that "
            "same day - the last day of the WHO series, drawn to show where the projection "
            "begins. No legend, so the dashed rule is unexplained inside the art. The caption "
            "continues past the lay'd cut with 'with gamma_H = 10, 15, 20, 25, 30', and the "
            "prose then reads five values off a panel that prints one curve: the five values are "
            "the parameter set of the run, not five plotted series." + TRUNC)

figure(24, 1, "line", FIG12, "Figure N.",
       cited(1, 24, ["Fig.12"], 1,
             "Results (Fig.12,13) show that these interventions will help reduce CUM to a lower "
             "plateau at a faster speed.", pattern="parenthetical"),
       "result",
       note="272.1 by 204.0 pt, same axes as Figure 11 - 0 to 16000 on y, 0 to 500 on x - but "
            "the divergence is now visible: after the observed dots stop near day 250, five thin "
            "solid forecasts fan upward from the common trace and never reconverge, the top one "
            "reaching about 15,500 by day 500. A vertical dashed rule marks day 250. The caption "
            "tail that the layer swallows reads 'with delta_H = 2, 4, 6, 8, 10 and 1/delta_H "
            "varying at the same time', which is what the five curves are; the prose says so in "
            "words on the same page. Cited from the abstract only, in the same parenthetical as "
            "Figure 13 - the two are the only pair the abstract cites together." + TRUNC)

# ---------------------------------------------------------------- p25, the four-panel Figure 13
def fig13(reg: int, alpha: str, yspan: str, extra: str) -> None:
    figure(25, reg, "line", FIG13, "Figure N.",
           cited(1, 25, ["Fig.12,13"], 1,
                 "Results (Fig.12,13) show that these interventions will help reduce CUM to a "
                 "lower plateau at a faster speed.", pattern="parenthetical"),
           "result",
           note=f"Panel {alpha} of the four-box Figure 13, 226.8 by 170.0 pt of pasted raster, "
                f"54.2 per cent of the measure. The four panels share one caption at 445.3 pt "
                f"and one layout, 2x2 with the alpha label set inside the top left of each "
                f"art ('{alpha}'), so the box a reader is in is printed inside the picture and "
                f"nowhere else. Axes: 'Time (day)' 0 to 500 in steps of 50 and a cumulative "
                f"axis {yspan}. Each panel inks the observed dash-dot run to about day 200, a "
                f"vertical dashed rule at that day, and then three or four thin forecasts that "
                f"fan apart - the fan widens as alpha grows, and only the alpha = 0.05 panel "
                f"turns upward off a x10^6 axis rather than flattening. No legend anywhere in "
                f"the group, so the four fan lines are unidentified." + extra + TRUNC)


fig13(1, "alpha = 0.05", "0 to 3 with a printed x10^6 multiplier",
      " This is the only panel on a millions axis: the other three sit at 13,000 to 14,000.")
fig13(2, "alpha = 0.1", "0 to about 13,000",
      " The top of the y axis is clipped by the art's own frame and the tick labels arrive from "
      "the layer as broken digit groups.")
fig13(3, "alpha = 0.3", "0 to about 14,000",
      " The fan here is the widest of the four after day 300, and the observed run is the "
      "longest.")
fig13(4, "alpha = 0.2", "0 to about 14,000",
      " The measured boxes are ordered left-right on the top row and right-left on the bottom "
      "row, so the reading order by region index is 0.05, 0.1, 0.3, 0.2 and the printed labels "
      "are what restore the numeric order.")

# ---------------------------------------------------------------- p27, the four-panel Figure 14 and Table 5
FIG14 = "Figure 14. The effect of"


def fig14(reg: int, panel: str, label: str, yspan: str) -> None:
    figure(27, reg, "line", FIG14, "Figure N.",
           cited(28, 27, ["Figure 14"], 2,
                 "The black line in Figure 14 represents the trend of CUM without changing"),
           "result",
           note=f"Panel {panel} of Figure 14, '{label}', 226.8 by 170.1 pt of pasted raster, "
                f"54.2 per cent of the measure, one of four boxes under a single caption at "
                f"436.8 pt. 'Time (day)' 0 to 700 in steps of 100 against a cumulative axis "
                f"{yspan} carrying a printed x10^4 multiplier. The inked content is the "
                f"observed marker run up to day 320, a vertical dashed rule at that day, and "
                f"then a fan of uncertainty bands - grey outermost, then red, blue and green - "
                f"around one heavy black central curve. The four bands are the four coloured "
                f"regions Table 5 defines, and the panel labels '1. alpha', '2. kappa', "
                f"'3. 1/gamma_H', '4. delta_H' are printed inside the top left of each art. No "
                f"legend: the colour key lives in Table 5, 190 pt below the last panel." + TRUNC)


fig14(1, "2", "2. kappa", "0 to 2.5")
fig14(2, "1", "1. alpha", "0 to 2.6")
fig14(3, "4", "4. delta_H", "0 to 2.5")
fig14(4, "3", "3. 1/gamma_H", "0 to 2.5")

table(27, 5, 5, 5, "result",
      "in different colored regions are listed in Table 5.",
      "Five printed rows over five columns: a header band with four colour names - Red, Blue, "
      "Green, Critical value - over four rows labelled 'Graph 1 alpha', 'Graph 2 kappa', "
      "'Graph 3 1/gamma_H' and 'Graph 4 delta_H'. Booktabs at 630.5, 650.0 and 722.5 pt, the "
      "outer rules 1.44 pt and the header rule 0.48 pt, each cut into five segments at the "
      "gutters, no vertical stroke, no border. 414.9 pt wide, 99.2 per cent of the measure. No "
      "unit and no caption beyond 'Value for alpha, kappa, 1/gamma_H and delta_H in different "
      "colored region'. The cells are hyphenated ranges, not numbers - 0.25-0.31, 0.31-0.33, "
      "0.33-0.4 against a critical value of 0.32 - so they are right-aligned by column and "
      "decimal_aligned is false. Printed defects: the Graph 4 row begins '0.6-0.01', a range "
      "that runs downward, and the four rows' bands overlap each other's critical values (Graph "
      "1's Green band reaches 0.4 past its critical 0.32), so the colour a point falls in is "
      "not well defined.",
      numeric=4,
      cap="Table 5. Value for")

# ---------------------------------------------------------------- p28 to p31, the sensitivity fans
figure(28, 1, "line",
       "Figure 15. Simulation of the eradicating date by varying the introduction time of medicine",
       "Figure N.", none_mention(), "result", numbers=True, labels=True,
       note="272.1 by 203.8 pt of pasted raster, 65.1 per cent of the measure. 'Time (day)' 0 to "
            "700 against a cumulative axis 0 to 2.5 on a printed x10^4 multiplier. Roughly forty "
            "thin solid curves rise through a magenta-cyan-yellow-red ramp ordered by height, "
            "over one heavy black curve with markers that carries the observed run to about day "
            "320. Instead of a legend the art prints eight inline numeric labels at the right "
            "edge inside the axes - tau = 240, 225, 210, 195, 180, 175, 160, 145 - so the "
            "parameter value of each curve is printed on the curve. The caption tail the layer "
            "swallows is 'tau'." + TRUNC)

figure(29, 1, "line",
       "Figure 16. Simulation of the eradicating day by varying the efficacy of medicine",
       "Figure N.",
       cited(29, 29, ["Figure 16"], 2,
             "The black lines in Figure 16 also represent no changing of the medicine efficacy"),
       "result", labels=True,
       note="The LEFT panel of Figure 16, 226.7 by 169.6 pt of pasted raster, 54.2 per cent, one "
            "of two boxes with one caption at 232.0 pt. 'time (day)' 0 to 700 against a "
            "cumulative axis 0 to 2.5 with a printed x10^4 multiplier. About thirty-five thin "
            "red curves and a total of some forty-four series take off from a common dash-dot "
            "reference; a dashed marker curve carries the observed run and the art annotates "
            "'Eradicating Points' inside the axes. No legend, no gridlines. Printed defect: the "
            "x10^4 multiplier prints on this panel only - the right panel's axis is a plain "
            "0 to 15,000 - so the pair look like the same quantity at two scales when they are "
            "the same quantity at one scale, and a reader who compares the two boxes reads a "
            "factor of ten that is not there." + TRUNC)

figure(29, 2, "line",
       "Figure 16. Simulation of the eradicating day by varying the efficacy of medicine",
       "Figure N.",
       cited(29, 29, ["Figure 16"], 2,
             "The black lines in Figure 16 also represent no changing of the medicine efficacy"),
       "result", labels=True,
       note="The RIGHT panel of Figure 16, same 226.7 by 169.6 pt box, cyan where the left panel "
            "is red: about thirty thin curves, 'Time (day)' 0 to 700 against a cumulative axis 0 "
            "to 15,000 in steps of 1,000 with no multiplier, and the same dash-dot reference, "
            "dashed marker curve and 'Eradicating Points' annotation. The two panels are the "
            "same family in the same layout under one caption and are booked as two rows with "
            "panel_count 1 each, not as one composite-panel: the vocabulary keeps the family of "
            "a same-family multi-panel exhibit. Colour is the only thing that separates the two "
            "parameter families and nothing on the page keys it." + TRUNC)

figure(29, 3, "line",
       "Figure 17. Impact of transmission rate on the cumulative number of individuals",
       "Figure N.",
       cited(30, 29, ["Figure 17"], 2,
             "The black dotted curve in Figure 17 represents the actual statistics."),
       "sensitivity",
       note="272.1 by 196.8 pt of pasted raster, 65.1 per cent of the measure, at the foot of p29 "
            "with its caption 8 pt under it. 'Cumulative number of individuals' 0 to 14,000 in "
            "steps of 2,000 against 'Time (day)' 0 to 300 in steps of 50. About forty thin red "
            "curves fan from the common trajectory; a black dotted curve carrying black star "
            "markers is the observed series; a light grey shaded envelope surrounds the fan. No "
            "legend, no gridlines, no printed numbers. Printed defect: the grey envelope runs "
            "past the top of the axes and is clipped at 14,000 between days 95 and 150, so for "
            "that stretch the plot shows the ceiling of its own frame rather than the model's "
            "output, and the red curves are unidentified - the caption says 'transmission rate' "
            "and prints no value on any curve.")

figure(30, 1, "line",
       "Figure 18. Impact of the incubation period to the cumulative number of individuals",
       "Figure N.",
       cited(30, 30, ["Figure 18"], 2,
             "we can see from Figure 18 that the trends of cumulative number of individuals are "
             "quite similar."),
       "sensitivity", labels=True,
       note="272.1 by 203.8 pt of pasted raster, 65.1 per cent of the measure. 'Cumulative "
            "number of individuals' 0 to 14,000 against 'Time (day)' 0 to 300. Three prominent "
            "curves - a red one that leaves the top of the frame early, a heavy black one with "
            "markers, and a blue one - plus one faint black curve, with inline labels sigma = "
            "1/5, 1/9 and 1/15 printed inside the axes. Those inline labels are the only key the "
            "figure has: there is no legend and no gridlines. The caption's 'to' is printed where "
            "'on' belongs, and the prose reads the panel as the evidence that the model is not "
            "sensitive to the incubation period - which the red curve, still climbing out of "
            "frame at day 300, does not quite show.")

FIG19 = "Figure 19. Cumulative number of individual after noises are added to"

figure(31, 1, "line", FIG19, "Figure N.", none_mention(), "sensitivity",
       note="The LEFT panel of Figure 19, 226.6 by 170.2 pt, 54.2 per cent of the measure, one "
            "of two boxes under one caption at 246.6 pt. 'Cumulative number of individuals' 0 to "
            "14,000 against 'Time (day)' 0 to 300. This panel is a hybrid and is the only "
            "reading of its kind on the paper: the axes, ticks and the black marker series are "
            "crisp vector line work while the red fit curves laid over them are a coarse pasted "
            "raster, visibly blurred against the text around it. Two red curves; no legend, no "
            "gridlines, no printed values. The caption tail the layer swallows is 'delta_H'." + TRUNC)

figure(31, 2, "line", FIG19, "Figure N.", none_mention(), "sensitivity",
       note="The RIGHT panel of Figure 19, the same 226.6 by 170.2 pt box with the same hybrid "
            "ink and four red fit curves where the left panel has two. 'Cumulative number of "
            "individuals' 0 to 14,000, 'Time (day)' 0 to 300, same black marker series. Neither "
            "panel carries a title or a key, so the only thing distinguishing the two noise "
            "levels is the count of red curves, and the caption ('after noises are added to "
            "delta_H') gives no value for either. Booked as two rows of family line, like the "
            "other same-family pairs on this paper.")

# ---------------------------------------------------------------- p33 and p34, the reprints
figure(33, 1, "map-or-plan-view", "", "none", none_mention(), "other",
       source="none", legend="inside", numbers=True, labels=True, position="above",
       note="An UNCAPPIONED reprint of the delivery-location map, 665x565 px at 158.5 to 436.8 pt "
            "by 527.9 to 764.0 pt - 278.3 by 236.1 pt, 66.5 per cent of the measure - printed in "
            "the Future Work section with no figure number, no title and no caption anywhere "
            "under it. The prose above it says only 'Their locations are presented in the "
            "following picture.' It is not the same image file as Figure 10: both are 665x565 px "
            "but they are two embedded objects, and this one carries a fresher basemap - its "
            "source line reads 'Source: WHO Ebola Response Roadmap 14 February 2015' against "
            "Figure 10's 4 February. Same design otherwise: the six-step orange district ramp "
            "with 'No cases reported', the 'Newly Infected' and 'Cases in last 21 days' keys, "
            "country names in maroon serif, six black stars on the sites the six dot colours "
            "mark. A reader who has met Figure 10 sees the same map twice with no signal that it "
            "is a repeat, and the paper's own numbering never acknowledges it.")

table(34, 1, 3, 7, "other", "The geographical coordinates for these headquarters are:",
      "An UNCAPPIONED reprint of Table 2, printed in the Future Work section under the sentence "
      "'The geographical coordinates for these headquarters are:' with no number and no caption, "
      "and it is not a fragment of the p21 grid: it is a complete second copy, same three rows, "
      "same seven columns, same six coordinate pairs including the erroneous '10.5202 E' "
      "latitude, same three rules at 115.8, 137.3 and 177.9 pt with the same seven segment "
      "breaks at the gutters and the same 440.2 pt width, 105.2 per cent of the measure. The "
      "only difference is vertical drift: the grid prints 36 pt higher on this page. The section "
      "that follows it restates Table 3's percentage row as prose ('13.93%, 6.21%, 0.79%, "
      "27.00%, 50.83% and 1.25%'), so the last two pages of the paper reprint one table and one "
      "number row from the middle of it.",
      numeric=6,
      cap="")

figure(20, 2, "map-or-plan-view",
       "Figure 10. Delivery location", "Figure N.",
       cited(1, 20, ["Fig.10"], 1,
             "we apply the weighted Fuzzy c- Means Clustering Algorithm and select 6 locations "
             "(Fig.10, Table.2)", pattern="parenthetical"),
       "result", legend="inside", numbers=True, labels=True,
       note="271.4 by 230.6 pt of pasted raster, 64.9 per cent of the measure, and the exhibit "
            "the whole delivery section rests on. Same 665x565 px WHO basemap as Figure 1 - "
            "green land, orange district ramp, six-step 'Total Cases' key with 'No cases "
            "reported', the two outlined keys for 'Newly Infected' and 'Cases in last 21 days', "
            "country names in maroon serif, 'Source: WHO, Ebola Response Roadmap 04 February "
            "2015' burned into the lower right - with the team's own overlay added: six dot "
            "colours, red, cyan, green, blue, magenta and yellow, one per headquarters set, and "
            "black star markers standing on the six chosen sites. Those star positions ARE the "
            "Table 2 coordinates: the paper never says so, and the six dots are the sets the "
            "caption of Table 3 says will 'later receive medicine and vaccines from the "
            "headquarter inside them'. One caption of two words, 'Delivery location', and no "
            "legend for the dots or the stars.")

# ---------------------------------------------------------------- exclusions
EXCLUDED.append({
    "page": 3,
    "bbox": REG[(3, 2)],
    "kind": KIND[(3, 2)],
    "reason": "background",
    "note": "five 14.1 pt bands at 692.4, 710.4, 728.4, 728.4 and 746.4 pt, x 90.0 to 505.4 pt "
            "with two of them starting at 144.7 and 227.1 pt - the shaded paragraph strips the "
            "word processor leaves behind inline equations, sitting under four lines of body "
            "text on Ebola transmission and carrying no ink of their own",
})

EXCLUDED.append({
    "page": 4,
    "bbox": REG[(4, 1)],
    "kind": KIND[(4, 1)],
    "reason": "background",
    "note": "seven 14.2 pt bands at 75.1, 75.1, 75.1, 93.1, 111.1, 111.1 and 129.1 pt spanning "
            "the full measure - the same paragraph shading as p3, here behind the first pages of "
            "prose and behind one short display line; no chart, no grid, no image",
})

EXCLUDED.append({
    "page": 11,
    "bbox": REG[(11, 1)],
    "kind": KIND[(11, 1)],
    "reason": "background",
    "note": "two 14.2 pt bands at 75.1 and 93.1 pt, x 114.0 to 462.8 pt, behind the displayed "
            "form of the SEIHCR equations at the head of p11 - the maths itself is drawn as "
            "characters and this box is the shading under it",
})

EXCLUDED.append({
    "page": 11,
    "bbox": REG[(11, 2)],
    "kind": KIND[(11, 2)],
    "reason": "background",
    "note": "two 14.3 pt bands at 511.4 and 529.4 pt, x 114.0 to 275.0 pt, behind the inline "
            "equation for the identification rate; the three short horizontal strokes at 493.3 "
            "pt just above this box are the fractions of that same equation and fall outside it",
})

EXCLUDED.append({
    "page": 12,
    "bbox": REG[(12, 1)],
    "kind": KIND[(12, 1)],
    "reason": "background",
    "note": "nine 14.1 pt bands from 319.7 to 471.8 pt spanning the measure, the shading behind "
            "equations (4.2) to (4.3); the box measures as one region because the bands touch "
            "down the page, and it holds no chart of any kind",
})

EXCLUDED.append({
    "page": 35,
    "bbox": REG[(35, 1)],
    "kind": KIND[(35, 1)],
    "reason": "not-an-exhibit",
    "note": "two 14.4 pt bands at 658.5 and 676.5 pt, x 111.0 to 505.4 pt, inside the reference "
            "list - the hanging-indent shading of two bibliography entries between [12] and "
            "[13], with the entry text above and below it",
})

EXCLUDED.append({
    "page": 36,
    "bbox": REG[(36, 1)],
    "kind": KIND[(36, 1)],
    "reason": "not-an-exhibit",
    "note": "two 14.4 pt bands at 344.9 and 363.2 pt, x 111.0 to 387.9 pt, again inside the "
            "bibliography - the indent shading of entries [19] and [20]",
})

# ---------------------------------------------------------------- payload
RULES = [
    "rows counts every printed row the region carries, header band included, and a grid split "
    "over a page turn is two rows with continued true on the second half only: the symbol grid "
    "prints 8 rows on p6 and 12 on p7, the taller Description cells pushing the p7 rows apart "
    "to 36.5 pt [table.rows]",
    "the symbol grid repeats no header on its second page and still records header_rows 1, so "
    "continued is the field that carries the break, not header_rows [table.continued]",
    "a grid whose every body row is ruled keeps the nearest closed label and states the truth "
    "in the note: the symbol grid has 0.48 pt rules under all nineteen rows, no vertical and no "
    "border, and records booktabs [table.rule_style]",
    "a caption line in the text layer is not a citation: Figures 2, 15 and 19 print their "
    "numbers only in their own captions and the prose never names them, so each records count 0 "
    "with first_page null [mention.count]",
    "a citation that lands in the abstract records lead_pages page minus 1: Figs 4, 5, 6, 7, 10, "
    "12 and 13 are named once each on p1 and print on pp14 to 29 in that order [mention.lead_pages]",
    "a citation that lands after the art records a negative lead_pages: Figure 14 prints on p27 "
    "and is named on p28, so it records -1 [mention.lead_pages]",
    "a caption the layer cannot finish is quoted only as far as its last printed word, and the "
    "maths tail is described in the note: Figures 11 to 19 and Table 5 all stop at the first "
    "private-use glyph [caption.verbatim]",
    "multi-panel exhibits of one family keep that family and are booked one row per measured "
    "box: Figures 2, 8, 13, 14, 16 and 19 hold three, two, four, four, two and two boxes, every "
    "row with panel_count 1, and none is composite-panel [geometry.panel_count]",
    "a raster overlay on crisp vector axes does not change the family: Figure 19's red fit "
    "curves are a pasted raster over vector ticks and a vector marker series, and it stays line "
    "[geometry.family]",
    "a filled area under named lines is still a line chart: Figure 7 inks a grey total-quantity "
    "area and three country curves, and Figure 8b inks a filled calculated area under an "
    "observed marker line [geometry.family]",
    "a map with a pasted terrain basemap and an overlay of dots and stars is map-or-plan-view, "
    "not photo-or-raster-image and not composite-panel: Figures 1, 10 and the p33 reprint record "
    "the same family [geometry.family]",
    "a legend printed above the axes is 'above' and one printed inside the frame is 'inside': "
    "Figure 7's four keys print above its frame and every other chart's print inside it "
    "[geometry.legend]",
    "width is measured on the printed text span and not on the ruling: Table 3's three rules "
    "cover 86.3 pt of its 415.4 pt width, and the table still records full at 99.3 per cent "
    "[table.width]",
    "a coordinate column of degrees with a hemisphere suffix is a numeric column: Table 2's six "
    "columns record numeric_cols 6 and text_cols 1 [table.numeric_cols]",
    "hyphenated ranges are not decimals: Table 5's four band columns are right-aligned by column "
    "and record decimal_aligned false [table.decimal_aligned]",
    "captions print below their figures and above their tables on this paper without exception, "
    "so every figure records position below and every table position above [caption.position]",
]

NOTE = (
    "Forty-five measured regions over twenty of thirty-six pages: 31 figure rows, 7 table rows, "
    "7 exclusions, nothing unmeasured. The paper prints nineteen numbered figures, one "
    "unnumbered symbol grid, five numbered tables, and one uncaptioned reprint each of a map and "
    "of Table 2. Figure 1 is the only exhibit whose art comes from a published source (a CDC "
    "distribution map of 4 February 2015); the rest are the team's own MATLAB output, pasted as "
    "raster in twenty-nine of the thirty-one boxes. Only Figure 3 (the compartmental schematic) "
    "and Figure 7 (the dose chart) are true vector line work.\n\n"
    "Two exhibits print twice, uncaptioned, and neither is acknowledged. p33 prints the "
    "delivery-location map again in the Future Work section, behind the sentence 'Their "
    "locations are presented in the following picture.', on a fresher WHO basemap - its source "
    "line reads 14 February 2015 where Figure 10's reads 4 February - with no figure number and "
    "no caption under it. p34 prints Table 2 again whole, same six coordinate pairs including "
    "the erroneous '10.5202 E' latitude, same seven-segment rules, 36 pt higher on the page, and "
    "the paragraph under it restates Table 3's percentage row as prose. Both are recorded as "
    "rows of their own with an empty caption rather than excluded as duplicates, because each is "
    "a complete second printing with air above and below it, not a fragment of the first; the "
    "counts they add to the census are the reason the note names them.\n\n"
    "One table has no box. Table 1 on p8 - the fitted parameter estimates, 'Parameter Guinea "
    "Sierra Leone Liberia' over R0 1.51 / 2.53 / 1.59 and N 12,000,000 / 6,100,000 / 4,092,310 "
    "- carries three rules at 598.15, 617.71 and 746.98 pt spanning 414.9 pt, 99.2 per cent of "
    "the measure, and the drawing pass still returns no region for it. The cause is not width "
    "and not the grouping gap that cost paper 69 its grids: a single cell is painted with a "
    "near-white fill, 0.976 grey, at 435.3 to 483.3 pt by 726.8 to 741.0 pt, and it sits 6.0 pt "
    "above the closing rule. At tol 8 the fill and the rule fuse into one 21.6 pt cluster, which "
    "fails RULE_HEIGHT_PT at 12 pt; the two rules left over span 19.6 pt between 598.15 and "
    "617.71 and fall under MIN_SIDE_PT at 25 pt, so the whole table disappears. At tol 2 the "
    "same page returns 90.0, 598.1, 504.9, 748.4 - the grid exactly. This is a new defect class "
    "for the lane's findings: a shade, not a rule, breaking a rule group.\n\n"
    "The caption is the weakest part of the paper. Nine captions lose their tail to the maths "
    "layer - Figures 11 to 19 stop at the first parameter symbol, so 'Figure 13. Simulation of "
    "predicted cumulative cases in Sierra Leone from Feb 4th, 2015' is all the layer holds and "
    "the four panels' alpha values live inside the art; Figure 14's caption arrives as 'The "
    "effect of' and nothing else; Table 5's as 'Value for'. Figure 2 prints one caption under "
    "the third of its three panels, 1006 pt from the first, and it is the word 'respectively' "
    "alone that maps panel to country. Figures 4, 5 and 6 are cited nowhere but the abstract, in "
    "a single parenthetical 'The model's results (Fig.4,5,6)'. No caption on the paper states a "
    "unit, a sample, or a conclusion, and Figure 13's four panels carry no key for their four "
    "fan lines.\n\n"
    "The mentions are thin exactly where the exhibits are thick. Thirty-one figure rows collect "
    "seven by-number citations that are not their own captions - Figs 4, 5, 6, 7, 10, 12 and 13 "
    "once each from the abstract, Figure 3, Figure 8, Figure 9, Figure 11, Figure 16 and Figure "
    "18 once each from the prose, Figure 14 once from the page after it, Figure 17 once from the "
    "page after it, and Table 2 and Table 5 once each from the sentence above them. Figures 2, "
    "15, 19, Table 3, Table 4 and both reprints record count 0. The severity analysis of section "
    "8 is built on four figures (15 to 19) of which two are never named in the text at all.\n\n"
    "Ruling. Every table on the paper is booktabs in the strict sense - horizontal rules only, no "
    "vertical stroke anywhere, no border - but the rules behave in three different ways. Tables "
    "2, 4 and 5 and both reprints cut each rule into one segment per column at the gutters, which "
    "is a 7-, 5-, 5- and 7-segment rule rather than a continuous one. Table 3 draws its three "
    "rules only across the date column, 86.3 pt of a 415.4 pt grid, so five of its eight columns "
    "are ungridded. The symbol grid rules every row, 0.48 pt under each, with 1.44 pt at the top, "
    "under the header and at the foot. Widths: Table 2 and its reprint 440.2 pt, 105.2 per cent "
    "of the 418.3 pt measure, overhanging both margins - the only exhibits on the paper that "
    "leave the text block on both sides; Tables 3, 4, 5 and the symbol grid 414.9 to 415.7 pt, "
    "99.2 to 99.4 per cent; and Figure 8's right panel overhangs the right margin alone by 21.4 "
    "pt.\n\n"
    "Printed defects, recorded not corrected. Figure 8's caption promises 'quantity of needed "
    "medicine per week' while the right panel's axis reads 'Unit dose of the medicine needed' "
    "and the prose calls it a daily dose; Figure 7's caption says 'per day' under an axis that "
    "says only 'Unit dose'. Table 2 and its p34 reprint both print '10.5202 E' for a latitude. "
    "Table 4 prints comma decimals, 18,64% and 21,85%, where Table 3 prints 13.93% and 6.21%, "
    "and the two tables split the same 111 unit doses. Table 5's Graph 4 row opens with "
    "'0.6-0.01', a band that runs downward, and its four bands overlap one another's critical "
    "values. Figure 8's left panel is labelled 'Time (day)' and its right 'time (day)'. Figure 6 "
    "is described by Figure 18's caption as the incubation period where the axis measures "
    "cumulative individuals, and the prose that discusses Figure 15 credits Figure 14 for its "
    "black line. The heading pass is as unusable here as on papers 68 and 69: it reads the "
    "parameter block between Figures 4 and 5 as a heading ('1 Estimation of R0' lands on p12, "
    "'2 Determination of other parameters' on p14), leaves the References page as "
    "'unnumbered-title References' and reads a wrapped bibliography line on p36 as a section of "
    "the paper, which is why p36 r1 is filed as a hanger rather than placed. "
    "Section 8's own numbering skips: the page heads read 8.1, 8.3 and nothing between."
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

out = PROXY / "pc70-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
