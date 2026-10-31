"""Restore the individually source-read, untitled five-paragraph q304 Summary."""
import copy
import json
from collections import Counter
from pathlib import Path
import sys

WORK = Path(r'F:\MCM\mcm-skill-work')
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
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, section_blocks, section_text, text_with_block_spans, write_new


def main():
    directory = STORE / 'reviews/20261031'
    output = directory / 'q304-summary-restoration-v2'
    if output.exists():
        raise ValueError('Create-only stage exists; preserve it')
    root = STORE / 'reflow-20261031-v38'
    catalog = Catalog(root)
    old = catalog.document('P-D-2020-2022868-71331b90')
    prepared_parent = Catalog(STORE / 'reflow-20261031-v37')
    before, after = copy.deepcopy(prepared_parent.document(old['paper_id'])), copy.deepcopy(old)
    old_scope, new_scope = before.pop('scope_id'), after.pop('scope_id')
    if before != after or old_scope == new_scope:
        raise ValueError('Prepared source evidence may transfer only across identical paper data')
    if old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews'):
        raise ValueError('Existing paper reviews require explicit replay')
    original = directory / 'q304-summary-ocr-v1'
    page_evidence = directory / 'q304-opening-pages-v1'
    original_manifest = read_json(original / 'manifest.json')
    original_page = read_json(original / 'page-0001.json')
    prepared = read_json(page_evidence / 'manifest.json')
    source = Path(read_json(root / 'scope.json')['source_root']) / old['source_relative_path']
    raw_path = root / 'papers' / old['paper_id'] / 'raw/pages.jsonl'
    if (catalog.identity != '62d23dc3f7382dfdf0ffa0c137abbba1101da4a98ded03a35092c5aff5cd80e3'
            or prepared['dataset_id'] != prepared_parent.identity or old['queue_position'] != 304
            or file_hash(source) != old['source_sha256'] or file_hash(raw_path) != old['raw_pages_sha256']
            or prepared['source_sha256'] != old['source_sha256']
            or original_manifest['source_sha256'] != old['source_sha256']
            or prepared['raw_pages_sha256'] != old['raw_pages_sha256']
            or len(original_page['lines']) != 36
            or file_hash(original / 'page-0001.json') != '64d4e62f926b69376258a4b10030faa86cd1e32d4f55654afca107ac96f4f5f7'
            or file_hash(original / 'page-0001.json') != original_manifest['pages'][0]['sha256']):
        raise ValueError('Exact source/native/OCR identity differs')
    for name, sha in prepared['files'].items():
        if file_hash(page_evidence / name) != sha:
            raise ValueError('Actually inspected source evidence changed')
    revised = copy.deepcopy(original_page)
    corrections = []
    for index, token in [(12, "Huskies'"), (24, "team's"), (27, "opponent's"), (28, "opponent.")]:
        # The first three apostrophes are visibly curly on the actual source page.
        # Line28has no possessive in the original wording and must remain unchanged.
        if original_page['lines'][index]['text'].count(token) != 1:
            raise ValueError('Exact source punctuation preimage changed')
        if index == 28:
            continue
        revised['lines'][index]['text'] = original_page['lines'][index]['text'].replace("'", '’')
        corrections.append({'original_ocr_index': index, 'old_text': original_page['lines'][index]['text'],
            'source_transcription': revised['lines'][index]['text'],
            'original_ocr_score_retained_as_original_only': original_page['lines'][index]['score'],
            'basis': 'Curly apostrophe actually read on the complete inspected source page;no word rewritten.'})
    if any(revised['lines'][i] != original_page['lines'][i] for i in range(36) if i not in {12, 24, 27}):
        raise ValueError('Other33OCRline objects changed')
    revised['manual_source_transcriptions'] = corrections
    revised['review_status'] = 'All five source paragraphs and source-page boundaries actually read;separate acceptance proof required.'
    output.mkdir(parents=True)
    findings = {'schema': 'source-prose-layout-findings-v2', 'paper_id': old['paper_id'],
        'source_sha256': old['source_sha256'], 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'reviewer': 'Codex root;2026-10-31;complete physicalpage1andpage2JPEGs and all36OCRlines actually read',
        'checked_pages': [1, 2], 'logical_author_paragraphs': 5,
        'source_boundary': 'Five untitled author Summaryparagraphs below competition form onphysicalpage1.Page2has separate paper title,TOCandfigure-list entries;no Summarycontinuation.No heading invented.',
        'paragraphs': ['shared team objective', 'dyadic/triadic structures have little impact',
            'new metrics and regression limitations motivate overall styles',
            'four styles,opponent-specific strategy and reported win/loss limits', 'Huskies current style versus better observed style'],
        'transcriptions': corrections,
        'preserved_claims': ['13-10-15season', 'structures had little impact', 'within1.5shots51.3percent',
            'no single metric universal', 'Tiki-Taka58.1percent', 'win likelihood never below37.5percent',
            'loss likelihood never above33.3percent', 'HighPressingwins30percent'],
        'excluded_source': ['competition form', 'third-party promotional footer', 'page2title/TOC/figure-list entries'],
        'scope_boundary': 'Prose restoration and paragraph/section boundaries only;no figure interpretation,formula verification or methodological validation.',
        'prepared_evidence_scope_transfer': {'old_scope_id': old_scope, 'new_scope_id': new_scope,
            'all_other_paper_fields_equivalent': True}, 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'findings.json', findings)
    json_new(output / 'page-0001.json', revised)
    manifest = {**original_manifest, 'pages': [{'page': 1, 'path': 'page-0001.json',
        'sha256': file_hash(output / 'page-0001.json'), 'line_count': 36,
        'low_confidence_lines': sum(line['score'] < .95 for line in revised['lines'])}],
        'source_recovery': {'original_manifest_sha256': file_hash(original / 'manifest.json'),
            'original_page_sha256': file_hash(original / 'page-0001.json'),
            'findings_sha256': file_hash(output / 'findings.json'),
            'only_changes': 'Three actually source-read curly apostrophes;all36original boxes/scores and33other complete line objects unchanged.'}}
    json_new(output / 'manifest.json', manifest)
    pages = rows(raw_path)
    prospective = copy.deepcopy(pages)
    first = prospective[0]
    if first.get('ocr_evidence') or any(phrase in ' '.join(line['text'] for line in first['lines'])
                                      for phrase in ['We all share', 'First, we created', 'Analyzing our home team']):
        raise ValueError('Native preimage should lack actual Summaryprose and OCR')
    for line in first['lines']:
        line['superseded_by_ocr'] = True
    for index, value in enumerate(revised['lines']):
        points = value['pdf_box']
        box = [min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)]
        first['lines'].append({'line_id': f'p0001-ocr-l{index:04d}', 'native_block': -1, 'page': 1,
            'bbox': box, 'text': value['text'], 'font_size': max(5, (box[3]-box[1])*.95),
            'bold': False, 'spans': [], 'ocr_score': value['score'], 'engine': 'rapidocr'})
    first['ocr_status'] = 'candidate'
    first['ocr_evidence'] = {'path': 'raw/ocr/page-0001.json', 'sha256': file_hash(output / 'page-0001.json'),
                             'models': manifest['model_sha256'], 'version': manifest['ocr_version']}
    raw = b''.join((json.dumps(page, ensure_ascii=True, sort_keys=True) + '\n').encode() for page in prospective)
    write_new(output / 'prospective-pages.jsonl', raw)
    metrics = STORE / 'span-metrics-20261031-q286-v1'
    working, _ = prepare_flow_pages(old, pages, metrics)
    working[0] = copy.deepcopy(first)
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    meta = {key: old[key] for key in keys}
    meta['raw_pages_sha256'] = digest(raw)
    identity = {key: meta[key] for key in ('paper_id', 'source_sha256', 'raw_pages_sha256')}
    evidence = [{'path': str(path), 'sha256': file_hash(path), 'description': desc,
                 **({'bundle_root': str(bundle)} if bundle else {})}
        for path, bundle, desc in [(page_evidence / 'manifest.json', page_evidence, 'Both actually read complete opening JPEGs and untouched native evidence.'),
            (original / 'manifest.json', original, 'All36original localOCRlines,boxesandconfidence scores.'),
            (output / 'findings.json', None, 'Exact source paragraphs and source-bound punctuation transcriptions.'),
            (output / 'manifest.json', None, 'Versioned source-adjudicated OCRmanifest.'),
            (output / 'page-0001.json', None, 'All36transcribed lines retaining original scores explicitly as original only.'),
            (Path(__file__), None, 'Exact create-only individual-paper stager.')]]
    files = {str(p): file_hash(p) for folder in (page_evidence, original) for p in folder.iterdir() if p.is_file()}
    files.update({e['path']: e['sha256'] for e in evidence})
    by_id = {line['line_id']: line for line in first['lines']}
    groups = []
    for name, kind, numbers in [('form', 'front_matter', range(7)), ('summary1', 'prose', range(7, 10)),
            ('summary2', 'prose', range(10, 14)), ('summary3', 'prose', range(14, 22)),
            ('summary4', 'prose', range(22, 30)), ('summary5', 'prose', range(30, 34)),
            ('promotion', 'furniture', range(34, 36))]:
        ids = [f'p0001-ocr-l{i:04d}' for i in numbers]
        groups.append({'group_id': name, 'kind': kind, 'source_line_ids': ids,
            'text_sha256': digest(' '.join(by_id[lid]['text'].strip() for lid in ids).encode()),
            'reason': 'Actually source-read complete five-paragraph untitled Summary;form/promotion separate.'})
    layout = {'schema': 'source-text-layout-review-v1', **identity, 'reviewer': findings['reviewer'],
        'reason': 'Recover all five missing author paragraphs;retain native and OCR evidence without invented heading.',
        'paragraph_boundaries_checked': True, 'reading_lanes_checked': True, 'pages': [{'page': 1, 'groups': groups}],
        'evidence': evidence, 'evidence_files': files,
        'remaining_uncertainties': ['Fresh24page native-metric rebinding still required.', 'All later chapter source acceptance pending.'],
        'source_fidelity_approved': False, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, prospective, (root / 'papers' / old['paper_id'] / 'raw/pdftotext.bin').read_bytes())
    validate_layout_reviews(candidate, prospective)
    actual = Counter(lid for b in candidate['blocks'] for lid in b['source_line_ids'])
    actual.update(line['line_id'] for line in candidate['excluded_source_lines'])
    if actual != Counter(line['line_id'] for p in prospective for line in p['lines']) or any(c != 1 for c in actual.values()):
        raise ValueError('Every native/OCRline must have exactly one source owner')
    ids, excluded = select_sections(candidate, 'abstract')
    selected = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text = text_with_block_spans(selected)[0]
    ids = [sid for sid in ids if any(b['section_id'] == sid for b in selected)]
    if (len(ids) != 1 or len(selected) != 5 or {p for b in selected for p in b['source_pages']} != {1}
            or not text.startswith('We all share one goal - making our home team')
            or not text.endswith('style, where they won more than half the time.')
            or any(s not in text for s in ['had little impact', '1.5 shots 51.3%', '58.1%', '37.5%', '33.3%', 'win only 30%'])
            or any(s in text for s in ['Summary Sheet', 'MCM/ICM', '关注', 'Contents'])):
        raise ValueError('Complete five-paragraph source Summaryguard failed')
    later = lambda d: [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(d) if min(b['source_pages']) > 1]
    if later(old) != later(candidate):
        raise ValueError('Later actual author body changed')
    proof = {'schema': 'source-checked-ocr-prose-page-v1', 'page': 1,
        'all_page_prose_and_boundaries_actually_read': True, 'resolved_codes': ['cross_engine_review', 'ocr_candidate_source_review'],
        'raw_page_sha256': digest(encoded(first)), 'layout_groups_sha256': digest(encoded(groups)),
        'final_page_blocks_sha256': digest(encoded(page_blocks_signature(candidate, 1))),
        'reviewed_page_jpeg_sha256': prepared['files']['page-0001.jpg'], 'reviewed_page_jpeg_bytes': 272106}
    review = {**identity, 'section_id': ids[0], 'text_sha256': digest(section_text(candidate, ids).encode()),
        'reviewer': findings['reviewer'], 'checked_pages': [1, 2], 'section_boundaries_checked': True,
        'paragraph_boundaries_checked': True, 'paragraph_blocks': [b['block_id'] for b in section_blocks(candidate, ids) if b['kind'] != 'heading'],
        'evidence': {'layout': 'layout.json', 'findings': 'findings.json'}, 'ocr_prose_page_reviews': [proof],
        'section_source_fidelity_approved': True, 'whole_paper_source_acceptance': False,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    apply_reviews(candidate, [review])
    apply_ocr_page_reviews(candidate, prospective)
    validate_ocr_page_reviews(candidate, prospective)
    if any(d.get('page') == 1 and d.get('status') != 'resolved' for d in candidate['defects']):
        raise ValueError('Source-read opening page retains a pending flag')
    json_new(output / 'layout.json', layout)
    json_new(output / 'source-review.json', review)
    prepare_review_bundles([output / 'layout.json'], identity_fields=('paper_id',), application_status='prospective source-checked prose;not a built corpus')
    write_new(output / 'summary-preview.md', text + '\n')
    json_new(output / 'candidate.json', candidate)
    result = {**identity, 'parent_dataset_id': catalog.identity, 'parent_raw_pages_sha256': old['raw_pages_sha256'],
        'characters': len(text), 'text_sha256': digest(text.encode()), 'logical_author_paragraphs': 5,
        'original_ocr_lines': 36, 'unchanged_ocr_line_objects': 33, 'manually_source_transcribed_lines': [12, 24, 27],
        'source_lines_accounted_once': True, 'later_actual_author_body_unchanged': True,
        'selected_source_status': 'verified in prospective stage only', 'native_metric_binding_transfer_still_required': True,
        'new_ocr_override_not_yet_in_any_corpus': True, 'span_metrics_source_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'proof_sha256': {name: file_hash(output / name) for name in ['manifest.json', 'page-0001.json', 'findings.json',
            'layout.json', 'source-review.json', 'summary-preview.md', 'prospective-pages.jsonl']},
        'stager_sha256': file_hash(Path(__file__)),
        'library_sha256': file_hash(RUNTIME / 'scripts/text_corpus.py'),
        'whole_paper_source_acceptance': False, 'ai_receipts_created': 0}
    json_new(output / 'preflight.json', result)
    print(text, flush=True)
    print(result, flush=True)


if __name__ == '__main__':
    main()
