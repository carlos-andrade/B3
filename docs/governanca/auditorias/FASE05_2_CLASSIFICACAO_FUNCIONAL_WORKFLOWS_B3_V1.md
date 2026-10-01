# FASE 05.2 — CLASSIFICAÇÃO FUNCIONAL DOS WORKFLOWS B3 V1

**Status:** CONCLUÍDA — TRIAGEM FUNCIONAL  
**Fonte normativa:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`  
**Entrada:** `docs/governanca/auditorias/FASE05_CLASSIFICACAO_DIVERGENCIAS_WORKFLOWS_V1.json`  
**Workflows classificados:** 109

## Objetivo

Classificar funcionalmente os workflows existentes antes de qualquer correção. Esta fase é uma **triagem nominal**, baseada no nome do workflow e em evidência já registrada na FASE 05. Não altera workflows, não reexecuta fases e não certifica conformidade semântica.

## Categorias

| Categoria | Quantidade |
|---|---:|
| BCB_MACRO | 2 |
| BVBG | 3 |
| COTAHIST | 95 |
| GOVERNANCA_MONITORAMENTO | 2 |
| INDICES | 1 |
| OUTROS | 2 |
| README | 1 |
| TESTE_AUXILIAR | 1 |
| WIKI | 2 |

## Estado operacional da triagem

| Estado | Quantidade |
|---|---:|
| ATIVO | 25 |
| AUXILIAR | 1 |
| A_VALIDAR | 2 |
| HISTORICO | 81 |

## Critério

- **GOVERNANCA_MONITORAMENTO:** auditoria e monitoramento estrutural.
- **README:** consolidação de README; permanece sujeito à janela de 23:55 Brasília.
- **COTAHIST:** workflows cujo nome identifica a cadeia histórica/operacional COTAHIST.
- **BCB_MACRO:** BCB, COPOM e núcleo macroeconômico.
- **BVBG:** ingestão/classificação/validação BVBG.
- **INDICES:** composição/importação de índices.
- **WIKI:** sincronização/publicação da Wiki.
- **TESTE_AUXILIAR:** testes ou diagnósticos identificáveis nominalmente.
- **OUTROS:** não enquadrados pelas regras acima.

## Limitação deliberada

A classificação por nome é **triagem**, não prova de responsabilidade. A FASE 05.3 deverá validar os casos históricos, fase/ano, gatilhos, dependências de evidência, estado ativo/legado e possíveis conflitos de responsabilidade diretamente no conteúdo dos workflows.

**Regra de isolamento:** nenhuma alteração operacional foi feita nesta fase. Nenhuma fase histórica foi reaberta. Nenhum README foi modificado.

## Próxima fase

**FASE 05.3 — VALIDAÇÃO DOS HISTÓRICOS E CASOS AMBÍGUOS.**
