# ROTINA DIÁRIA COTAHIST — 23:55 + 08:55 BRT

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-E485F4205CA6 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 92c7bd4840b16335c24e75c59d6429a52fd8a2474a0146dcdbca5d69595f4f4e|
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

**Arquivo:** PARTE01_ROTINA_ATUALIZACAO_DIARIA_COTAHIST_V1.1.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Atualização diária pré e pós-fechamento da base histórica COTAHIST  
**Caminho:** docs/ingestao/PARTE01_ROTINA_ATUALIZACAO_DIARIA_COTAHIST_V1.1.md  
**Data de criação:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## Rotina oficial

A base COTAHIST será consultada **duas vezes por dia**, indefinidamente:

1. **23:55 — horário de Brasília**
2. **08:55 — horário de Brasília, no dia seguinte**

O objetivo é obter a atualização disponibilizada pela B3 após o pregão e executar uma segunda conferência antes da abertura do pregão seguinte.

## Agendamento técnico

O GitHub Actions utiliza UTC. Brasília utiliza o fuso `America/Sao_Paulo`.

| Rotina | Brasília | UTC |
|---|---:|---:|
| Atualização 1 | 23:55 | 02:55 |
| Atualização 2 | 08:55 | 11:55 |

Cron configurado:

- `55 2 * * *`
- `55 11 * * *`

## Fluxo de cada execução

```
Horário programado
      ↓
Identificar ano em America/Sao_Paulo
      ↓
Consultar fonte B3
      ↓
Download com retries
      ↓
Validar ZIP
      ↓
Validar 245 bytes
      ↓
Header 00
      ↓
Registros 01
      ↓
Trailer 99
      ↓
SHA-256
      ↓
Manifesto VALIDADO
      ↓
Comparação com versão persistida
      ↓
Alteração? → commit + push
Sem alteração? → nenhuma alteração artificial
```

## Continuidade

A rotina possui agendamento sem data final.

`concurrency` usa grupo único e `cancel-in-progress: false`, evitando que uma execução seja cancelada automaticamente por outra.

A rotina também pode ser disparada manualmente por `workflow_dispatch`.

## Integridade

Falha de download, validação ou persistência não pode ser interpretada como ausência de dados.

Somente uma execução que conclua todas as validações pode produzir o estado `VALIDADO`.

## Auditoria

Cada atualização mantém:

- arquivo RAW;
- SHA-256;
- manifesto;
- histórico Git;
- evidência do workflow.

## Observação operacional

O horário é tratado explicitamente como **America/Sao_Paulo**, e não como o fuso do usuário ou do runner do GitHub.

## Implementação

Workflow:

`.github/workflows/cotahist-atualizacao-diaria.yml`

Commit da alteração:

`174e9677561362e6e52aa806d38f0b4d9f14f1a8`

Versão da rotina: **V1.1**

A versão anterior V1.0 foi substituída operacionalmente pela rotina V1.1.
