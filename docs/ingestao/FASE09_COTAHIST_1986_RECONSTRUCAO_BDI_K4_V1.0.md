# FASE 09 — Reconstrução da relação BDI × COTAHIST × K4

**Arquivo:** FASE09_COTAHIST_1986_RECONSTRUCAO_BDI_K4_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Relação entre publicação histórica do BDI e chave estrutural do COTAHIST na colisão K4 de 10/10/1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 09 inicia a reconstrução formal da relação entre a estrutura publicada no BDI, as dimensões preservadas no COTAHIST, a chave estrutural K4 e a possibilidade de uma dimensão histórica não preservada na K4.

O objetivo é separar dimensão preservada, dimensão publicada mas não preservada e hipótese ainda não demonstrada.

## 2. Registro-alvo

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW: **140808** e **140809**.

A K4 das duas linhas é idêntica. Os agregados são diferentes.

## 3. Base factual consolidada

### 3.1 COTAHIST

A documentação oficial atual da B3 define CODBDI como código de classificação no BDI e identifica 62 como Mercado a Termo. O mesmo conjunto documental define TPMERC 030 como TERMO.

A página oficial de séries históricas informa que o arquivo contém, entre outros elementos, tipo de mercado, especificação, preços, quantidade de negócios e volume negociado.

Fontes de controle documental:
- B3 — Layout do Arquivo de Cotações Históricas, revisão oficial recuperada na FASE 08.
- B3 — página oficial de Cotações Históricas.

### 3.2 Publicação histórica

A evidência contemporânea de 05/06/1986 já recuperada demonstra uma tabela de Mercado a Termo com as dimensões:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

A mesma fonte demonstra que um mesmo emissor/família podia aparecer em múltiplas linhas com o mesmo prazo quando o Tipo era diferente, como nos registros históricos de Mendes Júnior PA/PB/PP 030.

Isso demonstra capacidade histórica de segmentação por Tipo, mas não identifica o Tipo das linhas Vigor 140808/140809.

### 3.3 Janela do evento

A reconstrução RAW de 09/10, 10/10 e 13/10/1986 mostrou:

- 09/10: 1 linha Vigor a termo com prazo 060;
- 10/10: 2 linhas Vigor a termo com prazo 060;
- 13/10: 1 linha Vigor a termo com prazo 060;
- todas com PP *C05 e DIMES 104;
- a duplicidade estrutural ocorre somente em 10/10.

A sequência é **1 → 2 → 1**, sem mudança nos campos estruturais conhecidos da K4.

## 4. Pergunta central

**Quais dimensões da publicação do Mercado a Termo eram potencialmente usadas para separar linhas no BDI, e quais dessas dimensões não estão representadas na K4 do COTAHIST?**

Classificação obrigatória:

- **PRESERVADA:** dimensão explicitamente presente na K4;
- **PUBLICADA_NAO_PRESERVADA:** dimensão demonstrada no BDI sem campo equivalente identificado na K4;
- **NAO_DEMONSTRADA:** hipótese sem evidência documental suficiente.

## 5. Matriz de dimensões

| Dimensão | Evidência | Preservada na K4? | Estado |
|---|---|---:|---|
| Data | COTAHIST | Sim | DOCUMENTADA |
| CODBDI | COTAHIST | Sim | DOCUMENTADA |
| CODNEG | COTAHIST | Sim | DOCUMENTADA |
| TPMERC | COTAHIST | Sim | DOCUMENTADA |
| CODISI | COTAHIST | Sim | DOCUMENTADA |
| DIMES | COTAHIST | Sim | DOCUMENTADA |
| ESPECI | COTAHIST | Sim | DOCUMENTADA |
| PRAZOT | COTAHIST | Sim | DOCUMENTADA |
| DATVEN | COTAHIST | Sim | DOCUMENTADA |
| Tipo histórico do BDI | BDI contemporâneo | Não identificado | POSSÍVEL DIMENSÃO PERDIDA |
| C05 | BDI/imprensa contemporânea | Está dentro de ESPECI | SEMÂNTICA NÃO RESOLVIDA |
| Taxa do termo | Evidência posterior/controle estrutural | Não | NÃO DEMONSTRADA PARA 1986 |
| Comprador/vendedor | Evidência posterior/controle estrutural | Não | NÃO DEMONSTRADA PARA 1986 |
| Comitente | Evidência posterior/controle estrutural | Não | NÃO DEMONSTRADA PARA 1986 |
| Participante/corretora | Evidência posterior/controle estrutural | Não | NÃO DEMONSTRADA PARA 1986 |

## 6. Teste lógico da dimensão perdida

Uma explicação estrutural compatível com a colisão precisa satisfazer simultaneamente:

1. a dimensão separadora existia no processo/publicação histórica;
2. podia gerar linhas distintas com o mesmo prazo;
3. não está codificada em nenhum campo da K4 analisada;
4. é compatível com a ocorrência em 10/10 e a ausência de duplicidade em 09/10 e 13/10;
5. não contradiz os demais registros do período.

Até esta fase, os itens 1 e 2 possuem suporte documental direto para a dimensão Tipo. Os itens 3 e 4 são compatíveis com os dados, mas não demonstram que Tipo foi a dimensão usada no alvo. O item 5 continua aberto.

## 7. Hipóteses concorrentes

### H1 — Tipo histórico não preservado na K4

**Estado:** PLAUSÍVEL / NÃO PROVADA.

O BDI de 1986 demonstra que Tipo podia separar linhas com o mesmo Prazo. Ainda falta o BDI de 10/10/1986 para demonstrar que as duas linhas Vigor tinham Tipos distintos.

### H2 — Outra dimensão operacional não preservada

**Estado:** PLAUSÍVEL / NÃO PROVADA.

Pode ter existido outra dimensão de registro, contraparte, condição contratual ou classificação operacional que não esteja refletida na K4. Não há evidência primária suficiente para especificá-la.

### H3 — Regra histórica de agregação/publicação

**Estado:** HIPÓTESE PRINCIPAL CONCORRENTE.

As duas linhas podem representar agrupamentos publicados separadamente por uma regra histórica que não está reconstruída no layout atual. A sequência 1 → 2 → 1 é compatível com a hipótese, mas não a demonstra.

### H4 — Erro de processamento/publicação

**Estado:** NÃO CONFIRMADO.

As duas linhas apresentam estatísticas internamente coerentes. Isso não prova correção histórica, mas também não sustenta, isoladamente, uma conclusão de erro.

## 8. O que já foi eliminado

- diferença de prazo: **REFUTADA**;
- diferença entre mercado à vista e termo: **REFUTADA**;
- C05 surgindo pela primeira vez no evento: **REFUTADA**;
- DIMES 104 surgindo pela primeira vez no evento: **REFUTADA**;
- perfil estatístico raro como explicação suficiente: **REFUTADA**;
- recorrência do mesmo K4 em outros anos como explicação: **REFUTADA**;
- C05 = Prazo: **REFUTADA**;
- Tipo = Prazo: **REFUTADA**.

## 9. Evidência decisiva ausente

A evidência de maior valor probatório continua sendo uma fonte primária ou reprodução verificável do **BDI de 10/10/1986**, preferencialmente contendo a seção Mercado a Termo e as linhas Vigor.

Para encerrar a causa, a fonte deverá permitir observar:

1. título/código publicado;
2. Tipo de cada linha;
3. Prazo;
4. Quantidade;
5. preços;
6. número de negócios;
7. eventual Volume;
8. cabeçalho da tabela;
9. página/edição/data;
10. proveniência documental.

Sem esses elementos, nenhuma dimensão oculta específica será atribuída às linhas 140808/140809.

## 10. Governança

- RAW permanece **intocado**.
- Linhas 140808 e 140809 permanecem preservadas.
- Nenhum campo histórico é recodificado.
- PP *C05 permanece literal.
- VGO 2 permanece literal.
- DIMES 104 permanece literal.
- DATVEN 99991231 permanece literal.
- Nenhuma linha é removida ou consolidada.
- Nenhuma identidade econômica é inferida.
- Nenhuma causalidade é atribuída ao Tipo.
- Fontes posteriores não são retroprojetadas como regra de 1986.

## 11. Próximo passo controlado

1. Catalogar exemplos de 1986 em que o mesmo título aparece em múltiplas linhas.
2. Identificar pares Tipo × Prazo observáveis.
3. Comparar essas linhas com a representação COTAHIST correspondente.
4. Verificar se alguma dimensão publicada no BDI desaparece sistematicamente na K4.
5. Procurar no COTAHIST 1986 outros padrões de estatísticas múltiplas para a mesma combinação estrutural parcial.
6. Testar se a colisão Vigor é compatível com uma regra geral ou permanece um caso singular.

## 12. Estado

**IMPLEMENTADO:** FASE 09 iniciada e formalizada.  
**EXECUTADO:** matriz BDI × COTAHIST × K4 e hipóteses concorrentes estruturadas.  
**VALIDADO:** separação histórica Tipo × Prazo e preservação dos campos K4 conhecidos.  
**NÃO RESOLVIDO:** dimensão efetivamente responsável pelas duas linhas Vigor e regra histórica de agregação/publicação.

**FASE 09:** ABERTA.
