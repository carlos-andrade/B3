# PARTE03 — BCB/COPOM — CONTRATO DE INGESTÃO V1.0

Arquivo: PARTE03_BCB_COPOM_CONTRATO_V1.0.md
Projeto: B3 - A BOLSA DO BRASIL
Tema: Banco Central do Brasil / Copom / política monetária
Caminho: docs/ingestao/
Data de criação: 24/09/2026
Repositório: carlos-andrade/B3

## Objetivo

Modelar eventos e documentos do Banco Central do Brasil relevantes para a ingestão macroeconômica da B3, com prioridade para Copom, Selic, Comunicados, Atas, Questionário Pré-Copom e Relatório de Política Monetária (RPM).

## Fontes primárias

1. Página oficial do Copom.
2. Portal de Dados Abertos do BCB — conjunto "Documentos do Copom".
3. API oficial do BCB para documentos do Copom.
4. Histórico oficial das taxas de juros básicas.
5. Página oficial do RPM e seu calendário de divulgação.

## Granularidade

Cada evento deve preservar:
- reunião do Copom;
- primeira e segunda sessão;
- horário/data de divulgação do Comunicado;
- data/hora de publicação da Ata;
- decisão/meta Selic;
- vigência da meta;
- resultado da votação quando disponível;
- RPM e data de publicação;
- QPC e data de publicação;
- URL da fonte;
- data/hora de captura;
- hash da evidência;
- status de tempo.

## Campos mínimos

event_id
source
source_url
event_name
event_code
meeting_number
meeting_session
scheduled_date
scheduled_time
timezone
event_time_status
reference_period
actual_value
previous_value
revised_value
consensus_value
selic_target_pct
selic_effective_start
vote_result
importance
status
retrieved_at
source_hash
evidence_path

## Regras temporais

- Timezone canônico: America/Sao_Paulo.
- Nunca transformar uma data de reunião em horário de divulgação sem evidência oficial.
- Comunicado: registrar o horário efetivamente publicado; quando apenas a regra institucional estiver disponível, marcar como APPROXIMATE.
- Ata: registrar 08:00 somente quando a fonte oficial suportar a regra/calendário; caso contrário, UNKNOWN.
- Para backtest, uma informação só pode entrar no estado do mercado depois do timestamp de publicação observado.
- Não usar Selic futura ou conteúdo de Ata antes da publicação.
- Revisões posteriores não podem retroagir sobre o dataset histórico de informação disponível no instante do evento.

## Eventos prioritários

COPOM_MEETING
COPOM_DECISION
COPOM_COMMUNICADO
COPOM_ATA
COPOM_QPC
COPOM_RPM
SELIC_TARGET

## Uso quantitativo futuro

Os eventos serão ligados a pregões e séries intraday da B3 para estudar:
- gap de abertura;
- retorno e volatilidade pré/pós-Copom;
- volume financeiro;
- agressão;
- Cumulative Delta;
- VWAP/TWAP;
- DOL/WIN;
- curva de juros;
- reação em janelas de 5m, 15m, 30m, 60m e sessão;
- surpresa de decisão versus expectativa disponível antes do evento.

O pipeline deve separar fato observado, expectativa pré-evento e interpretação posterior.
