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
