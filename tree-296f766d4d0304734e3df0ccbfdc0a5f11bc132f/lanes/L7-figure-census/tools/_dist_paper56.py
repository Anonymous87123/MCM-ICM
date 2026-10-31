"""Hand pass for P-A-2014-31333-acc8bc3b (a 2014 A paper that replays the Nagel-Schreckenberg
cellular-automaton traffic model over four rule systems and charts average flow and average
accidents for twelve simulation types), 17 PDF pages.

Eight measured regions over four pages, all exhibits and nothing else: eight grouped bar charts,
one flow chart and one accident chart per rule system, on pages 8 to 11. No exhibit in this paper
carries a number at all - the chart titles are drawn inside the artwork and the text layer prints
no caption line anywhere - so every row records an empty caption, `caption_source` none and
numbering none.

    p8-r1   bar   AVERAGE FLOW RATES OF RIGHT HAND RULE
    p8-r2   bar   RIGHT HAND RULE AVERAGE ACCIDENTS
    p9-r1   bar   AVERAGE FLOW RATES OF NO RULES
    p9-r2   bar   AVERAGE ACCIDENTS OF NO RULES
    p10-r1  bar   AVERAGE FLOW RATES OF NO CHANGE RULE
    p10-r2  bar   AVERAGE ACCIDENTS FOR NO CHANGE RULE
    p11-r1  bar   AVERAGE FLOW RATES OF MIDDLE LANE RULE
    p11-r2  bar   AVERAGE ACCIDENTS FOR MIDDLE LANE RULE

Usage: python -I tools/_dist_paper56.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2014-31333-acc8bc3b"
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

RES = "4 Results"
FIGS = "4.2 Figures"
RIGHT = "4.2.1 Right Hand Rule"
NORULE = "4.2.2 No Rules"
NOCHANGE = "4.2.3 No Lane Changes"
MIDDLE = "4.2.4 Middle Lane Rule"

PATH: dict[tuple[int, int], tuple[list[str], str]] = {
    (8, 1): ([RES, FIGS, RIGHT], "other"),
    (8, 2): ([RES, FIGS, RIGHT], "other"),
    (9, 1): ([RES, FIGS, NORULE], "other"),
    (9, 2): ([RES, FIGS, NORULE], "other"),
    (10, 1): ([RES, FIGS, NOCHANGE], "other"),
    (10, 2): ([RES, FIGS, NOCHANGE], "other"),
    (11, 1): ([RES, FIGS, MIDDLE], "other"),
    (11, 2): ([RES, FIGS, MIDDLE], "other"),
}

VENTIONS = {8: 2, 9: 2, 10: 2, 11: 2}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
PAGE_SEEN: dict[int, int] = {}

INTRO_FIGURES = ("The figures presented on the following pages summarize the data that were "
                 "collected for each of the four")
MIDDLE_POINTER = "This can be seen in the second figure of Section 4.2.4"


def deictic(first_page: int, lead_pages: int, quote: str) -> dict:
    """A pointer that prints no exhibit number, so it counts as zero named citations."""
    return {"first_page": first_page, "lead_pages": lead_pages, "style": [], "count": 0,
            "lead_sentence": quote, "trail_sentence": "", "lead_pattern": "direct",
            "read_sentences": 1, "gap_sentences": None}


MENTION = {
    1: deictic(7, 1, INTRO_FIGURES),
    2: deictic(7, 1, INTRO_FIGURES),
    3: deictic(7, 2, INTRO_FIGURES),
    4: deictic(7, 2, INTRO_FIGURES),
    5: deictic(7, 3, INTRO_FIGURES),
    6: deictic(7, 3, INTRO_FIGURES),
    7: deictic(7, 4, INTRO_FIGURES),
    8: deictic(12, -1, MIDDLE_POINTER),
}


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route, kind = PATH[(page, reg)]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": PAGE_SEEN[page] + sum(VENTIONS[p] for p in VENTIONS if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def figure(page: int, reg: int, key: int, *, legend: str = "outside-right",
           labels: bool = False, note: str = "") -> None:
    ORDER.append((page, reg))
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": "bar",
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": "",
        "caption_source": "none",
        "note": note,
        "place": place(page, reg),
        "mention": dict(MENTION[key]),
        "caption": {
            "verbatim": "",
            "numbering": "none",
            "words": 0,
            "sentences": 0,
            "units": False,
            "variables": False,
            "variable_count": 0,
            "conditions": False,
            "concludes": False,
            "voice": "none",
            "position": "below",
        },
        "geometry": {
            "family": "bar",
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": True,
            "data_labels": labels,
        },
    }


def build() -> str:
    figure(8, 1, 1,
           note="Grouped vertical bars over twelve simulation types - Fast/Slow x Computer / "
                "Accident Prone / Normal x Heavy/Light - with five lane-count series in a "
                "darkening grey ramp, keyed OUTSIDE the frame at the right as 'two lanes' to "
                "'six lanes'. The in-image title is 'AVERAGE FLOW RATES OF RIGHT HAND RULE', "
                "with 'Average Cars/unit of time' up the y axis to 4 and 'Simulation Type' "
                "under the rotated x labels. Complete frame, horizontal gridlines at every tick, "
                "no vertical gridlines, no data labels. The tick label 'Fast-Accident "
                "Proine-Light' is the paper's typo. No group draws all five series, so the "
                "legend promises more bars than any group shows [geometry.legend].")
    figure(8, 2, 2,
           note="The accident twin of the same simulation grid: 'RIGHT HAND RULE AVERAGE "
                "ACCIDENTS' over the same twelve types, y 'Average Number of Accidents' 0 to "
                "2000 by 200, same five-series grey legend outside right, complete frame and "
                "horizontal gridlines. Two of the twelve groups carry all the bars - "
                "Fast-Accident Prone-Heavy reaching 1800 and Slow-Accident Prone-Heavy about "
                "1500 - and the rest are near-empty, which is the shape the accident counts "
                "really have [geometry.printed_numbers].")
    figure(9, 1, 3,
           note="The no-rule flow chart: 'AVERAGE FLOW RATES OF NO RULES', five lane series "
                "outside right, y 0 to 4.5 by 0.5 with the highest tick at 4, horizontal "
                "gridlines, complete frame. Two bars reach 3.5 and 3.3 with no headroom label. "
                "Twelve simulation types on the x axis, all legible, this time spelled "
                "'Fast-Accident Prone-Light' correctly, so the typo on p8 is not systematic.")
    figure(9, 2, 4,
           note="The no-rule accident chart. Its legend is corrupt: five swatches are listed "
                "but two of them both read 'three lanes' and no 'four lanes' entry exists, so "
                "the key does not match the five-series key used on the p8 and p10 plates. Ten "
                "of the twelve simulation types show no bars at all, only "
                "Fast-Accident Prone-Heavy (four bars) and Slow-Accident Prone-Heavy (two) "
                "carry any, and y runs 0 to 2500 by 500 [geometry.legend].")
    figure(10, 1, 5,
           note="The no-lane-change flow chart: 'AVERAGE FLOW RATES OF NO CHANGE RULE', five "
                "lane series outside right, complete frame and horizontal gridlines. Its y axis "
                "tops out at 3.5 rather than the 4 of the two earlier flow plates, and its two "
                "tallest bars stop flush against the top rule, so the three flow charts cannot "
                "be read against each other by eye even though they share one legend "
                "[geometry.printed_numbers].")
    figure(10, 2, 6,
           note="The no-lane-change accident chart, titled 'AVERAGE ACCIDENTS FOR NO CHANGE "
                "RULE' - 'FOR' where its siblings read 'OF' or 'OF NO RULES' - with y 0 to 2500 "
                "by 500, five clean legend entries outside right, complete frame. Again only "
                "the two accident-prone-heavy groups are populated, five bars in the first and "
                "three in the second, the tallest just under the 2500 gridline.")
    figure(11, 1, 7,
           note="The middle-lane flow chart: 'AVERAGE FLOW RATES OF MIDDLE LANE RULE', and the "
                "only plate in the paper with a two-entry legend, 'lane three' against 'lane "
                "five', outside right. Same twelve simulation types, y 0 to 3 by 0.5, complete "
                "frame and horizontal gridlines, no data labels.")
    figure(11, 2, 8, labels=True,
           note="The middle-lane accident chart and the ONLY plate in the paper with values "
                "written on the data: 'AVERAGE ACCIDENTS FOR MIDDLE LANE RULE', two lane series, "
                "y 0 to 3000 by 500, with 211.3, 98.8, 66.2, 97.3, 30.6, 102 and 86.1 printed "
                "beside the small bars, while the two tall accident-prone-heavy bars carry no "
                "label at all - the drop from about 2600 to 211 is the point the prose makes "
                "about Section 4.2.4 [geometry.data_labels].")

    rules = [
        "No exhibit in this paper is numbered. Not one of the eight charts has a printed "
        "caption line in the text layer, and no prose sentence cites a figure by number: the "
        "only pointer is the section-4.2 lead 'The figures presented on the following pages "
        "summarize the data that were collected for each of the four', plus one structural "
        "reference on p12. All eight rows therefore record an empty caption, "
        "`caption_source` none and numbering none [caption.numbering].",
        "The chart titles are drawn INSIDE the artwork - 'AVERAGE FLOW RATES OF RIGHT HAND "
        "RULE' and the like - in small caps, so they are quoted in the row notes and are not "
        "mistaken for captions; the caption fields stay empty rather than carrying an in-image "
        "title as if it were a caption [caption.verbatim].",
        "All eight charts are one construction: grouped vertical bars, twelve simulation-type "
        "groups, a grey-to-black ramp of lane-count series keyed outside the frame at the right, "
        "a complete frame, horizontal gridlines at every tick and rotated text labels on the x "
        "axis with no numeric x scale [geometry.family].",
        "Four of the eight are flow charts and four are accident charts, and the flow charts do "
        "not share a y scale: 0 to 4 on p8, 0 to 4 on p9 and 0 to 3.5 on p10, so only the "
        "accident charts (all 0 to 2000, 2500, 2500 and 3000) are even roughly comparable "
        "[geometry.printed_numbers].",
        "The accident plates are mostly empty by nature: accidents only appear in the two "
        "accident-prone-heavy groups, so ten of the twelve x slots carry no bar on most "
        "accident charts. An empty group is not a missing series and is not counted as an "
        "exclusion [geometry.legend].",
        "Two legends are defective. The p9 accident chart lists five swatches of which two both "
        "read 'three lanes' with no 'four lanes' entry, and on the p8 and p9 flow charts no "
        "group draws all five series the legend promises; both are recorded as printed "
        "[geometry.legend].",
        "Exactly one plate writes values onto its data - the p11 accident chart, with 211.3, "
        "98.8, 66.2, 97.3, 30.6, 102 and 86.1 beside the small bars and nothing beside the two "
        "tall ones - so `data_labels` is true on that row alone [geometry.data_labels].",
        "The eight pointers are deictic. Seven rows quote the section-4.2 lead sentence one to "
        "four pages before their plate, and the p11 accident chart quotes the p12 sentence "
        "'This can be seen in the second figure of Section 4.2.4', which points back a page and "
        "by position rather than by number, so it carries `lead_pages` -1 [mention.lead_pages].",
        "Section paths come from the four rule headings the paper prints - 4.2.1 Right Hand "
        "Rule, 4.2.2 No Rules, 4.2.3 No Lane Changes, 4.2.4 Middle Lane Rule - under 4.2 "
        "Figures, so each plate sits on the heading that names the rule it charts instead of on "
        "a flattened 4.2 path [place.section_path].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2014\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "A-31333-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER],
        "tables": [],
        "excluded_regions": [],
        "rules": rules,
        "note": (
            "Eight measured regions over four of seventeen pages, and every one of them an "
            "exhibit: eight grouped bar charts over twelve simulation types, one flow chart and "
            "one accident chart for each of the four rule systems, on pages 8 to 11. Families: "
            "8 `bar`, uniform, no tables, no exclusions, nothing unresolved and no declared "
            "gaps. Not one chart carries a figure number - the titles are drawn inside the "
            "artwork in small caps and the text layer prints no caption line anywhere - so all "
            "eight rows record an empty caption with `caption_source` none, and the only prose "
            "pointers are the section-4.2 lead sentence and one positional reference on p12. "
            "Faults worth carrying downstream: the flow charts use three different y scales "
            "(0-4, 0-4, 0-3.5), the p9 accident legend lists 'three lanes' twice and never "
            "'four lanes', no group on the p8 or p9 flow plates draws all five series the "
            "legend promises, only the p11 accident plate labels its data, and the p8 x labels "
            "print 'Fast-Accident Proine-Light'."
        ),
    }
    out = PROXY / "pc56-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
