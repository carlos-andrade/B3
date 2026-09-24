# PARTE03 — JANELA TEMPORAL COPOM × B3 — V1.0

**Arquivo:** PARTE03_BCB_COPOM_B3_JANELA_EVENTO_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Data de criação:** 24/09/2026
**Fonte macro:** Banco Central do Brasil
**Estado:** ESPECIFICAÇÃO

## 1. Objetivo

Definir uma estrutura auditável para medir a reação intradiária dos contratos B3 aos eventos Copom sem look-ahead.

## 2. Evento-âncora — 281ª reunião

- Reunião: 15–16/09/2026
- Decisão: 16/09/2026
- Meta anterior: 14,00%
- Meta nova: 13,75%
- Vigência: 17/09/2026
- Votação: 7–0
- Comunicado: 16/09/2026
- Ata: 22/09/2026

O BCB estabelece que os comunicados são divulgados após o término da segunda sessão, a partir das 18h. Portanto, sem timestamp documental específico, a janela não deve tratar 18:00 como horário exato do release.

## 3. Instrumentos

### Juros
- DI1 — contratos relevantes ao vértice analisado.

### Índice
- WIN — contrato futuro de Ibovespa vigente no pregão.

### Câmbio
- WDO — contrato futuro de dólar vigente no pregão.

## 4. Janelas

Cada evento deve gerar:

1. **PRE** — período anterior ao evento.
2. **EVENTO** — intervalo cuja âncora é o timestamp comprovado.
3. **POST_5M**
4. **POST_15M**
5. **POST_30M**
6. **POST_60M**
7. **FECHAMENTO**
8. **D+1_OPEN** — abertura do pregão seguinte.

Quando o timestamp exato não estiver comprovado, registrar a janela como **BOUNDARY/INTERVAL**, nunca como ponto exato.

## 5. Métricas mínimas

Para cada instrumento:

- retorno;
- máxima excursão favorável;
- máxima excursão adversa;
- amplitude;
- volume financeiro;
- número de negócios, quando disponível;
- agressão compradora/vendedora;
- Cumulative Delta;
- VWAP;
- distância do preço à VWAP;
- volatilidade realizada;
- gap;
- deslocamento em ticks;
- liquidez disponível, quando dataset permitir.

## 6. Regra de informação

Um dado só pode entrar no estado informacional do backtest quando sua disponibilidade temporal for <= timestamp da barra/evento.

A Ata publicada em 22/09/2026 **não pode** ser utilizada para explicar ou filtrar a reação de mercado de 16/09/2026 em um backtest causal.

## 7. Estado atual

**Evento Copom:** NORMALIZED  
**Timestamp exato do Comunicado 281:** UNKNOWN  
**RAW HTTP integral:** PENDING  
**SHA-256 HTTP:** PENDING  
**Dataset intradiário B3 no repositório:** NÃO LOCALIZADO  
**Reconciliação de preços/fluxo:** PENDING_DATASET

## 8. Critério de conclusão

A reconciliação 281 somente será marcada como COMPLETE quando houver:

- dados intradiários B3;
- timezone documentado;
- contrato negociado identificado;
- timestamp sem ambiguidade ou intervalo explicitamente modelado;
- OHLC/volume;
- fluxo, se disponível;
- hash/evidência do dataset;
- teste no-lookahead;
- relatório de resultados.

## 9. Fonte institucional

O Portal de Dados Abertos do BCB identifica os dados de Atas e Comunicados como base oficial e informa que a decisão é divulgada no mesmo dia por Comunicado. O BCB também documenta que os comunicados são divulgados após o término da segunda sessão, a partir das 18h.
