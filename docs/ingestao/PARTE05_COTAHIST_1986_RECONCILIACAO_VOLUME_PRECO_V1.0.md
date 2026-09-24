# PARTE05 — Reconciliação QUATOT × VOLTOT × PREÇO — COTAHIST 1986

**Arquivo:** PARTE05_COTAHIST_1986_RECONCILIACAO_VOLUME_PRECO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Quantidade, volume, preço e fator de cotação  
**Caminho:** docs/ingestao/PARTE05_COTAHIST_1986_RECONCILIACAO_VOLUME_PRECO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Base normativa do teste

O layout oficial do COTAHIST define:

- PREULT: preço do último negócio;
- TOTNEG: número de negócios;
- QUATOT: quantidade total de títulos negociados;
- VOLTOT: volume total de títulos negociados;
- FATCOT: fator de cotação, com 1 para cotação unitária e 1000 para cotação por lote de mil ações.

Os campos de preço e VOLTOT têm duas casas decimais no layout. Portanto, a relação econômica entre preço, quantidade e volume **não pode ser tratada como identidade exata universal**.

## 2. Resultado da auditoria

Foram examinados **177.981 registros tipo 01** do COTAHIST 1986.

Distribuição de FATCOT:

| FATCOT | Registros |
|---:|---:|
| 1 | 23.586 |
| 1000 | 154.395 |

Foram encontrados **61 registros com VOLTOT = 0 e QUATOT > 0**.

A primeira classificação automática marcou esses registros como inconsistentes. A análise semântica posterior mostrou que todos os 61 possuem:

- FATCOT = 1000;
- TOTNEG = 1;
- quantidade pequena;
- PREULT positivo;
- valor teórico `PREULT × QUATOT ÷ FATCOT` igual ou inferior a **0,01**.

Como VOLTOT possui somente duas casas decimais, esses valores podem ser representados como **0,00** sem constituir erro do RAW.

## 3. Exemplo

Registro da linha 24.048:

- data: 04/03/1986;
- ativo: SUR 2;
- PREULT: 9,00;
- QUATOT: 1;
- FATCOT: 1000;
- TOTNEG: 1;
- VOLTOT: 0,00.

Valor econômico teórico:

`9,00 × 1 ÷ 1000 = 0,009`

Arredondado para duas casas decimais:

`0,01`

Dependendo da convenção histórica de gravação/arredondamento, a representação em centavos pode resultar em zero ou um centavo. Portanto, esse caso exige preservação do valor RAW e não autorização para “corrigir” VOLTOT.

## 4. Classificação final dos 61 casos

**VOLTOT_ZERO_COMPATIVEL_ARREDONDAMENTO_0_01: 61**

Não foi encontrado, nesta frente, nenhum caso classificado como:

- quantidade zero com volume não zero;
- quantidade negativa;
- volume negativo;
- preço negativo;
- FATCOT não positivo;
- outlier econômico comprovado.

## 5. Regra de integridade

A seguinte regra passa a integrar o contrato de qualidade:

> VOLTOT = 0 com QUATOT > 0 não é automaticamente erro. Antes de classificar como inconsistência, deve-se verificar preço, FATCOT, quantidade, número de negócios e resolução decimal do campo VOLTOT.

Também fica proibido usar simplesmente:

`VOLTOT = PREULT × QUATOT`

como regra universal.

Para FATCOT = 1000, o fator de cotação precisa ser considerado. Além disso, PREULT é o último negócio e não necessariamente o preço de todos os negócios que compõem QUATOT/VOLTOT.

## 6. Conclusão

**STATUS: RECONCILIADO — SEM ERRO ECONÔMICO COMPROVADO NESTA FRENTE.**

Os 61 registros anteriormente sinalizados permanecem no RAW e são classificados como casos compatíveis com a resolução monetária do campo VOLTOT.

Nenhum valor do RAW foi alterado.

## 7. Artefatos

- Script: `scripts/ingestao/auditar_quantidade_volume_preco_cotahist_1986_v1.py`
- Workflow: `.github/workflows/cotahist-quantidade-volume-preco-1986-v1.yml`
- Resultado: `dados/cotahist/quality/COTAHIST_1986_AUDITORIA_QUANTIDADE_VOLUME_PRECO_V1.json`

Schema do resultado: **1.1.0**

Workflow final: **36021101194 — success**

Commits principais:
- Script: `8c3db376830b1624c56906d83fb06a675afdcd01`
- Workflow: `2591c4ef4000db83e2d0dda7d905ca56d37d1365`

## 8. Fonte técnica

Layout oficial de Cotações Históricas da B3:
https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

A própria B3 informa que a série histórica contém dados desde 1986 e que as cotações são fornecidas na moeda e forma de cotação da época, sem ajustes posteriores.