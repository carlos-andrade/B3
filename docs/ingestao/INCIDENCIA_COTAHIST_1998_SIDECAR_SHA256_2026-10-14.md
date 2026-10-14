# INCIDÊNCIA CONTROLADA — COTAHIST 1998: DIVERGÊNCIA DE SIDECAR SHA-256

**Data de deteção:** 14/10/2026  
**Projeto:** B3 — A Bolsa do Brasil  
**Estado:** ENCERRADA — SIDECAR CORRIGIDO E AUDITORIA FÍSICA APROVADA  
**Âmbito:** integridade física do CSV NORMALIZED de 1998

## 1. Resumo

A auditoria inicial identificou divergência isolada no sidecar SHA-256 de 1998. Após a correção e reexecução integral, a auditoria física validou **41/41 anos**, sem falhas, e terminou com `APROVADO`.

- **CSV físico SHA-256:** `21b4740da8eb763259a0d859e261534de826449148c4d57d1f457f5721354e79`
- **SHA-256 do manifesto:** `21b4740da8eb763259a0d859e261534de826449148c4d57d1f457f5721354e79`
- **SHA-256 do sidecar anterior:** `d1297e58cbbdf225f792b49a29f9143d3e041e66fd280808732e8c3513eb6bee`
- **SHA-256 do sidecar corrigido:** `21b4740da8eb763259a0d859e261534de826449148c4d57d1f457f5721354e79`
- **Linhas normalizadas:** 104.971
- **Campos:** 25
- **Intervalo de datas:** 1998-01-02 a 1998-12-30
- **Datas inválidas / fora do ano:** 0 / 0
- **Manifesto:** `dados/cotahist/normalized/manifests/COTAHIST_A1998_quality.json`
- **Sidecar:** `dados/cotahist/normalized/manifests/COTAHIST_A1998.csv.sha256`

A auditoria original indicou que o hash físico do CSV coincide com o hash do manifesto; a divergência era exclusivamente no sidecar. O sidecar foi corrigido em commit `0a0805be7c5f23faac04c02b430104f3dcde7ae6`. O workflow de auditoria física foi ajustado em `5eb51dee02912030638566c0aa36bd122c06d6d4` para auditar futuras alterações aos sidecars; execução de revalidação: [run 38576260466](https://github.com/carlos-andrade/B3/actions/runs/38576260466), concluída com sucesso.

## 2. Evidência

- Relatório físico completo: [AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json)
- Execução auditável: [workflow run 38568351293](https://github.com/carlos-andrade/B3/actions/runs/38568351293)
- O workflow terminou em falha de propósito, aplicando o gate fail-closed e preservando o relatório no repositório.

## 3. Correção autorizada e validação final

O utilizador autorizou explicitamente a resolução da exceção em 14/10/2026. A causa foi isolada ao sidecar: o SHA-256 do CSV físico e o do manifesto eram idênticos. A correção atualiza apenas `dados/cotahist/normalized/manifests/COTAHIST_A1998.csv.sha256` para o SHA-256 já confirmado pelo CSV e manifesto.

- CSV NORMALIZED: preservado, sem reescrita.
- Manifesto de qualidade: preservado.
- RAW e manifesto RAW: preservados.
- Nenhuma linha foi removida, deduplicada ou reordenada.
- A auditoria física foi reacionada para confirmar os 41 anos; não declarar aprovação global até o workflow concluir com sucesso.

## 4. Impacto e risco

- **Integridade do CSV versus manifesto:** consistente pelo SHA-256 observado.
- **Integridade do sidecar:** inconsistente; o valor não representa o conteúdo físico atual.
- **Risco operacional:** utilizadores ou pipelines que confiem exclusivamente no sidecar podem rejeitar o ficheiro ou produzir um diagnóstico falso de corrupção.
- **Limite da conclusão:** esta evidência não prova qual dos históricos gerou o sidecar divergente nem autoriza reescrita automática.

## 5. Critério de encerramento — cumprido

O incidente está encerrado. O workflow [38576260466](https://github.com/carlos-andrade/B3/actions/runs/38576260466) terminou com `success`; o relatório físico confirmou `APROVADO`, 41 anos auditados, 41 validados e zero falhas. Para 1998, CSV, manifesto e sidecar apresentam o mesmo SHA-256; foram confirmadas 104.971 linhas, 25 campos, zero datas inválidas e zero datas fora do ano. O CSV, o manifesto de qualidade e os dados RAW foram preservados.

---
