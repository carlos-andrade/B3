# FASE 09C — Reconstrução documental da regra de agregação/publicação do BDI — Vigor 10/10/1986

**Arquivo:** FASE09C_COTAHIST_1986_RECONSTRUCAO_REGRA_BDI_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reconstrução documental da origem de duas linhas estatísticas sob a mesma K4  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Ponto de partida

As FASES 08C, 08H e 09B convergem para uma única colisão K4 no COTAHIST 1986:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

As linhas RAW 140808 e 140809 possuem a mesma K4 e estatísticas diferentes.

FASE 09B demonstrou, no universo integral de 1986, que não existe uma população comparável de colisões. Portanto, a FASE 09C abandona a busca estatística genérica e passa a investigar a regra histórica de publicação/agregação do BDI.

## 2. Pergunta documental

Qual dimensão existente no processo de registro/publicação do Mercado a Termo da Bovespa em 10/10/1986 permitia que dois agregados estatísticos distintos fossem publicados para o mesmo ativo, prazo e demais campos hoje preservados na K4?

Dimensões a testar separadamente:

1. Tipo de operação a termo;
2. taxa/preço ou faixa de taxa;
3. comitente/participante/corretora;
4. posição de compra ou venda;
5. modalidade ou condição operacional;
6. regra de agregação do boletim;
7. correção/republicação/erro operacional;
8. qualquer outro campo existente no BDI e ausente no COTAHIST.

## 3. Evidência contemporânea já recuperada

O Jornal do Brasil de 05/06/1986 reproduz uma tabela do mercado a termo com as dimensões **Tipo** e **Prazo**, além de Quant, Fech, Máx, Mín, Méd e N°. A mesma publicação contém Vigor PP C05 e outros códigos Cxx. Isso demonstra que havia mais de uma dimensão de classificação/publicação além do prazo. citeturn0search0

A evidência, entretanto, não permite concluir que C05 seja o campo Tipo, nem que Tipo seja a dimensão que causou a colisão Vigor.

## 4. Evidência normativa e estrutural

O layout oficial do COTAHIST define DATA DO PREGÃO nas posições 03–10 e CODBDI como código utilizado para classificar os papéis na emissão do BDI. TPMERC identifica o mercado em que o papel está cadastrado. citeturn0search36

Regulamentação posterior da Bovespa documenta o BDI como boletim diário contendo operações dos mercados administrados pela Bolsa e informações dos mercados de liquidação futura. Essa fonte é posterior a 1986 e, portanto, serve como evidência de função institucional do BDI, não como prova direta da regra vigente em 1986. citeturn1search17

Manual posterior também registra que informações de taxas mínima, máxima e média das operações a termo para diferentes tipos de termo eram divulgadas no BDI. Novamente, a fonte é posterior e não deve ser retroprojetada automaticamente para 1986. citeturn0search37

## 5. Evidência institucional para recuperação primária

A B3 informa que o Centro de Memória preserva mais de 100.000 itens documentais e permite pesquisa no acervo digital ou presencial. A instituição disponibiliza atendimento a pesquisadores mediante agendamento. citeturn1search11

A página atual de pesquisa por pregão da B3 também informa que permite acesso a boletins diários e arquivos, inclusive retroativos, embora a interface atualmente disponível não tenha fornecido, nesta etapa, o BDI de 10/10/1986. citeturn1search1

## 6. Documento decisivo a recuperar

Prioridade máxima:

**Boletim Diário de Informações — Bovespa — pregão de 10/10/1986**, preferencialmente a seção **Mercado a Termo**, contendo Vigor / VGO 2 / PP C05 / prazo 060.

Prioridades secundárias:

- BDI de 09/10/1986;
- BDI de 13/10/1986;
- páginas imediatamente anteriores/posteriores da mesma série;
- legenda de Tipo/Cxx;
- manual/regulamento operacional vigente em 1986;
- tabela ou nota metodológica sobre agregação das operações a termo.

## 7. Campos que devem ser extraídos do BDI

Quando o exemplar for recuperado, registrar literalmente:

- título da publicação;
- data do pregão;
- número da edição, se existente;
- número da página;
- seção/capítulo;
- cabeçalho completo da tabela;
- título do ativo;
- Tipo;
- Prazo;
- Quant.;
- Fech.;
- Máx.;
- Mín.;
- Méd.;
- Volume, se presente;
- N° de negócios, se presente;
- código Cxx completo;
- qualquer coluna adicional;
- notas de rodapé;
- legenda da tabela;
- identificação/catalogação do acervo;
- URL, ID ou referência institucional do item;
- imagem/PDF, quando disponível.

## 8. Testes de decisão

### H1 — Tipo é a dimensão ausente

Somente será aceita se o BDI de 10/10/1986 demonstrar que as duas linhas Vigor possuem Tipos diferentes ou se documentação contemporânea estabelecer explicitamente que Tipo gera agregações separadas sob as demais condições do alvo.

### H2 — taxa/preço é a dimensão ausente

Somente será aceita se documentação contemporânea demonstrar agregação separada por taxa ou condição equivalente e os dois perfis do COTAHIST puderem ser reconciliados com essa regra.

### H3 — participante/comitente/posição é a dimensão ausente

Somente será aceita com documentação contemporânea que demonstre essa dimensão como chave de publicação/agregação.

### H4 — regra histórica de agregação/publicação do BDI

Será aceita se a documentação demonstrar que o BDI podia publicar mais de uma linha para o mesmo conjunto de campos hoje representado pela K4, por uma regra editorial/operacional de agregação.

### H5 — erro de processamento/publicação

Somente será aceita mediante evidência de correção, errata, inconsistência documental ou outra prova contemporânea.

## 9. O que NÃO será feito

- Não serão fundidas as linhas 140808 e 140809.
- Não será escolhido um dos dois registros como correto.
- Não será atribuído significado a C05 sem evidência.
- Não será retroprojetada uma regra moderna para 1986.
- Não será inferida identidade econômica apenas porque a K4 coincide.
- Não será alterado o RAW.

## 10. Estado

**IMPLEMENTADO:** protocolo documental definido.  
**EXECUTADO:** pesquisa pública inicial executada.  
**VALIDADO:** evidência estrutural/normativa disponível e limitações registradas.  
**CAUSA HISTÓRICA:** NÃO RESOLVIDA.  
**EVIDÊNCIA DECISIVA:** BDI de 10/10/1986 ainda não recuperado.

## 11. Próxima ação

Prosseguir exclusivamente na recuperação do exemplar primário do BDI de 10/10/1986 e, em paralelo, procurar o regulamento/manual Bovespa efetivamente vigente em 1986. A investigação será encerrada somente quando a regra puder ser demonstrada documentalmente ou quando a ausência do documento for formalmente registrada como limite da reconstrução.

## 12. Fontes externas consultadas

- Jornal do Brasil, 05/06/1986 — evidência contemporânea de tabela do mercado a termo e nomenclatura Cxx. citeturn0search0
- B3 — Layout oficial do COTAHIST. citeturn0search36
- B3 — Regulamento posterior sobre BDI. citeturn1search17
- B3 — Manual posterior de procedimentos do mercado a termo. citeturn0search37
- B3 — Centro de Memória. citeturn1search11
- B3 — Pesquisa por pregão/boletins retroativos. citeturn1search1
- Decreto-Lei nº 2.286/1986 — contexto normativo do mercado a termo. citeturn0search2

## 13. Pesquisa documental adicional — 25/09/2026

### 13.1 Busca do BDI primário

Foi realizada nova rodada de pesquisa pública direcionada especificamente a:

- BDI / Boletim Diário de Informações Bovespa;
- pregão de 10/10/1986;
- pregões adjacentes de 09/10/1986 e 13/10/1986;
- Mercado a Termo;
- Vigor / VGO2;
- PP C05;
- prazo 060;
- cópias PDF e referências documentais da Bolsa de Valores de São Paulo.

**Resultado:** o exemplar primário do BDI de 10/10/1986 não foi localizado nas fontes públicas indexadas consultadas nesta etapa.

Isso é um **resultado de busca**, não uma prova de inexistência do documento.

### 13.2 Nova evidência secundária contemporânea

A pesquisa recuperou novamente a edição do Jornal do Brasil de 05/06/1986. O conteúdo mostra, no mercado a termo, a coexistência de campos de **Tipo** e **Prazo**, além de Quant., Fech., Máx., Mín., Méd. e N°. Também aparecem códigos Cxx, inclusive Vigor PP C05. 

Essa fonte reforça a existência histórica de dimensões de publicação que não aparecem explicitamente na K4 do COTAHIST, mas continua sem demonstrar qual delas gerou a duplicidade específica de Vigor em 10/10/1986.

### 13.3 Evidência posterior não retroprojetada

Foram localizados documentos posteriores da Bovespa/B3 que descrevem o BDI e a divulgação de informações do mercado a termo. Eles permanecem classificados apenas como evidência institucional posterior e não são utilizados para afirmar a regra vigente em 1986.

### 13.4 Controle de hipóteses

| Hipótese | Estado após esta etapa | Motivo |
|---|---|---|
| H1 — Tipo | PLAUSÍVEL / NÃO PROVADA | Há evidência contemporânea de Tipo × Prazo, mas não da linha Vigor de 10/10/1986 |
| H2 — taxa/preço | NÃO PROVADA | Nenhuma fonte contemporânea localizada estabelece essa chave para a colisão |
| H3 — participante/comitente/posição | NÃO PROVADA | Nenhuma fonte contemporânea localizada estabelece essa chave de agregação |
| H4 — regra histórica de agregação/publicação | PLAUSÍVEL / NÃO PROVADA | Continua compatível com a existência de uma dimensão editorial/operacional perdida na K4 |
| H5 — erro de processamento/publicação | NÃO PROVADA | Nenhuma errata/correção contemporânea localizada |

### 13.5 Rastro institucional

Foi criado o issue de acompanhamento:

**Issue #4 — FASE 09C — Recuperação do BDI Bovespa de 10/10/1986 — Vigor/VGO2**

Objetivo: manter rastreável a recuperação da fonte primária e impedir que a investigação seja encerrada por inferência.

### 13.6 Decisão desta rodada

A investigação **não avança para uma conclusão causal**.

O estado permanece:

- **IMPLEMENTADO:** SIM
- **EXECUTADO:** SIM
- **VALIDADO:** SIM, quanto ao protocolo e à evidência disponível
- **CAUSA HISTÓRICA RESOLVIDA:** NÃO
- **RAW ALTERADO:** NÃO
- **REGISTROS 140808/140809 FUNDIDOS:** NÃO

A próxima frente continua sendo a recuperação institucional/arquivística do BDI de 10/10/1986 e da documentação operacional efetivamente vigente naquele período.


## 14. FASE 09C — Rodada documental adicional: natureza e formato do BDI

### 14.1 Evidência histórica da existência do BDI

Foi localizada literatura acadêmica/documental que identifica o **BDI — Boletim Diário de Informações** como publicação diária da Bovespa e como fonte de dados completos sobre o pregão. A documentação consultada também registra o BDI como publicação própria da Bolsa de Valores de São Paulo.

Essa evidência confirma a existência e a função informacional do BDI no período histórico estudado, mas não fornece o exemplar específico de 10/10/1986.

### 14.2 Evidência sobre o arquivo BDI e sua relação com a estrutura de dados

Foi localizada documentação técnica histórica descrevendo o BDI eletrônico da Bovespa como arquivo gerado ao final do pregão. A mesma documentação reproduz o layout conhecido de dados Bovespa, no qual CODBDI é utilizado para classificação na emissão do BDI.

Isso reforça uma distinção importante para a reconstrução:

**COTAHIST não deve ser tratado automaticamente como cópia integral do BDI.**

O próprio layout preserva CODBDI como classificação relacionada à emissão do BDI, enquanto outras dimensões históricas de publicação podem não sobreviver no registro final de cotação.

### 14.3 Evidência contemporânea já recuperada

A edição do Jornal do Brasil de 05/06/1986 continua sendo a principal evidência contemporânea publicamente recuperada para a estrutura visual do mercado a termo. Ela apresenta explicitamente:

`Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°`

e registra Vigor como `Vigor PP C05`.

Essa evidência é consistente com a hipótese de que o processo editorial do mercado a termo possuía dimensões que não estão explicitamente representadas na K4.

**Limite:** não existe, nesta etapa, evidência suficiente para mapear `C05` para `Tipo`, nem para afirmar que a dimensão Tipo explica as duas linhas Vigor de 10/10/1986.

### 14.4 Evidência normativa posterior — somente como controle de contexto

Regulamento posterior da Bovespa descreve o BDI como publicação diária das operações dos mercados administrados pela Bolsa e das negociações/posições em mercados de liquidação futura. A fonte é posterior a 1986 e permanece classificada como **contexto institucional**, sem retroprojeção da regra.

### 14.5 Resultado da rodada

A rodada adicional aumenta a sustentação da hipótese de que:

1. o BDI era uma camada de publicação/informação própria da Bovespa;
2. o COTAHIST possui uma estrutura de dados relacionada ao BDI, mas não necessariamente equivalente;
3. havia dimensões de apresentação do mercado a termo que não aparecem explicitamente na K4;
4. a causa específica da colisão Vigor continua dependente do documento primário ou de documentação normativa contemporânea.

### 14.6 Estado após a rodada

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM, quanto à existência/função do BDI e à distinção entre publicação BDI e estrutura COTAHIST  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**EVIDÊNCIA DECISIVA:** ainda ausente  
**RAW:** preservado integralmente


## 15. Rodada documental adicional — 25/09/2026

### 15.1 Busca orientada por código e nomenclatura

Foi executada nova busca pública com combinações específicas de PP C05, Vigor PP C05, Vigor + mercado a termo, Vigor + Prazo, Vigor + 060, VGO2, BDI + Vigor, C05 + mercado a termo e manuais/regulamentos Bovespa relacionados ao mercado a termo.

O resultado não forneceu o exemplar primário do BDI de 10/10/1986 nem os exemplares adjacentes de 09/10/1986 e 13/10/1986.

### 15.2 Reforço da evidência contemporânea

A edição do Jornal do Brasil de 05/06/1986 continua sendo a evidência contemporânea pública mais útil localizada para a estrutura visual do Mercado a Termo. A publicação apresenta a separação entre Tipo e Prazo e registra Vigor com o código PP C05.

Esse achado permite afirmar com maior segurança que, em junho de 1986, a publicação do mercado a termo continha uma dimensão denominada Tipo, distinta da dimensão Prazo.

Não permite afirmar:
- que C05 seja o valor do campo Tipo;
- que C05 seja uma chave de agregação;
- que a colisão de 10/10/1986 tenha sido causada pelo campo Tipo;
- que as duas linhas COTAHIST correspondam a dois Tipos diferentes.

### 15.3 Controle de fontes normativas posteriores

Foram localizados manuais/regulamentos posteriores da Bovespa que descrevem codificação e divulgação de operações a termo no BDI. Esses documentos são úteis para compreender a função institucional do BDI, mas permanecem explicitamente classificados como evidência posterior.

A documentação posterior registra que determinadas informações de operações a termo e taxas eram divulgadas no BDI. Isso não é utilizado para reconstruir automaticamente a regra vigente em 1986.

### 15.4 Atualização das hipóteses

| Hipótese | Estado | Atualização |
|---|---|---|
| H1 — Tipo | PLAUSÍVEL / NÃO PROVADA | Evidência contemporânea confirma Tipo × Prazo, mas não identifica o Tipo das duas linhas Vigor de 10/10/1986. |
| H2 — taxa/preço | NÃO PROVADA | Nenhuma documentação contemporânea recuperada demonstra essa chave para o alvo. |
| H3 — participante/comitente/posição | NÃO PROVADA | Nenhuma documentação contemporânea recuperada demonstra essa chave de agregação para o alvo. |
| H4 — regra histórica de agregação/publicação | PLAUSÍVEL / NÃO PROVADA | Continua compatível com a existência de dimensão editorial/operacional ausente da K4. |
| H5 — erro de processamento/publicação | NÃO PROVADA | Não foi localizada errata/correção contemporânea. |

### 15.5 Decisão da rodada

A busca adicional não autoriza conclusão causal.

Estado:
- IMPLEMENTADO: SIM
- EXECUTADO: SIM
- VALIDADO: SIM, quanto à evidência disponível e aos limites da pesquisa
- CAUSA HISTÓRICA RESOLVIDA: NÃO
- RAW ALTERADO: NÃO
- REGISTROS 140808/140809 FUNDIDOS: NÃO
- ISSUE #4: atualizado com o resultado da rodada

A próxima ação permanece institucional/arquivística: obter o BDI de 10/10/1986 e a documentação operacional efetivamente vigente na Bovespa naquele período.


## 16. Rodada 25/09/2026 — verificação do canal institucional B3

### 16.1 Pesquisa por pregão da B3

A página oficial atual da B3 informa explicitamente que a **Pesquisa por pregão** fornece acesso a boletins diários e arquivos emitidos pela B3 e que arquivos retroativos podem ser obtidos selecionando a data desejada. citeturn1search0turn1search1

A própria documentação institucional também registra que, a partir de 2016, o antigo arquivo de Cotações do Histórico Regular, identificado como **BDI — Segmento BOVESPA**, teve sua publicação descontinuada no contexto da integração da pós-negociação. citeturn1search20

Esse achado é relevante porque confirma documentalmente que **BDI Segmento BOVESPA** era uma categoria específica de publicação histórica, distinta do conceito genérico de COTAHIST.

### 16.2 Limitação atual

A interface pública atualmente indexada não expôs diretamente o arquivo histórico de 10/10/1986 durante a pesquisa. Portanto, não é correto afirmar que o arquivo inexiste; apenas que ele não foi recuperado pela interface/indexação pública utilizada nesta etapa.

### 16.3 Consequência metodológica

A investigação passa a distinguir formalmente três camadas:

1. **COTAHIST** — arquivo histórico de cotações utilizado na reconstrução;
2. **BDI Segmento BOVESPA** — publicação histórica específica da Bolsa;
3. **Pesquisa por pregão B3** — canal institucional atual para arquivos/boletins retroativos.

A existência da camada 2 não resolve a colisão K4, mas fortalece a necessidade de recuperar o BDI original antes de atribuir semântica às duas linhas Vigor.

### 16.4 Próximo teste

O próximo teste documental será direcionado à recuperação do **BDI Segmento BOVESPA** por referência histórica, procurando:
- nomenclatura do arquivo;
- identificador/código do boletim;
- estrutura de URL ou catálogo histórico;
- documentação de migração/arquivo legado;
- referência institucional que permita solicitar especificamente o exemplar de 10/10/1986.

**Estado:** causa histórica ainda NÃO RESOLVIDA.


## 17. Rodada 25/09/2026 — arqueologia da nomenclatura do arquivo BDI

### 17.1 Identificação institucional mais precisa

Nova pesquisa documental recuperou o Comunicado oficial BM&FBOVESPA nº 031/2016-DO. O documento identifica expressamente o arquivo histórico como **Cotações do Histórico Regular (BDI — Segmento BOVESPA)** e informa que sua publicação seria descontinuada após a segunda fase do Projeto de Integração da Pós-Negociação. O comunicado também descreve canais de disponibilização de arquivos, incluindo Pesquisa por Pregão e FTP. citeturn1search11

Esse resultado é importante porque fornece uma nomenclatura institucional mais precisa para a busca arquivística. A investigação deixa de procurar apenas “BDI” e passa a procurar especificamente a expressão **Cotações do Histórico Regular / BDI — Segmento BOVESPA**.

### 17.2 Separação entre série BDI e filename moderno

A pesquisa encontrou também PDFs modernos com nomenclatura bdi_00_YYYYMMDD.pdf, identificados como Boletim Diário de Informações — Segmento Bovespa. Esses arquivos comprovam a existência de uma série documental BDI moderna, mas não demonstram que esse padrão de filename ou formato existisse em 1986.

Portanto, o padrão moderno não será retroprojetado para o período histórico.

### 17.3 Resultado da arqueologia

Até esta rodada, não foi recuperado:

- o filename histórico específico de 10/10/1986;
- um identificador persistente do exemplar;
- uma URL pública atual que abra diretamente o documento de 10/10/1986;
- uma especificação pública que prove o padrão de arquivo aplicável a 1986.

Foi criada a nota técnica:

docs/ingestao/FASE09C_BDI_SEGMENTO_BOVESPA_ARQUEOLOGIA_ARQUIVO_V1.0.md

Ela registra a nomenclatura institucional, o critério de evidência e a distinção entre pistas modernas e evidência histórica.

### 17.4 Consequência metodológica

A camada documental agora fica explicitamente separada em:

1. **COTAHIST** — fonte estatística histórica já preservada no repositório;
2. **Cotações do Histórico Regular / BDI — Segmento BOVESPA** — publicação histórica específica que precisa ser recuperada;
3. **Pesquisa por Pregão B3** — canal institucional posterior para consulta de arquivos/boletins.

A existência da segunda camada está documentalmente confirmada, mas o exemplar decisivo de 10/10/1986 continua não recuperado.

### 17.5 Estado da hipótese

A nova evidência fortalece a estratégia de recuperação institucional, mas **não resolve a causa da colisão K4**.

Permanece:

- **H1 — Tipo:** PLAUSÍVEL / NÃO PROVADA
- **H2 — taxa/preço:** NÃO PROVADA
- **H3 — participante/comitente/posição:** NÃO PROVADA
- **H4 — regra histórica de agregação/publicação:** PLAUSÍVEL / NÃO PROVADA
- **H5 — erro de processamento/publicação:** NÃO PROVADA

### 17.6 Estado operacional

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM, quanto à nomenclatura institucional e aos limites da busca  
**BDI 10/10/1986 RECUPERADO:** NÃO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO  
**REGISTROS 140808/140809 FUNDIDOS:** NÃO

### 17.7 Próxima frente

A busca continua exclusivamente na arqueologia do arquivo legado:

- documentação de migração para a Pesquisa por Pregão;
- manuais de Market Data que descrevam o arquivo legado;
- catálogos e identificadores históricos;
- referências a FTP/servidores legados;
- Centro de Memória B3;
- qualquer documento que permita solicitar o exemplar de 10/10/1986 por identificação inequívoca.

Não será aceito um filename moderno como substituto da fonte primária de 1986.


## 18. Rodada 25/09/2026 — limite da arqueologia pública e formalização da recuperação institucional

### 18.1 Nova busca de infraestrutura legada

Foi realizada nova busca documental especificamente por “Cotações do Histórico Regular”, FTP, DIN/MTA, Market Data, Pesquisa por Pregão, nome de arquivo, diretório e documentação de migração.

O resultado primário relevante continua sendo o Comunicado BM&FBOVESPA nº 031/2016-DO, que identifica expressamente **Cotações do Histórico Regular (BDI — Segmento BOVESPA)** e registra a existência de canais institucionais de distribuição, incluindo Pesquisa por Pregão, FTP e DIN/MTA.

Não foi localizado, em fonte pública indexada, um documento que forneça o filename, caminho de diretório ou identificador persistente do exemplar de 10/10/1986. citeturn1search26

### 18.2 Decisão metodológica

A investigação não continuará gerando URLs por combinação de padrões modernos. O padrão `bdi_00_YYYYMMDD.pdf` permanece classificado como **pista posterior**, sem aplicação retroativa a 1986.

A próxima ação formal é institucional/arquivística: solicitar o item pelo conjunto inequívoco de atributos do pregão e da colisão.

### 18.3 Documento de solicitação criado

Foi criado:

`docs/ingestao/SOLICITACAO_INSTITUCIONAL_BDI_BOVESPA_19861010_V1.0.md`

O documento especifica:

- BDI Segmento BOVESPA / Cotações do Histórico Regular;
- pregão 10/10/1986;
- Mercado a Termo;
- Vigor/VGO2;
- PP C05;
- prazo 060;
- CODBDI 62;
- TPMERC 030;
- CODISI VGORACPP;
- DIMES 104;
- linhas RAW 140808 e 140809;
- documentos secundários de 09/10/1986 e 13/10/1986;
- manual/regulamento vigente em 1986;
- legenda histórica de Tipo/Cxx.

### 18.4 Estado

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM — quanto ao protocolo e à infraestrutura documental identificada  
**BDI 10/10/1986 RECUPERADO:** NÃO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO  
**REGISTROS 140808/140809 FUNDIDOS:** NÃO

A FASE 09C permanece aberta até recuperação da fonte primária ou formalização documental de limite arquivístico suficiente para encerrar a reconstrução como inconclusiva.
