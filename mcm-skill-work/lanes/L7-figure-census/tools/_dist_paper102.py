"""Hand census of P-C-2016-52815-2e6f0093 (Team 52815, 18 pages, 9 measured regions).

A Bayesian Goodgrant paper: impute the missing IPEDS columns, regress a Goodness score on price and
enrolment, roll the coefficients forward five years, then allocate money by an iterative hill-climb.
Nine measured regions resolve into SIX FIGURE ROWS and THREE EXCLUSIONS, with nothing unaccounted.

  p1  r1  --         excluded         the paper's prose summary set as one full-page raster
  p5  r1  Figure 1   heatmap-or-contour  the missingness matrix, ~2000 observations x ~200 variables
  p8  r1  Figure 2   scatter          change in log GDP against change in unemployment, OLS line
  p10 r1  Figure 3   scatter          normal Q-Q of the main model
  p10 r2  Figure 4   scatter          residuals against fitted values
  p11 r1  Figure 5   scatter          actual against fitted values
  p12 r1  Figure 6   line             the two-school funding example, two panels side by side
  p12 r2  --         excluded         panel (b) of the same Figure 6; one row cannot become two
  p12 r3  --         excluded         the 'Algorithm 1' pseudocode listing

TWO PRINTED TABLES HAVE NO MEASURED REGION AT ALL and are declared gaps: Table 1 (p14 into p15) and
Table 2 (p15 into p16), both unruled text columns of eight columns.

THE TWO RESIDUAL DIAGNOSTICS MAKE OPPOSITE CLAIMS ABOUT ONE QUANTITY: p9 reads Figure 4 as showing
variance DECREASING with the fitted value and Figure 5 as showing error INCREASING with it.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2016-52815-2e6f0093"
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
            variables: int = 0) -> dict:
    return {"verbatim": schema.norm(verbatim), "numbering": f"{kind} N:",
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


S_21 = [head(4, "2.1 Data Gathering")]
S_32 = [head(6, "3.2 Contribution to GDP")]
S_35 = [head(9, "3.5 Analysis of Linear Model Assumptions")]
S_41 = [head(11, "4.1 Minimal Equivalent Example")]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
for _group in (S_21, S_32, S_35, S_41):
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


CAP1 = caption("Figure 1: Initial Missingness Structure of Data")
CAP2 = caption("Figure 2: Regression of ∆ logGDP vs ∆ Unemployment")
CAP3 = caption("Figure 3: Q-Q Plot for Main Model")
CAP4 = caption("Figure 4: Residual vs Predicted Plot for Main Model")
CAP5 = caption("Figure 5: Actual vs Predicted Plot for Main Model")
CAP6 = caption("Figure 6: 2D Example of Optimizing Funding Distribution")

# ============================================================ 2.1: the missingness matrix
figure(5, 1, "heatmap-or-contour", CAP1, "text-layer",
       cited(4, 5, ["Figure 1"], 2,
             lead="Figure 1 shows the initial missingness structure",
             trail="In Figure 1, the x axis represents cases, the y variables"),
       S_21,
       "The MI package's missingness matrix: about 2000 observations down the ordinate against about 200 "
       "variables across the abscissa, red for present and black for missing, with an in-frame title "
       "'Dark represents missing data', axis labels 'Observation Number' and 'Standardized Variable', a "
       "subtitle 'Clustered by missingness' and a COLOUR BAR OUTSIDE THE RIGHT EDGE ticked 0, 5, 10, 15 "
       "and 20. THE TWO ENCODINGS CONTRADICT EACH OTHER: the title says the colour is binary (dark = "
       "missing) while the colour scale is continuous from 0 to 20 and carries no label, no unit and no "
       "statement of what the number counts, and the panel itself prints no tick labels on the ordinate "
       "below 500 and none at all on the top axis. THE VARIABLE NAMES ARE UNREADABLE BY DESIGN - 200 "
       "labels rotated 90 degrees and overlapping - and the paper concedes it, 'the names of which are "
       "not intended to be legible'. THE CITING SENTENCE SWAPS THE AXES: p4 reads 'the x axis represents "
       "cases, the y variables' while the chart prints observation number on the y axis and the "
       "standardised variables on the x. Three structures are visible and the prose names them one by "
       "one (a solid black band across the top rows, a black block over the SAT/ACT columns for "
       "observations 900 to 2000, and a striped black block at the right). THE CAPTION PASS WELDED A "
       "BODY SENTENCE TO IT: the caption group reads 'Figure 1: Initial Missingness Structure of Data "
       "either to public or private schools and is rectified in the python script.', whose tail belongs "
       "to the sentence starting 'On the right, a strange missingness pattern is observed, but this is "
       "due to the factors applying' on the previous page; the verbatim recorded here is the caption "
       "line alone, and the caption prints BELOW.",
       geometry("heatmap-or-contour", colorbar=True, labels=True), "1", section_kind="model")

# ============================================================ 3.2: the GDP regression
figure(8, 1, "scatter", CAP2, "text-layer",
       cited(8, 8, ["Figure 2"], 1,
             lead="See in Figure 2 a scatterplot of the chart with regression line plotted."),
       S_32,
       "Seventy-odd hollow circles with a red least-squares line across the frame, 'Change in "
       "Unemployment' from -2 to 3 on the abscissa against 'Change in logGDP' from -0.03 to 0.08 on the "
       "ordinate. Both axes are named, there is no gridline, no colour, no legend and no marker "
       "distinguishing any observation. THE FIT IS ASSERTED, NOT REPORTED: no R squared, no slope, no "
       "intercept, no residual standard error and no sample size is printed on the figure or in the "
       "sentence that reads it, which says only 'The model fit looks surprisingly good.' The band is "
       "wide - at a change in unemployment of -0.9 the points run from 0.015 to 0.082 - and one point at "
       "(-0.9, 0.082) sits four times the typical residual above the line, while the line itself is "
       "drawn out to both frame edges beyond where any observation lies. Caption prints BELOW, cleanly, "
       "and the citing sentence FOLLOWS the figure on the same page.",
       geometry("scatter", labels=True), "2", section_kind="model")

# ============================================================ 3.5: the three diagnostics
figure(10, 1, "scatter", CAP3, "text-layer",
       cited(9, 10, ["Figure 3"], 1,
             lead="We first consider a normal Quantile-Quantile Plot (Figure 3)."),
       S_35,
       "A normal Q-Q plot of the main model, in-frame title 'Normal Q-Q Plot', 'Theoretical Quantiles' "
       "against 'Sample Quantiles' from about -1.6 to 3.2 and -1.6 to 3.1, drawn as small hollow circles "
       "with no reference line. THE ABSENCE OF THE 45-DEGREE LINE IS THE WHOLE POINT: a Q-Q plot is read "
       "against the straight line a normal sample would follow, and without it the systematic S-shape - "
       "flat through the middle, rising steeply past a theoretical quantile of 1.5 and flattening below "
       "-0.6 - cannot be measured at all, and the two rightmost circles come away from the body of the "
       "trend with no scale on the plot to say by how much. The citing sentence is the paper's own "
       "verdict and it "
       "is generous in both directions: 'It does not look perfectly normal, contrary to the assumptions "
       "which lead to our posterior estimates, but it is close enough.' Caption prints BELOW; the "
       "sentence naming it is on the PREVIOUS page.",
       geometry("scatter", labels=True), "3", section_kind="evaluation")

figure(10, 2, "scatter", CAP4, "text-layer",
       cited(9, 10, ["Figure 4"], 1,
             lead="This predicted versus residual plot is more worrisome (Figure 4)."),
       S_35,
       "Residuals against fitted values, dense cloud of small hollow circles, both axes labelled with "
       "RAW R OBJECT NAMES: 'ypred' on the abscissa from 1 to 8 and 'resids' on the ordinate from -1.5 "
       "to 3, neither capitalised, neither given a unit, and no zero line drawn although the whole "
       "reading of the plot depends on where zero is. The cloud is a funnel: near a fitted value of 1.5 "
       "the residuals span roughly -0.5 to 1.9 and by 3.5 roughly -0.25 to 0.8, with three stray points "
       "far out at about (4.6, -1.3), (5.5, 2.9) and (7.7, -0.75). THE CITING SENTENCE AND THE FIGURE "
       "AFTER IT CLAIM "
       "OPPOSITE THINGS ABOUT THE SAME QUANTITY: p9 reads this plot as 'We actually see a decrease in "
       "variance as the predicted value increases' and then reads Figure 5, drawn from the same two "
       "columns, as 'The error of the prediction seems to increase as the predicted value increases'. "
       "Both plots show the spread narrowing as the fitted value rises; the second sentence contradicts "
       "the first about one dataset in consecutive paragraphs. Caption prints BELOW, and the caption "
       "says 'for Main Model' without saying which model that is beyond the section number.",
       geometry("scatter", labels=True), "4", section_kind="evaluation", order=2)

figure(11, 1, "scatter", CAP5, "text-layer",
       cited(9, 11, ["Figure 5"], 1,
             lead="The error of the prediction seems to increase as the predicted value increases "
                  "(Figure 5)."),
       S_35,
       "The third diagnostic in a row, actual against fitted: 'ypred' from 1 to 8 across the abscissa "
       "and a bare 'y' from 0.5 to 7.5 up the ordinate, again raw R names with no units. NO IDENTITY "
       "LINE IS DRAWN, so an 'Actual vs Predicted Plot' - the caption's words - prints nothing against "
       "which the prediction can be judged; a reader cannot see whether the model over- or "
       "under-predicts, only that the fitted values are confined to 1.2 to 3.5 while the actual values "
       "run to 7.1. Most points jam into the corner at 1.2 to 1.8. A dozen or so sit above the body of the "
       "cloud, at (2.2, 4.4), (2.5, 4.35), (2.9, 4.05), (3.0, 4.4), (3.2, 5.0), (4.6, 2.85) and "
       "(5.5, 6.4), and the last point prints at (7.7, 7.1) on the far corner of the frame. The citing sentence says the error "
       "increases with the fitted value, which the funnel of Figure 4 contradicts; the paper reads this "
       "as 'This plot again serves as evidence against this model the most correct.', a sentence with "
       "two grammars in it and no referent for either. Caption prints BELOW; the naming sentence is TWO "
       "pages back.",
       geometry("scatter", labels=True), "5", section_kind="evaluation", order=3)

# ============================================================ 4.1: the two-school example
figure(12, 1, "line", CAP6, "text-layer",
       cited(11, 12, ["Figure 6"], 1,
             lead="Consider an example (see Figure 6) in which we have only two schools competing"),
       S_41,
       "Two curves side by side, both plotting Goodness against 'Effective Tuition (Thousands of "
       "Dollars)' on identical axes (ordinate -0.5 to 2.5, abscissa -0.2 to 2.8), each carrying a blue "
       "dot at the starting tuition, a red dot at the disbursed tuition and two violet annotation boxes "
       "'Change in Funding' and 'Change in Goodness'. The left curve is steep - it crosses zero at about "
       "0.35 and reaches 1.78 by a tuition of 2.0 - and the right curve saturates near 1.0 to 1.2 over "
       "the same interval, which is the whole point of the example and does read correctly. WHAT IS "
       "MISSING IS THE LABELLING: neither panel carries an (a) or a (b), neither panel names School A or "
       "School B, and the caption mentions neither, so the reader has to infer from the citing prose "
       "that the steep graph is School A and the flat one School B - and the prose locates them as 'the "
       "school on the left' and 'the school on the right', which is the only cue in the paper. The left "
       "panel's funding annotation is set as a horizontal line under the curve labelled 'Changing "
       "Funding' while the right panel's reads 'Change in Funding', the same annotation in two tenses, "
       "and neither states the 0.75-to-2.0 span the prose calls 'a disbursement of 1.3 thousand "
       "dollars'. THE CAPTION PASS WELDED A BODY SENTENCE TO IT AGAIN: the group reads 'Figure 6: 2D "
       "Example of Optimizing Funding Distribution each iteration until all our funds are depleted.', "
       "whose tail belongs to the sentence '... we iteratively check which school would most benefit "
       "from a small disbursement until we have exhausted our funds.'; the verbatim recorded here is the "
       "caption line alone. Caption prints BELOW the pair.",
       geometry("line", panels=2, layout="1x2", labels=True), "6", section_kind="model")

# ============================================================ the refusals
EXCLUDED.append({
    "page": 1, "bbox": REG[(1, 1)], "reason": "not-an-exhibit",
    "note": "The paper's summary of the model, set as ONE FULL-PAGE RASTER: the page carries no text "
            "layer at all and the image is fifteen paragraphs of running prose about the Bayesian "
            "multi-stage model, with no table, no chart, no formula box and no number. It is prose that "
            "happens to be a picture, not an exhibit.",
})

EXCLUDED.append({
    "page": 12, "bbox": REG[(12, 2)], "reason": "fragment-of-other",
    "note": "The second panel of Figure 6. The two measured regions of p12 sit on the same ordinate "
            "band, one from x = 110 to 943 and one from x = 769 to 1594, i.e. the left and right halves "
            "of one two-panel figure whose one caption, 'Figure 6: 2D Example of Optimizing Funding "
            "Distribution', prints under the pair. The figure is recorded once as a two-panel row; this "
            "region holds the flatter curve, School B.",
})

EXCLUDED.append({
    "page": 12, "bbox": REG[(12, 3)], "reason": "not-an-exhibit",
    "note": "The 'Algorithm 1' pseudocode listing under 4.3: eleven lines of set-up and loop body "
            "between two horizontal rules, with hyphens standing in for an indent that the LaTeX run "
            "never produced and no vertical rules at all. Its body is ordinary text, so it is a "
            "printed listing rather than an exhibit; the paper's own display of the loop is the only "
            "one it has, and it is recorded here so the region is not simply dropped.",
})

RULES = [
    "Measure first, then read the pixels: nine measured regions resolve into six figure rows and three "
    "refusals, and every region is accounted for once [place.doc_order].",
    "A figure can be two measured regions: p12's two regions are the left and right panels of one "
    "two-panel figure with no (a)/(b) labels and no school names, so the second is an exclusion rather "
    "than a row of its own [geometry.panel_count].",
    "A caption group can carry a body sentence welded to its tail: Figures 1 and 6 both do, and the "
    "recorded verbatim is the caption line alone with the weld spelled out in the row note "
    "[caption.verbatim].",
    "The caption pass cannot see what the figure prints: the citing sentence says the missingness "
    "matrix puts cases on the x axis, and the chart prints observations on the y [mention.lead_sentence].",
    "Two diagnostics of one model can be read in opposite directions in consecutive paragraphs - "
    "Figure 4 as variance decreasing, Figure 5 as error increasing - and neither plot carries the "
    "reference line that would settle it [geometry.shared_axes].",
    "A chart can print its axes as raw software object names: Figures 4 and 5 label them 'ypred', "
    "'resids' and 'y' with no unit and no capitalisation [geometry.data_labels].",
    "A colour scale can contradict its own title: Figure 1 says dark means missing and then prints a "
    "continuous 0-to-20 colour bar with no label [geometry.colorbar].",
    "Two printed tables have no measured region at all - Table 1 and Table 2, both unruled text columns "
    "that run from one page to the next - so neither can become a row, neither carries a mention record, "
    "and both are declared gaps in the note [mention.count].",
]

NOTE = """\
Paper 102, Team 52815: a Bayesian multi-stage model of Goodgrant funding. Majors are matched to
job counts and unemployment, the economy-wide job total is regressed on GDP change, each school gets a
Goodness score from price and enrolment, the posteriors are rolled forward five years, and money is
allocated by iterating the school with the largest Goodness gain per dollar. Eighteen pages, nine
measured regions over six of them, resolving into SIX FIGURE ROWS and THREE EXCLUSIONS, with nothing
unaccounted.

Figure 1 is the missingness matrix from the R MI package: about 2000 observations against about 200
variables, red for present and black for missing, with an in-frame title 'Dark represents missing data'
and a colour bar ticked 0 to 20 that contradicts it. The variable names are printed rotated and
overlapping, and the paper says so: 'the names of which are not intended to be legible'. The sentence
that describes the chart swaps its axes - 'the x axis represents cases, the y variables' - against a
chart that puts Observation Number on the y axis.

Figure 2 is the GDP regression: seventy-odd hollow circles and a red line, axes named, and no statistic
of any kind printed. The prose asks the reader to accept 'The model fit looks surprisingly good' on the
strength of the picture alone.

Figures 3, 4 and 5 are the linear-model diagnostics, and all three are missing the one reference each
needs. The Q-Q plot has no 45-degree line, so its S-shape cannot be measured, and the paper calls it
'close enough'. The residual-versus-fitted plot has no zero line and raw R axis names ('ypred',
'resids'), and the actual-versus-predicted plot has no identity line and axes named 'ypred' and 'y'.
Worse, consecutive paragraphs read the last two in opposite directions: Figure 4 is said to show
variance DECREASING with the fitted value and Figure 5, drawn from the same columns, is said to show
error INCREASING with it.

Figure 6 is the minimal example: two Goodness curves on identical axes, the steep one School A and the
flat one School B, with violet annotation boxes for the funding and Goodness changes. It reads correctly
and carries no panel letters and no school names, so only the prose identifies which curve is which,
and the two panels print the same annotation as 'Changing Funding' and 'Change in Funding'.

Two printed exhibits have no measured region at all. Table 1 (7 Results from Model) prints
'Schools | Year One .. Year Five | Total | ROI' as unruled text columns with the caption above, starts
at the foot of p14 and runs onto p15, and caps every school's five-year total near 50,000,000 - the
two rows it prints on p14 both land just over the cap, at 50,017,570 and 50,011,398.
Table 2, the unconstrained model, starts on p15 and runs onto p16: it lets Georgia Perimeter College
take 220,954,796 over the five years and prints its ROI to four decimals, where Table 1 prints three,
and its first nine printed ROI values lie inside 92.5848 to 92.5870 while Table 1's run from 145.520
down to 2.585. Every row's Total in both tables that was checked is the exact sum of its five years.
Both captions print
ABOVE and both tables are declared gaps here because neither produced a measured region.

Families: scatter 4 (Figures 2, 3, 4, 5), heatmap-or-contour 1, line 1.
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

out = PROXY / "pc102-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
