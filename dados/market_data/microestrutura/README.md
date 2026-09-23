# Microestrutura

**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Microestrutura de mercado  
**Caminho:** dados/market_data/microestrutura/README.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo

Construir uma camada específica para estudos intradiários de:

- agressão;
- volume por negócio;
- Cumulative Delta;
- VWAP;
- TWAP;
- liquidez;
- desequilíbrio comprador/vendedor;
- gaps e FVG;
- comportamento temporal.

## Regra metodológica

Não inferir agressão somente a partir de OHLC.

Se a fonte não identificar o lado agressor, qualquer classificação deverá:

1. declarar o algoritmo utilizado;
2. indicar suas limitações;
3. distinguir observação de inferência;
4. permitir reprodução.

## Cumulative Delta

Definição operacional futura:

`Delta_t = Volume_Agressor_Comprador,t - Volume_Agressor_Vendedor,t`

`CumulativeDelta_t = Σ Delta_i`

A implementação somente será considerada validada quando a origem dos volumes e a regra de classificação forem documentadas.

## VWAP

`VWAP = Σ(Preço_i × Volume_i) / ΣVolume_i`

A sessão, janela temporal e tratamento de negócios fora do fluxo principal deverão ser registrados.

## TWAP

A metodologia deverá especificar:

- janela;
- frequência de amostragem;
- preço utilizado;
- tratamento de intervalos sem negócio.
