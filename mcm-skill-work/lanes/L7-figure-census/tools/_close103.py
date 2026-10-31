"""Close paper 103 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-D-2016-42220-7261f9d3"

ROW = (
    "| 103 | P-D-2016-42220-7261f9d3 | mcm-9a | closed 2026-10-24 sha 7261f9d3 "
    "layout 972cf59afacbfb5a (figures=23 tables=5 excluded=0 unaccounted=0; 21 pages, 28 measured "
    "regions over 15 of them, every one resolving into a census row - TWENTY-THREE FIGURE ROWS AND FIVE "
    "TABLE ROWS, nothing refused; THE NUMBER FIVE IS USED TWICE - p10 prints 'Figure 5 A point source "
    "flow' and p12 prints 'Figure 5 Original network', the citing sentence says only 'Figure 5 and 6', "
    "and both plates print bare edge decimals with nothing saying what they are (eight on 5b, sixteen on "
    "6); TWO CITING SENTENCES NAME THE WRONG FIGURE - p12 reads the sensitivity plate of Figure 7 as "
    "'three lines in Figure 13' and p16 credits the capacity plates of Figures 17 and 18 to 'Figure 11 "
    "and 12'; FOUR FIGURE ROWS ARE NAMED BY NO SENTENCE AT ALL (Figures 10, 11, 14, 19, the media-share "
    "pair, the spread network and the public-opinion curve); PAIRS ARE DRAWN ON INCOMPATIBLE SCALES - "
    "Figures 12 and 13 use 0.25-0.65 against 0.70-0.78 for the same quantity, Figures 15 and 16 use "
    "0-100 against 40-160, and Figures 17 and 18 put a probability and a delay on ONE untitled 0-to-1.2 "
    "axis that is drawn down to -0.2; the media-share plates run to -0.1 on a non-negative share; TABLE "
    "5'S ARITHMETIC FAILS IN ONE CELL - the Internet absolute error prints 0.12 where 0.773 against "
    "0.785 gives 0.012, while the 1.55% beside it is computed from the correct value - and its true "
    "values (newspaper 0.3, Internet 0.773) contradict TABLES 3/4'S market shares for the same country "
    "(0.09, 0.27) with no year in either table; p16 reads Congo's ratio as ending 'lower' than America's "
    "when the plates put it near 35 against America's 10 to 14; Table 2 alone is a closed box with "
    "vertical rules and the only merged cells, Tables 1, 3, 4 and 5 are booktabs, and Tables 3/4 print "
    "their single row label as the clipped 'Weigh'; Figure 3's choropleth has no country labels and a "
    "key whose percentages are relative to nothing stated, Figure 4's seven-country mesh carries no "
    "arrowheads, no legend and no weights, Figure 9's five bars (58, 62, 53, 54, 61) sit on an axis "
    "labelled only 0/40/60 in five colours with no legend, Figure 19 carries three unlabelled reference "
    "rules, and Figures 20 and 21 print their two-entry legends in OPPOSITE orders; families line 14, "
    "node-link-network 6, table-grid 5, bar 1, map-or-plan-view 1, flowchart-or-schematic 1) |"
)

READ = (
    "| 103 | P-D-2016-42220-7261f9d3 | 21 | 28 | 23 | 5 | closed, `check.py` layout identical, "
    "unaccounted 0; 28 measured regions over 15 of 21 pages resolving into 23 figure rows and 5 table "
    "rows with no refusal; Figure 5 numbered twice (p10 point source, p12 original network); p12 cites "
    "Figure 13 while reading Figure 7 and p16 cites Figures 11/12 while reading 17/18; Figures 10, 11, "
    "14 and 19 named by no sentence; Figures 12/13 on 0.25-0.65 vs 0.70-0.78, Figures 15/16 on 0-100 vs "
    "40-160, Figures 17/18 put probability and delay on one untitled axis to -0.2; Table 5's Internet "
    "absolute error prints 0.12 instead of 0.012 and its true values contradict Tables 3/4; Table 2 the "
    "only boxed grid with verticals and merged cells; Figure 19 carries three unlabelled reference "
    "rules; Figures 20/21 key their legends in opposite orders |"
)

prefix = f"| 103 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 103 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
