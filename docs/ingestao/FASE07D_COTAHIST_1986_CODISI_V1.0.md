# FASE 07D — CODISI do COTAHIST 1986

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-EBBAC62FB0F4 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 801a1c927e0c1918f91d28977208b246ecd08c03d547a49b939a01fe7c3ddf2d |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** FASE07D_COTAHIST_1986_CODISI_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação histórica do campo CODISI  
**Caminho:** docs/ingestao/FASE07D_COTAHIST_1986_CODISI_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo
Determinar como CODISI deve ser interpretado para 1986 e medir presença, cardinalidade e relações com CODNEG/TPMERC.

## Evidência oficial B3
CODISI ocupa as posições 231–242. O layout B3 descreve o campo como código do papel no sistema ISIN ou código interno do papel e estabelece que o código ISIN é utilizado a partir de 15/05/1995. Portanto, para COTAHIST 1986, esta frente trata CODISI como código interno, não como ISIN. Fonte: B3, Layout do Arquivo – Cotações Históricas, revisão 02. Referência pública para layouts: [Layout dos arquivos — Pesquisa por Pregão, B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/layout-dos-arquivos/). A cópia exata da revisão 02 deve ser preservada com data e hash antes de ser usada como evidência primária.

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
