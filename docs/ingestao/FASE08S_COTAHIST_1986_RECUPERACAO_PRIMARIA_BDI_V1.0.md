# FASE 08S — Recuperação Primária Dirigida do BDI — COTAHIST 1986

**Arquivo:** FASE08S_COTAHIST_1986_RECUPERACAO_PRIMARIA_BDI_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Recuperação do exemplar primário do BDI de outubro de 1986 e reconstrução de sua estrutura  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 08S concentra a investigação no caminho institucional identificado na 08R: localizar no acervo da B3/Museu B3 e em hemerotecas públicas o material primário ou reprodução contemporânea do BDI de 10/10/1986, com prioridade para a seção Mercado a Termo.

## 2. Descoberta institucional confirmada

A página oficial do Centro de Memória B3 informa que o centro guarda e preserva documentos e objetos que contam a história do mercado de capitais brasileiro e da B3, possui acervo superior a 100.000 itens e permite pesquisa pelo acervo digital ou presencialmente mediante agendamento.

O link institucional conduz ao acervo digital do Museu B3 (`mub3.org.br/acervo`). A interface recuperada pelo mecanismo de pesquisa não permite consulta textual sem JavaScript, portanto a existência do acervo foi confirmada, mas não foi possível extrair, nesta execução, um registro catalográfico do BDI de 10/10/1986.

## 3. Hemeroteca Digital

A Hemeroteca Digital da Biblioteca Nacional disponibiliza acervos de periódicos históricos e apresenta navegação por ano, incluindo 1986. Foram localizadas páginas de acervo digital que confirmam a disponibilidade de periódicos desse período.

Entretanto, a execução desta fase não recuperou uma página de jornal de 10/10–14/10/1986 contendo o BDI integral ou as duas linhas Vigor da colisão.

## 4. Busca nominal do evento

Foram testadas combinações com:

- `10/10/1986`;
- `13/10/1986`;
- `Vigor`;
- `VGO 2`;
- `PP C05`;
- `Mercado a Termo`;
- `Bovespa`;
- `BDI`.

Não foi localizado exemplar público verificável do BDI de 10/10/1986 nem reprodução suficiente para identificar as duas agregações do Vigor.

## 5. Resultado probatório

A FASE 08S produziu uma descoberta de infraestrutura documental, mas não a peça primária desejada.

### Confirmado

1. A B3 possui acervo institucional histórico relevante.
2. O acervo digital do Museu B3 está vinculado oficialmente ao Centro de Memória.
3. A Hemeroteca Digital da Biblioteca Nacional possui cobertura de periódicos de 1986.

### Não localizado

1. BDI de 10/10/1986.
2. BDI de 09/10/1986.
3. BDI de 13/10/1986.
4. Legenda primária de C05.
5. Legenda primária da coluna Tipo.
6. Norma Bovespa de 1985–1987 que explique diretamente a colisão K4.

## 6. Estrutura que deverá ser extraída quando o BDI for recuperado

A análise deve preservar separadamente, sem normalização prematura:

- título;
- Tipo;
- Prazo;
- Quantidade;
- Fechamento;
- Máxima;
- Mínima;
- Média;
- Volume, quando presente;
- Número de negócios;
- eventuais códigos ou classificações adicionais;
- cabeçalho da seção;
- página do BDI;
- data do boletim;
- fonte física/digital e identificador do acervo.

A finalidade é comparar diretamente a estrutura publicada com os campos COTAHIST:

`ESPECI ↔ Tipo/publicação` — hipótese a testar, não equivalência assumida.

`PRAZOT ↔ Prazo` — correspondência estrutural já documentada.

`QUATOT ↔ Quantidade` — correspondência estrutural a validar no exemplar.

`PREULT ↔ Fechamento`, `PREMAX ↔ Máxima`, `PREMIN ↔ Mínima`, `PREMED ↔ Média`, `TOTNEG ↔ Número de negócios` — correspondências estruturais já observadas, ainda sujeitas à validação documental primária.

## 7. Relação com a colisão K4

O objetivo não é apenas localizar Vigor no BDI. O teste decisivo será verificar se o boletim de 10/10/1986 apresenta:

1. duas linhas para Vigor no mesmo prazo;
2. duas classificações Tipo distintas;
3. alguma taxa ou código adicional distinto;
4. duas agregações com quantidades e números de negócios compatíveis com as linhas RAW 140808 e 140809;
5. uma regra editorial/operacional que explique a coexistência das duas linhas.

Se uma dessas estruturas for encontrada, ela será comparada campo a campo com o COTAHIST antes de qualquer conclusão causal.

## 8. Governança

- RAW permanece intocado.
- Linhas 140808 e 140809 permanecem preservadas.
- Nenhuma equivalência C05/Tipo foi criada.
- Nenhuma taxa foi inferida.
- Nenhuma identidade econômica foi inferida.
- Nenhuma linha foi consolidada.
- Nenhuma estatística foi reescrita.

## 9. Estado da FASE 08S

**IMPLEMENTADO:** frente de recuperação primária BDI estruturada.  
**EXECUTADO:** consulta institucional B3/Museu B3, Hemeroteca Digital e busca nominal dirigida às datas/códigos do evento.  
**VALIDADO:** existência e acesso institucional ao acervo histórico B3; cobertura de periódicos de 1986 na Hemeroteca Digital.  
**NÃO RESOLVIDO:** recuperação do exemplar primário do BDI de 10/10/1986 e causa da colisão K4.  
**EVIDÊNCIA AUSENTE:** BDI primário/reprodução verificável do pregão de 10/10/1986.

## 10. Próxima frente

A investigação deve continuar por **FASE 08T — pesquisa de catálogo/identificador e solicitação institucional**, concentrando-se em:

1. identificar no acervo digital B3/Museu B3 termos e identificadores relacionados a `Boletim Diário de Informações`, `BDI`, `Bovespa`, `1986`, `Mercado a Termo`;
2. reconstruir a edição/data a partir de catálogos e jornais contemporâneos;
3. identificar eventual número de página/seção do BDI;
4. procurar reproduções integrais em bibliotecas universitárias e catálogos bibliográficos;
5. preparar uma requisição documental precisa para o acervo institucional, caso o exemplar não esteja publicamente digitalizado.

O critério de resolução permanece:

**fonte primária → estrutura publicada → regra histórica → relação demonstrável com as linhas 140808/140809.**
