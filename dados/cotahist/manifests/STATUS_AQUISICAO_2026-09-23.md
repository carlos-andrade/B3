# STATUS DE AQUISIÇÃO — COTAHIST 1986 → ATUAL

**Arquivo:** STATUS_AQUISICAO_2026-09-23.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Estado operacional da aquisição da série histórica COTAHIST  
**Caminho:** dados/cotahist/manifests/STATUS_AQUISICAO_2026-09-23.md  
**Data:** 23/09/2026  
**Repositório:** carlos-andrade/B3

## Escopo
- Início oficial: **1986**
- Fim: período mais recente disponibilizado pela B3
- Fonte primária: B3 — Cotações Históricas
- Produto: COTAHIST anual

## Verificação
A B3 confirma que sua série histórica contém preços dos títulos negociados desde 1986. O layout oficial define COTAHIST.AAAA.TXT, com registros de 245 bytes, header 00, cotação 01 e trailer 99.

## Resultado da tentativa neste ambiente
**1986 ainda NÃO está marcado como ingerido.**

A tentativa de acesso direto ao endpoint legado não pôde ser executada neste ambiente porque o resolvedor DNS não conseguiu resolver o host bvmf.bmfbovespa.com.br.

Portanto:
- nenhum ZIP foi fabricado;
- nenhum RAW foi declarado;
- nenhum checksum foi inventado;
- nenhum ano foi marcado como validado.

## Ferramenta preparada
scripts/ingestao/download_cotahist_1986_atual.py

A ferramenta baixa os anuais, preserva o ZIP, calcula SHA-256, valida ZIP/TXT, exige 245 bytes por registro, verifica header 00 e trailer 99, conta registros e grava manifesto JSON.

## Execução
python scripts/ingestao/download_cotahist_1986_atual.py --start 1986 --end 2026

## Regra
**Não considerar um ano ingerido sem ZIP + SHA-256 + validação estrutural + manifesto.**

O escopo permanece **1986 → atual**.
