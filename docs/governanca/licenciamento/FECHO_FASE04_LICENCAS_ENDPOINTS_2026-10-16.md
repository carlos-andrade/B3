# Relatório de execução — Fase 04: licenciamento e autorização de endpoints

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-FASE04-LIC-EP-20261016 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_FECHO_FASE_OPERACIONAL |
| **Fase** | FASE 04 — Licenciamento e autorização de endpoints |
| **Estado** | AUDITORIA TÉCNICA APROVADA; AUTORIZAÇÕES EXTERNAS PENDENTES; FAIL_CLOSED |
| **Versão** | 1.0.2 |
| **SHA-256 (conteúdo canónico)** | 15fa1a5a026aee0b5225a3833ba9b333854be660d297e47d5bc024c44347f64c |
| **Commit de referência (versão anterior)** | [65d284ea0a624ef1772eb476e537cebdd62a7574](https://github.com/carlos-andrade/B3/commit/65d284ea0a624ef1772eb476e537cebdd62a7574) |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — autorização externa não inferida |
| **Origem** | Registo versionado de autorização, gate Python e testes unitários |
| **Autoridade superior** | [Carta Magna B3](../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

## 1. Decisão executiva

A Fase 04 operacional foi identificada como a verificação de licenças e autorização dos endpoints, usando como fonte de verdade o registo `docs/governanca/licenciamento/REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json` e o gate `scripts/governanca/validar_autorizacao_endpoint.py`.

**Resultado:** controlos técnicos existentes verificados; a autorização comercial/jurídica externa não está completa. O estado final é **PARCIAL — FAIL_CLOSED**, não uma liberação geral de ingestão.

A acessibilidade HTTP, a existência de dados RAW e a conclusão anterior de workflows não constituem licença nem autorização retroativa. Nenhum pedido de autorização foi inventado ou apresentado como aprovado.

## 2. Inventário de autorização

O registo contém seis IDs únicos e aplica a política `FAIL_CLOSED`.

| Endpoint ID | Estado registado | Decisão operacional |
|---|---|---|
| `B3_PESQUISA_POR_PREGAO_API` | `PROHIBITED_AUTOMATED_COLLECTION` | Recolha automatizada proibida; não contornar pela API ou por rota alternativa |
| `B3_BDI_TABLE_API` | `REVIEW_REQUIRED` | Novas capturas bloqueadas até licença/termos ou autorização escrita |
| `B3_COTAHIST_DAILY` | `REVIEW_REQUIRED` | Novas capturas/publicações automatizadas bloqueadas até confirmação escrita do âmbito |
| `B3_DRP_RAPINEGOCIOS` | `REVIEW_REQUIRED` | Bloqueado até confirmação oficial de endpoint, finalidade, limites e direitos de uso |
| `BCB_COPOM_API_JSON` | `AUTHORIZED_WITH_CONDITIONS` | Permitido apenas no âmbito ODbL documentado, com atribuição e obrigações aplicáveis |
| `BCB_COPOM_PDF_ATTACHMENT` | `REVIEW_REQUIRED` | Anexo separado; direitos de armazenamento/redistribuição ainda não confirmados |

O resultado não transforma a permissão condicional do JSON Copom em permissão irrestrita para os PDFs anexos.

## 3. Verificações técnicas realizadas

- Inspeção do registo estruturado: seis endpoints; IDs únicos; política global `FAIL_CLOSED`.
- Inspeção do validador: consulta apenas o registo versionado; não realiza chamadas de rede; endpoint desconhecido bloqueia por omissão.
- Inspeção dos testes unitários: casos de endpoint proibido, endpoints B3 pendentes, API Copom ODbL, endpoint desconhecido, estado `AUTHORIZED` sem prova contratual e exigência de licença/escopo explícitos.
- Inspeção dos workflows de ingestão COTAHIST diário e BDI: ambos executam testes de autorização e avaliam o gate antes do job de captura; o job de ingestão/captura depende de `authorized == 'true'`.
- Inspeção do script Pesquisa por Pregão: o gate é chamado antes de qualquer pedido HTTP; a recolha automatizada proibida falha fechada.
- Não foram executadas chamadas aos endpoints B3/BDI/DRP, nem tentativas de contornar restrições.
- Auditoria automatizada do registo: [run 38901173441](https://github.com/carlos-andrade/B3/actions/runs/38901173441) — **success** no HEAD `0e0ae4bfec21648171966e60d7c8a8562965e04e`; os testes unitários passaram, os seis endpoints foram avaliados, um ficou autorizado sob condições e cinco bloqueados, sem erros de controlo. Artefacto: [b3-auditoria-autorizacao-endpoints](https://github.com/carlos-andrade/B3/actions/runs/38901173441/artifacts/12045768807).

## 4. Critérios de saída

- [x] Registo estruturado de autorização identificado como fonte de verdade operacional.
- [x] Estados dos seis endpoints reconciliados com as decisões documentadas.
- [x] Gate técnico e testes unitários existentes inspecionados.
- [x] Workflows COTAHIST e BDI inspecionados para gate antes da captura.
- [x] Proibição da Pesquisa por Pregão preservada; sem rota alternativa.
- [x] O JSON Copom limitado ao escopo ODbL declarado; PDF separado.
- [ ] Confirmação escrita da B3 para o âmbito COTAHIST: pesquisa interna, armazenamento, backtests, desenvolvimento de produto e publicação/redistribuição.
- [ ] Termos/licença aplicáveis ao endpoint BDI e autorização para automação/armazenamento.
- [ ] Confirmação oficial do endpoint DRP/Rapinegócios e respetivos direitos.
- [ ] Confirmação de licença do PDF Copom para armazenamento/redistribuição pretendidos.

## 5. Bloqueios e decisão de segurança

Os quatro pedidos de confirmação externa acima não podem ser resolvidos apenas por alteração de código. Enquanto não houver evidência oficial registada, os gates continuam bloqueados. A rotina diária COTAHIST e a captura BDI não podem ser consideradas autorizadas para novas recolhas só porque existem workflows agendados.

Esta decisão não altera os dados históricos já persistidos, não reescreve RAW ou NORMALIZED e não reabre anos COTAHIST encerrados. COTAHIST 1986–2025 mantém-se em modo de consulta; 2026 continua incremental apenas na medida permitida pela autorização efetiva. `BLOOMBERG_MAIL` permanece fora do âmbito B3.

## 6. Próximas ações autorizadas

1. Obter confirmação escrita da B3 sobre os usos pretendidos do COTAHIST e registar documento, escopo, vigência e SHA-256 da evidência.
2. Obter termos/licença oficiais específicos para BDI e DRP antes de reativar captura.
3. Confirmar separadamente os direitos aplicáveis ao PDF da Ata Copom.
4. Manter os gates fail-closed e reexecutar a auditoria após cada alteração documentada do registo.
5. Não tratar esta fase como autorização jurídica/comercial final até os documentos externos serem validados.

## 7. Limitações

Este fecho verifica a implementação e a coerência do registo versionado; não é parecer jurídico, contrato da B3, nem confirmação externa de direitos de uso. O estado final é parcial enquanto as evidências externas permanecerem ausentes.
