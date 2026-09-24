# B3 Data Observatory — V1

**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** `dashboards/`  
**Versão:** V1  
**Data de criação:** 24/09/2026

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
