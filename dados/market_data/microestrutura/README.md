# Microestrutura

| Campo | Valor |
|---|---|
| **ID** | B3-MARKETDATA-MICROESTRUTURA-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_TECNICO |
| **Fase** | Market Data — microestrutura |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 076b61adb76f33a720568634d105bd8963aab4ba42d7288f6ab1c2e989001fe9 |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação metodológica e aprovação humana |
| **Origem** | Plano metodológico de Market Data e microestrutura B3 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
