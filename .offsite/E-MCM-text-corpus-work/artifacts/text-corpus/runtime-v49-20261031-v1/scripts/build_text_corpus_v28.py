"""Freeze two source-local absences and recover one intact excluded prose line."""
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
    parent = base / 'reflow-20261031-v27'
    output = base / 'reflow-20261031-v28'
    request = base / 'build-request-reflow-20261031-v28.json'
    report = base / 'integrity-reflow-20261031-v28.json'
    if any(path.exists() for path in (output, request, report)):
        raise ValueError('Create-only build state exists; preserve it')
    catalog = Catalog(parent)
    accepted = read_json(base / 'integrity-reflow-20261031-v27.json')
    audit_path = base / 'span-origin-flow-full-20261031-v22.json'
    audit = read_json(audit_path)
    directory = base / 'reviews/20261031'
    repair = directory / 'q236-caption-prose-line-repair-v1.json'
    absences = [directory / f'q{n:03d}-abstract-absence-v1.json' for n in (11, 169)]
    exact = {str(path.resolve()): file_hash(path) for path in [repair, *absences]}
    totals = audit['totals']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity or
            audit['parent_dataset_id'] != catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256'] != exact or
            (totals['papers'], totals['pages'], totals['source_lines']) != (435, 11552, 954866) or
            totals['contents_pages_before'] != 352 or totals['contents_pages_after'] != 352):
        raise ValueError('Exact full prospective replay required')
    preflight_path = directory / 'q236-caption-prose-line-preflight-v1.json'
    preflight = read_json(preflight_path)
    if (preflight['parent_dataset_id'] != catalog.identity or preflight['proof_sha256'] != file_hash(repair) or
            not all(preflight[key] for key in ('source_lines_accounted_once', 'literal_block_bytes_unchanged',
                                               'other_kinds_and_defects_unchanged')) or
            preflight['restored_block_id'] != 'b000014' or preflight['restored_prose_characters'] != 78 or
            (preflight['reader_characters_before'], preflight['reader_characters_after']) != (2668, 2748)):
        raise ValueError('Exact single-line preflight differs')
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
    if len(inputs['ocr_manifest_sha256']) != 53:
        raise ValueError('Unchanged53OCR inputs required')
    inputs['text_repair_sha256'].append(repair)
    inputs['absence_review_sha256'].extend(absences)
    for paths in inputs.values():
        if len({str(path.resolve()) for path in paths}) != len(paths):
            raise ValueError('Duplicate new input')
    native = base / 'native-20261029-v1'
    native_id = Catalog(native).identity
    if native_id != scope['parent_dataset_id']:
        raise ValueError('Original native generation required')
    bindings = {field: {str(path.resolve()): file_hash(path) for path in paths} for field, paths in inputs.items()}
    old_abstract = {item['paper_id']: item for item in catalog.select('abstract')}
    old_author = {item['paper_id']: item for item in catalog.select('all_author_text')}
    repaired_pid = preflight['paper_id']
    absent_pids = {read_json(path)['paper_id'] for path in absences}
    if any(old_abstract[pid]['status'] != 'unresolved' or old_abstract[pid]['characters'] for pid in absent_pids):
        raise ValueError('Only empty unresolved abstract preimages may change to absent')
    metrics = base / 'span-metrics-20261030-v1'
    json_new(request, {'native_dataset_id': native_id, 'previous_candidate_dataset_id': catalog.identity,
        'prospective_report_sha256': file_hash(audit_path), 'preflight_sha256': file_hash(preflight_path),
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'query_policy_sha256': file_hash(work / 'scripts/corpus_queries.py'),
        'change': 'Source-local abstract absence for q11/q169; recover exactly78existing q236prose characters excluded as a false caption. Preserve all other author bytes/flags; paragraph seams remain pending.',
        'source_boundary_reviews_added': 0, 'whole_paper_acceptances_added': 0,
        'ai_reading_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'],
              inputs['text_repair_sha256'], inputs['absence_review_sha256'], inputs['layout_review_sha256'],
              metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (work / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v28.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    deltas = {}
    for family, previous in (('abstract', old_abstract), ('all_author_text', old_author)):
        changed = []
        for item in built.select(family):
            old = previous[item['paper_id']]
            if item['paper_id'] == repaired_pid:
                before, _ = catalog.text_and_spans(old)
                after, _ = built.text_and_spans(item)
                doc = catalog.document(repaired_pid)
                by_id = {block['block_id']: block for block in doc['blocks']}
                a, middle, b = [by_id[key]['text'] for key in ('b000013', 'b000014', 'b000015')]
                seam = a + '\n\n' + b
                replacement = a + '\n\n' + middle + '\n\n' + b
                if before.count(seam) != 1 or after != before.replace(seam, replacement):
                    raise ValueError('Source bytes changed beyond exact one-line insertion: ' + family)
                changed.append(item['paper_id'])
            elif item['text_sha256'] != old['text_sha256']:
                raise ValueError('Unrelated author bytes changed: ' + item['paper_id'])
            expected_status = 'verified-absent' if family == 'abstract' and item['paper_id'] in absent_pids else old['status']
            if item['status'] != expected_status:
                raise ValueError('Unrelated source status changed: ' + family + ':' + item['paper_id'])
        if changed != [repaired_pid]:
            raise ValueError('Exact repaired selection missing')
        deltas[family] = {'changed_papers': changed, 'additional_characters_including_separators': 80}
    result = validate(output, work, True)
    if (result['defects'] != accepted['defects'] or result['totals'] != accepted['totals'] or
            result['source_completeness_accepted'] or not result['structural_integrity_pass']):
        raise ValueError('Unrelated structural counts/defects or whole-source acceptance changed')
    if any(file_hash(Path(path)) != sha for mapping in bindings.values() for path, sha in mapping.items()):
        raise ValueError('Source proof changed during build')
    if any(file_hash(work / 'scripts' / name) != sha for name, sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report, result)
    json_new(base / 'generation-delta-reflow-20261031-v28.json', {
        'parent_dataset_id': catalog.identity, 'dataset_id': built.identity, 'families': deltas,
        'new_source_local_abstract_absences': sorted(absent_pids), 'other_flags_and_counts_unchanged': True,
        'whole_paper_acceptance': False, 'ai_receipts_created': 0})
    print(result, flush=True)


if __name__ == '__main__':
    main()
