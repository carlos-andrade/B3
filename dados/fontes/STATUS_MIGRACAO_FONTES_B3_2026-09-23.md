# Status da migração das fontes B3 — 2026-09-23

## Objetivo

Migrar a ingestão do repositório `carlos-andrade/B3` das rotas legadas descontinuadas para as fontes atuais da B3, preservando evidência, data, URL, SHA-256 e validações.

## Estado atual

| Camada | Dataset / fonte | Estado | Evidência |
|---|---|---|---|
| Cadastro | BVBG.028.02 / Instruments | Em validação | Pesquisa por Pregão; arquivo `IN{aammdd}.zip` |
| BDI | DailyAverageStocks | Captura automatizada em teste | API POST BDI; endpoint date-addressed |
| Mercado | BVBG.086.01 | Mapeado | Pesquisa por Pregão |
| Mercado | BVBG.087.01 | Mapeado | Pesquisa por Pregão |
| Mercado | BVBG.186.01 | Mapeado | Pesquisa por Pregão |
| Mercado | BVBG.187.01 | Mapeado | Pesquisa por Pregão |
| Cadastro | BVBG.029.02 | Mapeado | Pesquisa por Pregão |

## Regra de validação

Nenhum inventário quantitativo será considerado oficial antes de:

1. captura do payload/arquivo original;
2. registro da URL e data;
3. SHA-256;
4. validação estrutural;
5. contagem de registros;
6. validação de chaves/códigos;
7. manifesto de captura;
8. publicação no repositório.

## Migração da API legada

A rota `/api/download/requestname` apresentou HTTP 400 nos testes realizados em 2026-09-23 e não deve mais ser tratada como rota operacional.

## Próxima validação

Executar o workflow da captura BDI e verificar:

- HTTP;
- JSON;
- presença de `table.columns`;
- presença de `table.values`;
- número de registros;
- SHA-256;
- persistência em `dados/bdi/raw/`;
- manifesto em `dados/bdi/manifests/`.

Após validar o BDI, implementar a captura real do BVBG.028.02 pela Pesquisa por Pregão e, em seguida, os demais layouts.
