# FASE 08K — Arqueologia do BDI/COTAHIST — Estrutura Histórica da Tabela de Mercado a Termo

**Arquivo:** FASE08K_COTAHIST_1986_ARQUEOLOGIA_BDI_TABELA_TERMO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** reconstrução documental da estrutura de publicação do mercado a termo em 1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Localizar uma publicação contemporânea de 1986 que preserve a estrutura da tabela de Mercado a Termo da Bolsa de Valores de São Paulo e comparar suas colunas com os campos estatísticos e estruturais do COTAHIST.

A frente é documental. Não altera o RAW e não transforma a colisão K4.

## 2. Evidência contemporânea localizada

Foi localizada no Jornal do Brasil, edição de 05/06/1986, uma página com a seção da Bolsa de Valores de São Paulo e a tabela **Mercado a Termo**.

A publicação apresenta explicitamente a estrutura:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

e exemplos de linhas com **PP 030**, seguidos de quantidade, preços e número de negócios. A mesma página contém também os totais do mercado a termo. citeturn3view1turn4view0

A fonte também mostra a existência contemporânea da notação **Vigor PP C05**, além de outras combinações Cxx como Met Duque PP C45, Weg PP C35, Chapeco PP C15/C05 e Cia Hering PP C50. citeturn3view0

## 3. Reconstrução da tabela histórica

### 3.1 Colunas identificadas

| Coluna histórica | Evidência | Relação preliminar com COTAHIST |
|---|---|---|
| Tipo | publicado na tabela | provavelmente classe/tipo da operação; sem mapeamento direto confirmado |
| Prazo | publicado; exemplos 030 | compatível estruturalmente com PRAZOT |
| Quant | publicado | compatível com QUATOT |
| Fech | publicado | compatível com PREULT |
| Máx | publicado | compatível com PREMAX |
| Mín | publicado | compatível com PREMIN |
| Méd | publicado | compatível com PREMED |
| N° | publicado | compatível com TOTNEG |

**Importante:** os mapeamentos acima são de estrutura estatística, não uma prova de identidade semântica campo-a-campo do layout de 1986.

## 4. Evidência especialmente relevante para a colisão

A tabela contemporânea demonstra que o mercado a termo era publicado com uma combinação explícita de:

- tipo;
- prazo;
- quantidade;
- preços mínimo/médio/máximo/fechamento;
- número de negócios.

Isso é importante porque a colisão de 10/10/1986 possui o mesmo K4, inclusive **PRAZOT = 060**, mas apresenta agregados estatísticos diferentes.

### Linha RAW 140808
- TOTNEG = 1
- QUATOT = 39.000.000
- PREAB = PREMAX = PREMIN = PREMED = PREULT = 190 / 100 = 1,90
- VOLTOT = 74.100,00

### Linha RAW 140809
- TOTNEG = 4
- QUATOT = 190.000.000
- PREAB = 165 / 100 = 1,65
- PREMIN = 1,65
- PREMED = 1,87
- PREMAX = 1,91
- PREULT = 1,75
- VOLTOT = 356.460,00

A diferença entre os dois registros, portanto, não é apenas de preço final: envolve quantidade, número de negócios, faixa de preços e volume financeiro.

## 5. Nova leitura estrutural

**K4 não contém todos os campos estatísticos publicados na tabela.**

O K4 utilizado na investigação identifica:

`DATAPREGAO + CODBDI + CODNEG + TPMERC + CODISI + DIMES + ESPECI + PRAZOT + DATVEN + PREEXE + INDOPC + PTOEXE`

Enquanto os agregados estatísticos incluem, entre outros:

`PREAB + PREMAX + PREMIN + PREMED + PREULT + TOTNEG + QUATOT + VOLTOT + FATCOT`

Assim, duas linhas com K4 equivalente podem, em princípio, ser diferentes no nível dos agregados de negociação sem que a K4 tenha um campo estatístico que as diferencie.

Isso **não prova** que a Bovespa tenha deliberadamente publicado duas agregações para a mesma K4; apenas demonstra que a estrutura publicada separava identificação/contrato de estatísticas de negociação.

## 6. O que a evidência resolve

### FATO VALIDADO

1. Existia em 1986 uma tabela de Mercado a Termo da Bovespa publicada com **Tipo, Prazo, Quantidade, Fechamento, Máxima, Mínima, Média e Número de negócios**. citeturn3view1turn4view0
2. O prazo era explicitamente publicado; há exemplos de **030** na tabela. citeturn4view0
3. A notação Cxx fazia parte da publicação de papéis em 1986, incluindo **Vigor PP C05**. citeturn3view0
4. A publicação contemporânea comprova que quantidade, preços e número de negócios eram dimensões distintas na apresentação do mercado a termo. citeturn4view0

### NÃO RESOLVIDO

1. significado histórico exato de C05;
2. significado completo de VGO 2;
3. significado de DIMES 104;
4. regra que poderia produzir duas agregações com a mesma combinação de campos estruturais;
5. se a duplicidade representa uma regra de publicação, uma dimensão operacional omitida no COTAHIST ou um artefato de processamento.

## 7. Hipóteses reavaliadas

| Hipótese | Estado após 08K |
|---|---|
| diferença de prazo explica a colisão | **REFUTADA** pelas linhas com PRAZOT=060 |
| C05 surgiu no dia da colisão | **REFUTADA** pela publicação de junho de 1986 |
| DIMES 104 surgiu no dia da colisão | **REFUTADA** pela cronologia da FASE 08E |
| spot vs termo explica a duplicidade | **REFUTADA** |
| perfil estatístico raro explica a colisão | **REFUTADA** pela FASE 08G |
| fenômeno recorrente em outros anos | **REFUTADO** no universo 1986–2026 pela FASE 08H |
| taxa do termo é a chave oculta | **NÃO CONFIRMADA** |
| contraparte/comitê é a chave oculta | **NÃO CONFIRMADA** |
| regra histórica de agregação/publicação | **HIPÓTESE PRINCIPAL** |
| erro de processamento | **NÃO CONFIRMADO** |

## 8. Limitação documental

A fonte localizada é uma reprodução de imprensa contemporânea, não o BDI primário da Bovespa.

Ela é suficiente para validar a **estrutura pública da tabela**, mas não para reconstruir o manual interno de geração do COTAHIST.

Continua sendo **EVIDÊNCIA AUSENTE**:

- BDI primário de 10/10/1986;
- manual/layout interno de 1986;
- legenda oficial contemporânea de C05;
- regra formal de agregação que permita duas linhas com a mesma K4.

## 9. Governança de dados

- RAW: **intocado**.
- Registros 140808 e 140809: **preservados**.
- Nenhuma linha excluída.
- Nenhuma linha consolidada.
- Nenhuma identidade econômica inferida.
- Nenhuma causa histórica declarada como fato.

## 10. Próxima frente

1. localizar outras páginas de imprensa de 1986 com a mesma tabela de Mercado a Termo;
2. localizar exemplares de BDI/Bovespa de 1986–1987;
3. procurar legendas para a coluna **Tipo** e para códigos Cxx;
4. procurar documentação que explique se **Tipo/Prazo** eram suficientes para distinguir registros ou se havia dimensões adicionais;
5. procurar referências contemporâneas a **taxas negociadas no mercado a termo** e verificar se elas eram publicadas como tabela separada ou incorporadas à linha do ativo.

## 11. Status

**IMPLEMENTADO:** FASE 08K executada.

**EXECUTADO:** localizada e analisada publicação contemporânea de 1986 contendo a tabela de Mercado a Termo da Bovespa.

**VALIDADO:** estrutura histórica pública com Tipo, Prazo, Quant, Fech, Máx, Mín, Méd e N°; existência contemporânea de Vigor PP C05.

**NÃO VALIDADO:** regra causal da colisão K4 de 10/10/1986.

## 12. Fonte de pesquisa documental utilizada

- Jornal do Brasil, edição de 05/06/1986, reprodução digital consultada em 25/09/2026. A página contém a seção Bolsa de Valores de São Paulo / Mercado a Termo e a notação Vigor PP C05. citeturn3view0turn3view1turn4view0