# PARTE03 — BCB/COPOM — RECONCILIAÇÃO DA 281ª REUNIÃO V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-CF8C551D777D |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a0e8c509f76e8103b766f597d8158cf95ca43ef217a4d2e1aa4ca8b8c3fc7e32 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE03_BCB_COPOM_281_RECONCILIACAO_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Tema:** Copom 281 — decisão, Ata, informação disponível e integração B3
**Caminho:** docs/ingestao/
**Data:** 24/09/2026
**Repositório:** carlos-andrade/B3

## Reconciliação oficial

- Reunião: 281ª
- Sessões: 15 e 16/09/2026
- Meta anterior: 14,00% a.a.
- Nova meta: 13,75% a.a.
- Vigência: 17/09/2026
- Votação: 7 a favor / 0 contra
- Ata: publicada em 22/09/2026
- Horário exato da publicação da Ata: UNKNOWN — sem timestamp oficial comprovado
- RAW da API — Ata 281: CAPTURADO; `dados/calendario_economico/copom/raw/atas_detalhes_281.json`; SHA-256 `fa402b27a6424c01d96fccce81f58347cc35dcb390e23d1fa31f2207792eba98`; 19.791 bytes
- RAW da API — Comunicado 281: CAPTURADO; `dados/calendario_economico/copom/raw/comunicados_detalhes_281.json`; SHA-256 `c32e5fccaba8d550544472f72f03222eb880fbb543674f77eb89d565d4dc9b66`; 6.503 bytes
- Listas oficiais de Atas/Comunicados: CAPTURADAS com sidecars SHA-256; ver `dados/calendario_economico/copom/raw/*.meta.json`
- PDF binário original da Ata: PENDENTE — a resposta JSON/API não é o PDF binário

## Votantes

Gabriel Muricca Galípolo; Ailton de Aquino Santos; Gilneu Francisco Astolfi Vivan; Izabela Moreira Correa; Nilton José Schneider David; Paulo Picchetti; Rodrigo Alves Teixeira.

## Controle temporal

A decisão somente entra no estado informacional a partir da divulgação em 16/09/2026. A Ata somente entra a partir de 22/09/2026. Horários exatos permanecem UNKNOWN até evidência documental.

## Integração B3

Após captura HTTP integral:
1. associar decisão à sessão B3 de 16/09/2026;
2. registrar timestamp real do Comunicado;
3. associar Ata à sessão B3 de 22/09/2026;
4. medir janelas intraday pós-evento;
5. separar reação ao Comunicado da reação posterior à Ata.

## Limitação

A captura foi executada pelo workflow [Capturar BCB - Copom](https://github.com/carlos-andrade/B3/actions/runs/38889256929), concluído com sucesso em 2026-10-16. O workflow capturou as respostas JSON da API, persistiu os sidecars com URL, timestamp, bytes e SHA-256 e validou `copom_281.json` (`OK: 1 eventos BCB/Copom validados`). O PDF binário continua pendente e o horário exato de publicação continua `UNKNOWN`; não inferir esses valores.
