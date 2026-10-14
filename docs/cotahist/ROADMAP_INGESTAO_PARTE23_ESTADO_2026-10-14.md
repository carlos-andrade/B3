# B3 — ROADMAP DE INGESTÃO COTAHIST — PARTE23 (RECONCILIADO)

**Data de referência:** 2026-10-14  
**Repositório:** https://github.com/carlos-andrade/B3  
**Estado:** auditoria integrada pós-promoção concluída e persistida; dados 2026 validados até 13/10/2026; calendário oficial externo e fecho anual permanecem pendentes.

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

## Auditoria integrada pós-promoção

Evidência canónica: [COTAHIST_2026_AUDITORIA_INTEGRADA_POS_PROMOCAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2026_AUDITORIA_INTEGRADA_POS_PROMOCAO_V1.json).

**Resultado:** `APROVADO_COM_LIMITACOES_NAO_BLOQUEANTES`. A cadeia de hashes RAW/NORMALIZED, contagens, campos, datas, FASE04–FASE09, candidato FASE10 e promoção FASE11 está coerente. A FASE11 mantém no seu registo a decisão histórica `REEXECUTAR_FASES_04_08`, porque a promoção antecedeu a revalidação; a auditoria integrada documenta que as revalidações posteriores apresentam os mesmos hashes.

### Limitações explícitas

1. FASE04 é auditoria de integridade/documentação; a comparação independente integral dos 25 campos RAW × NORMALIZED é certificada pela FASE06.
2. A sequência física contém regressões temporais reportadas na FASE08. As linhas foram preservadas, sem reordenação ou deduplicação.
3. O calendário oficial histórico B3 não está persistido como referência verificável nesta cadeia. Não declarar equivalência com o calendário oficial.
4. A última data observada é 2026-10-13. Isto não constitui fecho anual de 2026.
5. A aprovação deste ciclo não certifica nem autoriza migração histórica 1986–2025.

## Roadmap operacional atualizado

| Ordem | Etapa | Estado | Próxima ação |
|---|---|---|---|
| 1 | Aquisição RAW 2026 | Concluída e identificada por hash | Monitorizar nova publicação oficial |
| 2 | FASE04–05 | Validadas após promoção | Reabrir apenas se RAW/NORMALIZED ou regras mudarem |
| 3 | FASE06 | Validada; 25 campos, zero divergências | Preservar evidência; não deduplicar |
| 4 | FASE07 | Validada; chave candidata ampliada sem colisões observadas | Não generalizar a conclusão para outros anos |
| 5 | FASE08 | Validada com exceções não bloqueadoras | Persistir calendário oficial e executar comparação externa |
| 6 | Gate 06–08 | Aprovado com exceções | Reabrir apenas se dados/regras mudarem |
| 7 | FASE09 | Liberada para FASE10; run success | Manter evidência atual; documento antigo fica histórico |
| 8 | FASE10 | Candidato validado sem diferenças | Não repetir sem mudança do candidato ou dos hashes |
| 9 | FASE11 | Promoção e hashes revalidados | Não repetir sem mudança do candidato ou das regras |
| 10 | Auditoria integrada pós-promoção | Concluída e persistida | Usar como estado consolidado deste ciclo |
| 11 | Calendário oficial B3 | Pendente | Obter, versionar e validar fonte/calendário oficial |
| 12 | Fecho anual 2026 | Pendente | Aguardar fim do ano e publicação anual oficial |
| 13 | Histórico 1986–2025 | Fora do âmbito desta aprovação | Seguir gates e evidências independentes por ano |

## Regras de integridade

- Não sobrescrever silenciosamente RAW/NORMALIZED.
- Não inventar execução, checksum ou resultado.
- Não deduplicar nem reordenar linhas para corrigir exceções da fonte.
- Não declarar o fecho anual de 2026 prematuramente.
- Preservar a auditoria antiga de atualidade como registo histórico; a evidência integrada atualiza o diagnóstico, não apaga o histórico.
- Não usar a aprovação 2026 como certificação dos anos 1986–2025.

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
- [Auditoria histórica de atualidade](https://github.com/carlos-andrade/B3/blob/main/docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md)

**Conclusão operacional:** o ciclo técnico COTAHIST 2026 está validado e promovido até 13/10/2026, com exceções explicitamente classificadas e sem bloqueadores internos. O próximo trabalho é a validação contra calendário oficial persistido e a monitorização da próxima publicação; não é necessária nova aquisição ou repetição de FASE10/FASE11 enquanto os hashes e regras permanecerem inalterados.
