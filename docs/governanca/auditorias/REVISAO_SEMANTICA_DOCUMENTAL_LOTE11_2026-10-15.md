# Revisão semântica documental — Lote 11: catálogo de ativos e classificação estrutural

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-011 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; MAPEAMENTO_OFICIAL_SCTYCTGY_PENDENTE |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação metodológica e da fonte oficial |
| **Origem** | Inspeção de 15 documentos de catálogo, inventário, classificação e fontes |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | FONTE OFICIAL → RAW → CLASSIFICAÇÃO ESTRUTURAL → VALIDAÇÃO → PUBLICAÇÃO |
| **Escopo** | README de classes de ativos, catálogo BVBG.028.02, snapshots, CFI e SctyCtgy |
| **Objetivo** | Separar classificação estrutural de classificação oficial e impedir inferências económicas não sustentadas |
| **Dependências** | BVBG.028.02, ExternalSecurityCategoryCode, taxonomia B3 vigente, manifestos e auditoria de catálogo |

## 1. Resultado executivo

Foram revistos 15 documentos. Os textos estabelecem corretamente que o cadastro oficial BVBG.028.02 é a origem do inventário, que snapshots de setembro são temporais, que categorias estruturais derivadas de AsstDesc/CFICd/OptnTp/XprtnDt/Undrlyg/SgmtNm/MktNm não equivalem automaticamente a classificação oficial da B3 e que códigos históricos de SctyCtgy não substituem a lista vigente.

A pendência de conteúdo mais relevante continua aberta: a lista oficial atual de ExternalSecurityCategoryCode/SctyCtgy ainda não foi capturada e validada integralmente. Até isso ocorrer, não inferir mapeamentos ausentes nem converter categorias estruturais em categorias oficiais. A contagem de instrumentos não é proxy de liquidez, negociabilidade ou qualidade económica.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| ativos/README.md | Índice do domínio de ativos | Define o catálogo como documentação de ativos e remete para regras de integridade e autoridade. | Tratar como navegação; não como prova de listagem atual de qualquer instrumento. |
| ativos/acoes/README.md | README de classe de ativos | Delimita a classe ações e identifica o catálogo/fonte de origem. | Os instrumentos efetivos devem vir do cadastro oficial e da captura com evidência. |
| ativos/balcao/README.md | README de classe de mercado | Delimita instrumentos registados/negociados em balcão organizado. | Não inferir equivalência com ações listadas; respeitar classificação e fonte específica. |
| ativos/bdrs/README.md | README de classe de ativos | Delimita BDRs no domínio de ativos. | A presença da pasta não prova existência, status vigente ou negociabilidade de qualquer BDR. |
| ativos/catalogo/INVENTARIO_B3_2026-09-21.md | Snapshot de inventário | Identifica BVBG.028.02 e descreve o processamento da captura. A data de referência é 21/09/2026. | Preservar como snapshot; consultar o catálogo mais recente para o estado corrente. |
| ativos/catalogo/PROTOCOLO_CAPTURA.md | Protocolo operacional de captura | Define sequência de captura, hash, detecção de duplicados e persistência. | Exigir RAW, hash, fonte, timestamp e validação; ausência ou erro deve bloquear promoção. |
| ativos/catalogo/README.md | Contrato de navegação do catálogo | Define BVBG.028.02 como fonte e rejeita listas manuais/tickers inventados. | Manter o catálogo ligado à fonte oficial; não assumir que estrutura planejada já está toda implementada. |
| ativos/catalogo/classificacao/ESTATISTICAS_CLASSIFICACAO_B3_2026-09-22.md | Estatística de snapshot | Estado explicitamente HISTORICO, data 22/09/2026 e aprovação metodológica pendente. | Usar apenas como estatística temporal; não reportar como contagem corrente. |
| ativos/catalogo/classificacao/README.md | Metodologia de classificação estrutural | Distingue OFICIAL_B3 de ESTRUTURAL e aponta atributos do cadastro usados para inferência. | Manter rótulos de confiança e fonte; não promover inferência a classe oficial. |
| ativos/catalogo/classificacao/REGRAS_CLASSIFICACAO_ESTRUTURAL_2026-09-23.md | Regras de classificação | Declara que categorias inferidas não equivalem a classificação oficial B3. | Aplicar apenas a campos presentes e regras documentadas; mapeamentos ausentes permanecem UNKNOWN/PENDENTE. |
| ativos/catalogo/estatisticas/ANALISE_ESTRUTURAL_BVBG028_2026-09-22.md | Análise quantitativa de snapshot | Separa fatos, hipótese controlada e inferência ainda não autorizada. | Preservar a separação epistemológica; não inferir liquidez, profundidade ou atividade a partir da cardinalidade do cadastro. |
| ativos/catalogo/fontes/EVIDENCIA_VIGENTE_SCTYCTGY_2026-09-23.md | Evidência de fonte | Declara que a correspondência vigente completa ainda não foi capturada. | A pendência é real; obter lista oficial atual antes de afirmar cobertura completa. |
| ativos/catalogo/fontes/NOTA_CLASSIFICACAO_CFI_SCTYCTGY_2026-09-23.md | Nota de classificação técnica | Distingue documentação B3, estrutura ISO CFI e necessidade de lista B3 vigente. | CFI ajuda a descrever estrutura, mas não substitui a taxonomia oficial B3 nem prova direitos de negociação. |
| ativos/catalogo/fontes/NOTA_FONTE_B3_2026-09-23.md | Nota de fonte oficial | Regista mudança nas antigas páginas públicas e aponta o BDI como canal de publicação de dados anteriormente disponíveis. | Verificar a página oficial na data de cada captura; preservar esta nota como evidência datada. |
| ativos/catalogo/fontes/REFERENCIA_HISTORICA_SCTYCTGY_2026-09-23.md | Referência histórica | Identifica explicitamente que a definição histórica de 2013 não representa a lista vigente. | Não usar como fonte autoritativa para mapeamentos atuais. |

## 3. Achados e decisões

### SEM-11-01 — taxonomia oficial incompleta

O documento de evidência vigente declara que a correspondência completa de SctyCtgy ainda não foi capturada. Este é um bloqueador de classificação oficial completa, não uma lacuna a preencher por inferência.

**Ação:** capturar a lista oficial atual de ExternalSecurityCategoryCode, preservar fonte/versão/data/hash e construir mapeamento explícito com cobertura, códigos desconhecidos e testes. Até lá, manter valores desconhecidos como UNKNOWN/PENDENTE.

### SEM-11-02 — snapshots históricos

Os inventários e estatísticas de 21–23/09/2026 são snapshots. A data de atualização do documento em outubro não muda a data de referência do conteúdo.

**Decisão:** preservar os snapshots; usar a captura BVBG.028.02 mais recente e sua evidência para números correntes.

### SEM-11-03 — classificação não é liquidez

A contagem de registos, categorias ou instrumentos no cadastro descreve o universo de identificação, não o volume negociado, spread, profundidade, turnover ou possibilidade atual de negociação.

**Decisão:** proibir inferência de liquidez a partir de cardinalidade do catálogo. Métricas de liquidez exigem dados de mercado adequados, período, unidade e fonte independentes.

### SEM-11-04 — CFI e SctyCtgy têm papéis distintos

CFI fornece uma classificação estruturada de instrumento; SctyCtgy/ExternalSecurityCategoryCode corresponde à taxonomia específica da fonte B3. Não se deve deduzir uma correspondência completa entre ambas sem tabela oficial e validação.

## 4. Conclusão

O conteúdo dos 15 documentos foi revisto. O catálogo e as regras de classificação preservam a distinção entre fonte oficial, snapshot e inferência estrutural. A classificação oficial completa permanece pendente da lista vigente ExternalSecurityCategoryCode.

COTAHIST 1986–2025 continua somente para consulta; 2026 mantém atualização diária. Não foram alterados dados RAW, datasets ou manifestos.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
