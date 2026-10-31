"""Read-only regression replay of saved deliveries, never new AI processing."""
import argparse
from pathlib import Path

from corpus_reader import Catalog, build_batch, state, wire
from text_corpus import file_hash, json_new, read_json


def verify(root,run):
    before = {p.relative_to(run).as_posix():file_hash(p) for p in run.rglob('*') if p.is_file()}
    catalog = Catalog(root)
    session,cursor,receipts,_ = state(catalog,run)
    paths = sorted((run/'batches').glob('*.json'))
    differences = []
    for number,path in enumerate(paths):
        batch = read_json(path)
        candidate = build_batch(catalog,session,batch['from_cursor'],number)
        if wire(candidate)!=wire(batch):
            differences.append(path.name)
    after = {p.relative_to(run).as_posix():file_hash(p) for p in run.rglob('*') if p.is_file()}
    if before!=after:
        raise ValueError('Existing immutable reading-run files changed')
    if differences:
        raise ValueError('Existing deliveries no longer reconstruct: '+str(differences))
    return {'dataset_id':catalog.identity,'run_id':session['run_id'],
        'saved_batches_reconstructed':len(paths),'saved_processing_receipts':len(receipts),'cursor':cursor,
        'wire_differences':differences,'existing_run_files_unchanged':True,
        'run_preimages':before,'verifier_sha256':file_hash(Path(__file__)),
        'reader_sha256':file_hash(Path(__file__).with_name('corpus_reader.py')),
        'query_policy_sha256':file_hash(Path(__file__).with_name('corpus_queries.py')),
        'ai_reading_receipts_created':0,'new_reading_acceptance':False,
        'meaning':'Compatibility replay of already saved deliveries only; no new reading, source review, cursor advancement or acknowledgement.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus-root',type=Path,required=True)
    parser.add_argument('--run-dir',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise ValueError('Create-only compatibility report exists; preserve it')
    result = verify(args.corpus_root.resolve(),args.run_dir.resolve())
    json_new(args.report,result)
    print({k:v for k,v in result.items() if k!='run_preimages'},flush=True)
