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