# Revisão semântica documental — Lote 05: WATCHDOG e Wiki operacional

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-005 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; ACOES_DE_SEGUIMENTO_ABERTAS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — revisão de conteúdo registada; aceitação operacional continua separada |
| **Origem** | Inspeção direta dos 12 documentos listados neste lote |
| **Autoridade superior** | [Carta Magna B3](../../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Revisão de conteúdo operacional WATCHDOG e Wiki; sem alteração de RAW, dados, limiares ou secrets |
| **Objetivo** | Validar o sentido dos documentos, separar factos atuais de históricos e identificar contradições/ações necessárias |
| **Dependências** | Issue #11; Issue #8; workflows e artefactos citados nos documentos; matriz semântica integral |

## 1. Resultado executivo

Foram inspecionados 12 documentos: sete documentos WATCHDOG e cinco páginas da Wiki. A revisão confirma que os documentos WATCHDOG, em geral, distinguem corretamente sucesso de execução de saúde dos dados e mantêm explícitas as pendências de heartbeat externo, aprovação dos limiares, ACK/escalonamento e retenção duradoura. A documentação não autoriza declarar a Fase C concluída.

A revisão encontrou **dívida de atualidade documental**, não uma autorização para mudar configurações operacionais: alguns relatórios citam execuções e contagens de falhas de janelas anteriores; esses números são evidência histórica, não estado atual automático. Devem ser preservados como fotografia temporal e complementados por um registo posterior, nunca reescritos como se os novos resultados fossem contemporâneos.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| `WATCHDOG/FASE_C_FECHAMENTO_OPERACAO_GOVERNANCA_2026-10-15.md` | Relatório de auditoria operacional | Coerente ao manter a Fase C aberta e separar execução bem-sucedida de aceitação operacional. Identifica heartbeat, limiares, ACK/escalonamento e retenção como pendências. | Manter EM_CURSO até evidência de secrets configuradas, teste externo, aprovação de limiares, política de alertas e aceitação humana. |
| `WATCHDOG/README.md` | Manual/estado operacional | Correto ao explicar que PASS de atualidade não certifica qualidade de negócio e que artefactos de 30 dias não são arquivo imutável. Valores 8 PASS/0 STALE/0 UNKNOWN são resultado da execução referenciada, não garantia permanente. | Tratar as contagens como históricas; atualizar o estado operacional somente após consultar uma nova execução e preservar a referência anterior. |
| `WATCHDOG/REGISTO_CORRECOES_PERSISTENCIA_COTAHIST_2026-10-15.md` | Registo de correções/incidentes | Distingue adequadamente persistência demonstrada em alguns fluxos da proveniência RAW ainda não reconciliada. Não deve ser lido como certificação global. | Preservar os registos de runs; acrescentar novos eventos versionados para as corridas de escrita observadas posteriormente. Não modificar RAW/sidecars/manifests para forçar hashes. |
| `WATCHDOG/TRIAGEM_EXECUCOES_DESFAVORAVEIS_2026-10-15.md` | Triagem preliminar de incidentes | O documento afirma explicitamente que a triagem é parcial, separa classes de falha e exige reconciliação de hashes físicos. As 12 execuções desfavoráveis pertencem à janela indicada no próprio texto. | Não tratar a lista histórica como contagem atual. Acrescentar atualização com causas/commits/regressões por ocorrência; manter Issue #11 aberta até todas as causas terem estado final e evidência. |
| `WATCHDOG/VERIFICACAO_REGRESSO_E_EVIDENCIAS_2026-10-15.md` | Relatório de regressão | Coerente ao não promover Fase C/D com base em workflows verdes. Contagens de runs e cabeçalhos são snapshots anteriores à normalização final e não devem ser usados como estado atual. | Manter como histórico; publicar relatório de regressão novo para o estado corrente e reconciliar incidentes de concorrência de escrita. |
| `WATCHDOG/heartbeat-supervisor-externo.md` | Runbook de supervisão | O desenho exige duas URLs distintas, timeout, teste de ausência e verificação de alerta/escalonamento. O texto não afirma que o serviço externo já está ativo. | Não alterar nem preencher secrets neste lote. A ativação depende de configuração real no GitHub e evidência do serviço externo, que não é visível no conteúdo público do repositório. |
| `WATCHDOG/limiares-provisorios-revisao.md` | Registo de decisão humana pendente | A matriz de oito controlos mantém decisões e proprietários pendentes e proíbe remover PROVISIONAL apenas porque um workflow passou. Sem autoridade sobre o contexto de negócio não se pode aprovar os valores por inferência. | Manter todos os limiares provisórios até aprovação explícita por controlo, com proprietário, data e justificação. |
| `WIKI/00-INICIO/ESTADO_ATUAL.md` | Resumo de estado | Critérios de estado e regra de não certificar apenas por aquisição são coerentes. A data de referência 2026-09-29 está desatualizada face às alterações de 2026-10-15. | Atualizar o resumo numa alteração própria, citando o roadmap atual e a auditoria documental; não apagar a data histórica sem registar a nova referência. |
| `WIKI/00-INICIO/VISAO_GERAL.md` | Visão geral de âmbito | Escopo (COTAHIST, dados B3, macro, microestrutura, pipelines, backtests) e princípio de proveniência são coerentes. Não declara certificação dos datasets. | Sem correção substantiva necessária; manter como documento de visão e não como fonte operacional de gates. |
| `WIKI/01-GOVERNANCA/MODELO_DE_GOVERNANCA.md` | Modelo de governança explicativo | A cadeia aquisição → RAW → normalização → validação → evidência → publicação → consumo e as regras de não sobrescrever RAW são coerentes com a governança atual. | Atualizar referência de autoridade para explicitar Carta Magna v1.3.0 e Layout Mestre v1.1.0, sem atribuir ao modelo poder normativo próprio. |
| `WIKI/01-GOVERNANCA/POLITICA_DE_EVIDENCIAS.md` | Política explicativa de evidências | Escala E0–E4 e distinção facto/hipótese/inferência/opinião são coerentes. A exigência de E3/E4 é apresentada como preferência (“sempre que possível”), não como gate universal. | Não elevar a preferência a requisito obrigatório sem decisão versionada; manter as classificações epistemológicas explícitas. |
| `WIKI/02-ARQUITETURA/ARQUITETURA_GERAL.md` | Descrição arquitetural | A separação de fontes, aquisição, RAW, normalização, validação e auditoria é coerente. É uma visão de alto nível, não prova de que todos os módulos ou testes estejam ativos. | Manter a limitação explícita; alterações de estado devem apontar para evidências operacionais específicas. |

## 3. Achados e decisões

### SEM-05-01 — snapshots operacionais históricos

**Achado:** os relatórios datados citam runs, contagens de falhas e resultados de atualidade de janelas específicas. A data de publicação/atualização do ficheiro não torna esses dados automaticamente atuais.

**Decisão:** preservar os documentos como evidência histórica. Para estado corrente, acrescentar novo relatório com janela, consulta e runs explícitos; não reescrever a narrativa anterior.

### SEM-05-02 — estado desatualizado na Wiki

**Achado:** `WIKI/00-INICIO/ESTADO_ATUAL.md` mantém data de referência 2026-09-29, anterior ao roadmap e auditorias de 2026-10-15.

**Ação:** atualização documental requerida, com referência cruzada ao [Plano Mestre](../../PLANO_MESTRE_DE_EXECUCAO.md) e à [Issue #11](https://github.com/carlos-andrade/B3/issues/11). O conteúdo antigo deve permanecer recuperável no Git.

### SEM-05-03 — nenhuma aprovação operacional inferida

**Achado:** os limiares estão PROVISIONAL; o heartbeat externo depende de secrets e endpoint independente; ACK/SLA/escalonamento e retenção duradoura permanecem pendentes.

**Decisão:** nenhuma alteração de configuração é autorizada por esta revisão semântica. A aceitação operacional continua a exigir evidência externa e aprovação humana.

### SEM-05-04 — limite de certificação de dados

**Achado:** relatórios de persistência documentam êxito de fluxos específicos, mas mantêm aberta a proveniência RAW e a reconciliação de hashes físicos por ano.

**Decisão:** não declarar certificação global; não alterar RAW, sidecars, manifests ou histórico COTAHIST para fazer os valores coincidirem.

## 4. Conclusão e estados

O conteúdo dos 12 documentos foi revisto. A classificação semântica deste lote está concluída com ações de seguimento explícitas. Isto **não** encerra a Fase C WATCHDOG nem certifica dados COTAHIST, nem substitui a revisão dos restantes documentos.

- Fase C WATCHDOG: EM_CURSO.
- Fase D/proveniência RAW: PENDENTE de reconciliação independente.
- Limiares: PROVISIONAL, aprovação humana pendente.
- Heartbeat externo: PENDENTE de configuração e teste.
- Issue #11: manter aberta enquanto houver incidentes ou ações sem evidência final.
- COTAHIST 1986–2025: somente consulta/read-only; 2026: atualização diária.
- `BLOOMBERG_MAIL`: fora do escopo semântico operacional deste projeto; referências existentes são apenas controlo de fronteira e não autorizam integrar o projeto.

## 5. Referências

- [Plano de fecho da Fase C](../../WATCHDOG/FASE_C_FECHAMENTO_OPERACAO_GOVERNANCA_2026-10-15.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
- [Issue #8](https://github.com/carlos-andrade/B3/issues/8)
- [Matriz integral de revisão](MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
