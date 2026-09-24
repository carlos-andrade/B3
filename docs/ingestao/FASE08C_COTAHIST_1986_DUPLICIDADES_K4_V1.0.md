# FASE 08C — Análise Estrutural das Duplicidades K4 — COTAHIST 1986

**Arquivo:** FASE08C_COTAHIST_1986_DUPLICIDADES_K4_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Classificação estrutural de colisões K4 em todo o COTAHIST 1986  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Determinar se a colisão K4 de VGO 2 em 10/10/1986 é um caso isolado ou pertence a uma classe mais ampla de duplicidades estruturais no COTAHIST 1986.

A análise deve responder:

1. quantos grupos K4 aparecem mais de uma vez;
2. quantas linhas estão envolvidas;
3. quantas colisões são no mesmo pregão e quantas atravessam pregões;
4. em quais combinações de mercado ocorrem;
5. quais campos diferem dentro de cada colisão;
6. se a colisão VGO 2 pertence a uma classe observável de eventos.

## 2. Definição operacional

Para esta fase, K4 é a chave histórica já utilizada na FASE 07F/08:

`DATA + CODBDI + CODNEG + TPMERC + CODISI + DIMES + ESPECI + PRAZOT + DATVEN + PREEXE + INDOPC + PTOEXE`

Uma **duplicidade K4** é qualquer chave com duas ou mais linhas tipo 01 no mesmo COTAHIST 1986.

A classificação é estrutural. Ela não determina identidade econômica nem erro de origem.

## 3. Método

O script:

`scripts/ingestao/analisar_duplicidades_k4_cotahist_1986_v1.py`

lê diretamente:

`dados/cotahist/raw/anual/COTAHIST_A1986.ZIP`

e produz:

`dados/cotahist/quality/COTAHIST_1986_FASE08C_DUPLICIDADES_K4_V1.json`

O cálculo preserva o RAW e compara, dentro de cada grupo duplicado, os campos de identidade e os principais campos estatísticos.

## 4. Classificações produzidas

Cada grupo duplicado recebe, entre outros, estes atributos:

- tamanho do grupo;
- mesmo pregão ou pregões diferentes;
- mercado CODBDI/TPMERC;
- conjunto de campos divergentes;
- presença ou ausência da colisão VGO 2 de 10/10/1986.

A distribuição das assinaturas de divergência é particularmente importante: ela permite verificar se VGO 2 reproduz um padrão recorrente ou constitui uma exceção estrutural.

## 5. Governança

- RAW não é alterado.
- Nenhuma linha é excluída.
- Nenhuma linha é consolidada.
- Nenhuma identidade econômica é inferida.
- A classificação descreve somente o que está presente no arquivo.
- Qualquer explicação histórica posterior deverá ser sustentada por documentação contemporânea.

## 6. Artefato e execução

Workflow:

`.github/workflows/cotahist-fase08c-duplicidades-k4-1986-v1.yml`

Implementação inicial:

- script commit: `3268cb308cc1f8eb97249f66f163a650be1fad48`
- workflow commit: `f1a91f8e36aa5c0ab4c5b92db23ce97ed4e4121c`

**Estado no momento da criação:** IMPLEMENTADO.

A fase somente será marcada como EXECUTADA após a publicação do JSON pelo GitHub Actions. Somente após conferência do artefato publicado será marcada como VALIDADA.

## 7. Próxima decisão analítica

Após a execução, comparar:

`VGO 2 / 10-10-1986 / CODBDI 62 / TPMERC 030`

com todas as demais colisões K4.

Se a mesma assinatura de divergência aparecer repetidamente, ela será tratada como **padrão observado** e investigada documentalmente.

Se não aparecer, a colisão VGO 2 será tratada como **caso estruturalmente singular**, sem concluir que seja erro.

## 8. Critério de fechamento da FASE 08C

A FASE 08C estará VALIDADA quando:

1. o JSON for publicado pelo workflow;
2. o SHA do RAW no artefato coincidir com o COTAHIST 1986 utilizado nas fases anteriores;
3. os totais de registros tipo 01 forem reconciliados;
4. os grupos duplicados puderem ser reproduzidos pela definição K4;
5. a colisão VGO 2 estiver explicitamente localizada na classificação;
6. nenhum resultado depender de alteração do RAW.

A FASE 08C não fecha a investigação histórica da FASE 08. Ela apenas estabelece a evidência estrutural necessária para decidir se a colisão VGO 2 é isolada ou pertence a uma classe recorrente.


## 9. Resultado publicado — 24/09/2026

O workflow publicou o artefato:

`dados/cotahist/quality/COTAHIST_1986_FASE08C_DUPLICIDADES_K4_V1.json`

Commit de publicação: `57ce26674059ec50dbdf5731539797f32c01dd55`.

### 9.1 Reconciliação

- registros tipo 01: **177.981**;
- grupos K4: **177.980**;
- grupos K4 duplicados: **1**;
- linhas pertencentes a grupos duplicados: **2**;
- duplicidades no mesmo pregão: **1**;
- duplicidades entre pregões: **0**;
- tamanho máximo do grupo: **2**;
- mercado da única colisão: **CODBDI 62 / TPMERC 030**;
- colisão identificada: **VGO 2 em 10/10/1986**.

O SHA-256 do RAW publicado é:

`350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`

Esse valor deve ser usado como âncora de reconciliação nas fases seguintes.

### 9.2 Resultado estrutural

A análise encontrou **uma única colisão K4 em todo o COTAHIST 1986**.

Portanto, com base no arquivo analisado, a colisão VGO 2:

- não é uma ocorrência recorrente em múltiplos pregões;
- não é uma classe recorrente de colisões K4 em 1986;
- não ocorre simultaneamente em outros mercados dentro da mesma classificação K4;
- é o único grupo com duas linhas que compartilham a mesma chave K4.

As duas linhas permanecem economicamente diferentes nos campos estatísticos: número de negócios, quantidade, volume e preços de negociação. A igualdade da K4 significa somente igualdade dos campos que compõem a chave; **não significa igualdade dos agregados de negociação**.

### 9.3 Conclusão da FASE 08C

**FATO VALIDADO:** a colisão VGO 2 é **estruturalmente singular dentro do COTAHIST 1986** segundo a K4 definida nas FASES 07/08.

**FATO VALIDADO:** as duas linhas pertencem ao mesmo pregão e ao mesmo contexto `CODBDI=62 / TPMERC=030`.

**FATO VALIDADO:** a K4 é idêntica, enquanto os agregados estatísticos são diferentes.

**NÃO DETERMINADO:** a causa histórica da duplicidade.

Não há base para converter essa singularidade em “erro”, “duplicação indevida” ou “dois ativos” sem documentação contemporânea.

A investigação histórica da FASE 08 permanece aberta. O foco passa agora de uma busca por recorrência estrutural para a busca de **evidência primária contemporânea de 10/10/1986** capaz de explicar a origem dos dois agregados.
