"""Promote two individually checked summaries; guard all remaining paper bytes."""
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


def later_signature(document):
    return [(block['source_line_ids'], block['text'], block['kind'], block['issues'])
            for block in all_author_blocks(document) if min(block['source_pages']) > 1]


def main():
    work = Path(__file__).resolve().parents[1]
    os.chdir(work)
    base = work / 'artifacts/text-corpus'
    parent = base / 'reflow-20261031-v30'
    output = base / 'reflow-20261031-v31'
    request = base / 'build-request-reflow-20261031-v31.json'
    report = base / 'integrity-reflow-20261031-v31.json'
    if any(path.exists() for path in (output, request, report)):
        raise ValueError('Create-only build state exists; preserve it')
    catalog = Catalog(parent)
    former = Catalog(base / 'reflow-20261031-v29')
    accepted = read_json(base / 'integrity-reflow-20261031-v30.json')
    audit_path = base / 'span-origin-flow-full-20261031-v25.json'
    audit = read_json(audit_path)
    directory = base / 'reviews/20261031'
    added = {field: [directory / f'q{queue}-summary-{suffix}-v1.json' for queue in (244, 248)]
        for field, suffix in (('layout_review_sha256', 'layout'), ('text_repair_sha256', 'word-repairs'),
                              ('source_review_sha256', 'source-review'))}
    exact = {str(path.resolve()): file_hash(path) for paths in added.values() for path in paths}
    totals = audit['totals']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity or
            audit['parent_dataset_id'] != catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256'] != exact or
            (totals['papers'], totals['pages'], totals['source_lines']) != (435, 11552, 954866) or
            totals['contents_pages_before'] != 352 or totals['contents_pages_after'] != 352):
        raise ValueError('Exact accepted parent and full prospective replay required')
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
                raise ValueError('Previously accepted source input changed: ' + name)
            inputs[field].append(path)
        inputs[field].extend(added.get(field, []))
        if len({str(path.resolve()) for path in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    native = base / 'native-20261029-v1'
    native_id = Catalog(native).identity
    if native_id != scope['parent_dataset_id'] or len(inputs['ocr_manifest_sha256']) != 53:
        raise ValueError('Original native generation and53unchanged OCR inputs required')
    bindings = {field: {str(path.resolve()): file_hash(path) for path in paths} for field, paths in inputs.items()}
    previous = {family: {item['paper_id']: item for item in catalog.select(family)}
                for family in ('abstract', 'all_author_text')}
    expected_defects = Counter(accepted['defects'])
    expected_totals = dict(accepted['totals'])
    expected_totals['boundary_verified'] += 2
    targets = {}
    transfers = {}
    metrics = base / 'span-metrics-20261030-v1'
    for queue, length, paragraphs in ((244, 2341, 7), (248, 3296, 5)):
        preflight_path = directory / f'q{queue}-summary-preflight-v1.json'
        preflight = read_json(preflight_path)
        pid = preflight['paper_id']
        old = catalog.document(pid)
        before = former.document(pid)
        target_proofs = {field: next(path for path in paths if f'q{queue}-' in path.name) for field, paths in added.items()}
        proof_hashes = {str(path.resolve()): file_hash(path) for path in target_proofs.values()}
        differences = {key for key in set(before) | set(old) if before.get(key) != old.get(key)}
        content_sha = digest(encoded({key: value for key, value in old.items() if key != 'scope_id'}))
        if (differences != {'scope_id'} or before['scope_id'] != read_json(former.root / 'scope.json')['scope_id'] or
                old['scope_id'] != scope['scope_id'] or
                content_sha != digest(encoded({key: value for key, value in before.items() if key != 'scope_id'})) or
                preflight['parent_dataset_id'] != former.identity or preflight['proof_sha256'] != proof_hashes or
                preflight['characters'] != length or preflight['logical_author_paragraphs'] != paragraphs or
                not preflight['source_lines_accounted_once'] or not preflight['later_author_text_unchanged'] or
                old.get('layout_reviews') or old.get('text_repair_reviews') or old.get('paragraph_join_reviews')):
            raise ValueError('Exact unchanged source/preflight binding required: ' + pid)
        summary = (directory / f'q{queue}-summary-preview-v1.md').read_text(encoding='utf-8').removesuffix('\n')
        if digest(summary.encode()) != preflight['text_sha256']:
            raise ValueError('Actually read restored preview changed')
        pages = rows(parent / 'papers' / pid / 'raw/pages.jsonl')
        working, _ = prepare_flow_pages(old, pages, metrics)
        layouts, _ = prepare_review_bundles([target_proofs['layout_review_sha256']], identity_fields=('paper_id',), application_status='applied text reading lanes; not whole-section source acceptance')
        applied = apply_layout_reviews(old, working, layouts)
        candidate = make_document({key: old[key] for key in ('paper_id', 'problem_type', 'year', 'queue_position',
            'page_count', 'source_sha256', 'source_relative_path', 'raw_pages_sha256')}, working, improved=True)
        candidate['layout_reviews'] = applied
        resolve_exact_comparisons(candidate, pages, (parent / 'papers' / pid / 'raw/pdftotext.bin').read_bytes())
        apply_text_repairs(candidate, [read_json(target_proofs['text_repair_sha256'])])
        apply_reviews(candidate, [read_json(target_proofs['source_review_sha256'])])
        validate_layout_reviews(candidate, pages)
        rest = [block for block in all_author_blocks(old) if min(block['source_pages']) > 1]
        author = summary + '\n\n' + text_with_block_spans(rest)[0]
        target_audit = next(item for item in audit['papers'] if item['paper_id'] == pid)
        if (len(candidate['blocks']) != target_audit['blocks'] or len(candidate['sections']) != target_audit['sections'] or
                text_with_block_spans(all_author_blocks(candidate))[0] != author or later_signature(old) != later_signature(candidate)):
            raise ValueError('Complete source Summary must be sole author-text change')
        expected_defects.subtract(open_defects(old))
        expected_defects.update(open_defects(candidate))
        expected_totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
        expected_totals['sections'] += len(candidate['sections']) - len(old['sections'])
        targets[pid] = {'abstract': summary, 'all_author_text': author, 'later_signature': later_signature(old)}
        transfers[pid] = {'preflight_sha256': file_hash(preflight_path), 'preflight_dataset_id': former.identity,
            'previous_document_sha256': file_hash(former.root / former.by_id[pid]['document']),
            'current_document_sha256': file_hash(parent / catalog.by_id[pid]['document']),
            'only_changed_field': 'scope_id', 'previous_scope_id': before['scope_id'], 'current_scope_id': old['scope_id'],
            'paper_content_excluding_scope_id_sha256': content_sha, 'old_open_defects': dict(open_defects(old)),
            'new_open_defects': dict(open_defects(candidate))}
    expected_defects = {code: count for code, count in expected_defects.items() if count}
    json_new(request, {'native_dataset_id': native_id, 'previous_candidate_dataset_id': catalog.identity,
        'prospective_report_sha256': file_hash(audit_path), 'preflight_binding_transfers': transfers,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'expected_open_defects': expected_defects, 'expected_totals': expected_totals,
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'change': 'Restore individually source-checked q244seven-paragraph/q248five-paragraph summaries,ten exact author wraps,q248same-baseline native ordering and keyword boundaries. All433other selections/statuses and both later author texts unchanged.',
        'source_boundary_reviews_added': 2, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'],
              inputs['text_repair_sha256'], inputs['absence_review_sha256'], inputs['layout_review_sha256'],
              metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (work / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v31.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            old = previous[family][item['paper_id']]
            target = targets.get(item['paper_id'])
            if target is None:
                if item['text_sha256'] != old['text_sha256'] or item['status'] != old['status']:
                    raise ValueError('Unrelated selected bytes/status changed: ' + item['paper_id'])
            elif built.text_and_spans(item)[0] != target[family] or item['status'] != ('verified' if family == 'abstract' else old['status']):
                raise ValueError('Source-restored selection/status differs: ' + item['paper_id'])
    for pid, target in targets.items():
        if later_signature(built.document(pid)) != target['later_signature']:
            raise ValueError('Later author source/text changed: ' + pid)
    result = validate(output, work, True)
    if (result['defects'] != expected_defects or result['totals'] != expected_totals or
            result['source_completeness_accepted'] or not result['structural_integrity_pass']):
        raise ValueError('Unexpected counts/defects/whole-source acceptance; retain failed candidate')
    if any(file_hash(Path(path)) != sha for mapping in bindings.values() for path, sha in mapping.items()):
        raise ValueError('Source proof changed during build')
    if any(file_hash(work / 'scripts' / name) != sha for name, sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
