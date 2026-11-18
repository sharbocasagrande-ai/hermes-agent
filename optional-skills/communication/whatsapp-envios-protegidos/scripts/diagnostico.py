#!/usr/bin/env python3
"""Read-only, minimized diagnostics for an already installed protected bridge."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import sqlite3

ROUTES = frozenset({'/health', '/owner-task/pending'})
TOOLS = frozenset({'whatsapp_envio_pontual', 'whatsapp_estado_envio', 'whatsapp_consultar_envios', 'whatsapp_preparar_mensagem', 'whatsapp_executar_ditado'})
CAPS = ('ownerTaskProtocol', 'ownerAudioProtocol', 'ownerVoiceActionProtocol', 'ownerDictationProtocol', 'ownerAckFlowProtocol', 'ownerDirectedProtocol', 'ownerContextPlanProtocol', 'ownerFollowupSpeechProtocol', 'ownerMissionProtocol', 'ownerContactProviderProtocol', 'ownerNaturalUtteranceProtocol', 'ownerStructuredRequestProtocol')
STATES = frozenset({'authorized', 'queued', 'preparing', 'sending', 'sent', 'uncertain', 'revoked', 'expired', 'failed', 'waiting_first', 'waiting_ack', 'claimed', 'thank_sending', 'blocking', 'completed', 'superseded', 'prepared', 'publishing', 'reviewed', 'consumed','recipient_pending','resolving','recipient_not_found','recipient_ambiguous','provider_unavailable','awaiting_preview','plan_reviewed'})


def safe_state(value):
    return value if isinstance(value, str) and value in STATES else 'unknown'


def project_health(data):
    data = data if isinstance(data, dict) else {}
    state = data.get('status')
    result = {'status': state if state in ('connected', 'disconnected', 'connecting', 'closed') else 'unknown'}
    caps = data.get('capabilities') or {}
    result['capabilities'] = {k: caps.get(k) == 1 for k in CAPS}
    revision = caps.get('ownerStructuredRequestRevision')
    result['structured_request_revision'] = revision if type(revision) is int and 0 < revision < 100000 else None
    digest = data.get('scriptHash')
    if isinstance(digest, str) and re.fullmatch('[a-f0-9]{16,64}', digest):
        result['script_hash'] = digest
    return result


def project_pending(data):
    data = data if isinstance(data, dict) else {}
    latest = data.get('latestTask') or {}
    tasks = data.get('tasks') if isinstance(data.get('tasks'), list) else []
    counts = {}
    for task in tasks:
        state = safe_state(task.get('state')) if isinstance(task, dict) else 'unknown'
        counts[state] = counts.get(state, 0) + 1
    followup = latest.get('followup') if isinstance(latest, dict) else None
    mission=data.get('mission') if isinstance(data.get('mission'),dict) else {}
    reason=mission.get('reason')
    raw_intake=data.get('intake') if isinstance(data.get('intake'),dict) else None
    intake=None
    if raw_intake is not None:
        kinds=('mission','task','preparation','dictation','context_plan','denied')
        reasons=('SOURCE_REGISTERED','NO_EXECUTABLE_INTENT','VOICE_INTENT_NOT_ADMITTED','VOICE_TIMEOUT','VOICE_UNCLEAR','VOICE_WORKER_UNAVAILABLE','VOICE_TRANSCRIPTION_FAILED','VOICE_REQUEST_REFUSED','UNSUPPORTED_FOLLOWUP','PROCESS_RESTART')
        stamp = raw_intake.get('stamp')
        intake={'stamp':stamp if type(stamp) is int and 0 < stamp < 10000000000 else None,
                'type':'voice' if raw_intake.get('type')=='voice' else 'unknown',
                'fresh':raw_intake.get('fresh') is True,
                'state':raw_intake.get('state') if raw_intake.get('state') in ('processing','complete','failed','uncertain') else 'unknown',
                'has_send_request':raw_intake.get('has_send_request') is True,
                'source_registered':raw_intake.get('source_registered') is True,
                'registered_kind':raw_intake.get('registered_kind') if raw_intake.get('registered_kind') in kinds else None,
                'reason':raw_intake.get('reason') if raw_intake.get('reason') in reasons else 'unknown'}
    return {'intake':intake,'mission_present':bool(mission),
            'mission_state':safe_state(mission.get('state')),
            'mission_reason':reason if reason in ('','RECIPIENT_REQUIRED','CONTACT_PROVIDER_UNAVAILABLE','PROVIDER_AUTH_REFRESH_REQUIRED','CONTACT_RESULTS_INCOMPLETE','CONTACT_PROVIDER_RESULT_INVALID','MISSION_PLAN_NOT_AVAILABLE') else 'unknown',
            'mission_revision':mission.get('revision') if type(mission.get('revision')) is int and 0<mission['revision']<100000 else None,
            'mission_candidate_count':mission.get('candidate_count') if type(mission.get('candidate_count')) is int and 0<=mission['candidate_count']<30 else None,
            'pending_by_state': counts,
            'context_plan_present': isinstance(data.get('plan'), dict),
            'context_plan_state': safe_state(data.get('plan', {}).get('state')) if isinstance(data.get('plan'), dict) else None,
            'dictated_sources': len(data.get('dictated')) if isinstance(data.get('dictated'), list) else 0,
            'preparation_present': isinstance(data.get('preparation'), dict),
            'latest_state': safe_state(latest.get('state')) if isinstance(latest, dict) else 'unknown',
            'latest_has_receipt': isinstance(latest, dict) and bool(latest.get('result_id')),
            'followup_state': safe_state(followup.get('state')) if isinstance(followup, dict) else None,
            'block_confirmed': isinstance(followup, dict) and followup.get('blocked') is True}


def inspect_sessions(profile):
    path = Path(profile) / 'state.db'
    if not path.is_file():
        return {'status': 'unavailable', 'reason': 'STATE_DB_NOT_FOUND'}
    result = []
    with sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True) as db:
        rows = db.execute('SELECT system_prompt_hash,tool_names FROM sessions WHERE source=? AND ended_at IS NULL', ('whatsapp',)).fetchall()
        for prompt_hash, pin_hash in rows:
            prompt = db.execute('SELECT prompt FROM system_prompts WHERE hash=?', (prompt_hash,)).fetchone()
            pin = db.execute('SELECT prompt FROM system_prompts WHERE hash=?', (pin_hash,)).fetchone()
            data = json.loads(pin[0]) if pin else {}
            names = {t.get('function', {}).get('name') or t.get('name') for t in data.get('tools', []) if isinstance(t, dict)}
            text = prompt[0] if prompt else ''
            deferred_bridge = {'tool_search', 'tool_describe', 'tool_call'} <= names
            result.append({'deferred_catalog_available': deferred_bridge,
                           'snapshot_alone_diagnoses_tool_absence': False,
                           'protected_tools_complete': TOOLS <= names,
                           'protected_tools_present': len(TOOLS & names),
                           'mission_resolver_in_snapshot':'whatsapp_resolver_missao' in names,
                           'administrative_policy_rc10_present':'shar-whatsapp-policy-rc10:start' in text,
                           'administrative_policy_rc8_present': 'shar-whatsapp-policy-rc8:start' in text,
                           'obsolete_policy_marker_present': 'shar-whatsapp-policy-20261110:start' in text})
    return {'status': 'read', 'active_whatsapp_sessions': len(result), 'sessions': result}


def load_reader(integration):
    if hasattr(os, 'geteuid') and os.geteuid() == 0:
        raise RuntimeError('EXECUTE_AS_OPERATIONAL_USER')
    path = (Path(integration).resolve() / 'client.py')
    if not path.is_file() or path.stat().st_uid != 0 or os.access(path, os.W_OK) or os.access(path.parent, os.W_OK):
        raise RuntimeError('TRUSTED_READ_ONLY_CLIENT_REQUIRED')
    spec = importlib.util.spec_from_file_location('protected_whatsapp_diagnostic_client', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return make_reader(module)


def make_reader(module):
    socket_path, headers = module.client_config()

    def read(route):
        if route not in ROUTES:
            raise ValueError('ROUTE_OUTSIDE_DIAGNOSTIC_SCOPE')
        connection = module.UnixHTTPConnection(socket_path)
        try:
            connection.request('GET', route, headers=headers)
            response = connection.getresponse()
            if response.status != 200:
                raise RuntimeError('DIAGNOSTIC_READ_REFUSED')
            payload = response.read(2 * 1024 * 1024 + 1)
            if len(payload) > 2 * 1024 * 1024:
                raise RuntimeError('RESULT_TOO_LARGE')
            return json.loads(payload)
        finally:
            connection.close()
    return read


def build_report(read, profile):
    report = {'read_only': True, 'real_message_sent': False, 'private_content_exported': False}
    for name, route, project in [('health', '/health', project_health), ('tasks', '/owner-task/pending', project_pending)]:
        try:
            report[name] = project(read(route))
        except Exception as error:
            report[name] = {'status': 'unavailable', 'error_type': type(error).__name__}
    try:
        report['context'] = inspect_sessions(profile)
    except Exception as error:
        report['context'] = {'status': 'unavailable', 'error_type': type(error).__name__}
    report['limits'] = ['No send/approval/source creation.', 'No delivery or reading proof.', 'No complete security audit.']
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', default=os.environ.get('HERMES_HOME'))
    parser.add_argument('--integration', required=True)
    args = parser.parse_args()
    if not args.profile or not Path(args.profile).is_dir():
        parser.error('Inform an existing profile with --profile or HERMES_HOME.')
    try:
        reader = load_reader(args.integration)
        report = build_report(reader, args.profile)
    except Exception as error:
        report = {'read_only': True, 'status': 'unavailable', 'error_type': type(error).__name__}
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
