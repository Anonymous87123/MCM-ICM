"""Snapshot explicit reading observations without inventing repairs or AI receipts."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
from text_corpus import file_hash, json_new, read_json


def checked_corrections(run, session, paths):
    corrections=[]
    for path in paths:
        value=read_json(path)
        number=value.get('receipt_sequence')
        if (value.get('schema')!='reading-observation-correction-v1' or type(number) is not int or number<0 or
                value.get('run_id')!=session['run_id'] or value.get('dataset_id')!=session['dataset_id'] or
                not value.get('correction') or not value.get('reviewer')):
            raise ValueError('Invalid observation correction identity')
        receipt_path=run/'receipts'/f'{number:06d}.json'
        batch_path=run/'batches'/f'{number:06d}.json'
        if file_hash(receipt_path)!=value.get('receipt_sha256') or file_hash(batch_path)!=value.get('batch_sha256'):
            raise ValueError('Observation correction no longer binds its immutable receipt/batch')
        receipt=read_json(receipt_path)
        if not any(o['paper_id']==value.get('paper_id') and any(i.get('code')==value.get('original_issue_code')
                for i in o.get('source_issues',[])) for o in receipt['observations']):
            raise ValueError('Correction does not identify an original issue')
        corrections.append({'path':str(path),'sha256':file_hash(path),'correction':value})
    return corrections


def snapshot(reader, root, run, output, corrections=()):
    if output.exists():
        raise ValueError('Create-only issue snapshot exists')
    # The run's original frozen reader validates its policy and receipt chain.
    # Do not import it into the mutable reader module namespace.
    result=subprocess.run([sys.executable,'-X','utf8',str(reader),'--corpus-root',str(root),
        'status','--run-dir',str(run)],capture_output=True,encoding='utf-8',errors='strict')
    if result.returncode:
        raise ValueError('Original reading-chain validation failed: '+result.stderr[:500])
    status=json.loads(result.stdout);session=read_json(run/'session.json');findings=[];bindings={}
    for number in range(status['batches_acknowledged']):
        path=run/'receipts'/f'{number:06d}.json';sha=file_hash(path);receipt=read_json(path)
        bindings[path.name]=sha
        for observation in receipt['observations']:
            for issue in observation.get('source_issues',[]):
                findings.append({'paper_id':observation['paper_id'],'receipt_sequence':number,
                    'receipt_sha256':sha,'source_issue':issue,
                    'observation':observation['observation']})
    if any(file_hash(run/'receipts'/name)!=sha for name,sha in bindings.items()):
        raise ValueError('Receipt changed during snapshot')
    amendments=checked_corrections(run,session,corrections)
    value={'schema':'reading-source-issue-snapshot-v1','dataset_id':status['dataset_id'],
        'run_id':status['run_id'],'session_sha256':file_hash(run/'session.json'),
        'frozen_reader':str(reader),'frozen_reader_sha256':file_hash(reader),
        'reading_status':status,'receipts':bindings,'explicit_issue_observations':len(findings),
        'papers_with_explicit_issue_observations':len({x['paper_id'] for x in findings}),
        'findings':findings,'observation_corrections':amendments,
        'correction_count':len(amendments),'raw_issue_count_is_uncorrected_history':True,
        'source_fidelity_approved':False,'ai_receipts_created':0,
        'meaning':'All explicit source_issues fields in acknowledged observations of this exact run. Other defects may appear only in narrative observations or await discovery. Original descriptions are not automatically cleared by later corpus generations; this is not a live unresolved-defect total.'}
    json_new(output,value);print({k:v for k,v in value.items() if k not in {'findings','receipts'}},flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reader',type=Path,required=True);p.add_argument('--corpus-root',type=Path,required=True)
    p.add_argument('--run-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--correction',type=Path,action='append',default=[])
    a=p.parse_args();snapshot(a.reader.resolve(),a.corpus_root.resolve(),a.run_dir.resolve(),a.output.resolve(),
                             [p.resolve() for p in a.correction])
