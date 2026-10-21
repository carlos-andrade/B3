# Auditoria R2–R4 e decisão de promoção — COTAHIST

- **Data da auditoria:** 2026-10-21
- **Repositório:** `carlos-andrade/B3`
- **Branch de trabalho:** `audit/r2-r3-r4-promotion-gate-2026-10-21`
- **Política de promoção:** bloqueada até evidência técnica suficiente e aprovação explícita
- **Âmbito:** gate de autorização, integridade do dataset COTAHIST, comparação histórica e direitos de armazenamento/publicação

## 1. Resumo executivo

**Decisão: NÃO PROMOVER.** A integridade declarada no manifesto não substitui a execução atual da FASE10, e a autorização operacional limitada do endpoint direto B3 não concede direitos de publicação de RAW, redistribuição ou uso comercial. A promoção só pode ser reavaliada depois de os gates R2 e R3 terminarem com evidência reproduzível e de a revisão histórica R4 estar documentada.

## 2. R2 — Gate de autorização

### Evidência de código observada

- O registo versionado declara a política global `FAIL_CLOSED`.
- O endpoint `B3_COTAHIST_DAILY` usa o estado `OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED`.
- O validador só permite esse estado quando identifica aquisição controlada para validação, revisão obrigatória antes de publicação, limites de âmbito para processamento interno e uma decisão que não presume direitos de publicação.
- A saída do gate define `operation_scope=INTERNAL_VALIDATION_ONLY` e `publication_authorized=false` para esse estado.
- Estados desconhecidos, endpoints não registados e estados sem evidência suficiente são bloqueados por omissão.

### Defeito encontrado e correção proposta nesta branch

O teste `test_limited_scope_without_required_controls_fails_closed` continha todos os controlos e esperava `allowed=True`, contradizendo o nome do teste. Foi corrigido para verificar separadamente quatro omissões de controlo (cada uma deve bloquear) e o cenário completo válido (permitido apenas para validação interna).

O workflow de auditoria foi também ajustado para correr em branches `audit/**` e em pull requests relevantes, para que o gate possa ser verificado antes de qualquer integração.

### Estado de execução

- **Revisão estática:** efetuada.
- **Correção de teste/workflow:** commitada nesta branch.
- **Testes unitários e auditoria integral:** aguardam resultado do GitHub Actions para esta branch; não declarar PASS antes de consultar o run e o artefacto `authorization_audit.json`.
- **Critério de aceitação:** todos os endpoints registados auditados, zero erros de controlo, estados desconhecidos bloqueados, e COTAHIST limitado a validação interna sem autorização de publicação.

## 3. R3 — FASE10: SHA-256, 25 campos e multiplicidade

### Valores atualmente declarados no repositório

| Artefacto | SHA-256 declarado | Linhas | Campos | Estado do manifesto |
|---|---|---:|---:|---|
| `COTAHIST_A2026.csv` | `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc` | 3.142.910 | 25 | `BLOQUEADO` |
| `COTAHIST_D14102026.csv` | `196b573c89e0a4fbf1b460b9a3c7390971758f1b5c1949cbbfe56bd287288aa9` | 18.156 | 25 | `VALIDADO` |
| `COTAHIST_D15102026.csv` | `e67473ac5c636f98c755094be50e66e14eeb124b28cb2b503c3384373c00bef0` | 18.827 | 25 | `VALIDADO` |

Estes são valores **registados nos manifests**, não uma afirmação de que foram recalculados nesta auditoria.

### Divergência de estado

O manifesto `COTAHIST_A2026_quality.json` está `BLOQUEADO` por `SOURCE_AUTHORIZATION_REVIEW_REQUIRED`, enquanto `COTAHIST_DATASET_ATUAL_V1.1.json` declara o dataset corrente `VIGENTE` e `status_frescor=VALIDADO`. Essa diferença de semântica/estado precisa de ser reconciliada antes da promoção; não se deve converter um bloqueio de autorização em aprovação de publicação.

### Validações FASE10 ainda exigidas

1. Ler os bytes atuais dos RAW e NORMALIZED canónicos e recalcular os respetivos SHA-256.
2. Validar cabeçalho/estrutura e reconciliar, campo a campo, os 25 campos do layout oficial.
3. Comparar contagem e multiplicidade das linhas entre RAW e NORMALIZED, sem deduplicação silenciosa.
4. Guardar contagens de divergências, amostras reproduzíveis, hashes, versão do parser e timestamp UTC no artefacto FASE10.
5. Comparar o resultado com o dataset canónico e os manifests diários incluídos na composição vigente.

**Estado R3: NÃO VALIDADO nesta execução.** Os dados consultados fornecem hashes e contagens registados, mas não comprovam o recálculo atual nem a reconciliação independente das linhas. A promoção fica bloqueada até a execução real gerar evidência E3/E4.

## 4. R4 — Histórico e permissões

### Evidência histórica existente

O manifesto anual regista `HISTORICAL_VALIDATION_OUTPUT_CONFLICT`: uma execução anterior reportou primeira data `2026-01-07`, enquanto a evidência mais recente registou `2026-01-02`. O mesmo manifesto declara que a reprodução M3-1C confirmou RAW → NORMALIZED, SHA e tamanho idênticos para o HEAD então auditado, com 3.142.910 linhas e última data `2026-10-13`; a causa dos logs históricos anteriores permanece desconhecida. Esta anotação histórica não substitui a repetição da FASE10 no HEAD atual.

### Âmbito de armazenamento/publicação

- A decisão de governação do registo autoriza, de forma limitada, aquisição controlada do endpoint direto de ficheiros para validação técnica e processamento interno.
- A decisão **não é uma licença emitida pela B3 nem um parecer jurídico**.
- Não está autorizada por este registo a publicação de novos ficheiros RAW num repositório público, a redistribuição, o uso comercial ou o desenvolvimento de produto.
- Os termos aplicáveis de Market Data, a política de consumo e eventuais direitos contratuais devem ser verificados para o uso concreto antes de publicar/redistribuir.
- O estado do endpoint direto não deve ser extrapolado para Pesquisa por Pregão, BDI, DRP ou outros endpoints.

**Estado R4:** limites de autorização documentados; auditoria comparativa integral de artefactos históricos continua dependente da FASE10 atual e da reconciliação dos estados dos manifests.

## 5. Decisão formal de promoção

**DECISÃO: PROMOÇÃO BLOQUEADA.**

Fundamentos:
1. A auditoria integral R2 tem de terminar com todos os endpoints auditados, zero erros e artefacto verificável.
2. A FASE10 R3 ainda não demonstrou nesta execução hashes recalculados, reconciliação dos 25 campos e igualdade de multiplicidade.
3. O manifesto anual e o dataset corrente têm estados que necessitam de reconciliação explícita.
4. Os direitos de publicação e redistribuição dos dados B3 não estão demonstrados pelo registo de autorização operacional limitada.

### Condições para reabrir a decisão

- [ ] Testes unitários R2 concluídos com sucesso no GitHub Actions.
- [ ] Auditoria integral R2 concluída; `audited_count = endpoint_count`, `errors = []`; artefacto preservado.
- [ ] FASE10 R3 executada no HEAD candidato, com SHA-256 recalculados, 25 campos reconciliados e multiplicidade reconciliada.
- [ ] Diferenças históricas explicadas ou explicitamente classificadas como não resolvidas, sem ocultar divergências.
- [ ] Estados do manifesto anual e do dataset canónico reconciliados.
- [ ] Direitos aplicáveis a armazenamento, publicação e redistribuição documentados para o âmbito pretendido.
- [ ] Aprovação explícita da pessoa responsável registada com data, âmbito, evidências e hash da decisão.

Até que todos os itens aplicáveis estejam satisfeitos e exista aprovação explícita, não promover, não publicar novos RAW e não alterar o estado para `LIBERADO`.

## 6. Proveniência principal

- Registo de autorização: `docs/governanca/licenciamento/REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json`
- Validador: `scripts/governanca/validar_autorizacao_endpoint.py`
- Testes: `scripts/governanca/test_validar_autorizacao_endpoint.py`
- Workflow de auditoria: `.github/workflows/b3-auditoria-autorizacao-endpoints.yml`
- Dataset corrente: `dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json`
- Manifesto anual: `dados/cotahist/normalized/manifests/COTAHIST_A2026_quality.json`
- Manifests diários: `dados/cotahist/normalized/manifests/diario/COTAHIST_D14102026_quality.json` e `COTAHIST_D15102026_quality.json`
- FASE10 histórica de 2017 (referência metodológica, não prova de 2026): `dados/cotahist/quality/COTAHIST_2017_FASE10_VALIDACAO_INDEPENDENTE_V1.json`
