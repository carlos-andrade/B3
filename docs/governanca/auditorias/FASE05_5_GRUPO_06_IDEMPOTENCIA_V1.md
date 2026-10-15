# FASE 05.5 — GRUPO 06 — IDEMPOTÊNCIA

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-58BAD3F6339C |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 31b9e6a8606bb69853a99a0d0fdcbb47046d0a88015d2efbe43ec30487a34e87 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Data:** 2026-10-01  
**Run auditor:** #52 — `36909698465`  
**Commit auditado:** `d8d0cccce9d8f7d8ab7f325b8cc72380f8d24cc6`

## Resultado

**GRUPO 06 — VALIDADO COM EXCEÇÃO HISTÓRICA FORMAL**

- Workflows auditados: **109**
- CONFORME: **25**
- CONFORME_COM_OBSERVACAO: **84**
- DIVERGENTE_CRITICA: **0**
- IDEMPOTENCE_SIGNAL sem padrão: **1**
- Bloqueadores críticos: **0**
- Bloqueadores altos: **0**

## Correção funcional

`.github/workflows/validar-bvbg02802.yml` foi corrigido no commit `416be26850a5c58023ae5f4329da606ec241e939`.

A publicação agora verifica alterações staged antes de criar commit e sincroniza com `origin/main` antes do push quando necessário.

O auditor foi ampliado para reconhecer `Sem alterações` no commit `b1be5dc1ff0447bad55d874e2fe2ad4e2df87f66`.

## Exceção histórica

A única ocorrência sem padrão estático de idempotência é:

`.github/workflows/cotahist-fase00-governanca-1994-v1.yml`

A FASE00/1994 pertence a uma cadeia histórica já encerrada e certificada. O workflow valida artefatos existentes e não publica dados. A ausência de deduplicação explícita não constitui risco operacional de duplicação neste contexto.

Não haverá alteração retroativa nem reabertura da cadeia de 1994.

## Conclusão

O Grupo 06 está **VALIDADO**, com uma exceção histórica formal.

Critérios atendidos: nenhuma divergência crítica/alta; risco funcional BVBG.028.02 corrigido; auditor corrigido; execução real concluída com sucesso; cadeia histórica preservada.

**Próximo grupo: CASOS ESPECIAIS.**
