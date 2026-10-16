# M3-1E — APROVAÇÃO GLOBAL COTAHIST NORMALIZED 2026

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-E00FFCD166B6 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | APROVADO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | b02d289ffde23f8957dfea7a4c15aa7b89afa04055b66544271fc9aba68684aa |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Proprietário do repositório — aprovação expressa registada em 2026-10-16 |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Data:** 2026-09-28  
**Status:** CONCLUÍDO — APROVAÇÃO GLOBAL CONCLUÍDA  
**Workflow:** `.github/workflows/cotahist-m3-1e-aprovacao-global.yml`  
**Run:** 36429403166  
**Job:** 108951402371  
**Commit avaliado:** c890e5dcdc96041199fe255b37165b73df1bad58

## 1. Resultado

O gate M3-1E foi executado automaticamente por `push` e terminou com:

`M3-1E_STATUS=APROVACAO_GLOBAL_CONCLUIDA`

Conclusão do run: `success`.

## 2. Evidências

- cadeia criptográfica: **OK**
- RAW SHA-256: `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`
- NORMALIZED SHA-256: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- parser: `1.1.0`
- armazenamento: Git LFS
- Dataset Oficial: `OFICIAL`
- canonical: `true`
- registros NORMALIZED: `2.919.760`
- primeira data: `2026-01-02`
- última data: `2026-09-23`
- conteúdo semântico: validado
- integridade entre RAW, NORMALIZED, checksum, quality manifest e Dataset Oficial: validada.

## 3. Regra de liberação

A aprovação M3-1E libera tecnicamente o modelo de armazenamento NORMALIZED anual para a fase histórica, mas **não libera automaticamente qualquer arquivo histórico já existente no repositório**.

Cada ano histórico deverá passar por:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY → RECONCILE`

## 4. Anomalia detectada

O checkout com LFS registrou:

`Encountered 1 file that should have been a pointer, but wasn't: dados/cotahist/normalized/anual/COTAHIST_A1987.csv`

Isso não invalidou o gate M3-1E porque o workflow valida formalmente o Dataset Oficial 2026. Porém, o arquivo 1987 existente **não pode ser considerado NORMALIZED histórico oficialmente aprovado** sem auditoria específica.

Estado:

- 2026: **OFICIAL / APROVADO**.
- 1987 existente: **NÃO CERTIFICADO POR ESTE GATE**.
- nenhum ano histórico é promovido automaticamente a Dataset Oficial.

## 5. Próxima fase — 1986

A auditoria histórica inicial deve preservar a regra do projeto de reconciliar 1986 antes de liberar 1987, incluindo:

1. `tpmerc`;
2. `codbdi`;
3. chave lógica correta;
4. 30 casos de OHLC;
5. volume e quantidade;
6. calendário de pregão;
7. comparação de amostras com RAW;
8. SHA-256;
9. reconstrução determinística;
10. persistência conforme Git LFS;
11. certificação;
12. reconciliação.

**Não liberar 1987 enquanto a reconciliação semântica de 1986 não estiver concluída.**


## 6. Reaprovação global e publicação — 2026-10-16

Esta secção prevalece sobre os números e resultados de 2026-09-28 acima, que permanecem preservados como histórico.

- Workflow: `.github/workflows/cotahist-m3-1e-aprovacao-global.yml`
- Run final: [38885204284](https://github.com/carlos-andrade/B3/actions/runs/38885204284)
- Resultado: `success`; `M3-1E_STATUS=APROVACAO_GLOBAL_CONCLUIDA`
- Commit de publicação: [a28437a81af29be36b6cf4569dc9f232539cd3bc](https://github.com/carlos-andrade/B3/commit/a28437a81af29be36b6cf4569dc9f232539cd3bc)
- RAW SHA-256: `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e`
- NORMALIZED SHA-256: `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`
- Parser: `1.1.2`; armazenamento: Git LFS.
- Registos: 3.142.910; campos: 25; intervalo: 2026-01-02 a 2026-10-13.
- Cadeia criptográfica, validação semântica, materialização física e coerência entre CSV, checksum, manifesto de qualidade e Dataset Oficial aprovadas.

### Resultado consolidado dos gates

| Gate | Run | Resultado |
|---|---:|---|
| M3-1C — CI de integridade e reprodutibilidade | [38884804282](https://github.com/carlos-andrade/B3/actions/runs/38884804282) | APROVADO |
| M3-1D — Dataset Oficial | [38885204516](https://github.com/carlos-andrade/B3/actions/runs/38885204516) | APROVADO |
| M3-1E — Aprovação global | [38885204284](https://github.com/carlos-andrade/B3/actions/runs/38885204284) | APROVADO |
| Dataset Oficial V2 — publicação do catálogo | [38885204334](https://github.com/carlos-andrade/B3/actions/runs/38885204334) | SUCCESS |

**Decisão:** NORMALIZED V2.0 adotado para os anos certificados; COTAHIST 2026 aprovado e publicado. A aprovação não certifica automaticamente os anos históricos 1986–2025: cada ano continua sujeito à sequência RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY → RECONCILE.
