"""Hand census of P-C-2015-39160-2b8963a3 (Team 39160, 17 pages, 9 measured regions).

Eight figures, no tables. The nine measured regions are eight exhibits plus one repeated
measurement: page 4 carries the same [33.8, 264.1, 296.3, 502.6] box twice, so the region pass
counts Figure 1's raster twice and the distinct-key count is eight.

  p4  r1/r2  Fig.1  node-link-network   three stacked layers of the ICM supervision network
  p10 r1     Fig.2  scatter             satisfaction against churn count, with a fitted curve
  p11 r1     Fig.3  scatter             satisfaction against performance
  p12 r1     Fig.4  other               two-slice pie of recruitment vs training budget
  p12 r2     Fig.5  line                three series over thirty years
  p13 r1     Fig.6  scatter             HR positions worked on against vacancies, saturating at 37
  p13 r2     Fig.7  scatter             vacancies by year, two regimes on one axis
  p14 r1     Fig.8  bar                 100% stacked columns of filled against vacant positions

Two structural findings. First, THE PAPER HAS NO CAPTION TEXT: every printed caption is the bare
label "Figure N" - no title, no unit, no description - and Figures 2 and 3 print even that inside
the raster, so those two captions are typed from the crops. Second, the text layer of pp13 and p14
INTERLEAVES the figure's own axis labels and tick values into the prose, so the prose sentences that
name Figures 6, 7 and 8 arrive split around numbers ('When HR is not able to work on at least 2/3 of
Figure 7 the current vacant 160 positions'). Figure 2 is never named anywhere in the text layer; its
label survives only inside its own raster.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2015-39160-2b8963a3"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]

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


def place(page: int, reg: int, kind: str, path: list[str], numbered: bool = True) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": c["region"],
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


def caption(verbatim: str, numbering: str = "Figure N", position: str = "above",
            words: int | None = None) -> dict:
    return {"verbatim": schema.norm(verbatim), "numbering": numbering,
            "words": words if words is not None else len(schema.words(verbatim)),
            "sentences": 1, "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


def geometry(family: str, panels: int = 1, layout: str = "1x1", legend: str = "none",
             colorbar: bool = False, labels: bool = False, numbers: bool = True,
             shared: bool = False, three_d: str = "no") -> dict:
    return {"family": family, "panel_count": panels, "panel_layout": layout,
            "legend": legend, "colorbar": colorbar, "data_labels": labels,
            "printed_numbers": numbers, "shared_axes": shared, "three_d": three_d}


SEC_212 = ["2.1 Multilayer Network: Positions Filled with People",
           "2.1.2 Organizing the Structure of ICM"]
SEC_345 = ["3.4.5 Analysis of the Intermediate Phase"]
SEC_355 = ["3.5.5 Analysis of the Final Model"]
SEC_41 = ["4 Results", "4.1 Budget Requirements for Talent Management"]
SEC_42 = ["4.2 Sustainability of 80% Full Status"]

_KNOWN = {schema.norm(h["label"]) for h in CTX["headings"]}
for _label in [p for group in (SEC_212, SEC_345, SEC_355, SEC_41, SEC_42) for p in group]:
    if schema.norm(_label) not in _KNOWN:
        raise SystemExit(f"section label is not an indexed heading: {_label!r}")

ITEMS: list[dict] = []


def figure(page: int, reg: int, number: str, family: str, cap: dict, cap_src: str,
           mention: dict, kind: str, section: list[str], note: str,
           geo: dict | None = None, section_kind: str = "model",
           other_note: str = "", confidence: str = "high") -> None:
    item = {
        "page": page, "bbox": REG[(page, reg)], "kind": kind, "family": family,
        "panel_count": (geo or {}).get("panel_count", 1),
        "caption_source": cap_src, "caption_verbatim": cap["verbatim"],
        "caption": cap, "geometry": geo or geometry(family),
        "place": place(page, reg, section_kind, section),
        "mention": mention, "note": note, "confidence": confidence,
        "printed_number": number,
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS.append(item)


# ------------------------------------------------------------------- p4 Figure 1
figure(4, 1, "1", "node-link-network",
       caption("Figure 1", position="below"),
       "text-layer",
       cited(4, 4, ["Figure 1"], 1,
             "Figure 1 depicts a subset of our multilayer network representing ICM."),
       "raster", SEC_212,
       "The ICM supervision network drawn three times, one layer per relation, in a single raster: "
       "the bottom band is the direct command tree (node 0 the research office manager with edges "
       "to 1, 2, 3 and across to node 4, then 4 fanning out to 5-11 and 11 to 12-17), the middle "
       "band is the 'works loosely with' relation drawn dense enough to read as a mesh of crossings, "
       "and the top band is the 'works closely with' relation, which prints as near-parallel "
       "horizontal bundles between neighbouring numbers. Nodes are small filled ovals labelled 0 to "
       "17, drawn in a second cluster at the right of each band where 0, 1, 2, 3 sit unconnected to "
       "the rest. No axis, no scale, no legend, no key to which band is which layer - the prose, not "
       "the picture, says bottom is command, middle is loosely, top is closely. The raster's own "
       "resolution is low enough that the 12-17 labels blur into the edges they sit on. THE REGION "
       "PASS MEASURES THIS BOX TWICE: p4 r1 and p4 r2 print the identical bbox, so the nine "
       "measured regions are eight distinct exhibits and one repeated measurement.",
       geometry("node-link-network", panels=3, layout="3x1", numbers=True))

# ------------------------------------------------------------------ p10 Figure 2
figure(10, 1, "2", "scatter",
       caption("Figure 2", position="above"),
       "typed-from-crop",
       uncited(),
       "raster", SEC_345,
       "Average satisfaction against the number of people churned, as filled squares with a fitted "
       "decreasing curve drawn through them: three points at 51-57 churned sit at 0.30, 0.29 and "
       "0.22, and the remaining twenty-odd collapse into a flat band between 0.15 and 0.18 from 58 "
       "to 80. Both axes are titled (Average satisfaction, Number of people churned) and printed to "
       "two decimals, with a full grid of both horizontal and vertical rules. The curve is a fitted "
       "hyperbolic decay and is NOT keyed - no label, no legend, no equation - so a reader cannot "
       "tell whether it is a model fit, a flattener or a hand-drawn guide. THIS FIGURE IS NEVER NAMED "
       "ANYWHERE: the text layer of the whole paper contains no 'Figure 2', and its label survives "
       "only as pixels inside the raster.",
       geometry("scatter", numbers=True))

# ------------------------------------------------------------------ p11 Figure 3
figure(11, 1, "3", "scatter",
       caption("Figure 3", position="above"),
       "typed-from-crop",
       cited(11, 11, ["Figure 3"], 1,
             "Figure 3 shows that we achieve this goal even with the introduction of numerous "
             "other variables"),
       "raster", SEC_355,
       "Average satisfaction against average performance as twenty-nine filled squares rising from "
       "(0.50, 0.565) to (0.61, 0.675) along a clearly linear ridge. Both axes titled "
       "(Avg Satisfaction, Avg Performance), both printed to two decimals, horizontal rules only. "
       "No line, no fit, no legend: the linearity the prose claims ('we achieve this goal') is left "
       "for the reader to eyeball off the squares. The point of the figure is that satisfaction "
       "still drives performance after six other variables were added, but neither axis is scaled "
       "to show the residual scatter against a fitted line, so no reader can measure how tight the "
       "relation actually is.",
       geometry("scatter", numbers=True))

# ------------------------------------------------------------------ p12 Figure 4
figure(12, 1, "4", "other",
       caption("Figure 4", position="above"),
       "text-layer",
       cited(11, 12, ["Figure 4"], 1,
             "Figure 4 is a pie chart showing the average budget spent on recruiting versus "
             "training over a period of thirty years"),
       "vector", SEC_41,
       "A two-slice greyscale pie dividing the thirty-year budget between Training Cost (dark, the "
       "larger slice) and Recruitment Cost (light). No percentages, no values, no totals, no axis; "
       "the two slices are identified only by two small squares in a legend at the lower right. The "
       "larger slice is roughly three quarters of the disc, and the split is drawn against the "
       "vertical, so the reader can estimate a fraction but nothing on the page prints one. "
       "Recorded as other because the vocabulary has no pie class and this is a part-to-whole disc, "
       "not a bar, not a scatter and not a diagram.",
       geometry("other", legend="outside-right", numbers=False),
       section_kind="result",
       other_note="two-slice greyscale pie chart of budget share (Training Cost vs Recruitment "
                  "Cost), legend squares at lower right, no percentages and no axis")

# ------------------------------------------------------------------ p12 Figure 5
figure(12, 2, "5", "line",
       caption("Figure 5", position="above"),
       "text-layer",
       cited(12, 12, ["Figure 5"], 1,
             "Figure 5 is a graph showing the changes in training cost, recruitment cost, and "
             "number of churned employees over the course of thirty years."),
       "vector", SEC_42,
       "Three greyscale series over thirty years, y 0 to 90 in tens, x labelled 1 to 30 with only the "
       "odd ticks printed (1, 3, 5 ... 29) and titled 'Year'. Legend OUTSIDE at the right with "
       "sample rules for Training Cost, Churned Employees and Recruitment Cost. Recruitment Cost "
       "runs flat at about 82 for the whole window; Churned Employees swings between 47 and 84 with "
       "a deep dip at year 4 and a spike at year 26; Training Cost drifts between 32 and 42. The "
       "two trend series are drawn in two greys so close that they cannot be told apart at legend "
       "size, and the plot carries a full grid of both horizontal and vertical rules which the line "
       "vertices sit on - a reader cannot say whether several flat stretches are data or single "
       "segments between years. All three series are counts of different things on one y axis with "
       "no shared unit.",
       geometry("line", legend="outside-right", numbers=True),
       section_kind="result")

# ------------------------------------------------------------------ p13 Figure 6
figure(13, 1, "6", "scatter",
       caption("Figure 6", position="above"),
       "text-layer",
       cited(13, 13, ["figure 6"], 1,
             "As shown in figure 6, as long as the number of vacancies is below the maximum 10% of "
             "total positions"),
       "vector", SEC_42,
       "Diamonds, not a line: 'Positions HR is Working on' against 'Vacancies', sixteen blue diamonds "
       "that climb from (44, 30) to (57, 37) in steps of one or two and then sit perfectly flat at "
       "37 from 57 through 71. The horizontal part is the point of the figure - 37 is the maximum "
       "ten percent of positions HR can work on at once, and the prose says so - but nothing on the "
       "picture marks that ceiling: no rule is drawn at 37, no label, no annotation. Both axes are "
       "titled and printed every two units, y 25 to 39 and x 40 to 75, horizontal rules only. Every "
       "piece of text on this figure is set BOLD, axis titles included, which no other figure here "
       "does.",
       geometry("scatter", numbers=True),
       section_kind="result")

# ------------------------------------------------------------------ p13 Figure 7
figure(13, 2, "7", "scatter",
       caption("Figure 7", position="above"),
       "text-layer",
       cited(13, 13, ["Figure 7"], 1,
             "When HR is not able to work on at least 2/3 of Figure 7"),
       "vector", SEC_42,
       "Twenty-five diamonds of 'Number of Vacancies' against 'Year number', y 60 to 160 in tens, x "
       "0 to 35 in fives, horizontal rules only, all text bold. The series does two visibly "
       "different things: from year 1 to about 21 it climbs with a sawtooth (every third or fourth "
       "year dips back ten to twenty vacancies), and from year 22 on it is flat near 140 with one "
       "outlier at 118. The prose attributes this to vacancies compounding once HR cannot handle two "
       "thirds of the current vacant positions, but the picture prints no threshold, no break marker "
       "and no second series to show that regime, so the causal claim rests entirely on the text. "
       "The y axis starts at 60 rather than 0, which magnifies the climbs.",
       geometry("scatter", numbers=True),
       section_kind="result")

# ------------------------------------------------------------------ p14 Figure 8
figure(14, 1, "8", "bar",
       caption("Figure 8", position="above"),
       "text-layer",
       cited(13, 14, ["Figure 8"], 1,
             "As we can see in 90 Figure 8, this means 80"),
       "vector", SEC_42,
       "A hundred-percent stacked column chart, thirty bars, y 0% to 100% in tens, x 1 to 30 with "
       "only the odd ticks printed and no axis title at all. Dark 'Pct Pos Filled' columns stack "
       "under pale 'Pct Pos Vacant', legend OUTSIDE at the right with fill swatches, and the filled "
       "bars are drawn with a fine vertical hatch that aliases into grey at this size. Filled "
       "positions run 83% in year 1, drop to a floor of about 61% around year 22, and finish near "
       "70%, which is the paper's answer on whether ICM can hold its 80% full status at 35% churn. "
       "No reference line at 80% is drawn although every sentence that cites this figure is about "
       "80%, and the x axis has no title while its tick labels are every other year - so the "
       "columns and the years cannot be aligned without counting bars.",
       geometry("bar", legend="outside-right", numbers=True),
       section_kind="result")

RULES = [
    "Measure first, then read the pixels: nine measured regions resolve into eight exhibits, and "
    "the ninth is the same box measured twice on p4, which the distinct-key count merges back into "
    "one exhibit [place.area_frac].",
    "A region that prints the identical bbox twice is one exhibit and not two: p4 r1 and p4 r2 are "
    "byte-identical crops of Figure 1, so no second row is invented for it [place.page_order].",
    "A printed caption that is only the label is recorded with that label alone: every caption in "
    "this paper is 'Figure N' and nothing else, so words is 2 and no title is transcribed "
    "[caption.words].",
    "A caption that sits inside its own raster is typed-from-crop even when the same words appear "
    "elsewhere in the text layer, because those occurrences are prose pointers and not the printed "
    "caption: that is Figures 2 and 3, transcribed off the crop [caption.verbatim].",
    "A caption printed above the plotted marks is position 'above', which is every figure here "
    "except Figure 1 whose label prints under the three bands [caption.position].",
    "A scatter with a fitted curve through it is still scatter and not line: Figure 2's squares are "
    "the data and the decaying curve is unkeyed, so the family follows the marks [geometry.family].",
    "A plot whose marks are discrete glyphs with no connecting stroke is scatter even when the "
    "glyphs trace a staircase, as Figure 6's diamonds do at the 37 ceiling [geometry.family].",
    "A hundred-percent stacked column is bar: Figure 8's filled and vacant shares are columns per "
    "year, so the family follows the mark and the stacking is a geometry detail [geometry.family].",
    "A stacked-band network with no axes is node-link-network: Figure 1's three bands are nodes and "
    "edges, and its three layers are panels rather than repeated measurements [geometry.panel_count].",
    "A pie has no vocabulary word and takes other with an other_note naming the part-to-whole disc "
    "and what the two slices are, which no bar, scatter or diagram class would carry "
    "[geometry.family].",
    "An unkeyed fitted curve is not a legend: Figure 2 draws a curve with no sample, no label and no "
    "equation, so legend stays none [geometry.legend].",
    "A key drawn to the right of the plotted area is outside-right, as Figures 4, 5 and 8 all do - "
    "Figure 4's key sits beside the pie because a pie has no axes to be outside of [geometry.legend].",
    "A figure whose axes carry no titles is recorded with printed_numbers true and the gap named in "
    "the note: Figure 8 prints a percentage scale and every-other-year ticks but titles neither axis "
    "[geometry.printed_numbers].",
    "An exhibit named a page before it prints takes a positive lead_pages: Figure 4 is described on "
    "p11 and prints on p12, and Figure 8 is named on p13 and prints on p14 [mention.lead_pages].",
    "An exhibit never named in the prose takes first_page None with count 0 and an empty style list "
    "rather than a guess: no sentence anywhere in this paper names Figure 2 [mention.count].",
    "A pointer whose sentence has the figure's own tick labels spliced into it is quoted exactly as "
    "the text layer prints it, splice and all, because that is what the page says "
    "[mention.lead_sentence].",
]

NOTE = """Paper 89, Team 39160. Seventeen pages, nine measured regions over six of them, and the nine
resolve into EIGHT exhibits: page 4 carries the identical box [33.8, 264.1, 296.3, 502.6] twice, so
Figure 1's raster is measured twice and the distinct-key count is eight. No exclusions, nothing
refused, unaccounted zero. The paper prints no table of any kind - 'Table' appears twelve times in
the text layer and never once with a number.

The paper has eight figures and NOT ONE CAPTION DESCRIBES ITS FIGURE. Every printed caption is the
bare label "Figure N": two words, no title, no unit, no variable list, no source, no conditions. It
is the emptiest caption set this lane has recorded, and it puts the whole burden of saying what a
picture is on the prose - which for Figure 2 never comes, because no sentence anywhere in the paper
names it. Figures 2 and 3 print even their bare label inside the raster rather than as live text, so
those two captions are typed from the crops.

The extraction of pp13 and p14 is also the worst interleaving this lane has hit short of a full
two-column paste. The prose sentences that name Figures 6, 7 and 8 arrive with the figure's own axis
titles and tick values spliced through them - "When HR is not able to work on at least 2/3 of Figure 7
the current vacant 160 positions, the number 150 140 Number of Vacancies of vacancies
compounds/increases 130 120 every year" - so the pointer sentence is quoted exactly as printed,
splice and all, rather than reconstructed.

What the pictures show, read off the crops. Figure 1 is the ICM supervision network drawn as three
stacked bands, nodes labelled 0-17, and it is the only figure whose caption position is below: the
label prints under the three bands. Nothing on it says which band is which relation; the prose
does. Figure 2 is satisfaction against churn count with a decay curve drawn through the squares and
left completely unkeyed - no label, no legend, no equation - so a reader cannot tell a model fit
from a hand-drawn guide. Figure 3 is satisfaction against performance, a clean linear ridge of
squares with no fitted line at all, in a section whose claim is that the relation holds. Figure 4 is
a greyscale two-slice pie of training against recruitment budget with no percentages and a legend of
two squares. Figure 5 puts three series with three different units on one 0-90 axis, in two greys too
close to tell apart, over a full grid. Figures 6 and 7 are both diamonds rather than lines; Figure 6
tells its story with the flat part of a staircase (HR saturating at 37 positions) and marks no
ceiling, Figure 7 tells its story with a regime change at year 22 and marks no break. Figure 8 is a
hundred-percent stacked column of filled against vacant positions, thirty years, and it draws no
reference line at the 80% threshold every sentence citing it is about.

Citation is thin and lopsided. Eight exhibits, four pointers: Figure 1 on its own page, Figure 3 on
its own page, Figure 4 one page early, Figure 8 one page early, and Figures 5, 6 and 7 each named once
on their own pages - while Figure 2 is never named at all. That is seven of eight exhibits cited at
least once and one never, which is better than the lane's average, but every pointer is a bare
"Figure N shows/is" with no reading of the picture in it."""

PAYLOAD = {
    "paper": PID,
    "layout_sha256": LAYOUT.get("layout_sha256") or LAYOUT.get("sha256", ""),
    "items": ITEMS,
    "tables": [],
    "excluded_regions": [],
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc89-payload.json"
out.write_text(json.dumps(PAYLOAD, ensure_ascii=False, indent=1), encoding="utf-8")
print("items", len(ITEMS), "tables", 0, "rules", len(RULES))
print("wrote", out)
