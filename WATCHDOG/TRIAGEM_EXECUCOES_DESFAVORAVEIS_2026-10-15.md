# Fase C — Triagem técnica preliminar das execuções desfavoráveis

**Data da análise:** 2026-10-15  
**Repositório:** `carlos-andrade/B3`  
**Issue de origem:** [WATCHDOG #11](https://github.com/carlos-andrade/B3/issues/11)  
**Estado:** `TRIAGEM PARCIAL — NÃO ENCERRAR INCIDENTE`

## 1. Objetivo e limites

Foi iniciada a leitura dos logs de execuções que compõem a Issue #11. Esta nota regista causas observadas diretamente nos logs, sem presumir que uma execução posterior bem-sucedida corrige todos os dados produzidos por uma execução anterior. A Issue #11 reportou 12 execuções desfavoráveis na janela de 24 horas verificada em 2026-10-15 às 12:04 UTC.

A análise abaixo cobre evidências representativas dos seis grupos reportados. A classificação de recuperação só deve ser finalizada depois de comparar os artefactos/dados afetados e as execuções posteriores do mesmo workflow.

## 2. Causas observadas nos logs

| Grupo | Execução examinada | Evidência observada | Classificação preliminar | Seguimento obrigatório |
|---|---|---|---|---|
| Auditoria SHA-256 documental canónico | [Run #38](https://github.com/carlos-andrade/B3/actions/runs/38721900554) | Teste `test_pending_status_exposes_calculated_digest` esperava `PENDENTE`, mas recebeu `CABECALHO_CONTROLO_INVALIDO`. | Provável incompatibilidade entre fixture/teste e validação de cabeçalho; falha concreta identificada. | Confirmar os outros runs deste grupo e o resultado de regressão após a correção. |
| Dataset oficial COTAHIST V2 | [Run #9](https://github.com/carlos-andrade/B3/actions/runs/38577021350) e [Run #8](https://github.com/carlos-andrade/B3/actions/runs/38576905445) | O log enumera `SHA_FISICO_VS_MANIFESTO_DIVERGENTE` e `AUDITORIA_FISICA_NAO_CONFIRMA_HASH_TRIPLO`; no run #8, a divergência de SHA é listada para anos 2016–2026. | Integridade não demonstrada; não classificar como falha transitória sem reconciliação. | Comparar ficheiros físicos, manifestos, hashes e proveniência por ano; bloquear publicação enquanto a divergência não estiver explicada. |
| Auditoria física independente NORMALIZED 1986–2026 | [Run #2](https://github.com/carlos-andrade/B3/actions/runs/38568351293) | O passo `Aplicar gate fail-closed` terminou com `AUDITORIA_FISICA_REPROVADA`. | Gate de integridade atuou em modo fail-closed; não é, por si só, defeito do gate. | Abrir o artefacto de auditoria e resolver as divergências de dados que motivaram a reprovação. |
| Composição de carteiras de índices B3 | [Run #18](https://github.com/carlos-andrade/B3/actions/runs/38666819065) | Símbolos SMLL e UTIL rejeitados com `'datetime.date' object is not subscriptable`. | Erro de tratamento de tipo/data no código de captura ou normalização. | Corrigir o acesso à data, adicionar teste unitário com objeto `datetime.date` e validar a captura dos índices afetados. |
| Atualização do catálogo B3 | [Run #16](https://github.com/carlos-andrade/B3/actions/runs/38661402996) | O passo de importação BVBG.028.02 terminou com `urllib.error.HTTPError: HTTP Error 400: Bad Request`. | Falha HTTP da fonte/requisição; causa raiz ainda não determinada. | Inspecionar endpoint, parâmetros, payload e resposta segura da fonte; distinguir erro de contrato de indisponibilidade. Não registar credenciais nem payloads sensíveis. |
| Importação diária automática COTAHIST | [Run #30](https://github.com/carlos-andrade/B3/actions/runs/38569195580) | Rebase interrompido por conflito de conteúdo em `dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json`. | Conflito concorrente de escrita/atualização no manifesto. | Tornar a persistência concorrente segura, reler o estado remoto e reconciliar o manifesto sem descartar atualizações. |

## 3. Evidência de recuperação parcial

A auditoria SHA-256 documental teve posteriormente uma execução bem-sucedida após a criação deste registo: [Run #70](https://github.com/carlos-andrade/B3/actions/runs/38743518607), conclusão `success`, no commit `fd639be6335b150fca79a26cc7d04a682a37c3ee`.

Isto comprova o sucesso daquela execução posterior; não elimina o histórico das falhas nem demonstra, por si só, que todos os documentos e hashes anteriores estejam corretos.

## 4. Decisões de governança

1. Manter a Issue #11 aberta enquanto houver falhas sem classificação final ou problemas de integridade sem reconciliação.
2. Não alterar manifestos, hashes ou datasets para fazer um teste passar sem verificar a origem física e a cadeia RAW → validação → normalização → publicação.
3. Não repetir automaticamente workflows que publicam dados quando a causa pode envolver conflito concorrente ou integridade física.
4. Cada falha deve terminar com causa, ação corretiva, commit, execução de regressão e evidência de dados reconciliados.
5. Manter separadas as categorias: defeito de código, falha da fonte, concorrência de escrita, gate de integridade corretamente acionado e incidente recuperado.
6. Não declarar a Fase C concluída com base apenas em execuções verdes.

## 5. Próxima sequência

- [ ] Confirmar as execuções posteriores de cada workflow e os respetivos artefactos.
- [ ] Resolver prioritariamente as divergências SHA físico/manifesto do COTAHIST e a reprovação da auditoria física.
- [ ] Corrigir e testar o erro de tipo `datetime.date` na composição de índices.
- [ ] Diagnosticar o HTTP 400 de BVBG.028.02.
- [ ] Corrigir a concorrência de persistência do manifesto diário COTAHIST.
- [ ] Atualizar a Issue #11 com a classificação final de cada ocorrência e evidências.
- [ ] Prosseguir com C2–C6 do [plano de fecho da Fase C](FASE_C_FECHAMENTO_OPERACAO_GOVERNANCA_2026-10-15.md).

**Decisão:** a triagem já identifica causas técnicas acionáveis, mas continua parcial. Não encerrar a Issue #11 nem a Fase C até as ações e evidências acima serem verificadas.
