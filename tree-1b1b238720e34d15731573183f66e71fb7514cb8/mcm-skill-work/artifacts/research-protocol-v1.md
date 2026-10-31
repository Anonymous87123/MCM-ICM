# Sequential Paper Research Protocol v1

Status: frozen after the 12-paper A-F calibration set on 2026-07-11.

## Purpose

This protocol governs the one-paper transaction used to turn the eligible MCM/ICM corpus into evidence-bearing type-specific rules and, eventually, an installable master skill. It freezes the minimum review standard demonstrated by the pilot. A later protocol version may add fields or checks, but it must migrate and revalidate every earlier artifact before use.

## Pilot Gate

- Papers: 12 of 12 closed and fully validated.
- Coverage: two papers from each type A-F, spanning an early and recent example where available.
- Atomic observations: 457.
- Current cumulative seed rules: A 14, B 23, C 24, D 28, E 25, F 24; total 138.
- Visual review: complete for every paper.
- Cross-validation: all 12 paper cards, observation files, type branches, manifest records, and extraction records pass `validate_paper_artifacts.py --require-complete-visual-review`.
- Regression suite: 20 of 20 tests pass.

## Transaction

Process exactly one paper at a time:

1. Select the first non-closed paper in the active type queue.
2. Verify manifest identity, hash, type, award basis, page count, and source path.
3. Locate authoritative context. Record whether the complete statement is available; never promote a paper restatement to an official requirement.
4. Extract page-aware text and render every page.
5. Review contact sheets for all pages and inspect every equation-, table-, figure-, map-, and compliance-critical page at full resolution.
6. Reconstruct the task, sections, dependency graph, assumptions, data lineage, models, validation, results, writing, language, and visualization.
7. Test arithmetic, units, signs, domains, conservation, objective orientation, metric definitions, dimensions, and cross-section consistency before accepting narrative claims.
8. Record atomic observations with exact page anchors, evidence class, counterevidence, confidence, and candidate rule IDs.
9. Record both defects and competitive strengths. Treat award status as provenance only. Use class `C` for hypotheses about why a paper may have succeeded unless an official judge source supports class `J`.
10. Update only the matching A-F rule branch. New single-paper rules remain `seed` with low confidence unless stronger evidence already exists.
11. Create the complete paper card, including independent corrections and unresolved questions.
12. Run single-paper cross-validation and the full regression suite.
13. Close the progress record atomically only after extraction, card, branch, and validation all pass.

## Evidence Rules

- `O`: direct source observation.
- `P`: close, source-anchored paraphrase.
- `I`: cross-paper induction supported within one problem type.
- `E`: independent correction or extension.
- `J`: judge-preference claim supported by authoritative judge evidence.
- `C`: conjecture, including paper-specific award explanations.

Never disguise an extension as historical evidence. Retain useful counterexamples and minority practices even when they are not promoted as defaults.

## Error Gate

A prestigious award never relaxes correctness checks. Record substantive errors explicitly and convert recurring risks into forbidden patterns and required tests. At minimum, audit:

- source totals, row and column totals, and conservation;
- dimensions, units, signs, nonnegative domains, and bounds;
- objective direction and criterion orientation;
- metric identities and invariants, including entropy normalization and MAE/MSE consistency;
- equation-assumption-prose consistency;
- data construct, exposure, selection, reporting, missingness, and deduplication;
- train, validation, and test separation and temporal availability;
- causal identification versus association or prediction;
- scenario basis, uncertainty, robustness, and decision reversal;
- policy authority, implementation, cost, distribution, rights, monitoring, and contingency;
- page limits and required communication artifacts.

Any blocking invariant failure caps downstream claims until corrected or bounded.

## Competitive-Strength Gate

Every paper card must identify what is worth learning even when the paper contains serious errors. Inspect:

- first-page clarity and task coverage;
- progressive model architecture and handoffs;
- useful abstractions and baselines;
- data engagement and anomaly discovery;
- purpose-aligned visualization;
- sensitivity or scale tests that reveal limits;
- candid limitation writing;
- audience-specific memos or letters;
- exact submission compliance.

These strengths explain possible persuasiveness, not mathematical validity or judging causality.

## Data and Reproduction Gate

Treat the observation process as part of the model. A final operational rule must identify raw sources, definitions, versions, transformations, missingness, exposure, uncertainty, code, environment, parameters, solver or training settings, and machine-readable results. When a historical paper omits them, preserve the omission as evidence and define the reproduction bundle that a new solution must provide.

## Schema Freeze

Protocol v1 uses the current schemas and validator contracts for manifest records, progress records, paper cards, and observations. Required paper-card arrays remain page anchored. Candidate observation rule IDs and paper-card rule impacts must resolve to the current type branch. Rule evidence must resolve across the observation corpus and exactly match `source_papers` and `source_count`.

If a later paper requires a schema change:

1. version the schema and validator;
2. document the reason and migration;
3. migrate every affected prior artifact;
4. rerun all paper validations and tests;
5. freeze a new protocol version only after the gate passes.

## Next Queue Item

After this freeze, full sequential study begins with `P-A-2010-7571-1ac2a627`, queue position 2. Type A remains active until every eligible A paper is closed; only then does the full study proceed through B, C, D, E, and F.
