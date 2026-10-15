# FASE 07G — Matriz Final de Identidade Histórica COTAHIST 1986

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-158450DF0C73 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 13fe29d44144ec7ebd82ae3677223ca715d8aceb3b2127d5beb80684f35ef5af |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
