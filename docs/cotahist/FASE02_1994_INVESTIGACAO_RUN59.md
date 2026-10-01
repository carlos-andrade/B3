# Investigação — COTAHIST 1994 FASE02 — Run #59

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
