# Revalidação semântica pós GOV-DIV-001 — Lotes 01–04 e documentos normativos prioritários

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-POST-GOVDIV-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVALIDACAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVALIDACAO_DOS_17_PRIORITARIOS_CONCLUIDA; ACOES_OPERACIONAIS_SEPARADAS; AUDITORIA_SHA256_PENDENTE |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | 4ba8972f85266797c79737c11fc641dacb728e56e5e9bfbf80661ddcf5f494d3 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente de validação formal |
| **Origem** | Inspeção dos documentos normativos, contratos e relatórios dos Lotes 01–04 no repositório B3 |
| **Autoridade superior** | [Carta Magna B3](../../CARTA_MAGNA_GOVERNANCA_B3.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md); [Layout Mestre](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Revalidação pós-decisão de documentos previamente revistos e reavaliação integral dos relatórios amostrais 01–04 |
| **Objetivo** | Remover a ambiguidade normativa residual sem reescrever evidência histórica nem declarar conclusão global sem provas |
| **Dependências** | GOV-DIV-001; Matriz de revisão semântica integral; relatórios dos Lotes 01–04 |

## 1. Resultado executivo

A decisão GOV-DIV-001 está registada e o Layout Mestre foi atualizado para a versão 1.2.0 no commit [9fe05cd90c172ee1453d501485752fa2142fc763](https://github.com/carlos-andrade/B3/commit/9fe05cd90c172ee1453d501485752fa2142fc763). A versão explicita autoridade por domínio e elimina a lista de precedência universal que colocava o Layout acima de evidência factual e documentação externa em qualquer circunstância. O hash canónico foi fixado no commit [13190eae1f57d59e02a995349c216979999343f2](https://github.com/carlos-andrade/B3/commit/13190eae1f57d59e02a995349c216979999343f2); a auditoria pós-commit desse SHA ainda precisa de terminar com resultado verificável antes da certificação.

A inspeção identificou linguagem em cartas e contratos que diz que o Layout prevalece operacionalmente. Essa linguagem é compatível com GOV-DIV-001 apenas no domínio executável: não pode ser interpretada como supremacia constitucional, nem como autorização para descartar factos oficiais. O registo de decisão e este relatório passam a ser a referência de reconciliação. Os textos históricos dos Lotes 01–04 não devem ser reescritos como se a decisão já existisse na data original.

## 2. Revalidação dos relatórios amostrais 01–04

| Relatório | Estado original | Resultado pós GOV-DIV-001 | Tratamento |
|---|---|---|---|
| [Lote 01](REVISAO_SEMANTICA_DOCUMENTAL_LOTE01_2026-10-15.md) | REVISAO_PARCIAL; DIVERGENCIA_ABERTA | A divergência de precedência descrita no §3 foi resolvida pela decisão versionada e pela atualização do Layout. As observações originais continuam válidas como registo histórico da divergência à data. | Preservar snapshot histórico; este relatório regista a resolução posterior. |
| [Lote 02](REVISAO_SEMANTICA_DOCUMENTAL_LOTE02_2026-10-15.md) | REVISAO_PARCIAL; METADADOS_LEGADOS_PENDENTES | Os achados sobre metadados, nomes históricos, referências cruzadas e estados de implementação continuam pendentes; não são resolvidos por GOV-DIV-001. | Preservar; manter ações por documento. |
| [Lote 03](REVISAO_SEMANTICA_DOCUMENTAL_LOTE03_2026-10-15.md) | REVISAO_PARCIAL; METADADOS_LEGADOS_PENDENTES | As questões de versão Dataset Oficial V1/V2 e adoção do contrato NORMALIZED V2.0 permanecem sem resolução automática. | Preservar; exigir evidência de adoção e mapa de versão antes de alterar estados. |
| [Lote 04](REVISAO_SEMANTICA_DOCUMENTAL_LOTE04_2026-10-15.md) | REVISAO_PARCIAL; CLASSIFICACAO_POR_AMOSTRAGEM | Continua a ser amostra de classificação; não pode sustentar conclusão sobre o restante inventário. Os seus alertas sobre rotina diária, retenção e natureza documental mantêm-se aplicáveis. | Preservar snapshot; completar revisão integral dos documentos elegíveis. |

## 3. Revalidação dos 17 documentos prioritários — revisão concluída

A lista abaixo regista o conjunto revalidado pós-decisão e está sincronizada com a matriz integral v1.2.0. Foram verificadas autoridade/domínio, referências canónicas, cadeia de autoridade, afirmações de precedência, limites entre documento normativo e evidência factual, estados/versões declarados e ações de implementação explicitamente descritas. A revalidação documental deste conjunto está concluída; isso não constitui aprovação formal do proprietário, nem prova execução de workflows ou adoção operacional de contratos.

1. `docs/CARTA_DE_CONFIANCA_DOS_DADOS.md`
2. `docs/CARTA_DE_GARANTIAS_DO_PROJETO_B3.md`
3. `docs/CARTA_MAGNA_GOVERNANCA_B3.md`
4. `docs/MODELO_GOVERNANCA_PARA_PROJETOS.md`
5. `docs/cotahist/CONTRATOS_EVIDENCIA_FASES_06_09_V1.md`
6. `docs/cotahist/CONTRATO_EVIDENCIA_FASES_00_09_V1.md`
7. `docs/cotahist/CONTRATO_EXECUCAO_SEQUENCIAL_FASES_COTAHIST_V1.md`
8. `docs/cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md`
9. `docs/governanca/CONTRATO_RETORNO_E_MONITORAMENTO_EXECUCOES_B3_V1.md`
10. `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`
11. `docs/governanca/politicas/POLITICA_RETENCAO_COTAHIST_1986_2026_V1.md`
12. `docs/ingestao/CONTRATO_DATASET_OFICIAL_COTAHIST_V1.0.md`
13. `docs/ingestao/CONTRATO_NORMALIZED_ANUAL_COTAHIST_V2.0.md`
14. `docs/ingestao/COTAHIST_1986_CONTRATO_IDENTIDADE_K4_V1.0.md`
15. `docs/ingestao/PARTE01_ROTINA_ATUALIZACAO_DIARIA_COTAHIST_V1.1.md`
16. `docs/ingestao/REGRAS_PERMANENTES_INGESTAO_HISTORICA_B3_V1.0.md`
17. `docs/ingestao/RUNBOOK_MIGRACAO_GIT_LFS_COTAHIST_A1987_V1.md`

### Conclusões semânticas confirmadas nesta etapa

- **Carta Magna:** a secção 2 já expressa a autoridade constitucional da Carta e o domínio operacional do Layout. A redação histórica posterior sobre ordem de correção deve ser lida como sequência de processo, não como precedência constitucional.
- **Layout Mestre:** a secção 2.2 foi corrigida para autoridade por domínio, reconciliação versionada e bloqueio limitado à decisão afetada. Versão 1.2.0.
- **Cartas de Confiança e Garantias e Modelo de Governança:** a linguagem de prevalência do Layout é válida para regras executáveis, mas não concede ao Layout autoridade para anular princípios constitucionais nem evidência factual externa. As cartas continuam em revisão até inspeção integral das demais secções.
- **Contratos técnicos e runbooks:** as cláusulas que remetem divergências operacionais ao Layout são compatíveis quando limitadas à execução. A revisão de cada contrato deve preservar as regras específicas de fase e não pode retrocertificar fases, alterar RAW ou modificar evidências históricas.
- **Política COTAHIST:** mantém-se a regra temporal: 1986–2025 apenas consulta/read-only; 2026 com atualização incremental diária. A decisão de hierarquia não certifica dados nem reabre anos encerrados.
- **Contrato NORMALIZED V2.0 e Dataset Oficial V1.0/V2.0:** estado de adoção e precedência de versão continuam a exigir evidência específica; GOV-DIV-001 não resolve esses temas.


### 3.1 Resultado das correções GOV-DIV-001 — 2026-10-16

- A cadeia de autoridade legada foi alinhada nos 17 cabeçalhos para `CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS`.
- A hierarquia universal da secção 3 do `MODELO_GOVERNANCA_PARA_PROJETOS.md` foi substituída por autoridade por domínio, com distinção explícita entre normas, contratos, implementação e evidência factual.
- O aditivo de 2026-10-01 da Carta Magna foi qualificado como histórico/processual, sem autoridade para impor precedência universal e sob a regra GOV-DIV-001.
- Referências ao caminho do Layout Mestre foram corrigidas onde identificadas.
- Os estados de adoção do NORMALIZED V2.0, execução da rotina diária e migração Git LFS A1987 continuam pendências operacionais próprias; não reabrem a conclusão da revisão semântica documental.

## 4. Limites e ações ainda abertas

- [ ] Confirmar auditoria SHA-256 pós-alterações documentais, incluindo Layout v1.2.0 e matriz v1.2.0.
- [x] Revalidar os 17 documentos prioritários por domínio de autoridade, cadeia normativa, referências, estados/versões e limites entre política, contrato, implementação e evidência; resultado registado na matriz v1.2.0.
- [ ] Comprovar adoção do Dataset Oficial V1.0 ou NORMALIZED V2.0 por artefactos, manifestos e workflows em execução; não inferir adoção apenas pela existência de documentos.
- [ ] Confirmar por evidência o estado de adoção do contrato NORMALIZED V2.0.
- [ ] Reconciliar referências e estados de implementação dos contratos de fase sem reabrir nem reescrever execuções históricas.
- [x] Atualizar a matriz integral por ficheiro com o resultado da revalidação GOV-DIV-001.
- [ ] Reexecutar a auditoria canónica e preservar o resultado/artefacto de execução.

## 5. Salvaguardas

- A revisão documental não certifica COTAHIST, BDI, BVBG.028.02, dados de mercado ou workflows.
- COTAHIST 1986–2025 permanece read-only; 2026 mantém atualização diária.
- Não alterar RAW, datasets, manifestos ou evidências de máquina para resolver divergências documentais.
- BLOOMBERG_MAIL permanece isolado e fora do âmbito B3.
- Relatórios dos Lotes 01–04 são snapshots históricos; esta revalidação é um aditivo posterior, não uma substituição retroativa.

## 6. Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-16 | Regista revalidação pós GOV-DIV-001, correção do Layout Mestre e estado residual sem declarar fecho global. | Commits do Layout; relatórios dos Lotes 01–04; matriz integral |
