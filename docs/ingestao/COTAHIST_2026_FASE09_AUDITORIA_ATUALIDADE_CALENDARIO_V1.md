# Registo histórico — COTAHIST 2026, FASE09: auditoria de atualidade e calendário oficial

| Campo | Valor |
|---|---|
| **ID** | B3-COTAHIST-FASE09-AUDITORIA-001 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | AUDITORIA_HISTORICA |
| **Fase** | COTAHIST 2026 — FASE09 |
| **Estado** | HISTORICO — consultar evidências pós-promoção para estado atual |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 279575c90574047bc49acf5c45b94b8981abfb448e1f0d5a99283406281b37ef |
| **Commit de referência (versão anterior)** | N/A — normalização inicial do cabeçalho |
| **Data de criação** | 2026-10-14 |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Responsável técnico do projeto B3 |
| **Aprovador** | Pendente — revisão documental; não constitui aprovação operacional atual |
| **Origem** | Evidências internas COTAHIST e calendário oficial B3 referenciados no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA 1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

> **AVISO DE ESTADO HISTÓRICO — 14/10/2026:** Esta auditoria descreve o NORMALIZED anterior, terminado em 23/09/2026. Após atualização do dataset, o manifesto e as evidências atuais indicam última data 13/10/2026, RAW SHA-256 `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e` e NORMALIZED SHA-256 `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`. Não usar a decisão de bloqueio abaixo como estado operacional atual. Consultar a auditoria pós-promoção [COTAHIST_2026_FASE11_AUDITORIA_POS_PROMOCAO_PARTE23_V1.md](COTAHIST_2026_FASE11_AUDITORIA_POS_PROMOCAO_PARTE23_V1.md) e o [roadmap PARTE23](../cotahist/ROADMAP_INGESTAO_PARTE23_ESTADO_2026-10-14.md). O conteúdo original foi preservado como histórico do estado anterior.

---

## COTAHIST 2026 — FASE09: auditoria de atualidade e calendário oficial

**Data da auditoria:** 2026-10-14  
**Repositório:** `carlos-andrade/B3`  
**Estado:** `BLOQUEADO_POR_DEFASAGEM_DO_DATASET`  
**Tipo:** auditoria documental e de atualidade; sem mutação dos dados.

## 1. Objetivo

Depois da validação técnica das FASE04–FASE08, verificar se o NORMALIZED 2026 continua atualizado face ao calendário oficial de negociação da B3 antes de prosseguir para novas fases.

## 2. Evidências internas verificadas

- Dataset: `dados/cotahist/normalized/anual/COTAHIST_A2026.csv`
- SHA-256 NORMALIZED: `befcf243540477cbae55b09231669b57d6bc84d6f91c96d8d71e32e14191e6c9`
- Registos: 2.919.760
- Primeira data: 2026-01-02
- Última data existente: **2026-09-23**
- FASE06: `VALIDADO`, 0 divergências RAW × NORMALIZED nos 25 campos.
- FASE07: `VALIDADO`, sem remoção de registos.
- FASE08: `VALIDADO_COM_EXCECAO`, sem bloqueios internos, mas sem calendário oficial persistido.

Fontes internas:
- [FASE06 — reconciliação](../../dados/cotahist/quality/COTAHIST_2026_FASE06_RECONCILIACAO_V1.json)
- [FASE07 — identidade e cardinalidade](../../dados/cotahist/quality/COTAHIST_2026_FASE07_IDENTIDADE_CHAVES_V1.json)
- [FASE08 — consistência temporal](../../dados/cotahist/quality/COTAHIST_2026_FASE08_SEMANTICA_CALENDARIO_V1.json)
- [Gate FASE06–FASE08](../../dados/cotahist/quality/COTAHIST_2026_GATE_06_08_V1.json)

## 3. Fonte oficial B3 e constatação de atualidade

A B3 publicou o [Calendário de negociação de 2026](https://www.b3.com.br/pt_br/noticias/calendario-de-negociacao-da-b3-confira-o-funcionamento-da-bolsa-em-2026.htm), com os dias sem negociação, incluindo 12/10/2026 (Nossa Senhora Aparecida).

A B3 confirmou em comunicado de **08/10/2026** que não haveria negociação na segunda-feira, **12/10/2026**, e que as atividades seriam retomadas normalmente na terça-feira, **13/10/2026**:
https://b3.com.br/pt_br/noticias/confira-o-funcionamento-da-b3-no-feriado-de-nossa-senhora-aparecida.htm

Comparação:
- Última sessão encontrada no NORMALIZED: **23/09/2026**.
- Última sessão de negociação confirmada pela fonte oficial consultada: **13/10/2026**.
- Diferença entre as datas: **20 dias corridos**.
- Logo, o dataset anual existente não cobre as sessões mais recentes confirmadas pela B3 e não pode ser tratado como atualizado a 14/10/2026.

## 4. Decisão

**FASE09: BLOQUEADA para certificação de atualidade e avanço para fases dependentes de cobertura recente.**

Motivo: o ficheiro NORMALIZED termina em 23/09/2026, enquanto a B3 confirmou negociação em 13/10/2026. A validação estrutural e a reconciliação RAW × NORMALIZED continuam válidas para o hash auditado, mas não demonstram atualidade da cobertura temporal.

## 5. Ações obrigatórias para desbloqueio

1. Consultar a fonte oficial de COTAHIST da B3 e obter a versão anual 2026 mais recente disponível.
2. Guardar o novo ficheiro RAW sem o sobrescrever silenciosamente; calcular e persistir SHA-256 e manifesto.
3. Normalizar para um novo artefacto versionado ou substituir o canónico apenas com histórico e cadeia de hashes auditável.
4. Reexecutar FASE04–FASE08 para o novo hash: integridade, manifesto/checksum, reconciliação dos 25 campos, identidade/cardinalidade e consistência temporal.
5. Reconciliar as datas observadas com o calendário oficial B3 e registar explicitamente qualquer exceção.
6. Só depois reabrir a certificação da FASE09 e permitir a fase seguinte.

## 6. Integridade e limites

- Nenhum ficheiro de dados foi alterado por esta auditoria.
- Nenhuma linha foi removida ou deduplicada.
- Não se presume que uma falha de cobertura temporal implique corrupção do conteúdo já reconciliado.
- O calendário de feriados é uma referência de sessões esperadas; não substitui a reconciliação dos dados COTAHIST.
- A aprovação anterior do gate 06–08 significa apenas que as evidências existentes passaram os critérios internos definidos. Não elimina a defasagem agora identificada.

## 7. Fontes

1. B3, *Calendário de negociação da B3: confira o funcionamento da bolsa em 2026*, 09/01/2026: https://www.b3.com.br/pt_br/noticias/calendario-de-negociacao-da-b3-confira-o-funcionamento-da-bolsa-em-2026.htm
2. B3, *Confira o funcionamento da B3 no feriado de Nossa Senhora Aparecida*, 08/10/2026: https://b3.com.br/pt_br/noticias/confira-o-funcionamento-da-b3-no-feriado-de-nossa-senhora-aparecida.htm
