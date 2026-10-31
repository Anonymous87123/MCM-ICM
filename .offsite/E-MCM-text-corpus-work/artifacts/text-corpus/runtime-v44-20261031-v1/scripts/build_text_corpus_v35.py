"""Promote q264's complete source-restored Summary; preserve all434others."""
from collections import Counter
import os
from pathlib import Path

from corpus_queries import all_author_blocks
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import apply_reviews, resegment, resolve_exact_comparisons
from source_absence_reviews import prepare_review_bundles
from source_layout_reviews import apply_layout_reviews, validate_layout_reviews
from source_span_metrics import prepare_flow_pages
from source_text_repairs import apply_text_repairs
from text_corpus import digest, file_hash, json_new, make_document, read_json, rows, text_with_block_spans, write_new
from validate_text_corpus import validate


def open_defects(document):
    return Counter(item['code'] for item in document['defects'] if item.get('status') != 'resolved')


def later_signature(document):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues'])
            for b in all_author_blocks(document) if min(b['source_pages']) > 1]


def main():
    work = Path(__file__).resolve().parents[1]
    os.chdir(work)
    base = work / 'artifacts/text-corpus'
    parent, output = base / 'reflow-20261031-v34', base / 'reflow-20261031-v35'
    request = base / 'build-request-reflow-20261031-v35.json'
    report = base / 'integrity-reflow-20261031-v35.json'
    if any(path.exists() for path in (output, request, report)):
        raise ValueError('Create-only state exists; preserve it')
    catalog = Catalog(parent)
    accepted = read_json(base / 'integrity-reflow-20261031-v34.json')
    if (catalog.identity != '3d6bf77d7c11927af409b69eae31073f26d5df6426e82d56c541fd9e6ec85d9e' or
            not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity):
        raise ValueError('Exact accepted parent required')
    directory = base / 'reviews/20261031'
    added = {field: directory / f'q264-summary-{suffix}-v2.json' for field, suffix in
             [('layout_review_sha256', 'layout'), ('text_repair_sha256', 'word-repairs'), ('source_review_sha256', 'source-review')]}
    proof_hashes = {str(path.resolve()): file_hash(path) for path in added.values()}
    preflight_path = directory / 'q264-summary-preflight-v2.json'
    preflight = read_json(preflight_path)
    pid = preflight['paper_id']
    old = catalog.document(pid)
    if (pid != 'P-C-2025-2514362-c904f1a9' or preflight['parent_dataset_id'] != catalog.identity or
            preflight['proof_sha256'] != proof_hashes or preflight['characters'] != 3055 or
            preflight['logical_author_paragraphs'] != 7 or preflight['selected_source_status'] != 'verified' or
            preflight['literal_wrap_occurrences_repaired'] != 11 or
            not preflight['source_lines_accounted_once'] or not preflight['later_author_text_unchanged'] or
            file_hash(work / 'scripts/stage_explicit_summary.py') != preflight['stager_sha256'] or
            old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews')):
        raise ValueError('Exact single-paper source preflight required')
    frozen_names = ('source_span_metrics.py', 'text_corpus.py', 'preview_span_origin_flow.py',
        'source_text_repairs.py', 'source_layout_reviews.py', 'source_absence_reviews.py', 'resegment_text_corpus.py',
        'corpus_queries.py', 'corpus_reader.py', 'source_paragraph_reviews.py', 'source_ocr_page_reviews.py',
        'extract_text_span_metrics.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')
    frozen = {name: file_hash(work / 'scripts' / name) for name in frozen_names}
    scope = read_json(parent / 'scope.json')
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    inputs = {field: [] for field in fields}
    for field in fields:
        for name, sha in scope.get(field, {}).items():
            path = Path(name)
            if file_hash(path) != sha:
                raise ValueError('Previously accepted source proof changed: ' + name)
            inputs[field].append(path)
        if field in added:
            inputs[field].append(added[field])
        if len({str(path.resolve()) for path in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    if len(inputs['ocr_manifest_sha256']) != 53:
        raise ValueError('All53accepted OCR inputs must remain')
    metrics = base / 'span-metrics-20261031-q267-v2'
    if file_hash(metrics / 'manifest.json') != scope['span_metrics_manifest_sha256']:
        raise ValueError('Accepted native metrics binding changed')
    bindings = {field: {str(path.resolve()): file_hash(path) for path in paths} for field, paths in inputs.items()}
    pages = rows(parent / 'papers' / pid / 'raw/pages.jsonl')
    working, _ = prepare_flow_pages(old, pages, metrics)
    layouts, _ = prepare_review_bundles([added['layout_review_sha256']], identity_fields=('paper_id',),
                                      application_status='applied individually source-checked prose lanes; no whole-paper acceptance')
    applied = apply_layout_reviews(old, working, layouts)
    keys = ('paper_id', 'problem_type', 'year', 'queue_position', 'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')
    candidate = make_document({key: old[key] for key in keys}, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (parent / 'papers' / pid / 'raw/pdftotext.bin').read_bytes())
    apply_text_repairs(candidate, [read_json(added['text_repair_sha256'])])
    apply_reviews(candidate, [read_json(added['source_review_sha256'])])
    validate_layout_reviews(candidate, pages)
    summary = (directory / 'q264-summary-preview-v2.md').read_text(encoding='utf-8').removesuffix('\n')
    rest = [b for b in all_author_blocks(old) if min(b['source_pages']) > 1]
    author = summary + '\n\n' + text_with_block_spans(rest)[0]
    if (len(summary) != 3055 or digest(summary.encode()) != preflight['text_sha256'] or
            text_with_block_spans(all_author_blocks(candidate))[0] != author or later_signature(old) != later_signature(candidate)):
        raise ValueError('Complete restored Summary must be sole author-text change')
    previous = {family: {item['paper_id']: item for item in catalog.select(family)} for family in ('abstract', 'all_author_text')}
    expected_defects = Counter(accepted['defects'])
    expected_defects.subtract(open_defects(old))
    expected_defects.update(open_defects(candidate))
    expected_defects = {code: count for code, count in expected_defects.items() if count}
    expected_totals = dict(accepted['totals'])
    expected_totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
    expected_totals['sections'] += len(candidate['sections']) - len(old['sections'])
    expected_totals['boundary_verified'] += 1
    native = base / 'native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native dataset changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'single_paper_source_preflight_sha256': file_hash(preflight_path),
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_open_defects': expected_defects, 'expected_totals': expected_totals,
        'change': 'Restore q264complete seven-paragraph Summary:printed host-effects sentence order,ColdWarparagraph continuation,ten discretionary wraps,one keyword compound join and complete keyword exclusion. All434other selections/statuses,laterq264prose and every raw source unchanged. q278preview remains separate and unresolved.',
        'source_boundary_reviews_added': 1, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
              inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (work / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v35.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            before = previous[family][item['paper_id']]
            if item['paper_id'] != pid:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated selected bytes/status changed: ' + item['paper_id'])
            elif built.text_and_spans(item)[0] != (summary if family == 'abstract' else author) or item['status'] != ('verified' if family == 'abstract' else before['status']):
                raise ValueError('Restored q264selection/status differs')
    if built.document(pid)['raw_pages_sha256'] != old['raw_pages_sha256'] or later_signature(built.document(pid)) != later_signature(old):
        raise ValueError('q264raw or later source/text changed')
    result = validate(output, work, True)
    if (result['defects'] != expected_defects or result['totals'] != expected_totals or
            result['source_completeness_accepted'] or not result['structural_integrity_pass']):
        raise ValueError('Unexpected counts/defects/acceptance; retain failed candidate')
    if any(file_hash(Path(path)) != sha for mapping in bindings.values() for path, sha in mapping.items()):
        raise ValueError('Source proof changed during build')
    if any(file_hash(work / 'scripts' / name) != sha for name, sha in frozen.items()):
        raise ValueError('Frozen core changed during build')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
