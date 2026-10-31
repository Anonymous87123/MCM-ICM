from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from corpus_queries import select_sections, selected_blocks
from text_corpus import export_document, file_hash, text_with_block_spans, validate_author_export


class ContinuousAuthorExportTests(unittest.TestCase):
    def document(self):
        sections = [
            ('summary', None, 'abstract', 'Summary'),
            ('child', 'summary', 'other', 'Author detail'),
            ('refs', 'summary', 'references', 'References'),
            ('refs-child', 'refs', 'other', 'Nested bibliography'),
            ('body', None, 'model', 'Method'),
        ]
        blocks = [
            ('form', 'summary', 'front_matter', 'Control number 42', [1]),
            ('summary-title', 'summary', 'heading', 'Summary', [1]),
            ('a', 'summary', 'prose', 'We compare café locations. In addi', [1]),
            ('page', 'summary', 'furniture', '1', [1]),
            ('b', 'summary', 'prose', 'tion, we keep all alternatives.', [2]),
            ('child', 'child', 'prose', 'A short author paragraph.', [2]),
            ('refs', 'refs', 'references', 'Third-party reference', [2]),
            ('refs-child', 'refs-child', 'prose', 'Nested reference prose', [2]),
            ('body-title', 'body', 'heading', 'Method', [3]),
            ('body', 'body', 'prose', 'Results enter the next decision.', [3]),
            ('caption', 'body', 'caption', 'Figure 1. Retained separately.', [3]),
        ]
        result = {'paper_id': 'synthetic', 'source_sha256': 'f' * 64,
                  'raw_pages_sha256': 'e' * 64, 'status': 'machine-draft',
                  'sections': [{'section_id': sid, 'parent_id': parent, 'role': role,
                                'title': title, 'boundary_status': 'pending'}
                               for sid, parent, role, title in sections],
                  'blocks': [{'block_id': bid, 'section_id': sid, 'kind': kind,
                              'text': text, 'source_pages': pages}
                             for bid, sid, kind, text, pages in blocks]}
        result['blocks'][4].update(paragraph_continues_from='a', paragraph_join_separator='')
        return result

    def test_continuous_view_matches_reader_without_furniture_or_nested_references(self):
        doc = self.document()
        ids, excluded = select_sections(doc, 'all_author_text')
        reader_text, reader_spans = text_with_block_spans(selected_blocks(
            doc, {'section_ids': ids, 'excluded_roles': sorted(excluded)}))
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            export_document(folder, doc)
            saved = json.loads((folder / 'document.json').read_text(encoding='utf-8'))
            text = (folder / 'author.md').read_bytes().decode('utf-8')
            mapping = json.loads((folder / 'author.source-map.json').read_text(encoding='utf-8'))
            self.assertEqual(text, reader_text + '\n')
            self.assertIn('In addition,', text)
            self.assertIn('A short author paragraph.', text)
            self.assertIn('Results enter the next decision.', text)
            for excluded_text in ('Control number', 'Third-party reference', 'Nested reference prose', 'Figure 1.'):
                self.assertNotIn(excluded_text, text)
                self.assertIn(excluded_text, (folder / 'full.md').read_text(encoding='utf-8'))
            self.assertEqual(mapping['block_spans'], reader_spans)
            self.assertEqual(mapping['document_sha256'], file_hash(folder / 'document.json'))
            by_id = {b['block_id']: b for b in doc['blocks']}
            for span in mapping['block_spans']:
                self.assertEqual(text[span['start']:span['end']], by_id[span['block_id']]['text'])
            self.assertFalse(mapping['source_fidelity_accepted'])
            self.assertEqual(validate_author_export(folder, saved), [])

    def test_view_and_map_corruption_are_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            export_document(folder, self.document())
            saved = json.loads((folder / 'document.json').read_text(encoding='utf-8'))
            with (folder / 'author.md').open('ab') as stream:
                stream.write(b'Silent extra prose')
            self.assertTrue(validate_author_export(folder, saved))
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            export_document(folder, self.document())
            saved = json.loads((folder / 'document.json').read_text(encoding='utf-8'))
            mapping = json.loads((folder / 'author.source-map.json').read_text(encoding='utf-8'))
            mapping['block_spans'][1]['start'] += 1
            (folder / 'author.source-map.json').write_text(json.dumps(mapping), encoding='utf-8')
            self.assertTrue(validate_author_export(folder, saved))

    def test_old_generations_remain_valid_without_new_view_but_unknown_policy_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            doc = self.document()
            self.assertEqual(validate_author_export(folder, doc), [])
            doc['author_view_policy'] = 'unknown'
            self.assertTrue(validate_author_export(folder, doc))


if __name__ == '__main__':
    unittest.main()
