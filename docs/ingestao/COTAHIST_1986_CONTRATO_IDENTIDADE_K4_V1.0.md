# COTAHIST 1986 — Contrato de Identidade e Colisão K4

**Arquivo:** COTAHIST_1986_CONTRATO_IDENTIDADE_K4_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Tema:** Reconciliação semântica / identidade lógica dos registros COTAHIST  
**Caminho:** docs/ingestao/COTAHIST_1986_CONTRATO_IDENTIDADE_K4_V1.0.md  
**Data de criação:** 24/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Formalizar, com base no RAW COTAHIST 1986 auditado, a diferença entre identidade contratual, identidade física do registro e observação econômica.

## 2. Evidência auditada

Fonte: `dados/cotahist/raw/anual/COTAHIST_A1986.ZIP`.

Resultado: `dados/cotahist/quality/COTAHIST_1986_AUDITORIA_CHAVES_V2.json`, schema 2.1.0.

- Registros tipo 01: **177.981**
- K1: 172.792 chaves distintas; 5.182 grupos repetidos; máximo 3 ocorrências.
- K2: 172.792 chaves distintas; 5.182 grupos repetidos; máximo 3 ocorrências.
- K3: 172.793 chaves distintas; 5.181 grupos repetidos; máximo 3 ocorrências.
- K4 contratual: 177.980 chaves distintas; **1 grupo repetido**; máximo 2 ocorrências.

K4 é:

`data_pregao + codbdi + codneg + tpmerc + especi + prazot + datven + preexe + indopc + codisi + dismes`

## 3. Colisão K4

Única colisão:

`19861010 | 62 | VGO 2 | 030 | PP *C05 | 060 | 99991231 | 0 | 0 | VGORACPP | 104`

As duas linhas são fisicamente distintas:

- linha RAW **140808**, SHA-256 `04280f94086266d5ea7aebd95eb8ccaf7771a6df3bbb210a189791369642a2e0`;
- linha RAW **140809**, SHA-256 `1e836a05ad33c4990d319ea85490820c723a666121de89c3ddfc9cea67f7789e`.

Elas também apresentam conteúdo econômico diferente. Entre outros campos:

| Campo | Linha 140808 | Linha 140809 |
|---|---:|---:|
| PREABE | 1,90 | 1,65 |
| PREMAX | 1,90 | 1,91 |
| PREMIN | 1,90 | 1,65 |
| PREMED | 1,90 | 1,87 |
| PREULT | 1,90 | 1,75 |
| TOTNEG | 1 | 4 |
| QUATOT | 39.000.000 | 190.000.000 |
| VOLTOT | 74.100 | 356.460 |

**Conclusão:** a colisão não é duplicidade física idêntica. K4 identifica o contrato/instrumento, mas não garante unicidade da observação econômica.

## 4. Contrato de identidade

### 4.1 RAW

O RAW é a camada de preservação da fonte. Nenhuma linha deve ser eliminada para satisfazer unicidade lógica.

A identidade física deve preservar, no mínimo:

- arquivo RAW;
- número da linha no arquivo;
- SHA-256 da linha RAW;
- campos originalmente presentes.

### 4.2 Instrumento/contrato

K4 deve ser tratado como **chave contratual/instrumental**, não como chave primária universal das observações.

### 4.3 Observação econômica

Uma observação econômica diária deve permanecer identificável separadamente do contrato. O COTAHIST 1986 demonstra que preço, negócios, quantidade e volume podem variar dentro da mesma K4 na mesma data.

## 5. Política de duplicidade

1. **Não deduplicar o RAW.**
2. **Não descartar linhas por colisão K4.**
3. Classificar K4 repetida como **colisão contratual / múltiplas observações econômicas**, até que a semântica completa da fonte determine a causa.
4. Qualquer deduplicação na camada NORMALIZED exige regra explícita, evidência e teste.
5. Uma linha só pode ser considerada duplicata física quando seus campos relevantes e sua representação RAW forem comprovadamente equivalentes.
6. Transformações devem ser rastreáveis do NORMALIZED ao RAW.

## 6. Decisão de engenharia

**K4 não será adotada como chave primária única do COTAHIST.**

Ela será mantida como identificador contratual. A arquitetura deverá separar:

`RAW identity → Contract identity (K4) → Economic observation identity`

Essa decisão evita perda silenciosa de dados históricos.

## 7. Estado

**1986 — chave contratual: FECHADA COM RESSALVA SEMÂNTICA.**

A unicidade de K4 foi auditada. A colisão foi explicada como duas observações econômicas distintas do mesmo contrato. Ainda permanecem as frentes de reconciliação de calendário, volume × quantidade, RAW × NORMALIZED e classificação das anomalias OHLC.

## 8. Auditoria e rastreabilidade

- Auditoria: `COTAHIST 1986 - Auditoria de Chaves Logicas V2`
- Script: `scripts/ingestao/auditar_chaves_logicas_cotahist_1986_v2.py`
- Schema do resultado: **2.1.0**
- Commit de correção do auditor: `62e62768ab01140fa237fd03acf6e13405050c1e`
- Commit de correção de persistência CI: `4e8c64bc9c73d86c81bdb76c6a804ba679018d84`
- Execução anterior de referência: `36014139135` (falha na persistência Git, não na análise dos dados).

