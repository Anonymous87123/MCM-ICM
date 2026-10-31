"""Freeze the completed v18 reader for read-only transport checks."""
from pathlib import Path
from corpus_reader import Catalog
from text_corpus import file_hash, json_new, read_json, write_new


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    root=base/'reflow-20261031-v18'
    output=base/'transport-runtime-v18-20261031-v1'
    if output.exists():
        raise ValueError('Create-only validation runtime exists')
    request=read_json(base/'build-request-reflow-20261031-v18.json')
    report=read_json(base/'integrity-reflow-20261031-v18.json')
    if not report['structural_integrity_pass'] or report['dataset_id']!=Catalog(root).identity:
        raise ValueError('Completed v18 structural report required')
    hashes={}
    for name in ('text_corpus.py','corpus_queries.py','corpus_reader.py','verify_reader_transport.py'):
        source=work/'scripts'/name
        sha=file_hash(source)
        if name in request['implementation_sha256'] and sha!=request['implementation_sha256'][name]:
            raise ValueError('V18 runtime no longer matches: '+name)
        hashes[name]=sha
    for name,sha in hashes.items():
        source=work/'scripts'/name
        if file_hash(source)!=sha:
            raise ValueError('Code changed while freezing runtime')
        write_new(output/'scripts'/name,source.read_bytes())
    json_new(output/'manifest.json',{'dataset_id':report['dataset_id'],'files':hashes,
        'purpose':'Read-only exact v18 transport verification; no AI receipts or source acceptance.'})
    print({'runtime':str(output),'files':len(hashes),'dataset_id':report['dataset_id']},flush=True)


if __name__=='__main__':
    main()
