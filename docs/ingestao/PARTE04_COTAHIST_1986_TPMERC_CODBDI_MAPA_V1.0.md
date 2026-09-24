# PARTE04 — COTAHIST 1986: MAPA SEMÂNTICO TPMERC × CODBDI V1.0

**Arquivo:** `PARTE04_COTAHIST_1986_TPMERC_CODBDI_MAPA_V1.0.md`  
**Projeto:** B3 — A Bolsa do Brasil  
**Tema:** Reconciliação semântica do COTAHIST 1986  
**Caminho:** `docs/ingestao/PARTE04_COTAHIST_1986_TPMERC_CODBDI_MAPA_V1.0.md`  
**Data de criação:** 24/09/2026  
**Repositório:** `carlos-andrade/B3`

## 1. Objetivo

Formalizar a interpretação dos códigos **TPMERC** e **CODBDI** efetivamente observados no COTAHIST 1986, usando o layout oficial da B3 como fonte normativa do significado dos códigos.

Este documento **não libera 1987**. A liberação continua condicionada aos testes de chave lógica, OHLC, quantidade/volume, calendário e comparação RAW → NORMALIZED.

## 2. Fonte normativa

A B3 documenta que o registro 01 é organizado por tipo de registro, data do pregão, código BDI, código de negociação e demais atributos do papel-mercado. O campo TPMERC identifica o mercado em que o papel está cadastrado. citeturn2view0

O layout oficial também define os campos de preço com duas casas decimais, VOLTOT com duas casas decimais e PTOEXE com seis casas decimais. QUATOT é a quantidade total de títulos negociados. citeturn2view0

## 3. TPMERC observado em 1986

| Código | Significado oficial B3 | Linhas observadas em 1986 | Status |
|---|---|---:|---|
| 010 | VISTA | 96.479 | CONFIRMADO |
| 012 | EXERCÍCIO DE OPÇÕES DE COMPRA | 835 | CONFIRMADO |
| 013 | EXERCÍCIO DE OPÇÕES DE VENDA | 152 | CONFIRMADO |
| 017 | LEILÃO | 99 | CONFIRMADO |
| 020 | FRACIONÁRIO | 36.021 | CONFIRMADO |
| 030 | TERMO | 36.596 | CONFIRMADO |
| 060 | FUTURO COM MOVIMENTAÇÃO CONTÍNUA | 11 | CONFIRMADO |
| 070 | OPÇÕES DE COMPRA | 7.027 | CONFIRMADO |
| 080 | OPÇÕES DE VENDA | 761 | CONFIRMADO |

A tabela oficial da B3 define exatamente esses códigos e significados. O código 050 também existe no layout, mas **não foi observado no inventário de 1986**; portanto não deve ser introduzido artificialmente no dataset. citeturn2view0

## 4. CODBDI observado em 1986

| Código | Significado oficial B3 | Linhas observadas | Status |
|---|---|---:|---|
| 02 | LOTE PADRÃO | 92.653 | CONFIRMADO |
| 06 | CONCORDATÁRIAS | 2.600 | CONFIRMADO |
| 10 | DIREITOS E RECIBOS | 343 | CONFIRMADO |
| 14 | CERT. INVEST./TÍT. DIV. PÚBLICA | 1.222 | CONFIRMADO |
| 38 | EXERCÍCIO DE OPÇÕES DE COMPRA | 835 | CONFIRMADO |
| 42 | EXERCÍCIO DE OPÇÕES DE VENDA | 152 | CONFIRMADO |
| 46 | LEILÃO DE NÃO COTADOS | 28 | CONFIRMADO |
| 50 | LEILÃO | 67 | CONFIRMADO |
| 54 | LEILÃO DE AÇÕES EM MORA | 4 | CONFIRMADO |
| 58 | OUTROS | 238 | CONFIRMADO |
| 62 | MERCADO A TERMO | 36.596 | CONFIRMADO |
| 70 | FUTURO COM RETENÇÃO DE GANHOS | 11 | CONFIRMADO |
| 78 | OPÇÕES DE COMPRA | 7.027 | CONFIRMADO |
| 82 | OPÇÕES DE VENDA | 761 | CONFIRMADO |
| 96 | MERCADO FRACIONÁRIO | 35.444 | CONFIRMADO |

Os significados acima são os constantes da tabela oficial de CODBDI da B3. citeturn2view0

## 5. Matriz observada TPMERC × CODBDI

A combinação observada em 1986 é:

- 010 × 02 = 92.653
- 010 × 06 = 2.600
- 010 × 10 = 343
- 010 × 14 = 645
- 010 × 58 = 238
- 012 × 38 = 835
- 013 × 42 = 152
- 017 × 46 = 28
- 017 × 50 = 67
- 017 × 54 = 4
- 020 × 14 = 577
- 020 × 96 = 35.444
- 030 × 62 = 36.596
- 060 × 70 = 11
- 070 × 78 = 7.027
- 080 × 82 = 761

### Observação importante

As correspondências 012/38, 013/42, 030/62, 060/70, 070/78 e 080/82 mostram forte coerência entre os dois sistemas de classificação. Isso é **evidência de consistência semântica**, não prova suficiente para definir a chave econômica do registro.

## 6. Resultado atual

### Confirmado

1. O layout físico de 245 bytes está alinhado ao layout oficial.
2. Os códigos TPMERC observados têm significado oficial identificável.
3. Os códigos CODBDI observados têm significado oficial identificável.
4. As escalas numéricas usadas na leitura inicial são compatíveis com o layout oficial:
   - preços: 2 casas;
   - VOLTOT: 2 casas;
   - PTOEXE: 6 casas. citeturn2view0
5. O inventário de 1986 contém 248 datas distintas de pregão.

### Ainda NÃO confirmado

- chave lógica econômica definitiva;
- explicação dos 29 casos de inconsistência OHLC;
- regra de tolerância definitiva para VOLTOT × PREMED × QUATOT;
- calendário oficial completo de negociação de 1986;
- equivalência integral de cada registro entre RAW e NORMALIZED.

## 7. Regra de governança

**1987 permanece BLOQUEADO.**

Nenhuma conclusão deste documento autoriza a promoção automática de 1986 para camada NORMALIZED definitiva nem a abertura da ingestão semântica de 1987.

## 8. Próximo teste

O próximo teste obrigatório é a **chave lógica**. Deve comparar, no mínimo:

1. `data_pregao + codneg + tpmerc`
2. `data_pregao + codbdi + codneg + tpmerc`
3. `data_pregao + codbdi + codneg + tpmerc + codisi + dismes`
4. uma chave enriquecida com os campos contratuais relevantes para termo/opções, especialmente `especi`, `prazot`, `datven`, `preexe`, `indopc` e `dismes`.

O objetivo não é apenas encontrar uma combinação sem duplicatas, mas determinar qual chave representa corretamente o **papel-mercado em um determinado pregão**, respeitando instrumentos com características contratuais distintas.

