# Complete text corpus checkpoint —2026-10-31,v4

Goal ACTIVE:435papers/11,552physicalpages, continuous traceable text, exhaustive
reader, separate installable skill and actual AI reading of ALL author chapters.
Abstracts are only the first checkpoint. Main agent/no new agents. Preserve every
source, old generation/failed draft, legacy record/history, installed skill and
dirty-worktree change. Formula correctness and figure interpretation paused.
Individual source restoration is required after repeated broad-rule failures.

## Latest accepted immutable corpus: v22

`reflow-20261031-v22`, dataset
`98ce58682c4bdbba819154c62a68c1a35f342b50fbee2b1b4aed9ff4de7eeb88`.
`integrity-reflow-20261031-v22.json` DONE/PASS/errors0:
435papers/11,552pages/954,866source lines exactly accounted,292,281blocks,
18,521candidate sections,5boundary reviews,2,619legacy preimages unchanged.
Source completeness FALSE; zero whole-paper source acceptance.427nonempty
abstract candidates/6source-local absences/2empty unresolved(q11/q169), only4
abstracts currently source-verified.19unresolved Unicode blocks and all remaining
source flags explicit. Flags overlap; they are not a count of proven prose defects.

v21also DONEPASS (cded4470...), retained. All prior generations and rejectedv13
remain untouched. Do not restart completed builds.

## Combined-task query omission FIXED

`corpus_queries.task_numbers` previously dropped second numbers in explicit
Task1&2/Problem2and3 labels. New policy
`38d6dc80383b375ce95ea374bf3fe0677e970a13be2143c9ad9de5b54a6beaca`
handles shared lists, plural labels, Roman/English numbers, Oxford commas and
explicit ranges. Task1&4 means only1/4; Tasks1–4 means1/2/3/4. Chapter ordinals,
years and Problem12 do not become task matches. Original Chinese behavior is
retained except that 问题12 no longer falsely matches1.

Three meaningful regression tests first RED, now PASS. Latest full suites:
328pytestPASS15.26s,326unittestOK14.42s. No need to repeat absent new core edits.
`reviews/20261031/task-selector-upgrade-inventory-v1.json` exhaustively compared
all18,524stored titles in all435papers:13changed headings, no other differences.
The original11 plus2Task2,3 code-appendix titles are all explicit shared labels.
The inventory proves query changes, not PDF fidelity or code/prose classification.
v22build includes exact11-title/22task-selection replay, with no duplicated blocks.

**Task mapping remains incomplete:** task1/2currently76nonempty candidates each,
task3=82,task4=56; all queries retain435targets. Other targets are UNRESOLVED,
not verified-absent. Do not claim all task chapters are mapped.

## Individually restored q53, applied in v22

Physically inspected pages1–3 individually. Old summary candidate included a
two-column newspaper handout then stopped before its announced four strategies.
- Actual summary7paragraphs/page1,4036characters.
- Separate literal title A Fishy Situation/page2,2821characters:4introductory
paragraphs,4complete strategy items,1closing paragraph.
- Join the source cross-column sentence losing access to the herring, put$1.00
back in non-body masthead ownership, preserve caption separately, no image
interpretation. Page3is Contents.
-9exact word-wrap/unit-glyph replacements, no author wording rewrite. All lines
owned once. Newspaper remains role other, explicit-title retrieval works; no
silent claim that it is already a verified memo category.
- Proofs/findings/stage in `reviews/20261031/q053-*` and
`scripts/stage_q053_opening_repair.py`. Later body/source acceptance pending.
Prior q32/q46paragraph links and q47–q50repairs retained.

## V22 affected transport COMPLETE

`reader-transport-reconstruction-20261031-v22-v1.json` DONEexit0. Six affected
queries(task1–4,abstract,all_author_text), each435targets, exact reassembly,
source spans, budgets and interrupted-resume replayPASS. No AI receipts created.
- abstract1,309,352characters/436batches/40resume replays.
- all_author_text20,103,007characters/5878batches/535resume replays.
Frozen reproduction runtime `transport-runtime-v22-20261031-v1/scripts/`.
Oldv20all19query report still retained. Do not sum overlapping queries or call
machine transport source fidelity/understanding.

## LIVE jobs — poll SAME handles, never restart

1. **session99935**: `python scripts/build_text_corpus_v23.py`, create-only
`reflow-20261031-v23`. Started after full prospectivev16PASS/errors0/conflicts0,
435/11552/954866/Contents352→352, binding4q55/q58proofs. Poll existing handle.
Do not edit13frozen modules or driver until terminal success/failure:
source_span_metrics.py,text_corpus.py,preview_span_origin_flow.py,
source_text_repairs.py,source_layout_reviews.py,source_absence_reviews.py,
resegment_text_corpus.py,corpus_queries.py,corpus_reader.py,
source_paragraph_reviews.py,index_text_corpus.py,validate_text_corpus.py,
verify_reader_transport.py, plus build_text_corpus_v23.py.
2. **session88695**: separate v10preview package from acceptedv22. Output
`artifacts/skill-packages/text-corpus-preview-20261031-v10/mcm-icm-master-skill`.
Base is **C:/Users/Lenovo/.claude/skills/mcm-icm-master-skill**;49base preimages
matchedv9before start. C:/Users/Lenovo/.codex/skills/mcm-cup-standard-write is a
different skill, not the package base. No installed write. Sparse output normal
during source/copy validation. Do not edit runtime/packaging templates mid-job.
After success run create-only smoke v10 from unrelated cwd, no ack.

v21session56885,v22session85337,prospectivev15session47160,
prospectivev16session88772,v22transportsession6212 all DONEexit0. v9package45395
and its smoke also DONEPASS. Do not repoll/restart these completed jobs.

## Q55/q58 individual repairs for v23

Source page1andnextpage2actually inspected for each.
- q55P-A-2021-2100454-dc37ed6a:7summary paragraphs,3075characters. GAME sentence
different fungi and their effect restored as one paragraph;9literal wraps/accent
repairs. Printed effeciency/representitive/shown retained. Source title/form,
both summary labels,keywords,watermark/QR stored separately. Page2Contents.
- q58P-A-2021-2110178-2aed1e20:6summary paragraphs,3005characters. ModelI
multi-fungi sentence restored; lexical hyphens in multi-fungi/long-term retained;
6literal wrap repairs. Bold model labels remain inline prose, not body sections.
Page2Contents; non-body text retained separately.
- stage_q055_q058_summary_repairs.py and source proofs inreviews/20261031.
Full prospectivev16replayed every legacy proof before v23start. Neither proof
adds whole-paper source acceptance or an AI processing receipt.

## Actual AI reading: v16 frozen previewv8 runtime only

Run `reading-runs/abstract-preview-20261030-v16`, runID
541d2520dc494e22a4ae952bd718d398, dataset
7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65.
At checkpoint save:88acks000000–000087, throughq87,85nonempty candidates
fullyprocessed; q5absence/q11empty unresolved separate. Source-verified processed4.
Current nextbatch000088/q88 was just requested; inspect currentstatus/output
before acknowledging. All observations are manually written after actual text
reading; no autoacks. Future counts may be ahead of this checkpoint.

Use only unmodified packagedpreviewv8reader for this old run:
`python artifacts/skill-packages/text-corpus-preview-20261030-v8/mcm-icm-master-skill/scripts/corpus_reader.py --corpus-root artifacts/text-corpus/reflow-20261030-v16 next --run-dir artifacts/text-corpus/reading-runs/abstract-preview-20261030-v16`
Same runtime/root forack/status. Current working policy differs and must refuse
mixed-policy resume. Never rewrite old receipts or sum different-version runs.

New observations000063–000087coverq65–q87, including split longq86/q87.
Important unresolved source issues now recorded: q66third-party opening quote;
q68/q72/q73/q76/q79/q84orphan/truncated Keywords; q75possible repeated source
definition; q81understand-/ing false paragraph and repeatedmnoise; q82Gaussian/
Mixture false paragraph and repeatedmnoise; q83/q84repeatedmnoise; q85pagefooter;
q86title merged with firstparagraph/inlineglyph; q87technical and executive
summaries on3pages need preserved original labels and source scope checking.
Q86ending admits insufficient statistical evidence, sudden-behavior failure and
better anchor-point than next-strike predictions. Q87ending concedes no proven
advantage over human profiling despite random-baseline improvement. All literal
candidate text was read, including limitations and noise; no source completion
or statistical/formula/figure correctness inferred.

## Other source check, image budget and next

q11overview01physicalpages4–6actually inspected for heading/object ownership:
problem-analysis continuation→8assumptions; notationtable; model1body. Findings
`q011-pages4-6-layout-findings-v1.json`. Prior source checks1–3/28–30retained.
Remaining prepared overviews unread; no whole-source abstract absence accepted.

This context segment used **8JPEGs/2,638,609bytes**:q53p1–3,q55p1/2,q58p1/2,
q11overview01. **No more images until compaction.** No rawPNG enteredcontext.
One/call≤450KB. Noagents,legacytransactions,installedwrites,deletes or cleanup.

Next: poll99935/88695,smokev10oncefinished; source-aware continuation afterfresh
image budget prioritizesq81–84OCRnoise/paragraphs and earlier unresolved cases.
Keep actual section reading moving and do not stop at an abstract checkpoint.
All source/all-chapter acceptance remains unfinished and goal staysACTIVE.
