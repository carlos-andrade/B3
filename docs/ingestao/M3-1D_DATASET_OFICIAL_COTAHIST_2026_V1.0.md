# M3-1D — Dataset Oficial COTAHIST 2026

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-7CEDC11768C1 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | APROVADO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 9bde71bc09cc386c06bc46037ef133deb822e8a26069c7f4cb211e2f351b6e71 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Proprietário do repositório — aprovação expressa registada em 2026-10-16 |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Caminho:** docs/ingestao/M3-1D_DATASET_OFICIAL_COTAHIST_2026_V1.0.md  
**Status:** CONCLUÍDO — DATASET_OFICIAL_VALIDADO

## Objetivo

Definir e validar o artefato canônico que representa o Dataset Oficial NORMALIZED do COTAHIST 2026.

## Artefato oficial

Manifesto:

`dados/cotahist/normalized/manifests/DATASET_OFICIAL_COTAHIST_2026.json`

Dataset canônico:

`dados/cotahist/normalized/anual/COTAHIST_A2026.csv`

## Execução oficial

- Workflow: `.github/workflows/cotahist-m3-1d-dataset-oficial-2026.yml`
- Run: `36428988106`
- Job: `108949989195`
- Commit avaliado: `e9576b486ab02dd3b27cdcdf9b9ba23fac83641d`
- Evento: `push`
- Resultado: `success`
- Evidência final: `M3-1D_STATUS=DATASET_OFICIAL_VALIDADO`

## Evidências

- Dataset oficial canônico: **OK**
- SHA: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- Registros: **2.919.760**
- Campos: **25**
- Primeira data: **2026-01-02**
- Última data: **2026-09-23**
- LFS materializado fisicamente: **OK**
- Tracking LFS: **OK**
- Checksum: **OK**
- Quality manifest: **OK**
- Validação semântica: **OK**

## Estado

**M3-1D CONCLUÍDO E APROVADO.**

O Dataset Oficial 2026 está validado como artefato canônico do NORMALIZED anual.

A migração histórica 1986–2025 permanece bloqueada até M3-1E.

## Próxima fase

Executar **M3-1E — Aprovação global**, que deverá consolidar M3-0, M3-1A, M3-1B, reconciliação, M3-1C e M3-1D, atualizar a documentação de governança e liberar formalmente a próxima etapa sem antecipar a migração histórica antes da certificação.


## 6. Revalidação e publicação — 2026-10-16

- Workflow: `.github/workflows/cotahist-m3-1d-dataset-oficial-2026.yml`
- Run: [38885204516](https://github.com/carlos-andrade/B3/actions/runs/38885204516)
- Resultado: `success`; `M3-1D_STATUS=DATASET_OFICIAL_VALIDADO`
- Estado do manifesto: `OFICIAL`
- Gate aprovado: `M3-1E`
- Parser: `1.1.2`
- RAW SHA-256: `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e`
- NORMALIZED SHA-256: `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`
- Registos: 3.142.910; campos: 25; intervalo: 2026-01-02 a 2026-10-13.
- Git LFS materializado fisicamente; checksum, manifest de qualidade e Dataset Oficial coerentes.

**Decisão:** M3-1D APROVADO; Dataset Oficial COTAHIST 2026 publicado.
