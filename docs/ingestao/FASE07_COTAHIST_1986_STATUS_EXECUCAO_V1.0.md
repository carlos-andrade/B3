# FASE 07 — COTAHIST 1986 — STATUS DE EXECUÇÃO E EVIDÊNCIA

**Projeto:** B3 — A Bolsa do Brasil  
**Escopo:** Identidade histórica COTAHIST 1986  
**Data:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Estado atual

A FASE 07 foi executada integralmente nas frentes 07A–07G.

**Estado global: FECHADA COM ANOMALIA RESIDUAL K4 DOCUMENTADA.**

O fechamento não significa que a anomalia econômica foi automaticamente resolvida. Significa que a anomalia foi localizada, reproduzida, documentada com linhas RAW e diferenças observáveis, sem alteração do dado original.

## 2. Matriz de execução

| Frente | Tema | Implementação | Execução | Validação |
|---|---|---:|---:|---:|
| 07A | Identidade histórica / K1–K4 | Sim | Sim | VALIDADA |
| 07B | TPMERC | Sim | Sim | VALIDADA |
| 07C | CODBDI | Sim | Sim | VALIDADA |
| 07D | CODISI | Sim | Sim | VALIDADA |
| 07E | DIMES | Sim | Sim | VALIDADA |
| 07F | Colisão K4 | Sim | Sim | VALIDADA — requer revisão semântica |
| 07G | Matriz final de identidade | Sim | Sim | VALIDADA |

## 3. Correção metodológica crítica

Durante a validação independente da colisão K4 foi identificada uma divergência de offsets em versões anteriores dos parsers.

O layout oficial B3 posiciona:

- PREEXE: 189–201;
- INDOPC: 202;
- DATVEN: 203–210;
- FATCOT: 211–217;
- PTOEXE: 218–230;
- CODISI: 231–242;
- DIMES: 243–245.

A correção foi aplicada aos parsers 07A, 07F e 07G.

Fonte oficial utilizada:
SeriesHistoricas_Layout.pdf, B3, Revisão 02, 05/10/2020.

## 4. 07A — Identidade histórica

Evidência:

dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_HISTORICA_V1.json

Resultado:

- 177.981 registros;
- 2.699 CODNEG distintos;
- K1: 172.792 grupos;
- K2: 172.792 grupos;
- K3: 172.793 grupos;
- K4: 177.980 grupos;
- K4 unitários: 177.979;
- K4 repetidos: 1 grupo;
- linhas no grupo K4 repetido: 2.

A chave K4 repetida é:

19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060 | 99991231 | 0 | 0 | 0

O resultado não autoriza inferência automática de identidade econômica definitiva.

## 5. 07F — Colisão K4

Evidência:

dados/cotahist/quality/COTAHIST_1986_COLISAO_K4_V1.json

Workflow validado:

- run: 36038214156;
- conclusão: success;
- commit de publicação da evidência: af2f398;
- evidência gerada em 2026-09-24T18:00:47Z.

Resultado:

- match_count = 2;
- linhas RAW: 140808 e 140809;
- os dois registros possuem o mesmo contexto K4;
- os hashes RAW são diferentes;
- há diferenças em PREAB, PREMAX, PREMIN, PREMED, PREULT, QUATOT, VOLTOT e TOTNEG;
- portanto, não são registros byte-a-byte idênticos;
- não foi inferida identidade econômica automática;
- a anomalia permanece classificada como REQUIRES_SEMANTIC_REVIEW.

Diferenças observadas:

- TOTNEG: 1 vs 4;
- QUATOT: 39.000.000 vs 190.000.000;
- VOLTOT: 7.410.000 vs 35.646.000;
- PREULT: 190 vs 175;
- PREMAX: 190 vs 191;
- PREMIN: 190 vs 165;
- PREMED: 190 vs 187.

Essas diferenças demonstram que as duas linhas carregam estatísticas de negociação distintas apesar da mesma chave K4.

## 6. 07G — Matriz final

Evidência:

dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_FINAL_V1.json

Workflow validado:

- run: 36038470140;
- conclusão: success;
- publicação da evidência: commit 2271f36.

Resultado:

- 177.981 registros;
- K4: 177.980 grupos;
- K4: 177.979 grupos unitários;
- 1 grupo K4 repetido;
- 2 linhas no grupo repetido;
- 2.699 CODNEG distintos;
- 1.817 CODNEG com múltiplos contextos de atributos;
- RAW e NORMALIZED declarados inalterados.

O artefato agora reporta explicitamente:

residual_k4_count = 1

e preserva a chave K4 repetida.

## 7. Integridade

Nenhuma etapa da FASE 07 altera:

- dados/cotahist/raw/;
- os dados normalizados reconciliados;
- os registros históricos originais.

As evidências são artefatos analíticos separados.

## 8. Decisão de fechamento

A FASE 07 pode ser fechada operacionalmente porque:

1. 07E possui evidência independente válida;
2. 07F possui evidência independente válida;
3. a colisão foi reproduzida diretamente no RAW;
4. as duas linhas foram inspecionadas;
5. as diferenças foram preservadas;
6. nenhum registro foi corrigido;
7. a anomalia econômica não foi artificialmente resolvida.

**Conclusão:** FASE 07 FECHADA COM ANOMALIA RESIDUAL K4 DOCUMENTADA.

A próxima fase deve tratar a semântica histórica da anomalia, sem transformar a chave K4 em identidade econômica definitiva sem evidência adicional.
