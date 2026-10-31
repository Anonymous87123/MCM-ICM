"""Apply individually inspected q47–q50 summary repairs, create-only."""
import os
from pathlib import Path

from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash,json_new,read_json,write_new
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1];os.chdir(work)
    base=work/'artifacts/text-corpus';parent=base/'reflow-20261031-v20'
    output=base/'reflow-20261031-v21'
    request=base/'build-request-reflow-20261031-v21.json'
    report=base/'integrity-reflow-20261031-v21.json'
    if any(p.exists() for p in (output,request,report)):
        raise ValueError('Create-only build state exists; inspect without restarting')
    audit_path=base/'span-origin-flow-full-20261031-v14.json';audit=read_json(audit_path)
    catalog=Catalog(parent);scope=read_json(parent/'scope.json');directory=base/'reviews/20261031'
    layouts=[directory/'q049-summary-layout-v1.json']
    repairs=[directory/name for name in ('q047-summary-repair-v2.json','q048-summary-repair-v2.json',
                                       'q050-summary-banner-repair-v2.json')]
    exact={str(p.resolve()):file_hash(p) for p in (*layouts,*repairs)};totals=audit['totals']
    accepted=read_json(base/'integrity-reflow-20261031-v20.json')
    if (not accepted['structural_integrity_pass'] or accepted['dataset_id']!=catalog.identity or
            audit['parent_dataset_id']!=catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256']!=exact or
            (totals['papers'],totals['pages'],totals['source_lines'])!=(435,11552,954866) or
            totals['contents_pages_before']!=352 or totals['contents_pages_after']!=352):
        raise ValueError('Accepted parent and full exact source replay required')
    frozen={name:file_hash(work/'scripts'/name) for name in audit['implementation_sha256']}
    if frozen!=audit['implementation_sha256']:
        raise ValueError('Audited implementation changed')
    frozen.update({name:file_hash(work/'scripts'/name) for name in
                   ('index_text_corpus.py','validate_text_corpus.py','verify_reader_transport.py')})
    native=base/'native-20261029-v1';native_id=Catalog(native).identity
    if native_id!=scope['parent_dataset_id']:
        raise ValueError('Original native input required, never already augmented OCR')
    fields=('ocr_manifest_sha256','source_review_sha256','text_repair_sha256',
            'absence_review_sha256','layout_review_sha256','paragraph_join_review_sha256')
    inputs={field:[] for field in fields}
    for field in fields:
        for name,sha in scope.get(field,{}).items():
            path=Path(name)
            if file_hash(path)!=sha:
                raise ValueError('Frozen source proof changed: '+name)
            inputs[field].append(path)
    inputs['layout_review_sha256']+=layouts;inputs['text_repair_sha256']+=repairs
    if len(inputs['ocr_manifest_sha256'])!=53:
        raise ValueError('Unverified Unicode OCR must stay unapplied')
    bindings={field:{str(p.resolve()):file_hash(p) for p in paths} for field,paths in inputs.items()}
    metrics=base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':native_id,'previous_candidate_dataset_id':catalog.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'implementation_sha256':frozen,'inputs':bindings,
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),
        'query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'change':'Individual q47/q48/q50 banner and QR ownership; q47 source word wrap; q49 six source paragraphs with separate title/form/keywords/promotion. Prior q32/q46 joins retained.',
        'remaining_limit':'Checked page1 repairs only; later source prose and whole-paper acceptance remain unreviewed.',
        'source_acceptances_added':0,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],
        metrics,inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py','index_text_corpus.py','validate_text_corpus.py','verify_reader_transport.py'):
        write_new(output/'inputs'/name,(work/'scripts'/name).read_bytes())
    write_new(output/'inputs/build_text_corpus_v21.py',Path(__file__).read_bytes())
    write_new(output/'inputs/build-request.json',request.read_bytes())
    print(index(output),flush=True);built=Catalog(output)
    abstract={s['paper_id']:s for s in built.select('abstract')}
    for pid,chars,paragraphs in (
            ('P-A-2020-2001334-a7774d36',3868,6),('P-A-2020-2002354-f00d018f',3097,8),
            ('P-A-2020-2003298-d28634b8',3510,6),('P-A-2020-2003485-fe70a967',3793,5)):
        item=abstract[pid];text,spans=built.text_and_spans(item)
        from corpus_queries import selected_blocks
        blocks=selected_blocks(built.document(pid),item)
        if (len(text)!=chars or {p for s in spans for p in s['pages']}!={1} or
                sum(b['kind']!='heading' for b in blocks)!=paragraphs or
                'MCM/ICM' in text or '关注数学模型' in text):
            raise ValueError('Individual summary source restoration changed: '+pid)
    for pid,chars in (('P-A-2016-54164-57a2b533',7515),('P-A-2019-1926690-fc36d223',2311)):
        if abstract[pid]['characters']!=chars:
            raise ValueError('Prior source repair regressed')
    result=validate(output,work,True)
    if result['defects'].get('contents_page_boundary_review',0)!=352:
        raise ValueError('Contents preservation changed; retain candidate')
    for mapping in bindings.values():
        if any(file_hash(Path(p))!=sha for p,sha in mapping.items()):
            raise ValueError('Source proof changed during build')
    if any(file_hash(work/'scripts'/name)!=sha for name,sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report,result);print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Failed candidate retained without source acceptance')


if __name__=='__main__':
    main()
