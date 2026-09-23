# ANÁLISE ESTRUTURAL DO INVENTÁRIO B3 — BVBG.028.02

**Arquivo:** ANALISE_ESTRUTURAL_BVBG028_2026-09-22.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Classificação quantitativa do inventário de instrumentos  
**Data de análise:** 2026-09-23  
**Fonte:** B3 Pesquisa por Pregão — BVBG.028.02  
**Snapshot:** 2026-09-22T18:39:18  
**Repositório:** carlos-andrade/B3

## 1. Evidência primária

O arquivo oficial capturado é `ativos/catalogo/raw/IN260922.zip`.

- Registros declarados: **120.973**
- Registros processados: **120.973**
- Validação de contagem: **TRUE**
- IDs de instrumentos duplicados: **0**
- Registros sem ticker: **750**
- Tamanho bruto: **20.151.525 bytes**
- SHA-256: `4e29690d9ce9e226bb61da80a167c11c50f828565431351eaf1f8fbbdcfe0a49`

## 2. Estrutura observada

A classificação não deve ser feita pelo ticker isoladamente. O inventário contém campos estruturais como `Asst`, `AsstDesc`, `SctyCtgy` e `CFICd`.

A documentação da B3 define `SctyCtgy` como Security Category e informa que sua codificação depende de uma lista externa (`ExternalSecurityCategoryCode`). Portanto, os códigos numéricos de `SctyCtgy` observados no snapshot não serão traduzidos por inferência.

O CFI é uma classificação internacional de instrumentos financeiros definida pela ISO 10962:2021. O código possui seis caracteres, com categoria, grupo e atributos.

## 3. Principais códigos CFI

| CFICd | Registros | % do inventário |
|---|---:|---:|
| OPESPS | 30.536 | 25,24% |
| OCASPS | 18.839 | 15,57% |
| OCESPS | 11.696 | 9,67% |
| EMXXXR | 4.989 | 4,12% |
| OPEMPS | 4.404 | 3,64% |
| OCAMPS | 2.660 | 2,20% |
| OCEICS | 2.203 | 1,82% |
| EPNNPR | 2.090 | 1,73% |
| OPEICS | 2.079 | 1,72% |
| ESVUFR | 2.076 | 1,72% |

Os quatro primeiros códigos, isoladamente, representam aproximadamente **54,6%** do inventário.

## 4. Principais ativos-base

| Asst | Registros |
|---|---:|
| IDI | 4.644 |
| PETR | 4.541 |
| DOL | 4.528 |
| BOVA | 3.539 |
| VALE | 3.415 |
| ITUB | 2.871 |
| BBDC | 2.507 |
| BBAS | 2.360 |
| EMBJ | 2.299 |
| WEGE | 2.227 |
| PRIO | 2.173 |
| BPAC | 1.987 |
| IBOV | 1.879 |
| BGI | 1.635 |
| B3SA | 1.446 |

**Observação:** esses números são quantidade de registros de instrumentos associados ao ativo-base, não volume financeiro, número de negócios ou liquidez.

## 5. Categoria de instrumento

O campo `SctyCtgy` apresenta forte concentração:

| SctyCtgy | Registros | % |
|---|---:|---:|
| 7 | 69.879 | 57,76% |
| 17 | 20.861 | 17,24% |
| 25 | 5.602 | 4,63% |
| 1 | 2.356 | 1,95% |
| 11 | 2.308 | 1,91% |
| 8 | 1.836 | 1,52% |
| 26 | 1.724 | 1,43% |
| 6 | 1.479 | 1,22% |
| 2 | 846 | 0,70% |
| 108 | 732 | 0,61% |

**Importante:** os códigos numéricos de `SctyCtgy` ainda não serão convertidos em nomes sem uma tabela oficial de correspondência. Isso evita classificação por inferência.

## 6. Interpretação técnica

### Fato

O catálogo de 22/09/2026 possui **120.973 registros válidos**, com correspondência integral entre a quantidade declarada no snapshot e a quantidade efetivamente processada.

### Fato

A dimensão CFI demonstra que uma parcela muito relevante do catálogo é composta por instrumentos derivados, especialmente famílias de opções e contratos relacionados.

### Hipótese controlada

A elevada concentração de códigos CFI iniciados por `O` é compatível com forte presença de instrumentos de opção no universo cadastral.

### Inferência ainda não autorizada

Não devemos concluir, apenas a partir do cadastro, quais instrumentos são mais líquidos ou mais relevantes para trading. Para isso será necessário cruzar o cadastro com **BDI, negócios, volume financeiro, preço, contratos em aberto e dados intraday**.

## 7. Próxima etapa do pipeline

A próxima camada será o cruzamento:

**Cadastro BVBG.028.02 → classificação oficial → BDI → PriceReport → volume/negócios → microestrutura.**

Isso permitirá separar:

1. universo cadastral;
2. instrumentos efetivamente negociados;
3. instrumentos com volume;
4. instrumentos com liquidez recorrente;
5. instrumentos adequados para estudos quantitativos;
6. instrumentos adequados para estratégias intraday;
7. instrumentos adequados para análise de fluxo.

## 8. Regra metodológica

Nenhum instrumento será classificado como ação, ETF, FII, BDR, futuro, opção, índice, moeda, juros ou commodity exclusivamente pelo ticker.

A classificação final deverá utilizar, em ordem de prioridade:

1. campos oficiais do BVBG.028.02;
2. CFI;
3. categoria oficial B3;
4. descrição oficial;
5. mercado/segmento oficial;
6. apenas como validação auxiliar, ticker e ativo-base.

## 9. Fonte normativa e controle de classificação

A B3 documenta `SctyCtgy` como Security Category e informa que a correspondência dos códigos é mantida em uma lista externa denominada `ExternalSecurityCategoryCode`. A tradução dos códigos numéricos somente será considerada oficial após a captura dessa lista.

A ISO 10962:2021 permanece como referência internacional para a estrutura do CFI Code. A ISO descreve o CFI como código de seis caracteres formado por categoria, grupo e atributos.

Fonte B3: catálogo de taxonomia UP2DATA / documentação do cadastro de instrumentos.

Fonte ISO: ISO 10962:2021.

## 10. Status

**CATÁLOGO BVBG.028.02: VALIDADO**

**CLASSIFICAÇÃO ESTRUTURAL: EM ANDAMENTO**

**LIQUIDEZ/MICROESTRUTURA: PRÓXIMA ETAPA**
