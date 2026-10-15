# FASE 07 — COTAHIST 1986 — FECHAMENTO DE IDENTIDADE HISTÓRICA

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-57E03D8B7838 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 4a3b0a89f2d30150c851e2ef03a775041b4c67b5079e9a8e91cf49efee257fa0 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Arquivo:** FASE07_COTAHIST_1986_FECHAMENTO_IDENTIDADE_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Tema:** Fechamento auditável da identidade histórica COTAHIST 1986  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Decisão

**FASE 07 FECHADA COM ANOMALIA RESIDUAL K4 DOCUMENTADA.**

A fase foi executada e validada nas frentes 07A, 07B, 07C, 07D, 07E, 07F e 07G.

A expressão “fechada” refere-se ao processo analítico e de evidência. Não significa que a anomalia K4 recebeu uma interpretação econômica definitiva.

## 2. Evidência primária

Arquivo RAW analisado:

dados/cotahist/raw/anual/COTAHIST_A1986.ZIP

Registros tipo 01 analisados:

177.981.

RAW e dados NORMALIZED permaneceram inalterados.

## 3. Correção de layout

A validação contra o layout oficial B3 confirmou os offsets:

| Campo | Posição inicial | Posição final |
|---|---:|---:|
| PREEXE | 189 | 201 |
| INDOPC | 202 | 202 |
| DATVEN | 203 | 210 |
| FATCOT | 211 | 217 |
| PTOEXE | 218 | 230 |
| CODISI | 231 | 242 |
| DIMES | 243 | 245 |

A correção foi aplicada aos parsers 07A, 07F e 07G antes do fechamento.

## 4. Resultado K4

A K4 analítica utilizada foi:

DATA_PREGÃO + CODBDI + CODNEG + TPMERC + CODISI + DIMES + ESPECI + PRAZOT + DATVEN + PREEXE + INDOPC + PTOEXE.

Resultado:

- 177.980 grupos K4;
- 177.979 grupos unitários;
- 1 grupo repetido;
- 2 registros no grupo repetido.

Chave residual:

19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0

## 5. Inspeção independente da colisão

Arquivo:

dados/cotahist/quality/COTAHIST_1986_COLISAO_K4_V1.json

Workflow:

36038214156 — success.

Os dois registros estão nas linhas RAW:

- 140808;
- 140809.

Os hashes SHA-256 são diferentes:

- 04280f94086266d5ea7aebd95eb8ccaf7771a6df3bbb210a189791369642a2e0;
- 1e836a05ad33c4990d319ea85490820c723a666121de89c3ddfc9cea67f7789e.

Diferenças materiais:

| Campo | Registro 140808 | Registro 140809 |
|---|---:|---:|
| TOTNEG | 1 | 4 |
| QUATOT | 39.000.000 | 190.000.000 |
| VOLTOT | 7.410.000 | 35.646.000 |
| PREAB | 190 | 165 |
| PREMAX | 190 | 191 |
| PREMIN | 190 | 165 |
| PREMED | 190 | 187 |
| PREULT | 190 | 175 |

Portanto, os dois registros não são cópias byte-a-byte.

## 6. Interpretação permitida

É permitido afirmar:

1. existem dois registros tipo 01 na mesma data;
2. ambos compartilham o mesmo contexto K4;
3. ambos possuem dados de negociação diferentes;
4. ambos foram preservados no RAW;
5. a ocorrência é uma anomalia de unicidade da chave analítica K4;
6. a causa histórica não foi determinada nesta fase.

Não é permitido afirmar, sem evidência adicional:

- que os registros representam ativos econômicos diferentes;
- que representam o mesmo ativo econômico;
- que um dos registros é erro de origem;
- que um deles deve ser excluído;
- que a diferença é mero ajuste contábil;
- que K4 é identidade econômica definitiva.

## 7. 07G — consolidação

Arquivo:

dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_FINAL_V1.json

Workflow:

36038470140 — success.

Resultado consolidado:

- 177.981 registros;
- 2.699 CODNEG distintos;
- 1 grupo K4 repetido;
- 2 linhas no grupo;
- residual_k4_count = 1;
- RAW unchanged = true;
- normalized unchanged = true;
- no economic identity inferred = true.

## 8. Integridade e governança

Nenhum registro RAW foi corrigido.

Nenhum registro NORMALIZED foi alterado para eliminar a anomalia.

A evidência da anomalia permanece armazenada separadamente dos dados de origem.

A regra de governança permanece:

**anomalia detectada não é sinônimo de correção autorizada.**

## 9. Próxima frente

A próxima frente recomendada é a **FASE 08 — semântica histórica da colisão K4**, começando pela investigação do significado de:

- CODBDI 62;
- TPMERC 030;
- CODNEG VGO 2;
- CODISI VGORACPP;
- DIMES 104;
- ESPECI PP *C05;
- PRAZOT 060;
- DATVEN 99991231;
- FATCOT 0001000;
- PREEXE 0;
- INDOPC 0;
- PTOEXE 0.

A FASE 08 deverá usar documentação histórica contemporânea a 1986 sempre que disponível e não poderá retroprojetar sem validação as definições atuais da B3.

## 10. Regra final

**FASE 07 encerrada operacionalmente. A anomalia K4 permanece aberta semanticamente.**
