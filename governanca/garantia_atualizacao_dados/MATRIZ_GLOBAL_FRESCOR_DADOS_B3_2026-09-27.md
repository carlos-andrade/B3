# MATRIZ GLOBAL DE FRESCOR DOS DADOS — B3

**Arquivo:** MATRIZ_GLOBAL_FRESCOR_DADOS_B3_2026-09-27.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Caminho:** governanca/garantia_atualizacao_dados/MATRIZ_GLOBAL_FRESCOR_DADOS_B3_2026-09-27.md  
**Data da verificação:** 27/09/2026  
**Repositório:** carlos-andrade/B3  
**Status global:** **NÃO CERTIFICADA**

## 1. Regra

A matriz compara a última observação que deveria estar disponível na fonte com a última observação efetivamente armazenada no repositório.

Para dados de mercado, usa-se o último pregão aplicável, e não simplesmente a data civil.

Um dataset só recebe **APROVADO** quando houver evidência suficiente de fonte, captura, RAW, integridade, normalização e frescor.

## 2. Referência temporal

Em 27/09/2026, domingo, a última sessão regular anterior é 25/09/2026. A própria B3 apresenta registros de mercado em 25/09/2026, enquanto o calendário oficial confirma a programação de negociação de 2026. citeturn0search0turn0search3

## 3. Matriz

| Dataset / domínio | Fonte | Última observação esperada | Última observação armazenada | Captura/geração | Status |
|---|---|---:|---:|---:|---|
| COTAHIST anual 2026 | B3 | **25/09/2026** | **22/09/2026** | 27/09/2026 | **PENDENTE — GAP 3 pregões** |
| COTAHIST histórico 1986–2025 | B3 | Encerramento de cada ano | Conforme registros anuais certificados | Atualização histórica | **CONDICIONAL** |
| Copom 281 | BCB | 16/09/2026; publicação 22/09/2026 | 16/09/2026; informação disponível 22/09/2026 | 25/09/2026 | **REGISTRADO** |
| Demais séries macroeconômicas BCB | BCB | Depende de cada série | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |
| Índices/carteiras B3 | B3 | Depende do calendário/metodologia | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |
| Derivativos/futuros/market data além do COTAHIST | B3 | Depende do produto e granularidade | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |

## 4. Evidência COTAHIST

O arquivo oficial do projeto está em:

`dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json`

O registro de 2026 informa:

- primeira data: 02/01/2026;
- última data: **22/09/2026**;
- 2.904.013 linhas normalizadas;
- SHA-256 RAW: `e40dc0cdb5ad6315296d88cdb5654240f15412be6fc13e3d47bc8606f9132fee`;
- SHA-256 NORMALIZED: `d97514f3224da3b70b5b890911c7383e86a6d69ffc5482eb610826d729b2a1fa`.

O dataset foi atualizado no repositório em 27/09/2026, mas isso **não elimina a defasagem temporal**: geração recente não significa observação recente.

## 5. Evidência Copom

Arquivo:

`dados/calendario_economico/copom/normalized/copom_281.json`

Registro:

- reunião: 281ª;
- reunião: 15–16/09/2026;
- informação disponível: 22/09/2026;
- normalização: 25/09/2026;
- fonte declarada: Banco Central do Brasil.

## 6. Critério de bloqueio

O status global permanece **NÃO CERTIFICADA** porque existe pelo menos um dataset de mercado obrigatório com defasagem conhecida.

Não é permitido emitir uma garantia integral enquanto:

1. o COTAHIST 2026 não alcançar a última sessão disponível;
2. os demais datasets obrigatórios não tiverem última data de observação identificada;
3. cada dataset não tiver evidência de captura e integridade;
4. não existir uma matriz consolidada sem pendências críticas.

## 7. Próxima ação operacional

Prioridade 1:

**Atualizar/reconciliar o COTAHIST 2026 até 25/09/2026**, validar RAW → NORMALIZED → manifest → hash → última data e atualizar esta matriz automaticamente.

Prioridade 2:

Inventariar os demais datasets efetivamente utilizados pelo projeto e atribuir a cada um:

`source → expected_last_date → stored_last_date → freshness_gap → raw → normalized → hash → workflow → commit → status`

## 8. Regra permanente

Esta matriz deve ser atualizada após cada ingestão relevante.

Nenhum dashboard, backtest ou estudo deve interpretar **“workflow executado com sucesso”** como sinônimo de **“dados estão atualizados até o último pregão”**.

**Status final em 27/09/2026: NÃO CERTIFICADA.**
