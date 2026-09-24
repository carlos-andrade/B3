# PARTE04 — BCB/COPOM — CONTRATO DE DADOS V2.1

Arquivo: PARTE04_BCB_COPOM_CONTRATO_DADOS_V2.1.md
Projeto: B3 - A BOLSA DO BRASIL
Tema: contrato auditável de ingestão do Copom
Caminho: docs/ingestao/
Data de criação: 24/09/2026
Repositório: carlos-andrade/B3

## Objetivo

Transformar publicações oficiais do Banco Central em eventos utilizáveis pelo calendário macroeconômico da B3 sem introduzir look-ahead bias.

## Hierarquia temporal

1. `scheduled_date`: data prevista/real da reunião.
2. `published_at`: publicação efetiva do documento.
3. `information_available_at`: primeiro instante em que a informação utilizada pelo modelo estava publicamente disponível.
4. `bar_timestamp`: timestamp do mercado.

Regra de backtest:

`information_available_at <= bar_timestamp`

Nunca substituir `published_at` por `scheduled_date`.

## Eventos

O pipeline deve distinguir pelo menos:

- `COPOM_DECISION`
- `COPOM_MINUTES`
- `COPOM_COMMUNICATION`

A decisão pode ser conhecida pelo Comunicado antes da Ata. Portanto, não usar automaticamente a data da Ata como disponibilidade da decisão.

## RAW

Cada captura deve preservar:

- resposta original;
- URL solicitada;
- URL final;
- timestamp UTC;
- Content-Type;
- tamanho;
- SHA-256.

RAW é imutável. Nova captura cria novo snapshot.

## NORMALIZED

Campos mínimos:

- event_id;
- source;
- source_url;
- event_code;
- meeting_number;
- scheduled_date;
- scheduled_time;
- event_time_status;
- published_at;
- information_available_at;
- status;
- evidências RAW.

Campos econômicos:

- decision_rate_percent_aa;
- decisão textual;
- votos, somente quando efetivamente extraídos;
- referência à Ata;
- referência ao Comunicado.

## Votos

Não inferir votos a partir da taxa final.

O campo de votos permanece `null` até que o parser consiga identificar explicitamente cada membro e seu voto no texto oficial da Ata.

## Controle de qualidade

Falha obrigatória quando:

- evento sem `meeting_number`;
- data inválida;
- duplicidade de `event_id`;
- `EXACT` sem horário;
- voto declarado sem evidência textual;
- taxa inferida sem evidência documental;
- `information_available_at` posterior ao timestamp utilizado no backtest.

## Fonte

O Portal de Dados Abertos do Banco Central disponibiliza listas e detalhes de Atas e Comunicados do Copom por API. A decisão é divulgada no mesmo dia por Comunicado; a Ata é normalmente divulgada na terça-feira seguinte às 08:00. A documentação também informa que todos os membros presentes votam e que os votos são divulgados.

Fonte oficial: Banco Central do Brasil / Portal de Dados Abertos.

## Status

V2.1 — contrato estabelecido.

Próxima etapa: separar decisão, comunicado e ata como eventos independentes e implementar parser de votos com evidência.
