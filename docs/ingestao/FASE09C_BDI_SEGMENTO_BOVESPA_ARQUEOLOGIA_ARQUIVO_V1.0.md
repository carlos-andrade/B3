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

- BM&FBOVESPA, Comunicado nº 031/2016-DO — documento oficial que identifica expressamente “Cotações do Histórico Regular (BDI — Segmento BOVESPA)” e informa sua descontinuação no contexto da integração da pós-negociação. citeturn3search0

## 12. Rodada adicional — reconstrução do padrão moderno de distribuição

### 12.1 Padrão de URL documentado

Pesquisa histórica independente encontrou referências consistentes ao padrão de publicação:

`/download/BOLETINSDIARIOS/bdi_00_YYYYMMDD.pdf`

Exemplos documentados para períodos posteriores apontam para a mesma família de diretório/nomenclatura. Esses exemplos permanecem classificados como pista de continuidade documental, não como prova de aplicação em 1986.

### 12.2 Valor probatório

O padrão `bdi_00_YYYYMMDD.pdf` pertence a infraestrutura posterior e não será retroprojetado para 1986.

### 12.3 Teste direto do endereço hipotético

Foi testado o endereço hipotético correspondente ao padrão moderno:

`https://bvmf.bmfbovespa.com.br/download/BOLETINSDIARIOS/bdi_00_19861010.pdf`

e a variante histórica no domínio `www.bmfbovespa.com.br`.

O teste não produziu recuperação verificável. **Isso não demonstra inexistência do arquivo.**

### 12.4 Conclusão operacional

1. **Série institucional:** Cotações do Histórico Regular — BDI — Segmento BOVESPA — CONFIRMADA.
2. **Padrão moderno de publicação BDI:** `BOLETINSDIARIOS/bdi_00_YYYYMMDD.pdf` — CONFIRMADO para períodos posteriores.
3. **Aplicação do padrão a 1986:** NÃO PROVADA.

## 13. Estado após esta rodada

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM, quanto às pistas documentais recuperadas  
**PADRÃO DE ARQUIVO DE 1986:** NÃO IDENTIFICADO  
**BDI 10/10/1986:** NÃO RECUPERADO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO

## 14. Rodada 25/09/2026 — fechamento da arqueologia pública e formalização do alvo institucional

A busca foi direcionada para “Cotações do Histórico Regular” + FTP, BDI — Segmento BOVESPA + FTP, DIN/MTA, Market Data, Pesquisa por Pregão, nome de arquivo, diretório e documentação de migração.

O resultado relevante permaneceu restrito ao **Comunicado BM&FBOVESPA nº 031/2016-DO**, que confirma a identidade institucional do arquivo e menciona Pesquisa por Pregão, FTP e DIN/MTA. Não foi localizado um documento público que forneça o caminho histórico, filename ou identificador persistente aplicável ao exemplar de 10/10/1986. citeturn3search0

Foi criado:

`docs/ingestao/SOLICITACAO_INSTITUCIONAL_BDI_BOVESPA_19861010_V1.0.md`

**Estado:** BDI 10/10/1986 NÃO RECUPERADO; causa histórica NÃO RESOLVIDA; RAW preservado.

## 15. Rodada 25/09/2026 — rastreamento do endereço FTP legado

### 15.1 Pista documental

O Comunicado nº 031/2016-DO informa que os arquivos seriam disponibilizados por **FTP, “no endereço indicado anteriormente”**, além de Pesquisa por Pregão e DIN/MTA. O trecho recuperado não apresenta o endereço anterior. citeturn3search0

### 15.2 Teste

Foi realizada busca específica pela frase literal “endereço indicado anteriormente”, combinada com BDI, FTP, Cotações do Histórico Regular, Segmento BOVESPA, Projeto de Integração da Pós-Negociação e DIN/MTA.

Não foi localizado, em fonte pública indexada, o documento anterior que identifique inequivocamente o endereço FTP legado.

### 15.3 Valor probatório

Cadeia documental candidata:

**Comunicado 031/2016-DO → documento anterior citado → endereço FTP legado → documentação/catálogo BDI → exemplar 10/10/1986.**

Estado:

- FTP histórico: **CONFIRMADO**;
- endereço FTP histórico: **NÃO IDENTIFICADO**;
- BDI 1986 nesse endereço: **NÃO PROVADO**;
- causa da colisão K4: **NÃO RESOLVIDA**.

## 16. Rodada 25/09/2026 — busca dos comunicados antecedentes ao 031/2016-DO

### 16.1 Objetivo

A busca seguinte foi deslocada do arquivo para a **documentação antecedente** ao Comunicado nº 031/2016-DO, procurando localizar o documento que teria definido o “endereço indicado anteriormente”.

Foram pesquisadas, em fonte oficial B3, referências a:

- comunicados BM&FBOVESPA imediatamente anteriores;
- “Cotações do Histórico Regular”;
- “BDI — Segmento BOVESPA”;
- FTP;
- Pesquisa por Pregão;
- Boletim Diário de Informações;
- IPN / Projeto de Integração da Pós-Negociação.

### 16.2 Resultado

A pesquisa oficial recuperou novamente o Comunicado nº 031/2016-DO e documentação institucional sobre o IPN, mas **não recuperou um documento antecedente com o endereço FTP legado exposto de forma verificável**. O material institucional sobre o IPN confirma o contexto de migração, mas não fornece o endereço necessário para fechar a cadeia arquivística. citeturn3search0turn0search0

### 16.3 Consequência metodológica

A busca por “comunicado anterior” não produziu ainda o elo decisivo. Portanto, não é permitido transformar nenhum domínio, diretório ou filename posterior em rota histórica de 1986.

A cadeia continua parcialmente aberta:

**Série BDI CONFIRMADA → canal FTP CONFIRMADO → endereço FTP NÃO IDENTIFICADO → catálogo/arquivo 1986 NÃO RECUPERADO.**

### 16.4 Próxima frente

A próxima busca deverá priorizar:

1. documentos técnicos de Market Data anteriores e posteriores a 2016;
2. manuais de distribuição/recepção de arquivos;
3. documentação de FTP, DIN/MTA e Secure Client;
4. índices e catálogos legados da BM&FBOVESPA;
5. referências ao BDI em documentação de participantes;
6. eventual documentação arquivística do Centro de Memória B3.

## 17. Estado atualizado

**IMPLEMENTADO:** SIM  
**EXECUTADO:** SIM  
**VALIDADO:** SIM  
**SÉRIE BDI:** CONFIRMADA  
**FTP HISTÓRICO:** CONFIRMADO  
**ENDEREÇO FTP:** NÃO IDENTIFICADO  
**CATÁLOGO/ID DE 1986:** NÃO IDENTIFICADO  
**BDI 10/10/1986:** NÃO RECUPERADO  
**CAUSA HISTÓRICA RESOLVIDA:** NÃO  
**RAW ALTERADO:** NÃO
