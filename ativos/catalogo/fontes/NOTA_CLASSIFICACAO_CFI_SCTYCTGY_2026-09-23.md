# NOTA DE CLASSIFICAÇÃO — BVBG.028.02 / CFI / SctyCtgy

| Campo | Valor |
|---|---|
| **ID** | B3-CAT-FONTE-004 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | NOTA_TECNICA_DE_CLASSIFICACAO |
| **Fase** | CLASSIFICACAO_CADASTRAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 8e669eff062aae29e5579d8ab5de668a85732e96e56dbc8f7509c167840002f7 |
| **Commit de referência (versão anterior)** | [fd4b1ae4d4d9f5479a9d03e1f01f8ccc42da01be](https://github.com/carlos-andrade/B3/commit/fd4b1ae4d4d9f5479a9d03e1f01f8ccc42da01be) |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório |
| **Origem** | Documentação B3 sobre SctyCtgy e ISO 10962:2021 para a estrutura do CFI; tradução oficial requer lista B3 vigente |
| **Autoridade superior** | [Norma de cabeçalho documental da GOVERNANÇA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
