# FASE 07F — Colisão residual K4 do COTAHIST 1986

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-C18556E7C4F3 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 68a31cf75283b2f5d1b050c29adce1132b74fd95a50e496d826b424db155f199 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
