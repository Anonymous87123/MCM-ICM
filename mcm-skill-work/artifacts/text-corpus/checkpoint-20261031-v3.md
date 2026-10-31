# Complete text corpus checkpoint -2026-10-31, v3

Goal ACTIVE:435 papers/11,552 pages, complete continuous traceable text, exhaustive
section reader, separate installable skill and actual AI reading of ALL author
chapters. Abstracts are a first checkpoint only. Main agent/no new agents. Formula
correctness and figure interpretation paused. Preserve every old generation,
failed draft, legacy artifact/history, source and installed skill. Repeated broad
repair failure must switch to individual paper/page restoration.

## Latest completed immutable corpus: v20

- Root `reflow-20261031-v20`; dataset
`abddf33234d0e9e04ca6c5a27c3bef1298fe5e2772b7452f2a6dd6489dd6995a`.
- `integrity-reflow-20261031-v20.json` completed PASS/errors0:435 papers,
11,552 physical pages,954,866 source lines exactly accounted,292,305 blocks,
18,524 candidate sections,5 source boundary reviews,2,619 protected legacy
preimages unchanged. Original PDF hashes freshly checked.
- Source completeness FALSE; zero whole-paper source acceptance.427 nonempty
abstract candidates/6 source-local absences/2 empty unresolved(q11/q169).
Machine flags overlap and do not count proven prose defects. Current19 unresolved
unicode blocks,5,115 cross-page candidates,9,746 word-wrap flags,18,519 section
boundaries and all other review frontiers remain explicit. Do not certify source
completeness from source-line accounting or transport.
- V19 also completed successfully, dataset50b96e98..., preserved. Earlier v18,
v17/v16 and rejected v13 remain untouched. Do not rerun finished builds.

## V20 source repairs and code

- Individually inspected q46 physical pages1–4: actual four-paragraph abstract
ends on page1, two-page letter occupies pages2–3, body begins page4. Old abstract
selection9572chars included the letter and repeated page3 header in mid-sentence.
New abstract2311chars, separate Memo7072chars; all letter author prose retained.
Form/title/date stored separately; five printed word wraps repaired literally.
- Source-checked page4 inline headings are now explicit openings without
discarding the first author sentence: Introduction1326chars/two paragraphs,
Problem Statement902chars, Data1135chars/three paragraphs; model subheadings also
preserved. The exact printed prefix names the section while the literal first
paragraph stays intact. New test first reproduced rejection; now passes.
- `source_paragraph_reviews.py` adds individually checked logical continuation
links while preserving each original block/line/page. Links require exact text
hashes, same section, adjacent physical pages, only furniture between fragments,
and complete checked-page coverage. Validator replays proofs; unlogged/branching
or stale links fail. `text_with_block_spans` produces joined chapter text and exact
block offsets. Reader, Markdown and SQLite share it; transport oracle rebuilds
separators independently. Old documents without links render identically.
- Checked q32 page3→4 continuation now7515chars, retaining the five paragraphs
previously stolen by midpage Contents. Checked q46 letter page2→3 now joins
`prey species (assumed to be deer)` without repeated header. Source blocks and
their raw hashes unchanged; no section/paper acceptance inferred.
- Proofs/findings in `reviews/20261031/`:q046-opening-layout-v1,
q046-opening-word-repairs-v1,q032-paragraph-continuation-v1,
q046-paragraph-continuation-v1. Stage scripts with corresponding names preserved.

## V20 transport COMPLETE

`reader-transport-reconstruction-20261031-v20-v1.json`, exit0. All19 queries, each
435 targets, exact full reassembly/resume/source spans/budgets PASS. No delivery
or AI receipt files created by simulation. Frozen reproduction runtime:
`transport-runtime-v20-20261031-v1/scripts/`.

- abstract1,311,438chars/437batches/40resume replays.
- all_author_text20,103,297chars/5879batches/535replays.
- memo318,363chars/129batches/12replays.
- Do not sum overlapping queries or call these source fidelity/AI understanding.
- Query policy24d0749e...; reader60f69df2...; libraryd9bbbf63...;
transport8a75da07.... Exact hashes in runtime manifest/build request/report.

## LIVE jobs: poll same sessions, never restart

1. **session56885**: `python scripts/build_text_corpus_v21.py`, create-only
`reflow-20261031-v21`. Latest outputq100; build-request frozen. Full prospective
`span-origin-flow-full-20261031-v14.json` completed PASS435/11552/954866,
errors0/replay conflicts0/Contents352→352, binding four exact q47–q50 proofs.
Do not edit its13 frozen modules or driver until terminal success/failure:
source_span_metrics.py,text_corpus.py,preview_span_origin_flow.py,
source_text_repairs.py,source_layout_reviews.py,source_absence_reviews.py,
resegment_text_corpus.py,corpus_queries.py,corpus_reader.py,
source_paragraph_reviews.py,index_text_corpus.py,validate_text_corpus.py,
verify_reader_transport.py, plus build_text_corpus_v21.py.
2. **session45395**: independent preview packagev9/v20, started
`package_text_corpus_skill.py --preview`, output
`artifacts/skill-packages/text-corpus-preview-20261031-v9/mcm-icm-master-skill`.
Still running/sparse output expected during full source/copy validation. Do not
restart or change packaging source templates/runtime. Installed base49preimages
checked on completion; no installed overwrite authorized/performed.
After completion run existing `smoke_test_packaged_corpus.py` from unrelated cwd
with new create-only smoke run/report. If package is incomplete, preserve it.

All sessions2438(v20build),7499(prospectivev13),53936(prospectivev14),
27573(v20transport),72334(pytest),32333(unittest) finished exit0; do not repoll.

## Individually checked q47–q50 staged repairs for v21

- q47 P-A-2020-2001334-a7774d36: actual six paragraphs; competition MCM/ICM
metadata and QR promotion separately classified, distribu-/tion joined only.
Candidate3868chars. Printed `date monthly`/`strategys effect` retained unedited.
- q48 P-A-2020-2002354-f00d018f: actual eight author paragraphs; banner and QR
promotion separately classified;3097chars. Both Summary Sheet and Summary labels
retained. First preflight display mistakenly subtracted only one heading and
reported9; separate immutable count-correction-v2 records8. The actual gate
already counted eight correctly; old report/source proofs preserved.
- q49 P-A-2020-2003298-d28634b8: separate title was merged with first paragraph;
actual six paragraphs restored with title/form/keywords/QR separate;3510chars.
- q50 P-A-2020-2003485-fe70a967: five paragraphs remain intact; exact banner
classification only;3793chars. Existing QR/keywords already excluded, no guessing.
- Three text proofsv2 directly freeze JPEG/native evidence, operations unchanged;
q49 layoutv1 has complete portable page evidence. Source acceptanceFALSE. Only
page1 inspected for these four; later/next-page boundaries remain unreviewed.

## Actual AI reading: v16 frozen runtime only

- Run `reading-runs/abstract-preview-20261030-v16`, ID
541d2520dc494e22a4ae952bd718d398, dataset
7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65.
- At checkpoint save:60acks000000–000059, throughq61,59nonempty candidates
fullyprocessed,4source-verified; q5absence/q11empty unresolved separate.
- Pending batch000060/q62 was actually read but observation/ack NOT YET SAVED.
Text2734chars includes a result table flattened into prose, formation table,
question-led power-duration→energy/piecewiseoptimization→wind/deviation
sensitivity→headwind-triggered team strategy→DirecteurSportifguide. Tables were
not interpreted/verified. Observe conditional crosswind/headwind versus rider
deviation evidence, report source table-role/paragraph classification pending.
Marker647af8d0e155f0527aef5303bf16d03cb37ca8833d840359abc22aa832e40eb8.
Always inspect currentstatus/batch before quoting later counts.
- Continue ONLY with previewv8 unmodified packaged runtime:
`python artifacts/skill-packages/text-corpus-preview-20261030-v8/mcm-icm-master-skill/scripts/corpus_reader.py --corpus-root artifacts/text-corpus/reflow-20261030-v16 next --run-dir artifacts/text-corpus/reading-runs/abstract-preview-20261030-v16`
Use same path/root forack/status. No mixed v16 cursor/v20policy or automaticacks.
Every processed batch has manually written observations/source issues BEFOREack.
- Q46 frozen candidate fullyread across3batches, including letter; no old receipt
bytes changed by source corrections. Q53 frozen6025char candidate includes a
magazine handout, price/caption inserted into a sentence and ends before announced
four strategies: physical source/ownership repair remains pending, not complete
handout reading. Q55–60 have real sentence/word/paragraph fragmentation recorded.
- Oldv11all-author andv10abstract runs separate; never sum them into this run.
All chapters/all-paper reading acceptance still FALSE.

## Tests, safety, immediate next

- Latest full suites325pytest PASS14.99s;323unittest OK14.497s. Expected negative
fixture statusfail is not suite failure. No broad reruns unless new edits/failures.
- This segment inspected **8JPEGs/3,079,797bytes**:q46p1–4, q47p1,q48p1,
q49p1,q50p1. **No more images until compaction**. No raw PNG/context image batches,
Codex JSONL dumps, subagents, deletes, legacy transactions or installed writes.
- Next: poll56885/45395; inspect real outcomes. Smoke-test previewv9 once complete.
Continue pendingq62 observation/manualack and subsequent exhaustive text batches.
Fresh image segment priorities:individual q51–60 fragmentation and q53 handout;
earlier q11/q169empty and q19/q21/q22/q23/q25/q27/q38 defects remain pending.
All-body chapter mapping, unicode/OCR and source fidelity frontiers remain open.
Promote batches of checked source repairs without weakening gates or rewriting
authors. Goal staysACTIVE; no final acceptance claimed.
