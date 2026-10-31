"""Stage one source-read summary, with explicit later metadata exceptions only."""
import argparse
from collections import Counter
from pathlib import Path
import sys

WORK = Path(r'F:\MCM\mcm-skill-work')
sys.path.insert(0, str(WORK / 'scripts'))
from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def stage(spec_path):
    spec = read_json(spec_path)
    directory = spec_path.parent
    version = spec['output_version']
    paths = {name: directory / (spec['output_prefix'] + '-' + name + f'-v{version}.json')
             for name in ('layout', 'word-repairs', 'source-review', 'preflight', 'candidate')}
    preview = directory / (spec['output_prefix'] + f'-preview-v{version}.md')
    if any(p.exists() for p in [*paths.values(), preview]):
        raise ValueError('Create-only source evidence exists;preserve it')
    catalog = Catalog(Path(spec['parent_corpus_root']))
    if catalog.identity != spec['parent_dataset_id'] or spec['schema'] != 'single-source-summary-restoration-v3':
        raise ValueError('Exact individually reviewed parent required')
    old = catalog.document(spec['paper_id'])
    if any(old.get(name) for name in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews')):
        raise ValueError('Existing source proof requires explicit replay')
    meta = {key: old[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    if any(spec[key] != value for key, value in meta.items()):
        raise ValueError('Source identity differs')
    root = Path(spec['parent_corpus_root'])
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    raw = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    if file_hash(source) != old['source_sha256'] or file_hash(raw) != old['raw_pages_sha256']:
        raise ValueError('PDF/native source binding changed')
    pages = rows(raw)
    folder = directory / spec['evidence_folder']
    manifest_path = folder / 'manifest.json'
    findings_path = directory / spec['findings']
    manifest, findings = read_json(manifest_path), read_json(findings_path)
    if any(manifest[key] != value or findings[key] != value for key, value in meta.items()):
        raise ValueError('Inspected source differs')
    for name, sha in manifest['files'].items():
        if file_hash(folder / name) != sha:
            raise ValueError('Original source evidence changed')
    if sorted(Path(p['path']).name for p in findings['evidence']) != sorted(f'page-{n:04d}.jpg' for n in spec['checked_pages']):
        raise ValueError('Actually inspected JPEG coverage differs')
    for proof in findings['evidence']:
        path = Path(proof['path'])
        if file_hash(path) != proof['sha256'] or path.stat().st_size != proof['bytes'] or not 0 < proof['bytes'] <= 450000:
            raise ValueError('Actually inspected JPEG changed')
    metrics = Path(spec['span_metrics_root'])
    if file_hash(metrics / 'manifest.json') != read_json(root / 'scope.json')['span_metrics_manifest_sha256']:
        raise ValueError('Exact accepted native metric binding required')
    evidence = [
        {'path': str(path), 'sha256': file_hash(path), 'description': description,
         **({'bundle_root': str(folder)} if path == manifest_path else {})}
        for path, description in [(findings_path, 'Actual one-paper complete prose and boundary findings.'),
            (spec_path, 'Exact individually source-read paragraph,metadata and word-wrap specification.'),
            (manifest_path, 'All original native/raster/JPEG evidence preserved.'),
            (Path(__file__), 'Exact create-only one-paper staging implementation.')]]
    files = {str(p): file_hash(p) for p in folder.iterdir() if p.is_file()}
    files.update({e['path']: e['sha256'] for e in evidence})
    layouts = []
    for page_spec in spec['pages']:
        groups = []
        for group in page_spec['groups']:
            lines = [line for line in pages[page_spec['page'] - 1]['lines']
                     if line['text'].strip() and not line.get('superseded_by_ocr') and
                     (line['line_id'] in group['source_line_ids'] if 'source_line_ids' in group else line['native_block'] in group['native_blocks'])]
            if not lines:
                raise ValueError('Empty source group')
            groups.append({'group_id': group['group_id'], 'kind': group['kind'],
                'source_line_ids': [line['line_id'] for line in lines],
                'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
                'reason': spec['reason'], **({'opens_section': group['opens_section']} if group.get('opens_section') else {})})
        layouts.append({'page': page_spec['page'], 'groups': groups})
    layout = {'schema': 'source-text-layout-review-v1', **meta, 'reviewer': spec['reviewer'],
        'reason': spec['reason'], 'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
        'pages': layouts, 'evidence': evidence, 'evidence_files': files, 'source_fidelity_approved': False,
        'remaining_uncertainties': spec['remaining_uncertainties'], 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    working, _ = prepare_flow_pages(old, pages, metrics)
    applied = apply_layout_reviews(old, working, [layout])
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    candidate = make_document({key: old[key] for key in keys}, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    groups = {b.get('layout_group_id'): b for b in candidate['blocks'] if b.get('layout_group_id')}
    operations = []
    for entry in spec['wrap_repairs']:
        block = groups[entry['group_id']]; text = block['text']; literal = []
        for before, after, count in entry['replacements']:
            if text.count(before) != count:
                raise ValueError('Exact discretionary-wrap preimage differs')
            changed = text.replace(before, after)
            op = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before, 'new': after, 'count': count,
                'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()), 'reason': spec['wrap_reason']}
            operations.append(op); literal.append(op); text = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
            'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(text.encode()),
            'transcription_operations_sha256': digest(encoded(literal)), 'reason': spec['wrap_reason']})
    classified_ids = []
    for item in spec.get('later_classifications', []):
        if item['to_kind'] not in {'title', 'front_matter', 'keywords', 'furniture', 'contents'}:
            raise ValueError('Later exception must restore an exact non-author classification')
        found = [b for b in candidate['blocks'] if b['text'] == item['text'] and b['source_pages'] == [item['page']]]
        if len(found) != 1 or found[0]['kind'] != 'prose' or item['page'] <= max(spec['abstract_pages']):
            raise ValueError('Exact later metadata classification preimage differs')
        block = found[0]
        before = [b for b in all_author_blocks(old) if b['source_line_ids'] == block['source_line_ids']]
        if len(before) != 1 or before[0]['text'] != item['text'] or before[0]['kind'] != 'prose':
            raise ValueError('Later metadata source IDs/text differ from original')
        operations.append({'block_id': block['block_id'], 'operation': 'classify', 'from_kind': 'prose', 'to_kind': item['to_kind'],
            'before_text_sha256': digest(block['text'].encode()), 'after_text_sha256': digest(block['text'].encode()),
            'reason': item['reason']})
        classified_ids.append(block['source_line_ids'])
    repair = {**meta, 'reviewer': spec['reviewer'], 'checked_pages': spec['checked_pages'], 'reason': spec['wrap_reason'],
        'operations': operations, 'evidence': evidence, 'source_fidelity_approved': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    if operations:
        apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, pages)
    expected = Counter(l['line_id'] for p in pages for l in p['lines'])
    actual = Counter(lid for b in candidate['blocks'] for lid in b['source_line_ids'])
    actual.update(l['line_id'] for l in candidate['excluded_source_lines'])
    if actual != expected or any(n != 1 for n in actual.values()):
        raise ValueError('Source-line ownership differs')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text = text_with_block_spans(selected)[0]
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    if (len(ids) != 1 or sum(b['kind'] != 'heading' for b in selected) != spec['expected_author_paragraphs']
            or {p for b in selected for p in b['source_pages']} != set(spec['abstract_pages'])
            or not text.startswith(spec['text_starts']) or not text.endswith(spec['text_ends'])
            or any(t not in text for t in spec['required_text']) or any(t in text for t in spec['forbidden_text'])):
        raise ValueError('Complete exact source Summary guards differ')
    exceptions = list(classified_ids)
    for item in spec.get('later_non_author_groups', []):
        block = groups[item['group_id']]
        if block['kind'] not in {'title', 'front_matter', 'keywords', 'furniture', 'contents'} or block['text'] != item['text']:
            raise ValueError('Later metadata exception is not an exact non-author group')
        found = [b for b in all_author_blocks(old) if b['source_line_ids'] == block['source_line_ids']]
        if len(found) != 1 or found[0]['text'] != item['text'] or found[0]['kind'] != 'prose':
            raise ValueError('Later misclassified-metadata preimage differs')
        exceptions.append(block['source_line_ids'])
    signature = lambda doc: [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(doc)
                             if min(b['source_pages']) > max(spec['abstract_pages']) and b['source_line_ids'] not in exceptions]
    if signature(old) != signature(candidate):
        raise ValueError('Later actual author body changed beyond exact metadata exceptions')
    review = {**meta, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': spec['reviewer'], 'checked_pages': spec['checked_pages'], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True,
        'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'findings': findings_path.name, 'specification': spec_path.name, 'layout': paths['layout'].name,
                    **({'repairs': paths['word-repairs'].name} if operations else {})},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    wanted, bids = {b['section_id'] for b in selected}, {b['block_id'] for b in selected}
    pending = [d for d in candidate['defects'] if d.get('status') != 'resolved' and
               (d.get('section_id') in wanted or d.get('page') in spec['abstract_pages'] or
                any(d.get(k) in bids for k in ('block_id', 'left', 'right')))]
    if pending or any(b['issues'] for b in selected):
        raise ValueError('Selected source summary retains unresolved issues')
    outputs = [('layout', layout), ('source-review', review), ('candidate', candidate)]
    if operations:
        outputs.append(('word-repairs', repair))
    for name, value in outputs:
        json_new(paths[name], value)
    prepare_review_bundles([paths['layout']], identity_fields=('paper_id',), application_status='preflight only;not a built corpus')
    result = {**meta, 'parent_dataset_id': catalog.identity, 'specification_sha256': file_hash(spec_path),
        'stager_sha256': file_hash(Path(__file__)), 'source_lines_accounted_once': True,
        'logical_author_paragraphs': spec['expected_author_paragraphs'], 'characters': len(text), 'text_sha256': digest(text.encode()),
        'literal_wrap_occurrences_repaired': sum(c[2] for e in spec['wrap_repairs'] for c in e['replacements']),
        'selected_source_status': 'verified in prospective stage only', 'later_actual_author_body_unchanged': True,
        'exact_later_metadata_source_ids_excluded': exceptions, 'section_boundaries_checked': True,
        'has_text_repairs': bool(operations),
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0,
        'proof_sha256': {str(paths[name]): file_hash(paths[name]) for name, _ in outputs}}
    json_new(paths['preflight'], result)
    write_new(preview, text + '\n')
    print(text, flush=True); print(result, flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', type=Path, required=True)
    stage(parser.parse_args().spec.resolve())
