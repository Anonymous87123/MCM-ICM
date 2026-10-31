"""Locate every malformed prose glyph without guessing that it is only a formula.

This inventory preserves mixed author explanation and source locations. It never
repairs, reclassifies or approves text; symbols/figures remain outside the audit.
"""
import argparse
from collections import Counter
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import bad_unicode, file_hash, json_new, rows


def glyph_contexts(text):
    return [{'offset': i, 'codepoint': f'U+{ord(c):04X}',
             'context': text[max(0, i - 48):min(len(text), i + 49)]}
            for i, c in enumerate(text) if bad_unicode(c)]


def audit(root):
    catalog = Catalog(root)
    papers = []
    totals = Counter()
    for record in catalog.papers:
        doc = catalog.document(record['paper_id'])
        affected = [b for b in doc['blocks'] if bad_unicode(b['text'])]
        totals.update(papers_checked=1, physical_pages=doc['page_count'])
        if not affected:
            continue
        raw = rows(root / 'papers' / doc['paper_id'] / 'raw/pages.jsonl')
        byid = {line['line_id']: line for page in raw for line in page['lines']}
        blocks = []
        for block in affected:
            lines = [byid[lid] for lid in block['source_line_ids'] if bad_unicode(byid[lid]['text'])]
            blocks.append({'block_id': block['block_id'], 'kind': block['kind'],
                'section_id': block['section_id'], 'source_pages': block['source_pages'],
                'source_line_ids': block['source_line_ids'], 'block_contexts': glyph_contexts(block['text']),
                'affected_native_lines': [{'line_id': line['line_id'], 'page': line['page'],
                    'bbox': line['bbox'], 'contexts': glyph_contexts(line['text'])} for line in lines],
                'disposition': 'Pending literal source/prose recovery. Do not discard surrounding explanation, infer a missing symbol, or treat display proximity as an exemption.'})
        physical_pages = sorted({p for b in affected for p in b['source_pages']})
        totals.update(papers_with_malformed_text=1, affected_blocks=len(blocks),
            affected_paper_pages=len(physical_pages),
            malformed_codepoints=sum(len(b['block_contexts']) for b in blocks))
        papers.append({'paper_id': doc['paper_id'], 'queue_position': record['queue_position'],
            'source_sha256': doc['source_sha256'], 'raw_pages_sha256': doc['raw_pages_sha256'],
            'document_sha256': record['document_sha256'], 'physical_pages': physical_pages, 'blocks': blocks})
    return {'dataset_id': catalog.identity, 'totals': dict(totals), 'papers': papers,
        'auditor_sha256': file_hash(Path(__file__)), 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus-root', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise ValueError('Create-only report exists; preserve it')
    result = audit(args.corpus_root.resolve())
    json_new(args.report, result)
    print({k: v for k, v in result.items() if k != 'papers'}, flush=True)
