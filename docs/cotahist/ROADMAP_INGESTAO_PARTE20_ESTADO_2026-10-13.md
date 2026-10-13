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

## 3. Última fase concluída e próxima fase autorizada
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

Contrato e pré-condições da FASE07 (registo histórico):
1. consumir o NORMALIZED e o hash fixados pela FASE06;
2. consumir a evidência FASE06 em modo somente leitura;
3. seguir o Layout Mestre e a regra de existência/validação;
4. não deduplicar nem remover linhas;
5. avaliar a chave candidata com base em colisões, campos do layout, amostras e análise dos registos colidentes;
6. não generalizar automaticamente a chave observada em 2006 para 2014;
7. persistir evidência própria de 2014 com contagens, hashes, colisões, decisão, limitações e timestamp;
8. executar validação independente antes de promover o status.

A chave candidata usada em 2006 incluiu `prazot` para separar colisões, mas a evidência de 2006 não autoriza deduplicação nem generalização automática para outros anos.
### FASE08 — calendário e consistência temporal — 2014
Estado: **VALIDADO_COM_EXCECAO — evidência persistida; atualização de classificação em reexecução**.

- Workflow: `.github/workflows/cotahist-fase08-calendario-2014-v1.yml`.
- Commit do workflow: `013100f0e271988c37b1edad58cf77a1d01f2f3b`.
- Contrato anual: usa NORMALIZED 2014 e evidências FASE06/FASE07; trigger inclui alterações nesses artefactos e no próprio workflow.
- Integridade do ficheiro: confirmado na branch `main`, sem referências residuais a 2013.
- Evidência persistida e revista: [COTAHIST_2014_FASE08_SEMANTICA_CALENDARIO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2014_FASE08_SEMANTICA_CALENDARIO_V1.json), commit `fb9ae230d9f658f166318aca6658a1415f3a9c77`; hash do blob `4ca480029a18007cb511e53f37fb838b99052f93`.
- Resultado: 392.228 registos; 248 datas de negociação entre 2014-01-02 e 2014-12-30; zero datas inválidas/fora do ano, zero regressões cronológicas e zero regressões temporais por instrumento; nenhuma linha removida.
- Métrica informativa: 97.444 transições decrescentes na ordenação lexicográfica da tupla de instrumento. Não equivale a regressão temporal; foi classificada explicitamente como não bloqueadora. Evidência revista no commit `fb9ae230d9f658f166318aca6658a1415f3a9c77`.
- Gate 06–08: execução com resultado `VALIDADO_COM_EXCECAO`, decisão `LIBERADO_PARA_FASE09`, zero bloqueadores e hash físico do NORMALIZED confirmado contra FASE06/FASE07/FASE08. Evidência: [COTAHIST_2014_GATE_06_08_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2014_GATE_06_08_V1.json), commit `f6f0a2f5c2b26cafd5fb18295a9043f00be9c999`.
- O Gate foi reexecutado após a atualização da evidência FASE08: commit `1632ec85a416c0716b519a0df46eee0211f26ac7`; status `VALIDADO_COM_EXCECAO`, decisão `LIBERADO_PARA_FASE09`, zero bloqueadores. A FASE09 foi liberada com evidência persistida `LIBERADO_PARA_FASE10`, zero bloqueadores e hashes RAW/NORMALIZED coincidentes. A FASE10 foi executada e validada independentemente: 392.228 registos RAW e NORMALIZED, 25 campos comparados, zero divergências, sem alteração do RAW nem deduplicação. Evidência: [COTAHIST_2014_FASE10_VALIDACAO_INDEPENDENTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2014_FASE10_VALIDACAO_INDEPENDENTE_V1.json). Workflow FASE10: commit `af473118b24f45a0c84d67129677449098c46a74`.

A FASE11 foi certificada: status `CERTIFICADO`, decisão `LIBERADO_PARA_FASE12`, zero bloqueadores, FASE10 com zero divergências nos 25 campos e hashes RAW/NORMALIZED registados. Evidência: [COTAHIST_2014_FASE11_CERTIFICACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2014_FASE11_CERTIFICACAO_V1.json), commit `ef0ba2e70ccc05ea00649c1869fb0d036f09c4fb`.

A FASE12 foi executada: status `FECHADO_COM_TRANSICAO_CONTROLADA`, decisão `FECHAR_2014_E_AUTORIZAR_CONTINUACAO_2015`, zero bloqueadores. A integridade do RAW 2015 foi confirmada: hash `593f8740ec1aa87c80c54c623f1759530b6b32cdadd34a64f0fc66a529f34e35`, coincidente com manifesto e sidecar; ZIP com um membro, zero comprimentos inválidos e 414.177 registos tipo 01. Evidência: [COTAHIST_2014_FASE12_FECHAMENTO_2015_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2014_FASE12_FECHAMENTO_2015_ABERTURA_V1.json), commit `0e5c089c0ad700c689e13a7e2ef3de8458f4d9e7`.

A transição **não certifica 2015**. O NORMALIZED CSV 2015 ainda não existe; a FASE04 de 2015 aguarda reconstrução e validação independente. Próximo ciclo autorizado: 2015, começando pela verificação das fases e dos artefactos existentes, sem assumir conclusão de qualquer fase.


### COTAHIST 2015 — estado inicial após transição

- FASE12 de 2014 autorizou a continuação de 2015 sem certificar o novo ano; RAW 2015 verificado com SHA-256 `593f8740ec1aa87c80c54c623f1759530b6b32cdadd34a64f0fc66a529f34e35`.
- FASE00: `VALIDADO`, decisão `AUTORIZAR_FASE01`; evidência commit `bbc5e2486dbd361cae5ec02fa7eaca41c0e3111b`.
- FASE01: `VALIDADO`, decisão `LIBERADO_PARA_FASE02`; RAW coincide com manifesto e sidecar; evidência commit `3a7064fd3dd9488105e0c88818d79a5337bcd658`.
- FASE02: `VALIDADO`, decisão `LIBERADO_PARA_FASE03`; ZIP íntegro, um membro, 245 bytes por registo, 414.177 registos tipo 01; evidência commit `f9af56709a2a33e54875336ffa98fde65edfb06e`.
- FASE03: `VALIDADO`, decisão `LIBERADO_PARA_FASE04`; zero comprimentos inválidos, zero datas inválidas, intervalo 2015-01-02 a 2015-12-30; evidência commit `cb45cc61331e38197c34dda5f0bdf4044e5b9238`.
- FASE04: `VALIDADO`, decisão `LIBERADO_PARA_FASE05`; NORMALIZED persistido, 414.177 linhas, 25 campos, zero datas inválidas/fora do ano, hash calculado igual ao manifesto e sidecar: `9b767ef5089e2eddb6125b025b4deb7b456896d11a74486c727e56da8a59757d`. Evidência `COTAHIST_2015_FASE04_NORMALIZACAO_V1.json`.
- Divergência de versão registada: manifesto declara parser `1.1.0`; script canónico atual declara `1.1.2`. O hash calculado coincide, por isso a versão não foi usada isoladamente como bloqueio nem o manifesto foi alterado.
- FASE05: `VALIDADO`, decisão `LIBERADO_PARA_FASE06`; RAW e NORMALIZED físicos coincidem com os respetivos manifestos e sidecars; ZIP PASS; 414.177 linhas, 25 campos; intervalo 2015-01-02 a 2015-12-30; nenhuma deduplicação. Evidência commit `9516220f561bda61325b5d1ad044a3baf9dce1eb`.
- FASE06: `VALIDADO`, decisão `LIBERADO_PARA_FASE07`; 414.177 registos RAW e NORMALIZED, 12 campos críticos, zero divergências, sem alteração RAW ou deduplicação. Evidência commit `a360c26e98dc5d6028cb4a41486b6bc9d0fe200f`.
- FASE07: `VALIDADO`, decisão `CHAVE_CANDIDATA_COM_PRAZOT_VALIDADA_POR_CARDINALIDADE`; 414.177 registos, 401.711 chaves-base distintas, 5.414 grupos duplicados na chave-base, 12.466 linhas excedentes; chave candidata com `prazot` tem 414.177 chaves distintas e zero colisões; nenhuma linha removida. Evidência: [COTAHIST_2015_FASE07_IDENTIDADE_CHAVES_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2015_FASE07_IDENTIDADE_CHAVES_V1.json), blob `b861799f7082858009a9e96adb21969af3b2cce9`.
- FASE08: `VALIDADO_COM_EXCECAO`, 414.177 registos, 246 datas de negociação entre 2015-01-02 e 2015-12-30; zero datas inválidas, zero regressões cronológicas e zero regressões temporais por instrumento; 94.112 transições lexicográficas de instrumentos explicitamente classificadas como métrica informativa não bloqueadora. Evidência: [COTAHIST_2015_FASE08_SEMANTICA_CALENDARIO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2015_FASE08_SEMANTICA_CALENDARIO_V1.json).
- Gate 06–08: `VALIDADO_COM_EXCECAO`, decisão `LIBERADO_PARA_FASE09`, zero bloqueadores; hash físico NORMALIZED coincidente entre FASE06/FASE07/FASE08. Evidência: [COTAHIST_2015_GATE_06_08_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2015_GATE_06_08_V1.json).
- FASE09: `LIBERADO_PARA_FASE10`, zero bloqueadores, hashes RAW/NORMALIZED confirmados. Evidência: [COTAHIST_2015_FASE09_PRE_RELEASE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2015_FASE09_PRE_RELEASE_V1.json).
- FASE10: `VALIDADO`, decisão `LIBERADO_PARA_FASE11`; 414.177 registos RAW e NORMALIZED, todos os 25 campos comparados, zero divergências, RAW imutável e sem deduplicação. Evidência: [COTAHIST_2015_FASE10_VALIDACAO_INDEPENDENTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2015_FASE10_VALIDACAO_INDEPENDENTE_V1.json), commit `9841b5c2751815593cc255550591d9d00c9323f3`.
- FASE11: `CERTIFICADO`, decisão `LIBERADO_PARA_FASE12`, zero bloqueadores; FASE10 sem divergências, Gate 06–08 com exceções classificadas e hashes RAW/NORMALIZED registados. Evidência: [COTAHIST_2015_FASE11_CERTIFICACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2015_FASE11_CERTIFICACAO_V1.json), blob `ad85083e59f8542b0416dd285bcfbe97ea333231`.
- FASE12: `FECHADO_COM_TRANSICAO_CONTROLADA`, decisão `FECHAR_2015_E_AUTORIZAR_CONTINUACAO_2016`, zero bloqueadores. RAW 2016 hash confirmado com manifesto/sidecar; ZIP íntegro, 466.734 registos tipo 01. Evidência: [COTAHIST_2015_FASE12_FECHAMENTO_2016_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2015_FASE12_FECHAMENTO_2016_ABERTURA_V1.json), commit `0e5c089c0ad700c689e13a7e2ef3de8458f4d9e7`.

### COTAHIST 2016 — estado inicial após transição

- FASE12 de 2015 autorizou a continuação de 2016 sem certificar o novo ano. Evidência: [COTAHIST_2015_FASE12_FECHAMENTO_2016_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2015_FASE12_FECHAMENTO_2016_ABERTURA_V1.json), status `FECHADO_COM_TRANSICAO_CONTROLADA`, decisão `FECHAR_2015_E_AUTORIZAR_CONTINUACAO_2016`.
- RAW 2016: SHA-256 `ffc82a9b973cb5901e68dc11bea1bbc9bf0a2c46749e0efe5a7a89229bc0d81f`, coincidente com manifesto e sidecar; ZIP com um membro, zero comprimentos inválidos, 466.734 registos tipo 01.
- FASE00: `VALIDADO`, decisão `AUTORIZAR_FASE01`; evidência blob `edad1b232c79fd790f3a5880659e28e3f82ab192`.
- FASE01: `VALIDADO`, decisão `LIBERADO_PARA_FASE02`; hash RAW coincide com manifesto e sidecar; evidência blob `23cfc1752bde33c713362d17502a489eeb4125d6`.
- FASE02: `VALIDADO`, decisão `LIBERADO_PARA_FASE03`; ZIP íntegro, um membro, 245 bytes por registo, 466.734 registos tipo 01; evidência blob `d0e8e98a8c8b35a54c57f310a3d242f1f5ddeb21`.
- FASE03: `VALIDADO`, decisão `LIBERADO_PARA_FASE04`; zero comprimentos/datas inválidos, intervalo 2016-01-04 a 2016-12-29; evidência commit `7a3fefff7eb89aaaa40bc865b67bd0b626e2e887`.
- FASE04: `VALIDADO`, decisão `LIBERADO_PARA_FASE05`; NORMALIZED persistido, 466.734 linhas, 25 campos, zero datas inválidas/fora do ano; hash calculado igual ao manifesto e sidecar `2d918553c976c74fcab7c065a25fa98efbffaf67f0fda73b46bbc7c8779ea66b`. Evidência: `COTAHIST_2016_FASE04_NORMALIZACAO_V1.json`, blob `d93c53accbe1585186ac8df0516f66c6e67c3362`.
- FASE05: `VALIDADO`, decisão `LIBERADO_PARA_FASE06`; RAW/NORMALIZED físicos coincidem com manifestos e sidecars, ZIP PASS, 466.734 linhas, 25 campos, datas 2016-01-04 a 2016-12-29, sem deduplicação. Evidência commit `b32869d5d19c5d5d86bfe4f412a466e237ef43d5`.
- FASE06: `VALIDADO`, decisão `LIBERADO_PARA_FASE07`; 466.734 registos RAW/NORMALIZED, 12 campos críticos, zero divergências, sem alteração RAW ou deduplicação. Evidência commit `1d76cccaff6cba0980141821833b174cbd14cd5d`.
- FASE07: `VALIDADO`, decisão `CHAVE_CANDIDATA_COM_PRAZOT_VALIDADA_POR_CARDINALIDADE`; 466.734 registos, 453.505 chaves-base distintas, 6.024 grupos duplicados na chave-base, 13.229 linhas excedentes; chave candidata com `prazot` tem 466.734 chaves distintas, zero colisões, nenhuma linha removida. Evidência blob `32285cf230bd498970886ea8b5cd6a9f8016cbf5`.
- FASE08: `VALIDADO_COM_EXCECAO`, decisão `LIBERADO_PARA_GATE_06_08`; 466.734 registos, 249 datas entre 2016-01-04 e 2016-12-29, zero datas inválidas/fora do ano, zero regressões cronológicas e temporais por instrumento; 101.379 transições lexicográficas de instrumentos classificadas como métrica informativa não bloqueadora. Evidência: [COTAHIST_2016_FASE08_SEMANTICA_CALENDARIO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_FASE08_SEMANTICA_CALENDARIO_V1.json).
- Gate 06–08: `VALIDADO_COM_EXCECAO`, decisão `LIBERADO_PARA_FASE09`; 466.734 registos, 25 campos, hash NORMALIZED `2d918553c976c74fcab7c065a25fa98efbffaf67f0fda73b46bbc7c8779ea66b`, zero bloqueadores, sem deduplicação/remoção de linhas. Evidência: [COTAHIST_2016_GATE_06_08_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_GATE_06_08_V1.json), commit `d7421e534a630d4571e9c782f63729c61f434fdd`.
- FASE09: `LIBERADO_PARA_FASE10`; pré-condições completas, zero ausências/bloqueios, hashes RAW/NORMALIZED e contagens confirmados. Evidência: [COTAHIST_2016_FASE09_PRE_RELEASE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_FASE09_PRE_RELEASE_V1.json), commit `1ff8794a583c07f0584f444fbcf7cf24cbd6aefe`.
- FASE10: `VALIDADO`, decisão `LIBERADO_PARA_FASE11`; 466.734 registos RAW/NORMALIZED, 25 campos comparados, zero divergências, sem mutação do RAW ou deduplicação. Evidência: [COTAHIST_2016_FASE10_VALIDACAO_INDEPENDENTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_FASE10_VALIDACAO_INDEPENDENTE_V1.json), blob `1321b70bd2c704965120b311cbaed5fa5a02ac2c`.
- FASE11: `CERTIFICADO`, decisão `LIBERADO_PARA_FASE12`; zero bloqueadores, 25 campos conferidos e zero divergências, hashes RAW/NORMALIZED confirmados. Evidência: [COTAHIST_2016_FASE11_CERTIFICACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_FASE11_CERTIFICACAO_V1.json), blob `dfc06ea03afad14bd1f0d218ddba246b07f0ed92`.
- FASE12: `FECHADO_COM_TRANSICAO_CONTROLADA`, decisão `FECHAR_2016_E_AUTORIZAR_CONTINUACAO_2017`; zero bloqueadores. RAW 2017 coincide com manifesto/sidecar, ZIP com um membro, zero comprimentos inválidos, 489.115 registos tipo 01. NORMALIZED CSV 2017 ausente; FASE04 de 2017 aguarda reconstrução. Evidência: [COTAHIST_2016_FASE12_FECHAMENTO_2017_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_FASE12_FECHAMENTO_2017_ABERTURA_V1.json), commit `39d371d4f683c3f668e71eddec4e951f0a99dba5`.

### COTAHIST 2017 — estado inicial após transição

- FASE12 de 2016 autorizou a continuação de 2017 sem certificar o novo ano.
- RAW 2017 SHA-256: `af6aaa85187c1d58ec6565522644066da573a7dc5b579c1d4c906ae95a2dea86`, coincide com manifesto e sidecar; ZIP íntegro, 489.115 registos tipo 01.
- FASE00: `VALIDADO`, decisão `AUTORIZAR_FASE01`; evidência blob `46ba901d23e828660382b3efbf782697db8956ef`.
- FASE01: `VALIDADO`, decisão `LIBERADO_PARA_FASE02`; RAW SHA coincide com manifesto/sidecar; evidência commit `0799b784e37685c0c9d332d3fe56c431a5428a78`.
- FASE02: `VALIDADO`, decisão `LIBERADO_PARA_FASE03`; ZIP íntegro, um membro, registos de 245 bytes, 489.115 registos tipo 01; evidência commit `1c023edfc00c5196267c14865645ba5cc9254ea8`.
- FASE03: `VALIDADO`, decisão `LIBERADO_PARA_FASE04`; zero comprimentos/datas inválidos, intervalo 2017-01-02 a 2017-12-28; evidência commit `b2fbad14e03f05eecc63b66ea7c673c43b5bbdf0`.
- FASE04: workflow publicado em `.github/workflows/cotahist-fase04-normalizacao-2017-v1.yml` (commit `ef2652d24e472b601a79e44f940aa60250c1c1b6`), com duas atualizações de gatilho. O NORMALIZED CSV e a evidência FASE04 ainda não foram encontrados; a execução precisa ser confirmada antes de avançar para FASE05. Manifesto existente espera 489.115 linhas, 25 campos e SHA-256 `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`.

## 4. Roadmap por marco

| Marco | Estado verificado | Próxima ação |
|---|---|---|
| COTAHIST 1986–2003 | Histórico com exceções específicas por ano | Preservar evidências; não presumir uniformidade |
| COTAHIST 2004–2013 | Ciclos anteriores registrados como concluídos/fechados, com exceções de calendário documentadas por ano | Não reexecutar sem causa/evidência |
| COTAHIST 2010 | FASE00–FASE12 concluídas; FASE11 certificado; FASE12 fechado com transição controlada | Preservar exceção de calendário oficial histórico não persistido |
| COTAHIST 2014 | FASE00–FASE12 concluídas; FASE11 `CERTIFICADO`; FASE12 `FECHADO_COM_TRANSICAO_CONTROLADA` | Preservar evidências e não reabrir sem causa concreta |
| COTAHIST 2015 | FASE00–FASE12 concluídas; FASE11 `CERTIFICADO`; FASE12 `FECHADO_COM_TRANSICAO_CONTROLADA` | Preservar evidências e não reabrir sem causa concreta |
| COTAHIST 2016 | FASE00–FASE12 concluídas; FASE11 `CERTIFICADO`; FASE12 `FECHADO_COM_TRANSICAO_CONTROLADA` | Preservar evidências e não reabrir sem causa concreta |
| COTAHIST 2017 | FASE00–FASE03 validadas; FASE04 de normalização pendente de evidência | Confirmar NORMALIZED físico contra manifesto/sidecar antes de FASE05 |
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

A FASE08 de 2014 foi validada com exceções classificadas; o Gate 06–08 foi aprovado com decisão `LIBERADO_PARA_FASE09`. A FASE09 foi liberada para FASE10. A FASE10 verificou independentemente os 25 campos RAW × NORMALIZED: 392.228 registos de cada lado, zero divergências, hash RAW `613d76f8a64c7ffba0406cb54c1fd187266f55ed8b6037cb85993b2071a5aae7` e hash NORMALIZED `af95fc567d875a2ba09221f4749cddae22281baf36145e9066021e2d13533c01`; evidência commit `075873272ce06a78d1765ab2cb6503d99d47345e`. A FASE11 foi certificada no commit `ef0ba2e70ccc05ea00649c1869fb0d036f09c4fb`. A FASE12 fechou 2014 e autorizou continuação para 2015 no commit `0e5c089c0ad700c689e13a7e2ef3de8458f4d9e7`. O CSV NORMALIZED de 2015 está ausente; a FASE04 de 2015 não está concluída. A REC-001 B3 × BLOOMBERG_MAIL continua bloqueada em trilha independente.



## 10. Retificação do estado operacional — 2026-10-13 (verificação posterior)

Esta secção prevalece como estado operacional mais recente sobre referências anteriores a 2014 como ciclo ativo. As secções anteriores são preservadas como histórico de execução.

### COTAHIST 2016 — encerramento confirmado

- FASE10: `VALIDADO`; 466.734 registos RAW e NORMALIZED; 25 campos comparados; zero divergências; `raw_modified=false`; `deduplication_performed=false`. Evidência: [COTAHIST_2016_FASE10_VALIDACAO_INDEPENDENTE_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_FASE10_VALIDACAO_INDEPENDENTE_V1.json).
- FASE11: `CERTIFICADO`; decisão `LIBERADO_PARA_FASE12`; zero bloqueadores. Evidência: [COTAHIST_2016_FASE11_CERTIFICACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_FASE11_CERTIFICACAO_V1.json).
- FASE12: `FECHADO_COM_TRANSICAO_CONTROLADA`; decisão `FECHAR_2016_E_AUTORIZAR_CONTINUACAO_2017`. O RAW 2017 foi verificado, mas esta transição não certifica 2017. Evidência: [COTAHIST_2016_FASE12_FECHAMENTO_2017_ABERTURA_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2016_FASE12_FECHAMENTO_2017_ABERTURA_V1.json).

### COTAHIST 2017 — estado ativo

- RAW SHA-256: `af6aaa85187c1d58ec6565522644066da573a7dc5b579c1d4c906ae95a2dea86`, igual ao manifesto e sidecar.
- FASE03: `VALIDADO`, decisão `LIBERADO_PARA_FASE04`; 489.115 registos tipo 01, 245 bytes por registo, zero comprimentos inválidos, zero datas inválidas, intervalo 2017-01-02 a 2017-12-28. Evidência: [COTAHIST_2017_FASE03_PARSING_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE03_PARSING_V1.json).
- FASE04: **PENDENTE DE EXECUÇÃO VERIFICÁVEL**. Workflow publicado: [cotahist-fase04-normalizacao-2017-v1.yml](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase04-normalizacao-2017-v1.yml). A branch consultada não contém `dados/cotahist/quality/COTAHIST_2017_FASE04_NORMALIZACAO_V1.json` nem `dados/cotahist/normalized/anual/COTAHIST_A2017.csv`; portanto, commits de alteração do workflow não são considerados prova de execução.
- O manifesto de NORMALIZED existente declara 489.115 linhas, 25 campos e hash esperado `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`. A FASE04 deve regenerar o CSV com o script canónico, comparar hash calculado com manifesto e sidecar e só publicar o CSV quando o resultado for `VALIDADO`.
- A consulta de estado do commit não retornou checks; não há evidência suficiente para afirmar sucesso ou falha de um run específico. A execução seguinte requer disparo explícito de `workflow_dispatch` no workflow FASE04 de 2017, seguido de verificação da evidência persistida e do CSV.

### Roadmap operacional atualizado

1. **FASE04 — 2017:** disparar o workflow; validar hash RAW, hash NORMALIZED, manifesto, sidecar, 25 campos, 489.115 linhas, datas e zero bloqueadores. Não avançar se a evidência estiver ausente ou bloqueada.
2. **FASE05 — 2017:** só após FASE04 `VALIDADO`; reconciliar integridade física, manifesto, sidecars, schema e contagens.
3. **FASE06–08 — 2017:** reconciliação RAW×NORMALIZED, identidade/chaves sem remoção de linhas e consistência temporal; manter exceções explícitas.
4. **Gate 06–08 → FASE09 → FASE10:** exigir evidência persistida em cada etapa e validação independente dos 25 campos.
5. **FASE11 → FASE12:** certificar e fechar 2017 apenas após gates anteriores concluídos; transição para 2018 não certifica automaticamente o novo ano.
6. **Pista paralela bloqueada:** REC-001 B3 × BLOOMBERG_MAIL continua `BLOCKED_ORDER_VARIANCE_REVIEW`; não declarar a diferença de multiplicidades como mera extensão temporal sem reconciliação por data.

**Regra de avanço:** nenhuma fase é marcada como concluída por existir workflow, por commit de código ou por hash esperado no manifesto. É necessária evidência de resultado produzida e persistida, reconciliada com os artefactos físicos.


## 11. Atualização após evidência FASE04 de 2017

Verificação posterior na branch `main` encontrou a evidência FASE04 que não estava disponível na consulta anterior. Esta secção prevalece para o estado atual; o histórico anterior permanece preservado.

### FASE04 — 2017: VALIDADO

- Evidência: [COTAHIST_2017_FASE04_NORMALIZACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE04_NORMALIZACAO_V1.json).
- Estado: `VALIDADO`; decisão `LIBERADO_PARA_FASE05`; lista de bloqueadores vazia.
- RAW SHA-256: `af6aaa85187c1d58ec6565522644066da573a7dc5b579c1d4c906ae95a2dea86`.
- NORMALIZED SHA-256 calculado, manifesto e sidecar coincidem: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`.
- Resultado: 489.115 linhas, 25 campos; primeira data 2017-01-02; última data 2017-12-28; zero datas inválidas e zero datas fora do ano.
- Diagnóstico registado: normalizador versão 1.1.2, retorno 0; `raw_modified=false`; `deduplication_performed=false`.
- O manifesto ainda declara parser 1.1.0 enquanto o script canónico é 1.1.2. Como o hash calculado coincide com manifesto e sidecar, a diferença de metadado fica registada e não invalida isoladamente o resultado.

### FASE05 — 2017: workflow publicado; evidência ainda pendente

- Workflow: [cotahist-fase05-manifesto-checksum-2017-v1.yml](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase05-manifesto-checksum-2017-v1.yml).
- Commit do workflow: [35ab6578b7995557fd3c7ffa3a08afea831fbade](https://github.com/carlos-andrade/B3/commit/35ab6578b7995557fd3c7ffa3a08afea831fbade).
- O workflow revalida fisicamente RAW/ZIP, manifesto de aquisição, sidecar RAW, NORMALIZED, manifesto NORMALIZED, sidecar NORMALIZED, contagem de linhas, 25 campos e intervalo de datas.
- A evidência esperada `dados/cotahist/quality/COTAHIST_2017_FASE05_MANIFESTO_CHECKSUM_V1.json` ainda não foi encontrada na branch na última consulta. Portanto, FASE05 permanece pendente; não promover para FASE06 sem a evidência persistida.
- A existência do workflow e o commit que o publicou não provam que o job executou. Se a evidência não surgir automaticamente, executar manualmente via GitHub Actions: **Run workflow** na branch `main`.

### Roadmap operacional imediato

1. Confirmar execução e persistência da FASE05 2017.
2. Se `VALIDADO`, criar/executar FASE06 para reconciliar 12 campos críticos RAW × NORMALIZED, sem deduplicar.
3. FASE07: auditar chaves e colisões sem remover linhas.
4. FASE08 e Gate 06–08: consistência temporal e classificação explícita de exceções.
5. Só depois avançar sequencialmente por FASE09, FASE10 independente dos 25 campos, FASE11 certificação e FASE12 fechamento/transição para 2018.
6. Manter `REC-001 B3 × BLOOMBERG_MAIL` bloqueada até à revisão da divergência de multiplicidades por data.

**Regra de promoção:** artefactos, hashes e contagens verificados na branch são necessários; workflow publicado sem evidência persistida não é conclusão de fase.


## 12. Verificação FASE05 e preparação FASE06 — 2017

Verificação realizada em 2026-10-13 na branch `main`: a evidência FASE05 foi encontrada e validada.

### FASE05 — 2017: VALIDADO

- Evidência: [COTAHIST_2017_FASE05_MANIFESTO_CHECKSUM_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE05_MANIFESTO_CHECKSUM_V1.json).
- Estado/decisão: `VALIDADO` / `LIBERADO_PARA_FASE06`.
- RAW SHA-256 calculado, manifesto e sidecar coincidem: `af6aaa85187c1d58ec6565522644066da573a7dc5b579c1d4c906ae95a2dea86`.
- NORMALIZED SHA-256 calculado, manifesto e sidecar coincidem: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`.
- ZIP: membro único `COTAHIST_A2017.TXT`; teste `PASS`.
- Contagem: 489.115 linhas, 25 campos; intervalo 2017-01-02 a 2017-12-28.
- `raw_modified=false`; `deduplication_performed=false`.
- Limite: reconciliação semântica linha a linha fica para FASE06.

### FASE06 — 2017: workflow publicado; resultado ainda pendente

- Workflow: [cotahist-fase06-reconciliacao-2017-v1.yml](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase06-reconciliacao-2017-v1.yml).
- Commit do workflow: https://github.com/carlos-andrade/B3/commit/f1056ff82766d12c8e3e08606a594b3469f9d8d2.
- Escopo: reconciliação de 12 campos críticos RAW × NORMALIZED, sem alterar RAW e sem deduplicar; a avaliação de chaves permanece na FASE07.
- A FASE06 só será promovida após a evidência `dados/cotahist/quality/COTAHIST_2017_FASE06_RECONCILIACAO_V1.json` estar persistida e auditada. A criação do workflow não prova execução.
- Próxima ação: executar manualmente **Run workflow** na branch `main`, caso o push não tenha iniciado a execução, e depois verificar a evidência.

### Roadmap operacional após esta verificação

1. FASE05 2017: concluída e validada.
2. FASE06 2017: workflow publicado; aguardando execução/evidência de reconciliação de 12 campos críticos.
3. FASE07 2017: chaves e cardinalidade, sem remover linhas; depende da FASE06 validada.
4. FASE08 + Gate 06–08: calendário e consistência temporal, com exceções explícitas.
5. FASE09 → FASE10: pré-release e validação independente dos 25 campos.
6. FASE11 → FASE12: certificação, fechamento e transição controlada para 2018.
7. REC-001 B3 × BLOOMBERG_MAIL continua bloqueada em trilha independente por divergência de multiplicidades/ordem; não contornar pela certificação anual.

**Regra de promoção:** não avançar de fase sem evidência persistida, hashes e contagens reconciliados.

## 13. FASE06 validada e FASE07 preparada — COTAHIST 2017

Verificação realizada em 2026-10-13 na branch `main`.

### FASE06 — 2017: VALIDADO

- Evidência: [COTAHIST_2017_FASE06_RECONCILIACAO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE06_RECONCILIACAO_V1.json).
- Commit da evidência: [6c1dc3e5f1476642de5e2060c62200017b0d26b9](https://github.com/carlos-andrade/B3/commit/6c1dc3e5f1476642de5e2060c62200017b0d26b9).
- Estado/decisão: `VALIDADO` / `LIBERADO_PARA_FASE07`.
- Registos RAW e NORMALIZED: 489.115 em cada lado.
- Campos críticos comparados: 12; divergências: zero; amostra de divergências vazia.
- Hash RAW: `af6aaa85187c1d58ec6565522644066da573a7dc5b579c1d4c906ae95a2dea86`.
- Hash NORMALIZED: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`.
- A evidência mantém a avaliação da unicidade da chave para a FASE07; `raw_immutable=true`; `deduplication_performed=false`.

### FASE07 — 2017: workflow publicado; evidência pendente

- Workflow: [cotahist-fase07-identidade-2017-v1.yml](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase07-identidade-2017-v1.yml).
- Commit do workflow: [e8f0e666bfba12fd084005f969efa5ac7c361812](https://github.com/carlos-andrade/B3/commit/e8f0e666bfba12fd084005f969efa5ac7c361812).
- O workflow testa a chave-base `data_pregao+codbdi+codneg+tpmerc+dismes` e a candidata com `prazot`, preservando todos os registos e emitindo amostras de colisões.
- A evidência `dados/cotahist/quality/COTAHIST_2017_FASE07_IDENTIDADE_CHAVES_V1.json` ainda não estava presente na consulta pós-publicação. FASE07 permanece pendente de resultado; a existência do workflow não prova a execução.

### Roadmap operacional imediato

1. FASE05 2017: VALIDADO.
2. FASE06 2017: VALIDADO; 489.115 registos, 12 campos críticos, zero divergências.
3. FASE07 2017: workflow publicado; executar/verificar a evidência de identidade e cardinalidade.
4. FASE08 2017 e Gate 06–08: dependem da FASE07 validada.
5. FASE09 → FASE10 independente dos 25 campos → FASE11 certificação → FASE12 fechamento/transição para 2018.
6. REC-001 B3 × BLOOMBERG_MAIL permanece em trilha separada, bloqueada até reconciliação da divergência de multiplicidades/ordem.

**Regra de promoção:** nenhuma fase posterior é promovida sem evidência própria persistida e validação dos respetivos pré-requisitos. Nenhuma linha pode ser removida ou deduplicada para forçar unicidade.

## 14. FASE07 validada e FASE08 preparada — COTAHIST 2017

Verificação realizada em 2026-10-13 na branch `main`; esta secção prevalece sobre estados operacionais anteriores, preservados como histórico.

### FASE07 — 2017: VALIDADO

- Evidência: [COTAHIST_2017_FASE07_IDENTIDADE_CHAVES_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE07_IDENTIDADE_CHAVES_V1.json).
- Commit da evidência: [81cc956e515b4455833d54711ed53362e99ae7a0](https://github.com/carlos-andrade/B3/commit/81cc956e515b4455833d54711ed53362e99ae7a0).
- Estado/decisão: `VALIDADO` / `CHAVE_CANDIDATA_COM_PRAZOT_VALIDADA_POR_CARDINALIDADE`.
- Registos: 489.115; hash NORMALIZED coincide com a FASE06: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`.
- Chave-base `data_pregao+codbdi+codneg+tpmerc+dismes`: 7.560 grupos duplicados e 15.256 linhas excedentes; todos os 7.560 grupos contêm diferenças entre linhas.
- Chave candidata `data_pregao+codbdi+codneg+tpmerc+prazot+dismes`: 489.115 chaves distintas, zero grupos duplicados e zero linhas excedentes.
- `deduplication_performed=false`; `source_rows_removed=0`.
- Limitação: decisão específica para o NORMALIZED 2017; não autoriza deduplicação nem generalização automática para outros anos.

### FASE08 — 2017: workflow publicado; execução/evidência pendente

- Workflow: [cotahist-fase08-calendario-2017-v1.yml](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase08-calendario-2017-v1.yml).
- Commit do workflow: [e9c04b7cfa6cbc5a80b20294743eb3e820720db0](https://github.com/carlos-andrade/B3/commit/e9c04b7cfa6cbc5a80b20294743eb3e820720db0).
- O workflow foi adaptado do contrato de FASE08 de 2016; verificado que não contém referências residuais a 2016. Consome NORMALIZED 2017 e evidências FASE06/FASE07, testa datas inválidas/fora do ano, regressões cronológicas, consistência temporal por instrumento, distribuição de dias e intervalos; preserva a ordem da fonte e não remove linhas.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2017_FASE08_SEMANTICA_CALENDARIO_V1.json`.
- A FASE08 ainda não está concluída. Executar `workflow_dispatch` na branch `main` se o push não iniciar a execução; só promover após conferir evidência, hash NORMALIZED, contagens, exceções e decisão.

### Roadmap operacional atualizado

1. FASE05 2017: VALIDADO.
2. FASE06 2017: VALIDADO — 489.115 registos, 12 campos críticos, zero divergências.
3. FASE07 2017: VALIDADO — chave candidata com `prazot`, zero colisões, nenhuma linha removida.
4. FASE08 2017: workflow publicado; aguarda execução e evidência persistida.
5. Gate 06–08: depende da FASE08 auditada; classificar exceções sem assumir calendário oficial externo não persistido.
6. FASE09 → FASE10 independente dos 25 campos → FASE11 certificação → FASE12 fechamento/transição controlada para 2018, sequencialmente e com evidência própria.
7. REC-001 B3 × BLOOMBERG_MAIL continua bloqueada em trilha independente até reconciliação da divergência de multiplicidades/ordem.

**Regra de promoção:** workflow publicado ou commit de código não prova conclusão. Não avançar para Gate 06–08 antes de a evidência FASE08 estar persistida e validada.


## 15. FASE08 validada com exceção; Gate 06–08 preparado — COTAHIST 2017

Verificação da evidência na branch `main`, em 2026-10-13.

### FASE08 — 2017: VALIDADO_COM_EXCECAO

- Evidência: [COTAHIST_2017_FASE08_SEMANTICA_CALENDARIO_V1.json](https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE08_SEMANTICA_CALENDARIO_V1.json).
- Estado/decisão: `VALIDADO_COM_EXCECAO` / `LIBERADO_PARA_GATE_06_08`; zero bloqueadores.
- NORMALIZED SHA-256: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`, igual à FASE06 e FASE07.
- Registos verificados: 489.115; 246 datas de negociação; intervalo 2017-01-02 a 2017-12-28.
- Datas inválidas/fora do ano: zero; regressões cronológicas: zero; regressões temporais por instrumento: zero; datas de fim de semana observadas: zero.
- Métrica lexicográfica informativa: 109.824 transições decrescentes da tupla de instrumento; explicitamente não bloqueadora e não confundida com regressão temporal.
- Exceções explícitas: calendário oficial histórico externo não persistido; intervalo de cinco dias entre 2017-02-24 e 2017-03-01. A fase não afirma equivalência com calendário oficial externo.
- `deduplication_performed=false`; `rows_removed=0`.

### Gate 06–08 — 2017: workflow publicado; evidência pendente

- Workflow: [cotahist-gate-06-08-2017-v1.yml](https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-gate-06-08-2017-v1.yml).
- Commit do workflow: [2c90b89335666d4cc911e49ea581b7ef9ef8f71d](https://github.com/carlos-andrade/B3/commit/2c90b89335666d4cc911e49ea581b7ef9ef8f71d).
- O gate revalida fisicamente o NORMALIZED, hash, 489.115 registos, 25 campos, datas, ausência de regressões cronológicas, hashes de FASE06/FASE07/FASE08, classificação das exceções e preservação de todas as linhas.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2017_GATE_06_08_V1.json`. Não foi encontrada na consulta após publicação do workflow; portanto, o Gate ainda não está aprovado e a FASE09 não está autorizada.

### Roadmap operacional

1. FASE05–FASE07 2017: VALIDADO.
2. FASE08 2017: VALIDADO_COM_EXCECAO, LIBERADO_PARA_GATE_06_08.
3. Gate 06–08 2017: workflow publicado; aguarda execução e evidência persistida.
4. FASE09: bloqueada até o Gate produzir decisão `LIBERADO_PARA_FASE09` sem bloqueadores.
5. FASE10 independente (25 campos) → FASE11 certificação → FASE12 fechamento/transição para 2018, apenas após os gates anteriores.
6. REC-001 B3 × BLOOMBERG_MAIL permanece bloqueada em trilha independente.

**Regra de promoção:** a evidência da FASE08 autoriza a execução do Gate, não substitui o Gate. Não promover para FASE09 com base apenas no status da FASE08 ou na publicação do workflow.


---

## Secção 16 — Gate 06–08 aprovado e FASE09 2017 preparada (2026-10-13)

### Evidência verificada
- Gate: `dados/cotahist/quality/COTAHIST_2017_GATE_06_08_V1.json`
- Estado: `VALIDADO_COM_EXCECAO`
- Decisão: `LIBERADO_PARA_FASE09`
- Bloqueadores: zero.
- Linhas verificadas: 489.115; campos: 25; datas de negociação: 246.
- SHA-256 NORMALIZED: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`.
- Regressões cronológicas e regressões temporais por instrumento: zero.
- Sem deduplicação e sem remoção de linhas.
- Exceções não bloqueantes mantidas explicitamente no JSON do Gate.

### FASE09 — workflow publicado
- Workflow: `.github/workflows/cotahist-fase09-prerelease-2017-v1.yml`
- Execução manual disponível via `workflow_dispatch`; também é acionado por alterações nas dependências monitorizadas.
- Commit de publicação: `f3918b6de8f86fdbf3e42a24242bae8f793da331`
- A FASE09 consolida evidências anteriores, valida hashes/contagens e verifica o Gate; não executa nem certifica a FASE10.
- **Estado da fase: PREPARADA; evidência FASE09 ainda por confirmar.** A criação do workflow não prova que o workflow já executou com sucesso.

### Próxima ação e regra de avanço
1. Executar o workflow `COTAHIST 2017 - FASE09 Pre-Release` no GitHub Actions, branch `main`, caso não tenha iniciado automaticamente.
2. Confirmar a criação e validar `dados/cotahist/quality/COTAHIST_2017_FASE09_PRE_RELEASE_V1.json`.
3. Só avançar para a FASE10 se a evidência indicar `status=LIBERADO_PARA_FASE10`, sem itens em `missing` nem `blocked`, com hashes e contagens consistentes.
4. Manter a trilha REC-001 B3 × BLOOMBERG_MAIL bloqueada e independente até validação própria.



---

## Secção 17 — FASE09 validada e FASE10 publicada para 2017 (2026-10-13)

### FASE09 — evidência verificada
- Evidência: `dados/cotahist/quality/COTAHIST_2017_FASE09_PRE_RELEASE_V1.json`
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE09_PRE_RELEASE_V1.json
- Estado/decisão: `LIBERADO_PARA_FASE10`.
- Preconditions: FASE03–08, Gate 06–08, RAW, NORMALIZED e MANIFEST = `OK`.
- `missing=[]`; `blocked=[]`.
- RAW SHA-256: `af6aaa85187c1d58ec6565522644066da573a7dc5b579c1d4c906ae95a2dea86`.
- NORMALIZED SHA-256: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`.
- Data de validação da evidência: `2026-10-13T12:13:36.165014+00:00`.

### FASE10 — workflow publicado
- Workflow: `.github/workflows/cotahist-fase10-validacao-independente-2017-v1.yml`
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase10-validacao-independente-2017-v1.yml
- Commit de publicação: `8c1a71a65db96dc649aa609b1034416449f1d970`.
- Base técnica: workflow de validação independente já usado para 2016, parametrizado para 2017.
- A execução reconcilia independentemente os 25 campos do RAW com o NORMALIZED, valida hashes e contagens e persiste a evidência da FASE10, inclusive em caso de bloqueio.
- **Estado atual: WORKFLOW PUBLICADO; execução/evidência FASE10 ainda por confirmar.** Não declarar a validação independente concluída apenas com a publicação do workflow.

### Próxima ação
1. Executar `COTAHIST 2017 - FASE10 Validacao Independente Integral` na branch `main`, caso não tenha iniciado automaticamente.
2. Validar `dados/cotahist/quality/COTAHIST_2017_FASE10_VALIDACAO_INDEPENDENTE_V1.json`.
3. Só liberar FASE11 quando `status=VALIDADO`, `decision=LIBERADO_PARA_FASE11`, `mismatch_count=0`, `raw_record_count=normalized_record_count=489115`, `field_count=25`, hashes consistentes e sem bloqueadores.
4. Manter RAW imutável, sem deduplicação ou remoção de linhas. REC-001 B3 × BLOOMBERG_MAIL continua em trilha independente.



---

## Secção 18 — FASE10 validada e FASE11 publicada para 2017 (2026-10-13)

### FASE10 — evidência verificada
- Evidência: `dados/cotahist/quality/COTAHIST_2017_FASE10_VALIDACAO_INDEPENDENTE_V1.json`
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE10_VALIDACAO_INDEPENDENTE_V1.json
- Estado: `VALIDADO`; decisão: `LIBERADO_PARA_FASE11`.
- Tipo: validação independente RAW → NORMALIZED, todos os campos.
- Registos RAW: 489.115; registos NORMALIZED: 489.115; tamanho dos registos: 245 bytes.
- Campos comparados: 25; divergências: 0; amostra de divergências vazia.
- RAW SHA-256: `af6aaa85187c1d58ec6565522644066da573a7dc5b579c1d4c906ae95a2dea86`.
- NORMALIZED SHA-256: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`.
- `raw_modified=false`; `deduplication_performed=false`.
- Timestamp da evidência: `2026-10-13T12:17:07.977714+00:00`.

### FASE11 — workflow de certificação publicado
- Workflow: `.github/workflows/cotahist-fase11-certificacao-2017-v1.yml`
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase11-certificacao-2017-v1.yml
- Commit de publicação: `09c4a918e245d85b6ba32800fe944e2d637c1f6f`.
- Base técnica: workflow de certificação 2016, parametrizado para 2017.
- Verifica FASE09, FASE10, Gate 06–08, manifesto, hashes, 25 campos e zero divergências.
- **Estado: WORKFLOW PUBLICADO; execução/evidência FASE11 ainda por confirmar.** A publicação não equivale a certificação concluída.

### Próxima ação
1. Executar `COTAHIST 2017 - FASE11 Certificacao` na branch `main`, caso não tenha iniciado automaticamente.
2. Verificar `dados/cotahist/quality/COTAHIST_2017_FASE11_CERTIFICACAO_V1.json`.
3. Só liberar FASE12 se a evidência indicar `status=CERTIFICADO`, `decision=LIBERADO_PARA_FASE12` e `blockers=[]`.
4. Preservar RAW e NORMALIZED; sem deduplicação ou remoção de linhas. REC-001 B3 × BLOOMBERG_MAIL permanece uma trilha independente.



---

## Secção 19 — FASE11 certificada e FASE12 publicada para 2017→2018 (2026-10-13)

### FASE11 — certificação verificada
- Evidência: `dados/cotahist/quality/COTAHIST_2017_FASE11_CERTIFICACAO_V1.json`
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE11_CERTIFICACAO_V1.json
- Estado: `CERTIFICADO`; decisão: `LIBERADO_PARA_FASE12`.
- Bloqueadores: zero.
- FASE10: `VALIDADO`; divergências: 0; campos verificados: 25.
- Hashes certificados:
  - RAW: `af6aaa85187c1d58ec6565522644066da573a7dc5b579c1d4c906ae95a2dea86`
  - NORMALIZED: `3f56da73cfe270b78c9e5e955efddfb7b61702d12f5954f3f3468464a619a0db`
- Timestamp da certificação: `2026-10-13T12:18:26.279850+00:00`.
- Âmbito: integridade e consistência COTAHIST 2017 conforme evidências FASE00–10; não certifica estratégias de investimento e não autoriza deduplicação.

### FASE12 — workflow de fechamento/transição publicado
- Workflow: `.github/workflows/cotahist-fase12-fechamento-2017-abertura-2018-v1.yml`
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase12-fechamento-2017-abertura-2018-v1.yml
- Commit: `1bcba36cc0c85845d4e8f603c91636092fb80516`.
- O workflow foi parametrizado a partir do fluxo de fechamento/transição 2016→2017 para fechar 2017 após certificação e verificar a integridade do RAW 2018.
- Manifesto e sidecar de checksum de 2018 estão presentes e declaram SHA-256 `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`; o ZIP binário não foi lido diretamente nesta verificação, portanto a integridade estrutural será confirmada pelo workflow.
- **Estado: WORKFLOW PUBLICADO; evidência FASE12 ainda por confirmar.** A publicação não equivale a fechamento concluído nem certifica 2018.

### Próxima ação
1. Executar `COTAHIST 2017 - FASE12 Fechamento e Transicao 2018` na branch `main`, caso não tenha iniciado automaticamente.
2. Validar `dados/cotahist/quality/COTAHIST_2017_FASE12_FECHAMENTO_2018_ABERTURA_V1.json`.
3. Só considerar 2017 fechado se a evidência indicar `FECHADO_COM_TRANSICAO_CONTROLADA`, decisão `FECHAR_2017_E_AUTORIZAR_CONTINUACAO_2018` e `blockers=[]`.
4. A transição não certifica 2018. A FASE04/etapas subsequentes de 2018 permanecem condicionadas à existência e validação do NORMALIZED.
5. Preservar RAW e registos: nenhuma deduplicação ou remoção. REC-001 B3 × BLOOMBERG_MAIL continua independente.



---

## Secção 20 — FASE12 validada; ciclo 2018 preparado com gate de governação (2026-10-13)

### FASE12 — fechamento de 2017 e transição para 2018
- Evidência: `dados/cotahist/quality/COTAHIST_2017_FASE12_FECHAMENTO_2018_ABERTURA_V1.json`
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2017_FASE12_FECHAMENTO_2018_ABERTURA_V1.json
- Estado: `FECHADO_COM_TRANSICAO_CONTROLADA`.
- Decisão: `FECHAR_2017_E_AUTORIZAR_CONTINUACAO_2018`.
- Bloqueadores: zero.
- FASE10 2017: `VALIDADO`; FASE11 2017: `CERTIFICADO`.
- RAW 2018 SHA-256 calculado = manifesto = sidecar: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`.
- ZIP: 1 membro; 580.155 registos tipo 01; zero comprimentos inválidos; header 00 e trailer 99 presentes.
- NORMALIZED CSV 2018 ausente; FASE04 continua por executar/validar. A FASE12 não certifica 2018.
- O workflow FASE12 foi ajustado para `lfs: true`, para garantir leitura do ficheiro RAW real no runner.
- Commit do workflow: `827e82a5631683404a912a09bc835268373e5e36`.

### Ciclo 2018 — FASE00 publicada, evidência pendente
- Workflow: `.github/workflows/cotahist-fase00-governanca-2018-v1.yml`
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase00-governanca-2018-v1.yml
- Commit da correção LFS: `971e60d337e5fc87eff8ba5dd746766cfc6aba6a`.
- A FASE00 valida a autorização da transição, o Layout Mestre, a proveniência e a presença dos artefactos 2018.
- **Estado: workflow publicado; evidência FASE00 ainda não encontrada.** O avanço para FASE01/FASE02 fica condicionado à evidência `COTAHIST_2018_FASE00_GOVERNANCA_V1.json` com decisão `AUTORIZAR_FASE01`.

### Próximos passos
1. Executar manualmente `COTAHIST 2018 - FASE00 Governanca e Pre-condicoes` na branch `main`, se não tiver iniciado automaticamente.
2. Verificar a evidência FASE00 antes de criar/acionar a FASE01; depois seguir sequencialmente FASE01 → FASE02 → FASE03 → FASE04.
3. FASE04 deve regenerar o NORMALIZED usando o script canónico e só publicar o CSV se hash, contagem, esquema e datas coincidirem com o manifesto/sidecar existentes.
4. Sem deduplicação e sem remoção de linhas. REC-001 B3 × BLOOMBERG_MAIL continua independente.



---

## Secção 21 — FASE00 2018 validada; FASE01 preparada (2026-10-13)

### FASE00 — governação e pré-condições
- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE00_GOVERNANCA_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE00_GOVERNANCA_V1.json
- Estado: `VALIDADO`; decisão: `AUTORIZAR_FASE01`; bloqueadores: zero.
- Transição 2017→2018 confirmada como `FECHADO_COM_TRANSICAO_CONTROLADA`.
- Layout Mestre: versão 1.0.1; RAW, manifesto e sidecar presentes.
- CSV NORMALIZED ausente de forma esperada nesta etapa; a reconstrução pertence à FASE04, depois das FASE01–03.
- Commit de evidência observado: `316cb5cd27f4d7fe3d72f3d09462922b889f3586`.

### FASE01 — workflow publicado; evidência pendente
- Workflow: `.github/workflows/cotahist-fase01-aquisicao-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase01-aquisicao-2018-v1.yml
- Commit de publicação: `f8f804cd71beeb7c17fd5d88335778cc2ff78595`.
- O workflow valida a autorização FASE00, proveniência B3 e coincidência do SHA-256 físico do RAW com manifesto e sidecar. O checkout usa Git LFS e a evidência identifica a verificação como retrospectiva do RAW já persistido.
- Hash esperado do RAW 2018: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`.
- A consulta posterior à publicação ainda não encontrou `dados/cotahist/quality/COTAHIST_2018_FASE01_AQUISICAO_RAW_V1.json`. Portanto, FASE01 permanece pendente; não presumir que o workflow terminou com sucesso só porque o commit existe.

### Roadmap operacional imediato
1. FASE00 2018: VALIDADO; autorização explícita para FASE01.
2. FASE01 2018: workflow publicado; aguarda evidência persistida e confirmação de `status=VALIDADO`, `decision=LIBERADO_PARA_FASE02`, hash RAW = manifesto = sidecar.
3. Só após validar a evidência FASE01, preparar/executar FASE02; depois FASE03.
4. FASE04 deve regenerar o CSV com o script canónico e comparar hash, contagem, esquema e datas com manifesto/sidecar existentes; registar a diferença de versão do parser sem a ocultar.
5. RAW imutável; sem deduplicação e sem remoção de linhas. REC-001 B3 × BLOOMBERG_MAIL continua numa trilha independente e bloqueada até reconciliação própria.


---

## Secção 22 — FASE01 validada; FASE02 preparada — COTAHIST 2018 (2026-10-13)

### FASE01 — aquisição/proveniência do RAW: VALIDADO
- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE01_AQUISICAO_RAW_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE01_AQUISICAO_RAW_V1.json
- Estado/decisão: `VALIDADO` / `LIBERADO_PARA_FASE02`.
- Tipo de evidência: verificação retrospectiva do RAW já persistido; não representa uma nova aquisição.
- Proveniência: B3; manifesto `VALIDADO`; SHA-256 físico = manifesto = sidecar = FASE01: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`.
- Evidência validada em `2026-10-13T14:18:28.442385+00:00`; commit do workflow FASE01: `f8f804cd71beeb7c17fd5d88335778cc2ff78595`.

### FASE02 — workflow publicado; evidência pendente
- Workflow: `.github/workflows/cotahist-fase02-integridade-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase02-integridade-2018-v1.yml
- Commit de publicação: `2c0458b174972531845d9918030639841f473725`.
- O workflow exige FASE01 validada e confirma SHA-256, integridade do ZIP, membro único, comprimentos de 245 bytes e presença de header `00`, cotações `01` e trailer `99`. Checkout configurado com Git LFS.
- A consulta após a publicação não encontrou `dados/cotahist/quality/COTAHIST_2018_FASE02_INTEGRIDADE_FONTE_V1.json`; logo, FASE02 ainda não pode ser considerada concluída.

### Roadmap operacional imediato
1. FASE00 2018: VALIDADO; `AUTORIZAR_FASE01`.
2. FASE01 2018: VALIDADO; `LIBERADO_PARA_FASE02`; hashes coincidentes.
3. FASE02 2018: workflow publicado; aguarda evidência persistida `VALIDADO` / `LIBERADO_PARA_FASE03`.
4. Só após FASE02 validada, preparar/executar FASE03 (parsing); depois FASE04 (normalização e reconstrução do CSV).
5. Manter o CSV ausente até a FASE04 canónica; comparar hash/contagem/esquema/datas com manifesto e sidecar, registando a diferença de versão do parser.
6. RAW imutável, sem deduplicação nem remoção de linhas. REC-001 B3 × BLOOMBERG_MAIL permanece independente e bloqueada até reconciliação própria.


---

## Secção 23 — FASE02 validada; FASE03 publicada — COTAHIST 2018 (2026-10-13)

### FASE02 — integridade da fonte: VALIDADO
- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE02_INTEGRIDADE_FONTE_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE02_INTEGRIDADE_FONTE_V1.json
- Estado/decisão: `VALIDADO` / `LIBERADO_PARA_FASE03`.
- SHA-256 RAW: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`, consistente com FASE01 e manifesto/sidecar.
- ZIP íntegro: um membro (`COTAHIST_A2018.TXT`), `zip_testzip_error=null`, zero registos com comprimento inválido.
- Total: 580.157 linhas físicas; 580.155 registos tipo `01`, um header `00` e um trailer `99`; cada registo tem 245 bytes.
- Timestamp da evidência: `2026-10-13T14:18:57.288252+00:00`.
- Âmbito limitado à integridade física/estrutura ZIP; ainda não certifica parsing nem NORMALIZED.

### FASE03 — workflow de parsing estrutural publicado; evidência pendente
- Workflow: `.github/workflows/cotahist-fase03-parsing-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase03-parsing-2018-v1.yml
- Commit de publicação: `348f223d54bfb46208647c6631b421f041bde030`.
- Adaptado do contrato de FASE03 2017, com referências de ano revistas e Git LFS ativado.
- Valida FASE02 e hash RAW, ZIP/membro, comprimento de 245 bytes, tipos de registo e datas das cotações 2018.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE03_PARSING_V1.json`; ainda não encontrada após publicação. Não considerar FASE03 concluída até validar o artefacto.

### Roadmap operacional imediato
1. FASE00: VALIDADO.
2. FASE01: VALIDADO; hashes RAW/manifesto/sidecar coincidentes.
3. FASE02: VALIDADO; 580.155 registos tipo 01, estrutura ZIP íntegra e comprimentos válidos.
4. FASE03: workflow publicado; aguarda execução/evidência `VALIDADO` / `LIBERADO_PARA_FASE04`, zero datas inválidas e zero datas fora de 2018.
5. FASE04: depois da FASE03, regenerar NORMALIZED com `scripts/ingestao/normalize_cotahist.py`; verificar 580.155 linhas, 25 campos, datas e hash contra manifesto/sidecar. Registar a diferença `parser_version=1.1.0` no manifesto versus script canónico `PARSER_VERSION=1.1.2`, sem alterar a evidência histórica silenciosamente.
6. Preservar RAW e linhas de origem; não deduplicar. REC-001 B3 × BLOOMBERG_MAIL continua independente e bloqueada até reconciliação própria.


---

## Secção 24 — FASE03 validada; FASE04 2018 publicada para normalização e reconciliação (2026-10-13)

### FASE03 — parsing estrutural: VALIDADO
- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE03_PARSING_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE03_PARSING_V1.json
- Blob SHA da evidência: `4f258d343ef3d62842a9c3f18ba49944109196aa`.
- Estado/decisão: `VALIDADO` / `LIBERADO_PARA_FASE04`.
- RAW SHA-256: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`, igual à FASE02.
- ZIP: membro único `COTAHIST_A2018.TXT`; 580.157 linhas físicas; 580.155 registos `01`, um `00` e um `99`.
- Comprimento inválido: 0; datas inválidas: 0; primeira data: 2018-01-02; última data: 2018-12-28.
- Timestamp da evidência: `2026-10-13T15:18:54.647413+00:00`.
- Limite: validação estrutural; não certifica a semântica nem a normalização.

### FASE04 — workflow publicado; execução/evidência ainda pendentes
- Workflow: `.github/workflows/cotahist-fase04-normalizacao-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase04-normalizacao-2018-v1.yml
- Commit de publicação: `cdcb13c0995a15e3f94a7c43063511175be70bcd`.
- O workflow é acionado por `workflow_dispatch` e por push nas dependências monitorizadas; valida FASE03, proveniência e SHA-256 do RAW, executa o script canónico e compara CSV, manifesto e sidecar.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE04_NORMALIZACAO_V1.json`.
- Critérios: 580.155 linhas, 25 campos, zero datas inválidas/fora de 2018, intervalo de datas reconciliado e hash do CSV coincidente com manifesto e sidecar. Se houver divergência, deve persistir evidência `BLOQUEADO` e não publicar CSV não validado.
- Diferença de versão registada para reconciliação: manifesto `parser_version=1.1.0`; script canónico `PARSER_VERSION=1.1.2`. Não atualizar manifesto/sidecar silenciosamente nem alterar o RAW.
- A criação/publicação do workflow não prova execução bem-sucedida; só promover para FASE05 após validar a evidência FASE04.

### Roadmap operacional imediato
1. FASE00–FASE03 2018: VALIDADO; FASE03 libera FASE04.
2. FASE04 2018: workflow publicado; aguarda evidência persistida e reconciliação do NORMALIZED.
3. Se FASE04 VALIDADO / `LIBERADO_PARA_FASE05`, avançar para FASE05; se BLOQUEADO, investigar os bloqueadores sem sobrescrever evidências históricas.
4. Preservar RAW imutável, sem deduplicação nem remoção de linhas. REC-001 B3 × BLOOMBERG_MAIL continua independente e bloqueada até reconciliação própria.


---

## Secção 25 — Verificação pós-publicação FASE04 (2026-10-13)

- Foi feita nova consulta ao branch `main` após a publicação do workflow FASE04.
- O workflow está presente em `.github/workflows/cotahist-fase04-normalizacao-2018-v1.yml`.
- Na consulta desta verificação, a evidência `dados/cotahist/quality/COTAHIST_2018_FASE04_NORMALIZACAO_V1.json` ainda não existia e o CSV `dados/cotahist/normalized/anual/COTAHIST_A2018.csv` também não estava publicado.
- Estado operacional: **FASE04 PENDENTE DE EVIDÊNCIA**. Não declarar a normalização executada ou aprovada apenas com base no workflow publicado.
- Ação necessária: abrir [GitHub Actions — COTAHIST 2018 FASE04](https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase04-normalizacao-2018-v1.yml), selecionar a branch `main` e executar `Run workflow` se não houver execução automática em curso. Depois verificar a evidência FASE04 e os respetivos hashes/contagens.
- Não executar FASE05 antes de a FASE04 produzir decisão `LIBERADO_PARA_FASE05` sem bloqueadores.


---

## Secção 26 — FASE04 validada; FASE05 publicada — COTAHIST 2018 (2026-10-13)

### FASE04 — normalização e reconciliação: VALIDADO
- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE04_NORMALIZACAO_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE04_NORMALIZACAO_V1.json
- Blob SHA da evidência: `ac768cf09da4f3b3e987f7250b9a3b177195eed6`.
- Estado/decisão: `VALIDADO` / `LIBERADO_PARA_FASE05`; bloqueadores: zero.
- NORMALIZED: 580.155 linhas, 25 campos, zero datas inválidas e zero datas fora de 2018; intervalo 2018-01-02 a 2018-12-28.
- SHA-256 calculado = manifesto = sidecar: `e3e57fdcf4be823830e6d6653d68275fa33af6d51b86392356cc29fe7a0f7981`.
- RAW SHA-256 preservado: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`.
- Script canónico executado sem erro, `PARSER_VERSION=1.1.2`; o manifesto histórico mantém `parser_version=1.1.0`. Diferença explícita na evidência; não houve alteração silenciosa do manifesto nem do sidecar.
- `raw_modified=false`; `deduplication_performed=false`.

### FASE05 — workflow manifesto/checksum publicado; execução pendente
- Workflow: `.github/workflows/cotahist-fase05-manifesto-checksum-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase05-manifesto-checksum-2018-v1.yml
- Commit de publicação: `402d08f594cb3439cf79e975fc69ba8a87d3ba0f`.
- Adaptado do contrato FASE05 de 2017 e endurecido para exigir FASE04 2018 VALIDADO, ausência de bloqueadores e coincidência dos hashes físicos com a evidência FASE04.
- Revalida o RAW físico, manifesto/sidecar RAW, CSV NORMALIZED, manifesto/sidecar NORMALIZED, estrutura ZIP, contagem, 25 campos e intervalo de datas.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE05_MANIFESTO_CHECKSUM_V1.json`.
- Estado: **WORKFLOW PUBLICADO; execução/evidência ainda por confirmar**. Não presumir que o push iniciou/terminou o workflow nem promover para FASE06 sem evidência.

### Roadmap operacional imediato
1. FASE00–FASE04 2018: VALIDADO; FASE04 liberou FASE05.
2. FASE05 2018: workflow publicado; executar/verificar a evidência de manifesto e checksum.
3. Só criar/acionar FASE06 depois de FASE05 `VALIDADO` / `LIBERADO_PARA_FASE06`; FASE06 reconcilia campos críticos RAW × NORMALIZED, sem deduplicação.
4. Manter RAW imutável e todas as linhas. REC-001 B3 × BLOOMBERG_MAIL permanece independente e bloqueada até reconciliação própria.


---

## Secção 27 — FASE05 validada; FASE06 publicada — COTAHIST 2018 (2026-10-13)

### FASE05 — manifesto e checksum: VALIDADO
- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE05_MANIFESTO_CHECKSUM_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE05_MANIFESTO_CHECKSUM_V1.json
- Blob SHA: `9a251e4f6e3304a6dea689f65bb0fdf3f8a7499d`.
- Estado/decisão: `VALIDADO` / `LIBERADO_PARA_FASE06`.
- RAW SHA-256 coincide entre cálculo físico, manifesto e sidecar: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`.
- NORMALIZED SHA-256 coincide entre cálculo físico, manifesto e sidecar: `e3e57fdcf4be823830e6d6653d68275fa33af6d51b86392356cc29fe7a0f7981`.
- ZIP íntegro, membro único `COTAHIST_A2018.TXT`; 580.155 linhas; 25 campos; datas 2018-01-02 a 2018-12-28.
- `raw_modified=false`; `deduplication_performed=false`.
- Timestamp da evidência: `2026-10-13T16:19:16.010825+00:00`.

### FASE06 — reconciliação semântica RAW × NORMALIZED: workflow publicado; execução pendente
- Workflow: `.github/workflows/cotahist-fase06-reconciliacao-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase06-reconciliacao-2018-v1.yml
- Commits: criação `0228cee170d85ae8c6b87fd1bbc844940cbf60c2`; endurecimento do gate `d897ef21b24904f560a00dc6fd60152552fd4c34`.
- O gate exige FASE05 2018 `VALIDADO` / `LIBERADO_PARA_FASE06` e confirma que os hashes RAW/NORMALIZED continuam iguais aos da evidência FASE05.
- Compara 12 campos críticos por ordem de registo, sem deduplicação: data, Cód. BDI, ticker, tipo de mercado, preços de abertura/máximo/mínimo/médio/último, número de negócios, quantidade e volume.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE06_RECONCILIACAO_V1.json`.
- Estado: **WORKFLOW PUBLICADO; evidência ainda não encontrada na consulta posterior à publicação**. Não declarar FASE06 concluída nem avançar para FASE07 sem evidência `VALIDADO` / `LIBERADO_PARA_FASE07`.
- O workflow persiste evidência diagnóstica inclusive quando encontra divergências; amostra de divergências limitada a 20 registos para diagnóstico.

### Roadmap operacional imediato
1. FASE00–FASE05 2018: VALIDADO; FASE05 libera FASE06.
2. FASE06 2018: executar/verificar a reconciliação semântica dos 12 campos críticos RAW × NORMALIZED.
3. Se FASE06 validar sem divergências, avançar para FASE07 identidade/cardinalidade; se bloquear, investigar sem corrigir ou deduplicar o RAW.
4. Preservar as evidências históricas e a trilha independente REC-001 B3 × BLOOMBERG_MAIL, que permanece bloqueada até reconciliação própria.
