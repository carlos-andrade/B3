# CONTRATOS DE EVIDÊNCIA — FASES 06–09 COTAHIST V1

**Data:** 2026-09-29  
**Escopo:** pipeline anual COTAHIST  
**Repositório:** `carlos-andrade/B3`  
**Status:** VIGENTE — CONTRATO DE EVIDÊNCIA

## 1. Finalidade

Formalizar o mínimo de evidência necessário para que as FASES 06, 07, 08 e 09 possam ser consideradas concluídas e, consequentemente, possam funcionar como pré-condições do gate independente da FASE10.

Este documento não reclassifica retroativamente nenhuma certificação. Evidência posterior não pode ser usada como prova automática de uma fase anterior.

## 2. Regra geral de evidência

Cada fase deve possuir, direta ou indiretamente por artefato equivalente explicitamente mapeado:

1. **identificação do ano**;
2. **entrada utilizada**;
3. **versão do procedimento/parser**, quando aplicável;
4. **checks executados**;
5. **quantidade de registros afetados**, quando aplicável;
6. **resultado esperado e resultado observado**;
7. **falhas/exceções**;
8. **hash/fingerprint**, quando aplicável;
9. **status final**;
10. **data/commit ou referência reprodutível**.

A existência de um CSV, manifesto ou FASE10 não satisfaz isoladamente este contrato.

## 3. Estados padronizados

- `VALIDADO`: todos os critérios obrigatórios passaram.
- `VALIDADO_COM_EXCECAO`: critérios passaram e toda exceção está identificada, delimitada e formalmente aceita.
- `PARCIAL`: existe evidência relacionada, mas falta requisito obrigatório.
- `BLOQUEADO`: pré-condição ausente ou falha impeditiva.
- `NAO_COMPROVADO`: não existe evidência específica suficiente no repositório.
- `NAO_APLICAVEL`: requisito formalmente fora do escopo.
- `EXCECAO_CONTROLADA`: somente para regras históricas previamente documentadas.

---

# 4. FASE 06 — RECONCILIAÇÃO

## Objetivo

Demonstrar que o produto normalizado corresponde à fonte RAW sob critérios quantitativos e/ou estruturais definidos.

## Entradas mínimas

- RAW anual;
- NORMALIZED anual;
- manifesto/checksum;
- especificação do parser;
- regra de correspondência entre RAW e NORMALIZED.

## Checks obrigatórios

1. correspondência de quantidade de registros aplicáveis;
2. correspondência de datas e registros de referência;
3. comparação de campos críticos;
4. comparação de OHLC;
5. comparação de quantidade/volume, quando presentes;
6. divergências classificadas;
7. exceções explicitamente preservadas.

## Evidência mínima

Um artefato versionado que contenha:

- ano;
- RAW hash;
- NORMALIZED hash;
- contagens;
- amostra ou fingerprint de comparação;
- divergências;
- exceções;
- decisão final.

## Critério de aprovação

`VALIDADO` ou `VALIDADO_COM_EXCECAO`, sem divergência não classificada.

## Bloqueios

- hashes ausentes quando exigidos;
- divergência não explicada;
- amostra incompatível;
- contagem incompatível sem justificativa formal.

---

# 5. FASE 07 — IDENTIDADE / CHAVES / CAMPOS

## Objetivo

Demonstrar que a identidade lógica dos registros e os campos estruturais essenciais foram interpretados de forma consistente.

## Entradas mínimas

- NORMALIZED;
- layout/especificação COTAHIST;
- regras de chave;
- regras de tipos e campos.

## Checks obrigatórios

1. chave lógica definida;
2. duplicidade segundo a chave avaliada;
3. campos obrigatórios;
4. comprimento/tipagem;
5. códigos estruturais relevantes;
6. campos que possam alterar a interpretação econômica do registro.

## Evidência mínima

Artefato contendo:

- definição da chave;
- cardinalidade;
- duplicidades;
- campos verificados;
- exceções;
- decisão final.

## Critério de aprovação

A chave deve ser determinística e as exceções devem ser explicitamente classificadas.

## Bloqueios

- chave não definida;
- duplicidades não explicadas;
- campo crítico truncado/corrompido;
- ambiguidade que altere a identidade econômica do registro.

---

# 6. FASE 08 — SEMÂNTICA / CALENDÁRIO / CONSISTÊNCIA

## Objetivo

Demonstrar que os registros fazem sentido dentro do domínio COTAHIST, incluindo calendário de pregão, códigos semânticos e relações entre campos.

## Entradas mínimas

- NORMALIZED;
- regras semânticas;
- calendário de referência aplicável;
- resultados das FASES 06 e 07.

## Checks obrigatórios

1. datas válidas;
2. datas dentro do ano;
3. coerência com calendário de pregão;
4. `TPMERC`;
5. `CODBDI`;
6. campos dependentes de código, inclusive `PRAZOT` quando aplicável;
7. relações OHLC;
8. quantidade/volume;
9. exceções históricas preservadas e classificadas.

## Evidência mínima

Artefato contendo:

- testes executados;
- contagens;
- datas de referência;
- códigos examinados;
- anomalias;
- classificação de exceções;
- decisão semântica.

## Critério de aprovação

`VALIDADO` ou `VALIDADO_COM_EXCECAO`. Exceção semântica não pode ser silenciosamente convertida em dado corrigido.

## Bloqueios

- código sem interpretação;
- calendário inconsistente sem explicação;
- exceção sem delimitação;
- transformação silenciosa de RAW;
- regra semântica que não possa ser reproduzida.

---

# 7. FASE 09 — PRÉ-RELEASE

## Objetivo

Consolidar as evidências 01–08 e decidir se o conjunto anual está apto a entrar no gate independente da FASE10.

## Entradas mínimas

- evidências 01–08;
- manifesto;
- hashes;
- NORMALIZED;
- regras de release;
- lista de exceções.

## Checks obrigatórios

1. todas as pré-condições anteriores estão presentes;
2. nenhum bloqueio aberto;
3. hashes coerentes;
4. contagens coerentes;
5. exceções listadas;
6. artefatos reproduzíveis;
7. estado de LFS, quando aplicável;
8. decisão explícita de release.

## Evidência mínima

`COTAHIST_<ANO>_FASE09_PRE_RELEASE_V1.json`, ou artefato equivalente formalmente mapeado, contendo:

- ano;
- referências das evidências 01–08;
- hashes;
- resultado de cada gate;
- exceções;
- decisão;
- versão do contrato.

## Critério de aprovação

Somente `LIBERADO_PARA_FASE10` quando todas as pré-condições obrigatórias estiverem satisfeitas.

## Bloqueios

Qualquer FASE 01–08 obrigatória ausente, `BLOQUEADO`, `NAO_COMPROVADO` ou com divergência não classificada.

---

# 8. Regra de equivalência retrospectiva

Para 1987–1993, um artefato antigo pode satisfazer este contrato somente se houver um **mapeamento explícito** demonstrando equivalência entre:

- teste executado;
- entrada;
- resultado;
- critério;
- exceções;
- rastreabilidade.

Não é permitido declarar equivalência apenas porque o resultado posterior foi `success`.

## 9. Relação com FASE10

A FASE10 continua sendo uma validação independente.

O novo contrato altera apenas a **pré-condição documental** da FASE10:

`FASES 01	ext{–}09 aprovadas ightarrow FASE10 liberada`

A FASE10 não pode retrocertificar FASES 06–09.

## 10. Regra de não-circularidade

Não usar como prova primária de uma fase:

- a própria evidência dessa fase;
- uma certificação posterior;
- a existência do NORMALIZED;
- o sucesso da FASE10;
- o sucesso da certificação anual.

Esses elementos podem ser referências complementares, nunca substitutos de evidência primária.

## 11. Versionamento

Qualquer alteração deste contrato deve:

1. incrementar a versão;
2. registrar a data;
3. explicar a mudança;
4. preservar a interpretação da versão anterior.

| Versão | Data | Alteração |
|---|---|---|
| 1.0 | 2026-09-29 | Contrato inicial das FASES 06–09. |
