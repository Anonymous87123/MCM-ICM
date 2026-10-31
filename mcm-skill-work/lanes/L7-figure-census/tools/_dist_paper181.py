"""Hand census of P-E-2019-1902054-4ff1f32f (Team 1902054, 17 pages, 10 measured regions).

An economic-cost paper for problem E 2019: a value model V(A) = E(A) + I(A) built from an ecological
term and an intervention term, then three cases - Kubuqi desert greening, a Baowu steel plant, and the
Wolong panda reserve. The paper measures TEN regions over NINE pages and every one of them is a
figure, so the census is ten figure rows, no tables and nothing refused.

  p6  r1  Figure 1    line                 valuation against area, positive initial ecosystem
  p7  r1  Figure 2    line                 the mirror plate, negative initial ecosystem
  p9  r1  Figure 3    photo-or-raster-image   two satellite images of Kubuqi, 2000 against 2016
  p10 r1  Figure 4    line                 the desert case, one S-curve with two callouts
  p11 r1  Figure 5    line                 cost-benefit curve with three coordinate boxes
  p11 r2  Figure 6    bar                  stacked cost-benefit columns for 6000 km2
  p12 r1  Figure 7    photo-or-raster-image   a smokestack photograph
  p13 r1  Figure 8    line                 the steel case, one descending curve
  p14 r1  Figure 9    map-or-plan-view     panda distribution before and after livestock
  p15 r1  Figure 10   line                 the reserve case, one sigmoid

Here region order IS reading order, unlike the two papers before this one: p11's Figure 5 sits in region
1 above its Figure 6 in region 2.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-E-2019-1902054-4ff1f32f"
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
LIG = "ﬁ"  # "benefit" and "certificate" are set with a real fi ligature in this document


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


S_6 = [head(6, "6 Categorize types of land use project")]
S_7 = [head(9, "7 Case studies")]
S_71 = [printed(9, "7.1 case 1: Desert greening in Kubuqi desert, China")]
S_72 = [printed(12, "7.2 case 2: China Baowu Steel Group")]
S_73 = [printed(14, "7.3 case 3: Wolong National Nature Reserve in Sichuan, China")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_KNOWN |= schema.printed_lines(PID)
for _group in (S_6, S_7, S_71, S_72, S_73):
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


CAP1 = caption("Figure 1: Positive initial system (+E(A))")
CAP2 = caption("Figure 2: Negative initial system (-E(A))")
CAP3 = caption("Figure 3: Comparison of kubuqi desert landform between year 2000 and 2016 (yu,")
CAP4 = caption("Figure 4: Applying the model to the desert green case")
CAP5 = caption(f"Figure 5: Cost bene{LIG}t plot of Kubuqi greening project")
CAP6 = caption("Figure 6: Cost-beneﬁt analysis of desert greening of 6000 km2 in Kubuqi, China")
CAP7 = caption("Figure 7: Air pollution in Shanghui")
CAP8 = caption("Figure 8: Applying the model to the steel production case")
CAP9 = caption("Figure 9: Predictions of giant panda distribution in Wolong Nature Reserve before")
CAP10 = caption("Figure 10: Applying the model to the panda nature reserve case")

# ============================================================ 6: the two valuation plates
figure(6, 1, "line", CAP1, "text-layer", uncited(), S_6,
       "The model's general plate: value V against project area A, with an in-art title reading "
       "'Valuation of land versus area of the land, with positive initial ecosystem'. Three strokes "
       "under an upper-left legend keyed K>0, K=0 and K<0, a dashed rule at V = 0, and three callout "
       "boxes along the right edge printing '+E(A) +I(A) : improvement', '+E(A) +0 : do no harm' and "
       "'+E(A) -I(A) : pollution'. The abscissa runs 0 to 30 in steps of 5 and the ordinate -30 to 50 in "
       "steps of 10, and NEITHER AXIS CARRIES A UNIT: what the 30 areas are - km2, hectares, projects - "
       "is given nowhere on the plate or in the section, and the reader learns from the case sections "
       "three pages later that the eventual scale is km2 in the thousands. TWO KEYS COMPETE FOR THE "
       "SAME THREE STROKES: the legend assigns K signs to the strokes while the callout boxes assign "
       "I(A) signs to the same three, and nothing says whether the K>0 curve is the improvement curve or "
       "a different curve that happens to rise, so a reader who follows the legend and a reader who "
       "follows the boxes will read the same stroke as two different cases. The K<0 crossing of the zero "
       "rule near A = 9 IS UNMARKED, and it is the number the paper's whole argument turns on - the area "
       "at which a polluting project stops destroying value - while the two callouts that do get "
       "coordinates are placed on the other two curves. NO SENTENCE IN THE BODY NAMES THIS FIGURE: the "
       "section prints the caption and moves straight into the negative case.",
       geometry("line", panels=1, legend="inside", labels=True, numbers=True), "1", section_kind="model")

figure(7, 1, "line", CAP2, "text-layer", uncited(), S_6,
       "The mirror plate, titled 'Valuation of land versus area of the land, with negative initial "
       "ecosystem'. THE PAIR IS NOT DRAWN ON ONE SCALE: this ordinate runs -50 to 50 while Figure 1's "
       "runs -30 to 50, so the same height on the page is a different value on the two plates and the "
       "pair cannot be laid one over the other although the section presents them as the two halves of "
       "one statement. The callout vocabulary also flips: Figure 1's boxes read '+E(A) +I(A)', "
       "'+E(A) +0', '+E(A) -I(A)' and this plate's read '-V(A) +I(A) : remedy', '-V(A) +0 : do no good', "
       "'-V(A) -I(A) : detrimental', so the SAME ecological term is written +E(A) on one plate and -V(A) "
       "on the next with no note that the sign convention changed. Where Figure 1's three strokes rise, "
       "these fall, which is the intended mirror; the zero crossings are again unmarked and again the "
       "quantity the section discusses. Abscissa 0 to 30, no unit on either axis, dashed zero rule, "
       "legend upper-left. NOT NAMED BY ANY SENTENCE, exactly like Figure 1.",
       geometry("line", panels=1, legend="inside", labels=True, numbers=True), "2", section_kind="model",
       order=1)

# ============================================================ 7: the three cases
figure(9, 1, "photo-or-raster-image", CAP3, "text-layer", uncited(), S_7,
       "Two satellite frames pasted side by side, each carrying its own sub-caption underneath - "
       "'(a): Satellite image of Kubuqi desert before greening in 2000' and '(b): Satellite image of "
       "Kubuqi desert after greening in 2016' - so the plate's argument is carried by type, not by any "
       "mark on the image. NO SCALE BAR, NO NORTH ARROW, NO SOURCE LINE, NO DATE STAMP AND NO LABELLED "
       "COMMON LANDMARK: the two frames are shown at different apparent extents and a reader has no way "
       "to tell how much of the change is greening and how much is the two scenes covering different "
       "grounds. Green and beige rasters with no key, no percentage of cover, and no boundary drawn "
       "around the 6000 km2 the rest of the paper computes against. The caption is the paper's own but "
       "truncates mid-parenthesis - 'between year 2000 and 2016 (yu,' - and its citation, 'yu, 2017', is "
       "the only attribution on the plate. The mention the extractor finds on p9 is the caption itself "
       "glued to the '(Campbell and BaoTou, 2017)' reference that precedes it, so NO PROSE SENTENCE NAMES "
       "THIS FIGURE either.",
       geometry("photo-or-raster-image", panels=2, layout="1x2", labels=True), "3", section_kind="result")

figure(10, 1, "line", CAP4, "text-layer",
       cited(10, 10, ["Figure 4"], 1,
             lead="From Figure 4 above we can see that the project turns the value of the land to "
                  "neutral (V = 0) when the"),
       S_71,
       "One red S-curve on a light grid, the desert case's value against implemented area. ONLY THREE "
       "NUMBERS ARE PRINTED: '0' at the origin and '5000' twice on the abscissa, with no tick ladder "
       "between them and no ordinal for the vertical axis at all, so the curve's start value and its "
       "plateau are readable only by counting grid lines. NO AXIS TITLES, NO UNIT: the plate never says "
       "the abscissa is km2 although the sentence that cites it does ('2091 km2', '4500 km2'). Two "
       "callouts carry the section's two numbers - 'Value turns positive at 2091' and 'Value reaches "
       "maximum at 4500' - both printed WITHOUT their unit on the plate, so the identical digits mean "
       "different things in the figure and in the prose. The callouts agree with the prose exactly, which "
       "is the one place the paper's arithmetic is checkable end to end. The equation the plate "
       "illustrates is printed above it and is scrambled in the text layer ('3000 V (A) = E(A) + I(A) = "
       "5000 − 1 + 3000e−0.001A'), its fraction flattened into a single line. Cited by the sentence that "
       "opens the page.",
       geometry("line", panels=1, legend="none", labels=True, numbers=True), "4", section_kind="result")

figure(11, 1, "line", CAP5, "text-layer",
       cited(11, 11, ["Figure 5"], 1,
             lead="From Figure 5, we can see that the project is losing money before the area of project "
                  "expands to 4285 k"),
       S_71,
       "The cost-benefit curve for the greening project: abscissa 0 to 14000 in steps of 2000, ordinate "
       "-2000 to 4000, one smooth stroke that rises from below zero, peaks and slides back to zero. THE "
       "PLATE CARRIES THREE SOFTWARE CALLOUT BOXES WITH FULL SOLVER PRECISION - (4284.776, 0), "
       "(5980.428, 1771.08) and (12399.999, 0) - which are the coordinates of a numeric root search "
       "handed straight to the typesetter: the two zeros print to three decimals and the maximum to two, "
       "the first zero sits one ten-thousandth away from a round 4285, and 12399.999 is 0.001 short of "
       "14000's neighbour. That is a solver artefact masquerading as measurement, in a paper whose "
       "underlying model is analytic. THE PROSE ROUNDS THE SAME NUMBERS AND CALLS THEM A RESULT: it says "
       "the project loses money 'before the area of project expands to 4285 km2' and reaches 'the maximum "
       "gains at 5980 km2', matching the first two boxes, but it NEVER MENTIONS THE SECOND ZERO CROSSING "
       "AT 12400 - the point where the project's value returns to nothing, i.e. the upper limit of "
       "viable area, and the one number on the plate that constrains the conclusion. The minimum near "
       "(2400, -2000) is unlabelled. No axis title, no unit on either axis, no legend, grid only.",
       geometry("line", panels=1, legend="none", labels=True, numbers=True), "5", section_kind="result")

figure(11, 2, "bar", CAP6, "text-layer", uncited(), S_71,
       "A stacked column chart with an in-art title set in the plot - 'Cost-benefit analysis of desert "
       "greening of 6000 km^2 in Kubuqi, China', the exponent written as a caret because the artwork was "
       "made outside the typesetting system. Four columns' worth of components from a four-entry legend "
       "printed ABOVE the plot - net change (green), benefit (yellow), cost (red), ecological value "
       "(blue) - and THE KEY MIXES A NET WITH ITS COMPONENTS, so one of the four swatches is the sum of "
       "the others and the legend implies four independent quantities. Ordinate -4000 to 6000 in steps of "
       "2000; NO NUMBER IS PRINTED ON ANY BAR, so every statement about this plate has to be read off the "
       "grid. Read off the grid the picture does not close: the After column's parts total roughly 2700 "
       "while its Net bar stands near 2100, and the Before column totals roughly -600 against a Net bar "
       "of about -600, so the stack does not compose into the bar drawn beneath its own key. The caption "
       "repeats the in-art title except that it writes 'Cost-beneﬁt' with a hyphen where the artwork "
       "does not. THE PROSE REACHES THIS PLATE ONLY BY DEIXIS - 'we can use the following graph' - and no "
       "sentence ever cites 'Figure 6'.",
       geometry("bar", panels=1, legend="above", labels=False, numbers=True), "6", section_kind="result",
       order=2)

figure(12, 1, "photo-or-raster-image", CAP7, "text-layer", uncited(), S_72,
       "A photograph of a smoking industrial stack with transmission pylons and a chimney plume against "
       "a flat sky, captioned 'Figure 7: Air pollution in Shanghui'. The city in the caption is MISSPELT "
       "- the paper discusses Baowu Steel, whose plant the section is about, and no Chinese city is "
       "written 'Shanghui'. THE PLATE CARRIES NO DATA OF ANY KIND: no measurement, no concentration, no "
       "date, no source, no location stamp, no scale, nothing that ties the photograph to the steel case "
       "whose section it sits in. It illustrates a claim ('the plant pollutes') rather than reporting "
       "anything the model uses, and no sentence in the section names it, so the page's prose never "
       "points at it. Included in the census as a figure because it is measured as a region and carries "
       "a figure number, not because it is evidence.",
       geometry("photo-or-raster-image", panels=1), "7", section_kind="result")

figure(13, 1, "line", CAP8, "text-layer",
       cited(13, 13, ["Figure 8"], 1,
             lead="As shown in Figure 8, the total value of this project decreases with increasing "
                  "land-use area."),
       S_72,
       "One descending red logistic curve on a grid, the steel case's total value against land-use area. "
       "THE PLATE IS ALMOST BARE: '0' and '5000' on the ordinate, '0', '5000', '10000' and '15000' on "
       "the abscissa, no axis titles, no unit, no legend, no callout, no annotation of any kind - no "
       "asymptote marked, no crossing marked, nothing printed inside the frame. Both the curve's start "
       "value (about 5000 on the other plate's scale) and its asymptote must be read off the grid. The "
       "citing sentence is a one-clause summary of the shape ('decreases with increasing land-use "
       "area') and names no value, so nothing on the plate is ever quoted in the text. The equation "
       "above it, V(A) = E(A) + I(A) = 5000 - 3000/(1 + 3000e^-0.001A), is the same form as the desert "
       "case with the terms' signs flipped, which the plate does not indicate.",
       geometry("line", panels=1, legend="none", labels=False, numbers=True), "8", section_kind="result")

figure(14, 1, "map-or-plan-view", CAP9, "text-layer",
       cited(14, 14, ["Figure 3"], 1,
             lead="conducted in 2017, May(Figure 3), the density of giant panda distribution undergoes a "
                  "signiﬁcant"),
       S_73,
       "Two raster heatmap panels side by side, headed 'Before Livestock' and 'After Livestock', a "
       "projected-metre coordinate frame and black open-circle point symbols laid over pale pink to dark "
       "green cells. THE TWO PANELS SHARE THE SAME EXTENT - x ticks 330000, 332000, 334000 and y ticks "
       "3435000, 3437000, 3439000 on both - so the pair is genuinely comparable, which is more than most "
       "plates in this census manage. What the comparison means is drawn badly: THE COLOUR RAMPS ARE "
       "DUPLICATED RATHER THAN SHARED, one 0-to-1 bar inside each panel, and NEITHER BAR IS NAMED - the "
       "reader is not told whether the ramp is a probability of presence, a habitat index or a density, "
       "nor what 0 and 1 mean; the near-zero cells are pale pink and are barely distinguishable from the "
       "white page, so the low end of the quantity is effectively invisible; no axis carries a title or a "
       "CRS, so the numbers are plainly metres but a reader cannot say of what projection; and there is "
       "no scale bar and no north arrow on a map exhibit. The POINT LAYERS ARE UNLABELLED: no key says "
       "whether a circle is a panda record, a camera trap or a survey site, no count accompanies either "
       "panel, yet the left panel visibly carries more circles through the central corridor than the "
       "right - the plate's whole finding - and the figure does not annotate it. The green linear feature "
       "is likewise unkeyed. CITED BY THE WRONG NUMBER: the only mention near this plate reads "
       "'May(Figure 3)', which sends a reader to the two Kubuqi satellite frames on p9; the caption is "
       "the paper's own and truncates at 'before' - the words 'and after livestock application (Liu, "
       "2017)' continue in a line the extractor reads as the next caption.",
       geometry("map-or-plan-view", panels=2, layout="1x2", legend="inside", colorbar=True,
                labels=True, numbers=True), "9", section_kind="result")

figure(15, 1, "line", CAP10, "text-layer", uncited(), S_73,
       "One green sigmoid on a light grid, the reserve case's value against area, drawn in the same "
       "unadorned house style as Figure 8: ordinate ticks 4000 and 2000 only, abscissa 0, 2000, 4000 and "
       "6000, the axes crossing at the origin rather than at the frame edge, and NOTHING ELSE - no axis "
       "titles, no unit, no legend (there is one series but it is unnamed on the plate), no callout, no "
       "data markers, no annotation of the plateau or of where value turns positive. The curve starts "
       "near a quarter of the frame height and flattens around 2500, both unlabelled, so the two numbers "
       "the case turns on exist only in the prose's equation V(A) = 410 + 2000/(1 + 2000e^-1.A). NOTHING "
       "IN THE ART NAMES THE PANDA RESERVE, LIVESTOCK, PANDAS OR ANY UNIT: the plate is indistinguishable "
       "from Figure 8 at a glance except for the curve's direction, and the caption 'Applying the model "
       "to the panda nature reserve case' is the only thing that identifies it. Reached only by the "
       "caption's own tail - 'which depicts a positive appropriate value of the true economic cost of "
       "Wolong Nature Reserve' - with no numbered citation anywhere in the section.",
       geometry("line", panels=1, legend="none", labels=False, numbers=True), "10", section_kind="result")

RULES = [
    "Measure first, then read the pixels: ten measured regions over nine of seventeen pages resolve into "
    "ten figure rows, no tables and no exclusions, because every region this paper measures is an "
    "exhibit [place.doc_order].",
    "Two plates presented as one statement are drawn on two scales: Figure 1's ordinate runs -30 to 50 "
    "and Figure 2's runs -50 to 50, while the ecological term is written '+E(A)' in the first plate's "
    "callouts and '-V(A)' in the second's [geometry.family].",
    "Six of ten rows are named by no sentence: Figures 1, 2, 3, 6, 7 and 10 are reached only through "
    "their captions, and Figure 6 by the deictic 'we can use the following graph' [mention.count].",
    "A figure can be cited under the wrong number inside its own section: p14 reads the panda "
    "distribution map as 'May(Figure 3)', which is the Kubuqi satellite pair three pages earlier "
    "[mention.lead_sentence].",
    "Software output can be typeset as a result: Figure 5 prints three callout boxes reading (4284.776, "
    "0), (5980.428, 1771.08) and (12399.999, 0), i.e. a numeric root search's coordinates to three "
    "decimals, while the prose beside it rounds them to 4285 and 5980 and never mentions the second zero "
    "crossing at 12400 [caption.verbatim].",
    "No axis anywhere in the paper carries a unit: the two valuation plates have no unit on either axis, "
    "Figure 4 prints '2091' and '4500' without the km2 its citing sentence supplies, and Figures 5, 8 and "
    "10 print tick numbers only [geometry.legend].",
    "A stacked plot can fail to compose: Figure 6's four-entry legend mixes a net change with its own "
    "components, no bar carries a number, and read off the grid the After column's parts total about "
    "2700 against a Net bar of about 2100 [geometry.family].",
    "A map can be drawn without the apparatus of a map: Figure 9 carries no axis titles, no stated CRS, "
    "no scale bar, no north arrow, no source, two duplicated unnamed 0-to-1 colour ramps and unlabelled "
    "point layers [geometry.legend].",
    "A photograph can stand where evidence is expected: Figure 7 is a smokestack photograph with no "
    "data, date, source or location, captioned with a misspelt city name and named by no sentence "
    "[caption.verbatim].",
    "Region order is reading order here, unlike the preceding papers: on p11 the Figure 5 curve occupies "
    "region 1 above its Figure 6 columns in region 2 [place.page_order].",
]

NOTE = """\
Paper 181, Team 1902054: the economic cost of land-use projects for problem E 2019. A value model that
adds an ecological term to an intervention term, V(A) = E(A) + I(A), then three worked cases - Kubuqi
desert greening, a Baowu steel plant and the Wolong panda reserve - with a discussion that recommends
reusing degraded land and protecting natural landform. Seventeen pages, ten measured regions over nine
of them, resolving into TEN FIGURE ROWS, no tables, no exclusions and nothing unaccounted.

THE CENSUS IS SMALL AND MOSTLY UNDRESSED. Six of the ten plates are line charts, and the paper draws all
six in the same bare style: grid, strokes, tick numbers, and nothing else. Figures 8 and 10 carry no axis
title, no unit, no legend and no annotation at all, so their curves are identified only by their
captions. Figures 4 and 5 print the numbers the case sections quote but strip their units. The two
valuation plates at the front carry in-art titles and callout boxes, and thereby expose a worse problem:
they are the paper's model drawn twice, and the second drawing changes the sign convention without
saying so - '+E(A)' on Figure 1's boxes becomes '-V(A)' on Figure 2's - and changes the ordinate from
-30-to-50 to -50-to-50, so the two halves of one statement cannot be laid over each other.

THE ARITHMETIC IS THE PAPER'S STRONGEST FEATURE AND ITS LEAST EXAMINED. Figure 4's two callouts, "Value
turns positive at 2091" and "Value reaches maximum at 4500", reproduce the citing sentence's 2091 km2 and
4500 km2 exactly. Figure 5's boxes reproduce the prose's 4285 and 5980. That agreement is real, and it
is also the only check the paper ever performs: the same Figure 5 boxes print a third coordinate,
12399.999, which is the area at which the project's value returns to zero - the upper bound of viability
- and the prose never mentions it. No table exists anywhere in the paper, so nothing else in it can be
checked at all: the coefficients behind the three cases are asserted in prose with no grid, no
sensitivity, and no calibration shown.

THE THREE NON-CHARTS. Figure 3 is the paper's only real evidence - two satellite frames of Kubuqi in
2000 and 2016 - and it is pasted, with sub-captions underneath and no scale bar, no north arrow, no
source and no common landmark, so the reader cannot separate greening from two scenes covering different
ground. Figure 7 is a photograph of a smoking stack captioned "Air pollution in Shanghui", a misspelling
in a section about Baowu Steel, carrying no data, no date, no location and no source, named by no
sentence. Figure 9 is the paper's one map: two projected-metre heatmap panels headed "Before Livestock"
and "After Livestock" over the same extent, which makes the pair genuinely comparable, undermined by two
duplicated unnamed 0-to-1 colour ramps, invisible near-zero cells, unlabelled point layers, no CRS, no
scale bar and no north arrow. Its own finding - fewer panda points in the central corridor after
livestock - is visible in the pixels and annotated nowhere.

CITATION IS CASUAL THROUGHOUT. Only four of the ten plates are named by a sentence, and one of those
four is wrong: p14 sends the reader to "Figure 3" while discussing the panda map that sits on the same
page as Figure 9. Figures 1 and 2 - the model itself - are printed with no prose reference at all, and
Figure 6 is reached by "we can use the following graph". Figure 10 is reached by its own caption's tail.

Families: line 6 (Figures 1, 2, 4, 5, 8, 10), photo-or-raster-image 2 (Figures 3, 7),
bar 1 (Figure 6), map-or-plan-view 1 (Figure 9).
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

out = PROXY / "pc181-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
