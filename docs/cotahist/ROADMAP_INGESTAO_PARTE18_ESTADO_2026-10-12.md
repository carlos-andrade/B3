# B3 — A BOLSA DO BRASIL
## PARTE18 — Roadmap de ingestão e certificação COTAHIST
**Data de referência:** 2026-10-12  
**Repositório oficial:** https://github.com/carlos-andrade/B3  
**Branch:** main  
**Estado geral:** EM CORREÇÃO E VALIDAÇÃO  
**Norma:** docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md

## 1. Objetivo desta continuação

Dar continuidade à PARTE17, inspecionar as falhas mais recentes, corrigir incompatibilidades identificadas no código, reduzir concorrência de escrita entre workflows e executar validações reais no GitHub Actions. Não declarar certificação sem evidência de execução concluída.

## 2. Diagnóstico confirmado

### 2.1 Dataset oficial — incompatibilidade de versão

A execução 23 de `COTAHIST - dataset oficial V1` falhou com `1998: parser incompatível`.

O gerador `scripts/ingestao/gerar_dataset_oficial_cotahist_v1.py` exigia exclusivamente `parser_version == "1.1.0"`, embora o manifesto de 1998 esteja marcado como `VALIDADO`, com parser `1.1.1`, 25 campos, 104.971 linhas, zero datas inválidas e zero datas fora do ano.

Evidência: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/normalized/manifests/COTAHIST_A1998_quality.json

### 2.2 Certificação anual

O script `scripts/ingestao/certificar_cotahist_anual_v1.py` também exigia apenas a versão `1.1.0`. Isso reproduzia a incompatibilidade na matriz de certificação.

Correção publicada: ambos os scripts passaram a reconhecer explicitamente as versões `1.1.0`, `1.1.1` e `1.1.2`. A lista é fechada; novas versões não serão aceites implicitamente.

Commits:
- `d949192d9de30a02c9ec45851a0a780b179c0c35` — compatibilidade explícita na certificação anual.
- `c5a0a204571dbd5b84f03e3f382e2ec5c6a0d059` — compatibilidade explícita no gerador do dataset oficial.

**Limite da correção:** reconhecer uma versão de parser não substitui a validação de integridade dos arquivos, hashes, esquema, calendário ou semântica. O dataset deve continuar a falhar fechado se qualquer outro critério falhar.

### 2.3 REC-001 — concorrência e gatilho excessivo

O workflow `.github/workflows/rec001-cotahist-bloomberg-mail.yml` usava `push.paths: '**'`, fazendo a publicação da própria evidência disparar outra execução. Isso contribuiu para execuções repetidas e rejeições de `git push` por concorrência.

Correção publicada no commit `f2512bec41c5062a27eb1846c30af7097b2e48a5`:
- gatilhos `push` limitados ao RAW COTAHIST 2026, ao script REC-001 e ao próprio workflow;
- execução agendada e manual preservadas;
- grupo de concorrência com `cancel-in-progress: false`;
- checkout com histórico completo para permitir `git pull --rebase`;
- publicação da evidência somente quando a comparação termina com sucesso;
- resumo de execução no `GITHUB_STEP_SUMMARY`.

As execuções já iniciadas sob a configuração antiga podem terminar em falha; avaliar separadamente os resultados após a estabilização. A alteração evita novos disparos provocados apenas pela gravação da evidência, mas não elimina conflitos com todos os outros workflows que escrevem em `main`.

### 2.4 Comparação REC-001 — falso positivo no cabeçalho temporal

A evidência REC-001 anterior comparava as linhas físicas desde a primeira linha, incluindo o registo tipo `00` (cabeçalho com data do snapshot) e o tipo `99` (trailer com contagem). Como o snapshot B3 terminava em 2026-09-23 e o RAW do BLOOMBERG_MAIL avançava até 2026-10-06, os cabeçalhos diferiam legitimamente e a comparação reportava divergência na posição 1 antes de comparar qualquer registo tipo `01`.

Correção publicada no commit `4cdafbfdc62803be8bc6fa823577f38dca176b3b`: comparar apenas registos tipo `01`, preservando a ordem física, reportando a primeira divergência real, posição comum e se cada fluxo se esgotou. Os cabeçalhos tipo `00` e trailers tipo `99` ficam explicitamente fora da comparação de sobreposição.

**Resultado verificado em 2026-10-12:** execução #210 concluída com sucesso técnico e evidência persistida. O comparador eliminou o falso positivo do cabeçalho e identificou divergência real na posição 222.003 dos registos tipo `01`, na data 2026-01-02 (`ABCBA235` no snapshot B3 versus `ABCBA243` no RAW BLOOMBERG_MAIL). Os 222.002 registos anteriores coincidem byte a byte. Estado de negócio: `FAIL_CONTENT_DIVERGENCE`; promoção bloqueada. A causa da divergência deve ser investigada, sem afrouxar a comparação nem assumir que a diferença é legítima antes de consultar os registos originais e a eventual política de retificações.

## 3. Roadmap por marco

| Marco | Estado observado | Próxima ação |
|---|---|---|
| COTAHIST 1986–2003 | Histórico de ingestão e certificação com exceções específicas por ano | Preservar evidências e não presumir uniformidade entre anos |
| COTAHIST 2004 | **FASE00–FASE12 concluídas**; 2004 certificado; transição validou RAW 2005 | COTAHIST 2005: **FASE04–FASE12 concluídas**, certificado e fechado; 2006: FASE01–FASE06 `VALIDADO`, 198.367 registos e zero divergências nos 12 campos críticos; FASE07 em execução |
| COTAHIST 2005 | FASE12 registada como concluída, com transição controlada | Preservar fechamento e evidências |
| COTAHIST 2006 | FASE00 aprovada em execução do GitHub Actions | Continuar a partir da fase seguinte prevista no plano |
| Certificação anual | **PASS** — execução #32 concluída com sucesso; matriz contém 41 anos certificados | Manter teste de regressão para versões homologadas |
| Dataset oficial | **PASS** — execução #24 concluída com sucesso; manifesto oficial publicado para 1986–2026 | Validar consistência entre manifesto, matriz e hashes em auditoria independente |
| REC-001 B3 × BLOOMBERG_MAIL | **FAIL_CONTENT_DIVERGENCE**; 222.002 registos tipo 01 coincidem; primeira diferença na posição 222.003, em 2026-01-02 | Investigar o par de registos divergentes e classificar causa; manter promoção bloqueada até resolução |
| Auditoria de workflows | **PASS** — execução #258 terminou com sucesso após a correção do workflow REC-001 | Reexecutar após o fim das execuções antigas e confirmar ausência de novos conflitos |

## 4. Critérios de aceite para publicação do dataset oficial

A publicação só pode ser considerada aprovada se:
1. todos os anos esperados (1986–2026) tiverem RAW, manifesto e matriz de certificação presentes;
2. o estado de qualidade for `VALIDADO`;
3. a versão do parser estiver na lista explicitamente homologada;
4. os 25 campos forem confirmados;
5. datas inválidas e datas fora do ano forem zero;
6. os hashes e as contagens corresponderem às evidências do ano;
7. nenhuma divergência bloqueadora permanecer na certificação;
8. o workflow terminar com sucesso e o manifesto final ficar disponível no repositório.

## 5. Ordem operacional imediata

1. Verificar os resultados finais das execuções disparadas pelos commits de correção.
2. Corrigir qualquer nova falha encontrada nos logs, sem afrouxar critérios de integridade.
3. Reexecutar a certificação anual e confirmar a matriz.
4. Reexecutar a geração do dataset oficial.
5. Validar a REC-001 e a publicação da sua evidência.
6. Reexecutar a auditoria de conformidade do Layout Mestre.
7. Só então atualizar os estados de fase e avançar o próximo ano/fase autorizado.

## 6. Registo de execução desta parte

As correções foram publicadas em `main`. A certificação anual #32, a geração do dataset oficial #24 e a auditoria de workflows #258 terminaram com sucesso. A matriz contém 41 anos sem falhas de certificação, mantendo explícita a exceção semântica controlada de 1986. A REC-001 #210 terminou com sucesso técnico, mas a comparação de negócio está bloqueada por divergência real na posição 222.003. A FASE05 de 2004 foi executada na run #2 e validou hashes e estrutura; a FASE06 foi executada e a evidência persistida com `VALIDADO`, 166.937 registos RAW e NORMALIZED, 12 campos críticos e `mismatch_count: 0`. A FASE07 foi executada e validou a chave candidata `(data_pregao, codbdi, codneg, tpmerc, prazot, dismes)`: a chave-base tinha 9.642 grupos de colisão e 20.705 linhas excedentes, mas incluir `prazot` separou todos os casos; 166.937 chaves distintas, zero colisões, zero linhas removidas. A FASE08 terminou com `VALIDADO_COM_EXCECAO` e liberou o gate 06–08. Foram observadas 249 datas de pregão, nenhuma data inválida/fora do ano, mas 30.148 regressões cronológicas porque a fonte mantém ordenação que não é globalmente cronológica. O workflow classificou essa característica como exceção não bloqueadora com base na reconciliação de linhas da FASE06; nenhuma linha foi reordenada nem removida. O calendário oficial histórico de sessões/feriados ainda não está persistido, portanto não se declara validação contra calendário externo B3.

**Regra de governança:** não saltar fases, não substituir evidência por inferência, não remover registos para forçar reconciliação e não promover o dataset quando os gates falharem.


## 7. Atualização incremental — 2026-10-12

### Estado operacional confirmado

- **2004:** FASE00–FASE12 concluídas; FASE11 `CERTIFICADO`. FASE10 comparou 166.937 registos e 25 campos com zero divergências. A transição para 2005 foi validada sem certificar 2005 automaticamente.
- **2005:** FASE04–FASE12 concluídas; FASE11 `CERTIFICADO`. FASE10 comparou 181.408 registos e 25 campos com zero divergências. A transição para 2006 validou o RAW e a integridade estrutural, mas não certificou 2006.
- **2006:** FASE00–FASE08 concluídas; gate 06–08 `GATE_APROVADO`. FASE01–FASE07 estão `VALIDADO`; FASE08 está `VALIDADO_COM_EXCECAO`, com 246 datas de pregão, zero datas inválidas/fora do ano, zero regressões cronológicas e nenhuma linha removida. A exceção não bloqueadora é a falta de calendário oficial histórico de sessões/feriados persistido.
- **2006, identidade:** a chave candidata `(data_pregao, codbdi, codneg, tpmerc, prazot, dismes)` produziu 198.367 chaves distintas e zero colisões. A chave-base tinha 11.764 grupos de colisão; nenhuma deduplicação foi realizada.
- **2006:** FASE11 terminou `CERTIFICADO`, sem bloqueadores; FASE10 comparou 198.367 registos e 25 campos com zero divergências. A FASE12 de fechamento 2006/abertura 2007 foi criada a partir do padrão de transição anterior e está a ser executada. Os workflows FASE01–11 de 2006 não existiam na `main`; estão a ser repostos individualmente a partir da branch de recuperação, evitando uma mesclagem ampla que também reverteria alterações recentes de governação.
- **REC-001 B3 × BLOOMBERG_MAIL:** permanece `FAIL_CONTENT_DIVERGENCE`. Os primeiros 222.002 registos tipo `01` coincidem; a primeira diferença está na posição 222.003, em 2026-01-02 (`ABCBA235` versus `ABCBA243`). Não promover até classificar a causa.
- **Auditoria de workflows:** a persistência foi corrigida para reconstruir a auditoria sobre `origin/main` após push concorrente. Execuções posteriores tiveram sucessos; algumas execuções antigas foram canceladas por concorrência. Confirmar o estado final da auditoria mais recente antes de declarar a fila limpa.

### Evidências de execução

- [FASE12 2004 — fechamento e transição 2005](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2004_FASE12_FECHAMENTO_2005_ABERTURA_V1.json)
- [FASE10 2005 — validação independente](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2005_FASE10_VALIDACAO_INDEPENDENTE_V1.json)
- [FASE12 2005 — fechamento e transição 2006](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2005_FASE12_FECHAMENTO_2006_ABERTURA_V1.json)
- [FASE06 2006 — reconciliação semântica](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2006_FASE06_RECONCILIACAO_V1.json)
- [FASE07 2006 — identidade e cardinalidade](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2006_FASE07_IDENTIDADE_CHAVES_V1.json)
- [FASE08 2006 — calendário e consistência](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2006_FASE08_SEMANTICA_CALENDARIO_V1.json)
