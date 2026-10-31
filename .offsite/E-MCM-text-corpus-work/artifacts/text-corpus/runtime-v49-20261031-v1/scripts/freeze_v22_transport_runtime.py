"""Retain the exact accepted v22 batching/query runtime before further repairs."""
from pathlib import Path
from text_corpus import file_hash,json_new,read_json,write_new


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    corpus=base/'reflow-20261031-v22';target=base/'transport-runtime-v22-20261031-v1'
    if target.exists():
        raise ValueError('Create-only runtime exists; preserve it')
    request=read_json(base/'build-request-reflow-20261031-v22.json')
    accepted=read_json(base/'integrity-reflow-20261031-v22.json')
    if not accepted['structural_integrity_pass']:
        raise ValueError('Accepted immutable v22 required')
    hashes={}
    for name in ('text_corpus.py','corpus_queries.py','corpus_reader.py','verify_reader_transport.py'):
        source=work/'scripts'/name;sha=file_hash(source)
        if sha!=request['implementation_sha256'][name]:
            raise ValueError('Runtime differs from frozen v22 build: '+name)
        write_new(target/'scripts'/name,source.read_bytes());hashes[name]=sha
    json_new(target/'manifest.json',{'corpus_root':str(corpus),'dataset_id':accepted['dataset_id'],
        'files':hashes,'purpose':'Machine transport reproduction only; no AI receipts or source acceptance.'})
    print({'runtime':str(target),'files':hashes},flush=True)


if __name__=='__main__':
    main()
