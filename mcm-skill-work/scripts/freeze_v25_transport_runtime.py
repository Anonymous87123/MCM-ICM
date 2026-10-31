"""Freeze accepted v25 reader code, preserving all earlier runtimes."""
from pathlib import Path
from text_corpus import file_hash, json_new, read_json, write_new


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    target=base/'transport-runtime-v25-20261031-v1'
    if target.exists():
        raise ValueError('Create-only runtime exists; preserve it')
    request=read_json(base/'build-request-reflow-20261031-v25.json')
    accepted=read_json(base/'integrity-reflow-20261031-v25.json')
    if not accepted['structural_integrity_pass'] or accepted['totals'].get('continuous_author_views_checked')!=435:
        raise ValueError('Accepted immutable v25 with all435continuous views required')
    names=('text_corpus.py','corpus_queries.py','corpus_reader.py','verify_reader_transport.py')
    hashes={name:file_hash(work/'scripts'/name) for name in names}
    if any(sha!=request['implementation_sha256'][name] for name,sha in hashes.items()):
        raise ValueError('Reader implementation differs from accepted build')
    for name in names:
        write_new(target/'scripts'/name,(work/'scripts'/name).read_bytes())
    json_new(target/'manifest.json',{'corpus_root':str(base/'reflow-20261031-v25'),
        'dataset_id':accepted['dataset_id'],'files':hashes,
        'purpose':'Exact transport reproduction; no AI receipts or source acceptance from simulation.'})
    print({'runtime':str(target),'files':hashes},flush=True)


if __name__=='__main__':
    main()
