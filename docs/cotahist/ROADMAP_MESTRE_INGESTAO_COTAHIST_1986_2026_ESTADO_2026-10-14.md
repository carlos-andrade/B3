# B3 — ROADMAP MESTRE DE INGESTÃO COTAHIST 1986–2026
**Data de referência:** 2026-10-14  
**Repositório oficial:** https://github.com/carlos-andrade/B3  
**Branch:** main  
**Estado global:** **CICLO OPERACIONAL VALIDADO — CONTINUIDADE ANUAL GOVERNADA**  
**Norma operacional:** `docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md`

> Este roadmap cobre exclusivamente o projeto B3: ingestão COTAHIST, normalização, qualidade, calendário, certificação anual, dataset oficial, workflows e governança. Não substitui as evidências JSON de cada fase.

## 1. Resumo executivo

### Concluído e verificado
- A matriz estrutural anual cobre **41 anos (1986–2026)**: RAW presente, manifesto de qualidade presente, estado `VALIDADO`, 25 campos, zero datas inválidas e zero datas fora do ano, conforme a matriz vigente de normalização.
- Há evidências de fases anuais de ingestão, reconciliação independente, certificação e fechamento/transição para múltiplos anos, incluindo FASE10/11/12 para 1999–2025 e artefatos específicos para os anos anteriores. **A certificação estrutural agregada não significa que todos os anos tenham semântica histórica plenamente certificada.**
- COTAHIST 2026 foi normalizado, reconciliado e promovido internamente até **13/10/2026**; os hashes RAW/NORMALIZED e manifestos estão coerentes.
- O calendário geral oficial B3 foi persistido e reconciliado para o intervalo observado de 2026: **195 sessões observadas = 195 esperadas; zero datas ausentes e zero inesperadas**.
- A persistência idempotente da evidência do calendário foi validada; execução final e auditoria do Layout Mestre concluídas com sucesso.
- A sequência original de registos foi preservada: sem deduplicação, remoção ou reordenação.

### Estado atual e limites residuais
1. **Matriz anual certificada automaticamente**: workflow [38570114992](https://github.com/carlos-andrade/B3/actions/runs/38570114992) concluído com sucesso; 41 anos presentes e linha 2026 sincronizada com parser 1.1.2 e 3.142.910 linhas.
2. **Dataset Oficial V1 gerado/validado**: workflow [38570165775](https://github.com/carlos-andrade/B3/actions/runs/38570165775) concluído com sucesso; 41 registos anuais, incluindo 2026 até 13/10.
3. **Auditoria de workflows concluída**: 550 workflows avaliados, zero divergências críticas, 407 conformes sem observações e 143 conformes com observações. Run [38570189171](https://github.com/carlos-andrade/B3/actions/runs/38570189171).
4. **Testes operacionais BDI e WATCHDOG concluídos**: [captura BDI](https://github.com/carlos-andrade/B3/actions/runs/38561123974) e [validação WATCHDOG](https://github.com/carlos-andrade/B3/actions/runs/38561328911) terminaram com sucesso.
5. **O ano de 2026 permanece parcial**, atualizado até 13/10/2026. O fecho anual só pode ocorrer após o fim do ano e a aquisição/validação da fonte anual final.
6. A exceção semântica histórica de 1986 permanece controlada; não declarar equivalência semântica plena de todo o período 1986–2026.
7. Exceções de calendário histórico de anos antigos e de ordenação/regressão permanecem documentadas; não corrigir a fonte reordenando ou removendo linhas.

## 2. Estado canónico COTAHIST 2026

- RAW SHA-256: `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e`
- NORMALIZED SHA-256: `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`
- Registos tipo 01: **3.142.910**; campos NORMALIZED: **25**.
- Intervalo: **2026-01-02 a 2026-10-13**.
- RAW e NORMALIZED sem mutação após as auditorias finais; zero deduplicação, zero linhas removidas, zero reordenação.
- Manifesto RAW: [COTAHIST_A2026.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/manifests/COTAHIST_A2026.json).
- Manifesto NORMALIZED: [COTAHIST_A2026_quality.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/normalized/manifests/COTAHIST_A2026_quality.json).

### Fases 2026

| Etapa | Estado verificado | Decisão/observação |
|---|---|---|
| Aquisição RAW e integridade da fonte | VALIDADO | ZIP íntegro; checksum canónico persistido |
| FASE04 — normalização/integridade | VALIDADO após revalidação pós-promoção | Hashes e manifestos coerentes |
| FASE05 — manifesto/checksum | VALIDADO | RAW/NORMALIZED coerentes |
| FASE06 — reconciliação semântica | VALIDADO | 25 campos; zero divergências RAW × NORMALIZED |
| FASE07 — identidade/chaves | VALIDADO | Chave candidata sem colisões observadas neste ano; não generalizar para outros anos |
| FASE08 — semântica/calendário | VALIDADO COM EXCEÇÕES NÃO BLOQUEADORAS | Exceções de ordenação/regressão preservadas; sem alterar linhas |
| Gate 06–08 | APROVADO COM EXCEÇÕES NÃO BLOQUEADORAS | Liberado para FASE09 |
| FASE09 — pre-release | LIBERADO PARA FASE10 | Sem ausências nem bloqueadores |
| FASE10 — validação independente do candidato | VALIDADO SEM DIFERENÇAS DE LINHAS | 3.142.910 de cada lado; zero linhas adicionadas/ausentes; multiplicidade preservada |
| FASE11 — promoção controlada | PROMOVIDO COM HASHES COERENTES | Revalidações posteriores confirmaram os hashes; a decisão histórica de reexecutar FASE04–08 permanece registrada |
| Calendário oficial B3 | VALIDADO NO INTERVALO OBSERVADO | 195/195 sessões; zero ausentes/inesperadas |
| Persistência idempotente | VALIDADA | Run [38558710582](https://github.com/carlos-andrade/B3/actions/runs/38558710582) |
| Fecho anual 2026 | PENDENTE | Aguardar fim do ano e fonte final |

### Evidências principais de 2026
- [Roadmap operacional PARTE23](https://github.com/carlos-andrade/B3/blob/main/docs/cotahist/ROADMAP_INGESTAO_PARTE23_ESTADO_2026-10-14.md)
- [FASE06 — reconciliação](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE06_RECONCILIACAO_V1.json)
- [FASE10 — validação independente](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE10_VALIDACAO_CANDIDATO_V1.json)
- [FASE11 — promoção](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_FASE11_PROMOCAO_V1.json)
- [Calendário oficial B3 2026](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/calendarios/B3_CALENDARIO_NEGOCIACAO_2026_V1.json)
- [Auditoria calendário oficial](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_AUDITORIA_CALENDARIO_OFICIAL_V1.json)
- [Auditoria persistência idempotente](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_AUDITORIA_PERSISTENCIA_IDEMPOTENTE_V1.json)
- [Auditoria Layout Mestre](https://github.com/carlos-andrade/B3/actions/runs/38558710892)

## 3. Certificação estrutural anual 1986–2026

Fonte: [Documento de certificação anual](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/CERTIFICACAO_ANUAL_COTAHIST_1986_2026_V1.0.md) e [matriz CSV](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv).

- Resultado estrutural reportado pela matriz: **41/41 anos** com manifesto, estado `VALIDADO`, 25 campos, zero datas inválidas e zero datas fora do ano.
- **1986:** mantém `CERTIFICADO_NORMALIZACAO_COM_EXCECAO_SEMANTICA`; não equivale a certificação semântica plena.
- **1998:** parser `1.1.1`; a lista de versões aceites deve continuar explicitamente homologada, sem inferir equivalência apenas pelo número da versão.
- **2026:** a linha da matriz foi sincronizada com o manifesto canónico de 14/10/2026 (parser 1.1.2; 3.142.910 linhas). Revalidar contagem, datas, parser e hash em cada atualização diária.
- Esta matriz certifica estrutura/normalização; não certifica por si só completude económica por pregão, semântica universal dos códigos, calendário oficial histórico de cada ano nem aptidão para uma estratégia.

## 4. Histórico de fases e transições

A árvore `dados/cotahist/quality/` contém artefactos por ano para reconciliação, validação independente, certificação e fechamento/transição. A lista de ficheiros e o respetivo conteúdo devem prevalecer sobre qualquer resumo textual antigo.

| Período | Estado consolidado que pode ser afirmado | Limite |
|---|---|---|
| 1986–1987 | RAW/NORMALIZED e reconciliações históricas específicas persistidos; evidências próprias de calendário/semântica/raw-normalized | 1986 mantém exceção semântica; confirmar fase a fase antes de afirmar certificação integral FASE00–12 |
| 1988–1998 | Artefactos de integridade/reconciliação e transições históricas existentes; 1998 tem tratamento específico de parser/OHLC/semântica | Não presumir uniformidade das fases ou do calendário oficial histórico |
| 1999–2005 | Fechamentos anuais/transições e FASE10/11/12 persistidos para os anos indicados nos artefactos; evidência independente de 25 campos em vários anos | Preservar exceções de calendário e semântica de cada ano |
| 2006–2013 | Cadeia de fases anuais e artefactos de FASE10/11/12 persistidos; reconciliações independentes reportadas sem divergências nos anos documentados | Gate e estado devem ser lidos na evidência de cada ano; calendário histórico oficial pode não estar persistido |
| 2014–2025 | Existem evidências anuais de FASE06, FASE10, FASE11 e FASE12 para os anos listados no repositório; a documentação recente regista validações independentes e transições controladas | A presença de um ficheiro não substitui a inspeção do seu status/hash; exceções continuam válidas até serem resolvidas por evidência |
| 2026 | FASE04–11, Gate 06–08, calendário oficial do intervalo observado e persistência idempotente concluídos | Ano parcial; fecho anual pendente; matriz anual e artefactos agregados requerem sincronização final |

**Regra de encerramento por ano:** um ano só pode ser declarado fechado quando a sua própria FASE12 e todas as pré-condições requeridas estiverem validadas e persistidas. A existência de RAW, NORMALIZED ou manifesto não substitui o fechamento.

## 5. Auditoria final interna do projeto B3

O encerramento deste roadmap é determinado exclusivamente pela integridade dos dados e artefactos mantidos no repositório B3. Os critérios são: coerência entre RAW, NORMALIZED, manifestos, checksums, matriz de certificação, dataset oficial, calendário, workflows e documentação; evidência de validação persistida; e preservação das exceções históricas. Cada fonte e integração externa tem o seu próprio âmbito de governança e não é uma dependência deste roadmap.

## 6. Backlog B3 para finalizar, em ordem de dependência

| Prioridade | Trabalho | Critério de conclusão | Estado |
|---|---|---|---|
| P0 | Certificação automática da matriz anual | Workflow [38570114992](https://github.com/carlos-andrade/B3/actions/runs/38570114992) verde; CSV com 41 anos e linha 2026 sincronizada (parser 1.1.2, 3.142.910 linhas) | **CONCLUÍDO** |
| P1 | Dataset Oficial V1 | Workflow [38570165775](https://github.com/carlos-andrade/B3/actions/runs/38570165775) concluído com sucesso; 41 anos e registo 2026 alinhado com manifesto | **CONCLUÍDO NO ESCOPO V1** |
| P1 | Auditoria física independente dos 41 CSV NORMALIZED | Relatório [AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json); workflow [38568351293](https://github.com/carlos-andrade/B3/actions/runs/38568351293) | **EXECUTADA: 40/41 validados; 1998 reprovado por divergência de sidecar, controlada sem alterar o histórico** |
| P2 | Rever exceções semânticas históricas e calendários antigos | Inventário por ano com fonte oficial, estado, risco e decisão; não apagar exceções antigas sem evidência | **PARCIAL / POR ANO** |
| P2 | Fecho anual COTAHIST 2026 | Fonte anual final disponível após 31/12/2026; repetir fases exigidas, calendário, reconciliação, certificação e FASE12 | **AGUARDAR** |
| P1 | Pipeline diário COTAHIST 2026 | Parser do manifesto alinhado com `PARSER_VERSION`; verifica SHA do NORMALIZED contra manifesto; conflito de hash RAW/NORMALIZED não substitui artefactos canónicos; relatórios persistidos antes do gate; reconciliação idempotente; refresh de `main` após espera de concorrência; checkout sem baixar todo o histórico LFS | **RUN 38569675449 VERDE; zero conflitos; índice corrente sem alteração material** |
| P1 | Congelamento das agregações históricas | Certificação preserva as linhas de 1986–2025; Dataset Oficial V1 reutiliza os registos históricos persistidos e recalcula somente 2026; ambos os workflows validados | **CONCLUÍDO — runs 38570114992 e 38570165775 verdes** |
| P3 | Monitorização incremental diária e de erratas | Atualização com hash, data de corte, validação, alerta de falha e reconciliação idempotente | **ATIVA; manter e auditar** |
| P3 | Certificação semântica de estratégia/uso quantitativo | Validar adequação dos campos e eventos à finalidade antes de qualquer backtest/uso de decisão | **FORA DO FECHO DE INGESTÃO; posterior** |

## 7. Sequência executável para encerramento do escopo B3

1. Matriz anual sincronizada e workflow de certificação concluído: [run 38570114992](https://github.com/carlos-andrade/B3/actions/runs/38570114992).
2. Dataset Oficial V1 gerado/validado com sucesso: [run 38570165775](https://github.com/carlos-andrade/B3/actions/runs/38570165775).
3. Corrigidas as duas divergências críticas detetadas na auditoria de workflows; teste BDI e validação WATCHDOG concluídos com sucesso.
4. Auditoria de conformidade atual: 550 workflows auditados, **zero divergências críticas**, 407 conformes sem observações e 143 conformes com observações. Run final: [38570189171](https://github.com/carlos-andrade/B3/actions/runs/38570189171).
5. Auditoria física executada sobre os 41 anos: **40 validados; 1998 com divergência isolada de sidecar**. O hash físico do CSV coincide com o manifesto (`21b4740da8eb763259a0d859e261534de826449148c4d57d1f457f5721354e79`), mas difere do sidecar (`d1297e58cbbdf225f792b49a29f9143d3e041e66fd280808732e8c3513eb6bee`). Relatório persistido; workflow [38568351293](https://github.com/carlos-andrade/B3/actions/runs/38568351293) reprovou pelo gate fail-closed. Incidência documentada em [INCIDENCIA_COTAHIST_1998_SIDECAR_SHA256_2026-10-14.md](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/INCIDENCIA_COTAHIST_1998_SIDECAR_SHA256_2026-10-14.md). Por regra de histórico somente consulta, CSV, manifesto e sidecar não foram alterados.
6. Atualizar documentação agregada apenas depois da validação dos dados e evidências; não alterar README fora da janela governada.
7. Manter 2026 como **PARCIAL** até ao fecho anual e manter a exceção semântica de 1986 explicitamente visível.

## 8. Regras invioláveis de integridade

- Nunca inventar execução, hash, fonte, aprovação ou resultado.
- Nunca apagar evidência histórica de falha; documentar a correção e a nova execução.
- Nunca deduplicar, remover ou reordenar registos para forçar reconciliação.
- Nunca tratar snapshots com datas de corte diferentes como se fossem o mesmo universo.
- Nunca declarar certificação estrutural como certificação semântica completa.
- Nunca declarar o fecho anual de 2026 antes da fonte anual final.
- Não declarar o Dataset Oficial certificado sem hashes, contagens, manifestos e evidências coerentes.
- Atualizar primeiro cartas normativas e evidências; depois verificar; só então atualizar README/Wiki.

## 9. Política de ciclo de vida — decisão de 14/10/2026

- **1986–2025: ENCERRADOS PARA INGESTÃO ROTINEIRA; DISPONÍVEIS APENAS PARA CONSULTA.** Preservar RAW, NORMALIZED, manifestos, hashes e evidências; não alterar no ciclo rotineiro.
- **2026: ATUALIZAÇÃO INCREMENTAL DIÁRIA**, com data de corte, hashes, normalização, reconciliação, validação, persistência idempotente e atualização controlada dos artefactos agregados. O importador diário obtém `parser_version` de `normalize_cotahist.PARSER_VERSION`; se a fonte mudar o hash de uma data já existente, preserva o RAW canónico e grava incidência de conflito, sem substituição automática. O workflow persiste os relatórios antes do gate fail-closed e usa checkout sem baixar desnecessariamente o histórico Git LFS.
- Achados históricos devem ser registados sem alteração silenciosa. Reabrir um ano exige decisão formal, motivo, fonte/evidência, escopo, versionamento e auditoria antes/depois.
- O encerramento operacional de 1986–2025 **não equivale a certificação semântica integral**. A exceção semântica de 1986 e demais exceções documentadas permanecem vigentes.
- 2026 só poderá ser fechado após o fim do ano, aquisição e validação da fonte anual final e conclusão das fases aplicáveis, incluindo FASE12.

Política normativa: https://github.com/carlos-andrade/B3/blob/main/docs/governanca/politicas/POLITICA_RETENCAO_COTAHIST_1986_2026_V1.md

### Histórico de execução do pipeline diário — 14/10/2026

- Run [38568954914](https://github.com/carlos-andrade/B3/actions/runs/38568954914): sucesso; importador consultou 14/10–08/10, não encontrou fonte publicada para 14/10 e manteve o último dia válido em 13/10; zero conflitos.
- Run [38569195580](https://github.com/carlos-andrade/B3/actions/runs/38569195580): falha na rebase por concorrência com uma execução anterior que atualizou o índice oficial corrente. A falha foi preservada; a correção implementa reconciliação idempotente e refresh de `main` após a fila de concorrência.
- Run [38569219335](https://github.com/carlos-andrade/B3/actions/runs/38569219335): sucesso; índice corrente validado até 13/10/2026, zero conflitos de fonte.
- Run [38569675449](https://github.com/carlos-andrade/B3/actions/runs/38569675449): **SUCESSO** com refresh de `main` após a fila, reconciliação idempotente, zero conflitos e relatório persistido em [COTAHIST_DIARIO_EXECUCAO_20261014T131134Z.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/diario/execucoes/COTAHIST_DIARIO_EXECUCAO_20261014T131134Z.json). A fonte diária de 14/10 ainda não estava publicada; último dia válido mantido em 13/10.

## 10. Decisão atual — escopo exclusivo B3

**COTAHIST 2026 interno:** validado e promovido até 13/10/2026, com hashes coerentes, calendário reconciliado para o intervalo observado e exceções não bloqueadoras documentadas.  
**Cobertura estrutural anual:** 41/41 anos conforme a matriz vigente, com 1986 em exceção semântica controlada; a matriz agregada precisa de atualização para refletir o snapshot atual de 2026.  
**Escopo B3 — ingestão COTAHIST:** **CICLO OPERACIONAL VALIDADO ATÉ 13/10/2026**. Matriz anual certificada automaticamente, Dataset Oficial V1 gerado com sucesso, testes BDI/WATCHDOG verdes e auditoria de 550 workflows sem divergências críticas ([run 38570189171](https://github.com/carlos-andrade/B3/actions/runs/38570189171)). Pela decisão de 14/10/2026, 1986–2025 ficam somente para consulta e 2026 segue atualização diária. A auditoria física independente foi executada e persistida: 40/41 aprovados; 1998 mantém exceção controlada de sidecar, sem alteração do histórico congelado. O pipeline diário foi validado com sucesso no run [38569675449](https://github.com/carlos-andrade/B3/actions/runs/38569675449), sem conflitos de fonte; a data de corte permanece 13/10/2026 porque a fonte de 14/10 não estava disponível.

---
**Documento de consolidação:** ROADMAP MESTRE COTAHIST 1986–2026, estado 2026-10-14.
