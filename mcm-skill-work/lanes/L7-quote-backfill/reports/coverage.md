# L7 quote backfill coverage

Recounted from the lane records and the emitted quote files by `tools/coverage.py`. No count on this page is typed by hand.

| lane | papers | chapter records | coded groups at emit | rows | shortfall | added since emit | empty | dup keys | short quotes |
|---|---|---|---|---|---|---|---|---|---|
| B | 76 | 1068 | 10333 | 10333 | 0 | 0 | 0 | 0 | 671 |
| C | 112 | 1112 | 10397 | 10397 | 0 | 0 | 0 | 0 | 645 |
| D | 55 | 598 | 5308 | 5308 | 0 | 0 | 0 | 0 | 397 |
| E | 60 | 662 | 5024 | 5024 | 0 | 0 | 0 | 0 | 356 |
| F | 48 | 672 | 6794 | 6794 | 0 | 0 | 0 | 0 | 479 |
| total | 351 | 4112 | 37856 | 37856 | 0 | 0 | 0 | 0 | 2548 |

## How each quote verifies

| level | rows | meaning |
|---|---|---|
| exact | 31542 | opening sentence found verbatim after whitespace folding |
| span | 1804 | longest contiguous run of at least 8 block words that verifies |
| nfkc | 1715 | found after NFKC, which collapses fi/fl ligatures |
| squeezed | 1370 | found after removing all whitespace, so line and column breaks vanish |
| unverified | 770 | formula or table block with no prose sentence; first words quoted as-is |
| gapped | 484 | in-order run of at least 8 block words, gaps of at most 8 foreign words |
| layout-only | 97 | paper lost its extracted text; quote copied from the layout unverified |
| ocr-only | 72 | layout read from page images; the extracted text never covered this block |
| text-gap | 2 | paper's text layer drops whole paragraphs; this block quoted from the layout |

## Verification text per lane

| source | rows |
|---|---|
| full.txt | 37592 |
| text/pages | 167 |
| missing | 97 |

## Labels outside the 13-job vocabulary

- **B**: `check+close:handoff` 5, `claim` 290, `claim+close:handoff` 2, `compute+close:handoff` 3, `define+close:handoff` 8, `define+close:route` 1, `derive+close:handoff` 1, `derive+close:route` 1, `ext:claim` 45, `ext:claim+close:handoff` 3, `ext:context` 183, `handoff+close:handoff` 5, `interpret+close:handoff` 50, `limit+close:handoff` 16, `limit+close:route` 1, `mechanism+close:handoff` 4, `read-figure+close:handoff` 12, `route+close:handoff` 10, `select+close:handoff` 2, `source+close:handoff` 6
- **C**: `compute+close:route` 1, `ext:claim` 156, `ext:context` 6, `interpret+close:handoff` 7, `mechanism+close:route` 1
- **D**: `ext:claim` 386, `ext:context` 86
- **E**: none
- **F**: `check+close:check` 1, `check+close:interpret` 1, `check+close:limit` 2, `check+close:route` 2, `compute+close:compute` 2, `compute+close:interpret` 6, `compute+close:select` 1, `define+close:define` 1, `define+close:derive` 1, `derive+close:select` 1, `ext:claim` 190, `ext:claim+close:handoff` 7, `ext:context` 172, `handoff+close:handoff` 21, `interpret+close:compare` 2, `interpret+close:handoff` 3, `interpret+close:interpret` 28, `interpret+close:limit` 6, `interpret+close:mechanism` 1, `interpret+close:select` 4, `limit+close:limit` 8, `limit+close:source` 3, `mechanism+close:derive` 2, `mechanism+close:mechanism` 1, `mechanism+close:route` 1, `mechanism+close:select` 1, `read-figure+close:handoff` 1, `read-figure+close:limit` 2, `read-figure+close:read-figure` 6, `read-figure+close:select` 1, `route+close:route` 5, `select+close:handoff` 17, `source+close:select` 1, `source+close:source` 4
