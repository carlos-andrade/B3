# Revisão semântica documental — Lote 15: arquitetura COTAHIST e evidências históricas

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-015 |
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
| **Aprovador** | N/A — revisão documental; não reabre nem certifica fases históricas |
| **Origem** | Inspeção de 15 contratos, matrizes e investigações de execução COTAHIST |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CONTRATO → FASE → EVIDÊNCIA → GATE → PROMOÇÃO |
| **Escopo** | Auditorias de workflow, investigações 1994/1995/1998, gates 06–08, índices, dependências e matrizes retrospectivas |
| **Objetivo** | Separar snapshots históricos de estado atual e validar que as evidências não autorizam reexecução retroativa |
| **Dependências** | Contratos de fases COTAHIST, manifestos, runs históricos e roadmap atual |

## 1. Resultado executivo

Foram revistos 15 documentos de arquitetura, gates e investigações COTAHIST. A regra comum é consistente: fases posteriores dependem de evidência explícita da fase anterior; sucesso de um workflow não prova automaticamente integridade/semântica; falta de evidência não deve ser convertida em sucesso; e auditorias posteriores não autorizam reabrir dados históricos.

Os relatórios datados de 29/09–02/10 descrevem o estado e os runs daquele momento. Em especial, os estados de 1994/1995 que aparecem como PENDENTE pertencem a essas investigações históricas. A decisão de governança mais recente mantém todos os anos anteriores a 2026 fechados e apenas para consulta. Portanto, estes relatórios não devem ser tratados como ordens operacionais atuais nem usados para reabrir 1994/1995.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/cotahist/AUDITORIA_WORKFLOWS_COTAHIST_V2.md | Auditoria de dependências de workflows | Identifica corridas, triggers concorrentes e ausência de dependências formais; declara que os achados não invalidam automaticamente releases históricos. | Usar como diagnóstico arquitetural histórico; novas correções devem ocorrer em workflows atuais/versionados, sem reexecução de anos fechados. |
| docs/cotahist/CADENA_EXECUCAO_1994_FASE06_12_V1.md | Contrato de cadeia histórica | Define ordem 06→12 e gates fail-closed; exige evidência específica de 1994, sem reutilizar a de 1993. | Preservar como especificação histórica da investigação; não usar para reabrir a cadeia fechada por decisão posterior. |
| docs/cotahist/COMPARATIVO_BASELINE_1993_VS_1994_FASE06_V1.md | Comparação de baseline | Distingue 1993 certificado de 1994 ainda pendente no snapshot de 01/10. | Estado de 1994 é histórico, não status corrente; preservar comparação e não reescrever retroativamente. |
| docs/cotahist/COTAHIST_1998_FASE06C_INVESTIGACAO_SEMANTICA_TERM_V1.md | Investigação semântica de mercado a termo | Separa fato, hipótese controlada e não demonstrado; rejeita a regra universal “violação OHLC = dado inválido” para TPMERC=030. | Manter a exceção diagnóstica; não corrigir RAW/NORMALIZED nem extrapolar a conclusão a outros segmentos sem evidência. |
| docs/cotahist/FASE02_1994_INVESTIGACAO_RUN59.md | Investigação de falha de workflow | Distingue falha de execução da integridade do RAW e regista que o Run #59 não tinha step logs disponíveis para atribuir a causa. | Preservar o run como falha histórica; não retrocertificar com base em nova execução. |
| docs/cotahist/FASE06_1995_INVESTIGACAO_PROVA_EXECUCAO_E_CAUSA.md | Investigação de prova de execução | Distingue execução real de ausência anterior de evidência e transfere identidade/cardinalidade para FASE07. | Preservar os resultados históricos e a separação de responsabilidades por fase. |
| docs/cotahist/FASE13_INVESTIGACAO_RUN10_1994.md | Investigação de cadeia fail-closed | Regista sucesso em FASE06–08 e falha em FASE09–12 por contrato/gate. | Não tratar a cadeia como fechada no snapshot; não executar hoje sem decisão explícita de reabertura, que não existe. |
| docs/cotahist/FASE13_INVESTIGACAO_RUN8_1994.md | Investigação de falha de cadeia | Regista que FASE13 não foi concluída e que a cadeia falhou por regra fail-closed; distingue dados de correção operacional. | Preservar como histórico; não marcar correção aplicada artificialmente nem reabrir 1994. |
| docs/cotahist/GATE_06_08_AJUSTE_2026-10-01.md | Registo de correção documental do gate | Afirma que a correção foi normativa/documental e não executou fases históricas. | Usar como evidência de contrato; não confundir correção documental com nova certificação de dados. |
| docs/cotahist/INDICE_CAMINHOS_COTAHIST_V1.md | Índice canónico de caminhos | Define caminhos de RAW, manifesto, NORMALIZED, quality e certificação e exige localizar antes de criar duplicados. | Coerente como índice; atualizar apenas quando o layout mudar por decisão versionada. |
| docs/cotahist/INVENTARIO_WORKFLOWS_COTAHIST_V1.md | Inventário arquitetural | Identifica pipelines históricos heterogéneos e dependências implícitas; recomenda reorganização por arquitetura, não renomeação. | Tratar contagens e diagnóstico como snapshot de 29/09; não converter inventário em autorização de alteração. |
| docs/cotahist/MAPEAMENTO_RETROSPECTIVO_1987_1988_FASES_06_09_V1.md | Mapeamento retrospectivo de evidências | Declara que não cria evidência retroativa e distingue COMPROVADA, PARCIAL, NAO_COMPROVADA e EXCECAO_CONTROLADA. | Preservar classificações com origem; não promover por equivalência não aprovada. |
| docs/cotahist/MATRIZ_DEPENDENCIAS_COTAHIST_V1.md | Matriz de dependências | Demonstra que concorrência/rebase não substituem dependências semânticas; materialização e FASE10 tinham independência formal no snapshot. | Usar como diagnóstico de arquitetura; tratar as colisões de persistência observadas em 15/10 como incidente separado. |
| docs/cotahist/MATRIZ_OPERACIONAL_TAREFAS_POR_FASE_V1.md | Matriz operacional de tarefas | Define sequência 00→12, uma fase por tarefa e correção na fase de origem; aponta o Layout Mestre como autoridade operacional. | Coerente com GOV-DIV-001; manter a cadeia fechada para anos históricos e aplicar a especificação atual apenas a operações autorizadas. |
| docs/cotahist/MATRIZ_RETROSPECTIVA_EVIDENCIAS_1987_1993_V1.md | Matriz retrospectiva de evidências | Distingue COMPROVADA, PARCIAL e NAO_COMPROVADA e impede que certificações posteriores provem fases anteriores. | Preservar como histórico; qualquer equivalência retrospetiva exige decisão e evidência específicas, sem inventar artefactos. |

## 3. Achados e decisões

### SEM-15-01 — estado histórico não é estado operacional atual

Os documentos datados de 29/09–02/10 mantêm estados PENDENTE de anos anteriores a 2026. Isso descreve a investigação naquele momento; não autoriza reabrir os anos fechados pela decisão posterior do projeto.

**Decisão:** manter documentos e runs como histórico. COTAHIST 1986–2025 é somente consulta/read-only; não reexecutar, alterar RAW, NORMALIZED, manifests ou gates históricos por esta revisão.

### SEM-15-02 — evidência de fase é independente de sucesso do workflow

Os documentos exigem que a fase produza artefacto verificável e que o gate confira estado e dependências. Um job verde isolado não substitui a evidência de negócio nem a validação independente.

**Decisão:** manter os gates como contrato de referência para operações autorizadas; não retrocertificar fases históricas nem transformar falhas de publicação em defeitos de dados sem prova.

### SEM-15-03 — invariantes devem ser específicas ao domínio

A investigação de TPMERC=030 em 1998 reconhece que a geometria OHLC convencional não é regra universal para todos os tipos de instrumento. O documento distingue claramente o que foi demonstrado do que permanece hipótese.

**Decisão:** preservar exceções por segmento e exigir evidência documental/empírica antes de impor invariantes gerais.

### SEM-15-04 — persistência concorrente é incidente operacional próprio

A matriz de dependências já identificava que triggers independentes podem criar corridas. As colisões de escrita observadas em outubro de 2026 devem ser ligadas a runs/commits próprios; não se pode inferir corrupção de RAW sem comparação de hashes e artefactos.

## 4. Conclusão

O conteúdo dos 15 documentos foi revisto. Não foram alterados dados, workflows ou evidências históricas. O lote é semânticamente concluído como revisão documental; as decisões históricas permanecem preservadas e não autorizam reexecução.

COTAHIST 1986–2025 permanece em consulta/read-only; 2026 mantém atualização diária. A proveniência RAW continua uma frente separada.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Plano Mestre de Execução](../../PLANO_MESTRE_DE_EXECUCAO.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
