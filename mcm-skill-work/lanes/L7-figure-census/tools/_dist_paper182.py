"""Hand census of P-E-2019-1902917-3fb00373 (Team 1902917, 24 pages, 16 measured regions).

An ecological-cost paper for problem E 2019: a short-run cost-benefit model built on replacement cost,
a long-run model built on AHP weighting and scoring, a paper-mill case for the short run, the Tennessee
Valley thermal power project for the long run, and a sensitivity study of the AHP weights. Sixteen
measured regions over eleven of twenty-four pages resolve into NINE FIGURE ROWS and THREE TABLE ROWS,
with four regions refused and nothing unaccounted.

  p4     -   Table 1     table-grid           caption only; the grid itself begins on p5
  p5  r1  Table 1     table-grid            sixteen notation rows, symbol | definition | unit
  p6  r1  Figure 1    flowchart-or-schematic   short run cost, nine boxes in four ranks
  p7  r1  Figure 2    flowchart-or-schematic   short run benefit, four boxes in three ranks
  p11 r1  Table 2     table-grid            ranking standards, seven columns, five bands
  p12 r1         -   EXCLUDED             rows 4 and 5 of Table 2, no repeated header
  p12 r2  Figure 3    flowchart-or-schematic   long run cost, eight boxes in three ranks
  p16 r1  Table 3     table-grid            the variation values scored against Table 2
  p18 r1  Figure 4    line                 MATLAB sensitivity plot, two affine strokes
  p21 r1         -   EXCLUDED             a reference-list text block
  p22 r1         -   map-or-plan-view     pasted Tennessee Valley map, no figure number
  p22 r2         -   table-as-figure      scanned Chinese construction-cost table
  p23 r1         -   EXCLUDED             running header
  p23 r2         -   table-as-figure      the cost table's last three plants, no header
  p23 r3         -   table-as-figure      scanned Chinese revenue table, 1947-1957
  p23 r4         -   table-as-figure      the revenue table continued, 1966-1958
  p24 r1         -   EXCLUDED             running header

The appendix's five exhibits have no figure numbers at all; they are screenshots of a printed Chinese
textbook pasted into the paper's own appendix, and the page furniture around them (running headers,
a bibliography block) is measured as regions by the layout pass, so four rows of the census are refusals
rather than exhibits. The MATLAB listing the paper introduces as "These are Matlab codes" is LIVE TEXT
on pp23-24, not a measured region, so it is not censused.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-E-2019-1902917-3fb00373"
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


S_3 = [head(4, "3 Symbol Description")]
S_411 = [head(5, "4.1.1 Cost Analysis")]
S_412 = [head(6, "4.1.2 Benefit Analysis")]
S_421 = [head(7, "4.2.1 Cost Analysis")]
S_4R = [head(11, "4 Ranking standards evaluation of indexes")]
S_2C = [head(16, "2 Calculation")]
S_6 = [head(17, "6 Sensitivity Analysis")]
S_APP = [printed(22, "Appendices")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_KNOWN |= schema.printed_lines(PID)
for _group in (S_3, S_411, S_412, S_421, S_4R, S_2C, S_6, S_APP):
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


CAPT1 = caption("Table 1: Notations", kind="Table", position="above")
CAP1 = caption("Figure 1：Schematic Diagram of Short Run Cost")
CAP2 = caption("Figure 2：Schematic Diagram of Short Run Benefit")
CAPT2 = caption("Table2: Ranking standards and scores of values’ changes of different indexes",
                kind="Table", position="above")
CAP3 = caption("Figure 3：Schematic Diagram of Long Run Cost")
CAPT3 = caption("Table3: The ranks and scores of values’ changes of different indexes according "
                "to Tab.2", kind="Table", position="above")
CAP4 = caption("Figure 4：Sensitivity analysis of weights of the indicators")
CAPP1 = caption("May 2005 map of TVA sites", position="below")
CAPP2 = caption("表 3-2 TWA 火力发电厂的建设成本表", position="above")

BOOKTABS = {"rule_style": "booktabs", "zebra": False, "diagonal_header": False,
            "units_in_header": False, "decimal_aligned": False, "orientation": "portrait",
            "note_sentence": ""}
BOOKTABS_UNITS = dict(BOOKTABS, units_in_header=True)
GRIDRULES = dict(BOOKTABS, rule_style="vertical-rules")

# ============================================================ 3: the notation grid
table(5, 1, S_3,
      "Sixteen body rows in three columns - symbol | definition | unit - ruled booktabs with no "
      "verticals, a rule above the first row and a rule at the foot, and NO COLUMN HEADS INSIDE THE "
      "REGION: the header line 'Symbols Definition Unit' is printed at the very foot of p4, under the "
      "caption, and the grid only begins on p5, so the exhibit's measured area carries neither its own "
      "caption nor its own header. THE SYMBOL COLUMN IS SET TWO WAYS: C_S, C_L, PC and EC print as two "
      "italic capitals with a subscript letter, while every later entry is italic with a letter "
      "subscript (LP_S, LP_W, LP_A, P_S, P_W, P_A, C_RS, C_RW, C_RA) - and the body of the paper then "
      "writes the same four headline quantities in roman capitals with no subscript at all ('CS = PC + "
      "EC', 'EC = f(P-LP)'), so a reader matching table to text has to translate. THE UNIT COLUMN "
      "MIXES THREE DIMENSIONS: currency for the four cost symbols ($), land area for the soil entries "
      "(m2) and volume for the water and air entries (m3), with the compound replacement rates in $/m2 "
      "and $/m3. TWO AMOUNTS ARE PRINTED WITH NO UNIT AT ALL - P, 'The amount of pollution generated by "
      "businesses', and LP, 'The amount of pollution which can be controlled by self-purification "
      "capability of nature' - although both are subtracted from the matching P_S, P_W and P_A in the "
      "model's own formula, P_S and LP_S being in m2 and P_W and LP_W in m3, so the empty cells make "
      "the model's arithmetic dimensionally unchecked. The LP definition wraps onto a second line, the "
      "three replacement-cost rows print a space after their slash ('Replacement/ restoration'), and "
      "nothing in the sixteen rows defines the AHP weights, J0, or the score G1 the later sections use. "
      "Caption prints ABOVE on p4; the grid follows on p5. NO SENTENCE NAMES THE TABLE.",
      dict(rows=17, cols=3, header_rows=1, merged_cells=False, numeric_cols=0, text_cols=3,
           width="full", continued=False, **BOOKTABS_UNITS),
      CAPT1, "text-layer", uncited(), section_kind="model")

# ============================================================ 4.1.1: the short-run cost tree
figure(6, 1, "flowchart-or-schematic", CAP1, "text-layer",
       cited(6, 6, ["Figure.1"], 1,
             lead="we use diagram in Figure.1 to show the relationship among every factor in it."),
       S_411,
       "A top-down tree of nine boxes in four ranks: Short run cost C into Economic cost C1 and "
       "Environmental cost C2; C1 into Capital cost C12; C12 into Labor cost C121, Land cost C122 and "
       "Material cost C123; C2 into Replacement cost of solid waste pollution C21, of water pollution "
       "C22 and of air pollution C23. Plain black hairline boxes with centred two-line labels (a name "
       "over an italic symbol), orthogonal connectors, no colour, no legend, no title. THE NUMBERING "
       "STARTS AT TWO ON BOTH BRANCHES: C1's only child is C12 and C2's children are C21 to C23, so "
       "there is no C11 anywhere and the second digit carries no meaning a reader can recover - the "
       "same slip recurs in Figure 2, where B1's only child is B12. THE SYMBOLS ARE A THIRD SYSTEM: the "
       "notation table two pages earlier defines CS, PC and EC for exactly these nodes, the body writes "
       "CS = PC + EC, and the plate renames them C, C1 and C2 with a subscript depth that then has to "
       "reach three digits to label the leaves (C121). THE DEPTH OF THE TREE IS ASYMMETRIC AND "
       "UNEXPLAINED: the economic branch goes three levels deep down to individual cost items while "
       "the environmental branch stops at the three replacement costs, so the two halves of one sum are "
       "drawn at different granularities with nothing saying why. The connector feeding C2's three "
       "children is drawn from C2's stem but runs further left than its own boxes and ends above the "
       "Capital cost box with no stem, which at print size reads as a dangling rule between the two "
       "branches. Cited by the sentence that introduces it; the caption is printed BELOW.",
       geometry("flowchart-or-schematic", labels=True), "1", section_kind="model")

# ============================================================ 4.1.2: the benefit tree
figure(7, 1, "flowchart-or-schematic", CAP2, "text-layer",
       cited(7, 7, ["Figure.2"], 1, lead="can be viewed in Figure.2."),
       S_412,
       "The same tree in the same style, four boxes in three ranks: Short run benefit B into Economic "
       "benefit B1 and Social benefit B2; B1 into a single wide box labelled 'aggregated present "
       "discounted values of the business's profits in its duration' over B12; B2 into Increase of "
       "employment rate B21 and Improvement of city image B22. THE NUMBERING AGAIN SKIPS ONE - B1's only "
       "child is B12 - so the plate and Figure 1 share an off-by-one in the index that neither the text "
       "nor the caption acknowledges. THE PLATE AND THE FORMULA DISAGREE ABOUT THE DISCOUNTING: the "
       "figure nests the discounted profit stream one level BELOW the economic benefit, as B12 under B1, "
       "while the formula on the same page writes that stream as a term of the total directly, "
       "B_S = sum of B_t/(1+r)^t plus B21 plus B22, so B1 has no content of its own in the formula and "
       "B12 never appears in it. A FOURTH SYMBOL SYSTEM ARRIVES WITH THE CAPTION: the text introduces "
       "the benefit as EB and SB and sums them into BS, the formula then calls the total B_S, and the "
       "plate calls the same three nodes B, B1 and B2. The discounted box is set much wider and taller "
       "than its siblings to hold three lines of prose, which unbalances the tree; no box carries a "
       "number or a value, so nothing on the plate is checkable against the case study's figures. "
       "Caption prints BELOW.",
       geometry("flowchart-or-schematic", labels=True), "2", section_kind="model")

# ============================================================ 4: the AHP band grid
table(11, 1, S_4R,
      "Seven columns - Ranking (Score) | Decrease of biodiversity | Reduction of air quality | "
      "Reduction of soil quality | Reduction of water quality | Impact on human health | Capital input "
      "- over five bands, ruled booktabs with no verticals and the caption above the header. THE BANDS "
      "ARE WRITTEN IN FIVE DIFFERENT QUANTITIES AND ONLY ONE CARRIES A SCALE: four columns are "
      "dimensionless percentage reductions, human health is an unlabelled count, and capital input is "
      "expressed as a multiple of an average cost AC that is never defined on this page (the reader "
      "learns on p16 that AC is $3,000 million). Row labels are set as a rank on one line and its score "
      "in parentheses on the next ('1' then '(9)'), so the first column is two lines deep in every row "
      "while the other six are one. Spelling and spacing break inside the cells - 'above0.5' with no "
      "space against 'above 0.5' in the next three columns, 'under0.1'/'under0.05' on the bottom band - "
      "and the tilde range separator is fullwidth. THE TABLE IS SPLIT ACROSS TWO PAGES WITH NO "
      "REPEATED HEADER: bands 4 and 5 fall on p12 as a bare block of three-digit rows under the running "
      "header (that overflow is refused in this census, see excluded_regions), so a reader reaching p12 "
      "sees '0.1~0.2 0.05~0.15 ...' with no column names anywhere above them. THE BAND BOUNDS ARE NOT "
      "NESTED THE SAME WAY IN ALL FIVE ENVIRONMENTAL COLUMNS: biodiversity and soil step 0.3/0.2/0.1 "
      "while air and water step 0.5/0.3/0.15/0.05, so a change of 0.1 falls in the soil column's "
      "fourth band and the water column's fourth band, and a change of 0.05 sits on the boundary of "
      "water's bottom band - the boundaries are printed without brackets, so whether a bound belongs to "
      "the band above or below it is decided nowhere, and Table 3 on p16 resolves one such tie against "
      "the table's own reading. Cited by the sentence that introduces it.",
      dict(rows=6, cols=7, header_rows=1, merged_cells=False, numeric_cols=6, text_cols=1,
           width="full", continued=True, **BOOKTABS),
      CAPT2, "text-layer",
      cited(11, 11, ["Table2"], 2,
            lead="we give the ranking standards of these environmental indexes in Table2:"),
      section_kind="model")

exclude(12, 1, "split-across-pages",
        "Rows 4 and 5 of Table 2 ('4 (3)' and '5 (1)' with their five bands) spilled onto p12 under "
        "the running header with no repeated header, no caption and no column names. Recorded as the "
        "table's continuation through Table 2's continued flag rather than as a table row of its own, "
        "because a grid without a header row cannot be censused as a table and inventing one would be "
        "an invention. The overflow is also the reason the band boundaries cannot be read off a single "
        "page.")

# ============================================================ 4.2.1: the long-run cost tree
figure(12, 2, "flowchart-or-schematic", CAP3, "text-layer",
       cited(12, 12, ["Figure.3"], 1,
             lead="we give the Figure.3 to illustrate our process of AHP."),
       S_421,
       "The long-run cost tree in the same house style, eight boxes in three ranks: Long run cost C "
       "into Economic cost C1 and Environmental cost C2; C1 into Capital input C12 with no children of "
       "its own; C2 into five tall narrow boxes - Decrease of biodiversity C21, Reduction of air "
       "quality C22, Reduction of soil quality C23, Reduction of water quality C24 and Impact on human "
       "health C25. THE FIVE ENVIRONMENTAL LEAVES ARE THE FIVE ENVIRONMENTAL COLUMNS OF TABLE 2 IN THE "
       "SAME ORDER, which is the one place in the paper where a plate and a grid can be checked against "
       "each other, and they agree. EVERYTHING ELSE IS CRAMPED: the five boxes are narrow enough that "
       "'Decrease of biodiversity' is broken mid-word as 'biodiversi-ty' with a hyphen the word does not "
       "contain, 'Environmental cost' wraps onto two lines inside its box and its C2 subscript sits on "
       "the connector descending from it, and the rightmost box runs almost to the type area's edge. "
       "THE ECONOMIC BRANCH IS NOW A LEAF: C12 'Capital input' has no children here although Figure 1 "
       "expanded the same node to labor, land and material, and the caption and text never say the "
       "long-run model has stopped decomposing it. C1's child is again numbered 12 with no C11, the "
       "third appearance of that skip. Nothing is quantified: the plate names the AHP criteria but "
       "carries none of the weights, ranks or scores that section 4 computes, and its five leaves are "
       "the six-vector w0's five environmental entries with no indication of order. Caption prints "
       "BELOW.",
       geometry("flowchart-or-schematic", labels=True), "3", section_kind="model", order=2)

# ============================================================ 2 Calculation: the scored grid
table(16, 1, S_2C,
      "Three columns - Cost Index | Variation Value | Ranking (Score) - over six rows (biodiversity "
      "0.2, air 0.4, soil 0.1, water 0.1, human health 20, capital input $4,120million), ruled "
      "booktabs BUT WITH ONE VERTICAL RULE after the first column and the caption printed above the "
      "header. THE VALUE COLUMN MIXES FIVE DIMENSIONLESS NUMBERS WITH ONE DOLLAR AMOUNT, and the "
      "ranking column packs two numbers into one cell ('3(5)' = rank 3, score 5), so neither column can "
      "be sorted or summed without reading it. ONE ROW CONTRADICTS TABLE 2'S OWN BANDS, AND THE "
      "CONTRADICTION IS VISIBLE INSIDE THIS PLATE: soil quality's 0.1 is scored rank 5, although Table "
      "2's soil column steps 0.3/0.2/0.1, which puts 0.1 in the rank-4 band, while the row directly "
      "below scores water quality's identical 0.1 as rank 4 - the same value, two ranks, one column "
      "apart. The other four rows do follow Table 2 (biodiversity 0.2 in 0.2-0.3 gives 3, air 0.4 in "
      "0.3-0.5 gives 2, health 20 in 20-30 gives 3), and capital input is checkable once the prose's AC "
      "is used: $4,120 million against the $3,000 million stated under the table is 1.373, inside Table "
      "2's AC-to-1.5AC band, so 3(5) is right. THE RANK VECTOR THAT FOLLOWS THE TABLE IS A PERMUTATION "
      "OF ITS SCORE COLUMN IN AN ORDER NOBODY STATES: p = (5,5,7,1,3,5) reads down the rows as "
      "capital input first, then biodiversity, air, soil, water and health - Table 2's own capital "
      "column is printed LAST - so the vector cannot be checked against the grid above it without "
      "reordering it. Caption prints ABOVE and cites Tab.2; NO SENTENCE NAMES THIS TABLE.",
      dict(rows=7, cols=3, header_rows=1, merged_cells=False, numeric_cols=2, text_cols=1,
           width="full", continued=False, **GRIDRULES),
      CAPT3, "text-layer", uncited(), section_kind="result")

# ============================================================ 6: the sensitivity plot
figure(18, 1, "line", CAP4, "text-layer",
       cited(18, 18, ["Figure.4"], 1,
             lead="Figure.4 illustrates a function of the score varying with the weight."),
       S_6,
       "A pasted MATLAB figure - measured as a single raster path while every other plate in this "
       "paper is vector - titled 'sensitivity', with axis titles 'proportion a' under a 0-to-1 abscissa "
       "and 'score of cost' beside a 3-to-6 ordinate at half-unit steps, two straight strokes and two "
       "floating labels placed inside the frame by gtext: 'after adjustment' beside the flatter blue "
       "line and 'before adjustment' beside the steeper red one. THE PLATE IS THE ONE EXHIBIT IN THE "
       "PAPER THAT MATCHES ITS PROSE TO THE DIGIT, and it matches by construction: the text gives the "
       "two fitted functions as 0.295a+4.705 and 0.858a+4.142, so at a = 0 the blue line must sit at "
       "4.705 and the red at 4.142, which is where the pixels put them, and at a = 1 both reduce to "
       "exactly 5.0, which is the 'converge to 5' the section claims. THAT CONVERGENCE IS A TAUTOLOGY "
       "AND NOT A FINDING: both intercepts are chosen so that each function equals 5 at a = 1, so the "
       "two lines meet at the right frame edge whatever the model does, and the whole visual claim - "
       "that the adjusted model is more stable because its slope is smaller - is a statement about two "
       "slopes printed 0.295 and 0.858, not about anything the figure tests. The crossing is drawn "
       "exactly on the axis border, where a reader scanning the plot reads it as a truncation rather "
       "than an intersection. The labels are unanchored text with no leader lines and no key, so which "
       "label belongs to which stroke is settled only by their vertical position; the plot carries tick "
       "marks on all four sides, MATLAB's default look, no grid, no annotation of the crossing and no "
       "statement of what the score's unit is. The code that produced the bitmap is printed as text in "
       "the appendix (a = 0:0.1:1; y1 = 0.295a+4.705; y2 = 0.858a+4.142; plot; ylim([3 6]); gtext), "
       "so the plate is reproducible but is not itself live. Caption prints BELOW.",
       geometry("line", panels=1, legend="inside", labels=True, numbers=True), "4",
       section_kind="result")

# ============================================================ Appendices: the pasted exhibits
figure(22, 1, "map-or-plan-view", CAPP1, "typed-from-crop", uncited(), S_APP,
       "A pasted screenshot of a road and administrative map of the Tennessee Valley, inside a blue "
       "frame with a PowerPoint-style legend strip pasted under it reading 'May 2005 map of TVA sites' "
       "with three swatches - dam, nuclear, fossil. Place labels print across seven states: Kentucky, "
       "Lexington, Knoxville, Nashville, Chattanooga, Huntsville, Birmingham, Memphis, Tupelo, Atlanta, "
       "Macon, Montgomery, Jackson, Charlotte, Columbia, with state abbreviations IL, MO, KY, TN, NC, "
       "SC, GA, AL, MS, AR, WV, VA and interstate shields 16, 20, 24, 26, 40, 55, 59, 65, 70, 75, 77, "
       "81, 85. THE PLATE HAS NO FIGURE NUMBER, NO CAPTION OF THE PAPER'S OWN AND NO APPARATUS: no "
       "scale bar, no north arrow, no graticule, no coordinate frame, no source or credit line for the "
       "basemap, and the only words tying it to the paper are the page's sentence 'This is the map of "
       "the power station:' - singular, although the screenshot covers a basin spanning parts of seven "
       "states and marks dozens of sites. ITS LEGEND DOES NOT MATCH ITS SYMBOLS: the swatches are keyed "
       "red, purple and orange for dam, nuclear and fossil while the map's own markers print red and "
       "yellow with white halos, so the fossil swatch (orange) has no orange marker to name. The "
       "bitmap is low-resolution with visible JPEG ringing around the markers, the purple nuclear "
       "symbols are almost invisible at print size, and nothing on the plate states which of the "
       "project's cost or benefit figures came from which site. Caption typed from the pasted strip; it "
       "prints BELOW the map inside the image.",
       geometry("map-or-plan-view", panels=1, legend="below", labels=True), "", section_kind="other")

figure(22, 2, "table-as-figure", CAPP2, "typed-from-crop", uncited(), S_APP,
       "A pasted screenshot of a page from a printed Chinese textbook: a ruled construction-cost table "
       "titled '表 3-2 TWA 火力发电厂的建设成本表' with a footnote marker ¹ that the paper never "
       "resolves. Six columns - plant name (merged down the rows) | year built (年) | installed capacity "
       "(万千瓦) | construction cost (美元/千瓦) split into two sub-columns, 按当年美元计 and 按1982年 "
       "不变价格计 - over eight plants: 沃茨巴 1942 24.0 92 556, 约翰逊维尔 1951 79.4 145 525, 威多斯"
       "克里克 1952 85.5 181 648, 肖尼 1953 175.0 145 512, 金斯敦 1954 172.3 154 536, 科尔伯特 1955 "
       "84.6 126 428, 约翰塞维尔 1955 84.7 139 473, 加拉廷 1956 60.0 126 386. THE TABLE IS THE SOURCE "
       "BOOK'S, NOT THE PAPER'S: it keeps the book's number 3-2 instead of an appendix number, it is "
       "entirely in Chinese inside an English paper with no translation of a single heading, and it is of "
       "the closed-box, full-grid kind - vertical rules between every column and rules above and below "
       "every row - so the appendix's two grid styles (booktabs in the body, hand-ruled box here) sit "
       "six pages apart with nothing reconciling them. THE UTILITY IS MISNAMED IN ITS OWN TITLE: 'TWA' "
       "where the paper, the caption of Figure 4 and the map all say TVA. NO CELL IS CHECKABLE: the two "
       "cost columns are a current-dollar and a constant-price pair whose ratio is a deflator the paper "
       "never prints, there is no total row and no column that sums, and the paper never uses any of "
       "these eight rows in its own benefit or cost figures. Caption typed from the in-image title; the "
       "paper's own lead-in above it is 'These are the cost tables:'.",
       geometry("table-as-figure", labels=True, numbers=True), "", section_kind="other", order=2)

figure(23, 2, "table-as-figure", caption("", position="below"), "none", uncited(), S_APP,
       "The continuation of the construction-cost table: the last three plants - 约翰逊维尔发电厂"
       "（扩建）1958 51.9 123 386, 艾伦火力发电厂 1959 99.0 — —, 加拉廷发电厂（扩建）1959 65.5 — — - "
       "in the same closed box with vertical grid, and NO HEADER ROW REPEATED, no table number and no "
       "caption on this page, so the three rows arrive bare under the running header. THE MISSING "
       "VALUES ARE EM DASHES WITH NO FOOTNOTE anywhere in the paper, so whether Allen and the Gallatin "
       "extension are omitted from a mean, treated as zero, or simply unavailable is unstated - which "
       "matters, because the eight priced plants and these three lines are the only plant-level data "
       "the appendix prints. Below the foot rule the next page section's running head ('第 4 章 TWA 电 "
       "力的开发成就与问题') bleeds into the crop, i.e. the scan includes the book's own chapter "
       "furniture. Census taken as its own row because the region is a separate pasted image and "
       "carries a cost table's content, with the continuation noted here rather than in a table flag.",
       geometry("table-as-figure", labels=True, numbers=True), "", section_kind="other", order=3)

figure(23, 3, "table-as-figure", caption("", position="above"), "none", uncited(), S_APP,
       "A second pasted screenshot from the same Chinese textbook: the centred chapter head '第 4 章 "
       "TWA 电力的开发成就与问题' above a six-column revenue table whose corner cell is split by a "
       "diagonal rule carrying 项目 over 年份, with the columns 电力收入 | 总收入 | 租金收入及其它项目"
       "收入 | 电力净收入 | 经营支出 and eleven year rows from 1957 down to 1947 (1957 234,871,850 / "
       "235,732,976 / 861,126 / 58,143,669 / 177,589,307 down to 1947 43,810,572 / 44,144,090 / "
       "333,518 / 21,248,377 / 22,305,341). THE TABLE'S ONE IDENTITY IS CHECKABLE AND FAILS TWICE: "
       "总收入 should equal 电力收入 plus 租金收入及其它项目收入, which holds to the digit for nine of "
       "the eleven rows, is off by exactly 100 in 1953 (104,285,187 + 592,682 = 104,877,869 against a "
       "printed 104,877,969) and off by TEN MILLION in 1952 (94,466,655 + 537,735 = 95,004,390 against "
       "a printed 85,004,390) - a single leading digit, which also breaks the otherwise monotone "
       "decline of the series and makes 1952's total smaller than 1951's while its revenue is larger. "
       "NO UNIT IS PRINTED ANYWHERE in the header, caption or foot although every cell is plainly a "
       "dollar amount, so the paper's own dollar figures elsewhere cannot be reconciled with this grid; "
       "1951 carries a dash in 电力净收入 with no note; there is no total row; the closed box is hand-"
       "ruled with scan skew and a grey page ground, and the value columns are printed to the dollar at "
       "seven to nine digits with no thousands separators, which is why the digit error is hard to see. "
       "Caption prints ABOVE the table as the book's chapter running head, which is furniture rather "
       "than a caption; the paper adds none.",
       geometry("table-as-figure", labels=True, numbers=True), "", section_kind="other", order=4)

figure(23, 4, "table-as-figure", caption("", position="above"), "none", uncited(), S_APP,
       "The revenue table's continuation on the same page: after the 1947 row (repeated from the region "
       "above) and one row struck through so heavily that every cell is illegible, the years run 1966, "
       "1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958 (1966 321,580,000 / 326,804,000 / 2,215,000 / "
       "47,889,000 / 270,221,000 down to 1958 232,217,189 / 233,548,166 / 1,330,977 / 54,981,946 / "
       "178,566,220), the 1966 row also carrying a struck line, with no header row repeated. THE YEAR "
       "ORDER BREAKS ACROSS THE PAGE: the table reads 1957 down to 1947, then jumps to 1966 and runs "
       "back down to 1958, so the eleven years 1948-1957 appear twice in different runs - 1957 and 1947 "
       "in the first, 1966-1958 in the second - and a reader cannot follow the series without reversing "
       "direction mid-table. THE IDENTITY DEGRADES TOWARD THE RECENT ROWS: it holds exactly at 1958 and "
       "1959 and then misses by 337 in 1960, by 2,765,000 in 1964 and by 3,009,000 in 1966, consistent "
       "with the later rows being rounded to thousands and with an income category the column set does "
       "not carry - but the plate itself never says so. The 1961 rental-income cell is BLANK with no "
       "dash, unlike the dash used for missing values elsewhere, and the two struck rows leave a "
       "reader unable to tell whether they were withdrawn or corrected. NO UNIT, NO CAPTION, NO TABLE "
       "NUMBER. The paper's lead-in 'These are Matlab codes:' is printed at the very foot of this "
       "region, orphaned from the listing it introduces - the code itself is live text on pp23-24 and "
       "is therefore not censused.",
       geometry("table-as-figure", labels=True, numbers=True), "", section_kind="other", order=5)

exclude(21, 1, "not-an-exhibit",
        "A block of three reference-list lines ('Biological Conservation 120, 549-565.', '[2] Songlin "
        "Xu, Economic Analysis of Enviromental Polltion[J]...', '[3] Hritonenko N, Yatsenko Y. "
        "Mathematical Modeling in Economics, Ecology, and') measured as a region because it is set as a "
        "run of vector text. Page furniture of the References section, not an exhibit.")

exclude(23, 1, "not-an-exhibit",
        "The running header 'Team #1902917  Page 23 of 24' with its rule, measured as a region. The "
        "first sliver of the pasted cost table's top border falls inside it, but the table's content is "
        "recorded on this page's regions 2 to 4.")

exclude(24, 1, "not-an-exhibit",
        "The running header 'Team #1902917  Page 24 of 24' with its rule, measured as a region. The "
        "MATLAB listing that follows on this page is live text, not a measured region, so nothing on "
        "p24 is an exhibit.")

RULES = [
    "Measure first, then read the pixels: sixteen measured regions over eleven of twenty-four pages "
    "resolve into nine figure rows, three table rows and four refusals, with nothing unaccounted "
    "[place.doc_order].",
    "The census of this appendix is a census of someone else's scanned pages: five regions on pp22-23 "
    "are pasted screenshots of a printed Chinese textbook - a TVA map, a construction-cost table and a "
    "revenue table split over two pages each - carrying no figure number, no caption in the paper's "
    "language and no unit [geometry.family].",
    "A table split across pages has to be one row and one refusal: Table 2's bands 4 and 5 fall on p12 "
    "under the running header with no repeated header, so the grid is recorded with continued set and "
    "the overflow refused as split-across-pages rather than invented as a headerless table "
    "[table.header_rows].",
    "The paper writes its pointers without a space: 'Figure.1', 'Figure.2', 'Figure.3', 'Figure.4', "
    "'Table2', 'Tab.2', and every one of them is cited exactly once [mention.lead_sentence].",
    "Seven of twelve exhibits are named by no sentence: the notation grid, Table 3, and all five "
    "appendix rows are reached only through a heading, a caption, or the page's deictic 'This is the "
    "map of the power station:' and 'These are the cost tables:' [mention.count].",
    "One arithmetic result stands on no vector the paper prints: p16 gives the cost score as "
    "G1 = pw0 = 372, while p = (5,5,7,1,3,5) against w0 = (1/2, 5/42, 1/14, 5/42, 1/21, 1/7) gives "
    "4.571, and the sensitivity section fits the same score at 0.858a+4.142, i.e. 4.14 to 5.0 "
    "[mention.lead_sentence].",
    "A grid can break its own band table: Table 3 scores soil quality's 0.1 as rank 5 although Table "
    "2's soil column steps 0.3/0.2/0.1 and puts 0.1 in rank 4, and scores water quality's identical "
    "0.1 as rank 4 in the next row down [table.numeric_cols].",
    "Three symbol systems describe the same two sums: the notation grid defines CS, PC and EC, the body "
    "writes CS = PC + EC and B_S = sum of B_t/(1+r)^t + B21 + B22, and the three tree plates use C, "
    "C1, C2, C12, C21-C25, B, B1, B2 and B12 - with the index 11 skipped in both trees "
    "[geometry.family].",
    "A sensitivity plot can prove its own tautology: Figure 4's two functions 0.295a+4.705 and "
    "0.858a+4.142 both reduce to exactly 5.0 at a = 1, so the 'converge to 5' the section reads off "
    "the plate was imposed when the functions were fitted [geometry.legend].",
    "The two checkable identities of the appendix fail in the direction a reader cannot see: the "
    "revenue table's 总收入 = 电力收入 + 租金 income misses by exactly 100 in 1953 and by ten million "
    "in 1952 (a leading digit printed 85,004,390 for 95,004,390), and the construction-cost table "
    "prints no total at all [geometry.family].",
]

NOTE = """\
Paper 182, Team 1902917: ecological cost inside the cost-benefit analysis of land use projects, for
problem E 2019. A short-run model that prices environmental damage by replacement cost, a long-run model
that ranks and scores the same costs with the Analytic Hierarchy Process, one case each - a small paper
mill for the short run, the Tennessee Valley thermal power programme for the long run - and a sensitivity
study of the AHP weights. Twenty-four pages, sixteen measured regions over eleven of them, resolving
into NINE FIGURE ROWS, THREE TABLE ROWS and FOUR REFUSALS, with nothing unaccounted.

THE PAPER IS ARGUED IN THREE SYMBOL SYSTEMS AND NONE OF THEM IS THE OTHER'S. The notation grid on p5
defines C_S, C_L, PC, EC, P, LP, P_S, P_W, P_A and the three replacement rates, and the body then writes
EC = f(P-LP) = C_RS*(P_S-LP_S) + C_RW*(P_W-LP_W) + C_RA*(P_A-LP_A) and CS = PC + EC. The three tree
plates ignore all of that: Figure 1 runs C into C1 and C2 and down to C121, C122 and C123, and Figure 2
does the same for the benefit side as B, B1, B2 and B12, while the benefit formula on the same page
calls the total B_S and the text one page earlier calls the parts EB and SB. No page maps one system to
another, and both trees skip index 11 - the only child of C1 is C12, the only child of B1 is B12 - so
the subscript's first digit carries a meaning that is never explained and cannot be recovered.

THE ONE NUMBER THAT SHOULD HAVE BEEN CHECKED AND WAS NOT. Section 2 Calculation scores the six cost
indexes against Table 2's bands, forms the rank vector p = (5,5,7,1,3,5), and reports the cost score as
G1 = pw0 = 372. With w0 = (1/2, 5/42, 1/14, 5/42, 1/21, 1/7) - the six weights the paper prints on p11,
which sum to one - the inner product is 4.571, not 372, and the sensitivity section two pages later fits
the same cost score as 0.858a + 4.142, a number of order 5. So G1 belongs to no scale the paper prints:
it is forty times the score the model itself produces and eighty times the fitted function, and no
sentence notices. Everything downstream of that number - the claim that benefit "always far exceeds" cost
- rests on comparing a benefit in dollars against a cost score in the single digits, and the paper does
not perform the comparison it asserts.

TABLE 2'S BANDS AND TABLE 3'S RANKS DISAGREE ONCE, VISIBLY. The five environmental bands step differently
by column (biodiversity and soil step 0.3/0.2/0.1, air and water step 0.5/0.3/0.15/0.05), so a change of
0.1 is rank 4 in the soil column and rank 4 in the water column. Table 3 scores soil's 0.1 as rank 5 and
water's 0.1 as rank 4 in the row directly beneath it. The other four rows do follow the bands, and the
capital row is checkable once the prose's average cost of $3,000 million is used: $4,120 million is 1.373
AC, which is Table 2's rank-3 band. Both tables also print two numbers in one cell ("3(5)") throughout.

THE PLATES. Figures 1 to 3 are the same hand-built tree three times, in plain hairlines with a name over
an italic symbol in each box: the short-run cost tree (nine boxes, four ranks), the short-run benefit
tree (four boxes, three ranks, one box made wide enough to hold three lines of prose) and the long-run
cost tree (eight boxes, three ranks, five narrow leaves whose labels break mid-word). Their one real
virtue is that Figure 3's five environmental leaves are Table 2's five environmental columns in the same
order, so a reader can lay the plate over the grid. Figure 4 is the paper's only quantified plate and the
only pasted raster in the body: a MATLAB plot of the two fitted cost-score functions against the
economic weight a, with the two strokes labelled by floating gtext text and meeting exactly at the frame's
right edge - a convergence that is a property of how the two affine functions were fitted (both equal 5 at
a = 1), not of anything the model tests.

THE APPENDIX IS SOMEONE ELSE'S BOOK. Five of the nine figure rows are screenshots of a printed Chinese
textbook: a road map of the Tennessee Valley captioned only by a pasted "May 2005 map of TVA sites" strip,
a construction-cost table (表 3-2, eight plants, closed box with full vertical grid, title mistyping the
utility as TWA) continued onto the next page with three more plants and two em-dash cells that no
footnote explains, and a revenue table for 1947-1957 continued out of order as 1966-1958, with two rows
struck through and one blank cell where every other missing value is a dash. Not one of these carries a
figure number, a caption in the paper's language or a unit, and the revenue table's only identity
总收入 = 电力收入 + rent income fails by exactly 100 at 1953 and by ten million at 1952, where the total
prints 85,004,390 for what the row sums to 95,004,390. The paper's own lead-in, "These are Matlab
codes:", sits orphaned at the foot of the page region above the listing, and the listing itself is live
text on two pages - measured as no region at all, so it is not in this census.

Families: table-as-figure 4 (the appendix's five screenshots are its map plus four table images),
flowchart-or-schematic 3 (Figures 1, 2, 3), line 1 (Figure 4), map-or-plan-view 1 (the appendix map), table-grid 3
(Tables 1, 2, 3).
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

out = PROXY / "pc182-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
