"""Find nested bibliography/contents/disclosure blocks returned by prose queries."""
import argparse
from collections import Counter
from pathlib import Path

from corpus_queries import EXCLUDED_AUTHOR_ROLES, select_sections, selected_blocks
from corpus_reader import Catalog,query_policy_hash
from text_corpus import file_hash, json_new
from verify_reader_transport import DEFAULT_QUERIES


def findings(document, queries=DEFAULT_QUERIES):
    sections = {s['section_id']:s for s in document['sections']}
    output = []
    for query in queries:
        ids,excluded = select_sections(document,query)
        blocks = selected_blocks(document,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        leaking = []
        for block in blocks:
            sid = block['section_id']
            seen = set()
            while sid:
                if sid in seen or sid not in sections:
                    raise ValueError('Invalid source hierarchy in query audit')
                seen.add(sid)
                section = sections[sid]
                if section['role'] in EXCLUDED_AUTHOR_ROLES:
                    leaking.append({'block_id':block['block_id'],'physical_pages':block['source_pages'],
                        'owner_section_id':block['section_id'],'excluded_ancestor_id':sid,
                        'excluded_role':section['role']})
                    break
                sid = section['parent_id']
        if leaking:
            output.append({'query':query,'selection_section_ids':ids,'leaked_blocks':leaking})
    return output


def audit(root):
    catalog = Catalog(root)
    totals = Counter()
    papers = []
    for record in catalog.papers:
        doc = catalog.document(record['paper_id'])
        found = findings(doc)
        totals.update(papers_checked=1,physical_pages=doc['page_count'],papers_with_query_leakage=bool(found),
            affected_paper_query_pairs=len(found),unique_leaking_blocks=len({b['block_id'] for f in found for b in f['leaked_blocks']}))
        if found:
            papers.append({'paper_id':doc['paper_id'],'queue_position':record['queue_position'],
                'document_sha256':record['document_sha256'],'queries':found})
    return {'dataset_id':catalog.identity,'query_policy_sha256':query_policy_hash(),
        'totals':dict(totals),'papers':papers,
        'auditor_sha256':file_hash(Path(__file__)),'source_fidelity_approved':False,
        'meaning':'These named prose queries currently return blocks inside explicitly non-author subtrees. Preserve raw content separately; do not equate transport reconstruction with correct author-prose selection.',
        'formula_verification':'paused','figure_distillation':'paused'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus-root',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise ValueError('Create-only query-subtree report exists; preserve it')
    result = audit(args.corpus_root.resolve())
    json_new(args.report,result)
    print({k:v for k,v in result.items() if k!='papers'},flush=True)
