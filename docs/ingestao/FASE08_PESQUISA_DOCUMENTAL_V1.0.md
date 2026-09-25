# FASE 08 — Pesquisa Documental Histórica — COTAHIST 1986

**Arquivo:** FASE08_PESQUISA_DOCUMENTAL_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Pesquisa documental da colisão K4 de 10/10/1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Investigar fontes contemporâneas capazes de explicar:

1. a convenção histórica VGO 2;
2. o código C05 em ESPECI = PP *C05;
3. DATVEN = 99991231;
4. a coexistência de duas linhas com K4 idêntica e agregados de negociação diferentes;
5. a semântica histórica do mercado a termo no registro-alvo.

## 2. Registro-alvo

19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0

Linhas RAW: 140808 e 140809.

## 3. Evidência documental localizada

### 3.1 Jornal do Brasil — 05/06/1986

Foi localizada uma publicação contemporânea de 05/06/1986 contendo tabela de cotações da Bovespa. A tabela registra Vigor PP C05 e apresenta outras ocorrências do padrão Cxx, como Weg PP C35, Metal Duque PP C45 e Brahma OP C15.

A evidência demonstra que a identificação Vigor PP C05 existia publicamente antes do registro-alvo de outubro de 1986 e que a notação Cxx era usada para múltiplos papéis.

A fonte não apresenta legenda suficiente para decodificar o número 05.

## 4. O que a pesquisa não resolveu

Continuam sem documentação primária suficiente:

- legenda oficial contemporânea para C05;
- significado completo de VGO 2;
- significado histórico de DIMES 104;
- significado de DATVEN = 99991231;
- regra documental explicando duas linhas com K4 idêntica e agregados diferentes;
- legenda dos códigos históricos de Tipo;
- relação entre Tipo e a colisão K4.

## 5. Semântica atualmente sustentada

| Elemento | Estado |
|---|---|
| CODBDI 62 | Mercado a termo — documentado pelo layout B3 |
| TPMERC 030 | Termo — documentado pelo layout B3 |
| PRAZOT 060 | Campo de prazo do termo; valor 60 — documentado |
| VGO 2 | Código histórico observado; sem decodificação completa |
| VGORACPP | Código interno histórico observado |
| DIMES 104 | Campo de distribuição/estado de direito; sem reconstrução histórica completa |
| PP C05 | Convenção histórica comprovada; significado do C05 não resolvido |
| DATVEN 99991231 | Placeholder aparente; sem definição histórica comprovada |
| duplicidade K4 | fato RAW comprovado; causa não determinada |
| Tipo histórico | dimensão publicada separadamente de Prazo; legenda de 1986 não recuperada |

## 6. Regra de evidência

Não será feita nenhuma transformação de C05, VGO 2, Tipo ou DATVEN com base apenas em analogia moderna.

A colisão permanecerá preservada no RAW e será tratada como evento histórico observável até existir documentação primária suficiente.

## 7. Fases estatísticas e documentais já concluídas

### 7.1 FASE 08H — Recorrência multianual

Foram analisados 41 anos, de 1986 a 2026, totalizando 24.314.082 registros tipo 01.

Resultado:

- 24.314.081 grupos K4;
- 1 único grupo K4 duplicado;
- 2 linhas no grupo duplicado;
- 1 único grupo com estatísticas diferentes;
- somente 1986 apresentou colisão K4.

A colisão é, portanto, única no universo analisado, mas isso não determina sua causa histórica.

### 7.2 FASE 08K — Arqueologia do BDI/COTAHIST

A publicação contemporânea de 05/06/1986 preserva a estrutura pública:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

Ela registra Vigor PP C05.

Conclusão: Tipo e Prazo são dimensões distintas; C05 não deve ser convertido automaticamente em Tipo.

### 7.3 FASE 08L–08N — Dimensões históricas

As fases 08L, 08M e 08N confirmaram a existência documental de uma dimensão Tipo e de códigos históricos como PP-G/PB-G/PP-H em publicações posteriores, mas não localizaram legenda primária suficiente para atribuir esses códigos a comprador, vendedor, corretora, comitente ou taxa.

## 8. FASE 08O — Busca da legenda primária dos códigos de Tipo

A FASE 08O foi executada em 25/09/2026 com busca dirigida a:

1. manuais/regulamentos Bovespa de 1985–1987;
2. tabelas de códigos;
3. especificações do Mercado a Termo;
4. circulares e documentação normativa;
5. BDI de 09/10, 10/10 e 13/10/1986;
6. ocorrências de Vigor nos pregões próximos.

### 8.1 Resultado

Não foi localizada uma legenda primária contemporânea suficiente para decodificar os códigos históricos de Tipo.

Também não foi localizada cópia pública verificável dos BDI de 09/10, 10/10 ou 13/10/1986.

A evidência contemporânea do Jornal do Brasil continua demonstrando a estrutura **Tipo × Prazo** e a ocorrência de **Vigor PP C05**, mas não fornece a legenda do Tipo nem do C05.

### 8.2 O que foi descartado

Não foi aceita como fato nenhuma das seguintes equivalências:

- Tipo = comprador;
- Tipo = vendedor;
- Tipo = corretora/participante;
- Tipo = comitente;
- Tipo = taxa;
- C05 = Tipo;
- Tipo = Prazo.

As quatro primeiras permanecem hipóteses documentais possíveis; as duas últimas equivalências não são sustentadas pela evidência localizada.

### 8.3 Impacto na colisão

A FASE 08O mantém aberta a possibilidade de uma dimensão operacional adicional não preservada na K4, mas não demonstra que a coluna Tipo seja essa dimensão nem que ela explique as linhas RAW 140808/140809.

A hipótese principal continua sendo:

**regra histórica de agregação/publicação ou dimensão operacional não representada na K4.**

O processamento como erro permanece não confirmado.

Documento detalhado:

`docs/ingestao/FASE08O_COTAHIST_1986_LEGENDA_PRIMARIA_TIPO_V1.0.md`

Commit: `c1e9b1c1ee7d2104e22765bb6c3ce7e1b72ca224`.

## 9. Governança

- RAW permanece intocado.
- Linhas 140808 e 140809 permanecem preservadas.
- C05 permanece literal.
- VGO 2 permanece literal.
- DIMES 104 permanece literal.
- DATVEN 99991231 permanece literal.
- Nenhuma consolidação estatística é realizada.
- Nenhuma identidade econômica é inferida.
- Nenhuma causalidade é atribuída à coluna Tipo.

## 10. Próxima frente controlada

A investigação deve avançar em duas linhas:

### A — Arquivos institucionais

Buscar acervos físicos/digitalizados de Bovespa/B3, CVM, Biblioteca Nacional, Senado/Diário Oficial, FGV, universidades e jornais que reproduzam o BDI integral.

### B — Reconstrução interna no COTAHIST

Testar, com dados já preservados:

1. Vigor em 09/10, 10/10 e 13/10/1986;
2. múltiplas linhas do mesmo título com diferentes classes publicadas;
3. relação PRAZOT × ESPECI × DIMES × estatísticas;
4. padrões que permitam falsificar a hipótese de agregação.

## 11. Estado

**IMPLEMENTADO:** FASE 08O executada e documentada.

**EXECUTADO:** busca dirigida por legenda primária e BDI próximo ao evento.

**VALIDADO:** ausência de legenda primária suficiente nas fontes públicas recuperadas; existência histórica de Tipo separado de Prazo; existência de Vigor PP C05 antes de outubro de 1986.

**NÃO RESOLVIDO:** legenda dos códigos históricos e relação causal com a colisão K4.

**FASE 08:** ABERTA — investigação histórica continua.


## 21. FASE 08P — Transição Vigor 09/10 → 10/10 → 13/10/1986

**Documento:** `docs/ingestao/FASE08P_COTAHIST_1986_TRANSICAO_VIGOR_0910_1310_V1.0.md`

A FASE 08P reconstruiu diretamente no RAW preservado o comportamento de VGO 2 / VGORACPP em 09/10, 10/10 e 13/10/1986.

### Resultado validado

- RAW SHA-256: `350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`
- 7 registros relevantes na janela.
- 09/10: 1 linha a termo PRAZOT 060.
- 10/10: 2 linhas a termo PRAZOT 060.
- 13/10: 1 linha a termo PRAZOT 060.
- Em toda a janela: ESPECI `PP *C05` e DIMES `104`.
- A colisão continua restrita às linhas RAW 140808 e 140809 de 10/10/1986.
- A chave estrutural é idêntica nas duas linhas:
  `19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060`.
- Os agregados estatísticos são distintos:
  - linha 140808: TOTNEG 1, QUATOT 39.000.000, VOLTOT 74.100,00, preços 1,90;
  - linha 140809: TOTNEG 4, QUATOT 190.000.000, VOLTOT 356.460,00, PREAB 1,65, PREMED 1,87, PREMAX 1,91, PREULT 1,75.

### Interpretação

A sequência temporal observada é `1 linha → 2 linhas → 1 linha` para a mesma combinação estrutural VGO 2 / termo 060 / C05 / DIMES 104.

Isso **não identifica a causa**. Reforça, porém, que a duplicidade não decorre de uma mudança de PRAZOT, ESPECI ou DIMES dentro da janela.

A hipótese de trabalho permanece: **regra histórica de agregação/publicação ou dimensão operacional não representada na chave K4**.

Não foi demonstrado que a dimensão ausente seja Tipo, taxa, comitente, corretora, comprador/vendedor ou outra classificação.

### Governança

RAW preservado; nenhuma linha removida ou consolidada; C05 mantido literalmente; nenhum Tipo inferido; nenhuma identidade econômica ou causalidade inferida.

**Status:** IMPLEMENTADO / EXECUTADO / VALIDADO quanto à reconstrução da janela; **NÃO RESOLVIDO** quanto à causa histórica.

**Próxima frente:** recuperação documental primária do BDI de 10/10/1986 e da regra de publicação/agregação do Mercado a Termo.


## 22. FASE 08Q — Arqueologia primária do BDI e regra de agregação

A FASE 08Q executou busca documental dirigida ao BDI de 09/10, 10/10 e 13/10/1986 e à regra histórica de publicação/agregação do Mercado a Termo.

**Documento:** `docs/ingestao/FASE08Q_COTAHIST_1986_ARQUEOLOGIA_PRIMARIA_BDI_AGREGACAO_V1.0.md`

### Resultado

- Não foi localizada publicamente uma cópia verificável do BDI de 10/10/1986 capaz de explicar diretamente as duas linhas VGO 2.
- A ausência foi classificada como **EVIDÊNCIA AUSENTE**, não como inexistência.
- Evidência contemporânea de 1986 já recuperada confirma a separação entre Tipo e Prazo e registra Vigor PP C05.
- Fontes institucionais/normativas confirmam a existência do BDI e o contexto formal do Mercado a Termo, mas não decodificam C05 nem explicam a colisão.
- A FASE 08P continua demonstrando a sequência `1 linha → 2 linhas → 1 linha` em 09/10 → 10/10 → 13/10 para VGO 2 / termo 060 / C05 / DIMES 104.

### Estado das hipóteses

A hipótese principal permanece **regra histórica de agregação/publicação ou dimensão operacional não preservada na chave K4**.

Não foi demonstrado que a dimensão oculta seja Tipo, taxa, comprador/vendedor, corretora ou comitente.

### Governança

RAW preservado; C05 mantido literalmente; nenhuma consolidação das linhas 140808/140809; nenhuma causa econômica inferida.

**Status:** IMPLEMENTADO / EXECUTADO / VALIDADO quanto à busca e classificação documental; **CAUSA NÃO RESOLVIDA**.

**Próxima frente:** arqueologia institucional dirigida — acervos Bovespa/B3, CVM, Hemeroteca Digital, bibliotecas universitárias e exemplares físicos/digitalizados do BDI de outubro de 1986.


## 23. FASE 08R — Arqueologia institucional dirigida

Documento: docs/ingestao/FASE08R_COTAHIST_1986_ARQUEOLOGIA_INSTITUCIONAL_BDI_V1.0.md

A FASE 08R deslocou a investigação da busca web genérica para acervos institucionais. Foi localizada página oficial da B3 sobre o Centro de Memória, que informa guarda e preservação de documentos e objetos da história do mercado de capitais brasileiro e da B3, com acervo superior a 100.000 itens e possibilidade de pesquisa digital ou presencial mediante agendamento.

Essa descoberta estabelece um caminho institucional concreto para tentar recuperar o BDI de outubro de 1986 e documentação Bovespa da época.

A CVM também mantém estrutura institucional de arquivos e Serviço de Informação ao Cidadão. A busca pública desta fase não localizou diretamente o BDI de 10/10/1986 nem legenda histórica de Tipo/C05.

A imprensa digitalizada continua útil como fonte de reconstrução, mas não foi recuperada reprodução verificável do BDI de 09/10, 10/10 ou 13/10/1986.

### Estado

**VALIDADO:** existência de acervo institucional B3 diretamente pertinente e natureza institucional do BDI.

**EVIDÊNCIA AUSENTE:** exemplar primário verificável do BDI de 10/10/1986.

**NÃO RESOLVIDO:** causa da colisão K4, legenda de C05/Tipo e regra exata de agregação/publicação.

### Próxima ação de maior valor probatório

Prioridade máxima: recuperação institucional do BDI de 10/10/1986. Em seguida, BDI de 09/10 e 13/10, BDI de pregões próximos contendo Vigor PP C05, manuais Bovespa de Mercado a Termo de 1985–1987, tabela/legenda de Tipo e circulares/normas contemporâneas.

A FASE 08R permanece aberta até existir cadeia documental rastreável: fonte primária → regra histórica → dimensão publicada → relação com as duas linhas COTAHIST.


## 24. FASE 08S — Recuperação primária dirigida do BDI

Documento: docs/ingestao/FASE08S_COTAHIST_1986_RECUPERACAO_PRIMARIA_BDI_V1.0.md

A FASE 08S concentrou a investigação no acervo institucional identificado na 08R. A página oficial do Centro de Memória B3 confirma acervo histórico superior a 100.000 itens e pesquisa digital ou presencial. O link institucional conduz ao acervo digital do Museu B3, mas sua interface não permitiu, nesta execução, extrair registro catalográfico específico do BDI de 10/10/1986.

A Hemeroteca Digital da Biblioteca Nacional confirma cobertura de periódicos de 1986, porém não foi recuperada nesta execução uma reprodução verificável do BDI de 10/10/1986 nem das duas linhas Vigor.

**VALIDADO:** existência do acervo institucional B3/Museu B3 e cobertura de periódicos de 1986 na Hemeroteca.  
**NÃO RESOLVIDO:** exemplar primário do BDI de 10/10/1986, legenda de C05/Tipo e causa da colisão.  
**EVIDÊNCIA AUSENTE:** BDI primário/reprodução verificável do pregão de 10/10/1986.

A próxima frente é a **FASE 08T — pesquisa de catálogo/identificador e solicitação institucional**, buscando identificadores do acervo, número de página/seção do BDI, catálogos bibliográficos e documentação Bovespa de 1985–1987.


## 25. FASE 08T — Pesquisa de catálogo e identificador do BDI

Documento: docs/ingestao/FASE08T_COTAHIST_1986_CATALOGO_IDENTIFICADOR_BDI_V1.0.md

A FASE 08T transformou a busca institucional em investigação catalográfica. O acervo oficial do MUB3 permite pesquisa por termos, tipo de registro e intervalo de datas; o Centro de Referência informa mais de 100 mil itens e representa historicamente a Bovespa. Nesta execução, porém, não foi identificado um registro catalográfico específico do BDI de 10/10/1986.

A Hemeroteca Digital da Biblioteca Nacional confirma estrutura de acervo por publicação, ano e página/edição e cobertura de 1986, mas também não forneceu nesta execução o exemplar ou reprodução verificável do BDI-alvo.

A estratégia passa a ser identificar o **objeto documental**, e não apenas buscar o texto da data: título/série, órgão produtor, data, edição, página, ID do acervo, suporte, coleção e restrições de acesso.

**IMPLEMENTADO:** estratégia catalográfica e solicitação institucional preparadas.  
**EXECUTADO:** pesquisa MUB3 e Hemeroteca Digital.  
**VALIDADO:** existência dos acervos e de mecanismos de consulta.  
**NÃO RESOLVIDO:** identificador específico e exemplar primário do BDI de 10/10/1986.

**Próxima frente:** FASE 08U — solicitação institucional formal e busca bibliográfica cruzada.


## 26. FASE 08U — Solicitação institucional e busca bibliográfica cruzada

Documento: docs/ingestao/FASE08U_COTAHIST_1986_SOLICITACAO_INSTITUCIONAL_BDI_V1.0.md

A FASE 08U confirmou os canais institucionais para prosseguir com a recuperação documental. O MUB3/Centro de Referência mantém base pública de acervo histórico; a pesquisa desta fase não identificou o item BDI de 10/10/1986. A CVM disponibiliza o SIC integrado ao Fala.BR para pedidos de acesso à informação; o portal público também não apresentou diretamente o BDI-alvo. citeturn0search6turn0search0

A busca bibliográfica cruzada confirmou a existência de documentação posterior que identifica o BDI como veículo de divulgação de informações da Bovespa, mas não recuperou identificador ou exemplar primário verificável de 10/10/1986. 

**IMPLEMENTADO:** protocolo de solicitação institucional e critérios de validação documental.  
**EXECUTADO:** pesquisa MUB3/CVM e busca bibliográfica cruzada.  
**VALIDADO:** canais formais de consulta/solicitação.  
**NÃO RESOLVIDO:** exemplar primário e identificador catalográfico do BDI de 10/10/1986.

**Próxima frente:** FASE 08V — arqueologia de imprensa de 09–14/10/1986 para procurar reproduções parciais da seção Mercado a Termo e eventual dupla ocorrência de Vigor.
