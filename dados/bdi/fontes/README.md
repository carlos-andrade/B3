# Fontes BDI

**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Fontes oficiais do BDI  
**Caminho:** dados/bdi/fontes/README.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

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
