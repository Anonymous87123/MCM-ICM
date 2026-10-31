"""Promote individually source-read q310/q311 summaries;preserve all other work."""
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
from text_corpus import digest, file_hash, json_new, read_json, text_with_block_spans, write_new
from validate_text_corpus import validate


def pending(document):
    return Counter(d['code'] for d in document['defects'] if d.get('status') != 'resolved')


def later(document):
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues']) for b in all_author_blocks(document)
            if min(b['source_pages']) > 1]


def main():
    os.chdir(WORK)
    parent, output = STORE / 'reflow-20261031-v42', STORE / 'reflow-20261031-v43'
    request = STORE / 'build-request-reflow-20261031-v43.json'
    report = STORE / 'integrity-reflow-20261031-v43.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Create-only build exists;preserve it')
    if shutil.disk_usage(STORE).free < 30 * 1024**3:
        raise ValueError('Require30GiBfree;no cleanup authorized')
    accepted = read_json(STORE / 'integrity-reflow-20261031-v42.json')
    catalog = Catalog(parent)
    if (catalog.identity != 'b7e6fbb054da44962fb664e4c4684ae4df8bf5da7c2356b9b7fe6dbf1cfc5a9e'
            or accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']):
        raise ValueError('Require exact acceptedv42')
    directory = STORE / 'reviews/20261031'
    targets, bound_stage, raw_overrides = {}, {}, {}
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    extra = {field: [] for field in fields}
    totals, defects = dict(accepted['totals']), Counter(accepted['defects'])
    final_binding = None
    for queue, pid, pages, length, paragraphs, lines, same, transcribed, wraps, expected_sha in [
        (310, 'P-D-2021-2121604-9d9314bb', 22, 2880, 9, 50, 47, [16,18,27], 5,
         '6739c5312b8261e569be37e98256668d86b4b2cd995f4cd84d8943bc4b29bdc7'),
        (311, 'P-D-2021-2124497-1be43b7c', 24, 2662, 5, 41, 41, [], 2,
         '2df057ac146f166b9f402c9a840be16b97a17189322e288d49a2acfca64a4a68')]:
        stage = directory / f'q{queue}-summary-restoration-v1'
        preflight_path = stage / 'preflight.json'
        binding_path = directory / f'q{queue}-native-binding-v1.json'
        preflight, binding = read_json(preflight_path), read_json(binding_path)
        old = catalog.document(pid)
        equality_key = ('complete_native_prose_equal_after_declared_ligature_expansion_and_wraps' if queue == 310
                        else 'complete_native_prose_equal_after_declared_ligature_expansion_glyph_recovery_and_wraps')
        if (preflight['paper_id'] != pid or old['queue_position'] != queue or old['page_count'] != pages
                or preflight['parent_dataset_id'] != catalog.identity
                or preflight['source_sha256'] != old['source_sha256']
                or preflight['parent_raw_pages_sha256'] != old['raw_pages_sha256']
                or preflight['characters'] != length or preflight['logical_author_paragraphs'] != paragraphs
                or preflight['original_ocr_lines'] != lines or preflight['unchanged_ocr_line_objects'] != same
                or preflight['manually_source_transcribed_lines'] != transcribed
                or preflight['literal_wrap_occurrences_repaired'] != wraps
                or preflight['author_wraps_repaired'] != wraps or preflight['separate_keyword_wraps_repaired']
                or not preflight[equality_key] or not preflight['source_lines_accounted_once']
                or not preflight['later_actual_author_body_unchanged'] or preflight['whole_paper_source_acceptance']
                or preflight['ai_receipts_created'] or preflight['selected_source_status'] != 'verified in prospective stage only'
                or preflight['text_sha256'] != expected_sha):
            raise ValueError('Exact individually source-read stage required')
        if queue == 311 and (preflight['non_author_ocr_indices'] != [17]
                or preflight['native_glyph_recovery'] != {'퐺': 'G', '푉': 'V', '퐸': 'E', '푝': 'p', '휎': 'σ'}
                or preflight['native_glyph_adjacent_spaces_recovered'] != ['σ is', 'σ values']):
            raise ValueError('Exact source-read glyph recovery and watermark ownership required')
        stager = Path(__file__).with_name(f'stage_q{queue}_summary_restoration_v1.py')
        binder = Path(__file__).with_name(f'bind_q{queue}_native_metrics_v1.py')
        bound_stage.update({str(stage / name): sha for name, sha in preflight['proof_sha256'].items()})
        bound_stage.update({str(preflight_path): file_hash(preflight_path), str(binding_path): file_hash(binding_path),
                            str(stage / 'candidate.json'): file_hash(stage / 'candidate.json'),
                            str(stager): preflight['stager_sha256'], str(binder): binding['binder_sha256']})
        if (preflight['library_sha256'] != file_hash(RUNTIME / 'scripts/text_corpus.py')
                or binding['paper_id'] != pid or binding['parent_dataset_id'] != catalog.identity
                or binding['library_sha256'] != preflight['library_sha256']
                or binding['staged_preflight_sha256'] != file_hash(preflight_path)
                or binding['all_target_native_pages_freshly_rematched'] != pages
                or binding['all_metric_payloads_unchanged'] != 435
                or binding['other_metric_complete_files_unchanged'] != 434
                or binding['proof_sha256'] != preflight['proof_sha256']
                or not binding['portable_page_proof_replay_pass']
                or binding['source_page_review_implementation_sha256'] != file_hash(RUNTIME / 'scripts/source_ocr_page_reviews.py')):
            raise ValueError('Native/OCR proof replay binding differs')
        candidate = read_json(stage / 'candidate.json')
        summary = (stage / 'summary-preview.md').read_text(encoding='utf-8').removesuffix('\n')
        author = summary + '\n\n' + text_with_block_spans([b for b in all_author_blocks(old) if min(b['source_pages']) > 1])[0]
        if (len(summary) != length or digest(summary.encode()) != expected_sha or later(old) != later(candidate)
                or text_with_block_spans(all_author_blocks(candidate))[0] != author):
            raise ValueError('Complete source selection or later actual author body changed')
        targets[pid] = {'abstract': summary, 'all_author_text': author}
        raw_overrides[pid] = preflight['raw_pages_sha256']
        for field, name in [('ocr_manifest_sha256', 'manifest.json'), ('source_review_sha256', 'source-review.json'),
                            ('layout_review_sha256', 'layout.json'), ('text_repair_sha256', 'word-repairs.json')]:
            extra[field].append(stage / name)
        defects.subtract(pending(old)); defects.update(pending(candidate))
        totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
        totals['sections'] += len(candidate['sections']) - len(old['sections'])
        totals['boundary_verified'] += 1
        totals['source_lines'] += lines
        final_binding = binding
    if any(file_hash(Path(path)) != sha for path, sha in bound_stage.items()):
        raise ValueError('Frozen individual source proof changed')
    defects = {code: count for code, count in defects.items() if count}
    scope, inputs = read_json(parent / 'scope.json'), {field: [] for field in fields}
    for field in fields:
        for path, sha in scope.get(field, {}).items():
            if file_hash(Path(path)) != sha:
                raise ValueError('Accepted evidence changed')
            inputs[field].append(Path(path))
        inputs[field].extend(extra[field])
        if len({str(p.resolve()) for p in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    metrics = STORE / 'span-metrics-20261031-q311-v1'
    if len(inputs['ocr_manifest_sha256']) != 60 or file_hash(metrics / 'manifest.json') != final_binding['metrics_manifest_sha256']:
        raise ValueError('Preserve58OCRinputs,add onlyq310/q311;require fresh native bindings')
    names = ('source_span_metrics.py', 'text_corpus.py', 'preview_span_origin_flow.py', 'source_text_repairs.py',
             'source_layout_reviews.py', 'source_absence_reviews.py', 'resegment_text_corpus.py', 'corpus_queries.py',
             'corpus_reader.py', 'source_paragraph_reviews.py', 'source_ocr_page_reviews.py', 'extract_text_span_metrics.py',
             'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')
    frozen = {name: file_hash(RUNTIME / 'scripts' / name) for name in names}
    parent_code = read_json(STORE / 'build-request-reflow-20261031-v42.json')['implementation_sha256']
    if any(frozen[name] != parent_code[name] for name in names):
        raise ValueError('Accepted runtime must remain unchanged')
    bindings = {field: {str(p.resolve()): file_hash(p) for p in paths} for field, paths in inputs.items()}
    previous = {family: {x['paper_id']: x for x in catalog.select(family)} for family in ('abstract', 'all_author_text')}
    if any(previous['abstract'][pid]['status'] != 'present-unverified' for pid in targets):
        raise ValueError('Two previously unverified summaries required')
    native = WORK / 'artifacts/text-corpus/native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native corpus changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'individual_source_stage_sha256': bound_stage, 'raw_pages_sha256_overrides': raw_overrides,
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_totals': totals, 'expected_open_defects': defects,
        'change': 'Individually source-read q310nine-paragraph/q311five-paragraph complete Summary restorations.Two native source-adjudicated OCR pages;all native evidence and original OCR retained.q310two apostrophes/one word space and five author wraps;q311original41OCRline objects unchanged,one watermark classified separately,two author wraps,printed inline glyph recovery only.Full keywords/form/title/promotion separate.All433other selections/statuses/raw and later actual author body unchanged.Runtime unchanged.',
        'source_boundary_reviews_added': 2, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
              inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (RUNTIME / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v43.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            pid, before = item['paper_id'], previous[family][item['paper_id']]
            if pid not in targets:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated source selection changed')
            elif built.text_and_spans(item)[0] != targets[pid][family] or item['status'] != ('verified' if family == 'abstract' else before['status']):
                raise ValueError('Complete restored source selection/status differs')
    for pid in catalog.by_id:
        old, new = catalog.document(pid), built.document(pid)
        if new['raw_pages_sha256'] != raw_overrides.get(pid, old['raw_pages_sha256']):
            raise ValueError('Raw evidence changed')
        if pid in targets and later(old) != later(new):
            raise ValueError('Later actual author body changed')
    result = validate(output, WORK, True)
    if (result['totals'] != totals or result['defects'] != defects or not result['structural_integrity_pass']
            or result['source_completeness_accepted']):
        raise ValueError('Unexpected global counts/defects/acceptance;preserve failed candidate')
    groups = [bound_stage, *bindings.values(), {str(RUNTIME / 'scripts' / name): sha for name, sha in frozen.items()}]
    if any(file_hash(Path(path)) != sha for group in groups for path, sha in group.items()):
        raise ValueError('Frozen source proofs/core changed')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
