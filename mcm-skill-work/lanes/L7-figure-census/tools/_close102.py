"""Close paper 102 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-C-2016-52815-2e6f0093"

ROW = (
    "| 102 | P-C-2016-52815-2e6f0093 | mcm-9a | closed 2026-10-24 sha 2e6f0093 "
    "layout 791caee29a9c3886 (figures=6 tables=0 excluded=3 unaccounted=0; 18 pages, 9 measured "
    "regions over 6 of them, resolving into SIX FIGURE ROWS and THREE EXCLUSIONS - a prose page set as "
    "one full-page raster, the second panel of a two-panel figure, and an 'Algorithm 1' pseudocode "
    "listing - with nothing unaccounted; TWO PRINTED TABLES HAVE NO MEASURED REGION AT ALL AND ARE "
    "DECLARED GAPS: Table 1 ('Schools | Year One .. Year Five | Total | ROI', unruled text columns, "
    "caption above, p14 into p15) caps every school's five-year total near 50,000,000 with its two p14 "
    "rows landing just over at 50,017,570 and 50,011,398, and Table 2 (p15 into p16) lets Georgia "
    "Perimeter College take 220,954,796 and prints ROI to four decimals where Table 1 prints three, its "
    "first nine values inside 92.5848 to 92.5870 against Table 1's 145.520 down to 2.585; THE TWO "
    "RESIDUAL DIAGNOSTICS ARE READ IN OPPOSITE DIRECTIONS IN CONSECUTIVE PARAGRAPHS - p9 has Figure 4 "
    "showing variance DECREASING as the fitted value rises and Figure 5, drawn from the same two "
    "columns, showing error INCREASING with it, and neither plot carries the reference line that would "
    "settle it (Figure 4 has no zero line, Figure 5 no identity line, the Q-Q of Figure 3 no 45-degree "
    "line); FIGURES 4 AND 5 PRINT RAW SOFTWARE AXIS NAMES, 'ypred' against 'resids' and 'ypred' against "
    "a bare 'y', with no unit on either; FIGURE 1 IS SELF-CONTRADICTORY - an in-frame title 'Dark "
    "represents missing data' over a binary red/black matrix, then a continuous colour bar ticked 0 to "
    "20 outside the right edge with no label and no unit - its ~200 variable names are printed rotated "
    "and overlapping so the paper concedes 'the names of which are not intended to be legible', and THE "
    "CITING SENTENCE SWAPS ITS AXES ('the x axis represents cases, the y variables' against a chart "
    "printing observation number on the y); FIGURE 2 ASSERTS A FIT IT NEVER REPORTS - no R squared, "
    "slope, residual error or n on the figure, the sentence reading only 'The model fit looks "
    "surprisingly good', over a band that spans 0.015 to 0.082 at one abscissa value with the line "
    "drawn out past every observation; FIGURE 6'S TWO PANELS CARRY NO (a)/(b) AND NO SCHOOL NAMES, so "
    "only the prose identifies School A as the steep curve, and the same annotation is printed "
    "'Changing Funding' in one panel and 'Change in Funding' in the other; the caption pass weld body "
    "sentences onto two of the six captions ('... Structure of Data either to public or private schools "
    "and is rectified in the python script.' and '... Funding Distribution each iteration until all our "
    "funds are depleted.') and the recorded verbatims are the caption lines alone; families scatter 4, "
    "heatmap-or-contour 1, line 1) |"
)

READ = (
    "| 102 | P-C-2016-52815-2e6f0093 | 18 | 9 | 6 | 0 | closed, `check.py` layout identical, "
    "unaccounted 0; 9 measured regions over 6 of 18 pages resolving into 6 figure rows and 3 exclusions "
    "(a prose page set as a full-page raster, the second panel of a two-panel figure, an 'Algorithm 1' "
    "pseudocode listing); two printed tables - Table 1 p14 into p15 and Table 2 p15 into p16, both "
    "unruled eight-column text grids - produced NO measured region and are declared gaps; p9 reads "
    "Figure 4 as variance decreasing with the fitted value and Figure 5 as error increasing with it, and "
    "neither plot carries a zero or identity line, while the Q-Q of Figure 3 has no 45-degree line; "
    "Figures 4 and 5 label their axes 'ypred', 'resids' and 'y'; Figure 1's title says dark means "
    "missing over a continuous 0-to-20 colour bar, and the citing sentence swaps its axes; Figure 2 "
    "reports no statistic; Figure 6's two panels carry no letters and no school names; two captions have "
    "body sentences welded to their tails |"
)

prefix = f"| 102 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 102 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
