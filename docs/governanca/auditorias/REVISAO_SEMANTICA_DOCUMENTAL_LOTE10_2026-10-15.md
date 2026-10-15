# Revisão semântica documental — Lote 10: licenciamento de market data e governação comercial

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-REV-SEM-010 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_REVISAO_SEMANTICA |
| **Fase** | FASE 3 — Revisão semântica e reconciliação |
| **Estado** | REVISAO_CONTEUDO_CONCLUIDA; VALIDACAO_DE_FONTE_E_LICENCA_PENDENTE |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE_CALCULO |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-15 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — revisão documental não equivale a parecer jurídico ou licença comercial |
| **Origem** | Inspeção de 14 documentos sobre Market Data B3, licenciamento e planeamento comercial |
| **Autoridade superior** | [Carta Magna B3](../../docs/CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | FONTE OFICIAL → INTERPRETAÇÃO DOCUMENTADA → LICENÇA/CONTRATO → PRODUTO → DISTRIBUIÇÃO |
| **Escopo** | Política comercial B3 Market Data 2026 V1.1, datasets, classificações, licenças, tarifas e go-to-market |
| **Objetivo** | Impedir que resumos internos sejam confundidos com a política oficial vigente ou autorização de redistribuição |
| **Dependências** | PDF oficial B3, notas de rodapé, Consumption Policy, contratos e pareceres de licenciamento |

## 1. Resultado executivo

Foram revistos 14 documentos. O conjunto contém salvaguardas adequadas: identifica a política comercial oficial como fonte primária, distingue display/non-display, depth, timeliness, finalidade, location e unidade de cobrança, e declara que as matrizes internas não substituem contrato, Consumption Policy ou validação formal da B3.

A revisão de conteúdo não verificou externamente a versão corrente do PDF, as notas de rodapé, as tarifas ou o enquadramento legal de cada produto. Portanto, os preços/tarifas citados devem ser tratados como referências documentais de 2026 V1.1, não como preços atuais garantidos nem autorização para comercialização. A redistribuição de dados e a entrega de feeds permanecem bloqueadas até confirmação de direitos aplicáveis.

## 2. Matriz de revisão por documento

| Caminho | Natureza | Resultado semântico | Ação/limite |
|---|---|---|---|
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/CHANGELOG.md | Histórico de alterações da política comercial | Regista a política 2026 V1.1 e a criação de artefactos internos. Não constitui licença nem contrato. | Preservar como histórico; confirmar cada versão no documento oficial antes de uso comercial. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/DATASETS-E-CLASSIFICACOES.md | Resumo de datasets e classes de licenciamento | Distingue datasets, profundidade, timeliness e aplicações, incluindo Enterprise/Location. | Validar termos, classes e disponibilidade na fonte oficial vigente; não inferir licença a partir da classificação interna. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/FONTE-PRIMARIA.md | Referência da fonte primária | Identifica emissor B3 S.A. e política comercial Market Data 2026 V1.1. | Acrescentar/confirmar URL, data de captura, hash do PDF e versão oficial quando a política for usada para decisão ou contrato. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/IMPACTO-NO-NEGOCIO.md | Análise de impacto | Reconhece que licenciamento é custo e que indicadores derivados (agressão, fluxo, Cumulative Delta) precisam de análise da origem e permissões. | Fazer análise por produto, transformação, usuário, canal e distribuição; derivação não implica automaticamente isenção de licença. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/LICENCAS-E-APLICACOES.md | Matriz de requisitos de licença | Exige ficha por produto com dataset, depth, timeliness, display/non-display, finalidade, usuário, localização, distribuição, transformação, licença, custo e evidência. | Tratar a ficha como gate pré-comercial; exigir confirmação documental da B3/assessoria competente antes do lançamento. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/MATRIZ-LICENCIAMENTO-PRODUTOS.md | Matriz de compliance/economia | Declara que é modelo operacional e não substitui contrato, política vigente, Consumption Policy ou validação formal da B3. | Manter todos os campos de evidência, tarifa e licença sem presumir valores ausentes. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/POLITICA-ESTRUTURADA.md | Resumo estruturado da política comercial | Resume unidades de cobrança, correções, mercado nacional/internacional e Non-Display Enterprise. | Conferir todas as regras e exceções no PDF oficial antes de calcular obrigações ou contratar. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/PRECOS-E-TARIFAS.md | Extrato de tarifas de referência | Declara que os valores vieram de tabelas indexadas e que a versão vigente/notas de rodapé devem ser validadas. | Não usar para proposta/contrato sem comparar com o PDF oficial e documentar data, unidade, impostos, câmbio e exceções. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/B3-MARKET-DATA/README.md | Índice da política oficial e artefactos | Aponta para Market Data B3 Commercial Policy 2026 V1.1 e URL de origem. | Manter o PDF oficial como fonte; adicionar prova de aquisição e hash quando for arquivado no repositório. |
| docs/NEGOCIO/06-GOVERNANCA-LICENCIAMENTO-REGULACAO/README.md | Índice de governança comercial | Exige separar RAW, dados licenciados, derivados e análise própria, com validação de redistribuição e risco regulatório. | Manter como regra de navegação; decisões finais exigem contrato/licença e revisão regulatória. |
| docs/NEGOCIO/07-GO-TO-MARKET/README.md | Plano de go-to-market | Sequência de validar problema, produto, preço e canais antes de escalar aquisição. | Manter como plano, não evidência de execução ou validação de mercado. |
| docs/NEGOCIO/08-CENARIOS-RECEITA/README.md | Cenários hipotéticos de receita | Identifica cenários B2C/B2B/projetos como hipotéticos e mantém regras de integridade. | Não tratar totais hipotéticos como forecast sem premissas, probabilidades, custos e dados observados. |
| docs/NEGOCIO/09-ROADMAP-COMERCIAL/README.md | Roadmap comercial | Organiza fases de fundação, MVP, validação, escala e enterprise; depende de arquitetura, licenças, ICP, pilotos e métricas. | Nenhuma fase é considerada concluída apenas por estar listada; exigir evidência e decisão de passagem. |
| docs/NEGOCIO/10-REGISTRO-DE-DECISOES/README.md | Índice de decisões comerciais | Exige registo auditável de decisões e hipóteses, com evidência, responsáveis e ações seguintes. | Usar para rastrear decisões; decisões sem registo/evidência permanecem não aprovadas. |

## 3. Achados e decisões

### SEM-10-01 — fonte oficial e atualidade tarifária

A existência de um PDF identificado como 2026 V1.1 não prova, por si só, que não exista versão posterior ou adenda. A fonte oficial deve ser reconsultada na data de cada decisão comercial, e o ficheiro usado deve ser identificado por versão, data de captura e SHA-256.

### SEM-10-02 — derivados não implicam isenção

Indicadores como agressão, fluxo e Cumulative Delta podem ser transformações de dados de mercado. O facto de serem calculados internamente não estabelece automaticamente o direito de redistribuir os dados de origem ou o resultado derivado. A análise deve considerar contrato, finalidade, usuário, display/non-display, profundidade e distribuição.

### SEM-10-03 — preços são referência, não autorização

A matriz de tarifas declara os limites da sua própria evidência. Não usar os valores como preço oficial atual nem base contratual até comparação com o documento primário, notas de rodapé e termos aplicáveis.

### SEM-10-04 — BLOOMBERG_MAIL fora do escopo

Nenhum documento deste lote autoriza integração com o projeto BLOOMBERG_MAIL. A fronteira de projeto permanece separada; a cadeia de fonte e licença para B3 deve ser validada independentemente.

## 4. Conclusão

O conteúdo dos 14 documentos foi revisto. As regras internas são adequadas como checklist de licenciamento, mas não substituem a fonte primária nem constituem parecer jurídico. O gate de comercialização continua dependente da verificação da política oficial vigente e de direitos de uso/distribuição por produto.

COTAHIST 1986–2025 permanece somente para consulta; 2026 mantém atualização diária. BLOOMBERG_MAIL permanece isolado e fora do âmbito operacional B3.

## 5. Referências

- [Matriz integral de revisão semântica](../auditorias/MATRIZ_REVISAO_SEMANTICA_INTEGRAL_B3_V1.md)
- [Issue #11](https://github.com/carlos-andrade/B3/issues/11)
