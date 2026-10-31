"""Close paper 100 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-C-2016-47823-59d82231"

ROW = (
    "| 100 | P-C-2016-47823-59d82231 | mcm-9a | closed 2026-10-24 sha 59d82231 "
    "layout b051a2fd49836d01 (figures=5 tables=7 excluded=4 unaccounted=0; 27 pages, 16 measured "
    "regions over 12 of them, resolving into FIVE FIGURE ROWS, SEVEN TABLE ROWS and FOUR EXCLUSIONS - "
    "three heads or tails of tables that turn the page and one in-body equation fragment - with "
    "nothing unaccounted; THE HEADING AND CAPTION PASSES BOTH COLLAPSE ON THIS PDF because its text "
    "layer writes ONE WORD PER LINE, so the heading index keeps only first words ('Data', 'Analysis', "
    "'Results', 'Testing', 'Appendix'), the caption pass finds NO caption group at all and every "
    "caption was located by hand from its line position, and the section labels recorded are the "
    "indexed labels verbatim rather than the printed headings; TABLE 4 AND THE APPENDIX LIST ARE ONE "
    "TABLE PRINTED TWICE AND THEY DISAGREE - for the ten shared rows the institution and ROI are "
    "identical while the undefined bare-letter column 't' reads 4 5 3 5 3 6 5 5 6 5 in Table 4 against "
    "4 5 3 4 3 5 4 4 5 4 in the appendix, and the merged foot row is worded differently in each "
    "('Utilization rate of funds in each year(%)' against 'of each year (%)'); TABLE 6'S CAPTION NAMES "
    "A STATISTIC ITS ROWS DO NOT PRINT - it reads 'the standard deviation of the investment amount "
    "correspond to the change of MRS k' and the foot row is the ARITHMETIC MEAN of the five rows above "
    "it in each column (10.49% = (12.18+9.09+10.88+7.64+12.67)/5), under a 'Year' column holding 1 to "
    "5 which are PERIOD INDICES and not years; TWO STOCK SCREENSHOTS CITE ONE SOURCE - Figures 1 and 2 "
    "are the same watermarked Foundation Center viewer, 11 subject bars and 28 state bars, both with "
    "every total printed at the bar end and NO AXIS, NO TICK, NO GRIDLINE AND NO SCALE, and the Source "
    "URL under the LOCATION chart is byte for byte the subject-filtered URL under the subject chart; "
    "FIGURE 3 IS A SKETCH WITH NO SCALE - a hand-drawn U against x curve marking delta-x and delta-U "
    "with dashed rectangles, no ticks, no numbers, no gridline, named only on the PAGE AFTER it prints; "
    "FIGURE 4 IS A FIFTEEN-BOX FLOWCHART WITH UNLABELLED ARROWS except the two YES/NO pairs and the "
    "Fletcher-Reeves step the text spends pages on collapsed into one box, named by no sentence, while "
    "FIGURE 5 is a MATLAB convergence curve titled only 'fitness' with a floating 'x 10^20' multiplier, "
    "NO ABSCISSA LABEL AT ALL and a step-shaped best-so-far trace, also named by no sentence; EVERY "
    "TABLE IS REFERRED TO AS 'the table above' OR NOT AT ALL and only two figure rows are ever named; "
    "Table 2 and Table 6 each print their head on one page and their foot on the next and the appendix "
    "list runs p23 to p24, so three measured regions are halves of a table recorded once; the tables "
    "keep raw database headers ('INSTNM'), five year columns headed only 1 to 5 with no year and no "
    "unit, amounts with no currency, an ellipsis row in Table 4, and thirty-one of the appendix's fifty "
    "rows invest exactly 0.00 in at least one year; Table 5's duplicate-focus test is ONE-SIDED (no "
    "Gates school appears in the model's list) and lists 'Land-Grant Universities' as one college; "
    "Table 1 defines nine symbols and neither k nor the yearly amounts; families bar 2, line 2, "
    "flowchart-or-schematic 1, table-grid 7) |"
)

READ = (
    "| 100 | P-C-2016-47823-59d82231 | 27 | 16 | 5 | 7 | closed, `check.py` layout identical, "
    "unaccounted 0; 16 measured regions over 12 of 27 pages resolving into 5 figure rows, 7 tables and "
    "4 exclusions (three table halves split by page turns and one in-body equation fragment); the "
    "heading index collapses to first words and the caption pass finds no caption at all because the "
    "text layer writes one word per line, so every caption was located by hand; Table 4 and the "
    "appendix 'Appendix 1: Recommending List' print the same fifty schools with DIFFERENT integers in "
    "the undefined column 't' for all ten shared rows; Table 6 is captioned 'standard deviation' while "
    "its foot row is the arithmetic mean of the rows above it, under a 'Year' column of period indices; "
    "Figures 1 and 2 are the same watermarked Foundation Center screenshots with no axis, tick or scale "
    "and the same printed source URL; Figure 3 is a hand sketch with no numbers; Figure 4 is a "
    "fifteen-box flowchart with unlabelled arrows and Figure 5 a MATLAB 'fitness' curve with no "
    "abscissa label, neither named by a sentence; every table is cited as 'the table above' or not at "
    "all |"
)

prefix = f"| 100 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 100 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
