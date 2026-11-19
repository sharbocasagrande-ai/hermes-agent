import importlib.util,json,unittest
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'scripts/diagnostico.py';spec=importlib.util.spec_from_file_location('skill_diagnostic',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class DiagnosticTests(unittest.TestCase):
 def test_mission_minimal_not_old_task_success(self):
  result=m.project_pending({'mission':{'state':'recipient_pending','reason':'CONTACT_PROVIDER_UNAVAILABLE','missionId':'PRIVATE_ID','query':'PRIVATE_NAME','text':'PRIVATE_BODY','recipient':'PRIVATE_PHONE','revision':2,'candidate_count':0},'latestTask':None})
  self.assertEqual(result['mission_state'],'recipient_pending');self.assertEqual(result['mission_revision'],2);self.assertFalse(result['latest_has_receipt']);self.assertNotIn('PRIVATE_',json.dumps(result))
 def test_capabilities_not_invented(self):
  h=m.project_health({'status':'connected','capabilities':{}});self.assertFalse(h['capabilities']['ownerMissionProtocol']);self.assertFalse(h['capabilities']['ownerContactProviderProtocol'])
 def test_untrusted_fields_not_reflected(self):
  p=m.project_pending({'mission':{'state':'PRIVATE_BODY','reason':'PRIVATE_TOKEN','candidate_count':-1,'revision':True}});self.assertEqual(p['mission_state'],'unknown');self.assertEqual(p['mission_reason'],'unknown');self.assertNotIn('PRIVATE_',json.dumps(p))
if __name__=='__main__':unittest.main()
