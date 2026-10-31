"""Rebind all23native pages after q306 source adjudication;preserve every payload."""
import copy
import json
from pathlib import Path
import sys

STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
RUNTIME = STORE / 'runtime-v39-20261031-v1'
sys.path.insert(0, str(RUNTIME / 'scripts'))
import pymupdf
from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from extract_text_span_metrics import FLAGS, match_page
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_ocr_page_reviews import apply_ocr_page_reviews, validate_ocr_page_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, file_hash, json_new, make_document, read_json, rows, text_with_block_spans, write_new


def main():
    metrics = STORE / 'span-metrics-20261031-q306-v1'
    report = STORE / 'reviews/20261031/q306-native-binding-v1.json'
    stage = STORE / 'reviews/20261031/q306-summary-restoration-v2'
    if metrics.exists() or report.exists():
        raise ValueError('Create-only binding exists;preserve it')
    parent = STORE / 'reflow-20261031-v40'
    catalog = Catalog(parent)
    preflight = read_json(stage / 'preflight.json')
    pid = preflight['paper_id']
    old = catalog.document(pid)
    if preflight['parent_dataset_id'] != catalog.identity or preflight['parent_raw_pages_sha256'] != old['raw_pages_sha256']:
        raise ValueError('Exact staged binding required')
    for name, sha in preflight['proof_sha256'].items():
        if file_hash(stage / name) != sha:
            raise ValueError('Staged proof changed')
    if file_hash(stage / 'prospective-pages.jsonl') != preflight['raw_pages_sha256']:
        raise ValueError('Prospective raw evidence changed')
    pages = rows(stage / 'prospective-pages.jsonl')
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    previous = STORE / 'span-metrics-20261031-q305-v1'
    previous_manifest = read_json(previous / 'manifest.json')
    if file_hash(source) != old['source_sha256'] or file_hash(previous / 'manifest.json') != preflight['span_metrics_source_manifest_sha256']:
        raise ValueError('PDF/native metrics changed')
    fresh = []
    with pymupdf.open(source) as pdf:
        if len(pdf) != len(pages) or len(pdf) != 23:
            raise ValueError('Expected23physical pages')
        for page, physical in zip(pages, pdf):
            fresh.append(match_page(page, physical.get_text('dict', flags=FLAGS, sort=False)))
    payload = b''.join((json.dumps(page, ensure_ascii=True, sort_keys=True) + '\n').encode() for page in fresh)
    if payload != (previous / 'papers' / pid / 'span-metrics.jsonl').read_bytes():
        raise ValueError('Fresh native payload differs')
    for other in catalog.by_id:
        folder = previous / 'papers' / other
        if file_hash(folder / 'COMPLETE.json') != previous_manifest['files'][other]:
            raise ValueError('Metric record changed')
        done = read_json(folder / 'COMPLETE.json')
        if file_hash(folder / 'span-metrics.jsonl') != done['files']['span-metrics.jsonl']:
            raise ValueError('Metric payload changed')
    metrics.mkdir(parents=True)
    for other in catalog.by_id:
        folder = previous / 'papers' / other
        write_new(metrics / 'papers' / other / 'span-metrics.jsonl', (folder / 'span-metrics.jsonl').read_bytes())
        if other == pid:
            complete = copy.deepcopy(read_json(folder / 'COMPLETE.json'))
            if complete['raw_pages_sha256'] != old['raw_pages_sha256']:
                raise ValueError('Previous native binding differs')
            complete['raw_pages_sha256'] = preflight['raw_pages_sha256']
            json_new(metrics / 'papers' / other / 'COMPLETE.json', complete)
        else:
            write_new(metrics / 'papers' / other / 'COMPLETE.json', (folder / 'COMPLETE.json').read_bytes())
    scope = read_json(previous / 'scope.json')
    overrides = copy.deepcopy(scope.get('source_raw_binding_overrides', {}))
    overrides[pid] = {'old_raw_pages_sha256': old['raw_pages_sha256'], 'new_raw_pages_sha256': preflight['raw_pages_sha256'],
        'native_payload_byte_identical': True, 'all_physical_pages_freshly_rematched': 23}
    scope.update(parent_dataset_id=catalog.identity, source_raw_binding_overrides=overrides)
    json_new(metrics / 'scope.json', scope)
    manifest = copy.deepcopy(previous_manifest)
    manifest.update(parent_dataset_id=catalog.identity, source_raw_binding_overrides=overrides)
    manifest['files'][pid] = file_hash(metrics / 'papers' / pid / 'COMPLETE.json')
    json_new(metrics / 'manifest.json', manifest)
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    meta = {key: old[key] for key in keys}
    meta['raw_pages_sha256'] = preflight['raw_pages_sha256']
    working, _ = prepare_flow_pages(meta, pages, metrics)
    layouts, _ = prepare_review_bundles([stage / 'layout.json'], identity_fields=('paper_id',), application_status='applied prose lanes;no whole-paper acceptance')
    applied = apply_layout_reviews(meta, working, layouts)
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (parent / 'papers' / pid / 'raw/pdftotext.bin').read_bytes())
    apply_text_repairs(candidate, [read_json(stage / 'word-repairs.json')])
    apply_reviews(candidate, [read_json(stage / 'source-review.json')])
    apply_ocr_page_reviews(candidate, pages)
    validate_layout_reviews(candidate, pages)
    validate_ocr_page_reviews(candidate, pages)
    ids, excluded = select_sections(candidate, 'abstract')
    text = text_with_block_spans(selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)}))[0]
    staged = read_json(stage / 'candidate.json')
    if (digest(text.encode()) != preflight['text_sha256']
            or text_with_block_spans(all_author_blocks(candidate))[0] != text_with_block_spans(all_author_blocks(staged))[0]
            or candidate['defects'] != staged['defects']):
        raise ValueError('Portable/native-bound replay changed prose or flags')
    if any(file_hash(metrics / 'papers' / other / 'span-metrics.jsonl') != file_hash(previous / 'papers' / other / 'span-metrics.jsonl') for other in catalog.by_id):
        raise ValueError('Copied native payload changed')
    if any(file_hash(metrics / 'papers' / other / 'COMPLETE.json') != previous_manifest['files'][other] for other in catalog.by_id if other != pid):
        raise ValueError('Other434metric records changed')
    result = {'paper_id': pid, 'parent_dataset_id': catalog.identity,
        'staged_preflight_sha256': file_hash(stage / 'preflight.json'), 'new_raw_pages_sha256': preflight['raw_pages_sha256'],
        'all_target_native_pages_freshly_rematched': 23, 'all_metric_payloads_unchanged': 435,
        'other_metric_complete_files_unchanged': 434, 'metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'portable_page_proof_replay_pass': True, 'characters': len(text), 'text_sha256': digest(text.encode()),
        'logical_author_paragraphs': 6, 'proof_sha256': preflight['proof_sha256'], 'binder_sha256': file_hash(Path(__file__)),
        'library_sha256': file_hash(RUNTIME / 'scripts/text_corpus.py'),
        'source_page_review_implementation_sha256': file_hash(RUNTIME / 'scripts/source_ocr_page_reviews.py'),
        'new_corpus_not_yet_built': True, 'whole_paper_source_acceptance': False, 'ai_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
