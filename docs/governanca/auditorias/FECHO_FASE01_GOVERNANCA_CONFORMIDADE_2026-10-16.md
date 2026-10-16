# Relatório de execução — Fase 01: governação e conformidade

| Campo | Valor |
|---|---|
| **ID** | B3-GOV-FASE01-FECHO-20261016 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_FECHO_FASE_GOVERNANCA |
| **Fase** | FASE 01 — Governação e conformidade |
| **Estado** | CONCLUIDA_COM_EVIDENCIA; GATES_RESIDUAIS_OPERACIONAIS_MANTIDOS_FAIL_CLOSED |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 0e5b156cba4ae6a1ec765202066d273cfec702742dd57c689e57efea6c0e1511 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Proprietário do repositório — validação formal final não inferida por automação |
| **Origem** | Revisão dos artefactos versionados, registos de decisão e execuções GitHub Actions |
| **Autoridade superior** | [Carta Magna B3](../../CARTA_MAGNA_GOVERNANCA_B3.md); [Layout Mestre Canónico B3](../layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Governação central](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Controlos inválidos, reconciliação GOV-DIV-001, revisão de conteúdo original e integridade documental |
| **Objetivo** | Registar a resolução verificável dos controlos de governação da Fase 01 e distinguir o fecho documental de pendências operacionais |
| **Dependências** | Matriz semântica integral; decisão GOV-DIV-001; auditoria SHA-256; registos de licenciamento e workflows |

## 1. Resultado executivo

A Fase 01 fica **documentalmente concluída com evidência**, sem declarar que todo o projeto B3 está concluído. Os controlos de governação identificados foram reconciliados, a cadeia normativa foi corrigida no Plano Mestre e os bloqueios operacionais que ainda dependem de terceiros ou de execução técnica permanecem separados e sujeitos a `FAIL_CLOSED`.

Esta conclusão não equivale a aprovação formal do proprietário, licença externa, certificação de dados COTAHIST, nem confirmação de que todas as execuções históricas foram bem-sucedidas.

## 2. Controlos resolvidos

### 2.1 Controlo inválido 225

O registo anterior identifica o controlo como encerrado, com 302/302 conformes, zero inválidos e zero divergências de hashes, associado ao commit `1e1870479431f49d4786fa89afbd41e4c40f60c0`. Esta evidência é preservada como resultado histórico do controlo, não como prova isolada do estado atual de todos os ficheiros.

A validação documental atual é suportada adicionalmente pela auditoria SHA-256 do commit `5ac103c3eca0cc820e759a41e53931f625796734`, execução [38894914716](https://github.com/carlos-andrade/B3/actions/runs/38894914716), cujo log reporta 332 ficheiros analisados, 332 `CONFORME`, zero pendentes, zero divergentes e zero hashes em formato inválido. A auditoria é somente de leitura.

### 2.2 Divergência GOV-DIV-001

A decisão normativa [B3-DEC-GOV-DIV-001](../decisoes/DECISAO_GOV_DIV_001_HIERARQUIA_NORMATIVA_B3_V1.md) estabelece autoridade por domínio:

1. Carta Magna — princípios constitucionais, competências e limites de autoridade.
2. Layout Mestre — especificação operacional dentro dos limites da Carta Magna.
3. Cartas de domínio e políticas — garantias e regras do domínio, reconciliadas com a autoridade superior.
4. Contratos técnicos — concretização das regras aprovadas.
5. Procedimentos, implementação e evidências — execução ou demonstração, sem autoridade normativa autónoma.

A regra de conflito é `FAIL_CLOSED` para a decisão afetada, com reconciliação versionada antes de alterar código ou workflows. O histórico anterior é preservado.

### 2.3 Fila original de 281 revisões

O relatório [Fecho da revisão das 281 pendências](REVISAO_SEMANTICA_PENDENCIAS_281_FECHO_2026-10-15.md) regista 281 documentos revistos em 22 lotes (05–26), com zero itens remanescentes na fila original `PENDENTE_REVISAO_DE_CONTEUDO`.

A revalidação dos 17 documentos prioritários após GOV-DIV-001 e a reconciliação dos Lotes 01–04 estão documentadas em [REVALIDACAO_SEMANTICA_POS_GOV_DIV_001_LOTES_01_A_04_2026-10-16.md](REVALIDACAO_SEMANTICA_POS_GOV_DIV_001_LOTES_01_A_04_2026-10-16.md). A fila original está fechada; ações operacionais encontradas durante a revisão não são automaticamente consideradas resolvidas.

### 2.4 Cadeia normativa do Plano Mestre

Foi corrigido o cabeçalho e as referências à cadeia de autoridade em `docs/PLANO_MESTRE_DE_EXECUCAO.md`, atualizando o documento para a versão 2.1.0 e substituindo a cadeia legada `PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO` por:

`CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS`

Alteração registada no commit [0a23dc9c3127e51c923b3b5b70364db7b951d144](https://github.com/carlos-andrade/B3/commit/0a23dc9c3127e51c923b3b5b70364db7b951d144).

## 3. Gates e limites ainda ativos

| Tema | Estado | Regra de controlo |
|---|---|---|
| Hashes documentais no commit auditado | 332/332 conformes no run 38894914716 | Reauditar após cada alteração documental |
| Licenças/autorização dos endpoints B3 | Parcial; autorizações externas pendentes | Não iniciar novas recolhas/publicações nos endpoints bloqueados |
| B3 Pesquisa por Pregão | Recolha automatizada proibida pela fonte citada no registo | Captura desativada; não contornar por endpoint interno |
| Git LFS COTAHIST A1987 | Fora do escopo desta fase; preflight obrigatório | Não migrar sem preflight do runbook |
| Capturas RAW e reconciliações | Pendências operacionais individualizadas | Não promover dados sem proveniência e reconciliação |
| WATCHDOG e falhas de workflows | Requerem acompanhamento próprio | Não confundir sucesso de hash documental com sucesso funcional dos workflows |

A evidência de licenciamento e o estado por endpoint estão em [REGISTRO_LICENCAS_AUTORIZACAO_ENDPOINTS_B3_2026-10-16.md](../licenciamento/REGISTRO_LICENCAS_AUTORIZACAO_ENDPOINTS_B3_2026-10-16.md). A existência técnica de um endpoint não constitui autorização para recolha, armazenamento público ou redistribuição.

## 4. Critérios de aceitação desta fase

- [x] O controlo 225 tem resultado histórico explícito e rastreável.
- [x] GOV-DIV-001 está formalizado e a hierarquia por domínio está expressa na Carta Magna.
- [x] O Plano Mestre foi alinhado à cadeia normativa canónica e versionado.
- [x] A fila original das 281 revisões foi encerrada por lotes documentados.
- [x] Os 17 documentos prioritários foram revalidados e os relatórios 01–04 receberam reconciliação posterior.
- [x] Existe auditoria SHA-256 com resultado observável de 332/332 conformes para o commit indicado.
- [x] As pendências de licenciamento e execução foram separadas e mantidas sob `FAIL_CLOSED`.
- [ ] Aprovação formal final do proprietário deste relatório — não inferida a partir de commits ou workflows.

## 5. Decisão de governação

A Fase 01 está concluída no âmbito dos controlos documentais definidos neste relatório, com uma aprovação formal final ainda não presumida. A conclusão não libera as fases seguintes para ignorar gates próprios. A migração Git LFS, a certificação COTAHIST, a autorização de fontes e as reconciliações RAW continuam a exigir os respetivos runbooks, evidências e critérios de aceitação.

Nenhuma evidência histórica deve ser reescrita para fazer parecer que uma decisão posterior já existia. Nenhum estado `EXISTE`, `ÍNTEGRO`, `VALIDADO`, `CERTIFICADO` ou `FECHADO` pode ser inferido de outro sem a respetiva evidência.
