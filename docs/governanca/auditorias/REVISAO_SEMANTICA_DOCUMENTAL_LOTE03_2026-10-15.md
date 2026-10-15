# Revisão semântica documental — Lote 03

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-003 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Classificação semântica e reconciliação |
| **Estado** | REVISAO_PARCIAL; METADADOS_LEGADOS_PENDENTES |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 8edcc3d7a1f8390e3db1df2d867e4210b0b56d3ccfbeb8acbcd7f1fec18ba21a |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente de aprovação específica |
| **Origem** | Inspeção direta dos três contratos-fonte e norma GOVERNANCA v1.0.3 |
| **Autoridade superior** | [Norma GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) |
| **Cadeia de autoridade** | CONTRATOS DE DADOS → LAYOUT MESTRE → IMPLEMENTAÇÃO → EVIDÊNCIAS → VALIDAÇÃO |
| **Escopo** | Contratos de seleção do Dataset Oficial, persistência NORMALIZED e identidade COTAHIST 1986 |
| **Objetivo** | Identificar o domínio de cada contrato e sinalizar pontos de reconciliação sem modificar as regras técnicas |
| **Dependências** | RAW, NORMALIZED, manifests, certificação, Dataset Oficial e evidências de identidade |

## 1. Resultado executivo

Foram inspecionados três contratos de ingestão/identidade. Os conteúdos têm responsabilidades distintas e devem ser mantidos como contratos específicos. Todos usam metadados legados em texto corrido em vez da tabela canónica GOVERNANCA. Não foram alterados os contratos nem os dados. Foram registados dois pontos de atenção: a V2.0 do contrato NORMALIZED está identificada no cabeçalho como proposta técnica aguardando implementação controlada, e o contrato do Dataset Oficial V1.0 descreve critérios que devem ser comparados com o Dataset Oficial V2.0 atualmente referenciado noutros documentos. Não se infere que exista divergência efetiva sem comparação integral.

## 2. Matriz

| Documento | Classificação | Fatos observados | Ação |
|---|---|---|---|
| [Contrato Dataset Oficial COTAHIST V1.0](../../ingestao/CONTRATO_DATASET_OFICIAL_COTAHIST_V1.0.md) | CONTRATO_SELECAO_DATASET | Define cadeia RAW → normalização → quality manifest → certificação anual → Dataset Oficial → aplicações; contém critérios de inclusão e exceções 1986/2026. | Comparar com o contrato/manifesto oficial V2.0 e mapear precedência de versões; não presumir que V1.0 continua a governar a versão V2.0. |
| [Contrato NORMALIZED Anual COTAHIST V2.0](../../ingestao/CONTRATO_NORMALIZED_ANUAL_COTAHIST_V2.0.md) | CONTRATO_PERSISTENCIA_NORMALIZED | Declara V2.0 como proposta técnica aguardando implementação controlada; especifica persistência anual e fail-closed para ausências/integridade. | Confirmar estado real de implementação e decisão de adoção por evidência/commit antes de alterar `PROPOSTA TÉCNICA`. |
| [Contrato Identidade K4 COTAHIST 1986](../../ingestao/COTAHIST_1986_CONTRATO_IDENTIDADE_K4_V1.0.md) | CONTRATO_IDENTIDADE_HISTORICA | Regista colisão K4 não idêntica, separando identidade contratual, identidade física RAW e observação económica; proíbe deduplicar RAW por K4. | Preservar como contrato de exceção histórica controlada; normalizar metadados sem alterar conclusões de identidade nem valores quantitativos. |

## 3. Pontos de reconciliação

### GOV-DATASET-VERSAO-001 — V1.0 versus Dataset Oficial V2.0

**Fato:** o contrato V1.0 aponta para `COTAHIST_DATASET_OFICIAL_V1.0.json`, enquanto [FASE10A M2 — Integração física com Dataset Oficial COTAHIST V2.0](../../ingestao/FASE10A_M2_DATASET_OFICIAL_FISICO_V2.0.md) especifica a V2 e está marcada `IMPLEMENTADO — PUBLICAÇÃO BLOQUEADA ATÉ M3`. A V2 exige NORMALIZED físico e certificação física; a publicação global continua bloqueada até M3. Trata-se de evolução de versão com condições de publicação explícitas, não de prova de incompatibilidade.

**Ação:** mapear formalmente V1.0 (contrato histórico) → FASE10A M2/V2.0 (contrato físico) → workflow V2 e Dataset Oficial V2.0. Comparar critérios, estados, 1986, atualização de 2026 e congelamento de 1986–2025; preservar o bloqueio de publicação global enquanto M3 não autorizar.

### GOV-NORMALIZED-ESTADO-001 — proposta técnica versus implementação

**Fato:** o cabeçalho do contrato NORMALIZED V2.0 diz `PROPOSTA TÉCNICA — AGUARDANDO IMPLEMENTAÇÃO CONTROLADA` e o corpo exige persistência permanente de CSVs certificados. O projeto tem artefactos NORMALIZED persistidos, mas a existência desses artefactos não prova que a V2.0 tenha sido formalmente adotada.

**Ação:** verificar registo de aprovação/adoção e workflows relevantes. Não alterar o estado documental por inferência.

## 4. Salvaguardas

- COTAHIST 1986–2025 permanece fechado para ingestão rotineira; não alterar RAW, NORMALIZED, manifests ou evidências históricos nesta revisão.
- COTAHIST 2026 continua sujeito a atualização incremental diária.
- Não deduplicar RAW 1986 com base em K4; manter distinção entre contrato e observação económica.
- Nenhuma aprovação ou certificação é inferida.
- Hashes canónicos deste relatório e dos contratos continuam pendentes de cálculo independente.

## 5. Próximos passos

1. Consolidar o mapa de precedência entre contrato V1.0, FASE10A M2/V2.0, workflow V2 e manifesto oficial.
2. Verificar evidência formal de adoção do contrato NORMALIZED V2.0.
3. Continuar a revisão de contratos de dados restantes, mantendo as regras técnicas intactas.
4. Após fechar a classificação semântica, normalizar cabeçalhos em lotes controlados e calcular hashes por ferramenta reprodutível.

## 6. Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-15 | Revisão semântica de três contratos de ingestão/identidade | Inspeção direta dos documentos-fonte |
