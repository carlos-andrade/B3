# CONTRATO DE RETORNO E MONITORAMENTO DE EXECUÇÕES B3 — V1

**Data:** 2026-10-01  
**Status:** VIGENTE

## 1. Objetivo

Cada workflow é uma unidade operacional independente. Sua execução deve produzir uma resposta verificável, sem depender de reexecução manual para descobrir se terminou favorável ou não.

## 2. Independência

Independência significa:

- um workflow não chama outro workflow;
- um workflow não reexecuta outro workflow;
- documentação/README não dispara fases técnicas;
- uma fase somente consome evidência anterior autorizada quando isso fizer parte de seu contrato;
- uma fase posterior nunca corrige ou executa a responsabilidade de uma fase anterior;
- correções permanecem na origem;
- o resultado persistido é a fonte de decisão, não a memória da execução.

## 3. Direcionalidade

A dependência, quando necessária, é somente de evidência e sempre para frente:

ENTRADA → EXECUÇÃO → EVIDÊNCIA → DECISÃO → PRÓXIMA FASE

Nunca:

FASE POSTERIOR → REEXECUÇÃO DA FASE ANTERIOR

## 4. Estados operacionais

Cada execução deve ser interpretada como:

- FAVORÁVEL: conclusão success ou estado explicitamente aprovado pelo contrato da tarefa;
- NÃO FAVORÁVEL: failure, cancelled, timed_out, action_required, stale ou equivalente;
- EM EXECUÇÃO: queued, in_progress, waiting, requested ou pending.

O estado do workflow não substitui o estado da evidência da fase.

## 5. Retorno obrigatório

Todo workflow operacional deve apresentar no GITHUB_STEP_SUMMARY:

1. nome do workflow;
2. fase/tarefa;
3. ano/ciclo, quando aplicável;
4. execução/run;
5. entrada utilizada;
6. evidência produzida;
7. status;
8. decisão;
9. bloqueadores;
10. exceções;
11. commit quando houver publicação;
12. próxima ação permitida;
13. indicação explícita se a execução deve ou não ser repetida.

## 6. Monitor permanente

O workflow .github/workflows/b3-monitor-execucoes-v1.yml verifica automaticamente as execuções recentes a cada 15 minutos.

Ele classifica:

- FAVORÁVEL;
- NÃO_FAVORÁVEL;
- EM_EXECUÇÃO.

O monitor não reexecuta workflows. Ele somente informa o estado, evitando que uma falha ou sucesso seja confundido com autorização para nova execução.

## 7. Retorno ao chat

O GitHub Actions não possui, por si só, um canal nativo que envie automaticamente cada resultado futuro para esta conversa.

Portanto, o projeto passa a usar o seguinte mecanismo auditável:

workflow → GITHUB_STEP_SUMMARY → monitor → leitura pelo ChatGPT → resposta no chat

Quando uma execução for verificada nesta conversa, o resultado deve ser apresentado com run, status, decisão, evidência e commit, sem reexecutar o workflow apenas para obter a resposta.

## 8. Regra anti-reexecução

Antes de executar novamente uma tarefa, verificar:

- run existente;
- conclusão;
- evidência existente;
- SHA/commit;
- decisão;
- incidentes;
- alteração real da entrada;
- correção pendente.

Se a execução existente continua válida e a entrada não mudou, NÃO executar novamente.

## 9. Agendamento

O monitor roda continuamente a cada 15 minutos.

O README possui agendamento separado para 23:55 America/Sao_Paulo, equivalente a 02:55 UTC neste regime de calendário, e não constitui gatilho operacional de fases.

## 10. Princípio final

EXECUTAR UMA VEZ → REGISTRAR → VERIFICAR → DECIDIR → AVANÇAR.

Não:

EXECUTAR → PERDER O RESULTADO → EXECUTAR NOVAMENTE PARA DESCOBRIR O RESULTADO.


---

## FONTE NORMATIVA CANÔNICA — 2026-10-01

Este documento é **derivado/operacional** e não constitui fonte independente para geração de código. As regras executáveis devem ser reconciliadas com:

`docs/governanca/LAYOUT_MESTRE_CANONICO_B3_V1.md`

**Regra:** Layout Mestre → especificação da tarefa → código/workflow → evidência.

Se houver divergência, o Layout Mestre prevalece até reconciliação e versionamento formal.