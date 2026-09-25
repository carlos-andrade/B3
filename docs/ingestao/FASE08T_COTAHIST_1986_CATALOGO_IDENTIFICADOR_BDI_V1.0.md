# FASE 08T — Pesquisa de Catálogo e Identificador do BDI — COTAHIST 1986

**Arquivo:** FASE08T_COTAHIST_1986_CATALOGO_IDENTIFICADOR_BDI_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Identificação catalográfica do BDI de outubro de 1986 e preparação de solicitação institucional  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Transformar a busca institucional da FASE 08S em uma investigação catalográfica objetiva: identificar registros, coleções, identificadores, datas e mecanismos de acesso que possam levar ao BDI de 10/10/1986.

## 2. Resultado — MUB3

A busca oficial localizou o **Acervo do MUB3 — Museu da Bolsa do Brasil**. A página permite pesquisa por termos, tipo de registro e intervalo de datas.

A página de referência informa que o Centro de Referência reúne mais de 100 mil itens e disponibiliza o banco de dados do acervo. A documentação institucional identifica explicitamente a **Bovespa** como uma das organizações históricas representadas no acervo.

### Estado da consulta

O mecanismo público indexado não retornou, nesta execução, um registro catalográfico específico para `BDI`, `Boletim Diário de Informações`, `Bovespa` e `1986` simultaneamente.

Portanto:

**ACERVO CONFIRMADO / ITEM ESPECÍFICO NÃO IDENTIFICADO.**

## 3. Resultado — Hemeroteca Digital

A Biblioteca Nacional mantém a Hemeroteca Digital com páginas de periódicos organizadas por publicação, ano e edição/página. Foram localizados registros que demonstram a navegação por 1986 e páginas numeradas, inclusive PDFs de periódicos daquele ano.

Isso é relevante porque o caminho correto para reproduções de BDI em jornais passa por identificar primeiro o periódico e depois a edição/página do dia do pregão.

### Limitação

A busca textual pública não forneceu nesta execução uma reprodução verificável do BDI de 10/10/1986.

## 4. Nova estratégia de identificação

A investigação deixa de buscar somente o texto `10/10/1986 BDI Vigor` e passa a buscar o **identificador do objeto documental**.

### Alvos catalográficos

1. título do periódico/documento;
2. órgão produtor: Bolsa de Valores de São Paulo / Bovespa;
3. série: Boletim Diário de Informações;
4. data de emissão;
5. número da edição, se existente;
6. número da página;
7. código/ID do item no acervo;
8. suporte: papel, microfilme, digitalização ou fotografia;
9. coleção/fundo;
10. restrição de acesso;
11. possibilidade de reprodução.

## 5. Teste decisivo para o BDI de 10/10/1986

Quando o item for identificado, deverão ser extraídos integralmente:

- cabeçalho;
- data;
- seção Mercado a Termo;
- Vigor;
- Tipo;
- Prazo;
- Quant;
- Fech;
- Máx;
- Mín;
- Méd;
- Volume;
- N°;
- qualquer código adicional.

A comparação será feita contra:

`140808 → TOTNEG 1 / QUATOT 39.000.000 / preços 1,90`

`140809 → TOTNEG 4 / QUATOT 190.000.000 / PREAB 1,65 / PREMED 1,87 / PREMAX 1,91 / PREULT 1,75`

Não será feita correspondência por aproximação visual sem validação campo a campo.

## 6. Solicitação institucional — preparação

Caso o item não esteja publicamente disponível, a solicitação ao Centro de Referência B3 deve pedir especificamente:

> Pesquisa no acervo histórico da Bovespa por exemplar do Boletim Diário de Informações (BDI) referente ao pregão de 10 de outubro de 1986, preferencialmente incluindo a seção Mercado a Termo, bem como exemplares de 9 e 13 de outubro de 1986. Solicita-se, se existente, o identificador catalográfico, número da edição/página, formato disponível e possibilidade de consulta ou reprodução.

Essa redação será usada como base documental, sem presumir que o acervo contenha o item.

## 7. Hipóteses e evidência

| Questão | Estado |
|---|---|
| MUB3 possui acervo histórico relevante | CONFIRMADO |
| Bovespa está representada no acervo institucional | CONFIRMADO |
| Existe registro público específico do BDI 10/10/1986 localizado nesta execução | NÃO LOCALIZADO |
| Hemeroteca possui material de 1986 | CONFIRMADO |
| Hemeroteca forneceu o BDI-alvo nesta execução | NÃO LOCALIZADO |
| C05 = Tipo | NÃO DEMONSTRADO |
| Tipo explica a colisão | NÃO DEMONSTRADO |
| Regra de agregação explicada | NÃO RESOLVIDO |

## 8. Governança

- RAW intocado.
- Linhas 140808/140809 preservadas.
- Nenhuma transformação semântica aplicada.
- Nenhuma consolidação estatística.
- Nenhuma identidade econômica inferida.
- Evidência ausente permanece explicitamente classificada como tal.

## 9. Estado

**IMPLEMENTADO:** estratégia catalográfica e solicitação institucional preparadas.  
**EXECUTADO:** pesquisa no acervo público MUB3 e Hemeroteca Digital.  
**VALIDADO:** existência do acervo MUB3 e de sua base pública; existência de cobertura Hemeroteca para 1986.  
**NÃO RESOLVIDO:** identificador específico e exemplar primário do BDI de 10/10/1986.

## 10. Próxima frente — FASE 08U

A próxima frente deve executar a **solicitação institucional formal e a busca bibliográfica cruzada**, priorizando:

1. Centro de Referência MUB3;
2. catálogos universitários;
3. bibliotecas com coleções de Bovespa;
4. Biblioteca Nacional;
5. CVM;
6. arquivos de jornais de São Paulo/Rio;
7. identificação de número de edição/página do BDI.

Critério de resolução:

**identificador documental → exemplar primário → tabela Mercado a Termo → correspondência com 140808/140809 → regra histórica demonstrável.**
