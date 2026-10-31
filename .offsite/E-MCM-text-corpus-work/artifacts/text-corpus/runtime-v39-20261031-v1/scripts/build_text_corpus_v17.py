"""Apply the checked q6/q12/q333 prose repairs in a new immutable corpus."""
import os
from pathlib import Path

from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash, json_new, read_json
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1]
    os.chdir(work)
    base=work/'artifacts/text-corpus'
    parent=base/'reflow-20261030-v16'
    output=base/'reflow-20261030-v17'
    request=base/'build-request-reflow-20261030-v17.json'
    report_path=base/'integrity-reflow-20261030-v17.json'
    if any(p.exists() for p in (output,request,report_path)):
        raise ValueError('Create-only build state exists; preserve and inspect it')
    audit_path=base/'span-origin-flow-full-20261030-v10.json'
    audit=read_json(audit_path)
    catalog=Catalog(parent)
    scope=read_json(parent/'scope.json')
    layout_paths=[base/'reviews/20261030'/name for name in
                  ('q333-opening-layout-v1.json','q012-summary-cover-layout-v1.json')]
    repair_paths=[base/'reviews/20261030'/name for name in
                  ('q006-determinate-word-repair-v1.json','q012-list-bullet-transcription-v1.json')]
    extra={str(p.resolve()):file_hash(p) for p in (*layout_paths,*repair_paths)}
    totals=audit['totals']
    if (audit['parent_dataset_id']!=catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256']!=extra or totals['papers']!=435 or totals['pages']!=11552 or
            totals['source_lines']!=954866 or totals['contents_pages_before']!=352 or totals['contents_pages_after']!=352):
        raise ValueError('Full source-line/review replay must pass for these exact four proofs')
    frozen={name:file_hash(work/'scripts'/name) for name in audit['implementation_sha256']}
    if frozen!=audit['implementation_sha256']:
        raise ValueError('Prospectively audited implementation changed')
    native=base/'native-20261029-v1'
    if Catalog(native).identity!=scope['parent_dataset_id']:
        raise ValueError('Original native input required; never reaugment OCR raw')
    fields=('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
            'absence_review_sha256','layout_review_sha256')
    inputs={field:[] for field in fields}
    for field in fields:
        for name,sha in scope[field].items():
            path=Path(name)
            if file_hash(path)!=sha:
                raise ValueError('Frozen input changed: '+name)
            inputs[field].append(path)
    inputs['layout_review_sha256']+=layout_paths
    inputs['text_repair_sha256']+=repair_paths
    if len(inputs['ocr_manifest_sha256'])!=53:
        raise ValueError('Unverified Unicode OCR must not be silently applied')
    bindings={field:{str(p.resolve()):file_hash(p) for p in paths} for field,paths in inputs.items()}
    metrics=base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':Catalog(native).identity,
        'previous_candidate_dataset_id':catalog.identity,'prospective_report_sha256':file_hash(audit_path),
        'driver_sha256':file_hash(Path(__file__)),'inputs':bindings,
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),
        'query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'change':'Source-checked q6 discretionary word join; q12 summary/cover and bullet repair; q333 opening lanes and 1.0/1.1/2.0 chapter boundaries.',
        'source_acceptances_added':0,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],metrics)
    print(index(output),flush=True)
    built=Catalog(output)
    selected={s['paper_id']:s for s in built.select('abstract')}
    for pid,characters in (('P-A-2012-15065-1cbc0cd9',2129),('P-E-2017-61502-f0a50d47',2073)):
        text,spans=built.text_and_spans(selected[pid])
        if len(text)!=characters or {p for s in spans for p in s['pages']}!={1}:
            raise ValueError('Checked abstract scope was not retained: '+pid)
    q6_text,_=built.text_and_spans(selected['P-A-2011-12149-cb2b7105'])
    if 'to determine the acceleration' not in q6_text or 'deter- mine' in q6_text:
        raise ValueError('Checked q6 word repair missing')
    result=validate(output,work,True)
    if result['defects'].get('contents_page_boundary_review',0)!=352:
        raise ValueError('Contents preservation changed; preserve candidate without promotion')
    for mapping in bindings.values():
        if any(file_hash(Path(p))!=sha for p,sha in mapping.items()):
            raise ValueError('Frozen input changed during build')
    if any(file_hash(work/'scripts'/name)!=sha for name,sha in frozen.items()):
        raise ValueError('Audited implementation changed during build')
    json_new(report_path,result)
    print({k:v for k,v in result.items() if k not in ('papers','defects')},flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Failed candidate retained without promotion')


if __name__=='__main__':
    main()
