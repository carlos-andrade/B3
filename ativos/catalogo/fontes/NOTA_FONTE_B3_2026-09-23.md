# Fonte B3 — Atualização do protocolo de dados

**Projeto:** B3 - A Bolsa do Brasil  
**Data:** 23/09/2026  
**Fonte:** B3 / arquivos.b3.com.br

## Verificação

Em 23/09/2026 foi verificado que a infraestrutura pública da B3 informa a desativação das antigas páginas de “Dados públicos de produtos listados e de balcão” e “Cotações” a partir de 31/03/2026. A B3 informa que os dados anteriormente publicados nessas páginas passaram a ser disponibilizados no **Boletim Diário do Mercado (BDI)** desde 15/12/2025.

A página atual do cadastro de instrumentos permanece disponível na infraestrutura `arquivos.b3.com.br`, mas sua interface é dinâmica e não expõe o conteúdo tabular completo ao coletor de texto.

## Consequência para o projeto

O BVBG.028.02 continua sendo tratado como fonte de cadastro de instrumentos. Porém, a rotina de captura não deve assumir que a antiga interface de dados públicos seja a única via de distribuição.

A partir desta versão, o projeto separa:

- **Cadastro:** identificação e características dos instrumentos;
- **BDI:** dados publicados diariamente no Boletim Diário do Mercado;
- **Dados históricos/mercado:** fontes específicas para preços, negócios, volume e demais séries.

## Regra

Nenhum inventário quantitativo será declarado como capturado até que o arquivo bruto correspondente esteja efetivamente disponível e seu conteúdo seja validado.

## Referência pública verificada

A B3 informa explicitamente a migração dos dados para o BDI e mantém o calendário/boletim na infraestrutura pública.

**Status:** fonte e arquitetura validadas; captura integral do BVBG.028.02 ainda pendente de acesso ao arquivo bruto.
