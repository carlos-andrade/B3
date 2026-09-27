# INVENTÁRIO BCB/SGS — NÚCLEO MACRO B3 V1

**Arquivo:** INVENTARIO_BCB_SGS_NUCLEO_MACRO_V1.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Caminho:** governanca/bcb_sgs/INVENTARIO_BCB_SGS_NUCLEO_MACRO_V1.md  
**Data:** 27/09/2026  
**Repositório:** carlos-andrade/B3

## Escopo inicial certificável

Este núcleo cobre as séries BCB/SGS prioritárias para contexto macroeconômico e backtests da B3:

| Código SGS | Série | Frequência | Unidade | Fonte |
|---:|---|---|---|---|
| 432 | Meta Selic definida pelo Copom | diária | % a.a. | BCB/Copom |
| 11 | Taxa Selic efetiva | diária | % a.a. | BCB |
| 12 | CDI | diária | % a.d. | Cetip/BCB |
| 1 | Dólar americano venda | diária | BRL/USD | BCB |
| 433 | IPCA | mensal | % mensal | IBGE via SGS |

A existência dessas séries é confirmada pelo catálogo/API do Banco Central. A API SGS impõe, desde 26/03/2025, limite de 10 anos para consultas JSON/CSV de séries diárias, exigindo consultas por janelas. citeturn1search0turn1search1

## Critério de certificação

Cada série precisa possuir:

1. RAW original retornado pela API;
2. metadados de captura;
3. SHA-256 RAW;
4. NORMALIZED CSV;
5. SHA-256 NORMALIZED;
6. contagem de observações;
7. primeira e última data;
8. duplicidade zero na chave série+data;
9. datas válidas;
10. valores numéricos ou NULL explicitamente aceito;
11. ausência de datas futuras indevidas;
12. manifesto QUALITY com status VALIDADO;
13. workflow com execução comprovada;
14. índice corrente consolidado.

## Regra de frescor

Para séries diárias, a referência é o último pregão/observação efetivamente disponibilizado pelo BCB. Para séries mensais, a referência é o último período publicado.

O workflow não certifica apenas porque executou. O manifesto deve demonstrar a qualidade do dado.

## Expansão futura

Depois do núcleo, serão adicionados grupos BCB/SGS de:

- inflação e núcleos;
- atividade econômica;
- crédito;
- emprego;
- setor fiscal;
- setor externo;
- agregados monetários;
- expectativas/Fundamental Focus;
- séries necessárias à modelagem macro da B3.

A expansão será feita por catálogo explícito de códigos, nunca por captura indiscriminada de toda a base SGS.

## Fontes oficiais

- Portal de Dados Abertos BCB/SGS.
- API BCData/SGS.
- Metadados oficiais de cada série.

A série 432 é diária, começa em 05/03/1999 e representa a meta Selic definida pelo Copom. citeturn1search0  
A série 1 é diária e representa a cotação de venda do dólar americano, com início em 28/11/1984. citeturn1search1  
A série 433 é o IPCA mensal; fontes que documentam o SGS identificam a série 433 como IPCA, com dados desde 1980. citeturn4search0  
A série 12 é o CDI diário, com dados desde 06/03/1986. citeturn4search1
