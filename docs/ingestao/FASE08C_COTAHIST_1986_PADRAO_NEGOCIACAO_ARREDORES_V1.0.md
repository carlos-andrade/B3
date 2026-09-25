# FASE 08C — Padrão Interno de Negociação ao Redor dos Dias Ausentes — COTAHIST 1986

**Arquivo:** FASE08C_COTAHIST_1986_PADRAO_NEGOCIACAO_ARREDORES_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Evidência interna de continuidade de atividade antes/depois dos 12 dias úteis sem registros  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Medir o comportamento observável do COTAHIST imediatamente antes e depois dos 12 dias úteis ausentes identificados na FASE 08B.

A análise verifica somente evidência interna do arquivo:
- quantidade de registros tipo 01;
- quantidade distinta de CODBDI;
- quantidade distinta de TPMERC;
- quantidade distinta de CODNEG;
- data observada imediatamente anterior;
- data observada imediatamente posterior;
- janela de até três sessões observadas em cada lado.

## 2. Regra de interpretação

Esta fase **não transforma continuidade estatística em prova de pregão**.

A existência de atividade relevante antes e depois de uma data ausente é apenas evidência compatível com continuidade de cobertura/atividade. A causa da ausência permanece dependente de fonte histórica primária ou institucional.

Também não são usados calendários modernos como substitutos do calendário Bovespa de 1986.

## 3. Métricas

Para cada candidato:
1. identifica a última data observada anterior;
2. identifica a primeira data observada posterior;
3. mede o intervalo calendário entre ambas;
4. registra contagem de registros em cada lado;
5. mede diversidade de CODBDI, TPMERC e CODNEG;
6. registra uma janela de três datas observadas antes e depois;
7. preserva a classificação como não resolvida.

O limiar de 500 registros é apenas um marcador descritivo de atividade ampla dentro desta análise e **não é um limiar de sessão oficial**.

## 4. Saída

O artefato JSON correspondente é:

`dados/cotahist/quality/COTAHIST_1986_PADRAO_NEGOCIACAO_ARREDORES_V1.json`

A análise é reproduzível diretamente sobre o RAW `COTAHIST_A1986.ZIP`.

## 5. Governança

- RAW permanece imutável.
- NORMALIZED permanece imutável.
- Nenhum registro é removido.
- Nenhuma data é criada.
- Nenhum feriado é inferido.
- Nenhum pregão é criado por continuidade estatística.
- O resultado é evidência auxiliar para a FASE 08, não decisão final de calendário.

## 6. Estado

**IMPLEMENTADO:** reconstrução interna do padrão de atividade ao redor dos 12 candidatos.

**PENDÊNCIA:** validação documental histórica de cada data.

**Próxima frente:** consolidar evidência interna com fontes institucionais e preparar a matriz de reconciliação final do calendário 1986.
