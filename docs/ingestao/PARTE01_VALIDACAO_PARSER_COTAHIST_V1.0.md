# PARTE 01 — VALIDAÇÃO DO PARSER COTAHIST V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-53AC69B90D13 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 19f4b8bb268f45b8d005a5cde98099f486c8894b6d698543f0736571f8e52c3e |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** PARTE01_VALIDACAO_PARSER_COTAHIST_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Validação estrutural e de qualidade da primeira normalização  
**Caminho:** docs/ingestao/PARTE01_VALIDACAO_PARSER_COTAHIST_V1.0.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## Escopo

A primeira validação automatizada usa o arquivo RAW COTAHIST de 1986 como caso de referência.

O manifesto do ano 1986 registra:

- arquivo: COTAHIST_A1986.ZIP;
- SHA-256: 350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018;
- 177.983 registros totais;
- 177.981 registros de cotação 01;
- registros de 245 bytes;
- header 00;
- trailer 99.

## Validações executadas pelo pipeline

### Estruturais

1. ZIP não vazio.
2. Exatamente um arquivo interno.
3. Parser aceita somente registros 01 para a camada NORMALIZED.
4. Cada registro 01 possui exatamente 245 bytes.
5. Campos são extraídos pelas posições do layout B3.
6. Datas são convertidas para ISO.
7. Preços são convertidos preservando duas casas decimais.
8. Campos vazios permanecem vazios.

### Qualidade

O pipeline calcula:

- número de linhas NORMALIZED;
- número de campos;
- primeira data;
- última data;
- datas estruturalmente inválidas;
- duplicidades da chave candidata.

### Chave candidata

data_pregao + codbdi + codneg + tpmerc + dismes

Esta chave é apenas **candidata**. A existência de duplicidades não será automaticamente tratada como erro sem análise do significado econômico e do estado de direito representado por dismes.

## Critério de aprovação

Um ano somente será liberado para normalização em escala quando:

- o RAW estiver VALIDADO;
- o parser completar sem erro;
- a saída NORMALIZED possuir registros;
- todos os campos obrigatórios existirem;
- não houver datas estruturalmente inválidas;
- as duplicidades forem medidas e classificadas;
- a evidência da execução estiver preservada como artefato.

## Importante

A ausência de ajuste de inflação, dividendos, bonificações ou outros eventos corporativos é intencional. A própria B3 informa que a série histórica é fornecida na moeda e forma de cotação da época, sem esses ajustes. 

Também não se deve interpretar COTAHIST como fluxo de ordens, agressão ou Cumulative Delta. Para esses estudos será necessária outra camada de dados.

## Estado

**RAW 1986:** VALIDADO.

**Parser:** implementado.

**Pipeline de teste:** implementado.

**Resultado quantitativo da NORMALIZED:** pendente da execução confirmada do GitHub Actions.

Não serão inventados números de normalização antes da execução efetiva.
