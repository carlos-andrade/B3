# FASE 05.5 — CORREÇÃO POR GRUPO 01 — OBSERVABILIDADE DOS WORKFLOWS ATIVOS

## Estado

- **FASE:** 05.5
- **Grupo:** 01 — OBSERVABILIDADE
- **Escopo:** workflows classificados como ATIVO
- **Correção:** inclusão explícita de `GITHUB_STEP_SUMMARY`
- **Impacto funcional pretendido:** nenhum; trata-se de observabilidade.
- **Workflows históricos:** não alterados.
- **README:** permanece governado pela janela 23:55 America/Sao_Paulo; a inclusão do summary não altera o gatilho operacional do README.
- **Auditor:** não corrige nem reexecuta workflows.

## Critério

A ausência isolada de `GITHUB_STEP_SUMMARY` foi classificada pelo Layout Mestre como alerta de observabilidade, não como defeito funcional de dados. A correção deste grupo adiciona um passo final, condicionado a `always()`, que registra no resumo o nome do workflow, o estado do job e a habilitação do mecanismo de observabilidade.

## Workflows corrigidos

| Workflow | Commit |
|---|---|
| `.github/workflows/atualizar-readme-b3.yml` | `f4003077ae044a7ba3602ac0ca823d6316897f69` |
| `.github/workflows/bcb-sgs-nucleo-macro-v1.yml` | `ac5b034498c86c7317dcf9342064fb7059ef8d3a` |
| `.github/workflows/capturar-bcb-copom.yml` | `6b286ac69bb69d16d3295ebb24f84679aa907294` |
| `.github/workflows/classificar-bvbg028.yml` | `1c6aed241ec95dca8d5afc806e49bd985e16937c` |
| `.github/workflows/cotahist-certificacao-anual-v1.yml` | `ab914fcdf874a58a497916056990a99dc521156b` |
| `.github/workflows/cotahist-dataset-oficial-v1.yml` | `803e334ddbd73632ee88841babdc5f682bc44970` |
| `.github/workflows/cotahist-dataset-oficial-v2.yml` | `10957b86e332849f90f68e7c8e6b61b8aba115a9` |
| `.github/workflows/cotahist-fase08h-recurrencia-k4-multianos-v1.yml` | `f19b922f7107931dc6553e7fa12976f7e4c300bc` |
| `.github/workflows/cotahist-importacao-diaria-v1.yml` | `505214c3c0fc6334da37135a94d026de58369c56` |
| `.github/workflows/cotahist-m3-0-gate-capacidade-2026.yml` | `d45a68e8a7fd8a748476ad534352dcf319d750f4` |
| `.github/workflows/cotahist-m3-1b-prova-lfs-2026.yml` | `074f539ced803dec1d54046af43f867627f53b80` |
| `.github/workflows/cotahist-m3-1b-reconciliar-manifest-2026.yml` | `574cc801bbb30ab50f6acb941298af09667809b2` |
| `.github/workflows/cotahist-normalizacao-controlada-v7.yml` | `7bf58f22e190e3c0f06e162763e23749f2162fb7` |
| `.github/workflows/cotahist-orquestrador-anual-dryrun-v1.yml` | `9f03f93e700ba279d2dd69e491e569389802f0a1` |
| `.github/workflows/cotahist-orquestrador-anual-dryrun-v2.yml` | `075f9d54be7bc633e75350a47cd82c4b4c417cee` |
| `.github/workflows/indices-b3-composicao-v1.yml` | `cf3f4607d65f11e79bdcd22757c1cc0cfbc49ca4` |
| `.github/workflows/processar-inventario-bvbg028.yml` | `48b9089719d369cb71b350693704ec530e1a0115` |
| `.github/workflows/sincronizar-wiki-b3.yml` | `77f4b3379584b8ba74fe1a1f6c4ea8dd1b1a248b` |
| `.github/workflows/validar-bvbg02802.yml` | `ad89300b5918513a5e73836f46407527987a1e0f` |

## Correção adicional de observabilidade

O workflow `.github/workflows/sincronizar-wiki.yml` também recebeu `GITHUB_STEP_SUMMARY`:

- commit: `723716cd8f3e156886aa4a7304fe60e6f9372a82`

A auditoria anterior havia registrado `NO_README_TRIGGER` nesse workflow. A versão atualmente verificada contém somente `WIKI/**` e o próprio workflow no `push.paths`; portanto, **não há README no gatilho atual**.

## Validação estática

1. Os 19 workflows ativos originalmente classificados apenas por `STEP_SUMMARY` foram atualizados.
2. O workflow Wiki adicional foi atualizado para observabilidade e não possui README no trigger atual.
3. Nenhum workflow histórico foi alterado como parte deste grupo.
4. Nenhuma chamada/reexecução de outro workflow foi introduzida.
5. Nenhum gatilho de fase posterior foi introduzido.
6. Nenhuma alteração de dados COTAHIST, RAW, normalized ou certificação foi feita.
7. A auditoria v2 permanece diagnóstica e deve ser executada pelo GitHub Actions para produzir a matriz automatizada pós-correção.

## Limitação

A execução do auditor v2 no ambiente desta sessão não pôde ser reproduzida localmente porque o ambiente de execução não possui resolução de rede para `github.com`. Portanto, **esta fase está validada estruturalmente, mas a matriz pós-correção em execução do GitHub Actions ainda é necessária**.

## Decisão

**FASE 05.5 — CONCLUÍDA E PRONTA PARA VALIDAÇÃO PÓS-CORREÇÃO.**

A próxima fase não deve corrigir novamente este grupo. Deve executar a auditoria v2 e comparar a matriz antes/depois, preservando os workflows históricos como somente leitura.
