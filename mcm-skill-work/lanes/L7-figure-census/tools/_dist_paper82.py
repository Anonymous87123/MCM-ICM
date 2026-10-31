"""Hand census of P-C-2015-35778-39d71af2 (Team 35778, 22 pages, 23 measured regions).

Twenty-one figure rows, one table row and one excluded region. The paper numbers Figures 1 to 21
with no gap and one table, and every one of them owns a measured region, so this census declares
no gap and nothing unresolved.

  p1  r1  (excluded) -                      the title-and-summary sheet, one vector frame
  p6  r1  Fig.1     flowchart-or-schematic  the staffing tree of ICM, boxes joined by connectors
  p7  r1  Fig.2     node-link-network       the 370-position affiliation network
  p7  r2  Fig.3     node-link-network       the employee affiliation/cooperation graph
  p10 r1  Fig.4     flowchart-or-schematic  the employee dismission algorithm
  p11 r1  Fig.5     flowchart-or-schematic  the employee promotion algorithm
  p13 r1  Fig.6     line                    the predicted working rate, 100 months
  p13 r3  Fig.7     line                    ten simulated recruitment-cost curves, in perspective
  p13 r2  Fig.8     line                    ten simulated training-cost curves, in perspective
  p14 r1  Fig.9     line                    working rate, churn rate 25 per cent
  p14 r2  Fig.10    line                    working rate, churn rate 35 per cent
  p14 r3  Fig.11    line                    working efficiency, churn rate 25 per cent
  p14 r4  Fig.12    line                    working efficiency, churn rate 35 per cent (axis says 25)
  p15 r1  Fig.13    scatter                 company benefit per month, churn rate 25 per cent
  p15 r2  Fig.14    scatter                 company benefit per month, churn rate 35 per cent
  p16 r1  Fig.15    line                    working rate, both recruitment methods
  p16 r2  Fig.16    line                    company performance, both recruitment methods
  p17 r1  Fig.17    line                    enthusiasm of middle-level employees
  p17 r2  Fig.18    line                    change times of middle-level employees
  p18 r1  Fig.19    node-link-network       the three-layer network, drawn in isometric planes
  p19 r1  Table 1   table-grid              the four-network comparison, three horizontal rules
  p20 r2  Fig.20    bar                     the stochastic-error stem plot
  p20 r1  Fig.21    line                    working rate under five growth coefficients

Two printed faults decide four rows of this record. The caption pair on p14 and the caption pair
on p15 each weld two labels into one printed line and push the two percentages onto a second line,
so those four captions are typed from the crops. Figure 12's axis then prints "churn rate=25%" on
the panel its caption calls 35 per cent, and Figure 14 does the same. The text layer loses the
spaces inside every caption glyph run on pp6-20 - the captions reach the layer as
"Figure1: Staffdistributionstructureineachdivision" - so each caption here was read off the proxy
and typed with its printed spacing.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2015-35778-39d71af2"
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

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def place(page: int, reg: int, kind: str, path: list[str]) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": c["region"],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          pattern: str = "direct") -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": 1, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


# ---------------------------------------------------------------- section paths
# The heading index is right on every figure row here and wrong on the table row: it files Table 1
# under "4 Sensitivity Analysis", whose heading prints at 707.7 pt on p19, forty-six points BELOW
# the bottom rule of the grid, while "3.2 The analysis of multilayer network" prints at 209.9 pt
# above it. Both p20 figures are filed under "5 Conclusion" for the same reason - the conclusion
# heading prints at 701.7 pt on the page - but they sit under "4.1" at 72.3 pt, and the section
# their readings belong to ("4.2") only starts at 412.8 pt, below both pictures.
SEC_222 = ["2 Human Capital Evolution Network Model", "2.2 Human capital static network model",
           "2.2.2 The definition of node and edge"]
SEC_231 = ["2 Human Capital Evolution Network Model", "2.3 Three evolution driving algorithm",
           "2.3.1 Employee dismission algorithm"]
SEC_232 = ["2 Human Capital Evolution Network Model", "2.3 Three evolution driving algorithm",
           "2.3.2 Employee promotion algorithm"]
SEC_241 = ["2 Human Capital Evolution Network Model", "2.4 Simulation results of the model",
           "2.4.1 Prediction for ICM’s budget requirements"]
SEC_242 = ["2 Human Capital Evolution Network Model", "2.4 Simulation results of the model",
           "2.4.2 Effects of the changing churn rate"]
SEC_243 = ["2 Human Capital Evolution Network Model", "2.4 Simulation results of the model",
           "2.4.3 Effects of no external recruitment of middle-level employees"]
SEC_31 = ["3 Multilayer Network Model", "3.1 The multilayer network for ICM"]
SEC_32 = ["3 Multilayer Network Model", "3.2 The analysis of multilayer network"]
SEC_41 = ["4 Sensitivity Analysis", "4.1 Uncertain effects produced by stochastic simulation"]

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "single",
           legend: str = "none", numbers: bool = True, labels: bool = False,
           three_d: str = "no", colorbar: bool = False, source: str = "text-layer",
           shared_axes: bool = False, note: str = "", other_note: str = "",
           confidence: str = "high") -> None:
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": confidence,
        "other_note": other_note,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, kind, path),
        "mention": mention,
        "caption": caption(cap_text, numbering),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": colorbar,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, cap_text: str, mention: dict, kind: str, path: list[str], *,
          rows: int, cols: int, numeric_cols: int, text_cols: int, rule_style: str,
          width: str, header_rows: int = 1, units_in_header: bool = False,
          note: str = "", note_sentence: str = "", source: str = "text-layer") -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, kind, path),
        "mention": mention,
        "caption": caption(cap_text, "Table N:", "above"),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule_style, "zebra": False, "merged_cells": False,
                  "diagonal_header": False, "units_in_header": units_in_header,
                  "decimal_aligned": False, "numeric_cols": numeric_cols,
                  "text_cols": text_cols, "width": width, "orientation": "portrait",
                  "continued": False, "note_sentence": note_sentence},
    })


# ---------------------------------------------------------------- 2.2 the drawn structures
figure(6, 1, "flowchart-or-schematic",
       "Figure 1: Staff distribution structure in each division", "Figure N:",
       cited(6, 6, ["Figure.1"], 1,
             "Here, we present a reasonable way of division, as is shown in Figure.1.",
             "as-shown-in"),
       "other", SEC_222, legend="below", labels=True, note=(
           "A five-tier staffing tree: CEO at the top, seven division heads under it, a row of "
           "PRODUCT boxes, six DIRECTOR boxes and a bottom row of twelve BRANCH boxes. Every box "
           "carries a name, a headcount digit and a salary band ('2 6-8', '4 6-8', '2 4-8'), so the "
           "picture prints numbers as well as names [geometry.printed_numbers]. Four glyphs key "
           "the employee grades in a legend line UNDER the tree - star for senior manager, square "
           "for experienced supervisor, triangle for inexperienced supervisor, circle for "
           "experienced employee - and the key is the only place those four marks are explained "
           "[geometry.legend]. The caption calls the drawing a distribution; the pixels are an "
           "organigram and the family follows the pixels [geometry.family]."))
figure(7, 1, "node-link-network",
       "Figure 2: Static affiliation network in ICM", "Figure N:",
       cited(7, 7, ["Figure.2"], 2, "The following Figure.2 is the affiliation network structure."),
       "other", SEC_222, labels=True, note=(
           "Roughly 370 nodes as small circles on curved edges, radiating from a dense hub. Nine "
           "named nodes carry baked labels - Prod.Manager, CEO, VP, Facilities, Research, "
           "Regional, Sales Marketing, Internet, World Wide - and the rest are unlabelled dots, so "
           "the figure prints no numeric scale at all [geometry.printed_numbers]. Colour separates "
           "nine office clusters and node radius encodes degree, which only the body sentence "
           "explains ('we count the degree of each position and directly reflect it in the radius "
           "of each point'); no legend and no size key print in the picture [geometry.legend]."))
figure(7, 2, "node-link-network",
       "Figure 3: Static cooperation relationships network in ICM", "Figure N:",
       cited(7, 7, ["Figure.3"], 1,
             "in Figure.3, the shortest length between employee3 and Exp.employee6 is 4"),
       "other", SEC_222, legend="inside", labels=True, note=(
           "Fourteen labelled employees and divisions in a hairball on the 370-position graph, with "
           "a two-entry key at upper right - a red dashed swatch 'affiliation' and a blue solid "
           "swatch 'cooperation' [geometry.legend]. The key is load-bearing: without it the two "
           "edge classes are the same green curve, because the red and blue strokes only appear on "
           "the three or four edges nearest the key. The caption sits on the second half of a "
           "printed line whose first half is Figure 2's caption, and its own last words ('in ICM') "
           "wrap to a second line, so the label the layer reports for Figure 2 swallows this one "
           "whole [caption.verbatim]."))
figure(10, 1, "flowchart-or-schematic",
       "Figure 4: Employee dismission algorithm", "Figure N:",
       cited(10, 10, ["Figure.4"], 1,
             "Figure.4 is employee churn algo- rithm, the mainly steps are as follows:"),
       "solution", SEC_231, labels=True, note=(
           "A vertical flowchart of eight boxes and two decision diamonds with labelled branches "
           "('NO', 'No'), one loop back to the top and a shaded terminal box. The body names it "
           "'employee churn algorithm' and the caption names it 'dismission'; both spellings are "
           "kept. No axes, no numbers, no key [geometry.legend]. The whole drawing is one 1-path "
           "raster, so none of its seven box labels exists in the text layer."))
figure(11, 1, "flowchart-or-schematic",
       "Figure 5: Employee promotion algorithm", "Figure N:",
       cited(11, 11, ["Figure.5"], 1,
             "Figure.5 is the employee promotion algorithm, the mainly steps are as follows:"),
       "solution", SEC_232, labels=True, note=(
           "The same box-and-diamond style as Figure 4, now three decisions deep with two 'No' "
           "loops returning to 'i=i-1' and one 'Yes' path through 'Set the productivity order'. The "
           "loop arrow crosses the top box, so the flow reads right-to-left at the top. One 1-path "
           "raster, no axes, no numbers."))
figure(13, 1, "line",
       "Figure 6: The prediction of working rate", "Figure N:",
       cited(13, 13, ["Figure.6"], 1,
             "we can simulate the on-the-job rate curve in next 100 months, as is shown in "
             "Figure.6.", "as-shown-in"),
       "other", SEC_241, note=(
           "One blue polyline over 100 months inside a closed axes frame; y runs 0.78 to 0.86 and "
           "carries the rotated title 'working rate', x is 'time/month'. The curve falls in steps "
           "from 0.85 to a floor near 0.79 and recovers to 0.82. Both axis titles print, no key, no "
           "colour bar, no annotation [geometry.printed_numbers]. The tick labels reach the text "
           "layer in reverse order ('etar' for 'rate', 'gnikrow' for 'working'), which is a layer "
           "artifact and not a printed defect."))
figure(13, 3, "line",
       "Figure 7: The cost of recruitment per month", "Figure N:",
       cited(13, 13, ["Figure.7"], 1,
             "we simulate model 10 times to predict the cost of recruitment and training cost per "
             "month, as is shown in Figure.7, Figure.8", "as-shown-in"),
       "other", SEC_241, three_d="perspective-bars", note=(
           "Ten simulation runs drawn as ten coloured polylines in one perspective box, the series "
           "stacked along a depth axis with no depth label, so the box is a 3-D ribbon plot and not "
           "a surface [geometry.three_d]. Depth is carried by the colour order alone: no key, no "
           "run number, no depth tick [geometry.legend]. y prints 'cost of recruitment per month' "
           "rotated, x prints 'time/month'. Ten curves over 100 months in a 1-path raster, so none "
           "of these titles is in the text layer."))
figure(13, 2, "line",
       "Figure 8: The cost of training per month", "Figure N:",
       cited(13, 13, ["Figure.8"], 1,
             "we simulate model 10 times to predict the cost of recruitment and training cost per "
             "month, as is shown in Figure.7, Figure.8", "as-shown-in"),
       "other", SEC_241, three_d="perspective-bars", note=(
           "The same perspective ribbon as Figure 7, now for training cost, and the same absence of "
           "a depth label or a key. The two figures are printed side by side at the identical size "
           "but on different y windows - the recruitment ribbons sit near 160-200 and the training "
           "ones spike to 300 - so the pair cannot be read against each other [place.area_frac]. "
           "Side by side they also share no axes, which the geometry records [geometry.shared_axes]."))

# ---------------------------------------------------------------- 2.4.2 the churn sweep
figure(14, 1, "line",
       "Figure 9: Working rate when churn rate is 25%", "Figure N:",
       cited(14, 14, ["Fig- ure.9"], 1,
             "the scatter diagram of total company performance per month is Figure.13"),
       "other", SEC_242, note=(
           "One blue polyline over 100 months on y 0.70-0.86, printed with the rotated title "
           "'working rate when churn rate=25%' and a dashed horizontal reference rule near 0.75 "
           "that no key explains [geometry.legend]. The panel is drawn as vector strokes, so its "
           "121 text items reach the layer - and every one of them arrives reversed ('%52=etar' for "
           "'rate=25%'), which is why the axis titles in this record were read off the crop and not "
           "off the layer. The number in the axis title is 25 per cent, as the caption says."))
figure(14, 2, "line",
       "Figure 10: Working rate when churn rate is 35%", "Figure N:",
       cited(14, 14, ["Fig- ure.10"], 1,
             "the scatter diagram of total company performance per month is Figure.12"),
       "other", SEC_242, note=(
           "The 35 per cent half of the pair, printed beside Figure 9 on a DIFFERENT window - 0.65 "
           "to 0.80 against 0.70 to 0.86 - so the two curves the caption invites the reader to "
           "compare are drawn on scales that differ by 0.05 at both ends and cannot be compared by "
           "shape [geometry.shared_axes]. One solid rule at 0.8 is drawn for reference and is left "
           "unlabelled. Vector strokes, reversed text in the layer, no key."))
figure(14, 3, "line",
       "Figure 11: Working efficiency when churn rate is 25%", "Figure N:",
       cited(14, 14, ["Figure.11"], 1,
             "the working efficiency curve figure of ICM’s employee Figure.11"),
       "other", SEC_242, source="typed-from-crop", note=(
           "Enthusiasm over 100 months on y 0.85-1.00, axis title printed 'enthusiasim when churn "
           "rate=25%' - the misspelling is printed and is carried in this note rather than "
           "corrected in the field [caption.verbatim]. The caption is typed from the crop because "
           "the text layer welds both labels of the p14 pair onto one line and drops the two "
           "percentages to a second line, leaving 'Figure 11: Working efficiency when churn rate "
           "isFigure 12: Working efficiency when churn rate is' as a single string with '25%' and "
           "'35%' after it [caption.verbatim]."))
figure(14, 4, "line",
       "Figure 12: Working efficiency when churn rate is 35%", "Figure N:",
       cited(14, 14, ["Figure.12"], 1,
             "the working efficiency curve figure of ICM’s employee is Figure.14"),
       "other", SEC_242, source="typed-from-crop", note=(
           "THE PANEL THE CAPTION CALLS 35 PER CENT PRINTS 25 PER CENT ON ITS OWN AXIS: the rotated "
           "title reads 'enthusiasim when churn rate=25%', character for character the same as "
           "Figure 11's, so the pair is either mislabelled or the wrong plot was pasted in "
           "[caption.verbatim]. The two panels are not mirror images either - this one falls from 1.0 "
           "to 0.75 and its neighbour from 0.95 to 0.85 - so the second half of the churn comparison "
           "cannot be identified from the artwork. Both panels use the same y window, which is the "
           "one thing the pair gets right [geometry.shared_axes]."))

# ---------------------------------------------------------------- 2.4.3 the recruitment comparison
figure(15, 1, "scatter",
       "Figure 13: Company performance when churn rate is 25%", "Figure N:",
       cited(14, 15, ["Figure.13"], 1,
             "the scatter diagram of total company performance per month is Figure.13"),
       "other", SEC_243, legend="inside", source="typed-from-crop", note=(
           "Company benefit per month as 100 isolated open diamonds with NO connecting stroke - the "
           "caption calls it a diagram and the pixels are a point cloud - plus one dashed horizontal "
           "rule keyed 'average benefit per month' in an inside box, which is the paper's only "
           "in-plot key in this section [geometry.legend]. y runs 165-195 and prints 'benefit per "
           "month when churn rate=25%/sigma', x prints 'time/month'. The key box is drawn on top of "
           "the dashed rule it labels, so the one number the key marks is partly obscured "
           "[caption.verbatim]."))
figure(15, 2, "scatter",
       "Figure 14: Company performance when churn rate is 35%", "Figure N:",
       cited(14, 15, ["Figure.14"], 1,
             "the working efficiency curve figure of ICM’s employee is Figure.14"),
       "other", SEC_243, legend="inside", source="typed-from-crop", note=(
           "The 35 per cent partner of Figure 13, drawn as 100 filled grey points with no "
           "connecting stroke and keyed the same way. It carries the same printed fault as Figure 12: "
           "the axis title reads 'benefit per month when churn rate=25%' under a caption that "
           "promises 35 per cent, so both second-half panels of this paper mislabel their own rate. "
           "Its window is 145-185 against Figure 13's 165-195, so the pair is drawn on two scales "
           "[geometry.shared_axes], and its key sits in the middle of the point cloud where it is "
           "hard to read [geometry.legend]."))
figure(16, 1, "line",
       "Figure 15: Working rate of two recruitment methods", "Figure N:",
       cited(16, 16, ["Figure.15"], 1,
             "Working rate: the working rate of two different recruitment methods in two years is "
             "shown in Figure.15."),
       "other", SEC_243, legend="outside-right", note=(
           "Two curves over 24 months, blue 'no external recruiting' above dark red 'external "
           "recruiting', keyed in a box printed to the RIGHT of the plot frame - the only key in "
           "the paper placed outside the axes [geometry.legend]. No axes frame is drawn at all, so "
           "the two series float on the tick grid, and the rotated y title is set so small that it "
           "reads as 'wr/degree' at print [caption.verbatim]. Both series carry square markers and "
           "differ mainly by colour, i.e. they are unfriendly to a monochrome reader."))
figure(16, 2, "line",
       "Figure 16: Company performance of two recruitment methods", "Figure N:",
       cited(17, 16, ["Figure.16"], 1,
             "the company performance of two different recruitment methods in two years is shown "
             "in Figure.16."),
       "other", SEC_243, legend="below", note=(
           "The same two-method comparison for company performance, keyed UNDER the plot at bottom "
           "right rather than beside it, so the pair of figures keys its two curves in two "
           "different places [geometry.legend]. No frame, no y title that survives print, and the x "
           "title 'time/month' runs into the last tick. This is the one figure whose citable pointer "
           "prints a page AFTER the artwork - the body reads it on p17 [mention.lead_pages]."))
figure(17, 1, "line",
       "Figure 17: Average enthusiasm of middle-level employees of two recruitment", "Figure N:",
       cited(17, 17, ["Figure.17"], 1,
             "of two different recruitment methods in two years is shown in Figure.17."),
       "other", SEC_243, legend="below", note=(
           "Two curves over 24 months on y 0.73-0.78, keyed under the plot at bottom right, with "
           "the lower y tick labels clipped by the left edge of the raster [geometry.legend]. The "
           "caption STOPS MID-PHRASE - it prints '... of two recruitment' and never reaches the "
           "word 'methods' that every other caption in the series carries - so the field records "
           "the truncated line and not the phrase the author meant [caption.verbatim]."))
figure(17, 2, "line",
       "Figure 18: Average change times of middle-level employees of two recruitment", "Figure N:",
       cited(17, 17, ["Figure.18"], 1,
             "of two different recruitment methods in two years is shown in Figure.18."),
       "other", SEC_243, legend="below", note=(
           "The second truncated caption of the pair, cut at the same word, over a two-curve plot "
           "keyed below and drawn with an open right edge [geometry.legend]. The sentence that "
           "points at it repeats the WRONG quantity - 'Average change times of middle-level "
           "employees: the average enthusiasm of middle-level employees ... is shown in Figure.18' "
           "- so the printed label and the printed reading describe two different measures "
           "[mention.lead_sentence]."))

# ---------------------------------------------------------------- 3.x and 4.x
figure(18, 1, "node-link-network",
       "Figure 19: The multilayer network for Networks office", "Figure N:",
       cited(18, 18, ["Figure.19"], 2,
             "Figure.19 shows the whole multilayer network structure"),
       "other", SEC_31, three_d="isometric", labels=True, note=(
           "Three networks drawn as three light-blue parallelograms stacked in an exploded "
           "isometric view, each holding its own cluster of nodes - one human-capital layer, one "
           "competition layer, one friendship layer - joined by dotted inter-layer edges. The three "
           "layer names print OUTSIDE the planes on the left, so the picture has labels but no key "
           "[geometry.legend]. Node ids print at 6 pt and collide with the curved intra-layer edges "
           "[caption.verbatim]. The body sentence admits the geometry is incomplete ('Not every "
           "cross-layers-edge is drawn in the Figure.19 just to show the meaning'), which is the "
           "one place the drawing's own shortfall is declared."))
figure(20, 2, "bar",
       "Figure 20: The stochastic error", "Figure N:",
       cited(20, 20, ["Figure.20"], 1,
             "Figure.20 show us the stochastic error produced by the random process."),
       "solution", SEC_41, note=(
           "A signed stem plot about a zero line: one vertical bar per month for the difference "
           "between two three-run averages, y titled 'The difference of working rate' over about "
           "-0.02 to 0.02, x titled 'Tme/month' with the missing letter printed [caption.verbatim]. "
           "The stems are drawn so densely that individual sign changes merge into a band, so the "
           "sentence that reads the maximum error as under 0.015 cannot be checked against the "
           "picture [geometry.printed_numbers]. No key."))
figure(20, 1, "line",
       "Figure 21: The working rate under different growth coefficient", "Figure N:",
       cited(20, 20, ["Figure.21"], 1,
             "Figure.21 shows the change of working rate under different coefficient value."),
       "solution", SEC_41, legend="outside-right", note=(
           "Five working-rate curves over 100 months on y titled 'Working Rate', keyed to the right "
           "of the frame with the five growth coefficients 1.02, 1.05, 1.07, 1.10 and 1.13 - the "
           "only place in the paper where a parameter value is printed beside its curve, and the "
           "key carries no title saying so [geometry.legend]. x tick labels are set vertically and "
           "collide into an unreadable band [caption.verbatim]. Its pointer and its heading are "
           "both out of step with the picture: the figure prints at 211-355 pt under 4.1, the "
           "sentence that reads it prints at 615.2 pt under 4.2, and the caption weld puts Figure "
           "21's label on the same line as Figure 20's [place.section_path]."))

# ---------------------------------------------------------------- 3.2 the comparison grid
table(19, 1, q("Table 1: Main characters for networks", 19),
      cited(19, 19, ["Table.1"], 1,
            "Table.1 gives out the main character conclusions of three monolayer networks and the "
            "multilayer net-"),
      "result", SEC_32, rows=5, cols=5, numeric_cols=4, text_cols=1, rule_style="booktabs",
      width="full", note=(
          "Three full-width rules at 471.5, 490.6 and 550.5 pt across 454.8 pt of the 454.7 pt "
          "measure, no vertical rule anywhere, no zebra [table.rule_style]. One header row - 'The "
          "layer type', 'Average degree', 'Average cluster', 'Average path length', 'Graph density' "
          "- and four body rows naming the three monolayer networks and the multilayer one. The "
          "title says 'characters' where 'characteristics' is meant [caption.verbatim]. Four "
          "numeric columns of differing precision (0.929 beside 0, 2.978 beside 11 is not printed, "
          "0.143) are right-aligned to the cell edge rather than to the decimal point, so the "
          "columns line up only by luck [table.decimal_aligned]. No unit prints in any header, and "
          "the row labels switch between 'The Human Capital layer' and 'The competition network' "
          "inside the same column [table.units_in_header]."),
      note_sentence=q("Table.1 gives out the main character conclusions of three monolayer networks "
                      "and the multilayer net-", 19))

# ---------------------------------------------------------------- the title sheet
EXCLUDED.append({"page": 1, "bbox": REG[(1, 1)], "reason": "not-an-exhibit",
                 "note": ("The title-and-summary sheet: one 310-path vector block enclosing the "
                          "paper's title, its running head and 29 lines of abstract, measured at "
                          "0.846 of the page and larger than every exhibit in the paper. It draws "
                          "a rule under the title at 187.0 pt and five short verticals, and it "
                          "holds no artwork [place.area_frac]."),
                 "confidence": "high"})

RULES: list[str] = [
    "Families: line x13, flowchart-or-schematic x3, node-link-network x3, scatter x2, bar x1, "
    "table-grid x1, over twenty-two rows from twenty-three measured regions plus one excluded "
    "title sheet [geometry.family].",
    "The excluded region is the title-and-summary sheet on p1, one 310-path vector block at 0.846 "
    "of the page holding the title, the running head and 29 abstract lines and no artwork at all - "
    "it is larger than every exhibit in the paper and is still not one [place.area_frac].",
    "The caption family noun does not decide the family here: Figure 1 is captioned a "
    "'Staff distribution structure' and the pixels are an organigram of boxes on connectors, so it "
    "is recorded flowchart-or-schematic, and Figure 13 is captioned a 'diagram' and the pixels are "
    "100 isolated points with no connecting stroke, so it is recorded scatter [geometry.family].",
    "Figures 7 and 8 are ten simulation runs per month drawn as ten polylines stacked in a "
    "perspective box with no depth axis, no depth tick and no key - a 3-D ribbon, recorded three_d "
    "with the family left as line because the marks are still time series [geometry.three_d].",
    "Figure 19 is the only exhibit drawn in three stacked planes and the only one whose labels "
    "print OUTSIDE the artwork: 'human capital layer', 'competition layer' and 'friendship layer' "
    "sit on the left margin, and no key explains the dotted inter-layer edges [geometry.legend].",
    "FOUR CAPTIONS CARRY A PRINTED CHURN RATE THE PANEL CONTRADICTS. Figures 11 and 12 share the "
    "caption pair 25/35 per cent and both axes print 'enthusiasim when churn rate=25%'; Figures 13 "
    "and 14 repeat the fault on benefit per month, so on this paper the second half of every "
    "comparison carries the first half's label [caption.verbatim].",
    "The word 'enthusiasim' is misspelled on both p14 axis titles and the x title of Figure 20 "
    "prints 'Tme/month' with the letter missing; the record keeps the printed spelling in the note "
    "and does not repair it [caption.verbatim].",
    "Four captions are typed from the crops because the p14 and p15 pairs weld two labels onto one "
    "printed line and drop the percentages to a second line, so the layer reports "
    "'Figure 11: Working efficiency when churn rate isFigure 12: Working efficiency when churn "
    "rate is' as one string and neither label can be quoted whole [caption.verbatim].",
    "Figures 17 and 18 are captioned '... of two recruitment' - the captions stop mid-phrase and "
    "never reach the word 'methods' that the rest of the series prints, so the truncation is "
    "recorded rather than completed [caption.verbatim].",
    "Side-by-side panels are drawn on different windows in every pair: Figures 9/10 on 0.70-0.86 "
    "against 0.65-0.80, Figures 13/14 on 165-195 against 145-185, and Figures 7/8 near 160-200 "
    "against spikes to 300 - so no pair can be compared by shape, and only Figures 11/12 share a "
    "window [geometry.shared_axes].",
    "Keys are placed four ways in one paper: under the tree (Figure 1), inside the plot (Figure 3 "
    "and both benefit scatters), outside the frame on the right (Figures 15 and 21) and under the "
    "plot at bottom right (Figures 16, 17 and 18), so a reader cannot rely on one position "
    "[geometry.legend].",
    "Table 1 is the paper's only grid: three full-width rules at 471.5, 490.6 and 550.5 pt across "
    "454.8 pt, no vertical, five columns and four numeric ones right-aligned to the cell edge "
    "rather than to the decimal point, so 0.929 and 0 line up by luck [table.decimal_aligned].",
    "The section index is right on every figure row and wrong on the table row: Table 1 prints at "
    "471.5-550.5 pt under '3.2 The analysis of multilayer network' at 209.9 pt while '4 Sensitivity "
    "Analysis' prints at 707.7 pt BELOW the grid, and both p20 figures are filed under '5 "
    "Conclusion' at 701.7 pt although they sit under '4.1' at 72.3 pt [place.section_path].",
    "Citation is complete and flat: all twenty-one figures and the table are named in prose, "
    "eighteen of them exactly once on the page that prints them, Figure 2 twice on its own page, "
    "Figure 19 twice across p18 and p19, and Figure 16 alone is read a page after it prints "
    "[mention.count].",
    "The pointers are written 'Figure.4' with a period and no space, while every caption prints "
    "'Figure 4:' with a colon, so the paper uses two numbering systems that never touch; the body "
    "also names Figure 4 'employee churn algorithm' where the caption says 'dismission' "
    "[caption.numbering].",
    "Text-layer losses to declare: every caption glyph run on pp6-20 reaches the layer with its "
    "spaces stripped ('Figure1: Staffdistributionstructureineachdivision'), and every vector axis "
    "title arrives reversed ('%52=etar' for 'rate=25%'), which is why all axis readings in this "
    "record came off the crops [caption.verbatim].",
]

NOTE = (
    "Paper 82, Team 35778, twenty-two pages, a 2015 paper that models ICM's staffing as a network "
    "and then simulates twenty years of hiring, promotion and churn. Twenty-three measured regions: "
    "twenty-one figure rows, one table row and one refusal, nothing unaccounted and nothing "
    "unresolved. The paper prints Figures 1 to 21 with no gap in the numbering and one numbered "
    "table, and every one of them owns a region - the first census in this batch with no declared "
    "gap.\n\n"
    "The first finding is a labelling failure that runs through the second half of the paper. The "
    "churn sweep is printed as two caption pairs, 25 per cent and 35 per cent, and the 35 per cent "
    "panel of each pair prints 25 per cent on its own rotated axis: Figure 12 is titled "
    "'enthusiasim when churn rate=25%' and Figure 14 prints 'benefit per month when churn rate=25%'. "
    "The two panels of each pair are also drawn on different y windows, so the comparison the "
    "captions promise cannot be made either by label or by shape. Neither half of the 35 per cent "
    "case is recoverable from the artwork.\n\n"
    "The second finding is the caption layer doing nothing. Twenty of the twenty-one captions are "
    "bare noun phrases of three to eleven words, none names a variable, a unit, a condition or a "
    "conclusion, and two of them stop mid-phrase at 'of two recruitment'. The paper's own readings "
    "live in the body prose, which is fine, but the captions are the only text that survives "
    "extraction for eight of these rows, and every one of those eight is a picture.\n\n"
    "The third is a measurement note rather than a paper fault: the caption glyph runs on pp6-20 "
    "have no space glyph in the embedded subset, so the text layer returns "
    "'Figure1: Staffdistributionstructureineachdivision' and the vector axis titles come back "
    "reversed. Every caption and every axis reading in this record was taken from the proxies.\n\n"
    "Table 1 is the paper's only grid, three horizontal rules with no vertical, and it is filed "
    "under 3.2 by hand because the heading index follows the last heading on the page, which is "
    "'4 Sensitivity Analysis' printing below the table. Both p20 figures needed the same treatment "
    "in reverse - the index files them under the conclusion that prints below them, while the "
    "section that reads them, 4.2, starts below the pictures as well."
)

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT.get("layout_sha256") or LAYOUT.get("sha256", ""),
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

if __name__ == "__main__":
    dest = PROXY / "pc82-payload.json"
    dest.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {dest}")
