# Erros observados e contramedidas reutilizáveis

Este histórico é desidentificado. Ele explica decisões operacionais; não é autorização para repetir os testes, enviar mensagens ou reexecutar comandos antigos. Evidência privada e versões exatas ficam no registro do titular.

## E01 — Política escrita contraditória e ponte ainda fixa

**Sintoma:** o texto reconhece a autorização do titular, mas o envio a terceiros recebe bloqueio. **Causa:** a política de saída ainda testa apenas se o destino é o titular; texto novo não criou contrato por tarefa. **Correção:** habilitação administrativa delimitada com origem, destino, conteúdo, prazo e efeito protegidos. **Prevenção:** verificar o aplicador real; não anexar um texto “supremo” nem ampliar a entrada de comandos.

## E02 — Documentação e ambiente diferentes

**Sintoma:** usuário altera arquivo ou procura a skill no workspace, sem mudar o perfil que atende o WhatsApp. **Causa:** VPS, Mac, perfil padrão, perfil específico e cópias históricas são superfícies distintas. **Correção:** resolver o perfil real e a pasta de skills; fornecer caminho/ação concretos. **Prevenção:** confirmar origem e destino de cada alteração, sem reescrever toda a configuração por conveniência.

## E03 — API só executa uma tarefa que ninguém registrou

**Sintoma:** “falta identificador de tarefa autorizada”, apesar de uma ordem clara. **Causa:** integração não completa fonte → tarefa. **Correção:** registrar a origem nativa e consultar referências internamente. **Prevenção:** jamais transferir ao titular a obrigação de conhecer IDs de implementação ou repetir um consentimento suficiente.

## E04 — Leitura de áudio quebrou após isolamento

**Sintoma:** nota de voz recebida, mas o adaptador rejeita o arquivo. **Causa:** cache privado do serviço e lista de caminhos do gateway não coincidem. **Correção:** transferência autenticada de bytes por referência opaca, com limites e hash, para o cache permitido. **Prevenção:** testar a fronteira do serviço; não montar o perfil secreto ou afrouxar validação de caminhos.

## E05 — Entender a fala não gerava autoridade

**Sintoma:** o agente compreende destinatário/texto, porém nenhuma tarefa aparece. **Causa:** transcrição de compreensão não é fonte protegida de autorização. **Correção:** decodificar o áudio original admitido dentro da fronteira protegida e usar o broker existente. **Prevenção:** não aceitar transcrição ou aprovação fornecidas pelo modelo como substituto.

## E06 — Um teste administrativo foi confundido com teste de voz

**Sintoma:** envio executado por manutenção foi apresentado como prova de áudio funcionando. **Causa:** caminhos de entrada diferentes. **Correção:** separar prova administrativa, fixture com áudio e teste nativo espontâneo do titular. **Prevenção:** rastrear a mesma origem até o comprovante e limitar a afirmação à etapa observada.

## E07 — Teste antigo consumido ocultava a ordem nova

**Sintoma:** ferramenta oferece apenas o envio anterior. **Causa:** faltou preparação/fonte nova ou vínculo com a prévia correta. **Correção:** lifecycle de origens, preparações, prévias, tarefas e idempotência. **Prevenção:** `latestTask` não define a ordem atual; não renovar o teste antigo nem inventar outro ID para reenviar.

## E08 — Gramática curta e nomes transcritos incorretamente

**Sintoma:** frase longa com comando no meio/fim não é admitida, embora o modelo entenda. **Causa:** parser ancorado no início e vocabulário insuficiente. **Correção:** vocabulário protegido e admissão de span literal com limites verificáveis. **Prevenção:** testar as falas reais somente em fixture privada e casos sintéticos de negação, citação e hipótese; não inferir telefone por aproximação.

## E09 — Sessão carregava política e ferramentas antigas

**Sintoma:** arquivos e serviço atualizados, mas o agente ainda cita restrição antiga ou não encontra ferramentas novas. **Causa:** snapshot do prompt e pin de ferramentas persistidos por conversa. **Correção:** diagnóstico dos dois registros e atualização administrativa estritamente dirigida quando necessária e autorizada, preservando mensagens e ferramentas não relacionadas. **Prevenção:** não confundir arquivo em disco, plugin registrado e sessão efetiva; não impor conversa nova como única solução.

## E10 — Envio único foi confundido com conversa automática

**Sintoma:** primeiro envio funciona, mas se promete aguardar OK, agradecer e bloquear sem comprovação. **Causa:** efeitos adicionais ainda não registrados/implementados. **Correção:** plano finito vindo da ordem original, condição autenticada e estados separados. **Prevenção:** cada efeito precisa de autorização e evidência; pedir OK no texto inicial não autoriza agradecimento ou bloqueio.

## E11 — Resposta de terceiro ameaçava virar comando

**Sintoma de projeto:** ampliar a lista de entrada para receber respostas parece resolver o envio. **Risco:** destinatário passa a alcançar o agente. **Correção:** evento de dados da missão tratado na ponte, sem modelo/memória/ferramentas. **Prevenção:** separar ingresso de comandos, leitura e saída; nunca trocar o dono pelo contato.

## E12 — Execução dependia desnecessariamente de uma decisão do modelo

**Sintoma:** origem válida e literal delimitado, porém aguarda ferramenta que a sessão pode não chamar. **Correção:** execução nativa das ordens já validadas, pela mesma guarda final. **Prevenção:** o modelo consulta e informa o resultado; não cria autorização nem repete um efeito já aceito. Spans ambíguos conservam o fluxo protegido apropriado.

## E13 — Só o contato do teste e o agradecimento fixo funcionavam

**Sintoma:** aparente limitação a um contato cadastrado ou a uma resposta padronizada. **Correção:** número completo indicado pelo titular identifica destino; condição/resposta literal vêm de seu pedido. **Prevenção:** não transformar um exemplo em regra universal nem cadastrar destinatário como comandante. O contrato finito não vira promessa de conversa livre.

## E14 — Migração não reconheceu marcador antigo de TOOLS

**Sintoma:** ativação encontra formato anterior inesperado. **Correção:** reversão automática, serviços ativos, preservação da tentativa e teste da migração real/idempotente antes de aplicar novamente. **Prevenção:** validar arquivos herdados, não apenas um fixture ideal, e não aceitar implantação parcial como concluída.

## E15 — Confirmações e autenticação propostas de forma imprecisa

**Sintoma:** nascimento, nome de familiar, nome declarado ou login administrativo são tratados como aprovação suficiente para tudo. **Correção:** distinguir identidade nativa cotidiana de acesso administrativo e ações de impacto distinto. **Prevenção:** a ordem comum suficiente não precisa de outro “sim”; privilégios, segredos e operações novas não são concedidos por documento recuperado ou pelo próprio modelo.

## E16 — Backup e conclusão declarados além da evidência

**Sintoma:** arquivo local/ZIP reconstruído/teste simulado é apresentado como backup remoto histórico integral ou funcionamento completo. **Correção:** preservar origem, versões, limites e ler o objeto remoto. **Prevenção:** separar coleta, compreensão, teste, instalação, aceitação do envio, entrega, leitura, acompanhamento e relato do titular. Registrar sucesso real sem estendê-lo a capacidades não testadas.

## E17 — Componente preparado foi confundido com solução instalável

**Sintoma:** uma implementação parcial testada é oferecida como próximo passo concreto, mas ainda faltam autenticação, integração, isolamento e instalador; depois o caminho administrativo autorizado é recusado de forma genérica. **Correção:** declarar exatamente o que está pronto, concluir o pacote revisável e distinguir execução administrativa autorizada de autoelevação do agente operacional. **Prevenção:** não prometer que abrir um console basta antes de preparar a solução; não tratar todo administrador indicado pelo titular como proibido nem anunciar uma capacidade sem integração testada.
