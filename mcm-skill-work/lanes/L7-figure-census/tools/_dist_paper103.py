"""Hand census of P-D-2016-42220-7261f9d3 (Team 42220, 21 pages, 28 measured regions).

An information-flow paper: a double-layer network, six media, an asymmetry index built from AHP
weights, then five applications. Twenty-eight measured regions resolve into TWENTY-THREE FIGURE ROWS
and FIVE TABLE ROWS, with nothing unaccounted and no refusals.

  p4  r1  Figure 1    node-link-network    the double-layer schematic: regions inside, global outside
  p5  r1  Figure 2    node-link-network    sender/receiver/content diagram, S1 S2 into R1 R2
  p6  r1  Table 1     table-grid           the six media and their weights, two blocks of two columns
  p7  r1  Table 2     table-grid           ten content indicators in two merged groups
  p9  r1  Figure 3    map-or-plan-view     GDP per capita, a six-band world choropleth
  p9  r2  Figure 4    node-link-network    the seven chosen countries joined by straight lines on a map
  p10 r1  Figure 5    flowchart-or-schematic  point source flow: eight rays, radius rho, angle theta
  p12 r1  Figure 6    node-link-network    the spreading network, sixteen edge values printed
  p12 r2  Figure 5    node-link-network    the original network - a SECOND figure numbered 5
  p12 r3  Figure 7    line                 sensitivity of W, three curves 0.9W / W / 1.1W
  p12 r4  Figure 8    line                 sensitivity of Si, the same three-curve shape
  p13 r1  Figure 9    bar                  propagation delay with one index removed, five bars
  p14 r1  Figure 10   line                 media market share in America, six series
  p14 r2  Figure 11   line                 media market share in China, six series
  p14 r3  Table 3     table-grid           America's six shares, one "Weigh" row
  p14 r4  Table 4     table-grid           China's six shares, one "Weigh" row
  p15 r1  Figure 12   line                 newspaper market share, actual and forecast
  p15 r2  Figure 13   line                 Internet market share, actual and forecast
  p15 r3  Table 5     table-grid           true value, forecast and both errors, two media only
  p15 r4  Figure 14   node-link-network    the spread network of the Bin Laden example
  p16 r1  Figure 15   line                 the ratio s in America against year
  p16 r2  Figure 16   line                 the ratio s in Congo against year
  p17 r1  Figure 17   line                 propagation probability and delay, America
  p17 r2  Figure 18   line                 propagation probability and delay, Congo
  p18 r1  Figure 19   line                 public opinion over time
  p19 r1  Figure 20   line                 propagation probability against information value
  p19 r2  Figure 21   line                 propagation delay against information value
  p20 r1  Figure 22   line                 the change rate of public opinion

THE NUMBER FIVE IS USED TWICE: p10 prints "Figure 5 A point source flow" and p12 prints "Figure 5
Original network", and p12's own citing sentence calls the second of them "Figure 5" without
distinguishing it from the first.

TABLE 5'S ABSOLUTE ERROR FOR THE INTERNET IS A DECIMAL SLIP: 0.773 against a forecast of 0.785 is
0.012, not the 0.12 printed, while the 1.55% relative error beside it is right.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-D-2016-42220-7261f9d3"
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


S_31 = [head(4, "3.1 Frame")]
S_32 = [head(5, "3.2 Inner Layer")]
S_321 = [head(5, "3.2.1 Index Extraction")]
S_33 = [head(9, "3.3 Outer Layer")]
S_34 = [head(11, "3.4 Information Flow Situation")]
S_351 = [head(12, "3.5.1 Change the Value")]
S_352 = [head(13, "3.5.2 Remove a Index")]
S_42 = [head(14, "4.2 Task 2")]
S_431 = [head(16, "4.3.1 Communication networks")]
S_432 = [head(16, "4.3.2 Communication networks")]
S_441 = [head(17, "4.4.1 Foundation of Model")]
S_451 = [head(19, "4.5.1 Influence in Spreading")]
S_452 = [head(19, "4.5.2 Influence in Public Opinion")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
for _group in (S_31, S_32, S_321, S_33, S_34, S_351, S_352, S_42, S_431, S_432, S_441, S_451, S_452):
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


CAP1 = caption("Figure 1 A double-layer Network", numbering="Figure N")
CAP2 = caption("Figure 2 Relationships of three entities in the diffusion process", numbering="Figure N")
CAPT1 = caption("Table 1 Different media and their effect on spreading communication",
                kind="Table", position="above", numbering="Table N")
CAPT2 = caption("Table 2 Evaluation indexes and their weights",
                kind="Table", position="above", numbering="Table N")
CAP3 = caption("Figure 3 GDP per capita", numbering="Figure N")
CAP4 = caption("Figure 4 Global network", numbering="Figure N")
CAP5 = caption("Figure 5 A point source flow", numbering="Figure N")
CAP5b = caption("Figure 5 Original network", numbering="Figure N")
CAP6 = caption("Figure 6 Information spreading network", numbering="Figure N")
CAP7 = caption("Figure 7 Sensitivity analysis of W", numbering="Figure N")
CAP8 = caption("Figure 8 Sensitivity analysis of Si", numbering="Figure N")
CAP9 = caption("Figure 9 Sensitivity Analysis of Removing a index", numbering="Figure N")
CAP10 = caption("Figure 10 Media Market Share in America", numbering="Figure N")
CAP11 = caption("Figure 11 Media Market Share in China", numbering="Figure N")
CAPT3 = caption("Table 3 Media Market Share in America",
                kind="Table", position="above", numbering="Table N")
CAPT4 = caption("Table 4 Media Market Share in China",
                kind="Table", position="above", numbering="Table N")
CAP12 = caption("Figure 12 Market share of Newspaper", numbering="Figure N")
CAP13 = caption("Figure 13 Market share of the Internet", numbering="Figure N")
CAPT5 = caption("Table 5 The Error in the Market Share of Different Media",
                kind="Table", position="above", numbering="Table N")
CAP14 = caption("Figure 14 Information Spread Network", numbering="Figure N")
CAP15 = caption("Figure 15 Ratio changes in America", numbering="Figure N")
CAP16 = caption("Figure 16 Ratio changes in Congo", numbering="Figure N")
CAP17 = caption("Figure 17 Capacities changes in America", numbering="Figure N")
CAP18 = caption("Figure 18 Capacities changes in Congo", numbering="Figure N")
CAP19 = caption("Figure 19 Public Opinion Changes", numbering="Figure N")
CAP20 = caption("Figure 20 Propagation Probability Changes", numbering="Figure N")
CAP21 = caption("Figure 21 Propagation Delay Changes", numbering="Figure N")
CAP22 = caption("Figure 22 Changes of Change rate", numbering="Figure N")

BOOKTABS = {"rule_style": "booktabs", "zebra": False, "diagonal_header": False,
            "units_in_header": False, "decimal_aligned": False, "orientation": "portrait",
            "note_sentence": ""}
BOXED = {"rule_style": "vertical-rules", "zebra": False, "diagonal_header": False,
         "units_in_header": False, "decimal_aligned": False, "orientation": "portrait",
         "note_sentence": ""}

# ============================================================ 3.1: the double-layer schematic
figure(4, 1, "node-link-network", CAP1, "text-layer",
       cited(4, 4, ["Figure 1"], 1,
             lead="The structure of our double-layer complex network is shown in Figure 1."),
       S_31,
       "A drawn schematic rather than a plot: three circles (the regions) each holding blue dots (the "
       "people) joined by thin arrows, an arc drawn across the page separating them from the outside, "
       "two thick yellow arrows labelled 'global network' and 'point-to-point network', and a two-entry "
       "legend at the lower right (open circle = region, blue dot = person). No axes, no numbers, no "
       "scale, no title inside the frame. THE LEGEND KEYS TWO GLYPHS AND NOT THE THREE THAT ARE DRAWN: it "
       "explains the circle and the dot but not the thin black arrows, and gives no key at all for the "
       "thick yellow arrows, whose direction is the whole content of the 'double layer'. THREE REGIONS "
       "ARE DRAWN where the model uses seven, and the arrows inside the circles run in several "
       "directions at once - some inwards, some outwards, one pair facing each other - so the "
       "illustration does not fix a direction of flow. The caption prints BELOW and is the only thing "
       "that names it.",
       geometry("node-link-network", labels=True), "1", section_kind="model")

# ============================================================ 3.2: sender, receiver, content
figure(5, 1, "node-link-network", CAP2, "text-layer",
       cited(5, 5, ["Figure 2"], 1, lead="Figure 2 shows the relationship."),
       S_32,
       "A two-sided diagram: an ellipse on the left holding S1 and S2, an ellipse on the right holding "
       "R1 and R2, and three arrows across the gap labelled C1, C2 and C3 - C1 from S1 to R1, C2 from "
       "S2 to R1 and C3 from S2 to R2. The three entities of the caption (sender, receiver, content) are "
       "drawn in two registers: senders and receivers are circles inside ellipses, while content is only "
       "an arrow label, so the 'three entities' are never the same kind of object on the page. "
       "NOTHING IS QUANTIFIED: no weights, no time axis, no direction of propagation beyond the "
       "arrowheads, and no statement of why one sender reaches one receiver and another reaches two. "
       "The ellipses are unlabelled - neither says which side is sender and which receiver, so the "
       "reading depends entirely on the S and R prefixes. Caption prints BELOW.",
       geometry("node-link-network", labels=True), "2", section_kind="model")

# ============================================================ 3.2.1: the media weights
table(6, 1, S_321,
      "The six media and their AHP weights, printed as TWO SIDE-BY-SIDE BLOCKS of two columns each - "
      "'Medium | Weight' twice - so the physical grid is four columns over three body rows: Newspaper 1, "
      "Telegraphy 0.5, Radio 2 | Television 2.5, Internet 3, Mobile phone 3.5. Ruling is booktabs: a "
      "rule above the header, a rule under it and a rule at the foot, no vertical rules and no rule "
      "between body rows. THE WEIGHTS HAVE NO SCALE AND NO UNIT: they run from 0.5 to 3.5, they are "
      "called 'effect on spreading communication' in the caption and 'weight' in the header, and "
      "nothing states what they are ratios of, whether they are normalised, or how an AHP comparison "
      "produced them; the prose only says the result 'has been approximated in order to simplify "
      "calculation'. 'Telegraphy' is printed as a medium and appears again in every later media table. "
      "Caption prints ABOVE; lead sentence 'The weight of different media is listed in Table 1.'",
      dict(rows=4, cols=4, header_rows=1, merged_cells=False, numeric_cols=2, text_cols=2,
           width="full", continued=False, **BOOKTABS),
      CAPT1, "text-layer",
      cited(6, 6, ["Table 1"], 1, lead="The weight of different media is listed in Table 1."),
      section_kind="model")

# ============================================================ 3.2.1: the content indicators
table(7, 1, S_321,
      "Ten content indicators in two weighted groups: 'Inherent value(0.7)' over five rows "
      "(Authenticity 0.318, Importance 0.174, Timeliness 0.247, Target 0.102, Confidentiality 0.159) "
      "and 'Quality of presentation(0.3)' over five rows (Clear scheme 0.203, Careful thinking 0.063, "
      "Accurate description 0.299, Concise expression 0.232, Comprehensive factors 0.203). THE RULING "
      "IS A CLOSED BOX WITH VERTICAL RULES - outer frame, a vertical rule between each pair of columns "
      "and a rule between every row - which is the other of the two table registers this paper uses, "
      "and the only table here with a merged cell: each group label spans its five rows and is printed "
      "once, so the grid is 3 columns over 11 physical rows. BOTH GROUPS SUM TO 1.000 and the two group "
      "weights sum to 1.0, so the arithmetic is consistent; what is missing is the direction of the "
      "weights - the prose says the ten values 'arrange from 0 to 9' for the indicator scores but never "
      "says the weights are shares of their group. The header cell prints 'General  indicator' with a "
      "double space and a rule fragment where the column rule meets it. Caption prints ABOVE; lead "
      "sentence 'Specific indexes and their weights are shown in Table 2.'",
      dict(rows=11, cols=3, header_rows=1, merged_cells=True, numeric_cols=1, text_cols=2,
           width="full", continued=False, **BOXED),
      CAPT2, "text-layer",
      cited(7, 7, ["Table 2"], 1, lead="Specific indexes and their weights are shown in Table 2."),
      section_kind="model")

# ============================================================ 3.3: the two outer-layer figures
figure(9, 1, "map-or-plan-view", CAP3, "text-layer",
       cited(9, 9, ["Figure 3"], 1,
             lead="we choose GDP per capita as the criteria, with data from the CJDBY.net[9], which is "
                  "shown in Figure 3."),
       S_33,
       "A world choropleth of GDP per capita in six colour bands, with a six-entry key in the lower "
       "left that reads, top to bottom, above 40%, 20%-40%, 10%-20%, 5%-10%, 2.5%-5% and below 2.5% - "
       "percentages of WHAT is never stated, and the top band's label is clipped where the swatch "
       "starts. NO COUNTRY IS LABELLED, there is no title inside the region, no projection note, no "
       "source line and no date for the data. TWO THINGS THE PROSE SAYS ARE NOT ON THE PLATE: it calls "
       "the purple band 'four times as big as the world average' when the key's top band starts at 40% "
       "above, and it names the countries it picks from this map without the map printing any of their "
       "names. The image is a pasted raster whose right edge carries a sliver of a neighbouring graphic, "
       "and one large land mass in the north-east quadrant prints unshaded, outside every band. Caption "
       "prints BELOW.",
       geometry("map-or-plan-view", labels=False), "3", section_kind="model")

figure(9, 2, "node-link-network", CAP4, "text-layer",
       cited(9, 9, ["Figure 4"], 1,
             lead="we choose seven typical countries in Figure 4"),
       S_33,
       "A political world map with seven red stars and eight straight yellow lines joining them, one per "
       "chosen country (America, Brazil, France, Congo, Russia, China, Austria per the prose). THE "
       "OVERLAY CARRIES NO INFORMATION BEYOND CONNECTEDNESS: the lines have no arrowheads so the flow is "
       "undirected, no thickness, no label and no weight; the stars are identical for all seven; and "
       "there is no legend anywhere on the plate, so nothing says what the lines mean. The lines are "
       "drawn straight across the oceans with no great-circle form and several cross each other, which "
       "makes the graph read as a complete mesh rather than the region-to-region flow the section is "
       "about. The basemap is a stock political map with country names baked in at several sizes, so the "
       "figure's legible text is the basemap's, not the paper's. Caption prints BELOW and sits alongside "
       "Figure 3's under the pair.",
       geometry("node-link-network", labels=True), "4", section_kind="model", order=2)

# ============================================================ 3.3: the rho-theta construction
figure(10, 1, "flowchart-or-schematic", CAP5, "text-layer",
       cited(10, 10, ["Figure 5"], 1, lead="as shown in Figure 5."),
       S_33,
       "A construction diagram, not a data plot: eight black arrows radiating from a common centre, a "
       "circle of radius rho drawn around it, the angle theta marked between the horizontal axis and one "
       "ray, and three dots on that ray labelled with the partial derivative df/drho. No axes, no "
       "numbers, no scale, no legend, no title inside the region. IT IS A FIGURE OF A FORMULA AND "
       "PRINTS ONE: the only text is the rho, the theta and the df/drho, and the caption 'A point source "
       "flow' does not say that the object is illustrating the gradient of a scalar field taken in polar "
       "coordinates. The eight arrows are equal in length and evenly spaced although the text that "
       "follows immediately infers that the tangential component vanishes and the radial one does not, "
       "which the drawing cannot show because no ray is distinguished except the labelled one. THE "
       "NUMBER FIVE IS USED TWICE IN THIS PAPER - this plate and the p12 'Original network' are both "
       "captioned Figure 5. Caption prints BELOW.",
       geometry("flowchart-or-schematic", labels=True), "5", section_kind="model")

# ============================================================ 3.4: the two spread networks
figure(12, 1, "node-link-network", CAP6, "text-layer",
       cited(12, 12, ["Figure 6"], 1,
             lead="Through the spread of information, as shown in Figure 6, the number of blue spots "
                  "increases"),
       S_34,
       "The spread network after one round: about twenty circular nodes joined by thin directed arrows, "
       "six of them filled solid blue and the rest open white, with SIXTEEN EDGE VALUES PRINTED as bare "
       "decimals - 0.37, 0.45, 0.13, 0.61, 0.78, 0.74, 0.26, 0.32, 0.93, 0.79, 0.88, 0.67, 0.6, 0.73, "
       "0.63, 0.84 - and no node label, index or name anywhere. THE NUMBERS HAVE NO STATED MEANING: the "
       "text that reads the pair never mentions them, and nothing says whether they are a spreading "
       "probability, an index value or an edge weight; one is printed to one decimal (0.6) beside "
       "fifteen printed to two. The fact the prose actually reads off the figure - how many blue spots "
       "there are - is not printed and can only be counted, and the count on the plate is six where the "
       "panel beside it starts from one. Several arrows run between nodes at the frame edge and one long "
       "line crosses the middle of the graph with its arrowhead in the middle rather than at an end. No "
       "axes, no legend, no scale. Caption prints BELOW; it prints BEFORE the citing sentence, which "
       "refers to 'Figure 5 and 6' jointly.",
       geometry("node-link-network", labels=True, numbers=True), "6", section_kind="model")

figure(12, 2, "node-link-network", CAP5b, "text-layer",
       cited(12, 12, ["Figure 5"], 1,
             lead="As shown in the Figure 5,there is only one node in the beginning which is information "
                  "source."),
       S_34,
       "The seed state of the same network: one blue node at the centre, eight arrows leaving it to "
       "eight open circles, each arrow labelled with a bare decimal (0.91, 0.73, 0.32, 0.81, 0.43, 0.63, "
       "0.26) and one more unlabelled-looking edge, with a further dozen open circles scattered around "
       "the frame carrying NO EDGES AT ALL. The labels are placed along the arrows without a leader and "
       "one of them (0.26) sits on the far side of its arrowhead, so which arrow a value belongs to is a "
       "guess where labels are close. NOTHING SAYS WHAT THE EIGHT VALUES ARE, and the count of edges "
       "does not match the eight values printed - one arrow carries no visible number. The nodes have no "
       "identities, so the figure cannot be checked against the network it claims to seed. THIS IS THE "
       "SECOND PLATE CAPTIONED FIGURE 5, after the p10 point-source diagram; the two are different "
       "drawings with different captions and the same number. Caption prints BELOW.",
       geometry("node-link-network", labels=True, numbers=True), "5", section_kind="model")

# ============================================================ 3.5.1: the two sensitivity pairs
figure(12, 3, "line", CAP7, "text-layer",
       cited(12, 12, ["Figure 7"], 1,
             lead="Figure 7 and Figure 8 show the sensitivity analysis of willing degree of receiver"),
       S_351,
       "Three curves of a 'ratio' against 'year' from 1980 to 2014, legend inside the upper right with "
       "a dashed green '0.9W', a solid blue 'W' and a dashed red '1.1W'; y ticks 0.0 to 0.7 in steps of "
       "0.1 and x ticks every two years rotated 45 degrees. All three are indistinguishable at about 0.05 "
       "until 1996 and then separate on an accelerating bend, reaching roughly 0.24, 0.46 and 0.66 by "
       "2014, so the index is only influential in the last third of the span. NO DATA POINTS ARE PLOTTED "
       "and no gridlines or uncertainty bands are drawn, so the curves read as model output with no "
       "observations to check them against; the y axis is titled 'ratio' with no statement of what is "
       "being ratioed. THE CITING SENTENCE MISNUMBERS IT: 'It is obvious that the total trend of three "
       "lines in Figure 13 is all rising' while it is reading this plate - Figure 13 is the Internet "
       "market share on p15. Caption prints BELOW, in the same line as Figure 8's caption, and both "
       "figures print BEFORE the sentences that read them.",
       geometry("line", legend="inside", labels=True), "7", section_kind="sensitivity")

figure(12, 4, "line", CAP8, "text-layer",
       cited(12, 12, ["Figure 8"], 1,
             lead="Figure 7 and Figure 8 show the sensitivity analysis of willing degree of receiver"),
       S_351,
       "The same construction for the interest-similarity index: dashed green '0.9Si', solid blue 'Si' "
       "and dashed red '1.1Si' over 1980 to 2014 on the same axes (ratio 0.0 to 0.7, years every two, "
       "rotated). The separation is much smaller than in the W pair - roughly 0.41, 0.45 and 0.50 at "
       "2014 against 0.24, 0.46 and 0.66 - which is the paper's point, that the model is less sensitive "
       "to similarity than to willingness, and the plates do carry it. WHAT THE PAIR DOES NOT DO IS PUT "
       "THE COMPARISON ON ONE AXIS: the two curves are printed as two figures with identical axes and "
       "identical legends and the reader has to hold one in memory against the other, and neither plate "
       "prints the spread at any year. Caption prints BELOW beside Figure 7's.",
       geometry("line", legend="inside", labels=True), "8", section_kind="sensitivity", order=2)

# ============================================================ 3.5.2: the removal test
figure(13, 1, "bar", CAP9, "text-layer",
       cited(13, 13, ["Figure 9"], 1,
             lead="Figure 9 shows the different propagation delay (when the propagation ratio reaches "
                  "10%)"),
       S_352,
       "Five vertical bars of 'Propagation delay time', one per scenario, on the categories normal, lack "
       "F, lack A, lack Ac and lack W, with the value PRINTED ABOVE EACH BAR: 58, 62, 53, 54 and 61. The "
       "bars are filled in five different colours - cyan, orange, red, green, blue - WITH NO LEGEND, so "
       "the colour carries nothing and five hues are spent on five categories already named on the axis. "
       "THE SCALE TRUNCATES THE DIFFERENCES: the ordinate is labelled only 0, 40 and 60 (with 20 on the "
       "tick and no label at the top), so a spread of 53 to 62 is drawn as bars that differ by less than "
       "a fifth of the visible height and by 13% of their own value, and there are no error bars or "
       "replicates to say whether that is signal. The prose then ranks the sensitivities - 'model is "
       "most sensitive to authority, later comes influence, Activity and Willing' - from a chart whose "
       "Activity bar (54) moves further from normal than its Willing bar (61 against 58). Caption prints "
       "BELOW.",
       geometry("bar", labels=True, numbers=True), "9", section_kind="sensitivity")

# ============================================================ 4.2: the media market shares
figure(14, 1, "line", CAP10, "text-layer",
       uncited(),
       S_42,
       "Six media-share series for America against year, legend inside the upper right keyed by colour "
       "only (black newspaper, red telegraph, blue radio, magenta television, green internet, navy "
       "phone), y axis titled 'ratio' and ticked from -0.1 to 1.0, x ticks every ten years from 1850 and "
       "rotated. The shapes are plausible - newspaper decays from about 0.84 near 1870 to 0.05 by 2010, "
       "telegraph peaks around 1920 and dies, radio peaks near 0.42 in 1980, television climbs to 0.32 - "
       "but THE AXIS RUNS INTO NEGATIVE SHARE: a quantity that cannot go below zero is printed down to "
       "-0.1, and the Internet and phone series appear only as short fragments after 1995, so two of the "
       "six are drawn without a beginning. No gridlines, no markers, no observation count, no source "
       "note on the plate. NO SENTENCE IN THE PAPER NAMES FIGURE 10: the text introduces 'the total trend "
       "in market share of six media plots as follows' and the plates print without being called by "
       "number anywhere. Caption prints BELOW.",
       geometry("line", legend="inside", labels=True), "10", section_kind="result")

figure(14, 2, "line", CAP11, "text-layer",
       uncited(),
       S_42,
       "The same six-series construction for China, same colour key, same 'ratio' ordinate from -0.1 to "
       "1.0, years from 1880. The shapes are markedly different from the American panel: telegraph "
       "starts at 1.0 in 1890 and collapses to 0.15 by 1950, newspaper runs near 0.20 to 0.35 mid-century "
       "before declining, radio peaks near 0.39 around 1960, television climbs to 0.31, and the Internet "
       "and phone are again late fragments. THE PAIR IS READ FROM ONE SENTENCE THAT NEVER NAMES EITHER "
       "PLATE, and the two panels share their axis ranges but not their start years (1850 against 1880), "
       "so corresponding moments do not line up when the plates are compared side by side. No source, no "
       "gridlines, no markers. Caption prints BELOW.",
       geometry("line", legend="inside", labels=True), "11", section_kind="result", order=2)

table(14, 3, S_42,
      "America's six market shares printed as ONE DATA ROW under a six-way stub: the header row reads "
      "Medium | Newspaper | Telegraph | Radio | Television | Internet | Phone and the single row is "
      "labelled 'Weigh' - the word 'Weight' clipped by the column width, reprinted on the next table too "
      "- with the values 0.09, 0.01, 0.04, 0.32, 0.27 and 0.27, which sum to 1.00. Ruling is booktabs "
      "with no vertical rules. MULTIPLE DEFECTS IN FOUR LINES: the row is called a weight while the "
      "column header calls the same numbers market shares and the prose calls them a forecast; the six "
      "values carry no unit and no date, so Table 3 does not say WHICH YEAR's shares these are although "
      "the section is about today and the plate beside it runs to 2010; and the six media are repeated "
      "in a second spelling system from Table 1's ('Phone' here against 'Mobile phone' there). Caption "
      "prints ABOVE; lead sentence 'The specific value of market share of different media is listed in "
      "Table 3 and Table 4.'",
      dict(rows=2, cols=7, header_rows=1, merged_cells=False, numeric_cols=6, text_cols=1,
           width="full", continued=False, **BOOKTABS),
      CAPT3, "text-layer",
      cited(14, 14, ["Table 3"], 1,
            lead="The specific value of market share of different media is listed in Table 3 and Table "
                 "4."),
      section_kind="result")

table(14, 4, S_42,
      "China's six market shares in the identical shape - header Medium | Newspaper | Telegraph | Radio "
      "| Television | Internet | Phone, one row labelled 'Weigh', values 0.12, 0.02, 0.07, 0.29, 0.25 "
      "and 0.25, summing to 1.00 - with the same booktabs ruling. The two tables therefore print the "
      "same six media for two countries and NO OTHER ROW, so the only data in the section is twelve "
      "numbers with no year, no source and no uncertainty. Caption prints ABOVE and no sentence beyond "
      "the joint one names this table separately.",
      dict(rows=2, cols=7, header_rows=1, merged_cells=False, numeric_cols=6, text_cols=1,
           width="full", continued=False, **BOOKTABS),
      CAPT4, "text-layer",
      cited(14, 14, ["Table 4"], 1,
            lead="The specific value of market share of different media is listed in Table 3 and Table "
                 "4."),
      section_kind="result", order=2)

# ============================================================ 4.2: the two market-share curves
figure(15, 1, "line", CAP12, "text-layer",
       cited(15, 15, ["Figure 12"], 1,
             lead="Figure 12 shows the market share of newspaper while Figure 13 shows the one of the"),
       S_42,
       "Newspaper market share against year, one axis, with a blue solid actual series and a green "
       "dashed forecast branch after the last observation - no legend on the plate, so the dashed/solid "
       "convention is only explained in the prose. The actual series falls from about 0.59 at 1995 to "
       "0.30 at 2015 across FIVE POINTS, and the forecast branch falls to about 0.27. Only the left and "
       "bottom spines are drawn, with no gridlines and no markers other than the vertices; the ordinate "
       "is titled nothing at all and the abscissa 'years', plural, where its sibling on the next plate "
       "prints 'year'. Caption prints BELOW.",
       geometry("line", labels=True), "12", section_kind="result")

figure(15, 2, "line", CAP13, "text-layer",
       cited(15, 15, ["Figure 13"], 1,
             lead="Figure 12 shows the market share of newspaper while Figure 13 shows the one of the"),
       S_42,
       "Internet market share against year with the same solid-actual and dashed-forecast convention and "
       "again no legend: four observed points from about 0.704 in 2011 to 0.773 in 2015 and a forecast "
       "branch to about 0.787. THE PAIR IS DRAWN ON INCOMPARABLE SCALES: the newspaper plate spans 0.25 "
       "to 0.65 and this one 0.70 to 0.78, so an 0.08 range is expanded to fill the frame and the flat "
       "line the prose reads as agreement with reality is an artefact of the zoom. Both plates plot only "
       "five years of data, and the sentence that reads them claims 'the green line is close to the blue "
       "one, with the relative error is under 10%' - true of the two numbers in Table 5, but the plates "
       "print no error, no axis title and no units. Caption prints BELOW.",
       geometry("line", labels=True), "13", section_kind="result", order=2)

table(15, 3, S_42,
      "The error audit, and the thinnest table in the paper: header Medium | True value | Forecast | "
      "Absolute Error | Relative Error over TWO rows - Newspaper 0.3, 0.28, 0.02, 6.67% and Internet "
      "0.773, 0.785, 0.12, 1.55% - though the caption promises 'Different Media' and the section's own "
      "figures print six. THE INTERNET ROW'S ARITHMETIC IS WRONG IN ONE CELL: 0.773 against a forecast "
      "of 0.785 is an absolute error of 0.012, not the 0.12 printed, and the 1.55% beside it is the "
      "correct relative error for 0.012 - so the absolute-error cell is out by a factor of ten while its "
      "neighbours are right. THE TRUE VALUES CONTRADICT TABLE 3 ON THE PREVIOUS PAGE, which gives "
      "America a newspaper share of 0.09 and an Internet share of 0.27 against 0.3 and 0.773 here, with "
      "no year stated in either table to explain the difference. Ruling is booktabs, caption ABOVE. "
      "Cited once, 'The specific error is shown in Table 5.'",
      dict(rows=3, cols=5, header_rows=1, merged_cells=False, numeric_cols=4, text_cols=1,
           width="half", continued=False, **BOOKTABS),
      CAPT5, "text-layer",
      cited(15, 15, ["Table 5"], 1, lead="The specific error is shown in Table 5."),
      section_kind="result")

figure(15, 4, "node-link-network", CAP14, "text-layer",
       uncited(),
       S_42,
       "The spread network of the worked example: several hundred small filled circles in six or seven "
       "colours joined by thin edges, with one orange-red hub near the centre connected by long straight "
       "spokes to much of the periphery. NO AXES, NO TICK, NO SCALE, NO LEGEND AND NO DIRECTION ON ANY "
       "EDGE: the colour families cluster on the left and right of the plate, which suggests communities "
       "of some kind, but the colours are keyed nowhere, so the clustering is unreadable as evidence. No "
       "node or edge is labelled, and the caption's 'Information Spread Network' gives no time, no round "
       "and no node count - the count the prose draws from this example (89 nodes against a reported 80 "
       "retweets) is not printed on the plate and cannot be checked from it. NO SENTENCE NAMES FIGURE "
       "14; the text says only 'Following are our results.' Caption prints BELOW.",
       geometry("node-link-network"), "14", section_kind="result")

# ============================================================ 4.3: capacities and ratios
figure(16, 1, "line", CAP15, "text-layer",
       cited(16, 16, ["Figure 15"], 1, lead="Figure 15 shows the ratio changes in America."),
       S_431,
       "One thin curve of 'ratio' against 'year', 1860 to 2060 on the abscissa (ticks every ten years, "
       "rotated) and 0 to 100 on the ordinate, sliding from about 100 near 1900 to about 10 by the "
       "2050s. THE PLATE DOES NOT SEPARATE WHAT WAS MEASURED FROM WHAT WAS MODELLED: the same stroke "
       "carries history and projection, the x axis runs past the last plotted point into empty space, "
       "and there is no marker, no shaded region, no note and no legend saying where the model starts - "
       "the prose says the ratio 'will reach approximately the number of 14 around the year 2050' while "
       "the curve has already reached about 10. The curve also carries small sawtooth notches at about "
       "1915, 1965 and 1985, i.e. the series is stitched from sources and the seams are visible as "
       "discontinuities in an otherwise smooth decay. Only two spines, no gridlines, no y units. Caption "
       "prints BELOW.",
       geometry("line", labels=True), "15", section_kind="result")

figure(16, 2, "line", CAP16, "text-layer",
       cited(16, 16, ["Figure 16"], 1,
             lead="In the same way, Figure 16 shows trend of ratio changes in Congo"),
       S_431,
       "The same construction for Congo: 'ratio' against 'year' from 1890 to 2060, ordinate from 40 to "
       "160 with its lowest tick at 40. The curve starts near 158 around 1900, dips to about 138 by 1920, "
       "peaks again near 147 in 1970 and falls to about 35 by 2050. THE ORDINATE IS TRUNCATED AND THE "
       "CURVE LEAVES IT: the axis is labelled from 40 up and the plotted minimum near 35 falls below the "
       "lowest label, so the final descent is drawn against an axis that has run out. THE PAIR'S TWO "
       "PLATES ARE ON DIFFERENT SCALES - 0 to 100 against 40 to 160 - for the same quantity under the "
       "same caption pattern, so the two curves cannot be compared by height, and the paper's own "
       "sentence misreads its direction: it says Congo 'will reach the number of 30 ... which is lower "
       "than the one of America' although the American plate ends near 10 to 14, so Congo ends higher, "
       "not lower. Caption prints BELOW.",
       geometry("line", labels=True), "16", section_kind="result", order=2)

figure(17, 1, "line", CAP17, "text-layer",
       cited(17, 17, ["Figure 17"], 1,
             lead="Figure 17 plots the variation trend for these two indicators of America."),
       S_432,
       "Two curves on one pair of axes over 1840 to 2040: a black 'propagation probability' rising from "
       "about 0.03 near 1860 to about 0.69 by 2045 and a red 'propagation delay' falling from about 0.95 "
       "to about 0.04, crossing near 0.42 in about 2015. The legend is inside the upper right and the "
       "only legible text besides it is the axis ticks; the ordinate has NO TITLE AT ALL. TWO "
       "DIMENSIONALLY DIFFERENT QUANTITIES ARE PLOTTED ON ONE UNLABELLED 0-TO-1.2 SCALE: a probability "
       "and a delay time share an axis with no unit, so the crossing at 2015 is a crossing of "
       "incommensurables and means nothing; the axis is also drawn down to -0.2, which a probability "
       "cannot take. The prose reads two 'time points' off the plate - 1870 and 2000 - as the moments "
       "newspaper and the Internet arrived, which are not marked on it. Caption prints BELOW.",
       geometry("line", legend="inside", labels=True), "17", section_kind="result")

figure(17, 2, "line", CAP18, "text-layer",
       cited(17, 17, ["Figure 18"], 1,
             lead="Figure 18 indicates the capacities in Congo changes in the same way."),
       S_432,
       "Congo's pair on the same axes and the same legend: red delay starts near 1.03 around 1885, holds "
       "a shoulder down to about 0.77 by 1940, plateaus to 1990 and then drops to about 0.55 by 2045; "
       "black probability rises gently from about 0.09 to about 0.47. THE TWO CURVES NEVER CROSS HERE, "
       "where the American pair crosses in 2015 - which is a real difference between the countries and "
       "the paper does not mention it, reading the plate only as 'changes in the same way'. Same "
       "defects: no ordinate title, an axis to -0.2 for a probability, no gridlines, and the plate runs "
       "to 2040 past the last datum. Caption prints BELOW.",
       geometry("line", legend="inside", labels=True), "18", section_kind="result", order=2)

# ============================================================ 4.4: public opinion
figure(18, 1, "line", CAP19, "text-layer",
       uncited(),
       S_441,
       "One blue series of 'public opinion' against 'time (h)', ordinate ticked 0.40 to 0.90 in steps of "
       "0.05 and abscissa 0.0 to 5.0 in steps of 0.5, box open on top and right: the curve opens at about "
       "0.53, dips, PEAKS AT ABOUT 0.90 NEAR t = 1.2, then falls to about 0.63 by t = 2.0 and settles "
       "into a shrinking oscillation around 0.65. THREE HORIZONTAL REFERENCE RULES CROSS THE PLOT WITH NO "
       "LEGEND AND NO LABEL - a solid red line near 0.645 and two black dash-dot lines near 0.70 and "
       "0.625 - so the band the prose calls a convergence value is drawn three times in two colours with "
       "nothing saying which is the target, which is the bound or what the third is. No gridlines, no "
       "minor ticks, no plotted markers. THE PROSE READS THE OPENING AS NEUTRAL AND THE PLATE SHOWS A "
       "TRANSIENT TO 0.90: the oscillation peaks nine tenths of the way up a 0.40-to-0.90 axis before "
       "settling, which the sentences about 'extreme' early change do not quantify. NO SENTENCE NAMES IT "
       "BY NUMBER: the text says only 'The trend for he public interest and opinion o change is shown as "
       "follows:' and the plate follows. Caption prints BELOW.",
       geometry("line", labels=True), "19", section_kind="result")

# ============================================================ 4.5: the factor sweeps
figure(19, 1, "line", CAP20, "text-layer",
       cited(19, 19, ["Figure 20"], 1,
             lead="Figure 20 and 21 show these two indicators"),
       S_451,
       "Propagation probability against 'information value' 0 to 9, two curves, legend INSIDE the upper "
       "right keyed black 'America' and red 'China'. Both rise monotonically and upward-convex from 0 at "
       "the origin, America ending near 0.60 and China near 0.55, so the prose's 'China is lower than "
       "America' is what the plate shows. THE ORDINATE HAS NO TITLE AND NO UNIT although it is ticked "
       "0.0 to 0.9; the curves are smooth approximations WITH NO PLOTTED DATA POINTS, no markers, no "
       "gridlines, and no minor ticks. The region's crop carries the tail of a body-text line ('...icators' "
       "change trend with time.') in its top strip, i.e. the measured box overlaps the prose above it. "
       "THE PAIR'S LEGEND ORDER IS REVERSED on the next plate (here black America then red China, there "
       "black China then red America), so a reader comparing the two panels has to re-read the key each "
       "time. Caption prints BELOW, above the sentence that reads the pair.",
       geometry("line", legend="inside", labels=True), "20", section_kind="result")

figure(19, 2, "line", CAP21, "text-layer",
       cited(19, 19, ["Figure 21"], 1,
             lead="Figure 20 and 21 show these two indicators"),
       S_451,
       "The companion sweep: propagation delay against the same 0-to-9 'information value' on an ordinate "
       "ticked 0.0 to 1.0, two curves falling monotonically - black 'China' from about 0.97 to about 0.30 "
       "and red 'America' from about 0.88 to about 0.24 - so China's delay stays ABOVE America's "
       "throughout, which is the mirror of Figure 20 and what the prose reads. THE LEGEND IS PRINTED IN "
       "THE OPPOSITE ORDER TO FIGURE 20'S (China first here, America first there) with the same two "
       "colours, so the two plates cannot be read with one key. The decay is roughly sigmoidal rather "
       "than the smooth convex rise of its partner, so the pair plots two different function shapes on "
       "axes that are separate on both plates. The ordinate again has NO TITLE AND NO UNIT. No markers, "
       "no gridlines, no annotated values, box open on top and right. NO NUMBERS ARE PRINTED BEYOND THE "
       "TICKS, so the prose's 'higher' and 'lower' claims are unquantified. Caption prints BELOW.",
       geometry("line", legend="inside", labels=True), "21", section_kind="result", order=2)

figure(20, 1, "line", CAP22, "text-layer",
       cited(19, 20, ["Figure 22"], 1,
             lead="Figure 22 shows the change of its value over time."),
       S_452,
       "'change rate' against 'information value' 0 to 9, two curves, legend inside the upper right keyed "
       "black 'China' and red 'America'. Both rise upward-convex; America runs above China across the "
       "whole range (about 0.15 to 0.54 against 0.05 to 0.49) and the gap narrows from roughly 0.10 at "
       "the origin to near-convergence at the right, so the prose's claim that America's change rate "
       "exceeds China's does hold. THE CURVES ARE DRAWN AS VISIBLY SEGMENTED PIECEWISE LINES rather than "
       "fitted strokes, unlike the smooth curves of Figures 20 and 21, so the trio is inconsistent in how "
       "its model output is rendered; and the ordinate spine stops at 0.7 with the frame left open above "
       "the plotted curves. No gridlines, no markers, no annotated values. Named on the PREVIOUS page - "
       "the citing sentence closes section 4.5.1 and the plate opens the next page. Caption prints BELOW.",
       geometry("line", legend="inside", labels=True), "22", section_kind="result")

RULES = [
    "Measure first, then read the pixels: twenty-eight measured regions resolve into twenty-three "
    "figure rows and five table rows, with no refusal and nothing unaccounted [place.doc_order].",
    "A figure number can be used twice: p10's point-source diagram and p12's original network are both "
    "captioned Figure 5, and p12's citing sentence names 'Figure 5' without saying which one it means "
    "[caption.verbatim].",
    "A citing sentence can name the wrong figure: p12 reads the sensitivity plate of Figure 7 as "
    "'three lines in Figure 13', and p16 credits the capacity plates of Figures 17 and 18 to 'Figure 11 "
    "and 12' [mention.lead_sentence].",
    "A pair of plates can be drawn on incompatible scales: Figures 12 and 13 use 0.25-0.65 and 0.70-0.78 "
    "for the same quantity, and Figures 15 and 16 use 0-100 and 40-160 [geometry.shared_axes].",
    "An axis can be drawn through a value the quantity cannot take: the media-share plates run to -0.1 "
    "and the capacity plates to -0.2, on ratios and on a probability [geometry.family].",
    "Two dimensionally different quantities can share one untitled axis: Figures 17 and 18 plot a "
    "probability and a delay on a 0-to-1.2 scale with no ordinate title [geometry.legend].",
    "A legend can be reordered for no reason between two companion plates: Figure 20 keys black America "
    "then red China and Figure 21 keys black China then red America in the same two colours "
    "[geometry.legend].",
    "A reference line can be drawn three times without a key: Figure 19 carries a solid red rule and two "
    "black dash-dot rules across the plot with no legend naming any of them [geometry.legend].",
    "Printed numbers can be unlabelled: Figures 5b and 6 print 24 edge values with no statement of what "
    "they are, and Figure 9 prints five bar values in five colours with no legend [geometry.printed_numbers].",
    "A table can contradict a table: Table 5's true values for newspaper and the Internet (0.3, 0.773) "
    "are not Table 3's market shares for the same country (0.09, 0.27) [table.numeric_cols].",
    "A printed cell can be a decimal slip: Table 5's Internet absolute error reads 0.12 where 0.773 "
    "against 0.785 gives 0.012, and the 1.55% beside it is computed from the correct value "
    "[table.header_rows].",
    "Four of twenty-three figure rows are named by no sentence at all - Figures 10, 11, 14 and 19, the "
    "media-share pair, the spread network and the public-opinion curve - and most of the rest are named "
    "by a sentence that prints after the plate [mention.count].",
]

NOTE = """\
Paper 103, Team 42220: information flow as a double-layer complex network. Six media are weighted by
AHP, ten content indicators are weighted in two groups, sender/receiver/similarity indexes give a
propagation probability, and five tasks follow - qualifying news, predicting today's media shares,
projecting to 2050, following public opinion, and sweeping factors. Twenty-one pages, twenty-eight
measured regions over fifteen of them, resolving into TWENTY-THREE FIGURE ROWS and FIVE TABLE ROWS,
with no refusal and nothing unaccounted.

The count of exhibits is not the count of numbers: the paper prints Figures 1 to 22 and Tables 1 to 5,
but the number five is used twice - p10's 'Figure 5 A point source flow' and p12's 'Figure 5 Original
network' - so twenty-three plates carry twenty-three captions and one repeated number, and the p12
sentence that reads the pair says only 'Figure 5 and 6'.

The two table registers are both present and never mix. Tables 1, 3, 4 and 5 are booktabs - a rule
above the header, a rule under it and a rule at the foot, no verticals. Table 2 alone is a closed box
with vertical rules and rules between every row, and it is the only table with merged cells, its two
group labels (Inherent value 0.7, Quality of presentation 0.3) each spanning five rows. Table 1 and
Table 2 both use the side-by-side-block shape for a two-column list: Table 1 is four physical columns
of 'Medium | Weight' over three rows; Table 2 is three columns over eleven rows.

Table 5 is the paper's error audit and it does not hold: the Internet's absolute error prints 0.12
where 0.773 against 0.785 gives 0.012, while the 1.55% beside it is right; the caption promises
'different media' and two are printed; and its true values for newspaper and the Internet (0.3, 0.773)
contradict Table 3's market shares for America (0.09, 0.27) with no year in either table.

The plates are six kinds of thing and mostly pairs. Figures 1, 2, 5b, 6 and 14 are networks: the
double-layer schematic, the sender/receiver diagram, the seed graph (one blue hub, eight labelled
edges), the spread graph (about twenty nodes, sixteen printed decimals) and the Bin Laden example (a
dense colour-coded radial graph with no legend at all). Figures 5 and 5b both print edge values as bare
decimals and nothing in either the plates or the prose says what the numbers are. Figure 3 is a
six-band world choropleth with no country labels and a key whose percentages are relative to nothing
stated; Figure 4 draws the seven chosen countries as a mesh of straight lines on a political map with
no arrowheads, no legend and no weights.

Figures 7 and 8 are the sensitivity pair - three curves each, legend inside - and the prose misnumbers
one of them as Figure 13. Figure 9 is a five-bar chart whose values sit between 53 and 62 on an axis
labelled 0, 40, 60, drawn in five colours with no legend, and the paper's ranking of the four indexes
disagrees with its own bars for Activity against Willing. Figures 10 and 11 are six-series media-share
profiles for America and China with the ordinate taken to -0.1 and two series existing only as late
fragments; neither is named by any sentence. Figures 12 and 13 are the newspaper and Internet forecasts,
drawn on 0.25-0.65 and 0.70-0.78 for the same quantity, each with five observations and an unlabelled
dashed forecast branch. Figures 15 and 16 are the ratio s for America and Congo on 0 to 100 and 40 to
160, and the paper reads Congo's ending as 'lower' when the plates put it near 35 against America's 10
to 14. Figures 17 and 18 put a probability and a delay on one untitled 0-to-1.2 axis; they cross in
2015 in America and never cross in Congo, a difference the text passes over. Figures 19 to 22 are four
ungarnished single-series time plots with no axis titles, no markers and no numbers.

Families: line 14 (Figures 7, 8, 10, 11, 12, 13, 15 to 22), node-link-network 6 (Figures 1, 2, 4,
5b, 6, 14), table-grid 5, bar 1 (Figure 9), map-or-plan-view 1 (Figure 3), flowchart-or-schematic 1
(Figure 5).
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

out = PROXY / "pc103-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
