# Comparativo 1993 × 1994 — FASE06 COTAHIST

**Versão:** V1.0  
**Data:** 2026-09-30  
**Escopo:** reconciliação RAW × NORMALIZED

## 1. Objetivo

Usar o ano de 1993, já certificado e fechado, como baseline auditável para avaliar a implementação da FASE06 de 1994, sem alterar, reverter ou reprocessar o histórico certificado de 1993.

## 2. Estado factual

| Item | 1993 | 1994 |
|---|---|---|
| Evidência FASE06 | Existe | Ainda não existe |
| Status | VALIDADO | PENDENTE |
| Registros RAW reconciliados | 116.198 | 119.097 esperados |
| Registros NORMALIZED | 116.198 | 119.097 |
| Campos críticos | 12 | 12 previstos |
| Mismatch | 0 | Não determinado |
| Decisão | VALIDADO | Ainda sem liberação para FASE07 |

Fonte 1993: dados/cotahist/quality/COTAHIST_1993_FASE06_RECONCILIACAO_V1.json.

Fonte 1994: dados/cotahist/quality/COTAHIST_1994_FASE06_RECONCILIACAO_V1.json não existe atualmente na branch main.

## 3. Baseline 1993

A evidência de 1993 registra comparação reproduzível RAW/NORMALIZED para 12 campos críticos:

- data_pregao
- codbdi
- codneg
- tpmerc
- preab
- premax
- premin
- premed
- preult
- totneg
- quatot
- voltot

O resultado registrado é mismatch_count = 0.

A evidência também registra aliases de cabeçalho normalizado e explicita tratamento canônico de datas e escalas decimais.

## 4. Implementação 1994 em análise

O workflow .github/workflows/cotahist-fase06-reconciliacao-1994-v1.yml usa os mesmos 12 conceitos de campo, mas implementa a extração diretamente sobre o layout COTAHIST com posições 1-based inclusivas convertidas para slices Python.

Offsets utilizados:

| Campo | Posição B3 |
|---|---:|
| DATA | 03–10 |
| CODBDI | 11–12 |
| CODNEG | 13–24 |
| TPMERC | 25–27 |
| PREABE | 57–69 |
| PREMAX | 70–82 |
| PREMIN | 83–95 |
| PREMED | 96–108 |
| PREULT | 109–121 |
| TOTNEG | 148–152 |
| QUATOT | 153–170 |
| VOLTOT | 171–188 |

A implementação de 1994 foi corrigida no commit f72318e46d60acdf4706287e138504183dac5541 para alinhar os offsets do layout.

## 5. Diferenças que exigem atenção

### 5.1 Nome preab × preabe

A evidência de 1993 registra preab na lista de campos críticos, enquanto o cabeçalho canônico normalizado registra preabe. O workflow de 1994 exige preabe diretamente.

**Conclusão:** o comparativo deve preservar o nome canônico do dataset (preabe) e documentar preab como alias histórico da evidência de 1993.

### 5.2 Regra de comparação numérica

A evidência de 1993 declara que datas são comparadas em representação canônica YYYYMMDD e que escalas decimais de 10^n são aceitas quando a razão é inteira e limitada.

A nova implementação de 1994 foi alinhada ao executor retrospectivo de 1993: usa Decimal, normalização canônica de datas, escalas decimais limitadas e alias explícito para preabe/preab.

**Conclusão:** a divergência de implementação identificada na auditoria anterior foi corrigida na cadeia V2; o resultado ainda depende da execução real.

### 5.3 Decisão da FASE06

1993 registra decision: VALIDADO. Para 1994, o workflow está preparado para registrar LIBERADO_PARA_FASE07 quando não houver divergências.

**Conclusão:** são semânticas diferentes: 1993 representa o resultado final da reconciliação; 1994 representa explicitamente o gate de transição.

### 5.4 Execução

A cadeia V2 de 1994 agora possui executor equivalente ao modelo retrospectivo de 1993 para FASE06–08 e executor sequencial para FASE09–12. A execução ainda precisa ser comprovada pelo runner e pelas evidências produzidas.

## 6. Decisão técnica deste comparativo

1. 1993 permanece intacto e certificado.
2. 1994 permanece bloqueado na FASE06.
3. Não usar novos gatilhos como substituto de evidência.
4. Executar a nova cadeia 1994 V2 e verificar FASE06–12.
5. Não promover FASE07 até a evidência FASE06 estar VALIDADO.

## 7. Evidências de referência

- dados/cotahist/quality/COTAHIST_1993_FASE06_RECONCILIACAO_V1.json
- dados/cotahist/quality/COTAHIST_1994_FASE06_RECONCILIACAO_V1.json — ausente no momento desta auditoria
- .github/workflows/cotahist-fase06-reconciliacao-1994-v1.yml
- docs/cotahist/REGRA_GERAL_EXISTENCIA_E_VALIDACAO_V1.md

## 8. Status oficial

**1993:** CERTIFICADO / FECHADO.  
**1994 FASE00–05:** VALIDADO.  
**1994 FASE06:** PENDENTE — execução/evidência ainda não comprovadas.  
**Promoção para FASE07:** NÃO AUTORIZADA.