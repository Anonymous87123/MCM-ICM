"""Citation lines and heading positions for P-C-2015-35778-39d71af2."""

import json
import re
import sys
from pathlib import Path

import pdfplumber

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-C-2015-35778-39d71af2"
head = (LANE / ".proxy" / f"{PID}-read.txt").read_text(encoding="utf-8").splitlines()
SRC = next(line.split(" ", 1)[1] for line in head if line.startswith("source "))

PAGES = [6, 7, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20]
PAT = re.compile(r"(fig(?:ure)?\.?\s*-?\s*\d+|tab(?:le)?\.?\s*\d+)", re.I)

with pdfplumber.open(SRC) as pdf:
    for n in PAGES:
        page = pdf.pages[n - 1]
        print(f"===== p{n}")
        for ln in page.extract_text_lines():
            t = ln["text"]
            if PAT.search(t):
                print(f"  y={ln['top']:7.1f} | {t}")
        print("  -- first lines of page:")
        for ln in page.extract_text_lines()[:3]:
            print(f"  y={ln['top']:7.1f} | {ln['text'][:100]}")
