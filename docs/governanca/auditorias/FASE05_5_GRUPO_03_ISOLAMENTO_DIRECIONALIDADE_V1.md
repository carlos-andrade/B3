# FASE05.5 — GRUPO 03 — ISOLAMENTO E DIRECIONALIDADE

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-DC8479BA1631 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | f5c5e3b215d3897c592b7d5a25a6603d97af449e7e68690fe2d8f3473d3b864d |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Data:** 2026-10-01  
**Repositório:** `carlos-andrade/B3`  
**Escopo:** auditoria semântica dos workflows pelo Layout Mestre Canônico B3 V1

## Resultado

O Grupo 03 é **VALIDADO** após correções no auditor e reexecução integral da matriz.

### Evidências

- Run #47 da auditoria: `36900015617`
- Commit auditado: `df2ff4adcda604b971cca98175885cd1a9837afc`
- Workflows auditados: **109**
- `DIRECTIONAL_INPUT_SIGNAL`: **0 falhas**
- `NO_POSTERIOR_PHASE_TRIGGER`: **0 falhas**
- divergências **CRÍTICAS**: **0**
- divergências **ALTAS**: **0**

## Correções que sustentaram a validação

1. Correção da captura de fases de dois dígitos no auditor.
2. Correção da distinção entre evidência de fase e trigger de workflow posterior.
3. Correção da extração do bloco `push`.
4. Correção das regexes YAML do auditor.
5. Correção do reconhecimento de permissões no nível de job e sintaxe inline.
6. Correção do workflow `classificar-bvbg028.yml` para sincronizar `main` antes da publicação.

## Interpretação

A ausência de falhas em `DIRECTIONAL_INPUT_SIGNAL` e `NO_POSTERIOR_PHASE_TRIGGER` demonstra conformidade estrutural da matriz auditada com as regras de isolamento e dependência direcional.

As observações restantes não bloqueadoras são:

- `STEP_SUMMARY`: 84
- `DECISION_SIGNAL`: 61
- `IDEMPOTENCE_SIGNAL`: 3
- `PERMISSIONS_MINIMAL`: 1
- `EVIDENCE_PERSISTENCE_SIGNAL`: 1

Essas observações não invalidam o Grupo 03.

## Regra de não reabertura

A certificação não autoriza reexecução ou alteração de fases históricas. Correções futuras devem ocorrer na origem e gerar nova evidência antes de qualquer promoção.

## Decisão

**GRUPO 03 — VALIDADO.**

Próxima frente: **GRUPO 04 — PERMISSÕES**.
