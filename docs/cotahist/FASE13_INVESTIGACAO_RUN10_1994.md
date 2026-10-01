# FASE13 — Investigação Run #10 da cadeia COTAHIST 1994

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
