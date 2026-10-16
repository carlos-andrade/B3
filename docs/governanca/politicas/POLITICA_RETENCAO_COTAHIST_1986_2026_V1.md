# POLÍTICA DE CICLO DE VIDA COTAHIST — HISTÓRICO FECHADO E ANO CORRENTE

| Campo | Valor |
|---|---|
| **ID** | B3-DOC-6A2DAA939ACB |
| **Projeto** | B3 — A BOLSA DO BRASIL |
| **Repositório** | [carlos-andrade/B3](https://github.com/carlos-andrade/B3) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | NORMALIZACAO_DOCUMENTAL |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 9a350693c200108e78ba2ad17e9334a80066a1e2e443f13226597fd91179f954|
| **Commit de referência (versão anterior)** | [3fac0651cae1370a22e493269dfc4bb91f3adaa8](https://github.com/carlos-andrade/B3/commit/3fac0651cae1370a22e493269dfc4bb91f3adaa8) |
| **Data de criação** | N/A — data original não identificada no ficheiro-base |
| **Data de atualização** | 2026-10-15 |
| **Responsável** | Manutenção técnica do projeto B3 |
| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |
| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |
| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | CARTA MAGNA → LAYOUT MESTRE → CONTRATOS/POLÍTICAS → IMPLEMENTAÇÃO → EVIDÊNCIAS |

**Versão:** 1.0  
**Data de decisão:** 2026-10-14  
**Projeto:** B3 — A Bolsa do Brasil  
**Repositório oficial:** https://github.com/carlos-andrade/B3  
**Estado:** VIGENTE

## 1. Decisão operacional

- **1986–2025: ENCERRADOS PARA INGESTÃO ROTINEIRA; DISPONÍVEIS APENAS PARA CONSULTA.**
- **2026: ANO CORRENTE; ATUALIZAÇÃO INCREMENTAL DIÁRIA.**
- O encerramento operacional do período histórico não representa, por si só, certificação semântica integral de todos os anos.

## 2. Regime de leitura para 1986–2025

Os dados, RAW, NORMALIZED, manifestos, checksums, evidências de qualidade, certificações e decisões históricas existentes devem ser tratados como um conjunto histórico de consulta e auditoria.

1. Não atualizar, substituir, regenerar ou promover dados históricos no ciclo rotineiro.
2. Não alterar RAW, NORMALIZED, manifestos, hashes ou evidências já persistidas.
3. Consultas, análises e backtests podem ler esses dados, respeitando as limitações e exceções documentadas de cada ano.
4. Um problema encontrado durante consulta deve ser registado como achado; não autoriza alteração silenciosa do histórico.
5. A matriz de certificação anual e o Dataset Oficial podem continuar a listar os anos históricos, mas os registos de 1986–2025 devem ser copiados da última versão oficial persistida, sem recalcular os seus metadados a partir de fontes históricas durante a rotina diária.
6. Qualquer reabertura futura de um ano histórico exige decisão explícita, escopo, motivo, evidência de origem, plano de impacto, versionamento e auditoria antes/depois. Sem essa autorização formal, o ano permanece somente para leitura.

## 3. Regime operacional para 2026

1. Atualizar diariamente quando houver nova fonte oficial disponível, sem inventar sessões nem dados ausentes.
2. Preservar o RAW de cada aquisição como imutável, com fonte, data/hora UTC de aquisição e SHA-256.
3. Executar normalização, reconciliação, validação de datas/calendário aplicável, contagens, hashes e persistência idempotente.
4. Atualizar manifestos, matriz anual, Dataset Oficial e evidências agregadas somente após validação bem-sucedida.
5. Manter registo explícito da data de corte; snapshots com cortes diferentes não são equivalentes.
6. Em falha ou divergência, manter a última versão validada, preservar evidências e sinalizar a atualização como não promovida.
7. A rotina de certificação e o Dataset Oficial devem recalcular apenas a linha/registo de 2026; as linhas/registos de 1986–2025 ficam congelados. Se faltar algum registo histórico previamente publicado, a rotina deve falhar fechado em vez de reconstruí-lo automaticamente.
8. **Não declarar 2026 fechado antes da fonte anual final, após 31/12/2026, e da conclusão das fases de validação e FASE12 aplicáveis.**

## 4. Limites de certificação

- O estado “encerrado para ingestão rotineira” significa congelamento operacional para preservar estabilidade e reprodutibilidade; não apaga exceções nem substitui a evidência de cada ano.
- **1986 mantém a exceção semântica histórica controlada.** Não declarar equivalência semântica plena de 1986–2025.
- Exceções de calendário, ordenação, regressão temporal, códigos e semântica permanecem documentadas e devem ser consideradas em qualquer utilização quantitativa.
- A certificação estrutural não equivale a certificação semântica, completude económica por sessão ou aptidão automática para estratégias.

## 5. Critérios de auditoria

Em cada atualização diária de 2026, auditar e persistir, conforme aplicável:

- origem e data de corte;
- SHA-256 do RAW e dos artefactos normalizados;
- contagens de linhas e campos;
- intervalo de datas e datas inválidas/fora do ano;
- reconciliação RAW × NORMALIZED e preservação da multiplicidade/ordem;
- coerência dos manifestos, matriz anual e Dataset Oficial;
- resultado dos workflows e tratamento explícito de falhas.

## 6. Regra de precedência

Esta política complementa o Roadmap Mestre e a certificação anual. Se um resumo antigo indicar reprocessamento rotineiro de anos anteriores a 2026, prevalece esta decisão de 14/10/2026: **1986–2025 somente consulta; 2026 atualização diária**. As limitações semânticas e os controlos de integridade continuam obrigatórios.

---
