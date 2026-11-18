# Diagnóstico e recuperação sem reduzir a segurança

## Ordem de investigação

Use esta sequência quando uma ordem suficiente não tiver sido executada. Comece com leitura e evidência; não use uma tentativa de envio como teste de conectividade. A palavra “liberação” não identifica sozinha a camada defeituosa.

### 1. Confirmar o ambiente efetivo

1. Resolver o perfil ativo e seu `HERMES_HOME`, workspace, conta de saída e conversa de comando. Uma pasta do Mac não altera automaticamente a VPS.
2. Identificar a release realmente apontada pelo serviço, não apenas um ZIP preparado ou código em outra pasta.
3. Consultar saúde por cliente autenticado e guardar somente status, capacidades e hash do código. Serviço conectado não prova autorização por tarefa.
4. Conferir que a conta pessoal permanece somente para monitoramento e grupos não receberam saída.
5. Usar `read_file` e `search_files` para o inventário pertinente; não imprimir `.env`, cookies, sessão, tokens ou banco bruto.

O script `scripts/diagnostico.py` é opcional e somente leitura. Recebe caminhos explícitos ou o perfil ativo e consulta apenas saúde/pendências; projeta campos seguros. Não chama a fila de recebimento do gateway, não envia, não prepara prévia e não renova fonte.

### 2. Separar recebimento, compreensão e autoridade do áudio

Se o Hermes parou de ler notas de voz:

1. Confirmar que o transporte recebeu a mensagem e baixou os bytes.
2. Verificar se a transferência entre cache privado e adaptador está usando a referência opaca autenticada e validando hash/tamanho.
3. Investigar rejeição de caminho, expiração da referência, tipo de áudio, falta de bytes ou limite de memória. Não afrouxar a validação de caminhos para fazer a leitura passar.
4. Confirmar a transcrição para compreensão pelo gateway.
5. Separadamente, confirmar o worker protegido que pode produzir a fonte de execução. O primeiro transcritor funcionar não prova que o segundo registrou a ordem.

Se houver nomes errados, conferir o vocabulário protegido e os contatos já identificados. Não corrigir telefone, criar alias fonético permanente ou transformar o palpite do modelo em autenticação. Uma assinatura literal precisa conservar o contrato do ditado.

### 3. Verificar a passagem fonte → tarefa

Se a resposta disser “a ferramenta exige uma tarefa já registrada”:

1. Consultar tarefas e fontes admitidas pela ferramenta de pendências.
2. Distinguir a ordem atual de `latestTask` consumida por teste anterior.
3. Verificar se há preparação nova, prévia confirmada, aprovação contextual ou ditado pendente, conforme o tipo de pedido.
4. Conferir se a origem é nova, do titular, recente e não encaminhada/citada/eco/grupo.
5. Examinar o parser da versão ativa: uma gramática ancorada apenas no início pode perder ordens no meio/fim de um áudio compreendido pelo modelo.
6. Conferir se o comando direto pode ser concluído nativamente. A falta de uma chamada do modelo não deve impedir uma tarefa literal já validada pela ponte.
7. Se houver fonte/tarefa, executar somente sua referência válida. Se não houver, registrar somente a ausência de referência executável; a lista vazia não identifica sozinha a causa; não pedir ao titular um ID administrativo nem repetir autorização clara.

Não registrar uma tarefa a partir da transcrição escrita pelo modelo. Não enviar telefone/texto novos por um cliente genérico para fabricar consentimento. Uma restauração administrativa de rascunho histórico é restauração de dados, não autorização nova.

### 4. Conferir as ferramentas efetivamente carregadas

Se o plugin foi atualizado mas a sessão só encontra o teste antigo ou ferramentas incompletas:

1. Comparar os esquemas registrados pelo plugin com o catálogo fixado na conversa em execução.
2. Conferir os cinco nomes de ferramentas e seus contratos. Não confundir a descrição em TOOLS com o esquema realmente oferecido ao modelo.
3. Examinar o vínculo do perfil e da sessão; não mudar de perfil ou conta para encontrar uma ferramenta com mais acesso.
4. Não inventar nomes de ferramentas nem acrescentar campos como destino ou aprovação a um esquema que só aceita referência.
5. Uma ferramenta encontrada é somente capacidade; ainda é necessária a fonte atual e válida da tarefa.

### 5. Conferir política atual versus snapshot da conversa

Se o agente reconhece o ditado e o contato, mas cita “envio somente ao titular”:

1. Comparar a política administrativa atual com o trecho realmente carregado na conversa.
2. Verificar simultaneamente o snapshot do prompt e o pin de ferramentas. Arquivo novo e reinício do serviço podem não mudar nenhum desses dois registros da conversa antiga.
3. Distinguir uma frase histórica/condicional de um bloqueio ainda vigente. Não anunciar que a habilitação técnica falta quando a release ativa já a implementa.
4. Preservar o cache e o histórico por padrão. Uma nova skill pode ser lida por `skill_view` sem reconstruir toda a conversa.
5. Se a própria causa for um snapshot obsoleto, usar a recarga nativa com aplicação imediata quando disponível e explicitamente autorizada. Caso contrário, preparar correção administrativa mínima da conversa do titular: apontadores/versões exatos, comparação antes de escrever, backup privado, mesmas mensagens e mesmas ferramentas não relacionadas.
6. Não apagar o histórico, resetar todas as sessões, alterar o provedor ou impor uma conversa nova como remédio universal. Também não permitir que o agente reescreva seus controles protegidos para se autorizar.

Mudanças de contexto podem invalidar cache de prompt e ter custo; não repetir a migração a cada turno. O procedimento administrativo é excepcional, dirigido à evidência de desatualização, não uma função cotidiana da skill.

### 6. Conferir efeito, identidade canônica e incerteza

Se a tarefa existe mas não há confirmação:

1. Consultar estado, validade, pausa e revogação.
2. Conferir transporte pronto, resolução de destinatário e guarda final imediatamente antes do efeito, inclusive depois da fila.
3. Conferir ID esperado, ID retornado e destinatário canônico confirmado. Um retorno incompleto não autoriza declarar enviado.
4. Em timeout/desconexão, reconciliar pelo mesmo ID. Não produzir outra tarefa, nonce ou mensagem para “tentar novamente” sem resolver a incerteza.
5. Preservar o banco atual. Restaurar um banco antigo depois de envio real pode apagar o comprovante e permitir duplicidade.

### 7. Conferir acompanhamento separado do envio inicial

Se o primeiro envio funcionou mas a sequência não:

1. Conferir se a ordem original autorizou condição, resposta, quantidade e bloqueio, e se esses campos foram admitidos no plano.
2. Conferir se a resposta é do contato correto, recente e vinculada ao primeiro envio quando citada.
3. Conferir prazo, estado, pausa, revogação, reivindicação transacional e fila.
4. Conferir a resposta literal realmente enviada; não entregar ao modelo a conversa do contato para ele inventar continuidade.
5. Conferir suporte e resultado do bloqueio antes de afirmar conclusão. Enviar, agradecer e bloquear são três efeitos com evidências distintas.

### 8. Aplicar a correção mínima autorizada

Antes de manutenção operacional:

1. Nomear a causa observada e o arquivo/componente que a implementa.
2. Preservar o estado anterior necessário, sem exportar segredos. Comparar a linha de base com o sistema ativo antes de usar um backup antigo.
3. Preparar a diferença, testes e reversão. Alterar a etapa defeituosa, não a identidade do titular ou as barreiras do serviço.
4. Rodar negativos em ambiente isolado com dados sintéticos e sem sessão real.
5. Aplicar somente pelo executor e acesso já autorizados. Não conceder sudo, desativar aprovação, montar pastas secretas ou abrir a ponte na rede para resolver um erro de interpretação.
6. Se uma tarefa/fluxo válido estiver em curso, preservar sua execução ou adiar a troca; não interromper sem necessidade.
7. Em falha parcial, retornar a uma versão conhecida com recibo, mantendo tarefas e efeitos atuais. Padrões antigos de marcadores em TOOLS devem ser cobertos pela migração e por teste antes de nova tentativa.
8. Conferir versão carregada, serviços, controles e backups remotos. Mensagem real de validação exige pedido específico do titular; instalar documentação não é esse pedido.

## Comunicação útil diante de falha

Informe: o que foi reconhecido; qual etapa não foi comprovada; a causa observada; o que pode ser corrigido dentro do acesso atual; qual dado ou operação administrativa realmente falta. Não dizer “falta autorização” quando a origem já é válida, “precisa repetir o número” quando ele já foi identificado, ou “áudio não funciona” quando o problema é apenas o registro da tarefa.

## Gramática e término na RC9.1

Em `UNSUPPORTED_FOLLOWUP` ou controles incluídos no literal, conferir `ownerFollowupSpeechProtocol`, hash e versão; seguir [acompanhamento falado e término](rc9-1-e-semantica-do-termino.md). Não inferir conserto do decoder por uma reprodução textual pura. A capacidade anunciada também não garante aceitação de qualquer frase.
