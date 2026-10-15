# Provedores e granularidade de Market Data B3

| Campo | Valor |
|---|---|
| **ID** | B3-MARKETDATA-PROVEDORES-GRANULARIDADE-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | MATRIZ_FONTES |
| **Fase** | Market Data — avaliação de provedores e granularidade |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 4098c1507167e1566f6012f3fe1bb18381e8e1ab6e925ea48241a985a855e7c8 |
| **Commit de referência (versão anterior)** | N/A — normalização inicial do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação técnica e aprovação humana |
| **Origem** | Documentação B3 de Market Data e matriz de avaliação interna |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Matriz inicial

| Fonte | EOD | Negócio a negócio | Agressor explícito | Uso |
|---|---:|---:|---:|---|
| BVBG.086.01 | Sim | conforme conteúdo do arquivo | a validar | histórico |
| BVBG.186.01 | Sim | Não tratar como tick feed | Não presumir | ações |
| BVBG.187.01 | Sim | Não tratar como tick feed | Não presumir | derivativos |
| Market Data intradiário | a definir | a definir | a definir | microestrutura |

## Critério

A ausência de evidência sobre um campo significa **não confirmado**, e não zero.

## Próxima validação

Capturar efetivamente um arquivo histórico de cada tipo e inspecionar:

- campos;
- número de registros;
- chaves;
- timestamps, se presentes;
- volume;
- preço médio;
- preço de abertura/mínimo/máximo/último;
- posições em aberto;
- eventuais indicadores de compra/venda.

Somente depois dessa inspeção será definida a arquitetura final de ingestão.
