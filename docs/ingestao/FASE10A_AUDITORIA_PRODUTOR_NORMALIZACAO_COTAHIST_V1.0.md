# FASE 10A — AUDITORIA DO PRODUTOR DE NORMALIZAÇÃO COTAHIST V1.0

**Projeto:** B3 — A Bolsa do Brasil  
**Escopo:** COTAHIST 1986–2026  
**Data:** 2026-09-28  
**Status:** AUDITORIA CONCLUÍDA — POLÍTICA DE PERSISTÊNCIA ANUAL PENDENTE

## 1. Objetivo

Rastrear a origem dos CSVs NORMALIZED anuais, identificar onde são produzidos, onde são persistidos, qual é sua retenção e verificar o consumo pelo Dataset Oficial e pelos dashboards.

Esta auditoria não altera RAW, NORMALIZED, manifests, certificações ou Dataset Oficial.

## 2. Evidências verificadas

### 2.1 Produtor anual

Arquivo:

`scripts/ingestao/normalize_cotahist.py`

Versão do parser:

`PARSER_VERSION = 1.1.0`

O script recebe ZIP RAW e caminho de saída CSV por argumento:

`--zip` + `--output`

Portanto, a normalização é determinística a partir do RAW preservado e do parser versionado.

### 2.2 Workflow anual

Arquivo:

`.github/workflows/cotahist-normalizacao-controlada-v7.yml`

O workflow:

1. recebe o ano por `workflow_dispatch`;
2. lê `dados/cotahist/raw/anual/COTAHIST_A{ano}.ZIP`;
3. gera o CSV em `/tmp/normalized/COTAHIST_A{ano}.csv`;
4. calcula SHA-256 do CSV;
5. executa `validar_normalized.py`;
6. copia apenas o relatório de qualidade e o SHA para `dados/cotahist/normalized/manifests/`;
7. publica CSV, JSON e SHA como artefatos GitHub Actions;
8. os artefatos possuem retenção de 30 dias.

**Conclusão:** o CSV anual NORMALIZED é atualmente um artefato de execução, não um arquivo persistido permanentemente no Git.

### 2.3 Ausência da camada anual persistida

A pasta:

`dados/cotahist/normalized/anual/`

existe, porém não contém os CSVs anuais.

A auditoria anterior identificou 0/41 CSVs anuais persistidos para 1986–2026.

Isso explica por que a lacuna é sistêmica e não específica de 1987.

### 2.4 Fluxo diário

Arquivo:

`.github/workflows/cotahist-importacao-diaria-v1.yml`

O importador diário:

`scripts/ingestao/importar_cotahist_diario_v1.py`

gera NORMALIZED diretamente em:

`dados/cotahist/normalized/diario/`

e o workflow executa:

`git add dados/cotahist/raw/diario dados/cotahist/normalized/diario ...`

Logo, o comportamento diário é diferente do comportamento anual: os CSVs diários são persistidos no repositório.

### 2.5 Dataset Oficial

O gerador do Dataset Oficial referencia arquivos NORMALIZED anuais, mas a cadeia anual atual não garante que esses arquivos existam fisicamente.

Consequentemente, existe uma diferença entre:

- **referência declarada no catálogo**; e
- **objeto de dados efetivamente persistido**.

Essa diferença precisa ser eliminada antes de tratar o Dataset Oficial como cadeia física completa.

### 2.6 Dataset corrente V1.1

`dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json` declara:

- snapshot anual 2026;
- `normalized_sha256`;
- incrementos diários de 23, 24 e 25/09/2026;
- caminhos dos CSVs diários;
- `fail_closed: true`.

O fluxo diário, portanto, já demonstra uma arquitetura operacional na qual RAW + NORMALIZED + manifest podem ser persistidos juntos.

### 2.7 Dashboard

Existem dois pontos de apresentação:

- `index.html` na raiz: consulta diretamente a árvore do GitHub e o Dataset Oficial V1.0;
- `dashboards/index.html`: lê exclusivamente `dashboards/data/dashboard.json`.

O arquivo `dashboards/data/dashboard.json` está explicitamente classificado como:

`SCHEMA_ONLY / NO OBSERVATIONS EMBEDDED`

e permanece em `AGUARDANDO_DADOS`.

Portanto, o dashboard V1 não é consumidor operacional dos CSVs NORMALIZED anuais.

## 3. Reconstruibilidade

A reconstrução anual é tecnicamente possível sem depender do artefato temporário, desde que:

- o RAW anual esteja preservado;
- o parser `normalize_cotahist.py` esteja preservado;
- a versão do parser esteja registrada;
- o processo de validação seja determinístico;
- o SHA-256 reconstruído seja comparado ao SHA registrado no manifest quando este existir.

Isso reduz o risco de perda histórica, mas não substitui a persistência do NORMALIZED se o contrato do Dataset Oficial exigir disponibilidade física permanente.

## 4. Achado arquitetural principal

A arquitetura implementada hoje é assimétrica:

**Anual:**

`RAW → NORMALIZED temporário → quality manifest persistido → certificação → catálogo oficial`

**Diário:**

`RAW persistido → NORMALIZED persistido → manifest persistido → Dataset Atual`

O contrato do Dataset Oficial descreve uma cadeia mais forte:

`RAW → NORMALIZED → QUALITY → CERTIFICATION → OFFICIAL`

Há, portanto, uma divergência entre o contrato conceitual e a implementação anual.

## 5. Decisão operacional

**NÃO regenerar os 41 CSVs ainda.**

Antes disso, deve ser formalizada uma decisão de arquitetura:

### Opção A — NORMALIZED anual permanente

Persistir:

`dados/cotahist/normalized/anual/COTAHIST_A{ano}.csv`

para 1986–2026.

Vantagem: o contrato passa a representar fisicamente os dados.

Custo: grande aumento de volume do repositório e necessidade de política para Git LFS ou armazenamento externo/versionado.

### Opção B — NORMALIZED anual reconstruível

Manter somente RAW + parser + manifests + SHA e declarar formalmente que o NORMALIZED anual é uma camada reconstruível, não um objeto persistido.

Nesse caso, o Dataset Oficial não deve apresentar o CSV anual como se estivesse permanentemente disponível sem uma regra explícita de reconstrução.

### Opção C — armazenamento de dados separado

Manter o código e metadados no Git e armazenar CSVs NORMALIZED anuais em armazenamento versionado externo, com URI, SHA-256 e política de retenção no manifest.

## 6. Recomendação técnica de governança

Não escolher A, B ou C por conveniência.

A escolha deve ser registrada no contrato NORMALIZED e refletida simultaneamente em:

- workflow de normalização;
- certificação anual;
- gerador do Dataset Oficial;
- manifests;
- dashboard;
- Carta de Confiança;
- política de reconstrução;
- testes de integridade.

## 7. Critério fail-closed

Até a decisão formal:

> Um ano não deve ser apresentado como possuindo NORMALIZED físico permanente quando o arquivo não estiver disponível no caminho declarado.

Também não se deve converter ausência do CSV em zero, nem inferir sua existência a partir de um SHA registrado.

## 8. Próxima frente

A próxima frente técnica deve ser a definição e implementação do **Contrato NORMALIZED Anual V2**, incluindo:

1. política de persistência;
2. política de armazenamento;
3. política de SHA;
4. política de reconstrução;
5. política de retenção;
6. integração com Dataset Oficial;
7. validação fail-closed;
8. integração com dashboard;
9. teste de reconstrução de pelo menos um ano;
10. somente depois, processamento sistemático de 1986–2026.

## 9. Resultado da auditoria

**NORMALIZADOR IDENTIFICADO:** sim.  
**Parser versionado:** sim — 1.1.0.  
**RAW anual preservado:** sim.  
**NORMALIZED anual permanente:** não comprovado; atualmente não persistido.  
**NORMALIZED diário permanente:** sim, conforme workflow diário.  
**Artefato anual temporário:** sim, retenção declarada de 30 dias.  
**Reconstrução determinística:** sim, tecnicamente possível a partir do RAW + parser.  
**Dashboard operacional conectado ao NORMALIZED anual:** não.  
**Necessidade de regenerar 41 CSVs imediatamente:** não.  
**Decisão de arquitetura necessária antes da regeneração:** sim.

## 10. Referências internas

- `scripts/ingestao/normalize_cotahist.py`
- `scripts/ingestao/importar_cotahist_diario_v1.py`
- `scripts/ingestao/reconciliar_cotahist_anual_v1.py`
- `.github/workflows/cotahist-normalizacao-controlada-v7.yml`
- `.github/workflows/cotahist-importacao-diaria-v1.yml`
- `dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json`
- `dados/cotahist/normalized/anual/`
- `dados/cotahist/normalized/diario/`
- `dashboards/index.html`
- `dashboards/data/dashboard.json`
- `docs/ingestao/CONTRATO_DATASET_OFICIAL_COTAHIST_V1.0.md`
- `docs/ingestao/FASE10A_AUDITORIA_ARQUITETURA_NORMALIZADA_V1.0.md`

---

**Regra de integridade:** nenhuma alteração de dados foi realizada durante esta auditoria.
