# PARTE03 — MANIFESTO DE EXECUÇÃO DO CALENDÁRIO ECONÔMICO V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-E228702E80D0 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 3f656cfc5a0d1f515c3ba236102192234d9b82d84c81715318a9eb7aae05195d |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE03_MANIFESTO_EXECUCAO_CALENDARIO_ECONOMICO_V1.0.md  
**Projeto:** B3 — A BOLSA DO BRASIL  
**Tema:** Estado da execução da ingestão do calendário econômico  
**Caminho:** docs/ingestao/PARTE03_MANIFESTO_EXECUCAO_CALENDARIO_ECONOMICO_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Estado

**FASE:** PARTE03 — CALENDÁRIO ECONÔMICO  
**STATUS:** ESTRUTURA INICIAL CRIADA  
**PRÓXIMO BLOCO:** captura RAW oficial → parser específico por fonte → NORMALIZED → reconciliação com sessões B3.

## Commits desta etapa

- `409210e6d141ba2685de64816414453b64127cf3` — contrato de ingestão.
- `b0d415ae5e47afc12c2d884a94374377a1d938df` — ingestidor RAW genérico.
- `46b8376a07a184e9c100fb5e41e8cdbc2711f01c` — matriz de fontes.

## Regra de arquitetura

O calendário econômico não será misturado ao COTAHIST. São domínios diferentes:

`COTAHIST` → mercado/preço/volume  
`CALENDARIO_ECONOMICO` → eventos/tempo/divulgação/revisão

A integração ocorrerá posteriormente por timestamp e sessão.

## Prioridade operacional

1. IBGE — calendário conjuntural.
2. Banco Central — Copom e política monetária.
3. Calendário de pregões B3.
4. Demais órgãos oficiais.
5. Reconciliação e auditoria.
6. Camada de features para backtest.

## Regra crítica para o setup

O calendário não será usado como "sinal" isolado. Ele será uma variável temporal/contextual para identificar regimes de risco, janelas de evento e possíveis alterações de microestrutura.

Qualquer uso em estratégia deverá distinguir claramente:

- evento conhecido antecipadamente;
- evento divulgado;
- valor realizado;
- revisão posterior;
- reação do preço após a divulgação.

Isso evita look-ahead bias.

## Evidência externa utilizada nesta etapa

IBGE mantém calendário de indicadores conjunturais e páginas específicas por indicador. Em 2026, por exemplo, o calendário oficial lista IPCA-15 em 25/09/2026, PNAD Contínua mensal em 29/09/2026 e IPCA em 09/10/2026. citeturn0search1turn0search7

O Banco Central documenta o calendário operacional do Copom e a publicação de comunicados/atas em [Comunicados do Copom — BCB](https://www.bcb.gov.br/controleinflacao/comunicadoscopom) e [Atas do Copom — BCB](https://www.bcb.gov.br/controleinflacao/atascopom). O calendário de divulgação do Relatório de Política Monetária deve ser consultado na fonte oficial correspondente antes da captura.
