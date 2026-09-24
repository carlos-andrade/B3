# PARTE03 — CONTRATO DE INGESTÃO DO CALENDÁRIO ECONÔMICO B3 V1.0

**Arquivo:** PARTE03_CALENDARIO_ECONOMICO_CONTRATO_V1.0.md  
**Projeto:** B3 — A BOLSA DO BRASIL  
**Tema:** Calendário econômico para ingestão, auditoria e backtest  
**Caminho:** docs/ingestao/PARTE03_CALENDARIO_ECONOMICO_CONTRATO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Criar uma camada de calendário econômico independente do COTAHIST, capaz de registrar eventos macroeconômicos relevantes para a B3 e associá-los temporalmente às sessões de mercado.

O calendário será tratado como **dado de evento**, não como indicador técnico.

## 2. Princípios

1. Fonte primária oficial sempre que existir.
2. RAW preservado antes de qualquer transformação.
3. NORMALIZED com esquema estável e auditável.
4. Nenhum valor de consenso, realizado ou revisão será inventado.
5. Data de publicação, horário do evento, período de referência e timestamp de ingestão são campos distintos.
6. Timezone explícito; padrão operacional: America/Sao_Paulo.
7. Eventos sem horário conhecido permanecem válidos, porém com `event_time_status=UNKNOWN`.
8. Alterações posteriores devem gerar nova evidência/versionamento, nunca sobrescrever silenciosamente o RAW anterior.
9. Backtest só pode utilizar informação que estivesse disponível no instante histórico do evento.

## 3. Fontes prioritárias

### Tier 1 — oficiais

- IBGE: calendário de divulgações e indicadores conjunturais.
- Banco Central do Brasil: Copom, decisões, atas, Relatório de Política Monetária e demais calendários oficiais.
- B3: calendário de pregões e eventos próprios, quando aplicável.
- Tesouro Nacional e demais órgãos oficiais, quando o evento possuir impacto operacional relevante.

### Tier 2 — fontes institucionais auxiliares

Utilizadas somente quando o evento não possuir fonte oficial estruturada suficiente. A fonte e a justificativa devem ser registradas.

### Tier 3 — agregadores

Não são fonte primária do dataset canônico. Podem ser usados para descoberta e reconciliação, nunca para substituir uma fonte oficial disponível.

## 4. Esquema NORMALIZED mínimo

| Campo | Obrigatório | Descrição |
|---|---:|---|
| event_id | SIM | ID determinístico do evento |
| source | SIM | Fonte institucional |
| source_url | SIM | URL de origem |
| event_name | SIM | Nome canônico |
| event_code | NÃO | Código oficial, quando existir |
| country | SIM | País |
| currency | NÃO | Moeda relacionada |
| reference_period | NÃO | Período do indicador |
| scheduled_date | SIM | Data prevista |
| scheduled_time | NÃO | Horário previsto |
| timezone | SIM | Fuso do horário |
| event_time_status | SIM | EXACT / APPROXIMATE / UNKNOWN |
| actual_value | NÃO | Valor divulgado |
| previous_value | NÃO | Valor anterior |
| revised_value | NÃO | Valor revisado |
| consensus_value | NÃO | Consenso, somente se houver fonte verificável |
| importance | SIM | LOW / MEDIUM / HIGH |
| status | SIM | SCHEDULED / RELEASED / CANCELLED / REVISED |
| retrieved_at | SIM | Momento da ingestão |
| source_hash | SIM | Hash da evidência RAW |
| evidence_path | SIM | Caminho do RAW |

## 5. Regras para trading e backtest

O dataset deve permitir construir janelas:

- pré-evento;
- instante do evento;
- pós-evento imediato;
- pós-evento estendido.

O motor de backtest deverá impedir look-ahead bias. Um evento só pode influenciar uma decisão depois do seu timestamp de disponibilização.

## 6. Primeira família de eventos

A ingestão inicial priorizará:

- IPCA;
- IPCA-15;
- INPC;
- PNAD Contínua;
- PIB;
- produção industrial;
- comércio;
- serviços;
- decisões do Copom/Selic;
- atas do Copom;
- Relatório de Política Monetária;
- outros eventos oficiais com potencial relevância para juros, câmbio e índice.

## 7. Histórico

A regra histórica do projeto continua sendo **1986 → mais recente** para dados de mercado. Para calendário econômico, o período histórico será limitado pela disponibilidade comprovável de cada fonte. A ausência de uma série histórica não será preenchida por estimativa.

## 8. Critério de aceite

A ingestão somente será considerada pronta quando:

- RAW puder ser reproduzido;
- NORMALIZED puder ser regenerado;
- cada registro possuir evidência;
- timestamps estiverem normalizados;
- duplicidades forem detectáveis;
- revisões forem preservadas;
- o calendário puder ser reconciliado com sessões B3;
- testes automatizados estiverem documentados.
