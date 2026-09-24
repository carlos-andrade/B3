# PARTE05 — Reconciliação do Calendário COTAHIST 1986

**Arquivo:** PARTE05_COTAHIST_1986_RECONCILIACAO_CALENDARIO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconciliação do calendário observável do COTAHIST 1986  
**Caminho:** docs/ingestao/PARTE05_COTAHIST_1986_RECONCILIACAO_CALENDARIO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Resultado

O RAW contém **248 datas distintas**, de **02/01/1986 a 30/12/1986**. São **247 datas em dias úteis** e uma data em sábado: **26/04/1986**, com apenas 3 registros.

A faixa contém 259 dias de segunda a sexta; portanto, há **12 dias úteis sem observação**.

## Dias úteis ausentes

- **10/02, 11/02, 12/02:** compatíveis com Carnaval/Quarta-feira de Cinzas.
- **28/02 e 03/03:** coincidem com o período de implantação do Plano Cruzado; o fechamento específico da Bovespa ainda requer fonte histórica de mercado.
- **27/03:** véspera da Sexta-feira da Paixão; requer confirmação específica.
- **28/03:** Sexta-feira da Paixão.
- **21/04:** Tiradentes.
- **01/05:** Dia do Trabalho.
- **26/05:** ainda sem explicação independente; requer fonte de mercado.
- **24/12:** véspera de Natal; requer confirmação histórica específica.
- **25/12:** Natal.

O calendário geral de São Paulo confirma as principais datas de Carnaval, Páscoa, Tiradentes, Dia do Trabalho e Natal, mas não substitui um calendário histórico oficial da Bovespa.

## Intervalos longos

1. **07/02 → 13/02:** fim de semana + Carnaval/Quarta-feira de Cinzas.
2. **27/02 → 04/03:** período do Plano Cruzado; fechamento de 28/02 e 03/03 ainda não provado como regra de mercado.
3. **26/03 → 31/03:** Páscoa explica 28–30/03; 27/03 ainda requer confirmação.

## Anomalia de fim de semana

Em **26/04/1986**, o RAW contém:

| Linha | CODBDI | CODNEG | TPMERC | SHA-256 |
|---:|---|---|---|---|
| 50.256 | 62 | SHA 8 | 030 | 5c316e84964bc515bc3dc60ff94ab7cab4a7d7f2291bee0f93c89f4ae79fa73a |
| 50.257 | 96 | MWE 2 | 020 | b348fb54c43c43d4b3c4e33fec385e8156d6976d03225c9dd284496b59049952 |
| 50.258 | 96 | SCP 4 | 020 | 4410e6d22f32e03a9cbab3e519fae8d39758d8540a9d28910169724719852a9d |

Esses registros permanecem no RAW. **26/04 não deve ser promovido automaticamente a pregão válido no NORMALIZED.**

## Status

**CALENDÁRIO 1986 — RECONCILIADO COM RESSALVAS.**

1986 permanece bloqueado para liberação final até:

1. confirmar 28/02 e 03/03;
2. confirmar 27/03;
3. explicar 26/05;
4. confirmar 24/12;
5. classificar economicamente os três registros de 26/04.

## Artefatos

- Resultado: `dados/cotahist/quality/COTAHIST_1986_AUDITORIA_CALENDARIO_V1.json`
- Reconciliação: `dados/cotahist/quality/COTAHIST_1986_RECONCILIACAO_CALENDARIO_V1.json`
- Script: `scripts/ingestao/auditar_calendario_cotahist_1986_v1.py`
- Workflow: `.github/workflows/cotahist-calendario-1986-v1.yml`

RAW SHA-256: `c5fe0a62488595ffb93e4a26752cfc63650e17f88110355becde1d7b5fbe685c`

## Fontes externas de contexto

- Calendário São Paulo 1986: https://calendario.online/calendario-1986-sp.html
- FGV Atlas Histórico — Plano Cruzado: https://atlas.fgv.br/verbete/6297
- Senado Federal — legislação do Plano Cruzado: https://legis.senado.gov.br/norma/527181/publicacao/34620671
