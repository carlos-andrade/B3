# DECISÃO R4 — Não promover COTAHIST 2026 sem autorização de publicação

- Data: 2026-10-21
- Projeto: B3 — A BOLSA DO BRASIL
- Âmbito: COTAHIST anual 2026
- Estado: DECISÃO DE NÃO PROMOÇÃO
- Governação aplicável: `docs/governanca/licenciamento/REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json`
- Decisão anterior de aquisição limitada: `docs/governanca/decisoes/DECISAO_REAVALIACAO_BLOQUEIO_COTAHIST_2026-10-21.md`

## Evidência disponível

O probe da fonte oficial concluiu com sucesso em 2026-10-21 e identificou um candidato estruturalmente válido:
- URL: `https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2026.ZIP`
- SHA-256 do candidato: `78032d39937bb540a57850a30ee3ef928462c5fa5c8dc073b2a10f64501740d0`
- Tamanho: 94.685.771 bytes
- Registos tipo `01`: 3.233.168
- Primeira data: 2026-01-02
- Última data: 2026-10-20
- ZIP/CRC: OK
- Comprimentos inválidos: 0
- Mutação do dataset canónico pelo probe: não

Execução: https://github.com/carlos-andrade/B3/actions/runs/39582797424

A execução FASE10 para este candidato foi iniciada em https://github.com/carlos-andrade/B3/actions/runs/39592181392. O resultado integral da FASE10 tem de ser consultado antes de declarar concluída a reconciliação dos 25 campos e a comparação de multiplicidade das linhas. O relatório FASE10 anterior, de 2026-10-14, corresponde a outro SHA e não constitui evidência para este candidato.

## Decisão

**Não promover o candidato para os dados canónicos do repositório público nesta etapa.**

Fundamentos:
1. A decisão operacional permite aquisição controlada para validação técnica e processamento interno, não concede licença de publicação do RAW, redistribuição, uso comercial ou desenvolvimento de produto.
2. O registo de autorização mantém `storage_and_redistribution=REVIEW_REQUIRED_BEFORE_PUBLICATION`.
3. A promoção existente alteraria artefactos RAW e NORMALIZED no repositório público; isso excede o âmbito atualmente autorizado.
4. A FASE10 deve terminar e fornecer evidência atualizada antes de se afirmar que as diferenças históricas foram reconciliadas.
5. Não presumir que os registos recentes são apenas adições: exigir comparação por linha integral e multiplicidade preservada, sem deduplicação.

## Condições para reconsideração

- FASE10 termina com sucesso contra o mesmo SHA do probe.
- Os 25 campos são reconciliados integralmente com o RAW.
- A comparação integral identifica explicitamente linhas adicionadas e ausentes, preservando multiplicidade.
- Os termos oficiais aplicáveis a armazenamento público e redistribuição são documentados, ou é obtida autorização escrita adequada.
- A FASE11 é revista para não impor igualdade total quando se trata de uma atualização legítima, mas exige que todas as linhas canónicas antigas permaneçam presentes; qualquer alteração histórica deve bloquear.
- Só uma decisão de promoção posterior, versionada e baseada nessas evidências pode autorizar alteração dos artefactos canónicos.

## Efeito

- RAW canónico: inalterado.
- NORMALIZED canónico: inalterado.
- Manifestos e checksums canónicos: inalterados por esta decisão.
- Aquisição limitada para validação interna: permitida nos termos registados.
- Publicação/redistribuição do candidato: não autorizada por esta decisão.
- Estado do roadmap: R4 decidido como **NÃO PROMOVER AGORA**; a validação técnica R3 continua em execução.
