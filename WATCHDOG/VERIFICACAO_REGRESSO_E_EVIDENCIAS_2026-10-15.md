# Verificação de regressões WATCHDOG — 2026-10-15

| Campo | Valor |
|---|---|
| **ID** | B3-WD-REGRESSION-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Tipo documental** | RELATORIO_DE_VERIFICACAO |
| **Fase** | FASE_C_OPERACAO_E_GOVERNANCA |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — auditor canónico após commit |
| **Data de atualização** | 2026-10-15 |
| **Aprovador** | Pendente |
| **Autoridade superior** | [CONSTITUICAO](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) e [Carta WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Evidências confirmadas

- **Índices B3:** [run #23](https://github.com/carlos-andrade/B3/actions/runs/38751515742): 6 testes passaram, 34 índices validados e zero rejeitados; persistência falhou porque o push foi rejeitado com `fetch first` após rebase. A concorrência não está comprovadamente resolvida.
- **Auditoria documental:** [run #75](https://github.com/carlos-andrade/B3/actions/runs/38749840001): quatro testes passaram; 298 ficheiros analisados, 44 conformes, 253 com cabeçalho de controlo inválido e um sem H1. Sucesso do workflow não significa conformidade global.
- **COTAHIST V2:** [run #9](https://github.com/carlos-andrade/B3/actions/runs/38577021350): gate bloqueou a geração/publicação devido a divergências de SHA físico, sidecar, manifesto e auditoria em múltiplos anos. Manter bloqueio até reconciliação por ano.
- **Importação diária COTAHIST:** [run #30](https://github.com/carlos-andrade/B3/actions/runs/38569195580): captura e reconciliação passaram; persistência falhou.

## Ações obrigatórias

1. Confirmar nova execução após a correção de persistência concorrente dos índices.
2. Reconciliar bytes físicos, SHA-256, sidecars, manifestos e auditoria COTAHIST por ano.
3. Corrigir a concorrência de persistência diária e comprovar commit remoto.
4. Priorizar correções de cabeçalho documental com testes de regressão.
5. Manter [Issue #11](https://github.com/carlos-andrade/B3/issues/11) aberta até haver causa final, correção, commit, regressão e evidência reconciliada para cada incidente.

## Decisão

A Fase C permanece EM_CURSO. Não foram recalculados nesta verificação os hashes dos ficheiros físicos num checkout independente, nem confirmado heartbeat externo. Esses controlos continuam pendentes.
