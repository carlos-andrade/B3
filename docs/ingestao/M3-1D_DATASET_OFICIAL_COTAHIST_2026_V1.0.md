# M3-1D — Dataset Oficial COTAHIST 2026

**Caminho:** docs/ingestao/M3-1D_DATASET_OFICIAL_COTAHIST_2026_V1.0.md  
**Status:** IMPLEMENTADO — EXECUÇÃO PENDENTE

## Objetivo

Definir e validar o artefato canônico que representa o Dataset Oficial NORMALIZED do COTAHIST 2026.

## Artefato oficial

Manifesto:

`dados/cotahist/normalized/manifests/DATASET_OFICIAL_COTAHIST_2026.json`

Dataset canônico:

`dados/cotahist/normalized/anual/COTAHIST_A2026.csv`

O manifesto aponta explicitamente para RAW, NORMALIZED, quality manifest e checksum, além de registrar parser, SHA, cardinalidade e intervalo temporal.

## Gate

Workflow:

`.github/workflows/cotahist-m3-1d-dataset-oficial-2026.yml`

O gate verifica:

1. presença física do RAW;
2. presença física do NORMALIZED via Git LFS;
3. tracking LFS;
4. ausência de ponteiro LFS como conteúdo final;
5. manifesto oficial;
6. canonicalidade do caminho;
7. SHA físico;
8. checksum;
9. SHA do quality manifest;
10. cardinalidade;
11. 25 campos;
12. primeira e última data;
13. validação semântica.

Qualquer divergência interrompe o workflow.

## Regra de aprovação

M3-1D somente será considerado concluído após execução real do workflow com:

`M3-1D_STATUS=DATASET_OFICIAL_VALIDADO`

Até essa execução, o estado permanece **PENDENTE**.

## Estado

M3-1C está aprovado.

M3-1D foi implementado e aguarda execução.

A migração histórica 1986–2025 permanece bloqueada até M3-1E.
