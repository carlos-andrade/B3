# FASE 08 — Pesquisa Documental Histórica — COTAHIST 1986

**Arquivo:** FASE08_PESQUISA_DOCUMENTAL_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Pesquisa documental da colisão K4 de 10/10/1986  
**Data:** 24/09/2026  
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

Foi localizada uma publicação contemporânea de 05/06/1986 contendo tabela de cotações da Bovespa. A tabela registra Vigor PP C05 e apresenta outras ocorrências do padrão Cxx, como Weg PP C35, Metal Duque PP C45 e Brahma OP C15. citeturn1search0

A evidência demonstra que:

- a identificação Vigor PP C05 existia publicamente antes do registro-alvo de outubro de 1986;
- a notação Cxx era usada para múltiplos papéis;
- portanto, PP *C05 no COTAHIST é compatível com uma convenção histórica de publicação de mercado.

A fonte não apresenta legenda suficiente para decodificar o número 05.

### 3.2 Evidência complementar sobre a persistência da convenção Cxx

Fonte de imprensa posterior preserva exemplos de papéis publicados com códigos Cxx, incluindo C05, C07, C15, C34, C35 e outros. Isso é apenas evidência corroborativa da existência da convenção; não deve ser usada para reconstruir retroativamente a semântica de C05 em 1986. citeturn1search41

## 4. O que a pesquisa NÃO resolveu

Não foi localizada, na busca pública realizada em 24/09/2026:

- cópia primária do Boletim Diário de Informações da Bovespa de 10/10/1986;
- legenda oficial contemporânea para C05;
- documento contemporâneo que associe VGO 2 a uma descrição cadastral completa;
- regra documental explicando duas linhas com K4 idêntica e agregados diferentes;
- fonte primária que estabeleça o significado de DATVEN = 99991231.

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

## 6. Regra de evidência

Não será feita nenhuma transformação de C05, VGO 2 ou DATVEN com base apenas em analogia moderna.

A colisão permanecerá preservada no RAW e será tratada como evento histórico observável até existir documentação primária suficiente.

## 7. Próxima frente

Prioridade máxima:

1. localizar Boletim Diário de Informações Bovespa de 10/10/1986;
2. localizar boletins dos dias úteis próximos, para acompanhar Vigor PP C05;
3. localizar regulamento/manual histórico do Mercado a Termo de 1986;
4. procurar documentos cadastrais/societários contemporâneos da Vigor;
5. comparar outros COTAHIST de 1986 com a mesma estrutura para verificar se duplicidades K4 ocorrem em outros papéis.

## 8. Status

**IMPLEMENTADO:** pesquisa documental executada.

**EXECUTADO:** fonte contemporânea com Vigor PP C05 localizada.

**VALIDADO:** existência histórica da notação Vigor PP C05; não validada a semântica do número 05.

**FASE 08:** ABERTA — investigação semântica continua.

## 9. Fontes

- Jornal do Brasil, 05/06/1986 — tabela de cotações Bovespa. citeturn1search0
- Evidência complementar em acervo de imprensa histórica. citeturn1search41

## 10. Segunda rodada — busca ampliada sobre C05 e mercado a termo

Em nova rodada de pesquisa foram consultados documentos históricos e normativos relacionados à Bovespa/CVM e ocorrências contemporâneas de C05.

### 10.1 C05 continua sem legenda documental

As buscas confirmam múltiplas ocorrências históricas de códigos Cxx em publicações de mercado, inclusive Vigor PP C05. Também aparecem combinações como C06*C05 e outros códigos Cxx em publicações posteriores. citeturn5search0turn6search0

Isso reforça que C05 é parte de uma convenção histórica de identificação/publicação, mas **não autoriza concluir que C05 seja concordata, classe acionária, série, direito ou evento societário específico**.

Uma fonte secundária de reprodução do layout histórico lista CODBDI 06 como "Concordatárias", enquanto CODBDI 62 corresponde ao mercado a termo. Isso é útil para separar os campos: a presença de C05 em ESPECI não deve ser confundida automaticamente com CODBDI 06. citeturn3search1

### 10.2 Mercado a termo

A regulamentação Bovespa disponível confirma que operações a termo possuem ativo-objeto e prazo de liquidação previamente fixado. A documentação normativa atual não é usada para reconstruir automaticamente a regra de 1986; serve apenas como contexto institucional. citeturn0search41

A Instrução CVM nº 36/1984 é uma fonte normativa contemporânea relevante para o estudo histórico dos mercados a futuro, a termo e de opções. Ela deve ser tratada como fonte primária regulatória de 1984, não como prova automática da regra específica de agregação do COTAHIST em 1986. citeturn0search42

### 10.3 Resultado desta rodada

Não foi localizada ainda uma fonte primária que explique:

- o significado numérico de C05;
- a convenção VGO 2;
- a origem de DATVEN 99991231;
- a razão para duas linhas com K4 idêntica em 10/10/1986.

**Nova evidência:** C05 é uma convenção histórica efetivamente publicada no mercado.

**Não houve mudança de classificação:** a causa da colisão K4 continua indeterminada.

## 11. Próxima investigação técnica

A investigação passa a ter duas frentes paralelas:

**A — documental**
1. localizar BDI/Bovespa de 10/10/1986;
2. localizar regulamentos Bovespa de 1984–1987 específicos do mercado a termo;
3. localizar tabelas históricas de códigos/legendas Cxx;
4. localizar documentação cadastral de Vigor.

**B — estatística no próprio COTAHIST 1986**
1. reconstruir a cronologia completa de C03 → C05 para VGORACPP;
2. medir a primeira e a última ocorrência de cada ESPECI;
3. cruzar ESPECI × DIMES × TPMERC × PRAZOT;
4. verificar se C05 aparece em outros CODISI;
5. procurar padrões de duplicidade de K4 em outros contextos históricos, caso existam.

Essa segunda frente pode revelar a regra de transição sem depender exclusivamente da recuperação de um BDI escaneado.

## 12. Estado

**IMPLEMENTADO:** segunda rodada documental executada.

**EXECUTADO:** fontes normativas e ocorrências históricas adicionais pesquisadas.

**VALIDADO:** C05 é convenção histórica observável; não validada sua legenda semântica.

**FASE 08:** ABERTA.

## 13. FASE 08B — Controle de execução e publicação da análise cronológica

O parser foi ampliado para reconstruir cronologicamente as transições do código VGO 2 em 1986, incluindo:

- transições de ESPECI por pregão;
- transições de DIMES por pregão;
- contexto de CODBDI × TPMERC × PRAZOT por pregão;
- contagem de duplicidades K4;
- exemplos de duplicidade no mesmo dia.

Commit do parser: `1d40ff35f355fb19be667268064095941b451973`.

A inspeção do parser confirma que essas estruturas estão implementadas no código e destinadas ao JSON de evidência.

### 13.1 Gate de evidência

Na verificação de 24/09/2026, o arquivo publicado em `dados/cotahist/quality/COTAHIST_1986_FASE08_SEMANTICA_K4_V1.json` ainda contém a versão anterior da evidência, com `schema_version = 1.0.0`, portanto **não foi considerado como resultado executado da FASE 08B**.

Isso é deliberado: não será atribuído status VALIDADO a uma análise cujo artefato de saída ainda não reflita o parser atualizado.

O arquivo publicado anterior continua útil como evidência da FASE 08A e preserva:

- 177.981 registros tipo 01;
- 2 linhas-alvo;
- 473 ocorrências de `CODISI = VGORACPP`;
- 443 ocorrências de `CODNEG = VGO 2`;
- 188 ocorrências de VGO 2 em mercado a termo;
- 246 ocorrências de VGO 2 em mercado à vista;
- 136 registros a termo com `PRAZOT = 030`;
- 52 registros a termo com `PRAZOT = 060`;
- 261 ocorrências de VGO 2 com `ESPECI = PP *C05`;
- 261 ocorrências de VGO 2 com `DIMES = 104`.

Esses números são tratados como evidência publicada da FASE 08A, não como saída nova da FASE 08B.

### 13.2 Classificação atual — FATO → PADRÃO → HIPÓTESE → EVIDÊNCIA NECESSÁRIA

**FATO**

- Em 10/10/1986 existem duas linhas RAW com a mesma chave K4 utilizada pela investigação.
- As linhas não são byte-idênticas e possuem estatísticas de negociação diferentes.
- O mesmo VGO 2 aparece em contexto à vista e a termo ao longo de 1986.
- No próprio dia 10/10/1986 há uma linha à vista e duas linhas a termo para VGO 2.
- As duas linhas a termo têm `PRAZOT = 060`, `ESPECI = PP *C05`, `DIMES = 104` e `CODISI = VGORACPP`.

**PADRÃO OBSERVADO**

- VGO 2 não é exclusivo do mercado a termo.
- A identificação Vigor/PP/Cxx aparece em publicação histórica contemporânea.
- Há reutilização do mesmo CODISI em diferentes contextos de mercado e diferentes valores de DIMES/ESPECI no arquivo de 1986.

**HIPÓTESE**

As duas linhas podem representar agregações ou classes de publicação distintas associadas à mesma identidade contratual/cadastral capturada pela K4. A hipótese permanece aberta entre, pelo menos, artefato de publicação, regra de agregação histórica ou classe de registro não representada pela K4 atual.

**EVIDÊNCIA NECESSÁRIA**

Para elevar a hipótese a conclusão documental são necessários:

1. o BDI/boletim de 10/10/1986 ou dia imediatamente anterior/posterior;
2. manual/layout histórico da Bovespa usado em 1986;
3. legenda contemporânea de C05;
4. regra histórica de publicação/agregação das operações a termo;
5. evidência independente que explique o uso de VGO 2 e DIMES 104.

### 13.3 Regra de governança

Até a publicação da saída atualizada da FASE 08B:

- RAW permanece intocado;
- nenhuma das duas linhas será removida;
- nenhuma linha será consolidada;
- nenhuma semântica econômica será inferida por igualdade de K4;
- o status da FASE 08B permanece **IMPLEMENTADO / EXECUÇÃO NÃO COMPROVADA NO ARTEFATO DE SAÍDA**.

## 14. Próximo passo controlado

A próxima ação técnica é publicar e verificar a saída do parser `1d40ff35f355fb19be667268064095941b451973`.

Somente depois dessa publicação serão extraídos os resultados completos de:

- `vgo_especi_transitions`;
- `vgo_dimes_transitions`;
- `vgo_market_by_date`;
- `duplicate_k4_groups_count`;
- `duplicate_k4_same_day_groups_count`.

A classificação documental e a eventual decisão de modelagem dependerão desses resultados.


## 15. FASE 08D — Reconstrução documental de 10/10/1986

A FASE 08D foi executada em 24/09/2026 com busca direcionada por fontes contemporâneas ao evento de 10/10/1986.

### 15.1 Resultado

Não foi localizada cópia primária verificável do Boletim Diário de Informações da Bovespa de 10/10/1986. Também não foi localizada documentação primária que explique diretamente a duplicidade K4.

Foi localizada, entretanto, evidência contemporânea anterior ao evento: publicação do Jornal do Brasil de 05/06/1986 com a identificação **Vigor PP C05**, além de outras ocorrências de códigos Cxx. Essa fonte valida a existência histórica da convenção de publicação, mas não decodifica o C05.

Também foi localizada fonte normativa oficial do Senado referente ao Decreto-Lei nº 2.286/1986, relacionado a operações a termo. Ela confirma o contexto regulatório contemporâneo, mas não explica a regra de gravação do COTAHIST.

### 15.2 Classificação

**FATO VALIDADO**
- Vigor PP C05 já era publicado antes de outubro de 1986.
- Operações a termo possuíam tratamento normativo específico em 1986.
- A colisão K4 de 10/10/1986 permanece única no COTAHIST 1986 segundo a FASE 08C.

**NÃO DETERMINADO**
- significado numérico de C05;
- significado histórico completo de VGO 2;
- significado histórico de DIMES 104;
- significado de DATVEN=99991231;
- causa da existência de duas linhas com K4 equivalente e estatísticas distintas.

Documento detalhado:
`docs/ingestao/FASE08D_COTAHIST_1986_RECONSTRUCAO_DOCUMENTAL_10101986_V1.0.md`

Commit: `e2bdc5a8ed434d754ad5640c4b218d0e7d62f3c6`

### 15.3 Próxima frente

A próxima frente controlada é a **FASE 08E — Reconstrução estatística da cronologia C03/C05/Cxx e DIMES/VGO 2**, usando somente o COTAHIST 1986 preservado, antes de qualquer nova hipótese semântica.


## 16. FASE 08H — Recorrência multianual de colisões K4

A FASE 08H foi executada sobre todos os arquivos `COTAHIST_A*.ZIP` presentes em `dados/cotahist/raw/anual`.

### 16.1 Cobertura

Foram analisados **41 anos, de 1986 a 2026**, totalizando **24.314.082 registros tipo 01**.

### 16.2 Resultado

O universo produziu:

- 24.314.081 grupos K4;
- 1 único grupo K4 duplicado;
- 2 linhas pertencentes ao grupo duplicado;
- 1 único grupo K4 com estatísticas diferentes;
- 0 grupos K4 duplicados com estatísticas comparadas idênticas;
- somente o ano **1986** com colisão K4.

A única colisão continua sendo:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW 140808 e 140809.

### 16.3 Conclusão controlada

A colisão K4 de 10/10/1986 é **única no universo anual analisado de 1986–2026**.

Isso valida a singularidade estatística do evento dentro do acervo, mas **não explica sua causa histórica**.

A investigação não autoriza concluir que a colisão seja erro, duplicação indevida, classe econômica distinta ou regra específica de agregação sem documentação adicional.

### 16.4 Governança

RAW permanece intocado.

Nenhuma linha foi removida ou consolidada.

Nenhuma identidade econômica foi inferida.

Documento detalhado:

`docs/ingestao/FASE08H_COTAHIST_RECORRENCIA_K4_MULTIANOS_V1.0.md`

Evidência:

`dados/cotahist/quality/COTAHIST_FASE08H_RECORRENCIA_K4_MULTIANOS_V1.json`

Workflow run: **36070061381 — SUCCESS**.

Commit de publicação da evidência: `c19566cf1481c245b6908f4a3e2238138656c229`.

### 16.5 Estado

**IMPLEMENTADO:** análise multianual criada.

**EXECUTADO:** 41 arquivos anuais processados.

**VALIDADO:** a colisão K4 com estatísticas diferentes ocorre somente em 1986 no universo analisado.

**FASE 08:** a pergunta de recorrência multianual está encerrada; permanece aberta a reconstrução histórica da regra que gerou a colisão.


## 17. FASE 08K — Arqueologia do BDI/COTAHIST

A FASE 08K localizou evidência contemporânea de 1986 que preserva a estrutura pública da tabela de **Mercado a Termo** da Bolsa de Valores de São Paulo.

A publicação do Jornal do Brasil de 05/06/1986 apresenta a estrutura:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

e exemplos com prazo **030**, quantidade, preços e número de negócios. citeturn3view1turn4view0

A mesma publicação registra **Vigor PP C05**, além de outras combinações Cxx, confirmando que a notação Cxx era efetivamente utilizada na publicação de mercado antes de outubro de 1986. citeturn3view0

### 17.1 Resultado estrutural

A evidência permite separar duas camadas:

- identificação/estrutura do instrumento e operação;
- agregados estatísticos da negociação.

Isso é compatível com a observação das fases 08F–08I de que as duas linhas de 10/10/1986 possuem K4 equivalente, mas estatísticas diferentes.

A evidência **não prova** que a Bovespa deliberadamente gerava duas linhas para a mesma K4. Ela apenas demonstra que a publicação histórica possuía múltiplas dimensões estatísticas que não fazem parte da K4 investigada.

### 17.2 Estado após 08K

**FATO VALIDADO:** estrutura pública histórica do Mercado a Termo com Tipo, Prazo, Quant, Fech, Máx, Mín, Méd e N°.

**FATO VALIDADO:** Vigor PP C05 já era publicado em junho de 1986.

**NÃO RESOLVIDO:** regra formal que explique duas linhas com a mesma K4 e agregados diferentes.

**EVIDÊNCIA AUSENTE:** BDI primário de 10/10/1986, manual interno de geração do COTAHIST, legenda oficial contemporânea de C05 e regra formal de agregação.

Documento detalhado: docs/ingestao/FASE08K_COTAHIST_1986_ARQUEOLOGIA_BDI_TABELA_TERMO_V1.0.md

Commit: f8439257cda46569e40b02980434f5fe60ea0cf1

**FASE 08K:** IMPLEMENTADA / EXECUTADA / VALIDADA quanto à estrutura documental encontrada; causa da colisão permanece NÃO DETERMINADA.


## 18. FASE 08L — Dimensões ocultas do Mercado a Termo

A FASE 08L comparou publicações históricas de 1986, 1987 e 1988 para testar se **Tipo**, **Prazo** e a convenção **Cxx** poderiam explicar a colisão K4.

A publicação de 1986 apresenta Tipo e Prazo na tabela de Mercado a Termo e registra Vigor PP C05. citeturn1search0turn2search1 Uma publicação de 1987 também mostra Cxx associado aos títulos. citeturn2search0turn2search2 Em 1988, a tabela de Operações a Termo apresenta explicitamente **Títulos | Tipo | Prazo | Quant. | Fech. | Máx. | Min. | Méd. | Volume | Nº neg.**, com exemplos de Tipo PP-Q e Prazo 030. citeturn1search29

### 18.1 Resultado

**VALIDADO:** Cxx não deve ser tratado como sinônimo da coluna Tipo.

**VALIDADO:** Tipo e Prazo aparecem como dimensões separadas na documentação pública posterior.

**NÃO VALIDADO:** a codificação exata de Tipo em 1986.

**NÃO VALIDADO:** qualquer dimensão oculta que explique especificamente as duas linhas de 10/10/1986.

**HIPÓTESE PRINCIPAL:** regra histórica de agregação/publicação ou dimensão operacional não preservada pela K4.

Documento detalhado:
`docs/ingestao/FASE08L_COTAHIST_1986_DIMENSOES_OCULTAS_TERMO_V1.0.md`

Commit: `161dac2a46d5d9df747da0408e53395885e289b8`

**FASE 08L:** IMPLEMENTADA / EXECUTADA / VALIDADA quanto à separação conceitual Tipo × Prazo × Cxx; causa da colisão permanece NÃO DETERMINADA.
