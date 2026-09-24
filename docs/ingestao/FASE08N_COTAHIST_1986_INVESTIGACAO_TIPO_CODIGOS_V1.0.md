# FASE 08N — Investigação dos Códigos de Tipo do Mercado a Termo

**Arquivo:** FASE08N_COTAHIST_1986_INVESTIGACAO_TIPO_CODIGOS_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Decodificação documental dos códigos históricos de Tipo e teste da hipótese de dimensão oculta na colisão K4 de 10/10/1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 08N dá continuidade à 08M e procura:

1. identificar a legenda dos códigos históricos de Tipo;
2. separar Tipo de Cxx;
3. verificar se códigos como PP-G, PB-G, PP-H e PP-C aparecem como classificação operacional;
4. procurar o mesmo título em Tipos diferentes;
5. testar associação documental com comprador, vendedor, corretora, comitente, taxa ou modalidade;
6. avaliar se Tipo pode explicar as duas linhas RAW 140808/140809.

## 2. Evidência contemporânea de 1986

O Jornal do Brasil de 05/06/1986 reproduz a tabela de Mercado a Termo da Bolsa de Valores de São Paulo com as colunas **Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**. A publicação também contém **Vigor PP C05**, além de outros títulos com códigos Cxx. citeturn0search0turn1search0

### Fato

A coluna Tipo existe documentalmente como coluna própria.

### Limitação

A fonte OCR não preserva uma legenda suficientemente clara que permita mapear cada código de Tipo para uma definição econômica.

## 3. Evidência de 1987

Publicações de 1987 mostram combinações como:

- Camig PP-G;
- Unipar PB-G;
- Cibran PP-G;
- Cotap PP-H;
- Vale Rio Doce PP-G;
- Vigor PP-G;
- Votec PP-G;
- Weg PP-G.

citeturn0search1turn1search1

Outra publicação de 1987 apresenta grande quantidade de ocorrências no formato **Título + PP/PB/OP + código alfabético**, mantendo os dados quantitativos e de preço. citeturn1search2

### Resultado

A evidência confirma a existência de uma convenção histórica de classificação/publicação além do simples código do ativo.

Porém, a pesquisa **não localizou legenda primária contemporânea suficiente para decodificar G, H, Q ou C05**.

## 4. Separação entre C05 e Tipo

A publicação de 1986 apresenta simultaneamente:

- Tipo como dimensão da tabela;
- Vigor PP C05 como identificação publicada.

Portanto:

**C05 NÃO pode ser convertido automaticamente em Tipo.**

A hipótese anterior “C05 = Tipo” permanece refutada como inferência de pipeline.

## 5. Teste de PP/PB/OP

Os registros históricos apresentam combinações como:

- PP;
- PB;
- OP;
- PA;
- PS;
- PN.

Essas siglas aparecem junto aos títulos em publicações históricas.

A pesquisa não encontrou fonte primária que permita afirmar, para 1986, que:

- PP = comprador;
- PB = vendedor;
- OP = operação própria;
- PA = agente específico;
- PS = vendedor específico.

### Estado

**NÃO DECODIFICADO.**

Não será criada tradução econômica automática.

## 6. Teste de códigos G/H/Q e outros

Foram observados:

- C05 em 1986;
- Cxx em diversos títulos em 1986;
- G e H em publicações de 1987;
- Q em formatos históricos posteriores.

A mudança de C05 para G/H/Q em publicações posteriores demonstra evolução da convenção de publicação, mas **não prova equivalência semântica entre os códigos**.

### Estado

**PADRÃO DOCUMENTAL OBSERVADO; SEMÂNTICA NÃO RESOLVIDA.**

## 7. Mesmo título em Tipos diferentes

A busca dirigida encontrou numerosos títulos com diferentes combinações históricas de classificação em diferentes datas.

Entretanto, **não foi localizada evidência primária suficientemente legível que demonstre, no mesmo pregão de 1986, o mesmo título e mesmo prazo simultaneamente em dois Tipos distintos**, de forma que permita associar essa diferença diretamente à colisão K4 de 10/10/1986.

Portanto, o teste decisivo permanece aberto.

## 8. Comprador/vendedor

A documentação regulatória mostra que operações a termo envolvem participantes/comitentes compradores e vendedores. Uma publicação normativa posterior descreve declarações de compra e venda e identifica separadamente Participantes e Comitentes. citeturn0search75turn0search2

Isso demonstra que comprador/vendedor e comitente são dimensões reais do mercado a termo.

**Não demonstra**, porém, que os códigos históricos PP/PB ou Tipo representassem essas dimensões no COTAHIST de 1986.

### Estado

**CONTEXTO CONFIRMADO; MAPEAMENTO PARA TIPO NÃO CONFIRMADO.**

## 9. Corretora/comitente

A documentação regulatória pesquisada confirma a existência de operações realizadas por corretoras por conta e ordem de clientes/comitentes. citeturn0search74

Novamente, isso não estabelece que a coluna Tipo histórica codificasse corretora, comitente ou contraparte.

### Estado

**NÃO CONFIRMADO.**

## 10. Taxa

A pesquisa confirma que taxa de juros faz parte das condições de determinadas operações a termo em documentação posterior. citeturn0search2

Não foi localizada fonte primária de 1986 que mostre a taxa como conteúdo da coluna Tipo ou que demonstre agregação do COTAHIST por taxa.

### Estado

**NÃO CONFIRMADO.**

## 11. Resultado sobre a colisão K4

Registro:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW: 140808 e 140809.

A FASE 08N não encontrou evidência suficiente para afirmar que a coluna Tipo explique a duplicidade.

### Classificação

**FATO**
- Tipo existia como dimensão publicada no Mercado a Termo.
- C05 não deve ser confundido com Tipo.
- Havia múltiplas convenções históricas de classificação/publicação.
- Comprador, vendedor, participante, comitente e taxa são dimensões reais do mercado a termo em documentação normativa.

**NÃO COMPROVADO**
- Tipo = comprador;
- Tipo = vendedor;
- Tipo = corretora;
- Tipo = comitente;
- Tipo = taxa;
- Tipo como chave de agregação do COTAHIST;
- Tipo como explicação das linhas 140808/140809.

## 12. Conclusão

A FASE 08N **não resolve a colisão K4**, mas reduz o espaço de hipóteses mal fundamentadas.

A evidência disponível permite afirmar que havia uma dimensão histórica denominada **Tipo**, independente de Prazo, e que a nomenclatura publicada evoluiu entre 1986 e 1987.

Não existe, contudo, documentação primária localizada que permita transformar os códigos históricos em semântica econômica segura.

Consequentemente, a hipótese operacional correta para o pipeline permanece:

> **Tipo é uma dimensão histórica potencialmente relevante, mas sua semântica e sua participação na regra de agregação do COTAHIST 1986 permanecem indeterminadas.**

## 13. Governança

- RAW permanece intocado.
- Linhas 140808 e 140809 permanecem separadas.
- C05 permanece literal.
- PP/PB/OP/PA/PS/PN permanecem literais.
- G/H/Q permanecem literais.
- Nenhum código recebe tradução econômica automática.
- Nenhuma linha é consolidada.
- Nenhuma causalidade é inferida.

## 14. Próxima frente

A FASE 08O deve abandonar a busca genérica e procurar **documentação primária de codificação**, priorizando:

1. manuais Bovespa 1985–1987;
2. boletins de especificação de operações a termo;
3. circulares de pregão;
4. tabelas de códigos de negócios;
5. documentos CVM/Bovespa com legendas de PP/PB/OP e G/H/Q;
6. BDI de 09/10, 10/10 e 13/10/1986;
7. comparação direta do Vigor em dias consecutivos.

O objetivo de 08O será encontrar a **legenda**, não gerar uma interpretação por analogia.

## 15. Estado

**IMPLEMENTADO:** investigação documental dirigida executada.

**EXECUTADO:** busca histórica 1986–1987 e documentação normativa relacionada ao mercado a termo.

**VALIDADO:**
- existência de Tipo;
- separação Tipo × Prazo;
- existência de C05 em 1986;
- existência posterior de PP-G/PB-G/PP-H;
- existência das dimensões comprador/vendedor/comitente/taxa no mercado a termo.

**NÃO VALIDADO:**
- legenda dos códigos;
- Tipo = comprador/vendedor;
- Tipo = corretora/comitente;
- Tipo = taxa;
- Tipo como chave de agregação;
- Tipo como causa da colisão K4.

**FASE 08N:** IMPLEMENTADA / EXECUTADA / VALIDADA quanto aos fatos documentais acima; causa da colisão permanece NÃO DETERMINADA.
