# FASE 05.2 — CLASSIFICAÇÃO FUNCIONAL DOS WORKFLOWS B3 V1

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-FAF2D0EE55C6 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 5d3edac7bd88cdce805a6b1a68b9dab23d8783f36e72f58326e35dd76e141218 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
