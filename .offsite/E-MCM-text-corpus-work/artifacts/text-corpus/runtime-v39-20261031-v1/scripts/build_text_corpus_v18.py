"""Create-only chapter-view release, with the checked q14 handout boundary."""
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
    base = work/'artifacts/text-corpus'
    parent = base/'reflow-20261030-v17'
    output = base/'reflow-20261031-v18'
    request = base/'build-request-reflow-20261031-v18.json'
    report_path = base/'integrity-reflow-20261031-v18.json'
    if any(p.exists() for p in (output, request, report_path)):
        raise ValueError('Create-only build state exists; inspect without restarting')
    audit_path = base/'span-origin-flow-full-20261031-v11.json'
    audit = read_json(audit_path)
    catalog = Catalog(parent)
    scope = read_json(parent/'scope.json')
    extra = [base/'reviews/20261030/q014-summary-handout-layout-v1.json']
    totals = audit['totals']
    if (audit['parent_dataset_id'] != catalog.identity or audit['errors'] or
            audit['review_replay_conflicts'] or audit['review_input_sha256'] !=
            {str(p.resolve()):file_hash(p) for p in extra} or
            (totals['papers'], totals['pages'], totals['source_lines']) != (435,11552,954866) or
            totals['contents_pages_before'] != 352 or totals['contents_pages_after'] != 352):
        raise ValueError('Exact full source-line/review replay has not passed')
    frozen = {name:file_hash(work/'scripts'/name) for name in audit['implementation_sha256']}
    if frozen != audit['implementation_sha256']:
        raise ValueError('Audited implementation changed')
    frozen.update({name:file_hash(work/'scripts'/name) for name in
                   ('index_text_corpus.py','validate_text_corpus.py')})
    native = base/'native-20261029-v1'
    native_id = Catalog(native).identity
    if native_id != scope['parent_dataset_id']:
        raise ValueError('Use original native input, never already augmented OCR raw')
    fields = ('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
              'absence_review_sha256','layout_review_sha256')
    inputs = {field:[] for field in fields}
    for field in fields:
        for name, sha in scope[field].items():
            path = Path(name)
            if file_hash(path) != sha:
                raise ValueError('Frozen input changed: '+name)
            inputs[field].append(path)
    inputs['layout_review_sha256'] += extra
    if len(inputs['ocr_manifest_sha256']) != 53:
        raise ValueError('Unverified Unicode OCR must remain unapplied')
    bindings = {field:{str(p.resolve()):file_hash(p) for p in paths} for field,paths in inputs.items()}
    metrics = base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':native_id,'previous_candidate_dataset_id':catalog.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'implementation_sha256':frozen,'inputs':bindings,
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),
        'query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'change':'Align chapter Markdown/SQLite with reader selection; preserve explicit typed non-author bodies separately; source-checked q14 Summary/handout boundary.',
        'source_acceptances_added':0,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],metrics)
    for name in ('corpus_reader.py','index_text_corpus.py','validate_text_corpus.py'):
        write_new(output/'inputs'/name,(work/'scripts'/name).read_bytes())
    write_new(output/'inputs/build_text_corpus_v18.py',Path(__file__).read_bytes())
    write_new(output/'inputs/build-request.json',request.read_bytes())
    print(index(output),flush=True)
    built = Catalog(output)
    selected = {s['paper_id']:s for s in built.select('abstract')}
    for pid, chars in (('P-A-2012-15065-1cbc0cd9',2129),('P-E-2017-61502-f0a50d47',2073),
                       ('P-A-2013-20559-c8c96095',2677)):
        text, spans = built.text_and_spans(selected[pid])
        if len(text) != chars or {p for s in spans for p in s['pages']} != {1}:
            raise ValueError('Checked Summary boundary changed: '+pid)
    q6,_ = built.text_and_spans(selected['P-A-2011-12149-cb2b7105'])
    if 'to determine the acceleration' not in q6 or 'deter- mine' in q6:
        raise ValueError('Previously checked q6 prose join lost')
    result = validate(output,work,True)
    if result['defects'].get('contents_page_boundary_review',0) != 352:
        raise ValueError('Contents candidate preservation changed')
    for mapping in bindings.values():
        if any(file_hash(Path(p)) != sha for p,sha in mapping.items()):
            raise ValueError('Frozen source proof changed during build')
    if any(file_hash(work/'scripts'/name) != sha for name,sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report_path,result)
    print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Failed candidate preserved without acceptance')


if __name__ == '__main__':
    main()
