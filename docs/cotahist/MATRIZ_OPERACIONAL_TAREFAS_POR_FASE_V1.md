# COTAHIST — MATRIZ OPERACIONAL DE TAREFAS POR FASE

**Versão:** 1.0  
**Data:** 2026-10-01  
**Status:** VIGENTE  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Este documento transforma a sequência canônica do COTAHIST em uma matriz operacional fechada.

Cada fase possui:

- objetivo;
- tarefas obrigatórias;
- entrada autorizada;
- saída/evidência;
- critério de conclusão;
- responsabilidade que não pode ser antecipada;
- dependência para a fase seguinte.

A regra principal é:

> **Uma tarefa pertence a uma única fase. Depois de concluída e certificada, ela não deve ser executada novamente por uma fase posterior.**

Se uma tarefa estiver incorreta, a correção pertence à fase que originou a tarefa.

---

## 2. Ordem canônica de execução

**FASE00 → FASE01 → FASE02 → FASE03 → FASE04 → FASE05 → FASE06 → FASE07 → FASE08 → GATE 06–08 → FASE09 → FASE10 → FASE11 → FASE12 → PRÓXIMO ANO**

### Regra de promoção

Nenhuma fase pode avançar apenas pela existência de arquivos.

A promoção exige:

**pré-condição → execução → evidência → validação → gate → próxima fase**

---

# 3. FASE00 — GOVERNANÇA / PRÉ-CONDIÇÕES

## Objetivo

Definir se o ciclo pode começar e sob quais regras.

## Tarefas

1. Identificar o ano/período alvo.
2. Definir o escopo do ciclo.
3. Identificar a fonte oficial aplicável.
4. Identificar o layout/documentação aplicável.
5. Verificar regras de governança vigentes.
6. Verificar incidentes e correções anteriores relevantes.
7. Verificar o caminho canônico dos artefatos.
8. Verificar se o ano já possui evidências.
9. Definir as pré-condições da FASE01.
10. Registrar exceções conhecidas antes da execução.

## Não pertence à FASE00

- aquisição do RAW;
- parsing;
- normalização;
- validação semântica;
- definição de chave lógica;
- certificação.

## Saída

**Evidência de governança e autorização para FASE01.**

---

# 4. FASE01 — AQUISIÇÃO / PRESERVAÇÃO DO RAW

## Objetivo

Obter ou confirmar a existência do arquivo-fonte e preservar sua imutabilidade.

## Tarefas

1. Procurar primeiro o arquivo no caminho canônico.
2. Se já existir, não baixar novamente sem justificativa.
3. Registrar nome do arquivo.
4. Registrar tamanho.
5. Registrar origem.
6. Registrar data/hora de aquisição, quando disponível.
7. Calcular SHA-256.
8. Preservar o arquivo RAW.
9. Criar/atualizar manifesto de aquisição.
10. Registrar qualquer falha de aquisição.

## Não pertence à FASE01

- interpretar campos;
- corrigir registros;
- normalizar;
- decidir chave;
- certificar dados.

## Saída

**RAW preservado + evidência de aquisição/existência.**

---

# 5. FASE02 — INTEGRIDADE DA FONTE

## Objetivo

Provar que o arquivo RAW está estruturalmente íntegro como fonte de dados.

## Tarefas

1. Confirmar SHA-256.
2. Confirmar manifesto.
3. Confirmar integridade do ZIP, quando aplicável.
4. Confirmar quantidade de membros do ZIP.
5. Identificar o membro de dados.
6. Confirmar tamanho/estrutura esperada.
7. Confirmar registros de controle conhecidos.
8. Confirmar comprimento físico dos registros.
9. Confirmar ausência de corrupção estrutural detectável.
10. Registrar a decisão de integridade da fonte.

## Não pertence à FASE02

- interpretar semanticamente campos;
- decidir significado de códigos;
- definir chave lógica;
- normalizar;
- validar calendário de negociação.

## Saída

**Fonte íntegra → autorização para FASE03.**

---

# 6. FASE03 — PARSING

## Objetivo

Transformar os registros físicos da fonte em registros estruturados sem alterar seu conteúdo semântico.

## Tarefas

1. Ler o arquivo RAW.
2. Identificar tipos de registro.
3. Respeitar offsets e larguras do layout.
4. Separar header, cotações e trailer.
5. Validar comprimento dos registros.
6. Extrair os campos conforme o layout.
7. Contar registros por tipo.
8. Validar datas em nível estrutural.
9. Registrar primeiro/último registro de cotação.
10. Registrar erros de parsing.
11. Produzir evidência reproduzível do parsing.

## Não pertence à FASE03

- definir significado econômico de códigos;
- escolher chave lógica;
- resolver cardinalidade;
- alterar valores;
- decidir calendário definitivo.

## Saída

**Registros estruturados + evidência de parsing.**

---

# 7. FASE04 — NORMALIZAÇÃO

## Objetivo

Gerar o dataset normalizado canônico a partir do parsing, preservando rastreabilidade com a fonte.

## Tarefas

1. Aplicar parser aprovado.
2. Produzir estrutura tabular canônica.
3. Padronizar representação dos campos.
4. Converter tipos conforme contrato.
5. Preservar os valores de origem.
6. Gerar CSV normalizado.
7. Calcular SHA-256 do normalizado.
8. Registrar quantidade de linhas.
9. Registrar quantidade de campos.
10. Validar datas estruturais.
11. Validar datas fora do ano.
12. Confirmar reconciliação determinística RAW → NORMALIZED.
13. Produzir manifesto de qualidade do normalizado.

## Não pertence à FASE04

- escolher chave lógica;
- decidir unicidade;
- resolver duplicidades semanticamente;
- certificar o ano.

## Saída

**NORMALIZED + manifesto de qualidade.**

---

# 8. FASE05 — MANIFESTO / CHECKSUM

## Objetivo

Fechar a identidade técnica dos artefatos produzidos até a normalização.

## Tarefas

1. Confirmar manifesto RAW.
2. Confirmar checksum RAW.
3. Confirmar SHA-256 do normalizado.
4. Confirmar manifesto do normalizado.
5. Comparar hashes com os artefatos efetivamente presentes.
6. Confirmar coerência entre manifestos.
7. Registrar versões de parser.
8. Registrar contagens.
9. Registrar status dos artefatos.
10. Autorizar FASE06.

## Não pertence à FASE05

- análise semântica;
- escolha de chave;
- análise de calendário;
- certificação.

## Saída

**Pacote técnico fechado para auditoria semântica.**

---

# 9. FASE06 — SEMÂNTICA / INVARIANTES

## Objetivo

Verificar se os campos e invariantes básicos possuem comportamento compatível com o contrato semântico conhecido.

## Tarefas

1. Consumir o RAW e o NORMALIZED já autorizados.
2. Confirmar presença dos campos necessários.
3. Verificar tipos numéricos.
4. Verificar OHLC.
5. Verificar quantidade.
6. Verificar volume.
7. Verificar códigos relevantes como TPMERC e CODBDI.
8. Verificar datas e invariantes básicos.
9. Executar amostras históricas.
10. Comparar amostras RAW × NORMALIZED.
11. Quantificar anomalias.
12. Quantificar duplicidades de chaves candidatas apenas como diagnóstico.
13. Separar erro comprovado de hipótese.
14. Registrar exceções sem convertê-las automaticamente em reprovação.
15. Produzir evidência semântica.

## Regra crítica

**FASE06 NÃO decide unicidade/cardinalidade da chave lógica.**

Uma chave candidata duplicada é observação diagnóstica até que a FASE07 determine sua validade.

## Não pertence à FASE06

- definição normativa da chave;
- decisão de cardinalidade;
- resolução definitiva de identidade;
- calendário completo;
- pré-release;
- certificação.

## Saída

**Evidência semântica → autorização para FASE07.**

---

# 10. FASE07 — IDENTIDADE / CHAVES / CARDINALIDADE

## Objetivo

Determinar como um registro é identificado dentro do universo histórico analisado.

## Tarefas

1. Consumir a evidência validada da FASE06.
2. Consultar o layout oficial aplicável.
3. Inventariar campos candidatos à identidade.
4. Avaliar combinações de campos.
5. Analisar duplicidades observadas na FASE06.
6. Classificar colisões.
7. Verificar se duplicidades são:
   - instrumentos diferentes;
   - mercados diferentes;
   - eventos diferentes;
   - registros legitimamente múltiplos;
   - erro de parsing;
   - outra condição documentada.
8. Comparar hipóteses com amostras históricas.
9. Testar a hipótese de chave em dados reais.
10. Determinar cardinalidade.
11. Registrar campos obrigatórios da identidade.
12. Registrar campos que não fazem parte da chave.
13. Registrar limitações e exceções.
14. Emitir decisão normativa da identidade.
15. Versionar o contrato de identidade.

## Regra crítica

**FASE07 pode consumir a FASE06, mas não pode reescrever sua evidência.**

Se a FASE07 descobrir que um resultado anterior está incorreto, deve registrar impacto e encaminhar correção para a fase de origem.

## Não pertence à FASE07

- reescrever semântica da FASE06;
- alterar o RAW;
- normalizar novamente;
- definir calendário completo;
- certificar o ano.

## Saída

**Contrato de identidade/chave/cardinalidade → autorização para FASE08.**

---

# 11. FASE08 — SEMÂNTICA AVANÇADA / CALENDÁRIO / CONSISTÊNCIA

## Objetivo

Verificar coerência histórica e temporal utilizando a identidade já definida.

## Tarefas

1. Consumir identidade da FASE07.
2. Validar calendário de pregões.
3. Verificar continuidade temporal.
4. Verificar datas de início/fim.
5. Detectar registros fora do período.
6. Verificar coerência entre instrumentos e datas.
7. Verificar consistência entre campos relacionados.
8. Verificar mudanças históricas de layout/códigos quando aplicável.
9. Classificar exceções históricas.
10. Executar reconciliações adicionais.
11. Produzir amostras de controle.
12. Registrar inconsistências.
13. Confirmar se as exceções são aceitáveis, documentadas ou bloqueadoras.

## Não pertence à FASE08

- redefinir chave da FASE07;
- alterar RAW;
- corrigir normalização silenciosamente;
- executar pré-release;
- certificar.

## Saída

**Evidência de consistência histórica/temporal → GATE 06–08.**

---

# 12. GATE 06–08 — PROMOÇÃO TÉCNICA

## Objetivo

Confirmar que as três fases técnicas estão concluídas antes do pré-release.

## Tarefas

1. Ler FASE06.
2. Ler FASE07.
3. Ler FASE08.
4. Confirmar status permitidos.
5. Confirmar evidências existentes.
6. Confirmar ausência de bloqueadores.
7. Confirmar que nenhuma fase está sendo executada dentro de outra.
8. Liberar ou bloquear FASE09.

## Não pertence ao GATE

- corrigir qualquer fase;
- executar nova análise técnica;
- substituir evidência.

## Saída

**LIBERADO/BLOQUEADO PARA FASE09.**

---

# 13. FASE09 — PRÉ-RELEASE

## Objetivo

Consolidar todas as evidências necessárias antes da validação independente.

## Tarefas

1. Confirmar FASE00–08.
2. Confirmar presença de RAW.
3. Confirmar normalizado.
4. Confirmar manifestos.
5. Confirmar checksums.
6. Confirmar evidências técnicas.
7. Confirmar exceções.
8. Confirmar ausência de lacunas bloqueadoras.
9. Produzir checklist pré-release.
10. Emitir decisão LIBERADO_PARA_FASE10 ou BLOQUEADO.

## Não pertence à FASE09

- corrigir fases anteriores;
- criar nova regra semântica;
- alterar identidade;
- certificar.

## Saída

**LIBERADO_PARA_FASE10.**

---

# 14. FASE10 — VALIDAÇÃO INDEPENDENTE

## Objetivo

Executar uma validação independente do pacote que será certificado.

## Tarefas

1. Ler as evidências anteriores.
2. Verificar hashes.
3. Verificar contagens.
4. Verificar coerência RAW × NORMALIZED.
5. Reexecutar testes independentes selecionados.
6. Verificar critérios de release.
7. Confirmar contratos de correção.
8. Detectar divergências.
9. Registrar evidências independentes.
10. Emitir VALIDADO ou BLOQUEADO.

## Regra crítica

A FASE10 é um **gate independente**.

Ela não substitui as fases anteriores nem pode corrigir seus artefatos silenciosamente.

## Saída

**VALIDADO → FASE11.**

---

# 15. FASE11 — CERTIFICAÇÃO / PROMOÇÃO

## Objetivo

Transformar o pacote validado em estado formalmente certificado.

## Tarefas

1. Confirmar FASE10.
2. Confirmar evidências anteriores.
3. Confirmar versão dos artefatos.
4. Confirmar status de qualidade.
5. Registrar exceções certificadas.
6. Registrar hashes finais.
7. Atualizar matriz de certificação.
8. Emitir certificado do ano.
9. Registrar estado de promoção.

## Não pertence à FASE11

- refazer parsing;
- refazer normalização;
- redefinir identidade;
- corrigir semântica;
- executar FASE12 dentro da certificação.

## Saída

**ANO CERTIFICADO / PROMOVIDO.**

---

# 16. FASE12 — FECHAMENTO / TRANSIÇÃO

## Objetivo

Encerrar formalmente o ano e autorizar o próximo ciclo.

## Tarefas

1. Confirmar certificação da FASE11.
2. Congelar os artefatos certificados.
3. Registrar hashes finais.
4. Registrar status final do ano.
5. Registrar exceções permanentes.
6. Fechar o ciclo.
7. Registrar data de fechamento.
8. Autorizar o próximo ano.
9. Não iniciar o próximo ano dentro da FASE12.
10. Produzir evidência de transição.

## Não pertence à FASE12

- executar FASE01 do próximo ano;
- alterar fases anteriores;
- certificar o próximo ano.

## Saída

**ANO FECHADO → PRÓXIMO ANO AUTORIZADO.**

---

# 17. Regra de correção

Quando ocorrer um erro:

| Onde o erro nasceu | Onde corrigir |
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

**Uma fase posterior nunca corrige uma fase anterior.**

Uma fase posterior pode apenas registrar:

**impacto identificado → evidência preservada → correção encaminhada à fase de origem.**

---

# 18. Regra de entrada e saída

Cada fase deve possuir exatamente:

**ENTRADA → PROCESSAMENTO → EVIDÊNCIA → DECISÃO → SAÍDA**

A saída de uma fase é a entrada autorizada da seguinte.

Não existe:

- salto silencioso;
- retorno automático;
- execução antecipada;
- responsabilidade compartilhada entre fases;
- correção cruzada;
- retrocertificação silenciosa.

---

# 19. Regra anti-repetição

Antes de iniciar qualquer fase:

1. verificar se a fase já possui evidência;
2. verificar o status da evidência;
3. verificar o commit que a produziu;
4. verificar se existe incidente aberto;
5. verificar se existe correção pendente da própria fase;
6. verificar se a fase seguinte já consumiu a evidência;
7. somente então decidir EXECUTAR, VALIDAR ou NÃO EXECUTAR.

Se a fase estiver **CONCLUÍDA e válida**, não deve ser executada novamente apenas porque:

- README mudou;
- documentação mudou;
- outra fase foi criada;
- outra fase foi concluída;
- layout visual foi reorganizado;
- uma fase posterior foi auditada.

---

# 20. Regra de gatilhos dos workflows

Cada workflow deve reagir somente a:

1. suas entradas autorizadas;
2. seu próprio arquivo;
3. execução manual controlada.

É proibido usar alterações genéricas de:

- README;
- docs inteiras;
- artefatos de fases posteriores;
- arquivos sem relação causal com a fase;

como gatilho para reexecutar uma fase já concluída.

---

# 21. Matriz resumida

| Ordem | Fase | Função principal | Entrega |
|---:|---|---|---|
| 00 | Governança | autorizar e enquadrar | pré-condições |
| 01 | Aquisição | preservar fonte | RAW |
| 02 | Integridade | provar integridade física | evidência de fonte |
| 03 | Parsing | estruturar registros | parsed/evidência |
| 04 | Normalização | criar dataset canônico | NORMALIZED |
| 05 | Manifesto | fechar identidade técnica | manifestos/checksums |
| 06 | Semântica | validar invariantes | evidência semântica |
| 07 | Identidade | definir chave/cardinalidade | contrato de identidade |
| 08 | Consistência | validar calendário/histórico | evidência avançada |
| Gate | 06–08 | promover tecnicamente | liberação |
| 09 | Pré-release | consolidar pacote | release candidate |
| 10 | Independente | testar o release | validação |
| 11 | Certificação | certificar/promover | certificado |
| 12 | Fechamento | congelar e transicionar | ano fechado |

---

# 22. Regra-mestra

> **A fase deve terminar todo o trabalho que pertence à sua responsabilidade antes de entregar o controle à fase seguinte.**

> **A fase seguinte somente consome a evidência da fase anterior; não volta para executá-la, corrigi-la ou substituí-la.**

> **Se uma decisão ainda pertence a uma fase posterior, ela não deve ser antecipada para acelerar a fase atual.**

---

## 23. Roadmap operacional após este catálogo

**1995**

FASE14 — PRESENÇA/INTEGRIDADE  
→ FASE03 — PARSING  
→ FASE04 — NORMALIZAÇÃO  
→ FASE05 — MANIFESTO/CHECKSUM  
→ **FASE06 — SEMÂNTICA: CONCLUÍDA**  
→ **FASE07 — IDENTIDADE/CHAVES/CARDINALIDADE: PRÓXIMA**  
→ FASE08  
→ GATE 06–08  
→ FASE09  
→ FASE10  
→ FASE11  
→ FASE12  
→ **1996**

1986 permanece em trilha histórica própria e não deve ser misturado ao ciclo operacional de 1995.

## 24. Estado

Este documento é o catálogo operacional de referência para novas execuções COTAHIST.

Qualquer novo workflow deve ser comparado a esta matriz antes de ser criado ou alterado.


---

# 25. REGRA ESPECÍFICA — ATUALIZAÇÃO DE README

A partir de 2026-10-01, **todos os arquivos README do projeto B3 somente podem ser atualizados às 23:55, horário de Brasília (America/Sao_Paulo)**.

Durante a execução normal das fases:

- não atualizar README;
- não usar README como mecanismo de sincronização intermediária;
- não disparar fases por alteração de README;
- não inserir resultados parciais no README;
- não alterar README para registrar uma correção antes da conclusão da respectiva fase.

O README é um **artefato de consolidação**, não um artefato operacional de execução.

## Ordem obrigatória de consolidação

Durante uma fase, a ordem é:

**execução → evidência → correção, se necessária → governança/cartas, quando aplicável → validação → consolidação no README somente às 23:55.**

A atualização do README deve refletir somente estados já persistidos e verificáveis no repositório.

## Regra de horário

O horário oficial é:

**23:55 — America/Sao_Paulo (Brasília)**

A automação deve tratar o fuso explicitamente e não depender do fuso padrão do runner do GitHub Actions.

## Regra de conteúdo

O README das 23:55 deve ser produzido a partir das evidências efetivamente existentes no repositório naquele momento.

É proibido utilizar o README para:

- criar uma evidência que ainda não existe;
- antecipar uma fase;
- fechar uma fase;
- corrigir retroativamente outra fase;
- substituir um manifesto;
- substituir uma certificação;
- mascarar falha de workflow.

## Regra de idempotência

A rotina das 23:55 deve ser idempotente:

- se não houver alteração real, não criar commit desnecessário;
- se houver alteração, produzir um único commit de consolidação;
- preservar o histórico e os hashes das evidências que fundamentaram o README.


# 26. CONTRATO EXECUTÁVEL — GATE 06–08

A partir de 2026-10-01, o GATE 06–08 passa a possuir contrato executável próprio em 'docs/cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md'.

O Gate é uma barreira de promoção, não uma nova fase técnica. Ele somente consome as evidências finais das FASE06, FASE07 e FASE08 e decide 'LIBERADO_PARA_FASE09' ou 'BLOQUEADO_PARA_FASE09'.

### 26.1 Evidências e estados

O Gate deve identificar explicitamente a evidência de cada fase, confirmar ano/ciclo, status, decisão, rastreabilidade e exceções. São estados de promoção: 'VALIDADO' e 'VALIDADO_COM_EXCECAO' quando a exceção for formal e não bloqueadora. Ausência, falha, invalidade ou estado desconhecido bloqueiam.

### 26.2 Responsabilidade

- FASE06: semântica/invariantes; não exige unicidade de chave.
- FASE07: identidade, chave e cardinalidade.
- FASE08: calendário, consistência e semântica avançada.
- GATE: somente verifica os três contratos, isolamento e bloqueadores.
- FASE09: somente consome a decisão do Gate.

### 26.3 Fail-closed

A liberação somente existe quando FASE06, FASE07 e FASE08 estão válidas, o isolamento está comprovado e não há bloqueadores. Qualquer condição ausente, falsa ou indeterminada bloqueia a promoção.

O Gate não corrige fases, não executa análise técnica nova e não usa README como fonte operacional.

### 26.4 Evidência própria

O Gate deve produzir evidência própria e auditável, preferencialmente em:
'dados/cotahist/quality/COTAHIST_<AAAA>_GATE_06_08_PROMOCAO_TECNICA_V1.json'.

A evidência deve registrar fases avaliadas, estados, caminhos das evidências, isolamento, bloqueadores, exceções não bloqueadoras, commits-fonte, timestamp e versão do contrato.

### 26.5 Correção e reexecução

Problemas encontrados pelo Gate são corrigidos na fase de origem. O fluxo é: bloqueio → incidente → correção na origem → nova evidência → novo Gate. README, documentação sem impacto e fases posteriores não podem disparar retroativamente uma fase concluída.
