import importlib.util,json,unittest
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'optional-skills/communication/whatsapp-envios-protegidos/scripts/diagnostico.py';s=importlib.util.spec_from_file_location('native_diag',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
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
if __name__=='__main__':unittest.main()
