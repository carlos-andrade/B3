# PARTE03 — B3 INTRADAY: CONTRATO DE INGESTÃO V1.0

**Arquivo:** PARTE03_B3_INTRADAY_CONTRATO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Ingestão de dados intradiários para reconciliação de eventos macro  
**Caminho:** docs/ingestao/PARTE03_B3_INTRADAY_CONTRATO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Estabelecer o contrato mínimo para ingestão de dados de mercado necessários à reconciliação causal de eventos do Copom com WIN, WDO e DI.

A primeira janela-alvo é a reunião 281 do Copom, com decisão em 16/09/2026 e comparação com a sessão seguinte, 17/09/2026.

## 2. Fonte primária identificada

A B3 disponibiliza arquivos históricos por pregão. A página oficial lista, entre outros, o **Boletim de Negociação BVBG.086.01 (PriceReport)** e o **Boletim de Negociação Simplificado de Derivativos BVBG.187.01 (DerivativesSimplifiedPriceReport)**. A mesma área disponibiliza layouts dos arquivos de negociação de derivativos. 

Fonte oficial:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/

## 3. Granularidade

O projeto deve distinguir:

- **EOD/consolidado:** usado para validação diária.
- **Intraday/event-driven:** necessário para janelas PRE/EVENTO/POST.
- **Tick/negócio a negócio:** preferencial para agressão, Cumulative Delta e microestrutura.
- **Barra temporal:** aceitável como fallback para retorno, range, VWAP/TWAP e volatilidade.

Não se deve inferir agressão ou Cumulative Delta verdadeiro a partir de OHLCV agregado sem declarar explicitamente que se trata de proxy.

## 4. Campos mínimos

Cada observação intraday deve, quando disponível, conter:

- trading_date
- timestamp
- timezone
- instrument
- contract
- price
- quantity
- financial_volume
- trade_id, quando disponível
- buy_sell/aggressor_side, quando disponível
- source
- source_file
- source_hash
- retrieved_at

Para barras:

- open
- high
- low
- close
- volume
- financial_volume
- trade_count

## 5. Instrumentos

Primeiro escopo:

- WIN — futuro de Ibovespa
- WDO — futuro de dólar
- DI — futuro de taxa de juros

O contrato específico deve ser resolvido pelo cadastro de instrumentos da B3 e registrado por ISIN/código quando disponível. Não assumir automaticamente que o ticker genérico identifica um único vencimento.

## 6. Janelas

Para cada evento:

- PRE: período anterior ao timestamp de informação
- EVENTO: intervalo do anúncio
- POST_5M
- POST_15M
- POST_30M
- POST_60M
- FECHAMENTO
- D+1_OPEN

Quando o timestamp exato do comunicado não estiver disponível, EVENTO deve permanecer como intervalo de incerteza e não como horário artificialmente fixado.

## 7. Métricas

### Preço
- retorno
- MFE
- MAE
- range
- gap
- distância em ticks

### Fluxo
- volume financeiro
- quantidade de negócios
- agressão compradora/vendedora
- Cumulative Delta
- volume por preço, quando disponível

### Referências
- VWAP
- TWAP
- distância do preço à VWAP

### Risco
- volatilidade realizada
- máxima excursão adversa
- máxima excursão favorável
- drawdown intraday
- liquidez/spread, quando disponível

## 8. Regra de causalidade

Nenhum campo publicado depois do timestamp de decisão pode ser usado para construir uma variável que represente informação disponível antes do evento.

Cada observação deve carregar seu timestamp de informação e sua fonte.

## 9. Estado atual

Em 24/09/2026:

- Repositório pesquisado: não foram encontrados datasets intraday WIN/WDO/DI já armazenados.
- Fonte oficial B3 identificada: SIM.
- Layouts oficiais identificados: SIM.
- Dados intraday efetivamente capturados para 16/09/2026 e 17/09/2026: PENDENTE.
- Cumulative Delta real: PENDENTE.
- Agressor-side real: PENDENTE.
- Reconciliação Copom × mercado: PENDENTE_DATASET.

## 10. Próxima etapa

A ingestão deve primeiro capturar os arquivos oficiais de negociação disponíveis para as datas 16/09/2026 e 17/09/2026, preservar o RAW byte-for-byte, calcular SHA-256 e só então normalizar.

Se o arquivo oficial disponível for consolidado/EOD, ele será usado como validação diária, não como substituto silencioso do tick data.

## 11. Integridade

Obrigatório:

1. RAW imutável.
2. SHA-256.
3. metadata de captura.
4. parser versionado.
5. NORMALIZED separado de RAW.
6. reconciliação auditável.
7. identificação explícita de campos ausentes.
8. nenhuma imputação de agressão sem evidência.

## 12. Referências

- B3 — Pesquisa por pregão.
- B3 — Layout dos arquivos.
- B3 — Dados disponíveis / UP2DATA.
