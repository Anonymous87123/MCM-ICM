"""Create a small immutable runtime for reproducing v20 chapter delivery checks."""
from pathlib import Path
from text_corpus import file_hash,json_new,read_json,write_new


def main():
    work=Path(__file__).resolve().parents[1];base=work/'artifacts/text-corpus'
    corpus=base/'reflow-20261031-v20';target=base/'transport-runtime-v20-20261031-v1'
    if target.exists():
        raise ValueError('Create-only runtime already exists; preserve it')
    request=read_json(base/'build-request-reflow-20261031-v20.json')
    hashes={}
    for name in ('text_corpus.py','corpus_queries.py','corpus_reader.py','verify_reader_transport.py'):
        source=work/'scripts'/name;sha=file_hash(source)
        if sha!=request['implementation_sha256'][name]:
            raise ValueError('Runtime differs from frozen v20 build: '+name)
        write_new(target/'scripts'/name,source.read_bytes());hashes[name]=sha
    json_new(target/'manifest.json',{'corpus_root':str(corpus),'files':hashes,
             'purpose':'Reproduce machine transport checks only; no AI receipts or source acceptance.'})
    print({'runtime':str(target),'files':hashes},flush=True)


if __name__=='__main__':
    main()
