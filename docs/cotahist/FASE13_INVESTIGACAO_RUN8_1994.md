# FASE13 — Investigação da falha da cadeia 1994 FASE06→FASE12

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-021-GACAO-RUN8-1994-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 4d1c8563bc63153e4a88a91d747e7d83a15ff88d1ff4f0efd59d11ddc8c80b4d |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


**Data:** 2026-10-01  
**Run:** #8  
**Run ID:** 36846966822  
**Commit de disparo:** 91042c3a1d513368a706f60bc7ea0f9dd8c0fe38  
**Workflow:** `.github/workflows/cotahist-cadeia-1994-06-12-v1.yml`

## Resultado

A FASE13 **não foi concluída**. O Run #8 terminou com `failure`.

O job `1994 — FASE06→FASE12` executou corretamente as FASE06–08, mas a etapa `FASE09-12 — pre-release, integridade, certificação e fechamento` terminou com exit code 1 por regra **fail-closed**.

## Evidência operacional

Saída da etapa:

```text
{"year": 1994, "records": 119097, "fases": {"06": "VALIDADO", "07": "VALIDADO", "08": "VALIDADO_COM_EXCECAO"}, "failed": []}
FAIL-CLOSED: cadeia 1994 bloqueada
{"year": 1994, "fases": {"06": "VALIDADO", "07": "VALIDADO_COM_EXCECAO", "08": "VALIDADO_COM_EXCECAO", "09": "LIBERADO_PARA_FASE10", "10": "BLOQUEADO", "11": "BLOQUEADO", "12": "BLOQUEADA"}
```

A leitura persistida da FASE10 identifica uma única condição falsa:

```json
"correction_applied": false
```

Todas as demais verificações de integridade foram verdadeiras, incluindo existência, manifesto, SHA-256 RAW, SHA-256 normalizado, número de linhas, número de campos e imutabilidade do RAW.

## Causa técnica

O script `scripts/ingestao/gerar_cadeia_cotahist_1994_fases09_12_v1.py` define explicitamente:

```python
"correction_applied": False
```

e inclui esse campo em `checks`. Portanto, a condição:

```python
f10_ok=f09_ok and all(checks.values())
```

nunca pode ser verdadeira enquanto `correction_applied` permanecer `False`.

Isso configura um **gate lógico bloqueante**, não uma falha de integridade do RAW ou do arquivo normalizado.

## Estado dos gates

| Fase | Estado |
|---|---|
| FASE06 | VALIDADO |
| FASE07 | VALIDADO |
| FASE08 | VALIDADO_COM_EXCECAO |
| FASE09 | LIBERADO_PARA_FASE10 |
| FASE10 | BLOQUEADO — `correction_applied=false` |
| FASE11 | BLOQUEADO por dependência da FASE10 |
| FASE12 | BLOQUEADA por dependência da FASE11 |
| Transição 1995 | NÃO AUTORIZADA |

## Integridade observada

- RAW 1994: presente e imutável.
- SHA-256 RAW: `b3bbd8e8d290c36943398c6f99a04e0721db2ebac3b917904df9efaacf3172eb`.
- SHA-256 normalizado: `f657bf43b6d8c73edf3b3e1672ac2466531f9a00b26bb778c24ed5f26baf84ff`.
- Registros normalizados: 119.097.
- Campos: 25.
- Manifesto: validado.
- FASE02/1994: já havia sido validada anteriormente após a correção do Run #59.

## Decisão

**NÃO avançar para FASE14.**

A próxima ação deve ser corrigir o contrato lógico da FASE10: distinguir uma eventual **correção aplicada aos dados** de uma **correção operacional/documental do pipeline**. Não se deve marcar `correction_applied=true` artificialmente apenas para passar o gate.

Após a correção do contrato, a cadeia 1994 FASE06→FASE12 deve ser executada novamente e somente um Run bem-sucedido poderá liberar a transição para 1995.
