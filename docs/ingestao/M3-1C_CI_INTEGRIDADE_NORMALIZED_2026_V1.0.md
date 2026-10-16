# M3-1C — CI de integridade NORMALIZED COTAHIST 2026

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-B9ACCD709A94 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | APROVADO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 2c3f054ccd9b48ef3bc7fe8605669a93647f64ffc0cf0996878c75681b27d9ea |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Proprietário do repositório — aprovação expressa registada em 2026-10-16 |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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


## 11. Revalidação operacional — 2026-10-16

A revalidação atual substitui os valores históricos de setembro de 2026 para o Dataset Oficial 2026.

- Workflow: `.github/workflows/cotahist-m3-1c-ci-normalized-2026.yml`
- Run: [38884804282](https://github.com/carlos-andrade/B3/actions/runs/38884804282)
- Resultado: `success`; `M3-1C_STATUS=CI_INTEGRIDADE_APROVADA`
- RAW SHA-256: `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e`
- NORMALIZED SHA-256: `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`
- Parser: `1.1.2`
- Registos: 3.142.910; campos: 25; intervalo: 2026-01-02 a 2026-10-13.
- Reconstrução determinística RAW → NORMALIZED: aprovada; SHA e tamanho coincidem.
- A contagem e as datas usam mínimo/máximo calendárico, não a primeira/última linha física do CSV, porque a ordem de origem não é cronológica.

**Decisão:** M3-1C APROVADO para a versão atual do NORMALIZED 2026.
