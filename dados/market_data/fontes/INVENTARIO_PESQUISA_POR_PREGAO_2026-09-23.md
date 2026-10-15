# Inventário da Pesquisa por Pregão — 2026-09-23

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-008-EGAO-2026-09-23-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_DE_FONTES |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | ee80e3cdec12c4f9a4a7c06f54646eda95a70dbec7db6c9d748417ee27b3cc9a |
| **Commit de referência (versão anterior)** | [7a09339f3244b84dd165400279b6da090bd2bb80](https://github.com/carlos-andrade/B3/commit/7a09339f3244b84dd165400279b6da090bd2bb80) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Inventário dos arquivos disponibilizados para download pela B3  
**Caminho:** dados/market_data/fontes/INVENTARIO_PESQUISA_POR_PREGAO_2026-09-23.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

Fonte oficial: [Pesquisa por Pregão — B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/).

**Ressalva de acesso:** a página informa que a coleta automatizada a partir dela, inclusive por ferramentas de IA, é vedada. Este inventário é uma observação documental datada; não autoriza scraping. Qualquer API/endpoint alternativo exige revisão própria dos termos e autorização.

## Escopo observado

A página oficial informa que permite acessar boletins diários e arquivos emitidos pela B3 e obter arquivos retroativos selecionando a data para cada arquivo.

## Arquivos listados na página

| Categoria/arquivo | Código ou identificação | Situação observada em 23/09/2026 |
|---|---|---|
| Agrupamento de Instrumentos Padronizados | Standardized Instrument Groups | ativo |
| Arquivo de Índices | BVBG.087.01 IndexReport | ativo |
| Boletim de Negociação | BVBG.086.01 PriceReport | ativo |
| Boletim Simplificado — Ações | BVBG.186.01 | ativo |
| Boletim Simplificado — Derivativos | BVBG.187.01 | ativo |
| Cadastro de instrumentos | BVBG.028.02 | ativo |
| Cadastro de instrumentos indicadores | BVBG.029.02 | ativo |
| Custo Unitário Diário de Tarifação | BVBG.044.01 | ativo |
| Custo Unitário de Tarifação | BVBG.043.01 | ativo |
| Fatores Primitivos de Risco | FPRs | ativo |
| Fórmulas de Risco | Risk Formulas | ativo |
| Informações Variáveis de Tarifação | BVBG.024.01 | ativo |
| Limites de Liquidez Diária | Daily Liquidity Limit | ativo |
| Outros Limites de Liquidez Diária | Other Limits | ativo |
| Lista de Instrumentos Negociáveis | Tradable Security List | ativo |
| Mapeamento de Grupos OTC | OTC Instrument Groups | ativo |
| Mapeamento de Grupos Padronizados | Standardized Instrument Groups | ativo |
| Margem Teórica Máxima / Garantias | Maximum Theoretical Margin | ativo |
| Prêmio de Referência — Opções sobre Ações | Equities Option Reference Premiums | ativo |
| Mercado de Câmbio — Taxas/Parâmetros/Operações | FX Market | ativo |
| Mercado de Câmbio — Volume Líquido Compensado | FX Net Settled Volume | ativo |
| Cenários de Margem — Ativos Líquidos | Derivatives Margin Scenarios | ativo |
| GTSLiNe — Fatores de Ponderação | Consideration Factors | histórico/atualização antiga |
| Indicadores Econômicos e Agropecuários — Final | Derivatives Economic/Agricultural Indicators | ativo |
| Negócios no Mercado de Balcão | OTC Market Trades | última atualização exibida: 12/12/2025 |
| Negócios registrados em leilão BACEN | BACEN Auction Registered Trades | histórico |
| Operações Estruturadas de Volatilidade | Volatility Transactions | histórico/descontinuado |
| Posições Travadas | Locked Positions | descontinuado; dados no BDI |
| Prêmio de Referência — Derivativos | Option Reference Premiums | ativo |
| Swap Cambial — Mark to Market | IDxUS Dollar Swap MTM | ativo |
| Taxas de Mercado para Swaps | Swap Market Rates | ativo |
| Preços Referenciais de Títulos Públicos | Government Securities Reference Prices | ativo |
| Parâmetros de Grupos de Instrumentos | Instrument Group Parameters | ativo |
| Renda Fixa Privada | Fixed Income | ativo |
| Taxas do Mercado de Renda Variável | BVBG.072.01 | ativo |

## Arquivos individuais de risco observados

A página também apresenta arquivos individuais de cenários de risco, incluindo:

- cenários de curva;
- cenários de curva por severidade;
- cenários de preço de referência;
- cenários de superfície;
- cenários de spot;
- matriz de risco para cálculo do RMKT pelo cliente.

## Importante

Este inventário é um **catálogo da página**, não a carga histórica dos arquivos.

A página permite selecionar datas retroativas e baixar arquivos. Para transformar isso em uma base histórica local, precisamos executar uma captura por arquivo/data, preservar o bruto, calcular SHA-256 e registrar manifesto.

Não será declarado que "toda a carga histórica" foi armazenada até que os downloads tenham sido efetivamente realizados e validados.

## Próxima etapa de ingestão

Prioridade:

1. BVBG.028.02 — instrumentos;
2. BVBG.029.02 — indicadores;
3. BVBG.086.01 — PriceReport;
4. BVBG.186.01 — ações;
5. BVBG.187.01 — derivativos;
6. BVBG.087.01 — índices;
7. demais arquivos de mercado;
8. arquivos de risco;
9. arquivos históricos/descontinuados, quando a B3 disponibilizar download retroativo.

Cada arquivo deverá ser armazenado como:

`dados/market_data/raw/<arquivo>/<YYYY-MM-DD>/`

com:

- arquivo bruto;
- SHA-256;
- tamanho;
- data de captura;
- data de referência;
- fonte;
- layout;
- número de registros;
- validação.

## Regra de preservação

O arquivo original nunca será sobrescrito por uma transformação. Dados normalizados serão derivados em diretório separado.
