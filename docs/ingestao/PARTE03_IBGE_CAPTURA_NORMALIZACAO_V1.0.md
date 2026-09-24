# PARTE03 — IBGE: CAPTURA RAW E NORMALIZAÇÃO V1.0

**Arquivo:** PARTE03_IBGE_CAPTURA_NORMALIZACAO_V1.0.md
**Projeto:** B3 — A BOLSA DO BRASIL
**Tema:** Primeira camada operacional do calendário econômico
**Data:** 24/09/2026

## Resultado

A primeira captura operacional do calendário conjuntural do IBGE foi estruturada.

A fonte oficial informa, entre outros eventos, IPCA-15 em 25/09/2026, PNAD Contínua mensal em 29/09/2026, IPP em 30/09/2026, PIM-PF em 02/10/2026, INPC e IPCA em 09/10/2026, PMS em 14/10/2026 e PMC em 15/10/2026. citeturn0search0

## Regra de horário

A página consultada fornece a data de divulgação, mas não estabelece no conteúdo capturado um horário intradiário para cada evento. Portanto:

`scheduled_time = null`
`event_time_status = UNKNOWN`

Não será assumido um horário de mercado por convenção.

## NORMALIZED

Os registros receberam:

- `event_id` determinístico;
- nome canônico;
- código do evento;
- período de referência;
- data programada;
- status;
- importância;
- timezone;
- fonte.

## Integridade

O snapshot está versionado como evidência operacional. A captura HTTP direta continuará sendo executada pelo downloader para obter o conteúdo bruto efetivamente recebido e seu SHA-256.

## Próxima etapa

Criar o adaptador de captura direta do calendário IBGE e o teste automático:

`HTTP → RAW → SHA256 → NORMALIZED → schema validation → duplicate detection`

A partir daí, conectar o calendário à agenda de pregões B3.
