# Registo de correções de persistência COTAHIST — 2026-10-15

| Campo | Valor |
|---|---|
| **ID** | B3-WD-COTAHIST-PERSIST-002 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | REGISTO_DE_CORRECAO |
| **Fase** | FASE_C_OPERACAO_E_GOVERNANCA / FASE_D_INTEGRIDADE_DOS_DADOS |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 35ff57753921d501684cf149f05a153ea865213cd34e04f8e3626d48cb2f9cf3 |
| **Commit de referência (versão anterior)** | [0e89f25a38e10b7efcf129647dd9de906b4d7d5e](https://github.com/carlos-andrade/B3/commit/0e89f25a38e10b7efcf129647dd9de906b4d7d5e) |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — requer aprovação humana |
| **Origem** | Runs de GitHub Actions referenciadas neste registo e histórico Git do repositório |
| **Autoridade superior** | [Constituição GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md), [Carta WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md) e [Norma de cabeçalho 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Estado e evidências verificadas

- [Índices B3 run #24](https://github.com/carlos-andrade/B3/actions/runs/38751655690): 6 testes passaram, 34 índices validados, zero rejeitados e persistência remota confirmada.
- [Importação diária COTAHIST run #35](https://github.com/carlos-andrade/B3/actions/runs/38755834492): importação e reconciliação anual 2026 aprovadas, persistência concluída, zero dias em conflito e 23 ficheiros de evidência publicados.
- [Dataset Oficial V2 run #11](https://github.com/carlos-andrade/B3/actions/runs/38755859349): dataset de 41 anos (1986–2026) gerado e persistido após materialização Git LFS; validação runtime dos hashes físicos, contagens, campos e datas. Não substitui revisão independente da proveniência RAW.
- [Auditoria documental canónica run #89](https://github.com/carlos-andrade/B3/actions/runs/38756553376): execução e artefacto concluídos; 302 ficheiros analisados, 52 CONFORME, 249 CABECALHO_CONTROLO_INVALIDO e 1 SEM_CABECALHO_H1. Sucesso técnico não equivale a conformidade global.
- [Validação WATCHDOG run #59](https://github.com/carlos-andrade/B3/actions/runs/38756553870): validação estrutural passou para 2 sistemas, 8 datasets monitorizados e 6 controlos catalogados. Não prova receção efetiva de heartbeat externo nem aprovação humana de limiares/SLA.

## 2. Correções de persistência

1. [Commit diário d79f1d3](https://github.com/carlos-andrade/B3/commit/d79f1d311a41e8dfa7d04b6230c60f9bf02a2909): até cinco tentativas de fetch/rebase/push e falha explícita após esgotamento; ausência de alterações não interrompe gates.
2. [Commit Dataset V2 b8a8e98](https://github.com/carlos-andrade/B3/commit/b8a8e9836251343b9287376e0957a48ee77e38a0): retry de persistência, correção de GITHUB_STEP_SUMMARY e remoção de trigger duplicado de auditoria física.

## 3. Riscos e próxima ação

- Não alterar RAW, sidecars ou manifestos para forçar correspondência de hashes; reconciliar bytes físicos e proveniência por ano.
- Corrigir cabeçalhos em lotes pequenos, inspecionados e validados, preservando o corpo e o histórico.
- Aprovar formalmente limiares de atualidade e testar heartbeat independente, SLA/escalonamento e retenção duradoura.
- Manter a [Issue #11](https://github.com/carlos-andrade/B3/issues/11) aberta até os gates pendentes serem resolvidos.
- A Fase C permanece EM_CURSO; a Fase D permanece em revisão independente de proveniência RAW. Não declarar certificação global.

## 4. Decisão

A eficácia da persistência está demonstrada para os três fluxos verificados (índices, importação diária e Dataset Oficial V2). Próxima ação: corrigir um lote piloto reduzido de cabeçalhos e reexecutar a auditoria, medindo a redução objetiva de não conformidades.
