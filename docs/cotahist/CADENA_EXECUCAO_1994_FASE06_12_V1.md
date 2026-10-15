# Cadeia COTAHIST 1994 — FASE06→FASE12

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-011-94-FASE06-12-V1-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 6a4f6e2922bb9fa22deb42e129f4a6e814bc979615d7c75030c6c510378049c0 |
| **Commit de referência (versão anterior)** | [7a09339f3244b84dd165400279b6da090bd2bb80](https://github.com/carlos-andrade/B3/commit/7a09339f3244b84dd165400279b6da090bd2bb80) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


Versão: V2.0
Data: 2026-10-01

## Objetivo

Reproduzir para 1994 a cadeia de auditoria usada no 1993 certificado, sem reutilizar evidência de 1993 como evidência de 1994.

## Ordem

RUN_START → FASE06 → FASE07 → FASE08 → FASE09 → FASE10 → FASE11 → FASE12.

## Implementação

FASE06–08:
scripts/ingestao/gerar_evidencias_cotahist_1994_fases06_08_v1.py

O executor foi derivado da cadeia retrospectiva certificada de 1993 e adaptado para 1994, preservando comparação RAW × NORMALIZED, 12 campos críticos, alias canônico preabe, comparação numérica por Decimal, identificação de chaves, validação estrutural de calendário, validações OHLC e fail-closed.

FASE09–12:
scripts/ingestao/gerar_cadeia_cotahist_1994_fases09_12_v1.py

São produzidas em sequência:
- FASE09 — pré-release
- FASE10 — integridade independente
- FASE11 — certificação
- FASE12 — fechamento/transição

## Regra anti-falso-positivo

A cadeia não altera o README para provar execução.

A ordem permanece:
execução → evidência → validação → README.

## Estado

A implementação da cadeia está publicada no repositório. Isso não equivale à prova de execução do GitHub Actions. A conclusão de cada fase depende da evidência efetivamente produzida pelo runner.

## Critério de promoção

FASE07 somente após FASE06 VALIDADO.
FASE08 somente após FASE07 VALIDADO.
FASE09 somente após FASE08 VALIDADO.
FASE10 somente após FASE09 liberado.
FASE11 somente após FASE10 VALIDADO.
FASE12 somente após FASE11 VALIDADO.

O README permanece fora da cadeia de evidência.
