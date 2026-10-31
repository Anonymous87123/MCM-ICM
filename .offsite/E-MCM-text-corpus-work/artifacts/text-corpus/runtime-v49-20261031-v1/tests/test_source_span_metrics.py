"""Reading order uses PDF origins without rewriting or interpreting math."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from source_span_metrics import flow_line,prepare_flow_pages,validate_flow_evidence
from extract_text_span_metrics import native_preimage
from text_corpus import encoded,file_hash,json_new,order_lines,prose_flow_line,write_new


class SourceSpanMetricFlowTests(unittest.TestCase):
    def fixture(self,text='(positive or negative),'):
        line={'line_id':'short','text':'X '+text,'font_size':12,'bbox':[60,100,250,170],
              'spans':[{'text':'X','bbox':[60,100,70,170],'size':12,'font':'CambriaMath'},
                       {'text':text,'bbox':[70,126,250,142],'size':12,'font':'Times'}]}
        metric={'line_id':'short','writing_mode':0,'direction':[1,0],
            'spans':[{'origin':[60,138],'ascender':3.1,'descender':-2.4},
                     {'origin':[70,138],'ascender':1.,'descender':-.33}]}
        return line,metric

    def test_short_clause_and_whitespace_use_actual_origin_not_word_count(self):
        for text in ('(positive or negative),',' '):
            line,metric=self.fixture(text);old=copy.deepcopy(line)
            moved=flow_line(line,metric,None,'e'*64)
            self.assertEqual(moved['bbox'],[60,126,250,142])
            self.assertEqual(line,old)
            self.assertEqual(moved['text'],line['text'])
            self.assertIs(prose_flow_line(moved),moved)
            before={'line_id':'previous','bbox':[60,110,500,126]}
            self.assertEqual([x['line_id'] for x in order_lines([moved,before],600)[0]],['previous','short'])

    def test_pure_glyph_line_needs_page_local_normal_font_and_preserves_all_text(self):
        line,metric=self.fixture();line['spans']=line['spans'][:1];metric['spans']=metric['spans'][:1]
        self.assertIs(flow_line(line,metric,None,'e'*64),line)
        ref={'ascender':1.,'descender':-.33,'font':'Times','source_line_id':'normal'}
        moved=flow_line(line,metric,ref,'e'*64)
        self.assertEqual(moved['bbox'][1],126)
        self.assertEqual(moved['text'],line['text'])

    def test_abnormal_trailing_space_cannot_move_a_heading_into_previous_sentence(self):
        line,metric=self.fixture('5 Simulation and Analysis')
        line['spans'][0]['text']=' '
        line['text']='5 Simulation and Analysis '
        moved=flow_line(line,metric,None,'e'*64)
        self.assertEqual(moved['bbox'][1:4:2],[126,142])
        previous={'line_id':'sentence-tail','bbox':[60,120,500,125]}
        self.assertEqual([x['line_id'] for x in order_lines([moved,previous],600)[0]],
                         ['sentence-tail','short'])
        line['text']=' '
        self.assertIs(flow_line(line,metric,None,'e'*64),line)

    def test_rotated_multibaseline_and_ordinary_font_lines_are_untouched(self):
        for update in ({'direction':[0,1]},{'writing_mode':1}):
            line,metric=self.fixture();metric.update(update)
            self.assertIs(flow_line(line,metric,None,'e'*64),line)
        line,metric=self.fixture();metric['spans'][0].update(ascender=1.,descender=-.33)
        self.assertIs(flow_line(line,metric,None,'e'*64),line)
        line,metric=self.fixture();line['spans'].append(dict(line['spans'][1]))
        metric['spans'].append({**metric['spans'][1],'origin':[70,160]})
        self.assertIs(flow_line(line,metric,None,'e'*64),line)

    def test_frozen_geometry_replays_and_rejects_forged_evidence_or_acceptance(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);evidence=root/'inputs/span-metrics'
            line,record=self.fixture();line.update(native_block=0,page=1)
            record['native_preimage_sha256']=native_preimage(line)
            raw=[{'page':1,'lines':[line]}]
            payload=evidence/'papers/p/span-metrics.jsonl'
            write_new(payload,json.dumps({'page':1,'lines':[record]})+'\n')
            complete=evidence/'papers/p/COMPLETE.json'
            json_new(complete,{'paper_id':'p','source_sha256':'a'*64,'raw_pages_sha256':'b'*64,
                              'page_count':1,'files':{'span-metrics.jsonl':file_hash(payload)}})
            manifest=evidence/'manifest.json';json_new(manifest,{'files':{'p':file_hash(complete)}})
            json_new(root/'scope.json',{'span_metrics_manifest_sha256':file_hash(manifest)})
            doc={'paper_id':'p','source_sha256':'a'*64,'raw_pages_sha256':'b'*64}
            _,flow=prepare_flow_pages(doc,raw,evidence)
            inferred=[{k:v for k,v in item.items() if k!='page'} for item in flow['changed_lines']]
            doc.update(span_origin_flow={'schema':flow['schema'],'metrics_sha256':flow['metrics_sha256'],
                                         'changed_lines':1,'source_fidelity_approved':False},
                       defects=[{'code':'inline_math_prose_flow_review','inference':inferred}],
                       blocks=[{'source_line_ids':['short'],'repairs':[
                           {'operation':'prose_flow_geometry_candidate',**inferred[0]}]}])
            validate_flow_evidence(root,doc,raw)
            for change in ('approval','page','block','missing'):
                altered=copy.deepcopy(doc)
                if change=='approval':altered['span_origin_flow']['source_fidelity_approved']=True
                if change=='page':altered['defects'][0]['inference'][0]['flow_bbox'][1]+=1
                if change=='block':altered['blocks'][0]['repairs'][0]['flow_bbox'][1]+=1
                if change=='missing':altered.pop('span_origin_flow')
                with self.assertRaises(ValueError):
                    validate_flow_evidence(root,altered,raw)
            complete.write_bytes(b'Changed source sidecar binding.')
            with self.assertRaisesRegex(ValueError,'manifest binding'):
                validate_flow_evidence(root,doc,raw)


if __name__=='__main__':
    unittest.main()
