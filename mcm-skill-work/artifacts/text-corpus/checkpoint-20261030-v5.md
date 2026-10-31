# Complete text corpus checkpoint - 2026-10-30, v5

The goal remains active: the full435-paper/11,552-page text database, exhaustive
section reader, and actual reading of ALL corresponding author chapters. The
all-abstract milestone is not final. Do not return to fragment-card production,
formula correctness or figure interpretation. OCR/page proxies are prose/layout
recovery only. No cleanup, legacy learning transaction, whole-paper closure,
installed-skill replacement or new subagent is authorized by this checkpoint.
Preserve every earlier checkpoint, generation, run, evidence file and failed draft.

## Current non-regressing immutable candidate: v14

- `reflow-20261030-v14/`, dataset
  `76e3a302c8675ac4eb4a1bf80706bba3d26e1fbf1e388fcb99135dc48ffbab03`.
- `build-request-reflow-20261030-v14.json`; create-only driver
  `scripts/build_text_corpus_v14.py` completed with exit0. No build remains running.
- `integrity-reflow-20261030-v14.json`: structural PASS, errors0; all435 PDFs,
  11,552 physical pages and954,866 raw lines accounted exactly once;292,489 blocks,
  18,521 section candidates,5 source-boundary-reviewed sections. All2,619 protected
  legacy preimages unchanged, including a fresh post-test hash check.
- Structured originals, full/section Markdown and SQLite are present for all435.
  This is extraction/accounting completeness, NOT prose/source-fidelity acceptance.
  `source_completeness_accepted:false`; zero whole-paper source acceptances.
- Abstracts:427 nonempty candidates,4 source-local absences(q5/q94/q162/q167),
  4 empty unresolved(q11/q165/q169/q170). q165's completed absence proof is now
  staged separately, not applied to v14. Do not count an absence as an abstract read.
- Five boundary reviews remain q1-q4 andq10; strict query status can still be more
  restrictive because source-page defects remain open.
- Parent for the successful batch was v12, dataset
  `0ba20e8d9d763e219e159779d38f7e97cb1375e3da7f01681aa6c0258ce7f06b`.
  Rebuild from `native-20261029-v1` plus the same53 frozen OCR manifests. Never
  reapply OCR to already augmented raw pages: duplicate OCR line IDs would result.
- Source-origin sidecar `span-metrics-20261030-v1/manifest.json` covers435/11,552,
  940,057 native lines and3,253,631 spans. Source-origin baselines are machine
  grouping evidence, not blanket source approval.

## Preserved failed v13 and the correction

- v13 dataset `4202b5277a50958f1acc017c8265a88ff9a40cb10bc0a081a84b53ca8805a71e`
  passed raw ownership but regressed split-line dotted contents: a trailing page
  number had accidentally become mandatory on the leader line. Contents flags
  fell345->143 and phantom body sections increased. It is NOT promoted or packaged.
- `reflow-20261030-v13-promotion-rejected.md` preserves the cause and evidence.
  Do not delete/rewrite v13 or quote its section increase as progress.
- v14 corrected the leader rule, preserves all previous Contents pages per paper,
  and also recognizes dash/middle-dot leaders. The per-page preservation guard
  rejects losses even if a different page would make aggregate counts increase.
- `span-origin-flow-full-20261030-v6.json`: prospective435/11,552/954,866, errors0,
  review-replay conflicts0, all345 old Contents pages retained;352 candidate pages
  afterward. Frozen implementation/review inputs were checked before/after build.
- Applied prose proofs retain q1 pages6/7/17 and add pages25/31:61 explicit groups
  total in `q001-merged-text-lanes-v2.json`. Three Figure-number author paragraphs
  restored; printed wording/duplicate chapter numbering preserved. q1p5's three
  literal operations/four BBS abbreviations rebound without new source approval.
- Singular Reference classification excludes bibliography but not Reference Frame
  or Reference Coordinate System. Plural Nomenclatures and addressed Letter titles
  have candidate normalized roles. These do not waive source-boundary reviews.

## Whole-scope quality inventories for v14

All reports below inspect435 papers/11,552 pages, preserve source bytes and are
diagnostics rather than accepted defect counts. Findings/flags overlap.

- `section-candidate-audit-20261030-v14.json`:4 verified absences,4 empty unresolved,
  58 multipage abstract scope checks,2 fragmentation candidates,33 possible form
  contamination and1 envelope warning. q40 envelope warning was previously
  source-checked as a false positive; do not repeatedly redo that same review.
- `contents-section-leakage-20261030-v14.json`:43 papers/44 candidate leaking pages
  (prior v11:47/48). Many remaining cases are OCR-split titles/page numbers; do not
  blanket-exclude pages merely because they have an early Contents label.
- `caption-prose-boundaries-20261030-v14.json`:123 papers/209 candidate caption
  blocks (prior212). Actual captions can contain the same verbs; source checks are
  required, not a broad Figure-regex override.
- `non-author-section-leakage-20261030-v14.json`:one remaining explicit heading,
  q164's `X References` (prior16). See the coupled appendix issue below.
- New `unicode-text-frontier-20261030-v14.json`:3 papers(q148/q237/q387),19 blocks,
  11 paper-page locations,161 malformed codepoints. Raw line IDs, source boxes and
  local contexts are recorded. Some errors occur inside author explanations; do
  not dismiss them as formula-only or delete their surrounding prose.
- Open flags: section boundaries18,516; hyphen joins9,746; private glyphs5,484;
  cross-page joins5,118; cross-engine1,850; contents352; inline flow469; margins251;
  OCR223; column order90; spacing57; Summary subheading5; opening Letter1;
  unresolved Unicode19. They are not distinct proven errors or evidence counts.

## Source reviews completed/staged since the previous checkpoint

- q94 `P-B-2012-13074-8fc549d2`: all22 native pages actually read and all8 bounded
  JPEG overviews inspected. Direct Introduction, body, sensitivity/evaluation,
  separate Conclusions and final Letter, no independent abstract. Local604-record
  inventory contains only the same22-page source. The full native census and
  `q094-abstract-absence-v1.json` are applied in v14, source-local only.
- q165 `P-C-2011-10607-6ed4fd93`: all20 native pages and7 overviews actually
  inspected. Contents -> Introduction -> body/recommendations/decision ->
  References; no independent abstract. `q165-full-native-prose-census-v1.json`
  retains its earlier then-unread image limitation; supplemental
  `q165-whole-source-layout-findings-v1.json` records the later complete check.
  `q165-abstract-absence-v1.json` staged with50 portable evidence files, not applied.
  Inventory checked all604 rows: `2106074.pdf` is an unrelated substring match,
  not a second source for team10607; exact token/hash checks retained.
- q165 pages9/10: `q165-pages9-10-prose-boundaries-v1.json` staged27 explicit
  groups, all active page lines exactly once;49 portable files preflighted.
  Figure2/3/4 author paragraphs and the complete Table5 reference sentence are
  retained; source-table cells/captions/attribution separate. No table values,
  chart meanings or formulas interpreted. Page8/11 mixed-source problems remain.
- q11 `P-A-2012-14990-e2428f0d`: all42 native pages actually read;
  `q011-full-native-prose-census-v1.json` saved. Prior opening pages1-3 layout
  findings retained. Full42-page evidence prepared as14 overviews but NOT fully
  inspected. Native-near-empty page29 particularly requires source checking.
  No absence approval. Memo/appendix/code are not silently relabelled as abstract.
- q169 `P-C-2011-8882-54492a1f`: all27 native pages actually read;
  `q169-full-native-prose-census-v1.json` saved. Nine full-source overviews are
  prepared but UNREAD. No source-local absence approval.
- q170 `P-C-2011-9089-838e50df`: all20 native pages actually read;
  `q170-full-native-prose-census-v1.json` saved. Seven overviews prepared;
  only overview00 (physical pages1-3) actually inspected. Title is followed by
  explicit1 Introduction, not an unheaded abstract. Six remaining overviews01-06
  are UNREAD. `q170-opening-layout-findings-v1.json` records exactly this limit.
- These native/layout censuses are source-recovery work, not exhaustive-reader
  receipts, new language cards, whole-paper source acceptance or learning closure.

## Actual reading receipts - preserve versions separately

Immutable v11 run `reading-runs/all-author-preview-20261030-v11/`, run ID
`553a50bf60444af4b857adcd50a75a67`:23 actual manually observed/acknowledged batches
000000-000022; cursor paper_index1/char_offset0, no pending batch. q1's complete
63,291-character candidate reached its end, including appendix code (not executed
or treated as natural prose). Source corruption/object leakage discoveries retained.

- `all-chapter-coverage-v11-q001-candidate-end-20261030.json`:one complete candidate
  paper,389 unique blocks/41 candidate sections processed out of98,621/17,584.
  Zero source-verified complete author-text papers; all-chapter acceptance=false.
- New observations000020-000022 are actual manual records, not auto-acknowledgment.
- Archived v10 abstract run:25 nonempty candidates read throughq27,4 verified
  processed for that version only. Earlier v10 all-author work also preserved.
- There is no v14 actual-reading run yet. NEVER reuse a v10/v11 cursor in v14 or
  sum repeated paper counts across versions. Delivery != agent processing !=
  source fidelity != understanding. Do not claim all435 abstracts/chapters read.

## New working-code candidates AFTER the v14 freeze - not applied to v14

- Shared HEADING_NUMBER normalization fixes bare `X References`; a bounded
  plain-font colon-appendix rule prevents a real appendix title staying inside
  bibliography. Two red regression tests first failed, then passed after changes.
  New Unicode inventory adds two tests. Formal latest runs:291 pytest PASS13.18s,
  289 unittest PASS12.452s; plan protocol PASS0. Expected negative-fixture stdout
  saying fail is not a suite failure. Earlier global tmp fixture failures remain
  preserved; do not edit old tmp expectations or run broad pytest as a repair.
- Important ACTUAL-PAPER blocker before any successor build: q164 native page11
  has its appendix heading late in geometric order, after extracted table labels.
  A bibliography-only correction could leave appendix material under References.
  Synthetic tests/raw-line accounting cannot approve this source order.
- `q164-reference-appendix-boundary-frontier-v1.json` records this coupled issue.
  Full11-page evidence is prepared in `source-reviews/q164-whole-source-20261030-v1/`
  but UNREAD. First inspect overview03 (physical pages10/11), prose/boundaries only;
  if necessary create focused/rotated bounded proxies and an explicit layout proof.
- All435-paper native-line comparison found only two additional plain-font appendix
  heading candidates: q352 pages25/27. They are not source-approved.
- Do not promote/build v15 solely because these tests pass. First source-check and
  bind q164's appendix boundary, accumulate remaining absence/prose fixes, then run
  a fresh full-scope ownership/review/Contents-preservation audit and freeze inputs.

## Packaging and next actions

Latest preview package remains v7/v11 in
`../skill-packages/text-corpus-preview-20261030-v7/mcm-icm-master-skill/`:21,529
payload files, copied integrity PASS0,49 installed preimages unchanged; relative
root/unrelated-cwd reader works. No v12/v13/v14 package or live installation.
Database absence errors rather than falling back to fragment cards. Full-chapter
query/coverage/final-gate support already exists; no need to rebuild packaging
after every typo. No full-read or final skill acceptance is claimed.

1. Next fresh image budget: inspect q164 overview03 and fix source appendix lane
   before promoting the bare-Roman role change. Then finish q170 overviews01-06.
   These seven calls fit a new eight-image segment if no extra crop is necessary.
2. Finish q169's nine and q11's fourteen whole-source overviews across later
   segments; full native censuses already exist, do not reread them needlessly.
3. Resolve the whole abstract quality inventory, then Introduction/all substantive
   chapters, exact paragraph chains and object boundaries. Process ALL defects,
   not only examples. Unicode frontier identifies the remaining literal damage.
4. Batch proofs plus staged q165, freeze/preview/rebuild from original native+53
   OCR manifests; preserve all old generations. Only source-accepted text can meet
   strict exhaustive-reading acceptance. Do not count text database work as closure.

This context transported exactly8 JPEGs: q165 seven overviews2,787,014bytes and
q170 overview00 428,257bytes, total3,215,271bytes. No more images until compaction;
never transport original PNGs, batch images or dump Codex JSONL/base64. Root only.
All own build/test/audit processes completed; no live MCM process remains here.
