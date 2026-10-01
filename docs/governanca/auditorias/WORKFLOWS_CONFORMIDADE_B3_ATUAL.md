# Auditoria de Conformidade dos Workflows B3

Fonte normativa: docs/governanca/LAYOUT_MESTRE_CANONICO_B3_V1.md
Gerado em UTC: 2026-10-01T14:41:17.284482+00:00
Workflows auditados: 109
Conformes: 5
Divergentes: 104

## Regra de decisão

Este auditor é diagnóstico. Ele não corrige, reexecuta ou promove workflows.
Correções devem ocorrer no workflow em que a divergência existe.

## Critérios

- Layout Mestre presente.
- Gatilho declarado.
- Sem chamada/reexecução de outro workflow.
- Sem README como gatilho operacional.
- Sem docs/ genérico como gatilho operacional.
- GITHUB_STEP_SUMMARY presente.
- README somente no cron 23:55 America/Sao_Paulo (02:55 UTC).
- Monitor em modo somente leitura e sem reexecução.

## Matriz

| Workflow | Status | Divergências |
|---|---|---|
| .github/workflows/atualizar-catalogo-b3.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/atualizar-readme-b3.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/b3-auditoria-workflows-layout-mestre-v1.yml | **CONFORME** | — |
| .github/workflows/b3-monitor-execucoes-v1.yml | **CONFORME** | — |
| .github/workflows/bcb-sgs-nucleo-macro-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/capturar-bcb-copom.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/capturar-pesquisa-pregao.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/classificar-bvbg028.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-calendario-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-calendario-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-ohlc-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-ohlc-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-quantidade-volume-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-quantidade-volume-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-cadeia-1994-06-12-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-calendario-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-certificacao-anual-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-certificacao-final-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-chave-logica-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-chave-logica-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-chaves-logicas-1986-v2.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-classificacao-excecoes-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-dataset-oficial-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-dataset-oficial-v2.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-diagnostico-prazot-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-evidencias-retrospectivas-1993-fases06-08-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase00-governanca-1993-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase00-governanca-1994-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase01-aquisicao-raw-1993-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase01-aquisicao-raw-1994-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase02-evidencia-1993-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase02-integridade-1994-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase03-parsing-1994-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase03-parsing-1995-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase04-normalizacao-1994-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase04-normalizacao-1995-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase05-manifesto-checksum-1994-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase05-manifesto-checksum-1995-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase06-reconciliacao-1994-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase06-semantica-1995-v1.yml | **DIVERGENTE** | NO_README_TRIGGER, STEP_SUMMARY |
| .github/workflows/cotahist-fase07-identidade-historica-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase07b-tpmerc-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase07c-codbdi-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase07d-codisi-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase07e-dimes-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase07f-colisao-k4-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase07g-matriz-identidade-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08-semantica-k4-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08a-matriz-calendario-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08b-evidencia-calendario-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08c-duplicidades-k4-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08c-padrao-negociacao-arredores-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08c-padroes-ausencia-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08e-cronologia-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08f-estrutura-estatistica-k4-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08g-recorrencia-perfis-k4-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08h-recurrencia-k4-multianos-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08i-reconstrucao-regra-agregacao-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase08p-transicao-vigor-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase09-prerelease-1993-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase09b-multiplicidade-term-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1989-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1990-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1991-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1992-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1993-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase12-fechamento-transicao-1993-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-fase14-presenca-integridade-1995-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-gate-historico-1986.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-importacao-diaria-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-integridade-campos-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-integridade-campos-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-m2-certificacao-fisica-1987-v2.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-m3-0-gate-capacidade-2026.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-m3-1b-prova-lfs-2026.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-m3-1b-reconciliar-manifest-2026.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-m3-1c-ci-normalized-2026.yml | **CONFORME** | — |
| .github/workflows/cotahist-m3-1d-dataset-oficial-2026.yml | **CONFORME** | — |
| .github/workflows/cotahist-m3-1e-aprovacao-global.yml | **CONFORME** | — |
| .github/workflows/cotahist-materializar-normalized-1989-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-materializar-normalized-1990-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-materializar-normalized-1991-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-materializar-normalized-1992-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-materializar-normalized-1993-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-normalizacao-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-normalizacao-controlada-v7.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-normalized-m1-1987.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-ohlc-1986-v2.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-ohlc-excecoes-contexto-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-orquestrador-anual-dryrun-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-orquestrador-anual-dryrun-v2.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-prazot-anomalias-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-quantidade-volume-preco-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-final-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-raw-normalized-1986-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-semantica-1986.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-semantica-1987-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-semantica-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-validacao-independente-1988-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/cotahist-validacao-independente-1988-v2.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/indices-b3-composicao-v1.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/processar-inventario-bvbg028.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/sincronizar-wiki-b3.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/sincronizar-wiki.yml | **DIVERGENTE** | NO_README_TRIGGER, STEP_SUMMARY |
| .github/workflows/testar-captura-bdi.yml | **DIVERGENTE** | STEP_SUMMARY |
| .github/workflows/validar-bvbg02802.yml | **DIVERGENTE** | STEP_SUMMARY |
