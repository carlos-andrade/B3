# COTAHIST 1998 — FASE06C — Investigação semântica do TPMERC=030

**Data:** 2026-10-02  
**Escopo:** registros TPMERC=030 (mercado a termo) do COTAHIST 1998  
**Objetivo:** determinar se a regra convencional PREMIN <= PREMED <= PREMAX e PREMIN <= PREULT <= PREMAX pode ser usada como regra de rejeição para registros históricos de termo.

## 1. Evidência interna do projeto

A FASE06B encontrou 8.234 registros TPMERC=030, todos com CODBDI=62, e 29 registros que violam pelo menos uma das relações convencionais de OHLC. A evidência original está preservada em dados/cotahist/quality/COTAHIST_1998_FASE06B_CONTEXT_TERM_V1.json.

| Regra | Casos |
|---|---:|
| PREABE fora de [PREMIN,PREMAX] | 16 |
| PREMED fora de [PREMIN,PREMAX] | 11 |
| PREULT < PREMIN | 3 |
| PREULT > PREMAX | 0 |

29 / 8.234 = 0,3521% dos registros TERM.

## 2. Evidência documental do layout

O layout oficial de Cotações Históricas da B3 define PREABE, PREMAX, PREMIN, PREMED e PREULT como campos do papel-mercado. Ele não estabelece, no trecho do layout, uma regra normativa de que esses cinco campos tenham obrigatoriamente a geometria de uma barra OHLC clássica. O layout também define TPMERC=030 como TERMO. citeturn1search6turn1search8

Isso é importante: a regra matemática usada na FASE06B era uma invariante analítica criada pelo validador, não uma regra explicitamente documentada no layout B3.

## 3. Evidência externa de comportamento do próprio mercado a termo

Há documentação pública de boletins de mercado contendo linhas T nas quais os campos publicados não obedecem à geometria estrita de uma barra OHLC.

Exemplo publicado em boletim reproduzido pela Gazeta Mercantil em 06/01/2009: ELET3T: abertura 27,36; mínimo 27,35; máximo 27,55; médio 27,55; fechamento 27,27. Nesse registro, o fechamento 27,27 está abaixo do mínimo 27,35. O mesmo boletim contém DURA4T com abertura 14,70; mínimo 14,64; máximo 14,95; médio 15,10; fechamento 14,84 — portanto, o preço médio também está acima do máximo. citeturn5search6

Esse comportamento não prova sozinho a semântica histórica exata de cada campo, mas prova algo suficiente para o gate de qualidade: não é seguro transformar a geometria OHLC convencional em condição universal de validade para TPMERC=030.

## 4. O que foi demonstrado

### FATO
- TPMERC=030 é mercado a termo. citeturn1search6turn1search8
- O layout B3 descreve os campos de preço do papel-mercado, mas não documenta a invariante OHLC convencional como critério de rejeição. citeturn1search6
- Existem publicações de mercado a termo com FECH < MÍN e MÉD > MÁX, demonstrando que essa geometria não pode ser presumida como universal para TERM. citeturn5search6
- Os 29 casos de 1998 permanecem preservados exatamente como foram encontrados; nenhum valor histórico foi alterado.

### HIPÓTESE CONTROLADA
As divergências podem decorrer da metodologia histórica de formação/publicação dos campos de mercado a termo, de convenções específicas do segmento ou de características do processo de consolidação do boletim. Não há evidência suficiente nesta etapa para escolher uma dessas explicações como definitiva.

### NÃO DEMONSTRADO
Ainda não foi demonstrado, para cada um dos 29 registros de 1998, qual evento/negócio originou cada preço. Também não foi obtida uma fonte histórica primária de 1998 que descreva a regra de cálculo de PREMED, PREABE, PREMIN, PREMAX e PREULT especificamente para o termo.

## 5. Decisão de governança

A regra da FASE06B — PREMIN <= PREMED <= PREMAX e PREMIN <= PREULT <= PREMAX — não deve ser usada como bloqueador universal para TPMERC=030.

A FASE06B permanece válida como diagnóstico estatístico: ela mede divergências em relação a uma geometria convencional. Porém, essas divergências não devem ser convertidas automaticamente em corrupção do dado.

Não se altera o RAW, não se altera a NORMALIZED e não se apagam as 29 ocorrências.

## 6. Consequência para a FASE07

A investigação remove o motivo específico de considerar as 29 ocorrências TERM, por si só, como prova de corrupção ou erro de parsing.

A FASE07 pode prosseguir quanto à identidade histórica/chaves, desde que seus próprios gates estejam satisfeitos. A semântica econômica detalhada dos campos TERM deve continuar registrada como pendência de documentação histórica, não como defeito do dado.

## 7. Próxima investigação recomendada

1. procurar documentação histórica Bovespa/BM&F anterior a 2000 sobre formação dos campos do boletim para termo;
2. cruzar uma amostra dos 29 casos com boletins diários históricos, quando disponíveis;
3. verificar TOTNEG, QUATOT, VOLTOT, PRAZOT e DATVEN desses casos para confirmar coerência interna;
4. criar um contrato separado para TPMERC=030, sem reutilizar invariantes de ações à vista;
5. somente promover uma regra de exceção para código depois de obter documentação ou evidência histórica suficiente.

## 8. Fontes consultadas

- B3 — Cotações históricas e descrição do produto: a série contém histórico desde 1986 e inclui preços, tipo de mercado e demais campos. citeturn1search0
- B3 — Layout oficial Cotações Históricas: campos de preço e tabela de TPMERC. citeturn1search6turn1search8
- Gazeta Mercantil — boletim de 06/01/2009, usado apenas como evidência externa de que linhas de mercado a termo publicadas podem não obedecer à geometria OHLC clássica. citeturn5search6

## 9. Estado

FASE06C: CONCLUÍDA — INVESTIGAÇÃO SEMÂNTICA PARCIALMENTE RESOLVIDA

Decisão: remover a interpretação de "violação OHLC = dado inválido" para TPMERC=030, preservando as ocorrências como evidência diagnóstica.

Não autorizado: corrigir valores históricos, preencher campos ou reescrever RAW/NORMALIZED.