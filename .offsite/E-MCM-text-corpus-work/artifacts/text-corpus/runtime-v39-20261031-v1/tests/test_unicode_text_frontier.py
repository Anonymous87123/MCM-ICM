import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_unicode_text_frontier import glyph_contexts


class GlyphContextTests(unittest.TestCase):
    def test_inline_and_display_like_damage_are_both_retained_with_context(self):
        text = 'Author explanation \ufffd next to an object; then \ud800 continues.'
        result = glyph_contexts(text)
        self.assertEqual([r['codepoint'] for r in result], ['U+FFFD', 'U+D800'])
        self.assertEqual([text[r['offset']] for r in result], ['\ufffd', '\ud800'])
        self.assertIn('Author explanation', result[0]['context'])
        self.assertIn('continues.', result[1]['context'])

    def test_valid_unicode_and_private_symbols_are_not_silently_called_repaired(self):
        self.assertEqual(glyph_contexts('Text with λ, a printed bullet \uf06c, and 中文.'), [])


if __name__ == '__main__':
    unittest.main()
