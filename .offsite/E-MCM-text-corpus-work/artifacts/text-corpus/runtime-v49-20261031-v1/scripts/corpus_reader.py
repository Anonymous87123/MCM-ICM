"""Exhaustive, bounded chapter reading with append-only delivery/processing receipts.

No vector search, snippets, automatic acknowledgement, or legacy-card fallback.
The standard-library UTF-8 byte upper bound is deliberately conservative for tokens.
"""
from __future__ import annotations

import argparse
import json
import sys
import uuid
from pathlib import Path

from text_corpus import PROSE_KINDS, absence_review_valid, canonical_role, digest, encoded, file_hash, json_new, read_json, section_blocks, section_text, text_with_block_spans
from corpus_queries import QUERY_FAMILIES,TASK_QUERIES,select_sections,selected_blocks,all_author_blocks


def query_policy_hash():
    return file_hash(Path(__file__).with_name('corpus_queries.py'))


def check_session_policy(session):
    # Pre-existing runs retain their frozen selections/receipt bytes. Every new
    # run binds the query policy and cannot silently resume under another one.
    if session.get('query_policy_sha256') and session['query_policy_sha256'] != query_policy_hash():
        raise ValueError('Query policy changed; preserve this run and start a new version-bound run')


def wire(value) -> bytes:
    def dump(obj):
        return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if isinstance(value, dict) and "completion_marker" in value:
        body = {k: v for k, v in value.items() if k != "completion_marker"}
        # Deterministic hashes AND the required marker physically at the end.
        return dump(body)[:-1] + b',"completion_marker":' + dump(value["completion_marker"]) + b"}"
    return dump(value)


class Catalog:
    def __init__(self, root: Path):
        self.root = root.resolve()
        path = self.root / "catalog.json"
        if not path.is_file():
            raise ValueError("Corpus catalog missing. No fallback to language-unit fragments.")
        self.catalog = read_json(path)
        binding = dict(self.catalog)
        claimed = binding.pop("dataset_id")
        if digest(encoded(binding)) != claimed:
            raise ValueError("Catalog identity invalid")
        self.identity = claimed
        self.papers = self.catalog["papers"]
        if len({p["paper_id"] for p in self.papers}) != len(self.papers):
            raise ValueError("Duplicate paper in catalog")
        self.by_id = {p["paper_id"]: p for p in self.papers}

    def document(self, pid: str) -> dict:
        item = self.by_id[pid]
        if not item.get("document"):
            raise ValueError(f"No extracted document: {pid}")
        path = (self.root / item["document"]).resolve()
        if not path.is_relative_to(self.root):
            raise ValueError("Document outside corpus root")
        if file_hash(path) != item["document_sha256"]:
            raise ValueError(f"Document bytes changed; new corpus generation required: {pid}")
        doc = read_json(path)
        if doc["paper_id"] != pid or doc["source_sha256"] != item["source_sha256"]:
            raise ValueError("Document source identity differs from catalog")
        return doc

    def select(self, section: str, scope="all", year=None, title=False) -> list[dict]:
        role = canonical_role(section)
        if scope != "all" and scope not in set("ABCDEF"):
            raise ValueError("Scope must be all or exactly one problem letter")
        selected = []
        for paper in self.papers:
            if scope != "all" and paper["problem_type"] != scope:
                continue
            if year is not None and paper["year"] != year:
                continue
            item = {"paper_id": paper["paper_id"], "queue_position": paper["queue_position"],
                    "status": "unresolved", "section_ids": [], "text_sha256": digest(b""), "characters": 0}
            if paper.get("document"):
                doc = self.document(paper["paper_id"])
                ids,excluded=select_sections(doc,section,exact_title=title)
                item["section_ids"]=ids
                if excluded:
                    item["excluded_roles"]=sorted(excluded)
                blocks = selected_blocks(doc,item)
                text = text_with_block_spans(blocks)[0]
                item.update(section_ids=ids, text_sha256=digest(text.encode()), characters=len(text))
                if text:
                    wanted = {b["section_id"] for b in blocks}
                    verified = all(self.review_valid(doc, s) for s in doc["sections"] if s["section_id"] in wanted)
                    pages = {p for b in blocks for p in b["source_pages"]}
                    bids = {b["block_id"] for b in blocks}
                    open_defects = [d for d in doc.get("defects", []) if d.get("status") != "resolved" and
                                    (d.get("section_id") in wanted or d.get("page") in pages or
                                     d.get("block_id") in bids or d.get("left") in bids or d.get("right") in bids)]
                    # Legacy section reviews bind canonical author-text blocks;
                    # newly exposed bibliography/object bytes were not reviewed.
                    verified = verified and all(b["kind"] in PROSE_KINDS for b in blocks)
                    verified = verified and not open_defects and not any(b.get("issues") for b in blocks)
                    item["status"] = "verified" if verified else "present-unverified"
                elif not title and self.absence_valid(doc, role):
                    # Even an empty selection must carry portable, unchanged
                    # whole-document evidence. There is no metadata-only waiver.
                    self.check_absence_evidence(doc, role)
                    item["status"] = "verified-absent"
            selected.append(item)
        if not selected:
            raise ValueError("Requested paper set is empty")
        return selected

    @staticmethod
    def review_valid(doc, section):
        review = section.get("review", {})
        blocks = section_blocks(doc, [section["section_id"]])
        pages = {p for b in blocks for p in b["source_pages"]}
        paragraph_ids = [b["block_id"] for b in blocks if b["kind"] != "heading"]
        return bool(section["boundary_status"] == "verified" and review.get("reviewer") and
                    review.get("source_sha256") == doc["source_sha256"] and
                    review.get("raw_pages_sha256") == doc.get("raw_pages_sha256") and
                    review.get("text_sha256") == digest(section_text(doc, [section["section_id"]]).encode()) and
                    review.get("section_boundaries_checked") is True and
                    review.get("paragraph_boundaries_checked") is True and
                    ("paragraph_blocks" not in review or review["paragraph_blocks"] == paragraph_ids) and
                    pages <= set(review.get("checked_pages", [])))

    @staticmethod
    def absence_valid(doc, role):
        review = doc.get("absence_reviews", {}).get(role, {})
        return role in doc.get("verified_absent_roles", []) and absence_review_valid(doc, role, review)

    def check_absence_evidence(self, doc, role):
        review = doc.get("absence_reviews", {}).get(role, {})
        files = review.get("evidence_files", {})
        if not self.absence_valid(doc, role) or not files:
            raise ValueError("Missing whole-source absence evidence")
        for rel, sha in files.items():
            path = (self.root / rel).resolve()
            if Path(rel).is_absolute() or not path.is_relative_to(self.root) or not path.is_file() or file_hash(path) != sha:
                raise ValueError("Whole-source absence evidence missing or changed")
        if any(files.get(p["path"]) != p["sha256"] for p in review["evidence"]):
            raise ValueError("Absence review evidence is not in its frozen bundle")

    def text_and_spans(self, selection: dict) -> tuple[str, list[dict]]:
        doc = self.document(selection["paper_id"])
        blocks = selected_blocks(doc, selection)
        text, spans = text_with_block_spans(blocks)
        if digest(text.encode()) != selection["text_sha256"] or len(text) != selection["characters"]:
            raise ValueError("Selection no longer matches source bytes")
        return text, spans


def start(catalog: Catalog, section: str, run_dir: Path, *, scope="all", year=None,
          title=False, allow_unverified=False, max_tokens=6000, max_bytes=32768) -> dict:
    if max_tokens < 1000 or max_bytes < 1000 or max_tokens > 6000 or max_bytes > 32768:
        raise ValueError("Budgets must be 1000..6000 tokens and 1000..32768 bytes")
    policy = query_policy_hash()
    scope_path = catalog.root/'scope.json'
    declared = read_json(scope_path).get('input_sha256',{}).get('queries') if scope_path.is_file() else None
    policy_changed = bool(declared and declared != policy)
    if policy_changed and not allow_unverified:
        raise ValueError('Query policy changed; build a new immutable generation before strict reading')
    selection = catalog.select(section, scope, year, title)
    unresolved = [x["paper_id"] for x in selection if x["status"] not in {"verified", "verified-absent"}]
    if unresolved and not allow_unverified:
        raise ValueError(f"Strict reading blocked: {len(unresolved)}/{len(selection)} papers unresolved. "
                         "Use --allow-unverified only for explicitly labelled draft reading; no full-completion claim.")
    run_dir = run_dir.resolve()
    if run_dir.exists():
        raise ValueError("Run directory already exists; resume it instead of overwriting")
    session = {"schema_version": 1, "run_id": uuid.uuid4().hex, "dataset_id": catalog.identity,
               "query_policy_sha256": policy,
               "query_policy_status": 'unfrozen-policy-preview' if policy_changed else 'frozen-policy',
               "query": {"section": section, "scope": scope, "year": year, "title": title, "mode": "exhaustive"},
               "allow_unverified": allow_unverified, "max_tokens": max_tokens, "max_bytes": max_bytes,
               "token_budget_method": "utf8-byte-upper-bound (not an actual model token count)",
               "selection": selection}
    json_new(run_dir / "session.json", session)
    return {"run_dir": str(run_dir), "run_id": session["run_id"], "target_papers": len(selection),
            "unresolved": len(unresolved), "preview": allow_unverified, "next": "next --run-dir <run_dir>"}


def state(catalog: Catalog, run_dir: Path):
    session = read_json(run_dir / "session.json")
    if session["dataset_id"] != catalog.identity:
        raise ValueError("Corpus version changed; old cursor cannot be reused")
    check_session_policy(session)
    cursor = {"paper_index": 0, "char_offset": 0}; prev = digest(encoded(session)); receipts = []
    paths = sorted((run_dir / "receipts").glob("*.json"))
    for number, path in enumerate(paths):
        if path.name != f"{number:06d}.json":
            raise ValueError("Receipt sequence has gaps")
        receipt = read_json(path)
        if receipt["previous_sha256"] != prev or receipt["from_cursor"] != cursor:
            raise ValueError("Receipt chain/cursor invalid")
        batch_path = run_dir / "batches" / path.name
        batch = read_json(batch_path)
        marker = batch.pop("completion_marker")
        if digest(wire(batch)) != marker or receipt["batch_id"] != marker:
            raise ValueError("Acknowledged batch modified")
        if receipt["to_cursor"] != batch["to_cursor"] or batch["from_cursor"] != cursor:
            raise ValueError("Receipt does not describe its delivered batch")
        cursor = receipt["to_cursor"]; prev = file_hash(path); receipts.append(receipt)
    return session, cursor, receipts, prev


def check_pending_batch(catalog, session, cursor, path):
    batch = read_json(path)
    base = dict(batch); marker = base.pop("completion_marker")
    if (digest(wire(base)) != marker or batch["from_cursor"] != cursor or
            batch["run_id"] != session["run_id"] or batch["dataset_id"] != catalog.identity):
        raise ValueError("Pending batch altered")
    for chunk in batch["chunks"]:
        item = session["selection"][chunk["paper_index"]]
        if item["paper_id"] != chunk["paper_id"]:
            raise ValueError("Pending batch paper differs")
        doc = catalog.document(item["paper_id"])
        if item["status"] == "verified-absent":
            catalog.check_absence_evidence(doc,canonical_role(session["query"]["section"]))
        text, _ = catalog.text_and_spans(item)
        if text[chunk["start"]:chunk["end"]] != chunk["text"]:
            raise ValueError("Pending batch source changed")
    return batch


def build_batch(catalog: Catalog, session: dict, cursor: dict, number: int) -> dict:
    """Pure batch construction: no delivery file, cursor write or AI receipt.

    Production delivery and transport-only reconstruction use this same path.
    Constructing bytes is never an assertion that an agent has read them.
    """
    if session['dataset_id'] != catalog.identity:
        raise ValueError('Corpus version changed; old cursor cannot be reused')
    check_session_policy(session)
    if (not 1000 <= session['max_tokens'] <= 6000 or
            not 1000 <= session['max_bytes'] <= 32768):
        raise ValueError('Invalid batch budget')
    if type(number) is not int or number < 0:
        raise ValueError('Invalid batch sequence')
    selections = session["selection"]
    index, offset = cursor.get('paper_index'), cursor.get('char_offset')
    if (type(index) is not int or type(offset) is not int or not 0 <= index <= len(selections) or
            offset < 0 or (index == len(selections) and offset != 0) or
            (index < len(selections) and offset > max(0, selections[index]['characters'] - 1))):
        raise ValueError('Cursor outside selected text')
    batch = {"run_id": session["run_id"], "dataset_id": catalog.identity, "sequence": number,
             "preview": session["allow_unverified"], "from_cursor": dict(cursor),
             "chunks": [], "to_cursor": dict(cursor), "finished": False}
    # Reserve exact transport envelope and the end-marker before fitting text.
    def fits(candidate):
        value = dict(candidate, completion_marker="0" * 64)
        size = len(wire(value))
        return size + 1 <= min(session["max_bytes"], session["max_tokens"])

    while batch["to_cursor"]["paper_index"] < len(selections):
        position = batch["to_cursor"]["paper_index"]
        offset = batch["to_cursor"]["char_offset"]
        item = selections[position]
        if not item["characters"]:
            doc = catalog.document(item["paper_id"])  # Empty records are source-bound too.
            if item["status"] == "verified-absent":
                catalog.check_absence_evidence(doc,canonical_role(session["query"]["section"]))
        text, spans = catalog.text_and_spans(item) if item["characters"] else ("", [])

        def candidate(end):
            piece = {"paper_id": item["paper_id"], "paper_index": position,
                     "status": item["status"], "start": offset, "end": end,
                     "total_characters": len(text), "whole_text_sha256": item["text_sha256"],
                     "text": text[offset:end],
                     "source_blocks": [s for s in spans if s["end"] > offset and s["start"] < end]}
            cursor2 = {"paper_index": position+1, "char_offset": 0} if end == len(text) else {
                "paper_index": position, "char_offset": end}
            return dict(batch, chunks=batch["chunks"] + [piece], to_cursor=cursor2,
                        finished=cursor2["paper_index"] == len(selections))

        if fits(candidate(len(text))):
            batch = candidate(len(text)); continue
        if batch["chunks"]:
            break  # Keep whole sections together whenever they fit an empty batch.
        low, high = offset, len(text)
        while low < high:
            mid = (low + high + 1) // 2
            if fits(candidate(mid)):
                low = mid
            else:
                high = mid - 1
        if low <= offset:
            raise ValueError("Budget too small for metadata and text; increase within safe limits")
        split = text.rfind("\n\n", offset, low)
        if split > offset + (low-offset)//3:
            low = split + 2  # Preserve separators byte-for-byte in reconstruction.
        else:
            # Long paragraphs may continue at a sentence/word boundary, never truncate.
            split = text.rfind(" ", offset, low)
            if split > offset:
                low = split + 1
        batch = candidate(low); break
    if not batch["chunks"]:
        return {"finished": True, "run_id": session["run_id"], "message": "All batches already processed; inspect status."}
    batch["completion_marker"] = digest(wire(batch))
    if len(wire(batch)) + 1 > min(session["max_bytes"], session["max_tokens"]):
        raise ValueError("Internal payload budget invariant failed")
    return batch


def next_batch(catalog: Catalog, run_dir: Path) -> dict:
    session, cursor, receipts, _ = state(catalog, run_dir)
    number = len(receipts); target = run_dir / "batches" / f"{number:06d}.json"
    if target.exists():
        return check_pending_batch(catalog, session, cursor, target)
    batch = build_batch(catalog, session, cursor, number)
    if batch.get('chunks'):
        json_new(target, batch)
    return batch


def acknowledge(catalog: Catalog, run_dir: Path, marker: str, observations: list[dict]) -> dict:
    session, cursor, receipts, previous = state(catalog, run_dir)
    target = run_dir / "batches" / f"{len(receipts):06d}.json"
    if not target.is_file():
        raise ValueError("No delivered pending batch")
    batch = check_pending_batch(catalog, session, cursor, target)
    base = dict(batch); actual = base.pop("completion_marker")
    if marker != actual or digest(wire(base)) != actual:
        raise ValueError("Wrong completion marker; truncated/unseen output cannot be acknowledged")
    expected = {c["paper_id"] for c in batch["chunks"]}
    supplied = {o.get("paper_id") for o in observations}
    if supplied != expected or len(supplied) != len(observations):
        raise ValueError("Provide exactly one observation for EVERY paper in this batch")
    for observation in observations:
        if not isinstance(observation.get("observation"), str) or not observation["observation"].strip():
            raise ValueError("Empty observation is not an AI-processing receipt")
        chunks = [c for c in batch["chunks"] if c["paper_id"] == observation["paper_id"]]
        allowed = {s["block_id"] for c in chunks for s in c["source_blocks"]}
        cited = set(observation.get("block_ids", []))
        if allowed and (not cited or not cited <= allowed):
            raise ValueError("Observations must cite source block IDs actually delivered")
        for c in chunks:
            if c["text"]:
                text, _ = catalog.text_and_spans(session["selection"][c["paper_index"]])
                if text[c["start"]:c["end"]] != c["text"]:
                    raise ValueError("Delivered text no longer matches corpus")
    receipt = {"run_id": session["run_id"], "batch_id": marker, "previous_sha256": previous,
               "from_cursor": cursor, "to_cursor": batch["to_cursor"], "observations": observations,
               "meaning": "agent asserted processing of delivered text; not proof of understanding"}
    json_new(run_dir / "receipts" / f"{len(receipts):06d}.json", receipt)
    return status(catalog, run_dir)


def status(catalog: Catalog, run_dir: Path) -> dict:
    session, cursor, receipts, _ = state(catalog, run_dir)
    selection = session["selection"]
    completed = selection[:cursor["paper_index"]]
    # Previously processed bytes must still bind this generation. In particular,
    # a completed run must not keep claiming acceptance after source mutation.
    for item in completed:
        doc = catalog.document(item["paper_id"])
        if item["status"] == "verified-absent":
            catalog.check_absence_evidence(doc,canonical_role(session["query"]["section"]))
    pending = run_dir / "batches" / f"{len(receipts):06d}.json"
    delivered_cursor = check_pending_batch(catalog, session, cursor, pending)["to_cursor"] if pending.exists() else cursor
    delivered = selection[:delivered_cursor["paper_index"]]
    unresolved = sum(s["status"] not in {"verified", "verified-absent"} for s in selection)
    return {"run_id": session["run_id"], "dataset_id": catalog.identity, "target_papers": len(selection),
            "query_policy_status":session.get('query_policy_status','legacy-frozen-selection'),
            "parts_present": sum(s["characters"] > 0 for s in selection),
            "verified_absent": sum(s["status"] == "verified-absent" for s in selection),
            "unresolved": unresolved, "fully_processed_present": sum(s["characters"] > 0 for s in completed),
            "fully_delivered_present": sum(s["characters"] > 0 for s in delivered),
            "delivered_cursor": delivered_cursor,
            "partially_delivered_current_paper": delivered_cursor["char_offset"] > 0,
            "source_verified_and_processed": sum(s["status"] == "verified" for s in completed),
            "papers_accounted_for": cursor["paper_index"], "cursor": cursor,
            "batches_acknowledged": len(receipts), "pending_batch_delivered": pending.exists(),
            "traversal_complete": cursor["paper_index"] == len(selection),
            "full_read_acceptance": cursor["paper_index"] == len(selection) and unresolved == 0 and
                session.get('query_policy_status') != 'unfrozen-policy-preview',
            "preview": session["allow_unverified"]}


def author_text_coverage(catalog: Catalog, run_dirs: list[Path]) -> dict:
    """Union actual acknowledged source-block character intervals across runs.

    Different chapter queries may overlap. An abstract receipt cannot cover a
    body block; pending delivery cannot cover anything. All runs bind one dataset.
    """
    intervals={};runs=[]
    for run_dir in run_dirs:
        session,cursor,receipts,_=state(catalog,run_dir)
        runs.append({"run_id":session["run_id"],"query":session["query"],"cursor":cursor,
                     "query_policy_status":session.get('query_policy_status','legacy-frozen-selection'),
                     "batches_acknowledged":len(receipts)})
        for number in range(len(receipts)):
            path=run_dir/"batches"/f"{number:06d}.json"
            saved=read_json(path)
            batch=check_pending_batch(catalog,session,saved["from_cursor"],path)
            for chunk in batch["chunks"]:
                item=session["selection"][chunk["paper_index"]]
                _,spans=catalog.text_and_spans(item)
                for span in spans:
                    left=max(span["start"],chunk["start"]);right=min(span["end"],chunk["end"])
                    if right>left:
                        intervals.setdefault((item["paper_id"],span["block_id"]),[]).append(
                            (left-span["start"],right-span["start"]))
    def covered(pid,block):
        ranges=sorted(intervals.get((pid,block["block_id"]),[]));end=0
        for left,right in ranges:
            if left>end:
                return False
            end=max(end,right)
        return bool(ranges) and end==len(block["text"])
    source_status={s["paper_id"]:s["status"] for s in catalog.select("all_author_text")}
    papers=[];total_blocks=processed_blocks=total_sections=processed_sections=complete=verified=0
    for paper in catalog.papers:
        doc=catalog.document(paper["paper_id"]);blocks=all_author_blocks(doc)
        done={b["block_id"] for b in blocks if covered(paper["paper_id"],b)}
        ids,excluded=select_sections(doc,"all_author_text");sections=[]
        for section in doc["sections"]:
            if section["section_id"] not in ids:
                continue
            part=section_blocks(doc,[section["section_id"]],excluded_roles=excluded)
            if not part:
                continue
            all_read=all(b["block_id"] in done for b in part)
            sections.append({"section_id":section["section_id"],"title":section["title"],
                "role":section["role"],"required_blocks":len(part),
                "processed_blocks":sum(b["block_id"] in done for b in part),
                "all_selected_text_processed":all_read,"source_boundary_status":section["boundary_status"]})
        all_read=bool(blocks) and len(done)==len(blocks)
        accepted=all_read and source_status[paper["paper_id"]]=="verified"
        papers.append({"paper_id":paper["paper_id"],"queue_position":paper["queue_position"],
            "required_blocks":len(blocks),"fully_processed_blocks":len(done),
            "all_author_text_processed":all_read,"source_verified_and_processed":accepted,"sections":sections})
        total_blocks+=len(blocks);processed_blocks+=len(done);complete+=all_read;verified+=accepted
        total_sections+=len(sections);processed_sections+=sum(s["all_selected_text_processed"] for s in sections)
    return {"dataset_id":catalog.identity,"runs":runs,"target_papers":len(catalog.papers),
        "all_author_text_processed_papers":complete,"source_verified_and_processed_papers":verified,
        "required_unique_blocks":total_blocks,"fully_processed_unique_blocks":processed_blocks,
        "required_candidate_sections":total_sections,"fully_processed_candidate_sections":processed_sections,
        "all_chapters_read_acceptance":verified==len(catalog.papers) and
            all(r['query_policy_status']!='unfrozen-policy-preview' for r in runs),"papers":papers,
        "meaning":"Union of acknowledged source-block character coverage; counts are processing assertions, not proof of understanding. Source fidelity remains separate."}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--corpus-root", type=Path, default=Path(__file__).resolve().parents[1] / "assets/text-corpus")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("sections")
    sub.add_parser("queries")
    coverage_parser=sub.add_parser("coverage")
    coverage_parser.add_argument("--run-dir",type=Path,action="append",required=True)
    coverage_parser.add_argument("--report",type=Path)
    a = sub.add_parser("start")
    a.add_argument("--section", required=True); a.add_argument("--scope", default="all")
    a.add_argument("--year", type=int); a.add_argument("--title", action="store_true")
    a.add_argument("--mode", choices=["exhaustive"], default="exhaustive")
    a.add_argument("--allow-unverified", action="store_true")
    a.add_argument("--max-tokens", type=int, default=6000); a.add_argument("--max-bytes", type=int, default=32768)
    a.add_argument("--run-dir", type=Path, required=True)
    for name in ("next", "status", "resume", "ack"):
        a = sub.add_parser(name); a.add_argument("--run-dir", type=Path, required=True)
        if name == "ack":
            a.add_argument("--completion-marker", required=True); a.add_argument("--observations", type=Path, required=True)
    args = p.parse_args(argv); catalog = Catalog(args.corpus_root)
    if args.command == "queries":
        result={"roles":"sections lists the source's candidate roles",
            "complete_queries":{name:sorted(roles) if roles else "all author sections, excluding Contents/References/AI disclosure" for name,roles in QUERY_FAMILIES.items()},
            "task_queries":TASK_QUERIES,"task_mapping":"Explicit Task/Problem/Question titles only; chapter numbers are never task IDs. Unmapped parts remain unresolved.",
            "exact_printed_heading":"start --section TITLE --title"}
    elif args.command == "coverage":
        result=author_text_coverage(catalog,args.run_dir)
        if args.report:
            json_new(args.report,result)
        result={k:v for k,v in result.items() if k!="papers"}
        if args.report:
            result["report"]=str(args.report)
    elif args.command == "sections":
        counts = {}; empty = {}
        for paper in catalog.papers:
            if paper.get("document"):
                doc = catalog.document(paper["paper_id"])
                for role in {s["role"] for s in doc["sections"]}:
                    ids = [s["section_id"] for s in doc["sections"] if s["role"] == role]
                    target = counts if section_text(doc, ids).strip() else empty
                    target[role] = target.get(role, 0)+1
        result = {"dataset_id": catalog.identity, "expected_papers": len(catalog.papers), "candidate_role_papers": counts,
                  "empty_candidate_role_papers": empty,
                  "note": "Candidate presence is not boundary verification; use --title for an exact original heading."}
    elif args.command == "start":
        result = start(catalog, args.section, args.run_dir, scope=args.scope, year=args.year, title=args.title,
                       allow_unverified=args.allow_unverified, max_tokens=args.max_tokens, max_bytes=args.max_bytes)
    elif args.command in {"next", "resume"}:
        result = next_batch(catalog, args.run_dir)
    elif args.command == "status":
        result = status(catalog, args.run_dir)
    else:
        result = acknowledge(catalog, args.run_dir, args.completion_marker, read_json(args.observations))
    # Compact wire format has the same byte size the batching code measured.
    sys.stdout.buffer.write(wire(result) + b"\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
