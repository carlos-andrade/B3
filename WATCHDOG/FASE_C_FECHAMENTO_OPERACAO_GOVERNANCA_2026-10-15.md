# FASE C — Fechamento de Operação e Governança do B3

| Campo | Valor |
|---|---|
| **ID** | B3-WD-FC-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | FASE_C_OPERACAO_E_GOVERNANCA |
| **Estado** | EM_CURSO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 2ae47460304997acfd64a61b19c6cd1b098220c3917b0ed4d6c97eb144780a7f |
| **Commit de referência (versão anterior)** | N/A — revisão inicial segundo a norma documental |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável operacional do projeto B3 |
| **Aprovador** | Pendente — não representa aprovação formal |
| **Origem** | Auditoria operacional WATCHDOG e Issue #11; revisão segundo GOVERNANCA |
| **Autoridade superior** | [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md), [Norma de Cabeçalho v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md), [Carta WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Resumo executivo

A infraestrutura básica existe e tem execuções recentes bem-sucedidas. Contudo, não é correto declarar a Fase C concluída: o supervisor externo por heartbeat está inativo até serem configuradas duas secrets, os limiares de atualidade continuam provisórios, a política de confirmação/escalonamento não está operacional e a retenção dos relatórios é de 30 dias, não imutável.

Além disso, a auditoria do monitor de execuções identificou uma issue aberta com falhas históricas recentes. O sucesso das execuções posteriores não apaga essas ocorrências; elas exigem triagem e evidência de recuperação.

## 2. Evidências verificadas

| Controlo | Evidência observada | Estado |
|---|---|---|
| Monitor de execuções GitHub Actions | Workflow agendado a cada 15 minutos; janela móvel de 24 horas; paginação; relatório JSON/Markdown; issue de alerta | IMPLEMENTADO, com limitações |
| Monitor de atualidade | Workflow diário; testes do avaliador; relatório por dataset; alerta para STALE/UNKNOWN | IMPLEMENTADO, limiares ainda provisórios |
| Última execução do monitor de atualidade consultada | [Run 38736100468](https://github.com/carlos-andrade/B3/actions/runs/38736100468), conclusão success | PASS de execução, não certificação global |
| Auditoria SHA-256 documental | [Run 38732542000](https://github.com/carlos-andrade/B3/actions/runs/38732542000), conclusão success | PASS de execução |
| Sincronização da Wiki | [Run 38737503360](https://github.com/carlos-andrade/B3/actions/runs/38737503360), conclusão success | PASS de execução |
| Issue de falhas do monitor | [Issue #11](https://github.com/carlos-andrade/B3/issues/11), relatório de 15/10/2026 12:04 UTC: 12 execuções desfavoráveis em 24 horas e 1 ativa | ABERTA — triagem necessária |
| Issue de atualidade | [Issue #8](https://github.com/carlos-andrade/B3/issues/8), fechada após recuperação em 14/10/2026 | Recuperação registada; limiares continuam provisórios |
| Supervisão independente | Secrets `WATCHDOG_HEARTBEAT_WORKFLOWS_URL` e `WATCHDOG_HEARTBEAT_DATA_URL` não confirmadas como configuradas | PENDENTE |
| Confirmação de receção e escalonamento | Issue GitHub existe; ACK, responsáveis primário/suplente e SLA não demonstrados | PARCIAL |
| Retenção das evidências | Artefactos GitHub Actions configurados para 30 dias | PARCIAL; não é arquivo imutável |
| Limiares de atualidade | Oito controlos listados no documento de revisão sem aprovação do proprietário | PENDENTE |

## 3. Plano de encerramento obrigatório

### C1 — Triagem das falhas de workflows

- [ ] Analisar as 12 execuções desfavoráveis registadas na issue #11.
- [ ] Distinguir falhas corrigidas, cancelamentos esperados, falhas transitórias e defeitos ainda ativos.
- [ ] Associar cada falha a causa, correção e execução posterior bem-sucedida, quando aplicável.
- [ ] Atualizar ou encerrar a issue somente após confirmar que não há incidentes ativos sem tratamento.

**Critério de aceitação:** nenhuma falha crítica sem classificação, responsável ou ação de seguimento.

### C2 — Aprovação dos limiares de atualidade

Rever `WATCHDOG/limiares-provisorios-revisao.md` e decidir cada uma das oito regras monitorizadas. A decisão deve incluir periodicidade esperada, tratamento de fins de semana/feriados, limiar, proprietário, data e justificação.

- [ ] BCB-SGS-432
- [ ] BCB-SGS-11
- [ ] BCB-SGS-12
- [ ] BCB-SGS-1
- [ ] BCB-SGS-433 (IPCA)
- [ ] B3-BDI-DAILY-AVERAGE-STOCKS
- [ ] COTAHIST-2026
- [ ] COTAHIST-DIARIO

**Critério de aceitação:** nenhuma regra é promovida de PROVISIONAL sem decisão explícita registada.

### C3 — Ativar supervisão externa independente

No repositório GitHub, em **Settings → Secrets and variables → Actions**, configurar duas secrets distintas:

- `WATCHDOG_HEARTBEAT_WORKFLOWS_URL`: endpoint de heartbeat exclusivo do monitor de workflows.
- `WATCHDOG_HEARTBEAT_DATA_URL`: endpoint de heartbeat exclusivo do monitor de atualidade.

As URLs devem pertencer a um serviço externo à execução GitHub Actions. Não publicar os valores das secrets em commits, issues ou mensagens.

- [ ] Configurar as duas secrets.
- [ ] Executar manualmente os dois workflows.
- [ ] Confirmar a receção de cada heartbeat no serviço externo.
- [ ] Simular ausência de heartbeat e confirmar o alerta.
- [ ] Registar a evidência de aceitação.

**Critério de aceitação:** a ausência de execução do monitor gera alerta externo independentemente do próprio GitHub Actions.

### C4 — Confirmar alertas e escalonamento

- [ ] Definir responsável primário e suplente.
- [ ] Definir SLA de reconhecimento e resolução por severidade.
- [ ] Confirmar o canal de entrega e a receção real dos alertas.
- [ ] Testar escalonamento quando não há reconhecimento.
- [ ] Documentar recuperação e encerramento do incidente.

**Critério de aceitação:** o alerta é recebido por uma pessoa/sistema responsável e existe um caminho de escalonamento testado.

### C5 — Evidência persistente

- [ ] Manter artefactos de 30 dias como evidência operacional de curto prazo.
- [ ] Definir armazenamento durável para relatórios, incidentes e aprovações que precisem de retenção superior.
- [ ] Preservar hashes, links das execuções, commit, timestamps UTC e decisão de auditoria.
- [ ] Não declarar os artefactos do GitHub como armazenamento imutável.

**Critério de aceitação:** as evidências críticas permanecem acessíveis pelo período de retenção aprovado e têm integridade verificável.

### C6 — Regressão e aceitação final

- [ ] Executar testes do avaliador de atualidade.
- [ ] Executar monitor de workflows e confirmar relatório.
- [ ] Executar auditoria SHA-256 documental.
- [ ] Confirmar que os dois heartbeats foram recebidos externamente.
- [ ] Confirmar que não existem incidentes críticos sem classificação.
- [ ] Registar a aceitação final e atualizar o estado da Fase C.

## 4. Regras de governança

1. Um workflow concluído com sucesso prova a conclusão daquela execução, não a qualidade total dos dados.
2. `PASS` com limiar `PROVISIONAL` não significa que a política de atualidade tenha sido aprovada.
3. Uma issue de incidente não deve ser encerrada só porque uma execução posterior passou; é necessária triagem e evidência.
4. A ausência de secret de heartbeat deve continuar visível como limitação, nunca ser descrita como supervisão independente ativa.
5. Não colocar tokens, URLs privadas de heartbeat ou outros segredos em documentação pública.
6. Alterações de estado devem ser sustentadas por evidências e registadas no repositório.

## 5. Decisão da auditoria

**A Fase C não está encerrada.** A infraestrutura interna está implementada em parte, mas a conclusão depende de ações humanas e de integração externa que não podem ser inferidas das execuções do GitHub.

**Próxima ação operacional:** tratar a issue #11 e configurar as duas secrets de heartbeat no GitHub; em paralelo, aprovar os oito limiares no documento de revisão. Após essas ações, executar o teste de aceitação C6.

## 6. Referências

- [WATCHDOG B3](README.md)
- [Guia de heartbeat externo](heartbeat-supervisor-externo.md)
- [Revisão dos limiares provisórios](limiares-provisorios-revisao.md)
- [Registo de controlos obrigatórios](registry/controlos-obrigatorios.json)
- [Issue #11 — Execuções desfavoráveis](https://github.com/carlos-andrade/B3/issues/11)
- [Issue #8 — Atualidade de dados](https://github.com/carlos-andrade/B3/issues/8)
- [Norma central WATCHDOG — GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/CARTA-WATCHDOG.md)

