# PARTE03 — B3 SPRD: ESPECIFICAÇÃO DE PARSER E VALIDAÇÃO V1.0

**Arquivo:** PARTE03_B3_SPRD_PARSER_VALIDACAO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Parser inicial dos arquivos SPRD e validação de integridade  
**Caminho:** docs/ingestao/PARTE03_B3_SPRD_PARSER_VALIDACAO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Criar a primeira camada versionada para transformar os arquivos históricos SPRD da B3 em dados normalizados, sem confundir o boletim consolidado com negócio a negócio.

## 2. Entrada

O parser aceita um ou mais arquivos ZIP oficiais já capturados. A captura deve ocorrer antes da execução do parser.

Validações obrigatórias:

- arquivo existente;
- ZIP estruturalmente válido;
- leitura sem corrupção;
- suporte a ZIP aninhado;
- identificação de XML;
- SHA-256 do arquivo de entrada.

## 3. Saída inicial

CSV normalizado com:

- trading_date;
- instrument;
- ticker;
- price;
- quantity;
- financial_volume;
- source_file.

A saída é deliberadamente mínima nesta versão porque os layouts XML podem variar entre versões.

## 4. Escopo de instrumentos

O parser procura inicialmente:

- WIN — futuro de Ibovespa;
- WDO — futuro de dólar;
- DI1 — futuro de DI.

O contrato não deve ser inferido apenas pelo prefixo. O cadastro de instrumentos deverá resolver vencimento, código completo e identificadores quando os XMLs forem efetivamente capturados.

## 5. Regra crítica de microestrutura

O SPRD é tratado nesta etapa como fonte consolidada/EOD.

Portanto:

- não gera agressor-side real;
- não gera Cumulative Delta real;
- não classifica comprador/vendedor por regra de preço;
- não substitui Negócio a Negócio;
- não deve ser usado para afirmar fluxo institucional intraday.

Qualquer proxy futuro deverá ser identificado como PROXY, nunca como delta real.

## 6. Controle de integridade

Cada execução registra:

- timestamp UTC da execução;
- SHA-256 dos ZIPs;
- quantidade de linhas produzidas;
- caminho da saída;
- ausência explícita de agressor-side e Cumulative Delta.

## 7. Próxima camada

Depois da captura efetiva dos SPRD de 16/09/2026 e 17/09/2026:

1. executar o parser;
2. validar datas e símbolos;
3. reconciliar preços/quantidades com fonte oficial;
4. construir dataset EOD;
5. localizar e capturar Negócio a Negócio;
6. criar parser específico para trades;
7. classificar agressão somente quando o campo/evidência permitir;
8. calcular Cumulative Delta real;
9. só então construir as janelas PRE/EVENTO/POST do Copom 281.

## 8. Estado em 24/09/2026

Parser versionado: SIM.  
SPRD 16/09/2026 capturado: PENDENTE.  
SPRD 17/09/2026 capturado: PENDENTE.  
SHA-256 dos arquivos: PENDENTE.  
Dataset EOD normalizado: PENDENTE.  
Negócio a Negócio: PENDENTE.  
Cumulative Delta real: PENDENTE.

## 9. Arquivo de implementação

scripts/ingestao/parsear_b3_sprd_v1.py

Commit da implementação: b161d3b25880597c352121aa14c992102c52197c.
