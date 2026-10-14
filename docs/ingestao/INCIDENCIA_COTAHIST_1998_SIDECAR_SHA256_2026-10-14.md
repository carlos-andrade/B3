# INCIDÊNCIA CONTROLADA — COTAHIST 1998: DIVERGÊNCIA DE SIDECAR SHA-256

**Data de deteção:** 14/10/2026  
**Projeto:** B3 — A Bolsa do Brasil  
**Estado:** ABERTA / CONTROLADA — HISTÓRICO NÃO ALTERADO  
**Âmbito:** integridade física do CSV NORMALIZED de 1998

## 1. Resumo

A auditoria física independente de 41 ficheiros NORMALIZED (1986–2026) validou 40 anos e reprovou a auditoria global por uma divergência isolada no sidecar SHA-256 de 1998.

- **CSV físico SHA-256:** `21b4740da8eb763259a0d859e261534de826449148c4d57d1f457f5721354e79`
- **SHA-256 do manifesto:** `21b4740da8eb763259a0d859e261534de826449148c4d57d1f457f5721354e79`
- **SHA-256 do sidecar:** `d1297e58cbbdf225f792b49a29f9143d3e041e66fd280808732e8c3513eb6bee`
- **Linhas normalizadas:** 104.971
- **Campos:** 25
- **Intervalo de datas:** 1998-01-02 a 1998-12-30
- **Datas inválidas / fora do ano:** 0 / 0
- **Manifesto:** `dados/cotahist/normalized/manifests/COTAHIST_A1998_quality.json`
- **Sidecar:** `dados/cotahist/normalized/manifests/COTAHIST_A1998.csv.sha256`

A auditoria indica que o hash físico do CSV coincide com o hash do manifesto; a divergência detetada é entre esse hash e o sidecar.

## 2. Evidência

- Relatório físico completo: [AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json)
- Execução auditável: [workflow run 38568351293](https://github.com/carlos-andrade/B3/actions/runs/38568351293)
- O workflow terminou em falha de propósito, aplicando o gate fail-closed e preservando o relatório no repositório.

## 3. Decisão de contenção

O ano de 1998 pertence ao período 1986–2025, encerrado para ingestão rotineira e disponível apenas para consulta. Em cumprimento da política de retenção:

1. Não alterar o CSV NORMALIZED.
2. Não alterar o manifesto nem o sidecar histórico no ciclo rotineiro.
3. Manter a divergência registada e visível para consultas e auditorias.
4. Não declarar a auditoria física global aprovada enquanto a divergência persistir.
5. Qualquer correção futura exige reabertura formal do ano, análise da origem dos dois hashes, evidência antes/depois e nova auditoria.

## 4. Impacto e risco

- **Integridade do CSV versus manifesto:** consistente pelo SHA-256 observado.
- **Integridade do sidecar:** inconsistente; o valor não representa o conteúdo físico atual.
- **Risco operacional:** utilizadores ou pipelines que confiem exclusivamente no sidecar podem rejeitar o ficheiro ou produzir um diagnóstico falso de corrupção.
- **Limite da conclusão:** esta evidência não prova qual dos históricos gerou o sidecar divergente nem autoriza reescrita automática.

## 5. Critério de resolução

Resolver apenas após autorização explícita para reabrir a evidência de 1998, confirmar a proveniência do sidecar e executar novamente a auditoria física completa. Até lá, o estado permanece **ABERTA / CONTROLADA**, sem mutação do histórico.

---
