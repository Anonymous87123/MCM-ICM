"""Combine individually checked q313-315; preserve every unrelated selection."""
from collections import Counter
import os
from pathlib import Path
import shutil
import sys

WORK = Path(r'F:\MCM\mcm-skill-work')
STORE = Path(r'E:\MCM-text-corpus-work\artifacts\text-corpus')
RUNTIME = STORE / 'runtime-v44-20261031-v1'
sys.path.insert(0, str(RUNTIME / 'scripts'))
from corpus_queries import all_author_blocks
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import digest, file_hash, json_new, read_json, text_with_block_spans, write_new
from validate_text_corpus import validate


def pending(doc):
    return Counter(d['code'] for d in doc['defects'] if d.get('status') != 'resolved')


def later(doc):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(doc) if min(b['source_pages']) > 1]


def main():
    os.chdir(WORK)
    parent, output = STORE / 'reflow-20261031-v44', STORE / 'reflow-20261031-v45'
    request, report = STORE / 'build-request-reflow-20261031-v45.json', STORE / 'integrity-reflow-20261031-v45.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Preserve existing create-only build')
    if shutil.disk_usage(STORE).free < 30 * 1024**3:
        raise ValueError('Require30GiBfree;no cleanup authorized')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v44.json')
    if (catalog.identity != 'c4b0662c32223c0eb8875492772c5ab0e80340ae29c0011616fc9c7e972a2d95'
            or accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']):
        raise ValueError('Exact accepted v44 required')
    directory = STORE / 'reviews/20261031'
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    extra = {f: [] for f in fields}
    targets, frozen_stages, raw_overrides = {}, {}, {}
    totals, defects = dict(accepted['totals']), Counter(accepted['defects'])
    for queue, pid, pages, length, paragraphs, stage_name, repair_name, equality, sha in [
        (313, 'P-D-2022-2208928-f4cfe761', 22, 2642, 4, 'q313-native-summary-v1', 'alphabetic-ligature-repairs.json',
         'complete_native_prose_equal_after_declared_ligature_expansion', 'e7c0eece52f1e8fde90f69771ca53edee316fb76aa78019cffad94c7bc66182c'),
        (314, 'P-D-2022-2215444-cd948920', 22, 3059, 5, 'q314-native-summary-v1', 'word-wrap-repairs.json',
         'complete_native_prose_equal_after_declared_source_wraps', '871440a847666473032cc5f2413bfa3030827a844f23b5be14ace3b115d5d178'),
        (315, 'P-D-2022-2218897-ba395a78', 23, 2984, 6, 'q315-summary-restoration-v2', 'word-wrap-repairs.json',
         'complete_native_prose_equal_after_declared_ligatures_space_and_wraps', 'b76772cb813aa946b80479aa86b2b79e11b2ace50c408b5f53f28e1cfcf31258')]:
        stage = directory / stage_name
        preflight_path = stage / 'preflight.json'
        p = read_json(preflight_path)
        old, candidate = catalog.document(pid), read_json(stage / 'candidate.json')
        if (p['paper_id'] != pid or old['queue_position'] != queue or old['page_count'] != pages
                or p['parent_dataset_id'] != catalog.identity or p['source_sha256'] != old['source_sha256']
                or p['characters'] != length or p['logical_author_paragraphs'] != paragraphs or p['text_sha256'] != sha
                or not p[equality] or not p['source_lines_accounted_once'] or not p['later_actual_author_body_unchanged']
                or p['whole_paper_source_acceptance'] or p['ai_receipts_created']):
            raise ValueError('Exact individual source-read stage required')
        stager = Path(__file__).with_name(f'stage_q{queue}_native_summary_v1.py' if queue != 315 else 'stage_q315_summary_restoration_v2.py')
        frozen_stages.update({str(stage / name): value for name, value in p['proof_sha256'].items()})
        frozen_stages.update({str(preflight_path): file_hash(preflight_path), str(stage / 'candidate.json'): file_hash(stage / 'candidate.json'),
                              str(stager): p['stager_sha256']})
        if queue != 315:
            if (not p['raw_pages_unchanged'] or p['ocr_used'] or p['raw_pages_sha256'] != old['raw_pages_sha256']
                    or p['native_metrics_manifest_sha256'] != file_hash(STORE / 'span-metrics-20261031-q312-v1/manifest.json')):
                raise ValueError('Native stages must preserve raw and existing metric binding')
        else:
            binding_path = directory / 'q315-native-binding-v1.json'
            b = read_json(binding_path)
            binder = Path(__file__).with_name('bind_q315_native_metrics_v1.py')
            if (p['parent_raw_pages_sha256'] != old['raw_pages_sha256'] or p['original_ocr_lines'] != 49
                    or p['unchanged_ocr_line_objects'] != 45 or p['original_boxes_and_scores_unchanged'] != 49
                    or p['manually_source_transcribed_lines'] != [15, 19, 27, 42] or p['author_wraps_repaired'] != 5
                    or b['paper_id'] != pid or b['parent_dataset_id'] != catalog.identity
                    or b['staged_preflight_sha256'] != file_hash(preflight_path)
                    or b['all_target_native_pages_freshly_rematched'] != 23 or b['all_metric_payloads_unchanged'] != 435
                    or b['other_metric_complete_files_unchanged'] != 434 or b['proof_sha256'] != p['proof_sha256']
                    or not b['portable_page_proof_replay_pass']
                    or b['library_sha256'] != file_hash(RUNTIME / 'scripts/text_corpus.py')
                    or b['source_page_review_implementation_sha256'] != file_hash(RUNTIME / 'scripts/source_ocr_page_reviews.py')
                    or b['metrics_manifest_sha256'] != file_hash(STORE / 'span-metrics-20261031-q315-v1/manifest.json')):
                raise ValueError('Fresh23-page OCR/native proof binding required')
            frozen_stages.update({str(binding_path): file_hash(binding_path), str(binder): b['binder_sha256']})
            raw_overrides[pid] = p['raw_pages_sha256']
            extra['ocr_manifest_sha256'].append(stage / 'manifest.json')
            totals['source_lines'] += 49
        summary = (stage / 'summary-preview.md').read_text(encoding='utf-8').removesuffix('\n')
        author = summary + '\n\n' + text_with_block_spans([x for x in all_author_blocks(old) if min(x['source_pages']) > 1])[0]
        if (len(summary) != length or digest(summary.encode()) != sha or later(old) != later(candidate)
                or text_with_block_spans(all_author_blocks(candidate))[0] != author):
            raise ValueError('Complete restored prose or later actual body differs')
        targets[pid] = {'abstract': summary, 'all_author_text': author}
        for field, name in [('source_review_sha256', 'source-review.json'), ('layout_review_sha256', 'layout.json'),
                            ('text_repair_sha256', repair_name)]:
            extra[field].append(stage / name)
        defects.subtract(pending(old)); defects.update(pending(candidate))
        totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
        totals['sections'] += len(candidate['sections']) - len(old['sections'])
        totals['boundary_verified'] += 1
    if any(file_hash(Path(p)) != sha for p, sha in frozen_stages.items()):
        raise ValueError('Frozen individual proof changed')
    defects = {k: v for k, v in defects.items() if v}
    scope, inputs = read_json(parent / 'scope.json'), {f: [] for f in fields}
    for field in fields:
        for path, sha in scope.get(field, {}).items():
            if file_hash(Path(path)) != sha:
                raise ValueError('Existing accepted evidence changed')
            inputs[field].append(Path(path))
        inputs[field].extend(extra[field])
        if len({str(p.resolve()) for p in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    if len(inputs['ocr_manifest_sha256']) != 62:
        raise ValueError('Preserve61OCRinputs,add only q315')
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    names = ('source_span_metrics.py', 'text_corpus.py', 'preview_span_origin_flow.py', 'source_text_repairs.py',
             'source_layout_reviews.py', 'source_absence_reviews.py', 'resegment_text_corpus.py', 'corpus_queries.py',
             'corpus_reader.py', 'source_paragraph_reviews.py', 'source_ocr_page_reviews.py', 'extract_text_span_metrics.py',
             'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')
    frozen = {name: file_hash(RUNTIME / 'scripts' / name) for name in names}
    if frozen != read_json(STORE / 'build-request-reflow-20261031-v44.json')['implementation_sha256']:
        raise ValueError('All production runtime implementations must stay unchanged')
    bindings = {f: {str(p.resolve()): file_hash(p) for p in paths} for f, paths in inputs.items()}
    previous = {family: {x['paper_id']: x for x in catalog.select(family)} for family in ('abstract', 'all_author_text')}
    if any(previous['abstract'][pid]['status'] != 'present-unverified' for pid in targets):
        raise ValueError('Exactly three previously unverified summaries required')
    native = WORK / 'artifacts/text-corpus/native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native corpus changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'individual_source_stage_sha256': frozen_stages, 'raw_pages_sha256_overrides': raw_overrides,
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_totals': totals, 'expected_open_defects': defects,
        'change': 'Only individually source-read q313/314 native paragraphs and q315 OCR-adjudicated six paragraphs. Preserve original wording,all native/original OCR evidence,all432 other selections/statuses/raw and all later actual author body. q315 physical page count23;original printed body count22 is not the physical count. No production runtime change.',
        'source_boundary_reviews_added': 3, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
              inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (RUNTIME / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v45.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            pid, before = item['paper_id'], previous[family][item['paper_id']]
            if pid not in targets:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated432 paper selection/status changed')
            elif built.text_and_spans(item)[0] != targets[pid][family] or item['status'] != ('verified' if family == 'abstract' else before['status']):
                raise ValueError('Complete restored selection/status differs')
    for pid in catalog.by_id:
        old, new = catalog.document(pid), built.document(pid)
        if new['raw_pages_sha256'] != raw_overrides.get(pid, old['raw_pages_sha256']):
            raise ValueError('Unexpected raw evidence change')
        if pid in targets and later(old) != later(new):
            raise ValueError('Later actual author body changed')
    result = validate(output, WORK, True)
    if (result['totals'] != totals or result['defects'] != defects or not result['structural_integrity_pass']
            or result['source_completeness_accepted']):
        raise ValueError('Unexpected counts/flags/acceptance;preserve failed candidate')
    for group in [frozen_stages, *bindings.values(), {str(RUNTIME / 'scripts' / name): sha for name, sha in frozen.items()}]:
        if any(file_hash(Path(path)) != sha for path, sha in group.items()):
            raise ValueError('Frozen proof/runtime changed')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
