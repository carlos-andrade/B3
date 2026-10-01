# FASE 05.3 — VALIDAÇÃO DOS HISTÓRICOS E CASOS AMBÍGUOS V1

**Status:** CONCLUÍDA COM PONTOS DE CONTROLE  
**Fonte normativa:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`  
**Entrada:** `docs/governanca/auditorias/FASE05_2_CLASSIFICACAO_FUNCIONAL_WORKFLOWS_B3_V1.json`

## 1. Objetivo

Validar a triagem funcional da FASE 05.2, distinguindo classificação nominal de responsabilidade efetiva. A fase não altera workflows e não reabre qualquer cadeia histórica.

## 2. Universo histórico

Foram identificados **81 workflows históricos**:

| Ano | Qtde. |
|---|---:|
| 1986 | 26 |
| 1987 | 12 |
| 1988 | 14 |
| 1989 | 2 |
| 1990 | 2 |
| 1991 | 2 |
| 1992 | 2 |
| 1993 | 8 |
| 1994 | 8 |
| 1995 | 5 |
| **Total** | **81** |

A identificação histórica é baseada no ano explicitamente incorporado ao nome do workflow. Isso é evidência de inventário, não certificação da correção funcional de cada workflow.

## 3. Casos ambíguos validados por conteúdo

### 3.1 `atualizar-catalogo-b3.yml`

O conteúdo executa `ferramentas/importar_bvbg028.py --date ...` e publica inventário em `ativos/catalogo` e `ativos/instrumentos`.

**Conclusão:** funcionalmente pertence a **BVBG**, embora o nome não revele essa função.

**Estado:** ATIVO.

### 3.2 `capturar-pesquisa-pregao.yml`

O conteúdo captura dados de mercado por pregão e grava em `dados/market_data/raw` e `dados/market_data/manifests`.

**Conclusão:** deve ser tratado como categoria funcional própria **MARKET_DATA_PREGAO**, em vez de `OUTROS`.

**Estado:** ATIVO.

## 4. Amostras históricas verificadas

### FASE14 — 1995

O workflow está restrito aos artefatos RAW, manifesto, checksum e ao próprio workflow. Não há gatilho de README ou documentação genérica.

**Resultado:** consistente com o princípio de isolamento observado.

### FASE06 — 1995

O workflow depende da evidência da FASE05, RAW 1995 e do próprio workflow. A evidência produzida libera exclusivamente a FASE07.

**Resultado:** consistente com a direção FASE05 → FASE06 → FASE07.

### FASE12 — 1993

O workflow é histórico e já integra a cadeia fechada de 1993. Entretanto, seu gatilho inclui a matriz anual de certificação `1986_2026`, além de vários artefatos.

**Resultado:** **PONTO DE CONTROLE para FASE05.4**. Não será corrigido nesta fase e não será reexecutado.

## 5. Conclusão

1. A FASE05.2 cumpriu sua função de triagem.
2. Dois casos classificados como `OUTROS` foram semanticamente identificados:
   - `atualizar-catalogo-b3.yml` → **BVBG**;
   - `capturar-pesquisa-pregao.yml` → **MARKET_DATA_PREGAO**.
3. Os 81 workflows históricos permanecem inventariados sem reabertura.
4. A FASE05.3 não autoriza qualquer alteração operacional.
5. Os achados de gatilhos/dependências serão tratados somente na FASE05.4.

**Regra de isolamento:** nenhuma fase histórica foi reaberta; nenhum README foi alterado; nenhum workflow foi modificado.

## Próxima fase

**FASE 05.4 — CLASSIFICAÇÃO SEMÂNTICA E MATRIZ DE CONFORMIDADE.**
