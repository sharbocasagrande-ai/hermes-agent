# Validação, evidência e restauração

## Separar os níveis de prova

| Nível | O que comprova | O que não comprova |
|---|---|---|
| Leitura de arquivo/skill | Conteúdo salvo e acessível | Regra carregada na sessão ou efeito externo. |
| Teste unitário | Contrato da unidade testada | Serviço ativo, transporte e dados reais. |
| Ponte HTTP/Unix com SDK fictício | Caminho integrado, guardas e efeitos simulados | Entrega real no WhatsApp. |
| Decodificar áudio real com banco/provedor temporários | Worker e parser daquele áudio | Novo pedido espontâneo pelo gateway após instalar. |
| Estado `sent` e ID do SDK | Integração aceitou aquele efeito | Leitura humana ou toda sequência de respostas. |
| Titular relata teste de áudio bem-sucedido | Evidência de uso real declarada pelo titular | Auditoria independente do host ou prova de todos os fluxos. |
| Recibo de entrega/leitura | Etapa específica do transporte, quando disponível | Consentimento para nova conversa. |

Nunca usar um envio administrativo realizado de outro canal como substituto do teste pelo áudio original do titular. Não afirmar que testes ou skill impedem todos os erros futuros.

## Aceite por cenário

Execute os cenários pertinentes à alteração. Os negativos usam dados sintéticos, armazenamento temporário e transporte fictício, nunca mensagens adversas em produção.

1. Ordem literal do titular para contato identificado: um único envio fiel, sem confirmação repetida.
2. Número completo novo: destino fixado sem cadastro administrativo nem adição à entrada de comandos.
3. Nome ambíguo/desconhecido: pedir apenas identificação essencial; nenhum palpite de telefone.
4. Áudio direto: bytes originais, reconhecimento, tarefa e execução pelo mesmo caminho protegido, sem chamada obrigatória do modelo quando o corpo está delimitado.
5. Áudio com ordem no meio/fim: fonte de ditado correta; escolha literal validada, sem texto inventado ou instruções de acompanhamento no corpo inicial.
6. Mesmo áudio/mesma origem repetidos: conservar tarefa/comprovante e não duplicar efeito. Bytes alterados sob o mesmo ID são conflito.
7. Rascunho e aprovação contextual: só a prévia confirmada correspondente pode ser enviada; edição revoga o envio pendente.
8. Teste anterior consumido: não representar uma nova ordem nem impedir seu novo registro legítimo.
9. Sem acompanhamento: nenhuma resposta automática após o contato responder.
10. Condição exata: somente resposta compatível do destinatário vinculado aciona o literal autorizado.
11. Primeira resposta autorizada: conteúdo adverso pode, no máximo, satisfazer esse gatilho; nunca autorizar comandos, dados, outros contatos ou memória.
12. Concorrência de respostas: um único efeito de resposta e bloqueio, se autorizado.
13. Bloqueio: somente se pedido, suportado e confirmado pelo transporte; ausência da capacidade impede prometer a sequência.
14. Pausa/revogação/expiração: revalidar após a fila e imediatamente antes do efeito; nada se rearma por resposta tardia.
15. Timeout/resultado incompleto/reinício durante efeito: estado incerto ou revogado, sem repetição automática.
16. Grupo, terceiro, eco, encaminhamento, citação incompatível ou histórico: não geram nova autorização.
17. HTTP adulterado: campos extras, troca de destino/corpo, transcrição do cliente ou flag de aprovação não criam tarefa.
18. Snapshot antigo: identificar política e pin da conversa, corrigir só o escopo autorizado e preservar histórico/ferramentas não relacionadas.
19. Migração de documentação: suportar marcadores antigos reais, idempotência e retorno seguro em falha.
20. Permissões: mesmo titular, mesmas contas/ACLs, política e sessão inacessíveis ao usuário operacional, sem nova saída da conta pessoal ou de grupos.

As contagens de testes são evidência datada da versão correspondente, não uma meta fixa nem garantia universal. O registro da instalação preserva a versão, suíte executada, hashes, ambiente, resultado e limites.

## Teste real

1. Usar somente pedido específico atual do titular para destinatário e conteúdo definidos. Não aproveitar os exemplos da documentação.
2. Iniciar pelo canal real escolhido: no caso de áudio, nota de voz do WhatsApp autenticado.
3. Observar fonte/tarefa e comprovante dessa mesma ordem.
4. Confirmar com o titular somente a recepção/resultado que ainda não puder ser observado; não pedir de novo autorização já suficiente.
5. Testar resposta/bloqueio apenas se também solicitados. Um primeiro envio bem-sucedido não comprova essas etapas.
6. Registrar a evidência mínima privada, sem copiar voz, conversa inteira ou credenciais para o repositório.

## Backup antes de alterar

Preservar skill anterior, documentos atingidos, manifesto/hash e recibo. Snapshot completo de sessão/bancos para recuperação, quando necessário à manutenção, fica em área administrativa privada da VPS. Exportação de configuração exclui `.env`, tokens, cookies, QR, sessões, áudio, transcrições privadas, USER e histórico bruto.

Comparar hashes da configuração ativa antes de reutilizar um backup remoto como linha de base. Registrar se uma cópia histórica foi reconstruída de arquivos preservados, em vez de afirmar que era um snapshot integral do passado.

Código e skills vão ao repositório adequado, preservando licença, recursos e histórico. Se o repositório for público, publicar apenas material técnico sem dados privados. O registro da instalação e comprovantes privados vão ao destino privado autorizado. Confirmar o commit/blob remoto e, para arquivos do Drive, conteúdo/versão ou checksum remoto, conforme o formato.

## Reversão segura

1. Suspender somente novos efeitos abrangidos e identificar tarefas em curso.
2. Conferir o recibo e os hashes antes de restaurar arquivos; divergência posterior exige revisão do conflito.
3. Retornar código/plugin/documentos ao estado anterior conhecido pelo mecanismo administrativo aprovado.
4. Preservar a sessão mais recente e o banco atual de tarefas. Não restaurar banco anterior sobre efeitos reais já ocorridos.
5. Não desfazer ou apagar mensagens como consequência automática de rollback.
6. Religar somente os serviços identificados; confirmar saúde e controles. Não deixar o gateway parado ao encerrar uma manutenção documental.
7. Registrar versão, estado de cada efeito, motivo e pendências. Preservar a release substituída para recuperação.

## Manutenção da skill

Atualizar uma única skill canônica no perfil efetivo. `skills` não é uma subpasta de `workspace`; uma cópia no workspace não substitui a skill descoberta pelo Hermes. Verificar por `skills_list` e `skill_view`, incluindo as referências necessárias. Não declarar a skill carregada só porque o arquivo foi escrito.

Preservar o cache de conversa por padrão. Atualizar instruções de encaminhamento para a skill nos documentos efetivos, sem apagar o histórico ou alterar o catálogo de ferramentas em uma revisão meramente documental. Se houver curadoria automática já configurada, uma fixação explícita da skill pode protegê-la de arquivamento; isso não cria agenda, rotina ou novo agente.
