# COTAHIST — Contrato de Execução Sequencial das Fases

**Versão:** 1.0.0  
**Data:** 2026-10-01  
**Aplicação inicial:** cadeia 1994 FASE06→FASE12

## Regra

Nenhuma fase posterior pode ser liberada apenas porque o arquivo existe. A fase anterior deve possuir evidência válida e status permitido pelo gate.

### Sequência obrigatória

1. FASE00 — Governança / pré-condições
2. FASE01 — Aquisição RAW
3. FASE02 — Integridade da fonte
4. FASE03–05 — Parsing, normalização e manifesto
5. FASE06 — Reconciliação RAW × NORMALIZED
6. FASE07 — Identidade / chaves
7. FASE08 — Semântica / calendário
8. GATE 06–08
9. FASE09 — Pré-release
10. FASE10 — Integridade do release
11. FASE11 — Certificação
12. FASE12 — Fechamento / transição
13. Somente após FASE12 concluída: próximo ano

## Condições de passagem

- FASE06, FASE07 e FASE08 devem estar em 'VALIDADO' ou 'VALIDADO_COM_EXCECAO'.
- FASE09 deve resultar em 'LIBERADO_PARA_FASE10'.
- FASE10 deve resultar em 'VALIDADO'.
- FASE11 só pode certificar após FASE10.
- FASE12 só pode fechar após FASE11.
- Falha em qualquer gate interrompe a cadeia.

## Contrato de correção

'correction_applied' não é uma condição de sucesso por si só.

Quando não houver correção de dados necessária:
- 'correction_required=false';
- 'correction_applied=false';
- 'correction_contract_valid=true'.

Quando houver correção necessária:
- a correção deve ser explicitamente registrada;
- sua evidência deve ser persistida;
- somente então 'correction_contract_valid' poderá ser verdadeiro.

É proibido transformar 'correction_applied' em 'true' artificialmente para satisfazer um gate.

## Fail-closed

A cadeia não deve avançar por inferência, existência de arquivo, execução parcial ou resultado de fase posterior.

O princípio é:

**pré-condição válida → execução → evidência → gate → próxima fase.**

## Aplicação no workflow

Workflow:

`.github/workflows/cotahist-cadeia-1994-06-12-v1.yml`

O workflow contém um gate explícito entre FASE06–08 e FASE09–12. A cadeia FASE09–12 mantém dependência lógica progressiva:

**FASE09 → FASE10 → FASE11 → FASE12.**
