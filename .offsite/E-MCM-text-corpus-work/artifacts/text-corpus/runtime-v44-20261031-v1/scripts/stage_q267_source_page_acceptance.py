"""Create-only native-metric rebinding and exact q267 OCR prose-page proof."""
import copy
import json
from pathlib import Path

import pymupdf

from corpus_queries import all_author_blocks, selected_blocks, select_sections
from corpus_reader import Catalog
from extract_text_span_metrics import FLAGS, match_page
from resegment_text_corpus import apply_reviews, resolve_exact_comparisons
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_ocr_page_reviews import apply_ocr_page_reviews, page_blocks_signature, validate_ocr_page_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, text_with_block_spans, write_new


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    parent = base / 'reflow-20261031-v32'
    accepted = read_json(base / 'integrity-reflow-20261031-v32.json')
    catalog = Catalog(parent)
    if accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']:
        raise ValueError('Accepted v32 parent required')
    stage = base / 'reviews/20261031/q267-ocr-line-restoration-v2'
    output = base / 'reviews/20261031/q267-source-page-acceptance-v1'
    metrics = base / 'span-metrics-20261031-q267-v2'
    if output.exists() or metrics.exists():
        raise ValueError('Create-only evidence exists; preserve it')
    preflight = read_json(stage / 'preflight.json')
    pid = preflight['paper_id']
    old = catalog.document(pid)
    original = Catalog(base / 'reflow-20261031-v30')
    former = original.document(pid)
    if ({key for key in set(old) | set(former) if old.get(key) != former.get(key)} != {'scope_id'} or
            old['raw_pages_sha256'] != preflight['parent_raw_pages_sha256'] or
            digest(encoded({key: value for key, value in old.items() if key != 'scope_id'})) !=
            digest(encoded({key: value for key, value in former.items() if key != 'scope_id'}))):
        raise ValueError('q267 staged source changed beyond exact scope-id transfer')
    for name, sha in preflight['proof_sha256'].items():
        if file_hash(stage / name) != sha:
            raise ValueError('Individually staged restoration changed')
    pages = rows(stage / 'prospective-pages.jsonl')
    if file_hash(stage / 'prospective-pages.jsonl') != preflight['prospective_raw_pages_sha256']:
        raise ValueError('Prospective raw evidence changed')
    source = Path(read_json(parent / 'scope.json')['source_root']) / old['source_relative_path']
    if file_hash(source) != old['source_sha256']:
        raise ValueError('Source PDF changed')
    previous_metrics = base / 'span-metrics-20261030-v1'
    previous_manifest = read_json(previous_metrics / 'manifest.json')
    if file_hash(previous_metrics / 'manifest.json') != preflight['span_metrics_source_manifest_sha256']:
        raise ValueError('Previously source-bound native metrics changed')
    # Freshly rematch every native line/span on all27physical pages. Only OCR
    # changed; the native metric payload must match byte-for-byte before rebinding.
    fresh = []
    with pymupdf.open(source) as pdf:
        if len(pdf) != len(pages):
            raise ValueError('Physical page count changed')
        for raw, physical in zip(pages, pdf):
            fresh.append(match_page(raw, physical.get_text('dict', flags=FLAGS, sort=False)))
    payload = b''.join((json.dumps(page, ensure_ascii=True, sort_keys=True)+'\n').encode() for page in fresh)
    previous_payload = previous_metrics / 'papers' / pid / 'span-metrics.jsonl'
    if payload != previous_payload.read_bytes():
        raise ValueError('Native PDF preimages/metric payload changed')
    old_complete = read_json(previous_metrics / 'papers' / pid / 'COMPLETE.json')
    if old_complete['raw_pages_sha256'] != old['raw_pages_sha256']:
        raise ValueError('Old native metric binding differs')
    # Materialize a separate sidecar generation; all434other complete files and
    # all435metric payloads keep their exact original bytes.
    for other in catalog.by_id:
        folder = previous_metrics / 'papers' / other
        if file_hash(folder / 'COMPLETE.json') != previous_manifest['files'][other]:
            raise ValueError('Old metric complete record changed')
        done = read_json(folder / 'COMPLETE.json')
        if file_hash(folder / 'span-metrics.jsonl') != done['files']['span-metrics.jsonl']:
            raise ValueError('Old metric payload changed')
    metrics.mkdir(parents=True)
    for other in catalog.by_id:
        folder = previous_metrics / 'papers' / other
        write_new(metrics / 'papers' / other / 'span-metrics.jsonl', (folder / 'span-metrics.jsonl').read_bytes())
        if other == pid:
            changed = copy.deepcopy(old_complete)
            changed['raw_pages_sha256'] = preflight['prospective_raw_pages_sha256']
            json_new(metrics / 'papers' / other / 'COMPLETE.json', changed)
        else:
            write_new(metrics / 'papers' / other / 'COMPLETE.json', (folder / 'COMPLETE.json').read_bytes())
    new_scope = read_json(previous_metrics / 'scope.json')
    new_scope.update(parent_dataset_id=catalog.identity, source_raw_binding_overrides={pid: {
        'old_raw_pages_sha256': old['raw_pages_sha256'], 'new_raw_pages_sha256': preflight['prospective_raw_pages_sha256'],
        'native_payload_byte_identical': True, 'all_physical_pages_freshly_rematched': len(pages)}})
    json_new(metrics / 'scope.json', new_scope)
    manifest = copy.deepcopy(previous_manifest)
    manifest['parent_dataset_id'] = catalog.identity
    manifest['files'][pid] = file_hash(metrics / 'papers' / pid / 'COMPLETE.json')
    manifest['source_raw_binding_overrides'] = new_scope['source_raw_binding_overrides']
    json_new(metrics / 'manifest.json', manifest)
    meta = {key: old[key] for key in ('paper_id', 'problem_type', 'year', 'queue_position',
        'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}
    meta['raw_pages_sha256'] = preflight['prospective_raw_pages_sha256']
    layout = read_json(stage / 'layout.json')
    layout['remaining_uncertainties'] = ['All later author chapters remain pending.']
    for source_evidence in (base / 'ocr-2516178-page1-20261029-v1/manifest.json',
                            base / 'ocr-2516178-page1-20261029-v1/page-0001.json'):
        layout['evidence_files'][str(source_evidence)] = file_hash(source_evidence)
    repair = read_json(stage / 'word-repairs.json')
    review = read_json(stage / 'source-review.json')
    working, _ = prepare_flow_pages(meta, pages, metrics)
    applied = apply_layout_reviews(meta, working, [layout])
    candidate = make_document(meta, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (parent / 'papers' / pid / 'raw/pdftotext.bin').read_bytes())
    apply_text_repairs(candidate, [repair])
    proof = {'schema': 'source-checked-ocr-prose-page-v1', 'page': 1,
        'all_page_prose_and_boundaries_actually_read': True,
        'resolved_codes': ['cross_engine_review', 'ocr_candidate_source_review'],
        'raw_page_sha256': digest(encoded(pages[0])),
        'layout_groups_sha256': digest(encoded(layout['pages'][0]['groups'])),
        'final_page_blocks_sha256': digest(encoded(page_blocks_signature(candidate, 1))),
        'reviewed_page_jpeg_sha256': '5e06d653ed47bb874b413bb92079421973410389fbb693ed41a74883e32b0ae9',
        'reviewed_page_jpeg_bytes': 385363}
    review['ocr_prose_page_reviews'] = [proof]
    apply_reviews(candidate, [review])
    apply_ocr_page_reviews(candidate, pages)
    validate_layout_reviews(candidate, pages)
    validate_ocr_page_reviews(candidate, pages)
    ids, excluded = select_sections(candidate, 'abstract')
    blocks = selected_blocks(candidate, {'section_ids': ids, 'excluded_roles': sorted(excluded)})
    text = text_with_block_spans(blocks)[0]
    later = lambda doc: [(block['source_line_ids'], block['text'], block['kind'], block['issues'])
        for block in all_author_blocks(doc) if min(block['source_pages']) > 1]
    if (digest(text.encode()) != preflight['text_sha256'] or later(old) != later(candidate) or
            any(item.get('status') != 'resolved' and item.get('page') == 1 for item in candidate['defects']) or
            any(block.get('issues') for block in blocks)):
        raise ValueError('Source-page acceptance changed prose or retains pending page flags')
    output.mkdir(parents=True)
    for name, value in (('layout.json', layout), ('word-repairs.json', repair), ('source-review.json', review)):
        json_new(output / name, value)
    result = {'paper_id': pid, 'parent_dataset_id': catalog.identity,
        'staged_preflight_sha256': file_hash(stage / 'preflight.json'), 'staged_dataset_id': original.identity,
        'staged_parent_only_changed_field': 'scope_id', 'characters': len(text), 'text_sha256': digest(text.encode()),
        'logical_author_paragraphs': 6, 'selected_source_status': 'verified',
        'new_raw_pages_sha256': meta['raw_pages_sha256'], 'source_lines_accounted_once': preflight['source_lines_accounted_once'],
        'later_author_text_unchanged': True, 'native_payload_byte_identical': True,
        'all_target_native_pages_freshly_rematched': len(pages), 'other_metric_complete_files_unchanged': 434,
        'all_metric_payloads_unchanged': 435, 'metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'ocr_manifest_sha256': file_hash(stage / 'manifest.json'),
        'proof_sha256': {str((output / name).resolve()): file_hash(output / name)
            for name in ('layout.json', 'word-repairs.json', 'source-review.json')},
        'source_page_review_implementation_sha256': file_hash(work / 'scripts/source_ocr_page_reviews.py'),
        'stager_sha256': file_hash(Path(__file__)), 'whole_paper_source_acceptance': False,
        'ai_reading_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'}
    json_new(output / 'preflight.json', result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
