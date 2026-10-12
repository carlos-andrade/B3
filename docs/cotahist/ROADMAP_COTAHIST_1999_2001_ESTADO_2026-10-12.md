# ROADMAP COTAHIST 1999–2003 — Estado em 2026-10-12

**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** `carlos-andrade/B3`  
**Estado:** 1999–2002 fechados/certificados; COTAHIST 2003 com FASE00–FASE02 validadas, próxima FASE03  
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
| FASE03–FASE12 | NÃO INICIADAS | Próxima: FASE03 — parsing estrutural |

### Estado físico de entrada 2003

- RAW: `dados/cotahist/raw/anual/COTAHIST_A2003.ZIP`
- SHA-256 RAW/manifesto/sidecar: `bcd337ebc1d92c190c4d8b77f582d2ec0890a8705fd5c10d68b28fa1eb15a2f0`
- ZIP: um membro, zero comprimentos inválidos, 148.112 registos tipo `01` e registos `00`/ `99` presentes.
- NORMALIZED: ausente; reconstrução só na FASE04.
