# Dados BDI — B3

**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Boletim Diário do Mercado (BDI)  
**Caminho:** dados/bdi/README.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

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

## Estrutura prevista

- `fontes/` — documentação das fontes;
- `2026/` — dados organizados por ano;
- `logs/` — manifestos e validações;
- `scripts/` — automações específicas do BDI.
