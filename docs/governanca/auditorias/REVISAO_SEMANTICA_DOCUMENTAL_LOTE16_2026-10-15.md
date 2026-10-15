# Revisão semântica documental — Lote 16: certificação anual, orquestração e roadmaps COTAHIST

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-016 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; ROADMAPS_HISTORICOS_PRESERVADOS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão documental; não autoriza promoção nem reabertura |
| **Origem** | Inspeção de 11 documentos de certificação, ordem, orquestração e roadmap |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CONTRATO → ORQUESTRADOR → EVIDÊNCIA → GATE → PROMOÇÃO |
| **Escopo** | Modelo de certificação anual, ordem operacional, orquestradores V1/V2, regra geral e roadmaps de 12–14/10 |
| **Objetivo** | Confirmar hierarquia entre contrato, dry-run e estado atual e corrigir caminhos genéricos inválidos |
| **Dependências** | Layout Mestre, manifests, evidências por fase, Issue #11 e roadmap atual |

## 1. Resultado executivo

Foram revistos 11 documentos. As regras de certificação e dependência são coerentes: o ano anterior serve de referência de processo, não de prova; cada fase requer evidência própria; um dry-run não deve alterar dados nem promover um ano; a ausência de evidência é bloqueadora; e a FASE12 não certifica automaticamente o ano seguinte.

Foi corrigido um defeito concreto no orquestrador V2: os caminhos genéricos usavam COTAHIST_AAAAAA.ZIP/CSV, incompatíveis com a convenção canónica A<AAAA>. Os caminhos foram alinhados ao índice de caminhos. Os roadmaps de 12–14/10 continuam snapshots históricos; a data de atualização do cabeçalho não muda a data de referência do estado descrito.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/cotahist/MODELO_CERTIFICACAO_ANUAL_COTAHIST_V1.md | Modelo de certificação | Define o baseline anterior como referência processual e proíbe copiar evidência entre anos. | Usar como modelo; não é certificação de nenhum ano por si só. |
| docs/cotahist/ORDEM_OPERACIONAL_ATUALIZACAO_V1.md | Ordem operacional | Exige execução real, evidência persistida, validação de gates e só depois atualização de README. | Coerente; o texto sobre FASE06/1994 é histórico e não autoriza reabertura. |
| docs/cotahist/ORQUESTRADOR_ANUAL_CANONICO_V1.md | Orquestrador DRY-RUN V1 | Não altera ficheiros nem promove anos; verifica pré-condições documentais antes de futura migração. | Tratar como proposta/versão inicial de DRY-RUN, não como pipeline de produção. |
| docs/cotahist/ORQUESTRADOR_ANUAL_CANONICO_V2.md | Orquestrador DRY-RUN V2 | Sequência 00–12 e estados OK/AUSENTE/BLOQUEADO/NAO_APLICAVEL/EXCECAO_CONTROLADA são coerentes. Caminhos genéricos AAAAAA eram inválidos. | Corrigido para COTAHIST_A<AAAA>.ZIP e COTAHIST_A<AAAA>.csv; confirmar a auditoria SHA-256 pós-alteração. |
| docs/cotahist/REGRA_GERAL_EXISTENCIA_E_VALIDACAO_V1.md | Regra de existência e validação | Exige artefactos identificáveis, verificáveis, persistidos, imutabilidade RAW e gates explícitos; sucesso de workflow não basta. | Manter como regra de gate, reconciliada com o Layout Mestre e a decisão GOV-DIV-001. |
| docs/cotahist/ROADMAP_COTAHIST_1999_2001_ESTADO_2026-10-12.md | Roadmap histórico multi-ano | Relata fechamentos/transições para 1999–2002 e estado de 2006 no mesmo documento; o nome do ficheiro não reflete todo o escopo descrito no título/corpo. | Preservar como snapshot; não renomear nem tratar como status corrente sem uma decisão documental própria. |
| docs/cotahist/ROADMAP_INGESTAO_PARTE18_ESTADO_2026-10-12.md | Roadmap PARTE18 | Documenta incompatibilidade de parser no Dataset Oficial V1 e a necessidade de separar versões/contratos. | Estado histórico; não reutilizar contagens/runs como atuais. |
| docs/cotahist/ROADMAP_INGESTAO_PARTE20_ESTADO_2026-10-13.md | Roadmap PARTE20 | Regista 2014 como ciclo ativo observado em 13/10 e explicitamente remete para PARTE23 como roadmap mais recente. | Manter como histórico e não como instrução atual de execução. |
| docs/cotahist/ROADMAP_INGESTAO_PARTE23_ESTADO_2026-10-14.md | Roadmap PARTE23 | Consolida o estado de 2026 até 13/10, hashes e fases, com limitações explícitas; não prova frescor posterior. | Usar como fotografia de 14/10; consultar a atualização diária posterior para o estado atual. |
| docs/cotahist/ROADMAP_MESTRE_INGESTAO_COTAHIST_1986_2026_ESTADO_2026-10-14.md | Roadmap mestre COTAHIST | Distingue certificação estrutural anual de semântica histórica completa e identifica pendências residuais. | Preservar o snapshot e reconciliar com a decisão de anos históricos em consulta/read-only e com o estado diário atual. |
| docs/cotahist/WORKFLOW_ORDEM_E_DEPENDENCIAS_V1.md | Contrato de ordem e dependências | Define FASE10 como gate independente e proíbe inferir execução individual de fases a partir de RAW/NORMALIZED/manifests existentes. | Coerente; usar para governança de workflow, sem reabrir anos históricos fechados. |

## 3. Achados e decisões

### SEM-16-01 — caminhos genéricos inválidos no Orquestrador V2

**Achado:** os placeholders COTAHIST_AAAAAA.ZIP/CSV não correspondem ao padrão anual canónico COTAHIST_A<AAAA>.ZIP/CSV.

**Correção:** os dois caminhos foram corrigidos para usar o placeholder canónico com quatro dígitos de ano. A alteração é documental e não executa nem promove fases. A auditoria SHA-256 posterior deve confirmar a integridade do ficheiro.

### SEM-16-02 — roadmaps têm datas de referência próprias

A data do cabeçalho foi normalizada para outubro, mas os estados descritos continuam referidos a 12, 13 ou 14/10. Isso não os transforma em fotografia de 15/10.

**Decisão:** manter cada roadmap como evidência histórica; para estado corrente, usar a versão mais recente e a evidência operacional posterior.

### SEM-16-03 — discrepância de nome/escopo do roadmap 1999–2001

O ficheiro tem nome 1999_2001, enquanto o título e o corpo incluem um escopo mais amplo, incluindo anos posteriores. Não alterar silenciosamente o histórico.

**Ação:** manter o estado como snapshot histórico e registar uma correção de nome/escopo em versão futura caso o documento volte a ser usado como roadmap ativo.

### SEM-16-04 — anos anteriores a 2026 permanecem fechados

Os roadmaps antigos contêm estados PENDENTE para 1994/1995, datados do período de investigação. A decisão de governança posterior determina que anos anteriores a 2026 estão encerrados para consulta, não para novas execuções.

**Decisão:** não reabrir anos históricos a partir destas instruções antigas; preservá-las como evidência da evolução do projeto.

## 4. Conclusão

O conteúdo dos 11 documentos foi revisto e um erro de placeholder foi corrigido no orquestrador V2. Não foram alterados dados, manifests ou workflows. Os roadmaps permanecem históricos; o estado corrente é controlado pelo roadmap atual e pelas evidências diárias.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Índice canónico de caminhos COTAHIST](../../docs/cotahist/INDICE_CAMINHOS_COTAHIST_V1.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
