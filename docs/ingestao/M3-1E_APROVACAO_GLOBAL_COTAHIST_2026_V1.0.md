# M3-1E — APROVAÇÃO GLOBAL COTAHIST NORMALIZED 2026

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
