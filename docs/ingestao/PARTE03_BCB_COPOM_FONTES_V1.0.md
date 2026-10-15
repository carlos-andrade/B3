# PARTE03 — BCB/COPOM — FONTES OFICIAIS V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-937957C66A34 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 0af38cabb0556a40e564f049df11ff54a34846282262e2e8257b8e7496367925 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Arquivo: PARTE03_BCB_COPOM_FONTES_V1.0.md
Projeto: B3 - A BOLSA DO BRASIL
Tema: matriz de fontes oficiais do Banco Central
Caminho: docs/ingestao/
Data de criação: 24/09/2026
Repositório: carlos-andrade/B3

| Domínio | Fonte primária | Uso |
|---|---|---|
| Copom | BCB — Comitê de Política Monetária | calendário, reuniões, atas e comunicados |
| Documentos | Portal Dados Abertos BCB — Documentos do Copom | API/listas de atas e comunicados |
| Selic | BCB — Histórico das taxas de juros básicas | decisão, vigência e histórico da meta |
| QPC | BCB — Questionário Pré-Copom | expectativas e informações pré-reunião |
| RPM | BCB — Relatório de Política Monetária | cenário e projeções trimestrais |

## Evidência oficial verificada em 24/09/2026

A página do Copom apresenta, para 2026, a reunião de setembro em 15–16/09, a Ata em 22/09 às 11:00, o RPM do 3º trimestre em 24/09 às 11:00, além das reuniões de novembro e dezembro. O Portal de Dados Abertos informa que os documentos do Copom possuem API oficial e que as atas são normalmente publicadas na terça-feira da semana seguinte às 08:00. A regra institucional também registra a divulgação do Comunicado após a segunda sessão, a partir das 18:00. 

## Histórico Selic 2026 verificado

O histórico oficial registra:
- 276ª: 28/01/2026 — 15,00% a.a.
- 277ª: 18/03/2026 — 14,75% a.a.
- 278ª: 29/04/2026 — 14,50% a.a.
- 279ª: 17/06/2026 — 14,25% a.a.
- 280ª: 05/08/2026 — 14,00% a.a.

A decisão deve ser modelada como evento com data de decisão e início de vigência, não apenas como valor anual.

## Política de fonte

Fonte secundária não substitui BCB para decisão, data ou horário quando o dado oficial estiver disponível.
