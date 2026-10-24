# Auditoria de Conformidade dos Workflows B3 — v2

| Campo | Valor |
|---|---|
| **ID** | B3-AUD-WORKFLOWS-CURRENT |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | GOVERNANCA_CONTINUA |
| **Estado** | EM_REVISAO |
| **Versão** | 2.0.0 |
| **SHA-256 (conteúdo canónico)** | 056b1aa571e3d9924e0d72149dbe56e3e485e8f69ed3102edf45f8ea419f3e68 |
| **Commit de referência (versão anterior)** | [1e7c0dc6d4c18856d2ff1a68e8cb3cdbb35671b0](https://github.com/carlos-andrade/B3/commit/1e7c0dc6d4c18856d2ff1a68e8cb3cdbb35671b0) |
| **Data de criação** | N/A — relatório regenerado automaticamente |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Automação de auditoria de governança B3 |
| **Aprovador** | Pendente — relatório diagnóstico, não constitui aprovação normativa |
| **Origem** | Gerado por scripts/governanca/auditar_workflows_b3.py |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


Fonte normativa: docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md
Gerado em UTC: 2026-10-24T00:57:31.984329+00:00
Workflows auditados: 561

## Regra de decisão

A v2 separa divergência funcional de observabilidade. Não corrige, reexecuta ou promove workflows.
Falhas CRITICA/ALTA são bloqueadoras; MEDIA/BAIXA são alertas para revisão.
Ausência isolada de GITHUB_STEP_SUMMARY não é defeito funcional de dados.

## Critérios ampliados

- Layout Mestre presente.
- Trigger declarado e causal.
- Sem chamada/reexecução de outro workflow.
- Sem README/docs genérico como trigger operacional.
- Sem trigger explícito de fase posterior.
- Dependência direcional identificável.
- Permissões compatíveis com escrita real.
- Persistência de evidência identificável.
- Sinal explícito de status/decisão.
- Sinal de idempotência/deduplicação quando aplicável.
- README exclusivamente na janela 23:55 America/Sao_Paulo.
- Monitor somente leitura e sem reexecução.

## Matriz

| Workflow | Fase | Status | Bloqueadores | Alertas |
|---|---:|---|---|---|
| .github/workflows/atualizar-catalogo-b3.yml | — | **CONFORME** | — | — |
| .github/workflows/atualizar-readme-b3.yml | — | **CONFORME** | — | — |
| .github/workflows/b3-auditoria-autorizacao-endpoints.yml | — | **CONFORME** | — | — |
| .github/workflows/b3-auditoria-sha256-documental.yml | — | **CONFORME** | — | — |
| .github/workflows/b3-auditoria-workflows-layout-mestre-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/b3-cotahist-rebase-conflict-hardening.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/b3-cvm-dados-abertos.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/b3-fontes-gratuitas-orquestrador.yml | — | **CONFORME** | — | — |
| .github/workflows/b3-monitor-execucoes-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/b3-normalizar-cabecalhos-invalidos.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/b3-ptax-bcb.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/bcb-sgs-nucleo-macro-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/capturar-bcb-copom.yml | — | **CONFORME** | — | — |
| .github/workflows/capturar-pesquisa-pregao.yml | — | **CONFORME_COM_OBSERVACAO** | — | IDEMPOTENCE_SIGNAL |
| .github/workflows/classificar-bvbg028.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-auditoria-calendario-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-calendario-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-fisica-normalized-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-auditoria-ohlc-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-ohlc-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-quantidade-volume-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-auditoria-quantidade-volume-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-cadeia-1994-06-12-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-calendario-1986-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-calendario-oficial-2026-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-certificacao-anual-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY, IDEMPOTENCE_SIGNAL |
| .github/workflows/cotahist-certificacao-final-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-chave-logica-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-chave-logica-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-chaves-logicas-1986-v2.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-classificacao-excecoes-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-dataset-oficial-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY, IDEMPOTENCE_SIGNAL |
| .github/workflows/cotahist-dataset-oficial-v2.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY, IDEMPOTENCE_SIGNAL |
| .github/workflows/cotahist-diagnostico-prazot-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-evidencias-retrospectivas-1993-fases06-08-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase00-governanca-1993-v1.yml | 0 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase00-governanca-1994-v1.yml | 0 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY, IDEMPOTENCE_SIGNAL |
| .github/workflows/cotahist-fase00-governanca-2002-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2003-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2004-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2005-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2006-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2007-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2008-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2009-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2010-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2011-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2012-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2013-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2014-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2015-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2016-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2017-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2018-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2019-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2020-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2021-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase00-governanca-2022-v1.yml | 0 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2000-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2001-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2002-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2003-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2004-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2005-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2006-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2007-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2008-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2009-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2010-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2011-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2012-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2013-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2014-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2015-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2016-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2017-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2018-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2019-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2020-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2021-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-2022-v1.yml | 1 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase01-aquisicao-raw-1993-v1.yml | 1 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase01-aquisicao-raw-1994-v1.yml | 1 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase02-evidencia-1993-v1.yml | 2 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase02-integridade-1994-v1.yml | 2 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase02-integridade-1999-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2000-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2001-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2002-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2003-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2004-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2005-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2006-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2007-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2008-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2009-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2010-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2011-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2012-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2013-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2014-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2015-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2016-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2017-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2018-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2019-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2020-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2021-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase02-integridade-2022-v1.yml | 2 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-1994-v1.yml | 3 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase03-parsing-1995-v1.yml | 3 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase03-parsing-1996-v1.yml | 3 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase03-parsing-1997-v1.yml | 3 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase03-parsing-1998-v1.yml | 3 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase03-parsing-1999-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2000-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2001-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2002-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2003-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2004-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2005-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2006-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2007-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2008-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2009-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2010-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2011-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2012-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2013-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2014-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2015-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2016-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2017-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2018-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2019-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2020-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2021-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase03-parsing-2022-v1.yml | 3 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-1994-v1.yml | 4 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase04-normalizacao-1995-v1.yml | 4 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase04-normalizacao-1996-v1.yml | 4 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase04-normalizacao-1997-v1.yml | 4 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase04-normalizacao-1998-v1.yml | 4 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase04-normalizacao-2015-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2016-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2017-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2018-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2019-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2020-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2020-v2.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2021-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2022-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2023-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2024-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2025-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-normalizacao-2026-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2000-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2001-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2002-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2003-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2004-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2005-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2006-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2007-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2008-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2009-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2010-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2011-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2012-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2013-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-recuperar-normalized-2014-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-1999-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2000-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2001-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2002-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2003-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2004-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2005-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2006-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2007-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2008-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2009-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2010-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2011-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2012-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2013-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase04-validacao-independente-2014-v1.yml | 4 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-1994-v1.yml | 5 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase05-manifesto-checksum-1995-v1.yml | 5 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase05-manifesto-checksum-1996-v1.yml | 5 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase05-manifesto-checksum-1997-v1.yml | 5 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase05-manifesto-checksum-1998-v1.yml | 5 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase05-manifesto-checksum-1999-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2000-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2001-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2002-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2003-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2004-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2005-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2006-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2007-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2008-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2009-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2010-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2011-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2012-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2013-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2014-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2015-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2016-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2017-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2018-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2019-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2020-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2021-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2022-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2023-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2024-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase05-manifesto-checksum-2025-v1.yml | 5 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-1994-v1.yml | 6 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase06-reconciliacao-1999-v1.yml | 6 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase06-reconciliacao-2000-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2001-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2002-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2003-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2004-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2005-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2006-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2007-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2008-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2009-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2010-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2011-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2012-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2013-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2014-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2015-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2016-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2017-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2018-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2019-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2020-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2021-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2022-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2023-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2024-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2025-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-2026-v1.yml | 6 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase06-reconciliacao-ohlc-1998-v1.yml | 6 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase06-semantica-1995-v1.yml | 6 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase06-semantica-1996-v1.yml | 6 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase06-semantica-1997-v1.yml | 6 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase06-semantica-1998-v1.yml | 6 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase06b-contexto-term-1998-v1.yml | 6 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07-identidade-1999-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2000-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2001-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2002-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2003-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2004-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2005-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2006-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2007-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2008-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2009-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2010-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2011-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2012-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2013-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2014-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2015-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2016-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2017-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2018-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2019-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2020-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2021-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2022-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2022-v2.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2023-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2024-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2025-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-2026-v1.yml | 7 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase07-identidade-historica-1986-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07-identidade-historica-1995-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07-identidade-historica-1996-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07-identidade-historica-1997-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07-identidade-historica-1998-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07a-colisoes-identidade-1998-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07b-semantica-prazot-1998-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07b-tpmerc-1986-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07c-codbdi-1986-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07c-validacao-chave-prazot-1997-1999-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07d-codisi-1986-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07e-dimes-1986-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07f-colisao-k4-1986-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase07g-matriz-identidade-1986-v1.yml | 7 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08-calendario-1999-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2000-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2001-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2002-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2003-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2004-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2005-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2006-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2007-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2008-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2009-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2010-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2011-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2012-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2013-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2014-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2015-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2016-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2017-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2018-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2019-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2020-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2021-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2021-v2.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2022-v2.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2023-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2024-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2025-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-calendario-2026-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-consistencia-1998-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08-diagnostico-ordem-2021-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08-semantica-k4-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08-semantica-k4-1995-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08-semantica-k4-1996-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08-semantica-k4-1997-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08a-matriz-calendario-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08b-evidencia-calendario-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08c-duplicidades-k4-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08c-padrao-negociacao-arredores-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08c-padroes-ausencia-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08e-cronologia-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08f-estrutura-estatistica-k4-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08g-recorrencia-perfis-k4-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08h-recurrencia-k4-multianos-v1.yml | 8 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase08i-reconstrucao-regra-agregacao-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase08p-transicao-vigor-1986-v1.yml | 8 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase09-prerelease-1993-v1.yml | 9 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase09-prerelease-1995-v1.yml | 9 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase09-prerelease-1996-v1.yml | 9 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase09-prerelease-1997-v1.yml | 9 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase09-prerelease-1999-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2000-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2001-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2002-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2003-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2004-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2005-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2006-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2007-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2008-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2009-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2010-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2011-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2012-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2013-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2014-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2015-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2016-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2017-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2018-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2019-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2020-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2021-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2022-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2023-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2024-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2025-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09-prerelease-2026-v1.yml | 9 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase09b-multiplicidade-term-1986-v1.yml | 9 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1988-v1.yml | 10 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1989-v1.yml | 10 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1990-v1.yml | 10 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1991-v1.yml | 10 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1992-v1.yml | 10 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1993-v1.yml | 10 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase10-integridade-1995-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-integridade-1996-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-integridade-1997-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-1999-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2000-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2001-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2002-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2003-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2004-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2005-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2006-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2007-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2008-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2009-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2010-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2011-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2012-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2013-retry-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2013-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2014-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2015-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2016-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2017-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2018-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2019-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2020-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2021-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2022-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2023-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2024-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validacao-independente-2025-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase10-validar-candidato-2026-v1.yml | 10 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-1995-v1.yml | 11 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase11-certificacao-1996-v1.yml | 11 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase11-certificacao-1997-v1.yml | 11 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase11-certificacao-1999-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2000-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2001-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2002-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2003-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2004-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2005-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2006-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2007-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2008-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2009-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2010-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2011-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2012-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2013-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2014-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2015-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2016-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2017-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2018-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2019-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2020-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2021-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2022-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2023-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2024-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-certificacao-2025-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase11-promocao-controlada-2026-v1.yml | 11 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-1995-abertura-1996-v1.yml | 12 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase12-fechamento-1996-abertura-1997-v1.yml | 12 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase12-fechamento-1997-abertura-1998-v1.yml | 12 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase12-fechamento-1999-abertura-2000-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2000-abertura-2001-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2001-abertura-2002-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2002-abertura-2003-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2003-abertura-2004-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2004-abertura-2005-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2005-abertura-2006-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2006-abertura-2007-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2007-abertura-2008-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2008-abertura-2009-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2009-abertura-2010-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2010-abertura-2011-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2011-abertura-2012-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2012-abertura-2013-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2013-abertura-2014-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2014-abertura-2015-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2015-abertura-2016-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2016-abertura-2017-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2017-abertura-2018-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2018-abertura-2019-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2019-abertura-2020-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2020-abertura-2021-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2021-abertura-2022-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2022-abertura-2023-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2023-abertura-2024-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2024-abertura-2025-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-2025-abertura-2026-v1.yml | 12 | **CONFORME** | — | — |
| .github/workflows/cotahist-fase12-fechamento-transicao-1993-v1.yml | 12 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase13-materializacao-1996-v1.yml | 13 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase13-materializacao-1997-v1.yml | 13 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase13-materializacao-1998-v1.yml | 13 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase14-presenca-integridade-1995-v1.yml | 14 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase14-presenca-integridade-1996-v1.yml | 14 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase14-presenca-integridade-1997-v1.yml | 14 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-fase14-presenca-integridade-1998-v1.yml | 14 | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-1999-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2000-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2001-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2002-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2003-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2004-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2005-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2006-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2007-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2008-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2009-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2010-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2011-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2012-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2013-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-gate-06-08-2014-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2015-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2016-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2017-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2018-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2019-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2020-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2021-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2022-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2023-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2024-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2025-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-06-08-2026-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-gate-historico-1986.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-importacao-diaria-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-integridade-campos-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-integridade-campos-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-lfs-migracao-controlada-a1987-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-m2-certificacao-fisica-1987-v2.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-m3-0-gate-capacidade-2026.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-m3-1b-prova-lfs-2026.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-m3-1b-reconciliar-manifest-2026.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-m3-1c-ci-normalized-2026.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-m3-1d-dataset-oficial-2026.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-m3-1e-aprovacao-global.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-main-publisher.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-materializar-normalized-1989-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-materializar-normalized-1990-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-materializar-normalized-1991-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-materializar-normalized-1992-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-materializar-normalized-1993-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-normalizacao-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-normalizacao-controlada-v7.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-normalized-m1-1987.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-ohlc-1986-v2.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-ohlc-excecoes-contexto-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-orquestrador-anual-dryrun-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-orquestrador-anual-dryrun-v2.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-prazot-anomalias-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-quantidade-volume-preco-1986-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-final-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-raw-normalized-1986-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-semantica-1986.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-reconciliacao-tpmerc021-bvbg028-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-recuperar-normalized-1999-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-refresh-probe-2026-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-scheduler-probe-a.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-scheduler-probe-b.yml | — | **CONFORME** | — | — |
| .github/workflows/cotahist-semantica-1987-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-semantica-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-validacao-independente-1988-v1.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-validacao-independente-1988-v2.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/cotahist-validation-tests.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY, IDEMPOTENCE_SIGNAL |
| .github/workflows/indices-b3-composicao-v1.yml | — | **CONFORME** | — | — |
| .github/workflows/processar-inventario-bvbg028.yml | — | **CONFORME** | — | — |
| .github/workflows/rec001-cotahist-bloomberg-mail.yml | — | **CONFORME** | — | — |
| .github/workflows/sincronizar-wiki-b3.yml | — | **CONFORME** | — | — |
| .github/workflows/testar-captura-bdi.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY |
| .github/workflows/validar-bvbg02802.yml | — | **CONFORME** | — | — |
| .github/workflows/watchdog-b3-validation.yml | — | **CONFORME_COM_OBSERVACAO** | — | STEP_SUMMARY, IDEMPOTENCE_SIGNAL |
| .github/workflows/watchdog-data-freshness.yml | — | **CONFORME** | — | — |

## Inventário estático de escritores COTAHIST

- Workflows COTAHIST/referenciados: **541**
- Escritores efetivos do repositório (push/API): **527**
- Commits locais sem push detetado: **0**
- Permissão de escrita sem comando de publicação detetado: **1**
- Read-only/artefactos: **13**
- Classificação baseada em análise estática; confirmar dinamicamente antes de alterar políticas de execução.

| Workflow | Classe | Branch destino | Grupo de concorrência | Paths de escrita detetados |
|---|---|---|---|---|
| .github/workflows/b3-cotahist-rebase-conflict-hardening.yml | REPO_WRITER | main | b3-cotahist-rebase-conflict-hardening | .github/workflows/cotahist-*.yml, .github/workflows/rec001-cotahist-bloomberg-mail.yml |
| .github/workflows/cotahist-auditoria-calendario-1987-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1987_AUDITORIA_CALENDARIO_V1.json |
| .github/workflows/cotahist-auditoria-calendario-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_AUDITORIA_CALENDARIO_V1.json |
| .github/workflows/cotahist-auditoria-fisica-normalized-v1.yml | REPO_WRITER | main | cotahist-auditoria-fisica-normalized-v1 | dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json |
| .github/workflows/cotahist-auditoria-ohlc-1987-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1987_AUDITORIA_OHLC_V1.json |
| .github/workflows/cotahist-auditoria-ohlc-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_AUDITORIA_OHLC_V1.json |
| .github/workflows/cotahist-auditoria-quantidade-volume-1987-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1987_AUDITORIA_QUANTIDADE_VOLUME_V1.json |
| .github/workflows/cotahist-auditoria-quantidade-volume-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_AUDITORIA_QUANTIDADE_VOLUME_V1.json |
| .github/workflows/cotahist-cadeia-1994-06-12-v1.yml | REPO_WRITER | main | cotahist-cadeia-1994-06-12 | DYNAMIC:$f |
| .github/workflows/cotahist-calendario-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_AUDITORIA_CALENDARIO_V1.json |
| .github/workflows/cotahist-calendario-oficial-2026-v1.yml | REPO_WRITER | main | cotahist-calendario-oficial-2026-v1 | DYNAMIC:$evidence |
| .github/workflows/cotahist-certificacao-final-1987-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1987_CERTIFICACAO_FINAL_V1.json |
| .github/workflows/cotahist-chave-logica-1987-v1.yml | REPO_WRITER | main | cotahist-1987-chave-logica | dados/cotahist/quality/COTAHIST_1987_AUDITORIA_CHAVE_LOGICA_V1.json |
| .github/workflows/cotahist-chave-logica-1988-v1.yml | REPO_WRITER | main | cotahist-1988-chave-logica | dados/cotahist/quality/COTAHIST_1988_AUDITORIA_CHAVE_LOGICA_V1.json |
| .github/workflows/cotahist-chaves-logicas-1986-v2.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_AUDITORIA_CHAVES_V2.json |
| .github/workflows/cotahist-classificacao-excecoes-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_CLASSIFICACAO_FINAL_EXCECOES_V1.json |
| .github/workflows/cotahist-diagnostico-prazot-1987-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1987_DIAGNOSTICO_PRAZOT_V1.json |
| .github/workflows/cotahist-evidencias-retrospectivas-1993-fases06-08-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1993_FASE06_RECONCILIACAO_V1.json, dados/cotahist/quality/COTAHIST_1993_FASE07_IDENTIDADE_CHAVES_V1.json, dados/cotahist/quality/COTAHIST_1993_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase00-governanca-1993-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1993_FASE00_GOVERNANCA_PRE_CONDICOES_V1.json |
| .github/workflows/cotahist-fase00-governanca-2002-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2003-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2004-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2005-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2006-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2007-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2008-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2009-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2010-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2011-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2012-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2013-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2014-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2015-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2016-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2017-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2018-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2019-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2020-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2021-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase00-governanca-2022-v1.yml | REPO_WRITER | main | cotahist-fase00-governanca-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE00_GOVERNANCA_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2000-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2001-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2002-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2003-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2004-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2005-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2006-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2007-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2008-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2009-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2010-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2011-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2012-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2013-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2014-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2015-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2016-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2017-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2018-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2019-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2020-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2021-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-2022-v1.yml | REPO_WRITER | main | cotahist-fase01-aquisicao-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-raw-1993-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1993_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase01-aquisicao-raw-1994-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1994_FASE01_AQUISICAO_RAW_V1.json |
| .github/workflows/cotahist-fase02-evidencia-1993-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1993_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-1994-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1994_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-1999-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2000-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2001-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2002-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2003-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2004-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2005-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2006-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2007-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2008-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2009-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2010-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2011-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2012-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2013-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2014-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2015-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2016-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2017-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2018-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2019-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2020-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2021-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase02-integridade-2022-v1.yml | REPO_WRITER | main | cotahist-fase02-integridade-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE02_INTEGRIDADE_FONTE_V1.json |
| .github/workflows/cotahist-fase03-parsing-1994-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1994_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-1995-v1.yml | REPO_WRITER | main | cotahist-fase03-1995 | dados/cotahist/quality/COTAHIST_1995_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-1996-v1.yml | REPO_WRITER | main | cotahist-fase03-1996 | dados/cotahist/quality/COTAHIST_1996_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-1997-v1.yml | REPO_WRITER | main | cotahist-fase03-1997 | dados/cotahist/quality/COTAHIST_1997_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-1998-v1.yml | REPO_WRITER | main | cotahist-fase03-1998 | dados/cotahist/quality/COTAHIST_1998_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-1999-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2000-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2001-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2002-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2003-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2004-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2005-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2006-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2007-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2008-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2009-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2010-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2011-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2012-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2013-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2014-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2015-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2016-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2017-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2018-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2019-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2020-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2021-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase03-parsing-2022-v1.yml | REPO_WRITER | main | cotahist-fase03-parsing-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE03_PARSING_V1.json |
| .github/workflows/cotahist-fase04-normalizacao-1994-v1.yml | REPO_WRITER | main | cotahist-materializar-normalized-1994-v2 | dados/cotahist/normalized/anual/COTAHIST_A1994.csv, dados/cotahist/quality/COTAHIST_1994_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-normalizacao-1995-v1.yml | REPO_WRITER | main | cotahist-fase04-1995 | dados/cotahist/normalized/anual/COTAHIST_A1995.csv, dados/cotahist/quality/COTAHIST_1995_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-normalizacao-1996-v1.yml | REPO_WRITER | main | cotahist-fase04-1996 | dados/cotahist/normalized/anual/COTAHIST_A1996.csv, dados/cotahist/quality/COTAHIST_1996_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-normalizacao-1997-v1.yml | REPO_WRITER | main | cotahist-fase04-1997 | dados/cotahist/normalized/anual/COTAHIST_A1997.csv, dados/cotahist/quality/COTAHIST_1997_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-normalizacao-1998-v1.yml | REPO_WRITER | main | cotahist-fase04-1998 | dados/cotahist/normalized/anual/COTAHIST_A1998.csv, dados/cotahist/quality/COTAHIST_1998_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-normalizacao-2015-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2015-v1 | DYNAMIC:$evidence, DYNAMIC:$norm |
| .github/workflows/cotahist-fase04-normalizacao-2016-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2016-v1 | DYNAMIC:$evidence, DYNAMIC:$norm |
| .github/workflows/cotahist-fase04-normalizacao-2017-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2017-v1 | DYNAMIC:$evidence, DYNAMIC:$norm, DYNAMIC:$conflict_file |
| .github/workflows/cotahist-fase04-normalizacao-2018-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2018-v1 | DYNAMIC:$evidence, DYNAMIC:$norm, DYNAMIC:$conflict_file |
| .github/workflows/cotahist-fase04-normalizacao-2019-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2019-v1 | DYNAMIC:$evidence, DYNAMIC:$norm, DYNAMIC:$conflict_file |
| .github/workflows/cotahist-fase04-normalizacao-2020-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2020-v1 | DYNAMIC:$evidence, DYNAMIC:$norm, DYNAMIC:$conflict_file |
| .github/workflows/cotahist-fase04-normalizacao-2020-v2.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2020-v2 | DYNAMIC:$evidence, DYNAMIC:$norm, DYNAMIC:$conflict_file |
| .github/workflows/cotahist-fase04-normalizacao-2021-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2021-v1 | DYNAMIC:$evidence, DYNAMIC:$norm, DYNAMIC:$conflict_file |
| .github/workflows/cotahist-fase04-normalizacao-2022-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2022-v1 | DYNAMIC:$evidence, DYNAMIC:$norm, DYNAMIC:$conflict_file |
| .github/workflows/cotahist-fase04-normalizacao-2023-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2023-v2 | dados/cotahist/quality/COTAHIST_2023_FASE02_INTEGRIDADE_FONTE_V1.json, dados/cotahist/quality/COTAHIST_2023_FASE03_PARSING_V1.json, dados/cotahist/quality/COTAHIST_2023_FASE04_NORMALIZACAO_V1.json, dados/cotahist/normalized/anual/COTAHIST_A2023.csv |
| .github/workflows/cotahist-fase04-normalizacao-2024-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2024-v1 | dados/cotahist/quality/COTAHIST_2024_FASE02_INTEGRIDADE_FONTE_V1.json, dados/cotahist/quality/COTAHIST_2024_FASE03_PARSING_V1.json, dados/cotahist/quality/COTAHIST_2024_FASE04_NORMALIZACAO_V1.json, dados/cotahist/normalized/anual/COTAHIST_A2024.csv |
| .github/workflows/cotahist-fase04-normalizacao-2025-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2025-v1 | dados/cotahist/quality/COTAHIST_2025_FASE02_INTEGRIDADE_FONTE_V1.json, dados/cotahist/quality/COTAHIST_2025_FASE03_PARSING_V1.json, dados/cotahist/quality/COTAHIST_2025_FASE04_NORMALIZACAO_V1.json, dados/cotahist/normalized/anual/COTAHIST_A2025.csv |
| .github/workflows/cotahist-fase04-normalizacao-2026-v1.yml | REPO_WRITER | main | cotahist-fase04-normalizacao-2026-v1 | dados/cotahist/quality/COTAHIST_2026_FASE04_NORMALIZACAO_V1.json, dados/cotahist/quality/COTAHIST_2026_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2000-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2000-v1 | dados/cotahist/normalized/anual/COTAHIST_A2000.csv, dados/cotahist/quality/COTAHIST_2000_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2001-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2001-v1 | dados/cotahist/normalized/anual/COTAHIST_A2001.csv, dados/cotahist/quality/COTAHIST_2001_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2002-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2002-v1 | dados/cotahist/normalized/anual/COTAHIST_A2002.csv, dados/cotahist/quality/COTAHIST_2002_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2003-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2003-v1 | dados/cotahist/normalized/anual/COTAHIST_A2003.csv, dados/cotahist/quality/COTAHIST_2003_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2004-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2004-v1 | dados/cotahist/normalized/anual/COTAHIST_A2004.csv, dados/cotahist/quality/COTAHIST_2004_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2005-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2005-v1 | dados/cotahist/normalized/anual/COTAHIST_A2005.csv, dados/cotahist/quality/COTAHIST_2005_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2006-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2006-v1 | dados/cotahist/normalized/anual/COTAHIST_A2006.csv, dados/cotahist/quality/COTAHIST_2006_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2007-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2007-v1 | dados/cotahist/normalized/anual/COTAHIST_A2007.csv, dados/cotahist/quality/COTAHIST_2007_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2008-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2008-v1 | dados/cotahist/normalized/anual/COTAHIST_A2008.csv, dados/cotahist/quality/COTAHIST_2008_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2009-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2009-v1 | dados/cotahist/normalized/anual/COTAHIST_A2009.csv, dados/cotahist/quality/COTAHIST_2009_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2010-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2010-v1 | dados/cotahist/normalized/anual/COTAHIST_A2010.csv, dados/cotahist/quality/COTAHIST_2010_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2011-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2011-v1 | dados/cotahist/normalized/anual/COTAHIST_A2011.csv, dados/cotahist/quality/COTAHIST_2011_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2012-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2012-v1 | dados/cotahist/normalized/anual/COTAHIST_A2012.csv, dados/cotahist/quality/COTAHIST_2012_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2013-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2013-v1 | dados/cotahist/normalized/anual/COTAHIST_A2013.csv, dados/cotahist/quality/COTAHIST_2013_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-recuperar-normalized-2014-v1.yml | REPO_WRITER | main | cotahist-fase04-recuperar-normalized-2014-v1 | dados/cotahist/normalized/anual/COTAHIST_A2014.csv, dados/cotahist/quality/COTAHIST_2014_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-1999-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2000-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2001-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2002-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2003-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2004-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2005-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2006-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2007-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2008-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2009-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2010-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2011-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2012-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2013-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase04-validacao-independente-2014-v1.yml | REPO_WRITER | main | cotahist-fase04-validacao-independente-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE04_NORMALIZACAO_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-1994-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1994_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-1995-v1.yml | REPO_WRITER | main | cotahist-fase05-1995 | dados/cotahist/quality/COTAHIST_1995_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-1996-v1.yml | REPO_WRITER | main | cotahist-fase05-1996 | dados/cotahist/quality/COTAHIST_1996_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-1997-v1.yml | REPO_WRITER | main | cotahist-fase05-1997 | dados/cotahist/quality/COTAHIST_1997_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-1998-v1.yml | REPO_WRITER | main | cotahist-fase05-1998 | dados/cotahist/quality/COTAHIST_1998_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-1999-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2000-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2001-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2002-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2003-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2004-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2005-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2006-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2007-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2008-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2009-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2010-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2011-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2012-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2013-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2014-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2015-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2016-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2017-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2018-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2019-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2020-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2021-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2022-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2023-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2023-v1 | dados/cotahist/quality/COTAHIST_2023_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2024-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2024-v1 | dados/cotahist/quality/COTAHIST_2024_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase05-manifesto-checksum-2025-v1.yml | REPO_WRITER | main | cotahist-fase05-manifesto-checksum-2025-v1 | dados/cotahist/quality/COTAHIST_2025_FASE05_MANIFESTO_CHECKSUM_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-1994-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1994_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-1999-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2000-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2001-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2002-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2003-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2004-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2005-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2006-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2007-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2008-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2009-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2010-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2011-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2012-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2013-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2014-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2015-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2016-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2017-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2018-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2019-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2020-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2021-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2022-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2023-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2023-v1 | dados/cotahist/quality/COTAHIST_2023_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2024-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2024-v1 | dados/cotahist/quality/COTAHIST_2024_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2025-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2025-v1 | dados/cotahist/quality/COTAHIST_2025_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-2026-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-2026-v1 | dados/cotahist/quality/COTAHIST_2026_FASE06_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-fase06-reconciliacao-ohlc-1998-v1.yml | REPO_WRITER | main | cotahist-fase06-reconciliacao-ohlc-1998 | dados/cotahist/quality/COTAHIST_1998_FASE06_RECONCILIACAO_OHLC_V1.json |
| .github/workflows/cotahist-fase06-semantica-1995-v1.yml | REPO_WRITER | main | cotahist-fase06-1995 | dados/cotahist/quality/COTAHIST_1995_FASE06_SEMANTICA_V1.json |
| .github/workflows/cotahist-fase06-semantica-1996-v1.yml | REPO_WRITER | main | cotahist-fase06-1996 | dados/cotahist/quality/COTAHIST_1996_FASE06_SEMANTICA_V1.json |
| .github/workflows/cotahist-fase06-semantica-1997-v1.yml | REPO_WRITER | main | cotahist-fase06-1997 | dados/cotahist/quality/COTAHIST_1997_FASE06_SEMANTICA_V1.json |
| .github/workflows/cotahist-fase06-semantica-1998-v1.yml | REPO_WRITER | main | cotahist-fase06-1998 | dados/cotahist/quality/COTAHIST_1998_FASE06_SEMANTICA_V1.json, dados/cotahist/quality/COTAHIST_1998_FASE06_RECONCILIACAO_OHLC_V1.json |
| .github/workflows/cotahist-fase06b-contexto-term-1998-v1.yml | REPO_WRITER | main | cotahist-fase06b-contexto-term-1998 | dados/cotahist/quality/COTAHIST_1998_FASE06B_CONTEXT_TERM_V1.json |
| .github/workflows/cotahist-fase07-identidade-1999-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2000-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2001-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2002-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2003-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2004-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2005-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2006-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2007-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2008-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2009-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2010-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2011-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2012-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2013-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2014-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2015-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2016-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2017-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2018-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2019-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2020-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2021-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2022-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2022-v2.yml | REPO_WRITER | main | cotahist-fase07-identidade-2022-v2 | dados/cotahist/quality/COTAHIST_2022_FASE07_IDENTIDADE_CHAVES_V2.json |
| .github/workflows/cotahist-fase07-identidade-2023-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2023-v1 | dados/cotahist/quality/COTAHIST_2023_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2024-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2024-v1 | dados/cotahist/quality/COTAHIST_2024_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2025-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2025-v1 | dados/cotahist/quality/COTAHIST_2025_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-2026-v1.yml | REPO_WRITER | main | cotahist-fase07-identidade-2026-v1 | dados/cotahist/quality/COTAHIST_2026_FASE07_IDENTIDADE_CHAVES_V1.json |
| .github/workflows/cotahist-fase07-identidade-historica-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_HISTORICA_V1.json |
| .github/workflows/cotahist-fase07-identidade-historica-1995-v1.yml | REPO_WRITER | main | cotahist-fase07-1995 | dados/cotahist/quality/COTAHIST_1995_FASE07_IDENTIDADE_HISTORICA_V1.json |
| .github/workflows/cotahist-fase07-identidade-historica-1996-v1.yml | REPO_WRITER | main | cotahist-fase07-1996 | dados/cotahist/quality/COTAHIST_1996_FASE07_IDENTIDADE_HISTORICA_V1.json |
| .github/workflows/cotahist-fase07-identidade-historica-1997-v1.yml | REPO_WRITER | main | cotahist-fase07-1997 | dados/cotahist/quality/COTAHIST_1997_FASE07_IDENTIDADE_HISTORICA_V1.json |
| .github/workflows/cotahist-fase07-identidade-historica-1998-v1.yml | REPO_WRITER | main | cotahist-fase07-1998 | dados/cotahist/quality/COTAHIST_1998_FASE07_IDENTIDADE_HISTORICA_V1.json |
| .github/workflows/cotahist-fase07a-colisoes-identidade-1998-v1.yml | REPO_WRITER | main | cotahist-fase07a-1998 | dados/cotahist/quality/COTAHIST_1998_FASE07A_COLISOES_IDENTIDADE_V1.json |
| .github/workflows/cotahist-fase07b-semantica-prazot-1998-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | cotahist-fase07b-${{ github.run_id }} | dados/cotahist/quality/COTAHIST_1998_FASE07B_SEMANTICA_PRAZOT_TPMERC030_V1.json |
| .github/workflows/cotahist-fase07b-tpmerc-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_TPMERC_V1.json |
| .github/workflows/cotahist-fase07c-codbdi-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_CODBDI_V1.json |
| .github/workflows/cotahist-fase07c-validacao-chave-prazot-1997-1999-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | cotahist-fase07c-${{ github.run_id }} | dados/cotahist/quality/COTAHIST_1998_FASE07C_VALIDACAO_CHAVE_PRAZOT_1997_1999_V1.json |
| .github/workflows/cotahist-fase07d-codisi-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_CODISI_V1.json |
| .github/workflows/cotahist-fase07e-dimes-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_DIMES_V1.json |
| .github/workflows/cotahist-fase07f-colisao-k4-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_COLISAO_K4_V1.json |
| .github/workflows/cotahist-fase07g-matriz-identidade-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_FINAL_V1.json |
| .github/workflows/cotahist-fase08-calendario-1999-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2000-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2001-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2002-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2003-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2004-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2005-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2006-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2007-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2008-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2009-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2010-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2011-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2012-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2013-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2014-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2015-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2016-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2017-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2018-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2019-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2020-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2021-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2021-v2.yml | REPO_WRITER | main | cotahist-fase08-calendario-2021-v2 | dados/cotahist/quality/COTAHIST_2021_FASE08_SEMANTICA_CALENDARIO_V2.json |
| .github/workflows/cotahist-fase08-calendario-2022-v2.yml | REPO_WRITER | main | cotahist-fase08-calendario-2022-v2 | dados/cotahist/quality/COTAHIST_2022_FASE08_SEMANTICA_CALENDARIO_V2.json |
| .github/workflows/cotahist-fase08-calendario-2023-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2023-v1 | dados/cotahist/quality/COTAHIST_2023_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2024-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2024-v1 | dados/cotahist/quality/COTAHIST_2024_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2025-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2025-v1 | dados/cotahist/quality/COTAHIST_2025_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-calendario-2026-v1.yml | REPO_WRITER | main | cotahist-fase08-calendario-2026-v1 | dados/cotahist/quality/COTAHIST_2026_FASE08_SEMANTICA_CALENDARIO_V1.json |
| .github/workflows/cotahist-fase08-consistencia-1998-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1998_FASE08_CONSISTENCIA_V1.json |
| .github/workflows/cotahist-fase08-diagnostico-ordem-2021-v1.yml | REPO_WRITER | main | cotahist-fase08-diagnostico-ordem-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE08_DIAGNOSTICO_ORDEM_V1.json |
| .github/workflows/cotahist-fase08-semantica-k4-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_FASE08_SEMANTICA_K4_V1.json |
| .github/workflows/cotahist-fase08-semantica-k4-1995-v1.yml | REPO_WRITER | main | cotahist-fase08-1995 | dados/cotahist/quality/COTAHIST_1995_FASE08_SEMANTICA_K4_V1.json |
| .github/workflows/cotahist-fase08-semantica-k4-1996-v1.yml | REPO_WRITER | main | cotahist-fase08-1996 | dados/cotahist/quality/COTAHIST_1996_FASE08_SEMANTICA_K4_V1.json |
| .github/workflows/cotahist-fase08-semantica-k4-1997-v1.yml | REPO_WRITER | main | cotahist-fase08-1997 | dados/cotahist/quality/COTAHIST_1997_FASE08_SEMANTICA_K4_V1.json |
| .github/workflows/cotahist-fase08a-matriz-calendario-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_MATRIZ_CALENDARIO_PROVISORIA_V1.json |
| .github/workflows/cotahist-fase08b-evidencia-calendario-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_EVIDENCIA_DIAS_UTEIS_AUSENTES_V1.json |
| .github/workflows/cotahist-fase08c-duplicidades-k4-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_FASE08C_DUPLICIDADES_K4_V1.json |
| .github/workflows/cotahist-fase08c-padrao-negociacao-arredores-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_PADRAO_NEGOCIACAO_ARREDORES_V1.json |
| .github/workflows/cotahist-fase08c-padroes-ausencia-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_EVIDENCIA_PADROES_AUSENCIA_V1.json |
| .github/workflows/cotahist-fase08e-cronologia-1986-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1986_FASE08E_CRONOLOGIA_V1.json |
| .github/workflows/cotahist-fase08f-estrutura-estatistica-k4-1986-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1986_FASE08F_ESTRUTURA_ESTATISTICA_K4_V1.json |
| .github/workflows/cotahist-fase08g-recorrencia-perfis-k4-1986-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1986_FASE08G_RECORRENCIA_PERFIS_K4_V1.json |
| .github/workflows/cotahist-fase08h-recurrencia-k4-multianos-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_FASE08H_RECORRENCIA_K4_MULTIANOS_V1.json |
| .github/workflows/cotahist-fase08i-reconstrucao-regra-agregacao-1986-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1986_FASE08I_RECONSTRUCAO_REGRA_AGREGACAO_V1.json |
| .github/workflows/cotahist-fase08p-transicao-vigor-1986-v1.yml | REPO_WRITER | main | cotahist-fase08p-transicao-vigor-1986 | dados/cotahist/quality/COTAHIST_1986_FASE08P_TRANSICAO_VIGOR_0910_1310_V1.json |
| .github/workflows/cotahist-fase09-prerelease-1993-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1993_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-1995-v1.yml | REPO_WRITER | main | cotahist-fase09-1995 | dados/cotahist/quality/COTAHIST_1995_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-1996-v1.yml | REPO_WRITER | main | cotahist-fase09-1996 | dados/cotahist/quality/COTAHIST_1996_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-1997-v1.yml | REPO_WRITER | main | cotahist-fase09-1997 | dados/cotahist/quality/COTAHIST_1997_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-1999-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2000-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2001-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2002-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2003-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2004-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2005-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2006-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2007-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2008-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2009-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2010-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2011-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2012-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2013-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2014-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2015-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2016-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2017-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2018-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2019-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2020-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2021-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2022-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2023-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2023-v1 | dados/cotahist/quality/COTAHIST_2023_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2024-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2024-v1 | dados/cotahist/quality/COTAHIST_2024_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2025-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2025-v1 | dados/cotahist/quality/COTAHIST_2025_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09-prerelease-2026-v1.yml | REPO_WRITER | main | cotahist-fase09-prerelease-2026-v1 | dados/cotahist/quality/COTAHIST_2026_FASE09_PRE_RELEASE_V1.json |
| .github/workflows/cotahist-fase09b-multiplicidade-term-1986-v1.yml | REPO_WRITER | main | cotahist-fase09b-1986 | dados/cotahist/quality/COTAHIST_1986_FASE09B_MULTIPLICIDADE_TERM_V1.json |
| .github/workflows/cotahist-fase10-integridade-1988-v1.yml | REPO_WRITER | main | cotahist-1988-fase10-integridade | dados/cotahist/quality/COTAHIST_1988_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-integridade-1989-v1.yml | REPO_WRITER | main | cotahist-fase10-integridade-1989-v1 | dados/cotahist/quality/COTAHIST_1989_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-integridade-1990-v1.yml | REPO_WRITER | main | cotahist-fase10-integridade-1990-v1 | dados/cotahist/quality/COTAHIST_1990_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-integridade-1991-v1.yml | REPO_WRITER | main | cotahist-fase10-integridade-1991-v1 | dados/cotahist/quality/COTAHIST_1991_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-integridade-1992-v1.yml | REPO_WRITER | main | cotahist-fase10-integridade-1992-v1 | dados/cotahist/quality/COTAHIST_1992_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-integridade-1993-v1.yml | REPO_WRITER | main | cotahist-fase10-integridade-1993-v1 | dados/cotahist/quality/COTAHIST_1993_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-integridade-1995-v1.yml | REPO_WRITER | main | cotahist-fase10-1995 | dados/cotahist/quality/COTAHIST_1995_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-integridade-1996-v1.yml | REPO_WRITER | main | cotahist-fase10-1996 | dados/cotahist/quality/COTAHIST_1996_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-integridade-1997-v1.yml | REPO_WRITER | main | cotahist-fase10-1997 | dados/cotahist/quality/COTAHIST_1997_FASE10_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-1999-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2000-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2001-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2002-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2003-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2004-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2005-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2006-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2007-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2008-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2009-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2010-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2011-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2012-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2013-retry-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2013-retry-v1 | dados/cotahist/quality/COTAHIST_2013_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2013-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2014-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2015-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2016-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2017-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2018-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2019-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2020-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2021-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2022-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2023-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2023-v1 | dados/cotahist/quality/COTAHIST_2023_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2024-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2024-v1 | dados/cotahist/quality/COTAHIST_2024_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validacao-independente-2025-v1.yml | REPO_WRITER | main | cotahist-fase10-validacao-independente-2025-v1 | dados/cotahist/quality/COTAHIST_2025_FASE10_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-fase10-validar-candidato-2026-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | cotahist-fase10-validar-candidato-2026-v1 | dados/cotahist/quality/COTAHIST_2026_FASE10_VALIDACAO_CANDIDATO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-1995-v1.yml | REPO_WRITER | main | cotahist-fase11-1995 | dados/cotahist/quality/COTAHIST_1995_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-1996-v1.yml | REPO_WRITER | main | cotahist-fase11-1996 | dados/cotahist/quality/COTAHIST_1996_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-1997-v1.yml | REPO_WRITER | main | cotahist-fase11-1997 | dados/cotahist/quality/COTAHIST_1997_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-1999-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-1999-v1 | dados/cotahist/quality/COTAHIST_1999_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2000-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2000-v1 | dados/cotahist/quality/COTAHIST_2000_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2001-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2001-v1 | dados/cotahist/quality/COTAHIST_2001_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2002-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2002-v1 | dados/cotahist/quality/COTAHIST_2002_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2003-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2003-v1 | dados/cotahist/quality/COTAHIST_2003_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2004-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2004-v1 | dados/cotahist/quality/COTAHIST_2004_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2005-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2005-v1 | dados/cotahist/quality/COTAHIST_2005_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2006-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2006-v1 | dados/cotahist/quality/COTAHIST_2006_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2007-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2007-v1 | dados/cotahist/quality/COTAHIST_2007_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2008-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2008-v1 | dados/cotahist/quality/COTAHIST_2008_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2009-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2009-v1 | dados/cotahist/quality/COTAHIST_2009_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2010-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2010-v1 | dados/cotahist/quality/COTAHIST_2010_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2011-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2011-v1 | dados/cotahist/quality/COTAHIST_2011_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2012-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2012-v1 | dados/cotahist/quality/COTAHIST_2012_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2013-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2013-v1 | dados/cotahist/quality/COTAHIST_2013_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2014-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2014-v1 | dados/cotahist/quality/COTAHIST_2014_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2015-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2015-v1 | dados/cotahist/quality/COTAHIST_2015_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2016-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2016-v1 | dados/cotahist/quality/COTAHIST_2016_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2017-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2017-v1 | dados/cotahist/quality/COTAHIST_2017_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2018-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2018-v1 | dados/cotahist/quality/COTAHIST_2018_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2019-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2019-v1 | dados/cotahist/quality/COTAHIST_2019_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2020-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2020-v1 | dados/cotahist/quality/COTAHIST_2020_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2021-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2021-v1 | dados/cotahist/quality/COTAHIST_2021_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2022-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2022-v1 | dados/cotahist/quality/COTAHIST_2022_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2023-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2023-v1 | dados/cotahist/quality/COTAHIST_2023_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2024-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2024-v1 | dados/cotahist/quality/COTAHIST_2024_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-certificacao-2025-v1.yml | REPO_WRITER | main | cotahist-fase11-certificacao-2025-v1 | dados/cotahist/quality/COTAHIST_2025_FASE11_CERTIFICACAO_V1.json |
| .github/workflows/cotahist-fase11-promocao-controlada-2026-v1.yml | REPO_WRITER | main | cotahist-fase11-promocao-controlada-2026-v1 | dados/cotahist/raw/anual/COTAHIST_A2026.ZIP, dados/cotahist/manifests/COTAHIST_A2026.json, dados/cotahist/checksums/COTAHIST_A2026.ZIP.sha256, dados/cotahist/normalized/anual/COTAHIST_A2026.csv |
| .github/workflows/cotahist-fase12-fechamento-1995-abertura-1996-v1.yml | REPO_WRITER | main | cotahist-fase12-1995-1996 | dados/cotahist/quality/COTAHIST_1995_FASE12_FECHAMENTO_1996_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-1996-abertura-1997-v1.yml | REPO_WRITER | main | cotahist-fase12-1996-1997-v2 | dados/cotahist/quality/COTAHIST_1996_FASE12_FECHAMENTO_1997_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-1997-abertura-1998-v1.yml | REPO_WRITER | main | cotahist-fase12-1997-1998 | dados/cotahist/quality/COTAHIST_1997_FASE12_FECHAMENTO_1998_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-1999-abertura-2000-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-1999-abertura-2000-v1 | dados/cotahist/quality/COTAHIST_1999_FASE12_FECHAMENTO_2000_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2000-abertura-2001-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2000-abertura-2001-v1 | dados/cotahist/quality/COTAHIST_2000_FASE12_FECHAMENTO_2001_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2001-abertura-2002-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2001-abertura-2002-v1 | dados/cotahist/quality/COTAHIST_2001_FASE12_FECHAMENTO_2002_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2002-abertura-2003-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2002-abertura-2003-v1 | dados/cotahist/quality/COTAHIST_2002_FASE12_FECHAMENTO_2003_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2003-abertura-2004-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2003-abertura-2004-v1 | dados/cotahist/quality/COTAHIST_2003_FASE12_FECHAMENTO_2004_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2004-abertura-2005-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2004-abertura-2005-v1 | dados/cotahist/quality/COTAHIST_2004_FASE12_FECHAMENTO_2005_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2005-abertura-2006-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2005-abertura-2006-v1 | dados/cotahist/quality/COTAHIST_2005_FASE12_FECHAMENTO_2006_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2006-abertura-2007-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2006-abertura-2007-v1 | dados/cotahist/quality/COTAHIST_2006_FASE12_FECHAMENTO_2007_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2007-abertura-2008-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2007-abertura-2008-v1 | dados/cotahist/quality/COTAHIST_2007_FASE12_FECHAMENTO_2008_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2008-abertura-2009-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2008-abertura-2009-v1 | dados/cotahist/quality/COTAHIST_2008_FASE12_FECHAMENTO_2009_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2009-abertura-2010-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2009-abertura-2010-v1 | dados/cotahist/quality/COTAHIST_2009_FASE12_FECHAMENTO_2010_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2010-abertura-2011-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2010-abertura-2011-v1 | dados/cotahist/quality/COTAHIST_2010_FASE12_FECHAMENTO_2011_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2011-abertura-2012-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2011-abertura-2012-v1 | dados/cotahist/quality/COTAHIST_2011_FASE12_FECHAMENTO_2012_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2012-abertura-2013-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2012-abertura-2013-v1 | dados/cotahist/quality/COTAHIST_2012_FASE12_FECHAMENTO_2013_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2013-abertura-2014-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2013-abertura-2014-v1 | dados/cotahist/quality/COTAHIST_2013_FASE12_FECHAMENTO_2014_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2014-abertura-2015-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2014-abertura-2015-v1 | dados/cotahist/quality/COTAHIST_2014_FASE12_FECHAMENTO_2015_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2015-abertura-2016-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2015-abertura-2016-v1 | dados/cotahist/quality/COTAHIST_2015_FASE12_FECHAMENTO_2016_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2016-abertura-2017-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2016-abertura-2017-v1 | dados/cotahist/quality/COTAHIST_2016_FASE12_FECHAMENTO_2017_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2017-abertura-2018-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2017-abertura-2018-v1 | dados/cotahist/quality/COTAHIST_2017_FASE12_FECHAMENTO_2018_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2018-abertura-2019-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2018-abertura-2019-v1 | dados/cotahist/quality/COTAHIST_2018_FASE12_FECHAMENTO_2019_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2019-abertura-2020-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2019-abertura-2020-v1 | dados/cotahist/quality/COTAHIST_2019_FASE12_FECHAMENTO_2020_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2020-abertura-2021-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2020-abertura-2021-v1 | dados/cotahist/quality/COTAHIST_2020_FASE12_FECHAMENTO_2021_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2021-abertura-2022-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2021-abertura-2022-v1 | dados/cotahist/quality/COTAHIST_2021_FASE12_FECHAMENTO_2022_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2022-abertura-2023-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2022-abertura-2023-v1 | dados/cotahist/quality/COTAHIST_2022_FASE12_FECHAMENTO_2023_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2023-abertura-2024-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2023-abertura-2024-v1 | dados/cotahist/quality/COTAHIST_2023_FASE12_FECHAMENTO_2024_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2024-abertura-2025-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2024-abertura-2025-v1 | dados/cotahist/quality/COTAHIST_2024_FASE12_FECHAMENTO_2025_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-2025-abertura-2026-v1.yml | REPO_WRITER | main | cotahist-fase12-fechamento-2025-abertura-2026-v1 | dados/cotahist/quality/COTAHIST_2025_FASE12_FECHAMENTO_2026_ABERTURA_V1.json |
| .github/workflows/cotahist-fase12-fechamento-transicao-1993-v1.yml | REPO_WRITER | main | cotahist-fase12-1993 | dados/cotahist/quality/COTAHIST_1993_FASE12_FECHAMENTO_TRANSICAO_V1.json |
| .github/workflows/cotahist-fase13-materializacao-1996-v1.yml | REPO_WRITER | main | cotahist-fase13-materializacao-1996 | dados/cotahist/normalized/anual/COTAHIST_A1996.csv, dados/cotahist/quality/COTAHIST_1996_FASE13_MATERIALIZACAO_V1.json |
| .github/workflows/cotahist-fase13-materializacao-1997-v1.yml | REPO_WRITER | main | cotahist-fase13-materializacao-1997 | dados/cotahist/normalized/anual/COTAHIST_A1997.csv, dados/cotahist/quality/COTAHIST_1997_FASE13_MATERIALIZACAO_V1.json |
| .github/workflows/cotahist-fase13-materializacao-1998-v1.yml | REPO_WRITER | main | cotahist-fase13-1998 | dados/cotahist/normalized/anual/COTAHIST_A1998.csv, dados/cotahist/quality/COTAHIST_1998_FASE13_MATERIALIZACAO_V1.json |
| .github/workflows/cotahist-fase14-presenca-integridade-1995-v1.yml | REPO_WRITER | main | cotahist-fase14-1995 | dados/cotahist/quality/COTAHIST_1995_FASE14_PRESENCA_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase14-presenca-integridade-1996-v1.yml | REPO_WRITER | main | cotahist-fase14-1996 | dados/cotahist/quality/COTAHIST_1996_FASE14_PRESENCA_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase14-presenca-integridade-1997-v1.yml | REPO_WRITER | main | cotahist-fase14-1997 | dados/cotahist/quality/COTAHIST_1997_FASE14_PRESENCA_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-fase14-presenca-integridade-1998-v1.yml | REPO_WRITER | main | cotahist-fase14-1998 | dados/cotahist/quality/COTAHIST_1998_FASE14_PRESENCA_INTEGRIDADE_V1.json |
| .github/workflows/cotahist-gate-06-08-1999-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1999_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2000-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2000_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2001-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2001_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2002-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2002_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2003-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2003_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2004-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2004_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2005-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2005_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2006-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2006_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2007-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2007_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2008-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2008_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2009-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2009_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2010-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2010_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2011-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2011_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2012-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2012_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2013-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_2013_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2014-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2014-v1 | dados/cotahist/quality/COTAHIST_2014_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2015-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2015-v1 | dados/cotahist/quality/COTAHIST_2015_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2016-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2016-v1 | dados/cotahist/quality/COTAHIST_2016_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2017-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2017-v1 | dados/cotahist/quality/COTAHIST_2017_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2018-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2018-v1 | dados/cotahist/quality/COTAHIST_2018_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2019-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2019-v1 | dados/cotahist/quality/COTAHIST_2019_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2020-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2020-v1 | dados/cotahist/quality/COTAHIST_2020_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2021-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2021-v1 | dados/cotahist/quality/COTAHIST_2021_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2022-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2022-v1 | dados/cotahist/quality/COTAHIST_2022_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2023-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2023-v1 | dados/cotahist/quality/COTAHIST_2023_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2024-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2024-v1 | dados/cotahist/quality/COTAHIST_2024_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2025-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2025-v1 | dados/cotahist/quality/COTAHIST_2025_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-06-08-2026-v1.yml | REPO_WRITER | main | cotahist-gate-06-08-2026-v1 | dados/cotahist/quality/COTAHIST_2026_GATE_06_08_V1.json |
| .github/workflows/cotahist-gate-historico-1986.yml | REPO_WRITER | main | cotahist-gate-historico-1986 | .gitattributes, dados/cotahist/normalized/anual/COTAHIST_A1986.csv, dados/cotahist/normalized/manifests/COTAHIST_A1986.csv.sha256, dados/cotahist/quality/COTAHIST_A1986_SEMANTIC_AUDIT.json |
| .github/workflows/cotahist-importacao-diaria-v1.yml | REPO_WRITER | main | cotahist-importacao-diaria-v1 | dados/cotahist/raw/diario, dados/cotahist/normalized/diario, dados/cotahist/normalized/manifests/diario, dados/cotahist/quality/diario |
| .github/workflows/cotahist-integridade-campos-1987-v1.yml | REPO_WRITER | main | cotahist-1987-integridade-campos | dados/cotahist/quality/COTAHIST_1987_AUDITORIA_INTEGRIDADE_CAMPOS_V1.json |
| .github/workflows/cotahist-integridade-campos-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_AUDITORIA_INTEGRIDADE_CAMPOS_V1.json |
| .github/workflows/cotahist-lfs-migracao-controlada-a1987-v1.yml | REPO_WRITER | main | cotahist-lfs-a1987-migracao-controlada | DYNAMIC:$FILE, dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json, dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json |
| .github/workflows/cotahist-m2-certificacao-fisica-1987-v2.yml | REPO_WRITER | main | cotahist-m2-certificacao-fisica | dados/cotahist/certificacao/v2/COTAHIST_A1987_CERTIFICACAO_FISICA_V2.0.json |
| .github/workflows/cotahist-m3-1b-prova-lfs-2026.yml | REPO_WRITER | main | cotahist-m3-1b-lfs-2026 | .gitattributes, dados/cotahist/normalized/anual/COTAHIST_A2026.csv |
| .github/workflows/cotahist-m3-1b-reconciliar-manifest-2026.yml | REPO_WRITER | main | cotahist-m3-1b-reconciliar-manifest-2026 | dados/cotahist/normalized/manifests/COTAHIST_A2026_quality.json, dados/cotahist/quality/COTAHIST_A2026_RECONCILIACAO_MANIFEST_V1.json |
| .github/workflows/cotahist-main-publisher.yml | REPO_WRITER | main | b3-cotahist-main-publish-${{ github.ref }} | dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv, dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json, dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json |
| .github/workflows/cotahist-materializar-normalized-1989-v1.yml | REPO_WRITER | main | cotahist-materializar-normalized-1989-v1 | dados/cotahist/normalized/anual/COTAHIST_A1989.csv |
| .github/workflows/cotahist-materializar-normalized-1990-v1.yml | REPO_WRITER | main | cotahist-materializar-normalized-1990-v1 | dados/cotahist/normalized/anual/COTAHIST_A1990.csv |
| .github/workflows/cotahist-materializar-normalized-1991-v1.yml | REPO_WRITER | main | cotahist-materializar-normalized-1991-v1 | dados/cotahist/normalized/anual/COTAHIST_A1991.csv |
| .github/workflows/cotahist-materializar-normalized-1992-v1.yml | REPO_WRITER | main | cotahist-materializar-normalized-1992-v1 | dados/cotahist/normalized/anual/COTAHIST_A1992.csv |
| .github/workflows/cotahist-materializar-normalized-1993-v1.yml | REPO_WRITER | main | cotahist-materializar-normalized-1993-v1 | dados/cotahist/normalized/anual/COTAHIST_A1993.csv |
| .github/workflows/cotahist-normalizacao-1988-v1.yml | REPO_WRITER | main | cotahist-normalizacao-1988 | dados/cotahist/normalized/anual/COTAHIST_A1988.csv, dados/cotahist/normalized/manifests/COTAHIST_A1988_quality.json |
| .github/workflows/cotahist-normalizacao-controlada-v7.yml | REPO_WRITER | main | cotahist-normalizacao-controlada-v7 | dados/cotahist/normalized/manifests/COTAHIST_A${ano}_quality.json, dados/cotahist/normalized/manifests/COTAHIST_A${ano}.csv.sha256 |
| .github/workflows/cotahist-normalized-m1-1987.yml | REPO_WRITER | main | cotahist-normalized-m1-1987 | dados/cotahist/normalized/anual/COTAHIST_A1987.csv |
| .github/workflows/cotahist-ohlc-1986-v2.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_AUDITORIA_OHLC_V2.json |
| .github/workflows/cotahist-ohlc-excecoes-contexto-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_OHLC_EXCECOES_CONTEXT_V1.json |
| .github/workflows/cotahist-prazot-anomalias-1987-v1.yml | REPO_WRITER | main | cotahist-1987-prazot-anomalias | dados/cotahist/quality/COTAHIST_1987_PRAZOT_ANOMALIAS_V1.json |
| .github/workflows/cotahist-quantidade-volume-preco-1986-v1.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_AUDITORIA_QUANTIDADE_VOLUME_PRECO_V1.json |
| .github/workflows/cotahist-reconciliacao-1987-v1.yml | REPO_WRITER | main | cotahist-1987-reconciliacao | dados/cotahist/quality/COTAHIST_1987_RECONCILIACAO_RAW_NORMALIZED_V1.json |
| .github/workflows/cotahist-reconciliacao-1988-v1.yml | REPO_WRITER | main | cotahist-1988-reconciliacao | dados/cotahist/quality/COTAHIST_1988_RECONCILIACAO_RAW_NORMALIZED_V1.json |
| .github/workflows/cotahist-reconciliacao-final-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_RECONCILIACAO_FINAL_V1.json |
| .github/workflows/cotahist-reconciliacao-raw-normalized-1986-v1.yml | REPO_WRITER | main | cotahist-reconciliacao-raw-normalized-1986 | dados/cotahist/quality/COTAHIST_1986_RECONCILIACAO_RAW_NORMALIZED_V1.json |
| .github/workflows/cotahist-reconciliacao-semantica-1986.yml | REPO_WRITER | UPSTREAM_OR_IMPLICIT | MISSING | dados/cotahist/quality/COTAHIST_1986_RECONCILIACAO_SEMANTICA_V1.json |
| .github/workflows/cotahist-reconciliacao-tpmerc021-bvbg028-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_A2026_TPMERC021_BVBG028_RECONCILIACAO_V1.json |
| .github/workflows/cotahist-recuperar-normalized-1999-v1.yml | REPO_WRITER | main | cotahist-recuperar-normalized-1999-v1 | dados/cotahist/normalized/anual/COTAHIST_A1999.csv, dados/cotahist/quality/COTAHIST_1999_FASE04_RECUPERACAO_V1.json |
| .github/workflows/cotahist-refresh-probe-2026-v1.yml | REPO_WRITER | main | cotahist-refresh-probe-2026-v1 | dados/cotahist/quality/COTAHIST_2026_FONTE_OFICIAL_REFRESH_PROBE_V1.json |
| .github/workflows/cotahist-semantica-1987-v1.yml | REPO_WRITER | main | cotahist-1987-semantica | dados/cotahist/quality/COTAHIST_1987_AUDITORIA_SEMANTICA_V1.json |
| .github/workflows/cotahist-semantica-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_AUDITORIA_SEMANTICA_V1.json |
| .github/workflows/cotahist-validacao-independente-1988-v1.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/cotahist-validacao-independente-1988-v2.yml | REPO_WRITER | main | MISSING | dados/cotahist/quality/COTAHIST_1988_VALIDACAO_INDEPENDENTE_V1.json |
| .github/workflows/rec001-cotahist-bloomberg-mail.yml | REPO_WRITER | main | rec001-cotahist-bloomberg-mail | dados/cotahist/quality/COTAHIST_A2026_REC001_BLOOMBERG_MAIL_V1.json |

## Recursos com múltiplos escritores estáticos

- Destinos estáticos partilhados: **11**
- Escritores com alvo dinâmico ou não resolvido: **15**

| Recurso de escrita | Nº de workflows | Writers |
|---|---:|---|
| .gitattributes | 2 | .github/workflows/cotahist-gate-historico-1986.yml, .github/workflows/cotahist-m3-1b-prova-lfs-2026.yml |
| dados/cotahist/normalized/anual/COTAHIST_A1996.csv | 2 | .github/workflows/cotahist-fase04-normalizacao-1996-v1.yml, .github/workflows/cotahist-fase13-materializacao-1996-v1.yml |
| dados/cotahist/normalized/anual/COTAHIST_A1997.csv | 2 | .github/workflows/cotahist-fase04-normalizacao-1997-v1.yml, .github/workflows/cotahist-fase13-materializacao-1997-v1.yml |
| dados/cotahist/normalized/anual/COTAHIST_A1998.csv | 2 | .github/workflows/cotahist-fase04-normalizacao-1998-v1.yml, .github/workflows/cotahist-fase13-materializacao-1998-v1.yml |
| dados/cotahist/normalized/anual/COTAHIST_A2026.csv | 2 | .github/workflows/cotahist-fase11-promocao-controlada-2026-v1.yml, .github/workflows/cotahist-m3-1b-prova-lfs-2026.yml |
| dados/cotahist/normalized/manifests/COTAHIST_A2026_quality.json | 2 | .github/workflows/cotahist-fase11-promocao-controlada-2026-v1.yml, .github/workflows/cotahist-m3-1b-reconciliar-manifest-2026.yml |
| dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json | 2 | .github/workflows/cotahist-lfs-migracao-controlada-a1987-v1.yml, .github/workflows/cotahist-main-publisher.yml |
| dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json | 2 | .github/workflows/cotahist-auditoria-fisica-normalized-v1.yml, .github/workflows/cotahist-lfs-migracao-controlada-a1987-v1.yml |
| dados/cotahist/quality/COTAHIST_1988_VALIDACAO_INDEPENDENTE_V1.json | 2 | .github/workflows/cotahist-validacao-independente-1988-v1.yml, .github/workflows/cotahist-validacao-independente-1988-v2.yml |
| dados/cotahist/quality/COTAHIST_1998_FASE06_RECONCILIACAO_OHLC_V1.json | 2 | .github/workflows/cotahist-fase06-reconciliacao-ohlc-1998-v1.yml, .github/workflows/cotahist-fase06-semantica-1998-v1.yml |
| dados/cotahist/quality/COTAHIST_2013_FASE10_VALIDACAO_INDEPENDENTE_V1.json | 2 | .github/workflows/cotahist-fase10-validacao-independente-2013-retry-v1.yml, .github/workflows/cotahist-fase10-validacao-independente-2013-v1.yml |

O JSON desta auditoria contém o inventário completo, incluindo workflows sem escrita efetiva.
