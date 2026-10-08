# B3 — CARTA DE RECEBIMENTO INCREMENTAL — V1.0

> Cabeçalho histórico — 2026-10-08.
> Origem: alinhamento arquitetural com BLOOMBERG_MAIL.
> Status: REGRA PERMANENTE.
> Repositórios: B3 e BLOOMBERG_MAIL.

## 1. Regra

O repositório B3 deve continuar recebendo **incrementos validados** das bases que tenham o B3 como destino de consolidação.

Para COTAHIST:
- a atualização diária é a unidade operacional;
- snapshots anuais permanecem como referência;
- incrementos não substituem RAW histórico;
- cada incremento deve ser identificável por período, arquivo e SHA-256;
- o incremento recebido deve passar por validação/reconciliação antes de ser incorporado à camada consolidada.

## 2. Relação com BLOOMBERG_MAIL

Fluxo governado:

**fonte oficial → BLOOMBERG_MAIL RAW → validação → reconciliação → B3**

O BLOOMBERG_MAIL preserva a aquisição e sua proveniência. O B3 preserva a base histórica/consolidada e recebe os incrementos validados.

A sincronização não autoriza:
- sobrescrita destrutiva;
- substituição de histórico;
- ajuste econômico;
- interpolação;
- invenção de valores.

## 3. Identidade

Cada incremento deve registrar:
- dataset;
- período/data de negociação;
- nome original;
- SHA-256;
- origem;
- data/hora de aquisição;
- caminho no BLOOMBERG_MAIL;
- caminho correspondente no B3;
- resultado da validação;
- resultado da reconciliação.

## 4. Reaquisição divergente

Se a mesma competência for recebida novamente com SHA diferente:
1. preservar as duas representações;
2. não escolher automaticamente uma delas;
3. executar reconciliação;
4. documentar a decisão;
5. bloquear promoção enquanto a divergência permanecer inexplicada.

## 5. COTAHIST

O B3 já possui automação de importação diária. Esta carta torna explícita a obrigação de manter essa atualização alinhada com os incrementos preservados no BLOOMBERG_MAIL.

## 6. Não-regressão

Uma base nova não poderá ser tratada como permanentemente atualizada se possuir apenas snapshot e nenhuma estratégia incremental documentada.
