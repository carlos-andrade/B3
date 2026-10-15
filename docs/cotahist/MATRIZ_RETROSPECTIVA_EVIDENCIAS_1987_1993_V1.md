# Matriz Retrospectiva de Evidências COTAHIST — V1

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-028-AS-1987-1993-V1-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 2570838dedf87ec4afa80e7def8baba3e8fde1ad02a9620a17601e77ceff8d35 |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


**Data:** 2026-09-29  
**Escopo:** 1987–1993  
**Finalidade:** impedir que certificações estruturais posteriores sejam usadas como prova retroativa de fases anteriores.

## Legenda

- **COMPROVADA** — existe artefato específico identificável.
- **PARCIAL** — há evidência relacionada, mas não cobre integralmente o contrato da fase.
- **NAO_COMPROVADA** — não foi localizada evidência específica suficiente no inventário atual.
- **EXCECAO_CONTROLADA** — regra histórica formalmente documentada.

## Matriz

| Ano | 00 Governança | 01 RAW | 02 Fonte | 03 Parsing | 04 Normalização | 05 Manifesto | 06 Reconciliação | 07 Chave/Identidade | 08 Semântica/Calendário | 09 Pré-release | 10 Independente | 11 Certificação | 12 Fechamento |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1987 | COMPROVADA | COMPROVADA | PARCIAL | PARCIAL | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | PARCIAL | COMPROVADA | COMPROVADA/TRANSIÇÃO |
| 1988 | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA |
| 1989 | COMPROVADA | COMPROVADA | PARCIAL | PARCIAL | COMPROVADA | COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA |
| 1990 | COMPROVADA | COMPROVADA | PARCIAL | PARCIAL | COMPROVADA | COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA |
| 1991 | COMPROVADA | COMPROVADA | PARCIAL | PARCIAL | COMPROVADA | COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA |
| 1992 | COMPROVADA | COMPROVADA | PARCIAL | PARCIAL | COMPROVADA | COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA |
| 1993 | COMPROVADA | COMPROVADA | PARCIAL | PARCIAL | COMPROVADA | COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | NAO_COMPROVADA | COMPROVADA | COMPROVADA | COMPROVADA |

## Evidências fortes identificadas

### 1987

A certificação final registra explicitamente os gates estruturais de reconciliação RAW-normalized, chave lógica, OHLC, quantidade/volume e calendário.

Também registra auditoria semântica e a exceção de PRAZOT, cuja validação independente permaneceu inconclusiva. Portanto, 1987 é estruturalmente certificado com exceção semântica controlada, e não deve ser tratado como semanticamente resolvido.

### 1988

Existe uma cadeia documental muito mais completa:

- auditorias de calendário;
- chave lógica;
- integridade dos campos;
- OHLC;
- quantidade/volume;
- semântica;
- reconciliação RAW-normalized;
- certificações das fases 1, 2, 3, 5, 6, 7, 8, 9 e 10;
- validação independente;
- fechamento/abertura de 1989.

A reconciliação final confirma os gates estruturais e preserva as exceções semânticas. A validação independente reproduziu os fingerprints das exceções.

### 1989–1993

O repositório contém, para esses anos:

- RAW;
- manifesto;
- normalização;
- validação independente FASE10;
- certificação anual;
- fechamento/abertura do ano seguinte.

Porém, o inventário atual não localizou evidência específica equivalente à cadeia retrospectiva de fases 06–09 existente em 1987/1988.

Isso não significa que essas atividades não tenham ocorrido. Significa apenas que, no estado documental atual do repositório, elas não podem ser consideradas comprovadas.

## Regra de interpretação

A matriz não rebaixa nem invalida as certificações já emitidas.

Ela introduz uma distinção formal:

**CERTIFICAÇÃO EXISTENTE ≠ RASTREABILIDADE COMPLETA DAS FASES 00–12.**

Essa distinção é necessária para o novo orquestrador.

## Consequência para 1994

O ano de 1994 não deve ser promovido pela simples existência de RAW, manifesto, normalização, matriz anual ou evidência estrutural posterior.

Antes da FASE10 de 1994, o pipeline canônico deverá possuir uma forma explícita de demonstrar as pré-condições 01–09.

## Próxima ação controlada

1. Criar contratos formais de evidência para fases 06–09.
2. Mapear retrospectivamente os artefatos 1987/1988 para esses contratos.
3. Definir se 1989–1993 podem ser classificados por equivalência documental, sem inventar evidências.
4. Executar novamente o DRY-RUN de 1993.
5. Só depois testar 1994.
