from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
import shutil
import sqlite3
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from text_corpus import (canonical_role, digest, encoded, export_document, file_hash,
                         is_heading, json_new, make_document, order_lines, section_blocks, section_text, title_role)
from corpus_reader import Catalog, acknowledge, next_batch, start, state, status, wire,author_text_coverage
from corpus_queries import task_numbers,all_author_blocks
from build_text_corpus import extract_record
from index_text_corpus import index
from validate_text_corpus import validate
from resegment_text_corpus import (apply_reviews, independent_key, resegment,
                                  resolve_exact_comparisons, validate_exact_comparisons)
from source_text_repairs import apply_text_repairs, replay_block, validate_evidence
from recover_empty_text_frontier import frontier, run as recover_frontier
from package_text_corpus_skill import package as package_corpus_skill
from audit_text_section_candidates import abstract_findings
from source_absence_reviews import (prepare_absence_reviews,apply_absence_reviews,validate_absence_reviews,
                                    prepare_review_bundles,validate_review_bundle)
from source_layout_reviews import apply_layout_reviews,validate_layout_reviews


def line(text, page=1, x=60, y=100, width=450, size=11, bold=False, block=0, idx=0):
    return {"text": text, "page": page, "bbox": [x, y, x+width, y+12], "font_size": size,
            "bold": bold, "native_block": block, "line_id": f"p{page}-b{block}-l{idx}"}


def fixture(root, count=3, verified=True, long=False, role="abstract"):
    papers = []
    for i in range(count):
        pid = f"P-A-2020-{i}-test"
        text = ("A complete paragraph reports a baseline, a change and a limit. " * (400 if long else 2)) + f"Paper {i}."
        doc = {"paper_id": pid, "source_sha256": "f" * 64, "raw_pages_sha256": "e" * 64, "page_count": 2,
               "verified_absent_roles": [],
               "sections": [
                   {"section_id": "s1", "title": "Summary", "role": role, "parent_id": None,
                    "boundary_status": "verified" if verified else "pending"},
                   {"section_id": "s2", "title": "A second summary subsection", "role": role, "parent_id": "s1",
                    "boundary_status": "verified" if verified else "pending"}],
               "blocks": [{"block_id": "b1", "section_id": "s1", "kind": "prose", "text": text,
                           "source_pages": [1], "issues": []},
                          {"block_id": "b2", "section_id": "s2", "kind": "prose", "text": "Tail paragraph.",
                           "source_pages": [2], "issues": []}]}
        if verified:
            for s in doc["sections"]:
                s["review"] = {"reviewer": "synthetic-test-only", "source_sha256": doc["source_sha256"],
                               "raw_pages_sha256": doc["raw_pages_sha256"],
                               "text_sha256": digest(section_text(doc, [s["section_id"]]).encode()),
                               "section_boundaries_checked": True, "paragraph_boundaries_checked": True,
                               "checked_pages": [1, 2]}
        path = root / "papers" / pid / "document.json"; json_new(path, doc)
        papers.append({"paper_id": pid, "queue_position": i+1, "problem_type": "A", "year": 2020,
                       "source_sha256": doc["source_sha256"], "document": str(path.relative_to(root)).replace("\\", "/"),
                       "document_sha256": file_hash(path)})
    catalog = {"schema_version": 1, "papers": papers}
    catalog["dataset_id"] = digest(encoded(catalog)); json_new(root / "catalog.json", catalog)
    return Catalog(root)


class TextReconstructionTests(unittest.TestCase):
    def test_summary_alias(self):
        for alias in ("Summary", "SUMMARY SHEET", "摘要", "abstract"):
            self.assertEqual(canonical_role(alias), "abstract")

    def test_competition_banner_is_summary_not_model(self):
        self.assertEqual(title_role("2016 Mathematical Contest in Modeling (MCM) Summary Sheet", 1), "abstract")
        self.assertFalse(is_heading(line("• Analytical Model: Using Fourier analysis we derive an analytical solution", bold=True), 11))

    def test_no_short_prose_filter_and_all_source_lines_accounted(self):
        lines = [line("Summary", bold=True), line("We stop.", y=130, block=1),
                 line("x = 2.", y=150, block=2)]
        doc = make_document({"paper_id": "p"}, [{"page": 1, "width": 600, "height": 800,
                                                "lines": lines, "comparison": {"status": "agreement"}}])
        refs = [r for b in doc["blocks"] for r in b["source_line_ids"]]
        self.assertCountEqual(refs, [x["line_id"] for x in lines])
        text = section_text(doc, [s["section_id"] for s in doc["sections"] if s["role"] == "abstract"])
        self.assertIn("We stop.", text); self.assertIn("x = 2.", text)
        self.assertTrue(all(s["boundary_status"] == "pending" for s in doc["sections"]))

    def test_untitled_opening_paragraphs_are_candidates_not_omitted_or_certified(self):
        ps=[{"page":1,"width":600,"height":800,"comparison":{"status":"agreement"},
             "lines":[line("An untitled abstract retains this whole paragraph.",y=100),
                      line("A second paragraph follows with further results.",y=150,block=1)]},
            {"page":2,"width":600,"height":800,"comparison":{"status":"agreement"},
             "lines":[line("1 Introduction",page=2,bold=True),
                      line("The actual introduction starts here.",page=2,y=140,block=1)]}]
        d=make_document({"paper_id":"synthetic"},ps,improved=True)
        opening=d["sections"][0]
        self.assertEqual(opening["origin"],"inferred-opening")
        self.assertEqual(opening["boundary_status"],"pending")
        self.assertEqual(section_text(d,[opening["section_id"]]),
                         "An untitled abstract retains this whole paragraph.\n\nA second paragraph follows with further results.")

    def test_columns_are_not_row_interleaved(self):
        lines = []
        for n in range(8):
            lines += [line(f"L{n} an entire complete source line", x=50, width=200, y=100+n*20, idx=n),
                      line(f"R{n} an entire complete source line", x=330, width=200, y=100+n*20, block=1, idx=n)]
        ordered, multi = order_lines(lines, 600)
        self.assertTrue(multi)
        self.assertEqual([x["text"].split()[0] for x in ordered], [f"L{i}" for i in range(8)]+[f"R{i}" for i in range(8)])

    def test_center_gutter_line_is_never_duplicated(self):
        ls = []
        for n in range(8):
            ls += [line("Left has enough source words", x=50, width=200, y=100+n*20, idx=n),
                   line("Right has enough source words", x=330, width=200, y=100+n*20, block=1, idx=n)]
        ls.append(line("x", x=298, width=4, y=170, block=2))
        ordered, multi = order_lines(ls, 600)
        self.assertTrue(multi)
        self.assertCountEqual([x["line_id"] for x in ordered], [x["line_id"] for x in ls])

    def test_cross_page_fragments_are_flagged_not_silently_joined(self):
        pages = [{"page": p, "width": 600, "height": 800,
                  "lines": [line(t, page=p)], "comparison": {"status": "agreement"}}
                 for p, t in [(1, "This sentence continues"), (2, "on the next page.")]]
        doc = make_document({"paper_id": "p"}, pages)
        self.assertIn("cross_page_join_review", [d["code"] for d in doc["defects"]])

    def test_empty_native_runs_do_not_split_a_continuous_paragraph(self):
        ls = [line("We describe a collision", idx=0), line(" ", y=114, idx=1),
              line("between a ball and a bat.", y=114, idx=2)]
        doc = make_document({"paper_id": "p"}, [{"page": 1, "width": 600, "height": 800,
                   "lines": ls, "comparison": {"status": "agreement"}}], improved=True)
        prose = [b for b in doc["blocks"] if b["kind"] == "prose"]
        self.assertEqual(len(prose), 1)
        self.assertEqual(prose[0]["text"], "We describe a collision between a ball and a bat.")
        self.assertEqual(len(doc["excluded_source_lines"]), 1)

    def test_native_block_per_line_is_not_a_paragraph_per_line(self):
        ls = [line("A continuous first line",x=84,y=100,block=1),
              line("continues onto its next line.",y=118,block=2),
              line("A genuinely indented next paragraph.",x=84,y=136,block=3)]
        doc = make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                            "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        prose=[b["text"] for b in doc["blocks"] if b["kind"]=="prose"]
        self.assertEqual(prose,["A continuous first line continues onto its next line.",
                                "A genuinely indented next paragraph."])

    def test_hanging_bullet_continuation_and_next_indented_paragraph(self):
        ls = [line("A full opening paragraph sets the ordinary body margin.", y=100,block=1),
              line("\uf0d8 A long bullet item continues onto another", x=81,y=118,block=2),
              line("indented line and finishes here.",x=102,y=136,block=3),
              line("The next author paragraph begins with an indent.",x=84,y=154,block=4)]
        doc=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                          "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        prose=[b["text"] for b in doc["blocks"] if b["kind"]=="prose"]
        self.assertEqual(len(prose),3)
        self.assertIn("another indented line",prose[1])

    def test_double_spaced_native_blocks_restore_indented_and_blank_line_paragraphs(self):
        ls=[line("Summary",bold=True,y=80)]
        texts=["The first paragraph has many words and continues with",
               "more ordinary words along the line without stopping its",
               "source sentence and it continues with enough other words",
               "until this first paragraph finally reaches its original end.",
               "The second indented paragraph has many words and continues",
               "onto another original source line with enough ordinary words",
               "and more original words before its final source sentence ends.",
               "The third paragraph follows a blank line with many words",
               "and continues with more words without a paragraph split",
               "until this paragraph finally reaches its original ending."]
        for i,t in enumerate(texts):
            ls.append(line(t,x=84 if i in (0,4) else 60,y=120+i*24+(24 if i>=7 else 0),block=i+1))
        d=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                   "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        prose=[b["text"] for b in d["blocks"] if b["kind"]=="prose"]
        self.assertEqual(prose,[" ".join(texts[:4])," ".join(texts[4:7])," ".join(texts[7:])])
        self.assertIn("expanded_line_spacing_review",[x["code"] for x in d["defects"]])
        self.assertTrue(all(s["boundary_status"]=="pending" for s in d["sections"]))

    def test_equal_spaced_complete_sentences_do_not_create_a_wrap_baseline(self):
        ls=[line(f"This is complete independent paragraph number {i} with enough words.",
                 y=100+i*24,block=i) for i in range(8)]
        d=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                   "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        self.assertEqual(len([b for b in d["blocks"] if b["kind"]=="prose"]),8)
        self.assertNotIn("expanded_line_spacing_review",[x["code"] for x in d["defects"]])

    def test_new_page_editor_letter_is_not_abstract_and_is_retained_as_memo(self):
        pages=[{"page":1,"width":600,"height":800,"comparison":{"status":"agreement"},
                "lines":[line("Summary",bold=True),line("A real author summary ends here.",y=140,block=1)]},
               {"page":2,"width":600,"height":800,"comparison":{"status":"agreement"},
                "lines":[line("Team #123",page=2,y=40),line("Dear editor,",page=2,y=90,block=1),
                         line("We request publication of the paper in your journal.",page=2,y=140,block=2)]}]
        d=make_document({"paper_id":"synthetic"},pages,improved=True)
        abstract=section_text(d,[s["section_id"] for s in d["sections"] if s["role"]=="abstract"])
        memo=section_text(d,[s["section_id"] for s in d["sections"] if s["role"]=="memo"])
        self.assertNotIn("editor",abstract);self.assertNotIn("publication",abstract)
        self.assertIn("Dear editor,",memo);self.assertIn("publication",memo)
        self.assertIn("opening_letter_boundary_review",[x["code"] for x in d["defects"]])

    def test_mid_summary_salutation_quote_cannot_start_a_letter_section(self):
        ls=[line("Summary",bold=True),line("Dear editor,",y=140,block=1),
            line("This address is discussed inside the author summary.",y=180,block=2)]
        d=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                   "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        self.assertFalse(any(s["role"]=="memo" for s in d["sections"]))

    def test_toc_entry_before_contents_title_cannot_leak_into_summary(self):
        ps = [{"page": 1, "width": 600, "height": 800, "comparison": {"status": "agreement"},
               "lines": [line("Summary", bold=True), line("A complete summary ends here.", y=140, block=1)]},
              {"page": 2, "width": 600, "height": 800, "comparison": {"status": "agreement"},
               "lines": [line("1 Introduction", page=2, y=100, block=1),
                         line("Contents", page=2, y=102, bold=True),
                         *[line("........... 2", page=2, y=140+i*20, block=2, idx=i) for i in range(3)]]}]
        doc = make_document({"paper_id": "p"}, ps, improved=True)
        abstract = section_text(doc, [s["section_id"] for s in doc["sections"] if s["role"] == "abstract"])
        self.assertNotIn("Introduction", abstract)
        self.assertNotIn("Contents", abstract)

    def test_singular_content_and_spaced_dot_leaders_stop_abstract(self):
        ps=[{"page":1,"width":600,"height":800,"comparison":{"status":"agreement"},
             "lines":[line("Summary",bold=True),line("A full abstract ends here.",y=130,block=1)]},
            {"page":2,"width":600,"height":800,"comparison":{"status":"agreement"},
             "lines":[line("Content",page=2,bold=True),
                      *[line(f"A chapter . . . . . {i}",page=2,y=140+i*20,block=1,idx=i) for i in range(3)]]}]
        d=make_document({"paper_id":"synthetic"},ps,improved=True)
        text=section_text(d,[s["section_id"] for s in d["sections"] if s["role"]=="abstract"])
        self.assertEqual(text,"Summary\n\nA full abstract ends here.")

    def test_untitled_dense_contents_preserves_lines_without_polluting_summary(self):
        entries = [line(f"A source chapter . . . . . . {i}", page=2, y=120+i*20, block=2, idx=i)
                   for i in range(1, 10)]
        fragments = [line(f"{i}.1", page=2, y=125+i*20, block=3, idx=i) for i in range(1, 7)]
        pages = [{"page":1,"width":600,"height":800,"comparison":{"status":"agreement"},
                  "lines":[line("Summary",bold=True),line("A full source abstract ends here.",y=140,block=1)]},
                 {"page":2,"width":600,"height":800,"comparison":{"status":"agreement"},
                  "lines":[line("Team #12345",page=2,y=30),*entries,*fragments]}]
        doc=make_document({"paper_id":"synthetic"},pages,improved=True)
        abstract=section_text(doc,[s["section_id"] for s in doc["sections"] if s["role"]=="abstract"])
        self.assertEqual(abstract,"Summary\n\nA full source abstract ends here.")
        self.assertTrue(any(s["origin"]=="inferred-dense-contents-page" for s in doc["sections"]))
        self.assertCountEqual([lid for b in doc["blocks"] for lid in b["source_line_ids"]],
                              [x["line_id"] for p in pages for x in p["lines"]])
        self.assertTrue(any(d["code"]=="contents_page_boundary_review" for d in doc["defects"]))

    def test_dotted_list_on_mixed_author_page_is_not_whole_page_contents(self):
        pages=[{"page":1,"width":600,"height":800,"comparison":{"status":"agreement"},
                "lines":[line("Summary",bold=True),
                         line("This complete author paragraph contains more than twenty words and must remain in the abstract even when a dotted list is printed below it.",y=140,block=1),
                         *[line(f"A source chapter ............ {i}",y=170+i*20,block=2,idx=i) for i in range(9)]]}]
        doc=make_document({"paper_id":"synthetic"},pages,improved=True)
        self.assertFalse(any(s["role"]=="contents" for s in doc["sections"]))
        self.assertIn("complete author paragraph",section_text(doc,["s0002"]))

    def test_dash_leader_contents_never_becomes_real_author_chapters(self):
        ps=[{'page':1,'width':600,'height':800,'comparison':{'status':'agreement'},
             'lines':[line('CONTENTS',bold=True),
                line('1. Introduction---------------------3',y=130,bold=True,block=1),
                line('2. Assumptions---------------------4',y=150,bold=True,block=2),
                line('3. Model---------------------6',y=170,bold=True,block=3),
                line('3.1 Method',y=190,block=4)]},
            {'page':2,'width':600,'height':800,'comparison':{'status':'agreement'},
             'lines':[line('1. Introduction',page=2,bold=True),
                      line('The actual introduction author paragraph is retained.',page=2,y=140,block=1)]}]
        d=make_document({'paper_id':'synthetic'},ps,improved=True)
        intro=[s['section_id'] for s in d['sections'] if s['role']=='introduction']
        self.assertEqual(len(intro),1)
        self.assertEqual(section_text(d,intro),'1. Introduction\n\nThe actual introduction author paragraph is retained.')
        self.assertCountEqual([lid for b in d['blocks'] for lid in b['source_line_ids']],
                              [x['line_id'] for p in ps for x in p['lines']])
        self.assertFalse(any(s['role']=='assumptions' for s in d['sections']))

    def test_singular_reference_is_stored_but_excluded_from_author_reading(self):
        for title in ('8 Reference','Reference','10. References','参考文献','Bibliographies'):
            ls=[line(title,page=4,bold=True),
                line('A bibliography entry with its original source details.',page=4,y=140,block=1),
                line('Appendix I',page=4,y=200,bold=True,block=2),
                line('The author appendix prose must remain in the reading.',page=4,y=230,block=3)]
            d=make_document({'paper_id':'synthetic'},[{'page':4,'width':600,'height':800,
                'lines':ls,'comparison':{'status':'agreement'}}],improved=True)
            text='\n'.join(b['text'] for b in all_author_blocks(d))
            self.assertNotIn('bibliography entry',text,title)
            self.assertIn('author appendix prose',text,title)
            self.assertTrue(any(b['kind']=='references' and 'bibliography entry' in b['text'] for b in d['blocks']))
            self.assertTrue(all(s['boundary_status']=='pending' for s in d['sections']))

    def test_breaking_down_problem_is_a_candidate_analysis_not_a_task_number(self):
        self.assertEqual(title_role('2. Breaking Down the Problem',3),'problem_analysis')
        self.assertEqual(title_role('Breaking Down the Problem',3),'problem_analysis')
        self.assertEqual(title_role('2. Breaking Down the Model',3),'model')

    def test_split_page_number_leaders_keep_all_toc_entries_out_of_body(self):
        for leader in ('.............','. . . . . . .','-------------','· · · · · · ·'):
            ls=[line('Contents',bold=True)]
            for i,title in enumerate(('1 Introduction','2 Assumptions','3 Model'),1):
                ls += [line(title,page=1,y=120+i*40,bold=True,block=i,idx=0),
                       line(leader,page=1,y=120+i*40,block=i,idx=1),
                       line(str(i+2),page=1,y=120+i*40,x=520,width=20,block=i,idx=2)]
            ps=[{'page':1,'width':600,'height':800,'lines':ls,'comparison':{'status':'agreement'}},
                {'page':2,'width':600,'height':800,'comparison':{'status':'agreement'},
                 'lines':[line('1 Introduction',page=2,bold=True),
                          line('The actual author introduction paragraph stays readable.',page=2,y=140,block=1)]}]
            d=make_document({'paper_id':'synthetic'},ps,improved=True)
            intro=[s['section_id'] for s in d['sections'] if s['role']=='introduction']
            self.assertEqual(len(intro),1,leader)
            self.assertIn('actual author introduction',section_text(d,intro),leader)
            self.assertFalse(any(s['role']=='assumptions' for s in d['sections']),leader)
            self.assertFalse(any(b['source_pages']==[1] for b in all_author_blocks(d)),leader)
            self.assertCountEqual([lid for b in d['blocks'] for lid in b['source_line_ids']],
                                  [l['line_id'] for p in ps for l in p['lines']])

    def test_reference_frame_is_not_a_bibliography_section(self):
        self.assertEqual(title_role('4 Reference Frame',7),'other')
        self.assertEqual(title_role('Reference Coordinate System',7),'other')
        self.assertEqual(title_role('10 Reference..',20),'references')

    def test_source_printed_plural_notation_and_addressed_letter_roles(self):
        self.assertEqual(title_role('4. Nomenclatures',5),'notation')
        self.assertEqual(title_role('11. A Letter to the Science Journal Editor',38),'memo')

    def test_bare_roman_heading_uses_the_same_number_prefix_as_detection(self):
        self.assertEqual(title_role('X References',10),'references')
        self.assertEqual(title_role('XII Bibliography',20),'references')
        self.assertEqual(title_role('C Appendix: Supplementary images',29),'appendix')
        self.assertEqual(title_role('IV.1 Reference Frame',7),'other')
        self.assertEqual(title_role('Reference Coordinate System',7),'other')

    def test_plain_font_colon_appendix_starts_after_bibliography_without_losing_prose(self):
        ls=[line('X References',page=4,bold=True),
            line('A bibliography entry must stay outside author imitation.',page=4,y=140,block=1),
            line('Appendix A: Additional author explanation',page=4,y=200,block=2),
            line('The full appendix author paragraph must still be selected.',page=4,y=240,block=3),
            line('Appendix A provides the supporting details for this result.',page=4,y=280,block=4)]
        d=make_document({'paper_id':'synthetic'},[{'page':4,'width':600,'height':800,
            'lines':ls,'comparison':{'status':'agreement'}}],improved=True)
        text='\n'.join(b['text'] for b in all_author_blocks(d))
        self.assertNotIn('bibliography entry',text)
        self.assertIn('full appendix author paragraph',text)
        self.assertTrue(any(s['role']=='appendix' for s in d['sections']))
        self.assertFalse(is_heading(ls[-1],11))
        self.assertFalse(is_heading(line('Appendix A: We have more data.',page=4),11))
        self.assertCountEqual([lid for b in d['blocks'] for lid in b['source_line_ids']],
                              [l['line_id'] for l in ls])
        self.assertTrue(all(s['boundary_status']=='pending' for s in d['sections']))

    def test_bold_wrapped_summary_sentences_are_not_new_section_headings(self):
        examples=["then conduct sensitivity analysis. The results indicate smaller bathtub with less surface",
                  "Afterwards, we performed sensitivity analysis of the model, analyzing its robustness to",
                  "The results reveal a fundamental correlation between cybersecurity effectiveness and the",
                  "2028 Olympic Medal Predictions Based on Random",
                  "40 miles, 12 repeaters are enough to accommodate 1000 simultaneous users. We",
                  "10 medals annually, and 77.8% for countries winning fewer than 10 medals annually. Addi-",
                  "Keywords: Recommendation System, Regression, PCA, Association Rule Learning",
                  "Results and Sensitivity Analysis：(i)The accuracy of the machine learning"]
        for text in examples:
            self.assertFalse(is_heading(line(text,bold=True),11),text)
        for text in ("3.2 Results and Discussion","Ocean wave model","Sensitivity Analysis","2.1 Model Development",
                     "5.2.2 Where is the Sweet Spot?","6-a. Facts and Assumptions","I.1 Introduction to Problem",
                     "2 Symbols, Hypothesis and Explanations","2-D Model","7.1General algorithm"):
            self.assertTrue(is_heading(line(text,bold=True,page=2),11),text)
        self.assertTrue(is_heading(line("2014 Mathematical Contest in Modeling (MCM) Summary Sheet",bold=True),11))

    def test_large_paper_title_with_result_keyword_cannot_steal_abstract(self):
        ls=[line("Summary Sheet",bold=True),
            line("Uncover the Hidden Secrets in Wordle Results",size=18,bold=True,y=140,block=1),
            line("The whole author abstract follows this paper title.",y=180,block=2)]
        doc=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                          "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        self.assertFalse(any(s["role"]=="results" for s in doc["sections"]))
        self.assertEqual(doc["blocks"][1]["kind"],"title")
        self.assertIn("whole author abstract",section_text(doc,["s0002"]))

    def test_structured_summary_sheet_headings_remain_inside_abstract(self):
        ls=[line("2014 Mathematical Contest in Modeling (MCM) Summary Sheet",bold=True),
            line("A complete problem and method paragraph.",y=140,block=1),
            line("Results",bold=True,y=180,block=2),
            line("A complete results paragraph with its qualification.",y=210,block=3),
            line("Strengths and Weaknesses Discussion：",bold=True,y=250,block=4),
            line("A complete limitations paragraph remains in the summary.",y=280,block=5),
            line("1 Introduction",bold=True,y=320,block=6),
            line("An actual body paragraph must not join the summary.",y=360,block=7)]
        d=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                        "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        abstract=next(s for s in d["sections"] if s["origin"]=="printed-heading" and s["role"]=="abstract")
        children=[s for s in d["sections"] if s["parent_id"]==abstract["section_id"]]
        self.assertEqual([s["role"] for s in children],["results","strengths_weaknesses"])
        text=section_text(d,[abstract["section_id"]])
        self.assertIn("results paragraph",text);self.assertIn("limitations paragraph",text)
        self.assertNotIn("actual body paragraph",text)
        self.assertTrue(all(s["boundary_status"]=="pending" for s in children))

    def test_plain_abstract_does_not_absorb_following_same_page_model(self):
        ls=[line("Abstract",bold=True),line("A short abstract ends here.",y=140,block=1),
            line("Ocean wave model",size=18,y=180,block=2),
            line("The separate model section follows the abstract.",y=220,block=3)]
        d=make_document({"paper_id":"synthetic"},[{"page":2,"width":600,"height":800,
                        "lines":[dict(x,page=2) for x in ls],"comparison":{"status":"agreement"}}],improved=True)
        self.assertEqual(next(s for s in d["sections"] if s["role"]=="model")["parent_id"],None)
        text=section_text(d,[s["section_id"] for s in d["sections"] if s["role"]=="abstract"])
        self.assertNotIn("separate model section",text)

    def test_opening_metadata_preserved_but_not_returned_as_abstract(self):
        texts = ["Group # 11199", "2/14/2011", "Summary", "An entire author paragraph stays here.", "February 22, 2010"]
        ls = [line(t, y=100+i*30, block=i, bold=t == "Summary") for i,t in enumerate(texts)]
        doc = make_document({"paper_id": "synthetic"}, [{"page": 1, "width": 600, "height": 800,
                            "lines": ls, "comparison": {"status": "agreement"}}], improved=True)
        abstract = section_text(doc, [s["section_id"] for s in doc["sections"] if s["role"] == "abstract"])
        self.assertNotIn("Group #", abstract); self.assertNotIn("2/14/2011", abstract)
        self.assertIn("An entire author paragraph", abstract)
        self.assertIn("February 22, 2010", abstract)  # No date stripping after author prose starts.
        self.assertEqual(doc["blocks"][0]["text"], "Group # 11199")
        self.assertEqual(doc["blocks"][0]["kind"], "front_matter")

    def test_competition_form_fields_not_author_language(self):
        texts = ["For office use only", "T1 ________________", "Problem Chosen",
                 "2010 Mathematical Contest in Modeling (MCM) Summary Sheet",
                 "(Attach a copy of this page to each copy of your solution paper.)",
                 "The full author paragraph begins here and is preserved."]
        ls = [line(t,y=100+i*30,block=i) for i,t in enumerate(texts)]
        doc = make_document({"paper_id": "synthetic"}, [{"page":1,"width":600,"height":800,
                            "lines":ls,"comparison":{"status":"agreement"}}], improved=True)
        abstract = section_text(doc,[s["section_id"] for s in doc["sections"] if s["role"] == "abstract"])
        self.assertEqual(abstract, texts[-1])

    def test_form_instructions_cannot_create_results_sections(self):
        texts=["2015 Mathematical Contest in Modeling (MCM) Summary Sheet",
               "(Attach a copy of this page to your solution paper.)",
               "Type a summary of your results on this page. Do not include",
               "the name of your school, advisor, or team members on this page.",
               "A full author summary paragraph follows the printed instructions."]
        ls=[line(t,y=100+i*30,block=i,bold=i<3) for i,t in enumerate(texts)]
        doc=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                          "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        text=section_text(doc,[s["section_id"] for s in doc["sections"] if s["role"]=="abstract"])
        self.assertEqual(text,texts[-1])
        self.assertFalse(any(s["role"]=="results" for s in doc["sections"]))

    def test_clustered_form_fragments_and_combined_contest_name_are_not_author_text(self):
        texts=["For office use only","T1 ________________","F1 ________________",
               "Team Control","Number","25142","Problem Chosen","A","2014",
               "Mathematical Contest in Modeling (MCM/ICM) Summary Sheet","Summary",
               "We compare all candidate rules under one common evaluation measure."]
        ls=[line(t,y=50+i*20,block=i,bold=i in (9,10)) for i,t in enumerate(texts)]
        d=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                       "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        t=section_text(d,[s["section_id"] for s in d["sections"] if s["role"]=="abstract"])
        self.assertEqual(t,"Summary\n\n"+texts[-1])
        owned=[lid for b in d["blocks"] for lid in b["source_line_ids"]]
        self.assertCountEqual(owned,[x["line_id"] for x in ls])

    def test_no_form_cluster_does_not_strip_year_or_number_author_paragraphs(self):
        ls=[line("Abstract",bold=True),line("2014",y=140,block=1),
            line("A",y=180,block=2),line("The year and category belong to this author text.",y=220,block=3)]
        d=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                       "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        t=section_text(d,[s["section_id"] for s in d["sections"] if s["role"]=="abstract"])
        self.assertIn("2014",t);self.assertIn("\n\nA\n\n",t)

    def test_form_cluster_does_not_strip_matching_author_tokens_after_body_starts(self):
        texts=["For office use only","T1 ________________","Problem Chosen",
               "Our original author paragraph has more than sixteen source words and explains why the experiment uses the following categories.",
               "2014","A"]
        ls=[line(t,y=50+i*30,block=i) for i,t in enumerate(texts)]
        d=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                       "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        t=section_text(d,[s["section_id"] for s in d["sections"] if s["role"]=="abstract"])
        self.assertIn(texts[3],t);self.assertIn("2014",t);self.assertTrue(t.endswith("A"))

    def test_icm_summary_banner_split_before_sheet_still_contains_full_summary(self):
        texts=["2015 Mathematical Contest in Modeling (ICM) Summary",
               "Sheet (Attach a copy of this page to your solution paper.)",
               "A whole abstract paragraph remains under the summary heading."]
        ls=[line(t,y=100+i*30,block=i,bold=i<2) for i,t in enumerate(texts)]
        doc=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                          "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        text=section_text(doc,[s["section_id"] for s in doc["sections"] if s["role"]=="abstract"])
        self.assertEqual(text,texts[-1])

    def test_short_real_abstract_is_not_a_sparse_title_cover(self):
        ls=[line("A Paper Title",size=20),line("Team # 12345",y=130,block=1),
            line("February 22, 2010",y=160,block=2),line("Abstract",y=190,block=3,bold=True),
            line("A short genuine abstract remains author prose.",y=220,block=4)]
        doc=make_document({"paper_id":"synthetic"},[{"page":1,"width":600,"height":800,
                          "lines":ls,"comparison":{"status":"agreement"}}],improved=True)
        text=section_text(doc,[s["section_id"] for s in doc["sections"] if s["role"]=="abstract"])
        self.assertIn("A short genuine abstract",text)

    def test_paper_title_before_second_printed_abstract_is_preserved_outside_prose(self):
        pages=[{"page":1,"width":600,"height":800,"comparison":{"status":"agreement"},
                "lines":[line("Summary",bold=True),line("The first printed summary is preserved.",y=150,block=1)]},
               {"page":2,"width":600,"height":800,"comparison":{"status":"agreement"},
                "lines":[line("The Design of a Useful Model",page=2,size=20,y=90),
                         line("Abstract",page=2,bold=True,y=140,block=1),
                         line("The second printed abstract is also preserved.",page=2,y=180,block=2)]}]
        d=make_document({"paper_id":"synthetic"},pages,improved=True)
        t=section_text(d,[s["section_id"] for s in d["sections"] if s["role"]=="abstract"])
        self.assertIn("first printed summary",t);self.assertIn("second printed abstract",t)
        self.assertNotIn("The Design",t)
        self.assertTrue(any(b["text"]=="The Design of a Useful Model" and b["kind"]=="title" for b in d["blocks"]))

    def test_split_number_heading_does_not_leak_into_previous_abstract(self):
        ps = [{"page":1,"width":600,"height":800,"comparison":{"status":"agreement"},
               "lines":[line("Abstract",bold=True),line("A complete author abstract ends here.",y=150,block=1)]},
              {"page":2,"width":600,"height":800,"comparison":{"status":"agreement"},
               "lines":[line("1",page=2,size=16,width=10),
                        line("Introduction",page=2,x=100,size=16,width=150,idx=1),
                        line("A full introduction paragraph follows here.",page=2,y=160,block=1)]}]
        doc = make_document({"paper_id":"synthetic"},ps,improved=True)
        abstract = section_text(doc,[s["section_id"] for s in doc["sections"] if s["role"] == "abstract"])
        self.assertEqual(abstract,"Abstract\n\nA complete author abstract ends here.")
        intro = next(s for s in doc["sections"] if s["role"] == "introduction")
        self.assertEqual(intro["title"],"1 Introduction")
        owned = [lid for b in doc["blocks"] for lid in b["source_line_ids"]]
        self.assertCountEqual(owned,[x["line_id"] for p in ps for x in p["lines"]])


class ExhaustiveReaderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def acknowledge_batch(self, cat, run, batch):
        observations = []
        for c in batch["chunks"]:
            observations.append({"paper_id": c["paper_id"], "observation": "Synthetic test observation, not a real-paper reading.",
                                 "block_ids": [s["block_id"] for s in c["source_blocks"]]})
        return acknowledge(cat, run, batch["completion_marker"], observations)

    def test_all_435_papers_selected_without_top_k(self):
        cat = fixture(self.root, count=435)
        self.assertEqual(len(cat.select("abstract")), 435)
        self.assertEqual(cat.select("abstract")[-1]["queue_position"], 435)

    def test_introduction_exhaustive_delivery_is_not_abstract_only(self):
        cat=fixture(self.root,count=9,role="introduction");run=self.root/"run"
        start(cat,"introduction",run,max_tokens=1800)
        seen=[]
        while not status(cat,run)["traversal_complete"]:
            batch=next_batch(cat,run)
            seen.extend(c["paper_id"] for c in batch["chunks"])
            self.acknowledge_batch(cat,run,batch)
        self.assertEqual(seen,[p["paper_id"] for p in cat.papers])
        self.assertTrue(status(cat,run)["full_read_acceptance"])

    def test_parent_child_multiple_matches_are_not_duplicated(self):
        cat = fixture(self.root, count=1)
        sel = cat.select("summary")[0]; text, spans = cat.text_and_spans(sel)
        self.assertEqual(text.count("Tail paragraph."), 1)
        self.assertEqual([s["block_id"] for s in spans], ["b1", "b2"])

    def test_strict_fails_closed_for_unverified(self):
        cat = fixture(self.root, verified=False)
        with self.assertRaisesRegex(ValueError, "Strict reading blocked"):
            start(cat, "abstract", self.root / "run")
        self.assertFalse((self.root / "run").exists())

    def test_full_long_sections_reconstruct_exactly_after_resume(self):
        cat = fixture(self.root, long=True); run = self.root / "run"
        start(cat, "abstract", run, max_tokens=3000)
        collected = {p["paper_id"]: "" for p in cat.papers}; count = 0
        while not status(cat, run)["traversal_complete"]:
            batch = next_batch(Catalog(self.root), run)
            self.assertLessEqual(len(wire(batch))+1, 3000)
            self.assertEqual(next_batch(cat, run), batch)
            for chunk in batch["chunks"]:
                self.assertEqual(chunk["start"], len(collected[chunk["paper_id"]]))
                collected[chunk["paper_id"]] += chunk["text"]
            self.acknowledge_batch(cat, run, batch); count += 1
        self.assertGreater(count, 3)
        for selected in cat.select("abstract"):
            self.assertEqual(collected[selected["paper_id"]], cat.text_and_spans(selected)[0])
        self.assertTrue(status(cat, run)["full_read_acceptance"])

    def test_delivery_is_not_processing(self):
        cat = fixture(self.root); run = self.root / "run"; start(cat, "abstract", run)
        next_batch(cat, run)
        self.assertEqual(status(cat, run)["fully_processed_present"], 0)
        self.assertTrue(status(cat, run)["pending_batch_delivered"])
        self.assertGreater(status(cat,run)["fully_delivered_present"],0)

    def test_status_rejects_mutated_pending_batch(self):
        cat=fixture(self.root);run=self.root/"run";start(cat,"abstract",run)
        next_batch(cat,run);path=run/"batches/000000.json"
        value=json.loads(path.read_text(encoding="utf-8"));value["chunks"][0]["text"]="changed"
        path.write_bytes(encoded(value))
        with self.assertRaisesRegex(ValueError,"Pending batch altered"):
            status(cat,run)

    def test_truncated_marker_and_missing_observations_rejected(self):
        cat = fixture(self.root); run = self.root / "run"; start(cat, "abstract", run)
        batch = next_batch(cat, run)
        with self.assertRaises(ValueError):
            acknowledge(cat, run, "bad", [])
        with self.assertRaises(ValueError):
            acknowledge(cat, run, batch["completion_marker"], [])

    def test_source_tampering_refused(self):
        cat = fixture(self.root); run = self.root / "run"; start(cat, "abstract", run)
        path = self.root / cat.papers[0]["document"]
        path.write_bytes(path.read_bytes() + b" ")
        with self.assertRaisesRegex(ValueError, "bytes changed"):
            next_batch(cat, run)

    def test_completed_status_rechecks_previously_processed_documents(self):
        cat = fixture(self.root, count=1); run = self.root / "run"
        start(cat, "abstract", run)
        self.acknowledge_batch(cat, run, next_batch(cat, run))
        self.assertTrue(status(cat, run)["full_read_acceptance"])
        path = self.root / cat.papers[0]["document"]
        path.write_bytes(path.read_bytes() + b" ")
        with self.assertRaisesRegex(ValueError, "bytes changed"):
            status(cat, run)

    def test_changed_corpus_rejects_old_cursor(self):
        cat = fixture(self.root); run = self.root / "run"; start(cat, "abstract", run)
        other = self.root / "other"; cat2 = fixture(other, count=2)
        with self.assertRaisesRegex(ValueError, "version changed"):
            next_batch(cat2, run)

    def test_preview_can_finish_delivery_but_never_acceptance(self):
        cat = fixture(self.root, count=1, verified=False); run = self.root / "run"
        start(cat, "abstract", run, allow_unverified=True)
        self.acknowledge_batch(cat, run, next_batch(cat, run))
        result = status(cat, run)
        self.assertTrue(result["traversal_complete"])
        self.assertFalse(result["full_read_acceptance"])

    def test_unknown_section_is_unresolved_not_verified_absence(self):
        cat = fixture(self.root)
        self.assertTrue(all(s["status"] == "unresolved" for s in cat.select("conclusion")))

    def test_exact_heading_and_explicit_type_year_filters(self):
        cat = fixture(self.root)
        self.assertEqual(len(cat.select("Summary", scope="A", year=2020, title=True)), 3)
        self.assertTrue(all(x["section_ids"] == ["s1"] for x in cat.select("Summary", title=True)))
        with self.assertRaisesRegex(ValueError, "empty"):
            cat.select("abstract", year=2019)

    def test_receipt_tampering_is_detected(self):
        cat = fixture(self.root); run = self.root / "run"; start(cat, "abstract", run, max_tokens=1500)
        batch = next_batch(cat, run); self.acknowledge_batch(cat, run, batch)
        path = run / "receipts/000000.json"
        receipt = json.loads(path.read_text(encoding="utf-8")); receipt["to_cursor"]["paper_index"] = 999
        path.write_text(json.dumps(receipt), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "does not describe"):
            status(cat, run)

    def test_reading_observation_must_cite_delivered_blocks(self):
        cat = fixture(self.root); run = self.root / "run"; start(cat, "abstract", run)
        batch = next_batch(cat, run)
        observations = [{"paper_id": c["paper_id"], "block_ids": ["not-delivered"], "observation": "Not a valid source reference."}
                        for c in batch["chunks"]]
        with self.assertRaisesRegex(ValueError, "actually delivered"):
            acknowledge(cat, run, batch["completion_marker"], observations)

    def test_status_flag_alone_is_not_source_verification(self):
        cat = fixture(self.root, count=1, verified=False)
        doc = cat.document(cat.papers[0]["paper_id"])
        for s in doc["sections"]:
            s["boundary_status"] = "verified"
            self.assertFalse(Catalog.review_valid(doc, s))

    def test_review_paragraph_ids_must_match_selected_source_blocks(self):
        cat=fixture(self.root,count=1);doc=cat.document(cat.papers[0]["paper_id"])
        s=doc["sections"][0];s["review"]["paragraph_blocks"]=["wrong-old-block-id"]
        self.assertFalse(Catalog.review_valid(doc,s))

    def test_absence_requires_whole_source_review_not_missing_heading(self):
        cat = fixture(self.root, count=1)
        doc = cat.document(cat.papers[0]["paper_id"])
        doc["verified_absent_roles"] = ["conclusion"]
        self.assertFalse(Catalog.absence_valid(doc, "conclusion"))
        doc["absence_reviews"] = {"conclusion": {"reviewer": "synthetic-test-only",
            "schema":"source-absence-review-v1","paper_id":doc["paper_id"],"role":"conclusion",
            "full_native_prose_read":True,"physical_page_heading_layout_checked":True,
            "evidence":[{"path":"synthetic-proof.txt","sha256":"c"*64,"description":"Synthetic source proof."}],
            "source_sha256": doc["source_sha256"], "raw_pages_sha256": doc["raw_pages_sha256"],
            "checked_pages": [1, 2], "page_count": 2, "reason": "Synthetic absence fixture."}}
        self.assertTrue(Catalog.absence_valid(doc, "conclusion"))

    def test_whole_source_absence_evidence_tampering_blocks_delivery(self):
        cat=fixture(self.root,count=1);doc=cat.document(cat.papers[0]["paper_id"])
        proof=self.root/"proof.txt";proof.write_bytes(b"Synthetic absence evidence; no real-paper review.")
        review={"schema":"source-absence-review-v1","paper_id":doc["paper_id"],"role":"conclusion",
                "reviewer":"synthetic-test-only","reason":"Synthetic whole-source absence test.",
                "source_sha256":doc["source_sha256"],"raw_pages_sha256":doc["raw_pages_sha256"],
                "checked_pages":[1,2],"page_count":2,"full_native_prose_read":True,
                "physical_page_heading_layout_checked":True,
                "evidence":[{"path":"proof.txt","sha256":file_hash(proof),"description":"Synthetic proof."}],
                "evidence_files":{"proof.txt":file_hash(proof)}}
        apply_absence_reviews(doc,[review])
        path=self.root/cat.papers[0]["document"];path.write_bytes(encoded(doc))
        catalog=cat.catalog;catalog["papers"][0]["document_sha256"]=file_hash(path)
        catalog.pop("dataset_id");catalog["dataset_id"]=digest(encoded(catalog))
        (self.root/"catalog.json").write_bytes(encoded(catalog));cat=Catalog(self.root)
        self.assertEqual(cat.select("conclusion")[0]["status"],"verified-absent")
        run=self.root/"absence-run";start(cat,"conclusion",run);next_batch(cat,run)
        proof.write_bytes(b"Changed proof.")
        with self.assertRaisesRegex(ValueError,"evidence missing or changed"):
            next_batch(cat,run)
        with self.assertRaisesRegex(ValueError,"evidence missing or changed"):
            cat.select("conclusion")

    def test_bad_scope_and_budget_rejected(self):
        cat = fixture(self.root)
        with self.assertRaises(ValueError):
            cat.select("abstract", "AB")
        with self.assertRaises(ValueError):
            start(cat, "abstract", self.root / "run", max_tokens=9000)

    def test_create_only_session(self):
        cat = fixture(self.root); run = self.root / "run"; start(cat, "abstract", run)
        before = file_hash(run / "session.json")
        with self.assertRaises(ValueError):
            start(cat, "abstract", run)
        self.assertEqual(file_hash(run / "session.json"), before)

    def test_missing_database_has_no_legacy_fallback(self):
        with self.assertRaisesRegex(ValueError, "No fallback"):
            Catalog(self.root)

    def test_unicode_wire_marker_is_last_and_byte_bound(self):
        value = {"chunks": [{"text": "完整摘要，α与🙂。"}], "completion_marker": "end"}
        self.assertTrue(wire(value).endswith(b'"completion_marker":"end"}'))
        self.assertEqual(json.loads(wire(value)), value)


class AllChapterReaderTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        self.cat=fixture(self.root,count=1);self.pid=self.cat.papers[0]["paper_id"]
        doc=self.cat.document(self.pid)
        specs=[("s3","1 Problem Restatement","introduction",None),
               ("s4","2 Problem Analysis","other",None),
               ("s5","3 Assumptions","assumptions",None),
               ("s6","4 Notation","notation",None),
               ("s7","5 Model construction","model",None),
               ("s8","6 Model for Problem1","model",None),
               ("s9","6.1 Solution to Question1","results","s8"),
               ("refs","References","references","s8"),
               ("s10","7 Question II","model",None),
               ("s11","8 Sensitivity","sensitivity",None),
               ("s12","9 Validation","validation",None),
               ("s13","10 Improvements","other",None),
               ("s14","Appendix A","appendix",None),
               ("ai","AI Use Report","ai_disclosure","s14"),
               ("unknown","Unusual author chapter","other",None)]
        for sid,title,role,parent in specs:
            doc["sections"].append({"section_id":sid,"title":title,"role":role,"parent_id":parent,"boundary_status":"verified"})
            text=("The entire long author paragraph continues with its evidence and limitations. "*90 if sid=="s7" else f"Complete source text of {sid}.")
            doc["blocks"].append({"block_id":"block-"+sid,"section_id":sid,"kind":"prose","text":text,"source_pages":[2],"issues":[]})
        for s in doc["sections"]:
            s["review"]={"reviewer":"synthetic-test-only","source_sha256":doc["source_sha256"],
                "raw_pages_sha256":doc["raw_pages_sha256"],"text_sha256":digest(section_text(doc,[s["section_id"]]).encode()),
                "section_boundaries_checked":True,"paragraph_boundaries_checked":True,"checked_pages":[1,2]}
        path=self.root/self.cat.papers[0]["document"];path.write_bytes(encoded(doc))
        cat=self.cat.catalog;cat["papers"][0]["document_sha256"]=file_hash(path)
        cat.pop("dataset_id");cat["dataset_id"]=digest(encoded(cat));(self.root/"catalog.json").write_bytes(encoded(cat))
        self.cat=Catalog(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def ack(self,run,batch):
        obs=[{"paper_id":c["paper_id"],"block_ids":[s["block_id"] for s in c["source_blocks"]],
              "observation":"Synthetic fixture processing only; no real-paper reading."} for c in batch["chunks"]]
        acknowledge(self.cat,run,batch["completion_marker"],obs)

    def test_explicit_task_sections_all_returned_without_chapter_number_guessing(self):
        one=self.cat.select("task_1")[0];text,_=self.cat.text_and_spans(one)
        self.assertIn("text of s8",text);self.assertIn("text of s9",text)
        self.assertEqual(text.count("text of s9"),1)
        self.assertNotIn("long author paragraph",text)
        two=self.cat.select("task_2")[0];self.assertEqual(two["section_ids"],["s10"])
        self.assertEqual(self.cat.select("task_3")[0]["status"],"unresolved")
        self.assertEqual(task_numbers("3 Model construction"),set())
        self.assertEqual(task_numbers("Solution to Question Three"),{3})
        self.assertEqual(self.cat.select("问题重述")[0]["section_ids"],["s3"])
        self.assertEqual(self.cat.select("问题分析")[0]["section_ids"],["s4"])
        self.assertEqual(set(self.cat.select("敏感性与检验")[0]["section_ids"]),{"s11","s12"})

    def test_all_author_text_includes_unknown_appendix_but_excludes_nested_non_author_roles(self):
        item=self.cat.select("all_author_text")[0];text,_=self.cat.text_and_spans(item)
        self.assertIn("text of unknown",text);self.assertIn("text of s14",text)
        self.assertNotIn("text of refs",text);self.assertNotIn("text of ai",text)
        self.assertIn("text of s6",text)
        self.assertEqual(text.count("text of s9"),1)

    def test_full_chapter_coverage_needs_acknowledged_complete_block_intervals(self):
        abstract=self.root/"abstract";start(self.cat,"abstract",abstract)
        while not status(self.cat,abstract)["traversal_complete"]:
            self.ack(abstract,next_batch(self.cat,abstract))
        first=author_text_coverage(self.cat,[abstract]);self.assertFalse(first["all_chapters_read_acceptance"])
        self.assertEqual(first["all_author_text_processed_papers"],0)
        body=self.root/"all";start(self.cat,"all_author_text",body,max_tokens=1800)
        pending=next_batch(self.cat,body)
        self.assertEqual(author_text_coverage(self.cat,[abstract,body])["fully_processed_unique_blocks"],first["fully_processed_unique_blocks"])
        self.ack(body,pending)
        self.assertFalse(author_text_coverage(self.cat,[body])["all_chapters_read_acceptance"])
        while not status(self.cat,body)["traversal_complete"]:
            self.ack(body,next_batch(self.cat,body))
        result=author_text_coverage(self.cat,[abstract,body,body])
        self.assertTrue(result["all_chapters_read_acceptance"])
        self.assertEqual(result["fully_processed_unique_blocks"],result["required_unique_blocks"])
        self.assertEqual(result["fully_processed_candidate_sections"],result["required_candidate_sections"])
        other=self.root/"different";newcat=fixture(other,count=2)
        with self.assertRaisesRegex(ValueError,"version changed"):
            author_text_coverage(newcat,[body])

    def test_task_absence_cannot_contradict_explicit_task_heading(self):
        doc=self.cat.document(self.pid)
        r={"schema":"source-absence-review-v1","paper_id":self.pid,"role":"task_1",
           "source_sha256":doc["source_sha256"],"raw_pages_sha256":doc["raw_pages_sha256"],
           "reviewer":"synthetic-test-only","reason":"Synthetic absence fixture.","page_count":2,
           "checked_pages":[1,2],"full_native_prose_read":True,"physical_page_heading_layout_checked":True,
           "evidence":[{"path":"proof","sha256":"c"*64,"description":"Synthetic source proof."}]}
        doc["verified_absent_roles"]=["task_1"];doc["absence_reviews"]={"task_1":r}
        self.assertFalse(Catalog.absence_valid(doc,"task_1"))
        r["role"]="task_4";doc["verified_absent_roles"]=["task_4"];doc["absence_reviews"]={"task_4":r}
        self.assertTrue(Catalog.absence_valid(doc,"task_4"))

    def test_final_packaging_rejects_abstract_only_even_if_source_audit_passes(self):
        run=self.root/"abstract";start(self.cat,"abstract",run)
        while not status(self.cat,run)["traversal_complete"]:
            self.ack(run,next_batch(self.cat,run))
        with tempfile.TemporaryDirectory() as release_parent:
            release=Path(release_parent)/"release"
            with patch("package_text_corpus_skill.validate",return_value={"structural_integrity_pass":True,"source_completeness_accepted":True}):
                with self.assertRaisesRegex(ValueError,"every author chapter"):
                    package_corpus_skill(self.root/"base",self.root,release,reading_run=run)
            self.assertFalse(release.exists())


class SourceLayoutAndAbsenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        self.proof=self.root/"proof.txt";self.proof.write_bytes(b"Synthetic layout evidence only.")
        self.meta={"paper_id":"synthetic","source_sha256":"a"*64,"raw_pages_sha256":"b"*64,"page_count":1}
        self.lines=[line("Author title",block=1,size=18),
                    line("The main sentence continues",x=200,y=140,block=2),
                    line("without a sidebar inserted in the middle.",x=200,y=160,block=3),
                    line("KEY CONCEPT: separate author callout",x=40,y=150,width=150,block=4)]
        self.pages=[{"page":1,"width":600,"height":800,"lines":self.lines,"comparison":{"status":"agreement"}}]
        groups=[]
        for name,kind,ids in (("title","title",[0]),("main","prose",[1,2]),("sidebar","author_callout",[3])):
            groups.append({"group_id":name,"kind":kind,"source_line_ids":[self.lines[i]["line_id"] for i in ids],
                           "text_sha256":digest(" ".join(self.lines[i]["text"] for i in ids).encode()),"reason":"Synthetic lane."})
        self.review={"schema":"source-text-layout-review-v1",**self.meta,"reviewer":"synthetic-test-only",
                     "reason":"Synthetic paragraph/side-lane fixture.","paragraph_boundaries_checked":True,
                     "reading_lanes_checked":True,"pages":[{"page":1,"groups":groups}],
                     "evidence":[{"path":"proof.txt","sha256":file_hash(self.proof),"description":"Synthetic evidence."}],
                     "evidence_files":{"proof.txt":file_hash(self.proof)}}

    def tearDown(self):
        self.tmp.cleanup()

    def test_reviewed_lanes_retain_sidebar_outside_main_sentence(self):
        ps=copy.deepcopy(self.pages);applied=apply_layout_reviews(self.meta,ps,[self.review])
        d=make_document(self.meta,ps,improved=True);d["layout_reviews"]=applied
        validate_layout_reviews(d,self.pages);validate_review_bundle(self.root,self.review)
        self.assertEqual([b["kind"] for b in d["blocks"]],["title","prose","author_callout"])
        self.assertEqual(d["blocks"][1]["text"],"The main sentence continues without a sidebar inserted in the middle.")
        self.assertIn("separate author callout",section_text(d,["s0001"]))
        d["blocks"][1],d["blocks"][2]=d["blocks"][2],d["blocks"][1]
        with self.assertRaisesRegex(ValueError,"ordering/classification"):
            validate_layout_reviews(d,self.pages)

    def test_layout_rejects_missing_duplicated_or_changed_native_lines(self):
        for mutate in ("missing","duplicate","text","source"):
            r=copy.deepcopy(self.review)
            if mutate=="missing":r["pages"][0]["groups"].pop()
            if mutate=="duplicate":r["pages"][0]["groups"].append(copy.deepcopy(r["pages"][0]["groups"][-1]))
            if mutate=="text":r["pages"][0]["groups"][0]["text_sha256"]="f"*64
            if mutate=="source":r["source_sha256"]="f"*64
            with self.assertRaises(ValueError):
                apply_layout_reviews(self.meta,copy.deepcopy(self.pages),[r])

    def test_reviewed_heading_keeps_section_scope_and_nonprose_locations(self):
        ps=copy.deepcopy(self.pages);r=copy.deepcopy(self.review)
        ps[0]['lines'][0]['text']='4 Model'
        first=r['pages'][0]['groups'][0]
        first.update(kind='heading',text_sha256=digest(b'4 Model'),
                     opens_section={'role':'model','level':1})
        r['pages'][0]['groups'][2]['kind']='source_object'
        applied=apply_layout_reviews(self.meta,ps,[r]);d=make_document(self.meta,ps,improved=True)
        d['layout_reviews']=applied;validate_layout_reviews(d,ps)
        model=next(s for s in d['sections'] if s['role']=='model')
        self.assertEqual(model['boundary_status'],'pending')
        text=section_text(d,[model['section_id']])
        self.assertIn('without a sidebar inserted in the middle.',text)
        self.assertNotIn('KEY CONCEPT',text)
        self.assertEqual(d['blocks'][-1]['kind'],'source_object')
        self.assertEqual(d['blocks'][-1]['source_line_ids'],[ps[0]['lines'][-1]['line_id']])
        model['role']='abstract'
        with self.assertRaisesRegex(ValueError,'opening ownership'):
            validate_layout_reviews(d,ps)

    def test_section_opening_cannot_be_attached_to_nonheading_or_wrong_role(self):
        for kind,opening in (('prose',{'role':'other','level':1}),
                             ('heading',{'role':'abstract','level':1}),
                             ('heading',{'role':'other','level':True})):
            r=copy.deepcopy(self.review)
            r['pages'][0]['groups'][0].update(kind=kind,opens_section=opening)
            with self.assertRaisesRegex(ValueError,'section opening invalid'):
                apply_layout_reviews(self.meta,copy.deepcopy(self.pages),[r])

    def test_evidence_bundle_preserves_nested_relative_proof_paths(self):
        bundle=self.root/"bundle";bundle.mkdir();nested=bundle/"nested";nested.mkdir()
        (nested/"image.jpg").write_bytes(b"Synthetic local image; not delivered to any agent.")
        manifest=bundle/"manifest.json";json_new(manifest,{"path":"nested/image.jpg"})
        r=copy.deepcopy(self.review)
        r["evidence"]=[{"path":str(manifest),"sha256":file_hash(manifest),"bundle_root":str(bundle),"description":"Synthetic bundle."}]
        path=self.root/"review.json";json_new(path,r)
        reviews,copies=prepare_review_bundles([path],identity_fields=("paper_id",),application_status="synthetic-only")
        output=self.root/"output"
        for rel,(source,sha) in copies.items():
            target=output/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(source.read_bytes())
        validate_review_bundle(output,reviews[0])
        self.assertTrue((output/Path(reviews[0]["evidence"][0]["path"]).parent/"nested/image.jpg").is_file())
        next(p for p in output.rglob("image.jpg")).write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError,"missing, escaped or changed"):
            validate_review_bundle(output,reviews[0])

    def test_absence_does_not_override_nonempty_role_or_partial_page_review(self):
        d=make_document(self.meta,self.pages,improved=True)
        review={"schema":"source-absence-review-v1",**self.meta,"role":"abstract","reviewer":"synthetic-test-only",
                "reason":"Synthetic absence contradiction test.","checked_pages":[1],"full_native_prose_read":True,
                "physical_page_heading_layout_checked":True,"evidence":self.review["evidence"],
                "evidence_files":self.review["evidence_files"]}
        with self.assertRaisesRegex(ValueError,"contradictory"):
            apply_absence_reviews(d,[review])
        review["role"]="conclusion";review["checked_pages"]=[]
        with self.assertRaisesRegex(ValueError,"Incomplete"):
            apply_absence_reviews(d,[review])


class LiteralSourceRepairTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name)
        self.proof = self.root / "evidence.txt"; self.proof.write_bytes(b"synthetic source proof")
        self.original = "The preference \uf06c is printed here."
        self.doc = {"paper_id": "synthetic", "source_sha256": "a"*64, "raw_pages_sha256": "b"*64,
                    "blocks": [{"block_id": "b1", "kind": "prose", "source_pages": [1],
                                "text": self.original, "issues": ["private_use_glyph_review"]}],
                    "defects": [{"code": "private_use_glyph_review", "block_id": "b1", "page": 1}]}
        self.review = {"paper_id": "synthetic", "source_sha256": "a"*64, "raw_pages_sha256": "b"*64,
                       "reviewer": "synthetic-test-only", "reason": "Literal glyph, not formula verification.",
                       "checked_pages": [1], "evidence": [{"path": "evidence.txt", "sha256": file_hash(self.proof),
                       "description": "Synthetic literal character proof."}], "operations": [{
                           "block_id": "b1", "operation": "literal_replace", "old": "\uf06c", "new": "λ", "count": 1,
                           "before_text_sha256": digest(self.original.encode()),
                           "after_text_sha256": digest(self.original.replace("\uf06c", "λ").encode()),
                           "reason": "Transcribe visible literal glyph."}]}

    def tearDown(self):
        self.tmp.cleanup()

    def test_literal_repair_replays_and_resolves_only_repaired_glyph(self):
        apply_text_repairs(self.doc, [self.review])
        block = self.doc["blocks"][0]
        self.assertEqual(replay_block(self.doc, block, self.original), block["text"])
        self.assertEqual(block["issues"], [])
        self.assertEqual(self.doc["defects"][0]["status"], "resolved")
        validate_evidence(self.root, self.doc)
        with self.assertRaisesRegex(ValueError, "already applied"):
            apply_text_repairs(self.doc, [self.review])

    def test_wrong_preimage_count_and_checked_pages_fail_closed(self):
        for key, value in (("count", 2), ("before_text_sha256", "f"*64)):
            review = copy.deepcopy(self.review); review["operations"][0][key] = value
            with self.assertRaises(ValueError):
                apply_text_repairs(copy.deepcopy(self.doc), [review])
        self.review["checked_pages"] = [2]
        with self.assertRaisesRegex(ValueError, "coverage"):
            apply_text_repairs(self.doc, [self.review])

    def test_unlogged_and_modified_repair_evidence_rejected(self):
        apply_text_repairs(self.doc, [self.review])
        self.doc["blocks"][0]["text_repair_review_ids"] = []
        with self.assertRaisesRegex(ValueError, "log/classification"):
            replay_block(self.doc, self.doc["blocks"][0], self.original)
        self.proof.write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "missing or modified"):
            validate_evidence(self.root, self.doc)

    def test_front_matter_classification_preserves_source_text(self):
        op = self.review["operations"][0]
        op.update(operation="classify", from_kind="prose", to_kind="front_matter",
                  after_text_sha256=op["before_text_sha256"])
        apply_text_repairs(self.doc, [self.review])
        block = self.doc["blocks"][0]
        self.assertEqual(block["kind"], "front_matter")
        self.assertEqual(replay_block(self.doc, block, self.original), self.original)

    def test_exact_cross_engine_equality_only_ignores_ligatures_and_whitespace(self):
        self.assertEqual(independent_key("deﬁne a ﬂight"), independent_key("define\n a flight"))
        self.assertNotEqual(independent_key("②"), independent_key("2"))
        doc = {"defects": [{"code": "cross_engine_review", "page": 1},
                           {"code": "cross_engine_review", "page": 2},
                           {"code": "section_boundary_pending", "section_id": "s1"}]}
        pages = [{"page": 1, "ocr_status": "not-requested", "lines": [{"text": "deﬁne a ﬂight"}]},
                 {"page": 2, "lines": [{"text": "missing prose remains"}]}]
        resolve_exact_comparisons(doc, pages, b"define a flight\fmissing\f")
        self.assertEqual(doc["defects"][0]["status"], "resolved")
        self.assertNotIn("status", doc["defects"][1])
        self.assertNotIn("status", doc["defects"][2])
        validate_exact_comparisons(doc, pages, b"define a flight\fmissing\f")
        with self.assertRaisesRegex(ValueError, "proof differs"):
            validate_exact_comparisons(doc, pages, b"lost source word\fmissing\f")


class AbstractEnvelopeAuditTests(unittest.TestCase):
    def test_printed_form_contamination_is_diagnosed_and_preserved(self):
        doc={"sections":[{"section_id":"s1","role":"abstract","parent_id":None}],"blocks":[
             {"block_id":"a","section_id":"s1","kind":"prose","source_pages":[1],"text":"For office use only T1 ________________"},
             {"block_id":"b","section_id":"s1","kind":"prose","source_pages":[1],"text":"The actual author paragraph."}]}
        before=copy.deepcopy(doc);codes={x["code"] for x in abstract_findings(doc)}
        self.assertIn("abstract_possible_form_contamination",codes);self.assertEqual(doc,before)

    def test_multipage_fragmented_letter_is_diagnosed_without_deleting_text(self):
        blocks=[{"block_id":"b0","section_id":"s1","kind":"prose","source_pages":[1],
                 "text":"The whole actual abstract ends on this page."}]
        blocks.append({"block_id":"letter","section_id":"s1","kind":"prose","source_pages":[2],"text":"Dear editor,"})
        for i in range(6):
            blocks.append({"block_id":f"b{i+1}","section_id":"s1","kind":"prose","source_pages":[2],
                           "text":"continued native wrap without a real paragraph ending"})
        doc={"sections":[{"section_id":"s1","role":"abstract","parent_id":None}],"blocks":blocks}
        before=copy.deepcopy(doc);findings=abstract_findings(doc);codes={x["code"] for x in findings}
        self.assertTrue({"abstract_multiple_page_scope_review","abstract_possible_line_fragmentation",
                         "abstract_possible_letter_contamination"}<=codes)
        self.assertEqual(doc,before)

    def test_legitimate_long_abstract_is_only_a_scope_review_not_rejected(self):
        doc={"sections":[{"section_id":"s1","role":"abstract","parent_id":None}],"blocks":[
             {"block_id":"a","section_id":"s1","kind":"prose","source_pages":[1],"text":"The first complete author paragraph."},
             {"block_id":"b","section_id":"s1","kind":"prose","source_pages":[2],"text":"The second complete author paragraph."}]}
        before=section_text(doc,["s1"]);findings=abstract_findings(doc)
        self.assertEqual([x["code"] for x in findings],["abstract_multiple_page_scope_review"])
        self.assertEqual(section_text(doc,["s1"]),before)

    def test_verified_absence_is_not_reported_as_unresolved_empty(self):
        doc={"paper_id":"synthetic","source_sha256":"a"*64,"raw_pages_sha256":"b"*64,"page_count":1,
             "sections":[],"blocks":[],"verified_absent_roles":["abstract"]}
        doc["absence_reviews"]={"abstract":{"schema":"source-absence-review-v1","paper_id":"synthetic",
             "source_sha256":"a"*64,"raw_pages_sha256":"b"*64,"page_count":1,"checked_pages":[1],
             "reviewer":"synthetic-test-only","role":"abstract","reason":"Synthetic absence fixture.",
             "full_native_prose_read":True,"physical_page_heading_layout_checked":True,
             "evidence":[{"path":"proof.txt","sha256":"c"*64,"description":"Synthetic proof."}]}}
        self.assertEqual(abstract_findings(doc),[{"code":"abstract_verified_absent"}])

    def test_unrecognized_toc_inside_abstract_is_flagged(self):
        doc={"sections":[{"section_id":"a","role":"abstract","origin":"printed-heading","parent_id":None}],
             "blocks":[{"block_id":"1","section_id":"a","kind":"prose","source_pages":[2],
                        "text":"Intro........1 Models........3 Results........9"}]}
        self.assertEqual(abstract_findings(doc)[0]["code"],"abstract_contains_possible_contents_entries")

    def test_omitted_same_page_sibling_is_flagged_not_silently_selected(self):
        doc={"sections":[{"section_id":"a","role":"abstract","origin":"printed-heading","parent_id":None},
                         {"section_id":"m","role":"model","parent_id":None}],
             "blocks":[{"block_id":"1","section_id":"a","kind":"heading","text":"Summary","source_pages":[1]},
                       {"block_id":"2","section_id":"a","kind":"prose","text":"Opening.","source_pages":[1]},
                       {"block_id":"3","section_id":"m","kind":"prose","text":"Possibly omitted continuation.","source_pages":[1]}]}
        found=abstract_findings(doc)
        self.assertEqual(found[0]["code"],"possible_abstract_envelope_exclusion")
        self.assertEqual(found[0]["block_ids"],["3"])
        doc["sections"][1]["parent_id"]="a"
        self.assertEqual(abstract_findings(doc),[])


class OCRFrontierTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name)
        cat = fixture(self.root, count=2)
        for paper in cat.papers:
            doc = cat.document(paper["paper_id"])
            doc["defects"] = [{"code": "native_text_empty_ocr_required", "page": 1}]
            path = self.root / paper["document"]; path.write_bytes(encoded(doc))
            paper["document_sha256"] = file_hash(path)
        value = cat.catalog; value.pop("dataset_id")
        value["dataset_id"] = digest(encoded(value))
        (self.root / "catalog.json").write_bytes(encoded(value))
        self.output = self.root / "ocr-frontier"

    def tearDown(self):
        self.tmp.cleanup()

    def fake_recover(self, root, pid, pages, output):
        doc = Catalog(root).document(pid); values = []
        for number in pages:
            path = output / f"page-{number:04d}.json"
            json_new(path, {"page": number, "lines": [], "review_status": "pending"})
            values.append({"page": number, "path": path.name, "sha256": file_hash(path)})
        json_new(output / "manifest.json", {"paper_id": pid, "source_sha256": doc["source_sha256"], "pages": values})

    def test_frontier_resume_skips_completed_without_promoting_source(self):
        with patch("recover_empty_text_frontier.recover", side_effect=self.fake_recover) as mocked:
            a = recover_frontier(self.root, self.output, max_papers=1)
            b = recover_frontier(self.root, self.output, max_papers=1)
            c = recover_frontier(self.root, self.output)
        self.assertEqual(mocked.call_count, 2)
        self.assertEqual([a["completed_pages"], b["completed_pages"], c["completed_pages"]], [1, 2, 2])
        self.assertEqual(frontier(Catalog(self.root))["page_count"], 2)

    def test_modified_completed_evidence_and_queue_fail_closed(self):
        with patch("recover_empty_text_frontier.recover", side_effect=self.fake_recover):
            report = recover_frontier(self.root, self.output, max_papers=1)
        manifest = self.output / report["manifests"][0]["path"]
        (manifest.parent / "page-0001.json").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "modified"):
            recover_frontier(self.root, self.output)
        (self.output / "queue.json").write_bytes(b"{}")
        with self.assertRaisesRegex(ValueError, "version changed"):
            recover_frontier(self.root, self.output)


class NativeCorpusIntegrationTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("pdftotext"), "Poppler not installed")
    def test_pdf_to_index_export_and_source_accounting(self):
        try:
            import pymupdf
        except ImportError:
            self.skipTest("PyMuPDF not installed")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); pdfpath = root / "source.pdf"; output = root / "corpus"
            pdf = pymupdf.open()
            p = pdf.new_page(); p.insert_text((72, 72), "Summary", fontsize=16)
            p.insert_text((72, 110), "A complete abstract has a method, a result and a boundary.")
            p = pdf.new_page(); p.insert_text((72, 72), "1 Introduction", fontsize=16)
            p.insert_text((72, 110), "The next section retains all its original running text.")
            pdfpath.write_bytes(pdf.tobytes()); pdf.close()
            m = {"paper_id": "P-A-2020-synthetic-test", "problem_type": "A", "year": 2020,
                 "queue_position": 1, "page_count": 2, "relative_path": "source.pdf", "sha256": file_hash(pdfpath)}
            scope = {"scope_id": "synthetic-only", "source_root": str(root), "paper_count": 1,
                     "physical_page_count": 2, "records": [m]}
            json_new(output / "scope.json", scope)
            extract_record(scope, m, output); index(output)
            result = validate(output, verify_pdfs=True)
            self.assertTrue(result["structural_integrity_pass"], result["errors"])
            self.assertFalse(result["source_completeness_accepted"])
            selected = Catalog(output).select("abstract")
            self.assertEqual(len(selected), 1)
            self.assertIn("complete abstract", Catalog(output).text_and_spans(selected[0])[0])
            json_new(output / "legacy-preimages.json", {})
            proof = output / "inputs/source-reviews/nested/proof.json"; json_new(proof, {"synthetic": True})
            base=root / "base-skill"; base.mkdir()
            (base/"SKILL.md").write_text("---\nname: synthetic-test\ndescription: Synthetic fixture only.\n---\n\n## Routes\n",encoding="utf-8")
            packed=root / "new-skill"
            result=package_corpus_skill(base,output,packed,preview=True)
            self.assertTrue(result["preview"])
            self.assertEqual((packed/"assets/text-corpus/inputs/source-reviews/nested/proof.json").read_bytes(),proof.read_bytes())
            self.assertTrue(validate(packed/"assets/text-corpus")["structural_integrity_pass"])
            with self.assertRaises(ValueError):
                index(output)
            # A valid SQLite file and a freshly bound catalog do not prove the
            # derived index contains the authoritative chapter text.
            con=sqlite3.connect(output/'corpus.sqlite3')
            con.execute("UPDATE sections SET text='stale chapter bytes'")
            con.execute("UPDATE section_search SET text='stale search bytes'")
            con.commit();con.close()
            binding=json.loads((output/'catalog.json').read_text(encoding='utf-8'))
            binding.pop('dataset_id');binding['sqlite_sha256']=file_hash(output/'corpus.sqlite3')
            binding['dataset_id']=digest(encoded(binding))
            (output/'catalog.json').write_text(json.dumps(binding),encoding='utf-8')
            rejected=validate(output)
            self.assertFalse(rejected['structural_integrity_pass'])
            self.assertTrue(any('SQLite section view mismatch' in e for e in rejected['errors']))
            self.assertTrue(any('SQLite search view mismatch' in e for e in rejected['errors']))

    @unittest.skipUnless(shutil.which("pdftotext"), "Poppler not installed")
    def test_source_bound_ocr_remains_preview_and_native_text_is_retained(self):
        try:
            import pymupdf
        except ImportError:
            self.skipTest("PyMuPDF not installed")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); output = root / "native"; derived = root / "ocr-derived"
            pdf = pymupdf.open(); page = pdf.new_page(); page.insert_text((72, 100), "Damaged native opening.")
            pdfpath = root / "source.pdf"; pdfpath.write_bytes(pdf.tobytes()); pdf.close()
            m = {"paper_id": "P-A-2020-ocr-synthetic", "problem_type": "A", "year": 2020,
                 "queue_position": 1, "page_count": 1, "relative_path": "source.pdf", "sha256": file_hash(pdfpath)}
            scope = {"scope_id": "synthetic", "source_root": str(root), "paper_count": 1,
                     "physical_page_count": 1, "records": [m]}
            json_new(output / "scope.json", scope); json_new(output / "legacy-preimages.json", {})
            extract_record(scope, m, output); index(output)
            evidence = root / "ocr"; pagefile = evidence / "page-0001.json"
            json_new(pagefile, {"page": 1, "lines": [
                {"text": "Summary", "score": .99, "pdf_box": [[72, 72], [150, 72], [150, 88], [72, 88]]},
                {"text": "A full restored paragraph is still an unverified OCR candidate.", "score": .98,
                 "pdf_box": [[72, 110], [450, 110], [450, 122], [72, 122]]}]})
            manifest = evidence / "manifest.json"
            json_new(manifest, {"paper_id": m["paper_id"], "source_sha256": m["sha256"], "ocr_version": "synthetic",
                                "model_sha256": {}, "pages": [{"page": 1, "path": pagefile.name, "sha256": file_hash(pagefile)}]})
            resegment(output, derived, [manifest]); index(derived)
            result = validate(derived)
            self.assertTrue(result["structural_integrity_pass"], result["errors"])
            self.assertFalse(result["source_completeness_accepted"])
            self.assertTrue((derived / "papers" / m["paper_id"] / "raw/parent-pages.jsonl").is_file())
            c = Catalog(derived); selected = c.select("abstract")[0]
            self.assertEqual(selected["status"], "present-unverified")
            self.assertIn("full restored paragraph", c.text_and_spans(selected)[0])


if __name__ == "__main__":
    unittest.main()
