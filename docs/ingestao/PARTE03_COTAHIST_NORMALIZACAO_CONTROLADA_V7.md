# PARTE03 — COTAHIST NORMALIZACAO CONTROLADA V7

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-4696F3AD1B1A |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | f7792ea957ea0a4badef81a1e85c831029fe33287777a13086d15f86792e69df |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
