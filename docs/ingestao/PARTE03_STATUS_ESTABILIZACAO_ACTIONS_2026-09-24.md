# PARTE03 — STATUS DE ESTABILIZACAO DOS GITHUB ACTIONS

Data: 2026-09-24

## Objetivo

Registrar a estabilizacao dos workflows COTAHIST e separar falhas historicas de novos eventos.

## Estado atual

Em 24/09/2026 foram removidos workflows COTAHIST legados da arvore `.github/workflows/`, incluindo as familias 2011-2026 e os workflows adicionais identificados posteriormente.

## Remocoes adicionais confirmadas

- `cotahist-normalizacao-historica.yml` — `90bc8b6ce6952f6015431c0a49cc4bf699e48a1c`
- `cotahist-normalizacao-teste.yml` — `e5b8ab38beabc0fa88ce819160d84150ce381a73`
- `cotahist-aquisicao.yml` — `c219700259574f90c48f2299cededcba11c43e37`
- `cotahist-atualizacao-diaria.yml` — `2fbd6e29647052a1b038324fa26431c1ad019496`
- `cotahist-auditoria-duplicidades.yml` — `7e83daa45b7b4b5708c92754385e9799c8f5e75b`
- `cotahist-reconciliacao-calendario-v1.yml` — `435ba4324673fe710c2de285bafd599625e7d106`
- `cotahist-auditoria-continuidade-1986-2026-v1.yml` — `d523d88a3a1daf43ef6b9f76530dcfd74e7c8814`
- `cotahist-auditoria-continuidade-1986-2026-v2.yml` — `f2a8aece4db0ab7ea2307546f165cadf917fcd20`
- `cotahist-normalizacao-1986-2010-v8.yml` — `e30e73e62c16cc2979d6455076e7f58b138a0209`
- `cotahist-normalizacao-1986-teste-v7.yml` — `3f99d47412df2ad1adb2fcef50b80a28ce406286`
- `cotahist-resumo-auditoria-v2.yml` — `135f511eadf5151d3b91d8e94377fc6a6ee21439`

Os seis `cotahist-normalizacao-2011-2026*` já haviam sido removidos no ciclo anterior de estabilizacao.

## Diagnostico dos gatilhos

Os workflows adicionais continham gatilhos `push`, inclusive para alterações em scripts e nos próprios workflows. Isso mantinha risco de novas execuções automáticas. A árvore atual foi limpa desses workflows antes da reconstrução do pipeline.

## Runs residuais

A consulta mais recente da API de Actions mostrou os runs mais novos como eventos de remoção executados às 12:52 UTC, todos `completed/failure`. Eles são residuais do estado anterior do workflow no momento dos respectivos pushes.

Não há, nesta verificação, evidência de um novo run COTAHIST posterior causado por um workflow COTAHIST ainda presente na árvore.

## Próximo teste

1. Fazer um commit fora de `.github/workflows/`.
2. Verificar que não nasce novo run COTAHIST.
3. Somente após essa confirmação criar um único **COTAHIST V7**.
4. V7 começa manualmente e com **um único ano de teste**.
5. Expandir somente depois da validação do ano-piloto.

## Limitação

A API disponível para os runs históricos não expôs jobs suficientes para atribuir a falha interna a uma etapa específica. A correção atual elimina os gatilhos automáticos legados; ela não reclassifica tecnicamente a causa dos failures históricos.
