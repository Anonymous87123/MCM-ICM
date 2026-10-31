# Full text corpus implementation checkpoint — 2026-10-29

## Current truth

The user's approved full-text database plan is being implemented. The foundation
is implemented and populated, but the full plan is NOT complete. Do not label this
corpus source-accepted or claim all abstracts have been read.

- Scope: 435 eligible papers, A84/B76/C112/D55/E60/F48, 11,552 physical pages.
- Current generation: `artifacts/text-corpus/reflow-20261029-v4/`.
- Dataset ID: `426a744a3c04a907d8bbf9aae27ccca5f81c1d0e953efa0f1b8f4e45f488379f`.
- 435 source PDFs re-extracted with hashes checked; all 11,552 pages accounted for.
- Structural integrity: pass, 0 errors. 940,238 source lines accounted for exactly
  once as retained blocks or explicitly documented exclusions (includes 181 OCR lines).
- 297,661 blocks and 15,599 section CANDIDATES. These are NOT verified paragraph
  or chapter counts. Heading false positives/false negatives still need repair.
- 431 nonempty abstract candidates, 4 unresolved empty candidates, 0 verified absent.
- Boundary verification applied: 1 section (q1 Summary). Full source acceptance: false.
- 2,619 protected legacy inputs checked unchanged. Legacy history/progress,
  language/model/evidence files and installed skill were not modified.
- `F:/MCM/AGENTS.md` was intentionally updated with the user's new priority.

## Implemented tools

All new code is in `scripts/`; tests in `tests/test_text_corpus.py`.

- `build_text_corpus.py`: freezes corpus scope/source bindings/preimages, extracts
  PyMuPDF text/spans/geometry and independent pdftotext bytes, create-only and resumable.
- `text_corpus.py`: section/paragraph candidates, typed furniture/captions/etc.,
  complete Markdown exports, source-line provenance and explicit defects.
- `resegment_text_corpus.py`: derives a new immutable generation from frozen pages,
  optional source-bound OCR evidence and explicit section reviews. Never overwrites.
- `recover_corpus_text_ocr.py`: local pinned RapidOCR ONNX models, memory-only
  page rendering, retained boxes/confidence/provenance. No remote OCR or image payload.
- `index_text_corpus.py`: immutable catalog + SQLite/FTS index and code snapshots.
- `corpus_reader.py`: exhaustive ordered selection, all matches + descendants without
  duplication, bounded exact-text chunks, resume, final completion marker, append-only
  observations/receipts, separate delivery/processing/source-verification counts.
- `validate_text_corpus.py`: hashes, all pages/source lines, section ownership,
  original text accounting, exports, SQLite, optional PDFs/legacy preimages. A structural
  pass never means source-fidelity acceptance.
- `package_text_corpus_skill.py`: new self-contained package with relative data
  attachment and full-reading route. Strict final release requires source acceptance
  and all-paper abstract reading acceptance; preview cannot bypass those requirements.

Reader defaults: max 6,000 tokens / 32 KiB. With no tokenizer installed it uses the
conservative UTF-8 byte upper bound, including output envelope and newline. It
therefore underuses, rather than exceeds, the token budget. Lower budgets supported.
No top-k, sentence snippets, quality filtering, automatic acknowledgements or card fallback.

## Current reading run

`artifacts/text-corpus/reading-runs/abstract-preview-20261029-v4/`

- Run ID: `18892ac9c3754c488a5b65438468c50c`.
- 2 acknowledged batches, 3/435 papers' candidate abstract texts actually read.
- 1 source-verified-and-processed; 434 unresolved in whole target scope.
- Cursor: paper_index=3, char_offset=0; no pending batch.
- Next is queue4, not q276. This is a text-database reading cursor, not legacy learning order/closure.
- q1 was visually checked against page1 and text/geometry on page2; five paragraphs.
  Root source review under `reviews/20261029/q001-abstract-v1.json` applied to v4.
- q2 was fully read and visually checked: six paragraphs; private-use glyphs and
  quotation transcription remain unresolved. NOT source-accepted.
- q3 was fully read and visually checked: true abstract is one paragraph/five sentences.
  Date above ABSTRACT was incorrectly included via inferred opening section. Repair
  as front matter in a new generation; do NOT silently treat this preview as clean.
- Observations under `reading-observations/`; q2/q3 defects under
  `reviews/20261029/q002-q003-text-defects-v1.json`.
- Do not auto-generate real-paper observations or claim a program traversal was AI reading.

Commands (from work root):

```text
python -B -X utf8 scripts/corpus_reader.py --corpus-root artifacts/text-corpus/reflow-20261029-v4 status --run-dir artifacts/text-corpus/reading-runs/abstract-preview-20261029-v4
python -B -X utf8 scripts/corpus_reader.py --corpus-root artifacts/text-corpus/reflow-20261029-v4 next --run-dir artifacts/text-corpus/reading-runs/abstract-preview-20261029-v4
```

Read ALL returned text, write substantive per-paper observations via apply_patch,
then acknowledge with the actual final marker. A new dataset invalidates this cursor;
never silently transplant it. Prior v3 reading run (q1 only) is retained.

## Recovery and remaining gaps

Four OCR opening-page candidates are integrated in v4, not source-verified:

- q80 P-A-2025-2500836-4285ad91: 49 OCR lines, all scores >=.95.
- q134 P-B-2020-2013836-4c773f05: 42 OCR lines, all scores >=.95.
- q267 P-C-2025-2516178-573cdff6: 46 OCR lines, all scores >=.95.
- q434 P-F-2025-2517199-1033f2d4: 44 OCR lines, 1 below .95.

OCR confidence is NOT proof of correctness. Original native page records are
preserved in `raw/parent-pages.jsonl`; OCR evidence is source/model-hash bound.
Additional OCR prototype for E2025 2508861 page2 is retained separately and not integrated.
Summary-Sheet competition banners no longer become model chapters; bold bullet
lead-ins no longer split the abstract into model/results sections.

Four still-empty abstract candidates, NOT verified absences:

- q11 P-A-2012-14990-e2428f0d (first page title, next contents).
- q162 P-C-2010-7812-c2fa13fd (starts with Problem and Introduction).
- q165 P-C-2011-10607-6ed4fd93 (first page contents).
- q169 P-C-2011-8882-54492a1f (first page contents).

Need inspect complete source/alternative extraction locations before declaring any
section genuinely absent. Do not substitute introduction for missing abstract.

v4 unresolved review flags (not all proven errors): section boundaries15,598;
hyphen joins9,116; private-use glyphs5,651; cross-page joins5,512; cross-engine
differences2,414; margin microtext251; native empty pages219; contents pages91;
column order85; malformed Unicode16; integrated OCR page reviews4.
Private-use/symbol flags include mathematics; do not resume formula correctness
checks. Type/retain non-prose regions separately without dropping surrounding prose.

## Packages, verification and safety

Current preview package:
`artifacts/skill-packages/text-corpus-preview-20261029-v2/mcm-icm-master-skill/`.
18,271 files plus package manifest, self-contained data attachment. Skill metadata
validation passes and its standalone reader reports 431 nonempty abstract candidates.
49 installed-skill source files independently checked unchanged after packaging.
It is NOT installed and NOT a final accepted release. Prior preview v1 preserved.

- Latest `pytest tests -q`: 212 passed.
- Latest `unittest discover -s tests -q`: 210 passed.
- Plan protocol validator: pass, 0 errors.
- Full unscoped pytest earlier: 253 passed/3 failed in old tmp q221 snapshot tests.
  Those historical tests expect obsolete live preimages/discovered status; unchanged.
- v4 all-PDF/legacy integrity report: pass/0 errors; source completeness false.
- No new subagents, no deletions, no legacy history append/full-paper completion.
- Only 3 compressed page proxies sent this segment, total803,717 bytes, one per
  call. No original PNG or whole session JSONL was sent. Continue the request guard.

Next: fix pre-ABSTRACT date/front-matter classification and q2 literal glyphs using
source-bound text repairs; inspect the four missing candidates; verify all abstract
boundaries/paragraph chains and continue actual ordered reading. Then repair
Introduction/all body sections and remaining text holes. Do not reduce the final
objective to 431 abstract candidates, a packaged preview, or a structural pass.
