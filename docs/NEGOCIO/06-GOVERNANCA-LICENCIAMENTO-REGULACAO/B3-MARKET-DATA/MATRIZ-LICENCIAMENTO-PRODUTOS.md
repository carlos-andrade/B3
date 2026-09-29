# Matriz de Licenciamento B3 — Produtos Comerciais

> **Status:** modelo operacional para análise econômica e compliance. Não substitui contrato, Commercial Policy vigente, Consumption Policy ou validação formal da B3.

## Objetivo

Traduzir a Market Data B3 Commercial Policy 2026 V1.1 para uma matriz operacional:

**Produto → Dataset → Depth → Timeliness → Display/Non-Display → Finalidade → License → Counting Unit → Tarifa → Custo → Receita → Margem → Evidência**

## Classificação de confiança

- **CONFIRMADO:** regra/tarifa encontrada na documentação oficial consultada.
- **HIPÓTESE:** possível enquadramento comercial; precisa de validação.
- **A VALIDAR:** não assumir como direito de uso/licença sem confirmação contratual.
- **EVIDÊNCIA HISTÓRICA:** valor encontrado em versão intermediária de 2026; não usar isoladamente para fechar preço.

## Matriz inicial dos produtos

| Produto | Dataset provável | Depth | Timeliness | Display / Non-Display | Finalidade | Licença provável | Status |
|---|---|---|---|---|---|---|---|
| Radar B3 | Equities + eventualmente Futures | L1 | Real-Time ou Delayed | Display | informação/monitoramento | A VALIDAR | HIPÓTESE |
| Pro Fluxo | Equities/Futures | L1/L2 conforme necessidade | Real-Time | Non-Display e/ou Display | análise de fluxo | A VALIDAR | HIPÓTESE |
| B3 Quant Lab | Equities/Futures/Options | L1/L2 | Real-Time/Delayed | Non-Display | pesquisa, modelagem e desenvolvimento | Product Development / Internal Use a validar | HIPÓTESE |
| B2B Analytics | Dataset contratado | conforme produto | conforme contrato | Display/Non-Display | analytics para cliente | Distribution / Product Development / outra a validar | A VALIDAR |
| API White-label Enterprise | Dataset contratado | conforme contrato | conforme contrato | Non-Display/Distribution | distribuição/integração | Enterprise ou licença específica | A VALIDAR |
| Projetos de Engenharia | Dataset do cliente ou contratado | conforme escopo | conforme escopo | conforme escopo | desenvolvimento sob encomenda | depende do contrato | A VALIDAR |

## Campos obrigatórios antes da comercialização

1. Dataset.
2. Profundidade: L1 ou L2.
3. Timeliness: Real-Time, Delayed Continuous ou Delayed Snapshot.
4. Display ou Non-Display.
5. Finalidade: Trading, Non-Trading ou outra classificação aplicável.
6. Tipo de licença.
7. Counting unit.
8. Usuários.
9. Localização.
10. Co-Location.
11. Distribuição a terceiros.
12. Transformação/derivação.
13. Necessidade de Enterprise.
14. Tarifa aplicável.
15. Evidência documental.
16. Data da consulta.
17. Versão da Commercial Policy.
18. Validação jurídica/comercial.

## Tarifas de referência de 2026

Os valores seguintes foram encontrados em **versão intermediária oficial de 2026** e permanecem classificados como **EVIDÊNCIA HISTÓRICA** até reconciliação integral com a V1.1.

### Non-Display — fora de Co-Location — por Dataset/mês

| Categoria | USD/mês | BRL/mês |
|---|---:|---:|
| Applications for Trading Purposes | 250 | 500 |
| Applications for other Purposes (Non-Trading) | 150 | 300 |
| Enterprise — Trading + Non-Trading | 3.500 | 7.000 |
| Enterprise for Trading Platforms | 5.000 | 10.000 |

### Fixed Income Display — Full Order Book L2

| Categoria | USD/mês | BRL/mês |
|---|---:|---:|
| Professional Terminal | 60 | 126 |
| Wallboard | 508 | 1.016 |

### Non-Display — dentro de Co-Location — por Dataset/mês

| Categoria | USD/mês | BRL/mês |
|---|---:|---:|
| Trading Purposes | 112,50 | 225 |
| Other Non-Trading | 67,50 | 135 |
| Enterprise — Trading + Non-Trading | 1.575 | 3.150 |
| Enterprise for Trading Platforms | 2.250 | 4.500 |

**Regra:** não usar esses números para fechar preço comercial definitivo sem confrontar a tabela completa da V1.1, notas e Consumption Policy.

## Regras cambiais e atualização

A documentação oficial consultada estabelece, em síntese:

- licenças nacionais em BRL;
- licenças internacionais em USD;
- conversão USD→BRL pela PTAX Venda aplicável ao último dia do mês de uso;
- correções de self-report com as condições/tarifas do mês da correção;
- atualização anual de tarifas nacionais por IPCA;
- atualização anual de tarifas internacionais por CPI;
- possibilidade de alteração de tarifas pela B3 mediante aviso prévio;
- possibilidade de descontos ou isenções conforme as regras aplicáveis.

## Modelo econômico

**Custo B3 mensal = Σ (Dataset × unidade de cobrança × tarifa aplicável)**

**Receita mensal = clientes pagantes × preço médio mensal**

**Margem de contribuição preliminar = Receita − custo B3 − infraestrutura − dados de terceiros − suporte − pagamentos − demais custos variáveis**

Receita hipotética não deve ser tratada como realizada.

## Ficha de licenciamento

```
PRODUTO:
CLIENTE:
DATASET:
DEPTH:
TIMELINESS:
DISPLAY/NON-DISPLAY:
FINALIDADE:
TIPO DE LICENÇA:
COUNTING UNIT:
USUÁRIOS:
LOCATION:
CO-LOCATION:
DISTRIBUIÇÃO:
TRANSFORMAÇÃO:
ENTERPRISE:
TARIFA:
MOEDA:
CUSTO MENSAL:
CUSTO ANUAL:
EVIDÊNCIA:
POLICY VERSION:
DATA DA CONSULTA:
STATUS:
OBSERVAÇÕES:
```

## Gate comercial obrigatório

**Fonte → Dataset → Direito de uso → Classificação → Licença → Tarifa → Custo → Contrato → Compliance → Produto**

Se qualquer etapa estiver **A VALIDAR**, o produto permanece em pré-comercialização.

## Próxima etapa

Transformar esta matriz em modelo quantitativo com preço, usuários, datasets, tarifas, custo B3, infraestrutura, CAC, churn, LTV, break-even, margem, cenários de 10/50/100/500/1.000 clientes e sensibilidades a PTAX e reajustes.

### Fontes de controle

- B3 — Market Data B3 Commercial Policy 2026 V1.1.
- B3 — Market Data B3 Consumption Policy.
- B3 — Periodical Self-Report Submission Manual.
- B3 — documentação oficial do novo sistema de contratação/reporting 2026.
- Valores históricos: versão intermediária oficial de 2026, mantidos apenas para reconciliação.

**Última revisão:** 2026-09-29
