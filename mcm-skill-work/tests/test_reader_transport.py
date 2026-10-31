import copy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from corpus_reader import build_batch, next_batch, start, state, wire
from verify_reader_transport import verify_query
from test_text_corpus import fixture


class TransportReconstructionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.catalog = fixture(self.root, count=3, long=True)

    def tearDown(self):
        self.tmp.cleanup()

    def test_real_batch_constructor_matches_delivery_without_advancing_ai_progress(self):
        run = self.root / 'actual-run'
        start(self.catalog, 'abstract', run, max_tokens=2000)
        session, cursor, receipts, _ = state(self.catalog, run)
        batch = build_batch(self.catalog, session, cursor, 0)
        self.assertFalse((run / 'batches').exists())
        self.assertEqual(wire(batch), wire(next_batch(self.catalog, run)))
        self.assertEqual(state(self.catalog, run)[1], cursor)
        self.assertEqual(receipts, [])
        self.assertFalse((run / 'receipts').exists())

    def test_full_long_sections_and_smaller_budget_roundtrip_without_any_run_files(self):
        before = sorted(p.relative_to(self.root) for p in self.root.rglob('*'))
        for budget in (1500, 3000, 6000):
            report = verify_query(self.catalog, 'abstract', max_tokens=budget)
            self.assertTrue(report['byte_reconstruction_pass'])
            self.assertEqual(report['target_papers'], 3)
            self.assertGreater(report['transport_batches'], 3)
            self.assertGreater(report['resume_checkpoints_replayed'], 0)
            self.assertLessEqual(report['maximum_wire_bytes'], budget)
            self.assertEqual(report['ai_reading_receipts_created'], 0)
            self.assertFalse(report['actual_ai_reading_acceptance'])
        self.assertEqual(before, sorted(p.relative_to(self.root) for p in self.root.rglob('*')))

    def test_empty_unresolved_parts_are_accounted_not_silently_skipped(self):
        report = verify_query(self.catalog, 'notation')
        self.assertEqual(report['target_papers'], 3)
        self.assertEqual(report['selection_status_counts'], {'unresolved': 3})
        self.assertEqual(len(report['papers']), 3)
        self.assertEqual(report['characters_reassembled'], 0)
        self.assertFalse(report['actual_ai_reading_acceptance'])

    def test_multibyte_unicode_and_literal_replacement_glyphs_survive_splitting(self):
        from corpus_reader import Catalog
        from text_corpus import digest, encoded, file_hash
        for paper in self.catalog.papers:
            doc = self.catalog.document(paper['paper_id'])
            doc['blocks'][0]['text'] = ('完整段落，α和🙂，原文未解决字形\ufffd。 ' * 300)
            path = self.root / paper['document']
            path.write_bytes(encoded(doc))
            paper['document_sha256'] = file_hash(path)
        value = self.catalog.catalog
        value.pop('dataset_id')
        value['dataset_id'] = digest(encoded(value))
        (self.root / 'catalog.json').write_bytes(encoded(value))
        report = verify_query(Catalog(self.root), 'abstract', max_tokens=1500)
        self.assertTrue(report['byte_reconstruction_pass'])
        self.assertGreater(report['transport_batches'], 3)
        self.assertFalse(report['actual_ai_reading_acceptance'])

    def test_changed_generation_and_invalid_cursor_fail_closed(self):
        run = self.root / 'run'
        start(self.catalog, 'abstract', run)
        session, cursor, _, _ = state(self.catalog, run)
        changed = copy.deepcopy(session)
        changed['dataset_id'] = 'wrong-generation'
        with self.assertRaisesRegex(ValueError, 'version changed'):
            build_batch(self.catalog, changed, cursor, 0)
        for bad in ({'paper_index': -1, 'char_offset': 0},
                    {'paper_index': 3, 'char_offset': 1},
                    {'paper_index': 0, 'char_offset': 1000000}):
            with self.assertRaisesRegex(ValueError, 'Cursor'):
                build_batch(self.catalog, session, bad, 0)

    def test_corrupted_reassembly_is_rejected_even_with_a_recomputed_end_marker(self):
        from text_corpus import digest
        original = build_batch

        def damaged(*args, **kwargs):
            batch = original(*args, **kwargs)
            batch['chunks'][0]['text'] = batch['chunks'][0]['text'][1:]
            batch.pop('completion_marker')
            batch['completion_marker'] = digest(wire(batch))
            return batch

        with patch('verify_reader_transport.build_batch', side_effect=damaged):
            with self.assertRaisesRegex(ValueError, 'Chunk text'):
                verify_query(self.catalog, 'abstract')


if __name__ == '__main__':
    unittest.main()
