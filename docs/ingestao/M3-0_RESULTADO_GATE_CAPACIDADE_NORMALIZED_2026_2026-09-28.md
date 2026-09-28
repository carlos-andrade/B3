# M3-0 — Resultado do Gate de Capacidade NORMALIZED 2026

**Arquivo:** M3-0_RESULTADO_GATE_CAPACIDADE_NORMALIZED_2026_2026-09-28.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Fase:** M3-0 — Gate de capacidade NORMALIZED  
**Data de execução:** 28/09/2026  
**Repositório:** carlos-andrade/B3  
**Branch:** main

## 1. Execução

- Workflow: `COTAHIST - M3-0 gate capacidade NORMALIZED 2026`
- Workflow file: `.github/workflows/cotahist-m3-0-gate-capacidade-2026.yml`
- Run number: **4**
- Run ID: **36405803352**
- Evento: `workflow_dispatch`
- Commit avaliado: `029cf43931a4d3f39f1e7df73116cca080152c3e`
- Job: `capacity`
- Duração aproximada: **2 min 3 s**
- Conclusão do GitHub Actions: **failure**

> A conclusão `failure` é esperada neste gate quando o arquivo NORMALIZED excede o limite definido. O erro não representa falha de normalização.

## 2. Evidências produzidas

| Evidência | Resultado |
|---|---:|
| Parser | 1.1.0 |
| COTAÇÕES tipo 01 | 2.919.760 |
| Primeira data | 2026-01-02 |
| Última data | 2026-09-23 |
| NORMALIZED bytes | 392.044.266 |
| NORMALIZED SHA-256 | `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9` |
| Manifest SHA-256 | `d97514f3224da3b70b5b890911c7383e86a6d69ffc5482eb610826d729b2a1fa` |
| Manifest linhas | 2.904.013 |
| Manifest campos | 25 |
| Decisão | **GIT_STANDARD_LIMIT** |

## 3. Interpretação

O arquivo NORMALIZED gerado em `/tmp` possui **392.044.266 bytes (~392,04 MB)**, superando o limite operacional de **100.000.000 bytes** estabelecido pelo M3-0.

Portanto:

**M3-0 = BLOQUEADO PARA PERSISTÊNCIA NORMAL NO GIT STANDARD.**

O workflow executou corretamente a proteção `fail-closed`: normalizou o RAW, mediu o resultado e interrompeu a migração antes de persistir o CSV anual.

## 4. O que não deve ser feito

Até decisão formal sobre armazenamento versionado, não:

- persistir `COTAHIST_A2026.csv` no Git padrão;
- dividir arbitrariamente o dataset;
- reduzir campos;
- deduplicar registros para diminuir tamanho;
- alterar o RAW;
- mascarar o tamanho por compressão sem contrato de distribuição/reprodutibilidade;
- iniciar a migração anual em lote.

## 5. Próxima decisão obrigatória

Avaliar e formalizar o mecanismo de armazenamento versionado para NORMALIZED anual acima de 100 MB, mantendo:

1. RAW imutável;
2. parser determinístico;
3. SHA-256;
4. manifesto de qualidade;
5. certificação física;
6. rastreabilidade de versão;
7. reprodução do NORMALIZED;
8. fail-closed;
9. compatibilidade com os workflows automáticos.

As alternativas devem ser comparadas formalmente antes de qualquer migração: Git LFS ou armazenamento externo versionado/reprodutível.

## 6. Avisos do GitHub Actions

O runner também registrou aviso de depreciação do Node.js 20 para `actions/checkout@v4`, sendo atualmente forçado a Node.js 24.

Esse aviso **não causou a falha do M3-0**. O job chegou normalmente às etapas de normalização e medição.

Também foi registrado aviso futuro de migração de `ubuntu-latest` para Ubuntu 26 em 19/10/2026.

Esses avisos devem ser tratados como manutenção do workflow, mas não alteram o resultado do gate.

## 7. Conclusão auditável

**RESULTADO:** `GIT_STANDARD_LIMIT`

**NORMALIZED 2026:** 392.044.266 bytes

**LIMITE M3-0:** 100.000.000 bytes

**ULTRAPASSAGEM:** 292.044.266 bytes

**STATUS M3-0:** BLOQUEADO

**M3 MIGRAÇÃO ANUAL:** NÃO INICIAR

**Próxima etapa:** decisão formal de armazenamento NORMALIZED versionado.
