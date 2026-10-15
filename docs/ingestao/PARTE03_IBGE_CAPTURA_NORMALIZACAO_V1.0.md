# PARTE03 — IBGE: CAPTURA RAW E NORMALIZAÇÃO V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-66403FC0FF00 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 6ffa1a345cc04b0842cb62e9762eed8ce5b778f5a46818dede57689ba0a125f8 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE03_IBGE_CAPTURA_NORMALIZACAO_V1.0.md
**Projeto:** B3 — A BOLSA DO BRASIL
**Tema:** Primeira camada operacional do calendário econômico
**Data:** 24/09/2026

## Resultado

A primeira captura operacional do calendário conjuntural do IBGE foi estruturada.

O calendário oficial do IBGE informa, entre outros eventos, IPCA-15 em 25/09/2026, PNAD Contínua mensal em 29/09/2026, IPP em 30/09/2026, PIM-PF em 02/10/2026, INPC e IPCA em 09/10/2026, PMS em 14/10/2026 e PMC em 15/10/2026. Fonte: [Calendário de divulgação — IBGE](https://www.ibge.gov.br/calendario-de-divulgacao-novoportal.html).

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
