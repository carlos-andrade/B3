# Revisão semântica documental — Lote 25: Copom, BCB, IBGE e calendário económico

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-025 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; CAPTURA_RAW_E_RECONCILIACAO_INTRADAY_PENDENTES |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão documental; não valida independentemente os eventos macro |
| **Origem** | Inspeção de 15 contratos, fontes, reconciliações e estado de API |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | FONTE OFICIAL → RAW → TIMESTAMP DE DISPONIBILIDADE → NORMALIZED → SESSÃO B3 → ANÁLISE |
| **Escopo** | Copom 281, endpoints BCB, janelas de evento, calendário económico, IBGE e rota BDM |
| **Objetivo** | Separar evento macro confirmado de evidência bruta capturada e de reação de mercado observada |
| **Dependências** | API BCB, arquivo RAW, hashes, calendário IBGE e dataset B3 intraday autorizado |

## 1. Resultado executivo

Foram revistos 15 documentos. A metodologia temporal é coerente: data da reunião, decisão, vigência, publicação do comunicado, publicação da ata e horário de disponibilidade são campos distintos. O modelo no-lookahead está correto ao exigir informação disponível no instante de decisão e ao separar evento agendado de informação publicada.

A documentação, contudo, deixa explícito que a captura HTTP integral da Ata/Comunicado Copom 281 e o dataset intraday B3 não foram demonstrados nos snapshots de 24/09. Os arquivos Markdown de calendário/Copom não devem ser tratados como RAW original quando contêm apenas metadados, resumo ou lista de observações. As referências temporárias foram substituídas em dois documentos por links oficiais persistentes; isso não equivale a nova captura do conteúdo fonte.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/PARTE03_BCB_COPOM_281_COMUNICADO_RECONCILIACAO_V1.0.md | Reconciliação comunicado × B3 | Distingue decisão, vigência e publicação e mantém SHA da resposta integral pendente. | Não afirmar RAW capturado nem reação intraday observada sem arquivo e hash. |
| docs/ingestao/PARTE03_BCB_COPOM_281_RECONCILIACAO_V1.0.md | Reconciliação oficial da reunião | Regista datas, taxa e votos, mas reconhece ausência de captura HTTP integral neste ambiente. | Revalidar os factos na fonte oficial antes de novo uso; não inventar hash. |
| docs/ingestao/PARTE03_BCB_COPOM_API_ENDPOINTS_V1.0.md | Inventário de endpoints BCB | Lista endpoints de atas/comunicados e diferencia lista de detalhe. | Testar resposta válida e esquema em nova captura; endpoint identificado não significa documento persistido. |
| docs/ingestao/PARTE03_BCB_COPOM_AUDITORIA_V1.0.md | Auditoria inicial de eventos Copom | Eventos foram modelados a partir de fontes oficiais, mas a etapa seguinte requer RAW e hash. | Tratar a camada normalizada como inicial; não declarar reconciliação completa com B3. |
| docs/ingestao/PARTE03_BCB_COPOM_B3_JANELA_EVENTO_V1.0.md | Especificação de janela-evento | Define janelas pré/pós e instrumentos, com separação de horário do evento e sessão B3. | Janelas são desenho analítico; sem dataset primário não existem resultados observados. |
| docs/ingestao/PARTE03_BCB_COPOM_CONTRATO_V1.0.md | Contrato de ingestão Copom | Exige fontes oficiais, timestamp de informação e separação entre expectativa pré-evento e interpretação posterior. | Coerente; cada documento requer RAW e SHA antes de certificação. |
| docs/ingestao/PARTE03_BCB_COPOM_EVENTOS_2026_V1.0.md | Calendário de eventos Copom | Regista reuniões, comunicado, ata e RPM em calendário, sem inferir efeito de mercado. | Datas/horários são snapshot verificado em 24/09; revalidar mudanças/revisões antes de usar em backtest. |
| docs/ingestao/PARTE03_BCB_COPOM_FONTES_V1.0.md | Matriz de fontes oficiais | Distingue Copom, documentos, Selic e QPC e define fonte secundária como auxiliar. | Manter a fonte BCB como autoridade para decisão, vigência e publicação. |
| docs/ingestao/PARTE03_BCB_COPOM_PIPELINE_API_V1.0.md | Pipeline de captura via API | Exige RAW original, SHA, parser, NORMALIZED e preservação de revisões. | Não declarar pipeline concluído sem captura e manifesto reais. |
| docs/ingestao/PARTE03_BCB_COPOM_STATUS_API_2026-09-24.md | Estado de API histórico | Confirma recursos JSON, mas afirma que Ata/Comunicado 281 não foram capturados nesta etapa. | Snapshot de 24/09; qualquer estado atual exige novo run e artefactos. |
| docs/ingestao/PARTE03_BDM_NEGOCIO_A_NEGOCIO_ROTA_HISTORICA_2026-09-24.md | Pesquisa de rota BDM | Identifica a mudança de canal histórico para o Boletim Diário do Mercado, mas mantém o arquivo trade-by-trade pendente. | A página/rota não prova que o binário foi obtido; respeitar termos de acesso e licença. |
| docs/ingestao/PARTE03_CALENDARIO_ECONOMICO_CONTRATO_V1.0.md | Contrato de calendário económico | Trata eventos como dados com fonte, RAW, revisões e timestamp, não como indicador técnico. | Coerente; fontes e schemas devem ser validados por evento e release. |
| docs/ingestao/PARTE03_FONTES_CALENDARIO_ECONOMICO_V1.0.md | Matriz de fontes do calendário | Define fonte primária por domínio e estados scheduled/revised/cancelled/unknown. | Não inserir consenso sem origem/timestamp; manter desconhecido quando o horário não é publicado. |
| docs/ingestao/PARTE03_IBGE_CAPTURA_NORMALIZACAO_V1.0.md | Captura/normalização IBGE | Distingue data de divulgação de horário intradiário e mantém event_time_status=UNKNOWN quando não há hora. A referência temporária foi substituída por link oficial. | A captura de 24/09 é snapshot; a resposta HTTP integral/hash continua necessária para RAW certificável. |
| docs/ingestao/PARTE03_MANIFESTO_EXECUCAO_CALENDARIO_ECONOMICO_V1.0.md | Manifesto inicial de execução | Declara estrutura inicial criada, não ingestão completa. Referências temporárias foram substituídas por links oficiais. | Não confundir manifesto inicial com estado atual; cada nova execução deve gerar evidência e hashes próprios. |

## 3. Achados e decisões

### SEM-25-01 — timestamps de evento são dimensões diferentes

A data de reunião, data de decisão, vigência, hora de publicação e momento em que o dado foi capturado não são intercambiáveis. O backtest deve usar o instante em que a informação se tornou disponível ao mercado, não o calendário planeado.

### SEM-25-02 — captura RAW Copom/IBGE ainda não demonstrada

Os documentos indicam que a resposta HTTP integral e o hash não foram obtidos na etapa documentada. Resumos/observações em Markdown não substituem o payload original.

**Decisão:** manter a captura integral e o SHA como pendentes; não inventar hash nem promover o registo descritivo a RAW.

### SEM-25-03 — microestrutura B3 ainda pendente

A janela-evento é uma especificação, não um resultado. Sem arquivo intraday autorizado e validado, não há números observados de agressão, Cumulative Delta, VWAP/TWAP ou reação do WIN/DOL/DI1.

### SEM-25-04 — estado de 24/09 é histórico

Os status da API e do calendário foram observados em 24/09/2026. Os cabeçalhos atualizados em outubro não implicam uma nova captura.

## 4. Conclusão

O conteúdo dos 15 documentos foi revisto. A modelagem temporal é coerente, mas captura RAW integral do Copom/IBGE e reconciliação com B3 intraday permanecem pendentes. Não foram inventados resultados de mercado.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária. A página Pesquisa por Pregão não pode ser objeto de scraping automatizado; endpoints alternativos exigem termos e autorização próprios.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Comunicados do Copom — BCB](https://www.bcb.gov.br/controleinflacao/comunicadoscopom)
- [Atas do Copom — BCB](https://www.bcb.gov.br/controleinflacao/atascopom)
- [Calendário de divulgação — IBGE](https://www.ibge.gov.br/calendario-de-divulgacao-novoportal.html)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
