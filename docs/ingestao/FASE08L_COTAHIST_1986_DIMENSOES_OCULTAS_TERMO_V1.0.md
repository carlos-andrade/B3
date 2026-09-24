# FASE 08L — Dimensões Ocultas do Mercado a Termo — Tipo, C05 e Agregação

**Arquivo:** FASE08L_COTAHIST_1986_DIMENSOES_OCULTAS_TERMO_V1.0.md
**Projeto:** B3 - A BOLSA DO BRASIL
**Tema:** investigação documental das dimensões não capturadas pela K4
**Data:** 25/09/2026
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Testar, com publicações históricas adicionais, se a coluna **Tipo** do Mercado a Termo ou a convenção **Cxx** fornecem uma dimensão capaz de explicar a colisão K4 de 10/10/1986.

## 2. Evidência de 1986

O Jornal do Brasil de 05/06/1986 apresenta a tabela de Mercado a Termo com as colunas **Tipo, Prazo, Quant, Fech, Máx, Mín, Méd e N°**. Há linhas com prazo 030 e códigos de papel como Vigor PP C05. citeturn1search0turn2search1

Isso permite uma distinção importante:

- **PP C05** aparece associado à identificação do papel na publicação;
- **Tipo/Prazo** aparecem como dimensões próprias da tabela de operações a termo;
- quantidade, preços e número de negócios aparecem como agregados da negociação.

Não foi encontrada, nessa fonte, uma legenda que faça C05 equivaler à coluna Tipo.

## 3. Evidência adicional de 1987

Uma publicação histórica de dezembro de 1987 apresenta explicitamente uma tabela de **Termo 30 Dias**, com estrutura semelhante, incluindo **Título, Abert., Mín., Méd., Máx., Fechto, Quant**. Nessa mesma publicação aparecem títulos com códigos Cxx, incluindo Agroceres PP C05 e Duratex PP C05. citeturn2search0

Outra publicação de 1987 reproduz Vigor PP C05 e mostra o padrão Cxx associado ao título, não como substituto evidente da informação de prazo do contrato. citeturn2search2

## 4. Evidência de 1988 — teste de persistência da estrutura

Uma publicação do Jornal do Brasil de 27/12/1988 apresenta a tabela **Operações a Termo** com as colunas:

**Títulos | Tipo | Prazo | Quant. (mil) | Fech. | Máx. | Min. | Méd. | Volume | Nº neg.**

Os exemplos mostram **PP-Q** como Tipo e **030** como Prazo. citeturn1search29

Esse achado é relevante porque demonstra que, em período posterior, **Tipo** e **Prazo** eram campos separados. Portanto, não há base documental para tratar C05 como sinônimo de Tipo.

## 5. C05 — resultado semântico

Nas fontes pesquisadas, C05 aparece em combinações como:

- Vigor PP C05;
- Agroceres PP C05;
- Duratex PP C05;
- Chapeco PP C05.

A repetição entre emissores demonstra que C05 é uma convenção de identificação/publicação reutilizada entre papéis. citeturn1search0turn2search0turn2search2

**Não foi localizada legenda documental suficiente para afirmar o significado econômico exato do número 05.**

Consequentemente, C05 não será convertido para uma categoria econômica no pipeline.

## 6. Tipo — resultado estrutural

A evidência de 1988 fornece uma decomposição documental clara:

`Título → Tipo → Prazo → Quant → preços → Volume → Nº negócios`

Isso é consistente com a hipótese de que o campo Tipo representa uma dimensão operacional/classificatória da operação a termo, enquanto Cxx pertence à identificação do título.

Entretanto, essa evidência é posterior a 1986. Ela **não prova que a codificação de Tipo em 1988 seja idêntica à de 1986**.

## 7. Aplicação à colisão K4

A colisão de 10/10/1986 possui:

`CODBDI=62 | TPMERC=030 | CODNEG=VGO 2 | CODISI=VGORACPP | DIMES=104 | ESPECI=PP *C05 | PRAZOT=060`

As duas linhas têm a mesma combinação desses campos, mas:

- TOTNEG = 1 versus 4;
- QUATOT = 39 milhões versus 190 milhões;
- preços completamente diferentes;
- VOLTOT = 74.100 versus 356.460.

Se a dimensão Tipo estivesse presente de forma distinta entre as duas linhas, ela teria de estar registrada em algum campo diferente da K4 investigada. A RAW disponível não apresenta tal diferença.

Portanto, a investigação agora separa duas possibilidades:

1. **dimensão operacional adicional não preservada no COTAHIST**;
2. **regra histórica de agregação/publicação que gerou duas linhas estatísticas para a mesma chave estrutural**.

## 8. Hipóteses

| Hipótese | Estado após 08L |
|---|---|
| C05 é o campo Tipo | **REFUTADA / SEM EVIDÊNCIA** |
| C05 identifica o prazo | **REFUTADA** |
| Tipo e Prazo são a mesma dimensão | **REFUTADA pela evidência posterior de estrutura separada** |
| C05 explica a colisão | **NÃO CONFIRMADA** |
| Tipo oculto explica a colisão | **POSSÍVEL, NÃO COMPROVADO** |
| dimensão operacional não preservada na K4 | **POSSÍVEL** |
| regra histórica de agregação | **HIPÓTESE PRINCIPAL** |
| erro de processamento | **NÃO CONFIRMADO** |

## 9. Resultado técnico

FASE 08L **não encontrou a chave oculta** que explique a colisão.

Encontrou, porém, uma evidência estrutural importante: **Tipo, Prazo e Cxx devem ser tratados como conceitos potencialmente distintos**, e não devem ser colapsados em uma única variável.

Isso reduz uma fonte relevante de erro semântico no pipeline histórico.

## 10. Regra para o pipeline B3

Até existir documentação primária:

- `ESPECI = PP *C05` será preservado literalmente;
- `PRAZOT = 060` será preservado como prazo de 60 dias/código 060, conforme o layout;
- nenhum valor de C05 será convertido em classe econômica;
- nenhuma coluna Tipo será inferida a partir de C05;
- a colisão K4 permanecerá como duas linhas RAW;
- nenhuma consolidação estatística será realizada.

## 11. Próxima frente

**FASE 08M — Busca documental dirigida pela coluna Tipo.**

Objetivos:

1. localizar tabelas de Mercado a Termo de 1986 com diferentes Tipos para o mesmo título;
2. comparar Tipo × Prazo × Cxx;
3. localizar legendas de códigos de Tipo;
4. procurar documentos Bovespa/CVM que descrevam as classes de operação a termo;
5. verificar se havia agrupamento por corretora, comitente, taxa, vendedor/comprador ou outra dimensão operacional.

## 12. Status

**IMPLEMENTADO:** investigação documental 08L executada.

**EXECUTADO:** fontes de 1986, 1987 e 1988 comparadas.

**VALIDADO:** Cxx não deve ser tratado como sinônimo documental de Tipo; Tipo e Prazo aparecem como dimensões separadas em publicação posterior.

**NÃO VALIDADO:** regra histórica de 1986 capaz de explicar a colisão K4.

**RAW:** intocado.