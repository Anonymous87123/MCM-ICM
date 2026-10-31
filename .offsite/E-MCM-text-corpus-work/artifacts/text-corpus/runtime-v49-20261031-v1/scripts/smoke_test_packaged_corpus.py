"""Check a separate skill attachment from an unrelated cwd; no AI ack or install."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

from text_corpus import file_hash, json_new, read_json


def smoke(package, run_dir, cwd, report):
    if run_dir.exists() or report.exists():
        raise ValueError('Create-only smoke artifacts exist; preserve them')
    script=package/'scripts/corpus_reader.py'
    manifest=read_json(package/'package-manifest.json')
    def call(arguments, expected=0):
        r=subprocess.run([sys.executable,str(script),*map(str,arguments)],cwd=cwd,
                         capture_output=True,encoding='utf-8',errors='strict')
        if r.returncode!=expected:
            raise ValueError('Packaged command failed: '+r.stderr[:600])
        return json.loads(r.stdout) if expected==0 else r.stderr.strip()
    sections=call(['sections'])
    if sections['expected_papers']!=435 or sections['dataset_id']!=manifest['dataset_id']:
        raise ValueError('Default relative attachment lookup lost corpus scope')
    missing=run_dir.parent/(run_dir.name+'-missing-database')
    if missing.exists():
        raise ValueError('Missing-database fixture path already exists')
    error=call(['--corpus-root',missing,'sections'],expected=1)
    if 'No fallback' not in error or missing.exists():
        raise ValueError('Missing attachment did not fail closed')
    started=call(['start','--section','abstract','--scope','all','--mode','exhaustive',
                  '--allow-unverified','--run-dir',run_dir])
    delivered=call(['next','--run-dir',run_dir])
    resumed=call(['resume','--run-dir',run_dir])
    status=call(['status','--run-dir',run_dir])
    if (delivered!=resumed or status['batches_acknowledged']!=0 or
            status['fully_processed_present']!=0 or status['full_read_acceptance'] or
            status['target_papers']!=435 or status['query_policy_status']!='frozen-policy'):
        raise ValueError('Packaged resume/processing separation changed')
    # No acknowledgement: this is machine transport, not a new actual reading.
    bindings=manifest['payload_sha256']
    for name in ('corpus_reader.py','corpus_queries.py','text_corpus.py'):
        expected=bindings.get('scripts/'+name,bindings.get('scripts\\'+name))
        if file_hash(package/'scripts'/name)!=expected:
            raise ValueError('Packaged implementation bytes changed')
    result={'dataset_id':manifest['dataset_id'],'package':str(package),'unrelated_cwd':str(cwd),
        'default_relative_attachment_pass':True,'missing_database_error':error,
        'target_papers':status['target_papers'],'query_policy_status':status['query_policy_status'],
        'pending_batch_replay_identical':True,'initial_completion_marker':delivered['completion_marker'],
        'initial_delivered_papers':[c['paper_id'] for c in delivered['chunks']],
        'ai_reading_receipts_created':0,'full_read_acceptance':False,
        'installed_skill_modified':False,'preview':manifest['preview']}
    json_new(report,result)
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package',type=Path,required=True)
    p.add_argument('--run-dir',type=Path,required=True)
    p.add_argument('--cwd',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True)
    a=p.parse_args()
    smoke(a.package.resolve(),a.run_dir.resolve(),a.cwd.resolve(),a.report.resolve())
