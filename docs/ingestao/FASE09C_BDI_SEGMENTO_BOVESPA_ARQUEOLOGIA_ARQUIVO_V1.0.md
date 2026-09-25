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

Fonte oficial: Comunicado BM&FBOVESPA nº 031/2016-DO. citeturn1search20

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

A partir desta rodada, a busca passa a ser executada em quatro camadas:

1. **Nomenclatura:** “Cotações do Histórico Regular”;
2. **Identidade institucional:** “BDI — Segmento BOVESPA”;
3. **Canal:** Pesquisa por Pregão / arquivos históricos / legado;
4. **Documento-alvo:** pregão de 10/10/1986, Mercado a Termo, Vigor/VGO2, PP C05, prazo 060.

A ordem é deliberada: primeiro localizar a identidade documental, depois tentar o exemplar.

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
**VALIDADO:** SIM, quanto à identificação da nomenclatura institucional e aos limites da busca  
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

- BM&FBOVESPA, Comunicado nº 031/2016-DO — documento oficial que identifica expressamente “Cotações do Histórico Regular (BDI — Segmento BOVESPA)” e informa sua descontinuação no contexto da integração da pós-negociação. citeturn1search20

## 12. Rodada adicional — reconstrução do padrão moderno de distribuição

### 12.1 Padrão de URL documentado

Pesquisa histórica independente encontrou referências consistentes ao padrão de publicação:

`/download/BOLETINSDIARIOS/bdi_00_YYYYMMDD.pdf`

Exemplos documentados para 2011, 2013, 2014, 2015 e 2020 apontam para a mesma família de diretório/nomenclatura. Fontes públicas reproduzem, por exemplo, o arquivo de 16/10/2015 como `bdi_00_20151016.pdf` e referências acadêmicas citam o mesmo padrão para outros pregões. citeturn2search12turn2search13

### 12.2 Valor probatório

Esse resultado é útil como **pista de continuidade documental**, mas não prova que o padrão `bdi_00_YYYYMMDD.pdf` tenha existido em 1986.

A nomenclatura documentada pertence a uma infraestrutura posterior. Portanto, ela não será utilizada para fabricar ou validar um BDI de 10/10/1986.

### 12.3 Teste direto do endereço hipotético

Foi testado o endereço hipotético correspondente ao padrão moderno:

`https://bvmf.bmfbovespa.com.br/download/BOLETINSDIARIOS/bdi_00_19861010.pdf`

e a variante histórica no domínio `www.bmfbovespa.com.br`.

O mecanismo de acesso utilizado não conseguiu recuperar esses endereços. **Isso não demonstra inexistência do arquivo.** Apenas registra que o teste não produziu uma recuperação verificável.

### 12.4 Nova conclusão operacional

Temos agora três níveis de identificação:

1. **Série institucional:** Cotações do Histórico Regular — BDI — Segmento BOVESPA — CONFIRMADA.
2. **Padrão moderno de publicação BDI:** `BOLETINSDIARIOS/bdi_00_YYYYMMDD.pdf` — CONFIRMADO para períodos posteriores.
3. **Aplicação do padrão a 1986:** NÃO PROVADA.

Consequentemente, o próximo alvo não é gerar novas URLs por tentativa, mas localizar documentação que ligue explicitamente a série histórica de 1986 a um identificador, catálogo, microfilme, digitalização ou arquivo institucional.

## 13. Estado após esta rodada

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM, quanto às pistas documentais recuperadas  
**PADRÃO DE ARQUIVO DE 1986:** NÃO IDENTIFICADO  
**BDI 10/10/1986:** NÃO RECUPERADO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO

## 14. Rodada 25/09/2026 — fechamento da arqueologia pública e formalização do alvo institucional

### 14.1 Resultado da busca por canal legado

Nova rodada de busca foi direcionada especificamente para:

- “Cotações do Histórico Regular” + FTP;
- “BDI — Segmento BOVESPA” + FTP;
- DIN/MTA;
- Market Data;
- Pesquisa por Pregão;
- nome de arquivo e diretório;
- documentação de migração e legado.

O resultado relevante permaneceu restrito ao **Comunicado BM&FBOVESPA nº 031/2016-DO**, que confirma a identidade institucional do arquivo e menciona canais como Pesquisa por Pregão, FTP e DIN/MTA. Não foi localizado um documento público que forneça o caminho histórico, filename ou identificador persistente aplicável ao exemplar de 10/10/1986. citeturn1search20

### 14.2 Conclusão desta rodada

A arqueologia pública atingiu, por enquanto, o seguinte limite:

1. **Identidade da série:** CONFIRMADA — Cotações do Histórico Regular (BDI — Segmento BOVESPA).
2. **Existência de canais institucionais históricos:** CONFIRMADA — Pesquisa por Pregão/FTP/DIN/MTA em documentação posterior.
3. **Padrão moderno bdi_00_YYYYMMDD.pdf:** CONFIRMADO apenas para períodos posteriores.
4. **Filename/ID/URL específico de 10/10/1986:** NÃO IDENTIFICADO.
5. **BDI primário de 10/10/1986:** NÃO RECUPERADO.

A tentativa direta de uma URL moderna com a data 19861010 não produziu recuperação verificável e não é tratada como prova de inexistência.

### 14.3 Próximo passo formal

Foi criado no repositório:

`docs/ingestao/SOLICITACAO_INSTITUCIONAL_BDI_BOVESPA_19861010_V1.0.md`

O documento fixa o alvo arquivístico, os campos COTAHIST da colisão, os documentos prioritários e o critério mínimo de evidência para encerramento da FASE 09C.

**Estado:** BDI 10/10/1986 NÃO RECUPERADO; causa histórica NÃO RESOLVIDA; RAW preservado.

## 15. Rodada 25/09/2026 — teste de recuperação do endereço histórico citado na documentação de migração

### 15.1 Nova pista documental

O Comunicado BM&FBOVESPA nº 031/2016-DO informa que os arquivos de produção seriam disponibilizados pela Pesquisa por Pregão e por **FTP, “no endereço indicado anteriormente”**, além de DIN/MTA. O próprio comunicado, porém, não expõe no trecho recuperado qual era esse endereço anterior. citeturn1search20

### 15.2 Resultado do teste

Foi realizada nova busca orientada pela frase literal **“endereço indicado anteriormente”**, combinada com:

- BDI;
- FTP;
- Cotações do Histórico Regular;
- Segmento BOVESPA;
- Projeto de Integração da Pós-Negociação;
- DIN/MTA.

A busca não recuperou, em fonte pública indexada, o documento anterior que contenha de forma inequívoca o endereço FTP legado do BDI Segmento BOVESPA.

### 15.3 Valor probatório

Este resultado é importante porque delimita uma possível rota arquivística:

**Comunicado 031/2016-DO → documento anterior citado → endereço FTP legado → documentação/catálogo do BDI.**

Entretanto, o elo intermediário ainda não foi recuperado. Portanto:

- **FTP legado:** CONFIRMADO como canal histórico;
- **endereço FTP legado:** NÃO IDENTIFICADO;
- **BDI 1986 nesse endereço:** NÃO PROVADO;
- **causa da colisão K4:** NÃO RESOLVIDA.

### 15.4 Próxima frente técnica

A pesquisa deixa de procurar apenas pelo nome do arquivo e passa a procurar o **documento anterior ao Comunicado 031/2016-DO** que estabeleceu o endereço FTP mencionado.

Prioridades:

1. comunicados BM&FBOVESPA imediatamente anteriores a 01/07/2016;
2. documentos do Projeto de Integração da Pós-Negociação que descrevam Market Data/FTP;
3. manuais de acesso a arquivos históricos;
4. documentos que contenham simultaneamente “BDI — Segmento BOVESPA” e “FTP”;
5. qualquer índice/catalogação de arquivos históricos herdado pela B3.

A regra permanece: nenhum endereço será tratado como rota válida para 1986 sem evidência documental.

## 16. Estado atualizado

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM, quanto à delimitação da pista documental  
**FTP HISTÓRICO:** CONFIRMADO COMO CANAL  
**ENDEREÇO FTP HISTÓRICO:** NÃO IDENTIFICADO  
**BDI 10/10/1986:** NÃO RECUPERADO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO
