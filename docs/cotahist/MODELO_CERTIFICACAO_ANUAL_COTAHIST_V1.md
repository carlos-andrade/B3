# MODELO DE CERTIFICAÇÃO ANUAL COTAHIST V1

**Status:** VIGENTE  
**Data:** 2026-10-01  
**Repositório:** carlos-andrade/B3

## 1. Finalidade

Este documento transforma a certificação de 1993 em **baseline operacional** para as certificações retrospectivas seguintes.

O ano anterior certificado serve como referência de:
- cadeia de fases;
- estrutura de evidências;
- critérios de reconciliação;
- identidade/chaves;
- semântica e calendário;
- tratamento de exceções;
- gates de promoção;
- rastreabilidade Git e workflow.

A evidência de um ano **nunca** é copiada para outro ano como prova.

## 2. Baseline 1993

1993 é o primeiro ano da cadeia atual com:
- FASE06 VALIDADO;
- FASE07 VALIDADO;
- FASE08 VALIDADO;
- FASE12 concluída;
- decisão de fechamento e transição para 1994.

A FASE08 de 1993 registrou:
- datas válidas;
- ausência de fins de semana;
- ordenação cronológica;
- limites anuais;
- relações OHLC válidas;
- distribuição observada de TPMERC/CODBDI;
- lacunas úteis tratadas apenas como candidatas a não-pregão.

## 3. Regra de réplica

Para cada novo ano YYYY:

1. usar 1993 como modelo estrutural;
2. copiar somente a **lógica**, nunca as evidências;
3. substituir o ano, hashes, contagens e caminhos;
4. executar a cadeia sobre o RAW e NORMALIZED reais de YYYY;
5. publicar a evidência produzida pelo próprio ano;
6. bloquear qualquer divergência não explicada;
7. documentar exceções controladas quando houver evidência objetiva para isso.

## 4. Exceção semântica controlada

Uma anomalia não deve ser corrigida silenciosamente.

Quando uma regra semântica encontra uma ocorrência incompatível com o padrão esperado, existem três estados:

| Situação | Estado |
|---|---|
| Regra satisfeita | VALIDADO |
| Anomalia conhecida, determinística, rastreada e sem alteração do dado | VALIDADO_COM_EXCECAO |
| Anomalia não explicada ou não reproduzível | BLOQUEADO |

### 4.1 Requisitos mínimos

Uma exceção controlada deve registrar:
- ano;
- fase;
- regra que falhou;
- ocorrência exata;
- identificadores do registro;
- valores originais;
- linha física quando aplicável;
- SHA-256 do RAW ao qual a exceção pertence;
- justificativa da classificação;
- confirmação de que nenhum dado foi alterado;
- decisão.

### 4.2 Regra de segurança

A exceção deve ser **específica**.

Não é permitido transformar:
- "qualquer TPMERC=080 é válido"
em uma exceção ampla.

É permitido registrar uma ocorrência determinística vinculada ao RAW exato, como:
- linha;
- TPMERC;
- CODBDI;
- CODNEG;
- preços observados;
- SHA-256.

Se o RAW mudar, a exceção deixa de ser automaticamente válida e a FASE08 deve voltar a bloquear.

## 5. Caso 1994

A execução real do RUN_ID **36832779037** encontrou:

- FASE06: VALIDADO;
- FASE07: VALIDADO;
- FASE08: BLOQUEADO.

A evidência produzida no artefato do run identificou duas violações OHLC:

1. linha 35516 — TPMERC 080, CODBDI 82, CODNEG OTC 55;
2. linha 39735 — TPMERC 080, CODBDI 82, CODNEG OTC 89.

A FASE06 confirmou que a reconciliação RAW × NORMALIZED não apresentou divergência nos 12 campos críticos. Portanto, essas ocorrências não devem ser "corrigidas" na normalização.

A decisão técnica adotada para 1994 é classificá-las como **exceções semânticas controladas**, condicionadas ao SHA-256 do RAW:

`b3bbd8e8d290c36943398c6f99a04e0721db2ebac3b917904df9efaacf3172eb`

Os registros permanecem exatamente como fornecidos pela fonte.

## 6. O que não pode acontecer

- alterar PREULT para fazê-lo caber no PREMIN/PREMAX;
- alterar PREMIN/PREMAX;
- excluir registros;
- mascarar a ocorrência;
- transformar todas as opções em exceção;
- marcar FASE08 como VALIDADO sem registrar a exceção;
- executar FASE09–12 enquanto existir bloqueio não classificado.

## 7. Gate de promoção

A cadeia posterior pode aceitar:

- FASE06 = VALIDADO ou VALIDADO_COM_EXCECAO;
- FASE07 = VALIDADO ou VALIDADO_COM_EXCECAO;
- FASE08 = VALIDADO ou VALIDADO_COM_EXCECAO.

Qualquer outro estado mantém o fluxo bloqueado.

## 8. Publicação de evidências

O workflow deve publicar somente arquivos que realmente existam.

A ausência de FASE09–12 durante um bloqueio em FASE08 é um resultado esperado do fail-closed e não pode produzir uma segunda falha artificial de `git add pathspec`.

## 9. Aplicação futura

Este documento deve ser consultado antes de iniciar a certificação de 1995 e dos anos seguintes.

Para cada novo ano, criar um comparativo:

`docs/cotahist/COMPARATIVO_BASELINE_YYYY_VS_YYYY+1_*.md`

e registrar:
- baseline usado;
- diferenças de implementação;
- diferenças de dados;
- exceções;
- decisões;
- commits;
- RUN_IDs;
- estado oficial.

## 10. Princípio permanente

**O baseline anterior ensina o processo; o próprio ano fornece a prova.**

A certificação deve preservar a fonte, tornar as exceções visíveis e impedir que uma anomalia seja escondida para obter um resultado verde.
