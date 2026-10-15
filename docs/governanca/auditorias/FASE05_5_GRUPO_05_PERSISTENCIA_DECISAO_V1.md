# FASE 05.5 — GRUPO 05 — PERSISTÊNCIA E DECISÃO

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-ADE295934AF9 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 50cebfbdda73397a0e27d39b6ace926ea022f2e9a464d4605cae7afd41c33940 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Data:** 2026-10-01  
**Run auditor:** #49 — `36908738096`  
**Commit auditado:** `e81bdce77ffa32e69bd0c5109927436b54d4abe4`

## Resultado

**GRUPO 05 — VALIDADO**

- Workflows auditados: **109**
- CONFORME: **23**
- CONFORME_COM_OBSERVACAO: **86**
- DIVERGENTE_CRITICA: **0**
- severidade ALTA: **0**
- DECISION_SIGNAL: **15 observações**
- EVIDENCE_PERSISTENCE_SIGNAL: **1 observação histórica**
- IDEMPOTENCE_SIGNAL: **3 observações**
- STEP_SUMMARY: **84 observações**

## Correção do auditor

O auditor foi corrigido no commit `e81bdce77ffa32e69bd0c5109927436b54d4abe4` para reconhecer mecanismos adicionais de fail-closed e resultados do GitHub Actions.

Comparação do detector:

- antes: **28** ocorrências de DECISION_SIGNAL;
- depois: **15**;
- redução: **13** ocorrências classificadas anteriormente por falso negativo do detector.

Nenhum workflow histórico foi alterado apenas para satisfazer o detector.

## Exceção histórica

A ocorrência de EVIDENCE_PERSISTENCE_SIGNAL permanece em:

`.github/workflows/cotahist-fase00-governanca-1994-v1.yml`

Ela permanece formalmente excepcional porque a cadeia histórica de 1994 está fechada e certificada. Não haverá reabertura retroativa.

## Interpretação das observações

A ausência de um padrão estático reconhecido pelo auditor não constitui, isoladamente, falha funcional. As 15 ocorrências restantes exigem apenas classificação/observabilidade e não apresentam bloqueador crítico ou alto.

A ausência de GITHUB_STEP_SUMMARY também permanece classificada como observabilidade, conforme o Layout Mestre.

## Decisão de promoção

O Grupo 05 está promovido porque:

1. a auditoria executou com sucesso;
2. não existem divergências críticas;
3. não existem divergências de severidade alta;
4. a persistência histórica excepcional está formalizada;
5. a correção foi feita na origem do auditor;
6. o resultado foi produzido por execução real do GitHub Actions;
7. não houve reexecução retroativa de fases históricas.

**Próximo grupo: GRUPO 06 — IDEMPOTÊNCIA.**
