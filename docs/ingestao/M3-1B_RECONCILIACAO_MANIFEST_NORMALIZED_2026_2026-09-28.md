# M3-1B — Reconciliação do manifest NORMALIZED 2026

**Arquivo:** M3-1B_RECONCILIACAO_MANIFEST_NORMALIZED_2026_2026-09-28.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/M3-1B_RECONCILIACAO_MANIFEST_NORMALIZED_2026_2026-09-28.md  
**Data:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** INVESTIGAÇÃO CONCLUÍDA — CORREÇÃO CONTROLADA EM EXECUÇÃO

## 1. Objetivo

Investigar a divergência entre o manifest NORMALIZED 2026 e a reconstrução determinística executada no M3-1B, antes da liberação do gate M3-1C.

## 2. Evidência histórica

O manifest foi criado no commit `ccea173449b70c1f2b95a787a04c2020b06fe1f7`, em 2026-09-23 15:28 UTC, com:

- RAW SHA-256: `e40dc0cdb5ad6315296d88cdb5654240f15412be6fc13e3d47bc8606f9132fee`
- NORMALIZED SHA-256: `d97514f3224da3b70b5b890911c7383e86a6d69ffc5482eb610826d729b2a1fa`
- registros: 2.904.013
- primeira data: 2026-01-02
- última data: 2026-09-22

## 3. Mudança posterior do RAW

O commit `e4598cdcdca6a955b4208109fe2fea5f8699fb4b`, em 2026-09-24 07:52 UTC, atualizou o COTAHIST_A2026.ZIP e seu checksum:

- RAW anterior: `e40dc0...`
- RAW posterior: `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`

O commit também atualizou `dados/cotahist/manifests/COTAHIST_A2026.json` e `dados/cotahist/checksums/COTAHIST_A2026.ZIP.sha256`.

Portanto, existe evidência objetiva de que o RAW mudou depois da criação do manifest NORMALIZED.

## 4. Reconstrução posterior

No M3-1B, usando o RAW atualmente presente no repositório e o parser `1.1.0`, a reconstrução produziu:

- registros tipo 01: 2.919.760
- primeira data: 2026-01-02
- última data: 2026-09-23
- tamanho: 392.044.266 bytes
- NORMALIZED SHA-256: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`

O NORMALIZED persistido em Git LFS possui exatamente esse OID e tamanho.

## 5. Conclusão causal

A divergência não é, neste momento, evidência de erro do parser.

A evidência de histórico indica:

`RAW versão 23/09` → manifest NORMALIZED `d97514...`

e posteriormente:

`RAW atualizado em 24/09` → reconstrução NORMALIZED `befcf243...`

Logo, o manifest NORMALIZED 2026 ficou **defasado em relação ao RAW posteriormente atualizado**.

O ponto que permanece obrigatório antes da aprovação é recalcular de forma controlada todos os metadados dependentes do RAW atual, incluindo a contagem de duplicidades da chave candidata, e então atualizar o manifest somente com essa evidência.

## 6. Correção

A correção será executada por workflow dedicado, em modo fail-closed:

1. calcular SHA-256 do RAW atual;
2. normalizar novamente com parser `1.1.0`;
3. calcular SHA, tamanho, registros e datas;
4. verificar correspondência com o NORMALIZED LFS persistido;
5. recalcular duplicidades da chave candidata;
6. gerar o manifest corrigido;
7. registrar a divergência anterior e a correção;
8. persistir o manifest somente após todas as verificações;
9. não alterar o RAW.

## 7. Gate

Até a conclusão desse workflow:

- M3-1B armazenamento físico: **APROVADO**
- Reconciliação do manifest: **PENDENTE**
- M3-1C: **BLOQUEADO**
- Migração histórica 1986–2025: **BLOQUEADA**

**Regra:** nenhum dado histórico adicional será migrado enquanto a cadeia RAW → NORMALIZED → manifest 2026 não estiver reconciliada.
