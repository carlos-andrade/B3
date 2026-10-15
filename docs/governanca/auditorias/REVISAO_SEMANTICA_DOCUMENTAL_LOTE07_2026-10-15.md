# Revisão semântica documental — Lote 07: relatórios de normalização e auditoria documental

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-007 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; RESULTADOS_HISTORICOS_IDENTIFICADOS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | b15acb185989b4d4a2347c0749139ef190568aa3c713cddc07247cea1e7560de |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — relatório de revisão; aprovação de alterações operacionais não concedida |
| **Origem** | Inspeção de conteúdo de nove relatórios de execução/auditoria |
| **Autoridade superior** | [Carta Magna B3](../../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Relatórios de execução de normalização de catálogos/readmes e auditorias documentais/workflows |
| **Objetivo** | Distinguir sucesso de auditoria de integridade, validade de conteúdo e estado operacional atual |
| **Dependências** | Runs e commits citados nos relatórios; matriz semântica integral |

## 1. Resultado executivo

Foram revistos nove documentos. Os relatórios dos Lotes 02–07 documentam mudanças editoriais em README e metadados, não validação de instrumentos financeiros nem certificação da atualidade/completude do catálogo. Os Lotes 02 e 03 registam que a auditoria estava pendente no momento da redação; relatórios posteriores dos Lotes 04–06 referenciam execuções conformes para os respetivos commits. Não se deve projetar um estado posterior para trás nem interpretar a ausência de auditoria naquele momento como falha de conteúdo.

A triagem documental e o relatório de conformidade de workflows são evidências diagnósticas com universo, commit, critérios e data próprios. A conformidade SHA-256 só prova integridade do conteúdo canónico, não validade semântica nem operacional.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/governanca/auditorias/RELATORIO_EXECUCAO_NORMALIZACAO_CATALOGOS_ATIVOS_LOTE02_2026-10-15.md | Relatório de execução editorial | Escopo é README de catálogos; afirma preservação do texto e ausência de alteração de dados de mercado. A auditoria estava pendente naquele snapshot. | Manter como histórico; não inferir conformidade até a evidência do run/commit correspondente. |
| docs/governanca/auditorias/RELATORIO_EXECUCAO_NORMALIZACAO_CATALOGOS_ATIVOS_LOTE03_2026-10-15.md | Relatório de execução editorial | Mesmo limite: metadados e README descritivos, sem validação dos instrumentos. A auditoria estava pendente na data do relatório. | Manter como histórico; não usar para declarar catálogo atualizado ou completo. |
| docs/governanca/auditorias/RELATORIO_EXECUCAO_NORMALIZACAO_CATALOGOS_ATIVOS_LOTE04_2026-10-15.md | Relatório de auditoria de metadados | Reporta execução e SHA-256 conformes no run 38730842955, para o commit indicado. Declara expressamente que não valida completude nem negociabilidade dos instrumentos. | Evidência limitada ao commit e ao controlo de hash; não é validação de negócio. |
| docs/governanca/auditorias/RELATORIO_EXECUCAO_NORMALIZACAO_CATALOGOS_ATIVOS_LOTE05_2026-10-15.md | Relatório de auditoria de metadados | Reporta conformidade SHA-256 no run 38731550044 e delimita o mesmo escopo editorial. | Preservar o limite: não promove classificação económica/regulatória nem a atualidade do catálogo. |
| docs/governanca/auditorias/RELATORIO_EXECUCAO_NORMALIZACAO_CATALOGO_ATIVOS_LOTE06_2026-10-15.md | Relatório de auditoria do README raiz de ativos | Reporta conformidade SHA-256 no run 38732287146; ressalva que não substitui contratos de dados ou ingestão. | Usar apenas como evidência estrutural do documento e commit auditados. |
| docs/governanca/auditorias/RELATORIO_EXECUCAO_NORMALIZACAO_MERCADOS_ALVO_LOTE07_2026-10-15.md | Relatório editorial de negócio | Regista normalização do README de mercados-alvo e separa auditoria do workflow de validação de mercado. | Não inferir aprovação de mercado-alvo, licenciamento ou pricing. |
| docs/governanca/auditorias/RELATORIO_EXECUCAO_NORMALIZACAO_READMES_NEGOCIO_LOTE06_2026-10-15.md | Relatório editorial de negócio | Regista commits de conteúdo e hash; afirma que documentos normativos, contratos e artefactos gerados permanecem fora da normalização genérica. | Preservar esta salvaguarda; os modelos económicos requerem revisão de premissas própria. |
| docs/governanca/auditorias/TRIAGEM_FAMILIAS_DOCUMENTAIS_SHA256_2026-10-15.md | Triagem histórica por família de caminho | Usa snapshot antigo (289 Markdown; 271 cabeçalhos inválidos e um sem H1) e diz explicitamente que o inventário não é revisão de conteúdo. | Números são históricos e não baseline atual. Manter como evidência temporal; a matriz semântica atual governa o estado por ficheiro. |
| docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.md | Relatório gerado de auditoria de workflows | Separa bloqueadores funcionais de alertas de observabilidade e proíbe que o relatório corrija/reexecute/promova workflows. A matriz é gerada e vinculada a critérios do auditor. | Tratar como snapshot gerado; verificar run/commit antes de citar estado atual. Não usar como autoridade normativa independente do Layout Mestre. |

## 3. Achados transversais

### SEM-07-01 — normalização documental não valida ativos

A adição de cabeçalhos, metadados e hashes a README não prova que um ativo esteja atualmente listado, elegível, negociável ou classificado corretamente. A fonte oficial, o catálogo de instrumentos e os contratos específicos continuam a determinar essas questões.

### SEM-07-02 — auditoria de hash tem âmbito limitado

CONFORME significa que o conteúdo canónico coincide com o hash declarado segundo a regra usada pelo auditor. Não prova que o texto seja atual, semanticamente correto ou aprovado.

### SEM-07-03 — snapshots antigos não são estado corrente

Os valores 289/271/1 e as contagens 108/109 pertencem a commits e momentos específicos. Não devem ser reutilizados como estado presente depois das normalizações e alterações posteriores.

### SEM-07-04 — relatório gerado não é norma

O relatório de workflows descreve a saída do auditor e deve permanecer subordinado ao Layout Mestre e à decisão GOV-DIV-001. Qualquer mudança de critérios exige alteração versionada do auditor/contrato, não edição manual do relatório gerado.

## 4. Conclusão

O conteúdo dos nove documentos foi revisto. Não foi alterado qualquer dado de mercado ou catálogo. O resultado semântico do lote é CONCLUÍDO com limites e ações explicitados; a revisão global continua aberta.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária. A proveniência RAW e a lista oficial ExternalSecurityCategoryCode continuam dependências independentes. BLOOMBERG_MAIL permanece isolado e fora do escopo operacional B3.

## 5. Referências

- [Matriz integral de revisão semântica](MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Plano Mestre de Execução](../../PLANO_MESTRE_DE_EXECUCAO.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
