# Dados BDI — B3

| Campo | Valor |
|---|---|
| **ID** | B3-DADOS-BDI-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_TECNICO |
| **Fase** | Ingestão de dados BDI |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 101c7b67fee0eefa6723340df0b4620762bfbc68ff04cb2822d1e64c1e4fbab7 |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação técnica e aprovação humana |
| **Origem** | Captura BDI, manifestos de ingestão e workflows B3 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Centralizar a camada de dados diários do Boletim Diário do Mercado da B3 para estudos auditáveis de mercado, liquidez, volume, derivativos, empréstimos e demais informações publicadas no boletim.

A B3 informa que dados anteriormente disponibilizados em páginas públicas de cotações passaram a ser consultados no BDI desde 15/12/2025. A página de cotações informa especificamente que os dados foram migrados para os capítulos de Renda Variável > Resumo de Ações > Negócio a Negócio e Derivativos > Derivativos de Bolsa > Negócio a Negócio.

## Escopo

- preservar referência temporal do boletim;
- catalogar capítulos e tabelas relevantes;
- capturar CSV/PDF quando disponíveis;
- validar estrutura, registros, duplicidades e campos;
- separar dado observado de interpretação analítica;
- alimentar estudos de volume, liquidez, derivativos e microestrutura.

## Regra de integridade

Nenhum número agregado será tratado como dado oficial do projeto sem identificação de data, tabela/capítulo, fonte B3 e, quando houver arquivo baixado, hash SHA-256.

## Fontes

- BDI automatizado da B3;
- Pesquisa por pregão;
- layouts e arquivos oficiais B3;
- fontes complementares somente quando claramente identificadas.

## Captura automatizada

A captura do endpoint `DailyAverageStocks` está configurada no workflow [Testar captura BDI](../../.github/workflows/testar-captura-bdi.yml), com agenda em dias úteis às 11:00 UTC e execução manual. A opção `--date auto` procura a última data disponível até sete dias de calendário para trás, validando JSON, colunas e registos antes de gravar. A captura conserva o RAW e o SHA-256 no manifesto. Se o SHA-256 de uma data já registada divergir, o script interrompe a execução e exige reconciliação explícita; não sobrescreve silenciosamente. Após a captura, o workflow aciona a reavaliação WATCHDOG da atualidade dos dados.

A data consultada é a data de observação do BDI; `captured_at_utc` é apenas o instante de captura. Não são intercambiáveis.

## Estrutura prevista

- `fontes/` — documentação das fontes;
- `2026/` — dados organizados por ano;
- `logs/` — manifestos e validações;
- `scripts/` — automações específicas do BDI.
