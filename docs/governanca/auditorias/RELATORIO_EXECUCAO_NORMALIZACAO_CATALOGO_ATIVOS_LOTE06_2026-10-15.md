# Relatório de execução — normalização do catálogo raiz de ativos — Lote 06

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-AUDIT-ATIVOS-LOTE06-20261015 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_EXECUCAO_AUDITORIA |
| **Fase** | Normalização documental e auditoria |
| **Estado** | CONFORME |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | ed50c63b46dfcc2061f8c48b770fff463ce7f8b2e1fc2fc843041817f16bd7bb |
| **Commit de referência (versão anterior)** | [06b2413a79e409ddf7f1b17be7d362b54ec89e63](https://github.com/carlos-andrade/B3/commit/06b2413a79e409ddf7f1b17be7d362b54ec89e63) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — relatório de execução |
| **Origem** | Execução e artefacto do workflow de auditoria documental |
| **Autoridade superior** | [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma de cabeçalho GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Evidência de execução da normalização documental Lote 06 |
| **Objetivo** | Registar o escopo, resultado e evidências verificadas do Lote 06 |
| **Dependências** | Workflow de auditoria SHA-256 documental B3 |

## Resultado

**Estado da execução:** CONCLUÍDA  
**Estado da auditoria SHA-256:** CONFORME  
**Workflow de auditoria:** [38732287146](https://github.com/carlos-andrade/B3/actions/runs/38732287146)  
**Commit auditado:** `06b2413a79e409ddf7f1b17be7d362b54ec89e63`

## Escopo

Foi normalizado o README de entrada da árvore `ativos/`:

- `ativos/README.md`

O documento recebeu metadados padronizados e regras de integridade para preservar a data de referência do inventário e evitar inferências não comprovadas sobre a disponibilidade de instrumentos. A lista estrutural de diretórios e a regra de permanência dos dados e automações no repositório foram preservadas.

## Evidência de auditoria

O workflow concluiu com sucesso, incluindo os testes unitários do hash canónico e a comparação SHA-256 documental.

- Ficheiros Markdown analisados: **294**
- `CONFORME`: **40**
- `CABECALHO_CONTROLO_INVALIDO`: **253**
- `SEM_CABECALHO_H1`: **1**
- Divergências de hash canónico: **0**
- Pendências de hash canónico: **0**

O ficheiro deste lote foi classificado como `CONFORME`, com hash declarado igual ao hash calculado.

## Limites

Este relatório comprova a execução documental e a auditoria de integridade dos hashes. Não constitui validação externa da completude do catálogo nem substitui os contratos de dados ou os processos de ingestão.

## Próxima ação

Manter contratos de dados, políticas e documentos normativos fora de alterações automáticas. Prosseguir com inventário e revisão semântica orientada, priorizando riscos de autoridade documental e evidência de dados.
