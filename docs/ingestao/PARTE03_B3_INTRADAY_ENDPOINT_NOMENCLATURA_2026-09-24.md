# PARTE03 — B3 INTRADAY: ENDPOINT E NOMENCLATURA CONFIRMADOS V1.0

**Arquivo:** PARTE03_B3_INTRADAY_ENDPOINT_NOMENCLATURA_2026-09-24.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Confirmação independente do endpoint e dos identificadores de arquivos  
**Caminho:** docs/ingestao/PARTE03_B3_INTRADAY_ENDPOINT_NOMENCLATURA_2026-09-24.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Nova evidência

Foi localizada documentação pública atual de uma biblioteca que acessa diretamente os arquivos oficiais da B3 e confirma o padrão:

`https://www.b3.com.br/pesquisapregao/download?filelist=<PREFIXO><YYMMDD>.zip`

Para o Simplified Price Report de derivativos:

`SPRD<YYMMDD>.zip`

A mesma documentação descreve o conteúdo como ZIP com XML bruto da B3.

Fonte técnica independente:
https://crdcj.github.io/PYield/b3/

## 2. Confirmação adicional

Outra implementação pública recente utiliza exatamente:

`https://www.b3.com.br/pesquisapregao/download?filelist=SPRD<YYMMDD>.zip`

para obter o Price Report simplificado.

Isso reforça que o padrão identificado anteriormente não é apenas uma hipótese baseada em nomenclatura.

## 3. Aplicação aos pregões-alvo

16/09/2026:

`SPRD260916.zip`

17/09/2026:

`SPRD260917.zip`

URL estrutural:

`https://www.b3.com.br/pesquisapregao/download?filelist=SPRD260916.zip`

e

`https://www.b3.com.br/pesquisapregao/download?filelist=SPRD260917.zip`

## 4. O que foi confirmado

ENDPOINT_PATTERN = CONFIRMED  
SPRD_NAMING = CONFIRMED  
XML_INSIDE_ZIP = CONFIRMED  
DATE_ENCODING = YYMMDD

## 5. O que continua pendente

BINARY_CAPTURE = PENDING

Não há SHA-256, tamanho ou conteúdo dos dois arquivos-alvo no repositório.

## 6. Consequência

A camada de aquisição está suficientemente especificada para executar uma captura fora do ambiente que bloqueia o domínio B3.

Assim que o binário estiver disponível, o pipeline já possui:

- capturador RAW;
- metadata;
- SHA-256;
- especificação de normalização;
- contrato de instrumentos;
- regras de validação;
- janela Copom 281.

## 7. Observação metodológica

O SPRD é adequado para validar preços/indicadores do boletim, mas não deve ser interpretado como substituto automático do negócio a negócio para agressão e Cumulative Delta.

## 8. Estado

Endpoint = CONFIRMADO  
Nomenclatura = CONFIRMADA  
Arquivo 16/09 = NÃO CAPTURADO  
Arquivo 17/09 = NÃO CAPTURADO  
Microestrutura = PENDENTE
