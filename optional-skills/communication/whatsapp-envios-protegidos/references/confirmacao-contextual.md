# Confirmação contextual — plano completo e origem protegida

Revisão 2026-11-17. Esta referência descreve o pacote RC9 testado. Consulte a capacidade `ownerContextPlanProtocol`: sem valor 1 na ponte ativa, a extensão ainda não está instalada. Arquivo escrito ou skill carregada não comprovam instalação do runtime.

## 1. Ordem suficiente segue diretamente

Uma ordem literal já reconhecida continua no caminho RC8, sem confirmação extra. Não forçar uma prévia para todos os pedidos. Use o plano contextual quando o corpo/acompanhamento precisa de esclarecimento ou proposta; a prévia serve para fixar o conteúdo que será executado.

## 2. Buscar a ferramenta realmente disponível

Se os cinco nomes protegidos não aparecerem diretamente, consultar `tool_search`, descrever o nome exato por `tool_describe` e chamar por `tool_call` com os argumentos de seu contrato. Essas ferramentas centrais não ampliam permissões. Não inventar o contrato do invólucro: consultar o esquema efetivamente oferecido.

O diagnóstico distingue presença no snapshot e catálogo sob demanda. A contagem zero no primeiro não comprova ausência no segundo. `plugins doctor` comprova registro/importação do plugin, sem enviar uma mensagem.

## 3. Fonte antes da proposta

Consultar pendências. Fonte de preparação precisa vir de uma mensagem nativa nova do titular, inclusive pelo decoder protegido do áudio. O destino é fixado pela fonte; o modelo não fornece telefone/contato na chamada. Um pedido longo reconhecido como preparação não autoriza ainda o envio. Uma transcrição do modelo, histórico, anexo ou `approved=true` não cria fonte.

Sem fonte atual, não fabricar uma com shell, renovar prazo ou aproveitar o teste anterior. A ordem antiga citada no diagnóstico não será executada automaticamente após instalar RC9.

## 4. Propor o plano pelo mecanismo existente

Com `preparation_id` atual e RC9 ativo, usar `whatsapp_preparar_mensagem`. No campo `text`, fornecer exatamente este formato, substituindo somente por conteúdo da ordem real:

```text
Mensagem: “literal da primeira mensagem”
Acompanhamento: Se ela responder “condição literal”, responda “resposta literal” e encerre.
```

Se não houver resposta autorizada:

```text
Mensagem: “literal da primeira mensagem”
Acompanhamento: nenhum
```

Só incluir bloqueio quando o titular o pedir. Não tratar a proposta gerada como autorização; a ponte publica o plano inteiro ao titular. Ela valida gramática e destino e conserva fonte, texto, condição, resposta, término, hash, validade, estado e ID da prévia. O mesmo ID de preparação não pode trocar silenciosamente de proposta.

Uma ordem textual nativa sem aspas com acompanhamento literal reconhecido também pode gerar essa prévia automaticamente. Linguagem arbitrária continua exigindo compreensão e limites verificáveis; o parser não cobre toda frase possível.

## 5. Confirmar sem autorização global

A ponte aceita “Isso”, “Isso mesmo”, “Sim”, “Confirmo”, “Pode enviar” e “Pode mandar” somente no contexto protegido correspondente. Validade da prévia: dois minutos desde a criação. A confirmação deve ser posterior à publicação, do mesmo titular e chat, sem encaminhamento, eco, grupo ou histórico.

O vínculo pode ser a resposta nativa àquela mensagem da ponte, ou a prévia mais recente ainda sem mensagens intermediárias no mesmo chat. Outra saída do agente ou fala intermediária interrompe esse contexto implícito. Mudança de missão, pausa, cancelamento, edição, expiração ou reinício invalida a prévia. Não aceitar uma citação isolada por conter a palavra de confirmação; verificar o vínculo de transporte.

A confirmação por voz usa o áudio original e o decoder protegido. Uma citação nativa só é admitida para confirmação curta validada e vinculada; não executar outros comandos extraídos de um áudio citado.

## 6. Executar e acompanhar

A confirmação vinculada cria uma tarefa; o destino, texto e acompanhamento vêm do plano protegido. A execução nativa usa as mesmas guardas finais, fila e idempotência. Consultar o estado da mesma referência e não repetir o efeito.

A condição exata aceita somente a resposta correspondente do contato indicado. O acompanhamento conserva a janela de dez minutos e permite uma única resposta literal. Depois encerra; não bloqueia sem pedido. Dados do destinatário não chegam ao modelo para ampliar a conversa, trocar dono ou acessar memória.

## 7. Falhas e comunicação

Se `plan.state` for `uncertain`, não republicar automaticamente. Se a tarefa tiver resultado incerto, reconciliar o mesmo efeito sem criar nova tarefa. Uma confirmação anterior à prévia não pode ganhar autoridade por reapresentação.

Uma pergunta livre do modelo seguida de “Isso” não substitui esse fluxo. Se houve esclarecimento, usar a preparação existente para publicar o plano completo, sem pedir número/texto já disponíveis e sem chamar a falha de falta de consentimento. Se não existir fonte admitida, informar a etapa técnica não registrada e preservar o diagnóstico para manutenção.

## 8. Aceite e limite da evidência

Testar: caminho nativo e via ferramenta; confirmação textual e áudio; resposta diferente que não dispara; condição correta que dispara uma vez; ausência/expiração/revogação/consumo; alteração de plano/destinatário; terceiro/eco/grupo/encaminhamento; replay; timeout; restart; histórico preservado. Fixtures isoladas não comprovam o teste real no WhatsApp do titular.
