# Fonte B3 — Atualização do protocolo de dados

| Campo | Valor |
|---|---|
| **ID** | B3-CAT-FONTE-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | NOTA_DE_FONTE |
| **Fase** | GOVERNANCA_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 17ab61786162769b08350ef116509a9555b32499981bd44e7b67a3e7151e47fd |
| **Commit de referência (versão anterior)** | [917257e8c85eb519d88116976c60db68aa118506](https://github.com/carlos-andrade/B3/commit/917257e8c85eb519d88116976c60db68aa118506) |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório |
| **Origem** | Referências públicas da B3 descritas abaixo; rever periodicamente a atualidade das páginas |
| **Autoridade superior** | [Norma de cabeçalho documental da GOVERNANÇA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
