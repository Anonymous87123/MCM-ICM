"""Serialize the root's explicitly reviewed q174 paragraph/side-lane map, create-only.

This is one source-bound layout correction, not an automatic reading receipt.
It asserts only the page/paragraph boundaries actually read and inspected.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import digest,file_hash,json_new,read_json,rows


def stage(root: Path,output: Path):
    pid="P-C-2012-14531-6018365f";catalog=Catalog(root);doc=catalog.document(pid)
    if (doc["source_sha256"] != "6018365f4456b37f2608d0c147748b8d16c8133c583091697e0e16041a894c66" or
            doc["raw_pages_sha256"] != "5c06833474723f11d6d41044b75945f0143c9bc02e7eec1d4e324c626109d15d"):
        raise ValueError("Reviewed source/raw page preimage differs")
    page=rows(root/"papers"/pid/"raw/pages.jsonl")[0]
    originals={x["line_id"]:x for x in page["lines"]}
    def ids(block,start=0,end=1):
        return [f"p0001-n{block:04d}-l{i:04d}" for i in range(start,end)]
    groups=[]
    def add(name,kind,lines,reason):
        groups.append({"group_id":name,"kind":kind,"source_line_ids":lines,
                       "text_sha256":digest(" ".join(originals[lid]["text"].strip() for lid in lines).encode()),
                       "reason":reason})
    meta=[x["line_id"] for x in page["lines"] if x["text"].strip() and x["native_block"]<22]
    add("official-form","front_matter",meta,"Printed form fields and instructions precede the author title; not author prose.")
    add("paper-title","title",ids(22,0,2),"Two-line paper title sits above the prose/sidebar area, not a model heading.")
    add("problem-clarification","prose",ids(23,1,7),"Right-lane Problem Clarification lead-in and its complete continuous paragraph.")
    add("assumptions","prose",ids(23,7,14),"Right-lane Assumptions lead-in and all five inline numbered assumptions; no sidebar labels inserted.")
    add("model-design","prose",ids(23,14,23),"Right-lane Model Design and Justification lead-in with its full paragraph.")
    add("results","prose",ids(23,23,30),"Right-lane Results and Sensitivity Analysis lead-in and all inline reported findings; no formula checking.")
    add("weakness-lead-in","heading",ids(23,30,31),"Standalone printed Strengths and Weaknesses Discussion lead-in, retained within summary scope.")
    add("strengths","prose",ids(24,0,4),"First indented paragraph under the strengths/weaknesses lead-in.")
    add("weaknesses","prose",ids(25,0,3),"Second indented paragraph starts However; its author grammar is preserved literally.")
    add("key-concepts","author_callout",ids(23,0,1)+sum((ids(b) for b in (27,29,31,33,35,36,37)),[]),
        "Author KEY CONCEPT sidebar and all six entries, retained as an independent callout after continuous main prose.")
    add("key-techniques","author_callout",sum((ids(b) for b in (39,41,43,45,46)),[]),
        "Author KEY TECHNIQUES sidebar and all three entries; the last entry wraps onto transmission.")
    evidence=root.parent/"source-reviews/q174-abstract-page1-20261029-v1"
    manifest=read_json(evidence/"manifest.json")
    if manifest["source_sha256"] != doc["source_sha256"] or manifest["raw_pages_sha256"] != doc["raw_pages_sha256"]:
        raise ValueError("Viewed source evidence differs")
    result={"schema":"source-text-layout-review-v1","paper_id":pid,"source_sha256":doc["source_sha256"],
            "raw_pages_sha256":doc["raw_pages_sha256"],"reviewer":"Codex root; full native page and bounded page proxy actually read",
            "reason":"The narrow left author sidebar was vertically interleaved inside right-lane sentences. Preserve metadata and title separately, then all main paragraphs continuously, then both labelled author callouts. No author sentence is rewritten and no line is dropped.",
            "paragraph_boundaries_checked":True,"reading_lanes_checked":True,
            "pages":[{"page":1,"groups":groups}],
            "evidence":[{"path":str((evidence/"manifest.json").resolve()),"sha256":file_hash(evidence/"manifest.json"),
                         "bundle_root":str(evidence.resolve()),
                         "description":"The actually inspected 408640byte page1 proxy and its original local raster/source bindings."}],
            "formula_verification":"paused","figure_distillation":"paused"}
    json_new(output,result)
    return {"paper_id":pid,"groups":len(groups),"author_callouts":2,"status":"staged, not a whole-section verification"}


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--corpus-root",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True);a=p.parse_args();print(stage(a.corpus_root.resolve(),a.output.resolve()))
