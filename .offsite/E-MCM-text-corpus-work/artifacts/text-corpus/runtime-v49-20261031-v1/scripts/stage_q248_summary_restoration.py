"""Recover q248's native paragraph order, not a rewritten or sampled Summary."""
from collections import Counter
from pathlib import Path

from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    directory = base / 'reviews/20261031'
    root = base / 'reflow-20261031-v29'
    paths = {name: directory / f'q248-summary-{name}-v1.json'
             for name in ('layout', 'word-repairs', 'source-review', 'preflight')}
    preview = directory / 'q248-summary-preview-v1.md'
    if any(path.exists() for path in [*paths.values(), preview]):
        raise ValueError('Create-only restoration evidence exists; preserve it')
    catalog = Catalog(root)
    old = catalog.document('P-C-2024-2406176-bd7757f9')
    if old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews'):
        raise ValueError('Existing paper-specific proof needs explicit replay')
    meta = {key: old[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    raw = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    if file_hash(raw) != old['raw_pages_sha256'] or file_hash(source) != old['source_sha256']:
        raise ValueError('Native/PDF binding changed')
    pages = rows(raw)
    folder = directory / 'q248-opening-pages-v1'
    manifest = read_json(folder / 'manifest.json')
    finding_path = directory / 'q248-opening-layout-findings-v1.json'
    findings = read_json(finding_path)
    if any(manifest[key] != old[key] or findings[key] != old[key] for key in meta):
        raise ValueError('Inspected evidence source differs')
    for name, sha in manifest['files'].items():
        if file_hash(folder / name) != sha:
            raise ValueError('Prepared evidence changed')
    for proof in findings['evidence']:
        path = work / proof['path']
        if file_hash(path) != proof['sha256'] or path.stat().st_size != proof['bytes'] or proof['bytes'] > 450000:
            raise ValueError('Actually inspected JPEG changed')
    evidence = [
        {'path': str(finding_path), 'sha256': file_hash(finding_path), 'description': 'Actually read two-page layout and native same-baseline sentence order.'},
        {'path': str(folder / 'manifest.json'), 'sha256': file_hash(folder / 'manifest.json'), 'bundle_root': str(folder), 'description': 'Both individually inspected JPEGs and original native/raster evidence.'}]
    files = {str(path): file_hash(path) for path in folder.iterdir() if path.is_file()}
    files[str(finding_path)] = file_hash(finding_path)

    def group(name, kind, natives, opening=None):
        lines = [line for line in pages[0]['lines'] if line['text'].strip() and not line.get('superseded_by_ocr') and line['native_block'] in natives]
        if not lines:
            raise ValueError('Empty exact layout group')
        return {'group_id': name, 'kind': kind, 'source_line_ids': [line['line_id'] for line in lines],
                'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
                'reason': 'Actual source paragraph order and separate metadata/keyword/furniture ownership.',
                **({'opens_section': opening} if opening else {})}

    groups = [group('p1-form', 'front_matter', range(2, 7)),
              group('p1-summary-title', 'heading', [7], {'role': 'abstract', 'level': 1}),
              *[group(f'p1-summary-{n-7}', 'prose', [n]) for n in range(8, 13)],
              group('p1-keywords', 'keywords', [13]),
              group('p1-third-party', 'furniture', [0, 1, 14, 15, 16, 17])]
    layout = {'schema': 'source-text-layout-review-v1', **meta, 'reviewer': findings['reviewer'],
        'reason': 'Restore five complete Summary paragraphs, observations-before-The-significance sentence order and full keyword ownership.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
        'pages': [{'page': 1, 'groups': groups}], 'evidence': evidence, 'evidence_files': files,
        'source_fidelity_approved': False, 'remaining_uncertainties': ['Every later chapter and Contents continuation remain pending.'],
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    working, _ = prepare_flow_pages(old, pages, base / 'span-metrics-20261030-v1')
    applied = apply_layout_reviews(old, working, [layout])
    candidate = make_document({key: old[key] for key in ('paper_id', 'problem_type', 'year', 'queue_position',
        'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}, working, improved=True)
    candidate['layout_reviews'] = applied
    block = next(block for block in candidate['blocks'] if block.get('layout_group_id') == 'p1-summary-5')
    text = block['text']
    if text.count('cap- t') != 1:
        raise ValueError('Exact discretionary word-wrap preimage differs')
    changed = text.replace('cap- t', 'capt')
    literal = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': 'cap- t', 'new': 'capt', 'count': 1,
        'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
        'reason': 'Printed cap-/tures is a discretionary word wrap, not a compound.'}
    resolution = {'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
        'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
        'before_text_sha256': digest(changed.encode()), 'after_text_sha256': digest(changed.encode()),
        'transcription_operations_sha256': digest(encoded([literal])),
        'reason': 'The one wrapped fragment in this complete paragraph was individually source-checked; real compounds remain.'}
    repair = {**meta, 'reviewer': findings['reviewer'], 'checked_pages': [1, 2],
        'reason': 'One literal discretionary break; no author spelling, numbers or claims changed.',
        'operations': [literal, resolution], 'evidence': evidence, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, pages)
    actual = Counter(lid for block in candidate['blocks'] for lid in block['source_line_ids'])
    actual.update(line['line_id'] for line in candidate['excluded_source_lines'])
    expected = Counter(line['line_id'] for page in pages for line in page['lines'])
    if actual != expected or any(value != 1 for value in actual.values()):
        raise ValueError('Source-line ownership lost or duplicated')
    ids, excluded = select_sections(candidate, 'abstract')
    blocks = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text, spans = text_with_block_spans(blocks)
    ids = [sid for sid in ids if any(block['section_id'] == sid for block in blocks)]
    if (len(ids) != 1 or sum(block['kind'] != 'heading' for block in blocks) != 5 or
            {page for span in spans for page in span['pages']} != {1} or
            not text.startswith('Summary\n\nMomentum,') or not text.endswith('Eventually, we pinpoint crucial factors for inclusion in future models.') or
            'real-world observations. The significance of momentum' not in text or
            'base on the Elo rating system' not in text or 'accurately captures momentum trends' not in text or
            any(token in text for token in ('Summary Sheet', 'MATHmodels', 'Keywords:', 'quantification model', 'cap- '))):
        raise ValueError('Exact five-paragraph source Summary differs')
    old_rest = [block for block in all_author_blocks(old) if min(block['source_pages']) > 1]
    new_rest = [block for block in all_author_blocks(candidate) if min(block['source_pages']) > 1]
    signature = lambda values: [(block['source_line_ids'], block['text'], block['kind'], block['issues']) for block in values]
    if signature(old_rest) != signature(new_rest):
        raise ValueError('Later author prose changed')
    sid = ids[0]
    source_review = {**meta, 'section_id': sid, 'text_sha256': digest(section_text(candidate, [sid]).encode()),
        'reviewer': findings['reviewer'], 'checked_pages': [1, 2],
        'section_boundaries_checked': True, 'paragraph_boundaries_checked': True,
        'paragraph_blocks': [block['block_id'] for block in section_blocks(candidate, [sid]) if block['kind'] != 'heading'],
        'evidence': {'findings': finding_path.name, 'layout': paths['layout'].name, 'literal_repairs': paths['word-repairs'].name},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    for name, value in [('layout', layout), ('word-repairs', repair), ('source-review', source_review)]:
        json_new(paths[name], value)
    prepare_review_bundles([paths['layout']], identity_fields=('paper_id',), application_status='preflight only')
    prepare_review_bundles([paths['word-repairs']], identity_fields=('paper_id',), application_status='preflight only')
    result = {'paper_id': old['paper_id'], 'parent_dataset_id': catalog.identity,
        'source_lines_accounted_once': True, 'logical_author_paragraphs': 5, 'characters': len(text),
        'text_sha256': digest(text.encode()), 'literal_wrap_occurrences_repaired': 1,
        'paragraph_hyphen_flags_resolved': 1, 'same_baseline_native_line_order_restored': True,
        'later_author_text_unchanged': True, 'section_boundaries_checked': True,
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0,
        'proof_sha256': {str(paths[name].resolve()): file_hash(paths[name]) for name in ('layout', 'word-repairs', 'source-review')}}
    json_new(paths['preflight'], result)
    write_new(preview, text + '\n')
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
