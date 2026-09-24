# PARTE03 — B3 INTRADAY: PADRÃO DE DOWNLOAD CONFIRMADO V1.0

**Arquivo:** PARTE03_B3_INTRADAY_PADRAO_DOWNLOAD_2026-09-24.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Padrões públicos de URL para Pesquisa por Pregão  
**Caminho:** docs/ingestao/PARTE03_B3_INTRADAY_PADRAO_DOWNLOAD_2026-09-24.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Resultado

A investigação encontrou implementações públicas independentes que confirmam que a B3 utiliza o endpoint:

https://www.b3.com.br/pesquisapregao/download?filelist=

com identificadores dependentes do tipo de arquivo e da data.

## 2. Padrões confirmados externamente

Para PriceReport, foi encontrado o padrão:

PRA + YYMMDD + .zip

Para Simplified Price Report de derivativos, foi encontrada implementação pública usando:

SPRD + YYMMDD + .zip

Para Instrument Report, outra implementação pública utiliza:

IN + YYMMDD + .zip

Esses padrões são evidência de implementação pública, não substituem a validação do arquivo retornado pela B3.

## 3. Primeiros candidatos para 16/09/2026

PriceReport:
PRA260916.zip

Simplified Price Report Derivatives:
SPRD260916.zip

InstrumentReport:
IN260916.zip

## 4. Primeiros candidatos para 17/09/2026

PriceReport:
PRA260917.zip

Simplified Price Report Derivatives:
SPRD260917.zip

InstrumentReport:
IN260917.zip

## 5. Regra de captura

Cada candidato deve ser testado por HTTP.

Aceitar somente se:

1. resposta HTTP for válida;
2. conteúdo for um arquivo ZIP estruturalmente válido;
3. ZIP possuir conteúdo compatível com o arquivo solicitado;
4. SHA-256 for calculado;
5. metadata for registrada.

Um HTTP 200 não significa automaticamente que o arquivo contém dados.

## 6. Validação de arquivo vazio

Há evidência pública de que a B3 pode retornar ZIP válido vazio em dias sem pregão. Portanto, o pipeline deve distinguir:

- HTTP_ERROR;
- ZIP_INVALID;
- ZIP_EMPTY;
- ZIP_VALID_WITH_DATA.

## 7. Limitação atual

A ferramenta de pesquisa não executa o download binário diretamente. Assim, os candidatos foram identificados, mas ainda não devem ser registrados como RAW capturado.

## 8. Próximo passo

Executar os candidatos em ambiente HTTP/Python/container, registrar o resultado e, se a rede permitir:

- capturar os ZIPs;
- calcular SHA-256;
- armazenar em dados/calendario_economico/raw ou pasta de mercado apropriada;
- extrair os XMLs;
- identificar WIN/WDO/DI;
- comparar com BVBG.187.01.

## 9. Fonte primária

A existência e finalidade dos arquivos permanecem ancoradas na página oficial Pesquisa por Pregão da B3.

