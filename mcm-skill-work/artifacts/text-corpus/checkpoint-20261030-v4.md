# Complete text corpus checkpoint — 2026-10-30, v4

The active goal remains the full435-paper/11,552-page database AND actual reading
of ALL corresponding author chapters: abstract, restatement, analysis, assumptions,
notation prose, tasks1–4 modeling/solution, sensitivity/validation, improvement/
evaluation, remaining substantive sections and appendices. An abstract checkpoint
is not final. Preserve v1–v3 and all datasets/runs/evidence, including failed drafts.
No legacy learning transaction/progress write, full-paper closure, installed-skill
replacement, formula correctness check or figure/chart interpretation is claimed.

## Current immutable candidate

- `reflow-20261030-v11/`.
- Dataset `7414f261633ac9ab8c5ac65f3552648538c04e17e87649d8d6fd3bf91f069ba9`.
- Build request `build-request-reflow-20261030-v11.json`; create-only driver
  `scripts/build_text_corpus_v11.py` rebuilt from `native-20261029-v1` using the
  same53 frozen OCR manifests plus existing/new explicit reviews. Do not reapply
  OCR to already augmented raw pages: that would duplicate OCR line IDs.
- `integrity-reflow-20261030-v11.json`: structural integrity PASS, errors0;
  all435 source PDFs checked,11,552 physical pages,954,866 raw lines accounted
  exactly once;290,105 blocks/18,524 section candidates;2,619 protected legacy
  preimages unchanged. These counts do not certify prose fidelity.
-5 source-boundary-reviewed abstracts(q1–q4 andq10); strict source status remains
  more restrictive because other page flags may remain. Zero whole-paper source
  acceptances; `source_completeness_accepted:false`.
-427 nonempty abstract candidates;2 source-local verified absences(q162/q167);
  6 unresolved empty q5,q11,q94,q165,q169,q170. q5 proof is now staged separately.
-219 formerly native-empty pages have unverified local OCR integrated, alongside
  4 earlier OCR pages; do not rerun OCR indiscriminately or call it source approval.

## Applied v11 text repairs

- Repeated wide line spacing can establish a prose-wrap baseline while retaining
  indentation/blank-line boundaries and a source-review flag. q10's first-page
  Summary is three paragraphs; its page2 Dear editor letter is a separate memo.
- Printed registration-form clusters and large titles preceding an explicit
  Abstract are separated from author prose without dropping raw lines. These
  general classifications remain machine candidates, not blanket source approval.
- Inline CambriaMath bbox outliers were pulling prose lines upwards. New working
  flow geometry uses a coherent ordinary-prose baseline only when enough words and
  a very tall math-font outlier support it; raw bbox/text remain unchanged. Every
  inferred flow box has a repair record and an open page flag. Math-only/sparse
  labels, drop caps and normal inline fonts do not establish this baseline.
- q1 physicalpage5: all three Model Overview paragraphs actually compared with the
  source JPEG; ordering now matches. Four printed BBS abbreviations restored by
  three exact counted/hash-bound literal operations. Proofs:
  `reviews/20261030/q001-page5-prose-transcription-v1.json` and
  `q001-page5-prose-order-v1.json`. Do not infer other changed lines are correct.
- q167 complete20-page absence proof applied; q162 absence/q174 text reading lanes
  and q1–q4 reviews/q2 literal repair retained.
- Prospective audit `prospective-reflow-20261030-v11d.json` had all435/11,552/
  954,866 with zero ownership/preimage errors.55 abstract selections changed before
  the additional explicit reviews. No prior generation was modified.

## Current actual-reading state

Current run `reading-runs/all-author-preview-20261030-v11/`, ID
`553a50bf60444af4b857adcd50a75a67`, queryall_author_text/all/exhaustive, preview=true.

-7 actual manually observed/acknowledged batches000000–000006, cursor paper_index0,
  char_offset22401 of q1's63291 characters. No pending batch. Next is batch000007.
- Actual text read through sourcepage16: Summary, Introduction, Assumption,
  Symbols description candidates, fundamental model/sweet-spot method, corking/
  double-spring method, parameter effects/estimation and evaluation introduction.
- Coverage report `all-chapter-coverage-v11-q001-at-22401-20261030.json`:
  96 fully processed unique blocks/11 candidate sections out of98,621 required
  unique blocks/17,584 candidate author sections. Zero complete all-author papers,
  zero all-chapter acceptance. Processing receipts are assertions, not proof of
  understanding or source fidelity.
- Genuine per-batch observations: `reading-observations/all-author-preview-
  20261030-v11-batch000000.json` through000006; no auto-ack or truncated receipt.
- Source defects discovered while reading are explicitly queued in
  `reviews/20261030/q001-prose-defect-frontier-v1.json`: short definitions/units
  still reorder, equation-adjacent sentences split, bullet titles interrupt prior
  continuations, table/diagram labels enter default prose, and some cross-page
  merges join multiple estimation items. Recovery is prose/layout-only; mathematical
  correctness and figure semantics remain paused. Need actual source checks, not
  a broad regex claim or fluent rewriting.

Archived v10 runs remain independently valid for that version ONLY:

- Abstract run ID`e1536e82bc4247f9b887b23f89f63540`:25 batches, cursor27/0,
  25 nonempty selections actually read throughq27, q5/q11 empty unresolved,
  4 source-verified processed, no pending. Nextq28 if inspecting archived v10.
- All-author run ID`d55cd63682634fbcb8dfdffc6b3e4b48`:2 batches, q1 cursor6935,
  no pending; older broken-order candidate observations retained.
- `all-chapter-coverage-v10-at-q027-20261030.json`:284 unique blocks/38 candidate
  sections processed; zero all-author-complete papers. Never sum repeated papers
  across versions or reuse these cursors in v11.

## Newly completed q5 source census — staged after build

- Paper `P-A-2011-11199-cfe6d809`; all21 native-text pages actually read and seven
  three-page heading/layout JPEG overviews actually checked. Page1 title cover,
  page2 directI.Introduction, vertical-air methods/comparisons/limitations, rotation
  methods, explicitIV.Conclusion onpage19, References20 andEnd Notes21. There is no
  independent abstract. The local "In summary" paragraph onpage16 and closing
  conclusion must not be relabelled as an abstract.
- `reviews/20261030/q005-abstract-absence-v1.json` plus hash-bound
  `q005-full-native-prose-census-v1.json`; portable preflight passes51 evidence
  files. Local604-record/file-inventory search found only the same21-page PDF.
- STAGED ONLY: v10/v11 not modified. This is source-local absence, not an abstract
  read or whole-paper prose approval. Quotation/replacement glyphs and mixed
  notation remain unresolved. Apply in a later batch with other accepted repairs.
- Evidence prepared by `scripts/prepare_text_source_overviews.py`; all native text
  and PNGs remain on disk, only bounded JPEGs transported.

## Whole-scope defects, tests and package

- Latest diagnostic `section-candidate-audit-20261030-v11.json`:6 empty unresolved,
  59 multipage,2 possible fragmentation,33 possible form contamination,1 possible
  letter contamination,1 envelope warning(q40 already source-checked false
  positive),2 verified absences. Findings overlap and are not all proven defects.
- Open source flags: boundaries18,519,hyphen9,766,privateglyph5,474,crosspage5,131,
  crossengine1,850,contents345,margin251,OCR223,column90,inline-math-flow228pages,
  expandedspacing57,summarysubheading5,openingletter1,Unicode21blocks. Changed
  paragraph/block granularity can change issue counts; don't infer glyph loss from
  count changes or equate these flags to distinct prose errors.
- Tests266 pytest passed/264 unittest passed after prose geometry changes; plan
  protocol validation PASS0. Expected negative-fixture stdout is not suite failure.
- Completed v10 preview package:
  `../skill-packages/text-corpus-preview-20261030-v6/mcm-icm-master-skill/`,21,418
  payload files plus manifest, relative database lookup works from unrelated cwd,
  installed skill unchanged. Wrong explicit database root correctly errors with no
  card fallback; that diagnostic was corrected by using the package's default path.
- New v11 preview package COMPLETE, execsession42480 exited0:
  `../skill-packages/text-corpus-preview-20261030-v7/mcm-icm-master-skill/`.
  21,529 payload files plus manifest; copied-corpus structural integrity PASS0;
  all49 installed-skill preimages unchanged. Packaged `sections` command from
  unrelated cwd finds all435 records, including the new restatement/analysis/
  improvements roles. Preview-only, not final and not installed. No live process
  remains from this checkpoint; do not restart packaging unnecessarily.
- New complete queries/task1–4/exact-title routes, coverage union and final
  all-chapter-reading package gate remain in scripts/templates. Explicit task
  labels are supported; chapter number alone is not a task ID. Unmapped tasks stay
  unresolved, never falsely absent. `corpus_queries.py` frozen inside v11 inputs.

## Next work and guardrails

1. Continue v11 all-author run atq1 offset22401, actual manual observations and ack
   only after reading full payload/marker. Full435-paper/all-chapter goal stays active.
2. Source-check queued short-prose/item-boundary defects after context compaction;
   current image quota is exhausted. Do not resume formula or graph verification.
3. Resolve the other5 unresolved empty cases after stagedq5, and other abstract/
   Introduction/all-body source defects. Do not declare source absence from a TOC,
   missing heading or first-page sample. Don't endlessly copy a generation per typo.
4. Batch reviewed changes andq5 proof into a future immutable version, preserve all
   inputs and run full ownership/provenance/source fidelity/reader checks. New
   dataset means new cursor; preview work is never strict full-reading acceptance.

No subagents or cleanup/deletion. This context viewed exactly8 JPEGs: q1page5
202,272bytes plus q5sevenoverviews2,435,336bytes, total2,637,608bytes. No more images
until compaction; originals never transported, no full Codex JSONL/base64 output.
