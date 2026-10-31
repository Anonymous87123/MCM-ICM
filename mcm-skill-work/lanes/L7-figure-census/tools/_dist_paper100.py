"""Hand census of P-C-2016-47823-59d82231 (Team 47823, 27 pages, 16 measured regions).

A Goodgrant-Foundation school-selection paper. Sixteen measured regions resolve into FIVE FIGURE ROWS,
SEVEN TABLE ROWS and FOUR EXCLUSIONS, with nothing unaccounted.

  p5  r1  Table 1    table-grid       the notation list, 2 by 10, closed box
  p5  r2  --         excluded         head of Table 2; the table turns the page and its caption is below
                                     its foot on p6, so it is recorded once at p6r1
  p6  r1  Table 2    table-grid       variable types and their use, 2 by 14, group cells merged
  p6  r2  Figure 1   bar              FC 1000 grants by subject, screenshot with value labels
  p7  r1  Figure 2   bar              FC 1000 grants by state, same tool, same printed source URL
  p10 r1  Table 3    table-grid       top ten candidate schools by PCA, 4 by 11
  p11 r1  Figure 3   line             a hand-drawn U against x curve marking delta-x and delta-U
  p15 r1  Figure 4   flowchart-or-schematic  the full-page LA_PSA_GT algorithm chart
  p17 r1  Figure 5   line             MATLAB convergence curve titled 'fitness'
  p17 r2  Table 4    table-grid       the top ten of the recommending list, 9 by 12
  p18 r1  Table 5    table-grid       the top ten schools by Gates Foundation amount, 3 by 11
  p18 r2  --         excluded         head of Table 6; caption below its foot on p19
  p19 r1  Table 6    table-grid       investment change under k +-5%, +-10%, 5 by 7
  p23 r1  (title)    table-grid       Appendix 1: Recommending List, 9 columns, ranks 1 to 35
  p24 r1  --         excluded         the same list turned the page, ranks 36 to 50 and its foot
  p26 r1  --         excluded         an in-body display-equation fragment, no frame, no number

TABLE 4 AND THE APPENDIX LIST ARE THE SAME FIFTY SCHOOLS, AND THEIR 't' COLUMN DISAGREES: for the ten
rows they share, the ROI and the institution are identical while the integer under 't' is 4, 5, 3, 5, 3,
6, 5, 5, 6, 5 in Table 4 and 4, 5, 3, 4, 3, 5, 4, 4, 5, 4 in the appendix. Two printed versions of one
table, both answering the same question with different values.

TABLE 6'S CAPTION SAYS STANDARD DEVIATION AND ITS ROWS ARE PERCENTAGE CHANGES WHOSE FOOT IS THEIR MEAN.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2016-47823-59d82231"
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


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below",
            variables: int = 0, sentences: int = 1) -> dict:
    """Caption block. Every caption in this paper prints BELOW its exhibit."""
    return {"verbatim": schema.norm(verbatim), "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": sentences, "units": False,
            "variables": variables > 0, "variable_count": variables,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def geometry(family: str, panels: int = 1, layout: str = "1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = False,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


def head(page: int, label: str) -> str:
    """The indexed heading on `page` with this label.

    The heading pass collapses for this paper: its text layer writes ONE WORD PER LINE, so every
    indexed heading keeps only its first word ('Data', 'Analysis', 'Results', ...). The census uses
    those labels verbatim rather than inventing the printed wording.
    """
    for h in CTX["headings"]:
        if h["page"] == page and h["label"] == label:
            return h["label"]
    raise SystemExit(f"no indexed heading {label!r} on p{page}")


S_ASSUME = [head(4, "Assumptions"), head(5, "Notation")]
S_DATA = [head(5, "Data"), head(5, "Analysis")]
S_FOCUS = [head(5, "Analysis")]
S_PCA = [head(9, "Results")]
S_TEST = [head(18, "Testing")]
S_APPX = [head(23, "Appendix")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
for _group in (S_ASSUME, S_DATA, S_FOCUS, S_PCA, S_TEST, S_APPX):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN:
            raise SystemExit(f"section label is not an indexed heading: {_label!r}")

CAPT1 = caption("Table 1: notation", numbering="Table N:")
CAPT2 = caption("Table 2: the different types of variables and their use", numbering="Table N:")
CAPT3 = caption("Table 3: top ten candidate schools by PCA", numbering="Table N:")
CAPT4 = caption("Table 4: the top ten schools and their investment amount in our recommending list "
                "(unit:million)", numbering="Table N:")
CAPT5 = caption("Table 5: the top ten schools ranked by Gates Foundation’s investment amount",
                numbering="Table N:")
CAPT6 = caption("Table 6: the standard deviation of the investment amount correspond to the change "
                "of MRS k", numbering="Table N:")
CAPT_APPX = caption("Appendix 1: Recommending List", numbering="none", position="above")
CAP1 = caption("Figure 1: distribution of grants from FC 1000 foundations by subject area [1]")
CAP2 = caption("Figure 2: distribution of grants from FC 1000 foundations by recipient location")
CAP3 = caption("Figure 3: the relationship between incremental utility and investment")
CAP4 = caption("Figure 4: flow chart of the LA_PSA_GT algorithm")
CAP5 = caption("Figure 5: fitness of the algorithm")

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
          cap_block: dict | None = None, cap_src: str = "none", mention: dict | None = None,
          section_kind: str = "other", order: int = 1) -> None:
    block = cap_block or caption("", numbering="none")
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)],
        "family": "table-grid", "caption_source": cap_src,
        "caption_verbatim": block["verbatim"], "caption": block, "table": spec,
        "place": place(page, reg, section_kind, section, order),
        "mention": mention or uncited(), "note": note, "confidence": "high",
    })


BOXED = {"header_rows": 1, "rule_style": "vertical-rules", "zebra": False,
         "diagonal_header": False, "units_in_header": False, "decimal_aligned": False,
         "orientation": "portrait", "note_sentence": ""}

# ============================================================ 3: the notation list
table(5, 1, S_ASSUME,
      "The paper's notation list: a black-filled header bar 'Notation | Meaning' over NINE body rows "
      "that run U (Social utility of the school), x (Amount of the investment), j (Time period "
      "(j =0,1,2,3,4,5)), m, M, N, k (MRS (marginal rate of substitution)), g (Graduation rate) and "
      "lambda,nu (Lagrange multiplier). CLOSED BOX: a rule at top and foot, rules between every pair "
      "of rows, vertical rules at both edges and between the two columns, so the nine rows are counted "
      "in ruled cells. Every entry is centred and italic, one symbol per row, and the header is white "
      "on black rather than ruled off. The caption 'Table 1: notation' prints BELOW and NO SENTENCE "
      "NAMES THE TABLE - the only pointer is the prose 'Here are the notations and their meanings in "
      "our paper:', which names nothing. Nine symbols are defined here and the model then uses "
      "quantities that appear in no row of it, among them the constant k that the paper later makes "
      "the subject of a whole sensitivity table.",
      dict(rows=10, cols=2, merged_cells=False, numeric_cols=0, text_cols=2, width="full",
           continued=False, **BOXED),
      CAPT1, "text-layer", section_kind="symbols")

# ============================================================ 4.1: variable types, over the page turn
table(6, 1, S_DATA,
      "The variable classification table, and it TURNS THE PAGE: the header bar 'Type and use | "
      "Variable' and four rows print at the foot of p5, the remaining nine rows and the caption print "
      "at the head of p6, so the exhibited region is the second half of a fourteen-row grid (header "
      "plus thirteen body rows) whose head is the unmeasured p5 region. The left column carries a "
      "GROUP LABEL that is ONE MERGED CELL SPANNING SEVERAL VARIABLE ROWS - 'Continuous data for "
      "school selecting' over four rows, 'Discrete data for school selecting' over one, 'Continuous "
      "data for determining the ROI' over four - so the horizontal rules break inside the right column "
      "and nowhere else, and the row count is the printed cell count, not the concept count. CLOSED "
      "BOX otherwise: vertical rules at both edges and between the columns, a rule above and below "
      "every row in the right column. Variable names are printed in the raw IPEDS spelling with no "
      "space before the parenthesis ('UGDS_(the distribution by race)', 'PPTUG_EF(part-time ratio)'), "
      "and the middle group's seven flags (CONTRAL PBI ANNHI TRIBAL AANAPII HIS NANTI) are printed as "
      "one run inside a single cell. The caption 'Table 2: the different types of variables and their "
      "use' prints BELOW and no sentence names it.",
      dict(rows=14, cols=2, merged_cells=True, numeric_cols=0, text_cols=2, width="full",
           continued=True, **BOXED),
      CAPT2, "text-layer", section_kind="symbols")

# ============================================================ 4.2: the two tool screenshots
figure(6, 2, "bar", CAP1, "text-layer",
       cited(6, 6, ["Figure 1"], 2, lead="The statistics are presented below"),
       S_FOCUS,
       "A horizontal bar chart pasted as a screenshot from the Foundation Center's own data viewer: a "
       "faint 'FOUNDATION CENTER' watermark sits behind the plot, the in-frame title reads "
       "'Distribution of Grants from FC 1000 Foundations by Subject Area, 2012', and eleven orange bars "
       "run downward from Health (5,001,048,709) through Education, Human Services, Public "
       "Affairs/Society Benefit, Arts and Culture, Environment and Animals, International Affairs, "
       "Science and Technology, Religion, Social Science to Other (31,649,337). NO AXIS, NO "
       "GRIDLINE, NO TICK AND NO SCALE: each bar's total is printed at its end and the order alone "
       "carries magnitude, so the eleven values are readable but the chart has no ruler. Category "
       "labels wrap onto two lines and the longest ('Public Affairs/Society Benefit', 'Environment and "
       "Animals', 'Science and Technology') are set tight against the bar ends. The caption prints "
       "BELOW with the double line 'Figure 1: distribution of grants from FC 1000 foundations by "
       "subject area [1] Source: http://data.foundationcenter.org/#/fc1000/subject:all/all/total/bar:"
       "amount/2012', and the prose that names it is the one before it, 'The statistics are presented "
       "below.' A later sentence reads a value off it: 'We can see that most foundation invested in "
       "the following three subjects: Health, Education and Human services from Figure 1.'",
       geometry("bar", labels=True, numbers=True), "1", section_kind="result", order=1)

figure(7, 1, "bar", CAP2, "text-layer",
       cited(7, 7, ["Figure 2"], 1,
             trail="Figure 2 tells us that most of the recipients are in four states"),
       S_FOCUS,
       "The same viewer, one page later, showing twenty-eight states instead of eleven subjects: in-"
       "frame title 'Distribution of Grants from FC 1000 Foundations by Recipient Location, 2012', "
       "orange bars from New York (3,106,887,447) and California (2,824,735,635) down through District "
       "of Columbia, Massachusetts, Texas and the rest to Louisiana (114,584,759), with every total "
       "printed at the bar end. Same absence of axis, gridline and tick as Figure 1, and the bar labels "
       "are set so small (about 4 pt in print) that the lower half of the list cannot be read without "
       "magnification. THE PRINTED SOURCE LINE UNDER IT IS BYTE-FOR-BYTE THE URL PRINTED UNDER FIGURE "
       "1 - 'http://data.foundationcenter.org/#/fc1000/subject:all/all/total/bar:amount/2012' - a "
       "subject-filtered query under a chart of recipient locations, so the two exhibits cite one "
       "source and two different views, and the citation does not reproduce what is shown. The caption "
       "prints BELOW and NO SENTENCE NAMES THE FIGURE BEFORE IT PRINTS; the only reference is the "
       "sentence after it, 'Figure 2 tells us that most of the recipients are in four states: New "
       "York, California, District of Columbia and Massachusetts.'",
       geometry("bar", labels=True, numbers=True), "2", section_kind="result", order=2)

# ============================================================ 5.2.4: the PCA shortlist
table(10, 1, S_PCA,
      "The PCA shortlist: a black-filled header bar 'Rank | UNITID | INSTNM | PCA Score' over ten "
      "ranked rows, from Widener University-Delaware Campus at 32.87 down to Richard Bland College of "
      "the College of William and Mary at 20.21. CLOSED BOX with vertical rules at both edges and "
      "between all four columns and a horizontal rule between every pair of rows. It is the only table "
      "in the paper with a RANK COLUMN, and the only one whose numbers carry a unit-bearing header. "
      "Captioned BELOW as 'Table 3: top ten candidate schools by PCA'; the reference is unnumbered and "
      "follows the table - 'In the table above, the school that has the highest PCA scores has the "
      "largest demand of grant based on our focus.' The scores fall from 32.87 to 20.21 across ten "
      "schools with no tie and no gap, and the column is centred, not decimal-aligned.",
      dict(rows=11, cols=4, merged_cells=False, numeric_cols=2, text_cols=2, width="full",
           continued=False, **BOXED),
      CAPT3, "text-layer",
      cited(10, 10, ["the table above"], 1,
            trail="In the table above, the school that has the highest PCA scores"),
      section_kind="result")

# ============================================================ 6.1: the sketched ROI curve
figure(11, 1, "line", CAP3, "text-layer",
       cited(12, 11, ["Figure 3"], 1, lead="In Figure 3 and equation (6)"),
       S_PCA,
       "A hand-drawn illustration, not a plot of data: two arrow-headed axes meeting at a point "
       "slightly left of centre, the ordinate labelled U and the abscissa labelled x at their far ends, "
       "one smooth concave-then-flattening curve rising from below the abscissa to the upper right, and "
       "TWO DASHED RECTANGLES drawn from two points on the curve to the axes to mark an incremental "
       "step: the ordinate pair is labelled delta-U and the abscissa step is labelled delta-x. NO "
       "TICKS, NO NUMBERS, NO SCALE, NO GRIDLINE, NO LEGEND, and no value of any kind - the curve "
       "encodes concavity and nothing else, so the equation it illustrates (ROI = delta-U over "
       "delta-x, printed as equation (6)) is the only quantitative statement in the section. The small "
       "body type of the labels, delta-U left of the ordinate and delta-x below the abscissa, is the "
       "smallest text on the page. Captioned BELOW as 'Figure 3: the relationship between incremental "
       "utility and investment'; the sentence that precedes it, 'We can plot a figure to describe the "
       "relationship:', names nothing, and the figure is first NAMED ON THE NEXT PAGE in 'In Figure 3 "
       "and equation (6), delta-x is the incremental amount of the inputs triggered by the "
       "investment.'",
       geometry("line"), "3", section_kind="model")

# ============================================================ 6.2.3: the algorithm chart
figure(15, 1, "flowchart-or-schematic", CAP4, "text-layer", uncited(), S_PCA,
       "A full-page vertical flowchart for the hybrid optimiser, drawn with plain rectangles, rounded "
       "terminals and two decision diamonds: Start, Initialize Lagrange multiplier, Construct Bound "
       "constrained problem, Initialize PSO parameters, Initialize the personal best particle and "
       "global best particle, Update the positions and velocities of the particles, Update the fitness "
       "the personal best particle and global best particle, Select the swarm previous best position "
       "as the initial point and update it by using Fletcher-Reeves conjugate gradient algorithm, the "
       "diamond PSO stopping criterion (NO arm loops back one box; YES arm falls through), the diamond "
       "Lagrange stopping criterion (NO arm loops back to the very first box from the left margin; YES "
       "arm falls through), Output f_gbest and g_best, End. Fifteen boxes and two nested loops, every "
       "arrow one-way and unlabelled except the two YES/NO pairs, no axes and no numbers. WHAT THE "
       "CHART DOES NOT SHOW is the inner detail the text spends four pages deriving: the conjugate-"
       "gradient step is collapsed into a single box, and the augmented-Lagrange update that the "
       "section is named for appears only as the first box and the second diamond. NO SENTENCE NAMES "
       "IT - the caption 'Figure 4: flow chart of the LA_PSA_GT algorithm' prints below the chart and "
       "the two definitions that follow it ('f_gbest is the maximum of the total ROI function', "
       "'g_best is vector of investment amount per year') are the only prose that touches it.",
       geometry("flowchart-or-schematic"), "4", section_kind="model")

# ============================================================ 7: the convergence curve
figure(17, 1, "line", CAP5, "text-layer", uncited(), S_PCA,
       "A MATLAB figure: one heavy red curve that drops from about 6e20 at iteration 0 through 1, 0.8 "
       "and 0.3 by iteration 25 and flattens onto the abscissa from about iteration 60 out to 150, "
       "inside a full box frame with light vertical gridlines at 50, 100 and 150. The in-frame title is "
       "the single word 'fitness'; the ordinate is graduated 0 to 6 with a floating multiplier 'x 10^20' "
       "printed at its top; the abscissa is graduated 0, 50, 100 and 150 and CARRIES NO LABEL AT ALL, "
       "so the unit of the horizontal axis (iterations? function evaluations?) is never stated. No "
       "legend, no data label, no value printed, and no marker on the point the algorithm stops at. "
       "The curve is a step function in its first forty iterations, falling in flat treads, so it "
       "records the best-so-far value rather than a converging sequence. Untitled in the sense that "
       "'fitness' names the quantity, not the plot, and NO SENTENCE NAMES THE FIGURE: the caption "
       "'Figure 5: fitness of the algorithm' prints below it and the following paragraph discusses "
       "small investments without referring back.",
       geometry("line", numbers=True), "5", section_kind="result")

# ============================================================ 7.1: the recommending list, first ten
table(17, 2, S_PCA,
      "The recommending list, first ten rows, NINE columns: Rank, INSTNM, ROI, then a bare 't' column, "
      "then five year columns headed only 1, 2, 3, 4, 5. Ten ranked rows carry ROI 2.22 down to 0.79 "
      "and five investment amounts each in millions; an ELEVENTH ROW prints nothing but an ellipsis in "
      "every one of the nine cells, and a TWELFTH row is a merged footer, 'Utilization rate of funds in "
      "each year(%)' spanning Rank through t, carrying 99.60 99.79 99.63 99.71 99.69 under the five "
      "year columns. THE TABLE IS A PREFIX OF THE FIFTY-ROW LIST PRINTED IN THE APPENDIX, and the two "
      "versions DISAGREE ON THE 't' COLUMN for all ten rows they share (4 5 3 5 3 6 5 5 6 5 here "
      "against 4 5 3 4 3 5 4 4 5 4 there) while ROI and institution names agree exactly. 't' is never "
      "defined anywhere in the paper, is printed as a single letter, and holds integers 2 to 6; "
      "'INSTNM' is the raw IPEDS variable name used as a header; the five year columns carry neither a "
      "year nor a total; the amounts give no currency. CLOSED BOX with vertical rules between all nine "
      "columns and a horizontal rule between every pair of rows. The caption prints BELOW and the "
      "sentence before it does not name the table: 'Here is a table of top ten schools in the "
      "recommending list ranked by total ROI in five years, including the investment duration.'",
      dict(rows=13, cols=9, merged_cells=True, numeric_cols=8, text_cols=1, width="full",
           continued=False, **BOXED),
      CAPT4, "text-layer",
      cited(17, 17, ["recommending list"], 2,
            lead="Here is a table of top ten schools in the recommending list ranked by total ROI in "
                 "five years"),
      section_kind="result")

# ============================================================ 8: the Gates comparison
table(18, 1, S_TEST,
      "The comparison table for the duplicate-focus test: a header bar 'Rank | INSTNM | Investment "
      "amount (million)' over ten rows, Harvard University 24.14, University of Washington 16.42, "
      "Seattle University 15.80, Yale University 7.50, Texas Tech University 6.96, University of "
      "Michigan 6.85, Land-Grant Universities 4.95, University of Kentucky 4.50, Columbia University "
      "3.78, Stanford University 3.25. CLOSED BOX, rules between every pair of rows and vertical rules "
      "between the three columns; the amounts carry two decimals and align on the point. It exists to "
      "support the claim that the model duplicates nobody's focus, and the test it supports is one-"
      "sided: the paper checks that no Gates school appears in its own list and never checks the "
      "reverse, so a list chosen to avoid those ten names passes by construction. 'Land-Grant "
      "Universities' is printed as if it were one institution, and the column header gives no "
      "currency. Captioned BELOW; referred to after the fact as 'In the table above, we can see that "
      "Gates Foundation invested mostly on those well-known schools like Harvard and Yale.'",
      dict(rows=11, cols=3, merged_cells=False, numeric_cols=2, text_cols=1, width="full",
           continued=False, **BOXED),
      CAPT5, "text-layer",
      cited(18, 18, ["the table above"], 1,
            trail="In the table above, we can see that Gates Foundation invested mostly"),
      section_kind="test")

# ============================================================ 8.1: the sensitivity sweep, over the turn
table(19, 1, S_TEST,
      "The sensitivity sweep on the constant k, and it TURNS THE PAGE: four rows (periods 1 to 4) print "
      "at the foot of p18, the fifth row and the foot row print at the head of p19, so the measured "
      "region holds two of the seven printed rows. Five columns: a 'Year' column holding 1, 2, 3, 4, 5 "
      "- PERIOD INDICES, NOT YEARS - against four change columns headed k minus 10%, k minus 5%, k plus "
      "5% and k plus 10%, all in per cent. CLOSED BOX throughout, rules between every pair of rows and "
      "vertical rules between all five columns. THE CAPTION AND THE CONTENT DO NOT MATCH: it reads "
      "'Table 6: the standard deviation of the investment amount correspond to the change of MRS k', "
      "and the rows are percentage changes of the investment amount under a perturbation of k whose "
      "foot row 'Mean value' carries 10.49% 4.83% 4.80% 11.08% - the arithmetic mean of the five rows "
      "above it in each column, not a standard deviation, and a standard deviation printed beside the "
      "values it summarises would be a different quantity on a different scale. The column change "
      "under k-5% is the smallest everywhere and under k+10% the largest, which is the only pattern the "
      "table carries. Captioned BELOW; referred to afterwards as 'From the table above, we can see that "
      "the influence of k is not very large, and within the range we can bear.'",
      dict(rows=7, cols=5, merged_cells=False, numeric_cols=4, text_cols=1, width="full",
           continued=True, **BOXED),
      CAPT6, "text-layer",
      cited(19, 19, ["the table above"], 1,
            trail="From the table above, we can see that the influence of k is not very large"),
      section_kind="sensitivity")

# ============================================================ appendix: the full fifty
table(23, 1, S_APPX,
      "The full recommending list, ranks 1 to 50, under the title line 'Appendix 1: Recommending "
      "List': the same nine columns as Table 4 (Rank, INSTNM, ROI, a bare 't', then five unlabelled year "
      "columns), ranks 1 to 35 on this page and 36 to 50 with the merged foot row on the next, ROI "
      "falling from 2.22 to 0.02 and ending on a footer 'Utilization rate of funds of each year (%)' "
      "spanning Rank through t with 99.60 99.79 99.63 99.71 99.69. CLOSED BOX with vertical rules "
      "between all nine columns and rules between every pair of rows; two institution names wrap onto "
      "two lines and stay single rows; row 39 prints 'Richard Bland College of the College of William "
      "and Mary' with 'of the College of' repeated. THE TEN ROWS THIS TABLE SHARES WITH TABLE 4 CARRY "
      "DIFFERENT 't' VALUES, and the footer wording differs between the two printings ('in each "
      "year(%)' against 'of each year (%)'), so the appendix is a second, later version of the table "
      "rather than a longer copy of it. Fifteen of the fifty rows invest exactly 0.00 in one or more "
      "years, and thirty-one rows carry at least one zero, which the paper never remarks on. It is the "
      "only exhibit in the paper with a title rather than a caption, and no sentence names it.",
      dict(rows=52, cols=9, merged_cells=True, numeric_cols=8, text_cols=1, width="full",
           continued=True, **BOXED),
      CAPT_APPX, "text-layer", section_kind="appendix")

# ============================================================ the four excluded regions
EXCLUDED.extend([
    {"page": 5, "bbox": REG[(5, 2)], "reason": "split-across-pages",
     "note": "The head of Table 2 - the header bar 'Type and use | Variable' and its first four rows - "
             "which prints at the foot of p5 and turns the page. The table is recorded once, at the "
             "region that carries its caption on p6, and its row count of fourteen covers both halves; "
             "this region would otherwise be a second row for one printed table."},
    {"page": 18, "bbox": REG[(18, 2)], "reason": "split-across-pages",
     "note": "The head of Table 6 - four of its five year rows - printed at the foot of p18 before the "
             "page turn. The table is recorded once at the p19 region that carries its caption, with "
             "the row count covering both halves."},
    {"page": 24, "bbox": REG[(24, 1)], "reason": "split-across-pages",
     "note": "The continuation of the appendix recommending list, ranks 36 to 50 plus the merged "
             "utilization footer, printed after the page turn from p23. Recorded with the p23 region as "
             "one fifty-row table."},
    {"page": 26, "bbox": REG[(26, 1)], "reason": "not-an-exhibit",
     "note": "A fragment of a displayed equation - an equals sign and a square root over two "
             "summations, the square of each constraint below the slack and the square of "
             "min{c_i(x), 0} for the rest. It has no frame, no axes, no caption and no number, and the "
             "left-hand side of the equation is outside the region, so nothing here is an exhibit."},
])

RULES = [
    "Measure first, then read the pixels: sixteen measured regions resolve into five figure rows, "
    "seven table rows and four exclusions, and every region is accounted for once [place.doc_order].",
    "A table can turn the page: Table 2 and Table 6 each print their head on one page and their foot on "
    "the next, and the appendix list runs from p23 to p24, so three measured regions are heads or tails "
    "of a table recorded once elsewhere [table.continued].",
    "A region can hold a piece of a formula rather than an exhibit: the p26 region is an equals sign "
    "and a root over two summations with no frame, no caption and no number [caption.numbering].",
    "Two exhibits that answer one question can disagree: Table 4 and the appendix list share their "
    "first ten institutions and ROIs and print DIFFERENT integers under the undefined column 't' "
    "(4 5 3 5 3 6 5 5 6 5 against 4 5 3 4 3 5 4 4 5 4) [table.numeric_cols].",
    "A caption can name a statistic the table does not print: Table 6 is captioned 'the standard "
    "deviation of the investment amount' and its foot row is the arithmetic MEAN of the five rows above "
    "it (10.49% = (12.18+9.09+10.88+7.64+12.67)/5) [caption.verbatim].",
    "Two stock screenshots can cite one source: Figures 1 and 2 are the same viewer, and the Source "
    "URL printed under the location chart is byte for byte the subject-filtered URL printed under the "
    "subject chart [mention.style].",
    "Headers can be left as variable names: 'INSTNM' stands over the institution column of every "
    "nine-column table, the year columns are headed only 1 to 5 with no year and no unit, and the "
    "column 't' holds integers 2 to 6 that no sentence defines [table.units_in_header].",
    "Citation is thin and always unnumbered at the table: two figure rows are named by a sentence, "
    "Figure 3 only on the page after it prints, and every table is referred to as 'the table above' "
    "or not at all, while Figures 4 and 5, Table 1, Table 2 and the appendix list are named by "
    "nothing [mention.count].",
]

NOTE = """\
Paper 100, Team 47823, a Goodgrant Foundation strategy: rank 2977 colleges, keep 500, fit an ROI
function on earnings and graduation rate, and distribute a five-year budget by a particle-swarm search
under an augmented-Lagrangian constraint. Twenty-seven pages, sixteen measured regions over twelve of
them, resolving into FIVE FIGURE ROWS, SEVEN TABLE ROWS and FOUR EXCLUSIONS, with nothing unaccounted.

THE HEADING INDEX COLLAPSES ON THIS PDF. Its text layer writes one word per line, so every indexed
heading keeps only its first word - 'Data', 'Analysis', 'Results', 'Testing', 'Appendix' - and the
section labels recorded here are those indexed labels verbatim rather than the printed headings, which
are '1 Problem Statement', '4 Data Analysis and Focus Decision', '5.2.4 PCA Results', '8.1 Sensitivity
Analysis' and so on. The same defect empties the caption pass: it finds no caption group in the paper
at all, so every caption in this record was located by hand from its line position on the page.

Table 1 is the notation list - nine symbols from U to lambda,nu - and it defines nothing that the
model later needs to look up: k, the constant that becomes the subject of a whole sensitivity table,
has no row, and neither do the five yearly investment amounts.

Table 2 classifies the IPEDS variables by type and use, and it TURNS THE PAGE: its header and four
rows print at the foot of p5, its other nine rows and its caption at the head of p6. The left column is
three merged group cells, so the horizontal rules break inside the right column only. Variable names
keep their raw database spelling and mostly lose the space before the parenthesis
('UGDS_(the distribution by race)', 'PPTUG_EF(part-time ratio)').

Figures 1 and 2 are stock screenshots from the Foundation Center viewer, watermarked, with every value
printed at the bar end but no axis, no tick, no gridline and no scale on either. Figure 2 charts
recipient locations and prints, as its Source, the same 'subject:all' URL as Figure 1. Both are used to
justify the paper's focus: invest less in Health, Education and Human Services and in New York,
California, DC and Massachusetts.

Figure 3 is a hand-drawn curve of U against x with delta-x and delta-U marked by dashed rectangles and
no ticks, numbers or scale anywhere. Its section says 'We can plot a figure to describe the
relationship:' and does not name it; the figure is first named on the next page.

Figure 4 is a full-page flowchart of the LA_PSA_GT hybrid: fifteen boxes, two nested loops, UNLABELLED
arrows except the two YES/NO pairs, and the Fletcher-Reeves step the text spends pages on collapsed
into one box. Figure 5 is a MATLAB convergence curve titled simply 'fitness', with a floating
'x 10^20' multiplier on the ordinate, no abscissa label at all, and a step-shaped best-so-far trace.
Neither figure is named by any sentence.

Table 3 is the PCA shortlist, ten schools from 32.87 to 20.21, the only table in the paper with a rank
column. Tables 4 to 6 and the appendix list are all closed-box grids in the same style as Tables 1 to
3, which makes the paper's evidentiary tables and its notation list indistinguishable at a glance.

Table 4 prints the first ten rows of the recommending list with an ellipsis row and a merged footer
'Utilization rate of funds in each year(%)' carrying 99.60 99.79 99.63 99.71 99.69. The appendix
prints the same list to fifty rows and repeats the footer with slightly different wording. THE TWO
VERSIONS DISAGREE ON THE 't' COLUMN for all ten shared institutions while agreeing on every ROI, so
one of the two printings reports an integer that the other contradicts. 't' itself is never defined,
holds 2 to 6, and is headed by a bare italic letter.

Table 5 is the Gates comparison: ten well-known schools with Gates amounts, used to claim the model
duplicates nobody's focus. The check runs one way only - no Gates school appears in the model's list -
so the test passes by construction. 'Land-Grant Universities' is listed as though it were one college.

Table 6 is the k-sensitivity sweep and its caption is wrong: it says 'the standard deviation of the
investment amount', and the foot row is the plain mean of the five rows above it in each column. Its
'Year' column holds 1 to 5 - period indices, not years. It also turns the page, printing four rows on
p18 and two on p19.

The appendix list is titled rather than captioned ('Appendix 1: Recommending List'), is named by no
sentence, prints row 39 as 'Richard Bland College of the College of William and Mary' with the phrase
repeated, and has thirty-one of its fifty rows investing exactly 0.00 in at least one year.

Families: bar 2, line 2, flowchart-or-schematic 1, table-grid 7.
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

out = PROXY / "pc100-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
