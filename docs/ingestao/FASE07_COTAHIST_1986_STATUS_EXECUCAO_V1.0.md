# FASE 07 — COTAHIST 1986 — STATUS DE EXECUÇÃO E EVIDÊNCIA

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-E45F637E0D30 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 0414123391c74502c09cb87f5dee4a37c24741bba24582bbac3e75641ce8bb94 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Projeto:** B3 — A Bolsa do Brasil  
**Escopo:** Identidade histórica COTAHIST 1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## Estado atual

**FASE 07 FECHADA COM ANOMALIA RESIDUAL K4 DOCUMENTADA.**

07A–07G foram executadas e possuem evidências. A revisão semântica 07F-S também foi concluída. A anomalia não foi corrigida nem artificialmente resolvida.

## Matriz de execução

| Frente | Tema | Execução | Estado |
|---|---|---:|---|
| 07A | Identidade histórica / K1–K4 | Sim | VALIDADA |
| 07B | TPMERC | Sim | VALIDADA |
| 07C | CODBDI | Sim | VALIDADA |
| 07D | CODISI | Sim | VALIDADA |
| 07E | DIMES | Sim | VALIDADA |
| 07F | Colisão K4 | Sim | VALIDADA |
| 07F-S | Revisão semântica K4 | Sim | CONCLUÍDA |
| 07G | Matriz final de identidade | Sim | VALIDADA |

## Colisão K4

Chave:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Foram preservadas duas linhas RAW consecutivas: 140808 e 140809.

As linhas possuem estatísticas de negociação diferentes e SHA-256 distintos. Portanto, não são duplicatas byte-a-byte.

## Revisão semântica 07F-S

Documento:

`docs/ingestao/FASE07F_S_COTAHIST_1986_REVISAO_SEMANTICA_K4_V1.0.md`

Classificação:

**ANOMALIA DE DUPLICIDADE ESTRUTURAL — SEM RESOLUÇÃO ECONÔMICA**

Regra operacional:

- preservar ambas as linhas;
- não deduplicar por K4;
- não somar os registros;
- não escolher arbitrariamente uma linha;
- marcar o par como anomalia;
- manter RAW e NORMALIZED inalterados.

## 07G — Matriz final

Evidência:

`dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_FINAL_V1.json`

- 177.981 registros;
- K4: 177.980 grupos;
- K4 unitários: 177.979;
- K4 repetidos: 1;
- linhas no grupo repetido: 2;
- 2.699 CODNEG distintos;
- 1.817 CODNEG com múltiplos contextos de atributos;
- residual_k4_count = 1;
- RAW e NORMALIZED inalterados.

## Integridade

Nenhum registro histórico foi excluído, corrigido ou substituído.

## Encerramento

A FASE 07 está encerrada operacionalmente. A única colisão residual permanece rastreável como exceção de qualidade e deve acompanhar as fases posteriores do pipeline.

**Próxima frente: FASE 08 — calendário histórico e reconciliação das sessões de negociação.**
