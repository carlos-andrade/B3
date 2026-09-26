# CARTA DE CONFIANÇA DOS WORKFLOWS — B3

**Arquivo:** CARTA_DE_CONFIANCA_WORKFLOWS.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Caminho:** governanca/CARTA_DE_CONFIANCA_WORKFLOWS.md  
**Data de criação:** 26/09/2026  
**Repositório:** carlos-andrade/B3  
**Versão:** 1.0  
**Status:** ATIVA  
**Natureza:** contrato operacional de confiabilidade, integridade, proveniência e auditoria

---

## 1. Finalidade

Esta Carta estabelece as condições técnicas mínimas para que os workflows automatizados do projeto B3 sejam considerados operacionalmente confiáveis.

A Carta não declara que uma fonte externa é infalível e não substitui auditoria, reconciliação ou validação independente. Ela define **quando o pipeline do projeto pode aceitar, transformar, publicar e versionar dados**.

A regra central é:

> **Dado somente pode ser considerado confiável dentro do projeto quando sua origem, captura, integridade, transformação e validação forem demonstráveis.**

---

## 2. Escopo

Esta Carta aplica-se a todos os workflows, scripts e processos automatizados que:

- capturam dados de mercado;
- capturam dados econômicos;
- importam COTAHIST;
- capturam dados do BCB, Copom e calendário econômico;
- normalizam arquivos;
- validam schemas e conteúdo;
- reconciliam fontes;
- geram artefatos derivados;
- atualizam dashboards;
- gravam dados no repositório;
- executam rotinas de manutenção, auditoria ou verificação;
- alimentam estudos, backtests ou automações posteriores.

A regra vale para workflows existentes e para qualquer workflow criado posteriormente.

---

## 3. Princípios obrigatórios

Todo workflow do projeto deve observar os seguintes princípios.

### 3.1 Fonte identificável

Toda captura deve identificar a fonte utilizada.

Sempre que tecnicamente possível, devem ser registrados:

- fonte;
- URL ou endpoint;
- recurso consultado;
- data/hora da captura;
- timezone;
- status HTTP;
- tipo de conteúdo;
- tamanho do conteúdo;
- hash SHA-256;
- versão do schema, quando aplicável.

### 3.2 Preservação do RAW

O conteúdo original recebido da fonte deve ser preservado antes da transformação.

O RAW é a evidência primária da captura realizada pelo pipeline.

Não é permitido considerar o NORMALIZED como substituto do RAW.

### 3.3 Separação RAW → NORMALIZED

A transformação deve ser explicitamente separada:

`FONTE → RAW → VALIDAÇÃO → NORMALIZED → PUBLICAÇÃO`

O NORMALIZED é uma representação derivada. Ele não deve destruir ou substituir a evidência original.

### 3.4 Integridade criptográfica

Quando o workflow gerar artefatos persistidos, deve registrar SHA-256 ou mecanismo equivalente adequado ao tipo de artefato.

O hash permite verificar se o conteúdo armazenado posteriormente corresponde ao conteúdo capturado.

### 3.5 Proveniência

Todo dado NORMALIZED relevante deve poder ser rastreado até o RAW que lhe deu origem.

Quando houver transformação, a relação deve ser documentável por:

- caminho do RAW;
- caminho do NORMALIZED;
- identificador da captura;
- timestamp;
- versão do script;
- commit Git;
- execução do workflow, quando disponível.

### 3.6 Validação antes de publicação

Nenhum dado NORMALIZED crítico deve ser publicado simplesmente porque o download funcionou.

A conclusão do transporte é apenas uma etapa do processo.

### 3.7 Falha explícita

Erro técnico, erro de schema, conteúdo vazio, resposta incompatível ou falha de validação deve produzir estado de falha quando impedir a conclusão confiável do processo.

Não é permitido mascarar uma exceção para transformar artificialmente um workflow em sucesso.

### 3.8 Idempotência

A reexecução de um workflow não pode corromper o histórico nem duplicar registros de forma indevida.

As chaves e regras de deduplicação devem ser determinísticas sempre que o domínio permitir.

### 3.9 Auditabilidade

Cada alteração automatizada relevante deve ser rastreável a:

- workflow;
- execução;
- script;
- commit;
- arquivos produzidos;
- validações realizadas.

### 3.10 Reprodutibilidade

Um workflow deve ser suficientemente determinístico para permitir investigação posterior de uma falha ou divergência.

---

## 4. Modelo de confiança operacional

A confiança do pipeline deve ser tratada em camadas.

### Camada 1 — Fonte

A origem do dado deve ser conhecida e identificada.

### Camada 2 — Transporte

O workflow deve comprovar que conseguiu obter uma resposta tecnicamente válida.

### Camada 3 — Evidência RAW

A resposta original deve ser preservada.

### Camada 4 — Integridade

O conteúdo deve possuir evidência de integridade adequada.

### Camada 5 — Schema

A estrutura deve corresponder ao contrato esperado ou a uma variante explicitamente suportada.

### Camada 6 — Semântica

Os campos devem representar o significado esperado.

### Camada 7 — Temporalidade

Datas, horários, períodos de referência e disponibilidade da informação devem ser coerentes.

### Camada 8 — Normalização

A transformação deve preservar os fatos relevantes da fonte.

### Camada 9 — Publicação

Somente dados aprovados pelas regras do pipeline podem ser disponibilizados como NORMALIZED confiável.

### Camada 10 — Versionamento

O resultado publicado deve ser versionado no Git quando fizer parte do estado persistente do projeto.

---

## 5. Estados operacionais

Os workflows devem distinguir pelo menos três estados conceituais:

### CONFIÁVEL

Todas as validações obrigatórias foram concluídas e as evidências mínimas estão presentes.

### CONDICIONAL

O dado pode existir como evidência ou material de investigação, mas possui uma ressalva documentada que impede seu uso como dado NORMALIZED definitivo.

### NÃO PUBLICÁVEL

Existe falha que impede a confiança mínima exigida.

Dados nesta condição não devem ser apresentados pelo pipeline como resultado normalizado válido.

---

## 6. Regra fundamental de publicação

> **NÃO CONFIAR = NÃO PUBLICAR.**

O pipeline deve interromper a cadeia de publicação quando ocorrer qualquer falha crítica, incluindo, mas não se limitando a:

- fonte indisponível;
- HTTP incompatível;
- conteúdo vazio;
- resposta truncada;
- JSON/XML/CSV inválido;
- schema incompatível;
- campo crítico ausente;
- tipo de dado incompatível;
- valor impossível dentro das regras do domínio;
- duplicidade não explicada;
- inconsistência temporal;
- quebra de continuidade não explicada;
- hash ausente quando obrigatório;
- RAW ausente;
- NORMALIZED sem evidência de origem;
- falha de reconciliação crítica;
- erro de transformação;
- exceção não tratada.

Uma falha não deve ser convertida silenciosamente em sucesso.

---

## 7. Critério para workflow SUCCESS

Um workflow pode ser considerado tecnicamente bem-sucedido somente quando:

1. as etapas obrigatórias foram executadas;
2. a fonte respondeu conforme o contrato esperado;
3. os dados necessários foram capturados;
4. o RAW foi preservado quando aplicável;
5. as validações obrigatórias passaram;
6. o NORMALIZED foi produzido quando previsto;
7. os metadados obrigatórios foram produzidos;
8. não houve falha crítica mascarada;
9. os artefatos foram persistidos conforme a política do workflow;
10. o commit foi realizado quando a etapa de versionamento fizer parte do contrato.

> **Workflow verde não significa que a realidade econômica é infalível. Significa que o processo cumpriu o contrato técnico definido para aquela execução.**

---

## 8. Critério para workflow FAILURE

O workflow deve terminar em FAILURE quando uma etapa crítica não puder ser concluída de forma confiável.

Um workflow não deve terminar em SUCCESS apenas porque:

- conseguiu acessar a URL;
- recebeu HTTP 200;
- criou um arquivo vazio;
- capturou parte dos dados;
- ignorou exceções;
- encontrou uma estrutura diferente e descartou o erro;
- publicou NORMALIZED sem validação.

---

## 9. Tratamento de retries

Retries devem ser:

- limitados;
- rastreáveis;
- tecnicamente justificados;
- seguros para reexecução;
- incapazes de mascarar falhas persistentes.

Erros transitórios de rede podem ser repetidos.

Erros de schema ou semântica não devem ser tratados como simples falhas transitórias sem diagnóstico.

Cada retry relevante deve permanecer auditável pelo histórico do workflow.

---

## 10. Idempotência e reexecução

A reexecução deve preservar a integridade histórica.

Quando possível:

- a mesma captura lógica deve produzir a mesma chave;
- registros equivalentes não devem ser duplicados;
- arquivos históricos não devem ser sobrescritos silenciosamente;
- correções devem possuir commit identificável;
- mudanças de conteúdo devem ser detectáveis por hash.

A reexecução de um workflow não pode ser utilizada para apagar evidências de uma execução anterior.

---

## 11. Schema e evolução das fontes

Fontes externas podem alterar nomes de campos, tipos ou estruturas.

O workflow deve:

1. detectar a variação;
2. tratar explicitamente as variantes suportadas;
3. registrar a transformação;
4. manter compatibilidade quando possível;
5. falhar de forma explícita quando a variação não puder ser interpretada com segurança.

Exemplo operacional já identificado no projeto: uma resposta do BCB apresentou variação na representação do campo de número de reunião. O código não deve assumir que `nroReuniao` estará sempre presente por indexação direta. Variações suportadas devem ser tratadas por função de extração segura e validação posterior.

---

## 12. Proveniência mínima obrigatória

Para dados de ingestão persistentes, o conjunto mínimo recomendado de metadados é:

| Campo | Obrigatório |
|---|---|
| source_url | Sim |
| final_url | Quando houver redirecionamento |
| retrieved_at | Sim |
| timezone | Sim |
| HTTP status | Sim, quando aplicável |
| content_type | Sim, quando aplicável |
| bytes | Sim, quando aplicável |
| sha256 | Sim para artefatos persistidos críticos |
| script/version | Sim |
| schema/version | Quando aplicável |
| raw_path | Sim quando houver RAW |
| normalized_path | Quando houver NORMALIZED |
| workflow/run | Sim quando disponível |
| git commit | Sim após versionamento |

---

## 13. Regras para dados econômicos e backtest

Dados econômicos não podem ser utilizados em backtest com informação que ainda não estava disponível no instante histórico analisado.

A regra operacional é:

`information_available_at <= bar_timestamp`

Quando a fonte disponibilizar posteriormente uma revisão de dado, a revisão deve ser tratada como nova informação, e não automaticamente como se estivesse disponível no passado.

O pipeline deve preservar, quando possível:

- data/hora do evento;
- data/hora de publicação;
- data/hora de disponibilidade;
- período de referência;
- versão ou revisão;
- fonte.

---

## 14. Regra específica para COTAHIST

O processo automático de COTAHIST deve obedecer ao mesmo contrato geral.

No mínimo, o pipeline deve:

1. identificar o período solicitado;
2. obter o arquivo da fonte definida;
3. preservar o RAW;
4. registrar metadados;
5. calcular hash;
6. validar tamanho e conteúdo;
7. validar estrutura dos registros;
8. validar período coberto;
9. identificar registros inválidos ou inesperados;
10. normalizar sem perder os campos necessários;
11. registrar a cobertura temporal;
12. evitar duplicação;
13. publicar somente após validação;
14. versionar o resultado no Git quando previsto;
15. produzir estado operacional verificável.

Uma execução automática não deve ser considerada concluída apenas porque o arquivo foi baixado.

---

## 15. Regra específica para BCB/Copom

Para dados do BCB/Copom, o pipeline deve tratar explicitamente:

- atas;
- comunicados;
- número da reunião;
- datas de referência;
- datas de publicação;
- texto;
- taxa quando extraível;
- URL do documento;
- disponibilidade da informação.

Campos com variações de nomenclatura devem ser normalizados por uma camada explícita de compatibilidade.

Uma exceção como `KeyError`, `JSONDecodeError`, falha de HTTP ou incompatibilidade semântica deve ser tratada como falha do pipeline, e não como ausência silenciosa de informação.

---

## 16. Política de commits

Quando um workflow produzir dados persistentes no repositório:

- o commit deve possuir mensagem identificável;
- o conjunto de arquivos alterados deve ser rastreável;
- o commit deve permitir reconstruir o estado publicado;
- correções de código devem possuir commit próprio quando tecnicamente conveniente;
- alterações de dados não devem apagar evidências históricas sem justificativa documentada.

O Git é parte da trilha de auditoria do projeto.

---

## 17. Segurança operacional

É proibido registrar em arquivos, logs ou artefatos públicos:

- tokens;
- senhas;
- chaves privadas;
- credenciais;
- segredos de autenticação.

Segredos devem permanecer em mecanismos apropriados do GitHub Actions ou do ambiente operacional.

---

## 18. Monitoramento obrigatório

A operação deve acompanhar, conforme a criticidade do workflow:

- última execução;
- último SUCCESS;
- último FAILURE;
- duração;
- frequência;
- atraso/freshness;
- quantidade de dados capturados;
- quantidade de registros normalizados;
- alterações anormais;
- falhas consecutivas;
- cobertura temporal.

O estado operacional deve ser verificável sem depender de interpretação manual do arquivo final.

---

## 19. Reconciliação

Quando houver mais de uma fonte independente para o mesmo fato, o projeto deve preferir reconciliação objetiva.

Diferenças devem ser classificadas como:

- diferença esperada;
- diferença de timestamp;
- revisão posterior;
- diferença de metodologia;
- erro de fonte;
- erro de transformação;
- diferença ainda não explicada.

Não é permitido escolher silenciosamente o valor mais conveniente.

---

## 20. Regra de não ocultação

Nenhum workflow deve:

- capturar uma exceção e continuar como se nada tivesse ocorrido;
- produzir arquivo parcial com aparência de completo;
- substituir dado inválido por zero sem regra documentada;
- substituir campo ausente por valor arbitrário;
- eliminar registros discrepantes sem registrar a razão;
- alterar histórico sem deixar trilha de auditoria;
- declarar sucesso quando uma etapa crítica falhou.

Quando uma decisão de fallback for necessária, ela deve estar codificada e documentada.

---

## 21. Contrato RAW → NORMALIZED

O pipeline deve ser compreendido como:

`SOURCE`
→ captura  
→ `RAW`
→ integridade  
→ validação estrutural  
→ validação semântica  
→ validação temporal  
→ transformação  
→ `NORMALIZED`
→ validação final  
→ publicação  
→ Git

Cada seta representa uma etapa verificável.

Se uma etapa crítica falhar, a cadeia deve parar ou produzir explicitamente um estado condicional/não publicável.

---

## 22. Matriz mínima de evidências

| Processo | Evidência mínima |
|---|---|
| Captura HTTP | URL + timestamp + status + conteúdo |
| Arquivo RAW | conteúdo + SHA-256 + metadados |
| JSON/XML/CSV | parse válido + schema |
| NORMALIZED | origem RAW + versão do transformador |
| Workflow | run + status + logs |
| Git | commit SHA + arquivos alterados |
| Backtest econômico | disponibilidade da informação |
| COTAHIST | período + integridade + cobertura |
| BCB/Copom | reunião + publicação + conteúdo + normalização |
| Dashboard | fonte dos dados + timestamp/versão |

---

## 23. Checklist de auditoria

Antes de considerar um pipeline confiável, verificar:

- [ ] Fonte identificada.
- [ ] URL/endpoint registrado.
- [ ] Timestamp registrado.
- [ ] Timezone registrado.
- [ ] RAW preservado quando aplicável.
- [ ] SHA-256 registrado quando aplicável.
- [ ] Schema validado.
- [ ] Campos críticos validados.
- [ ] Temporalidade validada.
- [ ] Duplicidade tratada.
- [ ] Transformação rastreável.
- [ ] NORMALIZED rastreável ao RAW.
- [ ] Falhas críticas interrompem a publicação.
- [ ] Retry não mascara erro estrutural.
- [ ] Reexecução é segura.
- [ ] Commit é rastreável.
- [ ] Workflow possui estado verificável.
- [ ] Backtest respeita disponibilidade temporal.
- [ ] Alterações de schema são tratadas explicitamente.
- [ ] Segredos não aparecem nos artefatos.
- [ ] Dados publicados possuem cobertura verificável.

---

## 24. Regra de confiança do projeto

A confiança não será determinada por aparência, quantidade de dados ou pelo simples estado verde do GitHub Actions.

A confiança será determinada pela evidência acumulada:

`FONTE + CAPTURA + RAW + INTEGRIDADE + SCHEMA + SEMÂNTICA + TEMPO + NORMALIZAÇÃO + AUDITORIA`

Quanto mais crítica for a utilização do dado, maior deve ser o nível de evidência exigido.

---

## 25. Regra para estudos e estratégias

Nenhum estudo quantitativo, indicador, backtest ou estratégia automatizada deve tratar um conjunto de dados como definitivo se o pipeline correspondente estiver:

- em FAILURE;
- com validação pendente;
- com schema incompatível;
- com proveniência quebrada;
- com período incompleto não documentado;
- com revisão histórica não identificada;
- ou em estado explicitamente NÃO PUBLICÁVEL.

A estratégia deve herdar a qualidade do dado que a alimenta.

---

## 26. Responsabilidade operacional

Esta Carta passa a ser parte integrante da governança do projeto B3.

Todo novo workflow deve respeitar este documento.

Toda alteração relevante em um workflow deve verificar se o contrato continua sendo atendido.

Se um workflow não puder cumprir este contrato, sua exceção deve ser:

1. identificada;
2. justificada;
3. documentada;
4. delimitada;
5. acompanhada de plano de correção, quando aplicável.

Exceções não devem se tornar comportamento silencioso permanente.

---

## 27. Regra de evolução

Esta Carta pode evoluir.

Toda nova versão deve:

- receber número de versão;
- registrar data;
- explicar a alteração;
- manter histórico;
- evitar alteração silenciosa de regras;
- atualizar workflows afetados.

Mudanças de contrato que alterem o significado de “confiável” devem ser explicitamente registradas.

---

## 28. Histórico de versões

### V1.0 — 26/09/2026

Criação da Carta de Confiança dos Workflows do projeto B3.

Estabelecidos:

- modelo de confiança em camadas;
- contrato RAW → NORMALIZED;
- critérios de SUCCESS e FAILURE;
- regra NÃO CONFIAR = NÃO PUBLICAR;
- proveniência;
- integridade por hash;
- validação de schema e semântica;
- temporalidade;
- idempotência;
- retries;
- auditoria;
- versionamento Git;
- regras de COTAHIST;
- regras de BCB/Copom;
- proteção contra ocultação de erros;
- requisitos para backtests;
- checklist operacional.

---

## 29. Declaração final

> **Os workflows do projeto B3 não devem ser tratados como caixas-pretas.**
>
> Cada workflow deve produzir evidência suficiente para que outra pessoa possa responder:
>
> **de onde veio o dado, quando foi capturado, o que foi recebido, como foi validado, como foi transformado, onde foi armazenado, qual versão do código o produziu e qual execução do workflow o publicou.**
>
> Se essas respostas não puderem ser demonstradas, a confiança deve ser reduzida e o dado não deve ser tratado como NORMALIZED definitivo.
>
> **Este é o padrão operacional mínimo para ingestão, transformação, publicação e utilização de dados no projeto B3.**

---

**Fim da Carta de Confiança dos Workflows — B3**
