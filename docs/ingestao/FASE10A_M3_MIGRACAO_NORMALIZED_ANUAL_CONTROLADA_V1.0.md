# FASE 10A — M3 — Migração NORMALIZED anual controlada V1.0

**Arquivo:** FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** M3-0 CONCLUÍDO — GIT_STANDARD_LIMIT — M3-1B CONCLUÍDO — MANIFEST 2026 RECONCILIADO — M3-1C LIBERADO

## 1. Objetivo

Migrar os anos COTAHIST ainda sem NORMALIZED anual físico para o caminho canônico:

`dados/cotahist/normalized/anual/COTAHIST_A{ANO}.csv`

mantendo:

- RAW imutável;
- parser 1.1.0;
- SHA-256;
- quality manifest;
- certificação física V2;
- rastreabilidade por commit;
- fail-closed.

## 2. Regra de segurança

Nenhum lote será iniciado antes do **Gate de Capacidade M3-0**.

Motivo: o tamanho do NORMALIZED pode ser muito superior ao ZIP RAW. A existência do RAW abaixo de 100 MB não prova que o CSV normalizado caberá no armazenamento Git padrão.

O contrato V2.0 exige interromper a migração se o limite de armazenamento/versionamento for atingido.

## 3. M3-0 — Gate de capacidade

Ano de referência:

**2026**

A execução deve:

1. regenerar NORMALIZED 2026 em `/tmp`;
2. calcular tamanho físico;
3. calcular SHA-256;
4. confirmar contagem/campos/datas contra o manifesto;
5. **não persistir o CSV**;
6. classificar:
   - `GIT_STANDARD_OK` se < 100 MB;
   - `GIT_STANDARD_LIMIT` se >= 100 MB;
7. registrar evidência.

## 4. Por que 2026 foi escolhido

O RAW 2026 já possui aproximadamente **84,5 MB** no repositório, enquanto 1987 demonstrou que a normalização pode expandir significativamente o volume físico.

Essa relação é apenas indicativa; o valor decisório será o tamanho real medido pela execução M3-0.

## 5. Regra de decisão

### Resultado M3-0 2026

NORMALIZED medido: **392.044.266 bytes**.

Decisão: **GIT_STANDARD_LIMIT**.

A persistência foi transferida para prova controlada em Git LFS.

### Regra quando NORMALIZED >= 100 MB

**PARAR no Git convencional.**

Não fazer:

- commit parcial;
- compressão manual para mascarar o limite;
- divisão arbitrária do CSV sem contrato;
- alteração do RAW;
- redução de campos;
- deduplicação.

Nesse caso foi executada a decisão técnica de Git LFS. A prova física 2026 foi concluída com sucesso e o manifest foi reconciliado.

## 6. Estratégia após aprovação do gate

A migração será feita em lotes pequenos, com preferência inicial para anos históricos de menor volume.

Cada ano:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY V2 → RECONCILE`

Um ano com falha não autoriza declarar o lote inteiro concluído.

## 7. Critérios de conclusão M3

Para cada ano migrado:

- CSV físico presente;
- tamanho validado;
- SHA físico = manifesto;
- linhas físicas = manifesto;
- schema = 25;
- datas coerentes;
- certificação física V2 = CERTIFICADO;
- commit de persistência registrado.

Depois dos lotes:

- Dataset Oficial V2 deve executar com SUCCESS;
- 1986 permanece com sua exceção semântica documentada;
- nenhum RAW é alterado.

## 8. Estado

M1 — **APROVADO**  
M2 — **APROVADO**  
M3-0 — **CONCLUÍDO — GIT_STANDARD_LIMIT**
M3-1A — **CONCLUÍDO**
M3-1B — **CONCLUÍDO — GIT LFS 2026**
Reconciliação manifest — **CONCLUÍDA**
M3-1C — **LIBERADO**
M3 histórico — **BLOQUEADO**

Próxima etapa: **M3-1C — validação CI do NORMALIZED 2026, seguida de M3-1D Dataset Oficial e M3-1E aprovação global.**

Registro formal: `docs/ingestao/M3-0_RESULTADO_GATE_CAPACIDADE_NORMALIZED_2026_2026-09-28.md`

Decisão M3-1: `docs/ingestao/M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md`


## 9. Atualização M3-1B — 2026-09-28

A divergência do manifest 2026 foi reconciliada. O RAW havia sido atualizado em 2026-09-24 após a criação do manifest NORMALIZED. O manifest foi alinhado ao RAW atual e ao NORMALIZED LFS fisicamente verificado.

- RAW SHA atual: `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`
- NORMALIZED SHA: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- Linhas: **2.919.760**
- Última data: **2026-09-23**
- M3-1C: **LIBERADO**
- Migração histórica: **CONTINUA BLOQUEADA ATÉ M3-1E**

Registro: `docs/ingestao/M3-1B_RECONCILIACAO_MANIFEST_NORMALIZED_2026_2026-09-28.md`.
