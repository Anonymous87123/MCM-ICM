"""Check that every coded unit's opening sentence is verbatim in the paper text.

The D lane promises one verbatim original sentence per job. `record.py` builds
that sentence from measured blocks, so a block whose span order was scrambled by
the PDF text layer produces a sentence the paper never printed. This tool folds
whitespace in both the sentence and `artifacts/papers/<pid>/text/full.txt` and
reports every unit whose opening sentence is not a substring.

Usage: python -I lanes/L2-d-ledger/tools/verify_quotes.py <paper_id> [<paper_id> ...]
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
LANE = ROOT / "lanes" / "L2-d-ledger"


LIGATURES = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi",
    "ﬄ": "ffl", "ﬅ": "ft", "ﬆ": "st",
}

PAGE_FURNITURE = re.compile(r"Team\s*#?\s*\d+\s*Page\s*\d+\s*of\s*\d+")

FURNITURE_PATH = LANE / "furniture.json"
FURNITURE = (
    json.loads(FURNITURE_PATH.read_text(encoding="utf-8")) if FURNITURE_PATH.exists() else {}
)
HEADS = FURNITURE.get("heads", {})
DROP_CHARS = FURNITURE.get("drop_chars", {})


def fold(text: str, drop: str = "") -> str:
    """Drop ligature codepoints, running page headers and every whitespace run.

    Word order and punctuation must still match exactly; only spacing, line
    wrapping, fi/fl ligatures and the running header ("Team # 35780 Page 16 of
    22"), which the text layer drops into the middle of a paragraph when the
    paragraph crosses a page break, are forgiven.

    `drop` names codepoints that carry no prose for one paper and that the text
    layer emits in a different order on the page than in full.txt, so keeping
    them would fail a sentence the paper really printed. Dropping runs before the
    ligature mapping, because some papers lose a ligature outright in full.txt
    (P-D-2017-56632-67f41f43 keeps no ﬀ, ﬃ or ﬄ at all and leaves "di cult"
    where the page sets "difficult"), so the dropped codepoint has to go before
    the ﬀ→ff substitution can turn it into letters.
    """
    text = PAGE_FURNITURE.sub(" ", text)
    for char in drop:
        text = text.replace(char, "")
    for lig, plain in LIGATURES.items():
        text = text.replace(lig, plain)
    return re.sub(r"\s+", "", text)


def main(pids: list[str]) -> int:
    total = miss = 0
    for pid in pids:
        # Some papers store their italic math as CESU-8 surrogate pairs, which
        # strict utf-8 rejects; surrogatepass keeps them as lone surrogates so the
        # prose around them can still be compared.
        full = (ROOT / "artifacts" / "papers" / pid / "text" / "full.txt").read_bytes().decode(
            "utf-8", errors="surrogatepass")
        # CESU-8 writes a math-italic letter as two surrogate code points; joining
        # them back into one super-BMP character lets the quote compare equal to
        # the character PyMuPDF hands out.
        try:
            full = full.encode("utf-16-le", errors="surrogatepass").decode("utf-16-le", errors="surrogatepass")
        except UnicodeDecodeError:
            pass
        # A running head that the text layer dropped in without its page number
        # cannot be caught by PAGE_FURNITURE; the lane names those strings per
        # paper in furniture.json so the removal stays auditable.
        for head in HEADS.get(pid, []):
            full = full.replace(head, " ")
        drop = "".join(DROP_CHARS.get(pid, []))
        full = fold(full, drop)
        rows = [json.loads(l) for l in (LANE / "jobs-d.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
        rows = [r for r in rows if r["paper"] == pid]
        bad = []
        for r in rows:
            for u in r["units"]:
                total += 1
                text = fold(u.get("open") or "", drop)
                if not text or text.endswith("…"):
                    text = text.rstrip(" …")
                if text and text in full:
                    continue
                miss += 1
                bad.append((r["chapter"], u["blocks"], text))
        print("%s units %d miss %d" % (pid, sum(len(r["units"]) for r in rows), len(bad)))
        for chapter, blocks, text in bad:
            safe = text[:120].encode("ascii", "backslashreplace").decode("ascii")
            print("   MISS %-22s %-16s %s" % (chapter, blocks, safe))
    print("TOTAL %d units, %d misses" % (total, miss))
    return 0 if miss == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
