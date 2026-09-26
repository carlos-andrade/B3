# CARTA DE GARANTIA DE ATUALIZAÇÃO DOS DADOS

**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** carlos-andrade/B3  
**Data da verificação:** 26/09/2026  
**Status:** **NÃO CERTIFICADA — PENDÊNCIA DE FRESCOR**

## 1. Objeto

Este documento estabelece a evidência auditável sobre a atualidade dos datasets mantidos no repositório. A finalidade é impedir que o projeto declare cobertura temporal integral sem comprovação documental.

## 2. Resultado da verificação

A verificação realizada em 26/09/2026 **não autoriza declarar que todos os últimos dados da B3 disponíveis até a data corrente já foram baixados**.

O motivo objetivo é o COTAHIST: o dataset oficial do projeto foi regenerado em 26/09/2026, porém o registro de 2026 informa **última data de mercado = 22/09/2026**. Portanto, a data de geração do dataset não pode ser confundida com a última data de pregão efetivamente ingerida.

### Evidência COTAHIST

- Dataset: `COTAHIST_OFICIAL` V1.0
- Arquivo: `dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json`
- Geração declarada: **2026-09-26**
- Período: **1986–2026**
- Última data de mercado no registro de 2026: **2026-09-22**
- Arquivo bruto de 2026: `dados/cotahist/raw/anual/COTAHIST_A2026.ZIP`
- Status de falha controlada: `fail_closed=true`
- Exceção histórica: 1986 permanece explicitamente marcada como exceção semântica controlada.

### Evidência Copom / BCB

- Captura RAW + NORMALIZED registrada em **25/09/2026**.
- Reunião mais recente registrada: **281ª reunião**, realizada em **15 e 16/09/2026**.
- A existência de captura recente não significa que todos os demais indicadores econômicos necessários ao projeto estejam atualizados; cada série deverá possuir seu próprio registro de frescor.

## 3. Critério de garantia

A garantia integral somente será emitida quando a matriz de frescor demonstrar, para cada dataset obrigatório:

`ultima_data_fonte <= ultima_data_armazenada`

com equivalência temporal apropriada ao tipo de dado e ao calendário de negociação/publicação.

Para dados de mercado, deve ser considerada a **última sessão de negociação efetivamente disponível**, e não simplesmente a data civil corrente.

## 4. Estado atual

| Dataset | Última observação identificada | Atualização do repositório | Situação |
|---|---|---|---|
| COTAHIST anual 2026 | 22/09/2026 | 26/09/2026 | **PENDENTE** |
| Copom/BCB | 15–16/09/2026 (281ª reunião) | 25/09/2026 | **REGISTRADO** |
| Outros datasets B3/macro | Necessitam matriz individual de frescor | — | **NÃO CERTIFICADOS** |

## 5. Regra de fail-closed

Enquanto existir pelo menos um dataset obrigatório sem prova de frescor, o status global permanece **NÃO CERTIFICADA**.

Nenhum workflow, dashboard, modelo, backtest ou relatório pode interpretar este documento como confirmação de cobertura integral.

## 6. Condição para emissão da próxima carta

A próxima versão poderá receber status **CERTIFICADA** somente após:

1. inventário dos datasets obrigatórios;
2. identificação da última data disponível em cada fonte oficial;
3. confirmação da última data armazenada;
4. reconciliação de pregões/feriados quando aplicável;
5. validação dos hashes e manifests;
6. verificação dos workflows de ingestão;
7. registro da evidência em matriz única de frescor;
8. aprovação sem pendências críticas.

## 7. Evidências de repositório

- Commit de atualização COTAHIST: `b159415d33b0be7fef2d1c63426f2b77bbea46ce`.
- Commit de importação diária COTAHIST: `1b2ef358f02c18fb1d1b061a41e97e13f957653e`.
- Commit de captura Copom RAW/NORMALIZED: `67f53402daacf15cfabca5a30f3a827b3c602c9a`.
- Carta de confiança dos workflows: `governanca/CARTA_DE_CONFIANCA_WORKFLOWS.md`.

## 8. Conclusão

**Não há, em 26/09/2026, evidência suficiente para afirmar que todos os últimos dados da B3 disponíveis até a data corrente já foram baixados.**

A principal pendência identificada é o intervalo entre **22/09/2026** e a última sessão de mercado disponível que deva constar no COTAHIST. A governança deve permanecer em modo **fail-closed** até a reconciliação dessa lacuna e a certificação dos demais datasets obrigatórios.

> Esta carta é uma certificação de estado, não uma declaração de que a cobertura integral já foi atingida.
