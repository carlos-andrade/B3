# PLANO MESTRE DE EXECUÇÃO — B3

**Arquivo:** PLANO_MESTRE_DE_EXECUCAO.md  
**Projeto:** B3 — A BOLSA DO BRASIL  
**Caminho:** docs/PLANO_MESTRE_DE_EXECUCAO.md  
**Data de criação:** 25/09/2026  
**Repositório:** carlos-andrade/B3  
**Versão:** 1.0  
**Status:** VIGENTE

## 1. Objetivo

Concluir a construção de uma infraestrutura histórica e operacional da B3 baseada em dados rastreáveis, validados, reproduzíveis e auditáveis, sem permitir que um problema histórico localizado bloqueie a evolução do projeto.

## 2. Estratégia geral

O projeto seguirá cinco frentes em paralelo controlado:

1. Dados: ingestão, normalização e validação.
2. Qualidade: auditoria, reconciliação e certificação.
3. Automação: workflows e reprocessamento reproduzível.
4. Produto: datasets, índice e dashboard.
5. Governança: documentação, decisões e critérios de promoção.

A regra é: nenhuma frente pode mascarar uma falha de outra frente.

## 3. Fase imediata — estabilização da ingestão

### 3.1 Fechar o ciclo 2011–2026

Prioridade operacional:

- verificar execução dos workflows;
- eliminar falhas recorrentes;
- confirmar artefatos gerados;
- validar quantidade, estrutura e cobertura temporal;
- registrar resultados;
- deixar o processo reproduzível e automático.

### 3.2 Isolar 1986

O ano de 1986 deixa de ser bloqueador global.

Será mantido em trilha própria enquanto forem investigados:

- layout;
- TPMERC;
- CODBDI;
- semântica dos registros;
- campos numéricos;
- compatibilidade com o padrão histórico.

Se a evidência não for suficiente, 1986 permanecerá NÃO VALIDADO, sem contaminar os anos posteriores.

## 4. Fase de certificação dos dados

Para cada período:

RAW → PARSED → NORMALIZED → VALIDATED

Serão produzidos indicadores objetivos de:

- cobertura;
- registros;
- duplicidades;
- perdas;
- datas;
- instrumentos;
- códigos;
- consistência numérica;
- integridade estrutural;
- reconciliação semântica.

Cada resultado deverá possuir evidência auditável.

## 5. Fase de dataset oficial

Depois da validação:

- definir estrutura canônica;
- consolidar datasets;
- separar dados brutos de dados derivados;
- criar metadados;
- registrar versões;
- criar checksums quando aplicável;
- estabelecer snapshots reproduzíveis.

O dataset publicado deverá indicar claramente seu status de validação.

## 6. Fase de índice e dashboard

O index.html e o dashboard deverão consumir exclusivamente dados existentes no repositório.

Nenhum valor será inventado pela interface.

A interface deverá apresentar, quando aplicável:

- período disponível;
- cobertura;
- status de validação;
- quantidade de registros;
- última atualização;
- falhas ou ressalvas;
- links para evidências;
- datasets disponíveis.

## 7. Fase de auditoria final

Executar uma auditoria transversal:

### Dados
- completude;
- duplicidade;
- continuidade;
- consistência.

### Semântica
- códigos;
- campos;
- períodos;
- mudanças de layout.

### Pipeline
- reprodutibilidade;
- automação;
- falhas;
- artefatos.

### Git
- histórico;
- commits;
- versões;
- rastreabilidade.

### Produto
- dashboard;
- índice;
- consumo dos dados;
- ausência de dados fictícios.

## 8. Fase de pesquisa quantitativa

Somente após a base histórica atingir o nível de validação adequado:

- séries temporais;
- retornos;
- volatilidade;
- volume financeiro;
- liquidez;
- gaps;
- VWAP/TWAP quando houver dados compatíveis;
- microestrutura quando houver dados intradiários;
- estudos de regime;
- backtests.

Dados inadequados para determinada análise deverão ser explicitamente classificados como inadequados para esse uso.

## 9. Ordem de prioridade

### P0 — Bloqueadores
- workflows quebrados;
- dados corrompidos;
- perda silenciosa;
- inconsistência estrutural;
- pipeline não reproduzível.

### P1 — Base oficial
- 2011–2026;
- normalização;
- validação;
- dataset canônico.

### P2 — Histórico legado
- 1986 e demais períodos com particularidades;
- resolução ou classificação formal das exceções.

### P3 — Produto
- índice;
- dashboard;
- documentação navegável.

### P4 — Pesquisa
- estudos quantitativos;
- microestrutura;
- estratégias;
- backtests.

## 10. Regra de avanço

Não esperaremos a resolução de todos os problemas históricos para avançar.

Um problema só bloqueará o projeto quando houver evidência de que ele contamina uma etapa posterior.

Assim:

problema localizado → isolamento → classificação → continuidade do projeto

e não:

problema localizado → paralisação total.

## 11. Próximo passo operacional

A próxima execução deverá ser uma auditoria de estado do repositório, verificando:

1. workflows ativos;
2. últimos runs e falhas;
3. artefatos produzidos;
4. anos disponíveis;
5. anos validados;
6. anos não validados;
7. estrutura atual de dados;
8. situação específica de 1986;
9. estado do index.html;
10. estado do dashboard.

Depois dessa fotografia, será definido o próximo bloco de execução sem repetir trabalho já concluído.

## 12. Critério de conclusão da etapa atual

A etapa de ingestão será considerada estabilizada quando:

- os workflows principais executarem automaticamente;
- falhas conhecidas estiverem classificadas;
- 2011–2026 tiverem cobertura e validação documentadas;
- 1986 estiver isolado caso permaneça inconclusivo;
- os datasets possuírem status explícito;
- os resultados forem reproduzíveis;
- a documentação estiver sincronizada com o estado real do repositório.

---

Regra-mestra: avançar continuamente, mas nunca transformar dado não validado em dado confiável apenas para acelerar o projeto.


## 13. Atualização de governança — 2026-10-01

A execução histórica do projeto passou a adotar um contrato explícito de execução linear e fail-closed para o COTAHIST.

A cadeia anual de referência é:

**00 → 01 → 02 → 03–05 → 06 → 07 → 08 → GATE → 09 → GATE → 10 → GATE → 11 → GATE → 12 → transição.**

A existência de RAW não implica necessidade de nova aquisição. O repositório deve ser consultado pelo caminho canônico antes de qualquer tentativa de download ou duplicação.

A série anual 1986–2026 possui RAW presente na matriz de certificação atual. O próximo ciclo operacional após o fechamento de 1994 é 1995, cujo RAW já existe no caminho canônico.

O objetivo operacional agora é executar 1995 usando os artefatos existentes, sem reaquisição desnecessária, preservando a mesma disciplina linear aplicada a 1994.

### 13.1 Regra anti-repetição

Antes de criar ou baixar qualquer artefato:

1. consultar o caminho canônico;
2. consultar manifesto;
3. consultar checksum;
4. consultar evidências existentes;
5. consultar matriz de certificação;
6. somente então decidir se existe lacuna real.

### 13.2 Estado de referência

- 1994: FECHADO / TRANSIÇÃO PARA 1995 AUTORIZADA.
- 1995: RAW PRESENTE / PRÓXIMO CICLO.
- 1996+: NÃO INICIAR ATÉ FECHAMENTO FORMAL DE 1995.
- 1986: EXCEÇÃO HISTÓRICA CONTROLADA.



## Aditivo de execução — 2026-10-01 — prevenção de regressão

O incidente da FASE06/1995 mostrou que a existência de certificações anteriores não impede a introdução de uma regra nova incorreta. Portanto, antes de criar ou alterar um gate, deve-se consultar certificações, incidentes, contratos de chaves e evidências históricas.

A responsabilidade foi separada: FASE06 valida semântica e invariantes; FASE07 valida identidade, chaves e cardinalidade. Uma duplicidade de chave candidata observada em FASE06 é evidência para FASE07, não reprovação automática da FASE06.

## REGRA ESTRUTURAL — ISOLAMENTO, MONOTONICIDADE E IMUTABILIDADE DAS FASES — 2026-10-01

As fases do COTAHIST são **monotônicas e isoladas**.

### Regra 1 — uma fase não retorna para fase anterior
Uma fase N não pode reabrir, recalcular, substituir, corrigir ou alterar a evidência normativa da fase N-1 ou de qualquer fase anterior. Se uma inconsistência anterior for descoberta, ela deve ser tratada como **incidente de governança/correção versionada da própria fase afetada**, sem transformar a fase posterior em responsável por ela.

### Regra 2 — uma fase não executa responsabilidade de fase posterior
Uma fase N não pode antecipar critérios pertencentes à fase N+1. Em especial:
- FASE06 não decide unicidade/cardinalidade de chave;
- FASE07 não reescreve a semântica certificada da FASE06;
- FASE08 não redefine identidade da FASE07;
- FASE09–12 não substituem os gates técnicos anteriores.

### Regra 3 — correção permanece na fase de origem
Se uma regra da FASE06 estiver errada, corrige-se a FASE06. Não se cria uma correção da FASE07 para mascarar a FASE06. Se uma regra da FASE07 estiver errada, corrige-se a FASE07.

### Regra 4 — dependência é somente leitura
Uma fase posterior pode **consumir** a evidência autorizada da fase anterior e os dados-fonte necessários à sua própria análise, mas não pode alterá-los nem reinterpretar silenciosamente o estado certificado da fase anterior.

### Regra 5 — promoção é unidirecional
O fluxo é exclusivamente:

**N-1 → N → N+1**

Não existe fluxo operacional **N+1 → N-1** nem **N → N+1 com responsabilidade de N+1 executada dentro de N**.

### Regra 6 — novo teste não retrocertifica
Uma fase posterior pode detectar um incidente com impacto potencial em fase anterior. Isso gera um **registro de impacto e revisão controlada**, não uma reexecução silenciosa nem uma alteração retroativa da evidência histórica.

### Regra 7 — gatilhos não podem quebrar a monotonicidade
Workflows de uma fase concluída não devem ser disparados por alterações genéricas de documentação, README ou artefatos de fases posteriores. O gatilho deve refletir somente a própria fase e suas entradas autorizadas.

### Matriz de responsabilidade

| Fase | Responsabilidade própria | Não pode assumir |
|---|---|---|
| 00 | governança/pré-condições | validação técnica posterior |
| 01 | aquisição/RAW | integridade semântica |
| 02 | integridade da fonte | parsing/normalização |
| 03 | parsing | normalização/identidade |
| 04 | normalização | identidade/semântica posterior |
| 05 | manifesto/checksum | semântica/chaves |
| 06 | semântica/invariantes | identidade/cardinalidade FASE07 |
| 07 | identidade/chaves/cardinalidade | reescrever FASE06 |
| 08 | semântica/calendário/consistência | reabrir identidade |
| 09 | pré-release | corrigir fases anteriores |
| 10 | validação independente | substituir evidências anteriores |
| 11 | certificação/promoção | refazer fases técnicas silenciosamente |
| 12 | fechamento/transição | certificar o próximo ano |

**Regra de governança:** descobrir algo numa fase posterior não autoriza essa fase a executar o trabalho de uma fase anterior.



## Aditivo normativo — GATE 06–08 — 2026-10-01

O projeto passa a reconhecer o **GATE 06–08 — PROMOÇÃO TÉCNICA** como barreira formal entre FASE08 e FASE09. O contrato específico está em 'docs/cotahist/CONTRATO_GATE_06_08_PROMOCAO_TECNICA_V1.md'.

O Gate não é fase técnica e não pode corrigir, reexecutar ou substituir FASE06, FASE07 ou FASE08. Ele somente verifica as evidências dessas três fases, os estados permitidos, o ano/ciclo, exceções, bloqueadores e o isolamento de responsabilidades.

A promoção é **fail-closed**: somente 'LIBERADO_PARA_FASE09' quando todas as condições obrigatórias forem satisfeitas; qualquer ausência, estado inválido ou condição indeterminada produz 'BLOQUEADO_PARA_FASE09'.

Correções permanecem na fase de origem. README e documentação genérica não são fontes operacionais do Gate e não podem provocar reexecução retroativa de fases concluídas.


## Aditivo — execução independente e retorno verificável — 2026-10-01

O contrato geral está em docs/governanca/CONTRATO_RETORNO_E_MONITORAMENTO_EXECUCOES_B3_V1.md.

Cada workflow deve operar como unidade independente, sem chamar ou reexecutar outro workflow. Dependências entre fases são exclusivamente direcionais e baseadas em evidências autorizadas.

Cada execução deve registrar no GITHUB_STEP_SUMMARY: workflow, fase/tarefa, run, entrada, evidência, status, decisão, bloqueadores, exceções, commit, próxima ação e indicação de reexecução.

O monitor permanente .github/workflows/b3-monitor-execucoes-v1.yml verifica execuções a cada 15 minutos e não dispara reexecuções. Seu objetivo é detectar FAVORÁVEL, NÃO_FAVORÁVEL ou EM_EXECUÇÃO.

A decisão de reexecutar deve ser baseada em mudança real da entrada, correção pendente ou alteração normativa aplicável. Sucesso, falha já registrada ou alteração de documentação não autorizam reexecução por si só.


---

## FONTE NORMATIVA CANÔNICA — 2026-10-01

Este documento é **derivado/operacional** e não constitui fonte independente para geração de código. As regras executáveis devem ser reconciliadas com:

`docs/governanca/LAYOUT_MESTRE_CANONICO_B3_V1.md`

**Regra:** Layout Mestre → especificação da tarefa → código/workflow → evidência.

Se houver divergência, o Layout Mestre prevalece até reconciliação e versionamento formal.