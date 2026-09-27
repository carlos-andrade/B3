# MATRIZ GLOBAL DE FRESCOR DOS DADOS — B3

**Arquivo:** MATRIZ_GLOBAL_FRESCOR_DADOS_B3_2026-09-27.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Caminho:** governanca/garantia_atualizacao_dados/MATRIZ_GLOBAL_FRESCOR_DADOS_B3_2026-09-27.md  
**Data da verificação:** 27/09/2026  
**Repositório:** carlos-andrade/B3  
**Status global:** **NÃO CERTIFICADA — COTAHIST DIÁRIO VALIDADO; CAMADA ANUAL AINDA DEFASADA**

## 1. Regra

A matriz compara a última observação que deveria estar disponível na fonte com a última observação efetivamente armazenada no repositório.

Para dados de mercado, usa-se o último pregão aplicável, e não simplesmente a data civil.

Um dataset só recebe **APROVADO** quando houver evidência suficiente de fonte, captura, RAW, integridade, normalização e frescor.

## 2. Referência temporal

Em 27/09/2026, domingo, a última sessão regular anterior é 25/09/2026.

## 3. Correção operacional executada no COTAHIST

A correção de backfill foi efetivamente executada em GitHub Actions.

- commit disparador: `ba2159a73ff5061e70652ba5d0d0457a42833277`;
- workflow run: `36320246044`;
- evento: `push`;
- resultado do job: **success**;
- commit de persistência dos dados: `76bd78434ddf2556d0cdd2528db0044cea514043`;
- 23/09/2026: **VALIDADO**, 15.747 linhas;
- 24/09/2026: **VALIDADO**, 15.903 linhas;
- 25/09/2026: **VALIDADO**, 16.593 linhas.

### Evidências SHA-256

| Data | RAW SHA-256 | NORMALIZED SHA-256 |
|---|---|---|
| 23/09/2026 | `e2671e6a18e3cf9e628713bf60dc278d5e7e4948026618497156231d3fec2c6f` | `5da9dc290badbd97da2c31aa121b9df2fe4f85a75aff972cb5020a21964cf0de` |
| 24/09/2026 | `7ef9fb0e832f2c67effaf65be66c736f593fecbe3c4598ad9d0be6ff5e6d5bfc` | `99962bd581e476908b97a5261f73eb973c4ef4d4373a7683a7b88e977a80d464` |
| 25/09/2026 | `1d62e1d49777c8b85dba3e546a5040d0f78765fb1cd439433c5303f5320ae4a8` | `f195a090d38055951972208c97f5cce49b221e462c60df9bc1c29d62ae8c93cc` |

## 4. Correção identificada no COTAHIST

A investigação mostrou que o projeto já possui **ingestão diária validada até 25/09/2026**:

- commit: `1b2ef358f02c18fb1d1b061a41e97e13f957653e`;
- data de referência: 25/09/2026;
- linhas normalizadas: 16.593;
- primeira/última data: 25/09/2026;
- status do manifesto: `VALIDADO`.

Portanto, o problema não é ausência total do dado de mercado de 25/09.

O problema é de **convergência entre camadas**: o Dataset Oficial anual de 2026 continua terminando em 22/09, enquanto a camada diária já alcançou 25/09.

## 5. Matriz

| Dataset / domínio | Fonte | Última observação esperada | Última observação armazenada | Captura/geração | Status |
|---|---|---:|---:|---:|---|
| COTAHIST diário | B3 | **25/09/2026** | **25/09/2026** | 26/09/2026 | **VALIDADO** |
| COTAHIST anual/oficial 2026 | B3 | **25/09/2026** | **25/09/2026 (dataset corrente composto)** | 27/09/2026 | **VALIDADO — ÍNDICE OFICIAL ATUAL V1.1** |
| COTAHIST histórico 1986–2025 | B3 | Encerramento de cada ano | Conforme registros anuais certificados | Atualização histórica | **CONDICIONAL** |
| Copom 281 | BCB | 16/09/2026; informação disponível 22/09/2026 | 16/09/2026; informação disponível 22/09/2026 | 25/09/2026 | **REGISTRADO** |
| Demais séries macroeconômicas BCB | BCB | Depende de cada série | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |
| Índices/carteiras B3 | B3 | Depende do calendário/metodologia | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |
| Derivativos/futuros/market data além do COTAHIST | B3 | Depende do produto e granularidade | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |

## 6. Evidência do Dataset Oficial

Arquivo:

`dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json`

O registro de 2026 informa:

- primeira data: 02/01/2026;
- última data: **22/09/2026**;
- 2.904.013 linhas normalizadas;
- SHA-256 RAW: `e40dc0cdb5ad6315296d88cdb5654240f15412be6fc13e3d47bc8606f9132fee`;
- SHA-256 NORMALIZED: `d97514f3224da3b70b5b890911c7383e86a6d69ffc5482eb610826d729b2a1fa`.

O snapshot anual permanece preservado com última data 22/09/2026. Para não reescrever o snapshot RAW/normalized e evitar falsa equivalência de origem, foi criado o índice corrente:

`dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json`

Esse índice comprova a composição do snapshot anual com os incrementos diários VALIDADO de 23/09, 24/09 e 25/09. A última observação corrente passa a ser 25/09/2026.

## 7. Causa operacional identificada

O workflow diário original importava apenas a data corrente:

`COTAHIST_D{data_corrente}.ZIP`

Isso cria uma vulnerabilidade operacional: se uma execução diária falhar ou não persistir determinado pregão, as execuções seguintes não fazem recuperação automática do dia perdido.

A correção foi aplicada no importador para executar **backfill dos últimos 7 dias**, ignorando datas sem arquivo/pregão e mantendo a validação RAW → NORMALIZED → manifest → SHA-256.

Arquivo alterado:

`scripts/ingestao/importar_cotahist_diario_v1.py`

Commit da correção:

`3fc2afb82409af9a642541c96ded14a971ecbad7`

## 8. Regra de fail-closed

A camada diária pode estar atualizada enquanto a camada anual/oficial permanece defasada.

Assim:

- **COTAHIST diário:** pode ser consumido para frescor corrente quando o manifesto estiver `VALIDADO`;
- **Snapshot anual:** permanece identificado separadamente e termina em 22/09/2026;
- **Dataset Oficial corrente:** pode ser declarado atualizado quando o índice composto atingir o último pregão aplicável e todos os incrementos estiverem `VALIDADO`;
- **Garantia global:** permanece **NÃO CERTIFICADA** até todos os datasets obrigatórios passarem pela mesma verificação.

Nenhum dashboard, backtest ou estudo deve interpretar “workflow executado com sucesso” como sinônimo de “todos os datasets estão atualizados”.

## 9. Próxima execução obrigatória

A próxima execução do workflow diário deverá tentar automaticamente recuperar os últimos 7 dias.

Objetivo mínimo:

1. localizar/importar 23/09/2026;
2. localizar/importar 24/09/2026;
3. manter/validar 25/09/2026;
4. gerar manifests e hashes;
5. reconciliar a camada diária com a camada anual/oficial;
6. atualizar esta matriz somente após evidência verificável.

## 10. Implementação da reconciliação anual

A reconciliação anual foi automatizada no workflow diário. O processo preserva o RAW anual da B3 como snapshot imutável e atualiza o NORMALIZED anual por composição com pregões diários `VALIDADO` posteriores ao último pregão do snapshot. A implementação usa processamento em streaming para evitar carregar milhões de registros do COTAHIST anual em memória.

Arquivo: `scripts/ingestao/reconciliar_cotahist_anual_v1.py`

## 11. Pendências globais

A garantia integral continua bloqueada porque:

1. o snapshot anual 2026 termina em 22/09, mas o Dataset Oficial corrente V1.1 já alcança 25/09 por composição auditável;
2. os demais datasets obrigatórios ainda não possuem inventário global de frescor;
3. não há evidência consolidada suficiente para certificar índices, carteiras, derivativos e demais séries macroeconômicas.

**Status final em 27/09/2026: NÃO CERTIFICADA.**
