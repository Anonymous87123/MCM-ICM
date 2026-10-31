# Full-text corpus checkpoint — 2026-10-31 v13

Goal remains ACTIVE. Scope435papers/11,552physical pages/all A–F. Full-source and all-chapter actual-reading acceptance remain unfinished. No installation, deletion, cleanup, legacy closure or new agents.

## Accepted and live candidate

- Latest accepted generation: `reflow-20261031-v30`,dataset `8bbcda111760e342bd2ccf70c7e18e2294986b329545e20a57f23aad77458e1e`.
- Structural PASS/errors0:435papers/11552pages/954866source lines;291702blocks/18490sections;435continuous author views;11verified boundaries;2619protected legacy inputs.
- Abstract source states:8verified/419present-unverified/8verified-absent/0emptyunresolved. Whole-source acceptance FALSE.
- V30transport reconstruction PASS; separate previewv16package+smoke PASS. Installed skill unchanged.
- Rejectedv31remains preserved. It restored q244/q248prose but q244keyword Performance wrap retained a page flag, so reader status failed the verified guard. No waiver or promotion.
- Q244newv2spec/proofs restore the separately stored keyword wrap;7author paragraphs/2341chars/SHA `b9ef84ca549269a660ea0ac7d1ef5e4319c1b5e9e21fc1e83db12d3cee7490b8`unchanged.9author wraps+1keyword wrap;5author flags+1keyword flag resolved. All source IDs once;later prose unchanged.
- Fullprospectivev26PASS:parentv30/exactq244v2+q248v1proofs;435/11552/954866;Contents352before/after;errors0/replay0.
- **LIVE buildsession67489**: `python -X utf8 scripts/build_text_corpus_v32.py`. Index completed435/11552;datasetcandidate `66c16ab51d1b915b5f8f851c1b600f84b158687b7f51fc30d1466d8746e43954`;291675blocks/18488sections. Global byte/status/validation guards still running. Do not promote until normal exit0 and `integrity-reflow-20261031-v32.json`PASS. Do not modify its frozen core/driver while live.

## q267source repair

- Paper `P-C-2025-2516178-573cdff6`;both complete opening JPEGs,focused first-task crop and all46old OCR lines actually read. Page2isContents;Summaryends page1before Keywords.
- Missing line recovered exactly: `the last-block cross-validation approach, a type of time-series cross-validation.`
- Failed local detection cropv1retained/rejected(score0.56801). Focused single-line local recognitionv2matches source(score0.99303);no download or source modification.
- `reviews/20261031/q267-ocr-line-restoration-v2`STAGED/PASS:46old OCR line objects unchanged+1inserted source line;6complete author paragraphs/3131chars;SHA `27db0000f9ad855f506391641f2c3fdda3d1b93a8f7dced4daaac0b8ace05f26`. Two false title fragments restored to prose;6wraps+1quote fixed. All source IDs accounted once;later author prose unchanged.
- Prospective q267raw hash `21ba8c30cc2e4278d3a3937b86dca166c53dc45e4ec37d96ebbe73dfb366261d`;not in accepted corpus yet. OCR/cross-engine page flags remain open;native metric rebinding still required.
- Earlier stagingv1failed because empty opening abstract placeholder was counted as a real chapter;its partial evidence preserved. V2filters nonempty source-owned chapter IDs, without excluding any author text.
- New `source_ocr_page_reviews.py`exists but is **not hooked into frozen core**. It requires exact raw-page bytes,complete source layout,final text/source IDs,actually read bounded JPEG and an accepted chapter review;it rejects formulas/objects/uncovered author material and preserves extraction disagreement as disagreement. Two focused tests PASS after fixing a synthetic assertion to preserve unrelated empty-section debt. No page flags automatically cleared yet.
- `stage_q267_source_page_acceptance.py`written but NOT RUN. Requires acceptedv32. It freshly rematches all27PDFnative pages,requires identical native metric payload,creates separate435-paper metrics sidecar and stages exact source-page approval. Must preserve old sidecar. Run afterv32acceptance;then integrate module into resegment/validator with meaningful tests beforev33build.

## Actual-reading run

- Original frozen reader only: `artifacts/skill-packages/text-corpus-preview-20261030-v8/mcm-icm-master-skill/scripts/corpus_reader.py`.
- Root `artifacts/text-corpus/reflow-20261030-v16`;run `reading-runs/abstract-preview-20261030-v16`;ID `541d2520dc494e22a4ae952bd718d398`.
- **274ACKs**,sequences000000–000273;cursorpaper_index274/char0;throughq274;266nonempty candidates fully processed;6old absences/2old empty unresolved/4old source-verified processed. No pending batch. Nextq275NOTrequested.
- q271was genuinely read in two pieces[0,4230)and[4230,4494),with separate receipts;no skipped tail. Q272–274complete candidates read. Source issues remain explicit.
- Latest snapshotthroughq270:625raw historical explicit issues/233papers;2bound corrections. It is not a live unresolved-defect total. Current run newer than snapshot;do not transfer receipts to later datasets.

## Tests and continuation

- Keyword core change:348pytest/346unittestPASS. Enhanced explicit-summary stager was followed by another348pytest/346unittestPASS(sessions96014/21468). New OCRpage module adds2focused tests only;full suite after hooks not run yet.
- This context used3JPEGs/732720bytes,allq267;no original PNG sent. Limit8images/4MiB per context;oneimage/call/max450000bytes.
- Existing non-root Python processes are `run_cc_parallel_handoff_batch.py`jobs;left untouched. Root owns only the known build/test sessions.
- Next:pollv32;source-bindq267metrics/page proof;hook/validate exact OCR prose-page acceptance;guarded newgeneration;continue frozen reader sequentially. Protect all previous versions/packages/failed candidates and installed skill.
