"""Freeze source-checked prose/caption separation on q165 pages9/10."""
from pathlib import Path

from corpus_reader import Catalog
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from text_corpus import digest, file_hash, json_new, make_document, rows, title_role


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261030-v12'
    doc = Catalog(root).document('P-C-2011-10607-6ed4fd93')
    output = base / 'reviews/20261030/q165-pages9-10-prose-boundaries-v1.json'
    if output.exists():
        raise ValueError('Create-only source proof exists; inspect, never overwrite')
    pages = rows(root / 'papers' / doc['paper_id'] / 'raw/pages.jsonl')
    selected = []

    def add(number, specification):
        page = pages[number - 1]
        byid = {line['line_id']: line for line in page['lines']}

        def ids(block, *indexes):
            return [line['line_id'] for line in page['lines']
                if line['native_block'] == block and line['text'].strip()
                and (not indexes or int(line['line_id'].rsplit('l', 1)[1]) in indexes)]

        groups = []
        for name, kind, pieces, level in specification(ids):
            members = [lid for piece in pieces for lid in piece]
            text = ' '.join(byid[lid]['text'].strip() for lid in members)
            group = {'group_id': f'p{number:04d}-{name}', 'kind': kind,
                'source_line_ids': members, 'text_sha256': digest(text.encode()),
                'reason': 'Actual source layout distinguishes centered object captions from indented author paragraphs; every active line retained once.'}
            if level is not None:
                group['opens_section'] = {'role': title_role(text, number), 'level': level}
            groups.append(group)
        selected.append({'page': number, 'groups': groups})

    add(9, lambda i: [
        ('header', 'furniture', [i(0)], None),
        ('power-station-attribution', 'prose', [i(1)], None),
        ('comparison-categories', 'prose', [i(2)], None),
        ('setup-handoff', 'prose', [i(3)], None),
        ('results-heading', 'heading', [i(4)], 4),
        ('object2-caption', 'caption', [i(5)], None),
        ('object2-author-discussion', 'prose', [i(6)], None),
        ('object3-caption', 'caption', [i(7)], None),
        ('object3-author-discussion', 'prose', [i(8)], None)])
    add(10, lambda i: [
        ('header', 'furniture', [i(0)], None),
        ('object4-caption', 'caption', [i(1, 1)], None),
        ('object4-author-discussion', 'prose', [i(1, 2, 3, 4, 5)], None),
        ('scope-limitation', 'prose', [i(2, 0, 1)], None),
        ('evaluation-heading', 'heading', [i(2, 2)], 3),
        ('strengths-heading', 'heading', [i(2, 3)], 4),
        ('strength1', 'list', [i(3), i(4, 0, 1)], None),
        ('strength2', 'list', [i(4, 2), i(5, 0)], None),
        ('weaknesses-heading', 'heading', [i(5, 1)], 4),
        ('weakness1', 'list', [i(6), i(7, 0)], None),
        ('weakness2', 'list', [i(7, 1), i(8)], None),
        ('prediction-heading', 'heading', [i(9)], 3),
        ('data-introduction-complete', 'prose', [i(10)], None),
        ('table5-source-object', 'source_object', [i(n) for n in range(11, 15)], None),
        ('table5-caption-and-source', 'caption', [i(15)], None),
        ('scenario-purpose', 'prose', [i(16)], None),
        ('table6-source-object', 'source_object', [i(17, *range(1, 12))], None),
        ('table6-caption', 'caption', [i(17, 12)], None)])
    folder = base / 'source-reviews/q165-whole-source-20261030-v1'
    findings = base / 'reviews/20261030/q165-whole-source-layout-findings-v1.json'
    review = {'schema': 'source-text-layout-review-v1',
        **{k: doc[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')},
        'reviewer': 'Codex root;2026-10-30;overviews02/03 actually inspected with all native lines on pages9/10',
        'reason': 'Restore Figure2/3/4 author paragraphs and the complete Table5 reference sentence; separate source-table cells/attribution from default prose without interpreting their values.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True, 'pages': selected,
        'evidence': [
            {'path': str(folder / 'manifest.json'), 'bundle_root': str(folder),
             'sha256': file_hash(folder / 'manifest.json'),
             'description': 'Frozen source pages; only prose/heading/caption boundaries reviewed.'},
            {'path': str(findings), 'sha256': file_hash(findings),
             'description': 'Actual overview observations and explicit remaining limitations.'}],
        'evidence_files': {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()},
        'remaining_uncertainties': [
            'Printed wording/grammar/claims are retained verbatim, not corrected or endorsed.',
            'Page8 source-attribution leakage is not source-corrected by this two-page proof; page11 mixed display/prose remains open.',
            'Private-use bullet glyphs remain in raw text with review flags; no blanket glyph deletion.',
            'No full-section fidelity, whole-paper source acceptance, formula correctness or chart interpretation.'],
        'application_status': 'Staged for a future immutable generation after the frozen v14 build; no parent modified.',
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    working, _ = prepare_flow_pages(doc, pages, base / 'span-metrics-20261030-v1')
    applied = apply_layout_reviews(doc, working, [review])
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count',
        'source_relative_path', 'source_sha256', 'raw_pages_sha256')
    candidate = make_document({k: doc[k] for k in keys}, working, improved=True)
    candidate['layout_reviews'] = applied
    validate_layout_reviews(candidate, pages)
    for number in (2, 3, 4):
        if not any(b['kind'] == 'prose' and b['text'].startswith(f'Figure {number} shows')
                for b in candidate['blocks']):
            raise ValueError('Source author paragraph missing from prose')
    if not any(b['kind'] == 'prose' and b['text'].startswith('According to relevant references,')
            and b['text'].endswith('Table 5.') for b in candidate['blocks']):
        raise ValueError('Split table-reference sentence not restored')
    json_new(output, review)
    print({'paper_id': doc['paper_id'], 'source_checked_pages': [9, 10],
        'groups': sum(len(p['groups']) for p in selected), 'whole_paper_source_acceptance': False})


if __name__ == '__main__':
    main()
