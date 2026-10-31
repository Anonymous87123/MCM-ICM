"""Create-only, hash-bound page overviews for text/heading coverage checks.

These bounded overviews complement full native prose reading, not replace it.
They do not interpret formulas or charts. Original page images stay on disk.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw

from make_review_proxy import main as proxy_main
from text_corpus import file_hash, json_new, read_json


def prepare(review_dir: Path, groups: list[list[int]], output: Path):
    manifest_path = review_dir / "manifest.json"
    manifest = read_json(manifest_path)
    if output.exists() or not groups or any(not 1 <= len(g) <= 3 or len(set(g)) != len(g) for g in groups):
        raise ValueError("Choose new output and distinct groups of one to three physical pages")
    pages = {p["physical_page"]: p for p in manifest["pages"]}
    all_numbers = [p for group in groups for p in group]
    if len(set(all_numbers)) != len(all_numbers) or not set(all_numbers) <= set(pages):
        raise ValueError("Contact-sheet coverage must be nonduplicated manifest pages")
    for number in all_numbers:
        record = pages[number]; image = (review_dir / record["raw_png"]).resolve()
        if not image.is_relative_to(review_dir.resolve()) or file_hash(image) != record["raw_sha256"]:
            raise ValueError("Frozen source-page rendering changed")
    output.mkdir(parents=True)
    sheets = []
    for index, numbers in enumerate(groups):
        tiles = []
        for number in numbers:
            with Image.open(review_dir / pages[number]["raw_png"]) as opened:
                tile = opened.convert("RGB")
                tile.thumbnail((1400, 1800), Image.Resampling.LANCZOS)
            labelled = Image.new("RGB", (tile.width, tile.height+40), "white")
            labelled.paste(tile, (0,40))
            ImageDraw.Draw(labelled).text((12,10), f"PHYSICAL PAGE {number}", fill="black")
            tiles.append(labelled)
        canvas = Image.new("RGB", (sum(t.width for t in tiles), max(t.height for t in tiles)), "white")
        x=0
        for tile in tiles:
            canvas.paste(tile,(x,0)); x += tile.width
        png=output/f"sheet-{index:02d}.png"; jpg=png.with_suffix(".jpg")
        canvas.save(png)
        proxy_main(["--input",str(png),"--output",str(jpg),"--max-width","3000",
                    "--max-height","1840","--max-bytes","450000"])
        sheets.append({"physical_pages":numbers,"proxy":jpg.name,"bytes":jpg.stat().st_size,
                       "proxy_sha256":file_hash(jpg),"raw_contact_sheet":png.name,"raw_sha256":file_hash(png)})
    result={"paper_id":manifest["paper_id"],"source_sha256":manifest["source_sha256"],
            "raw_pages_sha256":manifest["raw_pages_sha256"],"page_manifest_sha256":file_hash(manifest_path),
            "physical_page_coverage":all_numbers,"sheets":sheets,
            "purpose":"text heading and page coverage; full prose is read separately",
            "formula_verification":"paused","figure_distillation":"paused"}
    json_new(output/"manifest.json",result)
    return result


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--review-dir",type=Path,required=True)
    p.add_argument("--group",type=int,nargs="+",action="append",required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args();prepare(args.review_dir.resolve(),args.group,args.output.resolve())
