# FASE 07B — TPMERC do COTAHIST 1986

**Arquivo:** FASE07B_COTAHIST_1986_TPMERC_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação semântica histórica do campo TPMERC  
**Caminho:** docs/ingestao/FASE07B_COTAHIST_1986_TPMERC_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo
Determinar os códigos TPMERC observados no COTAHIST 1986 e confrontá-los com a tabela oficial B3.

## Evidência oficial
O layout B3 define TPMERC nas posições 25–27 do registro tipo 01 como o código do mercado em que o papel está cadastrado. A tabela publicada pela B3 contém: 010 VISTA; 012 EXERCÍCIO DE OPÇÕES DE COMPRA; 013 EXERCÍCIO DE OPÇÕES DE VENDA; 017 LEILÃO; 020 FRACIONÁRIO; 030 TERMO; 050 FUTURO COM RETENÇÃO DE GANHO; 060 FUTURO COM MOVIMENTAÇÃO CONTÍNUA; 070 OPÇÕES DE COMPRA; 080 OPÇÕES DE VENDA.

Fonte: B3, *LAYOUT DO ARQUIVO – COTAÇÕES HISTÓRICAS*, revisão 01, 13/04/2017.

## Regra de interpretação
A tabela de 2017 é evidência documental B3, mas sua data não prova isoladamente que a semântica textual era idêntica em 1986. Códigos observados serão marcados como documentados no layout; códigos não documentados não receberão significado inventado. TPMERC é atributo de classificação de mercado, não identidade econômica permanente.

## Artefatos
Script: scripts/ingestao/analisar_tpmerc_cotahist_1986_v1.py  
Resultado: dados/cotahist/quality/COTAHIST_1986_TPMERC_V1.json

## Governança
RAW e NORMALIZED não podem ser alterados por esta frente. A conclusão histórica definitiva exige validação temporal adicional quando houver necessidade de provar continuidade semântica até 1986.

## Próxima frente
Após execução e auditoria do JSON: **07C — CODBDI**.