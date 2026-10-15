# B3 — Registo de aplicação da GOVERNANCA na Fase C

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REG-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | REGISTO_DE_GOVERNANCA |
| **Fase** | FASE_C_OPERACAO_E_GOVERNANCA |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 44f007d85e5fd928bd9c511d5c9c8274245bc8191c493b472a750412dcefb74e |
| **Commit de referência (versão anterior)** | N/A — revisão inicial segundo a norma documental |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável operacional do projeto B3 |
| **Aprovador** | Pendente — não representa aprovação formal |
| **Origem** | Auditoria da Fase C, triagem técnica e normas centrais GOVERNANCA |
| **Autoridade superior** | [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md), [Norma de Cabeçalho v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md), [Carta WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objetivo

Registar a aplicação explícita, no projeto B3, das regras normativas do repositório central GOVERNANCA. Este documento é um registo local de adoção; não altera nem substitui a autoridade central.

## 2. Normas verificadas

Em 2026-10-15 foram consultadas as seguintes fontes públicas do repositório central:

- [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md): evidência antes de alegação; rastreabilidade; critérios mensuráveis; revisão humana onde necessária; integridade; ausência de dados não equivale a sucesso; supervisão independente WATCHDOG. O próprio documento mantém estado de proposta para revisão, pelo que não deve ser descrito como Constituição formalmente ratificada.
- [CABEÇALHO/NORMA-CABECALHO-PADRAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md), v1.0.3, estado APROVADO: título H1 e tabela Markdown de metadados obrigatórios; origem e autoridade; estado/versão/data; hash canónico distinto do Git blob SHA; commit de referência anterior; exceções justificadas.
- [WATCHDOG/CARTA-WATCHDOG.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md), estado EM_REVISAO: mandato operacional proposto; evidência, estado UNKNOWN quando a evidência é insuficiente, privilégio mínimo, separação entre deteção/notificação/remediação e supervisão independente. É padrão proposto, ainda não uma aprovação corporativa.

## 3. Regras locais obrigatórias para a Fase C

1. A norma central GOVERNANCA é a referência de desenho e documentação; qualquer conflito é registado e escalado, sem alterar a norma central a partir do repositório B3.
2. Não marcar um controlo como APROVADO/CONCLUIDO sem evidência, critério de aceitação, responsável e autoridade de decisão identificáveis.
3. Distinguir execução de workflow, qualidade dos dados, integridade de artefactos e aceitação operacional como afirmações diferentes.
4. Não remover o estado PROVISIONAL dos limiares de atualidade sem decisão explícita e justificação registadas.
5. Não fechar incidentes por mera execução posterior bem-sucedida; verificar impacto, causa, recuperação, artefactos e regressão.
6. A ausência de monitor, heartbeat, alerta ou dados é UNKNOWN/PENDENTE, nunca PASS.
7. Segredos, URLs privadas de heartbeat e tokens não podem ser registados em ficheiros versionados, issues públicas ou mensagens.
8. Manter cadeia RAW → validação → normalização → publicação, procedência e hashes. Não modificar dados/manifests para contornar gates.
9. Mudanças com risco sobre datasets históricos ou publicação têm validação, evidência e plano de recuperação antes de aceitar o resultado.
10. Todos os documentos Markdown novos devem seguir a Norma de Cabeçalho v1.0.3. Documentos anteriores podem ser corrigidos por lote, preservando o corpo, histórico e links; cada lote exige diff verificável.
11. O SHA-256 canónico indicado no cabeçalho deve ser calculado segundo a norma após o preenchimento do conteúdo, removendo apenas as duas linhas de controlo definidas pela norma. O commit deste registo é a referência de histórico Git, mas o próprio documento novo usa N/A como commit de referência anterior.
12. As decisões dependentes do proprietário são registadas como PENDENTE até decisão explícita; a execução técnica não substitui essa aprovação.

## 4. Estado de conformidade conhecido

| Elemento | Estado | Evidência / bloqueio |
|---|---|---|
| Referência à autoridade central GOVERNANCA | REGISTADO | Este documento e links normativos acima |
| Critérios de fecho da Fase C | EM_CURSO | [Plano de fecho](FASE_C_FECHAMENTO_OPERACAO_GOVERNANCA_2026-10-15.md) |
| Triagem de execuções desfavoráveis | PARCIAL | [Triagem técnica](TRIAGEM_EXECUCOES_DESFAVORAVEIS_2026-10-15.md), Issue #11 permanece aberta |
| Aprovação dos oito limiares | PENDENTE | [Matriz de limiares](limiares-provisorios-revisao.md) |
| Supervisão externa independente | PENDENTE | Secrets e testes externos não confirmados |
| ACK, responsáveis e escalonamento | PARCIAL | Runbook ainda carece de confirmação operacional |
| Evidência com retenção duradoura | PARCIAL | Artefactos atuais têm 30 dias; arquivo durável não foi aceite |
| Integridade/reconciliação COTAHIST | PENDENTE DE INVESTIGAÇÃO | Logs anteriores apresentam divergências de SHA físico/manifesto |
| Conformidade integral de todos os Markdown | NÃO CERTIFICADA | Requer auditoria por lotes e registo das exceções |

## 5. Ordem de execução retomada

1. Rever a falha da auditoria documental e corrigir apenas a causa confirmada por testes. A norma exige cabeçalho válido; o teste com `PENDENTE` deve ser reconhecido como pendente se as duas linhas de controlo estiverem presentes. Não aceitar o resultado `CABECALHO_CONTROLO_INVALIDO` sem verificar o ficheiro e o código.
2. Reconciliar divergências de SHA físicos/manifestos do COTAHIST antes de voltar a classificar esses datasets como íntegros.
3. Corrigir erro de tipo de data na composição de índices, com teste unitário e validação da fonte.
4. Investigar HTTP 400 na importação BVBG.028.02 com registo seguro de status, endpoint e formato de requisição.
5. Tornar a persistência do manifesto diário COTAHIST resistente a conflitos concorrentes, sem perda de dados nem force push.
6. Rever os oito limiares com a decisão do proprietário.
7. Configurar heartbeat externo, responsáveis/SLA, retenção de evidências e executar testes de aceitação.
8. Só depois, atualizar a matriz de controlos e decidir o encerramento da Fase C.

## 6. Referências do projeto B3

- [Plano de fecho da Fase C](FASE_C_FECHAMENTO_OPERACAO_GOVERNANCA_2026-10-15.md)
- [Triagem técnica das execuções desfavoráveis](TRIAGEM_EXECUCOES_DESFAVORAVEIS_2026-10-15.md)
- [Controlos obrigatórios do WATCHDOG](registry/controlos-obrigatorios.json)
- [Revisão de limiares](limiares-provisorios-revisao.md)
- [Guia heartbeat externo](heartbeat-supervisor-externo.md)
- [Issue #11 — Execuções desfavoráveis](https://github.com/carlos-andrade/B3/issues/11)

**Decisão atual:** a adoção explícita da referência GOVERNANCA fica registada; a Fase C continua EM_CURSO e não certificada.
