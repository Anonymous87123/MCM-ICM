"""Freeze individual q114/q116 summary restorations in a new corpus generation."""
import os
from pathlib import Path

from corpus_queries import selected_blocks
from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash, json_new, read_json, write_new
from validate_text_corpus import validate


def main():
    work = Path(__file__).resolve().parents[1]
    os.chdir(work)
    base = work / 'artifacts/text-corpus'
    parent = base / 'reflow-20261031-v25'
    output = base / 'reflow-20261031-v26'
    request = base / 'build-request-reflow-20261031-v26.json'
    report = base / 'integrity-reflow-20261031-v26.json'
    if any(p.exists() for p in (output, request, report)):
        raise ValueError('Create-only build state exists; preserve it')
    accepted = read_json(base / 'integrity-reflow-20261031-v25.json')
    audit_path = base / 'span-origin-flow-full-20261031-v20.json'
    audit = read_json(audit_path)
    catalog = Catalog(parent)
    scope = read_json(parent / 'scope.json')
    directory = base / 'reviews/20261031'
    layouts = [directory / f'q{n:03d}-summary-layout-v1.json' for n in (114, 116)]
    repairs = [directory / f'q{n:03d}-summary-word-repairs-v1.json' for n in (114, 116)]
    paragraphs = [directory / 'q114-summary-paragraph-v1.json']
    reviews = [directory / f'q{n:03d}-summary-{kind}-source-review-v1.json'
               for n, kind in ((114, 'opening'), (114, 'executive'), (116, 'opening'))]
    exact = {str(p.resolve()): file_hash(p) for p in (*layouts, *repairs, *paragraphs, *reviews)}
    totals = audit['totals']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id'] != catalog.identity or
            audit['parent_dataset_id'] != catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256'] != exact or
            (totals['papers'], totals['pages'], totals['source_lines']) != (435, 11552, 954866) or
            totals['contents_pages_before'] != 352 or totals['contents_pages_after'] != 352):
        raise ValueError('Exact frozen full prospective replay required')
    preflights = [read_json(directory / f'q{n:03d}-summary-preflight-v1.json') for n in (114, 116)]
    if any(p['parent_dataset_id'] != catalog.identity or not p['source_lines_accounted_once'] or
           p['logical_author_paragraphs'] != 10 for p in preflights):
        raise ValueError('Individual source preflight differs')
    if [p['characters'] for p in preflights] != [4148, 2971]:
        raise ValueError('Checked summary lengths differ')
    frozen = {name: file_hash(work / 'scripts' / name) for name in audit['implementation_sha256']}
    if frozen != audit['implementation_sha256']:
        raise ValueError('Audited implementation changed')
    frozen.update({name: file_hash(work / 'scripts' / name) for name in
                   ('index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py')})
    fields = ('ocr_manifest_sha256', 'source_review_sha256', 'text_repair_sha256',
              'absence_review_sha256', 'layout_review_sha256', 'paragraph_join_review_sha256')
    inputs = {field: [] for field in fields}
    for field in fields:
        for name, sha in scope.get(field, {}).items():
            path = Path(name)
            if file_hash(path) != sha:
                raise ValueError('Source proof changed: ' + name)
            inputs[field].append(path)
    inputs['layout_review_sha256'] += layouts
    inputs['text_repair_sha256'] += repairs
    inputs['paragraph_join_review_sha256'] += paragraphs
    inputs['source_review_sha256'] += reviews
    if len(inputs['ocr_manifest_sha256']) != 53:
        raise ValueError('Unverified Unicode OCR must stay unapplied')
    native = base / 'native-20261029-v1'
    native_id = Catalog(native).identity
    if native_id != scope['parent_dataset_id']:
        raise ValueError('Original native generation required')
    bindings = {field: {str(p.resolve()): file_hash(p) for p in paths} for field, paths in inputs.items()}
    old_abstract = {s['paper_id']: s for s in catalog.select('abstract')}
    metrics = base / 'span-metrics-20261030-v1'
    json_new(request, {'native_dataset_id': native_id, 'previous_candidate_dataset_id': catalog.identity,
        'prospective_report_sha256': file_hash(audit_path), 'driver_sha256': file_hash(Path(__file__)),
        'implementation_sha256': frozen, 'inputs': bindings,
        'span_metrics_manifest_sha256': file_hash(metrics / 'manifest.json'),
        'query_policy_sha256': file_hash(work / 'scripts/corpus_queries.py'),
        'change': 'Individual q114 opening/late Executive Summary restoration, Contents exclusion and source-checked recommend cross-page join; q116 full six-contribution Summary, including previously omitted contribution2 opening. Preserve all435 continuous author views and unresolved flags.',
        'remaining_limit': 'Machine review flags, other source defects, later bodies and actual all-chapter reading remain pending.',
        'source_boundary_reviews_added': 3, 'whole_paper_acceptances_added': 0,
        'ai_reading_receipts_created': 0, 'formula_verification': 'paused', 'figure_distillation': 'paused'})
    resegment(native, output, inputs['ocr_manifest_sha256'], inputs['source_review_sha256'],
              inputs['text_repair_sha256'], inputs['absence_review_sha256'], inputs['layout_review_sha256'],
              metrics, inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py', 'index_text_corpus.py', 'validate_text_corpus.py', 'verify_reader_transport.py'):
        write_new(output / 'inputs' / name, (work / 'scripts' / name).read_bytes())
    write_new(output / 'inputs/build_text_corpus_v26.py', Path(__file__).read_bytes())
    write_new(output / 'inputs/build-request.json', request.read_bytes())
    print(index(output), flush=True)
    built = Catalog(output)
    expected = {p['paper_id']: p for p in preflights}
    for item in built.select('abstract'):
        pid = item['paper_id']
        if pid not in expected:
            if item['text_sha256'] != old_abstract[pid]['text_sha256']:
                raise ValueError('Unrelated abstract changed: ' + pid)
            continue
        contract = expected[pid]
        text, spans = built.text_and_spans(item)
        blocks = selected_blocks(built.document(pid), item)
        logical = sum(b['kind'] in {'prose', 'list', 'mixed', 'author_callout'} for b in blocks) - sum(
            bool(b.get('paragraph_continues_from')) for b in blocks)
        if (len(text) != contract['characters'] or item['text_sha256'] != contract['sha256'] or
                sorted({p for s in spans for p in s['pages']}) != contract['physical_pages'] or logical != 10):
            raise ValueError('Checked individual summary contract changed')
    result = validate(output, work, True)
    if (result['defects'].get('contents_page_boundary_review', 0) != 352 or
            result['totals'].get('continuous_author_views_checked') != 435 or
            result['totals'].get('boundary_verified') != 9):
        raise ValueError('Contents preservation, author views or exact boundary reviews differ; retain candidate')
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
