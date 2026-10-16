# Revisão semântica documental — Lote 23: catálogo de fontes e contratos NORMALIZED

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-023 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; SNAPSHOTS_E_CONTRATOS_CLASSIFICADOS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | cdab39853d059452380775cb93d8cbdda112cc7bc36124586c27512d891a891e |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | N/A — revisão documental; não certifica todos os anos |
| **Origem** | Inspeção de 10 documentos de fonte, parser, catálogo e rotina diária |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | TERMOS → FONTE → RAW → PARSER → NORMALIZED → MANIFESTO → QUALITY |
| **Escopo** | Catálogo de fontes, endpoint, rotina diária, parser e contratos NORMALIZED |
| **Objetivo** | Distinguir versões históricas, evidência estrutural e estado diário corrente |
| **Dependências** | Fonte oficial B3, contratos NORMALIZED V1/V2, manifestos e auditorias posteriores |

## 1. Resultado executivo

Foram revistos dez documentos. A distinção entre RAW imutável, transformação determinística, manifesto de qualidade, validação estrutural e auditoria semântica está consistente. Os catálogos V1.0/V1.1 são documentos de escopo e cobertura, não prova de que todos os datasets estejam adquiridos ou licenciados. A matriz 41/41 e a cobertura até 23/09 são resultados históricos, não estado corrente de 15/10.

Foram aplicadas duas correções: as citações temporárias do contrato NORMALIZED foram substituídas por referências persistentes às páginas oficiais B3; e a rotina diária passou a exigir verificação dos termos do endpoint antes de ativar automação. A página Pesquisa por Pregão proíbe coleta automatizada a partir dela, inclusive por ferramentas de IA; um endpoint direto de ZIP/API precisa de análise de termos própria, sem presumir autorização.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/PARTE01_AUDITORIA_SEMANTICA_DUPLICIDADES_COTAHIST_V1.0.md | Auditoria semântica de duplicidades | Distingue chave candidata de chave natural definitiva e proíbe exclusão de registos nesta fase. | Manter a chave definitiva pendente até evidência histórica; contagens citadas são do snapshot da auditoria. |
| docs/ingestao/PARTE01_CATALOGO_FONTES_DADOS_B3_V1.0.md | Catálogo inicial de fontes | Inventaria fontes B3 prioritárias para ingestão e backtests; admite que períodos e layouts precisam de levantamento específico. | Tratar como V1 inicial; não inferir disponibilidade, licença ou granularidade completa a partir do catálogo. |
| docs/ingestao/PARTE01_CATALOGO_FONTES_DADOS_B3_V1.1.md | Atualização temporal do catálogo | Define 1986 como marco histórico e exige matriz de cobertura antes de considerar a etapa concluída. | V1.1 não prova aquisição completa; manter cobertura anual/campos vinculada a artefactos e manifestos. |
| docs/ingestao/PARTE01_CATALOGO_OPERACIONAL_COTAHIST_1986_ATUAL_V1.0.md | Catálogo operacional histórico | Identifica a página oficial Cotações Históricas e requisitos de RAW, checksum, metadata, parser e manifesto. | Estado de 23/09 é histórico; endpoint e termos devem ser revalidados antes de automação atual. |
| docs/ingestao/PARTE01_CONTRATO_EVIDENCIA_NORMALIZED_V1.0.md | Contrato de evidência | Exige que o manifesto identifique RAW, parser, SHA e testes; a cadeia é reproduzível e auditável. | Coerente; o contrato não prova que cada ano esteja hoje materializado/certificado. |
| docs/ingestao/PARTE01_CONTRATO_NORMALIZED_COTAHIST_V1.0.md | Contrato da camada NORMALIZED V1 | Define 25 campos, preservação RAW e separação EOD versus tick/book. Citações temporárias foram substituídas por links oficiais persistentes. | V1 deve ser lido como contrato histórico e reconciliado com V2 onde houver diferença; não misturar versões silenciosamente. |
| docs/ingestao/PARTE01_DESCOBERTA_ENDPOINT_COTAHIST_V1.0.md | Descoberta histórica do endpoint | Documenta a rota legada e a fonte B3 consultada em 23/09; não afirma que o endpoint histórico seja invariável. | Revalidar URL, resposta, termos e hash em cada mudança de endpoint; preservar a evidência histórica. |
| docs/ingestao/PARTE01_MATRIZ_VALIDACAO_NORMALIZED_1986_2026_V1.0.md | Matriz de validação histórica | Reporta 41/41 anos validados estruturalmente em 23/09 e mantém auditoria semântica de duplicidades aberta. | Não usar como estado atual sem nova geração; estrutural não significa semântica integral. |
| docs/ingestao/PARTE01_ROTINA_ATUALIZACAO_DIARIA_COTAHIST_V1.0.md | Runbook de atualização diária | Define atualização sem data final, SHA, manifesto e mutação apenas quando há alteração. Foi adicionado gate de termos do endpoint. | Confirmar autorização específica do endpoint antes de automatizar; scraping da página Pesquisa por Pregão é vedado. |
| docs/ingestao/PARTE01_VALIDACAO_PARSER_COTAHIST_V1.0.md | Relatório de validação do parser | Separa implementação do parser da execução confirmada e proíbe inventar números antes de Actions. | Resultado histórico; consultar evidência posterior para estado corrente do parser e dos datasets. |

## 3. Achados e decisões

### SEM-23-01 — catálogo de fontes não prova cobertura

A lista de fontes é um plano de ingestão. Cobertura real exige arquivo bruto, hash, data, parser, manifesto e testes para cada dataset/período.

### SEM-23-02 — versões V1/V1.1 e V2 devem permanecer separadas

O contrato NORMALIZED V1 e a versão V2 de persistência/certificação têm escopos e requisitos distintos. Não se deve combinar regras sem decisão versionada e matriz de compatibilidade.

### SEM-23-03 — termos de acesso são pré-condição para automação

A rotina diária deve confirmar autorização/termos do endpoint concreto. A proibição da página Pesquisa por Pregão não deve ser extrapolada automaticamente a toda API, mas também não pode ser ignorada: cada endpoint precisa de análise própria.

### SEM-23-04 — matriz 41/41 é histórica e estrutural

A matriz de 23/09 não certifica atualidade diária de 15/10 nem semântica completa. A revisão de duplicidades e a exceção K4 permanecem distintas da integridade física.

## 4. Conclusão

O conteúdo dos dez documentos foi revisto. Foram corrigidas referências temporárias e adicionado um gate de termos à rotina diária. Não foram alterados dados RAW/NORMALIZED ou manifestos.

COTAHIST 1986–2025 permanece somente para consulta/read-only; 2026 mantém atualização diária.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Cotações históricas — B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/)
- [Layout dos arquivos — B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/layout-dos-arquivos/)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
