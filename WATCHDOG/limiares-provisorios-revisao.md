# Revisão e aprovação dos limiares de atualidade — WATCHDOG B3

**Estado:** para revisão do proprietário; nenhum limiar fica aprovado por este documento.  
**Data de preparação:** 2026-10-13  
**Fonte de configuração:** `WATCHDOG/registry/datasets-monitorizados.json`  
**Regra de integridade:** a idade é calculada a partir da data de observação do dataset, nunca da data de ingestão.

## Matriz de decisão

| Controlo | Campo/data observada | Limiar atual | Estado | Pergunta obrigatória ao proprietário |
|---|---|---:|---|---|
| BCB-SGS-432 | `ultima_data` na série SGS 432 | 3 dias de calendário | PROVISIONAL | A série deve ser atualizada diariamente? Qual atraso máximo tolerável, incluindo fins de semana e feriados? |
| BCB-SGS-11 | `ultima_data` na série SGS 11 | 5 dias de calendário | PROVISIONAL | O limite cobre a periodicidade real da série e feriados sem esconder atrasos operacionais? |
| BCB-SGS-12 | `ultima_data` na série SGS 12 | 5 dias de calendário | PROVISIONAL | O limite cobre a periodicidade real da série e feriados sem esconder atrasos operacionais? |
| BCB-SGS-1 | `ultima_data` na série SGS 1 | 5 dias de calendário | PROVISIONAL | O limite cobre a periodicidade real da série e feriados sem esconder atrasos operacionais? |
| BCB-SGS-433 (IPCA) | `ultima_data` na série SGS 433 | 45 dias de calendário | PROVISIONAL | A periodicidade de divulgação do IPCA justifica 45 dias? Qual regra de atraso após divulgação deve gerar alerta? |
| B3-BDI-DAILY-AVERAGE-STOCKS | Data do manifesto `date` | 5 dias de calendário | PROVISIONAL | A publicação tem cadência diária de dias úteis? Como tratar feriados, fins de semana e atrasos da fonte? |
| COTAHIST-2026 | `ultima_data_observacao` no manifesto anual | 30 dias de calendário | PROVISIONAL | O snapshot anual é apenas uma referência de cobertura? Confirmar que a atualidade operacional é avaliada pelo controlo diário separado. |
| COTAHIST-DIARIO | `ultima_data` nos manifestos diários normalizados | 5 dias de calendário | PROVISIONAL | A regra deve usar dias de calendário ou dias de pregão? Definir o comportamento esperado em feriados e suspensões de publicação. |

## Orientações para a decisão

1. **Não aprovar apenas porque a execução passou.** O resultado `8 PASS, 0 STALE, 0 UNKNOWN` comprova que os valores observados ficaram dentro dos limites configurados naquela execução; não comprova que os limites de negócio são adequados.
2. **Distinguir calendário e periodicidade.** Para séries diárias, definir como tratar fins de semana, feriados e atraso da própria fonte. Para séries mensais, definir uma regra ligada à data esperada de divulgação, se necessário.
3. **Definir o significado do alerta.** O limiar deve representar o máximo atraso aceitável para a finalidade do projeto, não apenas um número conveniente para evitar alertas.
4. **Manter datas de observação e ingestão separadas.** A ingestão recente de dados antigos não deve converter um dataset em `PASS`.
5. **Registar a aprovação por controlo.** Preencher a tabela abaixo apenas após decisão explícita do proprietário responsável.

## Registo de aprovação

| Controlo | Decisão (APROVAR / ALTERAR) | Limiar aprovado | Proprietário | Data UTC | Justificação / evidência |
|---|---|---:|---|---|---|
| BCB-SGS-432 | PENDENTE | — | PENDENTE | — | — |
| BCB-SGS-11 | PENDENTE | — | PENDENTE | — | — |
| BCB-SGS-12 | PENDENTE | — | PENDENTE | — | — |
| BCB-SGS-1 | PENDENTE | — | PENDENTE | — | — |
| BCB-SGS-433 | PENDENTE | — | PENDENTE | — | — |
| B3-BDI-DAILY-AVERAGE-STOCKS | PENDENTE | — | PENDENTE | — | — |
| COTAHIST-2026 | PENDENTE | — | PENDENTE | — | — |
| COTAHIST-DIARIO | PENDENTE | — | PENDENTE | — | — |

## Critério de conclusão

A revisão só fica concluída quando cada linha tem decisão, limiar aprovado, proprietário, data e justificação. Após a aprovação, atualizar `datasets-monitorizados.json`, remover `threshold_status: PROVISIONAL` apenas dos controlos aprovados, executar o workflow de validação e uma nova avaliação de atualidade, e anexar as evidências ao registo central GOVERNANCA.

**Estado atual: revisão preparada; aprovação humana pendente.**
