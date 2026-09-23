# Market Data — B3

**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Market Data histórico e microestrutura  
**Caminho:** dados/market_data/README.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

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
