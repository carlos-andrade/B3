# TAM / SAM / SOM — Estrutura de Dimensionamento

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-64CE9E40F612 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | deb4b5285e9517910994ceb0da2d921a63215495f754546da283177dd5f86277 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Dimensionar o mercado do B3 Market Intelligence Engine sem confundir população potencial com receita efetivamente alcançável.

## Definições

TAM: todo o valor econômico potencial dentro do escopo definido.

SAM: parte do TAM compatível com geografia, cliente, produto, dados/licenças e capacidade operacional.

SOM: parte do SAM realisticamente alcançável no horizonte definido, considerando distribuição, produto, concorrência e execução.

## Método recomendado

Abordagem bottom-up:

Número de compradores potenciais x ARPU anual.

Para B2B:

Número de contas-alvo x contrato anual médio.

Para API:

Contas x fee fixo + consumo esperado.

## Estado atual

Ainda não há base validada suficiente para declarar TAM/SAM/SOM como números de mercado. Este arquivo define o modelo e não apresenta um TAM fictício.

## Dados necessários

1. população relevante de traders e investidores;
2. profissionais e pequenas mesas;
3. gestoras, escritórios, consultorias e fintechs;
4. gastos comparáveis com ferramentas de mercado;
5. concorrentes e faixas de preço;
6. direitos de distribuição/licenciamento;
7. conversão observada;
8. retenção observada;
9. capacidade operacional.

## Regra de governança

Qualquer TAM/SAM/SOM publicado no projeto deve separar: FATO → FONTE → ASSUNÇÃO → CÁLCULO → INTERVALO → LIMITAÇÃO.

Status: estrutura pronta para pesquisa quantitativa.
