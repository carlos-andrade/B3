# RECONCILIAÇÃO — COPOM 281 — COMUNICADO × B3

**Arquivo:** PARTE03_BCB_COPOM_281_COMUNICADO_RECONCILIACAO_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Data:** 24/09/2026
**Versão:** V1.0

## 1. Fato confirmado

A 281ª reunião do Copom ocorreu em 15 e 16/09/2026. A decisão foi divulgada em 16/09/2026 e reduziu a meta Selic de 14,00% para 13,75% a.a.; a taxa passou a vigorar em 17/09/2026. A Ata oficial, publicada em 22/09/2026, confirma decisão unânime por 7 votos.

## 2. Comunicado

O catálogo oficial de Comunicados do Copom confirma que o BCB publica a decisão no mesmo dia. A captura documental de 24/09/2026 foi registrada em:

`dados/calendario_economico/raw/bcb_copom_281_comunicado_2026-09-24.md`

O arquivo é snapshot documental. **SHA-256 da resposta HTTP integral: PENDENTE.**

## 3. Informação temporal

- Data de decisão: 16/09/2026
- Data de início da nova meta: 17/09/2026
- Horário exato do Comunicado: UNKNOWN
- Regra institucional do BCB: comunicado após o término da segunda sessão, a partir das 18h.

Para backtest, não será atribuído um timestamp intradiário exato sem evidência de publicação.

## 4. Ligação com B3

O evento deve ser ligado posteriormente às séries intradiárias da B3, no mínimo:

- WIN — contrato futuro de Ibovespa;
- WDO — contrato futuro de dólar;
- DI — contratos futuros de juros;
- volume financeiro;
- agressão;
- Cumulative Delta, quando disponível;
- VWAP/TWAP;
- volatilidade;
- gap e deslocamento pós-evento.

### Janela-evento proposta

**Âncora:** 16/09/2026 — decisão Copom.

**Janelas a calcular somente após ingestão dos dados B3:**
- pré-evento;
- 18:00–18:30, sem presumir timestamp exato do comunicado;
- pós-evento;
- fechamento;
- abertura de 17/09/2026.

Nenhum retorno, volume, delta ou reação de preço deve ser inventado nesta etapa.

## 5. No-lookahead

A informação da decisão pode ser usada em backtests somente a partir do timestamp efetivamente comprovado de disponibilidade. A Ata de 22/09/2026 não pode contaminar qualquer backtest de 16/09/2026.

## 6. Estado

**COPOM_COMUNICADO:** NORMALIZED  
**HTTP_RAW_INTEGRAL:** PENDING  
**SHA256_HTTP:** PENDING  
**B3_INTRADAY_RECONCILIATION:** PENDING_DATASET

## 7. Próximo passo técnico

Capturar a resposta HTTP integral do recurso oficial/API do BCB, calcular SHA-256 e, em seguida, executar a reconciliação temporal com o dataset intradiário B3.