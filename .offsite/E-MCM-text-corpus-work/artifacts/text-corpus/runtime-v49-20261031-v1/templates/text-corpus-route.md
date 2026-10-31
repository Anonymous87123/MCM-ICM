## Complete-corpus reading (takes precedence for requests about all papers)

When the user asks how all awarded papers write a section, read the complete
requested sections before synthesizing or drafting. Type-specific reference
routing below does NOT narrow an explicit all-papers request. Do not substitute
language cards, sentence skeletons, paragraph previews, search hits or top-k papers.

The local data attachment is `assets/text-corpus/`; the reader also accepts an
explicit `--corpus-root` before the subcommand. If missing, report the missing
database. There is no fragment-only fallback. See
[complete-corpus-reading.md](references/complete-corpus-reading.md).

1. Run `python scripts/corpus_reader.py sections` and `queries` to inspect roles
   and complete query families. Keep problem restatement/analysis and explicit
   task numbers distinct; chapter numbers do not establish task identities.
2. Start an exhaustive run, e.g.
   `python scripts/corpus_reader.py start --section abstract --scope all --mode exhaustive --run-dir <new-run-directory>`.
3. Call `next --run-dir <run-directory>` and actually read ALL returned text, not
   only the first sentence or the beginning of each chunk. Preserve the end marker.
4. Write observations for EVERY paper in this batch, citing delivered block IDs.
   A partial chapter warrants observations about that portion only. Then call
   `ack --run-dir <run-directory> --completion-marker <marker> --observations <json-file>`.
5. Continue with `next`/`resume` until status confirms traversal complete. No
   automatic acknowledgements. Save the run path across context changes.
6. Synthesize using all per-paper observations, count supporting papers and
   counterexamples, and re-open full source sections when comparing wording.
   Do not imply all originals remain simultaneously in the context window.

For all chapters use `--section all_author_text`. Use `coverage --run-dir <run>`
(repeat for multiple same-generation runs) to inspect source-block coverage of
every author chapter. Unknown-role sections and appendices remain in the full
traversal. A finished abstract run does not establish full-body reading acceptance.

Normal strict mode refuses unverified boundaries/text. `--allow-unverified` is
only an explicitly labelled draft preview, not whole-corpus acceptance. Distinguish
papers expected, section present, verified absent, unresolved, fully delivered,
AI-processing receipts, and source-verified reading. Receipts document agent
assertions; they do not prove comprehension. Never say "read all papers" when
some were skipped, unresolved, truncated, or merely traversed by a program.

Default author-section queries exclude nested Contents, References and AI reports,
not just those at the top level. Their text remains separately addressable by an
explicit role/title request. A selected parent still includes all author children.
New runs bind a query-policy hash as well as the data version. If either changes,
preserve the old run and start a new version-bound run; do not edit its receipts.

The reader caps each batch at 6,000 tokens and 32 KiB; without a tokenizer it uses
a conservative UTF-8 byte upper bound. Lower `--max-tokens`/`--max-bytes` when the
remaining context is smaller. Keep the tool output limit above the entire batch.
Normal reading transfers text only. Local OCR/page-text checks do not authorize
figure interpretation or equation verification while those tasks are paused.

