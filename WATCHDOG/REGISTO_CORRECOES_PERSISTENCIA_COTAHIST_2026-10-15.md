# Registo de correções de persistência COTAHIST — 2026-10-15

| Campo | Valor |
|---|---|
| **ID** | B3-WD-COTAHIST-PERSIST-002 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Tipo documental** | REGISTO_DE_CORRECAO |
| **Fase** | FASE_C_OPERACAO_E_GOVERNANCA / FASE_D_INTEGRIDADE_DOS_DADOS |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.0 |
| **Data de atualização** | 2026-10-15 |
| **Aprovador** | Pendente |
| **Autoridade superior** | [Constituição GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) e [Carta WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Contexto e evidência anterior

- [COTAHIST importação diária run #30](https://github.com/carlos-andrade/B3/actions/runs/38569195580): captura e reconciliação passaram, mas a persistência falhou.
- [COTAHIST Dataset Oficial V2 run #9](https://github.com/carlos-andrade/B3/actions/runs/38577021350): o gate bloqueou corretamente a publicação devido a divergências de hash entre bytes físicos, auditoria, sidecar e manifesto.
- A análise do workflow diário mostrou um `git pull --rebase` seguido de um único `git push`, sem repetição em caso de atualização concorrente. O comando `git commit ... || exit 0` também podia terminar o job antes do gate e da publicação de evidências quando não havia alterações.

## 2. Alterações aplicadas

1. **Importação diária** — commit [d79f1d311a41e8dfa7d04b6230c60f9bf02a2909](https://github.com/carlos-andrade/B3/commit/d79f1d311a41e8dfa7d04b6230c60f9bf02a2909): persistência condicional e até cinco tentativas de `fetch` + `rebase` + `push`; falha explícita se as tentativas não forem bem-sucedidas; ausência de alterações já não termina o job antes dos gates.
2. **Dataset Oficial V2** — commit [b8a8e9836251343b9287376e0957a48ee77e38a0](https://github.com/carlos-andrade/B3/commit/b8a8e9836251343b9287376e0957a48ee77e38a0): mesma estratégia de persistência; correção do redirecionamento de `GITHUB_STEP_SUMMARY`; remoção de duplicação no trigger de auditoria física.

## 3. Verificação posterior

- [Índices B3 run #24](https://github.com/carlos-andrade/B3/actions/runs/38751655690) concluiu com sucesso após a lógica de retry já existente no workflow: 6 testes passaram, 34 índices validados, zero rejeitados; commit de dados remoto confirmado nos logs.
- [Importação diária run #35](https://github.com/carlos-andrade/B3/actions/runs/38755834492) terminou com sucesso: importação diária e reconciliação anual 2026 aprovadas; commit, rebase e push remoto concluídos; gate `EXECUCAO_SEM_CONFLITOS` com zero dias em conflito; 23 ficheiros de evidência publicados.
- [Dataset Oficial V2 run #11](https://github.com/carlos-andrade/B3/actions/runs/38755859349) terminou com sucesso. O script fail-closed gerou e persistiu o dataset com 41 anos (1986–2026), após materializar os CSVs anuais via Git LFS; o commit de dados foi rebased e enviado para `main`, e o artefacto foi publicado. O código validou em runtime o estado da auditoria global, hashes físicos contra auditoria/sidecar/manifesto, contagem de linhas e campos, e datas. Esta validação corresponde à evidência disponível no repositório e na execução, não substituindo uma revisão independente da proveniência dos ficheiros RAW.

## 4. Riscos e gates pendentes

- Não recalcular ou alterar sidecars/manifests para forçar correspondência: reconciliar proveniência e bytes físicos por ano.
- Execução diária #35 verificada: sucesso, gate de conflitos aprovado e artefactos publicados.
- Dataset Oficial V2 #11 verificado: geração de 41 anos, persistência e publicação do artefacto concluídas com sucesso; manter monitorização e revisão independente de proveniência RAW.
- Corrigir os cabeçalhos documentais em lotes controlados; auditoria #86 reportou 301 ficheiros: 52 conformes, 248 com cabeçalho de controlo inválido e 1 sem H1.
- Manter a [Issue #11](https://github.com/carlos-andrade/B3/issues/11) aberta até resolver os incidentes e obter evidência final.
- Aprovar formalmente os limiares provisórios de atualidade e testar heartbeat independente, escalonamento/SLA e retenção duradoura.

## 5. Decisão

As correções de persistência foram implementadas. A eficácia da persistência está **demonstrada para índices, importação diária e Dataset Oficial V2** nas execuções verificadas. O gate físico do Dataset Oficial V2 aceitou os 41 anos no runtime da run #11. A Fase C permanece EM_CURSO; a Fase D pode avançar para validação de proveniência RAW e revisão independente, sem declarar certificação global final antes dessa revisão.
