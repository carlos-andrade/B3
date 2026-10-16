# Relatório de execução — Fase 03 operacional: capturas RAW e reconciliação de fontes

| Campo | Valor |
|---|---|
| **ID** | B3-INGESTAO-FASE03-20261016 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_FECHO_FASE_OPERACIONAL |
| **Fase** | FASE 03 — Capturas RAW e reconciliações de fontes |
| **Estado** | EXECUTADA_PARCIALMENTE; BLOQUEIOS_EXTERNOS_FAIL_CLOSED |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | ef584c564c2241936214aefa9c37e4c6438127845e3455209b4dfe6b87e5a503 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-16 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — não inferido de execução automática |
| **Origem** | Registo operacional de capturas RAW, manifestos e runs do GitHub Actions |
| **Autoridade superior** | [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md); [Layout Mestre B3](https://github.com/carlos-andrade/B3/blob/main/docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |
| **Escopo** | Verificar capturas autorizadas, integridade RAW, metadados e reconciliações; preservar bloqueios de autorização e lacunas de evidência |
| **Objetivo** | Promover apenas fontes cuja captura e integridade estejam comprovadas, sem contornar restrições de acesso |
| **Dependências** | Registo de capturas, manifestos, sidecars, workflows e políticas de licenciamento |

## 1. Decisão executiva

A Fase 03 foi executada no âmbito permitido: foram verificadas as evidências persistidas das capturas existentes e reconciliados os estados dos workflows. **A fase não pode ser declarada integralmente concluída**, porque permanecem bloqueios de autorização/acesso e lacunas específicas de cobertura. Nenhum endpoint restrito foi contornado, nenhum dado foi inventado e nenhuma fonte consolidada foi tratada como substituta de dados negócio a negócio.

## 2. Evidências verificadas

| Fonte/atividade | Evidência | Resultado verificado | Decisão |
|---|---|---|---|
| COTAHIST diário até 2026-10-15 | [Run 38889032782](https://github.com/carlos-andrade/B3/actions/runs/38889032782); relatório `COTAHIST_DIARIO_EXECUCAO_20261016T013436Z.json` | Workflow `success`; RAW ZIP, NORMALIZED CSV e manifesto persistidos; 18.827 registos, 25 campos, data única 2026-10-15; zero conflitos reportados | Validado para a data de referência documentada; não altera o snapshot anual histórico |
| BDI — DailyAverageStocks | [Run 38889119047](https://github.com/carlos-andrade/B3/actions/runs/38889119047) | Workflow `success`; página 1, 9 registos, 4 colunas; RAW e manifesto com SHA-256 persistidos | Captura desta tabela validada; cobertura integral do BDI continua não demonstrada |
| BCB/Copom — reunião 281 | [Run 38889256929](https://github.com/carlos-andrade/B3/actions/runs/38889256929) | Workflow `success`; JSON de listas/detalhes e NORMALIZED persistidos; metadados de captura e hashes registados | Captura API validada; horário exato de publicação do comunicado não comprovado |
| PDF oficial da Ata 281 | [Run 38889815903](https://github.com/carlos-andrade/B3/actions/runs/38889815903) | Workflow `success`; PDF binário de 401.502 bytes, assinatura `%PDF-` validada e SHA-256 persistido | Captura binária validada, separada da resposta JSON |
| Auditoria documental do HEAD de referência | [Run 38899464790](https://github.com/carlos-andrade/B3/actions/runs/38899464790) | Workflow `success` no commit `3e623cb6c194ce4d70ab37f97341f92c6a8e58c5` | Confirma integridade documental desse commit; não substitui validação funcional de cada fonte |

## 3. Bloqueios mantidos em FAIL_CLOSED

### 3.1 BDM — negócio a negócio de derivativos (P0)

**BLOQUEADO — sem captura automatizada.** A documentação de origem no repositório assinala restrição de coleta automatizada para a página Pesquisa por Pregão. Não se tentou contornar a restrição por endpoint interno, rota alternativa não autorizada ou dados consolidados.

Para desbloquear, é necessária uma via autorizada e os arquivos brutos das datas de referência 2026-09-16 e 2026-09-17. Após a obtenção autorizada, cada arquivo deve ter URL/recurso, data de referência, formato, bytes, SHA-256, layout/colunas, contagem, intervalo temporal e contratos reconciliados. Até então, agressor explícito e Cumulative Delta permanecem **NÃO CONFIRMADOS / NÃO CALCULADOS**.

Referência: [contrato de reconciliação negócio a negócio](PARTE03_NEGOCIO_A_NEGOCIO_RECONCILIACAO_FONTE_V1.0.md).

### 3.2 Timestamp exato do comunicado Copom

**PENDENTE — evidência temporal insuficiente.** A captura comprova a data de referência do comunicado, mas não um horário oficial de publicação. O campo deve permanecer `UNKNOWN`; não atribuir timestamp sintético nem usar uma hora inferida em estudos de eventos/backtests.

### 3.3 Cobertura integral do BDI

**PARCIAL.** A evidência cobre apenas `DailyAverageStocks`, página 1, data de referência 2026-10-15. Não declarar o BDI integralmente capturado ou reconciliado. Cada tabela/capítulo futuro exige captura, manifesto e reconciliação próprios.

## 4. Regras de integridade aplicadas

- Não foram alterados RAWs, NORMALIZED, manifestos ou sidecars históricos nesta fase.
- Não foi executada captura automatizada proibida nem contornado mecanismo de autorização.
- Não foi calculado Cumulative Delta sem dados trade-by-trade validados e sem confirmação do campo agressor.
- A data/horário desconhecidos permanecem explicitamente desconhecidos.
- A presença de uma captura isolada não foi generalizada para cobertura integral da fonte.
- Runs verdes foram tratados como evidência de execução do workflow, não como prova de completude semântica além do respetivo escopo.

## 5. Critérios de saída

- [x] Estado dos workflows de COTAHIST diário, BDI, BCB/Copom e PDF binário verificado.
- [x] Evidências existentes, caminhos e limitações registados.
- [x] Bloqueio BDM preservado por restrição de autorização/acesso.
- [x] Timestamp Copom mantido `UNKNOWN` por falta de prova.
- [x] Cobertura BDI classificada como parcial.
- [ ] Captura autorizada dos arquivos BDM 2026-09-16 e 2026-09-17.
- [ ] Fonte oficial que comprove o horário exato de publicação do comunicado Copom.
- [ ] Matriz de cobertura BDI por tabela/capítulo com captura e manifesto próprios.

## 6. Decisão final

**FASE 03 EXECUTADA PARCIALMENTE; NÃO LIBERADA PARA FECHO GLOBAL.** O trabalho permitido foi verificado e documentado. Os três itens pendentes acima permanecem bloqueadores/pendências explícitas. A próxima ação autorizada é obter autorização e os arquivos BDM por via permitida, em paralelo com a procura de evidência oficial do timestamp e a expansão controlada da matriz BDI. Nenhum bloqueio foi removido por inferência.
