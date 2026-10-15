# FASE 05.5 — GRUPO 02 — TRIGGERS

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-E6AA39D6E2C9 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 3bf47df7512f68d7e24876566e43c975c36d6090e01416ed6da3f5e031cde2a1 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Data:** 2026-10-01  
**Estado:** VALIDADO  
**Fonte normativa:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`  
**Matriz:** `docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.json`

## Evidência de execução

- Auditor v2: **Run #35 — 36890645073 — SUCCESS**
- Commit auditado: `faf30c3f94a52d36a237c25900f67a9a32ed2261`
- Workflows auditados: **109**
- `TRIGGER_DECLARED`: **109/109 OK**
- `NO_POSTERIOR_PHASE_TRIGGER`: **109/109 OK**

## Exceção normativa

O único workflow identificado pelos checks `NO_README_TRIGGER` e `NO_GENERIC_DOCS_TRIGGER` é o próprio `atualizar-readme-b3.yml`. Ele é a rotina consolidada do README e está explicitamente submetido à regra especial de consolidação às 23:55 Brasília. Portanto, não é uma divergência operacional de fase.

## Decisão

**GRUPO 02 — TRIGGERS = VALIDADO.**

As divergências restantes da matriz pertencem a outros grupos, principalmente permissões, observabilidade, decisão e idempotência. Elas não reabrem este grupo.

## Continuidade

O **GRUPO 03 — ISOLAMENTO/DIRECIONALIDADE** consumirá esta evidência somente em leitura. Qualquer correção futura será realizada na origem correspondente.
