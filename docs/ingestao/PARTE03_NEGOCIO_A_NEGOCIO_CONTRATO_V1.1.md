# PARTE03 — NEGÓCIO A NEGÓCIO: CONTRATO DE INGESTÃO V1.1

**Arquivo:** PARTE03_NEGOCIO_A_NEGOCIO_CONTRATO_V1.1.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Ingestão de trades para microestrutura e Cumulative Delta  
**Caminho:** docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_CONTRATO_V1.1.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Definir o contrato operacional para ingestão de Negócio a Negócio dos derivativos B3, com foco inicial no Copom 281:

- 16/09/2026 — decisão do Copom;
- 17/09/2026 — sessão D+1.

Instrumentos-alvo:

- WIN;
- WDO;
- DI1.

## 2. Granularidade obrigatória

A unidade primária do dataset é um negócio individual.

Campos mínimos:

- trading_date;
- timestamp;
- timezone;
- instrument;
- ticker;
- contract;
- price;
- quantity;
- trade_id, se disponível;
- buy_order_id, se disponível;
- sell_order_id, se disponível;
- aggressor_side, se disponível;
- source;
- source_file;
- source_hash;
- retrieved_at.

Quando o arquivo fornecer campos adicionais, eles devem ser preservados no RAW e incorporados ao NORMALIZED sem perda de informação relevante.

## 3. Classificação de agressão

Prioridade:

1. campo explícito de agressor fornecido pela fonte;
2. campo de lado da ordem/agressor derivado inequivocamente pelo layout oficial;
3. classificação por bid/ask apenas quando bid e ask forem observados de forma temporalmente consistente;
4. regra de tick/price apenas como PROXY.

A classificação 4 nunca deve ser rotulada como agressão real.

## 4. Cumulative Delta

Para cada contrato:

Delta_t = volume_agressor_comprador,t - volume_agressor_vendedor,t

CumulativeDelta_t = soma acumulada de Delta desde o início da sessão.

Regras:

- quantidade deve permanecer na unidade original do contrato;
- não misturar contratos diferentes;
- reset no início de cada sessão;
- preservar sinal;
- registrar número de negócios classificados e não classificados;
- calcular cobertura de classificação.

Indicador de qualidade:

aggressor_coverage = negócios_classificados / negócios_totais.

Cumulative Delta real somente pode ser publicado quando a origem permitir classificação defensável.

## 5. VWAP

VWAP por sessão:

VWAP_t = soma(preço_i × quantidade_i) / soma(quantidade_i)

Quando o contrato possuir multiplicador financeiro específico, manter também uma métrica financeira separada. Não substituir quantidade por volume financeiro sem documentar a transformação.

## 6. TWAP

TWAP deve ser calculado sobre observações temporais ou barras uniformemente espaçadas. Não tratar cada negócio como peso igual e chamar o resultado de TWAP sem especificação.

## 7. Janelas do Copom 281

O dataset deve permitir recorte:

- PRE;
- EVENTO;
- POST_5M;
- POST_15M;
- POST_30M;
- POST_60M;
- FECHAMENTO;
- D+1_OPEN.

O timestamp exato de divulgação do comunicado continua desconhecido. Logo, a janela EVENTO deve ser parametrizável e não pode assumir 18:00 artificialmente.

## 8. Integridade

Cada lote deve registrar:

- nome do arquivo;
- SHA-256;
- tamanho;
- data de pregão;
- quantidade de trades;
- intervalo temporal;
- contratos encontrados;
- registros descartados;
- motivo do descarte;
- cobertura de agressão;
- versão do parser.

## 9. Controles contra look-ahead

Nenhum evento posterior pode contaminar variáveis calculadas para PRE ou EVENTO.

O timestamp de cada negócio deve ser mantido na normalização.

A informação sobre o resultado do Copom somente pode ser usada após seu timestamp de disponibilidade no estudo de evento.

## 10. Estado atual

Contrato de Negócio a Negócio: definido nesta versão.  
Arquivo binário B3 capturado: PENDENTE.  
Parser específico: próxima etapa.  
Agressor-side real: PENDENTE.  
Cumulative Delta real: PENDENTE.  
Reconciliação Copom × microestrutura: PENDENTE.

## 11. Regra de auditoria

Não preencher campos ausentes com inferência silenciosa.

Valores possíveis para agressor_side:

- BUY;
- SELL;
- UNKNOWN;
- PROXY_BUY;
- PROXY_SELL.

