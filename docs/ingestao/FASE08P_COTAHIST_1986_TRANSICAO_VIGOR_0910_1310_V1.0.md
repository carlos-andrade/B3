# FASE 08P — COTAHIST 1986: Transição Vigor 09/10 → 10/10 → 13/10/1986

**Arquivo:** FASE08P_COTAHIST_1986_TRANSICAO_VIGOR_0910_1310_V1.0.md  
**Projeto:** B3 — Bolsa do Brasil  
**Fase:** 08P  
**Tema:** reconstrução interna do comportamento de VGO 2 / VGORACPP em 09/10, 10/10 e 13/10/1986  
**Caminho:** `docs/ingestao/FASE08P_COTAHIST_1986_TRANSICAO_VIGOR_0910_1310_V1.0.md`  
**Data de criação:** 25/09/2026  
**Repositório:** `carlos-andrade/B3`

## 1. Objetivo

Verificar, diretamente no RAW preservado do COTAHIST_A1986.ZIP, se a colisão K4 observada em 10/10/1986 é um evento isolado ou parte de uma transição estrutural nos pregões imediatamente anterior e posterior.

Janela analisada:

- 09/10/1986
- 10/10/1986
- 13/10/1986

Escopo:

- CODNEG = `VGO 2`
- CODISI = `VGORACPP`

## 2. Fonte e integridade

**RAW:** `dados/cotahist/raw/anual/COTAHIST_A1986.ZIP`

**SHA-256 do RAW:**

`350e6086c8f991484832ca3cd23e900b692769bfd3311017800231fd896c8018`

O RAW não foi alterado.

## 3. Método

O parser lê os registros tipo 01 em largura fixa e preserva separadamente:

- data;
- CODBDI;
- CODNEG;
- TPMERC;
- ESPECI;
- PRAZOT;
- CODISI;
- DIMES;
- PREAB, PREMAX, PREMIN, PREMED, PREULT;
- TOTNEG;
- QUATOT;
- VOLTOT;
- FATCOT.

Os campos estatísticos utilizam o mesmo mapa de posições fixas validado na FASE 08F:

- TOTNEG: posições 148–152;
- QUATOT: 153–170;
- VOLTOT: 171–188;
- FATCOT: 211–217.

A comparação estrutural agrupa por:

`DATA + CODBDI + CODNEG + TPMERC + CODISI + DIMES + ESPECI + PRAZOT`

sem usar os campos estatísticos como parte da chave.

## 4. Resultado bruto da janela

Foram encontrados **7 registros relevantes**:

| Data | Registros VGO 2 | Termo 060 | Spot |
|---|---:|---:|---:|
| 09/10/1986 | 2 | 1 | 1 |
| 10/10/1986 | 3 | 2 | 1 |
| 13/10/1986 | 2 | 1 | 1 |

Em todos os 7 registros:

- ESPECI = `PP *C05`;
- DIMES = `104`;
- o registro a termo possui PRAZOT = `060`.

## 5. Colisão de 10/10/1986

A colisão permanece exatamente localizada em:

`19861010 | 62 | VGO 2 | 030 | VGORACPP | 104 | PP *C05 | 060`

Linhas RAW:

- **140808**
- **140809**

### Linha 140808

- TOTNEG = 1
- QUATOT = 39.000.000
- VOLTOT = 74.100,00
- PREAB = PREMAX = PREMIN = PREMED = PREULT = 1,90
- FATCOT = 1.000

### Linha 140809

- TOTNEG = 4
- QUATOT = 190.000.000
- VOLTOT = 356.460,00
- PREAB = 1,65
- PREMIN = 1,65
- PREMED = 1,87
- PREMAX = 1,91
- PREULT = 1,75
- FATCOT = 1.000

As duas linhas possuem a mesma chave estrutural, mas agregados estatísticos distintos.

## 6. Comparação temporal

### 09/10/1986

Existe uma única linha VGO 2 a termo com:

- TPMERC = 030;
- PRAZOT = 060;
- ESPECI = PP *C05;
- DIMES = 104.

Não há duplicidade estrutural equivalente.

### 10/10/1986

Existem duas linhas a termo com exatamente a mesma chave estrutural.

A colisão ocorre neste pregão.

### 13/10/1986

Volta a existir uma única linha VGO 2 a termo com:

- TPMERC = 030;
- PRAZOT = 060;
- ESPECI = PP *C05;
- DIMES = 104.

Não há nova duplicidade estrutural equivalente.

## 7. FATO

1. A colisão é **intra-dia** e ocorre somente em 10/10/1986 nesta janela de três pregões.
2. 09/10 possui uma única linha estruturalmente correspondente.
3. 13/10 possui uma única linha estruturalmente correspondente.
4. A estrutura cadastral observada não muda entre 09/10, 10/10 e 13/10 para a linha a termo: C05, DIMES 104 e PRAZOT 060 permanecem presentes.
5. A duplicidade de 10/10 não pode ser explicada, dentro desta janela, por mudança de PRAZOT, ESPECI, DIMES, CODBDI, TPMERC, CODNEG ou CODISI.
6. Os dois registros de 10/10 são preservados no RAW e não foram consolidados.

## 8. PADRÃO

O padrão observado é:

`1 linha → 2 linhas → 1 linha`

para a mesma combinação estrutural VGO 2 / termo 060 / C05 / DIMES 104.

Isso reforça que a duplicidade é um evento pontual de publicação/agregação ou de alguma dimensão operacional não representada na chave K4.

## 9. HIPÓTESE

A hipótese de trabalho permanece:

> Em 10/10/1986 houve uma dimensão de negociação/agregação ou uma regra histórica de publicação que produziu duas linhas estatísticas para a mesma chave estrutural preservada no COTAHIST.

Essa formulação é uma **hipótese**, não uma identificação causal.

A FASE 08P não encontrou evidência suficiente para determinar se a dimensão ausente estava relacionada a Tipo, contraparte/comitente, corretora, taxa ou outra regra operacional.

## 10. Hipóteses que não foram demonstradas

Não foi demonstrado que a colisão seja causada por:

- mudança de vencimento;
- primeira ocorrência de C05;
- primeira ocorrência de DIMES 104;
- diferença entre mercado à vista e a termo;
- erro de cálculo estatístico;
- Tipo específico;
- taxa de operação;
- comprador/vendedor;
- corretora;
- comitente.

## 11. EVIDÊNCIA AUSENTE

Continua ausente uma fonte histórica primária ou suficientemente próxima de 10/10/1986 que revele a regra exata usada para separar ou agregar as duas linhas.

Especialmente relevantes:

- BDI de 09/10/1986;
- BDI de 10/10/1986;
- BDI de 13/10/1986;
- manual operacional Bovespa vigente em outubro de 1986;
- legenda oficial dos códigos Tipo;
- regra histórica de agregação do Mercado a Termo no COTAHIST/BDI.

## 12. Governança dos dados

- RAW alterado: **NÃO**
- Linhas RAW removidas: **NÃO**
- Linhas consolidadas: **NÃO**
- C05 convertido semanticamente: **NÃO**
- Tipo inferido a partir de C05: **NÃO**
- Identidade econômica inferida: **NÃO**
- Causa histórica inferida como fato: **NÃO**

## 13. Status

**IMPLEMENTADO:** parser e workflow da FASE 08P.

**EXECUTADO:** análise da janela 09/10 → 10/10 → 13/10/1986 e publicação da evidência corrigida.

**VALIDADO:** evidência publicada contém o mapa correto de campos e confirma 7 registros, 2 linhas-alvo e 1 grupo de colisão estrutural.

**NÃO RESOLVIDO:** causa histórica/operacional da colisão K4.

## 14. Próxima frente

A investigação deve avançar para a reconstrução documental do **BDI de 10/10/1986 e da regra de publicação do Mercado a Termo**, procurando uma fonte que permita distinguir:

1. Tipo;
2. prazo;
3. taxa;
4. comitente;
5. corretora/intermediário;
6. comprador/vendedor;
7. outras dimensões operacionais.

O objetivo da próxima fase é transformar a hipótese de “dimensão não preservada ou regra histórica de agregação” em uma regra documentalmente demonstrada, ou rejeitá-la.

