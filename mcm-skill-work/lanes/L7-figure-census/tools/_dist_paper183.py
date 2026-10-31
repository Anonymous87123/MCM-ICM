"""Hand census of P-E-2019-1903455-a52f7980 (Team 1903455, 25 pages, 47 measured regions).

An ecosystem-services valuation paper for problem E 2019: eleven indicators weighted by entropy weight
and coefficient of variation, a hierarchical clustering of the resulting index into weak / moderate /
strong, a Gaussian-named logistic fit of that index against original cost, an SVM forecast of the
benefit-cost ratio to 2035, a sustainable-development factor that rescales it, and a sensitivity study
of one parameter. Twenty-two content regions resolve into FIFTEEN FIGURE ROWS and SEVEN TABLE ROWS;
the remaining twenty-five regions are one advertiser's banner repeated on every page and are refused.

  p4     r1  Figure 1      flowchart-or-schematic   the ESVM pipeline, boxes and one feedback branch
  p5     r1  Figure 2      flowchart-or-schematic   four service clusters around a globe icon
  p9     r1  Table 2       table-grid               five columns, eleven weighted indicators
  p10    r1  Figure 3      bar                      five gradient bars with per-row cut points
  p10    r2  Table 3       table-grid               four projects, size and intensity
  p11    r1  Figure 4      bar                      four bars plus a rank line on a second axis
  p12    r1  Figure 5      scatter                  index against cost with a sigmoid fit
  p13    r1  Figure 6(a)   scatter                  ratio by year, ordinate truncated at 2
  p13    r2  Figure 6(b)   scatter                  ratio by year, ordinate from 0
  p16    r1  Figure 7(a)   line                     fit with 95% bounds to 2034, parabola
  p16    r2  Figure 7(b)   line                     fit with bounds, monotone rise
  p16    r3  Figure 8      line                     four curves, two circles, one shaded region
  p17    r1  Table 4       table-grid               BCR at six years, annotation rows inside
  p18    r1  Figure 9      other                    four 3-D pies, sustainable against not
  p18    r2  Figure 10     other                    six pasted icons around a centre disc
  p19    r1  Figure 11     line                     four projects under sustainable measures
  p19    r2  Table 5       table-grid               four exponentials in one equation column
  p20    r1  Figure 12     line                     sensitivity, legend carries Table 5's amplitudes
  p21    r1  Figure 13     line                     one parameter swept over four values
  p25    r1  Appendix 1    table-grid               project PB, two series, six years
  p25    r2  Appendix 2    table-grid               project PC, two series, six years
  p25    r3  Appendix 3    table-grid               project PD, two series, six years

Table 1 (Notations) is LIVE TEXT at the foot of p4 and is not a measured region, so it is not in this
census. The banner 关注数学模型 2 MATHmodels 获取更多资讯 is a 678-path vector block at y=767-839 of
all twenty-five pages - twenty-five measured regions of page furniture, refused one by one rather than
collapsed, because the layout pass measured them.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-E-2019-1903455-a52f7980"
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


S_12 = [head(3, "1.2 Our work")]
S_41 = [head(5, "4.1 Ecological Services System(ESS)")]
S_412 = [head(7, "4.1.2 Weight of indicators")]
S_421 = [head(9, "4.2.1 Hierarchical clustering")]
S_422 = [head(10, "4.2.2 The result of intensity evaluation")]
S_511 = [head(11, "5.1.1 Cost analysis")]
S_513 = [head(13, "5.1.3 The ratio of benefit-cost analysis")]
S_52 = [head(14, "5.2 Prediction of Benefit-cost radio with SVM regression method")]
S_53 = [head(16, "5.3 Result analysis")]
S_61 = [head(17, "6.1 Analysis of ecosystem services measures")]
S_62 = [head(18, "6.2 Influence of Sustainability on benefit-cost ratio")]
S_7 = [head(20, "7 Sensitivity Analysis")]
S_A1 = [printed(25, "Appendix 1: ESVM result of project PB")]
S_A2 = [printed(25, "Appendix 2: ESVM result of project PC")]
S_A3 = [printed(25, "Appendix 3: ESVM result of project PD")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_KNOWN |= schema.printed_lines(PID)
for _group in (S_12, S_41, S_412, S_421, S_422, S_511, S_513, S_52, S_53, S_61, S_62, S_7,
               S_A1, S_A2, S_A3):
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


CAP1 = caption("Figure.1 Framework of ESVM")
CAP2 = caption("Figure.2 Ecological Services System.")
CAPT2 = caption("Table 2 Weight values of the indicators", kind="Table", position="above")
CAP3 = caption("Figure.3 Classification standards of varying ecosystem service index, which is "
               "classified as weak, moderate and strong.")
CAPT3 = caption("Table 3 Description of practical project of varying sizes", kind="Table",
                position="above")
CAP4 = caption("Figure.4 Comparison of ESI original ranking and intensity valuation indicators.")
CAP5 = caption("Figure.5 The relationship curve between original costs and ESI .")
CAP6 = ("Figure.6 The practical value (1995~2019) of benefit. (a) scatter plot of benefit-cost "
        "rate over time not taking into account the cost of ecosystem services; (b) scatter plot of "
        "benefit- cost rate over time taking into account the cost of ecosystem services.")
CAP6A = caption(CAP6)
CAP6B = caption(CAP6)
CAP7 = ("Figure.7 The practical value (1995~2019) and predicted value(2019~2035) of benefit-cost "
        "rate of project PA. The blue line is made by the method of support vector machine "
        "regression, and the red dotted line is a fitting curve with a confidence interval of "
        "0.95.(a) fitting curve of available benefit data over time; (b) fitting curve of benefit "
        "data over time taking into account the cost of ecosystem services.")
CAP7A = caption(CAP7)
CAP7B = caption(CAP7)
CAP8 = caption('Figure.8 The practical value (1995-2019) and predicted value of benefit-cost ratio of ܱᇿඔ࿐ଆ\u0f98 project PA(2019-2035).')

CAPT4 = caption("Table 4 BCR of the project PA according to Figure.8", kind="Table",
                position="above")
CAP9 = caption("Figure.9 Statistical results of four projects (a)project PA; (b)project PB; "
               "(c) project PC; (d) project PD")
CAP10 = caption("Figure.10 The schematic diagram of the six sustainable development indicators")
CAP11 = caption("Figure.11 Benefit-cost ratio curve of four projects which influenced by "
                "sustainable development measures only")
CAPT5 = caption("Table 5 Result of fitting according to Figure.11", kind="Table", position="above")
CAP12 = caption("Figure.12 The curve of benefit-cost ratio over time of four project.")
CAP13 = caption('Figure.13 The curve of benefit-cost ratio over time with different \uf071 (project PA).')

CAPA1 = caption("Appendix 1: ESVM result of project PB", kind="Table", position="above")
CAPA2 = caption("Appendix 2: ESVM result of project PC", kind="Table", position="above")
CAPA3 = caption("Appendix 3: ESVM result of project PD", kind="Table", position="above")

BOOKTABS = {"rule_style": "booktabs", "zebra": False, "diagonal_header": False,
            "units_in_header": False, "decimal_aligned": False, "orientation": "portrait",
            "note_sentence": ""}
BOXED = dict(BOOKTABS, rule_style="boxed")
BOXED_DEC = dict(BOXED, decimal_aligned=True)
ANNEX = dict(BOXED, width="full")

# ============================================================ 1.2: the framework
figure(4, 1, "flowchart-or-schematic", CAP1, "text-layer", uncited(), S_12,
       "A left-to-right directed pipeline in seven ranks, box fills keyed to stage but never keyed "
       "anywhere on the plate: an 'Ecosystem services system' block over eleven indicator boxes "
       "(provisioning in yellow - Raw material production, Water supply, Food production, "
       "Performance & art, Pest control; regulating in green - Water regulation, Solid regulation, "
       "Gas regulation, Recreation & tourism, Soil conservation, Biodiversity protection), then an "
       "arrow carrying two stacked labels 'EWM' and 'CVM' to a blue 'Ecosystem service index' box, an "
       "arrow carrying 'SVM regression predict' and 'Fitting' to a dark-green ellipse 'Ecosystem "
       "services evaluation model', a red arrow down to 'True cost-benefit analysis' and on to "
       "'Advice on project planning and management'. Two side branches sit off the main line: a blue "
       "'Index rationality analysis' box descends through an 'HC' edge label into the same index box, "
       "and the three regulation boxes feed, through a plain square bracket with NO ARROWHEAD, into a "
       "green 'Sustainable development factor' which then drives a horizontal red arrow into 'True "
       "cost-benefit analysis'. The dashed container at the right lists the four practical projects "
       "the rest of the paper turns on: A private enterprise relocation, B factory construction, C "
       "national pipeline engineering, D house construction. DEFECTS: the horizontal arrow from the "
       "sustainable development factor lands on the vertical shaft of the model arrow rather than on "
       "a box, so its target is not determinate; the bracket from the regulation boxes carries no "
       "arrowhead, so the direction of that influence is decided nowhere; two independent methods sit "
       "on one arrow twice (EWM and CVM, then SVM regression predict and Fitting) with nothing to say "
       "whether they are alternatives or a sequence; 'HC' is defined nowhere in the paper, though the "
       "body's 4.2.1 is where clustering lives; and 'Solid regulation' is printed for what the body "
       "elsewhere treats as a soil service. The plate carries no value, no number and no figure number "
       "inside the art. NO SENTENCE NAMES IT: the plate is reached only through the page's deictic "
       "'The whole modeling process can be shown as follows:'.",
       geometry("flowchart-or-schematic", labels=True), "1", section_kind="model")

# ============================================================ 4.1: the four service classes
figure(5, 1, "flowchart-or-schematic", CAP2, "text-layer", uncited(), S_41,
       "A concept diagram: a central globe-in-palm icon with four curved arrows out to four "
       "clusters of labelled ellipses - Provisioning (Water supply, Food production, Raw material "
       "production), Regulating (Gas regulation, Solid regulation, Water regulation), Cultural "
       "(Recreation & tourism, Performance & art) and Biotope (Soil conservation, Pest control, "
       "Biodiversity protection) - each cluster ending in its class name, with a stray verb fragment "
       "'Provide' beside a clip-art worker and five unlabelled clip-art icons (ripples, a warning "
       "triangle, a bottle with a plant, a pillared building, a sunrise over a field) scattered for "
       "decoration. THE FOURTH CLASS IS NOT THE ONE THE TEXT PROMISES: the paragraph below cites the "
       "Millennium Ecosystem Assessment's four classes, whose fourth is supporting services, while "
       "the plate prints 'Biotope services' - and the paper then carries that word into every later "
       "exhibit and into the index formula as BSI, so the rename propagates through the whole model. "
       "The four ellipse fills (green, blue, yellow, peach) are never keyed, so the classes are "
       "recoverable only from spatial grouping; arrowheads are mixed in convention, some pointing "
       "into a noun label and some out of it, and two of the provisioning arrows cross. Its caption "
       "fragment sits at the bottom edge of the region, below the art. NO SENTENCE NAMES IT: the "
       "caption line 'Figure.2 Ecological Services System.' is the only place the number appears.",
       geometry("flowchart-or-schematic", labels=True), "2", section_kind="model")

# ============================================================ 4.1.2: the weight grid
table(9, 1, S_412,
      "Five columns in a three-tier indicator hierarchy - Indicators(I) | Indicators(II) | Weights | "
      "Indicators(III) | Weights - over eleven weighted leaves, in a closed box with vertical rules "
      "between all five columns, rules between every row, and cell shading (blue for the band "
      "weights, yellow for the leaf weights) instead of a column label. THE TWO 'Weights' COLUMNS "
      "CARRY THE SAME NAME AND DIFFERENT DENOMINATORS, and the shading is the only thing that says "
      "so. FOUR OF THE FOUR BAND TOTALS FAIL THEIR OWN SUB-ROWS: Provisioning 0.2591 against "
      "0.0705+0.1038+0.1063 = 0.2806, Regulating 0.2647 against 0.1157+0.0743+0.1089 = 0.2989, "
      "Biotope 0.1900 against 0.1189+0.0348+0.0438 = 0.1975, Cultural 0.2862 against "
      "0.1293+0.0937 = 0.2230. The failure is not rounding: the eleven leaf weights sum to exactly "
      "1.0000 and the four band weights sum to exactly 1.0000, so the table prints two mutually "
      "inconsistent normalisations side by side and the ESI formula that follows uses neither in a "
      "way a reader can check - W1 to W4 are multiplied by PSI to CSI, and no page says whether W1 is "
      "0.2591 over the provisioning leaves or the provisioning leaves' own sum. The prose does at "
      "least describe the printed numbers ('the weight of recreation & tourism 0.1293 is the "
      "largest, cultural services 0.2862 ranks first, regulating second, provisioning third and "
      "biotope last'), so the census can check prose against grid and the two agree - it is the "
      "arithmetic between the grid's own columns that fails. 'Intensity' is merged down all eleven "
      "rows as an unexplained third tier, the three 'Indicators' levels are numbered with Roman "
      "numerals and no legend, and 'Solid regulation' appears again. No unit is printed anywhere; "
      "every value is dimensionless. NO SENTENCE NAMES IT: the two sentences that reach it write the "
      "pointer in lower case ('As can be seen from table 2 below' on p9) or off-hand ('Since the "
      "specific value of those indicators have been given in Table 2').",
      dict(rows=12, cols=5, header_rows=1, merged_cells=True, numeric_cols=2, text_cols=3,
           width="full", continued=False, **BOXED_DEC),
      CAPT2, "text-layer",
      cited(9, 9, ["Table 2", "table 2"], 2,
            lead="As can be seen from table 2 below, for the 11 evaluation indicators, the weight "
                 "difference between them is not big"),
      section_kind="model")

# ============================================================ 4.2.1: the classification bars
figure(10, 1, "bar", CAP3, "text-layer",
       cited(10, 10, ["Figure.3"], 1,
             lead="As shown in Figure.3, the classification standards of the four combined indicators "
                  "and the comprehensive metric vary a little."),
       S_421,
       "Five full-width horizontal bars on one 0-to-100 scale, filled with a yellow-to-orange-to-red "
       "gradient, one row per class (Ecosystem services, Provisioning, Regulating, Cultural, Biotope) "
       "and a legend keying weak / moderate / strong - which makes the plate read as a colour ramp "
       "and a three-bin scale at once. EACH ROW CARRIES ITS OWN PAIR OF CUT POINTS: the top row "
       "29.45 and 68.37, the provisioning row 25.2 and 57.92, regulating 47.34 and 69.04, cultural "
       "35.6 and 68.12, biotope 24.89 and 55.63. THE PROSE QUOTES ONE GLOBAL STANDARD AND ONLY THE "
       "AGGREGATE ROW MATCHES IT - p10 fixes 'less than 29.45 is weak, between 29.45 and 68.37 "
       "moderate, more than 68.37 strong' - so as a classification standard the figure depicts five "
       "different standards, and the top row is neither the sum of the four below it nor on their cut "
       "points. The legend swatches are flat yellow, orange and red while the bars are continuous "
       "gradients, so no swatch matches the colour under it. The scale carries no axis title and no "
       "unit, so the index is scaled in nothing a reader can name. The cut points are drawn as dashed "
       "vertical markers labelled only by floating numbers. Cited by the sentence below it and "
       "named once in prose.",
       geometry("bar", labels=True, numbers=True), "3", section_kind="result", order=1)

# ============================================================ 4.2.2: the project grid
table(10, 2, S_422,
      "Four columns - Project | Name | Size | Intensity - over four projects, ruled booktabs with no "
      "verticals and the caption above the header, the cleanest grid in the paper. Rows: PA private "
      "enterprise relocation, medium, weak; PB factory construction, medium, moderate; PC national "
      "pipeline engineering, large, strong; PD house construction, small, weak. THE GRID IS ENTIRELY "
      "CATEGORICAL: no cell is numeric, no column sums, and nothing anywhere in the paper defines the "
      "small / medium / large scale or the weak / moderate / strong classes beyond a prose sentence "
      "giving one threshold triple, so the four rows cannot be checked against anything - they are "
      "the paper's assumptions set as a table. THE TWO MEDIUM PROJECTS DIFFER IN INTENSITY (PA weak, "
      "PB moderate), so size is not acting as a proxy for the index, and nothing in the paper "
      "reconciles the difference with the nine component indices the earlier sections compute. The "
      "caption's 'sizes' does not match its header's 'Size', the project column is typeset with "
      "subscripts while the body writes plain PA to PD, and the fourth name ('House construction') "
      "drops the 'project' its three siblings carry. Cited on p11, i.e. AFTER the table it names: "
      "'From the above Table 3 we can see that PA, PB, PC, and PD are land use projects of different "
      "sizes'.",
      dict(rows=5, cols=4, header_rows=1, merged_cells=False, numeric_cols=0, text_cols=4,
           width="full", continued=False, **BOOKTABS),
      CAPT3, "text-layer",
      cited(11, 10, ["Table 3"], 1,
            lead="From the above Table 3 we can see that PA, PB, PC, and PD are land use projects of "
                 "different sizes"),
      section_kind="result", order=2)

# ============================================================ 4.2.2: the rank comparison
figure(11, 1, "bar", CAP4, "text-layer",
       cited(10, 11, ["Figure.4"], 1,
             lead="As shown in Figure.4, we assign different colors to the different ecosystem "
                  "service intensity levels of weak, moderate and strong"),
       S_422,
       "Four gradient-filled bars on a left axis 0 to 100 with an overlaid black line of round "
       "markers read against a right axis that carries three words instead of numbers (strong at the "
       "top, moderate in the middle, weak at the bottom), legend entries 'Intensity' keyed by a "
       "gradient swatch and 'Rank' keyed by a line-and-dot. THE TWO SERIES ARE THE SAME FOUR "
       "NUMBERS: the bars print 19.82, 44.21, 96.74 and 17.64 for PA to PD, and the line's markers sit "
       "on exactly those values, so the 'comparison of ESI original ranking and intensity valuation "
       "indicators' the caption promises shows the two indicators never disagreeing - the line adds "
       "nothing to the bars and the comparison has no content. A RANK IS ALSO NOT A PERCENTAGE: an "
       "ordinal position is plotted on the same 0-to-100 scale as a valuation intensity, and the "
       "right-hand categorical axis carries no tick marks, so where the class boundaries fall on the "
       "left scale cannot be read off the plate at all. Neither axis carries a title or a unit, and "
       "the bar fill varies with bar height, which reads as a value scale rather than a series. The "
       "caption prints below the art; the citing sentence is on the preceding page.",
       geometry("bar", legend="inside", labels=True, numbers=True), "4", section_kind="result")

# ============================================================ 5.1.1: the cost curve
figure(12, 1, "scatter", CAP5, "text-layer",
       cited(12, 12, ["Figure.5"], 2,
             lead="we make the cost of project PA and the discrete points of ESI and fit it with "
                  "Gaussian method, such as Figure.5 shows."),
       S_511,
       "A scatter of about thirty black points of the ecosystem service index against original cost, "
       "ordinate 0 to 1 in tenths, abscissa 0 to 6 with a free-floating 'x 10^5' multiplier printed "
       "outside the frame, one solid blue fitted curve, a legend keying 'Fitting curve' and "
       "'Scatter', a vertical black dashed line labelled 'Forecast area' at about 5 x 10^5 and an "
       "UNLABELLED horizontal red dashed line just above the curve's right-hand plateau. THE METHOD "
       "IS MISNAMED: the text says the points were fitted 'with Gaussian method' while the curve drawn "
       "is a logistic sigmoid and the formula printed under the plate is "
       "ESI = 0.9462/(1+exp(0.000072(Co-312654))), whose upper asymptote is 0.9462; the drawn curve "
       "reads closer to 0.97 at the right edge, so the plate, the formula and the multiplier do not "
       "agree with each other. The scatter is wide about the fit between 3 x 10^5 and 4.5 x 10^5 "
       "(points from about 0.2 up to about 0.9 around a curve near 0.6 to 0.9) and no goodness-of-fit "
       "statistic is printed anywhere, so the logistic claim rests on the eye. Neither axis carries a "
       "unit - 'ESI' is an index and 'Original Cost' is never given a currency - and the multiplier "
       "sits outside the axis so the abscissa alone reads 0 to 6. Named twice on its own page, once "
       "as the lead-in and once as 'From the above Figure.5'.",
       geometry("scatter", legend="inside", labels=True, numbers=True), "5", section_kind="result")

# ============================================================ 5.1.3: the ratio by year, panel a
figure(13, 1, "scatter", CAP6A, "text-layer",
       cited(13, 13, ["Figure.6"], 1,
             lead="As can be seen from Figure.6, without considering the cost of ecosystem services, "
                  "the benefit of an existing project tends to increase"),
       S_513,
       "Panel (a) of a two-panel figure, printed as a separate raster beside panel (b): about "
       "twenty-five blue round markers of the benefit-cost ratio by year from 1995 to 2019 with no "
       "connecting line and no legend, panel letter '(a)' set inside the plot frame over the data "
       "field. THE ORDINATE IS TRUNCATED AT 2, not zero, so the rise from about 2.1 to about 13.9 is "
       "drawn on a frame missing its lower tenth, while its partner panel starts at zero - the two "
       "halves of one figure are therefore on different origins and cannot be compared by eye, which "
       "is the whole purpose of a panel pair. The abscissa is ticked every third year over a series of "
       "annual observations, so individual points are visually unanchored to their years, and the "
       "ratio is given no definition beyond the prose's 'I = Br Cr' two pages earlier. Caption is "
       "printed below the pair, once, and describes both panels; this row's slice of it is panel (a).",
       geometry("scatter", panels=2, layout="1x2", numbers=False), "6(a)", section_kind="result",
       order=1)

# ============================================================ 5.1.3: the ratio by year, panel b
figure(13, 2, "scatter", CAP6B, "text-layer",
       cited(13, 13, ["Figure.6"], 1,
             lead="although the growth trend is relatively slow in the early stage, the benefits of "
                  "the project will gradually increase over time"),
       S_513,
       "Panel (b) of the same figure, a raster of the same size and scale beside (a): about "
       "twenty-five blue round markers rising from about 0.2 in 1995 to about 4.4 in 2019, ordinate 0 "
       "to 12 in steps of two, no line, no legend, panel letter inside the frame, and its last "
       "abscissa label clipped to '201' where the crop meets the page edge - the panel letter and the "
       "marker style are identical to panel (a)'s, so the only thing distinguishing 'without the cost "
       "of ecosystem services' from 'with it' is the letter. THE TWO PANELS ARE THE PAPER'S ONE "
       "QUALITATIVE CLAIM AND THEY DIFFER ONLY IN SCALE AND ORIGIN: (a) is a rise to a peak and a fall, "
       "(b) a monotone rise whose top value is a third of (a)'s, which the prose reads as 'the benefits "
       "of the project will gradually increase over time'. The paper's own sentence order shows the "
       "claim is carried by the pair, not either panel, and the caption typesets the hyphen break as "
       "'benefit- cost'. The citing sentence for this panel never names the figure - the naming "
       "sentence is the panel-(a) one on the same page.",
       geometry("scatter", panels=2, layout="1x2", numbers=False), "6(b)", section_kind="result",
       order=2)

# ============================================================ 5.2: the forecast, panel a
figure(16, 1, "line", CAP7A, "text-layer",
       cited(15, 16, ["Figure.7"], 1,
             lead="we predict the changes over 2019-2035 years and got the change curve as shown in "
                  "the Figure.7."),
       S_52,
       "Panel (a) of the forecast figure: the 1995-2019 markers, one blue solid regression curve and "
       "two red dotted confidence bounds at 95%, plotted to 2034 with a vertical dashed line at 2019 "
       "marking the forecast, a legend keying 'Income-cost ratio vs. Year', 'Regression curve', "
       "'Lower confidence bounds (95%)' and 'Upper confidence bounds (95%)', and an italic 'Forecast "
       "area' label placed BELOW the zero line in empty space rather than over the forecast region. "
       "THE LEGEND RENAMES THE QUANTITY: axis and caption both say benefit-cost ratio while the data "
       "series is keyed 'Income-cost ratio vs. Year', and panel (b)'s series is keyed 'Benefit vs. "
       "Year', so one figure carries three names for what the model treats as one ratio. The two "
       "confidence keys print identical red dotted swatches and the band is neither filled nor "
       "labelled on the plot; the ordinate runs to -6 to hold the falling tail, with a bold zero rule. "
       "The crossing and the peak are annotated with red arrows only - no number is printed at either "
       "- so the peak the prose reports as 2013 has no value on the plate. THE PAGE'S NEXT SENTENCE "
       "MISNAMES THE PANEL: it reads 'As can be seen from the Figure.8(a)', which points at Figure 8 "
       "for what is Figure 7's left panel.",
       geometry("line", panels=2, layout="1x2", legend="inside", labels=True), "7(a)",
       section_kind="result", order=1)

# ============================================================ 5.2: the forecast, panel b
figure(16, 2, "line", CAP7B, "text-layer",
       cited(16, 16, ["Figure.7(b)"], 1,
             lead="As for the Figure.7(b), the project PA is based on the consideration of the cost "
                  "of ecosystem services, that is, the external cost."),
       S_52,
       "Panel (b) of the forecast figure in the same style: about twenty-five black markers, one blue "
       "regression line, a pair of red dashed prediction bounds under a SINGLE legend entry "
       "('Pred bounds (95%)') although two lines are drawn, 'Forecast area' placed far above the "
       "curve, and a 0-to-12 ordinate against panel (a)'s -6-to-14. THE PANEL CONTRADICTS THE SHAPE "
       "ITS CAPTION PROMISES: (a) is a parabola peaking near 13.5 at 2013 and falling through zero "
       "just before 2034, and (b) - which is supposed to be the same project with the ecosystem cost "
       "added - is a nearly straight monotone rise from about 0 to about 6 with no peak and no "
       "decline inside the forecast window. The prose then reads the pair as 'the benefit does not "
       "show a declining trend, but steadily increases', which is true of (b) and false of (a) on one "
       "and the same fitted model. The markers sit essentially on the line, so the observed scatter "
       "the fitted band is meant to bound is invisible at print size. Panel letter '(a)' and '(b)' "
       "are the only per-panel identification; the caption is printed once below the pair.",
       geometry("line", panels=2, layout="1x2", legend="inside", labels=True), "7(b)",
       section_kind="result", order=2)

# ============================================================ 5.3: the four-curve comparison
figure(16, 3, "line", CAP8, "text-layer",
       cited(16, 16, ["Fiugre.8", "Figure.8"], 3,
             lead="we have combined the two maps of Fiugre.8 to facilitate comparative analysis."),
       S_53,
       "The comparison plate the paper builds its result on: four curves over 1995-2034 - "
       "'Considering ecosystem services' solid blue, 'Considering ecosystem services(predicted)' "
       "dashed light blue, 'Not considering ecosystem services' solid orange, 'Not considering "
       "ecosystem services(predicted)' dashed orange - on a -4 to 12 ordinate with a zero rule, a "
       "dashed vertical at 2019, two red circles with arrows (the crossing of the two predicted curves "
       "at about 2026 and the orange predicted curve's zero crossing at about 2032), dotted drop lines "
       "from the 2013 peak and from the zero crossing, and a SHADED BLUE REGION LABELLED IN PLACE "
       "'Anti-over region' WITH NO LEGEND ENTRY. The plate is the one exhibit whose two headline "
       "events the text also states - the intersection at 2026 and the collapse to zero - and they "
       "agree in the decade, but the drop line lands at about 2032 while Table 4 scores 'Zero' at "
       "2033, and the 2013 peak is marked without a value although Table 4 prints 11.38 for it. "
       "Nothing on the plate carries a number: the crossings, the peak and the zero are all left to "
       "the reader's eye while the four curves' legend carries the paper's only description of what "
       "is being compared. THE CITATION SPELLS THE NUMBER WRONG - 'the two maps of Fiugre.8' - and "
       "the corrected spelling appears only in the caption printed beneath the plate and in the "
       "paragraph overleaf. Caption prints BELOW.",
       geometry("line", legend="inside", labels=True), "8", section_kind="result", order=3)

# ============================================================ 5.3: the BCR grid
table(17, 1, S_53,
      "Nine columns in a closed box - the project label and the N / Y switch merged down two rows "
      "each, then a row-label column over six years (1995, 2013, 2019, 2026, 2030, 2033) - and four "
      "data rows: N BCR 1.06 11.38 10.48 6.13 2.26 0, N Description arrows and words, Y BCR 0.73 "
      "6.03 6.10 6.13 6.24 6.39, Y Description six arrows. THE ARITHMETIC INSIDE THE GRID IS "
      "CORRECT AND THAT IS WORTH RECORDING: 11.38 is the true maximum of the N row and 'Highest' sits "
      "at 2013; every N arrow matches the sign of the step it describes; the Y row rises strictly, so "
      "its six arrows are right; and N and Y are both 6.13 at 2026, which is exactly where "
      "'Intersection' is printed. WHAT THE GRID DOES NOT DO IS SET THOSE NUMBERS AS NUMBERS: the "
      "Description rows mix prose words and arrow glyphs into a numeric column, so no decimal point "
      "aligns down the table and nothing in the table or caption keys the arrows; the final value "
      "prints as bare '0' where its eleven neighbours carry two decimals; the corner cell above the "
      "row-label column reads 'Year', which is the label for the six columns to its right, leaving "
      "the row-label column's head empty; and 'Intersection' names no curves. THE METRIC IS RENAMED "
      "ACROSS THE PAPER'S OWN GRIDS: this table says BCR while the three appendix tables of the same "
      "template say ICR, with no note. No unit is printed; the ratio is dimensionless. Cited by the "
      "sentence above it and by its own caption, which types the pointer 'Figure.8' with the full "
      "stop inside the number.",
      dict(rows=5, cols=9, header_rows=1, merged_cells=True, numeric_cols=6, text_cols=3,
           continued=False, **ANNEX),
      CAPT4, "text-layer",
      cited(17, 17, ["Table 4"], 2,
            lead="Table 4 shows the specific values and descriptions of some special information "
                 "points in Figure 8."),
      section_kind="result")

# ============================================================ 6.1: the four pies
figure(18, 1, "other", CAP9, "text-layer",
       cited(17, 18, ["Figure.9"], 1,
             lead="From the pie chart shown in Figure.9, we can see land use projects of different "
                  "scales PA, PB, PC, and PD."),
       S_61,
       "Four 3-D exploded pies in a row under one shared two-entry legend strip (blue "
       "'Unsustainable measures', orange 'Sustainable measures'), each pie headed only by a letter "
       "beneath it, each split in two and each slice labelled inside in white: PA 71 / 29, PB 67 / "
       "33, PC 91 / 9, PD 54 / 46. THE PROSE'S READING IS FAITHFUL TO THE PIXELS: 'for national "
       "pipeline projects, projects taking sustainable development measures accounted for 91%' names "
       "panel (c), which is PC, national pipeline engineering - so the one number the text quotes is "
       "attributable and the four pies are what make the scale comparison. THE PLATE'S FAULTS ARE "
       "TECHNICAL: the 3-D perspective distorts every wedge so printed percentages do not match "
       "apparent areas (PC's 91% wedge visually overshoots its number), the 9% label is squeezed into "
       "a sliver and rotated until it is nearly illegible, no pie carries a title, and the legend "
       "puts the minority category first. The scale claim the paragraph draws from the four pies - "
       "'as the scale of the project increases, the proportion ... is also increasing' - is consistent "
       "with 54 (small PD) < 67 and 71 (both medium) < 91 (large PC). Family recorded as other: the "
       "closed vocabulary has no pie class, and the plate is neither a scatter nor a bar.",
       geometry("other", panels=4, layout="1x4", legend="above", labels=True, numbers=True,
                three_d="perspective-bars"), "9", section_kind="result",
       other_note="four 3-D pie charts - the closed vocabulary has no pie class")

# ============================================================ 6.1: the six indicators
figure(18, 2, "other", CAP10, "text-layer",
       cited(18, 18, ["Figure.10"], 1,
             lead="and the sustainable development indicators are shown in Figure.10."),
       S_61,
       "Six clip-art icons scattered around a central disc labelled 'Sustainable development', each "
       "beside one label - Gas regulation, Solid regulation, Soil conservation, Water regulation, "
       "Biodiversity protection, Recreation & tourism - in six unrelated visual styles and scales. "
       "SIX HAND-CURSOR ARTEFACTS ARE VISIBLE beside the icons, so the plate is a pasted screenshot "
       "taken off an icon site rather than artwork the paper drew, and a sixth icon (a blue rising bar "
       "chart with an arrow) sits beside the centre disc belonging to no label at all. THERE IS NO "
       "RELATION IN THE PIXELS: no arrow, no link, no hierarchy and no quantity connects the six "
       "indicators to the centre or to each other, so the part-whole relation the paper needs - eleven "
       "indicators split into six sustainable and five unsustainable - is asserted in the paragraph "
       "and drawn nowhere. THE SPLIT IS ALSO NOT THE ONE THE EARLIER SECTIONS USE: the weight grid's "
       "eleven leaves are Provisioning (three), Regulating (three), Biotope (three) and Cultural "
       "(two), and these six names re-cut the same eleven into a different six with two names ('Solid "
       "regulation', 'Recreation & tourism') carried over verbatim and no page mapping the two "
       "partitions. Its caption is printed below; family recorded as other for the same reason as "
       "Figure 9.",
       geometry("other", labels=True), "10", section_kind="result", order=2,
       other_note="six pasted clip-art icons around a centre disc, with no link drawn between them")

# ============================================================ 6.2: the four sustainable curves
figure(19, 1, "line", CAP11, "text-layer",
       cited(18, 19, ["Figure.11"], 3,
             lead="The results are shown in Figure.11."),
       S_62,
       "Four curves of the benefit-cost ratio by year from 1995 to 2034, solid to 2019 and dotted "
       "into the forecast, ordinate 0 to 7 in unit steps, legend keying Project A to D as four filled "
       "rectangles, a dashed vertical at 2019, an italic 'Forecast area', and FOUR BLACK "
       "DOUBLE-HEADED VERTICAL ARROWS annotating the gaps between curves around 2021, 2028, 2031 and "
       "2033 WITH NO KEY AND NO NUMBER. THE LEGEND SWATCHES DO NOT MATCH THE DRAWN CURVES - the key "
       "prints dark red, dark green, blue and orange while the strokes read blue, green, "
       "purple-brown and yellow - and the keys are plain filled rectangles, so they carry neither the "
       "line style nor the marker that distinguish observed from predicted. THE PLATE'S WINDOW "
       "DISAGREES WITH ITS OWN LEAD-IN: the paragraph above says the model is used to predict the "
       "ratio 'influenced by sustainable development measures for 2004-2018' while the abscissa runs "
       "from 1995, and the axis title is typeset 'Benefit-cost ratio(sustainable measures)' with no "
       "space after the parenthesis and a lower-case s. The four unlabelled double-headed arrows are "
       "the only indication that the divergence between projects is the finding. Cited three times "
       "across pp18-19, named as 'Figure.11' with a full stop inside the number.",
       geometry("line", legend="inside", labels=True, numbers=True), "11", section_kind="result")

# ============================================================ 6.2: the fitting grid
table(19, 2, S_62,
      "Two columns - Project | Equation - over the four projects, booktabs with a rule above the "
      "header, under it and at the foot, the equation strings centred in a column wide enough to hold "
      "them. As printed: B_PA = 87.31 exp(0.1056 dt) + 0.0014, B_PB = 88.4 exp(0.1098 dt) + 0.0014, "
      "B_PC = 101.4 exp(0.1198 dt) + 0.0014, B_PD = 11.98 exp(0.1033 dt) + 0.0013. THE FOUR "
      "EQUATIONS CANNOT GENERATE THE PAPER'S OWN DATA: every one has a positive exponent, so each "
      "benefit grows without bound in dt, while Table 4's N row and all three appendix tables run "
      "their non-sustainable series down to exactly zero at a printed final year - Table 4 reaches 0 "
      "at 2033, Appendix 1 at 2028, Appendix 2 at 2020 and Appendix 3 at 2056. Nothing reconciles a "
      "monotone exponential with a series that lands on zero. THE PRINTING IS UNEVEN: two coefficients "
      "carry two decimals and two carry one, the constant term is 0.0014 three times and 0.0013 for "
      "PD, and the independent variable is written 'dt' (a delta) which no page defines - the reader "
      "cannot tell whether it is elapsed years from 1995, from 2019, or something else. PD's amplitude "
      "11.98 is about a seventh of its three siblings for no stated reason, and the nested subscripts "
      "B_PA etc. are set as a subscript inside a subscript. NO GOODNESS-OF-FIT STATISTIC IS PRINTED "
      "anywhere - no R2, no standard error, no n - so none of the four fits is checkable. Cited by "
      "the sentence above it and by its caption.",
      dict(rows=5, cols=2, header_rows=1, merged_cells=False, numeric_cols=0, text_cols=2,
           width="full", continued=False, **BOOKTABS),
      CAPT5, "text-layer",
      cited(19, 19, ["Table 5"], 2, lead="The fitting results are shown in Table 5."),
      section_kind="result", order=2)

# ============================================================ 7: the sensitivity plate
figure(20, 1, "line", CAP12, "text-layer",
       cited(20, 20, ["Figure 12"], 1,
             lead="Based on the sustainable development factors calculated from the above four "
                  "projects, we calculate their real benefit-cost ratio, as shown in Figure 12."),
       S_7,
       "Four curves of the ratio by year to 2034 on a 1-to-9 ordinate, solid to 2019 and dotted "
       "after, a dashed vertical at 2019, an italic 'Forecast area', and a LEGEND THAT READS "
       "'theta(Project A)=87.31', 'theta(Project B)=88.4', 'theta(Project C)=101.4', 'theta(Project "
       "D)=11.98'. THOSE FOUR NUMBERS ARE TABLE 5'S FITTED AMPLITUDES, not the sensitivity's "
       "free parameter: the section that follows sweeps theta over 80, 60, 40 and 20 (Figure 13), so "
       "the legend mixes a project label, a parameter symbol and a quantity the preceding table "
       "already fixed, and a reader cannot tell whether colour encodes the project or the parameter. "
       "TWO OF THE FOUR CURVES COINCIDE: A (green) and B (orange) end within a tenth of each other at "
       "the right edge and are not separable at print size, although their legends differ, while C "
       "and D separate clearly - which is itself the shape of the amplitudes 87.31, 88.4, 101.4 and "
       "11.98. The legend colours for A to D differ again from Figure 11's assignment, the theta "
       "glyph is printed small and inconsistently, no value is printed at any endpoint, and nothing "
       "on the plate states what is being varied. Cited once by the sentence that introduces it; "
       "caption prints BELOW.",
       geometry("line", panels=1, legend="inside", labels=True, numbers=True), "12",
       section_kind="result")

# ============================================================ 7: the parameter sweep
figure(21, 1, "line", CAP13, "text-layer",
       cited(21, 21, ["Figure.13"], 1, lead="The final result is shown in Figure.13."),
       S_7,
       "The robustness plate: four curves on a 1-to-8 ordinate, solid to 2019 and dotted into the "
       "forecast, legend keying the parameter at four values only - 'theta=80' blue, 'theta=60' "
       "orange, 'theta=40' green, 'theta=20' purple - with a dashed vertical at 2019 and an italic "
       "'Forecast area'. THE CLAIM IS CHECKABLE ON THE PIXELS AND HOLDS: at 2034 the spacing between "
       "adjacent curves shrinks as the parameter grows, the 80-to-60 gap being about 0.3 against the "
       "40-to-20 gap of about 1.0 to 1.3, so the paper's sentence that the model is stable because "
       "adjacent parameters converge is supported by the drawing rather than imposed on it. THE "
       "EFFECT IS SMALL AND LATE: the four curves are nearly superimposed from 1995 to about 2013 and "
       "separate only after 2022, and the total vertical spread at 2034 is about 1.6 units on an "
       "8-unit axis - roughly a fifth of the frame - so the stability is real but the plate has to be "
       "read against the forecast tail alone. The theta symbol is printed in the caption but "
       "undefined in the visible art (the parameter's meaning is in the body's equation 23), and no "
       "endpoint value is printed. Cited once by the deictic sentence 'The final result is shown in "
       "Figure.13.'",
       geometry("line", legend="inside", labels=True, numbers=True), "13", section_kind="result")

# ============================================================ Appendices: the three result grids
APP_SPEC = dict(rows=5, cols=9, header_rows=1, merged_cells=True, numeric_cols=6, text_cols=3,
                continued=False, **ANNEX)

table(25, 1, S_A1,
      "The result grid for project PB in the same nine-column closed-box template as Table 4, with "
      "the series renamed ICR: N ICR 2.38 12.52 10.26 6.32 2.18 0 at 1995, 2012, 2015, 2020, 2025 and "
      "2028, its Description row carrying arrows plus 'Highest' at 2012, 'Intersection' at 2020 and "
      "'Zero' at 2028; Y ICR 1.29 3.68 5.81 6.32 7.24 7.89 with six rise arrows. EVERY INTERNAL "
      "CHECK PASSES: 12.52 is the row maximum where 'Highest' stands, the N arrows match their step "
      "signs, Y rises strictly, and N and Y meet at 6.32 in 2020 where 'Intersection' is printed. The "
      "defects are the family's: a bare '0' against two-decimal neighbours, arrow glyphs keyed "
      "nowhere, 'Intersection' naming no curves, 'Year' occupying the corner cell, decimals broken by "
      "the annotation rows, and a time grid (1995, 2012, 2015, 2020, 2025, 2028) that does not match "
      "Table 4's - the first interval is seventeen years and the last three. NO SENTENCE NAMES THE "
      "APPENDIX NUMBER: p17 says only 'The specific results are shown in Appendix 1，2，3', one "
      "sentence naming all three grids, which is what this row's mention records.",
      APP_SPEC, CAPA1, "text-layer",
      cited(17, 25, ["Appendix 1"], 1,
            lead="The specific results are shown in Appendix 1，2，3."),
      section_kind="result")

table(25, 2, S_A2,
      "The result grid for project PC, same template: N ICR 4.92 20.16 16.24 11.72 4.37 0 at 1995, "
      "2010, 2013, 2016, 2018 and 2020 with 'Highest' at 2010, 'Intersection' at 2016 and 'Zero' at "
      "2020; Y ICR 2.67 6.27 9.19 11.72 12.46 13.25 with six rise arrows. The internal checks pass "
      "again (20.16 is the row maximum, arrows match signs, Y is strictly increasing, both series are "
      "11.72 at 2016). THE SAMPLING IS THE ODDS ONE OUT: the five intervals are 15, 3, 3, 2 and 2 "
      "years, so the zero is asserted two years after a still-declining 4.37, against a trajectory "
      "that the preceding intervals would put well above zero - the exponential of Table 5 for PC has "
      "the LARGEST amplitude of the four (101.4), which makes the fastest collapse to zero the least "
      "explicable. Same family defects: bare '0', unkeyed arrows, 'Year' in the corner cell, "
      "annotation rows inside a numeric column, no unit. Named only by p17's collective sentence.",
      APP_SPEC, CAPA2, "text-layer",
      cited(17, 25, ["Appendix 2"], 1,
            lead="The specific results are shown in Appendix 1，2，3."),
      section_kind="result", order=2)

table(25, 3, S_A3,
      "The result grid for project PD, same template: N ICR 1.06 6.33 5.49 3.87 1.75 0 at 1995, "
      "2026, 2035, 2043, 2050 and 2056 with 'Highest' at 2026, 'Intersection' at 2043 and 'Zero' at "
      "2056; Y ICR 0.73 2.26 3.15 3.87 4.26 4.82 with six rise arrows. THE 1995 COLUMN IS TABLE 4's "
      "1995 COLUMN COPIED: PD's opening pair is N 1.06 and Y 0.73, digit for digit the pair Table 4 "
      "prints for PA, while the other two appendices carry their own openings (PB 2.38 / 1.29, PC "
      "4.92 / 2.67) - so one of the four projects' base years is either a paste error or a genuine "
      "coincidence the paper never remarks on, and PD is also the amplitude outlier of Table 5 "
      "(11.98 against 87.31, 88.4 and 101.4). Its time grid is the most irregular of the four: a "
      "31-year first interval to 2026, then 9, 8, 7 and 6. Internal checks pass as in its siblings. "
      "Same family defects, no unit, named only by p17's collective sentence.",
      APP_SPEC, CAPA3, "text-layer",
      cited(17, 25, ["Appendix 3"], 1,
            lead="The specific results are shown in Appendix 1，2，3."),
      section_kind="result", order=3)

BANNER = ("A 678-path vector block at y=767-839 of the page, printing '关注数学模型 2 MATHmodels "
          "获取更多资讯' - an advertiser's banner set as page furniture on every one of the paper's "
          "twenty-five pages. Measured as a region because it is drawn as vector paths at the foot of "
          "every page; not an exhibit of any kind. Refused per page rather than collapsed, because "
          "each page's banner is its own measured region and collapsing them would overstate the "
          "census's coverage.")

for _page in range(1, 26):
    _last = max(k[1] for k in REG if k[0] == _page)
    exclude(_page, _last, "not-an-exhibit", BANNER)

RULES = [
    "Measure first, then read the pixels: forty-seven measured regions over all twenty-five pages "
    "resolve into fifteen figure rows, seven table rows and twenty-five refusals, with nothing "
    "unaccounted [place.doc_order].",
    "Twenty-five of the forty-seven regions are the same advertiser's banner on every page of the "
    "paper, so the census keeps a region count that its exhibit count does not share "
    "[place.page_order].",
    "The weight grid prints two normalisations of the same eleven indicators: its leaf weights sum "
    "to exactly 1.0000 and its four band weights also sum to exactly 1.0000, while every band total "
    "disagrees with its own sub-rows by 0.0215, 0.0342, 0.0075 and -0.0632 [table.numeric_cols].",
    "One panel pair is printed on two different ordinate origins - Figure 6(a) truncated at 2 and "
    "6(b) from 0 - so the comparison the figure exists to make cannot be read across the pair "
    "[geometry.family].",
    "One figure renames its own series: Figure 7(a) keys the data 'Income-cost ratio vs. Year' on "
    "axes labelled benefit-cost ratio, and panel (b) keys the same quantity 'Benefit vs. Year' "
    "[geometry.legend].",
    "The citation of Figure 7's left panel is written 'Figure.8(a)' on p15, two pages before the "
    "plate it names, and the citation of Figure 8 is written 'Fiugre.8' on p16 "
    "[mention.lead_sentence].",
    "Two exhibits are named by no sentence at all - Figure 1, reached only through 'The whole "
    "modeling process can be shown as follows:', and Figure 2, whose number appears only in its "
    "caption - while Table 2 is reached twice, once with the pointer set in lower case "
    "[mention.count].",
    "A caption can promise a relation the pixels do not draw: Figure 9's four pies are labelled and "
    "checkable, but Figure 10's six icons carry cursor artefacts and no link of any kind to the "
    "centre they are arranged around [caption.verbatim].",
    "The appendix grids pass their internal checks (maximum where 'Highest' stands, arrows matching "
    "step signs, both series meeting where 'Intersection' prints) but their final values print as "
    "bare '0' and their arrows carry no key [table.numeric_cols].",
    "The paper's exponents cannot produce its own series: Table 5 fits four functions with positive "
    "growth terms while Table 4 and the three appendices run the non-sustainable series to exactly "
    "zero at a printed year [table.text_cols]",
    "The notation grid on p4 is live text rather than a measured region, so it is not censused "
    "although the paper's Table 1 numbering starts there [table.header_rows]",
]

NOTE = """\
Paper 183, Team 1903455: ecosystem services priced into the cost-benefit analysis of land use projects,
for problem E 2019. Eleven indicators are weighted by entropy weight and coefficient of variation into
an ecosystem service index, the index is clustered into weak, moderate and strong, the index is fitted
against original cost with a curve the text calls Gaussian and the formula prints as a logistic, a
support vector regression forecasts the benefit-cost ratio to 2035, a sustainable development factor
rescales it, and one parameter is swept for sensitivity. Twenty-five pages, forty-seven measured
regions, of which twenty-two are exhibits, resolving into FIFTEEN FIGURE ROWS and SEVEN TABLE ROWS,
with twenty-five refusals and nothing unaccounted.

THE FRAME IS DRAWN ONCE AND THEN NEVER USED. Figure 1 lays out the whole pipeline - indicators, two
weighting methods on one arrow, the index, hierarchical clustering, an SVM regression, an evaluation
model, a sustainable development factor feeding a true cost-benefit analysis, advice, and a dashed box
of four practical projects - and no plate after it returns to that frame: the plates from Figure 3
onward are all matplotlib output about one project or four, and the box labels A to D never reappear.

THE WEIGHT GRID PRINTS TWO DIFFERENT NORMALISATIONS AND NEITHER IS RECONCILED WITH THE OTHER. Table 2
gives four band weights (0.2591, 0.2647, 0.1900, 0.2862) which sum to exactly 1.0000, and eleven leaf
weights which also sum to exactly 1.0000. Every band total fails its own sub-rows: provisioning prints
0.2591 where its three leaves sum to 0.2806, regulating 0.2647 against 0.2989, biotope 0.1900 against
0.1975, and cultural 0.2862 against 0.2230. The distinction between the two scales is carried by cell
shading rather than by a column label, and the ESI formula that follows multiplies W1 to W4 by the four
class indices without saying which scale W1 to W4 belong to.

THE PROSE QUOTES ONE CLASSIFICATION STANDARD AND THE FIGURE PRINTS FIVE. p10 states that below 29.45
is weak, 29.45 to 68.37 moderate and above 68.37 strong. Figure 3 prints per-row cut points - 25.2 and
57.92 for provisioning, 47.34 and 69.04 for regulating, 35.6 and 68.12 for cultural, 24.89 and 55.63
for biotope - so only the aggregate row uses the numbers the text quotes, and the aggregate row is
neither a total of the four below it nor on their boundaries. The three-bin legend swatches are flat
colours over continuous gradient bars, and the 0-to-100 scale carries no title and no unit.

THE PANEL PAIR IS TWO PLOTS OF ONE MODEL ON TWO ORIGINS. Figure 6(a) truncates its ordinate at 2 and
rises to about 13.9, Figure 6(b) starts at 0 and rises to about 4.4, and the paper's one qualitative
claim - without the ecosystem cost the ratio peaks and falls, with it the ratio keeps rising - is
carried entirely by that pair. Figure 7 repeats the exercise for the forecast: (a) is a parabola
peaking near 13.5 at 2013 and crossing zero before 2034 on a -6-to-14 ordinate, (b) is a near-straight
rise to about 6 on a 0-to-12 ordinate with no peak at all, its two confidence bounds keyed as one
legend entry, and the paragraph that reads the pair cites 'Figure.8(a)' for panel (a) of Figure 7.

THE ONE ARITHMETIC THAT FAILS ACROSS EXHIBITS IS THE FIT AGAINST THE SERIES. Table 5 fits four
exponentials, B = a exp(b dt) + c with b positive for all four projects, so each benefit grows without
bound; Table 4 and the three appendix grids run the corresponding non-sustainable series to a printed
zero at a stated year (2033 for PA, 2028 for PB, 2020 for PC, 2056 for PD). Inside the grids the
arithmetic is sound - the maximum sits where 'Highest' prints, every arrow matches its step's sign, and
the two series meet exactly where 'Intersection' stands - but the grids' annotation rows break every
decimal column, their final values print as bare zero, their arrow glyphs are keyed nowhere, and the
metric is called BCR in Table 4 and ICR in all three appendices. Appendix 3's opening pair for PD,
N 1.06 and Y 0.73, is Table 4's opening pair for PA digit for digit.

THE APPENDIX IS THREE GRIDS OF ONE TEMPLATE, and the fourth exhibit of the family is Table 4 in the
body: nine columns, the project and the N / Y switch merged down, six years, and a Description row of
words and arrows stacked inside the numeric columns. That template is the paper's one successful
device: unlike most grids in this corpus, its internal checks can actually be run, and they pass.

FIGURE 9 IS FAITHFUL AND FIGURE 10 IS DECORATION. The four 3-D pies carry printed percentages (PA
71/29, PB 67/33, PC 91/9, PD 54/46) and the sentence that reads them names national pipeline
engineering, i.e. the 91/9 panel - so the paper's quoted statistic is attributable, even though
perspective distorts the wedges and the 9% label is nearly illegible. Figure 10 is six clip-art icons
taken off an icon site with the mouse cursors still in the screenshot: no link, no hierarchy, and no
mapping from its six names back to the weight grid's eleven leaves.

Families: line 6 (Figures 7a, 7b, 8, 11, 12, 13), table-grid 7 (Tables 2, 3, 4, 5 and Appendices 1-3),
scatter 3 (Figures 5, 6a, 6b), flowchart-or-schematic 2 (Figures 1, 2), bar 2 (Figures 3, 4), other 2
(Figures 9, 10 - pies and pasted icons, neither of which the closed vocabulary names).
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

out = PROXY / "pc183-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
