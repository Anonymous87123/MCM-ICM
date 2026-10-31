"""Inline font metrics must not reorder surrounding prose or mutate evidence."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from text_corpus import make_document, order_lines, prose_flow_line


def prose(text, y, idx, x=60, width=450):
    return {"text":text,"bbox":[x,y,x+width,y+16],"line_id":f"l{idx}",
            "page":1,"font_size":12,"bold":False,"native_block":1,
            "spans":[{"text":text,"bbox":[x,y,x+width,y+16],"font":"TimesNewRoman","size":12}]}


def inline(y=132,idx=2,x=60,width=450):
    item=prose("(X) as the function of the impact location and ball mass",y,idx,x,width)
    item["bbox"][1]=y-27;item["bbox"][3]=y+43
    item["spans"]=[{"text":"X","font":"CambriaMath","size":12,"bbox":[x,y-27,x+10,y+43]},
                   {"text":item["text"][2:],"font":"TimesNewRoman","size":12,
                    "bbox":[x+10,y,x+width,y+16]}]
    return item


class ProseFlowGeometryTests(unittest.TestCase):
    def test_inline_font_bbox_cannot_pull_following_prose_before_previous_line(self):
        lines=[prose("We derive the expression of batted ball speed",116,1),inline(),
               prose("and retain all original source words in this paragraph.",148,3)]
        original=copy.deepcopy(lines)
        doc=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
               "lines":lines,"comparison":{"status":"agreement"}}],improved=True)
        paragraphs=[b for b in doc["blocks"] if b["kind"]=="prose"]
        self.assertEqual([b["text"] for b in paragraphs],[" ".join(x["text"] for x in lines)])
        self.assertEqual(paragraphs[0]["source_line_ids"],["l1","l2","l3"])
        self.assertEqual(lines,original)
        self.assertTrue(any(r["operation"]=="prose_flow_geometry_candidate" for r in paragraphs[0]["repairs"]))
        self.assertIn("inline_math_prose_flow_review",[d["code"] for d in doc["defects"]])
        self.assertTrue(all(s["boundary_status"]=="pending" for s in doc["sections"]))

    def test_equation_sparse_label_normal_inline_and_dropcap_unchanged(self):
        for text in ("X = Y + Z", "speed X", "one two three"):
            item=inline();item["spans"][1]["text"]=text
            self.assertIs(prose_flow_line(item),item)
        ordinary=inline();ordinary["spans"][0]["bbox"][1:4:2]=[130,150]
        self.assertIs(prose_flow_line(ordinary),ordinary)
        dropcap=inline();dropcap["spans"][0]["font"]="TimesNewRoman"
        self.assertIs(prose_flow_line(dropcap),dropcap)

    def test_two_columns_keep_lane_order_and_every_line_once(self):
        lines=[]
        for n in range(8):
            for lane,x in enumerate((50,330)):
                item=inline(100+n*20,n+lane*10,x,200) if n==2 else prose(
                    f"Column {lane} keeps these ordinary source words",100+n*20,n+lane*10,x,200)
                lines.append(item)
        ordered,multi=order_lines([prose_flow_line(x) for x in lines],600)
        self.assertTrue(multi)
        self.assertEqual([x["line_id"] for x in ordered],
                         [f"l{i}" for i in range(8)]+[f"l{i+10}" for i in range(8)])


if __name__ == "__main__":
    unittest.main()
