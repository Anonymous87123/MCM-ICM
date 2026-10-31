"""Restore two complete technical summaries and separate their intervening memo."""
from collections import Counter
from pathlib import Path
from corpus_reader import Catalog
from corpus_queries import select_sections, selected_blocks
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_paragraph_reviews import apply_paragraph_reviews, validate_paragraph_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, file_hash, json_new, make_document, rows, text_with_block_spans


def main():
    base = Path(__file__).resolve().parents[1] / 'artifacts/text-corpus'
    root = base / 'reflow-20261031-v24'; out = base / 'reviews/20261031'
    targets = [out / f'q096-opening-{name}-v1.json' for name in ('layout', 'word-repairs', 'paragraph', 'preflight')]
    if any(p.exists() for p in targets):
        raise ValueError('Create-only q96 proof exists; preserve it')
    catalog = Catalog(root); old = catalog.document('P-B-2012-15171-ce229936')
    pages = rows(root / 'papers' / old['paper_id'] / 'raw/pages.jsonl')
    folder = out / 'q096-opening-pages-v1'; findings = out / 'q096-opening-findings-v1.json'
    evidence = [{'path': str(findings), 'sha256': file_hash(findings), 'description': 'Individual physical-page prose and ownership findings.'},
                {'path': str(folder / 'manifest.json'), 'sha256': file_hash(folder / 'manifest.json'),
                 'bundle_root': str(folder), 'description': 'Prepared native/page evidence; only pages1–4 actually inspected.'}]
    files = {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()}; files[str(findings)] = file_hash(findings)
    def group(page, name, kind, natives=None, ids=None, opening=None):
        members = [x for x in pages[page-1]['lines'] if x['text'].strip() and
                   (x['line_id'] in ids if ids is not None else x['native_block'] in natives)]
        return {'group_id': name, 'kind': kind, 'source_line_ids': [x['line_id'] for x in members],
                'text_sha256': digest(' '.join(x['text'].strip() for x in members).encode()),
                'reason': 'Individually checked printed paragraph indentation, text lane and section ownership.',
                **({'opens_section': opening} if opening else {})}
    def part(page, name, kind, block, start, end, opening=None):
        return group(page, name, kind, ids=[f'p{page:04d}-n{block:04d}-l{i:04d}' for i in range(start, end+1)], opening=opening)
    groups = {
        1: [part(1, f'p1-summary-{i}', 'prose', 0, a, b) for i, (a, b) in enumerate(((0,10),(11,15),(16,20),(21,27),(28,33)),1)],
        2: [group(2, 'p2-team', 'furniture', [0]),
            group(2, 'p2-memo-header', 'author_callout', [1], opening={'role':'memo','level':1,'source_context':'memo-recipient-header'}),
            part(2, 'p2-memo-summary-title', 'heading', 2, 0, 0, {'role':'other','level':2,'source_context':'memo-summary-subsection'}),
            part(2, 'p2-memo-summary-body', 'prose', 2, 1, 10),
            part(2, 'p2-proposals-title', 'heading', 3, 0, 0, {'role':'other','level':2}),
            part(2, 'p2-itinerary', 'prose', 3, 1, 6),
            part(2, 'p2-distance-management', 'prose', 3, 7, 13),
            group(2, 'p2-choice', 'prose', [4]),
            part(2, 'p2-costs-title', 'heading', 5, 0, 0, {'role':'other','level':2}),
            part(2, 'p2-costs-body', 'prose', 5, 1, 9)],
        3: [group(3, 'p3-paper-title', 'title', [0,1]), group(3, 'p3-team-date', 'front_matter', [2,3]),
            group(3, 'p3-summary-title', 'heading', [4], opening={'role':'abstract','level':1}),
            group(3, 'p3-summary-1', 'prose', range(5,17)), group(3, 'p3-summary-2', 'prose', range(17,23)),
            group(3, 'p3-summary-3a', 'prose', range(23,27)), group(3, 'p3-page', 'furniture', [27])],
        4: [group(4, 'p4-header', 'furniture', [0]), group(4, 'p4-summary-3b', 'prose', [1,2]),
            group(4, 'p4-summary-4', 'prose', range(3,11)), group(4, 'p4-summary-5', 'prose', range(11,18)),
            group(4, 'p4-introduction-title', 'heading', [18], opening={'role':'introduction','level':1}),
            group(4, 'p4-introduction', 'prose', range(19,30)),
            group(4, 'p4-parameters-title', 'heading', [30], opening={'role':'other','level':1})]}
    meta = {k: old[k] for k in ('paper_id','source_sha256','raw_pages_sha256')}
    layout = {'schema':'source-text-layout-review-v1', **meta, 'reviewer':'Codex root;2026-10-31; physical pages1–4',
        'reason':'Separate untitled summary, independent memo and complete cross-page formal Summary. Preserve literal local headings.',
        'paragraph_boundaries_checked':True, 'reading_lanes_checked':True,
        'pages':[{'page':p,'groups':g} for p,g in groups.items()], 'evidence':evidence,'evidence_files':files,
        'source_fidelity_approved':False,'remaining_uncertainties':['Physical pages5–36 remain unreviewed.'],
        'formula_verification':'paused','figure_distillation':'paused'}
    working, _ = prepare_flow_pages(old,pages,base/'span-metrics-20261030-v1')
    applied = apply_layout_reviews(old,working,[layout]); candidate = make_document(meta,working,improved=True)
    candidate['layout_reviews'] = applied; validate_layout_reviews(candidate,pages)
    block = next(b for b in candidate['blocks'] if b.get('layout_group_id')=='p4-summary-5')
    before = block['text']; after = before.replace('con- ﬁ','conﬁ')
    if before.count('con- ﬁ') != 1 or before == after:
        raise ValueError('Exact checked discretionary line wrap differs')
    repair = {**meta,'reviewer':layout['reviewer'],'reason':'One source-checked discretionary line-wrap repair; no paraphrase.',
        'checked_pages':[1,2,3,4],'operations':[{'block_id':block['block_id'],'operation':'literal_replace',
            'old':'con- ﬁ','new':'conﬁ','count':1,'before_text_sha256':digest(before.encode()),
            'after_text_sha256':digest(after.encode()),'reason':'Printed con- / ﬁdently is one word across a line wrap.'}],
        'evidence':evidence,'source_fidelity_approved':False,'formula_verification':'paused','figure_distillation':'paused'}
    apply_text_repairs(candidate,[repair])
    left = next(b for b in candidate['blocks'] if b.get('layout_group_id')=='p3-summary-3a')
    right = next(b for b in candidate['blocks'] if b.get('layout_group_id')=='p4-summary-3b')
    join = {'schema':'source-paragraph-join-review-v1',**meta,'reviewer':layout['reviewer'],
        'reason':'The printed formal Summary third paragraph continues from physicalpage3topage4.',
        'checked_pages':[3,4],'evidence':evidence,'evidence_files':files,'joins':[
            {'left_block_id':left['block_id'],'right_block_id':right['block_id'],'separator':' ',
             'left_text_sha256':digest(left['text'].encode()),'right_text_sha256':digest(right['text'].encode()),
             'reason':'Their potential destination sites is a source-checked ordinary word boundary in the same paragraph.'}],
        'source_fidelity_approved':False,'formula_verification':'paused','figure_distillation':'paused'}
    apply_paragraph_reviews(candidate,[join]); validate_paragraph_reviews(candidate); validate_layout_reviews(candidate,pages)
    source = Counter(x['line_id'] for p in pages for x in p['lines'])
    used = Counter(x for b in candidate['blocks'] for x in b['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if source != used or any(n!=1 for n in used.values()):
        raise ValueError('Source line lost or duplicated')
    results = {}
    for query, expected_pages, paragraphs in [('abstract',{1,3,4},10),('memo',{2},5),('introduction',{4},1)]:
        ids, excluded = select_sections(candidate,query)
        blocks = selected_blocks(candidate,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        text, spans = text_with_block_spans(blocks)
        count = sum(b['kind']=='prose' for b in blocks)-sum(bool(b.get('paragraph_continues_from')) for b in blocks)
        if {p for s in spans for p in s['pages']} != expected_pages or count != paragraphs:
            raise ValueError('Checked query scope/paragraphs differ: '+query)
        if query == 'abstract' and ('To: Managers' in text or 'February 12' in text or
                'their potential destination sites than motor boats.' not in text or
                not text.endswith('a maximum throughput in this range.')):
            raise ValueError('Summary scope/continuation differs')
        results[query] = {'characters':len(text),'sha256':digest(text.encode()),'physical_pages':sorted(expected_pages),
                          'logical_author_paragraphs':paragraphs}
        print(query,text,sep='\n',flush=True)
    for path, value in zip(targets[:3],(layout,repair,join)):
        json_new(path,value)
    for path in (targets[0],targets[2]):
        prepare_review_bundles([path],identity_fields=('paper_id',),application_status='preflight only')
    result = {'parent_dataset_id':catalog.identity,'paper_id':old['paper_id'],'results':results,
        'literal_repairs':1,'source_lines_accounted_once':True,'source_fidelity_approved':False,'ai_receipts_created':0}
    json_new(targets[3],result); print(result,flush=True)


if __name__ == '__main__':
    main()
