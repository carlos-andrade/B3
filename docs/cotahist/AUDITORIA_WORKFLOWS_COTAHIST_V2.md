# Auditoria de Workflows COTAHIST — Fase de Ordenação V2

**Data:** 2026-09-29  
**Repositório:** carlos-andrade/B3  
**Escopo:** arquitetura COTAHIST e dependências entre workflows  
**Estado:** AUDITORIA EM ANDAMENTO — 1994 permanece bloqueado

## 1. Objetivo

Verificar se os workflows existentes respeitam a ordem canônica 00–12 e identificar corridas, dependências implícitas, duplicidade de responsabilidade e pontos em que um workflow pode publicar antes de sua pré-condição estar comprovada.

## 2. Ordem canônica

00 Governança → 01 Aquisição/RAW → 02 Integridade da fonte → 03 Parsing → 04 Normalização → 05 Manifesto/Checksum → 06 Reconciliação → 07 Identidade → 08 Semântica/Consistência → 09 Pré-release → 10 Validação independente → 11 Certificação/Promoção → 12 Fechamento/Abertura.

## 3. Achados confirmados

### A01 — FASE 10 e materialização não possuem dependência formal

Os workflows anuais de materialização (ex.: 1992/1993) e FASE 10 possuem ambos gatilhos `push` sobre arquivos relacionados. A FASE 10 não declara `needs:` nem `workflow_run` dependente da conclusão da materialização.

**Risco:** corrida temporal. A FASE 10 pode iniciar em um commit em que o NORMALIZED ainda não está materializado. Isso já ocorreu operacionalmente em 1990–1993 e exigiu retrigger.

**Classificação:** NÃO CONFORMIDADE DE ORQUESTRAÇÃO.

### A02 — Certificação anual é acionável independentemente da FASE 10

`cotahist-certificacao-anual-v1.yml` possui `push`, `schedule` e `workflow_dispatch`. O workflow lê a matriz e grava no Git, mas não declara uma dependência operacional de uma execução FASE 10 bem-sucedida no mesmo ciclo.

**Risco:** certificação pode ser recalculada antes/depois de evidências sem uma cadeia formal de promoção.

**Classificação:** DEPENDÊNCIA IMPLÍCITA.

### A03 — Dataset Oficial V2 também é independente

`cotahist-dataset-oficial-v2.yml` é disparado por alterações em NORMALIZED, manifests e certificação. Não há `needs`/orquestrador que imponha a sequência FASE10 → certificação → dataset oficial.

**Risco:** publicação concorrente ou promoção prematura.

**Classificação:** DEPENDÊNCIA IMPLÍCITA.

### A04 — Normalização controlada V7 e materialização anual têm responsabilidades sobrepostas

`cotahist-normalizacao-controlada-v7.yml` normaliza e valida, mas publica principalmente manifestos/checksum; os workflows `materializar-normalized-AAAA-v1.yml` materializam o CSV anual. Isso cria duas trilhas operacionais para a mesma transformação.

**Risco:** divergência de execução e dificuldade de provar qual trilha é canônica.

**Classificação:** DUPLICIDADE FUNCIONAL A SER RESOLVIDA.

### A05 — Workflow histórico 1986 possui comportamento diferente do pipeline anual normal

`cotahist-gate-historico-1986.yml` combina normalização, auditoria semântica, validação estrutural, persistência LFS, manifesto e gate final em uma única cadeia.

Isso é compatível com o caráter de exceção histórica de 1986 e não deve ser simplesmente encaixado no pipeline anual padrão.

**Classificação:** EXCEÇÃO CONTROLADA.

### A06 — Validação independente de 1988 usa checkout com LFS desabilitado

`cotahist-validacao-independente-1988-v2.yml` usa `lfs: false`, embora valide um dataset NORMALIZED que é armazenado em LFS.

O workflow possui gates próprios e preserva RAW imutável/não correção, mas a política de checkout deve ser revisada para garantir que a validação independente realmente opere sobre o conteúdo materializado e não sobre ponteiro LFS.

**Classificação:** PONTO DE AUDITORIA — NÃO DECLARAR FALHA DE DADOS SEM TESTE.

### A07 — Workflows que fazem commit no próprio main amplificam corridas

Vários workflows possuem `contents: write` e executam `git commit` + `rebase` + `push`. Isso é operacionalmente possível, mas quando múltiplos workflows são disparados pelo mesmo conjunto de alterações, o rebase reduz conflitos de Git, mas não cria dependência semântica entre pipelines.

**Classificação:** RISCO SISTÊMICO DE ORQUESTRAÇÃO.

## 4. Decisão provisória

**NÃO iniciar FASE 10 de 1994 ainda.**

A arquitetura precisa primeiro ter uma cadeia explícita de promoção.

## 5. Arquitetura alvo

A partir do pipeline normal anual:

RAW
→ integridade
→ parsing/normalização
→ manifesto/hash
→ reconciliação
→ identidade
→ semântica
→ pré-release
→ FASE10
→ certificação
→ dataset oficial
→ fechamento.

A implementação deverá usar dependências explícitas, preferencialmente jobs `needs:` dentro de um orquestrador ou workflows reutilizáveis chamados em sequência. Gatilhos por `push` devem deixar de ser o mecanismo principal de dependência entre fases.

## 6. Próxima auditoria

1. Inventariar todos os `.github/workflows/cotahist-*.yml`.
2. Classificar cada workflow 00–12.
3. Identificar ativos, históricos e legados.
4. Mapear triggers e arquivos de saída.
5. Construir DAG.
6. Testar pontos A01–A07.
7. Criar plano de migração sem apagar histórico.
8. Só então liberar 1994.

## 7. Regra de segurança

Nenhum achado desta auditoria invalida automaticamente os releases 1988–1993. Os dados e evidências já existentes permanecem preservados. Qualquer não conformidade será tratada separadamente como problema de processo/orquestração até que uma prova de integridade de dados demonstre o contrário.

