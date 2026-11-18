# Voz nativa, admissão e grafia — RC10.1

Use quando o titular deu uma ordem no celular e o modelo a compreendeu, mas a missão não apareceu. A referência foi atualizada após um caso real em 2026-11-18: a voz foi autenticada e transcrita, porém uma gramática ancorada no início ignorou o comando depois de uma introdução conversacional. Serviço conectado e testes sintéticos anteriores não comprovavam admissão daquele áudio.

## Fonte e diagnóstico

Confirmar `ownerNaturalUtteranceProtocol=1` e a release/hash carregados. Consultar `intake` e `mission` pela ponte existente. `intake` distingue estado da decodificação, presença de pedido de envio, fonte admitida, tipo de registro e motivo da recusa. `fresh=false` é histórico; não tratá-lo como a ordem corrente. Um ditado admitido pode existir antes da tarefa e precisa continuar visível. Não usar `latestTask` antigo como recibo do pedido novo.

Na versão administrativa corrigida, uma instrução direta pode vir depois de um preâmbulo conversacional. A seleção considera apenas conteúdo nativo autenticado e não interpreta comando em citação, hipótese, narrativa de terceiro ou negação. Ela não cria autoridade a partir da transcrição entregue pelo modelo. Escopo não compreendido fica em preparação para plano completo ou gera falha técnica explícita; não copiar instruções de acompanhamento para o corpo inicial nem alegar falta de consentimento.

## Acompanhamento falado

O fluxo finito pode reconhecer “quando ele responde bom dia, você manda um OK e não responde mais e encerra conversa”. O plano preserva o texto inicial, a condição exata, a resposta literal única e o término sem bloqueio. Ressalva sobre manter regras de segurança/autonomia não acrescenta efeitos. Outra operação no sufixo, contradição ou resposta indefinida não vira permissão de conversa livre. Conferir o plano admitido, não apenas a descrição do modelo.

## Grafia sugerida não prova identidade

Uma busca sem resultado pode testar no máximo duas variantes ortográficas limitadas de um único nome. Não é busca ampla na agenda, alias permanente, prova de parentesco ou autorização de envio. A sugestão conserva o cadastro CONTACT, recurso e telefone canonicalForm da agenda fixa; nunca deduz dígitos. Uma variante com resultado interrompe buscas mais amplas. Truncamento e falha de provedor impedem escolha automática.

O plano mostra nome e número e identifica a sugestão de grafia. Essa pessoa só é selecionada pela confirmação nativa vinculada à prévia; homônimos continuam exigindo identificação. Não cadastrar o destinatário como remetente autorizado nem trocar a tarefa de outra pessoa. Não suprimir ou duplicar a prévia nativa com outra pergunta livre.

## Validação real e recuperação

Uma reprodução do texto original em banco e transporte simulados comprova a regressão do parser e do fluxo; uma consulta real da agenda comprova a integração de leitura. Nenhuma delas comprova envio real pelo celular. O aceite real precisa de nova mensagem nativa do titular, referência nova, recibo do envio e estado do acompanhamento. Não rearmar o áudio do incidente, inventar evento de transporte ou reutilizar aprovação histórica para acelerar a validação.

Manutenção preserva política do dono, ACLs, sandbox, leitor OAuth e conversa. Corrigir interpretação do pedido não exige outro escritor OAuth, reset de sessão ou novas permissões. O reparo RC10.1 foi validado com 323 testes Node Linux, incluindo o fluxo completo da ponte com transporte simulado, e sete testes do instalador; essas contagens pertencem àquele pacote, sem promessa de gramática universal.
