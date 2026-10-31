"""Promote q256's complete source-checked Summary with every other paper guarded."""
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
from text_corpus import digest, encoded, file_hash, json_new, make_document, read_json, rows, text_with_block_spans, write_new
from validate_text_corpus import validate


def open_defects(document):
    return Counter(item['code'] for item in document['defects'] if item.get('status') != 'resolved')


def main():
    work = Path(__file__).resolve().parents[1]
    os.chdir(work)
    base = work / 'artifacts/text-corpus'
    parent = base / 'reflow-20261031-v29'
    output = base / 'reflow-20261031-v30'
    request = base / 'build-request-reflow-20261031-v30.json'
    report = base / 'integrity-reflow-20261031-v30.json'
    if any(path.exists() for path in (output, request, report)):
        raise ValueError('Create-only build state exists; preserve it')
    catalog = Catalog(parent)
    accepted = read_json(base / 'integrity-reflow-20261031-v29.json')
    audit_path = base / 'span-origin-flow-full-20261031-v24.json'
    audit = read_json(audit_path)
    directory = base / 'reviews/20261031'
    added = {'layout_review_sha256': directory / 'q256-summary-layout-v1.json',
             'text_repair_sha256': directory / 'q256-summary-word-repairs-v1.json',
             'source_review_sha256': directory / 'q256-summary-source-review-v1.json'}
    exact = {str(path.resolve()): file_hash(path) for path in added.values()}
    totals = audit['totals']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity or
            audit['parent_dataset_id'] != catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256'] != exact or
            (totals['papers'], totals['pages'], totals['source_lines']) != (435, 11552, 954866) or
            totals['contents_pages_before'] != 352 or totals['contents_pages_after'] != 352):
        raise ValueError('Exact full prospective replay required')
    preflight_path = directory / 'q256-summary-preflight-v1.json'
    preflight = read_json(preflight_path)
    pid = preflight['paper_id']
    old_doc = catalog.document(pid)
    former = Catalog(base / 'reflow-20261031-v28')
    former_doc = former.document(pid)
    differences = {key for key in set(former_doc) | set(old_doc) if former_doc.get(key) != old_doc.get(key)}
    if (differences != {'scope_id'} or
            former_doc['scope_id'] != read_json(former.root / 'scope.json')['scope_id'] or
            old_doc['scope_id'] != read_json(parent / 'scope.json')['scope_id']):
        raise ValueError('Only each generation\'s exact bound scope_id may differ')
    content_sha = digest(encoded({key: value for key, value in old_doc.items() if key != 'scope_id'}))
    if (preflight['parent_dataset_id'] != former.identity or preflight['proof_sha256'] != exact or
            content_sha != digest(encoded({key: value for key, value in former_doc.items() if key != 'scope_id'})) or
            preflight['characters'] != 3433 or preflight['logical_author_paragraphs'] != 3 or
            preflight['marginal_grid_source_lines_retained'] != 687 or not preflight['source_lines_accounted_once']):
        raise ValueError('Older preflight must bind unchanged paper content and exact proof set')
    if old_doc.get('layout_reviews') or old_doc.get('text_repair_reviews') or old_doc.get('paragraph_join_reviews'):
        raise ValueError('Previous q256proof needs explicit replay')
    expected_summary = (directory / 'q256-summary-preview-v1.md').read_text(encoding='utf-8').removesuffix('\n')
    if digest(expected_summary.encode()) != preflight['text_sha256']:
        raise ValueError('Actually read restored Summary changed')
    frozen = {name: file_hash(work / 'scripts' / name) for name in audit['implementation_sha256']}
    if frozen != audit['implementation_sha256']:
        raise ValueError('Audited implementation changed')
    frozen.update({name: file_hash(work / 'scripts' / name) for name in
                   ('index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')})
    scope = read_json(parent / 'scope.json')
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    inputs = {field: [] for field in fields}
    for field in fields:
        for name, sha in scope.get(field, {}).items():
            path = Path(name)
            if file_hash(path) != sha:
                raise ValueError('Previously accepted proof changed: ' + name)
            inputs[field].append(path)
        if field in added:
            inputs[field].append(added[field])
        if len({str(path.resolve()) for path in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    if len(inputs['ocr_manifest_sha256']) != 53:
        raise ValueError('Unchanged53OCR inputs required')
    native = base / 'native-20261029-v1'
    native_id = Catalog(native).identity
    if native_id != scope['parent_dataset_id']:
        raise ValueError('Original native generation required')
    bindings = {field: {str(path.resolve()): file_hash(path) for path in paths} for field, paths in inputs.items()}
    previous = {family: {item['paper_id']: item for item in catalog.select(family)}
                for family in ('abstract', 'all_author_text')}
    old_rest = [block for block in all_author_blocks(old_doc) if min(block['source_pages']) > 2]
    rest_text = text_with_block_spans(old_rest)[0]
    metrics = base / 'span-metrics-20261030-v1'
    pages = rows(parent / 'papers' / pid / 'raw/pages.jsonl')
    working, _ = prepare_flow_pages(old_doc, pages, metrics)
    layouts, _ = prepare_review_bundles([added['layout_review_sha256']], identity_fields=('paper_id',), application_status='applied text reading lanes; not whole-section source acceptance')
    applied = apply_layout_reviews(old_doc, working, layouts)
    candidate = make_document({key: old_doc[key] for key in ('paper_id', 'problem_type', 'year', 'queue_position',
        'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}, working, improved=True)
    candidate['layout_reviews'] = applied
    resolve_exact_comparisons(candidate, pages, (parent / 'papers' / pid / 'raw/pdftotext.bin').read_bytes())
    apply_text_repairs(candidate, [read_json(added['text_repair_sha256'])])
    apply_reviews(candidate, [read_json(added['source_review_sha256'])])
    validate_layout_reviews(candidate, pages)
    expected_defects = Counter(accepted['defects'])
    expected_defects.subtract(open_defects(old_doc))
    expected_defects.update(open_defects(candidate))
    expected_defects = {code: count for code, count in expected_defects.items() if count}
    target_audit = next(item for item in audit['papers'] if item['paper_id'] == pid)
    if (len(candidate['blocks']) != target_audit['blocks'] or len(candidate['sections']) != target_audit['sections'] or
            text_with_block_spans(all_author_blocks(candidate))[0] != expected_summary + '\n\n' + rest_text):
        raise ValueError('Restored Summary must be the sole author-text change')
    json_new(request, {'native_dataset_id': native_id, 'previous_candidate_dataset_id': catalog.identity,
        'prospective_report_sha256': file_hash(audit_path), 'preflight_sha256': file_hash(preflight_path),
        'preflight_binding_transfer': {'previous_preflight_dataset_id': former.identity,
            'previous_document_sha256': file_hash(former.root / former.by_id[pid]['document']),
            'current_document_sha256': file_hash(parent / catalog.by_id[pid]['document']),
            'only_changed_field': 'scope_id', 'previous_scope_id': former_doc['scope_id'],
            'current_scope_id': old_doc['scope_id'], 'paper_content_excluding_scope_id_sha256': content_sha},
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_open_defects': expected_defects,
        'target_old_open_defects': dict(open_defects(old_doc)), 'target_new_open_defects': dict(open_defects(candidate)),
        'change': 'Restore complete q256three-paragraph Summary, four exact wraps,687marginal glyphs in retained furniture and OCR Contents ownership. Source-checked layout groups precede automatic microtext filtering;434other paper selections and laterq256author prose must remain unchanged.',
        'source_boundary_reviews_added': 1, 'whole_paper_acceptances_added': 0,
        'ai_reading_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'],
              inputs['text_repair_sha256'], inputs['absence_review_sha256'], inputs['layout_review_sha256'],
              metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (work / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v30.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            old = previous[family][item['paper_id']]
            if item['paper_id'] != pid:
                if item['text_sha256'] != old['text_sha256'] or item['status'] != old['status']:
                    raise ValueError('Unrelated selected bytes/status changed: ' + item['paper_id'])
                continue
            text, _ = built.text_and_spans(item)
            expected = expected_summary if family == 'abstract' else expected_summary + '\n\n' + rest_text
            expected_status = 'verified' if family == 'abstract' else old['status']
            if text != expected or item['status'] != expected_status:
                raise ValueError('Exact source-restored q256selection/status differs: ' + family)
    new_doc = built.document(pid)
    new_rest = [block for block in all_author_blocks(new_doc) if min(block['source_pages']) > 2]
    signature = lambda blocks: [(block['source_line_ids'], block['text'], block['kind'], block['issues']) for block in blocks]
    if signature(old_rest) != signature(new_rest):
        raise ValueError('Later q256author prose/source ownership changed')
    result = validate(output, work, True)
    expected_totals = dict(accepted['totals'])
    expected_totals['blocks'] += len(candidate['blocks']) - len(old_doc['blocks'])
    expected_totals['sections'] += len(candidate['sections']) - len(old_doc['sections'])
    expected_totals['boundary_verified'] += 1
    if (result['defects'] != expected_defects or result['totals'] != expected_totals or
            result['source_completeness_accepted'] or not result['structural_integrity_pass']):
        raise ValueError('Unexpected counts/defects or whole-source acceptance; retain failed candidate')
    if any(file_hash(Path(path)) != sha for mapping in bindings.values() for path, sha in mapping.items()):
        raise ValueError('Source proof changed during build')
    if any(file_hash(work / 'scripts' / name) != sha for name, sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
