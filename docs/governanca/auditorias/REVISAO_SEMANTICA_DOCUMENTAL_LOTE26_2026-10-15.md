# Revisão semântica documental — Lote 26: auditorias históricas, contratos de microestrutura e reconciliação

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-026 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; HISTORICO_PRESERVADO; CAPTURA_TRADE_BY_TRADE_PENDENTE |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão documental; não certifica microestrutura nem semântica completa de 1986 |
| **Origem** | Inspeção de 17 documentos de auditoria 1986, negócio a negócio, contratos Copom e automação |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | FONTE AUTORIZADA → RAW → HASH → PARSER → NORMALIZED → RECONCILIAÇÃO |
| **Escopo** | Auditoria estrutural 1986, contratos de negócio a negócio, mapa TPMERC/CODBDI, calendário/volume/preço e processo automático |
| **Objetivo** | Confirmar limites entre desenho de pipeline, execução real e conclusão semântica |
| **Dependências** | Dados brutos, manifests, contratos B3, API BCB e evidências de workflows |

## 1. Resultado executivo

Foram revistos 17 documentos. A regra metodológica comum é consistente: desenho do parser, endpoint ou workflow não prova que o arquivo foi capturado; sucesso de normalização estrutural não resolve a identidade económica de 1986; e o estado de uma execução em setembro não é o estado corrente.

A auditoria estrutural A1986 descreve duplicidades, nulos e preços dentro do universo/hash daquela execução. A reconciliação determinística RAW→NORMALIZED de 1986 aparece como pendente no documento de Parte06; isso é um estado histórico do documento, não autorização para executar hoje nem prova de que a reconciliação já foi concluída. A decisão de projeto mantém 1986–2025 fechados para consulta. A aquisição de negócios individuais intraday continua pendente, e não se devem inventar métricas de agressão/Cumulative Delta.

Foram corrigidas duas citações temporárias: a contingência de importação COTAHIST agora remete para a página oficial de Cotações Históricas e exige respeito aos termos; a solicitação institucional de BDI já não usa um marcador de pesquisa transitório como prova de acesso.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/PARTE03_COTAHIST_AUDITORIA_A1986_V1.0.md | Auditoria estrutural de 1986 | Regista duplicidades e distribuições com hash e universo; distingue anomalias de exclusão automática. | Preservar como auditoria histórica; não inferir semântica económica nem reabrir 1986. |
| docs/ingestao/PARTE03_COTAHIST_NORMALIZACAO_CONTROLADA_V7.md | Plano de normalização controlada | Define fail-closed, parser, RAW, data, hash, quality e evidências; o estado “não expandir” pertence ao snapshot anterior. | Não usar como instrução corrente sem reconciliar com contratos posteriores; anos pré-2026 permanecem consulta/read-only. |
| docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_CONTRATO_V1.1.md | Contrato de ingestão trade-by-trade | Define granularidade, agressor, Cumulative Delta, VWAP/TWAP e mantém dataset real pendente. | Não gerar métricas observadas sem arquivo autorizado e parser validado. |
| docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_ENDPOINT_DERIV_V1.0.md | Descoberta de endpoint | Nomeia endpoint e workflow candidato, mas o conteúdo do ZIP/TXT, layout e agressor permanecem pendentes. | Endpoint identificado não equivale a arquivo adquirido nem a permissão de uso. |
| docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_FONTE_OFICIAL_V1.0.md | Fonte e rota de aquisição | Direciona a pesquisa para BDM > Derivativos > Negócio a negócio e proíbe produzir números antes da captura. | Respeitar termos/licença; página Pesquisa por Pregão não pode ser objeto de scraping automatizado. |
| docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_LAYOUT_DERIV_V1.0.md | Layout proposto para derivativos | Define 12 campos e reconhece que timestamp, lado agressor e arquivo binário ainda não foram validados. | Layout é proposta técnica, não prova do esquema real. |
| docs/ingestao/PARTE03_NEGOCIO_A_NEGOCIO_RECONCILIACAO_FONTE_V1.0.md | Reconciliação de fonte | Exige origem, data, formato, tamanho, SHA, colunas, número de registos e intervalo temporal. | Coerente; a captura efetiva continua pendente até existir artefacto verificável. |
| docs/ingestao/PARTE03_STATUS_ESTABILIZACAO_ACTIONS_2026-09-24.md | Diagnóstico histórico de Actions | Regista triggers residuais e recomenda um teste manual de 1986, mas o estado pertence a 24/09. | Preservar como histórico; não executar o plano antigo para reabrir anos fechados. |
| docs/ingestao/PARTE04_BCB_COPOM_CONTRATO_DADOS_V2.1.md | Contrato de dados Copom V2.1 | Separa reunião, decisão, comunicado, ata e vigência; exige informação disponível no instante correto. | Coerente como contrato; a captura integral e parser de votos permanecem pendentes. |
| docs/ingestao/PARTE04_COTAHIST_1986_TPMERC_CODBDI_MAPA_V1.0.md | Mapa semântico de códigos | Organiza TPMERC × CODBDI observados, mas não declara a identidade económica definitiva. | Manter códigos não mapeados e hipóteses separadas; não inferir chave por frequência. |
| docs/ingestao/PARTE04_RECONCILIACAO_SEMANTICA_COTAHIST_1986_V1.0.md | Plano de reconciliação semântica | Mantém 1986 bloqueado para liberação semântica e proíbe alteração de RAW; o status é anterior ao fechamento operacional de consulta. | Preservar como snapshot de investigação; não reabrir nem promover sem decisão formal. |
| docs/ingestao/PARTE05_COTAHIST_1986_RECONCILIACAO_CALENDARIO_V1.0.md | Reconciliação de calendário | Identifica 12 dias úteis candidatos e uma observação em sábado, com fontes históricas de contexto. | A causa dos dias ausentes não está provada; não classificar como feriado/suspensão sem fonte primária. |
| docs/ingestao/PARTE05_COTAHIST_1986_RECONCILIACAO_VOLUME_PRECO_V1.0.md | Reconciliação de volume/preço | Analisa 61 casos e exige unidade/cotação histórica; diferenças de escala não são automaticamente erro. | Preservar os casos e método; não corrigir valores históricos por regra moderna sem prova. |
| docs/ingestao/PARTE06_COTAHIST_RECONCILIACAO_RAW_NORMALIZED_1986_V1.0.md | Contrato de reconciliação determinística | Define critérios RAW→NORMALIZED e declara execução pendente no documento. | O estado é histórico; não declarar conclusão a partir do contrato, nem executar retroativamente por esta revisão. |
| docs/ingestao/PROCESSO_AUTOMATICO_IMPORTACAO_COTAHIST_V1.0.md | Processo automático de importação | Define captura, hash, manifesto, validação e fallback. A referência temporária foi substituída por fonte oficial com ressalva de termos. | Endpoint direto exige termos próprios; scraping da página Pesquisa por Pregão é vedado. |
| docs/ingestao/SOLICITACAO_INSTITUCIONAL_BDI_BOVESPA_19861010_V1.0.md | Rascunho de solicitação institucional | Contém alvo e critérios para o BDI de 10/10/1986, mas não prova envio, protocolo, recebimento ou resposta. Referência temporária foi removida. | Não marcar solicitação como enviada; exigir autorização do proprietário, comprovativo e identificador de documento. |
| docs/ingestao/VERIFICACAO_AUTOMACAO_COTAHIST_2026-09-25.md | Verificação histórica de automação | Afirma que a primeira execução real ainda não tinha evidência suficiente em 25/09. | Snapshot histórico; estado atual depende de runs posteriores, não da atualização do cabeçalho. |

## 3. Achados e decisões

### SEM-26-01 — microestrutura sem arquivo primário

A especificação trade-by-trade não substitui o arquivo. Os documentos declaram o dataset real como pendente e proíbem estimar agressão ou Cumulative Delta.

**Decisão:** manter a análise intraday sem resultados observados até existir fonte autorizada, binário, hash, parser e validação.

### SEM-26-02 — anos históricos fechados

Documentos antigos recomendam reexecutar normalização de 1986 e expandir a série após um teste. A decisão posterior do projeto fecha todos os anos anteriores a 2026 para consulta.

**Decisão:** preservar os documentos como histórico, sem executar os passos antigos nem alterar RAW/NORMALIZED.

### SEM-26-03 — dias úteis ausentes e preço/volume

A auditoria de calendário e a análise de 61 casos não demonstram, por si, falha de ingestão. Exigem fonte oficial histórica, unidade, sessão e evidência por caso.

### SEM-26-04 — solicitação institucional não enviada

O documento é um rascunho, não um recibo. A causa da colisão K4 não deve ser marcada como resolvida até existir fonte primária identificada.

## 4. Conclusão

O conteúdo dos 17 documentos foi revisto. As referências temporárias foram corrigidas e os estados históricos foram separados do estado corrente. Não foram alterados dados, workflows ou manifestos.

COTAHIST 1986–2025 permanece somente para consulta/read-only; 2026 mantém atualização diária. A causa histórica K4 e a captura trade-by-trade continuam pendentes.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Cotações históricas — B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/)
- [Pesquisa por Pregão — B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
