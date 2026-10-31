"""Promote individually source-read q307/q308/q309 summaries;no broad text rule."""
from collections import Counter
import copy
import os
from pathlib import Path
import shutil
import sys

WORK = Path(r'F:\MCM\mcm-skill-work')
STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
RUNTIME = STORE / 'runtime-v39-20261031-v1'
sys.path.insert(0, str(RUNTIME / 'scripts'))
from corpus_queries import all_author_blocks
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import digest, file_hash, json_new, read_json, text_with_block_spans, write_new
from validate_text_corpus import validate


def pending(document):
    return Counter(d['code'] for d in document['defects'] if d.get('status') != 'resolved')


def later(document, excluded):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(document)
            if min(b['source_pages']) > 1 and b['source_line_ids'] not in excluded]


def main():
    os.chdir(WORK)
    base = WORK / 'artifacts/text-corpus'
    parent, output = STORE / 'reflow-20261031-v41', STORE / 'reflow-20261031-v42'
    request, report = STORE / 'build-request-reflow-20261031-v42.json', STORE / 'integrity-reflow-20261031-v42.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Create-only build exists;preserve it')
    if shutil.disk_usage(STORE).free < 30 * 1024**3:
        raise ValueError('Require30GiBfree;no cleanup authorized')
    accepted = read_json(STORE / 'integrity-reflow-20261031-v41.json')
    catalog = Catalog(parent)
    if (catalog.identity != 'ee6baee4e95da88d7ebb2f4b64956b2856eed61ea8906faf554a09420dd3493e'
            or accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']):
        raise ValueError('Require accepted exactv41')
    staged_parent = Catalog(STORE / 'reflow-20261031-v40')
    directory = STORE / 'reviews/20261031'
    helper = Path(__file__).with_name('stage_text_summary_spec_v4.py')
    helper_sha = file_hash(helper)
    targets = {}
    transfer = {}
    extra_inputs = {'layout_review_sha256': [], 'source_review_sha256': [], 'text_repair_sha256': []}
    bound_stage = {str(helper): helper_sha}
    expected_defects, expected_totals = Counter(accepted['defects']), dict(accepted['totals'])
    for queue, version, length, paras, wraps in [(307, 1, 2218, 5, 6), (309, 1, 3481, 6, 4)]:
        prefix = f'q{queue}-summary'
        preflight_path = directory / f'{prefix}-preflight-v{version}.json'
        preflight = read_json(preflight_path)
        bound_stage[str(preflight_path)] = file_hash(preflight_path)
        pid = preflight['paper_id']
        old, source_old = catalog.document(pid), staged_parent.document(pid)
        before, after = copy.deepcopy(source_old), copy.deepcopy(old)
        first_scope, second_scope = before.pop('scope_id'), after.pop('scope_id')
        if before != after or first_scope == second_scope:
            raise ValueError('Stage transfer must change only corpus scope identity')
        transfer[pid] = {'old_scope_id': first_scope, 'new_scope_id': second_scope,
                         'all_other_document_fields_equivalent': True}
        if (old['queue_position'] != queue or preflight['parent_dataset_id'] != staged_parent.identity
                or preflight['raw_pages_sha256'] != old['raw_pages_sha256']
                or preflight['source_sha256'] != old['source_sha256']
                or preflight['stager_sha256'] != helper_sha or preflight['characters'] != length
                or preflight['logical_author_paragraphs'] != paras
                or preflight['literal_wrap_occurrences_repaired'] != wraps
                or not preflight['source_lines_accounted_once'] or not preflight['later_actual_author_body_unchanged']
                or not preflight['section_boundaries_checked'] or preflight['whole_paper_source_acceptance']
                or preflight['ai_receipts_created'] or preflight['selected_source_status'] != 'verified in prospective stage only'):
            raise ValueError('Exact individually source-read summary preflight required')
        spec = directory / f'{prefix}-spec-v{version}.json'
        if file_hash(spec) != preflight['specification_sha256']:
            raise ValueError('Source specification changed')
        bound_stage[str(spec)] = file_hash(spec)
        for path, sha in preflight['proof_sha256'].items():
            if file_hash(Path(path)) != sha:
                raise ValueError('Exact staged source proof changed')
            bound_stage[path] = sha
        candidate = read_json(directory / f'{prefix}-candidate-v{version}.json')
        summary_path = directory / f'{prefix}-preview-v{version}.md'
        summary = summary_path.read_text(encoding='utf-8').removesuffix('\n')
        if len(summary) != length or digest(summary.encode()) != preflight['text_sha256']:
            raise ValueError('Complete restored summary bytes differ')
        bound_stage[str(summary_path)] = file_hash(summary_path)
        excluded = preflight['exact_later_metadata_source_ids_excluded']
        if excluded:
            raise ValueError('No later metadata exceptions authorized for these two summaries')
        for source_ids in excluded:
            previous = [b for b in all_author_blocks(old) if b['source_line_ids'] == source_ids]
            fixed = [b for b in candidate['blocks'] if b['source_line_ids'] == source_ids]
            if (len(previous) != 1 or len(fixed) != 1 or previous[0]['text'] != fixed[0]['text']
                    or fixed[0]['kind'] not in {'title', 'front_matter'}):
                raise ValueError('Exact metadata exception changed source bytes')
        rest = [b for b in all_author_blocks(old) if min(b['source_pages']) > 1 and b['source_line_ids'] not in excluded]
        author = summary + '\n\n' + text_with_block_spans(rest)[0]
        if later(old, excluded) != later(candidate, excluded) or text_with_block_spans(all_author_blocks(candidate))[0] != author:
            raise ValueError('Later actual body changed')
        targets[pid] = {'abstract': summary, 'all_author_text': author, 'excluded': excluded, 'candidate': candidate}
        for field, suffix in [('layout_review_sha256', 'layout'), ('source_review_sha256', 'source-review')]:
            extra_inputs[field].append(directory / f'{prefix}-{suffix}-v{version}.json')
        if preflight['has_text_repairs']:
            extra_inputs['text_repair_sha256'].append(directory / f'{prefix}-word-repairs-v{version}.json')
        elif (directory / f'{prefix}-word-repairs-v{version}.json').exists():
            raise ValueError('No empty/undeclared transcription review allowed')
        expected_defects.subtract(pending(old)); expected_defects.update(pending(candidate))
        expected_totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
        expected_totals['sections'] += len(candidate['sections']) - len(old['sections'])
        expected_totals['boundary_verified'] += 1
    # q308 required a separate source-adjudicated OCR stage,not the native-only helper.
    stage = directory / 'q308-summary-restoration-v1'
    preflight_path = stage / 'preflight.json'
    preflight = read_json(preflight_path)
    bind_path = directory / 'q308-native-binding-v1.json'
    binding = read_json(bind_path)
    pid = preflight['paper_id']
    old = catalog.document(pid)
    if (pid != 'P-D-2021-2106028-e54d016e' or old['queue_position'] != 308
            or preflight['parent_dataset_id'] != catalog.identity
            or preflight['source_sha256'] != old['source_sha256']
            or preflight['parent_raw_pages_sha256'] != old['raw_pages_sha256']
            or preflight['characters'] != 2233 or preflight['logical_author_paragraphs'] != 10 or preflight['original_ocr_lines'] != 43
            or preflight['unchanged_ocr_line_objects'] != 37
            or preflight['manually_source_transcribed_lines'] != [15,19,22,25,29,33]
            or preflight['literal_wrap_occurrences_repaired'] != 2
            or preflight['author_wraps_repaired'] != 1 or preflight['separate_keyword_wraps_repaired'] != 1
            or not preflight['complete_native_prose_equal_after_declared_ligature_expansion_and_wraps']
            or not preflight['source_lines_accounted_once'] or not preflight['later_actual_author_body_unchanged']
            or preflight['whole_paper_source_acceptance'] or preflight['ai_receipts_created']):
        raise ValueError('Exact individually source-read q308OCR stage required')
    bound_stage.update({str(stage / name): sha for name, sha in preflight['proof_sha256'].items()})
    bound_stage.update({str(preflight_path): file_hash(preflight_path), str(bind_path): file_hash(bind_path),
        str(stage / 'candidate.json'): file_hash(stage / 'candidate.json'),
        str(Path(__file__).with_name('stage_q308_summary_restoration_v1.py')): preflight['stager_sha256'],
        str(Path(__file__).with_name('bind_q308_native_metrics_v1.py')): binding['binder_sha256']})
    if (preflight['library_sha256'] != file_hash(RUNTIME / 'scripts/text_corpus.py')
            or binding['library_sha256'] != preflight['library_sha256']
            or binding['staged_preflight_sha256'] != file_hash(preflight_path)
            or binding['all_target_native_pages_freshly_rematched'] != 25
            or binding['all_metric_payloads_unchanged'] != 435 or binding['other_metric_complete_files_unchanged'] != 434
            or not binding['portable_page_proof_replay_pass']
            or binding['source_page_review_implementation_sha256'] != file_hash(RUNTIME / 'scripts/source_ocr_page_reviews.py')):
        raise ValueError('Exact native/OCR page replay binding required')
    if any(file_hash(Path(path)) != sha for path, sha in bound_stage.items()):
        raise ValueError('Individual stage proof changed')
    candidate = read_json(stage / 'candidate.json')
    summary = (stage / 'summary-preview.md').read_text(encoding='utf-8').removesuffix('\n')
    author = summary + '\n\n' + text_with_block_spans([b for b in all_author_blocks(old) if min(b['source_pages']) > 1])[0]
    if (len(summary) != preflight['characters'] or digest(summary.encode()) != preflight['text_sha256']
            or later(old, []) != later(candidate, []) or text_with_block_spans(all_author_blocks(candidate))[0] != author):
        raise ValueError('Complete q308Summary or later body differs')
    targets[pid] = {'abstract': summary, 'all_author_text': author, 'excluded': [], 'candidate': candidate}
    raw_overrides = {pid: preflight['raw_pages_sha256']}
    extra_inputs['ocr_manifest_sha256'] = [stage / 'manifest.json']
    extra_inputs['layout_review_sha256'].append(stage / 'layout.json')
    extra_inputs['source_review_sha256'].append(stage / 'source-review.json')
    extra_inputs['text_repair_sha256'].append(stage / 'word-repairs.json')
    expected_defects.subtract(pending(old)); expected_defects.update(pending(candidate))
    expected_totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
    expected_totals['sections'] += len(candidate['sections']) - len(old['sections'])
    expected_totals['boundary_verified'] += 1
    expected_totals['source_lines'] += 43
    expected_defects = {code: count for code, count in expected_defects.items() if count}
    scope = read_json(parent / 'scope.json')
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    inputs = {field: [] for field in fields}
    for field in fields:
        for path, sha in scope.get(field, {}).items():
            if file_hash(Path(path)) != sha:
                raise ValueError('Accepted evidence changed')
            inputs[field].append(Path(path))
        inputs[field].extend(extra_inputs.get(field, []))
        if len({str(p.resolve()) for p in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    metrics = STORE / 'span-metrics-20261031-q308-v1'
    if len(inputs['ocr_manifest_sha256']) != 58 or file_hash(metrics / 'manifest.json') != binding['metrics_manifest_sha256']:
        raise ValueError('Preserve57existingOCRinputs,add onlyq308,and use freshly bound native metrics')
    names = ('source_span_metrics.py', 'text_corpus.py', 'preview_span_origin_flow.py', 'source_text_repairs.py',
             'source_layout_reviews.py', 'source_absence_reviews.py', 'resegment_text_corpus.py', 'corpus_queries.py',
             'corpus_reader.py', 'source_paragraph_reviews.py', 'source_ocr_page_reviews.py', 'extract_text_span_metrics.py',
             'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')
    frozen = {name: file_hash(RUNTIME / 'scripts' / name) for name in names}
    parent_code = read_json(STORE / 'build-request-reflow-20261031-v41.json')['implementation_sha256']
    if any(frozen[name] != parent_code[name] for name in names):
        raise ValueError('Accepted runtime must remain unchanged')
    bindings = {field: {str(p.resolve()): file_hash(p) for p in paths} for field, paths in inputs.items()}
    previous = {family: {x['paper_id']: x for x in catalog.select(family)} for family in ('abstract', 'all_author_text')}
    if any(previous['abstract'][pid]['status'] != 'present-unverified' for pid in targets):
        raise ValueError('Three previously unverified summaries required')
    native = base / 'native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native corpus changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'individual_source_stage_sha256': bound_stage, 'explicit_unchanged_source_transfer': transfer,
        'raw_pages_sha256_overrides': raw_overrides,
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_totals': expected_totals, 'expected_open_defects': expected_defects,
        'change': 'Three individually source-read summariesq307throughq309complete prose restored.q307fiveparagraphs/sixwraps;q308tenprose-listunits,source-adjudicatedOCRwithsixprintedbullets/twospacesrestoredandtwoexactwraps;q309sixparagraphs/fourwraps.Form,title,fullkeywordsandpromotion retained separately.All432otherselections/statuses/rawandalllateractualbodyunchanged.Nativenativerawunchanged;q308originalnativeandoriginalOCRpreserved.Runtimeunchanged.',
        'source_boundary_reviews_added': 3, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
              inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (RUNTIME / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v42.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            pid = item['paper_id']; before = previous[family][pid]
            if pid not in targets:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated source selection changed')
            elif built.text_and_spans(item)[0] != targets[pid][family] or item['status'] != ('verified' if family == 'abstract' else before['status']):
                raise ValueError('Exact complete restored source selection/status differs')
    for pid in catalog.by_id:
        old, new = catalog.document(pid), built.document(pid)
        if new['raw_pages_sha256'] != raw_overrides.get(pid, old['raw_pages_sha256']):
            raise ValueError('Raw source evidence changed')
        if pid in targets and later(old, targets[pid]['excluded']) != later(new, targets[pid]['excluded']):
            raise ValueError('Later actual source body changed')
    result = validate(output, WORK, True)
    if (result['totals'] != expected_totals or result['defects'] != expected_defects
            or not result['structural_integrity_pass'] or result['source_completeness_accepted']):
        raise ValueError('Unexpected global counts/defects/acceptance;preserve failed candidate')
    all_bound = [bound_stage, *bindings.values(), {str(RUNTIME / 'scripts' / name): sha for name, sha in frozen.items()}]
    if any(file_hash(Path(path)) != sha for group in all_bound for path, sha in group.items()):
        raise ValueError('Frozen source proofs/core changed')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
