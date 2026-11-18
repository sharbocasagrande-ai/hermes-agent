"""Behavior contracts for the protected WhatsApp skill's read-only diagnostic."""
import importlib.util
import json
from pathlib import Path
import sqlite3
from unittest.mock import Mock


def locate_skill():
    for root in Path(__file__).resolve().parents:
        for relative in ['bundle/whatsapp-envios-protegidos', 'optional-skills/communication/whatsapp-envios-protegidos', '.']:
            path = root / relative
            if (path / 'SKILL.md').is_file() and (path / 'scripts/diagnostico.py').is_file():
                return path
    raise RuntimeError('Skill package not found')


SKILL = locate_skill()
spec = importlib.util.spec_from_file_location('whatsapp_skill_diagnostic', SKILL / 'scripts/diagnostico.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_pending_projection_excludes_private_values():
    payload = {'dictated': [{'source_id': 'PRIVATE_ID', 'dictation': 'PRIVATE_TEXT', 'recipient_name': 'PRIVATE_NAME'}], 'tasks': [{'id': 'PRIVATE_ID', 'state': 'authorized', 'text': 'PRIVATE_TEXT'}], 'preparation': {'text': 'PRIVATE_TEXT'}, 'latestTask': {'state': 'sent', 'recipient': 'PRIVATE_NUMBER', 'result_id': 'PRIVATE_RECEIPT', 'followup': {'state': 'completed', 'blocked': True, 'reply': 'PRIVATE_TEXT'}}}
    result = m.project_pending(payload)
    assert 'PRIVATE_' not in json.dumps(result)
    assert result['pending_by_state'] == {'authorized': 1}
    assert result['latest_has_receipt'] and result['block_confirmed']


def test_health_projection_drops_session_paths_and_extra_fields():
    result = m.project_health({'status': 'connected', 'scriptHash': 'a' * 16, 'session': 'PRIVATE_SESSION', 'token': 'PRIVATE_TOKEN', 'capabilities': {'ownerDirectedProtocol': 1, 'private': 'PRIVATE_FIELD'}})
    assert result['status'] == 'connected'
    assert result['capabilities']['ownerDirectedProtocol']
    assert 'PRIVATE_' not in json.dumps(result)


def test_report_calls_only_two_read_endpoints(tmp_path):
    reader = Mock(side_effect=[{'status': 'connected'}, {'latestTask': {'state': 'sent', 'result_id': 'PRIVATE_RECEIPT'}}])
    result = m.build_report(reader, tmp_path)
    assert [call.args for call in reader.call_args_list] == [('/health',), ('/owner-task/pending',)]
    assert result['read_only'] and not result['real_message_sent']
    assert not (tmp_path / 'state.db').exists()
    assert 'PRIVATE_' not in json.dumps(result)


def test_read_failure_is_minimized_and_does_not_trigger_retry_or_send(tmp_path):
    reader = Mock(side_effect=RuntimeError('PRIVATE_TOKEN_AND_MESSAGE'))
    result = m.build_report(reader, tmp_path)
    assert reader.call_count == 2
    assert result['health']['status'] == 'unavailable'
    assert result['tasks']['status'] == 'unavailable'
    assert 'PRIVATE_' not in json.dumps(result)


def make_context(profile, names):
    with sqlite3.connect(profile / 'state.db') as db:
        db.executescript('CREATE TABLE sessions(source,ended_at,system_prompt_hash,tool_names);CREATE TABLE system_prompts(hash,prompt);')
        db.execute('INSERT INTO sessions VALUES(?,NULL,?,?)', ('whatsapp', 'prompt', 'pin'))
        db.execute('INSERT INTO system_prompts VALUES(?,?)', ('prompt', 'PRIVATE_MEMORY\n<!-- shar-whatsapp-policy-rc8:start -->'))
        db.execute('INSERT INTO system_prompts VALUES(?,?)', ('pin', json.dumps({'tools': [{'function': {'name': n}} for n in names]})))


def test_current_context_is_read_without_exporting_or_changing_history(tmp_path):
    make_context(tmp_path, m.TOOLS)
    original = (tmp_path / 'state.db').read_bytes()
    result = m.inspect_sessions(tmp_path)
    assert result['sessions'][0]['protected_tools_complete']
    assert result['sessions'][0]['administrative_policy_rc8_present']
    assert 'PRIVATE_' not in json.dumps(result)
    assert (tmp_path / 'state.db').read_bytes() == original


def test_frozen_tool_pin_gap_is_visible_without_guessing_current_permission(tmp_path):
    make_context(tmp_path, {'terminal'})
    result = m.inspect_sessions(tmp_path)
    assert not result['sessions'][0]['protected_tools_complete']
    assert result['sessions'][0]['protected_tools_present'] == 0
    assert result['sessions'][0]['administrative_policy_rc8_present']


def test_http_adapter_uses_get_and_rejects_effects_before_connecting():
    client = Mock()
    client.client_config.return_value = ('FAKE_SOCKET', {'Authorization': 'PRIVATE_FAKE_TOKEN'})
    connection = client.UnixHTTPConnection.return_value
    connection.getresponse.return_value.status = 200
    connection.getresponse.return_value.read.return_value = b'{"status":"connected"}'
    read = m.make_reader(client)
    assert read('/health')['status'] == 'connected'
    assert read('/owner-task/pending')['status'] == 'connected'
    for route in ['/send', '/messages', '/owner-task/dictated', '/owner-task/send', '/archive/search?query=x']:
        try:
            read(route)
        except ValueError:
            pass
        else:
            raise AssertionError('An effect or queue route was accepted')
    assert [call.args for call in connection.request.call_args_list] == [('GET', '/health'), ('GET', '/owner-task/pending')]
    assert connection.close.call_count == 2


def test_http_refusal_closes_connection_and_does_not_read_private_body():
    client = Mock()
    client.client_config.return_value = ('FAKE_SOCKET', {})
    connection = client.UnixHTTPConnection.return_value
    connection.getresponse.return_value.status = 403
    read = m.make_reader(client)
    try:
        read('/health')
    except RuntimeError:
        pass
    else:
        raise AssertionError('HTTP refusal should fail')
    connection.getresponse.return_value.read.assert_not_called()
    connection.close.assert_called_once()


def test_deferred_catalog_is_not_diagnosed_as_missing_tools(tmp_path):
    profile=tmp_path/'profile';profile.mkdir();db=sqlite3.connect(profile/'state.db')
    db.executescript('CREATE TABLE sessions(source,ended_at,system_prompt_hash,tool_names);CREATE TABLE system_prompts(hash,prompt);')
    tools=[{'type':'function','function':{'name':n}} for n in ['tool_search','tool_describe','tool_call']]
    db.execute('INSERT INTO system_prompts VALUES(?,?)',('pin',json.dumps({'tools':tools})))
    db.execute('INSERT INTO system_prompts VALUES(?,?)',('prompt','shar-whatsapp-policy-rc8:start'))
    db.execute('INSERT INTO sessions VALUES(?,NULL,?,?)',('whatsapp','prompt','pin'));db.commit();db.close()
    row=m.inspect_sessions(profile)['sessions'][0]
    assert row['protected_tools_present']==0
    assert row['deferred_catalog_available'] is True
    assert row['snapshot_alone_diagnoses_tool_absence'] is False


def test_context_plan_projection_drops_private_content_and_source():
    value=m.project_pending({'plan':{'state':'reviewed','planId':'PRIVATE_ID','text':'PRIVATE_TEXT','recipient':'PRIVATE_NUMBER'}})
    assert value['context_plan_present'] is True
    assert value['context_plan_state']=='reviewed'
    assert 'PRIVATE_' not in json.dumps(value)



def test_followup_speech_capability_is_reported_without_private_fields():
    value = m.project_health({'status': 'connected', 'scriptHash': 'a' * 16, 'capabilities': {'ownerFollowupSpeechProtocol': 1}, 'transcript': 'PRIVATE_TEXT'})
    assert value['capabilities']['ownerFollowupSpeechProtocol'] is True
    assert 'PRIVATE_' not in json.dumps(value)


def test_missing_followup_speech_is_not_invented_from_connection_status():
    value = m.project_health({'status': 'connected', 'capabilities': {'ownerContextPlanProtocol': 1}})
    assert value['capabilities']['ownerContextPlanProtocol'] is True
    assert value['capabilities']['ownerFollowupSpeechProtocol'] is False
