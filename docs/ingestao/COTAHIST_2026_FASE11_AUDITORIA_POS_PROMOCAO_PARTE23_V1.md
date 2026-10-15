# COTAHIST 2026 — Auditoria pós-promoção integrada — PARTE23

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-E40498209574 |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | RELATORIO_DE_AUDITORIA |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 598c3986946d38061b9f6e8a6875598b271844233332eb3d6d8cc7329279efa1 |
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Data:** 2026-10-14  
**Repositório:** `carlos-andrade/B3`  
**Branch auditada:** `main`  
**Tipo:** leitura cruzada de evidências persistidas; sem mutação de dados  
**Resultado:** `APROVADO_COM_EXCECOES_DOCUMENTADAS`  
**Escopo:** coerência entre RAW, NORMALIZED, FASE04–FASE11 e atualidade do dataset

## 1. Resultado executivo

A auditoria cruzou os manifestos e as evidências atuais do branch `main`. Os hashes RAW/NORMALIZED coincidem entre manifestos, sidecars e evidências centrais. A FASE06 reporta zero divergências; FASE07 não removeu linhas; FASE08 mantém exceções explicitamente não bloqueadoras; FASE09 liberou para FASE10; FASE10 validou o candidato sem diferenças de linhas; FASE11 registou a promoção controlada.

O dataset NORMALIZED contém 3.142.910 registos de cotação, 25 campos e cobre 2026-01-02 a 2026-10-13. A evidência anterior de defasagem, que terminava em 2026-09-23, ficou obsoleta após a atualização do dataset em 14/10/2026.

**Limite importante:** esta é uma auditoria cruzada de evidências persistidas, não uma nova leitura byte a byte de todo o CSV de 422 MB nesta sessão, nem uma nova execução dos workflows. Os resultados de reconciliação integral são os reportados pelas evidências de FASE06 e FASE10.

## 2. Identidade dos artefactos canónicos

| Elemento | Resultado |
|---|---|
| RAW | `dados/cotahist/raw/anual/COTAHIST_A2026.ZIP` |
| SHA-256 RAW | `580d3b0bc768ef86c4b1afdd6d08eb05bae76f21db04f8cbc636d5bec54cdd7e` |
| NORMALIZED | `dados/cotahist/normalized/anual/COTAHIST_A2026.csv` |
| SHA-256 NORMALIZED | `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc` |
| Linhas NORMALIZED | 3.142.910 |
| Campos | 25 |
| Primeira data | 2026-01-02 |
| Última data observada | 2026-10-13 |
| Datas inválidas / fora do ano | 0 / 0 |
| Datas de negociação distintas (FASE08) | 195 |

### Verificação de hashes

- Manifesto RAW: `sha256` igual ao hash RAW acima.
- Sidecar RAW: igual ao hash RAW acima.
- Manifesto NORMALIZED: `raw_sha256` e `normalized_sha256` iguais aos hashes correspondentes.
- Sidecar NORMALIZED: igual ao hash NORMALIZED acima.
- FASE04, FASE05, FASE06, FASE07, FASE08, Gate 06–08, FASE09, FASE10 e FASE11 referenciam o mesmo hash NORMALIZED quando esse campo existe.

## 3. Matriz de evidências

| Fase/artefacto | Estado observado | Resultado relevante | Conclusão da auditoria |
|---|---|---|---|
| FASE04 | `VALIDADO` | RAW/NORMALIZED com hashes canónicos; última data 13/10; sem datas inválidas/fora do ano | Coerente |
| FASE05 | `VALIDADO` | Manifestos e sidecars RAW/NORMALIZED coerentes | Coerente |
| FASE06 | `VALIDADO` | 3.142.910 linhas RAW e NORMALIZED; zero divergências; 25 campos | Coerente |
| FASE07 | `VALIDADO` | 3.142.910 registos; hash de origem coincide; zero linhas removidas; deduplicação não executada | Coerente |
| FASE08 | `VALIDADO_COM_EXCECAO` | Zero bloqueadores; 195 datas; última data 13/10; regressões temporais por instrumento documentadas | Aprovado com exceções |
| Gate 06–08 | `APROVADO_COM_EXCECOES_NAO_BLOQUEANTES` | Decisão `LIBERADO_PARA_FASE09`; contagem e hash NORMALIZED coincidem | Aprovado com exceções |
| FASE09 | `LIBERADO_PARA_FASE10` | Ausências e bloqueadores vazios; hashes RAW/NORMALIZED atuais | Liberado |
| FASE10 | `VALIDADO_SEM_DIFERENCAS_DE_LINHAS` | 3.142.910 linhas em ambos; zero adicionadas/ausentes; multiconjunto integral igual; reconciliação dos 25 campos | Candidato validado |
| FASE11 | `PROMOVIDO_COM_HASHES_COHERENTES` | Hashes canónicos iguais; 3.142.910 linhas; sem deduplicação | Promoção registada |

## 4. Exceções preservadas

A FASE08 identifica:
- regressões da sequência física da fonte;
- regressões temporais por instrumento;
- métricas de ordenação lexicográfica não exigidas pelo contrato;
- ausência de calendário oficial histórico persistido na evidência original.

O Gate 06–08 classifica as exceções como não bloqueadoras para a consistência interna, com zero bloqueadores. A auditoria não reordena nem remove registos. A ausência de calendário oficial persistido deve continuar como limitação documental a resolver, sem invalidar retroativamente a reconciliação dos campos.

## 5. Atualidade e auditoria documental anterior

A evidência antiga `docs/ingestao/COTAHIST_2026_FASE09_AUDITORIA_ATUALIDADE_CALENDARIO_V1.md` apontava última data 2026-09-23 e hash NORMALIZED diferente. O manifesto atual e as evidências posteriores apontam última data 2026-10-13 e hash `e7763b6fa5e40acfed5e58b5dde65fe276a2def7ff43bdc160de34b871f4cbdc`.

Conclusão: a auditoria anterior permanece válida como registo histórico do estado que avaliou, mas está obsoleta como descrição do estado atual. Esta nota constitui a evidência de atualização documental; não apagar nem alterar o histórico.

A data 2026-10-13 é a última data observada no dataset verificado, não uma garantia de atualidade futura. Se a B3 publicar uma atualização posterior, o RAW deve ser reavaliado e as fases dependentes reexecutadas.

## 6. Limites e ações seguintes

1. Confirmar no painel de Actions que os workflows que produziram as evidências atuais terminaram com sucesso; esta auditoria não substitui os logs dos runs.
2. Atualizar a documentação central de estado para apontar para esta auditoria e marcar a auditoria de 23/09 como histórica.
3. Manter as exceções FASE08 documentadas e não deduplicar.
4. Monitorizar a próxima publicação oficial; ao mudar o RAW, reabrir FASE04–FASE09, repetir validação independente e promoção controlada.
5. Não declarar o fecho anual de 2026 antecipadamente.

## 7. Referências

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

---
**Estado final desta auditoria:** `APROVADO_COM_EXCECOES_DOCUMENTADAS` — evidências e hashes coerentes; exceções não bloqueadoras preservadas; auditoria documental antiga supersedida para fins de estado atual.
