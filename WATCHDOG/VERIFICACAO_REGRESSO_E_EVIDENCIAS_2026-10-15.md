# Verificação de regressões WATCHDOG — 2026-10-15

| Campo | Valor |
|---|---|
| **ID** | B3-WD-REGRESSION-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_VERIFICACAO |
| **Fase** | FASE_C_OPERACAO_E_GOVERNANCA / FASE_D_INTEGRIDADE_DOS_DADOS |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | dbef3047b2798d238bb490de85ad54beb795ae931eefd8feff3687e27b81364e |
| **Commit de referência (versão anterior)** | [37a02d83a1a9884f733b56fcba632c99553ec3f3](https://github.com/carlos-andrade/B3/commit/37a02d83a1a9884f733b56fcba632c99553ec3f3) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável operacional do projeto B3 |
| **Aprovador** | Pendente — não representa aprovação formal |
| **Origem** | Logs GitHub Actions referenciados na Issue #11 e evidências do WATCHDOG |
| **Autoridade superior** | [Constituição GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md), [Norma de cabeçalho 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) e [Carta WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Evidências confirmadas e atualizadas

- **Índices B3:** [run #24](https://github.com/carlos-andrade/B3/actions/runs/38751655690): seis testes passaram, 34 índices validados, zero rejeitados e persistência remota confirmada após a correção.
- **Auditoria documental:** [run #89](https://github.com/carlos-andrade/B3/actions/runs/38756553376): 302 ficheiros analisados, 52 conformes, 249 com cabeçalho de controlo inválido e um sem H1. O workflow passou tecnicamente; a conformidade global continua reprovada.
- **COTAHIST V2:** [run #11](https://github.com/carlos-andrade/B3/actions/runs/38755859349): dataset de 41 anos (1986–2026) gerado e persistido após materialização Git LFS; o gate runtime verificou hashes físicos, sidecars/manifestos, contagens, campos e datas. Falta revisão independente da proveniência RAW.
- **Importação diária COTAHIST:** [run #35](https://github.com/carlos-andrade/B3/actions/runs/38755834492): importação e reconciliação anual 2026 aprovadas; persistência remota concluída, zero dias em conflito e 23 ficheiros de evidência publicados.
- **Validação WATCHDOG:** [run #59](https://github.com/carlos-andrade/B3/actions/runs/38756553870): validação estrutural passou para dois sistemas, oito datasets monitorizados e seis controlos catalogados; não prova heartbeat externo efetivo nem aprovação humana de limiares/SLA.

## 2. Ações obrigatórias ainda abertas

1. Reconciliar independentemente a proveniência dos bytes RAW e os hashes físicos por ano, sem alterar sidecars ou manifestos para forçar correspondência.
2. Corrigir cabeçalhos documentais em lotes pequenos, com diffs verificáveis e nova auditoria após cada lote.
3. Aprovar os limiares de atualidade e testar heartbeat independente, SLA/escalonamento e retenção duradoura de evidências.
4. Manter [Issue #11](https://github.com/carlos-andrade/B3/issues/11) aberta até haver causa final, correção, commit, regressão e evidência reconciliada para cada incidente.

## 3. Decisão

A eficácia da persistência está demonstrada para índices, importação diária e Dataset Oficial V2 nas execuções referenciadas. A Fase C permanece EM_CURSO; a Fase D permanece em revisão independente de proveniência RAW. Não declarar certificação global.
