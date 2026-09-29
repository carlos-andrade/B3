# Matriz Econômica B3

## Objetivo
Comparar as linhas comerciais do B3 Market Intelligence Engine por ticket, complexidade, margem potencial, risco regulatório/licenciamento e capacidade de escala.

> Os valores monetários abaixo são hipóteses de modelagem. Não são previsão de receita.

| Produto | Cliente | Ticket mensal de referência | Complexidade | Escala | Dependência de dados/licenças | Risco regulatório | Papel estratégico |
|---|---|---:|---|---|---|---|---|
| Radar B3 | Trader/estudante avançado | R$79–199 | Média | Alta | Alta | Médio | Aquisição |
| Pro Fluxo | Trader avançado/pequena mesa | R$249–599 | Alta | Média/alta | Alta | Médio/alto | Monetização |
| B3 Quant Lab | Quant/pesquisador | R$299–1.500 | Alta | Média | Alta | Médio | Diferenciação |
| B2B Analytics | Gestoras/mesas/consultorias | R$2.000–10.000+ | Alta | Média | Muito alta | Alto | Receita recorrente B2B |
| API / White-label | Fintechs/empresas | Contrato | Muito alta | Alta | Muito alta | Alto | Infraestrutura |
| Projetos de Engenharia | Empresas | R$5.000–50.000+ por projeto | Alta | Baixa/média | Variável | Variável | Caixa + aquisição B2B |

## Critérios de decisão

### Valor econômico
Priorizar soluções em que o cliente paga por redução de tempo, melhoria de processo, acesso estruturado à informação ou infraestrutura.

### Recorrência
MRR deve ser separado de receita de projetos. Projetos podem financiar produto, mas não devem ser confundidos com ARR recorrente.

### Margem
A margem dependerá principalmente de:
- custo de dados/licenciamento;
- infraestrutura;
- armazenamento e processamento;
- suporte;
- aquisição de clientes;
- desenvolvimento e manutenção;
- custos jurídicos/compliance.

### Risco de distribuição
Antes de qualquer produto comercial, classificar cada fonte como:
1. dado bruto de terceiro;
2. dado licenciado;
3. dado derivado;
4. indicador/modelo próprio;
5. análise própria.

A comercialização de qualquer camada deve respeitar os direitos da fonte.

## Hipótese operacional inicial

A arquitetura comercial deve ser construída em camadas:

Dados → Tratamento → Indicadores → Contexto → Diagnóstico → Alertas → Workflow → Produto

A camada de produto não deve depender de uma única fonte nem de uma única forma de monetização.

## Próxima validação
Executar testes reais de disposição a pagar e calcular:
- CAC;
- churn;
- ARPU;
- margem de contribuição;
- payback;
- LTV;
- conversão de teste para pago.

Status: modelo inicial — requer validação comercial.
