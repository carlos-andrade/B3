# PARTE03 — AQUISIÇÃO B3 SPRD: STATUS DE CAPTURA V1.1

**Arquivo:** PARTE03_B3_SPRD_AQUISICAO_STATUS_2026-09-24.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Aquisição dos arquivos SPRD do Copom 281  
**Caminho:** docs/ingestao/PARTE03_B3_SPRD_AQUISICAO_STATUS_2026-09-24.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Registrar o estado auditável da tentativa de obtenção dos arquivos históricos SPRD correspondentes aos pregões de 16/09/2026 e 17/09/2026.

## 2. Alvos

- SPRD260916.zip — pregão de 16/09/2026.
- SPRD260917.zip — pregão de 17/09/2026.

Endpoint documentado:

https://www.b3.com.br/pesquisapregao/download?filelist=SPRD<AAMMDD>.zip

## 3. Resultado desta etapa

A aquisição binária não foi confirmada neste ambiente.

Testes realizados:

- acesso direto ao endpoint oficial B3: inacessível pelo mecanismo de navegação disponível;
- busca pública pelos nomes exatos dos arquivos: sem resultado indexado;
- tentativa de consulta a proxy público documentado: endpoint inacessível pelo mecanismo de navegação disponível.

## 4. Regra de evidência

Não foram registrados:

- SHA-256 dos SPRD;
- tamanho de arquivo como evidência primária;
- listagem ZIP;
- XML extraído;
- quantidade de registros;
- preços de WIN/WDO/DI;
- volume;
- número de negócios.

Portanto, nenhum desses campos deve ser tratado como capturado.

## 5. Estado

SPRD 16/09/2026: PENDENTE_CAPTURA_BINARIA.  
SPRD 17/09/2026: PENDENTE_CAPTURA_BINARIA.  
Parser: DISPONÍVEL.  
SHA-256: PENDENTE.  
Dataset normalizado: PENDENTE.  
Negócio a Negócio: PENDENTE.  
Cumulative Delta real: PENDENTE.

## 6. Próxima ação operacional

A aquisição deve ser executada por um ambiente com acesso HTTP ao endpoint B3, preferencialmente via GitHub Actions já preparado no arquivo:

scripts/ingestao/capturar_b3_sprd_copom_2026.yml

O workflow deve preservar os ZIPs e os XMLs extraídos como artefatos. Após a captura, o parser versionado deve ser executado e os hashes registrados no repositório.

## 7. Integridade metodológica

Este documento não transforma URL candidata em dado capturado. A distinção permanece:

URL conhecida != arquivo obtido != dado validado.

