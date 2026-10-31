"""Close paper 93 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-A-2016-46830-92f43919"

ROW = (
    "| 93 | P-A-2016-46830-92f43919 | mcm-9a | closed 2026-10-24 sha 4f34a23372f23204 "
    "layout 4aa7a4c4b811ec4a (figures=12 tables=9 excluded=3 unaccounted=0; 51 pages, 24 measured "
    "regions over 14 of them, resolving into TWELVE FIGURE ROWS, NINE TABLE ROWS AND THREE "
    "EXCLUSIONS; the paper is table-heavy for a 2016 outstanding paper - every table carries a "
    "printed caption and a number, and the sensitivity block alone supplies SIX IDENTICAL-LOOKING "
    "5x8 AND 2x8 RESPONSE GRIDS (Tables 4 to 9) whose only difference is the row label and the "
    "quantity in the caption, so a reader must read the caption to know whether a cell is water "
    "consumption or outlet temperature; FIGURE 1 IS A DECLARED GAP - its caption prints at the top "
    "of p9 with no art on that page and its node-link chart begins at the foot of p8, where the "
    "extractor boxed only two drawn-text slices ('Forced convection', 'comfort model') instead of the "
    "diagram, and those two slices are excluded as fragment-of-other; FIGURE 3'S CAPTION PRINTS ON "
    "THE PAGE AFTER ITS ART (art at the foot of p12, caption at the top of p13) and the same clip-art "
    "is printed a THIRD time on p44 with no caption and no pointer, excluded as duplicate; FIGURE 10 "
    "IS A SIDE-BY-SIDE PAIR IN ONE FRAME WITH NO PANEL LETTERS - the left column is lettered "
    "'Strategy1' with one decision loop ('While sum<1800 (30 minutes)', sum=sum+beta_t, 'Dispersed "
    "the water in interval within the range of 0 to 1800') and the right column 'Strategy2' with "
    "three ('While Tb< the highest water temperature', 'While Tmin1<Ts', 'While Tmin2<Ts', ending "
    "'Finding the optimal temperature of adding water/draining'), so the row order runs "
    "right-to-left against the reading order; citation is thin - only Figures 7, 8, 11 and 12 are "
    "named by a sentence and Figures 2, 3, 4, 5, 6, 9 and 10 by none, with Figure 8 the paper's only "
    "abbreviated pointer ('(Fig 8)') and FIGURE 11 NAMED AFTER IT IS PRINTED (p33 'Where, T (t ) is "
    "determined Fig11.', one word, no space, no period, so the first mention page is one past the "
    "exhibit page); TWO ARITHMETIC DEFECTS PRINT IN THE TABLES - Table 3's 900 s cell reads '3143814' "
    "with the decimal point missing (its neighbours are 316.0650, 315.1926, 313.6271) and Table 9 "
    "prints POSITIVE '0.03%' in a column where its sibling Table 5 prints '-0.03%', the sign dropped "
    "in a column that is otherwise negative or zero; Table 2 is the only exhibit with a Units column "
    "and Table 3's corner cell is split by a diagonal stroke reading 'T / t'; the two temperature-"
    "field pairs behave very differently - Figures 4 and 5 share one colour bar (40 to 45 deg C) so "
    "their comparison is honest, while Figures 6 and 7 are drawn in two visual idioms (colour-barred "
    "surface against un-barred wire mesh with markers) and cannot be read against one another at all; "
    "SECTION PLACEMENT QUOTES PRINTED LINES WHERE THE HEADING INDEX FAILED - the extractor drops the "
    "numbering from 5.2.1 to 5.2.3 (indexed as bare list lines '1 The shape and volume of the tub' "
    "and '3 Heat transfer rate') and misses 4.1.3 entirely, yet all four print on the page; families "
    "flowchart-or-schematic 5, line 3, heatmap-or-contour 2, surface-or-3D 2, table-grid 9) |"
)

READ = (
    "| 93 | P-A-2016-46830-92f43919 | 51 | 24 | 12 | 9 | closed, `check.py` layout identical, "
    "unaccounted 0; 24 measured regions over 14 of 51 pages resolving into 12 figure rows, 9 tables "
    "and 3 exclusions; Figure 1 is a declared gap (caption on p9, art starting at the foot of p8, "
    "only two drawn-text slices boxed) and the two slices are excluded as fragment-of-other; Figure "
    "3's caption prints on the page after its art and the same clip-art repeats on p44, excluded as "
    "duplicate; Figure 10 is a side-by-side pair with no panel letters whose left column is Strategy "
    "1 and right column Strategy 2, so the row order runs right-to-left; only Figures 7, 8, 11 and 12 "
    "are named by a sentence and Figure 11 is named after it is printed ('determined Fig11.'); Table "
    "3's 900 s cell loses a decimal point ('3143814') and Table 9 flips '-0.03%' to '0.03%' |"
)

prefix = f"| 93 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 93 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
