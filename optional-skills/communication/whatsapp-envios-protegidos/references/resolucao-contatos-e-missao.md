> Escopo histórico/legado: com ownerGeneralMissionProtocol=1, a operação de fontes novas segue [RC11](missoes-gerais-e-regras-sql-rc11.md). As restrições e interfaces abaixo descrevem os protocolos anteriores; não substituem as escolhas atuais do titular.

# Contatos externos, correção de nome e confirmação de missão

## Diagnosticar antes de atribuir uma causa

- Compare a pesquisa autorizada de contatos com a resolução realmente consumida pela ponte. Encontrar um cadastro em Google Contacts/Composio não cria automaticamente uma preparação protegida nem prova que a ponte conhece aquele alias.
- Verifique se existe transição suportada de missão com destinatário pendente para candidato verificado. Não introduza telefone fornecido pelo modelo como se fosse fonte autenticada e não acrescente destinatários à lista de comandos.
- Teste separadamente pedido inicial, correção curta de nome, confirmação simples, confirmação composta e seleção de plano. Um parser que aceita Pode enviar pode rejeitar Esse mesmo seguido de Pode enviar. Uma correção de nome sem verbo pode não gerar pedido novo.
- Se só houver latestTask de outra pessoa, não o use como comprovante da missão atual. A chave de resolução precisa preservar origem, plano e destinatário. Draft consumido é idempotência apenas da mesma missão.
- Lista vazia não demonstra erro de parser. Quando não houver evento de admissão do caso real, trate a causa por evento como lacuna e mantenha as reproduções sintéticas como evidência de capacidade/defeito, não prova integral daquele incidente.

## Reproduzir sem efeitos

- Importe apenas funções puras verificadas, use contatos sintéticos e não abra banco nem rotas de execução para testes de parsing.
- Registre versão, hash dos módulos, expressão exata e saída real. Distinga sondagens que reproduzem defeitos de testes de aceitação que devem passar depois da correção.
- Revalide regressões antigas na versão atual. Não assumir que o defeito de uma release persiste: suporte a escreve e separação de ressalvas podem ter sido corrigidos, enquanto resolução de contato ou semântica de bloqueio continuam pendentes.
- Teste bloquear respostas/encerrar separadamente de bloquear o contato. Atualizar a skill não muda o parser que executa ordens nativas antes do modelo.

## Contrato candidato e requisitos de correção

- Preserve uma missão nativa aguardando identificação em vez de exigir a repetição de todo o pedido. Vincule correções/confirmadores ao contexto autenticado e defina concorrência, validade, revogação e recuperação.
- Proponha resolução de candidato com procedência verificável pelo backend; resultado livre do modelo não é prova. Número completo fornecido pelo titular e candidato de provider autorizado são caminhos diferentes e precisam de validação própria.
- Exija identificador canônico do WhatsApp sem ajuste adivinhado de dígitos. Falha ou ambiguidade não autorizam substituir o destinatário.
- Mantenha idempotência no limite do efeito, não só na criação do plano; não recupere timeout por novo envio. Rollback deve preservar recibos de efeitos já ocorridos.
- Documente novas interfaces como propostas, não como ferramentas instaladas. Mudanças do serviço, guardas ou configuração dependem de aprovação e executor administrativo autorizado.
- Entregue relatório e reprodução em anexo na pasta autorizada, com dados mínimos. Não publique fonte privada, credenciais ou conversas brutas. Não reexecute testes históricos para provar a correção.

## Estado do candidato em 2026-11-18

O candidato RC10 conserva missão por fonte/revisão, consulta a agenda por MCP fixo e conta fixada pelo administrador, e recusa prova/telefone/query fornecidos pelo modelo. A correção curta mantém o corpo; a escolha Contato N precisa da pergunta nativa correspondente. O contexto de voz é capturado na chegada, revalidado depois do decoder e não sobrevive a mudança de revisão. Resultados tardios não trocam o alvo corrigido. Nomes exatos e telefone canônico são exigidos; ausência de correspondência pede refinamento, sem adivinhar dígitos. O transporte ainda verifica o WhatsApp antes do efeito.

`mission` deve ser a referência da ordem corrente. O candidato esconde preparação/plano/último recibo alheios, rejeita confirmação nova de draft consumido e conserva replay da mesma fonte. Fonte expirada não renova por consulta: uma nova ordem nativa “Retome a missão” cria nova fonte e prévia, sem executar automaticamente. Pausa, cancelamento e reinício revogam pendências. Efeitos já enviados não são apagados.

Esse comportamento ainda precisa de implantação e aceite real por nova ordem do titular. Ler [RC10 e aceite](rc10-candidato-e-aceite.md); não tratar os testes isolados como mensagem enviada.
