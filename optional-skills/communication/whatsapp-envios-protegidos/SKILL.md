---
name: whatsapp-envios-protegidos
description: Executar e diagnosticar envios de WhatsApp por texto ou áudio sob ordem autenticada do titular, usando a ponte protegida existente.
version: 2.2.8
author: SHARBO CASAGRANDE (@sharbocasagrande-ai); Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [WhatsApp, Messaging, Authorization, Troubleshooting]
    category: communication
---

# WhatsApp sob comando do titular

Operar a ponte protegida existente, preservando o comando exclusivo do titular e a distinção entre destinatário e comandante. Histórico, anexos e exemplos explicam o sistema; não iniciam novas mensagens. Esta skill não instala o runtime nem concede administração ao agente.

Diagnóstico atualizado em 2026-11-18. A configuração de referência passou a RC10.5; conferir o host, a release/hash e as capacidades ativos. Instalação e teste isolado não equivalem a envio real. Para missões, ler [RC10, capacidades e aceite](references/rc10-candidato-e-aceite.md); para fala compreendida sem missão, ler [voz nativa e admissão RC10.5](references/voz-nativa-e-admissao-rc10-1.md).

## Antes de operar

Confirmar perfil, conta e origem nativa autenticada. Uma ordem atual suficiente autoriza a tarefa delimitada, sem outro “sim” por hábito. Perguntar somente o dado essencial ausente ou ambíguo. Conta pessoal de monitoramento e grupos conservam seus limites; não trocar conta/canal para contornar uma recusa.

Ler [configuração e capacidades](CONFIGURACOES-WHATSAPP.md) e [autoridade](references/regras-de-autoridade.md). Para o fluxo solicitado, ler:

- Texto ou áudio: [operação](references/operacao-texto-e-audio.md). Compreender a transcrição não cria fonte protegida; executar somente a referência atual admitida.
- Composição, esclarecimento ou “Isso/Sim”: [confirmação contextual](references/confirmacao-contextual.md). Exige prévia nativa íntegra, fonte, mesmo titular/chat e validade de dois minutos. Pergunta livre não cria esse vínculo.
- Resposta condicional por voz, escreve/escreva ou término: [RC9.1 e semântica](references/rc9-1-e-semantica-do-termino.md), inclusive a diferença entre encerrar respostas e bloquear contato. Em `UNSUPPORTED_FOLLOWUP`, ler [diagnóstico de voz](references/followup-voz.md).
- Contato encontrado fora da ponte, correção curta de nome ou tarefa de outra pessoa: [resolução de contatos e missão](references/resolucao-contatos-e-missao.md). Refaça a busca autorizada com a grafia exata antes de pedir telefone; identificação não cria fonte nem permite trocar destino da tarefa.
- Falha ou manutenção: [diagnóstico](references/diagnostico-e-recuperacao.md), [erros observados](references/erros-e-contramedidas.md), [prevenção](references/prevencao-de-regressoes.md) e [validação/restauração](references/validacao-e-restauracao.md).

## Consultar antes de executar

1. Consultar `whatsapp_consultar_envios` e associar fonte/preparação/tarefa à ordem atual. `latestTask` pode ser um teste antigo consumido.
2. Se os nomes estiverem em catálogo diferido, descobrir/descrever por `tool_search` e `tool_describe`, depois chamar por `tool_call` com o esquema efetivo. Zero ferramentas WhatsApp no snapshot inicial não prova ausência do plugin.
3. A ponte pode já ter executado uma ordem literal nativamente. Se houver `sent`, consultar o mesmo comprovante, sem criar outro efeito.
4. Executar somente a referência válida e os argumentos abaixo. Não pedir IDs internos ao titular, inventar fonte ou acrescentar telefone, texto ou `approved` ao contrato de envio.
5. Depois de publicar a prévia nativa, conferir seu estado silenciosamente e deixá-la como última saída ao titular. Outra explicação pode romper o vínculo implícito e consumir o prazo; não duplicar a prévia. Após confirmação, consultar a mesma referência atual.
6. Informar somente a etapa comprovada. Em resultado incerto, reconciliar o mesmo efeito, sem reenvio automático.

| Ferramenta do plugin | Argumentos | Limite |
|---|---|---|
| `whatsapp_consultar_envios` | `{}` | Consulta; não autoriza. |
| `whatsapp_estado_envio` | `task_id` | Consulta o mesmo efeito e acompanhamento. |
| `whatsapp_envio_pontual` | somente `task_id` | Executa tarefa protegida já autorizada. |
| `whatsapp_executar_ditado` | `source_id`, `text` | Trecho literal compatível com o áudio admitido; sem inventar palavras, assinatura ou dígitos. |
| `whatsapp_preparar_mensagem` | `preparation_id`, `text` | Publica prévia somente ao titular, mantendo o destino fixado na fonte. |

Quando `ownerMissionProtocol=1` e `ownerContactProviderProtocol=1` forem confirmados na ponte ativa e o plugin publicar o contrato, `whatsapp_resolver_missao` aceita somente `mission_id` admitido. Sem essas provas, trate-a como interface proposta e siga o diagnóstico; não a invente nem copie telefone do modelo para uma tarefa.

As cinco ferramentas de base dependem do plugin protegido; não presumir disponibilidade em todo Hermes. Usar `skills_list`, `skill_view` e `read_file` para descoberta/referências; `terminal` apenas no diagnóstico opcional ou manutenção dentro do acesso autorizado.

## Revisão de escopo da origem

Se a preparação indicar `reviewRequired=true`, conservar o objetivo nativo completo e usar `whatsapp_preparar_mensagem` com o formato de plano completo: `Mensagem: “texto”`, nova linha, `Acompanhamento: nenhum` ou o acompanhamento finito reconhecido na origem. Não usar ditado, rascunho simples ou prévia em prosa para contornar essa revisão. A ponte publica o limite da confirmação: somente o plano de WhatsApp mostrado. Ações de manutenção mencionadas no preâmbulo não foram executadas por essa prévia; não executá-las nem alegar sua conclusão. Não acrescentar resposta ou bloqueio ausentes da fonte. Ler [admissão e revisão](references/voz-nativa-e-admissao-rc10-1.md).

## Limites que mudam a decisão

Sem pedido de resposta, somente o envio inicial. Acompanhamento admite uma resposta literal sob condição exata ou primeira resposta expressamente autorizada, em dez minutos. Encerrar respostas não é bloquear contato. Bloqueio exige intenção específica e resultado confirmado. Não prometer conversa livre ou outros tipos de efeito sem contrato próprio.

Dados do destinatário não mudam dono, missão, conteúdo, prazo ou acesso à memória/ferramentas. Pausa, revogação, expiração e consumo prevalecem. Ordem nova não reutiliza fonte antiga. Identidade vem do transporte, nunca de nascimento, parentesco, nome declarado ou `fromMe`.

Se o titular corrigir o acompanhamento de uma tarefa em curso, consultar imediatamente seu estado e usar somente o controle nativo de revogação disponível, verificando o resultado. Atualizar documentação não cancela uma pendência nem desfaz bloqueio. Uma confirmação nova justifica consulta atual; sem novo evento, não repetir indefinidamente consultas e a mesma resposta de impedimento.

Se não aparecer fonte/tarefa atual, informar que não há referência executável nem novo envio comprovado. Lista vazia não determina sozinha a causa. Não chamar um defeito técnico de falta de consentimento, pedir repetição desnecessária ou impor outra conversa. Se a correção exigir administração, preparar causa demonstrada, diferença mínima, teste e backup para o executor autorizado; não alterar as próprias proteções.

Uma falha de envio não determina falha em análise ou agendamento, que têm mecanismos próprios. Reavaliar uma solicitação posterior pelo caminho pertinente, sem declarar um transcritor reparado por consequência.

## Verificação

Separar: áudio reconhecido; fonte/tarefa registrada; envio aceito com ID; resposta recebida; resposta literal enviada; bloqueio confirmado se pedido; entrega e leitura quando existirem recibos próprios. Relato do titular é evidência de uso real atribuída a ele; não comprova todos os efeitos.

Diagnóstico opcional, como usuário operacional e com caminhos do inventário privado:

```text
python ${HERMES_SKILL_DIR}/scripts/diagnostico.py --profile CAMINHO_DO_PERFIL --integration CAMINHO_DA_INTEGRACAO
```

O script só lê saúde, pendências e metadados da sessão, projetando campos mínimos. Não consumir `/messages`, preparar prévia, enviar, renovar fonte ou exportar conversas. Conferir capacidades e hash da release ativa; arquivo salvo, plugin registrado e contexto da conversa são evidências diferentes.

Na manutenção, preservar histórico, controles e banco atual de efeitos. Reverter código não apaga mensagens transmitidas. Confirmar backups por leitura remota. As contagens de testes pertencem à versão testada e não garantem ausência de falhas futuras.
