"""Check each candidate mention quote against the text layer of its page."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

import schema

PID = "P-B-2015-38720-26d38781"

CANDIDATES = [
    (7, "From the information from MH370 (Figure 1), we determined the search area to be "
        "basically rectangular in shape"),
    (7, "These flights vary in type from transatlantic to shorter hops between (Figure 2)"),
    (15, "we are also going to include the corners bordering the circles in our search area "
         "(Figure 3)"),
    (17, "taking this into account makes the distribution significantly more complex "
         "(Figure 4)"),
    (17, "we will imagine that just as many planes end up between Points A and A’ and between "
         "B’ and B as along the rest of the flight path (Figure 5)"),
    (27, "Figure 11 shows a typical solution as it moves according to the bounded random "
         "flight path."),
    (44, "A three-dimensional (Figure 25) and two-dimensional graph (Figure 26) of the initial "
         "distribution are displayed below"),
    (44, "it can be either the strip centered at y=20 mi or the strip centered at y=-20 mi, "
         "because they are equivalent (Figure 27)"),
    (45, "Now, the location of the third pass can be determined by finding the highest "
         "remaining probability distribution, here centered around y=-20 miles (Figure 28)"),
]

for page, text in CANDIDATES:
    ok = schema.norm(text) in schema.page_text(PID, page)
    print(f"p{page} words={len(schema.words(text)):2} ok={ok} {text[:70]}")
