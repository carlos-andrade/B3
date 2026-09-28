# M3-1B — Resultado da prova física Git LFS NORMALIZED 2026

**Arquivo:** M3-1B_RESULTADO_PROVA_LFS_2026_2026-09-28.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/M3-1B_RESULTADO_PROVA_LFS_2026_2026-09-28.md  
**Data:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** CONCLUÍDO — PROVA FÍSICA LFS APROVADA

## 1. Execução

- Workflow: `COTAHIST - M3-1B prova física Git LFS NORMALIZED 2026`
- Run: `36419262539`
- Job: `108917764369`
- Run number: `3`
- Evento: `push`
- Commit de origem: `819546fb310b085f13a4fbb777cd58fabf280736`
- Conclusão: `success`
- Início: `2026-09-28T12:02:16Z`
- Conclusão: `2026-09-28T12:05:05Z`

## 2. NORMALIZED gerado

- Parser: `1.1.0`
- Registros tipo 01: **2.919.760**
- Primeira data encontrada: **2026-01-02**
- Última data encontrada: **2026-09-23**
- Tamanho: **392.044.266 bytes**
- SHA-256:
  `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`

## 3. Validação pré-persistência

A etapa `Validar NORMALIZED antes da persistência` foi concluída com sucesso.

A cadeia utilizada foi:

`RAW_SHA → NORMALIZED_SHA → validar_normalized.py → persistência`

Nenhuma falha foi registrada na etapa de validação.

## 4. Persistência LFS

O arquivo canônico foi criado em:

`dados/cotahist/normalized/anual/COTAHIST_A2026.csv`

O tracking confirmado foi:

- filter: `lfs`
- diff: `lfs`
- merge: `lfs`

O objeto GitHub ficou representado pelo ponteiro LFS:

- OID: `sha256:befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- size: **392.044.266 bytes**

Commit de persistência:

`dcb7dd16649245d0ac3e9f58a1bca521941e7fb1`

Mensagem:

`data(cotahist): persistir NORMALIZED 2026 via Git LFS`

## 5. Prova física

Após o push, o workflow executou:

- `git lfs ls-files --long`
- `git lfs pull`
- existência física do CSV
- SHA-256 do arquivo materializado
- comparação do tamanho físico com o arquivo gerado em /tmp

Resultado:

`befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9 * dados/cotahist/normalized/anual/COTAHIST_A2026.csv`

Resultado SHA:

**OK**

Resultado final do workflow:

`M3-1B_STATUS=PROVA_LFS_FISICA_CONCLUIDA`

Tamanho físico:

**392.044.266 bytes**

## 6. Concorrência de automações

Durante a execução, o README automático avançou `main` de:

`819546f`

para:

`9151202`

A proteção implementada no M3-1B executou:

`git fetch → git rebase origin/main → git push`

e concluiu com:

`PUSH_STATUS=SUCESSO`

Portanto, a correção de concorrência foi efetivamente exercitada e validada.

## 7. Integridade do RAW

A prova não altera o RAW.

O RAW utilizado continua sendo:

`dados/cotahist/raw/anual/COTAHIST_A2026.ZIP`

SHA registrado no manifest:

`e40dc0cdb5ad6315296d88cdb5654240f15412be6fc13e3d47bc8606f9132fee`

## 8. Divergência encontrada para reconciliação

Existe uma divergência documental que **não deve ser ocultada nem corrigida silenciosamente**.

O manifest atual registra:

- `ultima_data = 2026-09-22`
- `normalized_sha256 = d97514f...`

Entretanto, a reconstrução determinística executada no M3-1B produziu:

- última data: **2026-09-23**
- SHA-256: `befcf243...`

O workflow M3-1B comprovou a consistência física do NORMALIZED reconstruído e persistido, mas não atualizou o manifest.

Portanto:

> **M3-1B de armazenamento físico está aprovado; a reconciliação do manifest permanece pendente e deve ser tratada como gate separado antes da aprovação global M3-1.**

Não alterar o manifest apenas para fazê-lo coincidir com o novo arquivo. Primeiro deve-se determinar por que a evidência anterior do manifest diverge da reconstrução atual.

## 9. Estado M3

- M3-0: **CONCLUÍDO — GIT_STANDARD_LIMIT**
- M3-1A: **CONCLUÍDO**
- M3-1B: **CONCLUÍDO — PROVA FÍSICA LFS**
- Reconciliação manifest × NORMALIZED: **PENDENTE**
- M3-1C: **BLOQUEADO ATÉ RECONCILIAÇÃO**
- M3 histórico 1986–2025: **BLOQUEADO**
- RAW: **PRESERVADO**

## 10. Próximo gate

Antes de iniciar M3-1C, executar:

1. investigar a origem da diferença `2026-09-22` × `2026-09-23`;
2. reconciliar manifest, RAW e NORMALIZED;
3. somente após evidência suficiente, atualizar o manifest se necessário;
4. registrar novo SHA e justificativa;
5. executar M3-1C;
6. calcular posteriormente o volume agregado necessário para 1986–2026;
7. manter a migração histórica bloqueada até M3-1E.

**Conclusão:** a infraestrutura Git LFS foi comprovada fisicamente para o NORMALIZED 2026 com integridade SHA-256 e materialização física confirmadas. A aprovação global de M3-1 ainda não foi concedida.
