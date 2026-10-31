"""Source-bound individual summary restorations; no global classifier rewrite."""
from collections import Counter
from pathlib import Path

from corpus_queries import all_author_blocks, select_sections, selected_blocks
from corpus_reader import Catalog
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_paragraph_reviews import apply_paragraph_reviews, validate_paragraph_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, file_hash, json_new, make_document, rows, section_blocks, section_text, text_with_block_spans


BASE = Path(__file__).resolve().parents[1] / 'artifacts/text-corpus'
OUT = BASE / 'reviews/20261031'


def stage(number, pid, folder_name, findings_name):
    catalog = Catalog(BASE / 'reflow-20261031-v25')
    old = catalog.document(pid)
    pages = rows(catalog.root / 'papers' / pid / 'raw/pages.jsonl')
    meta = {k: old[k] for k in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    prefix = f'q{number:03d}-summary'
    paths = {name: OUT / f'{prefix}-{name}-v1.json' for name in ('layout', 'word-repairs', 'preflight')}
    if number == 114:
        paths['paragraph'] = OUT / f'{prefix}-paragraph-v1.json'
    review_names = ['opening', 'executive'] if number == 114 else ['opening']
    review_paths = [OUT / f'{prefix}-{name}-source-review-v1.json' for name in review_names]
    if any(p.exists() for p in (*paths.values(), *review_paths)):
        raise ValueError('Create-only proof already exists; preserve it')
    folder = OUT / folder_name
    findings = OUT / findings_name
    evidence = [{'path': str(findings), 'sha256': file_hash(findings),
                 'description': 'Actually checked printed prose, paragraph and section ownership findings.'},
                {'path': str(folder / 'manifest.json'), 'sha256': file_hash(folder / 'manifest.json'),
                 'bundle_root': str(folder), 'description': 'All prepared physical pages individually inspected as bounded JPEGs and native lines.'}]
    evidence_files = {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()}
    evidence_files[str(findings)] = file_hash(findings)

    def group(page, name, kind, natives=None, ids=None, opening=None):
        members = [x for x in pages[page-1]['lines'] if x['text'].strip() and
                   (x['line_id'] in ids if ids is not None else x['native_block'] in natives)]
        if not members:
            raise ValueError('Empty source group: ' + name)
        return {'group_id': name, 'kind': kind, 'source_line_ids': [x['line_id'] for x in members],
                'text_sha256': digest(' '.join(x['text'].strip() for x in members).encode()),
                'reason': 'Printed source paragraph, inline contribution and navigation ownership checked individually.',
                **({'opens_section': opening} if opening else {})}

    def part(page, name, kind, native, start, end, opening=None):
        return group(page, name, kind, ids=[f'p{page:04d}-n{native:04d}-l{i:04d}'
                                          for i in range(start, end+1)], opening=opening)

    if number == 114:
        groups = {
            1: [group(1, 'p1-form', 'front_matter', range(15)),
                group(1, 'p1-title', 'title', [15]),
                group(1, 'p1-summary-title', 'heading', [16], opening={'role': 'abstract', 'level': 1}),
                *[group(1, f'p1-summary-{n-16}', 'prose', [n]) for n in range(17, 22)]],
            2: [group(2, 'p2-header', 'furniture', [0]),
                group(2, 'p2-contents-title', 'heading', [1], opening={'role': 'contents', 'level': 1}),
                group(2, 'p2-contents-entries', 'source_object', range(2, 22))],
            3: [group(3, 'p3-header', 'furniture', [0]),
                group(3, 'p3-contents-entries', 'source_object', range(1, 9))],
            29: [group(29, 'p29-header', 'furniture', [0]),
                 group(29, 'p29-executive-title', 'heading', [1], opening={
                     'role': 'abstract', 'level': 1, 'source_context': 'independent-executive-summary'}),
                 *[group(29, f'p29-executive-{n-1}', 'prose', [n]) for n in range(2, 6)],
                 group(29, 'p29-table', 'source_object', [6, 7]),
                 group(29, 'p29-executive-5a', 'prose', [8])],
            30: [group(30, 'p30-header', 'furniture', [0]),
                 group(30, 'p30-executive-5b', 'prose', [1])]}
        checked = [1, 2, 3, 4, 29, 30]
        reason = 'Complete five-paragraph opening summary plus five-paragraph late Executive Summary; separate two Contents pages and table; restore cross-page recommend.'
    else:
        groups = {1: [group(1, 'p1-form', 'front_matter', range(19)),
                      group(1, 'p1-title', 'title', [19]),
                      part(1, 'p1-summary-title', 'heading', 20, 0, 0, {'role': 'abstract', 'level': 1}),
                      part(1, 'p1-opening', 'prose', 20, 1, 3),
                      group(1, 'p1-design', 'prose', [21]),
                      part(1, 'p1-contribution-intro', 'prose', 22, 0, 0),
                      part(1, 'p1-contribution-1', 'list', 22, 1, 2),
                      *[group(1, f'p1-contribution-{n-21}', 'list', [n]) for n in range(23, 28)],
                      group(1, 'p1-closing', 'prose', [28])]}
        checked = [1, 2]
        reason = 'Restore all ten Summary body blocks, including the full first sentence of contribution2; competition form and paper title stay separate.'
    layout = {'schema': 'source-text-layout-review-v1', **meta,
              'reviewer': f'Codex root;2026-10-31;individually checked physicalpages{checked}',
              'reason': reason, 'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
              'pages': [{'page': p, 'groups': values} for p, values in groups.items()],
              'evidence': evidence, 'evidence_files': evidence_files,
              'source_fidelity_approved': False,
              'remaining_uncertainties': ['Other body pages and pending machine review flags remain unaccepted.'],
              'formula_verification': 'paused', 'figure_distillation': 'paused'}
    working, _ = prepare_flow_pages(old, pages, BASE / 'span-metrics-20261030-v1')
    applied = apply_layout_reviews(old, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    validate_layout_reviews(candidate, pages)
    by_group = {b.get('layout_group_id'): b for b in candidate['blocks'] if b.get('layout_group_id')}
    if number == 114:
        replacements = {'p1-summary-5': [('advan- t', 'advant')],
                        'p29-executive-1': [('prob- le', 'proble')],
                        'p29-executive-2': [('con- st', 'const'), ('assump- ', 'assump'), ('De- bris', 'Debris')],
                        'p29-executive-3': [('sev- er', 'sever'), ('O- DR', 'ODR')],
                        'p29-executive-4': [('clean- e', 'cleane')],
                        'p29-executive-5a': [('remov- i', 'removi'), ('rec-', 'rec')]}
    else:
        replacements = {'p1-contribution-2': [('PTV- V', 'PTV-V')]}
    operations = []
    for name, pairs in replacements.items():
        block = by_group[name]
        text = block['text']
        for before, after in pairs:
            if text.count(before) != 1:
                raise ValueError(f'Exact source wrap differs: {name}/{before}')
            changed = text.replace(before, after)
            operations.append({'block_id': block['block_id'], 'operation': 'literal_replace',
                               'old': before, 'new': after, 'count': 1,
                               'before_text_sha256': digest(text.encode()),
                               'after_text_sha256': digest(changed.encode()),
                               'reason': 'Individually checked printed line-wrap characters; preserve author wording and real compound hyphens.'})
            text = changed
    repair = {**meta, 'reviewer': layout['reviewer'], 'checked_pages': checked,
              'reason': 'Exact short transcription operations for individually inspected source line wraps.',
              'operations': operations, 'evidence': evidence, 'source_fidelity_approved': False,
              'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    join = None
    if number == 114:
        left, right = by_group['p29-executive-5a'], by_group['p30-executive-5b']
        join = {'schema': 'source-paragraph-join-review-v1', **meta, 'reviewer': layout['reviewer'],
                'checked_pages': [29, 30], 'reason': 'Final Executive Summary paragraph continues across the last two physical pages.',
                'evidence': evidence, 'evidence_files': evidence_files,
                'joins': [{'left_block_id': left['block_id'], 'right_block_id': right['block_id'],
                           'separator': '', 'discretionary_wrap_word': 'recommend',
                           'left_text_sha256': digest(left['text'].encode()),
                           'right_text_sha256': digest(right['text'].encode()),
                           'reason': 'Source prints rec- at page29 bottom and ommend at page30 top; the hyphen removal is separately logged.'}],
                'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
        apply_paragraph_reviews(candidate, [join])
        validate_paragraph_reviews(candidate)
    validate_layout_reviews(candidate, pages)
    source = Counter(x['line_id'] for p in pages for x in p['lines'])
    used = Counter(lid for b in candidate['blocks'] for lid in b['source_line_ids'])
    used.update(x['line_id'] for x in candidate['excluded_source_lines'])
    if source != used or any(n != 1 for n in used.values()):
        raise ValueError('Source line lost or duplicated')
    ids, excluded = select_sections(candidate, 'abstract')
    blocks = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text, spans = text_with_block_spans(blocks)
    expected_pages = {1, 29, 30} if number == 114 else {1}
    logical = sum(b['kind'] in {'prose', 'list', 'mixed', 'author_callout'} for b in blocks) - sum(
        bool(b.get('paragraph_continues_from')) for b in blocks)
    if {p for s in spans for p in s['pages']} != expected_pages or logical != 10:
        raise ValueError('Complete abstract selection/paragraph count differs: ' + repr({
            'pages': sorted({p for s in spans for p in s['pages']}), 'logical': logical,
            'selected': ids, 'blocks': [(b['block_id'], b['kind'], b.get('layout_group_id'),
                                      b['text'][:100]) for b in blocks]}))
    if number == 114:
        if (not text.startswith('summary\n\nWe aim to devise') or not text.endswith('beneﬁts both environmentally and economically.') or
                'strongly recommend the government' not in text or 'Rank Approach' in text):
            raise ValueError('Complete dual-summary source contract differs')
        _, author_spans = text_with_block_spans(all_author_blocks(candidate))
        if any(p in (2, 3) for s in author_spans for p in s['pages']):
            raise ValueError('Navigation leaked into author view')
    elif (not text.startswith('Summary\n\nIn this paper, we analyze') or not text.endswith('accident prevention.') or
          '(2) We analyze the throughput' not in text or 'PTV- VISSIM' in text or
          sum(b['kind'] == 'list' for b in blocks) != 6):
        raise ValueError('Complete six-contribution summary differs')
    reviews = []
    for section in [s for s in candidate['sections'] if s['section_id'] in ids]:
        body = section_blocks(candidate, [section['section_id']])
        if not body:
            continue
        reviews.append({**meta, 'section_id': section['section_id'],
                        'text_sha256': digest(section_text(candidate, [section['section_id']]).encode()),
                        'reviewer': layout['reviewer'], 'checked_pages': checked,
                        'section_boundaries_checked': True, 'paragraph_boundaries_checked': True,
                        'paragraph_blocks': [b['block_id'] for b in body if b['kind'] != 'heading'],
                        'evidence': {'findings': findings.name, 'layout': paths['layout'].name,
                                     'literal_repairs': paths['word-repairs'].name,
                                     'scope': reason},
                        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
                        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    if len(reviews) != len(review_paths):
        raise ValueError('Reviewed section count differs')
    for name, value in [('layout', layout), ('word-repairs', repair), *([('paragraph', join)] if join else [])]:
        json_new(paths[name], value)
    for path, review in zip(review_paths, reviews):
        json_new(path, review)
    for name in ('layout', *(['paragraph'] if join else [])):
        prepare_review_bundles([paths[name]], identity_fields=('paper_id',), application_status='preflight only')
    result = {'paper_id': pid, 'parent_dataset_id': catalog.identity, 'characters': len(text),
              'sha256': digest(text.encode()), 'physical_pages': sorted(expected_pages),
              'logical_author_paragraphs': logical, 'literal_repairs': len(operations),
              'boundary_reviews': len(reviews), 'source_lines_accounted_once': True,
              'unresolved_machine_flags_retained': True, 'source_fidelity_approved': False,
              'ai_reading_receipts_created': 0}
    json_new(paths['preflight'], result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    stage(114, 'P-B-2016-48573-960f7126', 'q114-opening-executive-pages-v1', 'q114-opening-executive-findings-v1.json')
    stage(116, 'P-B-2017-56731-a60a9459', 'q116-opening-pages-v1', 'q116-opening-findings-v1.json')
