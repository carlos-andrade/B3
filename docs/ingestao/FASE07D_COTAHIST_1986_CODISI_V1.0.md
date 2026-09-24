# FASE 07D — CODISI do COTAHIST 1986

**Arquivo:** FASE07D_COTAHIST_1986_CODISI_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação histórica do campo CODISI  
**Caminho:** docs/ingestao/FASE07D_COTAHIST_1986_CODISI_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo
Determinar como CODISI deve ser interpretado para 1986 e medir presença, cardinalidade e relações com CODNEG/TPMERC.

## Evidência oficial B3
CODISI ocupa as posições 231–242. O layout B3 descreve o campo como código do papel no sistema ISIN ou código interno do papel e estabelece que o código ISIN é utilizado a partir de 15/05/1995. Portanto, para COTAHIST 1986, esta frente trata CODISI como código interno, não como ISIN. Fonte: B3, Layout do Arquivo – Cotações Históricas, revisão 02. citeturn1view0

## Regras
- CODISI de 1986 não será rotulado como ISIN.
- Valores não vazios serão classificados como CODIGO_INTERNO_1986.
- Valores vazios permanecem vazios.
- Nenhuma equivalência CODISI = CODNEG será presumida.
- CODISI não será chave econômica definitiva isolada.

## Métricas
O analisador calcula total de registros, preenchimento, cardinalidade, tamanho, pregões, CODNEG distintos e distribuição de TPMERC por CODISI.

## Artefatos
Script: scripts/ingestao/analisar_codisi_cotahist_1986_v1.py  
Resultado esperado: dados/cotahist/quality/COTAHIST_1986_CODISI_V1.json

## Governança
RAW e NORMALIZED permanecem inalterados.

## Próxima frente
**07E — DIMES.**
