# Revisão semântica documental — Lote 21: encerramento histórico 1986 e arquitetura NORMALIZED

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-021 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; HISTORICO_PRESERVADO; CONTRATOS_V1_V2_RECONCILIADOS_POR_VERSAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão documental; não reabre fases históricas |
| **Origem** | Inspeção de 15 documentos de FASE09/FASE10A e persistência anual |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | RAW → NORMALIZED → CERTIFICAÇÃO FÍSICA → DATASET OFICIAL → EVIDÊNCIA |
| **Escopo** | Investigação K4/BDI de 1986, arquitetura NORMALIZED, migração 1987 e Dataset Oficial V1/V2 |
| **Objetivo** | Distinguir encerramento operacional de causa histórica não resolvida e snapshots de migração de estado atual |
| **Dependências** | Contratos Dataset Oficial V1.0/V2.0, NORMALIZED anual V2.0, evidências físicas e roadmap atual |

## 1. Resultado executivo

Foram revistos 15 documentos. A FASE09C declara o caso 1986 encerrado operacionalmente, sem resolver a causa histórica da colisão K4; isso é coerente com a regra atual de manter 1986–2025 em consulta/read-only. O encerramento não afirma que o registo está errado nem autoriza correção.

Os documentos FASE10A foram escritos durante a migração de CSVs anuais para persistência física e certificação. Estados como “1987 não certificado”, “1986 próximo gate” e Dataset Oficial V1.0 descrevem snapshots de setembro. A documentação posterior de Dataset Oficial V2 e a decisão do projeto de encerrar anos anteriores a 2026 para consulta têm precedência temporal; os relatórios antigos permanecem úteis como histórico de arquitetura, não como instrução corrente.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/FASE09A_COTAHIST_1986_MATRIZ_COMPARATIVA_BDI_COTAHIST_V1.0.md | Comparação BDI × COTAHIST | Suporta multiplicidade por Tipo com mesmo Prazo em publicação de 05/06/1986, mas não identifica o Tipo das linhas Vigor de 10/10. | Citação temporária deve ser substituída por fonte persistente; causa K4 permanece não resolvida. |
| docs/ingestao/FASE09B_COTAHIST_1986_MULTIPLICIDADE_TERM_V1.0.md | Teste de multiplicidade sobre RAW integral | Diferencia K4 diferente de K4 idêntica com estatísticas diferentes; não aplica correção semântica. | Preservar o resultado no universo e hash indicados; não generalizar para outros universos sem evidência. |
| docs/ingestao/FASE09C_BDI_SEGMENTO_BOVESPA_ARQUEOLOGIA_ARQUIVO_V1.0.md | Pesquisa de nomenclatura de arquivo BDI | Identifica nome/canal histórico, mas confirma que o BDI 10/10/1986 e os identificadores alvo não foram recuperados. | Não confundir a identificação do canal com recuperação do arquivo. |
| docs/ingestao/FASE09C_COTAHIST_1986_BUSCA_PRIMARIA_BDI_10101986_V1.0.md | Busca primária | Mantém a busca aberta e exige a tabela literal, cabeçalhos e notas quando a fonte for recuperada. | Não inferir causa nem declarar fonte localizada sem artefacto persistido. |
| docs/ingestao/FASE09C_COTAHIST_1986_RECONSTRUCAO_REGRA_BDI_V1.0.md | Reconstrução de regra de publicação | Converge que a evidência decisiva é o BDI de 10/10/1986; não aceita a hipótese de dimensão ausente como fato. | Manter a regra histórica como não demonstrada. |
| docs/ingestao/FASE09C_DECISAO_DE_ENCERRAMENTO_1986_V1.0.md | Decisão de encerramento operacional | Encerra o caso como não bloqueante para ingestão, preservando a causa histórica não resolvida e RAW intacto. | Coerente com consulta/read-only; não significa resolução semântica definitiva. |
| docs/ingestao/FASE09_COTAHIST_1986_RECONSTRUCAO_BDI_K4_V1.0.md | Contrato de investigação FASE09 | Separa dimensão preservada, dimensão publicada e hipótese não demonstrada. | FASE09 permanece aberta semanticamente até fonte primária; não alterar as duas linhas. |
| docs/ingestao/FASE10A_AUDITORIA_ARQUITETURA_NORMALIZADA_V1.0.md | Auditoria arquitetural histórica | Identifica que a certificação não garantia persistência física do CSV e deixa decisão de armazenamento pendente no snapshot de 27/09. | Preservar como histórico; a migração V2 e o estado atual devem ser referenciados separadamente. |
| docs/ingestao/FASE10A_AUDITORIA_PRODUTOR_NORMALIZACAO_COTAHIST_V1.0.md | Auditoria do produtor NORMALIZED | Confirma que o parser recebe RAW e saída por argumento e que o processo é determinístico sob parser versionado. | Não confundir determinismo do parser com integridade/semântica de todos os anos. |
| docs/ingestao/FASE10A_M1_PERSISTENCIA_NORMALIZED_1987_V1.0.md | Prova de persistência de 1987 | Define critérios de RAW, NORMALIZED, SHA, validação, persistência e manifesto; a ordem de não migrar em massa antes de M2 é histórica. | Não usar a proibição antiga como estado atual sem reconciliar com V2; não reprocessar 1987 por este relatório. |
| docs/ingestao/FASE10A_M2_CERTIFICACAO_FISICA_1987_V2.0.md | Certificação física de 1987 | Estabelece que certificação exige CSV físico, manifesto e hashes; declara o escopo restrito ao ano de 1987. | Evidência limitada ao ano/commit da prova; não certifica automaticamente todos os anos. |
| docs/ingestao/FASE10A_M2_DATASET_OFICIAL_FISICO_V2.0.md | Integração física Dataset Oficial V2 | Exige RAW + NORMALIZED físico + QUALITY + certificação física antes de publicar. | Coerente como contrato V2; não usar status de setembro como estado corrente. |
| docs/ingestao/FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md | Plano de migração em lotes | Descreve migração controlada e gates físicos, mas contém estados “1987 não certificado/1986 próximo gate” de 28/09. | Snapshot histórico supersedido para estado corrente; preservar sem reescrever. |
| docs/ingestao/FASE10A_RECONCILIACAO_DATASET_OFICIAL_V1.0.md | Reconciliação de Dataset Oficial V1 | Expõe a inconsistência de declarar ficheiros anuais sem garantir existência física e identifica a diferença entre V1.0 e V1.1. | Não usar V1 como contrato atual sem reconciliação; a versão V2 deve governar os novos artefactos conforme decisão versionada. |
| docs/ingestao/FASE10_COTAHIST_1987_PLANO_V1.0.md | Plano histórico de validação 1987 | Define validação a partir de RAW e proíbe inventar dados; é um plano, não certificado de execução. | Preservar como plano histórico; anos pré-2026 continuam fechados para consulta no ciclo atual. |

## 3. Achados e decisões

### SEM-21-01 — encerramento operacional de 1986 não resolve a causa K4

A decisão FASE09C é explícita: a anomalia não bloqueia a ingestão histórica, mas a causa não foi resolvida documentalmente.

**Decisão:** preservar ambas as linhas e a exceção. A revisão documental não reabre a investigação nem altera dados.

### SEM-21-02 — Dataset Oficial V1.0 versus V2.0

Os documentos V1.0 registam a inconsistência histórica entre catálogo de arquivos e existência física dos CSVs. O contrato V2.0 acrescenta o gate de persistência física e certificação. Estes textos devem ser tratados como versões distintas, não fundidos num contrato ambíguo.

**Decisão:** V2.0 é a referência para a cadeia física atual, conforme as decisões e evidências posteriores; V1.0 permanece histórico.

### SEM-21-03 — certificação por ano não é transferência automática

A prova de 1987 valida apenas o ano e os artefactos explicitamente citados. Não autoriza copiar a certificação para todos os anos.

### SEM-21-04 — fontes temporárias

A FASE09A usa marcador temporário de pesquisa para fonte histórica. A referência deve ser persistente antes de o documento ser usado como evidência formal externa.

## 4. Conclusão

O conteúdo dos 15 documentos foi revisto. O caso K4 de 1986 permanece encerrado operacionalmente como exceção histórica, sem causa económica definitiva. Os documentos de migração V1/V2 foram classificados pela versão e data, evitando conflito artificial entre snapshots.

COTAHIST 1986–2025 permanece somente para consulta/read-only; 2026 mantém atualização diária.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Contrato NORMALIZED anual V2.0](CONTRATO_NORMALIZED_ANUAL_COTAHIST_V2.0.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
