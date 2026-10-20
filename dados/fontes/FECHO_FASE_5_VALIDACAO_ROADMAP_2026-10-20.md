# Fecho da Fase 5 — validação e decisão do roadmap de fontes públicas

| Campo | Valor |
|---|---|
| ID | B3-FECHO-F5-FONTES-20261020 |
| Projeto | B3 — A BOLSA DO BRASIL |
| Data de verificação | 2026-10-20 |
| Estado da Fase 5 | **CONCLUÍDA COM RESSALVAS** |
| Estado do roadmap global | **ABERTO — não elegível para fecho integral** |
| Auditoria SHA-256 | [Run 39414349355](https://github.com/carlos-andrade/B3/actions/runs/39414349355) |
| WATCHDOG independente | [Run 39421518597](https://github.com/carlos-andrade/B3/actions/runs/39421518597) |
| Backlog operacional | [Issue #16](https://github.com/carlos-andrade/B3/issues/16) |
| WATCHDOG | [Issue #12](https://github.com/carlos-andrade/B3/issues/12) |

## 1. Objetivo da verificação

Validar a evidência acumulada nas fases 1–4, conferir integridade documental e CI, analisar a execução WATCHDOG posterior às alterações e decidir se os critérios permitem encerrar o roadmap global.

## 2. Verificações realizadas

| Controlo | Resultado | Evidência / interpretação |
|---|---|---|
| Política de aquisição publicada e em vigor | PASS | [Política B3](../../WIKI/01-GOVERNANCA/POLITICA_AQUISICAO_DADOS_PUBLICOS_GRATUITOS_V1.md) e adenda no repositório GOVERNANCA |
| Inventário de fontes versionado | PASS COM ESCOPO LIMITADO | 14 registos iniciais; inventário relevante ao projeto, não exaustivo de toda a Internet |
| Validador do inventário e testes | PASS | Orquestrador runs [#16](https://github.com/carlos-andrade/B3/actions/runs/39412861864), [#17](https://github.com/carlos-andrade/B3/actions/runs/39413299122), [#18](https://github.com/carlos-andrade/B3/actions/runs/39413806000) |
| Captura CVM DFP/ITR | PASS — RAW + manifestos | [Run #2](https://github.com/carlos-andrade/B3/actions/runs/39413170519); ZIP íntegros, licença ODbL identificada, SHA-256 e manifestos publicados; ainda não certificados |
| Captura PTAX EUR/USD | PASS — janela móvel de 30 dias | [Run #2](https://github.com/carlos-andrade/B3/actions/runs/39413690563); 100 observações por moeda, RAW, manifestos e SHA-256 publicados; backfill histórico não realizado |
| Gate do canal restrito do catálogo B3 | PASS | [Run #22](https://github.com/carlos-andrade/B3/actions/runs/39412913659) passou sem chamada de rede; captura recorrente pelo canal associado à interface restrita permanece desativada |
| Auditoria SHA-256 documental | PASS | [Run 39414349355](https://github.com/carlos-andrade/B3/actions/runs/39414349355): job `auditar` concluído com `success`; testes do hash canónico e comparação de SHA-256 passaram |
| WATCHDOG posterior às correções | EXECUÇÃO PASS; ESTADO AGREGADO DESFAVORÁVEL | [Run 39421518597](https://github.com/carlos-andrade/B3/actions/runs/39421518597) concluiu tecnicamente com `success`, mas o relatório de 2026-10-20T12:20:38Z classificou o estado `NAO_FAVORAVEL`: 70 execuções observadas, 49 success, 17 cancelled, 3 failure e 1 ativa no instante da fotografia. Falhas listadas: primeiro run PTAX, primeiro run CVM e Atualizar catálogo B3 #19. Os primeiros dois foram corrigidos e os reruns passaram; o run #19 precisa ser distinguido do gate posterior que passou. O próprio monitor não dispõe de heartbeat externo configurado. |

## 3. Decisão sobre o roadmap

**A Fase 5 fica concluída como etapa de validação e decisão. O roadmap global NÃO fica encerrado.**

A auditoria documental SHA-256 passou e os principais workflows de ingestão corrigidos passaram. Contudo, os critérios de fecho global exigem cobertura/validação por dataset e tratamento das pendências ainda abertas. A execução WATCHDOG é tecnicamente bem-sucedida, mas o seu resultado agregado é `NAO_FAVORAVEL`; por isso, não se declara o ambiente globalmente favorável nem se fecha a Issue #12.

## 4. Pendências que bloqueiam o fecho global

1. Backfill histórico PTAX para além da janela móvel de 30 dias.
2. Captura e validação dos restantes conjuntos CVM: informe diário de fundos, cadastro de fundos e cadastro de companhias abertas.
3. Verificação por dataset dos termos/licenças e implementação para IBGE/SIDRA e Tesouro Transparente.
4. Evidência dos termos e autorização aplicáveis a BVBG.028.02 e confirmação do âmbito de automação, armazenamento e redistribuição de COTAHIST/BDI.
5. Confirmar canal oficial e permitido para DRP/Rapinegocios.
6. Triar as falhas do WATCHDOG, distinguir falhas históricas corrigidas de falhas atuais, e configurar supervisão externa independente se exigida pela governança.
7. Atualizar a auditoria e inventário com novas evidências, sem promover RAW a NORMALIZED/CERTIFIED antes das validações de domínio.

Acompanhar estas tarefas em [Issue #16](https://github.com/carlos-andrade/B3/issues/16). Manter [Issue #12](https://github.com/carlos-andrade/B3/issues/12) aberta até uma fotografia WATCHDOG favorável e triagem documentada das execuções desfavoráveis.

## 5. Critérios finais da Fase 5

- [x] Rever política, inventário, evidências de ingestão e gates.
- [x] Confirmar que a auditoria automática SHA-256 terminou com sucesso.
- [x] Executar e inspecionar o novo WATCHDOG.
- [x] Registar decisão explícita de não fechar prematuramente o roadmap global.
- [x] Deixar as pendências abertas e associadas a issues verificáveis.
- [ ] Fecho integral do roadmap — bloqueado até resolução das pendências da secção 4.

## 6. Regra de integridade

Este fecho não significa que todas as fontes públicas gratuitas da Internet foram identificadas, nem certifica a qualidade fundamental de todos os dados. A cobertura é incremental e delimitada ao universo relevante ao projeto B3. Disponibilidade técnica, autorização de recolha, direitos de utilização/redistribuição, integridade e qualidade dos dados permanecem decisões separadas.
