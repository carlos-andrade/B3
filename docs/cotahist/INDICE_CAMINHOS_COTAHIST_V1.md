# ÍNDICE CANÔNICO DE CAMINHOS — COTAHIST

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
