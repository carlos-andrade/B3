# FASE 10A — M3 — Migração NORMALIZED anual controlada V1.0

**Arquivo:** FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** M3-1D CONCLUÍDO — DATASET OFICIAL 2026 VALIDADO — M3-1E PENDENTE

## 1. Objetivo

Migrar os anos COTAHIST ainda sem NORMALIZED anual físico para o caminho canônico:

`dados/cotahist/normalized/anual/COTAHIST_A{ANO}.csv`

mantendo RAW imutável, parser 1.1.0, SHA-256, quality manifest, certificação física, rastreabilidade por commit e fail-closed.

## 2. Gates concluídos

### M3-0 — capacidade

NORMALIZED 2026: **392.044.266 bytes**.

Decisão: **GIT_STANDARD_LIMIT**.

### M3-1A — preparação

Git LFS configurado para NORMALIZED anual.

### M3-1B — prova física

2026 persistido via Git LFS com SHA:

`befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`

### Reconciliação

Manifest alinhado ao RAW atual.

RAW SHA:

`4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`

### M3-1C — CI

**APROVADO**

Run: `36428513803`

Evidência:

`M3-1C_STATUS=CI_INTEGRIDADE_APROVADA`

### M3-1D — Dataset Oficial

**APROVADO**

Run: `36428988106`

Evidência:

`M3-1D_STATUS=DATASET_OFICIAL_VALIDADO`

Dataset:

`dados/cotahist/normalized/anual/COTAHIST_A2026.csv`

Registros: **2.919.760**

Campos: **25**

Primeira data: **2026-01-02**

Última data: **2026-09-23**

## 3. M3-1E — aprovação global

O próximo gate deverá consolidar formalmente:

- M3-0;
- M3-1A;
- M3-1B;
- reconciliação do manifest;
- M3-1C;
- M3-1D;
- preservação do RAW;
- integridade do Dataset Oficial;
- política de Git LFS;
- documentação de governança.

Somente após M3-1E aprovado poderá ser liberada a migração histórica 1986–2025.

## 4. Regra de segurança

A migração histórica permanece bloqueada até a certificação M3-1E.

Não será iniciado lote histórico antecipadamente.

A cadeia oficial permanece:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY → RECONCILE`

## 5. Estado oficial

- M1 — **APROVADO**
- M2 — **APROVADO**
- M3-0 — **CONCLUÍDO**
- M3-1A — **CONCLUÍDO**
- M3-1B — **CONCLUÍDO**
- Reconciliação manifest — **CONCLUÍDA**
- M3-1C — **APROVADO**
- M3-1D — **APROVADO**
- M3-1E — **PENDENTE**
- Migração histórica 1986–2025 — **BLOQUEADA**

## 6. Próxima etapa

**M3-1E — Aprovação global.**

O gate deve ser executável, auditável e fail-closed. A aprovação não será declarada apenas por documentação; deverá existir evidência de execução real.
