# PR #14 — relatório de reconciliação de conflitos

| Campo | Valor |
|---|---|
| **ID** | B3-PR14-CONFLICTS-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_AUDITORIA_CONFLITOS_PULL_REQUEST |
| **Fase** | RECONCILIACAO_PR14 |
| **Estado** | DIAGNOSTICO_CONCLUIDO; VALIDACAO_OPERACIONAL_PENDENTE; MERGE_BLOQUEADO |
| **Versão** | 1.0.0 |
| **Data** | 2026-10-20 |
| **Autoridade superior** | [Carta Magna B3](../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre Canónico B3](../governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Decisão GOV-DIV-001](../governanca/decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

## 1. Resultado

O PR #14 não pode ser integrado em segurança por um merge direto: o GitHub reporta conflito (`mergeable=false`, `mergeable_state=dirty`). A branch `feat/cotahist-2006-offline-recovery` tinha 51 commits à frente e 2.329 atrás de `main` no snapshot consultado.

## 2. Achados

1. Os workflows FASE00, FASE01–FASE11 e Gate 06–08 relevantes para 2006 já existem na `main`; não é necessário reintroduzi-los como novos ficheiros.
2. Os workflows na branch original divergem do conteúdo atual de `main` em diferenças materiais, incluindo trigger de branch e persistência de evidências.
3. A `main` usa `main` como branch de trigger e destino de persistência nos workflows canónicos consultados. A versão antiga não deve substituir essas decisões em bloco.
4. O RAW COTAHIST 2006, manifesto e checksums relevantes correspondem aos mesmos objetos Git nos snapshots comparados.
5. O CSV normalizado de 2006 existe em `main` como objeto Git LFS, com ponteiro OID SHA-256 `d9025ebcc01413111c67a0bb573f4ff2676aae2105e8204f19d13f9a313ee69d`. Esta constatação não prova, por si só, que o conteúdo físico de LFS foi materializado e validado neste workflow.
6. As evidências FASE01 em `main` e na branch do PR têm timestamps diferentes. Não se deve substituir uma evidência pela outra sem reconciliar proveniência e propósito.

## 3. Ações de reconciliação

- Criada a branch de revisão `fix/pr14-conflicts-main-sync` a partir do HEAD atual de `main`.
- Registado o [plano de recuperação controlada](PLANO_RECUPERACAO_COTAHIST_2006_OFFLINE_V1.md) nessa branch.
- Preservados os workflows existentes em `main`, o CSV LFS, o RAW, os checksums, os manifestos e as evidências.
- Publicado comentário no PR para tornar visíveis os achados e explicar por que não é seguro fazer merge automático.

## 4. Testes e limitações

| Controlo | Resultado |
|---|---|
| Estado do PR e mergeable | Confirmado como conflitante |
| Comparação de árvores / inventário de ficheiros | Concluída |
| Existência de workflows de 2006 na `main` | Confirmada |
| Triggers e persistência dos workflows atuais | Inspecionados |
| Validação YAML executada em runner | PENDENTE |
| Execução real das fases em sequência | PENDENTE |
| Materialização e hash físico do objeto LFS | PENDENTE |
| Reconciliação independente RAW × NORMALIZED de 25 campos | PENDENTE |
| Certificação COTAHIST 2006 | NÃO DECLARADA |

## 5. Decisão

**Manter o PR #14 aberto, sem merge, até os gates de validação e os conflitos lógicos estarem resolvidos.** Não confundir diagnóstico dos conflitos com certificação dos dados. Não declarar resolvido o problema da PR só porque se criou uma branch e documentação.
