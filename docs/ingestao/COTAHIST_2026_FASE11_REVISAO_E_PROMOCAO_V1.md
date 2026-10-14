# COTAHIST 2026 — FASE10 e FASE11

## FASE10 — resultado verificado

Relatório: [FASE10](../../dados/cotahist/quality/COTAHIST_2026_FASE10_VALIDACAO_CANDIDATO_V1.json)

- Estado: VALIDADO_COM_DIFERENCAS_A_REVISAR.
- RAW candidato SHA-256: 580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e.
- NORMALIZED candidato SHA-256: e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc.
- Registos anteriores: 2.919.760.
- Registos candidatos: 3.142.910.
- Ocorrências antigas ausentes: 0.
- Ocorrências adicionais: 223.150.
- Datas: 2026-01-02 a 2026-10-13.
- Reconciliação RAW/NORMALIZED: 25 campos, sem divergências.
- Deduplicação: não realizada.

A comparação indica inclusão integral das ocorrências antigas e adição de novas ocorrências. A FASE10 não alterou os dados canónicos.

## FASE11 — promoção controlada

Workflow: [cotahist-fase11-promocao-controlada-2026-v1.yml](../../.github/workflows/cotahist-fase11-promocao-controlada-2026-v1.yml)

O workflow foi publicado para descarregar novamente a fonte, repetir a reconciliação, verificar que nenhuma ocorrência antiga desapareceu e só então atualizar RAW, NORMALIZED, manifestos e checksums.

**Estado de execução:** não confirmado nesta auditoria. O ficheiro do workflow e o seu commit não comprovam que a execução terminou.

Evidência esperada: `dados/cotahist/quality/COTAHIST_2026_FASE11_PROMOCAO_V1.json`.

Após confirmação da promoção, executar novamente as FASES 04–08 e o gate 06–08. Evidências antigas não certificam novos hashes.
