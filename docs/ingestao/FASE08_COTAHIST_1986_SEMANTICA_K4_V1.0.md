# FASE 08 — Semântica Histórica da Colisão K4 — COTAHIST 1986

**Arquivo:** FASE08_COTAHIST_1986_SEMANTICA_K4_V1.0.md  
**Projeto:** B3 - A BOLSA DO BRASIL  
**Tema:** Semântica histórica da colisão residual K4  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Determinar, com evidência histórica e sem retroprojeção indevida, o significado econômico e cadastral dos campos que formam a colisão K4 de 10/10/1986.

Registro-alvo:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0`

## 2. Evidência RAW

A FASE 07F identificou duas linhas RAW, 140808 e 140809, com a mesma K4 e estatísticas de negociação distintas.

A análise da FASE 08 preserva o RAW e produz somente evidência analítica.

## 3. Evidência documental

O layout oficial B3 define CODBDI como código utilizado para classificar os papéis na emissão do Boletim Diário de Informações e lista **62 = MERCADO A TERMO**. Também define TPMERC como tipo de mercado e lista **030 = TERMO**. O layout define PRAZOT como prazo em dias do mercado a termo. citeturn2search28

O mesmo layout estabelece que CODISI era, antes de 15/05/1995, código interno do papel; portanto, VGORACPP em 1986 não deve ser tratado como ISIN. DIMES é definido como número de distribuição do papel / sequência correspondente ao estado de direito vigente. citeturn0search33

Fontes contemporâneas de imprensa de 1986 também mostram a Vigor negociada como **Vigor PP**, demonstrando que a identificação resumida observada no COTAHIST é compatível com a nomenclatura acionária daquele período. Essa evidência, porém, não decodifica por si só o sufixo C05. citeturn3search0

Uma fonte corporativa posterior registra que Vigor e Leco obtiveram registro como companhias abertas em 1984 e que Vigor realizou uma joint venture com a Arla em 1986. Isso confirma o contexto societário de Vigor em 1986, mas não é prova direta da semântica de VGO 2 ou C05. citeturn3search1

## 4. Leitura dos campos

| Campo | Valor | Leitura atual | Grau |
|---|---|---|---|
| CODBDI | 62 | Mercado a termo | Documentado |
| TPMERC | 030 | Termo | Documentado |
| CODNEG | VGO 2 | Código histórico de negociação observado no RAW | Observado |
| NOMRES | VGOR | Nome resumido observado | Observado |
| CODISI | VGORACPP | Código interno histórico do papel | Validado |
| DIMES | 104 | Distribuição/estado de direito | Documentado, sem reconstrução histórica completa |
| ESPECI | PP *C05 | Especificação histórica; C05 ainda não decodificado | Parcial |
| PRAZOT | 060 | Campo de prazo do termo, 60 dias | Campo documentado |
| DATVEN | 99991231 | Valor-placeholder aparente | Inferência; requer fonte contemporânea |
| FATCOT | 0001000 | Fator de cotação observado | Observado |
| PREEXE | 0 | Sem preço de exercício registrado | Observado |
| INDOPC | 0 | Indicador observado | Observado |
| PTOEXE | 0 | Sem preço/ponto de exercício registrado | Observado |

## 5. Resultado da investigação

A semântica disponível permite afirmar com alta confiança que a ocorrência está associada a **mercado a termo**.

Não permite afirmar ainda:

- que VGO 2 seja simplesmente um ticker atual equivalente a VGOR;
- que C05 represente determinada série ou evento corporativo específico;
- que 99991231 seja formalmente uma data de vencimento “indefinida”;
- que as duas linhas sejam um erro de duplicação;
- que as duas linhas representem dois ativos econômicos diferentes.

## 6. Hipótese de trabalho

A hipótese operacional mais consistente com a evidência atual é:

> as duas linhas pertencem ao mesmo contexto contratual/cadastral segundo a K4, mas representam agregações de negociação distintas publicadas no arquivo histórico.

Esta é **hipótese**, não conclusão histórica.

## 7. Evidência quantitativa

A FASE 08 executa diretamente sobre o COTAHIST_A1986.ZIP e calcula:

- quantidade total de registros tipo 01;
- todos os registros VGO 2;
- todos os registros com CODISI VGORACPP;
- todos os registros com CODNEG VGO 2;
- todos os registros cujo NOMRES contém VGOR;
- frequência de CODBDI 62;
- frequência de TPMERC 030.

Artefato:

`dados/cotahist/quality/COTAHIST_1986_FASE08_SEMANTICA_K4_V1.json`

## 8. Critério de fechamento

A FASE 08 somente poderá ser fechada quando existir evidência histórica suficiente para decodificar, no mínimo:

1. a convenção VGO 2;
2. o significado histórico de C05;
3. a função de DIMES 104 em 1986;
4. o significado de DATVEN 99991231;
5. a regra que permitia duas linhas com a mesma K4 e estatísticas distintas.

Até lá, a FASE 08 permanece **ABERTA — INVESTIGAÇÃO SEMÂNTICA**.

## 9. Governança

Nenhum RAW será alterado.

Nenhuma linha será excluída.

Nenhuma identidade econômica será imposta por conveniência de modelagem.

Toda hipótese permanecerá separada de fato observado e de definição documental.
