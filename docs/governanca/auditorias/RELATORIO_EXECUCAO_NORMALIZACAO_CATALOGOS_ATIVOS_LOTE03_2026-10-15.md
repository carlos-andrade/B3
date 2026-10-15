# Relatório de execução — normalização de catálogos de ativos, lote 03

| Campo | Valor |
|---|---|
| **ID** | B3-ATIVOS-NORM-LOTE03-2026-10-15 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_EXECUCAO_DOCUMENTAL |
| **Fase** | Fase 5 — Normalização controlada |
| **Estado** | EXECUTADO; AUDITORIA AUTOMÁTICA PENDENTE |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 8cd61111a8fbb728cf8aec2fe3c2c087a7d34be9bebf1cf08e8fc2f5193eaf56 |
| **Commit de referência (versão anterior)** | [999aeec9a680c19d74cc81d1884a4cb0433ba75c](https://github.com/carlos-andrade/B3/commit/999aeec9a680c19d74cc81d1884a4cb0433ba75c) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — registo operacional, sem aprovação normativa |
| **Origem** | Alterações versionadas na branch main e norma documental GOVERNANCA v1.0.3 |
| **Autoridade superior** | [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA); Layout Mestre Canónico B3 |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Normalização de README descritivos em ativos; sem alteração de dados de mercado |
| **Objetivo** | Registar alterações, limites e validação do lote 03 |
| **Dependências** | Auditor SHA-256 documental; README dos catálogos de ativos |

## 1. Alterações realizadas

Foram normalizados os cabeçalhos de:
- `ativos/indices/README.md`
- `ativos/fundos/README.md`
- `ativos/fiis/README.md`

O lote preservou os textos descritivos preexistentes, acrescentando metadados documentais. Os três documentos permanecem em `EM_REVISAO`; a normalização não significa aprovação das definições de domínio nem valida a atualidade de quaisquer cadastros de instrumentos.

## 2. Integridade

Os SHA-256 canónicos foram calculados em UTF-8/LF, excluindo apenas as linhas de hash e commit de referência, conforme a norma documental. A confirmação final depende da auditoria oficial do workflow e do respetivo artefacto; não se declara conformidade antes dessa evidência.

## 3. Salvaguardas

- Nenhum dado de mercado, RAW, manifesto, contrato ou pipeline foi alterado.
- Não foram inferidos dados de instrumentos ou critérios de listagem.
- Contratos técnicos, documentos normativos e relatórios históricos permanecem fora da normalização automática.

## 4. Próxima ação

Validar o resultado do workflow para este lote. Em caso de conformidade, continuar com README descritivos de baixo risco; caso contrário, corrigir divergências antes de avançar.
