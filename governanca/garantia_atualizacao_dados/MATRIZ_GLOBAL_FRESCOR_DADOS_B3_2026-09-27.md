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

Em 27/09/2026, domingo, a última sessão regular anterior é 25/09/2026.

## 3. Correção identificada no COTAHIST

A investigação mostrou que o projeto já possui **ingestão diária validada até 25/09/2026**:

- commit: `1b2ef358f02c18fb1d1b061a41e97e13f957653e`;
- data de referência: 25/09/2026;
- linhas normalizadas: 16.593;
- primeira/última data: 25/09/2026;
- status do manifesto: `VALIDADO`.

Portanto, o problema não é ausência total do dado de mercado de 25/09.

O problema é de **convergência entre camadas**: o Dataset Oficial anual de 2026 continua terminando em 22/09, enquanto a camada diária já alcançou 25/09.

## 4. Matriz

| Dataset / domínio | Fonte | Última observação esperada | Última observação armazenada | Captura/geração | Status |
|---|---|---:|---:|---:|---|
| COTAHIST diário | B3 | **25/09/2026** | **25/09/2026** | 26/09/2026 | **VALIDADO** |
| COTAHIST anual/oficial 2026 | B3 | **25/09/2026** | **22/09/2026** | 27/09/2026 | **PENDENTE — CAMADA ANUAL DEFASADA** |
| COTAHIST histórico 1986–2025 | B3 | Encerramento de cada ano | Conforme registros anuais certificados | Atualização histórica | **CONDICIONAL** |
| Copom 281 | BCB | 16/09/2026; informação disponível 22/09/2026 | 16/09/2026; informação disponível 22/09/2026 | 25/09/2026 | **REGISTRADO** |
| Demais séries macroeconômicas BCB | BCB | Depende de cada série | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |
| Índices/carteiras B3 | B3 | Depende do calendário/metodologia | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |
| Derivativos/futuros/market data além do COTAHIST | B3 | Depende do produto e granularidade | Não consolidado nesta matriz | — | **NÃO CERTIFICADO** |

## 5. Evidência do Dataset Oficial

Arquivo:

`dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json`

O registro de 2026 informa:

- primeira data: 02/01/2026;
- última data: **22/09/2026**;
- 2.904.013 linhas normalizadas;
- SHA-256 RAW: `e40dc0cdb5ad6315296d88cdb5654240f15412be6fc13e3d47bc8606f9132fee`;
- SHA-256 NORMALIZED: `d97514f3224da3b70b5b890911c7383e86a6d69ffc5482eb610826d729b2a1fa`.

O manifesto foi atualizado em 27/09/2026 pelo commit:

`561888200a6def1c90815e0b5f67c8b1f835fd3e`

Esse commit alterou a data de geração do manifesto, mas não incorporou as observações diárias posteriores a 22/09.

## 6. Causa operacional identificada

O workflow diário original importava apenas a data corrente:

`COTAHIST_D{data_corrente}.ZIP`

Isso cria uma vulnerabilidade operacional: se uma execução diária falhar ou não persistir determinado pregão, as execuções seguintes não fazem recuperação automática do dia perdido.

A correção foi aplicada no importador para executar **backfill dos últimos 7 dias**, ignorando datas sem arquivo/pregão e mantendo a validação RAW → NORMALIZED → manifest → SHA-256.

Arquivo alterado:

`scripts/ingestao/importar_cotahist_diario_v1.py`

Commit da correção:

`3fc2afb82409af9a642541c96ded14a971ecbad7`

## 7. Regra de fail-closed

A camada diária pode estar atualizada enquanto a camada anual/oficial permanece defasada.

Assim:

- **COTAHIST diário:** pode ser consumido para frescor corrente quando o manifesto estiver `VALIDADO`;
- **Dataset Oficial anual:** não deve ser declarado atualizado enquanto `ultima_data` não alcançar o último pregão aplicável;
- **Garantia global:** permanece **NÃO CERTIFICADA** até todos os datasets obrigatórios passarem pela mesma verificação.

Nenhum dashboard, backtest ou estudo deve interpretar “workflow executado com sucesso” como sinônimo de “todos os datasets estão atualizados”.

## 8. Próxima execução obrigatória

A próxima execução do workflow diário deverá tentar automaticamente recuperar os últimos 7 dias.

Objetivo mínimo:

1. localizar/importar 23/09/2026;
2. localizar/importar 24/09/2026;
3. manter/validar 25/09/2026;
4. gerar manifests e hashes;
5. reconciliar a camada diária com a camada anual/oficial;
6. atualizar esta matriz somente após evidência verificável.

## 9. Pendências globais

A garantia integral continua bloqueada porque:

1. o Dataset Oficial anual 2026 ainda termina em 22/09;
2. os demais datasets obrigatórios ainda não possuem inventário global de frescor;
3. não há evidência consolidada suficiente para certificar índices, carteiras, derivativos e demais séries macroeconômicas.

**Status final em 27/09/2026: NÃO CERTIFICADA.**
