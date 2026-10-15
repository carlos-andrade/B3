# INVESTIGAÇÃO — FASE06 1995 — PROVA DE EXECUÇÃO E CAUSA DA FALHA

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-019-XECUCAO-E-CAUSA-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 81c31566ab47269f01d57e1adb38d40aca8f159e50aa1c3801881175619f7e3d |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


Data: 2026-10-01

## Prova de execução

Commit auditado:
2373ddb6091792f6cffe2c5ac6a4bf2ed4fb1d7f

Check suite:
99831673560

Workflow run:
36859032714

Jobs:
- semantica — 110358392000 — FAILURE
- validar_fase06_1995 — 110358393439 — FAILURE
- atualizar — 110358392972 — SUCCESS

Conclusão: a FASE06 foi efetivamente executada. A ausência anterior da evidência não significava ausência de execução.

## Causa técnica observada

O job semantica encerrou com:

FAIL-CLOSED: inconsistências semânticas

As primeiras ocorrências registradas foram chaves duplicadas:

- ('19950103', '62', 'ELE 6', '030')
- ('19950104', '62', 'CST 6', '030')
- ('19950104', '62', 'ELE 6', '030')
- ('19950104', '62', 'PET 4', '030')
- ('19950104', '62', 'USI 4', '030')
- ('19950105', '62', 'PET 4', '030')
- ('19950106', '62', 'BES 4', '030')
- ('19950109', '62', 'TEL 4', '030')
- ('19950110', '62', 'CST 6', '030')
- ('19950110', '62', 'INE 4', '030')

A validação estava impondo unicidade da chave:

data + codbdi + codneg + tpmerc

## Interpretação

A prova demonstra falha do validador semântico, não prova de corrupção do RAW.

O layout oficial da B3 descreve o arquivo COTAHIST como classificado por Tipo de Registro, Data do Pregão, Código BDI, Nome da empresa e Código de Negociação, e não estabelece no trecho consultado uma regra geral de unicidade para a chave data+codbdi+codneg+tpmerc.

Fonte oficial consultada:
B3 — Layout do Arquivo de Cotações Históricas (COTAHIST.AAAA.TXT).

Portanto, a regra de unicidade deve ser tratada como hipótese de validação até que seja reconciliada com a semântica histórica de 1995 e com o layout oficial aplicável.

## Estado

FASE06: EXECUTADA, mas NÃO VALIDADA.

FASE07 permanece bloqueada até correção e nova execução da FASE06.

Importante: não liberar 1995 para FASE07 com base apenas nesta execução.

## Próximo passo controlado

1. Investigar semanticamente as duplicidades observadas.
2. Confirmar se existe campo adicional necessário à chave lógica histórica ou se duplicidades são legítimas no COTAHIST.
3. Corrigir o contrato do validador somente após essa reconciliação.
4. Reexecutar FASE06.
5. Somente com evidência VALIDADO e decisão LIBERADO_PARA_FASE07 liberar a FASE07.


## RESOLUÇÃO — 2026-10-01

A FASE06 foi corrigida para não tratar a chave candidata como única. Nova execução produziu evidência `VALIDADO` e `LIBERADO_PARA_FASE07`.

Resultado observado:
- registros tipo 01: 104.791;
- chaves candidatas duplicadas: 258;
- linhas adicionais decorrentes dessas colisões: 258;
- registros exatamente idênticos entre si: 0;
- erros semânticos: 0;
- amostras OHLC: 30;
- decisão: `LIBERADO_PARA_FASE07`.

A presença de 258 colisões de chave candidata, sem registros exatamente idênticos, confirma que a unicidade dessa composição não pode ser presumida. A resolução da identidade/cardinalidade fica formalmente transferida para a FASE07.

**Evidência final:** `dados/cotahist/quality/COTAHIST_1995_FASE06_SEMANTICA_V1.json`

**Regra permanente:** FASE06 = semântica/invariantes; FASE07 = identidade/chaves/cardinalidade.
