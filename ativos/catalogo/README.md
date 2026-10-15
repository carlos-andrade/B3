# Catálogo de Instrumentos B3

| Campo | Valor |
|---|---|
| **ID** | B3-ATIVOS-CATALOGO-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_TECNICO |
| **Fase** | Catálogo de instrumentos |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 8989dec8ba24e619f5fc242c9bf8aa056dc11ad6423c5b0cea83c1bee1ea27d5 |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | 2026-09-23 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação dos dados e aprovação humana |
| **Origem** | Catálogo B3 e pipeline de captura de instrumentos |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Esta pasta é o núcleo do inventário efetivo dos instrumentos da B3. O catálogo deve ser reconstruído a partir do cadastro oficial, evitando listas manuais e tickers inventados.

## Fonte oficial

A B3 disponibiliza diariamente o **Cadastro de Instrumentos (Listado)** e informa que o arquivo BVBG.028.02 identifica os instrumentos do mercado listado. A B3 também disponibiliza o cadastro por meio dos Dados Públicos.

## Estrutura planejada

- `INVENTARIO_B3_YYYY-MM-DD.csv` — inventário bruto/consolidado da data de referência.
- `INVENTARIO_B3_YYYY-MM-DD.md` — resumo auditável da captura.
- `instrumentos/` — diretórios individuais dos instrumentos, quando a materialização por ativo for executada.
- `fontes/` — documentação, layouts e metadados das fontes.
- `logs/` — registros de execução, contagens, erros e validações.

## Regra de integridade

O inventário é **data-dependent**. Um instrumento presente em uma data não deve ser tratado automaticamente como ativo negociável em outra data. Toda fotografia do catálogo deve registrar a data de captura.

## Campos mínimos desejados

`TckrSymb`, identificação/ISIN, descrição, categoria, segmento, mercado, empresa/emissor, vencimento quando aplicável, ativo-objeto quando aplicável e demais campos fornecidos pelo cadastro oficial.

## Status

**Etapa atual:** estrutura e pipeline preparados; a materialização dos instrumentos deve usar o arquivo oficial da data de referência, sem completar dados por inferência.
