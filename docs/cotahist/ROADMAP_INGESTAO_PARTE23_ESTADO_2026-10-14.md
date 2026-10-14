# B3 — ROADMAP DE INGESTÃO COTAHIST — PARTE23

**Data de referência:** 2026-10-14  
**Repositório:** https://github.com/carlos-andrade/B3  
**Branch:** main  
**Estado geral:** BLOQUEADO PARA CERTIFICAÇÃO DE ATUALIDADE — COTAHIST 2026  
**Continuidade:** PARTE22_INGESTÃO DE DADOS  
**Norma:** docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md

## 1. Objetivo e regra de continuidade

Retomar a ingestão a partir das evidências persistidas, sem presumir que o sucesso de um workflow de auditoria de conformidade certifique a atualidade do dataset ou autorize automaticamente fases posteriores.

## 2. Constatações verificadas em 14/10/2026

### 2.1 Auditoria de atualidade

A evidência documental `docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md` declara:

- Estado: `BLOQUEADO_POR_DEFASAGEM_DO_DATASET`.
- NORMALIZED observado nessa auditoria: 2.919.760 registos, SHA-256 `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`.
- Última data no dataset: 2026-09-23.
- Última sessão de negociação confirmada na evidência: 2026-10-13.
- Diferença: 20 dias corridos.
- Decisão explícita: não certificar atualidade nem avançar para fases dependentes da cobertura recente até atualizar o dataset e reexecutar as validações.

### 2.2 Conflito entre artefactos da FASE09

O artefacto `dados/cotahist/quality/COTAHIST_2026_FASE09_PRE_RELEASE_V1.json` contém `status=LIBERADO_PARA_FASE10`, hashes RAW/NORMALIZED e lista de bloqueadores vazia. Porém, a auditoria de atualidade acima identifica cobertura temporal desatualizada. São contratos diferentes: o pré-release técnico consolida os hashes e as evidências que recebeu; a auditoria de atualidade verifica a cobertura face às sessões oficiais mais recentes.

**Decisão operacional da PARTE23:** a certificação global da FASE09 fica bloqueada por atualidade, apesar do resultado técnico anterior de pré-release. Não apagar nem reescrever a evidência histórica. Produzir uma nova evidência versionada após a atualização dos dados e revalidar as dependências.

### 2.3 Workflow de conformidade

A execução #718 do workflow `B3 - Auditoria de conformidade dos workflows pelo Layout Mestre V1` terminou com sucesso em 14/10/2026. Isso confirma o resultado desse job de auditoria estática, não a atualidade do COTAHIST nem a conclusão das FASE10–FASE12.

## 3. Roadmap operacional

| Ordem | Etapa | Estado | Critério para avançar |
|---|---|---|---|
| 1 | Aquisição do COTAHIST 2026 mais recente disponível na fonte oficial | PENDENTE | RAW preservado, origem documentada, ZIP íntegro, SHA-256 e manifesto |
| 2 | FASE04 — normalização | REEXECUTAR APÓS AQUISIÇÃO | CSV gerado de forma determinística, layout de 25 campos e contagens documentadas |
| 3 | FASE05 — manifesto/checksum | REEXECUTAR APÓS AQUISIÇÃO | Hashes RAW/NORMALIZED conferidos de forma independente |
| 4 | FASE06 — reconciliação | REEXECUTAR APÓS AQUISIÇÃO | Comparação RAW × NORMALIZED nos 25 campos, zero divergências não explicadas |
| 5 | FASE07 — identidade/chaves | REEXECUTAR APÓS AQUISIÇÃO | Colisões e cardinalidade documentadas; nenhuma deduplicação automática |
| 6 | FASE08 — calendário/consistência temporal | REEXECUTAR APÓS AQUISIÇÃO | Datas comparadas com calendário oficial e exceções classificadas |
| 7 | Gate 06–08 | BLOQUEADO ATÉ REVALIDAÇÃO | Hashes coerentes, zero bloqueadores e exceções não bloqueadoras justificadas |
| 8 | FASE09 — pré-release + auditoria de atualidade | BLOQUEADA | Cobertura atualizada até a sessão oficial mais recente disponível; evidência técnica e temporal coerentes |
| 9 | FASE10 — validação independente | NÃO CERTIFICADA NESTE CICLO | Executar somente depois da FASE09 desbloqueada; comparar os 25 campos independentemente |
| 10 | FASE11 — certificação | NÃO CERTIFICADA NESTE CICLO | FASE10 aprovada, hashes e evidências coerentes |
| 11 | FASE12 — encerramento/transição | NÃO CERTIFICADA NESTE CICLO | Fecho formal e autorização explícita para o ano seguinte |

## 4. Regras de integridade

1. Não sobrescrever silenciosamente o RAW existente: preservar histórico, hashes e proveniência.
2. Não inventar ZIP, checksum, contagem, sessão de negociação ou resultado de workflow.
3. Não remover nem deduplicar registos como parte da atualização.
4. Não promover fases por inferência baseada no sucesso de um workflow de conformidade diferente.
5. Toda a evidência deve identificar o hash exato dos dados auditados.
6. Se a fonte oficial não estiver acessível, registar a falha de aquisição e manter o gate bloqueado.
7. O novo CSV deve ser rastreável ao RAW exato e às versões dos scripts/layout usados.

## 5. Próxima ação autorizada

Investigar e executar a aquisição do COTAHIST 2026 mais recente disponível na fonte oficial da B3. Se a aquisição for concluída, persistir RAW + SHA-256 + manifesto e reexecutar FASE04–FASE08 em sequência. Se a aquisição não for possível no ambiente disponível, não simular conclusão: registar o bloqueio com evidência e manter a FASE09 global bloqueada.

## 6. Referências

- Repositório: https://github.com/carlos-andrade/B3
- Auditoria de atualidade: https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md
- Evidência técnica FASE09: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE09_PRE_RELEASE_V1.json
- Workflow FASE09: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase09-prerelease-2026-v1.yml
- Execução #718 de conformidade: https://github.com/carlos-andrade/B3/actions/runs/38556380160

---
**Regra de encerramento:** a PARTE23 não declara a ingestão de 2026 concluída. O gate global permanece bloqueado até que a atualidade do dataset seja demonstrada por artefactos reproduzíveis e hashes auditáveis.
