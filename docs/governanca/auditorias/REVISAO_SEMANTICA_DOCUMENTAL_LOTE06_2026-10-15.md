# Revisão semântica documental — Lote 06: contratos de governança e auditorias de workflows

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-006 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; SNAPSHOTS_HISTORICOS_PRESERVADOS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação final de governança quando aplicável |
| **Origem** | Inspeção de conteúdo, critérios, resultados e limites de 15 documentos |
| **Autoridade superior** | [Carta Magna B3](../../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Incidente histórico COTAHIST 1999, inventário/plano documental e auditorias FASE04–FASE05.5 |
| **Objetivo** | Separar resultados históricos de estado atual, validar o sentido dos gates e registrar riscos de interpretação |
| **Dependências** | Matriz de conformidade de workflows, evidências GitHub Actions citadas e Issue #11 |

## 1. Resultado executivo

Foram revistos 15 documentos. Os relatórios FASE04–FASE05.5 são snapshots de auditorias e correções realizadas principalmente em 2026-10-01, com atualizações de metadados em 2026-10-15. Os seus números (108 ou 109 workflows, 104 divergentes, 84 observações de STEP_SUMMARY, etc.) devem ser lidos com a data e o commit auditado de cada relatório. Não são métricas atuais sem uma nova execução e não devem ser consolidados numa única contagem atemporal.

O conteúdo reforça corretamente que uma divergência estrutural do auditor não é automaticamente defeito funcional; que os workflows históricos não devem ser reabertos para satisfazer um detector estático; e que a ausência de evidência/observabilidade não certifica os dados. O relatório de incidente COTAHIST 1999 regista uma recuperação determinística e uma igualdade de hash para a versão descrita, mas isso não certifica outros anos nem substitui a revisão independente da proveniência RAW.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| `docs/CARTA_INCIDENTE_INTEGRIDADE_COTAHIST_1999_V1.md` | Carta/registo de incidente histórico | Regista ausência do NORMALIZED, divergência inicial e recuperação posterior com hash/contagem/data coincidentes com o manifesto citado. A narrativa separa a falha original da recuperação. | Preservar cronologia e valores históricos; qualquer incidente novo entra como adenda versionada. Não extrapolar a recuperação de 1999 para outros anos. |
| `docs/governanca/INVENTARIO_MATRIZ_CONFORMIDADE_DOCUMENTAL_B3_V1.md` | Inventário e relatório de conformidade | Declara explicitamente que o inventário estrutural não é auditoria de conteúdo. Inclui vários resultados históricos e contagens sucessivas. | Manter como histórico de auditoria; a matriz semântica integral é a fonte atual do estado por documento. Não tratar números antigos como baseline atual. |
| `docs/governanca/PLANO_NORMALIZACAO_DOCUMENTAL_GOVERNANCA_V1.md` | Plano de normalização documental | As secções antigas preservam contagens e estados históricos; as atualizações finais distinguem conformidade estrutural de revisão semântica. | Preservar histórico; atualizar apenas a secção corrente e a referência à matriz/Lotes 05–06. |
| `docs/governanca/auditorias/FASE04_AUDITORIA_WORKFLOWS_LAYOUT_MESTRE_V1.md` | Plano/relatório de auditoria estrutural | FASE04 declara que não altera nem reexecuta workflows e que a auditoria estrutural não promove workflows. O inventário de 108 ficheiros é temporal. | Usar como evidência histórica da metodologia; consultar matriz e execução atuais para estado presente. |
| `docs/governanca/auditorias/FASE05_2_CLASSIFICACAO_FUNCIONAL_WORKFLOWS_B3_V1.md` | Classificação funcional nominal | Declara 109 workflows classificados por nome e admite que nome não prova responsabilidade funcional. | Não inferir conformidade funcional a partir da classificação nominal. |
| `docs/governanca/auditorias/FASE05_3_VALIDACAO_HISTORICOS_CASOS_AMBIGUOS_V1.md` | Validação de workflows históricos/ambíguos | Declara 81 workflows históricos e afirma que inventário por nome/ano não certifica correção funcional. Preserva a não reabertura de cadeias históricas. | Manter a regra de somente leitura para cadeias fechadas; novas correções apenas em versões controladas e com autorização. |
| `docs/governanca/auditorias/FASE05_4_CLASSIFICACAO_SEMANTICA_MATRIZ_CONFORMIDADE_WORKFLOWS_B3_V1.md` | Matriz semântica de workflows | Distingue observabilidade de defeito funcional e explica que 5/104 é resultado de critérios estruturais limitados. A data de referência é 2026-10-01. | Não apresentar 104 divergências como contagem atual; referenciar a data, commit e regras do auditor. |
| `docs/governanca/auditorias/FASE05_5_CASOS_ESPECIAIS_V1.md` | Auditoria de casos especiais | Reporta 108 workflows no snapshot de 2026-10-01 e zero divergências críticas, dentro do escopo do auditor então utilizado. | Interpretar como evidência histórica limitada ao detector e commit identificados; não generalizar para a árvore atual. |
| `docs/governanca/auditorias/FASE05_5_CORRECOES_GRUPO_01_OBSERVABILIDADE_ATIVOS_V1.md` | Registo de correções de observabilidade | Documenta inclusão de GITHUB_STEP_SUMMARY e preservação dos workflows históricos; o texto exige validação pós-correção pelo GitHub Actions. | A conclusão local “pronta para validação” não equivale a aceitação operacional; usar execução posterior específica como prova. |
| `docs/governanca/auditorias/FASE05_5_GRUPO_02_TRIGGERS_V1.md` | Validação de triggers | Regista 109/109 nos checks de trigger para o commit/run referenciado e exceção explícita do workflow que consolida README. | Resultado válido para aquele commit e checks; não significa que todos os restantes grupos estejam conformes. |
| `docs/governanca/auditorias/FASE05_5_GRUPO_03_ISOLAMENTO_DIRECIONALIDADE_V1.md` | Validação de isolamento | Regista zero falhas nos sinais direcionais para a matriz auditada e separa observações não bloqueadoras. | Preservar exceções e âmbito do detector; não usar como autorização para reexecutar fases históricas. |
| `docs/governanca/auditorias/FASE05_5_GRUPO_04_PERMISSOES_V1.md` | Validação de permissões | Regista uma exceção histórica na FASE00/1994, sem falhas críticas/altas no snapshot. | Não alterar retroativamente a cadeia fechada; qualquer melhoria deve ser uma versão nova controlada. |
| `docs/governanca/auditorias/FASE05_5_GRUPO_05_PERSISTENCIA_DECISAO_V1.md` | Validação de persistência/decisão | Regista zero divergências críticas/altas, mas mantém observações de idempotência, persistência e STEP_SUMMARY. | Distinguir ausência de bloqueador crítico de conformidade total; as observações devem continuar rastreáveis. |
| `docs/governanca/auditorias/FASE05_5_GRUPO_06_IDEMPOTENCIA_V1.md` | Validação de idempotência | Regista correção do fluxo BVBG.028.02 e uma exceção histórica de FASE00/1994. | Tratar a conclusão como resultado da versão auditada; preservar a cadeia histórica e verificar novos incidentes de persistência separadamente. |
| `docs/governanca/auditorias/FASE05_CLASSIFICACAO_DIVERGENCIAS_WORKFLOWS_V1.md` | Classificação inicial de divergências | Declara explicitamente que os 104 divergentes eram sobretudo observabilidade no auditor inicial e não certificação funcional. | Manter como fotografia diagnóstica histórica; não converter o estado antigo em estado atual. |

## 3. Achados semânticos transversais

### SEM-06-01 — contagens de auditoria dependem de snapshot

**Fato observado:** os relatórios citam snapshots de 108 ou 109 workflows e commits diferentes. Isso é compatível com evolução temporal do repositório, mas as contagens não podem ser comparadas sem normalizar data, commit, universo e versão do auditor.

**Decisão:** conservar cada resultado com o respetivo run/commit. A matriz semântica atual, e não a tabela histórica de uma auditoria anterior, controla o estado corrente da revisão de conteúdo.

### SEM-06-02 — detector estrutural não equivale a defeito funcional

**Fato observado:** vários documentos distinguem ausência de STEP_SUMMARY, sinais de decisão e padrões de idempotência de falhas funcionais efetivas. Também registam exceções históricas.

**Decisão:** não promover nem reprovar workflow exclusivamente por uma etiqueta do detector sem analisar o contrato funcional e a evidência. A decisão normativa GOV-DIV-001 determina reconciliação por domínio e tratamento versionado.

### SEM-06-03 — imutabilidade histórica

**Fato observado:** os contratos de auditoria proíbem reabrir cadeias históricas fechadas apenas para satisfazer uma auditoria posterior.

**Decisão:** preservar COTAHIST 1986–2025 em consulta/read-only e manter 2026 incremental diário. Este lote não altera RAW, NORMALIZED, sidecars, manifests, workflows ou evidências de máquina.

### SEM-06-04 — incidentes e correções posteriores

**Fato observado:** a carta de COTAHIST 1999 descreve uma recuperação específica e o grupo de idempotência descreve uma correção específica no catálogo BVBG.028.02. Relatórios posteriores de 2026-10-15 voltam a registar colisões concorrentes de escrita.

**Decisão:** as correções antigas não resolvem automaticamente incidentes novos. As corridas de escrita de 2026-10-15 devem ser tratadas como incidente próprio, com causa, commit, regressão e evidência; sem alterações artificiais a dados para forçar correspondência.

## 4. Conclusão

O conteúdo dos 15 documentos foi revisto e classificado. Não foram alterados workflows nem dados. Os documentos são úteis como evidência histórica/metodológica, mas vários números são snapshots antigos e devem ser citados com o run/commit correto.

COTAHIST 1986–2025 permanece somente para consulta; 2026 continua incremental diário; a proveniência RAW permanece uma frente separada. `BLOOMBERG_MAIL` continua isolado e fora do escopo operacional B3.

## 5. Referências

- [Matriz integral de revisão semântica](MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Plano Mestre de Execução](../../PLANO_MESTRE_DE_EXECUCAO.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
