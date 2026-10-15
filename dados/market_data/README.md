# Market Data — B3

| Campo | Valor |
|---|---|
| **ID** | B3-MARKETDATA-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_TECNICO |
| **Fase** | Market Data histórico e microestrutura |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 43d0c4160b91aff4383f66505da911f8025f5f0c5c702e6e01b1ce697b089e34 |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação técnica e aprovação humana |
| **Origem** | Fontes e documentação de Market Data B3 referenciadas no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Organizar os arquivos históricos oficiais da B3 usados para reconstruir preços, negócios, volume e métricas quantitativas.

## Hierarquia de fontes

### BVBG.086.01 — PriceReport
Arquivo completo de preços e demais valores de negociação, disponibilizado pela B3 ao fim do dia. A documentação oficial descreve o PriceReport como contendo informações completas de preços e valores de negociação. citeturn0search6

### BVBG.186.01 — Simplified Price Report — Equities
Versão simplificada para o mercado de ações.

### BVBG.187.01 — Simplified Price Report — Derivatives
Versão simplificada para o mercado de derivativos.

A página oficial de pesquisa por pregão disponibiliza atualmente esses três arquivos para consulta histórica. citeturn0search1turn0search2

## Limitação importante

BVBG.186.01 e BVBG.187.01 são relatórios simplificados de fim de dia. Eles não devem ser tratados como feed tick a tick.

Para reconstrução de microestrutura intradiária serão necessários arquivos com granularidade de negócios compatível com a métrica estudada.

## Métricas

A partir dos dados adequados, o projeto poderá calcular:

- retorno;
- amplitude;
- volatilidade;
- volume financeiro;
- VWAP;
- TWAP;
- distribuição temporal dos negócios;
- gaps;
- liquidez;
- estatísticas de execução.

Agressão e Cumulative Delta somente serão calculados quando a fonte permitir determinar, de forma auditável, o lado agressor ou uma metodologia de classificação explicitamente documentada.
