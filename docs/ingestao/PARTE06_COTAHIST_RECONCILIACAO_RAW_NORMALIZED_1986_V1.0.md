# PARTE06 — Reconciliação Determinística RAW → NORMALIZED — COTAHIST 1986 V1.0

**Arquivo:** PARTE06_COTAHIST_RECONCILIACAO_RAW_NORMALIZED_1986_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Reprodutibilidade e integridade da transformação RAW → NORMALIZED  
**Caminho:** docs/ingestao/PARTE06_COTAHIST_RECONCILIACAO_RAW_NORMALIZED_1986_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## Objetivo

Demonstrar, por execução efetiva, que o COTAHIST 1986 NORMALIZED registrado no manifesto pode ser reproduzido a partir do RAW atualmente preservado, usando o parser versionado.

## Critério

A reconciliação só é considerada **RECONCILIADO** quando todos os testes forem verdadeiros:

1. SHA-256 do RAW atual = SHA-256 registrado no manifesto;
2. parser = versão contratada 1.1.0;
3. contagem independente de registros tipo 01 no RAW = linhas NORMALIZED do manifesto;
4. número de linhas geradas pelo parser = manifesto;
5. número de campos gerados = manifesto;
6. SHA-256 do NORMALIZED reproduzido = SHA-256 registrado no manifesto.

## Princípio

O teste não altera o RAW e não promove nenhum arquivo gerado a fonte primária.

A evidência estabelece:

`RAW identificado por SHA-256`
→ `parser 1.1.0`
→ `NORMALIZED reproduzido`
→ `SHA-256 idêntico ao manifesto`

Isso permite verificar se o artefato NORMALIZED anteriormente validado é deterministicamente reproduzível.

## Resultado esperado para 1986

Manifesto atualmente registrado:

- RAW SHA-256: `350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`
- NORMALIZED SHA-256: `fbd00ff5b24075813132193dc794e29015df20b7dc6bedad7e896b30406329`
- Registros NORMALIZED: `177981`
- Campos: `25`
- Parser: `1.1.0`

Esses valores são referências de manifesto; a classificação final depende da execução do workflow.

## Regra de decisão

### RECONCILIADO

Todos os testes passam.

### REVISAR

Qualquer teste falha.

Em caso de REVISAR, nenhum valor do RAW será corrigido. O próximo passo será localizar a divergência entre fonte, parser, manifesto ou artefato.

## Artefatos

- Script: `scripts/ingestao/reconciliar_raw_normalized_cotahist_1986_v1.py`
- Workflow: `.github/workflows/cotahist-reconciliacao-raw-normalized-1986-v1.yml`
- Evidência: `dados/cotahist/quality/COTAHIST_1986_RECONCILIACAO_RAW_NORMALIZED_V1.json`

## Estado

**PENDENTE DE EXECUÇÃO.**

Nenhuma conclusão de reconciliação deve ser declarada antes da execução efetiva do workflow.
