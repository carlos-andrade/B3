# B3 Data Observatory — V1

| Campo | Valor |
|---|---|
| **ID** | B3-DASH-README-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | README_TECNICO |
| **Fase** | Visualização e observabilidade |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a92315a5976227df491360e47e52c783531d32429fb34c69032afb822aa5d78d |
| **Commit de referência (versão anterior)** | N/A — primeira normalização do cabeçalho |
| **Data de criação** | 2026-09-24 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação funcional e aprovação humana |
| **Origem** | Estrutura `dashboards/` e contrato de `data/dashboard.json` |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Disponibilizar uma camada de visualização somente leitura para os resultados do pipeline de ingestão, normalização e validação histórica da B3.

## Arquitetura

`pipeline → data/dashboard.json → dashboards/index.html`

O HTML não contém observações de mercado embutidas. O snapshot JSON é a única fonte dos indicadores exibidos.

## Contrato inicial

- `kpis`: indicadores consolidados;
- `years`: anos efetivamente publicados;
- `runs`: execuções do pipeline;
- `checks`: validações;
- `by_year`: resultados anuais;
- `provenance`: origem e classificação do snapshot.

**Regra:** ausência de dado permanece ausência de dado; não converter `null` em zero.

## Estado da V1

A interface está pronta e foi criada sem inventar resultados. A alimentação com dados reais deve ser feita pelo pipeline de ingestão/normalização/validação.
