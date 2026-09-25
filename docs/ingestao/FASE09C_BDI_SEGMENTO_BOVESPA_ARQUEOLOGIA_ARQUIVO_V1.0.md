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
