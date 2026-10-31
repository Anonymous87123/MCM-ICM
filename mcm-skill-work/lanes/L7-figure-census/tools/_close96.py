"""Close paper 96 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-B-2016-42745-4dc9ed2b"

ROW = (
    "| 96 | P-B-2016-42745-4dc9ed2b | mcm-9a | closed 2026-10-24 sha 4dc9ed2b48ba9415 "
    "layout 5f74a621729554d3 (figures=25 tables=3 excluded=15 unaccounted=0; 26 pages, 43 measured "
    "regions over 15 of them, resolving into TWENTY-FIVE FIGURE ROWS, THREE TABLE ROWS and FIFTEEN "
    "EXCLUSIONS - ten of the exclusions are prose blocks whose text lines are drawn as paths, four "
    "are the image tiles that make up Figure 4, one is the references list; THE CAPTION IS A NUMBER "
    "AND NOTHING ELSE - twenty-four figures print a label and eighteen of those are the bare form "
    "'Figure N', while Figure 1 appends a citation marker, Figure 6 a data-source credit and Figures "
    "13 to 16 the parameter of the run ('4%', '3%', '2%', 'logarithm'), so not one caption contains "
    "a word describing its exhibit, and the three tables print no caption and no number at all; ONE "
    "PICTURE IS PRINTED NINE TIMES - the 1000 by 1000 debris matrix (grey grid, X and Y 0 to 1000, a "
    "central void about 300 cells across, a dense ring at 700 to 800 cells, in-plot title 'Simulation "
    "Space Debris Distribution') appears as the executive summary's teaser on p2, as Figure 5, as "
    "Figures 8, 10 and 12 beside the profit charts and as Figures 13 to 16 at four increase rates, "
    "all nine boxes at the identical aspect 1.117 and at four printed sizes 0.179, 0.088, 0.064 and "
    "0.045 of the page; CITATION IS CLOSE TO ABSENT - only Figures 1 to 5 are named by a sentence, "
    "all five on the pages they print on ('Figure 1 shows ... in LEO; Figure 3 is ... in LEO', "
    "'shown in figure 2' in the lower case, 'and derive Figure 4', 'can be vividly shown in the "
    "following Figure 5, Figure 5' where the pointer's own trailing label collides with the printed "
    "one), and Figures 6 to 24 are pointed at only by phrases that name nothing; TWO EXHIBITS "
    "CONTRADICT THE SENTENCES BESIDE THEM - Figure 6 prints the observed launch catalogue (markers "
    "falling to 40 and climbing back to 150 between 2001 and 2015) with an UNKEYED dotted trend "
    "while the text says the model starts at 110 satellites and 'will increase by 5% each year', and "
    "Figures 7, 9 and 11 print the title 'The Profits v.s. the Number of Debris remaining' over a "
    "right axis labelled 'Debris left' with no unit on that axis; THE PAYOFF MATRICES ON P23 READ BY "
    "UNDERLINING - 4 by 4 grids with one vertical rule and one header rule, no box and no interior "
    "lines, where the two Nash equilibria the prose names are marked only by underlining '(-21,-8.4)' "
    "and '(-27,-11.7)' in the first matrix and the single equilibrium of the new standards by "
    "underlining '(-19.5,-3.3)' in the second, and no line of text explains the convention; families "
    "bar 11, scatter 10, line 2, histogram 1, heatmap-or-contour 1, table-grid 3) |"
)

READ = (
    "| 96 | P-B-2016-42745-4dc9ed2b | 26 | 43 | 25 | 3 | closed, `check.py` layout identical, "
    "unaccounted 0; 43 measured regions over 15 of 26 pages resolving into 25 figure rows, 3 tables "
    "and 15 exclusions; 18 of the 24 printed figure labels are the bare form 'Figure N' and no "
    "caption describes its exhibit; one 1000 by 1000 debris-matrix picture is printed nine times at "
    "one aspect and four sizes, four of those printings distinguished only by a parameter suffix; "
    "only Figures 1 to 5 are ever named by a sentence; Figure 6 plots the observed launch catalogue "
    "against a text that assumes 5% annual growth, and the profit charts' titles say 'remaining' "
    "where their right axis says 'left'; the two payoff matrices mark their Nash equilibria by "
    "underlining alone |"
)

prefix = f"| 96 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 96 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
