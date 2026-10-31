# F: storage recovery — 2026-10-31

The user requested immediate cleanup of the full F: volume. Corpus construction
and AI reading did not advance during this operation.

## Cause and scope

- F: capacity reported by Windows: 214,748,360,704 bytes (approximately 200 GiB).
- Available space before recovery: 585,728 bytes.
- Thirty-four native/reflow generations: 81,643,235,453 logical bytes.
- Seventeen standalone preview packages: 41,454,821,141 logical bytes.
- Total: 1,128,586 file paths, 123,098,056,594 logical bytes (114.644 GiB).
- Source PDF directory: 604 files, 1,705,049,237 bytes. No source PDF was changed.
- The builder recopied all papers' raw/parent data, structured text and metrics
  for each correction generation; packaging copied the corpus again. A missing
  allocation budget and missing immutable-content reuse caused accumulation.

## Recovery method

1. NTFS lossless compression of the oldest preview package only. `compact.exe`
   completed successfully: 1,213,660,129 data bytes stored in 437,911,709 bytes;
   available F: space became 781,291,520 bytes. Counts printed by compact include
   filesystem entries and are not the corpus-file inventory denominator.
2. SHA-256 deduplication of frozen files at least 65,536 bytes in the explicitly
   named native/reflow and preview directories. Only `.jsonl`, `.json`, `.bin`,
   `.md`, `.txt`, and `.py` are eligible. SQLite databases are excluded.
3. A temporary same-volume hardlink is created only after full hashes agree.
   Atomic replacement retains the original target if replacement fails. A
   successful replacement is checked to reference the verified canonical file.
   All original paths and bytes remain available; versions are NOT removed.
4. Every replacement is logged with source, destination, hash, length and original
   file identity. Independent verification rehashes the resulting physical files
   and checks every committed destination path against that log.

The first two attempts failed at the first replacement because Windows rejected
replacing an open target. Their original bytes remained intact, temporary links
were removed, and failure logs are retained in v1/v2 and probe1 directories.
The successful single-file probe is separately recorded in
`../storage-recovery-20261031-probe2/`. V3 recovered about 74 GiB and stopped
safely before creating an overlong temporary path. The failed target remained
unchanged. V4 uses a short temporary basename and continues while skipping
already-shared files; its journal is in `../storage-recovery-20261031-v4/`.

## Preservation and future use

- No originals, learning outputs, transaction history, reading runs, observations,
  or other projects are removed. E: reading and build datasets are not deduplicated.
- Shared frozen files must NEVER be edited in place. Corrections must use a new
  version/path; opening an existing hardlink for writing changes all its names.
- Explorer's summed folder sizes may still count each hardlink name; actual
  volume free space is the meaningful recovery measure.
- No more full corpus/package generations on F:. New large outputs must pass
  `scripts/assert_corpus_storage_budget.ps1` on E:, with a positive estimate for
  all new copies, a 20 GiB reserve, and 2x allocation headroom. This preflight is
  required by F:/MCM/AGENTS.md; it is not retroactively injected into frozen
  build scripts. Do not claim those historical scripts were modified.

## Results

Consult `../storage-recovery-20261031-v4/summary.txt` for the final continuation
totals, the per-pass `verification.txt` files for independent hash verification,
and `protected-corpus-validation.json` for source
PDF/legacy-input and current dataset validation. A missing result is pending,
not a successful check. The per-root before inventory is `inventory-apply.tsv`.

Storage guard tests passed for: valid E: output/budget; rejecting F: output;
rejecting path traversal; rejecting an existing output; zero estimate;
insufficient space; a reserve below 20 GiB; all arguments missing; and missing
estimate. These checks create no output directories.

This storage operation is not source-fidelity approval, an AI reading receipt,
a paper-learning closure, or final text-database acceptance.
