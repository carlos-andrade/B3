# Revisão semântica documental — Lote 04: classificação por natureza documental

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-004 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Classificação semântica e reconciliação |
| **Estado** | REVISAO_PARCIAL; CLASSIFICACAO_POR_AMOSTRAGEM |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular por ferramenta reprodutível conforme GOVERNANCA v1.0.3 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente de aprovação específica |
| **Origem** | Inspeção de conteúdo de documentos do repositório B3 e comparação com os relatórios dos Lotes 01–03 |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); Layout Mestre Canónico B3 |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objetivo e limites

Classificar uma amostra de documentos pela sua função real, evitando aplicar cabeçalhos ou estados normativos de forma mecânica. Este lote é uma classificação documental, não uma certificação de conformidade e não altera os contratos ou regras de ingestão.

## 2. Classificação semântica da amostra

| Caminho | Natureza | Evidência observada | Tratamento recomendado |
|---|---|---|---|
| `docs/ingestao/REGRAS_PERMANENTES_INGESTAO_HISTORICA_B3_V1.0.md` | Regra operacional/documento normativo de domínio | Define marco temporal 1986, fonte primária, preservação RAW, integridade e limites de inferência | Preservar conteúdo. Normalizar cabeçalho somente com estado documental reconciliado; o corpo declara “ATIVA”, mas a aprovação formal não está demonstrada no próprio ficheiro |
| `docs/ingestao/RUNBOOK_MIGRACAO_GIT_LFS_COTAHIST_A1987_V1.md` | Runbook operacional | Define pré-condições imutáveis para migração A1987, caminho, SHA-256, tamanho, linhas e workflow; declara que a migração ainda não foi executada | Tratar como instrução operacional controlada. Não executar a migração nem alterar os valores de controlo durante a normalização documental |
| `docs/ingestao/PARTE01_ROTINA_ATUALIZACAO_DIARIA_COTAHIST_V1.1.md` | Runbook/rotina de atualização | Documenta dois horários BRT, conversão UTC e fluxo de execução | Reconciliar com a política atual: 1986–2025 em consulta/read-only e 2026 com atualização diária. Não assumir que o agendamento descrito prova execução bem-sucedida |
| `docs/ingestao/CONTRATO_DATASET_OFICIAL_COTAHIST_V1.0.md` | Contrato de dados histórico | O Lote 03 identificou versão histórica face ao contrato físico FASE10A M2/V2.0 | Manter como referência histórica; explicitar hierarquia de versão no índice de contratos antes de alterar estados |
| `docs/ingestao/CONTRATO_NORMALIZED_ANUAL_COTAHIST_V2.0.md` | Proposta/contrato de dados | O Lote 03 registou estado de proposta à espera de implementação controlada | Não marcar como adotado sem evidência de aprovação/implementação |
| `docs/ingestao/COTAHIST_1986_CONTRATO_IDENTIDADE_K4_V1.0.md` | Contrato de identidade e reconciliação | Define identidade K4; o Lote 03 recomenda não deduplicar RAW de 1986 apenas com K4 | Preservar o contrato e manter a cautela de identidade no pipeline |
| `docs/cotahist/CONTRATOS_EVIDENCIA_FASES_06_09_V1.md` | Contrato de evidência de fases | O Lote 02 identificou critérios de evidência para fases 06–09 | Tratar como contrato operacional; verificar referências cruzadas antes de qualquer alteração |
| `docs/cotahist/CONTRATO_EVIDENCIA_FASES_00_09_V1.md` | Contrato de evidência de fases | O Lote 02 identificou escopo de evidência abrangendo fases 00–09 | Manter alinhamento com o contrato sequencial e com o gate de promoção |
| `docs/cotahist/CONTRATO_EXECUCAO_SEQUENCIAL_FASES_COTAHIST_V1.md` | Contrato de execução | O Lote 02 identificou a sequência de fases COTAHIST como contrato operacional | Não reordenar fases sem decisão versionada e evidência |
| `docs/cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md` | Gate/contrato de promoção técnica | O Lote 02 identificou regras de promoção entre fases técnicas | Preservar como gate; a execução do gate deve ser evidenciada separadamente |
| `docs/governanca/CONTRATO_RETORNO_E_MONITORAMENTO_EXECUCOES_B3_V1.md` | Contrato de observabilidade/retorno | O Lote 02 identificou obrigações de retorno e monitorização | Separar a especificação do contrato da prova de execução real |
| `docs/governanca/politicas/POLITICA_RETENCAO_COTAHIST_1986_2026_V1.md` | Política de retenção e ciclo de vida | Define tratamento temporal de COTAHIST; política deve respeitar o corte entre histórico fechado e 2026 corrente | Manter alinhada com a regra: 1986–2025 read-only; 2026 atualizado diariamente |

## 3. Decisões de classificação

1. **Documentos humanos** (regras, runbooks, políticas e contratos) podem receber o cabeçalho visual padrão, mas a normalização deve preservar o corpo técnico e distinguir estado operacional de aprovação formal.
2. **Relatórios históricos de execução** devem conservar data, resultado, workflow/commit e limitações; não devem ser reescritos como se o estado atual fosse o estado histórico.
3. **Artefactos gerados e formatos de máquina** exigem tratamento específico. A norma Markdown não autoriza a alteração de schemas, dados, hashes de conteúdo bruto ou ficheiros de contrato técnico apenas para satisfazer a aparência do cabeçalho.
4. Um nome de ficheiro, uma classificação preliminar por diretório ou um estado escrito no corpo não bastam, isoladamente, para provar aprovação, execução ou conformidade.
5. A rotina diária documentada é uma especificação de agendamento; a prova de execução deve vir dos runs e dos resultados correspondentes.

## 4. Regras de preservação do projeto

- COTAHIST de 1986 a 2025: encerrado para ingestão de rotina e disponível para consulta, sem mutação retroativa no fluxo diário.
- COTAHIST 2026: atualização diária, com aquisição, validação e evidência rastreáveis.
- O contrato K4 não autoriza deduplicação automática do RAW de 1986.
- O projeto BLOOMBERG_MAIL permanece fora do âmbito deste lote e isolado no seu repositório próprio.

## 5. Pendências e próximos gates

- [ ] Classificar por conteúdo o restante inventário, incluindo relatórios históricos, modelos, artefactos gerados e documentos de máquina.
- [ ] Resolver `GOV-DIV-001` por decisão normativa versionada; não alterar silenciosamente a Carta Magna nem o Layout Mestre.
- [ ] Normalizar um pequeno lote de documentos humanos após determinar estado e autoridade, preservando conteúdo e referências técnicas.
- [ ] Calcular SHA-256 canónico após a normalização e executar a auditoria, exigindo pelo menos um resultado real `CONFORME` ou `DIVERGENTE`.
- [ ] Atualizar a matriz documental e o Plano Mestre após cada gate concluído.

## 6. Resultado

A amostra confirma que o inventário não pode ser normalizado por uma regra única aplicada indistintamente. A classe documental determina o tratamento: contrato, runbook, política, relatório histórico, modelo e artefacto de máquina têm riscos de alteração diferentes. Este lote não certifica conformidade global, não resolve `GOV-DIV-001` e não declara hashes de produção validados.
