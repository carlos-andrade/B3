# B3 — ROADMAP DE INGESTÃO COTAHIST — PARTE23 (RECONCILIADO)

**Data de referência:** 2026-10-14  
**Repositório:** https://github.com/carlos-andrade/B3  
**Estado:** COTAHIST 2026 atualizado até 13/10; revalidação técnica aprovada; auditoria pós-promoção a consolidar.

## Correção do diagnóstico inicial

A auditoria `docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md` descrevia um NORMALIZED terminado em 23/09/2026. Essa evidência ficou desatualizada após a atualização do dataset em 14/10/2026. Preservar o documento como histórico; não tratar o seu bloqueio por defasagem como estado atual.

## Estado verificado no branch main

- RAW SHA-256: `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e`.
- NORMALIZED SHA-256: `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`.
- 3.142.910 registos, 25 campos; intervalo 2026-01-02 a 2026-10-13.
- FASE04/05: `VALIDADO`, hashes e manifestos coerentes.
- FASE06: `VALIDADO`, zero divergências RAW × NORMALIZED.
- FASE08: `VALIDADO_COM_EXCECAO`, zero bloqueadores; exceções de ordenação/regressão por instrumento preservadas, sem reordenar nem remover linhas.
- Gate 06–08: `APROVADO_COM_EXCECOES_NAO_BLOQUEANTES`, decisão `LIBERADO_PARA_FASE09`.
- FASE09: `LIBERADO_PARA_FASE10`, sem ausências nem bloqueadores, validado às 11:25:35 UTC.
- FASE10 candidato: `VALIDADO_SEM_DIFERENCAS_DE_LINHAS`; 3.142.910 linhas de cada lado, zero linhas adicionadas/ausentes, multiplicidade integral preservada, reconciliação dos 25 campos, nenhuma deduplicação.
- FASE11: `PROMOVIDO_COM_HASHES_COHERENTES`; hashes iguais aos atuais, 3.142.910 linhas, última data 2026-10-13.

A evidência FASE11 contém a decisão histórica `REEXECUTAR_FASES_04_08`, pois a promoção antecedeu as revalidações mais recentes. As evidências posteriores apresentam os mesmos hashes; falta consolidar uma auditoria pós-promoção única, cruzando todas as fases e a atualidade.

## Roadmap operacional

| Ordem | Etapa | Estado | Próxima ação |
|---|---|---|---|
| 1 | Aquisição RAW 2026 | Concluída | Preservar hash e proveniência |
| 2 | FASE04–05 | Validadas | Cruzar hashes com todas as fases |
| 3 | FASE06 | Validada; zero divergências | Preservar evidência; não deduplicar |
| 4 | FASE07 | Evidência existente | Confirmar hash/cardinalidade na auditoria integrada |
| 5 | FASE08 | Validada com exceções não bloqueadoras | Manter exceções classificadas |
| 6 | Gate 06–08 | Aprovado com exceções | Reabrir apenas se dados/regras mudarem |
| 7 | FASE09 | Liberada para FASE10 | Atualizar a documentação de atualidade obsoleta |
| 8 | FASE10 | Candidato validado sem diferenças | Preservar relatório e hashes |
| 9 | FASE11 | Promoção registada | Auditar estado remoto pós-promoção |
| 10 | Fecho técnico do ciclo | Em consolidação | Confirmar hashes, contagens, calendário e estados |
| 11 | Atualizações futuras | Contínuas | Verificar nova publicação oficial e reabrir fases se RAW mudar |

## Critérios para a auditoria pós-promoção

1. Confirmar SHA-256 RAW `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e` e NORMALIZED `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`.
2. Confirmar coerência entre manifestos e sidecars.
3. Confirmar que FASE04–FASE09 referenciam esses hashes.
4. Confirmar resultado FASE10, sem diferenças e sem deduplicação.
5. Confirmar promoção efetiva e imutabilidade do conteúdo pós-validação.
6. Confirmar que 13/10 é a última sessão observada neste artefacto, sem presumir atualização indefinida.

## Regras de integridade

- Não sobrescrever silenciosamente RAW/NORMALIZED.
- Não inventar execução, checksum ou resultado.
- Não deduplicar nem reordenar linhas para corrigir exceções da fonte.
- Não declarar o fecho anual de 2026 prematuramente.
- Preservar a auditoria antiga como registo histórico; acrescentar evidência que a supersede.

## Referências

- [Manifesto RAW](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/manifests/COTAHIST_A2026.json)
- [Manifesto NORMALIZED](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/normalized/manifests/COTAHIST_A2026_quality.json)
- [FASE09](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE09_PRE_RELEASE_V1.json)
- [FASE10](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE10_VALIDACAO_CANDIDATO_V1.json)
- [FASE11](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE11_PROMOCAO_V1.json)
- [Auditoria histórica de atualidade](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md)
- [Execução #718](https://github.com/carlos-andrade/B3/actions/runs/38556380160)

**Conclusão:** o bloqueio inicial por defasagem foi superado pela atualização de 14/10/2026. O próximo gate é a auditoria pós-promoção integrada, não uma nova aquisição nem o fecho anual prematuro.
