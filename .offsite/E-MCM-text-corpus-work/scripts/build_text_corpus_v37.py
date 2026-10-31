"""Promote two individually source-restored summaries; preserve all other texts."""
from collections import Counter
import copy
import os
from pathlib import Path
import shutil
import sys

WORK = Path(r'F:\MCM\mcm-skill-work')
STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
sys.path.insert(0, str(WORK / 'scripts'))
from corpus_queries import all_author_blocks
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import apply_reviews, resegment, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_ocr_page_reviews import apply_ocr_page_reviews, validate_ocr_page_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, file_hash, json_new, make_document, read_json, rows, text_with_block_spans, write_new
from validate_text_corpus import validate


def pending(document):
    return Counter(d['code'] for d in document['defects'] if d.get('status') != 'resolved')


def later(document, excluded_ids=()):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues'])
            for b in all_author_blocks(document)
            if min(b['source_pages']) > 1 and b['source_line_ids'] != excluded_ids]


def main():
    os.chdir(WORK)
    base = WORK / 'artifacts/text-corpus'
    parent, output = STORE / 'reflow-20261031-v36', STORE / 'reflow-20261031-v37'
    request, report = STORE / 'build-request-reflow-20261031-v37.json', STORE / 'integrity-reflow-20261031-v37.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Create-only generation exists; preserve it')
    if shutil.disk_usage(STORE).free < 30 * 1024**3:
        raise ValueError('Require30GiBfree; no cleanup authorized')
    catalog, staged_parent = Catalog(parent), Catalog(base / 'reflow-20261031-v34')
    accepted = read_json(STORE / 'integrity-reflow-20261031-v36.json')
    if (catalog.identity != 'a25a3b6ad46aa8c017eb10c6b8e3ce543fb43b684e3c096265ffdaa2bd737914'
            or accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']):
        raise ValueError('Exact acceptedv36required')
    directory = STORE / 'reviews/20261031'
    q286 = directory / 'q286-summary-restoration-v1'
    a, b = read_json(q286 / 'preflight.json'), read_json(directory / 'q292-summary-preflight-v2.json')
    bind_path = directory / 'q286-native-binding-v1.json'
    binding = read_json(bind_path)
    pids = (a['paper_id'], b['paper_id'])
    if pids != ('P-D-2017-68942-f0b0893e', 'P-D-2018-82794-47f05792'):
        raise ValueError('Exact two individually checked papers required')
    transfer = {}
    for pid in pids:
        old, current = copy.deepcopy(staged_parent.document(pid)), copy.deepcopy(catalog.document(pid))
        old_scope, new_scope = old.pop('scope_id'), current.pop('scope_id')
        if old != current or old_scope == new_scope:
            raise ValueError('Staged source transfer must change scope identity only')
        transfer[pid] = {'old_scope_id': old_scope, 'new_scope_id': new_scope,
                         'all_other_document_fields_byte_equivalent': True}
    if any(x['parent_dataset_id'] != staged_parent.identity or not x['source_lines_accounted_once'] for x in (a, b)):
        raise ValueError('Source preflights do not bind unchanged parents')
    if (a['characters'] != 2353 or a['logical_author_paragraphs'] != 4 or not a['later_actual_author_body_unchanged']
            or b['characters'] != 2422 or b['logical_author_paragraphs'] != 6 or not b['later_author_text_unchanged']
            or b['selected_source_status'] != 'verified' or b['literal_wrap_occurrences_repaired'] != 5):
        raise ValueError('Exact complete source paragraph guards differ')
    for name, sha in a['proof_sha256'].items():
        if file_hash(q286 / name) != sha:
            raise ValueError('q286staged proof changed')
    for name, sha in b['proof_sha256'].items():
        if file_hash(Path(name)) != sha:
            raise ValueError('q292staged proof changed')
    if (binding['staged_preflight_sha256'] != file_hash(q286 / 'preflight.json')
            or binding['all_target_native_pages_freshly_rematched'] != 37
            or binding['all_metric_payloads_unchanged'] != 435
            or binding['other_metric_complete_files_unchanged'] != 434
            or not binding['portable_page_proof_replay_pass']
            or file_hash(WORK / 'scripts/source_ocr_page_reviews.py') != binding['source_page_review_implementation_sha256']
            or file_hash(Path(__file__).with_name('bind_q286_native_metrics_v1.py')) != binding['binder_sha256']
            or file_hash(Path(__file__).with_name('stage_q286_summary_restoration_v1.py')) != a['stager_sha256']
            or file_hash(WORK / 'scripts/stage_explicit_summary.py') != b['stager_sha256']):
        raise ValueError('Source/native binding or staging implementation changed')
    metrics = STORE / 'span-metrics-20261031-q286-v1'
    if file_hash(metrics / 'manifest.json') != binding['metrics_manifest_sha256']:
        raise ValueError('Freshly rematched native metric manifest changed')
    names = ('source_span_metrics.py', 'text_corpus.py', 'preview_span_origin_flow.py', 'source_text_repairs.py',
             'source_layout_reviews.py', 'source_absence_reviews.py', 'resegment_text_corpus.py', 'corpus_queries.py',
             'corpus_reader.py', 'source_paragraph_reviews.py', 'source_ocr_page_reviews.py', 'extract_text_span_metrics.py',
             'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')
    frozen = {name: file_hash(WORK / 'scripts' / name) for name in names}
    scope = read_json(parent / 'scope.json')
    additions = {
        'ocr_manifest_sha256': [q286 / 'manifest.json'],
        'source_review_sha256': [q286 / 'source-review.json', directory / 'q292-summary-source-review-v2.json'],
        'text_repair_sha256': [q286 / 'word-repairs.json', directory / 'q292-summary-word-repairs-v2.json'],
        'layout_review_sha256': [q286 / 'layout.json', directory / 'q292-summary-layout-v2.json']}
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    inputs = {field: [] for field in fields}
    for field in fields:
        for name, sha in scope.get(field, {}).items():
            if file_hash(Path(name)) != sha:
                raise ValueError('Accepted evidence changed: ' + name)
            inputs[field].append(Path(name))
        inputs[field].extend(additions.get(field, []))
        if len({str(p.resolve()) for p in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    if len(inputs['ocr_manifest_sha256']) != 54:
        raise ValueError('Preserve all53accepted OCRinputs plus exactly one new input')
    bindings = {field: {str(p.resolve()): file_hash(p) for p in paths} for field, paths in inputs.items()}
    candidates, texts, titles = {}, {}, {}
    expected_defects, expected_totals = Counter(accepted['defects']), dict(accepted['totals'])
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    for pid, preflight, folder, prefix in [(pids[0], a, q286, ''), (pids[1], b, directory, 'q292-summary-')]:
        old = catalog.document(pid)
        if prefix:
            paths = {name: folder / (prefix + suffix + '-v2.json') for name, suffix in
                     [('layout', 'layout'), ('repair', 'word-repairs'), ('review', 'source-review')]}
            pages = rows(parent / 'papers' / pid / 'raw/pages.jsonl')
            summary_file = folder / 'q292-summary-preview-v2.md'
        else:
            paths = {name: folder / file for name, file in [('layout', 'layout.json'), ('repair', 'word-repairs.json'), ('review', 'source-review.json')]}
            pages = rows(folder / 'prospective-pages.jsonl')
            summary_file = folder / 'summary-preview.md'
        meta = {key: old[key] for key in keys}
        meta['raw_pages_sha256'] = preflight.get('raw_pages_sha256', old['raw_pages_sha256'])
        working, _ = prepare_flow_pages(meta, pages, metrics)
        layouts, _ = prepare_review_bundles([paths['layout']], identity_fields=('paper_id',),
            application_status='applied individually source-checked prose lanes;not whole-paper acceptance')
        applied = apply_layout_reviews(meta, working, layouts)
        candidate = make_document(meta, working, improved=True)
        candidate['layout_reviews'] = applied
        resolve_exact_comparisons(candidate, pages, (parent / 'papers' / pid / 'raw/pdftotext.bin').read_bytes())
        apply_text_repairs(candidate, [read_json(paths['repair'])])
        apply_reviews(candidate, [read_json(paths['review'])])
        apply_ocr_page_reviews(candidate, pages)
        validate_layout_reviews(candidate, pages)
        validate_ocr_page_reviews(candidate, pages)
        summary = summary_file.read_text(encoding='utf-8').removesuffix('\n')
        if len(summary) != preflight['characters'] or digest(summary.encode()) != preflight['text_sha256']:
            raise ValueError('Exact source summary changed')
        excluded = []
        if pid == pids[0]:
            title = 'Optimizing Passenger Throughput at an Airport Security Checkpoint'
            found = [x for x in old['blocks'] if x['text'] == title and x['source_pages'] == [2]]
            if len(found) != 1 or found[0]['kind'] != 'prose':
                raise ValueError('Separate old page2title preimage changed')
            excluded = found[0]['source_line_ids']
        titles[pid] = excluded
        rest = [x for x in all_author_blocks(old) if min(x['source_pages']) > 1 and x['source_line_ids'] != excluded]
        author = summary + '\n\n' + text_with_block_spans(rest)[0]
        if later(old, excluded) != later(candidate, excluded) or text_with_block_spans(all_author_blocks(candidate))[0] != author:
            raise ValueError('Later actual author body changed')
        candidates[pid], texts[pid] = candidate, {'abstract': summary, 'all_author_text': author}
        expected_defects.subtract(pending(old)); expected_defects.update(pending(candidate))
        expected_totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
        expected_totals['sections'] += len(candidate['sections']) - len(old['sections'])
        expected_totals['boundary_verified'] += 1
        expected_totals['source_lines'] += sum(len(p['lines']) for p in pages) - sum(len(p['lines']) for p in rows(parent / 'papers' / pid / 'raw/pages.jsonl'))
    expected_defects = {key: count for key, count in expected_defects.items() if count}
    previous = {family: {x['paper_id']: x for x in catalog.select(family)} for family in ('abstract', 'all_author_text')}
    if any(previous['abstract'][pid]['status'] != 'present-unverified' for pid in pids):
        raise ValueError('Two previously unverified summaries expected')
    native = base / 'native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native dataset changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'explicit_unchanged_source_transfer': transfer, 'q286_preflight_sha256': file_hash(q286 / 'preflight.json'),
        'q292_preflight_sha256': file_hash(directory / 'q292-summary-preflight-v2.json'),
        'q286_native_binding_sha256': file_hash(bind_path), 'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_totals': expected_totals, 'expected_open_defects': expected_defects,
        'change': 'Two individually source-checked summaries:q286native-empty scanned page recovered as four paragraphs;separate page2title reclassified.Q292six complete paragraphs include missing WeightedBetweennessline and five printed wrap repairs.Other433selections/statuses,all later actual prose and all other raw evidence unchanged.',
        'source_boundary_reviews_added': 2, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
              inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (WORK / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v37.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            pid = item['paper_id']; before = previous[family][pid]
            if pid not in pids:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated source selection changed: ' + pid)
            elif built.text_and_spans(item)[0] != texts[pid][family] or item['status'] != ('verified' if family == 'abstract' else before['status']):
                raise ValueError('Target source selection/status differs')
    for pid in catalog.by_id:
        old, new = catalog.document(pid), built.document(pid)
        wanted_raw = a['raw_pages_sha256'] if pid == pids[0] else old['raw_pages_sha256']
        if new['raw_pages_sha256'] != wanted_raw:
            raise ValueError('Unexpected raw source change: ' + pid)
        if pid in pids and later(old, titles[pid]) != later(new, titles[pid]):
            raise ValueError('Later target body changed')
    result = validate(output, WORK, True)
    if (result['defects'] != expected_defects or result['totals'] != expected_totals
            or not result['structural_integrity_pass'] or result['source_completeness_accepted']):
        raise ValueError('Unexpected global counts/defects/acceptance;preserve failed candidate')
    if any(file_hash(Path(path)) != sha for group in bindings.values() for path, sha in group.items()) or any(file_hash(WORK / 'scripts' / name) != sha for name, sha in frozen.items()):
        raise ValueError('Frozen source proof/core changed during build')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
