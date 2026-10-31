from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from package_text_corpus_skill import package
from test_text_corpus import fixture
from text_corpus import json_new


class PackageQueryPolicyTests(unittest.TestCase):
    def test_preview_cannot_hide_mixed_database_and_reader_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            corpus = root/'corpus'
            fixture(corpus,count=1)
            json_new(corpus/'scope.json',{'input_sha256':{'queries':'0'*64}})
            with patch('package_text_corpus_skill.validate') as validator:
                with self.assertRaisesRegex(ValueError,'freeze query policy'):
                    package(root/'base',corpus,root/'output',preview=True)
                validator.assert_not_called()
            self.assertFalse((root/'output').exists())


if __name__ == '__main__':
    unittest.main()
