# FASE 07G — Matriz Final de Identidade Histórica COTAHIST 1986

**Arquivo:** FASE07G_COTAHIST_1986_MATRIZ_IDENTIDADE_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Tema:** Matriz auditável de identidade histórica  
**Caminho:** docs/ingestao/FASE07G_COTAHIST_1986_MATRIZ_IDENTIDADE_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo
Consolidar as evidências das frentes 07A–07F e recalcular K1, K2, K3 e K4 diretamente no RAW.

## Regras
- CODNEG é código de negociação, não identidade econômica permanente.
- TPMERC é dimensão de tipo de mercado.
- CODBDI é dimensão de classificação BDI.
- CODISI em 1986 é tratado como código interno do papel, não como ISIN.
- DIMES é atributo histórico de distribuição/estado de direito.
- K4 é chave analítica enriquecida e não é declarada chave econômica definitiva.

## Colisão residual
A matriz recupera novamente do RAW o grupo K4 residual previamente identificado e registra SHA-256 e campos objetivos dos registros. A ocorrência não é classificada automaticamente como duplicidade.

## Governança
RAW e NORMALIZED permanecem inalterados.

**Resultado:** dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_FINAL_V1.json
