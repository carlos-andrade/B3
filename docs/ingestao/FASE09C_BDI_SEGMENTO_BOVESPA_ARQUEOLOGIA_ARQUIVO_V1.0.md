# FASE 09C — Arqueologia do arquivo BDI — Segmento BOVESPA

**Arquivo:** FASE09C_BDI_SEGMENTO_BOVESPA_ARQUEOLOGIA_ARQUIVO_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Identificação histórica do arquivo/canal do BDI Segmento BOVESPA  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Identificar, com evidência documental, a nomenclatura, o canal de distribuição e, se possível, o identificador ou padrão de arquivo do antigo **BDI — Segmento BOVESPA / Cotações do Histórico Regular**, para criar uma rota institucionalmente verificável até o pregão de 10/10/1986.

O objetivo desta nota é **localizar a fonte**, não inferir a causa da colisão K4.

## 2. Evidência institucional primária recuperada

Comunicado oficial BM&FBOVESPA nº 031/2016-DO informa que os arquivos então utilizados incluíam:

- **BD Pregão — Segmento BM&F**;
- **Cotações do Histórico Regular — BDI — Segmento BOVESPA**.

O mesmo comunicado registra que a publicação desses arquivos seria descontinuada após a implantação da segunda fase do Projeto de Integração da Pós-Negociação. Também informa que os novos arquivos seriam disponibilizados pela Pesquisa por Pregão, FTP e outros canais institucionais.

Fonte oficial: Comunicado BM&FBOVESPA nº 031/2016-DO. citeturn3search0

## 3. Resultado da arqueologia de nomenclatura

A expressão institucional mais precisa recuperada é:

**Cotações do Histórico Regular (BDI — Segmento BOVESPA)**

Isso é mais específico do que simplesmente “BDI” e deve ser usado como nomenclatura de pesquisa nas próximas buscas.

Até esta rodada, **não foi localizado** em fonte pública indexada:

- nome exato do arquivo histórico diário correspondente a 1986;
- catálogo público que associe um identificador persistente ao BDI de 10/10/1986;
- URL pública atual que permita abrir diretamente o exemplar de 10/10/1986;
- documentação pública que prove um padrão de filename aplicável a 1986.

## 4. Não confundir com os PDFs modernos bdi_00_YYYYMMDD

A pesquisa também recuperou PDFs modernos denominados, por exemplo, bdi_00_YYYYMMDD.pdf, publicados como **Boletim Diário de Informações — Segmento Bovespa**.

Esses arquivos modernos são evidência de uma série documental BDI, mas **não devem ser tratados como prova do filename ou formato do BDI de 1986**.

Portanto:

**bdi_00_YYYYMMDD.pdf ≠ prova do arquivo Cotações do Histórico Regular de 1986.**

A nomenclatura moderna será mantida apenas como pista arquivística, sem retroprojeção.

## 5. Canal institucional atual

A B3 mantém a Pesquisa por Pregão como canal para consulta de boletins e arquivos, inclusive retroativos. A existência desse canal não demonstra, por si só, que o exemplar de 10/10/1986 permaneça publicamente acessível pela interface atual.

A ausência do arquivo na indexação/interface consultada deve ser registrada como **não recuperação**, não como inexistência.

## 6. Hipótese operacional de recuperação

A busca é executada em quatro camadas:

1. **Nomenclatura:** “Cotações do Histórico Regular”;
2. **Identidade institucional:** “BDI — Segmento BOVESPA”;
3. **Canal:** Pesquisa por Pregão / arquivos históricos / legado;
4. **Documento-alvo:** pregão de 10/10/1986, Mercado a Termo, Vigor/VGO2, PP C05, prazo 060.

## 7. Critério de evidência

Uma rota será considerada **RECUPERADA** somente se houver pelo menos um dos seguintes:

- arquivo primário;
- PDF/imagem primária;
- catálogo institucional com identificador inequívoco;
- documentação oficial que forneça filename/ID e permita apontar para o exemplar;
- solicitação/resposta institucional que identifique o item arquivado.

Resultados de busca, cópias de terceiros e documentos posteriores serão classificados como **PISTA**, não como fonte decisiva.

## 8. Relação com a colisão K4

A colisão permanece:

19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0

Linhas RAW:

- 140808
- 140809

Nenhuma semântica nova será atribuída às duas linhas até que a evidência histórica seja recuperada.

## 9. Estado

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM  
**BDI 10/10/1986 RECUPERADO:** NÃO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO

## 10. Próxima ação

Continuar a busca documental especificamente por:

- “Cotações do Histórico Regular”;
- “BDI Segmento BOVESPA”;
- documentação de migração da Pesquisa por Pregão;
- catálogos/índices de arquivos históricos;
- manuais de Market Data que descrevam o arquivo legado;
- referências a FTP/arquivo legado;
- acervo do Centro de Memória B3.

Não utilizar padrões de filename modernos como se fossem válidos para 1986 sem evidência.

## 11. Fonte principal desta nota

- BM&FBOVESPA, Comunicado nº 031/2016-DO — documento oficial que identifica expressamente “Cotações do Histórico Regular (BDI — Segmento BOVESPA)” e informa sua descontinuação no contexto da integração da pós-negociação. citeturn3search0

## 12. Rodada adicional — padrão moderno de distribuição

A pesquisa recuperou referências consistentes ao padrão posterior:

`/download/BOLETINSDIARIOS/bdi_00_YYYYMMDD.pdf`

Esse padrão é confirmado para períodos posteriores e permanece classificado como pista de continuidade documental, não como prova de aplicação em 1986.

O teste hipotético de `bdi_00_19861010.pdf` não produziu recuperação verificável. Isso não demonstra inexistência.

## 13. Rodada 25/09/2026 — fechamento parcial da arqueologia pública

A busca por “Cotações do Histórico Regular” + FTP, BDI — Segmento BOVESPA + FTP, DIN/MTA, Market Data, Pesquisa por Pregão, nome de arquivo, diretório e documentação de migração confirmou a série e o canal, mas não o identificador de 1986. citeturn3search0

Foi criado:

`docs/ingestao/SOLICITACAO_INSTITUCIONAL_BDI_BOVESPA_19861010_V1.0.md`

## 14. Rodada 25/09/2026 — rastreamento do endereço FTP legado

O Comunicado nº 031/2016-DO informa que os arquivos seriam disponibilizados por **FTP, “no endereço indicado anteriormente”**, além de Pesquisa por Pregão e DIN/MTA. O trecho recuperado não apresenta o endereço anterior. citeturn3search0

A busca pela frase literal “endereço indicado anteriormente”, combinada com BDI, FTP, Cotações do Histórico Regular, Segmento BOVESPA, IPN e DIN/MTA, não recuperou o documento anterior com o endereço de forma inequívoca.

Cadeia candidata:

**Comunicado 031/2016-DO → documento anterior citado → endereço FTP legado → documentação/catálogo BDI → exemplar 10/10/1986.**

## 15. Rodada 25/09/2026 — identificação de um servidor FTP institucional posterior

### 15.1 Nova evidência oficial

Foi recuperado o **Comunicado Externo B3 nº 011/2018-VPC**, de 29/06/2018, sobre a desativação dos portais e do servidor FTP e a descontinuidade do BD/BDI em PDF.

O documento identifica nominalmente o servidor:

**ftp.bmf.com.br**

e informa que, em 30/11/2018, esse servidor FTP seria desativado, juntamente com a publicação do Boletim Diário (BD) e do Boletim Diário de Informações (BDI) em formato PDF. A partir de 01/12/2018, os dados passariam ao UP2DATA. citeturn1search40

### 15.2 Valor probatório

Esta é uma melhoria importante na identificação do **canal FTP institucional**, porque agora temos um hostname explicitamente documentado pela própria B3:

**FTP institucional documentado em 2018 = ftp.bmf.com.br**

Entretanto, o documento é de **2018**, enquanto a referência do Comunicado 031/2016-DO ao “endereço indicado anteriormente” é de 2016.

Portanto, não é permitido afirmar ainda que:

**ftp.bmf.com.br = endereço citado em 2016**

sem recuperar um documento que faça essa ligação.

Também não é permitido retroprojetar esse hostname para 1986.

### 15.3 Relação com o BDI

O Comunicado 011/2018-VPC associa explicitamente o servidor FTP à infraestrutura que seria desativada e menciona a descontinuidade do **BD/BDI em formato PDF**. Isso reforça que o FTP fazia parte da cadeia real de distribuição do BDI em período posterior. citeturn1search40

A cadeia documental passa a ser:

**BDI Segmento BOVESPA CONFIRMADO → FTP CONFIRMADO → hostname ftp.bmf.com.br CONFIRMADO em 2018 → ligação específica com o endereço de 2016 NÃO PROVADA → ligação com 1986 NÃO PROVADA.**

## 16. Rodada 25/09/2026 — conteúdo normativo do BDI

Foi localizada documentação oficial BM&FBOVESPA sobre o **Boletim Diário de Informações (BDI)**.

O Regulamento de Operações do Segmento BOVESPA, revisão 03 de 16/12/2008, estabelece que a Bolsa editava diariamente o BDI, em papel e/ou forma eletrônica, destinado às Sociedades Corretoras e acessível a outros públicos. Também estabelece que o BDI publicava negociações e posições em aberto nos mercados de liquidação futura, além de opções exercidas. citeturn1search36turn1search37

O Manual de Procedimentos Operacionais, revisão 03 de 07/04/2010, repete que o BDI era editado diariamente e continha operações dos mercados administrados, incluindo negociações e posições em aberto nos mercados de liquidação futura. citeturn1search39

### 16.1 Valor probatório

Esses documentos **não resolvem a colisão Vigor de 1986**, porque são posteriores.

Mas estabelecem documentalmente uma propriedade importante do BDI:

**BDI = publicação institucional diária das operações/posições de mercados administrados, incluindo mercados de liquidação futura.**

Isso fortalece a necessidade de recuperar a publicação histórica do dia específico antes de interpretar por que duas linhas COTAHIST foram produzidas para o mesmo K4.

## 17. O que foi efetivamente aprendido nesta rodada

| Evidência | Período | Estado | O que prova |
|---|---:|---|---|
| Cotações do Histórico Regular (BDI — Segmento BOVESPA) | 2016 | CONFIRMADA | Identidade da série |
| FTP como canal | 2016 | CONFIRMADO | Existência do canal |
| `ftp.bmf.com.br` | 2018 | CONFIRMADO | Hostname FTP institucional posterior |
| BD/BDI PDF via infraestrutura FTP | 2018 | CONFIRMADO | Relação do FTP com BD/BDI posterior |
| BDI diário | 2008/2010 | CONFIRMADO | Natureza institucional diária do BDI |
| Filename `bdi_00_YYYYMMDD.pdf` | posterior | CONFIRMADO | Padrão posterior |
| Aplicação de `ftp.bmf.com.br` a 1986 | 1986 | NÃO PROVADA | Nenhuma |
| Filename de 1986 | 1986 | NÃO IDENTIFICADO | Nenhum |
| BDI de 10/10/1986 | 1986 | NÃO RECUPERADO | Nenhum |
| Regra causadora da colisão K4 | 1986 | NÃO RESOLVIDA | Nenhuma |

## 18. Estado atualizado

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM  
**SÉRIE BDI:** CONFIRMADA  
**FTP HISTÓRICO:** CONFIRMADO  
**HOSTNAME FTP POSTERIOR (2018):** `ftp.bmf.com.br` — CONFIRMADO  
**ENDEREÇO FTP ESPECÍFICO DE 2016:** NÃO IDENTIFICADO  
**CATÁLOGO/ID DE 1986:** NÃO IDENTIFICADO  
**BDI 10/10/1986:** NÃO RECUPERADO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO

## 19. Próxima frente técnica

A pesquisa agora deve tentar fechar especificamente o elo:

**ftp.bmf.com.br (2018) ↔ endereço FTP citado em 2016**

Prioridades:

1. documentos B3/BM&FBOVESPA de 2015–2017 que mencionem `ftp.bmf.com.br`;
2. manuais técnicos de distribuição de arquivos;
3. documentação de participantes/vendors sobre o FTP;
4. referências a diretórios BDI dentro do FTP;
5. documentos de migração do IPN;
6. somente depois, tentar reconstruir a possível cadeia histórica anterior.

Mesmo que esse elo seja fechado, **isso ainda não provará a existência do mesmo canal em 1986**. A resolução da causa K4 continuará condicionada à recuperação do BDI histórico ou de documentação primária/normativa contemporânea capaz de explicar a publicação.

**Regra mantida: RAW COTAHIST não será alterado.**


## 20. Rodada 25/09/2026 — fechamento do elo do hostname em 2016

Foi localizada uma evidência oficial adicional no próprio **Comunicado 031/2016-DO**: o documento informa que, durante os testes do novo BVBG.086/BVBG.087, o download dos arquivos poderia ser realizado por:

`ftp://ftp.bmf.com.br/IPN/TRS`

A referência é inequívoca quanto ao **hostname `ftp.bmf.com.br` já estar em uso institucional em 2016**. citeturn1search0

### 20.1 O que esta evidência resolve

A cadeia temporal agora fica mais precisa:

**2016:** `ftp.bmf.com.br` CONFIRMADO em documento oficial, com o caminho específico `/IPN/TRS` para os arquivos de teste BVBG.086/BVBG.087. citeturn1search0

**2018:** `ftp.bmf.com.br` CONFIRMADO novamente como servidor FTP institucional, cuja desativação foi anunciada juntamente com a descontinuidade do BD/BDI em PDF. citeturn1search1

Portanto, já não é correto registrar o hostname como apenas “posterior a 2016”. Ele está documentalmente comprovado em **2016 e 2018**.

### 20.2 Limitação importante

O caminho `/IPN/TRS` identificado em 2016 pertence aos arquivos de teste BVBG.086/BVBG.087 e **não foi demonstrado como diretório do BDI Segmento BOVESPA**.

Logo:

- **hostname FTP em 2016:** CONFIRMADO;
- **caminho `/IPN/TRS` em 2016:** CONFIRMADO para BVBG.086/BVBG.087;
- **BDI histórico dentro de `/IPN/TRS`:** NÃO PROVADO;
- **diretório específico do BDI em 2016:** NÃO IDENTIFICADO;
- **arquivo BDI de 10/10/1986:** NÃO RECUPERADO.

Essa distinção é necessária para evitar transformar uma evidência de infraestrutura em uma identificação indevida do arquivo histórico.

### 20.3 Novo estado da cadeia

A cadeia passa a ser:

**BDI Segmento BOVESPA CONFIRMADO → FTP institucional CONFIRMADO em 2016 → hostname `ftp.bmf.com.br` CONFIRMADO em 2016 → caminho `/IPN/TRS` CONFIRMADO para BVBG de teste → BDI dentro desse caminho NÃO PROVADO → BDI 10/10/1986 NÃO RECUPERADO.**

A evidência de 2018 permanece independente e confirma que o mesmo hostname estava associado à infraestrutura FTP desativada naquele período, juntamente com a descontinuidade do BD/BDI em PDF. citeturn1search1

## 21. Estado atualizado após a rodada

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM  
**HOSTNAME `ftp.bmf.com.br` EM 2016:** CONFIRMADO  
**CAMINHO `/IPN/TRS` EM 2016:** CONFIRMADO — BVBG.086/BVBG.087  
**DIRETÓRIO BDI 2016:** NÃO IDENTIFICADO  
**CATÁLOGO/ID DE 1986:** NÃO IDENTIFICADO  
**BDI 10/10/1986:** NÃO RECUPERADO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO

## 22. Próxima frente

A próxima busca deve abandonar a hipótese de que o caminho `/IPN/TRS` seja automaticamente o diretório do BDI e procurar, de forma específica:

1. documentos oficiais de 2015–2017 com `ftp.bmf.com.br` + **BDI**;
2. documentos que mencionem **BOLETINSDIARIOS**, **BDI**, **Cotações do Histórico Regular** e diretórios FTP;
3. catálogos técnicos de arquivos eletrônicos anteriores ao BVBG;
4. manuais de Market Data/BDI que indiquem diretórios ou nomes de arquivos;
5. documentação de migração que relacione os antigos arquivos eletrônicos BDI aos novos BVBG.

**Regra mantida:** nenhum filename moderno será retroprojetado para 1986 e o RAW COTAHIST permanecerá intocado.


## 23. Rodada 25/09/2026 — recuperação do ecossistema legado BDIN/BDPregao

Uma nova busca documental recuperou evidência técnica sobre os arquivos eletrônicos legados da BOVESPA/BM&FBovespa.

### 23.1 BDIN — evidência de layout oficial

Foi localizado o documento oficial **Layout do Arquivo de Cotações — BDIN**, datado de 21/03/2011. O documento informa que o BDIN:

- permitia acesso às informações relativas à negociação do dia;
- continha informações de índices e papéis negociados;
- era gerado diariamente após o encerramento do pregão;
- utilizava o nome lógico **BDIN_PUB**;
- possuía registros específicos de resumo diário por papel e por código de BDI.

Fonte: documento de layout hospedado no domínio histórico BVMF/BM&FBovespa. citeturn4search6

### 23.2 Evidência anterior sobre o BDIN

Também foi recuperada uma versão histórica do layout, atualizada em 07/04/1999, que identifica o arquivo como **BDIN_PUB**, com código de arquivo BDIN e origem BOVESPA. citeturn4search7

Isso demonstra que a família BDIN é anterior a 2011 e constitui uma camada eletrônica própria de cotações da BOVESPA.

### 23.3 Limitação para a colisão Vigor

Essa descoberta **não resolve a colisão K4**.

O layout BDIN recuperado descreve cotações/negociações de índices e papéis e não demonstra que o arquivo continha a tabela histórica específica do **Mercado a Termo** na qual aparecem as duas linhas Vigor de 10/10/1986.

Além disso, o comunicado oficial de 2016 distingue explicitamente:

- **BD Pregão — Segmento BM&F**;
- **Cotações do Histórico Regular — BDI — Segmento BOVESPA**.

O comunicado também informa que esses dois arquivos seriam descontinuados após a segunda fase do Projeto de Integração da Pós-Negociação. citeturn5search19

Portanto, **BDIN_PUB não deve ser substituído semanticamente por BDI Segmento BOVESPA**.

### 23.4 Nova pista documental de URL legada

Uma fonte técnica independente, publicada em 2011, registrou uma URL histórica para BDIN no formato:

`http://www.bmfbovespa.com.br/fechamento-pregao/bdi/bdi@MM@@DD@@YY@`

A mesma fonte descreve BDIN como arquivo geral de preços de ações negociadas e separa esse arquivo do **BDPregao**, destinado a futuros/opções/derivativos. citeturn2search0

Essa referência é classificada como **PISTA SECUNDÁRIA**, não como fonte primária.

O valor dessa pista é arqueológico: ela mostra que a distribuição eletrônica utilizava uma família de arquivos BDI/BDIN e que havia uma rota HTTP histórica distinta das rotas FTP de outros arquivos.

### 23.5 Nova pista sobre o FTP e o ecossistema de arquivos

A mesma fonte técnica registra que o servidor `ftp.bmf.com.br` era navegável e que arquivos disponibilizados no FTP possuíam estruturas de diretórios correspondentes por HTTP. citeturn2search0

Isso é consistente com a evidência oficial já recuperada para 2016 e 2018, mas continua sendo evidência secundária para os nomes específicos de diretórios.

### 23.6 Conclusão desta rodada

Foi possível separar melhor três camadas que não devem ser confundidas:

1. **BDIN / BDIN_PUB** — arquivo eletrônico de cotações/negociações da BOVESPA, com layout documentado;
2. **BD Pregão — Segmento BM&F** — arquivo histórico distinto;
3. **Cotações do Histórico Regular — BDI — Segmento BOVESPA** — série explicitamente identificada pela BM&FBOVESPA em 2016 e ainda não recuperada para 10/10/1986.

Essa distinção é relevante porque a evidência necessária para explicar a colisão Vigor continua sendo a camada histórica correspondente ao **BDI Segmento BOVESPA / Mercado a Termo**, e não simplesmente qualquer arquivo chamado BDI/BDIN.

## 24. Estado após a rodada

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM  
**BDIN/BDIN_PUB DOCUMENTADO:** SIM  
**BDIN IDENTIFICADO COMO CAMADA ELETRÔNICA DE COTAÇÕES:** SIM  
**BDI — COTAÇÕES DO HISTÓRICO REGULAR — IDENTIFICADO INSTITUCIONALMENTE:** SIM  
**ARQUIVO/ITEM BDI DE 10/10/1986:** NÃO RECUPERADO  
**DIRETÓRIO BDI HISTÓRICO:** NÃO IDENTIFICADO  
**CAUSA DA COLISÃO K4:** NÃO RESOLVIDA  
**RAW COTAHIST:** INALTERADO

## 25. Próxima busca de alta prioridade

A próxima frente deve procurar especificamente a relação entre:

**BDIN/BDI → Pesquisa por Pregão → Cotações do Histórico Regular → Mercado a Termo**

Prioridades:

1. layouts antigos que contenham explicitamente **termos/mercado a termo**;
2. manuais de arquivos BDI anteriores a 2016;
3. referências a **BDI** em documentação de sistemas legados;
4. caminhos HTTP/FTP contendo `bdi`, `BDIN`, `fechamento-pregao` ou `boletim`;
5. documentação que explique a diferença entre **BDIN** e **Cotações do Histórico Regular — BDI**;
6. somente após essa separação, testar rotas históricas para 10/10/1986.

**Regra mantida:** a URL secundária não será tratada como prova do arquivo de 1986; nenhum filename será retroprojetado e o RAW COTAHIST permanecerá intocado.


## 26. Rodada 25/09/2026 — BDIN oficial comprova a presença de Mercado a Termo na camada eletrônica de cotações

Foi recuperado diretamente no domínio histórico da BM&FBovespa o **Layout do Arquivo de Cotações — BDIN**, de 21/03/2011.

O documento oficial define o arquivo como **BDIN_PUB**, gerado diariamente após o encerramento do pregão, e informa que o registro 02 é o **Resumo Diário de Negociações por Papel — Mercado**. citeturn1search0

Mais importante para a FASE 09C, o registro 02 contém explicitamente:

- CODBDI — código BDI;
- ESPECI — especificação do papel;
- CODNEG — código de negociação;
- TPMERC — tipo de mercado;
- PRAZOT — prazo em dias do mercado a termo;
- PREABE, PREMAX, PREMIN, PREMED, PREULT;
- TOTNEG, QUATOT, VOLTOT;
- PREEXE;
- DATVEN;
- INDOPC;
- FATCOT;
- PTOEXE;
- CODISI;
- DISMES. citeturn2view0

### 26.1 Consequência para a reconstrução

Existe, portanto, uma evidência oficial de que a camada eletrônica de cotações BOVESPA possuía estrutura capaz de representar **Mercado a Termo** e vários dos mesmos campos estruturais presentes no COTAHIST.

Isso aproxima a arquitetura documental do problema Vigor, mas **não resolve a colisão**. O layout BDIN de 2011 não contém, no registro 02 recuperado, um campo explicitamente denominado **Tipo** que corresponda à coluna Tipo observada no Jornal do Brasil de 05/06/1986.

Também não foi localizada, nesta rodada, uma tabela que demonstre que ESPECI, INDCAR, CODBDI, DISMES ou outro campo do BDIN seja semanticamente equivalente à coluna histórica Tipo do jornal.

### 26.2 Relação com os campos do COTAHIST

| BDIN | COTAHIST | Situação |
|---|---|---|
| CODBDI | CODBDI | correspondência direta |
| CODNEG | CODNEG | correspondência direta |
| TPMERC | TPMERC | correspondência direta |
| ESPECI | ESPECI | correspondência direta |
| PRAZOT | PRAZOT | correspondência direta |
| PREABE/PREMAX/PREMIN/PREMED/PREULT | PREAB/PREMAX/PREMIN/PREMED/PREULT | correspondência funcional |
| TOTNEG | TOTNEG | correspondência direta |
| QUATOT | QUATOT | correspondência direta |
| VOLTOT | VOLTOT | correspondência direta |
| PREEXE | PREEXE | correspondência direta |
| DATVEN | DATVEN | correspondência direta |
| INDOPC | INDOPC | correspondência direta |
| FATCOT | FATCOT | correspondência direta |
| PTOEXE | PTOEXE | correspondência direta |
| CODISI | CODISI | correspondência direta |
| DISMES | DIMES | correspondência funcional/nominal a confirmar |

A última linha permanece marcada como **a confirmar**: o BDIN usa DISMES e o COTAHIST usa DIMES; a semelhança nominal não basta para afirmar identidade histórica sem documentação de mapeamento.

### 26.3 Evidência histórica anterior a 2011

Foi localizada também uma cópia pública de um layout BDIN atualizado em **07/04/1999**, que mantém o nome **BDIN_PUB** e a estrutura de arquivo de cotações da BOVESPA. Essa cópia não é tratada como fonte primária, mas demonstra a existência da família BDIN em 1999. citeturn3search2

Isso reforça a continuidade documental da família BDIN antes de 2011, sem retroprojetá-la para 1986.

### 26.4 Limite probatório

A nova evidência permite afirmar:

**BDIN oficial → cotações BOVESPA → mercado a termo representado → estrutura parcialmente coincidente com COTAHIST.**

Ainda não permite afirmar:

**BDIN 1999/2011 = BDI Segmento BOVESPA de 1986**, nem que o BDIN explique a existência de duas linhas Vigor no COTAHIST.

A fonte decisiva continua sendo o documento contemporâneo a 1986 ou o exemplar BDI de 10/10/1986.

## 27. Estado atualizado

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM  
**BDIN OFICIAL COM MERCADO A TERMO:** CONFIRMADO  
**CORRESPONDÊNCIA BDIN↔COTAHIST:** PARCIALMENTE CONFIRMADA  
**CAMPO HISTÓRICO TIPO:** IDENTIDADE NÃO PROVADA  
**BDI 10/10/1986:** NÃO RECUPERADO  
**CAUSA DA COLISÃO K4:** NÃO RESOLVIDA  
**RAW COTAHIST:** INALTERADO

## 28. Próxima frente

A pesquisa deve agora procurar documentação de **BDIN/BDI anterior a 1999** e, sobretudo, qualquer tabela de códigos que relacione:

**Tipo → ESPECI / INDCAR / CODBDI / DIMES-DISMES / Cxx**

Sem essa tabela, nenhuma dessas colunas será reinterpretada como o Tipo publicado em 1986.

## 29. Rodada 25/09/2026 — semântica oficial de CODBDI, INDCAR e TPMERC

A busca por tabelas associadas ao layout BDIN produziu uma evidência útil para separar três dimensões que poderiam ser confundidas com o Tipo observado na publicação de 1986.

O layout oficial do BDIN identifica:

- CODBDI: código utilizado para classificar os papéis na emissão do Boletim Diário de Informações, com referência à tabela associada NE001;
- INDCAR: indicador de característica do papel, com referência à tabela PA020;
- TPMERC: tipo de mercado, com referência à tabela PA003;
- PRAZOT: prazo em dias do Mercado a Termo. citeturn1search12turn2search0

A documentação secundária que reproduz o mesmo layout explicita exemplos de INDCAR, como participação no cálculo do índice Bovespa, mercado META, opção em dólar e SWOPTION. citeturn1search13

### 29.1 Consequência metodológica

Essa separação é importante:

CODBDI ≠ INDCAR ≠ TPMERC ≠ PRAZOT

No layout posterior, são campos independentes, com funções diferentes.

Portanto, a coluna histórica Tipo do Jornal do Brasil de 05/06/1986 não pode ser atribuída automaticamente a nenhum desses campos.

### 29.2 Nova matriz de hipóteses

| Dimensão candidata | Evidência posterior | Pode ser identificada como Tipo de 1986? |
|---|---|---|
| CODBDI | classificação BDI | NÃO |
| INDCAR | característica do papel | NÃO |
| TPMERC | tipo de mercado | NÃO |
| PRAZOT | prazo do termo | NÃO |
| ESPECI | especificação do papel | NÃO |
| Cxx dentro de ESPECI | nomenclatura observada historicamente | NÃO |
| Tipo do jornal | coluna documental separada | AINDA NÃO MAPEADO |

A conclusão é deliberadamente conservadora: a documentação posterior ajuda a excluir equivalências simplistas, mas não fornece o mapeamento histórico de 1986.

### 29.3 Novo teste documental prioritário

O próximo alvo deve ser a recuperação da tabela NE001, PA020 e PA003 ou versões anteriores dessas tabelas, procurando:

1. nomenclaturas antigas;
2. mudanças de código;
3. eventual campo que tenha sido incorporado/removido;
4. referências explícitas a Tipo;
5. códigos associados a Cxx;
6. documentação específica de Mercado a Termo.

Até que uma dessas fontes estabeleça a relação histórica, Tipo continua sendo uma dimensão não observada pelo K4.

## 30. Estado atualizado

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM  
**CODBDI — CLASSIFICAÇÃO BDI:** CONFIRMADO  
**INDCAR — CARACTERÍSTICA DO PAPEL:** CONFIRMADO  
**TPMERC — TIPO DE MERCADO:** CONFIRMADO  
**PRAZOT — PRAZO DO TERMO:** CONFIRMADO  
**TIPO HISTÓRICO DE 1986 MAPEADO:** NÃO  
**BDI 10/10/1986:** NÃO RECUPERADO  
**CAUSA DA COLISÃO K4:** NÃO RESOLVIDA  
**RAW COTAHIST:** INALTERADO
