# MODELO-MESTRE DE GOVERNANÇA PARA PROJETOS

**Arquivo:** MODELO_GOVERNANCA_PARA_PROJETOS.md  
**Projeto de origem:** B3 — A BOLSA DO BRASIL  
**Caminho:** docs/MODELO_GOVERNANCA_PARA_PROJETOS.md  
**Data de criação:** 25/09/2026  
**Repositório:** carlos-andrade/B3  
**Versão:** 1.0  
**Status:** VIGENTE  
**Natureza:** Norma-modelo reutilizável

---

## 1. FINALIDADE

Este documento estabelece o **modelo-mestre de governança** que deverá servir de referência para os demais projetos mantidos por Carlos Andrade.

A governança de cada projeto deverá ser formalizada em documento próprio, adaptado ao seu domínio, mas preservando os princípios, controles e critérios definidos neste modelo.

A experiência acumulada no Projeto B3 — incluindo ingestão de dados, reconciliação semântica, validações, auditorias, testes, versionamento, automação e tratamento de exceções — constitui a base prática deste modelo.

---

## 2. PRINCÍPIO SUPREMO

> **A governança prevalece sobre a conveniência operacional.**

Nenhum atalho operacional, pressão por velocidade, resultado esperado, hipótese de pesquisa ou preferência de implementação poderá justificar a violação das regras de integridade, rastreabilidade, reprodutibilidade e evidência definidas pela governança do projeto.

---

## 3. HIERARQUIA DE GOVERNANÇA

Quando houver conflito entre documentos ou decisões, deverá ser aplicada a seguinte ordem:

1. Carta Magna de Governança do projeto;
2. políticas e normas técnicas específicas;
3. carta ou política de confiança dos dados;
4. contratos e especificações de pipeline;
5. procedimentos operacionais;
6. detalhes de implementação.

Uma implementação nunca poderá contrariar uma norma superior sem uma alteração formal e versionada dessa norma.

---

## 4. PRINCÍPIOS OBRIGATÓRIOS

Todo projeto deverá observar, quando aplicável:

- **evidência:** afirmações relevantes devem possuir base verificável;
- **proveniência:** deve ser possível identificar a origem de dados e resultados;
- **rastreabilidade:** transformações devem poder ser reconstruídas;
- **reprodutibilidade:** resultados importantes devem poder ser reproduzidos;
- **integridade:** alterações não podem ocorrer silenciosamente;
- **transparência:** limitações e incertezas devem ser registradas;
- **separação epistemológica:** fato, transformação, inferência, hipótese e opinião técnica não devem ser confundidos;
- **versionamento:** código, documentação, regras e decisões relevantes devem ser versionados;
- **automação:** tarefas recorrentes e verificáveis devem ser automatizadas sempre que tecnicamente possível;
- **fail-closed:** uma validação crítica reprovada impede a promoção do artefato;
- **não retroatividade:** uma correção não deve apagar o histórico do estado anterior;
- **preservação de evidências:** falhas, exceções e resultados de testes relevantes devem permanecer auditáveis.

---

## 5. CICLO DE VIDA DOS ARTEFATOS

Cada projeto deverá definir estados adequados ao seu domínio. Como referência:

**FONTE → RAW → PROCESSADO → NORMALIZADO → VALIDADO → DERIVADO → PUBLICADO**

Também devem existir estados de exceção, como:

**NÃO VALIDADO → REJEITADO → DEPRECADO**

A passagem entre estados deverá possuir critérios objetivos.

Nenhum artefato poderá ser apresentado como validado quando não cumprir os critérios definidos para sua promoção.

---

## 6. FONTES E EVIDÊNCIAS

Cada projeto deverá estabelecer uma hierarquia de fontes.

Como regra geral:

1. fonte primária oficial;
2. documentação técnica oficial;
3. fonte institucional verificável;
4. fonte secundária especializada;
5. fonte terciária ou comunitária, quando necessária e devidamente identificada.

A autoridade de uma fonte não elimina a necessidade de verificar integridade, contexto, período de validade e compatibilidade com o objeto analisado.

Documentos externos não devem ser tratados como verdade automática.

Documentos internos definem o processo do projeto, mas não podem transformar uma hipótese em fato.

---

## 7. GOVERNANÇA DOS DADOS

Quando o projeto utilizar dados, deverá registrar, conforme aplicável:

- origem;
- data de aquisição;
- período de referência;
- formato;
- versão;
- checksum ou mecanismo equivalente de integridade;
- esquema;
- transformações aplicadas;
- regras de normalização;
- validações executadas;
- resultados das validações;
- limitações conhecidas;
- status de confiança;
- relação com dados derivados.

Nenhum dado relevante deverá ser inventado, completado silenciosamente ou alterado sem registro.

---

## 8. GOVERNANÇA TEMPORAL

Dados históricos devem respeitar mudanças de:

- formato;
- layout;
- nomenclatura;
- códigos;
- instrumentos;
- regras de mercado;
- calendários;
- unidades;
- convenções técnicas.

Uma regra válida em determinado período não deve ser aplicada retroativamente sem evidência de que sua validade se estende ao período anterior.

Segmentos históricos não resolvidos devem ser isolados e classificados como não validados.

**Um período não resolvido não deve contaminar períodos posteriormente validados.**

---

## 9. GOVERNANÇA SEMÂNTICA

Quando houver códigos, campos ou classificações, o projeto deverá distinguir:

- valor observado;
- significado documentado;
- interpretação técnica;
- inferência;
- hipótese.

Mapeamentos semânticos devem possuir evidência suficiente para justificar a interpretação adotada.

Quando o significado não puder ser determinado com segurança, o campo deverá permanecer explicitamente classificado como incerto ou não validado.

---

## 10. VALIDAÇÃO

Toda validação relevante deverá possuir:

1. objeto;
2. regra;
3. entrada;
4. método;
5. resultado;
6. evidência;
7. status;
8. data ou versão.

Testes positivos não eliminam a necessidade de testes negativos.

Quando aplicável, devem ser avaliados:

- completude;
- duplicidade;
- consistência estrutural;
- consistência temporal;
- consistência semântica;
- integridade numérica;
- continuidade;
- reconciliação;
- outliers;
- perdas silenciosas;
- alterações inesperadas;
- estabilidade entre versões.

---

## 11. AUDITORIA

Auditoria não deve verificar apenas se o resultado parece correto.

Deve verificar também:

- de onde veio;
- como foi transformado;
- quais regras foram aplicadas;
- quais testes foram executados;
- quais testes falharam;
- quais exceções permaneceram;
- quem ou qual processo produziu o resultado;
- qual versão estava vigente;
- se o resultado pode ser reproduzido.

A auditoria deverá preservar evidências suficientes para reconstrução posterior.

---

## 12. EXCEÇÕES E FALHAS

Falhas não devem ser escondidas para manter o pipeline verde.

Uma exceção deverá ser:

- identificada;
- classificada;
- registrada;
- isolada quando necessário;
- acompanhada de evidência;
- corrigida ou formalmente aceita como limitação.

Quando uma parte do projeto estiver inconclusiva, o restante poderá avançar desde que exista isolamento técnico suficiente para impedir contaminação dos resultados.

---

## 13. GIT E VERSIONAMENTO

O repositório deverá funcionar como registro histórico do projeto.

Alterações relevantes deverão ser:

- versionadas;
- descritas por mensagens de commit claras;
- associadas ao artefato alterado;
- preservadas no histórico.

Não deverá existir dependência de alteração manual local como fonte de verdade quando o repositório for o sistema oficial do projeto.

Documentos normativos devem possuir versão e status.

---

## 14. AUTOMAÇÃO E WORKFLOWS

Processos recorrentes deverão ser automatizados quando possível.

Workflows automatizados deverão:

- possuir finalidade identificável;
- produzir logs;
- expor falhas;
- preservar artefatos relevantes;
- evitar alterações silenciosas;
- ser reproduzíveis;
- possuir critérios de sucesso e falha.

Uma execução automática não será considerada correta apenas porque terminou sem erro técnico; os resultados também deverão passar pelas validações definidas.

Falhas recorrentes deverão ser tratadas como incidentes do projeto.

---

## 15. PUBLICAÇÃO E INTERFACES

Dashboards, páginas HTML, APIs, relatórios e demais interfaces deverão consumir dados provenientes das camadas governadas do projeto.

A interface não poderá:

- inventar valores;
- mascarar falhas;
- transformar ausência de dado em zero sem regra explícita;
- apresentar dado não validado como validado;
- apagar informação sobre limitações.

A apresentação deve preservar o status de confiança do dado de origem.

---

## 16. PESQUISA, ANÁLISE E INFERÊNCIA

Resultados analíticos deverão distinguir:

**FATO:** observado ou documentado.

**TRANSFORMAÇÃO:** resultado de uma regra determinística aplicada ao dado.

**INFERÊNCIA:** conclusão derivada dos fatos e transformações.

**HIPÓTESE:** explicação ainda não demonstrada.

**CENÁRIO:** condição hipotética utilizada para análise.

Nenhuma inferência deverá ser apresentada como fato.

---

## 17. MODELOS QUANTITATIVOS

Quando o projeto utilizar estatística, modelagem, backtest ou métricas quantitativas, deverão ser considerados, conforme aplicável:

- definição da amostra;
- período;
- granularidade;
- viés de seleção;
- survivorship bias;
- look-ahead bias;
- data snooping;
- overfitting;
- custos;
- slippage;
- liquidez;
- outliers;
- regime de mercado;
- estabilidade fora da amostra;
- drawdown;
- sensibilidade dos parâmetros.

Resultado histórico não constitui garantia de resultado futuro.

---

## 18. CRITÉRIOS DE PROMOÇÃO

Um artefato somente poderá avançar para um estado superior quando cumprir os critérios definidos para esse estado.

Como referência:

### NÃO VALIDADO
Há dados ou implementação, mas as evidências são insuficientes.

### VALIDADO COM RESSALVAS
Os critérios principais foram atendidos, mas existem limitações explicitamente registradas.

### VALIDADO
Os critérios definidos foram atendidos e as evidências são suficientes para o uso previsto.

### REJEITADO
O artefato falhou em requisito crítico ou apresentou inconsistência incompatível com o uso previsto.

### DEPRECADO
O artefato deixou de ser a versão vigente, mas permanece preservado para auditoria histórica.

---

## 19. PRINCÍPIO DA NÃO CONTAMINAÇÃO

Um erro localizado não deve ser propagado para dados, versões ou períodos que não dependem dele.

Quando uma inconsistência for encontrada, o projeto deverá determinar seu alcance:

**local → dependências diretas → dependências indiretas → impacto global**

Somente após essa análise deverá ser definida a necessidade de reprocessamento.

---

## 20. MUDANÇAS DE GOVERNANÇA

Alterações nas regras fundamentais do projeto deverão:

1. ser documentadas;
2. possuir justificativa;
3. indicar impacto;
4. possuir nova versão;
5. preservar a versão anterior;
6. registrar a data de vigência;
7. identificar os artefatos afetados.

Uma nova regra não deve apagar a existência da regra anterior.

---

## 21. REVISÃO PERIÓDICA

A governança deverá ser revisada quando houver:

- descoberta de nova evidência relevante;
- mudança estrutural do projeto;
- mudança de fonte;
- mudança de metodologia;
- falha sistêmica;
- nova classe de dados;
- alteração significativa de arquitetura;
- necessidade identificada por auditoria.

A revisão não deve ocorrer apenas por calendário; eventos relevantes também podem exigir revisão extraordinária.

---

## 22. REGISTRO DE DECISÕES

Decisões relevantes deverão registrar, quando aplicável:

- decisão;
- contexto;
- evidências consideradas;
- alternativas analisadas;
- motivo da decisão;
- impacto;
- data;
- versão;
- responsável pelo registro.

O objetivo é permitir que uma decisão seja compreendida mesmo depois de longo período.

---

## 23. REGRA CONTRA INVENÇÃO

Quando uma informação não estiver disponível ou não puder ser validada:

**não inventar.**

A resposta correta poderá ser:

- desconhecido;
- não encontrado;
- não validado;
- inconclusivo;
- indisponível;
- aguardando evidência.

A ausência de informação é um estado legítimo do projeto.

---

## 24. PRINCÍPIO DE REPRODUTIBILIDADE

Um resultado relevante deverá ser reproduzível a partir de:

**fonte + versão + regras + código + parâmetros + ambiente relevante + evidências**

Quando isso não for possível, a limitação deverá ser registrada.

---

## 25. RELAÇÃO COM A CARTA DE CONFIANÇA DOS DADOS

A **Carta de Confiança dos Dados** responde principalmente:

> **Quando podemos considerar um dado confiável para determinado uso?**

Este **Modelo-Mestre de Governança** responde:

> **Quais leis, princípios, controles e procedimentos devem reger a construção e manutenção do projeto?**

A Carta Magna específica de cada projeto deverá incorporar os dois conceitos sem confundi-los.

---

## 26. ADAPTAÇÃO A OUTROS PROJETOS

Este documento é um **modelo de referência**, não um molde cego.

Cada projeto deverá criar sua própria Carta Magna de Governança, adaptando:

- fontes;
- riscos;
- tipos de dados;
- requisitos legais;
- critérios de validação;
- arquitetura;
- segurança;
- métricas;
- ciclos de revisão.

Entretanto, os princípios de integridade, rastreabilidade, evidência, versionamento, transparência e não invenção devem ser preservados salvo justificativa formal e documentada.

---

## 27. REGRA FINAL

> **Se não puder ser rastreado, testado, reproduzido e explicado, não deverá ser tratado como conhecimento validado do projeto.**

O projeto pode avançar com incertezas.

O que não pode acontecer é transformar incerteza em certeza sem evidência.

---

## 28. HISTÓRICO DE VERSÕES

| Versão | Data | Alteração | Status |
|---|---|---|---|
| 1.0 | 25/09/2026 | Criação do modelo-mestre reutilizável. | VIGENTE |
| 1.1 | 25/09/2026 | Inclusão dos requisitos de automação de ingestão de fontes externas e atualização recorrente. | VIGENTE |

## 29. AUTOMAÇÃO DE INGESTÃO DE FONTES EXTERNAS

Quando um projeto depender de uma fonte externa recorrente, a governança deverá definir explicitamente o processo de atualização automática.

A cadeia mínima deverá ser:

**fonte externa → aquisição automática → RAW íntegro → checksum → parsing → normalização → validação → manifest → publicação**

A automação deverá registrar fonte, endpoint, data/hora da tentativa, período, resultado da aquisição, integridade, checksum, versão do parser, resultado dos testes, commit e falhas.

### 29.1 Falha da fonte

Se a fonte primária estiver indisponível, a pipeline deverá permanecer em estado explícito de falha/indisponibilidade. Não poderá substituir automaticamente a fonte por outra sem regra previamente governada.

### 29.2 Dados recorrentes

Para dados diários, mensais ou anuais, a governança deverá definir frequência, janela de atualização, política para dias sem publicação, reprocessamento, correções retroativas, retenção de evidências e alertas.

### 29.3 Aplicação ao COTAHIST

No Projeto B3, o COTAHIST corrente possui processo automático de aquisição diária quando a fonte pública permite. A série anual permanece responsável pelo backfill histórico e certificação. A série diária é a camada incremental corrente.

A existência do workflow automático não transforma, por si só, o arquivo em dado validado. A promoção depende da cadeia completa de confiança.

## 30. REGRA DE ATUALIZAÇÃO SEM CONTAMINAÇÃO

Uma atualização nova não poderá apagar a evidência da versão anterior. Correções retroativas da fonte devem ser registradas como nova evidência e seu impacto nos derivados deve ser determinado.

## 31. REGRA FINAL

> **Se não puder ser rastreado, testado, reproduzido e explicado, não deverá ser tratado como conhecimento validado do projeto.**

O projeto pode avançar com incertezas. O que não pode acontecer é transformar incerteza em certeza sem evidência.
