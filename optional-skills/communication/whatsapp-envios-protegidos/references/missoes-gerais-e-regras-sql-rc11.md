# Missões gerais e regras SQL — RC11

A direção explícita de 2026-11-19 é envio direto quando claro, acompanhamento literal ou por objetivo conforme cada ordem, e padrões futuros ajustáveis pelo WhatsApp. Autenticação exclusiva permanece estrutural. Não há cadastro de destinatário como comandante.

## Contrato da fonte

`general_mission.current` preserva `sourceId`, `native_text`, `context`, `proposal`, `resolution`, estado e efeitos. `general_mission.rules` publica versão e defaults. A ponte registra mensagens nativas atuais autenticadas antes de gramáticas de envio. A transcrição original protegida é a referência; transcrição de leitura, ferramenta, histórico ou documento não substituem essa origem.

`whatsapp_executar_missao({source_id,plan})` aceita:

- `send`: `clarity: clear|needs_review`, `deliveries: [{recipients:[nomes/números expressos],text,reply}]`, `preview` opcional. Nenhuma pessoa pode ser omitida por não ter alias local. Mesmo destinatário repetido é deduplicado; conteúdos conflitantes para o mesmo destino exigem esclarecimento.
- `clarify`: `question` específica ao dado ausente. Preserva o pedido, sem envio.
- `continue`: `selection` igual ao candidate_id mostrado pela ponte, `corrected_query` expresso na resposta nativa, `duration_ms`/`max_replies` para completar limites. Só a pergunta corrente e válida.
- `confirm`: somente prévia corrente completa, íntegra, publicada e não expirada. Não confirma outro contato ou plano antigo.
- `configure`: `patch` com chaves conhecidas de rules. `send_mode: direct_clear|preview`; `source_ttl_ms`, `task_ttl_ms`, `preview_ttl_ms`, `literal_reply_window_ms`; `objective_duration_ms`, `objective_max_replies`; `reply_defaults`. Números devem vir da ordem. Não usar chaves inventadas, como confirm_before_send. Identidade e acesso não são campos configuráveis.
- `cancel`: `scope: latest|all|recipients` e `recipients` quando esse for o escopo. “Todas” exige alcance geral expresso. Cancelar acompanhamento de uma pessoa não altera outros contatos.
- `ignore`: conversa comum sem efeito de missão.

## Respostas

`reply.mode=none`; ou `literal` com `text`, condição `{mode:any}` ou `{mode:exact,text}`, `duration_ms`, `max_replies`; ou `objective` com `goal`, prazo e máximo de respostas. `block_after` só para pedido expresso de bloquear o contato/pessoa. Pergunte limites de objetivo ausentes, sem reiniciar o pedido inteiro. Condição exata compara frase normalizada; o plano literal não faz interpretação semântica de respostas.

O objetivo é conversa textual limitada. O helper usa o modelo configurado, sem ferramentas ou memória principal; recebe objetivo, mensagem inicial, até doze turnos da própria missão, mensagem do contato, prazo e saldo de respostas. Saída só texto e indicação de conclusão. A ponte fixa contato e limites antes do transporte. Falha/timeout fica incerto sem retry automático. A pausa/revogação é conferida outra vez após a redação.

## SQL e recibos

Tabelas aditivas: `mission_rule_versions`, `general_owner_sources`, `general_owner_requests`, `general_mission_effects`, `mission_conversations`, `mission_reply_events`. O agente comum não escreve diretamente no banco protegido. O versionamento guarda fonte nativa da mudança; consultas não renovam validade. Cada destino tem task_id, ID de mensagem, estado e acompanhamento próprios.

`recorded` comprova a fonte; `resolving` não é envio; `awaiting_details` conserva a dúvida; `reviewed` é prévia; `sent` é transporte aceito; `partial` e `uncertain` exigem reconciliação. Reinício não rearma estados incertos. Relato do destinatário, entrega e leitura são provas separadas.

## Validação

RC11 precisa das capacidades general/rules/objective=1, revisão6, hash do código, sete ferramentas no contexto atual, worker local autenticado, SQL efetivo e histórico preservado. Testar origem nova do titular após instalar. Não repetir ordens históricas, não fabricar evento em produção e não enviar teste manual para contatos. Os incidentes usados na reprodução não concedem autorização de reenvio.

Se a agenda indicar PROVIDER_AUTH_REFRESH_REQUIRED/CONTACT_PROVIDER_UNAVAILABLE, uma consulta Composio normal pode renovar a conexão existente; kind resume permite uma única retomada técnica da mesma fonte atual, válida, sem efeitos e com plano imutável. Não pedir nova ordem só por renovação OAuth. 
