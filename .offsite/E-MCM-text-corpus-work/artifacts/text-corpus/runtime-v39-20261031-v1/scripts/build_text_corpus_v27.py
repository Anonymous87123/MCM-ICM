"""Freeze seven exact reviewed wrap resolutions; preserve all author text bytes."""
import os
from pathlib import Path

from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash, json_new, read_json, write_new
from validate_text_corpus import validate


def main():
    work = Path(__file__).resolve().parents[1]
    os.chdir(work)
    base = work / 'artifacts/text-corpus'
    parent = base / 'reflow-20261031-v26'
    output = base / 'reflow-20261031-v27'
    request = base / 'build-request-reflow-20261031-v27.json'
    report = base / 'integrity-reflow-20261031-v27.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Create-only build state exists; preserve it')
    catalog = Catalog(parent)
    accepted = read_json(base / 'integrity-reflow-20261031-v26.json')
    audit_path = base / 'span-origin-flow-full-20261031-v21.json'
    audit = read_json(audit_path)
    directory = base / 'reviews/20261031'
    repairs = [directory / f'q{n:03d}-summary-word-repairs-v2.json' for n in (114, 116)]
    exact = {str(p.resolve()): file_hash(p) for p in repairs}
    totals = audit['totals']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity or
            audit['parent_dataset_id'] != catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256'] != exact or
            (totals['papers'], totals['pages'], totals['source_lines']) != (435, 11552, 954866) or
            totals['contents_pages_before'] != 352 or totals['contents_pages_after'] != 352):
        raise ValueError('Exact frozen full prospective replay required')
    preflight_path = directory / 'q114-q116-wrap-resolution-preflight-v1.json'
    preflight = read_json(preflight_path)
    if (preflight['parent_dataset_id'] != catalog.identity or preflight['proof_files'] != exact or
            [c['flags_resolved'] for c in preflight['contracts']] != [6, 1] or
            any(not c['source_lines_unchanged'] or not c['author_text_unchanged'] or
                not c['other_open_defects_unchanged'] for c in preflight['contracts'])):
        raise ValueError('Individual source preflight differs')
    frozen = {name: file_hash(work / 'scripts' / name) for name in audit['implementation_sha256']}
    if frozen != audit['implementation_sha256']:
        raise ValueError('Audited implementation changed')
    frozen.update({name: file_hash(work / 'scripts' / name) for name in
                   ('index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')})
    scope = read_json(parent / 'scope.json')
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    inputs = {field: [] for field in fields}
    replacements = {str((directory / f'q{n:03d}-summary-word-repairs-v1.json').resolve()): path
                    for n, path in zip((114, 116), repairs)}
    replaced = set()
    for field in fields:
        for name, sha in scope.get(field, {}).items():
            path = Path(name)
            if file_hash(path) != sha:
                raise ValueError('Previously accepted proof changed: ' + name)
            if field == 'text_repair_sha256' and str(path.resolve()) in replacements:
                replacement = replacements[str(path.resolve())]
                transfer = read_json(replacement)['binding_transfer']
                if (transfer['parent_dataset_id'] != catalog.identity or
                        transfer['previous_external_file_sha256'] != sha):
                    raise ValueError('Replacement lacks exact previous external proof')
                inputs[field].append(replacement)
                replaced.add(str(path.resolve()))
            else:
                inputs[field].append(path)
    if replaced != set(replacements) or len(inputs['ocr_manifest_sha256']) != 53:
        raise ValueError('Both exact replacements and unchanged53OCR inputs required')
    native = base / 'native-20261029-v1'
    native_id = Catalog(native).identity
    if native_id != scope['parent_dataset_id']:
        raise ValueError('Original native generation required')
    bindings = {field: {str(p.resolve()): file_hash(p) for p in paths} for field, paths in inputs.items()}
    old_abstract = {s['paper_id']: s for s in catalog.select('abstract')}
    old_author = {s['paper_id']: s['text_sha256'] for s in catalog.select('all_author_text')}
    metrics = base / 'span-metrics-20261030-v1'
    json_new(request, {'native_dataset_id': native_id, 'previous_candidate_dataset_id': catalog.identity,
        'prospective_report_sha256': file_hash(audit_path), 'preflight_sha256': file_hash(preflight_path),
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'query_policy_sha256': file_hash(work / 'scripts/corpus_queries.py'),
        'change': 'Explicitly resolve seven source-checked wrap flags in q114/q116. All435 abstract and all-author text bytes must remain unchanged; all other open defects remain.',
        'source_boundary_reviews_added': 0, 'whole_paper_acceptances_added': 0,
        'ai_reading_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'],
              inputs['text_repair_sha256'], inputs['absence_review_sha256'], inputs['layout_review_sha256'],
              metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (work / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v27.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for item in built.select('abstract'):
        old = old_abstract[item['paper_id']]
        if item['text_sha256'] != old['text_sha256']:
            raise ValueError('Abstract bytes changed: ' + item['paper_id'])
        expected_status = 'verified' if item['paper_id'] == 'P-B-2017-56731-a60a9459' else old['status']
        if item['status'] != expected_status:
            raise ValueError('Unrelated source status changed: ' + item['paper_id'])
    if any(s['text_sha256'] != old_author[s['paper_id']] for s in built.select('all_author_text')):
        raise ValueError('Author text changed')
    result = validate(output, work, True)
    expected_defects = dict(accepted['defects'])
    expected_defects['hyphen_join_review'] -= 7
    if (result['defects'] != expected_defects or result['totals'] != accepted['totals'] or
            result['source_completeness_accepted']):
        raise ValueError('Unrelated structural counts/defects or whole-source acceptance changed')
    if any(file_hash(Path(p)) != sha for mapping in bindings.values() for p, sha in mapping.items()):
        raise ValueError('Source proof changed during build')
    if any(file_hash(work / 'scripts' / name) != sha for name, sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report, result)
    print(result, flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Failed candidate retained without acceptance')


if __name__ == '__main__':
    main()
