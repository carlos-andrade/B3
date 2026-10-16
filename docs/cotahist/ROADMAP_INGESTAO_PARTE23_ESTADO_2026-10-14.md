# B3 — ROADMAP DE INGESTÃO COTAHIST — PARTE23 (RECONCILIADO)

| Campo | Valor |
|---|---|
| **ID** | B3-COTAHIST-ROADMAP-PARTE23-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | ROADMAP |
| **Fase** | Atualização operacional e governança documental |
| **Estado** | EM_CURSO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | d5a796f99a9f227d078288415757e024bbab6ae853b172037f3faad75acb0225 |
| **Commit de referência (versão anterior)** | [b372140a1ead563b373e5eace26cb5e923d06642](https://github.com/carlos-andrade/B3/commit/b372140a1ead563b373e5eace26cb5e923d06642) |
| **Data de criação** | 2026-10-14 |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Responsável técnico B3 |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Evidências COTAHIST e workflows do repositório B3 |
| **Autoridade superior** | [Layout Mestre B3](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md); [Norma de cabeçalho GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Escopo** | Estado operacional PARTE23 e transição anual COTAHIST |
| **Objetivo** | Consolidar o estado comprovado e orientar a próxima atualização diária de 2026 |
| **Dependências** | Dataset Oficial V2, auditoria física 1986–2026, manifestos e workflows |

## Estado verificado no branch main

- RAW SHA-256: `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e`.
- NORMALIZED SHA-256: `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`.
- 3.142.910 registos, 25 campos; intervalo observado 2026-01-02 a 2026-10-13.
- FASE04/05: `VALIDADO`; hashes, manifestos e sidecars coerentes.
- FASE06: `VALIDADO`; reconciliação semântica integral dos 25 campos, zero divergências RAW × NORMALIZED.
- FASE07: `VALIDADO`; chave candidata ampliada sem colisões observadas neste ano; sem deduplicação ou remoção de linhas.
- FASE08: `VALIDADO_COM_EXCECAO`; zero bloqueadores. Exceções de ordenação/regressão por instrumento mantidas sem reordenar nem remover linhas.
- Gate 06–08: `APROVADO_COM_EXCECOES_NAO_BLOQUEANTES`, decisão `LIBERADO_PARA_FASE09`.
- FASE09: `LIBERADO_PARA_FASE10`, sem ausências nem bloqueadores. Run [38556379769](https://github.com/carlos-andrade/B3/actions/runs/38556379769) concluído com sucesso.
- FASE10: `VALIDADO_SEM_DIFERENCAS_DE_LINHAS`; 3.142.910 linhas de cada lado, zero linhas adicionadas/ausentes, multiplicidade integral preservada e nenhuma deduplicação.
- FASE11: `PROMOVIDO_COM_HASHES_COHERENTES`; hashes promovidos coincidem com as evidências revalidadas após a promoção.
- Auditoria do Layout Mestre: run [38556380160](https://github.com/carlos-andrade/B3/actions/runs/38556380160) concluído com sucesso.

## Auditoria física histórica 1986–2026 — atualização

**Resultado:** `APROVADO`. Foram auditados 41 anos; 41 validados, zero com falha. Em 1998, SHA-256 físico, sidecar e manifesto coincidem em `21b4740da8eb763259a0d859e261534de826449148c4d57d1f457f5721354e79`. Contagem física e manifesto: 104.971 linhas; 25 campos; zero datas inválidas e zero datas fora do ano. A execução [38576260466](https://github.com/carlos-andrade/B3/actions/runs/38576260466) concluiu com sucesso. O incidente está encerrado; não houve reescrita do CSV nem alteração dos dados RAW.

Evidência canónica: [AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json).

## Auditoria integrada pós-promoção

Evidência canónica: [COTAHIST_2026_AUDITORIA_INTEGRADA_POS_PROMOCAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_AUDITORIA_INTEGRADA_POS_PROMOCAO_V1.json).

**Resultado:** `APROVADO_COM_LIMITACOES_NAO_BLOQUEANTES`. A cadeia de hashes RAW/NORMALIZED, contagens, campos, datas, FASE04–FASE09, candidato FASE10 e promoção FASE11 está coerente. A FASE11 mantém no seu registo a decisão histórica `REEXECUTAR_FASES_04_08`, porque a promoção antecedeu a revalidação; a auditoria integrada documenta que as revalidações posteriores apresentam os mesmos hashes.

### Limitações explícitas

1. FASE04 é auditoria de integridade/documentação; a comparação independente integral dos 25 campos RAW × NORMALIZED é certificada pela FASE06.
2. A sequência física contém regressões temporais reportadas na FASE08. As linhas foram preservadas, sem reordenação ou deduplicação.
3. A fonte oficial foi persistida em `dados/cotahist/calendarios/B3_CALENDARIO_NEGOCIACAO_2026_V1.json`. O workflow comparou as 195 sessões observadas com as 195 sessões esperadas no intervalo e encontrou zero datas ausentes ou inesperadas. O resultado vale para o calendário geral e para o intervalo observado, não para o fecho anual nem para regras específicas de cada segmento.
4. A última data observada é 2026-10-13. Isto não constitui fecho anual de 2026.
5. A aprovação deste ciclo não certifica nem autoriza migração histórica 1986–2025.

## Roadmap operacional atualizado

| Ordem | Etapa | Estado | Próxima ação |
|---|---|---|---|
| 1 | Aquisição RAW 2026 | Concluída e identificada por hash | Monitorizar nova publicação oficial |
| 2 | FASE04–05 | Validadas após promoção | Reabrir apenas se RAW/NORMALIZED ou regras mudarem |
| 3 | FASE06 | Validada; 25 campos, zero divergências | Preservar evidência; não deduplicar |
| 4 | FASE07 | Validada; chave candidata ampliada sem colisões observadas | Não generalizar a conclusão para outros anos |
| 5 | FASE08 | Validada com exceções não bloqueadoras | Preservar sequência original e exceções; calendário validado separadamente |
| 6 | Gate 06–08 | Aprovado com exceções | Reabrir apenas se dados/regras mudarem |
| 7 | FASE09 | Liberada para FASE10; run success | Manter evidência atual; documento antigo fica histórico |
| 8 | FASE10 | Candidato validado sem diferenças | Não repetir sem mudança do candidato ou dos hashes |
| 9 | FASE11 | Promoção e hashes revalidados | Não repetir sem mudança do candidato ou das regras |
| 10 | Auditoria integrada pós-promoção | Concluída e persistida | Usar como estado consolidado deste ciclo |
| 11 | Fonte oficial do calendário B3 | Persistida e reconciliada | Preservar evidência e monitorizar futuras erratas oficiais |
| 12 | Auditoria calendário oficial 2026 | Concluída sem divergências | 195 sessões observadas = 195 esperadas; zero ausentes/inesperadas ([run](https://github.com/carlos-andrade/B3/actions/runs/38558710582)) |
| 13 | Persistência idempotente da evidência | Verificada com sucesso | Run [38558710582](https://github.com/carlos-andrade/B3/actions/runs/38558710582): comparação e persistência concluídas sem conflito |
| 14 | Fecho anual 2026 | Pendente | Aguardar fim do ano e publicação anual oficial |
| 15 | Histórico 1986–2025 | Encerrado para ingestão; somente consulta | Preservar RAW/NORMALIZED/manifestos; reabertura só por decisão formal |
| 16 | Auditoria física 1986–2026 | `APROVADO`; 41/41 anos validados, zero falhas (run [38576260466](https://github.com/carlos-andrade/B3/actions/runs/38576260466)) | Manter auditoria como gate de integridade e reexecutar quando CSV, sidecars ou regras de auditoria mudarem |
| 17 | Pipeline de atualização diária 2026 | Código e workflow atualizados; execução operacional validada sem conflitos | Verificar cada run diário, manifestos e dataset corrente |
| 18 | Dataset Oficial V2 | `PUBLICADO` — run [38577163285](https://github.com/carlos-andrade/B3/actions/runs/38577163285) concluído com sucesso; 41 anos incluídos (1986–2026), todos `VALIDADO`; JSON persistido no commit `74ead78`; artefacto da execução publicado | A integridade dos dados foi confirmada; a exceção de armazenamento LFS de 1987 está identificada e documentada em [INCIDENCIA_GIT_LFS_COTAHIST_A1987](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/INCIDENCIA_GIT_LFS_COTAHIST_A1987_2026-10-14.md): CSV de 15.518.211 bytes guardado como blob Git apesar da regra wildcard LFS, enquanto 1986 e 2026 são ponteiros LFS. Formalizar migração de armazenamento separadamente, preservando SHA-256 do conteúdo; não alterar agora o ficheiro histórico; manter gate fail-closed |

## Regras de integridade

- Não sobrescrever silenciosamente RAW/NORMALIZED.
- Não inventar execução, checksum ou resultado.
- Não deduplicar nem reordenar linhas para corrigir exceções da fonte.
- Não declarar o fecho anual de 2026 prematuramente.
- Preservar a auditoria antiga de atualidade como registo histórico; a evidência integrada atualiza o diagnóstico, não apaga o histórico.
- Não usar a aprovação 2026 como certificação semântica dos anos 1986–2025.
- Na atualização diária, alinhar a versão do manifesto com o parser efetivo e nunca substituir automaticamente RAW quando o hash da fonte de uma data existente divergir; persistir a incidência e falhar fechado.
- O workflow diário usa checkout sem materialização integral de Git LFS; o reconciliador do índice corrente depende de manifestos, não da leitura do CSV anual completo.

## Referências

- [Manifesto RAW](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/manifests/COTAHIST_A2026.json)
- [Manifesto NORMALIZED](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/normalized/manifests/COTAHIST_A2026_quality.json)
- [FASE04](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE04_NORMALIZACAO_V1.json)
- [FASE05](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE05_MANIFESTO_CHECKSUM_V1.json)
- [FASE06](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE06_RECONCILIACAO_V1.json)
- [FASE07](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE07_IDENTIDADE_CHAVES_V1.json)
- [FASE08](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE08_SEMANTICA_CALENDARIO_V1.json)
- [Gate 06–08](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_GATE_06_08_V1.json)
- [FASE09](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE09_PRE_RELEASE_V1.json)
- [FASE10](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE10_VALIDACAO_CANDIDATO_V1.json)
- [FASE11](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE11_PROMOCAO_V1.json)
- [Calendário oficial B3 2026 persistido](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/calendarios/B3_CALENDARIO_NEGOCIACAO_2026_V1.json)
- [Auditoria automatizada do calendário oficial — evidência](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_AUDITORIA_CALENDARIO_OFICIAL_V1.json)
- [Execução final da auditoria e persistência idempotente](https://github.com/carlos-andrade/B3/actions/runs/38558710582)
- [Auditoria de persistência idempotente — evidência JSON](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_AUDITORIA_PERSISTENCIA_IDEMPOTENTE_V1.json)
- [Auditoria pós-promoção complementar](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_AUDITORIA_POS_PROMOCAO_CALENDARIO_OFICIAL_V1.json)
- [Workflow de auditoria do calendário oficial](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-calendario-oficial-2026-v1.yml)
- [Auditoria histórica de atualidade](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md)

**Conclusão operacional:** o ciclo técnico COTAHIST 2026 está validado e promovido até 13/10/2026. A execução diária mais recente [38570797936](https://github.com/carlos-andrade/B3/actions/runs/38570797936) terminou com sucesso: a fonte de 14/10 ainda não estava publicada, os dados até 13/10 permaneceram inalterados e foram registados zero conflitos de hash. A reconciliação do índice corrente foi idempotente. A auditoria de conformidade dos workflows [38570797752](https://github.com/carlos-andrade/B3/actions/runs/38570797752) validou 550 workflows, zero divergências críticas e 143 observações não bloqueadoras. O calendário oficial foi reconciliado para o intervalo observado, sem divergências. O histórico 1986–2025 está congelado para consulta. A exceção histórica de 1998 foi resolvida: o sidecar foi alinhado ao SHA-256 confirmado pelo CSV e manifesto. A auditoria física completa terminou com sucesso no run [38576260466](https://github.com/carlos-andrade/B3/actions/runs/38576260466), com `APROVADO`, 41/41 anos validados e zero falhas. O incidente está encerrado; os dados CSV e manifestos históricos foram preservados. O Dataset Oficial V2 foi publicado com sucesso no run [38577163285](https://github.com/carlos-andrade/B3/actions/runs/38577163285). O gerador validou os 41 anos contra a auditoria física global canónica, sem criar certificados individuais artificiais. O ficheiro [COTAHIST_DATASET_OFICIAL_V2.0.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json) foi persistido no commit `74ead78`; contém o período 1986–2026, estado `VIGENTE`, origem de certificação na auditoria física global e `fail_closed: true`. O artefacto `cotahist-dataset-oficial-v2` foi carregado (SHA-256 do ZIP: `974d6cdec48b38ae3922055f0d0b62037144cc88125903a8f97f522b3e26d778`). A auditoria de conformidade do Layout Mestre também passou no run [38577163321](https://github.com/carlos-andrade/B3/actions/runs/38577163321). Foi investigado e documentado em [INCIDENCIA_GIT_LFS_COTAHIST_A1987](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/INCIDENCIA_GIT_LFS_COTAHIST_A1987_2026-10-14.md) o aviso não bloqueante de Git LFS: a árvore Git confirma que `dados/cotahist/normalized/anual/COTAHIST_A1987.csv` está guardado como blob Git de 15.518.211 bytes, embora `.gitattributes` aplique a regra LFS a todos os CSV anuais; os ficheiros A1986 e A2026 estão representados por ponteiros LFS de 133/134 bytes. A geração V2 e a auditoria física passaram, pelo que isto é uma inconsistência de armazenamento/histórico, não uma falha de hash observada no dataset. Não migrar automaticamente: planear uma alteração controlada do armazenamento e provar que o SHA-256 do conteúdo permanece idêntico. O fecho anual 2026 permanece pendente até ao fim do ano.

## Adenda operacional — revalidação retrospectiva 1994 (2026-10-14)

- **FASE03:** reexecutada e validada no run [38582977979](https://github.com/carlos-andrade/B3/actions/runs/38582977979); evidência persistida em [COTAHIST_1994_FASE03_PARSING_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_1994_FASE03_PARSING_V1.json).
- **Resultado:** 119.099 registos estruturais, dos quais 119.097 tipo `01`, 1 header `00` e 1 trailer `99`; 245 bytes por registo; zero comprimentos inválidos e zero datas inválidas; intervalo de cotações 1994-01-03 a 1994-12-29.
- **Integridade:** SHA-256 RAW permanece `b3bbd8e8d290c36943398c6f99a04e0721db2ebac3b917904df9efaacf3172eb`, igual ao valor da FASE01. Decisão `LIBERADO_PARA_FASE04`.
- **Fases seguintes:** as evidências existentes FASE04–FASE12 foram inspecionadas; FASE04–07 e FASE09–12 permanecem consistentes com os hashes RAW/NORMALIZED já registados; FASE08 está `VALIDADO_COM_EXCECAO`, sem alterar nem reordenar dados. Não se reexecutou a normalização histórica porque 1994 pertence ao histórico encerrado e as evidências existentes já documentam os mesmos hashes.
- **Correção operacional:** removido o cron `*/5 * * * *` do workflow [cotahist-fase03-parsing-1994-v1.yml](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase03-parsing-1994-v1.yml), que provocava revalidações periódicas desnecessárias e atualizações repetidas do timestamp. Permanecem `workflow_dispatch` e gatilhos `push` específicos.
- **Commit da correção do cron:** [54425d583a07ef9caef481e7e9425fe48bd33be1](https://github.com/carlos-andrade/B3/commit/54425d583a07ef9caef481e7e9425fe48bd33be1).
- **Auditoria pós-correção:** Layout Mestre concluído com sucesso no run [38583879502](https://github.com/carlos-andrade/B3/actions/runs/38583879502), commit auditado `54425d583a07ef9caef481e7e9425fe48bd33be1`. A reexecução FASE03 acionada pelo push terminou com sucesso no run [38583879352](https://github.com/carlos-andrade/B3/actions/runs/38583879352); a evidência foi persistida no commit `917c0caf3955fd05c829790c4edb08c476705421`.
- **Controlo anti-loop:** removido o cron de cinco minutos; o workflow só responde a execução manual ou alterações nos paths explicitamente listados. A evidência FASE03 não consta dos paths do gatilho `push`, pelo que o commit gerado pela própria execução não dispara outra execução. O teste pós-correção concluiu com sucesso; não é necessário rerun adicional.
- **Próximos passos:** manter a migração de armazenamento Git LFS do CSV 1987 isolada e pendente até ser possível provar preservação byte a byte e disponibilidade do objeto LFS; continuar a atualização diária de 2026 sem tocar nos anos históricos.


## Adenda de continuidade — preparação da migração LFS A1987 (2026-10-14)

- **Implementação direta:** o proprietário informou que o repositório desativou Pull Requests. Para não bloquear o trabalho, os ficheiros de controlo foram publicados diretamente em `main` por commits normais de avanço, sem reescrita de histórico.
- **Anti-loop:** workflow exclusivamente manual (`workflow_dispatch`), sem cron e sem gatilho push. Modo predefinido `preflight`; migração exige escolha manual de `migrate`.
- **Gates:** hash SHA-256, tamanho, linhas, 25 campos e datas antes da alteração; ponteiro LFS com OID/tamanho esperados; checkout limpo após push; revalidação física global e regeneração do Dataset Oficial V2.
- **Estado real:** workflow integrado em `main`, mas ainda não executado. Nenhum CSV ou manifesto foi alterado pela preparação. A incidência de armazenamento A1987 permanece aberta até evidência pós-migração aprovada.
- **Próximo passo:** executar primeiro `preflight`; executar `migrate` somente depois de analisar o log de preflight. Não repetir workflows concluídos sem mudança de código/dados.


## Atualização final — migração Git LFS A1987 (2026-10-14)

**Estado atual da incidência: RESOLVIDA COM EVIDÊNCIA.** Esta adenda substitui apenas o estado operacional anterior da incidência LFS; os registos anteriores permanecem como histórico.

- Workflow manual [38591026646](https://github.com/carlos-andrade/B3/actions/runs/38591026646): `success`, modo `migrate`; todas as etapas, incluindo as pós-migração, concluídas com sucesso.
- Commit da migração do CSV A1987: [e8c6bf21eeba789b763a9c88d6433dabe8b31b9a](https://github.com/carlos-andrade/B3/commit/e8c6bf21eeba789b763a9c88d6433dabe8b31b9a).
- Representação Git confirmada como ponteiro LFS de 133 bytes; OID `sha256:5dd255d8164ab321fe577d0cac0b4c1ee94b590d785343202762036786adffcc`; tamanho do objeto 15.518.211 bytes.
- Checkout limpo e materialização do objeto LFS validados: SHA-256 idêntico, 130.665 linhas de dados, 25 campos, primeira data 1987-01-02 e última 1987-12-30.
- Auditoria física global pós-migração: `APROVADO`, 41 anos auditados, 41 validados, zero falhas. Evidência canónica: [AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json).
- Dataset Oficial V2 regenerado após a auditoria, incluindo 41 anos: [COTAHIST_DATASET_OFICIAL_V2.0.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json). As evidências geradas já coincidiam com as canónicas, portanto não foi necessário novo commit de evidência.
- Incidência detalhada encerrada em [INCIDENCIA_GIT_LFS_COTAHIST_A1987_2026-10-14.md](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/INCIDENCIA_GIT_LFS_COTAHIST_A1987_2026-10-14.md).

### Roadmap imediato

| Etapa | Estado | Decisão |
|---|---|---|
| Migração controlada da representação A1987 para Git LFS | Concluída | Conteúdo preservado; sem reescrita de histórico |
| Checkout limpo + SHA/bytes/linhas/campos/datas | Aprovado | Hash antes/depois idêntico |
| Auditoria física global 1986–2026 | Aprovada | 41/41 anos; zero falhas |
| Regeneração Dataset Oficial V2 | Concluída | 41 anos incluídos; estado vigente |
| Fecho da incidência LFS A1987 | Concluído | Não repetir sem nova evidência de anomalia |
| Ingestão histórica 1986–2025 | Congelada para consulta | Não alterar no ciclo diário |
| Atualização diária 2026 | Ativa | Continuar a validar cada publicação e preservar fail-closed |
| Fecho anual 2026 | Pendente | Só após fim do ano e publicação anual oficial |


## Adenda operacional — atualização diária até 2026-10-15 (2026-10-16)

A execução [COTAHIST importação diária run 38889032782](https://github.com/carlos-andrade/B3/actions/runs/38889032782) concluiu com sucesso em 2026-10-16. O relatório `dados/cotahist/quality/diario/execucoes/COTAHIST_DIARIO_EXECUCAO_20261016T013436Z.json` registou `2026-10-15: IMPORTED`, `2026-10-14: UNCHANGED`, `2026-10-13: UNCHANGED` e zero conflitos. O manifesto diário de 15/10 está `VALIDADO`, com 18.827 registos e 25 campos; SHA-256 RAW `346a8ec8ab89db34c5ff2388246d6f658a5e04d989fd549d0ba57e52d90967c8`, SHA-256 NORMALIZED `e67473ac5c636f98c755094be50e66e14eeb124b28cb2b503c3384373c00bef0`. O Dataset Corrente V1.1 passou a apontar para 15/10/2026, combinando o snapshot anual imutável até 13/10 com os incrementos diários validados de 14 e 15/10. O histórico 1986–2025 permanece congelado.

## Governação documental — adoção da norma transversal

Este documento foi normalizado para a norma de cabeçalho da GOVERNANCA v1.0.3. A normalização não altera as evidências de dados citadas nem substitui os JSON canónicos.

- Plano de adoção: [PLANO_NORMALIZACAO_DOCUMENTAL_GOVERNANCA_V1.md](../governanca/PLANO_NORMALIZACAO_DOCUMENTAL_GOVERNANCA_V1.md)
- Incidência Git LFS A1987 encerrada com evidência: [INCIDENCIA_GIT_LFS_COTAHIST_A1987_2026-10-14.md](../ingestao/INCIDENCIA_GIT_LFS_COTAHIST_A1987_2026-10-14.md)
