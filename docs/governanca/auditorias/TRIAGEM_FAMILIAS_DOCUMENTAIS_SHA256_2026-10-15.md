# Auditoria documental B3 — triagem por famílias de caminhos

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-AUDIT-TRIAGEM-002 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_AUDITORIA |
| **Fase** | Normalização documental — triagem por famílias |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 72d7adc3aa98542ebca1ca738e45a2894daa7be277b1a64f8837211503934e29 |
| **Commit de referência (versão anterior)** | [e1977d176b98fec097da7f0ed8d3852d9a871bc0](https://github.com/carlos-andrade/B3/commit/e1977d176b98fec097da7f0ed8d3852d9a871bc0) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente de aprovação específica |
| **Origem** | Artefacto de auditoria SHA-256 documental do workflow 38724652701 |
| **Autoridade superior** | [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA); Layout Mestre Canónico B3 |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Triagem estrutural de Markdown; não altera conteúdo nem contratos de dados |
| **Objetivo** | Ordenar a normalização em lotes seguros e auditáveis |
| **Dependências** | Relatório SHA-256 documental; inventário documental; revisão semântica por lotes |

## 1. Evidência de base

A execução [38724652701](https://github.com/carlos-andrade/B3/actions/runs/38724652701) terminou com sucesso no commit `e1977d176b98fec097da7f0ed8d3852d9a871bc0`. O artefacto de auditoria reportou 289 ficheiros Markdown: 17 `CONFORME`, 271 `CABECALHO_CONTROLO_INVALIDO` e 1 `SEM_CABECALHO_H1`. Não foram reportadas divergências SHA-256 nem pendências de hash. Os três documentos alterados no ciclo anterior foram confirmados como `CONFORME`.

## 2. Distribuição dos 271 casos por família de caminho

| Família | Casos | Tratamento inicial |
|---|---:|---|
| `docs/ingestao/` | 132 | Prioridade alta; separar relatórios de execução, contratos, evidências e documentos de calendário antes de alterar |
| `docs/NEGOCIO/` | 30 | Classificar documentos de negócio e modelos; preservar definições e premissas existentes |
| `docs/cotahist/` | 25 | Tratar como documentação operacional/contratual COTAHIST; não alterar gates, sequenciamento ou critérios de promoção sem revisão semântica |
| `docs/governanca/` | 16 | Revisão normativa prioritária; resolver conflitos de autoridade por decisão versionada, sem edição normativa implícita |
| `ativos/catalogo/` | 11 | Distinguir protocolo, inventário, evidência de fonte, estatísticas e README |
| `dados/market_data/` | 5 | Preservar contratos de granularidade, histórico, microestrutura e fontes |
| `dados/bdi/` | 4 | Distinguir protocolo e documentação de ingestão de dados |
| `dados/calendario_economico/` | 3 | Preservar documentos-fonte e evidências originais |
| `dados/fontes/` | 2 | Classificar diagnóstico e estado de migração de fontes |
| `WIKI/` | 6 | Normalizar páginas editoriais após conferir estrutura e referências internas |
| Outras famílias e ficheiros isolados | 37 | Triagem por tipo documental antes de qualquer alteração |

A contagem é agrupada por prefixos de caminho do relatório da execução. Não representa classificação semântica final nem autorização para modificar automaticamente os ficheiros.

## 3. Ordem de execução e salvaguardas

1. **Lote A — documentos editoriais simples e README**: confirmar se o documento é humano/editorial e aplicar cabeçalho conforme a norma, preservando integralmente o corpo e as ligações.
2. **Lote B — inventários, protocolos e documentação de fontes**: rever campos exigidos pelo tipo; manter a proveniência e os identificadores originais.
3. **Lote C — relatórios de auditoria e evidências históricas**: manter os resultados históricos imutáveis no conteúdo substantivo; acrescentar metadados apenas quando a norma e o tipo permitirem.
4. **Lote D — contratos, gates, workflows e documentação normativa**: exigir revisão semântica individual e decisão autorizada para qualquer conflito; não fazer substituição em massa.
5. **Lote E — documentos gerados ou ligados a artefactos de máquina**: não inserir cabeçalhos sem contrato explícito que o permita.
6. Após cada lote, executar testes, calcular SHA-256 canónico, confirmar artefacto de auditoria e registar os resultados antes de iniciar o seguinte.

## 4. Exceção identificada

O ficheiro `docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md` foi reportado como `SEM_CABECALHO_H1`. A ausência de H1 deve ser investigada quanto ao tipo e à estrutura antes de o editar; não deve ser corrigida automaticamente apenas para satisfazer o auditor.

## 5. Restrições de projeto

- COTAHIST de 1986 a 2025 permanece encerrado para ingestão rotineira e disponível para consulta.
- COTAHIST 2026 segue atualização diária, com gates e evidência persistida; não promover fases sem prova.
- RAW, dados, manifestos, contratos e evidências de máquina não são alterados por esta triagem.
- `BLOOMBERG_MAIL` permanece fora do escopo operacional deste projeto B3.
- O conflito normativo `GOV-DIV-001` permanece aberto; a triagem não altera a precedência entre Carta Magna e Layout Mestre.

## 6. Estado e próximo passo

A integridade SHA-256 está sem divergências no snapshot auditado. A conformidade estrutural global ainda não foi atingida: 271 ficheiros requerem triagem de cabeçalho. Próxima ação: obter a lista completa de caminhos por estado a partir do artefacto, confirmar os tipos documentais em lotes pequenos e iniciar pelo lote de baixo risco, sem alteração automática de contratos ou relatórios históricos.
