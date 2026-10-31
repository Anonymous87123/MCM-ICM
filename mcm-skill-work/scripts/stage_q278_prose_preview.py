"""Create-only q278 prose restoration; retain a source-printed anomaly unresolved."""
from collections import Counter
from pathlib import Path

from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from resegment_text_corpus import resolve_exact_comparisons
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, text_with_block_spans, write_new


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    root = base / 'reflow-20261031-v34'
    parent = '3d6bf77d7c11927af409b69eae31073f26d5df6426e82d56c541fd9e6ec85d9e'
    pid = 'P-D-2016-44173-aa1c9913'
    directory = base / 'reviews/20261031'
    output = directory / 'q278-prose-preview-v1'
    if output.exists():
        raise ValueError('Preserve existing preview; create-only output')
    catalog = Catalog(root)
    if catalog.identity != parent:
        raise ValueError('Exact accepted parent required')
    old = catalog.document(pid)
    if old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews'):
        raise ValueError('Existing proof needs explicit replay')
    meta = {key: old[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    folder = directory / 'q278-native-source-pages-v2'
    manifest_path = folder / 'manifest.json'
    findings_path = directory / 'q278-opening-findings-v1.json'
    manifest, findings = read_json(manifest_path), read_json(findings_path)
    raw = root / 'papers' / pid / 'raw/pages.jsonl'
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    if (any(manifest[k] != v or findings[k] != v for k, v in meta.items()) or
            file_hash(raw) != meta['raw_pages_sha256'] or file_hash(source) != meta['source_sha256']):
        raise ValueError('Inspected source identity changed')
    for name, sha in manifest['files'].items():
        if file_hash(folder / name) != sha:
            raise ValueError('Prepared native or image evidence changed')
    for name, sha in findings['checked_jpeg_sha256'].items():
        if file_hash(folder / name) != sha or (folder / name).stat().st_size > 450000:
            raise ValueError('Actually inspected bounded JPEG differs')
    if not findings['source_anomalies'] or findings['section_source_fidelity_approved']:
        raise ValueError('Source-printed uncertainty must remain open')
    evidence = [
        {'path': str(findings_path), 'sha256': file_hash(findings_path), 'description': 'Actual source prose/layout review; malformed printed possessive remains unresolved.'},
        {'path': str(manifest_path), 'sha256': file_hash(manifest_path), 'bundle_root': str(folder), 'description': 'Native lines and both actually inspected bounded opening JPEGs.'},
        {'path': str(Path(__file__)), 'sha256': file_hash(Path(__file__)), 'description': 'Exact one-paper layout and four word-wrap preimages; no fidelity approval.'}]
    files = {str(path): file_hash(path) for path in folder.iterdir() if path.is_file()}
    files.update({proof['path']: proof['sha256'] for proof in evidence})
    pages = rows(raw)
    native = pages[0]['lines']
    if len(native) != 44:
        raise ValueError('Exact reviewed page has 44 native lines')

    def group(gid, kind, ids, opening=None):
        chosen = [line for lid in ids for line in native if line['line_id'] == lid]
        if len(chosen) != len(ids):
            raise ValueError('Native lane missing')
        value = {'group_id': gid, 'kind': kind, 'source_line_ids': ids,
                 'text_sha256': digest(' '.join(line['text'].strip() for line in chosen).encode()),
                 'reason': 'Source-checked complete page ownership; five author paragraphs, separate template/title.'}
        if opening:
            value['opens_section'] = opening
        return value

    by_block = lambda number: [line['line_id'] for line in native if line['native_block'] == number]
    groups = [group('office-form', 'front_matter', [line['line_id'] for line in native if line['native_block'] <= 4]),
              group('printed-summary-banner', 'front_matter', ['p0001-n0005-l0000']),
              group('template-instruction', 'front_matter', ['p0001-n0005-l0001']),
              group('paper-title', 'title', ['p0001-n0006-l0000']),
              group('opening', 'prose', by_block(6)[1:]),
              *[group(name, 'prose', by_block(number)) for name, number in [('first', 7), ('second', 8), ('third', 9), ('finally', 10)]]]
    layout = {'schema': 'source-text-layout-review-v1', **meta, 'reviewer': findings['reviewer'],
              'reason': 'Restore all five author paragraphs while retaining the printed source anomaly unresolved.',
              'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
              'pages': [{'page': 1, 'groups': groups}], 'evidence': evidence, 'evidence_files': files,
              'source_fidelity_approved': False, 'remaining_uncertainties': findings['source_anomalies'],
              'formula_verification': 'paused', 'figure_distillation': 'paused'}
    working, _ = prepare_flow_pages(old, pages, base / 'span-metrics-20261030-v1')
    applied = apply_layout_reviews(old, working, [layout])
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    candidate = make_document({key: old[key] for key in keys}, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (root / 'papers' / pid / 'raw/pdftotext.bin').read_bytes())
    by_group = {block.get('layout_group_id'): block for block in candidate['blocks'] if block.get('layout_group_id')}
    operations = []
    for name, changes in [('first', [('me- dia', 'media')]), ('third', [('n- i', 'ni'), ('t- s', 'ts'), ('r- m', 'rm')])]:
        block = by_group[name]
        text, literals = block['text'], []
        for before, after in changes:
            if text.count(before) != 1:
                raise ValueError('Exact checked word-wrap differs')
            changed = text.replace(before, after)
            op = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before, 'new': after, 'count': 1,
                  'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
                  'reason': 'Exact printed discretionary line wrap; preserve all other characters.'}
            operations.append(op)
            literals.append(op)
            text = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
                           'source_line_ids_sha256': digest(encoded(block['source_line_ids'])),
                           'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(text.encode()),
                           'transcription_operations_sha256': digest(encoded(literals)),
                           'reason': 'All discretionary line wraps in this paragraph checked against source.'})
    repair = {**meta, 'reviewer': findings['reviewer'], 'checked_pages': [1, 2],
              'reason': 'Four exact word wraps only; do not repair the malformed printed possessive by guessing.',
              'operations': operations, 'evidence': evidence, 'source_fidelity_approved': False,
              'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    retained = [block for block in candidate['blocks'] if block.get('layout_group_id') and block['source_pages'] == [1]]
    for block, declared in zip(retained, groups):
        if (block['layout_group_id'] != declared['group_id'] or
                block.get('pre_repair_kind', block['kind']) != declared['kind'] or
                block['source_line_ids'] != declared['source_line_ids']):
            raise ValueError(f"Exact lane differs: {declared['group_id']}, wanted {declared['kind']}, got {block['layout_group_id']}/{block.get('pre_repair_kind', block['kind'])}")
    validate_layout_reviews(candidate, pages)
    actual = Counter(lid for block in candidate['blocks'] for lid in block['source_line_ids'])
    actual.update(line['line_id'] for line in candidate['excluded_source_lines'])
    expected = Counter(line['line_id'] for page in pages for line in page['lines'])
    if actual != expected or any(count != 1 for count in actual.values()):
        raise ValueError('Source ownership lost or duplicated')
    ids, excluded = select_sections(candidate, 'abstract')
    blocks = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text, spans = text_with_block_spans(blocks)
    paragraphs = [block for block in blocks if block['kind'] != 'heading']
    anomaly = 'people ˛a´rs initial opinion'
    if (len(paragraphs) != 5 or text.count(anomaly) != 1 or "people's" in text or
            not text.startswith('The ﬂow of information') or not text.endswith('certain extent.') or
            {page for span in spans for page in span['pages']} != {1} or
            any(part in text for part in ['For ofﬁce', 'Attach a copy', 'How to Understand'])):
        raise ValueError('Complete five-paragraph preview/source anomaly guard failed')
    signature = lambda document: [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(document) if min(b['source_pages']) > 1]
    if signature(old) != signature(candidate):
        raise ValueError('Later author text changed')
    if candidate.get('source_reviews') or any(s.get('source_fidelity_approved') for s in candidate['sections']):
        raise ValueError('Preview must not gain source approval')
    result = {**meta, 'parent_dataset_id': parent, 'source_lines_accounted_once': True,
              'source_template_banner': '2016 Mathematical Contest in Modeling (MCM) Summary Sheet',
              'author_abstract_heading': None, 'heading_status': 'Untitled author summary under a template banner; no author heading invented.',
              'logical_author_paragraphs': 5, 'characters': len(text), 'text_sha256': digest(text.encode()),
              'literal_wrap_occurrences_repaired': 4, 'later_author_text_unchanged': True,
              'source_anomalies': findings['source_anomalies'], 'selected_source_status': 'present-unverified',
              'section_source_fidelity_approved': False, 'whole_paper_source_acceptance': False,
              'ai_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    output.mkdir()
    for name, value in [('layout', layout), ('word-repairs', repair), ('candidate', candidate), ('preflight', result)]:
        json_new(output / (name + '.json'), value)
    write_new(output / 'abstract-preview.md', text + '\n')
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
