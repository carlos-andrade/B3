# CAC, LTV e Churn

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-6C3BB24F4FF1 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 6b7cab18a56704441aa10cbbdda5ebb8e29161d44c2f13b70aac7a774cf4a74c |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Métricas

CAC = despesas de aquisição / novos clientes.

Churn mensal = clientes perdidos no período / clientes no início do período.

LTV simplificado = ARPU x margem de contribuição / churn mensal.

Payback = CAC / contribuição mensal média por cliente.

## Instrumentação

Registrar por cohort: data de aquisição, canal, plano, preço, receita, custo variável, ativação, retenção, churn, expansão, downgrade e motivo de cancelamento.

## Regra de qualidade

Não tratar LTV calculado com amostra pequena como estimativa robusta. Registrar tamanho da amostra, intervalo e limitações.

Status: framework de medição.
