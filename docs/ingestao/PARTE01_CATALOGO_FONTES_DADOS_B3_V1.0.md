# PARTE01 — Catálogo de Fontes de Dados B3 para Ingestão e Backtests

**Arquivo:** PARTE01_CATALOGO_FONTES_DADOS_B3_V1.0.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Inventário de dados históricos e dados de referência para ingestão e backtests  
**Caminho:** docs/ingestao/PARTE01_CATALOGO_FONTES_DADOS_B3_V1.0.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3  
**Status:** V1.0 — inventário inicial auditado por fontes públicas da B3

## 1. Objetivo

Construir um catálogo completo das fontes públicas e comerciais relevantes da B3 para formar uma base histórica destinada a:

- backtests;
- estudos de microestrutura;
- séries de preços;
- volume e negócios;
- derivativos;
- índices;
- instrumentos;
- marcação a mercado;
- construção e validação de setups.

A regra é **não limitar a base ao BVBG.028.02**. O cadastro de instrumentos é apenas a camada de identificação/referência.

## 2. Fontes prioritárias identificadas

### 2.1 BVBG.028.02 — InstrumentReport

Função: cadastro de instrumentos negociáveis e instrumentos aceitos em garantia.

Uso no projeto:
- identificação de instrumentos;
- códigos;
- características;
- mapeamento entre instrumentos e séries;
- dimensão mestre para normalização histórica.

Fonte: B3 — Pesquisa por pregão / Layout de arquivos.

### 2.2 BVBG.029.02 — IndicatorReport

Função: cadastro de instrumentos indicadores.

Uso:
- índices;
- indicadores de preço;
- referência para séries de indicadores.

### 2.3 BVBG.086.01 — PriceReport

Função: dados relativos às negociações realizadas no dia de referência.

Uso:
- preços;
- estatísticas de negociação;
- reconstrução de séries de mercado;
- base para validações de EOD.

### 2.4 BVBG.087.01 — IndexReport

Função: dados de índices, IOPVs e valores de referência para BDRs.

Uso:
- Ibovespa e demais índices disponíveis;
- IOPV;
- valores de referência;
- validação de benchmarks.

### 2.5 BVBG.186.01 — Simplified Price Report — Equities

Função: boletim simplificado de negociação do mercado de ações.

Uso:
- séries de renda variável;
- OHLC e estatísticas disponibilizadas;
- backtests de ações.

### 2.6 BVBG.187.01 — Simplified Price Report — Derivatives

Função: boletim simplificado de negociação do mercado de derivativos.

Uso:
- futuros;
- opções;
- derivativos listados;
- séries para backtests.

## 3. Séries históricas de cotações

A B3 disponibiliza uma série histórica de cotações com histórico de preços desde **1986**.

Campos informados pela B3 incluem, entre outros:
- empresa/nome;
- código;
- ISIN;
- tipo de mercado;
- especificação;
- preço anterior;
- abertura;
- mínimo;
- médio;
- máximo;
- fechamento;
- quantidade de negócios;
- volume negociado.

Formato divulgado: arquivos compactados, com dados TXT e layout específico.

Esta fonte é fundamental para ampliar o horizonte histórico além da disponibilidade dos arquivos BVBG atuais.

## 4. Histórico diário e pesquisa por pregão

A página de Pesquisa por Pregão permite selecionar arquivos retroativos por data.

Devemos ingerir, quando disponíveis e pertinentes:
- cadastro de instrumentos;
- cadastro de indicadores;
- PriceReport;
- IndexReport;
- boletins simplificados de ações;
- boletins simplificados de derivativos;
- arquivos históricos específicos de derivativos;
- demais arquivos de fechamento necessários à reconstrução das sessões.

## 5. Derivativos — arquivos históricos relevantes

A documentação histórica da B3 identifica famílias de arquivos para:

- negócios realizados em pregão;
- negócios parciais;
- negócios preliminares;
- negócios finais;
- after-hours;
- atualização de contratos em aberto;
- mercado de balcão;
- opções flexíveis;
- superfícies/volatilidades;
- prêmios de referência;
- contratos autorizados;
- posições;
- informações de risco/margem.

Os layouts são versionados por período. Para backtests históricos, o parser deverá respeitar a versão do layout vigente na data do arquivo.

## 6. Dados públicos complementares

O Hub de Dados Públicos da B3 também disponibiliza categorias relevantes, incluindo:

- renda variável;
- renda fixa;
- derivativos;
- BDRs;
- ETFs;
- empréstimo de ativos;
- índices;
- dados de mercado;
- cotações históricas;
- valor de mercado;
- posições em aberto;
- contratos a vencer;
- informações de negociação.

Essas fontes devem ser catalogadas antes de definirmos o conjunto mínimo definitivo.

## 7. UP2DATA / UP2DATA On Demand

A B3 informa que o UP2DATA distribui dados de fechamento e referência de diferentes mercados.

O UP2DATA On Demand é uma fonte comercial de dados históricos e a B3 informa que seus pacotes podem consolidar **20 anos de histórico**.

Uso potencial:
- dados históricos que não estejam disponíveis gratuitamente;
- maior granularidade;
- complementação de séries;
- dados necessários para pesquisas institucionais.

**Importante:** contratação e direitos de uso devem ser verificados antes de qualquer ingestão comercial.

## 8. Horizonte temporal

A meta do projeto será:

**1990 → disponível mais recente**

Entretanto, não devemos fabricar continuidade histórica onde a fonte não existir.

A base deverá registrar explicitamente:

- data inicial real da fonte;
- data final real da fonte;
- lacunas;
- mudanças de metodologia;
- mudanças de código;
- mudanças de mercado;
- mudanças de layout;
- instrumentos descontinuados;
- instrumentos sucessores.

Quando uma fonte começa antes de 1990, ela será preservada desde o primeiro registro útil, sujeito ao objetivo específico do dataset.

## 9. Arquitetura de ingestão proposta

### Camada A — Raw

Guardar o arquivo original sem alteração.

### Camada B — Normalized

Converter formatos históricos distintos para um esquema canônico.

### Camada C — Instrument Master

Relacionar:
- instrumento;
- código;
- ISIN;
- mercado;
- vencimento;
- contrato;
- ativo-objeto;
- datas de início/fim.

### Camada D — Market Data

Normalizar:
- timestamp;
- preço;
- quantidade;
- financeiro;
- número de negócios;
- OHLC;
- ajustes;
- posições;
- demais campos disponíveis.

### Camada E — Derived

Construir somente após preservação dos dados brutos:
- VWAP;
- TWAP;
- volume financeiro;
- volatilidade;
- retornos;
- gaps;
- FVG;
- medidas de fluxo;
- Cumulative Delta, quando os dados permitirem.

## 10. Regra para Cumulative Delta

Não devemos inferir Cumulative Delta histórico a partir de OHLC diário como se fosse fluxo real.

Para obter Delta de qualidade precisamos de dados com informação suficiente para classificar agressão/negócios.

Portanto:

- OHLC = não equivale a fluxo;
- volume total = não equivale a agressão;
- negócios/ticks = podem permitir reconstrução parcial, dependendo dos campos;
- dados de book/agressão explícitos = camada superior de microestrutura.

## 11. Regra para backtests

Todo dataset deverá carregar metadados:

- fonte;
- arquivo;
- versão do layout;
- data do pregão;
- timestamp de ingestão;
- checksum, quando possível;
- parser utilizado;
- versão do parser;
- quantidade de registros;
- registros rejeitados;
- motivo das rejeições;
- cobertura temporal;
- cobertura por instrumento.

## 12. Prioridade de ingestão

### P0 — Obrigatório

1. BVBG.028.02
2. série histórica de cotações
3. BVBG.086.01
4. BVBG.087.01
5. BVBG.186.01
6. BVBG.187.01

### P1 — Derivativos

7. negócios finais
8. negócios preliminares
9. negócios parciais
10. after-hours
11. ajustes
12. contratos em aberto
13. cadastro/contratos autorizados
14. opções e respectivas referências de volatilidade

### P2 — Contexto

15. índices
16. indicadores econômicos
17. DI
18. câmbio
19. renda fixa
20. empréstimo de ativos
21. demais dados públicos relevantes

### P3 — Microestrutura avançada

22. dados intraday/tick disponíveis
23. book/market-by-order, quando legalmente e tecnicamente disponíveis
24. agressão/classificação de negócios
25. dados necessários para reconstrução de fluxo

## 13. Critério de completude

A pergunta do projeto não será:

> "Temos BVBG.028.02?"

Será:

> "Conseguimos reconstruir, com rastreabilidade, o estado do mercado para cada sessão e instrumento necessário ao backtest?"

Um dataset só será considerado **BACKTEST-READY** quando sua cobertura, qualidade, identidade dos instrumentos e regras de transformação estiverem documentadas.

## 14. Próxima etapa

O próximo trabalho da PARTE01 deverá ser transformar este catálogo em uma **matriz de ingestão**, contendo:

| Fonte | Mercado | Granularidade | Início disponível | Fim disponível | Campos | Acesso | Formato | Prioridade | Backtest |
|---|---|---|---|---|---|---|---|---|---|
| BVBG.028.02 | Todos/Referência | Diário | a verificar | atual | Instrumentos | Público | conforme B3 | P0 | Sim |
| BVBG.029.02 | Índices/Indicadores | Diário | a verificar | atual | Indicadores | Público | conforme B3 | P0 | Sim |
| BVBG.086.01 | Negociação | Diário | a verificar | atual | Preços/negociação | Público | conforme B3 | P0 | Sim |
| BVBG.087.01 | Índices | Diário | a verificar | atual | Índices/IOPV | Público | conforme B3 | P0 | Sim |
| BVBG.186.01 | Ações | Diário | a verificar | atual | Negociação | Público | conforme B3 | P0 | Sim |
| BVBG.187.01 | Derivativos | Diário | a verificar | atual | Negociação | Público | conforme B3 | P0 | Sim |
| Cotações históricas | Renda variável | Diário | 1986 | atual | OHLC/volume/negócios | Público | ZIP/TXT | P0 | Sim |

---

## Fontes oficiais consultadas

- B3 — Pesquisa por Pregão.
- B3 — Layout dos arquivos.
- B3 — Cotações Históricas.
- B3 — Hub de Dados Públicos.
- B3 — UP2DATA / Dados disponíveis.
- B3 — documentação histórica de arquivos de derivativos.

**Nota:** este documento é um inventário técnico inicial. As datas exatas de início/fim de cada arquivo e as versões históricas dos layouts serão levantadas na matriz de ingestão antes da implementação dos parsers.
