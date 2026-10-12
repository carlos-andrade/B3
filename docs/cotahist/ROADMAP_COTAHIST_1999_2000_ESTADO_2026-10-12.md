# ROADMAP COTAHIST 1999–2000 — Estado em 2026-10-12

**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** `carlos-andrade/B3`  
**Estado:** 1999 fechado; 2000 em execução controlada  
**Norma:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md` v1.0.1  
**Incidente de referência:** `docs/CARTA_INCIDENTE_INTEGRIDADE_COTAHIST_1999_V1.md`

## Resumo executivo

- **COTAHIST 1999:** FASE00–FASE10 validadas; FASE11 certificado; FASE12 fechou 1999 e autorizou a transição controlada para 2000.
- **COTAHIST 2000:** FASE01–FASE07 validadas; FASE08 `VALIDADO_COM_EXCECAO`; Gate 06–08 criado e aguardando execução final no GitHub Actions.
- O CSV normalizado de 2000 foi recuperado e persistido. O hash físico coincide com o manifesto e o sidecar.
- Nenhum registo foi deduplicado nem removido.
- O ano 2001 permanece bloqueado até fechamento formal de 2000.

## COTAHIST 1999

| Fase | Estado | Evidência |
|---|---|---|
| FASE00 | VALIDADO | Governança/pré-condições existentes |
| FASE01 | VALIDADO | RAW/manifesto/checksum canónicos |
| FASE02 | VALIDADO | `dados/cotahist/quality/COTAHIST_1999_FASE02_INTEGRIDADE_FONTE_V1.json` |
| FASE03 | VALIDADO | `dados/cotahist/quality/COTAHIST_1999_FASE03_PARSING_V1.json` |
| FASE04 | VALIDADO | `dados/cotahist/quality/COTAHIST_1999_FASE04_NORMALIZACAO_V1.json` |
| FASE05 | VALIDADO | `dados/cotahist/quality/COTAHIST_1999_FASE05_MANIFESTO_CHECKSUM_V1.json` |
| FASE06 | VALIDADO | `dados/cotahist/quality/COTAHIST_1999_FASE06_RECONCILIACAO_V1.json` |
| FASE07 | VALIDADO | `dados/cotahist/quality/COTAHIST_1999_FASE07_IDENTIDADE_CHAVES_V1.json` |
| FASE08 | VALIDADO_COM_EXCECAO | `dados/cotahist/quality/COTAHIST_1999_FASE08_SEMANTICA_CALENDARIO_V1.json` |
| Gate 06–08 | GATE_APROVADO | `dados/cotahist/quality/COTAHIST_1999_GATE_06_08_V1.json` |
| FASE09 | LIBERADO_PARA_FASE10 | `dados/cotahist/quality/COTAHIST_1999_FASE09_PRE_RELEASE_V1.json` |
| FASE10 | VALIDADO | `dados/cotahist/quality/COTAHIST_1999_FASE10_VALIDACAO_INDEPENDENTE_V1.json` |
| FASE11 | CERTIFICADO | `dados/cotahist/quality/COTAHIST_1999_FASE11_CERTIFICACAO_V1.json` |
| FASE12 | FECHADO_COM_TRANSICAO_CONTROLADA | `dados/cotahist/quality/COTAHIST_1999_FASE12_FECHAMENTO_2000_ABERTURA_V1.json` |

### Integridade normalizado 1999

- RAW SHA-256: `fe7428b367a2d40acaefe823fd5080254d07f9ad6c29fc64c9e6876cbd876f09`
- NORMALIZED SHA-256: `0bf3643a8a06f6e513f97d8cf4d5fd0a7ac718af6d8a55a9ac8bdd230d4e2b1d`
- Registos: 129.841; campos: 25; divergências independentes: 0.
- Correção do normalizador: versão 1.1.2, com offsets restaurados para `ptoexe`, `codisi` e `dismes`.

## COTAHIST 2000

| Fase | Estado | Evidência |
|---|---|---|
| FASE00 | Governança comum | Regras do LAYOUT Mestre |
| FASE01 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE01_AQUISICAO_RAW_V1.json` |
| FASE02 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE02_INTEGRIDADE_FONTE_V1.json` |
| FASE03 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE03_PARSING_V1.json` |
| FASE04 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE04_NORMALIZACAO_V1.json` |
| FASE05 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE05_MANIFESTO_CHECKSUM_V1.json` |
| FASE06 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE06_RECONCILIACAO_V1.json` |
| FASE07 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE07_IDENTIDADE_CHAVES_V1.json` |
| FASE08 | VALIDADO_COM_EXCECAO | `dados/cotahist/quality/COTAHIST_2000_FASE08_SEMANTICA_CALENDARIO_V1.json` |
| Gate 06–08 | PENDENTE | Workflow `cotahist-gate-06-08-2000-v1.yml` em fila |
| FASE09 | NÃO INICIADA | Aguarda Gate 06–08 |
| FASE10 | NÃO INICIADA | Validação independente de todos os 25 campos |
| FASE11 | NÃO INICIADA | Certificação condicionada à FASE10 |
| FASE12 | NÃO INICIADA | Fechamento de 2000 e transição para 2001 |

### Integridade normalizado 2000

- RAW SHA-256: `77ba58b5138e384be140759bf836e8cc22189cdfecdf80e4c13672c535f42bd6`
- NORMALIZED SHA-256: `d0f3158c05ccfb50d1d7bcf98ec75f4a4480a7dd5acd1fae19ffd1d51e64ecca`
- Registos: 153.682; campos: 25; divergências FASE06 nos 12 campos críticos: 0.
- O CSV foi regenerado a partir do RAW e reconciliado com manifesto/sidecar.

### Decisão de identidade 2000

- Chave base `[data_pregao,codbdi,codneg,tpmerc,dismes]`: 6.069 grupos de colisão, 8.150 linhas excedentes; nenhum grupo era idêntico em todos os campos.
- Chave candidata `[data_pregao,codbdi,codneg,tpmerc,prazot,dismes]`: zero grupos duplicados.
- A chave candidata foi validada empiricamente para 2000; nenhuma linha foi removida.

### Exceções temporais 2000

- 248 datas distintas, de `2000-01-03` a `2000-12-28`.
- Zero datas inválidas, fora do ano ou em fim de semana.
- 22.957 regressões de data na ordem global dos registos. Não se ordenou o CSV: a FASE06 confirmou os campos críticos linha a linha, e a FASE08 registou a ordem original como característica da fonte, não como requisito de cronologia global.
- A FASE10 independente deverá comparar todos os 25 campos linha a linha.
- A lista oficial histórica de feriados/sessões B3 de 2000 não está persistida; a limitação permanece explicitamente classificada.

## Próximas ações

1. Concluir a execução do Gate 06–08 de 2000 e confirmar a evidência persistida.
2. Executar FASE09 de 2000.
3. Executar FASE10 independente comparando os 25 campos RAW × NORMALIZED.
4. Só após FASE10 validada, executar FASE11 certificação.
5. Executar FASE12 para fechar 2000; só então abrir 2001.
6. Não atualizar README fora da janela de 23:55 Brasília.
