# Revisão semântica documental — Lote 09: produtos, mercados e economia do negócio

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-009 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; HIPOTESES_COMERCIAIS_NAO_VALIDADAS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão semântica; não aprova preços, produto ou estratégia comercial |
| **Origem** | Inspeção de 16 documentos de produto, mercado-alvo e economia |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | GOVERNANÇA → HIPÓTESES → TESTES → EVIDÊNCIA → DECISÃO |
| **Escopo** | Visão executiva, segmentos, produtos, B2B, engenharia, pricing e métricas económicas |
| **Objetivo** | Confirmar separação entre hipóteses comerciais, cálculos ilustrativos e resultados observados |
| **Dependências** | Entrevistas, disposição a pagar, custos, licenças, dados de mercado e registo de decisões comerciais |

## 1. Resultado executivo

Foram revistos 16 documentos. O conjunto mantém, de forma consistente, preços e cenários como hipóteses, exige validação de mercado e licenciamento antes de comercializar dados, e não inventa números de TAM/SAM/SOM. A revisão não encontrou base documental para tratar as faixas de preço ou projeções económicas como receita realizada ou previsão aprovada.

O cálculo ilustrativo de break-even é aritmeticamente coerente com contribuição média de R$ 160 por cliente e custos fixos de R$ 30.000/mês: 30.000 / 160 = 187,5, arredondado para 188 clientes. A validade comercial depende de premissas verificadas, impostos, inadimplência, custos extraordinários e amostra real; o documento já declara esses limites.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/NEGOCIO/00-VISAO-EXECUTIVA.md | Visão executiva | Define a cadeia dado → tratamento → indicador → contexto → diagnóstico → alerta → decisão assistida e proíbe tratar hipóteses de faturamento como garantias. | Manter como tese estratégica; métricas comerciais precisam de evidência antes de promoção. |
| docs/NEGOCIO/01-MERCADOS-ALVO/README.md | Índice de segmentos | Classifica segmentos como hipóteses e exige ICP, problema, ticket, canal, risco regulatório e disposição a pagar. | Não escalar segmento só por constar na lista; exigir entrevistas e evidência documentada. |
| docs/NEGOCIO/02-PRODUTOS/B3-QUANT-LAB.md | Hipótese de produto | Apresenta funcionalidades e faixa de R$ 299–1.500/mês como hipótese condicionada a escopo/licenciamento. | Validar com clientes e direitos de dados antes de preço/oferta pública. |
| docs/NEGOCIO/02-PRODUTOS/PRO-FLUXO.md | Hipótese de produto | Posiciona fluxos e contexto operacional; preço está rotulado como hipótese. | Não declarar produto disponível nem desempenho sem implementação e testes demonstrados. |
| docs/NEGOCIO/02-PRODUTOS/RADAR-B3.md | Hipótese de produto | Descreve dashboard diário e faixa de preço a validar com clientes. | Exigir evidência de qualidade/atualidade e licenças dos dados consumidos. |
| docs/NEGOCIO/03-B2B/API-WHITELABEL-ENTERPRISE.md | Hipótese de oferta B2B | Admite dados agregados/serviços, mas proíbe comercializar feeds sem verificar direitos de uso/distribuição. | Licenciamento e segurança são gates antes de qualquer distribuição. |
| docs/NEGOCIO/03-B2B/B2B-ANALYTICS.md | Hipótese de serviço B2B | Faixa de R$ 2.000–10.000+/mês está condicionada a escopo, SLA, dados, licenças e integração. | Não tratar a faixa como preço validado ou receita recorrente observada. |
| docs/NEGOCIO/04-IMPLEMENTACAO/PROJETOS-ENGENHARIA.md | Hipótese de serviços | Identifica serviços de engenharia e classifica preços como referência experimental, não promessa de receita. | Separar receita de projetos de ARR/MRR de produto. |
| docs/NEGOCIO/05-ECONOMIA/BREAK-EVEN.md | Modelo matemático | Fórmula e resultado ilustrativo são aritmeticamente consistentes: R$ 30.000 / R$ 160 = 187,5, arredondado para 188 clientes. | Validar custos fixos/variáveis, contribuição, impostos, chargebacks e inadimplência antes de usar como plano financeiro. |
| docs/NEGOCIO/05-ECONOMIA/CAC-LTV-CHURN.md | Framework de métricas | Define fórmulas e exige cohorts, tamanho de amostra e limitações. Alerta que LTV com amostra pequena não é robusto. | Não reportar LTV como estimativa robusta sem dados reais e janela de observação suficiente. |
| docs/NEGOCIO/05-ECONOMIA/ICP.md | Hipóteses de cliente ideal | Identifica perfis de trader, mesa/profissional e pesquisador/quant, sem confundir necessidade proposta com validação de mercado. | Validar por entrevistas, problemas mensuráveis, retenção e disposição a pagar. |
| docs/NEGOCIO/05-ECONOMIA/MATRIZ-ECONOMICA-B3.md | Matriz de comparação económica | Rotula tickets como hipóteses e separa MRR de receita de projetos, além de incluir dependência de dados/licenças e risco regulatório. | Preencher com métricas observadas antes de decisão de prioridade comercial. |
| docs/NEGOCIO/05-ECONOMIA/PRICING.md | Framework de pricing | Define experimentos e métricas de preço; o status é explicitamente hipótese de pricing. | Não publicar preços definitivos sem testar disposição a pagar e custo de servir. |
| docs/NEGOCIO/05-ECONOMIA/README.md | Índice económico | Exige separar factos, premissas, cálculos e resultados e rotular cenários como ilustrativos até validação. | Manter como regra editorial do domínio comercial. |
| docs/NEGOCIO/05-ECONOMIA/TAM-SAM-SOM.md | Método de dimensionamento | Define TAM/SAM/SOM e declara que não há base validada suficiente para números de mercado. | Não preencher estimativas sem fontes, geografia, segmentos, preço, concorrência e capacidade operacional. |
| docs/NEGOCIO/05-ECONOMIA/UNIT-ECONOMICS.md | Framework económico | Exige CAC, LTV, churn e cenários; classifica valores como matemáticos, não previsões. | A revisão futura deve ligar cada parâmetro à fonte, período, amostra e sensibilidade. |

## 3. Achados transversais

### SEM-09-01 — hipóteses de preço sem validação observada

As faixas de preço estão explicitamente marcadas como hipóteses. Não devem ser promovidas a tabela comercial oficial sem entrevistas, testes de disposição a pagar, custos de servir e decisão versionada.

### SEM-09-02 — modelo de break-even é ilustrativo

A aritmética do exemplo está correta, mas a saída de 188 clientes depende de contribuição de R$ 160 e custo fixo de R$ 30.000/mês. A revisão não valida as premissas de negócio.

### SEM-09-03 — licenciamento é gate comercial

Os documentos B2B reconhecem que dados/feed não podem ser redistribuídos sem confirmação de direitos. A integração comercial não deve anteceder a revisão de licenças, contratos e segurança.

### SEM-09-04 — TAM/SAM/SOM não estimado

O documento declara corretamente ausência de base validada. Não adicionar estimativas inventadas para aparentar completude.

## 4. Conclusão

O conteúdo dos 16 documentos foi revisto e classificado. Não foram aprovados preços, previsões, mercados-alvo nem decisões de investimento. O estado do lote é revisão semântica concluída, com hipóteses comerciais pendentes de validação empírica.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
