# Investigação — COTAHIST 1994 FASE02 — Run #59

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-018-ESTIGACAO-RUN59-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 6778f15216395022143bb6ba0854d520600c0cbbba3d404a14a9caed4e9023f4 |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


## Identificação

- Repositório: `carlos-andrade/B3`
- Workflow: `.github/workflows/cotahist-fase02-integridade-1994-v1.yml`
- Run: `#59`
- Run ID: `36845127395`
- Commit disparador: `ab659b4267e72b1234b3c7a1ca5ed76d6598d087`
- Data/hora: 2026-10-01 09:48:44 UTC
- Resultado: `failure`

## Evidências verificadas

- RAW: `dados/cotahist/raw/anual/COTAHIST_A1994.ZIP` existe.
- SHA-256 no manifesto: `b3bbd8e8d290c36943398c6f99a04e0721db2ebac3b917904df9efaacf3172eb`.
- SHA-256 no checksum: o mesmo valor.
- Evidência FASE02 existente: `VALIDADO`, com o mesmo SHA-256 e um membro ZIP.
- A API de Jobs do Run #59 retorna `total_count=0`; portanto não há step log disponível para atribuir a falha a uma rejeição do RAW.

## Causa técnica identificada

O workflow presente no commit `ab659b4` contém uma quebra de sintaxe no heredoc Python da etapa **Validar integridade do RAW**. A escrita da evidência aparece como:

```python
pathlib.Path("...").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"
")
```

A forma correta é:

```python
pathlib.Path("...").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\\n")
```

A FASE03 operacional usa a construção correta.

## Conclusão

O Run #59 deve ser classificado como **falha do workflow**, não como falha de integridade do COTAHIST 1994. O conjunto manifesto/checksum/RAW/evidência existente permanece coerente.

## Correção planejada

1. Corrigir o `write_text` para usar `"\\n"`.
2. Tornar a publicação idempotente com `git diff --cached --quiet && exit 0`.
3. Disparar nova execução da FASE02.
4. Só liberar formalmente a FASE02 após novo run `success`.

O Run #59 permanece registrado como falha histórica; uma nova execução não deve apagá-lo nem ser usada para retrocertificá-lo.
