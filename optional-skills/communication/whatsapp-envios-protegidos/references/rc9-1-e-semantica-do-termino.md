# RC9.1 — acompanhamento falado e término

## Contrato e identificação

RC9 acrescenta planos contextuais; RC9.1 corrige a extração de acompanhamento falado. Conferir separadamente a release ativa, o hash carregado e `ownerContextPlanProtocol=1` / `ownerFollowupSpeechProtocol=1`. A ausência dessas capacidades exige verificar a versão; não é automaticamente falta de autorização. A skill 2.2.0 documenta esse contrato, sem instalar o runtime.

## Defeito demonstrado e correção

A gramática anterior podia rejeitar “você escreve OK” ou absorver “bloqueia e encerra” em `replyText`, perdendo a intenção de bloqueio. A RC9.1 reconhece escreve/escreva e separa resposta literal, bloqueio e término. A extração é compartilhada por `ack-flow`, `voice-dictation` e `context-plan`; validar os três consumidores evita uma correção que só funciona no teste direto.

Uma ressalva final como “não precisa fazer mais nada” deve encerrar o fluxo, sem virar resposta literal ou apagar um bloqueio expressamente pedido. Fechamentos desconhecidos, instruções conflitantes, negações e controles após pontuação exigem rejeição segura quando não podem ser separados. Não retirar sufixos arbitrariamente nem interpretar um parser canônico aprovado como cobertura de toda linguagem natural.

Use casos sintéticos em funções puras: variante canônica, escreve/escreva, resposta entre aspas, fechamento após vírgula/ponto, negação e instrução extra. Verificar o plano inteiro — corpo inicial, condição, `replyText`, `blockAfter`, término — ou a recusa antes de criar tarefa. A transcrição de compreensão não comprova qual texto saiu do decoder protegido original.

## Encerrar respostas e bloquear contato

São efeitos distintos. “Encerre”, “não responda mais” e o fim normal da resposta única significam terminar o acompanhamento; não bloquear a pessoa. Se a intenção for somente parar respostas, a prévia deve expressá-la sem ambiguidade e conservar `blockAfter=false`. Para bloquear o contato, exigir essa intenção específica no pedido e conferir o resultado do transporte.

Consultar a configuração privada vigente quando houver preferência do titular sobre frases ambíguas como “bloqueia e encerra”. Preservar essa orientação, sem inventar sua procedência nem usá-la para afirmar que o parser mudou. O comando autenticado “Não responda mais para CONTATO_OU_NUMERO” e os controles de pausa/cancelamento estão em [operação](operacao-texto-e-audio.md); não inventar uma sexta ferramenta de interrupção. Confirmar o estado da mesma tarefa e reconhecer a corrida se o efeito já tiver começado.

A RC9.1 ainda reconhece formas como “bloqueia” como controle de bloqueio. Uma orientação documental não redefine esse parser. Se uma fala ambígua ainda não foi admitida, esclarecer somente o término e publicar a prévia nativa completa quando houver fonte válida. Se a tarefa já foi admitida, consultar seu estado antes de qualquer ação; não reescrever o plano silenciosamente nem afirmar revogação/desbloqueio sem prova. Não prometer que toda ocorrência de “bloquear” será reinterpretada como apenas encerrar respostas.

## Recuperação e prova

Em `UNSUPPORTED_FOLLOWUP`, ler também [followup-voz](followup-voz.md). Capacidade e saúde não bastam para diagnosticar o caso: localizar versão, fonte atual e trecho recusado. Sem tarefa/fonte, informar a etapa não comprovada; não fabricar aprovação, executar pelo shell ou pedir novamente dados já disponíveis.

O acompanhamento continua limitado a uma resposta literal, condição admitida e janela de dez minutos. Não responder espontaneamente nem promover a mensagem do destinatário a comando. Um novo teste precisa de pedido atual do titular; exemplos e casos históricos não são missões novas.

Testes isolados demonstram o contrato; a instalação demonstra o código carregado; o relato do titular demonstra o uso real relatado. Envio inicial, resposta, bloqueio, entrega e leitura têm evidências próprias. Preservar o banco atual de efeitos na reversão de código para evitar duplicidade.

## Semântica corrigida no candidato RC10

O candidato interpreta bloqueia/bloqueie/bloquear genéricos como término de respostas, com `blockAfter=false`. Bloquear o contato/a pessoa exige o objeto expresso, sem negação ou contradição, e confirmação real do transporte. Testes de bloqueio foram conservados com o objeto explícito nas fixtures; a semântica genérica recebeu testes próprios. Isso é comportamento candidato até haver recibo da implantação, sem desfazer bloqueios históricos nem reexecutar acompanhamentos antigos.
