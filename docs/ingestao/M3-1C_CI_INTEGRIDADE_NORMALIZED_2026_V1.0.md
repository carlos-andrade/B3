# M3-1C — CI de integridade NORMALIZED COTAHIST 2026

**Caminho:** docs/ingestao/M3-1C_CI_INTEGRIDADE_NORMALIZED_2026_V1.0.md  
**Status:** CONCLUÍDO — CI_INTEGRIDADE_APROVADA

## Objetivo

Transformar a prova física M3-1B em um gate CI repetível e fail-closed para o NORMALIZED 2026.

## Verificações executadas

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

## Execução oficial

- Workflow: `.github/workflows/cotahist-m3-1c-ci-normalized-2026.yml`
- Run: `36428513803`
- Run number: `1`
- Job: `validate`
- Job ID: `108948384728`
- Commit avaliado: `a06d7b9dd55525210cfa2ae878b29dcfbbf025bb`
- Evento: `push`
- Início: `2026-09-28T13:25:31Z`
- Conclusão: `2026-09-28T13:28:35Z`
- Resultado GitHub Actions: `success`

## Evidências principais

- Registros tipo 01: **2.919.760**
- Primeira data: **2026-01-02**
- Última data: **2026-09-23**
- Campos: **25**
- SHA NORMALIZED: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- Reconstrução: `M3-1C_REPRODUCIBILIDADE=OK`
- SHA reconstruído = SHA persistido.
- Contagem/datas: `ROWS=2919760 FIRST=2026-01-02 LAST=2026-09-23`
- Certificação final: `M3-1C_STATUS=CI_INTEGRIDADE_APROVADA`

## Critério

Qualquer divergência interrompe o workflow. A execução oficial concluiu com sucesso e todas as verificações previstas foram aprovadas.

## Estado

**M3-1C CONCLUÍDO E APROVADO.**

O gate CI passa a constituir evidência operacional repetível da integridade do NORMALIZED 2026.

A migração histórica permanece bloqueada até M3-1E.

## Próxima fase

Liberar formalmente **M3-1D — Dataset Oficial 2026**, mantendo 1986–2025 bloqueado até a conclusão dos gates subsequentes.
