# FASE05.4 — CLASSIFICAÇÃO SEMÂNTICA E MATRIZ DE CONFORMIDADE DOS WORKFLOWS B3

**Status:** CONCLUÍDA COM PONTOS DE CONTROLE  
**Fonte normativa:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`  
**Escopo:** 109 workflows  
**Data de referência:** 2026-10-01

## 1. Objetivo

Transformar a triagem funcional das FASES 05, 05.2 e 05.3 em uma classificação semântica utilizável para a próxima etapa de melhoria do auditor, sem modificar workflows e sem reabrir cadeias históricas.

A FASE05.4 não é fase de correção operacional.

## 2. Fontes utilizadas

- `docs/governanca/auditorias/FASE05_2_CLASSIFICACAO_FUNCIONAL_WORKFLOWS_B3_V1.json`
- `docs/governanca/auditorias/FASE05_3_VALIDACAO_HISTORICOS_CASOS_AMBIGUOS_V1.json`
- `docs/governanca/auditorias/WORKFLOWS_CONFORMIDADE_B3_ATUAL.json`
- `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`

## 3. Resultado quantitativo

| Dimensão | Resultado |
|---|---:|
| Workflows auditados | 109 |
| COTAHIST | 95 |
| BCB_MACRO | 2 |
| BVBG | 3 |
| Governança/monitoramento | 2 |
| WIKI | 2 |
| README | 1 |
| ÍNDICES | 1 |
| Teste auxiliar | 1 |
| MARKET_DATA_PREGAO | 1 |
| OUTROS residual | 1 |
| Históricos | 81 |
| Ativos | 25 |
| Auxiliar | 1 |
| A validar | 2 |
| Conformes no auditor estrutural atual | 5 |
| Divergentes no auditor estrutural atual | 104 |

## 4. Correções semânticas de classificação

### 4.1 Atualizar catálogo B3

`.github/workflows/atualizar-catalogo-b3.yml`

Classificação anterior: OUTROS.  
Classificação semântica: **BVBG / ATIVO**.

Evidência direta: o workflow executa `ferramentas/importar_bvbg028.py` e publica em `ativos/catalogo` e `ativos/instrumentos`.

A divergência registrada pelo auditor atual é ausência de `GITHUB_STEP_SUMMARY`. Isso é observabilidade, não evidência de defeito funcional.

### 4.2 Captura de pesquisa por pregão

`.github/workflows/capturar-pesquisa-pregao.yml`

Classificação anterior: OUTROS / A_VALIDAR.  
Classificação semântica: **MARKET_DATA_PREGAO / ATIVO**.

Evidência direta: captura dados por pregão e persiste em `dados/market_data/raw` e manifests.

O trigger por push observado está restrito ao próprio workflow e à ferramenta de ingestão.

## 5. Pontos de controle

### FASE06 — 1995

`.github/workflows/cotahist-fase06-semantica-1995-v1.yml`

O conteúdo atual apresenta isolamento compatível: FASE05 + RAW 1995 + próprio workflow, liberando a FASE07.

A ocorrência histórica de `NO_README_TRIGGER` permanece como incidente de origem. **Não será corrigida retroativamente nesta fase.**

### FASE12 — 1993

`.github/workflows/cotahist-fase12-fechamento-transicao-1993-v1.yml`

O trigger inclui a matriz anual de certificação 1986–2026 e múltiplas evidências.

Isso é um ponto de controle de causalidade/isolamento para o auditor melhorado. **Não autoriza reexecução do histórico de 1993.**

### Certificação anual

`.github/workflows/cotahist-certificacao-anual-v1.yml`

Workflow ativo multianual. Requer validação específica posterior de:

- causalidade dos gatilhos;
- idempotência;
- janela operacional;
- dependências de evidência;
- comportamento de publicação.

### Wiki

`.github/workflows/sincronizar-wiki.yml`

O auditor registra `NO_README_TRIGGER`. O workflow usa `WIKI/**`, o próprio workflow e agendamento frequente.

A revisão deve ocorrer em contrato específico da Wiki; não haverá correção nesta fase.

## 6. Interpretação correta do resultado 5/104

O resultado **5 conformes / 104 divergentes** não significa que existam 104 defeitos funcionais.

O auditor estrutural atual identifica principalmente ausência de `GITHUB_STEP_SUMMARY`.

A FASE05.4 separa:

- **OBSERVABILIDADE** — requisito de retorno/auditoria;
- **TRIGGER** — possível problema de causalidade;
- **PONTO_DE_CONTROLE** — necessita investigação sem reabrir histórico;
- **CONFORME** — critérios atuais satisfeitos.

Portanto, a ausência de `STEP_SUMMARY` não deve ser tratada como corrupção de dados, falha semântica ou quebra da cadeia COTAHIST.

## 7. Matriz de conformidade por grupo

| Grupo | Qtde | Prioridade | Decisão |
|---|---:|---|---|
| COTAHIST | 95 | Isolamento + observabilidade | Não corrigir históricos; revisar ativos por grupo |
| BCB_MACRO | 2 | Observabilidade | Correção posterior agrupada |
| BVBG | 3 | Observabilidade + responsabilidade | Manter classificação e revisar contrato |
| Governança/monitoramento | 2 | Conformidade | Referência estrutural |
| WIKI | 2 | Trigger | Revisão contratual separada |
| README | 1 | Regra 23:55 | Manter como consolidação |
| ÍNDICES | 1 | Observabilidade | Revisão posterior |
| Teste auxiliar | 1 | Observabilidade | Não promover a operacional |
| MARKET_DATA_PREGAO | 1 | Observabilidade | Nova categoria reconhecida |
| OUTROS residual | 1 | Classificação | Manter sob validação |

## 8. Regras semânticas consolidadas

Um workflow somente poderá ser considerado semanticamente conforme quando houver compatibilidade entre:

**responsabilidade → entrada → processamento → evidência → decisão → saída**

Além disso:

- não chama outro workflow;
- não reexecuta outro workflow;
- não depende de README;
- não usa `docs/` genérico como gatilho operacional;
- não depende de fase posterior;
- possui observabilidade adequada;
- respeita isolamento;
- respeita a responsabilidade definida no Layout Mestre.

## 9. Decisões desta fase

1. **Nenhum workflow operacional foi alterado.**
2. **Nenhum histórico COTAHIST foi reaberto.**
3. **1994 permanece congelado.**
4. **1993 permanece fechado.**
5. **1995 permanece em FASE07.**
6. As duas classificações ambíguas foram resolvidas semanticamente.
7. Pontos de controle foram preservados para investigação posterior.
8. A próxima etapa é **MELHORIA DO AUDITOR**, não correção em massa.

## 10. Artefato detalhado

A matriz estruturada desta fase está em:

`docs/governanca/auditorias/FASE05_4_CLASSIFICACAO_SEMANTICA_MATRIZ_CONFORMIDADE_WORKFLOWS_B3_V1.json`

## 11. Commit

`845b7d89412d19e322d1954af34d7067045d06a3`

## 12. Próxima fase

**MELHORIA DO AUDITOR**

O auditor deverá passar de uma verificação estrutural simples para uma verificação capaz de identificar, quando aplicável:

- responsabilidade por workflow;
- dependências direcionais;
- trigger causal;
- isolamento por fase;
- risco de trigger por fase posterior;
- permissões;
- idempotência;
- persistência de evidência;
- decisão explícita;
- fail-closed;
- política de reexecução.

Nenhuma correção em massa deve ser feita antes dessa melhoria.


## 13. Melhoria do auditor — conclusão

A etapa seguinte foi executada sem alterar retrospectivamente os workflows históricos.

O auditor `scripts/governanca/auditar_workflows_b3.py` foi evoluído para a versão **2.0.0**, passando a distinguir:

- conformidade;
- conformidade com observação;
- divergência crítica;
- alertas de média/baixa severidade.

Além da estrutura anterior, passou a verificar sinais de:

1. trigger causal;
2. trigger de fase posterior;
3. dependência direcional;
4. permissões compatíveis com escrita real;
5. persistência de evidência;
6. decisão/status;
7. idempotência/deduplicação;
8. isolamento e ausência de reexecução;
9. política especial do README;
10. comportamento somente-leitura do monitor.

A ausência isolada de `GITHUB_STEP_SUMMARY` foi formalmente reclassificada como **observabilidade**, não como defeito funcional de dados.

### Commits da melhoria

- Auditor v2: `47ff09231564d71187cfc96aa1804652a6e0cd77`
- Workflow adaptado ao schema v2: `944706915327604352a8893bbd6f7410084d992d`

### Regra de não automação

O auditor continua estritamente diagnóstico. Ele não corrige, reexecuta ou promove workflows.

## 14. Consolidação normativa nas Cartas

Após a melhoria do auditor, as regras foram gravadas também nas quatro fontes de governança subordinadas ao Layout Mestre:

- `docs/CARTA_DE_CONFIANCA_DOS_DADOS.md`
  - commit `78a149d123dd4b5df6e5fb892b2ab1225b446808`
- `docs/CARTA_MAGNA_GOVERNANCA_B3.md`
  - commit `1e12daddc76d341a40dd45d1eaba074a6892f83b`
- `docs/CARTA_DE_GARANTIAS_DO_PROJETO_B3.md`
  - commit `2682466fb5f59ee16358aaff09de58e34b751dd3`
- `docs/MODELO_GOVERNANCA_PARA_PROJETOS.md`
  - commit `62a0a4392c083c805b87a20780b72136eb25d4a9`

O próprio Layout Mestre também recebeu a regra:

- `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`
  - commit `5c53cee3503c7102eb1e6dce0b15593960144da9`

A hierarquia permanece:

**CARTAS/DOCUMENTOS DE ENTRADA → LAYOUT MESTRE → CÓDIGO → EVIDÊNCIA → VALIDAÇÃO → DECISÃO**

As Cartas foram atualizadas como fontes de entrada/histórico; o Layout Mestre permanece a autoridade operacional única.
