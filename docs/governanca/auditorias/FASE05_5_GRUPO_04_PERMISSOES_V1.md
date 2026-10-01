# FASE05.5 — GRUPO 04 — PERMISSÕES

**Data:** 2026-10-01  
**Repositório:** `carlos-andrade/B3`  
**Escopo:** compatibilidade entre permissões declaradas e operação efetiva dos workflows.

## Resultado

**VALIDADO COM EXCEÇÃO HISTÓRICA FORMAL.**

A matriz auditada contém 109 workflows e não apresenta divergências críticas ou altas de permissão.

### Evidência

- Auditoria: Run #47 — `36900015617`
- Commit auditado: `df2ff4adcda604b971cca98175885cd1a9837afc`
- `PERMISSIONS_MATCH_WRITE`: sem falhas críticas
- `PERMISSIONS_MINIMAL`: 1 observação

## Exceção

Workflow:

`.github/workflows/cotahist-fase00-governanca-1994-v1.yml`

O workflow declara `contents: write`, porém sua operação efetiva é somente leitura/validação dos artefatos da FASE00. O auditor classificou:

`PERMISSIONS_MINIMAL = false`

com severidade **MEDIA**.

## Tratamento

A FASE00/1994 pertence a uma cadeia histórica já fechada e certificada. Conforme o Layout Mestre Canônico, uma auditoria estrutural posterior não deve reabrir workflow histórico fechado.

Portanto:

1. nenhuma alteração retroativa foi aplicada à FASE00/1994;
2. a permissão excessiva foi registrada como exceção histórica;
3. a exceção não bloqueia a arquitetura atual;
4. eventual melhoria futura deve ser implementada somente por nova versão controlada, sem reescrever o histórico certificado.

## Decisão

**GRUPO 04 — VALIDADO COM EXCEÇÃO HISTÓRICA.**

Próxima frente: **GRUPO 05 — PERSISTÊNCIA E DECISÃO**.

## Regra de não reabertura

Esta evidência não autoriza reexecução da FASE00/1994 nem alteração de sua cadeia histórica.
