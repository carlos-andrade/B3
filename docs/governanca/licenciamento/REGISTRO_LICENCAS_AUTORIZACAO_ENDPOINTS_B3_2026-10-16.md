# REGISTO DE LICENÇAS E AUTORIZAÇÃO DE ENDPOINTS — B3

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-LIC-EP-20261016 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | REGISTRO_DE_CONFORMIDADE |
| **Fase** | LICENCIAMENTO_E_AUTORIZACAO_DE_FONTES |
| **Estado** | PARCIAL — GATES FAIL-CLOSED IMPLEMENTADOS; AUTORIZAÇÕES EXTERNAS PENDENTES |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | b494aa5a4555a26a4a10d2019e6400c9c38c25991eb350349a31b64911a6b8e9 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — titular/autoridade da fonte e responsável jurídico/comercial |
| **Origem** | Termos oficiais das fontes, políticas de dados e inventário de endpoints do repositório |
| **Autoridade superior** | [Carta Magna de Governança B3](../../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre Canónico](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

## 1. Decisão executiva

A verificação técnica encontrou endpoints acessíveis, mas não encontrou prova de autorização suficiente para todas as formas de recolha, armazenamento, desenvolvimento, publicação em repositório público ou redistribuição previstas pelo projeto.

**Decisão:** aplicar `FAIL_CLOSED` aos endpoints B3 com autorização não demonstrada. Não iniciar nova recolha automatizada nem publicar novos dados provenientes desses endpoints até a evidência de autorização estar registada. Os RAW já existentes são preservados; a sua existência não é certificação de licença nem autorização retroativa.

A página oficial B3 **Pesquisa por Pregão** proíbe expressamente recolha automatizada, incluindo por ferramentas de IA, para qualquer finalidade. O workflow e o script correspondentes ficam desativados para captura. A proibição é aplicada àquela página/API; não é generalizada sem análise a todos os domínios B3.

## 2. Matriz de autorização por fonte

A fonte de verdade operacional é o registo estruturado [REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json](REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json).

| ID | Fonte / endpoint | Acesso técnico | Recolha automatizada | Armazenamento no GitHub público / backtest / produto | Decisão |
|---|---|---|---|---|---|
| `B3_PESQUISA_POR_PREGAO_API` | API usada pela página Pesquisa por Pregão | Endpoint identificado | **PROIBIDA** nos termos da página oficial | Não autorizado por este registo | Captura desativada; não contornar por endpoint interno |
| `B3_BDI_TABLE_API` | `https://arquivos.b3.com.br/bdi/table/...` | Endpoint técnico identificado no domínio B3 | **BLOQUEADA** até licença/termos confirmados | Não verificado | Gate fail-closed; manter RAW anterior sem promoção de novos dados |
| `B3_COTAHIST_DAILY` | `https://bvmf.bmfbovespa.com.br/InstDados/SerHist/...` | Arquivo histórico direto identificado; layout oficial rotulado “Informação Pública” | **BLOQUEADA temporariamente** até confirmação do âmbito de utilização | Não verificado para publicação/redistribuição e product development | Gate fail-closed para novas capturas/publicações; solicitar confirmação escrita à B3 |
| `B3_DRP_RAPINEGOCIOS` | `https://drp.b3.com.br/rapinegocios/tickercsv/...` | Descoberto por implementação independente de terceiros | **BLOQUEADA** — canal não confirmado oficialmente | Não verificado | Não executar captura até confirmação oficial |
| `BCB_COPOM_API_JSON` | API oficial do Copom | Catálogo oficial e API identificados | Permitida sob condições da licença aberta declarada no catálogo | ODbL; cumprir atribuição e obrigações aplicáveis a bases derivadas | Permitida com condições documentadas |
| `BCB_COPOM_PDF_ATTACHMENT` | PDF referenciado por `urlPdfAta` | PDF oficial capturado e validado tecnicamente | Captura técnica executada; âmbito específico da licença do anexo não confirmado separadamente | Redistribuição comercial não verificada | Preservar proveniência; confirmar âmbito do anexo antes de redistribuição/comercialização |

## 3. Evidência oficial e interpretação

### 3.1 B3 — Pesquisa por Pregão

Fonte: [página oficial Pesquisa por Pregão](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/).

A página declara que os dados são propriedade exclusiva da B3 e destinados estritamente a consulta informativa, vedando recolha automatizada, inclusive por IA, para fins comerciais ou não, próprios ou de terceiros.

**Decisão implementada:** desativar a recolha automatizada por essa página/API. Não tratar a acessibilidade técnica nem um token de download como autorização.

### 3.2 B3 — políticas de Market Data

Fontes oficiais:
- [Market Data B3 Consumption Policy V1.1](https://www.b3.com.br/data/files/66/61/27/F2/DCCFF91094DCD8F9AC094EA8/Market%20Data%20B3%20Consumption%20Policy%20V1.1.pdf)
- [Market Data B3 Commercial Policy 2026 V1.1](https://www.b3.com.br/data/files/CC/61/C9/7E/DCCFF91094DCD8F9AC094EA8/Market%20Data%20B3%20Commercial%20Policy%202026%20V1.1.pdf)
- [Novo sistema de contratação e reporte de Market Data B3](https://clientes.b3.com.br/en/w/new-market-data-b3-contracting-and-reporting-system)

A política comercial V1.1 consultada indica eficácia de **01/11/2026 a 31/12/2026**. Em 16/10/2026, não deve ser tratada como a versão já efetiva; a análise contratual deve confirmar a versão V1.0 aplicável até 31/10/2026 e preparar a transição para V1.1.

As políticas distinguem licença, dataset, profundidade, timeliness, aplicação Display/Non-Display, finalidade, acesso direto/indireto e reporte. Uma licença para uma finalidade não deve ser presumida como permissão para outra.

O layout COTAHIST rotulado “Informação Pública” prova a classificação publicada no documento de layout, **não resolve sozinho** os direitos de automação, armazenamento de uma cópia num repositório público, uso em desenvolvimento de produto ou redistribuição de dados históricos. É necessária confirmação escrita do âmbito concreto.

### 3.3 B3 — BDI API

Endpoint observado: `https://arquivos.b3.com.br/bdi/table/{endpoint}/{start}/{end}/{page}/{pageSize}`.

O domínio é da B3 e a API foi usada tecnicamente. Não foi localizada, nesta auditoria, uma licença pública específica ou autorização escrita que cubra o método automatizado POST, a frequência, a persistência no GitHub público e os usos posteriores. A regra da página Pesquisa por Pregão não é automaticamente estendida a este endpoint; a ausência de prova também não é convertida em autorização.

**Decisão:** bloquear novas capturas automáticas até a confirmação do termo/licença aplicável.

### 3.4 B3 — DRP/Rapinegócios

Endpoint candidato: `https://drp.b3.com.br/rapinegocios/tickercsv/{YYYY-MM-DD}?type=1`.

A descoberta veio de implementação independente, não de uma especificação oficial de autorização da B3. Não fazer chamadas automatizadas nem inferir autorização a partir da resposta HTTP, do formato ZIP ou da disponibilidade pública do host.

**Decisão:** bloqueado até a B3 confirmar por escrito o endpoint, a finalidade permitida, os limites de acesso, a retenção e os direitos de uso.

### 3.5 BCB — API Copom e PDF

O [catálogo oficial Copom do BCB](https://www.bcb.gov.br/conteudo/dadosabertos/BCBDeinf/elements_copom.html) declara a licença **Open Database License (ODbL)**. A ingestão do JSON pode prosseguir sob as obrigações aplicáveis de atribuição e compartilhamento da base derivada. A licença do conjunto não deve ser presumida como autorização ilimitada de redistribuição comercial de cada anexo externo: o PDF deve continuar identificado separadamente.

## 4. Controles técnicos implementados

1. Criado o registo estruturado de fontes e decisões de autorização.
2. Criado `scripts/governanca/validar_autorizacao_endpoint.py`, um gate fail-closed sem chamadas HTTP. Uma licença aberta só passa com licença, URL e âmbito explícitos; uma autorização B3 exige evidência contratual/escrita com referência, aprovador, data, validade, âmbito e hash da evidência.
3. O importador COTAHIST diário e o capturador BDI passam a consultar o gate antes de fazer pedidos.
4. O workflow de Pesquisa por Pregão passa a ser informativo e não executa recolha.
5. O workflow BDI deixa de executar captura automática enquanto o gate não autorizar.
6. A configuração candidata DRP/Rapinegócios inclui o gate antes de qualquer tentativa de download.
7. Nenhum RAW histórico foi apagado ou reescrito como parte desta decisão.

## 5. Evidências de autorização necessárias para desbloqueio

Para cada endpoint B3 bloqueado, anexar ou referenciar uma evidência emitida por autoridade competente que responda, no mínimo:

- endpoint exato, caminho/recurso e métodos HTTP permitidos;
- dataset e granularidade autorizados;
- frequência, limites de requisição, autenticação e uso de credenciais;
- finalidade: consulta, investigação interna, backtest, desenvolvimento de produto ou atividade comercial;
- permissão para armazenar RAW e NORMALIZED;
- permissão para manter os dados num repositório GitHub público;
- permissão para derivados, publicação e redistribuição;
- obrigações de atribuição, reporte, pagamento, retenção e eliminação;
- titular/entidade contratante, data de início e validade;
- identificador do contrato/autorização e hash da evidência arquivada ou referência privada auditável.

A aprovação deve ser por endpoint e finalidade. Um contrato genérico ou a autorização de um produto não deve ser extrapolado para endpoints ou usos não abrangidos.

## 6. Critérios de fecho

A pendência só passa a **CONCLUÍDA** quando:
1. a matriz tiver a evidência da autorização/licença vigente;
2. a fonte e a finalidade estiverem explicitamente abrangidas;
3. o registo estruturado for atualizado;
4. o gate automatizado passar para o estado autorizado;
5. a execução de teste provar que o gate bloqueia o estado pendente e permite apenas o estado aprovado;
6. a auditoria documental SHA-256 estiver conforme.

## 7. Estado final em 16/10/2026

- **Resolvido:** a proibição expressa da Pesquisa por Pregão foi aplicada tecnicamente; endpoints sem autorização comprovada passaram a bloquear novas capturas.
- **Autorizado com condições:** API JSON do Copom do BCB, sob ODbL.
- **Pendente de confirmação externa:** COTAHIST para automação/publicação no repositório público, BDI API, DRP/Rapinegócios e âmbito da licença do PDF Copom para redistribuição comercial.
- **Não afirmado:** que exista contrato ou autorização B3 que não esteja representado por evidência verificável.

Este registo é um controlo operacional e não substitui aconselhamento jurídico nem o contrato emitido pelo fornecedor dos dados.

## 8. Evidência de execução dos gates — 16/10/2026

| Controlo | Execução | Resultado comprovado |
|---|---|---|
| Pesquisa por Pregão | [run 38893246712](https://github.com/carlos-andrade/B3/actions/runs/38893246712) | Workflow de conformidade concluído; nenhuma chamada HTTP executada |
| COTAHIST diário | [run 38894476519](https://github.com/carlos-andrade/B3/actions/runs/38894476519) | Testes do gate passaram; autorização REVIEW_REQUIRED; job de importação foi **SKIPPED** |
| BDI API | [run 38894476389](https://github.com/carlos-andrade/B3/actions/runs/38894476389) | Testes do gate passaram; captura foi **SKIPPED** |
| BCB Copom JSON | [run 38894476513](https://github.com/carlos-andrade/B3/actions/runs/38894476513) | Sete testes passaram; captura JSON e validação NORMALIZED concluídas |
| PDF externo da Ata | Incluído na [run 38894476513](https://github.com/carlos-andrade/B3/actions/runs/38894476513) | O gate devolveu authorized=false; log confirmou PDF_ATTACHMENT_SKIPPED_LICENSE_SCOPE_UNCONFIRMED |
| Auditoria documental anterior à última atualização deste registo | [run 38893920324](https://github.com/carlos-andrade/B3/actions/runs/38893920324) | 332 documentos conformes, zero pendentes e zero divergentes no commit auditado; o registo foi posteriormente atualizado e a auditoria final está associada ao HEAD indicado no resultado desta execução |

Os jobs COTAHIST e BDI terminarem com sucesso significa que o controlo de autorização foi aplicado corretamente; **não** significa que a recolha de dados foi executada. O resultado de captura para esses dois endpoints é deliberadamente bloqueado.
