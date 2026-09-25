# FASE 10 — COTAHIST 1987 — Plano de Execução e Critérios de Fechamento V1.0

**Arquivo:** FASE10_COTAHIST_1987_PLANO_V1.0.md  
**Projeto:** B3 — A Bolsa do Brasil  
**Caminho:** docs/ingestao/FASE10_COTAHIST_1987_PLANO_V1.0.md  
**Data de criação:** 25/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Iniciar a validação auditável do COTAHIST 1987, usando o RAW preservado como fonte primária e reaproveitando a infraestrutura criada em 1986 sem repetir investigações históricas que não sejam necessárias para a integridade do dataset.

## 2. Estado inicial verificado

- RAW: `dados/cotahist/raw/anual/COTAHIST_A1987.ZIP` presente.
- Manifesto RAW: `dados/cotahist/manifests/COTAHIST_A1987.json`.
- SHA-256 RAW: `16db2bbda8cf770ad177af762c6e651422dee7b1dc7a62ea75fa10e5760f517d`.
- Evidência de normalização existente: `dados/cotahist/normalized/manifests/COTAHIST_A1987_quality.json`.
- A evidência registra parser 1.1.0, 130.665 linhas normalizadas, 25 campos, primeira data 1987-01-02 e última 1987-12-30.
- Auditoria existente registra 230 grupos duplicados pela chave candidata `data_pregao+codbdi+codneg+tpmerc+dismes`, todos com linhas completas diferentes; `prazot` diferencia os dois registros nos exemplos auditados.
- O CSV normalizado anual não está atualmente versionado em `dados/cotahist/normalized/anual/`; portanto, a primeira tarefa não é assumir que o dataset normalizado está disponível, mas reconciliar a evidência/manifests com o artefato efetivamente publicado.

## 3. Princípio de trabalho

1987 será tratado como ano independente. A exceção histórica de 1986 não será usada para presumir defeitos em 1987.

A regra é:

**RAW → reprodução da normalização → auditoria estrutural → auditoria semântica → reconciliação → certificação.**

Nenhum registro será descartado, consolidado ou corrigido sem evidência objetiva e regra documentada.

## 4. Frente 10A — Reconciliação do artefato normalizado

1. Confirmar SHA-256 do RAW.
2. Reexecutar o parser oficial sobre o ZIP 1987.
3. Recalcular SHA-256 do CSV.
4. Comparar com `COTAHIST_A1987.csv.sha256` e com `COTAHIST_A1987_quality.json`.
5. Confirmar contagem de registros, datas e campos.
6. Determinar por que o CSV não está versionado em `normalized/anual` e preservar o resultado de forma reproduzível.

## 5. Frente 10B — Estrutura e calendário

Validar:

- registros 01;
- integridade dos 245 bytes;
- intervalo temporal;
- datas inválidas;
- datas fora de 1987;
- continuidade e dias de negociação;
- consistência entre RAW e normalizado.

## 6. Frente 10C — Semântica mínima

Validar empiricamente, sem extrapolação:

- TPMERC;
- CODBDI;
- ESPECI;
- PRAZOT;
- DIMES;
- CODISI;
- comportamento dos contratos a termo.

A presença de múltiplos registros para a mesma chave parcial não será classificada automaticamente como erro. Primeiro será verificado se a dimensão omitida da chave candidata explica a multiplicidade.

## 7. Frente 10D — Duplicidades

A auditoria deve separar:

1. duplicidade física/identical row;
2. multiplicidade legítima de instrumentos/condições;
3. colisão de chave candidata;
4. divergência de campos econômicos.

O resultado deve informar quantidades, exemplos e regra de interpretação.

## 8. Frente 10E — Qualidade quantitativa

Validar, no mínimo:

- preços;
- quantidade;
- volume;
- negócios;
- fatores de cotação;
- preço de exercício;
- consistência aritmética quando aplicável;
- extremos e outliers para investigação, sem correção automática.

## 9. Critério de fechamento

A FASE 10 só será considerada fechada quando houver:

- RAW preservado e identificado por SHA-256;
- normalização reproduzível;
- manifesto de qualidade;
- auditoria de duplicidades/multiplicidade;
- reconciliação RAW → normalizado;
- registro explícito de exceções;
- decisão de qualidade do ano.

## 10. Regra de governança

Não transformar uma anomalia em “erro” sem evidência. Não transformar uma hipótese semântica em dado oficial. Toda exceção deve ser documentada e rastreável.

**Status:** INICIADA — FRENTE 10A PRIORITÁRIA.
