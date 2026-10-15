# ÍNDICE CANÔNICO DE CAMINHOS — COTAHIST

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-023-HOS-COTAHIST-V1-MD |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO_COTAHIST |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 1194897fa413b93b778cd8ad890d5d4700d8e6239e82b26415f7113b51bf3ee3 |
| **Commit de referência (versão anterior)** | [b65ba085fcb987a4457198fc0d31e4e9f7364fbb](https://github.com/carlos-andrade/B3/commit/b65ba085fcb987a4457198fc0d31e4e9f7364fbb) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; evidências e referências no corpo do documento |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


**Versão:** 1.0  
**Data:** 2026-10-01  
**Status:** VIGENTE

## 1. Regra de resolução

Para qualquer ano `AAAA`, resolver primeiro:

`AAAA → dados/cotahist/raw/anual/COTAHIST_AAAAA.ZIP`

Não utilizar busca ampla como substituto do caminho canônico.

## 2. Estrutura

| Função | Caminho |
|---|---|
| RAW anual | `dados/cotahist/raw/anual/COTAHIST_A<AAAA>.ZIP` |
| Manifesto | `dados/cotahist/manifests/COTAHIST_A<AAAA>.json` |
| Checksum | `dados/cotahist/checksums/COTAHIST_A<AAAA>.ZIP.sha256` |
| Normalizado anual | `dados/cotahist/normalized/anual/COTAHIST_A<AAAA>.csv` |
| Qualidade/evidências | `dados/cotahist/quality/` |
| Certificação anual | `dados/cotahist/certificacao/` |
| Documentação normativa | `docs/cotahist/` |
| Workflows | `.github/workflows/` |
| Scripts de ingestão | `scripts/ingestao/` |

## 3. Regra de existência

Se o arquivo existir no caminho canônico, ele deve ser tratado como **PRESENTE**.

Se não for encontrado, a investigação deve verificar:

1. caminho exato;
2. árvore do repositório;
3. manifesto;
4. checksum;
5. matriz de certificação;
6. evidências de qualidade.

Somente depois disso pode ser classificado como AUSENTE.

## 4. Regra de aquisição

A aquisição somente deve ocorrer quando houver uma lacuna real.

Se RAW, manifesto e checksum já existirem e forem coerentes, não baixar nem duplicar o arquivo.

## 5. Regra de validação

**PRESENTE ≠ VALIDADO ≠ CERTIFICADO ≠ FECHADO.**

Cada estado exige sua própria evidência.

## 6. Estado confirmado em 2026-10-01

A matriz `COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv` registra RAW presente para 1986–2026.

1995 foi confirmado diretamente no caminho canônico:

`dados/cotahist/raw/anual/COTAHIST_A1995.ZIP`

Manifesto e checksum de 1995 registram:

`de553f41a3ce15ec8a082ed1c2d451df58520a447d3f39417f45e7feb5a995fc`

## 7. Precedência operacional

O índice deve ser consultado antes de:

- nova aquisição;
- criação de manifesto;
- geração de checksum;
- declaração de ausência;
- criação de duplicata;
- início de uma nova fase.

## 8. Regra final

> **Primeiro localizar. Depois validar. Só então adquirir, corrigir ou avançar.**

<!-- FASE06 gate retrigger auditavel 2026-10-01 -->
