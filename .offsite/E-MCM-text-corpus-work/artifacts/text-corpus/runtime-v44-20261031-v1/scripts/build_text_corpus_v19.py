"""Apply the individually source-checked q29–q32 prose repairs, create-only."""
import os
from pathlib import Path

from corpus_reader import Catalog
from index_text_corpus import index
from resegment_text_corpus import resegment
from text_corpus import file_hash, json_new, read_json, write_new
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1];os.chdir(work)
    base=work/'artifacts/text-corpus';parent=base/'reflow-20261031-v18'
    output=base/'reflow-20261031-v19'
    request=base/'build-request-reflow-20261031-v19.json'
    report_path=base/'integrity-reflow-20261031-v19.json'
    if any(p.exists() for p in (output,request,report_path)):
        raise ValueError('Create-only build state exists; inspect without restarting')
    audit_path=base/'span-origin-flow-full-20261031-v12.json';audit=read_json(audit_path)
    catalog=Catalog(parent);scope=read_json(parent/'scope.json')
    directory=base/'reviews/20261031'
    layouts=[directory/name for name in ('q030-summary-prose-layout-v1.json',
        'q031-summary-abstract-layout-v1.json','q032-opening-mixed-contents-layout-v1.json')]
    repairs=[directory/name for name in ('q029-summary-word-repair-v1.json','q032-temperature-word-repair-v1.json')]
    extra={str(p.resolve()):file_hash(p) for p in (*layouts,*repairs)};totals=audit['totals']
    if (audit['parent_dataset_id']!=catalog.identity or audit['errors'] or audit['review_replay_conflicts'] or
            audit['review_input_sha256']!=extra or
            (totals['papers'],totals['pages'],totals['source_lines'])!=(435,11552,954866) or
            totals['contents_pages_before']!=352 or totals['contents_pages_after']!=352):
        raise ValueError('Full exact source-line/review replay required for these five proofs')
    frozen={name:file_hash(work/'scripts'/name) for name in audit['implementation_sha256']}
    if frozen!=audit['implementation_sha256']:
        raise ValueError('Audited implementation changed')
    frozen.update({name:file_hash(work/'scripts'/name) for name in ('index_text_corpus.py','validate_text_corpus.py')})
    native=base/'native-20261029-v1';native_id=Catalog(native).identity
    if native_id!=scope['parent_dataset_id']:
        raise ValueError('Original native input required, never already augmented OCR raw')
    fields=('ocr_manifest_sha256','source_review_sha256','text_repair_sha256','absence_review_sha256','layout_review_sha256')
    inputs={field:[] for field in fields}
    for field in fields:
        for name,sha in scope[field].items():
            path=Path(name)
            if file_hash(path)!=sha:
                raise ValueError('Frozen source proof changed: '+name)
            inputs[field].append(path)
    inputs['layout_review_sha256']+=layouts;inputs['text_repair_sha256']+=repairs
    if len(inputs['ocr_manifest_sha256'])!=53:
        raise ValueError('Unverified Unicode OCR remains unapplied')
    bindings={field:{str(p.resolve()):file_hash(p) for p in paths} for field,paths in inputs.items()}
    metrics=base/'span-metrics-20261030-v1'
    json_new(request,{'native_dataset_id':native_id,'previous_candidate_dataset_id':catalog.identity,
        'prospective_report_sha256':file_hash(audit_path),'driver_sha256':file_hash(Path(__file__)),
        'implementation_sha256':frozen,'inputs':bindings,
        'span_metrics_manifest_sha256':file_hash(metrics/'manifest.json'),
        'query_policy_sha256':file_hash(work/'scripts/corpus_queries.py'),
        'change':'Individual q29 discretionary word joins; q30 inline prose/paragraph lanes; q31 two abstracts with form/date separated; q32 real abstract-child continuation above midpage Contents and word join. Contents-page flag retained.',
        'remaining_limit':'Source-checked cross-page paragraph still stored as adjacent fragments; logical join pending. No whole-section/paper acceptance.',
        'source_acceptances_added':0,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    resegment(native,output,inputs['ocr_manifest_sha256'],inputs['source_review_sha256'],
        inputs['text_repair_sha256'],inputs['absence_review_sha256'],inputs['layout_review_sha256'],metrics)
    for name in ('corpus_reader.py','index_text_corpus.py','validate_text_corpus.py'):
        write_new(output/'inputs'/name,(work/'scripts'/name).read_bytes())
    write_new(output/'inputs/build_text_corpus_v19.py',Path(__file__).read_bytes())
    write_new(output/'inputs/build-request.json',request.read_bytes())
    print(index(output),flush=True)
    built=Catalog(output);selected={s['paper_id']:s for s in built.select('abstract')}
    checks=(('P-A-2016-44845-998bce33',1978,{1}),('P-A-2016-46830-92f43919',2490,{1}),
            ('P-A-2016-48649-e4d30266',2925,{1,2}),('P-A-2016-54164-57a2b533',7516,{1,3,4}),
            ('P-A-2013-20559-c8c96095',2677,{1}),('P-E-2017-61502-f0a50d47',2073,{1}))
    for pid,chars,pages in checks:
        text,spans=built.text_and_spans(selected[pid])
        if len(text)!=chars or {p for s in spans for p in s['pages']}!=pages:
            raise ValueError('Checked source scope changed: '+pid)
    result=validate(output,work,True)
    if result['defects'].get('contents_page_boundary_review',0)!=352:
        raise ValueError('Contents preservation changed; retain failed candidate')
    for mapping in bindings.values():
        if any(file_hash(Path(p))!=sha for p,sha in mapping.items()):
            raise ValueError('Frozen proof changed during build')
    if any(file_hash(work/'scripts'/name)!=sha for name,sha in frozen.items()):
        raise ValueError('Frozen implementation changed during build')
    json_new(report_path,result);print(result,flush=True)
    if not result['structural_integrity_pass']:
        raise ValueError('Failed candidate retained without source acceptance')


if __name__=='__main__':
    main()
