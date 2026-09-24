# FASE 08O — Legenda Primária dos Códigos de Tipo — COTAHIST 1986

**Arquivo:** FASE08O_COTAHIST_1986_LEGENDA_PRIMARIA_TIPO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Busca dirigida da legenda histórica de Tipo no Mercado a Termo  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 08O foi aberta para tentar recuperar uma **legenda primária ou quase primária** dos códigos históricos usados na coluna **Tipo** do Mercado a Termo e verificar se essa dimensão pode explicar a colisão K4 de 10/10/1986.

Prioridades:

1. manuais/regulamentos Bovespa de 1985–1987;
2. tabelas de códigos;
3. circulares e especificações do Mercado a Termo;
4. BDI de 09/10, 10/10 e 13/10/1986;
5. comparação direta da publicação de Vigor nos pregões próximos.

## 2. Resultado da busca

A busca pública dirigida em 25/09/2026 **não localizou uma legenda primária contemporânea suficiente para decodificar os códigos históricos de Tipo**.

Também não foi localizada uma cópia pública verificável do BDI da Bovespa de 09/10, 10/10 ou 13/10/1986 que permita reconstruir diretamente a publicação do evento-alvo.

Portanto, **não foi realizada conversão semântica dos códigos PP/PB/OP/PA/PS/PN ou dos sufixos G/H/Q**.

## 3. Evidência contemporânea localizada

### 3.1 Jornal do Brasil — 05/06/1986

A publicação contemporânea apresenta a tabela do Mercado a Termo com a estrutura:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

A mesma publicação registra **Vigor PP C05** e diversos outros códigos Cxx.

Isso confirma:

- a coluna Tipo existia na publicação de mercado;
- Tipo era apresentado separadamente de Prazo;
- Vigor PP C05 era uma notação pública anterior ao evento de outubro;
- C05 não pode ser usado como se fosse automaticamente o código da coluna Tipo.

Fonte: Jornal do Brasil, 05/06/1986, acervo de imprensa histórica.

### 3.2 Publicações posteriores de 1987

Foram localizadas publicações de 1987 com combinações como:

- PP-G;
- PB-G;
- PP-H;
- Vigor PP-G;
- outros títulos com padrões semelhantes.

Essas fontes são úteis para demonstrar a persistência de uma dimensão classificatória histórica, mas **não são prova suficiente da legenda usada em 1986**.

### 3.3 Documentação normativa

A pesquisa também encontrou documentação normativa posterior e fontes regulatórias que demonstram que operações a termo envolvem dimensões como:

- comprador;
- vendedor;
- participante;
- comitente;
- taxa;
- prazo.

Essas dimensões são relevantes para a hipótese de uma variável operacional não preservada na K4, mas **não foi encontrada uma fonte primária que faça o mapeamento Tipo = uma dessas dimensões em 1986**.

## 4. Resultado sobre a hipótese Tipo

| Hipótese | Resultado |
|---|---|
| C05 = Tipo | **REFUTADA COMO EQUIVALÊNCIA AUTOMÁTICA** |
| Tipo = Prazo | **REFUTADA** |
| Tipo = comprador | **NÃO CONFIRMADA** |
| Tipo = vendedor | **NÃO CONFIRMADA** |
| Tipo = corretora/participante | **NÃO CONFIRMADA** |
| Tipo = comitente | **NÃO CONFIRMADA** |
| Tipo = taxa | **NÃO CONFIRMADA** |
| Tipo separa as linhas 140808/140809 | **NÃO CONFIRMADA** |
| Regra histórica de agregação/publicação | **HIPÓTESE PRINCIPAL** |
| Erro de processamento | **NÃO CONFIRMADO** |

## 5. Ponto importante para a colisão K4

O resultado da FASE 08O **não elimina** a hipótese de uma dimensão operacional adicional.

Ele apenas estabelece que, com a documentação pública recuperada até agora:

> não é possível atribuir um significado econômico aos códigos históricos de Tipo sem uma legenda contemporânea confiável.

Assim, a colisão continua sendo tratada como:

- duas linhas RAW;
- mesma K4 investigada;
- estatísticas diferentes;
- evento único no universo multianual 1986–2026 analisado;
- causa histórica não determinada.

## 6. Evidência ausente

Continuam prioritários:

1. BDI Bovespa de 09/10/1986;
2. BDI Bovespa de 10/10/1986;
3. BDI Bovespa de 13/10/1986;
4. manual/regulamento Bovespa de Mercado a Termo vigente em 1986;
5. tabela histórica oficial de códigos de Tipo;
6. circular ou procedimento operacional contemporâneo que defina PP/PB/OP/PA/PS/PN;
7. definição oficial dos sufixos G/H/Q;
8. regra de agregação utilizada na geração das tabelas/COTAHIST.

**Ausência de localização pública não deve ser interpretada como inexistência do documento.**

## 7. Governança de dados

- RAW permanece intocado.
- Linhas 140808 e 140809 permanecem preservadas.
- C05 permanece literal como publicado.
- VGO 2 permanece literal.
- DIMES 104 permanece literal.
- DATVEN 99991231 permanece literal.
- Nenhuma consolidação estatística é realizada.
- Nenhuma identidade econômica é inferida.
- Nenhuma causalidade é atribuída à coluna Tipo.

## 8. Estado da FASE 08O

**IMPLEMENTADO:** busca documental dirigida executada.

**EXECUTADO:** consultas específicas sobre legenda de Tipo, manuais Bovespa, BDI e Vigor nos pregões próximos.

**VALIDADO:** ausência de legenda primária suficiente nas fontes públicas recuperadas; existência histórica de Tipo separado de Prazo; existência de Vigor PP C05 antes de outubro de 1986.

**NÃO RESOLVIDO:** legenda dos códigos históricos e relação causal com a colisão K4.

## 9. Próxima frente controlada

A próxima frente deve deixar de repetir buscas genéricas e avançar em duas linhas de evidência:

### A — Arquivos institucionais

Buscar acervos físicos/digitalizados de:

- Bovespa/B3;
- CVM;
- Biblioteca Nacional;
- Senado/Diário Oficial;
- FGV e acervos universitários;
- jornais com reprodução integral do BDI.

### B — Reconstrução interna no COTAHIST

Usar somente os dados já preservados para testar:

1. Vigor em 09/10, 10/10 e 13/10/1986;
2. Tipo/Cxx por pregão quando recuperável em fonte documental;
3. existência de múltiplas linhas do mesmo título com diferentes classes publicadas;
4. relação entre PRAZOT, ESPECI, DIMES e estatísticas;
5. qualquer padrão que permita falsificar a hipótese de agregação.

## 10. Conclusão

A FASE 08O **não encontrou a legenda primária procurada**.

O resultado é útil porque evita uma falsa decodificação dos códigos históricos.

A hipótese de que uma dimensão operacional adicional possa ter existido permanece aberta, mas **não há evidência suficiente para afirmar que Tipo explique as duas linhas da colisão K4 de 10/10/1986**.

A investigação histórica permanece aberta e auditável.
