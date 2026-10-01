# FASE04 — Auditoria de Workflows contra o Layout Mestre V1

Projeto: B3 — A BOLSA DO BRASIL
Repositório: carlos-andrade/B3
Data: 2026-10-01
Fase de governança: FASE04 — auditoria de conformidade
Fonte normativa única: docs/governanca/LAYOUT_MESTRE_CANONICO_B3_V1.md
Status: AUDITORIA ESTRUTURAL INICIADA — NÃO PROMOVER

## 1. Objetivo

Auditar os workflows existentes contra o Layout Mestre Canônico antes de qualquer correção.

A auditoria verifica, no mínimo:
1. independência entre workflows;
2. dependências direcionais;
3. ausência de chamadas/reexecuções entre workflows;
4. gatilhos próprios e causais;
5. ausência de README como gatilho operacional;
6. ausência de docs/ genérico como gatilho operacional;
7. presença de GITHUB_STEP_SUMMARY;
8. regra especial do README — somente 23:55 America/Sao_Paulo;
9. monitor independente e somente leitura;
10. rastreabilidade;
11. idempotência quando aplicável;
12. fail-closed quando aplicável;
13. ausência de responsabilidade de fase posterior;
14. ausência de reexecução por ruído documental.

## 2. Inventário

O diretório .github/workflows/ contém atualmente 108 arquivos YAML de workflow.

O inventário foi obtido diretamente do branch main antes da criação do auditor automático.

Nenhum workflow foi removido, reescrito ou desativado nesta fase.

## 3. Instrumentação criada

Foi criado o auditor determinístico:

scripts/governanca/auditar_workflows_b3.py

Função:
- varrer todos os workflows;
- verificar critérios estruturais;
- gerar matriz JSON;
- gerar matriz Markdown;
- identificar divergências;
- não corrigir workflows;
- não reexecutar workflows;
- não promover fases.

Foi criado o workflow:

.github/workflows/b3-auditoria-workflows-layout-mestre-v1.yml

Função:
- executar a auditoria;
- produzir GITHUB_STEP_SUMMARY;
- persistir a matriz;
- executar por alteração relevante, manualmente ou em rotina diária;
- não usar README como entrada;
- não depender de outro workflow.

Artefatos previstos:
- docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.json
- docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.md

## 4. Auditoria direcionada já realizada

Antes da instrumentação completa, foram inspecionados diretamente workflows críticos do ciclo atual e de governança.

### 4.1 README

Workflow:
.github/workflows/atualizar-readme-b3.yml

Conforme em:
- cron 23:55 America/Sao_Paulo;
- ausência de push trigger;
- ausência de disparo de fases.

Divergência identificada:
- ausência de GITHUB_STEP_SUMMARY.

O ajuste pertence à fase de correção, não a esta auditoria.

### 4.2 Monitor

Workflow:
.github/workflows/b3-monitor-execucoes-v1.yml

Conforme nos critérios inspecionados:
- schedule a cada 15 minutos;
- actions: read;
- contents: read;
- ausência de reexecução;
- publicação em GITHUB_STEP_SUMMARY.

Resultado direcionado: CONFORME.

### 4.3 FASE14 — 1995

Workflow:
.github/workflows/cotahist-fase14-presenca-integridade-1995-v1.yml

Conforme em:
- responsabilidade de presença/integridade;
- entrada RAW explícita;
- gatilho próprio;
- workflow_dispatch;
- sem chamada a outro workflow;
- preservação do RAW.

Divergência:
- ausência de GITHUB_STEP_SUMMARY.

### 4.4 FASE03 — 1995

Workflow:
.github/workflows/cotahist-fase03-parsing-1995-v1.yml

Conforme em:
- dependência explícita da evidência FASE14;
- parsing estrutural próprio;
- ausência de chamada a outro workflow;
- gatilhos relacionados à própria tarefa.

Divergência:
- ausência de GITHUB_STEP_SUMMARY.

### 4.5 FASE04 — 1995

Workflow:
.github/workflows/cotahist-fase04-normalizacao-1995-v1.yml

Conforme em:
- consumo da evidência FASE03;
- responsabilidade de normalização;
- fail-closed para pré-condição FASE03;
- saída normalizada própria.

Divergência:
- ausência de GITHUB_STEP_SUMMARY.

### 4.6 FASE09 — 1993

Workflow:
.github/workflows/cotahist-fase09-prerelease-1993-v1.yml

Conforme em:
- consolidação de evidências anteriores;
- não retrocertificação;
- bloqueio quando evidência obrigatória está ausente;
- decisão explícita.

Divergência:
- ausência de GITHUB_STEP_SUMMARY.

Este workflow pertence ao histórico de 1993 e não deve ser reexecutado apenas para corrigir nomenclatura.

### 4.7 Certificação anual

Workflow:
.github/workflows/cotahist-certificacao-anual-v1.yml

Conforme em:
- consumo de evidências;
- atualização da matriz de certificação;
- schedule próprio;
- workflow_dispatch;
- ausência de chamada explícita a outro workflow.

Divergência:
- ausência de GITHUB_STEP_SUMMARY.

### 4.8 Importação diária

Workflow:
.github/workflows/cotahist-importacao-diaria-v1.yml

Divergência estrutural identificada:
- ausência de GITHUB_STEP_SUMMARY.

Também deverá ser verificado na matriz completa se a responsabilidade de reconciliar o dataset anual permanece compatível com a separação entre aquisição/importação e fases de validação/certificação.

Nenhuma correção foi aplicada nesta auditoria.

### 4.9 Orquestrador DRY-RUN

Workflow:
.github/workflows/cotahist-orquestrador-anual-dryrun-v2.yml

Conforme em:
- execução manual;
- modo DRY-RUN;
- ausência de mutação declarada;
- ausência de push/publicação;
- verificação da cadeia 00–12.

Ponto de governança a validar na matriz completa:
- dependências de fases devem ser representadas por evidência autorizada;
- workflows não devem chamar/reexecutar outros workflows;
- DRY-RUN deve permanecer diagnóstico e não pode ser interpretado como executor da cadeia real.

Divergência:
- ausência de GITHUB_STEP_SUMMARY.

## 5. Regra de classificação

Nesta fase:

DIVERGENTE não significa dado incorreto.

Significa que o workflow possui alguma característica que precisa ser reconciliada com o Layout Mestre.

A sequência obrigatória é:

AUDITAR → CLASSIFICAR → INVESTIGAR → CORRIGIR NA ORIGEM → VALIDAR → PROMOVER

## 6. Não ações executadas

Nesta fase não houve:
- alteração de workflow operacional existente;
- reexecução de workflow histórico;
- correção de FASE14;
- correção de FASE03;
- correção de FASE04;
- correção de FASE09;
- reabertura de 1994;
- reabertura de 1993;
- alteração de README;
- alteração da certificação histórica;
- alteração do RAW.

Isso preserva isolamento e monotonicidade.

## 7. Resultado da FASE04

Estado atual:

AUDITORIA ESTRUTURAL INICIADA.

O inventário de 108 workflows foi consolidado e o auditor automático foi incorporado ao repositório.

A matriz completa deve ser gerada pelo novo workflow antes de qualquer lote de correções.

Evidências de implementação:
- scripts/governanca/auditar_workflows_b3.py
- .github/workflows/b3-auditoria-workflows-layout-mestre-v1.yml

## 8. Próxima fase

FASE05 — CLASSIFICAÇÃO DAS DIVERGÊNCIAS E CORREÇÃO NA ORIGEM

Somente workflows efetivamente classificados como divergentes serão alterados.

Workflows conformes não serão modificados.

## 9. Controle de versão

| Item | Commit |
|---|---|
| Auditor automático | 6261df19a1adfb51bc3bf3ba6938f09afdfdb5d |
| Workflow automático de auditoria | 07a56073de6997b77a0b36845bd6e3223675128d |

## 10. Regra final

A auditoria não substitui o Layout Mestre.

O Layout Mestre continua sendo a única fonte normativa operacional:

LAYOUT MESTRE → WORKFLOW → EVIDÊNCIA → VALIDAÇÃO → DECISÃO
