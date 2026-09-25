# FASE 08B — Matriz de Evidência dos Dias Úteis Ausentes — COTAHIST 1986

**Arquivo:** FASE08B_COTAHIST_1986_EVIDENCIA_DIAS_UTEIS_AUSENTES_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação histórica dos dias úteis sem observação no COTAHIST 1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Consolidar, em uma matriz auditável, os 12 dias úteis sem registros tipo 01 identificados na auditoria do COTAHIST 1986, distinguindo:

- fato observado no RAW;
- contexto civil;
- evidência institucional;
- hipótese;
- estado de resolução.

A matriz não transforma feriado civil em feriado de bolsa sem evidência específica.

## 2. Dias candidatos

| Data | Observação COTAHIST | Estado |
|---|---|---|
| 10/02/1986 | 0 registros | PENDENTE |
| 11/02/1986 | 0 registros | PENDENTE |
| 12/02/1986 | 0 registros | PENDENTE |
| 28/02/1986 | 0 registros | PENDENTE |
| 03/03/1986 | 0 registros | PENDENTE |
| 27/03/1986 | 0 registros | PENDENTE |
| 28/03/1986 | 0 registros | PENDENTE |
| 21/04/1986 | 0 registros | PENDENTE |
| 01/05/1986 | 0 registros | PENDENTE |
| 26/05/1986 | 0 registros | PENDENTE |
| 24/12/1986 | 0 registros | PENDENTE |
| 25/12/1986 | 0 registros | PENDENTE |

## 3. Evidência atualmente disponível

A auditoria do COTAHIST comprova apenas a ausência de registros tipo 01 nessas datas.

A B3 mantém atualmente calendário de negociação estruturado por segmento/atividade; isso não constitui, por si só, prova do calendário Bovespa de 1986.

O Centro de Memória B3 informa possuir acervo histórico superior a 100.000 itens e disponibilizar pesquisa digital ou presencial mediante agendamento. Essa é uma fonte institucional diretamente pertinente à recuperação do calendário/BDI histórico. citeturn0search0

A CVM mantém arquivos e canais institucionais de acesso à informação, mas a pesquisa pública realizada nesta fase não localizou um calendário Bovespa diário de 1986 aplicável aos 12 casos. citeturn0search1turn0search13

## 4. Classificação metodológica

Nenhuma das 12 datas será classificada definitivamente como:

- feriado Bovespa;
- suspensão de negociação;
- pregão cancelado;
- falha de ingestão;
- ausência de arquivo.

sem documentação histórica específica.

Mesmo quando a data coincide com um feriado civil conhecido, a classificação final permanece **PENDENTE**.

## 5. Caso especial — 26/04/1986

26/04/1986 é diferente dos 12 candidatos: existe observação no RAW, apesar de ser sábado.

Foram preservados três registros:

- linha 50256 — CODBDI 62 / SHA 8 / TPMERC 030;
- linha 50257 — CODBDI 96 / MWE 2 / TPMERC 020;
- linha 50258 — CODBDI 96 / SCP 4 / TPMERC 020.

A existência desses registros não prova que 26/04 tenha sido pregão regular. Também não autoriza sua remoção.

## 6. Resultado

A FASE 08B não encerra nenhum dos 12 casos.

Estado atual:

**12 dias úteis = PENDENTE_FONTE_HISTORICA**

**26/04/1986 = ANOMALIA_DE_DATA_OBSERVADA**

## 7. Governança

- RAW permanece imutável.
- NORMALIZED permanece imutável.
- Nenhuma data é criada.
- Nenhuma data é excluída.
- Nenhum feriado é inferido por calendário moderno.
- Toda classificação futura deverá apontar para fonte histórica identificável.

## 8. Próxima frente

A investigação deve priorizar material institucional primário: BDI de 1986, calendário histórico da Bovespa, circulares e manuais de negociação.

A prioridade é obter evidência documental para cada uma das 12 datas e, separadamente, explicar a origem dos três registros de 26/04.

## 9. Estado

**IMPLEMENTADO:** matriz metodológica dos 12 dias ausentes.

**NÃO RESOLVIDO:** classificação histórica definitiva.

**BLOQUEIO:** ausência de calendário/BDI primário verificável para 1986.
