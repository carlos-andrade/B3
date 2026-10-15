# PARTE03 — B3 INTRADAY: PADRÃO DE DOWNLOAD CONFIRMADO V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-E34F23DEB3A8 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 91dec2cad93dd2c2a8a7e815f82656bc8842e8e62621a2eaceb8df84cf3a42c7 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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

