"""Individually restore q308's ten source-read prose/list units, preserving evidence."""
import copy
import json
from collections import Counter
from pathlib import Path
import sys

STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
RUNTIME = STORE / 'runtime-v39-20261031-v1'
sys.path.insert(0, str(RUNTIME / 'scripts'))
from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_ocr_page_reviews import apply_ocr_page_reviews, page_blocks_signature, validate_ocr_page_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, normalized_lines, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def main():
    directory = STORE / 'reviews/20261031'
    output = directory / 'q308-summary-restoration-v1'
    if output.exists():
        raise ValueError('Create-only output exists; preserve it')
    root, prepared_root = STORE / 'reflow-20261031-v41', STORE / 'reflow-20261031-v40'
    catalog, prepared_parent = Catalog(root), Catalog(prepared_root)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v41.json')
    if accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']:
        raise ValueError('Accepted v41 required')
    old = catalog.document('P-D-2021-2106028-e54d016e')
    previous, current = copy.deepcopy(prepared_parent.document(old['paper_id'])), copy.deepcopy(old)
    old_scope, new_scope = previous.pop('scope_id'), current.pop('scope_id')
    if previous != current or old_scope == new_scope:
        raise ValueError('Prepared page transfer must change scope only')
    if any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews')):
        raise ValueError('Existing source reviews require explicit replay')
    original, evidence_folder = directory / 'q308-summary-ocr-v1', directory / 'q308-opening-pages-v1'
    original_manifest, original_page = read_json(original / 'manifest.json'), read_json(original / 'page-0001.json')
    prepared = read_json(evidence_folder / 'manifest.json')
    raw_path = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    if (old['queue_position'] != 308 or old['page_count'] != 25
            or prepared['dataset_id'] != prepared_parent.identity
            or file_hash(source) != old['source_sha256']
            or file_hash(raw_path) != old['raw_pages_sha256']
            or old['raw_pages_sha256'] != '4ce17bbecb2baf695dcb63e5328934d9d1eee8348de4bd8e94ef041405b6bffd'
            or prepared['source_sha256'] != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256']
            or original_manifest['source_sha256'] != old['source_sha256']
            or len(original_page['lines']) != 43
            or file_hash(original / 'page-0001.json') != '8516b372db0fa7fdc32c2c0fd4d26294e480e4c0db7bbcbf70117b41652f3e74'
            or file_hash(original / 'page-0001.json') != original_manifest['pages'][0]['sha256']):
        raise ValueError('Exact source/native/OCR identity differs')
    for name, sha in prepared['files'].items():
        if file_hash(evidence_folder / name) != sha:
            raise ValueError('Actually read source evidence changed')
    pages = rows(raw_path)
    native = {line['line_id']: line for line in pages[0]['lines']}
    revised = copy.deepcopy(original_page)
    table = str.maketrans(dict(zip('ﬀﬁﬂﬃﬄﬅﬆ', ('ff', 'fi', 'fl', 'ffi', 'ffl', 'st', 'st'))))
    corrections = []
    for index, number in [(15, 14), (19, 16), (22, 17), (25, 18), (29, 19), (33, 20)]:
        lid = f'p0001-n{number:04d}-l0000'
        corrected = native[lid]['text'].translate(table)
        before = original_page['lines'][index]['text']
        if not corrected.startswith('• ') or before == corrected or before.replace(' ', '') != corrected[2:].replace(' ', ''):
            raise ValueError('Only source-read missing bullet/spacing expected')
        revised['lines'][index]['text'] = corrected
        corrections.append({'original_ocr_index': index, 'old_text': before,
            'source_transcription': corrected, 'corroborating_native_line_id': lid,
            'original_ocr_score_retained_as_original_only': original_page['lines'][index]['score'],
            'basis': 'Both complete source pages actually read;restore printed bullet and exact word spacing,expand only ordinary alphabetic ligatures.'})
    changed_indices = {item['original_ocr_index'] for item in corrections}
    if any(revised['lines'][i] != original_page['lines'][i] for i in range(43) if i not in changed_indices):
        raise ValueError('Other37 OCR line objects changed')
    revised['manual_source_transcriptions'] = corrections
    revised['review_status'] = 'Two opening paragraphs,seven complete bullets,closing,keywords and boundaries actually source-read;separate proof required.'
    output.mkdir(parents=True)
    findings = {'schema': 'source-prose-layout-findings-v2', 'paper_id': old['paper_id'],
        'source_sha256': old['source_sha256'], 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'reviewer': 'Codex root;2026-10-31;both complete source JPEGs,all native page1lines and all43OCRlines actually read',
        'checked_pages': [1, 2], 'logical_author_paragraphs': 10,
        'source_boundary': 'Page1Summary:two opening paragraphs,seven complete problem bullets,one closing.Separate form,two-line title,full two-line keywords and promotions.Page2title/Contents,no continuation.',
        'source_conflict': 'Native-versus-pdftotext automatic agreement unresolved;localOCR plus actual source adjudication,not automatic agreement,provides the acceptance proof.',
        'transcriptions': corrections, 'source_wraps': ['revolutions', 'evolution in keywords'],
        'presentation_ligatures': 'Ordinary alphabetic ligatures expanded;exact native evidence retained.All ten units must equal native prose under only this expansion and one checked author wrap.Printed bullet markers retained.',
        'preserved_wording': ['times goes by', 'influncers', 'representatives of revolutionary', 'possible influence of Internet'],
        'prepared_evidence_scope_transfer': {'old_scope_id': old_scope, 'new_scope_id': new_scope, 'all_other_paper_fields_equivalent': True},
        'scope_boundary': 'Prose and boundaries only;mentions of tables/charts/models are author text,not figure interpretation or formula correctness acceptance.',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    json_new(output / 'page-0001.json', revised)
    manifest = {**original_manifest, 'pages': [{'page': 1, 'path': 'page-0001.json',
        'sha256': file_hash(output / 'page-0001.json'), 'line_count': 43,
        'low_confidence_lines': sum(line['score'] < .95 for line in revised['lines'])}],
        'source_recovery': {'original_manifest_sha256': file_hash(original / 'manifest.json'),
            'original_page_sha256': file_hash(original / 'page-0001.json'), 'findings_sha256': file_hash(output / 'findings.json'),
            'only_changes': 'Six missing printed bullets and two associated spacing errors;all43boxes/scores and37other line objects unchanged.'}}
    json_new(output / 'manifest.json', manifest)
    prospective = copy.deepcopy(pages)
    first = prospective[0]
    if first.get('ocr_evidence') or not any('As the productivity has developed rapidly' in line['text'] for line in first['lines']):
        raise ValueError('Exact native q308 opening differs')
    for line in first['lines']:
        line['superseded_by_ocr'] = True
    for number, value in enumerate(revised['lines']):
        points = value['pdf_box']
        box = [min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)]
        first['lines'].append({'line_id': f'p0001-ocr-l{number:04d}', 'native_block': -1, 'page': 1,
            'bbox': box, 'text': value['text'], 'font_size': max(5, (box[3]-box[1])*.95),
            'bold': value['text'].strip().lower() in {'summary', 'abstract', 'introduction', 'contents'},
            'spans': [], 'ocr_score': value['score'], 'engine': 'rapidocr'})
    first['ocr_status'] = 'candidate'
    first['ocr_evidence'] = {'path': 'raw/ocr/page-0001.json', 'sha256': file_hash(output / 'page-0001.json'),
        'models': manifest['model_sha256'], 'version': manifest['ocr_version']}
    raw = b''.join((json.dumps(page, ensure_ascii=True, sort_keys=True) + '\n').encode() for page in prospective)
    write_new(output / 'prospective-pages.jsonl', raw)
    metrics = STORE / 'span-metrics-20261031-q306-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    working[0] = copy.deepcopy(first)
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    meta = {key: old[key] for key in keys}
    meta['raw_pages_sha256'] = digest(raw)
    identity = {key: meta[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': description,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, description in [
        (evidence_folder / 'manifest.json', evidence_folder, 'Both actually read opening source JPEGs and native evidence.'),
        (original / 'manifest.json', original, 'All43originalOCRlines,boxes and scores.'),
        (output / 'findings.json', None, 'Complete ten-unit prose/list source and conflict adjudication.'),
        (output / 'manifest.json', None, 'Source-adjudicated OCRmanifest.'),
        (output / 'page-0001.json', None, 'All43OCRline objects with original scores retained as original only.'),
        (Path(__file__), None, 'Individual create-only source restoration implementation.')]]
    files = {str(path): file_hash(path) for folder in (evidence_folder, original) for path in folder.iterdir() if path.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    by_id = {line['line_id']: line for line in first['lines']}
    definitions = [('form', 'front_matter', range(7)), ('title', 'title', [7, 8]), ('heading', 'heading', [9]),
        ('summary1', 'prose', range(10, 13)), ('summary2', 'prose', range(13, 15)),
        ('summary3', 'list', range(15, 17)), ('summary4', 'list', range(17, 19)),
        ('summary5', 'list', range(19, 22)), ('summary6', 'list', range(22, 25)),
        ('summary7', 'list', range(25, 29)), ('summary8', 'list', range(29, 33)),
        ('summary9', 'list', range(33, 36)), ('summary10', 'prose', range(36, 39)),
        ('keywords', 'keywords', [39, 40]), ('promotion', 'furniture', [41, 42])]
    groups = []
    for name, kind, numbers in definitions:
        ids = [f'p0001-ocr-l{i:04d}' for i in numbers]
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': ids,
            'text_sha256': digest(' '.join(by_id[lid]['text'].strip() for lid in ids).encode()),
            'reason': 'Actually source-read paragraph and non-author ownership.',
            **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'heading' else {})})
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': findings['reviewer'],
        'reason': 'Preserve two introductory paragraphs,seven printed list items and the complete closing;retain full keywords separately.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}],
        'evidence': evidence, 'evidence_files': files, 'remaining_uncertainties': ['Fresh25page native binding required.', 'Later chapter source acceptance pending.'],
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, prospective, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    blocks = {block.get('layout_group_id'): block for block in candidate['blocks']}
    replacements = {'summary7': [('vo- l', 'vol')], 'keywords': [('vo- l', 'vol')]}
    operations = []
    for group, pairs in replacements.items():
        block, literals = blocks[group], []
        text = block['text']
        for before, after in pairs:
            if text.count(before) != 1:
                raise ValueError('Exact source wrap differs:' + group + repr(text))
            changed = text.replace(before, after)
            operation = {'block_id': block['block_id'], 'operation': 'literal_replace', 'old': before, 'new': after,
                'count': 1, 'before_text_sha256': digest(text.encode()), 'after_text_sha256': digest(changed.encode()),
                'reason': 'Actually source-read discretionary wrap;retain genuine hyper-parameters compound.'}
            operations.append(operation); literals.append(operation); text = changed
        operations.append({'block_id': block['block_id'], 'operation': 'resolve_hyphen_join_review',
            'source_line_ids_sha256': digest(encoded(block['source_line_ids'])), 'before_text_sha256': digest(text.encode()),
            'after_text_sha256': digest(text.encode()), 'transcription_operations_sha256': digest(encoded(literals)),
            'reason': 'Every source-line wrap in this group individually checked.'})
    repair = {**identity, 'reviewer': findings['reviewer'], 'checked_pages': [1, 2],
        'reason': 'One author wrap and one separate keyword wrap;no author rewrite.', 'operations': operations,
        'evidence': evidence, 'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, prospective)
    actual = Counter(lid for block in candidate['blocks'] for lid in block['source_line_ids'])
    actual.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if actual != Counter(line['line_id'] for page in prospective for line in page['lines']) or any(count != 1 for count in actual.values()):
        raise ValueError('Every native/OCRline must have exactly one owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text = text_with_block_spans(selected)[0]
    ids = [sid for sid in ids if any(block['section_id'] == sid for block in selected)]
    table = str.maketrans(dict(zip('ﬀﬁﬂﬃﬄﬅﬆ', ('ff', 'fi', 'fl', 'ffi', 'ffl', 'st', 'st'))))
    native_paras = [normalized_lines([line for line in pages[0]['lines'] if line['native_block'] == n])[0].translate(table)
        for n in range(12, 22)]
    for group, pairs in replacements.items():
        if group == 'keywords':
            continue
        at = int(group.removeprefix('summary')) - 1
        for before, after in pairs:
            native_paras[at] = native_paras[at].replace(before, after)
    expected = 'Summary\n\n' + '\n\n'.join(native_paras)
    if (text != expected or len(ids) != 1 or sum(block['kind'] != 'heading' for block in selected) != 10
            or {page for block in selected for page in block['source_pages']} != {1}
            or any(value not in text for value in ['influncers', 'acousticness and valence', 'Nat King Cole and The Beatles', 'possible influence of Internet'])
            or any(value in text for value in ['Summary Sheet', 'MCM/ICM', 'Keywords:', '关注'])
            or any(block['text'].strip() == 'dex.' for block in selected)):
        raise ValueError('Complete original-native prose equality or boundary guard failed')
    later = lambda doc: [(block['source_line_ids'], block['text'], block['kind'], block['issues']) for block in all_author_blocks(doc) if min(block['source_pages']) > 1]
    if later(old) != later(candidate):
        raise ValueError('Later author body changed')
    proof = {'schema': 'source-checked-ocr-prose-page-v1', 'page': 1,
        'all_page_prose_and_boundaries_actually_read': True, 'resolved_codes': ['cross_engine_review', 'ocr_candidate_source_review'],
        'raw_page_sha256': digest(encoded(first)), 'layout_groups_sha256': digest(encoded(groups)),
        'final_page_blocks_sha256': digest(encoded(page_blocks_signature(candidate, 1))),
        'reviewed_page_jpeg_sha256': prepared['files']['page-0001.jpg'], 'reviewed_page_jpeg_bytes': 358601}
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': findings['reviewer'], 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True, 'paragraph_blocks': [block['block_id'] for block in section_blocks(candidate, ids) if block['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'word-repairs.json'},
        'ocr_prose_page_reviews': [proof], 'section_source_fidelity_approved': True,
        'whole_paper_source_acceptance': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review]); apply_ocr_page_reviews(candidate, prospective)
    validate_ocr_page_reviews(candidate, prospective)
    if any(defect.get('page') == 1 and defect.get('status') != 'resolved' for defect in candidate['defects']):
        raise ValueError('Source-checked page retains pending flags')
    json_new(output / 'layout.json', layout); json_new(output / 'word-repairs.json', repair); json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='prospective source-checked prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n'); json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'characters': len(text), 'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 10,
        'original_ocr_lines': 43, 'unchanged_ocr_line_objects': 37, 'manually_source_transcribed_lines': [15,19,22,25,29,33],
        'literal_wrap_occurrences_repaired': 2, 'author_wraps_repaired': 1, 'separate_keyword_wraps_repaired': 1,
        'complete_native_prose_equal_after_declared_ligature_expansion_and_wraps': True,
        'source_lines_accounted_once': True, 'later_actual_author_body_unchanged': True,
        'selected_source_status': 'verified in prospective stage only', 'native_metric_binding_transfer_still_required': True,
        'new_ocr_override_not_yet_in_any_corpus': True, 'span_metrics_source_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['manifest.json', 'page-0001.json', 'findings.json',
            'layout.json', 'word-repairs.json', 'source-review.json', 'summary-preview.md', 'prospective-pages.jsonl']},
        'stager_sha256': file_hash(Path(__file__)), 'library_sha256': file_hash(RUNTIME / 'scripts/text_corpus.py'),
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True); print(result, flush=True)


if __name__ == '__main__':
    main()
