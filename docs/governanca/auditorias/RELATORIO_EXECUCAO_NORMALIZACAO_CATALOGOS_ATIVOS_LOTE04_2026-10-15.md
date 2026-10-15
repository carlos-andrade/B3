# Relatório de execução — normalização dos catálogos de ativos — Lote 04

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-AUDIT-ATIVOS-LOTE04-20261015 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_EXECUCAO_AUDITORIA |
| **Fase** | Normalização documental e auditoria |
| **Estado** | CONFORME |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 11480d095a03ef6779343a0229d2facc67b0ed91bd72ccb815eeb424a92dafdf |
| **Commit de referência (versão anterior)** | [cedd28f4ccf1ff64095f80fae4f1ac14b2d24e90](https://github.com/carlos-andrade/B3/commit/cedd28f4ccf1ff64095f80fae4f1ac14b2d24e90) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — relatório de execução |
| **Origem** | Execução e artefacto do workflow de auditoria documental |
| **Autoridade superior** | [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma de cabeçalho GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Evidência de execução da normalização documental Lote 04 |
| **Objetivo** | Registar o escopo, resultado e evidências verificadas do Lote 04 |
| **Dependências** | Workflow de auditoria SHA-256 documental B3 |

## Resultado

**Estado da execução:** CONCLUÍDA  
**Estado da auditoria SHA-256:** CONFORME  
**Workflow de auditoria:** [38730842955](https://github.com/carlos-andrade/B3/actions/runs/38730842955)  
**Commit auditado:** `cedd28f4ccf1ff64095f80fae4f1ac14b2d24e90`

## Escopo

Foram normalizados seis README descritivos de catálogos de ativos:

- `ativos/cepac/README.md`
- `ativos/criptoativos/README.md`
- `ativos/emprestimo_ativos/README.md`
- `ativos/futuros/README.md`
- `ativos/juros/README.md`
- `ativos/moedas/README.md`

As alterações padronizaram metadados documentais, identificadores, escopo, objetivo, dependências e regras de integridade. Os textos preservam o escopo original e acrescentam salvaguardas para não presumir listagem, vigência ou negociabilidade sem evidência oficial datada.

## Evidência de auditoria

O workflow concluiu com sucesso, incluindo os testes unitários do hash canónico e a comparação SHA-256 documental.

- Ficheiros Markdown analisados: **292**
- `CONFORME`: **34**
- `CABECALHO_CONTROLO_INVALIDO`: **257**
- `SEM_CABECALHO_H1`: **1**
- Divergências de hash canónico: **0**
- Pendências de hash canónico: **0**

Os seis ficheiros deste lote foram classificados individualmente como `CONFORME`, com hash declarado igual ao hash calculado.

## Limites

Este relatório comprova a execução documental e a auditoria de integridade dos hashes. Não constitui validação externa da completude dos catálogos, nem prova que todos os instrumentos mencionados estejam atualmente listados ou negociáveis na B3.

## Próxima ação

Continuar a normalização de README descritivos de baixo risco, mantendo contratos de dados, políticas e documentos normativos fora de alterações automáticas e sujeitos a revisão semântica específica.
