"""Stage ONE manually source-reviewed summary specification, never a corpus batch."""
import argparse
from collections import Counter
from pathlib import Path

from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def stage(spec_path):
    work = Path(__file__).resolve().parents[1]
    spec = read_json(spec_path)
    base = work / 'artifacts/text-corpus'
    directory = spec_path.parent
    version = spec.get('output_version', 1)
    if type(version) is not int or version < 1:
        raise ValueError('Positive integer output version required')
    paths = {name: directory / (spec['output_prefix'] + '-' + name + f'-v{version}.json')
             for name in ('layout', 'word-repairs', 'source-review', 'preflight')}
    preview = directory / (spec['output_prefix'] + f'-preview-v{version}.md')
    if any(path.exists() for path in [*paths.values(), preview]):
        raise ValueError('Create-only evidence exists; preserve it')
    root = base / spec['parent_generation']
    catalog = Catalog(root)
    if catalog.identity != spec['parent_dataset_id'] or spec.get('schema') != 'explicit-single-summary-restoration-v1':
        raise ValueError('Exact reviewed parent dataset/specification required')
    old = catalog.document(spec['paper_id'])
    if old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews'):
        raise ValueError('Existing source proof needs explicit replay, not this first-restoration tool')
    meta = {key: old[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    if any(spec[key] != value for key, value in meta.items()) or not spec.get('reviewer'):
        raise ValueError('Manually checked paper/source identity required')
    raw = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    if file_hash(raw) != old['raw_pages_sha256'] or file_hash(source) != old['source_sha256']:
        raise ValueError('Native/PDF binding changed')
    pages = rows(raw)
    folder = directory / spec['evidence_folder']
    manifest_path = folder / 'manifest.json'
    manifest = read_json(manifest_path)
    findings_path = directory / spec['findings']
    findings = read_json(findings_path)
    if any(manifest[key] != value or findings[key] != value for key, value in meta.items()):
        raise ValueError('Inspected source evidence differs')
    for name, sha in manifest['files'].items():
        if file_hash(folder / name) != sha:
            raise ValueError('Prepared native/raster/proxy evidence changed')
    if sorted(proof['path'].split('/')[-1] for proof in findings['evidence']) != sorted(
            f'page-{page:04d}.jpg' for page in spec['checked_pages']):
        raise ValueError('Checked page/JPEG coverage differs')
    for proof in findings['evidence']:
        path = work / proof['path']
        if file_hash(path) != proof['sha256'] or path.stat().st_size != proof['bytes'] or proof['bytes'] > 450000:
            raise ValueError('Actually inspected JPEG changed')
    evidence = [
        {'path': str(findings_path), 'sha256': file_hash(findings_path), 'description': 'Actual individually inspected source prose/layout findings.'},
        {'path': str(spec_path), 'sha256': file_hash(spec_path), 'description': 'Single-paper manually specified native paragraphs, exact wraps and source-reading guards.'},
        {'path': str(manifest_path), 'sha256': file_hash(manifest_path), 'bundle_root': str(folder), 'description': 'All original page evidence retained; bounded JPEGs individually inspected.'}]
    files = {str(path): file_hash(path) for path in folder.iterdir() if path.is_file()}
    files.update({str(findings_path): file_hash(findings_path), str(spec_path): file_hash(spec_path)})
    reviewed_pages = []
    for page_spec in spec['pages']:
        number = page_spec['page']
        groups = []
        for value in page_spec['groups']:
            lines = [line for line in pages[number-1]['lines'] if line['text'].strip() and not line.get('superseded_by_ocr') and
                     (line['line_id'] in value['source_line_ids'] if 'source_line_ids' in value else line['native_block'] in value['native_blocks'])]
            if not lines:
                raise ValueError('Empty exact native source group')
            groups.append({'group_id': value['group_id'], 'kind': value['kind'],
                'source_line_ids': [line['line_id'] for line in lines],
                'text_sha256': digest(' '.join(line['text'].strip() for line in lines).encode()),
                'reason': spec['reason'], **({'opens_section': value['opens_section']} if value.get('opens_section') else {})})
        reviewed_pages.append({'page': number, 'groups': groups})
    layout = {'schema': 'source-text-layout-review-v1', **meta, 'reviewer': spec['reviewer'], 'reason': spec['reason'],
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True, 'pages': reviewed_pages,
        'evidence': evidence, 'evidence_files': files, 'source_fidelity_approved': False,
        'remaining_uncertainties': spec['remaining_uncertainties'], 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    working, _ = prepare_flow_pages(old, pages, base / 'span-metrics-20261030-v1')
    applied = apply_layout_reviews(old, working, [layout])
    candidate = make_document({key: old[key] for key in ('paper_id', 'problem_type', 'year', 'queue_position',
        'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    groups = {block.get('layout_group_id'): block for block in candidate['blocks'] if block.get('layout_group_id')}
    operations = []
    for entry in spec['wrap_repairs']:
        block = groups[entry['group_id']]
        text = block['text']
        literal = []
        for change in entry['replacements']:
            before, after, count = change
            if text.count(before) != count:
                raise ValueError('Exact printed word-wrap preimage differs')
            changed = text.replace(before, after)
            op = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before, 'new': after, 'count': count,
                'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()), 'reason': spec['wrap_reason']}
            literal.append(op)
            operations.append(op)
            text = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
            'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(text.encode()),
            'transcription_operations_sha256': digest(encoded(literal)), 'reason': spec['wrap_reason']})
    repair = {**meta, 'reviewer': spec['reviewer'], 'checked_pages': spec['checked_pages'],
        'reason': spec['wrap_reason'], 'operations': operations, 'evidence': evidence,
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
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
    if (len(ids) != 1 or sum(block['kind'] != 'heading' for block in blocks) != spec['expected_author_paragraphs'] or
            {page for span in spans for page in span['pages']} != set(spec['abstract_pages']) or
            not text.startswith(spec['text_starts']) or not text.endswith(spec['text_ends']) or
            any(token not in text for token in spec['required_text']) or any(token in text for token in spec['forbidden_text'])):
        raise ValueError('Exact complete source Summary guards differ')
    signature = lambda document: [(block['source_line_ids'], block['text'], block['kind'], block['issues'])
        for block in all_author_blocks(document) if min(block['source_pages']) > max(spec['abstract_pages'])]
    if signature(old) != signature(candidate):
        raise ValueError('Later author text changed')
    sid = ids[0]
    source_review = {**meta, 'section_id': sid, 'text_sha256': digest(section_text(candidate, [sid]).encode()),
        'reviewer': spec['reviewer'], 'checked_pages': spec['checked_pages'],
        'section_boundaries_checked': True, 'paragraph_boundaries_checked': True,
        'paragraph_blocks': [block['block_id'] for block in section_blocks(candidate, [sid]) if block['kind'] != 'heading'],
        'evidence': {'findings': findings_path.name, 'specification': spec_path.name, 'layout': paths['layout'].name, 'literal_repairs': paths['word-repairs'].name},
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [source_review])
    wanted = {block['section_id'] for block in blocks}
    wanted_pages = {page for block in blocks for page in block['source_pages']}
    wanted_blocks = {block['block_id'] for block in blocks}
    pending = [item for item in candidate['defects'] if item.get('status') != 'resolved' and
               (item.get('section_id') in wanted or item.get('page') in wanted_pages or
                item.get('block_id') in wanted_blocks or item.get('left') in wanted_blocks or
                item.get('right') in wanted_blocks)]
    if pending or any(block.get('issues') for block in blocks):
        raise ValueError('Selected Summary retains unresolved source/page defects')
    for name, value in [('layout', layout), ('word-repairs', repair), ('source-review', source_review)]:
        json_new(paths[name], value)
    prepare_review_bundles([paths['layout']], identity_fields=('paper_id',), application_status='preflight only')
    prepare_review_bundles([paths['word-repairs']], identity_fields=('paper_id',), application_status='preflight only')
    result = {'paper_id': old['paper_id'], 'parent_dataset_id': catalog.identity, 'specification_sha256': file_hash(spec_path),
        'stager_sha256': file_hash(Path(__file__)), 'source_lines_accounted_once': True,
        'logical_author_paragraphs': spec['expected_author_paragraphs'], 'characters': len(text), 'text_sha256': digest(text.encode()),
        'literal_wrap_occurrences_repaired': sum(change[2] for entry in spec['wrap_repairs'] for change in entry['replacements']),
        'paragraph_hyphen_flags_resolved': sum(groups[entry['group_id']]['kind'] != 'keywords' for entry in spec['wrap_repairs']),
        'keyword_hyphen_flags_resolved': sum(groups[entry['group_id']]['kind'] == 'keywords' for entry in spec['wrap_repairs']),
        'selected_source_status': 'verified', 'later_author_text_unchanged': True,
        'section_boundaries_checked': True, 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0,
        'proof_sha256': {str(paths[name].resolve()): file_hash(paths[name]) for name in ('layout', 'word-repairs', 'source-review')}}
    json_new(paths['preflight'], result)
    write_new(preview, text + '\n')
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', type=Path, required=True)
    stage(parser.parse_args().spec.resolve())
