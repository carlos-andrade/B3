# NOTA DE CLASSIFICAÇÃO — BVBG.028.02 / CFI / SctyCtgy

**Arquivo:** NOTA_CLASSIFICACAO_CFI_SCTYCTGY_2026-09-23.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Validação de classificação de instrumentos  
**Data:** 2026-09-23  
**Fonte primária:** B3 / ISO  
**Repositório:** carlos-andrade/B3

## 1. Evidência B3

A documentação oficial da B3 para o cadastro de instrumentos define `SctyCtgy` como **Security Category** e informa que esse campo utiliza uma lista externa de códigos: `ExternalSecurityCategoryCode`, mantida em arquivo de listas externas da B3.

Portanto, os códigos numéricos observados no inventário de 22/09/2026 **não devem ser traduzidos por inferência**. A correspondência oficial precisa ser obtida da lista externa da B3.

## 2. Evidência ISO — CFI

A ISO 10962:2021 define a estrutura internacional do CFI Code. O código possui seis caracteres: uma categoria, um grupo e atributos adicionais. A ISO apresenta, por exemplo, `ESVUFR` como código de ações ordinárias com voto, sem restrição, integralizadas e registradas.

Fonte: ISO 10962:2021.

## 3. Aplicação ao inventário B3

No snapshot BVBG.028.02 de 22/09/2026 foram processados 120.973 registros.

Os códigos CFI devem ser utilizados como camada de classificação estrutural, mas não substituem a classificação oficial B3 de `SctyCtgy`.

### Regra

**Classificação oficial = campos B3 + lista externa B3 + CFI ISO.**

Ticker e ativo-base são apenas campos auxiliares.

## 4. Estado da validação

- BVBG.028.02: **VALIDADO**
- `SctyCtgy`: **MAPEADO ESTRUTURALMENTE, MAS SEM TRADUÇÃO NUMÉRICA SEM A LISTA EXTERNA**
- CFI: **VALIDADO COMO PADRÃO INTERNACIONAL**
- Classificação econômica final: **EM ANDAMENTO**

## 5. Próximo passo

Capturar a lista externa `ExternalSecurityCategoryCode` da B3, preservá-la como fonte, calcular a correspondência dos códigos `SctyCtgy` observados e gerar uma classificação normalizada auditável.

