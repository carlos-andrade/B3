# FASE 07F-S — Revisão semântica da colisão K4 do COTAHIST 1986

**Arquivo:** FASE07F_S_COTAHIST_1986_REVISAO_SEMANTICA_K4_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Revisão semântica da única colisão residual K4  
**Caminho:** docs/ingestao/FASE07F_S_COTAHIST_1986_REVISAO_SEMANTICA_K4_V1.0.md  
**Data de criação:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objeto

Revisar semanticamente os dois registros de 10/10/1986 que compartilham a mesma chave K4:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

## 2. Evidência primária

A evidência RAW está em `dados/cotahist/quality/COTAHIST_1986_COLISAO_K4_V1.json`.

Foram encontrados exatamente dois registros consecutivos: linhas RAW 140808 e 140809.

Ambos possuem o mesmo DATA_PREGÃO, CODBDI, CODNEG, TPMERC, CODISI, DIMES, ESPECI, PRAZOT, DATVEN, PREEXE, INDOPC e PTOEXE.

## 3. Diferenças econômicas

**Linha 140808**
- TOTNEG = 1
- QUATOT = 39.000.000
- VOLTOT = 7.410.000
- PREAB/PREMAX/PREMIN/PREMED/PREULT = 190

**Linha 140809**
- TOTNEG = 4
- QUATOT = 190.000.000
- VOLTOT = 35.646.000
- PREAB = 165
- PREMAX = 191
- PREMIN = 165
- PREMED = 187
- PREULT = 175

Os SHA-256 dos registros são diferentes.

## 4. Interpretação

As linhas não são duplicatas byte-a-byte.

K4 é uma chave analítica enriquecida, mas não contém as estatísticas de negociação que diferenciam as duas observações. Portanto, não há base suficiente para somar, escolher ou substituir uma linha pela outra.

A posição consecutiva no RAW é compatível com uma anomalia de origem ou com duas observações históricas que o layout disponível não consegue distinguir temporalmente.

## 5. Classificação

**ANOMALIA DE DUPLICIDADE ESTRUTURAL — SEM RESOLUÇÃO ECONÔMICA**

Não classificar como ativo diferente, erro de preço, correção automática ou registro descartável.

## 6. Regra do pipeline

Até existir evidência histórica independente:

1. preservar as duas linhas;
2. não deduplicar por K4;
3. não agregar as estatísticas;
4. não selecionar arbitrariamente uma das linhas;
5. marcar o par como anomalia de identidade;
6. manter RAW e NORMALIZED inalterados;
7. carregar a anomalia para as fases posteriores de qualidade.

## 7. Estado

A análise de identidade histórica está operacionalmente completa. A colisão K4 permanece como anomalia residual documentada, sem correção dos dados.

**Conclusão:** FASE 07 encerrável com anomalia residual rastreável para auditoria.
