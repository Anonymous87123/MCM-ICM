# MCM/ICM Learning Execution Rules

- Follow `F:\MCM\plan.md` and process exactly one deterministic paper through G0-G8 before advancing.
- The root agent is the only writer and transaction owner. Read-only subagents may audit bounded page, language, formula, visual, or transaction ranges.

## Request-body guard

- The configured Responses endpoint has returned nginx HTTP 413 with active JSONL segments of about 8.9-10.6 MB, including about 6.1-6.9 MB of decoded image data. The nginx limit itself is unknown, so treat 4 MiB as a conservative per-context-segment image ceiling.
- Never output an entire file from `C:\Users\Lenovo\.codex\sessions` or `archived_sessions`. Use streaming counts, hashes, selected metadata, and summaries that exclude `data:image` payloads.
- Never batch images. One image result per tool call, and never use `detail: "original"` on a full rendered PDF page.
- Before visual inspection, run `python mcm-skill-work\scripts\make_review_proxy.py --input <png> --output <jpg> --max-bytes 450000`. Inspect the proxy with `detail: "high"`.
- For exact equations, plots, tables, or code, pass `--crop LEFT TOP RIGHT BOTTOM` to create a focused proxy from the original page. The original raster remains authoritative for coordinates and local pixel checks.
- After eight proxies, move further visual inspection to a fresh read-only subagent with `fork_turns: "none"`, or continue with text-only checks until compaction. Return only a concise textual audit to the root.
- Transport limits do not permit sampled review. Every physical page and every required formula/visual still needs the coverage required by `plan.md`.
