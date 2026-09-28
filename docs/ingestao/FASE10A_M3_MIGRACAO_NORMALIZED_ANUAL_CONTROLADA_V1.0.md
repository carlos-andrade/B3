# FASE 10A — M3 — Migração NORMALIZED anual controlada V1.0

**Arquivo:** FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md  
**Data:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** **M3-1E CONCLUÍDO — FASE HISTÓRICA LIBERADA SOB GATES**

## 1. Objetivo

Migrar os anos COTAHIST para:

`dados/cotahist/normalized/anual/COTAHIST_A{ANO}.csv`

mantendo RAW imutável, parser 1.1.0, SHA-256, quality manifest, certificação física, rastreabilidade por commit e fail-closed.

## 2. M3-1 — armazenamento aprovado

O gate global M3-1E foi concluído com sucesso.

- Run: **36429403166**
- Job: **108951402371**
- Evidência: `M3-1E_STATUS=APROVACAO_GLOBAL_CONCLUIDA`
- Git LFS: **VALIDADO**
- Dataset Oficial 2026: **APROVADO**

O registro completo está em:

`docs/ingestao/M3-1E_APROVACAO_GLOBAL_COTAHIST_2026_V1.0.md`

## 3. Dataset Oficial 2026

- arquivo: `dados/cotahist/normalized/anual/COTAHIST_A2026.csv`
- SHA-256: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- registros: **2.919.760**
- campos: **25**
- primeira data: **2026-01-02**
- última data: **2026-09-23**

## 4. Liberação histórica

A fase histórica está **LIBERADA SOB GATES**, não como migração irrestrita.

Cada ano deverá executar:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY → RECONCILE`

Nenhum ano será considerado Oficial apenas porque um CSV já existe no repositório.

## 5. Regra especial 1986 → 1987

O projeto mantém a regra de que **1986 é o primeiro ano de reconciliação semântica e deve ser concluído antes da liberação de 1987**.

Para 1986 são obrigatórios:

1. `tpmerc`;
2. `codbdi`;
3. chave lógica correta;
4. 30 casos de OHLC;
5. volume e quantidade;
6. calendário de pregão;
7. amostras comparadas diretamente com RAW;
8. SHA-256;
9. reconstrução determinística;
10. persistência via Git LFS;
11. certificação;
12. reconciliação.

## 6. Anomalia preexistente 1987

O gate M3-1E identificou no checkout LFS:

`Encountered 1 file that should have been a pointer, but wasn't: dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

Consequência:

**COTAHIST_A1987.csv existente não está certificado como Dataset Oficial.**

A anomalia deve ser tratada em auditoria específica, sem apagar ou alterar RAW.

## 7. Próxima etapa operacional

Criar e executar o gate controlado de **COTAHIST 1986**, produzindo:

- NORMALIZED 1986;
- quality manifest;
- checksum;
- evidência de reconstrução;
- testes semânticos;
- certificação;
- reconciliação;
- Dataset Oficial 1986 somente após todos os gates.

Somente depois disso poderá ser avaliada a promoção de 1987.

## 8. Estado oficial

- M3-0 — **CONCLUÍDO**
- M3-1A — **CONCLUÍDO**
- M3-1B — **CONCLUÍDO**
- Reconciliação 2026 — **CONCLUÍDA**
- M3-1C — **APROVADO**
- M3-1D — **APROVADO**
- M3-1E — **APROVADO**
- M3-1 — **APROVADO**
- Fase histórica — **LIBERADA SOB GATES**
- 2026 — **DATASET OFICIAL**
- 1987 preexistente — **NÃO CERTIFICADO**
- 1986 — **PRÓXIMO GATE**
