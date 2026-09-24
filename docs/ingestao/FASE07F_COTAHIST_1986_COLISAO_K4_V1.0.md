# FASE 07F — Colisão residual K4 do COTAHIST 1986

**Arquivo:** FASE07F_COTAHIST_1986_COLISAO_K4_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Investigação da única colisão residual da chave contratual K4  
**Caminho:** docs/ingestao/FASE07F_COTAHIST_1986_COLISAO_K4_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Investigar os dois registros que permanecem no mesmo grupo da chave K4.

K4 = DATA_PREGÃO + CODBDI + CODNEG + TPMERC + CODISI + DIMES + ESPECI + PRAZOT + DATVEN + PREEXE + INDOPC + PTOEXE.

## 2. Offsets oficiais utilizados

Após reconciliação com o layout oficial B3:

- PREEXE: 189–201;
- INDOPC: 202;
- DATVEN: 203–210;
- FATCOT: 211–217;
- PTOEXE: 218–230;
- CODISI: 231–242;
- DIMES: 243–245.

FATCOT não integra a K4, mas foi preservado na inspeção completa dos registros.

## 3. Colisão

19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0

Foram encontrados exatamente 2 registros.

## 4. Método

O analisador percorre o RAW, seleciona registros tipo 01, reconstrói o prefixo K4 conhecido, recupera os registros completos, calcula SHA-256 e compara os campos.

A seleção por prefixo foi usada para evitar falsos negativos decorrentes de diferenças de representação entre versões históricas do parser. Os campos completos foram então preservados para inspeção.

## 5. Resultado validado

Arquivo:

dados/cotahist/quality/COTAHIST_1986_COLISAO_K4_V1.json

Workflow validado:

- run: 36038214156;
- conclusão: success;
- publicação da evidência: commit af2f398;
- match_count: 2;
- linhas RAW: 140808 e 140809.

Os dois registros possuem o mesmo K4, mas diferem em:

- TOTNEG;
- QUATOT;
- VOLTOT;
- PREAB;
- PREMAX;
- PREMIN;
- PREMED;
- PREULT.

Os hashes SHA-256 também são diferentes.

## 6. Regra de classificação

Coincidência de K4 não é tratada automaticamente como duplicidade econômica.

A conclusão do artefato é:

REQUIRES_SEMANTIC_REVIEW

A fase 07 não exclui, corrige ou substitui nenhum dos dois registros.

## 7. Governança

RAW e NORMALIZED permanecem inalterados.

**Próxima frente:** investigação semântica histórica da anomalia K4.
