"""Full-queue chapter-mapping repair inventory; unknown never means absent.

Every paper keeps its complete stored heading map, including unclassified/custom
titles. This does not invent task IDs from chapter numbers or approve boundaries.
"""
import argparse
from collections import Counter
from pathlib import Path

from corpus_reader import Catalog, query_policy_hash
from corpus_queries import task_numbers
from text_corpus import PROSE_KINDS, file_hash, json_new
from verify_reader_transport import DEFAULT_QUERIES


def audit(root, queries=DEFAULT_QUERIES):
    catalog = Catalog(root)
    query_rows = {query: catalog.select(query) for query in queries}
    expected = [p['paper_id'] for p in catalog.papers]
    if any([r['paper_id'] for r in rows] != expected for rows in query_rows.values()):
        raise ValueError('A mapping inventory must not filter out an unmapped paper')
    by_query = {query: {r['paper_id']: r for r in rows} for query, rows in query_rows.items()}
    papers = []
    totals = Counter()
    for record in catalog.papers:
        doc = catalog.document(record['paper_id'])
        owned = {}
        for block in doc['blocks']:
            owned.setdefault(block['section_id'], []).append(block)
        chapters = []
        for section in doc['sections']:
            blocks = owned.get(section['section_id'], [])
            chapters.append({'section_id': section['section_id'], 'parent_id': section['parent_id'],
                'printed_title_or_candidate_label': section['title'], 'stored_role': section['role'],
                'origin': section.get('origin', 'unspecified'), 'boundary_status': section['boundary_status'],
                'physical_pages': sorted({p for b in blocks for p in b['source_pages']}),
                'owned_blocks': len(blocks),
                'owned_candidate_prose_characters': sum(len(b['text']) for b in blocks if b['kind'] in PROSE_KINDS),
                'source_heading_line_ids': [lid for b in blocks if b['kind'] == 'heading'
                    for lid in b.get('source_line_ids', [])],
                'explicit_printed_task_numbers': sorted(task_numbers(section['title']))})
        missing = [query for query in queries if by_query[query][doc['paper_id']]['status'] == 'unresolved']
        absences = [query for query in queries if by_query[query][doc['paper_id']]['status'] == 'verified-absent']
        uncertain = [query for query in queries if by_query[query][doc['paper_id']]['status'] == 'present-unverified']
        papers.append({'paper_id': doc['paper_id'], 'queue_position': record['queue_position'],
            'document_sha256': record['document_sha256'], 'source_sha256': doc['source_sha256'],
            'empty_unresolved_queries': missing, 'source_local_verified_absent_queries': absences,
            'nonempty_source_unverified_queries': uncertain, 'complete_stored_chapter_map': chapters,
            'next_action': 'Read source prose/boundaries and bind every relevant chapter or genuine source-local absence. Do not infer task identity from numeric chapter order or substitute a few matching samples.'})
        totals.update(papers_checked=1, candidate_sections=len(chapters),
            papers_with_empty_unresolved_queries=bool(missing), empty_unresolved_paper_query_pairs=len(missing))
    counts = {query: dict(Counter(r['status'] for r in rows)) for query, rows in query_rows.items()}
    return {'dataset_id': catalog.identity, 'query_policy_sha256':query_policy_hash(),
        'totals': dict(totals), 'query_status_counts': counts,
        'papers': papers, 'auditor_sha256': file_hash(Path(__file__)),
        'meaning': 'All query targets remain in scope. Empty-unresolved means mapping/content is not yet established, NOT that a paper lacks the requested part. Nonempty text also remains subject to fidelity review.',
        'source_fidelity_approved': False, 'ai_reading_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus-root', type=Path, required=True)
    parser.add_argument('--query', action='append')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise ValueError('Create-only mapping report exists; preserve it')
    result = audit(args.corpus_root.resolve(), args.query or DEFAULT_QUERIES)
    json_new(args.report, result)
    print({k: v for k, v in result.items() if k != 'papers'}, flush=True)
