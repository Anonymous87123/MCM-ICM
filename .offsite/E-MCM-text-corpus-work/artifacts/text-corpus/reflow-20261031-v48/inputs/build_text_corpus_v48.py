"""Promote source-read q323-326 only; preserve all raw sources and unrelated selections."""
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
    return [(b['source_line_ids'], b['text'], b['kind'], b['issues'])
            for b in all_author_blocks(doc) if min(b['source_pages']) > 1]


def main():
    os.chdir(WORK)
    parent, output = STORE / 'reflow-20261031-v47', STORE / 'reflow-20261031-v48'
    request = STORE / 'build-request-reflow-20261031-v48.json'
    report = STORE / 'integrity-reflow-20261031-v48.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Preserve existing create-only build')
    if shutil.disk_usage(STORE).free < 30 * 1024**3:
        raise ValueError('Require30GiBfree;no cleanup authorized')
    catalog = Catalog(parent)
    accepted = read_json(STORE / 'integrity-reflow-20261031-v47.json')
    if (catalog.identity != 'cf78c18aae577ae8eaeb940c6c05270ae6fc19ee3f3a1c85e22b746270da7508'
            or accepted['dataset_id'] != catalog.identity or not accepted['structural_integrity_pass']):
        raise ValueError('Exact accepted v47 required')
    directory = STORE / 'reviews/20261031'
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    extra = {field: [] for field in fields}
    targets, frozen_stages = {}, {}
    totals, defects = dict(accepted['totals']), Counter(accepted['defects'])
    metrics = STORE / 'span-metrics-20261031-q315-v1'
    earlier = Catalog(STORE / 'reflow-20261031-v46')
    for queue, pid, pages, version, length, paragraphs, sha, stager_sha in [
        (323, 'P-D-2024-2429211-de10f571', 25, 1, 3067, 4,
         '583b2ecec320add4e0482e7762da81dc5dfd5d19c590f8a32a89574a2cfa4789',
         'c47b9d02709f646373f740a2904f8c5a1098253d0d041351a21573396a2637eb'),
        (324, 'P-D-2025-2504188-db12259e', 26, 1, 2772, 6,
         'aa6f4e6b4d8be6578d757d4039f771f151bc325a01ee47bbf1f516f3091e8134',
         '97f3178de9dc1b3d419ec6ceb152360f60a1d043df4ea5bf457147e2fbb6f15c'),
        (325, 'P-D-2025-2507692-249f88dd', 25, 2, 2836, 6,
         '2d6654539447c0db2238dd0bf184b8153c43492138072743a0ac2023ae2a1420',
         '2c9f6601b20bd4d2c86186d91133159829a12d25c8d1d0e66918ea4158ce363c'),
        (326, 'P-D-2025-2516219-17e4e820', 25, 1, 2763, 5,
         '65c10719c72e41c2a0b083d5a4c7feca1d41ca27d04454cf81e0dbe8eb88e3be',
         '0080a92c6ca2af991208d2bfe929b2586695ba0f38f7ce5c42ceb0ca2133c8ff')]:
        stage = directory / f'q{queue}-native-summary-v{version}'
        preflight_path = stage / 'preflight.json'
        p = read_json(preflight_path)
        old, candidate = catalog.document(pid), read_json(stage / 'candidate.json')
        if (p['paper_id'] != pid or old['queue_position'] != queue or old['page_count'] != pages
                or p['parent_dataset_id'] != earlier.identity
                or p['source_sha256'] != old['source_sha256']
                or p['raw_pages_sha256'] != old['raw_pages_sha256'] or not p['raw_pages_unchanged']
                or p['characters'] != length or p['logical_author_paragraphs'] != paragraphs
                or p['text_sha256'] != sha or p['stager_sha256'] != stager_sha
                or not p['source_lines_accounted_once'] or not p['later_actual_author_body_unchanged']
                or p['whole_paper_source_acceptance'] or p['ai_receipts_created'] or p['ocr_used']
                or p['native_metrics_manifest_sha256'] != file_hash(metrics / 'manifest.json')):
            raise ValueError('Exact frozen individual source-read stage required')
        preimage = earlier.document(pid)
        changed = {key for key in set(preimage) | set(old) if preimage.get(key) != old.get(key)}
        if (changed != {'scope_id'}
                or preimage['scope_id'] != '960bf99280f06de911967885d9f50c5cc9baabd4d23f31357e3e70aefc6ae8ad'
                or old['scope_id'] != '7ade617d1073c41ab21f31dfb14c5a5e41b2b23b8c42f4e74344f264adbf0d01'):
            raise ValueError('Frozen v46stage permits only exact v47scope identity change;all content/source fields identical')
        if queue == 323:
            if (not p['complete_native_prose_equal_after_declared_ligature_expansions']
                    or p['ligatures_expanded'] != 3 or p['independent_prose_lines_equal_in_order'] != 33):
                raise ValueError('Exact three source-read IJC ligature expansions required')
        elif not p['complete_native_prose_equal_after_declared_source_wraps']:
            raise ValueError('Complete source-read prose equality required')
        if queue in (324, 325) and p['margin_microtext_lines_preserved_as_furniture'] != 687:
            raise ValueError('All687page-local margin objects must be preserved')
        if (queue == 324 and p['independent_prose_lines_equal_in_order'] != 32
                or queue == 325 and (not p['independent_complete_prose_tokens_equal_in_order']
                    or p['independent_engine_exact_watermark_insert_groups'] != 15)
                or queue == 326 and (p['author_wraps_repaired'] != 11
                    or p['genuine_hyphen_line_spaces_closed'] != 1
                    or p['independent_prose_lines_equal_in_order_after_declared_comparison_spacing'] != 35)):
            raise ValueError('Exact independent comparison/source-wrap assertions required')
        stager = Path(__file__).with_name(f'stage_q{queue}_native_summary_v{version}.py')
        frozen_stages.update({str(stage / name): value for name, value in p['proof_sha256'].items()})
        frozen_stages.update({str(preflight_path): file_hash(preflight_path),
            str(stage / 'candidate.json'): file_hash(stage / 'candidate.json'), str(stager): stager_sha})
        summary = (stage / 'summary-preview.md').read_text(encoding='utf-8').removesuffix('\n')
        author = summary + '\n\n' + text_with_block_spans(
            [block for block in all_author_blocks(old) if min(block['source_pages']) > 1])[0]
        if (len(summary) != length or digest(summary.encode()) != sha or later(old) != later(candidate)
                or text_with_block_spans(all_author_blocks(candidate))[0] != author):
            raise ValueError('Complete restored selection or later author body differs')
        targets[pid] = {'abstract': summary, 'all_author_text': author}
        extra['source_review_sha256'].append(stage / 'source-review.json')
        extra['layout_review_sha256'].append(stage / 'layout.json')
        if queue in (323, 326):
            extra['text_repair_sha256'].append(stage / 'word-wrap-repairs.json')
        defects.subtract(pending(old))
        defects.update(pending(candidate))
        totals['blocks'] += len(candidate['blocks']) - len(old['blocks'])
        totals['sections'] += len(candidate['sections']) - len(old['sections'])
        totals['boundary_verified'] += 1
    if any(file_hash(Path(path)) != sha for path, sha in frozen_stages.items()):
        raise ValueError('Frozen individual source proof changed')
    defects = {key: value for key, value in defects.items() if value}
    scope, inputs = read_json(parent / 'scope.json'), {field: [] for field in fields}
    for field in fields:
        for path, sha in scope.get(field, {}).items():
            if file_hash(Path(path)) != sha:
                raise ValueError('Existing accepted evidence changed')
            inputs[field].append(Path(path))
        inputs[field].extend(extra[field])
        if len({str(path.resolve()) for path in inputs[field]}) != len(inputs[field]):
            raise ValueError('Duplicate source input')
    if len(inputs['ocr_manifest_sha256']) != 62:
        raise ValueError('All62existing OCR raw inputs must remain unchanged')
    names = ('source_span_metrics.py', 'text_corpus.py', 'preview_span_origin_flow.py', 'source_text_repairs.py',
        'source_layout_reviews.py', 'source_absence_reviews.py', 'resegment_text_corpus.py', 'corpus_queries.py',
        'corpus_reader.py', 'source_paragraph_reviews.py', 'source_ocr_page_reviews.py', 'extract_text_span_metrics.py',
        'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')
    frozen = {name: file_hash(RUNTIME / 'scripts' / name) for name in names}
    if frozen != read_json(STORE / 'build-request-reflow-20261031-v47.json')['implementation_sha256']:
        raise ValueError('Production runtime must remain unchanged')
    bindings = {field: {str(path.resolve()): file_hash(path) for path in paths} for field, paths in inputs.items()}
    previous = {family: {item['paper_id']: item for item in catalog.select(family)}
                for family in ('abstract', 'all_author_text')}
    if any(previous['abstract'][pid]['status'] != 'present-unverified' for pid in targets):
        raise ValueError('Exactly four previously unverified summaries required')
    native = WORK / 'artifacts/text-corpus/native-20261029-v1'
    if Catalog(native).identity != scope['parent_dataset_id']:
        raise ValueError('Original native corpus changed')
    json_new(request, {'previous_candidate_dataset_id': catalog.identity, 'native_dataset_id': Catalog(native).identity,
        'driver_sha256': file_hash(Path(__file__)), 'implementation_sha256': frozen, 'inputs': bindings,
        'individual_source_stage_sha256': frozen_stages, 'raw_pages_sha256_overrides': {},
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'expected_totals': totals, 'expected_open_defects': defects,
        'change': 'Only source-read q323-326 Summary layouts.q323three IJC ligature expansions;q324/325all687margin m objects separately preserved;q326eleven prose wraps and one genuine-hyphen space closure.Inline notation retained verbatim,no semantics or correctness recovery.All435raw/all431other selections/statuses/all later actual author body unchanged.Exact v46to47scope-only preimages proved.All15runtime unchanged.Failedq325v1preserved.',
        'source_boundary_reviews_added': 4, 'whole_paper_acceptances_added': 0, 'ai_reading_receipts_created': 0,
        'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'], inputs['text_repair_sha256'],
              inputs['absence_review_sha256'], inputs['layout_review_sha256'], metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (RUNTIME / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v48.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    for family in previous:
        for item in built.select(family):
            pid, before = item['paper_id'], previous[family][item['paper_id']]
            if pid not in targets:
                if item['text_sha256'] != before['text_sha256'] or item['status'] != before['status']:
                    raise ValueError('Unrelated431paper selection/status changed')
            elif (built.text_and_spans(item)[0] != targets[pid][family]
                    or item['status'] != ('verified' if family == 'abstract' else before['status'])):
                raise ValueError('Complete restored selection/status differs')
    for pid in catalog.by_id:
        old, new = catalog.document(pid), built.document(pid)
        if new['raw_pages_sha256'] != old['raw_pages_sha256']:
            raise ValueError('Unexpected raw source change')
        if pid in targets and later(old) != later(new):
            raise ValueError('Later author body changed')
    result = validate(output, WORK, True)
    if (result['totals'] != totals or result['defects'] != defects
            or not result['structural_integrity_pass'] or result['source_completeness_accepted']):
        raise ValueError('Unexpected counts/flags/acceptance;preserve failed candidate')
    for group in [frozen_stages, *bindings.values(),
                  {str(RUNTIME / 'scripts' / name): sha for name, sha in frozen.items()}]:
        if any(file_hash(Path(path)) != sha for path, sha in group.items()):
            raise ValueError('Frozen proof/runtime changed')
    json_new(report, result)
    print(result, flush=True)


if __name__ == '__main__':
    main()
