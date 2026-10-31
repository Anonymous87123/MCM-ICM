import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import trace_d38727_closure as trace


class D38727ProvenanceTests(unittest.TestCase):
    def session(self, path, records):
        path.write_text("".join(json.dumps(row) + "\n" for row in records), encoding="utf-8")

    def test_text_only_drops_images_and_reasoning_blocks(self):
        blocks = [{"type": "text", "text": "validator result"},
                  {"type": "image", "source": {"data": "DO_NOT_EXPORT"}},
                  {"type": "thinking", "thinking": "DO_NOT_EXPORT"},
                  {"type": "text", "text": "data:image/png;base64,DO_NOT_EXPORT"}]
        text = trace.text_only(blocks)
        self.assertIn("validator result", text)
        self.assertNotIn("DO_NOT_EXPORT", text)
        self.assertNotIn("data:image", text)

    def test_bounded_reader_ignores_api_request_duplicates(self):
        call_id = next(iter(trace.CALLS))
        command = {"type": "tool_use", "id": call_id, "name": "Bash", "input": {"command": "python validator.py"}}
        records = [
            {"type": "api-request", "message": {"content": [command]}},
            {"type": "assistant", "timestamp": "example", "message": {"content": [command, {"type": "thinking", "thinking": "DO_NOT_EXPORT"}]}},
            {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": call_id, "content": "MODEL:0"}]}},
            {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "other", "name": "Read", "input": {"file_path": "page.png"}}]}},
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.jsonl"
            self.session(path, records)
            evidence, images = trace.inspect_session(path, start=2, end=3)
        self.assertEqual([item["line"] for item in evidence], [2, 3])
        self.assertEqual(images, [])
        self.assertFalse(evidence[0]["complete_visual_flag_present"])
        self.assertNotIn("DO_NOT_EXPORT", json.dumps(evidence))

    def test_oversized_command_is_not_exported(self):
        call_id = next(iter(trace.CALLS))
        row = {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": call_id, "input": {"command": "x" * 5001}}]}}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.jsonl"
            self.session(path, [row])
            with self.assertRaisesRegex(ValueError, "oversized or image-bearing"):
                trace.inspect_session(path, 1, 1)

    def test_duplicate_calls_cannot_replace_a_missing_result(self):
        evidence = []
        for call_id in trace.CALLS:
            evidence.extend([{"call_id": call_id, "kind": "tool_use"}] * 2)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "trace.json"
            with mock.patch.object(trace, "inspect_session", return_value=(evidence, [])), mock.patch.object(trace.tx, "load_history") as loader:
                with self.assertRaisesRegex(ValueError, "three original calls"):
                    trace.build(Path("unused"), output)
                loader.assert_not_called()
            self.assertFalse(output.exists())

    def test_existing_report_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "trace.json"
            output.write_bytes(b"old evidence")
            with mock.patch.object(trace, "inspect_session") as reader:
                with self.assertRaises(FileExistsError):
                    trace.build(Path("unused"), output)
                reader.assert_not_called()
            self.assertEqual(output.read_bytes(), b"old evidence")


if __name__ == "__main__":
    unittest.main()
