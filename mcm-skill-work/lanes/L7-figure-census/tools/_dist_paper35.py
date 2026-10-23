"""Hand pass for P-B-2012-15171-ce229936 (Big Long River rafting, 36 pp).

The geometry pass measures 22 regions over 16 pages. The paper numbers twenty-two
exhibits `Figure 1` … `Figure 22` and every one of them is measured, one printed number
per region:

    Figure 1   p13-r1  boats failing against max start time
    Figure 2   p13-r2  campsite utilization against minimum nights for the slow boat
    Figure 3   p14-r1  the same utilization plot one optimisation further
    Figure 4   p15-r1  failure rate F against DX at Y = 100
    Figure 5   p15-r2  utilization mu against DX at Y = 100
    Figure 6   p16-r1  failure rate F against campsite count Y at DX = 7
    Figure 7   p17-r1  total trips per season against campsite count Y
    Figure 8   p17-r2  per-campsite utilization along the river
    Figure 9   p19-r1  unplaceable rafts against rafts added each day
    Figure 10  p19-r2  campsite utilization against rafts added each day
    Figure 11  p20-r1  failed rafts against campsite count
    Figure 12  p20-r2  utilization against campsite count
    Figure 13  p21-r1  mean trip length of failed boats against rafts added each day
    Figure 14  p21-r2  mean speed of failed boats against rafts added each day
    Figure 15  p22-r1  total placed boats against rafts added each day
    Figure 16  p24-r1  schematic of a boat's stopping position between campsites
    Figure 17  p30-r1  probability of a 14-mile extra run, fast boat, far campsites
    Figure 18  p31-r1  … fast boat, medium-distance campsites
    Figure 19  p32-r1  … fast boat, close campsites
    Figure 20  p33-r1  … slow boat, far campsites
    Figure 21  p34-r1  … slow boat, medium-distance campsites
    Figure 22  p35-r1  … slow boat, close campsites

Accounting: 22 figure items, 0 counted tables, 0 exclusions = 22 regions.

`Table 1: Parameters` is printed on p5 and is not a measured region: the geometry pass
finds no graphic block on that page, so the table is a declared gap and is not counted.

Families, read off cropped page proxies:

* `scatter` is Figures 1-7 and 9-15: one axes each, filled circular or diamond markers
  (most carrying short capped error bars), printed tick numbers on both axes, no legend,
  no connecting line and no bars. Figure 8 is the exception in that run.
* `bar` is Figure 8: one solid bar per campsite along a common zero baseline, axis titles
  "Campsite" and "mu".
* `flowchart-or-schematic` is Figure 16: an annotated one-dimensional drawing of the river,
  "First Launch" to "Final Exit", with raft glyphs, an `x` mark, three `D` spacing labels
  and a `delta` arrow; no axes and no plotted data.
* `line` is the six appendix figures 17-22: five or six smooth probability curves per
  panel, a heavy horizontal 1% cutoff rule, a boxed in-plot legend keyed to P(fast) and a
  boxed parameter note, one axes each.

Section paths avoid the plot-title lines that `context_extract` reports as headings
("18 Time Optimization (DX = 6 y = 100)", "80 Minimum Nights for Slow Boat …",
"100 Campsite mu (Y=100, DX = 6)"): those are in-plot titles, not numbered headings.

Usage: python -I tools/_dist_paper35.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2012-15171-ce229936"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}
HEADKIND = {h["label"]: h["kind"] for h in CTX["headings"]}


def ctext(page: int, start: str, stop: str | None = None) -> str:
    """The printed caption as the text layer carries it, cut at `start`..`stop`.

    The plotting package leaves in-plot titles and axis tick numbers in the text layer
    next to the caption, so every caption here is cut out of the page text between an
    explicit opening and the first token of whatever follows it on the page.
    """
    text = schema.page_text(PID, page)
    i = text.find(start)
    if i < 0:
        raise KeyError((page, start))
    cut = text[i:]
    if stop:
        j = cut.find(stop)
        if j < 0:
            raise KeyError((page, stop))
        cut = cut[:j]
    return cut.strip()


AGENT = "5.2 Agent-based model"
ITIN = "5.3 Itinerary Model"
APPX = ["7 Appendix", "7.1 Probabilistic Model"]

PATH = {
    13: [AGENT, "5.2.2 Optimizations"],
    14: [AGENT, "5.2.3 Results"],
    15: [AGENT, "5.2.3 Results"],
    16: [AGENT, "5.2.3 Results"],
    17: [AGENT, "5.2.3 Results"],
    19: [ITIN, "5.3.2 Results"],
    20: [ITIN, "5.3.2 Results"],
    21: [ITIN, "5.3.2 Results"],
    22: [ITIN, "5.3.2 Results"],
    24: ["5.4 Probability Model"],
}
for _p in range(30, 36):
    PATH[_p] = list(APPX)

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# accounted regions per page, counted first so doc_order stays monotonic
VENTION = {13: 2, 14: 1, 15: 2, 16: 1, 17: 2, 19: 2, 20: 2, 21: 2, 22: 1, 24: 1,
           30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route = PATH[page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": True,
        "section_kind": HEADKIND[route[-1]],
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str, position: str) -> dict:
    return {
        "verbatim": text,
        "numbering": "Figure N:",
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": position,
    }


def figure(page: int, reg: int, family: str, caption: str, *, panels: int = 1,
           legend: str = "none", numbers: bool = True, labels: bool = False,
           mention: dict | None = None, note: str = "") -> None:
    ORDER.append((page, reg))
    blocking = dict(mention) if mention else dict(NULL_MENTION)
    if blocking["first_page"] is not None and blocking["lead_pages"] is None:
        blocking["lead_pages"] = page - blocking["first_page"]
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": panels,
        "caption_verbatim": caption,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": blocking,
        "caption": caption_block(caption, "below"),
        "geometry": {
            "family": family,
            "panel_count": panels,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            trail: str = "", count: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": trail,
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": None}


ERRBAR = ("One axes: dark filled markers carrying short capped error bars, printed tick "
          "numbers on both axes, no legend, no colour bar, no connecting line.")
POINTS = ("One axes: dark filled circular markers only, printed tick numbers on both "
          "axes, no legend, no colour bar, no connecting line.")

CURVES = ("One axes: thin solid curves, no markers, one heavy black horizontal rule at the "
          "1% cutoff, a boxed inside legend keyed P(fast) = .1 … .9, and a boxed note of the "
          "location, site spacing and campsite count used for that run.")


def build() -> str:
    # 5.2.2 and 5.2.3 - the agent-based optimisation plots
    figure(13, 1, "scatter",
           ctext(13, "Figure 1:", "80 Minimum Nights"),
           note="Failure share against the latest permitted start time, in-plot title "
                "'Time Optimization (DX = 6 y = 100)'; y axis '% of boats failing to find "
                "camp' 2-18, x axis 'Max Start Time (hrs)' 8-16. " + POINTS)
    figure(13, 2, "scatter",
           ctext(13, "Figure 2:", "5.2.3 Results"),
           note="Campsite utilization against the minimum number of nights allowed for the "
                "slow boat, in-plot title 'Minimum Nights for Slow Boat (DX = 6 y = 100)'; "
                "y axis 'Utilization of camp sites' 66-80, x axis 'Minimum Nights Slow "
                "Boat' 6-14. " + POINTS)
    figure(14, 1, "scatter",
           ctext(14, "Figure 3:", "on how to optimize"),
           note="The near-duplicate of Figure 2 one optimisation setting later, printed "
                "with the same caption wording and the same two axes; the markers now lie "
                "on a clean rising diagonal. " + POINTS)
    figure(15, 1, "scatter",
           ctext(15, "Figure 4:", "µ vs. ∆X (Y = 100)"),
           mention=mention(14, ["Figure 4"], "Figure 4 shows our results.", "direct"),
           note="Failure rate F against the day-length margin DX at 100 campsites: markers "
                "cluster near zero below the carrying capacity then climb linearly; y axis "
                "'% of boats failing to find camp' 0-100, x axis 'DX' 0-10. " + POINTS)
    figure(15, 2, "scatter",
           ctext(15, "Figure 5:", None),
           mention=mention(14, ["Figure 5"],
                           "Figure 5 shows how increasing the number of boats launched each "
                           "day increases the percent of campsites utilized each night for "
                           "the season.", "direct"),
           note="Utilization mu against the day-length margin DX: a saturating point cloud "
                "flattening toward 100 per cent; y axis the single symbol 'mu' 0-100, x "
                "axis 'DX' 0-10. " + POINTS)
    figure(16, 1, "scatter",
           ctext(16, "Figure 6:", "In this model the carrying capacity"),
           note="Failure rate F against the number of campsites Y at DX = 7: markers decay "
                "to the baseline and flatten along it; y axis '% of boats failing to find "
                "camp' 0-10, x axis 'Y' 50-400. " + POINTS)

    # 5.2.3 continued - the season-scale plots
    figure(17, 1, "scatter",
           ctext(17, "Figure 7:", "100 Campsite"),
           mention=mention(16, ["Figure 7"],
                           "Figure 7 demonstrates how the carrying capacity of the river "
                           "increases as the number of camp sites available increases.",
                           "direct"),
           note="Total trips per season against campsite count: markers rising linearly, "
                "reaching about 1170 trips at 100 campsites as the text states; y axis 'X' "
                "0-2500, x axis 'Y' 0-250. " + POINTS)
    figure(17, 2, "bar",
           ctext(17, "Figure 8:", "5.3 Itinerary Model"),
           mention=mention(16, ["Figure 8"],
                           "Figure 8 shows the percent utilization of each campsite.",
                           "direct"),
           note="Campsite utilization per campsite along the river: one solid bar per "
                "campsite on a common zero baseline, the bars low before mile 20 and after "
                "mile 90 and highest through the middle; y axis 'mu' 0-100, x axis "
                "'Campsite' 0-100. No error bars, no legend.")
    figure(19, 1, "scatter",
           ctext(19, "Figure 9:", "µ vs. ∆X (Y = 100)"),
           mention=mention(18, ["Figure 9"],
                           "Figure 9 shows the plot of unplaceable rafts vs the number of "
                           "rafts added to the river when Y = 100.", "direct"),
           note="Unplaceable rafts against rafts added each day for the itinerary model, "
                "in-plot title 'F vs. DX (Y = 100)'; y axis 'Failed rafts' -100 to 500, x "
                "axis 'Rafts added each day' 0-12. " + ERRBAR)
    figure(19, 2, "scatter",
           ctext(19, "Figure 10:", "for ∆X ≤ 6"),
           mention=mention(18, ["Figure 10"],
                           "Figure 10 shows the plot of campsite utilization vs. the number "
                           "of rafts added to the river each day.", "direct"),
           note="Campsite utilization against rafts added each day, in-plot title "
                "'mu vs. DX (Y = 100)'; y axis 'Campsite Utilization (%)' 0-100, x axis "
                "'Rafts added each day' 0-12. " + ERRBAR)
    figure(20, 1, "scatter",
           ctext(20, "Figure 11:", "µ vs. Y (∆X = 7)"),
           note="Failed rafts against campsite count at DX = 7: error-bar markers falling "
                "toward zero as campsites are added; y axis 'Failed Rafts' -100 to 700, x "
                "axis 'Campsites' 0-200. " + ERRBAR)
    figure(20, 2, "scatter",
           ctext(20, "Figure 12:", "heuristic for boat placement"),
           note="Utilization against campsite count at DX = 7: a descending ladder of "
                "error-bar markers; y axis 'Utilization (%)' 30-100, x axis 'Campsites' "
                "0-200. " + ERRBAR)
    figure(21, 1, "scatter",
           ctext(21, "Figure 13:", "9 v of Failed Boats"),
           mention=mention(22, ["Figure 13"], "This can be seen in Figure 13.", "direct"),
           note="Mean trip length n of the failed boats against rafts added each day, "
                "in-plot title 'n of Failed Boats vs. DX (Y = 100)'; y axis 'n of Failed "
                "Boats' 7-16, x axis 'Rafts Added Each Day' 0-20. The prose cites this "
                "plot from p22 to show failure is uncorrelated with trip length. " + ERRBAR)
    figure(21, 2, "scatter",
           ctext(21, "Figure 14:", "Figure 15 shows"),
           mention=mention(22, ["Figure 14"],
                           "However, as seen in Figure 14, the average speed of failed "
                           "boats is approximately 7.5 when ∆X = 7, right at the carrying "
                           "capacity.", "parenthetical"),
           note="Mean speed v of the failed boats against rafts added each day, in-plot "
                "title 'v of Failed Boats vs. DX (Y = 100)'; y axis 'v of Failed Boats' "
                "3-9, x axis 'Rafts Added Each Day' 0-20. " + ERRBAR)
    figure(22, 1, "scatter",
           ctext(22, "Figure 15:", "to the carrying capacity estimates"),
           mention=mention(21, ["Figure 15"],
                           "Figure 15 shows the total number of boats that could be "
                           "successfully placed using the greedy algorithm described in "
                           "section 5.3.1.", "direct"),
           note="Total placed boats T against rafts added each day: diamond markers with "
                "very short bars rising steeply then flattening near 1400 boats; y axis "
                "'Total rafts accommodated' 0-1600, x axis 'Rafts added each day' 0-12. "
                + ERRBAR)

    # 5.4 - the geometry diagram
    figure(24, 1, "flowchart-or-schematic",
           ctext(24, "Figure 16:", "The ‘x’ on Figure 16"),
           legend="none", numbers=False, labels=True,
           mention=mention(24, ["Figure 16"],
                           "The ‘x’ on Figure 16 is the spot where the boat in question "
                           "wishes to stop.", "direct"),
           note="Drawn art, not data graphics: a horizontal river rule running 'First "
                "Launch' to 'Final Exit' with short tick partitions, five black triangular "
                "raft glyphs at irregular intervals, an 'x' mark with a small open hull "
                "glyph under it to the left and three 'D' labels spanning successive gaps "
                "to the right, plus a downward 'delta' arrow. No axes, no scales, no tick "
                "numbers; the letters w, D and delta are the diagram's own variables.")

    # 7.1 - the six appendix probability panels
    appendix = [
        ("Figure 17:", None, False,
         "Fast boat, far campsites: six curves (P(fast) = .1 … .9) plus the heavy 1% cutoff "
         "rule, x axis 'Number of Boats' 0-100, y 0-.25, site spacing 7.5 miles and 29 "
         "campsites in the note box."),
        ("Figure 18:", None, False,
         "Fast boat, medium-distance campsites: five curves, y 0-.20 in steps of .02, "
         "spacing 3.75 miles and 59 campsites."),
        ("Figure 19:", None, False,
         "Fast boat, close campsites: five curves, y 0-.06, spacing 1.25 miles and 99 "
         "campsites."),
        ("Figure 20:", None, False,
         "Slow boat, far campsites: five curves, y 0-.25, spacing 7.5 miles and 29 "
         "campsites."),
        ("Figure 21:", None, False,
         "Slow boat, medium-distance campsites: five curves, y 0-.25, spacing 3.75 miles "
         "and 59 campsites."),
        ("Figure 22:", None, False,
         "Slow boat, close campsites: five curves with the steepest tails of the six, y "
         "0-.07, spacing 1.25 miles and 99 campsites."),
    ]
    for (label, stop, labels, note), page in zip(appendix, range(30, 36)):
        figure(page, 1, "line", ctext(page, label, stop), legend="inside",
               numbers=True, labels=labels, note=note + " " + CURVES)

    rules = [
        "Every one of the twenty-two regions carries a printed 'Figure N:' caption, so the "
        "items and the numbers pair one-to-one and the paper contributes no table rows "
        "[caption.verbatim].",
        "Figures 1-7 and 9-15 are unconnected marker clouds - most with short capped error "
        "bars - on printed tick frames, so they are scatter and not line or bar "
        "[geometry.family].",
        "Figure 8 is the one bar chart in the paper: a single solid bar per campsite on a "
        "common zero baseline [geometry.family].",
        "Figure 16 is drawn art with no axes, no tick numbers and no plotted values, so it "
        "is flowchart-or-schematic and printed_numbers is false [geometry.printed_numbers].",
        "The six appendix panels are the only figures with an in-plot legend, boxed inside "
        "the frame and keyed to P(fast) [geometry.legend].",
        "The appendix panels carry printed tick numbers but their axis titles sit inside the "
        "plot as prose, so data_labels records the parameter note box "
        "[geometry.data_labels].",
        "Ten figures are cited in running text within one page of the exhibit: 4, 5, 7, 8, 9, "
        "10 and 15 from the page before, 13 and 14 from the page after, and 16 on its own "
        "page [mention.lead_sentence].",
        "Figures 11 and 12 are introduced on p18 but printed two pages later on p20, so no "
        "mention row is recorded for them [mention.first_page].",
        "Caption text is cut out of the page text between the 'Figure N:' label and the next "
        "token on the page, because the plotting package leaves in-plot titles and tick "
        "numbers in the same text run [caption.verbatim].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "B-15171-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER],
        "tables": [],
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twenty-two measured regions, twenty-two accounted: twenty-two figure items, no "
            "counted tables and no exclusions. All twenty-two printed figure numbers attach "
            "one-to-one to a measured region. Declared gap: 'Table 1: Parameters' is printed "
            "on p5 and the geometry pass measures no block on that page, so it is recorded "
            "here and not counted. Section paths use the numbered headings only; the "
            "plot-title lines that context_extract reports as headings ('18 Time "
            "Optimization (DX = 6 y = 100)', '80 Minimum Nights for Slow Boat (DX = 6 y = "
            "100)', '100 Campsite mu (Y=100, DX = 6)') are in-plot titles and are not used."
        ),
    }
    out = PROXY / "pb35-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
