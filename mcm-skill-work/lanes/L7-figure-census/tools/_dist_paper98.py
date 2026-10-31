"""Hand census of P-B-2016-52221-f8094e57 (Team 52221, 23 pages, 21 measured regions).

A space-insurance / active-debris-removal paper. Twenty-one measured regions resolve into FOURTEEN
FIGURE ROWS, SIX TABLE ROWS and ONE EXCLUSION.

  p3  r3  Figure 1   scatter                debris shell over a blue planet disk, no axes
  p3  r2  Figure 2   scatter                elongated dot cloud around a filled black disk, no axes
  p4  r1  Table 1    table-grid             the notation list, 2 by 21, booktabs, caption ABOVE
  p5  r1  Figure 3   flowchart-or-schematic the business model, keyed by arrow colour
  p7  r1  Figure 4   photo-or-raster-image  a screenshot of the DAS input dialog, no plot on it
  p8  r1  Figure 5   line                   five diameter series, log impacts against altitude
  p11 r1  Figure 6   line                   one premium-rate curve, title in lower case in frame
  p12 r1  Figure 7   flowchart-or-schematic THE SAME diagram as Figure 3 plus red ticks and queries
  p14 r1  --         table-grid             small-debris judge matrix, 5 by 5
  p14 r2  --         table-grid             medium and large matrices STACKED in one region, 5 and 3
  p15 r1  --         table-grid             judge matrix, 5 by 5
  p15 r2  --         table-grid             judge matrix, 5 by 5
  p15 r3  --         table-grid             judge matrix, 4 by 5, the Microsatellite row dropped
  p16 r1  Figure 8   line                   five diameter series, log impacts against starting date
  p16 r2  Figure 9   line                   one altitude-800 curve under a plural "Contours" title
  p17 r1  Figure 10  line                   one altitude-400 curve, the same plural title
  p18 r1  Figure 11  line                   one altitude-2000 curve, the same plural title
  p19 r1  Figure 12  line                   four curves legended "data 7%" to "data 10%"
  p19 r2  Figure 13  line                   four duration curves 3, 5, 7 and 9 years
  p22 r1  --         flowchart-or-schematic the executive-summary repeat of Figure 3, NO CAPTION

  p3  r1  excluded   fragment-of-other      the container that boxes Figures 1 and 2 together

Only five of the fourteen figure rows are named by a sentence, and one of those five names a figure
that prints four pages later. Figures 8 to 13, the two opening illustrations, Table 1 and all six
matrices carry no citation.

THE SCHEMATIC IS PRINTED TWICE. Figure 3 and Figure 7 are the same box-and-arrow diagram; Figure 7
adds red check marks and red question marks that nothing in the paper keys, and the executive summary
prints the same diagram a third time on p22 with no caption at all.

THE ONE EXHIBIT SHOWING THE SOFTWARE SHOWS A FORM. Figure 4 is a screenshot of the DAS input dialog
with a pending request for an altitude-impact plot that was never drawn; several of its widget labels
are truncated mid-word ("Duratio", "Inclinat", "Type of") and the environment value is misspelled.

NINE AXIS LABELS SAY "log" AND NO AXIS IS LOGARITHMIC in the sense a reader can check: the ticks are
evenly spaced numbers, so the reader is shown the log of the data but never the ruler it was taken on.

ONE MEASURED REGION HOLDS TWO TABLES. On p14 the second matrix region boxes a five-row matrix and,
under it, a three-row matrix with the header repeated and the Microsatellite row dropped; a census
that records one region as one row cannot split it.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2016-52221-f8094e57"
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


def place(page: int, reg: int, kind: str, path: list[str], order: int = 1,
          numbered: bool = True) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": numbered,
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


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below",
            variables: int = 0, sentences: int = 1) -> dict:
    """Caption block. `verbatim` is what the page prints under the exhibit."""
    return {"verbatim": schema.norm(verbatim), "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": sentences, "units": False,
            "variables": variables > 0, "variable_count": variables,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def no_caption() -> dict:
    """The block for an exhibit that prints no caption at all: the six matrices and p22."""
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


S_11 = [head(3, "1 Introduction"), head(3, "1.1 Background")]
S_13 = [head(4, "1.3 Symbol Description")]
S_2 = [head(5, "2 Commercial Opportunity")]
S_32 = [head(6, "3 Space Debris Distribution Rule"), head(6, "3.2 ORDEM2000")]
S_331 = [head(6, "3 Space Debris Distribution Rule"),
         head(7, "3.3.1 General Rule of Space Debris Distribution")]
S_52 = [head(10, "5 Premium Rate"), head(11, "5.2 Improved Model")]
S_6 = [head(12, "6 Strategy of ADR")]
S_622 = [head(13, "6.2 Second Step: Fuzzy Comprehensive Evaluation"),
         head(13, "6.2.2 Implementation of Fuzzy Comprehensive Evaluation")]
S_7 = [head(15, "7 The Impact of Insurance Duration")]
S_8 = [head(16, "8 Model Implementation and Economy Validation")]
S_9 = ["9 What If and Sensitive Analysis"]
S_8N = ["未编号标题 Executive Summary"]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
_KNOWN |= {schema.norm(h["title"]) for h in CTX["headings"] if h.get("title")}
_PRINTED = schema.printed_lines(PID)
for _group in (S_11, S_13, S_2, S_32, S_331, S_52, S_6, S_622, S_7, S_8):
    for _label in _group:
        if schema.norm(_label) not in _KNOWN and schema.norm(_label) not in _PRINTED:
            raise SystemExit(f"section label is neither an indexed heading nor a printed line: "
                             f"{_label!r}")
if schema.norm(S_9[0]) not in _PRINTED:
    raise SystemExit("the section 9 heading is not a printed line")

# The printed captions. Figures 1 and 2 carry a second-hand source tag; 5 and 8 to 13 are bare
# labels with no describing text at all; the six matrices carry nothing.
CAP1 = caption("Figure 1: Debris in Low Earth Orbit [3]")
CAP2 = caption("Figure 2: Debris in High Earth Orbit [3]")
CAPT1 = caption("Table 1: Notation", numbering="Table N:", position="above")
CAP3 = caption("Figure 3: Model Schematic Diagram")
CAP4 = caption("Figure 4: DAS")
CAP5 = caption("Figure 5", numbering="Figure N")
CAP6 = caption("Figure 6: Premium Rate Model")
CAP7 = caption("Figure 7: Model Schematic Diagram")
CAP8 = caption("Figure 8", numbering="Figure N")
CAP9 = caption("Figure 9", numbering="Figure N")
CAP10 = caption("Figure 10", numbering="Figure N")
CAP11 = caption("Figure 11", numbering="Figure N")
CAP12 = caption("Figure 12", numbering="Figure N")
CAP13 = caption("Figure 13", numbering="Figure N")

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_block: dict, cap_src: str, mention: dict,
           section: list[str], note: str, geo: dict | None = None, number: str = "",
           section_kind: str = "other", confidence: str = "high", order: int = 1,
           numbered: bool = True) -> None:
    ITEMS.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)], "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap_block["verbatim"],
        "caption": cap_block, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section, order, numbered),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    })


def table(page: int, reg: int, section: list[str], note: str, spec: dict,
          cap_block: dict | None = None, cap_src: str = "none",
          section_kind: str = "other", order: int = 1) -> None:
    block = cap_block or no_caption()
    TABLES.append({
        "page": page, "bbox": REG[(page, reg)], "kind": KIND[(page, reg)],
        "family": "table-grid", "caption_source": cap_src,
        "caption_verbatim": block["verbatim"], "caption": block, "table": spec,
        "place": place(page, reg, section_kind, section, order),
        "mention": uncited(), "note": note, "confidence": "high",
    })


# ============================================================ 1.1: the two copied illustrations
figure(3, 3, "scatter", CAP1, "text-layer", uncited(), S_11,
       "A pale blue-lavender filled circle with darker specks printed inside it, wrapped in a thick "
       "shell of dense black dots that bands solid along the top and lower rim and thins to a "
       "near-white crescent at the upper right, with a sparse white halo and a faint vertical column "
       "of dots outside it. NO AXES, no ticks, no scale, no altitude reference, no hemisphere "
       "reference, no title, no legend, no label of any kind - the picture asserts 'Low Earth Orbit' "
       "through its caption alone, and nothing on the drawing says how high the shell is, how thick "
       "it is or what the vertical column is. Two mark classes are mixed without a key: the blue disk "
       "is a flat graphic rather than an Earth image, and whether its colour is background or data "
       "cannot be told. The asymmetric density of the shell (an orbital-inclination effect, if it is "
       "one) is unexplained, and the crescent gap at the upper right reads either as a physical void "
       "or as a rendering defect. It is a redrawn second-hand illustration, tagged [3] in the caption "
       "and nowhere else, and at print size the fine dots coalesce into solid black banding.",
       geometry("scatter"), "1", section_kind="introduction", order=1)

figure(3, 2, "scatter", CAP2, "text-layer", uncited(), S_11,
       "The right-hand panel of the same pair: an elongated lens-shaped cloud of thousands of small "
       "black dots running left to right with a sparse halo of outliers, a solid filled black disk at "
       "its centre, concentric arc ribbons and chord lines sweeping to the two ends, and a few faint "
       "straight streaks crossing the left lobe. NO AXES, no ticks, no scale, no altitude reference, "
       "no title, no legend, no callout. The central solid disk is a different mark class from the "
       "surrounding dots and nothing names it, so the one feature that would carry the 'High Earth "
       "Orbit' claim - Earth, or a dense cluster - is unlabelled; the concentric ribbons look like "
       "drawn guide curves rather than data, so two mark types are mixed again with no distinction. "
       "The two panels are printed inside a single vector container that boxes them together, and the "
       "left panel is the only one of the two whose planet is drawn; the pair therefore reads as one "
       "exhibit, with the panel split marked by nothing but position.",
       geometry("scatter"), "2", section_kind="introduction", order=2)

# ============================================================ 1.3: the notation table
table(4, 1, S_13,
      "The notation list as a two-column, twenty-one-row grid: a header row 'Symbol | Meaning' and "
      "twenty body rows from q (expected value of debris) through Mt (target mass), every one of them "
      "a symbol against a noun phrase and not one of them carrying a value, a unit or a default. "
      "Ruling: a thin rule above the header, a heavy rule under it and a thin rule at the foot, with "
      "no vertical rule, no interior row rule and no box - the booktabs shape - and the symbol column "
      "right-aligned against a meaning column that starts flush at one x position, so the symbols "
      "line up on their right edges while their glyph heights differ. The caption prints ABOVE the "
      "table, 'Table 1: Notation', which makes it the only exhibit in the paper whose caption sits "
      "above its exhibit; NO SENTENCE NAMES IT, and section 1.3 prints the heading and then the table "
      "and nothing else. Twenty-one rows of notation for a paper whose remaining exhibits print nine "
      "axis labels between them is the paper's one careful piece of typography.",
      {"rows": 21, "cols": 2, "header_rows": 1, "rule_style": "booktabs", "zebra": False,
       "merged_cells": False, "diagonal_header": False, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 0, "text_cols": 2, "width": "full",
       "orientation": "portrait", "continued": False, "note_sentence": ""},
      CAPT1, "text-layer", section_kind="symbols")

# ============================================================ 2: the business-model schematic
figure(5, 1, "flowchart-or-schematic", CAP3, "text-layer",
       cited(1, 5, ["fig.3", "Figure3"], 2,
             "The structure of whole service is demonstrated in fig.3"),
       S_2,
       "A block diagram rather than a chart: eight navy-bordered boxes - Insurance Duration (Time), "
       "Space Debris Distribution Rule, Probability of Collision before ADR (Risk), Strategy of ADR, "
       "Premium Rate, ADR Cost, Owner of spacecraft, Our Company - joined by filled arrows in two "
       "colours, orange-brown for money and navy for determination, with a two-line key at mid-left "
       "('fund flow', 'determine') and three edge labels, 'Premium(Income)', 'Claims' and 'Cost'. NO "
       "AXES, no tick, no number, no rate, no currency and no period appears anywhere on it, so the "
       "'model' the caption names is purely qualitative: it states which box feeds which and nothing "
       "about magnitude. MEANING IS CARRIED BY ARROW COLOUR ALONE, so in greyscale the two classes of "
       "edge collapse into one and the diagram says both that money flows and that one box determines "
       "another along the same lines. 'Premium(Income)' and 'Claims' sit tight against their shafts "
       "and are easy to attach to the wrong direction, and the left chain terminates at 'Owner of "
       "spacecraft' with no keyed flow entering it. It is named on p1, four pages before it prints, by "
       "'The structure of whole service is demonstrated in fig.3', and again on p6 as 'Figure3'.",
       geometry("flowchart-or-schematic", legend="inside"), "3", section_kind="model")

# ============================================================ 3.2: the software screenshot
figure(7, 1, "photo-or-raster-image", CAP4, "text-layer",
       cited(7, 7, ["figure 4"], 1,
             "The Debris Assessment Software (DAS) is a software based on ORDEM 2000, its operation "
             "interface is shown in figure 4"),
       S_32,
       "A screenshot of a Win32 application window, not a data exhibit: green title bar reading 'DAS "
       "- project - [Science and Engineering Utilities]', menu bar, toolbar, a tab strip with "
       "'Science and Engineering' selected, a tree pane listing six utilities and an open dialog "
       "'Debris Impacts vs. Orbit Altitude' holding Start 2016 yr, Duratio 10 yr, Avg. S/C "
       "X-Sectional 1 m^2, Inclinat 28.5 deg, a combo reading 'Meteroids & Orbital', an impactor-"
       "diameter list of 2, 5, 10 and 15 cm, two plot-type radio buttons, and the buttons Plot, Reset "
       "and Help. NO PLOT IS DRAWN: the exhibit shows the form that would request an altitude-impact "
       "plot, with the request still pending, so the figure supports no number in the paper and the "
       "claim it is cited for - that DAS gives the debris distribution - rests on the citation, not "
       "on the picture. Four widget labels are truncated mid-word by their own layout ('Duratio', "
       "'Inclinat', 'Type of', and both radio labels clipped to 'Orbital Al' and 'Orbital A'), the "
       "environment value is misspelled ('Meteroids'), the diameter list box is clipped by its "
       "scrollbar, and which plot the highlighted option would produce is not decidable. It is the "
       "only low-resolution raster in the paper and the only exhibit whose content is a program's "
       "chrome rather than its output.",
       geometry("photo-or-raster-image"), "4", section_kind="model")

# ============================================================ 3.3.1: flux against altitude
figure(8, 1, "line", CAP5, "text-layer",
       cited(7, 8, ["Figure 5"], 1,
             "Figure 5 indicates the number (per year) of debris impacts, of each impactor size we "
             "expected"),
       S_331,
       "Five solid curves - dark red, salmon, olive, blue, green - over 'Altitude (km)' graduated 200 "
       "to 1800 in steps of 400 with the axis label set in two lines past the end of the axis, "
       "against 'log(Number of Impacts)' running minus 1.0 to minus 7.5 downward. The legend is "
       "outside the frame at the upper right and overhangs its border, with five entries that number "
       "the series and give the size: '01 Diameter: 0.20 (cm)' through '05 Diameter: 10.00 (cm)'. A "
       "boxed annotation inside the plot area records Start Year 2016.00 yr, Duration 1.00 yrs, "
       "Inclination 28.50 deg, C-S Area 1.00 m^2, Environment Orbital Debris Only. THERE IS NO "
       "TITLE and the caption is the bare label 'Figure 5': the only sentence that points at it, on "
       "the preceding page, says it 'indicates the number (per year) of debris impacts, of each "
       "impactor size we expected' and names no axis. The ordinate is labelled 'log' but graduated in "
       "evenly spaced numbers from minus 1 to minus 7.5, so the reader is shown the log of the counts "
       "and never the counts; every tick is negative, which means the axis plots a quantity smaller "
       "than one over its whole range.",
       geometry("line", legend="outside-right"), "5", section_kind="model")

# ============================================================ 5.2: the premium-rate curve
figure(11, 1, "line", CAP6, "text-layer",
       cited(11, 11, ["Figure 6"], 1,
             "Figure 6 shows how premium rate changes with the failure rate"),
       S_52,
       "One dark-blue concave curve, rising and then flattening, over 'probability of collision' "
       "graduated 1 to 10 with NO ZERO TICK and a detached 'x 10^-4' printed below the right end of "
       "the axis rather than at its label, against 'insurance premium rate of our model' graduated "
       "0.02 to 0.06. The in-frame title is 'premium rate model', in lower case, while the caption "
       "prints 'Figure 6: Premium Rate Model' in title case - the same three words in two casings on "
       "one exhibit. No legend and no series identity, which is correct for a single curve, and no "
       "value printed on the line. The sentence that cites it names a different abscissa from the one "
       "the exhibit draws: 'Figure 6 shows how premium rate changes with the failure rate' against an "
       "axis labelled 'probability of collision', and the equation printed immediately above the "
       "figure, alpha = (8 + log10 beta-hat)/100, is written in the failure rate.",
       geometry("line"), "6", section_kind="model")

# ============================================================ 6: the same schematic, annotated
figure(12, 1, "flowchart-or-schematic", CAP7, "text-layer",
       cited(12, 12, ["fig.7"], 1, "This is shown in fig.7"),
       S_6,
       "THE SAME DIAGRAM AS FIGURE 3 - the same eight boxes, the same two-colour arrows, the same "
       "mid-left key 'fund flow' and 'determine', the same edge labels 'Premium(Income)', 'Claims' and "
       "'Cost' - printed again seven pages later with one addition: SIX RED MARKS in the margin of the "
       "edges. Three red check marks sit on the Debris Distribution to Probability, Probability to "
       "Premium Rate and Debris Distribution to Premium Rate paths, and three red question marks on "
       "the Insurance Duration to Debris Distribution, the Debris Distribution to Strategy of ADR fork "
       "and the Strategy of ADR to ADR Cost edges. Nothing in the paper, before or after, says what a "
       "tick or a query means on this diagram, so the second printing adds a judgement the original "
       "did not make and gives the reader no way to read it; the same colour-only key means both "
       "printings collapse in greyscale. The thick 'Premium(Income)' arrow is drawn double-headed "
       "under a single label and runs through its own text. Two captions in the paper are identical "
       "word for word, 'Figure 3: Model Schematic Diagram' and 'Figure 7: Model Schematic Diagram', so "
       "the pair is told apart by its number alone.",
       geometry("flowchart-or-schematic", legend="inside"), "7", section_kind="solution")

# ============================================================ 6.2.2: the six judge matrices
_MAT = {"rows": 5, "cols": 5, "header_rows": 1, "rule_style": "booktabs", "zebra": False,
        "merged_cells": False, "diagonal_header": False, "units_in_header": False,
        "decimal_aligned": False, "numeric_cols": 4, "text_cols": 1, "width": "full",
        "orientation": "portrait", "continued": False, "note_sentence": ""}

table(14, 1, S_622,
      "A judge matrix for small-sized debris, five columns by five rows: an empty stub cell over four "
      "criteria headers - Cost of manufacture, Cost of using, Fitness, Time consuming - and four row "
      "stubs, Ground-based Laser, Space-based Laser, Microsatellite, Large Satellite, against twenty "
      "bare one-decimal numbers. Ruling is booktabs again, thin above the header, heavy under it and "
      "thin at the foot, with no vertical rule and no box, so five columns of numbers stand unaligned "
      "against their own headers: the headers spread wider than the numeric columns under them and "
      "the stub column's right edge, not its left, is what lines up. NO CAPTION, NO NUMBER AND NO "
      "CITING SENTENCE - the reader meets the block under the prose line 'Small-sized Debris:' and "
      "knows only from the position on the page that it belongs to the small-debris case. The paper "
      "prints five more of these blocks without captions either.",
      dict(_MAT), section_kind="evaluation")

table(14, 2, S_622,
      "TWO MATRICES INSIDE ONE MEASURED REGION, stacked: a five-row medium-sized block with the same "
      "four headers and the same four method stubs, and directly beneath it a THREE-row block that "
      "repeats the header row and drops the Microsatellite stub, because 'Microsatellites are not "
      "suitable for large debris' as the prose above says. Both blocks are booktabs, thin above the "
      "header, heavy under it, thin at the foot, no verticals, no box; the numeric columns are bare "
      "one-decimal values and the stub column is right-aligned against them. The region that "
      "fig_extract measured covers both blocks because the two are nearer to each other than to "
      "anything else on the page, so ONE REGION CANNOT BECOME TWO ROWS: the census records eight rows "
      "here - five and three, with a second header row - and the row count is the only place the "
      "split survives. Neither block carries a caption, a number or a sentence, and the second one's "
      "own label, 'Large-sized Debris:', prints two paragraphs above it, separated from the block by "
      "the run of prose that explains why Microsatellites are excluded.",
      {"rows": 8, "cols": 5, "header_rows": 2, "rule_style": "booktabs", "zebra": False,
       "merged_cells": False, "diagonal_header": False, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 4, "text_cols": 1, "width": "full",
       "orientation": "portrait", "continued": False, "note_sentence": ""},
      section_kind="evaluation")

table(15, 1, S_622,
      "The third uncaptioned judge matrix, five by five: four method stubs against the four criteria "
      "Cost of manufacture, Cost of using, Fitness and Time consuming, emptied of context by having "
      "no header for what the numbers measure - the cells are bare one-decimal values from 0.1 to "
      "1.0, so a reader cannot tell whether higher is better on 'Cost of manufacture' or worse. "
      "Booktabs ruling as before, no verticals, no box, and the top rule begins the crop, so nothing "
      "on the page above or below identifies which of the three debris sizes this matrix judges. In "
      "five of the six matrices the same four criteria are printed in the same order and only the "
      "numbers change, which is the only reason the six blocks can be grouped at all.",
      dict(_MAT), section_kind="evaluation", order=1)

table(15, 2, S_622,
      "The fourth judge matrix, five by five, the same four criteria and the same four stubs with "
      "different values (Ground-based Laser 0.4, 0.4, 0.5, 0.4 against Space-based Laser 0.2, 0.3, "
      "0.7, 0.3 and Microsatellite 1.0, 0.4, 0.3, 0.1). Booktabs, no verticals, no box, no caption "
      "and no number; the prose below the block closes the case with 'Then, B = [0.260, 0.310, "
      "0.420]. The large satellite is the best method', a three-element vector for a four-alternative "
      "matrix, so the block that produced the printed result and the vector that reports it do not "
      "have the same width.",
      dict(_MAT), section_kind="evaluation", order=2)

table(15, 3, S_622,
      "The fifth and last judge matrix, and the only one with THREE body rows: Ground-based Laser, "
      "Space-based Laser and Large Satellite, with the Microsatellite stub dropped as it was in the "
      "large-debris block on p14, under the same four criteria headers and an empty stub cell. "
      "Booktabs, thin above the header, heavy under it, thin at the foot, no verticals and no box; the "
      "row pitch is slightly larger than the block above it, so the shorter table sits lower in its "
      "space. No caption, no number, no citing sentence - and the prose above the block ends with "
      "'consideration.', a word that belongs to a sentence about something else.",
      {"rows": 4, "cols": 5, "header_rows": 1, "rule_style": "booktabs", "zebra": False,
       "merged_cells": False, "diagonal_header": False, "units_in_header": False,
       "decimal_aligned": False, "numeric_cols": 4, "text_cols": 1, "width": "full",
       "orientation": "portrait", "continued": False, "note_sentence": ""},
      section_kind="evaluation", order=3)

# ============================================================ 7 and 8: the economy runs
figure(16, 1, "line", CAP8, "text-layer", uncited(), S_7,
       "Five solid curves in the same five colours as Figure 5, but over 'Starting Date (yr)' "
       "graduated 1980 to 2100 in decades, against 'log(Number of Impacts)' graduated minus 1.2 to "
       "minus 5.6, with the same five-entry legend outside the frame at the upper right - '01 "
       "Diameter: 0.20 (cm)' through '05 Diameter: 10.00 (cm)' - and a boxed annotation inside the "
       "plot: Altitude 800.00 km, Duration 1.00 yrs, Inclination 28.50 deg, C-S Area 1.00 m^2. THE "
       "ANNOTATION CONTRADICTS THE ABSCISSA: a duration of one year is printed over an axis that "
       "spans a hundred and twenty years, and the curves only begin near 2000 while the axis starts "
       "at 1980, so a fifth of the frame is dead space under a parameter box that says the run is one "
       "year long. No title, no citation, and the caption is the bare label 'Figure 8'.",
       geometry("line", legend="outside-right"), "8", section_kind="sensitivity", order=1)

figure(16, 2, "line", CAP9, "text-layer", uncited(), S_8,
       "One dark-red curve falling steeply and flattening toward large diameters, over 'log(Diameter "
       "Threshold (cm))' graduated minus 1.0 to 1.5, against 'log(Number of Impacts)' graduated 0.5 "
       "down to minus 5.5 - the only axis in the paper that crosses zero. The boxed in-frame title "
       "reads 'Number of Impacts vs. Impactor Diameter Threshold (Orbital Altitude Contours)': PLURAL "
       "CONTOURS OVER A SINGLE CURVE. The legend outside the frame has one entry, '01 Altitude : 800 "
       "km', with a space before its colon that no other legend in the paper prints, and a boxed "
       "parameter block sits inside the plot area covering gridlines: Start Year 2016.00 yr, Duration "
       "5.00 yrs, Inclination 28.50 deg, C-S Area 1.00 m^2. Both axes are labelled 'log' and both are "
       "graduated in evenly spaced numbers, so the log is in the values and never in the ruler. No "
       "citation; caption is the bare label 'Figure 9'.",
       geometry("line", legend="outside-right"), "9", section_kind="evaluation", order=2)

figure(17, 1, "line", CAP10, "text-layer", uncited(), S_8,
       "The same template again at altitude 400 km: one curve over 'log[Diameter Threshold (cm)]' "
       "graduated minus 1.0 to 3.0 in half units, against 'log[Number of Impacts]' graduated 0.0 down "
       "to minus 6.5, with the same boxed title 'Number of Impacts vs. Impactor Diameter Threshold "
       "(Orbital Altitude Contours)' and one legend entry outside the frame, '01 Altitude: 400 (km)'. "
       "The curve stops at about 2.0 while the axis runs to 3.0, leaving a third of the frame empty, "
       "and the ordinate's own label is clipped by the title box at the upper left. The parameter "
       "block inside the plot reads Start Year 2016.00 yr, Duration 5.00 yrs, Inclination 28.50 deg, "
       "C-S Area 1.00 m^2 - BYTE-IDENTICAL TO FIGURE 11'S, although the two exhibits are the two ends "
       "of a nineteen-fold spread in altitude and nothing in either parameter block changes. No "
       "citation; caption is the bare label 'Figure 10'.",
       geometry("line", legend="outside-right"), "10", section_kind="evaluation")

figure(18, 1, "line", CAP11, "text-layer", uncited(), S_8,
       "The same template at altitude 2000 km: one curve over 'log[Diameter Threshold (cm)]' "
       "graduated minus 1.0 to 2.0 against 'log[Number of Impacts]' graduated 0.0 down to minus 7.0, "
       "same boxed '... (Orbital Altitude Contours)' title, one legend entry outside the frame, '01 "
       "Altitude: 2000 (km)'. The curve ends near 1.7 at about minus 6.7, short of both axis limits, "
       "and the x-axis arrow overshoots its last tick. Its parameter block is identical to Figure "
       "10's including the inclination of 28.50 deg. NO SENTENCE NAMES IT: the page that carries it "
       "prints 'Shown in figure, our model can handle this situation well.', which points at an "
       "exhibit it does not name, and the caption is the bare label 'Figure 11'.",
       geometry("line", legend="outside-right"), "11", section_kind="evaluation")

# ============================================================ 9: the what-if pair
figure(19, 1, "line", CAP12, "text-layer", uncited(), S_9,
       "Four rising curves - red lowest, then dark blue, green and magenta uppermost - over "
       "'probability of collision' graduated 1 to 10 with no zero tick and the multiplier 'x 10^-4' "
       "printed loose below the right end of the axis, against 'insurance premium rate of our model' "
       "graduated 0.01 to 0.08; the in-frame title is 'insurance premium rate' and the legend inside "
       "the frame at the lower right reads 'data 7%', 'data 8%', 'data 9%', 'data 10%'. WHAT THE "
       "PERCENTAGES MEASURE IS NEVER STATED - no axis, no title, no sentence names the quantity - so "
       "the four curves differ by a parameter the reader cannot identify, and the only exhibit in the "
       "paper that shows a sensitivity as four parallel curves is unreadable without the body text. "
       "The top curve flattens below the 0.08 limit and no value is printed anywhere. Figure 12's "
       "caption is the bare label; the page prints it as a bare line above the prose.",
       geometry("line", legend="inside"), "12", section_kind="sensitivity", order=1)

figure(19, 2, "line", CAP13, "text-layer", uncited(), S_9,
       "Four descending sigmoid curves over 'log[Diameter Threshold(cm)]' - note the missing space "
       "before '(cm)' that Figure 12 prints with a space - graduated minus 1.5 to 2, against "
       "'log[Flux]' graduated 3 down to minus 8, with the in-frame title 'flux changing with different "
       "durations' and a legend inside the frame at the upper right reading '3 years', '5 years', '7 "
       "years', '9 years'. THE FOUR CURVES NEARLY SUPERIMPOSE, so the exhibit that exists to show "
       "that duration does not matter shows four curves a reader cannot separate, and the ordinate "
       "runs to minus 8 while the data bottom out near minus 6.8. The caption is the bare label "
       "'Figure 13' and the sentence immediately above it - 'The sensitive analysis proves this point "
       "directly.' - names no figure, so the exhibit is bracketed by adjacency rather than cited.",
       geometry("line", legend="inside"), "13", section_kind="sensitivity", order=2)

# ============================================================ executive summary: the third copy
figure(22, 1, "flowchart-or-schematic", no_caption(), "none", uncited(), S_8N,
       "The business-model diagram a THIRD time, in the executive summary: the same eight boxes - "
       "Insurance Duration (Time), Space Debris Distribution Rule, Probability of Collision before ADR "
       "(Risk), Strategy of ADR, Premium Rate, ADR Cost, Owner of spacecraft, Our Company - the same "
       "orange and navy arrow classes with the same free-floating key at the left margin ('fund "
       "flow', 'determine'), and the same edge labels 'Premium(Income)', 'Claims' and 'Cost', the "
       "last set vertically inside a wide solid arrow whose head overlaps the ADR Cost box. NO "
       "CAPTION AND NO NUMBER: the only pointer is the sentence closing the paragraph above it, 'The "
       "model is demonstrated in the figure below:', which would serve for any of the three copies. "
       "The 'Premium(Income)' arrow is drawn double-headed although it carries a single label and the "
       "'Claims' arrow shows no arrowhead at the company end. A summary that repeats an exhibit twice "
       "already printed, without its number, gives the reader no way to know it is the same diagram.",
       geometry("flowchart-or-schematic", legend="inside"), "", section_kind="other",
       numbered=False)

# ============================================================ the container over Figures 1 and 2
EXCLUDED.append({
    "page": 3, "bbox": REG[(3, 1)], "reason": "fragment-of-other",
    "note": "The measured vector region on p3 boxes BOTH opening pictures plus both of their "
            "captions; its two vector paths are the left and right panels' frames, and the caption "
            "block inside it reads '[3] [3] Figure 2: Debris in High Earth Orbit Figure 1: Debris'. "
            "Counting it as an exhibit would double-count the two illustrations recorded as Figure 1 "
            "and Figure 2, so it is excluded as a container.",
})

RULES = [
    "Measure first, then read the pixels: twenty-one measured regions resolve into fourteen figure "
    "rows, six table rows and one exclusion, and every region is accounted for once "
    "[place.doc_order].",
    "One measured region can hold two tables: the p14 lower region boxes a five-row matrix and, under "
    "it, a three-row matrix with the header repeated and the Microsatellite stub dropped, so the row "
    "count of eight with a second header row is the only record that the region is two tables "
    "[table.rows].",
    "A repeated exhibit is its own row only when the repeat is counted: the business-model diagram is "
    "printed on p5, again on p12 with six unexplained red ticks and queries, and a third time in the "
    "executive summary on p22 with no caption at all [geometry.family].",
    "The one exhibit that shows the data source shows a form: Figure 4 is a screenshot of the DAS "
    "input dialog with the plot still pending, so no number in the paper can be traced to a picture "
    "[geometry.family].",
    "Nine axis labels in this paper say 'log' and every one of them is graduated in evenly spaced "
    "numbers, so the log is a transform of the plotted values rather than a ruler the reader can "
    "measure against [geometry.shared_axes].",
    "Three single-curve exhibits carry a boxed title promising '(Orbital Altitude Contours)' in the "
    "plural, one at 800 km, one at 400 km and one at 2000 km, and the parameter blocks of the last two "
    "are identical line for line including the inclination [caption.verbatim].",
    "Five of the fourteen figure rows are named by a sentence and no table row or matrix is named at "
    "all; the remaining nine figures are pointed at by phrases that name nothing, from 'Shown in "
    "figure, our model can handle this situation well.' to 'The model is demonstrated in the figure "
    "below:' [mention.count].",
    "A caption whose only content is the number is not a description: seven figure rows print nothing "
    "but 'Figure 5', 'Figure 8', 'Figure 9', 'Figure 10', 'Figure 11', 'Figure 12' and 'Figure 13', "
    "and the six matrices print nothing at all [caption.numbering].",
]

NOTE = """\
Paper 98, Team 52221, a space-insurance model with active debris removal and a fuzzy comprehensive
evaluation. Twenty-three pages, twenty-one measured regions on fourteen of them, resolving into
FOURTEEN FIGURE ROWS, SIX TABLE ROWS and ONE EXCLUSION - the vector container on p3 that boxes the
two opening illustrations together - with nothing unaccounted.

Citation is thin and one citation is anachronistic. Only five figure rows are named by a sentence:
Figure 3 by p1's "The structure of whole service is demonstrated in fig.3", four pages before the
exhibit prints; Figure 4 and Figure 5 both on p7; Figure 6 on p11; Figure 7 on p12 by "This is shown
in fig.7". Everything else is pointed at by phrases that name nothing - "Here comes the diagram
showing the flux of the different-sized debris:", "Shown in figure, our model can handle this
situation well.", "The model is demonstrated in the figure below:" - and Figures 1, 2, 8, 9, 10, 11,
12, 13, Table 1 and all six matrices are unnamed.

The schematic is printed three times. Figure 3 on p5 and Figure 7 on p12 are the same eight-box
diagram with the same two-colour arrow key, and Figure 7 adds six red marks - three ticks and three
question marks - that nothing in the paper explains; the executive summary prints the same diagram a
third time on p22 with no caption and no number, introduced only by "The model is demonstrated in the
figure below:". Both named copies carry the identical caption text "Model Schematic Diagram", so they
are told apart by number alone. Money and determination are distinguished by arrow colour and nothing
else, and the diagram prints no rate, no currency and no period.

Figure 4, the exhibit cited for the debris data, is a screenshot of the DAS input dialog. No plot is
drawn on it: it shows Start 2016 yr, Duration 10 yr, a 1 m^2 cross-section, a 28.5 deg inclination, a
"cm" impactor list of 2, 5, 10 and 15, and two radio buttons clipped to "Orbital Al" and "Orbital A",
with the environment combo misspelled "Meteroids & Orbital" and three labels truncated mid-word
("Duratio", "Inclinat", "Type of"). Whatever the paper's numbers came from, this exhibit is not it.

The two opening illustrations are second-hand, tagged [3], and carry no axes, no scale, no altitude
reference and no label of any kind: one is a dot shell over a flat blue disk, the other an elongated
dot cloud around a filled black disk that nothing names. They carry "Low Earth Orbit" and "High Earth
Orbit" through their captions alone.

The run charts split into two templates. Figures 5 and 8 are the same five-diameter family - legend
exactly "01 Diameter: 0.20 (cm)" through "05 Diameter: 10.00 (cm)", placed outside the frame and
overhanging its right border - one plotted against altitude 200 to 1800 km, one against starting date
1980 to 2100, both against "log(Number of Impacts)" graduated in evenly spaced numbers from minus 1
downward. Figure 8's parameter box reads "Duration = 1.00 yrs" over a hundred-and-twenty-year abscissa,
and its curves begin near 2000, leaving the first fifth of the frame empty. Figures 9, 10 and 11 repeat
one template a third way: a single red curve under the boxed title "Number of Impacts vs. Impactor
Diameter Threshold (Orbital Altitude Contours)" - plural contours, one curve - at 800, 400 and 2000 km
respectively, with the 400 and 2000 km parameter blocks identical line for line including "Inclination
= 28.50 deg", and with both axes labelled "log" and graduated linearly.

Figures 6, 12 and 13 are the what-if exhibits. Figure 6 is one premium-rate curve against "probability
of collision" graduated 1 to 10 with the multiplier "x 10^-4" loose below the axis end and the in-frame
title in lower case, "premium rate model", against the caption's "Premium Rate Model"; the sentence that
cites it speaks of the "failure rate" instead. Figure 12 is four parallel curves legended "data 7%"
through "data 10%", and NOTHING IN THE PAPER SAYS WHAT THE PERCENTAGES MEASURE. Figure 13 is four
duration curves, 3, 5, 7 and 9 years, that nearly superimpose, so the exhibit meant to show that
duration does not matter cannot show it; it sits directly under the sentence "The sensitive analysis
proves this point directly.", which names no figure.

Table 1 is the one carefully built grid in the paper and the only exhibit whose caption prints above
it: two columns, a header row and twenty body rows from q to Mt, booktabs rules, symbols right-aligned
against a meaning column that starts flush. The six judge matrices in section 6.2.2 are typed the same
way and are captioned by nothing: five of them print the same four criteria (Cost of manufacture, Cost
of using, Fitness, Time consuming) against the same method stubs, with an empty stub cell over the
criteria, and two of the six drop the Microsatellite row for large debris. The second matrix region on
p14 boxes two of these blocks at once, a five-row and a three-row, so one measured region cannot be two
rows and the split survives only in the recorded row count. Nothing on any matrix says which debris
size it judges except the prose paragraph above it, and the closed vector that the paper reports -
"Then, B = [0.260, 0.310, 0.420]. The large satellite is the best method" - has three elements for a
four-alternative matrix.

Families: line 8, flowchart-or-schematic 3, scatter 2, photo-or-raster-image 1, table-grid 6.
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

out = PROXY / "pc98-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("items", len(ITEMS), "tables", len(TABLES), "excluded", len(EXCLUDED))
print("regions accounted", len(ITEMS) + len(TABLES) + len(EXCLUDED))
