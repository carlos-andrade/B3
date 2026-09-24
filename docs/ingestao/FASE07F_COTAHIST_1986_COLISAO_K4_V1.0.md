# FASE 07F — Colisão residual K4 do COTAHIST 1986

**Arquivo:** FASE07F_COTAHIST_1986_COLISAO_K4_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Investigação da única colisão residual da chave contratual K4  
**Caminho:** docs/ingestao/FASE07F_COTAHIST_1986_COLISAO_K4_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo
Investigar os dois registros que permanecem no mesmo grupo da chave K4.

K4 = DATA_PREGÃO + CODBDI + CODNEG + TPMERC + CODISI + DIMES + ESPECI + PRAZOT + DATVEN + PREEXE + INDOPC + PTOEXE.

## Colisão conhecida
19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0.0 | 0 | 0.0

A auditoria anterior registrou 2 registros neste grupo.

## Método
O analisador percorre o RAW, seleciona registros tipo 01, reconstrói K4, recupera os registros completos, calcula SHA-256 e compara os campos.

## Regra
Coincidência de K4 não será tratada automaticamente como duplicidade. A classificação dependerá das diferenças objetivas encontradas no registro completo.

## Governança
RAW e NORMALIZED permanecem inalterados.

**Resultado esperado:** dados/cotahist/quality/COTAHIST_1986_COLISAO_K4_V1.json

## Próxima frente
07G — Matriz Final de Identidade Histórica 1986.
