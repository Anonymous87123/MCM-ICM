"""Close paper 88 in CLAIMS.md, the recovery file and the README progress table.

Same upsert shape as _close8586.py: an existing row for the same number and pid is replaced, never
duplicated, and the README row goes in before the `| 121 |` anchor.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-D-2015-38996-1efe10af"

ROW = (
    "| 88 | P-D-2015-38996-1efe10af | mcm-9a | closed 2026-10-24 sha 6aeb84678b2cd8c3 "
    "layout f49e4c7246ff90da (figures=11 tables=5 excluded=3 unaccounted=0; 21 pages, 19 measured "
    "regions over 9 of them; families line 6, table-grid 5, bar 2, flowchart-or-schematic 2, "
    "other 1; ONE DRAWING ARRIVES AS FOUR REGIONS - Figure 8 is a single system-dynamics diagram of "
    "three dotted clusters (Society, Economic, Environment & Resources) and 23 boxes, but the three "
    "sub-graphs are pasted as their own bitmaps inside the outer vector drawing, so the 0.29-area "
    "vector region is the exhibit and the three raster pieces inside it repeat clusters already in "
    "it and are excluded as duplicates; THE RULE-ONLY BLIND SPOT IS HIT AGAIN - Table 1, 'the "
    "process of calculation of weighting process', prints on p9 as a run of text with no rules, "
    "owns no measured region and is declared a gap, and it is the one grid the paper never cites "
    "while Tables 2-6 are all drawn and all named; Figure 7 is two pasted column charts under one "
    "printed caption over the same 22 index numbers on different y windows (0-0.0015 and 0-0.005), "
    "neither axis titled, a quarter of the bars at exactly zero; Figures 9 and 10 share an axis "
    "frame with NO axis titles and NO units, and in Figure 10 the four programmes sit on top of "
    "each other until the last third of the window; Figure 6's two confidence bands (0.8 grey, "
    "0.95 light blue) are keyed only in the sentence above the figure; Figure 1's Level-1 circles "
    "break every indicator name mid-word ('Labor force participat ion rate') and print 'Education' "
    "twice as a Level-2 box; Figure 2 ticks both axes only at 0 and 1, squeezes four year markers "
    "into an unreadable cluster and lets rotated ray labels collide with the theta arc; Figure 3 "
    "has no axes at all and is recorded as other with an other_note; Figure 4 labels each country "
    "path with 2003/2012 only and prints '2012' twice inside America's; Table 2 is transposed "
    "(countries across, one measure down) and colours two distances red with no key; Table 3 is "
    "nine grey boxes in three rows in index order though the prose calls it a ranking, prints NO "
    "header row (header_rows recorded as 1 because the schema has no zero) and leaves its last "
    "cell empty; Table 4 colours its one rejection red and its acceptances green with no legend; "
    "Table 5 is three unrelated lists of 5, 10 and 8 estimated equations side by side, wrapping "
    "onto unindented continuation lines; Table 6's four proposals agree to the fourth decimal in "
    "three of four years, so the ranking it is meant to support is not visible in its own numbers; "
    "citation is regular on this paper - Figure 7 and Table 5 named a page before they print, "
    "Table 6 a page before its grid, Figure 2 named a page after it once parenthetically) |"
)

READ = (
    "| 88 | P-D-2015-38996-1efe10af | 21 | 19 | 11 | 5 | closed, `check.py` layout identical, "
    "unaccounted 0; 19 measured regions over 9 of 21 pages = 11 figure rows + 5 grids + 3 "
    "exclusions; Figure 8 is ONE diagram measured as four regions because its three sub-graphs are "
    "pasted bitmaps inside the outer vector drawing, so the three pieces are duplicates of clusters "
    "already in the 0.29-area exhibit; Table 1 prints on p9 as ruleless text with no measured "
    "region and is declared a gap, and it is the only grid never cited; Figure 7 is two pasted "
    "column charts under one caption on different y windows, neither axis titled, a quarter of the "
    "bars at zero; Figures 9 and 10 have no axis titles and no units and in Figure 10 the four "
    "programmes overlap until the last third; Figure 6's confidence bands are keyed only in prose; "
    "Table 2 is transposed with two unkeyed red cells, Table 3 prints no header row and ends in an "
    "empty cell, Table 5 holds three unrelated equation lists side by side, Table 6 cannot show the "
    "ranking it argues for |"
)

claims = LANE / "CLAIMS.md"
recovery = LANE / "CLAIMS-rows-mcm-9a.md"

prefix = f"| 88 | {PID} |"
for path in (claims, recovery):
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(path.name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 88 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README", "rows", len(rows))
