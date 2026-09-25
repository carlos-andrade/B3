# FASE 08A — Matriz Canônica Provisória do Calendário COTAHIST 1986

**Arquivo:** FASE08A_COTAHIST_1986_MATRIZ_CALENDARIO_PROVISORIA_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação histórica das sessões de negociação de 1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Transformar a auditoria observável do COTAHIST 1986 em uma matriz diária auditável, separando **observação do arquivo**, **fim de semana** e **dia útil ainda sem fonte histórica suficiente**.

Esta fase não cria um calendário histórico por inferência.

## 2. Evidência de partida

O RAW contém 248 datas distintas entre 02/01/1986 e 30/12/1986, sendo 247 em dias úteis e uma ocorrência em sábado (26/04/1986). O artefato de auditoria registra 177.981 registros tipo 01 e preserva o SHA do RAW.

A matriz usa esse artefato como fonte de observação e não altera RAW ou NORMALIZED.

## 3. Regra de classificação

| Status | Regra |
|---|---|
| OBSERVADA_COTAHIST | Existe registro tipo 01 na data |
| NAO_SESSAO_FIM_DE_SEMANA | Sábado/domingo sem tratar isso como prova histórica de pregão |
| PENDENTE_FONTE_HISTORICA | Dia útil sem registro; exige fonte histórica aplicável à Bovespa de 1986 |

Um dia útil ausente **não** é classificado como feriado, suspensão, ausência de ingestão ou pregão cancelado sem evidência documental.

## 4. Candidatos atuais

A auditoria existente identifica 12 dias úteis sem observação:

- 10/02/1986
- 11/02/1986
- 12/02/1986
- 28/02/1986
- 03/03/1986
- 27/03/1986
- 28/03/1986
- 21/04/1986
- 01/05/1986
- 26/05/1986
- 24/12/1986
- 25/12/1986

A classificação acima permanece **PENDENTE_FONTE_HISTORICA** nesta matriz, mesmo quando a data coincide com feriado conhecido no calendário civil. Isso evita retroprojetar o calendário moderno para a Bovespa de 1986.

## 5. Anomalia preservada

26/04/1986 permanece como data observada no RAW, apesar de sábado. Seus três registros continuam preservados como anomalia de data:

- linha 50256: CODBDI 62 / SHA 8 / TPMERC 030;
- linha 50257: CODBDI 96 / MWE 2 / TPMERC 020;
- linha 50258: CODBDI 96 / SCP 4 / TPMERC 020.

A matriz não remove, corrige ou promove esses registros a sessão válida.

## 6. Fonte institucional

A B3 mantém uma página oficial de calendário de negociação e informa que o calendário é segmentado por atividade e segmento de mercado. Isso sustenta a regra metodológica de não converter automaticamente um calendário civil em calendário de negociação. citeturn0search0

Para 1986, porém, a fonte pública atualmente recuperada não fornece o calendário diário histórico necessário para fechar os 12 candidatos.

## 7. Estado

**IMPLEMENTADO:** matriz diária provisória e regra de governança.

**NÃO RESOLVIDO:** calendário oficial/histórico diário da Bovespa para 1986.

**BLOQUEIO DE FECHAMENTO:** os 12 dias úteis candidatos e a anomalia de 26/04/1986 exigem evidência histórica específica antes de serem classificados definitivamente.

## 8. Próxima ação

Prioridade probatória:

1. recuperar calendário/boletim Bovespa de 1986;
2. validar 10–12/02, 28/02, 03/03, 27–28/03, 21/04, 01/05, 26/05 e 24–25/12;
3. explicar a ocorrência de 26/04;
4. produzir calendário canônico definitivo com fonte e hash por evidência.

## Artefatos

- Script: `scripts/ingestao/construir_matriz_calendario_1986_v1.py`
- Resultado: `dados/cotahist/quality/COTAHIST_1986_MATRIZ_CALENDARIO_PROVISORIA_V1.json`
- Workflow: `.github/workflows/cotahist-fase08a-matriz-calendario-1986-v1.yml`

**Regra:** nenhum dado histórico é inventado para preencher lacunas.
