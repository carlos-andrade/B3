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

## 3. Roadmap por marco

| Marco | Estado observado | Próxima ação |
|---|---|---|
| COTAHIST 1986–2003 | Histórico de ingestão e certificação com exceções específicas por ano | Preservar evidências e não presumir uniformidade entre anos |
| COTAHIST 2004 | FASE00–FASE04 registadas como validadas na continuidade anterior | Confirmar evidências e avançar FASE05 em sequência |
| COTAHIST 2005 | FASE12 registada como concluída, com transição controlada | Preservar fechamento e evidências |
| COTAHIST 2006 | FASE00 aprovada em execução do GitHub Actions | Continuar a partir da fase seguinte prevista no plano |
| Certificação anual | Código corrigido para aceitar versões homologadas | Confirmar execução do workflow e matriz publicada |
| Dataset oficial | Código corrigido para aceitar versões homologadas | Confirmar execução; não promover enquanto houver anos não certificados |
| REC-001 B3 × BLOOMBERG_MAIL | Workflow corrigido para limitar triggers e serializar execuções próprias | Verificar resultado de comparação, hashes e persistência da evidência |
| Auditoria de workflows | Execução recente falhou durante publicação por rejeição non-fast-forward e conflito no rebase | Reexecutar após estabilização das gravações concorrentes e investigar conflitos remanescentes |

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

As correções de código e de workflow foram publicadas em `main`. No momento deste registo, as execuções acionadas por esses commits ainda estavam em andamento; portanto, não se declara PASS para certificação anual, dataset oficial, REC-001 ou auditoria sem consulta aos resultados finais.

**Regra de governança:** não saltar fases, não substituir evidência por inferência, não remover registos para forçar reconciliação e não promover o dataset quando os gates falharem.
