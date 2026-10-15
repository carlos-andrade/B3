# Orquestrador Anual Canônico COTAHIST — V1 (DRY-RUN)

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-031-UAL-CANONICO-V1-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 69ffdb2518405dbb330ada3c5f0b3e3a88f5b2fbfd368584bea20c23f1d9552c |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


**Data:** 2026-09-29  
**Objetivo:** testar a precedência semântica do pipeline anual sem substituir, desativar ou disparar os workflows legados.

## Regra central

O orquestrador não considera um arquivo existente como prova suficiente de que uma fase anterior foi executada. Cada promoção exige evidência identificável.

Fluxo alvo:

00 GOVERNANÇA → 01 RAW → 02 INTEGRIDADE DA FONTE → 03 PARSING → 04 NORMALIZAÇÃO → 05 MANIFESTO → 06 RECONCILIAÇÃO → 07 IDENTIDADE/CHAVES → 08 SEMÂNTICA/CALENDÁRIO → 09 PRÉ-RELEASE → 10 VALIDAÇÃO INDEPENDENTE → 11 CERTIFICAÇÃO → 12 PUBLICAÇÃO/FECHAMENTO

## Modo DRY-RUN

- Somente leitura.
- Não altera arquivos.
- Não faz commit.
- Não faz push.
- Não publica dataset.
- Não desativa workflows existentes.
- Não promove nenhum ano.
- Produz apenas um resumo no log da execução.

## Primeiro caso de teste

Ano: **1993**.

1993 foi escolhido porque já possui evidência de FASE10 e certificação estrutural conhecidas. O DRY-RUN não deve simplesmente repetir esse resultado: deve testar se as pré-condições 00–09 estão documentalmente demonstradas.

## Estados

- OK: evidência encontrada e compatível.
- AUSENTE: não há evidência suficiente.
- BLOQUEADO: uma dependência obrigatória anterior está ausente.
- NAO_APLICAVEL: fase explicitamente fora do escopo do ano.
- EXCECAO_CONTROLADA: somente quando uma regra formal registrada no repositório justificar a exceção.

## Gate de promoção

A FASE10 só pode ser marcada como LIBERADA quando 01–09 estiverem em estado aceitável. A existência de COTAHIST_*_FASE10_INTEGRIDADE_V1.json não retrocertifica as fases anteriores.

## Resultado esperado do primeiro DRY-RUN

Para 1993, espera-se que:

- RAW e manifesto sejam encontrados;
- evidência FASE10 seja encontrada;
- certificação anual seja encontrada;
- as fases históricas 06–09 sejam identificadas como não suficientemente documentadas, caso não exista evidência específica para elas;
- o resultado final do DRY-RUN seja BLOQUEADO PARA PROMOÇÃO, sem invalidar a FASE10 já registrada.

Esse resultado é intencional: o teste serve para revelar a lacuna de rastreabilidade antes de tentar usar o novo DAG para 1994.

## Critério para 1994

1994 só poderá entrar no orquestrador canônico depois que:

1. o DRY-RUN de 1993 for executado;
2. as lacunas encontradas forem classificadas;
3. as fases 00–09 forem representadas por evidências reais ou regras formais de equivalência;
4. o DAG for testado novamente em ano já certificado;
5. somente então for criado o caminho controlado de promoção de 1994.

## Relação com workflows legados

Os workflows existentes continuam ativos durante esta fase. O orquestrador é uma camada de verificação de precedência, não uma migração automática.

A migração futura deve ser feita por substituição controlada, com teste, evidência e rollback definido.
