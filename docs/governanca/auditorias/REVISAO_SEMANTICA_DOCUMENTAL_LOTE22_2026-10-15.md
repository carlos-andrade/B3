# Revisão semântica documental — Lote 22: incidências e gates de armazenamento NORMALIZED

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-022 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; INCIDENTES_HISTORICOS_PRESERVADOS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 8f8525648dbcf3a589e920b2ee4bc8a95e82b4ed4d23812a2fd277daae95f886 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão documental; não altera a decisão de armazenamento já registada |
| **Origem** | Inspeção de nove documentos de incidências e gates M3 |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | RAW → NORMALIZED FÍSICO → SHA → QUALITY → CERTIFICAÇÃO → DATASET OFICIAL |
| **Escopo** | Incidentes de sidecar/LFS e gates M3-0/M3-1B–M3-1E |
| **Objetivo** | Distinguir incidentes encerrados de snapshots de gate e evitar reabrir anos históricos |
| **Dependências** | Manifests, sidecars, Git LFS, Dataset Oficial V2 e auditoria física anual |

## 1. Resultado executivo

Foram revistos nove documentos. A incidência do sidecar de 1998 regista correção e auditoria física posterior aprovada para 41/41 anos, sem falhas no universo e execução citados. A incidência Git LFS de 1987 regista migração controlada e preservação do conteúdo RAW/NORMALIZED. Estes são incidentes de representação/integridade e não autorizam inferir correção semântica de todos os anos.

Os documentos M3 de 28/09 descrevem a decisão de armazenamento Git LFS e os gates do NORMALIZED 2026. Os seus estados de 1986/1987 e hashes de 22/09 são históricos; não devem ser confundidos com a atualização de 2026 até 13/10 documentada posteriormente. A aprovação M3-1E refere-se à infraestrutura e Dataset Oficial de 2026, não à certificação semântica integral de 1986–2026.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/INCIDENCIA_COTAHIST_1998_SIDECAR_SHA256_2026-10-14.md | Incidente de integridade encerrado | Distingue sidecar divergente de conteúdo CSV/RAW e regista que a auditoria física posterior aprovou 41/41 anos. | Preservar evidência e hashes; não inferir certificação semântica completa a partir da auditoria física. |
| docs/ingestao/INCIDENCIA_GIT_LFS_COTAHIST_A1987_2026-10-14.md | Incidente de representação LFS | Regista migração de representação, preservação de conteúdo e fechamento técnico com aprovação formal pendente. | Manter estado de aprovação formal distinto de conclusão técnica; não reescrever histórico. |
| docs/ingestao/M3-0_RESULTADO_GATE_CAPACIDADE_NORMALIZED_2026_2026-09-28.md | Resultado de gate de capacidade | O failure é esperado quando o CSV excede limite Git convencional; isso não significa falha de normalização. | Tratar como prova de limite de armazenamento, não defeito de dados. |
| docs/ingestao/M3-1B_RECONCILIACAO_MANIFEST_NORMALIZED_2026_2026-09-28.md | Reconciliação histórica de manifest | Explica divergência de hashes por mudança posterior do RAW e reconstrução; os hashes citados pertencem ao snapshot de setembro. | Não usar esses hashes como atuais; consultar manifests posteriores. |
| docs/ingestao/M3-1B_RESULTADO_PROVA_LFS_2026_2026-09-28.md | Prova física LFS | Regista materialização física e integridade para NORMALIZED 2026 no run citado, mas não concedeu aprovação global então. | Escopo limitado ao run e artefactos citados; não extrapolar para anos ou versões posteriores. |
| docs/ingestao/M3-1C_CI_INTEGRIDADE_NORMALIZED_2026_V1.0.md | Gate CI de integridade | Exige presença, tracking LFS, SHA, validação semântica e reconstrução determinística. | Coerente como gate; o estado histórico de migração bloqueada não deve ser reutilizado sem a decisão posterior. |
| docs/ingestao/M3-1D_DATASET_OFICIAL_COTAHIST_2026_V1.0.md | Dataset Oficial 2026 — snapshot M3-1D | Declara validação do artefacto oficial e run específico. | Evidência do snapshot de setembro; a versão V2 posterior e atualização diária determinam o estado mais recente. |
| docs/ingestao/M3-1E_APROVACAO_GLOBAL_COTAHIST_2026_V1.0.md | Aprovação global do armazenamento 2026 | Aprova M3-1 para 2026 e ainda condiciona a migração histórica a gates semânticos de 1986. | Não interpretar como certificação semântica global nem como autorização para alterar anos fechados; preservar como decisão técnica histórica. |
| docs/ingestao/M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md | Decisão de armazenamento | Aprova Git LFS para CSV anual grande, com caminho lógico, SHA, CI e fail-closed. | A decisão técnica de armazenamento permanece distinta da política de retenção e da certificação de cada ano. |

## 3. Achados e decisões

### SEM-22-01 — integridade física e semântica são gates distintos

Sidecar, manifesto, CSV físico e RAW podem coincidir em hash sem que a semântica de cada linha esteja totalmente demonstrada. A auditoria 41/41 é estrutural/física dentro do universo testado.

### SEM-22-02 — M3-1E não é certificação semântica global

A aprovação global do M3-1 diz respeito à arquitetura de armazenamento e ao Dataset Oficial de 2026 no snapshot. Não autoriza inferir que cada ano esteja semanticamente certificado nem reabrir anos históricos.

### SEM-22-03 — estados de setembro foram supersedidos temporalmente

Os hashes e cortes de 22/09 ou o estado “1986 próximo gate” pertencem à execução histórica. A atualização posterior de 2026 até 13/10 e os contratos V2 devem ser consultados para o estado corrente.

### SEM-22-04 — incidentes encerrados não devem ser reabertos sem nova evidência

Os incidentes 1998 e LFS 1987 têm critérios de fechamento documentados. Uma falha nova exige incidente próprio com run, commit, causa e prova; não se altera retroativamente o incidente antigo.

## 4. Conclusão

O conteúdo dos nove documentos foi revisto. A representação física e o armazenamento são tratados separadamente da semântica; os incidentes encerrados permanecem históricos. A revisão não altera RAW, NORMALIZED ou manifestos.

COTAHIST 1986–2025 permanece somente para consulta/read-only; 2026 mantém atualização diária.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Incidência LFS A1987](INCIDENCIA_GIT_LFS_COTAHIST_A1987_2026-10-14.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
