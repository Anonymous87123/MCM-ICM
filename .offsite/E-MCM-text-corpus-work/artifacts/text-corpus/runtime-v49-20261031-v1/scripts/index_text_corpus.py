"""Freeze a rebuildable SQLite index and a content-bound corpus catalog, create-only."""
from __future__ import annotations

import argparse
import json
import sqlite3
from collections import Counter
from pathlib import Path

from text_corpus import digest, encoded, exported_section_text, file_hash, json_new, read_json, write_new


def index(root: Path) -> dict:
    scope = read_json(root / "scope.json")
    if (root / "catalog.json").exists() or (root / "corpus.sqlite3").exists():
        raise ValueError("Index/catalog exists. Keep this generation; create another version to change it.")
    for key, name in (("builder", "build_text_corpus.py"), ("library", "text_corpus.py")):
        sha = scope.get("input_sha256", {}).get(key)
        if sha:
            snapshot = root / "inputs" / name
            source = Path(__file__).with_name(name)
            if snapshot.exists():
                if file_hash(snapshot) != sha:
                    raise ValueError("Frozen builder snapshot differs")
            elif file_hash(source) == sha:
                write_new(snapshot, source.read_bytes())
            else:
                raise ValueError("Builder changed before code snapshot; original code must be recovered")
    catalog = {"schema_version": 1, "scope_id": scope["scope_id"], "papers": [], "status": "draft"}
    totals = Counter(expected_papers=scope["paper_count"], expected_pages=scope["physical_page_count"])
    con = sqlite3.connect(root / "corpus.sqlite3")
    try:
        con.executescript("""
        CREATE TABLE papers(paper_id TEXT PRIMARY KEY, queue_position INTEGER UNIQUE,
            problem_type TEXT, year INTEGER, page_count INTEGER, document_sha256 TEXT, status TEXT);
        CREATE TABLE sections(paper_id TEXT, section_id TEXT, parent_id TEXT, title TEXT,
            role TEXT, boundary_status TEXT, text TEXT, text_sha256 TEXT,
            PRIMARY KEY(paper_id, section_id));
        CREATE INDEX section_roles ON sections(role, paper_id);
        CREATE VIRTUAL TABLE section_search USING fts5(paper_id UNINDEXED,section_id UNINDEXED,title,text);
        """)
        for record in scope["records"]:
            pid = record["paper_id"]; folder = root / "papers" / pid
            entry = {k: record[k] for k in ("paper_id", "queue_position", "problem_type", "year", "page_count")}
            entry.update(source_sha256=record["sha256"], document=None, document_sha256=None, files={})
            if (folder / "COMPLETE.json").is_file():
                complete = read_json(folder / "COMPLETE.json")
                if complete["scope_id"] != scope["scope_id"]:
                    raise ValueError(f"Scope binding differs: {pid}")
                for rel, sha in complete["files"].items():
                    if file_hash(folder / rel) != sha:
                        raise ValueError(f"Frozen paper file changed: {pid}/{rel}")
                    entry["files"][f"papers/{pid}/{rel}"] = sha
                entry["files"][f"papers/{pid}/COMPLETE.json"] = file_hash(folder / "COMPLETE.json")
                entry.update(document=f"papers/{pid}/document.json", document_sha256=file_hash(folder / "document.json"))
                doc = read_json(folder / "document.json")
                totals.update(extracted_papers=1, extracted_pages=doc["page_count"],
                              sections=len(doc["sections"]), blocks=len(doc["blocks"]), defects=len(doc["defects"]))
                for section in doc["sections"]:
                    text = exported_section_text(doc, section["section_id"])
                    con.execute("INSERT INTO sections VALUES(?,?,?,?,?,?,?,?)", (pid, section["section_id"],
                                section["parent_id"], section["title"], section["role"], section["boundary_status"],
                                text, digest(text.encode())))
                    con.execute("INSERT INTO section_search VALUES(?,?,?,?)", (pid, section["section_id"], section["title"], text))
            con.execute("INSERT INTO papers VALUES(?,?,?,?,?,?,?)", (pid, record["queue_position"], record["problem_type"],
                        record["year"], record["page_count"], entry["document_sha256"],
                        "machine-draft" if entry["document"] else "missing-extraction"))
            catalog["papers"].append(entry)
        con.commit()
        if con.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ValueError("SQLite integrity check failed")
    finally:
        con.close()
    catalog["sqlite_sha256"] = file_hash(root / "corpus.sqlite3")
    catalog["totals"] = dict(totals)
    catalog["dataset_id"] = digest(encoded(catalog))
    json_new(root / "catalog.json", catalog)
    return {"dataset_id": catalog["dataset_id"], **dict(totals), "status": "draft; source review pending"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(index(args.corpus_root.resolve()), ensure_ascii=False))
