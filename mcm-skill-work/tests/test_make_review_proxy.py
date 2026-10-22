from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from PIL import Image

from scripts.make_review_proxy import main


class MakeReviewProxyTests(unittest.TestCase):
    def run_proxy(self, *arguments: str) -> dict[str, object]:
        output = io.StringIO()
        with redirect_stdout(output):
            result = main(list(arguments))
        self.assertEqual(result, 0)
        return json.loads(output.getvalue())

    def test_cli_creates_a_jpeg_within_the_requested_byte_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.png"
            proxy = root / "proxy.jpg"
            Image.effect_noise((1200, 1600), 100).convert("RGB").save(source)

            report = self.run_proxy(
                "--input",
                str(source),
                "--output",
                str(proxy),
                "--max-bytes",
                "450000",
            )

            self.assertLessEqual(proxy.stat().st_size, 450_000)
            self.assertEqual(report["bytes"], proxy.stat().st_size)
            with Image.open(proxy) as image:
                self.assertEqual(image.format, "JPEG")
                self.assertLessEqual(image.width, 1400)
                self.assertLessEqual(image.height, 1800)

    def test_crop_is_applied_before_proxy_encoding(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.png"
            proxy = root / "crop.jpg"
            Image.new("RGB", (1000, 800), "white").save(source)

            report = self.run_proxy(
                "--input",
                str(source),
                "--output",
                str(proxy),
                "--crop",
                "100,150,700,650",
            )

            self.assertEqual(report["crop"], [100, 150, 700, 650])
            self.assertEqual(report["proxy_width"], 600)
            self.assertEqual(report["proxy_height"], 500)

    def test_out_of_bounds_crop_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.png"
            proxy = root / "crop.jpg"
            Image.new("RGB", (640, 480), "white").save(source)

            with self.assertRaisesRegex(SystemExit, "crop exceeds source bounds"):
                main(
                    [
                        "--input",
                        str(source),
                        "--output",
                        str(proxy),
                        "--crop",
                        "0,0,641,480",
                    ]
                )


if __name__ == "__main__":
    unittest.main()
