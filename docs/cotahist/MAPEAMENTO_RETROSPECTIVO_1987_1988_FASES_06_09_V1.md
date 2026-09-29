# MAPEAMENTO RETROSPECTIVO — FASES 06–09 — 1987/1988 V1

**Data:** 2026-09-29  
**Objetivo:** mapear somente evidências efetivamente localizadas no repositório para o novo contrato das FASES 06–09.

## 1. Regra

Este documento não cria evidência retroativa. Ele apenas estabelece correspondência documental entre artefatos existentes e os requisitos do contrato `CONTRATOS_EVIDENCIA_FASES_06_09_V1.md`.

Classificação:

- **COMPROVADA** — requisito atendido por artefato identificável.
- **PARCIAL** — artefato relacionado, mas falta requisito do contrato.
- **NAO_COMPROVADA** — não foi localizada evidência específica suficiente.
- **EXCECAO_CONTROLADA** — evidência depende de regra histórica formal.

## 2. 1987

### FASE 06 — Reconciliação

**Status retrospectivo: COMPROVADA.**

Evidências localizadas:

- `scripts/ingestao/auditar_ohlc_cotahist_1987_v1.py`
  - blob SHA: `3407d3fb4749f4ce76d945b8515f6d0b5bad4705`
- `scripts/ingestao/auditar_quantidade_volume_cotahist_1987_v1.py`
  - blob SHA: `c1232fd8d13da4b56182fa672428b5b2636812c`
- matriz retrospectiva já registra reconciliação RAW/NORMALIZED como comprovada.

**Observação:** a existência dos scripts demonstra os testes específicos, mas o artefato consolidado de decisão da FASE06 deve continuar sendo identificado separadamente quando necessário para o orquestrador.

### FASE 07 — Identidade / Chaves

**Status retrospectivo: COMPROVADA.**

Evidência:

- `scripts/ingestao/auditar_chave_logica_cotahist_1987_v1.py`
  - blob SHA: `731379267d7abc1b41dd943d33ef12d87b941a7d`

A auditoria específica de chave lógica é evidência primária compatível com o contrato.

### FASE 08 — Semântica / Calendário

**Status retrospectivo: COMPROVADA COM EXCEÇÃO CONTROLADA.**

Evidência:

- `scripts/ingestao/auditar_calendario_cotahist_1987_v1.py`
  - blob SHA: `af80a66f14143f619ff6fc3286507f5c17a8f8b2`
- a matriz retrospectiva registra auditoria semântica e a exceção histórica de `PRAZOT`.

**Limitação:** a exceção de `PRAZOT` permanece semanticamente inconclusiva. Portanto, não deve ser convertida em `VALIDADO` sem exceção.

### FASE 09 — Pré-release

**Status retrospectivo: COMPROVADA, sujeito à preservação da exceção semântica.**

A matriz retrospectiva registra pré-release comprovado. A decisão futura deve carregar a exceção de `PRAZOT` explicitamente.

---

## 3. 1988

### FASE 06 — Reconciliação

**Status retrospectivo: COMPROVADA.**

Evidências específicas:

- `scripts/ingestao/auditar_ohlc_cotahist_1988_v1.py`
  - blob SHA: `1e65d03cf6d8395e9209e3315c4c8acec8305fa4`
- `scripts/ingestao/auditar_quantidade_volume_cotahist_1988_v1.py`
  - blob SHA: `7cf936c6ff2664b2da595a11478f54145e9c1b90`
- evidência independente:
  `dados/cotahist/quality/COTAHIST_1988_FASE10_INTEGRIDADE_V1.json`
  - blob SHA: `04e42d3dfdb5495787df4afd8393587abeede1c0`

A matriz retrospectiva registra a cadeia de reconciliação RAW/NORMALIZED como comprovada.

### FASE 07 — Identidade / Chaves

**Status retrospectivo: COMPROVADA.**

Evidência:

- `scripts/ingestao/auditar_chave_logica_cotahist_1988_v1.py`
  - blob SHA: `f9623177894056316df0ef16b193d30cb70e6c7e`

### FASE 08 — Semântica / Calendário

**Status retrospectivo: COMPROVADA.**

Evidência:

- `scripts/ingestao/auditar_calendario_cotahist_1988_v1.py`
  - blob SHA: `210466a04d27ae8fb5ac8fa6b3961578f1c5e82c`
- a matriz retrospectiva registra também cadeia semântica e preservação de exceções.

### FASE 09 — Pré-release

**Status retrospectivo: COMPROVADA.**

A matriz retrospectiva registra pré-release comprovado e uma cadeia documental completa para 1988, incluindo auditorias de calendário, chave, campos, OHLC, quantidade/volume, semântica, reconciliação, certificações e validação independente.

---

## 4. Resultado do mapeamento

| Ano | F06 | F07 | F08 | F09 | Observação |
|---|---|---|---|---|---|
| 1987 | COMPROVADA | COMPROVADA | EXCECAO_CONTROLADA | COMPROVADA | `PRAZOT` permanece exceção semântica |
| 1988 | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | cadeia documental mais completa |

## 5. O que ainda não está provado

Este mapeamento **não** prova automaticamente que 1989–1993 satisfazem os contratos 06–09.

Para 1989–1993, a matriz retrospectiva atual permanece:

- F06: NAO_COMPROVADA;
- F07: NAO_COMPROVADA;
- F08: NAO_COMPROVADA;
- F09: NAO_COMPROVADA.

Isso deve permanecer assim até que artefatos equivalentes sejam localizados ou produzidos por processo retrospectivo formalmente autorizado.

## 6. Regra para o DRY-RUN

O orquestrador pode usar este documento como fonte de equivalência **somente para 1987 e 1988** e somente dentro dos estados explicitamente registrados.

Não deve inferir equivalência para 1989–1993.

## 7. Próximo gate

1. atualizar o DRY-RUN para consumir contratos/equivalências;
2. executar o DRY-RUN em 1993;
3. confirmar que 1993 permanece bloqueado se F06–F09 não tiverem evidência;
4. somente depois analisar a possibilidade de equivalência retrospectiva de 1989–1993;
5. manter 1994 sem promoção até o fechamento dessa análise.
