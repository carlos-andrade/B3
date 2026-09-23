# Catálogo de Instrumentos B3

**Projeto:** B3 - A Bolsa do Brasil  
**Repositório:** `carlos-andrade/B3`  
**Data de criação:** 23/09/2026  
**Fonte primária:** B3 — Cadastro de Instrumentos (Listado), BVBG.028.02 / InstrumentsConsolidated

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
