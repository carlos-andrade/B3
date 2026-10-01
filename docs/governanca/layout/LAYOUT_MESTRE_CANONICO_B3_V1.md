# LAYOUT MESTRE CANÔNICO DE GOVERNANÇA, EXECUÇÃO E GERAÇÃO DE CÓDIGO — B3

**Projeto:** B3 — A BOLSA DO BRASIL  
**Repositório:** carlos-andrade/B3  
**Arquivo canônico:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`  
**Versão:** 1.0.0  
**Data:** 2026-10-01  
**Status:** VIGENTE  
**Natureza:** documento normativo único para execução, governança e geração de código

---

## 1. FINALIDADE

Este documento consolida em um único layout operacional as regras que governam:

- dados;
- ingestão;
- preservação do RAW;
- parsing;
- normalização;
- manifestos;
- checksums;
- semântica;
- identidade e chaves;
- calendário;
- validação;
- gates;
- certificação;
- fechamento;
- workflows;
- monitoramento;
- reexecução;
- auditoria;
- versionamento;
- geração e alteração de código;
- atualização de documentação;
- tratamento de incidentes;
- rastreabilidade.

A partir desta versão, **este layout é a única especificação normativa operacional utilizada diretamente para criar, alterar ou validar código no repositório B3**.

As cartas e demais documentos normativos anteriores passam a funcionar como **fontes de entrada/contribuição** para este layout. Não são fontes independentes de geração de código.

---

# 2. HIERARQUIA CANÔNICA

A hierarquia operacional passa a ser:

**FONTES EXTERNAS → CARTAS/DOCUMENTOS DE ENTRADA → LAYOUT MESTRE → CÓDIGO/WORKFLOWS → EVIDÊNCIAS → VALIDAÇÃO → CONSOLIDAÇÃO**

### 2.1 Regra fundamental

Nenhum código novo deve ser criado diretamente a partir de:

- uma Carta;
- um README;
- uma discussão;
- uma hipótese;
- uma mensagem de chat;
- um documento operacional isolado;
- uma implementação anterior sem reconciliação com este layout.

Esses materiais podem fornecer informação, requisito ou evidência, mas a regra executável deve estar consolidada neste documento antes de gerar ou alterar código.

### 2.2 Regra de precedência

Em caso de divergência entre documentos:

1. este LAYOUT MESTRE;
2. evidência factual persistida;
3. documentação oficial externa aplicável;
4. cartas e documentos de entrada;
5. procedimentos derivados;
6. implementação existente.

Uma divergência relevante deve gerar reconciliação versionada antes de ser transformada em código.

---

# 3. CARTAS COMO FONTES DE ENTRADA

As cartas existentes permanecem preservadas por rastreabilidade histórica, mas deixam de funcionar como autoridades paralelas.

### 3.1 Fontes atualmente incorporadas

- `docs/CARTA_DE_CONFIANCA_DOS_DADOS.md`
- `docs/CARTA_MAGNA_GOVERNANCA_B3.md`
- `docs/CARTA_DE_GARANTIAS_DO_PROJETO_B3.md`
- `docs/MODELO_GOVERNANCA_PARA_PROJETOS.md`
- `docs/PLANO_MESTRE_DE_EXECUCAO.md`
- contratos técnicos específicos já existentes, quando suas regras forem incorporadas a este layout.

### 3.2 Regra de alimentação

Uma Carta pode:

- propor uma regra;
- registrar uma garantia;
- registrar uma decisão histórica;
- fornecer contexto;
- apontar uma obrigação.

Mas **não pode, isoladamente, criar uma nova regra executável de código**.

A nova regra deve ser:

**proposta → reconciliada → incorporada neste layout → versionada → então implementada.**

### 3.3 Regra contra divergência

Se uma Carta contiver regra diferente deste layout:

**LAYOUT MESTRE prevalece operacionalmente.**

A divergência deve ser registrada para reconciliação e não deve gerar alteração automática de código.

---

# 4. PRINCÍPIOS OBRIGATÓRIOS

Todo código, workflow, script e pipeline deve obedecer:

1. evidência;
2. proveniência;
3. rastreabilidade;
4. reprodutibilidade;
5. integridade;
6. transparência;
7. separação entre fato, transformação, inferência e hipótese;
8. versionamento;
9. automação governada;
10. fail-closed;
11. não invenção;
12. não retrocertificação;
13. preservação de incidentes;
14. correção na fase de origem;
15. execução monotônica;
16. dependências direcionais;
17. idempotência quando aplicável;
18. ausência de reexecução por ruído documental.

---

# 5. CLASSIFICAÇÃO EPISTEMOLÓGICA

Toda decisão relevante deve distinguir:

**FATO** — observado diretamente na fonte ou evidência.

**TRANSFORMAÇÃO** — resultado determinístico de regra documentada.

**INFERÊNCIA** — interpretação derivada dos dados.

**HIPÓTESE** — explicação ainda não comprovada.

**EXCEÇÃO** — comportamento histórico ou operacional conhecido e formalmente classificado.

Uma hipótese nunca pode ser convertida silenciosamente em regra de rejeição.

---

# 6. ESTADOS DOS ARTEFATOS

Os estados devem ser explícitos.

### 6.1 Estados de dados

- EXISTE
- ÍNTEGRO
- PARSED
- NORMALIZED
- VALIDADO
- VALIDADO_COM_EXCECAO
- CERTIFICADO
- FECHADO
- TRANSIÇÃO_AUTORIZADA
- NÃO_VALIDADO
- BLOQUEADO
- REJEITADO

### 6.2 Regra

A existência física de um arquivo não prova sua integridade.

Integridade não prova semântica.

Validação não equivale a certificação.

Certificação não equivale a fechamento.

Fechamento de um período não certifica outro período.

---

# 7. RASTREABILIDADE MÍNIMA

Todo artefato derivado deve permitir identificar, quando aplicável:

1. fonte;
2. arquivo RAW;
3. período;
4. data de aquisição;
5. layout;
6. parser;
7. normalização;
8. testes;
9. evidência;
10. commit;
11. workflow/run;
12. correções;
13. rejeições;
14. exceções;
15. decisão de promoção.

---

# 8. PRESERVAÇÃO DO RAW

RAW é imutável semanticamente.

É proibido:

- alterar RAW silenciosamente;
- substituir arquivo bruto sem nova evidência;
- corrigir RAW para satisfazer parser;
- apagar histórico de versões;
- mascarar divergência de checksum.

Correções pertencem às camadas derivadas e devem manter vínculo com a origem.

---

# 9. LOCALIZAÇÃO CANÔNICA COTAHIST

Para COTAHIST anual:

- RAW: `dados/cotahist/raw/anual/COTAHIST_A<AAAA>.ZIP`
- manifesto: `dados/cotahist/manifests/COTAHIST_A<AAAA>.json`
- checksum: `dados/cotahist/checksums/COTAHIST_A<AAAA>.ZIP.sha256`
- normalizado: `dados/cotahist/normalized/anual/COTAHIST_A<AAAA>.csv`
- qualidade: `dados/cotahist/quality/`
- certificação: `dados/cotahist/certificacao/`

**Regra:** localizar primeiro no caminho canônico; somente depois investigar aquisição ou ausência.

Uma busca ampla que falhe não constitui prova de ausência.

---

# 10. CADEIA CANÔNICA DE PROCESSAMENTO

A cadeia padrão é:

**FONTE → AQUISIÇÃO → RAW → INTEGRIDADE → PARSING → NORMALIZAÇÃO → MANIFESTO/CHECKSUM → SEMÂNTICA → IDENTIDADE → CALENDÁRIO/CONSISTÊNCIA → GATE → PRÉ-RELEASE → VALIDAÇÃO INDEPENDENTE → CERTIFICAÇÃO → FECHAMENTO → TRANSIÇÃO**

Cada etapa possui responsabilidade própria.

---

# 11. FASES COTAHIST

## FASE00 — GOVERNANÇA / PRÉ-CONDIÇÕES

Responsabilidade:

- definir escopo;
- confirmar contratos;
- confirmar fontes;
- confirmar entradas;
- autorizar execução.

Não executa validações posteriores.

**Saída:** pré-condições autorizadas.

## FASE01 — AQUISIÇÃO / RAW

Responsabilidade:

- adquirir;
- preservar;
- registrar origem;
- registrar período;
- registrar checksum;
- registrar evidência de aquisição.

Não interpreta semanticamente o conteúdo.

**Saída:** RAW.

## FASE02 — INTEGRIDADE DA FONTE

Responsabilidade:

- verificar existência;
- ZIP;
- tamanho;
- checksum;
- estrutura física;
- presença de membro esperado.

Não faz parsing semântico.

**Saída:** evidência de integridade.

## FASE03 — PARSING

Responsabilidade:

- interpretar layout;
- verificar tamanho de registro;
- identificar tipos;
- validar datas estruturais;
- produzir representação estruturada.

Não define identidade normativa.

**Saída:** evidência de parsing.

## FASE04 — NORMALIZAÇÃO

Responsabilidade:

- converter para esquema canônico;
- aplicar transformações determinísticas;
- preservar rastreabilidade;
- produzir dataset normalizado.

Não decide identidade posterior.

**Saída:** NORMALIZED.

## FASE05 — MANIFESTO / CHECKSUM

Responsabilidade:

- fechar hashes;
- registrar metadados;
- confirmar coerência entre artefatos.

Não executa semântica posterior.

**Saída:** manifesto/checksum.

## FASE06 — SEMÂNTICA / INVARIANTES

Responsabilidade:

- verificar invariantes;
- comparar RAW × NORMALIZED;
- validar campos e domínios;
- testar amostras;
- registrar exceções;
- quantificar duplicidades diagnósticas.

**Regra crítica:** FASE06 não decide unicidade/cardinalidade da chave lógica.

Uma chave candidata duplicada é observação diagnóstica até a FASE07.

**Saída:** evidência semântica → FASE07.

## FASE07 — IDENTIDADE / CHAVES / CARDINALIDADE

Responsabilidade:

- testar candidatos de chave;
- analisar colisões;
- classificar duplicidades;
- testar hipóteses em dados históricos;
- decidir identidade;
- determinar cardinalidade;
- versionar decisão.

Não reescreve FASE06.

**Saída:** contrato de identidade → FASE08.

## FASE08 — SEMÂNTICA AVANÇADA / CALENDÁRIO / CONSISTÊNCIA

Responsabilidade:

- calendário de pregões;
- continuidade;
- coerência temporal;
- consistência entre instrumentos;
- mudanças históricas;
- exceções.

Não redefine identidade.

**Saída:** evidência avançada → GATE.

---

# 12. GATE 06–08

O Gate é uma barreira de promoção, não uma fase técnica.

Consome exclusivamente:

- evidência FASE06;
- evidência FASE07;
- evidência FASE08;
- ano/ciclo;
- commits;
- estado operacional quando disponível;
- contratos vigentes.

Não usa README como fonte operacional.

### 12.1 Promoção

**LIBERADO_PARA_FASE09** somente quando:

`E06_OK AND E07_OK AND E08_OK AND ISOLAMENTO_OK AND SEM_BLOQUEADORES`

### 12.2 Bloqueio

Bloqueia:

- evidência ausente;
- status inválido;
- ano incorreto;
- decisão incompatível;
- campo contratual ausente;
- exceção sem classificação;
- incerteza não resolvida;
- violação de isolamento.

### 12.3 Correção

O Gate nunca corrige uma fase.

Fluxo:

**bloqueio → incidente → correção na origem → nova evidência → novo Gate**

---

# 13. FASE09 — PRÉ-RELEASE

Consolida evidências já produzidas.

Não cria nova semântica.

Não corrige fases anteriores.

**Saída:** LIBERADO_PARA_FASE10 ou BLOQUEADO.

---

# 14. FASE10 — VALIDAÇÃO INDEPENDENTE

Responsabilidade:

- verificar hashes;
- verificar contagens;
- verificar RAW × NORMALIZED;
- repetir testes independentes selecionados;
- verificar contratos de correção;
- detectar divergências.

Não substitui evidências anteriores.

**Saída:** VALIDADO ou BLOQUEADO.

---

# 15. FASE11 — CERTIFICAÇÃO / PROMOÇÃO

Responsabilidade:

- confirmar FASE10;
- registrar hashes;
- registrar exceções;
- atualizar matriz de certificação;
- emitir certificação.

Não refaz fases técnicas silenciosamente.

**Saída:** CERTIFICADO/PROMOVIDO.

---

# 16. FASE12 — FECHAMENTO / TRANSIÇÃO

Responsabilidade:

- confirmar FASE11;
- congelar artefatos;
- registrar hashes finais;
- fechar o período;
- autorizar próximo ciclo.

Não inicia o próximo ciclo dentro da própria FASE12.

**Saída:** FECHADO → TRANSIÇÃO_AUTORIZADA.

---

# 17. REGRA DE ISOLAMENTO E MONOTONICIDADE

As fases são independentes e monotônicas.

Uma fase N:

- não reabre N-1;
- não corrige N-1;
- não executa N+1;
- não substitui evidência anterior;
- somente consome evidência autorizada.

O fluxo permitido é:

**N-1 → N → N+1**

Nunca:

**N+1 → N-1**

nem:

**N → executar responsabilidade de N+1**

---

# 18. REGRA DE CORREÇÃO

O erro é corrigido na fase em que nasceu.

| Origem | Correção |
|---|---|
| FASE00 | FASE00 |
| FASE01 | FASE01 |
| FASE02 | FASE02 |
| FASE03 | FASE03 |
| FASE04 | FASE04 |
| FASE05 | FASE05 |
| FASE06 | FASE06 |
| FASE07 | FASE07 |
| FASE08 | FASE08 |
| FASE09 | FASE09 |
| FASE10 | FASE10 |
| FASE11 | FASE11 |
| FASE12 | FASE12 |

Uma fase posterior pode registrar impacto, mas não pode mascarar a origem.

---

# 19. REGRA DE ENTRADA/PROCESSAMENTO/SAÍDA

Toda tarefa deve possuir:

**ENTRADA → PROCESSAMENTO → EVIDÊNCIA → DECISÃO → SAÍDA**

Não existe:

- salto silencioso;
- promoção por existência;
- retorno automático;
- correção cruzada;
- retrocertificação;
- responsabilidade compartilhada sem contrato.

---

# 20. WORKFLOWS — INDEPENDÊNCIA

Cada workflow deve ser uma unidade operacional independente.

É proibido:

- chamar outro workflow;
- reexecutar outro workflow;
- depender de README;
- depender de alteração genérica em `docs/`;
- ser acionado por artefato posterior sem relação causal;
- usar documentação como gatilho de reprocessamento.

Dependências entre fases são representadas por **evidência autorizada**, não por chamadas entre workflows.

---

# 21. GATILHOS DOS WORKFLOWS

Um workflow pode executar por:

1. entrada autorizada da própria tarefa;
2. alteração do próprio workflow;
3. execução manual controlada;
4. agendamento próprio, quando a tarefa for recorrente.

Não pode executar por:

- README;
- documentação genérica;
- alteração de fase posterior;
- mudança sem relação causal.

---

# 22. RETORNO PADRONIZADO DE TODO WORKFLOW

Todo workflow operacional deve escrever no `GITHUB_STEP_SUMMARY`:

- workflow;
- fase/tarefa;
- ano/ciclo;
- run;
- commit;
- entrada;
- evidência produzida;
- status;
- decisão;
- bloqueadores;
- exceções;
- próxima ação;
- indicação `REEXECUTAR=SIM|NÃO`;
- motivo da decisão de reexecução.

Formato lógico mínimo:

**RESULTADO: FAVORÁVEL | NÃO_FAVORÁVEL | EM_EXECUÇÃO**

**DECISÃO: AVANÇAR | BLOQUEAR | NÃO_REEXECUTAR | INVESTIGAR**

---

# 23. MONITORAMENTO PERMANENTE

O monitor:

`.github/workflows/b3-monitor-execucoes-v1.yml`

deve verificar periodicamente:

- execuções recentes;
- sucesso;
- falha;
- cancelamento;
- timeout;
- execução pendente;
- stale;
- ausência de evidência quando identificável.

O monitor **não reexecuta workflows**.

Ele apenas classifica:

- FAVORÁVEL;
- NÃO_FAVORÁVEL;
- EM_EXECUÇÃO.

---

# 24. REGRA ANTI-REEXECUÇÃO

Antes de reexecutar:

1. localizar run existente;
2. verificar conclusão;
3. verificar evidência;
4. verificar commit;
5. verificar decisão;
6. verificar incidente;
7. verificar alteração real da entrada;
8. verificar correção pendente;
9. verificar alteração normativa aplicável.

Se a entrada não mudou e a evidência continua válida:

**NÃO REEXECUTAR.**

Falha antiga também não autoriza reexecução cega: primeiro identificar a causa.

---

# 25. README

README é artefato de consolidação.

Todos os README do projeto somente podem ser atualizados às:

**23:55 — America/Sao_Paulo**

A rotina deve:

- consumir apenas evidências persistidas;
- ser idempotente;
- não disparar fases;
- não corrigir fases;
- não fechar fases;
- não substituir evidências;
- não criar commits se não houver alteração real.

README não é fonte operacional de decisão.

---

# 26. GERAÇÃO E ALTERAÇÃO DE CÓDIGO

Esta é uma regra central.

### 26.1 Fonte única para código

Todo novo:

- Python;
- Shell;
- YAML;
- workflow;
- script;
- validador;
- parser;
- normalizador;
- monitor;
- automação;
- estrutura de evidência;

deve ser derivado do **LAYOUT MESTRE**.

### 26.2 Processo obrigatório

**REQUISITO → RECONCILIAÇÃO → LAYOUT MESTRE → ESPECIFICAÇÃO DA TAREFA → CÓDIGO → TESTE → EVIDÊNCIA → COMMIT**

### 26.3 Proibição

É proibido gerar código diretamente de:

- Carta isolada;
- README;
- conversa;
- hipótese;
- código legado não reconciliado;
- resultado de workflow sem decisão normativa.

### 26.4 Alteração de regra

Quando uma nova necessidade surgir:

**necessidade → proposta → impacto → reconciliação → atualização deste layout → implementação → validação**

A ordem não pode ser invertida.

---

# 27. CONTRATO MÍNIMO PARA NOVO CÓDIGO

Antes de criar código, deve existir no layout ou em uma especificação derivada dele:

1. objetivo;
2. fase/tarefa;
3. entradas;
4. saídas;
5. evidências;
6. critérios de sucesso;
7. critérios de bloqueio;
8. responsabilidade;
9. não-responsabilidades;
10. gatilho autorizado;
11. regra de idempotência;
12. regra de reexecução;
13. estado esperado;
14. caminho dos artefatos;
15. estratégia de auditoria.

Sem isso, o código não deve ser promovido ao repositório.

---

# 28. CONTRATO DE EVIDÊNCIA

Toda execução relevante deve produzir evidência persistida quando a tarefa exigir.

A evidência deve permitir responder:

- o que foi executado;
- em qual ciclo;
- com qual entrada;
- por qual versão;
- quando;
- qual resultado;
- quais testes;
- quais exceções;
- qual decisão;
- qual commit;
- qual próximo passo.

---

# 29. INCIDENTES

Classes mínimas:

1. incidente de fonte;
2. incidente de RAW;
3. incidente de parsing;
4. incidente de normalização;
5. incidente semântico;
6. incidente de identidade;
7. incidente de calendário;
8. incidente de gate;
9. incidente de workflow;
10. incidente de publicação;
11. incidente de governança.

Uma falha de workflow não deve ser classificada automaticamente como corrupção do dado.

Incidentes relevantes permanecem preservados.

---

# 30. CONTRATO DE CORREÇÃO

Os indicadores:

- `correction_required`;
- `correction_applied`;
- `correction_contract_valid`;

devem representar o estado real.

Quando não houver correção:

- `correction_required=false`;
- `correction_applied=false`;
- `correction_contract_valid=true`.

É proibido alterar indicadores apenas para satisfazer um gate.

---

# 31. FAIL-CLOSED

Uma condição crítica ausente, inválida, desconhecida ou contraditória bloqueia promoção.

Nunca promover por:

- inferência;
- aparência;
- existência de arquivo;
- execução parcial;
- sucesso de fase posterior;
- README atualizado;
- ausência de erro visível.

---

# 32. DUPLICIDADES E CHAVES

Duplicidade não é automaticamente corrupção.

Antes de deduplicar:

1. registrar ocorrência;
2. quantificar;
3. classificar;
4. testar hipótese de identidade;
5. verificar layout;
6. verificar período;
7. decidir na fase responsável.

FASE06 registra observação.

FASE07 decide identidade/cardinalidade.

---

# 33. NÃO INVENÇÃO

É proibido:

- inventar registros;
- completar preços silenciosamente;
- inventar volume;
- criar negócios inexistentes;
- converter hipótese em dado;
- corrigir sem preservar original;
- remover outlier sem regra;
- apagar falha relevante.

Dados imputados devem ser explicitamente classificados como derivados/imputados.

---

# 34. REPRODUTIBILIDADE

Mesma entrada + mesmo código + mesmos parâmetros + mesmas regras devem produzir resultado equivalente.

Divergência inesperada exige investigação de determinismo.

---

# 35. VERSIONAMENTO

Toda alteração relevante de:

- código;
- parser;
- schema;
- layout;
- semântica;
- regra;
- workflow;
- validação;
- fonte;
- calendário;

deve possuir commit identificável.

O histórico do Git faz parte da auditoria.

---

# 36. REGRA PARA DADOS QUANTITATIVOS

Antes de usar dados em backtest, estudo ou modelo:

- cobertura temporal;
- sobrevivência;
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
- qualidade do volume;
- consistência de preços.

Uma série longa não é automaticamente adequada para backtest.

---

# 37. AUDITORIA

Uma auditoria deve separar:

**fato → evidência → regra → execução → resultado → decisão**

Não deve substituir evidência por narrativa.

---

# 38. ESTADOS DE PROMOÇÃO

### FAVORÁVEL

Execução concluída e contrato satisfeito.

### NÃO_FAVORÁVEL

Falha, bloqueio, cancelamento, timeout ou evidência incompatível.

### EM_EXECUÇÃO

Ainda não existe resultado final.

O estado do workflow não substitui o estado da evidência.

---

# 39. ROADMAP CANÔNICO ATUAL

### 1995

FASE14 — PRESENÇA/INTEGRIDADE — **VALIDADA**  
→ FASE03 — PARSING — **VALIDADA**  
→ FASE04 — NORMALIZAÇÃO — **VALIDADA**  
→ FASE05 — MANIFESTO/CHECKSUM — **VALIDADA**  
→ FASE06 — SEMÂNTICA — **VALIDADA**  
→ **FASE07 — IDENTIDADE/CHAVES/CARDINALIDADE — PRÓXIMA**  
→ FASE08  
→ GATE 06–08  
→ FASE09  
→ FASE10  
→ FASE11  
→ FASE12  
→ 1996

1986 permanece em trilha histórica própria e não deve contaminar o ciclo operacional de 1995.

---

# 40. REGRA DE TRANSIÇÃO ENTRE ANOS

Somente FASE12 concluída autoriza transição.

A transição:

- não certifica o próximo ano;
- não executa o próximo ano;
- não modifica o ano anterior;
- somente autoriza o início do próximo ciclo.

---

# 41. CONTROLE DAS CARTAS APÓS A CONSOLIDAÇÃO

As cartas passam a possuir natureza de:

**DOCUMENTOS DE ENTRADA / HISTÓRICO DE GOVERNANÇA**

e não de especificações independentes de código.

Quando uma Carta for atualizada, a alteração deve ser avaliada contra este layout.

Se produzir nova regra operacional:

**Carta → proposta → reconciliação → atualização do Layout → código**

Nunca:

**Carta → código**

---

# 42. CONTROLE DE DOCUMENTOS DERIVADOS

Documentos operacionais específicos podem continuar existindo para:

- facilitar leitura;
- registrar contratos;
- preservar histórico;
- documentar uma fase;
- explicar uma implementação.

Mas suas regras executáveis devem ser compatíveis com este layout.

Em caso de divergência, este layout deve ser atualizado ou a regra derivada deve ser corrigida antes de nova implementação.

---

# 43. TESTE DE CONFORMIDADE DE QUALQUER WORKFLOW

Antes de considerar um workflow conforme, verificar:

- [ ] responsabilidade única;
- [ ] entrada definida;
- [ ] saída definida;
- [ ] evidência definida;
- [ ] gatilho autorizado;
- [ ] sem dependência circular;
- [ ] sem chamada a outro workflow;
- [ ] sem reexecução automática de outro workflow;
- [ ] sem README como entrada operacional;
- [ ] sem docs genéricos como gatilho;
- [ ] GITHUB_STEP_SUMMARY;
- [ ] decisão explícita;
- [ ] bloqueadores explícitos;
- [ ] regra de reexecução;
- [ ] commit rastreável;
- [ ] idempotência quando aplicável;
- [ ] fail-closed quando aplicável.

---

# 44. TESTE DE CONFORMIDADE DE QUALQUER NOVO CÓDIGO

- [ ] regra existe neste layout;
- [ ] fase/tarefa definida;
- [ ] entrada definida;
- [ ] saída definida;
- [ ] evidência definida;
- [ ] caminho definido;
- [ ] critérios de sucesso definidos;
- [ ] critérios de bloqueio definidos;
- [ ] regra de reexecução definida;
- [ ] responsabilidade isolada;
- [ ] testes previstos;
- [ ] auditoria prevista;
- [ ] commit previsto.

Se qualquer item crítico estiver ausente, o código não deve ser considerado pronto.

---

# 45. REGRA DE OURO

> **Uma única regra operacional deve possuir uma única fonte normativa canônica.**

> **As cartas alimentam o Layout. O Layout governa o código. O código produz evidência. A evidência permite validação. A validação permite promoção.**

> **Nenhum código deve nascer diretamente de uma Carta, README, conversa ou hipótese.**

---

# 46. PRINCÍPIO FINAL

**LAYOUT MESTRE → CÓDIGO → EVIDÊNCIA → VALIDAÇÃO → DECISÃO**

Esse é o fluxo oficial do repositório B3.

Qualquer processo futuro deve ser enquadrado neste fluxo antes de ser implementado.

---

## Controle de versão

| Versão | Data | Alteração | Status |
|---|---|---|---|
| 1.0.0 | 2026-10-01 | Consolidação das cartas, contratos, matriz operacional, governança de workflows, monitoramento, README, gates, fases e regra única de geração de código. | VIGENTE |


## 40. AUDITORIA SEMÂNTICA DOS WORKFLOWS — REGRA VIGENTE

A auditoria de workflows deve distinguir conformidade funcional de observabilidade.

O auditor canônico deve verificar, além da existência do trigger e do Layout Mestre:

1. responsabilidade do workflow;
2. causalidade do trigger;
3. isolamento;
4. dependências direcionais;
5. ausência de gatilho explícito de fase posterior;
6. permissões compatíveis com a operação real;
7. persistência da evidência;
8. existência de decisão/status explícito;
9. sinais de idempotência/deduplicação quando aplicável;
10. regra especial do README;
11. comportamento somente-leitura do monitor;
12. ausência de reexecução de outro workflow.

A ausência isolada de `GITHUB_STEP_SUMMARY` é classificada como **observabilidade** e não deve ser interpretada automaticamente como falha funcional dos dados.

O auditor é exclusivamente diagnóstico:

**auditar → classificar → evidenciar → decidir correção**

Nunca:

**auditar → alterar automaticamente → reexecutar → promover**

### 40.1 Severidade

- **CRITICA/ALTA:** potencial bloqueador funcional ou de governança.
- **MEDIA:** alerta que exige revisão.
- **BAIXA:** observabilidade ou melhoria recomendada.

Workflow histórico não deve ser reaberto somente porque a auditoria atual encontrou uma divergência estrutural. A correção, quando necessária, deve ocorrer na origem e respeitar o contrato de fechamento histórico.

### 40.2 Auditor canônico

O auditor vigente é:

`scripts/governanca/auditar_workflows_b3.py`

A saída é:

`docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.json`

e

`docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.md`

A implementação deve permanecer alinhada a este Layout Mestre.
