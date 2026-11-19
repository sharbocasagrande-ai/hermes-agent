import importlib.util,json,unittest
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'scripts/diagnostico.py';s=importlib.util.spec_from_file_location('native_diag',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class NativeIntakeDiagnosticTests(unittest.TestCase):
 def test_fresh_unadmitted_voice_does_not_look_like_old_success(self):
  x=m.project_pending({'intake':{'type':'voice','fresh':True,'state':'complete','has_send_request':True,'source_registered':False,'reason':'VOICE_INTENT_NOT_ADMITTED','transcript':'PRIVATE_BODY','inbound':'PRIVATE_OWNER_ID','token':'PRIVATE_TOKEN'}})
  self.assertEqual(x['intake']['reason'],'VOICE_INTENT_NOT_ADMITTED');self.assertFalse(x['intake']['source_registered']);self.assertNotIn('PRIVATE_',json.dumps(x))
 def test_stale_intake_is_explicitly_historical(self):
  x=m.project_pending({'intake':{'type':'voice','fresh':False,'state':'complete','reason':'NO_EXECUTABLE_INTENT'}});self.assertFalse(x['intake']['fresh'])
 def test_dictation_registration_is_distinct_from_task_creation(self):
  x=m.project_pending({'intake':{'type':'voice','fresh':True,'state':'complete','source_registered':True,'registered_kind':'dictation','reason':'SOURCE_REGISTERED'}});self.assertEqual(x['intake']['registered_kind'],'dictation')
 def test_unknown_reason_and_capability_are_not_invented(self):
  x=m.project_pending({'intake':{'type':'PRIVATE_TYPE','state':'PRIVATE_STATE','reason':'PRIVATE_TOKEN','registered_kind':'PRIVATE_TOOL'}});self.assertEqual(x['intake']['reason'],'unknown');self.assertNotIn('PRIVATE_',json.dumps(x));self.assertFalse(m.project_health({})['capabilities']['ownerNaturalUtteranceProtocol'])
 def test_structured_protocol_is_observed_not_assumed(self):
  self.assertFalse(m.project_health({})['capabilities']['ownerStructuredRequestProtocol'])
  self.assertTrue(m.project_health({'capabilities':{'ownerStructuredRequestProtocol':1}})['capabilities']['ownerStructuredRequestProtocol'])
 def test_expired_new_order_keeps_native_stamp_without_private_content(self):
  x=m.project_pending({'intake':{'type':'voice','stamp':1795027279,'fresh':False,'state':'complete','reason':'VOICE_INTENT_NOT_ADMITTED','transcript':'PRIVATE_BODY','inbound':'PRIVATE_OWNER'}})
  self.assertEqual(x['intake']['stamp'],1795027279);self.assertFalse(x['intake']['fresh']);self.assertNotIn('PRIVATE_',json.dumps(x))
  for bad in [True,'1795027279',-1,10000000000]:self.assertIsNone(m.project_pending({'intake':{'stamp':bad}})['intake']['stamp'])
 def test_runtime_revision_is_observed_and_not_inferred_from_protocol(self):
  self.assertEqual(m.project_health({'capabilities':{'ownerStructuredRequestProtocol':1,'ownerStructuredRequestRevision':3}})['structured_request_revision'],3)
  for bad in [None,True,'3',-1,100000]:self.assertIsNone(m.project_health({'capabilities':{'ownerStructuredRequestRevision':bad}})['structured_request_revision'])
 def test_recipient_clarification_is_a_preserved_mission_not_a_technical_refusal(self):
  x=m.project_pending({'mission':{'state':'recipient_pending','reason':'RECIPIENT_REQUIRED','query':'PRIVATE_QUERY','text':'PRIVATE_TEXT'}});self.assertTrue(x['mission_present']);self.assertEqual(x['mission_reason'],'RECIPIENT_REQUIRED');self.assertNotIn('PRIVATE_',json.dumps(x))
 def test_scope_review_is_minimized_without_exporting_native_objective(self):
  x=m.project_pending({'preparation':{'reviewRequired':True,'objective':'PRIVATE_OBJECTIVE','preparationId':'PRIVATE_ID','recipient_name':'PRIVATE_PERSON'}});self.assertTrue(x['preparation_review_required']);self.assertNotIn('PRIVATE_',json.dumps(x))
  for bad in [None,False,'true',1]:self.assertFalse(m.project_pending({'preparation':{'reviewRequired':bad}})['preparation_review_required'])
if __name__=='__main__':unittest.main()

def test_general_mission_projection_keeps_only_counts_and_rules():
    raw={'general_mission':{'rules':{'version':2,'send_mode':'direct_clear','reply_defaults':{'goal':'PRIVATE_GOAL'}},'current':{'state':'sent','kind':'send','sourceId':'PRIVATE_SOURCE','native_text':'PRIVATE_TRANSCRIPT','context':[{'text':'PRIVATE_HISTORY'}],'recipients':[{'state':'sent','recipient':'PRIVATE_PHONE','text':'PRIVATE_BODY','result_id':'PRIVATE_RECEIPT'}]}}}
    out=m.project_pending(raw)
    assert out['general_source_present'] and out['general_state']=='sent'
    assert out['general_recipient_count']==1 and out['general_sent_count']==1
    assert out['rules_version']==2 and out['send_mode']=='direct_clear'
    assert 'PRIVATE_'not in json.dumps(out)
