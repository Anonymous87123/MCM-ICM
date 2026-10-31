# Complete text corpus checkpoint — 2026-10-31, v9

Goal ACTIVE. Read v7 for accepted-v26 provenance and v8 for earlier receipts.
This checkpoint changes only source-layout findings and actual reading records.
All prior datasets, packages, failures, PDFs, installed skill and learning history
remain preserved. Formula correctness/figure distillation are paused. No agents.

## Accepted corpus and implementation

- V26 dataset `341bd403e4ca1fc92448a5c8b608cc94e49ff66c09146703d2e116ea45d07b7d`.
- 435papers/11,552pages/954,866lines accounted once;292,140blocks/18,509candidate
  sections;435continuous author Markdown/source maps checked.9boundary reviews;
  2,619protected preimages unchanged. Structural PASS/errors0 remains distinct
  from source acceptance: source completeness FALSE/zero whole-paper acceptance.
- Abstract candidates427, existing source-local absences6, empty unresolved2,
  source-verified selections5. No new accepted generation was built this segment.
- V26 transport, separatev13preview and unrelated-cwd smoke DONE/PASS. Latest full
  tests339pytest/337unittest PASS; no corpus/reader/core code changes since.

## New bounded source findings

- `reviews/20261031/q011-pages7-27-layout-findings-v1.json`: seven individually
  inspected JPEGs02–08 cover21physicalpages. Local Introduction/Conclusion
  headings belong to numbered models and must not become paper synopsis roles.
  Combined with earlier findings, visual layout checked pages1–30. Remaining
  pages31–42: overviews10–13. Full native census was read earlier; do not redo it.
- `reviews/20261031/q169-pages1-3-layout-findings-v1.json`: overview00checked.
  Contents precedes explicit Introduction, which continues onto page3before
  Assumptions/ABriefView. This roadmap is Introduction prose, not an abstract.
  Remaining physicalpages4–27: overviews01–08. Native census already read.
- Both proof files were parsed and checked against their source/raw manifest
  hashes and each inspected JPEG hash: PASS. Neither proves whole-source absence,
  all-paragraph fidelity or whole-paper source completeness. No corpus status or
  original manifest was silently changed.
- This context segment has used exactly8JPEGs/2,357,611bytes. NO more images
  until compaction. One image per call; originals stay on disk.

## Actual abstract reading — oldv16/frozenpreviewv8 ONLY

Run `reading-runs/abstract-preview-20261030-v16`, ID
`541d2520dc494e22a4ae952bd718d398`, dataset
`7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65`.

- 166acknowledgements000000–000165; cursorpaper_index170/char0, throughq170.
- 162nonempty candidates completely processed;6existing absent sections accounted
  for;2empty unresolved(q11/q169).4source-verified-and-processed. No pending batch.
  Nextq171NOTrequested. Do not sum old/new corpus runs or promote this processing
  to current-v26 source-complete reading.
- New observations000152–000165were written after actual text reading. Q166long
  ExecutiveSummary was read in two acknowledged segments, without marking the
  first segment complete. Q162/165/167/170existing absence entries deliver no text;
  they were not counted as read abstracts. Q169remains unresolved, not absent.
- New defects include mid-sentence splits, source-compound/word-wrap ambiguity,
  keyword/form/promotion leakage, repeated-m tails(q154/q159), flattened question
  lists, and page2title leakage. Preserve literal author grammar/claims and all
  original delivered bytes. No figures/formulas interpreted or new cards made.
- Snapshot `reviews/20261031/reading-source-issues-v16-through-q170-v1.json`:
  all166receipt bindings checked;333rawhistorical explicit issues/142papers;
  two earlier append-only observation corrections validated. This is NOT a live
  unresolved-defect total. Original receipts/batches were not rewritten.

Resume ONLY the packagedpreviewv8 `corpus_reader.py` with `reflow-20261030-v16`.
After compaction finish q11overviews10–13and q169overviews01–08, then continue
individual q93/q137/q110prose repairs. All-abstract processing is only the first
checkpoint; all author chapters, source repairs and actual-reading acceptance
remain outstanding. Preserve pauses and all old data.
