# PARTE03 — NEGÓCIO A NEGÓCIO: ENDPOINT DERIV IDENTIFICADO V1.0

**Arquivo:** PARTE03_NEGOCIO_A_NEGOCIO_ENDPOINT_DERIV_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Endpoint de distribuição do feed tick-by-tick de derivativos  
**Caminho:** docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_ENDPOINT_DERIV_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Descoberta

Foi identificado um endpoint de distribuição utilizado por uma implementação pública atual de coleta de dados B3:

https://drp.b3.com.br/rapinegocios/tickercsv/{YYYY-MM-DD}?type=1

A implementação pública documenta:

- type=1 = DERIV;
- ZIP diário;
- arquivo interno no padrão DD-MM-YYYY_NEGOCIOSAVISTA_DRV.txt.

Fonte independente utilizada para descoberta:
https://github.com/gustavobjorgefo/b3-data-collector

A fonte é independente da B3 e não deve ser tratada como documentação oficial da B3. Ela serve como evidência técnica reproduzível do endpoint observado.

## 2. Datas-alvo

- 2026-09-16;
- 2026-09-17.

## 3. Nome esperado

Para cada data, o pipeline espera:

DD-MM-YYYY_NEGOCIOSAVISTA_DRV.zip

com TXT correspondente dentro do ZIP.

## 4. Escopo

Este feed é o candidato primário para:

- WIN;
- WDO;
- DI1.

A presença efetiva dos contratos deve ser comprovada pela inspeção do arquivo capturado.

## 5. Integridade

A captura obrigatoriamente registra:

- URL;
- arquivo ZIP bruto;
- SHA-256;
- teste de integridade ZIP;
- listagem do ZIP;
- arquivos extraídos;
- tamanho dos arquivos.

## 6. Regra de evidência

A identificação do endpoint não equivale à captura do arquivo.

Estado atual:

Endpoint DERIV identificado: SIM.  
Arquivo 16/09/2026: PENDENTE_CAPTURA.  
Arquivo 17/09/2026: PENDENTE_CAPTURA.  
SHA-256: PENDENTE.  
TXT interno: PENDENTE.  
Layout: PENDENTE.  
Agressor: PENDENTE.

## 7. Workflow

Arquivo:

scripts/ingestao/capturar_b3_negocio_a_negocio_deriv_2026.yml

O workflow baixa as duas datas, valida o ZIP, calcula SHA-256 e publica os artefatos.

