"""Finish validation of the indexed v17 left by an interrupted build; no rebuild."""
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import file_hash, json_new, read_json
from validate_text_corpus import validate


def main():
    work=Path(__file__).resolve().parents[1]
    base=work/'artifacts/text-corpus'
    root=base/'reflow-20261030-v17'
    output=base/'integrity-reflow-20261030-v17.json'
    recovery=base/'finalization-recovery-v17-20261031-v1.json'
    if output.exists() or recovery.exists():
        raise ValueError('Create-only finalization report exists; inspect it, never overwrite')
    request_path=base/'build-request-reflow-20261030-v17.json'
    request=read_json(request_path)
    audit_path=base/'span-origin-flow-full-20261030-v10.json'
    audit=read_json(audit_path)
    if (file_hash(audit_path)!=request['prospective_report_sha256'] or
            file_hash(work/'scripts/build_text_corpus_v17.py')!=request['driver_sha256'] or
            audit['errors'] or audit['review_replay_conflicts']):
        raise ValueError('Frozen build driver/preflight no longer binds')
    for name,sha in audit['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:
            raise ValueError('Frozen implementation changed: '+name)
    scope=read_json(root/'scope.json')
    for field,mapping in request['inputs'].items():
        if scope.get(field)!=mapping:
            raise ValueError('Indexed generation input set differs: '+field)
        if any(file_hash(Path(p))!=sha for p,sha in mapping.items()):
            raise ValueError('Frozen build input changed: '+field)
    native=Catalog(base/'native-20261029-v1')
    if native.identity!=request['native_dataset_id'] or native.identity!=scope['parent_dataset_id']:
        raise ValueError('Original native generation binding differs')
    catalog=Catalog(root)
    if len(catalog.papers)!=435 or sum(p['page_count'] for p in catalog.papers)!=11552:
        raise ValueError('Complete indexed scope missing')
    selected={s['paper_id']:s for s in catalog.select('abstract')}
    corrected=[]
    for pid,characters in (('P-A-2012-15065-1cbc0cd9',2129),('P-E-2017-61502-f0a50d47',2073)):
        text,spans=catalog.text_and_spans(selected[pid])
        if len(text)!=characters or {p for s in spans for p in s['pages']}!={1}:
            raise ValueError('Checked abstract scope was not retained: '+pid)
        corrected.append({'paper_id':pid,'abstract_characters':len(text),'abstract_pages':[1]})
    text,_=catalog.text_and_spans(selected['P-A-2011-12149-cb2b7105'])
    if 'to determine the acceleration' not in text or 'deter- mine' in text:
        raise ValueError('Checked q6 word repair missing')
    result=validate(root,work,True)
    if not result['structural_integrity_pass'] or result['defects'].get('contents_page_boundary_review',0)!=352:
        raise ValueError('Existing indexed generation failed full validation; preserve without promotion')
    for mapping in request['inputs'].values():
        if any(file_hash(Path(p))!=sha for p,sha in mapping.items()):
            raise ValueError('Frozen input changed during finalization')
    for name,sha in audit['implementation_sha256'].items():
        if file_hash(work/'scripts'/name)!=sha:
            raise ValueError('Frozen implementation changed during finalization')
    json_new(output,result)
    json_new(recovery,{'dataset_id':catalog.identity,'reason':'Original build stopped after its complete index was printed and before the integrity report was saved; validate existing bytes without rebuilding or reapplying OCR.',
        'build_request_sha256':file_hash(request_path),'original_driver_sha256':request['driver_sha256'],
        'finalizer_sha256':file_hash(Path(__file__)),'integrity_report_sha256':file_hash(output),
        'corrected_abstract_scopes':corrected,'q6_checked_word_retained':True,
        'all_frozen_inputs_unchanged':True,'structural_integrity_pass':True,
        'source_completeness_accepted':False,'ai_reading_receipts_created':0,
        'formula_verification':'paused','figure_distillation':'paused'})
    print({k:v for k,v in result.items() if k not in ('papers','defects')},flush=True)


if __name__=='__main__':
    main()
