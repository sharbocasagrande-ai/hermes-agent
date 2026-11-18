# RC10 candidato: missão, agenda e aceite

Revisão 2026-11-18. Produção observada: RC9.1. O candidato não está implantado. Não confundir resultado isolado, código carregado e efeito no canal real.

## O que muda

A missão conserva a fonte nativa, corpo/objetivo, identificação, versão e prazo de cinco minutos. A consulta autenticada ao Composio usa somente o nome da missão, agenda fixa e telefone canônico da fonte CONTACT. Homônimos exigem seleção nativa; correção curta só na identificação vinculada. O modelo não injeta destino/prova/aprovação. A preparação fica fixa ao alvo. A prévia contém nome, número, texto e escopo; a confirmação composta só vale no plano atual. O prazo do plano nunca ultrapassa o da missão.

`whatsapp_resolver_missao` recebe apenas `mission_id`. Só usar após confirmar o sexto contrato no plugin e `ownerMissionProtocol=1` / `ownerContactProviderProtocol=1` na ponte ativa. O estado minimizado da missão não é comprovante de envio. Preparação de texto a compor usa o mecanismo existente; não chamar envio livre. Em falha OAuth, a conexão normal do Hermes mantém a renovação e pode preceder uma única tentativa protegida, dentro do prazo; não criar gerenciador paralelo ou copiar refresh token.

## Integração proposta

O serviço WhatsApp conserva o sandbox existente. Um leitor local separado executa sob o proprietário da credencial, sem rede, com código administrativo imutável, fonte read-only e socket Unix com verificação Linux de identidade do cliente. Projeta somente o access token vigente e sua expiração; não exporta refresh, grava nova credencial, escolhe ferramenta ou altera ACLs da credencial. O cliente protegido consulta HTTPS Composio fixo e a conta de contatos fixada pelo administrador. Mudanças de arquivo atômicas são lidas novamente. Expiração ou revogação falham sem envio.

O leitor é componente novo e exige implantação administrativa do pacote concreto. Sua existência no pacote não comprova serviço ativo. Preservar sessão, comando exclusivo, conta pessoal de monitoramento, grupos desabilitados e banco atual de efeitos. Reversão restaura código/contexto por comparação, nunca um banco antigo sobre comprovantes novos.

## Evidência e limites

As 12 sondagens do relatório de 17/11 foram reproduzidas na base de hashes coincidentes com a RC9.1. O candidato passou em testes Linux isolados de missão, voz, provider, HTTP/SDK fictício e credencial local. As contagens e hashes pertencem ao relatório de evidências daquele pacote, sem garantia de linguagem natural universal. A instalação não envia mensagens de teste. Aceite no canal real aguarda nova ordem do titular, sem retomar missões de destinatários anteriores ou exemplos históricos automaticamente.

A orientação de encerrar respostas sem bloquear pessoa é permanente; na RC9.1 o parser genérico ainda pode bloquear. No candidato, somente bloquear o contato/a pessoa habilita esse efeito. Não declarar desbloqueio histórico ou cancelamento por editar a skill.
