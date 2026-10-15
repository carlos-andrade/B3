# Relatório de execução — normalização dos catálogos de ativos — Lote 05

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-AUDIT-ATIVOS-LOTE05-20261015 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_EXECUCAO_AUDITORIA |
| **Fase** | Normalização documental e auditoria |
| **Estado** | CONFORME |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 1d7f763b0357e708f1bd145510ac681789759890bc0a5354874c6d1cb259513a |
| **Commit de referência (versão anterior)** | [715ce33c3a2f6456993e920900f45863e37578c7](https://github.com/carlos-andrade/B3/commit/715ce33c3a2f6456993e920900f45863e37578c7) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — relatório de execução |
| **Origem** | Execução e artefacto do workflow de auditoria documental |
| **Autoridade superior** | [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma de cabeçalho GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Evidência de execução da normalização documental Lote 05 |
| **Objetivo** | Registar o escopo, resultado e evidências verificadas do Lote 05 |
| **Dependências** | Workflow de auditoria SHA-256 documental B3 |

## Resultado

**Estado da execução:** CONCLUÍDA  
**Estado da auditoria SHA-256:** CONFORME  
**Workflow de auditoria:** [38731550044](https://github.com/carlos-andrade/B3/actions/runs/38731550044)  
**Commit auditado:** `715ce33c3a2f6456993e920900f45863e37578c7`

## Escopo

Foram normalizados três README descritivos de catálogos de ativos:

- `ativos/opcoes/README.md`
- `ativos/termo/README.md`
- `ativos/renda_fixa/README.md`

As alterações padronizaram metadados documentais, identificadores, escopo, objetivo, dependências e regras de integridade, preservando a descrição original e esclarecendo que disponibilidade e elegibilidade dependem de evidência oficial datada.

## Evidência de auditoria

O workflow concluiu com sucesso, incluindo os testes unitários do hash canónico e a comparação SHA-256 documental.

- Ficheiros Markdown analisados: **293**
- `CONFORME`: **38**
- `CABECALHO_CONTROLO_INVALIDO`: **254**
- `SEM_CABECALHO_H1`: **1**
- Divergências de hash canónico: **0**
- Pendências de hash canónico: **0**

Os três ficheiros deste lote foram classificados individualmente como `CONFORME`, com hash declarado igual ao hash calculado.

## Limites

Este relatório comprova a execução documental e a auditoria de integridade dos hashes. Não constitui validação externa da completude dos catálogos, nem prova que todos os instrumentos mencionados estejam atualmente listados ou negociáveis na B3.

## Próxima ação

Continuar a normalização de README descritivos de baixo risco. Manter contratos de dados, políticas e documentos normativos fora de alterações automáticas e sujeitos a revisão semântica específica.
