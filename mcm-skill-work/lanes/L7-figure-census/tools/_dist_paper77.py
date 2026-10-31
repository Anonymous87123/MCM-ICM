"""Hand census of P-B-2015-38720-26d38781 (Team 38720, 61 pages, 47 measured regions).

The paper prints thirty-seven numbered figures and one unnumbered table picture; it also prints
three variable-definition grids that the region pass never returned, declared as a gap below.

   p1  r1  refused - summary-sheet cover form
   p7  r1  Fig.1   map-or-plan-view      search area of MH370
   p8  r1  Fig.2   composite-panel       five cells: world map plus three count panels
   p15 r1  Fig.3   flowchart-or-schematic diagram of the search area
   p16 r1  none    table-as-figure       aircraft specification grid, heading above, no number
   p17 r1  Fig.4   scatter               the distributed search area
   p17 r2  Fig.5   surface-or-3D         the same distribution in 3-D
   p18 r1  Fig.6   photo-or-raster-image radar console screenshot, bare caption
   p22 r1  Fig.7   scatter               5000 simulated crashes
   p23 r1  refused - inline standard-error equation
   p24 r1  refused - inline vector equation
   p24 r2  Fig.8   scatter               random vector generation
   p25 r1  Fig.9   line                  example random flight path
   p27 r1  Fig.10  scatter               random bounded path vectors
   p27 r2  Fig.11  line                  example bounded random flight path
   p28 r1  Fig.12  histogram             bounded random histogram
   p29 r1  refused - inline equation
   p29 r2  refused - inline equation
   p29 r3  Fig.13  flowchart-or-schematic weighted bounded random vector generation
   p30 r1  Fig.14  line                  weighted bounded random trial
   p31 r1  Fig.15  histogram             weighted bounded random histogram
   p33 r1  Fig.16  flowchart-or-schematic striped vector generation
   p33 r2  Fig.17  line                  striped trial example
   p34 r1  Fig.18  histogram             striped path histogram
   p36 r1  Fig.19  flowchart-or-schematic spiral striped vector generation
   p36 r2  Fig.20  line                  spiral striped random trial
   p37 r1  Fig.21  histogram             spiral striped histogram
   p38 r1  refused - inline equation
   p38 r2  refused - inline equation
   p39 r1  Fig.22  line                  sinusoidal vector generation
   p39 r2  Fig.23  line                  sinusoidal example trial
   p40 r1  Fig.24  histogram             sinusoidal histogram
   p42 r1  refused - inline equation
   p42 r2  refused - inline equation
   p44 r1  Fig.25  surface-or-3D         3-D normal distribution
   p44 r2  Fig.26  line                  2-D normal distribution
   p44 r3  Fig.27  line                  2-D Bayesian search method, first pass
   p45 r1  Fig.28  line                  2-D Bayesian search method, second pass
   p46 r1  Fig.29  histogram             Bayesian histogram
   p47 r1  Fig.30  histogram             striped uncertain histogram
   p49 r1  Fig.31  histogram             Bayesian Cessna histogram
   p51 r1  Fig.32  flowchart-or-schematic two planes diagram
   p52 r1  Fig.33  histogram             two planes histogram
   p53 r1  Fig.34  scatter               95% CI, random solutions
   p53 r2  Fig.35  scatter               95% CI, nonrandom solutions
   p54 r1  Fig.36  scatter               95% CI, discovery uncertainty
   p56 r1  Fig.37  line                  human survival time in cold water

Thirty-eight figure rows and nine refusals, no tables in the measured list and nothing
unresolved. The three unmeasured printed grids are declared in the note and the rules.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2015-38720-26d38781"
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

# Letter page, 612 x 792 pt; the text block runs x 72 to 540, so the measure is 468 pt
MEASURE = 468.0
DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def pct(span: float) -> str:
    return f"{span / MEASURE * 100:.1f}"


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


def none_mention() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": "direct",
            "read_sentences": 1, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


# ---------------------------------------------------------------- section paths
# The heading index never returns the Solution headings - they are set in the body face, not
# the display face - so those labels are typed from the printed headings, each checked against
# the text layer of the page it prints on.
SEC_HIST = ["2 Research", "2.3 Analysis of the History of Ocean Plane Crashes"]
SEC_SCEN = ["3 Foundation of Analysis", "3.2 Determining a Realistic Scenario"]
SEC_CALC = ["3 Foundation of Analysis", "3.3 Search Plane Calculations"]
SEC_51 = ["5 Models", "5.1 Normal Distribution"]
SEC_511 = SEC_51 + [q("Solution 5.1.1: Completely Random Flight Path", 24)]
SEC_512 = SEC_51 + [q("Solution 5.1.2: Bounded Random Flight Path", 26)]
SEC_513 = SEC_51 + [q("Solution 5.1.3: Bounded Weighted Random Flight Path", 29)]
SEC_514 = SEC_51 + [q("Solution 5.1.4: Descending Striped Flight Path", 32)]
SEC_515 = SEC_51 + [q("Solution 5.1.5: Spiral Striped Flight Path", 35)]
SEC_516 = SEC_51 + [q("Solution 5.1.6: Sinusoidal Flight Path", 38)]
SEC_52 = ["5 Models", "5.2 Normal Distribution with Discovery Uncertainty"]
SEC_521 = SEC_52 + [q("Solution 5.2.1: Bayesian Adjusted Flight Paths", 44)]
SEC_522 = SEC_52 + [q("Solution 5.2.2: Spiral Striped Flight Path", 47)]
SEC_61 = ["6 Solution Stability",
          q("6.1 Bayesian Adjusted Flight Path with a lost Cessna 172", 49)]
SEC_62 = ["6 Solution Stability", "6.2 Two Planes Flying Striped Patterns"]
SEC_71 = ["7 Results", "7.1 The Normal Distribution Model"]
SEC_72 = ["7 Results", "7.2 Discovery Uncertainty Model"]
SEC_81 = ["8 Conclusion", "8.1 Recommendation"]


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "single",
           legend: str = "none", numbers: bool = True, labels: bool = False,
           three_d: str = "no", position: str = "below", shared_axes: bool = False,
           note: str = "", other_note: str = "", confidence: str = "high") -> None:
    """Every caption on this paper is typeset as part of the picture, so all are typed from the
    crop: the text layer holds not one of the thirty-seven caption strings."""
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": confidence,
        "other_note": other_note,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": "typed-from-crop",
        "note": note,
        "place": place(page, reg, kind, path),
        "mention": mention,
        "caption": caption(cap_text, numbering, position),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "reason": reason,
        "note": note,
    })


# ---------------------------------------------------------------- refusals
excluded(1, 1, "not-an-exhibit",
         ("The summary sheet's cover form: Team Control Number 38720 and Problem Chosen B in "
          "their boxes, with the four T and four F office-use rules either side, all above the "
          "title block. No artwork and no caption, and the abstract's own text prints below it "
          "as live text."))
for _pg, _reg, _what in ((23, 1, "standard error of the mean"), (24, 1, "the update of the "
                         "search-plane position vector"), (29, 1, "the bounded weighted random "
                         "step toward A"), (29, 2, "the bounded weighted random step toward B"),
                         (38, 1, "the sinusoidal update rule"), (38, 2, "the sinusoidal turn "
                         "condition"), (42, 1, "the posterior containment probability"),
                         (42, 2, "the containment probability of the searched cell")):
    excluded(_pg, _reg, "fragment-of-other",
             (f"A display equation of {_what} set as an inline picture inside running text: "
              "typeset mathematics in a wide strip, with no frame, no axes, no marks and no "
              "caption. It is not an exhibit."))

# ---------------------------------------------------------------- figures
figure(7, 1, "map-or-plan-view", "Figure 1: Search Area of Malaysia Flight 370",
       "Figure N:",
       cited(7, 7, ["Figure 1"], 1,
             "From the information from MH370 (Figure 1), we determined the search area to be "
             "basically rectangular in shape"),
       "other", SEC_HIST, legend="inside", numbers=False, note=(
           "A regional map of the eastern Indian Ocean and Western Australia: shaded land, blue "
           "bathymetry, a pale coastline, the search area marked along a red arc with an arrow, "
           "and a three-entry key box inside the frame plus a scale bar and a world-locator "
           "inset. The only geographic frame in the paper, and the only figure whose legend sits "
           "inside the picture."))
figure(8, 1, "composite-panel", "Figure 2: Total Missing Aircraft", "Figure N:",
       cited(7, 8, ["Figure 2"], 1,
             "These flights vary in type from transatlantic to shorter hops between (Figure 2)"),
       "other", SEC_HIST, panels=5, layout="map above a row of 4", legend="inside",
       numbers=True, labels=True, other_note=(
           "A world map with callout dots joined by great-circle lines, over a row of three "
           "count panels (a bare 89 with its phrase, a Land/Sea pie, a five-slice type pie) and "
           "a year-range timeline. Five cells of four different kinds in one frame."), note=(
           "One pasted infographic rather than a chart: the map carries the geography, the "
           "number block the headline count, the two pies the splits, and the timeline the year "
           "histogram drawn as rows of plus signs. Every panel prints its own numbers, and the "
           "pie slices are labelled by leader line rather than by a key box. Logos and "
           "publisher fine print sit in the bottom-right corner."))
figure(15, 1, "flowchart-or-schematic", "Figure 3: Diagram of Search Area", "Figure N:",
       cited(15, 15, ["Figure 3"], 1,
             "we are also going to include the corners bordering the circles in our search area "
             "(Figure 3)"),
       "model", SEC_SCEN, labels=True, note=(
           "A drawn construction, not a plot: two dashed circles inside a long rectangle on a "
           "dotted centreline, the tangent chords marked, a radius labelled r, the chord gap "
           "labelled L and the four points A, A', B', B lettered on the axis. It defines the "
           "search area the rest of section 3 works in."))
figure(16, 1, "table-as-figure", "Types of Potential Lost Planes", "none", none_mention(),
       "model", SEC_SCEN, numbers=True, labels=True, position="above", note=(
           "A specification grid pasted in as a picture: three aircraft columns by eight rows "
           "of performance data, the Boeing 777 column picked out in blue bold, source numbers "
           "in the header. Its heading stands above the frame and it never receives a figure or "
           "table number, which is why it is recorded with numbering none and its heading typed "
           "as the caption."))
figure(17, 1, "scatter", "Figure 4: Realistic Distributed Search Area", "Figure N:",
       cited(17, 17, ["Figure 4"], 1,
             "taking this into account makes the distribution significantly more complex "
             "(Figure 4)"),
       "model", SEC_SCEN, numbers=True, note=(
           "A dot cloud of several thousand simulated end points, banded tight about the "
           "mid-line and thinning to the frame edges, inside the blue search-area rectangle with "
           "the red centreline drawn across it. Axes carry only the italic captions y (miles) "
           "and x (miles) and a handful of numerals."))
figure(17, 2, "surface-or-3D", "Figure 5: Normally Distributed 3-D Graph", "Figure N:",
       cited(17, 17, ["Figure 5"], 1,
             "as along the rest of the flight Therefore, we can path (Figure 5)."),
       "model", SEC_SCEN, numbers=True, three_d="surface-mesh", note=(
           "The same distribution as the Figure 4 cloud, drawn in perspective: one shaded bell "
           "surface over a boxed floor, its peak offset to the right of the centre, each axis "
           "wall ticked and titled, and the vertical axis running 0.000 to 0.020. The paper's "
           "first 3-D plot."))
figure(18, 1, "photo-or-raster-image", "Figure 6", "Figure N", none_mention(),
       "model", SEC_CALC, legend="inside", note=(
           "A screenshot of the P-3 radar console: a polar scope with range rings and an azimuth "
           "scale, a bright swept sector, and four embedded instrument insets at the corners. "
           "Nothing in it is plotted-by-the-authors data, so it is a raster, not a chart. Its "
           "caption is the bare string 'Figure 6' with no title at all, which is why the "
           "verbatim is two words and the numbering keeps the number without a colon."))
figure(22, 1, "scatter", "Figure 7: 5000 Normally Distributed Plane Crashes", "Figure N:",
       none_mention(), "model", SEC_51, numbers=True, note=(
           "The distribution shown at full simulation size: five thousand points inside the "
           "search box, pierced by the red centreline, with the vertical axis labelled 100 to "
           "-100 and the horizontal axis ticked but given only its title. It repeats the Figure "
           "4 construction at larger n."))
figure(24, 2, "scatter", "Figure 8: Random Vector Generation", "Figure N:", none_mention(),
       "model", SEC_511, legend="outside-right", numbers=True, labels=True, note=(
           "A vector construction drawn over the search box: the crashed plane as a green dot, "
           "the search plane as a magenta dot on the red A-B line, dotted construction lines and "
           "a short arrow showing the step from the previous position to the next, with the "
           "three position symbols printed on the art and a three-entry key box outside the "
           "frame on the right."))
figure(25, 1, "line", "Figure 9: Example Random Flight Path", "Figure N:", none_mention(),
       "solution", SEC_511, numbers=True, note=(
           "One simulated path: a single black polyline that wanders across the search box and "
           "sprawls far outside it, down to -800 on the vertical scale. This one row is the "
           "first of seven trial figures that each pair a plotted path with a histogram of the "
           "search time."))
figure(27, 1, "scatter", "Figure 10: Random Bounded Path Vector", "Figure N:", none_mention(),
       "solution", SEC_512, legend="outside-right", numbers=True, labels=True, note=(
           "The bounded version of the vector construction: the same box, baseline and two dot "
           "colours, but three successive search-plane positions lettered on the art with dotted "
           "links and one near-vertical step, so the drawing shows the bounding rule rather than "
           "one path."))
figure(27, 2, "line", "Figure 11: Example Bounded Random Flight Path", "Figure N:",
       cited(27, 27, ["Figure 11"], 1,
             "Figure 11 shows a typical solution as it moves according to the bounded random "
             "flight path."),
       "solution", SEC_512, numbers=True, note=(
           "A bounded trial: a dense tangle of black segments confined inside the left half of "
           "the search box, the path kept within the frame the way the previous figure's rule "
           "demands. Caption is the only figure caption in the paper's body text layer at all - "
           "the layer holds it because the sentence that introduces it happens to start with the "
           "words 'Figure 11'."))
figure(28, 1, "histogram", "Figure 12: Bounded Random Histogram", "Figure N:",
       none_mention(), "result", SEC_512, numbers=True, note=(
           "The search-time distribution of the bounded random runs: orange bars rising from a "
           "zero baseline, tallest at the left near 43 and decaying rightwards with one isolated "
           "bar near the far right. Axis titles Frequency and Amount of Time (Hours). The bars "
           "have visibly unequal widths, so it is a histogram in name and a binned bar chart in "
           "fact."))
figure(29, 3, "flowchart-or-schematic", "Figure 13: Weighted Bounded Random Vector Generation",
       "Figure N:", none_mention(), "model", SEC_513, legend="outside-right", numbers=True,
       labels=True, note=(
           "The weighted construction: the search box, the two search-plane positions lettered "
           "with the step between them, the two normals toward B drawn as solid and dashed "
           "arrows, the distances d_A and d_B and the 15-to-1 weighting printed on the art, plus "
           "the green crashed-plane dot. Both axes carry their titles and the vertical one "
           "prints 'y (mies)' - the paper's own typo survives into the record."))
figure(30, 1, "line", "Figure 14: Weighted Bounded Random Vector Trial", "Figure N:",
       none_mention(), "solution", SEC_513, numbers=True, note=(
           "The weighted trial: a dense fan of black polylines all starting from one point at the "
           "left edge of the box and wandering across it - the many-run version of a single "
           "path, and the only trial figure in the paper that draws more than one simulated "
           "path in the same frame."))
figure(31, 1, "histogram", "Figure 15: Weighted Bounded Random Histogram", "Figure N:",
       none_mention(), "result", SEC_513, numbers=True, note=(
           "Search times for the weighted runs: orange bars on a horizontal axis that runs to "
           "300 hours - four times the reach of any other histogram in the paper - with the peak "
           "at the far left. The weighting is what buys the long thin tail."))
figure(33, 1, "flowchart-or-schematic", "Figure 16: Striped Vector Generation", "Figure N:",
       none_mention(), "model", SEC_514, legend="outside-right", numbers=True, labels=True,
       note=(
           "The striped construction: the search box, the plane's points at A, B and the corners, "
           "a grey horizontal line marking the offset, a 2d dimension arrow and the short "
           "turn segments at each end that carry the plane down to the next stripe. Same box and "
           "labels as the earlier constructions, with the key box beside the frame."))
figure(33, 2, "line", "Figure 17: Striped Trial Example", "Figure N:", none_mention(),
       "solution", SEC_514, numbers=True, note=(
           "One striped trial: five straight black lines across the top of the box at 90, 70, "
           "50, 30 and 10 miles, one short return segment and a single dot where the plane was "
           "found. The stripes are drawn as they are flown, so the picture is the plan itself "
           "rather than a wandering path."))
figure(34, 1, "histogram", "Figure 18: Striped Path Histogram", "Figure N:", none_mention(),
       "result", SEC_514, numbers=True, note=(
           "Search times for the striped runs: eleven outlined orange bars peaking near 16 in the "
           "sixth to eighth bins and tapering to one or two at both ends - the only symmetric "
           "histogram in the paper, and the only one whose bars are outlined in black as well as "
           "filled."))
figure(36, 1, "flowchart-or-schematic", "Figure 19: Spiral Striped Vector Generation",
       "Figure N:", none_mention(), "model", SEC_515, legend="outside-right", numbers=True,
       labels=True, note=(
           "The striped construction: two pairs of horizontal lines inside the search box, one "
           "pair above and one below the red baseline, joined by curved arrows that carry the "
           "plane from one stripe to the next, with the arc s_0 and the track space 2d bracketed "
           "on the art and a two-entry key box outside the frame."))
figure(36, 2, "line", "Figure 20: Spiral Striped Random Trial", "Figure N:", none_mention(),
       "solution", SEC_515, numbers=True, note=(
           "One striped trial: two near-horizontal black lines crossing most of the frame and a "
           "single dot where the plane was found. The emptiest exhibit in the paper - the path "
           "degenerates to two straights, and it still rates a full figure."))
figure(37, 1, "histogram", "Figure 21: Spiral Striped Histogram", "Figure N:", none_mention(),
       "result", SEC_515, numbers=True, note=(
           "The spiral striped search times: eleven orange bars from a peak near 17 down to "
           "isolated single counts, on the same Frequency against Amount of Time (Hours) frame "
           "as Figure 12."))
figure(39, 1, "line", "Figure 22: Sinusoidal Vector Generation", "Figure N:", none_mention(),
       "model", SEC_516, legend="outside-right", numbers=True, labels=True, note=(
           "The sinusoidal construction: one curve oscillating about the red baseline across the "
           "whole box, violet dots at A on the left edge, two successive crests bracketed as 2d, "
           "and the arc s_0 marked near the start. Same frame and same two-entry key box as "
           "Figure 19."))
figure(39, 2, "line", "Figure 23: Sinusoidal Example Trial", "Figure N:", none_mention(),
       "solution", SEC_516, numbers=True, note=(
           "One sinusoidal trial: the trail confined to the left fifth of the box along the "
           "baseline, ending in a spike and a small dot, with the rest of the frame empty. "
           "Mirrors Figure 20's shape in the other direction."))
figure(40, 1, "histogram", "Figure 24: Sinusoidal Histogram", "Figure N:", none_mention(),
       "result", SEC_516, numbers=True, note=(
           "The sinusoidal search times: twelve orange bars declining from about 34 with a "
           "secondary step near 9 to 10 hours and isolated low bars out to 30. Third of the four "
           "identical orange histograms."))
figure(44, 1, "surface-or-3D", "Figure 25: 3D Normal Distribution", "Figure N:",
       cited(44, 44, ["Figure 25"], 1,
             "A three-dimensional (Figure 25) and two-dimensional graph (Figure 26) of the "
             "initial distribution are displayed below"),
       "model", SEC_521, numbers=True, three_d="surface-mesh", note=(
           "The initial probability distribution in perspective, the second 3-D surface in the "
           "paper and the same bell as Figure 5 with the red centreline drawn on the surface "
           "itself. It pairs with the flat version printed beside it."))
figure(44, 2, "line", "Figure 26: 2D Normal Distribution", "Figure N:",
       cited(44, 44, ["Figure 26"], 1,
             "A three-dimensional (Figure 25) and two-dimensional graph (Figure 26) of the "
             "initial distribution are displayed below"),
       "model", SEC_521, numbers=True, note=(
           "The same distribution seen flat: a filled bell curve with the mean marked by a "
           "vertical line, on Probability against y (miles). Printed beside Figure 25 and cited "
           "in the same sentence as it, which is the only place in the paper where two figures "
           "share one citing sentence."))
figure(44, 3, "line", "Figure 27: 2D Bayesian Search Method (1)", "Figure N:",
       cited(44, 44, ["Figure 27"], 1,
             "can be either the strip centered at y=20 mi or the strip centered at y=-20 mi, "
             "because they are equivalent (Figure 27)."),
       "model", SEC_521, numbers=True, labels=True, note=(
           "The first search pass drawn on the distribution: the bell curve, a purple shaded "
           "band marking the searched strip, two 2d double arrows spanning the band edges and a "
           "callout reading Next Search Area. It is the only figure in the paper that annotates "
           "the art with a printed instruction."))
figure(45, 1, "line", "Figure 28: 2D Bayesian Search Method (2)", "Figure N:",
       cited(45, 45, ["Figure 28"], 1,
             "Now, the location of the third pass can be determined by finding the highest "
             "remaining probability distribution, here centered around y=-20 miles (Figure 28)."),
       "model", SEC_521, numbers=True, labels=True, note=(
           "The second-pass update: the wide original bell and a narrow curve on the same axes "
           "showing what the distribution has become, the purple band and the Next Search Area "
           "callout carried over from Figure 27."))
figure(46, 1, "histogram", "Figure 29: Bayesian Histogram", "Figure N:", none_mention(),
       "result", SEC_521, numbers=True, note=(
           "Search times for the Bayesian runs: contiguous orange bars peaking near 5 hours and "
           "decaying rightwards, on Frequency up to 120. The tallest-scaled histogram in the "
           "paper."))
figure(47, 1, "histogram", "Figure 30: Striped Uncertain Histogram", "Figure N:",
       none_mention(), "result", SEC_522, numbers=True, note=(
           "The striped uncertain runs: orange bars drawn as closely spaced pairs of differing "
           "height, decaying left to right on Frequency to 80. The only histogram in the paper "
           "whose bars are visibly paired, which is the striped pattern showing through the bin "
           "structure."))
figure(49, 1, "histogram", "Figure 31: Bayesian Cessna Histogram", "Figure N:", none_mention(),
       "result", SEC_61, numbers=True, note=(
           "Search times for the Cessna case: orange bars from a peak near 77 down to near zero "
           "by 25 hours, the largest peak count in any of the paper's histograms."))
figure(51, 1, "flowchart-or-schematic", "Figure 32: Two Planes Diagram", "Figure N:",
       none_mention(), "model", SEC_62, numbers=True, note=(
           "A bare construction of the two-plane case: the search box, three green segments "
           "along the upper half and two orange segments below the baseline, one ending on a "
           "black dot. No arrows, no labels and no key - the plainest schematic in the paper."))
figure(52, 1, "histogram", "Figure 33: Two Planes Histogram", "Figure N:", none_mention(),
       "result", SEC_62, numbers=True, note=(
           "Search times for the two-plane runs: bars peaking near 20 in the first two bins, "
           "decaying to a single count by 7 hours on a 0 to 15 scale."))
figure(53, 1, "scatter", "Figure 34", "Figure N", none_mention(), "result", SEC_71,
       legend="outside-right", numbers=True, note=(
           "Ninety-five per cent confidence intervals for the two random solutions: two capped "
           "vertical whiskers at fixed categorical positions, black about 43 hours and blue "
           "about 38, with no line joining them and no points. A bare caption - the string "
           "'Figure 34' and nothing else - and a two-entry key box."))
figure(53, 2, "scatter", "Figure 35", "Figure N", none_mention(), "result", SEC_71,
       legend="outside-right", numbers=True, note=(
           "The same interval construction for the four nonrandom solutions: four capped "
           "whiskers at fixed positions on a 0 to 9 scale, black, blue, green and amber, with a "
           "four-entry key box. Printed directly below Figure 34 as its comparable pair."))
figure(54, 1, "scatter", "Figure 36", "Figure N", none_mention(), "result", SEC_72,
       legend="outside-right", numbers=True, labels=True, note=(
           "Intervals for the three discovery-uncertainty cases: three capped whiskers on a 0 to "
           "10 scale, each annotated beside the bar with its found percentage (95%, 80%, 82%). "
           "Bare caption like its two predecessors."))
figure(56, 1, "line", "Figure 37: Human Survival Time in Cold Water", "Figure N:",
       none_mention(), "other", SEC_81, legend="inside", numbers=True, note=(
           "Five rising curves in three line styles on Survival time against Water temperature, "
           "labelled High, Medium and Low insulation, with three horizontal double arrows "
           "spanning the gaps between adjacent curves near 30 hours. The only figure in the "
           "paper that is neither a simulated distribution nor a schematic of the search "
           "geometry."))

# ---------------------------------------------------------------- rules and note
RULES: list[str] = [
    "The single finding of this paper's census is that not one caption is quotable: the text "
    "layer holds thirty-seven numbered figures and not one of the thirty-seven caption strings. "
    "Every caption is typeset as part of the pasted picture, or set in a face the extraction "
    "drops, so all thirty-eight rows carry typed-from-crop and none could be checked against "
    "the page text [caption.verbatim].",
    "Families spread wide because the paper is a simulation study: eleven line plots, nine "
    "histograms, seven scatters, five schematics, two 3-D surfaces, one map, one raster "
    "screenshot, one pasted table and one five-cell infographic. No categorical bar chart, no "
    "box plot, no node-link network, no heatmap and no contour plot anywhere in sixty-one pages "
    "[geometry.family].",
    "Numbering is 'Figure N:' for thirty-three of the thirty-seven printed figures and the bare "
    "'Figure N' with no colon and no title for four of them: Figure 6 under the radar "
    "screenshot, and Figures 34, 35 and 36 under the three confidence-interval plots "
    "[caption.numbering].",
    "Every caption prints BELOW its picture without exception, thirty-eight rows in and not one "
    "above; the pasted aircraft grid on p16 is the only region whose label stands above it, and "
    "that label is a heading, not a caption, so it is recorded with numbering none and position "
    "above [caption.position].",
    "Citation is almost absent: of thirty-eight rows only nine are ever named in prose (Figures "
    "1, 2, 3, 4, 5, 11, 25, 26, 27 and 28), and eight of those nine names are inside a "
    "parenthesis in a sentence that also carries something else. Twenty-eight rows carry an "
    "empty mention. Every one of the nine is cited on the page it prints on: no figure leads or "
    "trails its citing sentence by even one page [mention.count].",
    "Two figures share one citing sentence - Figures 25 and 26, 'A three-dimensional (Figure 25) "
    "and two-dimensional graph (Figure 26) of the initial distribution are displayed below' - "
    "which is the only sentence in the paper that names two figures at once [mention.count].",
    "Three variable-definition grids print on pp13, p14 and p41 and NONE of them is in the "
    "measured roster: the region pass returned no region on any of those three pages although "
    "each carries twenty-nine, thirty and fourteen long rules. They are declared here as the "
    "paper's table gap rather than recorded as table rows, because no measured region exists to "
    "anchor them [place.area_frac].",
    "The exhibits come in matched runs, and the runs are the real structure: the five later "
    "search methods each get a vector-generation schematic, a single trial and a search-time "
    "histogram, in that order and with no exception - Figures 10, 11, 12 for the bounded random, "
    "13, 14, 15 for the weighted, 16, 17, 18 for the striped, 19, 20, 21 for the spiral and 22, "
    "23, 24 for the sinusoidal. The first method, the completely random one, gets only the first "
    "two, because the paper says most of its simulations never finish and no mean can be "
    "established, so no histogram could be drawn [place.doc_order].",
    "One frame carries most of the paper: sixteen of the thirty-eight rows are drawn inside the "
    "same blue-bordered search box on x 0-550 and y +-100 miles with the red centreline across "
    "it, from Figure 4 through Figure 33, so the same rectangle is redrawn sixteen times with "
    "different marks inside it [geometry.family].",
    "Legend placement splits cleanly: eight rows carry a key box outside the frame on the right "
    "(Figures 8, 10, 13, 16, 19, 22, 34, 35 and 36), four carry theirs inside the picture "
    "(Figures 1, 2, 6 and 37), and the other twenty-six print no key at all "
    "[geometry.legend].",
    "Area does not separate exhibit from furniture: the refusal on p1 measures 0.206 of the "
    "sheet, larger than the paper's first numbered figure, and five of the nine refusals are "
    "inline equation strips under 0.03 that were measured only because the picture is a raster "
    "[place.area_frac].",
    "Section paths are assembled by hand: the heading index returns the table of contents on "
    "pp2-3 as headings, misses all eight printed 'Solution N.N.N:' headings because they are "
    "set in the body face, and returns the running word Conclusion seven times as a heading. "
    "Each path here is the printed chain with its matching page [place.section_path].",
]

NOTE = (
    "Paper 77, Team 38720, sixty-one pages, a 2015 paper on searching for a plane lost over the "
    "ocean. Forty-seven measured regions: thirty-eight exhibit rows and nine refusals, nothing "
    "unaccounted and nothing unresolved. The paper prints thirty-seven numbered figures and "
    "every one of them is here; the thirty-eighth row is the aircraft specification grid on p16, "
    "which is pasted in as a picture and never numbered.\n\n"
    "The one thing to know about this paper is that no caption reaches the text layer. All "
    "thirty-seven captions are painted into the pictures, so every one was read off the crop and "
    "typed in, and the layer's whole contribution to the census is a single sentence on p27 that "
    "happens to begin with the words 'Figure 11'. Three of the captions are bare - 'Figure 6', "
    "'Figure 34', 'Figure 35', 'Figure 36' - with no title, no colon and nothing after the "
    "number.\n\n"
    "What is drawn is a simulation study's whole apparatus. Six search methods are presented in "
    "the same three-beat rhythm - a schematic of the vector rule, one sample trial and a "
    "histogram of the search times across a hundred runs - and only the first of the six breaks "
    "it, because its paths never finish and so never produce a search time to bin. Around them "
    "sit the search-geometry "
    "figures, all drawn in one shared frame - a blue search box on a miles grid with a red "
    "centreline - and a small block of Bayesian figures on distributions instead of paths.\n\n"
    "Two exhibits are pictures rather than charts: the p18 radar console screenshot, which is "
    "the only raster in the census and carries the barest caption in the paper, and the p8 "
    "infographic, five cells of four different kinds - a world map of missing aircraft, a bare "
    "count, two pies and a year timeline - pasted in whole from the Aviation Safety Network. The "
    "p16 aircraft specification grid is a fourth kind: a printed table preserved as an image, "
    "which is why it is a table-as-figure row and not a table row.\n\n"
    "Three printed tables are missing from the record and that is a declared gap, not an "
    "oversight: the Lost Plane Variables grid on p13, the Search Variables grid on p14 and the "
    "Discovery Uncertainty variables on p41 are drawn as closed rule boxes of twenty-nine, "
    "thirty and fourteen rules, and the region pass returned nothing on any of those pages even "
    "though it flagged them. No measured region exists, so no table row could be anchored there.\n\n"
    "Citation is the weakest part of the paper. Twenty-eight of the thirty-eight exhibits are "
    "never named in prose at all; the nine that are get a parenthetical pointer at best, and "
    "only Figures 25 and 26 share a sentence. The figure numbers do run in order and nobody "
    "skips, which is more than several papers in this lane manage."
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

out = PROXY / "pc77-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
