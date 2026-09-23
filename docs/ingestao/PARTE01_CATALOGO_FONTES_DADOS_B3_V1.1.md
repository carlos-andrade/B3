# PARTE01 — Catálogo de Fontes de Dados B3 para Ingestão e Backtests

**Arquivo:** PARTE01_CATALOGO_FONTES_DADOS_B3_V1.1.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Tema:** Inventário histórico completo de fontes de dados para ingestão e backtests  
**Caminho:** docs/ingestao/PARTE01_CATALOGO_FONTES_DADOS_B3_V1.1.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3  
**Status:** V1.1 — marco temporal oficial atualizado

## 1. Regra permanente do projeto

> **MARCO TEMPORAL OFICIAL DO PROJETO B3: 1986.**

A partir desta versão, o projeto B3 passa a ter como objetivo preservar e ingerir **toda a série histórica de cotações disponibilizada pela B3 desde 1986**, até o período mais recente disponível.

O horizonte **1990 → atual** deixa de ser o marco principal. 1990 continua sendo um subconjunto útil para determinadas análises, mas **1986 é o marco oficial**.

Esta regra deve orientar:
- aquisição;
- armazenamento;
- normalização;
- controle de cobertura;
- validação;
- versionamento;
- backtests;
- documentação.

## 2. Escopo da série histórica de cotações

A prioridade P0 inclui a série histórica de cotações da B3 desde 1986, preservando os arquivos originais quando disponibilizados.

A série deverá ser mantida em duas formas:

### RAW
Arquivo original fornecido pela fonte, sem alteração.

### NORMALIZED
Representação canônica para consultas e backtests.

A existência de uma camada NORMALIZED **nunca substitui o RAW**.

## 3. Campos históricos

Sempre que presentes na fonte, preservar:
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
- volume negociado;
- demais campos fornecidos pelo layout original.

Campos adicionais devem ser preservados mesmo que ainda não tenham utilização no backtest.

## 4. Regra de cobertura

O objetivo é:

**1986 → último dado oficialmente disponível**

Não devemos:
- preencher lacunas com valores inventados;
- criar continuidade artificial;
- substituir dados ausentes sem identificação;
- misturar fontes sem registrar a origem;
- aplicar ajustes irreversíveis ao RAW.

Cada dataset deverá informar:
- primeira data efetivamente disponível;
- última data efetivamente disponível;
- pregões cobertos;
- pregões ausentes;
- instrumentos cobertos;
- campos disponíveis;
- alterações de layout;
- alterações de metodologia;
- alterações de código;
- instrumentos descontinuados e sucessores, quando identificáveis.

## 5. Relação com BVBG.028.02

O **BVBG.028.02 permanece como uma das fontes fundamentais**, mas não representa sozinho o universo histórico.

Ele deverá funcionar como parte do **Instrument Master**, auxiliando na identificação e normalização dos instrumentos.

A série histórica de cotações desde 1986 será tratada como uma fonte histórica própria e será relacionada ao Instrument Master sempre que houver chaves suficientes.

## 6. Backtests

A base histórica de cotações desde 1986 será o fundamento para:

- estudos de longo prazo;
- retornos;
- volatilidade;
- gaps;
- regimes de mercado;
- comportamento de ativos;
- análise de volume;
- estudos de índices;
- validação de hipóteses;
- backtests EOD;
- construção de amostras para modelos intraday quando houver dados de granularidade suficiente.

## 7. Limitação metodológica

A série histórica de cotações **não deve ser confundida com microestrutura intraday**.

OHLC, volume financeiro e número de negócios não são equivalentes a:
- agressão;
- Cumulative Delta;
- livro de ofertas;
- Market by Order;
- Market by Price;
- fluxo institucional.

Essas dimensões serão ingeridas separadamente quando os dados históricos correspondentes estiverem disponíveis.

## 8. Prioridade atual

### P0 — aquisição imediata

1. **Série histórica de cotações B3 — desde 1986**
2. **BVBG.028.02**
3. BVBG.029.02
4. BVBG.086.01
5. BVBG.087.01
6. BVBG.186.01
7. BVBG.187.01

### P1 — complementação histórica

- negócios;
- derivativos;
- contratos;
- ajustes;
- posições em aberto;
- opções;
- volatilidade;
- after-hours;
- demais arquivos históricos relevantes.

### P2 — microestrutura

- intraday;
- ticks;
- agressão;
- book;
- dados necessários para reconstrução de fluxo.

## 9. Critério BACKTEST-READY

Nenhuma série será declarada pronta apenas porque o arquivo foi baixado.

Será necessário validar:

1. cobertura temporal;
2. integridade;
3. duplicidade;
4. consistência de preços;
5. consistência de volume;
6. identificação dos instrumentos;
7. mudanças corporativas/metodológicas aplicáveis;
8. mudanças de layout;
9. gaps de dados;
10. rastreabilidade RAW → NORMALIZED.

## 10. Próxima etapa operacional

A próxima etapa da PARTE01 é localizar e catalogar **todos os arquivos oficiais da série histórica de cotações B3 desde 1986**, registrar seus períodos, formatos e layouts, e então construir o pipeline de ingestão no repositório.

**Não considerar a etapa concluída até que a matriz de cobertura demonstre exatamente quais anos, pregões, instrumentos e campos foram efetivamente obtidos.**
