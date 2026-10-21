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
- **Testes unitários:** PASS — 11 testes concluídos em 0,222 s, sem falhas, no run [39621833806](https://github.com/carlos-andrade/B3/actions/runs/39621833806).
- **Auditoria integral:** PASS no mesmo run — 7/7 endpoints auditados, 3 permitidos pelo respetivo âmbito, 4 bloqueados, `errors=[]`.
- **Artefacto:** [b3-auditoria-autorizacao-endpoints](https://github.com/carlos-andrade/B3/actions/runs/39621833806/artifacts/12354514648), SHA-256 do ZIP `aab8a1bcd46b42b4e5097ca8f11a3dc3b37a5b871eea42b3ffb6b713fc849be9`, retenção indicada até 2026-11-20.
- **Critério de aceitação:** satisfeito para R2 neste commit auditado: todos os endpoints registados auditados, zero erros de controlo, e COTAHIST limitado a validação interna sem autorização de publicação. O run foi executado no commit `7d82dec1a37ab95feb290bcfc2e36ee432255bb1`; a revisão do commit posterior que contém este relatório está separadamente em execução.

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

### Execução FASE10 encontrada e correção do comparador

O run [39592181392](https://github.com/carlos-andrade/B3/actions/runs/39592181392), executado em 2026-10-21, concluiu com sucesso a validação RAW → NORMALIZED do candidato. Evidência registada:

- RAW candidato: SHA-256 `78032d39937bb540a57850a30ee3ef928462c5fa5c8dc073b2a10f64501740d0`, 94.685.771 bytes.
- NORMALIZED candidato: SHA-256 `e9319702ef63c9d2d89d5c7b3b67f496d4c538824bc666248320a618af4deecf`, 434.061.968 bytes.
- RAW e NORMALIZED: 3.233.168 registos de cotação, 25 campos, 0 comprimentos RAW inválidos; reconciliação de todas as linhas RAW → NORMALIZED = verdadeira.
- Candidato cobre `2026-01-02` a `2026-10-20`.
- O comparador original comparou o candidato apenas com o snapshot anual, não com a composição completa do dataset canónico (snapshot + incrementos diários validados). Produziu 90.258 linhas adicionais face ao snapshot anual, zero linhas canónicas ausentes e `full_row_multiset_unchanged=false`.

Por isso foi corrigido o workflow nesta branch para incluir os incrementos diários canónicos de 14 e 15 de outubro no cálculo de multiplicidade, preservar as ocorrências duplicadas e persistir a evidência na branch de trabalho, sem fazer push para `main`. A reexecução com comparação da composição completa está no run [39622127035](https://github.com/carlos-andrade/B3/actions/runs/39622127035); no momento deste registo, o run está em fila e ainda não há resultado final.

**Estado R3: VALIDADO SEM DIFERENÇAS DE LINHAS; GATE R4 DE PROMOÇÃO CONTINUA BLOQUEADO.** O artefacto FASE10 produzido no run [39628922181](https://github.com/carlos-andrade/B3/actions/runs/39628922181) comparou o candidato anual com a composição canónica vigente até 20/10/2026 (snapshot anual + incrementos diários de 14, 15, 16, 19 e 20 de outubro). O JSON foi preservado na branch de validação e os passos de verificação terminaram com sucesso.

Valores auditados:
- RAW candidato: SHA-256 `78032d39937bb540a57850a30ee3ef928462c5fa5c8dc073b2a10f64501740d0`; 94.685.771 bytes.
- NORMALIZED candidato: SHA-256 `e9319702ef63c9d2d89d5c7b3b67f496d4c538824bc666248320a618af4deecf`; 434.061.968 bytes.
- NORMALIZED anual canónico: SHA-256 `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`.
- RAW e NORMALIZED: 3.233.168 registos de cotação; 25 campos; zero comprimentos RAW inválidos; todas as linhas RAW reconciliadas campo a campo para NORMALIZED.
- Composição canónica (snapshot + 5 incrementos diários): 3.233.168 linhas; candidato: 3.233.168 linhas.
- Diferenças por SHA-256 da linha integral com multiplicidade preservada: `candidate_rows_added_vs_canonical=0`, `canonical_rows_absent_from_candidate=0`, `full_row_multiset_unchanged=true`. Nenhuma deduplicação foi aplicada.
- Relatório FASE10: `status=VALIDADO_SEM_DIFERENCAS_DE_LINHAS`, `canonical_mutated=false`, `raw_committed=false`, `normalized_committed=false`, `promotion_authorized=false`.

A diferença anterior de 53.275 linhas resultava de comparar com uma composição incompleta terminada em 15/10; corresponde exatamente aos incrementos canónicos então ausentes: 16/10 (23.018 linhas), 19/10 (15.046) e 20/10 (15.211). O candidato não tem diferença de linhas frente à composição canónica atual.

## 4. R4 — Histórico e permissões

### Evidência histórica existente

A história do manifesto anual mostra mudança de estado sem mudança do hash/contagem do NORMALIZED:
- Commit [3e49146](https://github.com/carlos-andrade/B3/commit/3e4914638dedb5bec1935abd4a9821e5ddc4cfc6), 14/10: `VALIDADO`, SHA `e7763b6f…71f4cbdc`, 3.142.910 linhas, 25 campos, datas 02/01–13/10.
- Commit [7363a76](https://github.com/carlos-andrade/B3/commit/7363a76884198450e4d34687cc3ab5e81663b4dd), 16/10: estado alterado para `BLOQUEADO` devido à divergência de cobertura e à necessidade de demonstrar autorização compatível.
- Commit [45058d8](https://github.com/carlos-andrade/B3/commit/45058d87a8ee076bf6d8f8a8f66a2849e1a87b0c): mantém bloqueio por autorização não demonstrada e conflito histórico de validação.
- Commit [6da968c](https://github.com/carlos-andrade/B3/commit/6da968cc85da50528d2fcf2dfeb6d633cf3111fb), 16/10: mantém `BLOQUEADO`, qualificando a divergência histórica como não reproduzida no HEAD então auditado; SHA e contagem permanecem iguais.

O manifesto regista `HISTORICAL_VALIDATION_OUTPUT_CONFLICT`: uma execução anterior reportou primeira data `2026-01-07`, enquanto a evidência mais recente registou `2026-01-02`. A reprodução M3-1C confirmou RAW → NORMALIZED, SHA e tamanho idênticos para o HEAD então auditado; a causa dos logs antigos continua desconhecida. O run FASE10 de 21/10 confirmou a nova fonte anual até 20/10, mas a reconciliação contra a composição canónica completa está a ser repetida nesta branch.

### Âmbito de armazenamento/publicação

- A decisão de governação do registo autoriza, de forma limitada, aquisição controlada do endpoint direto de ficheiros para validação técnica e processamento interno.
- A decisão **não é uma licença emitida pela B3 nem um parecer jurídico**.
- Não está autorizada por este registo a publicação de novos ficheiros RAW num repositório público, a redistribuição, o uso comercial ou o desenvolvimento de produto.
- Os termos aplicáveis de Market Data, a política de consumo e eventuais direitos contratuais devem ser verificados para o uso concreto antes de publicar/redistribuir.
- O estado do endpoint direto não deve ser extrapolado para Pesquisa por Pregão, BDI, DRP ou outros endpoints.

**Estado R4: BLOQUEADO POR AUTORIZAÇÃO DE PUBLICAÇÃO/REDISTRIBUIÇÃO PENDENTE.** A validação técnica da FASE10 passou, mas o manifesto anual permanece `BLOQUEADO` com `SOURCE_AUTHORIZATION_REVIEW_REQUIRED` (`OPEN`). O registo oficial permite aquisição controlada para validação interna e declara `storage_and_redistribution=REVIEW_REQUIRED_BEFORE_PUBLICATION`; não contém `publication_authorized=true`. A equivalência técnica não autoriza promover ou redistribuir RAW/anual NORMALIZED.

A correção EXDEV e de concorrência foi integrada na [PR #26](https://github.com/carlos-andrade/B3/pull/26). O run [39629823149](https://github.com/carlos-andrade/B3/actions/runs/39629823149) passou no gate de autorização operacional, importação, reconciliação, gate de conflitos e upload de evidência. A correção que separa aquisição interna de publicação foi integrada na [PR #28](https://github.com/carlos-andrade/B3/pull/28), commit [6b8fded](https://github.com/carlos-andrade/B3/commit/6b8fded9157251f2452c3cc00662b6ecd134f541): antes de persistir qualquer dado, o workflow exige autorização explícita e escopo de publicação permitido no registo. O run de PR [39630975069](https://github.com/carlos-andrade/B3/actions/runs/39630975069) passou; a persistência foi corretamente ignorada no evento PR.

**Limite da remediação:** o novo gate deve impedir novas publicações automáticas sem autorização explícita; não reescreve nem apaga artefactos que já se encontram no histórico público Git. Nenhum artefacto canónico foi promovido por esta auditoria.

## 5. Decisão formal de promoção

**DECISÃO: PROMOÇÃO BLOQUEADA. R2 E R3 TÉCNICAS PASSARAM; R4 DE PUBLICAÇÃO CONTINUA PENDENTE.**

Fundamentos:
1. R2: 11 testes unitários e auditoria de 7/7 endpoints com `errors=[]`; o âmbito COTAHIST permanece limitado a uso interno.
2. R3: candidato e composição canónica integral coincidem em 3.233.168 linhas; hashes recalculados, 25 campos reconciliados e multiplicidade idêntica.
3. R4: o manifesto anual continua `BLOQUEADO` por revisão de autorização; o registo não concede publicação/redistribuição.
4. O gate fail-closed de publicação foi integrado; falta confirmar a sua execução pós-merge em `main`.

### Condições para reabrir a decisão

- [x] Testes unitários R2 concluídos com sucesso no GitHub Actions.
- [x] Auditoria integral R2 concluída; 7/7 endpoints auditados, `errors=[]`; artefacto de evidência preservado.
- [x] FASE10 R3 executada com hashes recalculados, 25 campos reconciliados e igualdade integral de multiplicidade: 3.233.168 linhas, zero adicionais e zero ausentes.
- [x] Diferença histórica de 53.275 linhas classificada como incrementos de 16, 19 e 20/10 que não estavam incluídos na composição da comparação anterior.
- [ ] Reconciliar o estado semântico do dataset `VIGENTE/VALIDADO` e do manifesto anual `BLOQUEADO` sem converter bloqueio de autorização em aprovação de publicação.
- [ ] Documentar licença/autorização que cubra armazenamento público e redistribuição, incluindo evidência contratual/escrita e âmbito aplicável.
- [ ] Confirmar no run de `main` pós-PR #28 o resultado `PERSISTENCIA_BLOQUEADA` e a ausência de novas alterações aos artefactos canónicos.
- [ ] Registar a aprovação explícita da pessoa responsável, com data, âmbito, evidências e hash da decisão.

Até que todos os itens aplicáveis estejam satisfeitos e exista aprovação explícita, não promover, não publicar novos RAW e não alterar o estado para `LIBERADO`.

## 6. Proveniência principal

- Registo de autorização: `docs/governanca/licenciamento/REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json`
- Validador: `scripts/governanca/validar_autorizacao_endpoint.py`
- Testes: `scripts/governanca/test_validar_autorizacao_endpoint.py`
- Workflow de auditoria: `.github/workflows/b3-auditoria-autorizacao-endpoints.yml`
- Dataset corrente: `dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json`
- Manifesto anual: `dados/cotahist/normalized/manifests/COTAHIST_A2026_quality.json`
- Manifests diários: `dados/cotahist/normalized/manifests/diario/COTAHIST_D14102026_quality.json`, `COTAHIST_D15102026_quality.json`, `COTAHIST_D16102026_quality.json`, `COTAHIST_D19102026_quality.json` e `COTAHIST_D20102026_quality.json`
- Workflow diário e gate de publicação: `.github/workflows/cotahist-importacao-diaria-v1.yml`
- Relatório FASE10 com igualdade de multiplicidade (branch auditada): `dados/cotahist/quality/COTAHIST_2026_FASE10_VALIDACAO_CANDIDATO_V1.json`, blob SHA `6baa2208ba48e8f5f10e8e14e3a6d73a65f5388b`
- FASE10 histórica de 2017 (referência metodológica, não prova de 2026): `dados/cotahist/quality/COTAHIST_2017_FASE10_VALIDACAO_INDEPENDENTE_V1.json`
