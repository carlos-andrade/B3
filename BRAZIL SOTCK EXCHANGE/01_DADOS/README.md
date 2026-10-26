# 01 — DADOS

## Objetivo
Organizar dados de mercado e macroeconómicos com proveniência, versões e qualidade mensurável.

## Camadas
- `RAW/`: cópias imutáveis da origem, acompanhadas de metadados e SHA-256.
- `STAGING/`: parsing, validações de esquema e normalização preliminar.
- `CANONICAL/`: datasets reconciliados, deduplicados segundo regras explícitas e prontos para consumo.
- `ESQUEMAS/`: layouts, dicionários de campos, unidades, tipos e regras de compatibilidade.

## Gate de promoção
Validar origem/licença, hash, layout, contagens, campos obrigatórios, duplicados, cobertura temporal e reconciliação. Em caso de falha desconhecida, bloquear a promoção.

Não colocar segredos, credenciais ou dados de terceiros sem autorização neste repositório.
