# M2 — Integração física com Dataset Oficial COTAHIST V2.0

**Arquivo:** FASE10A_M2_DATASET_OFICIAL_FISICO_V2.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M2_DATASET_OFICIAL_FISICO_V2.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** IMPLEMENTADO — PUBLICAÇÃO BLOQUEADA ATÉ M3

## Objetivo

Eliminar a inconsistência arquitetural em que o Dataset Oficial declarava arquivos NORMALIZED sem exigir sua existência física.

A V2 passa a exigir:

`RAW + NORMALIZED físico + QUALITY + CERTIFICAÇÃO FÍSICA → DATASET OFICIAL`

## Implementação

Script:

`scripts/ingestao/gerar_dataset_oficial_cotahist_v2.py`

Workflow:

`.github/workflows/cotahist-dataset-oficial-v2.yml`

Dataset de saída:

`dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json`

## Regra fail-closed

O Dataset Oficial V2 **não é publicado** se qualquer ano de 1986–2026 apresentar:

- RAW ausente;
- NORMALIZED ausente;
- quality manifest ausente/inválido;
- certificação física V2 ausente;
- SHA físico divergente;
- caminho NORMALIZED não canônico;
- quantidade/certificação física incompatível.

## Estado atual

O ano **1987** já possui:

- NORMALIZED físico persistido;
- SHA reconciliado;
- certificação física V2 aprovada;
- evidência versionada.

Os demais anos ainda não possuem NORMALIZED anual físico no caminho canônico. Portanto, a publicação do Dataset Oficial V2 permanece corretamente bloqueada.

## Decisão

Esta etapa não autoriza publicação parcial do Dataset Oficial.

A publicação somente ocorrerá quando M3 concluir a persistência/certificação dos anos necessários e o workflow V2 retornar SUCCESS.

## Próxima etapa

**M3 — persistência NORMALIZED anual em lotes controlados**, começando pelos anos definidos na matriz de migração.
