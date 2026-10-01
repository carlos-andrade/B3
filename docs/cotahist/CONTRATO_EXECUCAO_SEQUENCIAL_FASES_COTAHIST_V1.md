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

## REGRA ESTRUTURAL — ISOLAMENTO, MONOTONICIDADE E IMUTABILIDADE DAS FASES — 2026-10-01

As fases do COTAHIST são **monotônicas e isoladas**.

### Regra 1 — uma fase não retorna para fase anterior
Uma fase N não pode reabrir, recalcular, substituir, corrigir ou alterar a evidência normativa da fase N-1 ou de qualquer fase anterior. Se uma inconsistência anterior for descoberta, ela deve ser tratada como **incidente de governança/correção versionada da própria fase afetada**, sem transformar a fase posterior em responsável por ela.

### Regra 2 — uma fase não executa responsabilidade de fase posterior
Uma fase N não pode antecipar critérios pertencentes à fase N+1. Em especial:
- FASE06 não decide unicidade/cardinalidade de chave;
- FASE07 não reescreve a semântica certificada da FASE06;
- FASE08 não redefine identidade da FASE07;
- FASE09–12 não substituem os gates técnicos anteriores.

### Regra 3 — correção permanece na fase de origem
Se uma regra da FASE06 estiver errada, corrige-se a FASE06. Não se cria uma correção da FASE07 para mascarar a FASE06. Se uma regra da FASE07 estiver errada, corrige-se a FASE07.

### Regra 4 — dependência é somente leitura
Uma fase posterior pode **consumir** a evidência autorizada da fase anterior e os dados-fonte necessários à sua própria análise, mas não pode alterá-los nem reinterpretar silenciosamente o estado certificado da fase anterior.

### Regra 5 — promoção é unidirecional
O fluxo é exclusivamente:

**N-1 → N → N+1**

Não existe fluxo operacional **N+1 → N-1** nem **N → N+1 com responsabilidade de N+1 executada dentro de N**.

### Regra 6 — novo teste não retrocertifica
Uma fase posterior pode detectar um incidente com impacto potencial em fase anterior. Isso gera um **registro de impacto e revisão controlada**, não uma reexecução silenciosa nem uma alteração retroativa da evidência histórica.

### Regra 7 — gatilhos não podem quebrar a monotonicidade
Workflows de uma fase concluída não devem ser disparados por alterações genéricas de documentação, README ou artefatos de fases posteriores. O gatilho deve refletir somente a própria fase e suas entradas autorizadas.

### Matriz de responsabilidade

| Fase | Responsabilidade própria | Não pode assumir |
|---|---|---|
| 00 | governança/pré-condições | validação técnica posterior |
| 01 | aquisição/RAW | integridade semântica |
| 02 | integridade da fonte | parsing/normalização |
| 03 | parsing | normalização/identidade |
| 04 | normalização | identidade/semântica posterior |
| 05 | manifesto/checksum | semântica/chaves |
| 06 | semântica/invariantes | identidade/cardinalidade FASE07 |
| 07 | identidade/chaves/cardinalidade | reescrever FASE06 |
| 08 | semântica/calendário/consistência | reabrir identidade |
| 09 | pré-release | corrigir fases anteriores |
| 10 | validação independente | substituir evidências anteriores |
| 11 | certificação/promoção | refazer fases técnicas silenciosamente |
| 12 | fechamento/transição | certificar o próximo ano |

**Regra de governança:** descobrir algo numa fase posterior não autoriza essa fase a executar o trabalho de uma fase anterior.

