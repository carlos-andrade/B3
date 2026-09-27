# CERTIFICAÇÃO GLOBAL DOS DADOS B3 — FECHAMENTO 2026-09-27

**Arquivo:** CERTIFICACAO_DOMINIOS_B3_2026-09-27.md  
**Projeto:** B3 - A Bolsa do Brasil  
**Caminho:** governanca/garantia_atualizacao_dados/CERTIFICACAO_DOMINIOS_B3_2026-09-27.md  
**Data de criação:** 27/09/2026  
**Repositório:** carlos-andrade/B3

## 1. Objetivo

Este documento fecha a auditoria de certificação dos domínios identificados na Matriz Global de Frescor.

A regra é FAIL-CLOSED: nenhum domínio pode receber o estado CERTIFICADO apenas porque existe um workflow, porque uma fonte pública responde ou porque uma execução de CI terminou com sucesso. A certificação exige evidência persistida, integridade, data de referência, origem, normalização e rastreabilidade.

## 2. Estado consolidado

| Domínio | Estado em 27/09/2026 | Evidência |
|---|---|---|
| COTAHIST diário 2026 | CERTIFICADO | Manifestos VALIDADO até 25/09/2026 |
| COTAHIST dataset corrente 2026 | CERTIFICADO | Índice oficial corrente V1.1; snapshot anual + incrementos 23/09–25/09 |
| COTAHIST histórico 1987–2025 | CONDICIONAL | Cobertura histórica existente, sujeita à validação anual por ano |
| COTAHIST 1986 | EXCEÇÃO HISTÓRICA NÃO CERTIFICÁVEL | Fase 09C encerrada como exceção documentada; não inventar observações ausentes |
| Copom 281 | CERTIFICADO | RAW + metadados + NORMALIZED persistidos; evento e data de publicação reconciliados |
| BCB/SGS núcleo macro | CERTIFICADO | SGS 432/11/12/1/433; manifesto geral VALIDADO; execução #5; índice oficial V1.0 |
| Índices B3 | NÃO CERTIFICADO | Fonte oficial atual identificada, mas falta captura/manifesto persistido e reconciliação no repositório |
| Carteiras B3 | NÃO CERTIFICADO | Carteira definitiva de setembro/2026 identificada na fonte B3, mas falta evidência persistida no repositório |
| Derivativos/futuros/opções | NÃO CERTIFICADO | Contratos e contrato de ingestão definidos, mas não há evidência suficiente de dataset corrente certificado |
| Fluxo/mercado intraday | NÃO CERTIFICADO | Contrato definido para WIN/WDO/DI, mas falta camada de dados e evidência corrente |
| Garantia global B3 | NÃO CERTIFICADA | Bloqueada pelos domínios acima |

## 3. Certificações efetivamente fechadas

### 3.1 COTAHIST

O dataset corrente 2026 é composto de:

- snapshot anual oficial encerrado em 22/09/2026;
- incremento diário VALIDADO de 23/09/2026;
- incremento diário VALIDADO de 24/09/2026;
- incremento diário VALIDADO de 25/09/2026.

O snapshot anual permanece imutável. O índice corrente é a camada de consumo atual.

Evidências principais:

- dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json
- dados/cotahist/normalized/manifests/diario/COTAHIST_D23092026_quality.json
- dados/cotahist/normalized/manifests/diario/COTAHIST_D24092026_quality.json
- dados/cotahist/normalized/manifests/diario/COTAHIST_D25092026_quality.json

Última observação corrente certificada: 25/09/2026.

### 3.2 BCB/SGS núcleo macro

O núcleo macro foi certificado em 27/09/2026. Evidência principal: `dados/bcb_sgs/oficial/BCB_SGS_DATASET_ATUAL_V1.0.json`.

- SGS 432: VALIDADO, última data 27/09/2026;
- SGS 11: VALIDADO, última data 25/09/2026;
- SGS 12: VALIDADO, última data 24/09/2026;
- SGS 1: VALIDADO, última data 25/09/2026;
- SGS 433/IPCA: VALIDADO, última data 01/08/2026, 560 observações.

O IPCA teve quatro duplicidades de borda na captura bruta entre chunks. O RAW foi preservado integralmente; a normalização passou a ignorar registros fora da janela solicitada. O manifesto final registra zero duplicidades.

### 3.3 Copom 281

A captura persistida contém RAW, metadados de captura e NORMALIZED.

Registro normalizado:

- reunião: 281;
- reunião: 15–16/09/2026;
- publicação: 22/09/2026;
- decisão: Selic 13,75% a.a.;
- origem: Banco Central do Brasil;
- fonte da API: https://www.bcb.gov.br/api/servico/sitebcb/copom.

A captura de 25/09/2026 possui SHA-256 nos metadados RAW e conteúdo normalizado correspondente.

## 4. Domínios que permanecem bloqueados

### 4.1 BCB — séries fora do núcleo certificado

Não é permitido transformar a existência do Copom em certificação de todo o BCB.

Para cada série BCB será necessário registrar:

1. código da série;
2. nome;
3. unidade;
4. frequência;
5. fonte oficial;
6. última data disponível na fonte;
7. última data armazenada;
8. timestamp de captura;
9. SHA-256 RAW;
10. SHA-256 NORMALIZED;
11. número de observações;
12. lacunas;
13. duplicidades;
14. status de validação;
15. evidência de workflow.

### 4.2 Índices e carteiras B3

A B3 informou oficialmente que a carteira definitiva do Ibovespa válida de 08/09/2026 a 31/12/2026 possui 76 ativos de 74 empresas. A página oficial também informa que os índices são rebalanceados quadrimestralmente.

Isso constitui evidência externa da fonte, mas não constitui, por si só, certificação do dataset do repositório.

A certificação somente ocorrerá depois de persistidos o arquivo oficial, metadados, hash, data de referência e manifesto de qualidade.

### 4.3 Derivativos, futuros e opções

O contrato de ingestão existente para WIN, WDO e DI não é evidência de que a camada de dados corrente esteja certificada.

A certificação exige dataset efetivamente capturado, normalizado e auditado.

## 5. Regra para o histórico 1986–2025

1986 permanece uma exceção histórica formal.

A decisão operacional registrada anteriormente é mantida:

- não fabricar registros;
- não interpolar pregões ausentes;
- não usar reconstrução observacional como dado oficial;
- manter a evidência da busca;
- permitir que os anos posteriores avancem independentemente.

Portanto, 1986 não deve bloquear a evolução dos demais anos, mas também não pode ser rotulado como completo.

## 6. Critério de encerramento da garantia global

A garantia global somente poderá mudar para CERTIFICADA quando todos os seguintes grupos tiverem estado CERTIFICADO:

1. COTAHIST corrente;
2. histórico COTAHIST dentro do escopo declarado;
3. Copom;
4. núcleo BCB/SGS obrigatório e demais séries BCB definidas no inventário;
5. índices B3;
6. carteiras B3;
7. derivativos/futuros/opções;
8. demais datasets definidos no inventário oficial do projeto.

Qualquer ausência crítica mantém o estado global em NÃO CERTIFICADA.

## 7. Regra de confiança

WORKFLOW VERDE NÃO É SINÔNIMO DE DADO FRESCO.

A confiança deve ser derivada da evidência do dado, não da execução da automação.

Um domínio só pode ser certificado quando:

SOURCE_DATE >= LAST_REQUIRED_DATE

STORED_DATE >= SOURCE_DATE

RAW_HASH = VALID

NORMALIZED_HASH = VALID

QUALITY_STATUS = VALIDADO

NO_CRITICAL_GAPS = TRUE

WORKFLOW_EVIDENCE = PRESENT

## 8. Conclusão

A auditoria foi concluída sem promover artificialmente domínios incompletos para CERTIFICADO.

Neste fechamento, COTAHIST corrente e Copom estão efetivamente certificados. Os demais domínios permanecem explicitamente bloqueados até que seus dados sejam capturados e auditados.

Esta separação é obrigatória para impedir que backtests, dashboards e estudos quantitativos consumam dados com frescor ou cobertura não comprovados.
