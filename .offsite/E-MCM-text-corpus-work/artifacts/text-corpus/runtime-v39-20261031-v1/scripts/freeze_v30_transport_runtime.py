"""Freeze acceptedv30 transport code; preserve earlier runtimes and receipts."""
from pathlib import Path
from text_corpus import file_hash, json_new, read_json, write_new


def main():
    work = Path(__file__).resolve().parents[1]
    base = work / 'artifacts/text-corpus'
    target = base / 'transport-runtime-v30-20261031-v1'
    if target.exists():
        raise ValueError('Create-only runtime exists; preserve it')
    accepted = read_json(base / 'integrity-reflow-20261031-v30.json')
    if not accepted['structural_integrity_pass'] or accepted['totals'].get('continuous_author_views_checked') != 435:
        raise ValueError('Accepted immutablev30 with435continuous author views required')
    names = ('text_corpus.py', 'corpus_queries.py', 'corpus_reader.py', 'verify_reader_transport.py')
    hashes = {name: file_hash(work / 'scripts' / name) for name in names}
    request = read_json(base / 'build-request-reflow-20261031-v30.json')
    if any(sha != request['implementation_sha256'][name] for name, sha in hashes.items()):
        raise ValueError('Runtime differs from accepted frozen build')
    for name in names:
        write_new(target / 'scripts' / name, (work / 'scripts' / name).read_bytes())
    json_new(target / 'manifest.json', {'corpus_root': str(base / 'reflow-20261031-v30'),
        'dataset_id': accepted['dataset_id'], 'files': hashes,
        'purpose': 'Exact machine transport reconstruction; creates no AI receipts or source acceptance.'})
    print({'runtime': str(target), 'files': hashes}, flush=True)


if __name__ == '__main__':
    main()
