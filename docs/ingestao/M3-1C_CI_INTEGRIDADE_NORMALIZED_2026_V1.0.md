# M3-1C — CI de integridade NORMALIZED COTAHIST 2026

**Caminho:** docs/ingestao/M3-1C_CI_INTEGRIDADE_NORMALIZED_2026_V1.0.md  
**Status:** IMPLEMENTADO — EXECUÇÃO PENDENTE

## Objetivo

Transformar a prova física M3-1B em um gate CI repetível e fail-closed para o NORMALIZED 2026.

## Verificações

1. RAW, NORMALIZED e manifests presentes.
2. Arquivo NORMALIZED materializado fisicamente via Git LFS.
3. Tracking LFS confirmado.
4. Arquivo não pode ser apenas ponteiro.
5. SHA físico = checksum registrado.
6. SHA físico = SHA do manifest.
7. RAW SHA do manifest = RAW atualmente persistido.
8. Validação semântica com `validar_normalized.py`.
9. Reconstrução determinística RAW → NORMALIZED.
10. SHA e tamanho da reconstrução = objeto persistido.
11. Contagem de linhas e 25 campos = manifest.
12. Primeira e última data = manifest.
13. Status final explícito: `M3-1C_STATUS=CI_INTEGRIDADE_APROVADA`.

## Workflow

`.github/workflows/cotahist-m3-1c-ci-normalized-2026.yml`

Trigger: `workflow_dispatch` e alterações relevantes em `main`.

O workflow possui `permissions: contents: read` e não altera dados.

## Critério

Qualquer divergência interrompe o workflow.

A aprovação M3-1C somente será declarada pelo próprio workflow após todas as verificações.

## Estado

M3-1C foi implementado em 2026-09-28. A execução deve ser verificada antes de liberar M3-1D.

A migração histórica permanece bloqueada até M3-1E.
