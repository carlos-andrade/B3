# Revisão semântica documental — Lote 17: certificação estrutural e atualidade COTAHIST

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-017 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; SNAPSHOTS_DE_2026_PRESERVADOS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 68863ff2769dc08accbcd0df105d0397d39608a0a76e33346911fb11ddb915d0 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão documental; não substitui auditoria técnica atual |
| **Origem** | Inspeção de 10 documentos de certificação anual, continuidade, calendário e promoção |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | RAW → NORMALIZED → MANIFESTO → FASES → AUDITORIA INDEPENDENTE → CERTIFICAÇÃO |
| **Escopo** | Certificação anual, resultado de auditoria V2, fases 09–11 de 2026, continuidade, calendário e falhas de normalização V4 |
| **Objetivo** | Separar fotografia histórica de evidência corrente e confirmar os limites da certificação estrutural |
| **Dependências** | Manifests atuais, qualidade JSON, auditoria pós-promoção Parte23 e runs oficiais |

## 1. Resultado executivo

Foram revistos dez documentos. A documentação distingue, corretamente, certificação estrutural de certificação semântica histórica completa, e a auditoria integrada pós-promoção de 2026 reconhece que fez leitura cruzada de evidências persistidas, não nova leitura byte a byte do CSV inteiro. A auditoria V2 de setembro e o diagnóstico V4 também são snapshots históricos.

Os documentos antigos de FASE09/10/11 contêm estados anteriores (dataset até 23/09 ou candidato ainda pendente) que foram supersedidos pela auditoria integrada pós-promoção Parte23 de 14/10, que regista dataset até 13/10, hashes e FASE11 concluída com exceções documentadas. Os estados antigos não devem ser usados como status corrente nem reescritos para fingir que o resultado posterior já existia.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/CERTIFICACAO_ANUAL_COTAHIST_1986_2026_V1.0.md | Modelo/matriz de certificação estrutural | Declara critérios explícitos (RAW, manifesto, parser homologado, 25 campos, qualidade) e limita a certificação a normalização estrutural. | Manter a ressalva semântica; atualizar matriz apenas após alteração validada de 2026. |
| docs/ingestao/COTAHIST_1986_2026_RESULTADO_AUDITORIA_V2.md | Auditoria estrutural histórica | Universo 1986–2026 e corte 23/09; distingue duplicidade exata de repetição de identidade e reconhece que gaps exigem calendário. | Preservar como snapshot de 24/09; não usar corte/contagens como atuais. |
| docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md | Auditoria histórica de atualidade | Já contém aviso explícito de estado histórico e aponta para Parte23. | Coerente; consultar auditoria pós-promoção para estado corrente. |
| docs/ingestao/COTAHIST_2026_FASE10_GATE_VALIDACAO_CANDIDATO_V1.md | Gate de candidato histórico | Estado candidato e NORMALIZED até 23/09 foram supersedidos pela atualização e promoção de 14/10. | Interpretar como histórico do candidato; não usar como estado operacional corrente. |
| docs/ingestao/COTAHIST_2026_FASE11_AUDITORIA_POS_PROMOCAO_PARTE23_V1.md | Auditoria integrada pós-promoção | Regista 3.142.910 registos, 25 campos, data até 13/10, hashes e limites da leitura cruzada. | É o snapshot mais recente neste conjunto, mas não substitui a atualização diária após 13/10 nem afirma leitura byte a byte nesta sessão. |
| docs/ingestao/COTAHIST_2026_FASE11_AUDITORIA_POS_PROMOCAO_V1.md | Auditoria pós-promoção anterior | Confirma promoção e hashes, mas identifica falha numa execução repetida e necessidade de idempotência. | Preservar como histórico; a auditoria Parte23 é a referência mais recente deste conjunto. |
| docs/ingestao/COTAHIST_2026_FASE11_REVISAO_E_PROMOCAO_V1.md | Nota de revisão FASE10/11 | Contém status antigo CANDIDATO e “execução não confirmada”, em conflito temporal com a promoção posterior. | Snapshot supersedido; nunca usar isoladamente como estado corrente. |
| docs/ingestao/COTAHIST_AUDITORIA_CONTINUIDADE_V2.md | Metodologia de continuidade | Regras de 245 bytes, calendário independente e tratamento de identidades múltiplas são metodologicamente coerentes. O estado “execução em andamento” é histórico. | Manter como metodologia; atualizar status de execução apenas em novo relatório/run. |
| docs/ingestao/COTAHIST_VALIDACAO_CALENDARIO_1986_2026.md | Contrato de validação de calendário | Proíbe declarar pregão ausente apenas pela diferença entre datas e exige calendário por ano e SHA da fonte. | Coerente; não declarar calendário completo sem fonte oficial e evidência por ano. |
| docs/ingestao/DIAGNOSTICO_COTAHIST_NORMALIZACAO_V4_2026-09-24.md | Diagnóstico de falha de workflow | Separa falha de publicação de artefactos de integridade dos dados e rejeita usar Actions como armazenamento permanente de CSVs grandes. | Preservar como diagnóstico histórico; não inferir corrupção RAW a partir de falha operacional. |

## 3. Achados e decisões

### SEM-17-01 — estados antigos de FASE09/10/11 são supersedidos

A FASE09 bloqueada, o candidato estruturalmente validado e a FASE11 não confirmada descrevem estados anteriores à atualização de 14/10. A auditoria integrada Parte23 regista a promoção posterior e assinala explicitamente a auditoria antiga como supersedida para estado atual.

**Decisão:** preservar todos os relatórios; consultar Parte23 e a evidência diária posterior para estado corrente. Não alterar retroativamente o resultado das execuções antigas.

### SEM-17-02 — certificação estrutural não é certificação semântica completa

A matriz anual certifica critérios estruturais e de qualidade; não elimina a exceção semântica histórica de 1986 nem prova a semântica completa de todos os anos.

**Decisão:** manter a distinção no dataset, roadmap e comunicações.

### SEM-17-03 — calendário exige fonte independente

O calendário oficial, as sessões por segmento e as exceções históricas são necessários para distinguir gaps naturais de pregões ausentes. Diferença de datas não basta.

**Decisão:** não promover uma ausência a falha de ingestão sem calendário oficial, data de referência e hash da fonte.

### SEM-17-04 — falha de workflow não prova corrupção de dados

Falhas de publicação de artefactos ou commits sem alterações não invalidam automaticamente RAW/NORMALIZED. Exigem inspeção de logs, estado remoto e hashes.

**Decisão:** preservar o diagnóstico e separar incidentes de persistência dos incidentes de dados.

## 4. Conclusão

O conteúdo dos dez documentos foi revisto. Os estados de setembro e início de outubro foram classificados como históricos; a auditoria integrada Parte23 é a referência mais recente neste conjunto para a promoção de 2026 até 13/10. A atualização de 14/10 não prova o estado diário posterior a esse corte.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Roadmap Mestre COTAHIST](../cotahist/ROADMAP_MESTRE_INGESTAO_COTAHIST_1986_2026_ESTADO_2026-10-14.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
