# B3 — CARTA DE RECEBIMENTO INCREMENTAL — V1.0

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-07ED255ECCD8 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 64ac4a94bcea519df11a0f446f122a28bc8086d352f50ae387bd511c722e9693 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
