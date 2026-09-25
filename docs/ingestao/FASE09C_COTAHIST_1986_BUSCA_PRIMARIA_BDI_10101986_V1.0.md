# FASE 09C — Busca Primária do BDI de 10/10/1986 — V1.0

**Arquivo:** FASE09C_COTAHIST_1986_BUSCA_PRIMARIA_BDI_10101986_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Recuperação da fonte primária para explicar a colisão K4 Vigor/VGO 2 de 10/10/1986  
**Data:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Continuar a FASE 09C com foco exclusivo na recuperação documental do **Boletim Diário de Informações (BDI) da Bovespa do pregão de 10/10/1986**, sem alterar o RAW e sem resolver a colisão K4 por inferência.

## 2. Alvo exato

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

Linhas RAW:

- 140808
- 140809

A investigação procura uma dimensão de publicação/agregação existente no BDI e ausente da K4 atualmente preservada.

## 3. Busca pública executada em 25/09/2026

Foram pesquisadas combinações direcionadas de:

- BDI;
- Boletim Diário de Informações;
- Bovespa;
- 10/10/1986;
- Vigor;
- VGO 2;
- C05;
- Mercado a Termo;
- PDF;
- arquivos históricos.

Também foi pesquisada a possibilidade de nomenclatura de arquivo baseada em data.

### Resultado

**O exemplar primário do BDI de 10/10/1986 não foi localizado nas fontes públicas indexadas pesquisadas.**

Isso significa apenas **não localizado nesta busca**. Não significa que o documento não exista.

## 4. Nova evidência relevante

Foi localizada uma edição do Jornal do Brasil de 05/06/1986 contendo tabela histórica do mercado a termo da Bovespa.

A publicação apresenta dimensões:

`Tipo | Prazo | Quant | Fech | Máx | Mín | Méd | N°`

e contém a identificação:

`Vigor PP C05`

A mesma tabela contém outros códigos Cxx, incluindo exemplos como C03, C15, C26, C30, C34, C35, C45 e C59.

**FATO VALIDADO:** a nomenclatura Cxx e a identificação Vigor PP C05 eram utilizadas em publicação de mercado antes de outubro de 1986.

**NÃO VALIDADO:** C05 ser necessariamente o campo Tipo, ou ser a dimensão responsável pela colisão K4.

Fonte pública:
Jornal do Brasil, 05/06/1986.

## 5. Evidência estrutural do COTAHIST

A documentação pública do layout COTAHIST descreve:

- CODBDI como código utilizado para classificar os papéis na emissão do BDI;
- TPMERC como tipo de mercado;
- ESPECI como especificação do papel;
- PRAZOT como prazo em dias do mercado a termo.

Isso reforça que o COTAHIST contém uma representação estruturada relacionada ao BDI, mas não deve ser presumido como uma cópia integral de todas as dimensões editoriais do boletim.

Fonte pública consultada: documentação do layout COTAHIST.

## 6. Evidência institucional posterior

Manuais posteriores da Bovespa/B3 documentam a divulgação no BDI de informações do Mercado a Termo e mencionam diferentes tipos de termo.

Essa evidência é útil para compreender a função institucional do BDI, mas **não será retroprojetada como prova da regra vigente em 1986**.

Portanto:

- evidência posterior = contexto;
- evidência contemporânea = prova histórica potencial;
- BDI de 10/10/1986 = documento decisivo ainda não recuperado.

## 7. Nova conclusão operacional

A busca atual não encerra a FASE 09C.

Ela estabelece quatro pontos:

1. o BDI era uma fonte institucional de informação de mercado;
2. a documentação pública do COTAHIST relaciona CODBDI à emissão do BDI;
3. a publicação contemporânea de junho de 1986 demonstra dimensões de publicação do mercado a termo além da K4;
4. a fonte primária de 10/10/1986 continua ausente.

## 8. Hipóteses

| Hipótese | Estado |
|---|---|
| H1 — Tipo é dimensão ausente | PLAUSÍVEL / NÃO PROVADA |
| H2 — taxa/preço é dimensão ausente | NÃO PROVADA |
| H3 — participante/comitente/posição | NÃO PROVADA |
| H4 — regra histórica de agregação do BDI | PLAUSÍVEL / NÃO PROVADA |
| H5 — erro de processamento/publicação | NÃO PROVADA |

Nenhuma hipótese é promovida a conclusão.

## 9. Governança

- RAW: **INTACTO**
- Linhas 140808/140809: **PRESERVADAS**
- Consolidação: **PROIBIDA**
- Correção manual: **PROIBIDA**
- C05 reinterpretado: **NÃO**
- Causa da colisão: **NÃO DETERMINADA**

## 10. Próxima ação

A próxima ação controlada é a **recuperação institucional/arquivística** do BDI:

1. BDI de 10/10/1986;
2. BDI de 09/10/1986;
3. BDI de 13/10/1986;
4. legenda de Tipo/Cxx;
5. manual/regulamento Bovespa vigente em 1986;
6. documentação operacional do Mercado a Termo vigente em 1986.

Quando a fonte for recuperada, a análise deverá extrair literalmente a tabela, cabeçalhos, notas e qualquer dimensão adicional.

**STATUS DA FASE 09C: ABERTA — CAUSA HISTÓRICA NÃO RESOLVIDA.**
