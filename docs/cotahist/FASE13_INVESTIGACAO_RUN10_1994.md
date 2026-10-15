# FASE13 — Investigação Run #10 da cadeia COTAHIST 1994

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-020-ACAO-RUN10-1994-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 75d0e790eb16a58392d9a0cacde042d0f46a700379ecb49346340c4ab81ada8d |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


## Identificação

- Workflow: `.github/workflows/cotahist-cadeia-1994-06-12-v1.yml`
- Run: #10
- Run ID: 36848531230
- Commit: `c4e37468428a464726ad3f3273b91dcc30c9385a`
- Data: 2026-10-01
- Resultado: FAILURE

## Verificação

A ordenação dos gates funcionou corretamente:

1. FASE06-08 — sucesso
2. GATE FASE06-08 antes de FASE09 — sucesso
3. FASE09-12 — falha fechada

A falha ocorreu dentro do contrato da FASE10.

O script `scripts/ingestao/gerar_cadeia_cotahist_1994_fases09_12_v1.py` define:

- `CORRECTION_REQUIRED=False`
- `correction_applied=False`
- `correction_contract_valid=True`

Entretanto, os campos informativos `correction_required=False` e `correction_applied=False` continuam dentro do dicionário `checks`, que é avaliado por `all(checks.values())`.

Isso torna `f10_ok` necessariamente falso quando nenhuma correção é necessária, apesar de o contrato de correção estar válido.

## Evidência persistida

A evidência atual da FASE10 confirma a contradição:

- `correction_required=false`
- `correction_applied=false`
- `correction_contract_valid=true`
- demais verificações de integridade: verdadeiras
- status: BLOQUEADO

Portanto, o problema é lógico no gate, não uma inconsistência do RAW, do normalizado ou dos hashes.

## Decisão

- FASE06-08: operacionalmente validadas.
- FASE09: executada e liberada.
- FASE10: bloqueada por bug de avaliação do próprio contrato.
- FASE11: não certificada.
- FASE12: não concluída.
- Transição para 1995: não autorizada.

## Correção necessária

O próximo ajuste deve retirar `correction_required` e `correction_applied` da condição booleana de integridade, mantendo-os como campos informativos, e usar `correction_contract_valid` como único gate de contrato.

Após a correção, a cadeia deve ser executada novamente e somente uma execução bem-sucedida poderá fechar 1994.

## Princípio

`pré-condição válida → execução → evidência → gate → próxima fase`.

Nenhuma fase posterior deve ser liberada com base em evidência BLOQUEADA.
