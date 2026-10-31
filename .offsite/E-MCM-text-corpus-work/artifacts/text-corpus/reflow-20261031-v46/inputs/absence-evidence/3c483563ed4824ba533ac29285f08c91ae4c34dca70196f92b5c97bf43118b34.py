"""Recover all four q286Summaryparagraphs; originals and existing runs unchanged."""
import copy
import json
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
from source_ocr_page_reviews import apply_ocr_page_reviews, page_blocks_signature, validate_ocr_page_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def main():
    base = WORK / 'artifacts/text-corpus'
    directory = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus\reviews\20261031')
    output = directory / 'q286-summary-restoration-v1'
    if output.exists():
        raise ValueError('Create-only stage exists; preserve it')
    root = base / 'reflow-20261031-v34'
    catalog = Catalog(root)
    old = catalog.document('P-D-2017-68942-f0b0893e')
    if old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews'):
        raise ValueError('Existing source proof requires explicit replay')
    original = base / 'reviews/20261031/q286-summary-ocr-v1'
    original_manifest = read_json(original / 'manifest.json')
    original_page = read_json(original / 'page-0001.json')
    page_evidence = base / 'reviews/20261031/q286-opening-pages-v1'
    prepared = read_json(page_evidence / 'manifest.json')
    crop_folder = directory / 'q286-prose-crops-v1'
    crop = read_json(crop_folder / 'result.json')
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    raw_path = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    if (catalog.identity != '3d6bf77d7c11927af409b69eae31073f26d5df6426e82d56c541fd9e6ec85d9e' or
            file_hash(source) != old['source_sha256'] or file_hash(raw_path) != old['raw_pages_sha256'] or
            original_manifest['source_sha256'] != old['source_sha256'] or
            prepared['source_sha256'] != old['source_sha256'] or prepared['raw_pages_sha256'] != old['raw_pages_sha256'] or
            crop['source_sha256'] != old['source_sha256'] or crop['raw_pages_sha256'] != old['raw_pages_sha256'] or
            crop['model_sha256'] != original_manifest['model_sha256'] or len(original_page['lines']) != 51 or
            file_hash(original / 'page-0001.json') != original_manifest['pages'][0]['sha256']):
        raise ValueError('Exact inspected PDF/native/OCR/crop identity differs')
    for name, sha in prepared['files'].items():
        if file_hash(page_evidence / name) != sha:
            raise ValueError('Actually inspected source image/native evidence changed')
    for entry in crop['crops']:
        index = entry['original_ocr_index']
        if (file_hash(crop_folder / f'line-{index:02d}.jpg') != entry['proxy_sha256'] or
                (crop_folder / f'line-{index:02d}.jpg').stat().st_size != entry['proxy_bytes']):
            raise ValueError('Actually inspected focused image changed')
    exact_line = 'typical security checkpoint. Our model divided the current screening process into individual components'
    if (crop['crops'][0]['lines'] != [{'text': exact_line, 'score': 0.9957}] or
            original_page['lines'][30]['text'] != 'ypn os os snd s    o n d ns adnts' or
            original_page['lines'][37]['text'].count('signifieant') != 1):
        raise ValueError('Exact two source-transcription preimages differ')
    revised = copy.deepcopy(original_page)
    revised['lines'][30]['text'] = exact_line
    revised['lines'][37]['text'] = revised['lines'][37]['text'].replace('signifieant', 'significant')
    corrections = [{'original_ocr_index': index, 'old_text': original_page['lines'][index]['text'],
        'source_transcription': revised['lines'][index]['text'],
        'original_ocr_score_retained_as_original_only': original_page['lines'][index]['score'],
        'basis': 'Actually inspected full source page and exact focused JPEG; recognition output is supporting evidence,not an automatic approval.'}
        for index in (30, 37)]
    if any(revised['lines'][i] != original_page['lines'][i] for i in range(51) if i not in {30, 37}):
        raise ValueError('Other49OCRline objects changed')
    revised['manual_source_transcriptions'] = corrections
    revised['review_status'] = 'Complete prose and source page boundaries actually read; separate acceptance proof required.'
    output.mkdir(parents=True)
    findings = {'schema': 'source-prose-layout-findings-v2', 'paper_id': old['paper_id'],
        'source_sha256': old['source_sha256'], 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'reviewer': 'Codex root;2026-10-31;both complete opening JPEGs,two focused source-line JPEGs and all51OCRlines actually read',
        'checked_pages': [1, 2], 'paragraphs': ['objective/NetLogoagent model', 'three bottlenecks', 'modifications/behavior', 'closing purpose'],
        'source_boundary': 'Four untitled author Summaryparagraphs onphysicalpage1under the competition template. Page2has a separate paper title followed by1Introduction;no summary continuation.',
        'transcriptions': corrections, 'preserved_claims': ['Internal Control Management(ICM)wording', 'approx3orlesssecondsperpassenger', 'over99percentvarianceandlength', 'standarddeviationtopping30minutes', 'up16percentthroughput', '33percentvariance reduction', 'behavior penalties less severe than expected'],
        'excluded_source': ['browser Print/Close/date/header/URL/footer', 'competition scoring form and instructions', 'separate page2paper title'],
        'scope_boundary': 'Page2image was used for text title/Introduction boundary only;no figure interpretation or formula verification.',
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    json_new(output / 'page-0001.json', revised)
    manifest = {**original_manifest, 'pages': [{'page': 1, 'path': 'page-0001.json', 'sha256': file_hash(output / 'page-0001.json'),
        'line_count': 51, 'low_confidence_lines': sum(line['score'] < .95 for line in revised['lines'])}],
        'source_recovery': {'original_manifest_sha256': file_hash(original / 'manifest.json'),
            'original_page_sha256': file_hash(original / 'page-0001.json'), 'findings_sha256': file_hash(output / 'findings.json'),
            'only_changes': 'Two manually source-checked line texts;all51original coordinates/confidence scores retained and49other line objects unchanged.'}}
    json_new(output / 'manifest.json', manifest)
    pages = rows(raw_path)
    prospective = copy.deepcopy(pages)
    first = prospective[0]
    if len(first['lines']) != 1 or first['lines'][0]['text'].strip() or first.get('ocr_evidence'):
        raise ValueError('Exact native-empty opening page required')
    first['lines'][0]['superseded_by_ocr'] = True
    for index, value in enumerate(revised['lines']):
        points = value['pdf_box']
        box = [min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)]
        first['lines'].append({'line_id': f'p0001-ocr-l{index:04d}', 'native_block': -1, 'page': 1,
            'bbox': box, 'text': value['text'], 'font_size': max(5, (box[3]-box[1])*.95),
            'bold': value['text'].strip().lower() in {'summary', 'abstract', 'introduction', 'contents'},
            'spans': [], 'ocr_score': value['score'], 'engine': 'rapidocr'})
    first['ocr_status'] = 'candidate'
    first['ocr_evidence'] = {'path': 'raw/ocr/page-0001.json', 'sha256': file_hash(output / 'page-0001.json'),
                             'models': manifest['model_sha256'], 'version': manifest['ocr_version']}
    raw = b''.join((json.dumps(page, ensure_ascii=True, sort_keys=True) + '\n').encode() for page in prospective)
    write_new(output / 'prospective-pages.jsonl', raw)
    working, _ = prepare_flow_pages(old, pages, base / 'span-metrics-20261031-q267-v2')
    working[0] = copy.deepcopy(first)
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    meta = {key: old[key] for key in keys}
    meta['raw_pages_sha256'] = digest(raw)
    identity = {key: meta[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': description, **({'bundle_root': str(bundle)} if bundle else {})}
        for path, bundle, description in [
            (page_evidence / 'manifest.json', page_evidence, 'Both actually inspected complete bounded source JPEGs plus untouched native lines.'),
            (original / 'manifest.json', original, 'Original51line localOCRincluding all original boxes,scores and failed line30.'),
            (crop_folder / 'result.json', crop_folder, 'Two actually inspected focused JPEGs and local recognition results.'),
            (output / 'findings.json', None, 'Complete source paragraph and boundary findings with explicit two-line human transcriptions.'),
            (output / 'manifest.json', None, 'Versioned source-adjudicated OCRmanifest;original source remains unchanged.'),
            (output / 'page-0001.json', None, 'Exact revised51line page with original scores explicitly retained as original only.'),
            (Path(__file__), None, 'Exact create-only one-paper staging implementation.')]]
    files = {str(path): file_hash(path) for folder in (page_evidence, original, crop_folder) for path in folder.iterdir() if path.is_file()}
    files.update({proof['path']: proof['sha256'] for proof in evidence})
    by_id = {line['line_id']: line for line in first['lines']}
    groups = []
    for name, kind, numbers in [('form-browser', 'front_matter', range(25)), ('summary1', 'prose', range(25, 35)),
                                ('summary2', 'prose', range(35, 41)), ('summary3', 'prose', range(41, 47)),
                                ('summary4', 'prose', range(47, 49)), ('browser-footer', 'furniture', range(49, 51))]:
        ids = [f'p0001-ocr-l{index:04d}' for index in numbers]
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': ids,
                       'text_sha256': digest(' '.join(by_id[lid]['text'].strip() for lid in ids).encode()),
                       'reason': 'Exact source-checked four-paragraph Summary;browser/form material retained separately.'})
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': findings['reviewer'],
        'reason': 'Recover complete native-empty Summary;no title-only substitute and no author heading invented.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}],
        'evidence': evidence, 'evidence_files': files, 'remaining_uncertainties': ['Native-metric binding transfer still required.', 'All later author chapters pending.'],
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, prospective, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    title = 'Optimizing Passenger Throughput at an Airport Security Checkpoint'
    title_blocks = [b for b in candidate['blocks'] if b['text'] == title and b['source_pages'] == [2]]
    if len(title_blocks) != 1 or title_blocks[0]['kind'] != 'prose':
        raise ValueError('Exact separately printed page2title preimage differs')
    title_block = title_blocks[0]
    repair = {**identity, 'reviewer': findings['reviewer'], 'checked_pages': [1, 2],
        'reason': 'Separate actually inspected two-line paper title from Summary;do not alter its text or surrounding Introduction.',
        'operations': [{'block_id': title_block['block_id'], 'operation': 'classify', 'from_kind': 'prose', 'to_kind': 'title',
            'before_text_sha256': digest(title.encode()), 'after_text_sha256': digest(title.encode()),
            'reason': 'Separate two-line page2paper title above1Introduction,not Summary prose.'}],
        'evidence': evidence, 'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_text_repairs(candidate, [repair])
    validate_layout_reviews(candidate, prospective)
    actual = Counter(lid for b in candidate['blocks'] for lid in b['source_line_ids'])
    actual.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if actual != Counter(line['line_id'] for page in prospective for line in page['lines']) or any(count != 1 for count in actual.values()):
        raise ValueError('Every native/OCRline must retain exactly one source owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text = text_with_block_spans(selected)[0]
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    if (len(ids) != 1 or len(selected) != 4 or {p for b in selected for p in b['source_pages']} != {1} or
            not text.startswith('The objective of our Internal Control Management (ICM) team') or
            not text.endswith("how to resolve one of travelling's biggest issues.") or
            exact_line not in text or 'three significant bottlenecks' not in text or title in text):
        raise ValueError('Complete four-paragraph author Summary guard failed')
    signature = lambda doc: [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(doc)
                             if min(b['source_pages']) > 1 and b['source_line_ids'] != title_block['source_line_ids']]
    if signature(old) != signature(candidate):
        raise ValueError('Later actual author body changed')
    proof = {'schema': 'source-checked-ocr-prose-page-v1', 'page': 1, 'all_page_prose_and_boundaries_actually_read': True,
        'resolved_codes': ['cross_engine_review', 'ocr_candidate_source_review'], 'raw_page_sha256': digest(encoded(first)),
        'layout_groups_sha256': digest(encoded(groups)), 'final_page_blocks_sha256': digest(encoded(page_blocks_signature(candidate, 1))),
        'reviewed_page_jpeg_sha256': prepared['files']['page-0001.jpg'], 'reviewed_page_jpeg_bytes': 189697}
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': findings['reviewer'], 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True, 'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'classification': 'word-repairs.json', 'findings': 'findings.json'},
        'ocr_prose_page_reviews': [proof], 'section_source_fidelity_approved': True,
        'whole_paper_source_acceptance': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    apply_ocr_page_reviews(candidate, prospective)
    validate_ocr_page_reviews(candidate, prospective)
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-checked opening page retains pending review flag')
    # Verify portability before writing proof files; explicit bundle roots include inspected JPEGs.
    json_new(output / 'layout.json', layout)
    json_new(output / 'word-repairs.json', repair)
    json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='prospective source-checked prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n')
    json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'characters': len(text), 'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 4,
        'original_ocr_lines': 51, 'unchanged_ocr_line_objects': 49, 'manually_source_transcribed_lines': [30, 37],
        'source_lines_accounted_once': True, 'later_actual_author_body_unchanged': True,
        'separate_page2title_reclassified_without_text_change': True, 'selected_source_status': 'verified in prospective stage only',
        'native_metric_binding_transfer_still_required': True, 'new_ocr_override_not_yet_in_any_corpus': True,
        'span_metrics_source_manifest_sha256': file_hash(base / 'span-metrics-20261031-q267-v2/manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['manifest.json', 'page-0001.json', 'findings.json', 'layout.json', 'word-repairs.json', 'source-review.json', 'summary-preview.md', 'prospective-pages.jsonl']},
        'stager_sha256': file_hash(Path(__file__)), 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
