"""Restore one source-checked three-paragraph Summary; preserve every raw line."""
from collections import Counter
from pathlib import Path

from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs, validate_hyphen_resolutions
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    directory = base / 'reviews/20261031'
    root = base / 'reflow-20261031-v28'
    paths = {name: directory / f'q256-summary-{name}-v1.json'
             for name in ('layout', 'word-repairs', 'source-review', 'preflight')}
    preview = directory / 'q256-summary-preview-v1.md'
    if any(path.exists() for path in [*paths.values(), preview]):
        raise ValueError('Create-only restoration evidence exists; preserve it')
    catalog = Catalog(root)
    old = catalog.document('P-C-2025-2501869-dbf7e00e')
    if old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews'):
        raise ValueError('Existing paper-specific proof needs explicit replay')
    meta = {key: old[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    raw = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    if file_hash(raw) != old['raw_pages_sha256'] or file_hash(source) != old['source_sha256']:
        raise ValueError('Native/PDF binding changed')
    pages = rows(raw)
    folder = directory / 'q256-opening-pages-v1'
    manifest = read_json(folder / 'manifest.json')
    finding_path = directory / 'q256-opening-layout-findings-v1.json'
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
        {'path': str(finding_path), 'sha256': file_hash(finding_path),
         'description': 'Actual three-page prose/layout findings; complete page1 Summary and following Contents/Introduction boundary.'},
        {'path': str(folder / 'manifest.json'), 'sha256': file_hash(folder / 'manifest.json'),
         'bundle_root': str(folder), 'description': 'Individually inspected JPEGs and native text; original rasters retained.'}]
    files = {str(path): file_hash(path) for path in folder.iterdir() if path.is_file()}
    files[str(finding_path)] = file_hash(finding_path)

    def group(page, name, kind, natives=None, ids=None, opening=None):
        lines = [line for line in pages[page-1]['lines'] if line['text'].strip() and not line.get('superseded_by_ocr') and
                 (line['line_id'] in ids if ids is not None else line['native_block'] in natives)]
        if not lines:
            raise ValueError('Empty exact layout group')
        return {'group_id': name, 'kind': kind, 'source_line_ids': [line['line_id'] for line in lines],
                'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
                'reason': 'Actually checked printed paragraph/navigation/marginal-glyph ownership.',
                **({'opens_section': opening} if opening else {})}

    marginal = [line for line in pages[0]['lines'] if line['native_block'] >= 13 and line['text'].strip()]
    if (len(marginal) != 687 or any(line['text'].strip() != 'm' or
            abs(line['font_size'] - 1.3789234161376953) > 1e-9 or line['bbox'][0] < 5 or
            line['bbox'][2] > 75 or line['bbox'][1] < 767 or line['bbox'][3] > 837 for line in marginal)):
        raise ValueError('Exact source-bound marginal glyph preimage differs')
    groups = {
        1: [group(1, 'p1-form', 'front_matter', range(2, 7)),
            group(1, 'p1-paper-title', 'title', [7, 8]),
            group(1, 'p1-summary-title', 'heading', ids=['p0001-n0009-l0000'], opening={'role': 'abstract', 'level': 1}),
            group(1, 'p1-summary-1', 'prose', ids=[f'p0001-n0009-l{n:04d}' for n in range(1, 17)]),
            group(1, 'p1-summary-2', 'prose', [10]),
            group(1, 'p1-summary-3', 'prose', [11]),
            group(1, 'p1-keywords', 'keywords', [12]),
            group(1, 'p1-third-party-watermark', 'furniture', [0, 1]),
            group(1, 'p1-marginal-grid', 'furniture', ids=[line['line_id'] for line in marginal])],
        2: [group(2, 'p2-contents-title', 'heading', ids=['p0002-ocr-l0000'], opening={'role': 'contents', 'level': 1}),
            group(2, 'p2-navigation', 'source_object', ids=[f'p0002-ocr-l{n:04d}' for n in range(1, 115)]),
            group(2, 'p2-third-party-promotion', 'furniture', ids=['p0002-ocr-l0115', 'p0002-ocr-l0116'])]}
    layout = {'schema': 'source-text-layout-review-v1', **meta, 'reviewer': findings['reviewer'],
        'reason': 'Restore all three Summary task paragraphs and exact end; preserve marginal glyphs and OCR Contents separately.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
        'pages': [{'page': page, 'groups': values} for page, values in groups.items()],
        'evidence': evidence, 'evidence_files': files, 'source_fidelity_approved': False,
        'remaining_uncertainties': ['All later author chapters and OCR navigation spelling remain pending.'],
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    working, _ = prepare_flow_pages(old, pages, base / 'span-metrics-20261030-v1')
    applied = apply_layout_reviews(old, working, [layout])
    candidate = make_document({key: old[key] for key in ('paper_id', 'problem_type', 'year', 'queue_position',
        'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}, working, improved=True)
    candidate['layout_reviews'] = applied
    by_group = {block.get('layout_group_id'): block for block in candidate['blocks'] if block.get('layout_group_id')}
    operations = []
    pairs = {'p1-summary-1': [('char- a', 'chara'), ('Compar- ', 'Compar')],
             'p1-summary-2': [('break- t', 'breakt'), ('two- s', 'two-s')]}
    for name, replacements in pairs.items():
        block = by_group[name]
        text = block['text']
        literal = []
        for before, after in replacements:
            if text.count(before) != 1:
                raise ValueError('Exact printed word-wrap preimage differs')
            changed = text.replace(before, after)
            operation = {'block_id': block['block_id'], 'operation': 'literal_replace',
                'old': before, 'new': after, 'count': 1,
                'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
                'reason': 'Exact printed discretionary break or compound wrap; author wording and genuine hyphens retained.'}
            literal.append(operation)
            operations.append(operation)
            text = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
            'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(text.encode()),
            'transcription_operations_sha256': digest(encoded(literal)),
            'reason': 'All discretionary/wrapped compound breaks in this exact complete source paragraph were individually checked.'})
    repair = {**meta, 'reviewer': findings['reviewer'], 'checked_pages': [1, 2, 3],
        'reason': 'Restore exactly four printed word wraps; preserve author claims/wording and all raw lines.',
        'operations': operations, 'evidence': evidence, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_hyphen_resolutions(candidate)
    validate_layout_reviews(candidate, pages)
    used = Counter(lid for block in candidate['blocks'] for lid in block['source_line_ids'])
    used.update(line['line_id'] for line in candidate['excluded_source_lines'])
    expected = Counter(line['line_id'] for page in pages for line in page['lines'])
    if used != expected or any(value != 1 for value in used.values()):
        raise ValueError('Source-line ownership lost or duplicated')
    ids, excluded = select_sections(candidate, 'abstract')
    blocks = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text, spans = text_with_block_spans(blocks)
    ids = [sid for sid in ids if any(block['section_id'] == sid for block in blocks)]
    body = [block for block in blocks if block['kind'] != 'heading']
    if (len(ids) != 1 or len(body) != 3 or {page for span in spans for page in span['pages']} != {1} or
            not text.startswith('Summary\n\nIn Question 1,') or
            not text.endswith('“breadth” of National Olympic Committees.') or
            any(token in text for token in ('MATHmodels', '微信公众号', 'Summary Sheet', 'Keywords:', 'char- ', 'Compar- ', 'break- ', 'two- ')) or
            not all(f'In Question {n},' in text for n in (1, 2, 3))):
        raise ValueError('Exact complete three-paragraph Summary selection differs')
    if any(2 in block['source_pages'] for block in all_author_blocks(candidate)):
        raise ValueError('Contents leaked into author text')
    section = next(section for section in candidate['sections'] if section['section_id'] == ids[0])
    source_review = {**meta, 'section_id': section['section_id'],
        'text_sha256': digest(section_text(candidate, [section['section_id']]).encode()),
        'reviewer': findings['reviewer'], 'checked_pages': [1, 2, 3],
        'section_boundaries_checked': True, 'paragraph_boundaries_checked': True,
        'paragraph_blocks': [block['block_id'] for block in section_blocks(candidate, [section['section_id']]) if block['kind'] != 'heading'],
        'evidence': {'findings': finding_path.name, 'layout': paths['layout'].name, 'literal_repairs': paths['word-repairs'].name},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    result = {'paper_id': old['paper_id'], 'parent_dataset_id': catalog.identity,
        'source_lines_accounted_once': True, 'logical_author_paragraphs': 3, 'characters': len(text),
        'text_sha256': digest(text.encode()), 'literal_wrap_occurrences_repaired': 4,
        'paragraph_hyphen_flags_resolved': 2, 'section_boundaries_checked': True,
        'marginal_grid_source_lines_retained': 687, 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    for name, value in [('layout', layout), ('word-repairs', repair), ('source-review', source_review)]:
        json_new(paths[name], value)
    prepare_review_bundles([paths['layout']], identity_fields=('paper_id',), application_status='preflight only')
    prepare_review_bundles([paths['word-repairs']], identity_fields=('paper_id',), application_status='preflight only')
    result['proof_sha256'] = {str(paths[name].resolve()): file_hash(paths[name]) for name in ('layout', 'word-repairs', 'source-review')}
    json_new(paths['preflight'], result)
    write_new(preview, text + '\n')
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
