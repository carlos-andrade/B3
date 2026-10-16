# B3 — REGISTRO DE CAPTURAS RAW E RECONCILIAÇÃO DE FONTES

| Campo | Valor |
|---|---|
| **ID** | B3-INGESTAO-RAW-RECONCILIACAO-20261016 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | REGISTRO_OPERACIONAL |
| **Fase** | CAPTURA_RAW_E_RECONCILIACAO |
| **Estado** | EM_CURSO_COM_BLOQUEIOS_EXPLICITOS |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 9306ddd65261ac9ea71774c8984976430ed3afad758dcdc14f493a767fe16a1b |
| **Commit de referência (versão anterior)** | N/A — registo operacional inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório |
| **Origem** | Artefactos RAW, manifestos e execuções GitHub Actions do repositório B3 |
| **Autoridade superior** | [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objetivo e regra de fecho

Consolidar o estado comprovado das capturas RAW e reconciliações de fontes. Um ficheiro normalizado ou uma página que identifica uma fonte não substitui a captura do artefacto bruto. Cada captura deve ter origem, data, caminho, SHA-256, tamanho, contagem e validação; os dados canónicos só podem ser promovidos após os gates correspondentes.

## 2. Capturas e reconciliações executadas em 2026-10-16

### 2.1 COTAHIST diário — fonte oficial B3

**Estado: CAPTURADO, NORMALIZADO E RECONCILIADO SEM CONFLITOS.**

- Execução diária: [run 38889032782](https://github.com/carlos-andrade/B3/actions/runs/38889032782) — sucesso.
- Relatório da execução: [COTAHIST_DIARIO_EXECUCAO_20261016T013436Z.json](../../dados/cotahist/quality/diario/execucoes/COTAHIST_DIARIO_EXECUCAO_20261016T013436Z.json).
- Data de referência mais recente: 2026-10-15; estado `IMPORTED`.
- RAW: `dados/cotahist/raw/diario/COTAHIST_D15102026.ZIP`.
- SHA-256 RAW: `346a8ec8ab89db34c5ff2388246d6f658a5e04d989fd549d0ba57e52d90967c8`.
- NORMALIZED: `dados/cotahist/normalized/diario/COTAHIST_D15102026.csv`.
- SHA-256 NORMALIZED: `e67473ac5c636f98c755094be50e66e14eeb124b28cb2b503c3384373c00bef0`.
- Manifesto: `dados/cotahist/normalized/manifests/diario/COTAHIST_D15102026_quality.json`; estado `VALIDADO`, 18.827 registos, 25 campos, data única 2026-10-15.
- Backfill de 7 dias: 14/10, 13/10 e 09/10 sem alteração; 12/10, 11/10 e 10/10 sem ficheiro/pregão; zero conflitos.
- Dataset corrente [COTAHIST_DATASET_ATUAL_V1.1.json](../../dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json) aponta para 2026-10-15. O snapshot anual permanece imutável até 13/10; 14/10 e 15/10 entram como incrementos diários validados.

### 2.2 BDI — endpoint DailyAverageStocks

**Estado: CAPTURADO E MANIFESTADO; cobertura limitada ao endpoint/tabela.**

- Execução: [run 38889119047](https://github.com/carlos-andrade/B3/actions/runs/38889119047) — sucesso.
- Data de referência: 2026-10-15.
- RAW: `dados/bdi/raw/DailyAverageStocks/2026-10-15/page_0001.json`.
- Manifesto: `dados/bdi/manifests/DailyAverageStocks/2026-10-15_page_0001.json`.
- SHA-256: `47bebb4f051628db066e1df44e661e31a7013194667bd252b530cd90b0559446`.
- Tamanho: 3.028 bytes; 4 colunas; 9 registos; página 1.
- O manifesto e o RAW foram produzidos pelo mesmo processo de captura e persistidos. Isto comprova a captura desta tabela, não a captura integral de todas as tabelas do BDI.

### 2.3 BCB/Copom — API oficial, reunião 281

**Estado: RAW API CAPTURADO, NORMALIZED VALIDADO E PUBLICADO.**

- Execução: [run 38889256929](https://github.com/carlos-andrade/B3/actions/runs/38889256929) — sucesso após correção de concorrência Git.
- A validação NORMALIZED terminou com `OK: 1 eventos BCB/Copom validados`.
- Lista de Atas: `dados/calendario_economico/copom/raw/atas_lista.json`; SHA-256 `11c2c2391585e482a428e43c8056a1813d278f3d6a8e8ec9d416cf087810a30d`, 642 bytes.
- Lista de Comunicados: `dados/calendario_economico/copom/raw/comunicados_lista.json`; SHA-256 `860788c5244763a35f358c634cbdf445b79312f00f2efeb9e412bee699e20d7c`, 615 bytes.
- Detalhe da Ata 281: `dados/calendario_economico/copom/raw/atas_detalhes_281.json`; SHA-256 `fa402b27a6424c01d96fccce81f58347cc35dcb390e23d1fa31f2207792eba98`, 19.791 bytes.
- Detalhe do Comunicado 281: `dados/calendario_economico/copom/raw/comunicados_detalhes_281.json`; SHA-256 `c32e5fccaba8d550544472f72f03222eb880fbb543674f77eb89d565d4dc9b66`, 6.503 bytes.
- Metadados `.meta.json` registam URLs solicitados/finais, hora de captura, tipo de conteúdo, tamanho e SHA-256. NORMALIZED: `dados/calendario_economico/copom/normalized/copom_281.json`.
- A resposta JSON da API e o texto da Ata fornecido pela API foram capturados. **O PDF oficial binário da Ata foi capturado e validado** em `dados/calendario_economico/copom/raw/ata_281.pdf`; SHA-256 `f03423dc25625aa14ae29c10fdacf7b4665b6714ab0667c0dc86a6f77c43665c`, 401.502 bytes, `application/pdf`, assinatura `%PDF-` validada. Metadados em `ata_281.pdf.meta.json`.

## 3. Pendências reais e bloqueios

### P0 — Negócio a negócio de derivativos (BDM)

**PENDENTE — NÃO PROMOVER NEM CALCULAR CUMULATIVE DELTA.**

A rota oficial identificada é B3 → Boletim Diário do Mercado → Derivativos → Derivativos de bolsa → Negócio a negócio. A documentação vigente da B3 informa que a página Pesquisa por Pregão veda coleta automatizada. Por isso, não foi executada nem será contornada a captura automatizada dessa página.

Para fechar a pendência, é necessário obter por via autorizada o arquivo bruto das datas de referência 16/09/2026 e 17/09/2026 e persistir, por arquivo: URL/recurso exato, data de referência, formato, tamanho, SHA-256, colunas/layout, contagem de registos, intervalo temporal e contratos presentes. Até essa prova, o dataset trade-by-trade, o campo agressor e o Cumulative Delta permanecem não confirmados.

Referências:
- [B3 — Pesquisa por Pregão e termos de uso](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/)
- [B3 — Cotações: migração para o BDM](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/cotacoes/)
- [Especificação de fonte e reconciliação](PARTE03_NEGOCIO_A_NEGOCIO_RECONCILIACAO_FONTE_V1.0.md)

### P1 — PDF binário da Ata Copom 281

**CONCLUÍDO — PDF ORIGINAL CAPTURADO.**

O workflow [run 38889815903](https://github.com/carlos-andrade/B3/actions/runs/38889815903) capturou o PDF oficial, verificou a assinatura `%PDF-` e persistiu o binário e o sidecar de metadados. SHA-256 `f03423dc25625aa14ae29c10fdacf7b4665b6714ab0667c0dc86a6f77c43665c`; tamanho 401.502 bytes. O JSON API permanece preservado separadamente.

### P1 — Timestamp intradiário exato do Comunicado Copom

**PENDENTE POR FALTA DE EVIDÊNCIA TEMPORAL.**

A data da decisão está documentada, mas o horário exato de publicação não foi confirmado. Manter `event_time_status=UNKNOWN`; não atribuir uma hora sintética nem permitir look-ahead em backtests.

### P2 — Cobertura integral do BDI

**PARCIAL.**

A captura validada cobre apenas `DailyAverageStocks`, data 15/10/2026, página 1. Não declarar todo o BDI reconciliado. Cada capítulo/tabela prioritário precisa de captura RAW e manifesto próprios.

## 4. Corrida concorrente corrigida

A primeira execução BCB em 16/10 capturou e validou os dados, mas o push falhou porque a captura BDI publicou um commit concorrente. O workflow BCB foi corrigido para executar `git pull --rebase origin main` antes do push. A reexecução [38889256929](https://github.com/carlos-andrade/B3/actions/runs/38889256929) terminou com sucesso. Não houve necessidade de reescrever o histórico.

## 5. Roadmap

| Etapa | Estado | Critério de saída |
|---|---|---|
| COTAHIST diário até 15/10 | CONCLUÍDO | RAW + manifesto + NORMALIZED validado; zero conflitos |
| BDI DailyAverageStocks 15/10 | CONCLUÍDO | RAW + SHA-256 + manifesto; 9 registos |
| BCB/Copom API 281 | CONCLUÍDO | 4 capturas RAW com metadados + NORMALIZED validado |
| PDF binário da Ata 281 | CONCLUÍDO | PDF original guardado, hash/tamanho verificados |
| BDM negócio a negócio | BLOQUEADO POR AUTORIZAÇÃO/ACESSO | Captura autorizada, layout e contagem reconciliados |
| Timestamp exato do Comunicado | PENDENTE | Fonte oficial com timestamp verificável |
| Cobertura integral do BDI | PARCIAL | Matriz por capítulo/tabela com evidências por data |

**Regra de promoção:** nenhuma pendência P0 pode ser marcada como concluída por inferência, por metadados de uma fonte diferente ou por documentação da rota de acesso. Os artefactos RAW permanecem imutáveis; as correções são registadas como novas capturas/versionamentos.
