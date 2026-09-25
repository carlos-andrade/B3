# FASE 09B — Teste de multiplicidade estrutural no Mercado a Termo

**Arquivo:** FASE09B_COTAHIST_1986_MULTIPLICIDADE_TERM_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Identificação sistemática de múltiplas linhas de termo com mesma chave parcial e comparação com K4  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 09B testa, de forma reproduzível sobre o RAW integral de 1986, se múltiplas linhas de termo com a mesma chave parcial são normalmente separadas pela K4 ou se permanecem colisões estatísticas.

## 2. Execução validada

Workflow: **COTAHIST FASE09B - Multiplicidade Term 1986**  
Run: **#6 — 36079369501**  
Head commit: **7c92ac2f3ec0d27d1cc13f3412bc6ba6074ec1d9**  
Conclusão: **success**  
Evidência: `dados/cotahist/quality/COTAHIST_1986_FASE09B_MULTIPLICIDADE_TERM_V1.json`  
Evidence SHA: **321e76d89cff9cbaf21c92efba1fac4d08e003d4**  
RAW ZIP SHA-256: **350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018**  
RAW extraído SHA-256: **c5fe0a62488595ffb93e4a26752cfc63650e17f88110355becde1d7b5fbe685c**

## 3. Resultado integral de 1986

- **177.981** registros tipo 01 processados.
- **36.595** grupos de termo pela chave parcial DATA + CODBDI + CODNEG + TPMERC + PRAZOT.
- **1** grupo com multiplicidade na chave parcial.
- **1** grupo com multiplicidade e estatísticas distintas.
- **36.595** grupos pela K4 completa.
- **1** colisão K4.
- **1** colisão K4 com estatísticas distintas.

A única ocorrência é:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Assim, o teste integral reproduz exatamente a exceção Vigor previamente identificada nas FASES 08C e 08H.

## 4. Classificação A/B/C

### Caso A — parcial múltipla, K4 diferente

**0 casos observados.**

### Caso B — parcial múltipla, mesma K4 e estatísticas diferentes

**1 caso observado.**

É o Vigor de 10/10/1986, linhas RAW 140808 e 140809.

### Caso C — parcial múltipla, mesma K4 e estatísticas iguais

**0 casos observados.**

## 5. Perfis estatísticos da colisão

**Linha 140808:** TOTNEG 1; QUATOT 39.000.000; VOLTOT 74.100,00; PREAB/PREMAX/PREMIN/PREMED/PREULT = 1,90.

**Linha 140809:** TOTNEG 4; QUATOT 190.000.000; VOLTOT 356.460,00; PREAB 1,65; PREMAX 1,91; PREMIN 1,65; PREMED 1,87; PREULT 1,75.

Os perfis são materialmente distintos. A diferença não está nos campos da K4.

## 6. Conclusão

O universo integral de 1986 apresenta **uma única multiplicidade na chave parcial e uma única colisão K4**, exatamente o caso Vigor.

Portanto, não há evidência de uma população de colisões K4 em 1986. A anomalia é estatisticamente excepcional dentro do arquivo anual.

Esse resultado fortalece a necessidade de investigação documental específica do BDI e das regras operacionais/publicação da época. Ele **não determina a causa histórica**.

As hipóteses continuam sendo: dimensão histórica não preservada na K4; regra operacional de agregação/publicação do BDI; outra dimensão operacional ausente da K4; ou erro de processamento/publicação.

## 7. Governança

- RAW alterado: **não**.
- Registros excluídos: **não**.
- Registros consolidados: **não**.
- Recodificação semântica: **não**.
- Identidade econômica inferida: **não**.
- Causa histórica inferida: **não**.

## 8. Status

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO

## 9. Próxima frente

A FASE 09B encerra o teste estatístico de multiplicidade no COTAHIST 1986.

A próxima frente é a reconstrução documental da regra de agregação/publicação do BDI para determinar qual dimensão histórica ou operacional permitia dois agregados sob a mesma K4.

Nenhuma alteração semântica deve ser aplicada ao dado normalizado sem evidência documental.