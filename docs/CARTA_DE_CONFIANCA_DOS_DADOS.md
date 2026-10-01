# CARTA DE CONFIANÇA DOS DADOS
## Repositório B3 — A BOLSA DO BRASIL

**Arquivo:** CARTA_DE_CONFIANCA_DOS_DADOS.md  
**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** carlos-andrade/B3  
**Data de criação:** 24/09/2026  
**Finalidade:** estabelecer os critérios mínimos para considerar confiáveis, auditáveis e reproduzíveis os dados gravados neste repositório.

---

## 1. Princípio fundamental

Nenhum dado deste repositório deve ser considerado confiável apenas porque está armazenado no GitHub.

A confiança deve resultar de uma cadeia verificável:

**fonte → aquisição → arquivo bruto → integridade → parsing → normalização → validação → reconciliação semântica → versionamento → auditoria.**

Se qualquer elo dessa cadeia estiver ausente, quebrado ou não documentado, o dado deve ser classificado como **não validado** até que a pendência seja resolvida.

---

## 2. Hierarquia de confiança

Os dados devem ser classificados, no mínimo, em quatro estados:

### 2.1 RAW — DADO BRUTO
Arquivo obtido da fonte original, preservado sem alteração semântica.

Regras:
- não alterar o conteúdo original;
- preservar nome, período, origem e data de aquisição;
- registrar checksum quando possível;
- nunca substituir silenciosamente um arquivo bruto.

### 2.2 PARSED — DADO EXTRAÍDO
Conteúdo convertido de seu formato original para uma representação estruturada.

Regras:
- manter referência inequívoca ao arquivo RAW;
- documentar layout, offsets, campos e tipos;
- registrar erros de leitura;
- não descartar registros silenciosamente.

### 2.3 NORMALIZED — DADO NORMALIZADO
Dados transformados para um esquema comum.

Regras:
- toda transformação deve ser determinística e documentada;
- códigos de origem não podem ser reinterpretados sem uma regra registrada;
- campos transformados devem manter rastreabilidade para o valor original;
- mudanças de regra exigem nova versão.

### 2.4 VALIDATED — DADO VALIDADO
Dado submetido aos testes definidos pelo projeto.

Somente este estado pode ser utilizado como base para análises quantitativas sem ressalva adicional.

---

## 3. Regra de rastreabilidade

Todo dado derivado deve poder responder:

1. Qual foi a fonte?
2. Qual arquivo original foi utilizado?
3. Qual período ele cobre?
4. Quando foi adquirido?
5. Qual versão do parser o processou?
6. Qual versão da normalização foi aplicada?
7. Quais validações foram executadas?
8. Qual commit produziu o resultado?
9. Quais registros foram rejeitados, corrigidos ou descartados?
10. É possível reproduzir o resultado?

Se essas perguntas não puderem ser respondidas, a confiança deve ser reduzida.

---

## 4. Integridade dos arquivos

Sempre que tecnicamente possível, cada arquivo de entrada deve possuir:

- tamanho em bytes;
- checksum/hash;
- fonte;
- URL ou identificador da origem;
- data de aquisição;
- período de referência;
- formato;
- versão do layout;
- status de validação.

Um arquivo cujo checksum mudou deve ser tratado como uma nova entrada até que a alteração seja explicada.

---

## 5. Integridade temporal

Datas são dados críticos.

Devem ser verificadas:

- data inicial;
- data final;
- continuidade temporal;
- duplicidade;
- registros fora do período esperado;
- datas inválidas;
- inversões temporais;
- lacunas justificadas e não justificadas;
- coerência entre data de negociação e calendário de mercado.

Não se deve preencher lacunas automaticamente sem registrar a regra utilizada.

---

## 6. Integridade estrutural

Cada dataset deve ser testado quanto a:

- quantidade de registros;
- quantidade de campos;
- tamanho dos registros, quando aplicável;
- tipos de dados;
- campos obrigatórios;
- valores nulos;
- valores fora do domínio;
- duplicidades;
- ordenação;
- chaves;
- consistência entre campos relacionados.

Falhas estruturais não podem ser mascaradas por conversões silenciosas.

---

## 7. Reconciliação semântica

Códigos de mercado não devem ser interpretados por aproximação.

Para campos como **TPMERC, CODBDI, CODNEG, ESPECI, PRAZOT, MODREF, PREULT, PREABE, PREMAX, PREMIN, PREMED, VOLTOT e QUATITENS**, a interpretação deve ser baseada na documentação da fonte e em evidência verificável.

Quando uma interpretação não puder ser comprovada, ela deve ser marcada como:

**HIPÓTESE — NÃO VALIDADA.**

Hipótese não pode ser promovida a fato apenas porque produz resultados plausíveis.

---

## 8. Regras específicas para COTAHIST

Para arquivos históricos da B3/COTAHIST:

- preservar os arquivos originais;
- respeitar o layout correspondente ao período;
- não assumir que layouts históricos são idênticos entre anos;
- validar o tamanho e a estrutura dos registros;
- mapear códigos explicitamente;
- separar mercado à vista, opções, futuros e demais modalidades conforme o código documentado;
- validar campos numéricos e casas decimais;
- validar datas;
- investigar registros rejeitados;
- registrar mudanças de layout;
- impedir que um parser moderno seja aplicado cegamente a arquivos históricos.

Um resultado aparentemente correto não substitui a validação do layout.

---

## 9. Regras contra dados inventados

É proibido:

- inventar registros;
- completar preços ausentes com estimativas sem marcação explícita;
- criar volume inexistente;
- inferir negócios que não estão presentes na fonte;
- transformar hipótese em dado;
- corrigir valores sem registrar o valor original;
- eliminar outliers sem justificativa e rastreabilidade;
- alterar retrospectivamente o RAW.

Qualquer imputação deve ser identificada como **DADO DERIVADO/IMPUTADO**, nunca como dado original.

---

## 10. Regras contra perda silenciosa

Nenhuma etapa de ingestão pode descartar registros sem contabilização.

Toda pipeline deve procurar produzir, quando aplicável:

**entrada → processados → aceitos → rejeitados → duplicados → corrigidos → saída.**

A soma das categorias deve ser reconciliável com a entrada, salvo exceções explicitamente documentadas.

---

## 11. Controle de duplicidade

Duplicatas devem ser investigadas antes de serem removidas.

Uma duplicidade pode representar:

- repetição legítima;
- registro duplicado na fonte;
- erro de ingestão;
- erro de chave;
- evento de mercado legítimo com atributos semelhantes.

Não se deve deduplicar apenas por aparência.

---

## 12. Versionamento

Toda alteração relevante em:

- parser;
- schema;
- mapeamento;
- normalização;
- validação;
- fonte;
- calendário;
- regras de classificação;

deve gerar versão identificável e commit no Git.

O histórico do Git constitui parte da trilha de auditoria.

Nenhum resultado validado deve depender de código ou regra que não esteja versionado.

---

## 13. Reprodutibilidade

Uma análise deve ser reproduzível a partir de:

**fonte + versão do código + parâmetros + regras + commit.**

Se duas execuções com os mesmos insumos e a mesma versão produzirem resultados diferentes, o pipeline deve ser considerado **não determinístico** até investigação.

---

## 14. Testes mínimos

Antes de promover um dataset a VALIDATED, devem ser executados, conforme aplicabilidade:

- teste de existência;
- teste de leitura;
- teste de encoding;
- teste estrutural;
- teste de schema;
- teste temporal;
- teste de duplicidade;
- teste de domínio;
- teste de cardinalidade;
- teste de continuidade;
- teste de reconciliação;
- teste de invariantes;
- teste de consistência entre etapas;
- teste de reprodutibilidade.

Os resultados dos testes devem ser preservados.

---

## 15. Evidência negativa também é evidência

Uma validação que falha deve ser registrada.

Não é permitido apagar o histórico de falhas apenas porque uma versão posterior foi corrigida.

Falhas importantes devem permanecer auditáveis para permitir reconstrução da evolução do projeto.

---

## 16. Separação entre fato, transformação e inferência

Todo resultado deve distinguir:

**FATO:** diretamente observado na fonte.

**TRANSFORMAÇÃO:** resultado determinístico de uma regra documentada.

**INFERÊNCIA:** interpretação produzida a partir dos dados.

**HIPÓTESE:** explicação ainda não comprovada.

Essa distinção é obrigatória em análises de mercado.

---

## 17. Dados para pesquisa quantitativa

Antes de utilizar uma série em backtests, estudos estatísticos ou modelos quantitativos, deve-se verificar:

- cobertura temporal;
- sobrevivência de ativos;
- corporate actions;
- splits;
- bonificações;
- dividendos;
- mudanças de ticker;
- ativos deslistados;
- viés de sobrevivência;
- liquidez;
- gaps artificiais;
- mudanças de metodologia;
- qualidade dos volumes;
- consistência dos preços.

Uma série histórica não é automaticamente adequada para backtest apenas por possuir muitas observações.

---

## 18. Proibição de confiança absoluta

Nenhum dataset deve ser descrito como:

**“100% correto”**, **“infalível”** ou **“sem erros”**.

A classificação apropriada é:

- **VALIDADO** — passou nos testes definidos;
- **VALIDADO COM RESSALVAS** — passou, mas possui limitações documentadas;
- **NÃO VALIDADO** — evidência insuficiente;
- **REJEITADO** — apresentou falha incompatível com o uso pretendido.

---

## 19. Regra de confiança operacional

A confiança de um dado é função da evidência disponível, não da aparência do resultado.

**Fonte confiável + arquivo íntegro + parser validado + semântica comprovada + testes aprovados + rastreabilidade + reprodutibilidade = dado apto ao uso definido.**

A ausência de qualquer componente crítico deve reduzir o nível de confiança.

---

## 20. Regra de ouro do repositório B3

> **Não confiaremos no dado porque ele parece correto. Confiaremos somente naquilo que conseguirmos rastrear, testar, reproduzir e explicar.**

Este documento estabelece a política de confiança dos dados do projeto **B3 — A BOLSA DO BRASIL** e deve ser tratado como documento normativo para as futuras etapas de ingestão, normalização, validação e análise.

---

## 21. Importação automática e atualização do COTAHIST

A ingestão do COTAHIST deve possuir uma cadeia automática de aquisição, integridade, normalização e validação sempre que a fonte permitir acesso automatizado.

Para a atualização corrente, o projeto utiliza a série diária pública da B3. A B3 informa que as séries históricas são disponibilizadas em ZIP e exigem o layout correspondente para interpretação. citeturn0search0turn0search13

A rotina automática deve: determinar a data de referência; adquirir o arquivo; validar o ZIP; calcular SHA-256; normalizar; executar validações; preservar evidências; publicar somente artefatos aprovados; tratar ausência de pregão como estado operacional conhecido; e falhar explicitamente em caso de corrupção ou erro de validação.

**Automação de aquisição não equivale a validação do conteúdo.** O arquivo somente poderá alimentar a camada oficial após integridade, parsing, normalização e validação.

### Estado atual

- automação de certificação: existente;
- automação de publicação do Dataset Oficial: existente;
- automação de aquisição diária do COTAHIST: formalizada e implementada no workflow corrente;
- disponibilidade da fonte B3: externa ao projeto e sujeita a mudanças.

A perda da fonte automática deve gerar incidente e não autoriza substituição silenciosa por fonte secundária.

---

## Controle de versão

**Versão:** 1.4  
**Data:** 01/10/2026  
**Alteração:** inclusão da governança da importação automática e atualização corrente do COTAHIST.  
**Status:** VIGENTE


## 22. CICLO DE CONFIANÇA, CERTIFICAÇÃO E FECHAMENTO

A confiança de um dataset histórico deve ser distinguida de sua simples existência, validação técnica e atualidade.

Para processos que adotem o ciclo formal COTAHIST, a cadeia passa a ser:

**RAW → PARSED → NORMALIZED → VALIDATED → PRÉ-RELEASE → VALIDAÇÃO INDEPENDENTE → CERTIFICADO → FECHADO → TRANSIÇÃO AUTORIZADA**

Cada estado exige evidência própria. Um estado posterior não deve ser usado como prova primária de um estado anterior quando o contrato exigir evidência específica.

### 22.1 CERTIFICADO
**CERTIFICADO** significa que o processo de certificação aplicável foi concluído e o escopo certificado está explicitamente identificado. Não significa que todos os demais períodos, datasets ou dados correntes estejam certificados.

### 22.2 FECHADO
**FECHADO** significa que o período cumpriu o conjunto de gates de encerramento definidos para o ciclo e possui evidência persistida de fechamento.

### 22.3 TRANSIÇÃO AUTORIZADA
A autorização para o próximo período é uma decisão de governança baseada em evidência. Ela não retrocertifica o próximo período e não substitui suas próprias validações.

### 22.4 Não retrocertificação
A certificação ou o fechamento de um ano não pode ser usado para declarar automaticamente como válidas as evidências de outro ano. Cada período deve manter sua própria cadeia de evidências.

## 23. Regra de confiança para dados correntes

A certificação histórica e a garantia de frescor são controles diferentes.

Um ano histórico pode estar **CERTIFICADO/FECHADO** enquanto a garantia de atualização dos dados correntes permanece **NÃO CERTIFICADA**. Nenhum dos estados invalida automaticamente o outro.

A utilização de dados correntes deve obedecer à matriz de frescor e às regras específicas de disponibilidade temporal.

## 24. Evidência de fechamento

Quando o processo possuir FASE12 ou equivalente, a evidência de fechamento deve registrar, no mínimo:
- período encerrado;
- fases e artefatos exigidos;
- resultado dos gates;
- certificação aplicável;
- bloqueios/exceções;
- hashes relevantes;
- decisão de fechamento;
- autorização ou bloqueio da transição;
- commit e workflow quando disponíveis.

## 25. Atualização da cadeia de confiança

A cadeia normativa passa a reconhecer que validação não é necessariamente o último estado operacional:

**fonte → aquisição → RAW → integridade → parsing → normalização → validação → reconciliação → pré-release → validação independente → certificação → fechamento → transição controlada → auditoria.**

A promoção deve permanecer fail-closed quando um gate crítico estiver ausente ou não comprovado.

## 26. Histórico de versões — atualização

| Versão | Data | Alteração | Status |
|---|---|---|---|
| 1.2 | 30/09/2026 | Inclusão do ciclo formal de certificação, fechamento, transição controlada, distinção entre confiança histórica e frescor corrente e evidência mínima de fechamento. | VIGENTE |


## 27. Regra canônica de localização

Para COTAHIST anual, a localização é determinística:

- RAW: `dados/cotahist/raw/anual/COTAHIST_A<AAAA>.ZIP`
- manifesto: `dados/cotahist/manifests/COTAHIST_A<AAAA>.json`
- checksum: `dados/cotahist/checksums/COTAHIST_A<AAAA>.ZIP.sha256`
- evidências: `dados/cotahist/quality/`
- certificação: `dados/cotahist/certificacao/`

**Regra:** ano → caminho canônico.

Uma busca ampla que não encontre um arquivo não constitui evidência de ausência. A verificação deve consultar o caminho canônico e, quando aplicável, a matriz de certificação.

Em 2026-10-01, o RAW de 1995 foi confirmado em `dados/cotahist/raw/anual/COTAHIST_A1995.ZIP`. Portanto, nenhum processo deve tentar baixá-lo ou duplicá-lo novamente apenas por uma busca incompleta.

## 28. Execução linear fail-closed

A ordem normativa do ciclo anual é:

**00 → 01 → 02 → 03–05 → 06 → 07 → 08 → GATE → 09 → GATE → 10 → GATE → 11 → GATE → 12 → transição autorizada.**

A regra operacional é:

**pré-condição válida → execução → evidência → gate → próxima fase.**

Falha em uma fase bloqueia as fases dependentes. Uma fase posterior não pode retrocertificar uma fase anterior.

## 29. Contrato de correção

`correction_required` e `correction_applied` são indicadores informativos. O gate deve avaliar o contrato por `correction_contract_valid`.

Quando nenhuma correção de dados é necessária:

- `correction_required=false`;
- `correction_applied=false`;
- `correction_contract_valid=true`.

É proibido alterar artificialmente indicadores para satisfazer um gate.

## 30. Incidentes de pipeline

Falha de workflow, falha de gate e falha de integridade do dado são classes distintas.

O Run #59 da FASE02/1994 foi classificado como falha do workflow, pois RAW, manifesto e checksum permaneciam coerentes. Os Runs #8 e #10 da cadeia 1994 demonstraram falhas lógicas de gate. Todos permanecem preservados como evidência histórica.

Uma correção posterior não apaga o incidente original.

## 31. Existência não é validação

A existência física de um arquivo prova apenas sua existência.

Validação exige evidência de integridade, processamento, testes e cumprimento do contrato aplicável.

A certificação anual 1986–2026 atualmente registrada demonstra presença de RAW para cada ano do intervalo, mas isso não elimina a necessidade de executar a cadeia própria de cada período quando o processo exigir fechamento formal.

## 32. Fechamento e transição

Um ano somente é formalmente fechado quando a FASE12 estiver concluída e sua evidência estiver persistida.

A transição para o ano seguinte não certifica o novo ano. O novo ano deve iniciar sua própria cadeia.

## 33. Histórico de versões — atualização

| Versão | Data | Alteração | Status |
|---|---|---|---|
| 1.2 | 30/09/2026 | Certificação, fechamento, transição controlada e distinção entre confiança histórica e frescor corrente. | SUPERADA |
| 1.3 | 01/10/2026 | Localização canônica, execução linear, contrato de correção, distinção entre falha de workflow e falha de dado, existência versus validação e preservação dos incidentes 1994. | VIGENTE |


## ADITIVO DE GOVERNANÇA — 2026-10-01 — FASE06/1995

### Regra permanente de reconciliação de chaves

A experiência da FASE06/1995 demonstrou que uma chave candidata não pode ser promovida automaticamente a chave lógica única apenas por conveniência de implementação.

A partir deste aditivo:

1. **Existência de duplicidade de chave candidata não é, isoladamente, corrupção do dado.**
2. A FASE06 deve registrar duplicidades como **observação diagnóstica**, sem reprovar o dataset exclusivamente por esse motivo.
3. A definição e o teste de unicidade da chave lógica pertencem ao contrato de **identidade/chaves da FASE07**, onde devem ser reconciliados com o layout oficial, o período histórico e os campos efetivamente disponíveis.
4. Uma chave somente pode ser declarada **canônica/única** quando houver evidência documental e empírica suficiente.
5. O validador não pode transformar uma hipótese de chave em regra de rejeição.
6. Duplicidades observadas devem permanecer quantificadas e auditáveis na evidência.
7. Se uma regra nova de validação contradizer dados históricos já certificados, a regra deve entrar em **reconciliação** antes de bloquear o ciclo.
8. Uma certificação anterior não substitui a investigação atual, mas também não pode ser ignorada sem análise de compatibilidade.

### Regra anti-regressão

Nenhum novo validador COTAHIST poderá introduzir uma condição de bloqueio baseada em:
- chave candidata não documentada;
- cardinalidade presumida;
- unicidade presumida;
- interpretação semântica não reconciliada;

sem antes possuir:
**fonte/layout → hipótese → amostra → teste histórico → decisão normativa → implementação → evidência.**

A FASE06/1995 passa a ser referência de incidente para impedir a repetição desse padrão.

### Incidente de referência

A execução comprovada da FASE06/1995 no workflow **Run 36859032714** identificou duplicidades na chave candidata data+codbdi+codneg+tpmerc. O incidente foi classificado como **falha do contrato do validador**, não como prova de corrupção do RAW.

O incidente permanece preservado e deve ser considerado em futuras certificações.

### Regra de não repetição de certificação

Antes de criar uma nova regra de certificação, o processo deve consultar:
- certificações anteriores;
- evidências das fases anteriores;
- incidentes históricos;
- contratos de chaves;
- layouts aplicáveis;
- exceções controladas.

A ausência dessa consulta é considerada falha de governança.

**Atualização normativa:** 2026-10-01 — inclusão da regra anti-regressão de chaves, classificação de duplicidades e obrigação de reconciliação antes de promover uma hipótese a critério de certificação.

## ADITIVO DE GOVERNANÇA — 2026-10-01 — ORDEM DE CORREÇÃO E AUDITORIA POR LAYOUT

A experiência acumulada nas auditorias de 1994 e 1995 passa a estabelecer uma ordem obrigatória para qualquer nova certificação COTAHIST.

### 1. Cartas antes do README

Após qualquer correção de regra, workflow, contrato ou evidência que altere a governança do projeto, a sequência obrigatória é:

**corrigir → atualizar as cartas normativas → registrar o incidente/evidência → verificar coerência documental → somente então atualizar o README.**

O README é camada de comunicação e inventário; não é a autoridade normativa. A atualização automática do README não pode antecipar nem substituir a atualização das cartas.

### 2. Layout antes da regra de auditoria

Antes de criar ou alterar um validador que dependa do significado, cardinalidade, identidade ou unicidade de campos COTAHIST, deve existir um contrato de layout aplicável ao período auditado.

A sequência mínima é:

**fonte oficial → layout aplicável → mapeamento de campos → hipótese de regra → amostra histórica → teste → decisão normativa → implementação → evidência → promoção.**

Nenhum critério de bloqueio deve ser criado apenas porque uma combinação de campos parece funcionar como chave.

### 3. Memória obrigatória das auditorias anteriores

Antes de executar uma nova fase, o processo deve consultar os incidentes e correções já registrados para evitar regressão. Em especial, os problemas de:

- busca incompleta de arquivos;
- confusão entre existência e validação;
- corrida de publicação;
- erro de heredoc/script;
- gates que avaliavam indicadores informativos como booleanos;
- execução não linear;
- unicidade presumida de chave;

não podem ser reintroduzidos por um novo workflow.

### 4. Regra de bloqueio preventivo

Se o layout aplicável não estiver identificado, ou se a regra proposta contradisser evidência histórica anterior, a auditoria deve parar em estado **AGUARDANDO RECONCILIAÇÃO**, e não transformar a incerteza em falha do dado.

**Regra permanente:** nenhum erro já corrigido deve voltar a ser convertido em critério de auditoria por falta de memória documental.

## CONTROLE DE VERSÃO — 2026-10-01

**Versão vigente:** 1.4  
**Alteração:** consolidação da regra de precedência documental, layout como pré-condição de auditoria e não repetição de erros já corrigidos.  
**Status:** VIGENTE

## REGRA PERMANENTE — ISOLAMENTO E MONOTONICIDADE DAS FASES — 2026-10-01

As fases são executadas em fluxo unidirecional e possuem responsabilidade própria. Uma fase posterior pode consumir evidência anterior em modo somente leitura, mas não pode reabrir, corrigir, substituir ou reescrever uma fase anterior. Uma fase anterior também não pode executar critérios pertencentes a uma fase posterior.

A regra operacional é:

**FASE N-1 → evidência → FASE N → evidência → FASE N+1.**

Correções pertencem à fase que originou o erro. Descoberta posterior gera incidente/impacto e revisão controlada, não correção silenciosa retroativa. Workflows concluídos não devem possuir gatilhos genéricos que os façam reexecutar por mudanças de README, documentação ou fases posteriores.

A matriz de responsabilidade vigente deve ser consultada antes da criação de qualquer novo workflow. Em particular, FASE06 é semântica/invariantes; FASE07 é identidade/chaves/cardinalidade; FASE08 é semântica/calendário/consistência; FASE09–12 não substituem essas fases.



## Aditivo normativo — GATE 06–08 — 2026-10-01

O projeto passa a reconhecer o **GATE 06–08 — PROMOÇÃO TÉCNICA** como barreira formal entre FASE08 e FASE09. O contrato específico está em 'docs/cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md'.

O Gate não é fase técnica e não pode corrigir, reexecutar ou substituir FASE06, FASE07 ou FASE08. Ele somente verifica as evidências dessas três fases, os estados permitidos, o ano/ciclo, exceções, bloqueadores e o isolamento de responsabilidades.

A promoção é **fail-closed**: somente 'LIBERADO_PARA_FASE09' quando todas as condições obrigatórias forem satisfeitas; qualquer ausência, estado inválido ou condição indeterminada produz 'BLOQUEADO_PARA_FASE09'.

Correções permanecem na fase de origem. README e documentação genérica não são fontes operacionais do Gate e não podem provocar reexecução retroativa de fases concluídas.


---

## REGRA DE CONSOLIDAÇÃO NO LAYOUT MESTRE — 2026-10-01

Esta carta é **documento de entrada e histórico de governança**. Ela não é uma especificação independente para geração de código.

Toda regra operacional desta carta que deva produzir ou alterar código deve ser consolidada no documento canônico:

`docs/governanca/LAYOUT_MESTRE_CANONICO_B3_V1.md`

Fluxo obrigatório:

**CARTA → PROPOSTA/CONTRIBUIÇÃO → RECONCILIAÇÃO → LAYOUT MESTRE → CÓDIGO → EVIDÊNCIA → VALIDAÇÃO.**

A carta não pode, isoladamente, disparar implementação, criar workflow, alterar parser, alterar validação ou determinar comportamento de código. Em caso de divergência operacional, o Layout Mestre prevalece até que uma reconciliação formal altere sua versão.

**Status desta carta:** preservada como fonte de entrada/histórico; regras executáveis subordinadas ao Layout Mestre.