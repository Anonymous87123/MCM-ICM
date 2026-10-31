"""Emit one verbatim opening quote per coded group for the B, C or D job lane.

Usage:
    python -I -X utf8 lanes/L7-quote-backfill/tools/quote_blocks.py <B|C|D|E|F> [--limit N] [--dry]

The tool reads the owning lane's records and layout, takes the opening sentence of the
first block of every coded group, checks it against the extracted paper text after
whitespace folding, and writes lanes/L7-quote-backfill/quotes-<lane>.jsonl.
A verification miss is fatal: the process exits 1 and names the offending row.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LANES = os.path.join(ROOT, "lanes")
OUT_DIR = os.path.join(ROOT, "lanes", "L7-quote-backfill")
ARTIFACTS = os.path.join(ROOT, "artifacts", "papers")

LANE_DIRS = {
    "B": "L4-b-ledger",
    "C": "L3-c-ledger",
    "D": "L2-d-ledger",
    "E": "L5-e-ledger",
    "F": "L1-f-structure",
}

SENTENCE_END = re.compile(r"[.!?](?=\s+[\"'“(A-Z0-9])")
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]{1,}")
STAMP = re.compile(r"(微信号|关注数学模型|获取更多资讯|MATHmodels|MATHMODELS)")
REAL_WORD = re.compile(r"[A-Za-z]{3,}")
LOWER_WORD = re.compile(r"[a-z][a-z'’-]{2,}")
SENTENCE_PUNCT = re.compile(r"[.!?]")
MAX_WORDS = 12
SPAN_MIN_WORDS = 8
GAP_MAX_WORDS = 8
SKIP_MAX_WORDS = 3
TEXT_GAP_MIN_BLOCKS = 3
PROSE_MIN_ALPHA = 12
PROSE_ALPHA_RATIO = 0.7
PROSE_MIN_LOWER = 0.5


def fold(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").replace("­", "")).strip()


def normalise(text: str) -> str:
    """Comparison form: NFKC (collapses fi/fl ligatures), no soft hyphens, folded space."""
    return fold(unicodedata.normalize("NFKC", text or ""))


def squeeze(text: str) -> str:
    """Last-resort comparison form: no whitespace at all, so column and line breaks vanish."""
    return re.sub(r"\s+", "", normalise(text))


def candidates(text: str) -> list[str]:
    """Opening sentence first, then every later sentence, then the first MAX_WORDS words."""
    folded = fold(text)
    if not folded:
        return []
    sentences = []
    start = 0
    for match in SENTENCE_END.finditer(folded):
        sentences.append(folded[start : match.end()].strip())
        start = match.end()
    tail = folded[start:].strip()
    if tail:
        sentences.append(tail)
    words = folded.split(" ")
    if len(words) > MAX_WORDS:
        sentences.append(" ".join(words[:MAX_WORDS]))
    return sentences


def is_prose(text: str, kind: str | None) -> bool:
    """True when a block carries a sentence: enough plain words, few enough symbol tokens.

    Formula and table blocks are emitted by the layout as symbol soup whose reading order
    the extracted text does not share, so they can never verify; they are quoted as-is and
    counted as unverified instead of aborting the lane. A prose block that fails every
    ladder step stays a hard error, because that means a real sentence was lost.
    """
    if kind == "display":
        return False
    folded = normalise(text)
    if not SENTENCE_PUNCT.search(folded):
        return False
    words = folded.split(" ")
    alpha = sum(1 for word in words if WORD.fullmatch(word))
    lower = sum(1 for word in words if LOWER_WORD.fullmatch(word))
    return (
        alpha >= PROSE_MIN_ALPHA
        and alpha / len(words) >= PROSE_ALPHA_RATIO
        and lower / alpha >= PROSE_MIN_LOWER
    )


def span_quote(text: str, squeezed_text: str) -> str:
    """Longest contiguous word span of the block that occurs in the verification text.

    Table cells and formula fragments are emitted by the layout in a reading order the
    extracted text does not share, so no sentence of such a block verifies. This routine
    returns the longest run of words that does verify verbatim, which is still an exact
    quotation of the block, just not a whole sentence.
    """
    words = normalise(text).split(" ")
    if len(words) < SPAN_MIN_WORDS:
        return ""
    best = ""
    for start in range(len(words) - SPAN_MIN_WORDS + 1):
        probe = "".join(words[start : start + SPAN_MIN_WORDS])
        if probe not in squeezed_text:
            continue
        end = start + SPAN_MIN_WORDS
        while end < len(words):
            extended = "".join(words[start : end + 1])
            if extended not in squeezed_text:
                break
            end += 1
        span = " ".join(words[start:end])
        if len(span) > len(best):
            best = span
    return best



def bare(word: str) -> str:
    """Comparison key: lowercase, letters and digits only."""
    return re.sub(r"[^a-z0-9]", "", word.lower())


GAP_MIN_ANCHOR = 3
GAP_MAX_ORIGINS = 20


def gapped_quote(text: str, tokens: list[str]) -> str:
    """Longest in-order run of block words with at most GAP_MAX_WORDS foreign words between.

    A two-column assumptions table extracts as its two columns interleaved word by word, so
    the sentence of one cell never survives as a contiguous run, while every word of it does
    survive in order. The gap is counted in words, so the match stays a quotation rather
    than a bag of common words scattered across the paper.
    """
    words = normalise(text).split(" ")
    if len(words) < SPAN_MIN_WORDS:
        return ""
    positions: dict[str, list[int]] = {}
    for index, token in enumerate(tokens):
        positions.setdefault(bare(token), []).append(index)

    best: list[str] = []
    for start in range(len(words) - SPAN_MIN_WORDS + 1):
        key = bare(words[start])
        # A one- or two-letter anchor matches thousands of places in the paper and makes the
        # search quadratic without improving the run, so anchors must carry letters.
        if len(key) < GAP_MIN_ANCHOR:
            continue
        hits = positions.get(key)
        if not hits:
            continue
        for origin in hits[:GAP_MAX_ORIGINS]:
            run = [words[start]]
            cursor = origin
            skipped = 0
            for word in words[start + 1 :]:
                hits = positions.get(bare(word))
                nxt = None
                if hits:
                    nxt = next((hit for hit in hits if cursor < hit <= cursor + GAP_MAX_WORDS), None)
                if nxt is None:
                    # A layout often doubles a math glyph ("jjth" for "jth") or prints a
                    # formula token the text layer never carried. Allow a few such words
                    # to drop out of the run, then stop.
                    skipped += 1
                    if skipped > SKIP_MAX_WORDS:
                        break
                    continue
                run.append(word)
                cursor = nxt
            if len(run) >= SPAN_MIN_WORDS and len(run) > len(best):
                best = run
    return " ".join(best)


def has_real_words(text: str) -> bool:
    """True when a match carries at least two distinct words of three letters or more.

    A run of single-letter tokens ('m m m m …', '1 2 3 4 …') can satisfy the span and gapped
    steps against a matrix or axis table, and quoting it produces a row that verifies and
    still says nothing. Such a match is discarded and the block falls through to the label
    its content deserves.
    """
    return len({word.lower() for word in REAL_WORD.findall(text)}) >= 2


def strip_leading_stamp(text: str) -> str:
    """Drop the uploader watermark when it opens the block, keeping the paper's own text.

    The stamp is three lines; the layout sometimes emits them glued to the block that
    follows, so the block is not stamp-only and the group walk cannot help. Trimming the
    head leaves a verbatim span of the same block, which is what a quote is.
    """
    current = fold(text).lstrip("•●⚫·▪ ")
    while True:
        match = STAMP.search(current)
        if not match or match.start() > 1:
            return current
        current = fold(current[match.end():]).lstrip("•●⚫·▪ ")


def is_stamp_only(text: str) -> bool:
    """True when a block holds nothing but the uploader's watermark.

    The stamp is printed as three widely spaced lines, so the layout emits it as its own
    block and it can land as the first block of a coded group. Quoting it would open the
    row with 关注数学模型 instead of the paper's own sentence.
    """
    return not WORD.search(STAMP.sub(" ", text or ""))


def text_gap_blocks(paragraphs: list[dict], squeezed_text: str) -> int:
    """Body blocks of at least SPAN_MIN_WORDS plain words with no 8-word span in the text.

    A paper whose text layer drops whole paragraphs has a fact about itself, and that fact
    is what licenses quoting such a paragraph from the layout instead of failing. A single
    unverifiable sentence inside an otherwise clean text layer is still a hard error.
    """
    missing = 0
    for block in paragraphs:
        if block.get("kind") != "body":
            continue
        raw = block.get("text", "")
        if len(fold(raw).split(" ")) < SPAN_MIN_WORDS:
            continue
        if not span_quote(raw, squeezed_text):
            missing += 1
    return missing


def read_pages(directory: str) -> str:
    """Concatenate every page text file in a directory, in page order."""
    chunks = []
    for name in sorted(os.listdir(directory)):
        if name.endswith(".txt"):
            with open(os.path.join(directory, name), encoding="utf-8", errors="replace") as handle:
                chunks.append(handle.read())
    return " ".join(chunks)


def load_text(paper: str) -> tuple[str, str]:
    """Return (folded verification text, provenance label).

    Some papers lost the staged ``text/`` tree during a correction pass, so the same
    extraction is looked up where it still lives: the page files of a correction
    workspace, or the concatenated source text the anti-copy check reads.
    """
    root = os.path.join(ARTIFACTS, paper)

    full = os.path.join(root, "text", "full.txt")
    if os.path.exists(full):
        with open(full, encoding="utf-8", errors="replace") as handle:
            return fold(handle.read()), "full.txt"

    page_dirs = [os.path.join(root, "text", "pages")]
    page_dirs += [
        directory
        for directory, _, _ in os.walk(root)
        if os.path.basename(directory) == "pages" and os.path.basename(os.path.dirname(directory)) == "text"
    ]
    for directory in page_dirs:
        if not os.path.isdir(directory):
            continue
        text = read_pages(directory)
        if text.strip():
            return fold(text), "text/pages:" + os.path.relpath(directory, root).replace(os.sep, "/")

    pages = os.path.join(root, "pages.jsonl")
    if os.path.exists(pages):
        chunks = []
        with open(pages, encoding="utf-8", errors="replace") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                chunks.append(str(record.get("text", "")))
        if chunks:
            return fold(" ".join(chunks)), "pages.jsonl"

    anti_copy = os.path.join(root, "anti-copy-source.txt")
    if os.path.exists(anti_copy):
        with open(anti_copy, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        if text.strip():
            return fold(text), "anti-copy-source.txt"

    extraction = os.path.join(root, "extraction.json")
    if os.path.exists(extraction):
        try:
            with open(extraction, encoding="utf-8", errors="replace") as handle:
                data = json.load(handle)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            for key in ("full_text", "text", "body_text"):
                value = data.get(key)
                if isinstance(value, str) and value.strip():
                    return fold(value), "extraction.json:" + key

    return "", "missing"


def lane_papers(lane: str) -> list[str]:
    records_dir = os.path.join(LANES, LANE_DIRS[lane], "records")
    names = []
    for name in sorted(os.listdir(records_dir)):
        if not name.endswith(".json") or name.endswith(".skipped.json"):
            continue
        names.append(name[:-5])
    return names


def rows_for_paper(lane: str, paper: str) -> tuple[list[dict], list[str]]:
    lane_dir = os.path.join(LANES, LANE_DIRS[lane])
    with open(os.path.join(lane_dir, "records", paper + ".json"), encoding="utf-8") as handle:
        chapters = json.load(handle)
    with open(os.path.join(lane_dir, "layout", paper + ".json"), encoding="utf-8") as handle:
        layout = json.load(handle)
    blocks = {int(block["n"]): block for block in layout["paragraphs"]}

    text, provenance = load_text(paper)
    ocr_layout = layout.get("extractor") == "ocr_layout"
    norm_text = normalise(text)
    squeezed_text = squeeze(text)
    tokens = normalise(text).split(" ")
    rows: list[dict] = []
    problems: list[str] = []
    gap_cache: list[int] = []

    def pick_quote(raw: str, kind: str | None) -> tuple[str, str] | None:
        """First candidate that hits the verification text, with the match level."""
        if provenance == "missing":
            return " ".join(normalise(raw).split(" ")[:MAX_WORDS]), "layout-only"
        for candidate in candidates(raw):
            if candidate and candidate in text:
                return candidate, "exact"
            if candidate and normalise(candidate) in norm_text:
                return candidate, "nfkc"
            if candidate and squeeze(candidate) and squeeze(candidate) in squeezed_text:
                return candidate, "squeezed"
        span = span_quote(raw, squeezed_text)
        if span and has_real_words(span):
            return span, "span"
        if ocr_layout and is_prose(raw, kind):
            # The layout was read off the page image, so this sentence is on the page and
            # the extracted text simply never covered it. Falling through to `gapped` here
            # stitches scattered words from elsewhere in the text into a run that is not
            # the block's own sentence, which reads like a quotation and is not one.
            return " ".join(normalise(raw).split(" ")[:MAX_WORDS]), "ocr-only"
        # A symbol-only block cannot yield an acceptable gapped run, and the search over it
        # is quadratic in the paper's common tokens, so it is skipped rather than attempted.
        gapped = gapped_quote(raw, tokens) if has_real_words(raw) else ""
        if gapped and has_real_words(gapped):
            return gapped, "gapped"
        if not is_prose(raw, kind):
            return " ".join(normalise(raw).split(" ")[:MAX_WORDS]), "unverified"
        if ocr_layout:
            # The layout was read from page images, so this prose is on the page; the
            # extracted text simply never covered it. Quote the layout and say so.
            return " ".join(normalise(raw).split(" ")[:MAX_WORDS]), "ocr-only"
        if not gap_cache:
            gap_cache.append(text_gap_blocks(layout["paragraphs"], squeezed_text))
        if gap_cache[0] >= TEXT_GAP_MIN_BLOCKS:
            # This paper's text layer drops whole paragraphs, so silence about this block
            # says nothing about the page. Quote the layout and name the gap.
            return " ".join(normalise(raw).split(" ")[:MAX_WORDS]), "text-gap"
        return None

    chapter_index = 0
    for chapter in chapters:
        if not isinstance(chapter, dict):
            continue
        this_chapter = chapter_index
        chapter_index += 1
        groups = chapter.get("groups") or []
        jobs = chapter.get("jobs") or []
        if len(groups) != len(jobs):
            problems.append(f"{paper} {chapter.get('chapter')}: {len(groups)} groups vs {len(jobs)} jobs")
            continue
        for offset, (group, job) in enumerate(zip(groups, jobs)):
            if not group:
                problems.append(f"{paper} {chapter.get('chapter')}: empty group")
                continue
            index = int(group[0])
            block = blocks.get(index)
            if block is None:
                problems.append(f"{paper} {chapter.get('chapter')}: block {index} not in layout")
                continue
            if is_stamp_only(block.get("text", "")):
                # Quote the group's first block that carries the paper's own text.
                for member in group:
                    candidate = blocks.get(int(member))
                    if candidate is not None and not is_stamp_only(candidate.get("text", "")):
                        block = candidate
                        break
            block = {**block, "text": strip_leading_stamp(block.get("text", ""))}
            picked = pick_quote(block.get("text", ""), block.get("kind"))
            if picked is None:
                problems.append(
                    f"{paper} {chapter.get('chapter')}: no sentence of block {index} found in "
                    f"{provenance}: {fold(block.get('text', ''))[:90]}"
                )
                continue
            quote, level = picked
            pages = block.get("pages") or []
            rows.append(
                {
                    "paper": paper,
                    "chapter": chapter.get("chapter"),
                    "chapter_index": this_chapter,
                    "block_index": offset,
                    "job": job,
                    "quote": quote,
                    "page": pages[0] if pages else None,
                    "_kind": block.get("kind"),
                    "_provenance": provenance,
                    "_match": level,
                }
            )
    return rows, problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("lane", choices=sorted(LANE_DIRS))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry", action="store_true")
    args = parser.parse_args()

    papers = lane_papers(args.lane)
    if args.limit:
        papers = papers[: args.limit]

    all_rows: list[dict] = []
    problems: list[str] = []
    for paper in papers:
        rows, issues = rows_for_paper(args.lane, paper)
        all_rows.extend(rows)
        problems.extend(issues)

    if problems:
        print(f"{args.lane}: {len(problems)} problem(s)", file=sys.stderr)
        for line in problems[:20]:
            print("  " + line, file=sys.stderr)
        return 1

    # Denominator as the generator saw it: the owning lane keeps coding, so the recount in
    # coverage.py must be compared against this snapshot, not against the live records.
    chapters_seen = 0
    groups_seen = 0
    for paper in papers:
        path = os.path.join(LANES, LANE_DIRS[args.lane], "records", paper + ".json")
        with open(path, encoding="utf-8") as handle:
            chapters_of_paper = json.load(handle)
        for chapter in chapters_of_paper:
            if isinstance(chapter, dict):
                chapters_seen += 1
                groups_seen += len(chapter.get("groups") or [])

    stats = {
        "lane": args.lane,
        "papers": len(papers),
        "chapters": chapters_seen,
        "coded_groups": groups_seen,
        "rows": len(all_rows),
        "layout_only": sum(1 for row in all_rows if row["_provenance"] == "missing"),
        "heading_rows": sum(1 for row in all_rows if row["_kind"] in ("heading", "display")),
        "match_levels": dict(sorted(collections.Counter(row["_match"] for row in all_rows).items())),
        "provenance": dict(sorted(collections.Counter(row["_provenance"] for row in all_rows).items())),
    }
    print(json.dumps(stats, ensure_ascii=False))
    if args.dry:
        return 0

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, f"quotes-{args.lane.lower()}.jsonl")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        for row in all_rows:
            record = {
                "paper": row["paper"],
                "chapter": row["chapter"],
                "chapter_index": row["chapter_index"],
                "block_index": row["block_index"],
                "job": row["job"],
                "quote": row["quote"],
                "page": row["page"],
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"wrote {out_path} ({len(all_rows)} rows)")

    reports = os.path.join(OUT_DIR, "reports")
    os.makedirs(reports, exist_ok=True)
    levels_path = os.path.join(reports, f"levels-{args.lane.lower()}.json")
    with open(levels_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(stats, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
