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

**Estado R3: VALIDADO TECNICAMENTE COM DIFERENÇAS REPRODUZIDAS; PROMOÇÃO NÃO AUTORIZADA.** O run [39624008823](https://github.com/carlos-andrade/B3/actions/runs/39624008823) concluiu a validação técnica da composição completa com sucesso (o passo de persistência também terminou com sucesso na branch de trabalho). Resultado do artefacto FASE10:
- RAW candidato SHA-256 `78032d39937bb540a57850a30ee3ef928462c5fa5c8dc073b2a10f64501740d0`; tamanho 94.685.771 bytes.
- NORMALIZED candidato SHA-256 `e9319702ef63c9d2d89d5c7b3b67f496d4c538824bc666248320a618af4deecf`; tamanho 434.061.968 bytes.
- SHA do NORMALIZED anual canónico: `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`.
- 3.233.168 registos candidatos e 25 campos; 0 comprimentos RAW inválidos; todas as linhas reconciliadas do RAW para o NORMALIZED.
- Composição canónica comparada: 3.179.893 linhas (snapshot anual + incrementos diários 14/10 e 15/10); candidato contém 53.275 linhas a mais e 0 linhas canónicas ausentes. `full_row_multiset_unchanged=false`.
- O estado correto é `VALIDADO_COM_DIFERENCAS_A_REVISAR), não igualdade integral e não elegibilidade para promoção.

A execução de PR [39624052757](https://github.com/carlos-andrade/B3/actions/runs/39624052757) confirmou estes mesmos números, mas falhou ao persistir a evidência porque a rotina tentou buscar a ref sintética `22/merge`. O workflow foi corrigido para obter a branch `pull_request.head.ref`; novas execuções em PR estão em curso. A evidência já foi registada na branch da FASE10, sem modificar o dataset canónico.

### Correção do workflow de evidências após a comparação

O workflow de FASE10 agora resolve a branch remota corretamente quando o evento é `pull_request`, em vez de usar `GITHUB_REF_NAME=<número>/merge`. Foi incluída validação explícita do resultado conhecido (53.275 linhas adicionais, zero linhas canónicas ausentes e 25 campos reconciliados), para que as diferenças não sejam tratadas como aprovação silenciosa. As execuções mais recentes após essa alteração estão em curso; a evidência funcional de multiplicidade está concluída no run 39624008823 e fica registada como resultado técnico, não como promoção.

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

**Estado R4:** comparação histórica dos estados de manifesto efetuada: o SHA/contagem do snapshot anual não mudou entre VALIDADO e BLOQUEADO; a decisão de bloqueio mudou por autorização/âmbito de uso, não por alteração do SHA do NORMALIZED. A FASE10 concluiu a comparação quantitativa da composição completa no run [39624008823](https://github.com/carlos-andrade/B3/actions/runs/39624008823): 53.275 linhas adicionais no candidato e zero linhas canónicas ausentes. Fica pendente classificar a origem dessas linhas adicionais e resolver a inconsistência semântica entre o dataset que declara `VIGENTE/VALIDADO` e o manifesto anual `BLOQUEADO`. A autorização operacional continua limitada a validação interna; não prova direito de publicação ou redistribuição.

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
