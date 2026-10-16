# Revisão semântica documental — Lote 27: reconciliação residual e estado corrente

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-027 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Reconciliação final da revisão de conteúdo |
| **Estado** | REVISAO_SEMANTICA_CONCLUIDA; EXCECOES_OPERACIONAIS_CONTROLADAS; HASH_POS_COMMIT_PENDENTE |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 63d3fe5a5f06efcf0490068ebf7e8bad7a4d92ded0388b90aa0abafd25619520 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — relatório de revisão; não aprova alterações operacionais nem dados |
| **Origem** | Revalidação de 17 documentos após GOV-DIV-001, quatro relatórios históricos, a própria decisão e duas páginas Wiki |
| **Autoridade superior** | [Carta Magna B3](../../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | 24 registos residuais: 17 documentos revalidados, quatro relatórios históricos, decisão GOV-DIV-001 e duas páginas Wiki |
| **Objetivo** | Fechar a fila de revisão de conteúdo sem confundir revisão documental, integridade criptográfica e aceitação operacional |
| **Dependências** | Matriz integral, auditoria SHA-256 pós-commit, Issue #11 e evidências de GitHub Actions |

## 1. Resultado executivo

Foram reavaliados os 17 documentos anteriormente marcados para revalidação após GOV-DIV-001, os quatro relatórios dos Lotes 01–04, a própria decisão e duas páginas Wiki. A decisão normativa separa competência constitucional, especificação operacional, contratos e implementação; conflitos adicionais não são resolvidos por extensão automática de GOV-DIV-001 e exigem IDs próprios.

A fila original de 281 documentos pendentes está revista. A matriz integral controla 303 ficheiros Markdown e associa cada registo a uma classe, um estado e um lote de evidência. O fecho semântico foi reconciliado, mas **não significa aprovação formal, certificação de dados, licença de redistribuição ou aceitação operacional**.

## 2. Documentos revalidados

### 2.1 Normas e contratos — 17

- `docs/CARTA_DE_CONFIANCA_DOS_DADOS.md`
- `docs/CARTA_DE_GARANTIAS_DO_PROJETO_B3.md`
- `docs/CARTA_MAGNA_GOVERNANCA_B3.md`
- `docs/MODELO_GOVERNANCA_PARA_PROJETOS.md`
- `docs/cotahist/CONTRATOS_EVIDENCIA_FASES_06_09_V1.md`
- `docs/cotahist/CONTRATO_EVIDENCIA_FASES_00_09_V1.md`
- `docs/cotahist/CONTRATO_EXECUCAO_SEQUENCIAL_FASES_COTAHIST_V1.md`
- `docs/cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md`
- `docs/governanca/CONTRATO_RETORNO_E_MONITORAMENTO_EXECUCOES_B3_V1.md`
- `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`
- `docs/governanca/politicas/POLITICA_RETENCAO_COTAHIST_1986_2026_V1.md`
- `docs/ingestao/CONTRATO_DATASET_OFICIAL_COTAHIST_V1.0.md`
- `docs/ingestao/CONTRATO_NORMALIZED_ANUAL_COTAHIST_V2.0.md`
- `docs/ingestao/COTAHIST_1986_CONTRATO_IDENTIDADE_K4_V1.0.md`
- `docs/ingestao/PARTE01_ROTINA_ATUALIZACAO_DIARIA_COTAHIST_V1.1.md`
- `docs/ingestao/REGRAS_PERMANENTES_INGESTAO_HISTORICA_B3_V1.0.md`
- `docs/ingestao/RUNBOOK_MIGRACAO_GIT_LFS_COTAHIST_A1987_V1.md`

**Resultado:** a hierarquia por domínio de GOV-DIV-001 é compatível com a separação entre autoridade normativa, contratos, implementação e evidência. Estados editoriais `EM_REVISAO` e aprovadores pendentes foram preservados quando não existia autorização para promovê-los. A revisão não altera RAW, manifestos, artefactos históricos nem estado de execução de workflows.

### 2.2 Relatórios históricos — quatro

- [Lote 01](REVISAO_SEMANTICA_DOCUMENTAL_LOTE01_2026-10-15.md)
- [Lote 02](REVISAO_SEMANTICA_DOCUMENTAL_LOTE02_2026-10-15.md)
- [Lote 03](REVISAO_SEMANTICA_DOCUMENTAL_LOTE03_2026-10-15.md)
- [Lote 04](REVISAO_SEMANTICA_DOCUMENTAL_LOTE04_2026-10-15.md)

**Resultado:** os quatro relatórios foram reexaminados como snapshots históricos. Os estados parciais e os próximos passos neles descritos são verdadeiros para a data original; não devem ser reescritos retroativamente para fingir que GOV-DIV-001 já existia. A matriz regista a revalidação posterior por este lote.

### 2.3 Outros registos — três

- [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md): critério de revisão semântica integral atualizado; auditoria SHA-256 pós-commit ainda pendente.
- [Estado Atual da Wiki](../../WIKI/00-INICIO/ESTADO_ATUAL.md): corrigido para a data de referência 2026-10-16, com evidências de execução e pendências reais.
- [Índice da Wiki](../../WIKI/README.md): aponta para o estado corrente e esclarece que a Wiki não substitui normas/contratos.

## 3. Decisões e limites

### DEC-27-01 — GOV-DIV-001 aplicado por domínio

A Carta Magna conserva autoridade constitucional; o Layout Mestre é a especificação operacional; cartas/políticas de domínio são reconciliadas com ambos; contratos concretizam as regras; procedimentos e workflows implementam-nas. Conflitos adicionais exigem IDs próprios e não são resolvidos por extensão automática desta decisão.

### DEC-27-02 — execução de workflows é evidência delimitada

A auditoria estática de workflows concluiu com sucesso no [run 38872342723](https://github.com/carlos-andrade/B3/actions/runs/38872342723), auditando 553 workflows. Isto é evidência de execução do auditor, não certificação funcional dos dados de mercado.

### DEC-27-03 — exceções operacionais permanecem abertas

- Proveniência RAW COTAHIST: revisão independente pendente.
- Taxonomia oficial `ExternalSecurityCategoryCode/SctyCtgy`: captura completa vigente pendente.
- WATCHDOG: heartbeat externo, ACK/escalonamento, retenção duradoura e aprovação humana dos limiares pendentes.
- COTAHIST 1986–2025 permanece read-only; 2026 mantém atualização diária.
- `BLOOMBERG_MAIL` permanece isolado e fora do âmbito B3.
- A auditoria SHA-256 pós-commit é o próximo gate; nenhum hash é considerado validado apenas por cálculo local.

## 4. Conclusão

A revisão de conteúdo dos 303 documentos inventariados está registada, incluindo a fila original de 281 pendências. A validação criptográfica posterior aos commits e a aceitação operacional continuam gates separados. As exceções são explícitas e não foram ocultadas para obter um estado artificialmente verde.

## 5. Referências

- [Matriz integral de revisão semântica](MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Plano Mestre de Execução](../../PLANO_MESTRE_DE_EXECUCAO.md)
- [Auditoria de workflows atual](WORKFLOWS_CONFORMIDADE_B3_ATUAL.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
