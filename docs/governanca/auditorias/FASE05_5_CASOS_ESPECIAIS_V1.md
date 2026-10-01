# FASE 05.5 — CASOS ESPECIAIS V1

**Projeto:** B3 — A BOLSA DO BRASIL  
**Data:** 2026-10-01  
**Status:** VALIDADO  
**Fonte normativa:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`

## 1. Escopo

Foram auditados os componentes com comportamento excepcional ou transversal:

- README de consolidação;
- monitor independente;
- auditor de governança;
- publicação da Wiki nativa;
- workflows legados/duplicados;
- exceção histórica FASE00/1994.

## 2. Evidência da reauditoria

- Workflow auditor: `b3-auditoria-workflows-layout-mestre-v1.yml`
- Execução registrada pelo commit de auditoria: `14ac766b0daa280f3adaeb7534498df8bca37d98`
- Matriz: `docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.json`
- Geração da matriz: `2026-10-01T22:43:56.661284+00:00`
- Workflows auditados: **108**
- CONFORME: **24**
- CONFORME_COM_OBSERVACAO: **84**
- DIVERGENTE_CRITICA: **0**
- severidade ALTA: **0**

## 3. Casos especiais validados

### 3.1 README

O README permanece artefato de consolidação e não de operação.

Regra confirmada:

- execução às 23:55 America/Sao_Paulo;
- sem gatilho `push`;
- sem disparo de fases;
- idempotência;
- Step Summary funcional.

Correção realizada na origem:

`.github/workflows/atualizar-readme-b3.yml`

Commit:

`1d3c796b249677397030d0c56a214ad3fba14cd4`

A correção eliminou a escrita escapada que impediria a persistência correta em `GITHUB_STEP_SUMMARY`.

### 3.2 Monitor independente

`.github/workflows/b3-monitor-execucoes-v1.yml`

Validação:

- somente leitura;
- sem escrita Git;
- sem reexecução;
- sem chamada de outro workflow;
- classificação de estado preservada;
- Step Summary presente.

Status na matriz: **CONFORME**.

### 3.3 Auditor de governança

`.github/workflows/b3-auditoria-workflows-layout-mestre-v1.yml`

Validação:

- usa o Layout Mestre como fonte normativa;
- não reexecuta workflows;
- persiste sua própria evidência;
- possui mecanismo de recuperação contra corrida de publicação;
- decisão explícita no Step Summary.

Status na matriz: **CONFORME**.

### 3.4 Wiki nativa

Foi identificada duplicação funcional: dois workflows publicavam a mesma Wiki nativa.

Workflow removido:

`.github/workflows/sincronizar-wiki.yml`

Commit:

`d0c6fa81daafea19fa169b99d0f49d9e382973b6`

Publicador canônico preservado:

`.github/workflows/sincronizar-wiki-b3.yml`

A decisão foi incorporada ao Layout Mestre no commit:

`b499abd9278134e8fbd124842cdb1ac4929948a1`

A matriz final contém somente o publicador canônico, classificado como **CONFORME**.

### 3.5 Exceção histórica FASE00/1994

A permissão `contents: write` permanece registrada como exceção histórica formal no workflow de governança de 1994.

Não houve alteração retroativa.

A exceção não produz divergência crítica ou alta e não reabre o ciclo 1994.

## 4. Regra consolidada

Casos especiais podem possuir comportamento diferente do padrão de fases, mas devem possuir:

**responsabilidade explícita → isolamento → permissão mínima compatível → idempotência quando aplicável → evidência → decisão → ausência de reexecução cruzada.**

## 5. Decisão

**CASOS ESPECIAIS = VALIDADO**

Não há bloqueador crítico ou de alta severidade.

Próxima etapa:

**CERTIFICAÇÃO DA ARQUITETURA**

