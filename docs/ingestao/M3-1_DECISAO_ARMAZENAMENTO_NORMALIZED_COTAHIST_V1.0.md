# M3-1 — Decisão de armazenamento do NORMALIZED anual COTAHIST V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-F26358B1E9E3 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | APROVADO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | d1c1f30c4e2c5387093429d4582008ea81b12e6f30aab083aa300ae5cff98aa4 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Proprietário do repositório — aprovação expressa registada em 2026-10-16 |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md  
**Data:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** **M3-1 APROVADO — Git LFS validado — Dataset Oficial 2026 aprovado — M3-1E concluído**

## 1. Decisão

O mecanismo físico aprovado para NORMALIZED anual acima do limite operacional de Git convencional é **Git LFS**, mantendo caminho lógico canônico, versionamento, recuperação física, SHA-256, CI e fail-closed.

## 2. Evidências consolidadas

- M3-0: **CONCLUÍDO — GIT_STANDARD_LIMIT**
- M3-1A: **CONCLUÍDO**
- M3-1B: **CONCLUÍDO — PROVA FÍSICA LFS 2026**
- Reconciliação do manifest 2026: **CONCLUÍDA**
- M3-1C: **APROVADO — CI_INTEGRIDADE_APROVADA**
- M3-1D: **APROVADO — DATASET_OFICIAL_VALIDADO**
- M3-1E: **APROVADO — APROVACAO_GLOBAL_CONCLUIDA**
- RAW: **PRESERVADO**
- NORMALIZED 2026: **PERSISTIDO VIA GIT LFS**

### Dataset Oficial 2026

- RAW SHA-256: `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`
- NORMALIZED SHA-256: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- registros: **2.919.760**
- campos: **25**
- primeira data: **2026-01-02**
- última data: **2026-09-23**
- parser: **1.1.0**

### Gate M3-1E

- Workflow: `.github/workflows/cotahist-m3-1e-aprovacao-global.yml`
- Run: **36429403166**
- Job: **108951402371**
- Commit avaliado: `c890e5dcdc96041199fe255b37165b73df1bad58`
- Conclusão: **success**
- Evidência: `M3-1E_STATUS=APROVACAO_GLOBAL_CONCLUIDA`

Registro detalhado:

`docs/ingestao/M3-1E_APROVACAO_GLOBAL_COTAHIST_2026_V1.0.md`

## 3. Governança

É proibido:

- persistir NORMALIZED anual acima do limite em Git convencional;
- dividir CSV arbitrariamente;
- reduzir campos;
- deduplicar para reduzir volume;
- alterar RAW para obter NORMALIZED menor;
- aprovar manifest sem verificar o RAW atual;
- promover arquivo histórico preexistente a Dataset Oficial sem os gates correspondentes.

Cadeia oficial:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY → RECONCILE`

## 4. Anomalia histórica identificada

Durante o checkout LFS do gate M3-1E, o runner registrou:

`Encountered 1 file that should have been a pointer, but wasn't: dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

O fato não invalida a aprovação de 2026, mas significa que o arquivo 1987 preexistente **não está certificado pelo processo M3**.

Ele deverá ser auditado antes de qualquer promoção para Dataset Oficial.

## 5. Estado atual

- **M3-0:** CONCLUÍDO
- **M3-1A:** CONCLUÍDO
- **M3-1B:** CONCLUÍDO
- **Reconciliação 2026:** CONCLUÍDA
- **M3-1C:** APROVADO
- **M3-1D:** APROVADO
- **M3-1E:** APROVADO
- **M3-1:** **APROVADO**
- **NORMALIZED 2026:** OFICIAL / GIT LFS
- **1987 preexistente:** NÃO CERTIFICADO
- **RAW:** PRESERVADO
- **Parser:** 1.1.0

## 6. Próximo gate

A aprovação de M3-1 libera a fase histórica, mas não elimina a regra semântica especial do projeto:

**1986 deve ser reconciliado antes da liberação de 1987.**

A reconciliação de 1986 deverá cobrir `tpmerc`, `codbdi`, chave lógica, 30 casos OHLC, volume/quantidade, calendário de pregão e amostras comparadas com RAW, além de SHA, reconstrução determinística, persistência, certificação e reconciliação.


## 6. Aditamento decisório — 2026-10-16

A adoção do Git LFS para NORMALIZED anual acima do limite do Git convencional e a publicação do Dataset Oficial 2026 foram confirmadas pelos gates atuais.

- M3-1C: run 38884804282 — success.
- M3-1D: run 38885204516 — success.
- M3-1E: run 38885204284 — success.
- Dataset Oficial V2: run 38885204334 — success.
- RAW SHA-256: `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e`.
- NORMALIZED SHA-256: `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`.
- Parser 1.1.2; 3.142.910 registos; 25 campos; 2026-01-02 a 2026-10-13.

A divergência entre a versão histórica do manifesto e a camada NORMALIZED atual foi reconciliada. Os workflows validam a versão do parser dinamicamente e comparam extremos calendáricos, sem presumir que a ordem física do CSV é cronológica.

**Decisão vigente:** Git LFS é o mecanismo de persistência aprovado para NORMALIZED anual de grande dimensão. A aprovação global não substitui a certificação individual dos anos históricos.
