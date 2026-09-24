# FASE 07 — IDENTIDADE HISTÓRICA DO COTAHIST 1986 V1.0

**Arquivo:** `FASE07_COTAHIST_1986_IDENTIDADE_HISTORICA_V1.0.md`  
**Projeto:** B3 — A Bolsa do Brasil  
**Tema:** Identidade histórica, reutilização de CODNEG e chaves candidatas  
**Caminho:** `docs/ingestao/FASE07_COTAHIST_1986_IDENTIDADE_HISTORICA_V1.0.md`  
**Data de criação:** 24/09/2026  
**Repositório:** `carlos-andrade/B3`

## 1. Objetivo

A FASE 07 transforma a reconciliação semântica inicial de 1986 em um teste formal de **identidade histórica**.

O objetivo não é encontrar uma chave que simplesmente elimine duplicidades. O objetivo é verificar quais atributos, combinados com a dimensão temporal, distinguem corretamente registros de **papel-mercado/instrumento** e quais atributos podem mudar ou ser reutilizados.

## 2. Princípio fundamental

**CODNEG isoladamente não é uma chave histórica suficiente.**

A análise deve considerar, no mínimo:

- DATA_PREGÃO;
- CODNEG;
- TPMERC;
- CODBDI;
- CODISI;
- DIMES.

Para instrumentos contratuais, a chave enriquecida também considera:

- ESPECI;
- PRAZOT;
- DATVEN;
- PREEXE;
- INDOPC;
- PTOEXE.

Uma chave candidata somente será promovida após evidência de unicidade, estabilidade semântica e coerência econômica.

## 3. Chaves testadas

### K1
`DATA_PREGÃO + CODNEG + TPMERC`

Serve como teste mínimo de reutilização de código dentro do pregão e mercado.

### K2
`DATA_PREGÃO + CODBDI + CODNEG + TPMERC`

Adiciona a classificação BDI.

### K3
`DATA_PREGÃO + CODBDI + CODNEG + TPMERC + CODISI + DIMES`

É a chave candidata operacional de identidade observacional, sem assumir ainda equivalência econômica.

### K4 — contratual
`DATA_PREGÃO + CODBDI + CODNEG + TPMERC + CODISI + DIMES + ESPECI + PRAZOT + DATVEN + PREEXE + INDOPC + PTOEXE`

É a chave de investigação para instrumentos cujo contrato pode distinguir séries com mesmo CODNEG.

## 4. O que será medido

Para cada chave:

1. número total de grupos;
2. grupos unitários;
3. grupos repetidos;
4. número de linhas pertencentes a grupos repetidos;
5. tamanho máximo de grupo repetido;
6. exemplos auditáveis das repetições.

Separadamente, para CODNEG:

1. quantidade de códigos distintos;
2. número de datas de aparição;
3. alterações de TPMERC;
4. alterações de CODBDI;
5. alterações de CODISI;
6. alterações de DIMES;
7. alterações de ESPECI.

## 5. Interpretação

### Evidência forte

- chave única dentro do universo analisado;
- atributos contratuais coerentes;
- continuidade temporal explicável;
- ausência de colisões semanticamente distintas.

### Evidência de alerta

- mesmo CODNEG associado a múltiplos TPMERC;
- mesmo CODNEG associado a múltiplos CODBDI;
- mudanças de CODISI;
- mudanças de DIMES;
- mudanças contratuais em ESPECI/PRAZOT/DATVEN/PREEXE/INDOPC/PTOEXE.

**Alerta não significa erro.** Pode representar mudança legítima do instrumento, evento corporativo, exercício, vencimento, migração de classificação ou reutilização histórica do código.

## 6. Regra específica para CODISI

CODISI será tratado como atributo de identidade forte, mas não como prova isolada de continuidade econômica.

O fato de dois registros compartilharem CODISI não autoriza concluir que todos os demais atributos representam o mesmo instrumento.

## 7. Regra específica para DIMES

DIMES será preservado como atributo histórico bruto/normalizado e investigado em conjunto com ESPECI e os demais campos contratuais.

Não será convertido em significado econômico definitivo sem documentação suficiente.

## 8. Saída auditável

O script `scripts/ingestao/analisar_identidade_historica_cotahist_1986_v1.py` gera:

`dados/cotahist/quality/COTAHIST_1986_IDENTIDADE_HISTORICA_V1.json`

A saída contém as métricas das quatro chaves, exemplos de colisões e análise de reutilização de CODNEG.

## 9. Governança

- RAW permanece imutável.
- NORMALIZED permanece imutável.
- Nenhum código recebe significado novo por inferência estatística isolada.
- Nenhuma chave é promovida por conveniência técnica.
- 1987 continua bloqueado até a aprovação das evidências de 1986.
- Toda mudança de interpretação deve gerar nova versão documental.

## 10. Critério de encerramento da FASE 07

A FASE 07 só poderá ser marcada como **CONCLUÍDA** quando:

- K1–K4 tiverem métricas executadas;
- colisões relevantes forem classificadas;
- reutilizações de CODNEG forem explicadas ou explicitamente marcadas como pendentes;
- CODISI e DIMES forem confrontados com atributos contratuais;
- uma chave observacional e uma chave econômica provisória forem documentadas;
- não houver alteração silenciosa de RAW/NORMALIZED.

**Status inicial:** EM EXECUÇÃO.
