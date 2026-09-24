# PARTE03 — B3 INTRADAY: DIAGNÓSTICO DO DOWNLOAD DINÂMICO V1.1

**Arquivo:** PARTE03_B3_INTRADAY_DIAGNOSTICO_DOWNLOAD_2026-09-24.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Diagnóstico do mecanismo de download da Pesquisa por Pregão  
**Caminho:** docs/ingestao/PARTE03_B3_INTRADAY_DIAGNOSTICO_DOWNLOAD_2026-09-24.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Nova evidência

A página oficial da B3 declara explicitamente:

- os arquivos podem ser baixados pela própria página;
- para arquivos retroativos, deve-se selecionar a data desejada para cada arquivo.

A página, porém, é renderizada com campos dinâmicos: o conteúdo textual exposto pela página contém placeholders como `{contentId}` e não entrega ao mecanismo de pesquisa o URL final do arquivo.

## 2. Arquivos confirmados na página

A Pesquisa por Pregão apresenta:

- BVBG.086.01 PriceReport;
- BVBG.187.01 DerivativesSimplifiedPriceReport;
- BVBG.028.02 Instruments File;
- BVBG.029.02 IndicatorReport.

## 3. Implicação

A existência do arquivo está comprovada, mas a URL final do objeto binário não está exposta no HTML textual indexado.

Portanto, a próxima aquisição exige uma camada que consiga executar a interação dinâmica da página ou obter o endpoint do serviço que alimenta os campos `contentId`.

## 4. Não confundir com ausência de dados

STATUS:

SOURCE_EXISTS = TRUE
RETROACTIVE_SELECTION = TRUE
WEB_TEXT_DOWNLOAD_URL = NOT_EXPOSED
BINARY_CAPTURE = PENDING

Isso significa **mecanismo de acesso ainda não resolvido**, e não ausência dos dados na B3.

## 5. Requisito para captura

A aquisição deverá preservar:

- URL/endpoint efetivamente utilizado;
- data selecionada;
- nome do arquivo;
- bytes recebidos;
- SHA-256;
- Content-Type;
- timestamp UTC de captura;
- resposta HTTP quando disponível;
- metadados de origem.

## 6. Microestrutura

A B3 também confirma que o Boletim Diário do Mercado contém o capítulo:

Derivativos > Derivativos de bolsa > Negócio a negócio.

Assim, a investigação deve continuar em duas frentes:

A. Pesquisa por Pregão — arquivos históricos Clearing B3;

B. Boletim Diário do Mercado — Negócio a Negócio de Derivativos.

## 7. Estado

16/09/2026 RAW = PENDENTE  
17/09/2026 RAW = PENDENTE  
Endpoint dinâmico = PENDENTE  
Contrato de instrumento = PENDENTE  
WIN/WDO/DI = PENDENTE  
Agressor = PENDENTE  
Cumulative Delta = PENDENTE

## 8. Regra

Não utilizar dados de terceiros como substituição silenciosa da fonte primária B3. Caso uma fonte licenciada seja posteriormente incorporada, ela deverá receber `source_type=LICENSED_VENDOR` e ser reconciliada com a B3 quando possível.
