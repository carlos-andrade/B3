# FASE 10A — M3 — Migração NORMALIZED anual controlada V1.0

**Arquivo:** FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10A_M3_MIGRACAO_NORMALIZED_ANUAL_CONTROLADA_V1.0.md  
**Data de criação:** 2026-09-28  
**Repositório:** carlos-andrade/B3  
**Status:** M3-0 CONCLUÍDO — GIT_STANDARD_LIMIT — M3-1 EM DECISÃO/PROVA

## 1. Objetivo

Migrar os anos COTAHIST ainda sem NORMALIZED anual físico para o caminho canônico:

`dados/cotahist/normalized/anual/COTAHIST_A{ANO}.csv`

mantendo:

- RAW imutável;
- parser 1.1.0;
- SHA-256;
- quality manifest;
- certificação física V2;
- rastreabilidade por commit;
- fail-closed.

## 2. Regra de segurança

Nenhum lote será iniciado antes do **Gate de Capacidade M3-0**.

Motivo: o tamanho do NORMALIZED pode ser muito superior ao ZIP RAW. A existência do RAW abaixo de 100 MB não prova que o CSV normalizado caberá no armazenamento Git padrão.

O contrato V2.0 exige interromper a migração se o limite de armazenamento/versionamento for atingido.

## 3. M3-0 — Gate de capacidade

Ano de referência:

**2026**

A execução deve:

1. regenerar NORMALIZED 2026 em `/tmp`;
2. calcular tamanho físico;
3. calcular SHA-256;
4. confirmar contagem/campos/datas contra o manifesto;
5. **não persistir o CSV**;
6. classificar:
   - `GIT_STANDARD_OK` se < 100 MB;
   - `GIT_STANDARD_LIMIT` se >= 100 MB;
7. registrar evidência.

## 4. Por que 2026 foi escolhido

O RAW 2026 já possui aproximadamente **84,5 MB** no repositório, enquanto 1987 demonstrou que a normalização pode expandir significativamente o volume físico.

Essa relação é apenas indicativa; o valor decisório será o tamanho real medido pela execução M3-0.

## 5. Regra de decisão

### Se NORMALIZED 2026 < 100 MB

Prosseguir para lotes controlados.

### Se NORMALIZED 2026 >= 100 MB

**PARAR.**

Não fazer:

- commit parcial;
- compressão manual para mascarar o limite;
- divisão arbitrária do CSV sem contrato;
- alteração do RAW;
- redução de campos;
- deduplicação.

Nesse caso será necessário decidir entre Git LFS ou armazenamento externo versionado, atualizar o contrato NORMALIZED V2.0 e somente depois continuar.

## 6. Estratégia após aprovação do gate

A migração será feita em lotes pequenos, com preferência inicial para anos históricos de menor volume.

Cada ano:

`RAW → NORMALIZE → SHA → VALIDATE → PERSIST → CERTIFY V2 → RECONCILE`

Um ano com falha não autoriza declarar o lote inteiro concluído.

## 7. Critérios de conclusão M3

Para cada ano migrado:

- CSV físico presente;
- tamanho validado;
- SHA físico = manifesto;
- linhas físicas = manifesto;
- schema = 25;
- datas coerentes;
- certificação física V2 = CERTIFICADO;
- commit de persistência registrado.

Depois dos lotes:

- Dataset Oficial V2 deve executar com SUCCESS;
- 1986 permanece com sua exceção semântica documentada;
- nenhum RAW é alterado.

## 8. Estado

M1 — **APROVADO**  
M2 — **APROVADO**  
M3-0 — **CONCLUÍDO — GIT_STANDARD_LIMIT**
M3-1 — **EM DECISÃO/PROVA — GIT LFS**
M3 histórico — **BLOQUEADO**

Próxima etapa: **prova controlada de armazenamento do NORMALIZED 2026 via Git LFS, seguida de validação física, SHA, certificação V2, CI e Dataset Oficial.**

Registro formal: `docs/ingestao/M3-0_RESULTADO_GATE_CAPACIDADE_NORMALIZED_2026_2026-09-28.md`

Decisão M3-1: `docs/ingestao/M3-1_DECISAO_ARMAZENAMENTO_NORMALIZED_COTAHIST_V1.0.md`
