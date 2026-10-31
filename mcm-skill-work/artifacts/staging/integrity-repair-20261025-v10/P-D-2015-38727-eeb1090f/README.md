# D38727 text recovery — not formula or visual acceptance

The original source PDF SHA-256 is `eeb1090fe4b2231af023d6bb25b69dc4db8eb570bb4ac2393f5caf426047aed0`. This pack repairs a source-text access problem without overwriting the live extraction or interpreting any chart/table.

## Proven from current bytes

The historical `text/full.txt` contains encoded Unicode surrogate codepoints, not literal replacement characters. Reading that file with `errors=replace` expands them into replacement characters; after the extraction script's documented newline/page handling, that lossy view matches all19 current page text files. This is a reproducible cause, not a guess based on how the console displays mathematical letters.

684 adjacent surrogate pairs can be combined into valid scalar characters. Eight unpaired codepoints remain on physical pages3,4,6 and are explicitly tagged, not guessed or dropped. The retained old `tmp/q275-text.txt` matches its recorded decoder after Windows newline translation; that old writer also introduced888 `CRCRLF` sequences. It was read for comparison, not executed.

The fresh text-only extraction from the same verified PDF is valid UTF-8, contains688 mathematical alphanumeric characters and no surrogate codepoints. Its layout/order differs from the historical generation, so full byte/text equivalence is explicitly **false**. Both generations remain separate. All68 language witnesses match the correct physical page in both views; all82 original examples pass anti-copy against each view, maximum shared run3.

## Files

- `original-raw-full.bin`: exact historical bytes, including the problematic encoding.
- `decoded-full.txt`, `decoded/pages/`: repaired historical view with explicit unresolved markers.
- `nfkc-preview-full.txt`, `nfkc-preview/pages/`: normalised reading aid only; mathematical styling is flattened.
- `fresh-native-full.bin`, `fresh-native/pages/`: distinct fresh text generation from the verified PDF; no images rendered.
- `recovery-report.json`: per-page diagnostics, input/output hashes, extractor hash, source-witness checks and both anti-copy replays.
- `recipe.py`: exact recovery generator.

PDF reading guidance treats extracted text as insufficient for layout fidelity. Accordingly, this pack does not certify fractions, symbol placement, equation reading order, physical paragraph boundaries or any graphic. It does not replace the existing model record or change `visual_review_status=pending`. Figure/chart distillation stays paused.

The failed v9 raw-equality attempt is retained with a note. The current comparison reports generation differences openly instead of claiming they disappeared. No live paper file, progress row, transaction, source PDF, old draft or installed skill was changed.
