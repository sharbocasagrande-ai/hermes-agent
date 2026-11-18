# Descritor da mensagem e instrução restritiva — RC10.3

Após a RC10.2-fix1, um novo pedido real ainda recebeu VOICE_INTENT_NOT_ADMITTED. A transcrição de leitura usou “mensagem de texto” e “E, somente isso, mande somente essa mensagem e não responda mais nada”. Essas construções não eram cobertas. Não tratar a revisão anterior nem seus testes como aceite desse pedido.

A RC10.3 reconhece o descritor de texto no envelope comum e delimita a cauda restritiva como metadado de envio único, sem acompanhamento ou bloqueio. Descritor desconhecido preserva preparação com destino e prévia, sem conceder execução direta; controle ambíguo também exige preparação. Conteúdo deliberadamente citado fica literal. Gramática comum não implica aceitação de qualquer frase.

Conferir ownerStructuredRequestRevision=3, release e hash ativos. A reprodução Linux passou em 351 testes Node e oito do atualizador. O teste de análise pura da fonte recusada lê a transcrição protegida, sem criar origem nem tarefa, alterar validade ou executar mensagem. Aceite real exige novo evento nativo depois da instalação e seu próprio comprovante.

No diagnóstico, correlacionar intake.stamp com a nova ordem. fresh=false pode ser o pedido mais recente que expirou enquanto se investigava; não demonstra que ele pertence a outra tentativa nem permite ignorar uma falha nova. Registrar timestamp, estado, razão e vínculo à tarefa. A revisão da skill preserva o stamp mínimo e a revisão estrutural sem exportar corpo, destinatário ou autenticação.

## Histórico RC10.2 preservado

# Análise estrutural comum — RC10.2

Usar a capacidade ownerStructuredRequestProtocol=1 para identificar a correção instalada. A RC10.1 transcrevia o novo áudio, detectava envio e ainda recusava a admissão por gramáticas diferentes nos caminhos de missão, plano e ditado. O decoder protegido deste incidente já tinha o vocativo Shar; a variante de leitura Char não era a causa real desse áudio.

A referência ao canal “mensagem do WhatsApp/no WhatsApp”, o envelope “celular/telefone de/do/da” e o aposto “meu filho” são elementos estruturais do pedido. Só o nome isolado segue à agenda. Parentesco não autentica o titular nem identifica automaticamente uma pessoa. O vocativo Char pode ser reconhecido como chamada sem reescrever o corpo literal e sem conceder autoridade.

Uma análise comum delimita nome, corpo, acompanhamento e restrições. “Não responda nada a ele” e ressalvas finais reconhecidas de segurança/autonomia ficam fora do texto do contato; ausência de acompanhamento mantém envio único, sem resposta posterior ou bloqueio. Ambiguidade permanece em preparação para prévia, nunca em envio com controles misturados. Palavras de controle citadas deliberadamente no corpo permanecem literais. Não reparar a grafia do corpo por conta própria.

Na RC10.2 inicial, 341 testes Node e oito do atualizador passaram no Linux, incluindo a frase nativa conferida, os dez casos fornecidos, variantes combinadas e caminhos com alias/agenda, além de replay, origem antiga, destinatário sem comando, citações e negações. A busca continua presa ao provedor e à procedência existentes; não há nova autorização para executar o áudio histórico. Testes simulados não são aceite real.

O atualizador preserva também as linhas nativas de voz/origem e recusa a troca durante decodificação ou efeito ativo. Exigir novo pedido nativo depois da implantação para comprovar missão/tarefa e seu próprio recibo.

A revisão final fix1 passou em 343 testes Node e oito do instalador. Acrescenta a guarda de cauda desconhecida fora de corpo citado e a preparação para citação sem fechamento, conservando a recusa anterior e a literalidade. A skill 2.2.5 corrige também o cabeçalho portátil e deixa explícita a natureza histórica da preparação RC10.

## Histórico RC10.1 preservado

# Voz nativa, admissão e grafia — RC10.1

Use quando o titular deu uma ordem no celular e o modelo a compreendeu, mas a missão não apareceu. A referência foi atualizada após um caso real em 2026-11-18: a voz foi autenticada e transcrita, porém uma gramática ancorada no início ignorou o comando depois de uma introdução conversacional. Serviço conectado e testes sintéticos anteriores não comprovavam admissão daquele áudio.

## Fonte e diagnóstico

Confirmar `ownerNaturalUtteranceProtocol=1` e a release/hash carregados. Consultar `intake` e `mission` pela ponte existente. `intake` distingue estado da decodificação, presença de pedido de envio, fonte admitida, tipo de registro e motivo da recusa. `fresh=false` significa que a validade passou; correlacionar o timestamp com a ordem antes de classificá-la como alheia à tentativa atual. Um ditado admitido pode existir antes da tarefa e precisa continuar visível. Não usar `latestTask` antigo como recibo do pedido novo.

Na versão administrativa corrigida, uma instrução direta pode vir depois de um preâmbulo conversacional. A seleção considera apenas conteúdo nativo autenticado e não interpreta comando em citação, hipótese, narrativa de terceiro ou negação. Ela não cria autoridade a partir da transcrição entregue pelo modelo. Escopo não compreendido fica em preparação para plano completo ou gera falha técnica explícita; não copiar instruções de acompanhamento para o corpo inicial nem alegar falta de consentimento.

## Admissão recusada após decodificação completa

Se `intake.state=complete`, `has_send_request=true`, `source_registered=false` e `reason=VOICE_INTENT_NOT_ADMITTED`, descreva falha de admissão do pedido, não falha comprovada do transcritor nem falta de consentimento. Registre a captura enquanto `fresh=true`; uma fotografia datada não mantém a fonte válida.

Reproduza separadamente seleção do comando, identificação, corpo e restrições. Compare linguagem com referência ao canal, expressão celular/telefone do contato, aposto de parentesco e vocativo transcrito como Char. Os parsers podem divergir entre missão de contato externo e ditado por alias local. Um teste deve ter controle positivo e negação; ler a transcrição do agente não comprova as palavras exatas do decoder protegido.

Verifique também se não responda nada e uma ressalva final de segurança vazam para o corpo literal. Corrigir só o reconhecimento pode revelar envio de controles indevidos. O reparo deve manter a proibição de resposta em campo próprio e usar preparação/prévia quando o span for ambíguo, sem afrouxar autenticação, fonte, negações ou idempotência. Não rearmar o áudio do incidente para validar a correção.

## Acompanhamento falado

O fluxo finito pode reconhecer “quando ele responde bom dia, você manda um OK e não responde mais e encerra conversa”. O plano preserva o texto inicial, a condição exata, a resposta literal única e o término sem bloqueio. Ressalva sobre manter regras de segurança/autonomia não acrescenta efeitos. Outra operação no sufixo, contradição ou resposta indefinida não vira permissão de conversa livre. Conferir o plano admitido, não apenas a descrição do modelo.

## Grafia sugerida não prova identidade

Uma busca sem resultado pode testar no máximo duas variantes ortográficas limitadas de um único nome. Não é busca ampla na agenda, alias permanente, prova de parentesco ou autorização de envio. A sugestão conserva o cadastro CONTACT, recurso e telefone canonicalForm da agenda fixa; nunca deduz dígitos. Uma variante com resultado interrompe buscas mais amplas. Truncamento e falha de provedor impedem escolha automática.

O plano mostra nome e número e identifica a sugestão de grafia. Essa pessoa só é selecionada pela confirmação nativa vinculada à prévia; homônimos continuam exigindo identificação. Não cadastrar o destinatário como remetente autorizado nem trocar a tarefa de outra pessoa. Não suprimir ou duplicar a prévia nativa com outra pergunta livre.

## Validação real e recuperação

Uma reprodução do texto original em banco e transporte simulados comprova a regressão do parser e do fluxo; uma consulta real da agenda comprova a integração de leitura. Nenhuma delas comprova envio real pelo celular. O aceite real precisa de nova mensagem nativa do titular, referência nova, recibo do envio e estado do acompanhamento. Não rearmar o áudio do incidente, inventar evento de transporte ou reutilizar aprovação histórica para acelerar a validação.

Manutenção preserva política do dono, ACLs, sandbox, leitor OAuth e conversa. Corrigir interpretação do pedido não exige outro escritor OAuth, reset de sessão ou novas permissões. O reparo RC10.1 foi validado com 323 testes Node Linux, incluindo o fluxo completo da ponte com transporte simulado, e sete testes do instalador; essas contagens pertencem àquele pacote, sem promessa de gramática universal.
