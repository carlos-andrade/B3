# PARTE 01 — CONTRATO DA CAMADA NORMALIZED COTAHIST V1.0

**Arquivo:** PARTE01_CONTRATO_NORMALIZED_COTAHIST_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Normalização reproduzível da série histórica COTAHIST  
**Caminho:** docs/ingestao/PARTE01_CONTRATO_NORMALIZED_COTAHIST_V1.0.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo

Criar uma camada NORMALIZED reproduzível a partir do RAW oficial COTAHIST, sem alterar o arquivo original.

A fonte oficial da B3 define o COTAHIST como arquivo anual com registros de 245 bytes, contendo header 00, cotações 01 e trailer 99. O registro 01 contém data, código de negociação, tipo de mercado, preços, negócios, quantidade, volume e identificadores. citeturn0search12turn0search0

## Princípios

1. RAW é a evidência primária e nunca é sobrescrito.
2. NORMALIZED é derivada exclusivamente do RAW.
3. Cada transformação deve ser reproduzível pelo parser versionado.
4. Campos textuais são preservados após remoção apenas de espaços de preenchimento.
5. Datas são convertidas de AAAAMMDD para ISO 8601 (AAAA-MM-DD).
6. Campos de preço são convertidos conforme a escala de duas casas indicada pela B3.
7. Volume é convertido conforme a escala definida no layout.
8. Campos vazios permanecem vazios; não são convertidos arbitrariamente em zero.
9. Nenhum ajuste de inflação, provento ou corporate action é aplicado nesta etapa.
10. A camada NORMALIZED não representa fluxo, agressão, Cumulative Delta ou microestrutura.

## Campos normalizados

| Campo | Origem | Tratamento |
|---|---:|---|
| data_pregao | 03–10 | ISO date |
| codbdi | 11–12 | texto |
| codneg | 13–24 | texto |
| tpmerc | 25–27 | texto |
| nomres | 28–39 | texto |
| especi | 40–49 | texto |
| prazot | 50–52 | texto |
| modref | 53–56 | texto |
| preabe | 57–69 | preço / 2 casas |
| premax | 70–82 | preço / 2 casas |
| premin | 83–95 | preço / 2 casas |
| premed | 96–108 | preço / 2 casas |
| preult | 109–121 | preço / 2 casas |
| preofc | 122–134 | preço / 2 casas |
| preofv | 135–147 | preço / 2 casas |
| totneg | 148–152 | inteiro |
| quatot | 153–170 | inteiro |
| voltot | 171–188 | numérico |
| preexe | 189–201 | preço / 2 casas |
| indopc | 202 | texto |
| datven | 203–210 | ISO date |
| fatcot | 211–217 | inteiro |
| ptoexe | 218–230 | preço / 6 casas |
| codisi | 231–242 | texto |
| dismes | 243–245 | texto |

As posições acima seguem o layout oficial B3, revisão 02, de 05/10/2020. citeturn1view0

## Chave operacional

A chave candidata inicial é:

`data_pregao + codbdi + codneg + tpmerc + dismes`

Ela será testada empiricamente por ano. Não será declarada como chave primária definitiva antes da análise de duplicidades.

## Controle de qualidade

Para cada ano normalizado deverão ser registrados:

- quantidade de registros 01 no RAW;
- quantidade de linhas no NORMALIZED;
- primeira data;
- última data;
- duplicidades da chave candidata;
- datas inválidas;
- preços negativos ou estruturalmente impossíveis;
- inconsistências entre campos;
- SHA-256 do RAW;
- versão do parser;
- data/hora da normalização.

## Limitação histórica

O layout oficial é a referência do parser. Caso algum ano apresente alteração estrutural, encoding incompatível ou campos que não possam ser interpretados pelo contrato atual, o ano será marcado como **REVISÃO NECESSÁRIA**, e não será forçada uma conversão.

## Separação de camadas

```
RAW B3
  ↓
VALIDAÇÃO ESTRUTURAL
  ↓
NORMALIZED COTAHIST
  ↓
INSTRUMENT MASTER
  ↓
MARKET DATA / FEATURES
```

COTAHIST é uma série histórica de cotações EOD. Ela não substitui dados tick-by-tick, book, agressão ou fluxo institucional. A B3 disponibiliza produtos específicos para outros tipos de dados de mercado. citeturn0search1
