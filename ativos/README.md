# Ativos negociados na B3

| Campo | Valor |
|---|---|
| **ID** | B3-ATIVOS-README-ROOT-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_CATALOGO_ATIVOS |
| **Fase** | Inventário e documentação de ativos |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | cd749e1a39fac6162ee5c259878e7bfb5dceb1354c658c19698b4484d77923d8 |
| **Commit de referência (versão anterior)** | [375495e43b8c39f8bd346dfe669ad065bc899a88](https://github.com/carlos-andrade/B3/commit/375495e43b8c39f8bd346dfe669ad065bc899a88) |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — README descritivo, sem aprovação normativa |
| **Origem** | Estrutura do catálogo de ativos B3 |
| **Autoridade superior** | [Layout Mestre Canónico B3](../docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma de cabeçalho GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Organização dos catálogos de instrumentos e ativos da B3 |
| **Objetivo** | Apresentar a estrutura dos catálogos de ativos e a fonte-base para inventário |
| **Dependências** | Cadastro de Instrumentos BVBG.028.02 e documentação oficial B3 aplicável |

## Objetivo

Esta árvore organiza os instrumentos negociáveis e seus cadastros por classe de mercado.

A fonte de referência para o inventário de instrumentos listados é o **Cadastro de Instrumentos BVBG.028.02**, divulgado pela B3. O cadastro é dinâmico: instrumentos podem ser incluídos, alterados ou retirados.

## Estrutura

- `acoes/`
- `bdrs/`
- `etfs/`
- `fiis/`
- `fundos/`
- `indices/`
- `futuros/`
- `opcoes/`
- `termo/`
- `renda_fixa/`
- `juros/`
- `moedas/`
- `commodities/`
- `criptoativos/`
- `balcao/`
- `cepac/`
- `emprestimo_ativos/`

**Regra:** todos os cadastros, estudos, dados históricos e automações sobre ativos da B3 devem permanecer dentro deste repositório.

## Regras de integridade

- Tratar o cadastro como dinâmico e preservar a data de referência dos inventários.
- Não presumir que um instrumento esteja ativo ou negociável sem evidência oficial datada.
- Preservar os contratos de dados e os processos de ingestão existentes; este README não os substitui.
