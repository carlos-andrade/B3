# Status da migração das fontes B3 — 2026-09-23

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-007-S-B3-2026-09-23-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_DE_FONTES |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | df969eabda04a9869bd09c322eb132000b9697e69f9d218af8cd291ab7654c37 |
| **Commit de referência (versão anterior)** | [7a09339f3244b84dd165400279b6da090bd2bb80](https://github.com/carlos-andrade/B3/commit/7a09339f3244b84dd165400279b6da090bd2bb80) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


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
