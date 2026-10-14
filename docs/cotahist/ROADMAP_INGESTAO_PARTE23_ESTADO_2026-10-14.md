# B3 — ROADMAP DE INGESTÃO COTAHIST — PARTE23 (RECONCILIADO)

**Data de referência:** 2026-10-14  
**Repositório:** https://github.com/carlos-andrade/B3  
**Estado:** auditoria integrada pós-promoção concluída; calendário oficial B3 reconciliado sem divergências para 02/01–13/10/2026; persistência idempotente verificada com sucesso; dados validados até 13/10/2026; fecho anual permanece pendente. Decisão de ciclo de vida: 1986–2025 somente consulta; 2026 atualização diária.

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
| 18 | Dataset Oficial V2 | Reprovado no run [38576248254](https://github.com/carlos-andrade/B3/actions/runs/38576248254) por exigir certificações físicas anuais individuais ausentes, apesar da auditoria física global aprovada; gerador ajustado para consumir a evidência global canónica; revalidação em curso no run [38577021350](https://github.com/carlos-andrade/B3/actions/runs/38577021350) | Confirmar execução, corrigir falhas reais se existirem e só então certificar publicação V2 |

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

**Conclusão operacional:** o ciclo técnico COTAHIST 2026 está validado e promovido até 13/10/2026. A execução diária mais recente [38570797936](https://github.com/carlos-andrade/B3/actions/runs/38570797936) terminou com sucesso: a fonte de 14/10 ainda não estava publicada, os dados até 13/10 permaneceram inalterados e foram registados zero conflitos de hash. A reconciliação do índice corrente foi idempotente. A auditoria de conformidade dos workflows [38570797752](https://github.com/carlos-andrade/B3/actions/runs/38570797752) validou 550 workflows, zero divergências críticas e 143 observações não bloqueadoras. O calendário oficial foi reconciliado para o intervalo observado, sem divergências. O histórico 1986–2025 está congelado para consulta. A exceção histórica de 1998 foi resolvida: o sidecar foi alinhado ao SHA-256 confirmado pelo CSV e manifesto. A auditoria física completa terminou com sucesso no run [38576260466](https://github.com/carlos-andrade/B3/actions/runs/38576260466), com `APROVADO`, 41/41 anos validados e zero falhas. O incidente está encerrado; os dados CSV e manifestos históricos foram preservados. A geração do Dataset Oficial V2 revelou um bloqueio distinto: o gerador exigia 41 ficheiros individuais de certificação física, enquanto a evidência canónica aprovada é a auditoria global. O gerador foi alterado para validar cada ano contra essa auditoria global, sem fabricar certificados individuais; execução de a primeira validação revelou que o workflow não materializava Git LFS, causando hashes de ponteiros em vez dos CSV físicos; checkout LFS ativado no commit `2c8ea2ca3ce59091f446c5d04b43957f2a4109a4`; revalidação após checkout LFS seletivo em curso no run [38577163285](https://github.com/carlos-andrade/B3/actions/runs/38577163285). O fecho anual 2026 permanece pendente até ao fim do ano.
