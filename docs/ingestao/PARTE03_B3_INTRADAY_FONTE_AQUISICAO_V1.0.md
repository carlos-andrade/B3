# PARTE03 — B3 INTRADAY: FONTE E AQUISIÇÃO V1.0

**Arquivo:** PARTE03_B3_INTRADAY_FONTE_AQUISICAO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Fonte oficial e procedimento de aquisição dos dados de negociação  
**Caminho:** docs/ingestao/PARTE03_B3_INTRADAY_FONTE_AQUISICAO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Evidência oficial

A página oficial Pesquisa por pregão da B3 informa que permite acessar boletins diários e arquivos emitidos pela B3 e selecionar datas retroativas para obtenção dos arquivos.

Fonte: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/

Entre os arquivos relevantes estão:

- BVBG.086.01 — PriceReport;
- BVBG.187.01 — DerivativesSimplifiedPriceReport;
- BVBG.028.02 — InstrumentReport.

A página oficial de layouts confirma a existência desses layouts.

## 2. Dados necessários

Para a primeira reconciliação:

- pregão 16/09/2026;
- pregão 17/09/2026;
- derivativos;
- WIN;
- WDO;
- DI;
- cadastro de instrumentos correspondente.

## 3. Limitação constatada

A interface pública indexada pela web expõe a seleção dinâmica de data e arquivo, mas não expõe no conteúdo textual um URL estático confiável para cada arquivo retroativo.

Portanto, não será fabricado um URL de download nem declarado que um arquivo foi capturado enquanto o conteúdo binário não estiver efetivamente disponível.

## 4. Ordem de aquisição

1. Selecionar 16/09/2026 na Pesquisa por pregão.
2. Obter BVBG.187.01 e/ou BVBG.086.01 conforme disponibilidade.
3. Obter BVBG.028.02 para identificação dos contratos.
4. Repetir para 17/09/2026.
5. Preservar os arquivos RAW sem alteração.
6. Calcular SHA-256.
7. Registrar tamanho, MIME type, data de captura e origem.
8. Validar estrutura contra o layout oficial.
9. Filtrar WIN/WDO/DI.
10. Só então gerar NORMALIZED.

## 5. Microestrutura

O BVBG.187.01 é um arquivo EOD de preços/dados resumidos de derivativos, portanto não deve ser tratado como tick-by-tick. A documentação oficial do arquivo o descreve como enviado EOD e disponível no site da B3.

Consequentemente:

- BVBG.187.01 = validação/consolidação EOD;
- BVBG.086.01 = investigar adequação à granularidade disponível;
- negócio a negócio = requisito para agressor/Cumulative Delta genuínos;
- OHLCV agregado = não suficiente para reconstruir agressor real.

## 6. Fonte alternativa oficial dentro do ecossistema B3

A documentação pública da B3 também identifica Negócio a Negócio – Listados, inclusive para derivativos, no Boletim Diário do Mercado.

Esse conjunto deve ser priorizado quando a granularidade necessária para microestrutura não estiver disponível no arquivo simplificado.

## 7. Estado em 24/09/2026

SOURCE_CONFIRMED = SIM  
RETROACTIVE_ACCESS_CONFIRMED = SIM  
STATIC_DOWNLOAD_URL_CONFIRMED = NÃO  
RAW_16_09_CAPTURED = NÃO  
RAW_17_09_CAPTURED = NÃO  
INTRADAY_TICK_DATA = PENDENTE  
AGGRESSOR_SIDE = PENDENTE  
CUMULATIVE_DELTA = PENDENTE

## 8. Regra de auditoria

Nenhuma análise de reação intraday do Copom 281 será publicada como resultado observado enquanto os arquivos de negociação correspondentes não estiverem preservados no repositório.
