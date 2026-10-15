# PLANO MESTRE DE EXECUÇÃO — B3

| Campo | Valor |
|---|---|
| **ID** | B3-PLANO-MESTRE-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | PLANO_EXECUCAO |
| **Fase** | Governança, preservação e execução do projeto |
| **Estado** | EM_REVISAO |
| **Versão** | 1.9.0 |
| **SHA-256 (conteúdo canónico)** | 6fa80b0fda2f99dd7071ede80c78b8e81c70630f56532ba4cd2df4292a77e9fc |
| **Commit de referência (versão anterior)** | [aa3007b3a5d2824338011775255779838f8d3933](https://github.com/carlos-andrade/B3/commit/aa3007b3a5d2824338011775255779838f8d3933) |
| **Data de criação** | 2026-09-25 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente de validação formal desta versão normalizada |
| **Origem** | Documento histórico B3 normalizado conforme a norma de cabeçalho GOVERNANCA v1.0.3 |
| **Autoridade superior** | [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); [Layout Mestre B3](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | Histórico Git, versões anteriores e evidências referenciadas no corpo |
| **Escopo** | Planeamento e coordenação das frentes de execução do projeto B3. |
| **Objetivo** | Orientar execução, validação e publicação sem ocultar falhas entre frentes. |
| **Dependências** | Fontes oficiais, contratos de dados, evidências de workflow e políticas aplicáveis |

## 1. Objetivo

Concluir a construção de uma infraestrutura histórica e operacional da B3 baseada em dados rastreáveis, validados, reproduzíveis e auditáveis, sem permitir que um problema histórico localizado bloqueie a evolução do projeto.

## 2. Estratégia geral

O projeto seguirá cinco frentes em paralelo controlado:

1. Dados: ingestão, normalização e validação.
2. Qualidade: auditoria, reconciliação e certificação.
3. Automação: workflows e reprocessamento reproduzível.
4. Produto: datasets, índice e dashboard.
5. Governança: documentação, decisões e critérios de promoção.

A regra é: nenhuma frente pode mascarar uma falha de outra frente.

## 3. Fase imediata — estabilização da ingestão

### 3.1 Fechar o ciclo 2011–2026

Prioridade operacional:

- verificar execução dos workflows;
- eliminar falhas recorrentes;
- confirmar artefatos gerados;
- validar quantidade, estrutura e cobertura temporal;
- registrar resultados;
- deixar o processo reproduzível e automático.

### 3.2 Isolar 1986

O ano de 1986 deixa de ser bloqueador global.

Será mantido em trilha própria enquanto forem investigados:

- layout;
- TPMERC;
- CODBDI;
- semântica dos registros;
- campos numéricos;
- compatibilidade com o padrão histórico.

Se a evidência não for suficiente, 1986 permanecerá NÃO VALIDADO, sem contaminar os anos posteriores.

## 4. Fase de certificação dos dados

Para cada período:

RAW → PARSED → NORMALIZED → VALIDATED

Serão produzidos indicadores objetivos de:

- cobertura;
- registros;
- duplicidades;
- perdas;
- datas;
- instrumentos;
- códigos;
- consistência numérica;
- integridade estrutural;
- reconciliação semântica.

Cada resultado deverá possuir evidência auditável.

## 5. Fase de dataset oficial

Depois da validação:

- definir estrutura canônica;
- consolidar datasets;
- separar dados brutos de dados derivados;
- criar metadados;
- registrar versões;
- criar checksums quando aplicável;
- estabelecer snapshots reproduzíveis.

O dataset publicado deverá indicar claramente seu status de validação.

## 6. Fase de índice e dashboard

O index.html e o dashboard deverão consumir exclusivamente dados existentes no repositório.

Nenhum valor será inventado pela interface.

A interface deverá apresentar, quando aplicável:

- período disponível;
- cobertura;
- status de validação;
- quantidade de registros;
- última atualização;
- falhas ou ressalvas;
- links para evidências;
- datasets disponíveis.

## 7. Fase de auditoria final

Executar uma auditoria transversal:

### Dados
- completude;
- duplicidade;
- continuidade;
- consistência.

### Semântica
- códigos;
- campos;
- períodos;
- mudanças de layout.

### Pipeline
- reprodutibilidade;
- automação;
- falhas;
- artefatos.

### Git
- histórico;
- commits;
- versões;
- rastreabilidade.

### Produto
- dashboard;
- índice;
- consumo dos dados;
- ausência de dados fictícios.

## 8. Fase de pesquisa quantitativa

Somente após a base histórica atingir o nível de validação adequado:

- séries temporais;
- retornos;
- volatilidade;
- volume financeiro;
- liquidez;
- gaps;
- VWAP/TWAP quando houver dados compatíveis;
- microestrutura quando houver dados intradiários;
- estudos de regime;
- backtests.

Dados inadequados para determinada análise deverão ser explicitamente classificados como inadequados para esse uso.

## 9. Ordem de prioridade

### P0 — Bloqueadores
- workflows quebrados;
- dados corrompidos;
- perda silenciosa;
- inconsistência estrutural;
- pipeline não reproduzível.

### P1 — Base oficial
- 2011–2026;
- normalização;
- validação;
- dataset canônico.

### P2 — Histórico legado
- 1986 e demais períodos com particularidades;
- resolução ou classificação formal das exceções.

### P3 — Produto
- índice;
- dashboard;
- documentação navegável.

### P4 — Pesquisa
- estudos quantitativos;
- microestrutura;
- estratégias;
- backtests.

## 10. Regra de avanço

Não esperaremos a resolução de todos os problemas históricos para avançar.

Um problema só bloqueará o projeto quando houver evidência de que ele contamina uma etapa posterior.

Assim:

problema localizado → isolamento → classificação → continuidade do projeto

e não:

problema localizado → paralisação total.

## 11. Próximo passo operacional

A próxima execução deverá ser uma auditoria de estado do repositório, verificando:

1. workflows ativos;
2. últimos runs e falhas;
3. artefatos produzidos;
4. anos disponíveis;
5. anos validados;
6. anos não validados;
7. estrutura atual de dados;
8. situação específica de 1986;
9. estado do index.html;
10. estado do dashboard.

Depois dessa fotografia, será definido o próximo bloco de execução sem repetir trabalho já concluído.

## 12. Critério de conclusão da etapa atual

A etapa de ingestão será considerada estabilizada quando:

- os workflows principais executarem automaticamente;
- falhas conhecidas estiverem classificadas;
- 2011–2026 tiverem cobertura e validação documentadas;
- 1986 estiver isolado caso permaneça inconclusivo;
- os datasets possuírem status explícito;
- os resultados forem reproduzíveis;
- a documentação estiver sincronizada com o estado real do repositório.

---

Regra-mestra: avançar continuamente, mas nunca transformar dado não validado em dado confiável apenas para acelerar o projeto.


## 13. Atualização de governança — 2026-10-01

A execução histórica do projeto passou a adotar um contrato explícito de execução linear e fail-closed para o COTAHIST.

A cadeia anual de referência é:

**00 → 01 → 02 → 03–05 → 06 → 07 → 08 → GATE → 09 → GATE → 10 → GATE → 11 → GATE → 12 → transição.**

A existência de RAW não implica necessidade de nova aquisição. O repositório deve ser consultado pelo caminho canônico antes de qualquer tentativa de download ou duplicação.

A série anual 1986–2026 possui RAW presente na matriz de certificação atual. O próximo ciclo operacional após o fechamento de 1994 é 1995, cujo RAW já existe no caminho canônico.

O objetivo operacional agora é executar 1995 usando os artefatos existentes, sem reaquisição desnecessária, preservando a mesma disciplina linear aplicada a 1994.

### 13.1 Regra anti-repetição

Antes de criar ou baixar qualquer artefato:

1. consultar o caminho canônico;
2. consultar manifesto;
3. consultar checksum;
4. consultar evidências existentes;
5. consultar matriz de certificação;
6. somente então decidir se existe lacuna real.

### 13.2 Estado de referência

- 1994: FECHADO / TRANSIÇÃO PARA 1995 AUTORIZADA.
- 1995: RAW PRESENTE / PRÓXIMO CICLO.
- 1996+: NÃO INICIAR ATÉ FECHAMENTO FORMAL DE 1995.
- 1986: EXCEÇÃO HISTÓRICA CONTROLADA.



## Aditivo de execução — 2026-10-01 — prevenção de regressão

O incidente da FASE06/1995 mostrou que a existência de certificações anteriores não impede a introdução de uma regra nova incorreta. Portanto, antes de criar ou alterar um gate, deve-se consultar certificações, incidentes, contratos de chaves e evidências históricas.

A responsabilidade foi separada: FASE06 valida semântica e invariantes; FASE07 valida identidade, chaves e cardinalidade. Uma duplicidade de chave candidata observada em FASE06 é evidência para FASE07, não reprovação automática da FASE06.

## REGRA ESTRUTURAL — ISOLAMENTO, MONOTONICIDADE E IMUTABILIDADE DAS FASES — 2026-10-01

As fases do COTAHIST são **monotônicas e isoladas**.

### Regra 1 — uma fase não retorna para fase anterior
Uma fase N não pode reabrir, recalcular, substituir, corrigir ou alterar a evidência normativa da fase N-1 ou de qualquer fase anterior. Se uma inconsistência anterior for descoberta, ela deve ser tratada como **incidente de governança/correção versionada da própria fase afetada**, sem transformar a fase posterior em responsável por ela.

### Regra 2 — uma fase não executa responsabilidade de fase posterior
Uma fase N não pode antecipar critérios pertencentes à fase N+1. Em especial:
- FASE06 não decide unicidade/cardinalidade de chave;
- FASE07 não reescreve a semântica certificada da FASE06;
- FASE08 não redefine identidade da FASE07;
- FASE09–12 não substituem os gates técnicos anteriores.

### Regra 3 — correção permanece na fase de origem
Se uma regra da FASE06 estiver errada, corrige-se a FASE06. Não se cria uma correção da FASE07 para mascarar a FASE06. Se uma regra da FASE07 estiver errada, corrige-se a FASE07.

### Regra 4 — dependência é somente leitura
Uma fase posterior pode **consumir** a evidência autorizada da fase anterior e os dados-fonte necessários à sua própria análise, mas não pode alterá-los nem reinterpretar silenciosamente o estado certificado da fase anterior.

### Regra 5 — promoção é unidirecional
O fluxo é exclusivamente:

**N-1 → N → N+1**

Não existe fluxo operacional **N+1 → N-1** nem **N → N+1 com responsabilidade de N+1 executada dentro de N**.

### Regra 6 — novo teste não retrocertifica
Uma fase posterior pode detectar um incidente com impacto potencial em fase anterior. Isso gera um **registro de impacto e revisão controlada**, não uma reexecução silenciosa nem uma alteração retroativa da evidência histórica.

### Regra 7 — gatilhos não podem quebrar a monotonicidade
Workflows de uma fase concluída não devem ser disparados por alterações genéricas de documentação, README ou artefatos de fases posteriores. O gatilho deve refletir somente a própria fase e suas entradas autorizadas.

### Matriz de responsabilidade

| Fase | Responsabilidade própria | Não pode assumir |
|---|---|---|
| 00 | governança/pré-condições | validação técnica posterior |
| 01 | aquisição/RAW | integridade semântica |
| 02 | integridade da fonte | parsing/normalização |
| 03 | parsing | normalização/identidade |
| 04 | normalização | identidade/semântica posterior |
| 05 | manifesto/checksum | semântica/chaves |
| 06 | semântica/invariantes | identidade/cardinalidade FASE07 |
| 07 | identidade/chaves/cardinalidade | reescrever FASE06 |
| 08 | semântica/calendário/consistência | reabrir identidade |
| 09 | pré-release | corrigir fases anteriores |
| 10 | validação independente | substituir evidências anteriores |
| 11 | certificação/promoção | refazer fases técnicas silenciosamente |
| 12 | fechamento/transição | certificar o próximo ano |

**Regra de governança:** descobrir algo numa fase posterior não autoriza essa fase a executar o trabalho de uma fase anterior.



## Aditivo normativo — GATE 06–08 — 2026-10-01

O projeto passa a reconhecer o **GATE 06–08 — PROMOÇÃO TÉCNICA** como barreira formal entre FASE08 e FASE09. O contrato específico está em 'docs/cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md'.

O Gate não é fase técnica e não pode corrigir, reexecutar ou substituir FASE06, FASE07 ou FASE08. Ele somente verifica as evidências dessas três fases, os estados permitidos, o ano/ciclo, exceções, bloqueadores e o isolamento de responsabilidades.

A promoção é **fail-closed**: somente 'LIBERADO_PARA_FASE09' quando todas as condições obrigatórias forem satisfeitas; qualquer ausência, estado inválido ou condição indeterminada produz 'BLOQUEADO_PARA_FASE09'.

Correções permanecem na fase de origem. README e documentação genérica não são fontes operacionais do Gate e não podem provocar reexecução retroativa de fases concluídas.


## Aditivo — execução independente e retorno verificável — 2026-10-01

O contrato geral está em docs/governanca/CONTRATO_RETORNO_E_MONITORAMENTO_EXECUCOES_B3_V1.md.

Cada workflow deve operar como unidade independente, sem chamar ou reexecutar outro workflow. Dependências entre fases são exclusivamente direcionais e baseadas em evidências autorizadas.

Cada execução deve registrar no GITHUB_STEP_SUMMARY: workflow, fase/tarefa, run, entrada, evidência, status, decisão, bloqueadores, exceções, commit, próxima ação e indicação de reexecução.

O monitor permanente .github/workflows/b3-monitor-execucoes-v1.yml verifica execuções a cada 15 minutos e não dispara reexecuções. Seu objetivo é detectar FAVORÁVEL, NÃO_FAVORÁVEL ou EM_EXECUÇÃO.

A decisão de reexecutar deve ser baseada em mudança real da entrada, correção pendente ou alteração normativa aplicável. Sucesso, falha já registrada ou alteração de documentação não autorizam reexecução por si só.


---

## FONTE NORMATIVA CANÔNICA — 2026-10-01

Este documento é **derivado/operacional** e não constitui fonte independente para geração de código. As regras executáveis devem ser reconciliadas com:

`docs/governanca/LAYOUT_MESTRE_CANONICO_B3_V1.md`

**Regra:** Layout Mestre → especificação da tarefa → código/workflow → evidência.

Se houver divergência, o Layout Mestre prevalece até reconciliação e versionamento formal.

## 14. Execução documental governada — 2026-10-15

A frente de governança documental segue o plano [B3-GOV-PLANO-001](governanca/PLANO_NORMALIZACAO_DOCUMENTAL_GOVERNANCA_V1.md) e a norma GOVERNANCA v1.0.3, sem substituir contratos técnicos específicos do pipeline.

### Estado verificado

- Inventário estrutural inicial concluído: 284 ficheiros enumerados antes de publicar a matriz; a árvore atual contém 285 ficheiros Markdown, incluindo a própria matriz, e 218 estão em `docs/`.
- Matriz publicada: [INVENTARIO_MATRIZ_CONFORMIDADE_DOCUMENTAL_B3_V1.md](governanca/INVENTARIO_MATRIZ_CONFORMIDADE_DOCUMENTAL_B3_V1.md).
- A matriz lista os 284 ficheiros presentes no instante da captura e exclui-se a si própria; a classificação é preliminar por caminho/nome, não uma auditoria semântica nem certificação de conformidade.
- Hashes canónicos dos documentos normalizados continuam pendentes de cálculo/verificação independente.

### Próximas ações obrigatórias

1. Validar a classificação por conteúdo, separando documentos humanos, históricos, modelos, relatórios gerados e artefactos com contrato próprio.
2. Priorizar governança/cartas/layout, planos/roadmaps ativos, contratos e políticas; não modificar em massa os históricos nem relatórios gerados.
3. Implementar cálculo canónico reproduzível UTF-8/LF conforme a norma, excluindo apenas as linhas SHA-256 e commit de referência.
4. Recalcular e verificar os hashes em lote, registrar evidências e commits reais.
5. Atualizar o roadmap após cada fase e não declarar conformidade global com base em amostra parcial.

### Restrições preservadas

- COTAHIST 1986–2025: fechado, apenas consulta e sem alteração sem decisão formal.
- COTAHIST 2026: atualização diária com validação de integridade e preservação da última versão válida.
- `BLOOMBERG_MAIL`: isolado; não é dependência para concluir o projeto B3.


## 15. Revisão semântica documental — 2026-10-15

A FASE 3 iniciou a classificação por conteúdo de documentos prioritários. Foram inspecionados cinco documentos e publicado o relatório [REVISAO_SEMANTICA_DOCUMENTAL_LOTE01_2026-10-15.md](governanca/auditorias/REVISAO_SEMANTICA_DOCUMENTAL_LOTE01_2026-10-15.md). O inventário inicial cobre 284 ficheiros no snapshot de origem; a árvore atual contém 286 ficheiros Markdown, dos quais 219 em `docs/`, após a publicação da matriz e do relatório.

### Divergência normativa aberta — GOV-DIV-001

A Carta Magna, secção 2, diz que a própria Carta Magna prevalece em caso de conflito. O Layout Mestre, secção 2.2, determina que o Layout Mestre prevalece operacionalmente e que as cartas são fontes de entrada, não autoridades paralelas. Não é possível satisfazer simultaneamente as duas regras em caso de conflito.

**Controlo:** para criação/alteração/validação de código, seguir provisoriamente a precedência operacional do Layout Mestre, sem declarar revogação da Carta Magna. A correção exige decisão normativa versionada e evidência autorizada. Até essa reconciliação, não alterar a Carta Magna nem normalizar conteúdo que consolide a contradição.

### Gate seguinte

1. Prosseguir revisão semântica dos contratos, políticas e procedimentos prioritários.
2. Registar as divergências adicionais antes de alterar documentos normativos.
3. Separar documentos humanos, históricos e artefactos gerados.
4. Preparar cálculo canónico reprodutível SHA-256, conforme GOVERNANCA v1.0.3.
5. Não declarar conformidade global enquanto os hashes e a revisão semântica não estiverem concluídos.


## 16. Revisão semântica e auditoria SHA-256 — 2026-10-15

### FASE 3 — Lote 02

Foi publicado o relatório [REVISAO_SEMANTICA_DOCUMENTAL_LOTE02_2026-10-15.md](governanca/auditorias/REVISAO_SEMANTICA_DOCUMENTAL_LOTE02_2026-10-15.md), cobrindo seis contratos/políticas COTAHIST e monitorização. A dívida de metadados legados foi registada; os contratos-fonte não foram alterados. A política de retenção mantém 1986–2025 fechados para ingestão rotineira e 2026 em atualização incremental diária.

### FASE 4 — Ferramenta de integridade documental

- Script somente de leitura: `scripts/governanca/auditar_sha256_documental_b3.py`.
- Workflow: `.github/workflows/b3-auditoria-sha256-documental.yml`.
- Evidência da primeira execução: [run 38713037198](https://github.com/carlos-andrade/B3/actions/runs/38713037198), conclusão `failure`.
- Baseline inicial: 286 Markdown; 271 cabeçalhos de controlo inválidos; 14 hashes pendentes; 1 ficheiro sem H1. Os estados refletem a ausência de metadados em documentos legados, não 271 divergências de hash.
- Correção efetuada: o auditor trata não conformidade documental legada como resultado reportável e reserva falha do job para erro de leitura. A versão corrigida foi executada com sucesso no run 38713567162; isso valida os testes e a triagem, não a conformidade dos hashes de produção.

### Gates e próximas ações

1. Registar a execução corrigida já confirmada no run 38713567162; preservar o artefacto JSON como evidência do run, sem alegar que foi commitado.
2. Refinar a classificação do baseline para separar documentação humana, histórica, gerada e artefactos com contrato próprio — iniciado no Lote 04, ainda incompleto.
3. Resolver a divergência normativa GOV-DIV-001 por decisão versionada, sem editar silenciosamente a Carta Magna ou o Layout Mestre.
4. Normalizar os próximos lotes de metadados sem alterar o corpo técnico e validar referências.
5. Calcular os hashes canónicos após estabilizar cada lote. Não declarar conformidade global antecipadamente.


## 17. Validação técnica do auditor SHA-256 e Lote 03 — 2026-10-15

### Evidência executada

- Testes unitários e auditoria somente de leitura concluídos com sucesso no [run 38713567162](https://github.com/carlos-andrade/B3/actions/runs/38713567162).
- Os testes cobrem: exclusão exata das duas linhas de controlo, normalização UTF-8/BOM/CRLF e rejeição quando faltam linhas de controlo.
- O snapshot analisou 287 Markdown: 271 `CABECALHO_CONTROLO_INVALIDO`, 15 `PENDENTE`, 1 `SEM_CABECALHO_H1`.
- **Limite:** nenhum documento foi classificado como `CONFORME` ou `DIVERGENTE` por hash no baseline; a execução valida o funcionamento técnico e a triagem, não a integridade dos hashes documentais atuais.
- Artefacto JSON de auditoria: disponível no separador Artifacts do run; a execução não alterou ficheiros documentais automaticamente.

### FASE 3 — Lotes semânticos

- Lote 01: cinco documentos de governança revistos; divergência GOV-DIV-001 aberta.
- Lote 02: seis contratos/políticas revistos; dívida de metadados legados registada.
- Lote 03: três contratos de ingestão/identidade revistos; evolução V1.0 → FASE10A M2/V2.0 do Dataset Oficial mapeada. Publicação global V2 continua bloqueada até M3.
- Os relatórios dos lotes estão ligados a partir do inventário documental e não substituem os contratos-fonte.

### Gate seguinte

1. Refinar a matriz semântica para separar documentos humanos, históricos, gerados e artefactos com contrato próprio.
2. Resolver GOV-DIV-001 por decisão normativa versionada.
3. Normalizar metadados nos próximos documentos aprovados para edição, sem alterar o corpo técnico.
4. Reexecutar auditoria após cada lote e confirmar pelo menos uma comparação real de hash antes de declarar o algoritmo validado contra documentos de produção.


## 18. Classificação semântica por natureza documental — Lote 04 — 2026-10-15

- Relatório publicado: [REVISAO_SEMANTICA_DOCUMENTAL_LOTE04_2026-10-15.md](governanca/auditorias/REVISAO_SEMANTICA_DOCUMENTAL_LOTE04_2026-10-15.md).
- Amostra de 12 documentos analisada por conteúdo: regras de ingestão histórica, runbook de migração LFS, rotina diária, contratos COTAHIST e políticas/contratos de evidência e monitorização.
- Resultado: classificação mais precisa entre documento normativo de domínio, runbook operacional, contrato de dados/identidade, contrato de evidência e política. Não foram alterados contratos-fonte nem dados.
- Limite: classificação global dos 288 Markdown (snapshot atual da árvore) não está concluída; artefactos gerados, históricos, modelos e formatos de máquina permanecem pendentes de triagem.
- Regras preservadas: COTAHIST 1986–2025 encerrado para ingestão de rotina e disponível para consulta; 2026 atualizado diariamente; BLOOMBERG_MAIL fora do âmbito.
- GOV-DIV-001 permanece aberta. A precedência operacional provisória do Layout Mestre em operações de código é aplicada sem declarar alteração da Carta Magna.
- Próximo gate: selecionar pequeno lote de documentos humanos com estado/autoridade claros, normalizar apenas metadados autorizados e validar pelo menos um hash documental real (CONFORME ou DIVERGENTE).

## 19. Resultado da auditoria SHA-256 pós-Lote 04 — 2026-10-15

- Execução confirmada: [run 38716296153](https://github.com/carlos-andrade/B3/actions/runs/38716296153), commit `4e09de3d7f6d2e87afb72788c84b16e285b35a8e`, conclusão `success`.
- Baseline auditado: 289 Markdown; 4 `CONFORME`; 13 `PENDENTE`; 271 `CABECALHO_CONTROLO_INVALIDO`; 1 `SEM_CABECALHO_H1`.
- Interpretação: os 271 casos são falhas de controlo/metadados, não 271 hashes divergentes. O artefacto JSON está anexado ao run, não commitado no repositório.
- O workflow passou a incluir alterações Markdown nos gatilhos de push. O run acima confirma que o workflow executou e produziu relatório no commit indicado.
- Próximo gate: normalizar apenas linhas de hash canónico em relatórios documentais cuja estrutura já satisfaça o contrato, recalcular hashes e confirmar nova execução automática. Não editar contratos normativos de autoridade para resolver `GOV-DIV-001`.

## 20. Auditoria SHA-256 confirmada após correção — 2026-10-15

- Execução oficial: [run 38719803051](https://github.com/carlos-andrade/B3/actions/runs/38719803051), commit `8b3797da39cc04ae778e2a289e34b384c6a2c907`, conclusão `success`.
- Resultado: 289 Markdown; 7 `CONFORME`; 10 `PENDENTE`; 271 `CABECALHO_CONTROLO_INVALIDO`; 1 `SEM_CABECALHO_H1`; zero `DIVERGENTE`.
- Os sete documentos selecionados para correção de hash foram confirmados pelo auditor oficial. Isto não equivale a conformidade global: os cabeçalhos legados e a revisão semântica do restante repositório continuam pendentes.
- Próxima etapa: iniciar normalização controlada de um lote pequeno de documentos humanos com cabeçalhos de controlo claros; preservar contratos, históricos, relatórios gerados e dados brutos.
- Restrições: COTAHIST 1986–2025 permanece fechado para ingestão rotineira e disponível para consulta; 2026 permanece incremental diário; BLOOMBERG_MAIL fora do escopo.

## 21. Auditoria SHA-256 após normalização dos 10 metadados — 2026-10-15

- Execução oficial: [run 38723560993](https://github.com/carlos-andrade/B3/actions/runs/38723560993), commit `5b2cbde2693fe8f1cd93bd9f9d71e45a5796cc3c`, conclusão `success`.
- Resultado auditado: 289 Markdown; 17 `CONFORME`; 271 `CABECALHO_CONTROLO_INVALIDO`; 1 `SEM_CABECALHO_H1`; zero `PENDENTE`, zero `DIVERGENTE` e zero `ERRO_LEITURA`.
- A auditoria confirmou os 10 hashes normalizados pela ferramenta canónica. A integridade dos hashes válidos foi verificada, mas a conformidade estrutural dos 271 documentos continua pendente.
- Próximo gate: classificar os cabeçalhos inválidos por tipo (humano, normativo, histórico, gerado, contrato/máquina) e normalizar lotes aprovados individualmente; triagem do documento COTAHIST 2026 sem H1 antes de editar.
- `GOV-DIV-001` continua aberta. COTAHIST 1986–2025 mantém-se somente para consulta de rotina; 2026 continua incremental diário; `BLOOMBERG_MAIL` permanece isolado e fora do escopo B3.


## 22. Atualização do roadmap — normalização documental concluída — 2026-10-15

### Resultado confirmado

A auditoria SHA-256 documental foi reexecutada após a normalização dos cabeçalhos e confirmou:

| Indicador | Resultado |
|---|---:|
| Ficheiros Markdown analisados | 302 |
| CONFORME | 302 |
| CABECALHO_CONTROLO_INVALIDO | 0 |
| DIVERGENTE | 0 |
| Outros estados inválidos reportados | 0 |

- Evidência primária: [auditoria SHA-256, run 159](https://github.com/carlos-andrade/B3/actions/runs/38768768725), conclusão `success`.
- Artefacto inspecionado: `sha256_documental_b3_report.json`; `files_scanned=302`, `status_counts={"CONFORME":302}`.
- Normalização automatizada: [workflow de normalização, run 1](https://github.com/carlos-andrade/B3/actions/runs/38767785791).
- Commit do lote automatizado de 190 documentos: [1e1870479431f49d4786fa89afbd41e4c40f60c0](https://github.com/carlos-andrade/B3/commit/1e1870479431f49d4786fa89afbd41e4c40f60c0).
- A correção incluiu o relatório gerado automaticamente `docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.md`, para evitar que a sua regeneração reintroduza um cabeçalho inválido.
- O resultado foi registado na [Issue #11](https://github.com/carlos-andrade/B3/issues/11).

### Decisão do roadmap

**Concluída:** normalização estrutural dos cabeçalhos e validação de integridade SHA-256 canónico para os 302 ficheiros Markdown abrangidos pelo auditor.

**Não abrangido por esta conclusão:** validade semântica de cada documento, certificação operacional dos dados, resolução de `GOV-DIV-001`, proveniência RAW COTAHIST, captura da lista oficial `ExternalSecurityCategoryCode`, ativação do heartbeat externo, aprovação dos limiares WATCHDOG e aceitação operacional final. Estes itens mantêm os estados próprios e não são promovidos por inferência.

### Próximas ações

1. Prosseguir a revisão semântica e a resolução versionada de divergências normativas, sem alterar silenciosamente documentos de autoridade.
2. Manter a revisão independente da proveniência RAW COTAHIST e a aquisição da lista oficial `ExternalSecurityCategoryCode` como dependências explícitas.
3. Continuar o encerramento da Fase C WATCHDOG: triagem de falhas, aprovação humana dos limiares, heartbeat externo, escalonamento e retenção durável.
4. Preservar COTAHIST 1986–2025 em modo de consulta e manter 2026 em atualização incremental diária.
5. Manter BLOOMBERG_MAIL isolado e fora do âmbito deste roadmap B3.

### Histórico de atualização

| Data | Alteração | Evidência |
|---|---|---|
| 2026-10-15 | Fecho da pendência dos 225 controlos inválidos; auditoria final confirmou 302/302 conformes, zero inválidos e zero divergentes | [Run 38768768725](https://github.com/carlos-andrade/B3/actions/runs/38768768725); [Issue #11](https://github.com/carlos-andrade/B3/issues/11) |


## 23. Reconciliação normativa GOV-DIV-001 e revisão semântica — 2026-10-15

### Decisão registada

A divergência GOV-DIV-001 foi reconciliada por separação de competências normativas, com decisão versionada em [DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md](governanca/decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md).

- Carta Magna B3 v1.3.0: princípios constitucionais, competências e processo de alteração normativa.
- Layout Mestre B3 v1.1.0: especificação operacional única para pipelines, workflows e código, subordinada aos limites constitucionais.
- Conflito aparente: fail-closed para a decisão afetada, reconciliação versionada e continuidade das trilhas independentes.
- Evidência da decisão e registo: [Issue #11](https://github.com/carlos-andrade/B3/issues/11).

### Estado da revisão semântica integral

A revisão semântica integral **continua em curso**. Os Lotes 01–04 são amostras documentadas, não uma revisão integral dos 303 Markdown presentes no snapshot de 2026-10-15. A auditoria SHA-256 valida integridade canónica, não a verdade, atualidade, coerência normativa ou validade operacional do conteúdo.

A matriz integral de controlo foi publicada em [MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md](governanca/auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md), enumerando 303 Markdown no snapshot. A matriz distingue 17 documentos com revisão prévia a revalidar, quatro relatórios amostrais, a decisão GOV-DIV-001 e 281 documentos ainda pendentes de revisão de conteúdo. A matriz é inventário/controlo de execução, não certificação de que todos foram revistos. A revisão deve avançar por lotes com classificação por conteúdo, domínio, autoridade, dependências, contradições, decisão requerida e evidência. Os documentos de autoridade e os contratos de dados têm prioridade; históricos e artefactos gerados exigem tratamento próprio, sem reescrita do passado.

### Resultado de auditoria estrutural pós-decisão

A auditoria do commit de decisão [run 38773908484](https://github.com/carlos-andrade/B3/actions/runs/38773908484) confirmou Carta Magna e Layout Mestre conformes, mas identificou hash divergente na própria decisão, corrigido no commit [7b0db7bef8cfb48ea4986629d8fd0a10ed44c333](https://github.com/carlos-andrade/B3/commit/7b0db7bef8cfb48ea4986629d8fd0a10ed44c333). A auditoria posterior a essa correção é obrigatória antes de declarar o conjunto documental conforme.

### Pendências não promovidas

- Revisão semântica de todos os documentos do inventário, sem inferir conclusão a partir de amostra.
- Outros conflitos de versão/estado identificados nos Lotes 02 e 03, incluindo contrato Dataset Oficial V1.0 versus V2.0 e estado de adoção do contrato NORMALIZED V2.0.
- Proveniência RAW COTAHIST, lista oficial ExternalSecurityCategoryCode e WATCHDOG permanecem frentes separadas.
- COTAHIST 1986–2025 continua apenas para consulta; 2026 mantém atualização diária.
- BLOOMBERG_MAIL permanece isolado e fora do escopo B3.
