# BRAZIL SOTCK EXCHANGE (B3) — Documento de Referência

- **Documento:** B3-REFERENCE-001
- **Versão:** 1.0
- **Data de pesquisa:** 26 de outubro de 2026
- **Estado:** referência inicial baseada em fontes públicas oficiais; requer revisão contínua de normativos e especificações operacionais
- **Repositório:** `carlos-andrade/B3`
- **Pasta:** `BRAZIL SOTCK EXCHANGE/`

> **Nota sobre o nome da pasta:** o nome `BRAZIL SOTCK EXCHANGE` foi preservado exatamente como solicitado. O nome institucional correto é **B3 — Brasil, Bolsa, Balcão**.

## 1. Sumário executivo

A B3 é a infraestrutura de mercado financeiro do Brasil que combina mercado listado e balcão organizado com serviços de pós-negociação, depósito centralizado, registo, dados, tecnologia e soluções adjacentes. Não deve ser entendida apenas como um “site de cotações” ou como um local de compra e venda de ações: a sua infraestrutura conecta negociação, compensação, liquidação, custódia e divulgação de informação. [1]

O mercado da B3 permite exposição a empresas brasileiras, índices, juros, moedas e commodities por meio de ações, units, ETFs, BDRs, fundos imobiliários, opções, contratos a termo e futuros, entre outros instrumentos. A disponibilidade e as características concretas de cada produto devem ser verificadas na ficha oficial atual e no respetivo contrato. [2–8]

Este documento organiza os principais conhecimentos necessários para estudar a B3, construir pipelines auditáveis de dados históricos e correntes, analisar microestrutura e desenvolver estratégias quantitativas sem confundir informação descritiva, hipótese de mercado e resultado comprovado.

## 2. Identidade, estrutura e funções

A B3 — Brasil, Bolsa, Balcão — resultou da combinação da BM&FBOVESPA com a Cetip. A empresa presta serviços a diferentes segmentos do sistema financeiro e possui um modelo de negócio integrado ao longo de várias etapas do ciclo de uma operação. [1]

### 2.1 Segmentos funcionais

1. **Mercado listado:** negociação organizada de ações, derivativos de ações, juros, moedas e mercadorias, entre outros produtos.
2. **Mercado de balcão:** infraestrutura para registo de instrumentos financeiros, inclusive renda fixa e derivativos, nos termos dos produtos e regras aplicáveis.
3. **Pós-negociação:** compensação, gestão de garantias, gestão de risco, liquidação e serviços de central depositária.
4. **Dados, tecnologia e serviços:** produção, tratamento e distribuição de dados e disponibilização de soluções tecnológicas.
5. **Infraestrutura adjacente:** serviços para processos de financiamento de veículos e imóveis e atividades relacionadas, que não devem ser confundidos com o núcleo de negociação de valores mobiliários. [1]

### 2.2 O que a B3 não é

A B3 não é a autoridade pública responsável por toda a regulação do mercado, não garante lucros ao investidor e não elimina riscos de preço ou de liquidez. A **CVM** é a autoridade pública responsável pela regulação e fiscalização do mercado de valores mobiliários dentro da sua competência. A B3, por sua vez, administra mercados e executa funções operacionais sob normas aplicáveis. [9–10]

## 3. Principais classes de ativos e instrumentos

| Classe | Exemplos / códigos conhecidos | Utilização típica | Riscos e verificações |
|---|---|---|---|
| Ações | PETR4, VALE3, ITUB4 (códigos ilustrativos) | Participação societária, valorização e proventos | Risco empresarial, preço, liquidez, governança e concentração |
| Units | Pacotes de valores mobiliários de um emissor | Exposição combinada conforme a estrutura do emissor | Direitos e composição dependem da emissão |
| ETFs | BOVA11 e outros fundos de índice | Acompanhar índice ou estratégia conforme regulamento | Erro de aderência, liquidez, custos e risco dos ativos |
| Fundos imobiliários (FIIs) | Cotas negociadas em bolsa | Exposição a imóveis ou ativos financeiros imobiliários | Vacância, crédito, juros, concentração, desconto sobre valor patrimonial |
| BDRs | Certificados relacionados a valores mobiliários estrangeiros | Exposição a ativos emitidos fora do Brasil | Risco do ativo, câmbio, estrutura do programa e liquidez |
| Opções | Calls e puts sobre ativos autorizados | Hedge, exposição assimétrica ou estratégia de volatilidade | Perda de prémio, tempo, volatilidade implícita, exercício e margem do lançador |
| Futuros de índice | IND e WIN | Exposição ou cobertura de risco de ações | Alavancagem, ajuste diário, basis, vencimento e margem |
| Futuros cambiais | DOL e WDO | Hedge cambial ou exposição ao USD/BRL futuro | Alavancagem, ajuste diário, basis, vencimento e margem |
| Futuros de juros | DI1 | Gestão de exposição à curva de juros | Duration, convexidade, mudança de curva e marcação a mercado |
| Commodities | Contratos como BGI, conforme especificação vigente | Hedge e exposição a preços agrícolas ou outras commodities | Basis, sazonalidade, vencimento, liquidez e regras do contrato |
| Termo e operações estruturadas | Conforme produto elegível | Exposição a prazo, rolagem ou combinações | Risco de contraparte, custos, execução e documentação do produto |

Fontes de produto: páginas oficiais da B3 para ações, ETFs, FIIs, opções, futuros de índice, mini dólar e DI1. [2–8, 11–14]

### 3.1 Ações: código e direitos

A B3 descreve ações como valores mobiliários representativos de participação no capital de sociedades anónimas. As ações ordinárias (ON) associam-se, em regra, ao direito de voto; as preferenciais (PN) têm direitos económicos ou preferências definidos na lei e nos documentos do emissor. Não se deve inferir a totalidade dos direitos apenas pelo ticker: é necessário consultar estatuto, formulário de referência, avisos e regras da emissão. [2]

A ficha oficial consultada indica liquidação física e financeira em **D+2** para ações no mercado à vista. Prazos e procedimentos devem ser reconfirmados antes de se codificar qualquer calendário de liquidação. [2]

### 3.2 ETFs, FIIs e BDRs

- **ETF:** fundo de índice negociado em bolsa. O objetivo, índice de referência, política, custos, risco de tracking e regras de criação/resgate dependem dos documentos do fundo. [11]
- **FII:** fundo que pode investir diretamente em imóveis ou em ativos e valores mobiliários ligados ao setor imobiliário. A distribuição de rendimentos não é garantida e o preço de mercado pode divergir do valor patrimonial. [12]
- **BDR:** certificado emitido por instituição depositária no Brasil que representa valores mobiliários emitidos no exterior. A análise deve incluir o ativo subjacente, taxa de câmbio, mercado de origem, patrocínio e regras do programa. [13]

### 3.3 Derivativos: índice, dólar e juros

**WIN — mini índice:** contrato futuro relacionado ao Ibovespa. A página educacional da B3 indica valor de R$ 0,20 por ponto para o mini índice, contra R$ 1,00 por ponto no contrato cheio. O P&L bruto aproximado de um contrato pode ser expresso como variação em pontos × valor do ponto × quantidade de contratos, antes de custos, slippage e efeitos de ajuste. Confirmar sempre especificação, vencimento e tick vigentes. [14]

**WDO — mini dólar:** a ficha consultada indica objeto USD/BRL, tamanho de USD 10.000 por contrato, cotação em BRL por USD 1.000 e variação mínima de BRL 0,50 por USD 1.000. O vencimento é mensal, no primeiro dia útil do mês; o último dia de negociação é a sessão anterior. Especificações devem ser validadas na ficha oficial vigente. [6]

**DI1 — futuro de taxa DI:** instrumento utilizado para exposição e cobertura do risco de taxa de juros. O PU e a taxa negociada são inversamente relacionados pela mecânica de desconto; variações de taxa causam marcação a mercado e ajustes. É incorreto tratar uma variação de “um ponto” como se tivesse o mesmo valor económico em todos os vencimentos sem usar a metodologia do contrato. [7]

**Opções:** calls e puts conferem direitos distintos ao titular. O prémio depende, entre outros fatores, de preço do subjacente, preço de exercício, prazo, volatilidade implícita, taxas e proventos. O titular pode perder todo o prémio; o lançador pode ter risco substancial e requisitos de garantia, dependendo da estrutura. A B3 lista opções com diferentes estilos de exercício e vencimentos, incluindo séries semanais específicas. [8, 15]

## 4. Índices de mercado

O **Ibovespa B3** é uma referência central para o desempenho das ações brasileiras. A sua carteira é teórica, composta por ações e units elegíveis segundo metodologia própria e revista periodicamente. A metodologia consultada descreve critérios de negociabilidade, presença em pregão, participação mínima no volume e limites de ponderação. A carteira, os pesos e os critérios concretos devem ser obtidos na versão vigente da metodologia e na composição oficial. [3]

### 4.1 Uso quantitativo do Ibovespa

O Ibovespa pode ser utilizado como:
- benchmark para ações e carteiras brasileiras;
- variável de contexto para testar se um ativo acompanha ou diverge do mercado;
- base para futuros, ETFs, opções e estratégias de hedge;
- série de referência para estimar beta, correlação, volatilidade relativa e drawdown.

**Cuidado:** o Ibovespa é uma carteira ponderada por metodologia própria, não uma média móvel dos preços das ações e não um substituto universal de breadth. Para breadth, é necessário calcular métricas como proporção de ativos acima das suas médias, avanço/declínio ou contribuição dos componentes, respeitando a composição e os dados de cada sessão.

## 5. Negociação, formação de preços e microestrutura

O mercado eletrónico combina ordens de compra e venda sob regras de prioridade e execução definidas pela bolsa e pelo sistema de negociação. Para estudar microestrutura, separar pelo menos:

- **Preço:** negócio executado, bid/ask, midpoint, preço de ajuste e preços de referência não são intercambiáveis.
- **Volume:** quantidade negociada; não é sinónimo de volume financeiro.
- **Volume financeiro (turnover):** soma do valor financeiro dos negócios segundo a definição da fonte.
- **Spread:** diferença entre melhor oferta de venda e melhor oferta de compra.
- **Profundidade:** quantidade disponível por nível do livro; ordens podem ser canceladas e o livro observado não é uma promessa de execução.
- **Agressão:** classificação de negócios como iniciados no ask ou no bid depende do feed e da regra de classificação.
- **Cumulative Delta (CVD):** acumulado da diferença entre volume comprador agressor e vendedor agressor, quando há dados e classificação adequados. É proxy de fluxo, não identificação infalível do “dinheiro institucional”.
- **VWAP:** preço médio ponderado por volume dentro da janela e universo definidos; a VWAP diária reinicia por sessão se assim for especificada.
- **TWAP:** média ponderada pelo tempo ou preço médio ao longo de uma janela, conforme a implementação; não é equivalente à VWAP.
- **Leilões de abertura/fecho, interrupções e limites:** devem ser tratados separadamente da negociação contínua.

A interpretação de fluxo depende da qualidade do feed, sincronização de timestamps, correção de negócios, regras de agressão, negócios fora de mercado contínuo e contrato/sessão estudados. Um aumento do volume, divergência do CVD, rejeição de VWAP ou um FVG não prova isoladamente acumulação/distribuição institucional.

### 5.1 Métricas derivadas recomendadas

1. Spread em ticks e em pontos-base.
2. Volume e volume financeiro por janela, ativo e fase da sessão.
3. Profundidade nos primeiros N níveis e desequilíbrio do livro, se o feed permitir.
4. CVD por sessão e por janelas definidas; documentar o algoritmo de classificação de agressor.
5. VWAP diária e semanal, com regras explícitas de reinício, sessão e tratamento de leilões.
6. Volatilidade realizada, ATR, range, gap overnight e excursões favorável/adversa após sinal.
7. Basis entre futuro e referência à vista, com sincronização de timestamps.
8. Liquidez/impacto: slippage realista, spread, profundidade e volume relativo.
9. Métricas de risco: volatilidade, drawdown, exposição, turnover, risco de cauda e perdas sequenciais.

## 6. Pós-negociação, contraparte central e risco

A B3 informa que, na pós-negociação, atua como contraparte central (CCP) e sistema de liquidação (SSS) para operações em mercados abrangidos pelas suas regras, incluindo operações no PUMA Trading System e derivativos de balcão elegíveis. A Câmara B3 mantém regras próprias de alocação, compensação, liquidação, garantias e administração de risco. [4]

Esta proteção de infraestrutura não equivale a seguro contra perdas de mercado do investidor. Em futuros e opções lançadas, margens, ajustes diários, eventos de volatilidade e alterações de exigências podem criar necessidades de liquidez superiores às inicialmente esperadas. O investidor deve compreender:
- margem inicial e de manutenção, quando aplicável;
- marcação a mercado e ajustes diários;
- liquidação e procedimentos de vencimento/exercício;
- regras de compensação e tratamento de incumprimento;
- risco de liquidez, de mercado, operacional, tecnológico e de contraparte nas etapas relevantes.

## 7. Regulação e governança

### 7.1 Autoridades e documentos essenciais

- **CVM:** regula e fiscaliza o mercado de valores mobiliários dentro da sua competência, incluindo companhias abertas, fundos, intermediários e ofertas públicas. [9]
- **Resolução CVM 135:** trata do funcionamento de mercados regulamentados e da constituição, organização e funcionamento das entidades administradoras de mercado organizado. Consultar sempre o texto consolidado e as alterações. [10]
- **Resolução CVM 175:** disciplina a constituição, o funcionamento e a divulgação de informações de fundos de investimento, incluindo anexos normativos por categoria; a página oficial indica alterações posteriores, inclusive em 2026. [16]
- **Normativos e manuais da B3:** especificações de produtos, negociação, listagem, pós-negociação, administração de risco, tarifas, horários, formatos de arquivos e procedimentos.
- **Documentos dos emissores e fundos:** formulários de referência, demonstrações financeiras, fatos relevantes, comunicados, atas, regulamentos e prospectos.
- **Outras fontes públicas:** Banco Central do Brasil para política monetária e estatísticas; IBGE para inflação e atividade; Tesouro Nacional para dívida pública; fontes institucionais específicas para cada indicador.

### 7.2 Governança corporativa

Os segmentos de listagem da B3 incluem regras diferenciadas de governança, por exemplo Novo Mercado, Nível 1 e Nível 2, além do segmento básico e regimes aplicáveis. O segmento pode informar requisitos de divulgação e direitos, mas **não garante** qualidade financeira, solvência, boa gestão nem retorno superior. Consultar o regulamento vigente e os documentos da empresa. [17]

## 8. Dados de mercado: fontes, direitos e qualidade

### 8.1 Fonte primária

Priorizar, nesta ordem, conforme a pergunta:
1. B3: especificações de produto, metodologias de índices, boletins, dados históricos, preços de ajuste, calendários, tarifas, normativos e políticas de market data.
2. CVM: atos regulatórios, dados cadastrais, documentos de emissores e fundos e divulgações exigidas.
3. Emissores: demonstrações financeiras, fatos relevantes, comunicados e apresentações originais.
4. Banco Central, IBGE, Tesouro Nacional e demais produtores oficiais para dados macroeconómicos.
5. Fornecedores autorizados para feeds e históricos licenciados, com direitos compatíveis com o uso pretendido.

### 8.2 COTAHIST e históricos

O COTAHIST é uma referência conhecida para dados históricos de cotações da B3, mas o pipeline deve confirmar a página oficial, layout, versão, períodos disponibilizados, tipos de registro, codificação, delimitadores e política de utilização. Não assumir que um ficheiro anual está completo nem que todos os instrumentos/situações estão cobertos.

Regras de ingestão:
- guardar o ficheiro original sem alteração como **RAW**;
- registar URL de origem, data/hora de obtenção, tamanho, hash SHA-256, período declarado e versão do layout;
- validar header/trailer, número de registos e campos obrigatórios;
- converter os registos num modelo normalizado sem apagar o RAW;
- reconciliar amostras com outra fonte oficial e manter relatórios de divergências;
- tornar operações idempotentes; reprocessar a mesma fonte não deve duplicar o dataset canónico;
- distinguir dados em falta de valores zero;
- armazenar calendário, fuso horário e regra de sessão;
- guardar versão do parser e hashes de entrada/saída;
- não promover dados quando os gates falham; aplicar política fail-closed para falhas desconhecidas.

**Limite de verificação desta versão:** este documento não declara validado um lote COTAHIST específico nem comprova que o repositório contenha todos os ficheiros oficiais. Isso exige uma execução separada com os artefactos e relatórios concretos.

### 8.3 Market data em tempo real e licenciamento

A política comercial de market data da B3 para 2026 inclui categorias distintas de finalidade, tempestividade e acesso, com preços por dataset e versões com períodos de vigência. A versão consultada indica versão 1.0 com vigência de 01/01 a 31/10/2026 e versão 1.1 de 01/11 a 31/12/2026. O documento tem classificação de informação confidencial; antes de contratar, distribuir ou incorporar dados em produtos, confirmar a política vigente diretamente com a B3 e as condições contratuais aplicáveis. [18]

Não presumir que uma cotação visível num terminal, site ou aplicação autoriza recolha automatizada, redistribuição, armazenamento de longo prazo ou uso comercial. A página da B3 para certas consultas de opções indica expressamente restrições à coleta automatizada. [19] Definir claramente:
- uso pessoal versus distribuição para terceiros;
- display versus non-display/uso algorítmico;
- dados em tempo real, atrasados, snapshot ou históricos;
- direitos de armazenamento, derivados e redistribuição;
- proveniência e auditoria das licenças.

### 8.4 Modelo mínimo de registo de dados

Cada lote de dados deve ter:
```text
source_name
source_url
retrieved_at_utc
market_date
timezone
dataset_name
instrument_universe
source_file_name
source_file_size
source_sha256
schema_or_layout_version
parser_version
record_count_raw
record_count_normalized
duplicate_count
nulls_by_field
reconciliation_status
validation_status
license_status
commit_sha
```

## 9. Contexto macroeconómico e calendário

Para analisar ações, índice, dólar e juros, manter calendário separado por **data/hora local, timezone, fonte, consenso, valor divulgado, surpresa, revisão e classe de evento**.

Fontes úteis:
- **Banco Central do Brasil:** decisões e comunicados do Copom, atas, Relatório de Política Monetária, estatísticas, Focus e dados relacionados a juros e crédito.
- **IBGE:** IPCA, IPCA-15, PIB, emprego, produção industrial, comércio e serviços.
- **Tesouro Nacional:** dados e calendário de dívida pública e títulos.
- **Fontes externas oficiais:** Federal Reserve, U.S. Bureau of Labor Statistics, BEA e outras entidades quando o evento afeta USD, taxas globais e apetite ao risco.

O calendário de divulgação do IBGE consultado apresenta datas futuras para indicadores, incluindo IPCA; usar sempre a versão atualizada do calendário em vez de codificar datas de forma permanente. [20]

### 9.1 Interpretação para B3

- **Juros:** mudanças de expectativas podem afetar ações de duration longa, bancos, empresas alavancadas, DI1 e custo de capital; o efeito depende do nível de surpresa e do cenário.
- **Inflação:** medir surpresa contra consenso, revisões e componentes; não inferir a resposta do mercado apenas do valor absoluto.
- **Câmbio:** afeta empresas importadoras/exportadoras, commodities e ativos com receitas/dívidas em moeda estrangeira, com sensibilidades diferentes.
- **Commodities:** acompanhar preço internacional, câmbio, basis, oferta/demanda e eventos específicos de cada cadeia.
- **Eventos internacionais:** dados dos EUA, decisões de bancos centrais e risco geopolítico podem afetar USD/BRL, juros locais e fluxos para mercados emergentes.

## 10. Esquema analítico para fluxo e setups quantitativos

Esta secção é uma metodologia de pesquisa, não uma promessa de rentabilidade nem a validação de uma estratégia específica.

### 10.1 Pipeline de decisão

1. **Regime:** classificar a sessão com volatilidade, tendência/range, eventos macro, correlações e contexto do Ibovespa.
2. **Localização:** níveis do dia anterior, abertura, máxima/mínima da sessão, VWAP, zonas de liquidez e gaps claramente definidos.
3. **Participação:** volume financeiro, volume relativo, spread, profundidade e CVD, se os dados estiverem disponíveis e validados.
4. **Confirmação:** exigir evidências independentes e pré-definidas. Não usar vários indicadores derivados do mesmo preço como se fossem confirmações independentes.
5. **Execução:** especificar ordem, risco de slippage, horário, tamanho, spread, tick, margem e situação de leilão.
6. **Invalidação:** definir antecipadamente o nível e as condições que tornam a hipótese errada.
7. **Saída e gestão:** stop, alvo, time stop, redução de exposição e limite de perda diária.
8. **Avaliação:** testar fora da amostra, caminhar por janelas temporais e aplicar custos plausíveis.

### 10.2 Gap entre VWAPs, VWAP/TWAP, FVG e liquidez

Para tornar estas ideias testáveis:
- Definir matematicamente cada VWAP: início/fim da sessão, mercado incluído, tratamento de leilões e negócios fora de sessão.
- Definir a TWAP usada e a frequência de amostragem; resultados mudam conforme a implementação.
- Definir FVG com regras formais de candles, timeframe, tamanho mínimo, mitigação e expiração. Não tratar o conceito de FVG/ICT como facto institucional universal.
- Definir “paragem do mercado” em termos observáveis: redução de velocidade, absorção aparente, falha de continuação, queda de agressão líquida ou aumento de volume sem progresso de preço.
- Cruzar CVD com preço e volume financeiro, mas testar falsos positivos e regimes de mercado.
- Usar VIX como variável contextual de risco global; o VIX não mede diretamente a volatilidade implícita das opções sobre ativos brasileiros e não deve ser tomado como confirmação autónoma para WIN ou WDO.

### 10.3 Regras obrigatórias para cada setup

Cada estudo deve documentar:
- identificador e versão;
- mercado, contrato, timeframe e sessão;
- fonte e resolução dos dados;
- definição exata do sinal;
- entrada e tipo de ordem;
- stop estrutural e invalidação;
- alvo, trailing stop e time stop;
- sizing e risco monetário máximo por operação/dia;
- comissões, emolumentos, spread e slippage;
- tratamento de rolagens, ajustes, leilões e eventos;
- amostras de treino, validação e teste;
- número de trades, taxa de acerto, payoff, expectativa líquida, profit factor, drawdown máximo, retorno por unidade de risco, exposição e sensibilidade aos parâmetros;
- testes de robustez por ativo, horário e regime.

A taxa de acerto isolada não demonstra vantagem estatística. Um setup pode ganhar frequentemente e perder dinheiro se as perdas forem grandes ou os custos forem ignorados.

## 11. Backtesting e estatística

O motor de testes deve evitar leakage temporal, survivorship bias e look-ahead bias. A composição histórica de índices e eventos corporativos deve refletir o período efetivo, quando a estratégia requer esses dados.

Práticas mínimas:
1. Separação cronológica de treino, validação e teste; nunca embaralhar séries temporais como se fossem observações independentes.
2. Walk-forward com parâmetros escolhidos apenas com dados disponíveis até cada data.
3. Custos e slippage modelados de forma conservadora, variando por liquidez e horário.
4. Simular execução realista: sinal não significa preenchimento garantido.
5. Considerar limites de preço, gaps, leilões, latência, ordens rejeitadas e falhas de dados quando relevantes.
6. Fazer análise de sensibilidade e correção para seleção excessiva de parâmetros.
7. Comparar com benchmark apropriado, buy-and-hold quando pertinente e estratégia simples de referência.
8. Reportar resultados brutos e líquidos, incluindo períodos desfavoráveis.

## 12. Riscos que não podem ser omitidos

- **Mercado:** preço, taxas, câmbio, volatilidade e correlação.
- **Alavancagem:** perdas e chamadas de margem podem ocorrer rapidamente.
- **Liquidez/execução:** spread, slippage, livro insuficiente e gap.
- **Contraparte e financiamento:** garantias, regras de liquidação e custos.
- **Operacional:** erros de ordens, duplicação, timestamps, falhas de parser e conectividade.
- **Modelo:** overfitting, dados enviesados, hipótese não identificada e drift de regime.
- **Dados/licença:** origem não autorizada, dados alterados, uso redistribuído sem direito.
- **Regulatório/fiscal:** regras dependem do instrumento e do perfil do participante; confirmar informação vigente com profissional qualificado quando necessário.

Nenhum indicador, setup, algoritmo ou combinação de filtros garante ganhos. O objetivo da investigação é identificar se uma hipótese apresenta expectativa líquida positiva, robusta e reproduzível em condições realisticamente modeladas.

## 13. Automação, arquitetura e governança recomendadas para o repositório B3

### 13.1 Camadas

- **RAW:** ficheiros exatamente como descarregados, imutáveis; metadados, hashes e registo de origem.
- **STAGING:** parse e normalização com esquema versionado.
- **CANONICAL:** dados reconciliados, sem duplicação lógica, com regras explícitas de atualização.
- **ANALYTICS:** features, métricas, índices derivados e datasets prontos para testes.
- **STRATEGIES:** especificações, código, parâmetros, resultados e relatórios.
- **AUDIT:** logs, hashes, relatórios de validação, exceções e trilho de decisões.

### 13.2 Gates de qualidade

A promoção do dataset deve falhar de forma fechada quando houver erro desconhecido. Gates recomendados:
- hash e tamanho do RAW reconciliados;
- esquema/layout validado;
- contagem de registos compatível;
- campos obrigatórios presentes;
- duplicados explicados;
- cobertura temporal validada;
- amostra reconciliada com fonte canónica;
- licença e finalidade verificadas;
- testes do parser aprovados;
- commit e logs identificáveis.

### 13.3 Agendamento

Se houver ingestão regular, separar:
- recolha de fecho/boletim após a publicação oficial;
- validação e reconciliação;
- atualização canónica;
- auditoria;
- verificação final antes da abertura seguinte.

Os horários devem ser baseados no calendário e nas publicações reais da B3, com timezone explícito e tolerância a atrasos. Uma execução agendada não deve declarar sucesso só porque o workflow terminou: deve provar integridade, completude e reconciliação.

### 13.4 Estrutura de pastas proposta

A seguinte estrutura é uma proposta e não declara que as pastas já existam:

```text
BRAZIL SOTCK EXCHANGE/
├── README.md
├── 00_GOVERNANCA/
│   ├── METODOLOGIA.md
│   ├── REGISTO_DE_DECISOES.md
│   └── LICENCAS_E_FONTES.md
├── 01_DADOS/
│   ├── RAW/
│   ├── STAGING/
│   ├── CANONICAL/
│   └── ESQUEMAS/
├── 02_MICROESTRUTURA/
│   ├── VWAP_TWAP/
│   ├── VOLUME_CVD/
│   └── LIQUIDEZ/
├── 03_MACRO/
│   ├── CALENDARIO/
│   └── INDICADORES/
├── 04_ESTRATEGIAS/
│   ├── ESPECIFICACOES/
│   ├── NTSL/
│   └── BACKTESTS/
├── 05_RELATORIOS/
├── 06_AUDITORIA/
└── 07_FONTES_OFICIAIS/
```

## 14. Lista de verificação para manter este documento correto

- [ ] Confirmar fichas e contratos vigentes antes de codificar ticks, lotes, vencimentos ou fórmulas de P&L.
- [ ] Rever horários sempre que a B3 publicar ofício circular; as alterações sazonais internacionais podem mudar as janelas de negociação. O ofício 050/2026-VNC prevê alterações a partir de 26/10/2026 para determinados produtos estruturados e 03/11/2026 para grades de ações e derivativos. [21]
- [ ] Rever a política de market data e os contratos de licença antes de armazenamento ou distribuição.
- [ ] Rever texto consolidado da CVM e normas B3 antes de alterações no pipeline.
- [ ] Manter datas de calendário e timezones como dados versionados.
- [ ] Validar cada estratégia com backtest reproduzível e custos.
- [ ] Separar informação oficial, resultado calculado, hipótese e inferência.
- [ ] Nunca declarar COTAHIST ou qualquer dataset “validado” sem apontar para a execução, os hashes e o relatório de reconciliação correspondentes.

## 15. Fontes oficiais consultadas

Data de consulta: **26 de outubro de 2026**. Os links abaixo são pontos de partida; usar a versão corrente, e não apenas esta fotografia documental.

1. B3 — Perfil institucional: https://ri.b3.com.br/pt-br/b3/perfil/
2. B3 — Ações: https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/acoes.htm
3. B3 — Ibovespa: https://b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/ibovespa-b3.htm
4. B3 — Compensação, liquidação e gestão de risco: https://www.b3.com.br/pt_br/regulacao/estrutura-normativa/regulamentos-e-manuais/compensacao-liquidacao-e-gerenciamento-de-riscos.htm
5. B3 — Futuros de Ibovespa: https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/futuro-de-ibovespa.htm
6. B3 — Futuro mini de dólar: https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/moedas/futuro-mini-de-taxa-de-cambio-de-reais-por-dolar-comercial.htm
7. B3 — Futuro de DI: https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/futuro-de-taxa-media-de-depositos-interfinanceiros-de-um-dia.htm
8. B3 — Opções sobre ações: https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/opcoes-sobre-acoes.htm
9. CVM — Qual o papel da CVM?: https://www.gov.br/cvm/pt-br/acesso-a-informacao-cvm/perguntas-frequentes-da-cvm/teste-assunto/teste-combo-assunto
10. CVM — Resolução 135: https://conteudo.cvm.gov.br/legislacao/resolucoes/resol135.html
11. B3 — ETFs: https://www.b3.com.br/pt_br/produtos-e-servicos/solucoes-para-emissores/fundos-de-investimentos/etfs-fundos-de-indices/
12. B3 — Fundos imobiliários: https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/fundos-de-investimento-imobiliario-fii.htm
13. B3 — BDRs (introdução): https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/certificado-de-deposito-de-acoes-bdr.htm
14. B3 Educação — Mini índice: https://borainvestir.b3.com.br/glossario/mini-indice/
15. B3 Educação — Opções sobre ações: https://edu.b3.com.br/w/opcoes-acoes
16. CVM — Resolução 175: https://conteudo.cvm.gov.br/legislacao/resolucoes/resol175.html
17. B3 — Segmentos de listagem: https://www.b3.com.br/pt_br/produtos-e-servicos/solucoes-para-emissores/segmentos-de-listagem/sobre-segmentos-de-listagem/
18. B3 — Política comercial de Market Data 2026 (PDF): https://www.b3.com.br/data/files/20/35/7A/71/5CCFF91094DCD8F9AC094EA8/Politica%20Comercial%20de%20Market%20Data%20B3%202026%20V1.1.pdf
19. B3 — Consultas de opções / aviso de utilização: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/opcoes/
20. IBGE — IPCA e calendário de divulgação: https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-ipca.html ; https://www.ibge.gov.br/calendario-divulgacao.html
21. B3 — Ofício Circular 050/2026-VNC, novos horários de negociação (PDF): https://www.b3.com.br/data/files/99/B7/82/67/8A631A103BBB511AAC094EA8/OC%20050-2026-VNC%20NOVOS%20HORARIOS%20DE%20NEGOCIACAO_PT.pdf
22. B3 — Tesouro Direto / tarifas: https://www.b3.com.br/pt_br/produtos-e-servicos/tarifas/tarifas-de-tesouro-direto/

## 16. Histórico de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.0 | 2026-10-26 | Criação da referência inicial: instituição, instrumentos, microestrutura, pós-negociação, regulação, dados, macro, backtesting e governança. |

---
**Aviso:** documento de referência educacional e de engenharia de dados. Não constitui recomendação individual de investimento, parecer jurídico, interpretação fiscal nem validação de rentabilidade de qualquer estratégia.
