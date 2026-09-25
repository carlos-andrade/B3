# FASE 09A — Matriz comparativa de publicação BDI × COTAHIST

**Arquivo:** FASE09A_COTAHIST_1986_MATRIZ_COMPARATIVA_BDI_COTAHIST_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Teste de dimensões publicadas no Mercado a Termo versus dimensões preservadas na K4  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

A FASE 09A executa o primeiro teste comparativo proposto na FASE 09: usar exemplos históricos contemporâneos para identificar dimensões que efetivamente separavam linhas publicadas com o mesmo prazo e verificar se essas dimensões possuem representação explícita na K4 do COTAHIST.

## 2. Evidência contemporânea principal

O Jornal do Brasil de 05/06/1986 apresenta a seção **Mercado a Termo** com o cabeçalho:

**Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°**

Na mesma publicação aparecem exemplos de múltiplas linhas para um mesmo emissor/família com o mesmo prazo:

- Mendes Júnior PA 030;
- Mendes Júnior PB 030;
- Mendes Júnior PP 030.

Também aparecem:

- Eluma PP C-030;
- Eluma PP E--030.

A fonte é contemporânea ao ano investigado e demonstra que a publicação histórica podia distinguir linhas por uma dimensão de **Tipo** sem alterar o **Prazo**. citeturn1search0

## 3. Teste contra a K4

A K4 do evento Vigor é:

`DATA | CODBDI | CODNEG | TPMERC | CODISI | DIMES | ESPECI | PRAZOT`

Para as linhas 140808/140809:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060`

Não existe na K4 um campo explicitamente identificado como **Tipo histórico de publicação**.

Isso produz uma assimetria observável:

| Dimensão | Publicação histórica | K4 |
|---|---|---|
| Tipo | SIM | NÃO IDENTIFICADO |
| Prazo | SIM | SIM — PRAZOT |
| Quantidade | SIM | SIM — QUATOT, fora da K4 |
| Fechamento | SIM | SIM — PREULT, fora da K4 |
| Máximo | SIM | SIM — PREMAX, fora da K4 |
| Mínimo | SIM | SIM — PREMIN, fora da K4 |
| Médio | SIM | SIM — PREMED, fora da K4 |
| Nº negócios | SIM | SIM — TOTNEG, fora da K4 |
| C05 | SIM, na identificação publicada | SIM, incorporado a ESPECI | 
| Tipo histórico específico das linhas Vigor | NÃO RECUPERADO | NÃO |

## 4. Resultado lógico

O exemplo Mendes Júnior demonstra uma propriedade importante:

> **Tipo podia produzir múltiplas linhas com o mesmo Prazo em uma publicação contemporânea de 1986.**

Portanto, Tipo é uma dimensão **capaz** de explicar uma multiplicidade que não seria explicada por PRAZOT.

Mas a inferência seguinte não é permitida:

> Tipo ≠ demonstrado como causa das linhas Vigor.

Para demonstrar isso seriam necessárias as linhas Vigor do BDI de 10/10/1986 ou documentação contemporânea equivalente.

## 5. Novo teste — C05

A mesma edição do Jornal do Brasil registra **Vigor PP C05** em sua publicação de mercado e registra também diversos outros códigos Cxx, como Weg PP C35, Met Duque PP C45 e Brahma OP C15. citeturn1search0

Isso reforça que C05 é uma convenção histórica de identificação/classificação publicada.

Não há, entretanto, legenda suficiente nessa fonte para afirmar:

- C05 = Tipo;
- C05 = prazo;
- C05 = comprador;
- C05 = vendedor;
- C05 = corretora;
- C05 = taxa;
- C05 = comitente.

Portanto, **C05 permanece semanticamente não resolvido**.

## 6. Aplicação ao evento Vigor

A sequência já reconstruída diretamente no RAW é:

`09/10/1986 → 1 linha`

`10/10/1986 → 2 linhas`

`13/10/1986 → 1 linha`

Mantendo:

- VGO 2;
- VGORACPP;
- CODBDI 62;
- TPMERC 030;
- DIMES 104;
- PP *C05;
- PRAZOT 060.

A publicação histórica demonstra que uma dimensão Tipo poderia separar linhas mantendo o mesmo prazo. Isso aumenta a plausibilidade de uma dimensão publicacional não preservada na K4.

Não demonstra, contudo, que essa dimensão estava diferente nas duas linhas Vigor.

## 7. Classificação da evidência

| Hipótese | Resultado FASE 09A |
|---|---|
| Tipo pode separar linhas com mesmo Prazo | **DOCUMENTADO** |
| Tipo é o campo que separou Vigor 140808/140809 | **NÃO DEMONSTRADO** |
| C05 é Tipo | **NÃO DEMONSTRADO** |
| C05 é Prazo | **REFUTADO** |
| Prazo explica sozinho a colisão | **REFUTADO** |
| Existe dimensão histórica publicada além da K4 | **GANHA SUPORTE** |
| Dimensão perdida é necessariamente Tipo | **NÃO DEMONSTRADO** |
| Regra de agregação/publicação explica a colisão | **AINDA NÃO DEMONSTRADO** |

## 8. Conclusão

A FASE 09A produz um avanço documental real:

**A publicação contemporânea de 1986 prova que Tipo era uma dimensão operacional/publicacional capaz de gerar linhas distintas para o mesmo prazo.**

Isso torna tecnicamente plausível que a K4 atual tenha perdido uma dimensão histórica relevante.

Porém, ainda não existe evidência suficiente para afirmar que:

`Tipo = causa da colisão Vigor`

A investigação permanece governada pelo princípio de não retroprojeção.

## 9. Próxima ação

A próxima etapa deve procurar no próprio universo COTAHIST 1986 padrões em que:

1. o mesmo CODNEG aparece em múltiplas linhas de termo;
2. o PRAZOT permanece igual;
3. ESPECI ou outros campos mudam;
4. os agregados estatísticos se dividem;
5. a divisão possa ser comparada com exemplos históricos de Tipo.

Esse teste poderá indicar se a colisão Vigor é compatível com um padrão recorrente ou se continua sendo um caso singular.

## 10. Governança

- RAW intocado.
- Nenhuma linha removida.
- Nenhuma consolidação.
- Nenhuma tradução de C05.
- Nenhum Tipo atribuído às linhas Vigor.
- Nenhuma causa econômica inferida.

**Status:** IMPLEMENTADO / EXECUTADO / VALIDADO quanto à evidência histórica de multiplicidade por Tipo com mesmo Prazo.  
**NÃO RESOLVIDO:** dimensão efetiva responsável pela colisão Vigor.
