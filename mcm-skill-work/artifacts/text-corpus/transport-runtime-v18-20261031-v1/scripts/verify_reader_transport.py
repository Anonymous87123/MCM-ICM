"""Reconstruct EVERY selected paper through the real batching path, without ack.

This is a byte/position/transport test, not AI reading or source-fidelity approval.
No session, delivery, receipt or learning-progress files are created. Only the
explicit create-only diagnostic report is written after all input checks pass.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

from corpus_reader import Catalog, build_batch, wire, query_policy_hash
from corpus_queries import selected_blocks
from text_corpus import digest, encoded, file_hash, json_new

DEFAULT_QUERIES = ('abstract', 'introduction', 'problem_restatement', 'problem_analysis',
    'assumptions', 'notation', 'task_1', 'task_2', 'task_3', 'task_4',
    'model_building_and_solution', 'sensitivity_validation', 'improvements_evaluation',
    'appendix', 'all_author_text')


class BoundedFrozenCatalog(Catalog):
    """One-paper cache for this immutable-input simulation, rechecked afterward."""
    def __init__(self, root):
        super().__init__(root)
        self._paper = None
        self._text_key = None
        self._text = None

    def document(self, pid):
        if self._paper is None or self._paper['paper_id'] != pid:
            self._paper = super().document(pid)
        return self._paper

    def text_and_spans(self, selection):
        key = (selection['paper_id'], tuple(selection['section_ids']),
            tuple(selection.get('excluded_roles', [])), selection['text_sha256'], selection['characters'])
        if self._text_key != key:
            self._text = super().text_and_spans(selection)
            self._text_key = key
        return self._text


def verify_query(catalog, query, *, max_tokens=6000, max_bytes=32768, progress=None):
    selection = catalog.select(query)
    if [s['paper_id'] for s in selection] != [p['paper_id'] for p in catalog.papers]:
        raise ValueError('Transport test must include the full frozen paper queue, including empty parts')
    session = {'schema_version': 1, 'dataset_id': catalog.identity,
        'query_policy_sha256':query_policy_hash(),
        'run_id': 'transport-only-' + digest(encoded([catalog.identity, query, max_tokens, max_bytes]))[:32],
        'query': {'section': query, 'scope': 'all', 'year': None, 'title': False, 'mode': 'exhaustive'},
        'selection': selection, 'allow_unverified': True,
        'max_tokens': max_tokens, 'max_bytes': max_bytes}
    cursor = {'paper_index': 0, 'char_offset': 0}
    sequence = 0
    characters = [0] * len(selection)
    hashes = [hashlib.sha256() for _ in selection]
    references = {}
    wire_hash = hashlib.sha256()
    checkpoints = maximum = total_bytes = 0
    while cursor['paper_index'] < len(selection):
        batch = build_batch(catalog, session, cursor, sequence)
        payload = wire(batch) + b'\n'
        received = json.loads(payload.decode('utf-8', 'strict'))
        marker = received.pop('completion_marker')
        if (digest(wire(received)) != marker or not payload.rstrip(b'\n').endswith(
                b'"completion_marker":"' + marker.encode() + b'"}') or
                len(payload) > min(max_tokens, max_bytes)):
            raise ValueError('Wire marker, UTF-8 encoding or exact payload budget failed')
        if sequence % 11 == 0:
            restored = json.loads(json.dumps({'dataset_id': catalog.identity, 'cursor': cursor,
                'sequence': sequence}))
            replay = build_batch(catalog, session, restored['cursor'], restored['sequence'])
            if wire(replay) + b'\n' != payload:
                raise ValueError('Restored transport cursor changes a pending batch')
            checkpoints += 1
        if not batch.get('chunks') or batch['from_cursor'] != cursor or batch['to_cursor'] == cursor:
            raise ValueError('Transport did not advance through the exact selected text')
        expected_cursor = dict(cursor)
        for chunk in batch['chunks']:
            position = expected_cursor['paper_index']
            item = selection[position]
            if (chunk['paper_index'] != position or chunk['paper_id'] != item['paper_id'] or
                    chunk['start'] != expected_cursor['char_offset'] or chunk['start'] != characters[position] or
                    chunk['status'] != item['status'] or chunk['whole_text_sha256'] != item['text_sha256']):
                raise ValueError('Chunk order, empty-part status, identity or continuation changed')
            if position not in references:
                blocks = selected_blocks(catalog.document(item['paper_id']), item)
                text = '\n\n'.join(b['text'] for b in blocks)
                spans = []
                end = 0
                for i, block in enumerate(blocks):
                    begin = end + (2 if i else 0)
                    end = begin + len(block['text'])
                    spans.append({'block_id': block['block_id'], 'section_id': block['section_id'],
                        'pages': block['source_pages'], 'start': begin, 'end': end})
                if digest(text.encode()) != item['text_sha256'] or len(text) != item['characters']:
                    raise ValueError('Reference blocks differ from frozen query selection')
                references[position] = text, spans
            reference, spans = references[position]
            wanted = [s for s in spans if s['end'] > chunk['start'] and s['start'] < chunk['end']]
            if (chunk['text'] != reference[chunk['start']:chunk['end']] or
                    chunk['source_blocks'] != wanted or chunk['total_characters'] != len(reference) or
                    chunk['end'] - chunk['start'] != len(chunk['text'])):
                raise ValueError('Chunk text or complete source-block/page metadata differs')
            hashes[position].update(chunk['text'].encode())
            characters[position] += len(chunk['text'])
            if chunk['end'] == len(reference):
                expected_cursor = {'paper_index': position + 1, 'char_offset': 0}
                # Bound memory: the reference itself is not the AI's observations.
                references.pop(position)
            else:
                expected_cursor = {'paper_index': position, 'char_offset': chunk['end']}
        if batch['to_cursor'] != expected_cursor or batch['finished'] != (expected_cursor['paper_index'] == len(selection)):
            raise ValueError('Batch cursor or completion flag disagrees with reconstructed text')
        cursor = expected_cursor
        sequence += 1
        maximum = max(maximum, len(payload))
        total_bytes += len(payload)
        wire_hash.update(payload)
        if progress and sequence % 250 == 0:
            progress({'query': query, 'transport_batches': sequence, 'paper_cursor': cursor['paper_index']})
    papers = []
    for i, item in enumerate(selection):
        if characters[i] != item['characters'] or hashes[i].hexdigest() != item['text_sha256']:
            raise ValueError('Full reassembly lost, repeated or changed selected source text')
        papers.append({'paper_id': item['paper_id'], 'queue_position': item['queue_position'],
            'status': item['status'], 'characters': characters[i],
            'reassembled_text_sha256': hashes[i].hexdigest(), 'byte_reconstruction_pass': True})
    return {'query': query, 'target_papers': len(selection), 'selection_status_counts': dict(Counter(
            s['status'] for s in selection)), 'characters_reassembled': sum(characters),
        'transport_batches': sequence, 'resume_checkpoints_replayed': checkpoints,
        'max_tokens': max_tokens, 'max_bytes': max_bytes, 'maximum_wire_bytes': maximum,
        'total_simulated_wire_bytes': total_bytes, 'wire_stream_sha256': wire_hash.hexdigest(),
        'byte_reconstruction_pass': True, 'papers': papers,
        'ai_reading_receipts_created': 0, 'actual_ai_reading_acceptance': False}


def audit(root, queries=DEFAULT_QUERIES, *, max_tokens=6000, max_bytes=32768):
    scripts = Path(__file__).resolve().parent
    implementation = {name: file_hash(scripts / name) for name in
        ('verify_reader_transport.py', 'corpus_reader.py', 'corpus_queries.py', 'text_corpus.py')}
    catalog = BoundedFrozenCatalog(root)
    before = file_hash(root / 'catalog.json')
    results = []
    for query in queries:
        result = verify_query(catalog, query, max_tokens=max_tokens, max_bytes=max_bytes,
            progress=lambda value: print(value, flush=True))
        results.append(result)
        print({k: v for k, v in result.items() if k != 'papers'}, flush=True)
    fresh = Catalog(root)
    if fresh.identity != catalog.identity or file_hash(root / 'catalog.json') != before:
        raise ValueError('Corpus identity changed during transport verification')
    for paper in fresh.papers:
        fresh.document(paper['paper_id'])
    if any(file_hash(scripts / name) != sha for name, sha in implementation.items()):
        raise ValueError('Transport implementation changed during verification')
    return {'schema': 'reader-transport-reconstruction-v1', 'dataset_id': catalog.identity,
        'catalog_sha256': before, 'implementation_sha256': implementation,
        'target_papers': len(catalog.papers), 'queries': results,
        'transport_reconstruction_pass': True, 'ai_reading_receipts_created': 0,
        'source_fidelity_approved': False, 'full_read_acceptance': False,
        'meaning': 'Machine simulation of the exact production batching path; no AI receipt/session/delivery files created, no prose fidelity or understanding inferred.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus-root', type=Path, required=True)
    parser.add_argument('--query', action='append')
    parser.add_argument('--max-tokens', type=int, default=6000)
    parser.add_argument('--max-bytes', type=int, default=32768)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise ValueError('Create-only transport report exists; preserve it')
    result = audit(args.corpus_root.resolve(), args.query or DEFAULT_QUERIES,
        max_tokens=args.max_tokens, max_bytes=args.max_bytes)
    json_new(args.report, result)
    print({k: v for k, v in result.items() if k != 'queries'}, flush=True)
