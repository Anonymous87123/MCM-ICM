"""Promote the individually source-adjudicated nine-paragraph q305Summary."""
from collections import Counter
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
from text_corpus import digest, file_hash, json_new, read_json, rows, text_with_block_spans, write_new
from validate_text_corpus import validate


def pending(document):
    return Counter(d['code'] for d in document['defects'] if d.get('status') != 'resolved')


def later(document):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(document)
            if min(b['source_pages']) > 1]


def main():
    os.chdir(WORK)
    base = WORK / 'artifacts/text-corpus'
    parent, output = STORE / 'reflow-20261031-v39', STORE / 'reflow-20261031-v40'
    request = STORE / 'build-request-reflow-20261031-v40.json'
    report = STORE / 'integrity-reflow-20261031-v40.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Create-only generation exists;preserve it')
    if shutil.disk_usage(STORE).free < 30 * 1024**3:
        raise ValueError('Require30GiBfree;no cleanup authorized')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v39.json')
    if (catalog.identity != 'd6b2d80eb3f7d220a15dc89eb949dcec0f94b4e3d247173417bda86d72e0bae1'
            or accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']):
        raise ValueError('Exact acceptedv39required')
    directory = STORE / 'reviews/20261031'
    stage = directory / 'q305-summary-restoration-v1'
    preflight = read_json(stage / 'preflight.json')
    bind_path = directory / 'q305-native-binding-v1.json'
    binding = read_json(bind_path)
    pid = preflight['paper_id']
    old = catalog.document(pid)
    candidate = read_json(stage / 'candidate.json')
    if (pid != 'P-D-2021-2100112-1b2d1f1c' or old['queue_position'] != 305
            or preflight['parent_dataset_id'] != catalog.identity
            or preflight['source_sha256'] != old['source_sha256']
            or preflight['parent_raw_pages_sha256'] != old['raw_pages_sha256']
            or preflight['characters'] != 3125 or preflight['logical_author_paragraphs'] != 9
            or preflight['original_ocr_lines'] != 50 or preflight['manually_source_transcribed_lines'] != [9, 28, 31]
            or preflight['literal_wrap_occurrences_repaired'] != 5
            or not preflight['complete_native_prose_equal_after_declared_ligature_expansion_and_wraps']
            or not preflight['source_lines_accounted_once'] or not preflight['later_actual_author_body_unchanged']
            or preflight['whole_paper_source_acceptance'] or preflight['ai_receipts_created']):
        raise ValueError('Exact source-read nine-paragraph preflight required')
    bound_stage = {str(stage / name): sha for name, sha in preflight['proof_sha256'].items()}
    bound_stage.update({str(stage / 'preflight.json'): file_hash(stage / 'preflight.json'),
        str(stage / 'candidate.json'): file_hash(stage / 'candidate.json'), str(bind_path): file_hash(bind_path),
        str(Path(__file__).with_name('stage_q305_summary_restoration_v1.py')): preflight['stager_sha256'],
        str(Path(__file__).with_name('bind_q305_native_metrics_v1.py')): binding['binder_sha256']})
    if any(file_hash(Path(p)) != sha for p, sha in bound_stage.items()):
        raise ValueError('Exact source stage changed')
    library = file_hash(RUNTIME / 'scripts/text_corpus.py')
    if (preflight['library_sha256'] != library or binding['library_sha256'] != library
            or binding['staged_preflight_sha256'] != file_hash(stage / 'preflight.json')
            or binding['all_target_native_pages_freshly_rematched'] != 24
            or binding['all_metric_payloads_unchanged'] != 435 or binding['other_metric_complete_files_unchanged'] != 434
            or not binding['portable_page_proof_replay_pass']
            or binding['source_page_review_implementation_sha256'] != file_hash(RUNTIME / 'scripts/source_ocr_page_reviews.py')):
        raise ValueError('Source/native replay binding changed')
    metrics = STORE / 'span-metrics-20261031-q305-v1'
    if file_hash(metrics / 'manifest.json') != binding['metrics_manifest_sha256']:
        raise ValueError('Freshly rematched native metrics changed')
    summary = (stage / 'summary-preview.md').read_text(encoding='utf-8').removesuffix('\n')
    rest = [b for b in all_author_blocks(old) if min(b['source_pages']) > 1]
    author = summary + '\n\n' + text_with_block_spans(rest)[0]
    if (len(summary) != 3125 or digest(summary.encode()) != preflight['text_sha256']
            or later(old) != later(candidate) or text_with_block_spans(all_author_blocks(candidate))[0] != author):
        raise ValueError('Complete Summaryor later author body differs')
    names = ('source_span_metrics.py', 'text_corpus.py', 'preview_span_origin_flow.py', 'source_text_repairs.py',
             'source_layout_reviews.py', 'source_absence_reviews.py', 'resegment_text_corpus.py', 'corpus_queries.py',
             'corpus_reader.py', 'source_paragraph_reviews.py', 'source_ocr_page_reviews.py', 'extract_text_span_metrics.py',
             'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')
    frozen = {name: file_hash(RUNTIME / 'scripts' / name) for name in names}
    parent_code = read_json(STORE / 'build-request-reflow-20261031-v39.json')['implementation_sha256']
    if any(frozen[name] != parent_code[name] for name in names):
        raise ValueError('Accepted runtime must remain unchanged')
    scope = read_json(parent / 'scope.json')
    additions = {'ocr_manifest_sha256': [stage / 'manifest.json'],
        'source_review_sha256': [stage / 'source-review.json'], 'layout_review_sha256': [stage / 'layout.json'],
        'text_repair_sha256': [stage / 'word-repairs.json']}
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    inputs = {field: [] for field in fields}
    for field in fields:
        for name, sha in scope.get(field, {}).items():
            if file_hash(Path(name)) != sha:
                raise ValueError('Accepted source evidence changed')
            inputs[field].append(Path(name))
        inputs[field].extend(additions.get(field, []))
        if len({str(p.resolve()) for p in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    if len(inputs['ocr_manifest_sha256']) != 56:
        raise ValueError('Preserve all55OCRinputs and add onlyq305')
    bindings = {field: {str(p.resolve()): file_hash(p) for p in paths} for field, paths in inputs.items()}
    expected_defects, expected_totals = Counter(accepted['defects']), dict(accepted['totals'])
    expected_defects.subtract(pending(old)); expected_defects.update(pending(candidate))
    expected_totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
    expected_totals['sections'] += len(candidate['sections']) - len(old['sections'])
    expected_totals['boundary_verified'] += 1
    expected_totals['source_lines'] += 50
    # Old native-template agreement is retained as original evidence, never as OCRacceptance.
    extra_ocr_review_pages = []
    ocr_papers = {read_json(path)['paper_id'] for path in inputs['ocr_manifest_sha256']} - {pid}
    for other in sorted(ocr_papers):
        previous_doc = catalog.document(other)
        for page in rows(parent / 'papers' / other / 'raw/pages.jsonl'):
            if ((page.get('ocr_status') == 'candidate' or page.get('ocr_evidence'))
                    and page.get('comparison', {}).get('status') == 'agreement'
                    and not any(d['code'] == 'cross_engine_review' and d.get('page') == page['page'] for d in previous_doc['defects'])):
                expected_defects['cross_engine_review'] += 1
                extra_ocr_review_pages.append({'paper_id': other, 'page': page['page']})
    expected_defects = {key: count for key, count in expected_defects.items() if count}
    previous = {family: {x['paper_id']: x for x in catalog.select(family)} for family in ('abstract', 'all_author_text')}
    if previous['abstract'][pid]['status'] != 'present-unverified':
        raise ValueError('Previously unverified split-paragraph Summaryrequired')
    native = base / 'native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native corpus changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'individual_source_stage_sha256': bound_stage, 'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_totals': expected_totals, 'expected_open_defects': expected_defects,
        'additional_stale_native_agreement_ocr_review_pages': extra_ocr_review_pages,
        'change': 'Q305individually source-read and native/OCRadjudicated Summaryin nine paragraphs,3125characters.Three source-read OCRpunctuation/spacing corrections and five exact wraps;all original native/OCRobjects preserved.Complete prose equals original native prose under declared ordinary presentation-ligature expansion and five checked wraps.The negative contagion finding is retained.All434other selections/statuses/raw and all later actual author body unchanged;runtime unchanged.',
        'source_boundary_reviews_added': 1, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    print({'expected_totals': expected_totals, 'additional_ocr_review_pages': extra_ocr_review_pages}, flush=True)
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
              inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (RUNTIME / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v40.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            before = previous[family][item['paper_id']]
            if item['paper_id'] != pid:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated source selection changed:' + item['paper_id'])
            elif built.text_and_spans(item)[0] != (summary if family == 'abstract' else author) or item['status'] != ('verified' if family == 'abstract' else before['status']):
                raise ValueError('Restored Summarytext/status differs')
    for other in catalog.by_id:
        old_doc, new_doc = catalog.document(other), built.document(other)
        if new_doc['raw_pages_sha256'] != (preflight['raw_pages_sha256'] if other == pid else old_doc['raw_pages_sha256']):
            raise ValueError('Unexpected raw source change')
        if other == pid and later(old_doc) != later(new_doc):
            raise ValueError('Later author body changed')
    result = validate(output, WORK, True)
    if (result['totals'] != expected_totals or result['defects'] != expected_defects
            or not result['structural_integrity_pass'] or result['source_completeness_accepted']):
        raise ValueError('Unexpected totals/flags/acceptance;preserve failed candidate')
    all_bindings = [bound_stage, *bindings.values(), {str(RUNTIME / 'scripts' / name): sha for name, sha in frozen.items()}]
    if any(file_hash(Path(path)) != sha for group in all_bindings for path, sha in group.items()):
        raise ValueError('Frozen source proofs/runtime changed')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
