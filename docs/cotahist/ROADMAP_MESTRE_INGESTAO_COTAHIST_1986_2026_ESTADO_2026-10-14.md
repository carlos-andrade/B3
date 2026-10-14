# B3 — ROADMAP MESTRE DE INGESTÃO COTAHIST 1986–2026
**Data de referência:** 2026-10-14  
**Repositório oficial:** https://github.com/carlos-andrade/B3  
**Branch:** main  
**Estado global:** **EM FINALIZAÇÃO DO ESCOPO B3 — INGESTÃO COTAHIST**  
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

### Pendências do escopo B3
1. **A matriz agregada de certificação anual foi sincronizada para 2026**: a linha CSV agora regista parser 1.1.2 e 3.142.910 linhas, coerentes com o manifesto canónico de 14/10. Falta executar a certificação automática e verificar a matriz completa contra todos os manifestos.
2. **O Dataset Oficial e os artefactos agregados precisam de auditoria final**: verificar alinhamento entre manifestos, matriz, dataset oficial, checksums, sidecars e documentação.
3. **O ano de 2026 não está fechado**: o conjunto está atualizado até 13/10/2026. O fecho anual só pode ocorrer após o fim do ano e a aquisição/validação da fonte anual final.
4. A exceção semântica histórica de 1986 permanece controlada; não declarar equivalência semântica plena de todo o período 1986–2026.
5. Exceções de calendário histórico de anos antigos e exceções de ordenação/regressão devem continuar explícitas; não corrigir a fonte reordenando ou removendo linhas.

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
- **2026:** a linha atual da matriz está desatualizada relativamente aos manifestos canónicos de 14/10. Regenerar a matriz a partir dos manifestos atuais e validar contagem, datas, parser e hash antes de a voltar a declarar sincronizada.
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
| P0 | Executar certificação automática da matriz anual | Workflow verde; CSV reconstruído a partir dos manifestos e todos os 41 anos verificados; confirmar a linha 2026 (parser 1.1.2, 3.142.910 linhas) | **PENDENTE DE EXECUÇÃO/VERIFICAÇÃO** |
| P1 | Auditar e reconciliar o Dataset Oficial | Manifestos, matriz anual, dataset oficial, checksums, sidecars e documentação concordam em versões, contagens, hashes e data de corte | **PENDENTE DE AUDITORIA** |
| P2 | Rever exceções semânticas históricas e calendários antigos | Inventário por ano com fonte oficial, estado, risco e decisão; não apagar exceções antigas sem evidência | **PARCIAL / POR ANO** |
| P2 | Fecho anual COTAHIST 2026 | Fonte anual final disponível após 31/12/2026; repetir fases exigidas, calendário, reconciliação, certificação e FASE12 | **AGUARDAR** |
| P3 | Monitorização incremental diária e de erratas | Atualização com hash, data de corte, validação, alerta de falha e reconciliação idempotente | **ATIVA; manter e auditar** |
| P3 | Certificação semântica de estratégia/uso quantitativo | Validar adequação dos campos e eventos à finalidade antes de qualquer backtest/uso de decisão | **FORA DO FECHO DE INGESTÃO; posterior** |

## 7. Sequência executável para encerramento do escopo B3

1. Regenerar e validar a matriz de certificação anual a partir dos manifestos atuais, sobretudo a linha de 2026.
2. Executar a auditoria física do Dataset Oficial e reconciliar manifesto, matriz, sidecars e checksums.
3. Verificar que o dataset oficial publicado corresponde aos dados canónicos e que as limitações de 1986 e 2026 estão explícitas.
4. Executar a auditoria final do Layout Mestre e dos workflows internos; verificar runs, artefactos e commits.
5. Atualizar a documentação agregada apenas depois da validação dos dados e das evidências.
6. Publicar um relatório de encerramento B3 com hashes, escopo, limitações, exceções, runs e decisão formal.
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

## 9. Decisão atual — escopo exclusivo B3

**COTAHIST 2026 interno:** validado e promovido até 13/10/2026, com hashes coerentes, calendário reconciliado para o intervalo observado e exceções não bloqueadoras documentadas.  
**Cobertura estrutural anual:** 41/41 anos conforme a matriz vigente, com 1986 em exceção semântica controlada; a matriz agregada precisa de atualização para refletir o snapshot atual de 2026.  
**Escopo B3 — ingestão COTAHIST:** **EM FINALIZAÇÃO**. As pendências imediatas são executar/verificar a certificação automática da matriz anual, auditar o Dataset Oficial e concluir a auditoria interna de governança. O fecho anual 2026 permanece pendente até existir a fonte anual final.

---
**Documento de consolidação:** ROADMAP MESTRE COTAHIST 1986–2026, estado 2026-10-14.
