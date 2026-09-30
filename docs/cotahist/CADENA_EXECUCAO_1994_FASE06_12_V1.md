# Cadeia COTAHIST 1994 — FASE06→FASE12

## Objetivo
Criar uma cadeia única, sequencial e fail-closed para provar o reconhecimento do GitHub Actions e preservar a ordem oficial das fases.

## Ordem
RUN_START → FASE06 → FASE07 → FASE08 → FASE09 → FASE10 → FASE11 → FASE12.

## Regra
Nenhuma fase posterior pode executar seu gate sem a conclusão da fase anterior. A existência de um arquivo de evidência, isoladamente, não certifica a fase: a evidência deve estar VALIDADO e o workflow oficial correspondente deve ser auditável.

## Estado inicial
FASE06 permanece pendente até existir execução comprovada e evidência publicada. FASE07–12 permanecem bloqueadas.

## Diagnóstico
O primeiro job não altera o repositório. Seu objetivo é produzir uma marca inequívoca de que o workflow foi reconhecido e iniciou. Se não houver run, job ou log RUN_START, o problema está antes da lógica de reconciliação.

## Observação
Esta cadeia não substitui as evidências oficiais individuais; ela funciona como orquestrador/gate de diagnóstico e execução sequencial.
