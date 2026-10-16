# Revisão semântica documental — Lote 02

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-002 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Classificação semântica e reconciliação |
| **Estado** | REVISAO_SEMANTICA_FECHADA; DIVIDA_HISTORICA_EXPLICITADA; GATES_OPERACIONAIS_SEPARADOS |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | c4e38c3a05cd48a41472953677c45f0acd775c57b19e7133d0a0345daa6b2b8d |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente de aprovação específica |
| **Origem** | Inspeção direta dos seis documentos listados e norma GOVERNANCA v1.0.3 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) |
| **Cadeia de autoridade** | FONTES → CONTRATOS/POLÍTICAS → LAYOUT MESTRE → CÓDIGO/WORKFLOWS → EVIDÊNCIAS → VALIDAÇÃO |
| **Escopo** | Classificação semântica de contratos e política; sem alteração de dados históricos ou workflows operacionais |
| **Objetivo** | Confirmar domínio e função dos contratos, identificar lacunas de metadados e impedir alterações incompatíveis com a governança técnica |
| **Dependências** | Norma GOVERNANCA v1.0.3; Layout Mestre B3; Política de ciclo de vida COTAHIST |

## 1. Resultado executivo

Foram revistos seis documentos. Todos têm função técnica reconhecível e devem preservar os contratos substantivos existentes. Cinco dos seis apresentam um formato legado sem a tabela de metadados exigida pela norma transversal; a política de ciclo de vida também usa metadados em texto corrido, sem cabeçalho tabular canónico. Esta constatação é dívida documental, não prova de falha dos pipelines nem autorização para alterar regras operacionais.

## 2. Matriz

| Documento | Classificação semântica | Observação | Ação recomendada |
|---|---|---|---|
| [Contrato de Evidência FASES 06–09](../../cotahist/CONTRATOS_EVIDENCIA_FASES_06_09_V1.md) | CONTRATO_EVIDENCIA_FASES | Define evidência mínima e estados para FASE06–09, com critério de aprovação e bloqueios. | Preservar o conteúdo técnico; normalizar metadados após mapear versão, autoridade, origem e hash. |
| [Contrato de Evidência FASES 00–09](../../cotahist/CONTRATO_EVIDENCIA_FASES_00_09_V1.md) | CONTRATO_EVIDENCIA_CADEIA | O nome mantém 00–09, mas o próprio corpo declara que a versão atual cobre 00–12. | Tratar o nome do ficheiro como referência histórica; decidir se título/nome devem ser reconciliados sem quebrar links. |
| [Contrato de Execução Sequencial COTAHIST](../../cotahist/CONTRATO_EXECUCAO_SEQUENCIAL_FASES_COTAHIST_V1.md) | CONTRATO_EXECUCAO_SEQUENCIAL | Define gates fail-closed, monotonicidade e responsabilidade por fase. | Preservar regras; mapear referências de workflow e compatibilidade com o Layout Mestre. |
| [Contrato Gate 06–08](../../cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md) | CONTRATO_GATE_PROMOCAO | Define entrada autorizada, estados permitidos e critérios do gate. | Preservar a semântica; verificar referências de evidência contra os workflows atuais antes de alterar. |
| [Contrato de Retorno e Monitoramento](../CONTRATO_RETORNO_E_MONITORAMENTO_EXECUCOES_B3_V1.md) | CONTRATO_MONITORAMENTO_EXECUCOES | Define estados operacionais, retorno no Step Summary, monitor e anti-reexecução. | Revisar referências atuais e manter monitor como observador, não executor. |
| [Política de Retenção COTAHIST 1986–2026](../politicas/POLITICA_RETENCAO_COTAHIST_1986_2026_V1.md) | POLITICA_CICLO_VIDA_DADOS | Regista 1986–2025 fechados para ingestão rotineira e 2026 em atualização diária; ressalva que encerramento não equivale a certificação integral. | Preservar integralmente as restrições históricas; qualquer normalização deve ser só de metadados e sem alterar política substantiva. |

## 3. Achados transversais

1. **Metadados legados:** a norma GOVERNANCA v1.0.3 exige título H1 e tabela Markdown de metadados; contratos antigos ainda usam linhas em texto corrido ou não têm cabeçalho padrão.
2. **Compatibilidade de referências:** não renomear contratos ou workflows sem mapear referências entrantes e preservar aliases/links.
3. **Autoridade operacional:** os contratos detalham responsabilidades técnicas; mudanças normativas devem ser reconciliadas com o Layout Mestre, não gerar autoridade paralela.
4. **Preservação do histórico:** não usar normalização de cabeçalho como razão para alterar dados, evidências ou regras COTAHIST.

## 4. Validação do auditor SHA-256

Foi criado um auditor somente de leitura em [auditar_sha256_documental_b3.py](../../../scripts/governanca/auditar_sha256_documental_b3.py) e workflow [b3-auditoria-sha256-documental.yml](../../../.github/workflows/b3-auditoria-sha256-documental.yml). A primeira execução identificou 286 ficheiros Markdown, com 271 classificados como cabeçalho de controlo inválido, 14 hashes pendentes e 1 ficheiro sem H1. Essa execução terminou em falha porque o auditor inicial tratava a dívida documental legada como erro de processo. O script foi corrigido para reportar o baseline legado sem falhar o job, mantendo erro de leitura como falha operacional; a reexecução corrigida foi concluída com sucesso no [run 38713381853](https://github.com/carlos-andrade/B3/actions/runs/38713381853). O job produziu artefacto JSON, sem modificar os documentos. A contagem desse snapshot foi 287 Markdown: 271 cabeçalhos de controlo inválidos, 15 hashes pendentes e 1 ficheiro sem H1.

Este resultado é um baseline de triagem, não uma certificação: a categoria CABECALHO_CONTROLO_INVALIDO agrega documentos que não contêm as duas linhas de controlo e requer subdivisão entre documento humano, histórico, gerado e artefacto com contrato próprio.

A versão atual inclui testes unitários para exclusão das duas linhas de controlo, normalização BOM/CRLF e rejeição de cabeçalho incompleto. Os testes e a auditoria passaram no [run 38713567162](https://github.com/carlos-andrade/B3/actions/runs/38713567162). O snapshot desse run continha 287 Markdown: 271 com controlos de cabeçalho inválidos, 15 pendentes e 1 sem H1. O resultado confirma execução técnica do auditor e dos testes; não confirma nenhum hash documental existente, pois nenhum documento chegou ao estado de comparação CONFORME/DIVERGENTE nesse baseline.

## 5. Próximos passos

1. Executar e validar os testes unitários do hash canónico adicionados em `tests/governanca/test_auditar_sha256_documental_b3.py`; a execução automatizada está em curso no momento desta atualização.
2. Refinar o auditor para distinguir documentos que exigem cabeçalho padrão dos que possuem contrato de geração próprio.
3. Reconciliar a divergência GOV-DIV-001 antes de qualquer alteração normativa.
4. Normalizar metadados de contratos em lotes pequenos, preservando integralmente o corpo e validando referências.
5. Calcular hashes canónicos após a versão final de cada lote; não preencher valores por estimativa.

## 6A. Adendo de fecho — 2026-10-16

**Estado da revisão semântica:** FECHADA para os seis documentos inspecionados. Os seis documentos agora apresentam cabeçalho de controlo estruturado com H1, metadados e cadeia de autoridade alinhada a GOV-DIV-001. A aparente divergência entre o nome físico `CONTRATO_EVIDENCIA_FASES_00_09_V1.md` e o seu âmbito normativo está resolvida documentalmente: o caminho foi mantido para compatibilidade, enquanto o corpo identifica explicitamente o contrato FASE00–FASE12 V2.0. Não renomear o ficheiro sem mapear referências e aprovar uma migração de links.

Os números de baseline dos runs 38713381853 e 38713567162 são históricos e não descrevem o estado atual. A auditoria canónica mais recente concluída, run [38881634574](https://github.com/carlos-andrade/B3/actions/runs/38881634574), analisou 330 ficheiros: 316 CONFORME, 14 PENDENTE, zero DIVERGENTE e zero FORMATO_HASH_INVALIDO.

**Separação de estado:** a revisão semântica e o teste do algoritmo estão fechados. Adoção de contratos, execução real de workflows e aprovação formal do proprietário não são inferidas por esta revisão e permanecem gates operacionais quando exigidos por cada contrato.


## 6. Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.1.0 | 2026-10-16 | Fecho da revisão semântica; snapshot original preservado; ações operacionais separadas | GOV-DIV-001, matriz integral v1.3.0 e auditoria SHA-256 run 38881634574 |
| 1.0.0 | 2026-10-15 | Revisão semântica de seis contratos/políticas; dívida de metadados e estado inicial do auditor registados | Inspeção direta dos documentos-fonte; workflow de auditoria SHA-256 |
| 1.1.0 | 2026-10-15 | Reexecução do auditor corrigido concluída com sucesso; artefacto JSON publicado no run | [Run 38713381853](https://github.com/carlos-andrade/B3/actions/runs/38713381853) |
| 1.2.0 | 2026-10-15 | Testes unitários do algoritmo e nova auditoria concluídos com sucesso; hashes existentes continuam sem validação efetiva no baseline | [Run 38713567162](https://github.com/carlos-andrade/B3/actions/runs/38713567162) |
