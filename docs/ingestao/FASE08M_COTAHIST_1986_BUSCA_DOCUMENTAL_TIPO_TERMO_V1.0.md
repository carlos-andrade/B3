# FASE 08M — Busca Documental Dirigida pela Coluna Tipo — Mercado a Termo 1986–1989

**Arquivo:** FASE08M_COTAHIST_1986_BUSCA_DOCUMENTAL_TIPO_TERMO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Investigação da dimensão histórica `Tipo` e sua possível relação com a colisão K4 de 10/10/1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Investigar se a coluna histórica **Tipo** do Mercado a Termo representava uma dimensão operacional independente de:

- título;
- prazo;
- código Cxx;
- preço;
- quantidade;
- número de negócios;

e verificar se essa dimensão poderia explicar, de forma documentada, a existência de duas linhas com a mesma K4 no COTAHIST de 10/10/1986.

A pesquisa também procura evidência de associação do Tipo com:

- comprador/vendedor;
- corretora;
- comitente;
- taxa;
- modalidade contratual;
- outra classificação operacional.

## 2. Registro-alvo

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW: **140808** e **140809**.

A investigação mantém as duas linhas intactas.

## 3. Evidência contemporânea de 1986

O Jornal do Brasil de 05/06/1986 reproduz uma tabela do Mercado a Termo da Bolsa de Valores de São Paulo com a estrutura:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

A mesma publicação registra **Vigor PP C05**, além de outras combinações Cxx. citeturn0search0turn1search0

### Resultado

Fica confirmado que **Tipo** era uma coluna publicada separadamente de **Prazo** na tabela histórica observada.

Também fica confirmado que **C05** aparecia associado ao título Vigor.

**Não fica demonstrado** que o valor C05 fosse o conteúdo da coluna Tipo. A evidência publicada apresenta C05 integrado à identificação do papel, enquanto Tipo aparece como dimensão própria da tabela.

## 4. Evidência de 1987

Publicações históricas de 1987 mostram múltiplos formatos de identificação, incluindo:

- Vigor PP-G;
- Votec PP-G;
- Vale Rio Doce PP-G;
- Cibran PP-G;
- Unipar PB-G;
- Varig PP-H;
- Cruzeiro Sul PP-H.

Esses registros demonstram que combinações como **PP-G**, **PB-G** e **PP-H** eram utilizadas na publicação de mercado naquele período. citeturn2search0turn2search4

Também foram localizados exemplos de **Vigor PP-G**, o que é importante porque demonstra uma notação posterior diferente de **Vigor PP C05**.

### Limitação

A documentação pública localizada não fornece uma legenda contemporânea suficientemente explícita para transformar automaticamente:

- G;
- H;
- Q;
- D;
- C05;

em categorias econômicas específicas.

Portanto, essas letras/códigos são preservados como **notação histórica observada**, não como semântica inferida.

## 5. Evidência de 1988

Publicação histórica de 1988 encontrada na pesquisa anterior apresenta explicitamente a tabela:

**Títulos | Tipo | Prazo | Quant. | Fech. | Máx. | Min. | Méd. | Volume | Nº neg.**

E mostra exemplos de códigos como:

- PP-Q;
- PB-Q;
- PP-G;
- outros formatos.

Essa evidência é importante porque confirma estruturalmente que **Tipo** e **Prazo** eram dimensões distintas na publicação histórica posterior.

Ela não prova que a codificação de 1988 fosse idêntica à de 1986.

## 6. Teste da hipótese “C05 = Tipo”

### Resultado

**REFUTADO COMO INFERÊNCIA OPERACIONAL.**

A evidência de 1986 apresenta simultaneamente:

- uma coluna **Tipo**;
- um campo de identificação do título contendo **C05**.

Portanto, não há base documental para tratar C05 como sinônimo da coluna Tipo.

Governança:

- `ESPECI = PP *C05` deve continuar sendo preservado literalmente;
- C05 não será convertido em Tipo;
- nenhuma classificação econômica será criada a partir de C05 sem fonte primária.

## 7. Teste da hipótese “Tipo = Prazo”

### Resultado

**REFUTADO.**

A tabela histórica de 1986 apresenta **Tipo** e **Prazo** como colunas separadas.

Logo:

`Tipo != Prazo`

como dimensão documental.

No COTAHIST, `PRAZOT = 060` continua sendo interpretado somente como campo de prazo do registro, conforme o layout B3, sem atribuição automática de semântica ao Tipo histórico.

## 8. Teste da hipótese “Tipo explica a colisão K4”

### Evidência disponível

A K4 atualmente utilizada contém:

- data;
- CODBDI;
- CODNEG;
- TPMERC;
- CODISI;
- DIMES;
- ESPECI;
- PRAZOT;
- DATVEN;
- PREEXE;
- INDOPC;
- PTOEXE.

A coluna histórica **Tipo** não aparece como componente explícito dessa K4.

### Resultado

**HIPÓTESE POSSÍVEL, MAS NÃO CONFIRMADA.**

A pesquisa demonstra que existia uma dimensão denominada Tipo na publicação histórica do Mercado a Termo. Porém, não foi localizada documentação primária de 1986 mostrando:

1. os códigos de Tipo usados em 10/10/1986;
2. se Tipo era persistido no COTAHIST;
3. se Tipo participava da regra de agregação;
4. se duas linhas com o mesmo conjunto de campos da K4 poderiam ter Tipos distintos;
5. se Tipo estava associado a corretora, comitente, comprador, vendedor, taxa ou modalidade.

## 9. Teste de comprador/vendedor

Foram encontradas fontes normativas e materiais históricos que tratam comprador e vendedor como papéis distintos em operações a termo. A documentação regulatória de mercado a termo, entretanto, não foi localizada com uma legenda que conecte diretamente essa distinção aos códigos históricos **PP-G, PB-G, PP-Q, PB-Q** ou ao **C05** de 1986.

### Resultado

**NÃO CONFIRMADO.**

Não é permitido converter:

- PP → comprador;
- PB → vendedor;

ou qualquer outra equivalência semelhante.

Essa hipótese permanece aberta apenas como possibilidade documental a ser investigada em fonte primária.

## 10. Teste de corretora/comitente

A pesquisa encontrou documentação contemporânea da CVM que trata explicitamente de posições de comitentes no mercado a termo e de responsabilidades de participantes, além de fontes posteriores que descrevem corretoras atuando por conta própria ou de comitentes.

Entretanto, nenhuma fonte localizada demonstra que a coluna histórica **Tipo** fosse uma codificação de:

- corretora;
- comitente;
- conta;
- grupo de clientes;
- contraparte.

### Resultado

**NÃO CONFIRMADO.**

Não será introduzida nenhuma dimensão de corretora/comitente na normalização do COTAHIST 1986 sem evidência direta.

## 11. Teste de taxa

A pesquisa confirma, em documentação de mercado a termo, que taxa pode fazer parte das condições de uma operação. Porém, não foi encontrada evidência contemporânea de 1986 que demonstre que a coluna **Tipo** fosse uma codificação da taxa ou que a taxa fosse usada para separar linhas estatísticas no COTAHIST.

### Resultado

**NÃO CONFIRMADO.**

A hipótese de agregação por taxa permanece aberta, mas sem evidência suficiente para ser incorporada ao modelo.

## 12. O que a FASE 08M conseguiu estabelecer

### FATOS

1. Em 1986, a publicação histórica do Mercado a Termo possuía uma dimensão explícita denominada **Tipo**.
2. Em 1986, **Tipo** aparecia separado de **Prazo**.
3. Vigor era publicado como **Vigor PP C05**.
4. Em 1987, aparecem formatos como **PP-G**, **PB-G** e **PP-H**.
5. Em publicação posterior, a estrutura continua separando **Tipo** de **Prazo**.
6. Não foi encontrada legenda primária que permita decodificar com segurança os códigos históricos.
7. Não foi encontrada evidência que conecte diretamente Tipo à colisão K4 de 10/10/1986.

### HIPÓTESES QUE PERMANECEM ABERTAS

- Tipo como dimensão operacional adicional;
- Tipo associado a modalidade/classificação de negociação;
- agregação histórica por uma dimensão não preservada na K4;
- regra específica de publicação do BDI;
- outra regra operacional de registro.

### HIPÓTESES NÃO COMPROVADAS

- Tipo = C05;
- Tipo = Prazo;
- Tipo = comprador;
- Tipo = vendedor;
- Tipo = corretora;
- Tipo = comitente;
- Tipo = taxa.

## 13. Impacto na interpretação da colisão

A FASE 08M **não resolve a causa** da colisão K4.

Ela, porém, altera o grau de confiança da hipótese de “dimensão oculta”:

**antes:** possibilidade abstrata;

**agora:** existe evidência documental de que o Mercado a Termo publicava uma dimensão chamada **Tipo**, independente de Prazo.

Isso torna tecnicamente justificável investigar se essa dimensão existia também no processo de geração do COTAHIST 1986.

Ainda não é permitido afirmar que ela explique as duas linhas 140808/140809.

## 14. Governança de dados

A FASE 08M determina:

- RAW permanece intocado;
- linhas 140808 e 140809 permanecem separadas;
- C05 permanece literal;
- PP-G/PB-G/PP-H permanecem como códigos históricos literais;
- nenhuma tradução econômica automática será adicionada ao pipeline;
- nenhuma linha será consolidada;
- nenhuma causa será atribuída à colisão sem evidência primária.

## 15. Próxima frente

A próxima investigação deve procurar especificamente:

1. boletins Bovespa de outubro de 1986 com a coluna Tipo legível;
2. legendas ou glossários de códigos Tipo;
3. manuais de pregão Bovespa de 1986–1987;
4. documentos de registro de operações a termo;
5. tabelas onde o **mesmo título e mesmo prazo** apareçam com **Tipos diferentes** no mesmo pregão;
6. evidência documental que relacione Tipo a comprador/vendedor, taxa, corretora, comitente ou modalidade.

A prioridade continua sendo encontrar uma fonte primária contemporânea.

## 16. Estado da FASE 08M

**IMPLEMENTADO:** pesquisa documental dirigida por Tipo executada.

**EXECUTADO:** fontes históricas de 1986–1989 e fontes regulatórias relacionadas ao mercado a termo foram pesquisadas.

**VALIDADO:**
- existência da coluna histórica Tipo;
- separação Tipo × Prazo;
- existência de Vigor PP C05;
- existência posterior de códigos como PP-G/PB-G/PP-H;
- impossibilidade de tratar C05 como Tipo.

**NÃO VALIDADO:**
- semântica econômica dos códigos Tipo;
- relação Tipo × comprador/vendedor;
- relação Tipo × corretora/comitente;
- relação Tipo × taxa;
- participação de Tipo na regra de agregação do COTAHIST;
- explicação da colisão K4 de 10/10/1986.

**FASE 08:** permanece aberta.

## 17. Fontes principais consultadas

- Jornal do Brasil, 05/06/1986 — tabela histórica do Mercado a Termo e ocorrência de Vigor PP C05. citeturn0search0turn1search0
- Jornal/Citação histórica de dezembro de 1987 — ocorrências de PP-G, PB-G, PP-H e Vigor PP-G. citeturn2search0
- Publicação histórica de 1987 — exemplos adicionais de codificação PP-G/PB-G/PP-H. citeturn2search4
- Documentação histórica/regulatória consultada nas fases anteriores sobre comprador, vendedor e mercado a termo.

