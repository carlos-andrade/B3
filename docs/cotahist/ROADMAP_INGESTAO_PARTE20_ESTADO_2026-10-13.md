# B3 — A BOLSA DO BRASIL
## PARTE20 — Roadmap de ingestão e certificação COTAHIST
**Data de referência:** 2026-10-13  
**Repositório oficial:** https://github.com/carlos-andrade/B3  
**Branch:** main  
**Estado geral:** EM EXECUÇÃO CONTROLADA  
**Norma operacional:** docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md

## 1. Objetivo
Dar continuidade à PARTE19 com base nas evidências efetivamente persistidas no repositório. Este documento corrige a prioridade operacional que aparecia no roadmap anterior: em 13/10/2026, o ciclo ativo observado é COTAHIST 2014, não 2010. Não declarar execução de workflow ou alteração de dados sem run/artefato verificável.

## 2. Estado confirmado do COTAHIST 2014
Evidências consultadas na branch principal em 13/10/2026:

- FASE00–FASE03: VALIDADO.
- RAW tipo 01: 392.228 registos; hash RAW registrado como `613d76f8a64c7ffba0406cb54c1fd187266f55ed8b6037cb85993b2071a5aae7`.
- FASE02: ZIP com um membro e zero erros estruturais.
- FASE03: 392.228 registos, zero datas inválidas/fora do ano e zero comprimentos inválidos.
- FASE04: NORMALIZED regenerado e validado independentemente, 392.228 linhas e 25 campos; hash NORMALIZED `af95fc567d875a2ba09221f4749cddae22281baf36145e9066021e2d13533c01`.
- FASE05: VALIDADO.
- FASE06: VALIDADO; 392.228 registos RAW e NORMALIZED, 12 campos críticos comparados, zero divergências. A evidência adia explicitamente a avaliação de unicidade da chave para a FASE07.
- Último artefato FASE06: `dados/cotahist/quality/COTAHIST_2014_FASE06_RECONCILIACAO_V1.json`.
- Commit de evidência: https://github.com/carlos-andrade/B3/commit/6f11ade95b9abf7be2b24bf56d622b9d76a566a1
- Commit que registra FASE05/FASE06 e atualiza o roadmap anterior: https://github.com/carlos-andrade/B3/commit/6d30a7e25caca3fe42f284f6a1126d059cedf6dd

## 3. Próxima fase autorizada
### FASE07 — identidade, chaves e cardinalidade — 2014
Estado: **VALIDADO — evidência persistida**.

- Workflow: `.github/workflows/cotahist-fase07-identidade-2014-v1.yml`.
- Evidência: `dados/cotahist/quality/COTAHIST_2014_FASE07_IDENTIDADE_CHAVES_V1.json`.
- Commit da evidência: `23a169b05c5efe088260b57fbe8f17473ef09529`.
- Hash da evidência no repositório: `6c58bce7fc42fd4cae7ef503dcfffabe9d99d53e`.
- Registos analisados: 392.228; hash NORMALIZED coincide com a FASE06: `af95fc567d875a2ba09221f4749cddae22281baf36145e9066021e2d13533c01`.
- Chave-base: 6.856 grupos duplicados, 15.155 linhas excedentes; nenhum grupo era composto por linhas integralmente idênticas.
- Chave candidata com `prazot`: 392.228 chaves distintas, zero colisões.
- `deduplication_performed=false`; `source_rows_removed=0`.

A evidência está persistida e os seus campos/contagens foram conferidos contra a FASE06. O endpoint disponível nesta sessão não expõe uma listagem geral dos runs; por isso, o estado do run é inferido do artefato produzido e commitado pelo workflow, e não de uma consulta direta ao painel de execuções.

Pré-condições:
1. consumir o NORMALIZED e o hash fixados pela FASE06;
2. consumir a evidência FASE06 em modo somente leitura;
3. seguir o Layout Mestre e a regra de existência/validação;
4. não deduplicar nem remover linhas;
5. avaliar a chave candidata com base em colisões, campos do layout, amostras e análise dos registos colidentes;
6. não generalizar automaticamente a chave observada em 2006 para 2014;
7. persistir evidência própria de 2014 com contagens, hashes, colisões, decisão, limitações e timestamp;
8. executar validação independente antes de promover o status.

A chave candidata usada em 2006 incluiu `prazot` para separar colisões, mas a evidência de 2006 não autoriza deduplicação nem generalização automática para outros anos.

## 4. Roadmap por marco

| Marco | Estado verificado | Próxima ação |
|---|---|---|
| COTAHIST 1986–2003 | Histórico com exceções específicas por ano | Preservar evidências; não presumir uniformidade |
| COTAHIST 2004–2013 | Ciclos anteriores registrados como concluídos/fechados, com exceções de calendário documentadas por ano | Não reexecutar sem causa/evidência |
| COTAHIST 2010 | FASE00–FASE12 concluídas; FASE11 certificado; FASE12 fechado com transição controlada | Preservar exceção de calendário oficial histórico não persistido |
| COTAHIST 2014 | FASE00–FASE07 validadas; workflow FASE08 publicado em `main` (commit `013100f0e271988c37b1edad58cf77a1d01f2f3b`) | Verificar evidência/run FASE08; não avançar sem resultado auditável |
| COTAHIST 2014 FASE08–FASE12 | Ainda não comprovadas como concluídas nesta continuação | Avançar sequencialmente após cada gate |
| REC-001 B3 × BLOOMBERG_MAIL | Promoção bloqueada por variação de ordem e diferença de multiplicidades | Reconciliar por data os 151.071 registos adicionais e classificar a variação de ordem |
| Auditoria de workflows | Correção de persistência após push concorrente registrada; fila final ainda precisa de confirmação independente | Verificar execuções recentes antes de declarar fila limpa |
| Dataset oficial / certificação anual | README anterior registra execuções bem-sucedidas; esta continuação não reexecutou esses workflows | Revalidar matriz, manifestos e hashes antes de qualquer nova declaração |

## 5. REC-001 — estado e bloqueio
A evidência consolidada no commit de 13/10 registra:
- snapshot B3: 2.919.760 registos tipo 01;
- RAW BLOOMBERG_MAIL: 3.070.831 registos tipo 01;
- diferença de multiplicidades: 151.071 registos;
- zero registos do snapshot B3 ausentes no RAW BLOOMBERG_MAIL na reconciliação por multiconjunto SHA-256;
- primeira divergência de ordem na posição 222.003, entre `ABCBA235` e `ABCBA243`, cujos payloads foram descritos como idênticos, mas aparecem em ordem inversa.

Estado de promoção: **BLOCKED_ORDER_VARIANCE_REVIEW**.

Não classificar os 151.071 registos como mera extensão temporal sem reconciliação por data. Não afrouxar a comparação, não sobrescrever RAW e não promover o dataset enquanto a classificação estiver pendente.

## 6. Ordem de execução
1. FASE07 de 2014: evidência persistida e conferida; 392.228 registos, zero colisões na chave candidata com `prazot`, nenhuma linha removida.
2. FASE08 de 2014: workflow publicado em `main`; validar se a execução automática foi disparada pelo push e procurar a evidência `dados/cotahist/quality/COTAHIST_2014_FASE08_SEMANTICA_CALENDARIO_V1.json`.
3. Não declarar FASE08 concluída até conferir a evidência, hashes, contagens e estado/decisão. Se não houver evidência, investigar o run e executar manualmente pelo mecanismo autorizado.
4. Só após FASE08 auditada, avaliar o Gate 06–08 e autorizar FASE09 conforme as dependências do Layout Mestre.
5. Em trilha separada, investigar REC-001; não permitir que esse bloqueio seja contornado pela certificação anual.

## 7. Regras de governança
- Ordem documental: **correção → cartas normativas → evidências/incidentes → verificação → README**.
- Fases são unidirecionais, monotônicas e isoladas.
- A fase posterior consome evidências anteriores em modo somente leitura.
- Ausência de artefato em busca ampla não prova ausência; verificar primeiro o caminho canônico.
- Workflow SUCCESS não equivale a validação de negócio.
- Não declarar execução, publicação ou certificação sem evidência verificável.
- Não alterar RAW nem fazer deduplicação para forçar concordância.
- Qualquer falha deve ser corrigida na fase de origem.

## 8. Registro desta continuação
A FASE07 de 2014 foi verificada pela evidência persistida `dados/cotahist/quality/COTAHIST_2014_FASE07_IDENTIDADE_CHAVES_V1.json`: 392.228 registos, 377.073 chaves-base distintas, 6.856 grupos duplicados na chave-base, 392.228 chaves candidatas distintas com `prazot`, zero colisões candidatas e zero linhas removidas. Evidência commit `23a169b05c5efe088260b57fbe8f17473ef09529`.

A FASE08 foi publicada em `.github/workflows/cotahist-fase08-calendario-2014-v1.yml`, commit `013100f0e271988c37b1edad58cf77a1d01f2f3b`. O workflow foi adaptado do contrato anual de 2013, com referências de ano e caminhos de 2014; o trigger contempla mudanças no próprio workflow, nas evidências FASE06/FASE07 e no NORMALIZED 2014. A leitura do ficheiro publicado confirmou a ausência de referências residuais a 2013. A execução automática deve ocorrer pelo evento de push, mas **o resultado do run e a evidência FASE08 ainda não foram confirmados nesta consulta**. Próximo passo: localizar o artefato persistido e validar a execução antes de avançar para o Gate 06–08. A REC-001 continua bloqueada.

