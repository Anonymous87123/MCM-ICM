"""Freeze corrected author-query exclusion in a separate immutable generation."""
import os
from pathlib import Path

from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash, json_new, read_json
from validate_text_corpus import validate


def main():
    work = Path(__file__).resolve().parents[1]
    os.chdir(work)
    base = work/'artifacts/text-corpus'
    parent = base/'reflow-20261030-v15'
    output = base/'reflow-20261030-v16'
    request = base/'build-request-reflow-20261030-v16.json'
    report_path = base/'integrity-reflow-20261030-v16.json'
    if any(p.exists() for p in (output,request,report_path)):
        raise ValueError('Create-only build state exists; preserve and inspect, never restart')
    audit_path = base/'span-origin-flow-full-20261030-v8.json'
    audit = read_json(audit_path)
    catalog = Catalog(parent)
    scope = read_json(parent/'scope.json')
    totals = audit['totals']
    if (audit['parent_dataset_id']!=catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256'] or totals['papers']!=435 or totals['pages']!=11552 or
            totals['source_lines']!=954866 or totals['contents_pages_before']!=352 or totals['contents_pages_after']!=352):
        raise ValueError('The full frozen-policy source/review preview must pass')
    for name,sha in audit['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:
            raise ValueError('Audited implementation changed: '+name)
    native = base/'native-20261029-v1'
    if Catalog(native).identity!=scope['parent_dataset_id']:
        raise ValueError('Original native generation required; never reaugment OCR raw')
    fields = ('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
              'absence_review_sha256','layout_review_sha256')
    inputs = {field:[] for field in fields}
    for field in fields:
        for name,sha in scope[field].items():
            path = Path(name)
            if file_hash(path)!=sha:
                raise ValueError('Frozen source proof/OCR input changed: '+name)
            inputs[field].append(path)
    if len(inputs['ocr_manifest_sha256'])!=53:
        raise ValueError('New Unicode OCR must remain unverified and unapplied')
    bindings = {field:{str(p.resolve()):file_hash(p) for p in paths} for field,paths in inputs.items()}
    metrics = base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':Catalog(native).identity,'previous_candidate_dataset_id':catalog.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),'inputs':bindings,
        'query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'change':'Exclude explicitly non-author descendant subtrees from default author-section queries; keep them separately addressable. New runs bind policy hashes and reject incompatible resume.',
        'source_acceptances_added':0,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],metrics)
    print(index(output),flush=True)
    result = validate(output,work,True)
    if result['defects'].get('contents_page_boundary_review',0)!=352:
        raise ValueError('Contents preservation changed; no promotion')
    for mapping in bindings.values():
        if any(file_hash(Path(p))!=sha for p,sha in mapping.items()):
            raise ValueError('Source proof/OCR bytes changed during build')
    for name,sha in audit['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:
            raise ValueError('Audited implementation changed during build')
    json_new(report_path,result)
    print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Preserve failed candidate; no promotion')


if __name__ == '__main__':
    main()
