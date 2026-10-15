# Revisão semântica documental — Lote 08: governança de dados, frescor e fronteira de projetos

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-008 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; DIVERGENCIA_DE_ESTADO_IDENTIFICADA |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente para decisões normativas; relatório não concede aprovação operacional |
| **Origem** | Inspeção de conteúdo de dez documentos de governança e garantia de dados |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../../docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../../docs/governanca/decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Confiança de workflows, carta de escopo Bloomberg, BCB/SGS, frescor e índices B3 |
| **Objetivo** | Identificar conflitos de estado, snapshots históricos e limites de certificação |
| **Dependências** | Runs/commits citados, matriz de frescor, Issue #11 e decisões de escopo |

## 1. Resultado executivo

Foram revistos dez documentos. A regra transversal de fail-closed, preservação RAW e separação entre data de execução e data de mercado é coerente. Os documentos de frescor e certificação datados de 26–27/09/2026 são fotografias históricas e não devem ser apresentados como estado corrente em 15/10/2026; os estados atuais devem ser consultados nas execuções e manifestos correspondentes.

Foi encontrada uma divergência semântica explícita na Carta de Confiança dos Workflows: o metadado superior declara EM_REVISAO, enquanto o corpo declara Status ATIVA. Sem decisão de autoridade não se escolhe silenciosamente qual estado prevalece; o documento permanece marcado para reconciliação.

A carta histórica de recebimento incremental Bloomberg foi atualizada para deixar claro que o texto original está fora do âmbito operacional B3 atual. O corpo histórico foi preservado e não autoriza integração entre repositórios.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| governanca/CARTA_DE_CONFIANCA_WORKFLOWS.md | Carta/política de confiança de workflows | Princípios de fonte identificável, RAW, proveniência, fail-closed e validação são coerentes. Existe conflito interno de estado: cabeçalho EM_REVISAO e corpo ATIVA. | Abrir reconciliação normativa de estado. Não declarar a carta plenamente aprovada/ativa sem decisão versionada que harmonize cabeçalho e corpo. |
| governanca/CARTA_RECEBIMENTO_INCREMENTAL_BLOOMBERG_MAIL_V1_0_2026-10-08.md | Carta histórica de integração entre projetos | O texto original descrevia fluxo BLOOMBERG_MAIL → B3, incompatível com o limite atual de isolamento. Foi adicionada nota de 2026-10-15: HISTÓRICO/NÃO APLICÁVEL à operação B3 atual, preservando o conteúdo original. | Não executar nem usar como dependência. Qualquer integração futura exige nova decisão explícita e contrato aprovado. |
| governanca/REGISTO_APLICACAO_GOVERNANCA_FASE_C_2026-10-15.md | Registo de aplicação de governança | Distingue corretamente propostas centrais de normas aprovadas e proíbe inferir aprovação, retirar PROVISIONAL ou expor secrets. Mantém Fase C em curso. | Manter como registo de aplicação; atualizar apenas quando existir evidência nova e autorização. |
| governanca/bcb_sgs/INVENTARIO_BCB_SGS_NUCLEO_MACRO_V1.md | Inventário de séries macro | Define requisitos de origem, RAW/NORMALIZED, hashes, QUALITY e frescor. As afirmações sobre séries/códigos SGS devem ser revalidadas contra fonte oficial antes de serem usadas para certificação. | Usar como contrato/inventário de escopo; validar os códigos e a atualidade no workflow/fonte oficial. Não considerar citações ou inventário, isoladamente, prova de ingestão corrente. |
| governanca/garantia_atualizacao_dados/CARTA_DE_GARANTIA_ATUALIZACAO_DADOS_2026-09-26.md | Carta histórica de frescor | O status NÃO CERTIFICADA é coerente com a fotografia de 26/09 e com a diferença entre data de geração e data de mercado. | Preservar como evidência temporal; não reutilizar como certificação corrente nem reescrever o snapshot histórico. |
| governanca/garantia_atualizacao_dados/CERTIFICACAO_DOMINIOS_B3_2026-09-27.md | Relatório histórico de certificação por domínio | Explicita fail-closed e separa COTAHIST/BCB/índices/derivativos; os estados pertencem a 27/09/2026. | Não tratar como estado atual. O run de índices #24 posterior confirmou 34 índices validados, mas cada domínio continua a exigir evidência específica e corrente. |
| governanca/garantia_atualizacao_dados/DIAGNOSTICO_FRESCOR_COTAHIST_2026-09-27.md | Diagnóstico histórico de frescor | Distingue COTAHIST diário de snapshot anual e identifica divergência de convergência, não ausência total do dia. | Manter como diagnóstico histórico; confirmar qualquer estado corrente em manifests e runs posteriores, sem inferir de timestamps de execução. |
| governanca/garantia_atualizacao_dados/MATRIZ_GLOBAL_FRESCOR_DADOS_B3_2026-09-27.md | Matriz histórica de frescor | Usa data de mercado, RAW, normalização e evidência como gates. O estado global NÃO CERTIFICADA é explicitamente temporal. | Preservar a fotografia e usar o monitor atual para estado corrente; não elevar nenhum domínio com base nesta matriz antiga. |
| governanca/garantia_atualizacao_dados/README.md | Índice/política de emissão de garantia | Requisitos de fonte, RAW, integridade, lacunas e workflow são coerentes. | Manter como índice de política; não emitir garantia até todos os requisitos e domínios obrigatórios estarem evidenciados. |
| governanca/indices_b3/INVENTARIO_INDICES_B3_V1.md | Inventário/contrato de certificação de índices | Exige fonte oficial, hashes, data de referência, rejeição de páginas vazias e manifestos VALIDADO. O texto cita evidências externas de 27/09 e não substitui a execução posterior. | Associar o estado atual à evidência do run #24; preservar o escopo de composição de carteiras de índices de ações, sem extrapolar a derivativos ou outros domínios. |

## 3. Achados e decisões

### SEM-08-01 — conflito interno de estado na Carta de Confiança dos Workflows

**Fato observado:** o cabeçalho declara EM_REVISAO, enquanto o corpo declara ATIVA. São estados materialmente diferentes.

**Decisão:** a divergência permanece aberta para decisão normativa. Até a reconciliação, não tratar a carta como aprovação inequívoca de toda a versão atual; aplicar os requisitos de segurança que não dependem da controvérsia e manter alterações de risco bloqueadas se a autoridade depender do estado da carta.

### SEM-08-02 — isolamento de BLOOMBERG_MAIL

**Correção aplicada:** a carta histórica foi versionada como 1.1.0 e recebeu nota explícita de que o fluxo de integração descrito no corpo não é aplicável à operação atual B3. O conteúdo de 2026-10-08 permanece recuperável no Git.

**Regra vigente:** BLOOMBERG_MAIL permanece isolado e fora do escopo operacional B3. Não criar ingestão, dependência de workflow ou transferência de dados por referência ao documento histórico.

### SEM-08-03 — frescor/certificação dependem de observação e evidência atuais

**Fato observado:** as cartas de 26–27/09 têm estados vinculados à data e à evidência daquele momento.

**Decisão:** não as usar como status corrente. Consultar os manifestos e workflows posteriores por domínio; manter a proveniência RAW como gate independente. A execução verde, por si só, não prova atualidade ou qualidade de negócio.

## 4. Conclusão

O conteúdo dos dez documentos foi revisto. A carta Bloomberg recebeu correção explícita de escopo; a divergência EM_REVISAO/ATIVA na Carta de Confiança dos Workflows permanece pendente de decisão normativa e não foi ocultada.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária. A revisão de proveniência RAW e a captura da lista oficial ExternalSecurityCategoryCode permanecem pendências separadas. BLOOMBERG_MAIL permanece isolado.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Plano Mestre de Execução](../../docs/PLANO_MESTRE_DE_EXECUCAO.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
