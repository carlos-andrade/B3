# ROADMAP COTAHIST 1999–2004 — Estado em 2026-10-12

**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** `carlos-andrade/B3`  
**Estado:** 1999–2003 fechados/certificados; COTAHIST 2004 com FASE00–FASE08 validadas; GATE 06–08 aprovado; FASE09 liberada; FASE10 validada; FASE11 certificada; FASE12 fechada; transição 2005 autorizada  
**Norma:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md` v1.0.1  
**Incidente de referência:** `docs/CARTA_INCIDENTE_INTEGRIDADE_COTAHIST_1999_V1.md`

## Resumo executivo

- **COTAHIST 1999:** FASE00–FASE10 validadas; FASE11 certificado; FASE12 fechou 1999 e autorizou a transição controlada para 2000.
- **COTAHIST 2000:** FASE01–FASE10 validadas; FASE11 certificado; FASE12 fechou 2000 e autorizou a transição controlada para 2001.
- O CSV normalizado de 2000 foi recuperado e persistido. O hash físico coincide com o manifesto e o sidecar.
- Nenhum registo foi deduplicado nem removido.
- **COTAHIST 2001:** FASE01–FASE12 concluídas; FASE10 independente comparou os 25 campos em 141.848 registos, zero divergências e hashes conferidos. Gate 06–08 aprovado; FASE11 `CERTIFICADO`; FASE12 `FECHADO_COM_TRANSICAO_CONTROLADA`.
- **COTAHIST 2002:** FASE00–FASE12 concluídas; FASE10 independente comparou os 25 campos em 129.973 registos, zero divergências. FASE11 `CERTIFICADO`; FASE12 `FECHADO_COM_TRANSICAO_CONTROLADA`.
- O ano 2002 foi liberado para início controlado pela FASE12 de 2001; a primeira fase do novo ciclo deve ser FASE00/FASE01, sem saltar etapas.

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
| Gate 06–08 | GATE_APROVADO | `dados/cotahist/quality/COTAHIST_2000_GATE_06_08_V1.json` |
| FASE09 | LIBERADO_PARA_FASE10 | `dados/cotahist/quality/COTAHIST_2000_FASE09_PRE_RELEASE_V1.json` |
| FASE10 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE10_VALIDACAO_INDEPENDENTE_V1.json` |
| FASE11 | CERTIFICADO | `dados/cotahist/quality/COTAHIST_2000_FASE11_CERTIFICACAO_V1.json` |
| FASE12 | FECHADO_COM_TRANSICAO_CONTROLADA | `dados/cotahist/quality/COTAHIST_2000_FASE12_FECHAMENTO_2001_ABERTURA_V1.json` |

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


## COTAHIST 2000 — Fechamento

| Fase | Estado | Evidência |
|---|---|---|
| Gate 06–08 | GATE_APROVADO | `dados/cotahist/quality/COTAHIST_2000_GATE_06_08_V1.json` |
| FASE09 | LIBERADO_PARA_FASE10 | `dados/cotahist/quality/COTAHIST_2000_FASE09_PRE_RELEASE_V1.json` |
| FASE10 | VALIDADO | `dados/cotahist/quality/COTAHIST_2000_FASE10_VALIDACAO_INDEPENDENTE_V1.json` |
| FASE11 | CERTIFICADO | `dados/cotahist/quality/COTAHIST_2000_FASE11_CERTIFICACAO_V1.json` |
| FASE12 | FECHADO_COM_TRANSICAO_CONTROLADA | `dados/cotahist/quality/COTAHIST_2000_FASE12_FECHAMENTO_2001_ABERTURA_V1.json` |

FASE10 comparou independentemente os 25 campos do RAW com o NORMALIZED: 153.682 registos, zero divergências. A transição verificou o RAW 2001, o manifesto e o sidecar com SHA-256 `0386ca1b80d207ef9876fe64c2d48e9af1b827b3ecc0365c0e99db5cacf20eb5`. O CSV normalizado de 2001 não existia no início da transição e foi recuperado na FASE04.

## COTAHIST 2001 — Estado atual

| Fase | Estado | Evidência |
|---|---|---|
| FASE01 | VALIDADO | `dados/cotahist/quality/COTAHIST_2001_FASE01_AQUISICAO_RAW_V1.json` |
| FASE02 | VALIDADO | `dados/cotahist/quality/COTAHIST_2001_FASE02_INTEGRIDADE_FONTE_V1.json` |
| FASE03 | VALIDADO | `dados/cotahist/quality/COTAHIST_2001_FASE03_PARSING_V1.json` |
| FASE04 recuperação | EVIDÊNCIA RECONSTRUÍDA | `dados/cotahist/quality/COTAHIST_2001_FASE04_RECUPERACAO_V1.json` |
| FASE04 independente | VALIDADO | `dados/cotahist/quality/COTAHIST_2001_FASE04_NORMALIZACAO_V1.json` |
| FASE05 | VALIDADO | `dados/cotahist/quality/COTAHIST_2001_FASE05_MANIFESTO_CHECKSUM_V1.json` |
| FASE06 | VALIDADO | `dados/cotahist/quality/COTAHIST_2001_FASE06_RECONCILIACAO_V1.json` |
| FASE07 | VALIDADO | `dados/cotahist/quality/COTAHIST_2001_FASE07_IDENTIDADE_CHAVES_V1.json` |
| FASE08 | VALIDADO_COM_EXCECAO | `dados/cotahist/quality/COTAHIST_2001_FASE08_SEMANTICA_CALENDARIO_V1.json` |
| Gate 06–08 | GATE_APROVADO | `dados/cotahist/quality/COTAHIST_2001_GATE_06_08_V1.json` |
| FASE09 | LIBERADO_PARA_FASE10 | `dados/cotahist/quality/COTAHIST_2001_FASE09_PRE_RELEASE_V1.json` |
| FASE10 | VALIDADO | `dados/cotahist/quality/COTAHIST_2001_FASE10_VALIDACAO_INDEPENDENTE_V1.json` |
| FASE11 | CERTIFICADO | `dados/cotahist/quality/COTAHIST_2001_FASE11_CERTIFICACAO_V1.json` |
| FASE12 | FECHADO_COM_TRANSICAO_CONTROLADA | `dados/cotahist/quality/COTAHIST_2001_FASE12_FECHAMENTO_2002_ABERTURA_V1.json` |

### Integridade normalizado 2001

- RAW SHA-256: `0386ca1b80d207ef9876fe64c2d48e9af1b827b3ecc0365c0e99db5cacf20eb5`
- NORMALIZED SHA-256: `d15b1d6b5a407a397c7deb6a555a8572d9f9f6539ab657821a2e08f9f186396a`
- Registos: 141.848; campos: 25; datas: 2001-01-02 a 2001-12-28; FASE06 comparou 12 campos críticos com zero divergências.

## Próximas ações atualizadas

1. FASE07–FASE09 de 2001 concluídas; Gate 06–08 aprovado no run [38244654290](https://github.com/carlos-andrade/B3/actions/runs/38244654290).
2. FASE10 independente de 2001 validada no run [38244793960](https://github.com/carlos-andrade/B3/actions/runs/38244793960): 25 campos, 141.848 registos, zero divergências.
3. FASE11 de 2001 certificada no run [38244879058](https://github.com/carlos-andrade/B3/actions/runs/38244879058).
4. FASE12 de 2001 concluída no run [38244969020](https://github.com/carlos-andrade/B3/actions/runs/38244969020): fechamento aprovado e RAW 2002 verificado; CSV normalizado 2002 ausente.
5. Próximo ciclo: iniciar 2002 em FASE00/FASE01, seguir sequencialmente, reconstruir NORMALIZED apenas na FASE04 e validar manifesto/checksum antes de avançar.
6. Não atualizar README fora da janela de 23:55 Brasília.


## COTAHIST 2002 — Estado atual

| Fase | Estado | Evidência |
|---|---|---|
| FASE00 | VALIDADO | [COTAHIST_2002_FASE00_GOVERNANCA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE00_GOVERNANCA_V1.json) |
| FASE01 | VALIDADO | [COTAHIST_2002_FASE01_AQUISICAO_RAW_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE01_AQUISICAO_RAW_V1.json) |
| FASE02 | VALIDADO | [COTAHIST_2002_FASE02_INTEGRIDADE_FONTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE02_INTEGRIDADE_FONTE_V1.json) |
| FASE03 | VALIDADO | [COTAHIST_2002_FASE03_PARSING_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE03_PARSING_V1.json) |
| FASE04 recuperação | EVIDÊNCIA RECONSTRUÍDA | [COTAHIST_2002_FASE04_RECUPERACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE04_RECUPERACAO_V1.json) |
| FASE04 independente | VALIDADO | [COTAHIST_2002_FASE04_NORMALIZACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE04_NORMALIZACAO_V1.json) |
| FASE05 | VALIDADO | [COTAHIST_2002_FASE05_MANIFESTO_CHECKSUM_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE05_MANIFESTO_CHECKSUM_V1.json) |
| FASE06 | VALIDADO | [COTAHIST_2002_FASE06_RECONCILIACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE06_RECONCILIACAO_V1.json) |
| FASE07 | VALIDADO | [COTAHIST_2002_FASE07_IDENTIDADE_CHAVES_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE07_IDENTIDADE_CHAVES_V1.json) |
| FASE08 | VALIDADO_COM_EXCECAO | [COTAHIST_2002_FASE08_SEMANTICA_CALENDARIO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE08_SEMANTICA_CALENDARIO_V1.json) |
| Gate 06–08 | GATE_APROVADO | [COTAHIST_2002_GATE_06_08_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_GATE_06_08_V1.json) |
| FASE09 | LIBERADO_PARA_FASE10 | [COTAHIST_2002_FASE09_PRE_RELEASE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE09_PRE_RELEASE_V1.json) |
| FASE10 | VALIDADO | [COTAHIST_2002_FASE10_VALIDACAO_INDEPENDENTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE10_VALIDACAO_INDEPENDENTE_V1.json) |
| FASE11 | CERTIFICADO | [COTAHIST_2002_FASE11_CERTIFICACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE11_CERTIFICACAO_V1.json) |
| FASE12 | FECHADO_COM_TRANSICAO_CONTROLADA | [COTAHIST_2002_FASE12_FECHAMENTO_2003_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE12_FECHAMENTO_2003_ABERTURA_V1.json) |

### Integridade inicial 2002

- RAW SHA-256: `ee002b9a533d310351ed07ccb3a8cd3badd84993a4969c5b58088d738de59116`
- Fonte: B3; manifesto e sidecar coincidentes.
- ZIP: um membro, zero registos com comprimento diferente de 245 bytes; 129.973 registos tipo `01`, um registo tipo `00` e um tipo `99`.
- NORMALIZED: ausente. Não reconstruir antes das FASE01–03; a recuperação/normalização pertence à FASE04.

## Próximas ações atualizadas

1. COTAHIST 2001 foi fechado formalmente na FASE12; a transição para 2002 está autorizada.
2. FASE00 de 2002 validada no run [38245106125](https://github.com/carlos-andrade/B3/actions/runs/38245106125).
3. FASE01 de 2002 validada no run [38245216624](https://github.com/carlos-andrade/B3/actions/runs/38245216624); a primeira tentativa de persistência falhou por corrida de push, a correção foi incorporada ao workflow e a execução posterior persistiu a evidência com sucesso.
4. FASE02 validada no run [38245293962](https://github.com/carlos-andrade/B3/actions/runs/38245293962): ZIP, checksum, membro, tipos de registo e comprimentos verificados.
5. FASE03 validada no run [38245400382](https://github.com/carlos-andrade/B3/actions/runs/38245400382): 129.973 registos tipo 01, zero datas inválidas e zero comprimentos incorretos.
6. FASE04 regenerou o CSV no run [38245476318](https://github.com/carlos-andrade/B3/actions/runs/38245476318).
7. FASE04 independente validada no run [38245570050](https://github.com/carlos-andrade/B3/actions/runs/38245570050): hash do arquivo físico, manifesto e sidecar coincidentes; 129.973 linhas, 25 campos e intervalo de datas esperado.
8. FASE05 validada no run [38245636852](https://github.com/carlos-andrade/B3/actions/runs/38245636852); hash físico, manifesto e sidecar coincidentes, contagem e datas coerentes.
9. FASE06 validada no run [38245704769](https://github.com/carlos-andrade/B3/actions/runs/38245704769): 12 campos críticos, 129.973 registos, zero divergências.
10. FASE07 validada no run [38245774114](https://github.com/carlos-andrade/B3/actions/runs/38245774114): chave-base com 6.263 grupos de colisão; chave candidata com `prazot` sem duplicados, 129.973 registos preservados.
11. FASE08 validada no run [38245835385](https://github.com/carlos-andrade/B3/actions/runs/38245835385): 249 datas, zero datas inválidas/fora do ano e exceções não bloqueadoras classificadas; fonte não reordenada.
12. Gate 06–08 aprovado no run [38245902575](https://github.com/carlos-andrade/B3/actions/runs/38245902575), sem bloqueadores.
13. FASE09 concluída no run [38245939874](https://github.com/carlos-andrade/B3/actions/runs/38245939874), `LIBERADO_PARA_FASE10`; hashes RAW/NORMALIZED conferidos.
14. FASE10 independente validada no run [38246008895](https://github.com/carlos-andrade/B3/actions/runs/38246008895): 25 campos, 129.973 registos, zero divergências.
15. FASE11 de 2002 certificada no run [38246101444](https://github.com/carlos-andrade/B3/actions/runs/38246101444), sem bloqueadores.
16. FASE12 de 2002 concluída no run [38246172736](https://github.com/carlos-andrade/B3/actions/runs/38246172736); RAW 2003, manifesto e sidecar coincidentes, ZIP válido, 148.112 registos tipo 01.
17. Iniciar 2003 em FASE00 e seguir linearmente; o CSV normalizado 2003 está ausente e só deve ser reconstruído na FASE04 após FASE01–03.
18. Não deduplicar; não atualizar README fora das 23:55 Brasília.


## COTAHIST 2003 — Estado atual

| Fase | Estado | Evidência |
|---|---|---|
| Transição 2002→2003 | AUTORIZADA | [COTAHIST_2002_FASE12_FECHAMENTO_2003_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2002_FASE12_FECHAMENTO_2003_ABERTURA_V1.json) |
| FASE00 | VALIDADO | [COTAHIST_2003_FASE00_GOVERNANCA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE00_GOVERNANCA_V1.json) |
| FASE01 | VALIDADO | [COTAHIST_2003_FASE01_AQUISICAO_RAW_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE01_AQUISICAO_RAW_V1.json) |
| FASE02 | VALIDADO | [COTAHIST_2003_FASE02_INTEGRIDADE_FONTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE02_INTEGRIDADE_FONTE_V1.json) |
| FASE03 | VALIDADO | [COTAHIST_2003_FASE03_PARSING_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE03_PARSING_V1.json) |
| FASE04 recuperação | EVIDÊNCIA RECONSTRUÍDA | [COTAHIST_2003_FASE04_RECUPERACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE04_RECUPERACAO_V1.json) |
| FASE04 independente | VALIDADO | [COTAHIST_2003_FASE04_NORMALIZACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE04_NORMALIZACAO_V1.json) |
| FASE05 | VALIDADO | [COTAHIST_2003_FASE05_MANIFESTO_CHECKSUM_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE05_MANIFESTO_CHECKSUM_V1.json) |
| FASE06 | VALIDADO | [COTAHIST_2003_FASE06_RECONCILIACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE06_RECONCILIACAO_V1.json) |
| FASE07 | VALIDADO | [COTAHIST_2003_FASE07_IDENTIDADE_CHAVES_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE07_IDENTIDADE_CHAVES_V1.json) |
| FASE08 | VALIDADO_COM_EXCECAO | [COTAHIST_2003_FASE08_SEMANTICA_CALENDARIO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE08_SEMANTICA_CALENDARIO_V1.json) |
| Gate 06–08 | GATE_APROVADO | [COTAHIST_2003_GATE_06_08_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_GATE_06_08_V1.json) |
| FASE09 | LIBERADO_PARA_FASE10 | [COTAHIST_2003_FASE09_PRE_RELEASE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE09_PRE_RELEASE_V1.json) |
| FASE10 | VALIDADO | [COTAHIST_2003_FASE10_VALIDACAO_INDEPENDENTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE10_VALIDACAO_INDEPENDENTE_V1.json) |
| FASE11 | CERTIFICADO | [COTAHIST_2003_FASE11_CERTIFICACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE11_CERTIFICACAO_V1.json) |
| FASE12 | FECHADO_COM_TRANSICAO_CONTROLADA | [COTAHIST_2003_FASE12_FECHAMENTO_2004_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE12_FECHAMENTO_2004_ABERTURA_V1.json) |

### Estado físico de entrada 2003

- RAW: `dados/cotahist/raw/anual/COTAHIST_A2003.ZIP`
- SHA-256 RAW/manifesto/sidecar: `bcd337ebc1d92c190c4d8b77f582d2ec0890a8705fd5c10d68b28fa1eb15a2f0`
- ZIP: um membro, zero comprimentos inválidos, 148.112 registos tipo `01` e registos `00`/ `99` presentes.
- NORMALIZED: ausente; reconstrução só na FASE04.


## COTAHIST 2004 — Estado atual

| Fase | Estado | Evidência |
|---|---|---|
| Transição 2003→2004 | AUTORIZADA | [COTAHIST_2003_FASE12_FECHAMENTO_2004_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2003_FASE12_FECHAMENTO_2004_ABERTURA_V1.json) |
| FASE00 | VALIDADO | [COTAHIST_2004_FASE00_GOVERNANCA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE00_GOVERNANCA_V1.json) |
| FASE01 | VALIDADO | [COTAHIST_2004_FASE01_AQUISICAO_RAW_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE01_AQUISICAO_RAW_V1.json) |
| FASE02 | VALIDADO | [COTAHIST_2004_FASE02_INTEGRIDADE_FONTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE02_INTEGRIDADE_FONTE_V1.json) |
| FASE03 | VALIDADO | [COTAHIST_2004_FASE03_PARSING_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE03_PARSING_V1.json) |
| FASE04 recuperação | EVIDÊNCIA RECONSTRUÍDA | [COTAHIST_2004_FASE04_RECUPERACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE04_RECUPERACAO_V1.json) |
| FASE04 independente | VALIDADO | [COTAHIST_2004_FASE04_NORMALIZACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE04_NORMALIZACAO_V1.json) |
| FASE05 | VALIDADO | [COTAHIST_2004_FASE05_MANIFESTO_CHECKSUM_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE05_MANIFESTO_CHECKSUM_V1.json) |
| FASE06 | VALIDADO | [COTAHIST_2004_FASE06_RECONCILIACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE06_RECONCILIACAO_V1.json) |
| FASE07 | VALIDADO | [COTAHIST_2004_FASE07_IDENTIDADE_CHAVES_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE07_IDENTIDADE_CHAVES_V1.json) |
| FASE08 | VALIDADO_COM_EXCECAO | [COTAHIST_2004_FASE08_SEMANTICA_CALENDARIO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE08_SEMANTICA_CALENDARIO_V1.json) |
| GATE 06–08 | GATE_APROVADO | [COTAHIST_2004_GATE_06_08_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_GATE_06_08_V1.json) |
| FASE09 | LIBERADO_PARA_FASE10 | [COTAHIST_2004_FASE09_PRE_RELEASE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE09_PRE_RELEASE_V1.json) |
| FASE10 | VALIDADO | [COTAHIST_2004_FASE10_VALIDACAO_INDEPENDENTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE10_VALIDACAO_INDEPENDENTE_V1.json) |
| FASE11 | CERTIFICADO | [COTAHIST_2004_FASE11_CERTIFICACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE11_CERTIFICACAO_V1.json) |
| FASE12 | FECHADO_COM_TRANSICAO_CONTROLADA | [COTAHIST_2004_FASE12_FECHAMENTO_2005_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE12_FECHAMENTO_2005_ABERTURA_V1.json) |

### Estado físico de entrada 2004

- RAW: `dados/cotahist/raw/anual/COTAHIST_A2004.ZIP`
- SHA-256 RAW/manifesto/sidecar: `f750ba8ee9e25299ed96811979befb29315d91667fedc3885c709440b4989467`
- ZIP: um membro, zero comprimentos inválidos, 166.937 registos tipo `01` e registos `00`/ `99` presentes.
- NORMALIZED: `dados/cotahist/normalized/anual/COTAHIST_A2004.csv`; SHA-256 `3c8521b70bcd9b3dbdbe94df6008be46b65a4bfd589d59aa798f22d8cac2bb77`; 166.937 linhas, 25 campos. FASE04 e FASE05 validadas; reconciliação semântica linha a linha permanece na FASE06.


## Atualização operacional — FASE05 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — FASE05 Manifesto e Checksum](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase05-manifesto-checksum-2004-v1.yml)
- Execução: [run 38251912597](https://github.com/carlos-andrade/B3/actions/runs/38251912597)
- Evidência persistida: [COTAHIST_2004_FASE05_MANIFESTO_CHECKSUM_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE05_MANIFESTO_CHECKSUM_V1.json)
- RAW SHA-256 calculado = manifesto = sidecar: `f750ba8ee9e25299ed96811979befb29315d91667fedc3885c709440b4989467`.
- NORMALIZED SHA-256 calculado = manifesto = sidecar: `3c8521b70bcd9b3dbdbe94df6008be46b65a4bfd589d59aa798f22d8cac2bb77`.
- ZIP íntegro; membro `COTAHIST_A2004.TXT`; 166.937 linhas normalizadas, 25 campos, datas de 2004-01-02 a 2004-12-30.
- RAW preservado; nenhuma deduplicação executada.
- Decisão: `LIBERADO_PARA_FASE06`. FASE05 verifica integridade física e não substitui a reconciliação semântica da FASE06.


## Atualização operacional — FASE06 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — FASE06 Reconciliação Semântica](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase06-reconciliacao-2004-v1.yml)
- Execução validada: [run 38252049063](https://github.com/carlos-andrade/B3/actions/runs/38252049063)
- Evidência persistida: [COTAHIST_2004_FASE06_RECONCILIACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE06_RECONCILIACAO_V1.json)
- Registros RAW: 166.937; registros NORMALIZED: 166.937.
- Campos críticos comparados linha a linha: 12; divergências: 0.
- RAW SHA-256: `f750ba8ee9e25299ed96811979befb29315d91667fedc3885c709440b4989467`.
- NORMALIZED SHA-256: `3c8521b70bcd9b3dbdbe94df6008be46b65a4bfd589d59aa798f22d8cac2bb77`.
- RAW preservado; nenhuma deduplicação executada. Unicidade/cardinalidade permanece expressamente reservada à FASE07.
- Decisão: `LIBERADO_PARA_FASE07`.


## Atualização operacional — FASE07 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — FASE07 Identidade e Cardinalidade](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase07-identidade-2004-v1.yml)
- Execução: [run 38252121389](https://github.com/carlos-andrade/B3/actions/runs/38252121389)
- Evidência: [COTAHIST_2004_FASE07_IDENTIDADE_CHAVES_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE07_IDENTIDADE_CHAVES_V1.json)
- Registros analisados: 166.937; hash NORMALIZED: `3c8521b70bcd9b3dbdbe94df6008be46b65a4bfd589d59aa798f22d8cac2bb77`.
- Chave-base `[data_pregao,codbdi,codneg,tpmerc,dismes]`: 9.642 grupos duplicados, 20.705 linhas excedentes; grupos com linhas idênticas completas: 0.
- Chave candidata com `prazot`: 166.937 chaves distintas, zero grupos duplicados.
- Decisão restrita a 2004 e à versão normalizada identificada: `CHAVE_CANDIDATA_COM_PRAZOT_VALIDADA_POR_CARDINALIDADE`.
- Nenhuma linha removida; deduplicação não executada. A decisão não se generaliza automaticamente a outros anos.
- Próxima etapa: FASE08, preservando a ordem original da fonte e classificando explicitamente limitações do calendário histórico.


## Atualização operacional — FASE08 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — FASE08 Calendário e Consistência](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase08-calendario-2004-v1.yml)
- Execução: [run 38252181158](https://github.com/carlos-andrade/B3/actions/runs/38252181158)
- Evidência: [COTAHIST_2004_FASE08_SEMANTICA_CALENDARIO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE08_SEMANTICA_CALENDARIO_V1.json)
- Estado: `VALIDADO_COM_EXCECAO`; decisão: `LIBERADO_PARA_GATE_06_08`; bloqueadores: 0.
- Linhas analisadas: 166.937; datas de pregão distintas: 249; regressões cronológicas globais: 30.148; regressões de data por instrumento: 12.489.
- A ordem original da fonte foi preservada. A ausência de calendário oficial histórico persistido permanece limitação explicitamente classificada; não se afirma equivalência com lista externa oficial de pregões.
- Próximo passo: executar o Gate 06–08 para verificar as evidências FASE06/07/08 em modo somente leitura.


## Atualização operacional — Gate 06–08 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — Gate 06–08](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-gate-06-08-2004-v1.yml)
- Execução: [run 38252248693](https://github.com/carlos-andrade/B3/actions/runs/38252248693)
- Evidência: [COTAHIST_2004_GATE_06_08_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_GATE_06_08_V1.json)
- Resultado: `GATE_APROVADO`; decisão: `APROVADO_PARA_ANALISE_FASE09`; bloqueadores: 0.
- Estados consumidos: FASE06 `VALIDADO`; FASE07 `VALIDADO`; FASE08 `VALIDADO_COM_EXCECAO`.
- As exceções da FASE08 permanecem registradas e não foram apagadas nem reclassificadas pelo Gate.
- Próxima etapa: FASE09 — pré-release.


## Atualização operacional — FASE09 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — FASE09 Pré-release](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase09-prerelease-2004-v1.yml)
- Execução: [run 38252303530](https://github.com/carlos-andrade/B3/actions/runs/38252303530)
- Evidência: [COTAHIST_2004_FASE09_PRE_RELEASE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE09_PRE_RELEASE_V1.json)
- Resultado: `LIBERADO_PARA_FASE10`; `missing=[]`; `blocked=[]`; Gate 06–08 `GATE_APROVADO`.
- SHA-256 RAW: `f750ba8ee9e25299ed96811979befb29315d91667fedc3885c709440b4989467`.
- SHA-256 NORMALIZED: `3c8521b70bcd9b3dbdbe94df6008be46b65a4bfd589d59aa798f22d8cac2bb77`.
- A FASE09 consolida evidências; não reexecuta fases anteriores nem certifica o ano.
- Próxima etapa: FASE10, validação independente dos 25 campos linha a linha.


## Atualização operacional — FASE10 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — FASE10 Validação Independente Integral](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase10-validacao-independente-2004-v1.yml)
- Execução: [run 38252359646](https://github.com/carlos-andrade/B3/actions/runs/38252359646)
- Evidência: [COTAHIST_2004_FASE10_VALIDACAO_INDEPENDENTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE10_VALIDACAO_INDEPENDENTE_V1.json)
- Resultado: `VALIDADO`; decisão: `LIBERADO_PARA_FASE11`.
- RAW: 166.937 registros; NORMALIZED: 166.937 registros; campos verificados: 25; divergências: 0.
- SHA-256 RAW: `f750ba8ee9e25299ed96811979befb29315d91667fedc3885c709440b4989467`.
- SHA-256 NORMALIZED: `3c8521b70bcd9b3dbdbe94df6008be46b65a4bfd589d59aa798f22d8cac2bb77`.
- RAW preservado; nenhuma deduplicação executada. A validação independente não certifica nem fecha o ano.
- Próxima etapa: FASE11 — certificação anual.


## Atualização operacional — FASE11 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — FASE11 Certificação](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase11-certificacao-2004-v1.yml)
- Execução: [run 38252431324](https://github.com/carlos-andrade/B3/actions/runs/38252431324)
- Evidência: [COTAHIST_2004_FASE11_CERTIFICACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE11_CERTIFICACAO_V1.json)
- Estado: `CERTIFICADO`; decisão: `LIBERADO_PARA_FASE12`; bloqueadores: 0.
- FASE10 independente: 25 campos, 166.937 registros, zero divergências.
- Escopo da certificação: integridade e consistência do conjunto COTAHIST 2004 conforme evidências anteriores; não certifica estratégias de investimento e não autoriza deduplicação.
- Próxima etapa: FASE12 — fechamento formal do ano e verificação das condições de transição para 2005.


## Atualização operacional — FASE12 COTAHIST 2004 — 2026-10-12

- Workflow: [COTAHIST 2004 — FASE12 Fechamento e Transição 2005](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase12-fechamento-2004-abertura-2005-v1.yml)
- Execução: [run 38252492115](https://github.com/carlos-andrade/B3/actions/runs/38252492115)
- Evidência: [COTAHIST_2004_FASE12_FECHAMENTO_2005_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE12_FECHAMENTO_2005_ABERTURA_V1.json)
- Resultado: `FECHADO_COM_TRANSICAO_CONTROLADA`; decisão: `FECHAR_2004_E_AUTORIZAR_CONTINUACAO_2005`; bloqueadores: 0.
- Certificação 2004 confirmada; RAW 2005 conferido contra manifesto e sidecar; ZIP íntegro, um membro, 181.408 registros tipo 01, registros de cabeçalho/trailer presentes.
- NORMALIZED 2005 ausente. A transição autoriza iniciar o ciclo 2005, mas não certifica o ano nem permite saltar fases; a normalização só pode ocorrer na FASE04 após FASE00–03.
- Próxima ação: iniciar 2005 pela governança/pré-condições e aquisição/integridade do RAW, em sequência controlada.
