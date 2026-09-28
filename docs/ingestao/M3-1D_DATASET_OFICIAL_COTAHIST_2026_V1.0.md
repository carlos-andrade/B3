# M3-1D — Dataset Oficial COTAHIST 2026

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
