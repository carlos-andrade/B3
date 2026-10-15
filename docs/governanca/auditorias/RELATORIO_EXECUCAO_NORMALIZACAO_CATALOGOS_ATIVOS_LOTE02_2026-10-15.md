# Relatório de execução — normalização de catálogos de ativos, lote 02

| Campo | Valor |
|---|---|
| **ID** | B3-ATIVOS-NORM-LOTE02-2026-10-15 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_EXECUCAO_DOCUMENTAL |
| **Fase** | Fase 5 — Normalização controlada |
| **Estado** | EXECUTADO; AUDITORIA AUTOMÁTICA PENDENTE |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 065c8994719aa138b1740963ebc1bb750dcbd867143d502c5e4c1fa5c7f67cc7 |
| **Commit de referência (versão anterior)** | [0ea6852b910cbc342c19f2e85391125d5df59dd9](https://github.com/carlos-andrade/B3/commit/0ea6852b910cbc342c19f2e85391125d5df59dd9) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — registo operacional, sem aprovação normativa |
| **Origem** | Alterações versionadas na branch main e norma documental GOVERNANCA v1.0.3 |
| **Autoridade superior** | [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA); Layout Mestre Canónico B3 |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Normalização de README descritivos em ativos; sem alteração de dados de mercado |
| **Objetivo** | Registar alterações, limites e validação do lote 02 |
| **Dependências** | Auditor SHA-256 documental; README dos catálogos de ativos |

## 1. Alterações realizadas

Foram normalizados os cabeçalhos de:
- `ativos/bdrs/README.md`
- `ativos/commodities/README.md`
- `ativos/etfs/README.md`

O lote anterior normalizou `ativos/acoes/README.md` e `ativos/balcao/README.md`. Os textos descritivos originais foram preservados, com metadados adicionados e estado `EM_REVISAO`; não foi inferida aprovação normativa.

## 2. Integridade

Os hashes canónicos foram calculados segundo a norma: UTF-8, finais de linha LF e exclusão apenas das linhas de SHA-256 e commit de referência. Os valores registados nos três documentos deste lote foram calculados antes da publicação. A auditoria de workflow do lote 02 ainda não foi localizada após a publicação do commit pelo Git Data API; por isso, estes documentos não são declarados conformes até a execução oficial confirmar os resultados.

## 3. Limites e salvaguardas

- Nenhum dado de mercado, RAW, manifesto ou contrato foi alterado.
- Não foram modificadas regras de instrumentos ou classificações regulatórias.
- A fonte BVBG.028.02 permanece referida apenas onde já estava declarada; este lote não valida a atualidade do catálogo de instrumentos.
- Documentos normativos e contratos técnicos continuam excluídos de normalização automática.

## 4. Próxima ação

Confirmar que o workflow SHA-256 é executado sobre o commit do lote; analisar o artefacto e corrigir qualquer divergência antes de continuar para novos README. Só depois avançar para o lote editorial seguinte.
