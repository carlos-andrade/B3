# Revisão semântica documental — Lote 24: B3 intraday, SPRD e negócio a negócio

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-024 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; CAPTURA_AUTOMATIZADA_BLOQUEADA_ATE_VALIDACAO_DE_TERMOS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — autorização de acesso/uso e licenciamento de dados |
| **Origem** | Inspeção de dez contratos e diagnósticos de dados intraday/negócio a negócio |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | TERMOS/AUTORIZAÇÃO → FONTE → CAPTURA → RAW → VALIDAÇÃO → MICROESTRUTURA |
| **Escopo** | Arquivos intraday, SPRD, negócio a negócio, endpoint/nomenclatura e parser |
| **Objetivo** | Separar descoberta técnica de autorização e impedir métricas de microestrutura sem fonte capturada |
| **Dependências** | Termos B3, endpoint autorizado, ficheiros binários, parser e hashes |

## 1. Resultado executivo

Foram revistos dez documentos. A metodologia é correta ao afirmar que uma URL conhecida não equivale a ficheiro obtido, que o ficheiro obtido não equivale a dado validado e que nenhuma métrica de agressão/Cumulative Delta pode ser inventada enquanto os ficheiros primários estiverem ausentes.

Os documentos de 24/09 descrevem descoberta de endpoint e nomenclatura para arquivos de Pesquisa por Pregão; também registam que os arquivos alvo de 16/09 e 17/09 não foram capturados. A página oficial Pesquisa por Pregão veda coleta automatizada a partir da própria página, inclusive por ferramentas de IA. Portanto, o mecanismo de download dinâmico/scraping descrito não pode ser ativado com base apenas na descoberta técnica. Deve ser substituído por uma API/rota explicitamente autorizada ou precedido de autorização documental da B3 e revisão de termos/licença.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/ingestao/PARTE03_B3_INTRADAY_CONTRATO_V1.0.md | Contrato de ingestão intraday | Define granularidade, campos mínimos, janelas e separação de camadas; proíbe imputar agressão sem evidência. | Contrato permanece proposta técnica; captura não deve iniciar sem endpoint autorizado e licença/termos confirmados. |
| docs/ingestao/PARTE03_B3_INTRADAY_DIAGNOSTICO_DOWNLOAD_2026-09-24.md | Diagnóstico de download dinâmico | Confirma nomes de ficheiros na página, mas não prova captura nem conteúdo disponível; declara que a ausência de arquivo não prova ausência de dados. | A descoberta de filelist não autoriza scraping; obter rota autorizada e arquivo persistido antes de qualquer análise. |
| docs/ingestao/PARTE03_B3_INTRADAY_ENDPOINT_NOMENCLATURA_2026-09-24.md | Descoberta de endpoint/nomenclatura | Endpoint e nomes foram confirmados no snapshot, mas os arquivos de 16/09 e 17/09 não foram capturados. | Estado de descoberta não é estado de ingestão; não ativar automação de página. |
| docs/ingestao/PARTE03_B3_INTRADAY_EVIDENCIA_ACESSO_2026-09-24.md | Evidência de acesso retroativo | Regista pesquisa e mudança estrutural da página, sem evidência de captura dos binários alvo. | Preservar como diagnóstico histórico; termos de acesso e endpoint autorizado permanecem gates. |
| docs/ingestao/PARTE03_B3_INTRADAY_FONTE_AQUISICAO_V1.0.md | Plano de fonte/aquisição | Exige arquivos primários, hashes e separação de EOD/intraday; Cumulative Delta e agressão continuam pendentes. | Não publicar análise intraday observada até existir dataset primário autorizado e validado. |
| docs/ingestao/PARTE03_B3_INTRADAY_PADRAO_DOWNLOAD_2026-09-24.md | Padrão de download descoberto | Descreve convenções de nomes e validação de arquivo vazio, mas depende da página oficial como fonte de descoberta. | Não automatizar coleta da página; usar somente rota explicitamente autorizada. |
| docs/ingestao/PARTE03_B3_INTRADAY_TESTE_CANDIDATOS_DOWNLOAD_2026-09-24.md | Teste de URLs candidatas | Distingue URL candidata de arquivo obtido e mantém os candidatos sem captura. | Não tratar sucesso HTTP ou nome previsível como evidência de dataset; autorização permanece pendente. |
| docs/ingestao/PARTE03_B3_NEGOCIO_A_NEGOCIO_ESPECIFICACAO_V1.0.md | Especificação de negócios | Separa negócio a negócio, negócios consolidados e cadastro de instrumentos; exige dados binários antes de medir agressão. | A especificação não comprova que a B3 disponibilizou o arquivo alvo nem autoriza redistribuição. |
| docs/ingestao/PARTE03_B3_SPRD_AQUISICAO_STATUS_2026-09-24.md | Estado de aquisição SPRD | Declara que URL conhecida ≠ arquivo obtido ≠ dado validado. | Snapshot histórico; não declarar aquisição concluída sem arquivo, hash e validação. |
| docs/ingestao/PARTE03_B3_SPRD_PARSER_VALIDACAO_V1.0.md | Especificação de parser SPRD | Define validação de estrutura, hashes e granularidade; mantém book/agressor/Cumulative Delta pendentes. | Parser especificado não equivale a parser validado sobre ficheiro real; manter métricas pendentes. |

## 3. Achados e decisões

### SEM-24-01 — restrição de coleta automatizada da Pesquisa por Pregão

A página oficial declara que a coleta automatizada a partir dela, inclusive por ferramentas de IA, é vedada. Os documentos descrevem descoberta de arquivos a partir dessa página e download dinâmico.

**Decisão:** não implementar nem ativar scraping da página. Qualquer rota alternativa/API exige verificação dos termos específicos e autorização documentada; o acesso técnico não é autorização.

### SEM-24-02 — endpoint conhecido não é captura

Os documentos não apresentam os arquivos binários de 16/09 e 17/09/2026 com hashes e validação. A nomenclatura dos arquivos não comprova conteúdo.

**Decisão:** estado de aquisição permanece PENDENTE até existir fonte autorizada, arquivo persistido, SHA-256, parser e qualidade.

### SEM-24-03 — microestrutura exige granularidade adequada

EOD e relatórios simplificados não substituem negócio a negócio. Agressão, Cumulative Delta e análise de reação intraday exigem fonte, lado agressor ou método documentado, sessão e janela.

**Decisão:** não produzir números observados nem preencher lacunas por estimativa.

## 4. Conclusão

O conteúdo dos dez documentos foi revisto. Os contratos técnicos são coerentes, mas a aquisição permanece pendente e o mecanismo de coleta a partir da página não deve ser automatizado. O gate de autorização/termos deve ser satisfeito antes de qualquer captura.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária. Esta revisão não autoriza scraping nem redistribuição comercial de dados B3.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Pesquisa por Pregão — B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
