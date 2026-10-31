"""Promote individually inspected q55/q58 summary paragraphs without rewriting old data."""
import os
from pathlib import Path

from corpus_reader import Catalog
from corpus_queries import selected_blocks
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash,json_new,read_json,write_new
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1];os.chdir(work);base=work/'artifacts/text-corpus'
    parent=base/'reflow-20261031-v22';output=base/'reflow-20261031-v23'
    request=base/'build-request-reflow-20261031-v23.json';report=base/'integrity-reflow-20261031-v23.json'
    if any(p.exists() for p in (output,request,report)):
        raise ValueError('Create-only build state exists; preserve it')
    accepted=read_json(base/'integrity-reflow-20261031-v22.json')
    audit_path=base/'span-origin-flow-full-20261031-v16.json';audit=read_json(audit_path)
    catalog=Catalog(parent);scope=read_json(parent/'scope.json');directory=base/'reviews/20261031'
    layouts=[directory/f'q{n:03d}-summary-layout-v1.json' for n in (55,58)]
    repairs=[directory/f'q{n:03d}-summary-word-repairs-v1.json' for n in (55,58)]
    exact={str(p.resolve()):file_hash(p) for p in (*layouts,*repairs)};totals=audit['totals']
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id']!=catalog.identity or
            audit['parent_dataset_id']!=catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256']!=exact or
            (totals['papers'],totals['pages'],totals['source_lines'])!=(435,11552,954866) or
            totals['contents_pages_before']!=352 or totals['contents_pages_after']!=352):
        raise ValueError('Exact full prospective replay required')
    frozen={name:file_hash(work/'scripts'/name) for name in audit['implementation_sha256']}
    if frozen!=audit['implementation_sha256']:
        raise ValueError('Audited implementation changed')
    frozen.update({name:file_hash(work/'scripts'/name) for name in
        ('index_text_corpus.py','validate_text_corpus.py','verify_reader_transport.py')})
    fields=('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
        'absence_review_sha256','layout_review_sha256','paragraph_join_review_sha256')
    inputs={field:[] for field in fields}
    for field in fields:
        for name,sha in scope.get(field,{}).items():
            path=Path(name)
            if file_hash(path)!=sha:
                raise ValueError('Source proof changed: '+name)
            inputs[field].append(path)
    inputs['layout_review_sha256']+=layouts;inputs['text_repair_sha256']+=repairs
    if len(inputs['ocr_manifest_sha256'])!=53:
        raise ValueError('Unverified Unicode OCR must stay unapplied')
    native=base/'native-20261029-v1';native_id=Catalog(native).identity
    if native_id!=scope['parent_dataset_id']:
        raise ValueError('Original native generation required')
    bindings={field:{str(p.resolve()):file_hash(p) for p in paths} for field,paths in inputs.items()}
    old_abstract={s['paper_id']:s for s in catalog.select('abstract')}
    metrics=base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':native_id,'previous_candidate_dataset_id':catalog.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'implementation_sha256':frozen,'inputs':bindings,
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),
        'query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'change':'Individual physical pages1/2 checked for q55 and q58; restore seven/six summary paragraphs, inline model lead-ins, fifteen exact word-wrap/accent edits, separately preserve labels/title/form/keywords/watermark/QR.',
        'remaining_limit':'Later source bodies, other text defects and whole-paper acceptance remain pending.',
        'source_acceptances_added':0,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],
        metrics,inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py','index_text_corpus.py','validate_text_corpus.py','verify_reader_transport.py'):
        write_new(output/'inputs'/name,(work/'scripts'/name).read_bytes())
    write_new(output/'inputs/build_text_corpus_v23.py',Path(__file__).read_bytes())
    write_new(output/'inputs/build-request.json',request.read_bytes())
    print(index(output),flush=True);built=Catalog(output)
    expected={'P-A-2021-2100454-dc37ed6a':(3075,7),'P-A-2021-2110178-2aed1e20':(3005,6)}
    for item in built.select('abstract'):
        pid=item['paper_id']
        if pid not in expected:
            if item['text_sha256']!=old_abstract[pid]['text_sha256']:
                raise ValueError('Unrelated abstract changed: '+pid)
            continue
        text,spans=built.text_and_spans(item);blocks=selected_blocks(built.document(pid),item)
        chars,count=expected[pid]
        if (len(text)!=chars or {p for s in spans for p in s['pages']}!={1} or
                sum(b['kind']!='heading' for b in blocks)!=count or 'MCM/ICM' in text or 'Keywords:' in text):
            raise ValueError('Checked individual summary contract changed')
    result=validate(output,work,True)
    if result['defects'].get('contents_page_boundary_review',0)!=352:
        raise ValueError('Contents preservation changed; retain candidate')
    if any(file_hash(Path(p))!=sha for mapping in bindings.values() for p,sha in mapping.items()):
        raise ValueError('Source proof changed during build')
    if any(file_hash(work/'scripts'/name)!=sha for name,sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report,result);print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Failed candidate retained without acceptance')


if __name__=='__main__':
    main()
