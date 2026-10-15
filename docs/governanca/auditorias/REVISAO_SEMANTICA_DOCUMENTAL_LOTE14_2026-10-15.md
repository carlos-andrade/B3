# Revisão semântica documental — Lote 14: fontes B3, BDI, calendário e microestrutura

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-014 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; GATE_DE_TERMS_E_CAPTURA_RAW_REGISTADO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — validação de acesso/termos e captura integral quando aplicável |
| **Origem** | Inspeção de 15 documentos de BDI, calendário económico, migração de fontes e Market Data |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | TERMOS/AUTORIZAÇÃO → FONTE → RAW → HASH → NORMALIZED → QUALITY → CONSUMO |
| **Escopo** | BDI, fontes de calendário, migração API B3, Market Data EOD e microestrutura |
| **Objetivo** | Corrigir rotulagem de pseudo-RAW, preservar estados históricos e registar o gate de termos de acesso |
| **Dependências** | Fontes oficiais B3/BCB/IBGE, endpoints específicos, manifestos e políticas de acesso |

## 1. Resultado executivo

Foram revistos 15 documentos. A arquitetura documental distingue adequadamente captura, RAW, normalização, manifesto, validação e granularidade de dados; os documentos de microestrutura não autorizam calcular agressão ou Cumulative Delta quando o lado agressor não é observável.

Foram corrigidos três registos que se intitulavam RAW, embora declarassem que a captura HTTP integral e o hash da fonte ainda estavam pendentes. Os ficheiros foram renomeados semanticamente para registos de fonte/snapshot descritivo, com estado explícito de captura RAW pendente. Nenhum payload bruto foi fabricado.

Foi também corrigida a referência não resolúvel a marcadores de citação temporários nos README de Market Data e histórico, substituindo-a por links oficiais da B3. Adicionou-se um gate de termos: a página oficial de Pesquisa por Pregão declara que a coleta automatizada a partir da própria página, inclusive por ferramentas de IA, é vedada. Não implementar scraping dessa página; endpoints/API alternativos exigem revisão independente dos termos e autorização antes da ativação.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| dados/bdi/2026/README.md | Índice anual BDI | Estrutura RAW/NORMALIZED/manifesto e validações de data, origem, hash, formato, duplicidade e campos ausentes é coerente. | Só declarar captura quando arquivo original e manifesto existirem; este README não prova ingestão diária completa. |
| dados/bdi/PROTOCOLO_CAPTURA.md | Protocolo operacional | Distingue BDI consolidado de granularidade intradiária e proíbe substituir o bruto. Foi adicionado gate de termos/autorizações. | Captura automática só após verificação dos termos do endpoint específico; scraping da página Pesquisa por Pregão permanece vedado. |
| dados/bdi/README.md | Índice BDI | Separa data observada de captured_at_utc e exige fonte, data e hash. Foi adicionada ressalva de acesso automatizado. | Confirmar termos do endpoint BDI antes de ativar workflow; existência técnica de API não equivale a autorização. |
| dados/bdi/fontes/README.md | Mapa de fontes BDI | Identifica o BDI como fonte diária consolidada e reconhece que nem todas as tabelas oferecem granularidade de microestrutura. | Confirmar cada tabela e campo numa captura autorizada; não assumir que o BDI permite reconstruir negócios tick a tick. |
| dados/calendario_economico/raw/bcb_copom_281_ata_2026-09-24.md | Registo de metadados de fonte | Antes era rotulado RAW embora dissesse que a captura HTTP integral e source_hash estavam pendentes. Corrigido para REGISTO_DE_FONTE_PENDENTE_RAW. | Captura integral oficial e hash da resposta continuam pendentes; não tratar este registo como corpo RAW da Ata. |
| dados/calendario_economico/raw/bcb_copom_281_comunicado_2026-09-24.md | Registo de metadados de fonte | Antes era rotulado como evidência RAW, mas o pipeline descrevia captura integral e hash pendentes. Corrigido para REGISTO_DE_FONTE_PENDENTE_RAW. | Captura e reconciliação com a sessão B3 continuam pendentes; não promover como comunicado bruto persistido. |
| dados/calendario_economico/raw/ibge_calendario_conjunturais_2026_20260924.md | Registo de observações do calendário | O conteúdo enumera eventos observados, não o payload HTTP original; título e tipo foram corrigidos para registo descritivo com RAW pendente. | Downloader oficial continua fonte canónica; hash deve corresponder ao conteúdo efetivamente recebido. |
| dados/cotahist/manifests/STATUS_AQUISICAO_2026-09-23.md | Snapshot histórico de aquisição | O texto afirma que 1986 não estava ingerido naquele momento, estado que não representa o estado posterior do dataset 1986–2026. | Preservar como fotografia de 23/09; não usar como estado corrente nem reescrever a cronologia. |
| dados/fontes/DIAGNOSTICO_MIGRACAO_API_B3_2026-09-23.md | Diagnóstico histórico de API | Regista HTTP 400 na rota legada e orienta a migração para BDI/Pesquisa por Pregão, sem aceitar presença de página como prova de captura. | Manter como histórico; qualquer endpoint novo exige teste, termos de uso, persistência e manifesto. |
| dados/fontes/STATUS_MIGRACAO_FONTES_B3_2026-09-23.md | Estado histórico de migração | A tabela de estados pertence a 23/09 e lista capturas ainda em teste naquele momento. | Não usar como estado corrente; atualizar em novo registo baseado em runs e artefactos atuais. |
| dados/market_data/PROVEDORES_E_GRANULARIDADE.md | Matriz de granularidade | Evita tratar BVBG.186.01/187.01 como feed tick a tick e não presume agressor explícito. | Manter a arquitetura em aberto até inspecionar ficheiros reais e confirmar termos/licenças da fonte. |
| dados/market_data/README.md | Política de Market Data | Distingue PriceReport completo de relatórios simplificados e exige lado agressor auditável. Referência de citação temporária foi substituída por link oficial; acrescentado gate de termos. | A página Pesquisa por Pregão proíbe coleta automatizada a partir dela; endpoint alternativo exige validação independente e autorização. |
| dados/market_data/fontes/INVENTARIO_PESQUISA_POR_PREGAO_2026-09-23.md | Inventário histórico da página | Lista arquivos e situações observadas em 23/09; a observação é temporal e não garante disponibilidade atual. Link oficial e ressalva de coleta automatizada foram acrescentados. | Preservar como snapshot; revalidar cada arquivo em captura autorizada e documentar a data. |
| dados/market_data/historico/README.md | Índice de dados históricos | Define captura por data, bruto, hash, manifesto e normalização separada. Referência temporária foi substituída por link oficial e foi acrescentada ressalva de termos. | Não automatizar scraping da página; confirmar termos/autorização de endpoint alternativo antes da execução. |
| dados/market_data/microestrutura/README.md | Metodologia de microestrutura | Fórmulas de Cumulative Delta, VWAP e TWAP são condicionadas à origem, classificação e janela documentadas. | Não calcular agressão/Cumulative Delta sem dados e método auditáveis; registrar sessão, janela e tratamento de intervalos sem negócio. |

## 3. Achados e decisões

### SEM-14-01 — restrição de coleta automatizada na página oficial B3

A página oficial de [Pesquisa por Pregão — B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/) declara que os dados são propriedade exclusiva da B3 e veda coleta automatizada a partir da página, inclusive por ferramentas de IA.

**Decisão operacional:** não implementar scraping dessa página. A API/endpoint BDI ou outro endpoint só pode ser automatizado após verificação separada dos termos aplicáveis, permissões, limites de acesso, armazenamento e reutilização. Não assumir que um endpoint alternativo herda autorização por ser tecnicamente acessível.

### SEM-14-02 — metadados de fonte não são RAW

Os três registos Copom/IBGE não continham a resposta HTTP integral e indicavam hash de fonte pendente. A rotulagem anterior poderia induzir consumidores a acreditar que a fonte bruta estava preservada.

**Correção:** os títulos/tipos/estados foram alterados para declarar explicitamente que são registos de metadados ou observações, com captura RAW pendente. Não foi inventado nem sintetizado um payload de fonte.

### SEM-14-03 — estado de migração histórico

Os relatórios de 23/09 descrevem falhas e estados de teste daquele dia. Eles não provam o estado dos pipelines atuais nem devem ser atualizados retroativamente.

**Decisão:** conservar os snapshots e criar novos relatórios com runs, commits, payloads e manifestos correntes quando houver evidência.

### SEM-14-04 — granularidade e inferência de agressor

Relatórios simplificados EOD e BDI consolidado não são automaticamente fontes de negócios tick a tick. Agressão e Cumulative Delta exigem lado agressor explícito ou metodologia de classificação documentada, com limitações.

**Decisão:** não fabricar granularidade nem inferir o lado agressor sem dados suficientes.

## 4. Conclusão

O conteúdo dos 15 documentos foi revisto; três registos foram corrigidos para não se apresentarem como RAW quando a captura integral ainda está pendente. Os README de Market Data/BDI passaram a explicitar a restrição da página oficial e a necessidade de revisão de termos para APIs alternativas.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária. A revisão não autoriza scraping da página B3 nem redistribuição comercial de dados.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Fonte oficial — Pesquisa por Pregão B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
