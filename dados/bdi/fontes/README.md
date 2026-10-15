# Fontes BDI

| Campo | Valor |
|---|---|
| **ID** | B3-DADOS-BDI-FONTES-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_FONTES |
| **Fase** | Ingestão BDI — mapeamento de fontes |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 8a5a37117af561954be29483d4ae3742c80ac4ad2c6744e8baf63b1e39ef7988 |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação das fontes e aprovação humana |
| **Origem** | Mapeamento de fontes BDI e documentação pública da B3 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Fonte primária

O BDI é a publicação diária da B3 que consolida informações das negociações realizadas no ambiente da Bolsa. A B3 informa que o boletim pode ser consultado por capítulos e que, após a publicação integral, as tabelas podem ser baixadas em CSV e PDF.

## Mapeamento inicial

| Necessidade | Fonte BDI a investigar |
|---|---|
| Ações / volume | Renda variável > Resumo de ações |
| Negócio a negócio | Renda variável > Resumo de ações > Negócio a Negócio |
| Derivativos | Derivativos > Derivativos de bolsa |
| Derivativos negócio a negócio | Derivativos > Derivativos de bolsa > Negócio a negócio |
| Empréstimo de ativos | Clearing > mercado de empréstimo |
| Posições em aberto | Clearing / derivativos, conforme tabela publicada |
| Indicadores | Indicadores e Informativos |

## Observação

Este arquivo registra o mapa de pesquisa, não uma afirmação de que todos os campos necessários para microestrutura estejam disponíveis no BDI. A existência de uma tabela deve ser confirmada na captura correspondente.

## Critério analítico

BDI é tratado como fonte diária consolidada. Para agressão, Cumulative Delta, VWAP/TWAP intradiário e microestrutura tick a tick, serão necessárias fontes de negócios/market data compatíveis com o nível de granularidade requerido.
