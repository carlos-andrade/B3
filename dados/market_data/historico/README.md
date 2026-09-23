# Histórico de Market Data

**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Arquivamento histórico de arquivos B3  
**Caminho:** dados/market_data/historico/README.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

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
