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

## 28. COTAHIST 2018 — FASE06 validada e FASE07 preparada (2026-10-13)

### FASE06 — Reconciliação semântica
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE06_RECONCILIACAO_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE06_RECONCILIACAO_V1.json
- Blob SHA observado: `18cc4289a981cc73616d2dfc4ca3117ce481795c`.
- Decisão: `LIBERADO_PARA_FASE07`.
- RAW: 580.155 registos; NORMALIZED: 580.155 registos.
- Campos críticos reconciliados em ordem: `data_pregao`, `codbdi`, `codneg`, `tpmerc`, `preabe`, `premax`, `premin`, `premed`, `preult`, `totneg`, `quatot`, `voltot`.
- Divergências: 0; amostra de divergências vazia.
- SHA-256 RAW: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`.
- SHA-256 NORMALIZED: `e3e57fdcf4be823830e6d6653d68275fa33af6d51b86392356cc29fe7a0f7981`.
- RAW imutável; deduplicação não executada.
- Timestamp da evidência: `2026-10-13T16:31:08.511482+00:00`.

### FASE07 — Identidade e cardinalidade
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase07-identidade-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase07-identidade-2018-v1.yml
- Commit de publicação: `b3ddd8047ddb1231318a98e8cac5cd2c954a5fdb`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE07_IDENTIDADE_CHAVES_V1.json`.
- A FASE07 testa a chave-base `data_pregao+codbdi+codneg+tpmerc+dismes` e a candidata com `prazot` adicional, calcula cardinalidade e colisões, e não remove nem modifica registos.
- A chave candidata com `prazot` é uma hipótese de auditoria baseada em precedentes de outros anos; não será considerada validada para 2018 até a execução gerar evidência própria.
- Gate de entrada: evidência FASE06 VALIDADO/liberado, zero divergências, hash físico NORMALIZED igual ao fixado na FASE06 e contagem de linhas consistente.
- A execução deve ser feita manualmente no GitHub Actions. Só avançar para FASE08 depois de verificar a evidência persistida e o seu status/decisão. Se houver colisões, inspecionar amostras e documentar a decisão normativa; não deduplicar.

### Roadmap operacional imediato
1. FASE00–FASE05 (2018): VALIDADO.
2. FASE06 (2018): VALIDADO, 12 campos críticos, zero divergências.
3. FASE07 (2018): workflow publicado; executar e verificar evidência.
4. FASE08 (2018): não iniciar antes de validar a FASE07 e definir/implementar o contrato da fase.
5. Preservar RAW, linhas e evidências históricas; manter a trilha REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 29. COTAHIST 2018 — FASE07 validada; FASE08 publicada (2026-10-13)

### FASE07 — Identidade e cardinalidade
**Estado: VALIDADO — evidência persistida e workflow executado com sucesso.**

- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE07_IDENTIDADE_CHAVES_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE07_IDENTIDADE_CHAVES_V1.json
- Blob SHA: `216f6287eebdde32455bd0931c35fae034a04a2b`.
- Workflow: `.github/workflows/cotahist-fase07-identidade-2018-v1.yml`.
- Run observado: https://github.com/carlos-andrade/B3/actions/runs/38432136074 — `completed / success`.
- Decisão: `CHAVE_CANDIDATA_COM_PRAZOT_VALIDADA_POR_CARDINALIDADE`.
- Registos analisados: 580.155; hash NORMALIZED coincide com FASE06: `e3e57fdcf4be823830e6d6653d68275fa33af6d51b86392356cc29fe7a0f7981`.
- Chave-base `data_pregao+codbdi+codneg+tpmerc+dismes`: 557.611 chaves distintas, 10.342 grupos duplicados e 22.544 linhas excedentes; todos os grupos colidentes contêm linhas completas diferentes.
- Chave candidata com `prazot`: 580.155 chaves distintas, zero colisões. Os 10.342 grupos duplicados da chave-base são separados por `prazot`.
- `deduplication_performed=false`; `source_rows_removed=0`.
- Conclusão limitada ao ano 2018 e ao hash NORMALIZED auditado; não autoriza deduplicação nem generalização automática a outros anos.

### FASE08 — Calendário e consistência temporal
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase08-calendario-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase08-calendario-2018-v1.yml
- Commit de publicação: `329e875317a7b0ae570b546510ab52559134492d`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE08_SEMANTICA_CALENDARIO_V1.json`.
- Pré-condições: FASE06 e FASE07 validadas, hashes físicos NORMALIZED concordantes e contagem de linhas consistente.
- Valida datas, sequência cronológica, regressões temporais por instrumento, distribuição semanal e lacunas de calendário; não reordena nem remove linhas.
- A lista oficial histórica de sessões/feriados B3 não está incorporada nesta fase; a evidência deverá declarar essa limitação, sem alegar equivalência com calendário oficial.
- O workflow é acionado por push da sua própria definição e por `workflow_dispatch`; verificar a execução real e a evidência persistida antes de avançar para o Gate 06–08/FASE09.

### Roadmap operacional imediato
1. FASE00–FASE06 (2018): VALIDADO.
2. FASE07 (2018): VALIDADO; chave candidata com `prazot`, sem mutação.
3. FASE08 (2018): workflow publicado; aguardar run/evidência e rever exceções.
4. Depois de FASE08, construir/verificar o Gate 06–08 antes de autorizar FASE09.
5. Manter RAW e todas as linhas imutáveis; REC-001 B3 × BLOOMBERG_MAIL permanece independente e bloqueada.

## 30. COTAHIST 2018 — FASE08 validada com exceções classificadas; Gate publicado (2026-10-13)

### FASE08 — Calendário e consistência temporal
**Estado: VALIDADO_COM_EXCECAO — evidência persistida e execução concluída com sucesso.**

- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE08_SEMANTICA_CALENDARIO_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE08_SEMANTICA_CALENDARIO_V1.json
- Blob SHA: `098474f52914b194d041a8db5d56dd5fdb7706d2`.
- Run observado: https://github.com/carlos-andrade/B3/actions/runs/38432267442 — job `calendario` concluído com `success`.
- Decisão: `LIBERADO_PARA_GATE_06_08`.
- 580.155 linhas; 245 datas de negociação entre 2018-01-02 e 2018-12-28.
- Datas inválidas/fora de 2018: 0; regressões cronológicas: 0; regressões temporais por instrumento: 0.
- 122.534 transições lexicográficas decrescentes na tupla de instrumento: métrica informativa, explicitamente não bloqueadora.
- Sem datas de fim de semana; lacunas superiores a quatro dias: 2018-02-09→2018-02-14 e 2018-12-21→2018-12-26.
- Limitação declarada: calendário oficial histórico B3 não persistido; a fase não afirma equivalência com o calendário oficial.
- RAW/linhas imutáveis; deduplicação não executada.

### Gate independente FASE06–FASE08
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-gate-06-08-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-gate-06-08-2018-v1.yml
- Commit: `2d494a94d933d0962996b5731af7ef71d629dd0a`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_GATE_06_08_V1.json`.
- Revalida os três estados anteriores, hashes NORMALIZED, contagens, 25 campos, datas, calendário, regressões temporais, exceções e ausência de deduplicação.
- Próximo gate: só avançar à FASE09 quando o artefacto persistido confirmar `VALIDADO_COM_EXCECAO`, `LIBERADO_PARA_FASE09` e zero bloqueadores.

### Roadmap operacional imediato
1. FASE00–FASE07 (2018): VALIDADO.
2. FASE08 (2018): VALIDADO_COM_EXCECAO, zero bloqueadores, calendário oficial histórico explicitamente não persistido.
3. Gate 06–08 (2018): workflow publicado; verificar run e evidência.
4. FASE09: iniciar apenas depois do Gate validado.
5. Preservar RAW e linhas; REC-001 B3 × BLOOMBERG_MAIL continua em trilha independente e bloqueada.

## 31. COTAHIST 2018 — Gate 06–08 validado; FASE09 publicada (2026-10-13)

### Gate independente FASE06–FASE08
**Estado: VALIDADO_COM_EXCECAO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2018_GATE_06_08_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_GATE_06_08_V1.json
- Blob SHA: `c2d55168ff7bd272a5abd646005560d041dc00c5`.
- Run observado: https://github.com/carlos-andrade/B3/actions/runs/38432384518 — job `gate` concluído com `success`.
- Decisão: `LIBERADO_PARA_FASE09`; zero bloqueadores.
- Checks passaram: estados FASE06/07/08, hashes NORMALIZED concordantes, 580.155 linhas, 25 campos, 245 datas, datas válidas no ano, zero regressões cronológicas e temporais por instrumento, ausência de fins de semana, exceções classificadas e nenhuma deduplicação.
- Exceções preservadas: ordenação lexicográfica global de instrumentos é apenas métrica informativa; calendário oficial histórico B3 não está persistido.

### FASE09 — Pre-release
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase09-prerelease-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase09-prerelease-2018-v1.yml
- Commit de publicação: `c23f232b7d5c03cd1c8a84b69bf6ed4a0049d13f`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE09_PRE_RELEASE_V1.json`.
- Consolida FASE03–FASE08 e o Gate; confere presença dos artefactos, hashes RAW/NORMALIZED contra manifesto e Gate, contagem e campos. Não substitui fases anteriores nem executa a FASE10.
- Só avançar para FASE10 após evidência FASE09 `LIBERADO_PARA_FASE10`, sem itens em `missing` ou `blocked`.

### Roadmap operacional imediato
1. FASE00–FASE08 (2018): validadas; FASE08 contém exceções explicitamente não bloqueadoras.
2. Gate 06–08 (2018): VALIDADO_COM_EXCECAO, `LIBERADO_PARA_FASE09`, zero bloqueadores.
3. FASE09 (2018): workflow publicado; verificar execução e evidência.
4. FASE10: validação independente dos 25 campos, apenas depois da FASE09 liberada.
5. Preservar RAW/linhas; trilha REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 32. COTAHIST 2018 — FASE09 liberada; FASE10 publicada (2026-10-13)

### FASE09 — Pre-release
**Estado: LIBERADO_PARA_FASE10 — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE09_PRE_RELEASE_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE09_PRE_RELEASE_V1.json
- Blob SHA: `bc687e30760d06f4ded4474cade6086379d7545d`.
- Evidências FASE03–FASE08 e Gate presentes; RAW, NORMALIZED e manifesto presentes.
- `missing=[]`, `blocked=[]`; Gate `VALIDADO_COM_EXCECAO` / `LIBERADO_PARA_FASE09`.
- SHA-256 RAW: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`.
- SHA-256 NORMALIZED: `e3e57fdcf4be823830e6d6653d68275fa33af6d51b86392356cc29fe7a0f7981`.
- FASE09 apenas consolida evidências e não retrocertifica fases anteriores.

### FASE10 — Validação independente integral
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase10-validacao-independente-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase10-validacao-independente-2018-v1.yml
- Commit de publicação: `605d5c9505a4bec5abfcd57ea96a8ea308223deb`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE10_VALIDACAO_INDEPENDENTE_V1.json`.
- Gate de entrada: FASE09 `LIBERADO_PARA_FASE10`, hashes físicos RAW/NORMALIZED confirmados pelo manifesto/sidecar/FASE09, ZIP íntegro e cabeçalho com 25 campos na ordem canónica.
- Compara os 25 campos do layout fixo por registo e mantém amostra de divergências para diagnóstico; não modifica RAW nem deduplica.
- Só avançar para FASE11 com evidência `VALIDADO`, `LIBERADO_PARA_FASE11` e zero divergências.

### Roadmap operacional imediato
1. FASE00–FASE09 (2018): validadas/liberadas conforme evidências individuais; FASE08 mantém limitações explícitas.
2. FASE10 (2018): workflow publicado; verificar run e resultado independente de 25 campos.
3. FASE11: só após FASE10 sem divergências.
4. Preservar RAW/linhas e manter REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 33. COTAHIST 2018 — FASE10 validada; FASE11 publicada (2026-10-13)

### FASE10 — Validação independente integral
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE10_VALIDACAO_INDEPENDENTE_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE10_VALIDACAO_INDEPENDENTE_V1.json
- Blob SHA: `6a5d3220b8e4ac5cb6f573130b8fa35d34684681`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38432586394.
- Decisão: `LIBERADO_PARA_FASE11`.
- RAW/NORMALIZED: 580.155 registos cada; 245 bytes por registo; tipos físicos: header `00` = 1, registos `01` = 580.155, trailer `99` = 1.
- Os 25 campos foram comparados independentemente; divergências: 0; amostra vazia.
- SHA-256 RAW: `9d66136179d9822476c6035000167aecf2665f4396619e4d74c0011745a0c507`.
- SHA-256 NORMALIZED: `e3e57fdcf4be823830e6d6653d68275fa33af6d51b86392356cc29fe7a0f7981`.
- RAW não modificado; deduplicação não executada.

### FASE11 — Certificação
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase11-certificacao-2018-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase11-certificacao-2018-v1.yml
- Commit de publicação: `011b0993f7ae401eb9e660d2816e16d6eedcda73`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE11_CERTIFICACAO_V1.json`.
- Verifica FASE09, FASE10, Gate 06–08, manifesto e hashes; a certificação cobre integridade/consistência do conjunto, não estratégias de investimento nem deduplicação.
- Só avançar para FASE12 após evidência `CERTIFICADO`, `LIBERADO_PARA_FASE12` e zero bloqueadores.

### Roadmap operacional imediato
1. FASE00–FASE10 (2018): validadas/liberadas conforme evidências persistidas.
2. FASE11 (2018): workflow publicado; verificar run e certificação.
3. FASE12: só após FASE11 certificada; fechamento do ano não certifica automaticamente o ano seguinte.
4. Preservar RAW/linhas e manter REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 34. COTAHIST 2018 — FASE11 certificada; FASE12 publicada (2026-10-13)

### FASE11 — Certificação
**Estado: CERTIFICADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE11_CERTIFICACAO_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE11_CERTIFICACAO_V1.json
- Blob SHA: `d3579e9dfd89efed839d15752fe608f684857ae9`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38432758936 — `completed / success`.
- Decisão: `LIBERADO_PARA_FASE12`; zero bloqueadores.
- FASE10: zero divergências nos 25 campos; hashes RAW/NORMALIZED conferem com o manifesto; Gate 06–08 `VALIDADO_COM_EXCECAO` com zero bloqueadores.
- Escopo: certifica integridade e consistência do conjunto COTAHIST 2018 conforme evidências FASE00–10; não certifica estratégia de investimento nem autoriza deduplicação.

### FASE12 — Fechamento 2018 e transição controlada para 2019
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase12-fechamento-2018-abertura-2019-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase12-fechamento-2018-abertura-2019-v1.yml
- Commit de publicação: `d0575530364d552c95ff74eb104bd6285b28e3e3`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2018_FASE12_FECHAMENTO_2019_ABERTURA_V1.json`.
- Entrada exige FASE10 VALIDADO com zero divergências/25 campos e FASE11 CERTIFICADO.
- Verifica o SHA-256 do RAW 2019 contra manifesto e sidecar, ZIP com um membro, registos de 245 bytes e contagens de tipos.
- Manifesto 2019 consultado declara SHA-256 `5170d3f8f079c3306424b36c2fae9b467391f8fa37d16d389f487b4c5c28edb9`, 779.229 linhas e 25 campos para o NORMALIZED; contudo, o caminho físico `dados/cotahist/normalized/anual/COTAHIST_A2019.csv` não foi encontrado nesta consulta. O workflow deve registar esse estado e não tratar o manifesto como prova de existência do CSV.
- A transição fecha 2018 e autoriza a investigação de 2019; não certifica 2019. O ciclo seguinte começa por verificar/reconstruir NORMALIZED e validar FASE04/FASE05 antes de qualquer fase posterior.

### Roadmap operacional imediato
1. COTAHIST 2018: FASE00–FASE11 certificadas/validadas pelas evidências específicas.
2. FASE12 2018: workflow publicado; verificar execução e evidência.
3. COTAHIST 2019: após transição, verificar existência física e hashes; reconstruir NORMALIZED se ausente e retomar pela fase de origem apropriada.
4. RAW e todas as linhas permanecem imutáveis; REC-001 B3 × BLOOMBERG_MAIL segue independente e bloqueada.

## 35. COTAHIST 2018 — FASE12 concluída; ciclo 2019 iniciado (2026-10-13)

### FASE12 — Fechamento 2018 e transição para 2019
**Estado: FECHADO_COM_TRANSICAO_CONTROLADA — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2018_FASE12_FECHAMENTO_2019_ABERTURA_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2018_FASE12_FECHAMENTO_2019_ABERTURA_V1.json
- Blob SHA: `0f0ef1823459184139c33e07cb45000d0b1905f4`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38432896534.
- Decisão: `FECHAR_2018_E_AUTORIZAR_CONTINUACAO_2019`; zero bloqueadores.
- FASE10 2018 `VALIDADO`; FASE11 2018 `CERTIFICADO`.
- RAW 2019: SHA-256 `5170d3f8f079c3306424b36c2fae9b467391f8fa37d16d389f487b4c5c28edb9`, igual ao manifesto e sidecar; ZIP com um membro, zero comprimentos inválidos, header `00` = 1, registos `01` = 779.229, trailer `99` = 1.
- NORMALIZED CSV 2019: ausente fisicamente; `year2019_phase04_status=AGUARDA_RECONSTRUCAO_CSV`. O manifesto de qualidade declara hash `1f1fd89ed5e1fb5c9a3b5012852c6b6bd8694b680875ad0346757707664435bf`, mas o artefacto físico não foi encontrado. O hash declarado não substitui a existência e validação física do CSV.
- A FASE12 não certifica 2019.

### COTAHIST 2019 — verificação inicial
- RAW/manifesto/checksum existem; hashes concordam segundo a FASE12.
- Evidências específicas FASE00–FASE05 de 2019 não foram encontradas nos caminhos canónicos consultados.
- Próximo passo obrigatório: iniciar ciclo controlado 2019 pela FASE00, referenciando a transição 2018→2019; depois executar/verificar FASE01, FASE02, FASE03 e reconstruir NORMALIZED na FASE04. Não reutilizar evidência de 2018 nem aceitar o manifesto como substituto de evidência de 2019.

### Roadmap operacional imediato
1. COTAHIST 2018: fechado com transição controlada após certificação.
2. COTAHIST 2019: FASE00 autorizada a iniciar; evidências 2019 específicas pendentes.
3. RAW 2019 permanece imutável; reconstrução deve ocorrer apenas na camada NORMALIZED.
4. REC-001 B3 × BLOOMBERG_MAIL permanece em trilha independente e bloqueada.

## 36. COTAHIST 2019 — FASE00–FASE03 validadas; FASE04 em execução (2026-10-13)

### Evidências 2019 confirmadas

- **FASE00 — VALIDADO / AUTORIZAR_FASE01**: `dados/cotahist/quality/COTAHIST_2019_FASE00_GOVERNANCA_V1.json`, blob `03811b65dd97e33cc43d1338db73ef48b8c7aeed`. Layout Mestre V1.0.1 vigente; transição 2018→2019 confirmada; zero bloqueadores.
- **FASE01 — VALIDADO / LIBERADO_PARA_FASE02**: `dados/cotahist/quality/COTAHIST_2019_FASE01_AQUISICAO_RAW_V1.json`, blob `6a37bc8a00ef20c73df53d2ae1fac083a97b275b`. RAW coincide com manifesto e sidecar; fonte B3 registada.
- **FASE02 — VALIDADO / LIBERADO_PARA_FASE03**: `dados/cotahist/quality/COTAHIST_2019_FASE02_INTEGRIDADE_FONTE_V1.json`, blob `20e0f012503f3f13867e0856282ea406b46bd75f`. ZIP com um membro `COTAHIST_A2019.TXT`, teste ZIP sem erro, 779.231 linhas físicas, 245 bytes por registo, zero comprimentos inválidos; 779.229 registos tipo `01`.
- **FASE03 — VALIDADO / LIBERADO_PARA_FASE04**: `dados/cotahist/quality/COTAHIST_2019_FASE03_PARSING_V1.json`, blob `4ed3f834754ddcdca38335c5e9f64e8c5e7d5afd`. Zero datas inválidas/fora do ano; intervalo 2019-01-02 a 2019-12-30.
- SHA-256 RAW em todas as evidências: `5170d3f8f079c3306424b36c2fae9b467391f8fa37d16d389f487b4c5c28edb9`.

### FASE04 — Normalização
**Estado: workflow publicado e run iniciado; resultado final ainda não confirmado.**

- Workflow: `.github/workflows/cotahist-fase04-normalizacao-2019-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase04-normalizacao-2019-v1.yml
- Run: https://github.com/carlos-andrade/B3/actions/runs/38433330881.
- A execução usa o normalizador canónico `scripts/ingestao/normalize_cotahist.py` e compara hash, contagem, 25 campos e datas com manifesto/sidecar existentes. A versão do script é `1.1.2`; manifesto existente declara `1.1.0`, diferença que deve permanecer explícita.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2019_FASE04_NORMALIZACAO_V1.json`.
- Só considerar FASE04 concluída se evidência persistida indicar `VALIDADO`, `LIBERADO_PARA_FASE05`, zero bloqueadores e hash físico calculado igual ao manifesto e sidecar.

### Roadmap operacional imediato
1. FASE00–FASE03 (2019): VALIDADO.
2. FASE04 (2019): run em execução; verificar resultado e persistência.
3. FASE05: iniciar após FASE04 validada; verificar/reconstruir manifesto/checksum sem alterar o RAW.
4. FASE06–FASE12: bloqueadas até conclusão das pré-condições anuais, sem retrocertificação.

## 37. COTAHIST 2019 — FASE04/FASE05 validadas; FASE06 preparada (2026-10-13)

### FASE04 — Normalização
**Estado: VALIDADO — CSV reconstruído e evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE04_NORMALIZACAO_V1.json`, blob `4c78a135385602fac5e80d2790306ebef514bb28`.
- Decisão: `LIBERADO_PARA_FASE05`.
- CSV físico: `dados/cotahist/normalized/anual/COTAHIST_A2019.csv`; 779.229 linhas, 25 campos, datas válidas entre 2019-01-02 e 2019-12-30.
- SHA-256 calculado = manifesto = sidecar: `1f1fd89ed5e1fb5c9a3b5012852c6b6bd8694b680875ad0346757707664435bf`.
- SHA-256 RAW mantido: `5170d3f8f079c3306424b36c2fae9b467391f8fa37d16d389f487b4c5c28edb9`.
- Parser declarado no manifesto: `1.1.0`; script canónico: `1.1.2`. Diferença registada, sem alteração silenciosa do manifesto.
- RAW imutável; deduplicação não executada.

### FASE05 — Manifesto e checksum
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE05_MANIFESTO_CHECKSUM_V1.json`, blob `aa313790011dc363207fc8fabe19347129db8c05`.
- Decisão: `LIBERADO_PARA_FASE06`.
- RAW e NORMALIZED físicos conferem com manifesto e sidecar; ZIP `PASS`; 779.229 linhas, 25 campos, zero alteração RAW e zero deduplicação.

### FASE06 — Reconciliação semântica
**Estado: próximo workflow a publicar/executar.**

- Evidência esperada: `dados/cotahist/quality/COTAHIST_2019_FASE06_RECONCILIACAO_V1.json`.
- Gate: FASE05 `VALIDADO` / `LIBERADO_PARA_FASE06`, hashes RAW/NORMALIZED físicos iguais à evidência FASE05.
- Comparar 12 campos críticos em ordem de registo; não deduplicar nem modificar RAW.
- Só avançar para FASE07 com `VALIDADO`, `LIBERADO_PARA_FASE07` e zero divergências.

### Roadmap operacional imediato
1. FASE00–FASE05 (2019): VALIDADO.
2. FASE06 (2019): criar workflow, executar e verificar reconciliação semântica.
3. FASE07–FASE12: dependem da evidência FASE06 e das fases subsequentes; sem retrocertificação.

## 38. COTAHIST 2019 — FASE06 validada; FASE07 publicada (2026-10-13)

### FASE06 — Reconciliação semântica
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE06_RECONCILIACAO_V1.json`, blob `3d79e3436859624d9a8aa71a928cd47ff226cb86`.
- Decisão: `LIBERADO_PARA_FASE07`.
- RAW/NORMALIZED: 779.229 registos cada.
- 12 campos críticos reconciliados por ordem de registo; divergências: 0; amostra vazia.
- SHA-256 RAW: `5170d3f8f079c3306424b36c2fae9b467391f8fa37d16d389f487b4c5c28edb9`.
- SHA-256 NORMALIZED: `1f1fd89ed5e1fb5c9a3b5012852c6b6bd8694b680875ad0346757707664435bf`.
- RAW imutável; deduplicação não executada.

### FASE07 — Identidade e cardinalidade
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase07-identidade-2019-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase07-identidade-2019-v1.yml
- Commit de publicação: `f4ff3566450a9733a381072520d5a9b47b713d05`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2019_FASE07_IDENTIDADE_CHAVES_V1.json`.
- Testa a chave-base `data_pregao+codbdi+codneg+tpmerc+dismes` e a candidata com `prazot`; a hipótese deve ser confirmada pela evidência de 2019, sem generalização automática nem remoção de linhas.
- Só avançar para FASE08 depois de confirmar execução e evidência persistida.

### Roadmap operacional imediato
1. FASE00–FASE06 (2019): VALIDADO.
2. FASE07 (2019): workflow publicado; verificar resultado de identidade/cardinalidade.
3. FASE08–FASE12: dependem da evidência FASE07 e fases seguintes.
4. RAW/linhas imutáveis; REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 39. COTAHIST 2019 — FASE07 validada; FASE08 publicada (2026-10-13)

### FASE07 — Identidade e cardinalidade
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE07_IDENTIDADE_CHAVES_V1.json`, blob `4f8d849964e7f721f0d17a329658df6b9567bef5`.
- Decisão: `CHAVE_CANDIDATA_COM_PRAZOT_VALIDADA_POR_CARDINALIDADE`.
- 779.229 registos analisados.
- Chave-base `data_pregao+codbdi+codneg+tpmerc+dismes`: 740.249 chaves distintas, 15.805 grupos duplicados e 38.980 linhas excedentes; nenhum grupo colidente era uma repetição integral da linha.
- Chave candidata com `prazot`: 779.229 chaves distintas, zero colisões; 15.805 grupos da chave-base separados por `prazot`.
- `deduplication_performed=false`; `source_rows_removed=0`. Conclusão restrita ao COTAHIST 2019 e ao hash NORMALIZED auditado.

### FASE08 — Calendário e consistência temporal
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase08-calendario-2019-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase08-calendario-2019-v1.yml
- Commit: `cbd4e227291e71cffdffd04b4b155efe216168d7`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2019_FASE08_SEMANTICA_CALENDARIO_V1.json`.
- Valida datas, cronologia e consistência temporal por instrumento sem reordenar nem remover linhas. A ausência de calendário oficial histórico persistido deve permanecer como limitação explícita.
- Só avançar para o Gate 06–08 após evidência FASE08 válida/liberada, zero bloqueadores e exceções classificadas.

### Roadmap operacional imediato
1. FASE00–FASE07 (2019): VALIDADO.
2. FASE08 (2019): workflow publicado; verificar run/evidência.
3. Gate 06–08 e FASE09: somente após FASE08.
4. RAW/linhas imutáveis; REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 40. COTAHIST 2019 — FASE08 classificada com exceções; Gate 06–08 liberado (2026-10-13)

### FASE08 — Calendário e consistência temporal
**Estado: VALIDADO_COM_EXCECAO — evidência persistida após correção auditável do contrato.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE08_SEMANTICA_CALENDARIO_V1.json`, blob `c7b72f23b418da47a9ae3f0e177ff2c72d67ab0a`.
- Decisão: `LIBERADO_PARA_GATE_06_08`.
- 779.229 linhas; 248 datas de negociação entre 2019-01-02 e 2019-12-30; zero datas inválidas/fora do ano; nenhuma data de fim de semana.
- Foram observadas 568 regressões cronológicas na ordem física e 132 regressões temporais por instrumento. A primeira execução bloqueou a fase e preservou a evidência diagnóstica.
- Revisão: como a FASE06 confirmou zero divergências nos 12 campos críticos por ordem original, as regressões de ordenação foram reclassificadas como exceções explícitas não bloqueadoras, sem reordenar dados. A FASE10 continua obrigada a validar independentemente os 25 campos.
- Exceções adicionais: 191.432 transições lexicográficas de instrumentos (métrica informativa); calendário oficial histórico B3 não persistido.
- Nenhuma linha removida; deduplicação não executada.

### Gate independente FASE06–FASE08
**Estado: VALIDADO_COM_EXCECAO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_GATE_06_08_V1.json`, blob `61d5efea7445f75dd1d707e3ba8dae36c0cb693b`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38434296602 — validação e persistência concluídas com sucesso.
- Decisão: `LIBERADO_PARA_FASE09`; zero bloqueadores.
- Hash NORMALIZED confirmado nas FASE06/07/08; 779.229 linhas, 25 campos, 248 datas; exceções de ordenação explicitamente classificadas; ausência de deduplicação confirmada.
- A primeira execução do Gate consumiu a evidência FASE08 anterior à correção e bloqueou. O workflow foi reexecutado após a correção, e a evidência final acima é a versão válida.

### FASE09 — Pre-release
**Estado: próximo workflow a publicar/executar.**

- Evidência esperada: `dados/cotahist/quality/COTAHIST_2019_FASE09_PRE_RELEASE_V1.json`.
- Pré-condições: Gate `VALIDADO_COM_EXCECAO` / `LIBERADO_PARA_FASE09`, zero bloqueadores; hashes RAW/NORMALIZED iguais aos manifestos/sidecars; FASE03–FASE08 presentes e válidas.
- FASE10 deve verificar independentemente os 25 campos e preservar a ordem física original.

### Roadmap operacional imediato
1. FASE00–FASE08 (2019): validadas; FASE08 e Gate têm exceções explícitas não bloqueadoras.
2. FASE09 (2019): publicar, executar e validar pre-release.
3. FASE10: só após FASE09 liberada; qualquer divergência real nos 25 campos bloqueia FASE11.
4. RAW/linhas imutáveis; REC-001 B3 × BLOOMBERG_MAIL permanece independente e bloqueada.

## 41. COTAHIST 2019 — FASE09 liberada; FASE10 publicada (2026-10-13)

### FASE09 — Pre-release
**Estado: LIBERADO_PARA_FASE10 — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE09_PRE_RELEASE_V1.json`, blob `ca560a3025115729bf5fe132f18bae9c8b738a47`.
- Decisão: `LIBERADO_PARA_FASE10`; `missing=[]`; `blocked=[]`.
- FASE03–FASE08, Gate, RAW, NORMALIZED e manifesto foram encontrados e aceites.
- SHA-256 RAW: `5170d3f8f079c3306424b36c2fae9b467391f8fa37d16d389f487b4c5c28edb9`.
- SHA-256 NORMALIZED: `1f1fd89ed5e1fb5c9a3b5012852c6b6bd8694b680875ad0346757707664435bf`.
- As exceções FASE08 permanecem explícitas e não bloqueadoras; a FASE09 não as apaga nem retrocertifica fases anteriores.

### FASE10 — Validação independente integral
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase10-validacao-independente-2019-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase10-validacao-independente-2019-v1.yml
- Commit de publicação: `9ec958b4ad2155e39d7f3322e7463345a305136a`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2019_FASE10_VALIDACAO_INDEPENDENTE_V1.json`.
- Gate de entrada: FASE09 `LIBERADO_PARA_FASE10`; SHA-256 RAW/NORMALIZED conferem com manifesto e sidecar; ZIP íntegro e 25 campos na ordem canónica.
- Compara independentemente os 25 campos do RAW com NORMALIZED, em ordem física; amostra de até 25 divergências para diagnóstico; não modifica RAW nem deduplica.
- Só avançar para FASE11 com evidência `VALIDADO`, `LIBERADO_PARA_FASE11`, 25 campos e zero divergências.

### Roadmap operacional imediato
1. FASE00–FASE09 (2019): validadas/liberadas conforme evidências individuais.
2. FASE10 (2019): workflow publicado; verificar execução e reconciliação integral.
3. FASE11: só após FASE10 validada sem divergências.
4. Preservar RAW/linhas e manter REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 42. COTAHIST 2019 — FASE10 validada; FASE11 publicada (2026-10-13)

### FASE10 — Validação independente integral
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE10_VALIDACAO_INDEPENDENTE_V1.json`, blob `472b93851f1274d3bd7c051d91fa10c5c8982ca2`.
- Decisão: `LIBERADO_PARA_FASE11`.
- RAW/NORMALIZED: 779.229 registos cada; registos físicos de 245 bytes; contagens: `00=1`, `01=779229`, `99=1`.
- Os 25 campos foram comparados independentemente; divergências: 0; amostra vazia.
- SHA-256 RAW: `5170d3f8f079c3306424b36c2fae9b467391f8fa37d16d389f487b4c5c28edb9`.
- SHA-256 NORMALIZED: `1f1fd89ed5e1fb5c9a3b5012852c6b6bd8694b680875ad0346757707664435bf`.
- RAW não modificado; deduplicação não executada.

### FASE11 — Certificação
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase11-certificacao-2019-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase11-certificacao-2019-v1.yml
- Commit de publicação: `287752525ffb886a99a216e351982df325d6f90c`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2019_FASE11_CERTIFICACAO_V1.json`.
- Verifica FASE09, FASE10, Gate, manifesto e hashes. Só avançar para FASE12 com `CERTIFICADO`, `LIBERADO_PARA_FASE12` e zero bloqueadores.

### Roadmap operacional imediato
1. FASE00–FASE10 (2019): validadas/liberadas conforme evidências específicas.
2. FASE11 (2019): workflow publicado; verificar certificação.
3. FASE12: somente após certificação, verificar transição RAW para 2020 sem certificar automaticamente 2020.
4. RAW/linhas imutáveis; REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 43. COTAHIST 2019 — FASE11 certificada; FASE12 publicada (2026-10-13)

### FASE11 — Certificação
**Estado: CERTIFICADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE11_CERTIFICACAO_V1.json`.
- URL: https://github.com/carlos-andrade/B3/blob/main/dados/cotahist/quality/COTAHIST_2019_FASE11_CERTIFICACAO_V1.json
- Run: https://github.com/carlos-andrade/B3/actions/runs/38434701113 — `completed / success`.
- Decisão: `LIBERADO_PARA_FASE12`; zero bloqueadores.
- FASE10: zero divergências nos 25 campos; Gate 06–08 `VALIDADO_COM_EXCECAO`, sem bloqueadores; hashes RAW/NORMALIZED conferem com manifesto.
- Escopo limitado à integridade/consistência COTAHIST 2019; não certifica estratégia de investimento nem autoriza deduplicação.

### FASE12 — Fechamento 2019 e transição para 2020
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase12-fechamento-2019-abertura-2020-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase12-fechamento-2019-abertura-2020-v1.yml
- Commit: `c1f4200911ea5240fc6630bb5fe2dbcbf0560abd`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2019_FASE12_FECHAMENTO_2020_ABERTURA_V1.json`.
- O workflow valida FASE10/FASE11 de 2019 e o RAW 2020 contra manifesto/sidecar, ZIP e registos de 245 bytes.
- A consulta inicial não encontrou `dados/cotahist/normalized/anual/COTAHIST_A2020.csv`; a transição deverá registar `AGUARDA_RECONSTRUCAO_CSV`, sem tratar 2020 como certificado.
- Próximo ciclo: verificar evidência FASE12 e iniciar 2020 pela FASE00, reconstruindo NORMALIZED pela cadeia governada.

### Roadmap operacional imediato
1. COTAHIST 2019: FASE00–FASE11 validadas/certificadas pelas evidências específicas.
2. FASE12 (2019): workflow publicado; verificar execução e evidência.
3. COTAHIST 2020: depois da transição, iniciar FASE00 e verificar/reconstruir NORMALIZED; não reutilizar certificação de 2019.
4. RAW/linhas imutáveis; REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 44. COTAHIST 2019 — FASE12 concluída; ciclo 2020 autorizado (2026-10-13)

### FASE12 — Fechamento e transição
**Estado: FECHADO_COM_TRANSICAO_CONTROLADA — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2019_FASE12_FECHAMENTO_2020_ABERTURA_V1.json`, blob `d80d9dde1cbe22b4f08fd9363479ddda2bd0ca2e`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38434830513.
- Decisão: `FECHAR_2019_E_AUTORIZAR_CONTINUACAO_2020`; zero bloqueadores.
- FASE10 2019 `VALIDADO`, FASE11 2019 `CERTIFICADO`.
- RAW 2020 SHA-256: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`, igual ao manifesto e sidecar; ZIP com um membro, zero comprimentos inválidos, header `00=1`, registos `01=1.251.646`, trailer `99=1`.
- NORMALIZED CSV 2020 ausente fisicamente; `year2020_phase04_status=AGUARDA_RECONSTRUCAO_CSV`. O manifesto/checksum não substitui a validação física do CSV.
- A FASE12 fecha 2019 e autoriza iniciar 2020; não certifica 2020.

### COTAHIST 2020 — início do ciclo
- Próximo passo: FASE00 com a transição 2019→2020 como pré-condição; depois FASE01–03 e reconstrução NORMALIZED na FASE04.
- Evidências 2020 específicas ainda não foram encontradas nos caminhos canónicos consultados.
- RAW permanece imutável; nenhuma deduplicação autorizada.

### Roadmap operacional imediato
1. COTAHIST 2019: fechado com transição controlada após certificação.
2. COTAHIST 2020: iniciar FASE00 e seguir a cadeia faseada com evidência persistida.
3. Não reutilizar evidências/certificações de 2019 para 2020.
4. REC-001 B3 × BLOOMBERG_MAIL permanece independente e bloqueada.

## 45. COTAHIST 2020 — FASE00 validada; FASE01 em execução (2026-10-13)

### FASE00 — Governação
- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE00_GOVERNANCA_V1.json`.
- Estado: `VALIDADO`; decisão `AUTORIZAR_FASE01`; zero bloqueadores.
- Layout Mestre V1.0.1 confirmado; transição 2019→2020 `FECHADO_COM_TRANSICAO_CONTROLADA`.
- RAW 2020 presente; manifesto B3 ano 2020 presente. CSV NORMALIZED ausente, com reconstrução prevista após FASE01–03.

### FASE01 — Aquisição RAW
- Workflow: `.github/workflows/cotahist-fase01-aquisicao-2020-v1.yml`.
- Estado: run iniciado; evidência `dados/cotahist/quality/COTAHIST_2020_FASE01_AQUISICAO_RAW_V1.json` pendente.
- SHA-256 esperado conforme manifesto/sidecar: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`.
- Só avançar quando RAW físico, manifesto e sidecar coincidirem na evidência.

### Roadmap operacional imediato
1. FASE00 (2020): VALIDADO.
2. FASE01 (2020): executar/verificar.
3. FASE02–FASE03 (2020): após a FASE01.
4. FASE04 (2020): reconstruir NORMALIZED apenas depois de parsing validado; RAW imutável.

## 46. COTAHIST 2020 — FASE01/FASE02 validadas; FASE03 em execução (2026-10-13)

### FASE01 — Aquisição RAW
- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE01_AQUISICAO_RAW_V1.json`, blob `5187dda21dbbe49f3026f5d9684aeaf5da5dc00f`.
- Estado `VALIDADO`; decisão `LIBERADO_PARA_FASE02`; RAW/manifesto/sidecar coincidem.
- SHA-256 RAW: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`.

### FASE02 — Integridade da fonte
- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE02_INTEGRIDADE_FONTE_V1.json`.
- Estado `VALIDADO`; decisão `LIBERADO_PARA_FASE03`.
- ZIP com um membro `COTAHIST_A2020.TXT`; teste ZIP sem erro; 1.251.648 linhas físicas; 245 bytes por registo; zero comprimentos inválidos; 1.251.646 registos tipo `01`.

### FASE03 — Parsing estrutural
- Workflow: `.github/workflows/cotahist-fase03-parsing-2020-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38435123333.
- Estado: em execução; evidência `dados/cotahist/quality/COTAHIST_2020_FASE03_PARSING_V1.json` pendente.
- Só avançar para FASE04 se a evidência confirmar zero comprimentos/datas inválidos e datas dentro de 2020.

### Roadmap operacional imediato
1. FASE00–FASE02 (2020): VALIDADO.
2. FASE03 (2020): verificar run e evidência.
3. FASE04 (2020): reconstruir NORMALIZED após FASE03 válida; comparar manifesto e sidecar sem atualizar silenciosamente hashes históricos.

## 47. COTAHIST 2020 — FASE03 validada; FASE04 em execução (2026-10-13)

### FASE03 — Parsing estrutural
- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE03_PARSING_V1.json`.
- Estado `VALIDADO`; decisão `LIBERADO_PARA_FASE04`.
- 1.251.646 registos tipo `01`; 1.251.648 linhas físicas; zero comprimentos inválidos; zero datas inválidas/fora do ano; intervalo 2020-01-02 a 2020-12-30.
- SHA-256 RAW: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`.

### FASE04 — Normalização
- Workflow: `.github/workflows/cotahist-fase04-normalizacao-2020-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase04-normalizacao-2020-v1.yml
- Estado: execução iniciada; evidência `dados/cotahist/quality/COTAHIST_2020_FASE04_NORMALIZACAO_V1.json` pendente.
- O CSV NORMALIZED está ausente; reconstruir com o normalizador canónico após gate FASE03, validando 25 campos, contagem, datas e hash contra manifesto/sidecar.
- Diferenças de versão do parser devem ser documentadas; não atualizar manifesto/sidecar silenciosamente.

### Roadmap operacional imediato
1. FASE00–FASE03 (2020): VALIDADO.
2. FASE04 (2020): run iniciado; verificar resultado e persistência do CSV.
3. FASE05–FASE12: dependem da validação FASE04 e das fases posteriores.

## 48. COTAHIST 2020 — FASE04 validada; FASE05 em execução (2026-10-13)

### FASE04 — Normalização
**Estado: VALIDADO — CSV reconstruído e evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE04_NORMALIZACAO_V1.json`, blob `ca39d64b4aa9df1ebdffd9dee93350ab64b3cd51`.
- Decisão: `LIBERADO_PARA_FASE05`.
- CSV físico: `dados/cotahist/normalized/anual/COTAHIST_A2020.csv`; 1.251.646 linhas, 25 campos; zero datas inválidas/fora do ano; intervalo 2020-01-02 a 2020-12-30.
- SHA-256 calculado = manifesto = sidecar: `cb9230638ae4cec17d9345401ba41e4576b6ff6369f32377367fe20f3c02de50`.
- SHA-256 RAW mantido: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`.
- Parser do manifesto `1.1.0`; script canónico `1.1.2`; diferença registada, sem alterar silenciosamente o manifesto.
- RAW imutável; deduplicação não executada.

### FASE05 — Manifesto e checksum
- Workflow: `.github/workflows/cotahist-fase05-manifesto-checksum-2020-v1.yml`.
- Estado: run iniciado; evidência `dados/cotahist/quality/COTAHIST_2020_FASE05_MANIFESTO_CHECKSUM_V1.json` pendente.
- Validar hashes físicos RAW/NORMALIZED contra manifesto e sidecars, integridade ZIP, contagem e 25 campos.
- Só avançar para FASE06 com evidência `VALIDADO` / `LIBERADO_PARA_FASE06`.

### Roadmap operacional imediato
1. FASE00–FASE04 (2020): VALIDADO.
2. FASE05 (2020): verificar execução e evidência.
3. FASE06–FASE12: bloqueadas até validação de cada fase precedente.

## 49. COTAHIST 2020 — FASE05 validada; FASE06 publicada (2026-10-13)

### FASE05 — Manifesto e checksum
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE05_MANIFESTO_CHECKSUM_V1.json`, blob `114ce5eeb41d218813c279e6f4c34db9f6b91caf`.
- Decisão: `LIBERADO_PARA_FASE06`.
- RAW SHA-256: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`; NORMALIZED SHA-256: `cb9230638ae4cec17d9345401ba41e4576b6ff6369f32377367fe20f3c02de50`.
- RAW/manifesto/sidecar e NORMALIZED/manifesto/sidecar concordantes; ZIP `PASS`; 1.251.646 linhas; 25 campos; datas 2020-01-02 a 2020-12-30; RAW imutável e deduplicação não executada.

### FASE06 — Reconciliação semântica
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase06-reconciliacao-2020-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase06-reconciliacao-2020-v1.yml
- Commit: `1e6d7418fab1f92f960d6b6fb9aaabad4ff52504`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2020_FASE06_RECONCILIACAO_V1.json`.
- Compara 12 campos críticos por ordem de registo, com hashes e contagens físicas confirmados; não modifica RAW nem deduplica.
- Só avançar para FASE07 com `VALIDADO`, `LIBERADO_PARA_FASE07` e zero divergências.

### Roadmap operacional imediato
1. FASE00–FASE05 (2020): VALIDADO.
2. FASE06 (2020): executar/verificar reconciliação semântica.
3. FASE07–FASE12: dependem das evidências das fases anteriores.

## 50. COTAHIST 2020 — FASE06 validada; FASE07 publicada (2026-10-13)

### FASE06 — Reconciliação semântica
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE06_RECONCILIACAO_V1.json`, blob `1402fa8e0779c2529c66c4134a0b588e9bfe39f1`.
- Decisão: `LIBERADO_PARA_FASE07`.
- 1.251.646 registos RAW/NORMALIZED reconciliados nos 12 campos críticos, em ordem original; divergências: 0.
- SHA-256 RAW: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`.
- SHA-256 NORMALIZED: `cb9230638ae4cec17d9345401ba41e4576b6ff6369f32377367fe20f3c02de50`.
- RAW imutável; deduplicação não executada.

### FASE07 — Identidade e cardinalidade
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase07-identidade-2020-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase07-identidade-2020-v1.yml
- Commit: `29d040e22ecd0d3868ca5645cf75c5e6d3cd1122`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2020_FASE07_IDENTIDADE_CHAVES_V1.json`.
- Avalia chave-base e chave candidata com `prazot`; não deduplica nem generaliza a outros anos.
- Só avançar para FASE08 após evidência persistida e validada.

### Roadmap operacional imediato
1. FASE00–FASE06 (2020): VALIDADO.
2. FASE07 (2020): workflow publicado; verificar identidade/cardinalidade.
3. FASE08–FASE12: bloqueadas até evidências das fases precedentes.

## 51. COTAHIST 2020 — FASE07 validada; FASE08 publicada (2026-10-13)

### FASE07 — Identidade e cardinalidade
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE07_IDENTIDADE_CHAVES_V1.json`, blob `18d7b4d1bc297b2f3af945a28610735f05653083`.
- Decisão: `CHAVE_CANDIDATA_COM_PRAZOT_VALIDADA_POR_CARDINALIDADE`.
- 1.251.646 registos analisados.
- Chave-base: 1.177.517 chaves distintas, 25.360 grupos colidentes e 74.129 linhas excedentes; todos os grupos colidentes contêm linhas completas diferentes.
- Chave candidata com `prazot`: 1.251.646 chaves distintas e zero colisões; 25.360 grupos base separados por `prazot`.
- Nenhuma deduplicação ou remoção de linhas.

### FASE08 — Calendário e consistência temporal
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase08-calendario-2020-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase08-calendario-2020-v1.yml
- Commit: `167e98a7eb3e064f32549fae244e9cdad1ab3d40`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2020_FASE08_SEMANTICA_CALENDARIO_V1.json`.
- Valida datas, cronologia, regressões por instrumento e lacunas de calendário; regressões de ordem só podem ser aceites como exceções se a reconciliação FASE06 confirmar os campos críticos em ordem original.
- Só avançar para Gate 06–08 depois de evidência FASE08 persistida e sem bloqueadores.

### Roadmap operacional imediato
1. FASE00–FASE07 (2020): VALIDADO.
2. FASE08 (2020): workflow publicado; verificar resultado.
3. Gate 06–08 e FASE09: somente após FASE08.

## 52. COTAHIST 2020 — FASE08 validada com exceção; Gate 06–08 a publicar (2026-10-13)

### FASE08 — Calendário e consistência temporal
**Estado: VALIDADO_COM_EXCECAO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE08_SEMANTICA_CALENDARIO_V1.json`, blob `553acb572207cdf89767a66b691077309e1c96c9`.
- Decisão: `LIBERADO_PARA_GATE_06_08`.
- 1.251.646 linhas; 249 datas de negociação entre 2020-01-02 e 2020-12-30; zero datas inválidas/fora do ano; nenhuma data de fim de semana.
- 45.574 regressões cronológicas na sequência física; zero regressões temporais por instrumento. As regressões de ordenação foram classificadas como exceção não bloqueadora com base na reconciliação FASE06 dos campos críticos por ordem original. FASE10 continuará a verificar os 25 campos.
- 266.523 transições lexicográficas de instrumentos: métrica informativa; calendário oficial histórico B3 não persistido.
- Nenhuma linha removida; deduplicação não executada.

### Gate independente FASE06–FASE08
**Estado: próximo workflow a publicar/executar.**

- Evidência esperada: `dados/cotahist/quality/COTAHIST_2020_GATE_06_08_V1.json`.
- Deve revalidar hashes, contagens, 25 campos, datas, exceções e ausência de mutação; aceitar regressões de ordenação somente se classificadas explicitamente como não bloqueadoras pela FASE08.
- Só avançar para FASE09 após Gate `VALIDADO_COM_EXCECAO` / `LIBERADO_PARA_FASE09` e zero bloqueadores.

### Roadmap operacional imediato
1. FASE00–FASE08 (2020): validadas; FASE08 contém exceção de ordem física explicitamente classificada.
2. Gate 06–08 (2020): publicar, executar e verificar.
3. FASE09–FASE12: somente após o Gate.

## 53. COTAHIST 2020 — Gate 06–08 validado; FASE09 publicada (2026-10-13)

### Gate independente FASE06–FASE08
**Estado: VALIDADO_COM_EXCECAO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_GATE_06_08_V1.json`, blob `ca9f838b086ed5691539e62ab87238e1df8c04a9`.
- Decisão: `LIBERADO_PARA_FASE09`; zero bloqueadores.
- 1.251.646 linhas, 25 campos, 249 datas; hashes NORMALIZED concordantes nas FASE06/07/08; zero datas inválidas/fora do ano e nenhuma data de fim de semana.
- 45.574 regressões cronológicas aceites como exceção explícita não bloqueadora; zero regressões temporais por instrumento; nenhuma deduplicação.

### FASE09 — Pre-release
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase09-prerelease-2020-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase09-prerelease-2020-v1.yml
- Commit: `5b28c1aa4b4c14aa0faa5198b6c262ebcb4cb1dc`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2020_FASE09_PRE_RELEASE_V1.json`.
- Gate `VALIDADO_COM_EXCECAO` / `LIBERADO_PARA_FASE09`; verificar artefactos, hashes e exceções classificadas antes da FASE10.

### Roadmap operacional imediato
1. FASE00–FASE08 (2020): validadas.
2. Gate 06–08 (2020): VALIDADO_COM_EXCECAO, zero bloqueadores.
3. FASE09 (2020): workflow publicado; verificar run/evidência.
4. FASE10–FASE12: dependem da FASE09 e da validação independente dos 25 campos.

## 54. COTAHIST 2020 — FASE09 liberada; FASE10 publicada (2026-10-13)

### FASE09 — Pre-release
**Estado: LIBERADO_PARA_FASE10 — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE09_PRE_RELEASE_V1.json`, blob `fe6aed84ce28399f18fc2a76d390cc28d31a1aad`.
- Decisão `LIBERADO_PARA_FASE10`; `missing=[]`; `blocked=[]`.
- FASE03–FASE08, Gate, RAW, NORMALIZED e manifesto aceites.
- SHA-256 RAW: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`.
- SHA-256 NORMALIZED: `cb9230638ae4cec17d9345401ba41e4576b6ff6369f32377367fe20f3c02de50`.
- Exceções FASE08 preservadas; FASE09 não retrocertifica fases anteriores.

### FASE10 — Validação independente integral
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase10-validacao-independente-2020-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase10-validacao-independente-2020-v1.yml
- Commit: `7580af260632916cf869d36013ae12abb5aabd59`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2020_FASE10_VALIDACAO_INDEPENDENTE_V1.json`.
- Comparar independentemente os 25 campos RAW × NORMALIZED, hashes/contagens e integridade do ZIP; não modificar RAW nem deduplicar.
- Só avançar para FASE11 com `VALIDADO`, `LIBERADO_PARA_FASE11`, 25 campos e zero divergências.

### Roadmap operacional imediato
1. FASE00–FASE09 (2020): validadas/liberadas conforme evidências.
2. FASE10 (2020): executar/verificar reconciliação integral.
3. FASE11–FASE12: dependem da FASE10 sem divergências.

## 55. COTAHIST 2020 — FASE10 validada; FASE11 publicada (2026-10-13)

### FASE10 — Validação independente integral
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE10_VALIDACAO_INDEPENDENTE_V1.json`, blob `a68df016a85281eccd6a1b3b0cb40b28220663a1`.
- Decisão: `LIBERADO_PARA_FASE11`.
- 1.251.646 registos RAW/NORMALIZED; registos físicos de 245 bytes; `00=1`, `01=1.251.646`, `99=1`.
- Os 25 campos foram comparados independentemente; divergências: 0; amostra vazia.
- SHA-256 RAW: `86442168939b9da7b3cc1ec1662c333ee5ab4c75f2be1865b5bf55ba4c52168f`.
- SHA-256 NORMALIZED: `cb9230638ae4cec17d9345401ba41e4576b6ff6369f32377367fe20f3c02de50`.
- RAW não modificado; deduplicação não executada.

### FASE11 — Certificação
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase11-certificacao-2020-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase11-certificacao-2020-v1.yml
- Commit: `7dc9cfa6d23bc5be24f0bb2850b52c5249cebc35`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2020_FASE11_CERTIFICACAO_V1.json`.
- Só avançar para FASE12 com `CERTIFICADO`, `LIBERADO_PARA_FASE12` e zero bloqueadores.

### Roadmap operacional imediato
1. FASE00–FASE10 (2020): validadas/liberadas conforme evidências individuais.
2. FASE11 (2020): workflow publicado; verificar certificação.
3. FASE12: somente após certificação; validar transição RAW 2021 sem certificar automaticamente 2021.

## 56. COTAHIST 2020 — FASE11 certificada; FASE12 publicada (2026-10-13)

### FASE11 — Certificação
**Estado: CERTIFICADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE11_CERTIFICACAO_V1.json`.
- Decisão: `LIBERADO_PARA_FASE12`; zero bloqueadores.
- FASE10: 25 campos, zero divergências; Gate 06–08 `VALIDADO_COM_EXCECAO`; hashes RAW/NORMALIZED conferem com manifesto.
- Escopo: integridade e consistência do COTAHIST 2020, sem autorização para deduplicação nem certificação de estratégias.

### FASE12 — Fechamento 2020 e transição para 2021
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase12-fechamento-2020-abertura-2021-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase12-fechamento-2020-abertura-2021-v1.yml
- Commit: `f338aa4f4d17d1869d93874326ab210842753aa6`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2020_FASE12_FECHAMENTO_2021_ABERTURA_V1.json`.
- RAW 2021: SHA-256 `b0d4aed17d609c7ba615a23320c2fd513b580a251ae7d884a5015ef8a3fe4705`, igual ao manifesto e sidecar; ZIP ainda precisa de validação física pela FASE12.
- A transição fecha 2020, não certifica 2021; o ciclo seguinte começa pela FASE00.

### Roadmap operacional imediato
1. COTAHIST 2020: FASE00–FASE11 validadas/certificadas.
2. FASE12 (2020): verificar run e evidência.
3. COTAHIST 2021: após transição, iniciar FASE00 e reconstruir NORMALIZED se ausente.
4. Preservar RAW/linhas e manter REC-001 B3 × BLOOMBERG_MAIL independente e bloqueada.

## 57. COTAHIST 2020 — FASE12 concluída; ciclo 2021 autorizado (2026-10-13)

### FASE12 — Fechamento e transição
**Estado: FECHADO_COM_TRANSICAO_CONTROLADA — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2020_FASE12_FECHAMENTO_2021_ABERTURA_V1.json`, blob `e37874a4d4e9b1c8d2d4cf92dcd160e97350b516`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38436853749 — sucesso.
- Decisão: `FECHAR_2020_E_AUTORIZAR_CONTINUACAO_2021`; zero bloqueadores.
- FASE10 2020 `VALIDADO`; FASE11 2020 `CERTIFICADO`.
- RAW 2021 SHA-256: `b0d4aed17d609c7ba615a23320c2fd513b580a251ae7d884a5015ef8a3fe4705`, igual ao manifesto e sidecar; ZIP com um membro, zero comprimentos inválidos; 1.831.862 registos tipo `01`.
- NORMALIZED CSV 2021 ausente; `year2021_phase04_status=AGUARDA_RECONSTRUCAO_CSV`. A transição não certifica 2021.

### COTAHIST 2021 — início do ciclo
- Iniciar pela FASE00, usando a transição 2020→2021 como pré-condição.
- Executar FASE01–03 e reconstruir NORMALIZED na FASE04.
- Não reutilizar evidências de anos anteriores; RAW imutável e deduplicação não autorizada.

### Roadmap operacional imediato
1. COTAHIST 2020: fechado após certificação.
2. COTAHIST 2021: FASE00 a iniciar.
3. REC-001 B3 × BLOOMBERG_MAIL continua independente e bloqueada.

## 58. COTAHIST 2021 — FASE00 validada; FASE01 iniciada (2026-10-13)

### FASE00 — Governação
- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE00_GOVERNANCA_V1.json`.
- Estado `VALIDADO`; decisão `AUTORIZAR_FASE01`; zero bloqueadores.
- Layout Mestre V1.0.1 confirmado; transição 2020→2021 validada.
- RAW 2021, manifesto e sidecar presentes; NORMALIZED CSV ausente, reconstrução prevista após FASE01–03.

### FASE01 — Aquisição RAW
- Workflow: `.github/workflows/cotahist-fase01-aquisicao-2021-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38437052896.
- Estado: enfileirado; evidência `dados/cotahist/quality/COTAHIST_2021_FASE01_AQUISICAO_RAW_V1.json` pendente.
- SHA-256 esperado conforme manifesto/sidecar: `b0d4aed17d609c7ba615a23320c2fd513b580a251ae7d884a5015ef8a3fe4705`.

### Roadmap operacional imediato
1. FASE00 (2021): VALIDADO.
2. FASE01 (2021): verificar run/evidência.
3. FASE02–FASE03 (2021): após FASE01.
4. FASE04 (2021): reconstruir NORMALIZED após parsing válido, sem modificar RAW.

## 59. COTAHIST 2021 — FASE01 validada; FASE02 publicada (2026-10-13)

### FASE01 — Aquisição/proveniência RAW
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE01_AQUISICAO_RAW_V1.json`.
- Blob SHA: `3ccff2ba3dcb682e46423180f1761ca3a0a7a698`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38437052896 — concluído com sucesso.
- Decisão: `LIBERADO_PARA_FASE02`.
- SHA-256 RAW: `b0d4aed17d609c7ba615a23320c2fd513b580a251ae7d884a5015ef8a3fe4705`; manifesto e sidecar concordam.
- Evidência classificada como verificação retrospectiva da aquisição: confirma proveniência e integridade do artefacto já persistido, sem o substituir nem modificar.

### FASE02 — Integridade física e estrutural
**Estado: WORKFLOW PUBLICADO; execução/evidência pendentes.**

- Workflow: `.github/workflows/cotahist-fase02-integridade-2021-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase02-integridade-2021-v1.yml
- Commit: `82b09e61aa219a0c16e3ced0e7b1cadb864809b8`.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE02_INTEGRIDADE_FONTE_V1.json`.
- Gate de entrada: FASE01 VALIDADO/liberado e igualdade do SHA-256 calculado com manifesto, sidecar e evidência FASE01.
- Valida ZIP, número de membros, CRC, tamanho de 245 bytes, tipos de registo `00`, `01` e `99`; não executa parsing nem normalização.
- Não foi encontrada execução da FASE02 no endpoint de runs consultado após a publicação; não declarar sucesso até a evidência persistir.

### Roadmap operacional imediato
1. COTAHIST 2021: FASE00 e FASE01 VALIDADO.
2. FASE02: workflow publicado; confirmar execução e evidência persistida.
3. FASE03: parsing apenas depois de FASE02 VALIDADO/liberado.
4. FASE04: reconstruir NORMALIZED a partir de RAW, preservando hash e todas as linhas.
5. REC-001 B3 × BLOOMBERG_MAIL permanece independente e bloqueada.

## 60. COTAHIST 2021 — FASE02 e FASE03 validadas; FASE04 em execução (2026-10-13)

### FASE02 — Integridade física da fonte
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE02_INTEGRIDADE_FONTE_V1.json`.
- Blob SHA: `4bc04facd284db779b457a7fe7c4580a38977692`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480257022 — sucesso.
- Decisão: `LIBERADO_PARA_FASE03`.
- RAW SHA-256: `b0d4aed17d609c7ba615a23320c2fd513b580a251ae7d884a5015ef8a3fe4705`; ZIP com um membro `COTAHIST_A2021.TXT`, CRC íntegro, zero comprimentos inválidos.
- 1.831.864 linhas físicas: header `00=1`, registos `01=1.831.862`, trailer `99=1`.

### FASE03 — Parsing estrutural
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE03_PARSING_V1.json`.
- Blob SHA: `baea76d4fa6fbe9c9d6dd264b9ce164f691f6702`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480328958 — sucesso.
- Decisão: `LIBERADO_PARA_FASE04`.
- 1.831.862 registos de cotação; 245 bytes por registo; zero comprimentos inválidos e zero datas inválidas.
- Intervalo: 2021-01-04 a 2021-12-30.
- Parsing estrutural não certifica normalização nem semântica.

### FASE04 — Normalização e reconciliação
**Estado: WORKFLOW EM EXECUÇÃO; evidência pendente no momento desta atualização.**

- Workflow: `.github/workflows/cotahist-fase04-normalizacao-2021-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-fase04-normalizacao-2021-v1.yml
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480393973.
- Objetivo: reconstruir NORMALIZED a partir do RAW imutável, conferir manifesto/checksum e reconciliar contagens/datas; só persistir CSV quando validado.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE04_NORMALIZACAO_V1.json`.
- Não avançar para FASE05 até validar a evidência persistida e confirmar o SHA-256 físico do CSV.

### Roadmap operacional imediato
1. FASE00–FASE03 (2021): VALIDADO.
2. FASE04 (2021): execução em curso; verificar resultado e artefactos.
3. FASE05: apenas após FASE04 VALIDADO.
4. Preservar RAW e linhas; não deduplicar.

## 61. COTAHIST 2021 — otimização operacional da FASE04 e preparação da FASE05 (2026-10-13)

- Identificada ineficiência no primeiro run da FASE04: checkout completo do repositório com `fetch-depth: 0` e LFS.
- Workflow corrigido para checkout esparso (`sparse-checkout`) apenas dos artefactos necessários e `fetch-depth: 1`, mantendo LFS e o normalizador canónico.
- Workflow corrigido: `.github/workflows/cotahist-fase04-normalizacao-2021-v1.yml`.
- Commit de correção: `9e983eae18868522be30e64ea0e8f3996d016fad`.
- Run inicial: https://github.com/carlos-andrade/B3/actions/runs/38480393973 — em execução no último ponto de observação, na etapa de normalização; não declarar resultado final.
- Run com checkout otimizado: https://github.com/carlos-andrade/B3/actions/runs/38480513763 — pendente atrás do run inicial, por `concurrency` sem cancelamento.
- FASE05 preparada: `.github/workflows/cotahist-fase05-manifesto-checksum-2021-v1.yml`, commit `f0d1fd8dfae54872d84d841d8676baa8547dd3dd`. O disparo automático foi limitado à evidência FASE04, evitando execução prematura na criação do workflow.
- Próximo passo: aguardar o run FASE04 inicial terminar; validar a evidência e o CSV persistidos. Se o run inicial falhar/expirar, o run otimizado poderá assumir após a libertação do grupo de concorrência.

## 62. COTAHIST 2021 — FASE04 validada; FASE05 em execução (2026-10-13)

### FASE04 — Normalização
**Estado: VALIDADO — evidência e NORMALIZED persistidos.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE04_NORMALIZACAO_V1.json`, blob `0480eb655b6917e91bf54089e59dc60ab259699a`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480393973 — `completed / success`.
- Decisão: `LIBERADO_PARA_FASE05`; zero bloqueadores.
- 1.831.862 linhas, 25 campos; datas inválidas/fora de 2021: zero; intervalo 2021-01-04 a 2021-12-30.
- SHA-256 NORMALIZED calculado = manifesto = sidecar: `0d0be90795918373ccbf2da068d563bef1d0ad83ca6b36f708730498aecfb3c2`.
- O CSV está em Git LFS, ponteiro com tamanho declarado de 247.991.181 bytes. RAW permanece inalterado; deduplicação não executada.
- O run de repetição com checkout esparso foi enfileirado e começou após o run inicial; acompanhar para garantir que termine sem divergência.

### FASE05 — Manifesto e checksum
**Estado: WORKFLOW EM EXECUÇÃO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase05-manifesto-checksum-2021-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480769247.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE05_MANIFESTO_CHECKSUM_V1.json`.
- O workflow foi ajustado para permitir disparo controlado por alteração da própria definição ou pela evidência FASE04. Isso evita depender exclusivamente de eventos de push originados por GitHub Actions, que podem não encadear workflows.
- FASE06 preparada em `.github/workflows/cotahist-fase06-reconciliacao-2021-v1.yml`; aguarda FASE05 e deve ser verificada após execução.

### Roadmap operacional imediato
1. FASE00–FASE04 (2021): VALIDADO.
2. FASE05 (2021): execução em curso; verificar hash físico RAW/NORMALIZED, manifesto, sidecar e evidência.
3. FASE06 (2021): preparada; executar após FASE05 validada e reconciliar os 12 campos críticos.
4. Preservar RAW/linhas; não deduplicar.

## 63. COTAHIST 2021 — FASE05 validada; FASE06 reexecutada (2026-10-13)

### FASE05 — Manifesto e checksum
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE05_MANIFESTO_CHECKSUM_V1.json`, blob `3c5993d25db3d8df2b519e3df9e1e71930daf3e3`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480769247 — `completed / success`.
- Decisão: `LIBERADO_PARA_FASE06`.
- RAW SHA-256: `b0d4aed17d609c7ba615a23320c2fd513b580a251ae7d884a5015ef8a3fe4705`; manifesto, sidecar e FASE01/02/04 concordantes.
- NORMALIZED SHA-256: `0d0be90795918373ccbf2da068d563bef1d0ad83ca6b36f708730498aecfb3c2`; manifesto, sidecar e FASE04 concordantes.
- 1.831.862 linhas, 25 campos, datas de 2021 válidas; ZIP `PASS`. RAW não modificado; nenhuma deduplicação.

### Correção de persistência da FASE04
- O run otimizado `38480513763` concluiu a validação, mas falhou ao persistir porque o CSV NORMALIZED não estava incluído no sparse-checkout.
- A lista sparse-checkout foi corrigida para incluir `dados/cotahist/normalized/anual/COTAHIST_A2021.csv`.
- Commit: `b8860f15a88dbfe760e745c20e1557fbcdfeb15b`.
- Run de verificação da correção: https://github.com/carlos-andrade/B3/actions/runs/38480963443 — enfileirado no último ponto de observação. A FASE04 original continua válida; o retry serve para provar persistência idempotente.

### FASE06 — Reconciliação semântica
**Estado: RUN EM EXECUÇÃO; evidência ainda não confirmada.**

- Workflow: `.github/workflows/cotahist-fase06-reconciliacao-2021-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480911087.
- O primeiro run `38480779003` ocorreu antes da evidência FASE05 e falhou na pré-condição; não foi encontrado artefacto FASE06 persistido desse run.
- Novo run disparado após FASE05 e após alteração controlada da definição; verificar evidência `dados/cotahist/quality/COTAHIST_2021_FASE06_RECONCILIACAO_V1.json`.
- Avançar para FASE07 somente se `VALIDADO`, `LIBERADO_PARA_FASE07`, `mismatch_count=0` e hashes/contagens concordantes.

### Roadmap operacional imediato
1. FASE00–FASE05 (2021): VALIDADO.
2. FASE06: execução em curso; verificar resultado e evidência.
3. Retry FASE04: aguardar e verificar persistência idempotente.
4. FASE07: somente após FASE06 sem divergências.

## 64. COTAHIST 2021 — FASE06 validada; FASE07 em execução (2026-10-13)

### FASE06 — Reconciliação semântica
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE06_RECONCILIACAO_V1.json`, blob `f7a3a56f63312b6714405041e16cb065549203c0`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480911087 — validação concluída com sucesso.
- Decisão: `LIBERADO_PARA_FASE07`; divergências: zero.
- 1.831.862 registos RAW e NORMALIZED; hashes concordantes.
- 12 campos críticos reconciliados: data, código BDI, ticker, mercado, preços de abertura/máximo/mínimo/médio/último, número de negócios, quantidade e volume financeiro.
- Chave/identidade fica deliberadamente para FASE07; nenhuma linha removida e nenhuma deduplicação.

### FASE07 — Identidade e cardinalidade
**Estado: RUN EM EXECUÇÃO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase07-identidade-2021-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481092183.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE07_IDENTIDADE_CHAVES_V1.json`.
- Testa chave-base e candidata com `prazot`, mede cardinalidade/colisões e preserva todas as linhas.
- Só avançar para FASE08 se a evidência confirmar `VALIDADO`, decisão de chave candidata validada por cardinalidade e zero colisões na chave aprovada.

### FASE04 — retry de persistência
- Run: https://github.com/carlos-andrade/B3/actions/runs/38480963443 — em execução na última observação.
- A primeira FASE04 permanece VALIDADO e o CSV/manifesto/sidecar estão persistidos. O retry testa a correção do sparse-checkout para evitar falha de indexação ao persistir o CSV LFS.
- Não tratar o retry pendente como falha da validação original nem como uma nova certificação.

### Roadmap operacional imediato
1. FASE00–FASE06 (2021): VALIDADO.
2. FASE07: aguardar evidência de identidade/cardinalidade.
3. FASE08: preparada; executar após FASE07 validada.
4. Acompanhar retry FASE04 até término e confirmar resultado.

## 65. COTAHIST 2021 — FASE07 validada; FASE08 e Gate preparados (2026-10-13)

### FASE07 — Identidade e cardinalidade
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE07_IDENTIDADE_CHAVES_V1.json`, blob `983a378e27f1b1860f786db7088d41ad6231aef2`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481092183 — `completed / success`.
- Decisão: `CHAVE_CANDIDATA_COM_PRAZOT_VALIDADA_POR_CARDINALIDADE`.
- Registos: 1.831.862; hash NORMALIZED: `0d0be90795918373ccbf2da068d563bef1d0ad83ca6b36f708730498aecfb3c2`.
- Chave-base `data_pregao+codbdi+codneg+tpmerc+dismes`: 1.748.312 chaves distintas; 28.694 grupos duplicados; 83.550 linhas excedentes. Nenhum grupo era idêntico na linha completa.
- Chave candidata com `prazot`: 1.831.862 chaves distintas; zero grupos duplicados/linhas excedentes. `prazot` separa os registos que colidem na chave-base.
- Conclusão restrita ao ficheiro/hash de 2021; nenhuma linha removida e nenhuma deduplicação.

### FASE08 — Calendário e consistência temporal
**Estado: RUN ENFILEIRADO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase08-calendario-2021-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase08-calendario-2021-v1.yml
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE08_SEMANTICA_CALENDARIO_V1.json`.
- Verifica datas, regressões cronológicas e temporais por instrumento, distribuição semanal e lacunas; não reordena nem remove linhas.
- O calendário oficial histórico B3 não está incorporado, pelo que a fase não poderá afirmar equivalência com a lista oficial de sessões/feriados.

### Gate independente FASE06–FASE08
**Estado: WORKFLOW PREPARADO; execução após FASE08.**

- Workflow: `.github/workflows/cotahist-gate-06-08-2021-v1.yml`.
- URL: https://github.com/carlos-andrade/B3/blob/main/.github/workflows/cotahist-gate-06-08-2021-v1.yml
- Revalida hashes, contagens, datas, 25 campos, exceções e ausência de deduplicação.
- O Gate só pode liberar FASE09 se as evidências FASE06/07/08 estiverem persistidas, os checks passarem e as exceções forem explícitas.

### FASE04 — repetição idempotente
- Run https://github.com/carlos-andrade/B3/actions/runs/38480963443 — `completed / success`.
- Evidência atualizada: `dados/cotahist/quality/COTAHIST_2021_FASE04_NORMALIZACAO_V1.json`, blob `279b70b0c6ba09e36c91fee894c6dca19469b21e`.
- O CSV foi persistido com sucesso após incluir o seu caminho na definição de sparse-checkout. Hash e contagem mantiveram-se inalterados.

### Roadmap operacional imediato
1. FASE00–FASE07 (2021): VALIDADO.
2. FASE08: run enfileirado; verificar evidência.
3. Gate 06–08: executar após FASE08.
4. FASE09: somente após Gate validado, sem bloqueadores.

## 66. COTAHIST 2021 — FASE08 bloqueada; diagnóstico de ordenação em curso (2026-10-13)

### Resultado da FASE08 original
**Estado: BLOQUEADO — não autoriza Gate 06–08 nem FASE09.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE08_SEMANTICA_CALENDARIO_V1.json`, blob `569fa602f53e092f27263d77ab49ad903ac89a93`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481217167 — validação falhou e evidência foi persistida.
- Datas inválidas: 0; datas fora de 2021: 0; 247 datas distintas, intervalo 2021-01-04 a 2021-12-30; datas de fim de semana: nenhuma.
- Regressões de data na ordem física: 139.405.
- Regressões temporais sob a chave instrumental inicial `codbdi+codneg+tpmerc+prazot+dismes`: 73.784.
- Bloqueadores: `REGRESSAO_CRONOLOGICA`, `REGRESSAO_TEMPORAL_POR_INSTRUMENTO`.
- A FASE06 confirmou que RAW e NORMALIZED correspondem linha a linha nos 12 campos críticos, mas isso prova fidelidade da transformação, não conformidade da ordenação com o contrato oficial.

### Fonte normativa e hipótese de diagnóstico
- Layout oficial B3, revisão 02 (05/10/2020): https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf
- O documento descreve o COTAHIST como classificado por tipo de registo, data do pregão, código BDI, nome da empresa e código de negociação. A FASE08 bloqueada não deve ser contornada até determinar se a sequência física de 2021 viola essa classificação, se há uma regra de ordenação adicional, ou se a chave de instrumento inicial era insuficiente.
- Não reordenar o NORMALIZED, não alterar o RAW e não classificar as regressões como não bloqueadoras sem evidência.

### Diagnóstico de ordenação — workflow separado
**Estado: RUN ENFILEIRADO; não certificador.**

- Workflow: `.github/workflows/cotahist-fase08-diagnostico-ordem-2021-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481418609.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE08_DIAGNOSTICO_ORDEM_V1.json`.
- Regista amostras com ticker/nome/especificação, regressões de ordenação por chaves candidatas (data-primeiro versus instrumento-primeiro) e regressões temporais usando identidade mais completa, incluindo `nomres`, `especi`, `modref` e `codisi`.
- O diagnóstico não altera a evidência FASE08 original e não libera fases seguintes. A decisão de correção dependerá dos resultados e da referência normativa.

### Roadmap operacional imediato
1. FASE00–FASE07 (2021): VALIDADO.
2. FASE08: BLOQUEADO; investigar ordenação e chave de instrumento.
3. Gate 06–08 e FASE09: suspensos até resolução documentada do bloqueio.
4. Preservar RAW, CSV original e evidência de bloqueio; nenhuma deduplicação.

## 67. COTAHIST 2021 — diagnóstico de ordenação concluído; FASE08 V2 em execução (2026-10-13)

### Diagnóstico de ordenação
**Estado: DIAGNOSTICO_CONCLUIDO — não certificador.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE08_DIAGNOSTICO_ORDEM_V1.json`, blob `1286007fc5c4a1bfae862b97f65ca6450e06e2de`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481418609 — sucesso.
- 1.831.862 registos; datas válidas; 247 datas distintas; intervalo 2021-01-04 a 2021-12-30.
- Regressões de data física: 139.405; regressões temporais sob a chave instrumental inicial: 73.784.
- Chave temporal mais completa testada (`codbdi+nomres+codneg+tpmerc+especi+prazot+modref+codisi+dismes`) ainda mostra 66.028 regressões; logo, a chave inicial não explica por si só a sequência observada.
- Regressões lexicográficas: chave data-primeiro = 207.261; instrumento-primeiro = 192.167; ticker/mercado/data = 71.237. Nenhuma das chaves candidatas testadas explica monotonicidade integral da ordem física.
- As amostras mostram blocos em que a data regressa de 2021-02-11 para 2021-01-04. A evidência não demonstra alteração dos valores, mas demonstra que a ordem física não é globalmente cronológica.
- Comparativo histórico: FASE08 de 2020 classificou 45.574 regressões cronológicas e zero regressões temporais por instrumento como exceção não bloqueadora após reconciliação de linhas críticas; 2019 registou 568/132. O caso 2021 tem magnitude superior e fica explicitamente registado para validação independente integral na FASE10.
- Fonte normativa: [Layout oficial COTAHIST B3, revisão 02](https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf). A descrição do arquivo refere classificação por tipo de registo, data do pregão, BDI, nome e código de negociação; por isso a exceção de 2021 não é ocultada.

### FASE08 V2 — consistência temporal com exceções explicitamente classificadas
**Estado: RUN EM EXECUÇÃO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase08-calendario-2021-v2.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/workflows/cotahist-fase08-calendario-2021-v2.yml
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE08_SEMANTICA_CALENDARIO_V2.json`.
- A V2 aplica o precedente auditável de 2019/2020: regressões de ordem física são classificadas como exceções não bloqueadoras somente porque a FASE06 comprova reconciliação dos campos críticos RAW × NORMALIZED, os hashes coincidem, as datas são válidas e nenhuma linha é reordenada/removida.
- Esta classificação não declara a ordem física correta nem certifica os 25 campos; a FASE10 continua obrigatória e deve comparar todos os campos em ordem original.
- A evidência FASE08 V1 BLOQUEADO e o diagnóstico separado permanecem preservados; o Gate/FASE09 foram atualizados para consumir V2, não V1.

### Roadmap operacional imediato
1. FASE00–FASE07 (2021): VALIDADO.
2. FASE08 V1: BLOQUEADO e preservado como histórico.
3. FASE08 V2: executar/verificar; aceitar apenas exceções explícitas e zero bloqueadores.
4. Gate 06–08: após V2 validada, confirmar hashes, datas, contagens e exceções.
5. FASE09: após Gate válido; FASE10 independente dos 25 campos continua obrigatória.

## 68. COTAHIST 2021 — FASE08 V2 e Gate 06–08 validados; FASE09 enfileirada (2026-10-13)

### FASE08 V2 — consistência temporal com exceções classificadas
**Estado: VALIDADO_COM_EXCECAO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE08_SEMANTICA_CALENDARIO_V2.json`, blob `cde96cf94a536ca698828036aa9964920851cda6`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481632305 — sucesso.
- Decisão: `LIBERADO_PARA_GATE_06_08`; zero bloqueadores.
- 1.831.862 linhas, 25 campos; 247 datas distintas; intervalo 2021-01-04 a 2021-12-30; datas inválidas/fora do ano: zero; fins de semana: nenhum.
- Regressões cronológicas: 139.405; regressões temporais por instrumento na chave usada pela fase: 73.784. Ambas são registadas como exceções não bloqueadoras, pois a FASE06 comprovou reconciliação dos campos críticos RAW × NORMALIZED na ordem original, os hashes coincidem e nenhuma linha foi reordenada/removida.
- Limitação explícita: a ordem física de 2021 não é declarada correta nem cronológica; a FASE10 permanece obrigatória para comparar independentemente todos os 25 campos.
- A evidência original FASE08 V1 `BLOQUEADO` e o diagnóstico de ordenação são preservados, sem substituição.

### Gate independente FASE06–FASE08
**Estado: VALIDADO_COM_EXCECAO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_GATE_06_08_V1.json`, blob `4a85ef6f5035a8b60feac77d99d906e9147b5c07`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481734467 — sucesso.
- Decisão: `LIBERADO_PARA_FASE09`; zero bloqueadores.
- Todos os checks passaram: FASE06/07/08, hashes NORMALIZED, contagens, 25 campos, datas válidas, exceções explicitamente classificadas, ausência de fins de semana e nenhuma deduplicação.

### FASE09 — Pre-release
**Estado: RUN ENFILEIRADO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase09-prerelease-2021-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481844157.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE09_PRE_RELEASE_V1.json`.
- Confere evidências, hashes RAW/NORMALIZED, manifesto e Gate. Só libera FASE10 se `missing=[]`, `blocked=[]` e o Gate estiver `VALIDADO_COM_EXCECAO / LIBERADO_PARA_FASE09`.

### FASE10 — validação independente de 25 campos
- Workflow preparado: `.github/workflows/cotahist-fase10-validacao-independente-2021-v1.yml`.
- Deve ser executado após FASE09 liberada; não avançar para FASE11 sem 25 campos comparados e zero divergências.

### Roadmap operacional imediato
1. FASE00–FASE08 V2 (2021): VALIDADO; exceções de ordem mantidas explícitas.
2. Gate 06–08: VALIDADO_COM_EXCECAO, liberado para FASE09.
3. FASE09: enfileirada; verificar evidência.
4. FASE10: executar após FASE09 e exigir zero divergências nos 25 campos.

## 69. COTAHIST 2021 — FASE09 liberada; FASE10 em fila (2026-10-13)

### FASE09 — Pre-release
**Estado: LIBERADO_PARA_FASE10 — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE09_PRE_RELEASE_V1.json`, blob `fff72fc5adcbe6ca1b657fc4edb984642b927f5f`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481844157 — `completed / success`.
- Decisão: `LIBERADO_PARA_FASE10`; `missing=[]`, `blocked=[]`.
- Gate: `VALIDADO_COM_EXCECAO / LIBERADO_PARA_FASE09`.
- SHA-256 RAW: `b0d4aed17d609c7ba615a23320c2fd513b580a251ae7d884a5015ef8a3fe4705`.
- SHA-256 NORMALIZED: `0d0be90795918373ccbf2da068d563bef1d0ad83ca6b36f708730498aecfb3c2`.
- FASE09 consolida as evidências e não retrocertifica fases anteriores; as exceções de ordenação continuam explícitas.

### FASE10 — Validação independente dos 25 campos
**Estado: RUN ENFILEIRADO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase10-validacao-independente-2021-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481931550.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE10_VALIDACAO_INDEPENDENTE_V1.json`.
- Gate: FASE09 liberada; hashes RAW/NORMALIZED devem conferir com manifesto/sidecar/FASE09; ZIP íntegro; comparação independente dos 25 campos, em ordem original.
- Só avançar para FASE11 se a evidência confirmar `VALIDADO`, `LIBERADO_PARA_FASE11`, 25 campos e zero divergências.

### Roadmap operacional imediato
1. FASE00–FASE09 (2021): validadas/liberadas conforme evidências persistidas, com exceções temporais explícitas.
2. FASE10: enfileirada; verificar execução, hashes e zero divergências nos 25 campos.
3. FASE11: somente após FASE10 validada.
4. Preservar RAW/CSV e as evidências históricas V1/V2; nenhuma deduplicação.

## 70. COTAHIST 2021 — FASE10 em execução; certificação e transição preparadas (2026-10-13)

- FASE10: run https://github.com/carlos-andrade/B3/actions/runs/38481931550, atualmente na comparação independente dos 25 campos; evidência ainda pendente.
- FASE11 preparada: `.github/workflows/cotahist-fase11-certificacao-2021-v1.yml`; só deverá executar após FASE10 VALIDADO, 25 campos e zero divergências.
- FASE12 preparada: `.github/workflows/cotahist-fase12-fechamento-2021-abertura-2022-v1.yml`; verifica a certificação 2021 e a proveniência/integridade do RAW 2022, sem certificar automaticamente o novo ano.
- RAW 2022 está presente no repositório, SHA-256 manifesto/sidecar `a4f9015b755f797d9c08b0d13f19dbfab18a6c75f379c0271a1cf1b5f6323cd8`; a validação física de 2022 pertence à FASE12 e ao ciclo subsequente.
- Nenhuma destas preparações autoriza pular a FASE10 nem deduplicar dados.

## 71. COTAHIST 2021 — FASE10 validada; FASE11 certificada; FASE12 em fila (2026-10-13)

### FASE10 — Validação independente integral
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE10_VALIDACAO_INDEPENDENTE_V1.json`, blob `f941caa5efedace19074f243b0dbe9df9c3388a3`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38481931550 — `completed / success`.
- Decisão: `LIBERADO_PARA_FASE11`.
- RAW/NORMALIZED: 1.831.862 registos cada; 245 bytes por registo; tipos físicos: header `00=1`, registos `01=1.831.862`, trailer `99=1`.
- Os 25 campos foram comparados independentemente, em ordem original; divergências: 0; amostra vazia.
- SHA-256 RAW: `b0d4aed17d609c7ba615a23320c2fd513b580a251ae7d884a5015ef8a3fe4705`.
- SHA-256 NORMALIZED: `0d0be90795918373ccbf2da068d563bef1d0ad83ca6b36f708730498aecfb3c2`.
- RAW inalterado; deduplicação não executada.

### FASE11 — Certificação
**Estado: CERTIFICADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE11_CERTIFICACAO_V1.json`, blob `2c6c9ecf6f282da55776adf75ecbb1f95ea0e94c`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482176735 — job de certificação concluído com sucesso.
- Decisão: `LIBERADO_PARA_FASE12`; zero bloqueadores.
- Estados verificados: FASE09 `LIBERADO_PARA_FASE10`, FASE10 `VALIDADO`, Gate `VALIDADO_COM_EXCECAO), manifesto `VALIDADO`.
- Escopo: integridade/consistência do COTAHIST 2021 segundo as evidências; a exceção de ordenação física permanece documentada e não autoriza reordenação/deduplicação.

### FASE12 — Fechamento 2021 e transição para 2022
**Estado: RUN ENFILEIRADO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase12-fechamento-2021-abertura-2022-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482231933.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2021_FASE12_FECHAMENTO_2022_ABERTURA_V1.json`.
- RAW 2022 está presente. Manifesto e sidecar declaram SHA-256 `a4f9015b755f797d9c08b0d13f19dbfab18a6c75f379c0271a1cf1b5f6323cd8`; a FASE12 irá validar o hash físico, ZIP e estrutura.
- A transição não certifica 2022. O ciclo 2022 deve iniciar pela FASE00/FASE01 próprias e validar/reconstruir NORMALIZED antes das fases seguintes.

### Roadmap operacional imediato
1. COTAHIST 2021: FASE00–FASE11 certificadas/validadas conforme evidências individuais.
2. FASE12: executar/verificar fechamento e transição para 2022.
3. COTAHIST 2022: iniciar ciclo próprio após FASE12; não reutilizar evidências de 2021.
4. Preservar RAW, linhas e exceções de ordenação; nenhuma deduplicação.

## 72. COTAHIST 2021 fechado; ciclo 2022 iniciado — FASE00–FASE02 validadas (2026-10-13)

### FASE12 — Fechamento 2021 e transição 2022
**Estado: FECHADO_COM_TRANSICAO_CONTROLADA — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2021_FASE12_FECHAMENTO_2022_ABERTURA_V1.json`, blob `f4bb9bfa928896d309c555fcc8dd67ea1cda4a82`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482231933 — sucesso.
- Decisão: `FECHAR_2021_E_AUTORIZAR_CONTINUACAO_2022`; zero bloqueadores.
- RAW 2022: SHA-256 físico = manifesto = sidecar `a4f9015b755f797d9c08b0d13f19dbfab18a6c75f379c0271a1cf1b5f6323cd8`.
- ZIP: um membro `COTAHIST_A2022.TXT`, 2.117.440 registos `01`, header/trailer únicos, zero comprimentos inválidos.
- NORMALIZED 2022 ausente no momento da transição; reconstrução pertence à FASE04 depois de FASE01–03.

### FASE00 — Governação 2022
**Estado: VALIDADO.**

- Evidência: `dados/cotahist/quality/COTAHIST_2022_FASE00_GOVERNANCA_V1.json`, blob `df8d5ef6965ebdd8a03812a60e663abe9ed9c2ea`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482307259 — sucesso.
- Decisão: `AUTORIZAR_FASE01`; transição 2021→2022 confirmada; layout mestre V1.0.1; zero bloqueadores.

### FASE01 — Aquisição/proveniência RAW 2022
**Estado: VALIDADO.**

- Evidência: `dados/cotahist/quality/COTAHIST_2022_FASE01_AQUISICAO_RAW_V1.json`, blob `c7abfbbad54526fa0a129cc6b92f06c6464f00c7`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482333847 — sucesso.
- Decisão: `LIBERADO_PARA_FASE02`; RAW SHA-256, manifesto e sidecar concordam; sem mutação do RAW.

### FASE02 — Integridade física da fonte 2022
**Estado: VALIDADO.**

- Evidência: `dados/cotahist/quality/COTAHIST_2022_FASE02_INTEGRIDADE_FONTE_V1.json`, blob `e3a5d31a4def74cb7e659dab4f72b2cc1c0beeca`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482393243 — sucesso.
- Decisão: `LIBERADO_PARA_FASE03`.
- 2.117.442 linhas físicas; header `00=1`, cotações `01=2.117.440`, trailer `99=1`; 245 bytes por registo; zero comprimentos inválidos.

### FASE03 — Parsing estrutural 2022
**Estado: RUN EM EXECUÇÃO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase03-parsing-2022-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482470145.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2022_FASE03_PARSING_V1.json`.

### FASE04 — Normalização 2022
**Estado: WORKFLOW PREPARADO; aguarda FASE03.**

- Workflow: `.github/workflows/cotahist-fase04-normalizacao-2022-v1.yml`.
- O checkout esparso inclui os artefactos necessários, incluindo o caminho NORMALIZED, para evitar falhas de persistência LFS observadas no primeiro ciclo de 2021.
- Não iniciar a validação da FASE04 até existir evidência FASE03 VALIDADO/liberado.

### Roadmap operacional imediato
1. 2021: fechado e certificado.
2. 2022: FASE00–FASE02 VALIDADO.
3. FASE03: execução em curso.
4. FASE04: aguardar parsing; reconstruir NORMALIZED sem alterar RAW.
5. REC-001 B3 × BLOOMBERG_MAIL continua independente e bloqueada.

## 73. COTAHIST 2022 — FASE03 validada; FASE04 em execução (2026-10-13)

### FASE03 — Parsing estrutural
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2022_FASE03_PARSING_V1.json`, blob `11c33a2b058012453fb865f0fe6a48a55604c1ed`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482470145 — sucesso.
- Decisão: `LIBERADO_PARA_FASE04`.
- 2.117.440 registos de cotação, 245 bytes por registo; zero comprimentos/datas inválidos.
- Intervalo: 2022-01-03 a 2022-12-29. Parsing não certifica normalização.

### FASE04 — Normalização e reconciliação
**Estado: RUN EM EXECUÇÃO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase04-normalizacao-2022-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482555165.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2022_FASE04_NORMALIZACAO_V1.json`.
- O checkout esparso já inclui o CSV NORMALIZED para persistência LFS; o objetivo é reconstruir a camada NORMALIZED sem tocar no RAW.
- FASE05 e FASE06 estão preparadas e devem ser acionadas somente após a evidência FASE04 estar persistida e validada.

### Roadmap operacional imediato
1. FASE00–FASE03 (2022): VALIDADO.
2. FASE04: normalização em execução.
3. FASE05: verificar manifesto/checksum após FASE04.
4. FASE06: reconciliação semântica depois de FASE05.
5. Preservar RAW e todas as linhas; não deduplicar.

## 74. COTAHIST 2022 — FASE04 validada; FASE05 em fila (2026-10-13)

### FASE04 — Normalização e reconciliação
**Estado: VALIDADO — evidência e CSV persistidos.**

- Evidência: `dados/cotahist/quality/COTAHIST_2022_FASE04_NORMALIZACAO_V1.json`, blob `5d65cc7973b851c13100921719ea9df4ab402499`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482555165 — `completed / success`.
- Decisão: `LIBERADO_PARA_FASE05`; zero bloqueadores.
- NORMALIZED: 2.117.440 linhas, 25 campos; datas inválidas/fora de 2022: zero; intervalo 2022-01-03 a 2022-12-29.
- SHA-256 NORMALIZED calculado = manifesto = sidecar: `4e0e75d0bab794eeffdaa23990e3651810c3654b31e1b6bd3c53b9e4f72d8148`.
- SHA-256 RAW: `a4f9015b755f797d9c08b0d13f19dbfab18a6c75f379c0271a1cf1b5f6323cd8`.
- Manifesto histórico mantém `parser_version=1.1.0`; script canónico executado reportou `PARSER_VERSION=1.1.2`. A diferença está explicitamente registada na evidência, sem atualização silenciosa do manifesto.
- RAW inalterado; deduplicação não executada.

### FASE05 — Manifesto e checksum
**Estado: RUN ENFILEIRADO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase05-manifesto-checksum-2022-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482836300.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2022_FASE05_MANIFESTO_CHECKSUM_V1.json`.
- Verifica hashes físicos RAW/NORMALIZED contra manifesto, sidecar e FASE04; ZIP íntegro e contagens. FASE06 só após FASE05 validada.

### Roadmap operacional imediato
1. FASE00–FASE04 (2022): VALIDADO.
2. FASE05: enfileirada; confirmar evidência e hashes.
3. FASE06: preparada; executar após FASE05.
4. Nenhuma deduplicação; RAW e todas as linhas preservadas.

## 75. COTAHIST 2022 — FASE05 validada; FASE06 em fila (2026-10-13)

### FASE05 — Manifesto e checksum
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2022_FASE05_MANIFESTO_CHECKSUM_V1.json`, blob `f1d9c9323014c78a79b684142310a6db7686ae17`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482836300 — validação e persistência concluídas com sucesso.
- Decisão: `LIBERADO_PARA_FASE06`.
- SHA-256 RAW: `a4f9015b755f797d9c08b0d13f19dbfab18a6c75f379c0271a1cf1b5f6323cd8`.
- SHA-256 NORMALIZED: `4e0e75d0bab794eeffdaa23990e3651810c3654b31e1b6bd3c53b9e4f72d8148`.
- Manifesto/sidecar/hashes físicos concordantes; 2.117.440 linhas, 25 campos; RAW inalterado, deduplicação não executada.

### FASE06 — Reconciliação semântica
**Estado: RUN ENFILEIRADO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase06-reconciliacao-2022-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482955506.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2022_FASE06_RECONCILIACAO_V1.json`.
- Compara 12 campos críticos RAW × NORMALIZED em ordem original; só liberar FASE07 com zero divergências e hashes/contagens concordantes.

### Roadmap operacional imediato
1. FASE00–FASE05 (2022): VALIDADO.
2. FASE06: enfileirada; verificar evidência.
3. FASE07: executar após FASE06 sem divergências.
4. FASE08 V2 e Gate: usar exceções temporais explícitas, mantendo o diagnóstico original.
5. Preservar RAW e todas as linhas.

## 76. COTAHIST 2022 — FASE06 validada; FASE07 em fila (2026-10-13)

### FASE06 — Reconciliação semântica
**Estado: VALIDADO — evidência persistida.**

- Evidência: `dados/cotahist/quality/COTAHIST_2022_FASE06_RECONCILIACAO_V1.json`, blob `0316afea997420dcb54cffd8ae596e04d6d749a5`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38482955506 — validação concluída com sucesso.
- Decisão: `LIBERADO_PARA_FASE07`; divergências: 0.
- 2.117.440 registos RAW e NORMALIZED; hashes concordantes.
- 12 campos críticos reconciliados em ordem original; nenhuma linha removida/deduplicada.

### FASE07 — Identidade e cardinalidade
**Estado: RUN ENFILEIRADO; evidência pendente.**

- Workflow: `.github/workflows/cotahist-fase07-identidade-2022-v1.yml`.
- Run: https://github.com/carlos-andrade/B3/actions/runs/38483116402.
- Evidência esperada: `dados/cotahist/quality/COTAHIST_2022_FASE07_IDENTIDADE_CHAVES_V1.json`.
- Avalia chave-base e chave candidata com `prazot`; preservar todas as linhas e não deduplicar.
- FASE08 V2 e Gate 06–08 já estão preparados, aguardando FASE07 validada.

### Roadmap operacional imediato
1. FASE00–FASE06 (2022): VALIDADO.
2. FASE07: executar/verificar cardinalidade.
3. FASE08 V2: depois de FASE07, com exceções de ordenação explicitadas.
4. Gate 06–08 e FASE09: só após FASE08 V2 e Gate aprovados.

