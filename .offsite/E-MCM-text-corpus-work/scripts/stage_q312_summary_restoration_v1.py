"""Restore q312's five individually source-read paragraphs, create-only."""
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
    output = directory / 'q312-summary-restoration-v1'
    if output.exists():
        raise ValueError('Create-only output exists; preserve it')
    root = STORE / 'reflow-20261031-v43'
    catalog = Catalog(root)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v43.json')
    if accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']:
        raise ValueError('Require acceptedv43')
    old = catalog.document('P-D-2021-2124668-12f9e4f1')
    if any(old.get(k) for k in ('layout_reviews', 'text_repair_reviews', 'paragraph_join_reviews')):
        raise ValueError('Existing reviews require explicit replay')
    original = directory / 'q312-summary-ocr-v1'
    evidence_folder = directory / 'q312-opening-pages-v1'
    original_manifest = read_json(original / 'manifest.json')
    original_page = read_json(original / 'page-0001.json')
    prepared = read_json(evidence_folder / 'manifest.json')
    raw_path = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    if (old['queue_position'] != 312 or old['page_count'] != 23
            or prepared['dataset_id'] != catalog.identity
            or old['raw_pages_sha256'] != '96549295d43e6d24cb33130dc8cd543e5984648a8045a243807ea83e160d762d'
            or file_hash(source) != old['source_sha256'] or file_hash(raw_path) != old['raw_pages_sha256']
            or prepared['source_sha256'] != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256']
            or original_manifest['source_sha256'] != old['source_sha256']
            or len(original_page['lines']) != 34
            or file_hash(original / 'page-0001.json') != 'a31403ddf9d7f4c252e3d5d53a6e83d61ebf846ebeddfc73338a733a8c857540'
            or file_hash(original / 'page-0001.json') != original_manifest['pages'][0]['sha256']):
        raise ValueError('Exact source/native/OCR identity differs')
    for name, sha in prepared['files'].items():
        if file_hash(evidence_folder / name) != sha:
            raise ValueError('Actually read source evidence changed')
    pages = rows(raw_path)
    revised = copy.deepcopy(original_page)
    edits = [(4, '9o', '90'), (6, 'Ourkey', 'Our key'), (13, 'genres,"', 'genres,”'),
             (18, '"sonic genres,"', '“sonic genres,”'), (22, "genre's", 'genre’s'),
             (26, '196os', '1960s'), (29, 'genres,"', 'genres,”')]
    corrections = []
    for at, before, after in edits:
        line = revised['lines'][at]
        if line['text'].count(before) != 1:
            raise ValueError('Exact OCR transcription preimage differs')
        previous = line['text']
        line['text'] = previous.replace(before, after)
        corrections.append({'ocr_index': at, 'before': previous, 'after': line['text'],
            'reason': 'Actually read complete source page and matching native line;source transcription only.'})
    for at, (before, after) in enumerate(zip(original_page['lines'], revised['lines'])):
        first, second = copy.deepcopy(before), copy.deepcopy(after)
        first.pop('text'); second.pop('text')
        if first != second or (at not in [x[0] for x in edits] and before != after):
            raise ValueError('All boxes/scores and27other original line objects must remain unchanged')
    revised['manual_source_transcriptions'] = corrections
    revised['review_status'] = 'All five paragraphs and both source pages actually read;seven line transcriptions preserve original boxes/scores;separate proof required.'
    output.mkdir(parents=True)
    reviewer = 'Codex root;2026-10-31;both complete source JPEGs,all nativep1lines and all34OCRlines actually read'
    findings = {'schema': 'source-prose-layout-findings-v2', 'paper_id': old['paper_id'],
        'source_sha256': old['source_sha256'], 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'reviewer': reviewer, 'checked_pages': [1, 2], 'logical_author_paragraphs': 5,
        'source_boundary': 'Page1Summary contains five complete author paragraphs.No Keywords printed.Team and citedGilScott-Heronfootnote separate.Page2title,subtitle,team,Contents andProblemStatementare outside Summary;no continuation.',
        'source_conflict': 'Native-versus-pdftotext comparison unresolved;localOCR plus actual source adjudication,not automatic agreement,provides acceptance proof.',
        'transcriptions': corrections, 'source_wraps': [],
        'presentation_ligatures': 'Ordinary alphabetic ligatures expanded;complete prose equals native under only that expansion.Original native evidence retained.',
        'source_ownership': {'ocr_index1': 'team front matter', 'ocr_index31': 'cited bibliographic footnote;retained as references,not original-team prose', 'ocr_indices32_33': 'third-party promotion'},
        'preserved_wording': ['21st century music', 'This failure inspired us', 'We also speculated', 'Q = 0.17'],
        'scope_boundary': 'Author prose and boundaries only;inline Qvalue retained without formula correctness or chart interpretation.',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    json_new(output / 'page-0001.json', revised)
    manifest = {**original_manifest, 'pages': [{'page': 1, 'path': 'page-0001.json',
        'sha256': file_hash(output / 'page-0001.json'), 'line_count': 34,
        'low_confidence_lines': sum(line['score'] < .95 for line in revised['lines'])}],
        'source_recovery': {'original_manifest_sha256': file_hash(original / 'manifest.json'),
            'original_page_sha256': file_hash(original / 'page-0001.json'), 'findings_sha256': file_hash(output / 'findings.json'),
            'only_changes': 'Seven source-read text transcriptions;all34originalboxes/scores and27otherlineobjects unchanged.Original confidence scores are not estimates for corrected text.'}}
    json_new(output / 'manifest.json', manifest)
    prospective = copy.deepcopy(pages)
    first = prospective[0]
    if first.get('ocr_evidence') or not any('From trained musicologists' in line['text'] for line in first['lines']):
        raise ValueError('Exact native opening differs')
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
    metrics = STORE / 'span-metrics-20261031-q311-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    working[0] = copy.deepcopy(first)
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    meta = {key: old[key] for key in keys}
    meta['raw_pages_sha256'] = digest(raw)
    identity = {key: meta[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': description,
        **({'bundle_root': str(bundle)} if bundle else {})} for path, bundle, description in [
        (evidence_folder / 'manifest.json', evidence_folder, 'Both actually read opening source JPEGs and native evidence.'),
        (original / 'manifest.json', original, 'All34originalOCRlines,boxes,scores and texts.'),
        (output / 'findings.json', None, 'Complete five-paragraph source/conflict adjudication.'),
        (output / 'manifest.json', None, 'Source-adjudicated OCRmanifest.'),
        (output / 'page-0001.json', None, 'Seven source transcriptions;all original boxes/scores retained.'),
        (Path(__file__), None, 'Individual create-only source restoration implementation.')]]
    files = {str(path): file_hash(path) for folder in (evidence_folder, original) for path in folder.iterdir() if path.is_file()}
    files.update({item['path']: item['sha256'] for item in evidence})
    by_id = {line['line_id']: line for line in first['lines']}
    definitions = [('heading', 'heading', [0]), ('team', 'front_matter', [1]),
        ('summary1', 'prose', range(2, 5)), ('summary2', 'prose', range(5, 9)),
        ('summary3', 'prose', range(9, 16)), ('summary4', 'prose', range(16, 24)),
        ('summary5', 'prose', range(24, 31)), ('reference', 'source_object', [31]),
        ('promotion', 'furniture', [32, 33])]
    groups = []
    for name, kind, numbers in definitions:
        ids = [f'p0001-ocr-l{i:04d}' for i in numbers]
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': ids,
            'text_sha256': digest(' '.join(by_id[lid]['text'].strip() for lid in ids).encode()),
            'reason': 'Actually source-read paragraph and separate cited-reference/non-author ownership.',
            **({'opens_section': {'role': 'abstract', 'level': 1}} if name == 'heading' else {})})
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': reviewer,
        'reason': 'Restore five complete author paragraphs and exact Summaryboundary;retain team,cited footnote and promotion separately.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True,
        'pages': [{'page': 1, 'groups': groups}], 'evidence': evidence, 'evidence_files': files,
        'remaining_uncertainties': ['Fresh23page native binding required.', 'Later chapter source acceptance pending.'],
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, prospective, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    reference = next(block for block in candidate['blocks'] if block.get('layout_group_id') == 'reference')
    repair = {**identity, 'reviewer': reviewer, 'checked_pages': [1, 2],
        'reason': 'Retain printed cited footnote separately from original-team prose;no author rewrite.',
        'operations': [{'block_id': reference['block_id'], 'operation': 'classify',
            'from_kind': 'source_object', 'to_kind': 'references',
            'before_text_sha256': digest(reference['text'].encode()), 'after_text_sha256': digest(reference['text'].encode()),
            'reason': 'Source-read GilScott-Heron bibliographic footnote;retain literal reference,exclude from default imitation.'}],
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
        for n in range(6, 11)]
    expected = 'SUMMARY\n\n' + '\n\n'.join(native_paras)
    if (text != expected or len(ids) != 1 or sum(block['kind'] != 'heading' for block in selected) != 5
            or {page for block in selected for page in block['source_pages']} != {1}
            or any(value not in text for value in ['90 years', 'Our key metric', '1960s', 'This failure inspired us', 'We also speculated', 'genre’s centroid'])
            or any(value in text for value in ['TEAM 2124668', 'Gil Scott-Heron', '关注', 'Contents', 'Problem Statement'])):
        raise ValueError('Complete original-native equality or boundary guard failed')
    later = lambda doc: [(block['source_line_ids'], block['text'], block['kind'], block['issues']) for block in all_author_blocks(doc) if min(block['source_pages']) > 1]
    if later(old) != later(candidate):
        raise ValueError('Later author body changed')
    proof = {'schema': 'source-checked-ocr-prose-page-v1', 'page': 1,
        'all_page_prose_and_boundaries_actually_read': True, 'resolved_codes': ['cross_engine_review', 'ocr_candidate_source_review'],
        'raw_page_sha256': digest(encoded(first)), 'layout_groups_sha256': digest(encoded(groups)),
        'final_page_blocks_sha256': digest(encoded(page_blocks_signature(candidate, 1))),
        'reviewed_page_jpeg_sha256': prepared['files']['page-0001.jpg'], 'reviewed_page_jpeg_bytes': 360827}
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': reviewer, 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True,
        'paragraph_blocks': [block['block_id'] for block in section_blocks(candidate, ids) if block['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json', 'repairs': 'reference-classification.json'},
        'ocr_prose_page_reviews': [proof], 'section_source_fidelity_approved': True,
        'whole_paper_source_acceptance': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review]); apply_ocr_page_reviews(candidate, prospective)
    validate_ocr_page_reviews(candidate, prospective)
    if any(defect.get('page') == 1 and defect.get('status') != 'resolved' for defect in candidate['defects']):
        raise ValueError('Source-checked page retains pending flags')
    json_new(output / 'layout.json', layout); json_new(output / 'reference-classification.json', repair)
    json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='prospective source-checked prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n'); json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'characters': len(text), 'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 5,
        'original_ocr_lines': 34, 'unchanged_ocr_line_objects': 27,
        'manually_source_transcribed_lines': [x[0] for x in edits], 'original_boxes_and_scores_unchanged': 34,
        'author_wraps_repaired': 0, 'separate_reference_blocks': 1,
        'complete_native_prose_equal_after_declared_ligature_expansion': True,
        'source_lines_accounted_once': True, 'later_actual_author_body_unchanged': True,
        'selected_source_status': 'verified in prospective stage only', 'native_metric_binding_transfer_still_required': True,
        'new_ocr_override_not_yet_in_any_corpus': True, 'span_metrics_source_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['manifest.json', 'page-0001.json', 'findings.json',
            'layout.json', 'reference-classification.json', 'source-review.json', 'summary-preview.md', 'prospective-pages.jsonl']},
        'stager_sha256': file_hash(Path(__file__)), 'library_sha256': file_hash(RUNTIME / 'scripts/text_corpus.py'),
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True); print(result, flush=True)


if __name__ == '__main__':
    main()
