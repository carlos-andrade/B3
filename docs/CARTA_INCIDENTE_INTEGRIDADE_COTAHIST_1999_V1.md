# CARTA DE INCIDENTE E INTEGRIDADE — COTAHIST 1999

**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** `carlos-andrade/B3`  
**Versão:** 1.0.0  
**Data:** 2026-10-12  
**Estado:** COTAHIST 1999 fechado e certificado; COTAHIST 2000 em execução até FASE08, Gate 06–08 pendente  
**Artefatos afetados:** COTAHIST anual de 1999, normalizador e evidência FASE04  
**Autoridade normativa operacional:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`

## 1. Fato observado

O CSV canónico `dados/cotahist/normalized/anual/COTAHIST_A1999.csv` não existia no repositório, embora o manifesto e o sidecar declarassem um SHA-256 esperado.

Foi executada uma recuperação determinística a partir do RAW imutável. A recuperação inicial produziu 129.841 registos, 25 campos e datas entre 1999-01-04 e 1999-12-30, mas o hash calculado (`d4c009984c23bde54532a9388da9841eca690286e10dc9c3502248f233840c7b`) divergiu do hash registado (`0bf3643a8a06f6e513f97d8cf4d5fd0a7ac718af6d8a55a9ac8bdd230d4e2b1d`).

A auditoria persistida em `dados/cotahist/quality/COTAHIST_1999_FASE04_RECUPERACAO_V1.json` classificou o resultado como bloqueado para promoção, sem alterar o RAW nem deduplicar registos.

## 2. Causa técnica identificada

A comparação do histórico do normalizador identificou alteração nos offsets dos três campos finais:

| Campo | Implementação anterior | Implementação corrigida |
|---|---:|---:|
| `ptoexe` | bytes 218–230, precisão de 6 casas | bytes 218–230, precisão de 6 casas |
| `codisi` | bytes 231–242 | bytes 231–242 |
| `dismes` | bytes 243–245 | bytes 243–245 |

A implementação publicada como versão 1.1.1 havia alterado incorretamente estes intervalos para 218–224, 225–236 e 237–245. A versão 1.1.2 restaura os offsets do layout de 245 bytes. A execução de recuperação concluiu com sucesso e reproduziu exatamente o SHA-256 histórico e do sidecar: `0bf3643a8a06f6e513f97d8cf4d5fd0a7ac718af6d8a55a9ac8bdd230d4e2b1d`. Contagem de 129.841 linhas, 25 campos e intervalo de datas coincidem com o manifesto.

## 3. Alterações persistidas

- Evidência canónica FASE02 validada: `dados/cotahist/quality/COTAHIST_1999_FASE02_INTEGRIDADE_FONTE_V1.json`
- Evidência canónica FASE03 validada: `dados/cotahist/quality/COTAHIST_1999_FASE03_PARSING_V1.json`
- Evidência independente FASE04 validada: `dados/cotahist/quality/COTAHIST_1999_FASE04_NORMALIZACAO_V1.json`
- Evidência FASE05 validada: `dados/cotahist/quality/COTAHIST_1999_FASE05_MANIFESTO_CHECKSUM_V1.json`
- Workflow FASE02: `.github/workflows/cotahist-fase02-integridade-1999-v1.yml`
- Workflow FASE03: `.github/workflows/cotahist-fase03-parsing-1999-v1.yml`
- Workflow FASE04: `.github/workflows/cotahist-fase04-validacao-independente-1999-v1.yml`
- Workflow FASE05: `.github/workflows/cotahist-fase05-manifesto-checksum-1999-v1.yml`
- Workflow FASE06 corrigido para comparar datas ISO, identificadores textuais e inteiros: `.github/workflows/cotahist-fase06-reconciliacao-1999-v1.yml`
- Evidência FASE06 validada: 129.841 registos RAW e NORMALIZED; 12 campos críticos comparados; zero divergências.
- Evidência FASE07 validada: chave base produziu 1.673 grupos de colisão e 1.765 linhas excedentes; a chave candidata que inclui `prazot` produziu zero grupos duplicados, sem remover linhas.
- Evidência FASE08: 246 datas distintas, intervalo 1999-01-04 a 1999-12-30, zero datas inválidas/fora do ano/regressões cronológicas; calendário oficial histórico externo não persistido, registado como exceção não bloqueadora apenas para consistência interna.
- Gate 06–08: `GATE_APROVADO`, decisão `APROVADO_PARA_ANALISE_FASE09`, sem bloqueadores.
- Workflows FASE07, FASE08 e Gate: `.github/workflows/cotahist-fase07-identidade-1999-v1.yml`, `.github/workflows/cotahist-fase08-calendario-1999-v1.yml`, `.github/workflows/cotahist-gate-06-08-1999-v1.yml`.
- Workflow FASE09: `.github/workflows/cotahist-fase09-prerelease-1999-v1.yml`.
- FASE09 1999: `LIBERADO_PARA_FASE10`; FASE10 independente: `VALIDADO`, 129.841 linhas e 25 campos, zero divergências; FASE11: `CERTIFICADO`; FASE12: `FECHADO_COM_TRANSICAO_CONTROLADA`.
- Transição 2000: RAW SHA-256 `77ba58b5138e384be140759bf836e8cc22189cdfecdf80e4c13672c535f42bd6` verificado contra manifesto e sidecar; ZIP estruturalmente válido.
- COTAHIST 2000 FASE01–06: evidências canónicas persistidas e validadas; CSV recuperado com 153.682 linhas, 25 campos, hash `d0f3158c05ccfb50d1d7bcf98ec75f4a4480a7dd5acd1fae19ffd1d51e64ecca` coincidente com manifesto e sidecar; FASE06 zero divergências nos 12 campos críticos.
- COTAHIST 2000 FASE07: chave base com 6.069 grupos de colisão e 8.150 linhas excedentes; chave candidata incluindo `prazot` com zero grupos duplicados, sem deduplicação.
- COTAHIST 2000 FASE08: 248 datas distintas; zero datas inválidas/fora do ano; 22.957 regressões de ordem global documentadas como característica da ordem da fonte, não como erro de data, pois a FASE06 reconciliou os campos críticos linha a linha. Calendário oficial histórico externo permanece não persistido.
- Gate 06–08 de 2000: workflow criado, execução em fila no GitHub Actions.

## 3.1 Alterações anteriores

- Workflow de recuperação: `.github/workflows/cotahist-recuperar-normalized-1999-v1.yml`
- Normalizador corrigido: `scripts/ingestao/normalize_cotahist.py`, versão 1.1.2
- CSV regenerado e auditoria de divergência persistidos pelo commit `34a66a213f81874f995cd4c2153cb4239a6d3c45`
- Correção do normalizador persistida pelo commit `70acbb8559fcecafd894629315513b5dbe9fdd42`
- Recuperação reconciliada e evidência atualizada pelo commit `f06d0618a1e828e0f11d88537fca80987d5cfc3a`
- LAYOUT Mestre 1.0.1 com controles fail-closed persistido pelo commit `86fcf9309d3d5712485a3442391f254e87b99c0f`
- Reexecução configurada pelo commit `afe1c4c018bd27ec6f6ab8dd092b2d654c975ac3`

## 4. Regras de contenção

1. Não alterar o RAW nem o seu checksum.
2. Não atualizar manifesto ou sidecar apenas para fazê-los coincidir com uma saída divergente.
3. Não deduplicar registos na FASE04; identidade e cardinalidade pertencem à FASE07.
4. Exigir existência física, tamanho não nulo, hash calculado e reconciliação com manifesto/sidecar antes de promover qualquer artefato.
5. Exigir evidência canónica da FASE03 e validação independente antes de desbloquear as fases seguintes.
6. Distinguir código publicado, execução iniciada, execução concluída, evidência persistida e gate aprovado.

## 5. Próximos passos

1. Concluir o Gate 06–08 de 2000 e rever a exceção de calendário histórico.
2. Executar FASE09 e FASE10 independente de 2000, com comparação integral dos 25 campos.
3. Executar FASE11 e FASE12 para fechar 2000 apenas após a certificação.
4. Só então iniciar 2001; não promover o ano com evidência ausente.

## 6. Estado no momento do registo

**Estado atual:** 1999 está fechado após FASE10 independente validada, FASE11 certificada e FASE12 concluída. Para 2000, FASE01–07 estão validadas; FASE08 está `VALIDADO_COM_EXCECAO`, com a ordem original não cronológica explicitada e sem reordenar dados. O Gate 06–08 está criado e em fila; FASE09–12 de 2000 e o ano 2001 permanecem bloqueados até aos respetivos gates.
