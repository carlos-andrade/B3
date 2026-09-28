# M3-1 — Decisão de armazenamento do NORMALIZED anual COTAHIST V1.0

**Arquivo:** M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** M3-1C CONCLUÍDO — M3-1D IMPLEMENTADO — EXECUÇÃO M3-1D PENDENTE

## 1. Contexto

O Gate M3-0 de capacidade foi executado para o COTAHIST 2026.

Resultado físico:

- NORMALIZED: **392.044.266 bytes**
- limite operacional do gate: **100.000.000 bytes**
- SHA-256 NORMALIZED: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- registros tipo 01: **2.919.760**
- campos: **25**
- primeira data: **2026-01-02**
- última data: **2026-09-23**
- decisão M3-0: **GIT_STANDARD_LIMIT**

## 2. Decisão arquitetural

O mecanismo físico aprovado para NORMALIZED anual acima do limite operacional de Git convencional é **Git LFS**, mantendo caminho lógico canônico, versionamento, recuperação física, SHA-256, CI e fail-closed.

A aprovação global de M3-1 continua condicionada à conclusão de M3-1D e M3-1E.

## 3. M3-1A — Preparação — CONCLUÍDA

Tracking LFS:

`dados/cotahist/normalized/anual/*.csv filter=lfs diff=lfs merge=lfs -text`

Arquivo:

`.gitattributes`

## 4. M3-1B — Prova física 2026 — CONCLUÍDA

Workflow:

`.github/workflows/cotahist-m3-1b-prova-lfs-2026.yml`

Evidência:

- Run: `36419262539`
- Job: `108917764369`
- Commit de persistência: `dcb7dd16649245d0ac3e9f58a1bca521941e7fb1`
- NORMALIZED: **392.044.266 bytes**
- SHA físico: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- LFS materializado fisicamente com sucesso.

## 5. Reconciliação do manifest — CONCLUÍDA

A divergência anterior foi classificada como **MANIFESTO DEFASADO EM RELAÇÃO AO RAW ATUAL**, após atualização posterior do RAW.

Manifest corrigido:

- RAW SHA: `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`
- NORMALIZED SHA: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- linhas: **2.919.760**
- campos: **25**
- primeira data: **2026-01-02**
- última data: **2026-09-23**

Evidência:

`dados/cotahist/quality/COTAHIST_A2026_RECONCILIACAO_MANIFEST_V1.json`

## 6. M3-1C — CI — CONCLUÍDO E APROVADO

Workflow:

`.github/workflows/cotahist-m3-1c-ci-normalized-2026.yml`

Execução oficial:

- Run: `36428513803`
- Job: `108948384728`
- Commit avaliado: `a06d7b9dd55525210cfa2ae878b29dcfbbf025bb`
- Resultado: `success`
- Evidência final: `M3-1C_STATUS=CI_INTEGRIDADE_APROVADA`

Principais evidências:

- reconstrução RAW → NORMALIZED: **OK**;
- SHA: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`;
- registros: **2.919.760**;
- primeira data: **2026-01-02**;
- última data: **2026-09-23**;
- 25 campos.

Registro:

`docs/ingestao/M3-1C_CI_INTEGRIDADE_NORMALIZED_2026_V1.0.md`

## 7. M3-1D — Dataset Oficial — IMPLEMENTADO

Foi criado o manifesto canônico:

`dados/cotahist/normalized/manifests/DATASET_OFICIAL_COTAHIST_2026.json`

E o gate:

`.github/workflows/cotahist-m3-1d-dataset-oficial-2026.yml`

O gate valida:

- acesso físico ao CSV materializado;
- tracking LFS;
- canonicalidade do caminho;
- manifesto oficial;
- checksum e SHA;
- alinhamento com o quality manifest;
- cardinalidade e 25 campos;
- primeira/última data;
- validação semântica.

**M3-1D ainda não está aprovado.** A aprovação dependerá da execução real do workflow com:

`M3-1D_STATUS=DATASET_OFICIAL_VALIDADO`

## 8. M3-1E — Aprovação global

Somente após M3-1D aprovado:

**M3-1 = APROVADO**

Antes disso, a migração histórica 1986–2025 permanece bloqueada.

## 9. Governança

É proibido:

- persistir NORMALIZED anual em Git convencional acima do limite operacional;
- dividir CSV arbitrariamente;
- reduzir campos para caber;
- deduplicar para reduzir volume;
- alterar RAW para obter um NORMALIZED menor;
- aprovar manifest sem verificar o RAW atual.

Cadeia oficial:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY → RECONCILE`

## 10. Estado atual

- **M3-0:** CONCLUÍDO — GIT_STANDARD_LIMIT
- **M3-1A:** CONCLUÍDO
- **M3-1B:** CONCLUÍDO — PROVA FÍSICA LFS 2026
- **Reconciliação manifest 2026:** CONCLUÍDA
- **M3-1C:** CONCLUÍDO — CI_INTEGRIDADE_APROVADA
- **M3-1D:** IMPLEMENTADO — EXECUÇÃO PENDENTE
- **M3-1E:** BLOQUEADO ATÉ M3-1D
- **M3 histórico 1986–2025:** BLOQUEADO
- **RAW:** PRESERVADO
- **Parser:** 1.1.0
- **NORMALIZED 2026:** PERSISTIDO VIA GIT LFS

## 11. Critério de aprovação M3-1

M3-1 somente poderá ser aprovado quando:

- LFS disponível;
- quota suficiente ou política definida;
- 2026 persistido;
- SHA reproduzível;
- M3-1C aprovado;
- Dataset Oficial validado;
- documentação atualizada;
- RAW preservado;
- nenhuma divergência de integridade permanecer aberta.
