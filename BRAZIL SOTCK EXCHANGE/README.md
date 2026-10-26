# BRAZIL SOTCK EXCHANGE

Pasta de referência, investigação e desenvolvimento quantitativo relacionados com a B3 — Brasil, Bolsa, Balcão.

**Documento de referência:** [B3_REFERENCIA_GERAL.md](B3_REFERENCIA_GERAL.md)  
**Data de criação da estrutura:** 2026-10-26

## Estrutura oficial do projeto

| Pasta | Finalidade |
|---|---|
| [00_GOVERNANCA/](00_GOVERNANCA/) | Metodologia, decisões, licenças e critérios de promoção |
| [01_DADOS/](01_DADOS/) | Pipeline de dados, esquemas e camadas RAW/STAGING/CANONICAL |
| [02_MICROESTRUTURA/](02_MICROESTRUTURA/) | VWAP/TWAP, volume, CVD, liquidez e execução |
| [03_MACRO/](03_MACRO/) | Calendário económico e indicadores oficiais |
| [04_ESTRATEGIAS/](04_ESTRATEGIAS/) | Especificações, NTSL e backtests |
| [05_RELATORIOS/](05_RELATORIOS/) | Relatórios de análise, validação e desempenho |
| [06_AUDITORIA/](06_AUDITORIA/) | Hashes, reconciliações, gates e exceções |
| [07_FONTES_OFICIAIS/](07_FONTES_OFICIAIS/) | Catálogo de fontes, formatos e direitos de uso |

## Regras de governação

1. Distinguir factos verificados, cálculos, hipóteses e inferências.
2. Registar fonte, data de referência, timezone, versão e hash sempre que aplicável.
3. Preservar os dados RAW sem alteração; não guardar no repositório dados cuja licença proíba a sua distribuição.
4. Promover dados apenas após validação de esquema, contagens, duplicados, cobertura, licença e reconciliação.
5. Versionar código, parâmetros, resultados e decisões.
6. Não declarar uma estratégia validada sem custos, slippage, gestão de risco, testes fora da amostra e métricas reproduzíveis.
7. Não prometer rentabilidade; documentar drawdown, incerteza e limitações.

## Convenções

- Nomes de pastas numerados para manter a ordem de leitura.
- Datas em formato ISO 8601 (YYYY-MM-DD); timestamps com timezone explícito.
- Dados de mercado e eventos macro devem distinguir data de referência de data/hora de publicação.
- Cada execução automatizada deve produzir logs e artefactos de auditoria.

As subpastas são representadas por ficheiros README.md, pois o Git não versiona diretórios vazios.
