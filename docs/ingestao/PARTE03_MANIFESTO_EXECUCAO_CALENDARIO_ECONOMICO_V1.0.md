# PARTE03 — MANIFESTO DE EXECUÇÃO DO CALENDÁRIO ECONÔMICO V1.0

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

O Banco Central documenta o calendário operacional do Copom e a publicação de comunicado/ata, além de disponibilizar calendário de divulgação do Relatório de Política Monetária. citeturn0search8turn0search4
