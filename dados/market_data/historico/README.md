# Histórico de Market Data

| Campo | Valor |
|---|---|
| **ID** | B3-MARKETDATA-HISTORICO-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_TECNICO |
| **Fase** | Market Data histórico |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 05aa05ebf1241b64e72714ab33fea298e3e1a58985354e5764f1f370f24ff666 |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação técnica e aprovação humana |
| **Origem** | Arquivos históricos e documentação de Market Data da B3 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Arquivos prioritários

| Arquivo | Mercado | Granularidade | Uso |
|---|---|---|---|
| BVBG.086.01 | Geral | EOD / completo | reconstrução histórica |
| BVBG.186.01 | Ações | EOD / simplificado | OHLC, média, negócios e campos disponíveis |
| BVBG.187.01 | Derivativos | EOD / simplificado | preços, média, negócios, posições/campos disponíveis |

A B3 confirma a disponibilidade desses arquivos na pesquisa por pregão. citeturn0search1

## Estrutura por data

`YYYY-MM-DD/`

Cada captura deve conter:

- arquivo bruto;
- hash SHA-256;
- manifesto;
- validação estrutural;
- versão normalizada, quando necessária.

## Regra

Nunca substituir o arquivo bruto por uma versão tratada.
