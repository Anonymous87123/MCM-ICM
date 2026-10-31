"""Close paper 98 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-B-2016-52221-f8094e57"

ROW = (
    "| 98 | P-B-2016-52221-f8094e57 | mcm-9a | closed 2026-10-24 sha f8094e5745d4f867 "
    "layout 5bd028a066f08b68 (figures=14 tables=6 excluded=1 unaccounted=0; 23 pages, 21 measured "
    "regions over 14 of them, resolving into FOURTEEN FIGURE ROWS, SIX TABLE ROWS and ONE EXCLUSION - "
    "the vector container on p3 that boxes Figures 1 and 2 together - with nothing unaccounted; THE "
    "SCHEMATIC IS PRINTED THREE TIMES - Figure 3 on p5 and Figure 7 on p12 are the same eight-box "
    "diagram with the same two-colour arrow key ('fund flow' orange against 'determine' navy, so the "
    "meaning vanishes in greyscale), Figure 7 adds SIX UNEXPLAINED RED MARKS (three ticks, three "
    "question marks) that no sentence in the paper keys, and the executive summary prints it a third "
    "time on p22 with NO CAPTION AND NO NUMBER behind 'The model is demonstrated in the figure "
    "below:', both named copies carrying the identical caption 'Model Schematic Diagram'; THE "
    "EXHIBIT CITED FOR THE DATA IS A SCREENSHOT OF AN INPUT FORM - Figure 4 is the DAS dialog with "
    "the plot still pending, no curve drawn, four widget labels truncated mid-word ('Duratio', "
    "'Inclinat', 'Type of', 'Orbital A'), the environment misspelled 'Meteroids', so no number in the "
    "paper traces to a picture; NINE AXIS LABELS SAY log AND NONE IS A LOG RULER - every one is "
    "graduated in evenly spaced numbers, and Figures 5 and 8 both run downwards from about minus 1 on "
    "'log(Number of Impacts)', so the reader is shown the log and never the counts; THREE ONE-CURVE "
    "EXHIBITS CARRY A PLURAL TITLE - Figures 9, 10 and 11 are each titled 'Number of Impacts vs. "
    "Impactor Diameter Threshold (Orbital Altitude Contours)' over a single curve at 800, 400 and "
    "2000 km, and the 400 and 2000 km parameter blocks are identical line for line including "
    "'Inclination = 28.50 deg'; Figure 8 prints 'Duration = 1.00 yrs' over an abscissa running 1980 "
    "to 2100 whose curves only begin near 2000; Figure 12's legend reads 'data 7%' to 'data 10%' and "
    "NOTHING IN THE PAPER SAYS WHAT THE PERCENTAGES MEASURE, while Figure 13's four duration curves "
    "nearly superimpose, so the exhibit meant to prove that duration does not matter cannot show it; "
    "THE MATRICES ARE SIX UNCAPTIONED GRIDS in section 6.2.2 sharing one booktabs shape - an empty "
    "stub cell over 'Cost of manufacture | Cost of using | Fitness | Time consuming', no vertical "
    "rule, no box - five of them with four method stubs and two of those dropping Microsatellite for "
    "large debris, and the p14 lower region BOXES TWO OF THEM AT ONCE (five rows and three rows, "
    "header repeated) so one measured region cannot become two rows and the split survives only in "
    "the recorded row count of eight with a second header row; the closed vector reported from those "
    "matrices, 'Then, B = [0.260, 0.310, 0.420]', has three elements for a four-alternative matrix; "
    "Table 1 is the one careful grid (two columns, header plus twenty body rows, caption printing "
    "ABOVE) and is named by no sentence; CITATION IS FIVE FIGURE ROWS - Figures 3, 4, 5, 6 and 7 are "
    "the only exhibits a sentence names, and Figure 3 is named on p1 four pages before it prints; "
    "families line 8, flowchart-or-schematic 3, scatter 2, photo-or-raster-image 1, table-grid 6) |"
)

READ = (
    "| 98 | P-B-2016-52221-f8094e57 | 23 | 21 | 14 | 6 | closed, `check.py` layout identical, "
    "unaccounted 0; 21 measured regions over 14 of 23 pages resolving into 14 figure rows, 6 tables "
    "and 1 exclusion (the p3 container boxing Figures 1 and 2); the business-model schematic is "
    "printed three times, twice under the identical caption 'Model Schematic Diagram' and once "
    "uncaptioned in the executive summary, with six unexplained red ticks and queries added to the "
    "second copy; Figure 4, the exhibit cited for the debris data, is a screenshot of the DAS input "
    "dialog with no plot drawn and four widget labels truncated mid-word; nine axis labels say 'log' "
    "and every axis is graduated in evenly spaced numbers; Figures 9 to 11 each carry a plural "
    "'(Orbital Altitude Contours)' title over a single curve and the 400 and 2000 km parameter blocks "
    "are identical; Figure 12's 'data 7%' to 'data 10%' legend measures a quantity the paper never "
    "names and Figure 13's four duration curves superimpose; the six section-6.2.2 judge matrices "
    "carry no caption and no number and the p14 region holds two of them at once; only Figures 3 to 7 "
    "are ever named by a sentence |"
)

prefix = f"| 98 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 98 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
