"""Freeze combined-task retrieval and individually restored q53 prose, create-only."""
import os
from pathlib import Path

from corpus_reader import Catalog
from corpus_queries import selected_blocks,select_sections,task_numbers
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash,json_new,read_json,write_new
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1];os.chdir(work)
    base=work/'artifacts/text-corpus';parent=base/'reflow-20261031-v21'
    output=base/'reflow-20261031-v22';request=base/'build-request-reflow-20261031-v22.json'
    report=base/'integrity-reflow-20261031-v22.json'
    if any(p.exists() for p in (output,request,report)):
        raise ValueError('Create-only build state exists; inspect without restarting')
    audit_path=base/'span-origin-flow-full-20261031-v15.json';audit=read_json(audit_path)
    catalog=Catalog(parent);scope=read_json(parent/'scope.json');directory=base/'reviews/20261031'
    layouts=[directory/'q053-opening-layout-v1.json'];repairs=[directory/'q053-opening-word-repairs-v1.json']
    exact={str(p.resolve()):file_hash(p) for p in (*layouts,*repairs)};totals=audit['totals']
    accepted=read_json(base/'integrity-reflow-20261031-v21.json')
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
    query_evidence=directory/'combined-task-query-defect-v1.json'
    labels=read_json(query_evidence)['matches']
    # Reproduce all11 real failures against the actual parent headings.
    for item in labels:
        paper=next(p for p in catalog.papers if p['queue_position']==item['queue'])
        doc=catalog.document(paper['paper_id'])
        section=next(s for s in doc['sections'] if s['section_id']==item['section_id'])
        if section['title']!=item['title'] or task_numbers(section['title'])!=set(item['explicit_tasks']):
            raise ValueError('Exact combined-task title binding differs')
    json_new(request,{'native_dataset_id':native_id,'previous_candidate_dataset_id':catalog.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'implementation_sha256':frozen,'inputs':bindings,
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),
        'query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'combined_task_defect_evidence_sha256':file_hash(query_evidence),
        'change':'Shared explicit task lists/ranges expose the complete shared chapter to each task; source-checked q53 seven-paragraph summary and separate complete newspaper handout, four strategies, cross-column prose, caption/price isolation and nine literal text repairs.',
        'remaining_limit':'Source completeness false; newspaper category other pending; later q53 body and all-paper prose frontier remain unreviewed.',
        'source_acceptances_added':0,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],
        metrics,inputs['paragraph_join_review_sha256'])
    for name in ('corpus_reader.py','index_text_corpus.py','validate_text_corpus.py','verify_reader_transport.py'):
        write_new(output/'inputs'/name,(work/'scripts'/name).read_bytes())
    write_new(output/'inputs/build_text_corpus_v22.py',Path(__file__).read_bytes())
    write_new(output/'inputs/build-request.json',request.read_bytes())
    write_new(output/'inputs/combined-task-query-defect-v1.json',query_evidence.read_bytes())
    print(index(output),flush=True);built=Catalog(output)
    abstract={s['paper_id']:s for s in built.select('abstract')}
    pid='P-A-2020-2017785-c87378f9';doc=built.document(pid)
    for query,chars,count in [('abstract',4036,7),('A Fishy Situation',2821,9)]:
        ids,excluded=select_sections(doc,query,exact_title=query!='abstract')
        from text_corpus import text_with_block_spans
        blocks=selected_blocks(doc,{'section_ids':ids,'excluded_roles':sorted(excluded)})
        text,spans=text_with_block_spans(blocks)
        if (len(text)!=chars or sum(b['kind']!='heading' for b in blocks)!=count or
                '$1.00' in text or 'Projected herring distribution' in text):
            raise ValueError('Q53 checked source restoration differs')
    for pid,chars in (('P-A-2016-54164-57a2b533',7515),('P-A-2019-1926690-fc36d223',2311),
                      ('P-A-2020-2001334-a7774d36',3868),('P-A-2020-2002354-f00d018f',3097),
                      ('P-A-2020-2003298-d28634b8',3510),('P-A-2020-2003485-fe70a967',3793)):
        if abstract[pid]['characters']!=chars:
            raise ValueError('Prior source repair regressed')
    replay=[]
    for item in labels:
        paper=next(p for p in built.papers if p['queue_position']==item['queue'])
        doc=built.document(paper['paper_id'])
        for number in item['explicit_tasks']:
            ids,excluded=select_sections(doc,f'task_{number}')
            blocks=selected_blocks(doc,{'section_ids':ids,'excluded_roles':sorted(excluded)})
            bids=[b['block_id'] for b in blocks]
            if item['section_id'] not in ids or len(set(bids))!=len(bids):
                raise ValueError('Shared task chapter missing or blocks duplicated')
            replay.append({'paper_id':paper['paper_id'],'section_id':item['section_id'],
                           'task':number,'selected_blocks':len(blocks)})
    json_new(base/'combined-task-query-replay-20261031-v1.json',{
        'dataset_id':built.identity,'policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'real_shared_titles':len(labels),'checks':replay,'ai_receipts_created':0,
        'source_fidelity_approved':False})
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
