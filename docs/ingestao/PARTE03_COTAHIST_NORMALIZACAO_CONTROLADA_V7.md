# PARTE03 — COTAHIST NORMALIZACAO CONTROLADA V7

Data: 2026-09-24

## Objetivo

Substituir a cadeia de workflows COTAHIST legados por um único pipeline controlado, inicialmente manual e limitado a um ano por execução.

## Regras

- Sem gatilho `push`.
- Execução exclusivamente por `workflow_dispatch`.
- Ano obrigatório entre 1986 e 2026.
- Primeira execução recomendada: 1986.
- O ZIP RAW precisa existir e ser não vazio.
- O normalizador vigente é `scripts/ingestao/normalize_cotahist.py`.
- A validação usa `scripts/ingestao/validar_normalized.py`.
- São preservados SHA-256 do RAW e do CSV normalizado.
- Evidências são persistidas em `dados/cotahist/normalized/manifests/`.
- O CSV completo permanece como artefato da execução, não é automaticamente gravado no Git.
- Não há expansão para processamento em massa antes da validação do ano-piloto.

## Controle de risco operacional

O V7 não possui `schedule` nem `push`. Alterações em documentação, scripts ou dados não devem iniciar este workflow automaticamente.

## Próxima etapa

Executar manualmente para 1986 e auditar:

1. existência e integridade do ZIP;
2. quantidade de registros tipo 01;
3. primeira e última data;
4. conformidade do layout;
5. SHA-256 RAW/normalizado;
6. relatório de qualidade;
7. persistência das evidências;
8. ausência de novos disparos automáticos.

Somente após aprovação do teste será considerada a expansão para os demais anos.
